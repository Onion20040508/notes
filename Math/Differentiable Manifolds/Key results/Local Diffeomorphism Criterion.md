---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 31.2", "Lee Theorem 4.5", "Lee Proposition 4.8"]
tags: [differentiable-manifolds, hub]
---
![[§31 Local Diffeomorphisms#^thm-31-2]]

## Treated in
- [[§31 Local Diffeomorphisms#^thm-31-2|Theorem §31.2: Local Diffeomorphisms Are Detected by the Differential]], in [[§31 Local Diffeomorphisms]]

## Its proof uses
- [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|Theorem §26.6: The Chain Rule]]
- [[§26 Derivations and the Abstract Tangent Space#^lem-26-8|Lemma §26.8: Open Subsets Have the Same Abstract Tangent Spaces]]
- [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|Proposition §26.9: Charts Are Diffeomorphisms]]
- [[§28 The Differential in Coordinates#^thm-28-2|Theorem §28.2: The Matrix of the Differential]]
- [[§31 Local Diffeomorphisms#^thm-31-1|Theorem §31.1: Inverse Function Theorem]]
- [[§31 Local Diffeomorphisms#^def-31-1|Definition §31.1: Local Diffeomorphism]]

## Used in (Differentiable Manifolds)
- [[§31 Local Diffeomorphisms#^cor-31-3|Corollary §31.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms]]
- [[§32 Submersions#^prop-32-1|Proposition §32.1: Dimension Constraints]]
- [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|Theorem §39.8: The Double Cover SU(2) → SO(3)]]

## Connections
- **Used for.** Diffeomorphisms are exactly the bijective local diffeomorphisms ([[§31 Local Diffeomorphisms#^cor-31-3|§31.3]]), and a map between manifolds of equal dimension that is a submersion, or an immersion, at every point is a local diffeomorphism ([[§32 Submersions#^prop-32-1|§32.1]]). The same inverse-function step, with [[§32 Submersions#^lem-32-3|§32.3]], builds the new chart in the [[Submersion Normal Form]].
- **Local, not global.** t ↦ (cos t, sin t) on (0, 4π) is a local diffeomorphism onto S¹ that is neither injective nor a covering map: (1, 0) has one preimage and every other point two ([[§31 Local Diffeomorphisms#^ex-31-1|Ex. §31.1]], [[§31 Local Diffeomorphisms#^rem-31-2|Covering Maps]]). Injectivity is the entire difference from a diffeomorphism ([[§31 Local Diffeomorphisms#^rem-31-3|§31, Remark]]).
- **Same idea elsewhere.** The analytic input is the [[Inverse Function Theorem (several variables)]] of 452, applied to the coordinate representation, whose Jacobian is the matrix of F_*p ([[Matrix of the Differential]]). In 590, ℝ → S¹ is a covering map ([[§24 Covering Spaces#^thm-24-2|590 §24.2]]) while its restriction to (0, ∞) is a local homeomorphism that is not ([[§24 Covering Spaces#^ex-24-2|590 Ex. §24.2]]), the same failure as (0, 4π) → S¹.
