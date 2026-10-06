---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 9
bdp: "2.5"
aliases: ["BDP 2.5"]
tags: [ordinary-differential-equations, math331]
---
← [[§8 Differences Between Linear and Nonlinear Differential Equations]] · ↑ [[· 2 First-Order Differential Equations]] · [[§10 Critical Thresholds and Bifurcations]] →

*Boyce–DiPrima, Section 2.5 · MATH 331 Written HW 2 (Problem 2), Midterm (Fall 2021) Q5, Midterm (Spring 2020) Q6.*

An autonomous equation $dy/dt = f(y)$ is one whose right side does not depend on $t$. It is separable, but the point of this section is that the graph of $f$ alone, without solving anything, shows how every solution behaves: where the equilibrium solutions are, which of them attract nearby solutions and which repel them, where solution curves bend, and what happens as $t \to \infty$. This qualitative picture is developed on models of population growth: exponential growth, the logistic equation with its carrying capacity, growth with a critical threshold, and a combination of the two. It is the one-dimensional case of the stability theory of Chapter 9 of BDP.

> [!definition] Definition §9.1: Autonomous Equation
> A first-order differential equation in which the independent variable does not appear explicitly,
>
> $$
> \frac{dy}{dt} = f(y) , \qquad (1)
> $$
>
> is called **autonomous**. The special case $f(y) = ay - b$ was solved in [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]].
>
> *BDP: 2.5, equation (1)*

^def-9-1

