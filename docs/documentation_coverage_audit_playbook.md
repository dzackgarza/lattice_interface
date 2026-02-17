# Documentation Coverage Audit Playbook

## Audience and Purpose

This document is for autonomous documentation agents.

Purpose: improve lattice-theoretic documentation coverage quality over repeated runs.

## Job Contract

Each run should produce one coherent documentation audit/improvement pass that leaves the repository's documentation quality measurably better, or a justified no-edit outcome.

## Scope

In scope:

- documentation auditing,
- documentation completion,
- documentation organization.

Out of scope:

- code implementation,
- runtime behavior changes,
- test-surface manipulation.

## Non-Negotiables

- Never check off checklist items.
- Never hide missing methods by narrowing scope or expanding ignore lists.
- Never replace precise mathematical contracts with vague wording.
- Never claim method coverage from memory when local source snapshots or canonical references are required.

## Quality Standard

Documentation edits should:

- be source-backed,
- use exact runtime method naming when practical,
- include caveats where mathematically necessary,
- improve discoverability and consistency across related docs,
- avoid unsupported extrapolation.

## Autonomy

The agent chooses planning, breadth, sequencing, and depth.

Use broad edits when needed to complete coherent improvements. Avoid artificial micro-pass constraints.

## Required Artifacts Per Pass

Update `docs/project/doc_coverage_audit_changelog.md` with:

- a pre-pass entry,
- a post-pass entry containing:
  - edits and rationale,
  - intentional non-edits,
  - remaining gaps,
  - prioritized handoff tasks,
  - commit hash (or `none` for no-edit passes).

## Commit Policy

- If documentation files changed, commit is mandatory.
- If no documentation files changed, do not force a content-only commit.

Preferred commit format:

`docs(audit): pass <PASS_ID> <target> <audit|add|clarify|reconcile>`

## Canonical Inputs

At minimum, consider:

- `README.md`
- `TEST_QUALITY.md`
- `AGENTS.md`
- `docs/sage_methods_checklist.md`
- `docs/julia_methods_checklist.md`
- `docs/lattice_wrapper_capability_checklist.md`
- `docs/method_ground_truth_tracker.csv`
- source manifests and local upstream snapshots under `docs/**/upstream/`

## Completion Criterion

Continue making passes over time until repeated audits find no high-signal improvements and remaining gaps are either explicitly queued or source-blocked.
