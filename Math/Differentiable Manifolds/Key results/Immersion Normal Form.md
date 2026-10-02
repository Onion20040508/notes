---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 32.1", "local normal form for immersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§32 Immersions#^thm-32-1]]

## Treated in
- [[§32 Immersions#^thm-32-1|Theorem §32.1: Local Normal Form for Immersions]], in [[§32 Immersions]]

## Its proof uses
- [[§2 Topological Manifolds#^lem-2-11|Lemma §2.11: Restricting and Recomposing Charts]]
- [[§13 Differentiable Structures#^def-13-3|Definition §13.3: Diffeomorphism of Open Subsets of Euclidean Space]]
- [[§15 Smooth Functions and Smooth Maps#^def-15-1|Definition §15.1: Smooth Chart]]
- [[§15 Smooth Functions and Smooth Maps#^def-15-3|Definition §15.3: Smooth Map and Diffeomorphism]]
- [[§15 Smooth Functions and Smooth Maps#^lem-15-4|Lemma §15.4: Composition of Smooth Maps]]
- [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|Proposition §23.9: Charts Are Diffeomorphisms]]
- [[§25 The Differential in Coordinates#^prop-25-1|Proposition §25.1: Partial Derivatives Upstairs and Downstairs]]
- [[§25 The Differential in Coordinates#^thm-25-2|Theorem §25.2: The Matrix of the Differential]]
- [[§28 Local Diffeomorphisms and Submersions#^def-28-1|Definition §28.1: Local Diffeomorphism]]
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-1|Theorem §28.1: Inverse Function Theorem]]
- [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|Lemma §28.6: Diffeomorphisms onto Open Sets Are Charts]]
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-7|Theorem §28.7: Local Normal Form for Submersions]]
- [[§32 Immersions#^def-32-1|Definition §32.1: Immersions]]

## Its proof uses (other subjects)
- [[Invertible ⟺ nonzero determinant]] (Linear Algebra)
- [[§9 Matrices#^ladr-3-57|LADR 3.57 Column rank equals row rank]]
- [[Inverse Function Theorem (several variables)]] (Multivariable Analysis)

## Used in (Differentiable Manifolds)
- [[§32 Immersions#^cor-32-2|Corollary §32.2: The Local Image of an Immersion]]
- [[§33 Embeddings#^thm-33-1|Theorem §33.1: The Image of an Embedding Is a Submanifold]]
- [[§33 Embeddings#^prop-33-2|Proposition §33.2: Immersions That Are Open onto Their Images]]

## Connections
- **Used for.** Locally, the image of an immersion is a submanifold of codimension n − m ([[§32 Immersions#^cor-32-2|§32.2]]).
- **Only local.** Globally the image need not be a submanifold. γ(t) = (t² − 1, t³ − t) crosses itself, making an X at the origin ([[§32 Immersions#^ex-32-1|Ex. §32.1]]). An injective immersion can run back into a point of its own image, making a T there, and then it is not a homeomorphism onto its image ([[§32 Immersions#^ex-32-2|Ex. §32.2]]).
- **Same idea elsewhere.** It mirrors the [[Submersion Normal Form]]: there F is locally a projection, here an inclusion. The case m = n is the [[Local Diffeomorphism Criterion]], from the [[Inverse Function Theorem (several variables)]]. In ℝⁿ⁺ᵏ the internal description of a manifold is a parametrization with injective derivative that is a homeomorphism onto its image ([[§16 Manifolds in Euclidean Space#^def-16-1|Def. §16.1]]), and [[§16 Manifolds in Euclidean Space#^thm-16-1|§16.1]] matches it with the level-set description.
- **Coming later in the course.** Embeddings, the immersions that are homeomorphisms onto their images, have submanifolds as images ([[§32 Immersions#^rem-32-1|announced for the next lecture]]). Beyond what has been announced, Whitney's theorem embeds every manifold in some ℝᴺ.
