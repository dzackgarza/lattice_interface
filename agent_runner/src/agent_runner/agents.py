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
    stderr_path: Path
    transcript_path: Path
    metadata_path: Path
    summary_path: Path


@dataclass(frozen=True)
class ProcessResult:
    exit_code: int
    stdout: str
    stderr: str
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
        classified = classify_usage_limit(self.name, result.stdout, result.stderr)
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
        cwd: Path | None = None,
    ) -> ProcessResult:
        final_args = list(args) + [prompt_string]
        cmd = local[self.binary][final_args]
        with local.env(**self._build_env()):
            if cwd is not None:
                with local.cwd(str(cwd)):
                    retcode, stdout, stderr = cmd.run(retcode=None)
            else:
                retcode, stdout, stderr = cmd.run(retcode=None)
        return ProcessResult(exit_code=retcode, stdout=stdout, stderr=stderr)


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
        result = self._run_command(args=args, prompt_string=prompt_string)
        return ProcessResult(
            exit_code=result.exit_code,
            stdout=result.stdout,
            stderr=result.stderr,
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
            args=args, prompt_string=prompt_string, cwd=config.settings.repo_root
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
        return self._run_command(args=args, prompt_string=prompt_string)


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
            args=args, prompt_string=prompt_string, cwd=config.settings.repo_root
        )


class HeartbeatAgent(AgentInterface):
    binary: str = "heartbeat"
    subcommand: str | None = None
    base_args: list[str] = []
    env: Mapping[str, str] = {}

    def _run_with_prompt(
        self, prompt_string: str, task: AgentTask, run_ctx: RunContext
    ) -> ProcessResult:
        from datetime import datetime, timezone

        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        return ProcessResult(exit_code=0, stdout=f"heartbeat ok at {ts}", stderr="")
