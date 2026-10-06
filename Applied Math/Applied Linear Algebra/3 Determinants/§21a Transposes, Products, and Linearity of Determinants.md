---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: "21a"
lay: "3.2"
aliases: ["Lay 3.2 (cont.)"]
tags: [applied-linear-algebra, math235]
---
← [[§21 Properties of Determinants]] · ↑ [[· 3 Determinants]] · [[§22 Cramer’s Rule, Volume, and Linear Transformations]] →

*Lay, Section 3.2 · MATH 235 lectures L11, L12.*

The section also shows that $\det A^T = \det A$ (so columns behave like rows), that $\det AB = (\det A)(\det B)$, and that $\det A$ is a linear function of each column separately.

## Column Operations

> [!theorem] Theorem §21.6: The Determinant of the Transpose
> If $A$ is an $n \times n$ matrix, then $\det A^T = \det A$.
>
> *Lay: Theorem 5 (3.2)*

^thm-21-6

> [!proof]+ Proof
> By induction on $n$ (the Principle of Mathematical Induction, [[§5 The Induction Principle#^def-5-1|250 Def. §5.1]]: if $P(1)$ holds and $P(k)$ implies $P(k+1)$ for each $k$, then $P(n)$ holds for all $n \ge 1$). The theorem is obvious for $n = 1$. Suppose it is true for $k \times k$ determinants and let $n = k + 1$. The entry $a_{1j}$ of $A$ sits in position $(j, 1)$ of $A^T$, and deleting row $j$ and column $1$ of $A^T$ gives $(A_{1j})^T$. So the cofactor of $a_{1j}$ in $A^T$ is $(-1)^{j+1}\det (A_{1j})^T = (-1)^{1+j}\det A_{1j}$, the cofactor of $a_{1j}$ in $A$, by the induction hypothesis applied to the $k \times k$ matrix $A_{1j}$. Hence the cofactor expansion of $\det A$ across the first *row* equals the cofactor expansion of $\det A^T$ down the first *column*, and by [[§20 Introduction to Determinants#^thm-20-1|Theorem §20.1]] these are $\det A$ and $\det A^T$. The theorem is true for $n = 1$, and its truth for one value of $n$ implies its truth for the next, so it is true for all $n \ge 1$.

^pf-21-6

*Uses:* [[§20 Introduction to Determinants#^def-20-2|Def. §20.2]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]]

> [!theorem] Corollary §21.7: Column Operations
> Each statement of [[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]] remains true when the word *row* is replaced everywhere by *column*: a column replacement does not change $\det A$, interchanging two columns changes its sign, and multiplying a column by $k$ multiplies $\det A$ by $k$. Likewise [[§21 Properties of Determinants#^cor-21-5|Corollary §21.5]] gives $\det A = 0$ when two columns are equal.
>
> *Lay: 3.2 (text after Theorem 5)*

^cor-21-7

> [!proof]+ Proof
> A column operation on $A$ is the same as the corresponding row operation on $A^T$. Apply [[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]] to $A^T$ and use $\det A^T = \det A$ ([[§21a Transposes, Products, and Linearity of Determinants#^thm-21-6|Theorem §21.6]]) before and after.

^pf-21-7

*Uses:* [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§21 Properties of Determinants#^thm-21-6|§21.6]]

Column operations are useful for theoretical purposes and for hand computation; for simplicity Lay performs only row operations in numerical work. The lecture uses both in the next computation.

> [!theorem] Proposition §21.8: The Vandermonde Determinant
> For numbers $z_1, \ldots, z_n$ let $\Delta(z_1, \ldots, z_n)$ be the $n \times n$ matrix whose $j$th column is $(1, z_j, z_j^2, \ldots, z_j^{n-1})$:
>
> $$
> \Delta(z_1, \ldots, z_n) = \begin{bmatrix} 1 & 1 & \cdots & 1 \\ z_1 & z_2 & \cdots & z_n \\ z_1^2 & z_2^2 & \cdots & z_n^2 \\ \vdots & \vdots & & \vdots \\ z_1^{n-1} & z_2^{n-1} & \cdots & z_n^{n-1} \end{bmatrix},
> \qquad
> \det \Delta(z_1, \ldots, z_n) = \prod_{i > j} (z_i - z_j) .
> $$
>
> For instance $\det\Delta(a, b) = b - a$, $\det\Delta(a, b, c) = (b - a)(c - a)(c - b)$, and
>
> $$
> \det\Delta(2, 4, 5) = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 4 & 5 \\ 4 & 16 & 25 \end{vmatrix} = (4 - 2)(5 - 2)(5 - 4) = 6 .
> $$
>
> In particular $\det\Delta(z_1, \ldots, z_n) \ne 0$ exactly when the $z_j$ are distinct. (Axler proves the same formula: [[§34 Determinants#^ladr-9-67|LADR 9.67]].)
>
> *Source: 235 lecture L12*

^prop-21-8

> [!proof]+ Proof
> *The lecture does $n = 3$ and the step from $n = 4$ to $n = 3$; here is the general induction.* For $n = 1$ the determinant is $1$, the empty product. Let $n \ge 2$. For $k = n, n-1, \ldots, 2$, in this order, replace row $k$ by row $k$ minus $z_1$ times row $k - 1$ (working from the bottom up, row $k - 1$ is still the original one when it is used). These replacements do not change the determinant ([[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]](a)), and the new $(k, j)$-entry is
>
> $$
> z_j^{k-1} - z_1 z_j^{k-2} = z_j^{k-2}(z_j - z_1) \qquad (k \ge 2) .
> $$
>
> The first column becomes $(1, 0, \ldots, 0)$, so expanding down it,
>
> $$
> \det\Delta(z_1, \ldots, z_n) = \det\begin{bmatrix} z_2 - z_1 & \cdots & z_n - z_1 \\ z_2(z_2 - z_1) & \cdots & z_n(z_n - z_1) \\ \vdots & & \vdots \\ z_2^{n-2}(z_2 - z_1) & \cdots & z_n^{n-2}(z_n - z_1) \end{bmatrix} .
> $$
>
> Column $j$ of this matrix has the common factor $z_j - z_1$; pulling it out of each column ([[§21a Transposes, Products, and Linearity of Determinants#^cor-21-7|Corollary §21.7]]) leaves $\Delta(z_2, \ldots, z_n)$:
>
> $$
> \det\Delta(z_1, \ldots, z_n) = (z_2 - z_1)(z_3 - z_1)\cdots(z_n - z_1)\,\det\Delta(z_2, \ldots, z_n) .
> $$
>
> By the induction hypothesis $\det\Delta(z_2, \ldots, z_n) = \prod_{i > j \ge 2}(z_i - z_j)$, and together with the factors $z_i - z_1$ this is $\prod_{i > j}(z_i - z_j)$.

^pf-21-8

*Uses:* [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§21 Properties of Determinants#^cor-21-7|§21.7]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]]

## Determinants and Matrix Products

> [!theorem] Theorem §21.9: Multiplicative Property
> If $A$ and $B$ are $n \times n$ matrices, then $\det AB = (\det A)(\det B)$.
>
> *Lay: Theorem 6 (3.2)*

^thm-21-9

> [!proof]+ Proof
> **$A$ not invertible.** Then $AB$ is not invertible either. (Lay cites Exercise 27 of 2.3; here is why: if $AB$ had an inverse, then $W = B(AB)^{-1}$ would satisfy $AW = I$, and an $n \times n$ matrix with a right inverse is invertible by the Invertible Matrix Theorem, a contradiction.) By [[§21 Properties of Determinants#^thm-21-3|Theorem §21.3]] both sides of $\det AB = (\det A)(\det B)$ are $0$.
>
> **$A$ invertible.** Then $A$ is row equivalent to $I_n$ (Invertible Matrix Theorem), so there are elementary matrices $E_1, \ldots, E_p$ with
>
> $$
> A = E_pE_{p-1}\cdots E_1 \cdot I_n = E_pE_{p-1}\cdots E_1 .
> $$
>
> Write $|A|$ for $\det A$. Repeated use of [[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]] in the form $\det EM = (\det E)(\det M)$ gives
>
> $$
> |AB| = |E_p \cdots E_1 B| = |E_p|\,|E_{p-1}\cdots E_1 B| = \cdots = |E_p|\cdots|E_1|\,|B| ,
> $$
>
> and the same computation with $B = I_n$ gives $|A| = |E_p|\cdots|E_1|$. Hence $|AB| = |A|\,|B|$.

^pf-21-9

*Uses:* [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]], [[§12 The Inverse of a Matrix#^thm-12-8|§12.8]] (an invertible matrix is a product of elementary matrices)

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-49|LADR 9.49]], where multiplicativity is immediate from the definition of $\det T$ as the factor by which $T$ scales alternating $n$-forms; transpose: [[§34 Determinants#^ladr-9-56|LADR 9.56]].
> - In group language, $\det: GL_n(\mathbb{R}) \to \mathbb{R}^\times$ is a homomorphism ([[§15 Homomorphisms#^def-15-1|493 Def. §15.1]]) from the general linear group ([[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]]) to the nonzero reals under multiplication.

> [!remark] Remark: Why It Works
> The lecture's geometric reason: the linear map $\mathbf{x} \mapsto A\mathbf{x}$ multiplies volumes by $|\det A|$ ([[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-5|Theorem §22.5]], [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-6|Theorem §22.6]]). Applying $B$ and then $A$ multiplies a volume first by $|\det B|$, then by $|\det A|$; and the composite is the map of $AB$. So $|\det AB| = |\det A|\,|\det B|$: the geometric argument gives the multiplicative property up to sign.
>
> *Source: 235 lecture L12*

^rem-21-4

> [!example] Example §21.4: Checking the Multiplicative Property
> Let $A = \begin{bmatrix} 6 & 1 \\ 3 & 2 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix}$. Then
>
> $$
> AB = \begin{bmatrix} 6 & 1 \\ 3 & 2 \end{bmatrix}\begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 25 & 20 \\ 14 & 13 \end{bmatrix}, \qquad \det AB = 25 \cdot 13 - 20 \cdot 14 = 325 - 280 = 45 ,
> $$
>
> and $\det A = 12 - 3 = 9$, $\det B = 8 - 3 = 5$, so $(\det A)(\det B) = 45 = \det AB$.
>
> **Warning.** There is no such rule for sums: $\det(A + B) \ne \det A + \det B$ in general. Here $A + B = \begin{bmatrix} 10 & 4 \\ 4 & 4 \end{bmatrix}$ has determinant $40 - 16 = 24$, while $\det A + \det B = 14$.
>
> *Lay: Example 3.2.5*

^ex-21-4

> [!theorem] Corollary §21.10: Inverses, Powers, Scalar Multiples
> Let $A$, $B$, $P$ be $n \times n$ matrices and $r$ a scalar.
> 1. If $A$ is invertible, $\det A^{-1} = \dfrac{1}{\det A}$.
> 2. $\det A^k = (\det A)^k$ for $k = 1, 2, \ldots$ (and for all integers $k$ if $A$ is invertible).
> 3. $\det(rA) = r^n \det A$.
> 4. $\det AB = \det BA$, even though $AB \ne BA$ in general.
> 5. If $P$ is invertible, $\det(PAP^{-1}) = \det A$.
>
> *Lay: 3.2, Exercises 31, 33, 34, 36*
> *Source: 235 lecture L12*

^cor-21-10

> [!proof]+ Proof
> 1. $\det A \cdot \det A^{-1} = \det(AA^{-1}) = \det I = 1$ ([[§21a Transposes, Products, and Linearity of Determinants#^thm-21-9|Theorem §21.9]], [[§20 Introduction to Determinants#^thm-20-2|Theorem §20.2]]), so $\det A \ne 0$ and $\det A^{-1} = 1/\det A$.
> 2. Induction on $k$: $\det A^{k+1} = \det(A^k A) = (\det A)^k \det A$. For negative $k$ combine with part 1.
> 3. $rA$ is obtained from $A$ by multiplying each of its $n$ rows by $r$; by [[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]](c) each multiplies the determinant by $r$.
> 4. $\det AB = (\det A)(\det B) = (\det B)(\det A) = \det BA$.
> 5. $\det(PAP^{-1}) = \det P \cdot \det A \cdot \det P^{-1} = \det A$, by part 1.

^pf-21-10

*Uses:* [[§21 Properties of Determinants#^thm-21-9|§21.9]], [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]]

> [!example] Example §21.5: Determinants of Matrix Expressions
> Let $A$ and $B$ be $3 \times 3$ matrices with $\det A = -3$ and $\det B = 4$. Then
>
> $$
> \begin{gathered}
> \det AB = (-3)(4) = -12, \qquad \det 5A = 5^3(-3) = -375, \qquad \det B^T = 4, \\
> \det A^{-1} = -\tfrac13, \qquad \det A^3 = (-3)^3 = -27, \qquad \det(B^{-1}AB) = \tfrac14 \cdot (-3) \cdot 4 = -3 .
> \end{gathered}
> $$
>
> For the checklist's $\det(-2AB^T)$: the factor $-2$ multiplies all three rows, so
>
> $$
> \det(-2AB^T) = (-2)^3 \det A \det B^T = (-8)(-3)(4) = 96 .
> $$
>
> The common error is to write $-2\det(AB^T)$: a scalar comes out of a determinant raised to the power $n$.
>
> *Lay: 3.2, Exercise 39*
> *Source: 235 checklist (3.1–3.2)*

^ex-21-5

## A Linearity Property of the Determinant Function

> [!theorem] Theorem §21.11: The Determinant Is Linear in Each Column
> Fix all columns of an $n \times n$ matrix except the $j$th, and define $T: \mathbb{R}^n \to \mathbb{R}$ by
>
> $$
> T(\mathbf{x}) = \det\,[\mathbf{a}_1 \ \cdots \ \mathbf{a}_{j-1} \ \ \mathbf{x} \ \ \mathbf{a}_{j+1} \ \cdots \ \mathbf{a}_n] .
> $$
>
> Then $T$ is linear:
>
> $$
> T(c\mathbf{x}) = cT(\mathbf{x}) \quad \text{for all scalars } c \text{ and all } \mathbf{x} \in \mathbb{R}^n, \qquad (2)
> $$
>
> $$
> T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \quad \text{for all } \mathbf{u}, \mathbf{v} \in \mathbb{R}^n . \qquad (3)
> $$
>
> By [[§21a Transposes, Products, and Linearity of Determinants#^thm-21-6|Theorem §21.6]] the same holds for each row. This (multi-)linearity is the starting point of the advanced treatment of determinants.
>
> *Lay: 3.2 (text), Equations (2) and (3)*

^thm-21-11

> [!proof]+ Proof
> Lay obtains (2) from [[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]](c) for columns, and (3) from a cofactor expansion down column $j$ (Exercise 43); the expansion gives both at once. Write $\mathbf{x} = (x_1, \ldots, x_n)$. Expanding down column $j$ ([[§20 Introduction to Determinants#^thm-20-1|Theorem §20.1]]),
>
> $$
> T(\mathbf{x}) = x_1C_{1j} + x_2C_{2j} + \cdots + x_nC_{nj}, \qquad C_{ij} = (-1)^{i+j}\det A_{ij} .
> $$
>
> The submatrix $A_{ij}$ omits column $j$, so the cofactors $C_{1j}, \ldots, C_{nj}$ do not depend on $\mathbf{x}$. Thus $T(\mathbf{x}) = \mathbf{c} \cdot \mathbf{x}$ for a fixed vector $\mathbf{c} = (C_{1j}, \ldots, C_{nj})$, and $T(c\mathbf{x}) = cT(\mathbf{x})$, $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ follow from the rules of arithmetic. For $2 \times 2$ matrices (the lecture's check):
>
> $$
> \det\begin{bmatrix} a + e & b \\ c + f & d \end{bmatrix} = (a + e)d - b(c + f) = (ad - bc) + (ed - bf) = \det\begin{bmatrix} a & b \\ c & d \end{bmatrix} + \det\begin{bmatrix} e & b \\ f & d \end{bmatrix} .
> $$

^pf-21-11

*Uses:* [[§20 Introduction to Determinants#^thm-20-1|§20.1]], [[§21 Properties of Determinants#^thm-21-6|§21.6]]
