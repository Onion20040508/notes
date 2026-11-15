---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 44.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§41 Embeddings#^thm-41-1]]

## Treated in
- [[§41 Embeddings#^thm-41-1|Theorem §41.1: The Image of an Embedding Is a Regular Submanifold]], in [[§41 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§17 Differentiable Structures#^lem-17-7|Lemma §17.7: Restricting and Recomposing Smooth Charts]]
- [[§37 Regular Submanifolds#^def-37-2|Definition §37.2: Regular Submanifold]]
- [[§37 Regular Submanifolds#^def-37-3|Definition §37.3: Adapted Chart]]
- [[§40 Immersions#^thm-40-1|Theorem §40.1: Local Normal Form for Immersions]]
- [[§40 Immersions#^cor-40-2|Corollary §40.2: The Local Image of an Immersion]]
- [[§41 Embeddings#^def-41-1|Definition §41.1: Embedding]]

## Used in (Differentiable Manifolds)
- [[§41 Embeddings#^prop-41-2|Proposition §41.2: Immersions That Are Open onto Their Images]]
- [[§41 Embeddings#^cor-41-3|Corollary §41.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§41 Embeddings#^prop-41-10|Proposition §41.10: Images of Embeddings Are Locally Closed]]
- [[§41 Embeddings#^cor-41-11|Corollary §41.11: Dense Regular Submanifolds Are Open]]
- [[§45 Fibrations#^prop-45-6|Proposition §45.6: Sections Are Closed Embeddings]]
- [[§41 Embeddings#^prop-41-18|Proposition §41.18: When an Immersed Submanifold Is Regular]]
- [[§43 The Unit Quaternions and SU(2)#^prop-43-5|Proposition §43.5: S³ Is SU(2)]]
- [[§66 The Whitney Embedding Theorem#^thm-66-6|Theorem §66.6: The Whitney Theorems for Compact Manifolds]]
- [[§66 The Whitney Embedding Theorem#^lem-66-8|Lemma §66.8: Proper Embeddings into ℝ²ᵐ⁺¹]]
- [[§66 The Whitney Embedding Theorem#^prop-66-10|Proposition §66.10: Immersions into ℝ²ᵐ from Any Embedding]]
- [[§66 The Whitney Embedding Theorem#^cor-66-12|Corollary §66.12: Every Manifold Has a Morse Function]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§41 Embeddings#^cor-41-3|§41.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§40 Immersions#^cor-40-2|§40.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the [[Torus|torus]] is an injective immersion with dense image ([[§41 Embeddings#^prop-41-14|Prop. §41.14]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§41 Embeddings#^rem-41-1|Where Is Injectivity Used?]]), which gives [[§41 Embeddings#^prop-41-2|§41.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§35 Local Diffeomorphisms#^ex-35-1|Ex. §35.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]).
