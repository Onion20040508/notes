---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 110
stewart: "16.4"
aliases: ["Stewart 16.4"]
tags: [calculus, math233]
---
← [[§109 The Fundamental Theorem for Line Integrals]] · ↑ [[· 16 Vector Calculus]] · [[§111 Curl and Divergence]] →

*Stewart, Section 16.4 · MATH 233 (UMass, Spring 2023): Practice Final Exam (Q2), Chapter 16 Review (Q6a).*

Green's Theorem turns a line integral around a simple closed curve $C$ into a double integral over the region $D$ that $C$ bounds. It is the Fundamental Theorem of Calculus one dimension up: an integral of derivatives over $D$ equals boundary values of the original functions, integrated over $\partial D$. It is used in both directions. A line integral that would need several parametrizations becomes one double integral, and an area becomes a line integral around the boundary. Cutting regions into pieces extends it to regions with holes. That gives the standard calculation for fields with a singularity, such as $(-y\,\mathbf{i} + x\,\mathbf{j})/(x^2 + y^2)$, and the proof of the test for conservative fields announced in §109 (the converse of [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Theorem §109.4]]).

## Green's Theorem

> [!definition] Definition §110.1: Positive Orientation
> Let $C$ be a simple closed curve and $D$ the region bounded by $C$, consisting of all points inside $C$ together with the points of $C$. The **positive orientation** of $C$ is a single *counterclockwise* traversal of $C$. Equivalently, if $C$ is given by $\mathbf{r}(t)$, $a \le t \le b$, then the region $D$ is always on the left as the point $\mathbf{r}(t)$ traverses $C$.
>
> **Notation.** $\displaystyle\oint_C P\,dx + Q\,dy$ indicates that the line integral is taken in the positive direction (Stewart also puts a counterclockwise arrow on the circle). The positively oriented boundary curve of $D$ is written $\partial D$.
>
> *Stewart: 16.4 (text)*

^def-110-1

> [!definition] Definition §110.2: Simple Region
> A plane region is **simple** if it is both of type I and of type II ([[§99 Double Integrals Over General Regions|§99]]). That is, it can be written both as
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

^def-110-2

