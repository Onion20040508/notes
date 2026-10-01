---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 12
lay: "2.2"
aliases: ["Lay 2.2"]
tags: [applied-linear-algebra, math235]
---
← [[§11 Matrix Operations]] · ↑ [[· 2 Matrix Algebra]] · [[§13 Characterizations of Invertible Matrices]] →

*Lay, Section 2.2 · MATH 235 lectures L7, L8, L9.*

A square matrix $A$ is invertible when some matrix $A^{-1}$ undoes it from both sides, $A^{-1}A = AA^{-1} = I$, the matrix analogue of the reciprocal of a nonzero number. For $2 \times 2$ matrices there is a formula, and the number $ad - bc$ decides whether the inverse exists. When $A^{-1}$ exists, $A\mathbf{x} = \mathbf{b}$ has exactly one solution, $\mathbf{x} = A^{-1}\mathbf{b}$; inverses of products and transposes follow simple rules. Each elementary row operation is multiplication on the left by an elementary matrix. This gives the main theorem: $A$ is invertible exactly when it row reduces to $I$, and the same row operations turn $I$ into $A^{-1}$. That is the algorithm for computing inverses: row reduce $[\,A \ \ I\,]$.

## Invertible Matrices

The reciprocal $5^{-1}$ of $5$ satisfies $5^{-1} \cdot 5 = 1$ and $5 \cdot 5^{-1} = 1$. The matrix version requires *both* equations, since matrix multiplication is not commutative, and avoids the slanted-line notation for division.

