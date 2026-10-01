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

*Stewart, Section 16.2 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q6b), Practice Final Exam (Q3).*

A line integral is like a single integral, except that the interval $[a, b]$ is replaced by a curve $C$. There are two kinds. The line integral of a scalar function with respect to arc length, $\int_C f\,ds$, weights each bit of the curve by its length; it gives the mass of a wire or the area of a curtain over $C$. The line integral of a vector field, $\int_C \mathbf{F} \cdot d\mathbf{r}$, adds up the component of $\mathbf{F}$ along the direction of travel; it is the work done by a force field. Both are computed the same way: parametrize $C$ and turn the line integral into an ordinary integral in the parameter. The first kind does not depend on the direction in which $C$ is traversed; the second changes sign when the direction is reversed.

## Line Integrals in the Plane

Let $C$ be a plane curve with parametric equations

$$
x = x(t), \qquad y = y(t), \qquad a \le t \le b, \qquad (1)
$$

or vector equation $\mathbf{r}(t) = x(t)\,\mathbf{i} + y(t)\,\mathbf{j}$, and assume that $C$ is a **smooth curve**: $\mathbf{r}'$ is continuous and $\mathbf{r}'(t) \ne \mathbf{0}$ ([[§87 Derivatives and Integrals of Vector Functions|§87]]). Divide $[a, b]$ into $n$ subintervals $[t_{i-1}, t_i]$ of equal width. The points $P_i = (x(t_i), y(t_i))$ divide $C$ into $n$ subarcs, of lengths $\Delta s_1, \ldots, \Delta s_n$. Choose a point $P_i^*(x_i^*, y_i^*)$ in the $i$th subarc (it corresponds to some $t_i^*$ in $[t_{i-1}, t_i]$).

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
> If $f$ is continuous, the limit in Definition §108.1 always exists, and
>
> $$
> \int_C f(x, y)\,ds = \int_a^b f(x(t), y(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt . \qquad (3)
> $$
>
> The value does not depend on the parametrization of $C$, provided that $C$ is traversed exactly once as $t$ increases from $a$ to $b$.
>
> *Stewart: 16.2, Equation 3*

^thm-108-1

*Stewart only indicates the proof ("a similar type of argument" to the arc length formula of [[§64 Calculus with Parametric Curves|§64]]); the derivation with the Mean Value Theorem and uniform continuity is in [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]].*

> [!remark]- Connections
> - 452 takes Formula 3 as the definition of the scalar line integral and derives it from the Riemann sums: [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]]. One dimension up it becomes the scalar surface integral [[§18 Surface Integrals#^def-18-5|452 Def. §18.5]] ([[§113 Surface Integrals#^thm-113-1|Theorem §113.1]] here).

> [!remark] Remark: Reading Formula 3
> - **How to remember it.** If $s(t)$ is the length of $C$ between $\mathbf{r}(a)$ and $\mathbf{r}(t)$, then ([[§88 Arc Length and Curvature|§88]])
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

> [!definition] Definition §108.3: Mass and Center of Mass of a Wire
> If $\rho(x, y)$ is the linear density at the point $(x, y)$ of a thin wire shaped like a curve $C$, the **mass** of the wire is
>
> $$
> m = \lim_{n \to \infty} \sum_{i=1}^{n} \rho(x_i^*, y_i^*)\,\Delta s_i = \int_C \rho(x, y)\,ds ,
> $$
>
> and its **center of mass** is the point $(\bar{x}, \bar{y})$, where
>
> $$
> \bar{x} = \frac1m \int_C x\,\rho(x, y)\,ds, \qquad \bar{y} = \frac1m \int_C y\,\rho(x, y)\,ds . \qquad (4)
> $$
>
> *Stewart: 16.2, Equations 4*

^def-108-3

For example, a semicircular wire $x^2 + y^2 = 1$, $y \ge 0$, with density $\rho = k(1 - y)$ (thicker near its base) has $m = \int_0^{\pi} k(1 - \sin t)\,dt = k(\pi - 2)$ and, by symmetry and (4), center of mass $\left(0, \frac{4 - \pi}{2(\pi - 2)}\right) \approx (0, 0.38)$ (Stewart Example 16.2.3).

## Line Integrals with Respect to x and y

> [!definition] Definition §108.4: Line Integrals with Respect to x and y
> Replacing $\Delta s_i$ in Definition §108.1 by $\Delta x_i = x_i - x_{i-1}$ or by $\Delta y_i = y_i - y_{i-1}$ gives the **line integrals of $f$ along $C$ with respect to $x$ and $y$**:
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
> Rewrite (8) as $\mathbf{r}(t) = \mathbf{r}_0 + t\,(\mathbf{r}_1 - \mathbf{r}_0)$. For all real $t$ this is the vector equation of the line through $\mathbf{r}_0$ with direction vector $\mathbf{r}_1 - \mathbf{r}_0$ ([[§84 Equations of Lines and Planes|§84]]). At $t = 0$ it gives $\mathbf{r}_0$ and at $t = 1$ it gives $\mathbf{r}_1$, and as $t$ increases from $0$ to $1$ the point moves along the line from $\mathbf{r}_0$ to $\mathbf{r}_1$, once.

^pf-108-3

*Uses:* [[§84 Equations of Lines and Planes|§84]] (vector equation of a line)

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
> The two curves have the same endpoints but give different answers: in general a line integral depends on the path, not only on its endpoints ([[§109 The Fundamental Theorem for Line Integrals#^def-109-1|§109]] studies when it does not). The answers also depend on the direction: for $-C_1$, the segment from $(0, 2)$ to $(-5, -3)$, parametrized by $x = -5t$, $y = 2 - 5t$, $0 \le t \le 1$, one finds $\int_{-C_1} y^2\,dx + x\,dy = \frac56$.
>
> *Stewart: Example 16.2.4*

^ex-108-3

![[m233-108-1.svg]]
*Example §108.3: two paths from $(-5,-3)$ to $(0,2)$. Along the segment $C_1$ (blue) the integral of $y^2\,dx + x\,dy$ is $-\frac56$; along the parabola $x = 4 - y^2$ (red), which swings out to $(4, 0)$, it is $\frac{245}{6}$. Same endpoints, different values: a line integral depends on the path.*

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
> Let $\mathbf{r}(t) = \langle x(t), y(t) \rangle$, $a \le t \le b$, parametrize $C$. Then $\tilde{\mathbf{r}}(u) = \mathbf{r}(a + b - u)$, $a \le u \le b$, parametrizes $-C$: it starts at $\mathbf{r}(b)$ and ends at $\mathbf{r}(a)$. By the Chain Rule $\tilde{x}'(u) = -x'(a + b - u)$. By Formulas 7 and the substitution $t = a + b - u$, $dt = -du$ ([[§38 The Substitution Rule|§38]]),
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

*Uses:* [[§108 Line Integrals#^thm-108-1|§108.1]], [[§108 Line Integrals#^thm-108-2|§108.2]], [[§108 Line Integrals#^def-108-5|Def. §108.5]], [[§38 The Substitution Rule|§38]] (substitution in definite integrals)

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
> In vector notation, Formulas 3 and 9 both read $\displaystyle\int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt$. For $f = 1$ this gives $\displaystyle\int_C ds = \int_a^b |\mathbf{r}'(t)|\,dt = L$, the length of $C$ ([[§88 Arc Length and Curvature|§88]]). Also
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

## Line Integrals of Vector Fields; Work

> [!remark] Remark: Where the Work Integral Comes From
> A constant force $\mathbf{F}$ moving an object along the displacement $\mathbf{D}$ does work $\mathbf{F} \cdot \mathbf{D}$ ([[§82 The Dot Product|§82]]). Now let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ be a continuous force field on $\mathbb{R}^3$ and $C$ a smooth curve, divided into subarcs $P_{i-1}P_i$ of lengths $\Delta s_i$ as before. If $\Delta s_i$ is small, the particle moving from $P_{i-1}$ to $P_i$ proceeds approximately in the direction of $\mathbf{T}(t_i^*)$, the unit tangent vector at $P_i^*$, so the work done along that subarc is approximately
>
> $$
> \mathbf{F}(x_i^*, y_i^*, z_i^*) \cdot \big[\Delta s_i\,\mathbf{T}(t_i^*)\big] = \big[\mathbf{F}(x_i^*, y_i^*, z_i^*) \cdot \mathbf{T}(t_i^*)\big]\,\Delta s_i ,
> $$
>
> and the total work is approximately the Riemann sum $\sum_{i=1}^{n} \big[\mathbf{F}(x_i^*, y_i^*, z_i^*) \cdot \mathbf{T}(x_i^*, y_i^*, z_i^*)\big]\,\Delta s_i$. $\qquad (11)$

^rem-108-3

> [!definition] Definition §108.7: Work
> The **work** $W$ done by the force field $\mathbf{F}$ in moving a particle along $C$ is the limit of the Riemann sums (11):
>
> $$
> W = \int_C \mathbf{F}(x, y, z) \cdot \mathbf{T}(x, y, z)\,ds = \int_C \mathbf{F} \cdot \mathbf{T}\,ds . \qquad (12)
> $$
>
> In words: *work is the line integral with respect to arc length of the tangential component of the force.*
>
> *Stewart: 16.2, Equation 12*

^def-108-7

If $C$ is given by $\mathbf{r}(t)$, then $\mathbf{T}(t) = \mathbf{r}'(t)/|\mathbf{r}'(t)|$, and Formula 9 turns (12) into

$$
W = \int_a^b \left[ \mathbf{F}(\mathbf{r}(t)) \cdot \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} \right] |\mathbf{r}'(t)|\,dt = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt .
$$

This integral is abbreviated $\int_C \mathbf{F} \cdot d\mathbf{r}$, and it makes sense for any continuous vector field.

> [!definition] Definition §108.8: Line Integral of a Vector Field
> Let $\mathbf{F}$ be a continuous vector field defined on a smooth curve $C$ given by a vector function $\mathbf{r}(t)$, $a \le t \le b$. The **line integral of $\mathbf{F}$ along $C$** is
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_C \mathbf{F} \cdot \mathbf{T}\,ds .
> $$
>
> Here $\mathbf{F}(\mathbf{r}(t))$ abbreviates $\mathbf{F}(x(t), y(t), z(t))$, and formally $d\mathbf{r} = \mathbf{r}'(t)\,dt$.
>
> *Stewart: 16.2, Definition 13*

^def-108-8

> [!remark]- Connections
> - The work integral in 452: [[§16 Line Integrals and Green's Theorem#^def-16-2|452 Def. §16.2]]. In the language of forms it is the integral of the 1-form $P\,dx + Q\,dy + R\,dz$, computed by pulling it back along $\mathbf{r}$: [[§22 The Algebra of Differential Forms#^ex-22-2|452 Ex. §22.2]], [[§22 The Algebra of Differential Forms#^def-22-5|452 Def. §22.5]].

> [!theorem] Theorem §108.6: Reversing the Orientation of a Vector Line Integral
> $$
> \int_{-C} \mathbf{F} \cdot d\mathbf{r} = -\int_C \mathbf{F} \cdot d\mathbf{r} .
> $$
>
> *Stewart: 16.2 (text)*

^thm-108-6

> [!proof]+ Proof
> $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F} \cdot \mathbf{T}\,ds$, and integrals with respect to arc length do not change when the orientation is reversed ([[§108 Line Integrals#^thm-108-4|Theorem §108.4]]). But the integrand does: replacing $C$ by $-C$ replaces the unit tangent vector $\mathbf{T}$ by $-\mathbf{T}$. Hence $\int_{-C} \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F} \cdot (-\mathbf{T})\,ds = -\int_C \mathbf{F} \cdot d\mathbf{r}$.

^pf-108-6

*Uses:* [[§108 Line Integrals#^def-108-8|Def. §108.8]], [[§108 Line Integrals#^thm-108-4|§108.4]]

> [!theorem] Theorem §108.7: Vector Line Integrals in Component Form
> If $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ is a vector field on $\mathbb{R}^3$, then
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C P\,dx + Q\,dy + R\,dz .
> $$
>
> Similarly, for a vector field $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ on $\mathbb{R}^2$,
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C P\,dx + Q\,dy . \qquad (14)
> $$
>
> *Stewart: 16.2 (text) and Equation 14*

^thm-108-7

> [!proof]+ Proof
> By Definition §108.8,
>
> $$
> \begin{aligned}
> \int_C \mathbf{F} \cdot d\mathbf{r} &= \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_a^b (P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}) \cdot \big(x'(t)\,\mathbf{i} + y'(t)\,\mathbf{j} + z'(t)\,\mathbf{k}\big)\,dt \\
> &= \int_a^b \Big[ P(x(t), y(t), z(t))\,x'(t) + Q(x(t), y(t), z(t))\,y'(t) + R(x(t), y(t), z(t))\,z'(t) \Big]\,dt .
> \end{aligned}
> $$
>
> By [[§108 Line Integrals#^thm-108-5|Theorem §108.5]] this last integral is precisely the line integral (10). The plane case is the same computation without the $z$ terms, using Formulas 7.

^pf-108-7

*Uses:* [[§108 Line Integrals#^def-108-8|Def. §108.8]], [[§108 Line Integrals#^thm-108-5|§108.5]], [[§108 Line Integrals#^thm-108-2|§108.2]]

For example, the integral of [[§108 Line Integrals#^ex-108-4|Example §108.4]] is $\int_C \mathbf{F} \cdot d\mathbf{r}$ for $\mathbf{F}(x, y, z) = y\,\mathbf{i} + z\,\mathbf{j} + x\,\mathbf{k}$.

> [!remark] Remark: Method — Evaluating a Line Integral
> 1. **Parametrize the curve** by $\mathbf{r}(t)$, $a \le t \le b$, in the direction of travel. Use (8) for segments, $x = x$, $y = g(x)$ (or $y$ as the parameter) for graphs, and $(\cos t, \sin t)$-type parametrizations for circles; for the curve of intersection of two surfaces, parametrize the simpler one (for a cylinder $x^2 + y^2 = a^2$, take $x = a\cos t$, $y = a\sin t$) and solve the other for the remaining coordinate. Split a piecewise-smooth curve into smooth pieces.
> 2. **Compute $\mathbf{r}'(t)$**, and $ds = |\mathbf{r}'(t)|\,dt$ for an integral with respect to arc length.
> 3. **Substitute** $x = x(t)$, $y = y(t)$, $z = z(t)$ into $f$ or $\mathbf{F}$, and $dx = x'(t)\,dt$ etc.:
>    $\int_C f\,ds = \int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt$, $\quad\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt$.
> 4. **Integrate in $t$** and add the pieces. If the parametrization runs against the given orientation, change the sign of $dx$, $dy$, $dz$ and $d\mathbf{r}$ integrals (not of $ds$ integrals).
> 5. **Look for shortcuts first**: a conservative field ([[§109 The Fundamental Theorem for Line Integrals#^thm-109-1|Theorem §109.1]]), or a closed curve in the plane or in space bounding a simple region or surface (Green's Theorem, [[§110 Green's Theorem#^thm-110-1|Theorem §110.1]]; Stokes' Theorem, [[§114 Stokes' Theorem#^thm-114-1|Theorem §114.1]]).

^rem-108-4

> [!example] Example §108.5: Work along a Segment
> Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $\mathbf{F}(x, y) = xy^2\,\mathbf{i} - x\,\mathbf{j}$ and $C$ is given by $\mathbf{r}(t) = (1 + t)\,\mathbf{i} + (2 - t)\,\mathbf{j}$, $0 \le t \le 2$.
>
> Here $\mathbf{r}'(t) = \mathbf{i} - \mathbf{j}$ and $\mathbf{F}(\mathbf{r}(t)) = (1 + t)(2 - t)^2\,\mathbf{i} - (1 + t)\,\mathbf{j}$, so
>
> $$
> \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) = (1 + t)(2 - t)^2 + (1 + t) = (1 + t)(t^2 - 4t + 5) = t^3 - 3t^2 + t + 5 .
> $$
>
> Therefore
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_0^2 (t^3 - 3t^2 + t + 5)\,dt = \left[ \frac{t^4}{4} - t^3 + \frac{t^2}{2} + 5t \right]_0^2 = 4 - 8 + 2 + 10 = 8 .
> $$
>
> (Is there a shortcut? $\partial P/\partial y = 2xy$ and $\partial Q/\partial x = -1$ are not equal, so $\mathbf{F}$ is not conservative ([[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Theorem §109.4]]) and the integral must be computed along the curve.)
>
> *Source: 233 Practice Final Exam, Q3*

^ex-108-5
