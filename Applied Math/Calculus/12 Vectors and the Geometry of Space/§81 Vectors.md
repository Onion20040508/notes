---
type: section
subject: "[[Calculus]]"
chapter: 12
section: 81
stewart: "12.2"
aliases: ["Stewart 12.2"]
tags: [calculus, math233]
---
← [[§80 Three-Dimensional Coordinate Systems]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§82 The Dot Product]] →

*Stewart, Section 12.2 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q6(b)), SI Midterm 1 Problem Set (Q5(b)).*

A vector is a quantity with both a magnitude and a direction: a displacement, a velocity, a force. This section introduces vectors first as arrows, with addition by the Triangle Law and multiplication by scalars, and then as triples of components, where the same operations become arithmetic on coordinates. The two pictures agree, and from here on most computations are done in components. The standard basis vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$, unit vectors, and resultant forces complete the toolkit used in the rest of Chapters 12 and 13.

## Geometric Description of Vectors

> [!definition] Definition §81.1: Vector
> A **vector** is represented by an arrow (a directed line segment): its length is the **magnitude** of the vector and the arrow points in its **direction**. Vectors are written in boldface ($\mathbf{v}$) or with an arrow ($\vec v$).
>
> If a particle moves along a line segment from $A$ to $B$, the **displacement vector** $\mathbf{v} = \overrightarrow{AB}$ has **initial point** $A$ (the tail) and **terminal point** $B$ (the tip). Two vectors with the same length and the same direction are **equivalent** (or **equal**), even if they are in different positions; we write $\mathbf{u} = \mathbf{v}$. The **zero vector** $\mathbf{0}$ has length $0$; it is the only vector with no specific direction.
>
> *Stewart: 12.2 (text)*

^def-81-1

> [!definition] Definition §81.2: Vector Addition (Triangle Law)
> If $\mathbf{u}$ and $\mathbf{v}$ are vectors positioned so that the initial point of $\mathbf{v}$ is at the terminal point of $\mathbf{u}$, then the **sum** $\mathbf{u} + \mathbf{v}$ is the vector from the initial point of $\mathbf{u}$ to the terminal point of $\mathbf{v}$.
>
> For displacements this says $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$: moving from $A$ to $B$ and then from $B$ to $C$ has the combined effect of moving from $A$ to $C$.
>
> *Stewart: 12.2, Definition of Vector Addition*

^def-81-2

> [!theorem] Theorem §81.1: Parallelogram Law
> Place $\mathbf{u}$ and $\mathbf{v}$ so that they start at the same point. Then $\mathbf{u} + \mathbf{v}$ lies along the diagonal of the parallelogram with sides $\mathbf{u}$ and $\mathbf{v}$, starting at the common point. In particular $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.
>
> *Stewart: 12.2 (text)*

^thm-81-1

> [!proof]+ Proof
> Let $\mathbf{u} = \overrightarrow{OA}$ and $\mathbf{v} = \overrightarrow{OB}$, and complete the parallelogram $OACB$. Opposite sides of a parallelogram are parallel and of equal length, and $\overrightarrow{AC}$ points the same way as $\overrightarrow{OB}$, so $\overrightarrow{AC} = \mathbf{v}$; likewise $\overrightarrow{BC} = \mathbf{u}$. By the Triangle Law,
>
> $$
> \mathbf{u} + \mathbf{v} = \overrightarrow{OA} + \overrightarrow{AC} = \overrightarrow{OC} = \overrightarrow{OB} + \overrightarrow{BC} = \mathbf{v} + \mathbf{u} ,
> $$
>
> and $\overrightarrow{OC}$ is the diagonal from $O$.

^pf-81-1