> [!theorem] Theorem §110.1: Green's Theorem
> Let $C$ be a positively oriented, piecewise-smooth, simple closed curve in the plane and let $D$ be the region bounded by $C$. If $P$ and $Q$ have continuous partial derivatives on an open region that contains $D$, then
>
> $$
> \oint_C P\,dx + Q\,dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA .
> $$
>
> In the notation of Definition §110.1:
>
> $$
> \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \oint_{\partial D} P\,dx + Q\,dy .
> $$
>
> The left side of the first equation is $\oint_C \mathbf{F} \cdot d\mathbf{r}$ for $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ ([[§108 Line Integrals#^thm-108-7|Theorem §108.7]]).
>
> *Stewart: 16.4, Green's Theorem and Equation 1*

^thm-110-1

> [!remark] Remark: The Fundamental Theorem of Calculus for Double Integrals
> Compare Equation 1 with Part 2 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus|§36]]):
>
> $$
> \int_a^b F'(x)\,dx = F(b) - F(a) .
> $$
>
> In both, the left side integrates derivatives ($F'$; $\partial Q/\partial x$ and $\partial P/\partial y$) over a domain, and the right side involves only the values of the original functions ($F$; $Q$ and $P$) on the boundary of the domain. In one dimension the domain is $[a, b]$ and its boundary is the two points $a$ and $b$.

^rem-110-1

Green's Theorem is not easy to prove in general. Stewart proves it for simple regions ([[§110 Green's Theorem#^def-110-2|Def. §110.2]]: both type I and type II), and then extends it by cutting.

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

^pf-110-1

*Uses:* [[§110 Green's Theorem#^def-110-1|Def. §110.1]], [[§110 Green's Theorem#^def-110-2|Def. §110.2]], [[§99 Double Integrals Over General Regions|§99]] (iterated integrals over type I and II regions), [[§36 The Fundamental Theorem of Calculus|§36]] (FTC Part 2), [[§108 Line Integrals#^thm-108-2|§108.2]] (line integrals with respect to x and y), [[§108 Line Integrals#^thm-108-4|§108.4]] (reversing orientation)

![[m233-110-1.svg]]
*Equation 2 on a type I region. The positively oriented boundary runs right along the bottom $C_1$, up $C_2$, left along the top $C_3$ and down $C_4$. Only $C_1$ and $C_3$ see $P\,dx$, with opposite signs because they are traversed in opposite directions. On each vertical segment at $x$ (blue), the Fundamental Theorem of Calculus in $y$ turns the difference $P(x, g_2(x)) - P(x, g_1(x))$ into $\int_{g_1}^{g_2} \partial P/\partial y\,dy$. Equation 3 is the same picture cut into horizontal segments.*

> [!remark]- Connections
> - Rigorous treatment: [[§16 Line Integrals and Green's Theorem#^thm-16-1|452 Thm. §16.1]], with the same proof (Fubini on type I and type II regions, [[§15 Multivariable Integration#^def-15-12|452 Def. §15.12]], plus the FTC; general regions by subdivision) and the same convention "$D$ on the left", which reappears there as the induced boundary orientation of Stokes' theorem. Hub: [[Green's Theorem]].
> - It is the flat case of Stokes' theorem ([[§114 Stokes' Theorem#^thm-114-1|Theorem §114.1]]; 452 [[Stokes' Theorem in ℝ³]]) and the case of 1-forms in the plane of the [[Generalized Stokes' Theorem]].

> [!remark] Remark: Method — Using Green's Theorem
> 1. **Check the curve.** $C$ must be closed, simple and piecewise smooth. Find its orientation: counterclockwise, with $D$ on the left, is positive. If $C$ is traversed clockwise, then $\oint_C P\,dx + Q\,dy = -\iint_D (Q_x - P_y)\,dA$.
> 2. **Check the field.** $P$ and $Q$ must have continuous partial derivatives on an open region containing *all* of $D$. A point of $D$ where $P$ or $Q$ is undefined ([[§110 Green's Theorem#^ex-110-5|Example §110.5]]) rules out a direct application.
> 3. **Compute** $\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}$. Terms of $P$ that depend on $x$ alone and terms of $Q$ that depend on $y$ alone drop out, however complicated they are.
> 4. **Evaluate the double integral**, choosing coordinates that fit $D$: polar coordinates for disks, annuli and sectors ([[§100 Double Integrals in Polar Coordinates|§100]]), and area formulas when the integrand is constant.
> 5. **Reverse direction.** Sometimes the line integral is the easier side: areas (Corollary §110.2), or the case $P = Q = 0$ on $C$, which gives $\iint_D (Q_x - P_y)\,dA = 0$ whatever $P$ and $Q$ do inside $D$.

^rem-110-2

> [!example] Example §110.1: A Triangle and a Circle
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

^ex-110-1

> [!example] Example §110.2: Checking Green's Theorem on a Quarter Disk
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

^ex-110-2

## Finding Areas with Green's Theorem

Since the area of $D$ is $\iint_D 1\,dA$, Green's Theorem expresses it as a line integral as soon as $\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} = 1$. Three convenient choices are

$$
P = 0,\ Q = x \qquad\text{or}\qquad P = -y,\ Q = 0 \qquad\text{or}\qquad P = -\tfrac12 y,\ Q = \tfrac12 x .
$$

> [!theorem] Corollary §110.2: Area as a Line Integral
> If $C$ and $D$ are as in Green's Theorem, the area of $D$ is
>
> $$
> A = \oint_C x\,dy = -\oint_C y\,dx = \frac12 \oint_C x\,dy - y\,dx .
> $$
>
> *Stewart: 16.4, Equation 5*

^cor-110-2

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

^pf-110-2

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]]

> [!example] Example §110.3: The Area of an Ellipse
> Find the area enclosed by the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$.
>
> The ellipse has the counterclockwise parametrization $x = a\cos t$, $y = b\sin t$, $0 \le t \le 2\pi$. By the third formula in Corollary §110.2,
>
> $$
> \begin{aligned}
> A &= \frac12 \oint_C x\,dy - y\,dx = \frac12 \int_0^{2\pi} \big[(a\cos t)(b\cos t) - (b\sin t)(-a\sin t)\big]\,dt \\
> &= \frac{ab}{2} \int_0^{2\pi} (\cos^2 t + \sin^2 t)\,dt = \frac{ab}{2} \int_0^{2\pi} dt = \pi ab .
> \end{aligned}
> $$
>
> *Stewart: Example 16.4.3*

^ex-110-3

> [!remark]- Remark: The Planimeter
> Corollary §110.2 explains how a **planimeter** works. This 19th-century mechanical instrument measures the area of a region by tracing its boundary. In a polar planimeter the pole is fixed, and as the tracer moves around the boundary curve, a wheel partly slides and partly rolls perpendicular to the tracer arm. The distance the wheel rolls is proportional to the enclosed area. (Stewart cites R. W. Gatterman, *Amer. Math. Monthly* 88 (1981), 701–704, and T. Leise, *College Math. J.* 38 (2007), 24–31.)

^rem-110-3

## Extended Versions of Green's Theorem

> [!theorem] Theorem §110.3: Green's Theorem for Finite Unions of Simple Regions
> Green's Theorem holds when $D$ is a finite union of non-overlapping simple regions and $C = \partial D$ is its positively oriented boundary.
>
> *Stewart: 16.4 (text)*

^thm-110-3

> [!proof]+ Proof
> First let $D = D_1 \cup D_2$, where $D_1$ and $D_2$ are simple and meet along a curve $C_3$. Let the rest of the boundary of $D_1$ be $C_1$ and the rest of the boundary of $D_2$ be $C_2$, so that $\partial D = C_1 \cup C_2$. The positively oriented boundary of $D_1$ is $C_1 \cup C_3$, and that of $D_2$ is $C_2 \cup (-C_3)$: the common curve is traversed in opposite directions, because the two regions lie on opposite sides of it. Green's Theorem for simple regions (Theorem §110.1) gives
>
> $$
> \int_{C_1 \cup C_3} P\,dx + Q\,dy = \iint_{D_1} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA, \qquad
> \int_{C_2 \cup (-C_3)} P\,dx + Q\,dy = \iint_{D_2} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA .
> $$
>
> Add the two equations. Since $\int_{-C_3} = -\int_{C_3}$, the line integrals along $C_3$ and $-C_3$ cancel, and the double integrals add up to the double integral over $D$:
>
> $$
> \int_{C_1 \cup C_2} P\,dx + Q\,dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA .
> $$
>
> This is Green's Theorem for $D$, since its boundary is $C = C_1 \cup C_2$. For a union of more simple regions, the same argument applies: every internal edge is shared by two of the pieces, it is traversed once in each direction, and its contributions cancel.

^pf-110-3

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§108 Line Integrals#^thm-108-4|§108.4]] (reversing orientation)

> [!example] Example §110.4: Sectors of Annuli
> **(a) A semiannulus.** Evaluate $\displaystyle\oint_C y^2\,dx + 3xy\,dy$, where $C$ is the boundary of the semiannular region $D$ in the upper half-plane between the circles $x^2 + y^2 = 1$ and $x^2 + y^2 = 4$.
>
> $D$ is not simple, but the $y$-axis divides it into two simple regions, so Theorem §110.3 applies. In polar coordinates $D = \{(r, \theta) \mid 1 \le r \le 2,\ 0 \le \theta \le \pi\}$, and
>
> $$
> \frac{\partial}{\partial x}(3xy) - \frac{\partial}{\partial y}(y^2) = 3y - 2y = y .
> $$
>
> Therefore
>
> $$
> \begin{aligned}
> \oint_C y^2\,dx + 3xy\,dy &= \iint_D y\,dA = \int_0^{\pi} \int_1^2 (r\sin\theta)\,r\,dr\,d\theta = \int_0^{\pi} \sin\theta\,d\theta \int_1^2 r^2\,dr \\
> &= \Big[-\cos\theta\Big]_0^{\pi} \Big[\tfrac13 r^3\Big]_1^2 = 2 \cdot \frac73 = \frac{14}{3} .
> \end{aligned}
> $$
>
> **(b) A sector of an annulus.** Use Green's Theorem to evaluate
>
> $$
> \oint_C \big(\sqrt{2 + x^3} - 8y^3\big)\,dx + \big(8x^3 + \sqrt{1 + y^3}\big)\,dy ,
> $$
>
> where $C$ is the boundary of $D = \{(x, y) \mid 1 \le x^2 + y^2 \le 4,\ -y \le x \le y,\ y \ge 0\}$, traversed in the positive sense.
>
> **The region.** $-y \le x \le y$ with $y \ge 0$ says $|x| \le y$: the wedge between the lines $y = x$ and $y = -x$ above the origin. So in polar coordinates $D = \{(r, \theta) \mid 1 \le r \le 2,\ \pi/4 \le \theta \le 3\pi/4\}$, a sector of an annulus. Like the semiannulus of part (a), it is a union of simple regions.
>
> **The integrand.** With $P = \sqrt{2 + x^3} - 8y^3$ and $Q = 8x^3 + \sqrt{1 + y^3}$, the square roots drop out:
>
> $$
> \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 24x^2 - (-24y^2) = 24(x^2 + y^2) = 24r^2 .
> $$
>
> **The integral.**
>
> $$
> \oint_C \cdots = \int_{\pi/4}^{3\pi/4} \int_1^2 24r^2 \cdot r\,dr\,d\theta = 24 \cdot \frac{\pi}{2} \cdot \Big[\tfrac14 r^4\Big]_1^2 = 12\pi \cdot \frac{16 - 1}{4} = 45\pi .
> $$
>
> *A caveat on the problem as set: $\sqrt{2 + x^3}$ is undefined where $x < -\sqrt[3]{2} \approx -1.26$, and $D$ reaches $x = -\sqrt2 \approx -1.41$ at its corner $(-\sqrt2, \sqrt2)$. So $P$ is not defined on all of $D$, and strictly the hypotheses of Green's Theorem fail. The intended point is step 3 of the method: a term of $P$ that depends on $x$ alone contributes nothing. The posted answer $45\pi$ is the value of the intended problem.*
>
> *Stewart: Example 16.4.4*
> *Source: 233 Practice Final Exam, Q2*

^ex-110-4

> [!theorem] Theorem §110.4: Green's Theorem for Regions with Holes
> Let $D$ be a region whose boundary $C$ consists of two piecewise-smooth simple closed curves, an outer curve $C_1$ and an inner curve $C_2$, oriented so that $D$ is always on the left as $C$ is traversed: counterclockwise on $C_1$, clockwise on $C_2$. If $P$ and $Q$ have continuous partial derivatives on an open region containing $D$, then
>
> $$
> \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \int_{C_1} P\,dx + Q\,dy + \int_{C_2} P\,dx + Q\,dy = \int_C P\,dx + Q\,dy .
> $$
>
> The same holds with several holes. Such regions are not simply connected ([[§109 The Fundamental Theorem for Line Integrals#^def-109-5|Definition §109.5]]).
>
> *Stewart: 16.4 (text)*

^thm-110-4

> [!proof]+ Proof
> Cut $D$ along two segments joining $C_1$ to $C_2$ (one on each side of the hole). This divides $D$ into two regions $D'$ and $D''$, as in the figure below, each a union of simple regions. Apply Theorem §110.3 to each and add:
>
> $$
> \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
> = \iint_{D'} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA + \iint_{D''} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
> = \int_{\partial D'} P\,dx + Q\,dy + \int_{\partial D''} P\,dx + Q\,dy .
> $$
>
> The boundaries $\partial D'$ and $\partial D''$ both run along each cut, in opposite directions, so the line integrals along the cuts cancel. What is left is $\partial D'$ and $\partial D''$ along $C_1$, which together make up $C_1$ counterclockwise, and along $C_2$, which together make up $C_2$ clockwise. So the sum is
>
> $$
> \int_{C_1} P\,dx + Q\,dy + \int_{C_2} P\,dx + Q\,dy = \int_C P\,dx + Q\,dy .
> $$
>
> With several holes, make more cuts; the bookkeeping is the same.

^pf-110-4

*Uses:* [[§110 Green's Theorem#^thm-110-3|§110.3]], [[§108 Line Integrals#^thm-108-4|§108.4]] (reversing orientation)

![[m233-110-2.svg]]
*The cutting argument for a region with a hole. Each half $D'$ and $D''$ gets its own counterclockwise boundary. Along the two cuts (green) the upper half travels one way and the lower half the other, so those contributions cancel. What remains is the outer curve $C_1$ counterclockwise and the inner curve $C_2$ clockwise, both with $D$ on the left.*

> [!example] Example §110.5: A Field with a Singularity at the Origin
> If $\mathbf{F}(x, y) = \dfrac{-y\,\mathbf{i} + x\,\mathbf{j}}{x^2 + y^2}$, show that $\displaystyle\int_C \mathbf{F} \cdot d\mathbf{r} = 2\pi$ for every positively oriented simple closed path $C$ that encloses the origin.
>
> Green's Theorem cannot be applied to $C$ directly, because $\mathbf{F}$ is undefined at the origin, which lies inside $C$. And $C$ is arbitrary, so we cannot parametrize it. Instead, choose $a > 0$ small enough that the counterclockwise circle $C'$ with center the origin and radius $a$ lies inside $C$. Let $D$ be the region between $C$ and $C'$. It does not contain the origin, and its positively oriented boundary is $C \cup (-C')$. With $P = \dfrac{-y}{x^2 + y^2}$ and $Q = \dfrac{x}{x^2 + y^2}$,
>
> $$
> \frac{\partial Q}{\partial x} = \frac{(x^2 + y^2) - x \cdot 2x}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}, \qquad
> \frac{\partial P}{\partial y} = \frac{-(x^2 + y^2) + y \cdot 2y}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2} .
> $$
>
> These are continuous away from the origin, hence on an open region containing $D$. By Theorem §110.4,
>
> $$
> \int_C P\,dx + Q\,dy + \int_{-C'} P\,dx + Q\,dy = \iint_D \left[ \frac{y^2 - x^2}{(x^2 + y^2)^2} - \frac{y^2 - x^2}{(x^2 + y^2)^2} \right] dA = 0 ,
> $$
>
> so $\displaystyle\int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C'} \mathbf{F} \cdot d\mathbf{r}$. The circle is easy: with $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j}$, $0 \le t \le 2\pi$,
>
> $$
> \int_{C'} \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_0^{2\pi} \frac{(-a\sin t)(-a\sin t) + (a\cos t)(a\cos t)}{a^2\cos^2 t + a^2\sin^2 t}\,dt = \int_0^{2\pi} dt = 2\pi .
> $$
>
> So $\int_C \mathbf{F} \cdot d\mathbf{r} = 2\pi$ for every such $C$, even though $\partial Q/\partial x = \partial P/\partial y$ everywhere on the domain of $\mathbf{F}$. In particular $\mathbf{F}$ is not conservative on $\mathbb{R}^2 \setminus \{(0, 0)\}$: its integral around a closed path is not $0$.
>
> *Stewart: Example 16.4.5*

^ex-110-5

> [!remark]- Connections
> - This field is the angle form $d\theta$ of 452, the standard closed but not exact form: [[Angle form on the punctured plane]], [[§22 The Algebra of Differential Forms#^prop-22-11|452 Prop. §22.11]]. The value $\frac{1}{2\pi}\oint_C \mathbf{F} \cdot d\mathbf{r}$ is the winding number of $C$ about the origin.

## Curl-Free Fields on Simply-Connected Regions

Green's Theorem supplies the proof, promised in §109 after [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Theorem §109.4]], of the test for conservative vector fields in the plane.

> [!theorem] Theorem §110.5: Test for Conservative Fields
> Let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ be a vector field on an open simply-connected region $D$. Suppose that $P$ and $Q$ have continuous first-order partial derivatives and
>
> $$
> \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} \quad \text{throughout } D .
> $$
>
> Then $\mathbf{F}$ is conservative.
>
> *Stewart: 16.3, Theorem 6 (proof sketched in 16.4)*

^thm-110-5

> [!proof]+ Proof
> *Stewart gives this as a sketch.* Let $C$ be any simple closed path in $D$, and $R$ the region that $C$ encloses. Since $D$ is simply connected, $C$ encloses only points of $D$, so $R \subseteq D$ and $P$, $Q$ have continuous partial derivatives on the open set $D \supseteq R$. If $C$ is positively oriented, Green's Theorem gives
>
> $$
> \oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C P\,dx + Q\,dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \iint_R 0\,dA = 0 .
> $$
>
> If $C$ is negatively oriented, the integral is $-0 = 0$. A closed curve that is not simple crosses itself at one or more points and can be broken up into a number of simple closed curves. The line integral of $\mathbf{F}$ around each of these is $0$, so the sum is $0$. Hence $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every closed curve $C$ in $D$. By [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|Theorem §109.2]], $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of path in $D$. Since $D$ is open and connected, $\mathbf{F}$ is conservative by [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Theorem §109.3]].
>
> (What makes this a sketch is the step "broken up into simple closed curves": it is clear for curves that cross themselves finitely often, but needs more care in general.)

^pf-110-5

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§109 The Fundamental Theorem for Line Integrals#^def-109-5|Def. §109.5]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|§109.2]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|§109.3]]

> [!remark]- Connections
> - Rigorous treatment in the language of forms: on a star-shaped domain every closed form is exact, [[§22 The Algebra of Differential Forms#^prop-22-12|452 Prop. §22.12]] ([[Poincaré Lemma]]). [[§110 Green's Theorem#^ex-110-5|Example §110.5]] shows that some hypothesis on the region is needed.
> - Topology's definition of simply connected (path-connected, every loop shrinks to a point): [[§23 The Fundamental Group#^def-23-3|590 Def. §23.3]]. Stewart's definition (every simple closed curve in $D$ encloses only points of $D$) agrees with it for open connected regions in the plane (a nontrivial fact of plane topology).
