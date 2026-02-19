# GAP Core: NormalFormIntMat and Decomposition Signature Fidelity (2026-02-18)

## What was wrong

Both `NormalFormIntMat` and `Decomposition` were documented with `(...)` placeholder signatures in:
- `docs/gap/lattice/gap_lattice_methods_reference.md`
- `docs/gap_methods_checklist.md`

## What is now correct

### NormalFormIntMat(mat, options)
- `mat`: integer matrix (n×m)
- `options`: integer bitmask (0–31+16): bit 0 = SNF (1) vs triangular/HNF (0); bit 1 = reduce off-diagonal; bit 2 = include row transforms; bit 3 = include col transforms; bit 4 (value 16) = destructive
- Returns: record with `normal` (computed form), optionally `rowtrans` (n×n unimodular) / `coltrans` (m×m unimodular), `signdet`, `rank`
- Source: `docs/gap/upstream/matint.gd §NormalFormIntMat`

### Decomposition(A, B, depth)
- `A`: m×n cyclotomic matrix, rank m ≤ n
- `B`: list of cyclotomic vectors of length n
- `depth`: nonneg integer (p-adic iterations, prime p=83 by default, auto-advanced if singular) or string "nonnegative" (assumes nonneg solutions, auto-computes iterations; first column of A must be positive)
- Returns: list; entry i = integer solution x s.t. x*A = B[i], or `fail` if no (nonneg integral) solution
- Source: `docs/gap/upstream/chap25.html §25.4-1`

## Intentional non-edits
- Checklist items remain `[ ]` (no static doc tests exist for these methods yet)
- `DecompositionInt(A, B, depth)` already had correct signature in reference; not changed

## Commit
51a9d73
