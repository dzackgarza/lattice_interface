# Documentation Coverage Audit Playbook

## Audience

Autonomous documentation agents.

## Objective

Increase lattice-theoretic documentation coverage quality over repeated scheduled executions.

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

Documentation changes should be:

- source-backed,
- method-precise,
- mathematically explicit,
- caveat-aware where needed,
- consistent across related docs.

## Operating Model

- Handoff tasks and recent changelog gaps are starting signals.
- Do not stop after the first valid fix if adjacent high-signal improvements remain.
- Expand audit breadth as needed while quality gradient remains positive.
- Work until the scoped audit objective is reasonably complete for the current execution.

## Required Run Artifacts

Update `docs/project/doc_coverage_audit_changelog.md` with:

- a pre-run record,
- a post-run record containing:
  - edits and rationale,
  - intentional non-edits,
  - remaining gaps,
  - prioritized next handoff tasks,
  - commit hash (or `none` for no-edit outcomes).

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

## Long-Run Completion Signal

Across scheduled executions, the process approaches completion when repeated audits find no high-signal improvements and remaining gaps are explicitly queued or clearly source-blocked.
