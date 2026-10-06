---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 1
section: 2
bdp: "1.2"
aliases: ["BDP 1.2"]
tags: [ordinary-differential-equations, math331]
---
← [[§1 Some Basic Mathematical Models; Direction Fields]] · ↑ [[· 1 Introduction to Differential Equations]] · [[§3 Classification of Differential Equations]] →

*Boyce–DiPrima, Section 1.2.*

Both models of [[§1 Some Basic Mathematical Models; Direction Fields|§1]] have the form $dy/dt = ay - b$ with constants $a$ and $b$. This section solves that equation by direct integration. The solution brings in an arbitrary constant, so a differential equation has a whole family of solutions, the general solution; an initial condition picks out one member. The explicit formula confirms what the direction fields suggested: the coefficient $a$ decides whether solutions approach the equilibrium $b/a$ or run away from it. For the falling object it also answers quantitative questions, such as when and how fast an object dropped from 300 m hits the ground.

## Solving dy/dt = ay − b

> [!example] Example §2.1: Field Mice and Owls, Solved
> Find the solutions of
>
> $$
> \frac{dp}{dt} = 0.5p - 450 \qquad (4)
> $$
>
> (equation (8) of [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-3|Example §1.3]]), and the solution with $p(0) = 850$.
>
> **Separate.** Write the equation as $\dfrac{dp}{dt} = \dfrac{p - 900}{2}$. If $p \ne 900$,
>
> $$
> \frac{dp/dt}{p - 900} = \frac12 .
> $$
>
> By the chain rule the left side is $\dfrac{d}{dt}\ln|p - 900|$, so integrating both sides gives
>
> $$
> \ln|p - 900| = \frac{t}{2} + C , \qquad |p - 900| = e^{C}e^{t/2}, \qquad p - 900 = \pm e^{C}e^{t/2} .
> $$
>
> **The family.** Writing $c = \pm e^{C}$,
>
> $$
> p = 900 + ce^{t/2} . \qquad (11)
> $$
>
> Here $c$ is an arbitrary nonzero constant. The equilibrium solution $p = 900$, excluded when we divided by $p - 900$, is the member $c = 0$. So (11), with $c$ arbitrary, lists the solutions found; for $c \ne 0$ they diverge from $p = 900$, as the direction field showed.
>
> **The initial condition.** $p(0) = 850$ requires the graph to pass through $(0, 850)$: $850 = 900 + c$, so $c = -50$ and
>
> $$
> p = 900 - 50e^{t/2} . \qquad (13)
> $$
>
> This population decreases and reaches $0$ when $e^{t/2} = 18$, that is, at $t = 2\ln 18 \approx 5.78$ months: the mice die out in finite time.
>
> *BDP: Example 1.2.1*

^ex-2-1

> [!definition] Definition §2.1: Initial Condition; Initial Value Problem
> A condition $y(t_0) = y_0$ that prescribes the value of the solution at one time, such as $p(0) = 850$, is an **initial condition**. A differential equation together with an initial condition is an **initial value problem**. Geometrically, the initial condition requires the graph of the solution to pass through the point $(t_0, y_0)$.
>
> *BDP: 1.2 (text)*

^def-2-1

> [!theorem] Theorem §2.1: Solution of dy/dt = ay − b
> Let $a \ne 0$ and $b$ be constants. Every solution of
>
> $$
> \frac{dy}{dt} = ay - b \qquad (3)
> $$
>
> on an interval has the form
>
> $$
> y(t) = \frac{b}{a} + ce^{at} \qquad (17)
> $$
>
> for a constant $c$, and each such function is a solution for all $t$. The solution of the initial value problem (3), $y(0) = y_0$, is
>
> $$
> y(t) = \frac{b}{a} + \Big(y_0 - \frac{b}{a}\Big)e^{at} . \qquad (18)
> $$
>
> The member $c = 0$ is the equilibrium solution $y = b/a$. If $a = 0$, the solutions are instead $y(t) = -bt + c$.
>
> *BDP: 1.2, Equations (17) and (18) (text and footnote 3)*

^thm-2-1

