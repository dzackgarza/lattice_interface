# Doc Coverage Audit Handoff (2026-02-17): g6k + flatter + LattE Integrale checklist surfaces

## Objective addressed
- FIRST GOAL: create missing checklist surfaces for known lattice-method packages absent from current top-level checklist map.
- SECOND GOAL (for new surfaces): add source-backed method/argument/constraint documentation for each new package.

## Completed work
- Added first-class checklist + detailed reference + upstream provenance surfaces for:
  - `g6k`
    - `docs/g6k_methods_checklist.md`
    - `docs/g6k/lattice/g6k_lattice_reference.md`
    - `docs/g6k/upstream/g6k_online_provenance_2026-02-17.md`
  - `flatter`
    - `docs/flatter_methods_checklist.md`
    - `docs/flatter/lattice/flatter_lattice_reference.md`
    - `docs/flatter/upstream/flatter_online_provenance_2026-02-17.md`
  - `LattE Integrale`
    - `docs/latte_integrale_methods_checklist.md`
    - `docs/latte_integrale/lattice/latte_integrale_lattice_reference.md`
    - `docs/latte_integrale/upstream/latte_integrale_online_provenance_2026-02-17.md`
- Captured method/command inventories and argument surfaces from canonical upstream docs/source:
  - g6k README + `g6k/siever.pyx` API declarations,
  - flatter README command/options and utility scripts,
  - LattE project site + official user-guide PDF command synopsis/options.
- Added explicit domain caveats for all three surfaces (Euclidean/polyhedral focus; no indefinite-form genus/isometry contract surface).

## Key decisions
- Prioritized package-surface creation over wording refinement.
- Kept checklist boxes unchecked (no new method-tagged test evidence in this pass).
- Did not edit pre-existing dirty files (`README.md`, `docs/documentation_coverage_audit_playbook.md`, `scripts/doc_coverage_scheduler.py`).

## Validation
- Per-file content sanity checks completed via local reads/grep.
- No runtime tests executed (documentation-only package-surface expansion).

## Remaining high-impact gaps
1. Navigation/index reconciliation: add these new checklist surfaces into stable global navigation/playbook/index files once those files are edited in a clean context.
2. Signature-fidelity deepening:
   - g6k: expand beyond core `Siever` methods to additional documented APIs if/when upstream renders fuller API docs.
   - LattE Integrale: extend option-level coverage for `count`/`integrate`/optimization subcommands beyond currently captured high-impact options.
3. Continue ecosystem survey for additional in-practice lattice stacks still lacking first-class checklist surfaces (e.g., additional reduction/enumeration tools with canonical docs).
4. Add `method:`-tagged tests for representative methods from these new packages before any checklist status promotion.

## Commit
- `3992ccc`