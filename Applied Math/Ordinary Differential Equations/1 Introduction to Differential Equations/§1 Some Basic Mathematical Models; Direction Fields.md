---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 1
section: 1
bdp: "1.1"
aliases: ["BDP 1.1"]
tags: [ordinary-differential-equations, math331]
---
↑ [[· 1 Introduction to Differential Equations]] · [[§2 Solutions of Some Differential Equations]] →

*Boyce–DiPrima, Section 1.1.*

Laws of nature are often statements about rates, and a law about rates written in symbols is a differential equation. This section builds two models of the form $dy/dt = ay - b$: an object falling against air resistance, and a population of field mice preyed on by owls. It then studies them *without solving them*, through the direction field, a picture of the slopes that every solution must follow. In both models a constant equilibrium solution separates the increasing solutions from the decreasing ones. For the falling object the other solutions are drawn toward it, and for the mice they are driven away. This qualitative picture comes before any formula and is often the most informative part of the analysis.

## Differential Equations as Mathematical Models

> [!definition] Definition §1.1: Differential Equation; Mathematical Model
> A **differential equation** is an equation containing derivatives of an unknown function. A differential equation that describes some physical process is called a **mathematical model** of the process.
>
> Constants in a model that depend on the particular object or situation, and may take a range of values (such as the mass $m$ and the drag coefficient $\gamma$ below), are called **parameters**. Constants with a fixed value for all objects (such as $g$) are physical constants.
>
> *BDP: 1.1 (text)*

^def-1-1

