---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 2
lay: "1.2"
aliases: ["Lay 1.2"]
tags: [applied-linear-algebra, math235]
---
← [[§1 Systems of Linear Equations]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§3 Vector Equations]] →

*Lay, Section 1.2 and Appendix A · MATH 235 lectures L1, L2.*

This section turns the elimination of [[§1 Systems of Linear Equations|§1]] into the row reduction algorithm, which brings any matrix to echelon form (forward phase) and then to reduced echelon form (backward phase). The reduced echelon form of a matrix is unique (proved here, following Lay's Appendix A), so its leading entries, the pivot positions, belong to the matrix itself. Pivots answer the two fundamental questions at once. A system is consistent exactly when the last column of its augmented matrix is not a pivot column, and a consistent system has a unique solution exactly when there are no free variables. Otherwise the free variables parametrize the infinitely many solutions.

## Echelon Forms

A **nonzero row** or column of a matrix is one that contains at least one nonzero entry. The **leading entry** of a nonzero row is its leftmost nonzero entry.

> [!definition] Definition §2.1: Echelon Form and Reduced Echelon Form
> A rectangular matrix is in **echelon form** (or **row echelon form**) if it has the following three properties:
> 1. All nonzero rows are above any rows of all zeros.
> 2. Each leading entry of a row is in a column to the right of the leading entry of the row above it.
> 3. All entries in a column below a leading entry are zeros.
>
> If a matrix in echelon form satisfies the following additional conditions, it is in **reduced echelon form** (or **reduced row echelon form**):
>
> 4. The leading entry in each nonzero row is $1$.
> 5. Each leading $1$ is the only nonzero entry in its column.
>
> An **echelon matrix** (respectively, **reduced echelon matrix**) is one in echelon form (respectively, reduced echelon form). Property 2 says that the leading entries form a steplike ("echelon") pattern moving down and to the right; property 3 follows from property 2 but is listed for emphasis. In the lecture's words: the first nonzero entry of each row has only zeros to its left and below it.
>
> *Lay: 1.2, Definition*

^def-2-1

> [!example] Example §2.1: Echelon or Not?
> With $\blacksquare$ a nonzero leading entry and $*$ any value, the general patterns
>
> $$
> \begin{bmatrix} \blacksquare & * & * & * \\ 0 & \blacksquare & * & * \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix},
> \qquad
> \begin{bmatrix} 1 & 0 & * & * \\ 0 & 1 & * & * \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
> $$
>
> are an echelon matrix and a reduced echelon matrix. Some specific matrices:
>
> $$
> \text{(a)}\ \begin{bmatrix} 4 & 3 & 4 & -1 \\ 0 & 0 & 2 & 3 \\ 0 & 0 & 0 & 1 \end{bmatrix}
> \qquad
> \text{(b)}\ \begin{bmatrix} 4 & 3 & 4 & -1 \\ 0 & 0 & 2 & 3 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 7 \end{bmatrix}
> \qquad
> \text{(c)}\ \begin{bmatrix} 1 & 2 & 3 \\ 0 & 5 & 0 \\ 2 & 0 & 1 \end{bmatrix}
> $$
>
> **(a)** is in echelon form: the leading entries $4, 2, 1$ step down and to the right. It is not reduced (the leading entries are not all $1$, and there are nonzero entries above the leading $2$ and $1$).
>
> **(b)** is not: the leading entry $2$ of row 3 is directly below the leading entry of row 2, with a nonzero entry under a leading entry. Subtracting row 2 from row 3 gives the row $[\,0\ 0\ 0\ {-2}\,]$; then adding $\tfrac72$ times this row to row 4 clears the $7$:
>
> $$
> \begin{bmatrix} 4 & 3 & 4 & -1 \\ 0 & 0 & 2 & 3 \\ 0 & 0 & 0 & -2 \\ 0 & 0 & 0 & 0 \end{bmatrix} ,
> $$
>
> an echelon form of (b).
>
> **(c)** is not: the entry $2$ below the leading $1$ of row 1 must be $0$.
>
> *Lay: Example 1.2.1*
> *Source: 235 lecture L1*

^ex-2-1

A matrix can be row reduced to many different echelon forms, by different sequences of row operations. The reduced echelon form, however, is unique.

> [!theorem] Theorem §2.1: Uniqueness of the Reduced Echelon Form
> Each matrix is row equivalent to one and only one reduced echelon matrix.
>
> *Lay: Theorem 1 (1.2); proof in Appendix A*

