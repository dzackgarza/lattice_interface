import pytest


def test_codex_hello_world_integration(recwarn):
    from agent_runner.orchestrator import Orchestrator, OrchestratorArgs

    rc = Orchestrator(
        args=OrchestratorArgs(agent="codex", task="debug_smoke_commit")
    ).run()
    if rc == 10:
        assert any(issubclass(w.category, RuntimeWarning) for w in recwarn.list)
        return
    assert rc == 0
