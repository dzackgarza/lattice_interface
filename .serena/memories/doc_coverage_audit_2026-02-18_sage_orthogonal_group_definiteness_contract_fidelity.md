# Doc Coverage Audit Handoff (2026-02-18): Sage `IntegralLattice.orthogonal_group` definiteness constraint

## Objectives covered
- FIRST GOAL (cursory package-surface maintenance): reviewed current checklist inventory and prior handoff memories; no clear new in-scope bilinear-form lattice package surface requiring a new checklist was identified in this pass.
- SECOND GOAL (active phase focus): corrected a source-backed contract-fidelity error in the Sage `IntegralLattice.orthogonal_group` definiteness constraint.

## The error
- Previous documentation tagged `IntegralLattice.orthogonal_group(gens=None, is_finite=None)` as `[PD]` (positive definite only) in three separate locations.
- Upstream local snapshot (`free_quadratic_module_integer_symmetric.html`) explicitly demonstrates that **negative definite** lattices (e.g. `IntegralLattice(-Matrix(ZZ, 2, [2,1,1,2]))`) work with `orthogonal_group()` and return a correct group.
- Only **indefinite** lattices raise `NotImplementedError: currently, we can only compute generators for orthogonal groups over definite lattices.`
- Therefore the correct constraint is `[DEFINITE]` (positive or negative definite), not `[PD]`.

## Completed edits
1. `docs/sage/integral_lattice/sage_integral_lattice_reference.md`
   - Method table: `[PD]` → `[DEFINITE]` for both `orthogonal_group` and `automorphisms` alias.
   - Caveat text: "requires positive definite lattice" → "requires a **definite** lattice (positive definite or negative definite); indefinite forms raise `NotImplementedError`".
   - Definiteness summary table: ND row now lists `orthogonal_group (automatic)` as available; INDEF row updated to note the `NotImplementedError`.

2. `docs/sage/lattice/sagemath_lattice_reference.md`
   - Method table §3 Symmetry: `[PD only — indefinite not yet implemented]` → `[DEFINITE — indefinite raises NotImplementedError]`; alias row `[PD only]` → `[DEFINITE]`.
   - Pitfalls §13: "requires positive definite" → "requires a **definite** lattice (positive or negative definite)" in two separate bullet points.

3. `docs/TODO.md`
   - Added and checked off Goal 2 contract-fidelity item for this pass.

## Source evidence
- Local upstream snapshot: `docs/sage/integral_lattice/upstream/free_quadratic_module_integer_symmetric.html`
  - Section `orthogonal_group`: example with `A2m = IntegralLattice(-Matrix(ZZ, 2, [2,1,1,2]))` → `A2m.orthogonal_group()` returns group of order 12 (succeeds).
  - Section `orthogonal_group`: example with `U = IntegralLattice(Matrix(ZZ, 2, [0,1,1,0]))` → `U.orthogonal_group()` raises `NotImplementedError: currently, we can only compute generators for orthogonal groups over definite lattices.`

## Commit
- `08c2e42` — docs: correct IntegralLattice.orthogonal_group definiteness constraint from [PD] to [DEFINITE]

## Validation
- Documentation-only pass; no runtime tests executed.

## Intentional non-edits
- Did not modify unrelated pre-existing dirty files:
  - `README.md`, `docs/documentation_coverage_audit_playbook.md`, `prompt.md`, `scripts/doc_coverage_scheduler.py`
  - untracked `.serena/`, `scripts/__pycache__/`

## Remaining high-impact gaps
1. Sage checklist has many unchecked `IntegralLattice` methods: `IntegralLattice(data, basis=None)`, `IntegralLatticeDirectSum`, `IntegralLatticeGluing`, `orthogonal_group`, `genus()`, `local_modification`, `twist`, `is_primitive`, `direct_sum`, `quadratic_form` — all undocumented with `method:` tagged tests.
2. Julia §2.3 Construction, §2.4 Intrinsic data, §2.8 Automorphism/isometry, §2.9 Module operations, §2.14 most accessors/attributes/operations remain entirely unchecked.
3. Missing local doc copies still open in TODO.md (flint, gap, ntl, fpylll, forms, g6k, crystallographic_stack, pari_gp).
