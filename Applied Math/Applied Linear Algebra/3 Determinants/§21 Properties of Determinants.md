---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: 21
lay: "3.2"
aliases: ["Lay 3.2"]
tags: [applied-linear-algebra, math235]
---
← [[§20 Introduction to Determinants]] · ↑ [[· 3 Determinants]] · [[§22 Cramer’s Rule, Volume, and Linear Transformations]] →

*Lay, Section 3.2 · MATH 235 lectures L11, L12.*

"The secret of determinants lies in how they change when row operations are performed" (Lay). A row replacement leaves the determinant unchanged, an interchange changes its sign, and scaling a row scales it. So row reducing to an echelon form computes $\det A$ in about $n^3$ steps instead of $n!$, and the same computation proves the central fact: $A$ is invertible if and only if $\det A \ne 0$, a new statement in the Invertible Matrix Theorem. The section also shows that $\det A^T = \det A$ (so columns behave like rows), that $\det AB = (\det A)(\det B)$, and that $\det A$ is a linear function of each column separately.

## Row Operations

[[§12 The Inverse of a Matrix|§12]] (2.2) showed that each elementary row operation on an $n \times n$ matrix $A$ is left multiplication by an elementary matrix $E$, obtained by performing the same operation on $I_n$.

> [!definition] Definition §21.1: Replacement, Interchange and Scaling Matrices
> An elementary matrix $E$ is
> - a **row replacement (matrix)** if $E$ is obtained from $I$ by adding a multiple of one row to another row;
> - an **interchange** if $E$ is obtained by interchanging two rows of $I$;
> - a **scale by $r$** if $E$ is obtained by multiplying a row of $I$ by a nonzero scalar $r$.
>
> *Lay: 3.2 (text, Proofs of Theorems 3 and 6)*

^def-21-1

> [!theorem] Theorem §21.1: Row Operations
> Let $A$ be a square matrix.
>
> a. If a multiple of one row of $A$ is added to another row to produce a matrix $B$, then $\det B = \det A$.
>
> b. If two rows of $A$ are interchanged to produce $B$, then $\det B = -\det A$.
>
> c. If one row of $A$ is multiplied by $k$ to produce $B$, then $\det B = k \cdot \det A$.
>
> Equivalently, in terms of Definition §21.1: if $A$ is $n \times n$ and $E$ is an $n \times n$ elementary matrix, then
>
> $$
> \det EA = (\det E)(\det A), \qquad \text{where} \quad \det E = \begin{cases} 1 & \text{if } E \text{ is a row replacement,} \\ -1 & \text{if } E \text{ is an interchange,} \\ r & \text{if } E \text{ is a scale by } r . \end{cases}
> $$
>
> *Lay: Theorem 3 (3.2)*

^thm-21-1

> [!remark] Remark: Why It Works
> For $n = 2$, $|\det|$ is the area of the parallelogram spanned by the rows ([[§22 Cramer’s Rule, Volume, and Linear Transformations|§22]], Theorem 9 of 3.3). Replacing a row $\mathbf{u}$ by $\mathbf{u} + k\mathbf{v}$ slides one side of the parallelogram parallel to the other side $\mathbf{v}$: base and height stay the same, so the area does not change, for any value of $k$. The lecture calls this the geometric reincarnation of a row replacement, and reads it algebraically through linearity in one row (Theorem §21.11 applied to $A^T$): $\det\begin{bmatrix} \mathbf{v} \\ \mathbf{u} + k\mathbf{v} \end{bmatrix} = \det\begin{bmatrix} \mathbf{v} \\ \mathbf{u} \end{bmatrix} + \det\begin{bmatrix} \mathbf{v} \\ k\mathbf{v} \end{bmatrix}$, and the last determinant is $0$.
>
> *Source: 235 lecture L12*

^rem-21-1

