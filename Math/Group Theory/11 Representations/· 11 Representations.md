---
type: chapter
subject: "[[Group Theory]]"
chapter: 11
tags: [chapter, group-theory]
---
# 11 Representations
↑ [[Group Theory]]

*Source: Lecture and Worksheet 13 (Mon Nov 2). Part II, Representation Theory, begins here.*

So far groups have acted on sets. Representation theory studies groups acting on vector spaces by linear maps. Many groups come to us this way ($GL_n(k)$, the symmetries of a cube acting on $\mathbb{R}^3$), and every action on a set produces one (the permutation representations of [[§59 Representations and Subrepresentations|§59]]). The lecture's remark: representation theory is good exercise because it mixes three kinds of objects, group elements, vectors and scalars, and one has to keep track of which is which.

The second step ([[§60 Direct Sums and Maschke's Theorem|§60]]) asks when a representation breaks into smaller ones. A subrepresentation puts all the matrices $\rho(g)$ in block triangular form; a complementary subrepresentation makes them block diagonal; and Maschke's theorem provides such a complement for every finite group over a field in which $|G| \neq 0$. Over $\mathbb{R}$ the proof is geometric ([[§61 Invariant Inner Products and Maschke over ℝ|§61]]): average an inner product over $G$ and take orthogonal complements; the same averaging shows that a finite group acts by orthogonal matrices in a suitable basis.

The third step ([[§63 Simple Representations|§63]]) names the pieces. A representation is simple if its only subrepresentations are $\{0\}$ and itself, irreducible if it is not a direct sum of two nonzero subrepresentations; under Maschke's hypotheses the two agree, and every finite-dimensional representation is a direct sum of simple ones. Unlike groups, whose simple pieces can be bonded together in many ways, representations simply add up, so the theory reduces to knowing the simple representations.

The fourth step ([[§64 Invariant Vectors|§64]] and [[§65 Characters of Representations|§65]]) starts on the remaining question, what the simple representations are, with the main tool: the character $\chi_V(g) = \operatorname{Tr}\rho_V(g)$. A first use counts the vectors that $G$ fixes. Averaging over a finite group is an idempotent onto them, so they split off as a direct summand, and their number is the average of the character, exactly when the field contains $\mathbb{Q}$. For a permutation representation this count is Burnside's Lemma, and the same averaging, applied to an arbitrary idempotent onto a subrepresentation, is the proof of Maschke's theorem ([[§60 Direct Sums and Maschke's Theorem|§60]]). Characters are constant on conjugacy classes and add over direct sums, so they are recorded in a character table with one column per conjugacy class; despite the name, a character is a homomorphism only in dimension $1$, where it is a character in the sense of Chapter 9.

**Builds on:** [[· 4 Homomorphisms and Isomorphisms|4 Homomorphisms and Isomorphisms]] (1), [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (3), [[· 6 Group Actions, Cosets, and Lagrange's Theorem|6 Group Actions, Cosets, and Lagrange's Theorem]] (2), [[· 7 Conjugacy and the Center|7 Conjugacy and the Center]] (1), [[· 8 Normal Subgroups and Quotient Groups|8 Normal Subgroups and Quotient Groups]] (1), [[· 9 Commutators, Solvable Groups and the Sylow Theorems|9 Commutators, Solvable Groups and the Sylow Theorems]] (1)
**Used by:** —
**Builds on (other subjects):** [[Linear Algebra]] (5)

## Sections
- [[§59 Representations and Subrepresentations]]
- [[§60 Direct Sums and Maschke's Theorem]]
- [[§61 Invariant Inner Products and Maschke over ℝ]]
- [[§62 Sesquilinear and Hermitian Forms]]
- [[§63 Simple Representations]]
- [[§64 Invariant Vectors]]
- [[§65 Characters of Representations]]

## Central results
- [[Maschke's Theorem]] (§60.10)
- [[Dimension of the Invariants]] (§64.10)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§60 Direct Sums and Maschke's Theorem#^lem-60-5|Lemma §60.5: An Idempotent Fixes Its Image]]: 11 later results
- [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|Proposition §60.6: An Idempotent Splits the Space]]: 10 later results
- [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|Proposition §61.5: G Preserves the Averaged Inner Product]]: 10 later results
- [[§60 Direct Sums and Maschke's Theorem#^prop-60-1|Proposition §60.1: Bases of a Direct Sum]]: 9 later results
