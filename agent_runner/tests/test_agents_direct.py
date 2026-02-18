import warnings

import pytest

from agent_runner import config
from agent_runner.agents import ClaudeAgent, CodexAgent, GeminiAgent, OllamaAgent
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
            warnings.warn("RateLimitUsageError observed during direct agent test", RuntimeWarning)


def test_codex_direct():
    agent = CodexAgent(
        name="codex",
        binary=config.settings.codex_bin,
        subcommand="exec",
        base_args=[],
        env={"PATH": config.settings.path_prefix},
    )
    _assert_agent(agent)


def test_gemini_direct():
    agent = GeminiAgent(
        name="gemini",
        binary=config.settings.gemini_bin,
        subcommand=None,
        base_args=[],
        env={"PATH": config.settings.path_prefix},
    )
    _assert_agent(agent)


def test_ollama_direct():
    agent = OllamaAgent(
        name="ollama",
        binary=config.settings.ollama_bin,
        subcommand=None,
        base_args=[],
        env={"PATH": config.settings.path_prefix},
    )
    _assert_agent(agent)


def test_claude_direct():
    agent = ClaudeAgent(
        name="claude",
        binary=config.settings.claude_bin,
        subcommand=None,
        base_args=[],
        env={"PATH": config.settings.path_prefix},
    )
    _assert_agent(agent)