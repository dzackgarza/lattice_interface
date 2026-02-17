# Documentation Coverage Audit Playbook

## Audience

Autonomous documentation agents.

## Objective

Improve lattice-theoretic documentation coverage quality over repeated executions.

## Agent Autonomy

You are responsible for choosing execution strategy.

- Choose planning, breadth, sequencing, and depth.
- Use broad or narrow edits as needed.
- Optimize for net documentation quality improvement under the constraints below.

## Hard Constraints

- Documentation work only.
- No code implementation or runtime behavior changes.
- No test-surface manipulation.
- Never check off checklist items.
- Never hide missing methods by narrowing coverage boundaries or expanding ignore lists.
- Never replace precise mathematical contracts with vague language.
- Never claim method coverage from memory when local snapshots or canonical references are required.

## Documentation Quality Requirements

### Coverage Integrity

- Track real method surfaces, not aliases or accounting shortcuts.
- Prefer explicit method-level accountability.
- Close missing-method gaps where source evidence exists.
- Keep unresolved gaps explicit and actionable.

### Mathematical Precision

- State contracts in mathematically meaningful terms.
- Include caveats for domain/definiteness/input assumptions when required.
- Avoid content-free statements and weak generic phrasing.

### Source Discipline

- Tie substantive claims to local source snapshots/manifests or canonical upstream docs.
- Refresh/add local snapshots when required for reliable verification.
- Do not elevate uncertain inference to fact.

### Consistency and Organization

- Keep related checklist and reference surfaces aligned.
- Resolve contradictory caveat wording across files.
- Improve discoverability (section structure, nearby method grouping) when it clarifies auditability.

### Negative-Gradient Avoidance

Do not make edits that are net-zero or negative quality gradient, including:

- pure reword churn with no precision gain,
- deletions that reduce provenance,
- speculative expansion without evidence,
- organizational churn that increases lookup cost.

## Required Artifacts Per Execution

Update `docs/project/doc_coverage_audit_changelog.md` with:

- a pre-run record,
- a post-run record containing:
  - edits and rationale,
  - intentional non-edits,
  - remaining gaps,
  - prioritized handoff tasks,
  - commit hash (or `none` for no-edit outcomes).

## Commit Requirements

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

Across scheduled executions, completion is approached when repeated audits produce no high-signal improvements and remaining gaps are explicitly queued or clearly source-blocked.
