# latticegen Method Test Gap Checklist

Tracks latticegen-relevant method/command surfaces documented in `docs/latticegen/reference/latticegen_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. fplll `latticegen` CLI (instance-generation toolchain)

### 1.1 Command surface

- [ ] `latticegen [-randseed <int|time>] r <d> <b>`
- [ ] `latticegen [-randseed <int|time>] s <d> <b> <b2>`
- [ ] `latticegen [-randseed <int|time>] u <d> <b>`
- [ ] `latticegen [-randseed <int|time>] n <d> <b> <c>`
  - Caveat: method selector `c` is documented as one of `b` or `q`.
- [ ] `latticegen [-randseed <int|time>] N <d> <b> <c>`
  - Caveat: method selector `c` is documented as one of `b` or `q`.
- [ ] `latticegen [-randseed <int|time>] q <d> <k> <b> <c>`
  - Caveat: method selector `c` is documented as one of `b`, `q`, or `p`.
- [ ] `latticegen [-randseed <int|time>] t <d> <f>`
- [ ] `latticegen [-randseed <int|time>] T <d>` with stdin weights

### 1.2 Deterministic generation controls

- [ ] `-randseed <integer>`
- [ ] `-randseed time`

---

## 2. Python `latticegen` Package (`TAdeJong/moire-lattice-generator`)

### 2.1 Lattice generation and transforms

- [ ] `latticegen.generate_ks(a_0, theta, psi=0)`
- [ ] `latticegen.generate_r_k(kappa=1, kappa_theta=0, xi=0, kappa_psi=0)`
- [ ] `latticegen.hexlattice_gen(r_k, xi, size=..., shift=..., chunks=...)`
- [ ] `latticegen.anylattice_gen(r_k, xi, mode='gaussian', size=..., shift=..., chunks=...)`
- [ ] `latticegen.transformations.rotate(vector, angle, center=(0, 0))`
- [ ] `latticegen.transformations.reflect(vector, axis=0.0, center=(0.0, 0.0))`
- [ ] `latticegen.transformations.scale(vector, factor, center=(0.0, 0.0))`

### 2.2 Singularity and strain analysis

- [ ] `latticegen.singularities.singularity_shift(r_k, xi0, chi=0.5, psi=0, origin=(0, 0), ns=None)`
- [ ] `latticegen.singularities.refined_singularity_shift(r_k, xi0, subpixels=..., **kwargs)`
- [ ] `latticegen.singularities.singularity_shift_simple(r_k, xi0, alpha=0.1, psi=0, origin=(0, 0), ns=None, cross=False)`
- [ ] `latticegen.singularities.refined_singularity_shift_simple(r_k, xi0, subpixels=..., **kwargs)`
- [ ] `latticegen.singularities.hyperbolic_shift(r_k, xi0, alpha=0.1, psi=0, origin=(0, 0), ns=None)`
- [ ] `latticegen.singularities.refined_hyperbolic_shift(r_k, xi0, subpixels=..., **kwargs)`
- [ ] `latticegen.strain.strain_method_1(r_k, r_k_u, delta=..., polar=False)`
- [ ] `latticegen.strain.strain_method_2(r_k, r_k_u, delta=..., polar=False)`
- [ ] `latticegen.strain.strain_method_3(r_k, r_k_u, delta=..., polar=False)`
- [ ] `latticegen.transformmatrix.to_matrix(...)`

---

## Toolchain-Selection Caveat

- The fplll `latticegen` CLI is for integer-lattice benchmark instance generation.
- The Python `latticegen` package is for moire/image-space lattice generation and analysis.
- Do not treat these as interchangeable APIs.

---

## References

- `docs/latticegen/reference/latticegen_lattice_reference.md`
- fplll `latticegen` docs: `https://fplll.github.io/fplll/latticegen_8cpp.html`
- fplll source (`latticegen.cpp`): `https://raw.githubusercontent.com/fplll/fplll/master/fplll/latticegen.cpp`
- Python latticegen docs: `https://moire-lattice-generator.readthedocs.io/en/latest/`
- Python latticegen API page: `https://moire-lattice-generator.readthedocs.io/en/latest/source/latticegen.html`
