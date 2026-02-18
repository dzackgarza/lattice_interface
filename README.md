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

## Agents

This repository defines Codex agents under `agents/`:

- `agents/doc_coverage/`
  - runner: `agents/doc_coverage/run_codex_docs_agent.sh`
  - prompt: `agents/doc_coverage/prompt.md`
  - playbook symlink: `agents/doc_coverage/playbook.md` -> `docs/documentation_coverage_audit_playbook.md`
- `agents/test_coverage/`
  - runner: `agents/test_coverage/run_codex_test_coverage_agent.sh`
  - prompt: `agents/test_coverage/prompt.md`
  - playbook symlink: `agents/test_coverage/playbook.md` -> `docs/test_coverage_playbook.md`

These agents can be run directly or orchestrated via system cron.
