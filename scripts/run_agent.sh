#!/usr/bin/env bash
# Usage: run_agent.sh <name> <script>
set -euo pipefail

NAME="$1"
SCRIPT="$2"
REPO_DIR="/home/dzack/lattice_interface"
FIRED_LOG="$REPO_DIR/tmp/cron_fired.log"
NTFY_TOPIC="dzg-lattice-doc-updates"

mkdir -p "$(dirname "$FIRED_LOG")"
echo "$(TZ=Asia/Taipei date '+%Y-%m-%d %H:%M:%S TST') fired: $NAME" >> "$FIRED_LOG"

# Heartbeat: just fire and exit, no ntfy
if [ "$NAME" = "heartbeat" ]; then
  exec "$SCRIPT"
fi

# Run agent, capture exit code
"$SCRIPT"
EXIT_CODE=$?

# Derive task log: agents/doc_coverage/run_*.sh -> tmp/agents/doc_coverage/task.log
TASK_KEY=$(basename "$(dirname "$SCRIPT")")
TASK_LOG="$REPO_DIR/tmp/agents/$TASK_KEY/task.log"

# Extract last run's section from task log (from last === separator to EOF)
if [ -f "$TASK_LOG" ]; then
  LAST_SECTION=$(awk '/^===[[:space:]]/{s=$0"\n"; next} length(s)>0{s=s$0"\n"} END{printf "%s", s}' "$TASK_LOG" | tail -c 1800)
else
  LAST_SECTION="(no task log)"
fi

# Notification content
if [ $EXIT_CODE -eq 0 ]; then
  STATUS="SUCCESS"
  PRIORITY="default"
  TAGS="white_check_mark"
else
  STATUS="FAILED (exit=$EXIT_CODE)"
  PRIORITY="high"
  TAGS="x"
fi

TIMESTAMP="$(TZ=Asia/Taipei date '+%Y-%m-%d %H:%M TST')"
TITLE="[$TASK_KEY] $NAME — $STATUS — $TIMESTAMP"
BODY="$LAST_SECTION"

curl -s \
  -H "Title: $TITLE" \
  -H "Priority: $PRIORITY" \
  -H "Tags: $TAGS" \
  -d "$BODY" \
  "https://ntfy.sh/$NTFY_TOPIC" > /dev/null

exit $EXIT_CODE
