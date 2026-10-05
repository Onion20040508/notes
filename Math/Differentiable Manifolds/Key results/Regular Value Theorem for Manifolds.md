---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 33.6", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§33 Submanifolds#^thm-33-6]]

## Treated in
- [[§33 Submanifolds#^thm-33-6|Theorem §33.6: The Regular Value Theorem for Manifolds]], in [[§33 Submanifolds]]

## Its proof uses
- [[§20 Linear Algebra Toolkit#^prop-20-1|Proposition §20.1: Standing Facts from Linear Algebra]]
- [[§23 The Geometric Tangent Space#^thm-23-3|Theorem §23.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|Theorem §26.6: The Chain Rule]]
- [[§29 Tangent Vectors as Velocities of Curves#^thm-29-4|Theorem §29.4: The Tangent Space of a Product]]
- [[§32 Submersions#^def-32-2|Definition §32.2: Regular Points and Critical Points]]
- [[§32 Submersions#^thm-32-4|Theorem §32.4: Local Normal Form for Submersions]]
- [[§33 Submanifolds#^prop-33-1|Proposition §33.1: Two Observations on Adapted Charts]]
- [[§33 Submanifolds#^def-33-1|Definition §33.1: Submanifold and Adapted Charts]]
- [[§33 Submanifolds#^prop-33-4|Proposition §33.4: Tangent Spaces of a Submanifold]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§33 Submanifolds#^cor-33-7|Corollary §33.7: Fibres of Submersions Are Submanifolds]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]
- [[§38 SU(2) → SO(3)꞉ The Double Cover#^prop-38-4|Proposition §38.4: The Unit Quaternions]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§33 Submanifolds#^cor-33-7|§33.7]]), in particular every fibre of a fibration ([[§34 Fibrations#^prop-34-2|§34.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§33 Submanifolds#^prop-33-8|§33.8]], [[§33 Submanifolds#^rem-33-2|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§34 Fibrations#^ex-34-1|Ex. §34.1]]). Even all fibres diffeomorphic does not make a fibration ([[§34 Fibrations#^ex-34-3|Ex. §34.3]]), unless the map is also proper and the base connected ([[§34 Fibrations#^thm-34-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§33 Submanifolds#^prop-33-5|§33.5]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
