---
type: section
subject: "[[Calculus]]"
chapter: 12
section: 93
stewart: "12.1"
aliases: ["Stewart 12.1"]
tags: [calculus, math233]
---
← [[§92 Applications of Taylor Polynomials]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§94 Vectors]] →

*Stewart, Section 12.1 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q2), SI Midterm 1 Problem Set (Q3(b)).*

Multivariable calculus takes place in space, so the first step is to give every point of space three coordinates. This section sets up the right-handed coordinate system, explains how a single equation in $x$, $y$, $z$ describes a surface (and a pair of equations a curve), and extends the distance formula of the plane to space by applying the Pythagorean Theorem twice. The distance formula gives the equation of a sphere, and completing the square recognizes a sphere in disguise. Everything later in the course, from vectors to triple integrals, is written in these coordinates.

## 3D Space

> [!definition] Definition §109.1: Coordinate Axes, Coordinate Planes and Octants
> Choose a fixed point $O$, the **origin**, and three directed lines through $O$ that are perpendicular to each other, the **coordinate axes**, labeled the $x$-, $y$- and $z$-axes. The direction of the $z$-axis is fixed by the **right-hand rule**: if the fingers of the right hand curl around the $z$-axis in the direction of a $90^\circ$ counterclockwise rotation from the positive $x$-axis to the positive $y$-axis, the thumb points in the positive direction of the $z$-axis.
>
> The axes determine three **coordinate planes**: the $xy$-plane (containing the $x$- and $y$-axes), the $yz$-plane and the $xz$-plane. They divide space into eight **octants**; the **first octant** is the one determined by the positive axes.
>
> *Stewart: 12.1 (text)*

^def-93-1

