# PARI/GP Method Test Gap Checklist

Tracks PARI/GP-relevant methods documented in `docs/pari_gp/lattice/pari_gp_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Reduction and Isometry APIs

- [ ] `qflll(x, {flag = 0})`
- [ ] `qflllgram(G, {flag = 0})`
  - Caveat: primary contract is positive-definite Gram reduction.
- [ ] `qfisom(G, H, {fl}, {grp})`
- [ ] `qfisominit(G, {fl}, {m})`
- [ ] `qfauto(G, {fl})`
- [ ] `qfautoexport(qfa, {flag})`
- [ ] `qforbits(G, V)`
  - Caveat: expects `G` to contain `-I` and `V` to contain one representative per pair `{v, -v}`.

## 2. Vector Search and Optimization

- [ ] `qfminim(x, {B}, {m}, {flag = 0})`
- [ ] `qfminimize(G)`
- [ ] `qfcvp(x, t, {B}, {m}, {flag = 0})`
- [ ] `qfrep(q, B, {flag = 0})`
- [ ] `qfeval({q}, x, {y})`
- [ ] `qfnorm(x, {q})`
  - Caveat: obsolete in upstream PARI docs; prefer `qfeval`.

## 3. Indefinite / Equation-Solving APIs

- [ ] `qfsolve(G)`
- [ ] `qfparam(G, sol, {flag = 0})`
- [ ] `qfsign(G)`

## 4. Low-Dimensional and Structural APIs

- [ ] `qfgaussred(q, {flag = 0})`
- [ ] `qfperfection(G)`

---

## Definiteness and Domain Caveats

- `qflllgram`, `qfminim`, and `qfminimize` are documented in positive-definite workflows.
- `qfauto`, `qfisom`, and `qfisominit` are documented for integer positive-definite quadratic forms.
- Indefinite arithmetic workflows should prioritize `qfsolve`/`qfparam`/`qfsign` and isometry tools (`qfisom`, `qfauto`).

---

## References

- `docs/pari_gp/lattice/pari_gp_lattice_reference.md`
- `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI vectors/matrices reference: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html`
- PARI function index: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/`
- PARI docs home: `https://pari.math.u-bordeaux.fr/`
