---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 8.5", "every atlas lies in a unique maximal atlas", "Lee Proposition 1.17"]
tags: [differentiable-manifolds, hub]
---
![[§8 Differentiable Structures#^thm-8-5]]

## Treated in
- [[§8 Differentiable Structures#^thm-8-5|Theorem §8.5: Every Atlas Lies in a Unique Maximal Atlas]], in [[§8 Differentiable Structures]]

## Its proof uses
- [[§8 Differentiable Structures#^prop-8-2|Proposition §8.2: Compatibility Is Not an Equivalence Relation]]
- [[§8 Differentiable Structures#^def-8-4|Definition §8.4: Smoothly Compatible Charts]]
- [[§8 Differentiable Structures#^def-8-6|Definition §8.6: Atlas]]
- [[§8 Differentiable Structures#^def-8-7|Definition §8.7: Compatible Atlases]]
- [[§8 Differentiable Structures#^def-8-8|Definition §8.8: Maximal Atlas]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§8 Differentiable Structures#^ex-8-5|Example §8.5: Two Smooth Structures on the Real Line]]
- [[§8 Differentiable Structures#^thm-8-7|Theorem §8.7: The Standard Atlas Is Smooth]]
- [[§8 Differentiable Structures#^lem-8-15|Lemma §8.15: Composition of Smooth Maps]]
- [[§8 Differentiable Structures#^prop-8-17|Proposition §8.17: Transport of Smooth Structure]]
- [[§8 Differentiable Structures#^cor-8-18|Corollary §8.18: Single-Chart Structures on ℝⁿ]]
- [[§9 Manifolds in Euclidean Space#^prop-9-2|Proposition §9.2: Regular Level Sets Are Smooth Manifolds]]
- [[§9 Manifolds in Euclidean Space#^prop-9-4|Proposition §9.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§10 Vector Spaces and Matrix Groups#^prop-10-9|Proposition §10.9: A Vector Space Is a Smooth Manifold]]
- [[§14 Local Diffeomorphisms and Submersions#^lem-14-7|Lemma §14.7: Diffeomorphisms onto Open Sets Are Charts]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Writing down any atlas specifies a smooth structure ([[§8 Differentiable Structures#^def-8-9|Def. §8.9]]): the standard atlas of ℂPⁿ ([[§8 Differentiable Structures#^thm-8-7|§8.7]]), graph charts on level sets ([[Regular Level Sets Are Smooth Manifolds]]), linear charts on a vector space ([[§10 Vector Spaces and Matrix Groups#^prop-10-9|§10.9]]). Two atlases give the same structure exactly when they are compatible, which is how the three circle atlases are compared ([[§9 Manifolds in Euclidean Space#^prop-9-4|§9.4]]).
- **Why the proof needs the atlas.** Compatibility of charts is not transitive ([[§8 Differentiable Structures#^prop-8-2|§8.2]]), so the charts compatible with one given chart need not form an atlas. The proof passes through a chart of the given atlas at each point of an overlap ([[§8 Differentiable Structures#^rem-8-7|§8, Remark]]).
- **Different structures.** ℝ with the identity chart and ℝ with the chart ∛x have different maximal atlases, yet they are diffeomorphic ([[§8 Differentiable Structures#^ex-8-5|Ex. §8.5]], [[§8 Differentiable Structures#^cor-8-18|§8.18]]). Structures that are not even diffeomorphic exist, on S⁷ and on ℝ⁴ ([[§8 Differentiable Structures#^rem-8-20|Distinct Structures versus Non-Diffeomorphic Manifolds]]).
- **Coming later in the course.** Integration of differential forms and Stokes' theorem need an orientation, given by an atlas whose transition maps have positive Jacobian determinant; such an atlas likewise lies in a unique maximal one.
