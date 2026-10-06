---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 58
stewart: "9.2"
aliases: ["Stewart 9.2"]
tags: [calculus]
---
← [[§57 Modeling with Differential Equations]] · ↑ [[· 9 Differential Equations]] · [[§59 Separable Equations]] →

*Stewart, Section 9.2.*

Most differential equations cannot be solved in the sense of obtaining an explicit formula for the solution. This section shows how much can be learned without one. A first-order equation $y' = F(x, y)$ prescribes the slope of the solution curve at every point, and drawing these slopes as short segments (a direction field) shows the shape of all solution curves at once: equilibria, limiting values, how solutions depend on the initial value. Following the slopes in small straight steps turns the same idea into a numerical method, Euler's method, which approximates the solution of an initial-value problem as accurately as we like by taking the step size small.

## Direction Fields

Suppose we want to sketch the graph of the solution of the initial-value problem

$$
y' = x + y, \qquad y(0) = 1 ,
$$

without a formula for it. The equation says that the slope at any point $(x, y)$ on the graph (the *solution curve*) is the sum $x + y$ of the coordinates of the point. Because the curve passes through $(0, 1)$, its slope there is $0 + 1 = 1$, so near $(0, 1)$ it looks like a short line segment through $(0, 1)$ with slope $1$. To guide the rest of the sketch, draw short segments with slope $x + y$ at many points $(x, y)$; at $(1, 2)$, for instance, the segment has slope $1 + 2 = 3$. Then draw the solution curve through $(0, 1)$ so that it is parallel to nearby segments.

> [!definition] Definition §58.1: Direction Field
> Consider a first-order differential equation of the form
>
> $$
> y' = F(x, y) ,
> $$
>
> where $F(x, y)$ is some expression in $x$ and $y$. The equation says that the slope of a solution curve at a point $(x, y)$ on the curve is $F(x, y)$. Short line segments with slope $F(x, y)$ drawn at several points $(x, y)$ form the **direction field** (or **slope field**) of the equation. The segments indicate the direction in which a solution curve is heading at each point, so the direction field shows the general shape of the solution curves.
>
> *Stewart: 9.2 (text)*

^def-58-1

