---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 29
lay: "4.7"
aliases: ["Lay 4.7"]
tags: [applied-linear-algebra, math235]
---
← [[§28 Rank]] · ↑ [[· 4 Vector Spaces]] · [[§30 Applications to Difference Equations]] →

*Lay, Section 4.7 · MATH 235 lecture L17.*

A basis $\mathcal{B}$ of an $n$-dimensional space $V$ gives each vector $\mathbf{x}$ a "name" $[\mathbf{x}]_{\mathcal B} \in \mathbb{R}^n$, the list of weights that build $\mathbf{x}$ from the basis ([[§26 Coordinate Systems#^def-26-1|Definition §26.1]]). Often a problem is posed in one basis $\mathcal{B}$ but is easier to solve in another basis $\mathcal{C}$; Chapters 5 and 7 are full of such changes (eigenvector bases). This section shows that the two coordinate vectors are related by a single invertible matrix, $[\mathbf{x}]_{\mathcal C} = P_{\mathcal C \leftarrow \mathcal B}[\mathbf{x}]_{\mathcal B}$, whose columns are the $\mathcal{C}$-coordinates of the old basis vectors, and how to compute it in $\mathbb{R}^n$ by one row reduction. (This is Section 4.6 in the 6th edition and in the instructor's checklist.)

> [!example] Example §29.1: Two Coordinate Systems for One Space
> Let $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$ and $\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2\}$ be bases of a vector space $V$ such that
>
> $$
> \mathbf{b}_1 = 4\mathbf{c}_1 + \mathbf{c}_2 \qquad\text{and}\qquad \mathbf{b}_2 = -6\mathbf{c}_1 + \mathbf{c}_2 . \qquad (1)
> $$
>
> **(a)** Suppose $\mathbf{x} = 3\mathbf{b}_1 + \mathbf{b}_2$, that is, $[\mathbf{x}]_{\mathcal B} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$. Find $[\mathbf{x}]_{\mathcal C}$.
>
> Apply the coordinate mapping of $\mathcal{C}$ to $\mathbf{x}$. It is linear ([[§26 Coordinate Systems#^thm-26-3|Theorem §26.3]]), so
>
> $$
> [\mathbf{x}]_{\mathcal C} = [3\mathbf{b}_1 + \mathbf{b}_2]_{\mathcal C} = 3[\mathbf{b}_1]_{\mathcal C} + [\mathbf{b}_2]_{\mathcal C} = \big[\, [\mathbf{b}_1]_{\mathcal C}\ \ [\mathbf{b}_2]_{\mathcal C} \,\big] \begin{bmatrix} 3 \\ 1 \end{bmatrix} ,
> $$
>
> writing the linear combination as a matrix times a vector. From (1), $[\mathbf{b}_1]_{\mathcal C} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$ and $[\mathbf{b}_2]_{\mathcal C} = \begin{bmatrix} -6 \\ 1 \end{bmatrix}$, so
>
> $$
> [\mathbf{x}]_{\mathcal C} = \begin{bmatrix} 4 & -6 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 12 - 6 \\ 3 + 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \end{bmatrix} .
> $$
>
> Check directly: $3\mathbf{b}_1 + \mathbf{b}_2 = 3(4\mathbf{c}_1 + \mathbf{c}_2) + (-6\mathbf{c}_1 + \mathbf{c}_2) = 6\mathbf{c}_1 + 4\mathbf{c}_2$.
>
> **(b)** The matrix converting $\mathcal{C}$-coordinates back into $\mathcal{B}$-coordinates is the inverse ([[§29 Change of Basis#^thm-29-2|Theorem §29.2]]):
>
> $$
> P_{\mathcal B \leftarrow \mathcal C} = \begin{bmatrix} 4 & -6 \\ 1 & 1 \end{bmatrix}^{-1} = \frac{1}{4 + 6} \begin{bmatrix} 1 & 6 \\ -1 & 4 \end{bmatrix} = \begin{bmatrix} .1 & .6 \\ -.1 & .4 \end{bmatrix} .
> $$
>
> Check: $\begin{bmatrix} .1 & .6 \\ -.1 & .4 \end{bmatrix}\begin{bmatrix} 6 \\ 4 \end{bmatrix} = \begin{bmatrix} .6 + 2.4 \\ -.6 + 1.6 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = [\mathbf{x}]_{\mathcal B}$.
>
> *Lay: Example 4.7.1 and Practice Problem 2*

^ex-29-1

![[m235-29-1.svg]]
*One vector $\mathbf{x}$, two coordinate grids. Left: the grid of $\mathcal{B}$; $\mathbf{x}$ is the diagonal of the parallelogram on $3\mathbf{b}_1$ and $\mathbf{b}_2$, so $[\mathbf{x}]_{\mathcal B} = (3, 1)$. Right: the grid of $\mathcal{C}$ (with $\mathbf{b}_1 = 4\mathbf{c}_1 + \mathbf{c}_2$, $\mathbf{b}_2 = -6\mathbf{c}_1 + \mathbf{c}_2$ as in Example §29.1, drawn for $\mathbf{c}_1 = (0.6, -0.2)$, $\mathbf{c}_2 = (0.2, 0.6)$); the same $\mathbf{x}$ is $6\mathbf{c}_1 + 4\mathbf{c}_2$, so $[\mathbf{x}]_{\mathcal C} = (6, 4)$.*

The argument of Example §29.1 works for any two bases.

> [!theorem] Theorem §29.1: The Change-of-Coordinates Matrix
> Let $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ and $\mathcal{C} = \{\mathbf{c}_1, \ldots, \mathbf{c}_n\}$ be bases of a vector space $V$. Then there is a unique $n \times n$ matrix $P_{\mathcal C \leftarrow \mathcal B}$ such that
>
> $$
> [\mathbf{x}]_{\mathcal C} = P_{\mathcal C \leftarrow \mathcal B}\, [\mathbf{x}]_{\mathcal B} \qquad \text{for all } \mathbf{x} \in V . \qquad (4)
> $$
>
> The columns of $P_{\mathcal C \leftarrow \mathcal B}$ are the $\mathcal{C}$-coordinate vectors of the vectors in the basis $\mathcal{B}$:
>
> $$
> P_{\mathcal C \leftarrow \mathcal B} = \big[\, [\mathbf{b}_1]_{\mathcal C}\ \ [\mathbf{b}_2]_{\mathcal C}\ \ \cdots\ \ [\mathbf{b}_n]_{\mathcal C} \,\big] . \qquad (5)
> $$
>
> *Lay: Theorem 15 (4.7)*

^thm-29-1

> [!proof]+ Proof
> Lay derives (4) in Example §29.1 and leaves the general proof to Exercises 15 and 16, which outline the following argument (lecture L17 gives the existence part the same way).
>
> **The matrix (5) works.** Let $\mathbf{x} \in V$. Since $\mathcal{B}$ spans $V$, there are scalars $x_1, \ldots, x_n$ with $\mathbf{x} = x_1\mathbf{b}_1 + \cdots + x_n\mathbf{b}_n$, that is, $[\mathbf{x}]_{\mathcal B} = (x_1, \ldots, x_n)$. Apply the coordinate mapping of $\mathcal{C}$, which is linear ([[§26 Coordinate Systems#^thm-26-3|Theorem §26.3]]):
>
> $$
> [\mathbf{x}]_{\mathcal C} = x_1 [\mathbf{b}_1]_{\mathcal C} + \cdots + x_n [\mathbf{b}_n]_{\mathcal C} = \big[\, [\mathbf{b}_1]_{\mathcal C}\ \cdots\ [\mathbf{b}_n]_{\mathcal C} \,\big] \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} ,
> $$
>
> by the definition of a matrix–vector product as a linear combination of the columns ([[§4 The Matrix Equation Ax = b#^def-4-1|Definition §4.1]]). The vector on the right is $[\mathbf{x}]_{\mathcal B}$, so the matrix in (5) satisfies (4).
>
> **Uniqueness.** Suppose $Q$ is any matrix with $[\mathbf{v}]_{\mathcal C} = Q[\mathbf{v}]_{\mathcal B}$ for each $\mathbf{v} \in V$. Take $\mathbf{v} = \mathbf{b}_1$: since $\mathbf{b}_1 = 1 \cdot \mathbf{b}_1 + 0 \cdot \mathbf{b}_2 + \cdots + 0 \cdot \mathbf{b}_n$, $[\mathbf{b}_1]_{\mathcal B} = \mathbf{e}_1$, and $Q\mathbf{e}_1$ is the first column of $Q$. So the first column of $Q$ is $[\mathbf{b}_1]_{\mathcal C}$. Similarly, for $k = 2, \ldots, n$, the $k$th column of $Q$ is $Q\mathbf{e}_k = Q[\mathbf{b}_k]_{\mathcal B} = [\mathbf{b}_k]_{\mathcal C}$. So $Q$ is the matrix (5).

^pf-29-1

*Uses:* [[§26 Coordinate Systems#^thm-26-3|§26.3]], [[§26 Coordinate Systems#^def-26-1|Def. §26.1]] (coordinates of a basis vector), [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]]

> [!definition] Definition §29.1: Change-of-Coordinates Matrix
> The matrix $P_{\mathcal C \leftarrow \mathcal B}$ of Theorem §29.1 is the **change-of-coordinates matrix from $\mathcal{B}$ to $\mathcal{C}$**. Multiplication by $P_{\mathcal C \leftarrow \mathcal B}$ converts $\mathcal{B}$-coordinates into $\mathcal{C}$-coordinates:
>
> $$
> V \xrightarrow{\ [\ ]_{\mathcal B}\ } \mathbb{R}^n \xrightarrow{\ P_{\mathcal C \leftarrow \mathcal B}\ } \mathbb{R}^n \qquad\text{equals}\qquad V \xrightarrow{\ [\ ]_{\mathcal C}\ } \mathbb{R}^n .
> $$
>
> To remember the construction: $P_{\mathcal C \leftarrow \mathcal B}[\mathbf{x}]_{\mathcal B}$ is a linear combination of the columns of $P_{\mathcal C \leftarrow \mathcal B}$, and the result is a $\mathcal{C}$-coordinate vector, so the columns should be $\mathcal{C}$-coordinate vectors too.
>
> *Lay: 4.7 (text and footnote 2)*

^def-29-1

> [!remark]- Connections
> - Rigorous treatment: $P_{\mathcal C \leftarrow \mathcal B}$ is the matrix of the identity operator with input basis $\mathcal{B}$ and output basis $\mathcal{C}$, Axler's $\mathcal{M}(I, (\mathbf{b}), (\mathbf{c}))$. That the two change-of-coordinates matrices are inverse to each other is [[§10 Invertibility and Isomorphisms#^ladr-3-82|LADR 3.82]], and conjugating by it changes the matrix of an operator, $A = C^{-1}BC$, [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]] (in Lay: similarity of matrix representations, Section 5.4, [[§35 Eigenvectors and Linear Transformations#^thm-35-2|Theorem §35.2]]).

> [!theorem] Theorem §29.2: The Change-of-Coordinates Matrix Is Invertible
> $P_{\mathcal C \leftarrow \mathcal B}$ is invertible, and its inverse converts $\mathcal{C}$-coordinates into $\mathcal{B}$-coordinates:
>
> $$
> (P_{\mathcal C \leftarrow \mathcal B})^{-1} = P_{\mathcal B \leftarrow \mathcal C} . \qquad (6)
> $$
>
> *Lay: 4.7 (text), Equation (6)*

^thm-29-2

> [!proof]+ Proof
> The columns of $P_{\mathcal C \leftarrow \mathcal B}$ are the coordinate vectors $[\mathbf{b}_1]_{\mathcal C}, \ldots, [\mathbf{b}_n]_{\mathcal C}$ of the linearly independent set $\mathcal{B}$. They are linearly independent: if $c_1[\mathbf{b}_1]_{\mathcal C} + \cdots + c_n[\mathbf{b}_n]_{\mathcal C} = \mathbf{0}$, then $[c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n]_{\mathcal C} = \mathbf{0}$, so $c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n = \mathbf{0}$ and all $c_i = 0$ ([[§26 Coordinate Systems#^cor-26-4|Corollary §26.4]], Lay's Exercise 25 in Section 4.4). A square matrix with linearly independent columns is invertible, by the Invertible Matrix Theorem ([[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1]]). Left-multiplying both sides of (4) by $(P_{\mathcal C \leftarrow \mathcal B})^{-1}$ gives
>
> $$
> (P_{\mathcal C \leftarrow \mathcal B})^{-1} [\mathbf{x}]_{\mathcal C} = [\mathbf{x}]_{\mathcal B} \qquad \text{for all } \mathbf{x} \in V .
> $$
>
> So $(P_{\mathcal C \leftarrow \mathcal B})^{-1}$ converts $\mathcal{C}$-coordinates into $\mathcal{B}$-coordinates. By the uniqueness in Theorem §29.1 (with $\mathcal{B}$ and $\mathcal{C}$ interchanged), it is $P_{\mathcal B \leftarrow \mathcal C}$. (Lay reads (6) off the displayed equation; the uniqueness statement is what makes it exact.)

^pf-29-2

*Uses:* [[§29 Change of Basis#^thm-29-1|§29.1]], [[§26 Coordinate Systems#^thm-26-3|§26.3]], [[§26 Coordinate Systems#^cor-26-4|§26.4]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]] (Invertible Matrix Theorem)

## Change of Basis in ℝⁿ

> [!theorem] Proposition §29.3: Change of Basis Through the Standard Basis
> Let $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$, $\mathcal{C} = \{\mathbf{c}_1, \ldots, \mathbf{c}_n\}$ and $\mathcal{D}$ be bases of $\mathbb{R}^n$ (or, in (c), of any vector space $V$), let $\mathcal{E} = \{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ be the standard basis, and let $P_{\mathcal B} = [\mathbf{b}_1\ \cdots\ \mathbf{b}_n]$ and $P_{\mathcal C} = [\mathbf{c}_1\ \cdots\ \mathbf{c}_n]$ be the change-of-coordinates matrices of [[§26 Coordinate Systems#^def-26-2|Definition §26.2]].
>
> (a) $P_{\mathcal E \leftarrow \mathcal B} = P_{\mathcal B}$.
>
> (b) $P_{\mathcal C \leftarrow \mathcal B} = P_{\mathcal C}^{-1} P_{\mathcal B}$.
>
> (c) $P_{\mathcal D \leftarrow \mathcal C}\, P_{\mathcal C \leftarrow \mathcal B} = P_{\mathcal D \leftarrow \mathcal B}$.
>
> *Lay: 4.7 (text); Exercise 20*
> *Source: 235 lecture L17*

^prop-29-3

> [!proof]+ Proof
> (a) For a vector $\mathbf{b}$ of $\mathbb{R}^n$, $\mathbf{b} = b_1\mathbf{e}_1 + \cdots + b_n\mathbf{e}_n$, so $[\mathbf{b}]_{\mathcal E} = \mathbf{b}$. By (5), the columns of $P_{\mathcal E \leftarrow \mathcal B}$ are $[\mathbf{b}_i]_{\mathcal E} = \mathbf{b}_i$.
>
> (c) For every $\mathbf{x}$, $[\mathbf{x}]_{\mathcal D} = P_{\mathcal D \leftarrow \mathcal C}[\mathbf{x}]_{\mathcal C} = P_{\mathcal D \leftarrow \mathcal C} P_{\mathcal C \leftarrow \mathcal B}[\mathbf{x}]_{\mathcal B}$. So the product satisfies (4) for the pair $\mathcal{B}$, $\mathcal{D}$, and by uniqueness in Theorem §29.1 it equals $P_{\mathcal D \leftarrow \mathcal B}$.
>
> (b) By (c) with $\mathcal{E}$ in the middle, (a) and Theorem §29.2:
>
> $$
> P_{\mathcal C \leftarrow \mathcal B} = P_{\mathcal C \leftarrow \mathcal E}\, P_{\mathcal E \leftarrow \mathcal B} = (P_{\mathcal E \leftarrow \mathcal C})^{-1} P_{\mathcal E \leftarrow \mathcal B} = P_{\mathcal C}^{-1} P_{\mathcal B} .
> $$
>
> Lay's version of the computation: $P_{\mathcal B}[\mathbf{x}]_{\mathcal B} = \mathbf{x}$, $P_{\mathcal C}[\mathbf{x}]_{\mathcal C} = \mathbf{x}$, so $[\mathbf{x}]_{\mathcal C} = P_{\mathcal C}^{-1}\mathbf{x} = P_{\mathcal C}^{-1}P_{\mathcal B}[\mathbf{x}]_{\mathcal B}$. The lecture writes the same thing as $P_{\mathcal C \leftarrow \mathcal B} = (P_{\mathcal S \leftarrow \mathcal C})^{-1} P_{\mathcal S \leftarrow \mathcal B}$ with $\mathcal{S}$ the standard basis.

^pf-29-3

*Uses:* [[§29 Change of Basis#^thm-29-1|§29.1]], [[§29 Change of Basis#^thm-29-2|§29.2]]

To change between two nonstandard bases of $\mathbb{R}^n$ we need the coordinates of the old basis vectors relative to the new basis. Finding $[\mathbf{b}_j]_{\mathcal C}$ means solving $[\mathbf{c}_1\ \cdots\ \mathbf{c}_n]\,\mathbf{y} = \mathbf{b}_j$, and all $n$ systems have the same coefficient matrix, so they can be solved at once.

> [!remark] Remark: Method — Computing the Change-of-Coordinates Matrix in ℝⁿ
> 1. Form the $n \times 2n$ matrix with the **new** basis on the left and the **old** basis on the right: $[\mathbf{c}_1\ \cdots\ \mathbf{c}_n \mid \mathbf{b}_1\ \cdots\ \mathbf{b}_n]$.
> 2. Row reduce until the left block is $I$:
>
> $$
> [\mathbf{c}_1\ \cdots\ \mathbf{c}_n \mid \mathbf{b}_1\ \cdots\ \mathbf{b}_n] \sim [\, I \mid P_{\mathcal C \leftarrow \mathcal B} \,] .
> $$
>
> 3. The right block is $P_{\mathcal C \leftarrow \mathcal B}$: its $j$th column solves $[\mathbf{c}_1\ \cdots\ \mathbf{c}_n]\,\mathbf{y} = \mathbf{b}_j$, so it is $[\mathbf{b}_j]_{\mathcal C}$. (The row operations multiply by $P_{\mathcal C}^{-1}$, in accordance with Proposition §29.3(b).)
> 4. For the other direction either invert ($P_{\mathcal B \leftarrow \mathcal C} = (P_{\mathcal C \leftarrow \mathcal B})^{-1}$) or reduce $[\mathbf{b}_1\ \cdots\ \mathbf{b}_n \mid \mathbf{c}_1\ \cdots\ \mathbf{c}_n] \sim [\, I \mid P_{\mathcal B \leftarrow \mathcal C} \,]$. The special case $[\mathbf{b}_1\ \cdots\ \mathbf{b}_n \mid I] \sim [\, I \mid P_{\mathcal B \leftarrow \mathcal E} \,]$ is the computation of $P_{\mathcal B}^{-1}$.
>
> Variant (lecture L17): reducing $[\mathbf{b}_1\ \cdots\ \mathbf{b}_n \mid \mathbf{c}_1\ \cdots\ \mathbf{c}_n]$ until the *right* block is $I$ leaves $P_{\mathcal C}^{-1}P_{\mathcal B} = P_{\mathcal C \leftarrow \mathcal B}$ on the left. For matrices larger than $2 \times 2$, one row reduction is faster than computing $P_{\mathcal C}^{-1}$ and then $P_{\mathcal C}^{-1}P_{\mathcal B}$.

^rem-29-1

> [!example] Example §29.2: The Change-of-Coordinates Matrix by Row Reduction
> Let $\mathbf{b}_1 = \begin{bmatrix} -9 \\ 1 \end{bmatrix}$, $\mathbf{b}_2 = \begin{bmatrix} -5 \\ -1 \end{bmatrix}$, $\mathbf{c}_1 = \begin{bmatrix} 1 \\ -4 \end{bmatrix}$, $\mathbf{c}_2 = \begin{bmatrix} 3 \\ -5 \end{bmatrix}$, and $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$, $\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2\}$. Find $P_{\mathcal C \leftarrow \mathcal B}$.
>
> Write $[\mathbf{b}_1]_{\mathcal C} = (x_1, x_2)$ and $[\mathbf{b}_2]_{\mathcal C} = (y_1, y_2)$. By definition, $[\mathbf{c}_1\ \mathbf{c}_2]\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \mathbf{b}_1$ and $[\mathbf{c}_1\ \mathbf{c}_2]\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \mathbf{b}_2$. Solve both at once. Add $4 \cdot$(row 1) to row 2, divide row 2 by $7$, then subtract $3 \cdot$(row 2) from row 1:
>
> $$
> \left[\begin{array}{rr|rr} 1 & 3 & -9 & -5 \\ -4 & -5 & 1 & -1 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 1 & 3 & -9 & -5 \\ 0 & 7 & -35 & -21 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 1 & 3 & -9 & -5 \\ 0 & 1 & -5 & -3 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 1 & 0 & 6 & 4 \\ 0 & 1 & -5 & -3 \end{array}\right] .
> $$
>
> So $[\mathbf{b}_1]_{\mathcal C} = \begin{bmatrix} 6 \\ -5 \end{bmatrix}$, $[\mathbf{b}_2]_{\mathcal C} = \begin{bmatrix} 4 \\ -3 \end{bmatrix}$, and
>
> $$
> P_{\mathcal C \leftarrow \mathcal B} = \big[\, [\mathbf{b}_1]_{\mathcal C}\ \ [\mathbf{b}_2]_{\mathcal C} \,\big] = \begin{bmatrix} 6 & 4 \\ -5 & -3 \end{bmatrix} .
> $$
>
> Check: $6\mathbf{c}_1 - 5\mathbf{c}_2 = (6 - 15,\ -24 + 25) = (-9, 1) = \mathbf{b}_1$ and $4\mathbf{c}_1 - 3\mathbf{c}_2 = (4 - 9,\ -16 + 15) = (-5, -1) = \mathbf{b}_2$.
>
> *Lay: Example 4.7.2*

^ex-29-2

> [!example] Example §29.3: Both Directions, with the Inverse
> Let $\mathbf{b}_1 = \begin{bmatrix} 1 \\ -3 \end{bmatrix}$, $\mathbf{b}_2 = \begin{bmatrix} -2 \\ 4 \end{bmatrix}$, $\mathbf{c}_1 = \begin{bmatrix} -7 \\ 9 \end{bmatrix}$, $\mathbf{c}_2 = \begin{bmatrix} -5 \\ 7 \end{bmatrix}$. Find (a) the change-of-coordinates matrix from $\mathcal{C}$ to $\mathcal{B}$, (b) the one from $\mathcal{B}$ to $\mathcal{C}$.
>
> **(a)** Now $P_{\mathcal B \leftarrow \mathcal C}$ is wanted, so $\mathcal{B}$ goes on the left. Add $3 \cdot$(row 1) to row 2, divide row 2 by $-2$, then add $2 \cdot$(row 2) to row 1:
>
> $$
> \left[\begin{array}{rr|rr} 1 & -2 & -7 & -5 \\ -3 & 4 & 9 & 7 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 1 & -2 & -7 & -5 \\ 0 & -2 & -12 & -8 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 1 & 0 & 5 & 3 \\ 0 & 1 & 6 & 4 \end{array}\right],
> \qquad P_{\mathcal B \leftarrow \mathcal C} = \begin{bmatrix} 5 & 3 \\ 6 & 4 \end{bmatrix} .
> $$
>
> **(b)** By Theorem §29.2 with $\mathcal{B}$ and $\mathcal{C}$ interchanged, and the $2 \times 2$ inverse formula ($\det = 20 - 18 = 2$):
>
> $$
> P_{\mathcal C \leftarrow \mathcal B} = (P_{\mathcal B \leftarrow \mathcal C})^{-1} = \frac12 \begin{bmatrix} 4 & -3 \\ -6 & 5 \end{bmatrix} = \begin{bmatrix} 2 & -3/2 \\ -3 & 5/2 \end{bmatrix} .
> $$
>
> Check: $2\mathbf{c}_1 - 3\mathbf{c}_2 = (-14 + 15,\ 18 - 21) = (1, -3) = \mathbf{b}_1$.
>
> *Lay: Example 4.7.3*

^ex-29-3

> [!example] Example §29.4: The Lecture's Example, Reducing the Other Block
> Let $\mathbf{b}_1 = \begin{bmatrix} 7 \\ 5 \end{bmatrix}$, $\mathbf{b}_2 = \begin{bmatrix} -3 \\ -1 \end{bmatrix}$, $\mathbf{c}_1 = \begin{bmatrix} 1 \\ -5 \end{bmatrix}$, $\mathbf{c}_2 = \begin{bmatrix} -2 \\ 2 \end{bmatrix}$. Find $P_{\mathcal C \leftarrow \mathcal B}$ and $P_{\mathcal B \leftarrow \mathcal C}$.
>
> The lecture reduces $[\mathbf{b}_1\ \mathbf{b}_2 \mid \mathbf{c}_1\ \mathbf{c}_2]$ until the right block is $I$ (the variant at the end of [[§29 Change of Basis#^rem-29-1|the method remark]]). Add $5 \cdot$(row 1) to row 2, divide row 2 by $-8$, then add $2 \cdot$(row 2) to row 1:
>
> $$
> \left[\begin{array}{rr|rr} 7 & -3 & 1 & -2 \\ 5 & -1 & -5 & 2 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 7 & -3 & 1 & -2 \\ 40 & -16 & 0 & -8 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} 7 & -3 & 1 & -2 \\ -5 & 2 & 0 & 1 \end{array}\right]
> \sim \left[\begin{array}{rr|rr} -3 & 1 & 1 & 0 \\ -5 & 2 & 0 & 1 \end{array}\right] .
> $$
>
> So
>
> $$
> P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} -3 & 1 \\ -5 & 2 \end{bmatrix} .
> $$
>
> Check, as Lay's method would read it: $-3\mathbf{c}_1 - 5\mathbf{c}_2 = (-3 + 10,\ 15 - 10) = (7, 5) = \mathbf{b}_1$ and $\mathbf{c}_1 + 2\mathbf{c}_2 = (1 - 4,\ -5 + 4) = (-3, -1) = \mathbf{b}_2$. The inverse ($\det = -6 + 5 = -1$) is
>
> $$
> P_{\mathcal B \leftarrow \mathcal C} = -\begin{bmatrix} 2 & -1 \\ 5 & -3 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ -5 & 3 \end{bmatrix},
> $$
>
> and indeed $-2\mathbf{b}_1 - 5\mathbf{b}_2 = (-14 + 15,\ -10 + 5) = (1, -5) = \mathbf{c}_1$.
>
> *Lay: 4.7, Exercise 7*
> *Source: 235 lecture L17*

^ex-29-4
