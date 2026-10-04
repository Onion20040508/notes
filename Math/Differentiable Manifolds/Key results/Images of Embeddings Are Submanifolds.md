---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 37.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§37 Embeddings#^thm-37-1]]

## Treated in
- [[§37 Embeddings#^thm-37-1|Theorem §37.1: The Image of an Embedding Is a Submanifold]], in [[§37 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§33 Submanifolds#^def-33-1|Definition §33.1: Submanifold and Adapted Charts]]
- [[§36 Immersions#^thm-36-1|Theorem §36.1: Local Normal Form for Immersions]]
- [[§36 Immersions#^cor-36-2|Corollary §36.2: The Local Image of an Immersion]]
- [[§37 Embeddings#^def-37-1|Definition §37.1: Embedding]]
- [[§37 Embeddings#^rem-37-1|Remark: Where Is Injectivity Used?]]

## Its proof uses (other subjects)
- [[§9 Continuous Functions#^prop-9-2|590 §9.2: Equivalent Definition of Homeomorphism]]

## Used in (Differentiable Manifolds)
- [[§37 Embeddings#^prop-37-2|Proposition §37.2: Immersions That Are Open onto Their Images]]
- [[§37 Embeddings#^cor-37-3|Corollary §37.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§37 Embeddings#^prop-37-7|Proposition §37.7: Images of Embeddings Are Locally Closed]]
- [[§37 Embeddings#^cor-37-8|Corollary §37.8: Dense Submanifolds Are Open]]
- [[§37 Embeddings#^prop-37-11|Proposition §37.11: The Irrational Line on the Torus]]
- [[§39 SU(2) → SO(3)꞉ The Double Cover#^prop-39-5|Proposition §39.5: S³ Is SU(2)]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§37 Embeddings#^cor-37-3|§37.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§36 Immersions#^cor-36-2|§36.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the torus is an injective immersion with dense image ([[§37 Embeddings#^prop-37-11|Prop. §37.11]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§37 Embeddings#^rem-37-1|Where Is Injectivity Used?]]), which gives [[§37 Embeddings#^prop-37-2|§37.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§31 Local Diffeomorphisms#^ex-31-1|Ex. §31.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§33 Submanifolds#^def-33-1|Def. §33.1]]).
