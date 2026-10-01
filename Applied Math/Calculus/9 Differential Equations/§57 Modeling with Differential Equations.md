---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 57
stewart: "9.1"
aliases: ["Stewart 9.1"]
tags: [calculus]
---
← [[§56 Probability]] · ↑ [[· 9 Differential Equations]] · [[§58 Direction Fields and Euler's Method]] →

*Stewart, Section 9.1.*

A mathematical model of a real-world process often takes the form of a differential equation: an equation that contains an unknown function and some of its derivatives. This is natural, because we usually observe how a quantity *changes* and want to predict its future values from that. The section builds three models (exponential population growth, the logistic equation with a carrying capacity, and the vibrating spring) and reads off what their solutions must look like before solving anything. Then it fixes the general vocabulary: order, solution, general solution, initial condition and initial-value problem.

## Models for Population Growth

Under ideal conditions (unlimited environment, adequate nutrition, no predators, immunity from disease), a population of bacteria or animals grows at a rate proportional to its size. The variables are $t$, time (the independent variable), and $P$, the number of individuals in the population (the dependent variable). The rate of growth is the derivative $dP/dt$.

> [!definition] Definition §57.1: The Exponential Growth Model
> The assumption that the rate of growth of a population is proportional to the population size is the differential equation
>
> $$
> \frac{dP}{dt} = kP ,
> $$
>
> where $k$ is the proportionality constant. It is a differential equation because it contains an unknown function $P$ and its derivative $dP/dt$. (It is the law of natural growth of [[§21 Exponential Growth and Decay#^def-21-1|Definition §21.1]]; Section 9.4 returns to it in [[§60 Models for Population Growth#^def-60-1|Definition §60.1]].)
>
> *Stewart: 9.1, Equation 1*

^def-57-1

> [!remark] Remark: Consequences Before Solving
> If we rule out a population of $0$, then $P(t) > 0$ for all $t$. So if $k > 0$, the equation shows that $P'(t) = kP(t) > 0$ for all $t$: the population is always increasing. Moreover, as $P(t)$ increases, $dP/dt = kP$ becomes larger: the growth rate increases as the population increases.

^rem-57-1

> [!theorem] Proposition §57.1: Exponential Functions Solve the Growth Equation
> For every constant $C$, the function $P(t) = Ce^{kt}$ is a solution of $dP/dt = kP$. The constant is the initial population: $C = P(0)$.
>
> *Stewart: 9.1 (text)*

^prop-57-1

> [!proof]+ Proof
> The equation asks for a function whose derivative is a constant multiple of itself, and exponential functions have that property ([[§17 The Chain Rule#^cor-17-4|Corollary §17.4]]):
>
> $$
> P'(t) = C\big(ke^{kt}\big) = k\big(Ce^{kt}\big) = kP(t) .
> $$
>
> Putting $t = 0$ gives $P(0) = Ce^{k \cdot 0} = C$.

^pf-57-1

*Uses:* [[§57 Modeling with Differential Equations#^def-57-1|Def. §57.1]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|§14.6]], [[§17 The Chain Rule#^cor-17-4|§17.4]]

*There are no other solutions: this is [[§21 Exponential Growth and Decay#^thm-21-1|Theorem §21.1]] (Stewart 3.8, Theorem 2), proved there; Stewart proves it in Section 9.4 ([[§60 Models for Population Growth#^thm-60-1|Theorem §60.1]]).*

> [!remark]- Connections
> - Uniqueness in one line: if $P' = kP$, then $\big(P(t)e^{-kt}\big)' = (P' - kP)e^{-kt} = 0$, so $P(t)e^{-kt}$ is constant by [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (vanishing derivative means constant). This is the argument of the proof of [[§21 Exponential Growth and Decay#^thm-21-1|Theorem §21.1]]. The multiplier $e^{-kt}$ is the integrating factor of [[§29 The Mean Value Theorem#^rem-29-2|451 Remark after Ex. §29.4]] and of [[§61 Linear Equations#^def-61-2|Definition §61.2]].

> [!remark] Remark: The Family of Solutions
> Letting $C$ vary through all the real numbers gives the *family* of solutions $P(t) = Ce^{kt}$. For $k > 0$ the graphs with $C > 0$ rise ever more steeply, those with $C < 0$ fall ever more steeply, and $C = 0$ gives the zero function. Populations have only positive values, so only the solutions with $C > 0$ are physically meaningful, and if we care only about times after the initial time $t = 0$, only their parts with $t \ge 0$.

^rem-57-2

Equation 1 is appropriate under ideal conditions, but a more realistic model must reflect that a given environment has limited resources. Many populations start by increasing exponentially, but the population levels off when it approaches its **carrying capacity** $M$ (or decreases toward $M$ if it ever exceeds $M$). A model that takes both trends into account should satisfy

$$
\frac{dP}{dt} \approx kP \quad \text{if } P \text{ is small (initially the growth rate is proportional to } P\text{)},
\qquad
\frac{dP}{dt} < 0 \quad \text{if } P > M \quad (P \text{ decreases if it ever exceeds } M) .
$$

> [!definition] Definition §57.2: The Logistic Differential Equation
> Assume that the rate of population growth is proportional to both the population and the difference between the carrying capacity $M$ and the population: $dP/dt = cP(M - P)$, where $c$ is the proportionality constant. Equivalently, with $k = cM$,
>
> $$
> \frac{dP}{dt} = kP\Big(1 - \frac{P}{M}\Big) .
> $$
>
> This is the **logistic differential equation**, proposed by the Dutch mathematical biologist Pierre-François Verhulst in the 1840s as a model for world population growth (solved explicitly in [[§60 Models for Population Growth#^thm-60-2|Theorem §60.2]]). It has both required properties: if $P$ is small compared with $M$, then $P/M$ is close to $0$ and $dP/dt \approx kP$; if $P > M$, then $1 - P/M < 0$ and $dP/dt < 0$.
>
> *Stewart: 9.1, Equation 2*

^def-57-2

> [!definition] Definition §57.3: Equilibrium Solution
> A constant function that is a solution of a differential equation is an **equilibrium solution**. Its graph is a horizontal line.
>
> *Stewart: 9.1 (text)*

^def-57-3

> [!theorem] Proposition §57.2: Qualitative Behaviour of Logistic Solutions
> Let $k > 0$ and $M > 0$, and let $P$ be a solution of the logistic equation (Definition §57.2).
> 1. The constant functions $P(t) = 0$ and $P(t) = M$ are equilibrium solutions.
> 2. If $0 < P(t) < M$, then $dP/dt > 0$: the population increases.
> 3. If $P(t) > M$, then $dP/dt < 0$: the population decreases.
> 4. In either case, if $P \to M$, then $dP/dt \to 0$: the population levels off.
>
> So the solution curves move away from the equilibrium solution $P = 0$ and toward the equilibrium solution $P = M$.
>
> *Stewart: 9.1 (text)*

^prop-57-2

> [!proof]+ Proof
> Everything is read off from the sign of the right side $kP(1 - P/M)$, a product of the positive constant $k$ and the two factors $P$ and $1 - P/M$.
> 1. If $P(t) = 0$ for all $t$, both sides of the equation are $0$, since the left side is the derivative of a constant and the factor $P$ on the right is $0$. If $P(t) = M$, the left side is again $0$ and the factor $1 - P/M$ on the right is $0$. Both are constant solutions, hence equilibrium solutions (Definition §57.3). Physically: a population that is ever $0$ or at the carrying capacity stays that way.
> 2. If $0 < P < M$, then $P > 0$ and $1 - P/M > 0$, so $dP/dt > 0$.
> 3. If $P > M$, then $P > 0$ but $1 - P/M < 0$, so $dP/dt < 0$.
> 4. The right side is a continuous function of $P$ that vanishes at $P = M$, so $dP/dt = kP(1 - P/M) \to kM(1 - 1) = 0$ as $P \to M$.

^pf-57-2

*Uses:* [[§57 Modeling with Differential Equations#^def-57-2|Def. §57.2]], [[§57 Modeling with Differential Equations#^def-57-3|Def. §57.3]]

![[m233-57-1.svg]]
*Solutions of the logistic equation. The equilibrium solutions $P = 0$ and $P = M$ (red) are horizontal lines. Solutions starting between them (blue) increase and level off at $M$: they look exponential at first, when $P$ is small, and flatten as $P \to M$. Solutions starting above $M$ (green) decrease toward $M$. (The curves are the explicit solutions found in Section 9.4, [[§60 Models for Population Growth#^thm-60-2|Theorem §60.2]].)*

## A Model for the Motion of a Spring

Consider an object with mass $m$ at the end of a vertical spring, and let $x(t)$ be its displacement from the equilibrium position at time $t$. By Hooke's Law ([[§42 Work#^def-42-4|Definition §42.4]]), if the spring is stretched (or compressed) $x$ units from its natural length, it exerts the restoring force $-kx$, where $k > 0$ is the *spring constant*.

> [!definition] Definition §57.4: The Spring Equation
> If we ignore any external resisting forces (air resistance, friction), Newton's Second Law (force equals mass times acceleration) gives
>
> $$
> m\,\frac{d^2x}{dt^2} = -kx .
> $$
>
> This is a *second-order* differential equation, because it involves second derivatives (Definition §57.5).
>
> *Stewart: 9.1, Equation 3*

^def-57-4

> [!theorem] Proposition §57.3: Sines and Cosines Solve the Spring Equation
> Let $\omega = \sqrt{k/m}$. For all constants $A$ and $B$, the function
>
> $$
> x(t) = A\sin\omega t + B\cos\omega t
> $$
>
> is a solution of the spring equation, and all solutions of the spring equation can be written in this form.
>
> *Stewart: 9.1 (text; Exercise 16)*

^prop-57-3

> [!proof]+ Proof
> Rewrite the equation as $\dfrac{d^2x}{dt^2} = -\dfrac{k}{m}\,x = -\omega^2 x$: the second derivative of $x$ is proportional to $x$ but has the opposite sign. Sine and cosine have this property ([[§16 Derivatives of Trigonometric Functions#^thm-16-1|Theorems §16.1]] and [[§16 Derivatives of Trigonometric Functions#^thm-16-2|§16.2]] with the [[§17 The Chain Rule#^thm-17-2|Chain Rule]]):
>
> $$
> x'(t) = A\omega\cos\omega t - B\omega\sin\omega t, \qquad x''(t) = -A\omega^2\sin\omega t - B\omega^2\cos\omega t = -\omega^2 x(t) .
> $$
>
> So $x$ is a solution. This is not surprising: we expect the spring to oscillate about its equilibrium position, so trigonometric functions should be involved.

^pf-57-3

*Uses:* [[§57 Modeling with Differential Equations#^def-57-4|Def. §57.4]], [[§16 Derivatives of Trigonometric Functions#^thm-16-1|§16.1]], [[§16 Derivatives of Trigonometric Functions#^thm-16-2|§16.2]], [[§17 The Chain Rule#^thm-17-2|§17.2]]

*That there are no other solutions is stated by Stewart without proof ("it turns out that"); it belongs to the theory of second-order linear equations, and no note in the vault proves it.*

## General Differential Equations

> [!definition] Definition §57.5: Differential Equation and Order
> A **differential equation** is an equation that contains an unknown function and one or more of its derivatives (first met in [[§33 Antiderivatives#^def-33-2|Definition §33.2]]). The **order** of a differential equation is the order of the highest derivative that occurs in the equation.
>
> Thus the growth and logistic equations (Definitions §57.1, §57.2) are first-order equations and the spring equation (Definition §57.4) is a second-order equation. The independent variable need not be time: in
>
> $$
> y' = xy
> $$
>
> it is understood that $y$ is an unknown function of $x$.
>
> *Stewart: 9.1 (text; Equation 4)*

^def-57-5

> [!definition] Definition §57.6: Solution and General Solution
> A function $f$ is a **solution** of a differential equation if the equation is satisfied when $y = f(x)$ and its derivatives are substituted into the equation. For example, $f$ is a solution of $y' = xy$ if
>
> $$
> f'(x) = xf(x)
> $$
>
> for all values of $x$ in some interval. To **solve** a differential equation means to find *all* possible solutions. The family of all solutions, usually written with an arbitrary constant, is the **general solution**.
>
> The simplest case is $y' = f(x)$, whose solutions are the antiderivatives of $f$ ([[§33 Antiderivatives#^thm-33-1|Theorem §33.1]]). For instance, the general solution of $y' = x^3$ is
>
> $$
> y = \frac{x^4}{4} + C ,
> $$
>
> where $C$ is an arbitrary constant. In general, solving a differential equation is not an easy matter: there is no systematic technique that solves all differential equations. Section 9.2 ([[§58 Direction Fields and Euler's Method|§58]]) shows how to sketch solutions and compute numerical approximations to them even without an explicit formula.
>
> *Stewart: 9.1 (text)*

^def-57-6

> [!remark]- Connections
> - That $x^4/4 + C$ gives *all* solutions of $y' = x^3$ (on an interval) is the fact that two functions with the same derivative differ by a constant: [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]], proved from the Mean Value Theorem; in this course, [[§26 The Mean Value Theorem#^cor-26-4|Corollary §26.4]].

> [!remark] Remark: Method — Checking a Proposed Solution
> 1. Compute the derivatives of the proposed function that occur in the equation.
> 2. Substitute them into the left side and into the right side *separately*, and simplify each side.
> 3. The function is a solution if the two sides agree for all $x$ in an interval. A single value of $x$ where they differ shows that it is not.
> 4. For a family with a constant $c$, carry $c$ through the computation: if the sides agree for every $c$, every member of the family is a solution.

^rem-57-3

> [!example] Example §57.1: Is It a Solution?
> Determine whether the function $y = x + 1/x$ is a solution of the given differential equation.
> (a) $xy' + y = 2x$ (b) $xy'' + 2y' = 0$
>
> The first and second derivatives (with respect to $x$) are
>
> $$
> y' = 1 - \frac{1}{x^2}, \qquad y'' = \frac{2}{x^3} .
> $$
>
> **(a)** The left side of the equation is
>
> $$
> xy' + y = x\Big(1 - \frac{1}{x^2}\Big) + \Big(x + \frac1x\Big) = x - \frac1x + x + \frac1x = 2x ,
> $$
>
> which equals the right side. So $y = x + 1/x$ is a solution (on $(0, \infty)$ and on $(-\infty, 0)$).
>
> **(b)** The left side is
>
> $$
> xy'' + 2y' = x\Big(\frac{2}{x^3}\Big) + 2\Big(1 - \frac{1}{x^2}\Big) = \frac{2}{x^2} + 2 - \frac{2}{x^2} = 2 ,
> $$
>
> which is not equal to the right side $0$. So $y = x + 1/x$ is not a solution.
>
> *Stewart: Example 9.1.1*

^ex-57-1

> [!example] Example §57.2: A Family of Solutions
> Show that every member of the family of functions
>
> $$
> y = \frac{1 + ce^t}{1 - ce^t}
> $$
>
> is a solution of the differential equation $y' = \frac12(y^2 - 1)$.
>
> **Left side.** By the Quotient Rule ([[§15 The Product and Quotient Rules#^thm-15-2|Theorem §15.2]]),
>
> $$
> y' = \frac{(1 - ce^t)(ce^t) - (1 + ce^t)(-ce^t)}{(1 - ce^t)^2} = \frac{ce^t - c^2e^{2t} + ce^t + c^2e^{2t}}{(1 - ce^t)^2} = \frac{2ce^t}{(1 - ce^t)^2} .
> $$
>
> **Right side.**
>
> $$
> \frac12(y^2 - 1) = \frac12\Big[\Big(\frac{1 + ce^t}{1 - ce^t}\Big)^2 - 1\Big] = \frac12 \cdot \frac{(1 + ce^t)^2 - (1 - ce^t)^2}{(1 - ce^t)^2} = \frac12 \cdot \frac{4ce^t}{(1 - ce^t)^2} = \frac{2ce^t}{(1 - ce^t)^2} .
> $$
>
> The two sides are equal, so for every value of $c$ the function is a solution (on each interval where $ce^t \ne 1$).
>
> The equation itself predicts the shape of the graphs: if $y \approx \pm 1$, then $y' \approx 0$, so the graphs are flat near $y = 1$ and $y = -1$. Indeed $c = 0$ gives the equilibrium solution $y = 1$. The other equilibrium solution $y = -1$ is *not* a member of the family for any $c$ (it is the limit as $c \to \pm\infty$), so the family is not quite the general solution.
>
> *Stewart: Example 9.1.2*

^ex-57-2

> [!definition] Definition §57.7: Initial Condition and Initial-Value Problem
> In applications we usually want not the general solution but the particular solution that satisfies a condition of the form
>
> $$
> y(t_0) = y_0 .
> $$
>
> This is an **initial condition**, and the problem of finding a solution of the differential equation that satisfies the initial condition is an **initial-value problem**. Geometrically, we pick out of the family of solution curves the one that passes through the point $(t_0, y_0)$. Physically, we measure the state of a system at time $t_0$ and use the solution of the initial-value problem to predict its future behaviour.
>
> *Stewart: 9.1 (text)*

^def-57-7

> [!example] Example §57.3: An Initial-Value Problem
> Find a solution of the differential equation $y' = \frac12(y^2 - 1)$ that satisfies the initial condition $y(0) = 2$.
>
> By Example §57.2, $y = \dfrac{1 + ce^t}{1 - ce^t}$ is a solution for every value of $c$. Substituting $t = 0$ and $y = 2$:
>
> $$
> 2 = \frac{1 + ce^0}{1 - ce^0} = \frac{1 + c}{1 - c} .
> $$
>
> So $2 - 2c = 1 + c$, which gives $c = \frac13$. The solution of the initial-value problem is
>
> $$
> y = \frac{1 + \frac13 e^t}{1 - \frac13 e^t} = \frac{3 + e^t}{3 - e^t} .
> $$
>
> Its graph is the one member of the family of Example §57.2 that passes through the point $(0, 2)$. The denominator vanishes at $t = \ln 3$, so as a solution of the initial-value problem it lives on the interval $(-\infty, \ln 3)$ containing $t_0 = 0$, and $y \to \infty$ as $t \to (\ln 3)^-$.
>
> *Stewart: Example 9.1.3*

^ex-57-3

![[m233-57-2.svg]]
*Members of the family $y = (1 + ce^t)/(1 - ce^t)$ of Example §57.2 (blue): $c < 0$ gives curves falling from $y = 1$ to $y = -1$, $c = 0$ the line $y = 1$, and $c > 0$ curves with a vertical asymptote at $t = -\ln c$. The initial condition $y(0) = 2$ selects $c = \frac13$ (red, Example §57.3): of its two branches, only the one through $(0, 2)$, on $(-\infty, \ln 3)$, solves the initial-value problem.*
