---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 12.22", "Jacobian of the coordinate representation"]
tags: [differentiable-manifolds, hub]
---
![[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22]]

## Treated in
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|Theorem §12.22: The Matrix of the Differential]], in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space]]

## Its proof uses
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-10|Definition §12.10: Pushforward — the Differential]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-10|Proposition §12.10: The Differential Is a Linear Map of Abstract Tangent Spaces]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|Theorem §12.16: Basis Theorem]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|Proposition §12.21: Partial Derivatives Upstairs and Downstairs]]

## Its proof uses (other subjects)
- [[3C Matrices#^ladr-3-31|LADR 3.31 Matrix of a linear map, M(T)]]

## Used in (Differentiable Manifolds)
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|Corollary §12.23: The Chain Rule in Coordinates]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|Corollary §12.24: Change of Coordinates]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|Proposition §12.25: Agreement with the Vector-Space Differential]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-27|Proposition §12.27: Regular Values Inside One Chart]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-33|Corollary §12.33: Product Coordinates]]
- [[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2|Lemma §13.2: The Differential in Coordinates]]
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-2|Theorem §14.2: Local Diffeomorphisms Are Detected by the Differential]]
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|Theorem §14.5: Local Normal Form for Submersions]]
- [[§14 Local Diffeomorphisms and Submersions#^cor-14-8|Corollary §14.8: Being a Submersion Is an Open Condition]]
- [[§15 Submanifolds#^prop-15-4|Proposition §15.4: Tangent Spaces of a Submanifold]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]

## Connections
- **Used for.** Every local computation with differentials: the chain rule and change of coordinates in matrices ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|§12.23]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|§12.24]]), agreement with the Jacobian on ℝⁿ ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]]), regular values inside one chart ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-27|§12.27]]), the [[Local Diffeomorphism Criterion]], the [[Submersion Normal Form]] and the transition maps of TM ([[Tangent Bundle Is a Smooth Manifold]]).
- **The map is intrinsic, the matrix is not.** Changing charts multiplies the matrix by Jacobians of transition maps, so only rank, kernel, image, injectivity and surjectivity are properties of F; that is why regular values are defined through F_*p ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-14|The Map Is Intrinsic — the Matrix Is Not]]). In polar coordinates ∂/∂θ corresponds to a vector of length r, not 1 ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^ex-12-3|Ex. §12.3]]).
- **Same idea elsewhere.** It is the matrix of a linear map in given bases ([[3C Matrices#^ladr-3-31|LADR 3.31]]), with the change-of-basis rule ([[3D Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]), and it is the Jacobian matrix of 452 ([[§6 Differentiability#^def-6-2|452 Def. §6.2]]). Row j is the gradient of the component Fʲ: gradients go across ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^rem-12-12|§12, Remark]]).
- **Coming later in the course.** When m = n, F pulls back dy¹ ∧ ⋯ ∧ dyⁿ to the determinant of this matrix times dx¹ ∧ ⋯ ∧ dxⁿ, the change-of-variables factor in integrating differential forms.
