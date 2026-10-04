---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 23.6", "chain rule on manifolds", "pushforward functoriality", "Lee Proposition 3.6"]
tags: [differentiable-manifolds, hub]
---
![[§23 Derivations and the Abstract Tangent Space#^thm-23-6]]

## Treated in
- [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|Theorem §23.6: The Chain Rule]], in [[§23 Derivations and the Abstract Tangent Space]]

## Its proof uses
- [[§23 Derivations and the Abstract Tangent Space#^def-23-4|Definition §23.4: Pullback of Germs]]
- [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Definition §23.5: Pushforward — the Differential]]

## Used in (Differentiable Manifolds)
- [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|Corollary §23.7: Diffeomorphisms Induce Isomorphisms]]
- [[§24 Coordinate Derivations and the Basis Theorem#^cor-24-9|Corollary §24.9: Smooth Invariance of Dimension]]
- [[§25 The Differential in Coordinates#^cor-25-3|Corollary §25.3: The Chain Rule in Coordinates]]
- [[§25 The Differential in Coordinates#^cor-25-4|Corollary §25.4: Change of Coordinates]]
- [[§26 Tangent Vectors as Velocities of Curves#^cor-26-3|Corollary §26.3: Velocity of a Composite — Computing Differentials by Curves]]
- [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|Theorem §26.4: The Tangent Space of a Product]]
- [[§28 Local Diffeomorphisms#^thm-28-2|Theorem §28.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§30 Submanifolds#^thm-30-6|Theorem §30.6: The Regular Value Theorem for Manifolds]]
- [[§31 Fibrations#^prop-31-1|Proposition §31.1: Fibres and Fibrations]]
- [[§34 Embeddings#^cor-34-3|Corollary §34.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§34 Embeddings#^prop-34-11|Proposition §34.11: The Irrational Line on the Torus]]
- [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^lem-35-7|Lemma §35.7: Translating the Differential]]
- [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-35-8|Theorem §35.8: The Double Cover SU(2) → SO(3)]]

## Connections
- **Used for.** Diffeomorphisms induce isomorphisms of tangent spaces ([[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]]), so a chart identifies T_pM with a tangent space of an open subset of ℝⁿ ([[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]); this is how the [[Basis Theorem for Tangent Spaces]] is proved. It also gives the chain rule and the change of coordinates in matrices ([[§25 The Differential in Coordinates#^cor-25-3|§25.3]], [[§25 The Differential in Coordinates#^cor-25-4|§25.4]]), differentials computed by curves ([[§26 Tangent Vectors as Velocities of Curves#^cor-26-3|§26.3]]) and the [[Local Diffeomorphism Criterion]].
- **Why the proof is one line.** Pulling back germs reverses the order, (G ∘ F)* = F* ∘ G*. The differential is the dual of pullback, so it composes in the same order as the maps, as dual maps do in linear algebra, (ST)′ = T′S′ ([[§12 Duality#^ladr-3-120|LADR 3.120]]).
- **Same idea elsewhere.** In coordinates it is the [[Multivariable Chain Rule]] of 452: the Jacobian of a composite is the product of the Jacobians ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). In 590, induced homomorphisms on π₁ compose the same way ([[Functoriality of π₁]]). Together with the basis theorem it shows that diffeomorphic manifolds have the same dimension, the easy smooth counterpart of [[Topological Invariance of Dimension]].
- **Coming later in the course.** Differential forms pull back along smooth maps with the same reversal of order, (G ∘ F)* = F* ∘ G*.
