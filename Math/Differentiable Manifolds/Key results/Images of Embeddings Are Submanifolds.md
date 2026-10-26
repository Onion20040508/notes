---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 44.1", "embedded submanifold", "Lee Proposition 5.2"]
tags: [differentiable-manifolds, hub]
---
![[§44 Embeddings#^thm-44-1]]

## Treated in
- [[§44 Embeddings#^thm-44-1|Theorem §44.1: The Image of an Embedding Is a Regular Submanifold]], in [[§44 Embeddings]]

## Its proof uses
- [[§1 Point-Set Topology Review#^prop-1-5|Proposition §1.5: Continuity and Homeomorphisms]]
- [[§3 Subspaces and Products#^def-3-1|Definition §3.1: Subspace Topology]]
- [[§17 Differentiable Structures#^lem-17-6|Lemma §17.6: Restricting and Recomposing Smooth Charts]]
- [[§37 Regular Submanifolds#^def-37-2|Definition §37.2: Regular Submanifold]]
- [[§37 Regular Submanifolds#^def-37-3|Definition §37.3: Adapted Chart]]
- [[§43 Immersions#^thm-43-1|Theorem §43.1: Local Normal Form for Immersions]]
- [[§43 Immersions#^cor-43-2|Corollary §43.2: The Local Image of an Immersion]]
- [[§44 Embeddings#^def-44-1|Definition §44.1: Embedding]]

## Used in (Differentiable Manifolds)
- [[§44 Embeddings#^prop-44-2|Proposition §44.2: Immersions That Are Open onto Their Images]]
- [[§44 Embeddings#^cor-44-3|Corollary §44.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§44 Embeddings#^prop-44-7|Proposition §44.7: Images of Embeddings Are Locally Closed]]
- [[§44 Embeddings#^cor-44-8|Corollary §44.8: Dense Regular Submanifolds Are Open]]
- [[§44 Embeddings#^prop-44-10|Proposition §44.10: Sections Are Closed Embeddings]]
- [[§44 Embeddings#^prop-44-15|Proposition §44.15: When an Immersed Submanifold Is Regular]]
- [[§47 The Unit Quaternions and SU(2)#^prop-47-5|Proposition §47.5: S³ Is SU(2)]]
- [[§65 The Whitney Embedding Theorem#^thm-65-4|Theorem §65.4: The Whitney Theorems for Compact Manifolds]]

## Connections
- **Used for.** An embedding is a diffeomorphism onto its image, with the induced smooth structure of the submanifold ([[§44 Embeddings#^cor-44-3|§44.3]]). Combined with [[Injective Proper Immersions Are Embeddings]], the image of an injective immersion of a compact manifold is a submanifold.
- **Why the topological condition.** The [[Immersion Normal Form]] only makes the image locally a submanifold, near F(p) for p in a small U ([[§43 Immersions#^cor-43-2|§43.2]]). Other parts of the image may come back into every neighbourhood: the irrational line on the [[Torus|torus]] is an injective immersion with dense image ([[§44 Embeddings#^prop-44-12|Prop. §44.12]]). Openness of F(U) in F(M) is what cuts those parts away.
- **Injectivity is not used.** The proof needs only that F be open onto its image ([[§44 Embeddings#^rem-44-1|Where Is Injectivity Used?]]), which gives [[§44 Embeddings#^prop-44-2|§44.2]]; the covering t ↦ (cos t, sin t) of S¹ is an example ([[§35 Local Diffeomorphisms#^ex-35-1|Ex. §35.1]]).
- **Same idea elsewhere.** The other main source of submanifolds is level sets, by the [[Regular Value Theorem for Manifolds]]. Both are checked against the same definition, a chart in which the subset is a coordinate slice ([[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]).
