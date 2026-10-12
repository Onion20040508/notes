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
- [[§19 Smooth Functions and Smooth Maps#^lem-19-5|Lemma §19.5: Composition of Smooth Maps]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-5|Definition §28.5: Pullback of Germs]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|Proposition §28.5: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]

## Used in (Differentiable Manifolds)
- [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|Corollary §28.7: Diffeomorphisms Induce Isomorphisms]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|Lemma §28.10: The Pushforward Along a Constant Map]]
- [[§29 Coordinate Derivations and the Basis Theorem#^cor-29-10|Corollary §29.10: Smooth Invariance of Dimension]]
- [[§30 The Differential in Coordinates#^cor-30-3|Corollary §30.3: The Chain Rule in Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4: Change of Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-9|Corollary §30.9: Regular Level Sets Are Topological Manifolds]]
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3: Velocity of a Composite — Computing Differentials by Curves]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§35 Local Diffeomorphisms#^thm-35-2|Theorem §35.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§36 Submersions#^ex-36-2|Example §36.2: Projections of Product Manifolds Are Submersions]]
- [[§37 Regular Submanifolds#^lem-37-11|Lemma §37.11: Level Sets Near a Regular Point]]
- [[§37 Regular Submanifolds#^thm-37-15|Theorem §37.15: Preimages of Transverse Submanifolds]]
- [[§37 Regular Submanifolds#^cor-37-17|Corollary §37.17: Special Cases of Transversality]]
- [[§38 Fibrations#^ex-38-1|Example §38.1: A Submersion That Is Not a Fibration]]
- [[§38 Fibrations#^prop-38-1|Proposition §38.1: Fibres and Fibrations]]
- [[§38 Fibrations#^prop-38-5|Proposition §38.5: Splitting Along a Section]]
- [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^ex-40-1|Example §40.1: Focal Points of the Parabola]]
- [[§41 Immersions#^ex-41-1|Example §41.1: An Immersion That Crosses Itself]]
- [[§42 Embeddings#^cor-42-3|Corollary §42.3: An Embedding Is a Diffeomorphism onto Its Image]]
- [[§42 Embeddings#^prop-42-12|Proposition §42.12: The Irrational Line on the Torus]]
- [[§42 Embeddings#^prop-42-13|Proposition §42.13: Images of Injective Immersions]]
- [[§45 The Unit Quaternions and SU(2)#^prop-45-5|Proposition §45.5: S³ Is SU(2)]]
- [[§46 SU(2) → SO(3)꞉ The Double Cover#^lem-46-3|Lemma §46.3: Translating the Differential]]
- [[§46 SU(2) → SO(3)꞉ The Double Cover#^thm-46-4|Theorem §46.4: The Double Cover SU(2) → SO(3)]]
- [[§57 Lie Groups and Left-Invariant Vector Fields#^ex-57-1|Example §57.1: Left-Invariant Fields on GL(n,ℝ)]]
- [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-5|Lemma §57.5: The Left-Invariant Extension Is Left-Invariant]]
- [[§57 Lie Groups and Left-Invariant Vector Fields#^lem-57-9|Lemma §57.9: Left-Invariant Fields Related by a Morphism]]

## Connections
- **Used for.** Diffeomorphisms induce isomorphisms of tangent spaces ([[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]), so a chart identifies T_pM with a tangent space of an open subset of ℝⁿ ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]); this is how the [[Basis Theorem for Tangent Spaces]] is proved. It also gives the chain rule and the change of coordinates in matrices ([[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), differentials computed by curves ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]) and the [[Local Diffeomorphism Criterion]].
- **Why the proof is one line.** Pulling back germs reverses the order, (G ∘ F)* = F* ∘ G*. The differential is the dual of pullback, so it composes in the same order as the maps, as dual maps do in linear algebra, (ST)′ = T′S′ ([[§12 Duality#^ladr-3-120|LADR 3.120]]).
- **Same idea elsewhere.** In coordinates it is the [[Multivariable Chain Rule]] of 452: the Jacobian of a composite is the product of the Jacobians ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). In 590, induced homomorphisms on π₁ compose the same way ([[Functoriality of π₁]]). Together with the basis theorem it shows that diffeomorphic manifolds have the same dimension, the easy smooth counterpart of [[Topological Invariance of Dimension]].
- **Pullbacks of covectors.** Dually, covectors pull back along smooth maps by the dual map of F_*p ([[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]]), one-forms pointwise ([[§51 One-Forms#^def-51-4|Def. §51.4]]), with the same reversal of order, (G ∘ F)* = F* ∘ G*; pullback commutes with d ([[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§51 One-Forms#^cor-51-4|§51.4]]). Higher-degree forms are still to come; on open subsets of ℝⁿ they and their pullbacks are in 452 ([[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]]).
