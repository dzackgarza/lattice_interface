# fpylll Method Test Gap Checklist

Tracks fpylll-relevant methods documented in `docs/fpylll/lattice/fpylll_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core Data Structures

- [ ] `IntegerMatrix(arg0, arg1=None, int_type='mpz')`
- [ ] `GSO.Mat(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`
- [ ] `MatGSO(B, U=None, UinvT=None, flags=GSO_DEFAULT, float_type='double', gram=False, update=False)`
- [ ] `LLL.Reduction(M, delta=LLL_DEF_DELTA, eta=LLL_DEF_ETA, flags=LLL_DEFAULT)`
- [ ] `BKZ.Param(block_size, strategies=BKZ_DEFAULT_STRATEGY, delta=LLL_DEF_DELTA, flags=BKZ_DEFAULT, max_loops=0, max_time=0, auto_abort=None, gh_factor=None, min_success_probability=BKZ_DEF_MIN_SUCCESS_PROBABILITY, rerandomization_density=BKZ_DEF_RERANDOMIZATION_DENSITY, dump_gso_filename=None, **kwds)`
- [ ] `BKZ.Reduction(M, lll_obj, param)`

## 2. LLL Surface

- [ ] `LLL.reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`
- [ ] `lll_reduction(B, U=None, delta=0.99, eta=0.51, method=None, float_type=None, precision=0, flags=LLL_DEFAULT)`
- [ ] `LLL.is_reduced(M, delta=0.99, eta=0.51)`

## 3. BKZ Surface

- [ ] `BKZ.reduction(B, BKZ.Param(...), U=None, float_type=None, precision=0)`
- [ ] `BKZ.Reduction(M, lll_obj, param)`
- [ ] `BKZ.Param(block_size, strategies=..., delta=..., flags=..., max_loops=..., max_time=..., auto_abort=..., gh_factor=..., min_success_probability=..., rerandomization_density=..., dump_gso_filename=..., **kwds)`
  - Caveat: current modules page shows BKZ section headers without full member signatures; this checklist keeps BKZ signatures source-anchored to `bkz.pyx` / `bkz_param.pyx`.

## 4. Enumeration / SVP / CVP

- [ ] `Enumeration(M, nr_solutions=1, strategy=EvaluatorStrategy.BEST_N_SOLUTIONS, sub_solutions=False)`
- [ ] `Enumeration.enumerate(first, last, max_dist, max_dist_expo, target=None, subtree=None, pruning=None, dual=False, subtree_reset=False)`
- [ ] `Enumeration.get_nodes(level=None)`
- [ ] `SVP.shortest_vector(B, method='fast', flags=SVP_DEFAULT, pruning=True, preprocess=True, max_aux_solutions=0)`
  - Caveat: `method='fast'` is heuristic; `method='proved'` is the proof-oriented mode.
- [ ] `CVP.closest_vector(B, t, method='fast', flags=CVP_DEFAULT)`
- [ ] `CVP.babai(B, t, *args, **kwargs)`
  - Caveat: practical CVP workflows assume LLL-preconditioned basis input.

## 5. Pruning and Utilities

- [ ] `Pruning.run(radius, cost, gso_r, target, metric='probability', flags=Pruning.GRADIENT, pruning=None, float_type='double')`
- [ ] `fpylll.util.adjust_radius_to_gh_bound(dist, dist_expo, block_size, root_det, gh_factor)`
- [ ] `fpylll.util.gaussian_heuristic(r)`

---

## Definiteness and Domain Caveat

- fpylll is a Euclidean lattice stack; it does not expose indefinite arithmetic-form classification semantics.

---

## References

- `docs/fpylll/lattice/fpylll_lattice_reference.md`
- `docs/fpylll/upstream/fpylll_online_provenance_2026-02-18.md`
- fpylll module docs: `https://fpylll.readthedocs.io/en/latest/modules.html`
- fpylll package docs home: `https://fpylll.readthedocs.io/`
- fpylll repository: `https://github.com/fplll/fpylll`
