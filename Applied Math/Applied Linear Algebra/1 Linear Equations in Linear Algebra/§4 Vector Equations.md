---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 4
lay: "1.3"
aliases: ["Lay 1.3"]
tags: [applied-linear-algebra, math235]
---
← [[§3 Solutions of Linear Systems]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§5 The Matrix Equation Ax = b]] →

*Lay, Section 1.3 · MATH 235 lectures L02, L2, L3.*

Until Chapter 4, a vector is an ordered list of numbers, written as a column. Vectors are added and scaled entry by entry, and geometrically they are points or arrows, added by the parallelogram rule. The central construction is the linear combination $c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p$. Asking whether $\mathbf{b}$ is a linear combination of given vectors is the same as asking whether a linear system is consistent, and the set of all linear combinations, the span, is a line or a plane through the origin in the simplest cases.

## Vectors in ℝⁿ

> [!definition] Definition §5.1: Vector, ℝⁿ, Zero Vector
> A matrix with only one column is a **column vector**, or simply a **vector**. For a positive integer $n$, $\mathbb{R}^n$ ("r-n") is the set of all lists (**ordered $n$-tuples**) of $n$ real numbers, written as $n \times 1$ column matrices:
>
> $$
> \mathbf{u} = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{bmatrix} .
> $$
>
> Two vectors in $\mathbb{R}^n$ are **equal** if and only if their corresponding entries are equal; so $\begin{bmatrix} 4 \\ 7 \end{bmatrix} \ne \begin{bmatrix} 7 \\ 4 \end{bmatrix}$. The vector whose entries are all zero is the **zero vector**, denoted $\mathbf{0}$ (its number of entries is clear from context).
>
> To save space, a column vector such as $\begin{bmatrix} 3 \\ -1 \end{bmatrix}$ may be written $(3, -1)$, with parentheses and a comma. This is different from the $1 \times 2$ row matrix $[\,3\ \ {-1}\,]$, which has a different shape.
>
> *Lay: 1.3 (text)*

^def-4-1

> [!definition] Definition §5.2: Vector Addition and Scalar Multiplication
> For $\mathbf{u}$, $\mathbf{v}$ in $\mathbb{R}^n$ and a real number $c$, the **sum** $\mathbf{u} + \mathbf{v}$ is the vector obtained by adding corresponding entries, and the **scalar multiple** $c\mathbf{u}$ is the vector obtained by multiplying each entry of $\mathbf{u}$ by $c$:
>
> $$
> \begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix} + \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix},
> \qquad
> c\begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix} = \begin{bmatrix} cu_1 \\ \vdots \\ cu_n \end{bmatrix} .
> $$
>
> The number $c$ is a **scalar** (lightface, to distinguish it from boldface vectors). We write $-\mathbf{u}$ for $(-1)\mathbf{u}$ and $\mathbf{u} - \mathbf{v}$ for $\mathbf{u} + (-1)\mathbf{v}$. For example, $\begin{bmatrix} 1 \\ -2 \end{bmatrix} + \begin{bmatrix} 2 \\ 5 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}$ and $5\begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 15 \\ -5 \end{bmatrix}$.
>
> *Lay: 1.3 (text)*

^def-4-2

