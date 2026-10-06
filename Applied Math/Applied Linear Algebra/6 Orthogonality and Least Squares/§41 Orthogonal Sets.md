---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 41
lay: "6.2"
aliases: ["Lay 6.2"]
tags: [applied-linear-algebra, math235]
---
← [[§40 Inner Product, Length, and Orthogonality]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§42 Orthogonal Projections]] →

*Lay, Section 6.2.*

A set of mutually orthogonal nonzero vectors is automatically linearly independent, and in an orthogonal basis the coordinates of a vector are found by one division each, $c_j = \mathbf{y} \cdot \mathbf{u}_j / \mathbf{u}_j \cdot \mathbf{u}_j$, with no system to solve. Each such term is the orthogonal projection of $\mathbf{y}$ onto a line, the construction behind everything in the rest of the chapter. The section ends with matrices whose columns are orthonormal: they satisfy $U^TU = I$ and preserve lengths and angles. Square ones are the orthogonal matrices.

## Orthogonal Sets

> [!definition] Definition §41.1: Orthogonal Set
> A set of vectors $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ in $\mathbb{R}^n$ is an **orthogonal set** if each pair of distinct vectors from the set is orthogonal, that is, if $\mathbf{u}_i \cdot \mathbf{u}_j = 0$ whenever $i \ne j$.
>
> *Lay: 6.2 (text)*

^def-41-1

> [!theorem] Theorem §41.1: Orthogonal Sets Are Linearly Independent
> If $S = \{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is an orthogonal set of nonzero vectors in $\mathbb{R}^n$, then $S$ is linearly independent and hence is a basis for the subspace spanned by $S$.
>
> *Lay: Theorem 4 (6.2)*

^thm-41-1

> [!proof]+ Proof
> Suppose $\mathbf{0} = c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p$. Take the inner product of both sides with $\mathbf{u}_1$:
>
> $$
> \begin{aligned}
> 0 = \mathbf{0} \cdot \mathbf{u}_1 &= (c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \cdots + c_p\mathbf{u}_p) \cdot \mathbf{u}_1 \\
> &= c_1(\mathbf{u}_1 \cdot \mathbf{u}_1) + c_2(\mathbf{u}_2 \cdot \mathbf{u}_1) + \cdots + c_p(\mathbf{u}_p \cdot \mathbf{u}_1) = c_1(\mathbf{u}_1 \cdot \mathbf{u}_1),
> \end{aligned}
> $$
>
> because $\mathbf{u}_1$ is orthogonal to $\mathbf{u}_2, \ldots, \mathbf{u}_p$. Since $\mathbf{u}_1 \ne \mathbf{0}$, $\mathbf{u}_1 \cdot \mathbf{u}_1 \ne 0$, so $c_1 = 0$. Taking the inner product with $\mathbf{u}_j$ instead shows $c_j = 0$ for each $j$. So the only linear relation is the trivial one, and $S$ is linearly independent. A linearly independent spanning set of a subspace is a basis of it.

^pf-41-1

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§7 Linear Independence#^def-7-1|Def. §7.1]] (linear independence), [[§18 Subspaces of ℝⁿ#^def-18-4|Def. §18.4]] (basis)

> [!definition] Definition §41.2: Orthogonal Basis
> An **orthogonal basis** for a subspace $W$ of $\mathbb{R}^n$ is a basis for $W$ that is also an orthogonal set.
>
> *Lay: 6.2, Definition*

^def-41-2

> [!theorem] Theorem §41.2: Coordinates in an Orthogonal Basis
> Let $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ be an orthogonal basis for a subspace $W$ of $\mathbb{R}^n$. For each $\mathbf{y}$ in $W$, the weights in the linear combination
>
> $$
> \mathbf{y} = c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p
> $$
>
> are given by
>
> $$
> c_j = \frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j} \qquad (j = 1, \ldots, p) .
> $$
>
> *Lay: Theorem 5 (6.2)*

^thm-41-2

> [!proof]+ Proof
> As in the proof of Theorem §41.1, orthogonality kills all but one term:
>
> $$
> \mathbf{y} \cdot \mathbf{u}_j = (c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p) \cdot \mathbf{u}_j = c_j(\mathbf{u}_j \cdot \mathbf{u}_j) .
> $$
>
> Since $\mathbf{u}_j \ne \mathbf{0}$ (it belongs to a basis), $\mathbf{u}_j \cdot \mathbf{u}_j \ne 0$, and we can solve for $c_j$.

