---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 10.2", "chain rule in several variables"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2]]

## Treated in
- [[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^thm-10-2|Theorem §10.2: Multivariable Chain Rule]], in [[Multivariable Analysis §10 Composition of Functions and the Chain Rule]]

## Its proof uses
- [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|Definition §3.1: Continuity]]
- [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Definition §4.1: Partial Derivatives]]

## Its proof uses (other subjects)
- [[Mean Value Theorem]] (Single Variable Analysis)

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §13 The Inverse Function Theorem#^thm-13-2|Theorem §13.2: Inverse Function Theorem]]
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-2|Theorem §14.2: Method of Lagrange Multipliers]]
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-3|Theorem §14.3: Lagrange Multipliers with Multiple Constraints]]
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Theorem §15.14: Change of Variables Formula — Rectangular Case]]
- [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|Theorem §17.5: Fundamental Solution of the 2D Laplacian]]
- [[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1|Theorem §20.1: Stokes' Theorem]]
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-3|Definition §22.3: Pullback]]
- [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-11|Proposition §22.11: A Closed Form That Is Not Exact]]

## Connections
- **Proof idea.** Split the increment of g into single-variable increments and apply the one-variable [[Mean Value Theorem]]. Continuity of the partials controls the intermediate points. The 451 version is the [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-3|Chain Rule]] (§28.3). Under differentiability alone, see [[Multivariable Analysis §6 Differentiability#^thm-6-9|Theorem §6.9]].
- **Linear algebra.** In matrix form, Dg = Df · D(φ, ψ) ([[Multivariable Analysis §10 Composition of Functions and the Chain Rule#^rem-10-2|Matrix Form]]): the derivative of a composition is the composition of the derivatives, and its matrix is the product of the matrices ([[Linear Algebra 3C Matrices#^ladr-3-43|LADR 3.43]]). Since determinants are multiplicative ([[Linear Algebra 9C Determinants#^ladr-9-49|LADR 9.49]]), a map and its inverse have [[Multivariable Analysis §13 The Inverse Function Theorem#^rem-13-6|reciprocal Jacobians]].
- **Used for.** It is the engine of the [[Inverse Function Theorem (several variables)]] and the [[Method of Lagrange Multipliers]], and it appears in the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|rectangular change of variables]]. It also underlies [[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-3|pullback]] and the reduction of [[Stokes' Theorem in ℝ³]] to the parameter domain.
