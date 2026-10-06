---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 22
lay: "2.9"
aliases: ["Lay 2.9"]
tags: [applied-linear-algebra, math235]
---
← [[§21 Subspaces of ℝⁿ]] · ↑ [[· 2 Matrix Algebra]] · [[§23 The Singular Matrix with Rows (1, 2) and (2, 4)]] →

*Lay, Section 2.9 · MATH 235 lecture L16.*

A basis of a subspace $H$ gives every vector of $H$ unique coordinates, so a basis of $p$ vectors makes $H$ look and act like $\mathbb{R}^p$. Every basis of $H$ has the same number of vectors, its dimension. For a matrix, $\dim \operatorname{Nul} A$ is the number of free variables and $\operatorname{rank} A = \dim \operatorname{Col} A$ is the number of pivot columns. Since every column is one or the other, they add up to the number of columns: the Rank Theorem. The Basis Theorem says that in a $p$-dimensional subspace, $p$ independent vectors, or $p$ spanning vectors, are automatically a basis. These ideas add six more statements to the Invertible Matrix Theorem ([[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]]).

## Coordinate Systems

The main reason for choosing a basis of a subspace $H$, rather than merely a spanning set, is that each vector of $H$ can then be written in only one way as a linear combination of the basis vectors.

> [!theorem] Proposition §22.1: Unique Representation in a Basis
> Let $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$ be a basis for a subspace $H$. Then each $\mathbf{x}$ in $H$ can be written in exactly one way as $\mathbf{x} = c_1\mathbf{b}_1 + \cdots + c_p\mathbf{b}_p$.
>
> *Lay: 2.9 (text)*

^prop-22-1

> [!proof]+ Proof
> Such weights exist because $\mathcal{B}$ spans $H$. Suppose $\mathbf{x}$ can be generated in two ways,
>
> $$
> \mathbf{x} = c_1\mathbf{b}_1 + \cdots + c_p\mathbf{b}_p \qquad\text{and}\qquad \mathbf{x} = d_1\mathbf{b}_1 + \cdots + d_p\mathbf{b}_p . \tag{1}
> $$
>
> Subtracting,
>
> $$
> \mathbf{0} = \mathbf{x} - \mathbf{x} = (c_1 - d_1)\mathbf{b}_1 + \cdots + (c_p - d_p)\mathbf{b}_p . \tag{2}
> $$
>
> Since $\mathcal{B}$ is linearly independent, the weights in (2) are all zero: $c_j = d_j$ for $1 \le j \le p$. So the two representations in (1) are the same.

^pf-22-1

