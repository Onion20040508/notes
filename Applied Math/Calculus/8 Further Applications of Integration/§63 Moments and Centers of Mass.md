---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 63
stewart: "8.3"
aliases: ["Stewart 8.3 (cont.)"]
tags: [calculus]
---
← [[§62 Applications to Physics and Engineering]] · ↑ [[· 8 Further Applications of Integration]] · [[§64 Applications to Economics and Biology]] →

*Stewart, Section 8.3.*

The goal is the point $P$ on which a thin plate of a given shape balances horizontally, its **center of mass** (or center of gravity). We start with point masses.

## Moments and Centers of Mass

> [!theorem] Theorem §63.1: Law of the Lever
> Two masses $m_1$ and $m_2$ attached to a rod of negligible mass, on opposite sides of a fulcrum and at distances $d_1$ and $d_2$ from it, balance if
>
> $$
> m_1 d_1 = m_2 d_2 .
> $$
>
> (A lighter person balances a heavier one on a seesaw by sitting farther from the center.)
>
> *Stewart: 8.3, Equation 2*

^thm-63-1

*This is a law of physics, not a theorem of calculus: Stewart takes it as the experimental fact discovered by Archimedes.*

> [!theorem] Proposition §63.2: Center of Mass of Two Particles
> Let the rod lie along the $x$-axis with $m_1$ at $x_1$ and $m_2$ at $x_2$, $x_1 < x_2$. The balance point (center of mass) is
>
> $$
> \bar x = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} .
> $$
>
> *Stewart: 8.3, Equation 3*

^prop-63-2

> [!proof]+ Proof
> If the fulcrum is at $\bar x$ with $x_1 < \bar x < x_2$, the distances are $d_1 = \bar x - x_1$ and $d_2 = x_2 - \bar x$. By the Law of the Lever the rod balances if and only if
>
> $$
> m_1(\bar x - x_1) = m_2(x_2 - \bar x) \iff m_1 \bar x + m_2 \bar x = m_1 x_1 + m_2 x_2 \iff \bar x = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} .
> $$
>
> This $\bar x$ does lie between $x_1$ and $x_2$: it is a weighted average of them with positive weights $\frac{m_1}{m_1 + m_2}$ and $\frac{m_2}{m_1 + m_2}$.

^pf-63-2

