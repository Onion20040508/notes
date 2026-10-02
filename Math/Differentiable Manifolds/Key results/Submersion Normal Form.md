---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 28.7", "local normal form for submersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§28 Local Diffeomorphisms and Submersions#^thm-28-7]]

## Treated in
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-7|Theorem §28.7: Local Normal Form for Submersions]], in [[§28 Local Diffeomorphisms and Submersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-11|Lemma §2.11: Restricting and Recomposing Charts]]
- [[§15 Smooth Functions and Smooth Maps#^lem-15-4|Lemma §15.4: Composition of Smooth Maps]]
- [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|Proposition §23.9: Charts Are Diffeomorphisms]]
- [[§25 The Differential in Coordinates#^prop-25-1|Proposition §25.1: Partial Derivatives Upstairs and Downstairs]]
- [[§25 The Differential in Coordinates#^thm-25-2|Theorem §25.2: The Matrix of the Differential]]
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-1|Theorem §28.1: Inverse Function Theorem]]
- [[§28 Local Diffeomorphisms and Submersions#^def-28-2|Definition §28.2: Submersion and Immersion]]
- [[§28 Local Diffeomorphisms and Submersions#^prop-28-4|Proposition §28.4: Dimension Constraints]]
- [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|Lemma §28.6: Diffeomorphisms onto Open Sets Are Charts]]

## Its proof uses (other subjects)
- [[Invertible ⟺ nonzero determinant]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§28 Local Diffeomorphisms and Submersions#^cor-28-8|Corollary §28.8: Being a Submersion Is an Open Condition]]
- [[§28 Local Diffeomorphisms and Submersions#^cor-28-9|Corollary §28.9: Submersions Are Open Maps]]
- [[§29 Submanifolds#^thm-29-6|Theorem §29.6: The Regular Value Theorem for Manifolds]]

## Connections
- **Used for.** Being a submersion is an open condition ([[§28 Local Diffeomorphisms and Submersions#^cor-28-8|§28.8]]), and submersions are open maps ([[§28 Local Diffeomorphisms and Submersions#^cor-28-9|§28.9]]), hence so are fibrations ([[§30 Fibrations#^prop-30-1|§30.1]]). It proves the [[Regular Value Theorem for Manifolds]]: near a point of the level set F is a projection, so the level set is a coordinate slice.
- **How.** Complete F¹, …, Fⁿ by m − n of the old coordinates to m functions with invertible Jacobian; the [[Inverse Function Theorem (several variables)]] makes them a local diffeomorphism, and [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|§28.6]] makes that a chart.
- **Local, not global.** A surjective submersion need not be a fibration: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has a broken fibre over 0 ([[§30 Fibrations#^ex-30-2|Ex. §30.2]]). Ehresmann's theorem adds properness to get local triviality over the whole base ([[§30 Fibrations#^thm-30-3|§30.3]]).
- **Same idea elsewhere.** The model is the projection ℝᵏ × ℝˡ → ℝᵏ ([[§28 Local Diffeomorphisms and Submersions#^ex-28-3|Ex. §28.3]]), and the mirror statement is the [[Immersion Normal Form]]. The 452 [[Implicit Function Theorem]] is the Euclidean shadow: near a regular point a level set is a graph.
