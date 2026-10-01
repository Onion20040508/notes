---
type: section
subject: "[[Calculus]]"
chapter: 6
section: 41
stewart: "6.3"
aliases: ["Stewart 6.3"]
tags: [calculus]
---
← [[§40 Volumes]] · ↑ [[· 6 Applications of Integration]] · [[§42 Work]] →

*Stewart, Section 6.3.*

Rotating the region under $y = 2x^2 - x^3$ about the $y$-axis produces a solid whose washers ([[§40 Volumes|§40]]) would require solving a cubic for $x$ in terms of $y$. The method of cylindrical shells avoids this. It cuts the region into strips *parallel* to the axis of rotation; each strip sweeps out a thin cylindrical shell of volume about $2\pi x\,f(x)\,\Delta x$ (circumference times height times thickness), and adding the shells gives $V = \int_a^b 2\pi x f(x)\,dx$. The section ends with how to choose between washers and shells.

## The Method of Cylindrical Shells

> [!theorem] Theorem §41.1: Volume of a Cylindrical Shell
> A cylindrical shell with inner radius $r_1$, outer radius $r_2$ and height $h$ has volume
>
> $$
> V = 2\pi r h\,\Delta r ,
> $$
>
> where $\Delta r = r_2 - r_1$ is the thickness of the shell and $r = \frac12 (r_1 + r_2)$ its average radius. It can be remembered as
>
> $$
> V = [\text{circumference}]\,[\text{height}]\,[\text{thickness}] .
> $$
>
> *Stewart: 6.3, Formula 1*

^thm-41-1

