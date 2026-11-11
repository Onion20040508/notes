---
type: chapter
subject: "[[Group Theory]]"
chapter: 12
tags: [chapter, group-theory]
---
# 12 Characters
↑ [[Group Theory]]

*Source: Lecture and Worksheet 15 (Mon Nov 9); Worksheet 16.*

By [[· 11 Representations and Maschke's Theorem|Chapter 11]], finite-dimensional representations of a finite group break into simple pieces (over $\mathbb{R}$, and over any field in which $|G| \neq 0$). This chapter ([[§66 Invariant Vectors|§66]], [[§67 Characters of Representations|§67]]) starts on the remaining question, what the simple representations are, with the main tool: the character $\chi_V(g) = \operatorname{Tr}\rho_V(g)$. A first use counts the vectors that $G$ fixes. Averaging over a finite group is an idempotent onto them, so they split off as a direct summand, and their number is the average of the character, exactly when the field contains $\mathbb{Q}$. For a permutation representation this count is Burnside's Lemma, and the same averaging, applied to an arbitrary idempotent onto a subrepresentation, is the proof of Maschke's theorem ([[§62 Direct Sums and Maschke's Theorem|§62]]). Characters are constant on conjugacy classes and add over direct sums, so they are recorded in a character table with one column per conjugacy class; despite the name, a character is a homomorphism only in dimension $1$, where it is a character in the sense of Chapter 9. Applied to the representation $\operatorname{Hom}(V, W)$, the same count gives the number of independent homomorphisms between two representations, $\dim \operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_g \chi_V(g)\chi_W(g^{-1})$ ([[§68 Homomorphisms Between Representations|§68]]).

**Builds on:** [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (1), [[· 6 Group Actions, Cosets, and Lagrange's Theorem|6 Group Actions, Cosets, and Lagrange's Theorem]] (4), [[· 7 Conjugacy and the Center|7 Conjugacy and the Center]] (4), [[· 11 Representations and Maschke's Theorem|11 Representations and Maschke's Theorem]] (30)
**Used by:** —
**Builds on (other subjects):** —

## Sections
- [[§66 Invariant Vectors]]
- [[§67 Characters of Representations]]
- [[§68 Homomorphisms Between Representations]]

## Central results
- [[Dimension of the Invariants]] (§66.10)
- [[Dimension of Hom_G(V, W)]] (§68.6)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§66 Invariant Vectors#^prop-66-1|Proposition §66.1: The Trace of a Product in Either Order]]: 8 later results
- [[§66 Invariant Vectors#^prop-66-6|Proposition §66.6: The Image of the Average Is the Invariants]]: 7 later results
- [[§66 Invariant Vectors#^cor-66-2|Corollary §66.2: Conjugate Matrices Have the Same Trace]]: 6 later results
- [[§66 Invariant Vectors#^prop-66-7|Proposition §66.7: The Average Is Idempotent]]: 6 later results
