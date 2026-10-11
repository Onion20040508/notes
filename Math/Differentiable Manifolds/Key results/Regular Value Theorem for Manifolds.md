---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 37.7", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§37 Regular Submanifolds#^thm-37-7]]

## Treated in
- [[§37 Regular Submanifolds#^thm-37-7|Theorem §37.7: The Regular Value Theorem for Manifolds]], in [[§37 Regular Submanifolds]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6: The Chain Rule]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Definition §29.1: Coordinate Functions of a Chart]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|Theorem §29.8: Dimension of the Tangent Space]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§36 Submersions#^def-36-3|Definition §36.3: Regular Points and Critical Points]]
- [[§36 Submersions#^def-36-4|Definition §36.4: Regular Values and Critical Values]]
- [[§36 Submersions#^thm-36-4|Theorem §36.4: Local Normal Form for Submersions]]
- [[§37 Regular Submanifolds#^def-37-1|Definition §37.1: Regular Submanifold]]
- [[§37 Regular Submanifolds#^prop-37-1|Proposition §37.1: Two Observations on Adapted Charts]]
- [[§37 Regular Submanifolds#^def-37-2|Definition §37.2: Adapted Chart]]
- [[§37 Regular Submanifolds#^prop-37-2|Proposition §37.2: The Induced Smooth Structure]]
- [[§37 Regular Submanifolds#^prop-37-4|Proposition §37.4: Tangent Spaces of a Regular Submanifold]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§37 Regular Submanifolds#^cor-37-8|Corollary §37.8: Fibres of Submersions Are Regular Submanifolds]]
- [[§37 Regular Submanifolds#^prop-37-9|Proposition §37.9: The Old and New Versions Agree]]
- [[§43 The Unit Quaternions and SU(2)#^prop-43-4|Proposition §43.4: The Unit Quaternions]]
- [[§44 SU(2) → SO(3)꞉ The Double Cover#^prop-44-1|Proposition §44.1: Conjugation by Unit Quaternions Is Rotation]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§37 Regular Submanifolds#^cor-37-8|§37.8]]), in particular every fibre of a fibration ([[§38 Fibrations#^prop-38-2|§38.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§37 Regular Submanifolds#^rem-37-3|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§38 Fibrations#^ex-38-1|Ex. §38.1]]). Even all fibres diffeomorphic does not make a fibration ([[§38 Fibrations#^ex-38-3|Ex. §38.3]]), unless the map is also proper and the base connected ([[§38 Fibrations#^thm-38-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§37 Regular Submanifolds#^prop-37-5|§37.5]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
