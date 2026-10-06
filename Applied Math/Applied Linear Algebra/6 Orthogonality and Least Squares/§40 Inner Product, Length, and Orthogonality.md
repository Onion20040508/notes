---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 40
lay: "6.1"
aliases: ["Lay 6.1"]
tags: [applied-linear-algebra, math235]
---
← [[§39 Iterative Estimates for Eigenvalues]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§40a Orthogonal Complements and Angles]] →

*Lay, Section 6.1 · MATH 235 lecture L22.*

Length, distance and perpendicularity, familiar in $\mathbb{R}^2$ and $\mathbb{R}^3$, all come from one algebraic operation: the inner product $\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T\mathbf{v}$. This section defines the three notions in $\mathbb{R}^n$, proves the Pythagorean Theorem, and introduces the orthogonal complement $W^\perp$ of a subspace. The main theorem says that the row space and the null space of a matrix are orthogonal complements, and so are the column space and the null space of the transpose. Everything in Chapter 6, up to least-squares solutions of inconsistent systems, is built on these ideas.

## The Inner Product

> [!definition] Definition §40.1: Inner Product
> Regard vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ as $n \times 1$ matrices. Then $\mathbf{u}^T$ is $1 \times n$, and the matrix product $\mathbf{u}^T\mathbf{v}$ is $1 \times 1$; we write it as a scalar without brackets. This number is the **inner product** (or **dot product**) of $\mathbf{u}$ and $\mathbf{v}$, written $\mathbf{u} \cdot \mathbf{v}$. If $\mathbf{u} = (u_1, \ldots, u_n)$ and $\mathbf{v} = (v_1, \ldots, v_n)$, then
>
> $$
> \mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T\mathbf{v} = \begin{bmatrix} u_1 & u_2 & \cdots & u_n \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = u_1v_1 + u_2v_2 + \cdots + u_nv_n .
> $$
>
> So the inner product is a special case of matrix multiplication: a $(1 \times n)$ matrix times an $(n \times 1)$ matrix gives a $(1 \times 1)$ matrix.
>
> *Lay: 6.1 (text)*

^def-40-1

