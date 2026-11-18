---
type: chapter
subject: "[[Group Theory]]"
chapter: 12
tags: [chapter, group-theory]
---
# 12 Characters
↑ [[Group Theory]]

*Source: Lecture and Worksheet 15 (Mon Nov 9); lecture and Worksheet 16 (Wed Nov 11); lecture (Fri Nov 13); lecture and Worksheet 17 (Mon Nov 16); lecture and Worksheet 18 (Wed Nov 18).*

By [[· 11 Representations and Maschke's Theorem|Chapter 11]], finite-dimensional representations of a finite group break into simple pieces (over $\mathbb{R}$, and over any field in which $|G| \neq 0$). This chapter ([[§66 Invariant Vectors|§66]], [[§67 Characters of Representations|§67]]) starts on the remaining question, what the simple representations are, with the main tool: the character $\chi_V(g) = \operatorname{Tr}\rho_V(g)$. A first use counts the vectors that $G$ fixes. Averaging over a finite group is an idempotent onto them, so they split off as a direct summand, and their number is the average of the character, exactly when the field contains $\mathbb{Q}$. For a permutation representation this count is Burnside's Lemma, and the same averaging, applied to an arbitrary idempotent onto a subrepresentation, is the proof of Maschke's theorem ([[§62 Direct Sums and Maschke's Theorem|§62]]). Characters are constant on conjugacy classes and add over direct sums, so they are recorded in a character table with one column per conjugacy class; despite the name, a character is a homomorphism only in dimension $1$, where it is a character in the sense of Chapter 9. Applied to the representation $\operatorname{Hom}(V, W)$, the same count gives the number of independent homomorphisms between two representations, $\dim \operatorname{Hom}_G(V, W) = \frac{1}{|G|}\sum_g \chi_V(g)\chi_W(g^{-1})$ ([[§68 Homomorphisms Between Representations|§68]]). The factor $\chi_V(g^{-1})$ in this count is the character of the dual representation $V^\vee$, on which $g$ acts by the inverse transpose of its matrix on $V$ ([[§69 Dual Representations|§69]]). Combined with the decomposition into simple representations, the count becomes a dot product of multiplicities: by Schur's Lemma, non-isomorphic simple representations admit only the zero homomorphism, and over $\mathbb{C}$ the homomorphisms from a simple representation to itself are the multiples of the identity ([[§70 Schur's Lemma and Multiplicities|§70]]). In the character table, with one column per conjugacy class and one row per simple representation, this says that the rows are orthogonal for a pairing of class functions; hence they are linearly independent, and there are at most as many simple representations as conjugacy classes ([[§71 The Character Table|§71]]).

**Builds on:** [[· 1 Groups and Subgroups|1 Groups and Subgroups]] (1), [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (1), [[· 6 Group Actions, Cosets, and Lagrange's Theorem|6 Group Actions, Cosets, and Lagrange's Theorem]] (8), [[· 7 Conjugacy and the Center|7 Conjugacy and the Center]] (13), [[· 11 Representations and Maschke's Theorem|11 Representations and Maschke's Theorem]] (69)
**Used by:** —
**Builds on (other subjects):** [[Linear Algebra]] (2)

## Sections
- [[§66 Invariant Vectors]]
- [[§67 Characters of Representations]]
- [[§68 Homomorphisms Between Representations]]
- [[§69 Dual Representations]]
- [[§70 Schur's Lemma and Multiplicities]]
- [[§71 The Character Table]]

## Central results
- [[Dimension of the Invariants]] (§66.10)
- [[Dimension of Hom_G(V, W)]] (§68.6)
- [[Schur's Lemma]] (§70.5)
- [[Orthogonality of Characters]] (§71.5)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§66 Invariant Vectors#^prop-66-6|Proposition §66.6: The Image of the Average Is the Invariants]]: 18 later results
- [[§66 Invariant Vectors#^prop-66-7|Proposition §66.7: The Average Is Idempotent]]: 17 later results
- [[§66 Invariant Vectors#^prop-66-4|Proposition §66.4: The Trace of an Idempotent]]: 16 later results
- [[Dimension of the Invariants|Theorem §66.10: Dimension of the Invariants]]: 15 later results
