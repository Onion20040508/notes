---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 17.5", "every atlas lies in a unique maximal atlas", "Lee Proposition 1.17"]
tags: [differentiable-manifolds, hub]
---
![[§17 Differentiable Structures#^thm-17-5]]

## Treated in
- [[§17 Differentiable Structures#^thm-17-5|Theorem §17.5: Every Atlas Lies in a Unique Maximal Atlas]], in [[§17 Differentiable Structures]]

## Its proof uses
- [[§2 Topological Manifolds#^prop-2-11|Proposition §2.11: Transition Functions Are Homeomorphisms]]
- [[§17 Differentiable Structures#^prop-17-2|Proposition §17.2: Compatibility Is Not an Equivalence Relation]]
- [[§17 Differentiable Structures#^def-17-3|Definition §17.3: Diffeomorphism of Open Subsets of Euclidean Space]]
- [[§17 Differentiable Structures#^def-17-4|Definition §17.4: Smoothly Compatible Charts]]
- [[§17 Differentiable Structures#^def-17-6|Definition §17.6: Atlas]]
- [[§17 Differentiable Structures#^def-17-7|Definition §17.7: Compatible Atlases]]
- [[§17 Differentiable Structures#^def-17-8|Definition §17.8: Maximal Atlas]]

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§17 Differentiable Structures#^prop-17-7|Proposition §17.7: Open Subsets of a Smooth Manifold Are Smooth Manifolds]]
- [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|Theorem §18.2: The Standard Atlas Is Smooth]]
- [[§18 Projective Spaces as Smooth Manifolds#^cor-18-5|Corollary §18.5: Real Projective Space]]
- [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Example §19.1: Two Smooth Structures on the Real Line]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-4|Proposition §19.4: The Two Notions of Diffeomorphism Agree]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-8|Proposition §19.8: Transport of Smooth Structure]]
- [[§19 Smooth Functions and Smooth Maps#^cor-19-9|Corollary §19.9: Single-Chart Structures on ℝⁿ]]
- [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2: Regular Level Sets Are Smooth Manifolds]]
- [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|Proposition §22.2: A Vector Space Is a Smooth Manifold]]
- [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|Corollary §23.2: Consequences]]
- [[§24 The Circle#^prop-24-1|Proposition §24.1: The Three Circle Atlases Define One Smooth Structure]]
- [[§36 Submersions#^lem-36-5|Lemma §36.5: Diffeomorphisms onto Open Sets Are Charts]]
- [[§37 Regular Submanifolds#^prop-37-1|Proposition §37.1: Open Subsets of a Product]]
- [[§37 Regular Submanifolds#^prop-37-3|Proposition §37.3: The Induced Smooth Structure]]
- [[§37 Regular Submanifolds#^prop-37-4|Proposition §37.4: Open Submanifolds Are the Regular Submanifolds of Codimension 0]]
- [[§37 Regular Submanifolds#^prop-37-9|Proposition §37.9: Regular Submanifolds of ℝⁿ⁺ᵏ: The Fourth Description]]
- [[§37 Regular Submanifolds#^prop-37-14|Proposition §37.14: The Old and New Versions Agree]]
- [[§39 Examples of Fibrations#^prop-39-1|Proposition §39.1: The Möbius Band Is a Fibration]]
- [[§49 The Tangent Bundle#^cor-49-3|Corollary §49.3: The Tangent Bundle Is a Fibration]]
- [[§52 Critical Points and the Hessian#^ex-52-1|Example §52.1: The Hessian Matrix Depends on the Chart]]

## Connections
- **Used for.** Writing down any atlas specifies a smooth structure ([[§17 Differentiable Structures#^def-17-9|Def. §17.9]]): the standard atlas of ℂPⁿ ([[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|§18.2]]), graph charts on level sets ([[Regular Level Sets Are Smooth Manifolds]]), linear charts on a vector space ([[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]). Two atlases give the same structure exactly when they are compatible, which is how the three circle atlases are compared ([[§24 The Circle#^prop-24-1|§24.1]]).
- **Why the proof needs the atlas.** Compatibility of charts is not transitive ([[§17 Differentiable Structures#^prop-17-2|§17.2]]), so the charts compatible with one given chart need not form an atlas. The proof passes through a chart of the given atlas at each point of an overlap ([[§17 Differentiable Structures#^pf-17-5|proof of §17.5]], [[§17 Differentiable Structures#^rem-17-8|§17, Remark]]).
- **Different structures.** ℝ with the identity chart and ℝ with the chart ∛x have different maximal atlases, yet they are diffeomorphic ([[§19 Smooth Functions and Smooth Maps#^ex-19-1|Ex. §19.1]], [[§19 Smooth Functions and Smooth Maps#^cor-19-9|§19.9]]). Structures that are not even diffeomorphic exist, on S⁷ and on ℝ⁴ ([[§19 Smooth Functions and Smooth Maps#^rem-19-8|Distinct Structures versus Non-Diffeomorphic Manifolds]]).
- **Coming later in the course.** Integration of differential forms and Stokes' theorem (452 states it for oriented compact regions: [[Generalized Stokes' Theorem]]) need an orientation, given by an atlas whose transition maps have positive Jacobian determinant; such an atlas likewise lies in a unique maximal one.
