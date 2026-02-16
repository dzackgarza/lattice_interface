# Sage Method Checklist

Tracks Sage-relevant methods from the Sage docs set.

---

## Module: sage.modules.free_quadratic_module

- [ ] `FreeQuadraticModule(R, n, inner_product_matrix)`
  - Caveat: supports degenerate and asymmetric pairings; do not assume symmetric Gram semantics.
- [ ] `FreeModule(ZZ, n, inner_product_matrix=G)`
- [ ] `VectorSpace(QQ, n, inner_product_matrix=M)`
- [ ] `inner_product_matrix()`
  - Caveat: ambient form matrix, not submodule Gram matrix.
- [ ] `gram_matrix()`
  - Caveat: for submodules this is basis-dependent (`B*A*B^T`).
- [ ] `determinant()`
- [ ] `discriminant()`
  - Caveat: discriminant convention differs from `IntegralLattice.discriminant()`.
- [ ] `ambient_module()`
- [ ] `ambient_vector_space()`
- [ ] `span(gens, check=True, already_echelonized=False)`
- [ ] `span_of_basis(basis, check=True, already_echelonized=False)`

## Module: sage.modules.free_module_integer (IntegerLattice)

- [ ] `IntegerLattice(basis, lll_reduce=True)`
  - Caveat: Euclidean embedding model (`Gram = B*B^T`), not arbitrary-form lattice constructor.
- [ ] `LLL()`
- [ ] `BKZ(*args, **kwds)`
- [ ] `HKZ()`
- [ ] `shortest_vector()`
- [ ] `closest_vector(target)`
- [ ] `approximate_closest_vector(target)`
  - Caveat: heuristic, not exact CVP guarantee.
- [ ] `babai(target, *args, **kwds)`
- [ ] `volume()`
- [ ] `discriminant()`
- [ ] `is_unimodular()`
- [ ] `reduced_basis`
- [ ] `update_reduced_basis()`
- [ ] `voronoi_cell()`
- [ ] `voronoi_relevant_vectors()`

## Module: sage.modules.free_quadratic_module_integer_symmetric (IntegralLattice)

- [ ] `IntegralLattice(data, basis=None)`
  - Caveat: requires non-degenerate symmetric form.
- [ ] `IntegralLatticeDirectSum(Lattices, return_embeddings=False)`
- [ ] `IntegralLatticeGluing(Lattices, glue, return_embeddings=False)`
- [ ] `gram_matrix()`
- [ ] `basis_matrix()`
- [ ] `inner_product_matrix()`
- [ ] `rank()`
- [ ] `degree()`
- [ ] `determinant()`
- [ ] `signature()`
- [ ] `signature_pair()`
- [ ] `is_even()`
- [ ] `is_positive_definite()`
- [ ] `is_negative_definite()`
- [ ] `is_definite()`
- [ ] `dual_lattice()`
- [ ] `discriminant_group(s=0)`
- [ ] `direct_sum(M)`
- [ ] `sublattice(basis)`
- [ ] `overlattice(gens)`
- [ ] `maximal_overlattice(p=None)`
- [ ] `orthogonal_complement(M)`
- [ ] `is_primitive(M)`
- [ ] `tensor_product(other, discard_basis=False)`
- [ ] `twist(s, discard_basis=False)`
- [ ] `LLL()`
- [ ] `lll()`
  - Caveat: `IntegralLattice.lll()/LLL()` returns a new lattice object; `IntegerLattice.LLL()` returns a reduced basis matrix and updates `reduced_basis` on the object.
- [ ] `short_vectors(n, **kwargs)`
- [ ] `enumerate_short_vectors()`
  - Caveat: returned vectors are not necessarily ordered strictly by length.
- [ ] `enumerate_close_vectors(target)`
  - Caveat: returned vectors are not necessarily ordered strictly by distance to the target.
- [ ] `minimum()`
- [ ] `maximum()`
- [ ] `orthogonal_group(gens=None, is_finite=None)`
  - Caveat: docs state generator computation is currently only for definite lattices; indefinite example raises `NotImplementedError`.
- [ ] `genus()`
- [ ] `quadratic_form()`
- [ ] `local_modification(M, G, p, check=True)`

## Module: sage.quadratic_forms.quadratic_form (QuadraticForm)

- [ ] `QuadraticForm(R, n, entries)`
- [ ] `QuadraticForm(p)`
- [ ] `QuadraticForm(R, M)`
- [ ] `QuadraticForm(M)`
- [ ] `DiagonalQuadraticForm(R, diag)`
- [ ] `quadratic_form_from_invariants(F, rk, det, P, sminus)`
- [ ] `QuadraticForm.from_polynomial(poly)`
- [ ] `dim()`
- [ ] `base_ring()`
- [ ] `coefficients()`
- [ ] `det()`
- [ ] `Gram_det()`
  - Caveat: do not conflate Hessian determinant and Gram determinant.
