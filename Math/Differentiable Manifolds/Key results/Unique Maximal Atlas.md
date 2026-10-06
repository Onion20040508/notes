---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 16.5", "every atlas lies in a unique maximal atlas", "Lee Proposition 1.17"]
tags: [differentiable-manifolds, hub]
---
![[§17 Differentiable Structures#^thm-17-5]]

## Treated in
- [[§17 Differentiable Structures#^thm-17-5|Theorem §17.5: Every Atlas Lies in a Unique Maximal Atlas]], in [[§17 Differentiable Structures]]

## Its proof uses
- [[§17 Differentiable Structures#^prop-17-2|Proposition §17.2: Compatibility Is Not an Equivalence Relation]]
- [[§17 Differentiable Structures#^def-17-4|Definition §17.4: Smoothly Compatible Charts]]
- [[§17 Differentiable Structures#^def-17-6|Definition §17.6: Atlas]]
- [[§17 Differentiable Structures#^def-17-7|Definition §17.7: Compatible Atlases]]
- [[§17 Differentiable Structures#^def-17-8|Definition §17.8: Maximal Atlas]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|Theorem §18.2: The Standard Atlas Is Smooth]]
- [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Example §19.1: Two Smooth Structures on the Real Line]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-4|Lemma §19.4: Composition of Smooth Maps]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-6|Proposition §19.6: Transport of Smooth Structure]]
- [[§19 Smooth Functions and Smooth Maps#^cor-19-7|Corollary §19.7: Single-Chart Structures on ℝⁿ]]
- [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2: Regular Level Sets Are Smooth Manifolds]]
- [[§24 The Circle#^prop-24-1|Proposition §24.1: The Three Circle Atlases Define One Smooth Structure]]
- [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|Proposition §22.2: A Vector Space Is a Smooth Manifold]]
- [[§34 Submersions#^lem-34-3|Lemma §34.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§35 Submanifolds#^prop-35-8|Proposition §35.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Writing down any atlas specifies a smooth structure ([[§17 Differentiable Structures#^def-17-9|Def. §17.9]]): the standard atlas of ℂPⁿ ([[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]]), graph charts on level sets ([[Regular Level Sets Are Smooth Manifolds]]), linear charts on a vector space ([[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]). Two atlases give the same structure exactly when they are compatible, which is how the three circle atlases are compared ([[§24 The Circle#^prop-24-1|§24.1]]).
- **Why the proof needs the atlas.** Compatibility of charts is not transitive ([[§17 Differentiable Structures#^prop-17-2|§17.2]]), so the charts compatible with one given chart need not form an atlas. The proof passes through a chart of the given atlas at each point of an overlap ([[§17 Differentiable Structures#^pf-17-5|proof of §17.5]], [[§17 Differentiable Structures#^rem-17-7|§17, Remark]]).
- **Different structures.** ℝ with the identity chart and ℝ with the chart ∛x have different maximal atlases, yet they are diffeomorphic ([[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]], [[§19 Smooth Functions and Smooth Maps#^cor-19-7|§19.7]]). Structures that are not even diffeomorphic exist, on S⁷ and on ℝ⁴ ([[§19 Smooth Functions and Smooth Maps#^rem-19-8|Distinct Structures versus Non-Diffeomorphic Manifolds]]).
- **Coming later in the course.** Integration of differential forms and Stokes' theorem (452 states it for oriented compact regions: [[Generalized Stokes' Theorem]]) need an orientation, given by an atlas whose transition maps have positive Jacobian determinant; such an atlas likewise lies in a unique maximal one.
