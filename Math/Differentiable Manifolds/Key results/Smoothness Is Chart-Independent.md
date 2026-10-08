---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 19.2", "Lee Proposition 2.5"]
tags: [differentiable-manifolds, hub]
---
![[§19 Smooth Functions and Smooth Maps#^prop-19-2]]

## Treated in
- [[§19 Smooth Functions and Smooth Maps#^prop-19-2|Proposition §19.2: Smoothness of a Map Does Not Depend on the Charts]], in [[§19 Smooth Functions and Smooth Maps]]

## Its proof uses
- [[§17 Differentiable Structures#^ex-17-1|Example §17.1: Euclidean Space]]
- [[§17 Differentiable Structures#^def-17-4|Definition §17.4: Smoothly Compatible Charts]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-1|Definition §19.1: Smooth Chart]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-2|Definition §19.2: Smooth Function on a Manifold]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-3|Definition §19.3: Smooth Map]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§19 Smooth Functions and Smooth Maps#^prop-19-6|Proposition §19.6: Transport of Smooth Structure]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-9|Proposition §19.9: Projections and Slice Inclusions Are Smooth]]
- [[§34 Submersions#^lem-34-3|Lemma §34.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3: Smooth Maps and Regular Submanifolds]]
- [[§47 One-Forms#^prop-47-1|Proposition §47.1: One-Forms in Coordinates]]
- [[§48 Vector Fields#^prop-48-1|Proposition §48.1: Vector Fields in Coordinates]]

## Connections
- **Used for.** Transport of smooth structure ([[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]), smoothness of projections and slice inclusions ([[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]]), diffeomorphisms onto open sets being charts ([[§34 Submersions#^lem-34-3|§34.3]], the step that finishes the [[Submersion Normal Form]]) and smooth maps into submanifolds ([[§35 Regular Submanifolds#^lem-35-3|§35.3]]).
- **Why compatibility is needed.** The proof pays one transition function, which is smooth because both charts lie in one maximal atlas ([[Unique Maximal Atlas]], [[§17 Differentiable Structures#^thm-17-1|§17.1]]). Charts from different structures give different answers: with ℝ̃ the line with the chart ∛x, the identity ℝ → ℝ̃ is not smooth, while x ↦ x³ is a diffeomorphism ([[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]]).
- **Same idea elsewhere.** The Euclidean core is the 452 [[Multivariable Chain Rule]]: a smooth map composed with a diffeomorphism is smooth. Between vector spaces the same check is independence of linear coordinates ([[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]]).
- **Coming later in the course.** Every later construction made in charts, from vector fields to integrals of differential forms, needs the same independence check; for integrals it comes from the [[Change of Variables Formula (multiple integrals)|change-of-variables formula]].
