---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: 24
lay: "3.1"
aliases: ["Lay 3.1"]
tags: [applied-linear-algebra, math235]
---
← [[§23 The Singular Matrix with Rows (1, 2) and (2, 4)]] · ↑ [[· 3 Determinants]] · [[§25 Properties of Determinants]] →

*Lay, Section 3.1 · MATH 235 lectures L11, L12.*

A $2 \times 2$ matrix is invertible exactly when $ad - bc \ne 0$ ([[§14 The Inverse of a Matrix#^thm-14-2|Theorem §14.2]], Theorem 4 of 2.2). This section extends that number to every square matrix. Row reducing a general invertible $3 \times 3$ matrix produces a six-term expression that must be nonzero, and rewriting it with $2 \times 2$ determinants suggests a recursive definition: an $n \times n$ determinant is an alternating sum of $n$ determinants of size $n - 1$ along the first row. The main fact, stated without proof, is that the same expansion works along any row or any column; choosing a row or column with many zeros makes hand computation fast, and for triangular matrices the determinant is simply the product of the diagonal entries.

## The Determinant of an n × n Matrix

> [!remark] Remark: Where the 3 × 3 Formula Comes From
> Let $A = [a_{ij}]$ be an invertible $3 \times 3$ matrix with $a_{11} \ne 0$. Multiply rows 2 and 3 by $a_{11}$ and subtract multiples of row 1:
>
> $$
> A \sim \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{11}a_{21} & a_{11}a_{22} & a_{11}a_{23} \\ a_{11}a_{31} & a_{11}a_{32} & a_{11}a_{33} \end{bmatrix} \sim \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ 0 & a_{11}a_{22} - a_{12}a_{21} & a_{11}a_{23} - a_{13}a_{21} \\ 0 & a_{11}a_{32} - a_{12}a_{31} & a_{11}a_{33} - a_{13}a_{31} \end{bmatrix} .
> $$
>
> Since $A$ is invertible, the $(2,2)$- or the $(3,2)$-entry on the right is nonzero; say the $(2,2)$-entry (otherwise interchange rows 2 and 3 first). Multiply row 3 by $a_{11}a_{22} - a_{12}a_{21}$ and add $-(a_{11}a_{32} - a_{12}a_{31})$ times row 2 to it. A short computation gives
>
> $$
> A \sim \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ 0 & a_{11}a_{22} - a_{12}a_{21} & a_{11}a_{23} - a_{13}a_{21} \\ 0 & 0 & a_{11}\Delta \end{bmatrix},
> $$
>
> $$
> \Delta = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} - a_{13}a_{22}a_{31} . \qquad (2)
> $$
>
> Since $A$ is invertible, $\Delta \ne 0$ (and conversely, by [[§25 Properties of Determinants#^thm-25-3|Theorem §25.3]]). Grouping the six terms in pairs,
>
> $$
> \Delta = a_{11} \det\begin{bmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{bmatrix} - a_{12} \det\begin{bmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{bmatrix} + a_{13} \det\begin{bmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{bmatrix} = a_{11}\det A_{11} - a_{12}\det A_{12} + a_{13}\det A_{13}, \qquad (3)
> $$
>
> where $A_{1j}$ is $A$ with the first row and the $j$th column deleted. This is the pattern the general definition copies.

^rem-24-1

> [!definition] Definition §30.1: The Submatrix A_ij
> For a square matrix $A$, $A_{ij}$ denotes the submatrix formed by deleting the $i$th row and the $j$th column of $A$. For instance,
>
> $$
> A = \begin{bmatrix} 1 & -2 & 5 & 0 \\ 2 & 0 & 4 & -1 \\ 3 & 1 & 0 & 7 \\ 0 & 4 & -2 & 0 \end{bmatrix}
> \quad\Longrightarrow\quad
> A_{32} = \begin{bmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{bmatrix}
> $$
>
> (cross out row 3 and column 2). The lectures write $M_{ij}(A)$ and call it a **minor** of $A$.
>
> *Lay: 3.1 (text)*

^def-24-1

> [!definition] Definition §30.2: Determinant
> For a $1 \times 1$ matrix, $\det\,[a_{11}] = a_{11}$. For $n \ge 2$, the **determinant** of an $n \times n$ matrix $A = [a_{ij}]$ is the sum of $n$ terms of the form $\pm a_{1j} \det A_{1j}$, with plus and minus signs alternating, where $a_{11}, a_{12}, \ldots, a_{1n}$ are the entries of the first row of $A$:
>
> $$
> \det A = a_{11}\det A_{11} - a_{12}\det A_{12} + \cdots + (-1)^{1+n} a_{1n}\det A_{1n} = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} \det A_{1j} .
> $$
>
> The definition is **recursive**: an $n \times n$ determinant is defined by determinants of $(n-1) \times (n-1)$ submatrices. For $n = 2$ it gives $\det A = a_{11}a_{22} - a_{12}a_{21}$, the number of [[§14 The Inverse of a Matrix#^def-14-2|Definition §14.2]]; for $n = 3$ it gives $\Delta$ of [[§24 Introduction to Determinants#^rem-24-1|Remark: Where the 3 × 3 Formula Comes From]]. Another common notation replaces the brackets by vertical bars: $\det A = |A|$.
>
> *Lay: 3.1, Definition*

^def-24-2

> [!remark]- Connections
> - Rigorous treatment: Axler defines $\det$ through the one-dimensional space of alternating $n$-linear forms ([[§37 Determinants#^ladr-9-43|LADR 9.43]]) and derives the closed formula $\det A = \sum_{\sigma} \operatorname{sign}(\sigma)\, a_{\sigma(1),1} \cdots a_{\sigma(n),n}$ over all $n!$ permutations ([[§37 Determinants#^ladr-9-46|LADR 9.46]]); unwinding Lay's recursion gives exactly this sum.
> - The sign of a permutation and the parity of the number of inversions: [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|493 Def. §21.2]], [[§36 Alternating Multilinear Forms#^ladr-9-32|LADR 9.32]]; the sign is $\det$ of the permutation matrix ([[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|493 Thm. §21.2]]).

> [!definition] Definition §30.3: Cofactor
> Given $A = [a_{ij}]$, the **$(i,j)$-cofactor** of $A$ is the number
>
> $$
> C_{ij} = (-1)^{i+j} \det A_{ij} . \qquad (4)
> $$
>
> With this notation [[§24 Introduction to Determinants#^def-24-2|Definition §24.2]] reads
>
> $$
> \det A = a_{11}C_{11} + a_{12}C_{12} + \cdots + a_{1n}C_{1n},
> $$
>
> the **cofactor expansion across the first row** of $A$.
>
> *Lay: 3.1, Equation (4)*

^def-24-3

> [!theorem] Theorem §30.1: Cofactor Expansion Along Any Row or Column
> The determinant of an $n \times n$ matrix $A$ can be computed by a cofactor expansion across any row or down any column. The expansion across the $i$th row is
>
> $$
> \det A = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in},
> $$
>
> and the expansion down the $j$th column is
>
> $$
> \det A = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj} .
> $$
>
> *Lay: Theorem 1 (3.1)*

^thm-24-1

*Lay omits the proof "to avoid a lengthy digression". It follows from the permutation formula [[§37 Determinants#^ladr-9-46|LADR 9.46]] by grouping its $n!$ terms according to which entry of row $i$ (or column $j$) they contain; LADR does not state the expansion itself.*

> [!remark] Remark: The Checkerboard of Signs
> The sign $(-1)^{i+j}$ in $C_{ij}$ depends only on the *position* of $a_{ij}$, not on the sign of $a_{ij}$ itself:
>
> $$
> \begin{bmatrix} + & - & + & \cdots \\ - & + & - & \\ + & - & + & \\ \vdots & & & \ddots \end{bmatrix}
> $$
>
> [[§24 Introduction to Determinants#^thm-24-1|Theorem §24.1]] pays off when a row or column contains many zeros: the terms with $a_{ij} = 0$ need no cofactor. In particular, if a whole row or column is zero, the expansion along it is a sum of zeros, so $\det A = 0$. From now on zero terms are omitted from expansions.

^rem-24-2

> [!example] Example §30.1: Expanding Across the First Row and Across the Third Row
> Compute $\det A$ for
>
> $$
> A = \begin{bmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{bmatrix} .
> $$
>
> **Across the first row** ([[§24 Introduction to Determinants#^def-24-2|Definition §24.2]]):
>
> $$
> \det A = 1 \cdot \begin{vmatrix} 4 & -1 \\ -2 & 0 \end{vmatrix} - 5 \begin{vmatrix} 2 & -1 \\ 0 & 0 \end{vmatrix} + 0 \begin{vmatrix} 2 & 4 \\ 0 & -2 \end{vmatrix} = 1(0 - 2) - 5(0 - 0) + 0(-4 - 0) = -2 .
> $$
>
> **Across the third row** ([[§24 Introduction to Determinants#^thm-24-1|Theorem §24.1]]), which has two zeros:
>
> $$
> \det A = a_{31}C_{31} + a_{32}C_{32} + a_{33}C_{33} = 0 + (-1)^{3+2}(-2) \begin{vmatrix} 1 & 0 \\ 2 & -1 \end{vmatrix} + 0 = -(-2)(-1) = -2 .
> $$
>
> The second computation needs a single $2 \times 2$ determinant.
>
> *Lay: Examples 3.1.1 and 3.1.2*

^ex-24-1

> [!example] Example §30.2: Following the Zeros
> Compute $\det A$ for
>
> $$
> A = \begin{bmatrix} 2 & 3 & 0 & 2 \\ 4 & 3 & 2 & 1 \\ 6 & 0 & 0 & 3 \\ 7 & 0 & 0 & 4 \end{bmatrix} .
> $$
>
> Row 4 has two zeros. Its signs are $- + - +$ (checkerboard), so expanding across row 4,
>
> $$
> \det A = -7 \det A_{41} + 4 \det A_{44} = -7 \begin{vmatrix} 3 & 0 & 2 \\ 3 & 2 & 1 \\ 0 & 0 & 3 \end{vmatrix} + 4 \begin{vmatrix} 2 & 3 & 0 \\ 4 & 3 & 2 \\ 6 & 0 & 0 \end{vmatrix} .
> $$
>
> In the first $3 \times 3$ determinant, row 3 has only the entry $3$, in position $(3,3)$ with sign $+$:
>
> $$
> \begin{vmatrix} 3 & 0 & 2 \\ 3 & 2 & 1 \\ 0 & 0 & 3 \end{vmatrix} = 3 \begin{vmatrix} 3 & 0 \\ 3 & 2 \end{vmatrix} = 3 \cdot 6 = 18 .
> $$
>
> In the second, column 3 has only the entry $2$, in position $(2,3)$ with sign $-$:
>
> $$
> \begin{vmatrix} 2 & 3 & 0 \\ 4 & 3 & 2 \\ 6 & 0 & 0 \end{vmatrix} = -2 \begin{vmatrix} 2 & 3 \\ 6 & 0 \end{vmatrix} = -2(0 - 18) = 36 .
> $$
>
> Hence $\det A = -7 \cdot 18 + 4 \cdot 36 = -126 + 144 = 18$.
>
> *Source: 235 lecture L11*

^ex-24-2

## Triangular Matrices

> [!example] Example §30.3: A Nearly Triangular Matrix
> Compute $\det A$ for
>
> $$
> A = \begin{bmatrix} 3 & -7 & 8 & 9 & -6 \\ 0 & 2 & -5 & 7 & 3 \\ 0 & 0 & 1 & 5 & 0 \\ 0 & 0 & 2 & 4 & -1 \\ 0 & 0 & 0 & -2 & 0 \end{bmatrix} .
> $$
>
> Down the first column all terms vanish except the first: $\det A = 3 \det A_{11}$. The $4 \times 4$ matrix $A_{11}$ again has a single nonzero entry, $2$, in its first column, so
>
> $$
> \det A = 3 \cdot 2 \cdot \begin{vmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{vmatrix} = 3 \cdot 2 \cdot (-2) = -12,
> $$
>
> using [[§24 Introduction to Determinants#^ex-24-1|Example §24.1]] for the $3 \times 3$ determinant.
>
> *Lay: Example 3.1.3*

^ex-24-3

> [!theorem] Theorem §30.2: Determinant of a Triangular Matrix
> If $A$ is a triangular matrix, then $\det A$ is the product of the entries on the main diagonal of $A$. In particular $\det I_n = 1$.
>
> *Lay: Theorem 2 (3.1)*

^thm-24-2

> [!proof]+ Proof
> *Lay says only that the method of [[§24 Introduction to Determinants#^ex-24-3|Example §24.3]] "is easily adapted"; here is the induction.* For $n = 1$ there is nothing to prove. Let $n \ge 2$ and assume the result for $(n-1) \times (n-1)$ triangular matrices.
>
> If $A$ is **upper** triangular, the only possibly nonzero entry of its first column is $a_{11}$, so the cofactor expansion down column 1 ([[§24 Introduction to Determinants#^thm-24-1|Theorem §24.1]]) gives $\det A = a_{11}C_{11} = a_{11}\det A_{11}$. Deleting row 1 and column 1 of an upper triangular matrix leaves an upper triangular matrix with diagonal $a_{22}, \ldots, a_{nn}$, so by the induction hypothesis $\det A_{11} = a_{22}\cdots a_{nn}$, and $\det A = a_{11}a_{22}\cdots a_{nn}$.
>
> If $A$ is **lower** triangular, the only possibly nonzero entry of its first row is $a_{11}$, so [[§24 Introduction to Determinants#^def-24-2|Definition §24.2]] itself gives $\det A = a_{11}\det A_{11}$, where $A_{11}$ is lower triangular with diagonal $a_{22}, \ldots, a_{nn}$; conclude as before.

^pf-24-2

*Uses:* [[§24 Introduction to Determinants#^def-24-2|Def. §24.2]], [[§24 Introduction to Determinants#^thm-24-1|§24.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§37 Determinants#^ladr-9-48|LADR 9.48]] (upper-triangular case), where only the identity permutation contributes to the permutation formula.

## The 3 × 3 Diagonal Rule

> [!theorem] Proposition §30.3: The Diagonal Rule for 3 × 3 Determinants
> Write a second copy of the first two columns to the right of a $3 \times 3$ matrix. Then $\det A$ is the sum of the three products along the downward diagonals minus the sum of the three products along the upward diagonals:
>
> $$
> \begin{array}{ccc|cc} a_{11} & a_{12} & a_{13} & a_{11} & a_{12} \\ a_{21} & a_{22} & a_{23} & a_{21} & a_{22} \\ a_{31} & a_{32} & a_{33} & a_{31} & a_{32} \end{array}
> \qquad
> \begin{aligned}
> \det A = {}& a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} \\
> & - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} .
> \end{aligned}
> $$
>
> This is **Sarrus' rule**. It does *not* generalize in any reasonable way to $4 \times 4$ or larger matrices: a $4 \times 4$ determinant has $24$ terms, not $8$.
>
> *Lay: 3.1, Exercise 15*
> *Source: 235 lecture L11*

^prop-24-3

> [!proof]+ Proof
> Expand across the first row ([[§24 Introduction to Determinants#^def-24-2|Definition §24.2]]) and multiply out the three $2 \times 2$ determinants:
>
> $$
> \det A = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31}) .
> $$
>
> The three positive terms $a_{11}a_{22}a_{33}$, $a_{12}a_{23}a_{31}$, $a_{13}a_{21}a_{32}$ are the downward diagonals, and the three negative terms $a_{11}a_{23}a_{32}$, $a_{12}a_{21}a_{33}$, $a_{13}a_{22}a_{31}$ are the upward diagonals. (This is formula (2) of [[§24 Introduction to Determinants#^rem-24-1|Remark: Where the 3 × 3 Formula Comes From]].)

^pf-24-3

*Uses:* [[§24 Introduction to Determinants#^def-24-2|Def. §24.2]]

> [!example] Example §30.4: The Diagonal Rule on a Singular Matrix
> For
>
> $$
> A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix},
> $$
>
> [[§24 Introduction to Determinants#^prop-24-3|Proposition §24.3]] gives
>
> $$
> \det A = 1 \cdot 5 \cdot 9 + 2 \cdot 6 \cdot 7 + 3 \cdot 4 \cdot 8 - 3 \cdot 5 \cdot 7 - 1 \cdot 6 \cdot 8 - 2 \cdot 4 \cdot 9 = 45 + 84 + 96 - 105 - 48 - 72 = 0 .
> $$
>
> The lecture groups the terms instead: $9(5 - 8) + 3(4 \cdot 8 - 5 \cdot 7) + 6(2 \cdot 7 - 8) = -27 - 9 + 36 = 0$. The value $0$ reflects that the rows are dependent: row 3 $= 2 \cdot$ row 2 $-$ row 1 ([[§25 Properties of Determinants#^cor-25-5|Corollary §25.5]]).
>
> *Source: 235 lecture L11*

^ex-24-4

> [!remark]- Connections
> - The same $2 \times 2$ and $3 \times 3$ determinants in Calculus, used to compute cross products: [[§96 The Cross Product#^def-96-2|Calc Def. §96.2]], [[§96 The Cross Product#^prop-96-1|Calc Prop. §96.1]]. LADR writes out the six terms as a sum over permutations: [[§37 Determinants#^ladr-9-47|LADR 9.47]].

> [!remark]- Remark: The Cost of Cofactor Expansion
> Expanding an $n \times n$ determinant by cofactors requires more than $n!$ multiplications. By Stirling's formula $n! \approx \sqrt{2\pi n}\,(n/e)^n$, which the lecture abbreviates to $n! \sim n^n e^{-n}$. Already $25! \approx 1.5 \times 10^{25}$: a computer doing $10^{12}$ multiplications per second would need more than $500{,}000$ years for a $25 \times 25$ determinant. Row reduction ([[§25 Properties of Determinants#^rem-25-3|§25, Remark: Numerical Notes]]) needs only about $2n^3/3$ operations.
>
> The lecture contrasts this with the **permanent**, $\operatorname{perm} A = \sum_j a_{ij} \operatorname{perm} A_{ij}$, the same expansion with all signs $+$. Row operations do not control the permanent, and no polynomial-time method is known: the best known methods, such as Ryser's formula with about $2^n n$ operations, are far faster than $n!$ but still exponential. The lecture links the question to the P vs NP problem. Precisely: computing the permanent is #P-complete (Valiant, 1979), so a polynomial-time algorithm for it would imply P = NP; the converse is not known.
>
> *Source: 235 lectures L11, L12*

^rem-24-3
