---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 41.2", "smooth atlas of TM", "Lee Proposition 3.18"]
tags: [differentiable-manifolds, hub]
---
![[§44 The Tangent Bundle#^prop-44-2]]

## Treated in
- [[§44 The Tangent Bundle#^prop-44-2|Proposition §44.2: The Smooth Atlas of TM]], in [[§44 The Tangent Bundle]]

## Its proof uses
- [[§17 Differentiable Structures#^def-17-4|Definition §17.4: Smoothly Compatible Charts]]
- [[§17 Differentiable Structures#^def-17-6|Definition §17.6: Atlas]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]
- [[§44 The Tangent Bundle#^def-44-4|Definition §44.4: Local Trivializations of TM]]

## Its proof uses (other subjects)
- [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84 Change-of-basis formula]]

## Used in (Differentiable Manifolds)
- [[§44 The Tangent Bundle#^cor-44-3|Corollary §44.3: The Tangent Bundle Is a Fibration]]
- [[§44 The Tangent Bundle#^prop-44-4|Proposition §44.4: The Tangent Bundle Is a Manifold (Claim)]]
- [[§45 The Cotangent Bundle#^prop-45-2|Proposition §45.2: The Smooth Atlas of T^*M]]
- [[§47 Vector Fields#^prop-47-1|Proposition §47.1: Vector Fields in Coordinates]]

## Connections
- **Used for.** TM is a manifold of dimension 2m fibring over M with fibre ℝᵐ, with the zero section a submanifold ([[§44 The Tangent Bundle#^cor-44-3|§44.3]]); vector fields are its sections ([[§47 Vector Fields#^def-47-1|Def. §47.1]]). The same charts with dual bases make T*M a vector bundle ([[§45 The Cotangent Bundle#^prop-45-2|§45.2]]).
- **How the charts transform.** Over an overlap the base point moves by the transition map of M and the vector by its Jacobian, the change of coordinates of [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]; covector components move by the inverse transpose. These are the change-of-basis formula and the transpose matrix of a dual map ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]], [[§12 Duality#^ladr-3-132|LADR 3.132]]).
- **Locally a product.** The trivializations identify each TU with U × ℝᵐ, but a fibration need not be a global product, as the Möbius band shows ([[§36 Fibrations#^ex-36-2|Ex. §36.2]]). Unlike the Hopf fibration, which has no section ([[§39 Projective Spaces and the Hopf Fibration#^rem-39-1|Sections Need Not Exist]]), TM always has the zero section.
- **Coming later in the course.** Flows: a vector field is a section of TM ([[§47 Vector Fields#^def-47-1|Def. §47.1]]), and its integral curves will fit together into a flow on M.
