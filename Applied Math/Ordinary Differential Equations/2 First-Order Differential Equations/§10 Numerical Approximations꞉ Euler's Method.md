---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 10
bdp: "2.7"
aliases: ["BDP 2.7"]
tags: [ordinary-differential-equations, math331]
---
← [[§9 Exact Differential Equations and Integrating Factors]] · ↑ [[· 2 First-Order Differential Equations]] · [[§11 The Existence and Uniqueness Theorem]] →

*Boyce–DiPrima, Section 2.7.*

If $f$ and $\partial f/\partial y$ are continuous, the initial value problem $y' = f(t, y)$, $y(t_0) = y_0$ has a unique solution near $t_0$ ([[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]]), but for the vast majority of equations it cannot be found by symbolic manipulation: the linear, separable and exact equations of §4–§9 are the main exceptions. A direction field shows the solutions qualitatively but gives no numbers. Euler's tangent line method turns the direction field into numbers: follow the tangent line for a short step, recompute the slope, and repeat. This section develops the method, tests it on two problems with known solutions, and explains why it works well for one and badly for the other: Euler's method is always following a neighbouring solution, and what matters is whether neighbouring solutions converge or diverge.

## The Tangent Line Method

Consider the initial value problem

$$
\frac{dy}{dt} = f(t, y), \qquad y(t_0) = y_0 , \qquad (1)
$$

with solution $y = \phi(t)$. For instance, the direction field of

$$
\frac{dy}{dt} = 3 - 2t - 0.5y \qquad (2)
$$

shows that a solution starting on the $y$-axis first increases, reaches a maximum and then decreases. Many tangent segments at successive values of $t$ almost touch each other, which suggests linking tangent segments into a piecewise linear graph that approximates a solution. Three questions arise: can the linking be done systematically, does the result approximate an actual solution, and how large is the error? The first two are answered here; the third is the subject of BDP's Chapter 8.

The solution passes through $(t_0, y_0)$, and by the differential equation its slope there is $f(t_0, y_0)$. So the tangent line to the solution curve at $(t_0, y_0)$ is

$$
y = y_0 + f(t_0, y_0)(t - t_0) . \qquad (3)
$$

It is a good approximation on an interval short enough that the slope of the solution does not change appreciably from its initial value, so if $t_1$ is close to $t_0$, $\phi(t_1)$ is approximated by

$$
y_1 = y_0 + f(t_0, y_0)(t_1 - t_0) . \qquad (4)
$$

To continue, we do not know $\phi(t_1)$, so we use $y_1$ in its place and construct the line through $(t_1, y_1)$ with slope $f(t_1, y_1)$, $y = y_1 + f(t_1, y_1)(t - t_1)$ (5), which gives $y_2 = y_1 + f(t_1, y_1)(t_2 - t_1)$ (6) at a nearby point $t_2$. Continuing in this manner gives the method.

> [!definition] Definition §10.1: Euler's Method (Tangent Line Method)
> For the initial value problem (1) and points $t_0 < t_1 < t_2 < \cdots$, the **Euler method**, or **tangent line method**, computes approximations $y_n$ to $\phi(t_n)$ by
>
> $$
> y_{n+1} = y_n + f(t_n, y_n)(t_{n+1} - t_n), \qquad n = 0, 1, 2, \ldots . \qquad (8)
> $$
>
> With the notation $f_n = f(t_n, y_n)$ this reads $y_{n+1} = y_n + f_n \cdot (t_{n+1} - t_n)$ (9), and with a uniform **step size** $h$, $t_{n+1} = t_n + h$, it becomes **Euler's formula**
>
> $$
> y_{n+1} = y_n + f_n h, \qquad n = 0, 1, 2, \ldots . \qquad (10)
> $$
>
> The **tangent line** starting at $(t_n, y_n)$ is
>
> $$
> y = y_n + f(t_n, y_n)(t - t_n) ; \qquad (7)
> $$
>
> using (7) with $n = 0$ on $[t_0, t_1]$, with $n = 1$ on $[t_1, t_2]$, and so on, gives a piecewise linear function approximating $\phi(t)$. The method was originated by Euler about 1768.
>
> *BDP: 2.7, equations (7)–(10)*

^def-10-1

