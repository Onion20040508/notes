---
subject: math
type: theorem
source: "[[Differentiable Manifolds]]"
aliases: ["MATH 591 35.2", "Lee Theorem 4.5", "Lee Proposition 4.8"]
tags: [differentiable-manifolds, hub]
---
![[§35 Local Diffeomorphisms#^thm-35-2]]

## Treated in
- [[§35 Local Diffeomorphisms#^thm-35-2|Theorem §35.2: Local Diffeomorphisms Are Detected by the Differential]], in [[§35 Local Diffeomorphisms]]

## Its proof uses
- [[§19 Smooth Functions and Smooth Maps#^prop-19-2|Proposition §19.2: Smoothness of a Map Does Not Depend on the Charts]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-3|Lemma §19.3: A Chart Mapped into a Given Chart]]
- [[§19 Smooth Functions and Smooth Maps#^prop-19-4|Proposition §19.4: The Two Notions of Diffeomorphism Agree]]
- [[§19 Smooth Functions and Smooth Maps#^lem-19-5|Lemma §19.5: Composition of Smooth Maps]]
- [[§21 Linear Algebra Toolkit#^prop-21-1|Proposition §21.1: Standing Facts from Linear Algebra]]
- [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6: The Chain Rule]]
- [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|Lemma §28.8: Open Subsets Have the Same Abstract Tangent Spaces]]
- [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9: Charts Are Diffeomorphisms]]
- [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|Theorem §29.9: Dimension of the Tangent Space]]
- [[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2: The Matrix of the Differential]]
- [[§35 Local Diffeomorphisms#^def-35-1|Definition §35.1: Local Diffeomorphism]]
- [[§35 Local Diffeomorphisms#^thm-35-1|Theorem §35.1: Inverse Function Theorem]]

## Used in (Differentiable Manifolds)
- [[§35 Local Diffeomorphisms#^cor-35-3|Corollary §35.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms]]
- [[§36 Submersions#^prop-36-1|Proposition §36.1: Dimension Constraints]]
- [[§46 SU(2) → SO(3)꞉ The Double Cover#^thm-46-4|Theorem §46.4: The Double Cover SU(2) → SO(3)]]

## Connections
- **Used for.** Diffeomorphisms are exactly the bijective local diffeomorphisms ([[§35 Local Diffeomorphisms#^cor-35-3|§35.3]]), and a map between manifolds of equal dimension that is a submersion, or an immersion, at every point is a local diffeomorphism ([[§36 Submersions#^prop-36-1|§36.1]]). The same inverse-function step, with [[§36 Submersions#^lem-36-5|§36.5]], builds the new chart in the [[Submersion Normal Form]].
- **Local, not global.** t ↦ (cos t, sin t) on (0, 4π) is a local diffeomorphism onto S¹ that is neither injective nor a covering map: (1, 0) has one preimage and every other point two ([[§35 Local Diffeomorphisms#^ex-35-1|Ex. §35.1]], [[§35 Local Diffeomorphisms#^rem-35-2|Covering Maps]]). Injectivity is the entire difference from a diffeomorphism ([[§35 Local Diffeomorphisms#^rem-35-3|§35, Remark]]).
- **Same idea elsewhere.** The analytic input is the [[Inverse Function Theorem (several variables)]] of 452, applied to the coordinate representation, whose Jacobian is the matrix of F_*p ([[Matrix of the Differential]]). In 590, ℝ → S¹ is a covering map ([[§31 Covering Spaces#^thm-31-2|590 §31.2]]) while its restriction to (0, ∞) is a local homeomorphism that is not ([[§31 Covering Spaces#^ex-31-2|590 Ex. §31.2]]), the same failure as (0, 4π) → S¹.
