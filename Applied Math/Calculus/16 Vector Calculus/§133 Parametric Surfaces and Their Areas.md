---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 133
stewart: "16.6"
aliases: ["Stewart 16.6"]
tags: [calculus, math233]
---
← [[§132 Curl and Divergence]] · ↑ [[· 16 Vector Calculus]] · [[§134 Surface Integrals]] →

*Stewart, Section 16.6 · MATH 233 (UMass, Spring 2023).*

A space curve is traced by a vector function $\mathbf{r}(t)$ of one parameter; a surface is traced by a vector function $\mathbf{r}(u, v)$ of two. Parametric surfaces include everything met so far (graphs $z = f(x, y)$, cylinders, spheres, cones, surfaces of revolution) and much more. The partial derivatives $\mathbf{r}_u$ and $\mathbf{r}_v$ are tangent vectors; their cross product is a normal vector, which gives the tangent plane, and its length is the area-magnification factor, which gives the surface area $\iint_D |\mathbf{r}_u \times \mathbf{r}_v|\,dA$. Both ingredients are reused in the next section to integrate over surfaces. (MATH 233 marked this section "time permitting".)

## Parametric Surfaces

> [!definition] Definition §133.1: Parametric Surface
> Let
>
> $$
> \mathbf{r}(u, v) = x(u, v)\,\mathbf{i} + y(u, v)\,\mathbf{j} + z(u, v)\,\mathbf{k} \qquad (1)
> $$
>
> be a vector-valued function defined on a region $D$ in the $uv$-plane. The set of all points $(x, y, z)$ in $\mathbb{R}^3$ such that
>
> $$
> x = x(u, v), \qquad y = y(u, v), \qquad z = z(u, v) \qquad (2)
> $$
>
> and $(u, v)$ varies throughout $D$ is called a **parametric surface** $S$, and Equations 2 are called **parametric equations** of $S$. The surface is traced out by the tip of the position vector $\mathbf{r}(u, v)$ as $(u, v)$ moves throughout $D$.
>
> *Stewart: 16.6, Equations 1 and 2*

^def-133-1

