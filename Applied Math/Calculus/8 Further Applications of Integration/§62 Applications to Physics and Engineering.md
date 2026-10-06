---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 62
stewart: "8.3"
aliases: ["Stewart 8.3"]
tags: [calculus]
---
← [[§61 Area of a Surface of Revolution]] · ↑ [[· 8 Further Applications of Integration]] · [[§63 Moments and Centers of Mass]] →

*Stewart, Section 8.3.*

Two physical quantities are computed here by the same strategy as areas, volumes and work ([[§48 Work|§48]]): cut the object into thin pieces, approximate the quantity on each piece, add (a Riemann sum), and pass to the limit. The first is the force that water exerts on a vertical dam or plate, where the pressure grows with depth. The second is the center of mass of a thin plate, the point where it balances; for a plate of uniform density it depends only on the shape and is called the centroid. The section ends with the Theorem of Pappus, which turns a centroid into the volume of a solid of revolution.

## Hydrostatic Pressure and Force

> [!definition] Definition §62.1: Pressure
> The **pressure** $P$ on a surface is the force per unit area:
>
> $$
> P = \frac{F}{A} .
> $$
>
> The SI unit is the newton per square meter, called a **pascal**: $1\ \text{N/m}^2 = 1\ \text{Pa}$; the kilopascal ($1\ \text{kPa} = 1000\ \text{Pa}$) is often more convenient. For a fluid of (mass) density $\rho$, the **weight density** is $\delta = \rho g$, where $g$ is the acceleration due to gravity. Water has $\rho = 1000\ \text{kg/m}^3$ and, in US Customary units, $\delta = 62.5\ \text{lb/ft}^3$.
>
> *Stewart: 8.3 (text)*

^def-62-1

> [!theorem] Theorem §62.1: Hydrostatic Pressure
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

^thm-62-1

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

^pf-62-1

