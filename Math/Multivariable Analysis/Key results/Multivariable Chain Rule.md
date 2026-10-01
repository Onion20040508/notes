---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 10.2", "chain rule in several variables"]
tags: [multivariable-analysis, hub]
---
![[§10 Composition of Functions and the Chain Rule#^thm-10-2]]

## Treated in
- [[§10 Composition of Functions and the Chain Rule#^thm-10-2|Theorem §10.2: Multivariable Chain Rule]], in [[§10 Composition of Functions and the Chain Rule]]

## Its proof uses
- [[§3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[§3 Continuity and Limits of Functions#^thm-3-1|Theorem §3.1: Sum and Difference of Continuous Functions]]
- [[§3 Continuity and Limits of Functions#^thm-3-2|Theorem §3.2: Product of Continuous Functions]]
- [[§4 Partial Derivatives#^def-4-1|Definition §4.1: Partial Derivatives]]
- [[§6 Differentiability#^thm-6-2|Theorem §6.2: Continuous Partials Imply Differentiability]]
- [[§10 Composition of Functions and the Chain Rule#^thm-10-1|Theorem §10.1: Continuity of Composition]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[§13 The Inverse Function Theorem#^thm-13-2|Theorem §13.2: Inverse Function Theorem]]
- [[§14 Optimization and Lagrange Multipliers#^thm-14-2|Theorem §14.2: Method of Lagrange Multipliers]]
- [[§14 Optimization and Lagrange Multipliers#^thm-14-3|Theorem §14.3: Lagrange Multipliers with Multiple Constraints]]
- [[§15 Multivariable Integration#^thm-15-14|Theorem §15.14: Change of Variables Formula — Rectangular Case]]
- [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|Theorem §17.5: Fundamental Solution of the 2D Laplacian]]
- [[§20 Stokes' Theorem in ℝ³#^thm-20-1|Theorem §20.1: Stokes' Theorem]]
- [[§22 The Algebra of Differential Forms#^prop-22-11|Proposition §22.11: A Closed Form That Is Not Exact]]

## Used in (Differentiable Manifolds)
- [[§4 The Regular Value Theorem#^def-4-1|Definition §4.1: Jacobian and Rank]]
- [[§4 The Regular Value Theorem#^thm-4-3|Theorem §4.3: Regular Value Theorem]]
- [[§5 Topological Groups and Classical Matrix Groups#^rem-5-3|Remark: The Method: Level Sets and the Implicit Function Theorem]]
- [[§5 Topological Groups and Classical Matrix Groups#^prop-5-9|Proposition §5.9: Derivative of the Determinant]]
- [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|Corollary §5.13: SL(n,ℝ) Is a Manifold of Dimension n² − 1]]
- [[§8 Differentiable Structures#^thm-8-1|Theorem §8.1: Compatibility Means the Two Notions Agree]]
- [[§8 Differentiable Structures#^ex-8-5|Example §8.5: Two Smooth Structures on the Real Line]]
- [[§8 Differentiable Structures#^thm-8-5|Theorem §8.5: Every Atlas Lies in a Unique Maximal Atlas]]
- [[§8 Differentiable Structures#^prop-8-12|Proposition §8.12: Some Chart Suffices — Every Chart Then Works]]
- [[§8 Differentiable Structures#^prop-8-13|Proposition §8.13: Smoothness of a Map Does Not Depend on the Charts]]
- [[§8 Differentiable Structures#^prop-8-14|Proposition §8.14: The Two Notions of Diffeomorphism Agree]]
- [[§8 Differentiable Structures#^lem-8-15|Lemma §8.15: Composition of Smooth Maps]]
- [[§9 Manifolds in Euclidean Space#^thm-9-1|Theorem §9.1: The Two Descriptions Agree]]
- [[§9 Manifolds in Euclidean Space#^prop-9-2|Proposition §9.2: Regular Level Sets Are Smooth Manifolds]]
- [[§9 Manifolds in Euclidean Space#^lem-9-3|Lemma §9.3: Smooth Maps into and out of Regular Level Sets]]
- [[§9 Manifolds in Euclidean Space#^prop-9-4|Proposition §9.4: The Three Circle Atlases Define One Smooth Structure]]
- [[§10 Vector Spaces and Matrix Groups#^lem-10-8|Lemma §10.8: Independence of Coordinates]]
- [[§10 Vector Spaces and Matrix Groups#^thm-10-10|Theorem §10.10: Coordinate-Free Formula for the Differential]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|Lemma §11.2: The Geometric Tangent Space of a Graph]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^cor-11-4|Corollary §11.4: Three Descriptions of the Geometric Tangent Space]]
- [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7: Preimages of Transverse Level Sets]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-1|Definition §12.1: The Directional Derivative Attached to a Tangent Vector]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-1|Proposition §12.1: Basic Properties of D_v]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-17|Lemma §12.17: Hadamard's Lemma]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|Corollary §12.23: The Chain Rule in Coordinates]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|Proposition §12.25: Agreement with the Vector-Space Differential]]
- [[§15 Submanifolds#^prop-15-8|Proposition §15.8: The Old and New Versions Agree]]
- [[§17 The Tangent Bundle#^prop-17-5|Proposition §17.5: The Cotangent Transition Maps]]

## Connections
- **Proof idea.** Split the increment of g into single-variable increments and apply the one-variable [[Mean Value Theorem]]. Continuity of the partials controls the intermediate points. The 451 version is the [[§28 Basic Properties of the Derivative#^thm-28-3|Chain Rule]] (§28.3). Under differentiability alone, see [[§6 Differentiability#^thm-6-9|Theorem §6.9]].
- **Linear algebra.** In matrix form, Dg = Df · D(φ, ψ) ([[§10 Composition of Functions and the Chain Rule#^rem-10-2|Matrix Form]]): the derivative of a composition is the composition of the derivatives, and its matrix is the product of the matrices ([[§9 Matrices#^ladr-3-43|LADR 3.43]]). Since determinants are multiplicative ([[§34 Determinants#^ladr-9-49|LADR 9.49]]), a map and its inverse have [[§13 The Inverse Function Theorem#^rem-13-6|reciprocal Jacobians]].
- **Used for.** It is the engine of the [[Inverse Function Theorem (several variables)]] and the [[Method of Lagrange Multipliers]], and it appears in the [[§15 Multivariable Integration#^thm-15-14|rectangular change of variables]]. It also underlies [[§22 The Algebra of Differential Forms#^def-22-3|pullback]] and the reduction of [[Stokes' Theorem in ℝ³]] to the parameter domain.
