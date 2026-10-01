---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 90
stewart: "14.1"
aliases: ["Stewart 14.1"]
tags: [calculus, math233]
---
← [[§89 Motion in Space꞉ Velocity and Acceleration]] · ↑ [[· 14 Partial Derivatives]] · [[§91 Limits and Continuity]] →

*Stewart, Section 14.1 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q22), Practice Exam 1 (Q1(d)).*

A function of several variables assigns a number to each point of a region in the plane or in space: the temperature at a point of the earth's surface, the volume of a cylinder of given radius and height. This section sets up the vocabulary for the rest of the chapter: domain and range, the graph of a function of two variables (a surface in $\mathbb{R}^3$), and its level curves (a contour map in the plane). The graph lives one dimension up and the contour map lives in the domain. For a function of three variables the graph would need four dimensions, so its level surfaces take over the role of the picture.

## Functions of Two Variables

> [!definition] Definition §90.1: Function of Two Variables
> A **function $f$ of two variables** is a rule that assigns to each ordered pair of real numbers $(x, y)$ in a set $D$ a unique real number denoted by $f(x, y)$. The set $D$ is the **domain** of $f$, and its **range** is the set of values that $f$ takes on, that is, $\{f(x, y) \mid (x, y) \in D\}$.
>
> Writing $z = f(x, y)$, the variables $x$ and $y$ are the **independent variables** and $z$ is the **dependent variable**. If $f$ is given by a formula and no domain is specified, the domain is understood to be the set of all pairs $(x, y)$ for which the formula defines a real number.
>
> *Stewart: 14.1, Definition (unnumbered) and text*

^def-90-1

A function of two variables is a function whose domain is a subset of $\mathbb{R}^2$ and whose range is a subset of $\mathbb{R}$. An arrow diagram pictures it: the domain $D$ drawn in the $xy$-plane, and arrows from each point $(x, y)$ to the number $f(x, y)$ on a vertical number line, the $z$-axis.