> [!remark]- Connections
> - ODE version: [[§1 Some Basic Mathematical Models; Direction Fields#^def-1-2|331 Def. §1.2]] (direction field of $dy/dt = f(t, y)$), with [[§1 Some Basic Mathematical Models; Direction Fields#^rem-1-1|331 Remark: Method — Reading a Direction Field]].

> [!remark] Remark: Method — Sketching Solution Curves from a Direction Field
> 1. Compute the slopes $F(x, y)$ at the points of a grid; a table organized by rows ($y$ fixed) is convenient. Look for curves along which the slope is constant (for example, where $F = 0$ the segments are horizontal).
> 2. Draw a short segment with the computed slope at each grid point. The more segments, the clearer the picture; computers draw detailed fields.
> 3. To sketch the solution through $(x_0, y_0)$, start there and move to the right, keeping the curve parallel to the nearby segments. Then return to $(x_0, y_0)$ and draw the curve to the left in the same way.
> 4. Read off the qualitative behaviour: horizontal lines along which all segments are horizontal are equilibrium solutions ([[§57 Modeling with Differential Equations#^def-57-3|Def. §57.3]]), and solutions that approach such a line have it as their limiting value.

^rem-58-1

> [!example] Example §58.1: Sketching a Direction Field
> (a) Sketch the direction field for the differential equation $y' = x^2 + y^2 - 1$.
> (b) Use part (a) to sketch the solution curve that passes through the origin.
>
> **(a)** Compute the slope at several points:
>
> | $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
> |---|---|---|---|---|---|---|---|---|---|---|
> | $y$ | $0$ | $0$ | $0$ | $0$ | $0$ | $1$ | $1$ | $1$ | $1$ | $1$ |
> | $y' = x^2 + y^2 - 1$ | $3$ | $0$ | $-1$ | $0$ | $3$ | $4$ | $1$ | $0$ | $1$ | $4$ |
>
> and draw short segments with these slopes at these points (and similarly at more points). The slope depends only on the distance $\sqrt{x^2 + y^2}$ from the origin: it is $0$ on the unit circle $x^2 + y^2 = 1$, negative inside it (at least $-1$, at the origin) and positive and growing outside it.
>
> **(b)** Start at the origin and move to the right in the direction of the segment there, which has slope $-1$. Continue drawing the curve so that it moves parallel to the nearby segments: it decreases while inside the unit circle, turns where it crosses the circle (slope $0$), and then climbs ever more steeply. Returning to the origin, draw the curve to the left in the same way.
>
> The picture is symmetric: since $F(-x, -y) = F(x, y)$, if $y(x)$ is a solution then so is $z(x) = -y(-x)$ (indeed $z'(x) = y'(-x) = F(-x, y(-x)) = F(-x, -z(x)) = F(x, z(x))$). Both pass through the origin, and an initial-value problem like this one has only one solution ([[§59 Separable Equations#^rem-59-2|Remark: Solution Curves Do Not Cross]]), so the solution through the origin is an odd function.
>
> *Stewart: Example 9.2.1*

^ex-58-1

![[m233-58-1.svg]]
*The direction field of $y' = x^2 + y^2 - 1$ (blue) on a grid of spacing $\frac14$, and the solution curve through the origin (red). On the unit circle (green) the segments are horizontal, so the solution curve has its turning points there. Outside the circle the slopes grow quickly, and the curve becomes nearly vertical.*

Direction fields also give insight into physical situations. A simple electric circuit contains an electromotive force (usually a battery or generator) that produces a voltage of $E(t)$ volts (V) and a current of $I(t)$ amperes (A) at time $t$, a resistor with a resistance of $R$ ohms ($\Omega$), an inductor with an inductance of $L$ henries (H), and a switch. By Ohm's Law the drop in voltage due to the resistor is $RI$; the voltage drop due to the inductor is $L(dI/dt)$.

> [!definition] Definition §58.2: The RL Circuit Equation
> One of Kirchhoff's laws says that the sum of the voltage drops equals the supplied voltage $E(t)$. Thus
>
> $$
> L\,\frac{dI}{dt} + RI = E(t) ,
> $$
>
> a first-order differential equation that models the current $I$ at time $t$. (Section 9.5 solves it as a linear equation: [[§61 Linear Equations#^def-61-3|Definition §61.3]].)
>
> *Stewart: 9.2, Equation 1*

^def-58-2

> [!example] Example §58.2: Current in a Circuit
> In the circuit of [[§58 Direction Fields and Euler's Method#^def-58-2|Definition §58.2]], suppose the resistance is $12\ \Omega$, the inductance is $4$ H, and a battery gives a constant voltage of $60$ V.
> (a) Draw a direction field for the equation with these values.
> (b) What can you say about the limiting value of the current?
> (c) Identify any equilibrium solutions.
> (d) If the switch is closed when $t = 0$, so that $I(0) = 0$, use the direction field to sketch the solution curve.
>
> **(a)** With $L = 4$, $R = 12$ and $E(t) = 60$ the equation becomes
>
> $$
> 4\,\frac{dI}{dt} + 12I = 60 \qquad\text{or}\qquad \frac{dI}{dt} = 15 - 3I .
> $$
>
> The slope $15 - 3I$ depends only on $I$: it is $0$ on the line $I = 5$, positive below it ($15$ at $I = 0$) and negative above it. So the segments are horizontal along $I = 5$, point upward below that line and downward above it, and are steeper the farther they are from it.
>
> **(b)** It appears from the direction field that all solutions approach the value $5$ A:
>
> $$
> \lim_{t \to \infty} I(t) = 5 .
> $$
>
> **(c)** The constant function $I(t) = 5$ is an equilibrium solution. Indeed, if $I(t) = 5$, then the left side of $dI/dt = 15 - 3I$ is $0$ and the right side is $15 - 3(5) = 0$.
>
> **(d)** Starting at $(0, 0)$ with slope $15$, the solution curve rises steeply, then flattens as it approaches the line $I = 5$ from below, without crossing it (the line is itself a solution curve, and solution curves do not cross: [[§59 Separable Equations#^rem-59-2|Remark: Solution Curves Do Not Cross]]).
>
> *Stewart: Example 9.2.2*

^ex-58-2

In [[§58 Direction Fields and Euler's Method#^ex-58-2|Example §58.2]] the segments along any horizontal line are parallel, because the independent variable $t$ does not occur on the right side of $I' = 15 - 3I$.

> [!definition] Definition §58.3: Autonomous Differential Equation
> A differential equation of the form
>
> $$
> y' = f(y) ,
> $$
>
> in which the independent variable is missing from the right side, is **autonomous**.
>
> *Stewart: 9.2 (text)*

^def-58-3

> [!remark]- Connections
> - ODE version: [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-1|331 Def. §8.1]] (autonomous equations, analysed there by equilibria, the phase line and stability).

> [!theorem] Proposition §58.1: Shifting Solutions of an Autonomous Equation
> If $y = g(t)$ is a solution of an autonomous equation $y' = f(y)$ and $c$ is a constant, then $y = g(t - c)$ is also a solution. So from one solution we obtain infinitely many others by shifting its graph to the right or left.
>
> *Stewart: 9.2 (text)*

^prop-58-1

> [!remark] Remark: Why It Works
> For an autonomous equation, the slopes at two points with the same $y$-coordinate are equal: the direction field looks the same along every horizontal line, so it is unchanged by a horizontal shift. A shifted solution curve is therefore still parallel to the segments everywhere. In [[§58 Direction Fields and Euler's Method#^ex-58-2|Example §58.2]], shifting the solution curve one and two time units to the right gives the solutions with $I(1) = 0$ and $I(2) = 0$: they correspond to closing the switch at $t = 1$ or $t = 2$.

^rem-58-2

> [!proof]+ Proof
> Stewart gives only the geometric argument above; here is the computation. Let $h(t) = g(t - c)$. By the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]), and because $g$ is a solution,
>
> $$
> h'(t) = g'(t - c) \cdot 1 = f\big(g(t - c)\big) = f\big(h(t)\big) ,
> $$
>
> so $h$ is a solution. The equation being autonomous is what makes the middle step work: for $y' = F(t, y)$ we would get $F(t - c, h(t))$ instead of $F(t, h(t))$.

^pf-58-1

*Uses:* [[§58 Direction Fields and Euler's Method#^def-58-3|Def. §58.3]], [[§17 The Chain Rule#^thm-17-2|§17.2]]

## Euler's Method

> [!remark] Remark: The Idea of Euler's Method
> Return to the initial-value problem $y' = x + y$, $y(0) = 1$. The equation tells us that $y'(0) = 0 + 1 = 1$, so the solution curve has slope $1$ at $(0, 1)$. As a first approximation to the solution we could use the linear approximation $L(x) = x + 1$, the tangent line at $(0, 1)$ ([[§23 Linear Approximations and Differentials#^def-23-1|Definition §23.1]]).
>
> Euler's idea was to improve on this by proceeding only a short distance along the tangent line and then making a midcourse correction, changing direction as indicated by the direction field. Start along the tangent line, but stop at $x = 0.5$; this horizontal distance is the **step size**. Since $L(0.5) = 1.5$, we have $y(0.5) \approx 1.5$, and we take $(0.5, 1.5)$ as the starting point of a new segment. The equation gives $y'(0.5) = 0.5 + 1.5 = 2$ there, so for $x > 0.5$ we use the linear function
>
> $$
> y = 1.5 + 2(x - 0.5) = 2x + 0.5 .
> $$
>
> With step size $0.25$ instead of $0.5$ we make more corrections and get a better approximation. In general: start at the point given by the initial value, proceed in the direction indicated by the direction field, stop after a short distance, look at the slope at the new location, proceed in that direction, and keep stopping and changing direction.

^rem-58-3

> [!definition] Definition §58.4: Euler's Method
> Approximate values for the solution of the initial-value problem $y' = F(x, y)$, $y(x_0) = y_0$, with step size $h$, at $x_n = x_{n-1} + h$, are
>
> $$
> y_n = y_{n-1} + hF(x_{n-1}, y_{n-1}), \qquad n = 1, 2, 3, \ldots
> $$
>
> That is, $y_1 = y_0 + hF(x_0, y_0)$ approximates the solution at $x_1 = x_0 + h$, then $y_2 = y_1 + hF(x_1, y_1)$ approximates it at $x_2 = x_1 + h$, and so on.
>
> *Stewart: 9.2 (box "Euler's Method")*

^def-58-4

> [!remark] Remark: Why It Works
> The equation says that the slope of the solution at $(x_0, y_0)$ is $y' = F(x_0, y_0)$. Moving along the tangent line from $x_0$ to $x_1 = x_0 + h$, the run is $h$, so the rise is $h F(x_0, y_0)$, and we arrive at height $y_1 = y_0 + hF(x_0, y_0)$. From $(x_1, y_1)$ we repeat with the slope $F(x_1, y_1)$ that the direction field prescribes *there*, and so on. Euler's method does not produce the exact solution; it gives approximations. But by decreasing the step size, and so increasing the number of midcourse corrections, we obtain successively better approximations to the exact solution.

^rem-58-4

> [!remark]- Connections
> - Why one step is accurate: by Taylor's theorem with $n = 2$, $y(x_0 + h) = y_0 + hy'(x_0) + \frac{h^2}{2}y''(\xi) = y_0 + hF(x_0, y_0) + \frac{h^2}{2}y''(\xi)$ for some $\xi$ between $x_0$ and $x_0 + h$ ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]). So one step errs by at most a constant times $h^2$; over the $(b - x_0)/h$ steps needed to reach $x = b$ these errors add up to roughly a constant times $h$, which is the behaviour seen in the table of Remark: How Accurate Is Euler's Method? below.
> - ODE version: [[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|331 Def. §10.1]] (Euler's formula, also with unequal steps), and [[§10 Numerical Approximations꞉ Euler's Method#^prop-10-1|331 Prop. §10.1]], where for $y' = 1 - t + y$ the error is proved to be at most a constant times $h$.

> [!example] Example §58.3: A Table of Euler Approximations
> Use Euler's method with step size $0.1$ to construct a table of approximate values for the solution of the initial-value problem
>
> $$
> y' = x + y, \qquad y(0) = 1 .
> $$
>
> Here $h = 0.1$, $x_0 = 0$, $y_0 = 1$ and $F(x, y) = x + y$. So
>
> $$
> \begin{aligned}
> y_1 &= y_0 + hF(x_0, y_0) = 1 + 0.1(0 + 1) = 1.1 , \\
> y_2 &= y_1 + hF(x_1, y_1) = 1.1 + 0.1(0.1 + 1.1) = 1.22 , \\
> y_3 &= y_2 + hF(x_2, y_2) = 1.22 + 0.1(0.2 + 1.22) = 1.362 .
> \end{aligned}
> $$
>
> This means that if $y(x)$ is the exact solution, then $y(0.3) \approx 1.362$. Continuing in the same way:
>
> | $n$ | $x_n$ | $y_n$ | | $n$ | $x_n$ | $y_n$ |
> |---|---|---|---|---|---|---|
> | $1$ | $0.1$ | $1.100000$ | | $6$ | $0.6$ | $1.943122$ |
> | $2$ | $0.2$ | $1.220000$ | | $7$ | $0.7$ | $2.197434$ |
> | $3$ | $0.3$ | $1.362000$ | | $8$ | $0.8$ | $2.487178$ |
> | $4$ | $0.4$ | $1.528200$ | | $9$ | $0.9$ | $2.815895$ |
> | $5$ | $0.5$ | $1.721020$ | | $10$ | $1.0$ | $3.187485$ |
>
> *Stewart: Example 9.2.3*

^ex-58-3

> [!remark] Remark: How Accurate Is Euler's Method?
> For a more accurate table we decrease the step size; with many small steps the computation is done by a calculator or computer. For the initial-value problem of [[§58 Direction Fields and Euler's Method#^ex-58-3|Example §58.3]], Stewart's table gives:
>
> | step size | Euler estimate of $y(0.5)$ | Euler estimate of $y(1)$ |
> |---|---|---|
> | $0.500$ | $1.500000$ | $2.500000$ |
> | $0.250$ | $1.625000$ | $2.882813$ |
> | $0.100$ | $1.721020$ | $3.187485$ |
> | $0.050$ | $1.757789$ | $3.306595$ |
> | $0.020$ | $1.781212$ | $3.383176$ |
> | $0.010$ | $1.789264$ | $3.409628$ |
> | $0.005$ | $1.793337$ | $3.423034$ |
> | $0.001$ | $1.796619$ | $3.433848$ |
>
> The estimates seem to approach limits, namely the true values of $y(0.5)$ and $y(1)$: the Euler approximations approach the exact solution curve as $h \to 0$.
>
> Here the exact solution is known: $y = 2e^x - x - 1$ (it is found by the method of [[§61 Linear Equations#^thm-61-1|Theorem §61.1]], since $y' - y = x$ is linear; check: $y' = 2e^x - 1 = x + (2e^x - x - 1) = x + y$ and $y(0) = 2 - 1 = 1$). So $y(0.5) = 2\sqrt e - 1.5 \approx 1.797443$ and $y(1) = 2e - 2 \approx 3.436564$. The errors at $x = 1$ are about $0.249$ for $h = 0.1$, $0.027$ for $h = 0.01$ and $0.0027$ for $h = 0.001$: dividing the step size by $10$ divides the error by about $10$. All the estimates are too small, because this solution curve is concave upward ($y'' = 2e^x > 0$), so each tangent-line step falls below it.
>
> Computer software that produces numerical approximations to solutions of differential equations uses refinements of Euler's method; Euler's method, simple and not very accurate, is the idea on which they are based.

^rem-58-5

![[m233-58-2.svg]]
*Euler's method for $y' = x + y$, $y(0) = 1$. With $h = 0.5$ (blue) the first step runs $h = 0.5$ along the tangent at $(0, 1)$ and rises $hF(0, 1) = 0.5$; at $(0.5, 1.5)$ the direction is corrected to slope $2$. With $h = 0.25$ (green) there are four corrections and the polygon stays closer to the exact solution (red). Both lie below it, since the curve is concave upward.*

> [!example] Example §58.4: Euler's Method for the Circuit
> In [[§58 Direction Fields and Euler's Method#^ex-58-2|Example §58.2]] (resistance $12\ \Omega$, inductance $4$ H, battery voltage $60$ V, switch closed at $t = 0$), the current $I$ at time $t$ is modeled by the initial-value problem
>
> $$
> \frac{dI}{dt} = 15 - 3I, \qquad I(0) = 0 .
> $$
>
> Estimate the current in the circuit half a second after the switch is closed.
>
> Use Euler's method with $F(t, I) = 15 - 3I$, $t_0 = 0$, $I_0 = 0$ and step size $h = 0.1$ second:
>
> $$
> \begin{aligned}
> I_1 &= 0 + 0.1(15 - 3 \cdot 0) = 1.5 , \\
> I_2 &= 1.5 + 0.1(15 - 3 \cdot 1.5) = 2.55 , \\
> I_3 &= 2.55 + 0.1(15 - 3 \cdot 2.55) = 3.285 , \\
> I_4 &= 3.285 + 0.1(15 - 3 \cdot 3.285) = 3.7995 , \\
> I_5 &= 3.7995 + 0.1(15 - 3 \cdot 3.7995) = 4.15965 .
> \end{aligned}
> $$
>
> So the current after $0.5$ s is
>
> $$
> I(0.5) \approx 4.16 \text{ A} .
> $$
>
> For comparison, the exact solution is $I(t) = 5 - 5e^{-3t}$ (Stewart finds it by separation of variables in Section 9.3, Example 4, in the text of [[§59 Separable Equations|§59]], and again as a linear equation in [[§61 Linear Equations#^ex-61-4|Example §61.4]]; check: $I' = 15e^{-3t} = 15 - 3(5 - 5e^{-3t})$ and $I(0) = 0$), so $I(0.5) = 5 - 5e^{-1.5} \approx 3.88$ A. Here the estimate is too large: this solution curve is concave downward ($I'' = -45e^{-3t} < 0$), so each tangent-line step overshoots it. The error, about $0.28$ A, shrinks as $h$ decreases.
>
> *Stewart: Example 9.2.4*

^ex-58-4