^pf-41-2

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§20 Orthonormal Bases#^ladr-6-25|LADR 6.25]] (orthonormal lists are linearly independent) and [[§20 Orthonormal Bases#^ladr-6-30|LADR 6.30]] ($v = \langle v, e_1\rangle e_1 + \cdots + \langle v, e_n\rangle e_n$); Axler works with orthonormal lists, so the denominators $\mathbf{u}_j \cdot \mathbf{u}_j$ are $1$.
> - In a Hilbert space the same coefficients give infinite expansions: [[§24 Orthonormal Sets and Bases#^prop-24-6|556 Prop. §24.6]], [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]].
> - PDE version: [[§24 Expansion in Series of Eigenfunctions#^prop-24-1|341 Prop. §24.1]] (the same formula for the coefficients of an expansion in orthogonal eigenfunctions, with $\int f\phi_mp\,dx$ in place of the dot product); the Fourier case is [[§6 Periodic Functions and Fourier Series#^prop-6-4|341 Prop. §6.4]].

> [!example] Example §41.1: An Orthogonal Basis of ℝ³
> Let
>
> $$
> \mathbf{u}_1 = \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix}, \qquad \mathbf{u}_2 = \begin{bmatrix} -1 \\ 2 \\ 1 \end{bmatrix}, \qquad \mathbf{u}_3 = \begin{bmatrix} -1/2 \\ -2 \\ 7/2 \end{bmatrix}, \qquad \mathbf{y} = \begin{bmatrix} 6 \\ 1 \\ -8 \end{bmatrix} .
> $$
>
> **(a) The set is orthogonal.** Check the three pairs:
>
> $$
> \begin{aligned}
> \mathbf{u}_1 \cdot \mathbf{u}_2 &= 3(-1) + 1(2) + 1(1) = 0, \\
> \mathbf{u}_1 \cdot \mathbf{u}_3 &= 3(-\tfrac12) + 1(-2) + 1(\tfrac72) = -\tfrac32 - 2 + \tfrac72 = 0, \\
> \mathbf{u}_2 \cdot \mathbf{u}_3 &= -1(-\tfrac12) + 2(-2) + 1(\tfrac72) = \tfrac12 - 4 + \tfrac72 = 0 .
> \end{aligned}
> $$
>
> The vectors are nonzero, so by Theorem §41.1 they are linearly independent; three independent vectors in $\mathbb{R}^3$ form a basis. So $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ is an orthogonal basis of $\mathbb{R}^3$.
>
> **(b) Coordinates of y.** Compute
>
> $$
> \mathbf{y} \cdot \mathbf{u}_1 = 18 + 1 - 8 = 11, \quad \mathbf{y} \cdot \mathbf{u}_2 = -6 + 2 - 8 = -12, \quad \mathbf{y} \cdot \mathbf{u}_3 = -3 - 2 - 28 = -33,
> $$
>
> $$
> \mathbf{u}_1 \cdot \mathbf{u}_1 = 9 + 1 + 1 = 11, \quad \mathbf{u}_2 \cdot \mathbf{u}_2 = 1 + 4 + 1 = 6, \quad \mathbf{u}_3 \cdot \mathbf{u}_3 = \tfrac14 + 4 + \tfrac{49}{4} = \tfrac{33}{2} .
> $$
>
> By Theorem §41.2,
>
> $$
> \mathbf{y} = \frac{11}{11}\mathbf{u}_1 + \frac{-12}{6}\mathbf{u}_2 + \frac{-33}{33/2}\mathbf{u}_3 = \mathbf{u}_1 - 2\mathbf{u}_2 - 2\mathbf{u}_3 .
> $$
>
> Check: $\mathbf{u}_1 - 2\mathbf{u}_2 - 2\mathbf{u}_3 = (3 + 2 + 1,\ 1 - 4 + 4,\ 1 - 2 - 7) = (6, 1, -8)$. With a basis that is not orthogonal, the weights would require row reducing $[\,\mathbf{u}_1\ \mathbf{u}_2\ \mathbf{u}_3\ \mathbf{y}\,]$.
>
> *Lay: Examples 6.2.1 and 6.2.2*

^ex-41-1

## An Orthogonal Projection

> [!definition] Definition §41.3: Orthogonal Projection onto a Line
> Let $\mathbf{u} \ne \mathbf{0}$ in $\mathbb{R}^n$ and $L = \operatorname{Span}\{\mathbf{u}\}$. For $\mathbf{y} \in \mathbb{R}^n$, the **orthogonal projection of $\mathbf{y}$ onto $\mathbf{u}$** (or **onto $L$**) is
>
> $$
> \hat{\mathbf{y}} = \operatorname{proj}_L \mathbf{y} = \frac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u},
> $$
>
> and $\mathbf{z} = \mathbf{y} - \hat{\mathbf{y}}$ is the **component of $\mathbf{y}$ orthogonal to $\mathbf{u}$**. Replacing $\mathbf{u}$ by $c\mathbf{u}$ ($c \ne 0$) does not change $\hat{\mathbf{y}}$, since $\frac{\mathbf{y} \cdot c\mathbf{u}}{c\mathbf{u} \cdot c\mathbf{u}}\,c\mathbf{u} = \frac{c^2\,\mathbf{y} \cdot \mathbf{u}}{c^2\,\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}$. So the projection depends only on the line $L$, which justifies the notation $\operatorname{proj}_L$.
>
> *Lay: 6.2, Equation (2); Exercise 31*

^def-41-3

> [!theorem] Proposition §41.3: Decomposing a Vector Along a Line
> Let $\mathbf{u} \ne \mathbf{0}$ and $\mathbf{y}$ be vectors in $\mathbb{R}^n$. There is exactly one way to write
>
> $$
> \mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}
> $$
>
> with $\hat{\mathbf{y}} = \alpha\mathbf{u}$ a multiple of $\mathbf{u}$ and $\mathbf{z}$ orthogonal to $\mathbf{u}$, namely $\alpha = \dfrac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}$: $\hat{\mathbf{y}}$ is the orthogonal projection of Definition §41.3.
>
> *Lay: 6.2 (text), Equation (1)*