> [!example] Example §90.1: Domains
> Evaluate and find the domain:
>
> $$
> \text{(a)}\ f(x, y) = \frac{\sqrt{x + y + 1}}{x - 1} \qquad \text{(b)}\ f(x, y) = x \ln(y^2 - x) \qquad \text{(c)}\ f(x, y, z) = \ln(z - y) + xy \sin z .
> $$
>
> **(a)** $f(3, 2) = \dfrac{\sqrt{3 + 2 + 1}}{3 - 1} = \dfrac{\sqrt 6}{2}$. The formula makes sense when the quantity under the square root is nonnegative and the denominator is not $0$:
>
> $$
> D = \{(x, y) \mid x + y + 1 \ge 0,\ x \ne 1\} .
> $$
>
> The inequality $x + y + 1 \ge 0$, or $y \ge -x - 1$, describes the points on or above the line $y = -x - 1$; from these the points on the vertical line $x = 1$ are removed.
>
> **(b)** $f(3, 2) = 3 \ln(2^2 - 3) = 3 \ln 1 = 0$. Since $\ln(y^2 - x)$ is defined only when $y^2 - x > 0$,
>
> $$
> D = \{(x, y) \mid x < y^2\} ,
> $$
>
> the set of points to the left of the parabola $x = y^2$. The parabola itself is not included.
>
> **(c)** A function of three variables ([[§90 Functions of Several Variables#^def-90-5|Definition §90.5]]). The term $xy \sin z$ is defined everywhere, and $\ln(z - y)$ needs $z - y > 0$. So
>
> $$
> D = \{(x, y, z) \in \mathbb{R}^3 \mid z > y\} ,
> $$
>
> a **half-space**: all points that lie above the plane $z = y$.
>
> *Stewart: Examples 14.1.1 and 14.1.14*

^ex-90-1

> [!remark]- Remark: Functions Given by Words and by Tables
> Not every function comes with a formula. Stewart's two examples:
> - The **wind-chill index** $W = f(T, v)$ is the temperature that it *feels* like when the actual temperature is $T$ (°C) and the wind speed is $v$ (km/h). It is given by a table of values from the weather services; for instance the entry $f(-5, 50) = -15$ says that $-5\,$°C with a $50\,$km/h wind feels like $-15\,$°C with no wind.
> - The **Cobb–Douglas production function** $P(L, K) = bL^{\alpha} K^{1 - \alpha}$ models the total production $P$ of an economy from the labor $L$ and the capital $K$. Cobb and Douglas (1928) fitted $P(L, K) = 1.01\,L^{0.75} K^{0.25}$ to US data for 1899–1922 (with 1899 values set to $100$). The model gives $P(147, 208) \approx 161.9$ and $P(194, 407) \approx 235.8$ for 1910 and 1920, close to the actual values $159$ and $231$. Its domain is $\{(L, K) \mid L \ge 0,\ K \ge 0\}$, since labor and capital are never negative.

^rem-90-1

## Graphs

> [!definition] Definition §90.2: Graph
> If $f$ is a function of two variables with domain $D$, the **graph** of $f$ is the set of all points $(x, y, z)$ in $\mathbb{R}^3$ such that $z = f(x, y)$ and $(x, y)$ is in $D$.
>
> *Stewart: 14.1, Definition (unnumbered)*

^def-90-2

The graph of $f$ is a surface $S$ with equation $z = f(x, y)$, lying directly above or below the domain $D$ in the $xy$-plane: the point of $S$ over $(x, y)$ is at height $f(x, y)$.

> [!definition] Definition §90.3: Linear Function
> A function of the form
>
> $$
> f(x, y) = ax + by + c
> $$
>
> is a **linear function**. Its graph has the equation $z = ax + by + c$, or $ax + by - z + c = 0$, so it is a plane ([[§84 Equations of Lines and Planes|§84]]).
>
> *Stewart: 14.1 (text)*

^def-90-3

Linear functions of two variables play the role in multivariable calculus that linear functions of one variable play in single-variable calculus: they are the functions we approximate by ([[§93 Tangent Planes and Linear Approximations|§93]]).

> [!example] Example §90.2: A Hemisphere
> Let $g(x, y) = \sqrt{9 - x^2 - y^2}$. Find the domain and range of $g$, sketch its graph, and describe its level curves for $k = 0, 1, 2, 3$.
>
> **Domain.** The square root needs $9 - x^2 - y^2 \ge 0$:
>
> $$
> D = \{(x, y) \mid x^2 + y^2 \le 9\} ,
> $$
>
> the disk with center $(0, 0)$ and radius $3$.
>
> **Range.** $z = \sqrt{9 - x^2 - y^2}$ is a nonnegative square root, so $z \ge 0$. Since $9 - x^2 - y^2 \le 9$, also $z \le 3$. Every value in between occurs: along the $x$-axis, $g(x, 0) = \sqrt{9 - x^2}$ decreases continuously from $3$ to $0$ as $x$ runs from $0$ to $3$. So the range is
>
> $$
> \{z \mid 0 \le z \le 3\} = [0, 3] .
> $$
>
> **Graph.** Squaring $z = \sqrt{9 - x^2 - y^2}$ gives $z^2 = 9 - x^2 - y^2$, or $x^2 + y^2 + z^2 = 9$: the sphere with center the origin and radius $3$. Since $z \ge 0$, the graph of $g$ is the top half of this sphere. An entire sphere cannot be the graph of a single function of $x$ and $y$ (a vertical line through the inside meets it twice); the lower hemisphere is the graph of $h(x, y) = -\sqrt{9 - x^2 - y^2}$.
>
> **Level curves** ([[§90 Functions of Several Variables#^def-90-4|Definition §90.4]]).
>
> $$
> \sqrt{9 - x^2 - y^2} = k \quad\Longleftrightarrow\quad x^2 + y^2 = 9 - k^2 \qquad (0 \le k \le 3) .
> $$
>
> These are concentric circles with center $(0, 0)$ and radius $\sqrt{9 - k^2}$: radius $3$, $\sqrt 8$, $\sqrt 5$ for $k = 0, 1, 2$, and the single point $(0, 0)$ for $k = 3$. Lifted to height $k$, they are the horizontal circles that make up the hemisphere. The circles crowd together near the edge of the disk, where the hemisphere is steep.
>
> *Stewart: Examples 14.1.2, 14.1.6 and 14.1.11*

^ex-90-2

## Level Curves and Contour Maps

> [!definition] Definition §90.4: Level Curves and Contour Map
> The **level curves** of a function $f$ of two variables are the curves with equations $f(x, y) = k$, where $k$ is a constant (in the range of $f$). A collection of level curves is called a **contour map** of $f$. Unless indicated otherwise, the values of $k$ in a contour map are equally spaced.
>
> *Stewart: 14.1, Definition (unnumbered) and text*

^def-90-4

> [!remark] Remark: Reading a Contour Map
> The level curve $f(x, y) = k$ is the set of points of the domain at which $f$ takes the value $k$: it shows where the graph of $f$ has height $k$. In other words, it is the trace of the graph in the horizontal plane $z = k$, projected down to the $xy$-plane. Lifting each level curve to its height reassembles the graph.
>
> Since the values of $k$ are equally spaced, the surface is **steep where the level curves are close together** and flatter where they are far apart. Familiar examples are topographic maps (curves of constant elevation; walking along one you neither climb nor descend), **isothermals** on a weather map (constant temperature) and **isobars** (constant pressure). To estimate a value from a contour map, interpolate between neighboring curves: a point a little closer to the curve $k = 70$ than to the curve $k = 80$ has a value of about $73$ (Stewart, Example 14.1.9).

^rem-90-2

> [!example] Example §90.3: A Plane and an Elliptic Paraboloid
> **(a)** Sketch the graph of $f(x, y) = 6 - 3x - 2y$ and its level curves for $k = -6, 0, 6, 12$.
>
> The graph $z = 6 - 3x - 2y$, or $3x + 2y + z = 6$, is a plane ([[§90 Functions of Several Variables#^def-90-3|Definition §90.3]]). Putting $y = z = 0$ gives the $x$-intercept $2$; likewise the $y$-intercept is $3$ and the $z$-intercept is $6$, which fixes the triangle of the plane in the first octant. The level curves are
>
> $$
> 6 - 3x - 2y = k \quad\Longleftrightarrow\quad 3x + 2y + (k - 6) = 0 ,
> $$
>
> a family of parallel lines with slope $-\frac32$. For $k = -6, 0, 6, 12$ they are $3x + 2y - 12 = 0$, $3x + 2y - 6 = 0$, $3x + 2y = 0$ and $3x + 2y + 6 = 0$. Equally spaced values of $k$ give equally spaced lines, because the graph is a plane: its steepness is the same everywhere.
>
> **(b)** Find the domain and range of $h(x, y) = 4x^2 + y^2 + 1$ and describe its level curves.
>
> $h$ is defined for every pair $(x, y)$, so the domain is $\mathbb{R}^2$. Since $x^2 \ge 0$ and $y^2 \ge 0$, $h(x, y) \ge 1$, and $h(0, y) = y^2 + 1$ takes every value $\ge 1$; so the range is $[1, \infty)$. The level curves are
>
> $$
> 4x^2 + y^2 + 1 = k \quad\Longleftrightarrow\quad \frac{x^2}{\frac14 (k - 1)} + \frac{y^2}{k - 1} = 1 \qquad (k > 1) ,
> $$
>
> a family of ellipses with semiaxes $\frac12 \sqrt{k - 1}$ and $\sqrt{k - 1}$ (and the single point $(0, 0)$ for $k = 1$). Lifted to height $k$ they become the horizontal traces of the graph $z = 4x^2 + y^2 + 1$, an elliptic paraboloid with vertex $(0, 0, 1)$ ([[§85 Cylinders and Quadric Surfaces|§85]]). Its vertical traces are parabolas.
>
> *Stewart: Examples 14.1.5, 14.1.8, 14.1.10 and 14.1.12*

^ex-90-3

> [!example] Example §90.4: Two Contour Maps from the Exams
> **(a)** Sketch the level curves of $f(x, y) = y e^x$ for the integers $-3 \le k \le 3$.
>
> $$
> y e^x = k \quad\Longleftrightarrow\quad y = k e^{-x} .
> $$
>
> For $k = 0$ the level curve is the $x$-axis. For $k = 1, 2, 3$ it is a decaying exponential curve above the $x$-axis through $(0, k)$, and for $k = -1, -2, -3$ its mirror image below the axis. All of them approach the $x$-axis as $x \to \infty$ and spread apart as $x \to -\infty$. So the graph of $f$ is steep for large $x$ (there the curves crowd together; indeed $f$ changes by $e^x \Delta y$ when $y$ changes by $\Delta y$) and nearly flat for very negative $x$. Every value $k$ occurs, so the range of $f$ is $\mathbb{R}$.
>
> **(b)** Describe the level curves of $f(x, y) = \sqrt{1 - x^2 - 2y^2}$. (Choices: concentric circles; concentric ellipses (not circles); parabolas with the same vertex; parabolas with different vertices; hyperbolas with the same vertex; hyperbolas with different vertices.)
>
> The values of $f$ lie in $[0, 1]$. For $0 \le k \le 1$,
>
> $$
> \sqrt{1 - x^2 - 2y^2} = k \quad\Longleftrightarrow\quad x^2 + 2y^2 = 1 - k^2 \quad\Longleftrightarrow\quad \frac{x^2}{1 - k^2} + \frac{y^2}{\frac12 (1 - k^2)} = 1 .
> $$
>
> For $k < 1$ these are ellipses with center $(0, 0)$ and semiaxes $\sqrt{1 - k^2}$ and $\sqrt{(1 - k^2)/2}$, in the ratio $\sqrt 2 : 1$, so they are not circles; for $k = 1$ the level set is the single point $(0, 0)$. **Answer: concentric ellipses (not circles).**
>
> *Source: 233 Midterm 1 Practice Questions, Q22*
> *Source: 233 Practice Exam 1, Q1(d)*

^ex-90-4

![[m233-90-1.svg]]
*Contour map of $f(x, y) = y e^x$ (Example §90.4(a)). The level curves $y = k e^{-x}$ for $k = 1, 2, 3$ (blue) and $k = -1, -2, -3$ (red) all approach the $x$-axis, the level curve $k = 0$. Where they crowd together, on the right, the graph of $f$ is steep; on the left it is nearly flat.*

## Functions of Three or More Variables

> [!definition] Definition §90.5: Function of Three Variables; Level Surfaces
> A **function of three variables**, $f$, is a rule that assigns to each ordered triple $(x, y, z)$ in a domain $D \subseteq \mathbb{R}^3$ a unique real number denoted by $f(x, y, z)$.
>
> The **level surfaces** of $f$ are the surfaces with equations $f(x, y, z) = k$, where $k$ is a constant. As the point $(x, y, z)$ moves along a level surface, the value $f(x, y, z)$ stays fixed.
>
> *Stewart: 14.1 (text)*

^def-90-5

For instance, the temperature $T$ at a point on the surface of the earth depends on the longitude $x$, the latitude $y$ and the time $t$, so $T = f(x, y, t)$. The graph of a function of three variables would lie in four-dimensional space, so we picture $f$ by its level surfaces instead.

> [!example] Example §90.5: Level Surfaces
> **(a)** The level surfaces of $f(x, y, z) = x^2 + y^2 + z^2$ are
>
> $$
> x^2 + y^2 + z^2 = k , \qquad k \ge 0 ,
> $$
>
> a family of concentric spheres with center the origin and radius $\sqrt k$ (the origin itself for $k = 0$; empty for $k < 0$). As $(x, y, z)$ varies over a sphere with center $O$, the value of $f$, the squared distance to $O$, stays fixed.
>
> **(b)** The level surfaces of $f(x, y, z) = x^2 - y - z^2$ are
>
> $$
> x^2 - y - z^2 = k \quad\Longleftrightarrow\quad y = x^2 - z^2 - k ,
> $$
>
> a family of hyperbolic paraboloids ([[§85 Cylinders and Quadric Surfaces|§85]]), each obtained from $y = x^2 - z^2$ by a shift of $-k$ along the $y$-axis.
>
> *Stewart: Examples 14.1.15 and 14.1.16*

^ex-90-5

> [!definition] Definition §90.6: Function of n Variables
> A **function of $n$ variables** is a rule that assigns a number $z = f(x_1, x_2, \ldots, x_n)$ to each $n$-tuple $(x_1, x_2, \ldots, x_n)$ of real numbers in its domain, a subset of $\mathbb{R}^n$. Writing $\mathbf{x} = \langle x_1, x_2, \ldots, x_n \rangle$, we also write $f(\mathbf{x})$ for $f(x_1, \ldots, x_n)$. So a function on a subset of $\mathbb{R}^n$ can be regarded in three ways:
> 1. as a function of $n$ real variables $x_1, x_2, \ldots, x_n$;
> 2. as a function of a single point variable $(x_1, x_2, \ldots, x_n)$;
> 3. as a function of a single vector variable $\mathbf{x} = \langle x_1, x_2, \ldots, x_n \rangle$.
>
> For example, if $n$ ingredients cost $c_i$ per unit and $x_i$ units of the $i$th ingredient are used, the total cost is
>
> $$
> C = f(x_1, \ldots, x_n) = c_1 x_1 + c_2 x_2 + \cdots + c_n x_n = \mathbf{c} \cdot \mathbf{x} , \qquad \mathbf{c} = \langle c_1, \ldots, c_n \rangle ,
> $$
>
> a linear function of $n$ variables, written with the dot product ([[§82 The Dot Product|§82]]).
>
> *Stewart: 14.1, Equation 3 and text*

^def-90-6

> [!remark]- Connections
> - A function $f(\mathbf{x}) = \mathbf{c} \cdot \mathbf{x}$ is a linear functional on $\mathbb{R}^n$, given by the dot product [[§19 Inner Products and Norms#^ladr-6-1|LADR 6.1]]; every linear functional on $\mathbb{R}^n$ has this form (the Riesz representation theorem in its simplest case).
