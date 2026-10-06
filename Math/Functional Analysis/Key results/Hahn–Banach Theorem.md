---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 5.2", "Hahn-Banach", "Lax §3.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§5 Statement and Motivation#^thm-5-2]]

## Treated in
- [[§5 Statement and Motivation#^thm-5-2|Theorem §5.2: Hahn–Banach]], in [[§5 Statement and Motivation]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§6 Proof of the Hahn–Banach Theorem#^lem-6-1|Lemma §6.1: One-Step Extension]]
- [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|Theorem §6.2: Zorn's Lemma]]

## Used in (Functional Analysis)
- [[§8 The Hyperplane Separation Theorem#^thm-8-1|Theorem §8.1: Hyperplane Separation; Geometric Hahn–Banach]]
- [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|Theorem §9.2: Complex Hahn–Banach]]

## Connections
- **How.** All the analysis is in the [[One-Step Extension Lemma]]: extending by one dimension comes down to choosing one number L(x₀) in an interval, which is nonempty by subadditivity. [[Zorn's Lemma]] then says “repeat until done” on the pairs (Z, ℓ_Z), ordered by extension ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). In a separable normed space, ordinary induction along a countable dense sequence would do instead ([[§6 Proof of the Hahn–Banach Theorem#^rem-6-4|Remark §6]]).
- **Why a general p.** The theorem is stated for a positive homogeneous subadditive p rather than a norm, because the separation theorem takes p to be the gauge of a convex set ([[Hyperplane Separation Theorem]]). Every norm and every C‖·‖ is such a p ([[§11 Normed Linear Spaces#^prop-11-1|§11.1]](a)). The simplest use gives every nonzero vector a functional with a prescribed value there ([[§6 Proof of the Hahn–Banach Theorem#^ex-6-1|Ex. §6.1]]). The extension is not unique.
- **Used for.** The [[Hyperplane Separation Theorem]] and the [[Complex Hahn–Banach Theorem]]. The same Zorn pattern gives [[Every Subspace Has a Complement]].
- **Same idea elsewhere.** On ℝⁿ every functional is x ↦ a·x ([[§3 Linear Maps, Convexity, and Linear Functionals#^ex-3-2|Ex. §3.2]]), and on a finite-dimensional inner product space every functional is ⟨·, a⟩ ([[Riesz representation theorem]], LADR 6.42). On a Hilbert space the bounded functionals are identified by the [[Riesz Representation Theorem (Hilbert spaces)]]. On a bare linear space Hahn–Banach is the only device for producing functionals ([[§5 Statement and Motivation#^rem-5-4|Remark §5]]), and it is what guarantees there are enough of them ([[§6 Proof of the Hahn–Banach Theorem#^rem-6-1|Remark §6]]).