*Uses:* [[§62 Applications to Physics and Engineering#^def-62-1|Def. §62.1]]

The pressure on a *vertical* plate is not constant: it increases with depth. That is why the force on a dam needs an integral.

> [!theorem] Theorem §62.2: Hydrostatic Force on a Vertical Plate
> A plate is submerged vertically in a fluid of weight density $\delta = \rho g$. Measure depth by an $x$-axis pointing down, with origin at the surface of the fluid. Suppose the plate extends from depth $a$ to depth $b$ ($0 \le a < b$) and its width at depth $x$ is $w(x)$, with $w$ continuous. Then the hydrostatic force (the force exerted by the fluid at rest) on one side of the plate is
>
> $$
> F = \int_a^b \delta\, x\, w(x)\,dx = \int_a^b \rho g\, x\, w(x)\,dx .
> $$
>
> In words: integrate pressure $\times$ (area of a horizontal strip), where the pressure is that at the depth of the strip.
>
> *Stewart: 8.3 (text and Examples 1–2); the general formula is Exercise 18*

^thm-62-2

> [!proof]+ Proof
> **Stewart's argument.** Divide $[a, b]$ into $n$ subintervals of length $\Delta x$ with endpoints $x_i$, and choose $x_i^{\ast} \in [x_{i-1}, x_i]$. The $i$th horizontal strip of the plate is approximately a rectangle of height $\Delta x$ and width $w(x_i^{\ast})$, so its area is $A_i \approx w(x_i^{\ast})\,\Delta x$. If $\Delta x$ is small, the pressure on the strip is almost constant, $P_i \approx \delta x_i^{\ast}$ by [[§62 Applications to Physics and Engineering#^thm-62-1|Theorem §62.1]], and the force on it is $F_i = P_i A_i \approx \delta x_i^{\ast} w(x_i^{\ast})\,\Delta x$. Adding,
>
> $$
> F = \sum_{i=1}^n F_i \approx \sum_{i=1}^n \delta x_i^* w(x_i^*)\,\Delta x \;\longrightarrow\; \int_a^b \delta x\, w(x)\,dx \qquad (n \to \infty).
> $$
>
> **Making the "$\approx$" precise.** The exact area of the $i$th strip is $A_i = \int_{x_{i-1}}^{x_i} w(x)\,dx$ ([[§45 Areas Between Curves#^thm-45-3|Theorem §45.3]], with the vertical depth as the variable). Every point of the strip has depth between $x_{i-1}$ and $x_i$, so the pressure there lies between $\delta x_{i-1}$ and $\delta x_i$, and the force on the strip (pressure acting on area, all perpendicular to the plate) satisfies
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

^pf-62-2

*Uses:* [[§62 Applications to Physics and Engineering#^thm-62-1|§62.1]], [[§39 The Definite Integral#^def-39-1|Def. §39.1]] (Riemann sums), [[§40 Properties of the Definite Integral#^thm-40-2|§40.2]] (additivity over adjacent intervals), [[§40 Properties of the Definite Integral#^thm-40-3|§40.3]] (comparison properties), [[§45 Areas Between Curves#^thm-45-3|§45.3]] (area as an integral of width)

![[m233-54-1.svg]]
*The dam of [[§62 Applications to Physics and Engineering#^ex-62-1|Example §62.1]]. With depth $x$ measured down from the water surface, the horizontal strip at depth $x$ (red) has width $w(x) = 2(15 + a)$, where similar triangles give $a / (16 - x) = 10/20$ (green). The pressure on the strip is about $\rho g x$, so it carries a force of about $\rho g x\,w(x)\,\Delta x$.*

> [!remark]- Connections
> - The proof is a Darboux–Stieltjes argument: with the cumulative area $A(x) = \int_a^x w$ as weight, $L_n$ and $U_n$ are the lower and upper sums of $\delta x$ with respect to $A$, so $F = \int_a^b \delta x\,dA(x)$ in the sense of [[§35 Riemann–Stieltjes Integrals#^def-35-1|451 Def. §35.1]].

> [!remark] Remark: Method — Hydrostatic Force
> 1. **Coordinates.** Choose an axis for depth. A vertical $x$-axis pointing down from the surface makes the depth simply $x$ ([[§62 Applications to Physics and Engineering#^ex-62-1|Example §62.1]]). Any other choice works if the depth is written correctly: with the origin at the bottom of the dam and $y$ up, depth is $16 - y$; with the origin at the center of a circular plate whose center is $7$ ft below the surface, depth is $7 - y$.
> 2. **Width.** Find the width of a horizontal strip as a function of the depth variable, from the equation of the edge or from similar triangles.
> 3. **Force on a strip.** Pressure $\times$ area: $\delta \cdot (\text{depth}) \cdot (\text{width}) \cdot \Delta x$. Use $\rho g$ with $\rho$ in $\text{kg/m}^3$ in SI units, and $\delta$ in $\text{lb/ft}^3$ in US units.
> 4. **Integrate** over the depths where the plate is under the fluid; a plate sticking out of the fluid is cut off at the surface.
> 5. **Evaluate** using symmetry where possible. In Stewart's Example 8.3.2 (the end of a drum of radius $3$ ft, center $7$ ft deep), $F = 125 \int_{-3}^{3} (7 - y)\sqrt{9 - y^2}\,dy$; the part $\int_{-3}^3 y\sqrt{9 - y^2}\,dy$ is $0$ because the integrand is odd ([[§43 The Substitution Rule#^thm-43-4|Theorem §43.4]]), and $\int_{-3}^3 \sqrt{9 - y^2}\,dy = \frac12 \pi (3)^2$ is the area of a half-disk, so $F = 875 \cdot \frac92 \pi = \frac{7875\pi}{2} \approx 12{,}370$ lb.

^rem-62-1

> [!example] Example §62.1: Force on a Trapezoidal Dam
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
> **Force.** By [[§62 Applications to Physics and Engineering#^thm-62-2|Theorem §62.2]] with $\rho = 1000\ \text{kg/m}^3$ and $g = 9.8\ \text{m/s}^2$,
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

^ex-62-1

*Continued in [[§63 Moments and Centers of Mass]]: moments, centers of mass, centroids and the Theorem of Pappus.*
