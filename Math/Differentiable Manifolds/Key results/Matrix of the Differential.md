---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 28.2", "Jacobian of the coordinate representation"]
tags: [differentiable-manifolds, hub]
---
![[§28 The Differential in Coordinates#^thm-28-2]]

## Treated in
- [[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2: The Matrix of the Differential]], in [[§28 The Differential in Coordinates]]

## Its proof uses
- [[§26 Derivations and the Abstract Tangent Space#^def-26-5|Definition §26.5: Pushforward — the Differential]]
- [[§26 Derivations and the Abstract Tangent Space#^prop-26-5|Proposition §26.5: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|Theorem §27.5: Basis Theorem]]
- [[§28 The Differential in Coordinates#^prop-28-1|Proposition §28.1: Partial Derivatives Upstairs and Downstairs]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-31|LADR 3.31 Matrix of a linear map, M(T)]]

## Used in (Differentiable Manifolds)
- [[§28 The Differential in Coordinates#^cor-28-3|Corollary §28.3: The Chain Rule in Coordinates]]
- [[§28 The Differential in Coordinates#^cor-28-4|Corollary §28.4: Change of Coordinates]]
- [[§28 The Differential in Coordinates#^prop-28-5|Proposition §28.5: Agreement with the Vector-Space Differential]]
- [[§28 The Differential in Coordinates#^prop-28-7|Proposition §28.7: Regular Values Inside One Chart]]
- [[§28 The Differential in Coordinates#^prop-28-9|Proposition §28.9: Maps with Zero Differential Are Constant]]
- [[§29 Tangent Vectors as Velocities of Curves#^cor-29-5|Corollary §29.5: Product Coordinates]]
- [[§30 The Cotangent Space#^lem-30-2|Lemma §30.2: The Differential in Coordinates]]
- [[§31 Local Diffeomorphisms#^thm-31-2|Theorem §31.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§32 Submersions#^thm-32-4|Theorem §32.4: Local Normal Form for Submersions]]
- [[§32 Submersions#^cor-32-5|Corollary §32.5: Being a Submersion Is an Open Condition]]
- [[§33 Submanifolds#^prop-33-4|Proposition §33.4: Tangent Spaces of a Submanifold]]
- [[§33 Submanifolds#^prop-33-8|Proposition §33.8: The Old and New Versions Agree]]
- [[§35 Immersions#^thm-35-1|Theorem §35.1: Local Normal Form for Immersions]]
- [[§38 SU(2) → SO(3)꞉ The Double Cover#^thm-38-10|Theorem §38.10: The Double Cover SU(2) → SO(3)]]
- [[§39 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-39-1|Example §39.1: Vectors in the Plane in Three Ways]]
- [[§40 Recap꞉ Covectors and the Four Differentials#^ex-40-1|Example §40.1: Covectors in the Plane]]
- [[§43 One-Forms#^prop-43-5|Proposition §43.5: Pullbacks in Coordinates]]

## Connections
- **Used for.** Every local computation with differentials: the chain rule and change of coordinates in matrices ([[§28 The Differential in Coordinates#^cor-28-3|§28.3]], [[§28 The Differential in Coordinates#^cor-28-4|§28.4]]), agreement with the Jacobian on ℝⁿ ([[§28 The Differential in Coordinates#^prop-28-5|§28.5]]), regular values inside one chart ([[§28 The Differential in Coordinates#^prop-28-7|§28.7]]), the [[Local Diffeomorphism Criterion]], the [[Submersion Normal Form]] and the transition maps of TM ([[Tangent Bundle Is a Smooth Manifold]]).
- **The map is intrinsic, the matrix is not.** Changing charts multiplies the matrix by Jacobians of transition maps, so only rank, kernel, image, injectivity and surjectivity are properties of F; that is why regular values are defined through F_*p ([[§28 The Differential in Coordinates#^rem-28-4|The Map Is Intrinsic — the Matrix Is Not]]). In polar coordinates ∂/∂θ corresponds to a vector of length r, not 1 ([[§28 The Differential in Coordinates#^ex-28-1|Ex. §28.1]]).
- **Same idea elsewhere.** It is the matrix of a linear map in given bases ([[§9 Matrices#^ladr-3-31|LADR 3.31]]), with the change-of-basis rule ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]), and it is the Jacobian matrix of 452 ([[§7 Differentiability#^def-7-3|452 Def. §7.3]]). Row j is the gradient of the component Fʲ: gradients go across ([[§28 The Differential in Coordinates#^rem-28-2|§28, Remark]]).
- **Coming later in the course.** When m = n, F pulls back dy¹ ∧ ⋯ ∧ dyⁿ to the determinant of this matrix times dx¹ ∧ ⋯ ∧ dxⁿ, the change-of-variables factor in integrating differential forms. 452 works out the case n = 2 ([[§37 The Algebra of Differential Forms#^ex-37-4|452 Ex. §37.4]]), the signed form of the [[Change of Variables Formula (multiple integrals)|change-of-variables formula]].
