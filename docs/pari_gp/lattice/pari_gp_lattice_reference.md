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

| Function | Description | Tags |
|----------|-------------|------|
| `qflll(x, {flag = 0})` | LLL reduction from basis-style matrix input | `[ZZMOD, RED]` |
| `qflllgram(G, {flag = 0})` | LLL-style reduction from Gram matrix input | `[PD, ZZMOD, RED]` |
| `qfisom(G, H, {fl}, {grp})` | Isometry/equivalence test between quadratic forms | `[NT]` |
| `qfisominit(G, {fl}, {m})` | Precomputation structure for repeated `qfisom` calls | `[NT]` |
| `qfauto(G, {fl})` | Automorphism group computations for forms | `[NT]` |
| `qfautoexport(qfa, {flag})` | Export/format automorphism data | `[NT]` |
| `qforbits(G, V)` | Orbit decomposition for action of a finite matrix group `G` on vectors `V` | `[NT]` |

Practical note:

- `qflllgram` is primarily a positive-definite workflow; outside that regime results may be heuristic/non-canonical.
- `qfauto`, `qfisom`, and `qfisominit` are documented for integer positive-definite forms.
- `qforbits` requires `G` to include `-I` and `V` to contain one representative per pair `{v, -v}`.

---

## 3. Vector Search and Optimization APIs

| Function | Description | Tags |
|----------|-------------|------|
| `qfminim(x, {B}, {m}, {flag = 0})` | Enumerate vectors with bounded quadratic value (or default minimal vectors) | `[PD, NT]` |
| `qfminimize(G)` | Minimization helper workflow for forms | `[PD, NT]` |
| `qfcvp(x, t, {B}, {m}, {flag = 0})` | Closest-vector routine in quadratic-form setting | `[PD, NT]` |
| `qfrep(q, B, {flag = 0})` | Representation routines for quadratic forms | `[NT]` |
| `qfeval({q}, x, {y})` | Evaluate quadratic form (or associated bilinear form when `y` is supplied) | `[NT]` |
| `qfnorm(x, {q})` | Obsolete norm helper retained for compatibility; use `qfeval` | `[NT]` |

---

## 4. Indefinite/Equation-Solving APIs

| Function | Description | Tags |
|----------|-------------|------|
| `qfsolve(G)` | Solve isotropy/zero-representation equation for form `G` | `[INDEF, NT]` |
| `qfparam(G, sol, {flag = 0})` | Parametrize conic solutions from known isotropic vector `sol` for ternary forms | `[INDEF, NT]` |
| `qfsign(G)` | Signature-related analysis of form | `[INDEF, NT]` |

Use these for indefinite arithmetic problems where shortest-vector Euclidean workflows are not the right abstraction.

---

## 5. Binary/Low-Dimensional and Structural APIs

| Function | Description | Tags |
|----------|-------------|------|
| `qfgaussred(q, {flag = 0})` | Gauss reduction of binary quadratic forms | `[NT]` |
| `qfperfection(G)` | Perfection/perfect-form style analysis (currently rank 8 only in upstream docs) | `[NT]` |

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
- Local provenance capture: `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI docs home: https://pari.math.u-bordeaux.fr/
- Sage PARI bridge docs for `qfsolve`/`qfparam`: https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html
