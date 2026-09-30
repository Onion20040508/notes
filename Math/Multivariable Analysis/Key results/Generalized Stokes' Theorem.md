---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 23.1", "Stokes' theorem for forms"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1]]

## Treated in
- [[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1|Theorem §23.1: Generalized Stokes' Theorem]], in [[Multivariable Analysis §23 The Generalized Stokes' Theorem]]

## Its proof uses
- (no proof in the notes)

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Special cases.** A 0-form on [a, b] gives the [[Fundamental Theorem of Calculus]]. A 1-form on a plane region gives [[Green's Theorem]], and on a surface in ℝ³ it gives [[Stokes' Theorem in ℝ³]]. A 2-form on a solid gives the [[Divergence Theorem in ℝ³]], and an (n−1)-form on a region in ℝⁿ gives the [[Divergence Theorem in ℝⁿ]]. The course verifies these cases rather than proving the general statement.
- **Ingredients.** On ℝ³, d on 0-, 1- and 2-forms is gradient, curl and divergence ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-2|§22.2]], [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-3|§22.3]], [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-4|§22.4]]). Both sides are computed by [[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-3|pullback]]; in top degree its coefficient is the Jacobian determinant, whose sign carries orientation and whose absolute value is the volume factor ([[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]]).
- **Linear algebra.** At each point a k-form is an alternating k-linear form ([[Linear Algebra 9B Alternating Multilinear Forms#^ladr-9-27|LADR 9.27]]), so antisymmetry of ∧ handles all the orientation signs of the classical proofs ([[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-1|wedge product]]).
- **Proofs of the classical cases.** Green and the divergence theorems reduce to the FTC in one variable. Stokes in ℝ³ reduces to Green on the parameter domain ([[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^rem-20-5|The Complete Picture]]). Together with [[Exterior Derivative Squares to Zero]], it shows that an exact form dη integrates to zero over any boundary ∂Ω.
