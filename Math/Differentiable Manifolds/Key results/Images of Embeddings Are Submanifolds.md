---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 36.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§36 Embeddings#^thm-36-1]]

## Treated in
- [[§36 Embeddings#^thm-36-1|Theorem §36.1: The Image of an Embedding Is a Submanifold]], in [[§36 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§33 Submanifolds#^def-33-1|Definition §33.1: Submanifold and Adapted Charts]]
- [[§35 Immersions#^thm-35-1|Theorem §35.1: Local Normal Form for Immersions]]
- [[§35 Immersions#^cor-35-2|Corollary §35.2: The Local Image of an Immersion]]
- [[§36 Embeddings#^rem-36-1|Remark: Where Is Injectivity Used?]]
- [[§36 Embeddings#^def-36-1|Definition §36.1: Embedding]]

## Its proof uses (other subjects)
- [[§9 Continuous Functions#^prop-9-2|590 §9.2: Equivalent Definition of Homeomorphism]]

## Used in (Differentiable Manifolds)
- [[§36 Embeddings#^prop-36-2|Proposition §36.2: Immersions That Are Open onto Their Images]]
- [[§36 Embeddings#^cor-36-3|Corollary §36.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§36 Embeddings#^prop-36-7|Proposition §36.7: Images of Embeddings Are Locally Closed]]
- [[§36 Embeddings#^cor-36-8|Corollary §36.8: Dense Submanifolds Are Open]]
- [[§36 Embeddings#^prop-36-11|Proposition §36.11: The Irrational Line on the Torus]]
- [[§38 SU(2) → SO(3)꞉ The Double Cover#^prop-38-5|Proposition §38.5: S³ Is SU(2)]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§36 Embeddings#^cor-36-3|§36.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§35 Immersions#^cor-35-2|§35.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the [[Torus|torus]] is an injective immersion with dense image ([[§36 Embeddings#^prop-36-11|Prop. §36.11]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§36 Embeddings#^rem-36-1|Where Is Injectivity Used?]]), which gives [[§36 Embeddings#^prop-36-2|§36.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§31 Local Diffeomorphisms#^ex-31-1|Ex. §31.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§33 Submanifolds#^def-33-1|Def. §33.1]]).
