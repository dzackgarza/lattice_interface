# Agent Runner

Centralized Python app for running agents with consistent logging and notifications.

## Organization

```
agent_runner/
├── src/agent_runner/
│   ├── orchestrator.py      # Main CLI entry point, run logic, error classification
│   ├── agents.py            # Agent classes (KiloAgent, ClaudeAgent, etc.)
│   ├── tasks.py             # Task definitions
│   ├── config.py            # Paths, binaries, settings
│   ├── errors.py            # Error classes (AgentConnectivityError, etc.)
│   ├── agent_errors.py      # Rate limit detection
│   ├── logging.py           # Logging utilities
│   ├── notifications.py     # ntfy notification sending
│   └── harness.py           # Subprocess execution with timeout
├── prompts/
│   └── debug/               # Debug prompts (hello_world, smoke, etc.)
└── logs/                    # Run logs (see below)
```

## Monitoring Live Runs

### Is an Agent Currently Working?

```bash
# Check heartbeat (runs every minute)
tail -f logs/heartbeat/task.log

# Check if any agent logs were created in the last few minutes
find logs -name "transcript.log" -mmin -5

# List recent runs by task
ls -lt logs/document_coverage/ | head -5
```

### Monitor Live Output

Runs stream output to `transcript.log` in real-time:

```bash
# Watch live output of a running agent
tail -f logs/document_coverage/<agent>/<run_id>/transcript.log

# Watch all document_coverage runs
tail -f logs/document_coverage/task.log
```

The agent writes output as it runs, so you can see progress in real-time.

### Recent Runs

```bash
# List recent runs by agent
ls -lt logs/document_coverage/opencode/ | head -10
ls -lt logs/document_coverage/kilo/ | head -10

# Check ntfy notifications (last 30 minutes)
curl -s "https://ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=30m"

# View crontab to see scheduled jobs
crontab -l
```

## Agent Slugs

Agent slugs are defined in `src/agent_runner/agents.py`:

```python
class AgentName(StrEnum):
    codex = "codex"
    claude = "claude"
    gemini = "gemini"
    kilo = "kilo"
    ollama = "ollama"
    opencode = "opencode"
    qwen = "qwen"
    auto = "auto"  # Auto-select best available agent
```

Binary paths and models are configured in `src/agent_runner/config.py`:

| Agent | Binary Config | Default Model |
|-------|--------------|---------------|
| `codex` | `codex_bin` | Configurable via `--config model_reasoning_effort` |
| `claude` | `claude_bin` | `sonnet` |
| `gemini` | `gemini_bin` | `auto` (via `AGENT_RUNNER_GEMINI_MODEL`) |
| `kilo` | `kilo_bin` | `kilo/minimax/minimax-m2.5:free` |
| `ollama` | `ollama_bin` | Configurable via `OLLAMA_MODEL` |
| `opencode` | `opencode_bin` | `opencode/glm-5-free` |
| `qwen` | `qwen_bin` | `coder-model` |

## Quick Start

```bash
# Run any agent with any task
uv run python -m agent_runner run --agent <agent> --task <task>

# Example: kilo with trivial debug task
uv run python -m agent_runner run --agent kilo --task debug_hello_simple
```

### Available Agents

| Agent | Binary Config | Model |
|-------|--------------|-------|
| `codex` | `codex_bin` | Configurable |
| `claude` | `claude_bin` | `sonnet` |
| `gemini` | `gemini_bin` | `auto` |
| `kilo` | `kilo_bin` | `minimax-m2.5:free` |
| `ollama` | `ollama_bin` | Configurable |
| `opencode` | `opencode_bin` | `glm-5-free` |
| `qwen` | `qwen_bin` | `coder-model` |

Use `--agent auto` to auto-select the best available agent.

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
- `src/agent_runner/orchestrator.py` - Main entry point, CLI, run logic, error classification
- `src/agent_runner/agents.py` - Agent implementations (KiloAgent, ClaudeAgent, etc.)
- `src/agent_runner/tasks.py` - Task definitions
- `src/agent_runner/config.py` - Paths, binaries, settings
- `src/agent_runner/errors.py` - Error classes
- `src/agent_runner/notifications.py` - ntfy notification sending
- `src/agent_runner/logging.py` - Logging utilities

## Adding a New Agent

