#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_FILE="$SCRIPT_DIR/prompt.md"
TASK_DIR="$REPO_DIR/tmp/agents/test_coverage"
AMP_DIR="$TASK_DIR/amp"

TASK_LOG="$TASK_DIR/task.log"
RUN_ID="$(date -u +'%Y%m%d_%H%M%S')"
AMP_DEBUG="$AMP_DIR/${RUN_ID}_debug.log"

mkdir -p "$TASK_DIR" "$AMP_DIR"

if ! /home/dzack/.local/bin/amp mcp list 2>/dev/null | grep -q 'serena'; then
  printf '\n=== %s [amp/test_coverage] ERROR: MCP server serena not configured ===\n' \
    "$(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$TASK_LOG"
  exit 3
fi

printf '\n=== %s [amp/test_coverage] ===\n' "$(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$TASK_LOG"

cd "$REPO_DIR"
/home/dzack/.local/bin/amp \
  --dangerously-allow-all \
  --archive \
  --mode smart \
  --log-file "$AMP_DEBUG" \
  < "$PROMPT_FILE" \
  >> "$TASK_LOG"
