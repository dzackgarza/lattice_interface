from __future__ import annotations

import os
import signal
import subprocess
import threading
from abc import ABC, abstractmethod
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from plumbum import local
from pydantic import BaseModel, ConfigDict

from . import config
from .agent_errors import classify_usage_limit
from .errors import (
    AgentConnectivityError,
    AgentMetadataError,
    AgentTimeoutError,
    RateLimitUsageError,
)
from .tasks import AgentTask

TIMEOUT_SECONDS = int(os.environ.get("AGENT_RUNNER_TIMEOUT_SECONDS", "900"))  # 15 minutes default


@dataclass(frozen=True)
class RunContext:
    run_id: str
    task_name: str
    agent_name: str
    run_dir: Path
    stdout_path: Path
    transcript_path: Path
    metadata_path: Path
    summary_path: Path


@dataclass(frozen=True)
class ProcessResult:
    exit_code: int
    stdout: str
    last_message_path: Path | None = None


class AgentInterface(BaseModel, ABC):
    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str
    binary: str
    subcommand: str | None
    base_args: list[str]
    env: Mapping[str, str]
    quality: int

    def run_task(
        self, task: AgentTask, run_ctx: RunContext, timeout_seconds: int = TIMEOUT_SECONDS
    ) -> ProcessResult:
        result = self._run_with_prompt(task.prompt_text(), task, run_ctx, timeout_seconds)
        classified = classify_usage_limit(self.name, result.stdout)
        if classified:
            raise RateLimitUsageError(self.name, classified.message)
        return result

    def check_connectivity(self, run_ctx: RunContext) -> None:
        hello_task = AgentTask(
            name="preflight_hello",
            task_key="preflight_hello",
            prompt_path=config.settings.debug_prompts()["smoke"],
            requires_commit=False,
        )
        result = self._run_with_prompt(
            hello_task.prompt_text(), hello_task, run_ctx, timeout_seconds=30
        )
        classified = classify_usage_limit(self.name, result.stdout)
        if classified:
            raise AgentConnectivityError(self.name, classified.message)
        if result.exit_code != 0:
            raise AgentConnectivityError(self.name, f"exit code {result.exit_code}")

    @abstractmethod
    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        raise NotImplementedError

    def _build_env(self) -> dict[str, str]:
        return {"PATH": self.env.get("PATH", "")}

    def _run_command(
        self,
        args: list[str],
        prompt_string: str,
        run_ctx: RunContext,
        cwd: Path | None = None,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        env = {**os.environ, **self._build_env()}
        final_args = [self.binary, *args, prompt_string]
        chunks: list[bytes] = []
        timed_out = False

        try:
            proc = subprocess.Popen(
                final_args,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=cwd,
                env=env,
                start_new_session=True,
            )
        except FileNotFoundError:
            msg = f"Binary not found: {self.binary}"
            raise AgentMetadataError(msg) from None

        with run_ctx.transcript_path.open("wb") as live_log:

            def read_output():
                assert proc.stdout is not None
                for line in iter(proc.stdout.readline, b""):
                    try:
                        live_log.write(line)
                        live_log.flush()
                    except ValueError:
                        pass  # live_log closed during forced shutdown; chunks still captured
                    chunks.append(line)

            reader_thread = threading.Thread(target=read_output)
            reader_thread.start()
            reader_thread.join(timeout=timeout_seconds)

            if reader_thread.is_alive():
                timed_out = True
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
                reader_thread.join(timeout=5)
                if reader_thread.is_alive():
                    os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
                    reader_thread.join(timeout=2)

        if timed_out:
            raise AgentTimeoutError(self.name, run_ctx.task_name, timeout_seconds)

        # Invariant: only reachable when the process completed within TIMEOUT_SECONDS.
        # A timed-out process always raises above; proc.wait() is never called on a killed process.
        assert not timed_out
        exit_code = proc.wait()
        combined = b"".join(chunks).decode("utf-8", errors="replace")
        return ProcessResult(exit_code=exit_code, stdout=combined)


class CodexAgent(AgentInterface):
    quality: int = 90

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        last_message = run_ctx.run_dir / "last_message.txt"
        args = [
            "--config",
            'model_reasoning_effort="high"',
            "--search",
            self.subcommand or "exec",
            "-C",
            str(config.settings.repo_root),
            "--sandbox",
            "workspace-write",
            "--full-auto",
            "--ephemeral",
            "-o",
            str(last_message),
        ]
        if task.name == "document_test_alignment":
            mcp_cmd = local[self.binary]["mcp", "get", "serena"]
            retcode, _, _ = mcp_cmd.run(_env=self._build_env(), retcode=None)
            if retcode != 0:
                msg = "MCP server 'serena' not configured for codex"
                raise AgentMetadataError(msg)
        result = self._run_command(
            args=args, prompt_string=prompt_string, run_ctx=run_ctx, timeout_seconds=timeout_seconds
        )
        return ProcessResult(
            exit_code=result.exit_code,
            stdout=result.stdout,
            last_message_path=last_message,
        )


class ClaudeAgent(AgentInterface):
    quality: int = 80

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,  # noqa: ARG002
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        args = [
            "-p",
            "--model",
            "sonnet",
            "--effort",
            "high",
            "--dangerously-skip-permissions",
            "--no-session-persistence",
        ]
        return self._run_command(
            args=args,
            prompt_string=prompt_string,
            run_ctx=run_ctx,
            cwd=config.settings.repo_root,
            timeout_seconds=timeout_seconds,
        )


class GeminiAgent(AgentInterface):
    quality: int = 40

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,  # noqa: ARG002
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        args = [
            "--model",
            config.settings.gemini_model,
            "--output-format",
            "json",
            "--prompt",
        ]
        return self._run_command(
            args=args, prompt_string=prompt_string, run_ctx=run_ctx, timeout_seconds=timeout_seconds
        )


class OllamaAgent(AgentInterface):
    quality: int = 50

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,  # noqa: ARG002
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        model = os.environ.get("OLLAMA_MODEL", "minimax-m2.5:cloud")
        args = [
            "launch",
            "claude",
            "--model",
            model,
            "--",
            "-p",
            "--dangerously-skip-permissions",
            "--no-session-persistence",
        ]
        return self._run_command(
            args=args,
            prompt_string=prompt_string,
            run_ctx=run_ctx,
            cwd=config.settings.repo_root,
            timeout_seconds=timeout_seconds,
        )


class KiloAgent(AgentInterface):
    quality: int = 70

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,  # noqa: ARG002
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        args = [
            "run",
            "--auto",
            "-m",
            "kilo/minimax/minimax-m2.5:free",
        ]
        return self._run_command(
            args=args,
            prompt_string=prompt_string,
            run_ctx=run_ctx,
            cwd=config.settings.repo_root,
            timeout_seconds=timeout_seconds,
        )


class OpencodeAgent(AgentInterface):
    quality: int = 60

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,  # noqa: ARG002
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        model = os.environ.get("OPENCODE_MODEL", "opencode/glm-5-free")
        args = [
            "run",
            "-m",
            model,
        ]
        return self._run_command(
            args=args,
            prompt_string=prompt_string,
            run_ctx=run_ctx,
            cwd=config.settings.repo_root,
            timeout_seconds=timeout_seconds,
        )


class QwenAgent(AgentInterface):
    quality: int = 20

    def _run_with_prompt(
        self,
        prompt_string: str,
        task: AgentTask,  # noqa: ARG002
        run_ctx: RunContext,
        timeout_seconds: int = TIMEOUT_SECONDS,
    ) -> ProcessResult:
        model = os.environ.get("QWEN_MODEL", "coder-model")
        args = [
            "--yolo",
            "-m",
            model,
            "--output-format",
            "stream-json",
        ]
        return self._run_command(
            args=args,
            prompt_string=prompt_string,
            run_ctx=run_ctx,
            cwd=config.settings.repo_root,
            timeout_seconds=timeout_seconds,
        )
