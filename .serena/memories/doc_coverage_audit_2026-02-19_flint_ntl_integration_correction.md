# FLINT/NTL Integration Verification and Corrections (2026-02-19)

## What Was Wrong

### FLINT (`docs/flint/lattice/flint_lattice_reference.md`)
All errors verified against `docs/flint/upstream/fmpz_lll.rst` and `docs/flint/upstream/fmpz_mat.rst`.

1. **eta interval**: Reference said `[0.5, sqrt(delta))` (closed). Upstream says `(0.5, sqrt(delta))` (open). Fixed.
2. **`fmpz_mat_hnf_xgcd`**: Existed in upstream (Cohen 2.4.5), missing from reference. Added.
3. **`fmpz_mat_hnf_pernet_stein`**: Reference showed `(H, A)` — missing `flint_rand_t state` third argument. Fixed.
4. **`fmpz_mat_hnf_modular_eldiv`**: Reference showed `(H, A, D)` with separate output H. Upstream is in-place: `(A, D)` — A is modified directly. Also requires A to be full rank and D to be a positive multiple of the largest elementary divisor. Fixed.
5. **`fmpz_mat_snf_iliopoulos`**: Reference showed `(S, A)`, missing `mod` parameter. Upstream: `(S, A, mod)`. Also: requires A to be square and nonsingular. Fixed.

### NTL (`docs/ntl/lattice/ntl_lattice_reference.md`)
All errors verified against `docs/ntl/upstream/LLL.txt`.

1. **`LatticeSolve` return value**: Reference said "returns image determinant". Upstream says "returns 1 if solvable, 0 if not". Fixed.
2. **`LLL_plus` first parameter**: Reference said `ZZ& det2`. Upstream: `vec_ZZ& D` — a vector where `D[i]/D[i-1]` = squared Gram-Schmidt length of i-th vector. Fixed.
3. **Missing rational delta overloads**: `LLL(det2, B, a, b, verbose)` and `LLL(det2, B, U, a, b, verbose)` existed in upstream but were absent from reference. Added.

## Goal 1 Status
All 8 previously flagged packages now have verified local upstream docs. TODO.md updated to reflect Goal 1 COMPLETE.

## Remaining Work (Goal 2)
- GAP Forms: type annotations for all arguments and return values
- SageMath: explicit type annotations
- Julia/Hecke.jl: explicit type annotations
