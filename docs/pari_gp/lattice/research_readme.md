# PARI/GP Lattice and Quadratic Form Reference
## Comprehensive matrix/form-oriented lattice methods

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite assumptions |
| `[PSD]` | Positive-semidefinite accepted (positive quadratic form, not necessarily definite) |
| `[DEG]` | Supports degenerate (singular) forms |
| `[INDEF]` | Indefinite-form workflow |
| `[ZZMOD]` | Integer/rational matrix basis setting |
| `[NT]` | Number-theoretic quadratic form workflows |
| `[RED]` | Basis reduction |
| `[ND]` | Non-degenerate (non-zero determinant) required |

---

## 1. Scope

PARI/GP exposes lattice functionality mainly through quadratic-form and matrix APIs (`qf*` family), not through high-level lattice object classes.

Representation model:

- Lattice as basis matrix or Gram matrix.
- Quadratic form as symmetric matrix.
- Algorithms are function-oriented (`qf...`) and can be composed directly.

---

## 2. Core Reduction and Isometry APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qflll(x, {flag = 0})` | `x`: integer matrix; `flag`: integer (optional, default 0) | integer matrix | LLL reduction from basis-style matrix input; returns reduced basis matrix | `[ZZMOD, RED]` |
| `qflllgram(G, {flag = 0})` | `G`: symmetric real matrix (Gram); `flag`: integer (optional, default 0) | integer matrix | LLL-style reduction from Gram matrix input; returns transformation matrix `T` such that `x.T` is LLL-reduced. **Accepts positive quadratic forms (not necessarily definite)** — upstream states G must correspond to a positive quadratic form but x need not have maximal rank | `[PSD, ZZMOD, RED]` |
| `qfcholesky(G)` | `G`: symmetric matrix | matrix or empty vector | Cholesky decomposition; returns `R` such that `^tR * R = G`, or empty `[]` if no solution exists. Unlike `qfcvp`/`qfminim`, upstream docs do not explicitly require positive-definite input; decomposition succeeds only when `G` is positive (semi)definite | `[PSD, RED]` |
| `qfjacobi(G)` | `G`: symmetric real matrix | vector `[L, V]` | Jacobi eigenvalue method for symmetric matrices; returns `L` (eigenvalues sorted increasingly) and `V` (orthogonal eigenvector matrix). **No positive-definite requirement** — upstream applies to any real symmetric matrix. Preferred over `mateigen` for symmetric matrices | `[RED]` |
| `qfisom(G, H, {fl}, {grp})` | `G`, `H`: symmetric integer matrices; `fl`: integer (optional); `grp`: vector (optional) | integer matrix or 0 | Isometry/equivalence test between quadratic forms; returns transformation matrix if equivalent, 0 otherwise. **Requires positive-definite forms** — upstream explicitly states G, H must represent positive definite quadratic forms | `[PD, NT]` |
| `qfisominit(G, {fl}, {m})` | `G`: symmetric integer matrix; `fl`: integer (optional); `m`: integer (optional) | vector | Precomputation structure for repeated `qfisom` calls. **Requires positive-definite form** — upstream explicitly states G must represent a positive definite quadratic form | `[PD, NT]` |
| `qfauto(G, {fl})` | `G`: symmetric integer matrix; `flag`: integer (optional) | vector | Automorphism group computations for forms; returns generating matrices. **Requires positive-definite form** — upstream explicitly states G must represent a positive definite quadratic form | `[PD, NT]` |
| `qfautoexport(qfa, {flag})` | `qfa`: vector (automorphism data); `flag`: integer (optional) | vector | Export/format automorphism data | `[NT]` |
| `qforbits(G, V)` | `G`: matrix group (generators); `V`: vector of vectors | vector | Orbit decomposition for action of a finite matrix group `G` on vectors `V`. **Requires** `G` contains `-I` (minus identity), and `V` should contain only one representative per pair `{v, -v}`; returns 0 if `G` does not stabilize `V` | `[NT]` |

Practical note:

- `qflllgram` accepts positive semidefinite forms (positive quadratic forms, not necessarily definite); the form need not have maximal rank.
- `qfminim`, `qfcvp`, and `qfrep` behavior is undefined for non-positive-definite input; upstream notes a "precision too low" error is likely.
- `qfauto`, `qfisom`, `qfisominit`, `qfperfection` require positive-definite forms (tagged `[PD]` in method entries).
- `qfminimize` requires only non-degenerate forms (non-zero determinant), not positive-definite.
- `qfjacobi`, `qfsign`, `qfsolve`, `qfgaussred` have no positive-definite requirement.

---

