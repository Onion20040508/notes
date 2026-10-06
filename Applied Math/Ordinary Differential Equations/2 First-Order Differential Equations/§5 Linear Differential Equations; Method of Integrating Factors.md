---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 5
bdp: "2.1"
aliases: ["BDP 2.1"]
tags: [ordinary-differential-equations, math331]
---
← [[§4 The Falling Object and the Field Mice and Owls]] · ↑ [[· 2 First-Order Differential Equations]] · [[§6 Separable Differential Equations]] →

*Boyce–DiPrima, Section 2.1 · MATH 331 Written HW 1 (Problem 2), Midterms Spring 2020 (Q4) and Summer 2023 (Q3).*

Chapter 2 studies first-order equations $dy/dt = f(t, y)$. No single method solves them all, so each section treats one class, and the most important class is the linear equations $y' + p(t)y = g(t)$. Leibniz's idea is to multiply the equation by a function $\mu(t)$, the integrating factor, chosen so that the left side becomes the derivative of the product $\mu(t)y$; then a single integration solves the equation. This gives an explicit formula for every solution, possibly with an integral that has to be left unevaluated. The formula also shows where solutions can fail to exist: only where $p$ or $g$ is discontinuous.

## First-Order Linear Equations

> [!definition] Definition §6.1: First-Order Linear Equation
> The equation $dy/dt = f(t, y)$ is a **first-order linear differential equation** if $f$ depends linearly on $y$. It is usually written in the **standard form**
>
> $$
> \frac{dy}{dt} + p(t)\,y = g(t) , \qquad (3)
> $$
>
> where $p$ and $g$ are given functions of $t$. Sometimes the form
>
> $$
> P(t)\,\frac{dy}{dt} + Q(t)\,y = G(t) \qquad (4)
> $$
>
> is more convenient; where $P(t) \ne 0$ it is converted to (3) by dividing by $P(t)$. The equations $dy/dt = -ay + b$ of [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]] are the case of constant coefficients.
>
> *BDP: 2.1 (text)*

^def-5-1

