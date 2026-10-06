---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 5
lay: "1.4"
aliases: ["Lay 1.4"]
tags: [applied-linear-algebra, math235]
---
← [[§4 Vector Equations]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§6 Solution Sets of Linear Systems]] →

*Lay, Section 1.4 · MATH 235 lectures L2, L3.*

A linear combination of vectors is a matrix times a vector: $A\mathbf{x}$ is the combination of the columns of $A$ with the entries of $\mathbf{x}$ as weights. So every linear system can be read in three equivalent ways, as a system of equations, as a vector equation and as a matrix equation $A\mathbf{x} = \mathbf{b}$, and all three are solved by row reducing $[\,A\ \ \mathbf{b}\,]$. The main result says when $A\mathbf{x} = \mathbf{b}$ is solvable for *every* $\mathbf{b}$: exactly when the columns of $A$ span $\mathbb{R}^m$, exactly when $A$ has a pivot in every row. The section ends with the row–vector rule for computing $A\mathbf{x}$ and the two linearity properties of $\mathbf{x} \mapsto A\mathbf{x}$.

## The Product Ax

> [!definition] Definition §5.1: The Product of a Matrix and a Vector
> If $A$ is an $m \times n$ matrix with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n$, and $\mathbf{x}$ is in $\mathbb{R}^n$, then the **product of $A$ and $\mathbf{x}$**, denoted $A\mathbf{x}$, is **the linear combination of the columns of $A$ using the corresponding entries in $\mathbf{x}$ as weights**:
>
> $$
> A\mathbf{x} = [\,\mathbf{a}_1\ \ \mathbf{a}_2\ \ \cdots\ \ \mathbf{a}_n\,]\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n .
> $$
>
> $A\mathbf{x}$ is defined only if the number of columns of $A$ equals the number of entries in $\mathbf{x}$; it is then a vector in $\mathbb{R}^m$.
>
> *Lay: 1.4, Definition*

