# Agent Runner

Centralized Python app for running agents with consistent logging and notifications.

## Amp CLI error (documented)

The Amp CLI currently fails in non-interactive mode with:

```
Error: The --archive flag requires --execute mode
Use: amp --execute "your message" --archive
```

This conflicts with the historical runner flags and is one reason the Amp runner is removed here.
Amp is replaced by the Gemini CLI using `--model auto` and JSON output for token parsing.

## Gemini cron note

Do not run Gemini in cron jobs unless the pytest suite passes. There are known global access issues that can cause long hangs or failures; verify `pytest` is green before scheduling Gemini runs.

## Debug smoke task

Use the built-in debug task to exercise network access and git commits:

```bash
agent_runner/.venv/bin/python -m agent_runner --agent codex --task debug_smoke_commit
```
