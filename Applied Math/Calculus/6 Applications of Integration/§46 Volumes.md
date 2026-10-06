---
type: section
subject: "[[Calculus]]"
chapter: 6
section: 46
stewart: "6.2"
aliases: ["Stewart 6.2"]
tags: [calculus]
---
← [[§45 Areas Between Curves]] · ↑ [[· 6 Applications of Integration]] · [[§47 Volumes by Cylindrical Shells]] →

*Stewart, Section 6.2.*

Volume is handled like area. Cut the solid by parallel planes into thin slabs, approximate each slab by a cylinder whose base is the cross-section, add the volumes, and take the limit. The result is the slicing formula $V = \int_a^b A(x)\,dx$, where $A(x)$ is the area of the cross-section at $x$. For a solid of revolution the cross-sections are disks or washers, so $A(x)$ is $\pi(\text{radius})^2$ or a difference of two such terms. The same formula handles any solid whose cross-sections have a computable area: pyramids, wedges, solids built on a given base.

## Definition of Volume

> [!definition] Definition §46.1: Cylinder
> A **cylinder** (more precisely, a *right cylinder*) is bounded by a plane region $B_1$, called the **base**, and a congruent region $B_2$ in a parallel plane; it consists of all points on line segments perpendicular to the base that join $B_1$ to $B_2$. If the base has area $A$ and the height (the distance from $B_1$ to $B_2$) is $h$, the **volume** of the cylinder is defined to be
>
> $$
> V = Ah .
> $$
>
> For a circular base of radius $r$ this is a circular cylinder, $V = \pi r^2 h$; for a rectangular base of length $l$ and width $w$, a rectangular box (rectangular parallelepiped), $V = lwh$.
>
> *Stewart: 6.2 (text)*

^def-46-1

For a solid $S$ that is not a cylinder, intersect $S$ with a plane: the plane region obtained is a **cross-section** of $S$. Let $A(x)$ be the area of the cross-section of $S$ in the plane $P_x$ perpendicular to the $x$-axis through the point $x$, $a \le x \le b$ (slice $S$ with a knife through $x$). Divide $S$ into $n$ slabs of equal width $\Delta x$ by the planes $P_{x_1}, P_{x_2}, \ldots$, like slices of a loaf of bread. With sample points $x_i^{\ast} \in [x_{i-1}, x_i]$, the $i$th slab $S_i$ (between $P_{x_{i-1}}$ and $P_{x_i}$) is approximately a cylinder with base area $A(x_i^{\ast})$ and height $\Delta x$, so

$$
V(S_i) \approx A(x_i^*)\,\Delta x \qquad\text{and}\qquad V \approx \sum_{i=1}^{n} A(x_i^*)\,\Delta x .
$$

The approximation improves as the slices get thinner, so the volume is *defined* as the limit, which is a definite integral.

> [!definition] Definition §46.2: Volume
> Let $S$ be a solid that lies between $x = a$ and $x = b$. If the cross-sectional area of $S$ in the plane $P_x$, through $x$ and perpendicular to the $x$-axis, is $A(x)$, where $A$ is a continuous function, then the **volume** of $S$ is
>
> $$
> V = \lim_{n \to \infty} \sum_{i=1}^{n} A(x_i^*)\,\Delta x = \int_a^b A(x)\,dx .
> $$
>
> Here $A(x)$ is the area of a *moving* cross-section, obtained by slicing through $x$ perpendicular to the $x$-axis.
>
> *Stewart: 6.2, Definition of Volume*

^def-46-2

