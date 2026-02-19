# PARI/GP Online Provenance (2026-02-17)

Scope: tighten PARI quadratic-form (`qf*`) method signatures and caveats in
`docs/pari_gp_methods_checklist.md` and
`docs/pari_gp/lattice/pari_gp_lattice_reference.md`.

## Canonical upstream sources checked

- PARI stable function index:
  - https://pari.math.u-bordeaux.fr/dochtml/ref-stable/function_index.html
- PARI vectors/matrices + quadratic forms chapter:
  - https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Vectors__matrices__linear_algebra_and_sets.html
- PARI docs home:
  - https://pari.math.u-bordeaux.fr/

## Signatures verified from the PARI chapter

- `qfauto(G, {fl})`
- `qfautoexport(qfa, {flag})`
- `qforbits(G, V)`
- `qfeval({q}, x, {y})`
- `qfisom(G, H, {fl}, {grp})`
- `qfisominit(G, {fl}, {m})`
- `qfgaussred(q, {flag = 0})`
- `qflll(x, {flag = 0})`
- `qflllgram(G, {flag = 0})`
- `qfminim(x, {B}, {m}, {flag = 0})`
- `qfminimize(G)`
- `qfnorm(x, {q})`
- `qfparam(G, sol, {flag = 0})`
- `qfperfection(G)`
- `qfrep(q, B, {flag = 0})`
- `qfsign(x)`
- `qfsolve(G)`
- `qfcvp(x, t, {B}, {m}, {flag = 0})`

## Constraint/caveat evidence captured

- `qfauto`, `qfisom`, `qfisominit`: documented for integer positive-definite forms.
- `qforbits`: requires group to contain `-I` and representative set convention modulo sign.
- `qfparam`: documented on ternary forms from a known isotropic solution.
- `qfperfection`: documented as currently rank-8 only.
- `qfnorm`: documented as obsolete in favor of `qfeval`.
- `qfbil`: documented as obsolete in favor of `qfeval`.
- `qfcholesky`: returns Cholesky factor `R` such that `^tR * R = G`, or `[]` if no solution exists.
- `qfjacobi`: Jacobi eigenvalue method for symmetric real matrices; preferred over `mateigen` for symmetric matrices.

## Local documentation targets updated

- `docs/pari_gp_methods_checklist.md`
- `docs/pari_gp/lattice/pari_gp_lattice_reference.md`

## 2026-02-19: Added missing PARI `qf*` functions

Added to reference documentation:
- `qfcholesky(G)` - Cholesky decomposition for symmetric matrices
- `qfjacobi(G)` - Jacobi eigenvalue method for symmetric real matrices
- `qfbil(x, y, {q})` - Bilinear form evaluation (marked as obsolete, superseded by `qfeval`)

Source: https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Vectors__matrices__linear_algebra_and_sets.html
