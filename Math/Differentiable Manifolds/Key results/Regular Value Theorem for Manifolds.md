---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 15.6", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§15 Submanifolds#^thm-15-6]]

## Treated in
- [[§15 Submanifolds#^thm-15-6|Theorem §15.6: The Regular Value Theorem for Manifolds]], in [[§15 Submanifolds]]

## Its proof uses
- [[§10 Vector Spaces and Matrix Groups#^prop-10-1|Proposition §10.1: Standing Facts from Linear Algebra]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|Theorem §12.11: The Chain Rule]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|Theorem §12.32: The Tangent Space of a Product]]
- [[§14 Local Diffeomorphisms and Submersions#^def-14-3|Definition §14.3: Regular Points and Critical Points]]
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|Theorem §14.5: Local Normal Form for Submersions]]
- [[§15 Submanifolds#^def-15-1|Definition §15.1: Submanifold and Adapted Charts]]
- [[§15 Submanifolds#^prop-15-1|Proposition §15.1: Two Observations on Adapted Charts]]
- [[§15 Submanifolds#^prop-15-4|Proposition §15.4: Tangent Spaces of a Submanifold]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§15 Submanifolds#^cor-15-7|Corollary §15.7: Fibres of Submersions Are Submanifolds]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§15 Submanifolds#^cor-15-7|§15.7]]), in particular every fibre of a fibration ([[§16 Fibrations#^prop-16-2|§16.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§15 Submanifolds#^prop-15-8|§15.8]], [[§15 Submanifolds#^rem-15-2|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§16 Fibrations#^ex-16-2|Ex. §16.2]]). Even all fibres diffeomorphic does not make a fibration ([[§16 Fibrations#^ex-16-4|Ex. §16.4]]), unless the map is also proper and the base connected ([[§16 Fibrations#^thm-16-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§15 Submanifolds#^prop-15-5|§15.5]]), is LADR's annihilator ([[3F Duality#^ladr-3-121|LADR 3.121]], [[3F Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
