---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 4.1", "uncountability of ℝ"]
tags: [measure-theory, hub]
---
![[Measure Theory §4 Uncountability#^thm-4-1]]

## Treated in
- [[Measure Theory §4 Uncountability#^thm-4-1|Theorem §4.1: Cantor's Theorem]], in [[Measure Theory §4 Uncountability]]

## Its proof uses
- [[Measure Theory §1 Countability and Set Theory#^def-1-4|Definition §1.4: Surjective (Onto)]]
- [[Measure Theory §1 Countability and Set Theory#^def-1-6|Definition §1.6: Bijection]]
- [[Measure Theory §4 Uncountability#^def-4-1|Definition §4.1: Power Set]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** The diagonal set A = {x : x ∉ f(x)} differs from every f(y), so no map X → 𝒫(X) is onto. It is the same diagonal trick that shows the [[Measure Theory §4 Uncountability#^ex-4-1|binary sequences are uncountable]] (Ex. §4.1).
- **Size of ℝ.** For X = ℕ, subsets of ℕ correspond to binary sequences via indicator functions, so 𝒫(ℕ) is uncountable. Binary expansion then gives [[Measure Theory §4 Uncountability#^ex-4-2|Ex. §4.2]]: [0, 1] is uncountable. MATH 451 uses this for the [[Single Variable Analysis §2 The Set ℚ of Rational Numbers#^thm-2-7|existence of transcendental numbers]] (451 §2.7).
- **Strict growth.** x ↦ {x} injects X into 𝒫(X), so |X| < |𝒫(X)|. It is the strict counterpart of the [[Cantor–Bernstein Theorem]], which turns injections both ways into a bijection.
- **In the course.** It is not cited later. The uncountability results that are used later come from Ex. §4.2: the [[Measure Theory §11 Borel Sets and Measure Spaces#^prop-11-21|Cantor set]] is uncountable but null (§11.21), and [[Measure Theory §19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-21|L∞ is not separable]] (§19.21).