> [!remark]- Connections
> - See also: [[§70 Linear Equations#^def-70-1|Calc Def. §70.1]] (Stewart's treatment, with $x$ for $t$) and [[§70 Linear Equations#^rem-70-1|Calc Remark: A Linear Equation That Is Not Separable]].

Sometimes the left side of a linear equation is already the derivative of a product, and the equation can be integrated at once.

> [!example] Example §6.1: An Exact Derivative
> Solve $(4 + t^2)\,\dfrac{dy}{dt} + 2ty = 4t$.
>
> The left side is the combination of $dy/dt$ and $y$ that appears in the product rule:
>
> $$
> \frac{d}{dt}\big[(4 + t^2)\,y\big] = (4 + t^2)\,\frac{dy}{dt} + 2t\,y .
> $$
>
> So the equation says $\dfrac{d}{dt}\big[(4 + t^2)\,y\big] = 4t$. Even though $y$ is unknown, both sides can be integrated with respect to $t$:
>
> $$
> (4 + t^2)\,y = 2t^2 + c , \qquad y = \frac{2t^2}{4 + t^2} + \frac{c}{4 + t^2} ,
> $$
>
> where $c$ is an arbitrary constant. This is the general solution, valid for all $t$ since $4 + t^2 > 0$.
>
> *BDP: Example 2.1.1*

^ex-5-1

> [!definition] Definition §6.2: Integrating Factor
> An **integrating factor** for the linear equation (3) is a function $\mu(t)$ such that, after (3) is multiplied by $\mu(t)$, the left side
>
> $$
> \mu(t)\,\frac{dy}{dt} + p(t)\mu(t)\,y
> $$
>
> is the derivative $\dfrac{d}{dt}\big[\mu(t)\,y\big]$ of the product. By the product rule, $\frac{d}{dt}(\mu y) = \mu y' + \mu' y$, so this happens exactly when
>
> $$
> \frac{d\mu(t)}{dt} = p(t)\,\mu(t) . \qquad (29)
> $$
>
> *BDP: 2.1 (text)*

^def-5-2

## Equations with a Constant Coefficient

> [!theorem] Theorem §6.1: Integrating Factor for y′ + ay = g(t)
> Let $a$ be a constant and $g$ continuous on an interval $I$ containing $t_0$. Then $\mu(t) = e^{at}$ is an integrating factor for
>
> $$
> \frac{dy}{dt} + ay = g(t) , \qquad (20)
> $$
>
> and the solutions of (20) on $I$ are exactly the functions
>
> $$
> y = e^{-at}\int_{t_0}^{t} e^{as}g(s)\,ds + ce^{-at} , \qquad (24)
> $$
>
> $c$ an arbitrary constant. Setting $t = t_0$ shows $c = y(t_0)\,e^{at_0}$, so the choice of $t_0$ changes the value of $c$ but not the family of solutions.
>
> *BDP: 2.1, Equations (21)–(24)*

^thm-5-1

> [!proof]+ Proof
> **Finding $\mu$.** By [[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-2|Definition §5.2]] with $p(t) = a$, an integrating factor must satisfy $\mu' = a\mu$. (BDP's Example 2.1.2 does this for $a = \frac12$: what function is its own derivative up to the factor $\frac12$?) Writing it as $\frac{d}{dt}\ln|\mu| = a$ gives $\ln|\mu| = at + C$, and since the most general integrating factor is not needed, take $\mu(t) = e^{at}$. Directly: $(e^{at})' = ae^{at}$.
>
> **Integrating.** Multiply (20) by $e^{at}$:
>
> $$
> e^{at}\,\frac{dy}{dt} + ae^{at}\,y = e^{at}g(t) , \qquad\text{that is,}\qquad \frac{d}{dt}\big(e^{at}y\big) = e^{at}g(t) . \qquad (22)
> $$
>
> The function $G(t) = \int_{t_0}^{t} e^{as}g(s)\,ds$ is an antiderivative of the continuous function $e^{at}g(t)$ on $I$ (Fundamental Theorem of Calculus, [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]). If $y$ solves (20), then by (22) $e^{at}y$ and $G$ have the same derivative on the interval $I$, so they differ by a constant ([[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]]): $e^{at}y = G(t) + c$, which is (24) after multiplying by $e^{-at}$. Conversely, if $y$ is given by (24), then $e^{at}y = G + c$ has derivative $e^{at}g$, and expanding the product rule, $e^{at}(y' + ay) = e^{at}g$; dividing by $e^{at} \ne 0$ gives (20).

^pf-5-1

*Uses:* [[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-2|Def. §5.2]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC II), [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]] (equal derivatives differ by a constant)

For many simple $g$ the integral in (24) can be evaluated, as in the next example. For complicated $g$ the solution is left in the integral form (24); the variable of integration is called $s$ to distinguish it from $t$.

> [!example] Example §6.2: A Constant-Coefficient Initial Value Problem
> Solve $\dfrac{dy}{dt} = -3y + 4t - 3$, $y(0) = 5$, and describe the behavior of the solutions as $t \to \infty$.
>
> **Standard form.** $y' + 3y = 4t - 3$, so $a = 3$ and $\mu(t) = e^{3t}$.
>
> **Integrate.** $\dfrac{d}{dt}\big(e^{3t}y\big) = (4t - 3)e^{3t}$. By parts, with $u = t$ and $dv = e^{3t}dt$,
>
> $$
> \int te^{3t}\,dt = \frac13 te^{3t} - \int \frac13 e^{3t}\,dt = \frac13 te^{3t} - \frac19 e^{3t} ,
> $$
>
> so
>
> $$
> e^{3t}y = 4\Big(\frac13 te^{3t} - \frac19 e^{3t}\Big) - e^{3t} + c = \Big(\frac43 t - \frac{13}{9}\Big)e^{3t} + c ,
> \qquad
> y = \frac43 t - \frac{13}{9} + ce^{-3t} .
> $$
>
> **Check.** For $y_p = \frac43 t - \frac{13}{9}$: $y_p' = \frac43$ and $-3y_p + 4t - 3 = -4t + \frac{13}{3} + 4t - 3 = \frac43$.
>
> **Initial condition.** $y(0) = -\frac{13}{9} + c = 5$, so $c = \frac{58}{9}$ and
>
> $$
> y = \frac43 t - \frac{13}{9} + \frac{58}{9}e^{-3t} .
> $$
>
> **Behavior.** The term $ce^{-3t}$ dies out, so *every* solution approaches the line $y = \frac43 t - \frac{13}{9}$ as $t \to \infty$. Compare BDP's Example 2.1.3, $y' - 2y = 4 - t$, with general solution $y = -\frac74 + \frac12 t + ce^{2t}$: there $a = -2 < 0$, the term $ce^{2t}$ grows, and the solutions diverge from one another, with the critical initial value $y(0) = -\frac74$ ($c = 0$) separating those that grow positively from those that grow negatively.
>
> *Source: 331 Written HW 1, Problem 2*

^ex-5-2

## The General Linear Equation

> [!theorem] Theorem §6.2: Solution of a First-Order Linear Equation
> Let $p$ and $g$ be continuous on an open interval $I$ containing $t_0$. Then
>
> $$
> \mu(t) = \exp\int p(t)\,dt \qquad (30)
> $$
>
> (with any fixed antiderivative of $p$ in the exponent) is a positive integrating factor for $y' + p(t)y = g(t)$ (3), and the solutions of (3) on $I$ are exactly the functions
>
> $$
> y = \frac{1}{\mu(t)}\left(\int_{t_0}^{t} \mu(s)\,g(s)\,ds + c\right) , \qquad (33)
> $$
>
> $c$ an arbitrary constant. Two integrations are involved: one to find $\mu$ from (30) and one to find $y$ from (33).
>
> *BDP: 2.1, Equations (29)–(33)*

^thm-5-2

> [!proof]+ Proof
> **Finding $\mu$.** An integrating factor must satisfy $\mu' = p(t)\mu$ ([[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-2|Definition §5.2]], (29)). Assume temporarily that $\mu > 0$. Then $\dfrac{\mu'}{\mu} = p(t)$, that is, $\dfrac{d}{dt}\ln\mu(t) = p(t)$, so
>
> $$
> \ln\mu(t) = \int p(t)\,dt + k .
> $$
>
> Choosing $k = 0$ gives the simplest function, $\mu(t) = \exp\int p(t)\,dt$, which is indeed positive for all $t$, as assumed. (The antiderivative exists because $p$ is continuous on $I$.) Directly: if $P$ is an antiderivative of $p$ on $I$, then $\big(e^{P}\big)' = P'e^{P} = p\,e^{P}$ by the chain rule, so $\mu = e^{P}$ satisfies (29).
>
> **Integrating.** Multiplying (3) by $\mu$ and using (29),
>
> $$
> \frac{d}{dt}\big(\mu(t)\,y\big) = \mu(t)\,y' + p(t)\mu(t)\,y = \mu(t)\,g(t) . \qquad (31)
> $$
>
> The function $\mu g$ is continuous on $I$, so $G(t) = \int_{t_0}^{t} \mu(s)g(s)\,ds$ is an antiderivative of it on $I$ (Fundamental Theorem of Calculus). If $y$ is a solution on $I$, then $\mu y$ and $G$ have the same derivative on the interval $I$, hence differ by a constant: $\mu y = G + c$ (BDP's (32)), and dividing by $\mu > 0$ gives (33). Conversely, if $y$ is given by (33), then $(\mu y)' = G' = \mu g$; expanding the left side with the product rule and (29) gives $\mu(y' + py) = \mu g$, and dividing by $\mu$ shows that $y$ solves (3) on $I$.

