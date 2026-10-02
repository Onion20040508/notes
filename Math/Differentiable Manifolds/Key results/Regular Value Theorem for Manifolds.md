---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 29.6", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§29 Submanifolds#^thm-29-6]]

## Treated in
- [[§29 Submanifolds#^thm-29-6|Theorem §29.6: The Regular Value Theorem for Manifolds]], in [[§29 Submanifolds]]

## Its proof uses
- [[§17 Linear Algebra Toolkit#^prop-17-1|Proposition §17.1: Standing Facts from Linear Algebra]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|Theorem §20.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|Theorem §23.6: The Chain Rule]]
- [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|Theorem §26.4: The Tangent Space of a Product]]
- [[§28 Local Diffeomorphisms and Submersions#^def-28-3|Definition §28.3: Regular Points and Critical Points]]
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-7|Theorem §28.7: Local Normal Form for Submersions]]
- [[§29 Submanifolds#^prop-29-1|Proposition §29.1: Two Observations on Adapted Charts]]
- [[§29 Submanifolds#^def-29-1|Definition §29.1: Submanifold and Adapted Charts]]
- [[§29 Submanifolds#^prop-29-4|Proposition §29.4: Tangent Spaces of a Submanifold]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§29 Submanifolds#^cor-29-7|Corollary §29.7: Fibres of Submersions Are Submanifolds]]
- [[§29 Submanifolds#^prop-29-8|Proposition §29.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§29 Submanifolds#^cor-29-7|§29.7]]), in particular every fibre of a fibration ([[§30 Fibrations#^prop-30-2|§30.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§29 Submanifolds#^prop-29-8|§29.8]], [[§29 Submanifolds#^rem-29-2|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§30 Fibrations#^ex-30-2|Ex. §30.2]]). Even all fibres diffeomorphic does not make a fibration ([[§30 Fibrations#^ex-30-4|Ex. §30.4]]), unless the map is also proper and the base connected ([[§30 Fibrations#^thm-30-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§29 Submanifolds#^prop-29-5|§29.5]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
