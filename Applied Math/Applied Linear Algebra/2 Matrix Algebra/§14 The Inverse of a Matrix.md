---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 14
lay: "2.2"
aliases: ["Lay 2.2"]
tags: [applied-linear-algebra, math235]
---
← [[§13 Properties of Matrix Multiplication, Powers, and Transposes]] · ↑ [[· 2 Matrix Algebra]] · [[§15 Elementary Matrices and the Inversion Algorithm]] →

*Lay, Section 2.2 · MATH 235 lectures L7, L8, L9.*

A square matrix $A$ is invertible when some matrix $A^{-1}$ undoes it from both sides, $A^{-1}A = AA^{-1} = I$, the matrix analogue of the reciprocal of a nonzero number. For $2 \times 2$ matrices there is a formula, and the number $ad - bc$ decides whether the inverse exists. When $A^{-1}$ exists, $A\mathbf{x} = \mathbf{b}$ has exactly one solution, $\mathbf{x} = A^{-1}\mathbf{b}$; inverses of products and transposes follow simple rules. Each elementary row operation is multiplication on the left by an elementary matrix. This gives the main theorem: $A$ is invertible exactly when it row reduces to $I$, and the same row operations turn $I$ into $A^{-1}$. That is the algorithm for computing inverses: row reduce $[\,A \ \ I\,]$.

## Invertible Matrices

The reciprocal $5^{-1}$ of $5$ satisfies $5^{-1} \cdot 5 = 1$ and $5 \cdot 5^{-1} = 1$. The matrix version requires *both* equations, since matrix multiplication is not commutative, and avoids the slanted-line notation for division.

