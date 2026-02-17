# Documentation Coverage Audit Playbook

## Audience

Documentation workers.

## Worker Job

Your job is to perform documentation auditing and improvement work for this repository.
Target outcome: documentation accounts for all lattice-theoretic methods and mathematically relevant contracts known across the active ecosystem, with explicit assumptions and source-backed caveats.

## Mathematical Orientation (Project-Specific)

This is a mathematics-first documentation project.

Documentation quality is measured by mathematical signal, not procedural completion.

Priority mathematical surfaces include:

- indefinite lattice methods and workflows,
- local/global/rational isometry and equivalence classification,
- genus, local symbols, and discriminant-form machinery,
- lattices/forms over `Z_p` and local Jordan/p-adic normal-form families with their input assumptions,
- automorphism/orthogonal-group structure and lattice embedding/overlattice operations.

Lower priority unless tied to lattice-mathematical contracts:

- generic matrix plumbing with no lattice/form-specific semantics.

## Execution Ownership

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
- Continue through additional clear, source-backed improvements whenever they remain available in scope.

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
- Preserve invariants and semantics explicitly (for example signature, determinant/discriminant, genus/discriminant-form contracts).

### Source Discipline

- Tie substantive claims to local source snapshots/manifests or canonical upstream docs.
- Use online survey/research to discover newly relevant method surfaces across the active ecosystem.
- Refresh/add local snapshots when required for reliable verification.
- Localize critical online evidence into repo docs (snapshots/manifests) so future audits remain reproducible offline.
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

### No Weak Deferral

Do not defer with weak placeholders such as `unknown`, `unverified`, `needs testing`, or similar when the question is reasonably answerable by:

- reading available documentation,
- surveying relevant online sources,
- reading source code,
- comparing nearby method contracts/invariants.

Such deferments are acceptable only when the blocker is real and explicit (for example missing upstream source, contradictory primary sources, or unavailable dependency context), and the blocker must be documented concretely.

These are project-wide quality values, not checks scoped to any particular subset of text.
Apply them continuously across the full documentation surface throughout the audit.

## Continuous Quality Questions

Use these questions continuously during planning, editing, and review:

- Are there online packages/docs with lattice algorithms not yet represented in our documentation surfaces?
- Do the docs clearly help a human understand what methods/tools are available and when to use them?
- Is the current organization cohesive and easy to navigate across checklists and detailed references?
- Do older docs need restructuring/reorganization to improve mathematical clarity or discoverability?
- Did any edit remove mathematically relevant information?
- Did I review `git diff` and validate that changes improve quality against these questions?
- Were edits grounded in real source documents/snapshots rather than assumptions or innate knowledge?
- Did I make any mathematical assumptions not clearly evidenced in source docs?
- Did I leave out critical assumptions (for example, positive-definite-only or ring/domain constraints)?
- Did I reconcile differing definitions/assumptions of lattices across sources where needed?
- Did I introduce restrictions or authoritative statements that are not explicitly documented?
- Is language anywhere in the touched documentation surface vague or mathematically imprecise?
- Am I improving project-wide clarity and precision rather than only patching local wording?
- Are improvements grounded in checkable/provable statements?
- Did I introduce vague claims such as `usually`, `typically`, `often`, or `most of the time` where exact truth values are available?
- Did I leave any weak deferrals (`unknown`, `unverified`, `needs testing`) that could have been resolved through reasonable documentation/source research?

## Execution Strategy

Work in repeated internal cycles during an assignment:

1. Build/refresh a ranked set of unresolved high-impact documentation gaps from current docs, changelog continuity notes, and upstream survey.
2. Select the highest-value in-scope cluster (not a single isolated typo-level edit).
3. Apply cohesive updates across related surfaces (checklist + detailed reference + provenance notes where needed).
4. Review git diff for mathematical precision, contract consistency, and evidence grounding.
5. Continue to the next highest-value unresolved cluster while meaningful improvements remain.

Treat each completed chunk as progress toward the broader assignment and continue with the next highest-value unresolved cluster.
Treat the assignment as complete when you judge the top-level goal has been achieved: full source-backed coverage of lattice-theoretic methods known in the active ecosystem.

## Required Artifacts Per Execution

Update `docs/project/doc_coverage_audit_changelog.md` with:

- execution continuity entries containing:
  - concise summary of completed work,
  - key decisions and intentional non-edits,
  - remaining gaps,
  - prioritized handoff tasks for future workers,
  - commit hash(es) (or `none` for no-edit outcomes).

Changelog structure is adaptive: do not enforce rigid templates. Format entries to fit current history and evolving requirements while keeping continuity clear.
Use git commits as the detailed change ledger; use changelog entries for continuity, context, and handoffs.

## Commit Requirements

- If documentation files changed, commit is mandatory.
- If no documentation files changed, do not force a content-only commit.

Commit message format is flexible. Include enough detail for future auditing and traceability.

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

## Known Upstream Project Repositories (Living Map)

Use these as primary upstream anchors when surveying for missing methods, changing contracts, and ecosystem drift.
Treat this list as living and update it when better canonical sources are identified.

- SageMath:
  - source: `https://github.com/sagemath/sage`
  - docs: `https://doc.sagemath.org`
- Oscar.jl:
  - source: `https://github.com/oscar-system/Oscar.jl`
  - docs: `https://docs.oscar-system.org`
- Hecke.jl:
  - source: `https://github.com/thofma/Hecke.jl`
  - docs: `https://docs.hecke.thofma.com`
- Nemo.jl (official):
  - source: `https://github.com/Nemocas/Nemo.jl`
  - docs: `https://nemocas.github.io/Nemo.jl/stable/`
- AbstractAlgebra.jl (upstream dependency surface used by OSCAR/Nemo):
  - source: `https://github.com/Nemocas/AbstractAlgebra.jl`
  - docs: `https://nemocas.github.io/AbstractAlgebra.jl/stable/`
- GAP system:
  - source: `https://github.com/gap-system/gap`
  - main docs hub: `https://www.gap-system.org/doc/`
  - release manuals (HTML): `https://docs.gap-system.org/doc/ref/chap0.html`
  - docs source location in repo: `https://github.com/gap-system/gap/tree/master/doc`
  - package docs/index: `https://gap-packages.github.io`
  - package repos org: `https://github.com/gap-packages`
  - GAP-maintained GitHub Pages hub: `https://gap-system.github.io/`
- fplll / fpylll:
  - fplll source: `https://github.com/fplll/fplll`
  - fpylll source: `https://github.com/fplll/fpylll`
- PARI/GP:
  - project site: `https://pari.math.u-bordeaux.fr`
  - VCS/development gateway: `https://pari.math.u-bordeaux.fr/git.html`

When using online survey results:

- resolve ambiguous package names to the mathematically relevant project (for example official `Nemo.jl` vs unrelated projects named \"Nemo\"),
- localize critical references into repository docs/snapshot structure for reproducibility,
- record provenance in changelog continuity notes.

## Long-Run Completion Signal

Across scheduled executions, completion is approached when repeated audits yield no further high-signal, source-backed improvements and remaining gaps are explicitly documented as blocked or lower-priority.