^thm-2-1

> [!proof]- Proof
> **Existence.** The row reduction algorithm (Remark: Method — The Row Reduction Algorithm, below) transforms any matrix $A$ into a reduced echelon matrix by row operations.
>
> **Uniqueness.** Let $A$ be $m \times n$, and suppose $A$ is row equivalent to reduced echelon matrices $U$ and $V$. Row equivalence is symmetric ([[§1 Systems of Linear Equations#^prop-1-1|Proposition §1.1]]) and transitive (perform one sequence of operations after the other), so $U \sim V$. Write $\mathbf{u}_1, \ldots, \mathbf{u}_n$ and $\mathbf{v}_1, \ldots, \mathbf{v}_n$ for the columns of $U$ and $V$. In $U$, call the location of a leading $1$ a *pivot position* and a column containing one a *pivot column*; this uses only the shape of $U$, not uniqueness. The proof idea (Lay's Appendix A): row-equivalent matrices have the same linear dependence relations among their columns.
>
> **Step 1: the same relations.** A list $(c_1, \ldots, c_n)$ satisfies $c_1\mathbf{u}_1 + \cdots + c_n\mathbf{u}_n = \mathbf{0}$ (entrywise: $\sum_j c_j u_{ij} = 0$ for every row $i$) exactly when it solves the homogeneous system with augmented matrix $[\,U\ \ \mathbf{0}\,]$. The row operations that turn $U$ into $V$ turn $[\,U\ \ \mathbf{0}\,]$ into $[\,V\ \ \mathbf{0}\,]$, since they keep a zero column zero. By [[§1 Systems of Linear Equations#^thm-1-2|Theorem §1.2]] the two systems have the same solutions:
>
> $$
> c_1\mathbf{u}_1 + \cdots + c_n\mathbf{u}_n = \mathbf{0} \iff c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0} . \qquad (\ast)
> $$
>
> **Step 2: pivot columns of a reduced echelon matrix.** *Claim:* column $j$ of $U$ is a pivot column if and only if it is not a linear combination of the columns to its left (for $j = 1$: if and only if it is nonzero). Let the nonzero rows of $U$ be rows $1, \ldots, r$, with leading $1$'s in columns $p_1 < p_2 < \cdots < p_r$. Since $U$ is reduced, column $p_i$ is $\mathbf{e}_i$: a $1$ in row $i$ and zeros elsewhere.
> - If $j = p_i$, then every column $k < j$ has a $0$ in row $i$ (those entries lie to the left of the leading entry of row $i$). So every combination of columns $1, \ldots, j - 1$ has $0$ in row $i$, while column $j$ has $1$ there: it is not such a combination.
> - If $j$ is not a pivot column, let $s$ be the number of pivot columns to its left, $p_s < j < p_{s+1}$. For each row $i > s$, the leading entry of row $i$ (if any) is in column $p_i > j$, so $u_{ij} = 0$. Hence
>
> $$
> \mathbf{u}_j = \sum_{i=1}^{s} u_{ij}\,\mathbf{e}_i = \sum_{i=1}^{s} u_{ij}\,\mathbf{u}_{p_i}, \qquad (\ast\ast)
> $$
>
>   a combination of the pivot columns to its left (the zero column if $s = 0$).
>
> **Step 3: the pivot columns agree.** "Column $j$ is a linear combination of the columns to its left" means that there are $c_1, \ldots, c_n$ with $c_j = 1$, $c_k = 0$ for $k > j$, and $\sum_k c_k\mathbf{u}_k = \mathbf{0}$. By $(\ast)$ this holds for $U$ exactly when it holds for $V$. By Step 2 (which applies equally to $V$), $U$ and $V$ have their pivot columns in the same places $p_1 < \cdots < p_r$. Both are reduced, so in both the column $p_i$ equals $\mathbf{e}_i$: corresponding pivot columns of $U$ and $V$ are equal.
>
> **Step 4: the other columns agree.** Let $j$ be a nonpivot column. By $(\ast\ast)$, the list $\mathbf{c}$ with $c_j = 1$, $c_{p_i} = -u_{ij}$ for $i \le s$, and all other entries $0$ satisfies $\sum_k c_k\mathbf{u}_k = \mathbf{0}$. By $(\ast)$, $\sum_k c_k\mathbf{v}_k = \mathbf{0}$ as well, that is,
>
> $$
> \mathbf{v}_j = \sum_{i=1}^{s} u_{ij}\,\mathbf{v}_{p_i} = \sum_{i=1}^{s} u_{ij}\,\mathbf{e}_i = \mathbf{u}_j .
> $$
>
> So every column of $V$ equals the corresponding column of $U$, and $V = U$. (Lay's Appendix A cites the fact from Section 4.3 that the pivot columns form a basis for the span of the columns; Step 2 replaces it by the direct computation $(\ast\ast)$.)

^pf-2-1

*Uses:* [[§1 Systems of Linear Equations#^prop-1-1|§1.1]], [[§1 Systems of Linear Equations#^thm-1-2|§1.2]], [[§2 Row Reduction and Echelon Forms#^def-2-1|Def. §2.1]], [[§3 Vector Equations#^def-3-3|Def. §3.3]] (linear combinations)

> [!definition] Definition §2.2: Echelon Form and Reduced Echelon Form of a Matrix
> If a matrix $A$ is row equivalent to an echelon matrix $U$, then $U$ is **an echelon form** (or row echelon form) **of $A$**. If $U$ is in reduced echelon form, $U$ is **the reduced echelon form of $A$**; "the" is justified by Theorem §2.1. Matrix programs abbreviate it **RREF** (and an echelon form **REF**).
>
> *Lay: 1.2 (text)*

^def-2-2

## Pivot Positions

> [!theorem] Corollary §2.2: Leading Entries Do Not Depend on the Echelon Form
> The leading entries of every echelon form of a matrix $A$ are in the same positions, namely the positions of the leading $1$'s in the reduced echelon form of $A$.
>
> *Lay: 1.2 (text)*

^cor-2-2

> [!proof]+ Proof
> Let $U$ be an echelon form of $A$. Turn $U$ into a reduced echelon matrix by the backward phase of row reduction (step 5 of the algorithm below): scale each nonzero row so that its leading entry is $1$, and add multiples of each row to the rows *above* it to create zeros above its leading entry. Scaling a row by $c \ne 0$ does not move its leading entry. If row $i$ has its leading entry in column $q$ and $r < i$, then row $r$ has its leading entry in a column $q' < q$, and adding a multiple of row $i$ to row $r$ changes only entries of row $r$ in columns $\ge q$, so row $r$ keeps its leading entry in column $q'$. Thus the result $R$ has its leading $1$'s exactly where $U$ has its leading entries. $R$ is row equivalent to $A$, so by Theorem §2.1 it is *the* reduced echelon form of $A$. Hence the leading entries of $U$ sit at the leading $1$'s of the reduced echelon form of $A$, whichever echelon form $U$ was.

^pf-2-2

*Uses:* [[§2 Row Reduction and Echelon Forms#^thm-2-1|§2.1]], [[§2 Row Reduction and Echelon Forms#^def-2-1|Def. §2.1]]

> [!definition] Definition §2.3: Pivot Position, Pivot Column, Pivot
> A **pivot position** in a matrix $A$ is a location in $A$ that corresponds to a leading $1$ in the reduced echelon form of $A$. A **pivot column** is a column of $A$ that contains a pivot position. A **pivot** is a nonzero number in a pivot position that is used as needed to create zeros by row operations.
>
> By Corollary §2.2, the pivot positions are also the locations of the leading entries in *any* echelon form of $A$.
>
> *Lay: 1.2, Definition; 1.2 (text)*

^def-2-3

> [!example] Example §2.2: Locating the Pivot Columns
> Row reduce $A$ to echelon form and locate the pivot columns of $A$:
>
> $$
> A = \begin{bmatrix} 0 & -3 & -6 & 4 & 9 \\ -1 & -2 & -1 & 3 & 1 \\ -2 & -3 & 0 & 3 & -1 \\ 1 & 4 & 5 & -9 & -7 \end{bmatrix} .
> $$
>
> The top of the leftmost nonzero column is the first pivot position, and a nonzero entry must be placed there. Interchanging rows 1 and 4 avoids fractions. Then add row 1 to row 2 and $2$ times row 1 to row 3:
>
> $$
> \begin{bmatrix} 1 & 4 & 5 & -9 & -7 \\ -1 & -2 & -1 & 3 & 1 \\ -2 & -3 & 0 & 3 & -1 \\ 0 & -3 & -6 & 4 & 9 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 4 & 5 & -9 & -7 \\ 0 & 2 & 4 & -6 & -6 \\ 0 & 5 & 10 & -15 & -15 \\ 0 & -3 & -6 & 4 & 9 \end{bmatrix} .
> $$
>
> The next pivot position is as far left as possible in row 2: column 2, with pivot $2$. Add $-\tfrac52$ times row 2 to row 3 and $\tfrac32$ times row 2 to row 4:
>
> $$
> \begin{bmatrix} 1 & 4 & 5 & -9 & -7 \\ 0 & 2 & 4 & -6 & -6 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -5 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 4 & 5 & -9 & -7 \\ 0 & 2 & 4 & -6 & -6 \\ 0 & 0 & 0 & -5 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> (Entrywise, row 3: $5 - \tfrac52 \cdot 2 = 0$, $10 - \tfrac52 \cdot 4 = 0$, $-15 + 15 = 0$, $-15 + 15 = 0$; row 4: $-3 + 3 = 0$, $-6 + 6 = 0$, $4 - 9 = -5$, $9 - 9 = 0$.) No leading entry can be created in column 3 without destroying the steps already built, but interchanging rows 3 and 4 produces one in column 4. The matrix is now in echelon form, with pattern
>
> $$
> \begin{bmatrix} \blacksquare & * & * & * & * \\ 0 & \blacksquare & * & * & * \\ 0 & 0 & 0 & \blacksquare & * \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So the pivot columns of $A$ are columns $1$, $2$ and $4$, and the pivot positions of $A$ are the $(1,1)$, $(2,2)$ and $(3,4)$ entries. The pivots used were $1$, $2$ and $-5$; they are not the entries $0$, $-2$, $3$ of $A$ in the pivot positions.
>
> *Lay: Example 1.2.2*

^ex-2-2

## The Row Reduction Algorithm

> [!remark] Remark: Method — The Row Reduction Algorithm
> 1. Begin with the leftmost nonzero column. This is a pivot column; the pivot position is at the top.
> 2. Select a nonzero entry in the pivot column as a pivot. If necessary, interchange rows to move this entry into the pivot position.
> 3. Use row replacement operations to create zeros in all positions below the pivot.
> 4. Cover (or ignore) the row containing the pivot position and all rows above it. Apply steps 1–3 to the submatrix that remains. Repeat until there are no more nonzero rows to modify.
> 5. Beginning with the rightmost pivot and working upward and to the left, create zeros above each pivot. If a pivot is not $1$, make it $1$ by a scaling operation.
>
> Steps 1–4 are the **forward phase** of the algorithm and produce an echelon form; step 5 is the **backward phase** and produces the (unique) reduced echelon form. The lecture's version of the operations: divide a row by a nonzero number, subtract a multiple of a row from another row, swap rows.

^rem-2-1

> [!example] Example §2.3: The Algorithm Step by Step
> Transform the matrix first into echelon form and then into reduced echelon form:
>
> $$
> \begin{bmatrix} 0 & 3 & -6 & 6 & 4 & -5 \\ 3 & -7 & 8 & -5 & 8 & 9 \\ 3 & -9 & 12 & -9 & 6 & 15 \end{bmatrix} .
> $$
>
> **Steps 1–2.** Column 1 is the leftmost nonzero column; its top entry is $0$, so interchange rows 1 and 3 (rows 1 and 2 would also do).
>
> **Step 3.** With two $3$'s in column 1, add $-1$ times row 1 to row 2 (no need to divide by the pivot first):
>
> $$
> \begin{bmatrix} 3 & -9 & 12 & -9 & 6 & 15 \\ 3 & -7 & 8 & -5 & 8 & 9 \\ 0 & 3 & -6 & 6 & 4 & -5 \end{bmatrix}
> \sim
> \begin{bmatrix} 3 & -9 & 12 & -9 & 6 & 15 \\ 0 & 2 & -4 & 4 & 2 & -6 \\ 0 & 3 & -6 & 6 & 4 & -5 \end{bmatrix} .
> $$
>
> **Step 4.** Cover row 1. Column 2 is the next pivot column, with pivot $2$. Add $-\tfrac32$ times row 2 to row 3 ($3 - 3 = 0$, $-6 + 6 = 0$, $6 - 6 = 0$, $4 - 3 = 1$, $-5 + 9 = 4$):
>
> $$
> \begin{bmatrix} 3 & -9 & 12 & -9 & 6 & 15 \\ 0 & 2 & -4 & 4 & 2 & -6 \\ 0 & 0 & 0 & 0 & 1 & 4 \end{bmatrix} .
> $$
>
> Covering row 2 leaves one row with leading entry $1$ in column 5; steps 1–3 need no work. This is an echelon form; the pivot columns are 1, 2 and 5.
>
> **Step 5.** Clear above the rightmost pivot (row 3): add $-6$ times row 3 to row 1 and $-2$ times row 3 to row 2. Then scale row 2 by $\tfrac12$, add $9$ times row 2 to row 1, and scale row 1 by $\tfrac13$:
>
> $$
> \begin{bmatrix} 3 & -9 & 12 & -9 & 0 & -9 \\ 0 & 2 & -4 & 4 & 0 & -14 \\ 0 & 0 & 0 & 0 & 1 & 4 \end{bmatrix}
> \sim
> \begin{bmatrix} 3 & -9 & 12 & -9 & 0 & -9 \\ 0 & 1 & -2 & 2 & 0 & -7 \\ 0 & 0 & 0 & 0 & 1 & 4 \end{bmatrix}
> \sim
> \begin{bmatrix} 3 & 0 & -6 & 9 & 0 & -72 \\ 0 & 1 & -2 & 2 & 0 & -7 \\ 0 & 0 & 0 & 0 & 1 & 4 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & -2 & 3 & 0 & -24 \\ 0 & 1 & -2 & 2 & 0 & -7 \\ 0 & 0 & 0 & 0 & 1 & 4 \end{bmatrix} .
> $$
>
> This is the reduced echelon form of the original matrix.
>
> **As a linear system** (Lay's Example 5). Read the original matrix as the augmented matrix of
>
> $$
> \begin{aligned}
> 3x_2 - 6x_3 + 6x_4 + 4x_5 &= -5 \\
> 3x_1 - 7x_2 + 8x_3 - 5x_4 + 8x_5 &= 9 \\
> 3x_1 - 9x_2 + 12x_3 - 9x_4 + 6x_5 &= 15 .
> \end{aligned}
> $$
>
> Already the echelon form answers both fundamental questions. There is no row $[\,0\ \cdots\ 0\ \ b\,]$ with $b \ne 0$, so the system is consistent (Theorem §2.3 below). The basic variables are $x_1, x_2, x_5$ and $x_3, x_4$ are free, so the solution is not unique: there are infinitely many solutions. The reduced echelon form gives them all:
>
> $$
> x_1 = -24 + 2x_3 - 3x_4, \qquad x_2 = -7 + 2x_3 - 2x_4, \qquad x_3, x_4 \text{ free}, \qquad x_5 = 4 .
> $$
>
> **Check** ($x_3 = x_4 = 0$, so $(-24, -7, 0, 0, 4)$): $3(-7) + 4(4) = -5$; $3(-24) - 7(-7) + 8(4) = -72 + 49 + 32 = 9$; $3(-24) - 9(-7) + 6(4) = -72 + 63 + 24 = 15$.
>
> *Lay: Examples 1.2.3 and 1.2.5*

^ex-2-3

> [!remark]- Remark: Numerical Notes — Partial Pivoting and Operation Counts
> In step 2 a computer program usually selects as pivot the entry of largest absolute value in the column. This **partial pivoting** reduces roundoff errors.
>
> The forward phase takes much longer than the backward phase. Work is measured in **flops** (floating point operations: one $+$, $-$, $\ast$ or $/$ on two real floating point numbers). For an $n \times (n + 1)$ matrix, reduction to echelon form can take $2n^3/3 + n^2/2 - 7n/6$ flops, about $2n^3/3$ when $n$ is moderately large (say $n \ge 30$); the further reduction to reduced echelon form needs at most $n^2$ flops.

^rem-2-2

## Solutions of Linear Systems

Applied to the augmented matrix of a linear system, row reduction describes the solution set explicitly. For example, if the augmented matrix has been reduced to
$$
\begin{bmatrix} 1 & 0 & -5 & 1 \\ 0 & 1 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix},
\qquad\text{the system is}\qquad
\begin{aligned} x_1 - 5x_3 &= 1 \\ x_2 + x_3 &= 4 \\ 0 &= 0 . \end{aligned}
$$

> [!definition] Definition §2.4: Basic Variables and Free Variables
> In a linear system, the variables corresponding to pivot columns of the coefficient matrix are **basic variables** (some texts say *leading variables*). The other variables are **free variables**.
>
> In the system above, $x_1$ and $x_2$ are basic and $x_3$ is free. Solving the reduced equations for the basic variables gives
>
> $$
> x_1 = 1 + 5x_3, \qquad x_2 = 4 - x_3, \qquad x_3 \text{ is free.}
> $$
>
> "$x_3$ is free" means that any value may be chosen for $x_3$; the formulas then determine $x_1$ and $x_2$. For $x_3 = 0$ the solution is $(1, 4, 0)$, for $x_3 = 1$ it is $(6, 3, 1)$. Each choice of $x_3$ gives a different solution, and every solution arises from a choice of $x_3$. This works because the reduced echelon form places each basic variable in one and only one equation.
>
> *Lay: 1.2 (text)*

^def-2-4

> [!definition] Definition §2.5: Parametric Description of a Solution Set
> A description of the solution set in which the free variables act as parameters, such as the formulas above, is a **parametric description** of the solution set, also called the **general solution** of the system. *Solving a system* means finding a parametric description of the solution set or determining that the solution set is empty.
>
> A consistent system with free variables has many parametric descriptions. (Adding $5$ times the second equation above to the first gives $x_1 + 5x_2 = 21$, $x_2 + x_3 = 4$, and $x_2$ could serve as the parameter.) The convention is always to use the free variables as the parameters. An inconsistent system has an empty solution set, even if it has free variables, and so has no parametric description.
>
> *Lay: 1.2 (text)*

^def-2-5

> [!example] Example §2.4: A General Solution
> Find the general solution of the linear system whose augmented matrix has been reduced to
>
> $$
> \begin{bmatrix} 1 & 6 & 2 & -5 & -2 & -4 \\ 0 & 0 & 2 & -8 & -1 & 3 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix} .
> $$
>
> The matrix is in echelon form; complete the reduction before solving. Add $2$ times row 3 to row 1 and row 3 to row 2; scale row 2 by $\tfrac12$; add $-2$ times row 2 to row 1:
>
> $$
> \sim
> \begin{bmatrix} 1 & 6 & 2 & -5 & 0 & 10 \\ 0 & 0 & 2 & -8 & 0 & 10 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 6 & 2 & -5 & 0 & 10 \\ 0 & 0 & 1 & -4 & 0 & 5 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 6 & 0 & 3 & 0 & 0 \\ 0 & 0 & 1 & -4 & 0 & 5 \\ 0 & 0 & 0 & 0 & 1 & 7 \end{bmatrix} .
> $$
>
> There are five variables (six columns). The system is now
>
> $$
> x_1 + 6x_2 + 3x_4 = 0, \qquad x_3 - 4x_4 = 5, \qquad x_5 = 7 .
> $$
>
> The pivot columns are 1, 3 and 5, so $x_1, x_3, x_5$ are basic and $x_2, x_4$ are free. The general solution is
>
> $$
> x_1 = -6x_2 - 3x_4, \qquad x_2 \text{ free}, \qquad x_3 = 5 + 4x_4, \qquad x_4 \text{ free}, \qquad x_5 = 7 .
> $$
>
> The value of $x_5$ is fixed by the third equation.
>
> *Lay: Example 1.2.4*

^ex-2-4

> [!remark]- Remark: Back-Substitution
> A computer solves a system in echelon form, such as
>
> $$
> x_1 - 7x_2 + 2x_3 - 5x_4 + 8x_5 = 10, \qquad x_2 - 3x_3 + 3x_4 + x_5 = -5, \qquad x_4 - x_5 = 4,
> $$
>
> by **back-substitution**: solve the last equation for $x_4$ in terms of $x_5$, substitute into the second and solve for $x_2$, then substitute both into the first and solve for $x_1$ (a small case by hand: [[§1 Systems of Linear Equations#^ex-1-5|Example §1.5]]). The matrix form of the backward phase uses the same number of arithmetic operations, and its discipline makes errors less likely in hand computation. Best strategy by hand: solve from the *reduced* echelon form only.

^rem-2-3

## Existence and Uniqueness Questions

A nonreduced echelon form is a poor tool for solving a system, but it is just right for the two fundamental questions of [[§1 Systems of Linear Equations#^rem-1-2|§1]].

> [!theorem] Theorem §2.3: Existence and Uniqueness Theorem
> A linear system is consistent if and only if the rightmost column of the augmented matrix is *not* a pivot column, that is, if and only if an echelon form of the augmented matrix has *no* row of the form
>
> $$
> [\,0\ \ \cdots\ \ 0\ \ b\,] \qquad \text{with } b \text{ nonzero.}
> $$
>
> If a linear system is consistent, then the solution set contains either (i) a unique solution, when there are no free variables, or (ii) infinitely many solutions, when there is at least one free variable.
>
> *Lay: Theorem 2 (1.2)*

^thm-2-3

> [!proof]+ Proof
> **The two forms of the condition agree.** In an echelon form of the augmented matrix, the pivot positions are the positions of the leading entries (Corollary §2.2). The rightmost column contains a pivot position exactly when some row has its leading entry in the last column, that is, when some row is $[\,0\ \cdots\ 0\ \ b\,]$ with $b \ne 0$.
>
> **Such a row makes the system inconsistent.** It stands for the equation $0x_1 + \cdots + 0x_n = b$, which no list of numbers satisfies. By [[§1 Systems of Linear Equations#^thm-1-2|Theorem §1.2]], the original system has the same (empty) solution set.
>
> **Otherwise the system is consistent.** Suppose there is no such row, and pass to the reduced echelon form (still without such a row). Every nonzero row then has its leading $1$ in a coefficient column, so every nonzero equation contains exactly one basic variable with coefficient $1$, and that basic variable appears in no other equation. Zero rows say $0 = 0$. Choose any values for the free variables (say all $0$) and solve each nonzero equation for its basic variable. This gives a solution of the reduced system, hence of the original one (Theorem §1.2).
>
> **Counting the solutions.** Let the system be consistent, with reduced system as above. Each solution is determined by the values of the free variables, since the equations express every basic variable in terms of them (a basic variable equals a constant when its equation contains no free variable). If there are no free variables, the reduced system reads $x_i = d_i$ for every $i$, and the solution is unique. If $x_j$ is free, then every real value of $x_j$ (with the other free variables, say, $0$) gives a solution, and different values give solutions that differ in the $j$th entry. So there are infinitely many solutions.

^pf-2-3

*Uses:* [[§1 Systems of Linear Equations#^thm-1-2|§1.2]], [[§2 Row Reduction and Echelon Forms#^cor-2-2|§2.2]], [[§2 Row Reduction and Echelon Forms#^def-2-4|Def. §2.4]]

> [!remark]- Connections
> - Axler gets the two counting consequences by dimension, without row reduction: a homogeneous system with more variables than equations has a nonzero solution ([[§8 Null Spaces and Ranges#^ladr-3-26|LADR 3.26]]), and a system with more equations than variables is inconsistent for some right-hand side ([[§8 Null Spaces and Ranges#^ladr-3-28|LADR 3.28]]). In Lay's language both are pivot counts: more columns than rows forces a free variable ([[§7 Linear Independence#^thm-7-6|Theorem §7.6]]), more rows than columns leaves a row without a pivot ([[§4 The Matrix Equation Ax = b#^thm-4-3|Theorem §4.3]]).

> [!theorem] Corollary §2.4: No Solution, One Solution, or Infinitely Many
> A system of linear equations has
> 1. no solution, or
> 2. exactly one solution, or
> 3. infinitely many solutions.
>
> *Lay: 1.1 (text; verified in 1.2)*

^cor-2-4

> [!proof]+ Proof
> If the system is inconsistent, it has no solution. If it is consistent, Theorem §2.3 says that it has exactly one solution (no free variables) or infinitely many (at least one free variable).

^pf-2-4

*Uses:* [[§2 Row Reduction and Echelon Forms#^thm-2-3|§2.3]]

The lecture's shorthand for the count: a consistent system has "$\infty^{k}$" solutions, $k$ the number of free variables, i.e. of nonpivot columns of the coefficient matrix, with $\infty^0 = 1$ ([[§1 Systems of Linear Equations#^rem-1-1|§1, Remark]]). A unique solution shows in the reduced echelon form as an identity block followed by zero rows, with the solution in the last column.

> [!remark] Remark: Method — Using Row Reduction to Solve a Linear System
> 1. Write the augmented matrix of the system.
> 2. Use the row reduction algorithm to obtain an equivalent augmented matrix in echelon form. Decide whether the system is consistent (look for a "bad row" $[\,0\ \cdots\ 0\ \ b\,]$, $b \ne 0$). If there is no solution, stop; otherwise, go on.
> 3. Continue row reduction to obtain the reduced echelon form.
> 4. Write the system of equations corresponding to the matrix obtained in step 3.
> 5. Rewrite each nonzero equation from step 4 so that its one basic variable is expressed in terms of any free variables appearing in the equation.

^rem-2-4

> [!example] Example §2.5: Five Unknowns, Two Free Variables
> Solve
>
> $$
> \begin{aligned}
> 2x_1 + 4x_2 - 2x_3 + 2x_4 + 4x_5 &= 2 \\
> x_1 + 2x_2 - x_3 + 2x_4 \phantom{{}+ 4x_5} &= 4 \\
> 3x_1 + 6x_2 - 2x_3 + x_4 + 9x_5 &= 1 \\
> 5x_1 + 10x_2 - 4x_3 + 5x_4 + 9x_5 &= 9 .
> \end{aligned}
> $$
>
> **Forward phase.** Divide row 1 by $2$, then clear column 1 ($R_2 - R_1$, $R_3 - 3R_1$, $R_4 - 5R_1$):
>
> $$
> \begin{bmatrix} 1 & 2 & -1 & 1 & 2 & 1 \\ 1 & 2 & -1 & 2 & 0 & 4 \\ 3 & 6 & -2 & 1 & 9 & 1 \\ 5 & 10 & -4 & 5 & 9 & 9 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 2 & -1 & 1 & 2 & 1 \\ 0 & 0 & 0 & 1 & -2 & 3 \\ 0 & 0 & 1 & -2 & 3 & -2 \\ 0 & 0 & 1 & 0 & -1 & 4 \end{bmatrix} .
> $$
>
> Column 2 has no pivot (all entries below row 1 are $0$). Swap rows 2 and 3 to get a pivot in column 3, then $R_4 - R_2$ gives $[\,0\ 0\ 0\ 2\ {-4}\ 6\,]$, and $R_4 - 2R_3$ gives a zero row:
>
> $$
> \sim
> \begin{bmatrix} 1 & 2 & -1 & 1 & 2 & 1 \\ 0 & 0 & 1 & -2 & 3 & -2 \\ 0 & 0 & 0 & 1 & -2 & 3 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> This echelon form already answers the questions: no bad row, so the system is consistent; columns 2 and 5 have no pivot, so $x_2$ and $x_5$ are free and there are infinitely many ("$\infty^2$") solutions.
>
> **Backward phase.** $R_2 + 2R_3$ gives $[\,0\ 0\ 1\ 0\ {-1}\ 4\,]$; $R_1 - R_3$ gives $[\,1\ 2\ {-1}\ 0\ 4\ {-2}\,]$; then $R_1 + R_2$:
>
> $$
> \begin{bmatrix} 1 & 2 & 0 & 0 & 3 & 2 \\ 0 & 0 & 1 & 0 & -1 & 4 \\ 0 & 0 & 0 & 1 & -2 & 3 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> **Parametric form.** The pivot variables are $x_1, x_3, x_4$. Set the free variables to parameters, $x_2 = t$, $x_5 = r$ ($t, r$ any numbers), and express the pivot variables through them:
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix}
> = \begin{bmatrix} 2 - 2t - 3r \\ t \\ 4 + r \\ 3 + 2r \\ r \end{bmatrix}
> = \begin{bmatrix} 2 \\ 0 \\ 4 \\ 3 \\ 0 \end{bmatrix}
> + t \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}
> + r \begin{bmatrix} -3 \\ 0 \\ 1 \\ 2 \\ 1 \end{bmatrix} .
> $$
>
> (Vector notation is introduced in [[§3 Vector Equations|§3]]; this is the "parametric vector form" of [[§5 Solution Sets of Linear Systems#^def-5-2|Definition §5.2]].) **Check:** $(2, 0, 4, 3, 0)$ gives $4 - 8 + 6 = 2$, $2 - 4 + 6 = 4$, $6 - 8 + 3 = 1$, $10 - 16 + 15 = 9$; and both direction vectors make every left side $0$ (for instance $(-3, 0, 1, 2, 1)$ in equation 3: $-9 - 2 + 2 + 9 = 0$).
>
> *In the L2 version the first row keeps the right-hand side $2$ after division by $2$ (it should be $1$), so some intermediate matrices there are off; the reduced echelon form and the parametric solution in both lectures are the ones above.*
>
> *Source: 235 lectures L1 and L2*

^ex-2-5
