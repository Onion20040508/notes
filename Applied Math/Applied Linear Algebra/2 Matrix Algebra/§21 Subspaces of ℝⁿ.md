---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 21
lay: "2.8"
aliases: ["Lay 2.8"]
tags: [applied-linear-algebra, math235]
---
← [[§20 Applications to Computer Graphics]] · ↑ [[· 2 Matrix Algebra]] · [[§22 Dimension and Rank]] →

*Lay, Section 2.8 · MATH 235 lectures L10, L16.*

A subspace of $\mathbb{R}^n$ is a set of vectors closed under addition and scalar multiplication: geometrically, $\{\mathbf{0}\}$, a line or plane through the origin, or a higher-dimensional analogue. Subspaces usually come from a matrix in one of two ways. The column space $\operatorname{Col} A$ is built explicitly as all combinations of the columns of $A$, and it is the set of $\mathbf{b}$ for which $A\mathbf{x} = \mathbf{b}$ is consistent. The null space $\operatorname{Nul} A$ is described implicitly as the solution set of $A\mathbf{x} = \mathbf{0}$. A basis, a linearly independent spanning set, describes a subspace with as few vectors as possible: the parametric vector form of the solutions of $A\mathbf{x} = \mathbf{0}$ gives a basis of $\operatorname{Nul} A$, and the pivot columns of $A$ itself give a basis of $\operatorname{Col} A$. (Lay places 2.8–2.9 here so that a reader can go on to Chapter 5 before Chapter 4, which redoes this material for general vector spaces in [[§29 Vector Spaces and Subspaces|§29]]–[[§34 Rank|§34]].)

## Subspaces

> [!definition] Definition §25.1: Subspace of ℝⁿ
> A **subspace** of $\mathbb{R}^n$ is any set $H$ in $\mathbb{R}^n$ that has three properties:
>
> a. The zero vector is in $H$.
> b. For each $\mathbf{u}$ and $\mathbf{v}$ in $H$, the sum $\mathbf{u} + \mathbf{v}$ is in $H$.
> c. For each $\mathbf{u}$ in $H$ and each scalar $c$, the vector $c\mathbf{u}$ is in $H$.
>
> In words, a subspace is **closed under addition and scalar multiplication**. $\mathbb{R}^n$ is a subspace of itself, and the set $\{\mathbf{0}\}$ consisting of the zero vector alone is a subspace, the **zero subspace**.
>
> *Lay: 2.8, Definition*

^def-21-1

