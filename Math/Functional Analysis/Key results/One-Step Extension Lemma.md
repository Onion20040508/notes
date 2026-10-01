---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 4.1", "Lax §3.1, proof of Thm 1"]
tags: [functional-analysis, hub]
---
![[§4 Proof of the Hahn–Banach Theorem#^lem-4-1]]

## Treated in
- [[§4 Proof of the Hahn–Banach Theorem#^lem-4-1|Lemma §4.1: One-Step Extension]], in [[§4 Proof of the Hahn–Banach Theorem]]

## Its proof uses
- [[§1 Linear Spaces#^def-1-2|Definition §1.2: Linear Subspace]]
- [[§1 Linear Spaces#^def-1-5|Definition §1.5: Linear Span]]
- [[§3 Statement and Motivation#^def-3-1|Definition §3.1: Positive Homogeneous; Subadditive]]

## Its proof uses (other subjects)
- [[Completeness Axiom]] (Single Variable Analysis)

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **How.** A linear extension to span{x₀, Y} is fixed by the single number c = L(x₀). By positive homogeneity it suffices to check the multiples a = ±1, which gives the sandwich ℓ(y′) − p(y′ − x₀) ≤ c ≤ p(x₀ + y) − ℓ(y). The sandwich is nonempty because ℓ(y′) + ℓ(y) = ℓ(y′ + y) ≤ p((y′ − x₀) + (x₀ + y)) ≤ p(y′ − x₀) + p(x₀ + y). Taking c to be a supremum uses the [[Completeness Axiom]].
- **Why both signs.** Positive homogeneity pulls out only scalars a ≥ 0. So a > 0 reduces to a = 1 and a < 0 to a = −1, and neither case covers the other. The conditions must be turned into bounds on c by equivalences, not one-sided estimates ([[§4 Proof of the Hahn–Banach Theorem#^rem-4-3|Remark §4]]). Any c in the interval works, so the extension is not unique.
- **Used for.** It contains all the analysis of the [[Hahn–Banach Theorem]]; [[Zorn's Lemma]] only repeats it ([[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]]). The same one-step move enlarges a subspace that meets Y only in 0 ([[§1 Linear Spaces#^lem-1-7|§1.7]], for [[Every Subspace Has a Complement]]). It also adds x/‖x‖ to an orthonormal set ([[Existence of Orthonormal Bases]]).
