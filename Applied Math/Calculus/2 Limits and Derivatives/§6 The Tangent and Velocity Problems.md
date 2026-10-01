---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 6
stewart: "2.1"
aliases: ["Stewart 2.1"]
tags: [calculus]
---
← [[§5 Inverse Functions and Logarithms]] · ↑ [[· 2 Limits and Derivatives]] · [[§7 The Limit of a Function]] →

*Stewart, Section 2.1.*

Two old problems lead to the idea of a limit. To find the tangent line to a curve at a point $P$ we need its slope, but we know only one point of the line; so we approximate it by secant lines through $P$ and a nearby point $Q$ and let $Q$ approach $P$. To find the velocity of a moving object at an instant, we approximate it by average velocities over shorter and shorter time intervals. Both answers are limits, and they are the same limit: the velocity is the slope of the tangent line to the position graph. Limits are developed in [[§7 The Limit of a Function|§7]]–[[§11 Limits at Infinity; Horizontal Asymptotes|§11]], and both problems are solved for good in [[§12 Derivatives and Rates of Change|§12]].

## The Tangent Problem

The word *tangent* comes from the Latin *tangens*, "touching": a tangent to a curve should touch the curve and follow its direction at the point of contact. For a circle one can follow Euclid and call a line tangent if it meets the circle exactly once. For more complicated curves this does not work: a line can be tangent to a curve $C$ at a point $P$ and still cross $C$ somewhere else, and a line that meets a curve only once need not be tangent to it.

> [!definition] Definition §6.1: Secant Line
> A **secant line** of a curve is a line that cuts (intersects) the curve more than once; in particular, the line through two points $P$ and $Q$ of the curve. For the graph of $f$ and the points $P(a, f(a))$ and $Q(x, f(x))$ with $x \ne a$, the slope of the secant line $PQ$ is
>
> $$
> m_{PQ} = \frac{f(x) - f(a)}{x - a} .
> $$
>
> (From the Latin *secans*, cutting.)
>
> *Stewart: 2.1 (text)*

^def-6-1

> [!definition] Definition §6.2: Tangent Line (Preliminary)
> The slope $m$ of the **tangent line** to a curve at a point $P$ is the limit of the slopes of the secant lines $PQ$ as $Q$ approaches $P$ along the curve:
>
> $$
> m = \lim_{Q \to P} m_{PQ}, \qquad\text{for the graph of } f \text{ at } P(a, f(a)):\quad m = \lim_{x \to a} \frac{f(x) - f(a)}{x - a} .
> $$
>
> The tangent line is the line through $P$ with slope $m$; by the point-slope form ([[§117 Coordinate Geometry and Lines|§117]], Appendix B) its equation is $y - f(a) = m(x - a)$. As $Q$ approaches $P$, the secant lines rotate about $P$ and approach the tangent line.
>
> Here "limit" is still the intuitive notion; limits are defined in [[§7 The Limit of a Function|§7]] and the tangent line precisely in [[§12 Derivatives and Rates of Change|§12]].
>
> *Stewart: 2.1 (text)*

^def-6-2