> [!proof]+ Proof
> Subtract the volume $V_1$ of the inner cylinder from the volume $V_2$ of the outer cylinder ([[§40 Volumes#^def-40-1|Definition §40.1]]):
>
> $$
> V = V_2 - V_1 = \pi r_2^2 h - \pi r_1^2 h = \pi (r_2^2 - r_1^2) h = \pi (r_2 + r_1)(r_2 - r_1) h = 2\pi\,\frac{r_2 + r_1}{2}\,h\,(r_2 - r_1) = 2\pi r h\,\Delta r .
> $$

^pf-41-1

*Uses:* [[§40 Volumes#^def-40-1|Def. §40.1]]

Now let $S$ be the solid obtained by rotating about the $y$-axis the region bounded by $y = f(x)$ (where $f(x) \ge 0$), $y = 0$, $x = a$ and $x = b$, where $b > a \ge 0$.

> [!theorem] Theorem §41.2: The Shell Method
> The volume of the solid obtained by rotating about the $y$-axis the region under the curve $y = f(x)$ from $a$ to $b$ is
>
> $$
> V = \int_a^b 2\pi x f(x)\,dx , \qquad\text{where } 0 \le a < b .
> $$
>
> To remember it, think of a typical shell, cut and flattened, with radius $x$, circumference $2\pi x$, height $f(x)$ and thickness $\Delta x$ or $dx$:
>
> $$
> V = \int_a^b \underbrace{(2\pi x)}_{\text{circumference}}\ \underbrace{[f(x)]}_{\text{height}}\ \underbrace{dx}_{\text{thickness}} .
> $$
>
> *Stewart: 6.3, Formula 2*

^thm-41-2

> [!remark] Remark: Why It Works
> Divide $[a, b]$ into $n$ subintervals $[x_{i-1}, x_i]$ of equal width $\Delta x$, and let $\bar x_i$ be the midpoint of the $i$th one. Rotating the rectangle with base $[x_{i-1}, x_i]$ and height $f(\bar x_i)$ about the $y$-axis gives a cylindrical shell with average radius $\bar x_i$, height $f(\bar x_i)$ and thickness $\Delta x$. By Theorem §41.1 its volume is
>
> $$
> V_i = (2\pi \bar x_i)\,[f(\bar x_i)]\,\Delta x ,
> \qquad\text{so}\qquad
> V \approx \sum_{i=1}^{n} V_i = \sum_{i=1}^{n} 2\pi \bar x_i f(\bar x_i)\,\Delta x .
> $$
>
> The approximation improves as $n \to \infty$, and by the definition of the integral the right side tends to $\int_a^b 2\pi x f(x)\,dx$. This makes the formula plausible. It does not prove it, because volume was *defined* by slicing perpendicular to an axis ([[§40 Volumes#^def-40-2|Definition §40.2]]), not by shells.

^rem-41-1

> [!proof]- Proof
> *Stewart proves the formula only later, in Exercise 7.1.81, by integration by parts ([[§44 Integration by Parts|§44]]), for $f$ one-to-one. Here is that argument, for $f$ increasing with a continuous derivative.* Let $c = f(a)$, $d = f(b)$, and let $g = f^{-1}$, so $x = g(y)$ for $c \le y \le d$.
>
> **Slicing.** Slice the solid perpendicular to the $y$-axis ([[§40 Volumes#^def-40-2|Definition §40.2]]). At height $y$ with $0 \le y \le c$, the cross-section is a washer with radii $a$ and $b$. At height $y$ with $c \le y \le d$, the region extends from $x = g(y)$ to $x = b$, so the cross-section is a washer with radii $g(y)$ and $b$. Hence
>
> $$
> V = \int_0^c \pi (b^2 - a^2)\,dy + \int_c^d \pi \big(b^2 - [g(y)]^2\big)\,dy = \pi b^2 d - \pi a^2 c - \int_c^d \pi [g(y)]^2\,dy .
> $$
>
> **Substitution.** In the last integral put $y = f(x)$, so $dy = f'(x)\,dx$, $g(f(x)) = x$, and $y = c, d$ correspond to $x = a, b$ ([[§38 The Substitution Rule#^thm-38-3|Theorem §38.3]]):
>
> $$
> \int_c^d [g(y)]^2\,dy = \int_a^b x^2 f'(x)\,dx .
> $$
>
> **Integration by parts** with $u = x^2$, $dv = f'(x)\,dx$:
>
> $$
> \int_a^b x^2 f'(x)\,dx = x^2 f(x) \Big]_a^b - \int_a^b 2x f(x)\,dx = b^2 d - a^2 c - \int_a^b 2x f(x)\,dx .
> $$
>
> **Conclusion.** Substituting back,
>
> $$
> V = \pi b^2 d - \pi a^2 c - \pi \Big(b^2 d - a^2 c - \int_a^b 2x f(x)\,dx\Big) = \int_a^b 2\pi x f(x)\,dx .
> $$
>
> For a decreasing $f$ the same computation works with the roles of the washers' radii adjusted, and a general $f$ is cut into monotone pieces. The cleanest general proof is a triple integral in cylindrical coordinates (below).

^pf-41-2

*Uses:* [[§40 Volumes#^def-40-2|Def. §40.2]], [[§38 The Substitution Rule#^thm-38-3|§38.3]], [[§44 Integration by Parts|§44]] (integration by parts)

![[m233-41-1.svg]]
*The shell method on Example §41.1. (a) A thin strip at distance $x$ from the $y$-axis, of height $f(x)$ and width $\Delta x$, sweeps out a cylindrical shell when rotated about the axis. (b) Cut along a vertical line and flattened, the shell is nearly a slab of length $2\pi x$ (its circumference), height $f(x)$ and thickness $\Delta x$, with volume $2\pi x f(x)\,\Delta x$.*

> [!remark]- Connections
> - The general proof: in cylindrical coordinates the solid is $\{0 \le z \le f(r),\ a \le r \le b\}$, and its volume $\int_0^{2\pi} \int_a^b \int_0^{f(r)} r\,dz\,dr\,d\theta = \int_a^b 2\pi r f(r)\,dr$ ([[§104 Triple Integrals in Cylindrical Coordinates|§104]]). The factor $r$ is the Jacobian of the change of variables, [[§15 Multivariable Integration#^thm-15-20|452 Thm. §15.20]].

> [!remark] Remark: Method — Cylindrical Shells
> 1. Sketch the region and a typical strip **parallel** to the axis of rotation; rotated, it sweeps out a shell.
> 2. **Radius** = the distance from the strip to the axis: $x$ for the $y$-axis, $|x - h|$ for the line $x = h$, $y$ for the $x$-axis.
> 3. **Height** = the length of the strip: $f(x)$, or top minus bottom $y_T - y_B$, or right minus left $x_R - x_L$ for horizontal strips.
> 4. **Thickness** = $dx$ for a vertical axis, $dy$ for a horizontal one.
> 5. $V = \int 2\pi\,(\text{radius})(\text{height})\,(\text{thickness})$ over the range of the strips.

^rem-41-2

> [!example] Example §41.1: A Cubic Rotated About the y-Axis
> Find the volume of the solid obtained by rotating about the $y$-axis the region bounded by $y = 2x^2 - x^3$ and $y = 0$.
>
> $2x^2 - x^3 = x^2(2 - x)$ is $\ge 0$ for $0 \le x \le 2$, so the region lies over $[0, 2]$. A typical shell has radius $x$, circumference $2\pi x$ and height $f(x) = 2x^2 - x^3$. By Theorem §41.2,
>
> $$
> V = \int_0^2 (2\pi x)(2x^2 - x^3)\,dx = 2\pi \int_0^2 (2x^3 - x^4)\,dx = 2\pi \Big[\tfrac12 x^4 - \tfrac15 x^5\Big]_0^2 = 2\pi \Big(8 - \frac{32}{5}\Big) = \frac{16}{5}\pi .
> $$
>
> With washers we would have had to find the local maximum of the curve (at $x = \frac43$) and solve the cubic $y = 2x^2 - x^3$ for $x$ in terms of $y$, in two branches. Slicing gives the same answer, but shells are far easier here.
>
> *Stewart: Example 6.3.1 and Note*

^ex-41-1

> [!example] Example §41.2: Shells Between Two Curves
> Find the volume of the solid obtained by rotating about the $y$-axis the region between $y = x$ and $y = x^2$.
>
> The curves meet at $x = 0$ and $x = 1$, and $x \ge x^2$ in between. A shell at $x$ has radius $x$, circumference $2\pi x$ and height $x - x^2$ (top minus bottom). So
>
> $$
> V = \int_0^1 (2\pi x)(x - x^2)\,dx = 2\pi \int_0^1 (x^2 - x^3)\,dx = 2\pi \Big[\frac{x^3}{3} - \frac{x^4}{4}\Big]_0^1 = \frac{\pi}{6} .
> $$
>
> *Stewart: Example 6.3.2*

^ex-41-2

> [!example] Example §41.3: Shells About the x-Axis
> Use cylindrical shells to find the volume of the solid obtained by rotating about the $x$-axis the region under $y = \sqrt{x}$ from $0$ to $1$.
>
> This was done with disks in [[§40 Volumes#^ex-40-2|Example §40.2]](a). For shells about the $x$-axis, use horizontal strips: write the curve as $x = y^2$, $0 \le y \le 1$. The strip at height $y$ runs from $x = y^2$ to $x = 1$, so the shell has radius $y$, circumference $2\pi y$ and height $1 - y^2$:
>
> $$
> V = \int_0^1 (2\pi y)(1 - y^2)\,dy = 2\pi \int_0^1 (y - y^3)\,dy = 2\pi \Big[\frac{y^2}{2} - \frac{y^4}{4}\Big]_0^1 = \frac{\pi}{2} ,
> $$
>
> in agreement with the disk method, which was simpler for this problem.
>
> *Stewart: Example 6.3.3*

^ex-41-3

> [!example] Example §41.4: Shells About the Line x = 2
> Find the volume of the solid obtained by rotating the region bounded by $y = x - x^2$ and $y = 0$ about the line $x = 2$.
>
> The region lies over $[0, 1]$, to the left of the axis. A shell at $x$ has radius $2 - x$ (the distance to the line $x = 2$), circumference $2\pi(2 - x)$ and height $x - x^2$. So
>
> $$
> V = \int_0^1 2\pi (2 - x)(x - x^2)\,dx = 2\pi \int_0^1 (x^3 - 3x^2 + 2x)\,dx = 2\pi \Big[\frac{x^4}{4} - x^3 + x^2\Big]_0^1 = 2\pi \cdot \frac14 = \frac{\pi}{2} .
> $$
>
> *Stewart: Example 6.3.4*

^ex-41-4

## Disks and Washers Versus Cylindrical Shells

> [!remark] Remark: Method — Choosing Between Washers and Shells
> 1. Decide which variable is easier to work with. Is the region more easily described by top and bottom curves $y = f(x)$, or by left and right curves $x = g(y)$? Are the limits of integration easier to find in one variable? Does one variable need two separate integrals and the other only one? Can the resulting integral actually be evaluated?
> 2. The variable dictates the method. Draw a sample rectangle in the region; its thickness, $\Delta x$ or $\Delta y$, is the variable of integration. Revolved about the axis, the rectangle becomes a disk or washer if it is perpendicular to the axis, and a shell if it is parallel to it.
> 3. Sometimes both methods work (Example §41.5).

^rem-41-3

> [!example] Example §41.5: The Same Solid Both Ways
> The region in the first quadrant bounded by $y = x^2$ and $y = 2x$ (which meet at $(0, 0)$ and $(2, 4)$) is rotated about the line $x = -1$. Find the volume using (a) $x$ and (b) $y$ as the variable of integration.
>
> **(a) Shells.** A vertical rectangle at $x$, $0 \le x \le 2$, runs from $y = x^2$ up to $y = 2x$. Rotated about $x = -1$ it gives a shell with radius $x + 1$ and height $2x - x^2$:
>
> $$
> V = \int_0^2 2\pi (x + 1)(2x - x^2)\,dx = 2\pi \int_0^2 (x^2 + 2x - x^3)\,dx = 2\pi \Big[\frac{x^3}{3} + x^2 - \frac{x^4}{4}\Big]_0^2 = 2\pi \Big(\frac83 + 4 - 4\Big) = \frac{16\pi}{3} .
> $$
>
> **(b) Washers.** A horizontal rectangle at height $y$, $0 \le y \le 4$, runs from $x = \frac12 y$ (the line) to $x = \sqrt{y}$ (the parabola). Rotated about $x = -1$ it gives a washer with inner radius $\frac12 y + 1$ and outer radius $\sqrt{y} + 1$:
>
> $$
> V = \int_0^4 \Big[\pi (\sqrt{y} + 1)^2 - \pi \big(\tfrac12 y + 1\big)^2\Big]\,dy = \pi \int_0^4 \big(2\sqrt{y} - \tfrac14 y^2\big)\,dy = \pi \Big[\tfrac43 y^{3/2} - \tfrac{1}{12} y^3\Big]_0^4 = \pi \Big(\frac{32}{3} - \frac{16}{3}\Big) = \frac{16\pi}{3} .
> $$
>
> *Stewart: Example 6.3.5*

^ex-41-5
