---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 40.1", "local normal form for immersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§40 Immersions#^thm-40-1]]

## Treated in
- [[§40 Immersions#^thm-40-1|Theorem §40.1: Local Normal Form for Immersions]], in [[§40 Immersions]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-1|Definition §19.1: Smooth Chart]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-2|Proposition §19.2: Smoothness of a Map Does Not Depend on the Charts]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-3|Proposition §19.3: The Two Notions of Diffeomorphism Agree]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-4|Lemma §19.4: Composition of Smooth Maps]]
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2: Coordinate Derivations]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§35 Local Diffeomorphisms#^def-35-1|Definition §35.1: Local Diffeomorphism]]
- [[§35 Local Diffeomorphisms#^thm-35-1|Theorem §35.1: Inverse Function Theorem]]
- [[§36 Submersions#^lem-36-3|Lemma §36.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§36 Submersions#^thm-36-4|Theorem §36.4: Local Normal Form for Submersions]]
- [[§40 Immersions#^def-40-1|Definition §40.1: Immersions]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-57|LADR 3.57 Column rank equals row rank]]

## Used in (Differentiable Manifolds)
- [[§40 Immersions#^cor-40-2|Corollary §40.2: The Local Image of an Immersion]]
- [[§41 Embeddings#^thm-41-1|Theorem §41.1: The Image of an Embedding Is a Regular Submanifold]]
- [[§41 Embeddings#^prop-41-2|Proposition §41.2: Immersions That Are Open onto Their Images]]

## Connections
- **Used for.** Locally, the image of an immersion is a submanifold of codimension n − m ([[§40 Immersions#^cor-40-2|§40.2]]).
- **Only local.** Globally the image need not be a submanifold. γ(t) = (t² − 1, t³ − t) crosses itself, making an X at the origin ([[§40 Immersions#^ex-40-1|Ex. §40.1]]). An injective immersion can run back into a point of its own image, making a T there, and then it is not a homeomorphism onto its image ([[§40 Immersions#^ex-40-2|Ex. §40.2]]).
- **Same idea elsewhere.** It mirrors the [[Submersion Normal Form]]: there F is locally a projection, here an inclusion. The case m = n is the [[Local Diffeomorphism Criterion]], from the [[Inverse Function Theorem (several variables)]]. In ℝⁿ⁺ᵏ the internal description of a manifold is a parametrization with injective derivative that is a homeomorphism onto its image ([[§20 Manifolds in Euclidean Space#^def-20-2|Def. §20.2]]), and [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] matches it with the level-set description.
- **Next: embeddings.** The immersions that are homeomorphisms onto their images have submanifolds as images ([[Images of Embeddings Are Submanifolds|§36.1]]), and an injective proper immersion is one ([[Injective Proper Immersions Are Embeddings|§36.5]]). Beyond what has been announced, Whitney's theorem embeds every manifold in some ℝᴺ.
