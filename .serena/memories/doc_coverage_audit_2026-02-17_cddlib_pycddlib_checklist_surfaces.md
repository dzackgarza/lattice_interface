# Doc Coverage Audit Handoff (2026-02-17): cddlib + pycddlib checklist surfaces

## Objectives addressed
- FIRST GOAL: close missing package-level checklist surfaces for known cdd-family package endpoints used in research workflows.
- SECOND GOAL (targeted): provide source-backed method inventories with argument signatures and domain constraints.

## Completed work
- Added first-class checklist/reference/provenance for `pycddlib`:
  - `docs/pycddlib_methods_checklist.md`
  - `docs/pycddlib/lattice/pycddlib_lattice_reference.md`
  - `docs/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md`
- Added first-class checklist/reference/provenance for `cddlib`:
  - `docs/cddlib_methods_checklist.md`
  - `docs/cddlib/lattice/cddlib_lattice_reference.md`
  - `docs/cddlib/upstream/cddlib_online_provenance_2026-02-17.md`

## Method surfaces captured
- pycddlib:
  - constructors and representation entry points (`Matrix`, `Polyhedron`, `polyhedron_from_matrix`)
  - canonicalization/redundancy APIs (`canonicalize`, `matrix_canonicalize`, redundancy wrappers)
  - adjacency/incidence extractors and H/V conversion accessors
  - LP interfaces (`linprog_from_array`, `linprog_from_matrix`)
- cddlib:
  - CLI drivers (`cdd`, `cddr+`)
  - C API conversion functions (`dd_PolyFile2Matrix`, `dd_DDMatrix2Poly`, ...)
  - adjacency/incidence APIs (`dd_DDInput*`, `dd_DDMatrix2Adjacency`, ...)
  - canonicalization/redundancy/matrix operations and LP APIs (`dd_Matrix2LP`, `dd_LPSolve`, ...)

## Contract/caveat fidelity
- pycddlib docs include explicit H-rep/V-rep row conventions and representation metadata contracts (`rep_type`, `lin_set`).
- cddlib docs include the signature forms provided in canonical cddlib manual pages, with explicit caveat that symbolic parameter names map to internal pointer/set structures.
- Both package surfaces carry explicit non-goal caveat: not indefinite-form genus/isometry classification APIs.

## Sources used
- pycddlib canonical docs + repository:
  - `https://pycddlib.readthedocs.io/en/3.0.2/`
  - `https://pycddlib.readthedocs.io/en/3.0.2/cdd.html`
  - `https://pycddlib.readthedocs.io/en/3.0.2/examples.html`
  - `https://pycddlib.readthedocs.io/en/3.0.2/lp.html`
  - `https://github.com/mcmtroffaes/pycddlib`
- cddlib canonical docs + repository:
  - `https://github.com/cddlib/cddlib`
  - `https://www.cs.mcgill.ca/~fukuda/soft/cddlibman/node1.html`
  - `node2`, `node5`, `node6`, `node7`, `node8`, `node10` under the same manual path

## Commits
- `88efcdc` — docs: add pycddlib package checklist and reference
- `1377142` — docs: add cddlib package checklist surface

## Validation
- Docs-only pass; no runtime test execution attempted.

## Remaining high-impact gaps
1. Add `method:` tagged tests for newly listed cddlib/pycddlib methods so checklist rows can transition from inventory to validated coverage.
2. Add navigation/index references to the two new checklist surfaces when shared index/playbook files are edited in a clean worktree.