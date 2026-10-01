---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 26
lay: "4.4"
aliases: ["Lay 4.4"]
tags: [applied-linear-algebra, math235]
---
← [[§25 Linearly Independent Sets; Bases]] · ↑ [[· 4 Vector Spaces]] · [[§27 The Dimension of a Vector Space]] →

*Lay, Section 4.4 · MATH 235 lectures L14, L15.*

A basis imposes a coordinate system on a vector space. Every vector is a linear combination of the basis vectors in exactly one way, and the weights are its coordinates. If the basis has $n$ vectors, the coordinate mapping $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal B}$ is a one-to-one linear map onto $\mathbb{R}^n$, an isomorphism, so the space "acts like" $\mathbb{R}^n$: questions about polynomials or functions become questions about column vectors, settled by row reduction. When the space is $\mathbb{R}^n$ itself, a basis $\mathcal{B}$ gives a new "view" of it, and the change-of-coordinates matrix $P_{\mathcal B}$ translates between the two views.

## The Unique Representation Theorem

> [!theorem] Theorem §26.1: The Unique Representation Theorem
> Let $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ be a basis for a vector space $V$. Then for each $\mathbf{x}$ in $V$, there exists a unique set of scalars $c_1, \ldots, c_n$ such that
>
> $$
> \mathbf{x} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n . \qquad (1)
> $$
>
> *Lay: Theorem 7 (4.4)*

^thm-26-1

> [!proof]+ Proof
> Since $\mathcal{B}$ spans $V$, there exist scalars such that (1) holds. Suppose $\mathbf{x}$ also has the representation $\mathbf{x} = d_1\mathbf{b}_1 + \cdots + d_n\mathbf{b}_n$ for scalars $d_1, \ldots, d_n$. Subtracting,
>
> $$
> \mathbf{0} = \mathbf{x} - \mathbf{x} = (c_1 - d_1)\mathbf{b}_1 + \cdots + (c_n - d_n)\mathbf{b}_n . \qquad (2)
> $$
>
> Since $\mathcal{B}$ is linearly independent, the weights in (2) must all be zero; that is, $c_j = d_j$ for $1 \le j \le n$.

^pf-26-1

*Uses:* [[§25 Linearly Independent Sets; Bases#^def-25-2|Def. §25.2]], [[§25 Linearly Independent Sets; Bases#^def-25-1|Def. §25.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§5 Bases#^ladr-2-28|LADR 2.28]], where uniqueness of the representation is shown to be *equivalent* to being a basis; the coordinate vector is Axler's $\mathcal{M}(v)$, [[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]]. In an orthogonal basis the weights have a closed formula: [[§41 Orthogonal Sets#^thm-41-2|Theorem §41.2]].

> [!definition] Definition §26.1: Coordinates; Coordinate Vector; Coordinate Mapping
> Suppose $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ is a basis for $V$ and $\mathbf{x}$ is in $V$. The **coordinates of $\mathbf{x}$ relative to the basis $\mathcal{B}$** (the **$\mathcal{B}$-coordinates of $\mathbf{x}$**) are the weights $c_1, \ldots, c_n$ such that $\mathbf{x} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$. The vector in $\mathbb{R}^n$
>
> $$
> [\mathbf{x}]_{\mathcal B} = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix}
> $$
>
> is the **coordinate vector of $\mathbf{x}$ (relative to $\mathcal{B}$)**, or the **$\mathcal{B}$-coordinate vector of $\mathbf{x}$**, and the mapping $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal B}$ is the **coordinate mapping (determined by $\mathcal{B}$)**. The definition assumes that $\mathcal{B}$ is an *indexed* set, its vectors listed in a fixed order, so that $[\mathbf{x}]_{\mathcal B}$ is unambiguous. Theorem §26.1 makes the coordinates well defined.
>
> *Lay: 4.4, Definition*

^def-26-1

