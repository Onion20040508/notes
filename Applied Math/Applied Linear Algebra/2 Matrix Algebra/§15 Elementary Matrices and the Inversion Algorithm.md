---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 15
lay: "2.2"
aliases: ["Lay 2.2 (cont.)"]
tags: [applied-linear-algebra, math235]
---
← [[§14 The Inverse of a Matrix]] · ↑ [[· 2 Matrix Algebra]] · [[§16 Characterizations of Invertible Matrices]] →

*Lay, Section 2.2 · MATH 235 lectures L7, L8, L9.*

Each elementary row operation is multiplication on the left by an elementary matrix. This gives the main theorem: $A$ is invertible exactly when it row reduces to $I$, and the same row operations turn $I$ into $A^{-1}$. That is the algorithm for computing inverses: row reduce $[\,A \ \ I\,]$.

## Elementary Matrices

An invertible matrix is row equivalent to an identity matrix, and $A^{-1}$ can be found by watching the row reduction of $A$ to $I$. The link is that row operations are matrix multiplications.

> [!definition] Definition §15.1: Elementary Matrix
> An **elementary matrix** is one that is obtained by performing a single elementary row operation on an identity matrix. There are three kinds, one for each kind of row operation: replacement, interchange and scaling.
>
> The lecture writes $E_{ij}(a)$ for the replacement matrix that adds $a$ times row $j$ to row $i$ ($i \ne j$): it is $I$ with the $(i, j)$-entry changed from $0$ to $a$,
>
> $$
> \big(E_{ij}(a)\big)_{k\ell} = \begin{cases} 1 & k = \ell, \\ a & (k, \ell) = (i, j), \\ 0 & \text{otherwise.} \end{cases}
> $$
>
> *Lay: 2.2 (text)*
> *Source: 235 lecture L9*

^def-15-1

> [!definition] Definition §15.2: Permutation Matrix
> An $n \times n$ matrix is a **permutation matrix** if each row and each column has exactly one nonzero entry, and that entry is $1$. Equivalently, its columns are $\mathbf{e}_1, \ldots, \mathbf{e}_n$ in some order. There are exactly $n!$ of them; for $n = 3$ the $3! = 6$ permutation matrices are
>
> $$
> \begin{bmatrix} 1&0&0\\0&1&0\\0&0&1 \end{bmatrix}, \
> \begin{bmatrix} 0&1&0\\1&0&0\\0&0&1 \end{bmatrix}, \
> \begin{bmatrix} 1&0&0\\0&0&1\\0&1&0 \end{bmatrix}, \
> \begin{bmatrix} 0&0&1\\0&1&0\\1&0&0 \end{bmatrix}, \
> \begin{bmatrix} 0&0&1\\1&0&0\\0&1&0 \end{bmatrix}, \
> \begin{bmatrix} 0&1&0\\0&0&1\\1&0&0 \end{bmatrix} .
> $$
>
> Left multiplication by a permutation matrix permutes the rows; the interchange elementary matrices are the permutation matrices that swap two rows.
>
> *Source: 235 lecture L9*

^def-15-2

