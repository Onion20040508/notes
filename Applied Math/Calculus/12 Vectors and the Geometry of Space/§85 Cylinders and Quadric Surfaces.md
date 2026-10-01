---
type: section
subject: "[[Calculus]]"
chapter: 12
section: 85
stewart: "12.6"
aliases: ["Stewart 12.6"]
tags: [calculus, math233]
---
← [[§84 Equations of Lines and Planes]] · ↑ [[· 12 Vectors and the Geometry of Space]] · [[§86 Vector Functions and Space Curves]] →

*Stewart, Section 12.6 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q11, Q12), Exam 1 Review (Q9).*

After planes and spheres, the next surfaces are cylinders and quadric surfaces, the graphs of second-degree equations in $x$, $y$, $z$. The tool for understanding them is the **trace**: slice the surface by planes parallel to the coordinate planes and recognize the plane curves (lines, parabolas, ellipses, hyperbolas) that appear. An equation missing a variable is a cylinder. Every quadric surface can be moved into one of six standard types (ellipsoid, cone, elliptic and hyperbolic paraboloid, hyperboloids of one and two sheets), recognized from the signs and powers in its equation. These surfaces are the standard examples of graphs and level surfaces in Chapter 14 (the hyperbolic paraboloid is the model saddle point) and the standard domains of integration in Chapter 15.

> [!definition] Definition §85.1: Traces
> The **traces** (or cross-sections) of a surface are the curves in which it intersects planes parallel to the coordinate planes, that is, planes $x = k$, $y = k$ or $z = k$.
>
> *Stewart: 12.6 (text)*

^def-85-1

## Cylinders

> [!definition] Definition §85.2: Cylinder
> A **cylinder** is a surface that consists of all lines, called **rulings**, that are parallel to a given line and pass through a given plane curve.
>
> *Stewart: 12.6 (text)*

^def-85-2

> [!theorem] Proposition §85.1: A Missing Variable Gives a Cylinder
> If one of the variables $x$, $y$ or $z$ is missing from the equation of a surface, then the surface is a cylinder whose rulings are parallel to the axis of the missing variable.
>
> *Stewart: 12.6 (text)*

^prop-85-1

> [!proof]+ Proof
> Say $y$ is missing, so the equation is $F(x, z) = 0$. Let $C$ be the curve $F(x, z) = 0$ in the $xz$-plane ($y = 0$). A point $(x, y, z)$ satisfies the equation if and only if $(x, 0, z)$ is on $C$, whatever $y$ is. So the surface is the union of the lines $\{(x_0, y, z_0) \mid y \in \mathbb{R}\}$ through the points $(x_0, 0, z_0)$ of $C$, all parallel to the $y$-axis: a cylinder by Definition §85.2. The other cases are the same with the variables renamed.

^pf-85-1

