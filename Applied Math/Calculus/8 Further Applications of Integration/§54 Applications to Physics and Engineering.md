---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 54
stewart: "8.3"
aliases: ["Stewart 8.3"]
tags: [calculus]
---
← [[§53 Area of a Surface of Revolution]] · ↑ [[· 8 Further Applications of Integration]] · [[§55 Applications to Economics and Biology]] →

*Stewart, Section 8.3.*

Two physical quantities are computed here by the same strategy as areas, volumes and work ([[§42 Work|§42]]): cut the object into thin pieces, approximate the quantity on each piece, add (a Riemann sum), and pass to the limit. The first is the force that water exerts on a vertical dam or plate, where the pressure grows with depth. The second is the center of mass of a thin plate, the point where it balances; for a plate of uniform density it depends only on the shape and is called the centroid. The section ends with the Theorem of Pappus, which turns a centroid into the volume of a solid of revolution.

## Hydrostatic Pressure and Force

> [!definition] Definition §54.1: Pressure
> The **pressure** $P$ on a surface is the force per unit area:
>
> $$
> P = \frac{F}{A} .
> $$
>
> The SI unit is the newton per square meter, called a **pascal**: $1\ \text{N/m}^2 = 1\ \text{Pa}$; the kilopascal ($1\ \text{kPa} = 1000\ \text{Pa}$) is often more convenient. For a fluid of (mass) density $\rho$, the **weight density** is $\delta = \rho g$, where $g$ is the acceleration due to gravity. Water has $\rho = 1000\ \text{kg/m}^3$ and, in US Customary units, $\delta = 62.5\ \text{lb/ft}^3$.
>
> *Stewart: 8.3 (text)*

^def-54-1

> [!theorem] Theorem §54.1: Hydrostatic Pressure
> At a depth $d$ in a fluid of mass density $\rho$, the pressure in any direction is
>
> $$
> P = \rho g d = \delta d .
> $$
>
> It depends only on the depth, not on the amount of fluid: a fish $2$ ft below the surface feels the same pressure in a small aquarium as in a lake. For example, at the bottom of a swimming pool $2$ m deep,
>
> $$
> P = 1000\ \text{kg/m}^3 \times 9.8\ \text{m/s}^2 \times 2\ \text{m} = 19{,}600\ \text{Pa} = 19.6\ \text{kPa},
> $$
>
> and at the bottom of a pool $8$ ft deep, $P = \delta d = 62.5\ \text{lb/ft}^3 \times 8\ \text{ft} = 500\ \text{lb/ft}^2$.
>
> *Stewart: 8.3, Equation 1*

^thm-54-1

> [!proof]+ Proof
> Let a thin horizontal plate of area $A$ be submerged at depth $d$. The fluid directly above it is a column of volume $V = Ad$, so its mass is $m = \rho V = \rho A d$, and its weight, the force it exerts on the plate, is
>
> $$
> F = mg = \rho g A d .
> $$
>
> So the pressure on the plate is $P = F/A = \rho g d = \delta d$.
>
> This computes the pressure on a *horizontal* surface. That the pressure at a point of a liquid is the same in all directions (a diver feels the same pressure on nose and both ears) is not derived: Stewart takes it as an experimentally verified principle of fluids. With it, $P = \delta d$ holds for a surface in any position.

^pf-54-1

