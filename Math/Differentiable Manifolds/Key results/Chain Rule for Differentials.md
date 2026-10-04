---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 26.6", "chain rule on manifolds", "pushforward functoriality", "Lee Proposition 3.6"]
tags: [differentiable-manifolds, hub]
---
![[§26 Derivations and the Abstract Tangent Space#^thm-26-6]]

## Treated in
- [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|Theorem §26.6: The Chain Rule]], in [[§26 Derivations and the Abstract Tangent Space]]

## Its proof uses
- [[§26 Derivations and the Abstract Tangent Space#^def-26-4|Definition §26.4: Pullback of Germs]]
- [[§26 Derivations and the Abstract Tangent Space#^def-26-5|Definition §26.5: Pushforward — the Differential]]

## Used in (Differentiable Manifolds)
- [[§26 Derivations and the Abstract Tangent Space#^cor-26-7|Corollary §26.7: Diffeomorphisms Induce Isomorphisms]]
- [[§27 Coordinate Derivations and the Basis Theorem#^cor-27-9|Corollary §27.9: Smooth Invariance of Dimension]]
- [[§28 The Differential in Coordinates#^cor-28-3|Corollary §28.3: The Chain Rule in Coordinates]]
- [[§28 The Differential in Coordinates#^cor-28-4|Corollary §28.4: Change of Coordinates]]
- [[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|Corollary §29.3: Velocity of a Composite — Computing Differentials by Curves]]
- [[§29 Tangent Vectors as Velocities of Curves#^thm-29-4|Theorem §29.4: The Tangent Space of a Product]]
- [[§31 Local Diffeomorphisms#^thm-31-2|Theorem §31.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§33 Submanifolds#^thm-33-6|Theorem §33.6: The Regular Value Theorem for Manifolds]]
- [[§34 Fibrations#^prop-34-1|Proposition §34.1: Fibres and Fibrations]]
- [[§37 Embeddings#^cor-37-3|Corollary §37.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§37 Embeddings#^prop-37-11|Proposition §37.11: The Irrational Line on the Torus]]
- [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^prop-39-5|Proposition §39.5: S³ Is SU(2)]]
- [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-39-9|Lemma §39.9: Translating the Differential]]
- [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-10|Theorem §39.10: The Double Cover SU(2) → SO(3)]]

## Connections
- **Used for.** Diffeomorphisms induce isomorphisms of tangent spaces ([[§26 Derivations and the Abstract Tangent Space#^cor-26-7|§26.7]]), so a chart identifies T_pM with a tangent space of an open subset of ℝⁿ ([[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]); this is how the [[Basis Theorem for Tangent Spaces]] is proved. It also gives the chain rule and the change of coordinates in matrices ([[§28 The Differential in Coordinates#^cor-28-3|§28.3]], [[§28 The Differential in Coordinates#^cor-28-4|§28.4]]), differentials computed by curves ([[§29 Tangent Vectors as Velocities of Curves#^cor-29-3|§29.3]]) and the [[Local Diffeomorphism Criterion]].
- **Why the proof is one line.** Pulling back germs reverses the order, (G ∘ F)* = F* ∘ G*. The differential is the dual of pullback, so it composes in the same order as the maps, as dual maps do in linear algebra, (ST)′ = T′S′ ([[§12 Duality#^ladr-3-120|LADR 3.120]]).
- **Same idea elsewhere.** In coordinates it is the [[Multivariable Chain Rule]] of 452: the Jacobian of a composite is the product of the Jacobians ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). In 590, induced homomorphisms on π₁ compose the same way ([[Functoriality of π₁]]). Together with the basis theorem it shows that diffeomorphic manifolds have the same dimension, the easy smooth counterpart of [[Topological Invariance of Dimension]].
- **Coming later in the course.** Differential forms pull back along smooth maps with the same reversal of order, (G ∘ F)* = F* ∘ G*.
