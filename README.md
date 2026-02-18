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

## Automation (System Cron)

This repo now uses system `crontab` directly. The single job entrypoint is:

- `scripts/run_doc_coverage_cron.sh`

### Prerequisites

Required commands:

- `/usr/bin/codex`
- `uvx` (used by Serena MCP setup)

Quick check:

```bash
command -v codex
command -v uvx
```

### Configure Serena MCP (Required)

One-time setup:

```bash
codex mcp add serena -- \
  uvx --from git+https://github.com/oraios/serena \
  serena start-mcp-server --project-from-cwd
```

Verify configuration:

```bash
codex mcp list
codex mcp get serena --json
```

### Install Crontab Entry

From repo root (`/home/dzack/lattice_interface`):

```bash
mkdir -p tmp/cron
scripts/run_doc_coverage_cron.sh
```

Add this line with `crontab -e`:

```cron
*/15 * * * * /home/dzack/lattice_interface/scripts/run_doc_coverage_cron.sh
```

### Manual Run

```bash
scripts/run_doc_coverage_cron.sh
```

### Logs and Outputs

- run log (START/END markers + codex output): `tmp/cron/codex.log`
- most recent final codex message: `tmp/cron/last_message.txt`
- continuity/history from agent perspective: `docs/project/doc_coverage_audit_changelog.md`

Useful quick checks:

```bash
crontab -l
tail -n 120 tmp/cron/codex.log
cat tmp/cron/last_message.txt
```

### Troubleshooting

- no scheduled runs visible:
  - confirm entry exists with `crontab -l`
  - run once manually: `scripts/run_doc_coverage_cron.sh`
  - inspect `tmp/cron/codex.log`
- MCP misconfiguration:
  - inspect log output for Serena MCP errors
  - rerun setup in `Configure Serena MCP (Required)`