## 3. Vector Search and Optimization APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfminim(x, {B}, {m}, {flag = 0})` | `x`: integer matrix; `B`: integer (optional, bound); `m`: integer (optional, limit); `flag`: integer (optional) | vector | Enumerate vectors with bounded quadratic value (or default minimal vectors); returns vector of vectors | `[PD, NT]` |
| `qfminimize(G)` | `G`: symmetric rational matrix with non-zero determinant | vector `[H, U, c]` | Minimization helper workflow for forms; returns `H = c*U~*G*U` with `H` integral and minimal determinant. **No positive-definite requirement** — upstream requires only rational coefficients and non-zero determinant | `[ND, NT]` |
| `qfcvp(x, t, {B}, {m}, {flag = 0})` | `x`: integer matrix (basis); `t`: integer vector (target); `B`, `m`, `flag`: optional integers | integer vector | Closest-vector routine in quadratic-form setting | `[PD, NT]` |
| `qfrep(q, B, {flag = 0})` | `q`: symmetric integer matrix (positive-definite); `B`: integer (bound); `flag`: integer (optional) | vector | Count vectors representing successive integers; returns vector whose i-th entry is half the count of vectors v with q(v) = i. **Requires positive-definite form** — upstream explicitly states q must represent a positive definite quadratic form | `[PD, NT]` |
| `qfeval({q}, x, {y})` | `q`: quadratic form (optional); `x`: integer vector/matrix; `y`: integer vector (optional) | integer | Evaluate quadratic form (or associated bilinear form when `y` is supplied) | `[NT]` |
| `qfnorm(x, {q})` | `x`: integer vector; `q`: quadratic form (optional) | integer | Obsolete norm helper retained for compatibility; use `qfeval` | `[NT]` |
| `qfbil(x, y, {q})` | `x`, `y`: vectors; `q`: quadratic form (optional) | integer | **OBSOLETE** - Bilinear form evaluation; superseded by `qfeval` | `[NT]` |
| `forqfvec(v, q, b, expr)` | `v`: loop variable; `q`: symmetric **integral** matrix (positive-definite); `b`: bound; `expr`: expression | none (loop construct) | Enumerate all pairs of nonzero vectors `(-v, v)` with `q(v) ≤ b`. Loop variable `v` runs through representatives of each pair. **Requires positive-definite integral matrix** — upstream explicitly states q must represent a positive definite quadratic form with integral entries. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §forqfvec (lines 338-370) | `[PD, ZZMOD, NT]` |

---

## 4. Indefinite/Equation-Solving APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfsolve(G)` | `G`: symmetric matrix with **rational coefficients**; `n ≥ 1` | integer vector, matrix, or integer | Solve quadratic equation `^tX G X = 0` over ℚ. Returns: (1) vector `v` (a solution), (2) matrix (columns generate totally isotropic subspace), or (3) integer: prime `p` (no local solution at `p`), `-1` (no real solution), `-2` (n=2 and -det G not a square, implying real solution exists but no local solution at some p dividing det G). **No positive-definite requirement**. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfsolve (lines 2656-2680) | `[INDEF, NT]` |
| `qfparam(G, sol, {flag = 0})` | `G`: symmetric integer matrix; `sol`: integer vector (isotropic); `flag`: integer (optional) | vector | Parametrize conic solutions from known isotropic vector `sol` for ternary forms | `[INDEF, NT]` |
| `qfsign(G)` | `G`: symmetric matrix | vector `[p, m]` | Signature of quadratic form; returns `p` (positive eigenvalues) and `m` (negative eigenvalues). Computed via Gaussian reduction. **No positive-definite requirement** — works for any symmetric matrix | `[INDEF, NT]` |

Use these for indefinite arithmetic problems where shortest-vector Euclidean workflows are not the right abstraction.

---

