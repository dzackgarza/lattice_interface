# Doc Coverage Audit Handoff (2026-02-17): CddInterface + NConvex checklist surfaces

## Objective addressed
- FIRST GOAL: ensure checklist coverage surfaces exist for known lattice-relevant package ecosystems; close remaining GAP package-level checklist gaps.
- SECOND GOAL (partial for new surfaces): provide source-backed method signatures/constraints where canonical docs are retrievable; explicitly triage source-blocked method inventories when not retrievable.

## Completed work
- Added first-class checklist/reference/provenance surfaces for `CddInterface`:
  - `docs/cddinterface_methods_checklist.md`
  - `docs/cddinterface/lattice/cddinterface_lattice_reference.md`
  - `docs/cddinterface/upstream/cddinterface_online_provenance_2026-02-17.md`
- Added first-class checklist/reference/provenance surfaces for `NConvex` (with explicit source-blocked triage status):
  - `docs/nconvex_methods_checklist.md`
  - `docs/nconvex/lattice/nconvex_lattice_reference.md`
  - `docs/nconvex/upstream/nconvex_online_provenance_2026-02-17.md`
- Wired both package surfaces into umbrella docs:
  - `docs/gap_methods_checklist.md` (expanded Cdd methods + explicit NConvex detailed-surface section + references)
  - `docs/gap/lattice/gap_lattice_methods_reference.md` (expanded Cdd representative/indexed methods; explicit NConvex method-index blocker note)
  - `docs/documentation_coverage_audit_playbook.md` (core references + upstream living map entries)
  - `docs/project/doc_coverage_audit_changelog.md` (new pass `20260217-14` + commit hash updates)

## Source survey used
- CddInterface package/docs:
  - `https://homalg-project.github.io/CddInterface/`
  - `https://homalg-project.github.io/CddInterface/doc/chap0_mj.html`
  - `https://homalg-project.github.io/CddInterface/doc/chap2_mj.html`
  - `https://homalg-project.github.io/CddInterface/doc/chap3_mj.html`
  - `https://homalg-project.github.io/CddInterface/doc/chap4_mj.html`
- NConvex package/repo:
  - `https://gap-packages.github.io/NConvex/`
  - `https://github.com/homalg-project/NConvex`

## Key decisions
- Elevated CddInterface and NConvex from umbrella-only mentions to dedicated top-level checklist surfaces.
- For CddInterface, documented additional method families from chapters 2-4 (`Cdd_InteriorPoint`, `Cdd_ExtendLinearity`, `Cdd_FacesWithInteriorPoints`, `Cdd_LinearProgram`, `Cdd_FourierProjection`, etc.).
- For NConvex, intentionally avoided speculative method signatures due inaccessible canonical method-index endpoints; created explicit triage status and provenance to preserve continuity.
- Kept all new checklist boxes unchecked (no `method:`-tagged test evidence introduced in this pass).

## Commits
- `071aecf` — docs: add cddinterface and nconvex checklist surfaces
- `5a979aa` — docs: record pass 20260217-14 commit hash

## Validation / environment notes
- Shell network fetch to external package hosts is blocked in this environment (`curl` cannot resolve host), so source survey relied on web retrieval paths.
- Left unrelated dirty/untracked files untouched (`scripts/doc_coverage_scheduler.py`, `.serena/`, `scripts/__pycache__/`).

## Remaining high-impact gaps
1. Retrieve canonical NConvex manual method-index pages and expand method-level checklist/reference contracts.
2. Add `method:`-tagged tests for representative CddInterface and NConvex methods before any checklist completion-state changes.
3. Optionally normalize changelog pass `20260217-14` commit-hash field to include both pass commits (`071aecf`, `5a979aa`) if strict multi-commit tracking is required.