^pf-5-2

*Uses:* [[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-1|Def. §5.1]], [[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-2|Def. §5.2]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC II), [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]] (equal derivatives differ by a constant)

> [!remark]- Connections
> - Rigorous ingredients: the antiderivative $\int_{t_0}^t \mu g\,ds$ of a continuous function is [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC II), and "same derivative on an interval implies they differ by a constant" is [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]]. The integrating factor itself appears in 451 as a trick for Rolle's Theorem: [[§29 The Mean Value Theorem#^rem-29-2|451 Remark after Ex. §29.4]].
> - See also: [[§70 Linear Equations#^thm-70-1|Calc Thm. §70.1]] (Stewart's treatment, $I(x) = e^{\int P\,dx}$, with the integrating factor [[§70 Linear Equations#^def-70-2|Calc Def. §70.2]]; [[§70 Linear Equations#^ex-70-3|Calc Ex. §70.3]] leaves a non-elementary integral unevaluated, as in [[§5 Linear Differential Equations; Method of Integrating Factors#^ex-5-4|Example §5.4]]). With the initial condition $y(t_0) = y_0$, (33) gives the unique solution of the initial value problem on all of $I$: this is Theorem 2.4.1, [[§8 Differences Between Linear and Nonlinear Differential Equations#^thm-8-1|Theorem §8.1]].

> [!remark] Remark: Method — Integrating Factors
> To solve a first-order linear equation:
> 1. **Standard form.** Divide by the coefficient of $y'$ to get $y' + p(t)y = g(t)$. Reading off $p$ and $g$ before this step is the most common error.
> 2. **Integrating factor.** Compute $\mu(t) = e^{\int p(t)\,dt}$; no constant of integration is needed. Simplify: $e^{2\ln|t|} = t^2$, $e^{\ln(100 + t)} = 100 + t$.
> 3. **Multiply and recognize.** Multiply the standard form by $\mu$; the left side is $(\mu y)'$. (Check by the product rule.)
> 4. **Integrate.** $\mu y = \int \mu g\,dt + c$. Do not forget the constant, and if the integral is not elementary, write it as $\int_{t_0}^{t} \mu(s)g(s)\,ds$ with a convenient $t_0$, usually the initial point.
> 5. **Solve for $y$** and impose the initial condition. The solution of an initial value problem lives on the largest interval containing $t_0$ on which $p$ and $g$ are continuous.

^rem-5-1

> [!example] Example §6.3: Coefficients with a Singularity
> **(a)** Solve the initial value problem $ty' + 2y = 4t^2$, $y(1) = 2$.
>
> **Standard form.** Divide by $t$: $y' + \dfrac2t\,y = 4t$, so $p(t) = 2/t$ and $g(t) = 4t$. Here $p$ has an infinite discontinuity at $t = 0$.
>
> **Integrating factor.** $\mu(t) = \exp\displaystyle\int \frac2t\,dt = e^{2\ln|t|} = t^2$.
>
> **Integrate.** $t^2y' + 2ty = (t^2y)' = 4t^3$, so $t^2y = t^4 + c$ and, for $t > 0$,
>
> $$
> y = t^2 + \frac{c}{t^2} . \qquad (37)
> $$
>
> **Initial condition.** $2 = 1 + c$, so $c = 1$ and
>
> $$
> y = t^2 + \frac{1}{t^2} , \qquad t > 0 . \qquad (38)
> $$
>
> **Interval.** The solution becomes unbounded as $t \to 0^+$, asymptotic to the positive $y$-axis: this is the effect of the discontinuity of $p$ at $0$. The function $t^2 + 1/t^2$ for $t < 0$ is part of the general solution of the equation, but *not* part of the solution of this initial value problem, which exists only on $0 < t < \infty$. It is the first example in which a solution fails to exist for some values of $t$.
>
> **A critical initial value.** For $y(1) = y_0$, $c = y_0 - 1$ and $y = t^2 + (y_0 - 1)/t^2$. Solutions with $y_0 > 1$ go to $+\infty$ and those with $y_0 < 1$ go to $-\infty$ as $t \to 0^+$. Only $y_0 = 1$ ($c = 0$) gives $y = t^2$, which stays bounded and differentiable even at $t = 0$.
>
> **(b)** Solve the initial value problem $t^5y' = -4t^4y + 2t^2$, $y(1) = 6$.
>
> **Standard form.** Move the $y$ term to the left and divide by $t^5$ (for $t \ne 0$): $y' + \dfrac4t\,y = \dfrac{2}{t^3}$, so $p(t) = 4/t$ and $g(t) = 2/t^3$. Both are discontinuous at $t = 0$ and continuous elsewhere; the initial point is $t = 1$, so the solution lives on $t > 0$.
>
> **Integrating factor.** $\mu(t) = \exp\displaystyle\int \frac4t\,dt = e^{4\ln|t|} = t^4$.
>
> **Integrate.** $(t^4y)' = t^4 \cdot \dfrac{2}{t^3} = 2t$, so $t^4y = t^2 + c$ and
>
> $$
> y = \frac{1}{t^2} + \frac{c}{t^4} .
> $$
>
> **Initial condition.** $y(1) = 1 + c = 6$, so $c = 5$ and
>
> $$
> y = \frac{1}{t^2} + \frac{5}{t^4} , \qquad t > 0 .
> $$
>
> **Check.** $y' = -\dfrac{2}{t^3} - \dfrac{20}{t^5}$, so $t^5y' = -2t^2 - 20$, while $-4t^4y + 2t^2 = -4t^2 - 20 + 2t^2 = -2t^2 - 20$.
>
> **No critical value here.** As $t \to 0^+$ every solution $1/t^2 + c/t^4$ is unbounded: $c/t^4$ dominates when $c \ne 0$, and $c = 0$ still leaves $1/t^2$. In (a) the forcing $g(t) = 4t$ was continuous at $0$ and one solution survived there; in (b) $g$ itself blows up at $0$, and no solution extends to $t \le 0$.
>
> *BDP: Example 2.1.4*
> *Source: 331 Midterm (Summer 2023), Q3*

^ex-5-3

![[m331-4-1.svg]]
*Integral curves $y = t^2 + c/t^2$ of $ty' + 2y = 4t^2$ (blue, $c = 2, 0.5, 0.2, -0.2, -0.5, -1$). The solution of the initial value problem $y(1) = 2$ (green, $c = 1$) lives on $t > 0$ only; the curve $t^2 + 1/t^2$ for $t < 0$ (pale green) belongs to the same formula but not to the solution. The critical solution $y = t^2$ (red, $c = 0$) separates the curves that blow up to $+\infty$ at $t = 0$ from those that go to $-\infty$, and is the only one that crosses $t = 0$.*

> [!example] Example §6.4: Leaving the Integral Unevaluated
> Solve the initial value problem $2y' + ty = 2$, $y(0) = 1$.
>
> **Standard form.** $y' + \dfrac t2\,y = 1$, so $p(t) = t/2$ and $\mu(t) = e^{t^2/4}$.
>
> **Integrate.** $\big(e^{t^2/4}y\big)' = e^{t^2/4}$. The function $e^{t^2/4}$ has no elementary antiderivative, so take the lower limit at the initial point $t = 0$:
>
> $$
> e^{t^2/4}y = \int_0^t e^{s^2/4}\,ds + c , \qquad
> y = e^{-t^2/4}\int_0^t e^{s^2/4}\,ds + ce^{-t^2/4} . \qquad (47)
> $$
>
> **Initial condition.** At $t = 0$ the integral is over $[0, 0]$, so $1 = 0 + c$ and $c = 1$:
>
> $$
> y = e^{-t^2/4}\int_0^t e^{s^2/4}\,ds + e^{-t^2/4} .
> $$
>
> This is a perfectly good answer: for each $t$ the integral is a definite integral that numerical integration evaluates to any accuracy, so the solution can be tabulated and plotted. Plots suggest that all solutions approach a common limit as $t \to \infty$. (BDP leaves it to Problem 22; the limit is $0$: $ce^{-t^2/4} \to 0$, and by L'Hôpital's rule ([[§31 Indeterminate Forms and L'Hospital's Rule#^thm-31-2|Calc Thm. §31.2]]) $\dfrac{\int_0^t e^{s^2/4}ds}{e^{t^2/4}}$ has the same limit as $\dfrac{e^{t^2/4}}{(t/2)e^{t^2/4}} = \dfrac2t \to 0$.)
>
> *BDP: Example 2.1.5*

^ex-5-4

> [!example] Example §6.5: A Second-Order Equation Reduced to a Linear One
> Find the solutions $y(t)$ of $y'' + \dfrac{y'}{t} = 3 + t$ by the substitution $v(t) = y'(t)$. (The solutions involve two unknown constants.)
>
> **Substitute.** With $v = y'$, $v' = y''$, and the equation becomes the first-order linear equation
>
> $$
> v' + \frac1t\,v = 3 + t .
> $$
>
> **Integrating factor.** $\mu = e^{\int dt/t} = e^{\ln|t|} = |t|$; on $t > 0$, $\mu = t$.
>
> **Integrate.** $(tv)' = (3 + t)t = 3t + t^2$, so
>
> $$
> tv = \frac32 t^2 + \frac13 t^3 + C_1 , \qquad v = \frac32 t + \frac13 t^2 + \frac{C_1}{t} .
> $$
>
> **Integrate again.** $y = \displaystyle\int v\,dt = \frac34 t^2 + \frac19 t^3 + C_1\ln t + C_2$, for $t > 0$.
>
> **Check.** $y' = \frac32 t + \frac13 t^2 + \frac{C_1}{t}$, $y'' = \frac32 + \frac23 t - \frac{C_1}{t^2}$, and $y'' + \frac{y'}{t} = \frac32 + \frac23 t - \frac{C_1}{t^2} + \frac32 + \frac13 t + \frac{C_1}{t^2} = 3 + t$.
>
> The trick works because $y$ itself does not appear in the equation; it reappears for second-order equations in reduction of order, [[§20 Repeated Roots; Reduction of Order#^prop-20-3|Proposition §20.3]].
>
> *Source: 331 Midterm (Spring 2020), Q4*

^ex-5-5
