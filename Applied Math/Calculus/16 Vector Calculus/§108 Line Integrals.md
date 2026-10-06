---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 108
stewart: "16.2"
aliases: ["Stewart 16.2"]
tags: [calculus, math233]
---
← [[§107 Vector Fields]] · ↑ [[· 16 Vector Calculus]] · [[§109 The Fundamental Theorem for Line Integrals]] →

*Stewart, Section 16.2 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q6(b)), Practice Final Exam (Q3).*

A line integral is like a single integral, except that the interval $[a, b]$ is replaced by a curve $C$. There are two kinds. The line integral of a scalar function with respect to arc length, $\int_C f\,ds$, weights each bit of the curve by its length; it gives the mass of a wire or the area of a curtain over $C$. The line integral of a vector field, $\int_C \mathbf{F} \cdot d\mathbf{r}$, adds up the component of $\mathbf{F}$ along the direction of travel; it is the work done by a force field. Both are computed the same way: parametrize $C$ and turn the line integral into an ordinary integral in the parameter. The first kind does not depend on the direction in which $C$ is traversed; the second changes sign when the direction is reversed.

## Line Integrals in the Plane

Let $C$ be a plane curve with parametric equations

$$
x = x(t), \qquad y = y(t), \qquad a \le t \le b, \qquad (1)
$$