*Uses:* [[§85 Cylinders and Quadric Surfaces#^def-85-2|Def. §85.2]]

> [!remark] Remark: A Cylinder Is Not a Circle
> In $\mathbb{R}^3$, $x^2 + y^2 = 1$ is a cylinder, not a circle. The circle in the $xy$-plane is described by the *pair* of equations $x^2 + y^2 = 1$, $z = 0$ (compare [[§80 Three-Dimensional Coordinate Systems#^ex-80-2|Example §80.2]]).

^rem-85-1

> [!example] Example §85.1: Cylinders
> **(a)** Sketch $z = x^2$. The variable $y$ is missing, so every vertical plane $y = k$ meets the surface in the parabola $z = x^2$. The surface is obtained by moving the parabola $z = x^2$ of the $xz$-plane in the direction of the $y$-axis: a **parabolic cylinder**, with rulings parallel to the $y$-axis.
>
> **(b)** Identify $x^2 + y^2 = 1$ and $y^2 + z^2 = 1$. In the first, $z$ is missing and each plane $z = k$ meets the surface in the circle of radius $1$ about the $z$-axis: a circular cylinder with axis the $z$-axis and vertical rulings. In the second, $x$ is missing: the circle $y^2 + z^2 = 1$, $x = 0$, moved parallel to the $x$-axis, a circular cylinder with axis the $x$-axis.
>
> **(c)** Sketch $z = 4 - x^2$, with its trace in $y = 3$. Again $y$ is missing, so this is a parabolic cylinder with rulings parallel to the $y$-axis. Its trace in $y = 0$ is the downward parabola $z = 4 - x^2 = (2 - x)(2 + x)$ with vertex $(0, 0, 4)$ and roots $x = \pm 2$; the trace in $y = 3$ is the identical parabola $z = 4 - x^2$ lying in the plane $y = 3$.
>
> *The posted answer says the $y = 3$ trace lies "in the plane $z = 3$"; it lies in the plane $y = 3$.*
>
> **(d)** Sketch $y^2 + z^2 = 9$, with its trace in $x = 4$. Now $x$ is missing: a right circular cylinder of radius $3$ whose axis is the $x$-axis. Its trace in $x = 4$ is the circle $y^2 + z^2 = 9$ of radius $3$ in the plane $x = 4$, centered at $(4, 0, 0)$.
>
> *Stewart: Examples 12.6.1 and 12.6.2*
> *Source: 233 Midterm 1 Practice Questions, Q11, Q12*

^ex-85-1

## Quadric Surfaces

> [!definition] Definition §85.3: Quadric Surface
> A **quadric surface** is the graph of a second-degree equation in three variables $x$, $y$ and $z$. The most general such equation is
>
> $$
> Ax^2 + By^2 + Cz^2 + Dxy + Eyz + Fxz + Gx + Hy + Iz + J = 0 ,
> $$
>
> where $A, B, C, \ldots, J$ are constants. By translation and rotation it can be brought into one of the two **standard forms**
>
> $$
> Ax^2 + By^2 + Cz^2 + J = 0 \qquad\text{or}\qquad Ax^2 + By^2 + Iz = 0 .
> $$
>
> Quadric surfaces are the three-dimensional counterparts of the conic sections ([[§67 Conic Sections|§67]]).
>
> *Stewart: 12.6 (text)*

^def-85-3

*Stewart states the reduction to standard form without proof. Removing the cross terms $Dxy$, $Eyz$, $Fxz$ is a rotation of axes: diagonalizing the symmetric quadratic form by an orthonormal basis, [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-13|LADR 9.13]] (the spectral theorem). The linear terms are then removed by completing squares, as in Example §85.5.*

> [!example] Example §85.2: An Ellipsoid by Traces
> Use traces to sketch $x^2 + \dfrac{y^2}{9} + \dfrac{z^2}{4} = 1$.
>
> Putting $z = 0$, the trace in the $xy$-plane is the ellipse $x^2 + y^2/9 = 1$. In general the horizontal trace in the plane $z = k$ is
>
> $$
> x^2 + \frac{y^2}{9} = 1 - \frac{k^2}{4}, \qquad z = k ,
> $$
>
> an ellipse provided $k^2 < 4$, that is, $-2 < k < 2$. (If $|k| = 2$ the trace is a single point, and for $|k| > 2$ it is empty.) Similarly the vertical traces are ellipses:
>
> $$
> \frac{y^2}{9} + \frac{z^2}{4} = 1 - k^2,\ x = k\ \ (-1 < k < 1), \qquad x^2 + \frac{z^2}{4} = 1 - \frac{k^2}{9},\ y = k\ \ (-3 < k < 3) .
> $$
>
> All traces are ellipses, so the surface is an **ellipsoid**, with intercepts $(\pm1, 0, 0)$, $(0, \pm3, 0)$, $(0, 0, \pm2)$. It is symmetric with respect to each coordinate plane, because only even powers of $x$, $y$, $z$ occur.
>
> *Stewart: Example 12.6.3*

^ex-85-2

> [!example] Example §85.3: Elliptic and Hyperbolic Paraboloids
> **(a)** $z = 4x^2 + y^2$. The trace in $x = 0$ is the parabola $z = y^2$; in $x = k$ it is $z = y^2 + 4k^2$, a parabola opening upward. In $y = k$ the trace is $z = 4x^2 + k^2$, again an upward parabola. The horizontal traces $4x^2 + y^2 = k$ are ellipses for $k > 0$ (the point $(0, 0, 0)$ for $k = 0$, empty for $k < 0$). Because of the elliptic and parabolic traces, the surface is an **elliptic paraboloid**.
>
> **(b)** $z = y^2 - x^2$. The traces in the vertical planes $x = k$ are the parabolas $z = y^2 - k^2$, which open upward; the traces in $y = k$ are the parabolas $z = -x^2 + k^2$, which open downward; the horizontal traces $y^2 - x^2 = k$ are hyperbolas (opening along the $y$-axis for $k > 0$, along the $x$-axis for $k < 0$, and the pair of lines $y = \pm x$ for $k = 0$). Fitting the traces together gives a saddle-shaped surface, the **hyperbolic paraboloid**. Along the $y$-axis the origin is a minimum of the upward parabola, along the $x$-axis a maximum of the downward one; this is the saddle point of [[§96 Maximum and Minimum Values#^def-96-2|Definition §96.2]].
>
> *Stewart: Examples 12.6.4 and 12.6.5*

^ex-85-3

![[m233-85-1.svg]]
*(a) The hyperbolic paraboloid $z = y^2 - x^2$ of Example §85.3(b): its trace in $x = 0$ is the upward parabola $z = y^2$ (red), its trace in $y = 0$ the downward parabola $z = -x^2$ (green), and the two meet at the saddle point at the origin. (b) The parabolic cylinder $z = 4 - x^2$ of Example §85.1(c): every trace $y = k$ is the same parabola, here $y = 0$ (dashed) and $y = 3$ (red), and the rulings run parallel to the $y$-axis.*

> [!example] Example §85.4: Hyperboloids of One and Two Sheets
> **(a)** Sketch $\dfrac{x^2}{4} + y^2 - \dfrac{z^2}{4} = 1$. The trace in a horizontal plane $z = k$ is the ellipse $\dfrac{x^2}{4} + y^2 = 1 + \dfrac{k^2}{4}$, which exists for every $k$ and grows with $|k|$. The traces in the $xz$- and $yz$-planes are the hyperbolas
>
> $$
> \frac{x^2}{4} - \frac{z^2}{4} = 1,\ y = 0 \qquad\text{and}\qquad y^2 - \frac{z^2}{4} = 1,\ x = 0 .
> $$
>
> This surface, connected and shaped like a cooling tower, is a **hyperboloid of one sheet**; its narrowest ellipse is $\frac{x^2}{4} + y^2 = 1$ in the $xy$-plane.
>
> **(b)** Identify and sketch $4x^2 - y^2 + 2z^2 + 4 = 0$. Dividing by $-4$ puts it in standard form:
>
> $$
> -x^2 + \frac{y^2}{4} - \frac{z^2}{2} = 1 .
> $$
>
> Compared with the table below, this is a **hyperboloid of two sheets** whose axis is the $y$-axis (the variable with the positive coefficient). The traces in the $xy$- and $yz$-planes are the hyperbolas $-x^2 + \frac{y^2}{4} = 1$, $z = 0$ and $\frac{y^2}{4} - \frac{z^2}{2} = 1$, $x = 0$. There is no trace in the $xz$-plane ($y = 0$ would require $-x^2 - z^2/2 = 1$), and the traces in the planes $y = k$ for $|k| > 2$ are the ellipses
>
> $$
> x^2 + \frac{z^2}{2} = \frac{k^2}{4} - 1, \qquad\text{that is,}\qquad \frac{x^2}{\frac{k^2}{4} - 1} + \frac{z^2}{2\big(\frac{k^2}{4} - 1\big)} = 1, \qquad y = k .
> $$
>
> The two sheets start at the vertices $(0, \pm2, 0)$ and open along the $y$-axis. Similarly, $-4x^2 + y^2 - 4z^2 = 4$, that is, $-x^2 + \frac{y^2}{4} - z^2 = 1$, is a hyperboloid of two sheets about the $y$-axis with vertices $(0, \pm 2, 0)$ and circular traces $x^2 + z^2 = \frac{k^2}{4} - 1$ in the planes $y = k$, $|k| > 2$.
>
> *Stewart: Examples 12.6.6 and 12.6.7*
> *Source: 233 Exam 1 Review, Q9(b)*

^ex-85-4

> [!theorem] Theorem §85.2: Graphs of Quadric Surfaces
> The six basic quadric surfaces in standard form (each symmetric about the $z$-axis) are:
>
> | Surface | Equation | Traces |
> |---|---|---|
> | Ellipsoid | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} = 1$ | All traces are ellipses. If $a = b = c$, it is a sphere. |
> | Cone | $\dfrac{z^2}{c^2} = \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2}$ | Horizontal traces are ellipses. Vertical traces in $x = k$ and $y = k$ are hyperbolas if $k \ne 0$, pairs of lines if $k = 0$. |
> | Elliptic paraboloid | $\dfrac{z}{c} = \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2}$ | Horizontal traces are ellipses; vertical traces are parabolas. The variable raised to the first power indicates the axis. |
> | Hyperboloid of one sheet | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$ | Horizontal traces are ellipses; vertical traces are hyperbolas. The axis is the variable with the negative coefficient. |
> | Hyperbolic paraboloid | $\dfrac{z}{c} = \dfrac{x^2}{a^2} - \dfrac{y^2}{b^2}$ | Horizontal traces are hyperbolas; vertical traces are parabolas. |
> | Hyperboloid of two sheets | $-\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} = 1$ | Horizontal traces in $z = k$ are ellipses if $k > c$ or $k < -c$; vertical traces are hyperbolas. The two minus signs indicate two sheets. |
>
> A quadric surface symmetric about a different axis has the variables exchanged accordingly.
>
> *Stewart: 12.6, Table 1*

^thm-85-2

> [!proof]- Proof
> Each statement is read off by fixing one variable (Definition §85.1) and recognizing the resulting conic ([[§67 Conic Sections|§67]]). Write $k$ for the fixed value.
> - **Ellipsoid.** $z = k$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 - \frac{k^2}{c^2}$, an ellipse for $|k| < c$ (a point for $|k| = c$, empty beyond); $x = k$ and $y = k$ are the same with the letters exchanged. If $a = b = c$ the equation is $x^2 + y^2 + z^2 = a^2$, a sphere ([[§80 Three-Dimensional Coordinate Systems#^thm-80-2|Theorem §80.2]]).
> - **Cone.** $z = k$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{k^2}{c^2}$, an ellipse for $k \ne 0$ (the origin for $k = 0$). $x = k$: $\frac{z^2}{c^2} - \frac{y^2}{b^2} = \frac{k^2}{a^2}$, a hyperbola if $k \ne 0$, and for $k = 0$ it factors as $\big(\frac zc - \frac yb\big)\big(\frac zc + \frac yb\big) = 0$, the two lines $z = \pm\frac cb\,y$. Likewise for $y = k$.
> - **Elliptic paraboloid.** $z = k$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{k}{c}$, an ellipse when $k/c > 0$. $x = k$: $z = \frac{c}{b^2}y^2 + \frac{ck^2}{a^2}$, a parabola, and likewise for $y = k$.
> - **Hyperboloid of one sheet.** $z = k$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 + \frac{k^2}{c^2} > 0$, always an ellipse. $x = k$: $\frac{y^2}{b^2} - \frac{z^2}{c^2} = 1 - \frac{k^2}{a^2}$, a hyperbola when $|k| \ne a$ (and a pair of lines when $|k| = a$, by the same factoring as for the cone).
> - **Hyperbolic paraboloid.** $z = k$: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = \frac kc$, a hyperbola for $k \ne 0$ (two lines for $k = 0$). $x = k$: $z = -\frac{c}{b^2}y^2 + \frac{ck^2}{a^2}$ and $y = k$: $z = \frac{c}{a^2}x^2 - \frac{ck^2}{b^2}$, parabolas opening in opposite directions.
> - **Hyperboloid of two sheets.** $z = k$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{k^2}{c^2} - 1$, an ellipse exactly when $|k| > c$ and empty when $|k| < c$, so the surface has no points with $-c < z < c$ and falls into two pieces. $x = k$: $\frac{z^2}{c^2} - \frac{y^2}{b^2} = 1 + \frac{k^2}{a^2}$, a hyperbola.
>
> In each case the surface has a vertical axis of symmetry, and replacing $z$ by $x$ or $y$ (exchanging variables) rotates the picture to the corresponding axis.

^pf-85-2

*Uses:* [[§85 Cylinders and Quadric Surfaces#^def-85-1|Def. §85.1]], [[§80 Three-Dimensional Coordinate Systems#^thm-80-2|§80.2]], conic sections ([[§67 Conic Sections|§67]])

> [!remark] Remark: Method — Identifying a Quadric Surface
> 1. **Collect the squares.** If a variable appears both squared and to the first power, complete the square in it (this translates the surface).
> 2. **Count powers.** A variable missing altogether: a cylinder ([[§85 Cylinders and Quadric Surfaces#^prop-85-1|Proposition §85.1]]). One variable to the first power: a paraboloid (elliptic if the two squares have the same sign on the same side, hyperbolic if opposite signs); its axis is the line of that variable. All three squared: an ellipsoid, a cone or a hyperboloid.
> 3. **Read the signs** (with constant $1$ on the right): three $+$ signs give an ellipsoid; one $-$ sign, a hyperboloid of one sheet, with axis along the negative variable; two $-$ signs, a hyperboloid of two sheets, with axis along the positive variable. If the constant is $0$ and the signs are mixed, it is a cone, with axis along the variable whose sign differs from the other two (if all three signs agree, the only point is the origin).
> 4. **Check with traces** in the coordinate planes and in a few parallel planes, and use them to sketch.

^rem-85-2

> [!example] Example §85.5: Completing the Square
> **(a)** Classify $x^2 + 2z^2 - 6x - y + 10 = 0$. Completing the square in $x$,
>
> $$
> (x^2 - 6x + 9) + 2z^2 - y + 10 - 9 = 0 \qquad\Longrightarrow\qquad y - 1 = (x - 3)^2 + 2z^2 .
> $$
>
> This is an elliptic paraboloid (Theorem §85.2 with the variables exchanged), with axis parallel to the $y$-axis and vertex shifted to $(3, 1, 0)$. Its traces in the planes $y = k$, $k > 1$, are the ellipses $(x - 3)^2 + 2z^2 = k - 1$; its trace in the $xy$-plane is the parabola $y = 1 + (x - 3)^2$, $z = 0$.
>
> **(b)** Identify $x = y^2 + z^2 - 2y - 4z + 5$. Completing squares in $y$ and $z$: $x = (y - 1)^2 + (z - 2)^2 + 5 - 1 - 4 = (y - 1)^2 + (z - 2)^2$. This is a circular paraboloid opening in the positive $x$-direction, with vertex $(0, 1, 2)$; the traces $x = k > 0$ are circles of radius $\sqrt{k}$ centered on the line $y = 1$, $z = 2$.
>
> **(c)** Identify $x^2 = y^2 + 4z^2$. All three variables are squared and there is no constant: a cone. Its axis is the $x$-axis, the variable alone on one side, and its traces $x = k$ are the ellipses $y^2 + 4z^2 = k^2$.
>
> *Stewart: Example 12.6.8*
> *Source: 233 Exam 1 Review, Q9(a), (c)*

^ex-85-5

## Applications of Quadric Surfaces

> [!remark]- Remark: Quadric Surfaces in the World
> The earth is commonly modeled as a sphere, but an ellipsoid is more accurate, because the earth's rotation flattens it at the poles. Circular paraboloids, obtained by rotating a parabola about its axis, collect and reflect light, sound, radio and television signals: in a satellite dish or radio telescope, signals from far away that strike the bowl are all reflected to the receiver at the focus. Cooling towers for nuclear reactors are often hyperboloids of one sheet, for structural stability, and pairs of hyperboloids are used as gears transmitting rotation between skew axes (the cogs are the generating lines of the hyperboloids).

^rem-85-3