> [!remark]- Connections
> - In $\mathbb{R}^2$ and $\mathbb{R}^3$ this is Stewart's dot product, [[§82 The Dot Product#^def-82-1|Calc Def. §82.1]], with the same properties [[§82 The Dot Product#^thm-82-1|Calc Thm. §82.1]].
> - Rigorous treatment: [[§19 Inner Products and Norms#^ladr-6-1|LADR 6.1]] (dot product on $\mathbb{R}^n$) and [[§19 Inner Products and Norms#^ladr-6-2|LADR 6.2]], where the properties of [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|Theorem §40.1]] become the axioms of an inner product on any vector space, over $\mathbb{R}$ or $\mathbb{C}$ (here: [[§46 Inner Product Spaces#^def-46-1|Definition §46.1]]).
> - See also: for vectors with complex entries BDP distinguishes $\mathbf{x}^T\mathbf{y}$ from the inner product $(\mathbf{x}, \mathbf{y}) = \mathbf{x}^T\overline{\mathbf{y}}$, which gives the length and orthogonality, [[§28 Matrices#^def-28-3|331 Def. §28.3]], [[§28 Matrices#^prop-28-2|331 Prop. §28.2]]; the two products compared on an example, [[§28 Matrices#^ex-28-2|331 Ex. §28.2]].

> [!example] Example §40.1: Computing Inner Products
> **(a)** For $\mathbf{v} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$ and $\mathbf{w} = \begin{bmatrix} -1 \\ 7 \end{bmatrix}$,
>
> $$
> \mathbf{v} \cdot \mathbf{w} = 5(-1) + 3 \cdot 7 = -5 + 21 = 16, \qquad\text{or as a matrix product}\qquad \begin{bmatrix} 5 & 3 \end{bmatrix} \begin{bmatrix} -1 \\ 7 \end{bmatrix} = \begin{bmatrix} 16 \end{bmatrix} .
> $$
>
> **(b)** For $\mathbf{u} = \begin{bmatrix} 2 \\ -5 \\ -1 \end{bmatrix}$ and $\mathbf{v} = \begin{bmatrix} 3 \\ 2 \\ -3 \end{bmatrix}$,
>
> $$
> \begin{aligned}
> \mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T\mathbf{v} &= (2)(3) + (-5)(2) + (-1)(-3) = 6 - 10 + 3 = -1, \\
> \mathbf{v} \cdot \mathbf{u} = \mathbf{v}^T\mathbf{u} &= (3)(2) + (2)(-5) + (-3)(-1) = 6 - 10 + 3 = -1 .
> \end{aligned}
> $$
>
> The two sums have the same terms in the same order, with the factors of each term swapped. This is why $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ in general.
>
> *Lay: Example 6.1.1*
> *Source: 235 lecture L22*

^ex-40-1

> [!theorem] Theorem §40.1: Properties of the Inner Product
> Let $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ be vectors in $\mathbb{R}^n$ and $c$ a scalar. Then
>
> a. $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$
>
> b. $(\mathbf{u} + \mathbf{v}) \cdot \mathbf{w} = \mathbf{u} \cdot \mathbf{w} + \mathbf{v} \cdot \mathbf{w}$
>
> c. $(c\mathbf{u}) \cdot \mathbf{v} = c(\mathbf{u} \cdot \mathbf{v}) = \mathbf{u} \cdot (c\mathbf{v})$
>
> d. $\mathbf{u} \cdot \mathbf{u} \ge 0$, and $\mathbf{u} \cdot \mathbf{u} = 0$ if and only if $\mathbf{u} = \mathbf{0}$.
>
> Combining (b) and (c) several times gives the rule
>
> $$
> (c_1\mathbf{u}_1 + \cdots + c_p\mathbf{u}_p) \cdot \mathbf{w} = c_1(\mathbf{u}_1 \cdot \mathbf{w}) + \cdots + c_p(\mathbf{u}_p \cdot \mathbf{w}) .
> $$
>
> *Lay: Theorem 1 (6.1)*

^thm-40-1

> [!proof]+ Proof
> Lay deduces these from the properties of the transpose (Exercises 21 and 22).
>
> (a) $\mathbf{u}^T\mathbf{v}$ is a $1 \times 1$ matrix, so it equals its own transpose: $\mathbf{u}^T\mathbf{v} = (\mathbf{u}^T\mathbf{v})^T = \mathbf{v}^T(\mathbf{u}^T)^T = \mathbf{v}^T\mathbf{u}$.
>
> (b) $(\mathbf{u} + \mathbf{v})^T\mathbf{w} = (\mathbf{u}^T + \mathbf{v}^T)\mathbf{w} = \mathbf{u}^T\mathbf{w} + \mathbf{v}^T\mathbf{w}$, by $(A + B)^T = A^T + B^T$ and the distributive law for matrix products.
>
> (c) $(c\mathbf{u})^T\mathbf{v} = (c\,\mathbf{u}^T)\mathbf{v} = c(\mathbf{u}^T\mathbf{v})$, and likewise $\mathbf{u}^T(c\mathbf{v}) = c(\mathbf{u}^T\mathbf{v})$, since scalars move through matrix products.
>
> (d) $\mathbf{u} \cdot \mathbf{u} = u_1^2 + \cdots + u_n^2$ is a sum of squares of real numbers, so it is $\ge 0$. It is $0$ exactly when every $u_i^2 = 0$, that is, when every $u_i = 0$.
>
> The rule for linear combinations follows from (b) by induction on $p$ (split off the last term), and then (c) pulls out each $c_i$.

^pf-40-1

*Uses:* [[§11 Matrix Operations#^thm-11-6|§11.6]] (properties of matrix multiplication), [[§11 Matrix Operations#^thm-11-7|§11.7]] (properties of the transpose)

## The Length of a Vector

> [!definition] Definition §40.2: Length (Norm)
> The **length** (or **norm**) of $\mathbf{v} \in \mathbb{R}^n$ is the nonnegative scalar
>
> $$
> \|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}, \qquad\text{so}\qquad \|\mathbf{v}\|^2 = \mathbf{v} \cdot \mathbf{v} .
> $$
>
> The square root exists because $\mathbf{v} \cdot \mathbf{v} \ge 0$ ([[§40 Inner Product, Length, and Orthogonality#^thm-40-1|Theorem §40.1]](d)). For $\mathbf{v} = (a, b) \in \mathbb{R}^2$, $\|\mathbf{v}\| = \sqrt{a^2 + b^2}$ is the length of the segment from the origin to the point $(a, b)$, by the Pythagorean Theorem of plane geometry; the diagonal of a box gives the same in $\mathbb{R}^3$.
>
> *Lay: 6.1, Definition*

^def-40-2

> [!theorem] Proposition §40.2: Length of a Scalar Multiple
> For every $\mathbf{v} \in \mathbb{R}^n$ and every scalar $c$,
>
> $$
> \|c\mathbf{v}\| = |c|\,\|\mathbf{v}\| .
> $$
>
> *Lay: 6.1 (text)*

^prop-40-2

> [!proof]+ Proof
> By [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|Theorem §40.1]](c), used twice, $\|c\mathbf{v}\|^2 = (c\mathbf{v}) \cdot (c\mathbf{v}) = c^2\,(\mathbf{v} \cdot \mathbf{v}) = c^2\|\mathbf{v}\|^2$. Both $\|c\mathbf{v}\|$ and $|c|\,\|\mathbf{v}\|$ are nonnegative, and $\sqrt{c^2} = |c|$, so taking square roots gives the claim.

^pf-40-2

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§40 Inner Product, Length, and Orthogonality#^def-40-2|Def. §40.2]]

> [!definition] Definition §40.3: Unit Vector; Normalizing
> A **unit vector** is a vector of length $1$. If $\mathbf{v} \ne \mathbf{0}$, then
>
> $$
> \mathbf{u} = \frac{1}{\|\mathbf{v}\|}\,\mathbf{v}
> $$
>
> is a unit vector, since $\|\mathbf{u}\| = \frac{1}{\|\mathbf{v}\|}\|\mathbf{v}\| = 1$ by [[§40 Inner Product, Length, and Orthogonality#^prop-40-2|Proposition §40.2]]. Passing from $\mathbf{v}$ to $\mathbf{u}$ is called **normalizing** $\mathbf{v}$, and $\mathbf{u}$ is said to be *in the same direction* as $\mathbf{v}$.
>
> *Lay: 6.1 (text)*

^def-40-3

> [!example] Example §40.2: Normalizing a Vector
> **(a)** Find a unit vector $\mathbf{u}$ in the same direction as $\mathbf{v} = (1, -2, 2, 0)$.
>
> $$
> \|\mathbf{v}\|^2 = \mathbf{v} \cdot \mathbf{v} = 1^2 + (-2)^2 + 2^2 + 0^2 = 9, \qquad \|\mathbf{v}\| = 3, \qquad
> \mathbf{u} = \frac{1}{3}\mathbf{v} = \begin{bmatrix} 1/3 \\ -2/3 \\ 2/3 \\ 0 \end{bmatrix} .
> $$
>
> Check: $\|\mathbf{u}\|^2 = \frac19 + \frac49 + \frac49 + 0 = 1$. (Checking $\|\mathbf{u}\|^2 = 1$ avoids square roots.)
>
> **(b)** Let $W$ be the subspace of $\mathbb{R}^2$ spanned by $\mathbf{x} = (\frac23, 1)$. Find a unit vector $\mathbf{z}$ that is a basis for $W$.
>
> $W$ is the line of all multiples of $\mathbf{x}$, and any nonzero vector in $W$ is a basis for it. To avoid fractions, scale first: $\mathbf{y} = 3\mathbf{x} = (2, 3)$. Then $\|\mathbf{y}\|^2 = 4 + 9 = 13$ and
>
> $$
> \mathbf{z} = \frac{1}{\sqrt{13}}\begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 2/\sqrt{13} \\ 3/\sqrt{13} \end{bmatrix} .
> $$
>
> The only other unit vector in $W$ is $-\mathbf{z} = (-2/\sqrt{13}, -3/\sqrt{13})$.
>
> *Lay: Examples 6.1.2 and 6.1.3*

^ex-40-2

## Distance in ℝⁿ

> [!definition] Definition §40.4: Distance
> For $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, the **distance between $\mathbf{u}$ and $\mathbf{v}$** is the length of $\mathbf{u} - \mathbf{v}$:
>
> $$
> \operatorname{dist}(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\| .
> $$
>
> In $\mathbb{R}$ this is the usual $|a - b|$. In $\mathbb{R}^n$,
>
> $$
> \operatorname{dist}(\mathbf{u}, \mathbf{v})^2 = (u_1 - v_1)^2 + \cdots + (u_n - v_n)^2 ,
> $$
>
> which for $n = 2, 3$ is the Euclidean distance formula: a multidimensional Pythagorean Theorem.
>
> *Lay: 6.1, Definition; Example 6.1.5*

^def-40-4

> [!example] Example §40.3: The Distance Between Two Vectors
> Compute the distance between $\mathbf{u} = (7, 1)$ and $\mathbf{v} = (3, 2)$.
>
> $$
> \mathbf{u} - \mathbf{v} = \begin{bmatrix} 7 \\ 1 \end{bmatrix} - \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ -1 \end{bmatrix}, \qquad \|\mathbf{u} - \mathbf{v}\| = \sqrt{4^2 + (-1)^2} = \sqrt{17} .
> $$
>
> Since $\mathbf{v} + (\mathbf{u} - \mathbf{v}) = \mathbf{u}$, the points $\mathbf{0}$, $\mathbf{v}$, $\mathbf{u}$, $\mathbf{u} - \mathbf{v}$ form a parallelogram, and the distance from $\mathbf{u}$ to $\mathbf{v}$ equals the distance from $\mathbf{u} - \mathbf{v}$ to $\mathbf{0}$.
>
> *Lay: Example 6.1.4*

^ex-40-3

## Orthogonal Vectors

> [!theorem] Proposition §40.3: Length of a Sum and of a Difference
> For all $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$,
>
> $$
> \|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\,\mathbf{u} \cdot \mathbf{v}, \qquad
> \|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\,\mathbf{u} \cdot \mathbf{v} .
> $$
>
> *Lay: 6.1, Equation (1)*

^prop-40-3

> [!proof]+ Proof
> By [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|Theorem §40.1]](b) (and (a) to use it in the second slot),
>
> $$
> \begin{aligned}
> \|\mathbf{u} + \mathbf{v}\|^2 = (\mathbf{u} + \mathbf{v}) \cdot (\mathbf{u} + \mathbf{v})
> &= \mathbf{u} \cdot (\mathbf{u} + \mathbf{v}) + \mathbf{v} \cdot (\mathbf{u} + \mathbf{v}) \\
> &= \mathbf{u} \cdot \mathbf{u} + \mathbf{u} \cdot \mathbf{v} + \mathbf{v} \cdot \mathbf{u} + \mathbf{v} \cdot \mathbf{v}
> = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\,\mathbf{u} \cdot \mathbf{v} ,
> \end{aligned}
> $$
>
> using $\mathbf{v} \cdot \mathbf{u} = \mathbf{u} \cdot \mathbf{v}$ in the last step. Replacing $\mathbf{v}$ by $-\mathbf{v}$, and using $\|-\mathbf{v}\| = \|\mathbf{v}\|$ and $\mathbf{u} \cdot (-\mathbf{v}) = -\mathbf{u} \cdot \mathbf{v}$ ([[§40 Inner Product, Length, and Orthogonality#^thm-40-1|Theorem §40.1]](c)), gives the second formula.

^pf-40-3

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§40 Inner Product, Length, and Orthogonality#^prop-40-2|§40.2]]

> [!remark] Remark: Why the Inner Product Detects Right Angles
> In $\mathbb{R}^2$ or $\mathbb{R}^3$, the lines through $\mathbf{0}$ and $\mathbf{u}$ and through $\mathbf{0}$ and $\mathbf{v}$ are perpendicular exactly when $\mathbf{u}$ is as far from $\mathbf{v}$ as from $-\mathbf{v}$: the points equidistant from $\mathbf{v}$ and $-\mathbf{v}$ form the perpendicular bisector of the segment from $-\mathbf{v}$ to $\mathbf{v}$, which is the line (or plane) through $\mathbf{0}$ perpendicular to $\mathbf{v}$. By [[§40 Inner Product, Length, and Orthogonality#^prop-40-3|Proposition §40.3]],
>
> $$
> \operatorname{dist}(\mathbf{u}, -\mathbf{v})^2 = \|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\,\mathbf{u} \cdot \mathbf{v}, \qquad
> \operatorname{dist}(\mathbf{u}, \mathbf{v})^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\,\mathbf{u} \cdot \mathbf{v} .
> $$
>
> These are equal if and only if $2\,\mathbf{u} \cdot \mathbf{v} = -2\,\mathbf{u} \cdot \mathbf{v}$, that is, $\mathbf{u} \cdot \mathbf{v} = 0$. So in the plane and in space, perpendicularity means $\mathbf{u} \cdot \mathbf{v} = 0$; [[§40 Inner Product, Length, and Orthogonality#^def-40-5|Definition §40.5]] takes this as the definition in $\mathbb{R}^n$.

^rem-40-1

> [!definition] Definition §40.5: Orthogonal Vectors
> Two vectors $\mathbf{u}$ and $\mathbf{v}$ in $\mathbb{R}^n$ are **orthogonal** (to each other) if $\mathbf{u} \cdot \mathbf{v} = 0$.
>
> The zero vector is orthogonal to every vector, since $\mathbf{0}^T\mathbf{v} = 0$.
>
> *Lay: 6.1, Definition*

^def-40-5

> [!theorem] Theorem §40.4: The Pythagorean Theorem
> Two vectors $\mathbf{u}$ and $\mathbf{v}$ are orthogonal if and only if
>
> $$
> \|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 .
> $$
>
> *Lay: Theorem 2 (6.1)*

^thm-40-4

> [!proof]+ Proof
> By [[§40 Inner Product, Length, and Orthogonality#^prop-40-3|Proposition §40.3]], $\|\mathbf{u} + \mathbf{v}\|^2 - \|\mathbf{u}\|^2 - \|\mathbf{v}\|^2 = 2\,\mathbf{u} \cdot \mathbf{v}$. This is $0$ if and only if $\mathbf{u} \cdot \mathbf{v} = 0$, that is, if and only if $\mathbf{u}$ and $\mathbf{v}$ are orthogonal.
>
> (The lecture used the difference instead: for the right triangle with legs $\mathbf{u}$, $\mathbf{v}$ and hypotenuse $\mathbf{u} - \mathbf{v}$, the second formula of [[§40 Inner Product, Length, and Orthogonality#^prop-40-3|Proposition §40.3]] gives $\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$ when $\mathbf{u} \cdot \mathbf{v} = 0$. It left as an exercise to recover the school formula $b = c\cos\varphi$ for a right triangle with leg $b$, hypotenuse $c$ and angle $\varphi$ between them: with legs $\mathbf{u} \perp \mathbf{v}$ and hypotenuse $\mathbf{h} = \mathbf{u} + \mathbf{v}$, [[§40 Inner Product, Length, and Orthogonality#^thm-40-9|Theorem §40.9]] gives $\|\mathbf{h}\|\,\|\mathbf{v}\|\cos\varphi = \mathbf{h} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{v} + \mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2$, so $\|\mathbf{v}\| = \|\mathbf{h}\|\cos\varphi$.)

^pf-40-4

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^prop-40-3|§40.3]], [[§40 Inner Product, Length, and Orthogonality#^def-40-5|Def. §40.5]]

> [!remark]- Connections
> - Rigorous treatment: [[§19 Inner Products and Norms#^ladr-6-12|LADR 6.12]], for any inner product space; Axler states only the direction "orthogonal $\Rightarrow$ the identity". The converse holds over $\mathbb{R}$ by the same computation, but fails over $\mathbb{C}$, where the identity says only $\operatorname{Re}\langle u, v \rangle = 0$.
> - Hilbert-space version, with its extension to finitely many orthonormal vectors: [[§24 Orthonormal Sets and Bases#^lem-24-1|556 Lem. §24.1]].

*Continued in [[§40a Orthogonal Complements and Angles]]: orthogonal complements, the fundamental subspaces as orthogonal complements, and angles in ℝ² and ℝ³.*