> [!example] Example §26.1: From Coordinates to the Vector
> **(a)** Let $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$ with $\mathbf{b}_1 = (1, 0)$, $\mathbf{b}_2 = (1, 2)$. If $[\mathbf{x}]_{\mathcal B} = (-2, 3)$, the coordinates say how to build $\mathbf{x}$ from $\mathcal{B}$:
>
> $$
> \mathbf{x} = (-2)\mathbf{b}_1 + 3\mathbf{b}_2 = (-2)\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 3\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 6 \end{bmatrix} .
> $$
>
> The lecture takes $[\mathbf{x}]_{\mathcal B} = (1, 4)$ for the same basis: $\mathbf{x} = 1\,(1, 0) + 4\,(1, 2) = (5, 8)$.
>
> **(b) The standard basis.** The entries of $\mathbf{x} = (1, 6)$ are its coordinates relative to $\mathcal{E} = \{\mathbf{e}_1, \mathbf{e}_2\}$, since $(1, 6) = 1 \cdot \mathbf{e}_1 + 6 \cdot \mathbf{e}_2$. In general, $[\mathbf{x}]_{\mathcal E} = \mathbf{x}$ for the standard basis $\mathcal{E}$ of $\mathbb{R}^n$ (the lecture's example: $\mathbf{v} = (v_1, \ldots, v_4) = v_1\mathbf{e}_1 + \cdots + v_4\mathbf{e}_4$ in $\mathbb{R}^4$).
>
> *Lay: Examples 4.4.1 and 4.4.2*
> *Source: 235 lecture L15*

^ex-26-1

> [!remark] Remark: Coordinates as Graph Paper
> A coordinate system on a set is a one-to-one mapping of its points into $\mathbb{R}^n$. Ordinary graph paper is the coordinate system of the standard basis: $\mathbf{x} = (1, 6)$ lies $1$ unit in the $\mathbf{e}_1$ direction and $6$ units in the $\mathbf{e}_2$ direction. Erasing the standard grid and drawing instead the grid of lines parallel to $\mathbf{b}_1$ and $\mathbf{b}_2$ through the integer multiples of the other vector gives "$\mathcal{B}$-graph paper", on which the same point has the new address $[\mathbf{x}]_{\mathcal B}$: in Example §26.1(a), $-2$ units in the $\mathbf{b}_1$ direction and $3$ units in the $\mathbf{b}_2$ direction (figure below, for Example §26.2). In crystallography, for instance, a basis $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ along three edges of a unit cell gives the natural coordinates of the atoms: $(\tfrac12, \tfrac12, 1)$ is the centre of the top face.

^rem-26-1

## Coordinates in ℝⁿ

> [!example] Example §26.2: Finding a Coordinate Vector
> Let $\mathbf{b}_1 = (2, 1)$, $\mathbf{b}_2 = (-1, 1)$, $\mathbf{x} = (4, 5)$ and $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2\}$. Find $[\mathbf{x}]_{\mathcal B}$.
>
> The coordinates $c_1, c_2$ satisfy
>
> $$
> c_1\begin{bmatrix} 2 \\ 1 \end{bmatrix} + c_2\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \end{bmatrix}, \qquad\text{that is,}\qquad \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \end{bmatrix} . \qquad (3)
> $$
>
> Row reduce (the lecture's steps: interchange, $R_2 - 2R_1$, scale, $R_1 - R_2$):
>
> $$
> \begin{bmatrix} 2 & -1 & 4 \\ 1 & 1 & 5 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 5 \\ 2 & -1 & 4 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 5 \\ 0 & -3 & -6 \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 5 \\ 0 & 1 & 2 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 2 \end{bmatrix} .
> $$
>
> So $c_1 = 3$, $c_2 = 2$: $\mathbf{x} = 3\mathbf{b}_1 + 2\mathbf{b}_2$ and $[\mathbf{x}]_{\mathcal B} = (3, 2)$. Check: $3(2, 1) + 2(-1, 1) = (4, 5)$.
>
> *Lay: Example 4.4.4*
> *Source: 235 lecture L15*

^ex-26-2

![[m235-26-1.svg]]
*Example §26.2 on two kinds of graph paper. On the standard grid the point $\mathbf{x}$ has address $(4, 5)$. On the grid built from $\mathbf{b}_1$ (blue lines) and $\mathbf{b}_2$ (green lines), the same point is reached by going $3$ steps along $\mathbf{b}_1$ and then $2$ steps along $\mathbf{b}_2$, so $[\mathbf{x}]_{\mathcal B} = (3, 2)$.*

The matrix in (3) changes the $\mathcal{B}$-coordinates of a vector into its standard coordinates. The same works for any basis of $\mathbb{R}^n$.

> [!definition] Definition §26.2: Change-of-Coordinates Matrix
> For a basis $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ of $\mathbb{R}^n$, let
>
> $$
> P_{\mathcal B} = [\mathbf{b}_1 \ \mathbf{b}_2 \ \cdots \ \mathbf{b}_n] .
> $$
>
> $P_{\mathcal B}$ is the **change-of-coordinates matrix** from $\mathcal{B}$ to the standard basis in $\mathbb{R}^n$.
>
> *Lay: 4.4 (text)*

^def-26-2

> [!theorem] Proposition §26.2: The Change-of-Coordinates Equation
> For a basis $\mathcal{B}$ of $\mathbb{R}^n$ and every $\mathbf{x}$ in $\mathbb{R}^n$,
>
> $$
> \mathbf{x} = P_{\mathcal B}[\mathbf{x}]_{\mathcal B} . \qquad (4)
> $$
>
> $P_{\mathcal B}$ is invertible, and $[\mathbf{x}]_{\mathcal B} = P_{\mathcal B}^{-1}\mathbf{x}$. So the coordinate mapping $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal B}$ of $\mathbb{R}^n$ is the matrix transformation of $P_{\mathcal B}^{-1}$, a one-to-one linear transformation from $\mathbb{R}^n$ onto $\mathbb{R}^n$.
>
> *Lay: 4.4, Equation (4) and text*

