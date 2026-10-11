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
- [[§17 Differentiable Structures#^def-17-6|Definition §17.6: Atlas]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-1|Definition §19.1: Smooth Chart]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-2|Definition §19.2: Smooth Function on a Manifold]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-3|Definition §19.3: Smooth Map]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Example §19.1: Two Smooth Structures on the Real Line]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-5|Proposition §19.5: Inclusions of and Maps into Open Subsets]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-7|Proposition §19.7: Transport of Smooth Structure]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-10|Proposition §19.10: Projections and Slice Inclusions Are Smooth]]
- [[§20 Manifolds in Euclidean Space#^lem-20-3|Lemma §20.3: Smooth Maps into and out of Regular Level Sets]]
- [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|Proposition §22.2: A Vector Space Is a Smooth Manifold]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§30 The Differential in Coordinates#^prop-30-8|Proposition §30.8: Regular Values Inside One Chart]]
- [[§30 The Differential in Coordinates#^prop-30-10|Proposition §30.10: Maps with Zero Differential Are Constant]]
- [[§35 Local Diffeomorphisms#^thm-35-2|Theorem §35.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§35 Local Diffeomorphisms#^cor-35-3|Corollary §35.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms]]
- [[§36 Submersions#^lem-36-3|Lemma §36.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§37 Regular Submanifolds#^lem-37-5|Lemma §37.5: Smooth Maps and Regular Submanifolds]]
- [[§39 Examples of Fibrations#^prop-39-1|Proposition §39.1: The Möbius Band Is a Fibration]]
- [[§40 Immersions#^thm-40-1|Theorem §40.1: Local Normal Form for Immersions]]
- [[§50 One-Forms#^prop-50-1|Proposition §50.1: One-Forms in Coordinates]]
- [[§50 One-Forms#^prop-50-5|Proposition §50.5: Pullbacks in Coordinates]]
- [[§51 Vector Fields#^prop-51-1|Proposition §51.1: Vector Fields in Coordinates]]

## Connections
- **Used for.** Transport of smooth structure ([[§19 Smooth Functions and Smooth Maps#^prop-19-7|§19.7]]), smoothness of projections and slice inclusions ([[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]), diffeomorphisms onto open sets being charts ([[§36 Submersions#^lem-36-3|§36.3]], the step that finishes the [[Submersion Normal Form]]) and smooth maps into submanifolds ([[§37 Regular Submanifolds#^lem-37-5|§37.5]]).
- **Why compatibility is needed.** The proof pays one transition function, which is smooth because both charts lie in one maximal atlas ([[Unique Maximal Atlas]], [[§17 Differentiable Structures#^thm-17-1|§17.1]]). Charts from different structures give different answers: with ℝ̃ the line with the chart ∛x, the identity ℝ → ℝ̃ is not smooth, while x ↦ x³ is a diffeomorphism ([[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]]).
- **Same idea elsewhere.** The Euclidean core is the 452 [[Multivariable Chain Rule]]: a smooth map composed with a diffeomorphism is smooth. Between vector spaces the same check is independence of linear coordinates ([[§22 The Differential of a Map Between Vector Spaces#^lem-22-1|§22.1]]).
- **Coming later in the course.** Every later construction made in charts, from vector fields to integrals of differential forms, needs the same independence check; for integrals it comes from the [[Change of Variables Formula (multiple integrals)|change-of-variables formula]].