> [!remark] Remark: Vectors as Points and Arrows
> Each point $(a, b)$ of the plane is identified with the column vector $\begin{bmatrix} a \\ b \end{bmatrix}$, so $\mathbb{R}^2$ may be regarded as the set of all points in the plane, and $\mathbb{R}^3$ as the points of three-dimensional space. A vector is often drawn as an arrow from the origin to the point; the points along the arrow have no special significance. In this picture (the lecture's "geometry" column), $\mathbf{u} + \mathbf{v}$ is head-to-tail addition and $a\mathbf{v}$ stretches $\mathbf{v}$ by the factor $a$: the arrow for $c\mathbf{u}$ is $|c|$ times as long as the arrow for $\mathbf{u}$, pointing the same way if $c > 0$ and the opposite way if $c < 0$. The set of all multiples of one nonzero vector is a line through the origin. (In physics arrows represent forces and may be moved about; that interpretation returns in Chapter 4.)

^rem-4-1

> [!theorem] Theorem §5.1: Parallelogram Rule for Addition
> If $\mathbf{u}$ and $\mathbf{v}$ in $\mathbb{R}^2$ are represented as points in the plane, then $\mathbf{u} + \mathbf{v}$ corresponds to the fourth vertex of the parallelogram whose other vertices are $\mathbf{u}$, $\mathbf{0}$ and $\mathbf{v}$.
>
> *Lay: 1.3, Parallelogram Rule for Addition*

^thm-4-1

> [!proof]+ Proof
> Lay says this "can be verified by analytic geometry"; here is the verification. Consider the quadrilateral with vertices $\mathbf{0}$, $\mathbf{u}$, $\mathbf{u} + \mathbf{v}$, $\mathbf{v}$ in this order. The side from $\mathbf{u}$ to $\mathbf{u} + \mathbf{v}$ has displacement $(\mathbf{u} + \mathbf{v}) - \mathbf{u} = \mathbf{v}$, the same as the side from $\mathbf{0}$ to $\mathbf{v}$; the side from $\mathbf{v}$ to $\mathbf{u} + \mathbf{v}$ has displacement $\mathbf{u}$, the same as the side from $\mathbf{0}$ to $\mathbf{u}$. So opposite sides are parallel and of equal length, and the quadrilateral is a parallelogram (degenerate if $\mathbf{u}$, $\mathbf{v}$ lie on one line through $\mathbf{0}$). Its fourth vertex, opposite $\mathbf{0}$, is $\mathbf{u} + \mathbf{v}$.

^pf-4-1

*Uses:* [[§4 Vector Equations#^def-4-2|Def. §4.2]]

![[m235-3-1.svg]]
*(a) The parallelogram rule for $\mathbf{u} = (2, 2)$, $\mathbf{v} = (-6, 1)$: the sum $(-4, 3)$ is the vertex opposite $\mathbf{0}$ (Lay's Example 2). (b) For $\mathbf{v}_1 = (1, 2)$, $\mathbf{v}_2 = (3, 1)$ the lines through integer multiples of $\mathbf{v}_1$ (red, parallel to $\mathbf{v}_2$) and of $\mathbf{v}_2$ (blue, parallel to $\mathbf{v}_1$) form a grid of parallelograms; every point of the plane is some $a\mathbf{v}_1 + b\mathbf{v}_2$, read off on this skewed grid. The span of $\mathbf{v}_1, \mathbf{v}_2$ is all of $\mathbb{R}^2$.*

> [!theorem] Theorem §5.2: Algebraic Properties of ℝⁿ
> For all $\mathbf{u}, \mathbf{v}, \mathbf{w}$ in $\mathbb{R}^n$ and all scalars $c$ and $d$:
>
> $$
> \begin{array}{ll}
> \text{(i)}\ \ \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} & \text{(v)}\ \ c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v} \\
> \text{(ii)}\ \ (\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w}) & \text{(vi)}\ \ (c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u} \\
> \text{(iii)}\ \ \mathbf{u} + \mathbf{0} = \mathbf{0} + \mathbf{u} = \mathbf{u} & \text{(vii)}\ \ c(d\mathbf{u}) = (cd)\mathbf{u} \\
> \text{(iv)}\ \ \mathbf{u} + (-\mathbf{u}) = -\mathbf{u} + \mathbf{u} = \mathbf{0} & \text{(viii)}\ \ 1\mathbf{u} = \mathbf{u}
> \end{array}
> $$
>
> where $-\mathbf{u}$ denotes $(-1)\mathbf{u}$.
>
> *Lay: 1.3, Algebraic Properties of ℝⁿ*

^thm-4-2

> [!proof]+ Proof
> Lay leaves this to the reader (Practice Problem 1, Exercises 33–34): each property holds entry by entry, because it holds for real numbers. Two vectors are equal when their $i$th entries agree for every $i$, and the $i$th entry of each side is:
> - (i) $u_i + v_i = v_i + u_i$; (ii) $(u_i + v_i) + w_i = u_i + (v_i + w_i)$; (iii) $u_i + 0 = 0 + u_i = u_i$; (iv) $u_i + (-1)u_i = 0$;
> - (v) $c(u_i + v_i) = cu_i + cv_i$; (vi) $(c + d)u_i = cu_i + du_i$; (vii) $c(du_i) = (cd)u_i$; (viii) $1 \cdot u_i = u_i$.
>
> These are the commutative, associative, identity, inverse and distributive laws of real arithmetic.

^pf-4-2

*Uses:* [[§4 Vector Equations#^def-4-1|Def. §4.1]], [[§4 Vector Equations#^def-4-2|Def. §4.2]]

> [!remark]- Connections
> - The same eight properties for Stewart's $V_n$: [[§94 Vectors#^thm-94-5|Calc Thm. §94.5]]. Axler turns them into the definition of an abstract vector space ([[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]); Lay does the same in [[§29 Vector Spaces and Subspaces#^def-29-1|Definition §29.1]] (Section 4.1).

> [!example] Example §5.1: Computing with Vectors
> Let $\mathbf{u} = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$ and $\mathbf{v} = \begin{bmatrix} 2 \\ -5 \end{bmatrix}$. Then
>
> $$
> 4\mathbf{u} = \begin{bmatrix} 4 \\ -8 \end{bmatrix}, \qquad (-3)\mathbf{v} = \begin{bmatrix} -6 \\ 15 \end{bmatrix}, \qquad
> 4\mathbf{u} + (-3)\mathbf{v} = \begin{bmatrix} 4 - 6 \\ -8 + 15 \end{bmatrix} = \begin{bmatrix} -2 \\ 7 \end{bmatrix} .
> $$
>
> Geometrically, for $\mathbf{w} = \begin{bmatrix} 3 \\ -1 \end{bmatrix}$ the multiples $2\mathbf{w} = \begin{bmatrix} 6 \\ -2 \end{bmatrix}$ and $-\tfrac23\mathbf{w} = \begin{bmatrix} -2 \\ 2/3 \end{bmatrix}$ lie on the line through $\mathbf{0}$ and $\mathbf{w}$: the arrow for $2\mathbf{w}$ is twice as long as that of $\mathbf{w}$ and points the same way, the arrow for $-\tfrac23\mathbf{w}$ is two-thirds as long and points the opposite way. In $\mathbb{R}^3$, $\mathbf{a} = (2, 3, 4)$ and $2\mathbf{a} = (4, 6, 8)$ likewise lie on one line through the origin.
>
> *Lay: Examples 1.3.1 and 1.3.3*

^ex-4-1

## Linear Combinations

> [!definition] Definition §5.3: Linear Combination, Weights
> Given vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_p$ in $\mathbb{R}^n$ and scalars $c_1, c_2, \ldots, c_p$, the vector
>
> $$
> \mathbf{y} = c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p
> $$
>
> is a **linear combination** of $\mathbf{v}_1, \ldots, \mathbf{v}_p$ with **weights** $c_1, \ldots, c_p$. Property (ii) of [[§4 Vector Equations#^thm-4-2|Theorem §4.2]] allows the parentheses to be omitted. The weights can be any real numbers, including zero: $\sqrt3\,\mathbf{v}_1 + \mathbf{v}_2$, $\tfrac12\mathbf{v}_1$ ($= \tfrac12\mathbf{v}_1 + 0\mathbf{v}_2$) and $\mathbf{0}$ ($= 0\mathbf{v}_1 + 0\mathbf{v}_2$) are linear combinations of $\mathbf{v}_1$ and $\mathbf{v}_2$.
>
> *Lay: 1.3 (text)*

^def-4-3

> [!remark]- Connections
> - Rigorous treatment: [[§4 Span and Linear Independence#^ladr-2-2|LADR 2.2]] (linear combination of a list in any vector space $V$) and [[§4 Span and Linear Independence#^ladr-2-4|LADR 2.4]] (span); Axler also shows that the span is the smallest subspace containing the vectors ([[§4 Span and Linear Independence#^ladr-2-6|LADR 2.6]]), which Lay reaches in [[§21 Subspaces of ℝⁿ#^prop-21-1|Proposition §21.1]] and [[§29 Vector Spaces and Subspaces#^thm-29-4|Theorem §29.4]].

Geometrically, $c_1\mathbf{v}_1 + c_2\mathbf{v}_2$ gives instructions for traveling from the origin: $c_1$ units in the $\mathbf{v}_1$ direction, then $c_2$ units parallel to $\mathbf{v}_2$. On the skewed grid of Figure (b) above, the weights can be read off. With $\mathbf{v}_1 = (-1, 1)$ and $\mathbf{v}_2 = (2, 1)$, Lay reads off $\mathbf{u} = 3\mathbf{v}_1 - 2\mathbf{v}_2$ from such a grid and estimates a point $\mathbf{w}$ between grid lines as $\mathbf{w} \approx \tfrac52\mathbf{v}_1 - \tfrac12\mathbf{v}_2$ (Lay's Example 4).

> [!theorem] Theorem §5.3: Vector Equations Are Linear Systems
> A vector equation
>
> $$
> x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n = \mathbf{b}
> $$
>
> has the same solution set as the linear system whose augmented matrix is
>
> $$
> [\,\mathbf{a}_1\ \ \mathbf{a}_2\ \ \cdots\ \ \mathbf{a}_n\ \ \mathbf{b}\,] . \qquad (5)
> $$
>
> In particular, $\mathbf{b}$ can be generated by a linear combination of $\mathbf{a}_1, \ldots, \mathbf{a}_n$ if and only if there exists a solution to the linear system corresponding to the matrix (5).
>
> *Lay: 1.3, boxed statement*

^thm-4-3

> [!proof]+ Proof
> Let $\mathbf{a}_j$ have entries $a_{1j}, \ldots, a_{mj}$ and $\mathbf{b}$ have entries $b_1, \ldots, b_m$. By the definitions of scalar multiplication and addition ([[§4 Vector Equations#^def-4-2|Definition §4.2]]), the left side of the vector equation is the vector whose $i$th entry is $a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n$. Two vectors are equal exactly when their corresponding entries are equal, so $(x_1, \ldots, x_n)$ satisfies the vector equation if and only if
>
> $$
> a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = b_i \qquad (i = 1, \ldots, m),
> $$
>
> which is the linear system whose augmented matrix has $i$th row $[\,a_{i1}\ \cdots\ a_{in}\ \ b_i\,]$, that is, the matrix (5) with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n, \mathbf{b}$. The last sentence restates the first: a solution $(x_1, \ldots, x_n)$ is exactly a list of weights with $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = \mathbf{b}$.

^pf-4-3

*Uses:* [[§4 Vector Equations#^def-4-1|Def. §4.1]], [[§4 Vector Equations#^def-4-2|Def. §4.2]], [[§1 Systems of Linear Equations#^def-1-7|Def. §1.7]]

The augmented matrix can be written down at once: put the vectors into the columns in the order in which they appear in the vector equation.

> [!definition] Definition §5.4: Span
> If $\mathbf{v}_1, \ldots, \mathbf{v}_p$ are in $\mathbb{R}^n$, the set of all linear combinations of $\mathbf{v}_1, \ldots, \mathbf{v}_p$ is denoted $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ and is called the **subset of $\mathbb{R}^n$ spanned** (or **generated**) **by** $\mathbf{v}_1, \ldots, \mathbf{v}_p$. That is, $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is the collection of all vectors that can be written in the form
>
> $$
> c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_p\mathbf{v}_p
> $$
>
> with $c_1, \ldots, c_p$ scalars. The lecture calls it the **linear span**.
>
> *Lay: 1.3, Definition*

^def-4-4

By [[§4 Vector Equations#^thm-4-3|Theorem §4.3]], asking whether $\mathbf{b}$ is in $\operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ amounts to asking whether the vector equation $x_1\mathbf{v}_1 + \cdots + x_p\mathbf{v}_p = \mathbf{b}$ has a solution, or equivalently whether the linear system with augmented matrix $[\,\mathbf{v}_1\ \cdots\ \mathbf{v}_p\ \ \mathbf{b}\,]$ is consistent. The span contains every scalar multiple of each $\mathbf{v}_j$ (for example $c\mathbf{v}_1 = c\mathbf{v}_1 + 0\mathbf{v}_2 + \cdots + 0\mathbf{v}_p$), and in particular it contains $\mathbf{0}$.

> [!theorem] Proposition §5.4: Sums and Multiples Stay in the Span
> If $\mathbf{u}$ and $\mathbf{v}$ are in $\operatorname{Span}\{\mathbf{w}_1, \ldots, \mathbf{w}_p\}$, then so are $\mathbf{u} + \mathbf{v}$ and $c\mathbf{u}$ for every scalar $c$.
>
> *Lay: 1.3, Practice Problem 3*

^prop-4-4

> [!proof]+ Proof
> By [[§4 Vector Equations#^def-4-4|Definition §4.4]] there are scalars $c_1, \ldots, c_p$ and $d_1, \ldots, d_p$ with $\mathbf{u} = c_1\mathbf{w}_1 + \cdots + c_p\mathbf{w}_p$ and $\mathbf{v} = d_1\mathbf{w}_1 + \cdots + d_p\mathbf{w}_p$. Regrouping by the algebraic properties of $\mathbb{R}^n$ (commutativity, associativity and property (vi)),
>
> $$
> \mathbf{u} + \mathbf{v} = (c_1 + d_1)\mathbf{w}_1 + \cdots + (c_p + d_p)\mathbf{w}_p ,
> $$
>
> and $c_1 + d_1, \ldots, c_p + d_p$ are scalars, so $\mathbf{u} + \mathbf{v}$ is in the span. (Lay's solution does this for $p = 3$.) Likewise, by properties (v) and (vii), $c\mathbf{u} = (cc_1)\mathbf{w}_1 + \cdots + (cc_p)\mathbf{w}_p$ is in the span.

^pf-4-4

*Uses:* [[§4 Vector Equations#^def-4-4|Def. §4.4]], [[§4 Vector Equations#^thm-4-2|§4.2]]

These two closure properties are what will make every span a *subspace* ([[§21 Subspaces of ℝⁿ#^prop-21-1|Proposition §21.1]]).

> [!remark] Remark: A Geometric Description of Span{v} and Span{u, v}
> - **One vector.** If $\mathbf{v} \ne \mathbf{0}$ in $\mathbb{R}^3$ (or $\mathbb{R}^2$), $\operatorname{Span}\{\mathbf{v}\}$ is the set of all scalar multiples of $\mathbf{v}$: the line through $\mathbf{0}$ in the direction of $\mathbf{v}$. ($\operatorname{Span}\{\mathbf{0}\} = \{\mathbf{0}\}$.)
> - **Two vectors.** If $\mathbf{u}$ and $\mathbf{v}$ are nonzero vectors in $\mathbb{R}^3$ and $\mathbf{v}$ is not a multiple of $\mathbf{u}$, then $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$ is the plane through $\mathbf{0}$ that contains $\mathbf{u}$ and $\mathbf{v}$ (and so contains the lines through $\mathbf{0}$ and $\mathbf{u}$ and through $\mathbf{0}$ and $\mathbf{v}$). If instead the two vectors are proportional, the span is only the line through $\mathbf{0}$ in their common direction.
>
> In the plane (lecture): $\mathbf{v}_1 = (1, 2)$ and $\mathbf{v}_2 = (3, 1)$ are not proportional, and the combinations $a\mathbf{v}_1 + b\mathbf{v}_2$, with $a$ and $b$ any numbers, fill the whole plane (Figure (b) above). But for $\mathbf{v}_1 = (1, 2)$ and $\mathbf{v}_2 = (-2, -4) = -2\mathbf{v}_1$, the span is just the line in the direction $(1, 2)$.
>
> *Source: 235 lecture L3*

^rem-4-2

> [!example] Example §5.2: In the Span or Not?
> **(a)** Is $\mathbf{b} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ a linear combination of $\mathbf{v} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ and $\mathbf{w} = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$?
>
> We need $x, y$ with $x\mathbf{v} + y\mathbf{w} = \mathbf{b}$, that is, $x + 4y = 1$, $2x + 5y = 1$, $3x + 6y = 1$. Row reduce $[\,\mathbf{v}\ \ \mathbf{w}\ \ \mathbf{b}\,]$:
>
> $$
> \begin{bmatrix} 1 & 4 & 1 \\ 2 & 5 & 1 \\ 3 & 6 & 1 \end{bmatrix}
> \xrightarrow[R_3 - 3R_1]{R_2 - 2R_1}
> \begin{bmatrix} 1 & 4 & 1 \\ 0 & -3 & -1 \\ 0 & -6 & -2 \end{bmatrix}
> \xrightarrow{R_3 - 2R_2}
> \begin{bmatrix} 1 & 4 & 1 \\ 0 & -3 & -1 \\ 0 & 0 & 0 \end{bmatrix}
> \xrightarrow[R_1 - 4R_2]{-\frac13 R_2}
> \begin{bmatrix} 1 & 0 & -1/3 \\ 0 & 1 & 1/3 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> No bad row ([[§3 Solutions of Linear Systems#^thm-3-1|Theorem §3.1]]), so yes: $x = -\tfrac13$, $y = \tfrac13$, and
>
> $$
> \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = -\frac13\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \frac13\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}
> \qquad \big(\text{check: } \tfrac{-1 + 4}{3} = \tfrac{-2 + 5}{3} = \tfrac{-3 + 6}{3} = 1\big).
> $$
>
> (Lay's Example 5 is of the same kind: $\mathbf{b} = (7, 4, -3)$ is $3\mathbf{a}_1 + 2\mathbf{a}_2$ for $\mathbf{a}_1 = (1, -2, -5)$, $\mathbf{a}_2 = (2, 5, 6)$.)
>
> **(b)** Let $\mathbf{a}_1 = \begin{bmatrix} 1 \\ -2 \\ 3 \end{bmatrix}$, $\mathbf{a}_2 = \begin{bmatrix} 5 \\ -13 \\ -3 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} -3 \\ 8 \\ 1 \end{bmatrix}$. Then $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_2\}$ is a plane through the origin in $\mathbb{R}^3$ ($\mathbf{a}_2$ is not a multiple of $\mathbf{a}_1$). Is $\mathbf{b}$ in that plane?
>
> $$
> \begin{bmatrix} 1 & 5 & -3 \\ -2 & -13 & 8 \\ 3 & -3 & 1 \end{bmatrix}
> \xrightarrow[R_3 - 3R_1]{R_2 + 2R_1}
> \begin{bmatrix} 1 & 5 & -3 \\ 0 & -3 & 2 \\ 0 & -18 & 10 \end{bmatrix}
> \xrightarrow{R_3 - 6R_2}
> \begin{bmatrix} 1 & 5 & -3 \\ 0 & -3 & 2 \\ 0 & 0 & -2 \end{bmatrix} .
> $$
>
> The third equation is $0 = -2$: the system has no solution, so $\mathbf{b}$ is *not* in $\operatorname{Span}\{\mathbf{a}_1, \mathbf{a}_2\}$.
>
> *Lay: Examples 1.3.5 and 1.3.6*
> *Source: 235 lecture L2*

^ex-4-2

> [!example] Example §5.3: Weights Need Not Be Unique
> Let $\mathbf{b} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$, $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 1/2 \\ 0 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} 1 \\ 1/2 \end{bmatrix}$. Then
>
> $$
> \mathbf{b} = 1 \cdot \mathbf{v}_1 + 2\mathbf{v}_2 \quad (\ast), \qquad \mathbf{b} = 2\mathbf{v}_3 \quad (\ast\ast),
> $$
>
> so $\mathbf{b}$ is a linear combination of $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ in at least two ways: $1\mathbf{v}_1 + 2\mathbf{v}_2 + 0\mathbf{v}_3$ and $0\mathbf{v}_1 + 0\mathbf{v}_2 + 2\mathbf{v}_3$. Mixing them gives more: $\tfrac13(\ast) + \tfrac23(\ast\ast)$ yields $\big(\tfrac13 + \tfrac23\big)\mathbf{b} = \mathbf{b} = \tfrac13\mathbf{v}_1 + \tfrac23\mathbf{v}_2 + \tfrac43\mathbf{v}_3$. **Check:** $\tfrac13 + \tfrac13 + \tfrac43 = 2$ and $\tfrac13 + 0 + \tfrac23 = 1$. In terms of [[§4 Vector Equations#^thm-4-3|Theorem §4.3]]: the system with augmented matrix $[\,\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_3\ \mathbf{b}\,]$ has 2 equations and 3 unknowns, so it has a free variable and, being consistent, infinitely many solutions. Uniqueness of weights is the subject of [[§8 Linear Independence|§8]].
>
> *The lecture writes the weight of $\mathbf{v}_3$ in the mixed combination as $\tfrac23$; it is $\tfrac23 \cdot 2 = \tfrac43$, as the check confirms.*
>
> *Source: 235 lecture L3*

^ex-4-3

## Linear Combinations in Applications

> [!example] Example §4.4: Costs per Dollar of Income
> A company manufactures two products. For \$1.00 worth of product B, it spends \$.45 on materials, \$.25 on labor and \$.15 on overhead; for \$1.00 worth of product C, \$.40 on materials, \$.30 on labor and \$.15 on overhead. The "costs per dollar of income" are
>
> $$
> \mathbf{b} = \begin{bmatrix} .45 \\ .25 \\ .15 \end{bmatrix}, \qquad \mathbf{c} = \begin{bmatrix} .40 \\ .30 \\ .15 \end{bmatrix} .
> $$
>
> **(a)** $100\mathbf{b} = (45, 25, 15)$ lists the costs of producing \$100 worth of product B: \$45 for materials, \$25 for labor and \$15 for overhead. The principle is (number of units) $\cdot$ (cost per unit) $=$ (total cost).
>
> **(b)** Producing $x_1$ dollars worth of B and $x_2$ dollars worth of C costs $x_1\mathbf{b}$ and $x_2\mathbf{c}$, so the total costs (materials, labor, overhead) are the linear combination $x_1\mathbf{b} + x_2\mathbf{c}$.
>
> *Lay: Example 1.3.7*

^ex-4-4
