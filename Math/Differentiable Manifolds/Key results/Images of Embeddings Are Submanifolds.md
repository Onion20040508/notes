---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 34.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§34 Embeddings#^thm-34-1]]

## Treated in
- [[§34 Embeddings#^thm-34-1|Theorem §34.1: The Image of an Embedding Is a Submanifold]], in [[§34 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§30 Submanifolds#^def-30-1|Definition §30.1: Submanifold and Adapted Charts]]
- [[§33 Immersions#^thm-33-1|Theorem §33.1: Local Normal Form for Immersions]]
- [[§33 Immersions#^cor-33-2|Corollary §33.2: The Local Image of an Immersion]]
- [[§34 Embeddings#^rem-34-1|Remark: Where Is Injectivity Used?]]
- [[§34 Embeddings#^def-34-1|Definition §34.1: Embedding]]

## Its proof uses (other subjects)
- [[§9 Continuous Functions#^prop-9-2|590 §9.2: Equivalent Definition of Homeomorphism]]

## Used in (Differentiable Manifolds)
- [[§34 Embeddings#^prop-34-2|Proposition §34.2: Immersions That Are Open onto Their Images]]
- [[§34 Embeddings#^cor-34-3|Corollary §34.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§34 Embeddings#^prop-34-7|Proposition §34.7: Images of Embeddings Are Locally Closed]]
- [[§34 Embeddings#^cor-34-8|Corollary §34.8: Dense Submanifolds Are Open]]
- [[§34 Embeddings#^prop-34-11|Proposition §34.11: The Irrational Line on the Torus]]
- [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-35-3|Proposition §35.3: S³ Is SU(2)]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§34 Embeddings#^cor-34-3|§34.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§33 Immersions#^cor-33-2|§33.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the torus is an injective immersion with dense image ([[§34 Embeddings#^prop-34-11|Prop. §34.11]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§34 Embeddings#^rem-34-1|Where Is Injectivity Used?]]), which gives [[§34 Embeddings#^prop-34-2|§34.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§28 Local Diffeomorphisms#^ex-28-1|Ex. §28.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§30 Submanifolds#^def-30-1|Def. §30.1]]).
