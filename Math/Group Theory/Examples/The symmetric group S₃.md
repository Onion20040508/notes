---
subject: math
type: example
source: "[[Group Theory]]"
tags: ["math493", "workhorse"]
---
The symmetric group $S_3$ of all permutations of $\{1, 2, 3\}$: six elements, namely the identity, the three transpositions and the two $3$-cycles. It is the smallest non-abelian group, so it is the first place to test any statement that might secretly need commutativity: cancellation with mixed sides, generated subgroups, left versus right cosets, normality, characters. Everything about it is computed by hand: the multiplication table, the six subgroups, the class equation $6 = 1 + 3 + 2$, and the normal subgroup $A_3$ with $S_3/A_3 \cong \mathbb{Z}/2\mathbb{Z}$. Its uses in MATH 493:

- The mixed hypothesis $gh_1 = h_2g$ does not cancel ([[Group Theory §2 First Consequences of the Axioms#^ex-2-1|§2]])
- $(gh)^2 \neq g^2h^2$ and $(gh)^{-1} \neq g^{-1}h^{-1}$ for two transpositions ([[Group Theory §4 Subgroups#^rem-4-1|§4]])
- Products of powers of the generators in a fixed order do not give $\langle g_1, g_2 \rangle$ ([[Group Theory §4 Subgroups#^ex-4-1|§4]])
- Elements in two-line and cycle notation, non-commutativity, and the multiplication table ([[Group Theory §10 Cycle Notation and the Group S₃#^ex-10-1|§10]])
- The mixed hypothesis revisited: conjugation relabels a transposition ([[Group Theory §12 Multiplying and Conjugating Cycles#^ex-12-2|§12]])
- $S_3$ has exactly six subgroups ([[Group Theory §13 Subgroups of S₃#^prop-13-1|§13]])
- The subgroup lattice: orders $1, 2, 3, 6$ all divide $6$ ([[Group Theory §13 Subgroups of S₃#^rem-13-1|§13]])
- The multiplication table as a worksheet problem (WS 2.4) ([[Group Theory §14 Multiplication Tables#^ex-14-5|§14]])
- $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$, since one is abelian and the other is not ([[Group Theory §16 Isomorphisms#^prop-16-3|§16]])
- The trivial center re-proves $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$ ([[Group Theory §16 Isomorphisms#^rem-16-4|§16]])
- $S_3$ permuting three variables: $x_1x_2 + x_2x_3 + x_1x_3$ is symmetric ([[Group Theory §19 Polynomial Rings, Permutation Matrices, and Representations#^ex-19-1|§19]])
- The permutation matrices of $(1\,2\,3)$ and $(1\,2)$ ([[Group Theory §19 Polynomial Rings, Permutation Matrices, and Representations#^ex-19-2|§19]])
- $\mathbb{Z}/3\mathbb{Z}$ rotating a triangle maps onto $A_3 \leq S_3$ ([[Group Theory §23 Actions#^ex-23-3|§23]])
- Left and right cosets of $\langle (1\,2) \rangle$ differ ([[Group Theory §26 Left and Right Cosets#^ex-26-1|§26]])
- The map $gH \mapsto Hg$ is not well defined ([[Group Theory §26 Left and Right Cosets#^ex-26-2|§26]])
- Cosets of the point stabilizer, read off from $\alpha(3)$ and $\alpha^{-1}(3)$ ([[Group Theory §28 Orbit–Stabilizer#^ex-28-2|§28]])
- Burnside's lemma: one orbit on $\{1, 2, 3\}$, three conjugacy classes ([[Group Theory §28 Orbit–Stabilizer#^ex-28-3|§28]])
- Three conjugacy classes, of sizes $1, 3, 2$ ([[Group Theory §31 Conjugacy Classes#^ex-31-2|§31]])
- The class equation $6 = 1 + 3 + 2$ and the trivial center ([[Group Theory §32 Conjugation as an Action and the Class Equation#^ex-32-1|§32]])
- A group with exactly three conjugacy classes has order $3$ or $6$, and $S_3$ occurs ([[Group Theory §32 Conjugation as an Action and the Class Equation#^cor-32-7|§32]])
- $\langle (1\,2) \rangle$ is not normal ([[Group Theory §35 Normal Subgroups#^ex-35-1|§35]])
- $A_3 = \langle (1\,2\,3) \rangle$ has index $2$, hence is normal ([[Group Theory §36 Sources of Normal Subgroups#^ex-36-1|§36]])
- The inclusion of $\langle (1\,2) \rangle$: images need not be normal ([[Group Theory §36 Sources of Normal Subgroups#^prop-36-3|§36]])
- The normal subgroups $\{e\}$, $A_3$, $S_3$ as unions of conjugacy classes ([[Group Theory §36 Sources of Normal Subgroups#^ex-36-3|§36]])
- $S_3/A_3$ is cyclic of order $2$ ([[Group Theory §37 Quotient Groups#^ex-37-1|§37]])
- $S_3$ as the quotient $S_4/V$ ([[Group Theory §39 Simple Groups#^prop-39-10|§39]])
- $PSL_2(\mathbb{F}_2) \cong S_3$, which is not simple ([[Group Theory §39 Simple Groups#^ex-39-3|§39]])
- The identity $S_3 \to S_3$ is not constant on conjugacy classes, so characters need an abelian target ([[Group Theory §40 Characters#^rem-40-3|§40]])

## The mixed hypothesis $gh_1 = h_2g$ does not cancel
![[Group Theory §2 First Consequences of the Axioms#^ex-2-1]]

## $(gh)^2 \neq g^2h^2$ and $(gh)^{-1} \neq g^{-1}h^{-1}$ for two transpositions
![[Group Theory §4 Subgroups#^rem-4-1]]

## Products of powers of the generators in a fixed order do not give $\langle g_1, g_2 \rangle$
![[Group Theory §4 Subgroups#^ex-4-1]]

## Elements in two-line and cycle notation, non-commutativity, and the multiplication table
![[Group Theory §10 Cycle Notation and the Group S₃#^ex-10-1]]

## The mixed hypothesis revisited: conjugation relabels a transposition
![[Group Theory §12 Multiplying and Conjugating Cycles#^ex-12-2]]

## $S_3$ has exactly six subgroups
![[Group Theory §13 Subgroups of S₃#^prop-13-1]]

## The subgroup lattice: orders $1, 2, 3, 6$ all divide $6$
![[Group Theory §13 Subgroups of S₃#^rem-13-1]]

## The multiplication table as a worksheet problem (WS 2.4)
![[Group Theory §14 Multiplication Tables#^ex-14-5]]

## $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$, since one is abelian and the other is not
![[Group Theory §16 Isomorphisms#^prop-16-3]]

## The trivial center re-proves $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$
![[Group Theory §16 Isomorphisms#^rem-16-4]]

## $S_3$ permuting three variables: $x_1x_2 + x_2x_3 + x_1x_3$ is symmetric
![[Group Theory §19 Polynomial Rings, Permutation Matrices, and Representations#^ex-19-1]]

## The permutation matrices of $(1\,2\,3)$ and $(1\,2)$
![[Group Theory §19 Polynomial Rings, Permutation Matrices, and Representations#^ex-19-2]]

## $\mathbb{Z}/3\mathbb{Z}$ rotating a triangle maps onto $A_3 \leq S_3$
![[Group Theory §23 Actions#^ex-23-3]]

## Left and right cosets of $\langle (1\,2) \rangle$ differ
![[Group Theory §26 Left and Right Cosets#^ex-26-1]]

## The map $gH \mapsto Hg$ is not well defined
![[Group Theory §26 Left and Right Cosets#^ex-26-2]]

## Cosets of the point stabilizer, read off from $\alpha(3)$ and $\alpha^{-1}(3)$
![[Group Theory §28 Orbit–Stabilizer#^ex-28-2]]

## Burnside's lemma: one orbit on $\{1, 2, 3\}$, three conjugacy classes
![[Group Theory §28 Orbit–Stabilizer#^ex-28-3]]

## Three conjugacy classes, of sizes $1, 3, 2$
![[Group Theory §31 Conjugacy Classes#^ex-31-2]]

## The class equation $6 = 1 + 3 + 2$ and the trivial center
![[Group Theory §32 Conjugation as an Action and the Class Equation#^ex-32-1]]

## A group with exactly three conjugacy classes has order $3$ or $6$, and $S_3$ occurs
![[Group Theory §32 Conjugation as an Action and the Class Equation#^cor-32-7]]

## $\langle (1\,2) \rangle$ is not normal
![[Group Theory §35 Normal Subgroups#^ex-35-1]]

## $A_3 = \langle (1\,2\,3) \rangle$ has index $2$, hence is normal
![[Group Theory §36 Sources of Normal Subgroups#^ex-36-1]]

## The inclusion of $\langle (1\,2) \rangle$: images need not be normal
![[Group Theory §36 Sources of Normal Subgroups#^prop-36-3]]

## The normal subgroups $\{e\}$, $A_3$, $S_3$ as unions of conjugacy classes
![[Group Theory §36 Sources of Normal Subgroups#^ex-36-3]]

## $S_3/A_3$ is cyclic of order $2$
![[Group Theory §37 Quotient Groups#^ex-37-1]]

## $S_3$ as the quotient $S_4/V$
![[Group Theory §39 Simple Groups#^prop-39-10]]

## $PSL_2(\mathbb{F}_2) \cong S_3$, which is not simple
![[Group Theory §39 Simple Groups#^ex-39-3]]

## The identity $S_3 \to S_3$ is not constant on conjugacy classes, so characters need an abelian target
![[Group Theory §40 Characters#^rem-40-3]]
