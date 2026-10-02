---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 28.2", "Lee Theorem 4.5", "Lee Proposition 4.8"]
tags: [differentiable-manifolds, hub]
---
![[§28 Local Diffeomorphisms and Submersions#^thm-28-2]]

## Treated in
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-2|Theorem §28.2: Local Diffeomorphisms Are Detected by the Differential]], in [[§28 Local Diffeomorphisms and Submersions]]

## Its proof uses
- [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|Theorem §23.6: The Chain Rule]]
- [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|Lemma §23.8: Open Subsets Have the Same Abstract Tangent Spaces]]
- [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|Proposition §23.9: Charts Are Diffeomorphisms]]
- [[§25 The Differential in Coordinates#^thm-25-2|Theorem §25.2: The Matrix of the Differential]]
- [[§28 Local Diffeomorphisms and Submersions#^def-28-1|Definition §28.1: Local Diffeomorphism]]
- [[§28 Local Diffeomorphisms and Submersions#^thm-28-1|Theorem §28.1: Inverse Function Theorem]]

## Used in (Differentiable Manifolds)
- [[§28 Local Diffeomorphisms and Submersions#^cor-28-3|Corollary §28.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms]]
- [[§28 Local Diffeomorphisms and Submersions#^prop-28-4|Proposition §28.4: Dimension Constraints]]

## Connections
- **Used for.** Diffeomorphisms are exactly the bijective local diffeomorphisms ([[§28 Local Diffeomorphisms and Submersions#^cor-28-3|§28.3]]), and a map between manifolds of equal dimension that is a submersion, or an immersion, at every point is a local diffeomorphism ([[§28 Local Diffeomorphisms and Submersions#^prop-28-4|§28.4]]). The same inverse-function step, with [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|§28.6]], builds the new chart in the [[Submersion Normal Form]].
- **Local, not global.** t ↦ (cos t, sin t) on (0, 4π) is a local diffeomorphism onto S¹ that is neither injective nor a covering map: (1, 0) has one preimage and every other point two ([[§28 Local Diffeomorphisms and Submersions#^ex-28-1|Ex. §28.1]], [[§28 Local Diffeomorphisms and Submersions#^rem-28-2|Covering Maps]]). Injectivity is the entire difference from a diffeomorphism ([[§28 Local Diffeomorphisms and Submersions#^rem-28-3|§14, Remark]]).
- **Same idea elsewhere.** The analytic input is the [[Inverse Function Theorem (several variables)]] of 452, applied to the coordinate representation, whose Jacobian is the matrix of F_*p ([[Matrix of the Differential]]). In 590, ℝ → S¹ is a covering map ([[§24 Covering Spaces#^thm-24-2|590 §24.2]]) while its restriction to (0, ∞) is a local homeomorphism that is not ([[§24 Covering Spaces#^ex-24-2|590 Ex. §24.2]]), the same failure as (0, 4π) → S¹.