> [!remark]- Connections
> - See also: [[§57 Modeling with Differential Equations#^def-57-5|Calc Def. §57.5]] (Stewart's definition, with the order of an equation; order is [[§3 Classification of Differential Equations#^def-3-3|Definition §3.3]] here) and Stewart's first models: natural growth, [[§57 Modeling with Differential Equations#^def-57-1|Calc Def. §57.1]], and the spring, [[§57 Modeling with Differential Equations#^def-57-4|Calc Def. §57.4]].

> [!example] Example §1.1: A Falling Object
> Formulate a differential equation for the motion of an object falling in the atmosphere near sea level.
>
> **Variables and units.** Let $t$ be time (in s) and $v(t)$ the velocity (in m/s), positive *downward*. Mass $m$ is in kg and force in newtons.
>
> **Principle.** Newton's second law, $F = ma$, with $a = dv/dt$:
>
> $$
> F = m\,\frac{dv}{dt} .
> $$
>
> **Forces.** Gravity pulls down with the weight $mg$, where $g \approx 9.8$ m/s² near the earth's surface. Air resistance (drag) is assumed proportional to the velocity: it has magnitude $\gamma v$, where $\gamma > 0$ is the **drag coefficient** (in kg/s, so that $\gamma v$ has the units kg·m/s² of a force), and it acts upward on a falling object. So $F = mg - \gamma v$ and
>
> $$
> m\,\frac{dv}{dt} = mg - \gamma v . \qquad (4)
> $$
>
> This is the model. It contains the parameters $m$ and $\gamma$, which depend strongly on the object (a streamlined object has a much smaller $\gamma$ than a rough blunt one), and the physical constant $g$. With $m = 10$ kg and $\gamma = 2$ kg/s it becomes
>
> $$
> \frac{dv}{dt} = 9.8 - \frac{v}{5} . \qquad (5)
> $$
>
> *BDP: Example 1.1.1*

^ex-1-1

## Direction Fields

> [!definition] Definition §1.2: Direction Field
> Consider a first-order equation
>
> $$
> \frac{dy}{dt} = f(t, y) , \qquad (6)
> $$
>
> where $f$ is a given function of two variables, the **rate function**. At each point $(t, y)$ of a rectangular grid, draw a short line segment with slope $f(t, y)$. The resulting picture is the **direction field** (or **slope field**) of equation (6).
>
> Each segment is tangent to the graph of the solution through that point. Constructing it requires no solving, only many evaluations of $f$, which makes it a natural task for a computer; a grid of a few hundred points usually shows the overall behavior of the solutions.
>
> *BDP: 1.1 (text)*

^def-1-2

> [!remark]- Connections
> - See also: [[§58 Direction Fields and Euler's Method#^def-58-1|Calc Def. §58.1]] (Stewart's treatment, with the direction field of $y' = x^2 + y^2 - 1$) and its [[§58 Direction Fields and Euler's Method#^rem-58-1|Calc Remark: Method — Sketching Solution Curves from a Direction Field]]. The same tangent segments, followed step by step, give Euler's method ([[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|Definition §10.1]]).
> - Equilibrium solutions ([[§1 Some Basic Mathematical Models; Direction Fields#^def-1-3|Definition §1.3]] below) in Stewart: [[§57 Modeling with Differential Equations#^def-57-3|Calc Def. §57.3]].

> [!definition] Definition §1.3: Equilibrium Solution
> A constant function $y(t) = y_0$ that satisfies the differential equation is an **equilibrium solution**. For an equation $dy/dt = f(y)$ whose rate function does not depend on $t$, the equilibrium solutions are found by solving the algebraic equation $f(y) = 0$.
>
> For the falling object, the equilibrium solution is called the **terminal velocity**: it is the velocity at which gravity and drag balance exactly.
>
> *BDP: 1.1 (text)*

^def-1-3

> [!example] Example §1.2: The Direction Field of the Falling Object
> Investigate the solutions of $\dfrac{dv}{dt} = 9.8 - \dfrac{v}{5}$ (equation (5)) without solving the equation.
>
> **Slopes from the equation.** If $v = 40$, then $dv/dt = 9.8 - 8 = 1.8$; so every solution crosses the horizontal line $v = 40$ with slope $1.8$. Likewise $dv/dt = 9.8 - 10 = -0.2$ on $v = 50$ and $dv/dt = 9.8 - 12 = -2.2$ on $v = 60$. Since the right side depends only on $v$, all segments on one horizontal line are parallel. Repeating this on a grid gives the direction field (Figure (a) below).
>
> **The critical value.** The slopes are positive below a certain value of $v$ and negative above it. That value makes the right side zero:
>
> $$
> 9.8 - \frac{v}{5} = 0 \iff v = 5(9.8) = 49 \text{ m/s} .
> $$
>
> The constant function $v(t) = 49$ is a solution: both sides of (5) are $0$. It is the equilibrium solution (the terminal velocity).
>
> **Conclusions.** An object falling slower than $49$ m/s speeds up, and one falling faster slows down. All other solutions appear to approach $v = 49$ as $t$ increases, so an object that has fallen long enough moves at very nearly the terminal velocity.
>
> For the general equation (4), with $m, \gamma > 0$ unspecified, the same reasoning gives the equilibrium solution $v = mg/\gamma$, with solutions below it increasing and solutions above it decreasing, all approaching $mg/\gamma$.
>
> *BDP: Example 1.1.2*

^ex-1-2

> [!remark] Remark: Method — Reading a Direction Field
> For an equation $dy/dt = f(t, y)$:
> 1. Evaluate $f$ on a grid of points (or along chosen lines $y =$ const, as in [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-2|Example §1.2]]) and draw a short segment of slope $f(t, y)$ at each point.
> 2. Find the curves where $f = 0$. If $f$ depends only on $y$, these are horizontal lines, and each is an equilibrium solution ([[§1 Some Basic Mathematical Models; Direction Fields#^def-1-3|Definition §1.3]]).
> 3. Determine the sign of $f$ between them: solutions increase where $f > 0$ and decrease where $f < 0$.
> 4. Sketch solution curves tangent to the segments everywhere, and read off the behavior as $t \to \infty$ and how it depends on the initial value.

^rem-1-1

## Field Mice and Owls

In the absence of predators, assume that a population of field mice grows at a rate proportional to its current size. This is not a physical law, but it is a common first hypothesis about population growth (a better model is the logistic equation, [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-3|Definition §8.3]]).

> [!definition] Definition §1.4: Rate Constant (Growth Rate)
> If $p(t)$ is the population at time $t$, the hypothesis is
>
> $$
> \frac{dp}{dt} = rp , \qquad (7)
> $$
>
> and the proportionality factor $r$ is called the **rate constant** or **growth rate**. It has units of $1/\text{time}$, so that both sides of (7) have the units of population per unit time.
>
> *BDP: 1.1 (text)*

^def-1-4

> [!remark]- Connections
> - See also: [[§57 Modeling with Differential Equations#^def-57-1|Calc Def. §57.1]] and [[§21 Exponential Growth and Decay#^def-21-1|Calc Def. §21.1]] (the law of natural growth), whose solutions $p = p(0)e^{rt}$ are found in [[§21 Exponential Growth and Decay#^thm-21-1|Calc Thm. §21.1]]; here they are the case $b = 0$ of [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]].

> [!example] Example §1.3: Mice Preyed On by Owls
> Let time be measured in months and suppose $r = 0.5$/month. Several owls in the neighborhood kill $15$ mice per day. Formulate the model and investigate its solutions graphically.
>
> **The model.** The predation is a constant loss rate. Since time is in months, it must be expressed per month: $15 \cdot 30 = 450$ mice/month. Subtracting it from (7),
>
> $$
> \frac{dp}{dt} = \frac{p}{2} - 450 . \qquad (8)
> $$
>
> **The direction field** (Figure (b) below). For large $p$ the right side is positive and solutions increase; for small $p$ it is negative and solutions decrease. The critical value is where the right side vanishes:
>
> $$
> \frac{p}{2} - 450 = 0 \iff p = 900 ,
> $$
>
> and $p(t) = 900$ is the equilibrium solution, at which growth and predation balance exactly.
>
> **Comparison with [[§1 Some Basic Mathematical Models; Direction Fields#^ex-1-2|Example §1.2]].** In both cases the equilibrium separates increasing from decreasing solutions. But here the other solutions *diverge* from it: a population slightly above $900$ grows ever faster, and one slightly below shrinks ever faster. So the equilibrium population, although it organizes the whole picture, would not be observed in practice.
>
> More generally, with growth rate $r > 0$ and predation rate $k > 0$,
>
> $$
> \frac{dp}{dt} = rp - k , \qquad (9)
> $$
>
> whose equilibrium solution is $p = k/r$; solutions above it increase and solutions below it decrease.
>
> *BDP: Example 1.1.3*

^ex-1-3

![[m331-1-1.svg]]
*Direction fields (gray) of (a) the falling object, $v' = 9.8 - v/5$, and (b) the mice and owls, $p' = p/2 - 450$, with the equilibrium solutions (red) and a few solution curves (blue, from the formulas of [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]]). In (a) the segments all point toward $v = 49$ and the solutions converge to it; in (b) they point away from $p = 900$, and solutions starting near it are pushed off ever faster.*

> [!remark] Remark: Limitations of the Two Models
> The falling-object model is valid only while the object falls freely, and only at speeds where drag is roughly proportional to velocity; for fast, large objects a drag proportional to $v^2$ is more accurate. The mouse model eventually predicts negative populations (if $p < 900$) or enormous ones (if $p > 900$). Both predictions are unrealistic, so the model is acceptable only over a fairly short time interval.

^rem-1-2

## Constructing Mathematical Models

Successful modeling cannot be reduced to a set of rules, and constructing a satisfactory model is sometimes the hardest part of a problem. BDP lists steps that are often part of the process.

> [!remark] Remark: Method — Constructing a Mathematical Model
> 1. **Variables.** Identify the independent and dependent variables and assign letters to them. Often the independent variable is time.
> 2. **Units.** Choose units for each variable. The choice is in a sense arbitrary, but some choices are much more convenient (seconds for the falling object, months for the mice).
> 3. **Principle.** State the basic principle that governs the problem: a recognized physical law such as Newton's second law, or a more speculative assumption based on experience or observation. This step is usually not purely mathematical.
> 4. **Equation.** Express the principle in terms of the variables of step 1. This may require physical constants or parameters (such as $\gamma$) and auxiliary variables that must be related to the primary ones.
> 5. **Units check.** Make sure each term has the same units. A dimensionally consistent equation may still have other flaws, but an inconsistent one is certainly wrong.
> 6. **Result.** In the problems here, step 4 gives a single differential equation; more complex problems may lead to a system of several equations.

^rem-1-3

> [!remark]- Remark: Historical Background (Newton, Leibniz, the Bernoullis)
> Differential equations began with the calculus of Isaac Newton (1643–1727) and Gottfried Wilhelm Leibniz (1646–1716). Newton classified first-order equations into the forms $dy/dx = f(x)$, $dy/dx = f(y)$ and $dy/dx = f(x, y)$, and solved the last by infinite series when $f$ is a polynomial. Leibniz, who introduced the notations $dy/dx$ and $\int$, discovered separation of variables ([[§5 Separable Differential Equations|§5]]) and the reduction of homogeneous equations to separable ones in 1691, and the method for first-order linear equations ([[§4 Linear Differential Equations; Method of Integrating Factors|§4]]) in 1694. The brothers Jakob (1654–1705) and Johann (1667–1748) Bernoulli of Basel developed many methods and applications, and both solved the brachistochrone problem; Johann's son Daniel (1700–1782) worked mainly on partial differential equations.

^rem-1-4
