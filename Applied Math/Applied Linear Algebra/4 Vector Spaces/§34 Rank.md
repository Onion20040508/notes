---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 34
lay: "4.6"
aliases: ["Lay 4.6"]
tags: [applied-linear-algebra, math235]
---
← [[§33 The Dimension of a Vector Space]] · ↑ [[· 4 Vector Spaces]] · [[§35 Change of Basis]] →

*Lay, Section 4.6 · MATH 235 lectures L16, L17.*

This section looks inside a matrix. Besides $\operatorname{Col} A$ and $\operatorname{Nul} A$, an $m \times n$ matrix has a third subspace, the row space $\operatorname{Row} A \subseteq \mathbb{R}^n$, and one row reduction gives bases for all three. The main result is the Rank Theorem: the column space and the row space have the same dimension, the rank of $A$, and $\operatorname{rank} A + \dim \operatorname{Nul} A = n$. So in a $40 \times 50$ matrix of random numbers, the maximal number of linearly independent columns equals the maximal number of linearly independent rows. The Rank Theorem answers questions about solvability of linear systems by counting, and it adds six statements to the Invertible Matrix Theorem. (In the 6th edition this material belongs to Section 4.5; the instructor's checklist items "dimensions of Row A, Nul A and Col A and their relation" and "the Invertible Matrix Theorem and the dimensions" are covered here.)

## The Row Space

The **row space** $\operatorname{Row} A$ of an $m \times n$ matrix $A$, the set of all linear combinations of its rows (each identified with a vector in $\mathbb{R}^n$), is defined in [[§30 Null Spaces, Column Spaces, and Linear Transformations#^def-30-3|Definition §30.3]]: the 6th edition introduces it in 4.2, the 5th here in 4.6. It is a subspace of $\mathbb{R}^n$ (a span, [[§29 Vector Spaces and Subspaces#^thm-29-4|Theorem §29.4]]), and $\operatorname{Row} A = \operatorname{Col} A^T$. For example (Lay's Example 4.6.1, also in lecture L16), for

$$
A = \begin{bmatrix} -2 & -5 & 8 & 0 & -17 \\ 1 & 3 & -5 & 1 & 5 \\ 3 & 11 & -19 & 7 & 1 \\ 1 & 7 & -13 & 5 & -3 \end{bmatrix},
\qquad
\begin{aligned}
\mathbf{r}_1 &= (-2, -5, 8, 0, -17) \\
\mathbf{r}_2 &= (1, 3, -5, 1, 5) \\
\mathbf{r}_3 &= (3, 11, -19, 7, 1) \\
\mathbf{r}_4 &= (1, 7, -13, 5, -3)
\end{aligned}
$$

$\operatorname{Row} A = \operatorname{Span}\{\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3, \mathbf{r}_4\}$, a subspace of $\mathbb{R}^5$. Row vectors are written horizontally, but may be written as columns when that is convenient.

Row operations change the linear dependence relations among the rows, so they do not tell us which rows of $A$ to keep. But they do preserve the row space itself.

> [!remark] Remark: Why It Works
> Lecture L16 shows the idea with two rows. Replacing row 2 by row 2 minus $3$ times row 1 turns $A$ with rows $\mathbf{r}_1, \mathbf{r}_2$ into $B$ with rows $\mathbf{r}_1, \mathbf{r}_2 - 3\mathbf{r}_1$. A typical element of $\operatorname{Row} B$ is
>
> $$
> c\,\mathbf{r}_1 + d\,(\mathbf{r}_2 - 3\mathbf{r}_1) = (c - 3d)\,\mathbf{r}_1 + d\,\mathbf{r}_2 ,
> $$
>
> and as $(c, d)$ runs through all pairs, so does $(c - 3d, d)$. So $\operatorname{Row} B = \operatorname{Row} A$.

^rem-34-1

> [!theorem] Theorem §34.1: Row Operations Preserve the Row Space
> If two matrices $A$ and $B$ are row equivalent, then their row spaces are the same. If $B$ is in echelon form, the nonzero rows of $B$ form a basis for the row space of $A$ as well as for that of $B$.
>
> *Lay: Theorem 13 (4.6)*

^thm-34-1

> [!proof]+ Proof
> If $B$ is obtained from $A$ by row operations, the rows of $B$ are linear combinations of the rows of $A$. So any linear combination of the rows of $B$ is a linear combination of the rows of $A$, and $\operatorname{Row} B \subseteq \operatorname{Row} A$. Row operations are reversible, so the same argument gives $\operatorname{Row} A \subseteq \operatorname{Row} B$. Hence the row spaces are equal.
>
> If $B$ is in echelon form, its nonzero rows span $\operatorname{Row} B$ (zero rows contribute nothing). They are linearly independent, because no nonzero row is a linear combination of the nonzero rows below it: each row below has zeros in the column of the leading entry of the given row, and in all columns to its left. List the nonzero rows in reverse order, the last one first. Then no row is a linear combination of the rows preceding it in the list, and the set is independent by [[§31 Linearly Independent Sets; Bases#^thm-31-1|Theorem §31.1]]. So the nonzero rows of $B$ form a basis of the common row space of $B$ and $A$.

^pf-34-1

*Uses:* [[§31 Linearly Independent Sets; Bases#^thm-31-1|§31.1]], [[§1 Systems of Linear Equations#^prop-1-1|§1.1]] (row operations are reversible)

The lecture also proved the converse, which Lay does not state.

> [!theorem] Proposition §34.2: Equal Row Spaces Means Row Equivalent
> Two $m \times n$ matrices $A$ and $B$ are row equivalent if and only if $\operatorname{Row} A = \operatorname{Row} B$.
>
> *Source: 235 lecture L16*

^prop-34-2

> [!proof]+ Proof
> "Only if" is [[§34 Rank#^thm-34-1|Theorem §34.1]]. For "if", the lecture's reason is that the reduced echelon form is unique: $A$ and $B$ are row equivalent exactly when they have the same reduced echelon form ([[§2 Row Reduction and Echelon Forms#^thm-2-1|Theorem §2.1]]). It remains to see that the reduced echelon form is determined by the row space; the lecture asserts this, and here is why.
>
> Let $R$ and $S$ be the reduced echelon forms of $A$ and $B$. By [[§34 Rank#^thm-34-1|Theorem §34.1]], $\operatorname{Row} R = \operatorname{Row} A = \operatorname{Row} B = \operatorname{Row} S$; call this subspace $W$. Let $\mathbf{r}_1, \ldots, \mathbf{r}_k$ be the nonzero rows of $R$, with leading $1$s in columns $p_1 < \cdots < p_k$. Column $p_i$ of $R$ has a $1$ in row $i$ and $0$ elsewhere.
>
> *The pivot columns are determined by $W$.* Let $\mathbf{w} = c_1\mathbf{r}_1 + \cdots + c_k\mathbf{r}_k$ be a nonzero vector in $W$, and let $i$ be the smallest index with $c_i \ne 0$. The rows $\mathbf{r}_l$ with $l \ge i$ are zero in all columns left of $p_i$, and in column $p_i$ only $\mathbf{r}_i$ is nonzero. So the first nonzero entry of $\mathbf{w}$ is $c_i$, in column $p_i$. Hence $\{p_1, \ldots, p_k\}$ is exactly the set of positions where nonzero vectors of $W$ have their first nonzero entry. The same holds for $S$, so $S$ has the same pivot columns $p_1, \ldots, p_k$ (and the same number $k = \dim W$ of nonzero rows).
>
> *The rows are determined by $W$.* Let $\mathbf{s}_i$ be the $i$th row of $S$. It lies in $W$, so $\mathbf{s}_i = c_1\mathbf{r}_1 + \cdots + c_k\mathbf{r}_k$, and reading off column $p_l$ gives $c_l$ = (entry of $\mathbf{s}_i$ in column $p_l$). Since $S$ is in reduced echelon form with pivots $p_1, \ldots, p_k$, that entry is $1$ if $l = i$ and $0$ otherwise. So $\mathbf{s}_i = \mathbf{r}_i$.
>
> Thus $R$ and $S$ have the same nonzero rows, and both have $m - k$ zero rows below them: $R = S$. So $A \sim R = S \sim B$, and $A$ and $B$ are row equivalent.

^pf-34-2

*Uses:* [[§34 Rank#^thm-34-1|§34.1]], [[§2 Row Reduction and Echelon Forms#^thm-2-1|§2.1]] (uniqueness of the reduced echelon form), [[§1 Systems of Linear Equations#^prop-1-1|§1.1]] (row operations are reversible)

> [!example] Example §34.1: Bases for Row A, Col A and Nul A
> Find bases for the row space, the column space and the null space of the matrix $A$ displayed above (Lay's Example 4.6.1).
>
> **Echelon form.** Interchange rows 1 and 2. Then add $2 \cdot$(row 1) to row 2, $-3 \cdot$(row 1) to row 3 and $-1 \cdot$(row 1) to row 4:
>
> $$
> \begin{bmatrix} 1 & 3 & -5 & 1 & 5 \\ 0 & 1 & -2 & 2 & -7 \\ 0 & 2 & -4 & 4 & -14 \\ 0 & 4 & -8 & 4 & -8 \end{bmatrix} .
> $$
>
> Subtract $2 \cdot$(row 2) from row 3 (giving a zero row) and $4 \cdot$(row 2) from row 4 (giving $(0, 0, 0, -4, 20)$), and interchange the last two rows:
>
> $$
> A \sim B = \begin{bmatrix} 1 & 3 & -5 & 1 & 5 \\ 0 & 1 & -2 & 2 & -7 \\ 0 & 0 & 0 & -4 & 20 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> **Row A.** By [[§34 Rank#^thm-34-1|Theorem §34.1]], the nonzero rows of $B$ form a basis:
>
> $$
> \{(1, 3, -5, 1, 5),\ (0, 1, -2, 2, -7),\ (0, 0, 0, -4, 20)\} .
> $$
>
> **Col A.** The pivots of $B$ are in columns $1$, $2$ and $4$, so columns $1$, $2$, $4$ *of $A$* (not of $B$) form a basis for $\operatorname{Col} A$:
>
> $$
> \left\{ \begin{bmatrix} -2 \\ 1 \\ 3 \\ 1 \end{bmatrix}, \begin{bmatrix} -5 \\ 3 \\ 11 \\ 7 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 7 \\ 5 \end{bmatrix} \right\} .
> $$
>
> **Nul A.** Here the *reduced* echelon form is needed. Divide row 3 of $B$ by $-4$, then clear column 4 and column 2 above the pivots:
>
> $$
> A \sim B \sim C = \begin{bmatrix} 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 3 \\ 0 & 0 & 0 & 1 & -5 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> $A\mathbf{x} = \mathbf{0}$ is equivalent to $C\mathbf{x} = \mathbf{0}$: $x_1 = -x_3 - x_5$, $x_2 = 2x_3 - 3x_5$, $x_4 = 5x_5$, with $x_3$ and $x_5$ free. So
>
> $$
> \mathbf{x} = x_3 \begin{bmatrix} -1 \\ 2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_5 \begin{bmatrix} -1 \\ -3 \\ 0 \\ 5 \\ 1 \end{bmatrix},
> \qquad \text{basis for } \operatorname{Nul} A: \ \left\{ \begin{bmatrix} -1 \\ 2 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} -1 \\ -3 \\ 0 \\ 5 \\ 1 \end{bmatrix} \right\} .
> $$
>
> Unlike the basis for $\operatorname{Col} A$, the bases for $\operatorname{Row} A$ and $\operatorname{Nul} A$ have no simple connection with the entries of $A$ itself.
>
> **Warning.** The first three rows of $B$ are linearly independent, but the first three rows of $A$ are not: $\mathbf{r}_3 = 2\mathbf{r}_1 + 7\mathbf{r}_2$ (check: $2(-2, -5, 8, 0, -17) + 7(1, 3, -5, 1, 5) = (3, 11, -19, 7, 1)$). Row operations may change the linear dependence relations among the *rows* of a matrix.
>
> *Lay: Example 4.6.2*

^ex-34-1

> [!remark] Remark: Method — Bases for Row A, Col A and Nul A
> 1. Row reduce $A$ to an echelon form $B$.
> 2. **Row A:** the nonzero rows of $B$ ([[§34 Rank#^thm-34-1|Theorem §34.1]]).
> 3. **Col A:** the columns of $A$ in the pivot positions of $B$ — columns of $A$, not of $B$.
> 4. **Nul A:** continue to the reduced echelon form, solve $A\mathbf{x} = \mathbf{0}$ for the basic variables, and write the solution in parametric vector form; the vectors multiplying the free variables form a basis.
> 5. **A basis of Row A made of rows of A** (Lay's footnote; the lecture's route "$\operatorname{Row} A = \operatorname{Col} A^T$"): row reduce $A^T$ and take the pivot columns of $A^T$. These are rows of $A$.
>
> The counts come along for free: $\dim \operatorname{Row} A = \dim \operatorname{Col} A$ = number of pivots, and $\dim \operatorname{Nul} A$ = number of free variables.

^rem-34-2

## The Rank Theorem

> [!definition] Definition §34.1: Rank
> The **rank** of $A$ is the dimension of the column space of $A$:
>
> $$
> \operatorname{rank} A = \dim \operatorname{Col} A .
> $$
>
> Since $\operatorname{Row} A = \operatorname{Col} A^T$, $\dim \operatorname{Row} A = \operatorname{rank} A^T$. The dimension of the null space is sometimes called the **nullity** of $A$ (Lay does not use this term).
>
> *Lay: 4.6, Definition*

^def-34-1

> [!theorem] Theorem §34.3: The Rank Theorem
> The dimensions of the column space and the row space of an $m \times n$ matrix $A$ are equal. This common dimension, the rank of $A$, also equals the number of pivot positions in $A$ and satisfies the equation
>
> $$
> \operatorname{rank} A + \dim \operatorname{Nul} A = n .
> $$
>
> In particular $\operatorname{rank} A^T = \operatorname{rank} A$.
>
> *Lay: Theorem 14 (4.6)*

^thm-34-3

> [!proof]+ Proof
> By [[§31 Linearly Independent Sets; Bases#^thm-31-3|Theorem §31.3]], the pivot columns of $A$ form a basis of $\operatorname{Col} A$, so $\operatorname{rank} A$ is the number of pivot columns of $A$, that is, the number of pivot positions in an echelon form $B$ of $A$. Since $B$ has one nonzero row for each pivot, and these rows form a basis for $\operatorname{Row} A$ ([[§34 Rank#^thm-34-1|Theorem §34.1]]), the rank of $A$ is also $\dim \operatorname{Row} A$.
>
> By [[§33 The Dimension of a Vector Space#^thm-33-8|Theorem §33.8]], $\dim \operatorname{Nul} A$ is the number of free variables in $A\mathbf{x} = \mathbf{0}$, that is, the number of columns of $A$ that are *not* pivot columns. (It is the number of these columns, not the columns themselves, that is related to $\operatorname{Nul} A$.) Obviously
>
> $$
> \{\text{number of pivot columns}\} + \{\text{number of nonpivot columns}\} = \{\text{number of columns}\} = n ,
> $$
>
> which is $\operatorname{rank} A + \dim \operatorname{Nul} A = n$. Finally $\operatorname{rank} A^T = \dim \operatorname{Col} A^T = \dim \operatorname{Row} A = \operatorname{rank} A$.

^pf-34-3

*Uses:* [[§34 Rank#^thm-34-1|§34.1]], [[§33 The Dimension of a Vector Space#^thm-33-8|§33.8]], [[§31 Linearly Independent Sets; Bases#^thm-31-3|§31.3]]

> [!remark]- Connections
> - Rigorous treatment: $\operatorname{rank} A + \dim \operatorname{Nul} A = n$ is the [[§8 Null Spaces and Ranges#^ladr-3-21|fundamental theorem of linear maps (LADR 3.21)]], $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ for any linear map on a finite-dimensional $V$, proved by extending a basis of the null space instead of counting pivots. Column rank equals row rank: [[§9 Matrices#^ladr-3-57|LADR 3.57]] (via a column–row factorization, without row reduction) and [[§12 Duality#^ladr-3-133|LADR 3.133]] (via dual maps); rank [[§9 Matrices#^ladr-3-58|LADR 3.58]].
> - Lay states the second equation for subspaces of $\mathbb{R}^n$ already in Section 2.9 ([[§22 Dimension and Rank#^thm-22-2|Theorem §22.2]]). Geometric form: $\operatorname{Row} A$ and $\operatorname{Nul} A$ are orthogonal complements in $\mathbb{R}^n$, [[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]].

> [!remark] Remark: The Geometry of the Rank Theorem
> Think of $A$ as the map $\mathbf{x} \mapsto A\mathbf{x}$ from $\mathbb{R}^n$ to $\mathbb{R}^m$. It collapses the $(\dim \operatorname{Nul} A)$-dimensional subspace $\operatorname{Nul} A$ to $\mathbf{0}$, and its image $\operatorname{Col} A$ has dimension $\operatorname{rank} A$: the $n$ dimensions of the domain are split between those that are killed and those that survive. Lecture L16's example is the projection $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} : \mathbb{R}^3 \to \mathbb{R}^2$. Here $\operatorname{Nul} A$ is the $z$-axis ($\dim 1$) and $\operatorname{Col} A = \mathbb{R}^2$ ($\dim 2$), and $1 + 2 = 3$. Every $\mathbf{x} = (x, y, z)$ splits as $(x, y, 0) + (0, 0, z)$: the first part lies in $\operatorname{Row} A$ (the $xy$-plane of $\mathbb{R}^3$) and is carried one-to-one onto $\operatorname{Col} A$, the second lies in $\operatorname{Nul} A$ and is sent to $\mathbf{0}$.
>
> *The lecture writes this splitting as $\mathbb{R}^3 = \operatorname{Nul}(A) \oplus \operatorname{Col}(A)$, with $\mathbf{x} = A\mathbf{x} + \mathbf{x}'$. But $\operatorname{Col} A = \mathbb{R}^2$ is not a subspace of $\mathbb{R}^3$; the statement holds only after $A\mathbf{x} = (x, y)$ is identified with $(x, y, 0)$. Written correctly, it is $\mathbb{R}^3 = \operatorname{Nul} A \oplus \operatorname{Row} A$, as above: every $\mathbf{x}$ is in exactly one way a vector of $\operatorname{Row} A$ plus a vector of $\operatorname{Nul} A$. The same holds for every $m \times n$ matrix, $\mathbb{R}^n = \operatorname{Nul} A \oplus \operatorname{Row} A$ (orthogonal complements, [[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]]). See also [[§22 Dimension and Rank#^rem-22-2|Remark: The Rank Theorem Geometrically]].*
>
> *Source: 235 lecture L16*

^rem-34-3

> [!theorem] Corollary §34.4: Rank Is at Most the Smaller Size
> For an $m \times n$ matrix $A$,
>
> $$
> \operatorname{rank} A \le \min(m, n), \qquad \dim \operatorname{Nul} A = n - \operatorname{rank} A \ge n - m .
> $$
>
> *Source: 235 lecture L17*

^cor-34-4

> [!proof]+ Proof
> By the Rank Theorem, $\operatorname{rank} A$ is the number of pivot positions. Each pivot occupies its own row and its own column, so there are at most $m$ and at most $n$ of them. The second statement is the Rank Theorem with $\operatorname{rank} A \le m$.

^pf-34-4

*Uses:* [[§34 Rank#^thm-34-3|§34.3]]

> [!example] Example §34.2: Counting with the Rank Theorem
> **(a)** If $A$ is a $7 \times 9$ matrix with a two-dimensional null space, what is the rank of $A$? Since $A$ has $9$ columns, $\operatorname{rank} A + 2 = 9$, so $\operatorname{rank} A = 7$.
>
> **(b)** Could a $6 \times 9$ matrix $A$, that is, a linear map $A : \mathbb{R}^9 \to \mathbb{R}^6$, have a two-dimensional null space? No. By the Rank Theorem $\dim \operatorname{Nul} A = 9 - \operatorname{rank} A$, and the columns of $A$ are vectors in $\mathbb{R}^6$, so $\operatorname{rank} A = \dim \operatorname{Col} A \le 6$ ([[§34 Rank#^cor-34-4|Corollary §34.4]]). Hence
>
> $$
> \dim \operatorname{Nul} A = 9 - \operatorname{rank} A \ge 9 - 6 = 3 > 2 .
> $$
>
> The lecture lists the cases: rank $6, 5, 4, \ldots$ give $\dim \operatorname{Nul} A = 3, 4, 5, \ldots$, never $2$. (A null space of dimension $2$ would force rank $7$.)
>
> *The lecture's third line reads $9 - 3 = 5$; for rank $4$ it should be $9 - 4 = 5$.*
>
> *Lay: Example 4.6.3*
> *Source: 235 lecture L17*

^ex-34-2

> [!example] Example §34.3: The Four Subspaces of a 3 × 3 Matrix
> Let
>
> $$
> A = \begin{bmatrix} 3 & 0 & -1 \\ 3 & 0 & -1 \\ 4 & 0 & 5 \end{bmatrix} .
> $$
>
> **Nul A.** $A\mathbf{x} = (3x_1 - x_3,\ 3x_1 - x_3,\ 4x_1 + 5x_3)$. This is $\mathbf{0}$ exactly when $3x_1 - x_3 = 0$ and $4x_1 + 5x_3 = 0$; the first gives $x_3 = 3x_1$, then the second gives $19x_1 = 0$, so $x_1 = x_3 = 0$ and $x_2$ is arbitrary. So $\operatorname{Nul} A$ is the $x_2$-axis, $\dim \operatorname{Nul} A = 1$.
>
> **Row A.** The rows $(3, 0, -1)$ and $(4, 0, 5)$ are independent and have middle entry $0$, so $\operatorname{Row} A$ is the $x_1x_3$-plane, of dimension $2$.
>
> **Col A.** The first two coordinates of $A\mathbf{x}$ are always equal, and columns $1$ and $3$, $(3, 3, 4)$ and $(-1, -1, 5)$, are independent. So $\operatorname{Col} A$ is the plane $x_1 - x_2 = 0$, of dimension $2$.
>
> **Nul A^T.** $A^T\mathbf{y} = (3y_1 + 3y_2 + 4y_3,\ 0,\ -y_1 - y_2 + 5y_3)$. Adding $3$ times the third entry to the first gives $19y_3 = 0$, so $y_3 = 0$ and $y_1 + y_2 = 0$: $\operatorname{Nul} A^T$ is the set of multiples of $(1, -1, 0)$.
>
> **Checks.** $\operatorname{rank} A + \dim \operatorname{Nul} A = 2 + 1 = 3 = n$ and $\operatorname{rank} A^T + \dim \operatorname{Nul} A^T = 2 + 1 = 3 = m$. In each copy of $\mathbb{R}^3$ the line is perpendicular to the plane, as Chapter 6 explains ([[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]]).
>
> *Lay: Example 4.6.4*
> *Source: 235 lecture L16*

^ex-34-3

![[m235-28-1.svg]]
*[[§34 Rank#^ex-34-3|Example §34.3]]. Left, the domain $\mathbb{R}^3$: $\operatorname{Row} A$ is the $x_1x_3$-plane (blue) and $\operatorname{Nul} A$ is the $x_2$-axis (red), perpendicular to it. Right, the codomain $\mathbb{R}^3$: $\operatorname{Col} A$, the range of $\mathbf{x} \mapsto A\mathbf{x}$, is the plane $x_1 = x_2$ (blue), and $\operatorname{Nul} A^T$ is the line through $(1, -1, 0)$ (red). The map squeezes the red line on the left to $\mathbf{0}$ and carries the blue plane on the left one-to-one onto the blue plane on the right.*

> [!remark] Remark: Images of a Basis
> If $\mathbf{b}_1, \ldots, \mathbf{b}_n$ is a basis of $\mathbb{R}^n$ and $A$ is $m \times n$, then the largest number of linearly independent vectors among $A\mathbf{b}_1, \ldots, A\mathbf{b}_n$ is $\operatorname{rank} A$. Indeed, every $\mathbf{x} \in \mathbb{R}^n$ is $c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$, so $A\mathbf{x} = c_1 A\mathbf{b}_1 + \cdots + c_n A\mathbf{b}_n$ and the vectors $A\mathbf{b}_i$ span $\operatorname{Col} A$. By the Spanning Set Theorem a subset of them is a basis of $\operatorname{Col} A$, with $\operatorname{rank} A$ elements; and by [[§33 The Dimension of a Vector Space#^thm-33-1|Theorem §33.1]] no more than $\operatorname{rank} A$ of them can be independent. (In the lecture's picture: a map $\mathbb{R}^3 \to \mathbb{R}^2$ of rank $2$ sends a basis to three vectors in a plane, two of them independent.)
>
> *Source: 235 lecture L17*

^rem-34-4

## Applications to Systems of Equations

> [!example] Example §34.4: A Homogeneous System with Two Basic Solutions
> A scientist has found two solutions to a homogeneous system of $40$ equations in $42$ variables. The two solutions are not multiples of each other, and all other solutions can be constructed by adding together appropriate multiples of these two. Can the scientist be *certain* that an associated nonhomogeneous system (with the same coefficients) has a solution?
>
> Yes. Let $A$ be the $40 \times 42$ coefficient matrix. The two solutions are linearly independent and span $\operatorname{Nul} A$, so $\dim \operatorname{Nul} A = 2$. By the Rank Theorem, $\dim \operatorname{Col} A = 42 - 2 = 40$. $\operatorname{Col} A$ is a $40$-dimensional subspace of $\mathbb{R}^{40}$, so $\operatorname{Col} A = \mathbb{R}^{40}$ ([[§33 The Dimension of a Vector Space#^cor-33-6|Corollary §33.6]]). Hence every equation $A\mathbf{x} = \mathbf{b}$ has a solution.
>
> *Lay: Example 4.6.5*

^ex-34-4

## Rank and the Invertible Matrix Theorem

The vector space ideas give six more statements for the Invertible Matrix Theorem, continuing the list (a)–(l) of Section 2.3 ([[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]]). Lay already adds the same six statements in Section 2.9 for subspaces of $\mathbb{R}^n$; their home in these notes is [[§22 Dimension and Rank#^thm-22-3|Theorem §22.3]]. Lay 5e repeats them here, in Section 4.6, with the general dimension theory behind them, and the theorem below restates them in that form.

> [!theorem] Theorem §34.5: The Invertible Matrix Theorem (Continued)
> Let $A$ be an $n \times n$ matrix. Then the following statements are each equivalent to the statement that $A$ is an invertible matrix.
>
> - (m) The columns of $A$ form a basis of $\mathbb{R}^n$.
> - (n) $\operatorname{Col} A = \mathbb{R}^n$.
> - (o) $\dim \operatorname{Col} A = n$.
> - (p) $\operatorname{rank} A = n$.
> - (q) $\operatorname{Nul} A = \{\mathbf{0}\}$.
> - (r) $\dim \operatorname{Nul} A = 0$.
>
> Since $A$ is invertible if and only if $A^T$ is (statement (l)), each statement may also be made for $A^T$, for instance $\operatorname{Row} A = \mathbb{R}^n$; Lay leaves these out to keep the list under thirty statements.
>
> These are statements (m)–(r) of [[§22 Dimension and Rank#^thm-22-3|Theorem §22.3]], restated. Previous version: [[§25 Properties of Determinants#^thm-25-4|Theorem §25.4]] ($\det A \ne 0$); next: [[§41 The Characteristic Equation#^thm-41-2|Theorem §41.2]] (statements (s), (t)).
>
> *Lay: 4.6, Theorem (The Invertible Matrix Theorem, continued)*

^thm-34-5

> [!proof]+ Proof
> Statement (m) is logically equivalent to statements (e) and (h) of [[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]] together: the columns of $A$ are linearly independent and span $\mathbb{R}^n$. The other five are linked to the earlier statements by the chain
>
> $$
> \text{(g)} \Rightarrow \text{(n)} \Rightarrow \text{(o)} \Rightarrow \text{(p)} \Rightarrow \text{(r)} \Rightarrow \text{(q)} \Rightarrow \text{(d)} .
> $$
>
> - (g) $\Rightarrow$ (n): (g) says $A\mathbf{x} = \mathbf{b}$ has at least one solution for each $\mathbf{b} \in \mathbb{R}^n$, and $\operatorname{Col} A$ is precisely the set of all $\mathbf{b}$ for which $A\mathbf{x} = \mathbf{b}$ is consistent.
> - (n) $\Rightarrow$ (o) $\Rightarrow$ (p): the definitions of dimension and rank ($\dim \mathbb{R}^n = n$).
> - (p) $\Rightarrow$ (r): if $\operatorname{rank} A = n$, the number of columns, then $\dim \operatorname{Nul} A = 0$ by the Rank Theorem.
> - (r) $\Rightarrow$ (q): the only $0$-dimensional subspace is $\{\mathbf{0}\}$.
> - (q) $\Rightarrow$ (d): (q) says that $A\mathbf{x} = \mathbf{0}$ has only the trivial solution, which is (d).
>
> Since (d) and (g) are already known to be equivalent to the invertibility of $A$, all six statements are.
>
> Lecture L16 closes the loop directly instead: if $\operatorname{Nul} A = \{\mathbf{0}\}$, then $\dim \operatorname{Nul} A = 0$, so $\dim \operatorname{Col} A = n$ by the Rank Theorem; then $\operatorname{Col} A = \mathbb{R}^n$ ([[§33 The Dimension of a Vector Space#^cor-33-6|Corollary §33.6]]), and the $n$ columns, spanning the $n$-dimensional $\mathbb{R}^n$, form a basis by the Basis Theorem. So (q) $\Rightarrow$ (m).

^pf-34-5

*Uses:* [[§16 Characterizations of Invertible Matrices#^thm-16-1|§16.1]] (statements (d), (e), (g), (h)), [[§34 Rank#^thm-34-3|§34.3]], [[§33 The Dimension of a Vector Space#^cor-33-6|§33.6]], [[§33 The Dimension of a Vector Space#^thm-33-5|§33.5]]

> [!remark]- Connections
> - Rigorous treatment: for an operator on a finite-dimensional space, injective ⟺ surjective ⟺ invertible, [[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]], a consequence of the fundamental theorem of linear maps. Later extensions of the theorem here: determinants and eigenvalues in Section 5.2 ([[§41 The Characteristic Equation#^thm-41-2|Theorem §41.2]]), orthogonal complements and singular values in [[§62★ The Singular Value Decomposition in Applications#^thm-62-2|Theorem §62.2]].

> [!remark]- Remark: Numerical Note — Computing the Rank
> Rank determination looks easy: reduce to echelon form and count the pivots. But unless the arithmetic is exact, row operations can change the *apparent* rank. In $\begin{bmatrix} 5 & 7 \\ 5 & x \end{bmatrix}$, if $x$ is not stored exactly as $7$, the computed rank may be $1$ or $2$, depending on whether the computer treats $x - 7$ as zero. In practice the effective rank is found from the singular value decomposition (Section 7.4), which also gives reliable bases for $\operatorname{Col} A$, $\operatorname{Row} A$, $\operatorname{Nul} A$ and $\operatorname{Nul} A^T$: [[§62★ The Singular Value Decomposition in Applications#^thm-62-1|Theorem §62.1]].

^rem-34-5
