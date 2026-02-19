# PARI/GP Lattice and Quadratic Form Reference
## Comprehensive matrix/form-oriented lattice methods

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite assumptions |
| `[INDEF]` | Indefinite-form workflow |
| `[ZZMOD]` | Integer/rational matrix basis setting |
| `[NT]` | Number-theoretic quadratic form workflows |
| `[RED]` | Basis reduction |

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
| `qflllgram(G, {flag = 0})` | `G`: symmetric integer matrix (Gram); `flag`: integer (optional, default 0) | integer matrix | LLL-style reduction from Gram matrix input; returns reduced Gram matrix | `[PD, ZZMOD, RED]` |
| `qfcholesky(G)` | `G`: symmetric matrix | matrix or empty vector | Cholesky decomposition; returns `R` such that `^tR * R = G`, or empty `[]` if no solution exists. Unlike `qfcvp`/`qfminim`, upstream docs do not explicitly require positive-definite input; decomposition succeeds only when `G` is positive (semi)definite | `[RED]` |
| `qfjacobi(G)` | `G`: symmetric real matrix | vector | Jacobi eigenvalue method for symmetric matrices; returns eigenvalues and eigenvectors | `[PD]` |
| `qfisom(G, H, {fl}, {grp})` | `G`, `H`: symmetric integer matrices; `fl`: integer (optional); `grp`: vector (optional) | integer matrix or 0 | Isometry/equivalence test between quadratic forms; returns transformation matrix if equivalent, 0 otherwise. **Requires positive-definite forms** — upstream explicitly states G, H must represent positive definite quadratic forms | `[PD, NT]` |
| `qfisominit(G, {fl}, {m})` | `G`: symmetric integer matrix; `fl`: integer (optional); `m`: integer (optional) | vector | Precomputation structure for repeated `qfisom` calls. **Requires positive-definite form** — upstream explicitly states G must represent a positive definite quadratic form | `[PD, NT]` |
| `qfauto(G, {fl})` | `G`: symmetric integer matrix; `flag`: integer (optional) | vector | Automorphism group computations for forms; returns generating matrices. **Requires positive-definite form** — upstream explicitly states G must represent a positive definite quadratic form | `[PD, NT]` |
| `qfautoexport(qfa, {flag})` | `qfa`: vector (automorphism data); `flag`: integer (optional) | vector | Export/format automorphism data | `[NT]` |
| `qforbits(G, V)` | `G`: matrix group (generators); `V`: vector of vectors | vector | Orbit decomposition for action of a finite matrix group `G` on vectors `V`. **Requires** `G` contains `-I` (minus identity), and `V` should contain only one representative per pair `{v, -v}`; returns 0 if `G` does not stabilize `V` | `[NT]` |

Practical note:

- `qflllgram` is primarily a positive-definite workflow; outside that regime results may be heuristic/non-canonical.
- `qfminim` and `qfcvp` behavior is undefined for non-positive-definite input; upstream notes a "precision too low" error is likely.
- `qfauto`, `qfisom`, `qfisominit` require positive-definite forms (now tagged `[PD]` in method entries).

---

## 3. Vector Search and Optimization APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfminim(x, {B}, {m}, {flag = 0})` | `x`: integer matrix; `B`: integer (optional, bound); `m`: integer (optional, limit); `flag`: integer (optional) | vector | Enumerate vectors with bounded quadratic value (or default minimal vectors); returns vector of vectors | `[PD, NT]` |
| `qfminimize(G)` | `G`: symmetric integer matrix | vector | Minimization helper workflow for forms | `[PD, NT]` |
| `qfcvp(x, t, {B}, {m}, {flag = 0})` | `x`: integer matrix (basis); `t`: integer vector (target); `B`, `m`, `flag`: optional integers | integer vector | Closest-vector routine in quadratic-form setting | `[PD, NT]` |
| `qfrep(q, B, {flag = 0})` | `q`: integer; `B`: integer matrix; `flag`: integer (optional) | vector | Representation routines for quadratic forms | `[NT]` |
| `qfeval({q}, x, {y})` | `q`: quadratic form (optional); `x`: integer vector/matrix; `y`: integer vector (optional) | integer | Evaluate quadratic form (or associated bilinear form when `y` is supplied) | `[NT]` |
| `qfnorm(x, {q})` | `x`: integer vector; `q`: quadratic form (optional) | integer | Obsolete norm helper retained for compatibility; use `qfeval` | `[NT]` |
| `qfbil(x, y, {q})` | `x`, `y`: vectors; `q`: quadratic form (optional) | integer | **OBSOLETE** - Bilinear form evaluation; superseded by `qfeval` | `[NT]` |

---

## 4. Indefinite/Equation-Solving APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfsolve(G)` | `G`: symmetric integer matrix | integer vector or 0 | Solve isotropy/zero-representation equation for form `G`; returns vector or 0 | `[INDEF, NT]` |
| `qfparam(G, sol, {flag = 0})` | `G`: symmetric integer matrix; `sol`: integer vector (isotropic); `flag`: integer (optional) | vector | Parametrize conic solutions from known isotropic vector `sol` for ternary forms | `[INDEF, NT]` |
| `qfsign(G)` | `G`: symmetric integer matrix | vector (3 components) | Signature-related analysis of form; returns [p, n, nullity] | `[INDEF, NT]` |

Use these for indefinite arithmetic problems where shortest-vector Euclidean workflows are not the right abstraction.

---

## 5. Binary/Low-Dimensional and Structural APIs

| Function | Argument Types | Return Type | Description | Tags |
|----------|----------------|-------------|-------------|------|
| `qfgaussred(q, {flag = 0})` | `q`: integer (binary form discriminant) or integer matrix; `flag`: integer (optional) | vector | Gauss reduction of binary quadratic forms | `[NT]` |
| `qfperfection(G)` | `G`: symmetric integer matrix | vector | Perfection/perfect-form style analysis; **requires positive-definite form** per upstream docs; currently rank 8 only | `[PD, NT]` |

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
- Local upstream snapshot: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` (§qfcholesky: no explicit PD requirement unlike qfcvp/qfminim)
- Local provenance capture: `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI docs home: https://pari.math.u-bordeaux.fr/
- Sage PARI bridge docs for `qfsolve`/`qfparam`: https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html
