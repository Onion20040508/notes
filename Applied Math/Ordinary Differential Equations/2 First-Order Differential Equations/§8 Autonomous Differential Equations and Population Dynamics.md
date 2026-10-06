---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 8
bdp: "2.5"
aliases: ["BDP 2.5"]
tags: [ordinary-differential-equations, math331]
---
← [[§7 Differences Between Linear and Nonlinear Differential Equations]] · ↑ [[· 2 First-Order Differential Equations]] · [[§9 Exact Differential Equations and Integrating Factors]] →

*Boyce–DiPrima, Section 2.5 · MATH 331 Written HW 2 (Problem 2), Midterm (Fall 2021) Q5, Midterm (Spring 2020) Q6.*

An autonomous equation $dy/dt = f(y)$ is one whose right side does not depend on $t$. It is separable, but the point of this section is that the graph of $f$ alone, without solving anything, shows how every solution behaves: where the equilibrium solutions are, which of them attract nearby solutions and which repel them, where solution curves bend, and what happens as $t \to \infty$. This qualitative picture is developed on models of population growth: exponential growth, the logistic equation with its carrying capacity, growth with a critical threshold, and a combination of the two. It is the one-dimensional case of the stability theory of Chapter 9 of BDP.

> [!definition] Definition §8.1: Autonomous Equation
> A first-order differential equation in which the independent variable does not appear explicitly,
>
> $$
> \frac{dy}{dt} = f(y) , \qquad (1)
> $$
>
> is called **autonomous**. The special case $f(y) = ay - b$ was solved in [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]].
>
> *BDP: 2.5, equation (1)*

^def-8-1

