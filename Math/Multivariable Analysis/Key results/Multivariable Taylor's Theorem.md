---
subject: math
type: theorem
source: "[[Multivariable Analysis]]"
aliases: ["MATH 452 11.2", "Taylor in several variables"]
tags: [multivariable-analysis, hub]
---
![[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2]]

## Treated in
- [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-2|Theorem §11.2: Multivariable Taylor's Theorem]], in [[§11 Taylor's Theorem for Multivariable Functions]]

## Its proof uses
- [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|Theorem §11.1: Derivatives of F(t)]]

## Its proof uses (other subjects)
- [[§31 Taylor's Theorem#^thm-31-2|451 §31.2: Taylor's Theorem with Lagrange Remainder]]

## Used in (Multivariable Analysis)
- [[§18 Second-Order Sufficient Conditions#^thm-18-1|Theorem §18.1: Second-Order Sufficient Conditions — Unconstrained]]

## Connections
- **Proof.** Restrict f to the segment, F(t) = f(x + th, y + tk), and apply the 451 [[§31 Taylor's Theorem#^thm-31-2|Taylor's Theorem with Lagrange Remainder]] at t = 1. The derivatives F⁽ᵐ⁾ come from [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-1|Theorem §11.1]], where [[Schwarz–Clairaut Theorem|equality of mixed partials]] collects the terms into binomial coefficients. The straight segment gives F⁽ᵐ⁾(0) = dᵐf with no correction terms ([[§11 Taylor's Theorem for Multivariable Functions#^rem-11-3|Why the Linear Path?]]).
- **Special cases.** N = 0 gives the two-variable mean value form ([[§11 Taylor's Theorem for Multivariable Functions#^ex-11-1|Example §11.1]]; compare [[§11 Taylor's Theorem for Multivariable Functions#^thm-11-4|Theorem §11.4]]). N = 1 gives f(x + h, y + k) = f + df + O(ρ²), which confirms [[§7 Differentiability#^def-7-1|differentiability]] ([[§11 Taylor's Theorem for Multivariable Functions#^ex-11-2|Example §11.2]]).
- **Linear algebra.** The second-order term is ½ times the quadratic form of the symmetric [[§18 Second-Order Sufficient Conditions#^def-18-1|Hessian]] ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-18|LADR 9.18]]). Its sign, read off from eigenvalues by the [[Real spectral theorem]], drives the [[Second Derivative Test in Several Variables]].
- **Used for.** It supplies the local linearization, with error control, in the first proof of the [[§24 The Change of Variables Formula#^thm-24-2|change of variables formula]] (§15.14).
- **Smooth remainder.** [[Hadamard's Lemma]] (591 Lemma §27.2) writes the first-order remainder with smooth coefficient functions instead of an intermediate point, which is what 591 needs to show that the [[§27 Coordinate Derivations and the Basis Theorem#^def-27-2|coordinate derivations]] span the tangent space ([[Basis Theorem for Tangent Spaces]], 591 Thm. §27.5).
