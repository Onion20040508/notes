---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 29.2", "Lee Proposition 3.23"]
tags: [differentiable-manifolds, hub]
---
![[§31 Tangent Vectors as Velocities of Curves#^thm-31-2]]

## Treated in
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2: Every Tangent Vector Is a Velocity]], in [[§31 Tangent Vectors as Velocities of Curves]]

## Its proof uses
- [[§19 Smooth Functions and Smooth Maps#^def-19-3|Definition §19.3: Smooth Map and Diffeomorphism]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Definition §29.1: Coordinate Functions of a Chart]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5: Basis Theorem]]
- [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Definition §31.2: Smooth Curve and Its Velocity]]
- [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|Proposition §31.1: Velocity in Coordinates]]

## Used in (Differentiable Manifolds)
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|Corollary §31.3: Velocity of a Composite — Computing Differentials by Curves]]
- [[§40 The Unit Quaternions and SU(2)#^prop-40-6|Proposition §40.6: The Tangent Space of SU(2) at the Identity]]

## Connections
- **Used for.** Computing differentials by curves: F_*p(D) is the velocity of F ∘ γ for any curve γ with velocity D ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]). This is how the tangent spaces of submanifolds ([[§35 Submanifolds#^prop-35-4|§35.4]]) and of products ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-6|§31.6]]) are read off, and it enters the comparison of the old and new regular value theorems ([[§35 Submanifolds#^prop-35-8|§35.8]]).
- **What it means.** T_pM is the set of curves through p modulo having the same velocity in one, hence every, chart: tangent vectors as velocities, with no ambient space ([[§31 Tangent Vectors as Velocities of Curves#^rem-31-1|The Two Faces Reconciled]]). The curve is a straight line in a chart, carried up by the inverse chart; the bending this introduces is invisible to the velocity ([[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]).
- **Same idea elsewhere.** For a level set in ℝᴺ, velocities of curves are the definition of the geometric tangent space ([[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]]). Between vector spaces dF_p(v) is the derivative of F(p + tv) at t = 0 ([[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]]); that curve method gave the tangent spaces of O(n) and the gradient of det ([[Jacobi's Formula]]). In ℝ² it is the 452 [[Directional Derivative Formula]].
- **Coming later in the course.** Vector fields are now defined ([[§47 Vector Fields#^def-47-1|Def. §47.1]]); their flows are still to come: an integral curve of a vector field has a prescribed velocity at every one of its points, not just at one.
