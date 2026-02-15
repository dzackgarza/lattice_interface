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
| `qflll(B, ...)` | LLL reduction from basis-style matrix input | `[ZZMOD, RED]` |
| `qflllgram(G, ...)` | LLL-style reduction from Gram matrix input | `[PD, ZZMOD, RED]` |
| `qfisom(G, H, ...)` | Isometry/equivalence test between quadratic forms | `[NT]` |
| `qfisominit(G, ...)` | Precomputation structure for repeated `qfisom` calls | `[NT]` |
| `qfauto(G, ...)` | Automorphism group computations for forms | `[NT]` |
| `qfautoexport(...)` | Export/format automorphism data | `[NT]` |
| `qforbits(Aut, V)` | Orbit decomposition under automorphism action | `[NT]` |

Practical note:

- `qflllgram` is primarily a positive-definite workflow; outside that regime results may be heuristic/non-canonical.

---

## 3. Vector Search and Optimization APIs

| Function | Description | Tags |
|----------|-------------|------|
| `qfminim(G, B, ...)` | Enumerate vectors with bounded quadratic value | `[PD, NT]` |
| `qfminimize(...)` | Minimization helper workflow for forms | `[PD, NT]` |
| `qfcvp(...)` | Closest-vector style routine in quadratic-form setting | `[PD, NT]` |
| `qfrep(...)` | Representation routines for quadratic forms | `[NT]` |
| `qfeval(G, v)` | Evaluate form on vector | `[NT]` |
| `qfnorm(...)` | Norm-related computations in quadratic context | `[NT]` |

---

## 4. Indefinite/Equation-Solving APIs

| Function | Description | Tags |
|----------|-------------|------|
| `qfsolve(G)` | Solve isotropy/zero-representation equation for form `G` | `[INDEF, NT]` |
| `qfparam(G, sol, flag=0)` | Parametrize conic solutions from known solution `sol` | `[INDEF, NT]` |
| `qfsign(G)` | Signature-related analysis of form | `[INDEF, NT]` |

Use these for indefinite arithmetic problems where shortest-vector Euclidean workflows are not the right abstraction.

---

## 5. Binary/Low-Dimensional and Structural APIs

| Function | Description | Tags |
|----------|-------------|------|
| `qfgaussred(Q)` | Gauss reduction of binary quadratic forms | `[NT]` |
| `qfperfection(...)` | Perfection/perfect-form style analysis | `[NT]` |

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
- PARI docs home: https://pari.math.u-bordeaux.fr/
- Sage PARI bridge docs for `qfsolve`/`qfparam`: https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html
