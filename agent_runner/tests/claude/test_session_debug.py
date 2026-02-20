import warnings

import pytest

from agent_runner import config
from agent_runner.agents import ClaudeAgent, SessionResume
from agent_runner.errors import RateLimitUsageError
from agent_runner.logging import build_run_context
from agent_runner.tasks import DebugSmokeCommitTask

SESSION_ID = "932c2c07-2549-40fb-8b08-97d6f90cc995"
SESSION_DIR = config.settings.repo_root / "agents" / "agent_management"


@pytest.mark.timeout(600)
def test_claude_session_recall():
    agent = ClaudeAgent(session=SessionResume(id=SESSION_ID, dir=SESSION_DIR))
    task = DebugSmokeCommitTask(
        name="debug_session_recall",
        task_key="debug_session_recall",
        prompt_path=config.settings.debug_prompts()["session_recall"],
        requires_commit=False,
    )
    run_ctx = build_run_context(agent_name=agent.name, task_name=task.name, run_id="test")
    try:
        result = agent.run_task(task, run_ctx)
        assert result.exit_code == 0
    except RateLimitUsageError as exc:
        with pytest.warns(RuntimeWarning):
            warnings.warn(str(exc), RuntimeWarning)
