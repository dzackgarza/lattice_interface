from __future__ import annotations

from abc import ABC
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, ConfigDict


class AgentTask(BaseModel, ABC):
    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str
    prompt_path: Path
    task_key: str
    requires_commit: bool = True
    notify: bool = True

    def prompt_text(self) -> str:
        return self.prompt_path.read_text(encoding="utf-8")

    def continuation_text(self) -> str:
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
        return (
            f"You are being woken up to continue a long-running task.\n\n"
            f"Current date and time: {timestamp}\n\n"
            f"You were paused after your last response and are now resuming. "
            f"Your original prompt is located at:\n\n"
            f"  {self.prompt_path}\n\n"
            f"If that prompt is no longer in your active context, re-read it now before proceeding. "
            f"Also re-read any documents mentioned in or linked from that prompt.\n\n"
            f"It is time for another iteration of your fundamental task. Please:\n\n"
            f"1. Complete another iteration of the core task described in your original prompt.\n"
            f"2. Address any outstanding work visible in your context or session memories.\n"
            f"3. Perform any self-maintenance needed to sustain this as an extremely long-horizon task "
            f"(updating memory files, tracking progress, recording what remains to be done, etc.).\n"
        )


class DocumentCoverageTask(AgentTask):
    pass


class DocumentTestAlignmentTask(AgentTask):
    pass


class DebugSmokeCommitTask(AgentTask):
    pass


class AgentManagementTask(AgentTask):
    pass