> [!proof]+ Proof
> **BDP's derivation.** Let $y$ be a solution with $y(t) \ne b/a$ on an interval. Then (3) can be written as
>
> $$
> \frac{dy/dt}{y - (b/a)} = a , \qquad (15)
> $$
>
> since $ay - b = a\,(y - b/a)$. By the chain rule the left side is $\dfrac{d}{dt}\ln\big|y(t) - \tfrac{b}{a}\big|$, so integrating gives
>
> $$
> \ln\Big|y(t) - \frac{b}{a}\Big| = at + C , \qquad (16)
> $$
>
> and exponentiating, $y(t) - b/a = \pm e^{C}e^{at}$, which is (17) with $c = \pm e^{C} \ne 0$.
>
> **Every solution has this form.** BDP asserts that (17) contains all solutions; here is why. The derivation above divided by $y - b/a$, which is not allowed at points where $y(t) = b/a$, and the sign $\pm$ could a priori change. Instead, let $y$ be any solution on an interval $I$ and put $u(t) = \big(y(t) - \tfrac{b}{a}\big)e^{-at}$. By the product rule and (3),
>
> $$
> u'(t) = y'(t)e^{-at} - a\Big(y(t) - \frac{b}{a}\Big)e^{-at} = \big(ay - b - ay + b\big)e^{-at} = 0 .
> $$
>
> A function with zero derivative on an interval is constant, so $u(t) = c$ and $y(t) = b/a + ce^{at}$ on $I$. In particular a solution that equals $b/a$ at one point has $c = 0$ and is the equilibrium solution. (The multiplier $e^{-at}$ is the integrating factor of [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-1|Theorem §4.1]], applied to $y' - ay = -b$.)
>
> **Each such function is a solution.** If $y = b/a + ce^{at}$, then $y' = ace^{at} = a\big(y - \tfrac{b}{a}\big) = ay - b$ for all $t$.
>
> **The initial value problem.** Setting $t = 0$ in (17) gives $y_0 = b/a + c$, so $c = y_0 - b/a$, which is (18).
>
> **The case $a = 0$.** Then (3) reads $y' = -b$, whose solutions on an interval are exactly $y = -bt + c$ (two functions with the same derivative differ by a constant).

^pf-2-1

