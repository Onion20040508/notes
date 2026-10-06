---
type: section
subject: "[[Calculus]]"
chapter: 6
section: 45
stewart: "6.1"
aliases: ["Stewart 6.1"]
tags: [calculus]
---
← [[§44 The Area Under y = x² from 0 to 1]] · ↑ [[· 6 Applications of Integration]] · [[§46 Volumes]] →

*Stewart, Section 6.1.*

Chapter 5 computed areas under a single graph. Here the region lies between two graphs, and the rectangle approximating a thin strip has height "top minus bottom". The area is then the integral of $f - g$. When the curves cross, the integrand becomes $|f - g|$ and the integral is split at the crossings. Some regions are better cut into horizontal strips, which means integrating with respect to $y$. The section is the first instance of the pattern of the whole chapter: approximate a small piece, add the pieces in a Riemann sum, and recognize the limit as an integral.

## Area Between Curves: Integrating with Respect to x

Let $S$ be the region between the curves $y = f(x)$ and $y = g(x)$ and the vertical lines $x = a$ and $x = b$, where $f$ and $g$ are continuous and $f(x) \ge g(x)$ on $[a, b]$:

$$
S = \{(x, y) \mid a \le x \le b,\ g(x) \le y \le f(x)\} .
$$

As in [[§38 The Area and Distance Problems#^def-38-1|Definition §38.1]], divide $S$ into $n$ strips of equal width $\Delta x$ and approximate the $i$th strip by a rectangle with base $\Delta x$ and height $f(x_i^*) - g(x_i^*)$. The Riemann sum $\sum_{i=1}^{n} [f(x_i^*) - g(x_i^*)]\,\Delta x$ approximates what we intuitively mean by the area of $S$.

> [!definition] Definition §45.1: Area Between Two Curves
> The **area** $A$ of the region $S$ is the limiting value of the sum of the areas of the approximating rectangles:
>
> $$
> A = \lim_{n \to \infty} \sum_{i=1}^{n} [f(x_i^*) - g(x_i^*)]\,\Delta x .
> $$
>
> When $g = 0$, $S$ is the region under the graph of $f$, and this is [[§38 The Area and Distance Problems#^def-38-1|Definition §38.1]].
>
> *Stewart: 6.1, Equation 1*

^def-45-1

> [!remark] Remark: Why It Works
> When $f$ and $g$ are both positive, the region $S$ is the region under $y = f(x)$ with the region under $y = g(x)$ removed, so
>
> $$
> A = [\text{area under } y = f(x)] - [\text{area under } y = g(x)] = \int_a^b f(x)\,dx - \int_a^b g(x)\,dx = \int_a^b [f(x) - g(x)]\,dx .
> $$

^rem-45-1

> [!theorem] Theorem §52.1: Area Between Curves
> The area $A$ of the region bounded by the curves $y = f(x)$, $y = g(x)$ and the lines $x = a$, $x = b$, where $f$ and $g$ are continuous and $f(x) \ge g(x)$ for all $x$ in $[a, b]$, is
>
> $$
> A = \int_a^b [f(x) - g(x)]\,dx .
> $$
>
> *Stewart: 6.1, Equation 2*

^thm-45-1

> [!proof]+ Proof
> The function $f - g$ is continuous on $[a, b]$, hence integrable ([[§39 The Definite Integral#^thm-39-1|Theorem §39.1]]). So the limit in [[§45 Areas Between Curves#^def-45-1|Definition §45.1]] exists for every choice of sample points, and by the definition of the integral ([[§39 The Definite Integral#^def-39-1|Definition §39.1]]) it equals $\int_a^b [f(x) - g(x)]\,dx$.

^pf-45-1

*Uses:* [[§45 Areas Between Curves#^def-45-1|Def. §45.1]], [[§39 The Definite Integral#^def-39-1|Def. §39.1]], [[§39 The Definite Integral#^thm-39-1|§39.1]]

> [!remark]- Connections
> - The same area as a double integral: $\iint_S 1\,dA$ over a type I region ([[§116 Double Integrals Over General Regions#^thm-116-5|Theorem §116.5]], [[§116 Double Integrals Over General Regions#^thm-116-1|Theorem §116.1]]). Its iterated form $\int_a^b \int_{g(x)}^{f(x)} 1\,dy\,dx$ is exactly [[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]], and the rigorous version is Fubini for type I regions, [[§23 Fubini's Theorem#^thm-23-2|452 Thm. §23.2]].

> [!remark] Remark: Method — Area Between Curves
> 1. **Sketch the region.** Identify the top curve $y_T$, the bottom curve $y_B$, and a typical approximating rectangle of width $\Delta x$ and height $y_T - y_B$.
> 2. **Find the limits.** If the sides are not given as lines $x = a$, $x = b$ (a side may shrink to a point), find the $x$-coordinates of the points where the curves meet by solving $y_T = y_B$. If they cannot be found exactly, locate them approximately with a graph and a computer and proceed in the same way (Stewart, Example 6.1.3).
> 3. **Add up the rectangles**: $\displaystyle A = \lim_{n \to \infty} \sum_{i=1}^{n} (y_T - y_B)\,\Delta x = \int_a^b (y_T - y_B)\,dx$.
> 4. **If the curves cross**, top and bottom trade places: split the interval at the crossings ([[§45 Areas Between Curves#^thm-45-2|Theorem §45.2]]).
> 5. **If the top or bottom boundary consists of different curves**, consider integrating with respect to $y$ instead ([[§45 Areas Between Curves#^thm-45-3|Theorem §45.3]]).

^rem-45-2

> [!example] Example §52.1: Top Minus Bottom
> **(a)** Find the area of the region bounded above by $y = e^x$, below by $y = x$, and on the sides by $x = 0$ and $x = 1$.
>
> The upper boundary is $y = e^x$ and the lower one $y = x$ (indeed $e^x > x$ for all $x$). By [[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]] with $f(x) = e^x$, $g(x) = x$, $a = 0$, $b = 1$,
>
> $$
> A = \int_0^1 (e^x - x)\,dx = e^x - \tfrac12 x^2 \Big]_0^1 = e - \tfrac12 - 1 = e - 1.5 .
> $$
>
> **(b)** Find the area of the region enclosed by the parabolas $y = x^2$ and $y = 2x - x^2$.
>
> Both sides of the region shrink to points, so first find where the curves meet: $x^2 = 2x - x^2$ gives $2x^2 - 2x = 0$, that is $2x(x - 1) = 0$, so $x = 0$ or $x = 1$. The points of intersection are $(0, 0)$ and $(1, 1)$. Between them $y_T = 2x - x^2$ and $y_B = x^2$ (at $x = \frac12$: $\frac34 > \frac14$). A typical rectangle has area $(y_T - y_B)\,\Delta x = (2x - 2x^2)\,\Delta x$, so
>
> $$
> A = \int_0^1 (2x - 2x^2)\,dx = 2 \int_0^1 (x - x^2)\,dx = 2 \Big[\frac{x^2}{2} - \frac{x^3}{3}\Big]_0^1 = 2 \Big(\frac12 - \frac13\Big) = \frac13 .
> $$
>
> *Stewart: Examples 6.1.1 and 6.1.2*

^ex-45-1

If $f(x) \ge g(x)$ for some values of $x$ but $g(x) \ge f(x)$ for others, split the region $S$ into regions $S_1, S_2, \ldots$ on which one curve stays on top, with areas $A_1, A_2, \ldots$, and *define* the area of $S$ to be $A = A_1 + A_2 + \cdots$.

> [!theorem] Theorem §52.2: Area Between Crossing Curves
> The area between the curves $y = f(x)$ and $y = g(x)$ (continuous) and between $x = a$ and $x = b$ is
>
> $$
> A = \int_a^b |f(x) - g(x)|\,dx .
> $$
>
> To evaluate it, the integral must still be split into the integrals giving $A_1, A_2, \ldots$.
>
> *Stewart: 6.1, Equation 3*

^thm-45-2

> [!proof]+ Proof
> Since
>
> $$
> |f(x) - g(x)| = \begin{cases} f(x) - g(x) & \text{when } f(x) \ge g(x) \\ g(x) - f(x) & \text{when } g(x) \ge f(x) , \end{cases}
> $$
>
> on each piece $[c, d]$ of the subdivision where one curve stays on top, [[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]] gives the area of that piece as $\int_c^d |f(x) - g(x)|\,dx$. Adding over the pieces and using Property 5 of integrals ([[§40 Properties of the Definite Integral#^thm-40-2|Theorem §40.2]]) gives $A_1 + A_2 + \cdots = \int_a^b |f(x) - g(x)|\,dx$. ($|f - g|$ is continuous, so the integral exists.)

^pf-45-2

*Uses:* [[§45 Areas Between Curves#^thm-45-1|§45.1]], [[§40 Properties of the Definite Integral#^thm-40-2|§40.2]]

> [!example] Example §52.2: Sine and Cosine
> Find the area of the region bounded by the curves $y = \sin x$, $y = \cos x$, $x = 0$ and $x = \pi/2$.
>
> The curves meet where $\sin x = \cos x$, that is, at $x = \pi/4$ (the only solution in $[0, \pi/2]$). On $[0, \pi/4]$, $\cos x \ge \sin x$; on $[\pi/4, \pi/2]$, $\sin x \ge \cos x$. By [[§45 Areas Between Curves#^thm-45-2|Theorem §45.2]],
>
> $$
> \begin{aligned}
> A &= \int_0^{\pi/2} |\cos x - \sin x|\,dx = A_1 + A_2 = \int_0^{\pi/4} (\cos x - \sin x)\,dx + \int_{\pi/4}^{\pi/2} (\sin x - \cos x)\,dx \\
> &= \Big[\sin x + \cos x\Big]_0^{\pi/4} + \Big[-\cos x - \sin x\Big]_{\pi/4}^{\pi/2}
> = \Big(\frac{1}{\sqrt2} + \frac{1}{\sqrt2} - 0 - 1\Big) + \Big(-0 - 1 + \frac{1}{\sqrt2} + \frac{1}{\sqrt2}\Big) = 2\sqrt2 - 2 .
> \end{aligned}
> $$
>
> The region is symmetric about $x = \pi/4$ (the reflection $x \mapsto \frac{\pi}{2} - x$ exchanges $\sin$ and $\cos$), so $A = 2A_1 = 2\int_0^{\pi/4} (\cos x - \sin x)\,dx$ would have saved some work.
>
> *Stewart: Example 6.1.4*

^ex-45-2

## Area Between Curves: Integrating with Respect to y

Some regions are best treated by regarding $x$ as a function of $y$.

> [!theorem] Theorem §52.3: Area Between Curves, Integrating with Respect to y
> If a region is bounded by curves $x = f(y)$, $x = g(y)$, $y = c$ and $y = d$, where $f$ and $g$ are continuous and $f(y) \ge g(y)$ for $c \le y \le d$, then its area is
>
> $$
> A = \int_c^d [f(y) - g(y)]\,dy .
> $$
>
> With $x_R$ for the right boundary and $x_L$ for the left boundary, $A = \displaystyle\int_c^d (x_R - x_L)\,dy$: a typical approximating rectangle now is horizontal, with dimensions $x_R - x_L$ and $\Delta y$.
>
> *Stewart: 6.1 (text)*

^thm-45-3

> [!proof]+ Proof
> Interchange the roles of $x$ and $y$ in [[§45 Areas Between Curves#^def-45-1|Definition §45.1]] and [[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]]: divide $[c, d]$ into $n$ subintervals of width $\Delta y$, approximate the $i$th horizontal strip by a rectangle of length $f(y_i^*) - g(y_i^*)$ and width $\Delta y$, and define the area as the limit of the sum of these areas. Since $f - g$ is continuous, the limit is $\int_c^d [f(y) - g(y)]\,dy$. (Reflecting the plane in the line $y = x$ turns the region into one of the type in [[§45 Areas Between Curves#^thm-45-1|Theorem §45.1]] without changing areas.)

^pf-45-3

*Uses:* [[§45 Areas Between Curves#^thm-45-1|§45.1]], [[§39 The Definite Integral#^def-39-1|Def. §39.1]]

> [!example] Example §52.3: A Parabola and a Line
> Find the area enclosed by the line $y = x - 1$ and the parabola $y^2 = 2x + 6$.
>
> **Intersections.** From the line, $x = y + 1$; substituting, $y^2 = 2(y + 1) + 6$, that is $y^2 - 2y - 8 = (y - 4)(y + 2) = 0$. So $y = 4$ or $y = -2$, and the points of intersection are $(5, 4)$ and $(-1, -2)$.
>
> **Integrating in $y$.** Solving the parabola for $x$, the left and right boundaries are $x_L = \frac12 y^2 - 3$ and $x_R = y + 1$, for $-2 \le y \le 4$. By [[§45 Areas Between Curves#^thm-45-3|Theorem §45.3]],
>
> $$
> \begin{aligned}
> A &= \int_{-2}^{4} (x_R - x_L)\,dy = \int_{-2}^{4} \Big[(y + 1) - \big(\tfrac12 y^2 - 3\big)\Big]\,dy = \int_{-2}^{4} \big(-\tfrac12 y^2 + y + 4\big)\,dy \\
> &= -\frac12 \Big(\frac{y^3}{3}\Big) + \frac{y^2}{2} + 4y \,\Big]_{-2}^{4} = \Big(-\tfrac16 (64) + 8 + 16\Big) - \Big(\tfrac43 + 2 - 8\Big) = \frac{40}{3} + \frac{14}{3} = 18 .
> \end{aligned}
> $$
>
> **Integrating in $x$** is possible but more involved, because the bottom boundary consists of two different curves: $y = -\sqrt{2x + 6}$ for $-3 \le x \le -1$ and $y = x - 1$ for $-1 \le x \le 5$. Splitting the region there,
>
> $$
> A_1 = \int_{-3}^{-1} 2\sqrt{2x + 6}\,dx = \tfrac23 (2x + 6)^{3/2} \Big]_{-3}^{-1} = \tfrac{16}{3}, \qquad
> A_2 = \int_{-1}^{5} \big[\sqrt{2x + 6} - (x - 1)\big]\,dx = \Big[\tfrac13 (2x + 6)^{3/2} - \tfrac12 x^2 + x\Big]_{-1}^{5} = \tfrac{38}{3} ,
> $$
>
> and $A_1 + A_2 = \frac{54}{3} = 18$ again.
>
> *Stewart: Example 6.1.5 and Note*

^ex-45-3

![[m233-39-1.svg]]
*[[§45 Areas Between Curves#^ex-45-3|Example §45.3]]. (a) Vertical rectangles run from the lower branch of the parabola up to the upper branch for $x < -1$, but from the line up to the parabola for $x > -1$: two integrals. (b) Every horizontal rectangle runs from the parabola $x_L$ to the line $x_R$, so one integral in $y$ suffices.*

> [!example] Example §52.4: Both Ways
> Find the area of the region enclosed by the curves $y = 1/x$, $y = x$ and $y = \frac14 x$, using (a) $x$ and (b) $y$ as the variable of integration.
>
> The region has corners at $(0, 0)$, at $(1, 1)$ (where $1/x = x$, $x > 0$) and at $(2, \frac12)$ (where $1/x = \frac14 x$, $x > 0$).
>
> **(a)** The top boundary consists of two curves, $y = x$ for $0 \le x \le 1$ and $y = 1/x$ for $1 \le x \le 2$; the bottom is $y = \frac14 x$ throughout. So
>
> $$
> A = A_1 + A_2 = \int_0^1 \big(x - \tfrac14 x\big)\,dx + \int_1^2 \Big(\frac1x - \frac14 x\Big)\,dx
> = \Big[\tfrac38 x^2\Big]_0^1 + \Big[\ln x - \tfrac18 x^2\Big]_1^2 = \tfrac38 + \big(\ln 2 - \tfrac12 + \tfrac18\big) = \ln 2 .
> $$
>
> **(b)** Now the left boundary is $x = y$ throughout, and the right boundary consists of two curves: $x = 4y$ for $0 \le y \le \frac12$ and $x = 1/y$ for $\frac12 \le y \le 1$. So
>
> $$
> A = A_1 + A_2 = \int_0^{1/2} (4y - y)\,dy + \int_{1/2}^{1} \Big(\frac1y - y\Big)\,dy
> = \Big[\tfrac32 y^2\Big]_0^{1/2} + \Big[\ln y - \tfrac12 y^2\Big]_{1/2}^{1} = \tfrac38 + \big(\ln 2 - \tfrac12 + \tfrac18\big) = \ln 2 .
> $$
>
> Here neither variable avoids the split; the two computations are equally long.
>
> *Stewart: Example 6.1.6*

^ex-45-4

## Applications

> [!example] Example §52.5: The Distance Between Two Cars
> Two cars, A and B, start side by side and move along the same road. Their velocity curves are given as graphs. What does the area between the curves represent? Estimate it with the Midpoint Rule.
>
> The area under the velocity curve of A is the distance traveled by car A in the first 16 seconds, and likewise for B ([[§42 Indefinite Integrals and the Net Change Theorem#^cor-42-3|Corollary §42.3]]). So the area between the curves, the difference of these two areas, is the distance between the cars after 16 seconds. Velocities read from the graphs and converted to ft/s ($1$ mi/h $= \frac{5280}{3600}$ ft/s):
>
> | $t$ | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 |
> |---|---|---|---|---|---|---|---|---|---|
> | $v_A$ | 0 | 34 | 54 | 67 | 76 | 84 | 89 | 92 | 95 |
> | $v_B$ | 0 | 21 | 34 | 44 | 51 | 56 | 60 | 63 | 65 |
> | $v_A - v_B$ | 0 | 13 | 20 | 23 | 25 | 28 | 29 | 29 | 30 |
>
> The Midpoint Rule ([[§39 The Definite Integral#^def-39-4|Definition §39.4]]) with $n = 4$, $\Delta t = 4$ uses the midpoints $\bar t_1 = 2$, $\bar t_2 = 6$, $\bar t_3 = 10$, $\bar t_4 = 14$:
>
> $$
> \int_0^{16} (v_A - v_B)\,dt \approx \Delta t\,[13 + 23 + 28 + 29] = 4(93) = 372 \text{ ft} .
> $$
>
> *Stewart: Example 6.1.7*

^ex-45-5

Stewart's Example 6.1.8 applies the same idea in epidemiology: for a measles pathogenesis curve modeled by $f(t) = -t(t - 21)(t + 1)$ (infected cells per mL on day $t$), the "level of infectiousness" between days $10$ and $18$ is the area between $N = f(t)$ and the chord from $(10, f(10)) = (10, 1210)$ to $(18, f(18)) = (18, 1026)$, namely $\int_{10}^{18} [f(t) - (-23t + 1440)]\,dt \approx 1877$ (cells/mL)·days.