## 5. Matrix Normal Forms (HNF/SNF)

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `mathnf(M, {flag = 0})` | `M`: matrix with entries in ℤ or K[X] (for some field K); `flag`: integer (optional, default 0) | matrix, `[H, U]`, or `[H, U, P]` depending on flag | Hermite normal form. Returns upper triangular `H` whose columns form a basis of the R-module spanned by columns of `M`. Transformation relation: `M * U = [0 \| H]` (not `U * M = H`). Flags: 0=H only; 1=`[H, U]` with `U ∈ GL(R)`; 4=`[H, U]` via LLL-based reduction (integer-only, provably small U); 5=`[H, U, P]` via Batut's algorithm with row permutation P (integer-only). Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §mathnf (lines 785-899) | `[ZZMOD, NT]` |
| `mathnfmod(x, d)` | `x`: integer matrix of **maximal rank**; `d`: integer, a positive multiple of the (nonzero) determinant of the lattice spanned by the columns of x | matrix | HNF of `x` using determinant bound `d`; uses less memory than `mathnf` but requires prior knowledge of `d` (e.g., from `matdetint`). **Constraint**: `x` must have maximal rank (rank equals number of rows); `d` must be a multiple of the determinant. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §mathnfmod (lines 909-927) | `[ZZMOD, NT]` |
| `mathnfmodid(x, d)` | `x`: integer matrix; `d`: integer or integer vector | matrix | HNF of the concatenation `[x \| diag(d)]`. When `d` is a vector, concatenates `x` with the diagonal matrix having diagonal `d`; when `d` is an integer, concatenates with `d * I`. **Not** a "modular HNF" in the ideal-theoretic sense — the result is the HNF of the extended matrix, not a unimodular transform of `x`. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §mathnfmodid (lines 928-955) | `[ZZMOD, NT]` |
| `matsnf(X, {flag = 0})` | `X`: integer matrix, or square matrix with polynomial entries; `flag`: integer (optional, default 0) | vector or `[U, V, D]` depending on flag | Smith normal form. Default (flag=0): returns vector of elementary divisors `[d_n, ..., d_1]` normalized so that `d_n \| d_{n-1} \| ... \| d_1`. Flag=1 (complete output): returns `[U, V, D]` where `U`, `V` are unimodular and `U*X*V = D`; for non-square `X`, `D` is padded with zeros. Flag=4 (cleanup): deletes divisors equal to 1. Flags can be combined (e.g., flag=5). Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §matsnf (lines 1566-1640) | `[ZZMOD, NT]` |

---

## 6. Binary/Low-Dimensional and Structural APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfgaussred(q, {flag = 0})` | `q`: symmetric matrix; `flag`: integer (optional, default 0) | matrix or vector `[U, V]` | Decomposition into squares of quadratic form; returns matrix M with diagonal entries as square coefficients. **Singular matrices supported** — upstream explicitly handles degenerate forms. If `flag = 1`, returns `[U, V]` with `q = ^tU * diag(V) * U`. Library also provides `qfgaussred_positive` which assumes positive-definite input for faster computation, returning `NULL` if a vector with negative norm occurs. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfgaussred (lines 2117-2174) | `[NT, DEG]` |
| `qfperfection(G)` | `G`: symmetric integer matrix | vector | Perfection/perfect-form style analysis; **requires positive-definite form** per upstream docs; currently rank 8 only | `[PD, NT]` |

---

## 7. Indefinite-First Usage Guidance

For indefinite lattices/forms:

1. Use invariants and solvability (`qfsign`, `qfsolve`).
2. Use parametrization (`qfparam`) once a solution exists.
3. Use isometry/automorphisms (`qfisom`, `qfauto`, `qforbits`) for classification/orbit structure.
4. Treat `qflllgram` as a reduction helper, not as canonical indefinite classification.

---

## 8. Sources

- PARI function index (stable): https://pari.math.u-bordeaux.fr/dochtml/ref-stable/function_index.html
- PARI vectors/matrices + qf APIs: https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Vectors__matrices__linear_algebra_and_sets.html
- Local upstream snapshot: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html`
  - §qfcholesky (lines 1951-1956): no explicit PD requirement, returns `[]` if no solution
  - §qfcvp (lines 1964-1975): requires positive definite; undefined behavior otherwise
  - §qflllgram (lines 2357-2369): "positive quadratic form (not necessarily definite)" — accepts PSD
  - §qfminim (lines 2396-2407): requires positive definite; undefined behavior otherwise
  - §qfminimize (lines 2501-2504): requires non-zero determinant, not positive-definite
  - §qfjacobi (lines 2238-2246): "real symmetric matrix" — no PD requirement
  - §qfrep (lines 2614-2616): requires positive definite
  - §forqfvec (lines 338-370): loop over vectors with bounded norm; requires positive-definite integral matrix
  - §qfsolve (lines 2656-2680): returns vector/matrix/integer; requires rational coefficients; no PD requirement
  - §qfsign (lines 2645-2648): returns [p, m] signature — no PD requirement
  - §qfgaussred (lines 2133-2134): "Singular matrices are supported"
  - §mathnf (lines 785-899): Hermite normal form; assumes ℤ base ring
  - §mathnfmod (lines 909-927): modular HNF; less memory than mathnf
  - §mathnfmodid (lines 928-955): HNF modulo ideal; returns unimodular matrix
  - §matsnf: Smith normal form; returns elementary divisors
- Local provenance capture: `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI docs home: https://pari.math.u-bordeaux.fr/
- Sage PARI bridge docs for `qfsolve`/`qfparam`: https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html