*Uses:* [[§63 Moments and Centers of Mass#^thm-63-1|§63.1]]

> [!definition] Definition §63.1: Moments on a Line
> Let particles of masses $m_1, \ldots, m_n$ sit at the points $x_1, \ldots, x_n$ of the $x$-axis, and let $m = \sum m_i$ be the total mass. The number $m_i x_i$ is the **moment** of $m_i$ (with respect to the origin), and
>
> $$
> M = \sum_{i=1}^n m_i x_i
> $$
>
> is the **moment of the system about the origin**.
>
> *Stewart: 8.3, Equation 4*

^def-63-1

> [!definition] Definition §63.2: Center of Mass on a Line
> The **center of mass** of the system is
>
> $$
> \bar x = \frac{\sum_{i=1}^n m_i x_i}{\sum_{i=1}^n m_i} = \frac{M}{m} .
> $$
>
> For $n = 2$ this is [[§63 Moments and Centers of Mass#^prop-63-2|Proposition §63.2]].
>
> *Stewart: 8.3, Equation 4*

^def-63-2

> [!remark] Remark: Why the Center of Mass Is the Balance Point
> $m \bar x = M$ says: if the whole mass were concentrated at $\bar x$, its moment would equal the moment of the system. Equivalently, the moments *about* $\bar x$ cancel:
>
> $$
> \sum_{i=1}^n m_i (x_i - \bar x) = M - m \bar x = 0 .
> $$
>
> The masses to the right of $\bar x$ contribute $\sum m_i d_i$ with $d_i = x_i - \bar x > 0$, those to the left contribute $-\sum m_j d_j$ with $d_j = \bar x - x_j > 0$, and the two totals are equal: the Law of the Lever for $n$ masses. (Stewart says only that Equation 4 "can be shown similarly" to the case $n = 2$.)

^rem-63-1
> [!definition] Definition §63.3: Moments in the Plane
> Let particles of masses $m_1, \ldots, m_n$ be located at the points $(x_1, y_1), \ldots, (x_n, y_n)$ of the $xy$-plane, with total mass $m = \sum m_i$. The **moment of the system about the $y$-axis** and the **moment of the system about the $x$-axis** are
>
> $$
> M_y = \sum_{i=1}^n m_i x_i, \qquad M_x = \sum_{i=1}^n m_i y_i .
> $$
>
> $M_y$ measures the tendency of the system to rotate about the $y$-axis, and $M_x$ the tendency to rotate about the $x$-axis. (Each uses the distance *to* the axis: $x_i$ is the distance from $(x_i, y_i)$ to the $y$-axis.)
>
> *Stewart: 8.3, Equations 5, 6 and 7*

^def-63-3

> [!definition] Definition §63.4: Center of Mass in the Plane
> The **center of mass** is $(\bar x, \bar y)$, where
>
> $$
> \bar x = \frac{M_y}{m}, \qquad \bar y = \frac{M_x}{m} .
> $$
>
> Since $m \bar x = M_y$ and $m \bar y = M_x$, it is the point where a single particle of mass $m$ would have the same moments as the system.
>
> *Stewart: 8.3, Equations 5, 6 and 7*

^def-63-4

> [!example] Example §63.1: Three Point Masses
> Find the moments and center of mass of the system of masses $3$, $4$ and $8$ at the points $(-1, 1)$, $(2, -1)$ and $(3, 2)$.
>
> By [[§63 Moments and Centers of Mass#^def-63-3|Definition §63.3]],
>
> $$
> M_y = 3(-1) + 4(2) + 8(3) = 29, \qquad M_x = 3(1) + 4(-1) + 8(2) = 15 .
> $$
>
> The total mass is $m = 3 + 4 + 8 = 15$, so by [[§63 Moments and Centers of Mass#^def-63-4|Definition §63.4]]
>
> $$
> \bar x = \frac{M_y}{m} = \frac{29}{15}, \qquad \bar y = \frac{M_x}{m} = \frac{15}{15} = 1 .
> $$
>
> The center of mass is $\big(1\frac{14}{15}, 1\big)$. It is pulled toward the heavy mass $8$ at $(3, 2)$.
>
> *Stewart: Example 8.3.3*

^ex-63-1

### Plates: Centroids

> [!definition] Definition §63.5: Lamina
> A **lamina** is a flat plate.
>
> *Stewart: 8.3 (text and margin note)*

^def-63-5

> [!definition] Definition §63.6: Centroid
> If a lamina of uniform density $\rho$ occupies a region $\mathcal{R}$ of the plane, its center of mass is called the **centroid** of $\mathcal{R}$. (By [[§63 Moments and Centers of Mass#^thm-63-3|Theorem §63.3]] below it depends only on the shape of $\mathcal{R}$, not on $\rho$. A plate of non-uniform density usually balances elsewhere; that case is treated with double integrals in [[§118 Applications of Double Integrals#^def-118-5|Definition §118.5]].)
>
> *Stewart: 8.3 (text and margin note)*

^def-63-6

> [!remark] Remark: The Principles Behind the Formulas
> Moments of plates are set up so that the following physical principles hold.
> 1. **Symmetry principle.** If $\mathcal{R}$ is symmetric about a line $l$, then the centroid of $\mathcal{R}$ lies on $l$. (Reflecting $\mathcal{R}$ in $l$ leaves $\mathcal{R}$, hence its centroid, fixed, and the only points fixed by the reflection are the points of $l$.) In particular the centroid of a rectangle is its center.
> 2. **Concentration.** If the entire mass of a region is concentrated at its center of mass, its moments are unchanged: a moment is (mass) $\times$ (distance of the center of mass from the axis).
> 3. **Additivity.** The moment of the union of two nonoverlapping regions is the sum of their moments.

^rem-63-2
> [!theorem] Theorem §63.3: Moments and Centroid of a Plate
> Let $f$ be continuous with $f \ge 0$ on $[a, b]$, and let $\mathcal{R}$ be the region under the graph of $f$ above $[a, b]$, occupied by a lamina of uniform density $\rho$. Then the moments of $\mathcal{R}$ about the $y$-axis and the $x$-axis, and its mass, are
>
> $$
> M_y = \rho \int_a^b x f(x)\,dx, \qquad M_x = \rho \int_a^b \tfrac12 [f(x)]^2\,dx, \qquad m = \rho A = \rho \int_a^b f(x)\,dx .
> $$
>
> The center of mass of the plate, that is, the centroid of $\mathcal{R}$, is the point $(\bar x, \bar y)$ with $m \bar x = M_y$, $m \bar y = M_x$; the $\rho$'s cancel and
>
> $$
> \bar x = \frac{1}{A} \int_a^b x f(x)\,dx, \qquad \bar y = \frac{1}{A} \int_a^b \tfrac12 [f(x)]^2\,dx ,
> $$
>
> where $A = \int_a^b f(x)\,dx$ is the area of $\mathcal{R}$.
>
> *Stewart: 8.3 (text) and Formulas 8*

^thm-63-3

> [!proof]+ Proof
> Divide $[a, b]$ into $n$ subintervals of equal width $\Delta x$ with endpoints $x_0, \ldots, x_n$, and let $\bar x_i = (x_{i-1} + x_i)/2$ be the midpoint of the $i$th one. Approximate $\mathcal{R}$ by the rectangles $R_i$ with base $[x_{i-1}, x_i]$ and height $f(\bar x_i)$.
>
> By the symmetry principle, the centroid of $R_i$ is its center $C_i\big(\bar x_i, \frac12 f(\bar x_i)\big)$. Its mass is density $\times$ area, $\rho f(\bar x_i)\,\Delta x$. By the concentration principle its moments are this mass times the distance from $C_i$ to the axis:
>
> $$
> M_y(R_i) = \big[\rho f(\bar x_i)\,\Delta x\big]\,\bar x_i = \rho\,\bar x_i f(\bar x_i)\,\Delta x, \qquad
> M_x(R_i) = \big[\rho f(\bar x_i)\,\Delta x\big]\,\tfrac12 f(\bar x_i) = \rho \cdot \tfrac12 [f(\bar x_i)]^2\,\Delta x .
> $$
>
> By additivity, the moments of the polygonal approximation $R_1 \cup \cdots \cup R_n$ are the sums of these. They are Riemann sums (midpoint rule) of the continuous functions $\rho x f(x)$ and $\rho \frac12 [f(x)]^2$, so as $n \to \infty$
>
> $$
> M_y = \lim_{n \to \infty} \sum_{i=1}^n \rho\,\bar x_i f(\bar x_i)\,\Delta x = \rho \int_a^b x f(x)\,dx, \qquad
> M_x = \lim_{n \to \infty} \sum_{i=1}^n \rho \cdot \tfrac12 [f(\bar x_i)]^2\,\Delta x = \rho \int_a^b \tfrac12 [f(x)]^2\,dx .
> $$
>
> (The moments of $\mathcal{R}$ are *defined* as these limits of the moments of the approximating polygons; the [[§63 Moments and Centers of Mass#^rem-63-2|principles]] fix the moments of the polygons.) The mass is density times area, $m = \rho A$ with $A = \int_a^b f(x)\,dx$ ([[§38 The Area and Distance Problems#^def-38-1|Definition §38.1]]); the midpoint sums above converge because $x f(x)$ and $\frac12 [f(x)]^2$ are continuous ([[§39 The Definite Integral#^thm-39-1|Theorem §39.1]]) and the limit of Riemann sums does not depend on the sample points ([[§39 The Definite Integral#^def-39-1|Definition §39.1]]). Dividing, $\bar x = M_y / m$ and $\bar y = M_x / m$, and $\rho$ cancels from numerator and denominator.

^pf-63-3

*Uses:* [[§63 Moments and Centers of Mass#^def-63-3|Def. §63.3]], [[§63 Moments and Centers of Mass#^def-63-4|Def. §63.4]], [[§63 Moments and Centers of Mass#^rem-63-2|Remark: The Principles Behind the Formulas]], [[§39 The Definite Integral#^def-39-1|Def. §39.1]], [[§39 The Definite Integral#^thm-39-1|§39.1]] (Riemann sums of continuous functions converge to the integral), [[§38 The Area and Distance Problems#^def-38-1|Def. §38.1]] (area under a curve)

> [!remark]- Connections
> - $\bar x = \int_a^b x f(x)\,dx \big/ \int_a^b f(x)\,dx$ is the average of $x$ with weight $f \ge 0$. The Weighted Mean Value Theorem [[§33 Properties of the Riemann Integral#^thm-33-10|451 Thm. §33.10]] (with the continuous function $x$ and the weight $f$) gives $\bar x \in [a, b]$: the centroid lies over the base of the region.

> [!example] Example §63.2: Semicircular Plate
> Find the center of mass of a semicircular plate of radius $r$ with uniform density.
>
> Place the semicircle as the region under $f(x) = \sqrt{r^2 - x^2}$, $-r \le x \le r$. It is symmetric about the $y$-axis, so by the symmetry principle $\bar x = 0$; no integral is needed. The area is $A = \frac12 \pi r^2$, and by [[§63 Moments and Centers of Mass#^thm-63-3|Theorem §63.3]]
>
> $$
> \begin{aligned}
> \bar y &= \frac{1}{A} \int_{-r}^{r} \tfrac12 [f(x)]^2\,dx = \frac{1}{\frac12 \pi r^2} \cdot \frac12 \int_{-r}^{r} \big(\sqrt{r^2 - x^2}\big)^2\,dx \\
> &= \frac{2}{\pi r^2} \int_0^r (r^2 - x^2)\,dx \qquad \text{(the integrand is even)} \\
> &= \frac{2}{\pi r^2} \Big[ r^2 x - \frac{x^3}{3} \Big]_0^r = \frac{2}{\pi r^2} \cdot \frac{2r^3}{3} = \frac{4r}{3\pi} .
> \end{aligned}
> $$
>
> The center of mass is $\big(0, \frac{4r}{3\pi}\big)$, at about $0.42\,r$ above the diameter.
>
> *Stewart: Example 8.3.4*

^ex-63-2

> [!theorem] Theorem §63.4: Centroid of a Region Between Two Curves
> Let $f$ and $g$ be continuous with $f(x) \ge g(x)$ on $[a, b]$, and let $\mathcal{R}$ be the region between $y = g(x)$ and $y = f(x)$, $a \le x \le b$, with area $A = \int_a^b [f(x) - g(x)]\,dx$. The centroid of $\mathcal{R}$ is $(\bar x, \bar y)$, where
>
> $$
> \bar x = \frac{1}{A} \int_a^b x\,[f(x) - g(x)]\,dx, \qquad
> \bar y = \frac{1}{A} \int_a^b \tfrac12 \big\{ [f(x)]^2 - [g(x)]^2 \big\}\,dx .
> $$
>
> [[§63 Moments and Centers of Mass#^thm-63-3|Theorem §63.3]] is the case $g = 0$.
>
> *Stewart: 8.3, Formulas 9*

^thm-63-4

> [!proof]+ Proof
> (Stewart says that "the same sort of argument" as for [[§63 Moments and Centers of Mass#^thm-63-3|Theorem §63.3]] gives these formulas and leaves the details as Exercise 51. Here they are.) Take a lamina of density $\rho$ on $\mathcal{R}$, divide $[a, b]$ into $n$ subintervals of width $\Delta x$ with midpoints $\bar x_i$, and approximate $\mathcal{R}$ by the rectangles $R_i$ with base $[x_{i-1}, x_i]$, bottom $g(\bar x_i)$ and top $f(\bar x_i)$. The rectangle $R_i$ has
>
> $$
> \text{mass } \rho\,[f(\bar x_i) - g(\bar x_i)]\,\Delta x, \qquad \text{center } C_i\Big(\bar x_i,\ \tfrac12\big[f(\bar x_i) + g(\bar x_i)\big]\Big) .
> $$
>
> By the concentration principle,
>
> $$
> M_y(R_i) = \rho\,\bar x_i\,[f(\bar x_i) - g(\bar x_i)]\,\Delta x, \qquad
> M_x(R_i) = \rho\,[f(\bar x_i) - g(\bar x_i)] \cdot \tfrac12 [f(\bar x_i) + g(\bar x_i)]\,\Delta x = \rho \cdot \tfrac12 \big\{ [f(\bar x_i)]^2 - [g(\bar x_i)]^2 \big\}\,\Delta x .
> $$
>
> By additivity and passing to the limit as in [[§63 Moments and Centers of Mass#^thm-63-3|Theorem §63.3]],
>
> $$
> M_y = \rho \int_a^b x\,[f(x) - g(x)]\,dx, \qquad M_x = \rho \int_a^b \tfrac12 \big\{ [f(x)]^2 - [g(x)]^2 \big\}\,dx ,
> $$
>
> and the mass is $m = \rho A$ ([[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]]). Dividing by $m$ gives the formulas.

^pf-63-4

*Uses:* [[§63 Moments and Centers of Mass#^thm-63-3|§63.3]], [[§63 Moments and Centers of Mass#^rem-63-2|Remark: The Principles Behind the Formulas]], [[§45 Areas Between Curves#^thm-45-1|§45.1]] (area between curves)

> [!remark]- Connections
> - These are [[§115 Double Integrals Over Rectangles#^def-115-4|iterated integrals]] in disguise: with $\mathcal{R}$ a [[§116 Double Integrals Over General Regions#^def-116-2|type I region]], $\int_{g(x)}^{f(x)} x\,dy = x[f(x) - g(x)]$ and $\int_{g(x)}^{f(x)} y\,dy = \frac12\{[f(x)]^2 - [g(x)]^2\}$, so by Fubini's theorem [[§23 Fubini's Theorem#^thm-23-2|452 Thm. §23.2]], $A\bar x = \iint_{\mathcal{R}} x\,dA$ and $A\bar y = \iint_{\mathcal{R}} y\,dA$. That is the definition used for plates of variable density in [[§118 Applications of Double Integrals#^def-118-5|Definition §118.5]].

> [!example] Example §63.3: Region Between a Line and a Parabola
> Find the centroid of the region bounded by the line $y = x$ and the parabola $y = x^2$.
>
> The curves meet where $x = x^2$, at $x = 0$ and $x = 1$, and $x \ge x^2$ on $[0, 1]$. So take $f(x) = x$, $g(x) = x^2$, $a = 0$, $b = 1$ in [[§63 Moments and Centers of Mass#^thm-63-4|Theorem §63.4]]. The area is
>
> $$
> A = \int_0^1 (x - x^2)\,dx = \Big[ \frac{x^2}{2} - \frac{x^3}{3} \Big]_0^1 = \frac12 - \frac13 = \frac16 .
> $$
>
> Therefore
>
> $$
> \begin{aligned}
> \bar x &= \frac{1}{A} \int_0^1 x\,(x - x^2)\,dx = 6 \int_0^1 (x^2 - x^3)\,dx = 6 \Big[ \frac{x^3}{3} - \frac{x^4}{4} \Big]_0^1 = 6 \cdot \frac{1}{12} = \frac12 , \\
> \bar y &= \frac{1}{A} \int_0^1 \tfrac12 (x^2 - x^4)\,dx = 3 \Big[ \frac{x^3}{3} - \frac{x^5}{5} \Big]_0^1 = 3 \cdot \frac{2}{15} = \frac25 .
> \end{aligned}
> $$
>
> The centroid is $\big(\frac12, \frac25\big)$. It lies inside the region: at $x = \frac12$ the region runs from $y = \frac14$ to $y = \frac12$.
>
> *Stewart: Example 8.3.6*

^ex-63-3

![[m233-54-2.svg]]
*[[§63 Moments and Centers of Mass#^ex-63-3|Example §63.3]]. A thin rectangle at $\bar x_i$ (green) reaches from $y = g(\bar x_i)$ to $y = f(\bar x_i)$; its mass sits at its center $C_i$, halfway between the two curves, which is where $\frac12\{[f]^2 - [g]^2\} = (f - g) \cdot \frac12 (f + g)$ comes from. Adding the moments of all such rectangles gives the centroid $\big(\frac12, \frac25\big)$ (red).*

*Chain:* ← [[§50 The Region Between y = x and y = x² and the Region Under y = √x#The Region Between y = x and y = x²|Chapter 6]]

## Theorem of Pappus

> [!theorem] Theorem §63.5: Theorem of Pappus
> Let $\mathcal{R}$ be a plane region that lies entirely on one side of a line $l$ in the plane. If $\mathcal{R}$ is rotated about $l$, then the volume of the resulting solid is the product of the area $A$ of $\mathcal{R}$ and the distance $d$ traveled by the centroid of $\mathcal{R}$:
>
> $$
> V = A d .
> $$
>
> *Stewart: 8.3, Theorem of Pappus*

^thm-63-5

> [!proof]+ Proof
> Stewart proves the special case in which $\mathcal{R}$ lies between $y = f(x)$ and $y = g(x)$, $a \le x \le b$ (with $f \ge g$ continuous), and $l$ is the $y$-axis. Since $\mathcal{R}$ lies on one side of $l$, we may take $0 \le a$. By the method of cylindrical shells ([[§47 Volumes by Cylindrical Shells#^thm-47-2|Theorem §47.2]]),
>
> $$
> \begin{aligned}
> V &= \int_a^b 2\pi x\,[f(x) - g(x)]\,dx = 2\pi \int_a^b x\,[f(x) - g(x)]\,dx \\
> &= 2\pi\,(\bar x A) \qquad \text{(by [[§63 Moments and Centers of Mass#^thm-63-4|Theorem §63.4]])} \\
> &= (2\pi \bar x)\,A = A d ,
> \end{aligned}
> $$
>
> where $d = 2\pi \bar x$ is the distance traveled by the centroid, at distance $\bar x$ from the $y$-axis, during one rotation about the $y$-axis.

^pf-63-5

*Uses:* [[§63 Moments and Centers of Mass#^thm-63-4|§63.4]], [[§47 Volumes by Cylindrical Shells#^thm-47-2|§47.2]] (shell method)

*Stewart proves only this special case. Any line $l$ can be made the $y$-axis by a choice of coordinates, so the proof covers every region that is bounded by two graphs over an interval in the direction perpendicular to $l$; a region that can be cut into finitely many such pieces follows by additivity of volumes and of moments.*

> [!example] Example §63.4: Volume of a Torus
> A torus is formed by rotating a circle of radius $r$ about a line in the plane of the circle at distance $R > r$ from the center of the circle. Find the volume of the torus.
>
> Rotate the disk bounded by the circle. Its area is $A = \pi r^2$. By the symmetry principle its centroid is its center, which travels around a circle of radius $R$, a distance $d = 2\pi R$. Since $R > r$, the disk lies on one side of the axis, and the Theorem of Pappus gives
>
> $$
> V = A d = (\pi r^2)(2\pi R) = 2\pi^2 r^2 R .
> $$
>
> Without Pappus one has to integrate, for instance by shells, $V = \int_{R - r}^{R + r} 2\pi x \cdot 2\sqrt{r^2 - (x - R)^2}\,dx$ (axis along the $y$-axis, center of the circle at $(R, 0)$). Stewart compares the method with his Exercise 6.2.75, which finds the volume by slicing ([[§46 Volumes|§46]]).
>
> *Stewart: Example 8.3.7*

^ex-63-4
