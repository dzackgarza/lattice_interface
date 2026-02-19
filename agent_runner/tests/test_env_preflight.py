"""Preflight checks: verify all required binaries are on the system PATH."""

import shutil

import pytest

REQUIRED_BINARIES = ["claude", "codex", "ollama", "gemini", "kilo", "opencode"]


@pytest.mark.parametrize("binary", REQUIRED_BINARIES)
def test_binary_on_path(binary: str) -> None:
    found = shutil.which(binary)
    assert found is not None, (
        f"Required binary '{binary}' not found on PATH. "
        f"Install it or ensure it is accessible on the current PATH."
    )
