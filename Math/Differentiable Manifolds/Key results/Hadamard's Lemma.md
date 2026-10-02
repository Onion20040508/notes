---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 24.2", "Lee Theorem C.15"]
tags: [differentiable-manifolds, hub]
---
![[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2]]

## Treated in
- [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-2|Lemma §24.2: Hadamard's Lemma]], in [[§24 Coordinate Derivations and the Basis Theorem]]

## Its proof uses
- (only definitions)

## Its proof uses (other subjects)
- [[Multivariable Chain Rule]] (Multivariable Analysis)
- [[Fundamental Theorem of Calculus]] (Single Variable Analysis)

## Used in (Differentiable Manifolds)
- [[§24 Coordinate Derivations and the Basis Theorem#^lem-24-3|Lemma §24.3: Taylor–Hadamard]]
- [[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|Proposition §27.4: Germs Vanishing to Second Order]]

## Connections
- **Used for.** Applied twice it gives Taylor–Hadamard ([[§24 Coordinate Derivations and the Basis Theorem#^lem-24-3|§24.3]]), hence every derivation on ℝⁿ is Σ D[rⁱ] ∂/∂rⁱ ([[§24 Coordinate Derivations and the Basis Theorem#^cor-24-4|§24.4]]), hence the [[Basis Theorem for Tangent Spaces]]. It also shows that I_p² consists of the germs vanishing to second order ([[§27 Tangent Spaces III꞉ The Cotangent Space#^prop-27-4|§27.4]]), the key step of [[Cotangent Space from Germs]].
- **What matters is that the fᵢ are smooth.** The remainder is a product of factors vanishing at a with smooth functions that do not blow up at a ([[§24 Coordinate Derivations and the Basis Theorem#^rem-24-2|§24, Remark]]). The remainder in 452's [[Multivariable Taylor's Theorem]] is evaluated at an unknown intermediate point, so it gives no such coefficient functions. The proof integrates along the segment from a to r, which is why the domain is a ball centred at a.
- **Same idea elsewhere.** The proof is the [[Fundamental Theorem of Calculus]] applied to t ↦ f(a + t(r − a)), with the [[Multivariable Chain Rule]]. For polynomials it is the factor theorem: p(a) = 0 gives p = (z − a)q ([[§13 Polynomials#^ladr-4-6|LADR 4.6]]). Hadamard says the same for smooth germs: a germ vanishing at a is a combination of the rⁱ − aⁱ with smooth coefficients.
