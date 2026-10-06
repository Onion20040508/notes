---
subject: math
type: theorem
source: "[[Measure Theory]]"
aliases: ["MATH 551 3.1"]
tags: [measure-theory, hub]
---
![[§3 Countability of Rationals and Unions#^prop-3-1]]

## Treated in
- [[§3 Countability of Rationals and Unions#^prop-3-1|Proposition §3.1: Countable Union of Countable Sets]], in [[§3 Countability of Rationals and Unions]]

## Its proof uses
- [[§1 Countability and Set Theory#^def-1-1|Definition §1.1: Countable Set]]
- [[§1 Countability and Set Theory#^thm-1-1|Theorem §1.1: Properties of Equivalence]]
- [[§1 Countability and Set Theory#^ex-1-3|Example §1.3: ℕ × ℕ ∼ ℕ]]
- [[§1 Countability and Set Theory#^def-1-8|Definition §1.8: Countable (Formal)]]

## Used in (Measure Theory)
- [[§3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2: ℚ is countable]]
- [[§4 Uncountability#^ex-4-2|Example §4.2: The interval [0,1] is uncountable]]
- [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3: Open Sets in ℝⁿ as Unions of Rectangles]]
- [[§10 Lebesgue Outer Measure#^prop-10-1|Proposition §10.1: Basic Properties of Outer Measure]]
- [[§28 Differentiation Theory#^thm-28-1|Theorem §28.1: Monotone Functions Have Countably Many Discontinuities]]
- [[§35 Lᵖ as a Banach Space#^cor-35-13|Corollary §35.13: Lᵖ is Separable for 1 ≤ p < ∞]]

## Connections
- **Proof idea.** List the n-th set as aₙ,₁, aₙ,₂, … and send aₙ,ₘ to (n, m). This puts the union in bijection with a subset of ℕ × ℕ, which is countable by the diagonal listing of [[§1 Countability and Set Theory#^ex-1-3|Ex. §1.3]].
- **Used for.** [[§3 Countability of Rationals and Unions#^cor-3-2|ℚ is countable]] (§3.2), the countably many dyadic cubes in [[§7 Structure of Open Sets#^prop-7-3|§7.3]], and the combined L-covering in countable subadditivity ([[Properties of Lebesgue Outer Measure]]). Later uses are [[§28 Differentiation Theory#^thm-28-1|Monotone Functions Have Countably Many Discontinuities]] (§18.1) and the [[§35 Lᵖ as a Banach Space#^cor-35-13|separability of Lᵖ]] (§19.20).
- **Measure analogue.** Countable subadditivity makes a countable union of null sets null, so every countable set is null ([[§10 Lebesgue Outer Measure#^ex-10-2|Ex. §10.2]]). The converse fails: the [[§14 The Vitali Set and the Cantor Set#^prop-14-7|Cantor set]] is uncountable and null.
- **Technique.** The “product + union closure” step of [[Measure Theory Problem-Solving Techniques#^rem-19-5|Technique 1: Reduction to Known Countability Results]]. MATH 451 proves ℚ countable by a diagonal listing instead ([[§2 The Set ℚ of Rational Numbers#^thm-2-5|451 §2.5]]).
- **Also proved in [[Logic and Proofs]]:** [[§14 Counting Infinite Sets#^ex-14-4|250 Ex. §14.4]] (elementary proof for a denumerable union of denumerable sets, first pairwise disjoint, then in general).
