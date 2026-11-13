---
type: chapter
subject: "[[Group Theory]]"
chapter: 11
tags: [chapter, group-theory]
---
# 11 Representations and Maschke's Theorem
↑ [[Group Theory]]

*Source: Lecture and Worksheet 13 (Mon Nov 2). Part II, Representation Theory, begins here.*

So far groups have acted on sets. Representation theory studies groups acting on vector spaces by linear maps. Many groups come to us this way ($GL_n(k)$, the symmetries of a cube acting on $\mathbb{R}^3$), and every action on a set produces one (the permutation representations of [[§61 Representations and Subrepresentations|§61]]). The lecture's remark: representation theory is good exercise because it mixes three kinds of objects, group elements, vectors and scalars, and one has to keep track of which is which.

The second step ([[§62 Direct Sums and Maschke's Theorem|§62]]) asks when a representation breaks into smaller ones. A subrepresentation puts all the matrices $\rho(g)$ in block triangular form; a complementary subrepresentation makes them block diagonal; and Maschke's theorem provides such a complement for every finite group over a field in which $|G| \neq 0$. Over $\mathbb{R}$ the proof is geometric ([[§63 Invariant Inner Products and Maschke over ℝ|§63]]): average an inner product over $G$ and take orthogonal complements; the same averaging shows that a finite group acts by orthogonal matrices in a suitable basis.

The third step ([[§65 Simple Representations|§65]]) names the pieces. A representation is simple if its only subrepresentations are $\{0\}$ and itself, irreducible if it is not a direct sum of two nonzero subrepresentations; under Maschke's hypotheses the two agree, and every finite-dimensional representation is a direct sum of simple ones. Unlike groups, whose simple pieces can be bonded together in many ways, representations simply add up, so the theory reduces to knowing the simple representations.

What the simple representations are is the subject of the next chapter, [[· 12 Characters|Characters]].

**Builds on:** [[· 4 Homomorphisms and Isomorphisms|4 Homomorphisms and Isomorphisms]] (1), [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (3), [[· 6 Group Actions, Cosets, and Lagrange's Theorem|6 Group Actions, Cosets, and Lagrange's Theorem]] (2), [[· 8 Normal Subgroups and Quotient Groups|8 Normal Subgroups and Quotient Groups]] (1), [[· 9 Commutators, Solvable Groups and the Sylow Theorems|9 Commutators, Solvable Groups and the Sylow Theorems]] (1)
**Used by:** [[· 12 Characters|12 Characters]] (35)
**Builds on (other subjects):** [[Linear Algebra]] (8)

## Sections
- [[§61 Representations and Subrepresentations]]
- [[§62 Direct Sums and Maschke's Theorem]]
- [[§63 Invariant Inner Products and Maschke over ℝ]]
- [[§64 Sesquilinear and Hermitian Forms]]
- [[§65 Simple Representations]]

## Central results
- [[Maschke's Theorem]] (§62.10)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|Lemma §62.5: An Idempotent Fixes Its Image]]: 17 later results
- [[§62 Direct Sums and Maschke's Theorem#^prop-62-6|Proposition §62.6: An Idempotent Splits the Space]]: 16 later results
- [[§63 Invariant Inner Products and Maschke over ℝ#^prop-63-5|Proposition §63.5: G Preserves the Averaged Inner Product]]: 16 later results
- [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|Proposition §62.1: Bases of a Direct Sum]]: 15 later results
