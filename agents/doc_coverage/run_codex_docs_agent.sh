#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_FILE="$SCRIPT_DIR/prompt.md"
LOG_DIR="$REPO_DIR/tmp/agents/doc_coverage"
LOG_FILE="$LOG_DIR/codex.log"
LAST_MSG_FILE="$LOG_DIR/last_message.txt"

mkdir -p "$LOG_DIR"

{
  echo "===== $(date -u +'%Y-%m-%d %H:%M:%S UTC') : START ====="
  /usr/bin/codex exec \
    -C "$REPO_DIR" \
    --sandbox workspace-write \
    --full-auto \
    --ephemeral \
    -o "$LAST_MSG_FILE" \
    - < "$PROMPT_FILE"
  EXIT_CODE=$?
  echo "===== $(date -u +'%Y-%m-%d %H:%M:%S UTC') : END (exit=${EXIT_CODE}) ====="
  exit $EXIT_CODE
} >> "$LOG_FILE" 2>&1