> [!proof]+ Proof
> We prove the elementary-matrix form, by induction on the size $n$ of $A$. The case $n = 1$ is trivial (the only elementary operation is scaling).
>
> **The case $n = 2$** (Lay leaves it to Exercises 33–36 of 3.1). Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, so $\det A = ad - bc$.
> - Replacement: $\det\begin{bmatrix} a + kc & b + kd \\ c & d \end{bmatrix} = (a + kc)d - (b + kd)c = ad - bc$, and likewise $\det\begin{bmatrix} a & b \\ c + ka & d + kb \end{bmatrix} = a(d + kb) - b(c + ka) = ad - bc$.
> - Interchange: $\det\begin{bmatrix} c & d \\ a & b \end{bmatrix} = cb - da = -(ad - bc)$.
> - Scale: $\det\begin{bmatrix} ra & rb \\ c & d \end{bmatrix} = r(ad - bc) = \det\begin{bmatrix} a & b \\ rc & rd \end{bmatrix}$.
>
> Taking $A = I_2$ gives $\det E = 1, -1, r$ in the three cases, so in each case $\det EA = (\det E)(\det A)$.
>
> **Induction step.** Suppose the theorem holds for $k \times k$ matrices with $k \ge 2$, and let $A$ be $n \times n$, $n = k + 1 \ge 3$. The action of $E$ on $A$ involves either two rows or only one row, so there is a row, say row $i$, that $E$ leaves unchanged. Let $A_{ij}$ and $B_{ij}$ be the matrices obtained by deleting row $i$ and column $j$ from $A$ and from $EA$. The rows of $B_{ij}$ are obtained from the rows of $A_{ij}$ by the same type of elementary row operation that $E$ performs on $A$ (row $i$, which is deleted, takes no part in it). These submatrices are only $k \times k$, so the induction hypothesis gives
>
> $$
> \det B_{ij} = \alpha \cdot \det A_{ij}, \qquad \alpha = 1, -1 \text{ or } r \text{ according to the type of } E .
> $$
>
> Row $i$ of $EA$ is row $i$ of $A$, with entries $a_{i1}, \ldots, a_{in}$. The cofactor expansion across row $i$ ([[§20 Introduction to Determinants#^thm-20-1|Theorem §20.1]]) gives
>
> $$
> \begin{aligned}
> \det EA &= a_{i1}(-1)^{i+1}\det B_{i1} + \cdots + a_{in}(-1)^{i+n}\det B_{in} \\
> &= \alpha a_{i1}(-1)^{i+1}\det A_{i1} + \cdots + \alpha a_{in}(-1)^{i+n}\det A_{in} = \alpha \cdot \det A .
> \end{aligned}
> $$
>
> In particular, taking $A = I_n$ (with $\det I_n = 1$, [[§20 Introduction to Determinants#^thm-20-2|Theorem §20.2]]) shows $\det E = \alpha$. So $\det EA = (\det E)(\det A)$ for $n \times n$ matrices, and by induction for all $n$.

^pf-21-1

*Uses:* [[§21 Properties of Determinants#^def-21-1|Def. §21.1]], [[§20 Introduction to Determinants#^def-20-2|Def. §20.2]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]], [[§12 The Inverse of a Matrix|§12]] (elementary matrices)

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-57|LADR 9.57]]. The logic runs the other way there: $\det$ is first shown to be an alternating multilinear function of the columns ([[§34 Determinants#^ladr-9-45|LADR 9.45]]), and the effect of row and column operations follows in one line each. Lay starts from the cofactor recursion and needs an induction.

## Computing Determinants by Row Reduction

Suppose a square matrix $A$ has been reduced to an echelon form $U$ using only row replacements and row interchanges; this is always possible by the row reduction algorithm of [[§2 Row Reduction and Echelon Forms|§2]].

> [!theorem] Proposition §21.2: The Determinant from an Echelon Form
> If $A$ is reduced to an echelon form $U$ by row replacements and $r$ row interchanges, then $\det A = (-1)^r \det U$, and
>
> $$
> \det A = \begin{cases} (-1)^r \cdot \Big(\text{product of pivots in } U\Big) & \text{when } A \text{ is invertible,} \\[4pt] 0 & \text{when } A \text{ is not invertible.} \end{cases} \qquad (1)
> $$
>
> Although the echelon form $U$ and its pivots are not unique, the product of the pivots is unique up to sign.
>
> *Lay: 3.2, Equation (1)*

^prop-21-2

> [!proof]+ Proof
> By Theorem §21.1, each replacement leaves the determinant unchanged and each interchange changes its sign, so $\det A = (-1)^r \det U$. A square matrix in echelon form is upper triangular, so $\det U = u_{11}u_{22}\cdots u_{nn}$ ([[§20 Introduction to Determinants#^thm-20-2|Theorem §20.2]]).
>
> If $A$ is invertible, then $A \sim I_n$, so $A$ has a pivot in every column ([[§13 Characterizations of Invertible Matrices|§13]], Theorem 8); the pivot positions of an $n \times n$ echelon matrix with $n$ pivots are the diagonal positions, so the $u_{ii}$ are exactly the pivots (they have not been scaled to $1$). If $A$ is not invertible, $U$ has fewer than $n$ pivots, hence fewer than $n$ nonzero rows, so its last row is zero, $u_{nn} = 0$, and the product $u_{11}\cdots u_{nn}$ is $0$.
>
> Finally, $\det A$ does not depend on the choice of $U$, so neither does $(-1)^r \cdot (\text{product of pivots})$: the product of the pivots is determined by $A$ up to sign.

^pf-21-2

*Uses:* [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]], [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8)

> [!remark] Remark: Method — Computing a Determinant by Row Reduction
> 1. Row reduce $A$ to an echelon form $U$, using row replacements (no effect on $\det$) and interchanges (each changes the sign). Keep count of the interchanges, $r$.
> 2. It is often convenient to **factor out a common multiple of one row** (Theorem §21.1(c)): $\begin{vmatrix} * & * & * \\ 5k & -2k & 3k \\ * & * & * \end{vmatrix} = k \begin{vmatrix} * & * & * \\ 5 & -2 & 3 \\ * & * & * \end{vmatrix}$, the starred rows unchanged.
> 3. $\det A = (-1)^r \times (\text{factors pulled out}) \times (\text{product of the diagonal entries of } U)$.
> 4. Row operations combine with cofactor expansion: once a column has a single nonzero entry, expand down it ([[§20 Introduction to Determinants#^thm-20-1|Theorem §20.1]]) and continue with a smaller matrix.
> 5. If two rows (or columns) become equal, or a row becomes zero, stop: $\det A = 0$.
>
> The lecture's variant goes on to scale each pivot to $1$: if the scalings divide rows by $k_1, \ldots, k_s$ and the result has $1$'s on the diagonal, then $\det A = (-1)^{\#\text{swaps}} \, k_1 k_2 \cdots k_s$; if a zero row appears, $\det A = 0$.

^rem-21-2

> [!example] Example §21.1: Reducing to Triangular Form
> **(a)** The lecture's version, $A = \begin{bmatrix} 3 & 2 \\ -1 & 5 \end{bmatrix}$:
>
> $$
> \begin{bmatrix} 3 & 2 \\ -1 & 5 \end{bmatrix} \xrightarrow{\ R_1 \leftrightarrow R_2\ } \begin{bmatrix} -1 & 5 \\ 3 & 2 \end{bmatrix} \xrightarrow{\ R_2 + 3R_1\ } \begin{bmatrix} -1 & 5 \\ 0 & 17 \end{bmatrix} \xrightarrow{\ R_1 \div (-1),\ R_2 \div 17\ } \begin{bmatrix} 1 & -5 \\ 0 & 1 \end{bmatrix} .
> $$
>
> One swap and scaling factors $-1$, $17$: $\det A = (-1)^1 \cdot (-1)(17) = 17$. Check: $3 \cdot 5 - 2 \cdot (-1) = 17$.
>
> **(b)** $A = \begin{bmatrix} 1 & -4 & 2 \\ -2 & 8 & -9 \\ -1 & 7 & 0 \end{bmatrix}$. The two replacements in column 1 do not change the determinant:
>
> $$
> \det A = \begin{vmatrix} 1 & -4 & 2 \\ -2 & 8 & -9 \\ -1 & 7 & 0 \end{vmatrix} = \begin{vmatrix} 1 & -4 & 2 \\ 0 & 0 & -5 \\ -1 & 7 & 0 \end{vmatrix} = \begin{vmatrix} 1 & -4 & 2 \\ 0 & 0 & -5 \\ 0 & 3 & 2 \end{vmatrix} .
> $$
>
> Interchanging rows 2 and 3 reverses the sign:
>
> $$
> \det A = -\begin{vmatrix} 1 & -4 & 2 \\ 0 & 3 & 2 \\ 0 & 0 & -5 \end{vmatrix} = -(1)(3)(-5) = 15 .
> $$
>
> **(c)** $A = \begin{bmatrix} 2 & -8 & 6 & 8 \\ 3 & -9 & 5 & 10 \\ -3 & 0 & 1 & -2 \\ 1 & -4 & 0 & 6 \end{bmatrix}$. To get a $1$ in the upper-left corner, factor $2$ out of row 1 (instead of interchanging rows 1 and 4), then clear column 1 with $R_2 - 3R_1$, $R_3 + 3R_1$, $R_4 - R_1$:
>
> $$
> \det A = 2\begin{vmatrix} 1 & -4 & 3 & 4 \\ 3 & -9 & 5 & 10 \\ -3 & 0 & 1 & -2 \\ 1 & -4 & 0 & 6 \end{vmatrix} = 2\begin{vmatrix} 1 & -4 & 3 & 4 \\ 0 & 3 & -4 & -2 \\ 0 & -12 & 10 & 10 \\ 0 & 0 & -3 & 2 \end{vmatrix} .
> $$
>
> Use the $3$ as a pivot ($R_3 + 4R_2$), then $R_4 - \tfrac12 R_3$:
>
> $$
> \det A = 2\begin{vmatrix} 1 & -4 & 3 & 4 \\ 0 & 3 & -4 & -2 \\ 0 & 0 & -6 & 2 \\ 0 & 0 & -3 & 2 \end{vmatrix} = 2\begin{vmatrix} 1 & -4 & 3 & 4 \\ 0 & 3 & -4 & -2 \\ 0 & 0 & -6 & 2 \\ 0 & 0 & 0 & 1 \end{vmatrix} = 2 \cdot (1)(3)(-6)(1) = -36 .
> $$
>
> *Lay: Examples 3.2.1 and 3.2.2*
> *Source: 235 lecture L12*

^ex-21-1

> [!example] Example §21.2: Row Operations Plus Cofactor Expansion
> Compute $\det A$ for $A = \begin{bmatrix} 0 & 1 & 2 & -1 \\ 2 & 5 & -7 & 3 \\ 0 & 3 & 6 & 2 \\ -2 & -5 & 4 & -2 \end{bmatrix}$.
>
> Use the $2$ in column 1 as a pivot: $R_4 + R_2$ gives row 4 $= (0, 0, -3, 1)$. Now column 1 has the single entry $2$, in position $(2,1)$ with sign $-$, so
>
> $$
> \det A = \begin{vmatrix} 0 & 1 & 2 & -1 \\ 2 & 5 & -7 & 3 \\ 0 & 3 & 6 & 2 \\ 0 & 0 & -3 & 1 \end{vmatrix} = -2\begin{vmatrix} 1 & 2 & -1 \\ 3 & 6 & 2 \\ 0 & -3 & 1 \end{vmatrix} = -2\begin{vmatrix} 1 & 2 & -1 \\ 0 & 0 & 5 \\ 0 & -3 & 1 \end{vmatrix}
> $$
>
> (the last step is $R_2 - 3R_1$). Interchanging rows 2 and 3 would give a triangular determinant; instead expand down the first column:
>
> $$
> \det A = (-2)(1)\begin{vmatrix} 0 & 5 \\ -3 & 1 \end{vmatrix} = -2 \cdot (0 + 15) = -30 .
> $$
>
> *Lay: Example 3.2.4*

^ex-21-2

> [!example] Example §21.3: Row Operations Without Numbers
> **(a)** Let $\mathbf{v}_1, \ldots, \mathbf{v}_4$ be the rows of a $4 \times 4$ matrix with determinant $5$. Then
>
> $$
> \det\begin{bmatrix} \mathbf{v}_1 \\ \mathbf{v}_1 + \mathbf{v}_2 \\ \mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3 \\ \mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3 + \mathbf{v}_4 \end{bmatrix}
> = \det\begin{bmatrix} \mathbf{v}_1 \\ \mathbf{v}_2 \\ \mathbf{v}_2 + \mathbf{v}_3 \\ \mathbf{v}_2 + \mathbf{v}_3 + \mathbf{v}_4 \end{bmatrix}
> = \det\begin{bmatrix} \mathbf{v}_1 \\ \mathbf{v}_2 \\ \mathbf{v}_3 \\ \mathbf{v}_3 + \mathbf{v}_4 \end{bmatrix}
> = \det\begin{bmatrix} \mathbf{v}_1 \\ \mathbf{v}_2 \\ \mathbf{v}_3 \\ \mathbf{v}_4 \end{bmatrix} = 5,
> $$
>
> subtracting row 1 from rows 2–4, then row 2 from rows 3–4, then row 3 from row 4: only replacements.
>
> **(b)** For $A = \begin{bmatrix} 3 & -1 & 2 & -5 \\ 0 & 5 & -3 & -6 \\ -6 & 7 & -7 & 4 \\ -5 & -8 & 0 & 9 \end{bmatrix}$, adding $2$ times row 1 to row 3 gives row 3 $= (0, 5, -3, -6)$, equal to row 2. A matrix with two equal rows has dependent rows, so $\det A = 0$ (Corollary §21.5); or directly: one more replacement $R_3 - R_2$ produces a zero row.
>
> *Lay: Example 3.2.3*
> *Source: 235 lecture L12*

^ex-21-3

## Invertibility

> [!theorem] Theorem §21.3: Invertibility and the Determinant
> A square matrix $A$ is invertible if and only if $\det A \ne 0$.
>
> *Lay: Theorem 4 (3.2)*

^thm-21-3

> [!proof]+ Proof
> By formula (1) of Proposition §21.2: if $A$ is invertible, $\det A$ is $\pm$ a product of pivots, which are nonzero, so $\det A \ne 0$; if $A$ is not invertible, $\det A = 0$.

^pf-21-3

*Uses:* [[§21 Properties of Determinants#^prop-21-2|§21.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-50|LADR 9.50]], for operators on any finite-dimensional space, proved from multiplicativity ($1 = \det(TT^{-1})$) and, for the converse, from the fact that a nonzero alternating $n$-form does not vanish on a basis ([[§33 Alternating Multilinear Forms#^ladr-9-39|LADR 9.39]]), with no row reduction.

> [!theorem] Theorem §21.4: The Invertible Matrix Theorem (Continued)
> Let $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$ be an $n \times n$ matrix. The statement
>
> $$
> \det A \ne 0
> $$
>
> is equivalent to each statement of the Invertible Matrix Theorem ([[§13 Characterizations of Invertible Matrices|§13]], Theorem 8; extended in [[§19 Dimension and Rank|§19]], 2.9). In particular, the following are equivalent:
> - $A$ is invertible;
> - $\det A \ne 0$;
> - the columns of $A$ are linearly independent;
> - the columns of $A$ span $\mathbb{R}^n$;
> - $\{\mathbf{a}_1, \ldots, \mathbf{a}_n\}$ is a basis of $\mathbb{R}^n$;
> - $A^T$ is invertible, that is, the rows of $A$ are linearly independent.
>
> (Lay lists the determinant condition as statement (t) when the theorem is extended again in 5.2: [[§33 The Characteristic Equation|§33]].)
>
> *Lay: 3.2 (text after Theorem 4)*
> *Source: 235 lecture L11*

^thm-21-4

> [!proof]+ Proof
> $A$ is invertible if and only if $\det A \ne 0$ by Theorem §21.3, and invertibility is equivalent to every statement of the Invertible Matrix Theorem. For the rows: the rows of $A$ are the columns of $A^T$, which are linearly independent if and only if $A^T$ is invertible, which holds if and only if $A$ is invertible (both by the Invertible Matrix Theorem).

^pf-21-4

*Uses:* [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8), [[§19 Dimension and Rank|§19]] (IMT continued)

> [!theorem] Corollary §21.5: Dependent Rows or Columns
> If the columns of $A$ are linearly dependent, or the rows of $A$ are linearly dependent, then $\det A = 0$. In practice, linear dependence is obvious when two columns or two rows are equal, or when a column or a row is zero.
>
> *Lay: 3.2 (text)*

^cor-21-5

> [!proof]+ Proof
> If the columns of $A$ are dependent, $A$ is not invertible, so $\det A = 0$ by Theorem §21.3. If the rows of $A$ are dependent, the columns of $A^T$ are dependent, so $A^T$ is singular; then $A$ is singular too (Invertible Matrix Theorem), and $\det A = 0$.

^pf-21-5

*Uses:* [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§21 Properties of Determinants#^thm-21-4|§21.4]]

> [!remark]- Remark: Numerical Notes
> 1. Most computer programs compute $\det A$ for a general matrix by formula (1) of Proposition §21.2.
> 2. Evaluating an $n \times n$ determinant by row operations takes about $2n^3/3$ arithmetic operations. A $25 \times 25$ determinant needs only about $10{,}000$ operations, a fraction of a second, against the $500{,}000$ years of cofactor expansion ([[§20 Introduction to Determinants#^rem-20-3|Remark §20.3]]). The lecture: "$N!$ steps by the Laplace formula, $\sim N^3$ by row reduction".
> 3. Computers handle large sparse matrices with special routines, and zero entries speed up hand computation too (Example §21.2).

^rem-21-3

## Column Operations

> [!theorem] Theorem §21.6: The Determinant of the Transpose
> If $A$ is an $n \times n$ matrix, then $\det A^T = \det A$.
>
> *Lay: Theorem 5 (3.2)*

^thm-21-6

> [!proof]+ Proof
> By induction on $n$ (the Principle of Mathematical Induction: if $P(1)$ holds and $P(k)$ implies $P(k+1)$ for each $k$, then $P(n)$ holds for all $n \ge 1$). The theorem is obvious for $n = 1$. Suppose it is true for $k \times k$ determinants and let $n = k + 1$. The entry $a_{1j}$ of $A$ sits in position $(j, 1)$ of $A^T$, and deleting row $j$ and column $1$ of $A^T$ gives $(A_{1j})^T$. So the cofactor of $a_{1j}$ in $A^T$ is $(-1)^{j+1}\det (A_{1j})^T = (-1)^{1+j}\det A_{1j}$, the cofactor of $a_{1j}$ in $A$, by the induction hypothesis applied to the $k \times k$ matrix $A_{1j}$. Hence the cofactor expansion of $\det A$ across the first *row* equals the cofactor expansion of $\det A^T$ down the first *column*, and by [[§20 Introduction to Determinants#^thm-20-1|Theorem §20.1]] these are $\det A$ and $\det A^T$. The theorem is true for $n = 1$, and its truth for one value of $n$ implies its truth for the next, so it is true for all $n \ge 1$.

^pf-21-6

*Uses:* [[§20 Introduction to Determinants#^def-20-2|Def. §20.2]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]]

> [!theorem] Corollary §21.7: Column Operations
> Each statement of Theorem §21.1 remains true when the word *row* is replaced everywhere by *column*: a column replacement does not change $\det A$, interchanging two columns changes its sign, and multiplying a column by $k$ multiplies $\det A$ by $k$. Likewise Corollary §21.5 gives $\det A = 0$ when two columns are equal.
>
> *Lay: 3.2 (text after Theorem 5)*

^cor-21-7

> [!proof]+ Proof
> A column operation on $A$ is the same as the corresponding row operation on $A^T$. Apply Theorem §21.1 to $A^T$ and use $\det A^T = \det A$ (Theorem §21.6) before and after.

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
> *The lecture does $n = 3$ and the step from $n = 4$ to $n = 3$; here is the general induction.* For $n = 1$ the determinant is $1$, the empty product. Let $n \ge 2$. For $k = n, n-1, \ldots, 2$, in this order, replace row $k$ by row $k$ minus $z_1$ times row $k - 1$ (working from the bottom up, row $k - 1$ is still the original one when it is used). These replacements do not change the determinant (Theorem §21.1(a)), and the new $(k, j)$-entry is
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
> Column $j$ of this matrix has the common factor $z_j - z_1$; pulling it out of each column (Corollary §21.7) leaves $\Delta(z_2, \ldots, z_n)$:
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

> [!remark] Remark: Why It Works
> The lecture's geometric reason: the linear map $\mathbf{x} \mapsto A\mathbf{x}$ multiplies volumes by $|\det A|$ ([[§22 Cramer’s Rule, Volume, and Linear Transformations|§22]], Theorem 10 of 3.3). Applying $B$ and then $A$ multiplies a volume first by $|\det B|$, then by $|\det A|$; and the composite is the map of $AB$. So $|\det AB| = |\det A|\,|\det B|$, at least up to sign.
>
> *Source: 235 lecture L12*

^rem-21-4

> [!proof]+ Proof
> **$A$ not invertible.** Then $AB$ is not invertible either. (Lay cites Exercise 27 of 2.3; here is why: if $AB$ had an inverse, then $W = B(AB)^{-1}$ would satisfy $AW = I$, and an $n \times n$ matrix with a right inverse is invertible by the Invertible Matrix Theorem, a contradiction.) By Theorem §21.3 both sides of $\det AB = (\det A)(\det B)$ are $0$.
>
> **$A$ invertible.** Then $A$ is row equivalent to $I_n$ (Invertible Matrix Theorem), so there are elementary matrices $E_1, \ldots, E_p$ with
>
> $$
> A = E_pE_{p-1}\cdots E_1 \cdot I_n = E_pE_{p-1}\cdots E_1 .
> $$
>
> Write $|A|$ for $\det A$. Repeated use of Theorem §21.1 in the form $\det EM = (\det E)(\det M)$ gives
>
> $$
> |AB| = |E_p \cdots E_1 B| = |E_p|\,|E_{p-1}\cdots E_1 B| = \cdots = |E_p|\cdots|E_1|\,|B| ,
> $$
>
> and the same computation with $B = I_n$ gives $|A| = |E_p|\cdots|E_1|$. Hence $|AB| = |A|\,|B|$.

^pf-21-9

*Uses:* [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§13 Characterizations of Invertible Matrices|§13]] (Theorem 8), [[§12 The Inverse of a Matrix|§12]] (Theorem 7: invertible matrices are products of elementary matrices)

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-49|LADR 9.49]], where multiplicativity is immediate from the definition of $\det T$ as the factor by which $T$ scales alternating $n$-forms; transpose: [[§34 Determinants#^ladr-9-56|LADR 9.56]].
> - In group language, $\det: GL_n(\mathbb{R}) \to \mathbb{R}^\times$ is a homomorphism from the general linear group ([[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]]) to the nonzero reals under multiplication.

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
> 1. $\det A \cdot \det A^{-1} = \det(AA^{-1}) = \det I = 1$ (Theorem §21.9, [[§20 Introduction to Determinants#^thm-20-2|Theorem §20.2]]), so $\det A \ne 0$ and $\det A^{-1} = 1/\det A$.
> 2. Induction on $k$: $\det A^{k+1} = \det(A^k A) = (\det A)^k \det A$. For negative $k$ combine with part 1.
> 3. $rA$ is obtained from $A$ by multiplying each of its $n$ rows by $r$; by Theorem §21.1(c) each multiplies the determinant by $r$.
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
> By Theorem §21.6 the same holds for each row. This (multi-)linearity is the starting point of the advanced treatment of determinants.
>
> *Lay: 3.2 (text), Equations (2) and (3)*

^thm-21-11

> [!proof]+ Proof
> Lay obtains (2) from Theorem §21.1(c) for columns, and (3) from a cofactor expansion down column $j$ (Exercise 43); the expansion gives both at once. Write $\mathbf{x} = (x_1, \ldots, x_n)$. Expanding down column $j$ ([[§20 Introduction to Determinants#^thm-20-1|Theorem §20.1]]),
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
