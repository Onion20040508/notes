---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 36.6", "local normal form for submersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§36 Submersions#^thm-36-6]]

## Treated in
- [[§36 Submersions#^thm-36-6|Theorem §36.6: Local Normal Form for Submersions]], in [[§36 Submersions]]

## Its proof uses
- [[§17 Differentiable Structures#^lem-17-6|Lemma §17.6: Restricting and Recomposing Smooth Charts]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-3|Lemma §19.3: A Chart Mapped into a Given Chart]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-4|Proposition §19.4: The Two Notions of Diffeomorphism Agree]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-5|Lemma §19.5: Composition of Smooth Maps]]
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Definition §29.1: Coordinate Functions of a Chart]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|Theorem §29.9: Dimension of the Tangent Space]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§35 Local Diffeomorphisms#^thm-35-1|Theorem §35.1: Inverse Function Theorem]]
- [[§36 Submersions#^prop-36-1|Proposition §36.1: Dimension Constraints]]
- [[§36 Submersions#^lem-36-5|Lemma §36.5: Diffeomorphisms onto Open Sets Are Charts]]

## Used in (Differentiable Manifolds)
- [[§36 Submersions#^cor-36-7|Corollary §36.7: Being a Submersion Is an Open Condition]]
- [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|Lemma §38.1: Level Sets Near a Regular Point]]
- [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|Theorem §38.2: The Regular Value Theorem for Manifolds]]
- [[§43 Immersions#^thm-43-1|Theorem §43.1: Local Normal Form for Immersions]]

## Connections
- **Used for.** Being a submersion is an open condition ([[§36 Submersions#^cor-36-7|§36.7]]), and submersions are open maps ([[§36 Submersions#^cor-36-9|§36.9]]), hence so are fibrations ([[§40 Fibrations#^prop-40-1|§40.1]]). It proves the [[Regular Value Theorem for Manifolds]]: near a point of the level set F is a projection, so the level set is a coordinate slice.
- **How.** Complete F¹, …, Fⁿ by m − n of the old coordinates to m functions with invertible Jacobian; the [[Inverse Function Theorem (several variables)]] makes them a local diffeomorphism, and [[§36 Submersions#^lem-36-5|§36.5]] makes that a chart.
- **Local, not global.** A surjective submersion need not be a fibration: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has a broken fibre over 0 ([[§40 Fibrations#^ex-40-1|Ex. §40.1]]). Ehresmann's theorem adds properness to get local triviality over the whole base ([[§40 Fibrations#^thm-40-3|§40.3]]).
- **Same idea elsewhere.** The model is the projection ℝᵏ × ℝˡ → ℝᵏ ([[§36 Submersions#^ex-36-1|Ex. §36.1]]), and the mirror statement is the [[Immersion Normal Form]]. The 452 [[Implicit Function Theorem]] is the Euclidean shadow: near a regular point a level set is a graph.
