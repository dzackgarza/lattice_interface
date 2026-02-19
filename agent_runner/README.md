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
| `opencode` | `opencode` | `opencode/glm-5-free` (via `OPENCODE_MODEL`) |
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

## Adding a New Agent

1. **Test the CLI manually** - Determine non-interactive flags:
   ```bash
   <binary> --help                    # Check available flags
   <binary> --yolo "say hello"        # Test auto-approve mode (common pattern)
   ```

2. **Add agent class** in `src/agent_runner/agents.py`:
   ```python
   class NewAgent(AgentInterface):
       def _run_with_prompt(
           self, prompt_string: str, task: AgentTask, run_ctx: RunContext
       ) -> ProcessResult:
           args = ["--flag1", "--flag2", "-m", "model-name"]
           return self._run_command(
               args=args,
               prompt_string=prompt_string,
               run_ctx=run_ctx,
               cwd=config.settings.repo_root,
           )
   ```

3. **Add binary path** in `src/agent_runner/config.py`:
   ```python
   newagent_bin: str = "/path/to/binary"
   ```

4. **Register in orchestrator** - `src/agent_runner/orchestrator.py`:
   - Add import: `from .agents import NewAgent`
   - Add to `AgentName` literal: `Literal[..., "newagent"]`
   - Add case in `_build_agent()`:
     ```python
     case "newagent":
         return NewAgent(
             name="newagent",
             binary=config.settings.newagent_bin,
             subcommand=None,
             base_args=[],
             env=env,
         )
     ```

5. **Create tests**:
   ```bash
   mkdir -p tests/newagent
   ```
   
   `tests/newagent/__init__.py`: (empty)
   
   `tests/newagent/test_direct.py`:
   ```python
   import warnings
   import pytest
   from agent_runner import config
   from agent_runner.agents import NewAgent
   from agent_runner.errors import RateLimitUsageError
   from agent_runner.logging import build_run_context
   from agent_runner.tasks import DebugSmokeCommitTask

   def test_newagent_direct():
       agent = NewAgent(
           name="newagent",
           binary=config.settings.newagent_bin,
           subcommand=None,
           base_args=[],
           env={"PATH": config.settings.path_prefix},
       )
       run_ctx = build_run_context(
           agent_name=agent.name, task_name="debug_hello_simple", run_id="test"
       )
       task = DebugSmokeCommitTask(
           name="debug_hello_simple",
           task_key="debug_hello_simple",
           prompt_path=config.settings.task_prompts()["debug_hello_simple"],
           requires_commit=False,
       )
       try:
           result = agent.run_task(task, run_ctx)
           assert result.exit_code == 0
       except RateLimitUsageError as exc:
           with pytest.warns(RuntimeWarning):
               warnings.warn(str(exc), RuntimeWarning)
   ```

   Add to `tests/test_agents_direct.py`:
   ```python
   from agent_runner.agents import NewAgent
   
   def test_newagent_direct():
       agent = NewAgent(...)
       _assert_agent(agent)
   ```

6. **Update this README** - Add row to Available Agents table.

7. **Run type check and tests**:
   ```bash
   uv run pyright src/
   uv run pytest tests/newagent/ tests/test_agents_direct.py::test_newagent_direct -v
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
