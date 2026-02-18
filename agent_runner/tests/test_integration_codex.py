import subprocess
from pathlib import Path


def test_codex_hello_world_integration():
    repo_root = Path(__file__).resolve().parents[2]
    python = repo_root / "agent_runner" / ".venv" / "bin" / "python"
    cmd = [
        str(python),
        "-m",
        "agent_runner",
        "--agent",
        "codex",
        "--task",
        "debug_smoke_commit",
    ]
    result = subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
