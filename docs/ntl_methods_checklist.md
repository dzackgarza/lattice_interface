# NTL Method Test Gap Checklist

Tracks NTL-relevant methods documented in `docs/ntl/lattice/ntl_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Exact LLL and Integer Solve

- [ ] `LLL(ZZ& det2, mat_ZZ& B, long verbose=0)`
- [ ] `LLL(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)`
- [ ] `LLL(ZZ& det2, mat_ZZ& B, long a, long b, long verbose=0)`
  - Caveat: explicit rational δ = a/b parameterization; not the default δ=0.99 variant.
- [ ] `LLL(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long a, long b, long verbose=0)`
  - Caveat: explicit rational δ = a/b parameterization with transformation matrix.
- [ ] `LLL_plus(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)`
- [ ] `image(ZZ& det2, mat_ZZ& B, mat_ZZ& U, long verbose=0)`
- [ ] `LatticeSolve(vec_ZZ& x, const mat_ZZ& A, const vec_ZZ& y, long reduce=0)`
- [ ] `ComputeGS(const mat_ZZ& B, mat_RR& mu, vec_RR& c)`
  - Caveat: Gram-Schmidt orthogonalization computation; outputs mu coefficients and squared lengths.
- [ ] `NearVector(vec_ZZ& w, const mat_ZZ& B, const vec_ZZ& a)`
  - Caveat: finds vector w ∈ B*Z such that w ≡ a (mod B*Z); CVP-like nearest vector to given target.

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

