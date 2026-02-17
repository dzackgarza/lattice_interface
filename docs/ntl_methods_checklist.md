# NTL Method Test Gap Checklist

Tracks NTL-relevant methods documented in `docs/ntl/lattice/ntl_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Exact LLL and Integer Solve

- [ ] `LLL(ZZ& det2, mat_ZZ& B, long verbose=0)`
- [ ] `LLL(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)`
- [ ] `LLL_plus(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)`
- [ ] `image(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)`
- [ ] `LatticeSolve(vec_ZZ& x, const mat_ZZ& A, const vec_ZZ& y, long reduce=0)`

## 2. Floating LLL and BKZ Families

- [ ] `[G_]LLL_{FP,QP,XD,RR}(mat_ZZ& B[, mat_ZZ& U], double delta=0.99, long deep=0, LLLCheckFct check=0, long verbose=0)`
  - Caveat: upstream documents `deep` as deprecated.
- [ ] `[G_]BKZ_{FP,QP,QP1,XD,RR}(mat_ZZ& B[, mat_ZZ& U], double delta=0.99, long BlockSize=10, long prune=0, LLLCheckFct check=0, long verbose=0)`
  - Caveat: Euclidean reduction workflow over row-basis integer matrices; not an indefinite genus/isometry classifier.

## 3. Hermite Normal Form

- [ ] `HNF(mat_ZZ& W, const mat_ZZ& A, const ZZ& D)`
  - Caveat: documented for full-column-rank input with determinant multiple precondition on `D`.

---

## References

- `docs/ntl/lattice/ntl_lattice_reference.md`
- NTL module map: `https://libntl.org/doc/tour-modules.html`
- NTL LLL/BKZ API docs: `https://libntl.org/doc/LLL.cpp.html`
- NTL HNF API docs: `https://libntl.org/doc/HNF.cpp.html`
- NTL tutorial examples: `https://libntl.org/doc/tour-ex4.html`

