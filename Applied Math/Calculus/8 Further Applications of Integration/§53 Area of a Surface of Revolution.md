---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 53
stewart: "8.2"
aliases: ["Stewart 8.2"]
tags: [calculus]
---
← [[§52 Arc Length]] · ↑ [[· 8 Further Applications of Integration]] · [[§54 Applications to Physics and Engineering]] →

*Stewart, Section 8.2.*

A surface of revolution is formed when a curve is rotated about a line; it is the lateral boundary of a solid of revolution as in [[§40 Volumes|§40]] and [[§41 Volumes by Cylindrical Shells|§41]]. Its area should match intuition: painting it should take as much paint as a flat region of the same area. The section starts from cylinders and cones, whose areas come from unrolling them flat, and computes the area of a band (a frustum of a cone). As with arc length ([[§52 Arc Length|§52]]), the curve is replaced by an inscribed polygon. Rotating the polygon gives a stack of bands, and the limit of their total area is the integral $S = \int 2\pi y\,ds$. In words: circumference times arc length.

## Cylinders, Cones and Bands

> [!definition] Definition §53.1: Lateral Area of a Cylinder and a Cone
> The lateral surface area of a circular cylinder with radius $r$ and height $h$ is
>
> $$
> A = 2\pi r h ,
> $$
>
> and the lateral surface area of a circular cone with base radius $r$ and slant height $l$ is
>
> $$
> A = \pi r l .
> $$
>
> *Stewart: 8.2 (text)*

^def-53-1

> [!remark] Remark: Why These Values
> **Cylinder.** Cut the cylinder along a line parallel to its axis and unroll it: the result is a rectangle with sides $2\pi r$ (the circumference) and $h$, of area $2\pi r h$.
>
> **Cone.** Cut the cone along a slant line from the apex and flatten it. The result is a sector of a circle with radius $l$ whose arc is the base circle, of length $2\pi r$. So its central angle is $\theta = 2\pi r / l$. A sector of radius $l$ and angle $\theta$ has area $\frac12 l^2 \theta$ (Stewart, Exercise 7.3.41), so
>
> $$
> A = \tfrac12 l^2 \theta = \tfrac12 l^2 \left(\frac{2\pi r}{l}\right) = \pi r l .
> $$

^rem-53-1

> [!theorem] Theorem §53.1: Area of a Band
> A **band** (frustum of a cone) with slant height $l$ and upper and lower radii $r_1 < r_2$ has lateral area
>
> $$
> A = 2\pi r l, \qquad\text{where } r = \tfrac12 (r_1 + r_2)
> $$
>
> is the average radius of the band.
>
> *Stewart: 8.2, Equations 1 and 2*

^thm-53-1

> [!proof]+ Proof
> Complete the band to a cone by adding a small cone on top, with base radius $r_1$ and slant height $l_1$. The large cone then has base radius $r_2$ and slant height $l_1 + l$. The band is the large cone minus the small one, so by Definition §53.1
>
> $$
> A = \pi r_2 (l_1 + l) - \pi r_1 l_1 = \pi\big[(r_2 - r_1) l_1 + r_2 l\big] . \qquad (1)
> $$
>
> To eliminate $l_1$, cut both cones by a plane through the axis. The apex, the foot of the axis and a point of the rim form a right triangle, with legs $r_1$ (small cone) or $r_2$ (large cone) and hypotenuses $l_1$ or $l_1 + l$. The two triangles share the angle at the apex, so they are similar:
>
> $$
> \frac{l_1}{r_1} = \frac{l_1 + l}{r_2}, \qquad\text{so}\qquad r_2 l_1 = r_1 l_1 + r_1 l, \qquad\text{i.e.}\qquad (r_2 - r_1) l_1 = r_1 l .
> $$
>
> Putting this into (1) gives $A = \pi(r_1 l + r_2 l) = 2\pi \cdot \frac12(r_1 + r_2) \cdot l = 2\pi r l$.
>
> If $r_1 = r_2$ the band is a cylinder of height $l$, and $2\pi r l$ agrees with Definition §53.1.

^pf-53-1

