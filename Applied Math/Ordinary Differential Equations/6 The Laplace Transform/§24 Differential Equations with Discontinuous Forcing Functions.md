---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 6
section: 24
bdp: "6.4"
aliases: ["BDP 6.4"]
tags: [ordinary-differential-equations, math331]
---
← [[§23 Step Functions]] · ↑ [[· 6 The Laplace Transform]] · [[§25 Impulse Functions]] →

*Boyce–DiPrima, Section 6.4 · MATH 331 Written HW 5 (Problems 4, 8); Final (Fall 2022, alternate), Q3.*

This section puts the step functions of [[§23 Step Functions|§23]] to work: linear equations with constant coefficients whose forcing term switches on and off, such as a voltage pulse in a circuit or a load applied to a spring for a while. Solving such a problem by hand means solving a separate initial value problem on each interval and matching values at the break points. The Laplace transform does all the intervals at once, because a delayed forcing term only contributes a factor $e^{-cs}$. The answer also shows how smooth the solution is: $y$ and $y'$ are continuous across a jump of the forcing term, and the jump appears in $y''$.

## Solving with the Laplace Transform

> [!definition] Definition §24.1: Forcing Function
> In a nonhomogeneous linear equation $ay'' + by' + cy = g(t)$, the nonhomogeneous term $g(t)$ is called the **forcing function**. In a mechanical system it is the applied force, in a circuit the applied voltage (or its derivative). In this section $g$ is piecewise continuous and may be discontinuous.
>
> *BDP: 6.4 (text)*

^def-24-1

