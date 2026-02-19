import warnings

import pytest

from agent_runner import config
from agent_runner.agents import OpenCodeAgent
from agent_runner.errors import RateLimitUsageError
from agent_runner.logging import build_run_context
from agent_runner.tasks import DebugSmokeCommitTask


def _task() -> DebugSmokeCommitTask:
    return DebugSmokeCommitTask(
        name="debug_hello_simple",
        task_key="debug_hello_simple",
        prompt_path=config.settings.task_prompts()["debug_hello_simple"],
        requires_commit=False,
    )


def test_opencode_direct():
    agent = OpenCodeAgent(
        name="opencode",
        binary=config.settings.opencode_bin,
        subcommand="run",
        base_args=[],
        env={},
    )
    run_ctx = build_run_context(agent_name=agent.name, task_name="debug_hello_simple", run_id="test")
    try:
        result = agent.run_task(_task(), run_ctx)
        assert result.exit_code == 0
    except RateLimitUsageError as exc:
        with pytest.warns(RuntimeWarning):
            warnings.warn(str(exc), RuntimeWarning)
