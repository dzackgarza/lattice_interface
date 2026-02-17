#!/usr/bin/env python3
# /// script
# dependencies = ["apscheduler>=3.10,<4"]
# ///

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler


REPO_DIR = Path("/notebooks/lattice_interface")
PROMPT_FILE = REPO_DIR / "prompt.md"
LOG_DIR = REPO_DIR / "tmp" / "cron"
LOG_FILE = LOG_DIR / "codex.log"
LAST_MSG_FILE = LOG_DIR / "last_message.txt"
LOCK_FILE = Path("/tmp/lattice_doc_coverage.lock")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def run_job() -> int:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "/usr/bin/flock",
        "-n",
        str(LOCK_FILE),
        "/usr/bin/codex",
        "exec",
        "-C",
        str(REPO_DIR),
        "--search",
        "-c",
        'model_reasoning_effort="high"',
        "--sandbox",
        "workspace-write",
        "--full-auto",
        "--ephemeral",
        "-o",
        str(LAST_MSG_FILE),
        "-",
    ]

    with PROMPT_FILE.open("rb") as stdin_fh, LOG_FILE.open("ab") as log_fh:
        log_fh.write(f"===== {utc_now()} : START =====\n".encode())
        log_fh.flush()
        proc = subprocess.run(
            cmd,
            stdin=stdin_fh,
            stdout=log_fh,
            stderr=log_fh,
            cwd=str(REPO_DIR),
            check=False,
            env=os.environ.copy(),
        )
        log_fh.write(f"===== {utc_now()} : END (exit={proc.returncode}) =====\n".encode())
        log_fh.flush()
        return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Hourly UV/APScheduler runner for doc coverage prompt.")
    parser.add_argument("--once", action="store_true", help="Run one job immediately and exit.")
    args = parser.parse_args()

    if args.once:
        return run_job()

    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(
        run_job,
        trigger="cron",
        minute=35,
        id="lattice_doc_coverage",
        replace_existing=True,
        max_instances=1,
        coalesce=True,
        misfire_grace_time=300,
    )
    print(f"[{utc_now()}] scheduler started; next runs at minute 35 each hour (UTC).", flush=True)
    scheduler.start()
    return 0


if __name__ == "__main__":
    sys.exit(main())
