import subprocess
import sys

import pytest


def test_cli_run_help():
    result = subprocess.run(
        [sys.executable, "-m", "agent_runner", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "run" in result.stdout.lower() or "agent" in result.stdout.lower()


def test_cli_run_command_help():
    result = subprocess.run(
        [sys.executable, "-m", "agent_runner", "run", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--agent" in result.stdout
    assert "--task" in result.stdout


def test_cli_heartbeat():
    result = subprocess.run(
        [sys.executable, "-m", "agent_runner", "heartbeat"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
