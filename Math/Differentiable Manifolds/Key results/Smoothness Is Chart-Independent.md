---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 15.2", "Lee Proposition 2.5"]
tags: [differentiable-manifolds, hub]
---
![[§15 Smooth Functions and Smooth Maps#^prop-15-2]]

## Treated in
- [[§15 Smooth Functions and Smooth Maps#^prop-15-2|Proposition §15.2: Smoothness of a Map Does Not Depend on the Charts]], in [[§15 Smooth Functions and Smooth Maps]]

## Its proof uses
- [[§13 Differentiable Structures#^ex-13-1|Example §13.1: Euclidean Space]]
- [[§13 Differentiable Structures#^def-13-4|Definition §13.4: Smoothly Compatible Charts]]
- [[§15 Smooth Functions and Smooth Maps#^def-15-1|Definition §15.1: Smooth Chart]]
- [[§15 Smooth Functions and Smooth Maps#^def-15-2|Definition §15.2: Smooth Function on a Manifold]]
- [[§15 Smooth Functions and Smooth Maps#^def-15-3|Definition §15.3: Smooth Map and Diffeomorphism]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§15 Smooth Functions and Smooth Maps#^prop-15-6|Proposition §15.6: Transport of Smooth Structure]]
- [[§15 Smooth Functions and Smooth Maps#^prop-15-9|Proposition §15.9: Projections and Slice Inclusions Are Smooth]]
- [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|Lemma §28.6: Diffeomorphisms onto Open Sets Are Charts]]
- [[§29 Submanifolds#^lem-29-3|Lemma §29.3: Smooth Maps and Submanifolds]]

## Connections
- **Used for.** Transport of smooth structure ([[§15 Smooth Functions and Smooth Maps#^prop-15-6|§15.6]]), smoothness of projections and slice inclusions ([[§15 Smooth Functions and Smooth Maps#^prop-15-9|§15.9]]), diffeomorphisms onto open sets being charts ([[§28 Local Diffeomorphisms and Submersions#^lem-28-6|§28.6]], the step that finishes the [[Submersion Normal Form]]) and smooth maps into submanifolds ([[§29 Submanifolds#^lem-29-3|§29.3]]).
- **Why compatibility is needed.** The proof pays one transition function, which is smooth because both charts lie in one maximal atlas ([[Unique Maximal Atlas]], [[§13 Differentiable Structures#^thm-13-1|§13.1]]). Charts from different structures give different answers: with ℝ̃ the line with the chart ∛x, the identity ℝ → ℝ̃ is not smooth, while x ↦ x³ is a diffeomorphism ([[§15 Smooth Functions and Smooth Maps#^ex-15-1|Ex. §15.1]]).
- **Same idea elsewhere.** The Euclidean core is the 452 [[Multivariable Chain Rule]]: a smooth map composed with a diffeomorphism is smooth. Between vector spaces the same check is independence of linear coordinates ([[§18 The Differential of a Map Between Vector Spaces#^lem-18-1|§18.1]]).
- **Coming later in the course.** Every later construction made in charts, from vector fields to integrals of differential forms, needs the same independence check; for integrals it comes from the change-of-variables formula.
