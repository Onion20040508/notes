---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 41.1", "local normal form for immersions", "Lee Theorem 4.12"]
tags: [differentiable-manifolds, hub]
---
![[§41 Immersions#^thm-41-1]]

## Treated in
- [[§41 Immersions#^thm-41-1|Theorem §41.1: Local Normal Form for Immersions]], in [[§41 Immersions]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§17 Differentiable Structures#^lem-17-6|Lemma §17.6: Restricting and Recomposing Smooth Charts]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-2|Proposition §19.2: Smoothness of a Map Does Not Depend on the Charts]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-3|Lemma §19.3: A Chart Mapped into a Given Chart]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-4|Proposition §19.4: The Two Notions of Diffeomorphism Agree]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-5|Lemma §19.5: Composition of Smooth Maps]]
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2: Coordinate Derivations]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§35 Local Diffeomorphisms#^thm-35-1|Theorem §35.1: Inverse Function Theorem]]
- [[§36 Submersions#^lem-36-5|Lemma §36.5: Diffeomorphisms onto Open Sets Are Charts]]
- [[§36 Submersions#^thm-36-6|Theorem §36.6: Local Normal Form for Submersions]]

## Used in (Differentiable Manifolds)
- [[§41 Immersions#^cor-41-2|Corollary §41.2: The Local Image of an Immersion]]
- [[§42 Embeddings#^thm-42-1|Theorem §42.1: The Image of an Embedding Is a Regular Submanifold]]
- [[§42 Embeddings#^prop-42-2|Proposition §42.2: Immersions That Are Open onto Their Images]]

## Connections
- **Used for.** Locally, the image of an immersion is a submanifold of codimension n − m ([[§41 Immersions#^cor-41-2|§41.2]]).
- **Only local.** Globally the image need not be a submanifold. γ(t) = (t² − 1, t³ − t) crosses itself, making an X at the origin ([[§41 Immersions#^ex-41-1|Ex. §41.1]]). An injective immersion can run back into a point of its own image, making a T there, and then it is not a homeomorphism onto its image ([[§41 Immersions#^ex-41-2|Ex. §41.2]]).
- **Same idea elsewhere.** It mirrors the [[Submersion Normal Form]]: there F is locally a projection, here an inclusion. The case m = n is the [[Local Diffeomorphism Criterion]], from the [[Inverse Function Theorem (several variables)]]. In ℝⁿ⁺ᵏ the internal description of a manifold is a parametrization with injective derivative that is a homeomorphism onto its image ([[§20 Manifolds in Euclidean Space#^def-20-2|Def. §20.2]]), and [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] matches it with the level-set description.
- **Next: embeddings.** The immersions that are homeomorphisms onto their images have submanifolds as images ([[Images of Embeddings Are Submanifolds|§36.1]]), and an injective proper immersion is one ([[Injective Proper Immersions Are Embeddings|§36.5]]). Beyond what has been announced, Whitney's theorem embeds every manifold in some ℝᴺ.