^def-5-1

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-50|LADR 3.50]] proves this as a property of matrix multiplication (there $A\mathbf{b}$ is defined entrywise, and "combination of the columns" is the theorem). Lay makes the column picture the definition and derives the entrywise rule ([[§5 The Matrix Equation Ax = b#^prop-5-4|Proposition §5.4]]).

> [!definition] Definition §5.2: Matrix Equation
> An equation of the form $A\mathbf{x} = \mathbf{b}$, with $A$ a given $m \times n$ matrix, $\mathbf{b}$ a given vector in $\mathbb{R}^m$ and $\mathbf{x}$ unknown, is a **matrix equation**, as distinguished from a vector equation $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = \mathbf{b}$.
>
> *Lay: 1.4 (text)*

^def-5-2

> [!example] Example §5.1: Products, Two Ways
> **(a)** By the definition,
>
> $$
> \begin{bmatrix} 1 & 2 & -1 \\ 0 & -5 & 3 \end{bmatrix}\begin{bmatrix} 4 \\ 3 \\ 7 \end{bmatrix}
> = 4\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 3\begin{bmatrix} 2 \\ -5 \end{bmatrix} + 7\begin{bmatrix} -1 \\ 3 \end{bmatrix}
> = \begin{bmatrix} 4 \\ 0 \end{bmatrix} + \begin{bmatrix} 6 \\ -15 \end{bmatrix} + \begin{bmatrix} -7 \\ 21 \end{bmatrix}
> = \begin{bmatrix} 3 \\ 6 \end{bmatrix} .
> $$
>
> By the row–vector rule ([[§5 The Matrix Equation Ax = b#^prop-5-4|Proposition §5.4]] below), each entry is a row of $A$ times $\mathbf{x}$: $1 \cdot 4 + 2 \cdot 3 + (-1) \cdot 7 = 3$ and $0 \cdot 4 + (-5) \cdot 3 + 3 \cdot 7 = 6$.
>
> **(b)**
>
> $$
> \begin{bmatrix} 2 & -3 \\ 8 & 0 \\ -5 & 2 \end{bmatrix}\begin{bmatrix} 4 \\ 7 \end{bmatrix}
> = 4\begin{bmatrix} 2 \\ 8 \\ -5 \end{bmatrix} + 7\begin{bmatrix} -3 \\ 0 \\ 2 \end{bmatrix}
> = \begin{bmatrix} 8 \\ 32 \\ -20 \end{bmatrix} + \begin{bmatrix} -21 \\ 0 \\ 14 \end{bmatrix}
> = \begin{bmatrix} -13 \\ 32 \\ -6 \end{bmatrix} ;
> $$
>
> row by row: $2 \cdot 4 + (-3) \cdot 7 = -13$, $8 \cdot 4 + 0 \cdot 7 = 32$, $(-5) \cdot 4 + 2 \cdot 7 = -6$.
>
> **(c)** Conversely, a linear combination is a matrix times a vector: for $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ in $\mathbb{R}^m$,
>
> $$
> 3\mathbf{v}_1 - 5\mathbf{v}_2 + 7\mathbf{v}_3 = [\,\mathbf{v}_1\ \ \mathbf{v}_2\ \ \mathbf{v}_3\,]\begin{bmatrix} 3 \\ -5 \\ 7 \end{bmatrix} .
> $$
>
> **(d)** The system $x_1 + 2x_2 - x_3 = 4$, $-5x_2 + 3x_3 = 1$ is the vector equation and the matrix equation
>
> $$
> x_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} 2 \\ -5 \end{bmatrix} + x_3\begin{bmatrix} -1 \\ 3 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix},
> \qquad
> \begin{bmatrix} 1 & 2 & -1 \\ 0 & -5 & 3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix} ;
> $$
>
> the matrix is the coefficient matrix of the system.
>
> *Lay: Examples 1.4.1, 1.4.2 and 1.4.5*

^ex-5-1

> [!theorem] Theorem §5.1: Three Views of a Linear System
> If $A$ is an $m \times n$ matrix with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n$, and $\mathbf{b}$ is in $\mathbb{R}^m$, the matrix equation
>
> $$
> A\mathbf{x} = \mathbf{b} \qquad (4)
> $$
>
> has the same solution set as the vector equation
>
> $$
> x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n = \mathbf{b} , \qquad (5)
> $$
>
> which, in turn, has the same solution set as the system of linear equations whose augmented matrix is
>
> $$
> [\,\mathbf{a}_1\ \ \mathbf{a}_2\ \ \cdots\ \ \mathbf{a}_n\ \ \mathbf{b}\,] . \qquad (6)
> $$
>
> *Lay: Theorem 3 (1.4)*

^thm-5-1

> [!proof]+ Proof
> By [[§5 The Matrix Equation Ax = b#^def-5-1|Definition §5.1]], $A\mathbf{x}$ is the vector $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$, so $\mathbf{x}$ satisfies (4) if and only if its entries satisfy (5). By [[§4 Vector Equations#^thm-4-3|Theorem §4.3]], (5) has the same solution set as the system with augmented matrix (6).

^pf-5-1

*Uses:* [[§5 The Matrix Equation Ax = b#^def-5-1|Def. §5.1]], [[§4 Vector Equations#^thm-4-3|§4.3]]

So a linear system can be viewed in three equivalent ways, as a matrix equation, a vector equation or a system of equations, and one may switch between them whenever convenient. All three are solved in the same way, by row reducing the augmented matrix (6).

## Existence of Solutions

> [!theorem] Corollary §5.2: Solvable Means b Is a Combination of the Columns
> The equation $A\mathbf{x} = \mathbf{b}$ has a solution if and only if $\mathbf{b}$ is a linear combination of the columns of $A$, that is, $\mathbf{b} \in \operatorname{Span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\}$.
>
> *Lay: 1.4 (text)*

^cor-5-2

> [!proof]+ Proof
> A solution $\mathbf{x}$ is a list of weights with $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = A\mathbf{x} = \mathbf{b}$ ([[§5 The Matrix Equation Ax = b#^def-5-1|Definition §5.1]]), and such weights exist exactly when $\mathbf{b}$ is in the span ([[§4 Vector Equations#^def-4-4|Definition §4.4]]).

^pf-5-2

*Uses:* [[§5 The Matrix Equation Ax = b#^def-5-1|Def. §5.1]], [[§4 Vector Equations#^def-4-4|Def. §4.4]]

A harder existence question: is $A\mathbf{x} = \mathbf{b}$ consistent for *all* possible $\mathbf{b}$?

> [!example] Example §5.2: For Which b Is Ax = b Consistent?
> Let
>
> $$
> A = \begin{bmatrix} 1 & 3 & 4 \\ -4 & 2 & -6 \\ -3 & -2 & -7 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} .
> $$
>
> Is $A\mathbf{x} = \mathbf{b}$ consistent for all $b_1, b_2, b_3$? Equivalently: when is $\mathbf{b}$ a linear combination of the columns $\mathbf{v}_1 = (1, -4, -3)$, $\mathbf{v}_2 = (3, 2, -2)$, $\mathbf{v}_3 = (4, -6, -7)$? Row reduce the augmented matrix, carrying $b_1, b_2, b_3$ along ($R_2 + 4R_1$, $R_3 + 3R_1$, then $R_3 - \tfrac12 R_2$):
>
> $$
> \begin{bmatrix} 1 & 3 & 4 & b_1 \\ -4 & 2 & -6 & b_2 \\ -3 & -2 & -7 & b_3 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & 4 & b_1 \\ 0 & 14 & 10 & b_2 + 4b_1 \\ 0 & 7 & 5 & b_3 + 3b_1 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & 4 & b_1 \\ 0 & 14 & 10 & b_2 + 4b_1 \\ 0 & 0 & 0 & b_3 + 3b_1 - \tfrac12(b_2 + 4b_1) \end{bmatrix} .
> $$
>
> The last entry is $b_1 - \tfrac12 b_2 + b_3$. The last row is a "bad row" unless this is $0$, so the equation is *not* consistent for every $\mathbf{b}$ (for instance $\mathbf{b} = (1, 0, 0)$ fails). The system is consistent if and only if
>
> $$
> b_1 - \tfrac12 b_2 + b_3 = 0 ,
> $$
>
> the equation of a plane through the origin in $\mathbb{R}^3$ (the lecture, in coordinates $x, y, z$, writes it $x - \tfrac{y}{2} + z = 0$). This plane is $\operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$, the set of all linear combinations of the columns of $A$. **Check:** each column satisfies the equation: $1 + 2 - 3 = 0$, $3 - 1 - 2 = 0$, $4 + 3 - 7 = 0$.
>
> The failure comes from the row of zeros in the echelon form of $A$. If $A$ had a pivot in every row, the augmented column could never produce a row $[\,0\ 0\ 0\ \ 1\,]$.
>
> *Lay: Example 1.4.3*
> *Source: 235 lecture L3*

^ex-5-2

> [!remark] Remark: Two Descriptions of Every Object
> The plane of [[§5 The Matrix Equation Ax = b#^ex-5-2|Example §5.2]] has two descriptions: as a span, $\{c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3\}$ (a *parametric* description), and as the solution set of the equation $b_1 - \tfrac12 b_2 + b_3 = 0$ (a *constraint* description). The lecture's "general principle": every object in linear algebra has both a span-like description and an equation-like description, and row reduction converts one into the other. Here row reducing $[\,A\ \ \mathbf{b}\,]$ turned the span into an equation; solving a system ([[§2 Row Reduction and Echelon Forms|§2]], [[§6 Solution Sets of Linear Systems|§6]]) turns equations into a span.
>
> *Source: 235 lecture L3*

^rem-5-1

> [!definition] Definition §5.3: Spanning ℝᵐ
> A set of vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ in $\mathbb{R}^m$ **spans** (or **generates**) $\mathbb{R}^m$ if every vector in $\mathbb{R}^m$ is a linear combination of $\mathbf{v}_1, \ldots, \mathbf{v}_p$, that is, if $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\} = \mathbb{R}^m$. "The columns of $A$ span $\mathbb{R}^m$" means that every $\mathbf{b}$ in $\mathbb{R}^m$ is a linear combination of the columns of $A$.
>
> *Lay: 1.4 (text)*

^def-5-3

> [!theorem] Theorem §5.3: When Ax = b Is Solvable for Every b
> Let $A$ be an $m \times n$ matrix. Then the following statements are logically equivalent; that is, for a particular $A$, either they are all true or they are all false.
>
> a. For each $\mathbf{b}$ in $\mathbb{R}^m$, the equation $A\mathbf{x} = \mathbf{b}$ has a solution.
>
> b. Each $\mathbf{b}$ in $\mathbb{R}^m$ is a linear combination of the columns of $A$.
>
> c. The columns of $A$ span $\mathbb{R}^m$.
>
> d. $A$ has a pivot position in every row.
>
> *Lay: Theorem 4 (1.4)*

^thm-5-3

> [!proof]+ Proof
> **(a) ⇔ (b) ⇔ (c).** (a) and (b) are equivalent by [[§5 The Matrix Equation Ax = b#^cor-5-2|Corollary §5.2]] applied to each $\mathbf{b}$, and (b) and (c) say the same thing by [[§5 The Matrix Equation Ax = b#^def-5-3|Definition §5.3]]. ("By definition", as the lecture puts it: $\mathbf{b} = a_1\mathbf{v}_1 + \cdots + a_n\mathbf{v}_n$ is the same as $\mathbf{b} = A\mathbf{a}$ with $\mathbf{a} = (a_1, \ldots, a_n)$.) So it suffices to show that (a) and (d) are both true or both false.
>
> Let $U$ be an echelon form of $A$. Given $\mathbf{b}$ in $\mathbb{R}^m$, the row operations that reduce $A$ to $U$ reduce $[\,A\ \ \mathbf{b}\,]$ to $[\,U\ \ \mathbf{d}\,]$ for some $\mathbf{d}$ in $\mathbb{R}^m$:
>
> $$
> [\,A\ \ \mathbf{b}\,] \sim \cdots \sim [\,U\ \ \mathbf{d}\,] .
> $$
>
> **(d) ⇒ (a).** If every row of $U$ contains a pivot position, there can be no pivot in the augmented column ($[\,U\ \ \mathbf{d}\,]$ is already in echelon form, and every row's leading entry lies in $U$). So no row $[\,0\ \cdots\ 0\ \ b\,]$ with $b \ne 0$ occurs, and $A\mathbf{x} = \mathbf{b}$ has a solution by the [[§3 Solutions of Linear Systems#^thm-3-1|Existence and Uniqueness Theorem]], for every $\mathbf{b}$.
>
> **not (d) ⇒ not (a).** If some row of $A$ has no pivot position, then $U$ has fewer than $m$ leading entries; since the nonzero rows of an echelon matrix each have one and come first, the last row of $U$ is all zeros. Let $\mathbf{d}$ be any vector with a $1$ in its last entry. Then $[\,U\ \ \mathbf{d}\,]$ has the bad row $[\,0\ \cdots\ 0\ \ 1\,]$ and represents an inconsistent system. Row operations are reversible ([[§1 Systems of Linear Equations#^prop-1-1|Proposition §1.1]]), so applying the inverse operations, in reverse order, to $[\,U\ \ \mathbf{d}\,]$ gives a matrix of the form $[\,A\ \ \mathbf{b}\,]$ for some $\mathbf{b}$ (the operations turn $U$ back into $A$ and act on the last column in some way). This system $A\mathbf{x} = \mathbf{b}$ is row equivalent to an inconsistent one, hence inconsistent ([[§1 Systems of Linear Equations#^thm-1-2|Theorem §1.2]]), and (a) is false.

^pf-5-3

*Uses:* [[§5 The Matrix Equation Ax = b#^cor-5-2|§5.2]], [[§5 The Matrix Equation Ax = b#^def-5-3|Def. §5.3]], [[§3 Solutions of Linear Systems#^thm-3-1|§3.1]], [[§1 Systems of Linear Equations#^prop-1-1|§1.1]], [[§1 Systems of Linear Equations#^thm-1-2|§1.2]]

> [!remark]- Connections
> - In operator language: the columns of $A$ span $\mathbb{R}^m$ exactly when the map $\mathbf{x} \mapsto A\mathbf{x}$ is onto ([[§10 The Matrix of a Linear Transformation#^thm-10-3|Theorem §10.3]]). A pivot in every row needs at least $m$ columns, so $n < m$ makes (a)–(d) fail; Axler proves this by dimension: [[§8 Null Spaces and Ranges#^ladr-3-24|LADR 3.24]] (no linear map to a higher-dimensional space is surjective), [[§8 Null Spaces and Ranges#^ladr-3-28|LADR 3.28]].

> [!remark] Remark: Warning — Coefficient Matrix, Not Augmented Matrix
> [[§5 The Matrix Equation Ax = b#^thm-5-3|Theorem §5.3]] is about the *coefficient* matrix $A$. If the augmented matrix $[\,A\ \ \mathbf{b}\,]$ has a pivot position in every row, the equation $A\mathbf{x} = \mathbf{b}$ may or may not be consistent: the pivot in the last row may sit in the augmented column. For example, $[\,A\ \ \mathbf{b}\,] = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}$ has a pivot in every row but is inconsistent.

^rem-5-2

## Computation of Ax

> [!theorem] Proposition §5.4: Row–Vector Rule for Computing Ax
> If the product $A\mathbf{x}$ is defined, then the $i$th entry in $A\mathbf{x}$ is the sum of the products of corresponding entries from row $i$ of $A$ and from the vector $\mathbf{x}$:
>
> $$
> (A\mathbf{x})_i = a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n .
> $$
>
> *Lay: 1.4, Row–Vector Rule for Computing Ax*

^prop-5-4

> [!proof]+ Proof
> Lay derives the rule from his Example 4; in general: the $i$th entry of $x_j\mathbf{a}_j$ is $x_ja_{ij}$, and entries of a sum are sums of entries, so the $i$th entry of $A\mathbf{x} = x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$ is $x_1a_{i1} + \cdots + x_na_{in}$. For instance,
>
> $$
> \begin{bmatrix} 2 & 3 & 4 \\ -1 & 5 & -3 \\ 6 & -2 & 8 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
> = x_1\begin{bmatrix} 2 \\ -1 \\ 6 \end{bmatrix} + x_2\begin{bmatrix} 3 \\ 5 \\ -2 \end{bmatrix} + x_3\begin{bmatrix} 4 \\ -3 \\ 8 \end{bmatrix}
> = \begin{bmatrix} 2x_1 + 3x_2 + 4x_3 \\ -x_1 + 5x_2 - 3x_3 \\ 6x_1 - 2x_2 + 8x_3 \end{bmatrix} ,
> $$
>
> and the first entry is row 1, $[\,2\ \ 3\ \ 4\,]$, times $\mathbf{x}$. The sum of products is sometimes called a *dot product* (Chapter 6).

^pf-5-4

*Uses:* [[§5 The Matrix Equation Ax = b#^def-5-1|Def. §5.1]], [[§4 Vector Equations#^def-4-2|Def. §4.2]]

> [!definition] Definition §5.4: Identity Matrix
> The $n \times n$ matrix with $1$'s on the diagonal and $0$'s elsewhere is the **identity matrix**, denoted $I$ or $I_n$. By the row–vector rule, $I_n\mathbf{x} = \mathbf{x}$ for every $\mathbf{x}$ in $\mathbb{R}^n$; for example,
>
> $$
> \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} r \\ s \\ t \end{bmatrix} = \begin{bmatrix} 1 \cdot r + 0 \cdot s + 0 \cdot t \\ 0 \cdot r + 1 \cdot s + 0 \cdot t \\ 0 \cdot r + 0 \cdot s + 1 \cdot t \end{bmatrix} = \begin{bmatrix} r \\ s \\ t \end{bmatrix} .
> $$
>
> *Lay: 1.4 (text); Example 1.4.5(c)*

^def-5-4

> [!remark]- Remark: Numerical Note — Columns or Rows?
> A fast program computes $A\mathbf{x}$ with data stored in contiguous memory. Fortran stores a matrix by columns, so professional Fortran codes compute $A\mathbf{x}$ as a linear combination of the columns ([[§5 The Matrix Equation Ax = b#^def-5-1|Definition §5.1]]); C stores matrices by rows, so there $A\mathbf{x}$ should be computed by the row–vector rule ([[§5 The Matrix Equation Ax = b#^prop-5-4|Proposition §5.4]]).

^rem-5-3

## Properties of the Matrix–Vector Product Ax

> [!theorem] Theorem §5.5: Linearity of the Matrix–Vector Product
> If $A$ is an $m \times n$ matrix, $\mathbf{u}$ and $\mathbf{v}$ are vectors in $\mathbb{R}^n$, and $c$ is a scalar, then:
>
> a. $A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$;
>
> b. $A(c\mathbf{u}) = c(A\mathbf{u})$.
>
> *Lay: Theorem 5 (1.4)*

^thm-5-5

> [!proof]+ Proof
> Let $A = [\,\mathbf{a}_1\ \cdots\ \mathbf{a}_n\,]$ and let $u_i$, $v_i$ be the $i$th entries of $\mathbf{u}$, $\mathbf{v}$. (Lay writes out $n = 3$; the general case is the same.) For (a), compute $A(\mathbf{u} + \mathbf{v})$ as the combination of the columns of $A$ with the entries of $\mathbf{u} + \mathbf{v}$ as weights, and regroup using the algebraic properties of $\mathbb{R}^m$:
>
> $$
> \begin{aligned}
> A(\mathbf{u} + \mathbf{v}) &= (u_1 + v_1)\mathbf{a}_1 + \cdots + (u_n + v_n)\mathbf{a}_n \\
> &= (u_1\mathbf{a}_1 + \cdots + u_n\mathbf{a}_n) + (v_1\mathbf{a}_1 + \cdots + v_n\mathbf{a}_n) = A\mathbf{u} + A\mathbf{v} .
> \end{aligned}
> $$
>
> For (b), the entries of $c\mathbf{u}$ are $cu_i$, so
>
> $$
> A(c\mathbf{u}) = (cu_1)\mathbf{a}_1 + \cdots + (cu_n)\mathbf{a}_n = c(u_1\mathbf{a}_1) + \cdots + c(u_n\mathbf{a}_n) = c(u_1\mathbf{a}_1 + \cdots + u_n\mathbf{a}_n) = c(A\mathbf{u}) .
> $$

^pf-5-5

*Uses:* [[§5 The Matrix Equation Ax = b#^def-5-1|Def. §5.1]], [[§4 Vector Equations#^thm-4-2|§4.2]] (properties (i), (ii), (v), (vi), (vii))

These two properties are what makes $\mathbf{x} \mapsto A\mathbf{x}$ a *linear transformation* ([[§9 Introduction to Linear Transformations#^def-9-4|Definition §9.4]]).

> [!example] Example §5.3: Checking Linearity
> Let $A = \begin{bmatrix} 2 & 5 \\ 3 & 1 \end{bmatrix}$, $\mathbf{u} = \begin{bmatrix} 4 \\ -1 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} -3 \\ 5 \end{bmatrix}$. Verify [[§5 The Matrix Equation Ax = b#^thm-5-5|Theorem §5.5]](a).
>
> $$
> \mathbf{u} + \mathbf{v} = \begin{bmatrix} 1 \\ 4 \end{bmatrix}, \qquad A(\mathbf{u} + \mathbf{v}) = \begin{bmatrix} 2 + 20 \\ 3 + 4 \end{bmatrix} = \begin{bmatrix} 22 \\ 7 \end{bmatrix} ;
> $$
>
> $$
> A\mathbf{u} = \begin{bmatrix} 8 - 5 \\ 12 - 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 11 \end{bmatrix}, \qquad
> A\mathbf{v} = \begin{bmatrix} -6 + 25 \\ -9 + 5 \end{bmatrix} = \begin{bmatrix} 19 \\ -4 \end{bmatrix}, \qquad
> A\mathbf{u} + A\mathbf{v} = \begin{bmatrix} 22 \\ 7 \end{bmatrix} .
> $$
>
> *Lay: 1.4, Practice Problem 2*

^ex-5-3
