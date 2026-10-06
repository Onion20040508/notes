---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 33.2", "Lee Theorem 4.5", "Lee Proposition 4.8"]
tags: [differentiable-manifolds, hub]
---
![[§33 Local Diffeomorphisms#^thm-33-2]]

## Treated in
- [[§33 Local Diffeomorphisms#^thm-33-2|Theorem §33.2: Local Diffeomorphisms Are Detected by the Differential]], in [[§33 Local Diffeomorphisms]]

## Its proof uses
- [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6: The Chain Rule]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|Lemma §28.8: Open Subsets Have the Same Abstract Tangent Spaces]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§33 Local Diffeomorphisms#^def-33-1|Definition §33.1: Local Diffeomorphism]]
- [[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1: Inverse Function Theorem]]

## Used in (Differentiable Manifolds)
- [[§33 Local Diffeomorphisms#^cor-33-3|Corollary §33.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms]]
- [[§34 Submersions#^prop-34-1|Proposition §34.1: Dimension Constraints]]
- [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|Theorem §41.4: The Double Cover SU(2) → SO(3)]]

## Connections
- **Used for.** Diffeomorphisms are exactly the bijective local diffeomorphisms ([[§33 Local Diffeomorphisms#^cor-33-3|§33.3]]), and a map between manifolds of equal dimension that is a submersion, or an immersion, at every point is a local diffeomorphism ([[§34 Submersions#^prop-34-1|§34.1]]). The same inverse-function step, with [[§34 Submersions#^lem-34-3|§34.3]], builds the new chart in the [[Submersion Normal Form]].
- **Local, not global.** t ↦ (cos t, sin t) on (0, 4π) is a local diffeomorphism onto S¹ that is neither injective nor a covering map: (1, 0) has one preimage and every other point two ([[§33 Local Diffeomorphisms#^ex-33-1|Ex. §33.1]], [[§33 Local Diffeomorphisms#^rem-33-2|Covering Maps]]). Injectivity is the entire difference from a diffeomorphism ([[§33 Local Diffeomorphisms#^rem-33-3|§33, Remark]]).
- **Same idea elsewhere.** The analytic input is the [[Inverse Function Theorem (several variables)]] of 452, applied to the coordinate representation, whose Jacobian is the matrix of F_*p ([[Matrix of the Differential]]). In 590, ℝ → S¹ is a covering map ([[§31 Covering Spaces#^thm-31-2|590 §31.2]]) while its restriction to (0, ∞) is a local homeomorphism that is not ([[§31 Covering Spaces#^ex-31-2|590 Ex. §31.2]]), the same failure as (0, 4π) → S¹.
