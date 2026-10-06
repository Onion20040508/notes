---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 3
section: 21
lay: "3.2"
aliases: ["Lay 3.2"]
tags: [applied-linear-algebra, math235]
---
← [[§20 Introduction to Determinants]] · ↑ [[· 3 Determinants]] · [[§21a Transposes, Products, and Linearity of Determinants]] →

*Lay, Section 3.2 · MATH 235 lectures L11, L12.*

"The secret of determinants lies in how they change when row operations are performed" (Lay). A row replacement leaves the determinant unchanged, an interchange changes its sign, and scaling a row scales it. So row reducing to an echelon form computes $\det A$ in about $n^3$ steps instead of $n!$, and the same computation proves the central fact: $A$ is invertible if and only if $\det A \ne 0$, a new statement in the Invertible Matrix Theorem. The section also shows that $\det A^T = \det A$ (so columns behave like rows), that $\det AB = (\det A)(\det B)$, and that $\det A$ is a linear function of each column separately.

## Row Operations

[[§12 The Inverse of a Matrix#^prop-12-6|Proposition §12.6]] (2.2) showed that each elementary row operation on an $n \times n$ matrix $A$ is left multiplication by an elementary matrix $E$, obtained by performing the same operation on $I_n$.

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
> Equivalently, in terms of [[§21 Properties of Determinants#^def-21-1|Definition §21.1]]: if $A$ is $n \times n$ and $E$ is an $n \times n$ elementary matrix, then
>
> $$
> \det EA = (\det E)(\det A), \qquad \text{where} \quad \det E = \begin{cases} 1 & \text{if } E \text{ is a row replacement,} \\ -1 & \text{if } E \text{ is an interchange,} \\ r & \text{if } E \text{ is a scale by } r . \end{cases}
> $$
>
> *Lay: Theorem 3 (3.2)*

^thm-21-1

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

*Uses:* [[§21 Properties of Determinants#^def-21-1|Def. §21.1]], [[§20 Introduction to Determinants#^def-20-2|Def. §20.2]], [[§20 Introduction to Determinants#^thm-20-1|§20.1]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]], [[§12 The Inverse of a Matrix#^def-12-3|Def. §12.3]], [[§12 The Inverse of a Matrix#^prop-12-6|§12.6]] (elementary matrices)

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-57|LADR 9.57]]. The logic runs the other way there: $\det$ is first shown to be an alternating multilinear function of the columns ([[§34 Determinants#^ladr-9-45|LADR 9.45]]), and the effect of row and column operations follows in one line each. Lay starts from the cofactor recursion and needs an induction.

> [!remark] Remark: Why It Works
> For $n = 2$, $|\det|$ is the area of the parallelogram spanned by the rows ([[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-4|Theorem §22.4]], applied to $A^T$). Replacing a row $\mathbf{u}$ by $\mathbf{u} + k\mathbf{v}$ slides one side of the parallelogram parallel to the other side $\mathbf{v}$: base and height stay the same, so the area does not change, for any value of $k$. The lecture calls this the geometric reincarnation of a row replacement, and reads it algebraically through linearity in one row ([[§21a Transposes, Products, and Linearity of Determinants#^thm-21-11|Theorem §21.11]] applied to $A^T$): $\det\begin{bmatrix} \mathbf{v} \\ \mathbf{u} + k\mathbf{v} \end{bmatrix} = \det\begin{bmatrix} \mathbf{v} \\ \mathbf{u} \end{bmatrix} + \det\begin{bmatrix} \mathbf{v} \\ k\mathbf{v} \end{bmatrix}$, and the last determinant is $0$.
>
> *Source: 235 lecture L12*

^rem-21-1

## Computing Determinants by Row Reduction

Suppose a square matrix $A$ has been reduced to an echelon form $U$ using only row replacements and row interchanges; this is always possible by the row reduction algorithm of [[§2 Row Reduction and Echelon Forms#^rem-2-1|§2, Remark: Method — The Row Reduction Algorithm]].

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
> By [[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]], each replacement leaves the determinant unchanged and each interchange changes its sign, so $\det A = (-1)^r \det U$. A square matrix in echelon form is upper triangular, so $\det U = u_{11}u_{22}\cdots u_{nn}$ ([[§20 Introduction to Determinants#^thm-20-2|Theorem §20.2]]).
>
> If $A$ is invertible, then $A \sim I_n$, so $A$ has a pivot in every column ([[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1]]); the pivot positions of an $n \times n$ echelon matrix with $n$ pivots are the diagonal positions, so the $u_{ii}$ are exactly the pivots (they have not been scaled to $1$). If $A$ is not invertible, $U$ has fewer than $n$ pivots, hence fewer than $n$ nonzero rows, so its last row is zero, $u_{nn} = 0$, and the product $u_{11}\cdots u_{nn}$ is $0$.
>
> Finally, $\det A$ does not depend on the choice of $U$, so neither does $(-1)^r \cdot (\text{product of pivots})$: the product of the pivots is determined by $A$ up to sign.

^pf-21-2

*Uses:* [[§21 Properties of Determinants#^thm-21-1|§21.1]], [[§20 Introduction to Determinants#^thm-20-2|§20.2]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]]

> [!remark] Remark: Method — Computing a Determinant by Row Reduction
> 1. Row reduce $A$ to an echelon form $U$, using row replacements (no effect on $\det$) and interchanges (each changes the sign). Keep count of the interchanges, $r$.
> 2. It is often convenient to **factor out a common multiple of one row** ([[§21 Properties of Determinants#^thm-21-1|Theorem §21.1]](c)): $\begin{vmatrix} \ast  & \ast  & \ast  \\ 5k & -2k & 3k \\ \ast  & \ast  & \ast  \end{vmatrix} = k \begin{vmatrix} \ast  & \ast  & \ast  \\ 5 & -2 & 3 \\ \ast  & \ast  & \ast  \end{vmatrix}$, the starred rows unchanged.
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
> **(b)** For $A = \begin{bmatrix} 3 & -1 & 2 & -5 \\ 0 & 5 & -3 & -6 \\ -6 & 7 & -7 & 4 \\ -5 & -8 & 0 & 9 \end{bmatrix}$, adding $2$ times row 1 to row 3 gives row 3 $= (0, 5, -3, -6)$, equal to row 2. A matrix with two equal rows has dependent rows, so $\det A = 0$ ([[§21 Properties of Determinants#^cor-21-5|Corollary §21.5]]); or directly: one more replacement $R_3 - R_2$ produces a zero row.
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
> By formula (1) of [[§21 Properties of Determinants#^prop-21-2|Proposition §21.2]]: if $A$ is invertible, $\det A$ is $\pm$ a product of pivots, which are nonzero, so $\det A \ne 0$; if $A$ is not invertible, $\det A = 0$.

^pf-21-3

*Uses:* [[§21 Properties of Determinants#^prop-21-2|§21.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§34 Determinants#^ladr-9-50|LADR 9.50]], for operators on any finite-dimensional space, proved from multiplicativity ($1 = \det(TT^{-1})$) and, for the converse, from the fact that a nonzero alternating $n$-form does not vanish on a basis ([[§33 Alternating Multilinear Forms#^ladr-9-39|LADR 9.39]]), with no row reduction.
> - See also: the determinant test in differential equations, where the determinant is the Wronskian. For $y'' + py' + qy = 0$, two solutions can be combined to meet every pair of initial conditions at $t_0$ if and only if their Wronskian is nonzero there, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-3|331 Thm. §14.3]]; for $n$ solutions of $\mathbf{x}' = P(t)\mathbf{x}$ with nonzero Wronskian, every solution is a unique combination of them, [[§30 Basic Theory of Systems of First-Order Linear Equations#^thm-30-2|331 Thm. §30.2]].

> [!theorem] Theorem §21.4: The Invertible Matrix Theorem (Continued)
> Let $A = [\mathbf{a}_1 \ \cdots \ \mathbf{a}_n]$ be an $n \times n$ matrix. The statement
>
> $$
> \det A \ne 0
> $$
>
> is equivalent to each statement of the Invertible Matrix Theorem: (a)–(l) of [[§13 Characterizations of Invertible Matrices#^thm-13-1|Theorem §13.1]] and (m)–(r) of [[§19 Dimension and Rank#^thm-19-3|Theorem §19.3]], the previous version. In particular, the following are equivalent:
> - $A$ is invertible;
> - $\det A \ne 0$;
> - the columns of $A$ are linearly independent;
> - the columns of $A$ span $\mathbb{R}^n$;
> - $\{\mathbf{a}_1, \ldots, \mathbf{a}_n\}$ is a basis of $\mathbb{R}^n$;
> - $A^T$ is invertible, that is, the rows of $A$ are linearly independent.
>
> (The next version is [[§28 Rank#^thm-28-5|Theorem §28.5]], Lay 4.6, which restates (m)–(r). Lay lists the determinant condition as statement (t) when the theorem is extended again in 5.2: [[§33 The Characteristic Equation#^thm-33-2|Theorem §33.2]].)
>
> *Lay: 3.2 (text after Theorem 4)*
> *Source: 235 lecture L11*

^thm-21-4

> [!proof]+ Proof
> $A$ is invertible if and only if $\det A \ne 0$ by [[§21 Properties of Determinants#^thm-21-3|Theorem §21.3]], and invertibility is equivalent to every statement of the Invertible Matrix Theorem. For the rows: the rows of $A$ are the columns of $A^T$, which are linearly independent if and only if $A^T$ is invertible, which holds if and only if $A$ is invertible (both by the Invertible Matrix Theorem).

^pf-21-4

*Uses:* [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]], [[§19 Dimension and Rank#^thm-19-3|§19.3]]

> [!theorem] Corollary §21.5: Dependent Rows or Columns
> If the columns of $A$ are linearly dependent, or the rows of $A$ are linearly dependent, then $\det A = 0$. In practice, linear dependence is obvious when two columns or two rows are equal, or when a column or a row is zero.
>
> *Lay: 3.2 (text)*

^cor-21-5

> [!proof]+ Proof
> If the columns of $A$ are dependent, $A$ is not invertible, so $\det A = 0$ by [[§21 Properties of Determinants#^thm-21-3|Theorem §21.3]]. If the rows of $A$ are dependent, the columns of $A^T$ are dependent, so $A^T$ is singular; then $A$ is singular too (Invertible Matrix Theorem), and $\det A = 0$.

^pf-21-5

*Uses:* [[§21 Properties of Determinants#^thm-21-3|§21.3]], [[§21 Properties of Determinants#^thm-21-4|§21.4]]

> [!remark]- Remark: Numerical Notes
> 1. Most computer programs compute $\det A$ for a general matrix by formula (1) of [[§21 Properties of Determinants#^prop-21-2|Proposition §21.2]].
> 2. Evaluating an $n \times n$ determinant by row operations takes about $2n^3/3$ arithmetic operations. A $25 \times 25$ determinant needs only about $10{,}000$ operations, a fraction of a second, against the $500{,}000$ years of cofactor expansion ([[§20 Introduction to Determinants#^rem-20-3|§20, Remark: The Cost of Cofactor Expansion]]). The lecture: "$N!$ steps by the Laplace formula, $\sim N^3$ by row reduction".
> 3. Computers handle large sparse matrices with special routines, and zero entries speed up hand computation too ([[§21 Properties of Determinants#^ex-21-2|Example §21.2]]).

^rem-21-3

*Continued in [[§21a Transposes, Products, and Linearity of Determinants]]: column operations and the transpose, the multiplicative property, and linearity in each column.*