*Uses:* [[§21 Subspaces of ℝⁿ#^def-21-4|Def. §21.4]], [[§8 Linear Independence#^def-8-1|Def. §8.1]]

> [!definition] Definition §22.1: Coordinates Relative to a Basis
> Suppose $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$ is a basis for a subspace $H$. For each $\mathbf{x}$ in $H$, the **coordinates of $\mathbf{x}$ relative to the basis $\mathcal{B}$** are the weights $c_1, \ldots, c_p$ such that $\mathbf{x} = c_1\mathbf{b}_1 + \cdots + c_p\mathbf{b}_p$, and the vector in $\mathbb{R}^p$
>
> $$
> [\mathbf{x}]_{\mathcal{B}} = \begin{bmatrix} c_1 \\ \vdots \\ c_p \end{bmatrix}
> $$
>
> is the **coordinate vector of $\mathbf{x}$ (relative to $\mathcal{B}$)**, or the **$\mathcal{B}$-coordinate vector of $\mathbf{x}$**. The elements of $\mathcal{B}$ must be numbered, since the entries of $[\mathbf{x}]_{\mathcal{B}}$ depend on their order.
>
> *Lay: 2.9, Definition*
> *Source: 235 lecture L16*

^def-22-1

> [!example] Example §22.1: Coordinates on a Plane in ℝ³
> Let $\mathbf{v}_1 = \begin{bmatrix} 3 \\ 6 \\ 2 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$, $\mathbf{x} = \begin{bmatrix} 3 \\ 12 \\ 7 \end{bmatrix}$ and $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$. Then $\mathcal{B}$ is a basis for $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$, because $\mathbf{v}_1$ and $\mathbf{v}_2$ are not multiples of each other, hence linearly independent. Determine whether $\mathbf{x}$ is in $H$, and if it is, find $[\mathbf{x}]_{\mathcal{B}}$.
>
> $\mathbf{x}$ is in $H$ exactly when the vector equation
>
> $$
> c_1\begin{bmatrix} 3 \\ 6 \\ 2 \end{bmatrix} + c_2\begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 12 \\ 7 \end{bmatrix}
> $$
>
> is consistent, and then $c_1$, $c_2$ are the $\mathcal{B}$-coordinates. The second entries give $6c_1 = 12$, so $c_1 = 2$; the first entries give $3(2) - c_2 = 3$, so $c_2 = 3$; and the third entries check: $2(2) + 3 = 7$. Equivalently,
>
> $$
> \begin{bmatrix} 3 & -1 & 3 \\ 6 & 0 & 12 \\ 2 & 1 & 7 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So $\mathbf{x} = 2\mathbf{v}_1 + 3\mathbf{v}_2$ is in $H$ and $[\mathbf{x}]_{\mathcal{B}} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$. The basis $\mathcal{B}$ determines a "coordinate system" on $H$, visualized by the grid in the figure below.
>
> *Lay: Example 2.9.1*

^ex-22-1

![[m235-19-1.svg]]
*[[§22 Dimension and Rank#^ex-22-1|Example §22.1]]. The plane $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ in $\mathbb{R}^3$ with the grid of the coordinate system defined by $\mathcal{B}$: grid lines are $c_1 = \text{const}$ and $c_2 = \text{const}$. The point $\mathbf{x} = 2\mathbf{v}_1 + 3\mathbf{v}_2$ has $\mathcal{B}$-coordinates $(2, 3)$, although as a vector of $\mathbb{R}^3$ it is $(3, 12, 7)$.*

*Chain: the same computation later in [[§32 Coordinate Systems#^ex-32-5|Chapter 4]], part (a)*

> [!remark] Remark: A Subspace with a Basis of p Vectors Looks Like ℝᵖ
> Although the points of $H$ in [[§22 Dimension and Rank#^ex-22-1|Example §22.1]] are in $\mathbb{R}^3$, they are completely determined by their coordinate vectors, which belong to $\mathbb{R}^2$; the grid makes $H$ "look" like $\mathbb{R}^2$. The correspondence $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal{B}}$ is a one-to-one correspondence between $H$ and $\mathbb{R}^2$ that preserves linear combinations. Such a correspondence is called an **isomorphism**, and $H$ is **isomorphic** to $\mathbb{R}^2$. In general, if $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$ is a basis for $H$, then $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal{B}}$ makes $H$ look and act like $\mathbb{R}^p$, even though the vectors of $H$ may have more than $p$ entries. Details in [[§32 Coordinate Systems#^thm-32-3|Theorem §32.3]]; rigorously, [[§10 Invertibility and Isomorphisms#^ladr-3-69|LADR 3.69]] and [[§10 Invertibility and Isomorphisms#^ladr-3-70|LADR 3.70]] (hub [[Dimension shows whether vector spaces are isomorphic]]).

^rem-22-1

## The Dimension of a Subspace

If a subspace $H$ has a basis of $p$ vectors, then every basis of $H$ consists of exactly $p$ vectors. Lay leaves this to Exercises 27–28 here and proves it for general vector spaces in 4.5 ([[§33 The Dimension of a Vector Space#^thm-33-2|Theorem §33.2]]; rigorously [[§6 Dimension#^ladr-2-34|LADR 2.34]]). So the following definition makes sense.

> [!definition] Definition §22.2: Dimension
> The **dimension** of a nonzero subspace $H$, denoted $\dim H$, is the number of vectors in any basis for $H$. The dimension of the zero subspace $\{\mathbf{0}\}$ is defined to be zero. (The zero subspace has *no* basis, because the zero vector by itself forms a linearly dependent set.)
>
> $\mathbb{R}^n$ has dimension $n$: every basis of $\mathbb{R}^n$ consists of $n$ vectors. A plane through $\mathbf{0}$ in $\mathbb{R}^3$ is two-dimensional, and a line through $\mathbf{0}$ is one-dimensional.
>
> *Lay: 2.9, Definition*
> *Source: 235 lecture L16*

^def-22-2

> [!remark]- Connections
> - Rigorous treatment: [[§6 Dimension#^ladr-2-35|LADR 2.35]] (dimension of a finite-dimensional vector space), well defined by [[§6 Dimension#^ladr-2-34|LADR 2.34]] (basis length does not depend on the basis), which rests on [[§4 Span and Linear Independence#^ladr-2-22|LADR 2.22]] (an independent list is never longer than a spanning list).

By [[§21 Subspaces of ℝⁿ#^ex-21-4|Example §21.4]], the parametric vector form of the solutions of $A\mathbf{x} = \mathbf{0}$ gives a basis of $\operatorname{Nul} A$ with one vector for each free variable. So **to find $\dim \operatorname{Nul} A$, count the free variables of $A\mathbf{x} = \mathbf{0}$**.

> [!definition] Definition §22.3: Rank
> The **rank** of a matrix $A$, denoted $\operatorname{rank} A$, is the dimension of the column space of $A$. Since the pivot columns of $A$ form a basis for $\operatorname{Col} A$ ([[§21 Subspaces of ℝⁿ#^thm-21-3|Theorem §21.3]]), **the rank of $A$ is the number of pivot columns of $A$**.
>
> *Lay: 2.9, Definition*
> *Source: 235 lecture L16*

^def-22-3

> [!remark]- Connections
> - Rigorous treatment: [[§9 Matrices#^ladr-3-58|LADR 3.58]] (rank of a matrix over $\mathbf{F}$ as its column rank, with no pivots); Axler proves that it also equals the row rank, [[§9 Matrices#^ladr-3-57|LADR 3.57]], which Lay proves in [[§34 Rank#^thm-34-3|Theorem §34.3]].

> [!example] Example §22.2: Rank and the Dimension of the Null Space
> **(a)** The null space of the matrix $A$ of [[§21 Subspaces of ℝⁿ#^ex-21-4|Example §21.4]] has the basis $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$, one vector for each of the free variables $x_2$, $x_4$, $x_5$. So $\dim \operatorname{Nul} A = 3$. Its pivot columns are columns 1 and 3, so $\operatorname{rank} A = 2$.
>
> **(b)** Determine the rank of
>
> $$
> A = \begin{bmatrix} 2 & 5 & -3 & -4 & 8 \\ 4 & 7 & -4 & -3 & 9 \\ 6 & 9 & -5 & 2 & 4 \\ 0 & -9 & 6 & 5 & -6 \end{bmatrix} .
> $$
>
> Reduce $A$ to echelon form:
>
> $$
> A \xrightarrow[R_3 - 3R_1]{R_2 - 2R_1}
> \begin{bmatrix} 2 & 5 & -3 & -4 & 8 \\ 0 & -3 & 2 & 5 & -7 \\ 0 & -6 & 4 & 14 & -20 \\ 0 & -9 & 6 & 5 & -6 \end{bmatrix}
> \xrightarrow[R_4 - 3R_2]{R_3 - 2R_2}
> \begin{bmatrix} 2 & 5 & -3 & -4 & 8 \\ 0 & -3 & 2 & 5 & -7 \\ 0 & 0 & 0 & 4 & -6 \\ 0 & 0 & 0 & -10 & 15 \end{bmatrix}
> \xrightarrow{R_4 + \frac52 R_3}
> \begin{bmatrix} 2 & 5 & -3 & -4 & 8 \\ 0 & -3 & 2 & 5 & -7 \\ 0 & 0 & 0 & 4 & -6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The pivot columns are columns 1, 2 and 4, so $\operatorname{rank} A = 3$. The two nonpivot columns, 3 and 5, correspond to the two free variables of $A\mathbf{x} = \mathbf{0}$, so $\dim \operatorname{Nul} A = 2$.
>
> *Lay: Examples 2.9.2 and 2.9.3*

^ex-22-2

Since the number of pivot columns plus the number of nonpivot columns is exactly the number of columns, the dimensions of $\operatorname{Col} A$ and $\operatorname{Nul} A$ are linked.

> [!theorem] Theorem §22.2: The Rank Theorem
> If a matrix $A$ has $n$ columns, then
>
> $$
> \operatorname{rank} A + \dim \operatorname{Nul} A = n .
> $$
>
> *Lay: Theorem 14 (2.9)*

^thm-22-2

> [!proof]+ Proof
> Reduce $A$ to echelon form. Each of the $n$ columns of $A$ is either a pivot column or a nonpivot column. By [[§22 Dimension and Rank#^def-22-3|Definition §22.3]], $\operatorname{rank} A$ is the number of pivot columns. The nonpivot columns correspond exactly to the free variables of $A\mathbf{x} = \mathbf{0}$, and by [[§21 Subspaces of ℝⁿ#^ex-21-4|Example §21.4]] (one basis vector of $\operatorname{Nul} A$ per free variable) $\dim \operatorname{Nul} A$ is the number of free variables. So
>
> $$
> \operatorname{rank} A + \dim \operatorname{Nul} A = \#\{\text{pivot columns}\} + \#\{\text{nonpivot columns}\} = n .
> $$

^pf-22-2

*Uses:* [[§22 Dimension and Rank#^def-22-3|Def. §22.3]], [[§22 Dimension and Rank#^def-22-2|Def. §22.2]], [[§21 Subspaces of ℝⁿ#^thm-21-3|§21.3]], [[§21 Subspaces of ℝⁿ#^ex-21-4|Ex. §21.4]]

> [!remark]- Connections
> - Rigorous treatment: the fundamental theorem of linear maps, $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$, [[§8 Null Spaces and Ranges#^ladr-3-21|LADR 3.21]] (hub [[Fundamental theorem of linear maps]]), proved by extending a basis of $\operatorname{null} T$ to a basis of $V$ instead of counting pivots; for $T(\mathbf{x}) = A\mathbf{x}$ it is this theorem. Lay's fuller version, with $\dim \operatorname{Row} A = \operatorname{rank} A$, is [[§34 Rank#^thm-34-3|Theorem §34.3]].

> [!remark] Remark: The Rank Theorem Geometrically
> Think of $A$ ($m \times n$) as the map $\mathbf{x} \mapsto A\mathbf{x}$ from $\mathbb{R}^n$ to $\mathbb{R}^m$. It collapses the subspace $\operatorname{Nul} A$ of $\mathbb{R}^n$ to the single point $\mathbf{0}$, and its image is the subspace $\operatorname{Col} A$ of $\mathbb{R}^m$. The Rank Theorem says that the dimensions lost ($\dim \operatorname{Nul} A$) and the dimensions kept ($\dim \operatorname{Col} A$) add up to the dimension $n$ of the domain. For the projection $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} : \mathbb{R}^3 \to \mathbb{R}^2$, $(x, y, z) \mapsto (x, y)$, the null space is the $z$-axis (dimension 1) and the column space is all of $\mathbb{R}^2$ (dimension 2): $1 + 2 = 3$. Each $\mathbf{x} = (x, y, z)$ splits as $(x, y, 0) + (0, 0, z)$. The first part lies in $\operatorname{Row} A$ (the span of the rows of $A$, [[§30 Null Spaces, Column Spaces, and Linear Transformations#^def-30-3|Definition §30.3]]), here the $xy$-plane of $\mathbb{R}^3$, and $A$ carries it one-to-one onto $\operatorname{Col} A = \mathbb{R}^2$. The second part is the projection of $\mathbf{x}$ onto the $z$-axis $\operatorname{Nul} A$, which $A$ kills. So $\mathbb{R}^3 = \operatorname{Nul} A \oplus \operatorname{Row} A$, a **direct sum** ([[§3 Subspaces#^ladr-1-41|LADR 1.41]]): every vector of $\mathbb{R}^3$ is in exactly one way a vector of $\operatorname{Nul} A$ plus a vector of $\operatorname{Row} A$ (equivalently, the two subspaces together span $\mathbb{R}^3$ and meet only in $\mathbf{0}$, [[§3 Subspaces#^ladr-1-46|LADR 1.46]]).
>
> **In general.** $\operatorname{Nul} A \subseteq \mathbb{R}^n$ and $\operatorname{Col} A \subseteq \mathbb{R}^m$ lie in different spaces unless $m = n$, so they cannot be summands of one direct sum. Even for a square $A$, where the Rank Theorem gives $\dim \operatorname{Nul} A + \dim \operatorname{Col} A = n$, the sum $\operatorname{Nul} A + \operatorname{Col} A$ need not be direct. For $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$, $A\mathbf{x} = (x_2, 0)$, so $\operatorname{Nul} A = \operatorname{Col} A = \operatorname{Span}\{\mathbf{e}_1\}$ and $\operatorname{Nul} A + \operatorname{Col} A$ is only a line in $\mathbb{R}^2$. (Lay's Practice Problem 2 of 2.8 is the $3 \times 3$ analogue, with $\mathbf{e}_1$ in both $\operatorname{Nul} A$ and $\operatorname{Col} A$.) The direct sums that do hold for every $m \times n$ matrix are
>
> $$
> \mathbb{R}^n = \operatorname{Nul} A \oplus \operatorname{Row} A \qquad\text{and}\qquad \mathbb{R}^m = \operatorname{Col} A \oplus \operatorname{Nul} A^T ,
> $$
>
> with the two summands orthogonal complements of each other ([[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]]; $\dim \operatorname{Row} A = \operatorname{rank} A$ by [[§34 Rank#^thm-34-3|Theorem §34.3]]).
>
> *The lecture writes the splitting in the example as $\mathbb{R}^3 = \operatorname{Nul}(A) \oplus \operatorname{Col}(A)$ and $\mathbf{x} = A(\mathbf{x}) + \mathbf{x}'$; since $\operatorname{Col} A$ and $A(\mathbf{x})$ lie in $\mathbb{R}^2$, this reads $\mathbb{R}^2$ as the $xy$-plane of $\mathbb{R}^3$, and the summand inside $\mathbb{R}^3$ is $\operatorname{Row} A$, as written above.*
>
> *Source: 235 lecture L16*

^rem-22-2

> [!example] Example §22.3: Null Space, Column Space and the Rank Theorem
> Let $A = \begin{bmatrix} 3 & 0 & -1 \\ 3 & 0 & -1 \\ 4 & 0 & 5 \end{bmatrix}$, a map $\mathbb{R}^3 \to \mathbb{R}^3$. Then
>
> $$
> A\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3x_1 - x_3 \\ 3x_1 - x_3 \\ 4x_1 + 5x_3 \end{bmatrix} .
> $$
>
> **Null space.** $A\mathbf{x} = \mathbf{0}$ means $3x_1 = x_3$ and $4x_1 + 5x_3 = 0$, so $4x_1 + 15x_1 = 0$, $x_1 = 0$ and $x_3 = 0$, with $x_2$ arbitrary. So $\operatorname{Nul} A$ is the $x_2$-axis, $\dim \operatorname{Nul} A = 1$.
>
> **Column space.** The first two coordinates of $A\mathbf{x}$ are always equal, so $\operatorname{Col} A$ lies in the plane $\{y_1 = y_2\}$. It is all of that plane: the columns $(3, 3, 4)$ and $(-1, -1, 5)$ lie in it and are not multiples of each other, so they span a plane. So $\operatorname{Col} A = \{y_1 = y_2\}$ and $\operatorname{rank} A = 2$. (By pivots: $R_2 - R_1$ and $R_3 - \frac43 R_1$ give $\begin{bmatrix} 3 & 0 & -1 \\ 0 & 0 & 0 \\ 0 & 0 & 19/3 \end{bmatrix}$, pivots in columns 1 and 3.)
>
> **Check.** $\operatorname{rank} A + \dim \operatorname{Nul} A = 2 + 1 = 3 = \dim \mathbb{R}^3$, the number of columns. Every line parallel to the $x_2$-axis is mapped to a single point of the plane $\operatorname{Col} A$.
>
> *Source: 235 lecture L16*

^ex-22-3

The next theorem is important for applications and is needed in Chapters 5 and 6. Lay states it here and proves it in 4.5; it is plausible if one thinks of a $p$-dimensional subspace as isomorphic to $\mathbb{R}^p$, since by the Invertible Matrix Theorem $p$ vectors in $\mathbb{R}^p$ are linearly independent if and only if they span $\mathbb{R}^p$.

**The Basis Theorem** (Lay's Theorem 15). *Let $H$ be a $p$-dimensional subspace of $\mathbb{R}^n$. Any linearly independent set of exactly $p$ elements in $H$ is automatically a basis for $H$. Also, any set of $p$ elements of $H$ that spans $H$ is automatically a basis for $H$.* Proved in [[§33 The Dimension of a Vector Space#^thm-33-5|Theorem §33.5]]; rigorously [[§6 Dimension#^ladr-2-38|LADR 2.38]] and [[§6 Dimension#^ladr-2-42|LADR 2.42]].

> [!example] Example §22.4: Bases, Dimensions and Coordinates
> **(a) Three independent vectors in $\mathbb{R}^3$.** The vectors $(1, 2, 0)$, $(3, 4, 0)$, $(5, 6, 7)$ are linearly independent: the matrix with these columns reduces by $R_2 - 2R_1$ to $\begin{bmatrix} 1 & 3 & 5 \\ 0 & -2 & -4 \\ 0 & 0 & 7 \end{bmatrix}$, with three pivots. (The lecture checks this with a determinant, expanding along row 3 by [[§24 Introduction to Determinants#^thm-24-1|Theorem §24.1]]: $\det = 7 \cdot (1 \cdot 4 - 3 \cdot 2) = -14 \ne 0$.) Since $\dim \mathbb{R}^3 = 3$, the Basis Theorem says they form a basis of $\mathbb{R}^3$, with no need to check spanning. Likewise every basis of $\mathbb{R}^4$ has exactly 4 vectors.
>
> **(b) The dimension of a span.** Let $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ with $\mathbf{v}_1 = (2, -8, 6)$, $\mathbf{v}_2 = (3, -7, -1)$, $\mathbf{v}_3 = (-1, 6, -7)$. $H$ is the column space of $A = [\,\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3\,]$, and
>
> $$
> \begin{bmatrix} 2 & 3 & -1 \\ -8 & -7 & 6 \\ 6 & -1 & -7 \end{bmatrix}
> \xrightarrow[R_3 - 3R_1]{R_2 + 4R_1}
> \begin{bmatrix} 2 & 3 & -1 \\ 0 & 5 & 2 \\ 0 & -10 & -4 \end{bmatrix}
> \xrightarrow{R_3 + 2R_2}
> \begin{bmatrix} 2 & 3 & -1 \\ 0 & 5 & 2 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> The pivot columns are 1 and 2, so $\{\mathbf{v}_1, \mathbf{v}_2\}$ is a basis for $H$ and $\dim H = 2$. (Indeed $\mathbf{v}_3 = -\tfrac{11}{10}\mathbf{v}_1 + \tfrac25\mathbf{v}_2$.)
>
> **(c) From coordinates to the vector.** For the basis $\mathcal{B} = \left\{\begin{bmatrix} 1 \\ .2 \end{bmatrix}, \begin{bmatrix} .2 \\ 1 \end{bmatrix}\right\}$ of $\mathbb{R}^2$ and $[\mathbf{x}]_{\mathcal{B}} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$,
>
> $$
> \mathbf{x} = 3\begin{bmatrix} 1 \\ .2 \end{bmatrix} + 2\begin{bmatrix} .2 \\ 1 \end{bmatrix} = \begin{bmatrix} 3.4 \\ 2.6 \end{bmatrix} .
> $$
>
> **(d) No four-dimensional subspace of $\mathbb{R}^3$.** A basis of a four-dimensional subspace would be four linearly independent vectors in $\mathbb{R}^3$, but any set of more than 3 vectors in $\mathbb{R}^3$ is linearly dependent ([[§8 Linear Independence#^thm-8-6|Theorem §8.6]]). So $\mathbb{R}^3$ has no four-dimensional subspace.
>
> *Lay: 2.9, Practice Problems 1–3*
> *Source: 235 lecture L16*

^ex-22-4

## Rank and the Invertible Matrix Theorem

The vector space concepts attached to a matrix give six more statements for the Invertible Matrix Theorem, numbered to follow the statements of [[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]].

> [!theorem] Theorem §22.3: The Invertible Matrix Theorem (Continued)
> Let $A$ be an $n \times n$ matrix. Then the following statements are each equivalent to the statement that $A$ is an invertible matrix.
>
> m. The columns of $A$ form a basis of $\mathbb{R}^n$.
> n. $\operatorname{Col} A = \mathbb{R}^n$.
> o. $\dim \operatorname{Col} A = n$.
> p. $\operatorname{rank} A = n$.
> q. $\operatorname{Nul} A = \{\mathbf{0}\}$.
> r. $\dim \operatorname{Nul} A = 0$.
>
> These continue statements (a)–(l) of [[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]], the previous version. This theorem is the home of (m)–(r): Lay 5e restates them in 4.6 ([[§34 Rank#^thm-34-5|Theorem §34.5]]). Next version: [[§25 Properties of Determinants#^thm-25-4|Theorem §25.4]] ($\det A \ne 0$).
>
> *Lay: 2.9, The Invertible Matrix Theorem (continued)*

^thm-22-3

> [!proof]+ Proof
> **(m).** By definition of a basis, (m) says that the columns of $A$ are linearly independent and span $\mathbb{R}^n$: statements (e) and (h) together. Each of these alone is equivalent to invertibility, so (m) is too.
>
> **(n)–(r).** These are linked to the earlier statements by a chain of almost trivial implications:
>
> $$
> \text{(g)} \Rightarrow \text{(n)} \Rightarrow \text{(o)} \Rightarrow \text{(p)} \Rightarrow \text{(r)} \Rightarrow \text{(q)} \Rightarrow \text{(d)} .
> $$
>
> - (g) $\Rightarrow$ (n): $\operatorname{Col} A$ is precisely the set of all $\mathbf{b}$ for which $A\mathbf{x} = \mathbf{b}$ is consistent, and (g) says this is every $\mathbf{b}$ in $\mathbb{R}^n$.
> - (n) $\Rightarrow$ (o) $\Rightarrow$ (p): $\dim \mathbb{R}^n = n$, and $\operatorname{rank} A = \dim \operatorname{Col} A$ by definition.
> - (p) $\Rightarrow$ (r): if $\operatorname{rank} A = n$, the number of columns, then $\dim \operatorname{Nul} A = n - n = 0$ by the Rank Theorem.
> - (r) $\Rightarrow$ (q): the only subspace of dimension $0$ is $\{\mathbf{0}\}$ (a nonzero subspace contains a nonzero vector, which is an independent set, so it has positive dimension).
> - (q) $\Rightarrow$ (d): $\operatorname{Nul} A = \{\mathbf{0}\}$ says exactly that $A\mathbf{x} = \mathbf{0}$ has only the trivial solution.
>
> Since (d) and (g) are already known to be equivalent to invertibility ([[§16 Characterizations of Invertible Matrices#^thm-16-1|Theorem §16.1]]), each statement in the chain is implied by invertibility (through (g)) and implies it (through (d)).

^pf-22-3

*Uses:* [[§16 Characterizations of Invertible Matrices#^thm-16-1|§16.1]], [[§22 Dimension and Rank#^thm-22-2|§22.2]], [[§22 Dimension and Rank#^def-22-2|Def. §22.2]], [[§22 Dimension and Rank#^def-22-3|Def. §22.3]], [[§21 Subspaces of ℝⁿ#^def-21-2|Def. §21.2]], [[§21 Subspaces of ℝⁿ#^def-21-4|Def. §21.4]]

The lecture proves the same chain the other way round: (m) $\Rightarrow$ (n) $\Rightarrow$ (o) $\Rightarrow$ (p) $\Rightarrow$ (q) by the Rank Theorem, and (q) $\Rightarrow$ (m) because $\dim \operatorname{Nul} A = 0$ gives $\dim \operatorname{Col} A = n$, so the $n$ columns span $\mathbb{R}^n$ and, being $n$ spanning vectors of an $n$-dimensional space, form a basis. The theorem is continued with $\det A \ne 0$ in [[§25 Properties of Determinants#^thm-25-4|Theorem §25.4]]; [[§34 Rank#^thm-34-5|Theorem §34.5]] restates (m)–(r) in Lay 4.6 and remarks that each statement may also be made for $A^T$ (for instance $\operatorname{Row} A = \mathbb{R}^n$); eigenvalues and the determinant give statements (s), (t) in [[§41 The Characteristic Equation#^thm-41-2|Theorem §41.2]]; and the theorem is concluded with (u)–(x), among them $\operatorname{Row} A = \mathbb{R}^n$, in [[§62★ The Singular Value Decomposition in Applications#^thm-62-2|Theorem §62.2]].

> [!remark]- Remark: Numerical Note — Rank in Practice
> Many algorithms in this text are good for understanding concepts and for small hand computations but unsuitable for large real problems. Rank is an example. It seems easy to reduce to echelon form and count pivots, but unless exact arithmetic is done on exactly specified entries, row operations can change the apparent rank. If $x$ in $\begin{bmatrix} 5 & 7 \\ 5 & x \end{bmatrix}$ is not stored exactly as $7$, the computed rank may be 1 or 2, depending on whether the computer treats $x - 7$ as zero. In practice the **effective rank** is found from the singular value decomposition: [[§61★ The Singular Value Decomposition#^rem-61-1|§61★, Remark: Numerical Note — Effective Rank]].

^rem-22-3
