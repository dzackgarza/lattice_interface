# GAP Crystallographic Stack Method Test Gap Checklist

Tracks GAP crystallographic package surfaces documented in
`docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surfaces

- [ ] `LoadPackage("Cryst")`
- [ ] `LoadPackage("CARATInterface")`
- [ ] `LoadPackage("CrystCat")`

---

## 2. Cryst Core Group and Lattice Methods

- [ ] `AffineCrystGroupOnRight(...)`
- [ ] `AsAffineCrystGroupOnRight(S)`
- [ ] `IsAffineCrystGroupOnRight(S)`
- [ ] `AffineCrystGroupOnLeft(...)`
- [ ] `PointGroup(G)`
- [ ] `TranslationsCrystGroup(G)`
- [ ] `SpaceGroupsByPointGroupOnRight(P[, norm[, orbsflag]])`
- [ ] `WyckoffPositions(...)`
- [ ] `WyckoffOrbit(...)`
- [ ] `WyckoffLattice(...)`

---

## 3. CrystCat and CARAT-Linked Class and Normalizer Methods

- [ ] `CrystCatZClass(...)`
- [ ] `CrystCatQClass(...)`
- [ ] `CrystCatQClasses(...)`
- [ ] `CaratZClassNumber(group)`
- [ ] `CaratQClassNumber(group)`
- [ ] `BravaisSubgroups(...)`
- [ ] `MaximalSubgroupsRepresentatives(group)`
- [ ] `NormalizerInGLnZ(group)`
- [ ] `CentralizerInGLnZ(group)`
- [ ] `BravaisGroup(group)`
- [ ] `BravaisSupergroups(...)`
- [ ] `ZClassRepsQClass(group)`
- [ ] `AffineNormalizer(group)`
- [ ] `PointGroupsBravaisClass(group)`
- [ ] `RationalClassesMaximalSubgroups(group)`

---

## Domain and Constraint Caveats

- These are Euclidean crystallographic and integer-matrix-group workflows.
- The methods are not general indefinite quadratic-form genus/isometry classifiers.
- Some method-surface evidence is from older package manuals and should be revalidated
  against current package docs/releases during a signature-fidelity pass.

---

## References

- `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
- `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Existing GAP umbrella reference:
  `docs/gap/lattice/gap_lattice_methods_reference.md`
- Cryst package page: `https://gap-packages.github.io/cryst/`
- GAP package install index (Cryst/CARATInterface/CrystCat entries):
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- CrystCat/CARAT function index chapter:
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/crystcat/doc/chap39.htm`
- Cryst manual chapter (historical mirror):
  `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap035.htm`
