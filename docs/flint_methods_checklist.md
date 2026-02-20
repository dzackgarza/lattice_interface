# FLINT Method Test Gap Checklist

Tracks FLINT-relevant methods documented in `docs/flint/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. LLL Context and Reduction

- [ ] `fmpz_lll_context_init_default(fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Parameter manipulation"
- [ ] `fmpz_lll_context_init(fl, delta, eta, rt, gt)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Parameter manipulation"
      Caveat: upstream parameter constraints are `delta in (0.25, 1)` and `eta in (0.5, sqrt(delta))` (both endpoints exclusive).
- [ ] `fmpz_lll(B, U, fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Main LLL functions"
- [ ] `fmpz_lll_with_removal(B, U, gs_B, fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Main LLL functions"
      Returns: new dimension of `B` after removal.
- [ ] `fmpz_lll_is_reduced(B, fl, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Note: `prec` is `flint_bitcnt_t` bit precision for the internal float check; return value is always conclusive.
- [ ] `fmpz_lll_is_reduced_with_removal(B, fl, gs_B, newd, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Note: Conclusive reducedness check with removal; `prec` is `flint_bitcnt_t`.
- [ ] `fmpz_lll_is_reduced_d(B, fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
- [ ] `fmpz_lll_is_reduced_mpfr(B, fl, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
- [ ] `fmpz_lll_is_reduced_d_with_removal(B, fl, gs_B, newd)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
- [ ] `fmpz_lll_is_reduced_mpfr_with_removal(B, fl, gs_B, newd, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
- [ ] `fmpz_mat_lll_original(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Classical LLL"
      Note: Classical LLL; `delta`, `eta` are `fmpq_t` rationals.
- [ ] `fmpz_mat_lll_storjohann(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Modified LLL"
      Note: Storjohann variant with improved dimension complexity; `delta`, `eta` are `fmpq_t`.
- [ ] `fmpz_mat_is_reduced(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Caveat: low-level floating variants (`fmpz_lll_d`, `fmpz_lll_mpf`) are documented as potentially returning non-reduced output in some cases.
      Note: `delta` and `eta` are `double` LLL parameters.
- [ ] `fmpz_mat_is_reduced_gram(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Note: Assumes `A` is the Gram matrix of the basis.
- [ ] `fmpz_mat_is_reduced_with_removal(A, delta, eta, gs_B, newd)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Note: Low-level with-removal predicate.
- [ ] `fmpz_mat_is_reduced_gram_with_removal(A, delta, eta, gs_B, newd)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Note: Gram matrix version with removal.

## 2. Hermite Normal Form

- [ ] `fmpz_mat_hnf(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_transform(H, T, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_classical(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_xgcd(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_minors(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_pernet_stein(H, A, state)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_modular(H, A, D)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_modular_eldiv(H, A, D)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_is_in_hnf(H)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"

## 3. Smith Normal Form

- [ ] `fmpz_mat_snf(S, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
- [ ] `fmpz_mat_snf_diagonal(S, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
- [ ] `fmpz_mat_snf_kannan_bachem(S, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
- [ ] `fmpz_mat_snf_iliopoulos(S, A, mod)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
      Caveat: requires `A` to be nonsingular `n×n`.
- [ ] `fmpz_mat_is_in_snf(S)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"

---

## Domain Caveat

- FLINT methods here are integer-matrix and Euclidean reduction/normal-form surfaces, not indefinite genus/isometry classification APIs.

---

## References

- `docs/flint/lattice/research_readme.md`
- FLINT `fmpz_lll` docs: `https://flintlib.org/doc/fmpz_lll.html`
- FLINT `fmpz_mat` docs: `https://flintlib.org/doc/fmpz_mat.html`
- FLINT docs index: `https://flintlib.org/doc/`

