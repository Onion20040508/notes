---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 38.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§38 Embeddings#^thm-38-1]]

## Treated in
- [[§38 Embeddings#^thm-38-1|Theorem §38.1: The Image of an Embedding Is a Submanifold]], in [[§38 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§35 Submanifolds#^def-35-1|Definition §35.1: Submanifold]]
- [[§35 Submanifolds#^def-35-2|Definition §35.2: Adapted Chart]]
- [[§37 Immersions#^thm-37-1|Theorem §37.1: Local Normal Form for Immersions]]
- [[§37 Immersions#^cor-37-2|Corollary §37.2: The Local Image of an Immersion]]
- [[§38 Embeddings#^def-38-1|Definition §38.1: Embedding]]

## Its proof uses (other subjects)
- [[§10 Continuous Functions#^prop-10-2|590 §10.2: Equivalent Definition of Homeomorphism]]

## Used in (Differentiable Manifolds)
- [[§38 Embeddings#^cor-38-3|Corollary §38.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§38 Embeddings#^prop-38-7|Proposition §38.7: Images of Embeddings Are Locally Closed]]
- [[§38 Embeddings#^cor-38-8|Corollary §38.8: Dense Submanifolds Are Open]]
- [[§40 The Unit Quaternions and SU(2)#^prop-40-5|Proposition §40.5: S³ Is SU(2)]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§38 Embeddings#^cor-38-3|§38.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§37 Immersions#^cor-37-2|§37.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the [[Torus|torus]] is an injective immersion with dense image ([[§38 Embeddings#^prop-38-11|Prop. §38.11]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§38 Embeddings#^rem-38-1|Where Is Injectivity Used?]]), which gives [[§38 Embeddings#^prop-38-2|§38.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§33 Local Diffeomorphisms#^ex-33-1|Ex. §33.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§35 Submanifolds#^def-35-1|Def. §35.1]]).
