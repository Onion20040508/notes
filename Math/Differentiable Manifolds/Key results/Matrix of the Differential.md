---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 28.2", "Jacobian of the coordinate representation"]
tags: [differentiable-manifolds, hub]
---
![[§30 The Differential in Coordinates#^thm-30-2]]

## Treated in
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]], in [[§30 The Differential in Coordinates]]

## Its proof uses
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|Proposition §28.5: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-31|LADR 3.31 Matrix of a linear map, M(T)]]

## Used in (Differentiable Manifolds)
- [[§30 The Differential in Coordinates#^cor-30-3|Corollary §30.3: The Chain Rule in Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4: Change of Coordinates]]
- [[§30 The Differential in Coordinates#^prop-30-5|Proposition §30.5: Agreement with the Vector-Space Differential]]
- [[§30 The Differential in Coordinates#^prop-30-7|Proposition §30.7: Regular Values Inside One Chart]]
- [[§30 The Differential in Coordinates#^prop-30-9|Proposition §30.9: Maps with Zero Differential Are Constant]]
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|Corollary §31.5: Product Coordinates]]
- [[§32 The Cotangent Space#^lem-32-2|Lemma §32.2: The Differential in Coordinates]]
- [[§33 Local Diffeomorphisms#^thm-33-2|Theorem §33.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§34 Submersions#^thm-34-4|Theorem §34.4: Local Normal Form for Submersions]]
- [[§34 Submersions#^cor-34-5|Corollary §34.5: Being a Submersion Is an Open Condition]]
- [[§35 Submanifolds#^prop-35-4|Proposition §35.4: Tangent Spaces of a Submanifold]]
- [[§35 Submanifolds#^prop-35-8|Proposition §35.8: The Old and New Versions Agree]]
- [[§37 Immersions#^thm-37-1|Theorem §37.1: Local Normal Form for Immersions]]
- [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4: The Double Cover SU(2) → SO(3)]]
- [[§42 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-42-1|Example §42.1: Vectors in the Plane in Three Ways]]
- [[§43 Recap꞉ Covectors and the Four Differentials#^ex-43-1|Example §43.1: Covectors in the Plane]]
- [[§46 One-Forms#^prop-46-5|Proposition §46.5: Pullbacks in Coordinates]]

## Connections
- **Used for.** Every local computation with differentials: the chain rule and change of coordinates in matrices ([[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), agreement with the Jacobian on ℝⁿ ([[§30 The Differential in Coordinates#^prop-30-5|§30.5]]), regular values inside one chart ([[§30 The Differential in Coordinates#^prop-30-7|§30.7]]), the [[Local Diffeomorphism Criterion]], the [[Submersion Normal Form]] and the transition maps of TM ([[Tangent Bundle Is a Smooth Manifold]]).
- **The map is intrinsic, the matrix is not.** Changing charts multiplies the matrix by Jacobians of transition maps, so only rank, kernel, image, injectivity and surjectivity are properties of F; that is why regular values are defined through F_*p ([[§30 The Differential in Coordinates#^rem-30-4|The Map Is Intrinsic — the Matrix Is Not]]). In polar coordinates ∂/∂θ corresponds to a vector of length r, not 1 ([[§30 The Differential in Coordinates#^ex-30-1|Ex. §30.1]]).
- **Same idea elsewhere.** It is the matrix of a linear map in given bases ([[§9 Matrices#^ladr-3-31|LADR 3.31]]), with the change-of-basis rule ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]), and it is the Jacobian matrix of 452 ([[§7 Differentiability#^def-7-3|452 Def. §7.3]]). Row j is the gradient of the component Fʲ: gradients go across ([[§30 The Differential in Coordinates#^rem-30-2|§28, Remark]]).
- **Coming later in the course.** When m = n, F pulls back dy¹ ∧ ⋯ ∧ dyⁿ to the determinant of this matrix times dx¹ ∧ ⋯ ∧ dxⁿ, the change-of-variables factor in integrating differential forms. 452 works out the case n = 2 ([[§37 The Algebra of Differential Forms#^ex-37-4|452 Ex. §37.4]]), the signed form of the [[Change of Variables Formula (multiple integrals)|change-of-variables formula]].
