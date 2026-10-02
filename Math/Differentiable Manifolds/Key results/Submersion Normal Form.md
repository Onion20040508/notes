---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 28.7", "local normal form for submersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§29 Submersions#^thm-29-4]]

## Treated in
- [[§29 Submersions#^thm-29-4|Theorem §29.4: Local Normal Form for Submersions]], in [[§28 Local Diffeomorphisms]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-11|Lemma §2.11: Restricting and Recomposing Charts]]
- [[§15 Smooth Functions and Smooth Maps#^lem-15-4|Lemma §15.4: Composition of Smooth Maps]]
- [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|Proposition §23.9: Charts Are Diffeomorphisms]]
- [[§25 The Differential in Coordinates#^prop-25-1|Proposition §25.1: Partial Derivatives Upstairs and Downstairs]]
- [[§25 The Differential in Coordinates#^thm-25-2|Theorem §25.2: The Matrix of the Differential]]
- [[§28 Local Diffeomorphisms#^thm-28-1|Theorem §28.1: Inverse Function Theorem]]
- [[§29 Submersions#^def-29-1|Definition §29.1: Submersion and Immersion]]
- [[§29 Submersions#^prop-29-1|Proposition §29.1: Dimension Constraints]]
- [[§29 Submersions#^lem-29-3|Lemma §29.3: Diffeomorphisms onto Open Sets Are Charts]]

## Its proof uses (other subjects)
- [[Invertible ⟺ nonzero determinant]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§29 Submersions#^cor-29-5|Corollary §29.5: Being a Submersion Is an Open Condition]]
- [[§29 Submersions#^cor-29-6|Corollary §29.6: Submersions Are Open Maps]]
- [[§30 Submanifolds#^thm-30-6|Theorem §30.6: The Regular Value Theorem for Manifolds]]
- [[§33 Immersions#^thm-33-1|Theorem §33.1: Local Normal Form for Immersions]]

## Connections
- **Used for.** Being a submersion is an open condition ([[§29 Submersions#^cor-29-5|§29.5]]), and submersions are open maps ([[§29 Submersions#^cor-29-6|§29.6]]), hence so are fibrations ([[§31 Fibrations#^prop-31-1|§31.1]]). It proves the [[Regular Value Theorem for Manifolds]]: near a point of the level set F is a projection, so the level set is a coordinate slice.
- **How.** Complete F¹, …, Fⁿ by m − n of the old coordinates to m functions with invertible Jacobian; the [[Inverse Function Theorem (several variables)]] makes them a local diffeomorphism, and [[§29 Submersions#^lem-29-3|§29.3]] makes that a chart.
- **Local, not global.** A surjective submersion need not be a fibration: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has a broken fibre over 0 ([[§31 Fibrations#^ex-31-2|Ex. §31.2]]). Ehresmann's theorem adds properness to get local triviality over the whole base ([[§31 Fibrations#^thm-31-3|§31.3]]).
- **Same idea elsewhere.** The model is the projection ℝᵏ × ℝˡ → ℝᵏ ([[§29 Submersions#^ex-29-1|Ex. §29.1]]), and the mirror statement is the [[Immersion Normal Form]]. The 452 [[Implicit Function Theorem]] is the Euclidean shadow: near a regular point a level set is a graph.
