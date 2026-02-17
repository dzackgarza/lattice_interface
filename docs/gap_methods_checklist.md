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
- [ ] `LoadPackage("NormalizInterface")`
- [ ] `LoadPackage("4ti2Interface")`
- [ ] `LoadPackage("toric")`
- [ ] `LoadPackage("NConvex")`
- [ ] `LoadPackage("CddInterface")`
- [ ] `LoadPackage("Forms")`

### 2.2 Cryst/CARAT/CrystCat

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
  - Caveat: crystallographic Euclidean setting, not indefinite arithmetic-lattice classification.

### 2.3 NormalizInterface

- [ ] `NmzCone(list)`
- [ ] `NmzCompute(cone[, props])`
- [ ] `NmzConeProperty(cone, property)`
- [ ] `NmzKnownConeProperties(cone)`
- [ ] `NmzHasConeProperty(cone, property)`
- [ ] `NmzGenerators(cone)`
- [ ] `NmzExtremeRays(cone)`
- [ ] `NmzSupportHyperplanes(cone)`
- [ ] `NmzHilbertBasis(cone)`
- [ ] `NmzHilbertSeries(cone)`
- [ ] `NmzHilbertQuasiPolynomial(cone)`
- [ ] `NmzTriangulation(cone)`
- [ ] `NmzTriangulationSize(cone)`
- [ ] `NmzTriangulationDetSum(cone)`
- [ ] `NmzLatticePoints(cone)`
- [ ] `NmzVerticesOfPolyhedron(cone)`

### 2.4 4ti2Interface

- [ ] `4ti2Interface_groebner_matrix(...)`
- [ ] `4ti2Interface_groebner_basis(...)`
- [ ] `4ti2Interface_hilbert_inequalities(...)`
- [ ] `4ti2Interface_hilbert_equalities_in_positive_orthant(...)`
- [ ] `4ti2Interface_hilbert_equalities_and_inequalities(...)`
- [ ] `4ti2Interface_zsolve_equalities_and_inequalities(...)`
- [ ] `4ti2Interface_graver_equalities(...)`

### 2.5 toric

- [ ] `InsideCone(...)`
- [ ] `InDualCone(...)`
- [ ] `PolytopeLatticePoints(...)`
- [ ] `Faces(...)`
- [ ] `ConesOfFan(...)`
- [ ] `NumberOfConesOfFan(...)`
- [ ] `ToricStar(...)`
- [ ] `DualSemigroupGenerators(...)`
- [ ] `EmbeddingAffineToricVariety(...)`
- [ ] `DivisorPolytope(...)`
- [ ] `DivisorPolytopeLatticePoints(...)`
- [ ] `RiemannRochBasis(...)`
- [ ] `EulerCharacteristic(...)`
- [ ] `BettiNumberToric(...)`
- [ ] `CardinalityOfToricVariety(...)`

### 2.6 CddInterface

- [ ] `Cdd_PolyhedronByInequalities(...)`
- [ ] `Cdd_PolyhedronByGenerators(...)`
- [ ] `Cdd_Canonicalize(P)`
- [ ] `Cdd_V_Rep(P)`
- [ ] `Cdd_H_Rep(P)`
- [ ] `Cdd_AmbientSpaceDimension(P)`
- [ ] `Cdd_Dimension(P)`
- [ ] `Cdd_GeneratingVertices(P)`
- [ ] `Cdd_GeneratingRays(P)`
- [ ] `Cdd_Equalities(P)`
- [ ] `Cdd_Inequalities(P)`
- [ ] `Cdd_Faces(P)`
- [ ] `Cdd_FacesWithFixedDimension(P, d)`
- [ ] `Cdd_Facets(P)`
- [ ] `Cdd_IsEmpty(P)`
- [ ] `Cdd_IsCone(P)`
- [ ] `Cdd_IsPointed(P)`

### 2.7 fplll hooks exposed in GAP

- [ ] `FPLLLReducedBasis(...)`
- [ ] `FPLLLShortestVector(...)`

---

## References

- `docs/gap/lattice/gap_lattice_methods_reference.md`
- GAP docs hub: `https://www.gap-system.org/doc/`
- GAP package index: `https://gap-packages.github.io`
- NormalizInterface package page: `https://gap-packages.github.io/NormalizInterface/`
- toric package page: `https://gap-packages.github.io/toric/`
- 4ti2Interface package page: `https://homalg-project.github.io/homalg_project/4ti2Interface/`
- CddInterface package page: `https://homalg-project.github.io/CddInterface/`