*Uses:* [[§81 Vectors#^def-81-1|Def. §81.1]], [[§81 Vectors#^def-81-2|Def. §81.2]]

> [!definition] Definition §81.3: Scalar Multiplication
> If $c$ is a real number (in this context called a **scalar**) and $\mathbf{v}$ is a vector, the **scalar multiple** $c\mathbf{v}$ is the vector whose length is $|c|$ times the length of $\mathbf{v}$ and whose direction is the same as $\mathbf{v}$ if $c > 0$ and opposite to $\mathbf{v}$ if $c < 0$. If $c = 0$ or $\mathbf{v} = \mathbf{0}$, then $c\mathbf{v} = \mathbf{0}$.
>
> Two nonzero vectors are **parallel** if they are scalar multiples of one another. The vector $-\mathbf{v} = (-1)\mathbf{v}$, with the same length as $\mathbf{v}$ and the opposite direction, is the **negative** of $\mathbf{v}$.
>
> *Stewart: 12.2, Definition of Scalar Multiplication*

^def-81-3

> [!definition] Definition §81.4: Difference of Vectors
> The **difference** of $\mathbf{u}$ and $\mathbf{v}$ is
>
> $$
> \mathbf{u} - \mathbf{v} = \mathbf{u} + (-\mathbf{v}) .
> $$
>
> Since $\mathbf{v} + (\mathbf{u} - \mathbf{v}) = \mathbf{u}$, if $\mathbf{u}$ and $\mathbf{v}$ start at the same point, then $\mathbf{u} - \mathbf{v}$ is the vector from the tip of $\mathbf{v}$ to the tip of $\mathbf{u}$.
>
> *Stewart: 12.2 (text)*

^def-81-4

![[m233-81-1.svg]]
*The geometric operations. (a) Triangle Law: $\mathbf{v}$ starts where $\mathbf{u}$ ends. (b) Parallelogram Law: the two routes around the parallelogram, $\mathbf{u}$ then $\mathbf{v}$ (blue) or $\mathbf{v}$ then $\mathbf{u}$ (green), end at the same point, so $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$. (c) With common tails, $\mathbf{u} - \mathbf{v}$ runs from the tip of $\mathbf{v}$ to the tip of $\mathbf{u}$.*

## Components of a Vector

> [!definition] Definition §81.5: Components and Position Vectors
> Place the initial point of a vector $\mathbf{a}$ at the origin of a rectangular coordinate system. Its terminal point then has coordinates $(a_1, a_2)$ or $(a_1, a_2, a_3)$, called the **components** of $\mathbf{a}$, and we write
>
> $$
> \mathbf{a} = \langle a_1, a_2 \rangle \qquad\text{or}\qquad \mathbf{a} = \langle a_1, a_2, a_3 \rangle .
> $$
>
> (The angle brackets distinguish the vector from the point $(a_1, a_2)$.) Every arrow equivalent to $\mathbf{a}$ is a **representation** of the algebraic vector $\mathbf{a}$; the representation $\overrightarrow{OP}$ from the origin to $P(a_1, a_2, a_3)$ is the **position vector** of $P$.
>
> *Stewart: 12.2 (text)*

^def-81-5

> [!theorem] Theorem §81.2: The Vector from A to B
> Given the points $A(x_1, y_1, z_1)$ and $B(x_2, y_2, z_2)$, the vector $\mathbf{a}$ with representation $\overrightarrow{AB}$ is
>
> $$
> \mathbf{a} = \langle x_2 - x_1,\ y_2 - y_1,\ z_2 - z_1 \rangle .
> $$
>
> *Stewart: 12.2, Equation 1*

^thm-81-2

> [!proof]+ Proof
> Let $\mathbf{a} = \langle a_1, a_2, a_3 \rangle = \overrightarrow{OP}$ with $P(a_1, a_2, a_3)$. The representation $\overrightarrow{AB}$ is the same displacement as $\overrightarrow{OP}$, so it moves $A$ by $a_1$ in $x$, $a_2$ in $y$ and $a_3$ in $z$: its terminal point is $(x_1 + a_1, y_1 + a_2, z_1 + a_3)$. Since that point is $B$, we get $x_1 + a_1 = x_2$, $y_1 + a_2 = y_2$, $z_1 + a_3 = z_2$, so $a_1 = x_2 - x_1$, $a_2 = y_2 - y_1$, $a_3 = z_2 - z_1$.

^pf-81-2

*Uses:* [[§81 Vectors#^def-81-5|Def. §81.5]]

> [!definition] Definition §81.6: Magnitude
> The **magnitude** or **length** of a vector $\mathbf{v}$ is the length of any of its representations; it is written $|\mathbf{v}|$ or $\|\mathbf{v}\|$.
>
> *Stewart: 12.2 (text)*

^def-81-6

> [!theorem] Theorem §81.3: Length of a Vector
> The length of the two-dimensional vector $\mathbf{a} = \langle a_1, a_2 \rangle$ is $|\mathbf{a}| = \sqrt{a_1^2 + a_2^2}$. The length of the three-dimensional vector $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$ is
>
> $$
> |\mathbf{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2} .
> $$
>
> *Stewart: 12.2 (boxed formulas)*

^thm-81-3

> [!proof]+ Proof
> Use the representation $\overrightarrow{OP}$ with $P(a_1, a_2, a_3)$. By the distance formula, its length is $\sqrt{(a_1 - 0)^2 + (a_2 - 0)^2 + (a_3 - 0)^2}$. The two-dimensional case is the same with the plane distance formula.

^pf-81-3

*Uses:* [[§81 Vectors#^def-81-6|Def. §81.6]], [[§80 Three-Dimensional Coordinate Systems#^thm-80-1|§80.1]]

> [!theorem] Theorem §81.4: Operations in Components
> If $\mathbf{a} = \langle a_1, a_2 \rangle$ and $\mathbf{b} = \langle b_1, b_2 \rangle$, then
>
> $$
> \mathbf{a} + \mathbf{b} = \langle a_1 + b_1,\ a_2 + b_2 \rangle, \qquad \mathbf{a} - \mathbf{b} = \langle a_1 - b_1,\ a_2 - b_2 \rangle, \qquad c\mathbf{a} = \langle ca_1,\ ca_2 \rangle .
> $$
>
> Similarly, for three-dimensional vectors,
>
> $$
> \begin{aligned}
> \langle a_1, a_2, a_3 \rangle + \langle b_1, b_2, b_3 \rangle &= \langle a_1 + b_1,\ a_2 + b_2,\ a_3 + b_3 \rangle, \\
> \langle a_1, a_2, a_3 \rangle - \langle b_1, b_2, b_3 \rangle &= \langle a_1 - b_1,\ a_2 - b_2,\ a_3 - b_3 \rangle, \\
> c\langle a_1, a_2, a_3 \rangle &= \langle ca_1,\ ca_2,\ ca_3 \rangle .
> \end{aligned}
> $$
>
> In words: to add or subtract vectors, add or subtract corresponding components; to multiply a vector by a scalar, multiply each component by that scalar.
>
> *Stewart: 12.2 (boxed formulas)*

^thm-81-4

*Stewart supports these formulas with the pictures described below (drawn for positive components), not with a proof; for $n$-dimensional vectors they become the definition of the operations ([[§81 Vectors#^def-81-7|Definition §81.7]]).*

> [!remark] Remark: Why It Works
> **Sum.** Draw $\mathbf{a} = \langle a_1, a_2 \rangle$ from the origin and then $\mathbf{b} = \langle b_1, b_2 \rangle$ from the tip $(a_1, a_2)$ of $\mathbf{a}$. The tip of $\mathbf{b}$ is $b_1$ further right and $b_2$ further up, at $(a_1 + b_1, a_2 + b_2)$. By the Triangle Law, $\mathbf{a} + \mathbf{b}$ is the arrow from the origin to that point.
>
> **Scalar multiple.** The arrow $\mathbf{a}$ is the hypotenuse of a right triangle with legs $a_1$ and $a_2$. For $c > 0$ the arrow $c\mathbf{a}$ points the same way and is $c$ times as long, so its triangle is similar to the first with ratio $c$ and has legs $ca_1$ and $ca_2$. For $c < 0$ the triangle is also reflected through the origin, which changes the sign of both legs. The difference then follows from $\mathbf{a} - \mathbf{b} = \mathbf{a} + (-1)\mathbf{b}$.

^rem-81-1

> [!definition] Definition §81.7: n-Dimensional Vectors
> $V_2$ and $V_3$ denote the sets of all two- and three-dimensional vectors. More generally, an **$n$-dimensional vector** is an ordered $n$-tuple
>
> $$
> \mathbf{a} = \langle a_1, a_2, \ldots, a_n \rangle
> $$
>
> of real numbers, the **components** of $\mathbf{a}$; their set is $V_n$. Addition and scalar multiplication in $V_n$ are defined componentwise, as in [[§81 Vectors#^thm-81-4|Theorem §81.4]].
>
> *Stewart: 12.2 (text)*

^def-81-7

> [!theorem] Theorem §81.5: Properties of Vectors
> If $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ are vectors in $V_n$ and $c$ and $d$ are scalars, then
>
> $$
> \begin{array}{ll}
> 1.\ \mathbf{a} + \mathbf{b} = \mathbf{b} + \mathbf{a} & 2.\ \mathbf{a} + (\mathbf{b} + \mathbf{c}) = (\mathbf{a} + \mathbf{b}) + \mathbf{c} \\
> 3.\ \mathbf{a} + \mathbf{0} = \mathbf{a} & 4.\ \mathbf{a} + (-\mathbf{a}) = \mathbf{0} \\
> 5.\ c(\mathbf{a} + \mathbf{b}) = c\mathbf{a} + c\mathbf{b} & 6.\ (c + d)\mathbf{a} = c\mathbf{a} + d\mathbf{a} \\
> 7.\ (cd)\mathbf{a} = c(d\mathbf{a}) & 8.\ 1\mathbf{a} = \mathbf{a}
> \end{array}
> $$
>
> *Stewart: 12.2, Properties of Vectors*

^thm-81-5

> [!proof]+ Proof
> Stewart proves Property 1 for $n = 2$ and leaves the rest as "readily verified". All eight follow the same way: write $\mathbf{a} = \langle a_1, \ldots, a_n \rangle$, $\mathbf{b} = \langle b_1, \ldots, b_n \rangle$, $\mathbf{c} = \langle c_1, \ldots, c_n \rangle$, compute each side in components by [[§81 Vectors#^def-81-7|Definition §81.7]], and use the corresponding law for real numbers in each component. Here $\mathbf{0} = \langle 0, \ldots, 0 \rangle$ and $-\mathbf{a} = (-1)\mathbf{a} = \langle -a_1, \ldots, -a_n \rangle$.
>
> 1. $\mathbf{a} + \mathbf{b} = \langle a_1 + b_1, \ldots, a_n + b_n \rangle = \langle b_1 + a_1, \ldots, b_n + a_n \rangle = \mathbf{b} + \mathbf{a}$ (commutativity of $+$ in $\mathbb{R}$).
> 2. Both sides have $i$-th component $a_i + b_i + c_i$, by associativity of $+$ in $\mathbb{R}$.
> 3. $\mathbf{a} + \mathbf{0} = \langle a_1 + 0, \ldots, a_n + 0 \rangle = \mathbf{a}$.
> 4. $\mathbf{a} + (-\mathbf{a}) = \langle a_1 - a_1, \ldots, a_n - a_n \rangle = \mathbf{0}$.
> 5. The $i$-th component of $c(\mathbf{a} + \mathbf{b})$ is $c(a_i + b_i) = ca_i + cb_i$, the $i$-th component of $c\mathbf{a} + c\mathbf{b}$ (distributive law in $\mathbb{R}$).
> 6. The $i$-th component of $(c + d)\mathbf{a}$ is $(c + d)a_i = ca_i + da_i$.
> 7. The $i$-th component of $(cd)\mathbf{a}$ is $(cd)a_i = c(da_i)$, the $i$-th component of $c(d\mathbf{a})$.
> 8. $1\mathbf{a} = \langle 1 \cdot a_1, \ldots, 1 \cdot a_n \rangle = \mathbf{a}$.

^pf-81-5

*Uses:* [[§81 Vectors#^def-81-7|Def. §81.7]]

> [!remark] Remark: The Geometric Meaning of Properties 1 and 2
> Property 1 is the Parallelogram Law ([[§81 Vectors#^thm-81-1|Theorem §81.1]]). Property 2, the associative law, can be seen by applying the Triangle Law several times: place $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ tip to tail, from a point $P$ to a point $Q$. Then $\overrightarrow{PQ}$ is obtained either by first forming $\mathbf{a} + \mathbf{b}$ and then adding $\mathbf{c}$, or by adding $\mathbf{a}$ to $\mathbf{b} + \mathbf{c}$.

^rem-81-2

> [!remark]- Connections
> - Properties 1–8 are exactly the axioms of a vector space ([[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]); $V_n$ is $\mathbb{R}^n$ with the componentwise operations of [[§1 Rⁿ and Cⁿ#^ladr-1-13|LADR 1.13]] and [[§1 Rⁿ and Cⁿ#^ladr-1-18|LADR 1.18]].
> - Matrix version: [[§3 Vector Equations#^thm-3-2|235 Thm. §3.2]] (the same eight properties for column vectors in $\mathbb{R}^n$), with linear combinations and spans of such vectors as the next step. The length of [[§81 Vectors#^thm-81-3|Theorem §81.3]] in $\mathbb{R}^n$: [[§40 Inner Product, Length, and Orthogonality#^def-40-2|235 Def. §40.2]].

> [!definition] Definition §81.8: Standard Basis Vectors
> The **standard basis vectors** in $V_3$ are
>
> $$
> \mathbf{i} = \langle 1, 0, 0 \rangle, \qquad \mathbf{j} = \langle 0, 1, 0 \rangle, \qquad \mathbf{k} = \langle 0, 0, 1 \rangle .
> $$
>
> They have length $1$ and point in the directions of the positive $x$-, $y$- and $z$-axes. In two dimensions, $\mathbf{i} = \langle 1, 0 \rangle$ and $\mathbf{j} = \langle 0, 1 \rangle$.
>
> *Stewart: 12.2 (boxed)*

^def-81-8

> [!theorem] Proposition §81.6: Components in Terms of i, j, k
> Every vector in $V_3$ and in $V_2$ can be written in terms of the standard basis vectors:
>
> $$
> \langle a_1, a_2, a_3 \rangle = a_1\mathbf{i} + a_2\mathbf{j} + a_3\mathbf{k}, \qquad \langle a_1, a_2 \rangle = a_1\mathbf{i} + a_2\mathbf{j} .
> $$
>
> For instance, $\langle 1, -2, 6 \rangle = \mathbf{i} - 2\mathbf{j} + 6\mathbf{k}$.
>
> *Stewart: 12.2, Equations 2 and 3*

^prop-81-6

> [!proof]+ Proof
> By [[§81 Vectors#^thm-81-4|Theorem §81.4]],
>
> $$
> \langle a_1, a_2, a_3 \rangle = \langle a_1, 0, 0 \rangle + \langle 0, a_2, 0 \rangle + \langle 0, 0, a_3 \rangle = a_1\langle 1, 0, 0 \rangle + a_2\langle 0, 1, 0 \rangle + a_3\langle 0, 0, 1 \rangle = a_1\mathbf{i} + a_2\mathbf{j} + a_3\mathbf{k} .
> $$
>
> The two-dimensional case is the same with two components.

^pf-81-6

*Uses:* [[§81 Vectors#^thm-81-4|§81.4]], [[§81 Vectors#^def-81-8|Def. §81.8]]

> [!definition] Definition §81.9: Unit Vector
> A **unit vector** is a vector whose length is $1$. For instance, $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$ are unit vectors.
>
> *Stewart: 12.2 (text)*

^def-81-9

> [!theorem] Proposition §81.7: The Unit Vector in the Direction of a
> If $\mathbf{a} \ne \mathbf{0}$, then the unit vector that has the same direction as $\mathbf{a}$ is
>
> $$
> \mathbf{u} = \frac{1}{|\mathbf{a}|}\,\mathbf{a} = \frac{\mathbf{a}}{|\mathbf{a}|} .
> $$
>
> *Stewart: 12.2, Equation 4*

^prop-81-7

> [!proof]+ Proof
> Let $c = 1/|\mathbf{a}|$, which is defined and positive because $\mathbf{a} \ne \mathbf{0}$. Then $\mathbf{u} = c\mathbf{a}$ with $c > 0$, so $\mathbf{u}$ has the same direction as $\mathbf{a}$ ([[§81 Vectors#^def-81-3|Definition §81.3]]), and
>
> $$
> |\mathbf{u}| = |c\mathbf{a}| = |c|\,|\mathbf{a}| = \frac{1}{|\mathbf{a}|}\,|\mathbf{a}| = 1 .
> $$

^pf-81-7

*Uses:* [[§81 Vectors#^def-81-3|Def. §81.3]], [[§81 Vectors#^def-81-9|Def. §81.9]]

> [!example] Example §81.1: Computing with Components
> **(a)** The vector represented by the directed segment from $A(2, -3, 4)$ to $B(-2, 1, 1)$ is, by [[§81 Vectors#^thm-81-2|Theorem §81.2]],
>
> $$
> \mathbf{a} = \langle -2 - 2,\ 1 - (-3),\ 1 - 4 \rangle = \langle -4, 4, -3 \rangle .
> $$
>
> **(b)** Let $\mathbf{a} = \langle 4, 0, 3 \rangle$ and $\mathbf{b} = \langle -2, 1, 5 \rangle$. Then $|\mathbf{a}| = \sqrt{4^2 + 0^2 + 3^2} = \sqrt{25} = 5$, and by [[§81 Vectors#^thm-81-4|Theorem §81.4]]
>
> $$
> \begin{aligned}
> \mathbf{a} + \mathbf{b} &= \langle 4 + (-2),\ 0 + 1,\ 3 + 5 \rangle = \langle 2, 1, 8 \rangle, \\
> \mathbf{a} - \mathbf{b} &= \langle 4 - (-2),\ 0 - 1,\ 3 - 5 \rangle = \langle 6, -1, -2 \rangle, \\
> 3\mathbf{b} &= \langle 3(-2),\ 3(1),\ 3(5) \rangle = \langle -6, 3, 15 \rangle, \\
> 2\mathbf{a} + 5\mathbf{b} &= \langle 8, 0, 6 \rangle + \langle -10, 5, 25 \rangle = \langle -2, 5, 31 \rangle .
> \end{aligned}
> $$
>
> **(c)** If $\mathbf{a} = \mathbf{i} + 2\mathbf{j} - 3\mathbf{k}$ and $\mathbf{b} = 4\mathbf{i} + 7\mathbf{k}$, then by Properties 1, 2, 5, 6 and 7 ([[§81 Vectors#^thm-81-5|Theorem §81.5]])
>
> $$
> 2\mathbf{a} + 3\mathbf{b} = 2\mathbf{i} + 4\mathbf{j} - 6\mathbf{k} + 12\mathbf{i} + 21\mathbf{k} = 14\mathbf{i} + 4\mathbf{j} + 15\mathbf{k} .
> $$
>
> *Stewart: Examples 12.2.3, 12.2.4 and 12.2.5*

^ex-81-1

> [!example] Example §81.2: A Unit Vector
> Find the unit vector in the direction of $2\mathbf{i} - \mathbf{j} - 2\mathbf{k}$.
>
> The vector has length $|2\mathbf{i} - \mathbf{j} - 2\mathbf{k}| = \sqrt{2^2 + (-1)^2 + (-2)^2} = \sqrt{9} = 3$, so by [[§81 Vectors#^prop-81-7|Proposition §81.7]] the unit vector with the same direction is
>
> $$
> \tfrac13 (2\mathbf{i} - \mathbf{j} - 2\mathbf{k}) = \tfrac23\,\mathbf{i} - \tfrac13\,\mathbf{j} - \tfrac23\,\mathbf{k} .
> $$
>
> *Stewart: Example 12.2.6*

^ex-81-2

> [!example] Example §81.3: The Fourth Vertex of a Parallelogram
> **(a)** $A(-2, 1, 3)$, $B(3, 5, 2)$ and $C(1, 2, 6)$ are three vertices of a parallelogram $ABCD$, with $AB$ and $BC$ two of its edges. Find the fourth vertex $D$.
>
> In the parallelogram $ABCD$ the side $AD$ is opposite to $BC$, so $\overrightarrow{AD} = \overrightarrow{BC}$. By [[§81 Vectors#^thm-81-2|Theorem §81.2]], $\overrightarrow{BC} = \langle 1 - 3,\ 2 - 5,\ 6 - 2 \rangle = \langle -2, -3, 4 \rangle$. So
>
> $$
> D = (-2 - 2,\ 1 - 3,\ 3 + 4) = (-4, -2, 7) .
> $$
>
> Check: $\overrightarrow{DC} = \langle 5, 4, -1 \rangle = \overrightarrow{AB}$.
>
> **(b)** Three vertices of a parallelogram are $P(0, -1, 1)$, $Q(0, 1, 0)$ and $R(2, 1, 1)$, and two of its sides are $PQ$ and $PR$. Find the fourth vertex.
>
> Now the two given sides meet at $P$, so by the Parallelogram Law ([[§81 Vectors#^thm-81-1|Theorem §81.1]]) the fourth vertex $S$ is the tip of $\overrightarrow{PQ} + \overrightarrow{PR}$ placed at $P$:
>
> $$
> \overrightarrow{PQ} + \overrightarrow{PR} = \langle 0, 2, -1 \rangle + \langle 2, 2, 0 \rangle = \langle 2, 4, -1 \rangle, \qquad S = (0 + 2,\ -1 + 4,\ 1 - 1) = (2, 3, 0) .
> $$
>
> Which vertex is "fourth" depends on which pairs of points are joined by sides: here $P$ is the vertex where the two given sides meet, in (a) it is $B$.
>
> *Source: 233 Midterm 1 Practice Questions, Q6(b); 233 SI Midterm 1 Problem Set, Q5(b)*

^ex-81-3

## Applications

> [!definition] Definition §81.10: Resultant Force
> A force is represented by a vector: it has a magnitude (in pounds or newtons) and a direction. If several forces act on an object, the **resultant force** experienced by the object is the vector sum of these forces.
>
> *Stewart: 12.2 (text)*

^def-81-10

> [!example] Example §81.4: Tensions in Two Wires
> A 100-lb weight hangs from two wires that make angles of $50^\circ$ and $32^\circ$ with the horizontal ceiling, the first going up to the left and the second up to the right. Find the tensions $\mathbf{T}_1$ and $\mathbf{T}_2$ and their magnitudes.
>
> Resolving into horizontal and vertical components,
>
> $$
> \mathbf{T}_1 = -|\mathbf{T}_1|\cos 50^\circ\,\mathbf{i} + |\mathbf{T}_1|\sin 50^\circ\,\mathbf{j} \qquad (5)
> \qquad\qquad
> \mathbf{T}_2 = |\mathbf{T}_2|\cos 32^\circ\,\mathbf{i} + |\mathbf{T}_2|\sin 32^\circ\,\mathbf{j} \qquad (6)
> $$
>
> The weight is $\mathbf{w} = -100\,\mathbf{j}$, and the weight hangs at rest, so the resultant force is zero: $\mathbf{T}_1 + \mathbf{T}_2 = -\mathbf{w} = 100\,\mathbf{j}$. Equating components,
>
> $$
> -|\mathbf{T}_1|\cos 50^\circ + |\mathbf{T}_2|\cos 32^\circ = 0, \qquad |\mathbf{T}_1|\sin 50^\circ + |\mathbf{T}_2|\sin 32^\circ = 100 .
> $$
>
> The first equation gives $|\mathbf{T}_2| = |\mathbf{T}_1|\cos 50^\circ / \cos 32^\circ$. Substituting into the second,
>
> $$
> |\mathbf{T}_1| \left( \sin 50^\circ + \cos 50^\circ\,\frac{\sin 32^\circ}{\cos 32^\circ} \right) = 100,
> \qquad
> |\mathbf{T}_1| = \frac{100}{\sin 50^\circ + \tan 32^\circ \cos 50^\circ} \approx \frac{100}{0.7660 + 0.4017} \approx 85.64\ \text{lb},
> $$
>
> and $|\mathbf{T}_2| = |\mathbf{T}_1|\cos 50^\circ/\cos 32^\circ \approx 85.64(0.6428)/0.8480 \approx 64.91$ lb. Substituting in (5) and (6),
>
> $$
> \mathbf{T}_1 \approx -55.05\,\mathbf{i} + 65.60\,\mathbf{j}, \qquad \mathbf{T}_2 \approx 55.05\,\mathbf{i} + 34.40\,\mathbf{j} .
> $$
>
> The horizontal components cancel and the vertical components add to $100$, as they must.
>
> *Stewart: Example 12.2.7*

^ex-81-4

> [!example] Example §81.5: Crossing a River
> A woman launches a boat from the south shore of a straight river that flows directly west at $4$ mi/h. She wants to land at the point directly across on the opposite shore. If the speed of the boat relative to the water is $8$ mi/h, in what direction should she steer?
>
> The **true course** of a boat is the direction of the resultant of its own velocity and the velocity of the current. Put the origin at the starting point, with $\mathbf{i}$ east and $\mathbf{j}$ north. The current is $\mathbf{v}_c = -4\,\mathbf{i}$. If she steers at angle $\theta$ from the positive $x$-axis, the boat's velocity in still water is $\mathbf{v}_b = 8(\cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j})$. The resultant velocity is
>
> $$
> \mathbf{v} = \mathbf{v}_b + \mathbf{v}_c = (-4 + 8\cos\theta)\,\mathbf{i} + (8\sin\theta)\,\mathbf{j} .
> $$
>
> To travel due north, the $x$-component must vanish: $-4 + 8\cos\theta = 0$, so $\cos\theta = \frac12$ and $\theta = 60^\circ$. She should steer at $60^\circ$ from east, that is, on the bearing N$\,30^\circ\,$E (turn $30^\circ$ from north toward east).
>
> *Stewart: Example 12.2.8*

^ex-81-5
