---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 13.5", "every atlas lies in a unique maximal atlas", "Lee Proposition 1.17"]
tags: [differentiable-manifolds, hub]
---
![[§13 Differentiable Structures#^thm-13-5]]

## Treated in
- [[§13 Differentiable Structures#^thm-13-5|Theorem §13.5: Every Atlas Lies in a Unique Maximal Atlas]], in [[§13 Differentiable Structures]]

## Its proof uses
- [[§13 Differentiable Structures#^prop-13-2|Proposition §13.2: Compatibility Is Not an Equivalence Relation]]
- [[§13 Differentiable Structures#^def-13-4|Definition §13.4: Smoothly Compatible Charts]]
- [[§13 Differentiable Structures#^def-13-6|Definition §13.6: Atlas]]
- [[§13 Differentiable Structures#^def-13-7|Definition §13.7: Compatible Atlases]]
- [[§13 Differentiable Structures#^def-13-8|Definition §13.8: Maximal Atlas]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§14 Projective Spaces as Smooth Manifolds#^thm-14-2|Theorem §14.2: The Standard Atlas Is Smooth]]
- [[§15 Smooth Functions and Smooth Maps#^ex-15-1|Example §15.1: Two Smooth Structures on the Real Line]]
- [[§15 Smooth Functions and Smooth Maps#^lem-15-4|Lemma §15.4: Composition of Smooth Maps]]
- [[§15 Smooth Functions and Smooth Maps#^prop-15-6|Proposition §15.6: Transport of Smooth Structure]]
- [[§15 Smooth Functions and Smooth Maps#^cor-15-7|Corollary §15.7: Single-Chart Structures on ℝⁿ]]
- [[§16 Manifolds in Euclidean Space#^prop-16-2|Proposition §16.2: Regular Level Sets Are Smooth Manifolds]]
- [[§16 Manifolds in Euclidean Space#^prop-16-4|Proposition §16.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§18 The Differential of a Map Between Vector Spaces#^prop-18-2|Proposition §18.2: A Vector Space Is a Smooth Manifold]]
- [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|Lemma §28.6: Diffeomorphisms onto Open Sets Are Charts]]
- [[§29 Submanifolds#^prop-29-8|Proposition §29.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Writing down any atlas specifies a smooth structure ([[§13 Differentiable Structures#^def-13-9|Def. §13.9]]): the standard atlas of ℂPⁿ ([[§14 Projective Spaces as Smooth Manifolds#^thm-14-2|§14.2]]), graph charts on level sets ([[Regular Level Sets Are Smooth Manifolds]]), linear charts on a vector space ([[§18 The Differential of a Map Between Vector Spaces#^prop-18-2|§18.2]]). Two atlases give the same structure exactly when they are compatible, which is how the three circle atlases are compared ([[§16 Manifolds in Euclidean Space#^prop-16-4|§16.4]]).
- **Why the proof needs the atlas.** Compatibility of charts is not transitive ([[§13 Differentiable Structures#^prop-13-2|§13.2]]), so the charts compatible with one given chart need not form an atlas. The proof passes through a chart of the given atlas at each point of an overlap ([[§13 Differentiable Structures#^rem-13-7|§8, Remark]]).
- **Different structures.** ℝ with the identity chart and ℝ with the chart ∛x have different maximal atlases, yet they are diffeomorphic ([[§15 Smooth Functions and Smooth Maps#^ex-15-1|Ex. §15.1]], [[§15 Smooth Functions and Smooth Maps#^cor-15-7|§15.7]]). Structures that are not even diffeomorphic exist, on S⁷ and on ℝ⁴ ([[§15 Smooth Functions and Smooth Maps#^rem-15-8|Distinct Structures versus Non-Diffeomorphic Manifolds]]).
- **Coming later in the course.** Integration of differential forms and Stokes' theorem need an orientation, given by an atlas whose transition maps have positive Jacobian determinant; such an atlas likewise lies in a unique maximal one.