> [!remark]- Connections
> - See also: [[§58 Direction Fields and Euler's Method#^def-58-3|Calc Def. §58.3]] (Stewart's autonomous equations), with the observation that a time-shift of a solution is again a solution, [[§58 Direction Fields and Euler's Method#^prop-58-1|Calc Prop. §58.1]]; and Stewart's logistic model, [[§60 Models for Population Growth#^def-60-2|Calc Def. §60.2]], [[§57 Modeling with Differential Equations#^prop-57-2|Calc Prop. §57.2]] (its qualitative behaviour) and [[§60 Models for Population Growth#^thm-60-2|Calc Thm. §60.2]] (its solution). The treatment here is fuller: phase lines, stability, thresholds and bifurcations.

## Exponential Growth

> [!definition] Definition §8.2: Exponential Growth; Rate of Growth or Decline
> Let $y = \phi(t)$ be the population of a species at time $t$. The simplest hypothesis is that the rate of change of $y$ is proportional to the current value of $y$:
>
> $$
> \frac{dy}{dt} = ry . \qquad (2)
> $$
>
> The constant $r$ is the **rate of growth** if $r > 0$ and the **rate of decline** if $r < 0$ (the rate constant of [[§1 Some Basic Mathematical Models; Direction Fields#^def-1-4|Definition §1.4]]). (In this section $y$ is a population, so the initial value $y(0) = y_0$ is taken positive.)
>
> *BDP: 2.5, equation (2)*

^def-8-2

> [!theorem] Proposition §8.1: Solution of the Exponential Growth Model
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

^prop-8-1

> [!proof]+ Proof
> Equation (2) is linear, $y' - ry = 0$, with integrating factor $e^{-rt}$: $(e^{-rt}y)' = 0$, so $e^{-rt}y = c$ and $y = ce^{rt}$. The initial condition gives $c = y_0$. By [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] this is the only solution, on all of $-\infty < t < \infty$.

^pf-8-1

*Uses:* [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|§7.1]], [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|§4.2]] (integrating factors)

With $r > 0$ the model predicts that the population grows exponentially for all time. Under ideal conditions (4) is reasonably accurate for many populations, at least for limited periods of time, but eventually limitations on space, food supply or other resources reduce the growth rate. (The observation goes back to Thomas Malthus, 1798; see also [[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]].)

## Logistic Growth

To account for the dependence of the growth rate on the population, replace the constant $r$ in (2) by a function $h(y)$: $dy/dt = h(y)\,y$ (5). Choose $h$ so that $h(y) \cong r > 0$ when $y$ is small, $h(y)$ decreases as $y$ grows, and $h(y) < 0$ when $y$ is large enough. The simplest such function is $h(y) = r - ay$ with $a > 0$.

> [!definition] Definition §8.3: Logistic Equation; Intrinsic Growth Rate
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

^def-8-3

The rest of this section shows how to sketch qualitatively correct solutions of (7), and of the general autonomous equation (1), without solving.

> [!definition] Definition §8.4: Equilibrium Solutions; Critical Points
> A constant solution $y = \phi(t) = y_1$ of the autonomous equation (1) is called an **equilibrium solution** (as in [[§1 Some Basic Mathematical Models; Direction Fields#^def-1-3|Definition §1.3]]), because it corresponds to no change in $y$ as $t$ increases. Since $dy/dt = 0$ for a constant function, the equilibrium solutions are found by locating the roots of
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

^def-8-4

To see the other solutions, graph $f(y)$ against $y$. For (7) the graph of $f(y) = r(1 - y/K)y$ is a parabola with intercepts $(0, 0)$ and $(K, 0)$, the critical points, and vertex $(K/2, rK/4)$. So $dy/dt > 0$ for $0 < y < K$, and $y$ is an increasing function of $t$ when $y$ is in this interval; and $dy/dt < 0$ for $y > K$, so there $y$ is decreasing.

> [!definition] Definition §8.5: Phase Line
> The $y$-axis, marked with the critical points and with arrows showing where $y$ increases ($f(y) > 0$) and where it decreases ($f(y) < 0$), is called the **phase line** of the autonomous equation (1). It is usually drawn vertically.
>
> For the logistic equation the phase line has dots at $y = 0$ and $y = K$, an upward arrow on $0 < y < K$ and a downward arrow on $y > K$.
>
> *BDP: 2.5 (text), Figure 2.5.3(a)*

^def-8-5

Near $y = 0$ and $y = K$ the slope $f(y)$ is near zero, so solution curves are flat there, and they steepen as $y$ moves away. Sketching in the $ty$-plane: draw the equilibrium solutions $y = 0$ and $y = K$; then curves that increase when $0 < y < K$, decrease when $y > K$, and flatten as $y$ approaches $0$ or $K$.

The sketch may seem to show other solutions running into $y = K$, but they cannot: by the uniqueness part of Theorem 2.4.2 only one solution passes through a given point of the $ty$-plane ([[§7 Differences Between Linear and Nonlinear Differential Equations#^cor-7-3|Corollary §7.3]]). So, although other solutions may be asymptotic to the equilibrium solution as $t \to \infty$, they never meet it at a finite time. A solution that starts in $0 < y < K$ stays there for all time, and one that starts in $K < y < \infty$ stays there.

Concavity and inflection points come from the second derivative.

> [!theorem] Proposition §8.2: Concavity of Solutions of an Autonomous Equation
> If $f$ is differentiable and $y = \phi(t)$ solves (1), then
>
> $$
> \frac{d^2y}{dt^2} = f'(y)\,f(y) . \qquad (8)
> $$
>
> So the graph of $y$ against $t$ is concave up where $f$ and $f'$ have the same sign, concave down where they have opposite signs, and inflection points may occur where $f'(y) = 0$.
>
> *BDP: 2.5, equation (8)*

^prop-8-2

> [!proof]+ Proof
> By (1) and the chain rule,
>
> $$
> \frac{d^2y}{dt^2} = \frac{d}{dt}\frac{dy}{dt} = \frac{d}{dt} f(y) = f'(y)\frac{dy}{dt} = f'(y)\,f(y) .
> $$
>
> The concavity statements are the sign of $y''$. (Away from the critical points $f(y) \ne 0$, so $y''$ can change sign only where $f'(y)$ does.)

^pf-8-2

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-1|Def. §8.1]]

For the logistic equation (7): on $0 < y < K/2$, $f$ is positive and increasing, so $f, f' > 0$ and solutions are concave up; on $K/2 < y < K$, $f > 0 > f'$, concave down; on $y > K$, $f$ is negative and decreasing, $f, f' < 0$, concave up. Every solution curve that crosses the line $y = K/2$ has an inflection point there. Finally, $K$ is the upper bound that is approached, but not exceeded, by growing populations starting below it, which justifies the names *saturation level* and *carrying capacity*. Comparing with (4): however small the nonlinear term in (7) (that is, however large $K$), solutions of (7) approach a finite value as $t \to \infty$, whereas solutions of (2) grow without bound. A tiny nonlinear term has a decisive effect for large $t$.

For quantitative information, solve (7).

> [!theorem] Proposition §8.3: Solution of the Logistic Equation
> The solution of the logistic equation (7) with $y(0) = y_0 \ge 0$ is
>
> $$
> y = \frac{y_0 K}{y_0 + (K - y_0)e^{-rt}} , \qquad (11)
> $$
>
> defined for all $t \ge 0$. It includes the equilibrium solutions $y = 0$ ($y_0 = 0$) and $y = K$ ($y_0 = K$). If $y_0 > 0$, then $\lim_{t \to \infty} y(t) = K$.
>
> *BDP: 2.5, equation (11)*

^prop-8-3

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
> **Cases $y_0 = 0$ and $y_0 = K$.** Formula (11) gives $y = 0$ and $y = K$, which are the solutions by [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-4|Definition §8.4]] and the uniqueness part of Theorem 2.4.2 ([[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]]).
>
> **Domain and limit.** For $t \ge 0$ the denominator $y_0 + (K - y_0)e^{-rt}$ is positive when $y_0 > 0$: it lies between $y_0$ and $K$. So (11) is defined for all $t \ge 0$, and as $t \to \infty$, $e^{-rt} \to 0$ and $y(t) \to y_0K/y_0 = K$.

^pf-8-3

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-3|Def. §8.3]], [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-4|Def. §8.4]], [[§7 Differences Between Linear and Nonlinear Differential Equations#^cor-7-3|§7.3]] (solutions do not cross), [[§11 The Existence and Uniqueness Theorem#^thm-11-8|§11.8]] (uniqueness), [[§5 Separable Differential Equations#^thm-5-1|§5.1]] (separation of variables)

So, for each $y_0 > 0$, the solution approaches the equilibrium solution $y = K$ as $t \to \infty$: after a long time the population is close to the saturation level regardless of its initial size, as long as that is positive, and solutions approach $K$ faster as $r$ increases. By contrast, solutions that start very near zero grow and approach $K$: the only way to make a solution remain near zero is to start *exactly* at zero.

> [!definition] Definition §8.6: Asymptotically Stable and Unstable Equilibria
> Let $y = y_1$ be an equilibrium solution of the autonomous equation (1).
> - It is an **asymptotically stable solution** (and $y_1$ an **asymptotically stable** equilibrium or critical point) if solutions that start sufficiently near $y_1$, on either side, approach $y_1$ as $t \to \infty$.
> - It is an **unstable equilibrium solution** (and $y_1$ an **unstable** critical point) if solutions that start near $y_1$, on either side, move away from it, however close to $y_1$ they start.
>
> For the logistic equation (7), $y = K$ is asymptotically stable and $y = 0$ is unstable ([[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|Proposition §8.3]]).
>
> *BDP: 2.5 (text)*

^def-8-6

> [!example] Example §8.1: The Pacific Halibut
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

^ex-8-1

## Stability in General

The ideas of [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-6|Definition §8.6]] apply to any autonomous equation, and two refinements from BDP's problems are used in the course: the semistable case, and a test for stability by the sign of $f'$.

> [!definition] Definition §8.7: Semistable Equilibrium
> An equilibrium solution $y = y_1$ of (1) is **semistable** if solutions lying on one side of it tend to approach it, whereas solutions lying on the other side depart from it.
>
> For example, $dy/dt = k(1 - y)^2$ with $k > 0$ has the single critical point $y = 1$, and $f(y) = k(1 - y)^2 > 0$ on both sides of it: solutions below $y = 1$ increase toward it, and solutions above it increase away from it. So $y = 1$ is semistable.
>
> *BDP: Problem 2.5.5*

^def-8-7

> [!theorem] Lemma §8.4: Monotone Bounded Solutions Tend to Equilibria
> Let $f$ be continuous, and let $y = \phi(t)$ be a solution of (1) on $[t_0, \infty)$ that is monotone and bounded. Then $L = \lim_{t \to \infty} \phi(t)$ exists and $f(L) = 0$: a solution that levels off does so at a critical point.
>
> *BDP: 2.5 (implicit in the text: solutions that level off do so at a critical point)*

^lem-8-4

> [!proof]+ Proof
> A bounded monotone function has a limit $L$ as $t \to \infty$, namely its supremum (if increasing) or infimum (if decreasing), by the argument of the monotone convergence theorem for sequences. Suppose $f(L) > 0$. Since $f$ is continuous, $\phi'(t) = f(\phi(t)) \to f(L)$, so there is $T$ with $\phi'(t) \ge f(L)/2$ for $t \ge T$. By the mean value theorem, $\phi(t) \ge \phi(T) + \frac12 f(L)(t - T) \to \infty$, contradicting boundedness. The case $f(L) < 0$ is the same with the inequalities reversed. Hence $f(L) = 0$.

^pf-8-4

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-4|Def. §8.4]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 Thm. §10.1]] (monotone convergence), [[§29 The Mean Value Theorem#^prop-29-8|451 Prop. §29.8]] (mean value inequality)

> [!theorem] Proposition §8.5: Stability from the Sign of the Derivative
> Let $f$ have a continuous derivative, and let $y_1$ be a critical point of (1), $f(y_1) = 0$. If $f'(y_1) < 0$, the equilibrium solution $\phi(t) = y_1$ is asymptotically stable; if $f'(y_1) > 0$, it is unstable.
>
> *BDP: Problem 2.5.14*

^prop-8-5

> [!proof]+ Proof
> **$f'(y_1) < 0$.** Since $f(y_1) = 0$, the difference quotient $f(y)/(y - y_1)$ tends to $f'(y_1) < 0$ as $y \to y_1$. So there is $\delta > 0$ such that $f(y) > 0$ for $y_1 - \delta < y < y_1$ and $f(y) < 0$ for $y_1 < y < y_1 + \delta$. Let $\phi$ be a solution with $y_1 - \delta < \phi(t_0) < y_1$. While $\phi$ stays in this interval it increases, since $\phi' = f(\phi) > 0$; and it can never reach $y_1$, because its graph cannot meet the equilibrium solution ([[§7 Differences Between Linear and Nonlinear Differential Equations#^cor-7-3|Corollary §7.3]]). So $\phi$ is increasing and $\phi(t_0) \le \phi(t) < y_1$; as BDP does throughout, we take for granted that such a solution, confined to a bounded interval, exists for all $t \ge t_0$. By [[§8 Autonomous Differential Equations and Population Dynamics#^lem-8-4|Lemma §8.4]], $\phi(t) \to L$ with $f(L) = 0$ and $\phi(t_0) < L \le y_1$; the only zero of $f$ in that range is $y_1$. Likewise a solution starting in $(y_1, y_1 + \delta)$ decreases to $y_1$. So $y_1$ is asymptotically stable.
>
> **$f'(y_1) > 0$.** Now there is $\delta > 0$ with $f < 0$ on $(y_1 - \delta, y_1)$ and $f > 0$ on $(y_1, y_1 + \delta]$. A solution starting in $(y_1, y_1 + \delta)$ increases. If it stayed below $y_1 + \delta$ for all $t \ge t_0$, it would be monotone and bounded, and by Lemma §8.4 it would tend to a zero of $f$ in $(y_1, y_1 + \delta]$; there is none. So it leaves the interval: it moves away from $y_1$, however close to $y_1$ it starts. The same holds below $y_1$, so $y_1$ is unstable.

^pf-8-5

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^lem-8-4|§8.4]], [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-6|Def. §8.6]], [[§7 Differences Between Linear and Nonlinear Differential Equations#^cor-7-3|§7.3]]

If $f'(y_1) = 0$ the test says nothing: $y' = k(1 - y)^2$ ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-7|Definition §8.7]]) has $f'(1) = 0$ and a semistable point, while $y' = -(y - 1)^3$ has $f'(1) = 0$ and an asymptotically stable one.

> [!remark] Remark: Method — Qualitative Analysis of an Autonomous Equation
> For $dy/dt = f(y)$:
> 1. **Critical points.** Solve $f(y) = 0$. Each root $y_1$ gives an equilibrium solution $y = y_1$ ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-4|Definition §8.4]]).
> 2. **Signs.** Determine the sign of $f$ on each interval between consecutive critical points, from the graph of $f$ against $y$ or from a sign table of its factors. Draw the phase line: an up arrow where $f > 0$, a down arrow where $f < 0$ ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-5|Definition §8.5]]).
> 3. **Classify.** Arrows pointing toward $y_1$ on both sides: asymptotically stable. Away on both sides: unstable. Toward on one side and away on the other: semistable (Definitions [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-6|§8.6]], [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-7|§8.7]]). Equivalently, when $f'(y_1) \ne 0$: stable if $f'(y_1) < 0$, unstable if $f'(y_1) > 0$ ([[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-5|Proposition §8.5]]).
> 4. **Concavity.** By [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|Proposition §8.2]], solutions are concave up where $f'f > 0$ and concave down where $f'f < 0$; inflection points lie on the lines $y = c$ where $f'(c) = 0$.
> 5. **Sketch.** Draw the equilibrium solutions as horizontal lines. Between them, draw solutions that are monotone in the direction of the arrows, never cross an equilibrium ([[§7 Differences Between Linear and Nonlinear Differential Equations#^cor-7-3|Corollary §7.3]]), flatten as they approach an equilibrium, and change concavity on the lines found in step 4. As $t \to \infty$ each bounded solution approaches an equilibrium ([[§8 Autonomous Differential Equations and Population Dynamics#^lem-8-4|Lemma §8.4]]).

^rem-8-1

> [!example] Example §8.2: A Mixing Tank as an Autonomous Equation
> A 5 gallon vat is full of pure water. At time $t = 0$ salt water is added through a pipe carrying water at a rate of 2 gallons per minute and a concentration of $\frac14$ pound per gallon. Water drains out at 2 gallons per minute, so the level stays at 5 gallons; the salt is always evenly mixed. Let $S(t)$ be the amount of salt (in pounds) at time $t$ (in minutes). **(a)** Set up the differential equation and initial condition. **(b)** Find $\lim_{t \to \infty} S(t)$, justifying the answer by classifying the equilibrium point.
>
> **(a)** As in [[§6 Modeling with First-Order Differential Equations#^rem-6-2|Remark: Method — Mixing Problems]], rate of change = rate in − rate out. Salt enters at $2 \cdot \frac14 = \frac12$ lb/min and leaves at $2 \cdot \frac{S}{5}$ lb/min (the outflow has concentration $S/5$), so
>
> $$
> \frac{dS}{dt} = \frac12 - \frac25 S, \qquad S(0) = 0 .
> $$
>
> **(b)** The equation is autonomous with $f(S) = \frac12 - \frac25 S$. Its only critical point is $S = \frac54$. For $S < \frac54$, $f(S) > 0$ (for instance $f(0) = \frac12$), and for $S > \frac54$, $f(S) < 0$ (for instance $f(2) = \frac12 - \frac45 < 0$). So the phase line has an up arrow below $\frac54$ and a down arrow above it, and $S = \frac54$ is asymptotically stable; also $f'(S) = -\frac25 < 0$ ([[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-5|Proposition §8.5]]). Since it is the only equilibrium, every solution approaches it ([[§8 Autonomous Differential Equations and Population Dynamics#^lem-8-4|Lemma §8.4]]), whatever the initial amount:
>
> $$
> \lim_{t \to \infty} S(t) = \frac54 \text{ lb} .
> $$
>
> This is the concentration of the inflow, $\frac14$ lb/gal, times the volume, $5$ gal. Here the equation is also linear and can be solved: $S(t) = \frac54\big(1 - e^{-2t/5}\big)$, which confirms the limit.
>
> *Source: 331 Midterm (Spring 2020), Q6*

^ex-8-2

## A Critical Threshold

Changing the sign of the right side of the logistic equation changes the behaviour completely. Consider

$$
\frac{dy}{dt} = -r\Big(1 - \frac yT\Big)y , \qquad (14)
$$

with positive constants $r$ and $T$. The graph of $f(y)$ is now a downward-shifted parabola through the critical points $y = 0$ and $y = T$, with vertex $(T/2, -rT/4)$. If $0 < y < T$ then $dy/dt < 0$ and $y$ decreases, so $\phi_1(t) = 0$ is asymptotically stable; if $y > T$ then $dy/dt > 0$ and $y$ increases, so $\phi_2(t) = T$ is unstable. By [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|Proposition §8.2]], $f'(y) < 0$ for $0 < y < T/2$ and $f'(y) > 0$ for $T/2 < y < T$, so solutions in the strip $0 < y < T$ are concave up below $T/2$ and concave down above it; for $y > T$ both $f$ and $f'$ are positive, and solutions are concave up. The solutions in $0 < y < T$ decrease to $0$; those above $T$ increase more and more steeply.

> [!definition] Definition §8.8: Threshold Level
> In equation (14) the value $T$ is a **threshold level**: if the initial value $y_0$ is less than $T$, the solution approaches zero as $t$ increases, and if $y_0 > T$ it grows without bound. Below the threshold, growth does not occur.
>
> *BDP: 2.5 (text)*

^def-8-8

> [!remark]- Connections
> - Stewart's versions of a threshold (a minimum viable population) and of harvesting, as modifications of the logistic equation: [[§60 Models for Population Growth#^def-60-3|Calc Def. §60.3]].

> [!theorem] Proposition §8.6: Solution of the Threshold Equation
> The solution of (14) with $y(0) = y_0 > 0$ is
>
> $$
> y = \frac{y_0 T}{y_0 + (T - y_0)e^{rt}} . \qquad (15)
> $$
>
> If $0 < y_0 < T$, then $y \to 0$ as $t \to \infty$. If $y_0 > T$, the denominator vanishes at
>
> $$
> t^* = \frac1r \ln \frac{y_0}{y_0 - T} , \qquad (16)
> $$
>
> and the solution has a vertical asymptote there: the population becomes unbounded in finite time.
>
> *BDP: 2.5, equations (15) and (16)*

^prop-8-6

> [!proof]+ Proof
> Equation (14) is (7) with $K$ replaced by $T$ and $r$ by $-r$, and the derivation of [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|Proposition §8.3]] did not use the sign of $r$; making the same replacements in (11) gives (15). To check it directly, let $D(t) = y_0 + (T - y_0)e^{rt}$, so $y = y_0T/D$ and $D - y_0 = (T - y_0)e^{rt}$. Then
>
> $$
> y' = -\frac{y_0T\,D'}{D^2} = -\frac{y_0T\,r(T - y_0)e^{rt}}{D^2}, \qquad
> -r\Big(1 - \frac yT\Big)y = -r\,\frac{D - y_0}{D}\,\frac{y_0T}{D} = -\frac{r\,(T - y_0)e^{rt}\,y_0T}{D^2} ,
> $$
>
> which agree, and $y(0) = y_0T/T = y_0$. By the uniqueness part of Theorem 2.4.2 ([[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]]) this is the solution as long as $D \ne 0$.
>
> If $0 < y_0 < T$, then $D(t) \ge y_0 > 0$ for $t \ge 0$ and $D(t) \to \infty$, so $y \to 0$. If $y_0 > T$, then $D(t) = y_0 - (y_0 - T)e^{rt}$ decreases from $y_0$ and vanishes when $e^{rt^*} = y_0/(y_0 - T)$, which is (16); since $y_0/(y_0 - T) > 1$, $t^* > 0$. As $t \to t^{*-}$, $D \to 0^+$ and $y \to +\infty$. (BDP leaves (16) as Problem 12.)

^pf-8-6

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|§8.3]], [[§11 The Existence and Uniqueness Theorem#^thm-11-8|§11.8]] (uniqueness)

The existence and location of this asymptote were not visible in the geometric analysis: here the explicit solution adds qualitative as well as quantitative information. Some species show the threshold phenomenon: if too few are present, the species cannot propagate itself successfully and becomes extinct, while above the threshold the population grows. In fluid mechanics, equations of the form (7) or (14) govern a small disturbance $y$ of a laminar flow; under (14) a disturbance below the *critical amplitude* $T$ is damped out, and one above it grows and the flow becomes turbulent.

## Logistic Growth with a Threshold

Unbounded growth is unrealistic, so (14) is modified by a factor that makes $dy/dt$ negative when $y$ is large:

$$
\frac{dy}{dt} = -r\Big(1 - \frac yT\Big)\Big(1 - \frac yK\Big)y , \qquad r > 0,\ 0 < T < K . \qquad (17)
$$

There are three critical points, $y = 0$, $y = T$ and $y = K$, giving the equilibrium solutions $\phi_1(t) = 0$, $\phi_2(t) = T$, $\phi_3(t) = K$. From the graph of $f$: $dy/dt > 0$ for $T < y < K$, and $dy/dt < 0$ for $y < T$ and for $y > K$. So $\phi_1 = 0$ and $\phi_3 = K$ are asymptotically stable and $\phi_2 = T$ is unstable. A population starting below the threshold $T$ declines to extinction; one starting above $T$ approaches the carrying capacity $K$. A model of this sort apparently describes the passenger pigeon, which could breed successfully only in large concentrations: by the late 1880s too few remained in any one place, and the species died out (the last one in 1914).

> [!theorem] Proposition §8.7: Inflection Points for Logistic Growth with a Threshold
> The inflection points of the solutions of (17) lie on the lines $y = y_1$ and $y = y_2$, where
>
> $$
> y_{1,2} = \frac{K + T \pm \sqrt{K^2 - KT + T^2}}{3} , \qquad (18)
> $$
>
> the plus sign giving $y_1$ and the minus sign $y_2$. These are the maximum point $y_1 \in (T, K)$ and the minimum point $y_2 \in (0, T)$ of $f(y)$.
>
> *BDP: 2.5, equation (18)*

^prop-8-7

> [!proof]+ Proof
> Expanding, $f(y) = -r\Big(y - \Big(\dfrac1T + \dfrac1K\Big)y^2 + \dfrac{y^3}{TK}\Big)$, so
>
> $$
> f'(y) = -r\Big(1 - \frac{2(T + K)}{TK}\,y + \frac{3y^2}{TK}\Big) = -\frac{r}{TK}\big(3y^2 - 2(K + T)y + KT\big) .
> $$
>
> By the quadratic formula $f'(y) = 0$ at $y = \big(2(K + T) \pm \sqrt{4(K + T)^2 - 12KT}\big)/6$, which simplifies to (18) because $(K + T)^2 - 3KT = K^2 - KT + T^2 > 0$. These are simple roots, so $f'$ changes sign at each of them; since $f(y) \ne 0$ there (by Rolle's theorem $f'$ has one root in $(0, T)$ and one in $(T, K)$, and these are the only two), $y'' = f'(y)f(y)$ changes sign exactly when a solution crosses $y = y_1$ or $y = y_2$ ([[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|Proposition §8.2]]). (BDP leaves the computation as Problem 13.)

^pf-8-7

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|§8.2]], [[§29 The Mean Value Theorem#^thm-29-2|451 Thm. §29.2]] (Rolle's theorem)

> [!example] Example §8.3: Phase Lines with a Threshold
> **(a)** A population of squirrels $P(t)$ ($t$ in years) satisfies
>
> $$
> \frac{dP}{dt} = 2P\Big(1 - \frac P2\Big)(P - 1) .
> $$
>
> Find all equilibrium points, draw the phase line and determine the stability of each. Graph the solutions with $P(0) = \frac18$, $P(0) = 1.5$ and $P(0) = 2.5$.
>
> **Equilibria.** $f(P) = 0$ when $P = 0$, $P = 2$ or $P = 1$.
>
> **Signs.** Tabulate the signs of the factors $2P$, $1 - P/2$ and $P - 1$:
>
> | interval | $2P$ | $1 - P/2$ | $P - 1$ | $f(P)$ | $P(t)$ |
> |---|---|---|---|---|---|
> | $P < 0$ | $-$ | $+$ | $-$ | $+$ | increasing |
> | $0 < P < 1$ | $+$ | $+$ | $-$ | $-$ | decreasing |
> | $1 < P < 2$ | $+$ | $+$ | $+$ | $+$ | increasing |
> | $P > 2$ | $+$ | $-$ | $+$ | $-$ | decreasing |
>
> **Classification.** The arrows point toward $P = 0$ from both sides and toward $P = 2$ from both sides, and away from $P = 1$ on both sides: $P = 0$ and $P = 2$ are asymptotically stable, $P = 1$ is unstable. The derivative test agrees: $f(P) = -P^3 + 3P^2 - 2P$, $f'(P) = -3P^2 + 6P - 2$, and $f'(0) = -2 < 0$, $f'(1) = 1 > 0$, $f'(2) = -2 < 0$.
>
> This is equation (17) with $r = 2$, threshold $T = 1$ and carrying capacity $K = 2$: indeed $-2(1 - P)(1 - P/2)P = 2P(1 - P/2)(P - 1)$. Squirrels below the threshold $1$ die out; above it they approach $2$.
>
> **The three solutions** (figure below). By (18) the inflection lines are $y_{1,2} = \big(3 \pm \sqrt{3}\big)/3 = 1 \pm 1/\sqrt3$, about $1.577$ and $0.423$.
> - $P(0) = \frac18$: below the threshold, so $P$ decreases to $0$; since $\frac18 < 0.423$, it is concave up throughout.
> - $P(0) = 1.5$: between $T = 1$ and $K = 2$, so $P$ increases to $2$; it starts concave up (below $1.577$) and has an inflection point where it crosses $P \approx 1.577$, then flattens toward $2$.
> - $P(0) = 2.5$: above $K$, so $P$ decreases to $2$, concave up.
>
> **(b)** A colony of quokka (in hundreds; $t$ in years) satisfies $\dfrac{dP}{dt} = 3P\Big(1 - \dfrac P3\Big)(P - 1)$. Draw the phase line and classify the equilibria; if $P(0) = P_0$, find all $P_0$ for which $\lim_{t \to \infty} P(t) > 0$.
>
> The same sign table, with $1 - P/3$ in place of $1 - P/2$, gives equilibria $0$ (asymptotically stable), $1$ (unstable) and $3$ (asymptotically stable): equation (17) with $r = 3$, $T = 1$, $K = 3$. A solution with $0 \le P_0 < 1$ decreases to $0$; $P_0 = 1$ stays at $1$; and $P_0 > 1$ gives $P(t) \to 3$. (Negative $P_0$ are not populations; those solutions increase to $0$.) So
>
> $$
> \lim_{t \to \infty} P(t) > 0 \iff P_0 \ge 1 .
> $$
>
> The equilibrium value $P_0 = 1$ belongs to the answer, although it is unstable: the limit of the constant solution is $1 > 0$.
>
> *Source: 331 Written HW 2, Problem 2(a)(b); 331 Midterm (Fall 2021), Q5*

^ex-8-3

![[m331-8-1.svg]]
*The squirrel equation $P' = 2P(1 - P/2)(P - 1)$ of [[§8 Autonomous Differential Equations and Population Dynamics#^ex-8-3|Example §8.3]](a). Left, the phase line: arrows point toward the stable equilibria $0$ and $2$ (green) and away from the unstable threshold $1$ (red). Right, solutions in the $tP$-plane: below the threshold (blue) they decay to $0$, above it (orange) they approach the carrying capacity $2$, never crossing the equilibrium lines. Solutions change concavity on the dashed lines $y_{1,2} = 1 \pm 1/\sqrt3$ of [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-7|Proposition §8.7]].*

## Bifurcation Points

When the right side depends on a parameter $a$, the critical points move as $a$ varies, and at special values of $a$ they can merge or split.

> [!definition] Definition §8.9: Bifurcation Point; Bifurcation Diagram
> For an equation
>
> $$
> \frac{dy}{dt} = f(a, y) ,
> $$
>
> where $a$ is a real parameter, the critical points usually depend on $a$. A value of $a$ at which critical points come together or separate, so that equilibrium solutions are lost or gained, is called a **bifurcation point**. The plot of the critical points as functions of $a$, in the $ay$-plane, is the **bifurcation diagram**. Three standard types:
> - **saddle–node bifurcation**: two critical points merge and disappear, as for $y' = a - y^2$ at $a = 0$ (no critical points for $a < 0$, the semistable point $0$ for $a = 0$, the points $\pm\sqrt a$ for $a > 0$);
> - **pitchfork bifurcation**: one critical point splits into three, as for $y' = ay - y^3$ at $a = 0$;
> - **transcritical bifurcation**: two critical points cross and **exchange stability**, as for $y' = ay - y^2$ at $a = 0$ (for $a < 0$, $y = 0$ is asymptotically stable and $y = a$ unstable; for $a > 0$ the reverse).
>
> *BDP: 2.5, Problems ("Bifurcation Points"; Problems 2.5.24–26 and their notes)*

^def-8-9

> [!example] Example §8.4: Harvesting Squirrels
> In [[§8 Autonomous Differential Equations and Population Dynamics#^ex-8-3|Example §8.3]](a), hunting is permitted: a fraction $\alpha$ of the squirrel population may be eliminated every year, so
>
> $$
> \frac{dP}{dt} = 2P\Big(1 - \frac P2\Big)(P - 1) - \alpha P , \qquad \alpha \ge 0 .
> $$
>
> One association asserts that no more than $20\%$ may be eliminated ($\alpha = 0.2$), otherwise the population goes extinct; another asserts that $40\%$ ($\alpha = 0.4$) is safe. Analyze the equation as $\alpha$ varies, decide who is right, and find the largest $\alpha$ for which the population does not go extinct.
>
> **Factor.** $2P(1 - P/2)(P - 1) = P(2 - P)(P - 1) = P(-P^2 + 3P - 2)$, so
>
> $$
> f_\alpha(P) = P(-P^2 + 3P - 2 - \alpha) = -P\,(P^2 - 3P + 2 + \alpha) .
> $$
>
> **Critical points.** $P = 0$, and the roots of $P^2 - 3P + 2 + \alpha = 0$. Completing the square, $\big(P - \frac32\big)^2 = \frac94 - 2 - \alpha = \frac14 - \alpha$, so
>
> $$
> P_\pm = \frac32 \pm \sqrt{\tfrac14 - \alpha} \qquad (\alpha \le \tfrac14) .
> $$
>
> **Case $0 \le \alpha < \frac14$.** Three critical points $0 < P_- < P_+$ (note $P_- \ge 1 > 0$), and $f_\alpha(P) = -P(P - P_-)(P - P_+)$. For $0 < P < P_-$, $f_\alpha < 0$; for $P_- < P < P_+$, $f_\alpha > 0$; for $P > P_+$, $f_\alpha < 0$. So $P = 0$ is asymptotically stable, $P_-$ is an unstable threshold and $P_+$ an asymptotically stable carrying capacity. The population survives (approaches $P_+$) exactly when $P(0) > P_-$. At $\alpha = 0$ this is Example §8.3 ($P_- = 1$, $P_+ = 2$); as $\alpha$ grows the threshold rises and the carrying capacity falls.
>
> **Case $\alpha = \frac14$.** $f_{1/4}(P) = -P\big(P - \frac32\big)^2 \le 0$ for $P \ge 0$, with a double root at $\frac32$. Solutions above $\frac32$ decrease to $\frac32$, solutions below it decrease to $0$: $P = \frac32$ is semistable ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-7|Definition §8.7]]).
>
> **Case $\alpha > \frac14$.** The quadratic $P^2 - 3P + 2 + \alpha$ has discriminant $9 - 4(2 + \alpha) = 1 - 4\alpha < 0$, so it is positive for all $P$, and $f_\alpha(P) < 0$ for every $P > 0$. The only critical point is $0$: every positive solution decreases, and by [[§8 Autonomous Differential Equations and Population Dynamics#^lem-8-4|Lemma §8.4]] it tends to $0$. The population goes extinct, whatever its size.
>
> **Answer.** $\alpha = \frac14$ is a bifurcation point (a saddle–node: the threshold and the carrying capacity merge at $\frac32$ and disappear). With $\alpha = 0.2$ there are equilibria $P_\pm = 1.5 \pm \sqrt{0.05} \approx 1.276$ and $1.724$, so a population above about $1.276$ survives and settles near $1.724$. With $\alpha = 0.4 > \frac14$ the population goes extinct. So the hunters (40%) are wrong, and hunting 20% is safe as the conservationists say; but their claim that more than 20% leads to extinction is too strong. The largest rate is
>
> $$
> \alpha_{\max} = \tfrac14 = 25\% ,
> $$
>
> at which a population starting at or above $\frac32$ still survives (tending to $\frac32$); for every $\alpha > \frac14$ extinction is certain. A harvest proportional to the population, as here, is the setting of the Schaefer model of fisheries (BDP Problem 2.5.19).
>
> *Source: 331 Written HW 2, Problem 2(c)*

^ex-8-4

![[m331-8-2.svg]]
*Bifurcation diagram of [[§8 Autonomous Differential Equations and Population Dynamics#^ex-8-4|Example §8.4]]: the critical points of $P' = 2P(1 - P/2)(P - 1) - \alpha P$ against the harvesting rate $\alpha$. Solid curves are asymptotically stable, the dashed one unstable. The threshold $P_-$ and the carrying capacity $P_+$ approach each other as $\alpha$ grows and merge at the semistable point $(\frac14, \frac32)$; beyond it (shaded) only $P = 0$ is left. The rate $\alpha = 0.2$ lies to the left of the bifurcation, $\alpha = 0.4$ to the right.*
