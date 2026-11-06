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

The third step ([[§62 Simple Representations|§62]]) names the pieces. A representation is simple if its only subrepresentations are $\{0\}$ and itself, irreducible if it is not a direct sum of two nonzero subrepresentations; under Maschke's hypotheses the two agree, and every finite-dimensional representation is a direct sum of simple ones. Unlike groups, whose simple pieces can be bonded together in many ways, representations simply add up, so the theory reduces to knowing the simple representations.

**Builds on:** [[· 4 Homomorphisms and Isomorphisms|4 Homomorphisms and Isomorphisms]] (1), [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (3), [[· 6 Group Actions, Cosets, and Lagrange's Theorem|6 Group Actions, Cosets, and Lagrange's Theorem]] (1), [[· 8 Normal Subgroups and Quotient Groups|8 Normal Subgroups and Quotient Groups]] (1), [[· 9 Commutators, Solvable Groups and the Sylow Theorems|9 Commutators, Solvable Groups and the Sylow Theorems]] (1)
**Used by:** —
**Builds on (other subjects):** [[Linear Algebra]] (5)

## Sections
- [[§59 Representations and Subrepresentations]]
- [[§60 Direct Sums and Maschke's Theorem]]
- [[§61 Invariant Inner Products and Maschke over ℝ]]
- [[§62 Simple Representations]]

## Central results
- [[Maschke's Theorem]] (§60.4)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-1|Proposition §61.1: Direct Sum of a Subspace and Its Orthogonal Complement]]: 5 later results
- [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-2|Proposition §61.2: Orthogonal Complements of Subrepresentations]]: 5 later results
- [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|Proposition §61.4: Averaging Gives an Inner Product]]: 5 later results
- [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|Proposition §61.5: G Preserves the Averaged Inner Product]]: 5 later results
