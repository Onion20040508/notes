---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 20.5", "pairing theorem"]
tags: [differentiable-manifolds, hub]
---
![[§21 Linear Algebra Toolkit#^thm-21-5]]

## Treated in
- [[§21 Linear Algebra Toolkit#^thm-21-5|Theorem §21.5: Non-Degenerate Pairings]], in [[§21 Linear Algebra Toolkit]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§21 Linear Algebra Toolkit#^prop-21-2|Proposition §21.2: The Dual Basis]]
- [[§21 Linear Algebra Toolkit#^def-21-4|Definition §21.4: Bilinear Pairing]]

## Its proof uses (other subjects)
- [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§32 The Cotangent Space#^thm-32-8|Theorem §32.8: The Cotangent Space from Germs]]

## Connections
- **Used for.** [[Cotangent Space from Germs]]: the pairing of T_pM with I_p/I_p², (D, class of f) ↦ D[f], is non-degenerate ([[§32 The Cotangent Space#^prop-32-7|§32.7]]), so the theorem gives T_pM ≅ (I_p/I_p²)* and I_p/I_p² ≅ T*_pM at once.
- **Both hypotheses are needed.** Each half of non-degeneracy gives one inequality of dimensions, and only together do they force the isomorphisms. Finite dimension cannot be dropped: for infinite-dimensional V the evaluation pairing of V with V* is non-degenerate, but V → V** is not onto ([[§21 Linear Algebra Toolkit#^rem-21-2|§20, Remark]]).
- **Same idea elsewhere.** The linear algebra is LADR's duality: dim V′ = dim V ([[§12 Duality#^ladr-3-111|LADR 3.111]]), and V ≅ V** canonically ([[§21 Linear Algebra Toolkit#^prop-21-3|§21.3]]). A real inner product is a non-degenerate pairing of V with itself, and then B^♭ is the isomorphism of the [[Riesz representation theorem]].
- **Coming later in the course.** In de Rham cohomology, (α, β) ↦ ∫ α ∧ β pairs Hᵏ with Hⁿ⁻ᵏ on a compact oriented n-manifold, and Poincaré duality says this pairing is non-degenerate.
