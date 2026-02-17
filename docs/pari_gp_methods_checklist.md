# PARI/GP Method Test Gap Checklist

Tracks PARI/GP-relevant methods documented in `docs/pari_gp/lattice/pari_gp_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Reduction and Isometry APIs

- [ ] `qflll(B, ...)`
- [ ] `qflllgram(G, ...)`
  - Caveat: primary contract is positive-definite Gram reduction.
- [ ] `qfisom(G, H, ...)`
- [ ] `qfisominit(G, ...)`
- [ ] `qfauto(G, ...)`
- [ ] `qfautoexport(...)`
- [ ] `qforbits(Aut, V)`

## 2. Vector Search and Optimization

- [ ] `qfminim(G, B, ...)`
- [ ] `qfminimize(...)`
- [ ] `qfcvp(...)`
- [ ] `qfrep(...)`
- [ ] `qfeval(G, v)`
- [ ] `qfnorm(...)`

## 3. Indefinite / Equation-Solving APIs

- [ ] `qfsolve(G)`
- [ ] `qfparam(G, sol, flag=0)`
- [ ] `qfsign(G)`

## 4. Low-Dimensional and Structural APIs

- [ ] `qfgaussred(Q)`
- [ ] `qfperfection(...)`

---

## Definiteness and Domain Caveats

- `qflllgram`, `qfminim`, and `qfminimize` are documented in positive-definite workflows.
- Indefinite arithmetic workflows should prioritize `qfsolve`/`qfparam`/`qfsign` and isometry tools (`qfisom`, `qfauto`).

---

## References

- `docs/pari_gp/lattice/pari_gp_lattice_reference.md`
- PARI vectors/matrices reference: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html`
- PARI function index: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/`
- PARI docs home: `https://pari.math.u-bordeaux.fr/`