> [!remark]- Connections
> - Rigorous treatment: subspaces of an arbitrary vector space, with the same three conditions, [[§3 Subspaces#^ladr-1-34|LADR 1.34]]; here in [[§29 Vector Spaces and Subspaces#^def-29-2|Definition §29.2]]. Over a general field the sum and scalar multiple are those of the ambient space; nothing changes in the proofs below.

> [!theorem] Proposition §25.1: A Span Is a Subspace
> For $\mathbf{v}_1, \ldots, \mathbf{v}_p$ in $\mathbb{R}^n$, the set $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ of all linear combinations of $\mathbf{v}_1, \ldots, \mathbf{v}_p$ is a subspace of $\mathbb{R}^n$, called the **subspace spanned** (or **generated**) by $\mathbf{v}_1, \ldots, \mathbf{v}_p$.
>
> *Lay: Examples 2.8.1 and 2.8.3*

^prop-21-1

> [!proof]+ Proof
> Let $H = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$. The zero vector is in $H$, because $\mathbf{0} = 0\mathbf{v}_1 + \cdots + 0\mathbf{v}_p$. Take two vectors in $H$, $\mathbf{u} = s_1\mathbf{v}_1 + \cdots + s_p\mathbf{v}_p$ and $\mathbf{v} = t_1\mathbf{v}_1 + \cdots + t_p\mathbf{v}_p$. Then
>
> $$
> \mathbf{u} + \mathbf{v} = (s_1 + t_1)\mathbf{v}_1 + \cdots + (s_p + t_p)\mathbf{v}_p
> $$
>
> is a linear combination of $\mathbf{v}_1, \ldots, \mathbf{v}_p$, hence in $H$, and for any scalar $c$, $c\mathbf{u} = (cs_1)\mathbf{v}_1 + \cdots + (cs_p)\mathbf{v}_p$ is in $H$.

^pf-21-1

*Uses:* [[§21 Subspaces of ℝⁿ#^def-21-1|Def. §21.1]], [[§4 Vector Equations#^def-4-4|Def. §4.4]]

For two vectors, $\operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ is the standard picture of a subspace: a plane through the origin. If $\mathbf{v}_1 \ne \mathbf{0}$ and $\mathbf{v}_2$ is a multiple of $\mathbf{v}_1$, they span only a line through the origin, which is also a subspace.

> [!example] Example §25.1: All Subspaces of ℝ, ℝ² and ℝ³
> **$\mathbb{R}$.** $\{0\}$ and $\mathbb{R}$ are subspaces, and there are no others: if a subspace $V$ of $\mathbb{R}$ contains some $a \ne 0$, then it contains $ca$ for every $c$, which is every real number.
>
> **$\mathbb{R}^2$.** Let $V$ be a subspace of $\mathbb{R}^2$.
> 1. $V = \{\mathbf{0}\}$ is possible.
> 2. If $V$ contains a vector $\mathbf{v} = (a, b) \ne \mathbf{0}$, it contains $c\mathbf{v}$ for all $c$: the whole line through $\mathbf{v}$ and the origin. If there is nothing else, $V$ is that line. For instance the vectors proportional to $(1, 2)$, the vectors $(a, 2a)$, form a subspace: $(a, 2a) + (b, 2b) = (a + b, 2(a + b))$ and $c(a, 2a) = (ca, 2(ca))$.
> 3. If $V$ contains two vectors $\mathbf{u}$, $\mathbf{v}$ that are not proportional, it contains all of their linear combinations, and these fill the whole plane (the lines parallel to $\mathbf{v}$ through the multiples of $\mathbf{u}$ cover $\mathbb{R}^2$). So $V = \mathbb{R}^2$.
>
> So the subspaces of $\mathbb{R}^2$ are $\{\mathbf{0}\}$, the lines through the origin, and $\mathbb{R}^2$. Each is a null space: $\{\mathbf{0}\} = \operatorname{Nul}\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, the line through $(a, b) \ne \mathbf{0}$ is $\operatorname{Nul}\begin{bmatrix} b & -a \end{bmatrix}$ (since $b(ca) - a(cb) = 0$, and conversely $bx - ay = 0$ forces $(x, y)$ to be a multiple of $(a, b)$), and $\mathbb{R}^2 = \operatorname{Nul}\begin{bmatrix} 0 & 0 \end{bmatrix}$.
>
> **$\mathbb{R}^3$.** The same reasoning gives: $\{\mathbf{0}\}$; lines through the origin (all vectors of $V$ proportional to one fixed vector); planes through the origin (if $V$ contains two non-proportional vectors $\mathbf{u}$, $\mathbf{v}$, it contains the plane they span, and if nothing else, it is that plane); and $\mathbb{R}^3$ (if $V$ contains three vectors not in one plane through the origin). In general the subspaces of $\mathbb{R}^n$ are the "flat" copies of $\mathbb{R}^0, \mathbb{R}^1, \ldots, \mathbb{R}^n$ passing through the origin; [[§22 Dimension and Rank#^rem-22-1|§22, Remark: A Subspace with a Basis of p Vectors Looks Like ℝᵖ]] makes "copy of $\mathbb{R}^k$" precise.
>
> *Source: 235 lecture L10*

^ex-21-1

> [!example] Example §25.2: Sets That Are Not Subspaces
> **(a)** A line $L$ *not* through the origin is not a subspace: it does not contain $\mathbf{0}$. It also fails closure: for $\mathbf{u}$, $\mathbf{v}$ on $L$, $\mathbf{u} + \mathbf{v}$ is not on $L$, and for $\mathbf{w}$ on $L$, $2\mathbf{w}$ is not on $L$.
>
> **(b)** The first quadrant $V = \{(x, y) : x \ge 0,\ y \ge 0\}$ contains $\mathbf{0}$ and is closed under addition (sums of nonnegative numbers are nonnegative), but not under scalar multiplication: for $\mathbf{v} = (1, 1)$ in $V$, $-\mathbf{v} = (-1, -1)$ is not in $V$. ($c\mathbf{v}$ stays in $V$ only for $c \ge 0$.)
>
> **(c)** The union of the two axes, $V = \{(x, y) : xy = 0\}$, contains $\mathbf{0}$ and is closed under scalar multiplication (a multiple of a vector on an axis stays on that axis), but not under addition: $(2, 0)$ and $(0, 3)$ are in $V$, but $(2, 0) + (0, 3) = (2, 3)$ is not, since $2 \cdot 3 \ne 0$.
>
> **(d)** The parabola $V = \{(x, y) : y^2 = x\}$ is not a subspace: $(1, 1)$ is in $V$ but $2(1, 1) = (2, 2)$ is not ($4 \ne 2$).
>
> The lecture's moral: subspaces of $\mathbb{R}^n$ are defined by *linear* conditions. Inequalities or nonlinear equations in the description of a set are a reason to suspect it is not a subspace. A subspace must contain $\mathbf{0}$, the whole line through the origin and any one of its nonzero vectors, and every diagonal of a parallelogram with two sides in it.
>
> *Lay: Example 2.8.2*
> *Source: 235 lecture L10*

^ex-21-2

![[m235-18-1.svg]]
*[[§21 Subspaces of ℝⁿ#^ex-21-2|Example §21.2]]. (a) A line $L$ not through $\mathbf{0}$: the sum $\mathbf{u} + \mathbf{v}$ of two of its vectors leaves it. (b) The first quadrant: $\mathbf{v}$ is in it but $-\mathbf{v}$ is not. (c) The two axes: $(2, 0)$ and $(0, 3)$ are in it but their sum, the diagonal of the parallelogram they span, is not.*

## Column Space and Null Space of a Matrix

> [!definition] Definition §21.2: Column Space
> The **column space** of a matrix $A$ is the set $\operatorname{Col} A$ of all linear combinations of the columns of $A$. If $A = [\,\mathbf{a}_1 \ \cdots \ \mathbf{a}_n\,]$ with columns in $\mathbb{R}^m$, then
>
> $$
> \operatorname{Col} A = \operatorname{Span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\} = \{A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\} .
> $$
>
> By [[§21 Subspaces of ℝⁿ#^prop-21-1|Proposition §21.1]], **the column space of an $m \times n$ matrix is a subspace of $\mathbb{R}^m$**. $\operatorname{Col} A = \mathbb{R}^m$ exactly when the columns of $A$ span $\mathbb{R}^m$; otherwise $\operatorname{Col} A$ is only part of $\mathbb{R}^m$.
>
> *Lay: 2.8, Definition*
> *Source: 235 lecture L10*

^def-21-2

> [!example] Example §25.3: Is b in the Column Space?
> Let $A = \begin{bmatrix} 1 & -3 & -4 \\ -4 & 6 & -2 \\ -3 & 7 & 6 \end{bmatrix}$ and $\mathbf{b} = \begin{bmatrix} 3 \\ 3 \\ -4 \end{bmatrix}$. Determine whether $\mathbf{b}$ is in $\operatorname{Col} A$.
>
> $\mathbf{b}$ is a linear combination of the columns of $A$ if and only if $\mathbf{b} = A\mathbf{x}$ for some $\mathbf{x}$, that is, if and only if $A\mathbf{x} = \mathbf{b}$ has a solution. Row reduce $[\,A \ \ \mathbf{b}\,]$:
>
> $$
> \begin{bmatrix} 1 & -3 & -4 & 3 \\ -4 & 6 & -2 & 3 \\ -3 & 7 & 6 & -4 \end{bmatrix}
> \xrightarrow[R_3 + 3R_1]{R_2 + 4R_1}
> \begin{bmatrix} 1 & -3 & -4 & 3 \\ 0 & -6 & -18 & 15 \\ 0 & -2 & -6 & 5 \end{bmatrix}
> \xrightarrow{R_3 - \frac13 R_2}
> \begin{bmatrix} 1 & -3 & -4 & 3 \\ 0 & -6 & -18 & 15 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The last column is not a pivot column, so $A\mathbf{x} = \mathbf{b}$ is consistent and $\mathbf{b}$ is in $\operatorname{Col} A$. Here $\operatorname{Col} A$ is a plane through the origin in $\mathbb{R}^3$ (only two pivots), and $\mathbf{b}$ happens to lie in it.
>
> In general, when a system is written as $A\mathbf{x} = \mathbf{b}$, **$\operatorname{Col} A$ is the set of all $\mathbf{b}$ for which the system has a solution**.
>
> *Lay: Example 2.8.4*

^ex-21-3

> [!definition] Definition §21.3: Null Space
> The **null space** of a matrix $A$ is the set $\operatorname{Nul} A$ of all solutions of the homogeneous equation $A\mathbf{x} = \mathbf{0}$. When $A$ has $n$ columns, $\operatorname{Nul} A$ is a subset of $\mathbb{R}^n$.
>
> *Lay: 2.8, Definition*

^def-21-3

> [!theorem] Theorem §25.2: The Null Space Is a Subspace
> The null space of an $m \times n$ matrix $A$ is a subspace of $\mathbb{R}^n$. Equivalently, the set of all solutions of a system $A\mathbf{x} = \mathbf{0}$ of $m$ homogeneous linear equations in $n$ unknowns is a subspace of $\mathbb{R}^n$.
>
> *Lay: Theorem 12 (2.8)*

^thm-21-2

> [!proof]+ Proof
> The zero vector is in $\operatorname{Nul} A$, because $A\mathbf{0} = \mathbf{0}$. Let $\mathbf{u}$ and $\mathbf{v}$ be in $\operatorname{Nul} A$, so $A\mathbf{u} = \mathbf{0}$ and $A\mathbf{v} = \mathbf{0}$. By the linearity of matrix multiplication ([[§5 The Matrix Equation Ax = b#^thm-5-5|Theorem §5.5]]),
>
> $$
> A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v} = \mathbf{0} + \mathbf{0} = \mathbf{0},
> $$
>
> so $\mathbf{u} + \mathbf{v}$ is in $\operatorname{Nul} A$. Also, for any scalar $c$, $A(c\mathbf{u}) = c(A\mathbf{u}) = c\mathbf{0} = \mathbf{0}$, so $c\mathbf{u}$ is in $\operatorname{Nul} A$.

^pf-21-2

*Uses:* [[§21 Subspaces of ℝⁿ#^def-21-1|Def. §21.1]], [[§5 The Matrix Equation Ax = b#^thm-5-5|§5.5]]

> [!remark]- Connections
> - Rigorous treatment: for a linear map $T : V \to W$, $\operatorname{null} T$ is a subspace of $V$ and $\operatorname{range} T$ a subspace of $W$, [[§8 Null Spaces and Ranges#^ladr-3-13|LADR 3.13]] and [[§8 Null Spaces and Ranges#^ladr-3-18|LADR 3.18]]; for $T(\mathbf{x}) = A\mathbf{x}$ these are $\operatorname{Nul} A$ and $\operatorname{Col} A$ (kernel and range, [[§30 Null Spaces, Column Spaces, and Linear Transformations#^def-30-5|Definition §30.5]], [[§30 Null Spaces, Column Spaces, and Linear Transformations#^def-30-6|Definition §30.6]]).

> [!remark] Remark: Implicit and Explicit Descriptions
> To test whether a given $\mathbf{v}$ is in $\operatorname{Nul} A$, just compute $A\mathbf{v}$. Because $\operatorname{Nul} A$ is described by a condition that must be checked for each vector, it is defined **implicitly**. The column space is defined **explicitly**: its vectors are constructed, as linear combinations of the columns. To get an explicit description of $\operatorname{Nul} A$, solve $A\mathbf{x} = \mathbf{0}$ and write the solution in parametric vector form ([[§21 Subspaces of ℝⁿ#^ex-21-4|Example §21.4]]). The lecture adds that *every* subspace of $\mathbb{R}^n$ arises both ways: it is $\operatorname{Nul} A$ for some $A$ and $\operatorname{Col} B$ for some $B$. (A subspace $H$ of $\mathbb{R}^n$ has a finite basis, [[§33 The Dimension of a Vector Space#^thm-33-3|Theorem §33.3]]; take $B$ with these basis vectors as columns. For $A$, take a matrix whose rows span the orthogonal complement $H^\perp$: then $\operatorname{Nul} A = (\operatorname{Row} A)^\perp = (H^\perp)^\perp = H$ by [[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]] and [[§50 Orthogonal Complements and Angles#^cor-50-4|Corollary §50.4]].) Natural questions are then how to describe $\operatorname{Nul} A$ as some $\operatorname{Col} B$, and how to tell whether $\operatorname{Nul} A = \operatorname{Nul} B$; bases answer both.
>
> *Source: 235 lecture L10*

^rem-21-1

## Basis for a Subspace

A subspace typically contains infinitely many vectors, so problems about it are best handled with a small finite set of vectors that span it. The smaller the set, the better, and a smallest spanning set must be linearly independent (a dependent spanning set contains a redundant vector, which can be dropped without changing the span, [[§8 Linear Independence#^prop-8-5|Proposition §8.5]]).

> [!definition] Definition §21.4: Basis
> A **basis** for a subspace $H$ of $\mathbb{R}^n$ is a linearly independent set in $H$ that spans $H$.
>
> For example, the columns of an invertible $n \times n$ matrix form a basis for $\mathbb{R}^n$, because they are linearly independent and span $\mathbb{R}^n$ by the Invertible Matrix Theorem ([[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]], (e) and (h)). The columns $\mathbf{e}_1, \ldots, \mathbf{e}_n$ of $I_n$ form the **standard basis** for $\mathbb{R}^n$.
>
> *Lay: 2.8, Definition; Example 2.8.5*
> *Source: 235 lecture L10*

^def-21-4

> [!remark]- Connections
> - Rigorous treatment: [[§5 Bases#^ladr-2-26|LADR 2.26]] (basis of any vector space) and [[§5 Bases#^ladr-2-28|LADR 2.28]] (every vector is a unique combination of the basis, the property used for coordinates in [[§22 Dimension and Rank#^prop-22-1|Proposition §22.1]]); here in general vector spaces, [[§31 Linearly Independent Sets; Bases#^def-31-2|Definition §31.2]].

> [!example] Example §26.1: A Basis for a Null Space
> Find a basis for the null space of
>
> $$
> A = \begin{bmatrix} -3 & 6 & -1 & 1 & -7 \\ 1 & -2 & 2 & 3 & -1 \\ 2 & -4 & 5 & 8 & -4 \end{bmatrix} .
> $$
>
> First write the solution of $A\mathbf{x} = \mathbf{0}$ in parametric vector form. Row reduce (interchange $R_1$, $R_2$; then $R_2 + 3R_1$, $R_3 - 2R_1$; then $R_2 \div 5$, $R_3 - R_2$, $R_1 - 2R_2$):
>
> $$
> [\,A \ \ \mathbf{0}\,] \sim \begin{bmatrix} 1 & -2 & 0 & -1 & 3 & 0 \\ 0 & 0 & 1 & 2 & -2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix},
> \qquad
> \begin{aligned} x_1 - 2x_2 - x_4 + 3x_5 &= 0 \\ x_3 + 2x_4 - 2x_5 &= 0 \end{aligned}
> $$
>
> The general solution is $x_1 = 2x_2 + x_4 - 3x_5$, $x_3 = -2x_4 + 2x_5$, with $x_2$, $x_4$, $x_5$ free:
>
> $$
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix} = \begin{bmatrix} 2x_2 + x_4 - 3x_5 \\ x_2 \\ -2x_4 + 2x_5 \\ x_4 \\ x_5 \end{bmatrix}
> = x_2\underbrace{\begin{bmatrix} 2 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}}_{\mathbf{u}} + x_4\underbrace{\begin{bmatrix} 1 \\ 0 \\ -2 \\ 1 \\ 0 \end{bmatrix}}_{\mathbf{v}} + x_5\underbrace{\begin{bmatrix} -3 \\ 0 \\ 2 \\ 0 \\ 1 \end{bmatrix}}_{\mathbf{w}} = x_2\mathbf{u} + x_4\mathbf{v} + x_5\mathbf{w} . \tag{1}
> $$
>
> Equation (1) shows that $\operatorname{Nul} A$ is the set of all linear combinations of $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$: these vectors span $\operatorname{Nul} A$. The construction makes them automatically linearly independent: by (1), $\mathbf{0} = x_2\mathbf{u} + x_4\mathbf{v} + x_5\mathbf{w}$ only if the weights $x_2$, $x_4$, $x_5$ are all zero (look at entries 2, 4 and 5, where exactly one of the vectors is nonzero, equal to 1). So $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is a basis for $\operatorname{Nul} A$, with one vector for each free variable.
>
> *Lay: Example 2.8.6*

^ex-21-4

> [!example] Example §26.2: A Basis for a Column Space
> **(a) An echelon matrix.** Find a basis for $\operatorname{Col} B$, where
>
> $$
> B = [\,\mathbf{b}_1 \ \cdots \ \mathbf{b}_5\,] = \begin{bmatrix} 1 & 0 & -3 & 5 & 0 \\ 0 & 1 & 2 & -1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The nonpivot columns are combinations of the pivot columns: $\mathbf{b}_3 = -3\mathbf{b}_1 + 2\mathbf{b}_2$ and $\mathbf{b}_4 = 5\mathbf{b}_1 - \mathbf{b}_2$. So any combination of $\mathbf{b}_1, \ldots, \mathbf{b}_5$ is actually a combination of $\mathbf{b}_1$, $\mathbf{b}_2$, $\mathbf{b}_5$: if $\mathbf{v} = c_1\mathbf{b}_1 + \cdots + c_5\mathbf{b}_5$, then
>
> $$
> \mathbf{v} = c_1\mathbf{b}_1 + c_2\mathbf{b}_2 + c_3(-3\mathbf{b}_1 + 2\mathbf{b}_2) + c_4(5\mathbf{b}_1 - \mathbf{b}_2) + c_5\mathbf{b}_5 .
> $$
>
> So $\{\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_5\}$ spans $\operatorname{Col} B$. These vectors are linearly independent, because they are columns of an identity matrix ($\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ of $\mathbb{R}^4$). So the pivot columns of $B$ form a basis for $\operatorname{Col} B$.
>
> **(b) A general matrix.** It can be verified that
>
> $$
> A = [\,\mathbf{a}_1 \ \cdots \ \mathbf{a}_5\,] = \begin{bmatrix} 1 & 3 & 3 & 2 & -9 \\ -2 & -2 & 2 & -8 & 2 \\ 2 & 3 & 0 & 7 & 1 \\ 3 & 4 & -1 & 11 & -8 \end{bmatrix}
> $$
>
> is row equivalent to $B$. Find a basis for $\operatorname{Col} A$.
>
> The pivot columns of $A$ are columns 1, 2 and 5. Since $A\mathbf{x} = \mathbf{0}$ and $B\mathbf{x} = \mathbf{0}$ have the same solutions, the columns of $A$ satisfy exactly the same linear dependence relations as the columns of $B$:
>
> $$
> \mathbf{a}_3 = -3\mathbf{a}_1 + 2\mathbf{a}_2 \qquad\text{and}\qquad \mathbf{a}_4 = 5\mathbf{a}_1 - \mathbf{a}_2 .
> $$
>
> (Check the first: $-3(1, -2, 2, 3) + 2(3, -2, 3, 4) = (3, 2, 0, -1) = \mathbf{a}_3$; the second: $5(1, -2, 2, 3) - (3, -2, 3, 4) = (2, -8, 7, 11) = \mathbf{a}_4$.) As in (a), $\mathbf{a}_3$ and $\mathbf{a}_4$ are not needed to span $\operatorname{Col} A$. And $\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_5\}$ is linearly independent, because any dependence relation among $\mathbf{a}_1$, $\mathbf{a}_2$, $\mathbf{a}_5$ would be the same relation among $\mathbf{b}_1$, $\mathbf{b}_2$, $\mathbf{b}_5$. So $\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_5\}$ is a basis for $\operatorname{Col} A$.
>
> **Warning.** The columns of $B$ are not a basis of $\operatorname{Col} A$: they all have last entry $0$, so they cannot even generate the columns of $A$.
>
> *Lay: Examples 2.8.7 and 2.8.8*

^ex-21-5

> [!theorem] Theorem §25.3: Pivot Columns Form a Basis for Col A
> The pivot columns of a matrix $A$ form a basis for the column space of $A$.
>
> *Lay: Theorem 13 (2.8)*

^thm-21-3

> [!proof]+ Proof
> (Lay: "The argument in Example 8 can be adapted to prove the theorem." Here is the adaptation; Lay writes it out for general vector spaces in 4.3, [[§31 Linearly Independent Sets; Bases#^thm-31-3|Theorem §31.3]].) Let $B$ be the reduced echelon form of $A$, with pivots in columns $p_1 < \cdots < p_r$.
>
> **The columns of $A$ and of $B$ satisfy the same dependence relations.** Row operations do not change the solution set of a homogeneous system, so for every $\mathbf{x}$, $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = \mathbf{0}$ if and only if $x_1\mathbf{b}_1 + \cdots + x_n\mathbf{b}_n = \mathbf{0}$.
>
> **In $B$.** The pivot columns of $B$ are $\mathbf{e}_1, \ldots, \mathbf{e}_r$, which are linearly independent. Every row of $B$ below row $r$ is zero, so every column of $B$ is a combination of $\mathbf{e}_1, \ldots, \mathbf{e}_r$: a nonpivot column $\mathbf{b}_k$ equals $b_{1k}\mathbf{b}_{p_1} + \cdots + b_{rk}\mathbf{b}_{p_r}$.
>
> **Transfer to $A$.** The relation $\mathbf{b}_k - (b_{1k}\mathbf{b}_{p_1} + \cdots + b_{rk}\mathbf{b}_{p_r}) = \mathbf{0}$ gives the same relation $\mathbf{a}_k = b_{1k}\mathbf{a}_{p_1} + \cdots + b_{rk}\mathbf{a}_{p_r}$, so each nonpivot column of $A$ is a combination of the pivot columns of $A$. Hence any combination of all the columns of $A$ can be rewritten as a combination of the pivot columns alone (as in [[§21 Subspaces of ℝⁿ#^ex-21-5|Example §21.5]](a)): the pivot columns span $\operatorname{Col} A$. Finally, a dependence relation $c_1\mathbf{a}_{p_1} + \cdots + c_r\mathbf{a}_{p_r} = \mathbf{0}$ would give $c_1\mathbf{b}_{p_1} + \cdots + c_r\mathbf{b}_{p_r} = \mathbf{0}$, so all $c_i = 0$: the pivot columns of $A$ are linearly independent. They form a basis for $\operatorname{Col} A$.

^pf-21-3

*Uses:* [[§21 Subspaces of ℝⁿ#^def-21-4|Def. §21.4]], [[§21 Subspaces of ℝⁿ#^def-21-2|Def. §21.2]], [[§2 Row Reduction and Echelon Forms#^def-2-1|Def. §2.1]], [[§2 Row Reduction and Echelon Forms#^def-2-3|Def. §2.3]], [[§1 Systems of Linear Equations#^thm-1-2|§1.2]], [[§8 Linear Independence#^def-8-1|Def. §8.1]]

> [!remark] Remark: Method — Bases for Nul A and Col A
> **Nul A.** Row reduce $[\,A \ \ \mathbf{0}\,]$ to reduced echelon form, solve for the basic variables in terms of the free variables, and write the general solution in parametric vector form $\mathbf{x} = x_{f_1}\mathbf{u}_1 + \cdots + x_{f_k}\mathbf{u}_k$, one vector for each free variable. The vectors $\mathbf{u}_1, \ldots, \mathbf{u}_k$ form a basis for $\operatorname{Nul} A$. (If there are no free variables, $\operatorname{Nul} A = \{\mathbf{0}\}$.)
>
> **Col A.** Row reduce $A$ to an echelon form (any echelon form) to locate the pivot columns. The corresponding columns **of $A$ itself**, not of the echelon form, form a basis for $\operatorname{Col} A$ ([[§21 Subspaces of ℝⁿ#^thm-21-3|Theorem §21.3]]). The columns of an echelon form are often not even in $\operatorname{Col} A$.
>
> *Source: 235 lecture L16*

^rem-21-2
