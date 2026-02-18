#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_FILE="$SCRIPT_DIR/prompt.md"
TASK_DIR="$REPO_DIR/tmp/agents/test_coverage"
CLAUDE_DIR="$TASK_DIR/claude"

TASK_LOG="$TASK_DIR/task.log"
RUN_ID="$(date -u +'%Y%m%d_%H%M%S')"
CLAUDE_DEBUG="$CLAUDE_DIR/${RUN_ID}_debug.log"

mkdir -p "$TASK_DIR" "$CLAUDE_DIR"

if ! /home/dzack/.local/bin/claude mcp get serena >/dev/null 2>&1; then
  printf '\n=== %s [claude/test_coverage] ERROR: MCP server serena not configured ===\n' \
    "$(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$TASK_LOG"
  exit 3
fi

printf '\n=== %s [claude/test_coverage] ===\n' "$(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$TASK_LOG"

cd "$REPO_DIR"
/home/dzack/.local/bin/claude \
  -p \
  --model sonnet \
  --effort high \
  --dangerously-skip-permissions \
  --no-session-persistence \
  < "$PROMPT_FILE" \
  >> "$TASK_LOG" \
  2> "$CLAUDE_DEBUG"
