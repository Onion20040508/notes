---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 34.1", "Stokes' theorem (classical)"]
tags: [multivariable-analysis, hub]
---
![[§34 Stokes' Theorem in ℝ³#^thm-34-1]]

## Treated in
- [[§34 Stokes' Theorem in ℝ³#^thm-34-1|Theorem §34.1: Stokes' Theorem]], in [[§34 Stokes' Theorem in ℝ³]]

## Its proof uses
- [[§6 Equality of Mixed Partials#^thm-6-1|Theorem §6.1: Schwarz–Clairaut]]
- [[§8 Algebra of Differentiable Functions#^thm-8-2|Theorem §8.2: Product Rule for Partial Derivatives]]
- [[§12 Composition of Functions and the Chain Rule#^thm-12-2|Theorem §12.2: Multivariable Chain Rule]]
- [[§27 Line Integrals and Green's Theorem#^thm-27-1|Theorem §27.1: Green's Theorem]]
- [[§27 Line Integrals and Green's Theorem#^def-27-2|Definition §27.2: Work Line Integral]]
- [[§27 Line Integrals and Green's Theorem#^def-27-6|Definition §27.6: Curl]]
- [[§31 Surface Integrals#^def-31-1|Definition §31.1: Parametrized Surface]]
- [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^def-32-1|Definition §32.1: Vector Surface Integral / Flux Integral]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Connections
- **Proof idea.** Pull both sides back to the parameter domain with the [[Multivariable Chain Rule]], apply [[Green's Theorem]] there, and match the integrands term by term. The second-derivative terms cancel by [[Schwarz–Clairaut Theorem]], which is why the parametrization must be C² ([[§34 Stokes' Theorem in ℝ³#^rem-34-3|Structure of the Proof]]).
- **Chain.** The flat case is [[§27 Line Integrals and Green's Theorem#^thm-27-3|Green's Theorem as 2D Stokes]]. The [[Divergence Theorem in ℝ³]] reduces to the FTC, while Stokes reduces to Green ([[§34 Stokes' Theorem in ℝ³#^rem-34-5|The Complete Picture]]). In forms language, d on 1-forms is the curl ([[§38 The Exterior Derivative#^prop-38-2|§38.2]]), and this is the case of the [[Generalized Stokes' Theorem]] for a 1-form on a surface.
- **Consequences.** The flux of a curl through a closed surface is zero, and it is the same for any two surfaces with the same boundary ([[§34 Stokes' Theorem in ℝ³#^rem-34-4|Special Cases]]). The first is also an instance of [[Exterior Derivative Squares to Zero]].
- **Linear algebra.** The components of X_u × X_v are the 2×2 minors of the derivative DX, i.e. the pullbacks of dy∧dz, dz∧dx and dx∧dy ([[§37 The Algebra of Differential Forms#^rem-37-3|The Cross Product Is the Pullback in Disguise]]).
- **Also in [[Calculus]]:** [[§136 Stokes' Theorem#^thm-136-1|Calc Thm. §136.1]] (computational treatment with worked examples).
