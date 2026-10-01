---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 14.2", "Lee Theorem 4.5", "Lee Proposition 4.8"]
tags: [differentiable-manifolds, hub]
---
![[§14 Local Diffeomorphisms and Submersions#^thm-14-2]]

## Treated in
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-2|Theorem §14.2: Local Diffeomorphisms Are Detected by the Differential]], in [[§14 Local Diffeomorphisms and Submersions]]

## Its proof uses
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-11|Theorem §12.11: The Chain Rule]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^lem-12-13|Lemma §12.13: Open Subsets Have the Same Abstract Tangent Spaces]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|Proposition §12.14: Charts Are Diffeomorphisms]]
- [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-22|Theorem §12.22: The Matrix of the Differential]]
- [[§14 Local Diffeomorphisms and Submersions#^thm-14-1|Theorem §14.1: Inverse Function Theorem]]
- [[§14 Local Diffeomorphisms and Submersions#^def-14-1|Definition §14.1: Local Diffeomorphism]]

## Used in (Differentiable Manifolds)
- [[§14 Local Diffeomorphisms and Submersions#^cor-14-3|Corollary §14.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms]]
- [[§14 Local Diffeomorphisms and Submersions#^prop-14-4|Proposition §14.4: Dimension Constraints]]

## Connections
- **Used for.** Diffeomorphisms are exactly the bijective local diffeomorphisms ([[§14 Local Diffeomorphisms and Submersions#^cor-14-3|§14.3]]), and a map between manifolds of equal dimension that is a submersion, or an immersion, at every point is a local diffeomorphism ([[§14 Local Diffeomorphisms and Submersions#^prop-14-4|§14.4]]). The same inverse-function step, with [[§14 Local Diffeomorphisms and Submersions#^lem-14-7|§14.7]], builds the new chart in the [[Submersion Normal Form]].
- **Local, not global.** t ↦ (cos t, sin t) on (0, 4π) is a local diffeomorphism onto S¹ that is neither injective nor a covering map: (1, 0) has one preimage and every other point two ([[§14 Local Diffeomorphisms and Submersions#^ex-14-1|Ex. §14.1]], [[§14 Local Diffeomorphisms and Submersions#^rem-14-2|Covering Maps]]). Injectivity is the entire difference from a diffeomorphism ([[§14 Local Diffeomorphisms and Submersions#^rem-14-3|§14, Remark]]).
- **Same idea elsewhere.** The analytic input is the [[Inverse Function Theorem (several variables)]] of 452, applied to the coordinate representation, whose Jacobian is the matrix of F_*p ([[Matrix of the Differential]]). In 590, ℝ → S¹ is a covering map ([[§24 Covering Spaces#^thm-24-2|590 §24.2]]) while its restriction to (0, ∞) is a local homeomorphism that is not ([[§24 Covering Spaces#^ex-24-2|590 Ex. §24.2]]), the same failure as (0, 4π) → S¹.
