---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 8.13", "Lee Proposition 2.5"]
tags: [differentiable-manifolds, hub]
---
![[§8 Differentiable Structures#^prop-8-13]]

## Treated in
- [[§8 Differentiable Structures#^prop-8-13|Proposition §8.13: Smoothness of a Map Does Not Depend on the Charts]], in [[§8 Differentiable Structures]]

## Its proof uses
- [[§8 Differentiable Structures#^ex-8-1|Example §8.1: Euclidean Space]]
- [[§8 Differentiable Structures#^def-8-4|Definition §8.4: Smoothly Compatible Charts]]
- [[§8 Differentiable Structures#^def-8-12|Definition §8.12: Smooth Chart]]
- [[§8 Differentiable Structures#^def-8-13|Definition §8.13: Smooth Function on a Manifold]]
- [[§8 Differentiable Structures#^def-8-14|Definition §8.14: Smooth Map and Diffeomorphism]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§8 Differentiable Structures#^prop-8-17|Proposition §8.17: Transport of Smooth Structure]]
- [[§8 Differentiable Structures#^prop-8-20|Proposition §8.20: Projections and Slice Inclusions Are Smooth]]
- [[§14 Local Diffeomorphisms and Submersions#^lem-14-7|Lemma §14.7: Diffeomorphisms onto Open Sets Are Charts]]
- [[§15 Submanifolds#^lem-15-3|Lemma §15.3: Smooth Maps and Submanifolds]]

## Connections
- **Used for.** Transport of smooth structure ([[§8 Differentiable Structures#^prop-8-17|§8.17]]), smoothness of projections and slice inclusions ([[§8 Differentiable Structures#^prop-8-20|§8.20]]), diffeomorphisms onto open sets being charts ([[§14 Local Diffeomorphisms and Submersions#^lem-14-7|§14.7]], the step that finishes the [[Submersion Normal Form]]) and smooth maps into submanifolds ([[§15 Submanifolds#^lem-15-3|§15.3]]).
- **Why compatibility is needed.** The proof pays one transition function, which is smooth because both charts lie in one maximal atlas ([[Unique Maximal Atlas]], [[§8 Differentiable Structures#^thm-8-1|§8.1]]). Charts from different structures give different answers: with ℝ̃ the line with the chart ∛x, the identity ℝ → ℝ̃ is not smooth, while x ↦ x³ is a diffeomorphism ([[§8 Differentiable Structures#^ex-8-5|Ex. §8.5]]).
- **Same idea elsewhere.** The Euclidean core is the 452 [[Multivariable Chain Rule]]: a smooth map composed with a diffeomorphism is smooth. Between vector spaces the same check is independence of linear coordinates ([[§10 Vector Spaces and Matrix Groups#^lem-10-8|§10.8]]).
- **Coming later in the course.** Every later construction made in charts, from vector fields to integrals of differential forms, needs the same independence check; for integrals it comes from the change-of-variables formula.
