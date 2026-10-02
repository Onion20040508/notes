---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 30.6", "Lee Corollary 5.14", "Lee Proposition 5.38"]
tags: [differentiable-manifolds, hub]
---
![[§30 Submanifolds#^thm-30-6]]

## Treated in
- [[§30 Submanifolds#^thm-30-6|Theorem §30.6: The Regular Value Theorem for Manifolds]], in [[§30 Submanifolds]]

## Its proof uses
- [[§17 Linear Algebra Toolkit#^prop-17-1|Proposition §17.1: Standing Facts from Linear Algebra]]
- [[§20 Tangent Spaces I꞉ The Geometric Picture#^thm-20-3|Theorem §20.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|Theorem §23.6: The Chain Rule]]
- [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|Theorem §26.4: The Tangent Space of a Product]]
- [[§29 Submersions#^def-29-2|Definition §29.2: Regular Points and Critical Points]]
- [[§29 Submersions#^thm-29-4|Theorem §29.4: Local Normal Form for Submersions]]
- [[§30 Submanifolds#^def-30-1|Definition §30.1: Submanifold and Adapted Charts]]
- [[§30 Submanifolds#^prop-30-1|Proposition §30.1: Two Observations on Adapted Charts]]
- [[§30 Submanifolds#^prop-30-4|Proposition §30.4: Tangent Spaces of a Submanifold]]

## Its proof uses (other subjects)
- [[Fundamental theorem of linear maps]] (Linear Algebra)

## Used in (Differentiable Manifolds)
- [[§30 Submanifolds#^cor-30-7|Corollary §30.7: Fibres of Submersions Are Submanifolds]]
- [[§30 Submanifolds#^prop-30-8|Proposition §30.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Every fibre of a submersion is a submanifold ([[§30 Submanifolds#^cor-30-7|§30.7]]), in particular every fibre of a fibration ([[§31 Fibrations#^prop-31-2|§31.2]]). It contains the Euclidean versions, with the same smooth structure and tangent spaces ([[§30 Submanifolds#^prop-30-8|§30.8]], [[§30 Submanifolds#^rem-30-2|The Regular Value Theorems — Old and New]]).
- **Proof, and its limits.** Near each point of the level set F is a projection, by the [[Submersion Normal Form]], so the level set is a coordinate slice. Fibres of a submersion can still change type: (x, y) ↦ x on ℝ² ∖ {(0, 1)} has one broken fibre ([[§31 Fibrations#^ex-31-2|Ex. §31.2]]). Even all fibres diffeomorphic does not make a fibration ([[§31 Fibrations#^ex-31-4|Ex. §31.4]]), unless the map is also proper and the base connected ([[§31 Fibrations#^thm-31-3|Ehresmann]]).
- **Same idea elsewhere.** ι_*(T_pS) = ker F_*p generalizes [[Geometric Tangent Space Is the Kernel of the Jacobian]], and dim S = m − n is rank–nullity ([[Fundamental theorem of linear maps]]). The conormal space, of dimension the codimension ([[§30 Submanifolds#^prop-30-5|§30.5]]), is LADR's annihilator ([[§12 Duality#^ladr-3-121|LADR 3.121]], [[§12 Duality#^ladr-3-125|LADR 3.125]]).
- **Coming later in the course.** Transversality on manifolds: the preimage of a submanifold under a transverse map is a submanifold of the same codimension, and this theorem is the case of a point. Sard's theorem makes regular values, and transversality, generic.
