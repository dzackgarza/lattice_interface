from __future__ import annotations


class AgentRunnerError(Exception):
    """Base error for agent runner."""


class AgentProcessError(AgentRunnerError):
    def __init__(self, agent: str, task: str, exit_code: int, detail: str | None = None) -> None:
        detail_msg = f" ({detail})" if detail else ""
        super().__init__(f"Agent {agent} failed for task {task} (exit={exit_code}){detail_msg}")
        self.agent = agent
        self.task = task
        self.exit_code = exit_code
        self.detail = detail


class AgentCommitMissingError(AgentRunnerError):
    def __init__(self, agent: str, task: str) -> None:
        super().__init__(f"No git commits detected during agent run for {agent}/{task}.")
        self.agent = agent
        self.task = task


class RateLimitUsageError(AgentRunnerError):
    def __init__(self, agent: str, detail: str) -> None:
        super().__init__(f"Usage limit for {agent}: {detail}")
        self.agent = agent
        self.detail = detail


class AgentMetadataError(AgentRunnerError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class AgentTimeoutError(AgentRunnerError):
    def __init__(self, agent: str, task: str, timeout_seconds: int) -> None:
        super().__init__(f"Agent {agent} timed out after {timeout_seconds}s for task {task}")
        self.agent = agent
        self.task = task
        self.timeout_seconds = timeout_seconds


class AgentConnectivityError(AgentRunnerError):
    def __init__(self, agent: str, detail: str) -> None:
        super().__init__(f"Agent {agent} connectivity check failed: {detail}")
        self.agent = agent
        self.detail = detail


class AgentSelectionError(AgentRunnerError):
    def __init__(self, detail: str) -> None:
        super().__init__(f"Auto agent selection failed: {detail}")
        self.detail = detail
