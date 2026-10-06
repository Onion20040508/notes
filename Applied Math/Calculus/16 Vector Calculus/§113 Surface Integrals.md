---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 113
stewart: "16.7"
aliases: ["Stewart 16.7"]
tags: [calculus, math233]
---
← [[§112 Parametric Surfaces and Their Areas]] · ↑ [[· 16 Vector Calculus]] · [[§114 Stokes' Theorem]] →

*Stewart, Section 16.7 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q4), Practice Final Exam (Q5), Practice Final Set 1 (Part II, Q5).*

Surface integrals are to surface area what line integrals are to arc length. The surface integral of a scalar function, $\iint_S f\,dS$, weights each patch of $S$ by its area; it is computed as a double integral over the parameter domain with the area factor $|\mathbf{r}_u \times \mathbf{r}_v|$ of [[§112 Parametric Surfaces and Their Areas#^def-112-4|Definition §112.4]]. The surface integral of a vector field, $\iint_S \mathbf{F} \cdot d\mathbf{S}$, is the flux of $\mathbf{F}$ across $S$: the integral of its normal component, which measures the rate of flow through $S$. Flux needs a choice of normal direction, an orientation, and its sign depends on that choice; the convention for closed surfaces is the outward normal. These integrals are one side of Stokes' Theorem and of the Divergence Theorem.

## Surface Integrals of Scalar Functions

Let $S$ have vector equation $\mathbf{r}(u, v) = x(u, v)\,\mathbf{i} + y(u, v)\,\mathbf{j} + z(u, v)\,\mathbf{k}$, $(u, v) \in D$. Suppose first that $D$ is a rectangle, divided into subrectangles $R_{ij}$ with dimensions $\Delta u$ and $\Delta v$; then $S$ is divided into corresponding patches $S_{ij}$. Evaluate $f$ at a point $P_{ij}^*$ in each patch, multiply by the area $\Delta S_{ij}$ of the patch, and sum.

> [!definition] Definition §113.1: Surface Integral of a Function
> The **surface integral of $f$ over the surface $S$** is
>
> $$
> \iint_S f(x, y, z)\,dS = \lim_{m, n \to \infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(P_{ij}^*)\,\Delta S_{ij} . \qquad (1)
> $$
>
> (Compare the line integral, [[§108 Line Integrals#^def-108-1|Definition §108.1]], and the double integral, [[§98 Double Integrals Over Rectangles#^def-98-2|Definition §98.2]].)
>
> *Stewart: 16.7, Equation 1*

^def-113-1

> [!theorem] Theorem §113.1: Evaluating a Surface Integral
> If the components of $\mathbf{r}$ are continuous, $\mathbf{r}_u$ and $\mathbf{r}_v$ are nonzero and nonparallel in the interior of $D$, and $S$ is covered only once as $(u, v)$ ranges throughout $D$, then (even when $D$ is not a rectangle)
>
> $$
> \iint_S f(x, y, z)\,dS = \iint_D f(\mathbf{r}(u, v))\,|\mathbf{r}_u \times \mathbf{r}_v|\,dA . \qquad (2)
> $$
>
> The value does not depend on the parametrization used. In particular $\iint_S 1\,dS = \iint_D |\mathbf{r}_u \times \mathbf{r}_v|\,dA = A(S)$.
>
> *Stewart: 16.7, Equation 2*

^thm-113-1

*Stewart only motivates Formula 2 ("it can be shown from Definition 1"): the patch area is approximated by $\Delta S_{ij} \approx |\mathbf{r}_u \times \mathbf{r}_v|\,\Delta u\,\Delta v$, as in [[§112 Parametric Surfaces and Their Areas#^rem-112-1|the surface area argument]]. 452 takes Formula 2 as the definition, with the area element derived from the Gram matrix: [[§18 Surface Integrals#^def-18-5|452 Def. §18.5]], [[§18 Surface Integrals#^thm-18-1|452 Thm. §18.1]].*

> [!remark]- Connections
> - The scalar surface integral in 452: [[§18 Surface Integrals#^def-18-5|452 Def. §18.5]], with the table comparing it to the scalar line integral $\int_\gamma f\,ds = \int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt$. Neither is the integral of a differential form, since neither sees orientation: [[§22 The Algebra of Differential Forms#^rem-22-8|452 Remark: Scalar Integrals Are Not Form Integrals]].

To use Formula 2, evaluate $f(\mathbf{r}(u, v))$ by writing $x = x(u, v)$, $y = y(u, v)$, $z = z(u, v)$ in the formula for $f(x, y, z)$.

> [!example] Example §113.1: A Parallelogram
> Let $S$ be the parallelogram parametrized by $\mathbf{r}(u, v) = \langle u + v,\ u - v,\ 1 + 2u + v \rangle$, $0 \le u \le 2$, $0 \le v \le 1$. Compute $\iint_S (x + y + z)\,dS$.
>
> $S$ is a piece of a plane, as in [[§112 Parametric Surfaces and Their Areas#^ex-112-1|Example §112.1]], with $\mathbf{r}_u = \langle 1, 1, 2 \rangle$ and $\mathbf{r}_v = \langle 1, -1, 1 \rangle$. Then
>
> $$
> \mathbf{r}_u \times \mathbf{r}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 2 \\ 1 & -1 & 1 \end{vmatrix} = (1 + 2)\,\mathbf{i} - (1 - 2)\,\mathbf{j} + (-1 - 1)\,\mathbf{k} = \langle 3, 1, -2 \rangle, \qquad |\mathbf{r}_u \times \mathbf{r}_v| = \sqrt{9 + 1 + 4} = \sqrt{14} .
> $$
>
> On $S$, $x + y + z = (u + v) + (u - v) + (1 + 2u + v) = 4u + v + 1$. By Formula 2,
>
> $$
> \iint_S (x + y + z)\,dS = \int_0^2 \int_0^1 (4u + v + 1)\sqrt{14}\,dv\,du = \sqrt{14} \int_0^2 \left(4u + \tfrac32\right) du = \sqrt{14}\,\big(8 + 3\big) = 11\sqrt{14} .
> $$
>
> *Source: 233 Practice Final Exam, Q5*

^ex-113-1

> [!definition] Definition §113.2: Mass of a Thin Sheet
> If a thin sheet (say, of aluminum foil) has the shape of a surface $S$ and density (mass per unit area) $\rho(x, y, z)$ at $(x, y, z)$, its total **mass** is
>
> $$
> m = \iint_S \rho(x, y, z)\,dS ,
> $$
>
> *Stewart: 16.7 (text)*

^def-113-2

> [!definition] Definition §113.3: Center of Mass of a Thin Sheet
> For a thin sheet with the shape of a surface $S$, density $\rho(x, y, z)$ and mass $m$ ([[§113 Surface Integrals#^def-113-2|Definition §113.2]]), its **center of mass** is $(\bar{x}, \bar{y}, \bar{z})$, where
>
> $$
> \bar{x} = \frac1m \iint_S x\,\rho(x, y, z)\,dS, \qquad \bar{y} = \frac1m \iint_S y\,\rho(x, y, z)\,dS, \qquad \bar{z} = \frac1m \iint_S z\,\rho(x, y, z)\,dS .
> $$
>
> *Stewart: 16.7 (text)*

^def-113-new1

> [!theorem] Theorem §113.2: Surface Integrals over Graphs
> If $S$ has equation $z = g(x, y)$ and $D$ is its projection onto the $xy$-plane, then
>
> $$
> \mathbf{r}_x \times \mathbf{r}_y = -\frac{\partial g}{\partial x}\,\mathbf{i} - \frac{\partial g}{\partial y}\,\mathbf{j} + \mathbf{k} \qquad (3)
> $$
>
> and
>
> $$
> \iint_S f(x, y, z)\,dS = \iint_D f(x, y, g(x, y)) \sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 + 1}\,dA . \qquad (4)
> $$
>
> Similar formulas hold when $S$ projects onto another coordinate plane; for instance, if $S$ has equation $y = h(x, z)$ and $D$ is its projection onto the $xz$-plane, then
>
> $$
> \iint_S f(x, y, z)\,dS = \iint_D f(x, h(x, z), z) \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 + \left(\frac{\partial y}{\partial z}\right)^2 + 1}\,dA .
> $$
>
> *Stewart: 16.7, Equations 3 and 4*

^thm-113-2

> [!proof]+ Proof
> Regard $S$ as a parametric surface with parametric equations $x = x$, $y = y$, $z = g(x, y)$. Then $\mathbf{r}_x = \mathbf{i} + (\partial g/\partial x)\,\mathbf{k}$ and $\mathbf{r}_y = \mathbf{j} + (\partial g/\partial y)\,\mathbf{k}$, and their cross product is (3), with length $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}$ (the computation of [[§112 Parametric Surfaces and Their Areas#^thm-112-2|Theorem §112.2]]). Substituting into Formula 2 gives (4). For $y = h(x, z)$, use the parameters $x$ and $z$ in the same way: $\mathbf{r}_x = \mathbf{i} + h_x\,\mathbf{j}$, $\mathbf{r}_z = h_z\,\mathbf{j} + \mathbf{k}$, and $|\mathbf{r}_x \times \mathbf{r}_z| = |\langle h_x, -1, h_z \rangle| = \sqrt{h_x^2 + h_z^2 + 1}$.

^pf-113-2

*Uses:* [[§113 Surface Integrals#^thm-113-1|§113.1]], [[§112 Parametric Surfaces and Their Areas#^thm-112-2|§112.2]], [[§112 Parametric Surfaces and Their Areas#^prop-112-1|§112.1]]

For example, for $S$: $z = x + y^2$, $0 \le x \le 1$, $0 \le y \le 2$, Formula 4 gives $\iint_S y\,dS = \int_0^1 \int_0^2 y\sqrt{1 + 1 + 4y^2}\,dy\,dx = \sqrt2 \int_0^2 y\sqrt{1 + 2y^2}\,dy = \sqrt2 \cdot \frac14 \cdot \frac23 (1 + 2y^2)^{3/2} \Big]_0^2 = \frac{13\sqrt2}{3}$ (Stewart, Example 16.7.2).

> [!definition] Definition §113.3: Piecewise-Smooth Surface
> A **piecewise-smooth surface** $S$ is a finite union of smooth surfaces $S_1, S_2, \ldots, S_n$ that intersect only along their boundaries. The surface integral of $f$ over $S$ is
>
> $$
> \iint_S f(x, y, z)\,dS = \iint_{S_1} f(x, y, z)\,dS + \cdots + \iint_{S_n} f(x, y, z)\,dS .
> $$
>
> *Stewart: 16.7 (text)*

^def-113-3

For instance, if $S$ consists of the cylinder $x^2 + y^2 = 1$ (sides $S_1$), the unit disk in the plane $z = 0$ (bottom $S_2$) and the part of the plane $z = 1 + x$ above it (top $S_3$), then $\iint_{S_1} z\,dS = \frac{3\pi}{2}$ (parametrize by $\theta$ and $z$, $0 \le z \le 1 + \cos\theta$, with $|\mathbf{r}_\theta \times \mathbf{r}_z| = 1$), $\iint_{S_2} z\,dS = 0$, and $\iint_{S_3} z\,dS = \sqrt2\,\pi$ (Formula 4), so $\iint_S z\,dS = \left(\frac32 + \sqrt2\right)\pi$ (Stewart, Example 16.7.3).

## Oriented Surfaces

To define surface integrals of vector fields, nonorientable surfaces such as the **Möbius strip** must be ruled out. (Take a long rectangular strip of paper, give it a half-twist, and tape the short edges together. An ant crawling along the middle starting at a point $P$ ends up on the "other side" and then, continuing, back at $P$ without ever crossing an edge: the strip has only one side.)

> [!definition] Definition §113.4: Oriented Surface
> Let $S$ be a surface that has a tangent plane at every point $(x, y, z)$ (except at any boundary point). There are two unit normal vectors $\mathbf{n}_1$ and $\mathbf{n}_2 = -\mathbf{n}_1$ at $(x, y, z)$. If it is possible to choose a unit normal vector $\mathbf{n}$ at every such point so that $\mathbf{n}$ varies continuously over $S$, then $S$ is called an **oriented surface**, and the choice of $\mathbf{n}$ provides $S$ with an **orientation**. Every orientable (two-sided) surface has two possible orientations.
>
> *Stewart: 16.7 (text)*

^def-113-4

> [!definition] Definition §113.5: Standard Orientations of Graphs and Parametric Surfaces
> **Graphs.** A surface $z = g(x, y)$ has the natural orientation given by the unit normal vector
>
> $$
> \mathbf{n} = \frac{-\dfrac{\partial g}{\partial x}\,\mathbf{i} - \dfrac{\partial g}{\partial y}\,\mathbf{j} + \mathbf{k}}{\sqrt{1 + \left(\dfrac{\partial g}{\partial x}\right)^2 + \left(\dfrac{\partial g}{\partial y}\right)^2}} . \qquad (5)
> $$
>
> Its $\mathbf{k}$-component is positive, so this is the **upward orientation** of the surface; $-\mathbf{n}$ gives the downward orientation.
>
> **Parametric surfaces.** A smooth orientable surface given by $\mathbf{r}(u, v)$ is automatically supplied with the orientation of the unit normal vector
>
> $$
> \mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{|\mathbf{r}_u \times \mathbf{r}_v|} , \qquad (6)
> $$
>
> and the opposite orientation is given by $-\mathbf{n}$ (obtained, for instance, by reversing the order of the parameters, since $\mathbf{r}_v \times \mathbf{r}_u = -\mathbf{r}_u \times \mathbf{r}_v$).
>
> *Stewart: 16.7, Equations 5 and 6*

^def-113-5

For the sphere $\mathbf{r}(\phi, \theta) = a\sin\phi\cos\theta\,\mathbf{i} + a\sin\phi\sin\theta\,\mathbf{j} + a\cos\phi\,\mathbf{k}$, [[§112 Parametric Surfaces and Their Areas#^ex-112-4|Example §112.4]] gives $\mathbf{r}_\phi \times \mathbf{r}_\theta = a^2\sin\phi\,(\sin\phi\cos\theta\,\mathbf{i} + \sin\phi\sin\theta\,\mathbf{j} + \cos\phi\,\mathbf{k})$ and $|\mathbf{r}_\phi \times \mathbf{r}_\theta| = a^2\sin\phi$, so the induced orientation is

$$
\mathbf{n} = \sin\phi\cos\theta\,\mathbf{i} + \sin\phi\sin\theta\,\mathbf{j} + \cos\phi\,\mathbf{k} = \frac1a\,\mathbf{r}(\phi, \theta) ,
$$

which points in the same direction as the position vector: outward from the sphere. The parametrization $\mathbf{r}(\theta, \phi)$ would induce the inward orientation.

> [!definition] Definition §113.6: Closed Surface
> A **closed surface** is a surface that is the boundary of a solid region $E$.
>
> *Stewart: 16.7 (text)*

^def-113-6

> [!definition] Definition §113.7: Positive Orientation of a Closed Surface
> For a closed surface, the convention is that the **positive orientation** is the one for which the normal vectors point *outward* from $E$; inward-pointing normals give the negative orientation.
>
> *Stewart: 16.7 (text)*

^def-113-new2

> [!example] Example §113.2: Choosing the Normal for a Given Orientation
> Find a normal vector for each surface with the given orientation.
>
> **(a)** The hemisphere of radius $2$ on the right side of the $xz$-plane ($x^2 + y^2 + z^2 = 4$, $y \ge 0$), outward. The gradient of $x^2 + y^2 + z^2$ is $\langle 2x, 2y, 2z \rangle$, normal to the sphere and pointing away from the origin, so $\mathbf{n} = \frac12\langle x, y, z \rangle$ (unit, outward), as for the sphere above. (The posted solution writes the hemisphere as the graph $y = \sqrt{4 - x^2 - z^2}$ and uses $\big\langle \frac{x}{\sqrt{4 - x^2 - z^2}},\ 1,\ \frac{z}{\sqrt{4 - x^2 - z^2}} \big\rangle$, which is this vector times $2/y$.)
>
> **(b)** The cylinder $\mathbf{r}(u, v) = \langle 2\cos u, 2\sin u, v \rangle$, $0 \le u \le 2\pi$, $-1 \le v \le 1$, inward. Here $\mathbf{r}_u = \langle -2\sin u, 2\cos u, 0 \rangle$, $\mathbf{r}_v = \langle 0, 0, 1 \rangle$ and
>
> $$
> \mathbf{r}_u \times \mathbf{r}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -2\sin u & 2\cos u & 0 \\ 0 & 0 & 1 \end{vmatrix} = \langle 2\cos u,\ 2\sin u,\ 0 \rangle ,
> $$
>
> which points away from the axis (it equals $\langle x, y, 0 \rangle$). For the inward orientation take $\mathbf{r}_v \times \mathbf{r}_u = \langle -2\cos u, -2\sin u, 0 \rangle$.
>
> **(c)** The bottom half of the cone $z^2 = x^2 + y^2$, upward. The bottom half is the graph of $g(x, y) = -\sqrt{x^2 + y^2}$, and by (5) the upward normal is
>
> $$
> \left\langle -g_x, -g_y, 1 \right\rangle = \left\langle \frac{x}{\sqrt{x^2 + y^2}},\ \frac{y}{\sqrt{x^2 + y^2}},\ 1 \right\rangle \qquad (x, y) \ne (0, 0) .
> $$
>
> **(d)** The surface $z = \ln(x + 2y)$, upward: $\langle -g_x, -g_y, 1 \rangle = \left\langle -\dfrac{1}{x + 2y},\ -\dfrac{2}{x + 2y},\ 1 \right\rangle$.
>
> **(e)** The part of the plane $z = x + 3$ inside the cylinder $x^2 + y^2 = 1$, downward. The upward normal is $\langle -1, 0, 1 \rangle$, so the downward one is $\langle 1, 0, -1 \rangle$.
>
> In each case the rule is: compute a normal from (5), (6) or a gradient, then check its direction at one convenient point and flip it if needed.
>
> *Source: 233 Chapter 16 Review, Q4*

^ex-113-2

## Surface Integrals of Vector Fields; Flux

> [!remark] Remark: Where the Flux Integral Comes From
> Let $S$ be an oriented surface with unit normal $\mathbf{n}$, and imagine a fluid with density $\rho(x, y, z)$ and velocity field $\mathbf{v}(x, y, z)$ flowing through $S$ (think of $S$ as an imaginary surface, like a fishing net across a stream). The rate of flow (mass per unit time) per unit area is the vector field $\rho\mathbf{v}$. If $S$ is divided into small patches $S_{ij}$, each nearly planar, the mass of fluid per unit time crossing $S_{ij}$ in the direction of $\mathbf{n}$ is approximately $(\rho\mathbf{v} \cdot \mathbf{n})\,A(S_{ij})$, since $\rho\mathbf{v} \cdot \mathbf{n}$ is the component of $\rho\mathbf{v}$ in the direction of $\mathbf{n}$. Summing and taking the limit, by [[§113 Surface Integrals#^def-113-1|Definition §113.1]] the rate of flow through $S$ is
>
> $$
> \iint_S \rho\mathbf{v} \cdot \mathbf{n}\,dS = \iint_S \rho(x, y, z)\,\mathbf{v}(x, y, z) \cdot \mathbf{n}(x, y, z)\,dS . \qquad (7)
> $$
>
> With $\mathbf{F} = \rho\mathbf{v}$ this is $\iint_S \mathbf{F} \cdot \mathbf{n}\,dS$, an integral that occurs in physics even when $\mathbf{F}$ is not $\rho\mathbf{v}$.

^rem-113-1

> [!definition] Definition §113.7: Surface Integral of a Vector Field; Flux
> If $\mathbf{F}$ is a continuous vector field defined on an oriented surface $S$ with unit normal vector $\mathbf{n}$, then the **surface integral of $\mathbf{F}$ over $S$** is
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{n}\,dS .
> $$
>
> This integral is also called the **flux** of $\mathbf{F}$ across $S$. In words: the surface integral of a vector field over $S$ is the surface integral of its normal component over $S$.
>
> *Stewart: 16.7, Definition 8*

^def-113-7

> [!remark]- Connections
> - The flux integral in 452: [[§18 Surface Integrals#^def-18-6|452 Def. §18.6]], with the vector area element $d\mathbf{S} = (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv$. In forms language it is the integral of a 2-form, and $\mathbf{r}_u \times \mathbf{r}_v$ is a pullback: [[§22 The Algebra of Differential Forms#^def-22-6|452 Def. §22.6]], [[§22 The Algebra of Differential Forms#^rem-22-3|452 Remark: The Cross Product Is the Pullback in Disguise]].

> [!theorem] Theorem §113.3: Flux through a Parametric Surface
> If $S$ is given by $\mathbf{r}(u, v)$, $(u, v) \in D$, and oriented by (6), then
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v)\,dA . \qquad (9)
> $$
>
> For the opposite orientation, multiply by $-1$.
>
> *Stewart: 16.7, Equation 9*

^thm-113-3

> [!proof]+ Proof
> By Definition §113.7, Equation 6 and Formula 2,
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \frac{\mathbf{r}_u \times \mathbf{r}_v}{|\mathbf{r}_u \times \mathbf{r}_v|}\,dS = \iint_D \left[ \mathbf{F}(\mathbf{r}(u, v)) \cdot \frac{\mathbf{r}_u \times \mathbf{r}_v}{|\mathbf{r}_u \times \mathbf{r}_v|} \right] |\mathbf{r}_u \times \mathbf{r}_v|\,dA = \iint_D \mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v)\,dA .
> $$
>
> The opposite orientation has unit normal $-\mathbf{n}$, which changes the sign of the integrand.

^pf-113-3

*Uses:* [[§113 Surface Integrals#^def-113-7|Def. §113.7]], [[§113 Surface Integrals#^def-113-5|Def. §113.5]], [[§113 Surface Integrals#^thm-113-1|§113.1]]

Compare (9) with $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt$ ([[§108 Line Integrals#^def-108-8|Definition §108.8]]): in both, the length factor cancels.

> [!theorem] Theorem §113.4: Flux through a Graph
> If $S$ is the graph $z = g(x, y)$, $(x, y) \in D$, with the upward orientation, and $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$, then
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \left( -P\frac{\partial g}{\partial x} - Q\frac{\partial g}{\partial y} + R \right) dA . \qquad (10)
> $$
>
> For the downward orientation, multiply by $-1$. Similar formulas hold if $S$ is given by $y = h(x, z)$ or $x = k(y, z)$.
>
> *Stewart: 16.7, Equation 10*

^thm-113-4

> [!proof]+ Proof
> With $x$ and $y$ as parameters, (3) gives $\mathbf{r}_x \times \mathbf{r}_y = -g_x\,\mathbf{i} - g_y\,\mathbf{j} + \mathbf{k}$, which induces the upward orientation (5). So
>
> $$
> \mathbf{F} \cdot (\mathbf{r}_x \times \mathbf{r}_y) = (P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}) \cdot \left( -\frac{\partial g}{\partial x}\,\mathbf{i} - \frac{\partial g}{\partial y}\,\mathbf{j} + \mathbf{k} \right) = -P\frac{\partial g}{\partial x} - Q\frac{\partial g}{\partial y} + R ,
> $$
>
> and Formula 9 gives (10). The downward orientation is the opposite one.

^pf-113-4

*Uses:* [[§113 Surface Integrals#^thm-113-3|§113.3]], [[§113 Surface Integrals#^thm-113-2|§113.2]], [[§113 Surface Integrals#^def-113-5|Def. §113.5]]

> [!remark] Remark: Method — Computing a Flux Integral
> 1. **Parametrize $S$** (graph, cylindrical or spherical coordinates, plane) and find the parameter domain $D$. For a closed or piecewise-smooth surface, list the pieces.
> 2. **Compute the normal** $\mathbf{r}_u \times \mathbf{r}_v$ (for a graph $z = g$, simply $\langle -g_x, -g_y, 1 \rangle$).
> 3. **Check the orientation** at one convenient point: upward or downward, outward or inward (closed surfaces: outward, Definition §113.6). If it is wrong, change the sign.
> 4. **Substitute** the parametrization into $\mathbf{F}$, dot with the normal, and integrate over $D$ (Formula 9 or 10). For a vertical normal on a horizontal piece, $\mathbf{F} \cdot (\pm\mathbf{k}) = \pm R$; for a sphere of radius $a$, the unit normal is $\mathbf{x}/a$.
> 5. **Look for shortcuts**: if $S$ is closed, the Divergence Theorem ([[§115 The Divergence Theorem#^thm-115-1|Theorem §115.1]]) may be easier; if $\mathbf{F}$ is a curl, Stokes' Theorem ([[§114 Stokes' Theorem#^thm-114-1|Theorem §114.1]]) lets you change the surface.

^rem-113-2

> [!example] Example §113.3: Two Integrals over the Unit Sphere
> Let $S$ be the unit sphere $x^2 + y^2 + z^2 = 1$, parametrized as in [[§112 Parametric Surfaces and Their Areas#^ex-112-4|Example §112.4]] with $a = 1$: $\mathbf{r}(\phi, \theta) = \sin\phi\cos\theta\,\mathbf{i} + \sin\phi\sin\theta\,\mathbf{j} + \cos\phi\,\mathbf{k}$, $0 \le \phi \le \pi$, $0 \le \theta \le 2\pi$, with $|\mathbf{r}_\phi \times \mathbf{r}_\theta| = \sin\phi$.
>
> **(a) A scalar integral: $\iint_S x^2\,dS$.** By Formula 2,
>
> $$
> \begin{aligned}
> \iint_S x^2\,dS &= \int_0^{2\pi} \int_0^{\pi} (\sin\phi\cos\theta)^2 \sin\phi\,d\phi\,d\theta = \int_0^{2\pi} \cos^2\theta\,d\theta \int_0^{\pi} \sin^3\phi\,d\phi \\
> &= \int_0^{2\pi} \tfrac12(1 + \cos 2\theta)\,d\theta \int_0^{\pi} (\sin\phi - \sin\phi\cos^2\phi)\,d\phi = \tfrac12\Big[\theta + \tfrac12\sin 2\theta\Big]_0^{2\pi} \Big[-\cos\phi + \tfrac13\cos^3\phi\Big]_0^{\pi} = \pi \cdot \frac43 = \frac{4\pi}{3} .
> \end{aligned}
> $$
>
> **(b) A flux: $\mathbf{F}(x, y, z) = z\,\mathbf{i} + y\,\mathbf{j} + x\,\mathbf{k}$ across $S$** (outward). Here $\mathbf{F}(\mathbf{r}(\phi, \theta)) = \cos\phi\,\mathbf{i} + \sin\phi\sin\theta\,\mathbf{j} + \sin\phi\cos\theta\,\mathbf{k}$, and $\mathbf{r}_\phi \times \mathbf{r}_\theta = \sin^2\phi\cos\theta\,\mathbf{i} + \sin^2\phi\sin\theta\,\mathbf{j} + \sin\phi\cos\phi\,\mathbf{k}$, which is $\sin\phi$ times the position vector and so points outward. Then
>
> $$
> \mathbf{F}(\mathbf{r}(\phi, \theta)) \cdot (\mathbf{r}_\phi \times \mathbf{r}_\theta) = \cos\phi\sin^2\phi\cos\theta + \sin^3\phi\sin^2\theta + \sin^2\phi\cos\phi\cos\theta ,
> $$
>
> and by Formula 9
>
> $$
> \begin{aligned}
> \iint_S \mathbf{F} \cdot d\mathbf{S} &= \int_0^{2\pi} \int_0^{\pi} \big(2\sin^2\phi\cos\phi\cos\theta + \sin^3\phi\sin^2\theta\big)\,d\phi\,d\theta \\
> &= 2\int_0^{\pi} \sin^2\phi\cos\phi\,d\phi \int_0^{2\pi} \cos\theta\,d\theta + \int_0^{\pi} \sin^3\phi\,d\phi \int_0^{2\pi} \sin^2\theta\,d\theta = 0 + \frac43 \cdot \pi = \frac{4\pi}{3} ,
> \end{aligned}
> $$
>
> using $\int_0^{2\pi} \cos\theta\,d\theta = 0$ and the integrals of part (a). If $\mathbf{F}$ is the velocity field of a fluid with density $1$, the answer is the rate of flow through the sphere in units of mass per unit time. (The Divergence Theorem gets this in one line: [[§115 The Divergence Theorem#^rem-115-1|§115, Remark: Two Fluxes in One Line]].)
>
> *Stewart: Examples 16.7.1 and 16.7.4*

^ex-113-3

> [!example] Example §113.4: Flux out of a Closed Surface
> Evaluate $\iint_S \mathbf{F} \cdot d\mathbf{S}$, where $\mathbf{F}(x, y, z) = y\,\mathbf{i} + x\,\mathbf{j} + z\,\mathbf{k}$ and $S$ is the boundary of the solid region $E$ enclosed by the paraboloid $z = 1 - x^2 - y^2$ and the plane $z = 0$.
>
> $S$ consists of a parabolic top $S_1$ and a circular bottom $S_2$. Since $S$ is closed, use the positive (outward) orientation: $S_1$ is oriented upward and $S_2$ downward.
>
> **Top.** $S_1$ is the graph of $g(x, y) = 1 - x^2 - y^2$ over the disk $D$: $x^2 + y^2 \le 1$, with $g_x = -2x$, $g_y = -2y$. With $P = y$, $Q = x$, $R = z = 1 - x^2 - y^2$, Formula 10 gives
>
> $$
> \begin{aligned}
> \iint_{S_1} \mathbf{F} \cdot d\mathbf{S} &= \iint_D \big[ -y(-2x) - x(-2y) + 1 - x^2 - y^2 \big]\,dA = \iint_D (1 + 4xy - x^2 - y^2)\,dA \\
> &= \int_0^{2\pi} \int_0^1 (1 + 4r^2\cos\theta\sin\theta - r^2)\,r\,dr\,d\theta = \int_0^{2\pi} \left( \tfrac14 + \cos\theta\sin\theta \right) d\theta = \tfrac14(2\pi) + 0 = \frac{\pi}{2} .
> \end{aligned}
> $$
>
> **Bottom.** $S_2$ is oriented downward, $\mathbf{n} = -\mathbf{k}$, and $z = 0$ on $S_2$:
>
> $$
> \iint_{S_2} \mathbf{F} \cdot d\mathbf{S} = \iint_{S_2} \mathbf{F} \cdot (-\mathbf{k})\,dS = \iint_D (-z)\,dA = \iint_D 0\,dA = 0 .
> $$
>
> **Total.** $\iint_S \mathbf{F} \cdot d\mathbf{S} = \dfrac{\pi}{2} + 0 = \dfrac{\pi}{2}$.
>
> *Stewart: Example 16.7.5*

^ex-113-4

![[m233-113-1.svg]]
*Example §113.4 in cross-section (the plane $y = 0$). The closed surface $S$ bounds the solid $E$ under the paraboloid. With the positive orientation every normal points out of $E$: up and outward on the cap $S_1$ (the upward normal $\langle 2x, 2y, 1 \rangle$ of Formula 10), straight down on the base $S_2$, which is why the base gets the sign $-1$.*

> [!example] Example §113.5: Flux through a Cone, Downward
> Evaluate $\iint_S \mathbf{F} \cdot d\mathbf{S}$, where $\mathbf{F} = \langle -x, -y, z^3 \rangle$ and $S$ is the part of the cone $z = \sqrt{x^2 + y^2}$ between the planes $z = 1$ and $z = 3$, with downward orientation.
>
> $S$ is the graph of $g(x, y) = \sqrt{x^2 + y^2}$ over the annulus $D$: $1 \le x^2 + y^2 \le 9$. The upward normal is
>
> $$
> \mathbf{r}_x \times \mathbf{r}_y = \langle -g_x, -g_y, 1 \rangle = \left\langle \frac{-x}{\sqrt{x^2 + y^2}},\ \frac{-y}{\sqrt{x^2 + y^2}},\ 1 \right\rangle ,
> $$
>
> which points up and in, toward the axis of the cone. The downward orientation uses its negative, $\left\langle \dfrac{x}{\sqrt{x^2 + y^2}}, \dfrac{y}{\sqrt{x^2 + y^2}}, -1 \right\rangle$. On $S$, $z^3 = (x^2 + y^2)^{3/2}$, so
>
> $$
> \mathbf{F} \cdot \left\langle \frac{x}{\sqrt{x^2 + y^2}}, \frac{y}{\sqrt{x^2 + y^2}}, -1 \right\rangle = \frac{-x^2 - y^2}{\sqrt{x^2 + y^2}} - (x^2 + y^2)^{3/2} = -\sqrt{x^2 + y^2} - (x^2 + y^2)^{3/2} .
> $$
>
> In polar coordinates ($\sqrt{x^2 + y^2} = r$),
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = -\int_0^{2\pi} \int_1^3 (r + r^3)\,r\,dr\,d\theta = -2\pi \left[ \frac{r^3}{3} + \frac{r^5}{5} \right]_1^3 = -2\pi \left( \frac{26}{3} + \frac{242}{5} \right) = -\frac{1712\pi}{15} .
> $$
>
> (The posted solution also sketches a second route: close $S$ with the disks at $z = 1$ and $z = 3$, apply the Divergence Theorem, and subtract the fluxes through the disks.)
>
> *Source: 233 Practice Final Set 1, Part II Q5*

^ex-113-5

> [!definition] Definition §113.8: Electric Flux
> If $\mathbf{E}$ is an electric field ([[§107 Vector Fields#^ex-107-2|Example §107.2]]), the surface integral $\iint_S \mathbf{E} \cdot d\mathbf{S}$ is called the **electric flux** of $\mathbf{E}$ through $S$. **Gauss's Law** of electrostatics says that the net charge enclosed by a closed surface $S$ is
>
> $$
> Q = \varepsilon_0 \iint_S \mathbf{E} \cdot d\mathbf{S} , \qquad (11)
> $$
>
> where $\varepsilon_0$ is the permittivity of free space ($\varepsilon_0 \approx 8.8542 \times 10^{-12}\ \mathrm{C^2/N \cdot m^2}$ in SI units).
>
> *Stewart: 16.7, Equation 11 and text*

^def-113-8

> [!definition] Definition §113.9: Heat Flow
> If the temperature at a point $(x, y, z)$ of a body is $u(x, y, z)$, the **heat flow** is the vector field $\mathbf{F} = -K\nabla u$, where the experimentally determined constant $K$ is the **conductivity** of the substance. The rate of heat flow across a surface $S$ in the body is $\iint_S \mathbf{F} \cdot d\mathbf{S} = -K\iint_S \nabla u \cdot d\mathbf{S}$.
>
> *Stewart: 16.7, Equation 11 and text*

^def-113-new3

For example, if the field of [[§113 Surface Integrals#^ex-113-3|Example §113.3(b)]] were an electric field, the charge enclosed by the unit sphere would be $Q = \frac43\pi\varepsilon_0$. And if the temperature in a metal ball is $u = C(x^2 + y^2 + z^2)$, then on the sphere $x^2 + y^2 + z^2 = a^2$, with outward normal $\mathbf{n} = \frac1a\langle x, y, z \rangle$, $\mathbf{F} \cdot \mathbf{n} = -KC\langle 2x, 2y, 2z \rangle \cdot \frac1a\langle x, y, z \rangle = -2aKC$, so the rate of heat flow across the sphere is $-2aKC \cdot 4\pi a^2 = -8KC\pi a^3$ (Stewart, Example 16.7.6).
