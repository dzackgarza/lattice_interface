#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_FILE="$SCRIPT_DIR/prompt.md"
TASK_DIR="$REPO_DIR/tmp/agents/doc_coverage"
CODEX_DIR="$TASK_DIR/codex"

TASK_LOG="$TASK_DIR/task.log"
RUN_ID="$(date -u +'%Y%m%d_%H%M%S')"
CODEX_DEBUG="$CODEX_DIR/${RUN_ID}_debug.log"
LAST_MSG="$CODEX_DIR/${RUN_ID}_last_message.txt"

mkdir -p "$TASK_DIR" "$CODEX_DIR"

printf '\n=== %s [codex/doc_coverage] ===\n' "$(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$TASK_LOG"

/home/dzack/.nvm/versions/node/v25.6.1/bin/codex exec \
  -C "$REPO_DIR" \
  --sandbox workspace-write \
  --full-auto \
  --ephemeral \
  -o "$LAST_MSG" \
  - < "$PROMPT_FILE" \
  >> "$CODEX_DEBUG" 2>&1

[ -f "$LAST_MSG" ] && cat "$LAST_MSG" >> "$TASK_LOG"
