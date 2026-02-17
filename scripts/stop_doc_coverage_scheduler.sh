#!/usr/bin/env bash
set -euo pipefail

PID_FILE="/notebooks/lattice_interface/tmp/cron/doc_coverage_scheduler.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "scheduler not running (no pid file)"
  exit 0
fi

PID="$(cat "$PID_FILE")"
if kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  echo "scheduler stopped (pid=$PID)"
else
  echo "stale pid file (pid=$PID not running)"
fi

pkill -f "scripts/doc_coverage_scheduler.py" >/dev/null 2>&1 || true
rm -f "$PID_FILE"
