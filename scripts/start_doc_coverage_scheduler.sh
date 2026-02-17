#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/notebooks/lattice_interface"
LOG_DIR="$REPO_DIR/tmp/cron"
PID_FILE="$LOG_DIR/doc_coverage_scheduler.pid"
OUT_FILE="$LOG_DIR/doc_coverage_scheduler.out"
UV_BIN="$(command -v uv)"

mkdir -p "$LOG_DIR"

EXISTING_PID="$(pgrep -fo "scripts/doc_coverage_scheduler.py" || true)"
if [[ -n "$EXISTING_PID" ]] && kill -0 "$EXISTING_PID" 2>/dev/null; then
  echo "$EXISTING_PID" > "$PID_FILE"
  echo "scheduler already running (pid=$EXISTING_PID)"
  exit 0
fi

if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  PID="$(cat "$PID_FILE")"
  if ps -p "$PID" -o args= | grep -q "doc_coverage_scheduler.py"; then
    echo "scheduler already running (pid=$PID)"
    exit 0
  fi
  rm -f "$PID_FILE"
fi

cd "$REPO_DIR"
setsid "$UV_BIN" run scripts/doc_coverage_scheduler.py >"$OUT_FILE" 2>&1 < /dev/null &
PID=$!
sleep 1

if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
  echo "$PID" > "$PID_FILE"
  echo "scheduler started (pid=$PID)"
else
  echo "scheduler failed to start; check $OUT_FILE"
  tail -n 40 "$OUT_FILE" || true
  rm -f "$PID_FILE"
  exit 1
fi