*Uses:* [[§54 Applications to Physics and Engineering#^def-54-1|Def. §54.1]]

The pressure on a *vertical* plate is not constant: it increases with depth. That is why the force on a dam needs an integral.

> [!theorem] Theorem §54.2: Hydrostatic Force on a Vertical Plate
> A plate is submerged vertically in a fluid of weight density $\delta = \rho g$. Measure depth by an $x$-axis pointing down, with origin at the surface of the fluid. Suppose the plate extends from depth $a$ to depth $b$ ($0 \le a < b$) and its width at depth $x$ is $w(x)$, with $w$ continuous. Then the hydrostatic force (the force exerted by the fluid at rest) on one side of the plate is
>
> $$
> F = \int_a^b \delta\, x\, w(x)\,dx = \int_a^b \rho g\, x\, w(x)\,dx .
> $$
>
> In words: integrate pressure $\times$ (area of a horizontal strip), where the pressure is that at the depth of the strip.
>
> *Stewart: 8.3 (text and Examples 1–2); the general formula is Exercise 18*

^thm-54-2

> [!proof]+ Proof
> **Stewart's argument.** Divide $[a, b]$ into $n$ subintervals of length $\Delta x$ with endpoints $x_i$, and choose $x_i^{\ast} \in [x_{i-1}, x_i]$. The $i$th horizontal strip of the plate is approximately a rectangle of height $\Delta x$ and width $w(x_i^{\ast})$, so its area is $A_i \approx w(x_i^{\ast})\,\Delta x$. If $\Delta x$ is small, the pressure on the strip is almost constant, $P_i \approx \delta x_i^{\ast}$ by Theorem §54.1, and the force on it is $F_i = P_i A_i \approx \delta x_i^{\ast} w(x_i^{\ast})\,\Delta x$. Adding,
>
> $$
> F = \sum_{i=1}^n F_i \approx \sum_{i=1}^n \delta x_i^* w(x_i^*)\,\Delta x \;\longrightarrow\; \int_a^b \delta x\, w(x)\,dx \qquad (n \to \infty).
> $$
>
> **Making the "$\approx$" precise.** The exact area of the $i$th strip is $A_i = \int_{x_{i-1}}^{x_i} w(x)\,dx$ ([[§39 Areas Between Curves#^thm-39-3|Theorem §39.3]], with the vertical depth as the variable). Every point of the strip has depth between $x_{i-1}$ and $x_i$, so the pressure there lies between $\delta x_{i-1}$ and $\delta x_i$, and the force on the strip (pressure acting on area, all perpendicular to the plate) satisfies
>
> $$
> \delta x_{i-1} A_i \le F_i \le \delta x_i A_i .
> $$
>
> Since $w \ge 0$ and $x_{i-1} \le x \le x_i$ on the strip, the integral obeys the same bounds:
>
> $$
> \delta x_{i-1} A_i \le \int_{x_{i-1}}^{x_i} \delta x\, w(x)\,dx \le \delta x_i A_i .
> $$
>
> Add over $i$. Both $F = \sum F_i$ and $I = \int_a^b \delta x\, w(x)\,dx$ lie between $L_n = \sum \delta x_{i-1} A_i$ and $U_n = \sum \delta x_i A_i$, and
>
> $$
> U_n - L_n = \sum_{i=1}^n \delta\,(x_i - x_{i-1})\,A_i = \delta\,\Delta x \sum_{i=1}^n A_i = \delta\,\Delta x \cdot (\text{area of the plate}) \;\longrightarrow\; 0 .
> $$
>
> So $|F - I| \le U_n - L_n$ for every $n$, and $F = I$.

^pf-54-2

*Uses:* [[§54 Applications to Physics and Engineering#^thm-54-1|§54.1]], [[§35 The Definite Integral#^def-35-1|Def. §35.1]] (Riemann sums), [[§35 The Definite Integral#^thm-35-5|§35.5]] (additivity over adjacent intervals), [[§35 The Definite Integral#^thm-35-6|§35.6]] (comparison properties), [[§39 Areas Between Curves#^thm-39-3|§39.3]] (area as an integral of width)

![[m233-54-1.svg]]
*The dam of Example §54.1. With depth $x$ measured down from the water surface, the horizontal strip at depth $x$ (red) has width $w(x) = 2(15 + a)$, where similar triangles give $a / (16 - x) = 10/20$ (green). The pressure on the strip is about $\rho g x$, so it carries a force of about $\rho g x\,w(x)\,\Delta x$.*

> [!remark]- Connections
> - The proof is a Darboux–Stieltjes argument: with the cumulative area $A(x) = \int_a^x w$ as weight, $L_n$ and $U_n$ are the lower and upper sums of $\delta x$ with respect to $A$, so $F = \int_a^b \delta x\,dA(x)$ in the sense of [[§35 Riemann–Stieltjes Integrals#^def-35-1|451 Def. §35.1]].

> [!remark] Remark: Method — Hydrostatic Force
> 1. **Coordinates.** Choose an axis for depth. A vertical $x$-axis pointing down from the surface makes the depth simply $x$ (Example §54.1). Any other choice works if the depth is written correctly: with the origin at the bottom of the dam and $y$ up, depth is $16 - y$; with the origin at the center of a circular plate whose center is $7$ ft below the surface, depth is $7 - y$.
> 2. **Width.** Find the width of a horizontal strip as a function of the depth variable, from the equation of the edge or from similar triangles.
> 3. **Force on a strip.** Pressure $\times$ area: $\delta \cdot (\text{depth}) \cdot (\text{width}) \cdot \Delta x$. Use $\rho g$ with $\rho$ in $\text{kg/m}^3$ in SI units, and $\delta$ in $\text{lb/ft}^3$ in US units.
> 4. **Integrate** over the depths where the plate is under the fluid; a plate sticking out of the fluid is cut off at the surface.
> 5. **Evaluate** using symmetry where possible. In Stewart's Example 8.3.2 (the end of a drum of radius $3$ ft, center $7$ ft deep), $F = 125 \int_{-3}^{3} (7 - y)\sqrt{9 - y^2}\,dy$; the part $\int_{-3}^3 y\sqrt{9 - y^2}\,dy$ is $0$ because the integrand is odd ([[§38 The Substitution Rule#^thm-38-4|Theorem §38.4]]), and $\int_{-3}^3 \sqrt{9 - y^2}\,dy = \frac12 \pi (3)^2$ is the area of a half-disk, so $F = 875 \cdot \frac92 \pi = \frac{7875\pi}{2} \approx 12{,}370$ lb.

^rem-54-1

> [!example] Example §54.1: Force on a Trapezoidal Dam
> A dam has the shape of a trapezoid with height $20$ m, width $50$ m at the top and $30$ m at the bottom. Find the force on the dam due to hydrostatic pressure if the water level is $4$ m below the top of the dam.
>
> **Coordinates.** Take a vertical $x$-axis with origin at the water surface, pointing down. The water is $20 - 4 = 16$ m deep, so $0 \le x \le 16$.
>
> **Width.** By symmetry about the center line, the half-width at depth $x$ is $15 + a$, where $a$ is the horizontal distance from the vertical line through the bottom corner to the slanted edge. The edge rises $20$ m while moving out $25 - 15 = 10$ m, and at depth $x$ we are $16 - x$ m above the bottom, so by similar triangles
>
> $$
> \frac{a}{16 - x} = \frac{10}{20}, \qquad a = 8 - \frac{x}{2}, \qquad w(x) = 2(15 + a) = 2\Big(23 - \frac{x}{2}\Big) = 46 - x .
> $$
>
> (Check: at the surface $w(0) = 46$ and at the bottom $w(16) = 30$.)
>
> **Force.** By Theorem §54.2 with $\rho = 1000\ \text{kg/m}^3$ and $g = 9.8\ \text{m/s}^2$,
>
> $$
> \begin{aligned}
> F &= \int_0^{16} 1000(9.8)\, x\,(46 - x)\,dx = 9800 \int_0^{16} (46x - x^2)\,dx = 9800 \Big[ 23x^2 - \frac{x^3}{3} \Big]_0^{16} \\
> &= 9800 \Big( 5888 - \frac{4096}{3} \Big) = 9800 \cdot \frac{13568}{3} \approx 4.43 \times 10^7\ \text{N} .
> \end{aligned}
> $$
>
> **Other coordinates.** With the origin at the center of the bottom and $y$ up, the right edge is the line through $(15, 0)$ and $(25, 20)$, $y = 2x - 30$, so the strip at height $y$ has width $2x = y + 30$ and lies at depth $16 - y$:
>
> $$
> F = 9800 \int_0^{16} (y + 30)(16 - y)\,dy = 9800 \int_0^{16} (480 - 14y - y^2)\,dy = 9800 \Big( 7680 - 1792 - \frac{4096}{3} \Big) ,
> $$
>
> the same number, $9800 \cdot \frac{13568}{3} \approx 4.43 \times 10^7$ N.
>
> *Stewart: Example 8.3.1*

^ex-54-1

## Moments and Centers of Mass

The goal is the point $P$ on which a thin plate of a given shape balances horizontally, its **center of mass** (or center of gravity). We start with point masses.

> [!theorem] Theorem §54.3: Law of the Lever
> Two masses $m_1$ and $m_2$ attached to a rod of negligible mass, on opposite sides of a fulcrum and at distances $d_1$ and $d_2$ from it, balance if
>
> $$
> m_1 d_1 = m_2 d_2 .
> $$
>
> (A lighter person balances a heavier one on a seesaw by sitting farther from the center.)
>
> *Stewart: 8.3, Equation 2*

^thm-54-3

*This is a law of physics, not a theorem of calculus: Stewart takes it as the experimental fact discovered by Archimedes.*

> [!theorem] Proposition §54.4: Center of Mass of Two Particles
> Let the rod lie along the $x$-axis with $m_1$ at $x_1$ and $m_2$ at $x_2$, $x_1 < x_2$. The balance point (center of mass) is
>
> $$
> \bar x = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} .
> $$
>
> *Stewart: 8.3, Equation 3*

^prop-54-4

> [!proof]+ Proof
> If the fulcrum is at $\bar x$ with $x_1 < \bar x < x_2$, the distances are $d_1 = \bar x - x_1$ and $d_2 = x_2 - \bar x$. By the Law of the Lever the rod balances if and only if
>
> $$
> m_1(\bar x - x_1) = m_2(x_2 - \bar x) \iff m_1 \bar x + m_2 \bar x = m_1 x_1 + m_2 x_2 \iff \bar x = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} .
> $$
>
> This $\bar x$ does lie between $x_1$ and $x_2$: it is a weighted average of them with positive weights $\frac{m_1}{m_1 + m_2}$ and $\frac{m_2}{m_1 + m_2}$.

^pf-54-4

*Uses:* [[§54 Applications to Physics and Engineering#^thm-54-3|§54.3]]

> [!definition] Definition §54.2: Moments and Center of Mass on a Line
> Let particles of masses $m_1, \ldots, m_n$ sit at the points $x_1, \ldots, x_n$ of the $x$-axis, and let $m = \sum m_i$ be the total mass. The number $m_i x_i$ is the **moment** of $m_i$ (with respect to the origin), and
>
> $$
> M = \sum_{i=1}^n m_i x_i
> $$
>
> is the **moment of the system about the origin**. The **center of mass** of the system is
>
> $$
> \bar x = \frac{\sum_{i=1}^n m_i x_i}{\sum_{i=1}^n m_i} = \frac{M}{m} .
> $$
>
> For $n = 2$ this is Proposition §54.4.
>
> *Stewart: 8.3, Equation 4*

^def-54-2

> [!remark] Remark: Why the Center of Mass Is the Balance Point
> $m \bar x = M$ says: if the whole mass were concentrated at $\bar x$, its moment would equal the moment of the system. Equivalently, the moments *about* $\bar x$ cancel:
>
> $$
> \sum_{i=1}^n m_i (x_i - \bar x) = M - m \bar x = 0 .
> $$
>
> The masses to the right of $\bar x$ contribute $\sum m_i d_i$ with $d_i = x_i - \bar x > 0$, those to the left contribute $-\sum m_j d_j$ with $d_j = \bar x - x_j > 0$, and the two totals are equal: the Law of the Lever for $n$ masses. (Stewart says only that Equation 4 "can be shown similarly" to the case $n = 2$.)

^rem-54-2

> [!definition] Definition §54.3: Moments and Center of Mass in the Plane
> Let particles of masses $m_1, \ldots, m_n$ be located at the points $(x_1, y_1), \ldots, (x_n, y_n)$ of the $xy$-plane, with total mass $m = \sum m_i$. The **moment of the system about the $y$-axis** and the **moment of the system about the $x$-axis** are
>
> $$
> M_y = \sum_{i=1}^n m_i x_i, \qquad M_x = \sum_{i=1}^n m_i y_i .
> $$
>
> $M_y$ measures the tendency of the system to rotate about the $y$-axis, and $M_x$ the tendency to rotate about the $x$-axis. (Each uses the distance *to* the axis: $x_i$ is the distance from $(x_i, y_i)$ to the $y$-axis.) The **center of mass** is $(\bar x, \bar y)$, where
>
> $$
> \bar x = \frac{M_y}{m}, \qquad \bar y = \frac{M_x}{m} .
> $$
>
> Since $m \bar x = M_y$ and $m \bar y = M_x$, it is the point where a single particle of mass $m$ would have the same moments as the system.
>
> *Stewart: 8.3, Equations 5, 6 and 7*

^def-54-3

> [!example] Example §54.2: Three Point Masses
> Find the moments and center of mass of the system of masses $3$, $4$ and $8$ at the points $(-1, 1)$, $(2, -1)$ and $(3, 2)$.
>
> By Definition §54.3,
>
> $$
> M_y = 3(-1) + 4(2) + 8(3) = 29, \qquad M_x = 3(1) + 4(-1) + 8(2) = 15 .
> $$
>
> The total mass is $m = 3 + 4 + 8 = 15$, so
>
> $$
> \bar x = \frac{M_y}{m} = \frac{29}{15}, \qquad \bar y = \frac{M_x}{m} = \frac{15}{15} = 1 .
> $$
>
> The center of mass is $\big(1\frac{14}{15}, 1\big)$. It is pulled toward the heavy mass $8$ at $(3, 2)$.
>
> *Stewart: Example 8.3.3*

^ex-54-2

### Plates: Centroids

> [!definition] Definition §54.4: Lamina
> A **lamina** is a flat plate.
>
> *Stewart: 8.3 (text and margin note)*

^def-54-4

> [!definition] Definition §54.4: Centroid
> If a lamina of uniform density $\rho$ occupies a region $\mathcal{R}$ of the plane, its center of mass is called the **centroid** of $\mathcal{R}$. (By Theorem §54.5 below it depends only on the shape of $\mathcal{R}$, not on $\rho$. A plate of non-uniform density usually balances elsewhere; that case is treated with double integrals in [[§101 Applications of Double Integrals#^def-101-3|Definition §101.3]].)
>
> *Stewart: 8.3 (text and margin note)*

^def-54-new1

> [!remark] Remark: The Principles Behind the Formulas
> Moments of plates are set up so that the following physical principles hold.
> 1. **Symmetry principle.** If $\mathcal{R}$ is symmetric about a line $l$, then the centroid of $\mathcal{R}$ lies on $l$. (Reflecting $\mathcal{R}$ in $l$ leaves $\mathcal{R}$, hence its centroid, fixed, and the only points fixed by the reflection are the points of $l$.) In particular the centroid of a rectangle is its center.
> 2. **Concentration.** If the entire mass of a region is concentrated at its center of mass, its moments are unchanged: a moment is (mass) $\times$ (distance of the center of mass from the axis).
> 3. **Additivity.** The moment of the union of two nonoverlapping regions is the sum of their moments.

^rem-54-3

> [!theorem] Theorem §54.5: Moments and Centroid of a Plate
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

^thm-54-5

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
> (The moments of $\mathcal{R}$ are *defined* as these limits of the moments of the approximating polygons; the [[§54 Applications to Physics and Engineering#^rem-54-3|principles]] fix the moments of the polygons.) The mass is density times area, $m = \rho A$ with $A = \int_a^b f(x)\,dx$ ([[§34 The Area and Distance Problems#^def-34-1|Definition §34.1]]); the midpoint sums above converge because $x f(x)$ and $\frac12 [f(x)]^2$ are continuous ([[§35 The Definite Integral#^thm-35-1|Theorem §35.1]]) and the limit of Riemann sums does not depend on the sample points ([[§35 The Definite Integral#^def-35-1|Definition §35.1]]). Dividing, $\bar x = M_y / m$ and $\bar y = M_x / m$, and $\rho$ cancels from numerator and denominator.

^pf-54-5

*Uses:* [[§54 Applications to Physics and Engineering#^def-54-3|Def. §54.3]], [[§54 Applications to Physics and Engineering#^rem-54-3|Remark: The Principles Behind the Formulas]], [[§35 The Definite Integral#^def-35-1|Def. §35.1]], [[§35 The Definite Integral#^thm-35-1|§35.1]] (Riemann sums of continuous functions converge to the integral), [[§34 The Area and Distance Problems#^def-34-1|Def. §34.1]] (area under a curve)

> [!remark]- Connections
> - $\bar x = \int_a^b x f(x)\,dx \big/ \int_a^b f(x)\,dx$ is the average of $x$ with weight $f \ge 0$. The Weighted Mean Value Theorem [[§33 Properties of the Riemann Integral#^thm-33-10|451 Thm. §33.10]] (with the continuous function $x$ and the weight $f$) gives $\bar x \in [a, b]$: the centroid lies over the base of the region.

> [!example] Example §54.3: Semicircular Plate
> Find the center of mass of a semicircular plate of radius $r$ with uniform density.
>
> Place the semicircle as the region under $f(x) = \sqrt{r^2 - x^2}$, $-r \le x \le r$. It is symmetric about the $y$-axis, so by the symmetry principle $\bar x = 0$; no integral is needed. The area is $A = \frac12 \pi r^2$, and by Theorem §54.5
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

^ex-54-3

> [!theorem] Theorem §54.6: Centroid of a Region Between Two Curves
> Let $f$ and $g$ be continuous with $f(x) \ge g(x)$ on $[a, b]$, and let $\mathcal{R}$ be the region between $y = g(x)$ and $y = f(x)$, $a \le x \le b$, with area $A = \int_a^b [f(x) - g(x)]\,dx$. The centroid of $\mathcal{R}$ is $(\bar x, \bar y)$, where
>
> $$
> \bar x = \frac{1}{A} \int_a^b x\,[f(x) - g(x)]\,dx, \qquad
> \bar y = \frac{1}{A} \int_a^b \tfrac12 \big\{ [f(x)]^2 - [g(x)]^2 \big\}\,dx .
> $$
>
> Theorem §54.5 is the case $g = 0$.
>
> *Stewart: 8.3, Formulas 9*

^thm-54-6

> [!proof]+ Proof
> (Stewart says that "the same sort of argument" as for Theorem §54.5 gives these formulas and leaves the details as Exercise 51. Here they are.) Take a lamina of density $\rho$ on $\mathcal{R}$, divide $[a, b]$ into $n$ subintervals of width $\Delta x$ with midpoints $\bar x_i$, and approximate $\mathcal{R}$ by the rectangles $R_i$ with base $[x_{i-1}, x_i]$, bottom $g(\bar x_i)$ and top $f(\bar x_i)$. The rectangle $R_i$ has
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
> By additivity and passing to the limit as in Theorem §54.5,
>
> $$
> M_y = \rho \int_a^b x\,[f(x) - g(x)]\,dx, \qquad M_x = \rho \int_a^b \tfrac12 \big\{ [f(x)]^2 - [g(x)]^2 \big\}\,dx ,
> $$
>
> and the mass is $m = \rho A$ ([[§39 Areas Between Curves#^thm-39-1|Theorem §39.1]]). Dividing by $m$ gives the formulas.

^pf-54-6

*Uses:* [[§54 Applications to Physics and Engineering#^thm-54-5|§54.5]], [[§54 Applications to Physics and Engineering#^rem-54-3|Remark: The Principles Behind the Formulas]], [[§39 Areas Between Curves#^thm-39-1|§39.1]] (area between curves)

> [!remark]- Connections
> - These are [[§98 Double Integrals Over Rectangles#^def-98-4|iterated integrals]] in disguise: with $\mathcal{R}$ a [[§99 Double Integrals Over General Regions#^def-99-2|type I region]], $\int_{g(x)}^{f(x)} x\,dy = x[f(x) - g(x)]$ and $\int_{g(x)}^{f(x)} y\,dy = \frac12\{[f(x)]^2 - [g(x)]^2\}$, so by Fubini's theorem [[§15 Multivariable Integration#^thm-15-9|452 Thm. §15.9]], $A\bar x = \iint_{\mathcal{R}} x\,dA$ and $A\bar y = \iint_{\mathcal{R}} y\,dA$. That is the definition used for plates of variable density in [[§101 Applications of Double Integrals#^def-101-3|Definition §101.3]].

> [!example] Example §54.4: Region Between a Line and a Parabola
> Find the centroid of the region bounded by the line $y = x$ and the parabola $y = x^2$.
>
> The curves meet where $x = x^2$, at $x = 0$ and $x = 1$, and $x \ge x^2$ on $[0, 1]$. So take $f(x) = x$, $g(x) = x^2$, $a = 0$, $b = 1$ in Theorem §54.6. The area is
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

^ex-54-4

![[m233-54-2.svg]]
*Example §54.4. A thin rectangle at $\bar x_i$ (green) reaches from $y = g(\bar x_i)$ to $y = f(\bar x_i)$; its mass sits at its center $C_i$, halfway between the two curves, which is where $\frac12\{[f]^2 - [g]^2\} = (f - g) \cdot \frac12 (f + g)$ comes from. Adding the moments of all such rectangles gives the centroid $\big(\frac12, \frac25\big)$ (red).*

## Theorem of Pappus

> [!theorem] Theorem §54.7: Theorem of Pappus
> Let $\mathcal{R}$ be a plane region that lies entirely on one side of a line $l$ in the plane. If $\mathcal{R}$ is rotated about $l$, then the volume of the resulting solid is the product of the area $A$ of $\mathcal{R}$ and the distance $d$ traveled by the centroid of $\mathcal{R}$:
>
> $$
> V = A d .
> $$
>
> *Stewart: 8.3, Theorem of Pappus*

^thm-54-7

> [!proof]+ Proof
> Stewart proves the special case in which $\mathcal{R}$ lies between $y = f(x)$ and $y = g(x)$, $a \le x \le b$ (with $f \ge g$ continuous), and $l$ is the $y$-axis. Since $\mathcal{R}$ lies on one side of $l$, we may take $0 \le a$. By the method of cylindrical shells ([[§41 Volumes by Cylindrical Shells#^thm-41-2|Theorem §41.2]]),
>
> $$
> \begin{aligned}
> V &= \int_a^b 2\pi x\,[f(x) - g(x)]\,dx = 2\pi \int_a^b x\,[f(x) - g(x)]\,dx \\
> &= 2\pi\,(\bar x A) \qquad \text{(by Theorem §54.6)} \\
> &= (2\pi \bar x)\,A = A d ,
> \end{aligned}
> $$
>
> where $d = 2\pi \bar x$ is the distance traveled by the centroid, at distance $\bar x$ from the $y$-axis, during one rotation about the $y$-axis.

^pf-54-7

*Uses:* [[§54 Applications to Physics and Engineering#^thm-54-6|§54.6]], [[§41 Volumes by Cylindrical Shells#^thm-41-2|§41.2]] (shell method)

*Stewart proves only this special case. Any line $l$ can be made the $y$-axis by a choice of coordinates, so the proof covers every region that is bounded by two graphs over an interval in the direction perpendicular to $l$; a region that can be cut into finitely many such pieces follows by additivity of volumes and of moments.*

> [!example] Example §54.5: Volume of a Torus
> A torus is formed by rotating a circle of radius $r$ about a line in the plane of the circle at distance $R > r$ from the center of the circle. Find the volume of the torus.
>
> Rotate the disk bounded by the circle. Its area is $A = \pi r^2$. By the symmetry principle its centroid is its center, which travels around a circle of radius $R$, a distance $d = 2\pi R$. Since $R > r$, the disk lies on one side of the axis, and the Theorem of Pappus gives
>
> $$
> V = A d = (\pi r^2)(2\pi R) = 2\pi^2 r^2 R .
> $$
>
> Without Pappus one has to integrate, for instance by shells, $V = \int_{R - r}^{R + r} 2\pi x \cdot 2\sqrt{r^2 - (x - R)^2}\,dx$ (axis along the $y$-axis, center of the circle at $(R, 0)$). Stewart compares the method with his Exercise 6.2.75, which finds the volume by slicing ([[§40 Volumes|§40]]).
>
> *Stewart: Example 8.3.7*

^ex-54-5
