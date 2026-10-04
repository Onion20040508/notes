---
subject: math
type: example
source: "[[Group Theory]]"
tags: ["math493", "workhorse"]
---
The symmetric group $S_3$ of all permutations of $\{1, 2, 3\}$: six elements, namely the identity, the three transpositions and the two $3$-cycles. It is the smallest non-abelian group, so it is the first place to test any statement that might secretly need commutativity: cancellation with mixed sides, generated subgroups, left versus right cosets, normality, characters. Everything about it is computed by hand: the multiplication table, the six subgroups, the class equation $6 = 1 + 3 + 2$, and the normal subgroup $A_3$ with $S_3/A_3 \cong \mathbb{Z}/2\mathbb{Z}$. Its uses in MATH 493:

- The mixed hypothesis $gh_1 = h_2g$ does not cancel ([[§2 First Consequences of the Axioms#^ex-2-1|§2]])
- $(gh)^2 \neq g^2h^2$ and $(gh)^{-1} \neq g^{-1}h^{-1}$ for two transpositions ([[§4 Subgroups#^rem-4-1|§4]])
- Products of powers of the generators in a fixed order do not give $\langle g_1, g_2 \rangle$ ([[§4 Subgroups#^ex-4-1|§4]])
- $S_3$ is the smallest group in which the fixed-order products fail ([[§4 Subgroups#^rem-4-2|§4]])
- Elements in two-line and cycle notation, non-commutativity, and the multiplication table ([[§10 Cycle Notation and the Group S₃#^ex-10-1|§10]])
- $S_3$ has exactly six subgroups ([[§13 The Symmetric Group S₃#^prop-13-1|§13]])
- The subgroup lattice: orders $1, 2, 3, 6$ all divide $6$ ([[§13 The Symmetric Group S₃#^rem-13-1|§13]])
- The mixed hypothesis revisited: conjugation relabels a transposition ([[§13 The Symmetric Group S₃#^ex-13-1|§12]])
- The multiplication table as a worksheet problem (WS 2.4) ([[§14 Multiplication Tables#^ex-14-5|§14]])
- $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$, since one is abelian and the other is not ([[§16 Isomorphisms#^prop-16-3|§16]])
- The trivial center re-proves $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$ ([[§16 Isomorphisms#^rem-16-4|§16]])
- $S_3$ permuting three variables: $x_1x_2 + x_2x_3 + x_1x_3$ is symmetric ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-1|§19]])
- The permutation matrices of $(1\,2\,3)$ and $(1\,2)$ ([[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-2|§19]])
- $\mathbb{Z}/3\mathbb{Z}$ rotating a triangle maps onto $A_3 \leq S_3$ ([[§25 Actions#^ex-25-3|§23]])
- Left and right cosets of $\langle (1\,2) \rangle$ differ ([[§28 Left and Right Cosets#^ex-28-1|§26]])
- The map $gH \mapsto Hg$ is not well defined ([[§28 Left and Right Cosets#^ex-28-2|§26]])
- Cosets of the point stabilizer, read off from $\alpha(3)$ and $\alpha^{-1}(3)$ ([[§30 Orbit–Stabilizer#^ex-30-2|§28]])
- Burnside's lemma: one orbit on $\{1, 2, 3\}$, three conjugacy classes ([[§30 Orbit–Stabilizer#^ex-30-3|§28]])
- Three conjugacy classes, of sizes $1, 3, 2$ ([[§33 Conjugacy Classes#^ex-33-2|§31]])
- The class equation $6 = 1 + 3 + 2$ and the trivial center ([[§34 Conjugation as an Action and the Class Equation#^ex-34-1|§32]])
- A group with exactly three conjugacy classes has order $3$ or $6$, and $S_3$ occurs ([[§34 Conjugation as an Action and the Class Equation#^cor-34-7|§32]])
- $\langle (1\,2) \rangle$ is not normal ([[§38 Normal Subgroups#^ex-38-1|§35]])
- $A_3 = \langle (1\,2\,3) \rangle$ has index $2$, hence is normal ([[§39 Sources of Normal Subgroups#^ex-39-1|§36]])
- The inclusion of $\langle (1\,2) \rangle$: images need not be normal ([[§39 Sources of Normal Subgroups#^prop-39-3|§36]])
- The normal subgroups $\{e\}$, $A_3$, $S_3$ as unions of conjugacy classes ([[§39 Sources of Normal Subgroups#^ex-39-3|§36]])
- $S_3/A_3$ is cyclic of order $2$ ([[§40 Quotient Groups#^ex-40-1|§37]])
- $S_3/A_3$ computed with the representatives $\{e, (2\,3)\}$ ([[§40 Quotient Groups#^ex-40-3|§37]])
- The representatives $\{e, (2\,3)\}$ form a subgroup, so $S_3/A_3 \cong \langle (2\,3) \rangle$ ([[§40 Quotient Groups#^rem-40-3|§37]])
- $AB$ need not be a subgroup: $A = \langle (1\,2) \rangle$, $B = \langle (1\,3) \rangle$ ([[§42 The Second and Third Isomorphism Theorems#^ex-42-1|§39]])
- $S_3$ as the quotient $S_4/V$ ([[§43 Simple Groups#^prop-43-10|§40]])
- $PSL_2(\mathbb{F}_2) \cong S_3$, which is not simple ([[§43 Simple Groups#^ex-43-3|§40]])
- $\langle (1\,2) \rangle \cong S_3/A_3$, and $S_4/V \cong S_3$, by the Second Isomorphism Theorem ([[§44 S₃, S₄, A₄ and A₅#^ex-44-1|§39]])
- The identity $S_3 \to S_3$ is not constant on conjugacy classes, so characters need an abelian target ([[§45 Characters#^rem-45-3|§41]])

## Chapter by chapter

Revisit parts for $S_3$, chapter by chapter: [[§5 A Zoo of Subgroups#The Symmetric Group S₃|Chapter 1]] · [[§13 The Symmetric Group S₃#S₃ Earlier in This Chapter|Chapter 3]] · [[§19 S₃, ℤ∕nℤ and Uₙ#The Symmetric Group S₃|Chapter 4]] · [[§23 S₃, Aₙ, Uₙ and GLₙ#The Symmetric Group S₃|Chapter 5]] · [[§32 Linear Groups, the Cube, S₃ and A₄#The Symmetric Group S₃|Chapter 6]] · [[§36 S₃, S₄ and GLₙ#The Symmetric Group S₃|Chapter 7]] · [[§44 S₃, S₄, A₄ and A₅#The Symmetric Group S₃|Chapter 8]] · [[§47 S₃, Aₙ and GLₙ#The Symmetric Group S₃|Chapter 9]].

## The mixed hypothesis $gh_1 = h_2g$ does not cancel
![[§2 First Consequences of the Axioms#^ex-2-1]]

## $(gh)^2 \neq g^2h^2$ and $(gh)^{-1} \neq g^{-1}h^{-1}$ for two transpositions
![[§4 Subgroups#^rem-4-1]]

## Products of powers of the generators in a fixed order do not give $\langle g_1, g_2 \rangle$
![[§4 Subgroups#^ex-4-1]]

## $S_3$ is the smallest group in which the fixed-order products fail
![[§4 Subgroups#^rem-4-2]]

## Elements in two-line and cycle notation, non-commutativity, and the multiplication table
![[§10 Cycle Notation and the Group S₃#^ex-10-1]]

## $S_3$ has exactly six subgroups
![[§13 The Symmetric Group S₃#^prop-13-1]]

## The subgroup lattice: orders $1, 2, 3, 6$ all divide $6$
![[§13 The Symmetric Group S₃#^rem-13-1]]

## The mixed hypothesis revisited: conjugation relabels a transposition
![[§13 The Symmetric Group S₃#^ex-13-1]]

## The multiplication table as a worksheet problem (WS 2.4)
![[§14 Multiplication Tables#^ex-14-5]]

## $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$, since one is abelian and the other is not
![[§16 Isomorphisms#^prop-16-3]]

## The trivial center re-proves $S_3 \not\cong \mathbb{Z}/6\mathbb{Z}$
![[§16 Isomorphisms#^rem-16-4]]

## $S_3$ permuting three variables: $x_1x_2 + x_2x_3 + x_1x_3$ is symmetric
![[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-1]]

## The permutation matrices of $(1\,2\,3)$ and $(1\,2)$
![[§20 Polynomial Rings, Permutation Matrices, and Representations#^ex-20-2]]

## $\mathbb{Z}/3\mathbb{Z}$ rotating a triangle maps onto $A_3 \leq S_3$
![[§25 Actions#^ex-25-3]]

## Left and right cosets of $\langle (1\,2) \rangle$ differ
![[§28 Left and Right Cosets#^ex-28-1]]

## The map $gH \mapsto Hg$ is not well defined
![[§28 Left and Right Cosets#^ex-28-2]]

## Cosets of the point stabilizer, read off from $\alpha(3)$ and $\alpha^{-1}(3)$
![[§30 Orbit–Stabilizer#^ex-30-2]]

## Burnside's lemma: one orbit on $\{1, 2, 3\}$, three conjugacy classes
![[§30 Orbit–Stabilizer#^ex-30-3]]

## Three conjugacy classes, of sizes $1, 3, 2$
![[§33 Conjugacy Classes#^ex-33-2]]

## The class equation $6 = 1 + 3 + 2$ and the trivial center
![[§34 Conjugation as an Action and the Class Equation#^ex-34-1]]

## A group with exactly three conjugacy classes has order $3$ or $6$, and $S_3$ occurs
![[§34 Conjugation as an Action and the Class Equation#^cor-34-7]]

## $\langle (1\,2) \rangle$ is not normal
![[§38 Normal Subgroups#^ex-38-1]]

## $A_3 = \langle (1\,2\,3) \rangle$ has index $2$, hence is normal
![[§39 Sources of Normal Subgroups#^ex-39-1]]

## The inclusion of $\langle (1\,2) \rangle$: images need not be normal
![[§39 Sources of Normal Subgroups#^prop-39-3]]

## The normal subgroups $\{e\}$, $A_3$, $S_3$ as unions of conjugacy classes
![[§39 Sources of Normal Subgroups#^ex-39-3]]

## $S_3/A_3$ is cyclic of order $2$
![[§40 Quotient Groups#^ex-40-1]]

## $S_3/A_3$ computed with the representatives $\{e, (2\,3)\}$
![[§40 Quotient Groups#^ex-40-3]]

## The representatives $\{e, (2\,3)\}$ form a subgroup, so $S_3/A_3 \cong \langle (2\,3) \rangle$
![[§40 Quotient Groups#^rem-40-3]]

## $AB$ need not be a subgroup: $A = \langle (1\,2) \rangle$, $B = \langle (1\,3) \rangle$
![[§42 The Second and Third Isomorphism Theorems#^ex-42-1]]

## $S_3$ as the quotient $S_4/V$
![[§43 Simple Groups#^prop-43-10]]

## $PSL_2(\mathbb{F}_2) \cong S_3$, which is not simple
![[§43 Simple Groups#^ex-43-3]]

## $\langle (1\,2) \rangle \cong S_3/A_3$, and $S_4/V \cong S_3$, by the Second Isomorphism Theorem
![[§44 S₃, S₄, A₄ and A₅#^ex-44-1]]

## The identity $S_3 \to S_3$ is not constant on conjugacy classes, so characters need an abelian target
![[§45 Characters#^rem-45-3]]
