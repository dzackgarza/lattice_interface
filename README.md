# Lattice Documentation (Indefinite-First)

## Purpose

This docs set exists to provide practical, accurate references for free/open lattice software with a **primary focus on indefinite lattices**.

The goal is to support workflows such as:

- indefinite quadratic form classification,
- local/global/rational isometry checks,
- discriminant-form and genus computations,
- hyperbolic/reflection-lattice methods (e.g. Vinberg-style workflows),
- lattice-with-isometry constructions used in arithmetic/algebraic geometry contexts.

## Priorities

1. Indefinite-lattice methods first.
2. Explicit method-level documentation (not vague package summaries).
3. Clear definiteness constraints and caveats.
4. Source-backed claims (official docs/source when possible).
5. Coverage across major free systems and packages.

## Non-Goals

- Proprietary CAS workflows (e.g. Magma, Wolfram).
- Polytope-counting-first documentation unless directly relevant to indefinite lattice work.
- Credit-by-alias or hidden coverage shortcuts.

## Practical Rule

When deciding what to add or refine, prefer content that improves indefinite workflows before expanding Euclidean-only reduction material.

## Automation (Cron Stand-In)

This repo currently uses a local scheduler stand-in instead of system cron:

- scheduler: `scripts/doc_coverage_scheduler.py` (APScheduler via `uv run`)
- start helper: `scripts/start_doc_coverage_scheduler.sh`
- stop helper: `scripts/stop_doc_coverage_scheduler.sh`
- legacy/manual runner: `scripts/run_doc_coverage_cron.sh`

### Current Setup

- schedule: every 10 minutes, UTC (`trigger="cron", minute=\"*/10\"`)
- single-instance protection:
  - APScheduler `max_instances=1`
  - file lock: `/tmp/lattice_doc_coverage.lock` via `flock -n`
- codex invocation (from scheduler):
  - prompt input: `prompt.md`
  - output summary file: `tmp/cron/last_message.txt`
  - combined stdout/stderr log: `tmp/cron/codex.log`
  - flags include `--search` and high reasoning effort (`model_reasoning_effort="high"`)

### Start / Stop

```bash
scripts/start_doc_coverage_scheduler.sh
scripts/stop_doc_coverage_scheduler.sh
```

The start script writes:

- PID file: `tmp/cron/doc_coverage_scheduler.pid`
- scheduler process output: `tmp/cron/doc_coverage_scheduler.out`

### Modify Schedule or Runtime Behavior

Edit `scripts/doc_coverage_scheduler.py`:

- schedule timing: `scheduler.add_job(... minute=\"*/10\" ...)`
- timezone: `BlockingScheduler(timezone="UTC")`
- codex flags: `cmd = [ ... ]` in `run_job()`
- lock behavior: `LOCK_FILE`
- log/output paths: `LOG_DIR`, `LOG_FILE`, `LAST_MSG_FILE`

After edits, restart:

```bash
scripts/stop_doc_coverage_scheduler.sh
scripts/start_doc_coverage_scheduler.sh
```

### Manual Run

One immediate run through the same scheduler code path:

```bash
uv run scripts/doc_coverage_scheduler.py --once
```

Legacy/manual wrapper:

```bash
scripts/run_doc_coverage_cron.sh
```

### Check Status

```bash
cat tmp/cron/doc_coverage_scheduler.pid
ps -fp "$(cat tmp/cron/doc_coverage_scheduler.pid)"
pgrep -af "scripts/doc_coverage_scheduler.py"
```

### Check Past Runs and Logs

- scheduler startup/runtime output: `tmp/cron/doc_coverage_scheduler.out`
- job run log (START/END markers + codex output): `tmp/cron/codex.log`
- most recent final codex message: `tmp/cron/last_message.txt`
- continuity/history from agent perspective: `docs/project/doc_coverage_audit_changelog.md`
- git-level history of changes:

```bash
git log --oneline -- docs/
```

Useful quick checks:

```bash
tail -n 80 tmp/cron/doc_coverage_scheduler.out
tail -n 120 tmp/cron/codex.log
```
