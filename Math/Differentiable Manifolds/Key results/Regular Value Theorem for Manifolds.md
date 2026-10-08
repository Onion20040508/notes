---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 35.7", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§35 Submanifolds#^thm-35-7]]

## Treated in
- [[§35 Submanifolds#^thm-35-7|Theorem §35.7: The Regular Value Theorem for Manifolds]], in [[§35 Submanifolds]]

## Its proof uses
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6: The Chain Rule]]
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: The Tangent Space of a Product]]
- [[§34 Submersions#^def-34-3|Definition §34.3: Regular Points and Critical Points]]
- [[§34 Submersions#^def-34-4|Definition §34.4: Regular Values and Critical Values]]
- [[§34 Submersions#^thm-34-4|Theorem §34.4: Local Normal Form for Submersions]]
- [[§35 Submanifolds#^def-35-1|Definition §35.1: Submanifold]]
- [[§35 Submanifolds#^prop-35-1|Proposition §35.1: Two Observations on Adapted Charts]]
- [[§35 Submanifolds#^def-35-2|Definition §35.2: Adapted Chart]]
- [[§35 Submanifolds#^prop-35-4|Proposition §35.4: Tangent Spaces of a Submanifold]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§35 Submanifolds#^cor-35-8|Corollary §35.8: Fibres of Submersions Are Submanifolds]]
- [[§35 Submanifolds#^prop-35-9|Proposition §35.9: The Old and New Versions Agree]]
- [[§40 The Unit Quaternions and SU(2)#^prop-40-4|Proposition §40.4: The Unit Quaternions]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§35 Submanifolds#^cor-35-8|§35.8]]), in particular every fibre of a fibration ([[§36 Fibrations#^prop-36-2|§36.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§35 Submanifolds#^prop-35-9|§35.9]], [[§35 Submanifolds#^rem-35-3|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§36 Fibrations#^ex-36-1|Ex. §36.1]]). Even all fibres diffeomorphic does not make a fibration ([[§36 Fibrations#^ex-36-3|Ex. §36.3]]), unless the map is also proper and the base connected ([[§36 Fibrations#^thm-36-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§35 Submanifolds#^prop-35-5|§35.5]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
