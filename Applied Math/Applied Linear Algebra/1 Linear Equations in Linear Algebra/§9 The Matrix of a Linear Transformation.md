---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 9
lay: "1.9"
aliases: ["Lay 1.9"]
tags: [applied-linear-algebra, math235]
---
← [[§8 Introduction to Linear Transformations]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§10 Linear Models in Business, Science, and Engineering]] →

*Lay, Section 1.9 · MATH 235 lecture L5.*

Every linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ is a matrix transformation. $T$ is determined by the images $T(\mathbf{e}_1), \ldots, T(\mathbf{e}_n)$ of the columns of the identity matrix, and these images are the columns of its standard matrix. This gives formulas for transformations described geometrically: rotations, reflections, contractions, shears, projections. The existence and uniqueness questions become properties of the map: $T$ is onto exactly when the columns of its matrix span $\mathbb{R}^m$, and one-to-one exactly when they are linearly independent.

## The Standard Matrix

The columns of the $n \times n$ identity matrix $I_n$ are the **standard basis vectors** $\mathbf{e}_1, \ldots, \mathbf{e}_n$: $\mathbf{e}_j$ has a $1$ in entry $j$ and $0$'s elsewhere. Every $\mathbf{x}$ in $\mathbb{R}^n$ is $\mathbf{x} = I_n\mathbf{x} = x_1\mathbf{e}_1 + \cdots + x_n\mathbf{e}_n$; for instance in $\mathbb{R}^2$, $\mathbf{x} = x_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

> [!theorem] Theorem §9.1: The Matrix of a Linear Transformation
> Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Then there exists a unique matrix $A$ such that
>
> $$
> T(\mathbf{x}) = A\mathbf{x} \qquad \text{for all } \mathbf{x} \text{ in } \mathbb{R}^n .
> $$
>
> In fact, $A$ is the $m \times n$ matrix whose $j$th column is the vector $T(\mathbf{e}_j)$, where $\mathbf{e}_j$ is the $j$th column of the identity matrix in $\mathbb{R}^n$:
>
> $$
> A = [\,T(\mathbf{e}_1)\ \ \cdots\ \ T(\mathbf{e}_n)\,] . \qquad (3)
> $$
>
> *Lay: Theorem 10 (1.9)*

^thm-9-1

