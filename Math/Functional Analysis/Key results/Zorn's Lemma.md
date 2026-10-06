---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 5.2", "Zorn", "Lax §3.1, proof of Thm 1"]
tags: [functional-analysis, hub]
---
![[§6 Proof of the Hahn–Banach Theorem#^thm-6-2]]

## Treated in
- [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|Theorem §6.2: Zorn's Lemma]], in [[§6 Proof of the Hahn–Banach Theorem]]

## Its proof uses
- (no proof in the notes)

## Used in (Functional Analysis)
- [[§28 Existence of Orthonormal Bases and Separability#^thm-28-1|Theorem §28.1: Existence of Orthonormal Bases]]

## Connections
- **Status.** It is equivalent to the axiom of choice and is taken as an axiom, with no proof. It says “repeat until finished” in a form that is legitimate when X has uncountable dimension ([[§6 Proof of the Hahn–Banach Theorem#^rem-6-4|Remark §5]]).
- **Used for.** It is used three times, always in the same pattern ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). For the [[Hahn–Banach Theorem]] the objects are pairs (Z, ℓ_Z), extended by the [[One-Step Extension Lemma]]. For [[Every Subspace Has a Complement]] they are subspaces meeting Y in 0. For [[Existence of Orthonormal Bases]] they are orthonormal sets. In each case the union of a chain is an upper bound, because any finitely many elements lie in a single member.
- **When it is not needed.** In finite dimensions, apply the one-step lemma finitely many times ([[§2 Quotient Spaces and Complements#^rem-2-3|Remark §1]]); LADR gets complements by extending a basis ([[§5 Bases#^ladr-2-33|LADR 2.33]]). In a separable normed space, ordinary induction along a countable dense sequence suffices for Hahn–Banach ([[§6 Proof of the Hahn–Banach Theorem#^rem-6-4|Remark §5]]), and Gram–Schmidt for orthonormal bases ([[Separable Hilbert Spaces Have Countable Orthonormal Bases]]).
- **Same idea elsewhere.** The axiom of choice also builds the Vitali set, the only non-measurable set in 551 ([[§14 The Vitali Set and the Cantor Set#^rem-14-6|551 Rem. §11.6]], [[The Vitali Set is Not Measurable]]).