For a cylinder the cross-sectional area is constant, $A(x) = A$, and [[§46 Volumes#^def-46-2|Definition §46.2]] gives $V = \int_a^b A\,dx = A(b - a)$, in agreement with $V = Ah$.

> [!remark]- Connections
> - Rigorous treatment: with volume defined as [[§11 Lebesgue Measurable Sets#^def-11-5|Lebesgue measure]], the slicing formula $m(E) = \int m(E_x)\,dx$ is the Cross-Section Theorem, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-4|551 Thm. §25.4]]. In this course it reappears as a double integral of the "height" ([[§115 Double Integrals Over Rectangles#^thm-115-2|Theorem §115.2]]) and as a triple integral computed by Fubini ([[§121 Applications of Triple Integrals#^thm-121-1|Theorem §121.1]]).

> [!theorem] Theorem §46.1: Volume Does Not Depend on the Slicing
> The volume given by [[§46 Volumes#^def-46-2|Definition §46.2]] is independent of how $S$ is situated with respect to the $x$-axis: no matter how we slice $S$ with parallel planes, we get the same value $V$.
>
> *Stewart: 6.2 (margin note)*

^thm-46-1

*Stewart omits the proof ("it can be proved"). Once volume is defined as Lebesgue measure, the slicing formula holds in every direction by [[§25 Invariance Properties and Fubini's Theorem#^thm-25-4|551 Thm. §25.4]], and the measure itself is unchanged by translations ([[§25 Invariance Properties and Fubini's Theorem#^thm-25-1|551 Thm. §25.1]]) and by rotations (a linear change of variables with $|\det| = 1$, [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]]).*

> [!example] Example §46.1: The Volume of a Sphere
> Show that the volume of a sphere of radius $r$ is $V = \frac43 \pi r^3$.
>
> Place the center at the origin. The plane $P_x$ ($-r \le x \le r$) cuts the sphere in a disk whose radius, by the Pythagorean Theorem, is $y = \sqrt{r^2 - x^2}$. So
>
> $$
> A(x) = \pi y^2 = \pi (r^2 - x^2) ,
> $$
>
> and by [[§46 Volumes#^def-46-2|Definition §46.2]], using that the integrand is even ([[§43 The Substitution Rule#^thm-43-4|Theorem §43.4]]),
>
> $$
> V = \int_{-r}^{r} \pi (r^2 - x^2)\,dx = 2\pi \int_0^r (r^2 - x^2)\,dx = 2\pi \Big[r^2 x - \frac{x^3}{3}\Big]_0^r = 2\pi \Big(r^3 - \frac{r^3}{3}\Big) = \frac43 \pi r^3 .
> $$
>
> For $r = 1$, $V = \frac43 \pi \approx 4.18879$. Here the slabs are circular cylinders, or **disks**. With midpoints $\bar x_i$ as sample points, the Riemann sums $\sum_{i=1}^{n} \pi(1 - \bar x_i^2)\,\Delta x$ give $\approx 4.2726$ with $5$ disks, $\approx 4.2097$ with $10$ and $\approx 4.1940$ with $20$, approaching the true volume.
>
> *Stewart: Example 6.2.1*

^ex-46-1

## Volumes of Solids of Revolution

> [!definition] Definition §46.3: Solid of Revolution
> If a plane region is revolved about a line, the resulting solid is a **solid of revolution**. Its cross-sections perpendicular to the axis of rotation are circular: disks, or washers (annular rings) if the solid has a hollow core around the axis.
>
> *Stewart: 6.2 (text)*

^def-46-3

> [!remark] Remark: Method — Disks and Washers
> Compute the volume of a solid of revolution with the defining formula
>
> $$
> V = \int_a^b A(x)\,dx \qquad\text{or}\qquad V = \int_c^d A(y)\,dy ,
> $$
>
> slicing perpendicular to the axis of rotation: integrate in $x$ for a horizontal axis and in $y$ for a vertical one.
> 1. **Disk.** If the cross-section is a disk, find its radius (in terms of $x$ or $y$) and use $A = \pi(\text{radius})^2$.
> 2. **Washer.** If it is a washer, find the inner radius $r_{\rm in}$ and the outer radius $r_{\rm out}$ from a sketch and subtract the inner disk from the outer one: $A = \pi(\text{outer radius})^2 - \pi(\text{inner radius})^2$.
> 3. **Radii about other axes.** A radius is a *distance to the axis*. For the axis $y = k$, a point at height $y$ is at distance $|k - y|$; for the axis $x = h$, a point at $x$ is at distance $|x - h|$.
> 4. **Check** the answer against a simple solid that contains or is contained in the given one.

^rem-46-1

> [!example] Example §46.2: Disks
> **(a)** Find the volume of the solid obtained by rotating about the $x$-axis the region under $y = \sqrt{x}$ from $0$ to $1$.
>
> Slicing through $x$ gives a disk of radius $\sqrt{x}$, with area $A(x) = \pi(\sqrt{x})^2 = \pi x$; the approximating cylinder (a disk of thickness $\Delta x$) has volume $\pi x\,\Delta x$. The solid lies between $x = 0$ and $x = 1$, so
>
> $$
> V = \int_0^1 \pi x\,dx = \pi \frac{x^2}{2} \Big]_0^1 = \frac{\pi}{2} .
> $$
>
> Check: rotating the square $[0, 1] \times [0, 1]$ instead gives a cylinder of radius $1$ and height $1$, with volume $\pi$. The given solid has half of that, which seems about right.
>
> **(b)** Find the volume of the solid obtained by rotating the region bounded by $y = x^3$, $y = 8$ and $x = 0$ about the $y$-axis.
>
> The axis is vertical, so slice perpendicular to the $y$-axis and integrate in $y$. At height $y$ the cross-section is a disk of radius $x = \sqrt[3]{y}$, so
>
> $$
> A(y) = \pi x^2 = \pi (\sqrt[3]{y})^2 = \pi y^{2/3} ,
> $$
>
> and since the solid lies between $y = 0$ and $y = 8$,
>
> $$
> V = \int_0^8 \pi y^{2/3}\,dy = \pi \Big[\tfrac35 y^{5/3}\Big]_0^8 = \pi \cdot \tfrac35 \cdot 32 = \frac{96\pi}{5} .
> $$
>
> *Stewart: Examples 6.2.2 and 6.2.3*

^ex-46-2

> [!example] Example §46.3: Washers About Three Axes
> The region $\mathcal{R}$ enclosed by $y = x$ and $y = x^2$ lies between their intersection points $(0, 0)$ and $(1, 1)$; on $[0, 1]$, $x \ge x^2$. Find the volume of the solid obtained by rotating $\mathcal{R}$ about (a) the $x$-axis, (b) the line $y = 2$, (c) the line $x = -1$.
>
> **(a)** The cross-section in the plane $P_x$ is a washer with inner radius $x^2$ and outer radius $x$:
>
> $$
> A(x) = \pi (x)^2 - \pi (x^2)^2 = \pi (x^2 - x^4), \qquad
> V = \int_0^1 \pi (x^2 - x^4)\,dx = \pi \Big[\frac{x^3}{3} - \frac{x^5}{5}\Big]_0^1 = \frac{2\pi}{15} .
> $$
>
> **(b)** Again a washer, but now the radii are distances to the line $y = 2$, which lies above $\mathcal{R}$: the inner radius is $2 - x$ (to the line $y = x$, the nearer curve) and the outer radius is $2 - x^2$. So
>
> $$
> \begin{aligned}
> V &= \int_0^1 \big[\pi (2 - x^2)^2 - \pi (2 - x)^2\big]\,dx = \pi \int_0^1 (x^4 - 5x^2 + 4x)\,dx \\
> &= \pi \Big[\frac{x^5}{5} - 5\,\frac{x^3}{3} + 4\,\frac{x^2}{2}\Big]_0^1 = \pi \Big(\frac15 - \frac53 + 2\Big) = \frac{8\pi}{15} ,
> \end{aligned}
> $$
>
> using $(2 - x^2)^2 - (2 - x)^2 = (4 - 4x^2 + x^4) - (4 - 4x + x^2) = x^4 - 5x^2 + 4x$.
>
> **(c)** The axis $x = -1$ is vertical, so slice horizontally. At height $y$ ($0 \le y \le 1$) the region runs from $x = y$ (on the line) to $x = \sqrt{y}$ (on the parabola), so the washer has inner radius $1 + y$ and outer radius $1 + \sqrt{y}$:
>
> $$
> \begin{aligned}
> V &= \int_0^1 \pi \big[(1 + \sqrt{y})^2 - (1 + y)^2\big]\,dy = \pi \int_0^1 \big(2\sqrt{y} - y - y^2\big)\,dy \\
> &= \pi \Big[\frac{4y^{3/2}}{3} - \frac{y^2}{2} - \frac{y^3}{3}\Big]_0^1 = \pi \Big(\frac43 - \frac12 - \frac13\Big) = \frac{\pi}{2} .
> \end{aligned}
> $$
>
> *Stewart: Examples 6.2.4, 6.2.5 and 6.2.6*

^ex-46-3

![[m233-40-1.svg]]
*[[§46 Volumes#^ex-46-3|Example §46.3]](b). (a) Rotating the red segment at $x$ about the line $y = 2$ sweeps out a washer. Its inner radius is the distance $2 - x$ from the axis to the nearer curve $y = x$, and its outer radius the distance $2 - x^2$ to the farther curve $y = x^2$. (b) The washer's area is the outer disk minus the inner disk.*

## Finding Volume Using Cross-Sectional Area

[[§46 Volumes#^def-46-2|Definition §46.2]] applies to any solid whose cross-sections have areas that are easy to compute, not only to solids of revolution.

> [!example] Example §46.4: Triangular Cross-Sections
> **(a)** A solid has a circular base of radius $1$, and its parallel cross-sections perpendicular to the base are equilateral triangles. Find its volume.
>
> Take the base to be the disk $x^2 + y^2 \le 1$ and slice perpendicular to the $x$-axis. At $x$ the cross-section is an equilateral triangle $ABC$ whose base $AB$ is the chord of the circle, with endpoint $B = (x, y)$, $y = \sqrt{1 - x^2}$. So $|AB| = 2y = 2\sqrt{1 - x^2}$, and an equilateral triangle with base $2y$ has height $\sqrt3\,y = \sqrt3 \sqrt{1 - x^2}$. Hence
>
> $$
> A(x) = \tfrac12 \cdot 2\sqrt{1 - x^2} \cdot \sqrt3 \sqrt{1 - x^2} = \sqrt3\,(1 - x^2) ,
> $$
>
> $$
> V = \int_{-1}^{1} \sqrt3\,(1 - x^2)\,dx = 2 \int_0^1 \sqrt3\,(1 - x^2)\,dx = 2\sqrt3 \Big[x - \frac{x^3}{3}\Big]_0^1 = \frac{4\sqrt3}{3} .
> $$
>
> **(b)** A wedge is cut out of a circular cylinder of radius $4$ by two planes. One is perpendicular to the axis of the cylinder; the other meets the first at an angle of $30°$ along a diameter of the cylinder. Find the volume of the wedge.
>
> Put the $x$-axis along the diameter where the planes meet. The base of the wedge is the half-disk $0 \le y \le \sqrt{16 - x^2}$, $-4 \le x \le 4$. The cross-section perpendicular to the $x$-axis at $x$ is a right triangle $ABC$ with base $y = \sqrt{16 - x^2}$ along the first plane and height $|BC| = y\tan 30° = \sqrt{16 - x^2}/\sqrt3$. So
>
> $$
> A(x) = \tfrac12 \sqrt{16 - x^2} \cdot \frac{1}{\sqrt3}\sqrt{16 - x^2} = \frac{16 - x^2}{2\sqrt3} ,
> $$
>
> $$
> V = \int_{-4}^{4} \frac{16 - x^2}{2\sqrt3}\,dx = \frac{1}{\sqrt3} \int_0^4 (16 - x^2)\,dx = \frac{1}{\sqrt3} \Big[16x - \frac{x^3}{3}\Big]_0^4 = \frac{1}{\sqrt3}\Big(64 - \frac{64}{3}\Big) = \frac{128}{3\sqrt3} .
> $$
>
> *Stewart: Examples 6.2.7 and 6.2.9*

^ex-46-4

> [!example] Example §46.5: The Volume of a Pyramid
> Find the volume of a pyramid whose base is a square with side $L$ and whose height is $h$.
>
> Put the vertex $O$ at the origin and the $x$-axis along the central axis, so the base lies in the plane $x = h$. The plane $P_x$ ($0 \le x \le h$) cuts the pyramid in a square of side $s$. By similar triangles,
>
> $$
> \frac{x}{h} = \frac{s/2}{L/2} = \frac{s}{L}, \qquad\text{so}\qquad s = \frac{Lx}{h}
> $$
>
> (equivalently: the edge line $OP$ has slope $L/(2h)$, so its equation is $y = Lx/(2h)$). Therefore $A(x) = s^2 = \dfrac{L^2}{h^2} x^2$, and
>
> $$
> V = \int_0^h \frac{L^2}{h^2} x^2\,dx = \frac{L^2}{h^2} \cdot \frac{x^3}{3} \Big]_0^h = \frac{L^2 h}{3} .
> $$
>
> The position of the pyramid is a matter of convenience ([[§46 Volumes#^thm-46-1|Theorem §46.1]]). With the center of the base at the origin and the vertex on the positive $y$-axis, the cross-section at height $y$ is a square of side $L(h - y)/h$, and
>
> $$
> V = \int_0^h \frac{L^2}{h^2} (h - y)^2\,dy = \frac{L^2}{h^2} \Big[-\frac{(h - y)^3}{3}\Big]_0^h = \frac{L^2}{h^2} \cdot \frac{h^3}{3} = \frac{L^2 h}{3} .
> $$
>
> *Stewart: Example 6.2.8 and Note*

^ex-46-5
