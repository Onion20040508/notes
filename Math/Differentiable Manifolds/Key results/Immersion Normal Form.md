---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 35.1", "local normal form for immersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§37 Immersions#^thm-37-1]]

## Treated in
- [[§37 Immersions#^thm-37-1|Theorem §37.1: Local Normal Form for Immersions]], in [[§37 Immersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§19 Smooth Functions and Smooth Maps#^def-19-1|Definition §19.1: Smooth Chart]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-4|Lemma §19.4: Composition of Smooth Maps]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§33 Local Diffeomorphisms#^def-33-1|Definition §33.1: Local Diffeomorphism]]
- [[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1: Inverse Function Theorem]]
- [[§34 Submersions#^lem-34-3|Lemma §34.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§34 Submersions#^thm-34-4|Theorem §34.4: Local Normal Form for Submersions]]
- [[§37 Immersions#^def-37-1|Definition §37.1: Immersions]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-57|LADR 3.57 Column rank equals row rank]]

## Used in (Differentiable Manifolds)
- [[§37 Immersions#^cor-37-2|Corollary §37.2: The Local Image of an Immersion]]
- [[§38 Embeddings#^thm-38-1|Theorem §38.1: The Image of an Embedding Is a Submanifold]]
- [[§38 Embeddings#^prop-38-2|Proposition §38.2: Immersions That Are Open onto Their Images]]

## Connections
- **Used for.** Locally, the image of an immersion is a submanifold of codimension n − m ([[§37 Immersions#^cor-37-2|§37.2]]).
- **Only local.** Globally the image need not be a submanifold. γ(t) = (t² − 1, t³ − t) crosses itself, making an X at the origin ([[§37 Immersions#^ex-37-1|Ex. §37.1]]). An injective immersion can run back into a point of its own image, making a T there, and then it is not a homeomorphism onto its image ([[§37 Immersions#^ex-37-2|Ex. §37.2]]).
- **Same idea elsewhere.** It mirrors the [[Submersion Normal Form]]: there F is locally a projection, here an inclusion. The case m = n is the [[Local Diffeomorphism Criterion]], from the [[Inverse Function Theorem (several variables)]]. In ℝⁿ⁺ᵏ the internal description of a manifold is a parametrization with injective derivative that is a homeomorphism onto its image ([[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]]), and [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] matches it with the level-set description.
- **Next: embeddings.** The immersions that are homeomorphisms onto their images have submanifolds as images ([[Images of Embeddings Are Submanifolds|§36.1]]), and an injective proper immersion is one ([[Injective Proper Immersions Are Embeddings|§36.5]]). Beyond what has been announced, Whitney's theorem embeds every manifold in some ℝᴺ.