> [!definition] Definition §12.1: Invertible Matrix; Inverse; Singular
> An $n \times n$ matrix $A$ is **invertible** if there is an $n \times n$ matrix $C$ such that
>
> $$
> CA = I \qquad\text{and}\qquad AC = I,
> $$
>
> where $I = I_n$. Such a $C$ is an **inverse** of $A$. By Proposition §12.1 it is unique; it is denoted $A^{-1}$, so that
>
> $$
> A^{-1}A = I \qquad\text{and}\qquad AA^{-1} = I .
> $$
>
> A matrix that is not invertible is called **singular**, and an invertible matrix is called **nonsingular**. Only square matrices are called invertible. (If an $m \times n$ matrix $A$ had $n \times m$ matrices $C$, $D$ with $CA = I_n$ and $AD = I_m$, then $m = n$ and $C = D$; see Lay's Exercises 23–25 in Section 2.1.)
>
> *Lay: 2.2 (text)*

^def-12-1

> [!remark]- Connections
> - Rigorous treatment: [[§10 Invertibility and Isomorphisms#^ladr-3-80|LADR 3.80]] (invertible square matrix) and, for linear maps, [[§10 Invertibility and Isomorphisms#^ladr-3-59|LADR 3.59]]–[[§10 Invertibility and Isomorphisms#^ladr-3-60|3.60]] (inverse, unique by the same one-line argument as Proposition §12.1); the matrix of the inverse map is the inverse matrix, [[§10 Invertibility and Isomorphisms#^ladr-3-86|LADR 3.86]].
> - The invertible $n \times n$ matrices form a group under multiplication, the general linear group: [[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]]. Theorem §12.4 below lists the group properties (inverses of inverses and of products).

> [!theorem] Proposition §12.1: The Inverse Is Unique
> If $B$ and $C$ are both inverses of $A$, then $B = C$.
>
> *Lay: 2.2 (text)*

^prop-12-1

> [!proof]+ Proof
> Using $AC = I$, associativity and $BA = I$,
>
> $$
> B = BI = B(AC) = (BA)C = IC = C .
> $$

^pf-12-1

*Uses:* [[§11 Matrix Operations#^thm-11-6|§11.6]] (associativity, identity)

> [!example] Example §12.1: Checking an Inverse, and a Matrix with No Inverse
> **(a)** For $A = \begin{bmatrix} 2 & 5 \\ -3 & -7 \end{bmatrix}$ and $C = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}$,
>
> $$
> AC = \begin{bmatrix} -14 + 15 & -10 + 10 \\ 21 - 21 & 15 - 14 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \qquad
> CA = \begin{bmatrix} -14 + 15 & -35 + 35 \\ 6 - 6 & 15 - 14 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix},
> $$
>
> so $C = A^{-1}$.
>
> **(b)** Not every nonzero matrix is invertible. $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ satisfies $AX = 0$ for $X = \begin{bmatrix} 0 & -2 \\ 0 & 1 \end{bmatrix} \ne 0$ ([[§11 Matrix Operations#^ex-11-3|Example §11.3]](c)). If some $B$ had $BA = I$, then
>
> $$
> X = IX = (BA)X = B(AX) = B0 = 0,
> $$
>
> a contradiction. So $A$ has no inverse. More generally, a matrix $A$ with $AX = 0$ for some nonzero $X$ is never invertible. The same argument shows that $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ is not invertible, since $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ -1 & -1 \end{bmatrix} = 0$.
>
> *Lay: Example 2.2.1*
> *Source: 235 lectures L7, L9*

^ex-12-1

## The 2 × 2 Case

> [!definition] Definition §12.2: Determinant of a 2 × 2 Matrix
> The **determinant** of $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is the number
>
> $$
> \det A = ad - bc .
> $$
>
> *Lay: 2.2 (text)*

^def-12-2

> [!theorem] Theorem §12.2: The Inverse of a 2 × 2 Matrix
> Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. If $ad - bc \ne 0$, then $A$ is invertible and
>
> $$
> A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} .
> $$
>
> If $ad - bc = 0$, then $A$ is not invertible. Thus a $2 \times 2$ matrix is invertible if and only if $\det A \ne 0$.
>
> *Lay: Theorem 4 (2.2)*

^thm-12-2

> [!proof]+ Proof
> (Lay outlines the proof in Exercises 25 and 26.)
>
> **$ad - bc \ne 0$.** Multiply out:
>
> $$
> \begin{bmatrix} a & b \\ c & d \end{bmatrix}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} = \begin{bmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{bmatrix} = (ad - bc)I, \qquad
> \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} da - bc & db - bd \\ -ca + ac & -cb + ad \end{bmatrix} = (ad - bc)I .
> $$
>
> Dividing by $ad - bc$ (Theorem §11.6(d)) shows that the matrix $\frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ satisfies both equations of Definition §12.1.
>
> **$ad - bc = 0$.** We find a nonzero $\mathbf{x}$ with $A\mathbf{x} = \mathbf{0}$. If $(a, b) \ne (0, 0)$, take $\mathbf{x} = \begin{bmatrix} -b \\ a \end{bmatrix} \ne \mathbf{0}$:
>
> $$
> A\mathbf{x} = \begin{bmatrix} -ab + ba \\ -cb + da \end{bmatrix} = \begin{bmatrix} 0 \\ ad - bc \end{bmatrix} = \mathbf{0} .
> $$
>
> If $a = b = 0$ and $(c, d) \ne (0, 0)$, take $\mathbf{x} = \begin{bmatrix} d \\ -c \end{bmatrix}$: $A\mathbf{x} = \begin{bmatrix} 0 \\ cd - dc \end{bmatrix} = \mathbf{0}$. If $A = 0$, any nonzero $\mathbf{x}$ works. Now if $A$ had an inverse, then $\mathbf{x} = A^{-1}(A\mathbf{x}) = A^{-1}\mathbf{0} = \mathbf{0}$, a contradiction. So $A$ is not invertible.

^pf-12-2

*Uses:* [[§12 The Inverse of a Matrix#^def-12-1|Def. §12.1]], [[§11 Matrix Operations#^thm-11-6|§11.6]]

The determinant is defined for all $n \times n$ matrices in [[§20 Introduction to Determinants|§20]], and $A$ is invertible exactly when $\det A \ne 0$ ([[§21 Properties of Determinants|§21]]). The lecture notes the cost: row reduction inverts an $N \times N$ matrix in about $N^3$ operations, while a determinant formula built like $ad - bc$ has $N!$ terms.

> [!theorem] Theorem §12.3: Solving Ax = b with the Inverse
> If $A$ is an invertible $n \times n$ matrix, then for each $\mathbf{b}$ in $\mathbb{R}^n$ the equation $A\mathbf{x} = \mathbf{b}$ has the unique solution $\mathbf{x} = A^{-1}\mathbf{b}$.
>
> *Lay: Theorem 5 (2.2)*

^thm-12-3

> [!proof]+ Proof
> **Existence.** $A(A^{-1}\mathbf{b}) = (AA^{-1})\mathbf{b} = I\mathbf{b} = \mathbf{b}$, so $A^{-1}\mathbf{b}$ is a solution.
>
> **Uniqueness.** If $A\mathbf{u} = \mathbf{b}$, multiply both sides on the left by $A^{-1}$: $A^{-1}A\mathbf{u} = A^{-1}\mathbf{b}$, that is, $I\mathbf{u} = A^{-1}\mathbf{b}$, so $\mathbf{u} = A^{-1}\mathbf{b}$.

^pf-12-3

*Uses:* [[§12 The Inverse of a Matrix#^def-12-1|Def. §12.1]], [[§11 Matrix Operations#^thm-11-2|§11.2]]

> [!example] Example §12.2: A 2 × 2 Inverse and a System
> Find the inverse of $A = \begin{bmatrix} 3 & 4 \\ 5 & 6 \end{bmatrix}$ and use it to solve
>
> $$
> \begin{aligned} 3x_1 + 4x_2 &= 3 \\ 5x_1 + 6x_2 &= 7 \end{aligned}
> $$
>
> Since $\det A = 3(6) - 4(5) = -2 \ne 0$, $A$ is invertible, and by Theorem §12.2
>
> $$
> A^{-1} = \frac{1}{-2}\begin{bmatrix} 6 & -4 \\ -5 & 3 \end{bmatrix} = \begin{bmatrix} 6/(-2) & -4/(-2) \\ -5/(-2) & 3/(-2) \end{bmatrix} = \begin{bmatrix} -3 & 2 \\ 5/2 & -3/2 \end{bmatrix} .
> $$
>
> The system is $A\mathbf{x} = \mathbf{b}$ with $\mathbf{b} = (3, 7)$, so by Theorem §12.3
>
> $$
> \mathbf{x} = A^{-1}\mathbf{b} = \begin{bmatrix} -3 & 2 \\ 5/2 & -3/2 \end{bmatrix}\begin{bmatrix} 3 \\ 7 \end{bmatrix} = \begin{bmatrix} -9 + 14 \\ 15/2 - 21/2 \end{bmatrix} = \begin{bmatrix} 5 \\ -3 \end{bmatrix} .
> $$
>
> (Check: $3(5) + 4(-3) = 3$, $5(5) + 6(-3) = 7$.) Lay notes that $\mathbf{x} = A^{-1}\mathbf{b}$ is seldom used numerically, because row reducing $[\,A \ \ \mathbf{b}\,]$ is nearly always faster and more accurate; the $2 \times 2$ case, done mentally, is the exception. The lecture adds the case where it pays: if hundreds of systems $A\mathbf{x} = \mathbf{b}_1$, $A\mathbf{x} = \mathbf{b}_2$, … share the same $A$, compute $A^{-1}$ once (about $N^3$ operations), and then each solution $\mathbf{x}_i = A^{-1}\mathbf{b}_i$ costs only a matrix–vector product (about $N^2$ operations). (The LU factorization of [[§15 Matrix Factorizations|§15]] does this better.)
>
> *Lay: Examples 2.2.2 and 2.2.4*
> *Source: 235 lecture L8*

^ex-12-2

> [!remark]- Remark: Flexibility and Stiffness Matrices
> A horizontal elastic beam supported at both ends carries forces $\mathbf{f} = (f_1, f_2, f_3)$ at three points, and $\mathbf{y} = (y_1, y_2, y_3)$ lists the deflections at those points. By Hooke's law, $\mathbf{y} = D\mathbf{f}$ for a **flexibility matrix** $D$; its inverse $D^{-1}$ is the **stiffness matrix**. Since $D = DI_3 = [\,D\mathbf{e}_1 \ D\mathbf{e}_2 \ D\mathbf{e}_3\,]$ and $\mathbf{e}_1$ is a unit downward force at point 1, column 1 of $D$ lists the deflections caused by a unit force at point 1. Likewise $D^{-1} = [\,D^{-1}\mathbf{e}_1 \ D^{-1}\mathbf{e}_2 \ D^{-1}\mathbf{e}_3\,]$, and reading $\mathbf{e}_1$ as a deflection, column 1 of $D^{-1}$ lists the forces that produce a unit deflection at point 1 and none at points 2 and 3; one or two of these forces must be negative (upward). If flexibility is measured in inches per pound, stiffness is in pounds per inch. (Lay's Example 3.)

^rem-12-1

## Properties of Inverses

> [!theorem] Theorem §12.4: Properties of Invertible Matrices
> **(a)** If $A$ is invertible, then $A^{-1}$ is invertible and $(A^{-1})^{-1} = A$.
>
> **(b)** If $A$ and $B$ are $n \times n$ invertible matrices, then so is $AB$, and the inverse of $AB$ is the product of the inverses of $A$ and $B$ in the reverse order:
>
> $$
> (AB)^{-1} = B^{-1}A^{-1} .
> $$
>
> **(c)** If $A$ is invertible, then so is $A^T$, and the inverse of $A^T$ is the transpose of $A^{-1}$:
>
> $$
> (A^T)^{-1} = (A^{-1})^T .
> $$
>
> *Lay: Theorem 6 (2.2)*

^thm-12-4

> [!proof]+ Proof
> Each part is proved by checking that the proposed matrix satisfies the definition of the inverse (Definition §12.1): multiplied on the left and on the right, it gives $I$.
>
> **(a)** We need $C$ with $A^{-1}C = I$ and $CA^{-1} = I$. These equations hold with $C = A$, so $A^{-1}$ is invertible with inverse $A$.
>
> **(b)** By associativity,
>
> $$
> (AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I, \qquad
> (B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I .
> $$
>
> **(c)** By Theorem §11.7(d) read from right to left, $(A^{-1})^TA^T = (AA^{-1})^T = I^T = I$, and similarly $A^T(A^{-1})^T = (A^{-1}A)^T = I^T = I$. So $A^T$ is invertible with inverse $(A^{-1})^T$.

^pf-12-4

*Uses:* [[§12 The Inverse of a Matrix#^def-12-1|Def. §12.1]], [[§11 Matrix Operations#^thm-11-6|§11.6]], [[§11 Matrix Operations#^thm-11-7|§11.7]]

> [!theorem] Corollary §12.5: Products of Invertible Matrices
> The product of $n \times n$ invertible matrices is invertible, and its inverse is the product of their inverses in the reverse order:
>
> $$
> (A_1A_2 \cdots A_k)^{-1} = A_k^{-1} \cdots A_2^{-1}A_1^{-1} .
> $$
>
> *Lay: 2.2 (text)*

^cor-12-5

> [!proof]+ Proof
> Induction on $k$; $k = 2$ is Theorem §12.4(b). If $A_1 \cdots A_{k-1}$ is invertible with inverse $A_{k-1}^{-1} \cdots A_1^{-1}$, then by Theorem §12.4(b) applied to the two matrices $A_1 \cdots A_{k-1}$ and $A_k$, the product $A_1 \cdots A_k$ is invertible with inverse $A_k^{-1}(A_1 \cdots A_{k-1})^{-1} = A_k^{-1}A_{k-1}^{-1} \cdots A_1^{-1}$.

^pf-12-5

*Uses:* [[§12 The Inverse of a Matrix#^thm-12-4|§12.4]]

> [!example] Example §12.3: Using the Rules for Inverses
> **(a)** Let $A$ and $B$ be invertible $n \times n$ matrices. Find $(-2AB^T)^{-1}$.
>
> First, for a scalar $r \ne 0$ and invertible $M$, $rM$ is invertible with $(rM)^{-1} = r^{-1}M^{-1}$, because $(rM)(r^{-1}M^{-1}) = (r r^{-1})MM^{-1} = I$ and likewise in the other order (Theorem §11.6(d); Lay's Practice Problem 3). Then by Theorem §12.4(b), extended to three factors by Corollary §12.5, and (c),
>
> $$
> (-2AB^T)^{-1} = \big((-2I)\,A\,B^T\big)^{-1} = (B^T)^{-1}A^{-1}(-2I)^{-1} = -\tfrac12\,(B^{-1})^TA^{-1} .
> $$
>
> **(b)** Solve $AB = C^2$ for $B$.
>
> *$A$ invertible.* Multiply on the left by $A^{-1}$: $B = A^{-1}C^2$ (not $C^2A^{-1}$; the order matters). For instance, with $A = \begin{bmatrix} 2 & 5 \\ -3 & -7 \end{bmatrix}$ (so $A^{-1} = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}$, Example §12.1) and $C = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, $C^2 = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ and
>
> $$
> B = A^{-1}C^2 = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} -7 & -19 \\ 3 & 8 \end{bmatrix} .
> $$
>
> (Check: $AB = \begin{bmatrix} -14 + 15 & -38 + 40 \\ 21 - 21 & 57 - 56 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = C^2$.) The solution is unique.
>
> *$A$ singular.* Then there may be no solution or infinitely many. Take $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$. Every column of $AB$ is a combination of the columns of $A$ (Proposition §11.3), hence a multiple of $(1, 2)$. With $C = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, the first column $(1, 0)$ of $C^2$ is not such a multiple, so $AB = C^2$ has no solution. With $C = A$ instead, $C^2 = A^2 = \begin{bmatrix} 5 & 10 \\ 10 & 20 \end{bmatrix} = 5A$, and $B = 5I$ is one solution; then $B = 5I + X$ is a solution for every $X$ with $AX = 0$, that is (Example §11.3(c)), for all
>
> $$
> B = \begin{bmatrix} 5 - 2s & -2t \\ s & 5 + t \end{bmatrix}, \qquad s, t \text{ arbitrary} .
> $$
>
> *Source: MATH 235 checklist (Sections 2.2–2.3)*

^ex-12-3

## Elementary Matrices

An invertible matrix is row equivalent to an identity matrix, and $A^{-1}$ can be found by watching the row reduction of $A$ to $I$. The link is that row operations are matrix multiplications.

> [!definition] Definition §12.3: Elementary Matrix
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

^def-12-3

> [!definition] Definition §12.4: Permutation Matrix
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

^def-12-4

> [!remark]- Connections
> - Permutation matrices are the matrices $M(\sigma)$ of the linear maps that permute the standard basis, and $\sigma \mapsto M(\sigma)$ is an injective homomorphism $S_n \to GL_n$: [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-5|493 Def. §19.5]], [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|493 Prop. §19.5]]. The count $n!$ is the order of $S_n$.

> [!theorem] Proposition §12.6: Row Operations Are Left Multiplications
> If an elementary row operation is performed on an $m \times n$ matrix $A$, the resulting matrix can be written as $EA$, where the $m \times m$ matrix $E$ is created by performing the same row operation on $I_m$.
>
> *Lay: 2.2 (text)*

^prop-12-6

> [!proof]+ Proof
> (Lay proves the $3 \times 3$ cases in Exercises 27–28; here is the general argument.) Each elementary row operation replaces the rows of a matrix by fixed linear combinations of its rows, with coefficients that depend only on the operation and not on the matrix: there are numbers $e_{ik}$ such that, for every matrix $M$ with $m$ rows,
>
> $$
> \operatorname{row}_i(\text{new } M) = \sum_{k=1}^m e_{ik}\operatorname{row}_k(M), \qquad i = 1, \ldots, m .
> $$
>
> (A replacement "row $i$ + $a$ · row $j$" has $e_{ii} = 1$, $e_{ij} = a$ and otherwise $e_{kk} = 1$, all other $e_{k\ell} = 0$; an interchange and a scaling are similar.) Applied to $M = I_m$, whose $k$th row is $\mathbf{e}_k^T$, this gives $\operatorname{row}_i(E) = \sum_k e_{ik}\mathbf{e}_k^T = [\,e_{i1} \ \cdots \ e_{im}\,]$. Now by equation (2) of §11 and the row–column rule,
>
> $$
> \operatorname{row}_i(EA) = \operatorname{row}_i(E)\,A = [\,e_{i1} \ \cdots \ e_{im}\,]\,A = \sum_{k=1}^m e_{ik}\operatorname{row}_k(A),
> $$
>
> which is row $i$ of the matrix obtained from $A$ by the operation.

^pf-12-6

*Uses:* [[§11 Matrix Operations#^prop-11-5|§11.5]], [[§11 Matrix Operations#^prop-11-4|§11.4]]

> [!theorem] Proposition §12.7: Elementary Matrices Are Invertible
> Each elementary matrix $E$ is invertible. The inverse of $E$ is the elementary matrix of the same type that transforms $E$ back into $I$.
>
> *Lay: 2.2 (text)*

^prop-12-7

> [!proof]+ Proof
> Row operations are reversible (§1): a replacement adding $a$ times row $j$ to row $i$ is undone by adding $-a$ times row $j$ to row $i$, an interchange by the same interchange, and scaling a row by $c \ne 0$ by scaling it by $1/c$. Let $E$ come from $I$ by an operation, and let $F$ be the elementary matrix of the reverse operation. By Proposition §12.6, $FE$ is the result of applying the reverse operation to $E$, which is $I$. Likewise $EF$ is the result of applying the original operation to $F$, which undoes the reverse operation and gives $I$. So $FE = EF = I$ and $F = E^{-1}$.

^pf-12-7

*Uses:* [[§12 The Inverse of a Matrix#^prop-12-6|§12.6]], [[§12 The Inverse of a Matrix#^def-12-1|Def. §12.1]], [[§1 Systems of Linear Equations|§1]] (row operations are reversible)

> [!example] Example §12.4: Elementary and Permutation Matrices
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

^ex-12-4

> [!theorem] Theorem §12.8: Invertibility and Row Reduction
> An $n \times n$ matrix $A$ is invertible if and only if $A$ is row equivalent to $I_n$, and in this case, any sequence of elementary row operations that reduces $A$ to $I_n$ also transforms $I_n$ into $A^{-1}$.
>
> *Lay: Theorem 7 (2.2)*

^thm-12-8

> [!proof]+ Proof
> **Invertible $\Rightarrow$ row equivalent to $I_n$.** Suppose $A$ is invertible. By Theorem §12.3 the equation $A\mathbf{x} = \mathbf{b}$ has a solution for each $\mathbf{b}$, so $A$ has a pivot position in every row (Theorem 4 of §4). Because $A$ is square, the $n$ pivot positions must lie on the main diagonal (each of the $n$ rows and each of the $n$ columns contains exactly one pivot, and pivots move strictly down and to the right), so the reduced echelon form of $A$ is $I_n$. That is, $A \sim I_n$.
>
> **Row equivalent to $I_n$ $\Rightarrow$ invertible.** Conversely, suppose $A \sim I_n$. Each step of the row reduction is left multiplication by an elementary matrix (Proposition §12.6), so there are elementary matrices $E_1, \ldots, E_p$ with
>
> $$
> A \sim E_1A \sim E_2(E_1A) \sim \cdots \sim E_p(E_{p-1} \cdots E_1A) = I_n,
> \qquad\text{that is,}\qquad
> E_p \cdots E_1A = I_n . \tag{1}
> $$
>
> The product $E_p \cdots E_1$ of invertible matrices is invertible (Proposition §12.7, Corollary §12.5), so multiplying (1) on the left by its inverse,
>
> $$
> (E_p \cdots E_1)^{-1}(E_p \cdots E_1)A = (E_p \cdots E_1)^{-1}I_n, \qquad A = (E_p \cdots E_1)^{-1} .
> $$
>
> Thus $A$ is invertible, as the inverse of an invertible matrix (Theorem §12.4(a)), and
>
> $$
> A^{-1} = \big[(E_p \cdots E_1)^{-1}\big]^{-1} = E_p \cdots E_1 = E_p \cdots E_1 \cdot I_n .
> $$
>
> This says that $A^{-1}$ results from applying the operations of $E_1, \ldots, E_p$ successively to $I_n$: the same sequence that reduced $A$ to $I_n$ in (1).

^pf-12-8

*Uses:* [[§12 The Inverse of a Matrix#^thm-12-3|§12.3]], [[§4 The Matrix Equation Ax = b|§4]] (Theorem 4), [[§2 Row Reduction and Echelon Forms|§2]] (pivot positions, reduced echelon form), [[§12 The Inverse of a Matrix#^prop-12-6|§12.6]], [[§12 The Inverse of a Matrix#^prop-12-7|§12.7]], [[§12 The Inverse of a Matrix#^cor-12-5|§12.5]], [[§12 The Inverse of a Matrix#^thm-12-4|§12.4]]

> [!remark] Remark: An Invertible Matrix Is a Product of Elementary Matrices
> The proof shows $A = (E_p \cdots E_1)^{-1} = E_1^{-1} \cdots E_p^{-1}$, a product of elementary matrices (Proposition §12.7). So the invertible matrices are exactly the products of elementary matrices; the lecture phrases it as products of replacement matrices $E_{ij}(a)$, permutation matrices and scalings. For example, if $E_{12}(7)\,P\,E_{31}(-2)\,A = I$ for a permutation matrix $P$, then $A^{-1} = E_{12}(7)\,P\,E_{31}(-2)$, and row reducing $[\,A \ \ I\,]$ builds exactly this product in the right half:
>
> $$
> [\,A \ \ I\,] \to [\,E_{31}(-2)A \ \ E_{31}(-2)\,] \to [\,PE_{31}(-2)A \ \ PE_{31}(-2)\,] \to [\,E_{12}(7)PE_{31}(-2)A \ \ E_{12}(7)PE_{31}(-2)\,] = [\,I \ \ A^{-1}\,] .
> $$
>
> *Source: 235 lecture L9*

^rem-12-2

## An Algorithm for Finding the Inverse

Placing $A$ and $I$ side by side, row operations on $[\,A \ \ I\,]$ act identically on both halves. By Theorem §12.8, either some row operations turn $A$ into $I_n$, and then they turn $I_n$ into $A^{-1}$, or $A$ is not invertible.

> [!remark] Remark: Method — Finding the Inverse of a Matrix
> 1. Form the $n \times 2n$ augmented matrix $[\,A \ \ I\,]$.
> 2. Row reduce it. If $A$ is row equivalent to $I$, then $[\,A \ \ I\,]$ is row equivalent to $[\,I \ \ A^{-1}\,]$: read off $A^{-1}$ on the right.
> 3. If at some stage the left half has fewer than $n$ pivots (for instance a row of zeros appears in it), then $A$ is not row equivalent to $I$ and $A$ does not have an inverse.
> 4. Check the answer by computing $AA^{-1}$. Checking $A^{-1}A = I$ is unnecessary, since $A$ is invertible (Corollary §13.2 in [[§13 Characterizations of Invertible Matrices|§13]]).
>
> For a $2 \times 2$ matrix, Theorem §12.2 is faster.
>
> *Lay: 2.2, Algorithm for Finding A⁻¹*

^rem-12-3

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

^rem-12-4

> [!example] Example §12.5: Inverting by Row Reduction
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
> So $\mathbf{u} = (-2, 3/2)$, $\mathbf{v} = (1, -1/2)$ and $A^{-1} = \begin{bmatrix} -2 & 1 \\ 3/2 & -1/2 \end{bmatrix}$, in agreement with Theorem §12.2: $\frac{1}{4 - 6}\begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix}$.
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
> The left half has only one pivot, so $A$ is not row equivalent to $I$ and has no inverse (as found in Example §12.1(b); also $\det A = 4 - 4 = 0$).
>
> *Source: 235 lectures L8, L9*

^ex-12-5

> [!remark]- Remark: Numerical Note
> In practical work $A^{-1}$ is seldom computed, unless its entries are needed. Computing both $A^{-1}$ and $A^{-1}\mathbf{b}$ takes about three times as many arithmetic operations as solving $A\mathbf{x} = \mathbf{b}$ by row reduction, and row reduction may be more accurate.

^rem-12-5
