---
type: section
subject: "[[Calculus]]"
chapter: 12
section: 83
stewart: "12.4"
aliases: ["Stewart 12.4"]
tags: [calculus, math233]
---
← [[§82 The Dot Product]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§84 Equations of Lines and Planes]] →

*Stewart, Section 12.4 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q3), Practice Exam 1 (Q1(a)), Exam 1 Review (Q1(d)–(g)), SI Midterm 1 Problem Set (Q3(a), Q5(a)).*

Given two vectors in space, the cross product produces a third vector perpendicular to both. It is defined by a formula in components, conveniently remembered as a $3 \times 3$ determinant, and then described geometrically: $\mathbf{a} \times \mathbf{b}$ is perpendicular to $\mathbf{a}$ and $\mathbf{b}$, its direction follows the right-hand rule, and its length $|\mathbf{a}||\mathbf{b}|\sin\theta$ is the area of the parallelogram spanned by $\mathbf{a}$ and $\mathbf{b}$. Unlike the dot product it is neither commutative nor associative. The scalar triple product $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ is a determinant and measures the volume of a parallelepiped. The cross product is the standard tool for normal vectors of planes ([[§84 Equations of Lines and Planes#^def-84-3|Definition §84.3]]), curvature and the binormal vector ([[§88 Arc Length and Curvature#^thm-88-4|Theorem §88.4]], [[§88a The TNB Frame and Torsion#^def-88-new1|Definition §88.6]]), and surface integrals in Chapter 16.

## The Cross Product of Two Vectors

> [!remark] Remark: Where the Formula Comes From
> Given nonzero $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$ and $\mathbf{b} = \langle b_1, b_2, b_3 \rangle$, look for $\mathbf{c} = \langle c_1, c_2, c_3 \rangle \ne \mathbf{0}$ with $\mathbf{a} \cdot \mathbf{c} = 0$ and $\mathbf{b} \cdot \mathbf{c} = 0$:
>
> $$
> a_1c_1 + a_2c_2 + a_3c_3 = 0 \qquad (1) \qquad\qquad b_1c_1 + b_2c_2 + b_3c_3 = 0 \qquad (2)
> $$
>
> Multiply (1) by $b_3$ and (2) by $a_3$ and subtract to eliminate $c_3$:
>
> $$
> (a_1b_3 - a_3b_1)c_1 + (a_2b_3 - a_3b_2)c_2 = 0 . \qquad (3)
> $$
>
> An equation $pc_1 + qc_2 = 0$ has the obvious solution $c_1 = q$, $c_2 = -p$, so take $c_1 = a_2b_3 - a_3b_2$ and $c_2 = a_3b_1 - a_1b_3$. Substituting into (1) and (2) then gives $c_3 = a_1b_2 - a_2b_1$. The resulting vector $\langle c_1, c_2, c_3 \rangle$ is the cross product.

^rem-83-1

> [!definition] Definition §83.1: Cross Product
> If $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$ and $\mathbf{b} = \langle b_1, b_2, b_3 \rangle$, then the **cross product** of $\mathbf{a}$ and $\mathbf{b}$ is the vector
>
> $$
> \mathbf{a} \times \mathbf{b} = \langle a_2b_3 - a_3b_2,\ a_3b_1 - a_1b_3,\ a_1b_2 - a_2b_1 \rangle .
> $$
>
> Since the result is a vector, it is also called the **vector product**. It is defined only for *three-dimensional* vectors.
>
> *Stewart: 12.4, Definition 4*

^def-83-1

> [!remark]- Connections
> - The three components are the $2 \times 2$ minors of the matrix with columns $\mathbf{a}$, $\mathbf{b}$; in the language of forms, $\mathbf{X}_u \times \mathbf{X}_v$ packages the pullbacks of $dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$: [[§22 The Algebra of Differential Forms#^rem-22-3|452 Remark: The Cross Product Is the Pullback in Disguise]]. That is why it exists only in $\mathbb{R}^3$.

> [!definition] Definition §83.2: Determinants of Order 2 and 3
> A **determinant of order 2** is
>
> $$
> \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc ,
> $$
>
> and a **determinant of order 3** is defined in terms of determinants of order 2 by expanding along the first row:
>
> $$
> \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}
> = a_1 \begin{vmatrix} b_2 & b_3 \\ c_2 & c_3 \end{vmatrix}
> - a_2 \begin{vmatrix} b_1 & b_3 \\ c_1 & c_3 \end{vmatrix}
> + a_3 \begin{vmatrix} b_1 & b_2 \\ c_1 & c_2 \end{vmatrix} .
> $$
>
> Each $a_i$ multiplies the order-2 determinant obtained by deleting the row and column of $a_i$; note the minus sign on the middle term. For example,
>
> $$
> \begin{vmatrix} 2 & 1 \\ -6 & 4 \end{vmatrix} = 2(4) - 1(-6) = 14, \qquad
> \begin{vmatrix} 1 & 2 & -1 \\ 3 & 0 & 1 \\ -5 & 4 & 2 \end{vmatrix} = 1(0 - 4) - 2(6 + 5) + (-1)(12 - 0) = -38 .
> $$
>
> *Stewart: 12.4, Equation 5*

^def-83-2

> [!theorem] Proposition §83.1: The Cross Product as a Determinant
> For $\mathbf{a} = a_1\mathbf{i} + a_2\mathbf{j} + a_3\mathbf{k}$ and $\mathbf{b} = b_1\mathbf{i} + b_2\mathbf{j} + b_3\mathbf{k}$,
>
> $$
> \mathbf{a} \times \mathbf{b}
> = \begin{vmatrix} a_2 & a_3 \\ b_2 & b_3 \end{vmatrix} \mathbf{i}
> - \begin{vmatrix} a_1 & a_3 \\ b_1 & b_3 \end{vmatrix} \mathbf{j}
> + \begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} \mathbf{k}
> = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} .
> $$
>
> The last expression is a *symbolic* determinant (its first row consists of vectors): expanding it formally by the rule of [[§83 The Cross Product#^def-83-2|Definition §83.2]] gives the middle expression. It is the easiest way to remember and compute cross products.
>
> *Stewart: 12.4, Equations 6 and 7*

^prop-83-1

> [!proof]+ Proof
> The three order-2 determinants are $a_2b_3 - a_3b_2$, $a_1b_3 - a_3b_1$ and $a_1b_2 - a_2b_1$. So the middle expression is $(a_2b_3 - a_3b_2)\mathbf{i} + (a_3b_1 - a_1b_3)\mathbf{j} + (a_1b_2 - a_2b_1)\mathbf{k}$, which is [[§83 The Cross Product#^def-83-1|Definition §83.1]] written with [[§81 Vectors#^prop-81-6|Proposition §81.6]].

^pf-83-1

*Uses:* [[§83 The Cross Product#^def-83-1|Def. §83.1]], [[§83 The Cross Product#^def-83-2|Def. §83.2]], [[§81 Vectors#^prop-81-6|§81.6]]

> [!remark]- Connections
> - Matrix version of [[§83 The Cross Product#^def-83-2|Definition §83.2]] and [[§83 The Cross Product#^prop-83-1|Proposition §83.1]]: [[§20 Introduction to Determinants#^def-20-2|235 Def. §20.2]] (the same expansion along the first row, for $n \times n$ matrices) and [[§20 Introduction to Determinants#^prop-20-3|235 Prop. §20.3]] (the diagonal rule for $3 \times 3$), with worked examples.

> [!example] Example §83.1: Computing Cross Products
> **(a)** If $\mathbf{a} = \langle 1, 3, 4 \rangle$ and $\mathbf{b} = \langle 2, 7, -5 \rangle$, then
>
> $$
> \mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 3 & 4 \\ 2 & 7 & -5 \end{vmatrix}
> = \begin{vmatrix} 3 & 4 \\ 7 & -5 \end{vmatrix}\mathbf{i} - \begin{vmatrix} 1 & 4 \\ 2 & -5 \end{vmatrix}\mathbf{j} + \begin{vmatrix} 1 & 3 \\ 2 & 7 \end{vmatrix}\mathbf{k}
> = (-15 - 28)\mathbf{i} - (-5 - 8)\mathbf{j} + (7 - 6)\mathbf{k} = -43\mathbf{i} + 13\mathbf{j} + \mathbf{k} .
> $$
>
> Check ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]] below): $\langle -43, 13, 1 \rangle \cdot \langle 1, 3, 4 \rangle = -43 + 39 + 4 = 0$ and $\langle -43, 13, 1 \rangle \cdot \langle 2, 7, -5 \rangle = -86 + 91 - 5 = 0$.
>
> **(b)** $\mathbf{a} \times \mathbf{a} = \mathbf{0}$ for every $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$:
>
> $$
> \mathbf{a} \times \mathbf{a} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ a_1 & a_2 & a_3 \end{vmatrix} = (a_2a_3 - a_3a_2)\mathbf{i} - (a_1a_3 - a_3a_1)\mathbf{j} + (a_1a_2 - a_2a_1)\mathbf{k} = \mathbf{0} .
> $$
>
> *Stewart: Examples 12.4.1 and 12.4.2*

^ex-83-1

## Properties of the Cross Product

> [!theorem] Theorem §83.2: The Cross Product Is Orthogonal to Both Factors
> The vector $\mathbf{a} \times \mathbf{b}$ is orthogonal to both $\mathbf{a}$ and $\mathbf{b}$.
>
> *Stewart: 12.4, Theorem 8*

^thm-83-2

> [!proof]+ Proof
> By [[§83 The Cross Product#^prop-83-1|Proposition §83.1]],
>
> $$
> \begin{aligned}
> (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{a}
> &= \begin{vmatrix} a_2 & a_3 \\ b_2 & b_3 \end{vmatrix} a_1 - \begin{vmatrix} a_1 & a_3 \\ b_1 & b_3 \end{vmatrix} a_2 + \begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} a_3 \\
> &= a_1(a_2b_3 - a_3b_2) - a_2(a_1b_3 - a_3b_1) + a_3(a_1b_2 - a_2b_1) \\
> &= a_1a_2b_3 - a_1b_2a_3 - a_1a_2b_3 + b_1a_2a_3 + a_1b_2a_3 - b_1a_2a_3 = 0 .
> \end{aligned}
> $$
>
> Stewart says "a similar computation" gives the other half; here it is:
>
> $$
> (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{b} = b_1(a_2b_3 - a_3b_2) - b_2(a_1b_3 - a_3b_1) + b_3(a_1b_2 - a_2b_1) = a_2b_1b_3 - a_3b_1b_2 - a_1b_2b_3 + a_3b_1b_2 + a_1b_2b_3 - a_2b_1b_3 = 0 .
> $$
>
> By [[§82 The Dot Product#^thm-82-4|Theorem §82.4]], $\mathbf{a} \times \mathbf{b}$ is orthogonal to $\mathbf{a}$ and to $\mathbf{b}$.

^pf-83-2

*Uses:* [[§83 The Cross Product#^prop-83-1|§83.1]], [[§82 The Dot Product#^thm-82-4|§82.4]]

> [!theorem] Proposition §83.3: Right-Hand Rule
> If $\mathbf{a}$ and $\mathbf{b}$ are represented by directed segments with the same initial point, then $\mathbf{a} \times \mathbf{b}$ points in a direction perpendicular to the plane through $\mathbf{a}$ and $\mathbf{b}$, given by the **right-hand rule**: if the fingers of the right hand curl in the direction of a rotation (through an angle less than $180^\circ$) from $\mathbf{a}$ to $\mathbf{b}$, the thumb points in the direction of $\mathbf{a} \times \mathbf{b}$.
>
> *Stewart: 12.4 (text)*

^prop-83-3

*Stewart states the direction without proof ("it turns out"). For $\mathbf{a} = \mathbf{i}$, $\mathbf{b} = \mathbf{j}$ it is the right-hand rule that orients the $z$-axis ([[§80 Three-Dimensional Coordinate Systems#^def-80-1|Definition §80.1]]), since $\mathbf{i} \times \mathbf{j} = \mathbf{k}$ ([[§83 The Cross Product#^prop-83-7|Proposition §83.7]]). A general pair can be turned into this one by a rotation and a stretching, during which $\mathbf{a} \times \mathbf{b}$ changes continuously and never becomes $\mathbf{0}$, so it cannot jump to the other side of the plane; making this precise is a matter of orientation and the sign of a determinant. The precise content is: by Property 5 of [[§83 The Cross Product#^thm-83-8|Theorem §83.8]] and [[§83a Triple Products and Torque#^thm-83-9|Theorem §83.9]], the determinant with rows $\mathbf{a}$, $\mathbf{b}$, $\mathbf{a} \times \mathbf{b}$ equals $\mathbf{a} \cdot (\mathbf{b} \times (\mathbf{a} \times \mathbf{b})) = (\mathbf{a} \times \mathbf{b}) \cdot (\mathbf{a} \times \mathbf{b}) = |\mathbf{a} \times \mathbf{b}|^2 > 0$ for nonparallel $\mathbf{a}$, $\mathbf{b}$, the same sign as for the right-handed triple $\mathbf{i}, \mathbf{j}, \mathbf{k}$ (determinant $1$).*

> [!theorem] Theorem §83.4: Length of the Cross Product
> If $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$ (so $0 \le \theta \le \pi$), then
>
> $$
> |\mathbf{a} \times \mathbf{b}| = |\mathbf{a}|\,|\mathbf{b}| \sin\theta .
> $$
>
> *Stewart: 12.4, Theorem 9*

^thm-83-4

> [!proof]+ Proof
> From the definitions of the cross product and the length of a vector,
>
> $$
> \begin{aligned}
> |\mathbf{a} \times \mathbf{b}|^2 &= (a_2b_3 - a_3b_2)^2 + (a_3b_1 - a_1b_3)^2 + (a_1b_2 - a_2b_1)^2 \\
> &= a_2^2b_3^2 - 2a_2a_3b_2b_3 + a_3^2b_2^2 + a_3^2b_1^2 - 2a_1a_3b_1b_3 + a_1^2b_3^2 + a_1^2b_2^2 - 2a_1a_2b_1b_2 + a_2^2b_1^2 \\
> &= (a_1^2 + a_2^2 + a_3^2)(b_1^2 + b_2^2 + b_3^2) - (a_1b_1 + a_2b_2 + a_3b_3)^2 \\
> &= |\mathbf{a}|^2|\mathbf{b}|^2 - (\mathbf{a} \cdot \mathbf{b})^2 .
> \end{aligned}
> $$
>
> (For the third line: the product $(a_1^2 + a_2^2 + a_3^2)(b_1^2 + b_2^2 + b_3^2)$ consists of the six terms $a_i^2b_j^2$ with $i \ne j$ appearing above, plus $a_1^2b_1^2 + a_2^2b_2^2 + a_3^2b_3^2$; and $(\mathbf{a} \cdot \mathbf{b})^2$ is that same sum of squares plus $2a_1a_2b_1b_2 + 2a_1a_3b_1b_3 + 2a_2a_3b_2b_3$.) By [[§82 The Dot Product#^thm-82-2|Theorem §82.2]],
>
> $$
> |\mathbf{a} \times \mathbf{b}|^2 = |\mathbf{a}|^2|\mathbf{b}|^2 - |\mathbf{a}|^2|\mathbf{b}|^2\cos^2\theta = |\mathbf{a}|^2|\mathbf{b}|^2(1 - \cos^2\theta) = |\mathbf{a}|^2|\mathbf{b}|^2\sin^2\theta .
> $$
>
> Take square roots; $\sqrt{\sin^2\theta} = \sin\theta$ because $\sin\theta \ge 0$ for $0 \le \theta \le \pi$.

^pf-83-4

*Uses:* [[§83 The Cross Product#^def-83-1|Def. §83.1]], [[§81 Vectors#^thm-81-3|§81.3]], [[§82 The Dot Product#^thm-82-2|§82.2]]

> [!remark]- Connections
> - The identity $|\mathbf{a} \times \mathbf{b}|^2 = |\mathbf{a}|^2|\mathbf{b}|^2 - (\mathbf{a} \cdot \mathbf{b})^2$ in the proof (Lagrange's identity) is the $\mathbb{R}^3$ case of the Gram-determinant area element $\sqrt{E\tilde G - F^2}$: [[§18 Surface Integrals#^thm-18-1|452 Thm. §18.1]].

> [!theorem] Corollary §83.5: Parallel Vectors
> Two nonzero vectors $\mathbf{a}$ and $\mathbf{b}$ are parallel if and only if $\mathbf{a} \times \mathbf{b} = \mathbf{0}$.
>
> *Stewart: 12.4, Corollary 10*

^cor-83-5

> [!proof]+ Proof
> Two nonzero vectors are parallel if and only if the angle between them is $\theta = 0$ or $\pi$. Since $|\mathbf{a}|, |\mathbf{b}| > 0$, [[§83 The Cross Product#^thm-83-4|Theorem §83.4]] shows that $|\mathbf{a} \times \mathbf{b}| = 0$ if and only if $\sin\theta = 0$, and for $\theta \in [0, \pi]$ that happens exactly when $\theta = 0$ or $\pi$. Finally, a vector has length $0$ only if it is $\mathbf{0}$.

^pf-83-5

*Uses:* [[§83 The Cross Product#^thm-83-4|§83.4]], [[§82 The Dot Product#^def-82-2|Def. §82.2]], [[§81 Vectors#^def-81-3|Def. §81.3]]

> [!remark] Remark: The Geometric Characterization of a × b
> A vector is determined by its magnitude and direction. So for nonparallel $\mathbf{a}$ and $\mathbf{b}$, $\mathbf{a} \times \mathbf{b}$ is *the* vector perpendicular to both $\mathbf{a}$ and $\mathbf{b}$, oriented by the right-hand rule, with length $|\mathbf{a}||\mathbf{b}|\sin\theta$. Physicists take this as the definition of $\mathbf{a} \times \mathbf{b}$.

^rem-83-2

> [!theorem] Corollary §83.6: Area of a Parallelogram
> The length of the cross product $\mathbf{a} \times \mathbf{b}$ is equal to the area of the parallelogram determined by $\mathbf{a}$ and $\mathbf{b}$. Consequently, the triangle with two sides $\mathbf{a}$ and $\mathbf{b}$ has area $\frac12|\mathbf{a} \times \mathbf{b}|$.
>
> *Stewart: 12.4 (boxed)*

^cor-83-6

> [!proof]+ Proof
> Represent $\mathbf{a}$ and $\mathbf{b}$ with a common initial point. The parallelogram they determine has base $|\mathbf{a}|$ and altitude $|\mathbf{b}|\sin\theta$ (the leg opposite $\theta$ in the right triangle with hypotenuse $\mathbf{b}$). So its area is $A = |\mathbf{a}|\,(|\mathbf{b}|\sin\theta) = |\mathbf{a} \times \mathbf{b}|$ by [[§83 The Cross Product#^thm-83-4|Theorem §83.4]]. A diagonal cuts the parallelogram into two congruent triangles, each of area $\frac12 A$.

^pf-83-6

*Uses:* [[§83 The Cross Product#^thm-83-4|§83.4]]

![[m233-83-1.svg]]
*(a) The parallelogram spanned by $\mathbf{a}$ and $\mathbf{b}$ has base $|\mathbf{a}|$ and height $|\mathbf{b}|\sin\theta$, so its area is $|\mathbf{a} \times \mathbf{b}|$; the vector $\mathbf{a} \times \mathbf{b}$ itself points out of the page, perpendicular to the parallelogram. (b) The parallelepiped spanned by $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$: its base has area $|\mathbf{b} \times \mathbf{c}|$, and its height is the length of the projection of $\mathbf{a}$ onto the normal $\mathbf{b} \times \mathbf{c}$ (blue), which is $|\mathbf{a}||\cos\theta|$ ([[§83a Triple Products and Torque#^thm-83-10|Theorem §83.10]]).*

> [!example] Example §83.2: Normal Vectors and Areas of Triangles
> **(a)** Find a vector perpendicular to the plane through $P(1, 4, 6)$, $Q(-2, 5, -1)$ and $R(1, -1, 1)$, and the area of the triangle $PQR$.
>
> $\overrightarrow{PQ} \times \overrightarrow{PR}$ is perpendicular to both $\overrightarrow{PQ}$ and $\overrightarrow{PR}$ ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]]), hence to the plane through $P$, $Q$, $R$. By [[§81 Vectors#^thm-81-2|Theorem §81.2]], $\overrightarrow{PQ} = \langle -3, 1, -7 \rangle$ and $\overrightarrow{PR} = \langle 0, -5, -5 \rangle$, and
>
> $$
> \overrightarrow{PQ} \times \overrightarrow{PR} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -3 & 1 & -7 \\ 0 & -5 & -5 \end{vmatrix} = (-5 - 35)\mathbf{i} - (15 - 0)\mathbf{j} + (15 - 0)\mathbf{k} = \langle -40, -15, 15 \rangle .
> $$
>
> Any nonzero multiple, such as $\langle -8, -3, 3 \rangle$, is also perpendicular to the plane. The parallelogram with sides $PQ$ and $PR$ has area $|\langle -40, -15, 15 \rangle| = \sqrt{1600 + 225 + 225} = \sqrt{2050} = 5\sqrt{82}$, so by [[§83 The Cross Product#^cor-83-6|Corollary §83.6]] the triangle has area $\frac52\sqrt{82}$.
>
> **(b)** The same for $P(2, 2, 6)$, $Q(0, 5, 5)$, $R(3, 1, 7)$: $\overrightarrow{PQ} = \langle -2, 3, -1 \rangle$, $\overrightarrow{PR} = \langle 1, -1, 1 \rangle$, and
>
> $$
> \overrightarrow{PQ} \times \overrightarrow{PR} = \big(3 \cdot 1 - (-1)(-1)\big)\mathbf{i} - \big((-2)(1) - (-1)(1)\big)\mathbf{j} + \big((-2)(-1) - 3 \cdot 1\big)\mathbf{k} = 2\mathbf{i} + \mathbf{j} - \mathbf{k} ,
> $$
>
> so the area of triangle $PQR$ is $\frac12\sqrt{4 + 1 + 1} = \frac{\sqrt6}{2}$.
>
> **(c)** The triangle with vertices $(2, 1, 1)$, $(1, 2, 1)$, $(1, 1, 2)$ has sides $\langle -1, 1, 0 \rangle$ and $\langle -1, 0, 1 \rangle$ from the first vertex; their cross product is $\langle 1 \cdot 1 - 0 \cdot 0,\ 0 \cdot (-1) - (-1)(1),\ (-1)(0) - 1 \cdot (-1) \rangle = \langle 1, 1, 1 \rangle$, so the area is $\frac{\sqrt3}{2}$. Likewise the triangle $A(2, 1, 0)$, $B(3, 0, 2)$, $C(0, 2, 1)$ has $\overrightarrow{AB} \times \overrightarrow{AC} = \langle 1, -1, 2 \rangle \times \langle -2, 1, 1 \rangle = \langle -3, -5, -1 \rangle$ and area $\frac{\sqrt{35}}{2}$.
>
> *Stewart: Examples 12.4.3 and 12.4.4*
> *Source: 233 Midterm 1 Practice Questions, Q3; 233 Practice Exam 1, Q1(a); 233 SI Midterm 1 Problem Set, Q5(a)*

^ex-83-2

> [!theorem] Proposition §83.7: Cross Products of i, j, k
> $$
> \begin{array}{lll}
> \mathbf{i} \times \mathbf{j} = \mathbf{k} & \mathbf{j} \times \mathbf{k} = \mathbf{i} & \mathbf{k} \times \mathbf{i} = \mathbf{j} \\
> \mathbf{j} \times \mathbf{i} = -\mathbf{k} & \mathbf{k} \times \mathbf{j} = -\mathbf{i} & \mathbf{i} \times \mathbf{k} = -\mathbf{j}
> \end{array}
> $$
>
> *Stewart: 12.4 (boxed)*

^prop-83-7

> [!proof]+ Proof
> Stewart obtains these from [[§83 The Cross Product#^thm-83-2|Theorems §83.2]] and [[§83 The Cross Product#^thm-83-4|§83.4]] with $\theta = \pi/2$ (each product is a unit vector perpendicular to both factors). Directly from [[§83 The Cross Product#^def-83-1|Definition §83.1]]: $\mathbf{i} \times \mathbf{j} = \langle 0 \cdot 0 - 0 \cdot 1,\ 0 \cdot 0 - 1 \cdot 0,\ 1 \cdot 1 - 0 \cdot 0 \rangle = \langle 0, 0, 1 \rangle = \mathbf{k}$; similarly $\mathbf{j} \times \mathbf{k} = \langle 1 \cdot 1 - 0 \cdot 0,\ 0, 0 \rangle = \mathbf{i}$ and $\mathbf{k} \times \mathbf{i} = \langle 0,\ 1 \cdot 1 - 0 \cdot 0,\ 0 \rangle = \mathbf{j}$. Exchanging the two factors in any of these computations changes the sign of every component, since each component has the form $a_ib_j - a_jb_i$; this gives the second row. (This is Property 1 of [[§83 The Cross Product#^thm-83-8|Theorem §83.8]] below.)

^pf-83-7

*Uses:* [[§83 The Cross Product#^def-83-1|Def. §83.1]]

> [!remark] Remark: Two Laws That Fail
> Since $\mathbf{i} \times \mathbf{j} = \mathbf{k}$ but $\mathbf{j} \times \mathbf{i} = -\mathbf{k}$, the cross product is **not commutative**. And
>
> $$
> \mathbf{i} \times (\mathbf{i} \times \mathbf{j}) = \mathbf{i} \times \mathbf{k} = -\mathbf{j}, \qquad (\mathbf{i} \times \mathbf{i}) \times \mathbf{j} = \mathbf{0} \times \mathbf{j} = \mathbf{0} ,
> $$
>
> so the associative law fails too: in general $(\mathbf{a} \times \mathbf{b}) \times \mathbf{c} \ne \mathbf{a} \times (\mathbf{b} \times \mathbf{c})$. Order and parentheses matter.

^rem-83-3

> [!theorem] Theorem §83.8: Properties of the Cross Product
> If $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ are vectors and $c$ is a scalar, then
>
> $$
> \begin{array}{ll}
> 1.\ \mathbf{a} \times \mathbf{b} = -\mathbf{b} \times \mathbf{a} & 2.\ (c\mathbf{a}) \times \mathbf{b} = c(\mathbf{a} \times \mathbf{b}) = \mathbf{a} \times (c\mathbf{b}) \\
> 3.\ \mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c} & 4.\ (\mathbf{a} + \mathbf{b}) \times \mathbf{c} = \mathbf{a} \times \mathbf{c} + \mathbf{b} \times \mathbf{c} \\
> 5.\ \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c} & 6.\ \mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}
> \end{array}
> $$
>
> *Stewart: 12.4, Theorem 11*

^thm-83-8

> [!proof]+ Proof
> Stewart proves Property 5 and leaves the rest as exercises. Write $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$, $\mathbf{b} = \langle b_1, b_2, b_3 \rangle$, $\mathbf{c} = \langle c_1, c_2, c_3 \rangle$.
>
> **1.** Each component of $\mathbf{a} \times \mathbf{b}$ has the form $a_ib_j - a_jb_i$; exchanging the roles of $\mathbf{a}$ and $\mathbf{b}$ turns it into $b_ia_j - b_ja_i = -(a_ib_j - a_jb_i)$.
>
> **2.** Replacing $a_i$ by $ca_i$ (or $b_j$ by $cb_j$) multiplies every term $a_ib_j - a_jb_i$ by $c$.
>
> **3.** The first component of $\mathbf{a} \times (\mathbf{b} + \mathbf{c})$ is $a_2(b_3 + c_3) - a_3(b_2 + c_2) = (a_2b_3 - a_3b_2) + (a_2c_3 - a_3c_2)$, the first component of $\mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$; the other components are the same computation.
>
> **4.** By 1, 3 and 1 again: $(\mathbf{a} + \mathbf{b}) \times \mathbf{c} = -\mathbf{c} \times (\mathbf{a} + \mathbf{b}) = -\mathbf{c} \times \mathbf{a} - \mathbf{c} \times \mathbf{b} = \mathbf{a} \times \mathbf{c} + \mathbf{b} \times \mathbf{c}$.
>
> **5.** Expanding and regrouping by $c_1$, $c_2$, $c_3$,
>
> $$
> \begin{aligned}
> \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) &= a_1(b_2c_3 - b_3c_2) + a_2(b_3c_1 - b_1c_3) + a_3(b_1c_2 - b_2c_1) \qquad (12) \\
> &= a_1b_2c_3 - a_1b_3c_2 + a_2b_3c_1 - a_2b_1c_3 + a_3b_1c_2 - a_3b_2c_1 \\
> &= (a_2b_3 - a_3b_2)c_1 + (a_3b_1 - a_1b_3)c_2 + (a_1b_2 - a_2b_1)c_3 = (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c} .
> \end{aligned}
> $$
>
> **6.** Let $\mathbf{d} = \mathbf{b} \times \mathbf{c} = \langle b_2c_3 - b_3c_2,\ b_3c_1 - b_1c_3,\ b_1c_2 - b_2c_1 \rangle$. The first component of $\mathbf{a} \times \mathbf{d}$ is
>
> $$
> \begin{aligned}
> a_2d_3 - a_3d_2 &= a_2(b_1c_2 - b_2c_1) - a_3(b_3c_1 - b_1c_3) = b_1(a_2c_2 + a_3c_3) - c_1(a_2b_2 + a_3b_3) \\
> &= b_1(a_1c_1 + a_2c_2 + a_3c_3) - c_1(a_1b_1 + a_2b_2 + a_3b_3) = (\mathbf{a} \cdot \mathbf{c})b_1 - (\mathbf{a} \cdot \mathbf{b})c_1 ,
> \end{aligned}
> $$
>
> where in the second line we added and subtracted $a_1b_1c_1$. This is the first component of $(\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$. [[§83 The Cross Product#^def-83-1|Definition §83.1]] is unchanged when the indices are permuted cyclically ($1 \to 2 \to 3 \to 1$), and so are dot products, so the same computation with shifted indices gives the second and third components.

^pf-83-8

*Uses:* [[§83 The Cross Product#^def-83-1|Def. §83.1]], [[§82 The Dot Product#^def-82-1|Def. §82.1]]

*The section continues in [[§83a Triple Products and Torque]].*