or vector equation $\mathbf{r}(t) = x(t)\,\mathbf{i} + y(t)\,\mathbf{j}$, and assume that $C$ is a **smooth curve**: $\mathbf{r}'$ is continuous and $\mathbf{r}'(t) \ne \mathbf{0}$ ([[§88 Arc Length and Curvature#^def-88-3|Definition §88.3]]). Divide $[a, b]$ into $n$ subintervals $[t_{i-1}, t_i]$ of equal width. The points $P_i = (x(t_i), y(t_i))$ divide $C$ into $n$ subarcs, of lengths $\Delta s_1, \ldots, \Delta s_n$. Choose a point $P_i^{\ast}(x_i^{\ast}, y_i^{\ast})$ in the $i$th subarc (it corresponds to some $t_i^{\ast}$ in $[t_{i-1}, t_i]$).

> [!definition] Definition §108.1: Line Integral with Respect to Arc Length
> If $f$ is defined on a smooth curve $C$ given by Equations 1, the **line integral of $f$ along $C$** is
>
> $$
> \int_C f(x, y)\,ds = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*, y_i^*)\,\Delta s_i
> $$
>
> if this limit exists.
>
> *Stewart: 16.2, Definition 2*

^def-108-1

> [!theorem] Theorem §108.1: Evaluating a Line Integral with Respect to Arc Length
> If $f$ is continuous, the limit in [[§108 Line Integrals#^def-108-1|Definition §108.1]] always exists, and
>
> $$
> \int_C f(x, y)\,ds = \int_a^b f(x(t), y(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt . \qquad (3)
> $$
>
> The value does not depend on the parametrization of $C$, provided that $C$ is traversed exactly once as $t$ increases from $a$ to $b$.
>
> *Stewart: 16.2, Equation 3*

^thm-108-1

*Stewart only indicates the proof ("a similar type of argument" to the arc length formula, [[§64 Calculus with Parametric Curves#^thm-64-4|Theorem §64.4]]); the derivation with the Mean Value Theorem and [[§19 Uniform Continuity#^def-19-1|uniform continuity]] is in [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]].*

> [!remark]- Connections
> - 452 takes Formula 3 as the definition of the scalar line integral and derives it from the Riemann sums: [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]]. One dimension up it becomes the scalar surface integral [[§18 Surface Integrals#^def-18-5|452 Def. §18.5]] ([[§113 Surface Integrals#^thm-113-1|Theorem §113.1]] here).

> [!remark] Remark: Reading Formula 3
> - **How to remember it.** If $s(t)$ is the length of $C$ between $\mathbf{r}(a)$ and $\mathbf{r}(t)$, then ([[§88 Arc Length and Curvature#^prop-88-2|Proposition §88.2]])
>
> $$
> \frac{ds}{dt} = |\mathbf{r}'(t)| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} .
> $$
>
> So: express everything in terms of $t$, using the parametric equations for $x$ and $y$, and write $ds = \sqrt{(dx/dt)^2 + (dy/dt)^2}\,dt$.
> - **Ordinary integrals are a special case.** If $C$ is the segment from $(a, 0)$ to $(b, 0)$, with $x$ as the parameter ($x = x$, $y = 0$, $a \le x \le b$), then $ds = dx$ and $\int_C f(x, y)\,ds = \int_a^b f(x, 0)\,dx$.
> - **Area of a curtain.** If $f(x, y) \ge 0$, $\int_C f(x, y)\,ds$ is the area of one side of the "fence" or "curtain" whose base is $C$ and whose height above the point $(x, y)$ is $f(x, y)$.

^rem-108-1

> [!definition] Definition §108.2: Piecewise-Smooth Curve
> $C$ is a **piecewise-smooth curve** if it is a union of a finite number of smooth curves $C_1, C_2, \ldots, C_n$, where the initial point of $C_{i+1}$ is the terminal point of $C_i$. The integral of $f$ along $C$ is then defined as the sum of the integrals along the smooth pieces:
>
> $$
> \int_C f(x, y)\,ds = \int_{C_1} f(x, y)\,ds + \int_{C_2} f(x, y)\,ds + \cdots + \int_{C_n} f(x, y)\,ds .
> $$
>
> *Stewart: 16.2 (text)*

^def-108-2

> [!remark]- Connections
> - Complex-variables version: [[§43 Contours#^def-43-5|342 Def. §43.5]] (a contour is a piecewise smooth arc).

> [!example] Example §108.1: Line Integrals with Respect to Arc Length
> **(a)** Evaluate $\int_C (2 + x^2 y)\,ds$, where $C$ is the upper half of the unit circle $x^2 + y^2 = 1$.
>
> Parametrize $C$ by $x = \cos t$, $y = \sin t$, $0 \le t \le \pi$. Then $\sqrt{(dx/dt)^2 + (dy/dt)^2} = \sqrt{\sin^2 t + \cos^2 t} = 1$, and Formula 3 gives
>
> $$
> \int_C (2 + x^2 y)\,ds = \int_0^{\pi} (2 + \cos^2 t \sin t)\,dt = \left[ 2t - \frac{\cos^3 t}{3} \right]_0^{\pi} = 2\pi + \frac13 + \frac13 = 2\pi + \frac23 .
> $$
>
> **(b)** Evaluate $\int_C 2x\,ds$, where $C$ consists of the arc $C_1$ of the parabola $y = x^2$ from $(0, 0)$ to $(1, 1)$ followed by the vertical segment $C_2$ from $(1, 1)$ to $(1, 2)$.
>
> $C$ is piecewise smooth. On $C_1$ use $x$ as the parameter: $x = x$, $y = x^2$, $0 \le x \le 1$, so $ds = \sqrt{1 + 4x^2}\,dx$ and
>
> $$
> \int_{C_1} 2x\,ds = \int_0^1 2x\sqrt{1 + 4x^2}\,dx = \frac14 \cdot \frac23 (1 + 4x^2)^{3/2} \Big]_0^1 = \frac{5\sqrt5 - 1}{6} .
> $$
>
> On $C_2$ use $y$: $x = 1$, $y = y$, $1 \le y \le 2$, so $ds = dy$ and $\int_{C_2} 2x\,ds = \int_1^2 2\,dy = 2$. Therefore
>
> $$
> \int_C 2x\,ds = \frac{5\sqrt5 - 1}{6} + 2 .
> $$
>
> *Stewart: Examples 16.2.1 and 16.2.2*

^ex-108-1

> [!definition] Definition §108.3: Mass of a Wire
> If $\rho(x, y)$ is the [[§20 Rates of Change in the Natural and Social Sciences#^def-20-3|linear density]] at the point $(x, y)$ of a thin wire shaped like a curve $C$, the **mass** of the wire is
>
> $$
> m = \lim_{n \to \infty} \sum_{i=1}^{n} \rho(x_i^*, y_i^*)\,\Delta s_i = \int_C \rho(x, y)\,ds ,
> $$
>
> *Stewart: 16.2, Equations 4*

^def-108-3

> [!definition] Definition §108.4: Center of Mass of a Wire
> For a thin wire shaped like a curve $C$, with linear density $\rho(x, y)$ and mass $m$ ([[§108 Line Integrals#^def-108-3|Definition §108.3]]), its **center of mass** is the point $(\bar{x}, \bar{y})$, where
>
> $$
> \bar{x} = \frac1m \int_C x\,\rho(x, y)\,ds, \qquad \bar{y} = \frac1m \int_C y\,\rho(x, y)\,ds . \qquad (4)
> $$
>
> *Stewart: 16.2, Equations 4*

^def-108-new1

For example, a semicircular wire $x^2 + y^2 = 1$, $y \ge 0$, with density $\rho = k(1 - y)$ (thicker near its base) has $m = \int_0^{\pi} k(1 - \sin t)\,dt = k(\pi - 2)$ and, by symmetry and (4), center of mass $\left(0, \frac{4 - \pi}{2(\pi - 2)}\right) \approx (0, 0.38)$ (Stewart, Example 16.2.3).

## Line Integrals with Respect to x and y

> [!definition] Definition §108.4: Line Integrals with Respect to x and y
> Replacing $\Delta s_i$ in [[§108 Line Integrals#^def-108-1|Definition §108.1]] by $\Delta x_i = x_i - x_{i-1}$ or by $\Delta y_i = y_i - y_{i-1}$ gives the **line integrals of $f$ along $C$ with respect to $x$ and $y$**:
>
> $$
> \int_C f(x, y)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*, y_i^*)\,\Delta x_i, \qquad (5)
> \qquad
> \int_C f(x, y)\,dy = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*, y_i^*)\,\Delta y_i . \qquad (6)
> $$
>
> To distinguish it from these, $\int_C f(x, y)\,ds$ is called the **line integral with respect to arc length**. When integrals with respect to $x$ and $y$ occur together, we abbreviate
>
> $$
> \int_C P(x, y)\,dx + \int_C Q(x, y)\,dy = \int_C P(x, y)\,dx + Q(x, y)\,dy .
> $$
>
> *Stewart: 16.2, Equations 5 and 6*

^def-108-4

> [!remark]- Connections
> - See also: [[§50 Cauchy–Goursat Theorem#^prop-50-1|342 Prop. §50.1]] (a contour integral $\int_C f(z)\,dz$ written as real line integrals with respect to $x$ and $y$).

> [!theorem] Theorem §108.2: Evaluating Line Integrals with Respect to x and y
> With $x = x(t)$, $y = y(t)$, $dx = x'(t)\,dt$, $dy = y'(t)\,dt$:
>
> $$
> \int_C f(x, y)\,dx = \int_a^b f(x(t), y(t))\,x'(t)\,dt, \qquad \int_C f(x, y)\,dy = \int_a^b f(x(t), y(t))\,y'(t)\,dt . \qquad (7)
> $$
>
> *Stewart: 16.2, Formulas 7*

^thm-108-2

*Stewart states Formulas 7 without proof; the argument is the one behind Formula 3, with the Mean Value Theorem applied to $x(t)$ alone: $\Delta x_i = x'(\tau_i)\,\Delta t$ for some $\tau_i$ in $[t_{i-1}, t_i]$. In 452 they are the definition of the work integral, [[§16 Line Integrals and Green's Theorem#^def-16-2|452 Def. §16.2]].*

> [!example] Example §108.2: Arc Length versus dx along the Same Curve
> Let $f(x, y) = y\sin x$. Evaluate $\int_C f\,ds$ and $\int_C f\,dx$, where $C$ is the part of the curve $y = \cos x$ from $(0, 1)$ to $(\pi/2, 0)$.
>
> Parametrize $C$ by $x = t$, $y = \cos t$, $0 \le t \le \pi/2$ (this runs from $(0, 1)$ to $(\pi/2, 0)$, as required). Then $x'(t) = 1$, $y'(t) = -\sin t$, and $ds = \sqrt{1 + \sin^2 t}\,dt$.
>
> **With respect to arc length.** By Formula 3,
>
> $$
> \int_C y\sin x\,ds = \int_0^{\pi/2} \cos t \sin t \sqrt{1 + \sin^2 t}\,dt .
> $$
>
> Substitute $u = 1 + \sin^2 t$, $du = 2\sin t\cos t\,dt$; $u$ runs from $1$ to $2$:
>
> $$
> \int_C y\sin x\,ds = \frac12 \int_1^2 \sqrt{u}\,du = \frac12 \cdot \frac23 \Big[u^{3/2}\Big]_1^2 = \frac{2\sqrt2 - 1}{3} .
> $$
>
> **With respect to $x$.** By Formulas 7, with $dx = x'(t)\,dt = dt$,
>
> $$
> \int_C y\sin x\,dx = \int_0^{\pi/2} \cos t \sin t\,dt = \Big[\tfrac12 \sin^2 t\Big]_0^{\pi/2} = \frac12 .
> $$
>
> The two answers differ because $ds$ and $dx$ weight the curve differently: $ds$ counts the length of each piece, $dx$ only its horizontal extent.
>
> *Source: 233 Chapter 16 Review, Q6(b)*

^ex-108-2

When setting up a line integral, the hardest step is often finding a parametric representation of a curve described geometrically. Line segments are the most common case.

> [!theorem] Proposition §108.3: Parametrizing a Line Segment
> The line segment that starts at $\mathbf{r}_0$ and ends at $\mathbf{r}_1$ has the vector representation
>
> $$
> \mathbf{r}(t) = (1 - t)\,\mathbf{r}_0 + t\,\mathbf{r}_1, \qquad 0 \le t \le 1 . \qquad (8)
> $$
>
> *Stewart: 16.2, Equation 8*

^prop-108-3

> [!proof]+ Proof
> Rewrite (8) as $\mathbf{r}(t) = \mathbf{r}_0 + t\,(\mathbf{r}_1 - \mathbf{r}_0)$. For all real $t$ this is the vector equation of the line through $\mathbf{r}_0$ with direction vector $\mathbf{r}_1 - \mathbf{r}_0$ ([[§84 Equations of Lines and Planes#^thm-84-1|Theorem §84.1]]). At $t = 0$ it gives $\mathbf{r}_0$ and at $t = 1$ it gives $\mathbf{r}_1$, and as $t$ increases from $0$ to $1$ the point moves along the line from $\mathbf{r}_0$ to $\mathbf{r}_1$, once. (This is [[§84 Equations of Lines and Planes#^prop-84-4|Proposition §84.4]], recalled here as Stewart does.)

^pf-108-3

*Uses:* [[§84 Equations of Lines and Planes#^thm-84-1|§84.1]], [[§84 Equations of Lines and Planes#^prop-84-4|§84.4]]

> [!example] Example §108.3: Same Endpoints, Different Paths
> Evaluate $\int_C y^2\,dx + x\,dy$ for (a) $C = C_1$, the line segment from $(-5, -3)$ to $(0, 2)$, and (b) $C = C_2$, the arc of the parabola $x = 4 - y^2$ from $(-5, -3)$ to $(0, 2)$.
>
> **(a)** By (8) with $\mathbf{r}_0 = \langle -5, -3 \rangle$ and $\mathbf{r}_1 = \langle 0, 2 \rangle$: $x = 5t - 5$, $y = 5t - 3$, $0 \le t \le 1$. Then $dx = 5\,dt$, $dy = 5\,dt$, and Formulas 7 give
>
> $$
> \begin{aligned}
> \int_{C_1} y^2\,dx + x\,dy &= \int_0^1 (5t - 3)^2 (5\,dt) + (5t - 5)(5\,dt) = 5 \int_0^1 (25t^2 - 25t + 4)\,dt \\
> &= 5 \left[ \frac{25t^3}{3} - \frac{25t^2}{2} + 4t \right]_0^1 = 5 \cdot \frac{50 - 75 + 24}{6} = -\frac56 .
> \end{aligned}
> $$
>
> **(b)** The parabola is given as a function of $y$, so take $y$ as the parameter: $x = 4 - y^2$, $y = y$, $-3 \le y \le 2$. Then $dx = -2y\,dy$ and
>
> $$
> \begin{aligned}
> \int_{C_2} y^2\,dx + x\,dy &= \int_{-3}^{2} y^2(-2y)\,dy + (4 - y^2)\,dy = \int_{-3}^{2} (-2y^3 - y^2 + 4)\,dy \\
> &= \left[ -\frac{y^4}{2} - \frac{y^3}{3} + 4y \right]_{-3}^{2} = \left(-\frac83\right) - \left(-\frac{81}{2} - 3\right) = \frac{245}{6} = 40\tfrac56 .
> \end{aligned}
> $$
>
> The two curves have the same endpoints but give different answers: in general a line integral depends on the path, not only on its endpoints ([[§109 The Fundamental Theorem for Line Integrals#^def-109-1|Definition §109.1]] and the theorems after it say when it does not). The answers also depend on the direction: for $-C_1$, the segment from $(0, 2)$ to $(-5, -3)$, parametrized by $x = -5t$, $y = 2 - 5t$, $0 \le t \le 1$, one finds $\int_{-C_1} y^2\,dx + x\,dy = \frac56$.
>
> *Stewart: Example 16.2.4*

^ex-108-3

![[m233-108-1.svg]]
*[[§108 Line Integrals#^ex-108-3|Example §108.3]]: two paths from $(-5,-3)$ to $(0,2)$. Along the segment $C_1$ (blue) the integral of $y^2\,dx + x\,dy$ is $-\frac56$; along the parabola $x = 4 - y^2$ (red), which swings out to $(4, 0)$, it is $\frac{245}{6}$. Same endpoints, different values: a line integral depends on the path.*

> [!definition] Definition §108.5: Orientation of a Curve
> A parametrization $x = x(t)$, $y = y(t)$, $a \le t \le b$, determines an **orientation** of the curve $C$: the positive direction is the direction of increasing $t$, from the initial point $A = \mathbf{r}(a)$ to the terminal point $B = \mathbf{r}(b)$. The curve consisting of the same points as $C$ with the opposite orientation (from $B$ to $A$) is denoted $-C$.
>
> *Stewart: 16.2 (text)*

^def-108-5

> [!theorem] Theorem §108.4: Reversing the Orientation
> Line integrals with respect to $x$ and $y$ change sign when the orientation is reversed; the line integral with respect to arc length does not:
>
> $$
> \int_{-C} f(x, y)\,dx = -\int_C f(x, y)\,dx, \qquad \int_{-C} f(x, y)\,dy = -\int_C f(x, y)\,dy, \qquad \int_{-C} f(x, y)\,ds = \int_C f(x, y)\,ds .
> $$
>
> *Stewart: 16.2 (text)*

^thm-108-4

> [!remark] Remark: Why It Works
> In the Riemann sums, reversing $C$ swaps the roles of $P_{i-1}$ and $P_i$. Each $\Delta x_i = x_i - x_{i-1}$ and $\Delta y_i$ changes sign, while each arc length $\Delta s_i$ is positive either way.

^rem-108-2

> [!proof]+ Proof
> Let $\mathbf{r}(t) = \langle x(t), y(t) \rangle$, $a \le t \le b$, parametrize $C$. Then $\tilde{\mathbf{r}}(u) = \mathbf{r}(a + b - u)$, $a \le u \le b$, parametrizes $-C$: it starts at $\mathbf{r}(b)$ and ends at $\mathbf{r}(a)$. By the Chain Rule $\tilde{x}'(u) = -x'(a + b - u)$. By Formulas 7 and the substitution $t = a + b - u$, $dt = -du$ ([[§38 The Substitution Rule#^thm-38-3|Theorem §38.3]]),
>
> $$
> \int_{-C} f\,dx = \int_a^b f(\mathbf{r}(a + b - u))\,\big(-x'(a + b - u)\big)\,du = \int_b^a f(\mathbf{r}(t))\,\big(-x'(t)\big)\,(-dt) = -\int_a^b f(\mathbf{r}(t))\,x'(t)\,dt = -\int_C f\,dx .
> $$
>
> The same computation with $y$ in place of $x$ gives the second formula. For the third, $|\tilde{\mathbf{r}}'(u)| = |\mathbf{r}'(a + b - u)|$ (the minus sign disappears in the length), so by Formula 3
>
> $$
> \int_{-C} f\,ds = \int_a^b f(\mathbf{r}(a + b - u))\,|\mathbf{r}'(a + b - u)|\,du = \int_b^a f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,(-dt) = \int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt = \int_C f\,ds .
> $$
>
> (Since the values do not depend on the parametrization, computing them with $\tilde{\mathbf{r}}$ is legitimate.)

^pf-108-4

*Uses:* [[§108 Line Integrals#^thm-108-1|§108.1]], [[§108 Line Integrals#^thm-108-2|§108.2]], [[§108 Line Integrals#^def-108-5|Def. §108.5]], [[§38 The Substitution Rule#^thm-38-3|§38.3]]

> [!remark]- Connections
> - Complex-variables version: [[§44 Contour Integrals#^thm-44-2|342 Thm. §44.2]] (reversing a contour changes the sign of a contour integral, and integrals add over pieces).

## Line Integrals in Space

> [!definition] Definition §108.6: Line Integrals in Space
> Let $C$ be a smooth space curve with parametric equations $x = x(t)$, $y = y(t)$, $z = z(t)$, $a \le t \le b$ (vector equation $\mathbf{r}(t) = x(t)\,\mathbf{i} + y(t)\,\mathbf{j} + z(t)\,\mathbf{k}$), and $f$ a function of three variables, continuous on a region containing $C$. With the subarcs, sample points and $\Delta s_i$ as in the plane, the **line integral of $f$ along $C$** (with respect to arc length) is
>
> $$
> \int_C f(x, y, z)\,ds = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*, y_i^*, z_i^*)\,\Delta s_i .
> $$
>
> Line integrals with respect to $x$, $y$ and $z$ are defined as in the plane; for instance
>
> $$
> \int_C f(x, y, z)\,dz = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*, y_i^*, z_i^*)\,\Delta z_i .
> $$
>
> *Stewart: 16.2 (text)*

^def-108-6

> [!theorem] Theorem §108.5: Evaluating Line Integrals in Space
> $$
> \int_C f(x, y, z)\,ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt \qquad (9)
> $$
>
> In vector notation, Formulas 3 and 9 both read $\displaystyle\int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt$. For $f = 1$ this gives $\displaystyle\int_C ds = \int_a^b |\mathbf{r}'(t)|\,dt = L$, the length of $C$ ([[§88 Arc Length and Curvature#^thm-88-1|Theorem §88.1]]). Also
>
> $$
> \int_C f(x, y, z)\,dz = \int_a^b f(x(t), y(t), z(t))\,z'(t)\,dt ,
> $$
>
> and similarly for $dx$ and $dy$. So integrals of the form
>
> $$
> \int_C P(x, y, z)\,dx + Q(x, y, z)\,dy + R(x, y, z)\,dz \qquad (10)
> $$
>
> are evaluated by expressing everything ($x, y, z, dx, dy, dz$) in terms of the parameter $t$.
>
> *Stewart: 16.2, Formulas 9 and 10*

^thm-108-5

*As in the plane, Stewart states these formulas without proof (see the note after [[§108 Line Integrals#^thm-108-1|Theorem §108.1]]).*

> [!example] Example §108.4: A Broken Line in Space
> Evaluate $\int_C y\,dx + z\,dy + x\,dz$, where $C$ consists of the line segment $C_1$ from $(2, 0, 0)$ to $(3, 4, 5)$, followed by the vertical line segment $C_2$ from $(3, 4, 5)$ to $(3, 4, 0)$.
>
> **On $C_1$.** By (8), $\mathbf{r}(t) = (1 - t)\langle 2, 0, 0 \rangle + t\langle 3, 4, 5 \rangle = \langle 2 + t, 4t, 5t \rangle$, that is, $x = 2 + t$, $y = 4t$, $z = 5t$, $0 \le t \le 1$. So $dx = dt$, $dy = 4\,dt$, $dz = 5\,dt$, and
>
> $$
> \int_{C_1} y\,dx + z\,dy + x\,dz = \int_0^1 (4t)\,dt + (5t)\,4\,dt + (2 + t)\,5\,dt = \int_0^1 (10 + 29t)\,dt = 10 + \frac{29}{2} = 24.5 .
> $$
>
> **On $C_2$.** $\mathbf{r}(t) = (1 - t)\langle 3, 4, 5 \rangle + t\langle 3, 4, 0 \rangle = \langle 3, 4, 5 - 5t \rangle$, so $x = 3$, $y = 4$, $z = 5 - 5t$. Then $dx = 0 = dy$, $dz = -5\,dt$, and
>
> $$
> \int_{C_2} y\,dx + z\,dy + x\,dz = \int_0^1 3\,(-5)\,dt = -15 .
> $$
>
> Adding, $\int_C y\,dx + z\,dy + x\,dz = 24.5 - 15 = 9.5$.
>
> *Stewart: Example 16.2.6*

^ex-108-4

*The section continues in [[§108a Line Integrals of Vector Fields]].*
