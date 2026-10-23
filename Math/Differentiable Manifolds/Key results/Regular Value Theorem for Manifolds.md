---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 38.2", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§38 The Regular Value Theorem for Manifolds#^thm-38-2]]

## Treated in
- [[§38 The Regular Value Theorem for Manifolds#^thm-38-2|Theorem §38.2: The Regular Value Theorem for Manifolds]], in [[§38 The Regular Value Theorem for Manifolds]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|Lemma §28.10: The Pushforward Along a Constant Map]]
- [[§36 Submersions#^thm-36-6|Theorem §36.6: Local Normal Form for Submersions]]
- [[§37 Regular Submanifolds#^prop-37-2|Proposition §37.2: Two Observations on Adapted Charts]]
- [[§37 Regular Submanifolds#^prop-37-3|Proposition §37.3: The Induced Smooth Structure]]
- [[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6: Tangent Spaces of a Regular Submanifold]]
- [[§38 The Regular Value Theorem for Manifolds#^lem-38-1|Lemma §38.1: Level Sets Near a Regular Point]]

## Used in (Differentiable Manifolds)
- [[§38 The Regular Value Theorem for Manifolds#^cor-38-3|Corollary §38.3: Fibres of Submersions Are Regular Submanifolds]]
- [[§38 The Regular Value Theorem for Manifolds#^prop-38-4|Proposition §38.4: The Old and New Versions Agree]]
- [[§39 Transversality and Lagrange Multipliers#^thm-39-1|Theorem §39.1: Preimages of Transverse Submanifolds]]
- [[§39 Transversality and Lagrange Multipliers#^prop-39-5|Proposition §39.5: The Conormal Space of a Regular Level Set]]
- [[§39 Transversality and Lagrange Multipliers#^thm-39-6|Theorem §39.6: Lagrange Multipliers]]
- [[§39 Transversality and Lagrange Multipliers#^thm-39-8|Theorem §39.8: Transverse Intersections in a Manifold]]
- [[§42 The Normal Bundle of a Submanifold of Euclidean Space#^prop-42-1|Proposition §42.1: The Normal Bundle Is a Submanifold]]
- [[§47 The Unit Quaternions and SU(2)#^prop-47-4|Proposition §47.4: The Unit Quaternions]]
- [[§48 SU(2) → SO(3)꞉ The Double Cover#^prop-48-1|Proposition §48.1: Conjugation by Unit Quaternions Is Rotation]]
- [[§63 Sard's Theorem#^thm-63-3|Theorem §63.3: Sard's Theorem]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§38 The Regular Value Theorem for Manifolds#^cor-38-3|§38.3]]), in particular every fibre of a fibration ([[§40 Fibrations#^prop-40-2|§40.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§38 The Regular Value Theorem for Manifolds#^prop-38-4|§38.4]], [[§38 The Regular Value Theorem for Manifolds#^rem-38-1|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§40 Fibrations#^ex-40-1|Ex. §40.1]]). Even all fibres diffeomorphic does not make a fibration ([[§40 Fibrations#^ex-40-2|Ex. §40.2]]), unless the map is also proper and the base connected ([[§40 Fibrations#^thm-40-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§37 Regular Submanifolds#^prop-37-8|§37.8]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
