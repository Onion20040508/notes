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
- (only definitions)

## Used in (Differentiable Manifolds)
- [[§32 Immersions#^cor-32-2|Corollary §32.2: The Local Image of an Immersion]]

## Connections
- **Used for.** Locally, the image of an immersion is a submanifold of codimension n − m ([[§32 Immersions#^cor-32-2|§32.2]]).
- **Only local.** Globally the image need not be a submanifold. γ(t) = (t² − 1, t³ − t) crosses itself, making an X at the origin ([[§32 Immersions#^ex-32-1|Ex. §32.1]]). An injective immersion can run back into a point of its own image, making a T there, and then it is not a homeomorphism onto its image ([[§32 Immersions#^ex-32-2|Ex. §32.2]]).
- **Same idea elsewhere.** It mirrors the [[Submersion Normal Form]]: there F is locally a projection, here an inclusion. The case m = n is the [[Local Diffeomorphism Criterion]], from the [[Inverse Function Theorem (several variables)]]. In ℝⁿ⁺ᵏ the internal description of a manifold is a parametrization with injective derivative that is a homeomorphism onto its image ([[§16 Manifolds in Euclidean Space#^def-16-1|Def. §16.1]]), and [[§16 Manifolds in Euclidean Space#^thm-16-1|§16.1]] matches it with the level-set description.
- **Coming later in the course.** Embeddings, the immersions that are homeomorphisms onto their images, have submanifolds as images ([[§32 Immersions#^rem-32-1|announced for the next lecture]]). Beyond what has been announced, Whitney's theorem embeds every manifold in some ℝᴺ.
