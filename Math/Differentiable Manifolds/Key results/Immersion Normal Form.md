---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 35.1", "local normal form for immersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§35 Immersions#^thm-35-1]]

## Treated in
- [[§35 Immersions#^thm-35-1|Theorem §35.1: Local Normal Form for Immersions]], in [[§35 Immersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§16 Differentiable Structures#^def-16-3|Definition §16.3: Diffeomorphism of Open Subsets of Euclidean Space]]
- [[§18 Smooth Functions and Smooth Maps#^def-18-1|Definition §18.1: Smooth Chart]]
- [[§18 Smooth Functions and Smooth Maps#^def-18-3|Definition §18.3: Smooth Map and Diffeomorphism]]
- [[§18 Smooth Functions and Smooth Maps#^lem-18-4|Lemma §18.4: Composition of Smooth Maps]]
- [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|Proposition §26.9: Charts Are Diffeomorphisms]]
- [[§28 The Differential in Coordinates#^prop-28-1|Proposition §28.1: Partial Derivatives Upstairs and Downstairs]]
- [[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2: The Matrix of the Differential]]
- [[§31 Local Diffeomorphisms#^thm-31-1|Theorem §31.1: Inverse Function Theorem]]
- [[§31 Local Diffeomorphisms#^def-31-1|Definition §31.1: Local Diffeomorphism]]
- [[§32 Submersions#^lem-32-3|Lemma §32.3: Diffeomorphisms onto Open Sets Are Charts]]
- [[§32 Submersions#^thm-32-4|Theorem §32.4: Local Normal Form for Submersions]]
- [[§35 Immersions#^def-35-1|Definition §35.1: Immersions]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-57|LADR 3.57 Column rank equals row rank]]

## Used in (Differentiable Manifolds)
- [[§35 Immersions#^cor-35-2|Corollary §35.2: The Local Image of an Immersion]]
- [[§36 Embeddings#^thm-36-1|Theorem §36.1: The Image of an Embedding Is a Submanifold]]
- [[§36 Embeddings#^prop-36-2|Proposition §36.2: Immersions That Are Open onto Their Images]]

## Connections
- **Used for.** Locally, the image of an immersion is a submanifold of codimension n − m ([[§35 Immersions#^cor-35-2|§35.2]]).
- **Only local.** Globally the image need not be a submanifold. γ(t) = (t² − 1, t³ − t) crosses itself, making an X at the origin ([[§35 Immersions#^ex-35-1|Ex. §35.1]]). An injective immersion can run back into a point of its own image, making a T there, and then it is not a homeomorphism onto its image ([[§35 Immersions#^ex-35-2|Ex. §35.2]]).
- **Same idea elsewhere.** It mirrors the [[Submersion Normal Form]]: there F is locally a projection, here an inclusion. The case m = n is the [[Local Diffeomorphism Criterion]], from the [[Inverse Function Theorem (several variables)]]. In ℝⁿ⁺ᵏ the internal description of a manifold is a parametrization with injective derivative that is a homeomorphism onto its image ([[§19 Manifolds in Euclidean Space#^def-19-1|Def. §19.1]]), and [[§19 Manifolds in Euclidean Space#^thm-19-1|§19.1]] matches it with the level-set description.
- **Next: embeddings.** The immersions that are homeomorphisms onto their images have submanifolds as images ([[Images of Embeddings Are Submanifolds|§36.1]]), and an injective proper immersion is one ([[Injective Proper Immersions Are Embeddings|§36.5]]). Beyond what has been announced, Whitney's theorem embeds every manifold in some ℝᴺ.
