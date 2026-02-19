# PARI/GP Method Test Gap Checklist

Tracks PARI/GP-relevant methods documented in `docs/pari_gp/lattice/pari_gp_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Reduction, Decomposition, and Isometry APIs

- [ ] `qflll(x, {flag = 0})`
- [ ] `qflllgram(G, {flag = 0})`
  - Caveat: accepts positive semidefinite forms (positive quadratic form, not necessarily definite); form need not have maximal rank.
- [ ] `qfcholesky(G)`
  - Caveat: no explicit positive-definite requirement in upstream; returns `[]` if decomposition fails (when G is not positive semidefinite).
- [ ] `qfjacobi(G)`
  - Caveat: no positive-definite requirement; applies to any real symmetric matrix. Returns `[L, V]` with eigenvalues and eigenvectors.
- [ ] `qfisom(G, H, {fl}, {grp})`
- [ ] `qfisominit(G, {fl}, {m})`
- [ ] `qfauto(G, {fl})`
- [ ] `qfautoexport(qfa, {flag})`
- [ ] `qforbits(G, V)`
  - Caveat: expects `G` to contain `-I` and `V` to contain one representative per pair `{v, -v}`.

## 2. Vector Search and Optimization

- [ ] `qfminim(x, {B}, {m}, {flag = 0})`
- [ ] `qfminimize(G)`
  - Caveat: requires non-degenerate form (non-zero determinant), not positive-definite. Returns `[H, U, c]` with minimized integral form.
- [ ] `qfcvp(x, t, {B}, {m}, {flag = 0})`
- [ ] `qfrep(q, B, {flag = 0})`
  - Caveat: requires positive-definite form per upstream.
- [ ] `qfeval({q}, x, {y})`
- [ ] `qfnorm(x, {q})`
  - Caveat: obsolete in upstream PARI docs; prefer `qfeval`.
- [ ] `qfbil(x, y, {q})`
  - Caveat: **OBSOLETE** in upstream PARI docs; superseded by `qfeval`.

## 3. Indefinite / Equation-Solving APIs

- [ ] `qfsolve(G)`
- [ ] `qfparam(G, sol, {flag = 0})`
- [ ] `qfsign(G)`
  - Caveat: returns `[p, m]` (positive and negative eigenvalues); no positive-definite requirement.

## 4. Low-Dimensional and Structural APIs

- [ ] `qfgaussred(q, {flag = 0})`
  - Caveat: singular matrices supported; no positive-definite requirement.
- [ ] `qfperfection(G)`

---

## Definiteness and Domain Caveats

- `qflllgram` accepts positive semidefinite forms (positive quadratic form, not necessarily definite).
- `qfminim`, `qfcvp`, and `qfrep` require positive-definite forms; behavior undefined otherwise.
- `qfauto`, `qfisom`, `qfisominit`, and `qfperfection` require positive-definite forms.
- `qfminimize` requires non-degenerate form (non-zero determinant), not positive-definite.
- `qfjacobi`, `qfsign`, `qfsolve`, and `qfgaussred` have no positive-definite requirement.
- Indefinite arithmetic workflows should prioritize `qfsolve`/`qfparam`/`qfsign` and isometry tools (`qfisom`, `qfauto`).

---

## References

- `docs/pari_gp/lattice/pari_gp_lattice_reference.md`
- `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI vectors/matrices reference: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html`
- PARI function index: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/`
- PARI docs home: `https://pari.math.u-bordeaux.fr/`
