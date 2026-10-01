---
type: section
subject: "[[Calculus]]"
chapter: 12
section: 84
stewart: "12.5"
aliases: ["Stewart 12.5"]
tags: [calculus, math233]
---
← [[§83 The Cross Product]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§85 Cylinders and Quadric Surfaces]] →

*Stewart, Section 12.5 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q4, Q6(a), Q7, Q8, Q9, Q10), Practice Exam 1 (Q1(b), Q2), SI Midterm 1 Problem Set (Q1, Q2).*

A line in space is determined by a point and a direction vector, a plane by a point and a normal vector. This section writes both down: lines by vector, parametric and symmetric equations, planes by a vector equation $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ that expands to a linear equation $ax + by + cz + d = 0$. The tools of the previous two sections do all the work: the cross product produces a normal vector from two vectors in a plane or a direction vector from two normals, the dot product gives angles between planes, and the scalar projection gives the distance from a point to a plane, hence between parallel planes and between skew lines. This is the most heavily examined section of Chapter 12.

## Lines

> [!theorem] Theorem §84.1: Vector Equation of a Line
> Let $L$ be the line through the point $P_0(x_0, y_0, z_0)$ parallel to the vector $\mathbf{v} \ne \mathbf{0}$, and let $\mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle$ be the position vector of $P_0$. A point $P$ with position vector $\mathbf{r}$ lies on $L$ if and only if
>
> $$
> \mathbf{r} = \mathbf{r}_0 + t\mathbf{v} \qquad (1)
> $$
>
> for some real number $t$.
>
> *Stewart: 12.5, Equation 1*

^thm-84-1

> [!proof]+ Proof
> Let $\mathbf{a}$ be the vector with representation $\overrightarrow{P_0P}$. By the Triangle Law, $\mathbf{r} = \mathbf{r}_0 + \mathbf{a}$. If $P$ is on $L$, then $\mathbf{a}$ lies along $L$, so it is parallel to $\mathbf{v}$ (or zero), and there is a scalar $t$ with $\mathbf{a} = t\mathbf{v}$; thus $\mathbf{r} = \mathbf{r}_0 + t\mathbf{v}$. Conversely, if $\mathbf{r} = \mathbf{r}_0 + t\mathbf{v}$, then $\overrightarrow{P_0P} = t\mathbf{v}$ is parallel to $\mathbf{v}$ (or zero), so $P$ lies on the line through $P_0$ in the direction of $\mathbf{v}$.

^pf-84-1

