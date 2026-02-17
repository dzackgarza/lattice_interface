# GAP Crystallographic Stack Lattice Methods Reference
## Cryst, CARATInterface, and CrystCat package surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | GAP package method |
| `[EUCLID]` | Euclidean crystallographic setting |
| `[PD]` | Positive-definite crystallographic regime |
| `[ZZMOD]` | Integer matrix or Z-module style workflow |
| `[GRP]` | Matrix-group/classification workflow |

---

## 1. Package Scope

| Package | Role | Tags |
|---------|------|------|
| `Cryst` | Affine crystallographic groups, space-group and Wyckoff workflows | `[PKG, EUCLID, PD, GRP]` |
| `CARATInterface` | Interface layer for CARAT-backed class and normalizer workflows | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CrystCat` | Catalog and class-index accessors (Q-classes/Z-classes and related group data) | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

---

## 2. Cryst Method Surface

| Method | Contract summary | Tags |
|--------|------------------|------|
| `AffineCrystGroupOnRight(...)` | Construct affine crystallographic group with right action conventions. | `[PKG, EUCLID, PD, GRP]` |
| `AsAffineCrystGroupOnRight(S)` | Convert matrix-group style object to affine crystallographic right-action object. | `[PKG, EUCLID, PD, GRP]` |
| `IsAffineCrystGroupOnRight(S)` | Predicate for right-action affine crystallographic objects. | `[PKG, EUCLID, PD, GRP]` |
| `AffineCrystGroupOnLeft(...)` | Construct affine crystallographic group with left action conventions. | `[PKG, EUCLID, PD, GRP]` |
| `PointGroup(G)` | Extract point-group quotient data of a crystallographic group. | `[PKG, EUCLID, PD, GRP]` |
| `TranslationsCrystGroup(G)` | Extract translation subgroup/lattice part of a crystallographic group. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `SpaceGroupsByPointGroupOnRight(P[, norm[, orbsflag]])` | Enumerate/classify space groups by fixed point-group data. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffPositions(...)` | Compute Wyckoff-position classification data. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffOrbit(...)` | Orbit-level Wyckoff computation. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffLattice(...)` | Lattice/subgroup data tied to Wyckoff-position workflows. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

Signature note:
- For methods documented only with name-level inventory in currently retrievable sources,
  argument placeholders remain `...` pending a full signature-lift pass from canonical
  current package manual pages.

---

## 3. CrystCat and CARAT-Linked Method Surface

| Method | Contract summary | Tags |
|--------|------------------|------|
| `CrystCatZClass(...)` | Access Z-class catalog representatives/data. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CrystCatQClass(...)` | Access Q-class catalog representative/data. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CrystCatQClasses(...)` | Enumerate/query Q-class family data in catalog surface. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratZClassNumber(group)` | Return CARAT-linked Z-class identifier for a group input. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratQClassNumber(group)` | Return CARAT-linked Q-class identifier for a group input. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSubgroups(...)` | Compute Bravais subgroup data for class/group context. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `MaximalSubgroupsRepresentatives(group)` | Compute representatives of maximal subgroups in the class context. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `NormalizerInGLnZ(group)` | Compute normalizer in `GL(n, Z)` for given group data. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CentralizerInGLnZ(group)` | Compute centralizer in `GL(n, Z)` for given group data. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisGroup(group)` | Return Bravais group associated to input class/group data. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSupergroups(...)` | Compute Bravais supergroup data. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `ZClassRepsQClass(group)` | Return Z-class representatives inside a fixed Q-class. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `AffineNormalizer(group)` | Compute affine normalizer in crystallographic context. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `PointGroupsBravaisClass(group)` | Point-group data for a Bravais-class context. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `RationalClassesMaximalSubgroups(group)` | Maximal-subgroup data across rational class surface. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

Attribution note:
- Current retrievable sources present these methods together in crystallographic class
  chapters; package ownership can straddle CrystCat and CARAT-backed interfaces.

---

## 4. Definiteness and Domain Caveats

- These APIs are crystallographic and integer-matrix-group workflows in Euclidean settings.
- They are not the same contract surface as indefinite arithmetic-lattice genus,
  discriminant-form, or local-global isometry APIs.
- Use with explicit awareness that some currently cited manuals are historical mirrors;
  treat precise modern argument typing as an open signature-fidelity task.

---

## 5. Consolidated Method Index

- `AffineCrystGroupOnLeft`
- `AffineCrystGroupOnRight`
- `AffineNormalizer`
- `AsAffineCrystGroupOnRight`
- `BravaisGroup`
- `BravaisSubgroups`
- `BravaisSupergroups`
- `CaratQClassNumber`
- `CaratZClassNumber`
- `CentralizerInGLnZ`
- `CrystCatQClass`
- `CrystCatQClasses`
- `CrystCatZClass`
- `IsAffineCrystGroupOnRight`
- `MaximalSubgroupsRepresentatives`
- `NormalizerInGLnZ`
- `PointGroup`
- `PointGroupsBravaisClass`
- `RationalClassesMaximalSubgroups`
- `SpaceGroupsByPointGroupOnRight`
- `TranslationsCrystGroup`
- `WyckoffLattice`
- `WyckoffOrbit`
- `WyckoffPositions`
- `ZClassRepsQClass`

---

## References

- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Existing umbrella mapping:
  `docs/gap/lattice/gap_lattice_methods_reference.md`
- Cryst package page: `https://gap-packages.github.io/cryst/`
- GAP package install index (Cryst/CARATInterface/CrystCat):
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- CrystCat/CARAT function chapter:
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/crystcat/doc/chap39.htm`
- Historical Cryst chapter mirror:
  `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap035.htm`
