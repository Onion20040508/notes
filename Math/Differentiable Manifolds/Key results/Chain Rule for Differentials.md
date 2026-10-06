---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 26.6", "chain rule on manifolds", "pushforward functoriality", "Lee Proposition 3.6"]
tags: [differentiable-manifolds, hub]
---
![[§28 Derivations and the Abstract Tangent Space#^thm-28-6]]

## Treated in
- [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6: The Chain Rule]], in [[§28 Derivations and the Abstract Tangent Space]]

## Its proof uses
- [[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5: Pullback of Germs]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]

## Used in (Differentiable Manifolds)
- [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|Corollary §28.7: Diffeomorphisms Induce Isomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-9|Corollary §29.9: Smooth Invariance of Dimension]]
- [[§30 The Differential in Coordinates#^cor-30-3|Corollary §30.3: The Chain Rule in Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4: Change of Coordinates]]
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3: Velocity of a Composite — Computing Differentials by Curves]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§33 Local Diffeomorphisms#^thm-33-2|Theorem §33.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§35 Submanifolds#^thm-35-6|Theorem §35.6: The Regular Value Theorem for Manifolds]]
- [[§36 Fibrations#^prop-36-1|Proposition §36.1: Fibres and Fibrations]]
- [[§38 Embeddings#^cor-38-3|Corollary §38.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§38 Embeddings#^prop-38-11|Proposition §38.11: The Irrational Line on the Torus]]
- [[§40 The Unit Quaternions and SU(2)#^prop-40-5|Proposition §40.5: S³ Is SU(2)]]
- [[§41 SU(2) → SO(3)꞉ The Double Cover#^lem-41-3|Lemma §41.3: Translating the Differential]]
- [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4: The Double Cover SU(2) → SO(3)]]

## Connections
- **Used for.** Diffeomorphisms induce isomorphisms of tangent spaces ([[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]), so a chart identifies T_pM with a tangent space of an open subset of ℝⁿ ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]); this is how the [[Basis Theorem for Tangent Spaces]] is proved. It also gives the chain rule and the change of coordinates in matrices ([[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), differentials computed by curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]) and the [[Local Diffeomorphism Criterion]].
- **Why the proof is one line.** Pulling back germs reverses the order, (G ∘ F)* = F* ∘ G*. The differential is the dual of pullback, so it composes in the same order as the maps, as dual maps do in linear algebra, (ST)′ = T′S′ ([[§12 Duality#^ladr-3-120|LADR 3.120]]).
- **Same idea elsewhere.** In coordinates it is the [[Multivariable Chain Rule]] of 452: the Jacobian of a composite is the product of the Jacobians ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). In 590, induced homomorphisms on π₁ compose the same way ([[Functoriality of π₁]]). Together with the basis theorem it shows that diffeomorphic manifolds have the same dimension, the easy smooth counterpart of [[Topological Invariance of Dimension]].
- **Pullbacks of covectors.** Dually, covectors pull back along smooth maps by the dual map of F_*p ([[§32 The Cotangent Space#^def-32-5|Def. §32.5]]), one-forms pointwise ([[§46 One-Forms#^def-46-4|Def. §46.4]]), with the same reversal of order, (G ∘ F)* = F* ∘ G*; pullback commutes with d ([[§32 The Cotangent Space#^prop-32-10|§32.10]], [[§46 One-Forms#^cor-46-4|§46.4]]). Higher-degree forms are still to come; on open subsets of ℝⁿ they and their pullbacks are in 452 ([[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]]).
