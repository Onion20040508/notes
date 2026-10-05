---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 18.2", "Lee Proposition 2.5"]
tags: [differentiable-manifolds, hub]
---
![[§18 Smooth Functions and Smooth Maps#^prop-18-2]]

## Treated in
- [[§18 Smooth Functions and Smooth Maps#^prop-18-2|Proposition §18.2: Smoothness of a Map Does Not Depend on the Charts]], in [[§18 Smooth Functions and Smooth Maps]]

## Its proof uses
- [[§16 Differentiable Structures#^ex-16-1|Example §16.1: Euclidean Space]]
- [[§16 Differentiable Structures#^def-16-4|Definition §16.4: Smoothly Compatible Charts]]
- [[§18 Smooth Functions and Smooth Maps#^def-18-1|Definition §18.1: Smooth Chart]]
- [[§18 Smooth Functions and Smooth Maps#^def-18-2|Definition §18.2: Smooth Function on a Manifold]]
- [[§18 Smooth Functions and Smooth Maps#^def-18-3|Definition §18.3: Smooth Map and Diffeomorphism]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§18 Smooth Functions and Smooth Maps#^prop-18-6|Proposition §18.6: Transport of Smooth Structure]]
- [[§18 Smooth Functions and Smooth Maps#^prop-18-9|Proposition §18.9: Projections and Slice Inclusions Are Smooth]]
- [[§32 Submersions#^lem-32-3|Lemma §32.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§33 Submanifolds#^lem-33-3|Lemma §33.3: Smooth Maps and Submanifolds]]
- [[§43 One-Forms#^prop-43-1|Proposition §43.1: One-Forms in Coordinates]]
- [[§44 Vector Fields#^prop-44-1|Proposition §44.1: Vector Fields in Coordinates]]

## Connections
- **Used for.** Transport of smooth structure ([[§18 Smooth Functions and Smooth Maps#^prop-18-6|§18.6]]), smoothness of projections and slice inclusions ([[§18 Smooth Functions and Smooth Maps#^prop-18-9|§18.9]]), diffeomorphisms onto open sets being charts ([[§32 Submersions#^lem-32-3|§32.3]], the step that finishes the [[Submersion Normal Form]]) and smooth maps into submanifolds ([[§33 Submanifolds#^lem-33-3|§33.3]]).
- **Why compatibility is needed.** The proof pays one transition function, which is smooth because both charts lie in one maximal atlas ([[Unique Maximal Atlas]], [[§16 Differentiable Structures#^thm-16-1|§16.1]]). Charts from different structures give different answers: with ℝ̃ the line with the chart ∛x, the identity ℝ → ℝ̃ is not smooth, while x ↦ x³ is a diffeomorphism ([[§18 Smooth Functions and Smooth Maps#^ex-18-1|Ex. §18.1]]).
- **Same idea elsewhere.** The Euclidean core is the 452 [[Multivariable Chain Rule]]: a smooth map composed with a diffeomorphism is smooth. Between vector spaces the same check is independence of linear coordinates ([[§21 The Differential of a Map Between Vector Spaces#^lem-21-1|§21.1]]).
- **Coming later in the course.** Every later construction made in charts, from vector fields to integrals of differential forms, needs the same independence check; for integrals it comes from the change-of-variables formula.
