---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 25.2", "Jacobian of the coordinate representation"]
tags: [differentiable-manifolds, hub]
---
![[§25 The Differential in Coordinates#^thm-25-2]]

## Treated in
- [[§25 The Differential in Coordinates#^thm-25-2|Theorem §25.2: The Matrix of the Differential]], in [[§25 The Differential in Coordinates]]

## Its proof uses
- [[§23 Derivations and the Abstract Tangent Space#^def-23-5|Definition §23.5: Pushforward — the Differential]]
- [[§23 Derivations and the Abstract Tangent Space#^prop-23-5|Proposition §23.5: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§24 Coordinate Derivations and the Basis Theorem#^thm-24-5|Theorem §24.5: Basis Theorem]]
- [[§25 The Differential in Coordinates#^prop-25-1|Proposition §25.1: Partial Derivatives Upstairs and Downstairs]]

## Its proof uses (other subjects)
- [[§9 Matrices#^ladr-3-31|LADR 3.31 Matrix of a linear map, M(T)]]

## Used in (Differentiable Manifolds)
- [[§25 The Differential in Coordinates#^cor-25-3|Corollary §25.3: The Chain Rule in Coordinates]]
- [[§25 The Differential in Coordinates#^cor-25-4|Corollary §25.4: Change of Coordinates]]
- [[§25 The Differential in Coordinates#^prop-25-5|Proposition §25.5: Agreement with the Vector-Space Differential]]
- [[§25 The Differential in Coordinates#^prop-25-7|Proposition §25.7: Regular Values Inside One Chart]]
- [[§25 The Differential in Coordinates#^prop-25-9|Proposition §25.9: Maps with Zero Differential Are Constant]]
- [[§26 Tangent Vectors as Velocities of Curves#^cor-26-5|Corollary §26.5: Product Coordinates]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|Lemma §27.2: The Differential in Coordinates]]
- [[§28 Local Diffeomorphisms#^thm-28-2|Theorem §28.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§29 Submersions#^thm-29-4|Theorem §29.4: Local Normal Form for Submersions]]
- [[§29 Submersions#^cor-29-5|Corollary §29.5: Being a Submersion Is an Open Condition]]
- [[§30 Submanifolds#^prop-30-4|Proposition §30.4: Tangent Spaces of a Submanifold]]
- [[§30 Submanifolds#^prop-30-8|Proposition §30.8: The Old and New Versions Agree]]
- [[§33 Immersions#^thm-33-1|Theorem §33.1: Local Normal Form for Immersions]]

## Connections
- **Used for.** Every local computation with differentials: the chain rule and change of coordinates in matrices ([[§25 The Differential in Coordinates#^cor-25-3|§25.3]], [[§25 The Differential in Coordinates#^cor-25-4|§25.4]]), agreement with the Jacobian on ℝⁿ ([[§25 The Differential in Coordinates#^prop-25-5|§25.5]]), regular values inside one chart ([[§25 The Differential in Coordinates#^prop-25-7|§25.7]]), the [[Local Diffeomorphism Criterion]], the [[Submersion Normal Form]] and the transition maps of TM ([[Tangent Bundle Is a Smooth Manifold]]).
- **The map is intrinsic, the matrix is not.** Changing charts multiplies the matrix by Jacobians of transition maps, so only rank, kernel, image, injectivity and surjectivity are properties of F; that is why regular values are defined through F_*p ([[§25 The Differential in Coordinates#^rem-25-4|The Map Is Intrinsic — the Matrix Is Not]]). In polar coordinates ∂/∂θ corresponds to a vector of length r, not 1 ([[§25 The Differential in Coordinates#^ex-25-1|Ex. §25.1]]).
- **Same idea elsewhere.** It is the matrix of a linear map in given bases ([[§9 Matrices#^ladr-3-31|LADR 3.31]]), with the change-of-basis rule ([[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]), and it is the Jacobian matrix of 452 ([[§6 Differentiability#^def-6-2|452 Def. §6.2]]). Row j is the gradient of the component Fʲ: gradients go across ([[§25 The Differential in Coordinates#^rem-25-2|§25, Remark]]).
- **Coming later in the course.** When m = n, F pulls back dy¹ ∧ ⋯ ∧ dyⁿ to the determinant of this matrix times dx¹ ∧ ⋯ ∧ dxⁿ, the change-of-variables factor in integrating differential forms.
