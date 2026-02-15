# Doc Completeness Audit (2026-02-14)

Scope:
- Local docs: `docs/sagemath_lattice_reference.md`, `docs/julia_lattice_methods_reference.md`
- Runtime test surface: method tags from `tests/sage_doc/*.py` and `tests/julia_doc/*.jl`
- External reference: Context7 (`/sagemath/documentation`, `/oscar-system/oscar.jl`)

## Summary

- `docs/sagemath_lattice_reference.md`: broad and high-quality for core lattice workflows, but not exhaustive against the full tested bridge/matrix surface.
- `docs/julia_lattice_methods_reference.md`: near-complete for tested Julia/Oscar surface; only Context7-visible integration omissions were found and patched.

## Measured Coverage Signals

- Sage test method tags discovered: `514`
- Sage tag strings not found verbatim in Sage doc: `288`
- Julia test method tags discovered: `127`
- Julia tag strings not found verbatim in Julia doc: `0`

Notes:
- The Sage "missing" count includes many deep matrix and number-field methods that are secondary to the core lattice API.
- `runtime_coverage` guard tags were excluded from actionable gaps.

## Context7 Comparison Results

Matched in local docs:
- Sage: `IntegralLatticeDirectSum`, `IntegralLatticeGluing`, `enumerate_short_vectors`, `IntegerLattice.shortest_vector`, `QuadraticForm.polynomial`.
- Julia/Oscar: `ZZLatWithIsom` constructors/accessors, `kernel_lattice`, `ambient_isometry`, `order_of_isometry`, `hermitian_structure`.

Originally missing vs Context7 (now patched):
- `Oscar.to_oscar(...)`
- Explicit `ambient_space(Lf)` accessor for `ZZLatWithIsom`
- Explicit `basis_matrix(Lf)` accessor for `ZZLatWithIsom`

## Priority Gaps (Before Patch)

1. Core API omissions
- `IntegerLattice`: `babai`, `update_reduced_basis`, `volume`.

2. Bridge API omissions
- Number-field bridge section lacked explicit list of widely used arithmetic/embedding helpers (`absolute_degree`, `absolute_field`, `real_embeddings`, `class_group`, `S_unit_group`, etc.).

3. Matrix section under-specification
- Matrix-level section omitted many operations used in static tests (`nrows/ncols`, kernels/nullities, `charpoly/minpoly`, row/column transforms, conversion helpers).

## Changes Applied

Updated `docs/julia_lattice_methods_reference.md`:
- Added `ambient_space(Lf)` and `basis_matrix(Lf)` to `ZZLatWithIsom` accessors.
- Added `Oscar.to_oscar(obj)` in Oscar integration points.

Updated `docs/sagemath_lattice_reference.md`:
- Added `IntegerLattice` entries: `babai`, `update_reduced_basis`, `volume`.
- Expanded matrix-level method table with high-use operations (shape, kernels/nullities, polynomial methods, predicates, row/column ops, conversion).
- Added an "Extended number-field API" table in section 17.1.

## Residual Gaps (Not Yet Exhaustively Documented)

Still intentionally non-exhaustive in Sage doc:
- Long tail of advanced `QuadraticForm` local-density/mass internals.
- Full number-field API breadth (e.g. every PARI/BNF helper).
- Full matrix method catalog beyond high-frequency operations.

These can be added in a follow-up pass if strict 1:1 doc-method parity is required.
