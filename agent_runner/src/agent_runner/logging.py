from __future__ import annotations

import json
import logging
from dataclasses import asdict
from pathlib import Path
from typing import Any

import structlog

from . import config
from .agents import RunContext


def build_run_context(agent_name: str, task_name: str, run_id: str) -> RunContext:
    run_dir = config.settings.log_root / task_name / agent_name / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = run_dir / "stdout.log"
    stderr_path = run_dir / "stderr.log"
    transcript_path = run_dir / "transcript.log"
    metadata_path = run_dir / "metadata.json"
    summary_path = run_dir / "summary.txt"
    return RunContext(
        run_id=run_id,
        task_name=task_name,
        agent_name=agent_name,
        run_dir=run_dir,
        stdout_path=stdout_path,
        stderr_path=stderr_path,
        transcript_path=transcript_path,
        metadata_path=metadata_path,
        summary_path=summary_path,
    )


def _configure_logging(run_ctx: RunContext) -> None:
    run_ctx.run_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(run_ctx.run_dir / "runner.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.EventRenamer("message"),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )


def get_logger(run_ctx: RunContext) -> structlog.BoundLogger:
    _configure_logging(run_ctx)
    return structlog.get_logger(
        "agent_runner",
        task=run_ctx.task_name,
        agent=run_ctx.agent_name,
        run_id=run_ctx.run_id,
    )


def get_summary_logger(run_ctx: RunContext) -> logging.Logger:
    logger = logging.getLogger(
        f"agent_runner.summary.{run_ctx.task_name}.{run_ctx.agent_name}"
    )
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = logging.Formatter("%(message)s")
    task_log = config.settings.log_root / run_ctx.task_name / "task.log"
    agent_log = config.settings.log_root / run_ctx.task_name / run_ctx.agent_name / "agent.log"
    task_log.parent.mkdir(parents=True, exist_ok=True)
    agent_log.parent.mkdir(parents=True, exist_ok=True)
    task_handler = logging.FileHandler(task_log, encoding="utf-8")
    task_handler.setFormatter(formatter)
    agent_handler = logging.FileHandler(agent_log, encoding="utf-8")
    agent_handler.setFormatter(formatter)
    logger.addHandler(task_handler)
    logger.addHandler(agent_handler)
    return logger


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_metadata(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_context_dict(run_ctx: RunContext) -> dict[str, Any]:
    return asdict(run_ctx)
