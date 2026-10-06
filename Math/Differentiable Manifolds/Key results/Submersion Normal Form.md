---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 32.4", "local normal form for submersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§34 Submersions#^thm-34-4]]

## Treated in
- [[§34 Submersions#^thm-34-4|Theorem §34.4: Local Normal Form for Submersions]], in [[§34 Submersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-4|Lemma §19.4: Composition of Smooth Maps]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1: Inverse Function Theorem]]
- [[§34 Submersions#^def-34-1|Definition §34.1: Submersion and Immersion]]
- [[§34 Submersions#^prop-34-1|Proposition §34.1: Dimension Constraints]]
- [[§34 Submersions#^lem-34-3|Lemma §34.3: Diffeomorphisms onto Open Sets Are Charts]]

## Its proof uses (other subjects)
- [[Invertible ⟺ nonzero determinant]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§34 Submersions#^cor-34-5|Corollary §34.5: Being a Submersion Is an Open Condition]]
- [[§34 Submersions#^cor-34-6|Corollary §34.6: Submersions Are Open Maps]]
- [[§35 Submanifolds#^thm-35-6|Theorem §35.6: The Regular Value Theorem for Manifolds]]
- [[§37 Immersions#^thm-37-1|Theorem §37.1: Local Normal Form for Immersions]]

## Connections
- **Used for.** Being a submersion is an open condition ([[§34 Submersions#^cor-34-5|§34.5]]), and submersions are open maps ([[§34 Submersions#^cor-34-6|§34.6]]), hence so are fibrations ([[§36 Fibrations#^prop-36-1|§36.1]]). It proves the [[Regular Value Theorem for Manifolds]]: near a point of the level set F is a projection, so the level set is a coordinate slice.
- **How.** Complete F¹, …, Fⁿ by m − n of the old coordinates to m functions with invertible Jacobian; the [[Inverse Function Theorem (several variables)]] makes them a local diffeomorphism, and [[§34 Submersions#^lem-34-3|§34.3]] makes that a chart.
- **Local, not global.** A surjective submersion need not be a fibration: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has a broken fibre over 0 ([[§36 Fibrations#^ex-36-1|Ex. §36.1]]). Ehresmann's theorem adds properness to get local triviality over the whole base ([[§36 Fibrations#^thm-36-3|§36.3]]).
- **Same idea elsewhere.** The model is the projection ℝᵏ × ℝˡ → ℝᵏ ([[§34 Submersions#^ex-34-1|Ex. §34.1]]), and the mirror statement is the [[Immersion Normal Form]]. The 452 [[Implicit Function Theorem]] is the Euclidean shadow: near a regular point a level set is a graph.
