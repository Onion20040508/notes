---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 13.2", "inverse function theorem in ℝⁿ"]
tags: [multivariable-analysis, hub]
---
![[§13 The Inverse Function Theorem#^thm-13-2]]

## Treated in
- [[§13 The Inverse Function Theorem#^thm-13-2|Theorem §13.2: Inverse Function Theorem]], in [[§13 The Inverse Function Theorem]]

## Its proof uses
- [[§10 Composition of Functions and the Chain Rule#^thm-10-2|Theorem §10.2: Multivariable Chain Rule]]
- [[§12 The Implicit Function Theorem#^thm-12-2|Theorem §12.2: Implicit Function Theorem — General Case]]
- [[§13 The Inverse Function Theorem#^def-13-1|Definition §13.1: Jacobian Matrix]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Used in (Differentiable Manifolds)
- [[§9 Manifolds in Euclidean Space#^thm-9-1|Theorem §9.1: The Two Descriptions Agree]]

## Connections
- **Proof idea.** Apply the [[§12 The Implicit Function Theorem#^thm-12-2|Implicit Function Theorem]] twice: first solve φ(x, y) = ũ for x, then solve ψ(X(y, ũ), y) = ṽ for y. The second step needs det J / φ_x ≠ 0 ([[§13 The Inverse Function Theorem#^rem-13-4|Tracking IFT Hypotheses]]). The [[Multivariable Chain Rule]] gives the Jacobian of the inverse.
- **One-variable version.** The 451 [[§29 The Mean Value Theorem#^thm-29-10|Inverse Function Theorem]] (§29.10) has the condition f′(x₀) ≠ 0 and the derivative 1/f′ ([[§13 The Inverse Function Theorem#^rem-13-5|Comparison: 1D vs 2D]]).
- **Linear algebra.** The hypothesis says that the derivative is an invertible linear map ([[Invertible ⟺ nonzero determinant]], LADR 9.50). The inverse's Jacobian is J⁻¹ ([[§10 Invertibility and Isomorphisms#^ladr-3-86|LADR 3.86]]), and the two Jacobian determinants are reciprocal ([[§13 The Inverse Function Theorem#^rem-13-6|Reciprocal Jacobians]], [[§34 Determinants#^ladr-9-49|LADR 9.49]]).
- **Where it goes.** A nonvanishing Jacobian is the hypothesis of the [[Change of Variables Formula (multiple integrals)]], where |J| is the area factor. For polar coordinates |J| = r ([[§13 The Inverse Function Theorem#^ex-13-4|Polar to Cartesian]]).