> [!remark]- Connections
> - Parametrized surfaces in 452: [[§31 Surface Integrals#^def-31-1|452 Def. §31.1]], with the tangent vectors [[§31 Surface Integrals#^def-31-2|452 Def. §31.2]] and the regularity condition $\mathbf{X}_u \times \mathbf{X}_v \ne \mathbf{0}$, [[§31 Surface Integrals#^def-31-3|452 Def. §31.3]] (Stewart's "smooth", [[§133 Parametric Surfaces and Their Areas#^def-133-4|Definition §133.4]] below).

For example, $\mathbf{r}(u, v) = 2\cos u\,\mathbf{i} + v\,\mathbf{j} + 2\sin u\,\mathbf{k}$ satisfies $x^2 + z^2 = 4\cos^2 u + 4\sin^2 u = 4$, with $y = v$ unrestricted: it is the circular cylinder of radius $2$ about the $y$-axis. Restricting the parameters to $0 \le u \le \pi/2$, $0 \le v \le 3$ gives only the quarter of it of length $3$ with $x \ge 0$, $z \ge 0$ (Stewart, Example 16.6.1).

> [!definition] Definition §133.2: Grid Curves
> If $S$ is given by $\mathbf{r}(u, v)$, keeping $u$ constant, $u = u_0$, makes $\mathbf{r}(u_0, v)$ a vector function of the single parameter $v$, which defines a curve $C_1$ on $S$. Similarly, keeping $v = v_0$ gives a curve $C_2$ given by $\mathbf{r}(u, v_0)$. These two families of curves, the images of the vertical and horizontal lines of the $uv$-plane, are called **grid curves**.
>
> *Stewart: 16.6 (text)*

^def-133-2

For the cylinder above, the grid curves with $u$ constant are horizontal lines and those with $v$ constant are circles. For the spiral tube $\mathbf{r}(u, v) = \langle (2 + \sin v)\cos u,\ (2 + \sin v)\sin u,\ u + \cos v \rangle$, the curves with $v$ constant are helices, and those with $u$ constant are circles, along which $z = u_0 + \cos v$ varies from $u_0 - 1$ to $u_0 + 1$ (Stewart, Example 16.6.2). Grid curves are like lines of latitude and longitude: giving $(u, v)$ locates a point on the surface the way latitude and longitude locate a point on the earth.

> [!example] Example §133.1: A Plane
> Find a vector function that represents the plane that passes through the point $P_0$ with position vector $\mathbf{r}_0$ and contains two nonparallel vectors $\mathbf{a}$ and $\mathbf{b}$.
>
> If $P$ is any point in the plane, we can get from $P_0$ to $P$ by moving a certain distance in the direction of $\mathbf{a}$ and another distance in the direction of $\mathbf{b}$ ([[§94 Vectors#^thm-94-1|Parallelogram Law]]): there are scalars $u$ and $v$ with $\overrightarrow{P_0P} = u\,\mathbf{a} + v\,\mathbf{b}$. If $\mathbf{r}$ is the position vector of $P$, then $\mathbf{r} = \overrightarrow{OP_0} + \overrightarrow{P_0P}$, so the vector equation of the plane is
>
> $$
> \mathbf{r}(u, v) = \mathbf{r}_0 + u\,\mathbf{a} + v\,\mathbf{b}, \qquad u, v \in \mathbb{R} .
> $$
>
> With $\mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle$, $\mathbf{a} = \langle a_1, a_2, a_3 \rangle$, $\mathbf{b} = \langle b_1, b_2, b_3 \rangle$, the parametric equations are
>
> $$
> x = x_0 + ua_1 + vb_1, \qquad y = y_0 + ua_2 + vb_2, \qquad z = z_0 + ua_3 + vb_3 .
> $$
>
> Restricting $(u, v)$ to $[0, 1] \times [0, 1]$ gives the parallelogram spanned by $\mathbf{a}$ and $\mathbf{b}$ at $P_0$; such a parallelogram reappears in [[§134 Surface Integrals#^ex-134-1|Example §134.1]].
>
> *Stewart: Example 16.6.3*

^ex-133-1

> [!theorem] Proposition §133.1: Graphs and Surfaces of Revolution as Parametric Surfaces
> **(a) Graphs.** A surface with equation $z = f(x, y)$, $(x, y) \in D$, is a parametric surface with $x$ and $y$ as parameters:
>
> $$
> x = x, \qquad y = y, \qquad z = f(x, y) .
> $$
>
> **(b) Surfaces of revolution.** The surface $S$ obtained by rotating the curve $y = f(x)$, $a \le x \le b$, about the $x$-axis, where $f(x) \ge 0$, has parametric equations
>
> $$
> x = x, \qquad y = f(x)\cos\theta, \qquad z = f(x)\sin\theta \qquad (3)
> $$
>
> with parameter domain $a \le x \le b$, $0 \le \theta \le 2\pi$, where $\theta$ is the angle of rotation.
>
> *Stewart: 16.6 (text) and Equations 3*

^prop-133-1

> [!proof]+ Proof
> (a) As $(x, y)$ ranges over $D$, the point $(x, y, f(x, y))$ ranges over the graph.
>
> (b) Rotating the point $(x, f(x), 0)$ of the curve about the $x$-axis keeps its $x$-coordinate and moves it on the circle in the plane perpendicular to the $x$-axis with center $(x, 0, 0)$ and radius $f(x)$ (its distance from the axis). The point of this circle at angle $\theta$ from the $xy$-plane is $(x, f(x)\cos\theta, f(x)\sin\theta)$. Every point of $S$ arises this way for some $x \in [a, b]$ and $\theta \in [0, 2\pi]$.

^pf-133-1

*Uses:* [[§133 Parametric Surfaces and Their Areas#^def-133-1|Def. §133.1]]

For instance, rotating $y = \sin x$, $0 \le x \le 2\pi$, about the $x$-axis gives $x = x$, $y = \sin x\cos\theta$, $z = \sin x\sin\theta$ (Stewart, Example 16.6.8), and the elliptic paraboloid $z = x^2 + 2y^2$ is $\mathbf{r}(x, y) = x\,\mathbf{i} + y\,\mathbf{j} + (x^2 + 2y^2)\,\mathbf{k}$ (Stewart, Example 16.6.6). Surfaces that are simple in cylindrical or spherical coordinates are parametrized by the coordinates that describe them: the cylinder $x^2 + y^2 = 4$, $0 \le z \le 1$, which is $r = 2$ in cylindrical coordinates, is $\mathbf{r}(\theta, z) = 2\cos\theta\,\mathbf{i} + 2\sin\theta\,\mathbf{j} + z\,\mathbf{k}$, $0 \le \theta \le 2\pi$, $0 \le z \le 1$ (Stewart, Example 16.6.5); the sphere is in [[§133 Parametric Surfaces and Their Areas#^ex-133-4|Example §133.4]].

> [!example] Example §133.2: Two Parametrizations of a Cone
> Find a parametric representation for the surface $z = 2\sqrt{x^2 + y^2}$, the top half of the cone $z^2 = 4x^2 + 4y^2$.
>
> **Solution 1: as a graph.** With $x$ and $y$ as parameters, $x = x$, $y = y$, $z = 2\sqrt{x^2 + y^2}$, so
>
> $$
> \mathbf{r}(x, y) = x\,\mathbf{i} + y\,\mathbf{j} + 2\sqrt{x^2 + y^2}\,\mathbf{k} .
> $$
>
> **Solution 2: with polar coordinates.** A point on the cone has $x = r\cos\theta$, $y = r\sin\theta$ and $z = 2\sqrt{x^2 + y^2} = 2r$. So
>
> $$
> \mathbf{r}(r, \theta) = r\cos\theta\,\mathbf{i} + r\sin\theta\,\mathbf{j} + 2r\,\mathbf{k}, \qquad r \ge 0,\ 0 \le \theta \le 2\pi .
> $$
>
> Parametrizations are not unique. The second one can be preferable: the part of the cone below the plane $z = 1$ is obtained just by changing the parameter domain to the rectangle $D = \{(r, \theta) \mid 0 \le r \le \frac12,\ 0 \le \theta \le 2\pi\}$. (Its grid curves are the horizontal circles $r = k$ and the rulings $\theta = c$.)
>
> *Stewart: Example 16.6.7*

^ex-133-2

## Tangent Planes

Let $S$ be traced out by $\mathbf{r}(u, v) = x(u, v)\,\mathbf{i} + y(u, v)\,\mathbf{j} + z(u, v)\,\mathbf{k}$, and let $P_0$ be the point with position vector $\mathbf{r}(u_0, v_0)$. The grid curve $C_1$ given by $\mathbf{r}(u_0, v)$ passes through $P_0$, and so does the grid curve $C_2$ given by $\mathbf{r}(u, v_0)$.

> [!definition] Definition §133.3: Tangent Vectors to a Parametric Surface
> The tangent vectors at $P_0$ to the grid curves $C_1$ and $C_2$ are the partial derivatives
>
> $$
> \mathbf{r}_v = \frac{\partial x}{\partial v}(u_0, v_0)\,\mathbf{i} + \frac{\partial y}{\partial v}(u_0, v_0)\,\mathbf{j} + \frac{\partial z}{\partial v}(u_0, v_0)\,\mathbf{k}, \qquad (4)
> $$
>
> $$
> \mathbf{r}_u = \frac{\partial x}{\partial u}(u_0, v_0)\,\mathbf{i} + \frac{\partial y}{\partial u}(u_0, v_0)\,\mathbf{j} + \frac{\partial z}{\partial u}(u_0, v_0)\,\mathbf{k} . \qquad (5)
> $$
>
> *Stewart: 16.6, Equations 4 and 5*

^def-133-3

> [!definition] Definition §133.4: Smooth Surface
> If $\mathbf{r}_u \times \mathbf{r}_v$ is never $\mathbf{0}$, the surface $S$ is called **smooth** (it has no "corners").
>
> *Stewart: 16.6, Equations 4 and 5*

^def-133-4

> [!definition] Definition §133.5: Tangent Plane to a Parametric Surface
> For a smooth surface, the **tangent plane** at $P_0$ is the plane that contains the tangent vectors $\mathbf{r}_u$ and $\mathbf{r}_v$, and the vector $\mathbf{r}_u \times \mathbf{r}_v$ is a normal vector to the tangent plane.
>
> *Stewart: 16.6, Equations 4 and 5*

^def-133-5

> [!example] Example §133.3: A Tangent Plane
> Find the tangent plane to the surface with parametric equations $x = u^2$, $y = v^2$, $z = u + 2v$ at the point $(1, 1, 3)$.
>
> The tangent vectors are
>
> $$
> \mathbf{r}_u = \frac{\partial x}{\partial u}\,\mathbf{i} + \frac{\partial y}{\partial u}\,\mathbf{j} + \frac{\partial z}{\partial u}\,\mathbf{k} = 2u\,\mathbf{i} + \mathbf{k}, \qquad \mathbf{r}_v = 2v\,\mathbf{j} + 2\,\mathbf{k} ,
> $$
>
> so a normal vector to the tangent plane is
>
> $$
> \mathbf{r}_u \times \mathbf{r}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2u & 0 & 1 \\ 0 & 2v & 2 \end{vmatrix} = -2v\,\mathbf{i} - 4u\,\mathbf{j} + 4uv\,\mathbf{k} .
> $$
>
> The point $(1, 1, 3)$ corresponds to $u = 1$, $v = 1$ (from $x = u^2 = 1$, $y = v^2 = 1$ and $z = u + 2v = 3$), where the normal vector is $-2\,\mathbf{i} - 4\,\mathbf{j} + 4\,\mathbf{k}$. So the tangent plane is
>
> $$
> -2(x - 1) - 4(y - 1) + 4(z - 3) = 0, \qquad\text{that is,}\qquad x + 2y - 2z + 3 = 0 .
> $$
>
> *Stewart: Example 16.6.9*

^ex-133-3

## Surface Area

> [!remark] Remark: Why the Surface Area Formula
> Suppose first that the parameter domain $D$ is a rectangle, divided into subrectangles $R_{ij}$ of size $\Delta u \times \Delta v$, with lower left corners $(u_i^{\ast}, v_j^{\ast})$. The part $S_{ij}$ of $S$ corresponding to $R_{ij}$ is a **patch** with corner $P_{ij}$, position vector $\mathbf{r}(u_i^{\ast}, v_j^{\ast})$. Let $\mathbf{r}_u^{\ast} = \mathbf{r}_u(u_i^{\ast}, v_j^{\ast})$ and $\mathbf{r}_v^{\ast} = \mathbf{r}_v(u_i^{\ast}, v_j^{\ast})$. The two edges of the patch at $P_{ij}$ are approximately the vectors $\Delta u\,\mathbf{r}_u^{\ast}$ and $\Delta v\,\mathbf{r}_v^{\ast}$, because partial derivatives are approximated by difference quotients. So $S_{ij}$ is approximated by the parallelogram they span, which lies in the tangent plane at $P_{ij}$ and has area
>
> $$
> |(\Delta u\,\mathbf{r}_u^*) \times (\Delta v\,\mathbf{r}_v^*)| = |\mathbf{r}_u^* \times \mathbf{r}_v^*|\,\Delta u\,\Delta v
> $$
>
> ([[§96 The Cross Product#^cor-96-6|Corollary §96.6]]). An approximation to the area of $S$ is $\sum_{i=1}^{m} \sum_{j=1}^{n} |\mathbf{r}_u^* \times \mathbf{r}_v^*|\,\Delta u\,\Delta v$, which gets better as the subrectangles shrink, and which is a Riemann sum for $\iint_D |\mathbf{r}_u \times \mathbf{r}_v|\,du\,dv$.

^rem-133-1

![[m233-112-1.svg]]
*Approximating a patch by a parallelogram. The subrectangle $R_{ij}$ (left) is mapped by $\mathbf{r}$ onto the curved patch $S_{ij}$ (blue). Its edges at $P_{ij}$ are nearly the vectors $\Delta u\,\mathbf{r}_u^{\ast}$ and $\Delta v\,\mathbf{r}_v^{\ast}$ (red), and the parallelogram they span (red, in the tangent plane) has area $|\mathbf{r}_u^{\ast} \times \mathbf{r}_v^{\ast}|\,\Delta u\,\Delta v$. So $|\mathbf{r}_u \times \mathbf{r}_v|$ is the factor by which $\mathbf{r}$ stretches small areas.*

> [!definition] Definition §133.6: Surface Area
> If a smooth parametric surface $S$ is given by the equation
>
> $$
> \mathbf{r}(u, v) = x(u, v)\,\mathbf{i} + y(u, v)\,\mathbf{j} + z(u, v)\,\mathbf{k}, \qquad (u, v) \in D ,
> $$
>
> and $S$ is covered just once as $(u, v)$ ranges throughout the parameter domain $D$, then the **surface area** of $S$ is
>
> $$
> A(S) = \iint_D |\mathbf{r}_u \times \mathbf{r}_v|\,dA, \qquad\text{where}\quad \mathbf{r}_u = \frac{\partial x}{\partial u}\,\mathbf{i} + \frac{\partial y}{\partial u}\,\mathbf{j} + \frac{\partial z}{\partial u}\,\mathbf{k}, \quad \mathbf{r}_v = \frac{\partial x}{\partial v}\,\mathbf{i} + \frac{\partial y}{\partial v}\,\mathbf{j} + \frac{\partial z}{\partial v}\,\mathbf{k} .
> $$
>
> *Stewart: 16.6, Definition 6*

^def-133-6

> [!remark]- Connections
> - In 452 the area element is derived from the Gram matrix, $dS = \sqrt{\det G}\,du\,dv = |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$: [[§31 Surface Integrals#^thm-31-1|452 Thm. §31.1]], and the area is the case $f = 1$ of [[§31 Surface Integrals#^def-31-5|452 Def. §31.5]]. The factor $|\mathbf{r}_u \times \mathbf{r}_v|$ plays the role that the Jacobian plays for a change of variables in the plane ([[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]]).

> [!example] Example §133.4: The Sphere
> (a) Find a parametric representation of the sphere $x^2 + y^2 + z^2 = a^2$. (b) Find its surface area.
>
> **(a)** The sphere is $\rho = a$ in spherical coordinates ([[§123 Triple Integrals in Spherical Coordinates#^def-123-1|Definition §123.1]]), so take the angles $\phi$ and $\theta$ as parameters:
>
> $$
> \mathbf{r}(\phi, \theta) = a\sin\phi\cos\theta\,\mathbf{i} + a\sin\phi\sin\theta\,\mathbf{j} + a\cos\phi\,\mathbf{k}, \qquad D = [0, \pi] \times [0, 2\pi] .
> $$
>
> The grid curves with $\phi$ constant are the circles of constant latitude (including the equator, $\phi = \pi/2$); those with $\theta$ constant are the meridians, semicircles from the north pole to the south pole.
>
> **(b)** The tangent vectors are $\mathbf{r}_\phi = \langle a\cos\phi\cos\theta,\ a\cos\phi\sin\theta,\ -a\sin\phi \rangle$ and $\mathbf{r}_\theta = \langle -a\sin\phi\sin\theta,\ a\sin\phi\cos\theta,\ 0 \rangle$, and
>
> $$
> \mathbf{r}_\phi \times \mathbf{r}_\theta = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a\cos\phi\cos\theta & a\cos\phi\sin\theta & -a\sin\phi \\ -a\sin\phi\sin\theta & a\sin\phi\cos\theta & 0 \end{vmatrix} = a^2\sin^2\phi\cos\theta\,\mathbf{i} + a^2\sin^2\phi\sin\theta\,\mathbf{j} + a^2\sin\phi\cos\phi\,\mathbf{k} .
> $$
>
> So
>
> $$
> |\mathbf{r}_\phi \times \mathbf{r}_\theta| = \sqrt{a^4\sin^4\phi\cos^2\theta + a^4\sin^4\phi\sin^2\theta + a^4\sin^2\phi\cos^2\phi} = \sqrt{a^4\sin^4\phi + a^4\sin^2\phi\cos^2\phi} = a^2\sqrt{\sin^2\phi} = a^2\sin\phi ,
> $$
>
> since $\sin\phi \ge 0$ for $0 \le \phi \le \pi$. By [[§133 Parametric Surfaces and Their Areas#^def-133-6|Definition §133.6]],
>
> $$
> A = \iint_D a^2\sin\phi\,dA = \int_0^{2\pi} \int_0^{\pi} a^2\sin\phi\,d\phi\,d\theta = a^2 \int_0^{2\pi} d\theta \int_0^{\pi} \sin\phi\,d\phi = a^2 (2\pi)(2) = 4\pi a^2 .
> $$
>
> (The factor $a^2\sin\phi$ is the spherical-coordinates volume factor $\rho^2\sin\phi$ of [[§123 Triple Integrals in Spherical Coordinates#^thm-123-2|Theorem §123.2]] at $\rho = a$.)
>
> *Stewart: Examples 16.6.4 and 16.6.10*

^ex-133-4

> [!theorem] Theorem §133.2: Surface Area of a Graph
> For a surface $S$ with equation $z = f(x, y)$, $(x, y) \in D$, where $f$ has continuous partial derivatives,
>
> $$
> \mathbf{r}_x \times \mathbf{r}_y = -\frac{\partial f}{\partial x}\,\mathbf{i} - \frac{\partial f}{\partial y}\,\mathbf{j} + \mathbf{k}, \qquad (7)
> \qquad
> |\mathbf{r}_x \times \mathbf{r}_y| = \sqrt{\left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2 + 1} , \qquad (8)
> $$
>
> and the surface area is
>
> $$
> A(S) = \iint_D \sqrt{1 + \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2}\,dA . \qquad (9)
> $$
>
> *Stewart: 16.6, Equations 7, 8 and 9*

^thm-133-2

> [!proof]+ Proof
> Use the parametrization $x = x$, $y = y$, $z = f(x, y)$ of [[§133 Parametric Surfaces and Their Areas#^prop-133-1|Proposition §133.1]]. Then
>
> $$
> \mathbf{r}_x = \mathbf{i} + \frac{\partial f}{\partial x}\,\mathbf{k}, \qquad \mathbf{r}_y = \mathbf{j} + \frac{\partial f}{\partial y}\,\mathbf{k}, \qquad
> \mathbf{r}_x \times \mathbf{r}_y = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & \partial f/\partial x \\ 0 & 1 & \partial f/\partial y \end{vmatrix} = -\frac{\partial f}{\partial x}\,\mathbf{i} - \frac{\partial f}{\partial y}\,\mathbf{j} + \mathbf{k} ,
> $$
>
> which is (7); its length is (8). This parametrization covers $S$ exactly once, and $\mathbf{r}_x \times \mathbf{r}_y$ is never $\mathbf{0}$ (its $\mathbf{k}$-component is $1$), so $S$ is smooth and [[§133 Parametric Surfaces and Their Areas#^def-133-6|Definition §133.6]] gives (9).

^pf-133-2

*Uses:* [[§133 Parametric Surfaces and Their Areas#^prop-133-1|§133.1]], [[§133 Parametric Surfaces and Their Areas#^def-133-6|Def. §133.6]], [[§133 Parametric Surfaces and Their Areas#^def-133-3|Def. §133.3]], [[§133 Parametric Surfaces and Their Areas#^def-133-4|Def. §133.4]]

Formula 9 is the surface area formula of [[§119 Surface Area#^thm-119-1|Theorem §119.1]] (Stewart 15.5, Formula 3); note its similarity to the arc length formula $L = \int_a^b \sqrt{1 + (dy/dx)^2}\,dx$ ([[§60 Arc Length#^thm-60-1|Theorem §60.1]]).

> [!example] Example §133.5: Part of a Paraboloid
> Find the area of the part of the paraboloid $z = x^2 + y^2$ that lies under the plane $z = 9$.
>
> The plane meets the paraboloid in the circle $x^2 + y^2 = 9$, $z = 9$, so the surface lies above the disk $D$ with center the origin and radius $3$. By Formula 9, with $\partial z/\partial x = 2x$ and $\partial z/\partial y = 2y$,
>
> $$
> A = \iint_D \sqrt{1 + (2x)^2 + (2y)^2}\,dA = \iint_D \sqrt{1 + 4(x^2 + y^2)}\,dA .
> $$
>
> In polar coordinates,
>
> $$
> A = \int_0^{2\pi} \int_0^3 \sqrt{1 + 4r^2}\,r\,dr\,d\theta = 2\pi \cdot \frac18 \cdot \frac23 (1 + 4r^2)^{3/2} \Big]_0^3 = \frac{\pi}{6}\big(37\sqrt{37} - 1\big) .
> $$
>
> *Stewart: Example 16.6.11*

^ex-133-5

*Chain: the same paraboloid earlier in [[§119 Surface Area#^ex-119-2|Chapter 15]].*

Is [[§133 Parametric Surfaces and Their Areas#^def-133-6|Definition §133.6]] consistent with the surface area formula for surfaces of revolution from single-variable calculus ([[§61 Area of a Surface of Revolution#^def-61-2|Definition §61.2]], Stewart 8.2.4)?

> [!theorem] Theorem §133.3: Surfaces of Revolution
> If $S$ is obtained by rotating the curve $y = f(x)$, $a \le x \le b$, about the $x$-axis, where $f(x) \ge 0$ and $f'$ is continuous, then
>
> $$
> A(S) = 2\pi \int_a^b f(x)\sqrt{1 + [f'(x)]^2}\,dx .
> $$
>
> This is the formula used to define the area of a surface of revolution in single-variable calculus, [[§61 Area of a Surface of Revolution#^def-61-2|Definition §61.2]].
>
> *Stewart: 16.6 (text)*

^thm-133-3

> [!proof]+ Proof
> Use the parametrization (3): $x = x$, $y = f(x)\cos\theta$, $z = f(x)\sin\theta$, $a \le x \le b$, $0 \le \theta \le 2\pi$. The tangent vectors are
>
> $$
> \mathbf{r}_x = \mathbf{i} + f'(x)\cos\theta\,\mathbf{j} + f'(x)\sin\theta\,\mathbf{k}, \qquad \mathbf{r}_\theta = -f(x)\sin\theta\,\mathbf{j} + f(x)\cos\theta\,\mathbf{k} ,
> $$
>
> so
>
> $$
> \mathbf{r}_x \times \mathbf{r}_\theta = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & f'(x)\cos\theta & f'(x)\sin\theta \\ 0 & -f(x)\sin\theta & f(x)\cos\theta \end{vmatrix} = f(x)f'(x)\,\mathbf{i} - f(x)\cos\theta\,\mathbf{j} - f(x)\sin\theta\,\mathbf{k}
> $$
>
> and
>
> $$
> |\mathbf{r}_x \times \mathbf{r}_\theta| = \sqrt{[f(x)]^2[f'(x)]^2 + [f(x)]^2\cos^2\theta + [f(x)]^2\sin^2\theta} = \sqrt{[f(x)]^2\big(1 + [f'(x)]^2\big)} = f(x)\sqrt{1 + [f'(x)]^2}
> $$
>
> because $f(x) \ge 0$. Therefore, by [[§133 Parametric Surfaces and Their Areas#^def-133-6|Definition §133.6]],
>
> $$
> A = \iint_D |\mathbf{r}_x \times \mathbf{r}_\theta|\,dA = \int_0^{2\pi} \int_a^b f(x)\sqrt{1 + [f'(x)]^2}\,dx\,d\theta = 2\pi \int_a^b f(x)\sqrt{1 + [f'(x)]^2}\,dx .
> $$

^pf-133-3

*Uses:* [[§133 Parametric Surfaces and Their Areas#^prop-133-1|§133.1]], [[§133 Parametric Surfaces and Their Areas#^def-133-6|Def. §133.6]]
