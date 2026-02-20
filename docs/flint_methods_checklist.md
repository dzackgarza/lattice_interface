# FLINT Method Test Gap Checklist

Tracks FLINT-relevant methods documented in `docs/flint/lattice/flint_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. LLL Context and Reduction

### Context Initialization

- [ ] `fmpz_lll_context_init_default(fl)`
- [ ] `fmpz_lll_context_init(fl, delta, eta, rt, gt)`
  - Caveat: upstream parameter constraints are `delta in (0.25, 1)` and `eta in (0.5, sqrt(delta))` (both endpoints exclusive).
- [ ] `fmpz_lll_randtest(fl, state)`

### Main LLL Functions

- [ ] `fmpz_lll(B, U, fl)`
- [ ] `fmpz_lll_with_removal(B, U, gs_B, fl)`
  - Returns: new dimension of `B` after removal.

### LLL Variants (Floating-Point)

- [ ] `fmpz_lll_d(B, U, fl)`
  - Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_d_heuristic(B, U, fl)`
  - Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_d_with_removal(B, U, gs_B, fl)`
  - Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_d_heuristic_with_removal(B, U, gs_B, fl)`
  - Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_mpf2(B, U, prec, fl)`
- [ ] `fmpz_lll_mpf(B, U, fl)`
  - Returns: 0 on success, -1 if precision maxes out.
- [ ] `fmpz_lll_mpf_with_removal(B, U, gs_B, fl)`
- [ ] `fmpz_lll_wrapper(B, U, fl)`
- [ ] `fmpz_lll_wrapper_with_removal(B, U, gs_B, fl)`
- [ ] `fmpz_lll_d_with_removal_knapsack(B, U, gs_B, fl)`
  - Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_wrapper_with_removal_knapsack(B, U, gs_B, fl)`

### ULLL (Unscheduled LLL)

- [ ] `fmpz_lll_with_removal_ulll(FM, UM, new_size, gs_B, fl)`
- [ ] `fmpz_lll_storjohann_ulll(FM, new_size, fl)`
  - Caveat: not tested, use at own risk.

### LLL Reducedness Checking

- [ ] `fmpz_lll_is_reduced(B, fl, prec)`
  - Returns: conclusive (non-zero if reduced, zero if not).
- [ ] `fmpz_lll_is_reduced_d(B, fl)`
  - Returns: non-zero = definitely reduced, zero = inconclusive.
- [ ] `fmpz_lll_is_reduced_mpfr(B, fl, prec)`
- [ ] `fmpz_lll_is_reduced_with_removal(B, fl, gs_B, newd, prec)`
  - Returns: conclusive.
- [ ] `fmpz_lll_is_reduced_d_with_removal(B, fl, gs_B, newd)`
- [ ] `fmpz_lll_is_reduced_mpfr_with_removal(B, fl, gs_B, newd, prec)`

### Reducedness Checking (Direct)

- [ ] `fmpz_mat_is_reduced(A, delta, eta)`
- [ ] `fmpz_mat_is_reduced_gram(A, delta, eta)`
  - Assumes: `A` is the Gram matrix of the basis.
- [ ] `fmpz_mat_is_reduced_with_removal(A, delta, eta, gs_B, newd)`
- [ ] `fmpz_mat_is_reduced_gram_with_removal(A, delta, eta, gs_B, newd)`

### Classical LLL

- [ ] `fmpz_mat_lll_original(A, delta, eta)`
- [ ] `fmpz_mat_lll_storjohann(A, delta, eta)`

## 2. Hermite Normal Form

- [ ] `fmpz_mat_hnf(H, A)`
  - Aliasing: allowed.
- [ ] `fmpz_mat_hnf_transform(H, T, A)`
  - Returns: `H` and transformation matrix `U` where `UA = H`.
- [ ] `fmpz_mat_hnf_classical(H, A)`
- [ ] `fmpz_mat_hnf_xgcd(H, A)`
- [ ] `fmpz_mat_hnf_modular(H, A, D)`
  - Constraint: `A` assumed rank `n`, `D` positive multiple of det of non-zero rows of `H`.
- [ ] `fmpz_mat_hnf_modular_eldiv(A, D)`
  - Constraint: `A` rank `n`, `D` positive multiple of largest elementary divisor.
- [ ] `fmpz_mat_hnf_minors(H, A)`
  - Constraint: `A` assumed rank `n`.
- [ ] `fmpz_mat_hnf_pernet_stein(H, A, state)`
- [ ] `fmpz_mat_is_in_hnf(A)`
  - Returns: 1 if in HNF, 0 otherwise.

## 3. Smith Normal Form

- [ ] `fmpz_mat_snf(S, A)`
- [ ] `fmpz_mat_snf_diagonal(S, A)`
  - Constraint: `A` must be diagonal matrix.
- [ ] `fmpz_mat_snf_kannan_bachem(S, A)`
- [ ] `fmpz_mat_snf_iliopoulos(S, A, mod)`
  - Constraint: `A` must be nonsingular `n x n`.
- [ ] `fmpz_mat_is_in_snf(A)`
  - Returns: 1 if in SNF, 0 otherwise.

## 4. Gram Matrix

- [ ] `fmpz_mat_gram(B, A)`
  - Description: computes Gram matrix of lattice spanned by rows of `A`.

---

## Domain Caveat

- FLINT methods here are integer-matrix and Euclidean reduction/normal-form surfaces, not indefinite genus/isometry classification APIs.

---

## References

- `docs/flint/lattice/flint_lattice_reference.md`
- FLINT `fmpz_lll` docs: `https://flintlib.org/doc/fmpz_lll.html`
- FLINT `fmpz_mat` docs: `https://flintlib.org/doc/fmpz_mat.html`
- FLINT docs index: `https://flintlib.org/doc/`

