# Doc Coverage Audit Handoff (2026-02-17): lrslib + polymake checklist surfaces

## Objective addressed
- FIRST GOAL: add checklist coverage surfaces for known lattice-method package ecosystems missing first-class top-level checklists.
- SECOND GOAL (triage/completeness): capture source-backed method/argument/type/constraint surfaces for newly added packages; explicitly flag source-access blockers.

## Completed work
- Added new first-class checklist + reference + upstream provenance surfaces for `lrslib`:
  - `docs/lrslib_methods_checklist.md`
  - `docs/lrslib/lattice/lrslib_lattice_reference.md`
  - `docs/lrslib/upstream/lrslib_online_provenance_2026-02-17.md`
- Added new first-class checklist + reference + upstream provenance surfaces for `polymake`:
  - `docs/polymake_methods_checklist.md`
  - `docs/polymake/lattice/polymake_lattice_reference.md`
  - `docs/polymake/upstream/polymake_online_provenance_2026-02-17.md`
- Appended continuity entry to changelog:
  - `docs/project/doc_coverage_audit_changelog.md` (Pass ID `20260217-16`).

## Source survey used
- lrslib canonical pages:
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/USERGUIDE.html`
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/lrslib.html`
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrs.1`
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/mplrs.1`
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrsnash.1`
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/fel.1`
- lrslib supplemental manpage mirrors for helper surfaces:
  - `https://www.mankier.com/1/polyv`
  - `https://manpages.debian.org/testing/lrslib/xref.1.en.html`
  - `https://www.mankier.com/1/lrsscripts`
- polymake pages:
  - `https://polymake.org/`
  - `https://github.com/polymake/polymake`
  - target API docs discovered: `https://polymake.org/release_docs/3.2/polytope.html`

## Key decisions
- Elevated both ecosystems to first-class top-level checklist surfaces rather than leaving them undocumented.
- Kept all checklist boxes unchecked (no method-tagged test evidence introduced in this pass).
- For polymake, documented direct-fetch blocker (HTTP 403 to release docs in this environment) and retained explicit signature-fidelity caveat.

## Intentional non-edits
- Did not modify unrelated pre-existing dirty/untracked files:
  - `README.md`
  - `docs/documentation_coverage_audit_playbook.md`
  - `scripts/doc_coverage_scheduler.py`
  - `.serena/`
  - `scripts/__pycache__/`
- Did not update `docs/method_ground_truth_tracker.csv`.

## Validation
- Documentation-only pass; no runtime tests executed.

## Remaining high-impact gaps
1. polymake signature-fidelity pass from directly retrievable release docs (or local docs build) is still needed.
2. Add `method:`-tagged tests for representative lrslib and polymake methods before any checklist completion-state updates.

## Prioritized follow-up tasks
1. Perform direct polymake method-signature extraction and tighten type/argument contracts in:
   - `docs/polymake/lattice/polymake_lattice_reference.md`
   - `docs/polymake_methods_checklist.md`
   - `docs/polymake/upstream/polymake_online_provenance_2026-02-17.md`
2. Add method-tagged tests and tracker linkage for lrslib/polymake high-impact methods in:
   - `tests/**`
   - `docs/method_ground_truth_tracker.csv`
   - new checklist files.

## Commit
- `592730d` — docs: add lrslib and polymake checklist surfaces