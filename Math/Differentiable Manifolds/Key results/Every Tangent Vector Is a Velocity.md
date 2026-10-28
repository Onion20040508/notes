---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 31.4", "Lee Proposition 3.23"]
tags: [differentiable-manifolds, hub]
---
![[§31 Tangent Vectors as Velocities of Curves#^thm-31-4]]

## Treated in
- [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|Theorem §31.4: Every Tangent Vector Is a Velocity]], in [[§31 Tangent Vectors as Velocities of Curves]]

## Its proof uses
- [[§19 Smooth Functions and Smooth Maps#^def-19-3|Definition §19.3: Smooth Map]]
- [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Definition §29.1: Coordinate Functions of a Chart]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6: Basis Theorem]]
- [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|Definition §31.1: Smooth Curve]]
- [[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|Proposition §31.1: Velocity in Coordinates]]
- [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Definition §31.2: Velocity of a Curve]]

## Used in (Differentiable Manifolds)
- [[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|Corollary §31.5: Velocity of a Composite — Computing Differentials by Curves]]
- [[§36 Submersions#^prop-36-3|Proposition §36.3: Local Extrema Are Critical Points]]
- [[§39 Transversality and Lagrange Multipliers#^thm-39-6|Theorem §39.6: Lagrange Multipliers]]
- [[§47 The Unit Quaternions and SU(2)#^prop-47-6|Proposition §47.6: The Tangent Space of SU(2) at the Identity]]
- [[§65 The Whitney Embedding Theorem#^lem-65-1|Lemma §65.1: Compact Manifolds Embed in Some ℝᵏ]]

## Connections
- **Used for.** Computing differentials by curves: F_*p(D) is the velocity of F ∘ γ for any curve γ with velocity D ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-5|§31.5]]). This is how the tangent spaces of submanifolds ([[§37 Regular Submanifolds#^prop-37-6|§37.6]]) and of products ([[§31 Tangent Vectors as Velocities of Curves#^cor-31-8|§31.8]]) are read off, and it enters the comparison of the old and new regular value theorems ([[§38 The Regular Value Theorem for Manifolds#^prop-38-4|§38.4]]).
- **What it means.** T_pM is the set of curves through p modulo having the same velocity in one, hence every, chart: tangent vectors as velocities, with no ambient space ([[§31 Tangent Vectors as Velocities of Curves#^rem-31-1|The Two Faces Reconciled]]). The curve is a straight line in a chart, carried up by the inverse chart; the bending this introduces is invisible to the velocity ([[§31 Tangent Vectors as Velocities of Curves#^prop-31-1|§31.1]]).
- **Same idea elsewhere.** For a level set in ℝᴺ, velocities of curves are the definition of the geometric tangent space ([[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]]). Between vector spaces dF_p(v) is the derivative of F(p + tv) at t = 0 ([[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]]); that curve method gave the tangent spaces of O(n) and the gradient of det ([[Jacobi's Formula]]). In ℝ² it is the 452 [[Directional Derivative Formula]].
- **Coming later in the course.** Vector fields are now defined ([[§56 Vector Fields#^def-56-1|Def. §56.1]]); their flows are still to come: an integral curve of a vector field has a prescribed velocity at every one of its points, not just at one.
