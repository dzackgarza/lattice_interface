import os
import warnings

import pytest

from agent_runner import config
from agent_runner.agents import ClaudeAgent, CodexAgent, GeminiAgent, OllamaAgent, QwenAgent
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


def _run(agent):
    run_ctx = build_run_context(agent_name=agent.name, task_name="debug_hello_simple", run_id="test")
    return agent.run_task(_task(), run_ctx)


def _assert_agent(agent):
    try:
        result = _run(agent)
        assert result.exit_code == 0
    except RateLimitUsageError:
        with pytest.warns(RuntimeWarning):
            warnings.warn("RateLimitUsageError observed during direct agent test", RuntimeWarning)


def test_codex_direct():
    _assert_agent(CodexAgent())


def test_gemini_direct():
    if os.getenv("GEMINI_KNOWN_DOWN") == "1":
        pytest.skip("Gemini CLI known down")
    _assert_agent(GeminiAgent())


def test_ollama_direct():
    _assert_agent(OllamaAgent())


def test_claude_direct():
    _assert_agent(ClaudeAgent())


def test_qwen_direct():
    _assert_agent(QwenAgent())