> [!remark]- Connections
> - Permutation matrices are the matrices $M(\sigma)$ of the linear maps that permute the standard basis, and $\sigma \mapsto M(\sigma)$ is an injective homomorphism $S_n \to GL_n$: [[§20 Polynomial Rings, Permutation Matrices, and Representations#^def-20-6|493 Def. §20.6]], [[§20 Polynomial Rings, Permutation Matrices, and Representations#^prop-20-5|493 Prop. §20.5]]. The count $n!$ is the order of $S_n$.

> [!theorem] Proposition §15.1: Row Operations Are Left Multiplications
> If an elementary row operation is performed on an $m \times n$ matrix $A$, the resulting matrix can be written as $EA$, where the $m \times m$ matrix $E$ is created by performing the same row operation on $I_m$.
>
> *Lay: 2.2 (text)*

^prop-15-1

> [!proof]+ Proof
> (Lay proves the $3 \times 3$ cases in Exercises 27–28; here is the general argument.) Each elementary row operation replaces the rows of a matrix by fixed linear combinations of its rows, with coefficients that depend only on the operation and not on the matrix: there are numbers $e_{ik}$ such that, for every matrix $M$ with $m$ rows,
>
> $$
> \operatorname{row}_i(\text{new } M) = \sum_{k=1}^m e_{ik}\operatorname{row}_k(M), \qquad i = 1, \ldots, m .
> $$
>
> (A replacement "row $i$ + $a$ · row $j$" has $e_{ii} = 1$, $e_{ij} = a$ and otherwise $e_{kk} = 1$, all other $e_{k\ell} = 0$; an interchange and a scaling are similar.) Applied to $M = I_m$, whose $k$th row is $\mathbf{e}_k^T$, this gives $\operatorname{row}_i(E) = \sum_k e_{ik}\mathbf{e}_k^T = [\,e_{i1} \ \cdots \ e_{im}\,]$. Now by [[§12 Matrix Operations#^prop-12-5|Proposition §12.5]] (equation (2) of [[§12 Matrix Operations|§12]]) and the row–column rule ([[§12 Matrix Operations#^prop-12-4|Proposition §12.4]]),
>
> $$
> \operatorname{row}_i(EA) = \operatorname{row}_i(E)\,A = [\,e_{i1} \ \cdots \ e_{im}\,]\,A = \sum_{k=1}^m e_{ik}\operatorname{row}_k(A),
> $$
>
> which is row $i$ of the matrix obtained from $A$ by the operation.

^pf-15-1

*Uses:* [[§12 Matrix Operations#^prop-12-5|§12.5]], [[§12 Matrix Operations#^prop-12-4|§12.4]]

> [!theorem] Proposition §15.2: Elementary Matrices Are Invertible
> Each elementary matrix $E$ is invertible. The inverse of $E$ is the elementary matrix of the same type that transforms $E$ back into $I$.
>
> *Lay: 2.2 (text)*

^prop-15-2

> [!proof]+ Proof
> Row operations are reversible ([[§1 Systems of Linear Equations#^prop-1-1|Proposition §1.1]]): a replacement adding $a$ times row $j$ to row $i$ is undone by adding $-a$ times row $j$ to row $i$, an interchange by the same interchange, and scaling a row by $c \ne 0$ by scaling it by $1/c$. Let $E$ come from $I$ by an operation, and let $F$ be the elementary matrix of the reverse operation. By [[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-1|Proposition §15.1]], $FE$ is the result of applying the reverse operation to $E$, which is $I$. Likewise $EF$ is the result of applying the original operation to $F$, which undoes the reverse operation and gives $I$. So $FE = EF = I$ and $F = E^{-1}$.

^pf-15-2

*Uses:* [[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-1|§15.1]], [[§14 The Inverse of a Matrix#^def-14-1|Def. §14.1]], [[§1 Systems of Linear Equations#^prop-1-1|§1.1]]

> [!example] Example §15.1: Elementary and Permutation Matrices
> **(a)** Let
>
> $$
> E_1 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}, \quad
> E_2 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad
> E_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 5 \end{bmatrix}, \quad
> A = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} .
> $$
>
> By the row–column rule,
>
> $$
> E_1A = \begin{bmatrix} a & b & c \\ d & e & f \\ g - 4a & h - 4b & i - 4c \end{bmatrix}, \quad
> E_2A = \begin{bmatrix} d & e & f \\ a & b & c \\ g & h & i \end{bmatrix}, \quad
> E_3A = \begin{bmatrix} a & b & c \\ d & e & f \\ 5g & 5h & 5i \end{bmatrix} .
> $$
>
> $E_1A$ adds $-4$ times row 1 to row 3 (replacement; $E_1 = E_{31}(-4)$), $E_2A$ interchanges rows 1 and 2, and $E_3A$ multiplies row 3 by 5, exactly the operations that produce $E_1$, $E_2$, $E_3$ from $I$. Similarly, in the lecture, $E_{31}(7)A$ is $A$ with row 3 replaced by row 3 plus $7$ times row 1.
>
> **(b)** To transform $E_1$ back into $I$, add $+4$ times row 1 to row 3. So
>
> $$
> E_1^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ +4 & 0 & 1 \end{bmatrix}, \qquad\text{in general}\qquad E_{ij}(a)^{-1} = E_{ij}(-a) .
> $$
>
> For instance $A = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = E_{13}(5)$ has inverse $E_{13}(-5) = \begin{bmatrix} 1 & 0 & -5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, which is also what row reducing $[\,A \ \ I\,]$ by "row 1 $-$ 5 · row 3" gives.
>
> **(c)** The permutation matrix $P = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ sends $\mathbf{e}_1 \mapsto \mathbf{e}_2$, $\mathbf{e}_2 \mapsto \mathbf{e}_3$, $\mathbf{e}_3 \mapsto \mathbf{e}_1$ (its columns). The inverse map sends $\mathbf{e}_2 \mapsto \mathbf{e}_1$, $\mathbf{e}_3 \mapsto \mathbf{e}_2$, $\mathbf{e}_1 \mapsto \mathbf{e}_3$, so its matrix has columns $P^{-1}\mathbf{e}_1 = \mathbf{e}_3$, $P^{-1}\mathbf{e}_2 = \mathbf{e}_1$, $P^{-1}\mathbf{e}_3 = \mathbf{e}_2$:
>
> $$
> P^{-1} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} = P^T .
> $$
>
> Row reducing $[\,P \ \ I\,]$ by two interchanges gives the same answer. In general the inverse of a permutation matrix is again a permutation matrix, namely its transpose: the $(i, j)$-entry of $P^TP$ is (column $i$ of $P$) $\cdot$ (column $j$ of $P$), which is $1$ if $i = j$ and $0$ otherwise, because the columns are distinct standard basis vectors.
>
> *The lecture's margin note beside $E_{31}(7)A$ reads "III row − 7 × I row"; the product it computes, with third row $(g + 7a,\ h + 7b,\ k + 7c)$, adds 7 times row 1 to row 3.*
>
> *Lay: Examples 2.2.5 and 2.2.6*
> *Source: 235 lecture L9*

^ex-15-1

> [!theorem] Theorem §15.3: Invertibility and Row Reduction
> An $n \times n$ matrix $A$ is invertible if and only if $A$ is row equivalent to $I_n$, and in this case, any sequence of elementary row operations that reduces $A$ to $I_n$ also transforms $I_n$ into $A^{-1}$.
>
> *Lay: Theorem 7 (2.2)*

^thm-15-3

> [!proof]+ Proof
> **Invertible $\Rightarrow$ row equivalent to $I_n$.** Suppose $A$ is invertible. By [[§14 The Inverse of a Matrix#^thm-14-3|Theorem §14.3]] the equation $A\mathbf{x} = \mathbf{b}$ has a solution for each $\mathbf{b}$, so $A$ has a pivot position in every row ([[§5 The Matrix Equation Ax = b#^thm-5-3|Theorem §5.3]]). Because $A$ is square, the $n$ pivot positions must lie on the main diagonal (each of the $n$ rows and each of the $n$ columns contains exactly one pivot, and pivots move strictly down and to the right), so the reduced echelon form of $A$ is $I_n$. That is, $A \sim I_n$.
>
> **Row equivalent to $I_n$ $\Rightarrow$ invertible.** Conversely, suppose $A \sim I_n$. Each step of the row reduction is left multiplication by an elementary matrix ([[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-1|Proposition §15.1]]), so there are elementary matrices $E_1, \ldots, E_p$ with
>
> $$
> A \sim E_1A \sim E_2(E_1A) \sim \cdots \sim E_p(E_{p-1} \cdots E_1A) = I_n,
> \qquad\text{that is,}\qquad
> E_p \cdots E_1A = I_n . \tag{1}
> $$
>
> The product $E_p \cdots E_1$ of invertible matrices is invertible ([[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-2|Proposition §15.2]], [[§14 The Inverse of a Matrix#^cor-14-5|Corollary §14.5]]), so multiplying (1) on the left by its inverse,
>
> $$
> (E_p \cdots E_1)^{-1}(E_p \cdots E_1)A = (E_p \cdots E_1)^{-1}I_n, \qquad A = (E_p \cdots E_1)^{-1} .
> $$
>
> Thus $A$ is invertible, as the inverse of an invertible matrix ([[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]](a)), and
>
> $$
> A^{-1} = \big[(E_p \cdots E_1)^{-1}\big]^{-1} = E_p \cdots E_1 = E_p \cdots E_1 \cdot I_n .
> $$
>
> This says that $A^{-1}$ results from applying the operations of $E_1, \ldots, E_p$ successively to $I_n$: the same sequence that reduced $A$ to $I_n$ in (1).

^pf-15-3

*Uses:* [[§14 The Inverse of a Matrix#^thm-14-3|§14.3]], [[§5 The Matrix Equation Ax = b#^thm-5-3|§5.3]], [[§2 Row Reduction and Echelon Forms#^def-2-3|Def. §2.3]], [[§2 Row Reduction and Echelon Forms#^def-2-2|Def. §2.2]], [[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-1|§15.1]], [[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-2|§15.2]], [[§14 The Inverse of a Matrix#^cor-14-5|§14.5]], [[§14 The Inverse of a Matrix#^thm-14-4|§14.4]]

> [!remark] Remark: An Invertible Matrix Is a Product of Elementary Matrices
> The proof shows $A = (E_p \cdots E_1)^{-1} = E_1^{-1} \cdots E_p^{-1}$, a product of elementary matrices ([[§15 Elementary Matrices and the Inversion Algorithm#^prop-15-2|Proposition §15.2]]). So the invertible matrices are exactly the products of elementary matrices; the lecture phrases it as products of replacement matrices $E_{ij}(a)$, permutation matrices and scalings. For example, if $E_{12}(7)\,P\,E_{31}(-2)\,A = I$ for a permutation matrix $P$, then $A^{-1} = E_{12}(7)\,P\,E_{31}(-2)$, and row reducing $[\,A \ \ I\,]$ builds exactly this product in the right half:
>
> $$
> [\,A \ \ I\,] \to [\,E_{31}(-2)A \ \ E_{31}(-2)\,] \to [\,PE_{31}(-2)A \ \ PE_{31}(-2)\,] \to [\,E_{12}(7)PE_{31}(-2)A \ \ E_{12}(7)PE_{31}(-2)\,] = [\,I \ \ A^{-1}\,] .
> $$
>
> *Source: 235 lecture L9*

^rem-15-1
## An Algorithm for Finding the Inverse

Placing $A$ and $I$ side by side, row operations on $[\,A \ \ I\,]$ act identically on both halves. By [[§15 Elementary Matrices and the Inversion Algorithm#^thm-15-3|Theorem §15.3]], either some row operations turn $A$ into $I_n$, and then they turn $I_n$ into $A^{-1}$, or $A$ is not invertible.

> [!remark] Remark: Method — Finding the Inverse of a Matrix
> 1. Form the $n \times 2n$ augmented matrix $[\,A \ \ I\,]$.
> 2. Row reduce it. If $A$ is row equivalent to $I$, then $[\,A \ \ I\,]$ is row equivalent to $[\,I \ \ A^{-1}\,]$: read off $A^{-1}$ on the right.
> 3. If at some stage the left half has fewer than $n$ pivots (for instance a row of zeros appears in it), then $A$ is not row equivalent to $I$ and $A$ does not have an inverse.
> 4. Check the answer by computing $AA^{-1}$. Checking $A^{-1}A = I$ is unnecessary, since $A$ is invertible ([[§16 Characterizations of Invertible Matrices#^cor-16-2|Corollary §16.2]]).
>
> For a $2 \times 2$ matrix, [[§14 The Inverse of a Matrix#^thm-14-2|Theorem §14.2]] is faster.
>
> *Lay: 2.2, Algorithm for Finding A⁻¹*

^rem-15-2
> [!remark] Remark: Another View of Matrix Inversion
> Write $I_n = [\,\mathbf{e}_1 \ \cdots \ \mathbf{e}_n\,]$. Row reducing $[\,A \ \ I\,]$ solves the $n$ systems
>
> $$
> A\mathbf{x} = \mathbf{e}_1, \quad A\mathbf{x} = \mathbf{e}_2, \quad \ldots, \quad A\mathbf{x} = \mathbf{e}_n \tag{2}
> $$
>
> simultaneously, with all their augmented columns placed next to $A$. Since $AA^{-1} = I$ and column $j$ of $AA^{-1}$ is $A$ times column $j$ of $A^{-1}$, the columns of $A^{-1}$ are precisely the solutions of the systems (2). The lecture motivates the algorithm this way: to find the matrix $B$ of the inverse transformation, find $B(\mathbf{e}_1)$ and $B(\mathbf{e}_2)$, that is, vectors $\mathbf{u}$, $\mathbf{v}$ with $A\mathbf{u} = \mathbf{e}_1$ and $A\mathbf{v} = \mathbf{e}_2$; then $B = [\,\mathbf{u} \ \ \mathbf{v}\,]$. This is useful when only one or two columns of $A^{-1}$ are needed: solve only the corresponding systems in (2).
>
> *Source: 235 lecture L8*

^rem-15-3
> [!example] Example §15.2: Inverting by Row Reduction
> **(a)** For $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, solve $A\mathbf{u} = \mathbf{e}_1$ and $A\mathbf{v} = \mathbf{e}_2$ at once:
>
> $$
> \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array}\right]
> \xrightarrow{R_2 - 3R_1}
> \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array}\right]
> \xrightarrow{R_2 \div (-2)}
> \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & 3/2 & -1/2 \end{array}\right]
> \xrightarrow{R_1 - 2R_2}
> \left[\begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & 3/2 & -1/2 \end{array}\right] .
> $$
>
> So $\mathbf{u} = (-2, 3/2)$, $\mathbf{v} = (1, -1/2)$ and $A^{-1} = \begin{bmatrix} -2 & 1 \\ 3/2 & -1/2 \end{bmatrix}$, in agreement with [[§14 The Inverse of a Matrix#^thm-14-2|Theorem §14.2]]: $\frac{1}{4 - 6}\begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix}$.
>
> **(b)** Find the inverse of $A = \begin{bmatrix} 1 & 2 & 1 \\ 1 & 3 & 2 \\ 1 & 0 & 1 \end{bmatrix}$.
>
> $$
> \left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 1 & 3 & 2 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \end{array}\right]
> \xrightarrow[R_3 - R_1]{R_2 - R_1}
> \left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -1 & 1 & 0 \\ 0 & -2 & 0 & -1 & 0 & 1 \end{array}\right]
> \xrightarrow[R_3 + 2R_2]{R_1 - 2R_2}
> \left[\begin{array}{ccc|ccc} 1 & 0 & -1 & 3 & -2 & 0 \\ 0 & 1 & 1 & -1 & 1 & 0 \\ 0 & 0 & 2 & -3 & 2 & 1 \end{array}\right]
> $$
>
> $$
> \xrightarrow{R_3 \div 2}
> \left[\begin{array}{ccc|ccc} 1 & 0 & -1 & 3 & -2 & 0 \\ 0 & 1 & 1 & -1 & 1 & 0 \\ 0 & 0 & 1 & -3/2 & 1 & 1/2 \end{array}\right]
> \xrightarrow[R_2 - R_3]{R_1 + R_3}
> \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3/2 & -1 & 1/2 \\ 0 & 1 & 0 & 1/2 & 0 & -1/2 \\ 0 & 0 & 1 & -3/2 & 1 & 1/2 \end{array}\right] .
> $$
>
> $A \sim I$, so $A$ is invertible and
>
> $$
> A^{-1} = \begin{bmatrix} 3/2 & -1 & 1/2 \\ 1/2 & 0 & -1/2 \\ -3/2 & 1 & 1/2 \end{bmatrix} .
> $$
>
> Check, row 1 of $A$ times the columns of $A^{-1}$: $\tfrac32 + 1 - \tfrac32 = 1$, $-1 + 0 + 1 = 0$, $\tfrac12 - 1 + \tfrac12 = 0$; rows 2 and 3 likewise give $(0, 1, 0)$ and $(0, 0, 1)$, so $AA^{-1} = I$.
>
> **(c) A singular matrix.** For $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$,
>
> $$
> \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 2 & 4 & 0 & 1 \end{array}\right]
> \xrightarrow{R_2 - 2R_1}
> \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 0 & -2 & 1 \end{array}\right] .
> $$
>
> The left half has only one pivot, so $A$ is not row equivalent to $I$ and has no inverse (as found in [[§14 The Inverse of a Matrix#^ex-14-1|Example §14.1]](b); also $\det A = 4 - 4 = 0$).
>
> *Source: 235 lectures L8, L9*

^ex-15-2

> [!remark]- Remark: Numerical Note
> In practical work $A^{-1}$ is seldom computed, unless its entries are needed. Computing both $A^{-1}$ and $A^{-1}\mathbf{b}$ takes about three times as many arithmetic operations as solving $A\mathbf{x} = \mathbf{b}$ by row reduction, and row reduction may be more accurate.

^rem-15-4