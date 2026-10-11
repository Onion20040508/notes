---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 38.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§40 Embeddings#^thm-40-1]]

## Treated in
- [[§40 Embeddings#^thm-40-1|Theorem §40.1: The Image of an Embedding Is a Regular Submanifold]], in [[§40 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10: Restricting and Recomposing Charts]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§37 Regular Submanifolds#^def-37-1|Definition §37.1: Regular Submanifold]]
- [[§37 Regular Submanifolds#^def-37-2|Definition §37.2: Adapted Chart]]
- [[§39 Immersions#^thm-39-1|Theorem §39.1: Local Normal Form for Immersions]]
- [[§39 Immersions#^cor-39-2|Corollary §39.2: The Local Image of an Immersion]]
- [[§40 Embeddings#^def-40-1|Definition §40.1: Embedding]]

## Its proof uses (other subjects)
- [[§10 Continuous Functions#^prop-10-2|590 §10.2: Equivalent Definition of Homeomorphism]]

## Used in (Differentiable Manifolds)
- [[§40 Embeddings#^prop-40-2|Proposition §40.2: Immersions That Are Open onto Their Images]]
- [[§40 Embeddings#^cor-40-3|Corollary §40.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§40 Embeddings#^prop-40-7|Proposition §40.7: Images of Embeddings Are Locally Closed]]
- [[§40 Embeddings#^cor-40-8|Corollary §40.8: Dense Regular Submanifolds Are Open]]
- [[§40 Embeddings#^prop-40-14|Proposition §40.14: When an Immersed Submanifold Is Regular]]
- [[§43 The Unit Quaternions and SU(2)#^prop-43-5|Proposition §43.5: S³ Is SU(2)]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§40 Embeddings#^cor-40-3|§40.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§39 Immersions#^cor-39-2|§39.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the [[Torus|torus]] is an injective immersion with dense image ([[§40 Embeddings#^prop-40-11|Prop. §40.11]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§40 Embeddings#^rem-40-1|Where Is Injectivity Used?]]), which gives [[§40 Embeddings#^prop-40-2|§40.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§35 Local Diffeomorphisms#^ex-35-1|Ex. §35.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§37 Regular Submanifolds#^def-37-1|Def. §37.1]]).
