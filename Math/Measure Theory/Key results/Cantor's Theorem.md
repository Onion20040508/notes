---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 4.1", "X is not equivalent to its power set"]
tags: [measure-theory, hub]
---
![[§4 Uncountability#^thm-4-1]]

## Treated in
- [[§4 Uncountability#^thm-4-1|Theorem §4.1: Cantor's Theorem]], in [[§4 Uncountability]]

## Its proof uses
- [[§1 Countability and Set Theory#^def-1-4|Definition §1.4: Surjective (Onto)]]
- [[§1 Countability and Set Theory#^def-1-6|Definition §1.6: Bijection]]
- [[§4 Uncountability#^def-4-1|Definition §4.1: Power Set]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** The diagonal set A = {x : x ∉ f(x)} differs from every f(y), so no map X → 𝒫(X) is onto. It is the same diagonal trick that shows the [[§4 Uncountability#^ex-4-1|binary sequences are uncountable]] (Ex. §4.1).
- **Size of ℝ.** For X = ℕ, subsets of ℕ correspond to binary sequences via indicator functions, so 𝒫(ℕ) is uncountable. Binary expansion then gives [[§4 Uncountability#^ex-4-2|Ex. §4.2]]: [0, 1] is uncountable. MATH 451 uses this for the [[§2 The Set ℚ of Rational Numbers#^thm-2-7|existence of transcendental numbers]] (451 §2.7).
- **Strict growth.** x ↦ {x} injects X into 𝒫(X), so |X| < |𝒫(X)|. It is the strict counterpart of the [[Cantor–Bernstein Theorem]], which turns injections both ways into a bijection.
- **In the course.** It is not cited later. The uncountability results that are used later come from Ex. §4.2: the [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Cantor set]] is uncountable but null (§11.21), and [[§35 Lᵖ as a Banach Space#^thm-35-14|L∞ is not separable]] (§19.21).
- **Also proved in [[Logic and Proofs]]:** [[§14a Uncountable Sets#^thm-14a-3|250 Thm. §14a.3]] (elementary proof with the same diagonal set, and |X| ≤ |𝒫(X)| via singletons).
