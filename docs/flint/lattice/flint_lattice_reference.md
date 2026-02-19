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
| `fmpz_lll_context_init_default(fl)` | Initialize default LLL context parameters. | `[ZZMOD, RED, C]` |
| `fmpz_lll_context_init(fl, delta, eta, rt, gt)` | Initialize context with explicit reduction parameters and representation/Gram strategy choices. | `[ZZMOD, RED, C]` |
| `fmpz_lll(B, U, state, fl)` | Main LLL entry point over integer matrix basis, optionally tracking transform matrix `U`. | `[ZZMOD, RED, C]` |
| `fmpz_lll_with_removal(B, U, gs_B, state, fl, new_size)` | LLL-with-removal variant returning reduced rank/size information. | `[ZZMOD, RED, C]` |
| `fmpz_lll_is_reduced(B, fl)` | Predicate checking whether basis meets LLL conditions for context `fl`. | `[ZZMOD, RED, C]` |
| `fmpz_mat_is_reduced(A, fl)` | Matrix-level reducedness predicate under LLL context. | `[ZZMOD, RED, C]` |

Documented parameter constraints:

- `delta` in `(0.25, 1)`,
- `eta` in `(0.5, sqrt(delta))`.

Note: both endpoints are exclusive; default values `delta=0.99`, `eta=0.51` confirm this.

Practical caveat from upstream docs:

- The low-level floating variants (`fmpz_lll_d`, `fmpz_lll_mpf`) can return successfully without guaranteeing reduced output in all cases.

---

## 3. Hermite Normal Form Surface (`fmpz_mat_hnf*`)

| API | Description | Tags |
|-----|-------------|------|
| `fmpz_mat_hnf(H, A)` | Compute Hermite normal form. | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_transform(H, T, A)` | HNF plus transformation matrix output. | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_classical(H, A)` | Classical HNF algorithm entry point (Cohen Algorithm 2.4.4). | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_xgcd(H, A)` | XGCD-accelerated HNF algorithm (Cohen Algorithm 2.4.5). | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_minors(H, A)` | HNF routine using the Kannan-Bachem minors strategy; requires `A` to be full rank. | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_pernet_stein(H, A, state)` | Pernet-Stein randomized HNF variant; requires `flint_rand_t state` for internal randomization. | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_modular(H, A, D)` | Modular HNF (Domich-Kannan-Trotter); requires `A` to be full row-rank and `D` to be a positive multiple of the determinant of the non-zero rows of the HNF. | `[ZZMOD, NF, C]` |
| `fmpz_mat_hnf_modular_eldiv(A, D)` | In-place modular-eldiv HNF; transforms `A` directly; requires `A` of full rank and `D` a positive multiple of its largest elementary divisor. | `[ZZMOD, NF, C]` |
| `fmpz_mat_is_in_hnf(H)` | Predicate that matrix is in HNF shape; returns 1 if so, 0 otherwise. | `[ZZMOD, NF, C]` |

---

## 4. Smith Normal Form Surface (`fmpz_mat_snf*`)

| API | Description | Tags |
|-----|-------------|------|
| `fmpz_mat_snf(S, A)` | Compute Smith normal form. | `[ZZMOD, NF, C]` |
| `fmpz_mat_snf_diagonal(S, A)` | Diagonalization-focused SNF helper. | `[ZZMOD, NF, C]` |
| `fmpz_mat_snf_kannan_bachem(S, A)` | Kannan-Bachem SNF algorithm variant. | `[ZZMOD, NF, C]` |
| `fmpz_mat_snf_iliopoulos(S, A, mod)` | Iliopoulos SNF algorithm variant; requires `A` to be square and nonsingular; `mod` is a modular bound parameter. | `[ZZMOD, NF, C]` |
| `fmpz_mat_is_in_snf(S)` | Predicate that matrix is in SNF shape. | `[ZZMOD, NF, C]` |

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

