# PARI/GP Lattice and Quadratic Form Reference
## Comprehensive matrix/form-oriented lattice methods

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite assumptions |
| `[PSD]` | Positive-semidefinite accepted (positive quadratic form, not necessarily definite) |
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
| `qflll(x, {flag = 0})` | `x`: integer matrix; `flag`: integer (optional, default 0) | integer matrix | LLL reduction from basis-style matrix input; returns reduced basis matrix | `[ZZMOD, RED]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qflll |
| `qflllgram(G, {flag = 0})` | `G`: symmetric real matrix (Gram); `flag`: integer (optional, default 0) | integer matrix | LLL-style reduction from Gram matrix input; returns transformation matrix `T` such that `x.T` is LLL-reduced. **Accepts positive quadratic forms (not necessarily definite)** — upstream states G must correspond to a positive quadratic form but x need not have maximal rank | `[PSD, ZZMOD, RED]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qflllgram |
| `qfcholesky(G)` | `G`: symmetric matrix | matrix or empty vector | Cholesky decomposition; returns `R` such that `^tR * R = G`, or empty `[]` if no solution exists. Unlike `qfcvp`/`qfminim`, upstream docs do not explicitly require positive-definite input; decomposition succeeds only when `G` is positive (semi)definite | `[RED]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfcholesky |
| `qfjacobi(G)` | `G`: symmetric real matrix | vector `[L, V]` | Jacobi eigenvalue method for symmetric matrices; returns `L` (eigenvalues sorted increasingly) and `V` (orthogonal eigenvector matrix). **No positive-definite requirement** — upstream applies to any real symmetric matrix. Preferred over `mateigen` for symmetric matrices | `[RED]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfjacobi |
| `qfisom(G, H, {fl}, {grp})` | `G`, `H`: symmetric integer matrices or `qfisominit` structure (for `G`); `fl`: `t_VEC` `[depth, bacher_level]` (optional, same semantics as in `qfisominit`); `grp`: vector of generator matrices — automorphism group of `H` (optional, speeds up computation; can be obtained from `qfauto(H)`) | integer matrix or 0 | Isometry/equivalence test between quadratic forms; returns invertible matrix `S` such that `G = ^t(S) H S` if isometric, 0 otherwise. `G` may be passed as a `qfisominit` structure (preferred when comparing many forms against the same `G`). **Requires positive-definite forms** — upstream explicitly states G, H must represent positive definite quadratic forms. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfisom | `[PD, NT]` |
| `qfisominit(G, {fl}, {m})` | `G`: symmetric integer matrix; `fl`: `t_VEC` `[depth, bacher_level]` (optional); `m`: matrix or `qfminim` output (optional) — set of vectors with squared norm ≤ max diagonal entry of `G`; if absent, computed internally (expensive for large dimension) | vector (isom structure) | Precomputation structure for repeated `qfisom`/`qfauto` calls against `G`. `fl[1]` = depth of scalar product combination; `fl[2]` = maximum level of Bacher polynomials; these control the invariants used and can trade speed vs. quality. **Requires positive-definite form** — upstream explicitly states G must represent a positive definite quadratic form. **Interface is experimental and may change in future releases.** Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfisominit | `[PD, NT]` |
| `qfauto(G, {fl})` | `G`: symmetric integer matrix or `qfisominit` structure; `fl`: `t_VEC` `[depth, bacher_level]` (optional, same semantics as in `qfisominit`) | vector `[o, g]` where `o` is the group order (integer) and `g` is a vector of generator matrices (each `H` satisfying `G = ^t(H) G H`) | Automorphism group of the lattice defined by `G`. **Requires positive-definite form** — upstream explicitly states G must represent a positive definite quadratic form. **Interface is experimental and may change in future releases.** Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfauto | `[PD, NT]` |
| `qfautoexport(qfa, {flag})` | `qfa`: vector (automorphism data); `flag`: integer (optional) | vector | Export/format automorphism data | `[NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfautoexport |
| `qforbits(G, V)` | `G`: matrix group (generators); `V`: vector of vectors | vector | Orbit decomposition for action of a finite matrix group `G` on vectors `V`. **Requires** `G` contains `-I` (minus identity), and `V` should contain only one representative per pair `{v, -v}`; returns 0 if `G` does not stabilize `V` | `[NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qforbits |

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
| `forqfvec(v, q, b, expr)` | `v`: formal variable (identifier); `q`: square symmetric integer matrix (positive definite quadratic form); `b`: integer (bound on q(v)); `expr`: GP expression | void (iterator) | Iterate over all pairs (-v, v) of nonzero vectors such that q(v) ≤ b, evaluating `expr` for each representative v. **Requires positive-definite integer form** — upstream explicitly states q must be a square symmetric integral matrix representing a positive definite quadratic form. Outputs exactly one representative per antipodal pair. Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §forqfvec | `[PD, NT]` |
| `qfminim(x, {B}, {m}, {flag = 0})` | `x`: integer matrix; `B`: integer (optional, bound); `m`: integer (optional, limit); `flag`: integer (optional) | vector | Enumerate vectors with bounded quadratic value (or default minimal vectors); returns vector of vectors | `[PD, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfminim |
| `qfminimize(G)` | `G`: symmetric rational matrix with non-zero determinant | vector `[H, U, c]` | Minimization helper workflow for forms; returns `H = c*U~*G*U` with `H` integral and minimal determinant. **No positive-definite requirement** — upstream requires only rational coefficients and non-zero determinant | `[ND, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfminimize |
| `qfcvp(x, t, {B}, {m}, {flag = 0})` | `x`: integer matrix (basis); `t`: integer vector (target); `B`, `m`, `flag`: optional integers | integer vector | Closest-vector routine in quadratic-form setting | `[PD, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfcvp |
| `qfrep(q, B, {flag = 0})` | `q`: symmetric integer matrix (positive-definite); `B`: integer (bound); `flag`: integer (optional) | vector | Count vectors representing successive integers; returns vector whose i-th entry is half the count of vectors v with q(v) = i. **Requires positive-definite form** — upstream explicitly states q must represent a positive definite quadratic form | `[PD, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfrep |
| `qfeval({q}, x, {y})` | `q`: quadratic form (optional); `x`: integer vector/matrix; `y`: integer vector (optional) | integer | Evaluate quadratic form (or associated bilinear form when `y` is supplied) | `[NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfeval |
| `qfnorm(x, {q})` | `x`: integer vector; `q`: quadratic form (optional) | integer | Obsolete norm helper retained for compatibility; use `qfeval` | `[NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfeval (marked obsolete) |
| `qfbil(x, y, {q})` | `x`, `y`: vectors; `q`: quadratic form (optional) | integer | **OBSOLETE** - Bilinear form evaluation; superseded by `qfeval` | `[NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfbil (marked obsolete) |

---

## 4. Indefinite/Equation-Solving APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfsolve(G)` | `G`: symmetric integer matrix | integer vector or 0 | Solve isotropy/zero-representation equation for form `G`; returns vector or 0 | `[INDEF, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfsolve |
| `qfparam(G, sol, {flag = 0})` | `G`: symmetric integer matrix; `sol`: integer vector (isotropic); `flag`: integer (optional) | vector | Parametrize conic solutions from known isotropic vector `sol` for ternary forms | `[INDEF, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfparam |
| `qfsign(G)` | `G`: symmetric matrix | vector `[p, m]` | Signature of quadratic form; returns `p` (positive eigenvalues) and `m` (negative eigenvalues). Computed via Gaussian reduction. **No positive-definite requirement** — works for any symmetric matrix | `[INDEF, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfsign |

Use these for indefinite arithmetic problems where shortest-vector Euclidean workflows are not the right abstraction.

---

## 5. Binary/Low-Dimensional and Structural APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfgaussred(q, {flag = 0})` | `q`: symmetric matrix; `flag`: integer (optional, default 0) | matrix or vector `[U, V]` | Decomposition into squares of quadratic form; returns matrix M with diagonal entries as square coefficients. **Singular matrices supported** — upstream explicitly handles degenerate forms. If `flag = 1`, returns `[U, V]` with `q = ^tU * diag(V) * U` | `[NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfgaussred |
| `qfperfection(G)` | `G`: symmetric integer matrix | vector | Perfection/perfect-form style analysis; **requires positive-definite form** per upstream docs; currently rank 8 only | `[PD, NT]` | `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfperfection |

---

## 6. Indefinite-First Usage Guidance

For indefinite lattices/forms:

1. Use invariants and solvability (`qfsign`, `qfsolve`).
2. Use parametrization (`qfparam`) once a solution exists.
3. Use isometry/automorphisms (`qfisom`, `qfauto`, `qforbits`) for classification/orbit structure.
4. Treat `qflllgram` as a reduction helper, not as canonical indefinite classification.

---

## 7. Sources

- PARI function index (stable): https://pari.math.u-bordeaux.fr/dochtml/ref-stable/function_index.html
- PARI vectors/matrices + qf APIs: https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Vectors__matrices__linear_algebra_and_sets.html
- Local upstream snapshot: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html`
  - §qfcholesky (lines 1951-1956): no explicit PD requirement, returns `[]` if no solution
  - §qfcvp (lines 1964-1975): requires positive definite; undefined behavior otherwise
  - §forqfvec (lines 336-366): "square and symmetric integral matrix representing a positive definite quadratic form"; iterates over all antipodal pairs with q(v) ≤ b
  - §qflllgram (lines 2357-2369): "positive quadratic form (not necessarily definite)" — accepts PSD
  - §qfminim (lines 2396-2407): requires positive definite; undefined behavior otherwise
  - §qfminimize (lines 2501-2504): requires non-zero determinant, not positive-definite
  - §qfjacobi (lines 2238-2246): "real symmetric matrix" — no PD requirement
  - §qfrep (lines 2614-2616): requires positive definite
  - §qfsign (lines 2645-2648): returns [p, m] signature — no PD requirement
  - §qfgaussred (lines 2133-2134): "Singular matrices are supported"
- Local provenance capture: `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI docs home: https://pari.math.u-bordeaux.fr/
- Sage PARI bridge docs for `qfsolve`/`qfparam`: https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html