1. **Test the CLI manually** - Determine non-interactive flags:
   ```bash
   <binary> --help                    # Check available flags
   <binary> --yolo "say hello"        # Test auto-approve mode
   ```

2. **Add to AgentName enum** in `src/agent_runner/agents.py`:
   ```python
   class AgentName(StrEnum):
       # ... existing agents ...
       newagent = "newagent"
   ```

3. **Add binary config** in `src/agent_runner/config.py`:
   ```python
   newagent_bin: str = "/path/to/newagent"
   ```

4. **Add agent builder** in `src/agent_runner/orchestrator.py`:
   - Import: `from .agents import NewAgentAgent`
   - Add case in `_build_agent()`:
   ```python
   case AgentName.newagent:
       return NewAgentAgent(
           name=AgentName.newagent,
           binary=config.settings.newagent_bin,
       )
   ```

5. **Test it**:
   ```bash
   uv run python -m agent_runner run --agent newagent --task debug_hello_simple
   ```

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
- `1` - agent/process error
- `2` - unhandled error
- `10` - rate limit (usage_limit)
- `11` - timeout
- `12` - connectivity error (model connection failed)
- `13` - agent selection error
- `14` - model/harness error

### Error Classification

Errors are classified based on symptoms:

| Classification | Meaning | Cause | Action |
|---------------|---------|-------|--------|
| `usage_limit` | Rate limit hit | API quota exceeded | Wait or use different agent |
| `timeout` | Process killed (>15min) | Agent hung | Check for infinite loops |
| `connectivity` | Model connection failed | Network/model issues | Check model availability |
| `commit_missing` | No commits made | Agent found nothing to do | May be expected |
| `process_error` | Agent crashed/exited non-zero | Internal error | Check transcript |

**Short run detection**: Runs completing in <3 minutes or with <10 lines of output are classified as `connectivity` errors (not `commit_missing`), since they indicate the model failed to connect/process properly.

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

## Debugging Failed Runs

### Step 1: Check ntfy Notifications

**Always start here.** Every run (success or failure) pushes a notification to ntfy.

```bash
# Fetch recent notifications as JSON
curl -s -H "Accept: application/json" "https://ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=2h" | jq .
```

Cross-reference notification timestamps against crontab times:
```bash
crontab -l
```

**Triage priority:**
1. **Missing notification** = silent failure (highest priority) - the run didn't complete notification, check orchestrator logs
2. **Failed notification** (tag: `x`) - agent ran but failed, proceed to Step 2
3. **Success notification** (tag: `white_check_mark`) - no action needed

### Step 2: Dump the Transcript

For failed runs, immediately dump the full transcript:

```bash
# Find the run directory matching the notification timestamp
ls -lt logs/document_coverage/<agent>/ | head -10

# Dump the transcript
cat logs/document_coverage/<agent>/<run_id>/transcript.log
```

Verify the transcript matches the notification failure reason:
- Notification says "Model not found" → transcript should show `ModelNotFoundError`
- Notification says "No git commits" → transcript should show agent activity but no code changes
- Notification says "usage limit" → transcript should show rate limit error
- Notification says "timeout" → transcript may be truncated/incomplete

### Step 3: Triage the Agent Failure

Common failure patterns:

| Error | Cause | Fix |
|-------|-------|-----|
| `ModelNotFoundError` | Model removed/deprecated | Update default model in `src/agent_runner/agents.py` |
| `No git commits detected` | Agent found nothing to fix | May be expected if docs already complete |
| `usage limit` | API rate limit hit | Wait or use different agent |
| `timeout` | Agent hung (>15min) | Check for infinite loops, increase timeout |
| Silent (no notification) | Runner crashed before notify | Check orchestrator logs, systemd journal |

### Example Debug Session

```bash
# 1. Check notifications - see opencode failing since 15:30
curl -s -H "Accept: application/json" "https://ntfy.sh/dzg-lattice-doc-updates/json?poll=1&since=3h" | jq '.title'

# 2. Find matching runs and dump transcripts
ls -lt logs/document_coverage/opencode/20260219_1*/

# 3. Check a specific failure
cat logs/document_coverage/opencode/20260219_153003/stdout.log

# 4. Error shows: Model not found: opencode/kimi-k2.5-free
# 5. Verify model exists: opencode run -m opencode/glm-5-free "hi"
# 6. Fix in agents.py, run typecheck, commit
```
