# FLINT Method Test Gap Checklist

Tracks FLINT-relevant methods documented in `docs/flint/lattice/flint_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. LLL Context and Reduction

- [ ] `fmpz_lll_context_init_default(fl)`
- [ ] `fmpz_lll_context_init(fl, delta, eta, rt, gt)`
  - Caveat: upstream parameter constraints are `delta in (0.25, 1)` and `eta in (0.5, sqrt(delta))` (both endpoints exclusive).
- [ ] `fmpz_lll(B, U, fl)`
- [ ] `fmpz_lll_with_removal(B, U, gs_B, fl)`
  - Returns: new dimension of `B` after removal.
- [ ] `fmpz_lll_is_reduced(B, fl)`
- [ ] `fmpz_mat_is_reduced(A, fl)`
  - Caveat: low-level floating variants (`fmpz_lll_d`, `fmpz_lll_mpf`) are documented as potentially returning non-reduced output in some cases.

## 2. Hermite Normal Form

- [ ] `fmpz_mat_hnf(H, A)`
- [ ] `fmpz_mat_hnf_transform(H, T, A)`
- [ ] `fmpz_mat_hnf_classical(H, A)`
- [ ] `fmpz_mat_hnf_xgcd(H, A)`
- [ ] `fmpz_mat_hnf_minors(H, A)`
- [ ] `fmpz_mat_hnf_pernet_stein(H, A, state)`
- [ ] `fmpz_mat_hnf_modular(H, A, D)`
- [ ] `fmpz_mat_hnf_modular_eldiv(H, A, D)`
- [ ] `fmpz_mat_is_in_hnf(H)`

## 3. Smith Normal Form

- [ ] `fmpz_mat_snf(S, A)`
- [ ] `fmpz_mat_snf_diagonal(S, A)`
- [ ] `fmpz_mat_snf_kannan_bachem(S, A)`
- [ ] `fmpz_mat_snf_iliopoulos(S, A, mod)`
- [ ] `fmpz_mat_is_in_snf(S)`

---

## Domain Caveat

- FLINT methods here are integer-matrix and Euclidean reduction/normal-form surfaces, not indefinite genus/isometry classification APIs.

---

## References

- `docs/flint/lattice/flint_lattice_reference.md`
- FLINT `fmpz_lll` docs: `https://flintlib.org/doc/fmpz_lll.html`
- FLINT `fmpz_mat` docs: `https://flintlib.org/doc/fmpz_mat.html`
- FLINT docs index: `https://flintlib.org/doc/`

