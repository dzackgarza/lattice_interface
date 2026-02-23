---
name: debug-autonomous-work
description: Debug autonomous agent workers, cron jobs, timeouts, and connectivity issues. Use when agent runs are failing, not running, or producing unexpected behavior.
---

# Debugging Autonomous Work

**Example tasks:** See `example_tasks/` directory

## Step 1: Check Current Time

```bash
date
timedatectl
```

## Step 2: Check ntfy Notifications

```bash
curl -s "https://ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=all"
```

## Step 3: Check Crontab

```bash
crontab -l
```

## Step 4: Check Transcripts

```bash
ls -lt agent_runner/logs/
```

## Step 5: Test Connectivity

```bash
cd agent_runner
timeout 30 uv run python -m agent_runner run --agent <agent> --task debug_hello_simple
```

## Step 6: Test Web/Git

```bash
timeout 30 uv run python -m agent_runner run --agent <agent> --task debug_curl_test
timeout 30 uv run python -m agent_runner run --agent <agent> --task debug_git_commit
```

## Step 7: Check Logs

```bash
tail -100 heartbeat.log
```
