---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 40
lay: "6.1"
aliases: ["Lay 6.1"]
tags: [applied-linear-algebra, math235]
---
← [[§39 Iterative Estimates for Eigenvalues]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§41 Orthogonal Sets]] →

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
> - Rigorous treatment: [[§19 Inner Products and Norms#^ladr-6-1|LADR 6.1]] (dot product on $\mathbb{R}^n$) and [[§19 Inner Products and Norms#^ladr-6-2|LADR 6.2]], where the properties of Theorem §40.1 become the axioms of an inner product on any vector space, over $\mathbb{R}$ or $\mathbb{C}$ (here: [[§46 Inner Product Spaces#^def-46-1|Definition §46.1]]).
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
> The square root exists because $\mathbf{v} \cdot \mathbf{v} \ge 0$ (Theorem §40.1(d)). For $\mathbf{v} = (a, b) \in \mathbb{R}^2$, $\|\mathbf{v}\| = \sqrt{a^2 + b^2}$ is the length of the segment from the origin to the point $(a, b)$, by the Pythagorean Theorem of plane geometry; the diagonal of a box gives the same in $\mathbb{R}^3$.
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
> By Theorem §40.1(c), used twice, $\|c\mathbf{v}\|^2 = (c\mathbf{v}) \cdot (c\mathbf{v}) = c^2\,(\mathbf{v} \cdot \mathbf{v}) = c^2\|\mathbf{v}\|^2$. Both $\|c\mathbf{v}\|$ and $|c|\,\|\mathbf{v}\|$ are nonnegative, and $\sqrt{c^2} = |c|$, so taking square roots gives the claim.

^pf-40-2

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§40 Inner Product, Length, and Orthogonality#^def-40-2|Def. §40.2]]

> [!definition] Definition §40.3: Unit Vector; Normalizing
> A **unit vector** is a vector of length $1$. If $\mathbf{v} \ne \mathbf{0}$, then
>
> $$
> \mathbf{u} = \frac{1}{\|\mathbf{v}\|}\,\mathbf{v}
> $$
>
> is a unit vector, since $\|\mathbf{u}\| = \frac{1}{\|\mathbf{v}\|}\|\mathbf{v}\| = 1$ by Proposition §40.2. Passing from $\mathbf{v}$ to $\mathbf{u}$ is called **normalizing** $\mathbf{v}$, and $\mathbf{u}$ is said to be *in the same direction* as $\mathbf{v}$.
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
> By Theorem §40.1(b) (and (a) to use it in the second slot),
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
> using $\mathbf{v} \cdot \mathbf{u} = \mathbf{u} \cdot \mathbf{v}$ in the last step. Replacing $\mathbf{v}$ by $-\mathbf{v}$, and using $\|-\mathbf{v}\| = \|\mathbf{v}\|$ and $\mathbf{u} \cdot (-\mathbf{v}) = -\mathbf{u} \cdot \mathbf{v}$ (Theorem §40.1(c)), gives the second formula.

^pf-40-3

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§40 Inner Product, Length, and Orthogonality#^prop-40-2|§40.2]]

> [!remark] Remark: Why the Inner Product Detects Right Angles
> In $\mathbb{R}^2$ or $\mathbb{R}^3$, the lines through $\mathbf{0}$ and $\mathbf{u}$ and through $\mathbf{0}$ and $\mathbf{v}$ are perpendicular exactly when $\mathbf{u}$ is as far from $\mathbf{v}$ as from $-\mathbf{v}$: the points equidistant from $\mathbf{v}$ and $-\mathbf{v}$ form the perpendicular bisector of the segment from $-\mathbf{v}$ to $\mathbf{v}$, which is the line (or plane) through $\mathbf{0}$ perpendicular to $\mathbf{v}$. By Proposition §40.3,
>
> $$
> \operatorname{dist}(\mathbf{u}, -\mathbf{v})^2 = \|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\,\mathbf{u} \cdot \mathbf{v}, \qquad
> \operatorname{dist}(\mathbf{u}, \mathbf{v})^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\,\mathbf{u} \cdot \mathbf{v} .
> $$
>
> These are equal if and only if $2\,\mathbf{u} \cdot \mathbf{v} = -2\,\mathbf{u} \cdot \mathbf{v}$, that is, $\mathbf{u} \cdot \mathbf{v} = 0$. So in the plane and in space, perpendicularity means $\mathbf{u} \cdot \mathbf{v} = 0$; Definition §40.5 takes this as the definition in $\mathbb{R}^n$.

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
> By Proposition §40.3, $\|\mathbf{u} + \mathbf{v}\|^2 - \|\mathbf{u}\|^2 - \|\mathbf{v}\|^2 = 2\,\mathbf{u} \cdot \mathbf{v}$. This is $0$ if and only if $\mathbf{u} \cdot \mathbf{v} = 0$, that is, if and only if $\mathbf{u}$ and $\mathbf{v}$ are orthogonal.
>
> (The lecture used the difference instead: for the right triangle with legs $\mathbf{u}$, $\mathbf{v}$ and hypotenuse $\mathbf{u} - \mathbf{v}$, the second formula of Proposition §40.3 gives $\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$ when $\mathbf{u} \cdot \mathbf{v} = 0$. It left as an exercise to recover the school formula $b = c\cos\varphi$ for a right triangle with leg $b$, hypotenuse $c$ and angle $\varphi$ between them: with legs $\mathbf{u} \perp \mathbf{v}$ and hypotenuse $\mathbf{h} = \mathbf{u} + \mathbf{v}$, Theorem §40.9 gives $\|\mathbf{h}\|\,\|\mathbf{v}\|\cos\varphi = \mathbf{h} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{v} + \mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2$, so $\|\mathbf{v}\| = \|\mathbf{h}\|\cos\varphi$.)

^pf-40-4

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^prop-40-3|§40.3]], [[§40 Inner Product, Length, and Orthogonality#^def-40-5|Def. §40.5]]

> [!remark]- Connections
> - Rigorous treatment: [[§19 Inner Products and Norms#^ladr-6-12|LADR 6.12]], for any inner product space; Axler states only the direction "orthogonal $\Rightarrow$ the identity". The converse holds over $\mathbb{R}$ by the same computation, but fails over $\mathbb{C}$, where the identity says only $\operatorname{Re}\langle u, v \rangle = 0$.
> - Hilbert-space version, with its extension to finitely many orthonormal vectors: [[§24 Orthonormal Sets and Bases#^lem-24-1|556 Lem. §24.1]].

## Orthogonal Complements

> [!definition] Definition §40.6: Orthogonal Complement
> Let $W$ be a subspace of $\mathbb{R}^n$. A vector $\mathbf{z}$ is **orthogonal to $W$** if $\mathbf{z}$ is orthogonal to every vector in $W$. The set of all vectors orthogonal to $W$ is the **orthogonal complement** of $W$, written $W^\perp$ (read "$W$ perp"):
>
> $$
> W^\perp = \{\mathbf{z} \in \mathbb{R}^n : \mathbf{z} \cdot \mathbf{w} = 0 \text{ for all } \mathbf{w} \in W\} .
> $$
>
> *Lay: 6.1 (text)*

^def-40-6

> [!theorem] Theorem §40.5: Basic Facts About the Orthogonal Complement
> Let $W$ be a subspace of $\mathbb{R}^n$.
>
> 1. A vector $\mathbf{x}$ is in $W^\perp$ if and only if $\mathbf{x}$ is orthogonal to every vector in a set that spans $W$.
> 2. $W^\perp$ is a subspace of $\mathbb{R}^n$.
> 3. $W \cap W^\perp = \{\mathbf{0}\}$.
>
> *Lay: 6.1, boxed facts 1 and 2; Exercise 31*

^thm-40-5

> [!proof]+ Proof
> Lay suggests these proofs in Exercises 29–31.
>
> (1) If $\mathbf{x} \in W^\perp$, then $\mathbf{x}$ is orthogonal to every vector of $W$, in particular to the vectors of a spanning set. Conversely, let $W = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ and $\mathbf{x} \cdot \mathbf{v}_j = 0$ for every $j$. Any $\mathbf{w} \in W$ is $\mathbf{w} = c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p$, and by the linear-combination rule of Theorem §40.1,
>
> $$
> \mathbf{w} \cdot \mathbf{x} = c_1(\mathbf{v}_1 \cdot \mathbf{x}) + \cdots + c_p(\mathbf{v}_p \cdot \mathbf{x}) = 0 .
> $$
>
> (2) $\mathbf{0} \in W^\perp$. Let $\mathbf{z}, \mathbf{z}_1, \mathbf{z}_2 \in W^\perp$, $c$ a scalar, and $\mathbf{u} \in W$. Then $(c\mathbf{z}) \cdot \mathbf{u} = c(\mathbf{z} \cdot \mathbf{u}) = 0$ and $(\mathbf{z}_1 + \mathbf{z}_2) \cdot \mathbf{u} = \mathbf{z}_1 \cdot \mathbf{u} + \mathbf{z}_2 \cdot \mathbf{u} = 0$. Since $\mathbf{u}$ was arbitrary, $c\mathbf{z}$ and $\mathbf{z}_1 + \mathbf{z}_2$ lie in $W^\perp$, which is therefore closed under scalar multiplication and addition.
>
> (3) If $\mathbf{x} \in W$ and $\mathbf{x} \in W^\perp$, then $\mathbf{x}$ is orthogonal to itself: $\mathbf{x} \cdot \mathbf{x} = 0$, so $\mathbf{x} = \mathbf{0}$ by Theorem §40.1(d).

^pf-40-5

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§18 Subspaces of ℝⁿ#^def-18-1|Def. §18.1]] (subspace)

> [!theorem] Theorem §40.6: The Fundamental Subspaces Are Orthogonal Complements
> Let $A$ be an $m \times n$ matrix. The orthogonal complement of the row space of $A$ is the null space of $A$, and the orthogonal complement of the column space of $A$ is the null space of $A^T$:
>
> $$
> (\operatorname{Row} A)^\perp = \operatorname{Nul} A \qquad\text{and}\qquad (\operatorname{Col} A)^\perp = \operatorname{Nul} A^T .
> $$
>
> *Lay: Theorem 3 (6.1)*

^thm-40-6

> [!proof]+ Proof
> Both equalities of sets are proved by showing two inclusions.
>
> Let $\mathbf{r}_1, \ldots, \mathbf{r}_m \in \mathbb{R}^n$ be the rows of $A$, written as vectors. By the row–column rule, the $i$th entry of $A\mathbf{x}$ is $\mathbf{r}_i \cdot \mathbf{x}$. If $\mathbf{x} \in \operatorname{Nul} A$, then $A\mathbf{x} = \mathbf{0}$, so $\mathbf{r}_i \cdot \mathbf{x} = 0$ for every $i$. The rows span $\operatorname{Row} A$, so $\mathbf{x} \in (\operatorname{Row} A)^\perp$ by Theorem §40.5(1). Conversely, if $\mathbf{x} \in (\operatorname{Row} A)^\perp$, then $\mathbf{x}$ is orthogonal to each row, every entry of $A\mathbf{x}$ is $0$, and $\mathbf{x} \in \operatorname{Nul} A$. This proves $(\operatorname{Row} A)^\perp = \operatorname{Nul} A$.
>
> This holds for every matrix, in particular for $A^T$: $(\operatorname{Row} A^T)^\perp = \operatorname{Nul} A^T$. The rows of $A^T$ are the columns of $A$, so $\operatorname{Row} A^T = \operatorname{Col} A$, which gives the second statement.

^pf-40-6

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-5|§40.5]], [[§4 The Matrix Equation Ax = b#^prop-4-4|§4.4]] (row–vector rule), [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-3|Def. §24.3]] (row space)

> [!remark]- Connections
> - Rigorous treatment: [[§22 Self-Adjoint and Normal Operators#^ladr-7-6|LADR 7.6]] ($\operatorname{null} T^* = (\operatorname{range} T)^\perp$ and $\operatorname{range} T^* = (\operatorname{null} T)^\perp$ for a linear map between inner product spaces; the transpose becomes the adjoint, and the row space is $\operatorname{range} T^*$). Orthogonal complements in general: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]], with $\dim U^\perp = \dim V - \dim U$ in [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|LADR 6.51]] and $(U^\perp)^\perp = U$ in [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]] (Proposition §40.7 and Corollary §40.8 below).
> - In a Hilbert space the orthogonal complement ([[§22 Projection and Orthogonal Decomposition#^def-22-1|556 Def. §22.1]]) of any set is a closed subspace, [[§22 Projection and Orthogonal Decomposition#^prop-22-3|556 Prop. §22.3]], and the double complement is the closed span, [[§22 Projection and Orthogonal Decomposition#^thm-22-6|556 Thm. §22.6]].

> [!theorem] Proposition §40.7: Dimension of the Orthogonal Complement
> If $W$ is a subspace of $\mathbb{R}^n$, then
>
> $$
> \dim W + \dim W^\perp = n .
> $$
>
> *Lay: 6.1, Practice Problem 3*

^prop-40-7

> [!proof]+ Proof
> If $W = \{\mathbf{0}\}$, then $W^\perp = \mathbb{R}^n$ and the formula reads $0 + n = n$. Otherwise let $\{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$ be a basis of $W$, $1 \le p \le n$, and let $A$ be the $p \times n$ matrix with rows $\mathbf{b}_1^T, \ldots, \mathbf{b}_p^T$. Then $W = \operatorname{Row} A$, and by Theorem §40.6, $W^\perp = (\operatorname{Row} A)^\perp = \operatorname{Nul} A$. By the Rank Theorem,
>
> $$
> \dim W + \dim W^\perp = \dim \operatorname{Row} A + \dim \operatorname{Nul} A = \operatorname{rank} A + \dim \operatorname{Nul} A = n .
> $$

^pf-40-7

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|§40.6]], [[§28 Rank#^thm-28-3|§28.3]] (the Rank Theorem)

> [!theorem] Corollary §40.8: The Double Complement
> If $W$ is a subspace of $\mathbb{R}^n$, then $(W^\perp)^\perp = W$. In particular, for an $m \times n$ matrix $A$,
>
> $$
> (\operatorname{Nul} A)^\perp = \operatorname{Row} A = \operatorname{Col} A^T \qquad\text{and}\qquad (\operatorname{Nul} A^T)^\perp = \operatorname{Col} A .
> $$
>
> The lecture stated the orthogonality theorem as $(\operatorname{Nul} A)^\perp = \operatorname{Row} A = \operatorname{Col} A^T$ together with $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$ (Theorem §40.6).
>
> *Source: 235 lecture L22*

^cor-40-8

> [!proof]+ Proof
> Every $\mathbf{w} \in W$ is orthogonal to every vector of $W^\perp$, so $W \subseteq (W^\perp)^\perp$. By Proposition §40.7, applied to $W$ and then to $W^\perp$,
>
> $$
> \dim (W^\perp)^\perp = n - \dim W^\perp = n - (n - \dim W) = \dim W .
> $$
>
> A subspace of $(W^\perp)^\perp$ with the same dimension is all of it (a basis of $W$ is a linearly independent set of $\dim (W^\perp)^\perp$ vectors there, hence a basis, by the Basis Theorem; this is [[§27 The Dimension of a Vector Space#^cor-27-6|Corollary §27.6]]). So $W = (W^\perp)^\perp$. Taking complements in Theorem §40.6 gives $(\operatorname{Nul} A)^\perp = ((\operatorname{Row} A)^\perp)^\perp = \operatorname{Row} A$ and $(\operatorname{Nul} A^T)^\perp = \operatorname{Col} A$.

^pf-40-8

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^prop-40-7|§40.7]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|§40.6]], [[§27 The Dimension of a Vector Space#^thm-27-5|§27.5]] (the Basis Theorem), [[§27 The Dimension of a Vector Space#^cor-27-6|§27.6]]

![[m235-40-1.svg]]
*The four fundamental subspaces of an $m \times n$ matrix $A$. In $\mathbb{R}^n$, $\operatorname{Row} A$ and $\operatorname{Nul} A$ are orthogonal complements (Theorem §40.6); in $\mathbb{R}^m$, so are $\operatorname{Col} A$ and $\operatorname{Nul} A^T$. Their dimensions add up to $n$ and to $m$ (Proposition §40.7): $\operatorname{rank} A + \dim \operatorname{Nul} A = n$ and $\operatorname{rank} A + \dim \operatorname{Nul} A^T = m$.*

> [!example] Example §40.4: A Plane and Its Normal Line
> **(a)** Let $W$ be a plane through the origin in $\mathbb{R}^3$ and $L$ the line through the origin perpendicular to $W$. For nonzero $\mathbf{z} \in L$ and $\mathbf{w} \in W$, the segments from $\mathbf{0}$ to $\mathbf{z}$ and to $\mathbf{w}$ are perpendicular, so $\mathbf{z} \cdot \mathbf{w} = 0$. In fact $L$ consists of *all* vectors orthogonal to $W$, and $W$ of all vectors orthogonal to $L$:
>
> $$
> L = W^\perp \qquad\text{and}\qquad W = L^\perp .
> $$
>
> **(b)** Concretely, let $W = \{\mathbf{x} \in \mathbb{R}^3 : x_1 + 2x_2 - x_3 = 0\}$, a plane through $\mathbf{0}$. With $\mathbf{v} = (1, 2, -1)$, the defining equation says $\mathbf{v} \cdot \mathbf{x} = 0$, so
>
> $$
> W = \{\mathbf{x} : \mathbf{v} \cdot \mathbf{x} = 0\} = \operatorname{Nul} \begin{bmatrix} 1 & 2 & -1 \end{bmatrix} = \operatorname{Span}\{\mathbf{v}\}^\perp .
> $$
>
> By Corollary §40.8, $W^\perp = (\operatorname{Span}\{\mathbf{v}\}^\perp)^\perp = \operatorname{Span}\{\mathbf{v}\}$: a vector $\mathbf{y}$ is orthogonal to $W$ if and only if $\mathbf{y} = \lambda\mathbf{v}$ for some scalar $\lambda$, that is, $\mathbf{y}$ is proportional to $(1, 2, -1)$. The dimensions agree with Proposition §40.7: $2 + 1 = 3$.
>
> *Lay: Example 6.1.6*
> *Source: 235 lecture L22*

^ex-40-4

> [!example] Example §40.5: Testing Membership in an Orthogonal Complement
> Let $W \subseteq \mathbb{R}^4$ be the set of solutions of
>
> $$
> x_1 + x_2 + x_3 + x_4 = 0, \qquad x_2 + x_3 = 0,
> $$
>
> and $\mathbf{u} = (0, 1, 1, 0)$. Show that $\mathbf{u} \in W^\perp$.
>
> **Method 1: a spanning set.** By Theorem §40.5(1) it is enough to check $\mathbf{u}$ against a finite set spanning $W$. Solving the system ($x_3 = -x_2$ from the second equation, then $x_1 = -x_4$ from the first), $W$ is the $2$-dimensional plane
>
> $$
> W = \operatorname{Span}\{\mathbf{w}_1, \mathbf{w}_2\}, \qquad \mathbf{w}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ -1 \end{bmatrix}, \quad \mathbf{w}_2 = \begin{bmatrix} 0 \\ 1 \\ -1 \\ 0 \end{bmatrix} .
> $$
>
> Then $\mathbf{u} \cdot \mathbf{w}_1 = 0 + 0 + 0 + 0 = 0$ and $\mathbf{u} \cdot \mathbf{w}_2 = 0 + 1 - 1 + 0 = 0$. This suffices, because any $\mathbf{w} \in W$ is $a\mathbf{w}_1 + b\mathbf{w}_2$, and $\mathbf{w} \cdot \mathbf{u} = a(\mathbf{w}_1 \cdot \mathbf{u}) + b(\mathbf{w}_2 \cdot \mathbf{u}) = 0$.
>
> **Method 2: the row space.** $W = \operatorname{Nul} A$ for
>
> $$
> A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 0 \end{bmatrix}, \qquad\text{so}\qquad W^\perp = (\operatorname{Nul} A)^\perp = \operatorname{Row} A = \operatorname{Span}\{\mathbf{r}_1, \mathbf{r}_2\}
> $$
>
> by Corollary §40.8, where $\mathbf{r}_1 = (1, 1, 1, 1)$ and $\mathbf{r}_2 = (0, 1, 1, 0)$ are the rows. The question becomes whether $\mathbf{u} \in \operatorname{Span}\{\mathbf{r}_1, \mathbf{r}_2\}$, and here $\mathbf{u} = \mathbf{r}_2$. This is the quickest solution; it needs no basis of $W$.
>
> *Source: 235 lecture L22*

^ex-40-5

## Angles in ℝ² and ℝ³ (Optional)

> [!theorem] Theorem §40.9: The Inner Product and the Angle
> Let $\mathbf{u}$ and $\mathbf{v}$ be nonzero vectors in $\mathbb{R}^2$ or $\mathbb{R}^3$, and let $\vartheta$ be the angle between the line segments from the origin to the points $\mathbf{u}$ and $\mathbf{v}$. Then
>
> $$
> \mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\| \cos\vartheta .
> $$
>
> For $n > 3$ this formula is used to *define* the angle between two nonzero vectors of $\mathbb{R}^n$. (In statistics, $\cos\vartheta$ for suitable vectors $\mathbf{u}$, $\mathbf{v}$ is the correlation coefficient.)
>
> *Lay: 6.1, Equation (2)*

^thm-40-9

> [!proof]+ Proof
> The triangle with vertices $\mathbf{0}$, $\mathbf{u}$, $\mathbf{v}$ has sides of lengths $\|\mathbf{u}\|$, $\|\mathbf{v}\|$, $\|\mathbf{u} - \mathbf{v}\|$, and its angle at $\mathbf{0}$ is $\vartheta$. The law of cosines ([[§119 Trigonometry#^thm-119-11|Calc Thm. §119.11]]) gives
>
> $$
> \|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\,\|\mathbf{v}\| \cos\vartheta .
> $$
>
> Solving for the last term, for $\mathbf{u} = (u_1, u_2)$, $\mathbf{v} = (v_1, v_2)$:
>
> $$
> \begin{aligned}
> \|\mathbf{u}\|\,\|\mathbf{v}\| \cos\vartheta &= \tfrac12\big[\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - \|\mathbf{u} - \mathbf{v}\|^2\big] \\
> &= \tfrac12\big[u_1^2 + u_2^2 + v_1^2 + v_2^2 - (u_1 - v_1)^2 - (u_2 - v_2)^2\big] \\
> &= \tfrac12\big[2u_1v_1 + 2u_2v_2\big] = u_1v_1 + u_2v_2 = \mathbf{u} \cdot \mathbf{v} .
> \end{aligned}
> $$
>
> In $\mathbb{R}^3$ the three points $\mathbf{0}$, $\mathbf{u}$, $\mathbf{v}$ still span a triangle in a plane, the law of cosines applies to it, and the same computation with a third coordinate gives $u_1v_1 + u_2v_2 + u_3v_3$. (If $\mathbf{u}$ and $\mathbf{v}$ lie on one line, the triangle is degenerate, $\vartheta = 0$ or $\pi$, and the formula is checked directly from $\mathbf{v} = c\mathbf{u}$.) Equivalently, the middle line is Proposition §40.3.

^pf-40-9

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^prop-40-3|§40.3]], [[§40 Inner Product, Length, and Orthogonality#^def-40-4|Def. §40.4]], [[§119 Trigonometry#^thm-119-11|Calc Thm. §119.11]] (law of cosines)

> [!remark]- Connections
> - Stewart proves the same formula for vectors in $\mathbb{R}^2$ and $\mathbb{R}^3$, also from the law of cosines: [[§82 The Dot Product#^thm-82-2|Calc Thm. §82.2]]; orthogonality test [[§82 The Dot Product#^thm-82-4|Calc Thm. §82.4]].
> - For $n > 3$ the definition of the angle needs $|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\|\,\|\mathbf{v}\|$ first: the Cauchy–Schwarz inequality, [[§19 Inner Products and Norms#^ladr-6-14|LADR 6.14]], proved here in [[§46 Inner Product Spaces#^thm-46-4|Theorem §46.4]].

> [!remark] Remark: The Cauchy Inequality
> Since $|\cos\vartheta| \le 1$, the angle formula gives $|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\|\,\|\mathbf{v}\|$, that is,
>
> $$
> (u_1v_1 + \cdots + u_nv_n)^2 \le (u_1^2 + \cdots + u_n^2)(v_1^2 + \cdots + v_n^2) .
> $$
>
> This is the Cauchy inequality. As an argument it only works for $n \le 3$, where the angle exists geometrically. For $n > 3$ the angle is *defined* by $\cos\vartheta = \mathbf{u} \cdot \mathbf{v} / (\|\mathbf{u}\|\,\|\mathbf{v}\|)$, and that definition makes sense only once the inequality is known. A proof that works in $\mathbb{R}^n$, and in every inner product space, is [[§46 Inner Product Spaces#^thm-46-4|Theorem §46.4]] (Cauchy–Schwarz).
>
> *Source: 235 lecture L22*

^rem-40-2