> [!remark] Remark: Method — Initial Value Problems with Discontinuous Forcing
> 1. Write $g(t)$ with step functions, every term in the form $u_c(t)\,k(t - c)$ ([[§23 Step Functions#^rem-23-1|Method of §23]]).
> 2. Transform the equation, using $\mathcal{L}\{y'\} = sY - y(0)$ and $\mathcal{L}\{y''\} = s^2Y - sy(0) - y'(0)$ ([[§22 Solution of Initial Value Problems#^thm-22-1|Theorem §22.1]], [[§22 Solution of Initial Value Problems#^cor-22-2|Corollary §22.2]]) and $\mathcal{L}\{u_c(t)k(t - c)\} = e^{-cs}K(s)$ ([[§23 Step Functions#^thm-23-2|Theorem §23.2]]). Solve for $Y(s)$.
> 3. Collect the terms of $Y(s)$ by exponential factor. Typically $Y(s) = \Phi(s) + \sum_c e^{-cs}H_c(s)$, where $\Phi$ comes from the initial conditions.
> 4. Invert: find $h_c(t) = \mathcal{L}^{-1}\{H_c(s)\}$ by partial fractions or completing the square, then delay it, $u_c(t)\,h_c(t - c)$ ([[§23 Step Functions#^rem-23-2|Method of §23]]).
> 5. Write $y$ piecewise on the intervals between break points, and read off the behavior on each: rest, response to the switched-on force, free motion after it is removed. Check that $y$ and $y'$ are continuous at the break points (Proposition §24.1).

^rem-24-1

> [!example] Example §24.1: A Rectangular Pulse
> Solve
>
> $$
> 2y'' + y' + 2y = g(t), \qquad g(t) = u_5(t) - u_{20}(t) = \begin{cases} 1, & 5 \le t < 20, \\ 0, & 0 \le t < 5 \text{ or } t \ge 20, \end{cases} \qquad y(0) = 0,\ y'(0) = 0 .
> $$
>
> This governs the charge on the capacitor of a circuit that receives a unit voltage pulse for $5 \le t < 20$, or a damped oscillator under a constant force switched on at $t = 5$ and off at $t = 20$.
>
> **Transform.** With zero initial values,
>
> $$
> 2s^2Y(s) + sY(s) + 2Y(s) = \mathcal{L}\{u_5(t)\} - \mathcal{L}\{u_{20}(t)\} = \frac{e^{-5s} - e^{-20s}}{s},
> \qquad
> Y(s) = \big(e^{-5s} - e^{-20s}\big)H(s), \quad H(s) = \frac{1}{s(2s^2 + s + 2)} .
> $$
>
> **Invert $H$.** Write $H(s) = \dfrac{a}{s} + \dfrac{bs + c}{2s^2 + s + 2}$, so $1 = a(2s^2 + s + 2) + (bs + c)s$. At $s = 0$: $a = \frac12$. Coefficient of $s^2$: $2a + b = 0$, $b = -1$. Coefficient of $s$: $a + c = 0$, $c = -\frac12$. Completing the square, $2s^2 + s + 2 = 2\big[(s + \frac14)^2 + \frac{15}{16}\big]$ and $s + \frac12 = (s + \frac14) + \frac14$, so
>
> $$
> H(s) = \frac{1/2}{s} - \frac12\left[\frac{s + \frac14}{(s + \frac14)^2 + \big(\frac{\sqrt{15}}{4}\big)^2} + \frac{1}{\sqrt{15}}\,\frac{\frac{\sqrt{15}}{4}}{(s + \frac14)^2 + \big(\frac{\sqrt{15}}{4}\big)^2}\right],
> $$
>
> $$
> h(t) = \mathcal{L}^{-1}\{H(s)\} = \frac12 - \frac12\Big(e^{-t/4}\cos\frac{\sqrt{15}\,t}{4} + \frac{1}{\sqrt{15}}\,e^{-t/4}\sin\frac{\sqrt{15}\,t}{4}\Big) .
> $$
>
> **The solution.** By [[§23 Step Functions#^thm-23-2|Theorem §23.2]],
>
> $$
> y(t) = u_5(t)\,h(t - 5) - u_{20}(t)\,h(t - 20) .
> $$
>
> **Three phases.**
> - $0 \le t < 5$: $y = 0$. The equation is $2y'' + y' + 2y = 0$ with zero initial values, so the system stays at rest; in particular $y(5) = y'(5) = 0$.
> - $5 \le t < 20$: $y = h(t - 5)$, the solution of $2y'' + y' + 2y = 1$ with zero data at $t = 5$. It is the constant $\frac12$ (the response to the constant force) plus a damped oscillation; it overshoots to a maximum $y \approx 0.722$ at $t \approx 8.24$ and settles toward $\frac12$. At $t = 20$, $y(20) \approx 0.50162$ and $y'(20) \approx 0.01125$.
> - $t \ge 20$: the forcing is off again, and $y$ is a damped oscillation about $y = 0$ starting from those values (minimum $\approx -0.223$ at $t \approx 23.27$).
>
> Solving the three problems separately and matching $y$ and $y'$ at $t = 5$ and $t = 20$ gives the same function, with much more work.
>
> *BDP: Example 6.4.1*

^ex-24-1

![[m331-24-1.svg]]
*The response of $2y'' + y' + 2y = u_5(t) - u_{20}(t)$, $y(0) = y'(0) = 0$ (blue) to the unit pulse (orange). Nothing happens before $t = 5$; while the pulse is on, $y$ overshoots and settles toward $\frac12$, the equilibrium of $2y = 1$; after $t = 20$ it oscillates back down to $0$. The curve has no corners: $y$ and $y'$ are continuous at $t = 5$ and $t = 20$, and only the curvature $y''$ jumps there.*

## Smoothness of the Solution at a Jump

In Example §24.1 one can compute directly from $h$ that $y$ and $y'$ are continuous at $t = 5$ and $t = 20$, while

$$
\lim_{t \to 5^-} y''(t) = 0, \qquad \lim_{t \to 5^+} y''(t) = h''(0) = \frac12 .
$$

So $y''$ jumps by $\frac12$ at $t = 5$, and in the same way by $-\frac12$ at $t = 20$. The jump of size $1$ in the forcing is balanced by a jump in the highest-order term $2y''$. This is general.

> [!theorem] Proposition §24.1: Continuity of y and y′ Across a Jump in g
> Let $p$ and $q$ be continuous on $\alpha < t < \beta$, let $g$ be piecewise continuous there, and let $y$ be the solution of
>
> $$
> y'' + p(t)y' + q(t)y = g(t), \qquad y(t_0) = y_0,\ y'(t_0) = y_0' . \qquad (16)
> $$
>
> Then $y$ and $y'$ are continuous on $\alpha < t < \beta$, and $y''$ has jump discontinuities at exactly the points where $g$ does, with the same jumps:
>
> $$
> y''(t_1^+) - y''(t_1^-) = g(t_1^+) - g(t_1^-) .
> $$
>
> Similarly, for an equation of order $n$ the solution and its first $n - 1$ derivatives are continuous, and the $n$th derivative jumps where $g$ does.
>
> *BDP: 6.4 (text)*

^prop-24-1

> [!proof]+ Proof
> BDP argues from the existence and uniqueness theorem; here is the argument written out. Let $t_1 < t_2 < \cdots$ be the jumps of $g$. On each closed interval $[t_k, t_{k+1}]$, let $g_k$ be $g$ with its one-sided limits as endpoint values; $g_k$ is continuous there (extend it continuously a little beyond the endpoints, so that the existence and uniqueness theorem, stated for open intervals, applies). "The solution" of (16) is built interval by interval: on the interval containing $t_0$, it is the solution given by [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]] (BDP Theorem 3.2.1); at each $t_k$, the values $y(t_k)$ and $y'(t_k)$ reached from the left are taken as initial values for the problem with forcing $g_k$ on the next interval, which again has a unique solution by Theorem 3.2.1. (This is also the function that the Laplace transform produces.)
>
> By construction $y$ and $y'$ have the same value from both sides at each $t_k$, so they are continuous. On each side of $t_k$ the equation holds up to the endpoint:
>
> $$
> y''(t_k^\pm) = g(t_k^\pm) - p(t_k)\,y'(t_k) - q(t_k)\,y(t_k) .
> $$
>
> The last two terms are the same on both sides, since $p, q, y, y'$ are continuous. Subtracting gives $y''(t_k^+) - y''(t_k^-) = g(t_k^+) - g(t_k^-)$. So $y''$ jumps exactly where $g$ does. For order $n$, the same construction makes $y, \ldots, y^{(n-1)}$ continuous, and the equation solved for $y^{(n)}$ transfers the jump of $g$ to $y^{(n)}$.

^pf-24-1

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|§14.1]] (existence and uniqueness, Theorem 3.2.1)

For $ay'' + by' + cy = g$, divide by $a$ first: the jump in $y''$ is the jump in $g$ divided by $a$. In Example §24.1 ($a = 2$) this is $\frac12$ at $t = 5$ and $-\frac12$ at $t = 20$. The more regular $g$ is, the more regular $y$ is: if $g$ is continuous but $g'$ jumps, then $y''$ is continuous and $y'''$ jumps (Example §24.2).

## More Examples

> [!example] Example §24.2: Ramp Loading
> Describe and find the solution of
>
> $$
> y'' + 4y = g(t), \qquad y(0) = 0,\ y'(0) = 0, \qquad g(t) = \begin{cases} 0, & 0 \le t < 5, \\ \frac15(t - 5), & 5 \le t < 10, \\ 1, & t \ge 10. \end{cases}
> $$
>
> The forcing **ramps** up from $0$ to $1$ over $5 \le t \le 10$ and then stays at $1$ (**ramp loading**).
>
> **Qualitatively.** For $t < 5$, $y = 0$. For $t > 10$ the equation is $y'' + 4y = 1$, whose solutions are $y = c_1\cos 2t + c_2\sin 2t + \frac14$: a simple harmonic oscillation about $y = \frac14$. In between, the solution oscillates about a linear function.
>
> **Steps.** By the method of [[§23 Step Functions#^rem-23-1|§23]], $g(t) = \frac15\big(u_5(t)(t - 5) - u_{10}(t)(t - 10)\big)$: the slope $\frac15$ is switched on at $t = 5$ and off at $t = 10$. Transforming, with $\mathcal{L}\{t\} = 1/s^2$,
>
> $$
> (s^2 + 4)Y(s) = \frac{e^{-5s} - e^{-10s}}{5s^2}, \qquad Y(s) = \frac15\big(e^{-5s} - e^{-10s}\big)H(s), \qquad H(s) = \frac{1}{s^2(s^2 + 4)} .
> $$
>
> Partial fractions give $H(s) = \dfrac{1/4}{s^2} - \dfrac{1/4}{s^2 + 4}$, so $h(t) = \frac14 t - \frac18\sin 2t$ and
>
> $$
> y(t) = \frac15\Big(u_5(t)\,h(t - 5) - u_{10}(t)\,h(t - 10)\Big) .
> $$
>
> **On each interval.** For $5 \le t < 10$: $y = \dfrac{t - 5}{20} - \dfrac{\sin 2(t - 5)}{40} = \dfrac{g(t)}{4} - \dfrac{\sin 2(t - 5)}{40}$, an oscillation about the line $g(t)/4$. For $t \ge 10$, using $\sin A - \sin B = 2\cos\frac{A + B}{2}\sin\frac{A - B}{2}$,
>
> $$
> y = \frac14 - \frac{\sin 2(t - 5) - \sin 2(t - 10)}{40} = \frac14 - \frac{\sin 5}{20}\cos(2t - 15) .
> $$
>
> So the eventual steady oscillation has amplitude $A = \dfrac{|\sin 5|}{20} \approx 0.0479$. (BDP finds this numerically: the first maximum after $t = 10$ is at $(10.642,\ 0.2979)$, and $0.2979 - 0.25 = 0.0479$. The closed form puts the maxima at $2t - 15 = 2k\pi$, since $\sin 5 < 0$; $k = 1$ gives $t = 7.5 + \pi \approx 10.642$.)
>
> **Smoothness.** Here $g$ is continuous but $g'$ jumps at $t = 5$ and $t = 10$. So $y$, $y'$ and $y''$ are continuous everywhere, and $y'''$ has jumps at $t = 5$ and $t = 10$ matching those of $g'$.
>
> *BDP: Example 6.4.2*

^ex-24-2

![[m331-24-2.svg]]
*Ramp loading of $y'' + 4y = g(t)$. While the load ramps up ($5 < t < 10$) the solution (blue) oscillates about the line $g(t)/4$ (orange, dashed), the quasi-static response; once the load is constant it oscillates about $\frac14$ with the constant amplitude $A = |\sin 5|/20 \approx 0.048$ (dotted band). The amplitude depends on how fast the load was applied.*

> [!example] Example §24.3: A Force Removed at t = 6
> Solve $y'' + y = g(t)$, $y(0) = 0$, $y'(0) = 0$, where $g(t) = t$ for $0 \le t < 6$ and $g(t) = 0$ for $t \ge 6$.
>
> **Steps.** $g(t) = t - u_6(t)\,t = t - u_6(t)\big[(t - 6) + 6\big]$, so $\mathcal{L}\{g\} = \dfrac{1}{s^2} - e^{-6s}\Big(\dfrac{1}{s^2} + \dfrac{6}{s}\Big)$.
>
> **Transform.** $(s^2 + 1)Y(s) = \mathcal{L}\{g\}$, so
>
> $$
> Y(s) = \big(1 - e^{-6s}\big)\frac{1}{s^2(s^2 + 1)} - 6e^{-6s}\frac{1}{s(s^2 + 1)} .
> $$
>
> **Invert.** $\dfrac{1}{s^2(s^2 + 1)} = \dfrac{1}{s^2} - \dfrac{1}{s^2 + 1}$ has inverse $t - \sin t$, and $\dfrac{1}{s(s^2 + 1)} = \dfrac1s - \dfrac{s}{s^2 + 1}$ has inverse $1 - \cos t$. By [[§23 Step Functions#^thm-23-2|Theorem §23.2]],
>
> $$
> y(t) = t - \sin t - u_6(t)\big[(t - 6) - \sin(t - 6)\big] - 6u_6(t)\big[1 - \cos(t - 6)\big] .
> $$
>
> **Piecewise.**
>
> $$
> y(t) = \begin{cases} t - \sin t, & 0 \le t < 6, \\ -\sin t + \sin(t - 6) + 6\cos(t - 6), & t \ge 6. \end{cases}
> $$
>
> After $t = 6$ the motion is a free oscillation $y'' + y = 0$. Check at $t = 6$: both formulas give $y(6) = 6 - \sin 6$ and $y'(6) = 1 - \cos 6$, as Proposition §24.1 requires.
>
> *Source: 331 Written HW 5, Problem 4*

^ex-24-3

> [!example] Example §24.4: A Step Switched On at t = 6
> Use Laplace transforms to solve $y'' + 4y' + 13y = u_6(t)$, $y(0) = 0$, $y'(0) = 1$, and find $\lim_{t \to \infty} y(t)$.
>
> **Transform.** $s^2Y - 1 + 4sY + 13Y = \dfrac{e^{-6s}}{s}$, so
>
> $$
> Y(s) = \frac{1}{s^2 + 4s + 13} + e^{-6s}\,\frac{1}{s(s^2 + 4s + 13)}, \qquad s^2 + 4s + 13 = (s + 2)^2 + 3^2 .
> $$
>
> **First term.** $\mathcal{L}^{-1}\Big\{\dfrac{1}{(s + 2)^2 + 3^2}\Big\} = \dfrac13 e^{-2t}\sin 3t$ ([[§23 Step Functions#^thm-23-3|Theorem §23.3]]).
>
> **Second term.** $\dfrac{1}{s(s^2 + 4s + 13)} = \dfrac{A}{s} + \dfrac{Bs + C}{s^2 + 4s + 13}$ with $1 = A(s^2 + 4s + 13) + (Bs + C)s$: $A = \frac{1}{13}$, $B = -A = -\frac{1}{13}$, $C = -4A = -\frac{4}{13}$. With $s + 4 = (s + 2) + 2$,
>
> $$
> \frac{1}{s(s^2 + 4s + 13)} = \frac{1}{13}\left[\frac1s - \frac{s + 2}{(s + 2)^2 + 9} - \frac23\cdot\frac{3}{(s + 2)^2 + 9}\right],
> \qquad
> g(t) = \frac{1}{13}\Big[1 - e^{-2t}\Big(\cos 3t + \frac23\sin 3t\Big)\Big] .
> $$
>
> **Solution.**
>
> $$
> y(t) = \frac13 e^{-2t}\sin 3t + \frac{u_6(t)}{13}\Big[1 - e^{-2(t - 6)}\Big(\cos 3(t - 6) + \frac23\sin 3(t - 6)\Big)\Big] .
> $$
>
> **Limit.** Every term except $\frac{1}{13}$ carries a factor $e^{-2t}$ or $e^{-2(t - 6)}$, so $\lim_{t \to \infty} y(t) = \dfrac{1}{13}$: the equilibrium of $13y = 1$, the constant force divided by the spring constant.
>
> *Source: 331 Written HW 5, Problem 8*

^ex-24-4

> [!example] Example §24.5: A First-Order Equation
> Solve $y' + 2y = u_5(t)\,e^{t - 5}$, $y(0) = 3$.
>
> **Transform.** The forcing is the translation of $e^t$ by $5$, so its transform is $e^{-5s}/(s - 1)$ ([[§23 Step Functions#^thm-23-2|Theorem §23.2]]):
>
> $$
> sY - 3 + 2Y = \frac{e^{-5s}}{s - 1}, \qquad Y(s) = \frac{3}{s + 2} + e^{-5s}\frac{1}{(s - 1)(s + 2)} .
> $$
>
> **Invert.** $\dfrac{1}{(s - 1)(s + 2)} = \dfrac13\Big(\dfrac{1}{s - 1} - \dfrac{1}{s + 2}\Big)$ has inverse $\frac13\big(e^t - e^{-2t}\big)$. So
>
> $$
> y(t) = 3e^{-2t} + \frac13\,u_5(t)\Big(e^{t - 5} - e^{-2(t - 5)}\Big)
> = \begin{cases} 3e^{-2t}, & 0 \le t < 5, \\ 3e^{-2t} + \frac13\big(e^{t - 5} - e^{-2(t - 5)}\big), & t \ge 5. \end{cases}
> $$
>
> For a first-order equation the highest derivative is $y'$: $y$ is continuous at $t = 5$, and $y'$ jumps by $1$, the size of the jump of the forcing term (from $0$ to $e^0 = 1$).
>
> *Source: 331 Final (Fall 2022, alternate), Q3*

^ex-24-5
