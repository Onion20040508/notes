---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 52
stewart: "8.1"
aliases: ["Stewart 8.1"]
tags: [calculus]
---
← [[§51 Improper Integrals]] · ↑ [[· 8 Further Applications of Integration]] · [[§53 Area of a Surface of Revolution]] →

*Stewart, Section 8.1.*

The length of a curve is defined the way the circumference of a circle is: inscribe polygonal paths with more and more sides and take the limit of their lengths. For the graph of a function with a continuous derivative, the Mean Value Theorem turns the polygon lengths into Riemann sums, and the limit becomes the integral $\int_a^b \sqrt{1 + [f'(x)]^2}\,dx$. Because of the square root these integrals can rarely be evaluated exactly, so the section also uses Simpson's Rule. The integrand is the derivative of the arc length function $s(x)$, and the differential $ds$, with $(ds)^2 = (dx)^2 + (dy)^2$, is used again for surface area in [[§53 Area of a Surface of Revolution#^def-53-2|§53]] and for parametric and space curves in [[§64 Calculus with Parametric Curves#^thm-64-4|Theorem §64.4]] and [[§88 Arc Length and Curvature#^thm-88-1|Theorem §88.1]].

## Arc Length of a Curve

> [!definition] Definition §52.1: Length of a Curve
> Let $C$ be the curve $y = f(x)$, $a \le x \le b$, where $f$ is continuous. Divide $[a, b]$ into $n$ subintervals with endpoints $x_0, x_1, \ldots, x_n$ and equal width $\Delta x$, and let $P_i = (x_i, y_i)$ with $y_i = f(x_i)$, the point of $C$ above $x_i$. The polygonal path with vertices $P_0, P_1, \ldots, P_n$ approximates $C$. The **length** $L$ of $C$ is the limit of the lengths of these paths, if the limit exists:
>
> $$
> L = \lim_{n \to \infty} \sum_{i=1}^n |P_{i-1} P_i| ,
> $$
>
> where $|P_{i-1} P_i| = \sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2}$ is the distance between $P_{i-1}$ and $P_i$.
>
> *Stewart: 8.1, Definition 1*

^def-52-1

![[m233-52-1.svg]]
*A polygonal path $P_0 P_1 \cdots P_n$ (red) inscribed in the curve $y = f(x)$ (blue), with vertices above equally spaced points $x_i$. The length of a polygon is a sum of distances. As $n$ grows, the chords hug the curve more closely, and their total length tends to the length of the curve.*

> [!remark] Remark: The Idea Behind the Definition
> The length of a polygon is the sum of the lengths of its segments, each found from the distance formula. The circumference of a circle is the limit of the perimeters of inscribed regular polygons as the number of sides grows. Definition §52.1 applies the same idea to any curve. It follows the pattern of the definitions of area ([[§34 The Area and Distance Problems#^def-34-1|Definition §34.1]]) and volume ([[§40 Volumes#^def-40-2|Definition §40.2]]): divide the object into many small parts, approximate each part by something whose size we know, add, and take the limit as $n \to \infty$.

^rem-52-1

> [!definition] Definition §52.2: Smooth Function
> A function $f$ is **smooth** on $[a, b]$ if its derivative $f'$ is continuous there: a small change in $x$ produces a small change in $f'(x)$.
>
> *Stewart: 8.1 (text)*

^def-52-2

> [!theorem] Theorem §52.1: The Arc Length Formula
> If $f'$ is continuous on $[a, b]$, then the length of the curve $y = f(x)$, $a \le x \le b$, is
>
> $$
> L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx .
> $$
>
> In Leibniz notation,
>
> $$
> L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx .
> $$
>
> *Stewart: 8.1, Formula 2 and Equation 3*

^thm-52-1

> [!proof]+ Proof
> Use the notation of Definition §52.1 and let $\Delta y_i = y_i - y_{i-1}$. Then
>
> $$
> |P_{i-1} P_i| = \sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2} = \sqrt{(\Delta x)^2 + (\Delta y_i)^2} .
> $$
>
> $f$ is differentiable on $[a, b]$, so the Mean Value Theorem applies to $f$ on each $[x_{i-1}, x_i]$: there is a number $x_i^*$ between $x_{i-1}$ and $x_i$ with
>
> $$
> f(x_i) - f(x_{i-1}) = f'(x_i^*)(x_i - x_{i-1}), \qquad\text{that is,}\qquad \Delta y_i = f'(x_i^*)\,\Delta x .
> $$
>
> Therefore, since $\Delta x > 0$,
>
> $$
> |P_{i-1} P_i| = \sqrt{(\Delta x)^2 + [f'(x_i^*)\,\Delta x]^2} = \sqrt{1 + [f'(x_i^*)]^2}\,\sqrt{(\Delta x)^2} = \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x ,
> $$
>
> and by Definition §52.1
>
> $$
> L = \lim_{n \to \infty} \sum_{i=1}^n |P_{i-1} P_i| = \lim_{n \to \infty} \sum_{i=1}^n \sqrt{1 + [f'(x_i^*)]^2}\,\Delta x .
> $$
>
> The last sum is a Riemann sum of $g(x) = \sqrt{1 + [f'(x)]^2}$ for the equal partition of $[a, b]$ with sample points $x_i^{\ast} \in [x_{i-1}, x_i]$. Since $f'$ is continuous, so is $g$; a continuous function is integrable, and then the Riemann sums tend to $\int_a^b g(x)\,dx$ for *every* choice of sample points ([[§35 The Definite Integral#^thm-35-1|Theorem §35.1]], [[§35 The Definite Integral#^def-35-1|Definition §35.1]]), in particular for the points $x_i^{\ast}$ supplied by the Mean Value Theorem. So the limit in Definition §52.1 exists and
>
> $$
> L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx .
> $$
>
> The Leibniz form is the same formula with $f'(x) = dy/dx$.

^pf-52-1

*Uses:* [[§52 Arc Length#^def-52-1|Def. §52.1]], [[§26 The Mean Value Theorem#^thm-26-2|§26.2]] (Mean Value Theorem), [[§35 The Definite Integral#^def-35-1|Def. §35.1]] (Riemann sums), [[§35 The Definite Integral#^thm-35-1|§35.1]] (continuous functions are integrable)

![[m233-52-2.svg]]
*One piece of the polygon. The chord $P_{i-1} P_i$ (red) is the hypotenuse of a right triangle with legs $\Delta x$ and $\Delta y_i$. By the Mean Value Theorem, some tangent line between $x_{i-1}$ and $x_i$ (green, at $x_i^{\ast}$) is parallel to the chord, so $\Delta y_i = f'(x_i^{\ast})\,\Delta x$ and $|P_{i-1} P_i| = \sqrt{1 + [f'(x_i^{\ast})]^2}\,\Delta x$, one term of a Riemann sum.*

> [!remark]- Connections
> - The analysis behind the proof: the Mean Value Theorem [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]; Riemann sums with arbitrary sample points and their limit for integrable functions, [[§32 The Definition of the Riemann Integral#^def-32-3|451 Def. §32.3]], with continuous functions integrable by [[§32 The Definition of the Riemann Integral#^thm-32-7|451 Thm. §32.7]].
> - The same derivation for a parametrized curve $(x(t), y(t))$ follows [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]]. There the two coordinates need two different Mean Value Theorem points, and uniform continuity of $x'$ and $y'$ closes the gap. Here $x$ itself is the parameter, so one point $x_i^*$ suffices.

> [!example] Example §52.1: A Semicubical Parabola
> Find the length of the arc of the semicubical parabola $y^2 = x^3$ between the points $(1, 1)$ and $(4, 8)$.
>
> Both points lie on the top half of the curve, $y = x^{3/2}$, for which
>
> $$
> \frac{dy}{dx} = \frac32 x^{1/2}, \qquad 1 + \left(\frac{dy}{dx}\right)^2 = 1 + \frac94 x .
> $$
>
> The derivative is continuous on $[1, 4]$, so by Theorem §52.1
>
> $$
> L = \int_1^4 \sqrt{1 + \tfrac94 x}\,dx .
> $$
>
> Substitute $u = 1 + \frac94 x$, $du = \frac94\,dx$. When $x = 1$, $u = \frac{13}{4}$; when $x = 4$, $u = 10$. So
>
> $$
> L = \frac49 \int_{13/4}^{10} \sqrt{u}\,du = \frac49 \cdot \frac23 u^{3/2} \Big]_{13/4}^{10} = \frac{8}{27}\left[10^{3/2} - \left(\tfrac{13}{4}\right)^{3/2}\right] = \frac{1}{27}\left(80\sqrt{10} - 13\sqrt{13}\right) ,
> $$
>
> using $\left(\frac{13}{4}\right)^{3/2} = \frac{13\sqrt{13}}{8}$.
>
> **Check.** $L \approx \frac{1}{27}(252.982 - 46.872) \approx 7.633705$. The arc should be slightly longer than the segment from $(1, 1)$ to $(4, 8)$, whose length is $\sqrt{3^2 + 7^2} = \sqrt{58} \approx 7.615773$. It is.
>
> *Stewart: Example 8.1.1*

^ex-52-1

> [!theorem] Theorem §52.2: Arc Length of a Curve x = g(y)
> If a curve has the equation $x = g(y)$, $c \le y \le d$, and $g'(y)$ is continuous, then its length is
>
> $$
> L = \int_c^d \sqrt{1 + [g'(y)]^2}\,dy = \int_c^d \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy .
> $$
>
> *Stewart: 8.1, Formula 4*

^thm-52-2

> [!proof]+ Proof
> Interchange the roles of $x$ and $y$. The length is defined as in Definition §52.1 with the roles of the axes exchanged: divide $[c, d]$ into $n$ equal parts at $y_0, \ldots, y_n$ and inscribe the polygon with vertices $(g(y_i), y_i)$. Reflecting in the line $y = x$, that is, $(x, y) \mapsto (y, x)$, carries this polygon to the polygon with vertices $(y_i, g(y_i))$ inscribed in the graph $y = g(x)$, $c \le x \le d$. The reflection preserves distances, since $\sqrt{(\Delta x)^2 + (\Delta y)^2}$ is symmetric in $\Delta x$ and $\Delta y$. So the two polygons have the same length for every $n$, and the two curves have the same length. By Theorem §52.1 applied to $y = g(x)$, that length is $\int_c^d \sqrt{1 + [g'(y)]^2}\,dy$ (renaming the variable of integration).

^pf-52-2

*Uses:* [[§52 Arc Length#^def-52-1|Def. §52.1]], [[§52 Arc Length#^thm-52-1|§52.1]]

> [!example] Example §52.2: A Parabola, Integrated in y
> Find the length of the arc of the parabola $y^2 = x$ from $(0, 0)$ to $(1, 1)$.
>
> **Choice of variable.** As a function of $x$ the arc is $y = \sqrt{x}$, whose derivative $\frac{1}{2\sqrt{x}}$ is unbounded at $x = 0$, so Theorem §52.1 does not apply on $[0, 1]$. As a function of $y$ it is $x = y^2$, $0 \le y \le 1$, with $dx/dy = 2y$ continuous. Theorem §52.2 gives
>
> $$
> L = \int_0^1 \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy = \int_0^1 \sqrt{1 + 4y^2}\,dy .
> $$
>
> **Trigonometric substitution** ([[§46 Trigonometric Substitution|§46]]). Let $y = \frac12 \tan\theta$, so $dy = \frac12 \sec^2\theta\,d\theta$ and $\sqrt{1 + 4y^2} = \sqrt{1 + \tan^2\theta} = \sec\theta$ (as $\sec\theta > 0$ for $0 \le \theta < \pi/2$). When $y = 0$, $\theta = 0$; when $y = 1$, $\tan\theta = 2$, so $\theta = \tan^{-1} 2 = \alpha$, say. With $\int \sec^3\theta\,d\theta = \frac12\big(\sec\theta\tan\theta + \ln|\sec\theta + \tan\theta|\big) + C$ (Stewart's Example 7.2.8, [[§45 Trigonometric Integrals#^ex-45-4|Example §45.4]]; or entry 21 of the Table of Integrals),
>
> $$
> \begin{aligned}
> L &= \int_0^\alpha \sec\theta \cdot \tfrac12 \sec^2\theta\,d\theta = \frac12 \int_0^\alpha \sec^3\theta\,d\theta = \frac12 \cdot \frac12 \Big[\sec\theta\tan\theta + \ln|\sec\theta + \tan\theta|\Big]_0^\alpha \\
> &= \frac14 \big(\sec\alpha\tan\alpha + \ln|\sec\alpha + \tan\alpha|\big) ,
> \end{aligned}
> $$
>
> since the bracket vanishes at $\theta = 0$ ($\sec 0 \tan 0 = 0$ and $\ln 1 = 0$). Now $\tan\alpha = 2$ gives $\sec^2\alpha = 1 + \tan^2\alpha = 5$, so $\sec\alpha = \sqrt5$ and
>
> $$
> L = \frac14\big(2\sqrt5 + \ln(\sqrt5 + 2)\big) = \frac{\sqrt5}{2} + \frac{\ln(\sqrt5 + 2)}{4} \approx 1.478943 .
> $$
>
> **Polygonal approximations.** Divide $[0, 1]$ on the $x$-axis into $n$ equal parts and join the points $(k/n, \sqrt{k/n})$ of the curve. For $n = 1$ the path is the diagonal of the unit square, $L_1 = \sqrt2$. The lengths $L_n$ increase toward $L$:
>
> | $n$ | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
> |---|---|---|---|---|---|---|---|
> | $L_n$ | 1.414 | 1.445 | 1.464 | 1.472 | 1.476 | 1.478 | 1.479 |
>
> *Stewart: Example 8.1.2*

^ex-52-2

> [!remark] Remark: Arc Length Integrals Are Often Not Elementary
> Because of the square root in Theorems §52.1 and §52.2, an arc length integral is often very hard or impossible to evaluate exactly, even for a curve as simple as the hyperbola $y = 1/x$ (Example §52.3 below). Then one settles for a numerical approximation, for instance by Simpson's Rule ([[§50 Approximate Integration#^def-50-5|Definition §50.5]]).

^rem-52-2

> [!example] Example §52.3: A Hyperbola, by Simpson's Rule
> (a) Set up an integral for the length of the arc of the hyperbola $xy = 1$ from $(1, 1)$ to $(2, \frac12)$. (b) Use Simpson's Rule with $n = 10$ to estimate the arc length.
>
> **(a)** $y = \dfrac1x$ and $\dfrac{dy}{dx} = -\dfrac{1}{x^2}$, so by Theorem §52.1
>
> $$
> L = \int_1^2 \sqrt{1 + \frac{1}{x^4}}\,dx .
> $$
>
> **(b)** Simpson's Rule with $a = 1$, $b = 2$, $n = 10$, $\Delta x = 0.1$ and $f(x) = \sqrt{1 + 1/x^4}$:
>
> $$
> L \approx \frac{\Delta x}{3}\big[f(1) + 4f(1.1) + 2f(1.2) + 4f(1.3) + \cdots + 2f(1.8) + 4f(1.9) + f(2)\big] .
> $$
>
> The values are
>
> | $x$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8 | 1.9 | 2.0 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $f(x)$ | 1.414214 | 1.297310 | 1.217478 | 1.161950 | 1.122634 | 1.094318 | 1.073586 | 1.058173 | 1.046547 | 1.037658 | 1.030776 |
> | weight | 1 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 2 | 4 | 1 |
>
> The endpoint terms add to $2.444990$, four times the odd-numbered values to $4 \times 5.649409 = 22.597636$ and twice the even-numbered interior values to $2 \times 4.460245 = 8.920490$. So
>
> $$
> L \approx \frac{0.1}{3}(33.963116) \approx 1.1321 .
> $$
>
> A computer gives $L \approx 1.1320904$, so Simpson's Rule is accurate to four decimal places.
>
> *Stewart: Example 8.1.3*

^ex-52-3

## The Arc Length Function

> [!definition] Definition §52.3: Arc Length Function
> Let $C$ be a smooth curve $y = f(x)$, $a \le x \le b$. The **arc length function** $s(x)$ is the distance along $C$ from the initial point $P_0(a, f(a))$ to the point $Q(x, f(x))$. By Theorem §52.1,
>
> $$
> s(x) = \int_a^x \sqrt{1 + [f'(t)]^2}\,dt .
> $$
>
> (The variable of integration is renamed $t$, so that $x$ does not have two meanings.)
>
> *Stewart: 8.1, Equation 5*

^def-52-3

> [!theorem] Theorem §52.3: Derivative of the Arc Length Function
> For the arc length function of a smooth curve $y = f(x)$,
>
> $$
> \frac{ds}{dx} = \sqrt{1 + [f'(x)]^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} .
> $$
>
> In particular $ds/dx \ge 1$ always, with $ds/dx = 1$ exactly where the slope $f'(x)$ of the curve is $0$.
>
> *Stewart: 8.1, Equation 6*

^thm-52-3

> [!proof]+ Proof
> The integrand $t \mapsto \sqrt{1 + [f'(t)]^2}$ of Definition §52.3 is continuous, because $f'$ is. By Part 1 of the Fundamental Theorem of Calculus, the function $x \mapsto \int_a^x \sqrt{1 + [f'(t)]^2}\,dt$ is differentiable with derivative $\sqrt{1 + [f'(x)]^2}$. Since $[f'(x)]^2 \ge 0$, this is at least $\sqrt1 = 1$, with equality exactly when $f'(x) = 0$.

^pf-52-3

*Uses:* [[§52 Arc Length#^def-52-3|Def. §52.3]], [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]] (FTC Part 1)

> [!remark]- Connections
> - Rigorous form of the step used: [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] ($x \mapsto \int_a^x f$ is differentiable wherever $f$ is continuous, with derivative $f(x)$).

> [!definition] Definition §52.4: Differential of Arc Length
> The **differential of arc length** is
>
> $$
> ds = \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx . \qquad (7)
> $$
>
> It is often written in the symmetric form
>
> $$
> (ds)^2 = (dx)^2 + (dy)^2 , \qquad (8)
> $$
>
> and solving (8) the other way gives
>
> $$
> ds = \sqrt{1 + \left(\frac{dx}{dy}\right)^2}\,dy . \qquad (9)
> $$
>
> *Stewart: 8.1, Equations 7–9*

^def-52-4

> [!remark] Remark: Reading the Formulas as L = ∫ ds
> Equation (8) is the Pythagorean theorem for the small right triangle with legs $dx$ and $dy$ whose hypotenuse $ds$ runs along the tangent line. For small $dx$ the tangent segment $ds$ is close to the true arc length $\Delta s$ over the same interval, just as the tangent-line increment $dy$ is close to $\Delta y$. Equation (8) is a mnemonic for both length formulas: write $L = \int ds$, then solve (8) as (7) to get Theorem §52.1, or as (9) to get Theorem §52.2. The same $ds$ appears in the surface area formulas of [[§53 Area of a Surface of Revolution#^thm-53-3|Theorem §53.3]], and for a parametric curve $x = x(t)$, $y = y(t)$, (8) gives $ds = \sqrt{(dx/dt)^2 + (dy/dt)^2}\,dt$ ([[§64 Calculus with Parametric Curves#^def-64-1|Definition §64.1]]).

^rem-52-3

> [!remark]- Connections
> - The scalar line integral $\int_\gamma f\,ds$ of [[§16 Line Integrals and Green's Theorem#^def-16-1|452 Def. §16.1]] is built on this $ds$, in the parametric form $ds = \sqrt{x'(t)^2 + y'(t)^2}\,dt$; with $f = 1$ it is the length of $\gamma$.

> [!example] Example §52.4: An Arc Length Function
> Find the arc length function for the curve $y = x^2 - \frac18 \ln x$, taking $P_0(1, 1)$ as the starting point.
>
> With $f(x) = x^2 - \frac18 \ln x$ (for $x > 0$),
>
> $$
> f'(x) = 2x - \frac{1}{8x}, \qquad
> 1 + [f'(x)]^2 = 1 + 4x^2 - \frac12 + \frac{1}{64x^2} = 4x^2 + \frac12 + \frac{1}{64x^2} = \left(2x + \frac{1}{8x}\right)^2 .
> $$
>
> (The middle term of the square is $2 \cdot 2x \cdot \frac{1}{8x} = \frac12$, which changes sign between $(2x - \frac{1}{8x})^2$ and $(2x + \frac{1}{8x})^2$.) Since $x > 0$, $\sqrt{1 + [f'(x)]^2} = 2x + \frac{1}{8x}$. So
>
> $$
> s(x) = \int_1^x \sqrt{1 + [f'(t)]^2}\,dt = \int_1^x \left(2t + \frac{1}{8t}\right) dt = t^2 + \frac18 \ln t \Big]_1^x = x^2 + \frac18 \ln x - 1 .
> $$
>
> For instance, the arc length along the curve from $(1, 1)$ to $(3, f(3))$ is
>
> $$
> s(3) = 3^2 + \frac18 \ln 3 - 1 = 8 + \frac{\ln 3}{8} \approx 8.1373 .
> $$
>
> For $x < 1$, $s(x)$ is negative: it is the length from $P_0$ back to $Q$ with a minus sign, since the integral runs from $1$ down to $x$.
>
> *Stewart: Example 8.1.4*

^ex-52-4

> [!remark] Remark: Method — Computing an Arc Length
> 1. **Choose the variable.** Write the curve as $y = f(x)$ or as $x = g(y)$ and use Theorem §52.1 or §52.2. Choose the form whose derivative is continuous on the whole closed interval: a vertical tangent at an endpoint makes $dy/dx$ unbounded there, while $dx/dy$ is fine ([[§52 Arc Length#^ex-52-2|Example §52.2]]).
> 2. **Simplify $1 + (\text{derivative})^2$.** Many textbook curves, such as $x^2 - \frac18 \ln x$, $\frac{x^3}{3} + \frac{1}{4x}$ or $a\cosh(x/a)$, are chosen so that $1 + [f'(x)]^2$ is a perfect square and the root disappears ([[§52 Arc Length#^ex-52-4|Example §52.4]]). Expand $[f'(x)]^2$ and look for $1 + (A - B)^2 = (A + B)^2$, which happens when $4AB = 1$.
> 3. **Integrate** with the substitution rule ([[§38 The Substitution Rule#^thm-38-3|Theorem §38.3]]), trigonometric substitution ([[§46 Trigonometric Substitution|§46]]) or a table ([[§49 Integration Using Tables and Technology|§49]]).
> 4. **If no antiderivative is available,** approximate the integral numerically, for example by Simpson's Rule ([[§52 Arc Length#^ex-52-3|Example §52.3]]).
> 5. **Check:** the arc length is at least the straight-line distance between the endpoints ([[§52 Arc Length#^ex-52-1|Example §52.1]]), since every inscribed polygon is at least as long as the chord.

^rem-52-4
