---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 17.5", "pairing theorem"]
tags: [differentiable-manifolds, hub]
---
![[§17 Linear Algebra Toolkit#^thm-17-5]]

## Treated in
- [[§17 Linear Algebra Toolkit#^thm-17-5|Theorem §17.5: Non-Degenerate Pairings]], in [[§17 Linear Algebra Toolkit]]

## Its proof uses
- [[§17 Linear Algebra Toolkit#^prop-17-1|Proposition §17.1: Standing Facts from Linear Algebra]]
- [[§17 Linear Algebra Toolkit#^prop-17-2|Proposition §17.2: The Dual Basis]]
- [[§17 Linear Algebra Toolkit#^def-17-3|Definition §17.3: Bilinear Pairing]]

## Its proof uses (other subjects)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^thm-27-7|Theorem §27.7: The Cotangent Space from Germs]]

## Connections
- **Used for.** [[Cotangent Space from Germs]]: the pairing of T_pM with I_p/I_p², (D, class of f) ↦ D[f], is non-degenerate ([[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-6|§27.6]]), so the theorem gives T_pM ≅ (I_p/I_p²)* and I_p/I_p² ≅ T*_pM at once.
- **Both hypotheses are needed.** Each half of non-degeneracy gives one inequality of dimensions, and only together do they force the isomorphisms. Finite dimension cannot be dropped: for infinite-dimensional V the evaluation pairing of V with V* is non-degenerate, but V → V** is not onto ([[§17 Linear Algebra Toolkit#^rem-17-2|§10, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's duality: dim V′ = dim V ([[§12 Duality#^ladr-3-111|LADR 3.111]]), and V ≅ V** canonically ([[§17 Linear Algebra Toolkit#^prop-17-3|§17.3]]). A real inner product is a non-degenerate pairing of V with itself, and then B^♭ is the isomorphism of the [[Riesz representation theorem]].
- **Coming later in the course.** In de Rham cohomology, (α, β) ↦ ∫ α ∧ β pairs Hᵏ with Hⁿ⁻ᵏ on a compact oriented n-manifold, and Poincaré duality says this pairing is non-degenerate.