- [ ] `matrix()`
- [ ] `Hessian_matrix()`
- [ ] `Gram_matrix()`
  - Caveat: Hessian and Gram normalization differ.
- [ ] `Gram_matrix_rational()`
- [ ] `has_integral_Gram_matrix()`
- [ ] `polynomial(names='x')`
- [ ] `bilinear_map(v, w)`
- [ ] `__call__(v)`
- [ ] `hasse_invariant(p)`
- [ ] `hasse_invariant__OMeara(p)`
- [ ] `signature()`
- [ ] `signature_vector()`
- [ ] `anisotropic_primes()`
- [ ] `is_isotropic(p)`
- [ ] `is_anisotropic(p)`
- [ ] `is_hyperbolic(p)`
- [ ] `rational_diagonal_form()`
- [ ] `is_positive_definite()`
- [ ] `is_negative_definite()`
- [ ] `is_definite()`
- [ ] `is_indefinite()`
- [ ] `compute_definiteness()`
- [ ] `compute_definiteness_string_by_determinants()`
- [ ] `level()`
- [ ] `level_ideal()`
- [ ] `is_primitive()`
- [ ] `primitive()`
- [ ] `adjoint_primitive()`
- [ ] `change_ring(R)`
- [ ] `lll()`
- [ ] `minkowski_reduction()`
- [ ] `minkowski_reduction_for_4vars__SP()`
- [ ] `reduced_binary_form()`
- [ ] `reduced_binary_form1()`
- [ ] `reduced_ternary_form__Dickson()`
- [ ] `theta_series(var, prec)`
  - Caveat: implemented via PARI `qfrep` (`theta_by_pari`), and `qfrep` is defined for positive-definite forms.
- [ ] `theta_by_cholesky(q_prec)`
- [ ] `theta_by_pari(prec)`
- [ ] `theta_series_degree_2(prec)`
- [ ] `short_vector_list_up_to_length(n)`
  - Caveat: docs show non-positive-definite input raises `ValueError: Quadratic form must be positive definite in order to enumerate short vectors`.
- [ ] `short_primitive_vector_list_up_to_length(n)`
- [ ] `automorphism_group()`
- [ ] `automorphisms()`
- [ ] `number_of_automorphisms()`
- [ ] `is_globally_equivalent_to(other)`
- [ ] `is_locally_equivalent_to(other, p)`
- [ ] `is_rationally_isometric(other)`
- [ ] `global_genus_symbol()`
- [ ] `local_genus_symbol(p)`
- [ ] `genera(sig_pair, det, ...)`
- [ ] `mass__by_Siegel_densities()`
- [ ] `conway_mass()`
- [ ] `conway_standard_mass()`
- [ ] `siegel_product()`
- [ ] `local_density(p, m)`
- [ ] `local_primitive_density(p, m)`
- [ ] `local_representation_conditions(...)`
- [ ] `is_locally_universal_at_prime(p)`
- [ ] `is_locally_universal_at_all_primes()`
- [ ] `is_locally_universal_at_all_places()`
- [ ] `is_locally_represented_number(m)`
- [ ] `is_locally_represented_number_at_place(m, p)`
- [ ] `solve(n)`
- [ ] `find_p_neighbor_from_vec(p, v)`
- [ ] `neighbor_iteration(p, ...)`
- [ ] `disc()`
- [ ] `content()`
- [ ] `adjoint()`
- [ ] `antiadjoint()`
- [ ] `reciprocal()`
- [ ] `omega()`
- [ ] `delta()`
- [ ] `xi()`
- [ ] `xi_rec()`
- [ ] `clifford_invariant()`
- [ ] `clifford_conductor()`
- [ ] `hasse_conductor()`
- [ ] `representation_number_list(B)`
- [ ] `representation_vector_list(B)`
  - Caveat: docs state this only works for positive-definite quadratic forms.
- [ ] `swap_variables(i, j)`
- [ ] `multiply_variable(i, s)`
- [ ] `divide_variable(i, s)`
- [ ] `add_symmetric(i, j, s)`
- [ ] `extract_variables(v)`
- [ ] `scale_by_factor(s)`

## Module: sage.quadratic_forms.genera.genus

