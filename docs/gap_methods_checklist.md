# GAP Method Test Gap Checklist

Tracks GAP-relevant lattice methods documented in `docs/gap/lattice/gap_lattice_methods_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core GAP

### 1.1 Integer-module normal forms and structure

- [ ] `NullspaceIntMat(mat)`
- [ ] `SolutionIntMat(mat, vec)`
- [ ] `SolutionNullspaceIntMat(mat, vec)`
- [ ] `BaseIntMat(mat)`
- [ ] `BaseIntersectionIntMats(m, n)`
- [ ] `HermiteNormalFormIntegerMat(M)`
- [ ] `HermiteNormalFormIntegerMatTransform(M)`
- [ ] `SmithNormalFormIntegerMat(M)`
- [ ] `SmithNormalFormIntegerMatTransforms(M)`
- [ ] `TriangulizedIntegerMat(mat)`
- [ ] `TriangulizedIntegerMatTransform(mat)`
- [ ] `TriangulizeIntegerMat(mat)`
- [ ] `DiagonalizeIntMat(mat)`
- [ ] `NormalFormIntMat(...)`
- [ ] `AbelianInvariantsOfList(list)`
- [ ] `ComplementIntMat(full, sub)`
- [ ] `DeterminantIntMat(mat)`
- [ ] `Decomposition(...)`
- [ ] `IntegralizedMat(A[, inforec])`
- [ ] `DecompositionInt(A, B, depth)`

### 1.2 LLL and Euclidean search

- [ ] `LLLReducedBasis(...)`
- [ ] `LLLReducedGramMat(G[, y])`
- [ ] `ShortestVectors(G, m[, "positive"])`
  - Caveat: finite enumeration contracts are in the positive-definite Euclidean regime.
- [ ] `OrthogonalEmbeddings(gram[, "positive"][, maxdim])`
  - Caveat: Euclidean embedding workflow, not a general indefinite classification API.

---

## 2. GAP Package Ecosystem

### 2.1 Package load surfaces (checklist anchor)

- [ ] `LoadPackage("Cryst")`
- [ ] `LoadPackage("CARATInterface")`
- [ ] `LoadPackage("CrystCat")`
- [ ] `LoadPackage("Forms")`
- [ ] `LoadPackage("HyperCells")`

### 2.2 Cryst/CARAT/CrystCat (canonical)

- [ ] `AffineCrystGroupOnRight(S)`
- [ ] `AsAffineCrystGroupOnRight(S)`
- [ ] `IsAffineCrystGroupOnRight(S)`
- [ ] `AffineCrystGroupOnLeft(S)`
- [ ] `PointGroup(S)`
- [ ] `TranslationsCrystGroup(S)`
- [ ] `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`
- [ ] `WyckoffPositions(S)`
- [ ] `WyckoffOrbit(G, p)`
- [ ] `WyckoffLattice(G, p)`
- [ ] `WyckoffNormalClosure(G, p)`
- [ ] `BravaisGroup(R)`
- [ ] `PointGroupsBravaisClass(R)`
- [ ] `BravaisSubgroups(R)`
- [ ] `BravaisSupergroups(R)`
- [ ] `NormalizerInGLnZ(R)`
- [ ] `CentralizerInGLnZ(R)`
- [ ] `IsBravaisEquivalent(R, S)`
- [ ] `CaratZClass(R)`
- [ ] `CaratZClassNumber(R)`
- [ ] `CaratQClass(R)`
- [ ] `CaratQClassNumber(R)`
- [ ] `RationalClassesMaximalSubgroups(R)`
- [ ] `ZClassRepsQClass(R)`
- [ ] `MaximalSubgroupsRepresentatives(R)`
- [ ] `AffineNormalizer(R)`
- [ ] `IsCaratZClass(R)`
- [ ] `IsCaratQClass(R)`
  - Caveat: crystallographic Euclidean setting, not indefinite arithmetic-lattice classification.
  - Caveat: `normedQclass` is `false` or a normalizer-element list in `GL(d,Z)`; `orbitsQclass` is boolean.
  - Caveat: selector arguments `f`, `s`, and `k` are not treated as active canonical parameters.
  - Legacy aliases triaged out of active canonical surface: `CrystCatZClass(...)`, `CrystCatQClass(...)`, `CrystCatQClasses(...)`.

### 2.3 Archived Out-of-Scope Polyhedral/Toric Surfaces

- Archived umbrella sections for `4ti2Interface`, `NormalizInterface`, `toric`, `NConvex`, and polyhedral `CddInterface` are maintained in:
  `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md`.
- Package-level archived checklists remain available under `docs/archive/scope_violations/`.

### 2.4 Forms package (detailed checklist surface)

- [ ] `AsSesquilinearForm(obj[, field][, antiautomorphism])`
- [ ] `AsQuadraticForm(obj[, field])`
- [ ] `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])`
- [ ] `QuadraticFormByMatrix(matrix[, field])`
- [ ] `IsometricForms(form1, form2)`
- [ ] `SimilarityForms(form1, form2)`
- [ ] `PreservedSesquilinearForms(G)`
- [ ] `PreservedQuadraticForms(G)`
- [ ] `OrthogonalSubgroups(G, n[, s])`
- [ ] `WittIndex(form)`
  - Caveat: finite-field form workflow; characteristic and irreducibility assumptions are documented in `docs/forms_methods_checklist.md`.

### 2.5 fplll hooks exposed in GAP

- [ ] `FPLLLReducedBasis(...)`
- [ ] `FPLLLShortestVector(...)`

---

## References

- `docs/gap/lattice/gap_lattice_methods_reference.md`
- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/lattice/crystallographic_stack_lattice_reference.md`
- `docs/archive/scope_violations/gap_methods_checklist_polyhedral_sections_2026-02-18.md`
- `docs/archive/scope_violations/cddinterface_methods_checklist.md`
- `docs/forms_methods_checklist.md`
- `docs/hypercells_methods_checklist.md`
- GAP docs hub: `https://www.gap-system.org/doc/`
- GAP package index: `https://gap-packages.github.io`
- GAP Cryst package manual: `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm`
- GAP Reference Manual (CARAT methods): `https://docs.gap-system.org/doc/ref/chap44.html`
- CARATInterface package manual: `https://www.math.rwth-aachen.de/~GAP/WWW2/PackagePages/caratinterface/doc/manual.pdf`
- HyperCells package page: `https://gap-packages.github.io/HyperCells/`
- Forms package page: `https://gap-packages.github.io/forms/`
- Forms manual: `https://gap-packages.github.io/forms/doc/chap0_mj.html`
