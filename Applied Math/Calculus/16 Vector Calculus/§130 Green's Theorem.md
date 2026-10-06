---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 130
stewart: "16.4"
aliases: ["Stewart 16.4"]
tags: [calculus, math233]
---
← [[§129 Conservative Vector Fields and Potential Functions]] · ↑ [[· 16 Vector Calculus]] · [[§131 Extended Versions of Green's Theorem]] →

*Stewart, Section 16.4 · MATH 233 (UMass, Spring 2023): Practice Final Exam (Q2), Chapter 16 Review (Q6(a)).*

Green's Theorem turns a line integral around a [[§129 Conservative Vector Fields and Potential Functions#^def-129-1|simple closed curve]] $C$ into a double integral over the region $D$ that $C$ bounds. It is the Fundamental Theorem of Calculus one dimension up: an integral of derivatives over $D$ equals boundary values of the original functions, integrated over $\partial D$. It is used in both directions. A line integral that would need several parametrizations becomes one double integral, and an area becomes a line integral around the boundary. Cutting regions into pieces extends it to regions with holes. That gives the standard calculation for fields with a singularity, such as $(-y\,\mathbf{i} + x\,\mathbf{j})/(x^2 + y^2)$, and the proof of the test for conservative fields announced in [[§128 The Fundamental Theorem for Line Integrals|§128]] (the converse of [[§129 Conservative Vector Fields and Potential Functions#^thm-129-1|Theorem §129.1]]).

## Green's Theorem

> [!definition] Definition §130.1: Positive Orientation
> Let $C$ be a simple closed curve and $D$ the region bounded by $C$, consisting of all points inside $C$ together with the points of $C$. The **positive orientation** of $C$ is a single *counterclockwise* traversal of $C$. Equivalently, if $C$ is given by $\mathbf{r}(t)$, $a \le t \le b$, then the region $D$ is always on the left as the point $\mathbf{r}(t)$ traverses $C$.
>
> **Notation.** $\displaystyle\oint_C P\,dx + Q\,dy$ indicates that the line integral is taken in the positive direction (Stewart also puts a counterclockwise arrow on the circle). The positively oriented boundary curve of $D$ is written $\partial D$.
>
> *Stewart: 16.4 (text)*

^def-130-1

> [!definition] Definition §130.2: Simple Region
> A plane region is **simple** if it is both of type I and of type II ([[§116 Double Integrals Over General Regions#^def-116-2|Definition §116.2]], [[§116 Double Integrals Over General Regions#^def-116-3|Definition §116.3]]). That is, it can be written both as
>
> $$
> D = \{(x, y) \mid a \le x \le b,\ g_1(x) \le y \le g_2(x)\}
> \quad\text{and as}\quad
> D = \{(x, y) \mid c \le y \le d,\ h_1(y) \le x \le h_2(y)\}
> $$
>
> with continuous functions $g_1 \le g_2$ and $h_1 \le h_2$.
>
> *Stewart: 16.4 (text)*

^def-130-2

> [!theorem] Theorem §130.1: Green's Theorem
> Let $C$ be a positively oriented, piecewise-smooth, simple closed curve in the plane and let $D$ be the region bounded by $C$. If $P$ and $Q$ have continuous partial derivatives on an open region that contains $D$, then
>
> $$
> \oint_C P\,dx + Q\,dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA .
> $$
>
> In the notation of [[§130 Green's Theorem#^def-130-1|Definition §130.1]]:
>
> $$
> \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \oint_{\partial D} P\,dx + Q\,dy .
> $$
>
> The left side of the first equation is $\oint_C \mathbf{F} \cdot d\mathbf{r}$ for $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ ([[§127 Line Integrals of Vector Fields#^thm-127-2|Theorem §127.2]]).
>
> *Stewart: 16.4, Green's Theorem and Equation 1*

^thm-130-1

Green's Theorem is not easy to prove in general. Stewart proves it for simple regions ([[§130 Green's Theorem#^def-130-2|Def. §130.2]]: both type I and type II), and then extends it by cutting.

> [!proof]+ Proof
> We prove the theorem when $D$ is a simple region. It suffices to prove the two equations
>
> $$
> \oint_C P\,dx = -\iint_D \frac{\partial P}{\partial y}\,dA \qquad (2)
> \qquad\qquad
> \oint_C Q\,dy = \iint_D \frac{\partial Q}{\partial x}\,dA \qquad (3)
> $$
>
> and add them.
>
> **Equation 2.** Write $D$ as a type I region, $D = \{(x, y) \mid a \le x \le b,\ g_1(x) \le y \le g_2(x)\}$. Computing the double integral as an iterated integral, and the inner integral by the Fundamental Theorem of Calculus in $y$ (with $x$ fixed),
>
> $$
> \iint_D \frac{\partial P}{\partial y}\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} \frac{\partial P}{\partial y}(x, y)\,dy\,dx = \int_a^b \big[ P(x, g_2(x)) - P(x, g_1(x)) \big]\,dx . \qquad (4)
> $$
>
> Now compute the left side of (2). Break $C$ into four curves: $C_1$ along the bottom $y = g_1(x)$ from left to right, $C_2$ up the vertical line $x = b$, $C_3$ along the top $y = g_2(x)$ from right to left, and $C_4$ down the vertical line $x = a$. $C_2$ or $C_4$ may reduce to a single point.
> - On $C_1$, take $x$ as the parameter: $x = x$, $y = g_1(x)$, $a \le x \le b$. So $\displaystyle\int_{C_1} P(x, y)\,dx = \int_a^b P(x, g_1(x))\,dx$.
> - $C_3$ runs from right to left, so $-C_3$ runs from left to right and has parametric equations $x = x$, $y = g_2(x)$, $a \le x \le b$. Reversing a curve changes the sign of a line integral, so
>
> $$
> \int_{C_3} P(x, y)\,dx = -\int_{-C_3} P(x, y)\,dx = -\int_a^b P(x, g_2(x))\,dx .
> $$
>
> - On $C_2$ and $C_4$, $x$ is constant, so $dx = 0$ and $\displaystyle\int_{C_2} P\,dx = 0 = \int_{C_4} P\,dx$.
>
> Adding the four pieces,
>
> $$
> \oint_C P(x, y)\,dx = \int_a^b P(x, g_1(x))\,dx - \int_a^b P(x, g_2(x))\,dx = -\iint_D \frac{\partial P}{\partial y}\,dA
> $$
>
> by (4). This is Equation 2.
>
> **Equation 3.** (Stewart leaves this as Exercise 34.) Write $D$ as a type II region, $D = \{(x, y) \mid c \le y \le d,\ h_1(y) \le x \le h_2(y)\}$. By the Fundamental Theorem of Calculus in $x$,
>
> $$
> \iint_D \frac{\partial Q}{\partial x}\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} \frac{\partial Q}{\partial x}(x, y)\,dx\,dy = \int_c^d \big[ Q(h_2(y), y) - Q(h_1(y), y) \big]\,dy .
> $$
>
> With $D$ on the left, $C$ runs *up* the right side $x = h_2(y)$ and *down* the left side $x = h_1(y)$. Taking $y$ as the parameter,
>
> $$
> \int_{\text{right}} Q\,dy = \int_c^d Q(h_2(y), y)\,dy, \qquad \int_{\text{left}} Q\,dy = -\int_c^d Q(h_1(y), y)\,dy ,
> $$
>
> and on the horizontal segments $y = c$ and $y = d$ (possibly single points), $dy = 0$. Adding gives Equation 3.
>
> Adding Equations 2 and 3 gives Green's Theorem.

^pf-130-1

*Uses:* [[§130 Green's Theorem#^def-130-1|Def. §130.1]], [[§130 Green's Theorem#^def-130-2|Def. §130.2]], [[§116 Double Integrals Over General Regions#^thm-116-1|§116.1]], [[§116 Double Integrals Over General Regions#^thm-116-2|§116.2]], [[§41 The Fundamental Theorem of Calculus#^thm-41-2|§41.2]], [[§126 Line Integrals#^thm-126-2|§126.2]] (line integrals with respect to x and y), [[§126 Line Integrals#^thm-126-4|§126.4]] (reversing orientation)

![[m233-110-1.svg]]
*Equation 2 on a type I region. The positively oriented boundary runs right along the bottom $C_1$, up $C_2$, left along the top $C_3$ and down $C_4$. Only $C_1$ and $C_3$ see $P\,dx$, with opposite signs because they are traversed in opposite directions. On each vertical segment at $x$ (blue), the Fundamental Theorem of Calculus in $y$ turns the difference $P(x, g_2(x)) - P(x, g_1(x))$ into $\int_{g_1}^{g_2} \partial P/\partial y\,dy$. Equation 3 is the same picture cut into horizontal segments.*

> [!remark]- Connections
> - Rigorous treatment: [[§27 Line Integrals and Green's Theorem#^thm-27-1|452 Thm. §27.1]], with the same proof (Fubini on type I and type II regions, [[§23 Fubini's Theorem#^def-23-1|452 Def. §23.1]], plus the FTC; general regions by subdivision) and the same convention "$D$ on the left", which reappears there as the induced boundary orientation of Stokes' theorem. Hub: [[Green's Theorem]].
> - It is the flat case of Stokes' theorem ([[§136 Stokes' Theorem#^thm-136-1|Theorem §136.1]]; 452 [[Stokes' Theorem in ℝ³]]) and the case of 1-forms in the plane of the [[Generalized Stokes' Theorem]].
> - See also: [[§50 Cauchy–Goursat Theorem#^thm-50-2|342 Thm. §50.2]] (Cauchy's theorem $\int_C f(z)\,dz = 0$, derived from Green's theorem and the Cauchy–Riemann equations) and [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^thm-51-3|342 Thm. §51.3]] (the Cauchy–Goursat theorem, which drops the continuity of $f'$).

> [!remark] Remark: The Fundamental Theorem of Calculus for Double Integrals
> Compare Equation 1 with Part 2 of the Fundamental Theorem of Calculus ([[§41 The Fundamental Theorem of Calculus#^thm-41-2|Theorem §41.2]]):
>
> $$
> \int_a^b F'(x)\,dx = F(b) - F(a) .
> $$
>
> In both, the left side integrates derivatives ($F'$; $\partial Q/\partial x$ and $\partial P/\partial y$) over a domain, and the right side involves only the values of the original functions ($F$; $Q$ and $P$) on the boundary of the domain. In one dimension the domain is $[a, b]$ and its boundary is the two points $a$ and $b$.

^rem-130-1

> [!remark] Remark: Method — Using Green's Theorem
> 1. **Check the curve.** $C$ must be closed, simple and piecewise smooth. Find its orientation: counterclockwise, with $D$ on the left, is positive. If $C$ is traversed clockwise, then $\oint_C P\,dx + Q\,dy = -\iint_D (Q_x - P_y)\,dA$.
> 2. **Check the field.** $P$ and $Q$ must have continuous partial derivatives on an open region containing *all* of $D$. A point of $D$ where $P$ or $Q$ is undefined ([[§131 Extended Versions of Green's Theorem#^ex-131-2|Example §131.2]]) rules out a direct application.
> 3. **Compute** $\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}$. Terms of $P$ that depend on $x$ alone and terms of $Q$ that depend on $y$ alone drop out, however complicated they are.
> 4. **Evaluate the double integral**, choosing coordinates that fit $D$: polar coordinates for disks, annuli and sectors ([[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]]), and area formulas when the integrand is constant.
> 5. **Reverse direction.** Sometimes the line integral is the easier side: areas ([[§130 Green's Theorem#^cor-130-2|Corollary §130.2]]), or the case $P = Q = 0$ on $C$, which gives $\iint_D (Q_x - P_y)\,dA = 0$ whatever $P$ and $Q$ do inside $D$.

^rem-130-2

> [!example] Example §130.1: A Triangle and a Circle
> **(a)** Evaluate $\displaystyle\int_C x^4\,dx + xy\,dy$, where $C$ is the triangular curve consisting of the line segments from $(0, 0)$ to $(1, 0)$, from $(1, 0)$ to $(0, 1)$ and from $(0, 1)$ to $(0, 0)$.
>
> Directly, this needs three parametrizations, one for each side. Instead: the region $D$ enclosed by $C$ is simple, $C$ is traversed counterclockwise (positively), and $P(x, y) = x^4$, $Q(x, y) = xy$ are polynomials. So
>
> $$
> \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = y - 0 = y ,
> $$
>
> and with $D = \{(x, y) \mid 0 \le x \le 1,\ 0 \le y \le 1 - x\}$,
>
> $$
> \begin{aligned}
> \int_C x^4\,dx + xy\,dy &= \iint_D y\,dA = \int_0^1 \int_0^{1-x} y\,dy\,dx = \int_0^1 \Big[\tfrac12 y^2\Big]_{y=0}^{y=1-x} dx \\
> &= \frac12 \int_0^1 (1 - x)^2\,dx = \Big[-\tfrac16 (1 - x)^3\Big]_0^1 = \frac16 .
> \end{aligned}
> $$
>
> **(b)** Evaluate $\displaystyle\oint_C (3y - e^{\sin x})\,dx + \big(7x + \sqrt{y^4 + 1}\big)\,dy$, where $C$ is the circle $x^2 + y^2 = 9$.
>
> Here $D$ is the disk $x^2 + y^2 \le 9$, and $P = 3y - e^{\sin x}$, $Q = 7x + \sqrt{y^4 + 1}$ have continuous partial derivatives everywhere. The awkward terms drop out (step 3 of the method):
>
> $$
> \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = \frac{\partial}{\partial x}\big(7x + \sqrt{y^4 + 1}\big) - \frac{\partial}{\partial y}\big(3y - e^{\sin x}\big) = 7 - 3 = 4 .
> $$
>
> In polar coordinates,
>
> $$
> \oint_C \cdots = \iint_D 4\,dA = \int_0^{2\pi} \int_0^3 4\,r\,dr\,d\theta = 4 \int_0^{2\pi} d\theta \int_0^3 r\,dr = 4 \cdot 2\pi \cdot \frac92 = 36\pi .
> $$
>
> Or, without integrating: $\iint_D 4\,dA = 4 \cdot \text{area}(D) = 4 \cdot \pi (3)^2 = 36\pi$. (Setting up the line integral directly is hopeless.)
>
> *Stewart: Examples 16.4.1 and 16.4.2*

^ex-130-1

> [!example] Example §130.2: Checking Green's Theorem on a Quarter Disk
> Let $\mathbf{F}(x, y) = \langle y^3, -x^3 \rangle$. Evaluate $\oint_C \mathbf{F} \cdot d\mathbf{r}$ for the closed curve $C$ consisting of the segment from $(0, 0)$ to $(1, 0)$, the part of the circle $x^2 + y^2 = 1$ from $(1, 0)$ to $(0, 1)$, and the segment from $(0, 1)$ to $(0, 0)$.
>
> **By Green's Theorem.** $C = C_1 \cup C_2 \cup C_3$ is simple, closed and piecewise smooth, and it is traversed counterclockwise around the quarter disk $D = \{0 \le r \le 1,\ 0 \le \theta \le \pi/2\}$. With $P = y^3$ and $Q = -x^3$,
>
> $$
> \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = -3x^2 - 3y^2 = -3r^2 ,
> $$
>
> so
>
> $$
> \oint_C \mathbf{F} \cdot d\mathbf{r} = \int_0^{\pi/2} \int_0^1 (-3r^2)\,r\,dr\,d\theta = \frac{\pi}{2} \cdot \Big[-\tfrac34 r^4\Big]_0^1 = -\frac{3\pi}{8} .
> $$
>
> **Directly.** On $C_1$ ($y = 0$, $dy = 0$) and on $C_3$ ($x = 0$, $dx = 0$) the integrand $y^3\,dx - x^3\,dy$ vanishes. On $C_2$, $x = \cos t$, $y = \sin t$, $0 \le t \le \pi/2$:
>
> $$
> \int_{C_2} y^3\,dx - x^3\,dy = \int_0^{\pi/2} \big[\sin^3 t\,(-\sin t) - \cos^3 t\,(\cos t)\big]\,dt = -\int_0^{\pi/2} (\sin^4 t + \cos^4 t)\,dt .
> $$
>
> Since $\sin^4 t + \cos^4 t = (\sin^2 t + \cos^2 t)^2 - 2\sin^2 t\cos^2 t = 1 - \tfrac12 \sin^2 2t$, the last integral is $\frac{\pi}{2} - \frac12 \cdot \frac{\pi}{4} = \frac{3\pi}{8}$. The total is $-\frac{3\pi}{8}$, as Green's Theorem predicts. The negative sign is reasonable: $\mathbf{F}$ points clockwise along the arc, against the direction of travel.
>
> *The posted solution writes the integrand as $3y^2 + 3x^2$ and gets $\frac{3\pi}{8}$. The sign of $\partial Q/\partial x - \partial P/\partial y$ is lost there; the direct computation confirms $-\frac{3\pi}{8}$.*
>
> *Source: 233 Chapter 16 Review, Q6(a)*

^ex-130-2

## Finding Areas with Green's Theorem

Since the area of $D$ is $\iint_D 1\,dA$, Green's Theorem expresses it as a line integral as soon as $\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} = 1$. Three convenient choices are

$$
P = 0,\ Q = x \qquad\text{or}\qquad P = -y,\ Q = 0 \qquad\text{or}\qquad P = -\tfrac12 y,\ Q = \tfrac12 x .
$$

> [!theorem] Corollary §130.2: Area as a Line Integral
> If $C$ and $D$ are as in Green's Theorem, the area of $D$ is
>
> $$
> A = \oint_C x\,dy = -\oint_C y\,dx = \frac12 \oint_C x\,dy - y\,dx .
> $$
>
> *Stewart: 16.4, Equation 5*

^cor-130-2

> [!proof]+ Proof
> Apply Green's Theorem to each of the three choices above. Each pair $P, Q$ is a polynomial, so it has continuous partial derivatives everywhere, and
>
> $$
> \frac{\partial x}{\partial x} - \frac{\partial 0}{\partial y} = 1, \qquad
> \frac{\partial 0}{\partial x} - \frac{\partial (-y)}{\partial y} = 1, \qquad
> \frac{\partial (\frac12 x)}{\partial x} - \frac{\partial (-\frac12 y)}{\partial y} = \frac12 + \frac12 = 1 .
> $$
>
> In each case $\oint_C P\,dx + Q\,dy = \iint_D 1\,dA = A$, which gives the three formulas.

^pf-130-2

*Uses:* [[§130 Green's Theorem#^thm-130-1|§130.1]]

> [!remark]- Connections
> - See also: [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^ex-51-2|342 Ex. §51.2]] (the area inside $C$ as $\frac{1}{2i}\int_C \bar z\,dz$, from Green's theorem).

> [!example] Example §130.3: The Area of an Ellipse
> Find the area enclosed by the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$.
>
> The ellipse has the counterclockwise parametrization $x = a\cos t$, $y = b\sin t$, $0 \le t \le 2\pi$. By the third formula in [[§130 Green's Theorem#^cor-130-2|Corollary §130.2]],
>
> $$
> \begin{aligned}
> A &= \frac12 \oint_C x\,dy - y\,dx = \frac12 \int_0^{2\pi} \big[(a\cos t)(b\cos t) - (b\sin t)(-a\sin t)\big]\,dt \\
> &= \frac{ab}{2} \int_0^{2\pi} (\cos^2 t + \sin^2 t)\,dt = \frac{ab}{2} \int_0^{2\pi} dt = \pi ab .
> \end{aligned}
> $$
>
> *Stewart: Example 16.4.3*

^ex-130-3

> [!remark]- Remark: The Planimeter
> [[§130 Green's Theorem#^cor-130-2|Corollary §130.2]] explains how a **planimeter** works. This 19th-century mechanical instrument measures the area of a region by tracing its boundary. In a polar planimeter the pole is fixed, and as the tracer moves around the boundary curve, a wheel partly slides and partly rolls perpendicular to the tracer arm. The distance the wheel rolls is proportional to the enclosed area. (Stewart cites R. W. Gatterman, *Amer. Math. Monthly* 88 (1981), 701–704, and T. Leise, *College Math. J.* 38 (2007), 24–31.)

^rem-130-3

*The section continues in [[§131 Extended Versions of Green's Theorem]].*
