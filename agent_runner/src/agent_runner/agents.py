from __future__ import annotations
from __future__ import annotations

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

import subprocess
from plumbum import local
from pydantic import BaseModel, ConfigDict

from . import config
from .agent_errors import classify_usage_limit
from .errors import AgentMetadataError, RateLimitUsageError
from .tasks import AgentTask


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

    def run_task(self, task: AgentTask, run_ctx: RunContext) -> ProcessResult:
        result = self._run_with_prompt(task.prompt_text(), task, run_ctx)
        classified = classify_usage_limit(self.name, result.stdout)
        if classified:
            raise RateLimitUsageError(self.name, classified.message)
        return result

    @abstractmethod
    def _run_with_prompt(
        self, prompt_string: str, task: AgentTask, run_ctx: RunContext
    ) -> ProcessResult:
        raise NotImplementedError

    def _build_env(self) -> dict[str, str]:
        env = {"PATH": self.env.get("PATH", "")}
        return env

    def _run_command(
        self,
        args: list[str],
        prompt_string: str,
        run_ctx: RunContext,
        cwd: Path | None = None,
    ) -> ProcessResult:
        env = {**os.environ, **self._build_env()}
        final_args = [self.binary] + list(args) + [prompt_string]
        chunks: list[bytes] = []
        with run_ctx.transcript_path.open("wb") as live_log:
            try:
                proc = subprocess.Popen(
                    final_args,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cwd,
                    env=env,
                )
            except FileNotFoundError:
                raise AgentMetadataError(f"Binary not found: {self.binary}")
            assert proc.stdout is not None
            for line in iter(proc.stdout.readline, b""):
                live_log.write(line)
                live_log.flush()
                chunks.append(line)
        exit_code = proc.wait()
        combined = b"".join(chunks).decode("utf-8", errors="replace")
        return ProcessResult(exit_code=exit_code, stdout=combined)


class CodexAgent(AgentInterface):
    def _run_with_prompt(
        self, prompt_string: str, task: AgentTask, run_ctx: RunContext
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
                raise AgentMetadataError("MCP server 'serena' not configured for codex")
        result = self._run_command(args=args, prompt_string=prompt_string, run_ctx=run_ctx)
        return ProcessResult(
            exit_code=result.exit_code,
            stdout=result.stdout,
            last_message_path=last_message,
        )


class ClaudeAgent(AgentInterface):
    def _run_with_prompt(
        self, prompt_string: str, task: AgentTask, run_ctx: RunContext
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
            args=args, prompt_string=prompt_string, run_ctx=run_ctx, cwd=config.settings.repo_root
        )


class GeminiAgent(AgentInterface):
    def _run_with_prompt(
        self, prompt_string: str, task: AgentTask, run_ctx: RunContext
    ) -> ProcessResult:
        args = [
            "--model",
            config.settings.gemini_model,
            "--output-format",
            "json",
            "--prompt",
        ]
        return self._run_command(args=args, prompt_string=prompt_string, run_ctx=run_ctx)


class OllamaAgent(AgentInterface):
    def _run_with_prompt(
        self, prompt_string: str, task: AgentTask, run_ctx: RunContext
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
            args=args, prompt_string=prompt_string, run_ctx=run_ctx, cwd=config.settings.repo_root
        )
