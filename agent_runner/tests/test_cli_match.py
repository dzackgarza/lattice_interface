import pytest

from agent_runner import orchestrator


def test_build_task_valid():
    task = orchestrator._build_task("document_coverage")
    assert task.name == "document_coverage"


def test_build_task_debug_smoke():
    task = orchestrator._build_task("debug_smoke_commit")
    assert task.name == "debug_smoke_commit"


def test_build_task_invalid():
    with pytest.raises(AssertionError):
        orchestrator._build_task("nope")