*Uses:* [[§81 Vectors#^def-81-2|Def. §81.2]], [[§81 Vectors#^def-81-3|Def. §81.3]]

> [!definition] Definition §84.1: Vector Equation, Parameter, Direction Numbers
> Equation (1) is a **vector equation** of $L$, and $t$ is the **parameter**: each value of $t$ gives the position vector of one point of $L$, and as $t$ varies the line is traced out by the tip of $\mathbf{r}$. Positive values of $t$ give points on one side of $P_0$, negative values points on the other side.
>
> If $\mathbf{v} = \langle a, b, c \rangle$ is used to describe the direction of $L$, then $a$, $b$, $c$ are **direction numbers** of $L$. Any three numbers proportional to $a$, $b$, $c$ are also direction numbers of $L$.
>
> *Stewart: 12.5 (text)*

^def-84-1

> [!theorem] Proposition §84.2: Parametric Equations of a Line
> Parametric equations for the line through the point $(x_0, y_0, z_0)$ and parallel to the direction vector $\langle a, b, c \rangle$ are
>
> $$
> x = x_0 + at, \qquad y = y_0 + bt, \qquad z = z_0 + ct \qquad (t \in \mathbb{R}) .
> $$
>
> *Stewart: 12.5, Equation 2*

^prop-84-2

> [!proof]+ Proof
> With $\mathbf{r} = \langle x, y, z \rangle$, $\mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle$ and $\mathbf{v} = \langle a, b, c \rangle$, Equation (1) reads $\langle x, y, z \rangle = \langle x_0 + ta, y_0 + tb, z_0 + tc \rangle$. Two vectors are equal if and only if corresponding components are equal.

^pf-84-2

*Uses:* [[§84 Equations of Lines and Planes#^thm-84-1|§84.1]], [[§81 Vectors#^thm-81-4|§81.4]]

> [!remark] Remark: Equations of a Line Are Not Unique
> Changing the point or the direction vector changes the equations but not the line. The line through $(5, 1, 3)$ parallel to $\mathbf{i} + 4\mathbf{j} - 2\mathbf{k}$ is $x = 5 + t$, $y = 1 + 4t$, $z = 3 - 2t$; starting instead from its point $(6, 5, 1)$ gives $x = 6 + t$, $y = 5 + 4t$, $z = 1 - 2t$, and using the parallel vector $2\mathbf{i} + 8\mathbf{j} - 4\mathbf{k}$ gives $x = 5 + 2t$, $y = 1 + 8t$, $z = 3 - 4t$. To decide whether two descriptions give the same line, check that the direction vectors are parallel and that one point of the first lies on the second.

^rem-84-1

> [!theorem] Proposition §84.3: Symmetric Equations of a Line
> If none of the direction numbers $a$, $b$, $c$ is $0$, the line of [[§84 Equations of Lines and Planes#^prop-84-2|Proposition §84.2]] is described by the **symmetric equations**
>
> $$
> \frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c} . \qquad (3)
> $$
>
> If one of them is $0$, say $a = 0$, the line is described by $x = x_0$, $\dfrac{y - y_0}{b} = \dfrac{z - z_0}{c}$, so it lies in the vertical plane $x = x_0$. For the line through $P_0(x_0, y_0, z_0)$ and $P_1(x_1, y_1, z_1)$ the direction numbers are $x_1 - x_0$, $y_1 - y_0$, $z_1 - z_0$, and the symmetric equations are
>
> $$
> \frac{x - x_0}{x_1 - x_0} = \frac{y - y_0}{y_1 - y_0} = \frac{z - z_0}{z_1 - z_0} .
> $$
>
> *Stewart: 12.5, Equation 3*

^prop-84-3

> [!proof]+ Proof
> If $a, b, c \ne 0$, solve each parametric equation for $t$: $t = (x - x_0)/a$, $t = (y - y_0)/b$, $t = (z - z_0)/c$. A point is on the line if and only if one $t$ satisfies all three, that is, if and only if the three quotients are equal. If $a = 0$ the first parametric equation says $x = x_0$ for every $t$, and $t$ is eliminated from the other two in the same way. For the line through $P_0$ and $P_1$, the vector $\overrightarrow{P_0P_1} = \langle x_1 - x_0, y_1 - y_0, z_1 - z_0 \rangle$ is parallel to it ([[§81 Vectors#^thm-81-2|Theorem §81.2]]).

^pf-84-3

*Uses:* [[§84 Equations of Lines and Planes#^prop-84-2|§84.2]], [[§81 Vectors#^thm-81-2|§81.2]]

> [!theorem] Proposition §84.4: Line Segment
> The line segment from $\mathbf{r}_0$ to $\mathbf{r}_1$ is given by the vector equation
>
> $$
> \mathbf{r}(t) = (1 - t)\mathbf{r}_0 + t\mathbf{r}_1, \qquad 0 \le t \le 1 .
> $$
>
> *Stewart: 12.5, Equation 4*

^prop-84-4

> [!proof]+ Proof
> The line through (the tips of) $\mathbf{r}_0$ and $\mathbf{r}_1$ has direction vector $\mathbf{v} = \mathbf{r}_1 - \mathbf{r}_0$, so by [[§84 Equations of Lines and Planes#^thm-84-1|Theorem §84.1]] its vector equation is $\mathbf{r} = \mathbf{r}_0 + t(\mathbf{r}_1 - \mathbf{r}_0) = (1 - t)\mathbf{r}_0 + t\mathbf{r}_1$. The value $t = 0$ gives $\mathbf{r}_0$ and $t = 1$ gives $\mathbf{r}_1$, and the points between them correspond to $0 \le t \le 1$ (for these $t$, $\overrightarrow{P_0P} = t(\mathbf{r}_1 - \mathbf{r}_0)$ points toward $\mathbf{r}_1$ and is no longer than $\mathbf{r}_1 - \mathbf{r}_0$).

^pf-84-4

*Uses:* [[§84 Equations of Lines and Planes#^thm-84-1|§84.1]]

> [!example] Example §84.1: Lines Through Given Points
> **(a)** Find a vector equation and parametric equations for the line through $(5, 1, 3)$ parallel to $\mathbf{i} + 4\mathbf{j} - 2\mathbf{k}$, and two other points on it.
>
> Here $\mathbf{r}_0 = 5\mathbf{i} + \mathbf{j} + 3\mathbf{k}$ and $\mathbf{v} = \mathbf{i} + 4\mathbf{j} - 2\mathbf{k}$, so $\mathbf{r} = (5 + t)\mathbf{i} + (1 + 4t)\mathbf{j} + (3 - 2t)\mathbf{k}$, that is, $x = 5 + t$, $y = 1 + 4t$, $z = 3 - 2t$. The value $t = 1$ gives the point $(6, 5, 1)$ and $t = -1$ gives $(4, -3, 5)$.
>
> **(b)** Find parametric and symmetric equations of the line through $A(2, 4, -3)$ and $B(3, -1, 1)$. Where does it meet the $xy$-plane? Which parameter values give the segment $AB$?
>
> The vector $\mathbf{v} = \overrightarrow{AB} = \langle 3 - 2, -1 - 4, 1 - (-3) \rangle = \langle 1, -5, 4 \rangle$ is parallel to the line. With $P_0 = A$,
>
> $$
> x = 2 + t, \quad y = 4 - 5t, \quad z = -3 + 4t \qquad\text{and}\qquad \frac{x - 2}{1} = \frac{y - 4}{-5} = \frac{z + 3}{4} .
> $$
>
> The line meets the $xy$-plane when $z = -3 + 4t = 0$, that is, $t = \frac34$; then $x = 2 + \frac34 = \frac{11}{4}$ and $y = 4 - 5 \cdot \frac34 = \frac14$, so the point is $\big(\frac{11}{4}, \frac14, 0\big)$. (Equivalently, put $z = 0$ in the symmetric equations: $\frac{x - 2}{1} = \frac{y - 4}{-5} = \frac34$.) Since $t = 0$ gives $A$ and $t = 1$ gives $B$, the segment $AB$ is $x = 2 + t$, $y = 4 - 5t$, $z = -3 + 4t$ with $0 \le t \le 1$, or $\mathbf{r}(t) = \langle 2 + t, 4 - 5t, -3 + 4t \rangle$, $0 \le t \le 1$.
>
> **(c)** The line through $A(-2, 1, 3)$ and $B(3, 5, 2)$ has direction $\overrightarrow{AB} = \langle 5, 4, -1 \rangle$ and parametric equations $x = -2 + 5t$, $y = 1 + 4t$, $z = 3 - t$; the line through $(1, 2, 3)$ and $(4, 6, 5)$ has direction $\langle 3, 4, 2 \rangle$ and equations $x = 1 + 3t$, $y = 2 + 4t$, $z = 3 + 2t$.
>
> *Stewart: Examples 12.5.1 and 12.5.2*
> *Source: 233 Midterm 1 Practice Questions, Q6(a); 233 SI Midterm 1 Problem Set, Q1(a)*

^ex-84-1

> [!definition] Definition §84.2: Skew Lines
> Two lines are **skew lines** if they do not intersect and are not parallel (and therefore do not lie in the same plane).
>
> *Stewart: 12.5 (text)*

^def-84-2

> [!remark] Remark: Method — Parallel, Intersecting or Skew
> Given $L_1$: $\mathbf{r} = \mathbf{r}_1 + t\mathbf{v}_1$ and $L_2$: $\mathbf{r} = \mathbf{r}_2 + s\mathbf{v}_2$ (use *different* parameters for the two lines):
> 1. If $\mathbf{v}_1$ and $\mathbf{v}_2$ are parallel (components proportional), the lines are parallel or identical; they are identical if a point of $L_1$ lies on $L_2$.
> 2. Otherwise, set the coordinates equal: three equations in the two unknowns $t$, $s$. Solve two of them.
> 3. If the solution satisfies the third equation, the lines intersect, at the point given by that $t$ (or $s$). If not, they are skew.

^rem-84-2

> [!example] Example §84.2: Skew Lines
> **(a)** Show that $L_1$: $x = 1 + t$, $y = -2 + 3t$, $z = 4 - t$ and $L_2$: $x = 2s$, $y = 3 + s$, $z = -3 + 4s$ are skew.
>
> The direction vectors $\langle 1, 3, -1 \rangle$ and $\langle 2, 1, 4 \rangle$ are not parallel (their components are not proportional). An intersection point would need $t$, $s$ with
>
> $$
> 1 + t = 2s, \qquad -2 + 3t = 3 + s, \qquad 4 - t = -3 + 4s .
> $$
>
> The first gives $s = (1 + t)/2$; then the second becomes $-4 + 6t = 7 + t$, so $t = \frac{11}{5}$ and $s = \frac85$. In the third equation, $4 - \frac{11}{5} = \frac95$ but $-3 + \frac{32}{5} = \frac{17}{5}$. So there are no such $t$, $s$: the lines do not intersect, and they are skew.
>
> **(b)** Are $L_1$: $x = 1 + 2t$, $y = 3t$, $z = 2 - t$ and $L_2$: $x = -1 + s$, $y = 4 + s$, $z = 1 + 3s$ parallel, skew or intersecting?
>
> The directions $\langle 2, 3, -1 \rangle$ and $\langle 1, 1, 3 \rangle$ are not parallel. From $1 + 2t = -1 + s$ we get $s = 2 + 2t$, and then $3t = 4 + s = 6 + 2t$ gives $t = 6$, $s = 14$. The $z$-coordinates are $2 - 6 = -4$ and $1 + 42 = 43$, which differ. The lines are skew.
>
> *Stewart: Example 12.5.3*
> *Source: 233 Midterm 1 Practice Questions, Q10*

^ex-84-2

## Planes

> [!definition] Definition §84.3: Normal Vector
> A plane in space is determined by a point $P_0(x_0, y_0, z_0)$ in the plane and a vector $\mathbf{n}$ orthogonal to the plane, called a **normal vector**. (A single vector parallel to the plane does not determine its "direction", but a perpendicular one does.)
>
> *Stewart: 12.5 (text)*

^def-84-3

> [!theorem] Theorem §84.5: Vector Equation of a Plane
> Let $\mathbf{r}_0$ be the position vector of $P_0$. A point $P$ with position vector $\mathbf{r}$ lies in the plane through $P_0$ with normal vector $\mathbf{n}$ if and only if
>
> $$
> \mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0, \qquad\text{equivalently}\qquad \mathbf{n} \cdot \mathbf{r} = \mathbf{n} \cdot \mathbf{r}_0 . \qquad (5),\ (6)
> $$
>
> Either equation is called a **vector equation of the plane**.
>
> *Stewart: 12.5, Equations 5 and 6*

^thm-84-5

> [!proof]+ Proof
> The vector $\mathbf{r} - \mathbf{r}_0$ is represented by $\overrightarrow{P_0P}$. If $P$ is in the plane, $\overrightarrow{P_0P}$ lies in the plane and the normal vector is orthogonal to it, so $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ by [[§82 The Dot Product#^thm-82-4|Theorem §82.4]]. Conversely, the vectors from $P_0$ orthogonal to $\mathbf{n}$ are exactly those lying in the plane through $P_0$ perpendicular to $\mathbf{n}$, so if $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ then $P$ is in the plane. Equation (6) is (5) rewritten using Property 3 of [[§82 The Dot Product#^thm-82-1|Theorem §82.1]].

^pf-84-5

*Uses:* [[§84 Equations of Lines and Planes#^def-84-3|Def. §84.3]], [[§82 The Dot Product#^thm-82-4|§82.4]], [[§82 The Dot Product#^thm-82-1|§82.1]]

> [!theorem] Proposition §84.6: Scalar Equation of a Plane
> A **scalar equation of the plane** through $P_0(x_0, y_0, z_0)$ with normal vector $\mathbf{n} = \langle a, b, c \rangle$ is
>
> $$
> a(x - x_0) + b(y - y_0) + c(z - z_0) = 0 . \qquad (7)
> $$
>
> *Stewart: 12.5, Equation 7*

^prop-84-6

> [!proof]+ Proof
> With $\mathbf{r} = \langle x, y, z \rangle$ and $\mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle$, Equation (5) reads $\langle a, b, c \rangle \cdot \langle x - x_0, y - y_0, z - z_0 \rangle = 0$; expand the dot product.

^pf-84-6

*Uses:* [[§84 Equations of Lines and Planes#^thm-84-5|§84.5]], [[§82 The Dot Product#^def-82-1|Def. §82.1]]

> [!theorem] Proposition §84.7: Planes Are Linear Equations
> Every plane has an equation of the form
>
> $$
> ax + by + cz + d = 0 , \qquad (8)
> $$
>
> a **linear equation** in $x$, $y$, $z$, where $\langle a, b, c \rangle$ is a normal vector. Conversely, if $a$, $b$, $c$ are not all $0$, the linear equation (8) represents a plane with normal vector $\langle a, b, c \rangle$.
>
> *Stewart: 12.5, Equation 8*

^prop-84-7

> [!proof]+ Proof
> Expanding (7) gives (8) with $d = -(ax_0 + by_0 + cz_0)$. For the converse (Stewart's Exercise 83), let $\mathbf{n} = \langle a, b, c \rangle \ne \mathbf{0}$ and put $\mathbf{r}_0 = -\dfrac{d}{a^2 + b^2 + c^2}\,\mathbf{n}$. Then $\mathbf{n} \cdot \mathbf{r}_0 = -d$, so (8), which says $\mathbf{n} \cdot \mathbf{r} = -d$, is the same as $\mathbf{n} \cdot \mathbf{r} = \mathbf{n} \cdot \mathbf{r}_0$. By [[§84 Equations of Lines and Planes#^thm-84-5|Theorem §84.5]] this is the plane through the point with position vector $\mathbf{r}_0$ with normal vector $\mathbf{n}$.

^pf-84-7

*Uses:* [[§84 Equations of Lines and Planes#^prop-84-6|§84.6]], [[§84 Equations of Lines and Planes#^thm-84-5|§84.5]]

> [!remark]- Connections
> - A plane through the origin is the orthogonal complement $\{\mathbf{n}\}^\perp$ of a normal vector ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]]), and any plane or line is a translate $\mathbf{r}_0 + U$ of a 2- or 1-dimensional subspace $U$ ([[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97]]); so is the solution set of any consistent linear system.

> [!example] Example §84.3: Equations of Planes and Where a Line Meets a Plane
> **(a)** The plane through $(2, 4, -1)$ with normal vector $\mathbf{n} = \langle 2, 3, 4 \rangle$ is $2(x - 2) + 3(y - 4) + 4(z + 1) = 0$, or $2x + 3y + 4z = 12$. Setting $y = z = 0$ gives the $x$-intercept $6$; similarly the $y$-intercept is $4$ and the $z$-intercept is $3$, which is enough to sketch the triangular piece of the plane in the first octant.
>
> **(b)** Find an equation of the plane through $P(1, 3, 2)$, $Q(3, -1, 6)$ and $R(5, 2, 0)$. The vectors $\mathbf{a} = \overrightarrow{PQ} = \langle 2, -4, 4 \rangle$ and $\mathbf{b} = \overrightarrow{PR} = \langle 4, -1, -2 \rangle$ lie in the plane, so their cross product is a normal vector ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]]):
>
> $$
> \mathbf{n} = \mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & -4 & 4 \\ 4 & -1 & -2 \end{vmatrix} = (8 + 4)\mathbf{i} - (-4 - 16)\mathbf{j} + (-2 + 16)\mathbf{k} = 12\mathbf{i} + 20\mathbf{j} + 14\mathbf{k} .
> $$
>
> With the point $P$: $12(x - 1) + 20(y - 3) + 14(z - 2) = 0$, or $6x + 10y + 7z = 50$. (The same method gives $-3(x - 3) + (y - 1) + 2(z - 1) = 0$ for the plane through $(3, 1, 1)$, $(4, 2, 2)$, $(4, 4, 1)$; and $6x + 3y + 2z = 6$ for the plane through $(1, 0, 0)$, $(0, 2, 0)$, $(0, 0, 3)$.)
>
> **(c)** Find the plane through $(9, 0, -3)$ containing the line $x = 7 - 2t$, $y = 1 + 3t$, $z = 6 + 4t$. The line supplies one vector in the plane, its direction $\mathbf{v} = \langle -2, 3, 4 \rangle$, and one point, $P_0(7, 1, 6)$ (at $t = 0$). A second vector in the plane runs from $P_0$ to the given point: $\mathbf{w} = \langle 2, -1, -9 \rangle$. Then
>
> $$
> \mathbf{v} \times \mathbf{w} = \big(3(-9) - 4(-1),\ 4(2) - (-2)(-9),\ (-2)(-1) - 3(2)\big) = \langle -23, -10, -4 \rangle ,
> $$
>
> so $\mathbf{n} = \langle 23, 10, 4 \rangle$ is normal, and the plane is $23(x - 9) + 10y + 4(z + 3) = 0$, or $23x + 10y + 4z - 195 = 0$. Check with $P_0$: $161 + 10 + 24 = 195$.
>
> **(d)** The lines $L_1$: $x = 1 - t$, $y = 2 + t$, $z = 1 + t$ and $L_2$: $x = 4s$, $y = 3 + 6s$, $z = 2 + 4s$ both pass through $P(0, 3, 2)$ (at $t = 1$ and $s = 0$), but they are different lines: the point $(1, 2, 1)$ of $L_1$ ($t = 0$) is not on $L_2$, since $x = 4s = 1$ forces $s = \frac14$ and then $y = 4.5 \ne 2$. Two intersecting lines lie in one plane, with normal vector
>
> $$
> \langle -1, 1, 1 \rangle \times \langle 4, 6, 4 \rangle = \big(1(4) - 1(6),\ 1(4) - (-1)(4),\ (-1)(6) - 1(4)\big) = \langle -2, 8, -10 \rangle ,
> $$
>
> so the plane is $-2(x - 0) + 8(y - 3) - 10(z - 2) = 0$, or $-2x + 8y - 10z - 4 = 0$ (equivalently $x - 4y + 5z + 2 = 0$).
>
> **(e)** *Where a line meets a plane.* Find the point where the line $x = 2 + 3t$, $y = -4t$, $z = 5 + t$ meets the plane $4x + 5y - 2z = 18$.
>
> Substitute the parametric equations into the equation of the plane:
>
> $$
> 4(2 + 3t) + 5(-4t) - 2(5 + t) = 18 \quad\Longrightarrow\quad -2 - 10t = 18 \quad\Longrightarrow\quad t = -2 .
> $$
>
> So the intersection point is $x = 2 - 6 = -4$, $y = 8$, $z = 5 - 2 = 3$: the point $(-4, 8, 3)$.
>
> **(f)** Find parametric equations of the line $L$ through $A(1, 2, 3)$ perpendicular to the plane $x - y + 2z = -1$, and the point $B$ where $L$ meets the plane.
>
> A line perpendicular to a plane is parallel to its normal vector $\langle 1, -1, 2 \rangle$ (read off from the coefficients, [[§84 Equations of Lines and Planes#^prop-84-7|Proposition §84.7]]). So $L$: $x = 1 + t$, $y = 2 - t$, $z = 3 + 2t$. Substituting,
>
> $$
> (1 + t) - (2 - t) + 2(3 + 2t) = -1 \quad\Longrightarrow\quad 5 + 6t = -1 \quad\Longrightarrow\quad t = -1 ,
> $$
>
> so $B = (0, 3, 1)$. Check: $0 - 3 + 2 = -1$. ($B$ is the point of the plane closest to $A$, the foot of the perpendicular.)
>
> *In (d), the practice sheet prints $L_1$ with $z = 1 + s$; its answer ("for $t = 1$ and $s = 0$ we get $P$") and the plane both require $z = 1 + t$, which is used here.*
>
> *Stewart: Examples 12.5.4, 12.5.5 and 12.5.6*
> *Source: 233 Midterm 1 Practice Questions, Q4, Q7(a), Q8, Q9; 233 Practice Exam 1, Q2(a)*

^ex-84-3

> [!definition] Definition §84.4: Parallel Planes and the Angle Between Planes
> Two planes are **parallel** if their normal vectors are parallel. If two planes are not parallel, they intersect in a straight line, and the **angle between the two planes** is the acute angle between their normal vectors.
>
> *Stewart: 12.5 (text)*

^def-84-4

> [!remark] Remark: A Line as the Intersection of Two Planes
> Two nonparallel planes $a_1x + b_1y + c_1z + d_1 = 0$ and $a_2x + b_2y + c_2z + d_2 = 0$ meet in a line, so a pair of linear equations can represent a line. The line is perpendicular to both normal vectors, so $\mathbf{n}_1 \times \mathbf{n}_2$ is a direction vector for it ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]]); a point on it is found by fixing one variable (often $z = 0$) and solving for the other two. Conversely, the symmetric equations (3) exhibit a line as the intersection of the two planes $\frac{x - x_0}{a} = \frac{y - y_0}{b}$ and $\frac{y - y_0}{b} = \frac{z - z_0}{c}$. Another way to find the line of intersection is to solve the two equations for two of the variables in terms of the third, which serves as the parameter.

^rem-84-3

> [!example] Example §84.4: The Angle and the Line Between Two Planes
> **(a)** Find the angle between the planes $x + y + z = 1$ and $x - 2y + 3z = 1$, and symmetric equations for their line of intersection $L$.
>
> The normal vectors are $\mathbf{n}_1 = \langle 1, 1, 1 \rangle$ and $\mathbf{n}_2 = \langle 1, -2, 3 \rangle$. By [[§82 The Dot Product#^cor-82-3|Corollary §82.3]],
>
> $$
> \cos\theta = \frac{\mathbf{n}_1 \cdot \mathbf{n}_2}{|\mathbf{n}_1|\,|\mathbf{n}_2|} = \frac{1 - 2 + 3}{\sqrt3\,\sqrt{14}} = \frac{2}{\sqrt{42}}, \qquad \theta = \cos^{-1}\!\Big(\frac{2}{\sqrt{42}}\Big) \approx 72^\circ .
> $$
>
> For a point on $L$, set $z = 0$: then $x + y = 1$ and $x - 2y = 1$, so $y = 0$, $x = 1$, and $(1, 0, 0)$ is on $L$. A direction vector is
>
> $$
> \mathbf{v} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 1 & -2 & 3 \end{vmatrix} = 5\mathbf{i} - 2\mathbf{j} - 3\mathbf{k}, \qquad\text{so}\qquad L:\ \frac{x - 1}{5} = \frac{y}{-2} = \frac{z}{-3} .
> $$
>
> **(b)** The planes $x + 2y = 0$ and $x + 2z = 3$ have normals $\langle 1, 2, 0 \rangle$ and $\langle 1, 0, 2 \rangle$, so the cosine of the angle between them is $\dfrac{1}{\sqrt5\,\sqrt5} = \dfrac15$.
>
> **(c)** The planes $x - 2y + z = 10$ and $2x + y - z = 0$ meet in a line with direction $\langle 1, -2, 1 \rangle \times \langle 2, 1, -1 \rangle = \langle 2 - 1,\ 2 + 1,\ 1 + 4 \rangle = \langle 1, 3, 5 \rangle$. Setting $z = 0$ gives $x - 2y = 10$, $2x + y = 0$, so $y = -2x$, $5x = 10$, and the point $(2, -4, 0)$. Parametric equations: $x = 2 + t$, $y = -4 + 3t$, $z = 5t$.
>
> *Stewart: Example 12.5.7*
> *Source: 233 Practice Exam 1, Q1(b); 233 SI Midterm 1 Problem Set, Q1(b)*

^ex-84-4

## Distances

> [!theorem] Theorem §84.8: Distance from a Point to a Plane
> The distance $D$ from the point $P_1(x_1, y_1, z_1)$ to the plane $ax + by + cz + d = 0$ is
>
> $$
> D = \frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2 + b^2 + c^2}} .
> $$
>
> *Stewart: 12.5, Equation 9*

^thm-84-8

> [!proof]+ Proof
> Let $P_0(x_0, y_0, z_0)$ be any point in the plane and $\mathbf{b} = \overrightarrow{P_0P_1} = \langle x_1 - x_0, y_1 - y_0, z_1 - z_0 \rangle$. The distance from $P_1$ to the plane is measured along the normal $\mathbf{n} = \langle a, b, c \rangle$, so it is the absolute value of the scalar projection of $\mathbf{b}$ onto $\mathbf{n}$ (figure below). By [[§82 The Dot Product#^thm-82-6|Theorem §82.6]],
>
> $$
> D = |\operatorname{comp}_{\mathbf{n}}\mathbf{b}| = \frac{|\mathbf{n} \cdot \mathbf{b}|}{|\mathbf{n}|} = \frac{|a(x_1 - x_0) + b(y_1 - y_0) + c(z_1 - z_0)|}{\sqrt{a^2 + b^2 + c^2}} = \frac{|(ax_1 + by_1 + cz_1) - (ax_0 + by_0 + cz_0)|}{\sqrt{a^2 + b^2 + c^2}} .
> $$
>
> Since $P_0$ lies in the plane, $ax_0 + by_0 + cz_0 + d = 0$, so $-(ax_0 + by_0 + cz_0) = d$, which gives the formula.

^pf-84-8

*Uses:* [[§82 The Dot Product#^thm-82-6|§82.6]], [[§84 Equations of Lines and Planes#^prop-84-7|§84.7]]

![[m233-84-1.svg]]
*The distance from $P_1$ to the plane is the length of the shadow of $\mathbf{b} = \overrightarrow{P_0P_1}$ on the normal direction $\mathbf{n}$, where $P_0$ is any point of the plane. Moving $P_0$ within the plane changes $\mathbf{b}$ only by a vector perpendicular to $\mathbf{n}$, which leaves $\operatorname{comp}_{\mathbf{n}}\mathbf{b}$ unchanged.*

> [!remark] Remark: Method — Distances Between Planes and Between Lines
> 1. **Parallel planes:** choose any point on one plane (set two variables to $0$) and use [[§84 Equations of Lines and Planes#^thm-84-8|Theorem §84.8]] for its distance to the other.
> 2. **A line parallel to a plane** (direction vector orthogonal to the normal, and a point of the line not on the plane): the distance from any point of the line to the plane.
> 3. **Skew lines:** they lie in parallel planes with common normal $\mathbf{n} = \mathbf{v}_1 \times \mathbf{v}_2$. Write the plane through a point of $L_2$ with normal $\mathbf{n}$, and take the distance from a point of $L_1$ to it. Equivalently, $D = |\overrightarrow{P_1P_2} \cdot \mathbf{n}|/|\mathbf{n}|$ for any $P_1$ on $L_1$ and $P_2$ on $L_2$.

^rem-84-4

> [!example] Example §84.5: Distances
> **(a)** Find the distance between the parallel planes $10x + 2y - 2z = 5$ and $5x + y - z = 1$.
>
> The normals $\langle 10, 2, -2 \rangle$ and $\langle 5, 1, -1 \rangle$ are parallel. Putting $y = z = 0$ in the first equation gives $10x = 5$, so $\big(\frac12, 0, 0\big)$ is on the first plane. Its distance to $5x + y - z - 1 = 0$ is
>
> $$
> D = \frac{|5(\frac12) + 1(0) - 1(0) - 1|}{\sqrt{5^2 + 1^2 + (-1)^2}} = \frac{\frac32}{3\sqrt3} = \frac{\sqrt3}{6} .
> $$
>
> **(b)** Find the distance between the skew lines $L_1$: $x = 1 + t$, $y = -2 + 3t$, $z = 4 - t$ and $L_2$: $x = 2s$, $y = 3 + s$, $z = -3 + 4s$ of [[§84 Equations of Lines and Planes#^ex-84-2|Example §84.2]](a).
>
> A common normal is $\mathbf{n} = \mathbf{v}_1 \times \mathbf{v}_2 = \langle 1, 3, -1 \rangle \times \langle 2, 1, 4 \rangle = \langle 12 + 1,\ -2 - 4,\ 1 - 6 \rangle = 13\mathbf{i} - 6\mathbf{j} - 5\mathbf{k}$. With $s = 0$, $(0, 3, -3)$ is on $L_2$, so the plane $P_2$ containing $L_2$ is $13(x - 0) - 6(y - 3) - 5(z + 3) = 0$, or $13x - 6y - 5z + 3 = 0$. With $t = 0$, $(1, -2, 4)$ is on $L_1$, and
>
> $$
> D = \frac{|13(1) - 6(-2) - 5(4) + 3|}{\sqrt{13^2 + (-6)^2 + (-5)^2}} = \frac{8}{\sqrt{230}} \approx 0.53 .
> $$
>
> **(c)** Find the distance $D$ from $(1, 6, -1)$ to the plane $2x + y - 2z = 19$, and the point $Q$ of the plane closest to $(1, 6, -1)$.
>
> $D = \dfrac{|2 + 6 + 2 - 19|}{\sqrt{4 + 1 + 4}} = \dfrac{9}{3} = 3$. The closest point lies on the line through $(1, 6, -1)$ along the normal: $x = 1 + 2t$, $y = 6 + t$, $z = -1 - 2t$. Substituting, $2(1 + 2t) + (6 + t) - 2(-1 - 2t) = 10 + 9t = 19$, so $t = 1$ and $Q = (3, 7, -3)$. Consistently, $|t|\,|\mathbf{n}| = 1 \cdot 3 = D$.
>
> **(d)** Let $P$ be the plane through $(1, 0, 0)$, $(0, 2, 0)$, $(0, 0, 3)$, that is, $6x + 3y + 2z = 6$ ([[§84 Equations of Lines and Planes#^ex-84-3|Example §84.3]](b)), and $L$ the line $x = 2t$, $y = -2t$, $z = -3t$ through the origin. Does $L$ meet $P$? Here $\mathbf{n} \cdot \mathbf{v} = \langle 6, 3, 2 \rangle \cdot \langle 2, -2, -3 \rangle = 12 - 6 - 6 = 0$, so $L$ is parallel to $P$ or lies in it; the origin is on $L$ but not on $P$, so $L$ is parallel to $P$ and never meets it. The distance is that of the origin from $P$: $D = |0 - 6|/\sqrt{36 + 9 + 4} = \frac67$.
>
> *Stewart: Examples 12.5.8 and 12.5.9*
> *Source: 233 SI Midterm 1 Problem Set, Q2(b)–(c); 233 Practice Exam 1, Q2(b)–(c)*

^ex-84-5
