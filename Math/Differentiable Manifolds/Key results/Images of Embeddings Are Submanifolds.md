---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 41.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§41 Embeddings#^thm-41-1]]

## Treated in
- [[§41 Embeddings#^thm-41-1|Theorem §41.1: The Image of an Embedding Is a Regular Submanifold]], in [[§41 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§37 Regular Submanifolds#^def-37-2|Definition §37.2: Regular Submanifold]]
- [[§37 Regular Submanifolds#^def-37-3|Definition §37.3: Adapted Chart]]
- [[§40 Immersions#^thm-40-1|Theorem §40.1: Local Normal Form for Immersions]]
- [[§40 Immersions#^cor-40-2|Corollary §40.2: The Local Image of an Immersion]]
- [[§41 Embeddings#^def-41-1|Definition §41.1: Embedding]]

## Its proof uses (other subjects)
- [[§10 Continuous Functions#^prop-10-2|590 §10.2: Equivalent Definition of Homeomorphism]]

## Used in (Differentiable Manifolds)
- [[§41 Embeddings#^prop-41-2|Proposition §41.2: Immersions That Are Open onto Their Images]]
- [[§41 Embeddings#^cor-41-3|Corollary §41.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§41 Embeddings#^prop-41-7|Proposition §41.7: Images of Embeddings Are Locally Closed]]
- [[§41 Embeddings#^cor-41-8|Corollary §41.8: Dense Regular Submanifolds Are Open]]
- [[§41 Embeddings#^prop-41-15|Proposition §41.15: When an Immersed Submanifold Is Regular]]
- [[§44 The Unit Quaternions and SU(2)#^prop-44-5|Proposition §44.5: S³ Is SU(2)]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§41 Embeddings#^cor-41-3|§41.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§40 Immersions#^cor-40-2|§40.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the [[Torus|torus]] is an injective immersion with dense image ([[§41 Embeddings#^prop-41-12|Prop. §41.12]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§41 Embeddings#^rem-41-1|Where Is Injectivity Used?]]), which gives [[§41 Embeddings#^prop-41-2|§41.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§35 Local Diffeomorphisms#^ex-35-1|Ex. §35.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]).
