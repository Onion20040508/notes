---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 20.1", "Stokes' theorem (classical)"]
tags: [multivariable-analysis, hub]
---
![[§20 Stokes' Theorem in ℝ³#^thm-20-1]]

## Treated in
- [[§20 Stokes' Theorem in ℝ³#^thm-20-1|Theorem §20.1: Stokes' Theorem]], in [[§20 Stokes' Theorem in ℝ³]]

## Its proof uses
- [[§5 Equality of Mixed Partials#^thm-5-1|Theorem §5.1: Schwarz–Clairaut]]
- [[§6 Differentiability#^thm-6-4|Theorem §6.4: Product Rule for Partial Derivatives]]
- [[§10 Composition of Functions and the Chain Rule#^thm-10-2|Theorem §10.2: Multivariable Chain Rule]]
- [[§16 Line Integrals and Green's Theorem#^thm-16-1|Theorem §16.1: Green's Theorem]]
- [[§16 Line Integrals and Green's Theorem#^def-16-2|Definition §16.2: Work Line Integral]]
- [[§16 Line Integrals and Green's Theorem#^def-16-5|Definition §16.5: Curl]]
- [[§18 Surface Integrals#^def-18-1|Definition §18.1: Parametrized Surface]]
- [[§18 Surface Integrals#^def-18-6|Definition §18.6: Vector Surface Integral / Flux Integral]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof idea.** Pull both sides back to the parameter domain with the [[Multivariable Chain Rule]], apply [[Green's Theorem]] there, and match the integrands term by term. The second-derivative terms cancel by [[Schwarz–Clairaut Theorem]], which is why the parametrization must be C² ([[§20 Stokes' Theorem in ℝ³#^rem-20-3|Structure of the Proof]]).
- **Chain.** The flat case is [[§16 Line Integrals and Green's Theorem#^thm-16-3|Green's Theorem as 2D Stokes]]. The [[Divergence Theorem in ℝ³]] reduces to the FTC, while Stokes reduces to Green ([[§20 Stokes' Theorem in ℝ³#^rem-20-5|The Complete Picture]]). In forms language, d on 1-forms is the curl ([[§22 The Algebra of Differential Forms#^prop-22-3|§22.3]]), and this is the case of the [[Generalized Stokes' Theorem]] for a 1-form on a surface.
- **Consequences.** The flux of a curl through a closed surface is zero, and it is the same for any two surfaces with the same boundary ([[§20 Stokes' Theorem in ℝ³#^rem-20-4|Special Cases]]). The first is also an instance of [[Exterior Derivative Squares to Zero]].
- **Linear algebra.** The components of X_u × X_v are the 2×2 minors of the derivative DX, i.e. the pullbacks of dy∧dz, dz∧dx and dx∧dy ([[§22 The Algebra of Differential Forms#^rem-22-3|The Cross Product Is the Pullback in Disguise]]).
- **Also in [[Calculus]]:** [[§114 Stokes' Theorem#^thm-114-1|Calc Thm. §114.1]] (computational treatment with worked examples).
