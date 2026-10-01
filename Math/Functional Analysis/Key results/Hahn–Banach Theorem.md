---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 3.2", "Hahn-Banach", "Lax §3.1, Thm 1"]
tags: [functional-analysis, hub]
---
![[§3 Statement and Motivation#^thm-3-2]]

## Treated in
- [[§3 Statement and Motivation#^thm-3-2|Theorem §3.2: Hahn–Banach]], in [[§3 Statement and Motivation]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§4 Proof of the Hahn–Banach Theorem#^lem-4-1|Lemma §4.1: One-Step Extension]]
- [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|Theorem §4.2: Zorn's Lemma]]

## Used in (Functional Analysis)
- [[§4 Proof of the Hahn–Banach Theorem#^ex-4-1|Example §4.1: Extending from a Line]]
- [[§6 The Hyperplane Separation Theorem#^thm-6-1|Theorem §6.1: Hyperplane Separation; Geometric Hahn–Banach]]
- [[§7 The Complex Hahn–Banach Theorem#^thm-7-1|Theorem §7.1: Complex Hahn–Banach]]

## Connections
- **How.** All the analysis is in the [[One-Step Extension Lemma]]: extending by one dimension comes down to choosing one number L(x₀) in an interval, which is nonempty by subadditivity. [[Zorn's Lemma]] then says “repeat until done” on the pairs (Z, ℓ_Z), ordered by extension ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). In a separable normed space, ordinary induction along a countable dense sequence would do instead ([[§4 Proof of the Hahn–Banach Theorem#^rem-4-4|Remark §4]]).
- **Why a general p.** The theorem is stated for a positive homogeneous subadditive p rather than a norm, because the separation theorem takes p to be the gauge of a convex set ([[Hyperplane Separation Theorem]]). Every norm and every C‖·‖ is such a p ([[§8 Normed Linear Spaces#^prop-8-1|§8.1]](a)). The simplest use gives every nonzero vector a functional with a prescribed value there ([[§4 Proof of the Hahn–Banach Theorem#^ex-4-1|Ex. §4.1]]). The extension is not unique.
- **Used for.** The [[Hyperplane Separation Theorem]] and the [[Complex Hahn–Banach Theorem]]. The same Zorn pattern gives [[Every Subspace Has a Complement]].
- **Same idea elsewhere.** On ℝⁿ every functional is x ↦ a·x ([[§2 Linear Maps, Convexity, and Linear Functionals#^ex-2-2|Ex. §2.2]]), and on a finite-dimensional inner product space every functional is ⟨·, a⟩ ([[Riesz representation theorem]], LADR 6.42). On a Hilbert space the bounded functionals are identified by the [[Riesz Representation Theorem (Hilbert spaces)]]. On a bare linear space Hahn–Banach is the only device for producing functionals ([[§3 Statement and Motivation#^rem-3-4|Remark §3]]), and it is what guarantees there are enough of them ([[§4 Proof of the Hahn–Banach Theorem#^rem-4-1|Remark §4]]).