*Uses:* [[§2 Solutions of Some Differential Equations#^def-2-1|Def. §2.1]], [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (zero derivative on an interval), [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]] (equal derivatives)

> [!remark]- Connections
> - The step "zero derivative on an interval implies constant": [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]], from the Mean Value Theorem; equal derivatives differ by a constant, [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]].
> - See also: [[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]] (the case $b = 0$, proved the same way) and [[§60 Models for Population Growth#^thm-60-1|Calc Thm. §60.1]] (Stewart's separation-of-variables derivation). Stewart's [[§60 Models for Population Growth#^rem-60-1|Calc Remark: Emigration]], $dP/dt = kP - m$, is (3) with $a = k$, $b = m$: the mice and owls of [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-3|Example §1.3]].

> [!definition] Definition §2.2: General Solution
> For $a \ne 0$, the expression (17), which contains all possible solutions of (3), is called the **general solution** of (3).
>
> *BDP: 1.2 (text)*

^def-2-2

> [!remark]- Connections
> - See also: [[§57 Modeling with Differential Equations#^def-57-6|Calc Def. §57.6]] (solution and general solution) and [[§57 Modeling with Differential Equations#^def-57-7|Calc Def. §57.7]] (initial condition, initial-value problem), Stewart's versions of [[§2 Solutions of Some Differential Equations#^def-2-1|Definitions §2.1]] and [[§2 Solutions of Some Differential Equations#^def-2-2|§2.2]].

> [!definition] Definition §2.2: Integral Curves
> Let (17) be the general solution of (3) ([[§2 Solutions of Some Differential Equations#^def-2-2|Definition §2.2]]). Its geometric representation, the infinite family of graphs of (17), one for each value of $c$, is the family of **integral curves** of the equation. Satisfying an initial condition amounts to picking out the integral curve through the given initial point.
>
> *BDP: 1.2 (text)*

^def-2-new1

> [!remark] Remark: What the Formula Says About the Two Models
> **Field mice.** With $a = r > 0$ and $b = k > 0$, (18) becomes
>
> $$
> p(t) = \frac{k}{r} + \Big(p_0 - \frac{k}{r}\Big)e^{rt} , \qquad (19)
> $$
>
> where $p_0$ is the initial population. If $p_0 = k/r$, then $p(t) = k/r$ for all $t$. Otherwise the sign of $p_0 - k/r$ decides everything: if $p_0 > k/r$ the population grows exponentially, and if $p_0 < k/r$ it decreases and reaches $0$ at a finite time (extinction). Negative values of (19) are meaningless for a population.
>
> **Falling object.** Writing $m\,dv/dt = mg - \gamma v$ as $dv/dt = -(\gamma/m)v + g$ means $a = -\gamma/m < 0$ and $b = -g < 0$, so $b/a = mg/\gamma$ and
>
> $$
> v(t) = \frac{mg}{\gamma} + \Big(v_0 - \frac{mg}{\gamma}\Big)e^{-\gamma t/m} , \qquad (20)
> $$
>
> where $v_0$ is the initial velocity. Every solution tends to the terminal velocity $mg/\gamma$, at a rate set by the exponent $-\gamma/m$: for a given mass, a larger drag coefficient means faster convergence.
>
> In short, the solutions of (3) approach the equilibrium $b/a$ when $a < 0$ and move away from it when $a > 0$, as the direction fields of [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-2|Examples §1.2]] and [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-3|§1.3]] suggested.

^rem-2-1

## The Falling Object

> [!example] Example §2.2: Velocity of a Dropped Object
> An object of mass $m = 10$ kg with drag coefficient $\gamma = 2$ kg/s is dropped from a height of $300$ m. Find its velocity at any time $t$.
>
> **Initial value problem.** The equation of motion is $\dfrac{dv}{dt} = 9.8 - \dfrac{v}{5}$ (equation (5) of [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-1|§1]]). "Dropped" means it starts from rest: $v(0) = 0$.
>
> **Solve.** Directly (rather than by substituting into (20)): $\dfrac{dv}{dt} = -\dfrac{v - 49}{5}$, so for $v \ne 49$
>
> $$
> \frac{dv/dt}{v - 49} = -\frac15 , \qquad \ln|v - 49| = -\frac{t}{5} + C , \qquad v = 49 + ce^{-t/5} . \qquad (25)
> $$
>
> **Initial condition.** $v(0) = 0$ gives $0 = 49 + c$, so $c = -49$ and
>
> $$
> v(t) = 49\big(1 - e^{-t/5}\big) . \qquad (26)
> $$
>
> This holds from the moment of release until the object hits the ground. Whatever the initial velocity, every solution (25) tends to the equilibrium $v = 49$ m/s, confirming [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-2|Example §1.2]].
>
> *BDP: Example 1.2.2*

^ex-2-2

> [!example] Example §2.3: Time and Speed of Impact
> For the object of [[§2 Solutions of Some Differential Equations#^ex-2-2|Example §2.2]], how long does it take to fall $300$ m, and how fast is it moving at impact?
>
> **Distance fallen.** The distance $x$ fallen satisfies $dx/dt = v$, so by (26)
>
> $$
> \frac{dx}{dt} = 49\big(1 - e^{-t/5}\big), \qquad x = 49t + 245e^{-t/5} + k ,
> $$
>
> since an antiderivative of $-49e^{-t/5}$ is $-49 \cdot (-5)e^{-t/5} = 245e^{-t/5}$. The object starts falling at $t = 0$ with $x = 0$, so $0 = 245 + k$, $k = -245$, and
>
> $$
> x(t) = 49t + 245e^{-t/5} - 245 . \qquad (29)
> $$
>
> **Time of impact.** The time $T$ of impact satisfies $x(T) = 300$:
>
> $$
> 49T + 245e^{-T/5} - 245 = 300 . \qquad (30)
> $$
>
> This equation cannot be solved in closed form. The function $x(t)$ is increasing ($x' = v > 0$ for $t > 0$), so there is exactly one root, and a numerical solver gives $T \approx 10.51$ s. (Check: $49(10.51) + 245e^{-2.102} - 245 \approx 515.0 + 29.9 - 245 \approx 299.9$.)
>
> **Speed at impact.** From (26), $v(T) = 49\big(1 - e^{-10.51/5}\big) \approx 49(1 - 0.1222) \approx 43.01$ m/s, about $88\%$ of the terminal velocity.
>
> *BDP: Example 1.2.2*

^ex-2-3

![[m331-2-1.svg]]
*The dropped object of [[§2 Solutions of Some Differential Equations#^ex-2-2|Examples §2.2]] and [[§2 Solutions of Some Differential Equations#^ex-2-3|§2.3]]. (a) The velocity rises toward the terminal velocity $49$ m/s but is still only $43.01$ m/s at the moment of impact. (b) The distance fallen; it reaches $300$ m at $T \approx 10.51$ s. Dotted: the formulas continued past impact, where they no longer describe the motion.*

## Further Remarks on Mathematical Modeling

> [!remark] Remark: Testing a Model
> The ultimate test of a model is whether its predictions agree with observation. For the falling object, Newton's laws are well established, but the assumption that drag is proportional to velocity is less certain, and $\gamma$ is hard to measure directly; it is sometimes found indirectly, by timing a fall from a known height and choosing the $\gamma$ that predicts the observed time. For the mice, $r$ and $k$ come from observations that vary considerably, and their constancy is doubtful: a constant predation rate is hard to sustain as the population shrinks, and unlimited exponential growth above $900$ contradicts real populations ([[§8 Autonomous Differential Equations and Population Dynamics|§8]]). If the discrepancies are too large, refine the model, observe more carefully, or both. Accuracy and simplicity usually trade off against each other, and even an imperfect model may explain the qualitative features of a problem.

^rem-2-2

> [!remark]- Remark: Historical Background (Euler, Lagrange, Laplace)
> Leonhard Euler (1707–1783) formulated problems of mechanics as differential equations and developed methods to solve them: the condition for exactness and the theory of integrating factors ([[§9 Exact Differential Equations and Integrating Factors|§9]], 1734–35), the general solution of homogeneous linear equations with constant coefficients ([[§13 Homogeneous Differential Equations with Constant Coefficients|§13]], 1743) and its nonhomogeneous extension, power series methods, and a numerical procedure ([[§10 Numerical Approximations꞉ Euler's Method|§10]], 1768–69). Joseph-Louis Lagrange (1736–1813) showed that the general solution of a homogeneous $n$th order linear equation is a linear combination of $n$ independent solutions ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian|§14]]) and developed variation of parameters ([[§18★ Variation of Parameters|§18★]]). Pierre-Simon de Laplace (1749–1827) is known for celestial mechanics, Laplace's equation, and the transform of [[§21 Definition of the Laplace Transform|§21]]. In the nineteenth century the interest turned to existence and uniqueness and to series methods.

^rem-2-3