*Uses:* [[§53 Area of a Surface of Revolution#^def-53-1|Def. §53.1]]

![[m233-53-1.svg]]
*A band is a large cone (slant height $l_1 + l$, radius $r_2$) with a small cone (dashed, slant height $l_1$, radius $r_1$) removed. Similar triangles through the axis link $l_1$ to $r_1$, $r_2$ and $l$, and the difference of the two cone areas becomes $2\pi$ times the average radius times the slant height.*

## The Surface Area Formula

> [!definition] Definition §53.2: Area of a Surface of Revolution
> Let $f$ be positive with a continuous derivative on $[a, b]$. The **surface area** of the surface obtained by rotating the curve $y = f(x)$, $a \le x \le b$, about the $x$-axis is
>
> $$
> S = \int_a^b 2\pi f(x) \sqrt{1 + [f'(x)]^2}\,dx ,
> $$
>
> in Leibniz notation
>
> $$
> S = \int_a^b 2\pi y \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx .
> $$
>
> *Stewart: 8.2, Equations 4 and 5*

^def-53-2

> [!remark] Remark: Why This Definition
> Follow the strategy used for arc length. Divide $[a, b]$ into $n$ subintervals with endpoints $x_0, \ldots, x_n$ and equal width $\Delta x$, and let $P_i = (x_i, y_i)$ with $y_i = f(x_i)$. Approximate the part of the surface between $x_{i-1}$ and $x_i$ by rotating the segment $P_{i-1} P_i$ about the $x$-axis. The result is a band with slant height $l = |P_{i-1} P_i|$ and average radius $r = \frac12 (y_{i-1} + y_i)$, so by Theorem §53.1 its area is
>
> $$
> 2\pi \, \frac{y_{i-1} + y_i}{2} \, |P_{i-1} P_i| .
> $$
>
> As in the proof of [[§52 Arc Length#^thm-52-1|Theorem §52.1]], $|P_{i-1} P_i| = \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x$ for some $x_i^*$ between $x_{i-1}$ and $x_i$. When $\Delta x$ is small, $y_i = f(x_i) \approx f(x_i^*)$ and $y_{i-1} = f(x_{i-1}) \approx f(x_i^*)$, since $f$ is continuous. So the band has area $\approx 2\pi f(x_i^*) \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x$, and the whole surface has area approximately
>
> $$
> \sum_{i=1}^n 2\pi f(x_i^*) \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x , \qquad (3)
> $$
>
> a Riemann sum for $g(x) = 2\pi f(x) \sqrt{1 + [f'(x)]^2}$. As $n \to \infty$ it tends to $\int_a^b g(x)\,dx$, which is the definition.
>
> Stewart only says that the approximation "appears to become better". Here is why the total band area has the same limit as (3). Let $M$ be the maximum of $|f'|$ and $K$ the maximum of $\sqrt{1 + [f'(x)]^2}$ on $[a, b]$; both exist because $f'$ is continuous. By the Mean Value Theorem $|f(u) - f(v)| \le M|u - v|$, so $\big|\frac12(y_{i-1} + y_i) - f(x_i^*)\big| \le M \Delta x$. The total band area therefore differs from (3) by at most
>
> $$
> \sum_{i=1}^n 2\pi \cdot M\Delta x \cdot K\,\Delta x = 2\pi M K (b - a)\,\Delta x \longrightarrow 0 .
> $$
>
> So the band areas of the inscribed polygons converge, and their limit is $S$.

^rem-53-2

![[m233-53-2.svg]]
*Rotating the curve $y = f(x)$ about the $x$-axis. The segment $P_{i-1} P_i$ of the inscribed polygon sweeps out a band (red) with radii $y_{i-1}$ and $y_i$ and slant height $|P_{i-1} P_i| = \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x$. By Theorem §53.1 its area is $2\pi \cdot \frac12(y_{i-1} + y_i) \cdot |P_{i-1} P_i|$, and adding the bands gives a Riemann sum for $\int_a^b 2\pi f(x) \sqrt{1 + [f'(x)]^2}\,dx$.*

> [!remark]- Connections
> - The surface is the parametrized surface $\mathbf{X}(x, \theta) = (x, f(x)\cos\theta, f(x)\sin\theta)$, $a \le x \le b$, $0 \le \theta \le 2\pi$. Here $\mathbf{X}_x = (1, f'\cos\theta, f'\sin\theta)$ and $\mathbf{X}_\theta = (0, -f\sin\theta, f\cos\theta)$, so $E = 1 + f'^2$, $F = 0$, $\tilde G = f^2$. The area element of [[§18 Surface Integrals#^thm-18-1|452 Thm. §18.1]] is $\sqrt{E\tilde G - F^2}\,dx\,d\theta = f\sqrt{1 + f'^2}\,dx\,d\theta$, and integrating over $\theta$ gives the integrand $2\pi f\sqrt{1 + f'^2}$ of Definition §53.2. In Calculus this general formula comes in [[§112 Parametric Surfaces and Their Areas|§112]].

> [!theorem] Theorem §53.2: Rotating a Curve x = g(y) About the x-Axis
> If the curve is described as $x = g(y)$, $c \le y \le d$, with $y \ge 0$ and $g'$ continuous, then the area of the surface obtained by rotating it about the $x$-axis is
>
> $$
> S = \int_c^d 2\pi y \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy .
> $$
>
> *Stewart: 8.2, Equation 6*

^thm-53-2

> [!proof]+ Proof
> Stewart states Equation 6 without comment. If the curve is not the graph of a function of $x$, Equation 6 is the definition. It comes from the argument of Remark: Why This Definition with the roles of $x$ and $y$ exchanged in the slant heights: divide $[c, d]$ into equal parts $\Delta y$, and note that the band from $P_{i-1}$ to $P_i$ has average radius exactly $\frac12(y_{i-1} + y_i)$ and slant height $\sqrt{1 + [g'(y_i^*)]^2}\,\Delta y$ ([[§52 Arc Length#^thm-52-2|Theorem §52.2]]).
>
> When the curve is also a graph $y = f(x)$, the two formulas agree. Suppose $g'(y) > 0$ for $c < y < d$, so $g$ is increasing from $a = g(c)$ to $b = g(d)$, with inverse $f$. For $a < x < b$ we have $f'(x) = 1/g'(y)$ where $y = f(x)$. The substitution $x = g(y)$, $dx = g'(y)\,dy$ gives, for small $\varepsilon > 0$,
>
> $$
> \int_{g(c + \varepsilon)}^{g(d - \varepsilon)} 2\pi f(x) \sqrt{1 + [f'(x)]^2}\,dx = \int_{c + \varepsilon}^{d - \varepsilon} 2\pi y \sqrt{1 + \frac{1}{[g'(y)]^2}}\; g'(y)\,dy = \int_{c + \varepsilon}^{d - \varepsilon} 2\pi y \sqrt{[g'(y)]^2 + 1}\,dy ,
> $$
>
> using $\sqrt{1 + 1/g'^2}\,g' = \sqrt{g'^2 + 1}$ for $g' > 0$. As $\varepsilon \to 0^+$ the right side tends to the integral in Equation 6, whose integrand is continuous on $[c, d]$. So the left side tends to the same value: it is Definition §53.2, an improper integral if $g'$ vanishes at an endpoint (where $f'$ is then unbounded, as in [[§53 Area of a Surface of Revolution#^ex-53-2|Example §53.2]]). If $g' < 0$ the same computation works with $|g'(y)|$ in place of $g'(y)$, the reversed limits of integration supplying the sign.

^pf-53-2

*Uses:* [[§53 Area of a Surface of Revolution#^def-53-2|Def. §53.2]], [[§53 Area of a Surface of Revolution#^thm-53-1|§53.1]], [[§52 Arc Length#^thm-52-2|§52.2]], [[§38 The Substitution Rule|§38]] (substitution in definite integrals), [[§51 Improper Integrals|§51]]

> [!theorem] Theorem §53.3: Surface Area as ∫ 2π(radius) ds
> For rotation about the $x$-axis, Equations 5 and 6 can both be written
>
> $$
> S = \int 2\pi y\,ds , \qquad (7)
> $$
>
> and for rotation about the $y$-axis (of a curve with $x \ge 0$) the surface area is
>
> $$
> S = \int 2\pi x\,ds . \qquad (8)
> $$
>
> In both, as in [[§52 Arc Length#^def-52-4|Definition §52.4]], one uses either
>
> $$
> ds = \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx \qquad\text{or}\qquad ds = \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy ,
> $$
>
> with the limits of integration in the corresponding variable.
>
> *Stewart: 8.2, Formulas 7 and 8*

^thm-53-3

> [!proof]+ Proof
> **Formula 7.** With the first $ds$, (7) is Definition §53.2 (Equation 5); with the second, it is Theorem §53.2 (Equation 6).
>
> **Formula 8.** *Stewart gives this as a sketch* ("a similar procedure"). Let the curve be $y = f(x)$, $a \le x \le b$, with $0 \le a$ and $f'$ continuous. Rotating the segment $P_{i-1} P_i$ about the $y$-axis gives a band with radii $x_{i-1}$ and $x_i$ and slant height $|P_{i-1} P_i|$. (If the segment is horizontal, the band is a flat ring, of area $\pi(x_i^2 - x_{i-1}^2) = 2\pi \cdot \frac12(x_{i-1} + x_i)(x_i - x_{i-1})$; so Theorem §53.1 still holds.) By Theorem §53.1 the band has area
>
> $$
> 2\pi \, \frac{x_{i-1} + x_i}{2} \, |P_{i-1} P_i| = 2\pi \, \frac{x_{i-1} + x_i}{2} \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x .
> $$
>
> Now $\big|\frac12(x_{i-1} + x_i) - x_i^*\big| \le \Delta x$, so exactly as in Remark: Why This Definition the total band area has the same limit as the Riemann sums $\sum 2\pi x_i^* \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x$, namely
>
> $$
> \int_a^b 2\pi x \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = \int 2\pi x\,ds .
> $$
>
> For a curve $x = g(y)$ the same argument with $[c, d]$ divided, or the substitution of the proof of Theorem §53.2, gives the form with $ds = \sqrt{1 + (dx/dy)^2}\,dy$.

^pf-53-3

*Uses:* [[§53 Area of a Surface of Revolution#^def-53-2|Def. §53.2]], [[§53 Area of a Surface of Revolution#^thm-53-1|§53.1]], [[§53 Area of a Surface of Revolution#^thm-53-2|§53.2]], [[§52 Arc Length#^thm-52-1|§52.1]], [[§52 Arc Length#^def-52-4|Def. §52.4]]

> [!remark] Remark: Circumference Times Arc Length
> Formulas 7 and 8 are easy to remember. As the point $(x, y)$ of the curve is rotated, it traces a circle whose radius is its distance from the axis: $y$ for the $x$-axis, $x$ for the $y$-axis. The integrand $2\pi y$ or $2\pi x$ is the circumference of that circle, and it is multiplied by the arc length element $ds$:
>
> $$
> S = \int \underbrace{2\pi \cdot \text{radius}}_{\text{circumference}} \, ds .
> $$
>
> Compare the volume by cylindrical shells, $V = \int 2\pi \cdot \text{radius} \cdot \text{height}\,dx$ ([[§41 Volumes by Cylindrical Shells|§41]]). The surface formula has $ds$ along the curve in place of the height times $dx$.

^rem-53-3

> [!remark] Remark: Method — Area of a Surface of Revolution
> 1. **Radius.** Identify the axis. The radius is the distance from $(x, y)$ to the axis: $y$ for the $x$-axis, $x$ for the $y$-axis, and $|y - c|$ for the line $y = c$. If $f$ changes sign, use $|f(x)|$ (Stewart, Exercise 46).
> 2. **Variable.** Choose $x$ or $y$ as the variable of integration, preferring the one whose derivative is continuous on the closed interval and gives a simpler $1 + (\text{derivative})^2$. The choice of variable is independent of the axis ([[§53 Area of a Surface of Revolution#^ex-53-3|Example §53.3]] does it both ways).
> 3. **Set up** $S = \int 2\pi \cdot \text{radius}\cdot ds$, with the radius, $ds$ and the limits all written in the chosen variable.
> 4. **Simplify.** For rotation about the $x$-axis the factor $y$ often cancels the square root ([[§53 Area of a Surface of Revolution#^ex-53-1|Example §53.1]]). Then integrate, or approximate numerically ([[§53 Area of a Surface of Revolution#^ex-53-4|Example §53.4]]).
> 5. **Check** against a cylinder or band with comparable dimensions (Example §53.3).

^rem-53-4

## Examples

> [!example] Example §53.1: A Zone of a Sphere
> The curve $y = \sqrt{4 - x^2}$, $-1 \le x \le 1$, is an arc of the circle $x^2 + y^2 = 4$. Find the area of the surface obtained by rotating this arc about the $x$-axis. (The surface is a portion of a sphere of radius $2$.)
>
> $$
> \frac{dy}{dx} = \tfrac12 (4 - x^2)^{-1/2}(-2x) = \frac{-x}{\sqrt{4 - x^2}} ,
> \qquad
> 1 + \left(\frac{dy}{dx}\right)^2 = 1 + \frac{x^2}{4 - x^2} = \frac{4 - x^2 + x^2}{4 - x^2} = \frac{4}{4 - x^2} .
> $$
>
> By Formula 7 with $ds = \sqrt{1 + (dy/dx)^2}\,dx$ (that is, Definition §53.2),
>
> $$
> S = \int_{-1}^{1} 2\pi y \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = 2\pi \int_{-1}^{1} \sqrt{4 - x^2}\,\frac{2}{\sqrt{4 - x^2}}\,dx = 4\pi \int_{-1}^{1} 1\,dx = 4\pi(2) = 8\pi .
> $$
>
> The radius $y = \sqrt{4 - x^2}$ cancels the square root exactly. The same cancellation for a sphere of radius $R$ cut by two parallel planes a distance $h$ apart gives $2\pi R h$, which depends only on $h$ (Stewart, Exercise 42). Here $R = 2$, $h = 2$ and $2\pi \cdot 2 \cdot 2 = 8\pi$.
>
> *Stewart: Example 8.2.1*

^ex-53-1

> [!example] Example §53.2: Integrating with Respect to y
> The portion of the curve $x = \frac23 y^{3/2}$ between $y = 0$ and $y = 3$ is rotated about the $x$-axis. Find the area of the resulting surface.
>
> Since $x$ is given as a function of $y$, use $y$ as the variable of integration. (As a function of $x$, $y = (\frac32 x)^{2/3}$ has an unbounded derivative at $x = 0$.) Here $dx/dy = y^{1/2}$, so by Formula 7 with $ds = \sqrt{1 + (dx/dy)^2}\,dy$ (Theorem §53.2),
>
> $$
> S = \int_0^3 2\pi y \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy = 2\pi \int_0^3 y \sqrt{1 + (y^{1/2})^2}\,dy = 2\pi \int_0^3 y \sqrt{1 + y}\,dy .
> $$
>
> Substitute $u = 1 + y$, $du = dy$, so $y = u - 1$; the limits become $u = 1$ and $u = 4$:
>
> $$
> \begin{aligned}
> S &= 2\pi \int_1^4 (u - 1)\sqrt{u}\,du = 2\pi \int_1^4 \big(u^{3/2} - u^{1/2}\big)\,du = 2\pi \Big[\tfrac25 u^{5/2} - \tfrac23 u^{3/2}\Big]_1^4 \\
> &= 2\pi \left[\left(\frac{64}{5} - \frac{16}{3}\right) - \left(\frac25 - \frac23\right)\right] = 2\pi \left[\frac{112}{15} + \frac{4}{15}\right] = 2\pi \cdot \frac{116}{15} = \frac{232}{15}\pi \approx 48.59 .
> \end{aligned}
> $$
>
> *Stewart: Example 8.2.2*

^ex-53-2

> [!example] Example §53.3: A Parabola Rotated About the y-Axis, Two Ways
> The arc of the parabola $y = x^2$ from $(1, 1)$ to $(2, 4)$ is rotated about the $y$-axis. Find the area of the resulting surface.
>
> **Solution 1 (in $x$).** $y = x^2$ and $dy/dx = 2x$. Formula 8 with $ds = \sqrt{1 + (dy/dx)^2}\,dx$ gives
>
> $$
> S = \int 2\pi x\,ds = \int_1^2 2\pi x \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = 2\pi \int_1^2 x \sqrt{1 + 4x^2}\,dx .
> $$
>
> Substitute $u = 1 + 4x^2$, $du = 8x\,dx$; the limits become $u = 5$ and $u = 17$:
>
> $$
> S = 2\pi \int_5^{17} \sqrt{u} \cdot \tfrac18\,du = \frac{\pi}{4} \int_5^{17} u^{1/2}\,du = \frac{\pi}{4} \Big[\tfrac23 u^{3/2}\Big]_5^{17} = \frac{\pi}{6}\big(17\sqrt{17} - 5\sqrt5\big) .
> $$
>
> **Solution 2 (in $y$).** $x = \sqrt{y}$, $1 \le y \le 4$, and $dx/dy = \dfrac{1}{2\sqrt{y}}$. Formula 8 with $ds = \sqrt{1 + (dx/dy)^2}\,dy$ gives
>
> $$
> \begin{aligned}
> S &= \int_1^4 2\pi x \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy = 2\pi \int_1^4 \sqrt{y} \sqrt{1 + \frac{1}{4y}}\,dy = 2\pi \int_1^4 \sqrt{y + \tfrac14}\,dy \\
> &= 2\pi \int_1^4 \sqrt{\tfrac14 (4y + 1)}\,dy = \pi \int_1^4 \sqrt{4y + 1}\,dy = \frac{\pi}{4} \int_5^{17} \sqrt{u}\,du \quad (u = 1 + 4y) \\
> &= \frac{\pi}{6}\big(17\sqrt{17} - 5\sqrt5\big) ,
> \end{aligned}
> $$
>
> as in Solution 1.
>
> **Check.** $S \approx \frac{\pi}{6}(70.093 - 11.180) \approx 30.85$. A cylinder of the same height $3$ and radius $1.5$, halfway between the upper and lower radii, has lateral area $2\pi(1.5)(3) \approx 28.27$. The band with the same top and bottom circles has slant height $\sqrt{1^2 + 3^2} = \sqrt{10}$ and, by Theorem §53.1, area $2\pi(1.5)\sqrt{10} \approx 29.80$. The surface should be slightly larger than that band, since the arc $x = \sqrt{y}$ bulges away from the axis beyond its chord and is longer than it, and it is.
>
> *Stewart: Example 8.2.3*

^ex-53-3

> [!example] Example §53.4: A Numerical Surface Area
> Set up an integral for the area of the surface generated by rotating the curve $y = e^x$, $0 \le x \le 1$, about the $x$-axis. Then evaluate it numerically, correct to three decimal places.
>
> $y = e^x$ and $dy/dx = e^x$, so by Formula 7 with $ds = \sqrt{1 + (dy/dx)^2}\,dx$,
>
> $$
> S = \int_0^1 2\pi y \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = 2\pi \int_0^1 e^x \sqrt{1 + e^{2x}}\,dx \approx 22.943
> $$
>
> by a calculator or computer. (Alternatively, use Formula 7 with $x = \ln y$, $1 \le y \le e$, and $ds = \sqrt{1 + (dx/dy)^2}\,dy$.)
>
> **Exact value** (not in Stewart). The substitution $u = e^x$, $du = e^x\,dx$, and entry 21 of the Table of Integrals, $\int \sqrt{1 + u^2}\,du = \frac{u}{2}\sqrt{1 + u^2} + \frac12 \ln\big(u + \sqrt{1 + u^2}\big) + C$, give
>
> $$
> S = 2\pi \int_1^e \sqrt{1 + u^2}\,du = \pi\Big[e\sqrt{1 + e^2} + \ln\big(e + \sqrt{1 + e^2}\big) - \sqrt2 - \ln\big(1 + \sqrt2\big)\Big] \approx 22.943 .
> $$
>
> *Stewart: Example 8.2.4*

^ex-53-4
