# Agent Runner

Centralized Python app for running agents with consistent logging and notifications.

## Quick Start

```bash
# Run any agent with any task
uv run python -m agent_runner run --agent <agent> --task <task>

# Example: kilo with trivial debug task
uv run python -m agent_runner run --agent kilo --task debug_hello_simple
```

### Available Agents

| Agent | Binary | Model |
|-------|--------|-------|
| `codex` | `codex` | Configurable via `--config model_reasoning_effort` |
| `claude` | `claude` | `sonnet` |
| `gemini` | `gemini` | `auto` (configurable via `AGENT_RUNNER_GEMINI_MODEL`) |
| `kilo` | `kilo` | `kilo/minimax/minimax-m2.5:free` |
| `ollama` | `ollama` | Configurable via `OLLAMA_MODEL` env var |
| `opencode` | `opencode` | `opencode/kimi-k2.5-free` (via `OPENCODE_MODEL`) |
| `qwen` | `qwen` | `coder-model` (via `QWEN_MODEL`) |

### Available Tasks

| Task | Description | Requires Commit |
|------|-------------|-----------------|
| `debug_hello_simple` | Say hello and exit | No |
| `debug_hello_world` | Hello world test | Yes |
| `debug_smoke_commit` | Exercise git commits | Yes |
| `document_coverage` | Run doc coverage agent | Yes |
| `document_test_alignment` | Run test coverage agent | Yes |
| `agent_management` | Run agent management tasks | Yes |

### Run Output

Logs are written to `logs/<task>/<agent>/<run_id>/`:

```
logs/
└── debug_hello_simple/
    └── kilo/
        └── 20260219_175043/
            ├── metadata.json    # Full run metadata (tokens, elapsed, etc.)
            ├── summary.txt      # Human-readable summary
            ├── transcript.log   # Raw agent output
            └── stdout.log       # Stdout capture
```

## Architecture

Key source files:
- `src/agent_runner/orchestrator.py` - Main entry point, CLI, run logic
- `src/agent_runner/agents.py` - Agent definitions (KiloAgent, ClaudeAgent, etc.)
- `src/agent_runner/tasks.py` - Task definitions
- `src/agent_runner/config.py` - Paths, binaries, settings

## Timeout

Agent runs timeout after 15 minutes by default. This triggers an `AgentTimeoutError` and sends a failure notification via ntfy.

To customize the timeout:

```bash
export AGENT_RUNNER_TIMEOUT_SECONDS=300  # 5 minutes
agent_runner run --agent claude --task document_coverage
```

The notification includes the agent name, task, run_id, and log directory.

Exit codes:
- `0` - success
- `1` - agent error
- `10` - rate limit
- `11` - timeout

## ntfy

The ntfy `/json` endpoint is a **streaming API** - it keeps the connection open. To fetch historical messages:

```bash
# Fetch all cached messages
curl "ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=all"

# Fetch last 30 minutes of messages
curl "ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=30m"

# Fetch just the latest message
curl "ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=latest"
```

Messages are cached for a few hours on ntfy.sh.

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

## Cron monitoring

The cron jobs run via crontab. To monitor:

```bash
# View current crontab
crontab -l

# Watch heartbeat logs (runs every minute)
tail -f logs/heartbeat/task.log

# Watch document_coverage task logs
tail -f logs/document_coverage/task.log

# List recent runs by agent
ls -lt logs/document_coverage/claude/ | head -5
```

To debug cron issues:
```bash
sudo journalctl -u cron --since "1 hour ago"
```