> [!definition] Definition §109.2: Coordinates and the Space ℝ³
> For a point $P$ in space let $a$ be the (directed) distance from the $yz$-plane to $P$, $b$ the distance from the $xz$-plane to $P$, and $c$ the distance from the $xy$-plane to $P$. The ordered triple $(a, b, c)$ gives the **coordinates** of $P$: $a$ is its $x$-coordinate, $b$ its $y$-coordinate, $c$ its $z$-coordinate. To locate $(a, b, c)$, start at $O$, move $a$ units along the $x$-axis, then $b$ units parallel to the $y$-axis, then $c$ units parallel to the $z$-axis.
>
> The set of all ordered triples is the [[§7a Several Quantifiers and the Cartesian Product#^def-7a-1|Cartesian product]]
>
> $$
> \mathbb{R}^3 = \mathbb{R} \times \mathbb{R} \times \mathbb{R} = \{(x, y, z) \mid x, y, z \in \mathbb{R}\} .
> $$
>
> The one-to-one correspondence between points of space and triples in $\mathbb{R}^3$ is the **three-dimensional rectangular coordinate system**. In these terms the first octant is the set of points whose coordinates are all positive.
>
> The point $P(a, b, c)$ is a corner of a rectangular box whose opposite corner is $O$. Dropping a perpendicular from $P$ to the $xy$-plane gives $Q(a, b, 0)$, the **projection** of $P$ onto the $xy$-plane; likewise $R(0, b, c)$ and $S(a, 0, c)$ are the projections of $P$ onto the $yz$-plane and the $xz$-plane.
>
> *Stewart: 12.1 (text)*

^def-93-2

> [!remark] Remark: Visualizing the Octants
> Look at a bottom corner of a room and call the corner the origin. The wall on your left is the $xz$-plane, the wall on your right is the $yz$-plane, and the floor is the $xy$-plane. The $x$-axis runs along the line where the floor meets the left wall, the $y$-axis where it meets the right wall, and the $z$-axis runs up from the floor along the corner. You stand in the first octant; seven other rooms (three on the same floor, four on the floor below) fill the other octants, all sharing the corner $O$.

^rem-93-1

## Surfaces and Solids

In plane analytic geometry the graph of an equation in $x$ and $y$ is a curve in $\mathbb{R}^2$. In space, an equation in $x$, $y$ and $z$ represents a **surface** in $\mathbb{R}^3$.

> [!remark] Remark: Plane or Line? Read the Context
> The same equation can mean different things. $x = 2$ is a line in $\mathbb{R}^2$ (the vertical line through $(2, 0)$), but in $\mathbb{R}^3$ it is the plane of all points $(2, y, z)$, parallel to the $yz$-plane. In general, for a constant $k$,
> - $x = k$ is a plane parallel to the $yz$-plane,
> - $y = k$ is a plane parallel to the $xz$-plane,
> - $z = k$ is a plane parallel to the $xy$-plane.
>
> The faces of the box of [[§93 Three-Dimensional Coordinate Systems#^def-93-2|Definition §93.2]] lie in the three coordinate planes $x = 0$ (the $yz$-plane), $y = 0$ (the $xz$-plane), $z = 0$ (the $xy$-plane) and in the planes $x = a$, $y = b$, $z = c$. A *pair* of equations usually describes a curve (the intersection of two surfaces), and inequalities describe solid regions.

^rem-93-2

> [!example] Example §109.1: Planes in ℝ³
> What surfaces in $\mathbb{R}^3$ are represented by (a) $z = 3$, (b) $y = 5$, (c) $y = x$?
>
> **(a)** $z = 3$ is the set $\{(x, y, z) \mid z = 3\}$: all points whose $z$-coordinate is $3$, with $x$ and $y$ arbitrary. This is the horizontal plane parallel to the $xy$-plane, three units above it.
>
> **(b)** $y = 5$ is the set of all points whose $y$-coordinate is $5$: the vertical plane parallel to the $xz$-plane, five units to the right of it.
>
> **(c)** $y = x$ is the set $\{(x, x, z) \mid x \in \mathbb{R},\ z \in \mathbb{R}\}$ of points whose $x$- and $y$-coordinates are equal. The variable $z$ is free, so with each point $(x, x, 0)$ of the line $y = x$ in the $xy$-plane it contains the whole vertical line above and below it. It is a vertical plane meeting the $xy$-plane in the line $y = x$, $z = 0$.
>
> *Stewart: Examples 12.1.1 and 12.1.3*

^ex-93-1

> [!example] Example §109.2: A Circle, a Cylinder and a Solid Cylinder
> (a) Which points $(x, y, z)$ satisfy both $x^2 + y^2 = 1$ and $z = 3$?
> (b) What does the equation $x^2 + y^2 = 1$ alone represent as a surface in $\mathbb{R}^3$?
> (c) What solid region is described by $x^2 + y^2 \le 1$, $2 \le z \le 4$?
>
> **(a)** Since $z = 3$, the points lie in the horizontal plane $z = 3$ of [[§93 Three-Dimensional Coordinate Systems#^ex-93-1|Example §93.1]](a). Since $x^2 + y^2 = 1$, they lie on the circle of radius $1$ centered on the $z$-axis in that plane. The answer is a circle, described by a *pair* of equations.
>
> **(b)** Now $z$ is unrestricted. A point $(x, y, z)$ satisfies the equation exactly when $(x, y)$ lies on the unit circle, whatever $z$ is. So the surface consists of all the horizontal circles $x^2 + y^2 = 1$, $z = k$, for every $k$: the **circular cylinder** of radius $1$ whose axis is the $z$-axis.
>
> **(c)** $x^2 + y^2 \le 1$ says that $(x, y, z)$ lies on or inside the circle of radius $1$ centered on the $z$-axis in the horizontal plane through it. Together with $2 \le z \le 4$, the region is the part of the solid circular cylinder of radius $1$ about the $z$-axis that lies on or between the planes $z = 2$ and $z = 4$.
>
> *Stewart: Example 12.1.2*

^ex-93-2

## Distance and Spheres

> [!theorem] Theorem §109.1: Distance Formula in Three Dimensions
> The distance $|P_1P_2|$ between the points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ is
>
> $$
> |P_1P_2| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} .
> $$
>
> *Stewart: 12.1, Distance Formula in Three Dimensions*

^thm-93-1

> [!proof]+ Proof
> Build the rectangular box with faces parallel to the coordinate planes that has $P_1$ and $P_2$ as opposite vertices, and let $A(x_2, y_1, z_1)$ and $B(x_2, y_2, z_1)$ be the two vertices shown in the figure below. Going from $P_1$ to $A$ changes only the $x$-coordinate, from $A$ to $B$ only $y$, and from $B$ to $P_2$ only $z$, so
>
> $$
> |P_1A| = |x_2 - x_1|, \qquad |AB| = |y_2 - y_1|, \qquad |BP_2| = |z_2 - z_1| .
> $$
>
> Both triangles $P_1AB$ and $P_1BP_2$ are right-angled. (Stewart asserts this; here is why. The segment $P_1A$ is parallel to the $x$-axis and $AB$ to the $y$-axis, so they meet at a right angle at $A$. The points $P_1$, $A$, $B$ all lie in the horizontal plane $z = z_1$, while $BP_2$ is parallel to the $z$-axis, hence perpendicular to every line through $B$ in that plane, in particular to $P_1B$.) Two applications of the Pythagorean Theorem give
>
> $$
> |P_1P_2|^2 = |P_1B|^2 + |BP_2|^2 \qquad\text{and}\qquad |P_1B|^2 = |P_1A|^2 + |AB|^2 .
> $$
>
> Combining them,
>
> $$
> |P_1P_2|^2 = |P_1A|^2 + |AB|^2 + |BP_2|^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2 ,
> $$
>
> since $|u|^2 = u^2$ for every real $u$. Taking square roots gives the formula.

^pf-93-1

*Uses:* [[§93 Three-Dimensional Coordinate Systems#^def-93-2|Def. §93.2]], the Pythagorean Theorem

![[m233-80-1.svg]]
*The proof of the distance formula. The edges $P_1A$, $AB$, $BP_2$ of the box (blue, blue, green) have lengths $|x_2 - x_1|$, $|y_2 - y_1|$, $|z_2 - z_1|$. The floor diagonal $P_1B$ (dashed) is the hypotenuse of the blue right triangle and a leg of the green one, whose hypotenuse is the space diagonal $P_1P_2$ (red). Each right triangle contributes one application of Pythagoras.*

> [!remark]- Connections
> - The distance is the Euclidean norm of the difference, $\|P_2 - P_1\|$, where $\|v\| = \sqrt{v \cdot v}$: [[§20 Inner Products and Norms#^ladr-6-7|LADR 6.7]], with the formula in $\mathbb{R}^n$ as [[§20 Inner Products and Norms#^ladr-6-8|LADR 6.8]](a). It is the distance used for convergence in $\mathbb{R}^n$ in [[§1 Sequences and Limits in ℝⁿ#^def-1-1|452 Def. §1.1]].

For instance, the distance from $P(2, -1, 7)$ to $Q(1, -3, 5)$ is $|PQ| = \sqrt{(1 - 2)^2 + (-3 + 1)^2 + (5 - 7)^2} = \sqrt{1 + 4 + 4} = 3$ (Stewart, Example 12.1.4).

> [!definition] Definition §109.3: Sphere
> The **sphere** with radius $r$ and center $C(h, k, l)$ is the set of all points $P(x, y, z)$ whose distance from $C$ is $r$.
>
> *Stewart: 12.1 (text)*

^def-93-3

> [!theorem] Theorem §109.2: Equation of a Sphere
> An equation of the sphere with center $C(h, k, l)$ and radius $r$ is
>
> $$
> (x - h)^2 + (y - k)^2 + (z - l)^2 = r^2 .
> $$
>
> In particular, if the center is the origin $O$, an equation of the sphere is $x^2 + y^2 + z^2 = r^2$.
>
> *Stewart: 12.1, Equation of a Sphere*

^thm-93-2

> [!proof]+ Proof
> By [[§93 Three-Dimensional Coordinate Systems#^def-93-3|Definition §93.3]], $P(x, y, z)$ lies on the sphere if and only if $|PC| = r$, that is, by the distance formula,
>
> $$
> \sqrt{(x - h)^2 + (y - k)^2 + (z - l)^2} = r .
> $$
>
> Both sides are nonnegative, so this is equivalent to the equation obtained by squaring both sides. For the origin take $h = k = l = 0$.

^pf-93-2

*Uses:* [[§93 Three-Dimensional Coordinate Systems#^def-93-3|Def. §93.3]], [[§93 Three-Dimensional Coordinate Systems#^thm-93-1|§93.1]]

> [!remark] Remark: Method — Recognizing a Sphere
> An equation $x^2 + y^2 + z^2 + Gx + Hy + Iz + J = 0$, with the three squares having the same coefficient $1$ (divide through first if they share another coefficient), is handled by **completing the square** in each variable:
> 1. Group $x^2 + Gx$, $y^2 + Hy$, $z^2 + Iz$ and add $(G/2)^2$, $(H/2)^2$, $(I/2)^2$ to both sides.
> 2. Rewrite as $(x + G/2)^2 + (y + H/2)^2 + (z + I/2)^2 = R$, where $R = (G^2 + H^2 + I^2)/4 - J$.
> 3. If $R > 0$, it is the sphere with center $(-G/2, -H/2, -I/2)$ and radius $\sqrt{R}$. If $R = 0$ the only solution is the center itself, and if $R < 0$ there are no points at all.

^rem-93-3

> [!example] Example §109.3: Spheres Through a Given Point
> **(a)** Find an equation of the sphere with center $(3, -1, 6)$ that passes through $(5, 2, 3)$.
>
> The radius is the distance from the center to the given point:
>
> $$
> r = \sqrt{(5 - 3)^2 + [2 - (-1)]^2 + (3 - 6)^2} = \sqrt{4 + 9 + 9} = \sqrt{22} .
> $$
>
> By [[§93 Three-Dimensional Coordinate Systems#^thm-93-2|Theorem §93.2]] an equation is $(x - 3)^2 + (y + 1)^2 + (z - 6)^2 = 22$.
>
> **(b)** Find the equation of the sphere with center $(2, 1, 1)$ containing the point $(1, -1, 2)$.
>
> Here $r^2 = (1 - 2)^2 + (-1 - 1)^2 + (2 - 1)^2 = 1 + 4 + 1 = 6$, so the sphere is $(x - 2)^2 + (y - 1)^2 + (z - 1)^2 = 6$. (There is no need to take the square root: the equation uses $r^2$.)
>
> *Stewart: Example 12.1.5*
> *Source: 233 Midterm 1 Practice Questions, Q2(a)*

^ex-93-3

> [!example] Example §109.4: Completing the Square
> Show that each equation represents a sphere, and find its center and radius.
>
> $$
> \text{(a)}\ x^2 + y^2 + z^2 + 4x - 6y + 2z + 6 = 0 \qquad
> \text{(b)}\ x^2 + y^2 + z^2 - 2x - 6y - 8z + 17 = 0 \qquad
> \text{(c)}\ x^2 - 4x + y^2 + 4y + z^2 = 8
> $$
>
> **(a)** Completing the squares ([[§93 Three-Dimensional Coordinate Systems#^rem-93-3|the method above]]),
>
> $$
> (x^2 + 4x + 4) + (y^2 - 6y + 9) + (z^2 + 2z + 1) = -6 + 4 + 9 + 1 ,
> $$
>
> that is, $(x + 2)^2 + (y - 3)^2 + (z + 1)^2 = 8$. This is the sphere with center $(-2, 3, -1)$ and radius $\sqrt{8} = 2\sqrt{2}$.
>
> **(b)** $(x^2 - 2x + 1) + (y^2 - 6y + 9) + (z^2 - 8z + 16) = -17 + 1 + 9 + 16 = 9$, so $(x - 1)^2 + (y - 3)^2 + (z - 4)^2 = 9$: center $(1, 3, 4)$, radius $3$.
>
> **(c)** $(x^2 - 4x + 4) + (y^2 + 4y + 4) + z^2 = 8 + 4 + 4 = 16$, so $(x - 2)^2 + (y + 2)^2 + z^2 = 16$: center $(2, -2, 0)$, radius $4$.
>
> *Stewart: Example 12.1.6*
> *Source: 233 Midterm 1 Practice Questions, Q2(b); 233 SI Midterm 1 Problem Set, Q3(b)*

^ex-93-4

> [!example] Example §109.5: A Region Between Two Spheres
> What region in $\mathbb{R}^3$ is represented by $1 \le x^2 + y^2 + z^2 \le 4$, $z \le 0$?
>
> Taking square roots (all quantities are nonnegative), the first condition says
>
> $$
> 1 \le \sqrt{x^2 + y^2 + z^2} \le 2 ,
> $$
>
> so the distance from $(x, y, z)$ to the origin is at least $1$ and at most $2$ ([[§93 Three-Dimensional Coordinate Systems#^thm-93-1|Theorem §93.1]]). The condition $z \le 0$ says the point lies on or below the $xy$-plane. So the region is the part of the solid between (or on) the spheres $x^2 + y^2 + z^2 = 1$ and $x^2 + y^2 + z^2 = 4$ that lies on or beneath the $xy$-plane: half of a thick spherical shell, like a bowl.
>
> *Stewart: Example 12.1.7*

^ex-93-5
