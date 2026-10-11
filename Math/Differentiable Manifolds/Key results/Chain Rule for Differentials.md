---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 28.6", "chain rule on manifolds", "pushforward functoriality", "Lee Proposition 3.6"]
tags: [differentiable-manifolds, hub]
---
![[§28 Derivations and the Abstract Tangent Space#^thm-28-6]]

## Treated in
- [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6: The Chain Rule]], in [[§28 Derivations and the Abstract Tangent Space]]

## Its proof uses
- [[§19 Smooth Functions and Smooth Maps#^lem-19-4|Lemma §19.4: Composition of Smooth Maps]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5: Pullback of Germs]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|Proposition §28.5: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]

## Used in (Differentiable Manifolds)
- [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|Corollary §28.7: Diffeomorphisms Induce Isomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-9|Corollary §29.9: Smooth Invariance of Dimension]]
- [[§30 The Differential in Coordinates#^cor-30-3|Corollary §30.3: The Chain Rule in Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4: Change of Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-9|Corollary §30.9: Regular Level Sets Are Topological Manifolds]]
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3: Velocity of a Composite — Computing Differentials by Curves]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§35 Local Diffeomorphisms#^thm-35-2|Theorem §35.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§36 Submersions#^ex-36-2|Example §36.2: Projections of Product Manifolds Are Submersions]]
- [[§37 Regular Submanifolds#^thm-37-9|Theorem §37.9: The Regular Value Theorem for Manifolds]]
- [[§38 Fibrations#^prop-38-1|Proposition §38.1: Fibres and Fibrations]]
- [[§38 Fibrations#^ex-38-2|Example §38.2: A Submersion That Is Not a Fibration]]
- [[§39 Immersions#^ex-39-1|Example §39.1: An Immersion That Crosses Itself]]
- [[§40 Embeddings#^cor-40-3|Corollary §40.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§40 Embeddings#^prop-40-11|Proposition §40.11: The Irrational Line on the Torus]]
- [[§40 Embeddings#^prop-40-12|Proposition §40.12: Images of Injective Immersions]]
- [[§43 The Unit Quaternions and SU(2)#^prop-43-5|Proposition §43.5: S³ Is SU(2)]]
- [[§44 SU(2) → SO(3)꞉ The Double Cover#^lem-44-3|Lemma §44.3: Translating the Differential]]
- [[§44 SU(2) → SO(3)꞉ The Double Cover#^thm-44-4|Theorem §44.4: The Double Cover SU(2) → SO(3)]]
- [[§54 Lie Groups and Left-Invariant Vector Fields#^ex-54-1|Example §54.1: Left-Invariant Fields on GL(n,ℝ)]]
- [[§54 Lie Groups and Left-Invariant Vector Fields#^thm-54-5|Theorem §54.5: The Lie Algebra Is the Tangent Space at the Identity]]

## Connections
- **Used for.** Diffeomorphisms induce isomorphisms of tangent spaces ([[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]), so a chart identifies T_pM with a tangent space of an open subset of ℝⁿ ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]); this is how the [[Basis Theorem for Tangent Spaces]] is proved. It also gives the chain rule and the change of coordinates in matrices ([[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), differentials computed by curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]) and the [[Local Diffeomorphism Criterion]].
- **Why the proof is one line.** Pulling back germs reverses the order, (G ∘ F)* = F* ∘ G*. The differential is the dual of pullback, so it composes in the same order as the maps, as dual maps do in linear algebra, (ST)′ = T′S′ ([[§12 Duality#^ladr-3-120|LADR 3.120]]).
- **Same idea elsewhere.** In coordinates it is the [[Multivariable Chain Rule]] of 452: the Jacobian of a composite is the product of the Jacobians ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). In 590, induced homomorphisms on π₁ compose the same way ([[Functoriality of π₁]]). Together with the basis theorem it shows that diffeomorphic manifolds have the same dimension, the easy smooth counterpart of [[Topological Invariance of Dimension]].
- **Pullbacks of covectors.** Dually, covectors pull back along smooth maps by the dual map of F_*p ([[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]]), one-forms pointwise ([[§49 One-Forms#^def-49-4|Def. §49.4]]), with the same reversal of order, (G ∘ F)* = F* ∘ G*; pullback commutes with d ([[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§49 One-Forms#^cor-49-4|§49.4]]). Higher-degree forms are still to come; on open subsets of ℝⁿ they and their pullbacks are in 452 ([[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]]).
