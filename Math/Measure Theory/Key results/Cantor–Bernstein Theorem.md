---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 2.2", "Schröder–Bernstein"]
tags: [measure-theory, hub]
---
![[§2 The Cantor–Bernstein Theorem#^thm-2-2]]

## Treated in
- [[§2 The Cantor–Bernstein Theorem#^thm-2-2|Theorem §2.2: Cantor–Bernstein]], in [[§2 The Cantor–Bernstein Theorem]]

## Its proof uses
- [[§1 Countability and Set Theory#^def-1-3|Definition §1.3: Injective (One-to-One)]]
- [[§1 Countability and Set Theory#^def-1-4|Definition §1.4: Surjective (Onto)]]
- [[§1 Countability and Set Theory#^def-1-6|Definition §1.6: Bijection]]
- [[§1 Countability and Set Theory#^def-1-7|Definition §1.7: Equivalence of Sets]]
- [[§2 The Cantor–Bernstein Theorem#^lem-2-1|Lemma §2.1: Key Lemma for Cantor–Bernstein]]

## Used in (Measure Theory)
- (not cited later in the course)

## Connections
- **Proof idea.** The [[§2 The Cantor–Bernstein Theorem#^lem-2-1|Key Lemma]] (§2.1) splits X = A ⊔ Aᶜ and Y = B ⊔ Bᶜ with f(A) = B and g(Bᶜ) = Aᶜ. The bijection is f on A and g⁻¹ on Aᶜ.
- **Used for.** It proves A ∼ B from two injections without writing down a bijection. This is [[Measure Theory Problem-Solving Techniques#^rem-19-6|Technique 2: The Cantor–Bernstein Squeeze]], applied in HW1 ([[Measure Theory Problem-Solving Techniques#^ex-19-9|Ex. T2]]). The same kind of comparison gives the Cantor set the cardinality 2^ℵ₀ of ℝ ([[§14 The Vitali Set and the Cantor Set#^rem-14-7|Rem. §11.7]]).
- **Context.** ∼ is the “same size” relation of MATH 451 ([[§2 The Set ℚ of Rational Numbers#^def-2-7|451 Def. §2.7]]). Cantor–Bernstein makes “injects into” antisymmetric on sizes. [[Cantor's Theorem]] shows the injection X → 𝒫(X) can never be upgraded to a bijection.
- **Also proved in [[Logic and Proofs]]:** [[§14a Uncountable Sets#^thm-14a-4|250 Thm. §14a.4]] (elementary proof by chains C₀ = X − g(Y), Cₖ₊₁ = g(f(Cₖ))).
