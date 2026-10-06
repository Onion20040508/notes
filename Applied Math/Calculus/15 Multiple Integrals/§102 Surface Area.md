---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 102
stewart: "15.5"
aliases: ["Stewart 15.5"]
tags: [calculus, math233]
---
← [[§101 Applications of Double Integrals]] · ↑ [[· 15 Multiple Integrals]] · [[§103 Triple Integrals]] →

*Stewart, Section 15.5 · MATH 233 (UMass, Spring 2023): Practice Exam 2 (Q4), Exam 2 Practice Questions (Q13).*

The area of a surface $z = f(x, y)$ is computed like arc length one dimension down. Over a small rectangle of area $\Delta A$, the surface is close to its tangent plane, and the piece of tangent plane above the rectangle is a parallelogram whose area, by the cross product, is $\sqrt{f_x^2 + f_y^2 + 1}\,\Delta A$. Adding and taking the limit gives surface area as a double integral. Surfaces of revolution were handled with single integrals in [[§53 Area of a Surface of Revolution|§53]]; general parametric surfaces come in [[§112 Parametric Surfaces and Their Areas|§112]], where the formula of this section reappears as a special case ([[§112 Parametric Surfaces and Their Areas#^thm-112-2|Theorem §112.2]]; Stewart notes that this section may be omitted if 16.6 is covered).

## The Surface Area of a Graph

> [!definition] Definition §102.1: Surface Area
> Let $S$ be the surface with equation $z = f(x, y)$, where $f$ has continuous partial derivatives; for the derivation assume $f(x, y) \ge 0$ and that the domain $D$ of $f$ is a rectangle. Divide $D$ into small rectangles $R_{ij}$ of area $\Delta A = \Delta x\,\Delta y$. If $(x_i, y_j)$ is the corner of $R_{ij}$ closest to the origin, let $P_{ij}(x_i, y_j, f(x_i, y_j))$ be the point of $S$ directly above it. The tangent plane to $S$ at $P_{ij}$ approximates $S$ near $P_{ij}$, so the area $\Delta T_{ij}$ of the part of this tangent plane (a parallelogram) that lies directly above $R_{ij}$ approximates the area $\Delta S_{ij}$ of the part of $S$ directly above $R_{ij}$. The **surface area** of $S$ is defined to be
>
> $$
> A(S) = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n \Delta T_{ij} . \qquad (1)
> $$
>
> *Stewart: 15.5, Equation 1*

^def-102-1

> [!theorem] Theorem §102.1: The Surface Area Formula
> The area of the surface with equation $z = f(x, y)$, $(x, y) \in D$, where $f_x$ and $f_y$ are continuous, is
>
> $$
> A(S) = \iint_D \sqrt{[f_x(x, y)]^2 + [f_y(x, y)]^2 + 1}\,dA . \qquad (2)
> $$
>
> In Leibniz notation,
>
> $$
> A(S) = \iint_D \sqrt{1 + \Big( \frac{\partial z}{\partial x} \Big)^2 + \Big( \frac{\partial z}{\partial y} \Big)^2}\,dA . \qquad (3)
> $$
>
> *Stewart: 15.5, Formulas 2 and 3*

^thm-102-1

> [!proof]+ Proof
> **The area of one parallelogram.** Let $\mathbf a$ and $\mathbf b$ be the vectors that start at $P_{ij}$ and lie along the sides of the parallelogram of area $\Delta T_{ij}$; they lie above the sides of $R_{ij}$ of lengths $\Delta x$ and $\Delta y$. The numbers $f_x(x_i, y_j)$ and $f_y(x_i, y_j)$ are the slopes of the tangent lines through $P_{ij}$ in the directions of $\mathbf a$ and $\mathbf b$ ([[§92 Partial Derivatives#^rem-92-1|§92, Remark: Partial Derivatives as Slopes]]), so going $\Delta x$ in the $x$-direction along the tangent plane raises $z$ by $f_x(x_i, y_j)\,\Delta x$, and similarly in the $y$-direction:
>
> $$
> \mathbf a = \Delta x\,\mathbf i + f_x(x_i, y_j)\,\Delta x\,\mathbf k , \qquad \mathbf b = \Delta y\,\mathbf j + f_y(x_i, y_j)\,\Delta y\,\mathbf k .
> $$
>
> The area of the parallelogram is $\Delta T_{ij} = |\mathbf a \times \mathbf b|$ ([[§83 The Cross Product#^cor-83-6|Corollary §83.6]]), and
>
> $$
> \mathbf a \times \mathbf b = \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\ \Delta x & 0 & f_x(x_i, y_j)\,\Delta x \\ 0 & \Delta y & f_y(x_i, y_j)\,\Delta y \end{vmatrix}
> = -f_x(x_i, y_j)\,\Delta x\,\Delta y\,\mathbf i - f_y(x_i, y_j)\,\Delta x\,\Delta y\,\mathbf j + \Delta x\,\Delta y\,\mathbf k
> = \big[ -f_x(x_i, y_j)\,\mathbf i - f_y(x_i, y_j)\,\mathbf j + \mathbf k \big]\,\Delta A .
> $$
>
> Thus
>
> $$
> \Delta T_{ij} = |\mathbf a \times \mathbf b| = \sqrt{[f_x(x_i, y_j)]^2 + [f_y(x_i, y_j)]^2 + 1}\,\Delta A .
> $$
>
> **The limit.** By [[§102 Surface Area#^def-102-1|Definition §102.1]],
>
> $$
> A(S) = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n \sqrt{[f_x(x_i, y_j)]^2 + [f_y(x_i, y_j)]^2 + 1}\,\Delta A .
> $$
>
> This is the limit of double Riemann sums of the continuous function $\sqrt{f_x^2 + f_y^2 + 1}$ (with the corners $(x_i, y_j)$ as sample points), so by [[§98 Double Integrals Over Rectangles#^def-98-2|Definition §98.2]] and [[§98 Double Integrals Over Rectangles#^thm-98-1|Theorem §98.1]] it is the double integral (2). (Stewart's derivation assumes $D$ is a rectangle; Formula 2 is then used for general regions $D$, where the double integral is that of [[§99 Double Integrals Over General Regions#^def-99-1|Definition §99.1]].)

^pf-102-1

*Uses:* [[§102 Surface Area#^def-102-1|Def. §102.1]], [[§83 The Cross Product#^cor-83-6|§83.6]] (area of a parallelogram), [[§92 Partial Derivatives#^rem-92-1|§92, Remark]] (partial derivatives as slopes), [[§98 Double Integrals Over Rectangles#^def-98-2|Def. §98.2]], [[§98 Double Integrals Over Rectangles#^thm-98-1|§98.1]], [[§99 Double Integrals Over General Regions#^def-99-1|Def. §99.1]] (general regions)

![[m233-102-1.svg]]
*The tangent parallelogram of [[§102 Surface Area#^def-102-1|Definition §102.1]]. Above the small rectangle $R_{ij}$ (green) the surface $S$ (blue) is approximated by the piece of its tangent plane at $P_{ij}$ (red), spanned by $\mathbf a = \langle \Delta x, 0, f_x\Delta x \rangle$ and $\mathbf b = \langle 0, \Delta y, f_y\Delta y \rangle$. Its area $|\mathbf a \times \mathbf b| = \sqrt{f_x^2 + f_y^2 + 1}\,\Delta A$ exceeds $\Delta A$ by the factor that measures how steeply the surface is tilted.*

> [!remark]- Connections
> - Rigorous treatment for parametrized surfaces: [[§18 Surface Integrals#^thm-18-1|452 Thm. §18.1]] (area element $\sqrt{\det G}\,du\,dv = |\mathbf X_u \times \mathbf X_v|\,du\,dv$); Formula 2 is the case $\mathbf X(x, y) = (x, y, f(x, y))$, with $\mathbf X_x \times \mathbf X_y = \langle -f_x, -f_y, 1 \rangle$. Hub: [[Surface Area via the Gram Matrix]].

> [!remark] Remark: Comparison with Arc Length
> Formula 3 is the analogue of the arc length formula $L = \int_a^b \sqrt{1 + (dy/dx)^2}\,dx$ ([[§52 Arc Length#^thm-52-1|Theorem §52.1]]): in both, the square root of $1$ plus the squared slopes is the factor by which the graph stretches the length or area of the domain. In particular $A(S) \ge A(D)$, with equality exactly when $S$ is horizontal ($f_x = f_y = 0$). For a plane $z = ax + by + c$ the factor is the constant $\sqrt{a^2 + b^2 + 1}$, so $A(S) = \sqrt{a^2 + b^2 + 1}\,A(D)$ (Stewart's Exercise 15.5.23). Stewart verifies in 16.6 ([[§112 Parametric Surfaces and Their Areas#^thm-112-3|Theorem §112.3]]) that Formula 2 is consistent with the area of a surface of revolution, [[§53 Area of a Surface of Revolution#^def-53-2|Definition §53.2]].

^rem-102-1

## Examples

> [!example] Example §102.1: A Surface over a Triangle
> Find the surface area of the part of the surface $z = x^2 + 2y + 2$ that lies above the triangular region $T$ in the $xy$-plane with vertices $(0, 0)$, $(1, 0)$ and $(1, 1)$.
>
> $T = \{(x, y) \mid 0 \le x \le 1,\ 0 \le y \le x\}$, and $f(x, y) = x^2 + 2y + 2$ has $f_x = 2x$, $f_y = 2$. By Formula 2,
>
> $$
> A = \iint_T \sqrt{(2x)^2 + (2)^2 + 1}\,dA = \int_0^1 \int_0^x \sqrt{4x^2 + 5}\,dy\,dx = \int_0^1 x\sqrt{4x^2 + 5}\,dx = \frac18 \cdot \frac23 (4x^2 + 5)^{3/2} \Big]_0^1 = \frac{1}{12}\big( 27 - 5\sqrt5 \big) .
> $$
>
> Integrating $dy$ first produced the factor $x$ that makes $\int x\sqrt{4x^2 + 5}\,dx$ a substitution ($u = 4x^2 + 5$).
>
> *Stewart: Example 15.5.1*

^ex-102-1

> [!example] Example §102.2: A Paraboloid Cut Off by a Plane
> Find the area of the part of the paraboloid $z = x^2 + y^2$ that lies under the plane $z = 9$.
>
> The plane meets the paraboloid in the circle $x^2 + y^2 = 9$, $z = 9$, so the surface lies above the disk $D$ with center the origin and radius $3$. By Formula 3,
>
> $$
> A = \iint_D \sqrt{1 + (2x)^2 + (2y)^2}\,dA = \iint_D \sqrt{1 + 4(x^2 + y^2)}\,dA .
> $$
>
> In polar coordinates ([[§100 Double Integrals in Polar Coordinates#^thm-100-1|Theorem §100.1]]),
>
> $$
> A = \int_0^{2\pi} \int_0^3 \sqrt{1 + 4r^2}\,r\,dr\,d\theta = \int_0^{2\pi} d\theta \int_0^3 \tfrac18 \sqrt{1 + 4r^2}\,(8r)\,dr = 2\pi \cdot \tfrac18 \cdot \tfrac23 (1 + 4r^2)^{3/2} \Big]_0^3 = \frac{\pi}{6}\big( 37\sqrt{37} - 1 \big) .
> $$
>
> *Stewart: Example 15.5.2*

^ex-102-2

*Chain: the same paraboloid later in [[§112 Parametric Surfaces and Their Areas#^ex-112-5|Chapter 16]].*

> [!example] Example §102.3: A Surface over a Region Bounded by a Quintic
> Find the surface area of the part of the graph of $z = 3 + 2y + x^4/4$ that lies over the region $R$ in the $xy$-plane bounded by $y = x^5$, $x = 1$ and the $x$-axis.
>
> $R = \{0 \le x \le 1,\ 0 \le y \le x^5\}$, and $z_x = x^3$, $z_y = 2$, so $\sqrt{1 + z_x^2 + z_y^2} = \sqrt{5 + x^6}$. Then
>
> $$
> A = \int_0^1 \int_0^{x^5} \sqrt{5 + x^6}\,dy\,dx = \int_0^1 x^5\sqrt{5 + x^6}\,dx = \int_5^6 \tfrac16 \sqrt u\,du = \frac16 \cdot \frac23 \Big[ u^{3/2} \Big]_5^6 = \frac{6^{3/2} - 5^{3/2}}{9} ,
> $$
>
> with $u = 5 + x^6$, $du = 6x^5\,dx$. Again the order $dy\,dx$ supplies the factor $x^5$ that the substitution needs.
>
> *Source: 233 Practice Exam 2, Q4*

^ex-102-3

> [!example] Example §102.4: A Cone over a Sector
> Let $D$ be the portion of the unit disk that lies above the line $y = -x$ and below the line $y = x$, where $x \ge 0$. Find the area of the part of the surface $z = \sqrt{x^2 + y^2}$ that lies above $D$.
>
> **The integrand.** With $f(x, y) = \sqrt{x^2 + y^2}$,
>
> $$
> f_x = \frac{x}{\sqrt{x^2 + y^2}} , \qquad f_y = \frac{y}{\sqrt{x^2 + y^2}} , \qquad f_x^2 + f_y^2 = \frac{x^2 + y^2}{x^2 + y^2} = 1 ,
> $$
>
> so $\sqrt{f_x^2 + f_y^2 + 1} = \sqrt2$ everywhere except at the origin, where $f$ is not differentiable (a single point does not affect the integral). The cone makes a constant angle of $45^\circ$ with the $xy$-plane, and every area element is stretched by the factor $\sqrt2$.
>
> **The region.** $D$ is the sector $-\pi/4 \le \theta \le \pi/4$, $0 \le r \le 1$, a quarter of the unit disk, with area $\pi/4$. So
>
> $$
> A = \iint_D \sqrt2\,dA = \sqrt2 \cdot A(D) = \frac{\sqrt2}{4}\pi .
> $$
>
> *Source: 233 Exam 2 Practice Questions, Q13*

^ex-102-4