^prop-41-3

> [!proof]+ Proof
> For any scalar $\alpha$, setting $\mathbf{z} = \mathbf{y} - \alpha\mathbf{u}$ gives $\mathbf{y} = \alpha\mathbf{u} + \mathbf{z}$; so the only question is when $\mathbf{z}$ is orthogonal to $\mathbf{u}$. By [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|Theorem §40.1]],
>
> $$
> (\mathbf{y} - \alpha\mathbf{u}) \cdot \mathbf{u} = \mathbf{y} \cdot \mathbf{u} - \alpha(\mathbf{u} \cdot \mathbf{u}) ,
> $$
>
> and since $\mathbf{u} \cdot \mathbf{u} \ne 0$, this is $0$ if and only if $\alpha = \mathbf{y} \cdot \mathbf{u} / \mathbf{u} \cdot \mathbf{u}$.

^pf-41-3

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§41 Orthogonal Sets#^def-41-3|Def. §41.3]]

> [!remark]- Connections
> - Stewart's vector projection $\operatorname{proj}_{\mathbf{a}} \mathbf{b} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|^2}\mathbf{a}$ in $\mathbb{R}^2$, $\mathbb{R}^3$: [[§82 The Dot Product#^def-82-5|Calc Def. §82.5]], [[§82 The Dot Product#^thm-82-6|Calc Thm. §82.6]].
> - Rigorous treatment: [[§19 Inner Products and Norms#^ladr-6-13|LADR 6.13]] (an orthogonal decomposition $u = cv + w$ with $w \perp v$, the step in Axler's proof of Cauchy–Schwarz) and [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-56|LADR 6.56]] (projection onto a one-dimensional subspace).

> [!example] Example §41.2: Projecting onto a Line
> Let $\mathbf{y} = \begin{bmatrix} 7 \\ 6 \end{bmatrix}$ and $\mathbf{u} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$. Find the orthogonal projection of $\mathbf{y}$ onto $\mathbf{u}$, write $\mathbf{y}$ as a sum of a vector in $L = \operatorname{Span}\{\mathbf{u}\}$ and a vector orthogonal to $\mathbf{u}$, and find the distance from $\mathbf{y}$ to $L$.
>
> **Projection.** $\mathbf{y} \cdot \mathbf{u} = 28 + 12 = 40$ and $\mathbf{u} \cdot \mathbf{u} = 16 + 4 = 20$, so
>
> $$
> \hat{\mathbf{y}} = \frac{40}{20}\mathbf{u} = 2\begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} 8 \\ 4 \end{bmatrix}, \qquad
> \mathbf{y} - \hat{\mathbf{y}} = \begin{bmatrix} 7 \\ 6 \end{bmatrix} - \begin{bmatrix} 8 \\ 4 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix} .
> $$
>
> **Decomposition.**
>
> $$
> \underbrace{\begin{bmatrix} 7 \\ 6 \end{bmatrix}}_{\mathbf{y}} = \underbrace{\begin{bmatrix} 8 \\ 4 \end{bmatrix}}_{\hat{\mathbf{y}}} + \underbrace{\begin{bmatrix} -1 \\ 2 \end{bmatrix}}_{\mathbf{y} - \hat{\mathbf{y}}} .
> $$
>
> Check: $\hat{\mathbf{y}} \cdot (\mathbf{y} - \hat{\mathbf{y}}) = -8 + 8 = 0$, so $\{\hat{\mathbf{y}}, \mathbf{y} - \hat{\mathbf{y}}\}$ is an orthogonal set, as it must be. (Using $\mathbf{u} = (2, 1)$ instead gives $\frac{20}{5}(2, 1) = (8, 4)$ again: the projection depends only on $L$.)
>
> **Distance.** The segment from $\mathbf{y}$ to $\hat{\mathbf{y}}$ is perpendicular to $L$, so $\hat{\mathbf{y}}$ is the point of $L$ closest to $\mathbf{y}$ (assumed here from plane geometry; proved in $\mathbb{R}^n$ in [[§42 Orthogonal Projections#^thm-42-3|Theorem §42.3]]). The distance from $\mathbf{y}$ to $L$ is
>
> $$
> \|\mathbf{y} - \hat{\mathbf{y}}\| = \sqrt{(-1)^2 + 2^2} = \sqrt5 .
> $$
>
> *Lay: Examples 6.2.3 and 6.2.4; 6.2, Practice Problem 2*

^ex-41-2

![[m235-41-1.svg]]
*Example §41.2. The projection $\hat{\mathbf{y}} = (8, 4)$ of $\mathbf{y} = (7, 6)$ onto the line $L$ through $\mathbf{u} = (4, 2)$ is the foot of the perpendicular from $\mathbf{y}$. The component $\mathbf{y} - \hat{\mathbf{y}} = (-1, 2)$ (red), drawn also from the origin, is orthogonal to $L$, and its length $\sqrt5$ is the distance from $\mathbf{y}$ to $L$.*

> [!remark] Remark: A Geometric Interpretation of Theorem §41.2
> Each term $\frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}\mathbf{u}_j$ in Theorem §41.2 is the orthogonal projection of $\mathbf{y}$ onto the line spanned by $\mathbf{u}_j$. So the theorem decomposes each $\mathbf{y} \in \operatorname{Span}\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ into the sum of its projections onto $p$ mutually orthogonal lines. For $W = \mathbb{R}^2 = \operatorname{Span}\{\mathbf{u}_1, \mathbf{u}_2\}$ with $\mathbf{u}_1 \perp \mathbf{u}_2$,
>
> $$
> \mathbf{y} = \frac{\mathbf{y} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1}\mathbf{u}_1 + \frac{\mathbf{y} \cdot \mathbf{u}_2}{\mathbf{u}_2 \cdot \mathbf{u}_2}\mathbf{u}_2
> $$
>
> writes $\mathbf{y}$ as the sum of its projections onto the two perpendicular axes determined by $\mathbf{u}_1$ and $\mathbf{u}_2$: ordinary coordinates, in a rotated coordinate system. In physics this is the decomposition of a force $\mathbf{y}$ into a component along a direction of interest $\mathbf{u}$ (say the direction of motion) and a component orthogonal to it, computed exactly as in Example §41.2.

^rem-41-1

## Orthonormal Sets

> [!definition] Definition §41.4: Orthonormal Set; Orthonormal Basis
> A set $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is an **orthonormal set** if it is an orthogonal set of unit vectors. If $W$ is the subspace spanned by such a set, then $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is an **orthonormal basis** for $W$; it is a basis because it is linearly independent by Theorem §41.1.
>
> The standard basis $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ of $\mathbb{R}^n$, and any nonempty subset of it, is orthonormal. Normalizing each vector of an orthogonal set of nonzero vectors produces an orthonormal set, since $\big(\frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}\big) \cdot \big(\frac{\mathbf{u}_j}{\|\mathbf{u}_j\|}\big) = \frac{\mathbf{u}_i \cdot \mathbf{u}_j}{\|\mathbf{u}_i\|\,\|\mathbf{u}_j\|}$ is still $0$ for $i \ne j$.
>
> *Lay: 6.2 (text); Exercise 32*

^def-41-4

> [!theorem] Theorem §41.4: Orthonormal Columns
> An $m \times n$ matrix $U$ has orthonormal columns if and only if $U^TU = I$.
>
> *Lay: Theorem 6 (6.2)*

^thm-41-4

> [!proof]+ Proof
> Write $U = [\,\mathbf{u}_1\ \cdots\ \mathbf{u}_n\,]$ with $\mathbf{u}_j \in \mathbb{R}^m$. The rows of $U^T$ are $\mathbf{u}_1^T, \ldots, \mathbf{u}_n^T$, so by the row–column rule the $(i, j)$-entry of $U^TU$ is $\mathbf{u}_i^T\mathbf{u}_j = \mathbf{u}_i \cdot \mathbf{u}_j$. For three columns:
>
> $$
> U^TU = \begin{bmatrix} \mathbf{u}_1^T \\ \mathbf{u}_2^T \\ \mathbf{u}_3^T \end{bmatrix} \begin{bmatrix} \mathbf{u}_1 & \mathbf{u}_2 & \mathbf{u}_3 \end{bmatrix} = \begin{bmatrix} \mathbf{u}_1^T\mathbf{u}_1 & \mathbf{u}_1^T\mathbf{u}_2 & \mathbf{u}_1^T\mathbf{u}_3 \\ \mathbf{u}_2^T\mathbf{u}_1 & \mathbf{u}_2^T\mathbf{u}_2 & \mathbf{u}_2^T\mathbf{u}_3 \\ \mathbf{u}_3^T\mathbf{u}_1 & \mathbf{u}_3^T\mathbf{u}_2 & \mathbf{u}_3^T\mathbf{u}_3 \end{bmatrix} .
> $$
>
> Hence $U^TU = I$ means exactly: the off-diagonal entries vanish, $\mathbf{u}_i \cdot \mathbf{u}_j = 0$ for $i \ne j$ (the columns are orthogonal), and the diagonal entries are $1$, $\mathbf{u}_j \cdot \mathbf{u}_j = 1$ (the columns are unit vectors).

^pf-41-4

*Uses:* [[§11 Matrix Operations#^prop-11-4|§11.4]] (row–column rule for products), [[§41 Orthogonal Sets#^def-41-4|Def. §41.4]]

> [!theorem] Theorem §41.5: Matrices with Orthonormal Columns Preserve Lengths and Angles
> Let $U$ be an $m \times n$ matrix with orthonormal columns, and let $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$. Then
>
> a. $\|U\mathbf{x}\| = \|\mathbf{x}\|$
>
> b. $(U\mathbf{x}) \cdot (U\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$
>
> c. $(U\mathbf{x}) \cdot (U\mathbf{y}) = 0$ if and only if $\mathbf{x} \cdot \mathbf{y} = 0$.
>
> So the linear map $\mathbf{x} \mapsto U\mathbf{x}$ preserves lengths and orthogonality.
>
> *Lay: Theorem 7 (6.2)*

^thm-41-5

> [!proof]+ Proof
> Lay leaves this as Exercise 25. (b): by Theorem §41.4,
>
> $$
> (U\mathbf{x}) \cdot (U\mathbf{y}) = (U\mathbf{x})^T(U\mathbf{y}) = \mathbf{x}^TU^TU\mathbf{y} = \mathbf{x}^TI\mathbf{y} = \mathbf{x} \cdot \mathbf{y} .
> $$
>
> (a): take $\mathbf{y} = \mathbf{x}$ in (b): $\|U\mathbf{x}\|^2 = \|\mathbf{x}\|^2$; both norms are nonnegative. (c) is immediate from (b).

^pf-41-5

*Uses:* [[§41 Orthogonal Sets#^thm-41-4|§41.4]], [[§11 Matrix Operations#^thm-11-7|§11.7]] ($(AB)^T = B^TA^T$)

> [!example] Example §41.3: A Matrix with Orthonormal Columns Preserves Length
> Let
>
> $$
> U = \begin{bmatrix} 1/\sqrt2 & 2/3 \\ 1/\sqrt2 & -2/3 \\ 0 & 1/3 \end{bmatrix}, \qquad \mathbf{x} = \begin{bmatrix} \sqrt2 \\ 3 \end{bmatrix}, \qquad \mathbf{y} = \begin{bmatrix} -3\sqrt2 \\ 6 \end{bmatrix} .
> $$
>
> **Orthonormal columns.**
>
> $$
> U^TU = \begin{bmatrix} 1/\sqrt2 & 1/\sqrt2 & 0 \\ 2/3 & -2/3 & 1/3 \end{bmatrix} \begin{bmatrix} 1/\sqrt2 & 2/3 \\ 1/\sqrt2 & -2/3 \\ 0 & 1/3 \end{bmatrix} = \begin{bmatrix} \frac12 + \frac12 & \frac{2}{3\sqrt2} - \frac{2}{3\sqrt2} \\ \frac{2}{3\sqrt2} - \frac{2}{3\sqrt2} & \frac49 + \frac49 + \frac19 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} .
> $$
>
> **Lengths.**
>
> $$
> U\mathbf{x} = \begin{bmatrix} 1 + 2 \\ 1 - 2 \\ 0 + 1 \end{bmatrix} = \begin{bmatrix} 3 \\ -1 \\ 1 \end{bmatrix}, \qquad \|U\mathbf{x}\| = \sqrt{9 + 1 + 1} = \sqrt{11}, \qquad \|\mathbf{x}\| = \sqrt{2 + 9} = \sqrt{11} .
> $$
>
> **Inner products.** $U\mathbf{y} = (-3 + 4,\ -3 - 4,\ 0 + 2) = (1, -7, 2)$, so $U\mathbf{x} \cdot U\mathbf{y} = 3 + 7 + 2 = 12$, while $\mathbf{x} \cdot \mathbf{y} = -6 + 18 = 12$.
>
> *Lay: Example 6.2.6; 6.2, Practice Problem 3*

^ex-41-3

> [!definition] Definition §41.5: Orthogonal Matrix
> An **orthogonal matrix** is a square invertible matrix $U$ such that $U^{-1} = U^T$.
>
> (A better name would be *orthonormal matrix*, but *orthogonal matrix* is the standard term.)
>
> *Lay: 6.2 (text)*

^def-41-5

> [!theorem] Proposition §41.6: Characterizing Orthogonal Matrices
> For an $n \times n$ matrix $U$ the following are equivalent:
>
> 1. $U$ is an orthogonal matrix;
> 2. $U$ has orthonormal columns;
> 3. $U$ has orthonormal rows.
>
> Moreover, an orthogonal matrix has $\det U = \pm 1$.
>
> *Lay: 6.2 (text); Exercises 27 and 28; Practice Problem 4*

^prop-41-6

> [!proof]+ Proof
> (1) ⇒ (2): $U^TU = U^{-1}U = I$, so the columns are orthonormal by Theorem §41.4.
>
> (2) ⇒ (1): by Theorem §41.4, $U^TU = I$. For square matrices a one-sided inverse is an inverse ([[§13 Characterizations of Invertible Matrices#^cor-13-2|Corollary §13.2]], from the Invertible Matrix Theorem), so $U$ is invertible with $U^{-1} = U^T$.
>
> (1) ⇔ (3): $U$ is orthogonal if and only if $U^T$ is: if $U^{-1} = U^T$, then $(U^T)^{-1} = (U^{-1})^T = (U^T)^T$, and conversely by the same computation for $U^T$. The rows of $U$ are the columns of $U^T$, so (3) for $U$ is (2) for $U^T$, which is equivalent to (1) for $U^T$, hence to (1) for $U$.
>
> **Determinant.** Taking determinants in $U^TU = I$ and using $\det U^T = \det U$ and the multiplicative property, $(\det U)^2 = \det(U^TU) = \det I = 1$, so $\det U = \pm 1$.

^pf-41-6

*Uses:* [[§41 Orthogonal Sets#^thm-41-4|§41.4]], [[§13 Characterizations of Invertible Matrices#^cor-13-2|§13.2]] (a one-sided inverse is an inverse), [[§12 The Inverse of a Matrix#^thm-12-4|§12.4]] ($(A^T)^{-1} = (A^{-1})^T$), [[§21 Properties of Determinants#^thm-21-6|§21.6]] ($\det A^T = \det A$), [[§21 Properties of Determinants#^thm-21-9|§21.9]] (multiplicative property)

> [!remark]- Connections
> - Rigorous treatment: real orthogonal matrices are the real unitary matrices, [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]] (unitary $\Leftrightarrow$ $Q^*Q = I$ $\Leftrightarrow$ orthonormal columns $\Leftrightarrow$ orthonormal rows $\Leftrightarrow$ norm-preserving); operator version [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-53|LADR 7.53]]. Orthogonal matrices return in [[§48★ Diagonalization of Symmetric Matrices#^def-48-2|Definition §48.2]] (orthogonal diagonalization).
> - The orthogonal matrices form the group $O(n) = \{A \in GL_n(\mathbb{R}) : A^TA = I\}$, [[§3 Basic Examples of Groups#^def-3-7|493 Def. §3.7]], and $\det : O(n) \to \{\pm 1\}$ is a homomorphism onto $\{\pm1\}$ with kernel $SO(n)$.

> [!example] Example §41.4: An Orthogonal Matrix
> Let
>
> $$
> U = \begin{bmatrix} 3/\sqrt{11} & -1/\sqrt6 & -1/\sqrt{66} \\ 1/\sqrt{11} & 2/\sqrt6 & -4/\sqrt{66} \\ 1/\sqrt{11} & 1/\sqrt6 & 7/\sqrt{66} \end{bmatrix} = [\,\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_3\,] .
> $$
>
> **The columns are orthonormal.** Using $\sqrt{11}\sqrt6 = \sqrt{66}$, $\sqrt{11}\sqrt{66} = \sqrt{726}$, $\sqrt6\sqrt{66} = \sqrt{396}$:
>
> $$
> \begin{aligned}
> \mathbf{v}_1 \cdot \mathbf{v}_2 &= (-3 + 2 + 1)/\sqrt{66} = 0, & \mathbf{v}_1 \cdot \mathbf{v}_1 &= 9/11 + 1/11 + 1/11 = 1, \\
> \mathbf{v}_1 \cdot \mathbf{v}_3 &= (-3 - 4 + 7)/\sqrt{726} = 0, & \mathbf{v}_2 \cdot \mathbf{v}_2 &= 1/6 + 4/6 + 1/6 = 1, \\
> \mathbf{v}_2 \cdot \mathbf{v}_3 &= (1 - 8 + 7)/\sqrt{396} = 0, & \mathbf{v}_3 \cdot \mathbf{v}_3 &= 1/66 + 16/66 + 49/66 = 1 .
> \end{aligned}
> $$
>
> So $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is an orthonormal set, hence an orthonormal basis of $\mathbb{R}^3$. These are the vectors $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$ of Example §41.1, normalized ($\|\mathbf{u}_3\| = \sqrt{33/2}$ and $\mathbf{u}_3/\|\mathbf{u}_3\| = (-1, -4, 7)/\sqrt{66}$). Since $U$ is square, it is an orthogonal matrix (Proposition §41.6).
>
> **The rows are orthonormal too**, as Proposition §41.6 predicts. Every product of two entries has denominator $11$, $6$ or $66$, so compute over $66$:
>
> $$
> \begin{aligned}
> \|\text{row}_1\|^2 &= \tfrac{9}{11} + \tfrac16 + \tfrac{1}{66} = \tfrac{54 + 11 + 1}{66} = 1, &
> \text{row}_1 \cdot \text{row}_2 &= \tfrac{3}{11} - \tfrac26 + \tfrac{4}{66} = \tfrac{18 - 22 + 4}{66} = 0, \\
> \|\text{row}_2\|^2 &= \tfrac{1}{11} + \tfrac46 + \tfrac{16}{66} = \tfrac{6 + 44 + 16}{66} = 1, &
> \text{row}_1 \cdot \text{row}_3 &= \tfrac{3}{11} - \tfrac16 - \tfrac{7}{66} = \tfrac{18 - 11 - 7}{66} = 0, \\
> \|\text{row}_3\|^2 &= \tfrac{1}{11} + \tfrac16 + \tfrac{49}{66} = \tfrac{6 + 11 + 49}{66} = 1, &
> \text{row}_2 \cdot \text{row}_3 &= \tfrac{1}{11} + \tfrac26 - \tfrac{28}{66} = \tfrac{6 + 22 - 28}{66} = 0 .
> \end{aligned}
> $$
>
> *Lay: Examples 6.2.5 and 6.2.7*

^ex-41-4
