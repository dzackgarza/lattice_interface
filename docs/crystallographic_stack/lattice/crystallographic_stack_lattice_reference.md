# GAP Crystallographic Stack Lattice Methods Reference
## Cryst, CARAT/Bravais, and CrystCat-related surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | GAP package method |
| `[EUCLID]` | Euclidean crystallographic setting |
| `[PD]` | Positive-definite crystallographic regime |
| `[ZZMOD]` | Integer matrix or Z-module style workflow |
| `[GRP]` | Matrix-group/classification workflow |
| `[LEGACY]` | Name appears in older mirrors but is not confirmed in current canonical docs |

---

## 1. Package Scope

| Package | Role | Tags |
|---------|------|------|
| `Cryst` | Affine crystallographic groups, space-group and Wyckoff workflows | `[PKG, EUCLID, PD, GRP]` |
| `CARATInterface` | CARAT-backed class and normalizer workflows for integral matrix groups | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CrystCat` | Catalog/index support for crystallographic classes and data | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

---

## 2. Canonical Cryst Method Surface (GAP Ref Chap. 35)

| Method | Contract summary | Tags |
|--------|------------------|------|
| `AffineCrystGroupOnRight(S)` | Convert `S` into an affine crystallographic group with right action convention. | `[PKG, EUCLID, PD, GRP]` |
| `AsAffineCrystGroupOnRight(S)` | Coerce to right-action affine crystallographic representation when possible. | `[PKG, EUCLID, PD, GRP]` |
| `IsAffineCrystGroupOnRight(S)` | Predicate for right-action affine crystallographic objects. | `[PKG, EUCLID, PD, GRP]` |
| `AffineCrystGroupOnLeft(S)` | Convert `S` into an affine crystallographic group with left action convention. | `[PKG, EUCLID, PD, GRP]` |
| `PointGroup(S)` | Return point-group quotient data of crystallographic object `S`. | `[PKG, EUCLID, PD, GRP]` |
| `TranslationsCrystGroup(S)` | Return translation subgroup/lattice part of crystallographic object `S`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])` | Enumerate/classify space groups with fixed point-group data `P`; `normedQclass` is `false` or a list of elements in `N_{GL(d,Z)}(P)`, and `orbitsQclass` is boolean (`true` requests all representatives in each normalizer orbit). | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffPositions(S)` | Compute Wyckoff-position classes for a space group `S`. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffOrbit(G, p)` | Return Wyckoff orbit of point `p` under group `G`. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffLattice(G, p)` | Return lattice/stabilizer data attached to Wyckoff computation at `(G, p)`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `WyckoffNormalClosure(G, p)` | Compute normal-closure object in the Wyckoff workflow for `(G, p)`. | `[PKG, EUCLID, PD, GRP]` |

---

## 3. Canonical CARAT/Bravais Surface (GAP Ref Chap. 44.6)

| Method | Contract summary | Tags |
|--------|------------------|------|
| `BravaisGroup(R)` | Compute Bravais group for matrix-group object `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `PointGroupsBravaisClass(R)` | Point-group data for Bravais class associated to `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSubgroups(R)` | Enumerate Bravais subgroups of class/group input `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSupergroups(R)` | Enumerate Bravais supergroups of class/group input `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `NormalizerInGLnZ(R)` | Compute normalizer of `R` in `GL(n, Z)`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CentralizerInGLnZ(R)` | Compute centralizer of `R` in `GL(n, Z)`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsBravaisEquivalent(R, S)` | Decide Bravais equivalence between two class/group objects. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratZClass(R)` | Return CARAT Z-class object for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratZClassNumber(R)` | Return CARAT Z-class index/number for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratQClass(R)` | Return CARAT Q-class object for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratQClassNumber(R)` | Return CARAT Q-class index/number for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `RationalClassesMaximalSubgroups(R)` | Return maximal-subgroup data across rational classes for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `ZClassRepsQClass(R)` | Return Z-class representatives in the Q-class of `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `MaximalSubgroupsRepresentatives(R)` | Return representatives of maximal subgroups for input class/group `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `AffineNormalizer(R)` | Compute affine normalizer in crystallographic class context. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsCaratZClass(R)` | Predicate: object `R` is a CARAT Z-class object. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsCaratQClass(R)` | Predicate: object `R` is a CARAT Q-class object. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

---

## 4. Legacy and Non-Canonical Signature Triage

The following names appear in older/historical materials but are not documented as
current canonical signatures in GAP Reference Chapter 44.6:

- `CrystCatZClass(...)`
- `CrystCatQClass(...)`
- `CrystCatQClasses(...)`

These are tracked as legacy aliases, not canonical active-surface contracts.

The following selectorized CARAT signatures are also treated as non-canonical in this
surface because current GAP reference and CARATInterface docs expose one-argument forms:

- `BravaisGroup(R[, f])`
- `PointGroupsBravaisClass(R[, f[, s]])`
- `BravaisSubgroups(R[, f[, s[, k]]])`
- `BravaisSupergroups(R[, f[, s[, k]]])`
- `NormalizerInGLnZ(R[, f])`
- `CentralizerInGLnZ(R[, f])`

---

## 5. Definiteness and Domain Caveats

- These APIs are crystallographic and integer-matrix-group workflows in Euclidean settings.
- They are not the same contract surface as indefinite arithmetic-lattice genus,
  discriminant-form, or local-global isometry APIs.
- For `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`:
  `normedQclass` is `false` or a list of normalizer elements in `GL(d,Z)`, and
  `orbitsQclass` is boolean (`true` returns all representatives in each normalizer orbit).
- Optional selector arguments `f`, `s`, and `k` are not retained as active contracts for
  CARAT methods in this surface because no accepted value domains are documented in current
  canonical references for these methods.

---

## 6. Consolidated Method Index

- `AffineCrystGroupOnLeft`
- `AffineCrystGroupOnRight`
- `AffineNormalizer`
- `AsAffineCrystGroupOnRight`
- `BravaisGroup`
- `BravaisSubgroups`
- `BravaisSupergroups`
- `CaratQClass`
- `CaratQClassNumber`
- `CaratZClass`
- `CaratZClassNumber`
- `CentralizerInGLnZ`
- `IsAffineCrystGroupOnRight`
- `IsBravaisEquivalent`
- `IsCaratQClass`
- `IsCaratZClass`
- `MaximalSubgroupsRepresentatives`
- `NormalizerInGLnZ`
- `PointGroup`
- `PointGroupsBravaisClass`
- `RationalClassesMaximalSubgroups`
- `SpaceGroupsByPointGroupOnRight`
- `TranslationsCrystGroup`
- `WyckoffLattice`
- `WyckoffNormalClosure`
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
- GAP Cryst package manual:
  `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm`
- GAP3 Cryst chapter mirror (supporting detail for normalizer/orbit selector semantics):
  `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap061.htm`
- GAP Reference Manual (CARAT methods):
  `https://docs.gap-system.org/doc/ref/chap44.html`
- CARATInterface package manual:
  `https://www.math.rwth-aachen.de/~GAP/WWW2/PackagePages/caratinterface/doc/manual.pdf`
