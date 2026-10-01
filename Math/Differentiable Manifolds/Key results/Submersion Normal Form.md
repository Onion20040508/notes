---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 14.5", "local normal form for submersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§14 Local Diffeomorphisms and Submersions#^thm-14-5]]

## Treated in
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|Theorem §14.5: Local Normal Form for Submersions]], in [[§14 Local Diffeomorphisms and Submersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-11|Lemma §2.11: Restricting and Recomposing Charts]]
- [[§8 Differentiable Structures#^lem-8-15|Lemma §8.15: Composition of Smooth Maps]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|Proposition §12.14: Charts Are Diffeomorphisms]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|Proposition §12.21: Partial Derivatives Upstairs and Downstairs]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|Theorem §12.22: The Matrix of the Differential]]
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-1|Theorem §14.1: Inverse Function Theorem]]
- [[§14 Local Diffeomorphisms and Submersions#^def-14-2|Definition §14.2: Submersion and Immersion]]
- [[§14 Local Diffeomorphisms and Submersions#^prop-14-4|Proposition §14.4: Dimension Constraints]]
- [[§14 Local Diffeomorphisms and Submersions#^lem-14-7|Lemma §14.7: Diffeomorphisms onto Open Sets Are Charts]]

## Its proof uses (other subjects)
- [[Invertible ⟺ nonzero determinant]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§14 Local Diffeomorphisms and Submersions#^cor-14-8|Corollary §14.8: Being a Submersion Is an Open Condition]]
- [[§14 Local Diffeomorphisms and Submersions#^cor-14-9|Corollary §14.9: Submersions Are Open Maps]]
- [[§15 Submanifolds#^thm-15-6|Theorem §15.6: The Regular Value Theorem for Manifolds]]

## Connections
- **Used for.** Being a submersion is an open condition ([[§14 Local Diffeomorphisms and Submersions#^cor-14-8|§14.8]]), and submersions are open maps ([[§14 Local Diffeomorphisms and Submersions#^cor-14-9|§14.9]]), hence so are fibrations ([[§16 Fibrations#^prop-16-1|§16.1]]). It proves the [[Regular Value Theorem for Manifolds]]: near a point of the level set F is a projection, so the level set is a coordinate slice.
- **How.** Complete F¹, …, Fⁿ by m − n of the old coordinates to m functions with invertible Jacobian; the [[Inverse Function Theorem (several variables)]] makes them a local diffeomorphism, and [[§14 Local Diffeomorphisms and Submersions#^lem-14-7|§14.7]] makes that a chart.
- **Local, not global.** A surjective submersion need not be a fibration: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has a broken fibre over 0 ([[§16 Fibrations#^ex-16-2|Ex. §16.2]]). Ehresmann's theorem adds properness to get local triviality over the whole base ([[§16 Fibrations#^thm-16-3|§16.3]]).
- **Same idea elsewhere.** The model is the projection ℝᵏ × ℝˡ → ℝᵏ ([[§14 Local Diffeomorphisms and Submersions#^ex-14-3|Ex. §14.3]]), and the mirror statement is the [[Immersion Normal Form]]. The 452 [[Implicit Function Theorem]] is the Euclidean shadow: near a regular point a level set is a graph.
