---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 9.2", "Taylor in several variables"]
tags: [multivariable-analysis, hub]
---
![[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-2]]

## Treated in
- [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-2|Theorem §9.2: Multivariable Taylor's Theorem]], in [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions]]

## Its proof uses
- [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-1|Theorem §9.1: Derivatives of F(t)]]

## Its proof uses (other subjects)
- [[Single Variable Analysis §31 Taylor's Theorem#^thm-31-2|451 §31.2: Taylor's Theorem with Lagrange Remainder]]

## Used in (Multivariable Analysis)
- [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^thm-14-4|Theorem §14.4: Second-Order Sufficient Conditions — Unconstrained]]
- [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|Theorem §15.14: Change of Variables Formula — Rectangular Case]]

## Connections
- **Proof.** Restrict f to the segment, F(t) = f(x + th, y + tk), and apply the 451 [[Single Variable Analysis §31 Taylor's Theorem#^thm-31-2|Taylor's Theorem with Lagrange Remainder]] at t = 1. The derivatives F⁽ᵐ⁾ come from [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^thm-9-1|Theorem §9.1]], where [[Schwarz–Clairaut Theorem|equality of mixed partials]] collects the terms into binomial coefficients. The straight segment gives F⁽ᵐ⁾(0) = dᵐf with no correction terms ([[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^rem-9-3|Why the Linear Path?]]).
- **Special cases.** N = 0 gives the two-variable mean value form ([[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^ex-9-1|Example §9.1]]; compare [[Mean Value Theorem in Several Variables]]). N = 1 gives f(x + h, y + k) = f + df + O(ρ²), which confirms [[Multivariable Analysis §6 Differentiability#^def-6-1|differentiability]] ([[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions#^ex-9-2|Example §9.2]]).
- **Linear algebra.** The second-order term is ½ times the quadratic form of the symmetric [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^def-14-2|Hessian]] ([[Linear Algebra 9A Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR 9.18]]). Its sign, read off from eigenvalues by the [[Real spectral theorem]], drives the [[Second Derivative Test in Several Variables]].
- **Used for.** It supplies the local linearization, with error control, in the first proof of the [[Multivariable Analysis §15 Multivariable Integration#^thm-15-14|change of variables formula]] (§15.14).
