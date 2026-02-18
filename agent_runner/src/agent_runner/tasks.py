from __future__ import annotations

from abc import ABC
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


class DocumentCoverageTask(AgentTask):
    pass


class DocumentTestAlignmentTask(AgentTask):
    pass


class DebugSmokeCommitTask(AgentTask):
    pass
