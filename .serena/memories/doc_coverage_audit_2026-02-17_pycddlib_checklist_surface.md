# Doc Coverage Audit Handoff (2026-02-17): pycddlib checklist surface

## Objective addressed
- FIRST GOAL: add checklist coverage surface for a known lattice/polyhedral package missing from repository checklists.
- SECOND GOAL (targeted): document method-level signatures, argument/type surfaces, and representation constraints from canonical upstream docs.

## Completed work
- Added first-class package checklist surface:
  - `docs/pycddlib_methods_checklist.md`
- Added detailed method reference:
  - `docs/pycddlib/lattice/pycddlib_lattice_reference.md`
- Added upstream provenance snapshot:
  - `docs/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md`

## Method surfaces captured
- Constructors/entry points: `Matrix(...)`, `polyhedron_from_matrix(...)`, `Polyhedron(...)`
- Canonicalization/redundancy: `canonicalize`, `matrix_canonicalize`, `matrix_redundancy_remove`, `redundancy_remove`, `redundancy_remove_from_array`, `matrix_rank`
- Adjacency/incidence/extraction: matrix and polyhedron copy/adjacency/incidence methods
- LP surface: `linprog_from_array`, `linprog_from_matrix`

## Contract/caveat fidelity
- Included source-backed representation contracts:
  - H-rep row convention `[b A]` with `0 <= b + A x`
  - V-rep row convention `[t V]` with documented `t=0` ray / `t=1` vertex examples
  - `rep_type`/`lin_set` metadata requirements
- Added explicit domain caveat that pycddlib is polyhedral/LP tooling and not indefinite genus/isometry classification.

## Sources used
- `https://pycddlib.readthedocs.io/en/3.0.2/`
- `https://pycddlib.readthedocs.io/en/3.0.2/cdd.html`
- `https://pycddlib.readthedocs.io/en/3.0.2/examples.html`
- `https://pycddlib.readthedocs.io/en/3.0.2/lp.html`
- `https://github.com/mcmtroffaes/pycddlib`

## Commit
- `88efcdc` — docs: add pycddlib package checklist and reference

## Validation
- No runtime/tests executed; this pass is docs-only and source-backed.

## Remaining high-impact gaps
1. Evaluate whether direct `cddlib` C/CLI package should get its own first-class checklist surface (separate from GAP `CddInterface` and Python `pycddlib`).
2. Add `method:` tagged tests for pycddlib methods listed in the new checklist so coverage can move from inventory to validated status.
3. If docs navigation/index surfaces are reconciled in a clean worktree, add explicit links to the new pycddlib checklist/reference.