> [!remark]- Connections
> - See also: [[§58 Direction Fields and Euler's Method#^def-58-4|Calc Def. §58.4]] (Stewart's statement of the same formula) and [[§58 Direction Fields and Euler's Method#^rem-58-5|Calc Remark: How Accurate Is Euler's Method?]], where the error is observed to shrink in proportion to $h$; the Connections there explain this with Taylor's theorem, [[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]: one step errs by about $\frac12 h^2 \phi''$, and $1/h$ steps accumulate an error of order $h$.

> [!remark] Remark: Method — Euler's Method
> To approximate the solution of $y' = f(t, y)$, $y(t_0) = y_0$ on $[t_0, t_0 + Nh]$:
> 1. Choose the step size $h$, and set $t_n = t_0 + nh$.
> 2. For $n = 0, 1, \ldots, N - 1$: compute the slope $f_n = f(t_n, y_n)$, then $y_{n+1} = y_n + h f_n$.
> 3. Record the results in a table with columns $n$, $t_n$, $y_n$, $f_n$ (and, if wanted, the tangent line $y = y_n + f_n(t - t_n)$ used on $[t_n, t_{n+1}]$).
> 4. To judge the accuracy, repeat with smaller $h$ (halving $h$ roughly halves the error) and compare.
>
> In practice the loop is done by a computer program: evaluate (10) repeatedly, and output a table or a plot.

^rem-10-1

> [!example] Example §10.1: Euler's Method Step by Step
> Use Euler's method with step size $h = 0.2$ to approximate the solution of
>
> $$
> \frac{dy}{dt} = 3 - 2t - 0.5y, \qquad y(0) = 1 \qquad (11)
> $$
>
> at $t = 0.2, 0.4, 0.6, 0.8$ and $1$, and compare with the exact solution.
>
> **The exact solution.** The equation is linear, $y' + \frac12 y = 3 - 2t$, with integrating factor $e^{t/2}$: $(e^{t/2}y)' = (3 - 2t)e^{t/2}$. Integrating by parts, $\int (3 - 2t)e^{t/2}\,dt = 2(3 - 2t)e^{t/2} + \int 4e^{t/2}\,dt = (14 - 4t)e^{t/2} + c$, so $y = 14 - 4t + ce^{-t/2}$, and $y(0) = 1$ gives $c = -13$:
>
> $$
> y = \phi(t) = 14 - 4t - 13e^{-t/2} . \qquad (12)
> $$
>
> **Euler.** Here $f(t, y) = 3 - 2t - 0.5y$, $t_0 = 0$, $y_0 = 1$. Then $f_0 = f(0, 1) = 3 - 0 - 0.5 = 2.5$, the tangent line near $t = 0$ is $y = 1 + 2.5t$ (13), and
>
> $$
> y_1 = 1 + (2.5)(0.2) = 1.5 .
> $$
>
> Next, $f_1 = f(0.2, 1.5) = 3 - 0.4 - 0.75 = 1.85$, the tangent line near $t = 0.2$ is $y = 1.5 + 1.85(t - 0.2) = 1.13 + 1.85t$ (14), and $y_2 = 1.5 + (1.85)(0.2) = 1.87$. Three more steps give:
>
> | $n$ | $t_n$ | $y_n$ | $f_n = f(t_n, y_n)$ | tangent line | exact $\phi(t_n)$ |
> |---|---|---|---|---|---|
> | $0$ | $0.0$ | $1.00000$ | $2.5$ | $y = 1 + 2.5(t - 0)$ | $1.00000$ |
> | $1$ | $0.2$ | $1.50000$ | $1.85$ | $y = 1.5 + 1.85(t - 0.2)$ | $1.43711$ |
> | $2$ | $0.4$ | $1.87000$ | $1.265$ | $y = 1.87 + 1.265(t - 0.4)$ | $1.75650$ |
> | $3$ | $0.6$ | $2.12300$ | $0.7385$ | $y = 2.123 + 0.7385(t - 0.6)$ | $1.96936$ |
> | $4$ | $0.8$ | $2.27070$ | $0.26465$ | $y = 2.2707 + 0.26465(t - 0.8)$ | $2.08584$ |
> | $5$ | $1.0$ | $2.32363$ | | | $2.11510$ |
>
> **Comparison.** Every Euler value is larger than the exact one. This is because the solution is concave down ($\phi''(t) = -\frac{13}{4}e^{-t/2} < 0$), so its tangent lines lie above its graph. At $t = 1$ the error is $2.32363 - 2.11510 = 0.20853$, about $9.86\%$ of the exact value: not accurate enough for a typical scientific or engineering application. One remedy is a smaller step size, with correspondingly more steps.
>
> *BDP: Example 2.7.1*

^ex-10-1

![[m331-10-1.svg]]
*Example §10.1: the Euler polygon with $h = 0.2$ (red) and the exact solution $\phi(t) = 14 - 4t - 13e^{-t/2}$ (blue). The first step runs $h = 0.2$ along the tangent at $(0, 1)$ and rises $hf_0 = 0.5$. Because $\phi$ is concave down, each tangent segment overshoots, and the errors accumulate to $0.209$ at $t = 1$.*

> [!example] Example §10.2: Smaller Steps
> For the same problem (11), use Euler's method with step sizes $h = 0.1, 0.05, 0.025, 0.01$ (that is, $50, 100, 200, 500$ steps to go from $t = 0$ to $t = 5$), and compare with the exact solution (12) on $0 \le t \le 5$.
>
> | $t$ | $h = 0.1$ | $h = 0.05$ | $h = 0.025$ | $h = 0.01$ | exact |
> |---|---|---|---|---|---|
> | $0.0$ | $1.0000$ | $1.0000$ | $1.0000$ | $1.0000$ | $1.0000$ |
> | $1.0$ | $2.2164$ | $2.1651$ | $2.1399$ | $2.1250$ | $2.1151$ |
> | $2.0$ | $1.3397$ | $1.2780$ | $1.2476$ | $1.2295$ | $1.2176$ |
> | $3.0$ | $-0.7903$ | $-0.8459$ | $-0.8734$ | $-0.8898$ | $-0.9007$ |
> | $4.0$ | $-3.6707$ | $-3.7152$ | $-3.7373$ | $-3.7506$ | $-3.7594$ |
> | $5.0$ | $-7.0003$ | $-7.0337$ | $-7.0504$ | $-7.0604$ | $-7.0671$ |
>
> (Entries are rounded to four places; more digits were kept in the computation.)
>
> **Accuracy improves as $h$ decreases.** Along each row the values approach the exact one. At $t = 2$ the value with $h = 0.1$ is too large by $0.1221$ (about $10\%$), the value with $h = 0.01$ by only $0.0119$ (about $1\%$): reducing the step size by a factor of $10$, with $10$ times as many computations, reduces the error by a factor of about $10$. The other rows confirm that reducing $h$ by a given factor reduces the error by about the same factor, which suggests that the error of Euler's method is approximately proportional to $h$ (proved for one equation in Proposition §10.1).
>
> **Accuracy improves as $t$ increases, for fixed $h$** (at least for $t > 2$): with $h = 0.1$ the error at $t = 5$ is only $0.0668$, a little more than half the error at $t = 2$. The reason is explained below.
>
> *BDP: Example 2.7.2*

^ex-10-2

> [!example] Example §10.3: A Problem Where Euler's Method Does Badly
> Consider
>
> $$
> \frac{dy}{dt} = 4 - t + 2y, \qquad y(0) = 1 . \qquad (15)
> $$
>
> The equation is linear, $y' - 2y = 4 - t$; with the integrating factor $e^{-2t}$, $(e^{-2t}y)' = (4 - t)e^{-2t}$, and integrating by parts, $e^{-2t}y = -\frac12(4 - t)e^{-2t} + \frac14 e^{-2t} + c$, so $y = -\frac74 + \frac12 t + ce^{2t}$. The initial condition gives $c = \frac{11}{4}$:
>
> $$
> y = -\frac74 + \frac12 t + \frac{11}{4}e^{2t} . \qquad (16)
> $$
>
> With the same step sizes as in Example §10.2:
>
> | $t$ | $h = 0.1$ | $h = 0.05$ | $h = 0.025$ | $h = 0.01$ | exact |
> |---|---|---|---|---|---|
> | $0.0$ | $1.000000$ | $1.000000$ | $1.000000$ | $1.000000$ | $1.000000$ |
> | $1.0$ | $15.77728$ | $17.25062$ | $18.10997$ | $18.67278$ | $19.06990$ |
> | $2.0$ | $104.6784$ | $123.7130$ | $135.5440$ | $143.5835$ | $149.3949$ |
> | $3.0$ | $652.5349$ | $837.0745$ | $959.2580$ | $1045.395$ | $1109.179$ |
> | $4.0$ | $4042.122$ | $5633.351$ | $6755.175$ | $7575.577$ | $8197.884$ |
> | $5.0$ | $25026.95$ | $37897.43$ | $47555.35$ | $54881.32$ | $60573.53$ |
>
> Again accuracy improves as $h$ decreases: at $t = 1$ the percentage error drops from $17.3\%$ ($h = 0.1$) to $2.1\%$ ($h = 0.01$). But for fixed $h$ the error grows fairly rapidly with $t$: even with $h = 0.01$ the error at $t = 5$ is $9.4\%$, and it is much larger for larger step sizes. Such errors are too large for most applications; one would need still smaller steps, or to restrict the computation to a short interval near the initial point. Euler's method is much less effective here than in Example §10.2.
>
> *BDP: Example 2.7.3*

^ex-10-3

## Converging and Diverging Families

To understand the difference, look again at Euler's method for the general problem (1), whose exact solution is $\phi$. A first-order equation has an infinite family of solutions, indexed by an arbitrary constant, and the initial condition picks out $\phi$, the one with $\phi(t_0) = y_0$. The first step of Euler's method uses the tangent line to $\phi$ at $(t_0, y_0)$ and produces $y_1$, which usually differs from $\phi(t_1)$. So the second step uses the tangent line not to $\phi$ but to a nearby solution $\phi_1$, the one through $(t_1, y_1)$; and so on. Euler's method uses a succession of tangent line approximations to a sequence of *different* solutions $\phi, \phi_1, \phi_2, \ldots$, each step following the solution through the point produced by the previous step. The quality of the approximation after many steps depends on how the solutions through the points $(t_n, y_n)$ behave.

> [!definition] Definition §10.2: Converging and Diverging Families of Solutions
> A family of solutions of a first-order equation, indexed by an arbitrary constant $c$, is a **converging family** if any two of its members approach each other as $t \to \infty$, and a **diverging family** if solutions corresponding to two nearby values of $c$ become arbitrarily far apart as $t$ increases.
>
> In Example §10.2 the general solution
>
> $$
> y = 14 - 4t + ce^{-t/2} \qquad (17)
> $$
>
> is a converging family: the term with $c$ tends to zero. In Example §10.3 the general solution
>
> $$
> y = -\frac74 + \frac12 t + ce^{2t} \qquad (18)
> $$
>
> is a diverging family: the term with $c$ grows without bound.
>
> *BDP: 2.7 (text)*

^def-10-2

> [!remark] Remark: Why Euler's Errors Depend on the Family
> In Example §10.2 ($c = -13$) it hardly matters which nearby solution Euler's method is following at each step, since all solutions get closer and closer to each other as $t$ increases: errors made early are damped out. This is why the errors there decrease for $t > 2$. In Example §10.3 we want the solution with $c = \frac{11}{4}$, but at each step the method follows another solution, which separates from the desired one faster and faster as $t$ increases: errors made early are amplified by the factor $e^{2t}$. So a member of a diverging family will always be harder to approximate than a member of a converging family, and the best one can hope for from a numerical procedure is that it reflects the behaviour of the actual solution.
>
> In both examples the accuracy could be judged by comparison with the exact solution, but usually the exact solution is not available when a numerical method is used. What is needed are bounds, or at least estimates, of the error that do not require knowing the solution. These, and algorithms much more efficient than Euler's, are the subject of BDP's Chapter 8 (not part of this course).

^rem-10-2

![[m331-10-2.svg]]
*Euler's method follows a different solution at each step. (a) For $y' = 3 - 2t - 0.5y$ with $h = 0.5$, the solutions through the successive Euler points (grey) form a converging family, so they crowd together and the Euler points (red) stay near the true solution (blue). (b) For $y' = 4 - t + 2y$ with $h = 0.25$, the family diverges: each Euler point lies on a lower member of the family, and these members fall away from the true solution exponentially.*

## Convergence of Euler's Method

Under suitable conditions on $f$, the approximation generated by Euler's method converges to the exact solution as the step size decreases. BDP states this without proof (it is part of the error analysis of Chapter 8), and lets the reader verify it for one equation, where everything can be computed.

> [!theorem] Proposition §10.1: Euler's Method Converges for y′ = 1 − t + y
> Consider $y' = 1 - t + y$, $y(t_0) = y_0$.
> 1. The exact solution is $y = \phi(t) = (y_0 - t_0)e^{t - t_0} + t$.
> 2. Euler's formula with step size $h$ gives $y_k = (1 + h)y_{k-1} + h - ht_{k-1}$ for $k = 1, 2, \ldots$, and hence
>
> $$
> y_n = (1 + h)^n (y_0 - t_0) + t_n \qquad (19)
> $$
>
> for each positive integer $n$.
> 3. For a fixed $t > t_0$, let $h = (t - t_0)/n$, so that $t_n = t$ for every $n$. Then $y_n \to \phi(t)$ as $n \to \infty$, that is, as $h \to 0$. More precisely, with $a = t - t_0$,
>
> $$
> |\phi(t) - y_n| \le |y_0 - t_0|\,e^{a}\,\frac{a}{2}\,h ,
> $$
>
> so the error is at most proportional to $h$.
>
> *BDP: Problem 2.7.15 (parts 1–3); the error bound in 3 is added*

^prop-10-1

> [!proof]+ Proof
> **1.** $\phi(t_0) = y_0 - t_0 + t_0 = y_0$, and $\phi'(t) = (y_0 - t_0)e^{t - t_0} + 1 = 1 - t + \big((y_0 - t_0)e^{t - t_0} + t\big) = 1 - t + \phi(t)$.
>
> **2.** Euler's formula (10) with $f(t, y) = 1 - t + y$ is $y_k = y_{k-1} + h(1 - t_{k-1} + y_{k-1}) = (1 + h)y_{k-1} + h - ht_{k-1}$. Now (19) by induction on $n$. For $n = 1$: $y_1 = (1 + h)y_0 + h - ht_0 = (1 + h)(y_0 - t_0) + t_0 + h = (1 + h)(y_0 - t_0) + t_1$. If (19) holds for $n = k$, then
>
> $$
> y_{k+1} = (1 + h)\big[(1 + h)^k(y_0 - t_0) + t_k\big] + h - ht_k = (1 + h)^{k+1}(y_0 - t_0) + t_k + h = (1 + h)^{k+1}(y_0 - t_0) + t_{k+1} .
> $$
>
> **3.** With $h = a/n$, (19) reads $y_n = \big(1 + \frac an\big)^n (y_0 - t_0) + t$, so
>
> $$
> \phi(t) - y_n = (y_0 - t_0)\Big[e^{a} - \Big(1 + \frac an\Big)^n\Big] .
> $$
>
> Since $\big(1 + \frac an\big)^n \to e^a$ (BDP's hint; it is $\lim_{x \to 0}(1 + x)^{1/x} = e$ raised to the power $a$, with $x = a/n$), $y_n \to \phi(t)$. For the rate, use $x - \frac{x^2}{2} \le \ln(1 + x) \le x$ for $x \ge 0$ (both sides vanish at $x = 0$, and the derivatives compare as $1 - x \le \frac{1}{1 + x} \le 1$). With $x = a/n$, multiplied by $n$:
>
> $$
> a - \frac{a^2}{2n} \le n\ln\Big(1 + \frac an\Big) \le a, \qquad\text{so}\qquad e^{a}\Big(1 - \frac{a^2}{2n}\Big) \le e^{a - a^2/(2n)} \le \Big(1 + \frac an\Big)^n \le e^{a} ,
> $$
>
> using $e^{-u} \ge 1 - u$. Hence $0 \le e^a - (1 + a/n)^n \le e^a \dfrac{a^2}{2n} = e^a\dfrac{a}{2}h$, which gives the bound.

^pf-10-1

*Uses:* [[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|Def. §10.1]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Calc Thm. §19.7]] ($e$ as a limit), [[§29 The Mean Value Theorem#^cor-29-7|451 Cor. §29.7]] (monotonicity from the sign of the derivative)

> [!remark]- Connections
> - The simplest case $y' = y$, $y(0) = 1$ (BDP Problem 2.7.16) gives $y_n = (1 + h)^n = (1 + t/n)^n$, Euler's own approximation to $e^t$; Stewart's version of this limit is [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Calc Thm. §19.7]], and the analogous discrete compound-interest model is [[§12★ First-Order Difference Equations#^prop-12-1|Proposition §12.1]] with $\rho = 1 + h$.