> [!definition] Definition §17.1: Invertible Matrix; Inverse; Singular
> An $n \times n$ matrix $A$ is **invertible** if there is an $n \times n$ matrix $C$ such that
>
> $$
> CA = I \qquad\text{and}\qquad AC = I,
> $$
>
> where $I = I_n$. Such a $C$ is an **inverse** of $A$. By [[§14 The Inverse of a Matrix#^prop-14-1|Proposition §14.1]] it is unique; it is denoted $A^{-1}$, so that
>
> $$
> A^{-1}A = I \qquad\text{and}\qquad AA^{-1} = I .
> $$
>
> A matrix that is not invertible is called **singular**, and an invertible matrix is called **nonsingular**. Only square matrices are called invertible. (If an $m \times n$ matrix $A$ had $n \times m$ matrices $C$, $D$ with $CA = I_n$ and $AD = I_m$, then $m = n$ and $C = D$; see Lay's Exercises 23–25 in Section 2.1.)
>
> *Lay: 2.2 (text)*

^def-14-1

> [!remark]- Connections
> - Rigorous treatment: [[§10 Invertibility and Isomorphisms#^ladr-3-80|LADR 3.80]] (invertible square matrix) and, for linear maps, [[§10 Invertibility and Isomorphisms#^ladr-3-59|LADR 3.59]]–[[§10 Invertibility and Isomorphisms#^ladr-3-60|3.60]] (inverse, unique by the same one-line argument as [[§14 The Inverse of a Matrix#^prop-14-1|Proposition §14.1]]); the matrix of the inverse map is the inverse matrix, [[§10 Invertibility and Isomorphisms#^ladr-3-86|LADR 3.86]].
> - The invertible $n \times n$ matrices form a group under multiplication, the general linear group: [[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]]. [[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]] below lists the group properties (inverses of inverses and of products).

> [!theorem] Proposition §17.1: The Inverse Is Unique
> If $B$ and $C$ are both inverses of $A$, then $B = C$.
>
> *Lay: 2.2 (text)*

^prop-14-1

> [!proof]+ Proof
> Using $AC = I$, associativity and $BA = I$,
>
> $$
> B = BI = B(AC) = (BA)C = IC = C .
> $$

^pf-14-1

*Uses:* [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|§13.1]] (associativity, identity)

> [!example] Example §17.1: Checking an Inverse, and a Matrix with No Inverse
> **(a)** For $A = \begin{bmatrix} 2 & 5 \\ -3 & -7 \end{bmatrix}$ and $C = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}$,
>
> $$
> AC = \begin{bmatrix} -14 + 15 & -10 + 10 \\ 21 - 21 & 15 - 14 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \qquad
> CA = \begin{bmatrix} -14 + 15 & -35 + 35 \\ 6 - 6 & 15 - 14 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix},
> $$
>
> so $C = A^{-1}$.
>
> **(b)** Not every nonzero matrix is invertible. $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ satisfies $AX = 0$ for $X = \begin{bmatrix} 0 & -2 \\ 0 & 1 \end{bmatrix} \ne 0$ ([[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-1|Example §13.1]](c)). If some $B$ had $BA = I$, then
>
> $$
> X = IX = (BA)X = B(AX) = B0 = 0,
> $$
>
> a contradiction. So $A$ has no inverse. More generally, a matrix $A$ with $AX = 0$ for some nonzero $X$ is never invertible. The same argument shows that $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ is not invertible, since $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ -1 & -1 \end{bmatrix} = 0$.
>
> *Lay: Example 2.2.1*
> *Source: 235 lectures L7, L9*

^ex-14-1

## The 2 × 2 Case

> [!definition] Definition §17.2: Determinant of a 2 × 2 Matrix
> The **determinant** of $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is the number
>
> $$
> \det A = ad - bc .
> $$
>
> *Lay: 2.2 (text)*

^def-14-2

> [!theorem] Theorem §17.2: The Inverse of a 2 × 2 Matrix
> Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$. If $ad - bc \ne 0$, then $A$ is invertible and
>
> $$
> A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} .
> $$
>
> If $ad - bc = 0$, then $A$ is not invertible. Thus a $2 \times 2$ matrix is invertible if and only if $\det A \ne 0$.
>
> *Lay: Theorem 4 (2.2)*

^thm-14-2

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
> Dividing by $ad - bc$ ([[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|Theorem §13.1]](d)) shows that the matrix $\frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ satisfies both equations of [[§14 The Inverse of a Matrix#^def-14-1|Definition §14.1]].
>
> **$ad - bc = 0$.** We find a nonzero $\mathbf{x}$ with $A\mathbf{x} = \mathbf{0}$. If $(a, b) \ne (0, 0)$, take $\mathbf{x} = \begin{bmatrix} -b \\ a \end{bmatrix} \ne \mathbf{0}$:
>
> $$
> A\mathbf{x} = \begin{bmatrix} -ab + ba \\ -cb + da \end{bmatrix} = \begin{bmatrix} 0 \\ ad - bc \end{bmatrix} = \mathbf{0} .
> $$
>
> If $a = b = 0$ and $(c, d) \ne (0, 0)$, take $\mathbf{x} = \begin{bmatrix} d \\ -c \end{bmatrix}$: $A\mathbf{x} = \begin{bmatrix} 0 \\ cd - dc \end{bmatrix} = \mathbf{0}$. If $A = 0$, any nonzero $\mathbf{x}$ works. Now if $A$ had an inverse, then $\mathbf{x} = A^{-1}(A\mathbf{x}) = A^{-1}\mathbf{0} = \mathbf{0}$, a contradiction. So $A$ is not invertible.

^pf-14-2

*Uses:* [[§14 The Inverse of a Matrix#^def-14-1|Def. §14.1]], [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|§13.1]]

The determinant is defined for all $n \times n$ matrices in [[§24 Introduction to Determinants#^def-24-2|Definition §24.2]], and $A$ is invertible exactly when $\det A \ne 0$ ([[§25 Properties of Determinants#^thm-25-3|Theorem §25.3]]). The lecture notes the cost: row reduction inverts an $N \times N$ matrix in about $N^3$ operations, while a determinant formula built like $ad - bc$ has $N!$ terms.

> [!theorem] Theorem §17.3: Solving Ax = b with the Inverse
> If $A$ is an invertible $n \times n$ matrix, then for each $\mathbf{b}$ in $\mathbb{R}^n$ the equation $A\mathbf{x} = \mathbf{b}$ has the unique solution $\mathbf{x} = A^{-1}\mathbf{b}$.
>
> *Lay: Theorem 5 (2.2)*

^thm-14-3

> [!proof]+ Proof
> **Existence.** $A(A^{-1}\mathbf{b}) = (AA^{-1})\mathbf{b} = I\mathbf{b} = \mathbf{b}$, so $A^{-1}\mathbf{b}$ is a solution.
>
> **Uniqueness.** If $A\mathbf{u} = \mathbf{b}$, multiply both sides on the left by $A^{-1}$: $A^{-1}A\mathbf{u} = A^{-1}\mathbf{b}$, that is, $I\mathbf{u} = A^{-1}\mathbf{b}$, so $\mathbf{u} = A^{-1}\mathbf{b}$.

^pf-14-3

*Uses:* [[§14 The Inverse of a Matrix#^def-14-1|Def. §14.1]], [[§12 Matrix Operations#^thm-12-2|§12.2]]

> [!example] Example §17.2: A 2 × 2 Inverse and a System
> Find the inverse of $A = \begin{bmatrix} 3 & 4 \\ 5 & 6 \end{bmatrix}$ and use it to solve
>
> $$
> \begin{aligned} 3x_1 + 4x_2 &= 3 \\ 5x_1 + 6x_2 &= 7 \end{aligned}
> $$
>
> Since $\det A = 3(6) - 4(5) = -2 \ne 0$, $A$ is invertible, and by [[§14 The Inverse of a Matrix#^thm-14-2|Theorem §14.2]]
>
> $$
> A^{-1} = \frac{1}{-2}\begin{bmatrix} 6 & -4 \\ -5 & 3 \end{bmatrix} = \begin{bmatrix} 6/(-2) & -4/(-2) \\ -5/(-2) & 3/(-2) \end{bmatrix} = \begin{bmatrix} -3 & 2 \\ 5/2 & -3/2 \end{bmatrix} .
> $$
>
> The system is $A\mathbf{x} = \mathbf{b}$ with $\mathbf{b} = (3, 7)$, so by [[§14 The Inverse of a Matrix#^thm-14-3|Theorem §14.3]]
>
> $$
> \mathbf{x} = A^{-1}\mathbf{b} = \begin{bmatrix} -3 & 2 \\ 5/2 & -3/2 \end{bmatrix}\begin{bmatrix} 3 \\ 7 \end{bmatrix} = \begin{bmatrix} -9 + 14 \\ 15/2 - 21/2 \end{bmatrix} = \begin{bmatrix} 5 \\ -3 \end{bmatrix} .
> $$
>
> (Check: $3(5) + 4(-3) = 3$, $5(5) + 6(-3) = 7$.) Lay notes that $\mathbf{x} = A^{-1}\mathbf{b}$ is seldom used numerically, because row reducing $[\,A \ \ \mathbf{b}\,]$ is nearly always faster and more accurate; the $2 \times 2$ case, done mentally, is the exception. The lecture adds the case where it pays: if hundreds of systems $A\mathbf{x} = \mathbf{b}_1$, $A\mathbf{x} = \mathbf{b}_2$, … share the same $A$, compute $A^{-1}$ once (about $N^3$ operations), and then each solution $\mathbf{x}_i = A^{-1}\mathbf{b}_i$ costs only a matrix–vector product (about $N^2$ operations). (The LU factorization, [[§18 Matrix Factorizations#^def-18-2|Definition §18.2]], does this better.)
>
> *Lay: Examples 2.2.2 and 2.2.4*
> *Source: 235 lecture L8*

^ex-14-2

> [!remark]- Remark: Flexibility and Stiffness Matrices
> A horizontal elastic beam supported at both ends carries forces $\mathbf{f} = (f_1, f_2, f_3)$ at three points, and $\mathbf{y} = (y_1, y_2, y_3)$ lists the deflections at those points. By Hooke's law, $\mathbf{y} = D\mathbf{f}$ for a **flexibility matrix** $D$; its inverse $D^{-1}$ is the **stiffness matrix**. Since $D = DI_3 = [\,D\mathbf{e}_1 \ D\mathbf{e}_2 \ D\mathbf{e}_3\,]$ and $\mathbf{e}_1$ is a unit downward force at point 1, column 1 of $D$ lists the deflections caused by a unit force at point 1. Likewise $D^{-1} = [\,D^{-1}\mathbf{e}_1 \ D^{-1}\mathbf{e}_2 \ D^{-1}\mathbf{e}_3\,]$, and reading $\mathbf{e}_1$ as a deflection, column 1 of $D^{-1}$ lists the forces that produce a unit deflection at point 1 and none at points 2 and 3; one or two of these forces must be negative (upward). If flexibility is measured in inches per pound, stiffness is in pounds per inch. (Lay's Example 3.)

^rem-14-1

## Properties of Inverses

> [!theorem] Theorem §17.4: Properties of Invertible Matrices
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

^thm-14-4

> [!proof]+ Proof
> Each part is proved by checking that the proposed matrix satisfies the definition of the inverse ([[§14 The Inverse of a Matrix#^def-14-1|Definition §14.1]]): multiplied on the left and on the right, it gives $I$.
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
> **(c)** By [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|Theorem §13.2]](d) read from right to left, $(A^{-1})^TA^T = (AA^{-1})^T = I^T = I$, and similarly $A^T(A^{-1})^T = (A^{-1}A)^T = I^T = I$. So $A^T$ is invertible with inverse $(A^{-1})^T$.

^pf-14-4

*Uses:* [[§14 The Inverse of a Matrix#^def-14-1|Def. §14.1]], [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|§13.1]], [[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-2|§13.2]]

> [!theorem] Corollary §17.5: Products of Invertible Matrices
> The product of $n \times n$ invertible matrices is invertible, and its inverse is the product of their inverses in the reverse order:
>
> $$
> (A_1A_2 \cdots A_k)^{-1} = A_k^{-1} \cdots A_2^{-1}A_1^{-1} .
> $$
>
> *Lay: 2.2 (text)*

^cor-14-5

> [!proof]+ Proof
> Induction on $k$; $k = 2$ is [[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]](b). If $A_1 \cdots A_{k-1}$ is invertible with inverse $A_{k-1}^{-1} \cdots A_1^{-1}$, then by [[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]](b) applied to the two matrices $A_1 \cdots A_{k-1}$ and $A_k$, the product $A_1 \cdots A_k$ is invertible with inverse $A_k^{-1}(A_1 \cdots A_{k-1})^{-1} = A_k^{-1}A_{k-1}^{-1} \cdots A_1^{-1}$.

^pf-14-5

*Uses:* [[§14 The Inverse of a Matrix#^thm-14-4|§14.4]]

> [!example] Example §17.3: Using the Rules for Inverses
> **(a)** Let $A$ and $B$ be invertible $n \times n$ matrices. Find $(-2AB^T)^{-1}$.
>
> First, for a scalar $r \ne 0$ and invertible $M$, $rM$ is invertible with $(rM)^{-1} = r^{-1}M^{-1}$, because $(rM)(r^{-1}M^{-1}) = (r r^{-1})MM^{-1} = I$ and likewise in the other order ([[§13 Properties of Matrix Multiplication, Powers, and Transposes#^thm-13-1|Theorem §13.1]](d); Lay's Practice Problem 3). Then by [[§14 The Inverse of a Matrix#^thm-14-4|Theorem §14.4]](b), extended to three factors by [[§14 The Inverse of a Matrix#^cor-14-5|Corollary §14.5]], and (c),
>
> $$
> (-2AB^T)^{-1} = \big((-2I)\,A\,B^T\big)^{-1} = (B^T)^{-1}A^{-1}(-2I)^{-1} = -\tfrac12\,(B^{-1})^TA^{-1} .
> $$
>
> **(b)** Solve $AB = C^2$ for $B$.
>
> *$A$ invertible.* Multiply on the left by $A^{-1}$: $B = A^{-1}C^2$ (not $C^2A^{-1}$; the order matters). For instance, with $A = \begin{bmatrix} 2 & 5 \\ -3 & -7 \end{bmatrix}$ (so $A^{-1} = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}$, [[§14 The Inverse of a Matrix#^ex-14-1|Example §14.1]]) and $C = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, $C^2 = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ and
>
> $$
> B = A^{-1}C^2 = \begin{bmatrix} -7 & -5 \\ 3 & 2 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} -7 & -19 \\ 3 & 8 \end{bmatrix} .
> $$
>
> (Check: $AB = \begin{bmatrix} -14 + 15 & -38 + 40 \\ 21 - 21 & 57 - 56 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = C^2$.) The solution is unique.
>
> *$A$ singular.* Then there may be no solution or infinitely many. Take $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$. Every column of $AB$ is a combination of the columns of $A$ ([[§12 Matrix Operations#^prop-12-3|Proposition §12.3]]), hence a multiple of $(1, 2)$. With $C = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, the first column $(1, 0)$ of $C^2$ is not such a multiple, so $AB = C^2$ has no solution. With $C = A$ instead, $C^2 = A^2 = \begin{bmatrix} 5 & 10 \\ 10 & 20 \end{bmatrix} = 5A$, and $B = 5I$ is one solution; then $B = 5I + X$ is a solution for every $X$ with $AX = 0$, that is ([[§13 Properties of Matrix Multiplication, Powers, and Transposes#^ex-13-1|Example §13.1]](c)), for all
>
> $$
> B = \begin{bmatrix} 5 - 2s & -2t \\ s & 5 + t \end{bmatrix}, \qquad s, t \text{ arbitrary} .
> $$
>
> *Source: 235 checklist (2.2–2.3)*

^ex-14-3

*Continued in [[§15 Elementary Matrices and the Inversion Algorithm]]: elementary and permutation matrices, invertibility and row reduction, and the algorithm for finding $A^{-1}$.*
