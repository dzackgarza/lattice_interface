#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_FILE="$SCRIPT_DIR/prompt.md"
TASK_DIR="$REPO_DIR/tmp/agents/doc_coverage"
AMP_DIR="$TASK_DIR/amp"

TASK_LOG="$TASK_DIR/task.log"
RUN_ID="$(date -u +'%Y%m%d_%H%M%S')"
AMP_DEBUG="$AMP_DIR/${RUN_ID}_debug.log"

mkdir -p "$TASK_DIR" "$AMP_DIR"

printf '\n=== %s [amp/doc_coverage] ===\n' "$(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$TASK_LOG"

cd "$REPO_DIR"
/home/dzack/.local/bin/amp \
  --dangerously-allow-all \
  --archive \
  --mode smart \
  --log-file "$AMP_DEBUG" \
  < "$PROMPT_FILE" \
  >> "$TASK_LOG"
