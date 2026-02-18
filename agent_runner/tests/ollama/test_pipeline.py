import json
from pathlib import Path

import pytest

from agent_runner import config
from agent_runner import orchestrator


def _latest_run_dir(task: str, agent: str) -> Path | None:
    root = config.settings.log_root / task / agent
    if not root.exists():
        return None
    candidates = [p for p in root.iterdir() if p.is_dir()]
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def _load_metadata(task: str, agent: str) -> dict | None:
    run_dir = _latest_run_dir(task, agent)
    if not run_dir:
        return None
    meta = run_dir / "metadata.json"
    if not meta.exists():
        return None
    return json.loads(meta.read_text(encoding="utf-8"))


def test_ollama_pipeline(recwarn):
    rc = orchestrator.run(agent="ollama", task="debug_hello_simple")
    if rc == 10:
        assert any(issubclass(w.category, RuntimeWarning) for w in recwarn.list)
        return
    assert rc == 0
    meta = _load_metadata("debug_hello_simple", "ollama")
    assert meta is not None
    assert (config.settings.log_root / "debug_hello_simple" / "task.log").exists()
