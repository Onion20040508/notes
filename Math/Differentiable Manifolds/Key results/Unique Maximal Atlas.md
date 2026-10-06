---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 16.5", "every atlas lies in a unique maximal atlas", "Lee Proposition 1.17"]
tags: [differentiable-manifolds, hub]
---
![[§16 Differentiable Structures#^thm-16-5]]

## Treated in
- [[§16 Differentiable Structures#^thm-16-5|Theorem §16.5: Every Atlas Lies in a Unique Maximal Atlas]], in [[§16 Differentiable Structures]]

## Its proof uses
- [[§16 Differentiable Structures#^prop-16-2|Proposition §16.2: Compatibility Is Not an Equivalence Relation]]
- [[§16 Differentiable Structures#^def-16-4|Definition §16.4: Smoothly Compatible Charts]]
- [[§16 Differentiable Structures#^def-16-6|Definition §16.6: Atlas]]
- [[§16 Differentiable Structures#^def-16-7|Definition §16.7: Compatible Atlases]]
- [[§16 Differentiable Structures#^def-16-8|Definition §16.8: Maximal Atlas]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§17 Projective Spaces as Smooth Manifolds#^thm-17-2|Theorem §17.2: The Standard Atlas Is Smooth]]
- [[§18 Smooth Functions and Smooth Maps#^ex-18-1|Example §18.1: Two Smooth Structures on the Real Line]]
- [[§18 Smooth Functions and Smooth Maps#^lem-18-4|Lemma §18.4: Composition of Smooth Maps]]
- [[§18 Smooth Functions and Smooth Maps#^prop-18-6|Proposition §18.6: Transport of Smooth Structure]]
- [[§18 Smooth Functions and Smooth Maps#^cor-18-7|Corollary §18.7: Single-Chart Structures on ℝⁿ]]
- [[§19 Manifolds in Euclidean Space#^prop-19-2|Proposition §19.2: Regular Level Sets Are Smooth Manifolds]]
- [[§19 Manifolds in Euclidean Space#^prop-19-4|Proposition §19.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§21 The Differential of a Map Between Vector Spaces#^prop-21-2|Proposition §21.2: A Vector Space Is a Smooth Manifold]]
- [[§32 Submersions#^lem-32-3|Lemma §32.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Writing down any atlas specifies a smooth structure ([[§16 Differentiable Structures#^def-16-9|Def. §16.9]]): the standard atlas of ℂPⁿ ([[§17 Projective Spaces as Smooth Manifolds#^thm-17-2|§17.2]]), graph charts on level sets ([[Regular Level Sets Are Smooth Manifolds]]), linear charts on a vector space ([[§21 The Differential of a Map Between Vector Spaces#^prop-21-2|§21.2]]). Two atlases give the same structure exactly when they are compatible, which is how the three circle atlases are compared ([[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]]).
- **Why the proof needs the atlas.** Compatibility of charts is not transitive ([[§16 Differentiable Structures#^prop-16-2|§16.2]]), so the charts compatible with one given chart need not form an atlas. The proof passes through a chart of the given atlas at each point of an overlap ([[§16 Differentiable Structures#^pf-16-5|proof of §16.5]], [[§16 Differentiable Structures#^rem-16-7|§16, Remark]]).
- **Different structures.** ℝ with the identity chart and ℝ with the chart ∛x have different maximal atlases, yet they are diffeomorphic ([[§18 Smooth Functions and Smooth Maps#^ex-18-1|Ex. §18.1]], [[§18 Smooth Functions and Smooth Maps#^cor-18-7|§18.7]]). Structures that are not even diffeomorphic exist, on S⁷ and on ℝ⁴ ([[§18 Smooth Functions and Smooth Maps#^rem-18-8|Distinct Structures versus Non-Diffeomorphic Manifolds]]).
- **Coming later in the course.** Integration of differential forms and Stokes' theorem (452 states it for oriented compact regions: [[Generalized Stokes' Theorem]]) need an orientation, given by an atlas whose transition maps have positive Jacobian determinant; such an atlas likewise lies in a unique maximal one.
