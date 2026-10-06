---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 134
stewart: "16.7"
aliases: ["Stewart 16.7"]
tags: [calculus, math233]
---
← [[§133 Parametric Surfaces and Their Areas]] · ↑ [[· 16 Vector Calculus]] · [[§135 Oriented Surfaces and Flux]] →

*Stewart, Section 16.7 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q4), Practice Final Exam (Q5), Practice Final Set 1 (Part II, Q5).*

Surface integrals are to surface area what line integrals are to arc length. The surface integral of a scalar function, $\iint_S f\,dS$, weights each patch of $S$ by its area; it is computed as a double integral over the parameter domain with the area factor $|\mathbf{r}_u \times \mathbf{r}_v|$ of [[§133 Parametric Surfaces and Their Areas#^def-133-6|Definition §133.6]]. The surface integral of a vector field, $\iint_S \mathbf{F} \cdot d\mathbf{S}$, is the flux of $\mathbf{F}$ across $S$: the integral of its normal component, which measures the rate of flow through $S$. Flux needs a choice of normal direction, an orientation, and its sign depends on that choice; the convention for closed surfaces is the outward normal. These integrals are one side of Stokes' Theorem and of the Divergence Theorem.

## Surface Integrals of Scalar Functions

Let $S$ have vector equation $\mathbf{r}(u, v) = x(u, v)\,\mathbf{i} + y(u, v)\,\mathbf{j} + z(u, v)\,\mathbf{k}$, $(u, v) \in D$. Suppose first that $D$ is a rectangle, divided into subrectangles $R_{ij}$ with dimensions $\Delta u$ and $\Delta v$; then $S$ is divided into corresponding patches $S_{ij}$. Evaluate $f$ at a point $P_{ij}^*$ in each patch, multiply by the area $\Delta S_{ij}$ of the patch, and sum.

> [!definition] Definition §134.1: Surface Integral of a Function
> The **surface integral of $f$ over the surface $S$** is
>
> $$
> \iint_S f(x, y, z)\,dS = \lim_{m, n \to \infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(P_{ij}^*)\,\Delta S_{ij} . \qquad (1)
> $$
>
> (Compare the line integral, [[§126 Line Integrals#^def-126-1|Definition §126.1]], and the double integral, [[§115 Double Integrals Over Rectangles#^def-115-2|Definition §115.2]].)
>
> *Stewart: 16.7, Equation 1*

^def-134-1

> [!theorem] Theorem §134.1: Evaluating a Surface Integral
> If the components of $\mathbf{r}$ are continuous, $\mathbf{r}_u$ and $\mathbf{r}_v$ are nonzero and nonparallel in the interior of $D$, and $S$ is covered only once as $(u, v)$ ranges throughout $D$, then (even when $D$ is not a rectangle)
>
> $$
> \iint_S f(x, y, z)\,dS = \iint_D f(\mathbf{r}(u, v))\,|\mathbf{r}_u \times \mathbf{r}_v|\,dA . \qquad (2)
> $$
>
> The value does not depend on the parametrization used. In particular $\iint_S 1\,dS = \iint_D |\mathbf{r}_u \times \mathbf{r}_v|\,dA = A(S)$.
>
> *Stewart: 16.7, Equation 2*

^thm-134-1

*Stewart only motivates Formula 2 ("it can be shown from Definition 1"): the patch area is approximated by $\Delta S_{ij} \approx |\mathbf{r}_u \times \mathbf{r}_v|\,\Delta u\,\Delta v$, as in [[§133 Parametric Surfaces and Their Areas#^rem-133-1|the surface area argument]]. 452 takes Formula 2 as the definition, with the area element derived from the Gram matrix: [[§31 Surface Integrals#^def-31-5|452 Def. §31.5]], [[§31 Surface Integrals#^thm-31-1|452 Thm. §31.1]].*

> [!remark]- Connections
> - The scalar surface integral in 452: [[§31 Surface Integrals#^def-31-5|452 Def. §31.5]], with the table comparing it to the scalar line integral $\int_\gamma f\,ds = \int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt$. Neither is the integral of a differential form, since neither sees orientation: [[§38 The Exterior Derivative#^rem-38-8|452 Remark: Scalar Integrals Are Not Form Integrals]].

To use Formula 2, evaluate $f(\mathbf{r}(u, v))$ by writing $x = x(u, v)$, $y = y(u, v)$, $z = z(u, v)$ in the formula for $f(x, y, z)$.

> [!example] Example §134.1: A Parallelogram
> Let $S$ be the parallelogram parametrized by $\mathbf{r}(u, v) = \langle u + v,\ u - v,\ 1 + 2u + v \rangle$, $0 \le u \le 2$, $0 \le v \le 1$. Compute $\iint_S (x + y + z)\,dS$.
>
> $S$ is a piece of a plane, as in [[§133 Parametric Surfaces and Their Areas#^ex-133-1|Example §133.1]], with $\mathbf{r}_u = \langle 1, 1, 2 \rangle$ and $\mathbf{r}_v = \langle 1, -1, 1 \rangle$. Then
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

^ex-134-1

> [!definition] Definition §134.2: Mass of a Thin Sheet
> If a thin sheet (say, of aluminum foil) has the shape of a surface $S$ and density (mass per unit area) $\rho(x, y, z)$ at $(x, y, z)$, its total **mass** is
>
> $$
> m = \iint_S \rho(x, y, z)\,dS ,
> $$
>
> *Stewart: 16.7 (text)*

^def-134-2

> [!definition] Definition §134.3: Center of Mass of a Thin Sheet
> For a thin sheet with the shape of a surface $S$, density $\rho(x, y, z)$ and mass $m$ ([[§134 Surface Integrals#^def-134-2|Definition §134.2]]), its **center of mass** is $(\bar{x}, \bar{y}, \bar{z})$, where
>
> $$
> \bar{x} = \frac1m \iint_S x\,\rho(x, y, z)\,dS, \qquad \bar{y} = \frac1m \iint_S y\,\rho(x, y, z)\,dS, \qquad \bar{z} = \frac1m \iint_S z\,\rho(x, y, z)\,dS .
> $$
>
> *Stewart: 16.7 (text)*

^def-134-3

> [!theorem] Theorem §134.2: Surface Integrals over Graphs
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

^thm-134-2

> [!proof]+ Proof
> Regard $S$ as a parametric surface with parametric equations $x = x$, $y = y$, $z = g(x, y)$. Then $\mathbf{r}_x = \mathbf{i} + (\partial g/\partial x)\,\mathbf{k}$ and $\mathbf{r}_y = \mathbf{j} + (\partial g/\partial y)\,\mathbf{k}$, and their cross product is (3), with length $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}$ (the computation of [[§133 Parametric Surfaces and Their Areas#^thm-133-2|Theorem §133.2]]). Substituting into Formula 2 gives (4). For $y = h(x, z)$, use the parameters $x$ and $z$ in the same way: $\mathbf{r}_x = \mathbf{i} + h_x\,\mathbf{j}$, $\mathbf{r}_z = h_z\,\mathbf{j} + \mathbf{k}$, and $|\mathbf{r}_x \times \mathbf{r}_z| = |\langle h_x, -1, h_z \rangle| = \sqrt{h_x^2 + h_z^2 + 1}$.

^pf-134-2

*Uses:* [[§134 Surface Integrals#^thm-134-1|§134.1]], [[§133 Parametric Surfaces and Their Areas#^thm-133-2|§133.2]], [[§133 Parametric Surfaces and Their Areas#^prop-133-1|§133.1]]

For example, for $S$: $z = x + y^2$, $0 \le x \le 1$, $0 \le y \le 2$, Formula 4 gives $\iint_S y\,dS = \int_0^1 \int_0^2 y\sqrt{1 + 1 + 4y^2}\,dy\,dx = \sqrt2 \int_0^2 y\sqrt{1 + 2y^2}\,dy = \sqrt2 \cdot \frac14 \cdot \frac23 (1 + 2y^2)^{3/2} \Big]_0^2 = \frac{13\sqrt2}{3}$ (Stewart, Example 16.7.2).

> [!definition] Definition §134.4: Piecewise-Smooth Surface
> A **piecewise-smooth surface** $S$ is a finite union of smooth surfaces $S_1, S_2, \ldots, S_n$ that intersect only along their boundaries. The surface integral of $f$ over $S$ is
>
> $$
> \iint_S f(x, y, z)\,dS = \iint_{S_1} f(x, y, z)\,dS + \cdots + \iint_{S_n} f(x, y, z)\,dS .
> $$
>
> *Stewart: 16.7 (text)*

^def-134-4

For instance, if $S$ consists of the cylinder $x^2 + y^2 = 1$ (sides $S_1$), the unit disk in the plane $z = 0$ (bottom $S_2$) and the part of the plane $z = 1 + x$ above it (top $S_3$), then $\iint_{S_1} z\,dS = \frac{3\pi}{2}$ (parametrize by $\theta$ and $z$, $0 \le z \le 1 + \cos\theta$, with $|\mathbf{r}_\theta \times \mathbf{r}_z| = 1$), $\iint_{S_2} z\,dS = 0$, and $\iint_{S_3} z\,dS = \sqrt2\,\pi$ (Formula 4), so $\iint_S z\,dS = \left(\frac32 + \sqrt2\right)\pi$ (Stewart, Example 16.7.3).

*The section continues in [[§135 Oriented Surfaces and Flux]].*
