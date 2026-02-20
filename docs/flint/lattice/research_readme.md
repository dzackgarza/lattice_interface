# FLINT Lattice and Integer-Matrix Reference
## `fmpz` reduction and normal-form APIs

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[ZZMOD]` | Integer matrix / `fmpz` model |
| `[RED]` | Reduction workflow |
| `[NF]` | Normal-form workflow |
| `[C]` | C API surface |
| `[FULLRANK]` | No rank restriction; algorithm handles arbitrary-rank input |
| `[FULLCOLRANK]` | Requires full column rank (rank = number of columns) |
| `[FULLROWRANK]` | Requires full row rank (rank = number of rows) |
| `[SQUARE]` | Requires square matrix |
| `[NONSING]` | Requires nonsingular matrix |
| `[INPLACE]` | Transforms input matrix in place; output aliases input |

---

## 1. Scope

FLINT exposes lattice-relevant functionality through integer matrix routines:

- LLL reduction (`fmpz_lll*`),
- Hermite normal form (`fmpz_mat_hnf*`),
- Smith normal form (`fmpz_mat_snf*`).

These are matrix-algorithm APIs, not high-level indefinite-lattice classification objects.

---

## 2. LLL Surface (`fmpz_lll`)

| API | Description | Tags |
|-----|-------------|------|
| `fmpz_lll_context_init_default(fl)` | Initialize default LLL context parameters (delta=0.99, eta=0.51, rt=Z_BASIS, gt=APPROX). Source: `fmpz_lll.h` | `[ZZMOD, RED, C]` |
| `fmpz_lll_context_init(fl, delta, eta, rt, gt)` | Initialize context with explicit reduction parameters. `[delta in (0.25, 1), eta in (0.5, sqrt(delta))]` Both endpoints exclusive. Source: `fmpz_lll.h` | `[ZZMOD, RED, C]` |
| `fmpz_lll(B, U, fl)` | Main LLL entry point over integer matrix basis, optionally tracking transform matrix `U`. `[INPLACE]` Reduces `B` in place. Source: `fmpz_lll.h` | `[ZZMOD, RED, C]` |
| `fmpz_lll_with_removal(B, U, gs_B, fl)` | LLL-with-removal variant. `[INPLACE]` Reduces `B` in place and removes vectors whose **squared** Gram-Schmidt length exceeds `gs_B`. Returns new dimension of `B` after removal. Source: `fmpz_lll.h` | `[ZZMOD, RED, C]` |
| `fmpz_lll_is_reduced(B, fl, prec)` | **Conclusive** reducedness check. `prec`: `flint_bitcnt_t` bit precision for the internal float check. Return value is always conclusive: non-zero means definitively reduced, zero means definitively not reduced. Calls heuristic `_d` or `_mpfr` variants first and returns early if they yield a conclusive answer. Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness" | `[ZZMOD, RED, C]` |
| `fmpz_lll_is_reduced_d(B, fl)` | **Heuristic** (inconclusive) reducedness check at machine (double) precision. Non-zero return means definitely reduced; **zero return is inconclusive** — does not prove unreduced. Delegates to `fmpz_mat_is_reduced` or `fmpz_mat_is_reduced_gram`. Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness" | `[ZZMOD, RED, C]` |
| `fmpz_mat_is_reduced(A, delta, eta)` | Low-level basis reducedness predicate. `delta`, `eta`: `double` — explicit LLL parameters (not a context object). Returns non-zero if `A` is LLL-reduced with the given `(delta, eta)`. Companion: `fmpz_mat_is_reduced_gram(A, delta, eta)` for Gram-matrix input. Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction" | `[ZZMOD, RED, C]` |

Practical caveat from upstream docs:

- The low-level floating variants (`fmpz_lll_d`, `fmpz_lll_mpf`) can return successfully without guaranteeing reduced output in all cases.
- The `fmpz_lll` function is the main user entry point; it currently calls ULLL internally.
- `fmpz_lll_is_reduced(B, fl, prec)` is conclusive; `fmpz_lll_is_reduced_d(B, fl)` is heuristic (zero return does not prove the basis is unreduced).

---

## 3. Hermite Normal Form Surface (`fmpz_mat_hnf*`)

| API | Description | Tags |
|-----|-------------|------|
| `fmpz_mat_hnf(H, A)` | Compute Hermite normal form. `[FULLRANK]` No rank restriction; algorithm auto-selects based on matrix characteristics. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_transform(H, U, A)` | HNF plus transformation matrix output; returns `U` such that `UA = H`. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_classical(H, A)` | Classical HNF algorithm (Cohen Algorithm 2.4.4). Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_xgcd(H, A)` | XGCD-accelerated HNF algorithm (Cohen Algorithm 2.4.5). Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_minors(H, A)` | HNF via Kannan-Bachem minors strategy. `[FULLCOLRANK]` Requires `A` to be full column rank. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_pernet_stein(H, A, state)` | Pernet-Stein randomized HNF variant; requires `flint_rand_t state` for internal randomization. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_modular(H, A, D)` | Modular HNF (Domich-Kannan-Trotter). `[FULLROWRANK]` Requires `A` to be full row rank and `D` to be a positive multiple of the determinant of the non-zero rows of the HNF. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_modular_eldiv(A, D)` | In-place modular HNF via elementary divisors. `[FULLCOLRANK, INPLACE]` Requires `A` to be full column rank and `D` to be a positive multiple of the largest elementary divisor of `A`. Transforms `A` directly. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_is_in_hnf(H)` | Predicate that matrix is in HNF shape; returns 1 if so, 0 otherwise. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |

---

## 4. Smith Normal Form Surface (`fmpz_mat_snf*`)

| API | Description | Tags |
|-----|-------------|------|
| `fmpz_mat_snf(S, A)` | Compute Smith normal form. `[FULLRANK]` No rank restriction; algorithm auto-selects based on matrix characteristics. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_snf_diagonal(S, A)` | Diagonalization-focused SNF helper; requires `A` to be diagonal. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_snf_kannan_bachem(S, A)` | Kannan-Bachem SNF algorithm variant. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_snf_iliopoulos(S, A, mod)` | Iliopoulos SNF algorithm variant. `[SQUARE, NONSING]` Requires `A` to be nonsingular `n×n`. Parameter `mod` is a modular bound for intermediate computations. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |
| `fmpz_mat_is_in_snf(S)` | Predicate that matrix is in SNF shape. Source: `fmpz_mat.h` | `[ZZMOD, NF, C]` |

---

## 5. Domain Caveat

FLINT surfaces here are Euclidean/integer matrix algorithms. They do not provide genus/discriminant-form/isometry-class APIs for indefinite arithmetic lattices.

---

## 6. Sources

- FLINT `fmpz_lll` docs: `https://flintlib.org/doc/fmpz_lll.html`
- FLINT `fmpz_mat` docs (HNF/SNF families): `https://flintlib.org/doc/fmpz_mat.html`
- FLINT docs index: `https://flintlib.org/doc/`
- Local upstream snapshot: `docs/flint/upstream/fmpz_lll.rst` (LLL surface; parameter constraints verified from this file)
- Local upstream snapshot: `docs/flint/upstream/fmpz_mat.rst` (HNF/SNF signatures verified from this file)

