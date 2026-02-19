from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="AGENT_RUNNER_", extra="ignore")

    repo_root: Path = Path(__file__).resolve().parents[3]
    agents_dir: Path = repo_root / "agents"
    log_root: Path = repo_root / "agent_runner" / "logs"
    prompts_dir: Path = repo_root / "agent_runner" / "prompts"
    debug_prompts_dir: Path = prompts_dir / "debug"

    ntfy_topic: str = "dzg-lattice-doc-updates"
    ntfy_server: str = "https://ntfy.sh"

    path_prefix: str = (
        "/home/dzack/.nvm/versions/node/v25.6.1/bin:/home/dzack/.local/bin"
    )

    codex_bin: str = "/home/dzack/.nvm/versions/node/v25.6.1/bin/codex"
    claude_bin: str = "/home/dzack/.local/bin/claude"
    gemini_bin: str = "gemini"
    gemini_model: str = "auto"
    ollama_bin: str = "ollama"
    kilo_bin: str = "/home/dzack/.nvm/versions/node/v25.6.1/bin/kilo"
    opencode_bin: str = "/home/dzack/.opencode/bin/opencode"

    def task_prompts(self) -> dict[str, Path]:
        return {
            "agent_management": self.agents_dir / "agent_management" / "prompt.md",
            "document_coverage": self.agents_dir / "doc_coverage" / "prompt.md",
            "document_test_alignment": self.agents_dir / "test_coverage" / "prompt.md",
            "debug_smoke_commit": self.prompts_dir / "debug" / "commit_smoke.md",
            "debug_hello_world": self.prompts_dir / "debug" / "hello_world.md",
            "debug_hello_simple": self.prompts_dir / "debug" / "hello_simple.md",
        }

    def debug_prompts(self) -> dict[str, Path]:
        return {
            "ping": self.debug_prompts_dir / "ping.md",
            "smoke": self.debug_prompts_dir / "smoke.md",
        }


settings = Settings()
