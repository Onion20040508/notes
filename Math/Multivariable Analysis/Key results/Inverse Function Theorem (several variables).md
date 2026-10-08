---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 16.2", "inverse function theorem in ℝⁿ"]
tags: [multivariable-analysis, hub]
---
![[§16 The Inverse Function Theorem#^thm-16-2]]

## Treated in
- [[§16 The Inverse Function Theorem#^thm-16-2|Theorem §16.2: Inverse Function Theorem]], in [[§16 The Inverse Function Theorem]]

## Its proof uses
- [[§12 Composition of Functions and the Chain Rule#^thm-12-2|Theorem §12.2: Multivariable Chain Rule]]
- [[§15 The Implicit Function Theorem#^thm-15-2|Theorem §15.2: Implicit Function Theorem — General Case]]
- [[§16 The Inverse Function Theorem#^def-16-1|Definition §16.1: Jacobian Matrix]]

## Used in (Multivariable Analysis)
- (not cited later in the course)

## Used in (Differentiable Manifolds)
- [[§7 The Regular Value Theorem#^thm-7-1|Theorem §7.1: Implicit Function Theorem — Lee Theorem C.40]]
- [[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1: Inverse Function Theorem]]
- [[§41 The Unit Quaternions and SU(2)#^prop-41-3|Proposition §41.3: Hyperspherical Charts Are Adapted to S³]]
- [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|Theorem §42.4: The Double Cover SU(2) → SO(3)]]

## Connections
- **Proof idea.** Apply the [[§15 The Implicit Function Theorem#^thm-15-2|Implicit Function Theorem]] twice: first solve φ(x, y) = ũ for x, then solve ψ(X(y, ũ), y) = ṽ for y. The second step needs det J / φ_x ≠ 0 ([[§16 The Inverse Function Theorem#^rem-16-4|Tracking IFT Hypotheses]]). The [[Multivariable Chain Rule]] gives the Jacobian of the inverse.
- **One-variable version.** The 451 [[§29 The Mean Value Theorem#^thm-29-10|Inverse Function Theorem]] (§29.10) has the condition f′(x₀) ≠ 0 and the derivative 1/f′ ([[§16 The Inverse Function Theorem#^rem-16-5|Comparison: 1D vs 2D]]).
- **Linear algebra.** The hypothesis says that the derivative is an invertible linear map ([[Invertible ⟺ nonzero determinant]], LADR 9.50). The inverse's Jacobian is J⁻¹ ([[§10 Invertibility and Isomorphisms#^ladr-3-86|LADR 3.86]]), and the two Jacobian determinants are reciprocal ([[§16 The Inverse Function Theorem#^rem-16-6|Reciprocal Jacobians]], [[§37 Determinants#^ladr-9-49|LADR 9.49]]).
- **Where it goes.** A nonvanishing Jacobian is the hypothesis of the [[Change of Variables Formula (multiple integrals)]], where |J| is the area factor. For polar coordinates |J| = r ([[§16 The Inverse Function Theorem#^ex-16-4|Polar to Cartesian]]).
- **On manifolds.** Quoted in all dimensions as [[§33 Local Diffeomorphisms#^thm-33-1|591 Thm. §33.1]], it is the analytic input of the [[Local Diffeomorphism Criterion]], the [[Submersion Normal Form]] and the [[Immersion Normal Form]].
- **Also in [[Complex Variables]]:** [[§114★ Local Inverses#^thm-114-1|342 Thm. §114.1]] (local inverses of conformal maps: for analytic f the Jacobian is |f′|², and the inverse is analytic; complex-variables version with worked examples).
