# fpylll Method Test Gap Checklist

Tracks fpylll-relevant methods documented in `docs/fpylll/lattice/fpylll_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core Data Structures

- [ ] `IntegerMatrix(...)`
- [ ] `GSO.Mat(B, U=None, UinvT=None, float_type='double', precision=0, gram=False, update=False)`
- [ ] `MatGSO(...)`
- [ ] `LLL.Reduction(M, delta=0.99, eta=0.51, flags=0)`
- [ ] `BKZ.Param(block_size, strategies=None, delta=..., flags=..., max_loops=..., max_time=...)`
- [ ] `BKZ.Reduction(M, lll_obj, param)`

## 2. LLL Surface

- [ ] `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=0)`
- [ ] `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=0)`
- [ ] `LLL.is_reduced(M, delta=0.99, eta=0.51)`

## 3. BKZ Surface

- [ ] `BKZ.reduction(B, BKZ.Param(...), U=None, float_type=None, precision=0)`
- [ ] `BKZ.Reduction(M, lll_obj, param)`
- [ ] `BKZ.Param(...)`
  - Caveat: official modules page currently lists BKZ as a section header without rendered member signatures; keep signatures source-anchored to the local reference + source examples until upstream docs expose full signatures.

## 4. Enumeration / SVP / CVP

- [ ] `Enumeration(M, nr_solutions=1, strategy=..., sub_solutions=..., threads=...)`
- [ ] `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`
- [ ] `Enumeration.get_nodes(level=None)`
- [ ] `SVP.shortest_vector(B, method='proved', flags=..., pruning=..., preprocess=True, max_aux_solutions=...)`
  - Caveat: `method='fast'` is heuristic; `method='proved'` is the proof-oriented mode.
- [ ] `CVP.closest_vector(B, t, method='fast', flags=...)`
- [ ] `CVP.babai(B, t, *args, **kwargs)`
  - Caveat: practical CVP workflows assume LLL-preconditioned basis input.

## 5. Pruning and Utilities

- [ ] `Pruning.run(...)`
- [ ] `fpylll.util.adjust_radius_to_gh_bound(...)`
- [ ] `fpylll.util.gaussian_heuristic(...)`

---

## Definiteness and Domain Caveat

- fpylll is a Euclidean lattice stack; it does not expose indefinite arithmetic-form classification semantics.

---

## References

- `docs/fpylll/lattice/fpylll_lattice_reference.md`
- fpylll module docs: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll package docs home: `https://fpylll.readthedocs.io/`
- fpylll repository: `https://github.com/fplll/fpylll`
