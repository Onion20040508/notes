---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 37.12", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§37 Regular Submanifolds#^thm-37-12]]

## Treated in
- [[§37 Regular Submanifolds#^thm-37-12|Theorem §37.12: The Regular Value Theorem for Manifolds]], in [[§37 Regular Submanifolds]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|Lemma §28.10: The Pushforward Along a Constant Map]]
- [[§36 Submersions#^thm-36-6|Theorem §36.6: Local Normal Form for Submersions]]
- [[§37 Regular Submanifolds#^prop-37-2|Proposition §37.2: Two Observations on Adapted Charts]]
- [[§37 Regular Submanifolds#^prop-37-3|Proposition §37.3: The Induced Smooth Structure]]
- [[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6: Tangent Spaces of a Regular Submanifold]]
- [[§37 Regular Submanifolds#^lem-37-11|Lemma §37.11: Level Sets Near a Regular Point]]

## Used in (Differentiable Manifolds)
- [[§37 Regular Submanifolds#^cor-37-13|Corollary §37.13: Fibres of Submersions Are Regular Submanifolds]]
- [[§37 Regular Submanifolds#^prop-37-14|Proposition §37.14: The Old and New Versions Agree]]
- [[§37 Regular Submanifolds#^thm-37-15|Theorem §37.15: Preimages of Transverse Submanifolds]]
- [[§37 Regular Submanifolds#^prop-37-19|Proposition §37.19: The Conormal Space of a Regular Level Set]]
- [[§37 Regular Submanifolds#^thm-37-20|Theorem §37.20: Lagrange Multipliers]]
- [[§40 The Normal Bundle of a Submanifold of Euclidean Space#^prop-40-1|Proposition §40.1: The Normal Bundle Is a Submanifold]]
- [[§45 The Unit Quaternions and SU(2)#^prop-45-4|Proposition §45.4: The Unit Quaternions]]
- [[§46 SU(2) → SO(3)꞉ The Double Cover#^prop-46-1|Proposition §46.1: Conjugation by Unit Quaternions Is Rotation]]
- [[§59 Sard's Theorem#^thm-59-1|Theorem §59.1: Sard's Theorem]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§37 Regular Submanifolds#^cor-37-13|§37.13]]), in particular every fibre of a fibration ([[§38 Fibrations#^prop-38-2|§38.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§37 Regular Submanifolds#^prop-37-14|§37.14]], [[§37 Regular Submanifolds#^rem-37-3|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§38 Fibrations#^ex-38-1|Ex. §38.1]]). Even all fibres diffeomorphic does not make a fibration ([[§38 Fibrations#^ex-38-2|Ex. §38.2]]), unless the map is also proper and the base connected ([[§38 Fibrations#^thm-38-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§37 Regular Submanifolds#^prop-37-8|§37.8]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