> [!proof]+ Proof
> **Existence.** Write $\mathbf{x} = I_n\mathbf{x} = [\,\mathbf{e}_1\ \cdots\ \mathbf{e}_n\,]\mathbf{x} = x_1\mathbf{e}_1 + \cdots + x_n\mathbf{e}_n$ and use the linearity of $T$ (the superposition principle):
>
> $$
> T(\mathbf{x}) = T(x_1\mathbf{e}_1 + \cdots + x_n\mathbf{e}_n) = x_1T(\mathbf{e}_1) + \cdots + x_nT(\mathbf{e}_n) = [\,T(\mathbf{e}_1)\ \cdots\ T(\mathbf{e}_n)\,]\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} = A\mathbf{x} .
> $$
>
> **Uniqueness** (Lay's Exercise 33). Suppose $B$ is an $m \times n$ matrix with $T(\mathbf{x}) = B\mathbf{x}$ for all $\mathbf{x}$. Then for each $j$, $B\mathbf{e}_j = 0\mathbf{b}_1 + \cdots + 1\mathbf{b}_j + \cdots + 0\mathbf{b}_n = \mathbf{b}_j$ is the $j$th column of $B$, and it equals $T(\mathbf{e}_j)$, the $j$th column of $A$. So $B = A$.

^pf-9-1

*Uses:* [[§8 Introduction to Linear Transformations#^prop-8-3|§8.3]] (superposition), [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]], [[§4 The Matrix Equation Ax = b#^def-4-4|Def. §4.4]]

> [!remark]- Connections
> - Rigorous treatment: a linear map is determined by its values on a basis, which may be prescribed freely, [[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]]; the standard matrix is Axler's $\mathcal{M}(T)$ ([[§9 Matrices#^ladr-3-31|LADR 3.31]]) for the standard bases. Axler allows any bases of any finite-dimensional $V$ and $W$, which Lay reaches in [[§35 Eigenvectors and Linear Transformations#^def-35-1|Definition §35.1]].

> [!definition] Definition §9.1: Standard Matrix
> The matrix $A = [\,T(\mathbf{e}_1)\ \cdots\ T(\mathbf{e}_n)\,]$ of [[§9 The Matrix of a Linear Transformation#^thm-9-1|Theorem §9.1]] is the **standard matrix for the linear transformation $T$**.
>
> *Lay: 1.9 (text)*

^def-9-1

So every linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a matrix transformation, and vice versa ([[§8 Introduction to Linear Transformations#^prop-8-2|Proposition §8.2]]). The term *linear transformation* focuses on a property of a mapping, *matrix transformation* on how it is implemented.

> [!example] Example §9.1: A Formula from the Images of e1 and e2
> **(a)** Suppose $T: \mathbb{R}^2 \to \mathbb{R}^3$ is linear with
>
> $$
> T(\mathbf{e}_1) = \begin{bmatrix} 5 \\ -7 \\ 2 \end{bmatrix}, \qquad T(\mathbf{e}_2) = \begin{bmatrix} -3 \\ 8 \\ 0 \end{bmatrix} .
> $$
>
> With no further information, $T$ is known everywhere: $\mathbf{x} = x_1\mathbf{e}_1 + x_2\mathbf{e}_2$, so by linearity
>
> $$
> T(\mathbf{x}) = x_1T(\mathbf{e}_1) + x_2T(\mathbf{e}_2) = x_1\begin{bmatrix} 5 \\ -7 \\ 2 \end{bmatrix} + x_2\begin{bmatrix} -3 \\ 8 \\ 0 \end{bmatrix} = \begin{bmatrix} 5x_1 - 3x_2 \\ -7x_1 + 8x_2 \\ 2x_1 + 0 \end{bmatrix} = \begin{bmatrix} 5 & -3 \\ -7 & 8 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} .
> $$
>
> **(b)** Projection onto the first coordinate axis in $\mathbb{R}^2$ sends $\mathbf{e}_1 \mapsto \mathbf{e}_1$ and $\mathbf{e}_2 \mapsto \mathbf{0}$, so its standard matrix is $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$. Projection onto the second axis sends $\mathbf{e}_1 \mapsto \mathbf{0}$, $\mathbf{e}_2 \mapsto \mathbf{e}_2$: $\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$. (In the lecture's picture, the first sends $(3, 2)$ to $(3, 0)$, and a rectangle with a corner at $\mathbf{0}$ collapses onto a segment of the $x_1$-axis.)
>
> *Lay: Example 1.9.1; Table 4*
> *Source: 235 lecture L5*

^ex-9-1

> [!example] Example §9.2: Dilation and Rotation
> **(a)** The dilation $T(\mathbf{x}) = 3\mathbf{x}$ on $\mathbb{R}^2$ has $T(\mathbf{e}_1) = 3\mathbf{e}_1 = (3, 0)$ and $T(\mathbf{e}_2) = 3\mathbf{e}_2 = (0, 3)$, so
>
> $$
> A = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix} .
> $$
>
> **(b)** Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ rotate each point about the origin through an angle $\varphi$, counterclockwise for positive $\varphi$. (That $T$ is linear can be shown geometrically: rotating a parallelogram gives the parallelogram of the rotated sides, as in [[§8 Introduction to Linear Transformations#^ex-8-4|Example §8.4]].) $\mathbf{e}_1 = (1, 0)$ rotates into $(\cos\varphi, \sin\varphi)$. $\mathbf{e}_2 = (0, 1)$ sits at angle $\pi/2$, so it rotates into the unit vector at angle $\varphi + \pi/2$:
>
> $$
> T(\mathbf{e}_2) = \begin{bmatrix} \cos(\varphi + \tfrac{\pi}{2}) \\ \sin(\varphi + \tfrac{\pi}{2}) \end{bmatrix} = \begin{bmatrix} -\sin\varphi \\ \cos\varphi \end{bmatrix} .
> $$
>
> By [[§9 The Matrix of a Linear Transformation#^thm-9-1|Theorem §9.1]],
>
> $$
> A = \begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix} .
> $$
>
> For $\varphi = \pi/2$ this is $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$, the rotation of [[§8 Introduction to Linear Transformations#^ex-8-4|Example §8.4(b)]].
>
> *Lay: Examples 1.9.2 and 1.9.3*
> *Source: 235 lecture L5*

^ex-9-2

![[m235-9-1.svg]]
*The rotation of [[§9 The Matrix of a Linear Transformation#^ex-9-2|Example §9.2]](b): $\mathbf{e}_1$ and $\mathbf{e}_2$ (blue) turn through $\varphi$ into the columns of the standard matrix (red), and the unit square turns with them.*

## Geometric Linear Transformations of ℝ²

A linear transformation of the plane is determined by what it does to $\mathbf{e}_1$ and $\mathbf{e}_2$, or equivalently to the **unit square** with sides $\mathbf{e}_1$, $\mathbf{e}_2$, which it maps onto the parallelogram with sides $T(\mathbf{e}_1)$, $T(\mathbf{e}_2)$.

> [!remark] Remark: A Catalog of Plane Transformations
> The standard matrices of Lay's Tables 1–4 ($k$ a scalar):
>
> | Transformation | Standard matrix | Transformation | Standard matrix |
> |---|---|---|---|
> | reflection through the $x_1$-axis | $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ | horizontal contraction ($0 < k < 1$) / expansion ($k > 1$) | $\begin{bmatrix} k & 0 \\ 0 & 1 \end{bmatrix}$ |
> | reflection through the $x_2$-axis | $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ | vertical contraction / expansion | $\begin{bmatrix} 1 & 0 \\ 0 & k \end{bmatrix}$ |
> | reflection through the line $x_2 = x_1$ | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ | horizontal shear | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ |
> | reflection through the line $x_2 = -x_1$ | $\begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$ | vertical shear | $\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$ |
> | reflection through the origin | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ | projection onto the $x_1$-axis / $x_2$-axis | $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$, $\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ |
>
> Each is read off from the images of $\mathbf{e}_1$ and $\mathbf{e}_2$: for instance, the reflection through $x_2 = x_1$ swaps $\mathbf{e}_1$ and $\mathbf{e}_2$, and the horizontal shear fixes $\mathbf{e}_1$ and sends $\mathbf{e}_2$ to $(k, 1)$. Other transformations are built by applying one after another (a horizontal shear followed by a reflection in the $x_2$-axis, say); such a composition is again linear ([[§11 Matrix Operations#^thm-11-2|Theorem §11.2]]).

^rem-9-1

![[m235-9-2.svg]]
*Four entries of the catalog acting on the unit square (dashed): the image of $\mathbf{e}_1$ is red, the image of $\mathbf{e}_2$ green, and the image of the square is the blue parallelogram they span.*

> [!example] Example §9.3: A Shear Followed by a Reflection
> Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ first perform a horizontal shear that maps $\mathbf{e}_2$ into $\mathbf{e}_2 - .5\mathbf{e}_1$ (leaving $\mathbf{e}_1$ unchanged), and then reflect the result through the $x_2$-axis. Assuming $T$ is linear, find its standard matrix.
>
> Follow $\mathbf{e}_1$ and $\mathbf{e}_2$. The shear fixes $\mathbf{e}_1 = (1, 0)$, and the reflection $(x_1, x_2) \mapsto (-x_1, x_2)$ sends it to $(-1, 0)$. The shear sends $\mathbf{e}_2$ to $\mathbf{e}_2 - .5\mathbf{e}_1 = (-.5, 1)$, and the reflection sends this to $(.5, 1)$. So
>
> $$
> A = [\,T(\mathbf{e}_1)\ \ T(\mathbf{e}_2)\,] = \begin{bmatrix} -1 & .5 \\ 0 & 1 \end{bmatrix} .
> $$
>
> *Lay: 1.9, Practice Problem 1*

^ex-9-3

## Existence and Uniqueness Questions

> [!definition] Definition §9.2: Onto
> A mapping $T: \mathbb{R}^n \to \mathbb{R}^m$ is **onto** $\mathbb{R}^m$ if each $\mathbf{b}$ in $\mathbb{R}^m$ is the image of *at least one* $\mathbf{x}$ in $\mathbb{R}^n$.
>
> Equivalently, the range of $T$ is all of the codomain $\mathbb{R}^m$: for each $\mathbf{b}$ in $\mathbb{R}^m$, $T(\mathbf{x}) = \mathbf{b}$ has at least one solution. "Does $T$ map $\mathbb{R}^n$ onto $\mathbb{R}^m$?" is an existence question.
>
> *Lay: 1.9, Definition*

^def-9-2

> [!definition] Definition §9.3: One-to-One
> A mapping $T: \mathbb{R}^n \to \mathbb{R}^m$ is **one-to-one** if each $\mathbf{b}$ in $\mathbb{R}^m$ is the image of *at most one* $\mathbf{x}$ in $\mathbb{R}^n$.
>
> Equivalently, for each $\mathbf{b}$ in $\mathbb{R}^m$, $T(\mathbf{x}) = \mathbf{b}$ has either a unique solution or none at all; $T$ is *not* one-to-one when some $\mathbf{b}$ is the image of more than one vector. "Is $T$ one-to-one?" is a uniqueness question.
>
> *Lay: 1.9, Definition*

^def-9-3

> [!remark]- Connections
> - The same notions for arbitrary functions: surjection and injection, [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]]; for linear maps, [[§8 Null Spaces and Ranges#^ladr-3-14|LADR 3.14]] (injective) and [[§8 Null Spaces and Ranges#^ladr-3-19|LADR 3.19]] (surjective).

The projections of Table 4 are neither one-to-one nor onto $\mathbb{R}^2$; the reflections, contractions/expansions ($k \ne 0$) and shears of Tables 1–3 are both.

> [!example] Example §9.4: Onto but Not One-to-One
> Let $T$ be the linear transformation with standard matrix
>
> $$
> A = \begin{bmatrix} 1 & -4 & 8 & 1 \\ 0 & 2 & -1 & 3 \\ 0 & 0 & 0 & 5 \end{bmatrix} .
> $$
>
> Does $T$ map $\mathbb{R}^4$ onto $\mathbb{R}^3$? Is $T$ one-to-one?
>
> $A$ is already in echelon form, with a pivot in each row (columns 1, 2, 4). By [[§4 The Matrix Equation Ax = b#^thm-4-3|Theorem §4.3]], $A\mathbf{x} = \mathbf{b}$ is consistent for every $\mathbf{b}$ in $\mathbb{R}^3$: $T$ maps $\mathbb{R}^4$ onto $\mathbb{R}^3$. But column 3 has no pivot, so $A\mathbf{x} = \mathbf{b}$ has a free variable ($x_3$; four variables, three basic): each $\mathbf{b}$ is the image of infinitely many $\mathbf{x}$, and $T$ is *not* one-to-one.
>
> *Lay: Example 1.9.4*

^ex-9-4

> [!theorem] Theorem §9.2: One-to-One Means Only the Trivial Solution
> Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Then $T$ is one-to-one if and only if the equation $T(\mathbf{x}) = \mathbf{0}$ has only the trivial solution.
>
> *Lay: Theorem 11 (1.9)*

^thm-9-2

> [!proof]+ Proof
> To prove "$P$ if and only if $Q$", Lay proves (1) if $P$ then $Q$, and (2a) if not $P$ then not $Q$ (the [[Contrapositive, Converse and Inverse|contrapositive]] of "if $Q$ then $P$").
>
> **(1)** Since $T$ is linear, $T(\mathbf{0}) = \mathbf{0}$ ([[§8 Introduction to Linear Transformations#^prop-8-3|Proposition §8.3]]). If $T$ is one-to-one, then $T(\mathbf{x}) = \mathbf{0}$ has at most one solution, hence only the trivial solution.
>
> **(2a)** If $T$ is not one-to-one, some $\mathbf{b}$ is the image of two different vectors $\mathbf{u} \ne \mathbf{v}$: $T(\mathbf{u}) = \mathbf{b}$ and $T(\mathbf{v}) = \mathbf{b}$. By linearity,
>
> $$
> T(\mathbf{u} - \mathbf{v}) = T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{b} - \mathbf{b} = \mathbf{0},
> $$
>
> and $\mathbf{u} - \mathbf{v} \ne \mathbf{0}$. So $T(\mathbf{x}) = \mathbf{0}$ has a nontrivial solution. Thus the two conditions are both true or both false.

^pf-9-2

*Uses:* [[§8 Introduction to Linear Transformations#^prop-8-3|§8.3]], [[§9 The Matrix of a Linear Transformation#^def-9-3|Def. §9.3]]

> [!remark]- Connections
> - Rigorous treatment: injective $\iff$ null space $= \{\mathbf{0}\}$, [[§8 Null Spaces and Ranges#^ladr-3-15|LADR 3.15]], with the same subtraction argument. The dimension counts behind Examples [[§9 The Matrix of a Linear Transformation#^ex-9-4|§9.4]] and [[§9 The Matrix of a Linear Transformation#^ex-9-5|§9.5]] ($\mathbb{R}^4 \to \mathbb{R}^3$ is never one-to-one, $\mathbb{R}^2 \to \mathbb{R}^3$ never onto) are [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]] and [[§8 Null Spaces and Ranges#^ladr-3-24|LADR 3.24]], respectively.

> [!theorem] Theorem §9.3: Onto and One-to-One via the Standard Matrix
> Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation, and let $A$ be the standard matrix for $T$. Then:
>
> a. $T$ maps $\mathbb{R}^n$ onto $\mathbb{R}^m$ if and only if the columns of $A$ span $\mathbb{R}^m$;
>
> b. $T$ is one-to-one if and only if the columns of $A$ are linearly independent.
>
> *Lay: Theorem 12 (1.9)*

^thm-9-3

> [!proof]+ Proof
> "If and only if" statements can be chained: from "$P$ iff $Q$" and "$Q$ iff $R$" follows "$P$ iff $R$".
>
> **(a)** By [[§4 The Matrix Equation Ax = b#^thm-4-3|Theorem §4.3]], the columns of $A$ span $\mathbb{R}^m$ if and only if $A\mathbf{x} = \mathbf{b}$ is consistent for each $\mathbf{b}$ in $\mathbb{R}^m$, that is, if and only if $T(\mathbf{x}) = \mathbf{b}$ has at least one solution for every $\mathbf{b}$. This is true if and only if $T$ maps $\mathbb{R}^n$ onto $\mathbb{R}^m$.
>
> **(b)** The equations $T(\mathbf{x}) = \mathbf{0}$ and $A\mathbf{x} = \mathbf{0}$ are the same except for notation. By [[§9 The Matrix of a Linear Transformation#^thm-9-2|Theorem §9.2]], $T$ is one-to-one if and only if $A\mathbf{x} = \mathbf{0}$ has only the trivial solution, which happens if and only if the columns of $A$ are linearly independent ([[§7 Linear Independence#^prop-7-1|Proposition §7.1]]).

^pf-9-3

*Uses:* [[§4 The Matrix Equation Ax = b#^thm-4-3|§4.3]], [[§9 The Matrix of a Linear Transformation#^thm-9-2|§9.2]], [[§7 Linear Independence#^prop-7-1|§7.1]], [[§9 The Matrix of a Linear Transformation#^thm-9-1|§9.1]]

In pivot terms: $T$ is onto iff $A$ has a pivot in every row, and one-to-one iff $A$ has a pivot in every column. Statement (a) also says: $T$ is onto iff every vector in $\mathbb{R}^m$ is a linear combination of the columns of $A$.

> [!example] Example §9.5: One-to-One but Not Onto
> **(a)** Let $T(x_1, x_2) = (3x_1 + x_2,\ 5x_1 + 7x_2,\ x_1 + 3x_2)$. (Column vectors are written in rows here, and $T(x_1, x_2)$ stands for $T((x_1, x_2))$.) Show that $T$ is a one-to-one linear transformation. Does $T$ map $\mathbb{R}^2$ onto $\mathbb{R}^3$?
>
> Reading off the coefficients row by row (the row–vector rule in reverse),
>
> $$
> T(\mathbf{x}) = \begin{bmatrix} 3x_1 + x_2 \\ 5x_1 + 7x_2 \\ x_1 + 3x_2 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 5 & 7 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = A\mathbf{x},
> $$
>
> so $T$ is linear with standard matrix $A$. The two columns $\mathbf{a}_1 = (3, 5, 1)$ and $\mathbf{a}_2 = (1, 7, 3)$ are not multiples of each other (the ratios of corresponding entries, $1/3$ and $7/5$, differ), so they are linearly independent, and $T$ is one-to-one by [[§9 The Matrix of a Linear Transformation#^thm-9-3|Theorem §9.3]](b). But $A$ is $3 \times 2$: it has at most 2 pivots, never 3, so its columns cannot span $\mathbb{R}^3$ ([[§4 The Matrix Equation Ax = b#^thm-4-3|Theorem §4.3]]), and $T$ is not onto $\mathbb{R}^3$. Its range is the plane $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_2\}$.
>
> **(b)** Suppose $A$ is a $7 \times 5$ matrix with 5 pivots, and $T(\mathbf{x}) = A\mathbf{x}$. Every one of the 5 columns has a pivot, so $A\mathbf{x} = \mathbf{0}$ has no free variable and $T$ is one-to-one. Only 5 of the 7 rows have pivots, so $T$ is not onto $\mathbb{R}^7$.
>
> *Lay: Example 1.9.5; 1.9, Practice Problem 2*

^ex-9-5
