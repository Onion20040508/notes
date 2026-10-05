---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 32.4", "local normal form for submersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§32 Submersions#^thm-32-4]]

## Treated in
- [[§32 Submersions#^thm-32-4|Theorem §32.4: Local Normal Form for Submersions]], in [[§32 Submersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§18 Smooth Functions and Smooth Maps#^lem-18-4|Lemma §18.4: Composition of Smooth Maps]]
- [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|Proposition §26.9: Charts Are Diffeomorphisms]]
- [[§28 The Differential in Coordinates#^prop-28-1|Proposition §28.1: Partial Derivatives Upstairs and Downstairs]]
- [[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2: The Matrix of the Differential]]
- [[§31 Local Diffeomorphisms#^thm-31-1|Theorem §31.1: Inverse Function Theorem]]
- [[§32 Submersions#^prop-32-1|Proposition §32.1: Dimension Constraints]]
- [[§32 Submersions#^def-32-1|Definition §32.1: Submersion and Immersion]]
- [[§32 Submersions#^lem-32-3|Lemma §32.3: Diffeomorphisms onto Open Sets Are Charts]]

## Its proof uses (other subjects)
- [[Invertible ⟺ nonzero determinant]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§32 Submersions#^cor-32-5|Corollary §32.5: Being a Submersion Is an Open Condition]]
- [[§32 Submersions#^cor-32-6|Corollary §32.6: Submersions Are Open Maps]]
- [[§33 Submanifolds#^thm-33-6|Theorem §33.6: The Regular Value Theorem for Manifolds]]
- [[§35 Immersions#^thm-35-1|Theorem §35.1: Local Normal Form for Immersions]]

## Connections
- **Used for.** Being a submersion is an open condition ([[§32 Submersions#^cor-32-5|§32.5]]), and submersions are open maps ([[§32 Submersions#^cor-32-6|§32.6]]), hence so are fibrations ([[§34 Fibrations#^prop-34-1|§34.1]]). It proves the [[Regular Value Theorem for Manifolds]]: near a point of the level set F is a projection, so the level set is a coordinate slice.
- **How.** Complete F¹, …, Fⁿ by m − n of the old coordinates to m functions with invertible Jacobian; the [[Inverse Function Theorem (several variables)]] makes them a local diffeomorphism, and [[§32 Submersions#^lem-32-3|§32.3]] makes that a chart.
- **Local, not global.** A surjective submersion need not be a fibration: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has a broken fibre over 0 ([[§34 Fibrations#^ex-34-1|Ex. §34.1]]). Ehresmann's theorem adds properness to get local triviality over the whole base ([[§34 Fibrations#^thm-34-3|§34.3]]).
- **Same idea elsewhere.** The model is the projection ℝᵏ × ℝˡ → ℝᵏ ([[§32 Submersions#^ex-32-1|Ex. §32.1]]), and the mirror statement is the [[Immersion Normal Form]]. The 452 [[Implicit Function Theorem]] is the Euclidean shadow: near a regular point a level set is a graph.