^prop-26-2

> [!proof]+ Proof
> If $[\mathbf{x}]_{\mathcal B} = (c_1, \ldots, c_n)$, then by the definition of a matrix–vector product, $P_{\mathcal B}[\mathbf{x}]_{\mathcal B} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n = \mathbf{x}$; this is (4). The columns of $P_{\mathcal B}$ form a basis for $\mathbb{R}^n$, so $P_{\mathcal B}$ is invertible by the Invertible Matrix Theorem ([[§19 Dimension and Rank#^thm-19-3|Theorem §19.3]], 2.9). Multiplying (4) on the left by $P_{\mathcal B}^{-1}$ gives $[\mathbf{x}]_{\mathcal B} = P_{\mathcal B}^{-1}\mathbf{x}$. The matrix transformation of an invertible matrix is one-to-one and onto (Invertible Matrix Theorem; Theorem 12 of 1.9, [[§9 The Matrix of a Linear Transformation#^thm-9-3|Theorem §9.3]]).

^pf-26-2

*Uses:* [[§26 Coordinate Systems#^def-26-1|Def. §26.1]], [[§26 Coordinate Systems#^def-26-2|Def. §26.2]], [[§13 Characterizations of Invertible Matrices#^thm-13-1|§13.1]], [[§19 Dimension and Rank#^thm-19-3|§19.3]], [[§9 The Matrix of a Linear Transformation#^thm-9-3|§9.3]]

The change-of-coordinates equation (4) is needed at several points in Chapters 5 and 7; the change between two arbitrary bases is [[§29 Change of Basis#^thm-29-1|Theorem §29.1]] (4.7).

## The Coordinate Mapping

Choosing a basis $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ for a vector space $V$ introduces a coordinate system in $V$. The coordinate mapping $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal B}$ connects the possibly unfamiliar space $V$ to the familiar space $\mathbb{R}^n$: points of $V$ can be identified by their new "names".

> [!theorem] Theorem §26.3: The Coordinate Mapping Is an Isomorphism onto ℝⁿ
> Let $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ be a basis for a vector space $V$. Then the coordinate mapping $\mathbf{x} \mapsto [\mathbf{x}]_{\mathcal B}$ is a one-to-one linear transformation from $V$ onto $\mathbb{R}^n$. Consequently, for $\mathbf{u}_1, \ldots, \mathbf{u}_p$ in $V$ and scalars $c_1, \ldots, c_p$,
>
> $$
> [c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p]_{\mathcal B} = c_1[\mathbf{u}_1]_{\mathcal B} + \cdots + c_p[\mathbf{u}_p]_{\mathcal B} : \qquad (5)
> $$
>
> the $\mathcal{B}$-coordinate vector of a linear combination is the *same* linear combination of the coordinate vectors.
>
> *Lay: Theorem 8 (4.4); Equation (5)*

^thm-26-3

> [!proof]+ Proof
> **Linear.** Take two typical vectors in $V$, $\mathbf{u} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n$ and $\mathbf{w} = d_1\mathbf{b}_1 + \cdots + d_n\mathbf{b}_n$. Then $\mathbf{u} + \mathbf{w} = (c_1 + d_1)\mathbf{b}_1 + \cdots + (c_n + d_n)\mathbf{b}_n$, so
>
> $$
> [\mathbf{u} + \mathbf{w}]_{\mathcal B} = \begin{bmatrix} c_1 + d_1 \\ \vdots \\ c_n + d_n \end{bmatrix} = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} + \begin{bmatrix} d_1 \\ \vdots \\ d_n \end{bmatrix} = [\mathbf{u}]_{\mathcal B} + [\mathbf{w}]_{\mathcal B} .
> $$
>
> For a scalar $r$, $r\mathbf{u} = (rc_1)\mathbf{b}_1 + \cdots + (rc_n)\mathbf{b}_n$, so $[r\mathbf{u}]_{\mathcal B} = (rc_1, \ldots, rc_n) = r[\mathbf{u}]_{\mathcal B}$. (These use Theorem §26.1: the displayed combinations are *the* representations of $\mathbf{u} + \mathbf{w}$ and $r\mathbf{u}$.) Equation (5) follows by applying these two rules repeatedly.
>
> **One-to-one** (Lay's Exercise 23). If $[\mathbf{u}]_{\mathcal B} = [\mathbf{w}]_{\mathcal B} = (c_1, \ldots, c_n)$, then $\mathbf{u} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n = \mathbf{w}$.
>
> **Onto $\mathbb{R}^n$** (Lay's Exercise 24). Given $\mathbf{y} = (y_1, \ldots, y_n)$ in $\mathbb{R}^n$, the vector $\mathbf{u} = y_1\mathbf{b}_1 + \cdots + y_n\mathbf{b}_n$ is in $V$ and $[\mathbf{u}]_{\mathcal B} = \mathbf{y}$.

^pf-26-3

*Uses:* [[§26 Coordinate Systems#^thm-26-1|§26.1]], [[§26 Coordinate Systems#^def-26-1|Def. §26.1]], [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-4|Def. §24.4]]

> [!definition] Definition §26.3: Isomorphism
> A one-to-one linear transformation from a vector space $V$ onto a vector space $W$ is an **isomorphism** from $V$ onto $W$ (Greek *iso*, "the same", and *morph*, "form" or "structure"). The notation and terminology of $V$ and $W$ may differ, but the two spaces are indistinguishable as vector spaces: *every vector space calculation in $V$ is accurately reproduced in $W$, and vice versa*. By Theorem §26.3, any real vector space with a basis of $n$ vectors is isomorphic to $\mathbb{R}^n$.
>
> *Lay: 4.4 (text)*

^def-26-3

> [!remark]- Connections
> - Rigorous treatment: isomorphisms [[§10 Invertibility and Isomorphisms#^ladr-3-69|LADR 3.69]], and [[Dimension shows whether vector spaces are isomorphic]] ([[§10 Invertibility and Isomorphisms#^ladr-3-70|LADR 3.70]]): finite-dimensional spaces are isomorphic exactly when they have the same dimension, the fact behind Lay's question at the end of 4.4 (answered in [[§27 The Dimension of a Vector Space#^thm-27-2|Theorem §27.2]]).
> - One-to-one and onto, and an invertible function is a bijection: [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]], [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]].

> [!theorem] Corollary §26.4: Coordinates Preserve Independence and Spanning
> Let $\mathcal{B}$ be a basis of $V$ with $n$ vectors, and let $\mathbf{u}_1, \ldots, \mathbf{u}_p$, $\mathbf{w}$ be in $V$.
> 1. $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is linearly independent in $V$ if and only if $\{[\mathbf{u}_1]_{\mathcal B}, \ldots, [\mathbf{u}_p]_{\mathcal B}\}$ is linearly independent in $\mathbb{R}^n$.
> 2. $\mathbf{w}$ is a linear combination of $\mathbf{u}_1, \ldots, \mathbf{u}_p$ if and only if $[\mathbf{w}]_{\mathcal B}$ is a linear combination of $[\mathbf{u}_1]_{\mathcal B}, \ldots, [\mathbf{u}_p]_{\mathcal B}$ (with the same weights).
>
> *Lay: 4.4, Exercises 25 and 26*

^cor-26-4

> [!proof]+ Proof
> **1.** By (5) and because the coordinate mapping is one-to-one with $[\mathbf{0}]_{\mathcal B} = \mathbf{0}$, the equations
>
> $$
> c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p = \mathbf{0} \ \text{ (in } V) \qquad\text{and}\qquad c_1[\mathbf{u}_1]_{\mathcal B} + \cdots + c_p[\mathbf{u}_p]_{\mathcal B} = \mathbf{0} \ \text{ (in } \mathbb{R}^n)
> $$
>
> have the same solutions $c_1, \ldots, c_p$: the second is $[c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p]_{\mathcal B} = [\mathbf{0}]_{\mathcal B}$. So one has only the trivial solution exactly when the other does.
>
> **2.** Likewise $\mathbf{w} = c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p$ if and only if $[\mathbf{w}]_{\mathcal B} = [c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p]_{\mathcal B} = c_1[\mathbf{u}_1]_{\mathcal B} + \cdots + c_p[\mathbf{u}_p]_{\mathcal B}$.

^pf-26-4

*Uses:* [[§26 Coordinate Systems#^thm-26-3|§26.3]], [[§25 Linearly Independent Sets; Bases#^def-25-1|Def. §25.1]]

> [!example] Example §26.3: Polynomials as Vectors in ℝ⁴; Two Coordinate Systems
> **(a) The monomial basis.** Let $\mathcal{B} = \{1, t, t^2, t^3\}$ be the standard basis of $\mathbb{P}_3$. A typical element $\mathbf{p}(t) = a_0 + a_1t + a_2t^2 + a_3t^3$ is already displayed as a linear combination of the basis vectors, so
>
> $$
> [\mathbf{p}]_{\mathcal B} = \begin{bmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \end{bmatrix} .
> $$
>
> The coordinate mapping $\mathbf{p} \mapsto [\mathbf{p}]_{\mathcal B}$ is an isomorphism from $\mathbb{P}_3$ onto $\mathbb{R}^4$: every vector space operation in $\mathbb{P}_3$ corresponds to the same operation in $\mathbb{R}^4$. By Taylor's formula, $a_k = \mathbf{p}^{(k)}(0)/k!$, so these coordinates are the right ones for recovering $\mathbf{p}$ from its derivatives at $0$.
>
> **(b) The Lagrange basis** (the lecture). The Lagrange polynomials for the nodes $1, 2, 3, 4$ ([[§22 Cramer’s Rule, Volume, and Linear Transformations#^ex-22-2|Example §22.2]]),
>
> $$
> L_1 = \frac{(t-2)(t-3)(t-4)}{(1-2)(1-3)(1-4)}, \quad L_2 = \frac{(t-1)(t-3)(t-4)}{(2-1)(2-3)(2-4)}, \quad L_3 = \frac{(t-1)(t-2)(t-4)}{(3-1)(3-2)(3-4)}, \quad L_4 = \frac{(t-1)(t-2)(t-3)}{(4-1)(4-2)(4-3)},
> $$
>
> satisfy $L_i(j) = 1$ if $i = j$ and $0$ otherwise. They form a basis $\mathcal{L}$ of $\mathbb{P}_3$. *Independent:* if $a_1L_1 + a_2L_2 + a_3L_3 + a_4L_4 = 0$, setting $t = 1$ gives $a_1 = 0$, and $t = 2, 3, 4$ give $a_2 = a_3 = a_4 = 0$. *Spanning:* every $\mathbf{p}$ in $\mathbb{P}_3$ equals $\mathbf{p}(1)L_1 + \mathbf{p}(2)L_2 + \mathbf{p}(3)L_3 + \mathbf{p}(4)L_4$, since both sides are cubic polynomials taking the same values at $1, 2, 3, 4$, and a nonzero polynomial of degree at most $3$ has at most $3$ zeros. Hence
>
> $$
> [\mathbf{p}]_{\mathcal L} = \begin{bmatrix} \mathbf{p}(1) \\ \mathbf{p}(2) \\ \mathbf{p}(3) \\ \mathbf{p}(4) \end{bmatrix} ,
> $$
>
> the right coordinates for recovering $\mathbf{p}$ from its values at $1, 2, 3, 4$. For example, $\mathbf{p}(t) = t^3$ has $[\mathbf{p}]_{\mathcal B} = (0, 0, 0, 1)$ but $[\mathbf{p}]_{\mathcal L} = (1, 8, 27, 64)$: the same vector, two names.
>
> **(c) Fibonacci-type sequences.** The subspace of sequences with $x_{n+1} = x_n + x_{n-1}$ ([[§23 Vector Spaces and Subspaces#^ex-23-2|Example §23.2]](e)) is isomorphic to $\mathbb{R}^2$: a sequence is determined by $(x_1, x_2)$, and $(x_n) \mapsto (x_1, x_2)$ is linear, one-to-one and onto. The sequences starting $1, 0, 1, 1, 2, \ldots$ and $0, 1, 1, 2, 3, \ldots$ form a basis, and the coordinates of a sequence relative to it are $(x_1, x_2)$. (The lecture announces "Fib $= \mathbb{R}^2$" in L14 and returns to these sequences with eigenvalues in L18: [[§30 Applications to Difference Equations#^ex-30-4|Example §30.4]] uses the basis of the two geometric sequences $(\varphi^k)$, $(\psi^k)$ instead, and finds the Fibonacci numbers in closed form.)
>
> *Lay: Example 4.4.5*
> *Source: 235 lectures L14, L15*

^ex-26-3

> [!example] Example §26.4: Testing Polynomials for Independence
> **(a)** Use coordinate vectors to verify that $1 + 2t^2$, $4 + t + 5t^2$ and $3 + 2t$ are linearly dependent in $\mathbb{P}_2$.
>
> Relative to the standard basis $\{1, t, t^2\}$ the coordinate vectors are $(1, 0, 2)$, $(4, 1, 5)$, $(3, 2, 0)$. Write them as the columns of $A$ and row reduce $[A \ \mathbf{0}]$ ($R_3 - 2R_1$, then $R_3 + 3R_2$):
>
> $$
> \begin{bmatrix} 1 & 4 & 3 & 0 \\ 0 & 1 & 2 & 0 \\ 2 & 5 & 0 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & 4 & 3 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & -3 & -6 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & 4 & 3 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> $x_3$ is free, so the columns of $A$ are linearly dependent, and by Corollary §26.4 so are the polynomials. In fact column 3 is $2$ times column 2 minus $5$ times column 1, and the corresponding relation for the polynomials is
>
> $$
> 3 + 2t = 2(4 + t + 5t^2) - 5(1 + 2t^2) .
> $$
>
> **(b)** (The lecture.) Are $\mathbf{p}_1 = t + t^2$, $\mathbf{p}_2 = 1 + t$, $\mathbf{p}_3 = 1$ linearly independent? Their coordinate vectors relative to $\{1, t, t^2\}$ are $(0, 1, 1)$, $(1, 1, 0)$, $(1, 0, 0)$. In the order $\mathbf{p}_3, \mathbf{p}_2, \mathbf{p}_1$,
>
> $$
> \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}
> $$
>
> is already in echelon form with three pivots, so the coordinate vectors, and hence the polynomials, are linearly independent: a basis of $\mathbb{P}_2$.
>
> *Lay: Example 4.4.6*
> *Source: 235 lecture L15*

^ex-26-4

> [!example] Example §26.5: Coordinates in a Plane and in ℙ₂
> **(a) A plane in $\mathbb{R}^3$.** Let $\mathbf{v}_1 = (3, 6, 2)$, $\mathbf{v}_2 = (-1, 0, 1)$, $\mathbf{x} = (3, 12, 7)$, and $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$, a basis for $H = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ (two vectors, not multiples of each other). Is $\mathbf{x}$ in $H$, and if so, what is $[\mathbf{x}]_{\mathcal B}$? If $\mathbf{x}$ is in $H$, then $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = \mathbf{x}$ is consistent, and $c_1$, $c_2$ are the $\mathcal{B}$-coordinates of $\mathbf{x}$. Row reduce:
>
> $$
> \begin{bmatrix} 3 & -1 & 3 \\ 6 & 0 & 12 \\ 2 & 1 & 7 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So $c_1 = 2$, $c_2 = 3$, and $[\mathbf{x}]_{\mathcal B} = (2, 3)$; check: $2(3, 6, 2) + 3(-1, 0, 1) = (3, 12, 7)$. The coordinate system on $H$ determined by $\mathcal{B}$ makes $H$ isomorphic to $\mathbb{R}^2$. (Would a different basis of $H$ also make it isomorphic to $\mathbb{R}^2$, and not to some other $\mathbb{R}^m$? Yes: all bases of $H$ have the same number of vectors, [[§27 The Dimension of a Vector Space#^thm-27-2|Theorem §27.2]].)
>
> **(b) A non-standard basis of $\mathbb{P}_2$.** $\mathcal{B} = \{1 + t,\ 1 + t^2,\ t + t^2\}$ is a basis for $\mathbb{P}_2$. Find the coordinate vector of $\mathbf{p}(t) = 6 + 3t - t^2$. Writing $\mathbf{p} = c_1(1 + t) + c_2(1 + t^2) + c_3(t + t^2)$ and comparing coefficients of $1$, $t$, $t^2$:
>
> $$
> c_1 + c_2 = 6, \qquad c_1 + c_3 = 3, \qquad c_2 + c_3 = -1 .
> $$
>
> Adding all three, $2(c_1 + c_2 + c_3) = 8$, so $c_1 + c_2 + c_3 = 4$, and then $c_3 = 4 - 6 = -2$, $c_2 = 4 - 3 = 1$, $c_1 = 4 - (-1) = 5$. So $[\mathbf{p}]_{\mathcal B} = (5, 1, -2)$. Check: $5(1 + t) + (1 + t^2) - 2(t + t^2) = 6 + 3t - t^2$. (In coordinates relative to $\{1, t, t^2\}$ this is the system with matrix $\begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$, of determinant $-2 \ne 0$, which also confirms that $\mathcal{B}$ is a basis, by Corollary §26.4.)
>
> *Lay: Example 4.4.7; Practice Problem 2 (4.4)*

^ex-26-5