> [!remark]- Connections
> - Rigorous version: the limit of the difference quotient is the derivative, [[§28 Basic Properties of the Derivative#^def-28-1|451 Def. §28.1]]; only $x \ne a$ is ever used, since at $x = a$ there is no secant.

> [!example] Example §6.1: The Tangent Line to a Parabola
> Find an equation of the tangent line to the parabola $y = x^2$ at the point $P(1, 1)$.
>
> We know one point of the tangent line, $P$, and need its slope $m$. Choose a nearby point $Q(x, x^2)$ on the parabola with $x \ne 1$, so that $Q \ne P$. The secant line $PQ$ has slope
>
> $$
> m_{PQ} = \frac{x^2 - 1}{x - 1} .
> $$
>
> For instance, $Q(1.5, 2.25)$ gives $m_{PQ} = \dfrac{2.25 - 1}{1.5 - 1} = \dfrac{1.25}{0.5} = 2.5$. More values, with $Q$ to the right and to the left of $P$:
>
> | $x$ | $2$ | $1.5$ | $1.1$ | $1.01$ | $1.001$ | | $0$ | $0.5$ | $0.9$ | $0.99$ | $0.999$ |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $m_{PQ}$ | $3$ | $2.5$ | $2.1$ | $2.01$ | $2.001$ | | $1$ | $1.5$ | $1.9$ | $1.99$ | $1.999$ |
>
> The closer $x$ is to $1$, the closer $m_{PQ}$ is to $2$. (The tables are no accident: for $x \ne 1$, $\dfrac{x^2 - 1}{x - 1} = \dfrac{(x - 1)(x + 1)}{x - 1} = x + 1$.) So the slope of the tangent line should be
>
> $$
> m = \lim_{Q \to P} m_{PQ} = \lim_{x \to 1} \frac{x^2 - 1}{x - 1} = 2 .
> $$
>
> Assuming this, the point-slope form gives the tangent line through $(1, 1)$:
>
> $$
> y - 1 = 2(x - 1), \qquad\text{that is,}\qquad y = 2x - 1 .
> $$
>
> *Stewart: Example 2.1.1*

^ex-6-1

![[m233-6-1.svg]]
*Secant lines through $P(1, 1)$ on $y = x^2$. With $Q$ at $x = 2, 1.5, 1.2$ (blue, lighter to darker) the slopes $m_{PQ} = x + 1$ are $3, 2.5, 2.2$; with $Q$ at $x = 0$ (green, $Q$ to the left of $P$) the slope is $1$. As $Q$ approaches $P$ from either side, the secants rotate about $P$ toward the tangent line $y = 2x - 1$ (red) of slope $2$.*

Many functions in the sciences are known only through experimental data. The same idea then gives an estimate of the slope of the tangent line.

> [!example] Example §6.2: Estimating a Slope from Data
> A pulse laser stores charge on a capacitor and releases it when the laser is fired. The table gives the charge $Q$ (coulombs) remaining on the capacitor $t$ seconds after firing. Estimate the slope of the tangent line at $t = 0.04$. (This slope is the electric current, in amperes, flowing from the capacitor to the laser.)
>
> | $t$ | $0$ | $0.02$ | $0.04$ | $0.06$ | $0.08$ | $0.1$ |
> |---|---|---|---|---|---|---|
> | $Q$ | $10$ | $8.187$ | $6.703$ | $5.488$ | $4.493$ | $3.676$ |
>
> Plot the points and join them by a smooth curve. **Secant slopes.** With $P(0.04, 6.703)$ and $R$ another data point,
>
> $$
> m_{PR} = \frac{Q_R - 6.703}{t_R - 0.04} :
> $$
>
> | $R$ | $(0, 10)$ | $(0.02, 8.187)$ | $(0.06, 5.488)$ | $(0.08, 4.493)$ | $(0.1, 3.676)$ |
> |---|---|---|---|---|---|
> | $m_{PR}$ | $\dfrac{3.297}{-0.04} = -82.425$ | $\dfrac{1.484}{-0.02} = -74.200$ | $\dfrac{-1.215}{0.02} = -60.750$ | $\dfrac{-2.210}{0.04} = -55.250$ | $\dfrac{-3.027}{0.06} = -50.450$ |
>
> The slope of the tangent line should lie between the slopes of the two closest secants, $-74.20$ and $-60.75$. Their average is
>
> $$
> \tfrac12(-74.20 - 60.75) = -67.475 ,
> $$
>
> so the slope of the tangent line is about $-67.5$.
>
> **Drawing the tangent.** Alternatively, draw an approximate tangent line at $P$ on the graph and measure a right triangle $ABC$ under it: from the drawing, $A \approx (0.02, 8.0)$ and $C \approx (0.06, 5.4)$, so the slope is
>
> $$
> -\frac{|AB|}{|BC|} \approx -\frac{8.0 - 5.4}{0.06 - 0.02} = -\frac{2.6}{0.04} = -65.0 .
> $$
>
> Physically: the current flowing from the capacitor to the laser $0.04$ s after firing is about $-65$ amperes.
>
> *Stewart: Example 2.1.2*

^ex-6-2

## The Velocity Problem

The speedometer of a car in city traffic shows a speed that keeps changing, yet we believe that the car has a definite velocity at each moment. How is this "instantaneous" velocity defined, if the position of the object is known at every time?

> [!definition] Definition §6.3: Average and Instantaneous Velocity
> Let $s(t)$ be the position at time $t$ of an object moving along a straight line. Its **average velocity** over the time interval from $t = a$ to $t = a + h$ ($h \ne 0$) is
>
> $$
> \text{average velocity} = \frac{\text{change in position}}{\text{time elapsed}} = \frac{s(a + h) - s(a)}{h} .
> $$
>
> The **instantaneous velocity** at $t = a$ is the limiting value of these average velocities over shorter and shorter time intervals, that is, as $h \to 0$.
>
> *Stewart: 2.1 (text)*

^def-6-3

> [!example] Example §6.3: A Falling Ball
> A ball is dropped from the upper observation deck of the CN Tower in Toronto, $450$ m above the ground. Find its velocity after $5$ seconds.
>
> **The model.** Galileo found that the distance fallen by a freely falling body is proportional to the square of the time it has been falling (neglecting air resistance). Near the earth's surface, with $s(t)$ in meters,
>
> $$
> s(t) = 4.9 t^2 .
> $$
>
> (The ball hits the ground when $4.9t^2 = 450$, at $t \approx 9.6$ s, so $t = 5$ is during the fall.)
>
> **Average velocities.** At a single instant $t = 5$ no time interval is involved, so approximate by the average velocity from $t = 5$ to $t = 5.1$:
>
> $$
> \frac{s(5.1) - s(5)}{0.1} = \frac{4.9(5.1)^2 - 4.9(5)^2}{0.1} = \frac{4.9(26.01 - 25)}{0.1} = 49.49 \text{ m/s} .
> $$
>
> Over shorter intervals:
>
> | time interval | $5 \le t \le 5.1$ | $5 \le t \le 5.05$ | $5 \le t \le 5.01$ | $5 \le t \le 5.001$ |
> |---|---|---|---|---|
> | average velocity (m/s) | $49.49$ | $49.245$ | $49.049$ | $49.0049$ |
>
> The averages approach $49$ m/s. The pattern is exact: for $h \ne 0$,
>
> $$
> \frac{4.9(5 + h)^2 - 4.9(5)^2}{h} = \frac{4.9(10h + h^2)}{h} = 4.9(10 + h) = 49 + 4.9h ,
> $$
>
> which gives each entry of the table ($h = 0.1$: $49.49$; $h = 0.001$: $49.0049$) and tends to $49$ as $h \to 0$. So the instantaneous velocity after $5$ seconds is $49$ m/s.
>
> *Stewart: Example 2.1.3*

^ex-6-3

> [!remark] Remark: Velocity Is the Slope of a Tangent Line
> The tangent problem and the velocity problem are the same problem. On the graph of the position function $s = 4.9t^2$, take $P(5, 4.9(5)^2)$ and $Q(5 + h, 4.9(5 + h)^2)$. The slope of the secant line $PQ$ (Definition §6.1) is
>
> $$
> m_{PQ} = \frac{4.9(5 + h)^2 - 4.9(5)^2}{(5 + h) - 5} ,
> $$
>
> which is exactly the average velocity over the interval $[5, 5 + h]$ (Definition §6.3). Letting $h \to 0$: the velocity at $t = 5$, the limit of the average velocities, equals the slope of the tangent line at $P$, the limit of the secant slopes (Definition §6.2). In general,
>
> $$
> \text{slope of secant line} = \text{average velocity}, \qquad \text{slope of tangent line} = \text{instantaneous velocity}.
> $$
>
> To solve either problem one must be able to compute limits. The next five sections develop the methods ([[§7 The Limit of a Function|§7]]–[[§11 Limits at Infinity; Horizontal Asymptotes|§11]]), and Section 2.7 ([[§12 Derivatives and Rates of Change|§12]]) returns to tangents and velocities.

^rem-6-1