- [ ] `Genus(A, factored_determinant=None)`
- [ ] `LocalGenusSymbol(A, p)`
- [ ] `genera(sig_pair, determinant, max_scale=None, even=False)`
- [ ] `is_GlobalGenus(G)`
- [ ] `p_adic_symbol(A, p, val)`
- [ ] `two_adic_symbol(A, val)`
- [ ] `is_2_adic_genus(symbol)`
- [ ] `signature_pair_of_matrix(A)`
- [ ] `is_even_matrix(A)`
- [ ] `canonical_2_adic_reduction(symbol)`
- [ ] `canonical_2_adic_compartments(symbol)`
- [ ] `canonical_2_adic_trains(symbol)`
- [ ] `basis_complement(B)`
- [ ] `split_odd(A)`
- [ ] `trace_diag_mod_8(A)`
- [ ] `prime()`
- [ ] `is_even()`
- [ ] `symbol_tuple_list()`
- [ ] `canonical_symbol()`
- [ ] `number_of_blocks()`
- [ ] `determinant()`
- [ ] `det()`
- [ ] `dimension()`
- [ ] `dim()`
- [ ] `rank()`
- [ ] `excess()`
- [ ] `scale()`
- [ ] `norm()`
- [ ] `level()`
- [ ] `direct_sum(other)`
- [ ] `gram_matrix(check=True)`
- [ ] `mass()`
- [ ] `automorphous_numbers()`
- [ ] `trains()`
- [ ] `compartments()`
- [ ] `signature_pair()`
- [ ] `signature()`
- [ ] `local_symbols()`
- [ ] `local_symbol(p)`
- [ ] `discriminant_form()`
- [ ] `rational_representative()`
- [ ] `representative()`
- [ ] `representatives(backend=None, algorithm=None)`
- [ ] `spinor_generators(proper)`
- [ ] `spinor_generators()`

## Module: sage.modules.torsion_quadratic_module

- [ ] `TorsionQuadraticModule(V, W, gens=None, modulus=None, modulus_qf=None, check=True)`
- [ ] `TorsionQuadraticForm(q)`
- [ ] `gens()`
- [ ] `gram_matrix_bilinear()`
- [ ] `gram_matrix_quadratic()`
- [ ] `value_module()`
- [ ] `value_module_qf()`
- [ ] `order()`
- [ ] `invariants()`
- [ ] `direct_sum(other)`
- [ ] `twist(s)`
- [ ] `submodule(gens)`
- [ ] `submodule_with_gens(gens)`
- [ ] `orthogonal_submodule_to(S)`
  - Caveat: method name is `orthogonal_submodule_to`, not `orthogonal_submodule`.
- [ ] `primary_part(m)`
- [ ] `all_submodules()`
- [ ] `quotient(W)`
- [ ] `normal_form(partial=False)`
- [ ] `brown_invariant()`
- [ ] `genus(signature_pair)`
- [ ] `is_genus(signature_pair, even=True)`
  - Caveat: docs include TODO: `implement the same for odd lattices`.
- [ ] `orthogonal_group(gens=None, check=False)`

## Module: sage.quadratic_forms.binary_qf

- [ ] `BinaryQF(a, b=None, c=None)`
- [ ] `discriminant()`
  - Caveat: distinct from `determinant()`/`det()` (Gram determinant normalization differs).
- [ ] `determinant()`
- [ ] `det()`
- [ ] `is_equivalent(other)`
- [ ] `is_indefinite()`
- [ ] `is_reduced()`
- [ ] `reduced_form()`
- [ ] `cycle()`
- [ ] `small_prime_value()`

## Module: sage.quadratic_forms.ternary_qf

- [ ] `TernaryQF(coeffs)`
- [ ] `disc()`
- [ ] `content()`
- [ ] `adjoint()`
- [ ] `omega()`
- [ ] `delta()`
- [ ] `level__Tornaria()`
- [ ] `is_definite()`
- [ ] `is_reduced()`
- [ ] `reduced_ternary_form__Dickson()`
- [ ] `automorphisms()`
- [ ] `number_of_automorphisms()`
- [ ] `representation_number_list(B)`
- [ ] `representation_vector_list(B)`
- [ ] `theta_series(var, prec)`

## Module: sage.combinat.root_system

- [ ] `RootSystem(type)`
- [ ] `root_lattice()`
  - Caveat: combinatorial root lattice API, not `IntegralLattice` API.
- [ ] `weight_lattice()`
- [ ] `root_space()`
- [ ] `weight_space()`
- [ ] `ambient_lattice()`
- [ ] `ambient_space()`
- [ ] `simple_roots()`
- [ ] `simple_coroots()`
- [ ] `positive_roots()`
- [ ] `highest_root()`
- [ ] `fundamental_weights()`
- [ ] `rho()`
- [ ] `scalar(...)`
  - Caveat: Cartan pairing semantics; do not treat as Euclidean inner product.
- [ ] `inner_product(...)`

## Module: sage.rings.number_field / ideals (Bridge Methods)

- [ ] `integral_basis()`
- [ ] `basis()`
- [ ] `free_module()`
  - Caveat: returns bare module; no stored metric/Gram.
- [ ] `trace()`
- [ ] `minkowski_embedding(prec=...)`
  - Caveat: floating approximation; not canonical exact Gram source.
- [ ] `discriminant()`
- [ ] `signature()`

## Module: sage.geometry.toric_lattice / toric geometry

- [ ] `ToricLattice(n)`
- [ ] `dual()`
  - Caveat: toric N/M duality, not metric dual from Gram form.
- [ ] `Fan(..., lattice=...)`
  - Caveat: fan/cone machinery uses module structure and does not consume lattice inner-product matrices.
- [ ] `Cone(..., lattice=...)`

Last updated: 2026-02-16
