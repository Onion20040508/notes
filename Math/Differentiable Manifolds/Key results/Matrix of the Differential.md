---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 30.2", "Jacobian of the coordinate representation"]
tags: [differentiable-manifolds, hub]
---
![[§30 The Differential in Coordinates#^thm-30-2]]

## Treated in
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]], in [[§30 The Differential in Coordinates]]

## Its proof uses
- [[§7 The Regular Value Theorem#^def-7-1|Definition §7.1: Jacobian Matrix]]
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|Proposition §28.5: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Definition §28.6: Pushforward — the Differential]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Definition §29.2: Coordinate Derivations]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]
- [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1: Partial Derivatives Upstairs and Downstairs]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-31|LADR 3.31 Matrix of a linear map, M(T)]]

## Used in (Differentiable Manifolds)
- [[§30 The Differential in Coordinates#^cor-30-3|Corollary §30.3: The Chain Rule in Coordinates]]
- [[§30 The Differential in Coordinates#^cor-30-4|Corollary §30.4: Change of Coordinates]]
- [[§30 The Differential in Coordinates#^prop-30-5|Proposition §30.5: Agreement with the Vector-Space Differential]]
- [[§30 The Differential in Coordinates#^prop-30-8|Proposition §30.8: Regular Values Inside One Chart]]
- [[§30 The Differential in Coordinates#^prop-30-10|Proposition §30.10: Maps with Zero Differential Are Constant]]
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|Corollary §31.5: Product Coordinates]]
- [[§33 Covectors in Coordinates#^lem-33-1|Lemma §33.1: The Differential in Coordinates]]
- [[§35 Local Diffeomorphisms#^thm-35-2|Theorem §35.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§36 Submersions#^thm-36-4|Theorem §36.4: Local Normal Form for Submersions]]
- [[§36 Submersions#^cor-36-5|Corollary §36.5: Being a Submersion Is an Open Condition]]
- [[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6: Tangent Spaces of a Regular Submanifold]]
- [[§37 Regular Submanifolds#^prop-37-11|Proposition §37.11: The Old and New Versions Agree]]
- [[§37 Regular Submanifolds#^thm-37-12|Theorem §37.12: Preimages of Transverse Submanifolds]]
- [[§39 Examples of Fibrations#^prop-39-2|Proposition §39.2: The Normal Bundle Is a Submanifold]]
- [[§40 Immersions#^ex-40-1|Example §40.1: An Immersion That Crosses Itself]]
- [[§40 Immersions#^thm-40-1|Theorem §40.1: Local Normal Form for Immersions]]
- [[§41 Embeddings#^prop-41-12|Proposition §41.12: The Irrational Line on the Torus]]
- [[§44 The Unit Quaternions and SU(2)#^prop-44-4|Proposition §44.4: The Unit Quaternions]]
- [[§45 SU(2) → SO(3)꞉ The Double Cover#^thm-45-4|Theorem §45.4: The Double Cover SU(2) → SO(3)]]
- [[§46 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-46-1|Example §46.1: Vectors in the Plane in Three Ways]]
- [[§47 Recap꞉ Covectors and the Four Differentials#^ex-47-1|Example §47.1: Covectors in the Plane]]
- [[§50 One-Forms#^prop-50-5|Proposition §50.5: Pullbacks in Coordinates]]
- [[§51 Critical Points and the Hessian#^prop-51-4|Proposition §51.4: The Zero Section Is a Regular Submanifold]]
- [[§51 Critical Points and the Hessian#^prop-51-5|Proposition §51.5: The Vertical Space of T^*M Along the Zero Section]]
- [[§51 Critical Points and the Hessian#^prop-51-6|Proposition §51.6: The Differential of df at a Critical Point]]

## Connections
- **Used for.** Every local computation with differentials: the chain rule and change of coordinates in matrices ([[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§30 The Differential in Coordinates#^cor-30-4|§30.4]]), agreement with the Jacobian on ℝⁿ ([[§30 The Differential in Coordinates#^prop-30-5|§30.5]]), regular values inside one chart ([[§30 The Differential in Coordinates#^prop-30-8|§30.8]]), the [[Local Diffeomorphism Criterion]], the [[Submersion Normal Form]] and the transition maps of TM ([[Tangent Bundle Is a Smooth Manifold]]).
- **The map is intrinsic, the matrix is not.** Changing charts multiplies the matrix by Jacobians of transition maps, so only rank, kernel, image, injectivity and surjectivity are properties of F; that is why regular values are defined through F_*p ([[§30 The Differential in Coordinates#^rem-30-5|The Map Is Intrinsic — the Matrix Is Not]]). In polar coordinates ∂/∂θ corresponds to a vector of length r, not 1 ([[§30 The Differential in Coordinates#^ex-30-1|Ex. §30.1]]).
- **Same idea elsewhere.** It is the matrix of a linear map in given bases ([[§9 Matrices#^ladr-3-31|LADR 3.31]]), with the change-of-basis rule ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]), and it is the Jacobian matrix of 452 ([[§7 Differentiability#^def-7-3|452 Def. §7.3]]). Row j is the gradient of the component Fʲ: gradients go across ([[§30 The Differential in Coordinates#^rem-30-2|§30, Remark]]).
- **Coming later in the course.** When m = n, F pulls back dy¹ ∧ ⋯ ∧ dyⁿ to the determinant of this matrix times dx¹ ∧ ⋯ ∧ dxⁿ, the change-of-variables factor in integrating differential forms. 452 works out the case n = 2 ([[§37 The Algebra of Differential Forms#^ex-37-4|452 Ex. §37.4]]), the signed form of the [[Change of Variables Formula (multiple integrals)|change-of-variables formula]].