> [!remark]- Connections
> - See also: [[§67 Direction Fields and Euler's Method#^def-67-3|Calc Def. §67.3]] (Stewart's autonomous equations), with the observation that a time-shift of a solution is again a solution, [[§67 Direction Fields and Euler's Method#^prop-67-1|Calc Prop. §67.1]]; and Stewart's logistic model, [[§69 Models for Population Growth#^def-69-2|Calc Def. §69.2]], [[§66 Modeling with Differential Equations#^prop-66-2|Calc Prop. §66.2]] (its qualitative behaviour) and [[§69 Models for Population Growth#^thm-69-2|Calc Thm. §69.2]] (its solution). The treatment here is fuller: phase lines, stability, thresholds and bifurcations.

## Exponential Growth

> [!definition] Definition §9.2: Exponential Growth; Rate of Growth or Decline
> Let $y = \phi(t)$ be the population of a species at time $t$. The simplest hypothesis is that the rate of change of $y$ is proportional to the current value of $y$:
>
> $$
> \frac{dy}{dt} = ry . \qquad (2)
> $$
>
> The constant $r$ is the **rate of growth** if $r > 0$ and the **rate of decline** if $r < 0$ (the rate constant of [[§1 Some Basic Mathematical Models; Direction Fields#^def-1-5|Definition §1.5]]). (In this section $y$ is a population, so the initial value $y(0) = y_0$ is taken positive.)
>
> *BDP: 2.5, equation (2)*

^def-9-2

> [!theorem] Proposition §9.1: Solution of the Exponential Growth Model
> The solution of (2) with the initial condition
>
> $$
> y(0) = y_0 \qquad (3)
> $$
>
> is
>
> $$
> y = y_0 e^{rt} . \qquad (4)
> $$
>
> *BDP: 2.5, equation (4)*

^prop-9-1

> [!proof]+ Proof
> Equation (2) is linear, $y' - ry = 0$, with integrating factor $e^{-rt}$: $(e^{-rt}y)' = 0$, so $e^{-rt}y = c$ and $y = ce^{rt}$. The initial condition gives $c = y_0$. By [[§8 Differences Between Linear and Nonlinear Differential Equations#^thm-8-1|Theorem §8.1]] this is the only solution, on all of $-\infty < t < \infty$.

^pf-9-1

*Uses:* [[§8 Differences Between Linear and Nonlinear Differential Equations#^thm-8-1|§8.1]], [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-2|§5.2]] (integrating factors)

With $r > 0$ the model predicts that the population grows exponentially for all time. Under ideal conditions (4) is reasonably accurate for many populations, at least for limited periods of time, but eventually limitations on space, food supply or other resources reduce the growth rate. (The observation goes back to Thomas Malthus, 1798; see also [[§24 Exponential Growth and Decay#^thm-24-1|Calc Thm. §24.1]].)

## Logistic Growth

To account for the dependence of the growth rate on the population, replace the constant $r$ in (2) by a function $h(y)$: $dy/dt = h(y)\,y$ (5). Choose $h$ so that $h(y) \cong r > 0$ when $y$ is small, $h(y)$ decreases as $y$ grows, and $h(y) < 0$ when $y$ is large enough. The simplest such function is $h(y) = r - ay$ with $a > 0$.

> [!definition] Definition §9.3: Logistic Equation; Intrinsic Growth Rate
> The equation
>
> $$
> \frac{dy}{dt} = (r - ay)\,y , \qquad (6)
> $$
>
> with positive constants $r$ and $a$, is the **Verhulst equation** or **logistic equation**. With $K = r/a$ it takes the equivalent form
>
> $$
> \frac{dy}{dt} = r\Big(1 - \frac{y}{K}\Big)\,y . \qquad (7)
> $$
>
> In this form $r$ is the **intrinsic growth rate**: the growth rate in the absence of any limiting factors. The constant $K$ is the **saturation level**, or **environmental carrying capacity**, of the species; the name is justified below (it is the level that growing populations approach but do not exceed).
>
> *BDP: 2.5, equations (6) and (7)*

^def-9-3

The rest of this section shows how to sketch qualitatively correct solutions of (7), and of the general autonomous equation (1), without solving.

> [!definition] Definition §9.4: Equilibrium Solutions; Critical Points
> A constant solution $y = \phi(t) = y_1$ of the autonomous equation (1) is called an **equilibrium solution** (as in [[§1 Some Basic Mathematical Models; Direction Fields#^def-1-4|Definition §1.4]]), because it corresponds to no change in $y$ as $t$ increases. Since $dy/dt = 0$ for a constant function, the equilibrium solutions are found by locating the roots of
>
> $$
> f(y) = 0 .
> $$
>
> These roots are also called **critical points** of (1).
>
> For the logistic equation (7), $r(1 - y/K)\,y = 0$ gives the equilibrium solutions $y = \phi_1(t) = 0$ and $y = \phi_2(t) = K$.
>
> *BDP: 2.5 (text)*

^def-9-4

To see the other solutions, graph $f(y)$ against $y$. For (7) the graph of $f(y) = r(1 - y/K)y$ is a parabola with intercepts $(0, 0)$ and $(K, 0)$, the critical points, and vertex $(K/2, rK/4)$. So $dy/dt > 0$ for $0 < y < K$, and $y$ is an increasing function of $t$ when $y$ is in this interval; and $dy/dt < 0$ for $y > K$, so there $y$ is decreasing.

> [!definition] Definition §9.5: Phase Line
> The $y$-axis, marked with the critical points and with arrows showing where $y$ increases ($f(y) > 0$) and where it decreases ($f(y) < 0$), is called the **phase line** of the autonomous equation (1). It is usually drawn vertically.
>
> For the logistic equation the phase line has dots at $y = 0$ and $y = K$, an upward arrow on $0 < y < K$ and a downward arrow on $y > K$.
>
> *BDP: 2.5 (text), Figure 2.5.3(a)*

^def-9-5

Near $y = 0$ and $y = K$ the slope $f(y)$ is near zero, so solution curves are flat there, and they steepen as $y$ moves away. Sketching in the $ty$-plane: draw the equilibrium solutions $y = 0$ and $y = K$; then curves that increase when $0 < y < K$, decrease when $y > K$, and flatten as $y$ approaches $0$ or $K$.

The sketch may seem to show other solutions running into $y = K$, but they cannot: by the uniqueness part of Theorem 2.4.2 only one solution passes through a given point of the $ty$-plane ([[§8 Differences Between Linear and Nonlinear Differential Equations#^cor-8-3|Corollary §8.3]]). So, although other solutions may be asymptotic to the equilibrium solution as $t \to \infty$, they never meet it at a finite time. A solution that starts in $0 < y < K$ stays there for all time, and one that starts in $K < y < \infty$ stays there.

Concavity and inflection points come from the second derivative.

> [!theorem] Proposition §9.2: Concavity of Solutions of an Autonomous Equation
> If $f$ is differentiable and $y = \phi(t)$ solves (1), then
>
> $$
> \frac{d^2y}{dt^2} = f'(y)\,f(y) . \qquad (8)
> $$
>
> So the graph of $y$ against $t$ is concave up where $f$ and $f'$ have the same sign, concave down where they have opposite signs, and inflection points may occur where $f'(y) = 0$.
>
> *BDP: 2.5, equation (8)*

^prop-9-2

> [!proof]+ Proof
> By (1) and the chain rule,
>
> $$
> \frac{d^2y}{dt^2} = \frac{d}{dt}\frac{dy}{dt} = \frac{d}{dt} f(y) = f'(y)\frac{dy}{dt} = f'(y)\,f(y) .
> $$
>
> The concavity statements are the sign of $y''$. (Away from the critical points $f(y) \ne 0$, so $y''$ can change sign only where $f'(y)$ does.)

^pf-9-2

*Uses:* [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-1|Def. §9.1]]

For the logistic equation (7): on $0 < y < K/2$, $f$ is positive and increasing, so $f, f' > 0$ and solutions are concave up; on $K/2 < y < K$, $f > 0 > f'$, concave down; on $y > K$, $f$ is negative and decreasing, $f, f' < 0$, concave up. Every solution curve that crosses the line $y = K/2$ has an inflection point there. Finally, $K$ is the upper bound that is approached, but not exceeded, by growing populations starting below it, which justifies the names *saturation level* and *carrying capacity*. Comparing with (4): however small the nonlinear term in (7) (that is, however large $K$), solutions of (7) approach a finite value as $t \to \infty$, whereas solutions of (2) grow without bound. A tiny nonlinear term has a decisive effect for large $t$.

For quantitative information, solve (7).

> [!theorem] Proposition §9.3: Solution of the Logistic Equation
> The solution of the logistic equation (7) with $y(0) = y_0 \ge 0$ is
>
> $$
> y = \frac{y_0 K}{y_0 + (K - y_0)e^{-rt}} , \qquad (11)
> $$
>
> defined for all $t \ge 0$. It includes the equilibrium solutions $y = 0$ ($y_0 = 0$) and $y = K$ ($y_0 = K$). If $y_0 > 0$, then $\lim_{t \to \infty} y(t) = K$.
>
> *BDP: 2.5, equation (11)*

^prop-9-3

> [!proof]+ Proof
> **Case $0 < y_0 < K$.** As noted above, the solution stays in $0 < y < K$, so $y \ne 0$ and $y \ne K$ and (7) can be written $\dfrac{dy}{(1 - y/K)\,y} = r\,dt$. The partial fraction expansion $\dfrac{1}{(1 - y/K)y} = \dfrac1y + \dfrac{1/K}{1 - y/K}$ gives
>
> $$
> \Big( \frac1y + \frac{1/K}{1 - y/K} \Big)\,dy = r\,dt , \qquad \ln|y| - \ln\Big|1 - \frac yK\Big| = rt + c . \qquad (9)
> $$
>
> Since $0 < y < K$, the absolute value bars can be dropped, and exponentiating,
>
> $$
> \frac{y}{1 - y/K} = Ce^{rt}, \qquad C = e^c . \qquad (10)
> $$
>
> At $t = 0$: $C = y_0/(1 - y_0/K) = y_0K/(K - y_0)$. Solving (10) for $y$: $y = (1 - y/K)Ce^{rt}$, so $y\,(1 + Ce^{rt}/K) = Ce^{rt}$ and
>
> $$
> y = \frac{Ce^{rt}}{1 + Ce^{rt}/K} = \frac{CK}{Ke^{-rt} + C} = \frac{y_0K^2/(K - y_0)}{Ke^{-rt} + y_0K/(K - y_0)} = \frac{y_0K}{(K - y_0)e^{-rt} + y_0} ,
> $$
>
> which is (11). (BDP leaves this algebra as Problem 10.)
>
> **Case $y_0 > K$.** (BDP leaves this case to the reader.) Now the solution stays in $y > K$, so $|1 - y/K| = y/K - 1$ and (9) becomes $\ln\big(y/(y/K - 1)\big) = rt + c$, that is, $y/(y/K - 1) = Ce^{rt}$, or $y/(1 - y/K) = -Ce^{rt}$. This is (10) with the constant $-C$, and the initial condition again gives the constant $y_0/(1 - y_0/K)$; the same algebra leads to (11).
>
> **Cases $y_0 = 0$ and $y_0 = K$.** Formula (11) gives $y = 0$ and $y = K$, which are the solutions by [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-4|Definition §9.4]] and the uniqueness part of Theorem 2.4.2 ([[§14 The Existence and Uniqueness Theorem#^thm-14-8|Theorem §14.8]]).
>
> **Domain and limit.** For $t \ge 0$ the denominator $y_0 + (K - y_0)e^{-rt}$ is positive when $y_0 > 0$: it lies between $y_0$ and $K$. So (11) is defined for all $t \ge 0$, and as $t \to \infty$, $e^{-rt} \to 0$ and $y(t) \to y_0K/y_0 = K$.

^pf-9-3

*Uses:* [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-3|Def. §9.3]], [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-4|Def. §9.4]], [[§8 Differences Between Linear and Nonlinear Differential Equations#^cor-8-3|§8.3]] (solutions do not cross), [[§14 The Existence and Uniqueness Theorem#^thm-14-8|§14.8]] (uniqueness), [[§6 Separable Differential Equations#^thm-6-1|§6.1]] (separation of variables)

*Forward reference: [[§14 The Existence and Uniqueness Theorem#^thm-14-8|Theorem §14.8]] (BDP Theorem 2.4.2) is proved later, in [[§14 The Existence and Uniqueness Theorem|§14]] (BDP 2.8).*

So, for each $y_0 > 0$, the solution approaches the equilibrium solution $y = K$ as $t \to \infty$: after a long time the population is close to the saturation level regardless of its initial size, as long as that is positive, and solutions approach $K$ faster as $r$ increases. By contrast, solutions that start very near zero grow and approach $K$: the only way to make a solution remain near zero is to start *exactly* at zero.

> [!definition] Definition §9.6: Asymptotically Stable and Unstable Equilibria
> Let $y = y_1$ be an equilibrium solution of the autonomous equation (1).
> - It is an **asymptotically stable solution** (and $y_1$ an **asymptotically stable** equilibrium or critical point) if solutions that start sufficiently near $y_1$, on either side, approach $y_1$ as $t \to \infty$.
> - It is an **unstable equilibrium solution** (and $y_1$ an **unstable** critical point) if solutions that start near $y_1$, on either side, move away from it, however close to $y_1$ they start.
>
> For the logistic equation (7), $y = K$ is asymptotically stable and $y = 0$ is unstable ([[§9 Autonomous Differential Equations and Population Dynamics#^prop-9-3|Proposition §9.3]]).
>
> *BDP: 2.5 (text)*

^def-9-6

> [!example] Example §9.1: The Pacific Halibut
> The logistic model has been applied to the natural growth of the halibut population in certain areas of the Pacific Ocean. Let $y$, measured in kilograms, be the biomass (the total mass) of the population at time $t$. The parameters are estimated to be $r = 0.71$/year and $K = 80.5 \times 10^6$ kg. If the initial biomass is $y_0 = 0.25K$, find the biomass 2 years later, and the time $\tau$ for which $y(\tau) = 0.75K$.
>
> **Scaling.** Divide (11) by $K$ (numerator and denominator by $K$):
>
> $$
> \frac yK = \frac{y_0/K}{(y_0/K) + (1 - y_0/K)e^{-rt}} . \qquad (12)
> $$
>
> **The biomass after 2 years.** With $y_0/K = 0.25$, $rt = 0.71 \cdot 2 = 1.42$:
>
> $$
> \frac{y(2)}{K} = \frac{0.25}{0.25 + 0.75e^{-1.42}} \cong \frac{0.25}{0.25 + 0.75 \cdot 0.24171} \cong 0.5797 ,
> $$
>
> so $y(2) \cong 0.5797 \cdot 80.5 \times 10^6 \cong 46.7 \times 10^6$ kg.
>
> **The time to reach $0.75K$.** Solve (12) for $t$. Cross-multiplying, $(y/K)(y_0/K) + (y/K)(1 - y_0/K)e^{-rt} = y_0/K$, so
>
> $$
> e^{-rt} = \frac{(y_0/K)(1 - y/K)}{(y/K)(1 - y_0/K)}, \qquad t = -\frac1r \ln \frac{(y_0/K)(1 - y/K)}{(y/K)(1 - y_0/K)} . \qquad (13)
> $$
>
> With $y_0/K = 0.25$ and $y/K = 0.75$:
>
> $$
> \tau = -\frac{1}{0.71} \ln \frac{(0.25)(0.25)}{(0.75)(0.75)} = \frac{1}{0.71} \ln 9 \cong 3.095 \text{ years} .
> $$
>
> *BDP: Example 2.5.1*

^ex-9-1

## Stability in General

The ideas of [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-6|Definition §9.6]] apply to any autonomous equation, and two refinements from BDP's problems are used in the course: the semistable case, and a test for stability by the sign of $f'$.

> [!definition] Definition §9.7: Semistable Equilibrium
> An equilibrium solution $y = y_1$ of (1) is **semistable** if solutions lying on one side of it tend to approach it, whereas solutions lying on the other side depart from it.
>
> For example, $dy/dt = k(1 - y)^2$ with $k > 0$ has the single critical point $y = 1$, and $f(y) = k(1 - y)^2 > 0$ on both sides of it: solutions below $y = 1$ increase toward it, and solutions above it increase away from it. So $y = 1$ is semistable.
>
> *BDP: Problem 2.5.5*

^def-9-7

> [!theorem] Lemma §9.4: Monotone Bounded Solutions Tend to Equilibria
> Let $f$ be continuous, and let $y = \phi(t)$ be a solution of (1) on $[t_0, \infty)$ that is monotone and bounded. Then $L = \lim_{t \to \infty} \phi(t)$ exists and $f(L) = 0$: a solution that levels off does so at a critical point.
>
> *BDP: 2.5 (implicit in the text: solutions that level off do so at a critical point)*

^lem-9-4

> [!proof]+ Proof
> A bounded monotone function has a limit $L$ as $t \to \infty$, namely its supremum (if increasing) or infimum (if decreasing), by the argument of the monotone convergence theorem for sequences ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 Thm. §10.1]]). Suppose $f(L) > 0$. Since $f$ is continuous, $\phi'(t) = f(\phi(t)) \to f(L)$, so there is $T$ with $\phi'(t) \ge f(L)/2$ for $t \ge T$. By the mean value theorem ([[§29 The Mean Value Theorem#^prop-29-8|451 Prop. §29.8]]), $\phi(t) \ge \phi(T) + \frac12 f(L)(t - T) \to \infty$, contradicting boundedness. The case $f(L) < 0$ is the same with the inequalities reversed. Hence $f(L) = 0$.

^pf-9-4

*Uses:* [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-4|Def. §9.4]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 Thm. §10.1]] (monotone convergence), [[§29 The Mean Value Theorem#^prop-29-8|451 Prop. §29.8]] (mean value inequality)

> [!theorem] Proposition §9.5: Stability from the Sign of the Derivative
> Let $f$ have a continuous derivative, and let $y_1$ be a critical point of (1), $f(y_1) = 0$. If $f'(y_1) < 0$, the equilibrium solution $\phi(t) = y_1$ is asymptotically stable; if $f'(y_1) > 0$, it is unstable.
>
> *BDP: Problem 2.5.14*

^prop-9-5

> [!proof]+ Proof
> **$f'(y_1) < 0$.** Since $f(y_1) = 0$, the difference quotient $f(y)/(y - y_1)$ tends to $f'(y_1) < 0$ as $y \to y_1$. So there is $\delta > 0$ such that $f(y) > 0$ for $y_1 - \delta < y < y_1$ and $f(y) < 0$ for $y_1 < y < y_1 + \delta$. Let $\phi$ be a solution with $y_1 - \delta < \phi(t_0) < y_1$. While $\phi$ stays in this interval it increases, since $\phi' = f(\phi) > 0$; and it can never reach $y_1$, because its graph cannot meet the equilibrium solution ([[§8 Differences Between Linear and Nonlinear Differential Equations#^cor-8-3|Corollary §8.3]]). So $\phi$ is increasing and $\phi(t_0) \le \phi(t) < y_1$; as BDP does throughout, we take for granted that such a solution, confined to a bounded interval, exists for all $t \ge t_0$. By [[§9 Autonomous Differential Equations and Population Dynamics#^lem-9-4|Lemma §9.4]], $\phi(t) \to L$ with $f(L) = 0$ and $\phi(t_0) < L \le y_1$; the only zero of $f$ in that range is $y_1$. Likewise a solution starting in $(y_1, y_1 + \delta)$ decreases to $y_1$. So $y_1$ is asymptotically stable.
>
> **$f'(y_1) > 0$.** Now there is $\delta > 0$ with $f < 0$ on $(y_1 - \delta, y_1)$ and $f > 0$ on $(y_1, y_1 + \delta]$. A solution starting in $(y_1, y_1 + \delta)$ increases. If it stayed below $y_1 + \delta$ for all $t \ge t_0$, it would be monotone and bounded, and by [[§9 Autonomous Differential Equations and Population Dynamics#^lem-9-4|Lemma §9.4]] it would tend to a zero of $f$ in $(y_1, y_1 + \delta]$; there is none. So it leaves the interval: it moves away from $y_1$, however close to $y_1$ it starts. The same holds below $y_1$, so $y_1$ is unstable.

^pf-9-5

*Uses:* [[§9 Autonomous Differential Equations and Population Dynamics#^lem-9-4|§9.4]], [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-6|Def. §9.6]], [[§8 Differences Between Linear and Nonlinear Differential Equations#^cor-8-3|§8.3]]

If $f'(y_1) = 0$ the test says nothing: $y' = k(1 - y)^2$ ([[§9 Autonomous Differential Equations and Population Dynamics#^def-9-7|Definition §9.7]]) has $f'(1) = 0$ and a semistable point, while $y' = -(y - 1)^3$ has $f'(1) = 0$ and an asymptotically stable one.

> [!remark] Remark: Method — Qualitative Analysis of an Autonomous Equation
> For $dy/dt = f(y)$:
> 1. **Critical points.** Solve $f(y) = 0$. Each root $y_1$ gives an equilibrium solution $y = y_1$ ([[§9 Autonomous Differential Equations and Population Dynamics#^def-9-4|Definition §9.4]]).
> 2. **Signs.** Determine the sign of $f$ on each interval between consecutive critical points, from the graph of $f$ against $y$ or from a sign table of its factors. Draw the phase line: an up arrow where $f > 0$, a down arrow where $f < 0$ ([[§9 Autonomous Differential Equations and Population Dynamics#^def-9-5|Definition §9.5]]).
> 3. **Classify.** Arrows pointing toward $y_1$ on both sides: asymptotically stable. Away on both sides: unstable. Toward on one side and away on the other: semistable (Definitions [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-6|§9.6]], [[§9 Autonomous Differential Equations and Population Dynamics#^def-9-7|§9.7]]). Equivalently, when $f'(y_1) \ne 0$: stable if $f'(y_1) < 0$, unstable if $f'(y_1) > 0$ ([[§9 Autonomous Differential Equations and Population Dynamics#^prop-9-5|Proposition §9.5]]).
> 4. **Concavity.** By [[§9 Autonomous Differential Equations and Population Dynamics#^prop-9-2|Proposition §9.2]], solutions are concave up where $f'f > 0$ and concave down where $f'f < 0$; inflection points lie on the lines $y = c$ where $f'(c) = 0$.
> 5. **Sketch.** Draw the equilibrium solutions as horizontal lines. Between them, draw solutions that are monotone in the direction of the arrows, never cross an equilibrium ([[§8 Differences Between Linear and Nonlinear Differential Equations#^cor-8-3|Corollary §8.3]]), flatten as they approach an equilibrium, and change concavity on the lines found in step 4. As $t \to \infty$ each bounded solution approaches an equilibrium ([[§9 Autonomous Differential Equations and Population Dynamics#^lem-9-4|Lemma §9.4]]).

^rem-9-1

> [!example] Example §9.2: A Mixing Tank as an Autonomous Equation
> A 5 gallon vat is full of pure water. At time $t = 0$ salt water is added through a pipe carrying water at a rate of 2 gallons per minute and a concentration of $\frac14$ pound per gallon. Water drains out at 2 gallons per minute, so the level stays at 5 gallons; the salt is always evenly mixed. Let $S(t)$ be the amount of salt (in pounds) at time $t$ (in minutes). **(a)** Set up the differential equation and initial condition. **(b)** Find $\lim_{t \to \infty} S(t)$, justifying the answer by classifying the equilibrium point.
>
> **(a)** As in [[§7 Modeling with First-Order Differential Equations#^rem-7-2|Remark: Method — Mixing Problems]], rate of change = rate in − rate out. Salt enters at $2 \cdot \frac14 = \frac12$ lb/min and leaves at $2 \cdot \frac{S}{5}$ lb/min (the outflow has concentration $S/5$), so
>
> $$
> \frac{dS}{dt} = \frac12 - \frac25 S, \qquad S(0) = 0 .
> $$
>
> **(b)** The equation is autonomous with $f(S) = \frac12 - \frac25 S$. Its only critical point is $S = \frac54$. For $S < \frac54$, $f(S) > 0$ (for instance $f(0) = \frac12$), and for $S > \frac54$, $f(S) < 0$ (for instance $f(2) = \frac12 - \frac45 < 0$). So the phase line has an up arrow below $\frac54$ and a down arrow above it, and $S = \frac54$ is asymptotically stable; also $f'(S) = -\frac25 < 0$ ([[§9 Autonomous Differential Equations and Population Dynamics#^prop-9-5|Proposition §9.5]]). Since it is the only equilibrium, every solution approaches it ([[§9 Autonomous Differential Equations and Population Dynamics#^lem-9-4|Lemma §9.4]]), whatever the initial amount:
>
> $$
> \lim_{t \to \infty} S(t) = \frac54 \text{ lb} .
> $$
>
> This is the concentration of the inflow, $\frac14$ lb/gal, times the volume, $5$ gal. Here the equation is also linear and can be solved: $S(t) = \frac54\big(1 - e^{-2t/5}\big)$, which confirms the limit.
>
> *Source: 331 Midterm (Spring 2020), Q6*

^ex-9-2

The threshold models and bifurcation points of BDP 2.5 continue in [[§10 Critical Thresholds and Bifurcations]].
