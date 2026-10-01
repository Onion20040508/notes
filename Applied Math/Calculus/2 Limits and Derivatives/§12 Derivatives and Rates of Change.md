---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 12
stewart: "2.7"
aliases: ["Stewart 2.7"]
tags: [calculus]
---
← [[§11 Limits at Infinity; Horizontal Asymptotes]] · ↑ [[· 2 Limits and Derivatives]] · [[§13 The Derivative as a Function]] →

*Stewart, Section 2.7.*

With limits available, the tangent and velocity problems of [[§6 The Tangent and Velocity Problems|§6]] can be solved exactly. Both lead to the same limit, of the difference quotient $\big(f(a + h) - f(a)\big)/h$ as $h \to 0$, and this limit is named the derivative $f'(a)$. The derivative has two readings: geometrically, the slope of the tangent line to $y = f(x)$ at $(a, f(a))$; physically, the instantaneous rate of change of $y$ with respect to $x$ (velocity, marginal cost, rate of reaction …). Every computation in this section goes straight back to the definition; the rules that shortcut it come in Chapter 3.

## Tangents

> [!definition] Definition §12.1: Tangent Line
> The **tangent line** to the curve $y = f(x)$ at the point $P(a, f(a))$ is the line through $P$ with slope
>
> $$
> m = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
> $$
>
> provided that this limit exists. The quotient is the slope $m_{PQ}$ of the secant line through $P$ and a nearby point $Q(x, f(x))$, $x \ne a$, so the tangent line is the limiting position of the secant line $PQ$ as $Q$ approaches $P$ along the curve. The slope of the tangent line is also called the **slope of the curve** at $P$.
>
> *Stewart: 2.7, Definition 1*

^def-12-1

> [!theorem] Theorem §12.1: Slope of the Tangent with an Increment
> Writing $h = x - a$, so that $x = a + h$, the slope of the tangent line in Definition §12.1 is
>
> $$
> m = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} ,
> $$
>
> in the sense that one limit exists if and only if the other does, and then they are equal. Here $h > 0$ puts $Q(a + h, f(a + h))$ to the right of $P$ and $h < 0$ to the left.
>
> *Stewart: 2.7, Equation 2*

^thm-12-1

> [!proof]+ Proof
> Stewart's reason is that $h = x - a$ approaches $0$ exactly when $x$ approaches $a$. In terms of the precise definition ([[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]): let $F(x) = \dfrac{f(x) - f(a)}{x - a}$, so that $F(a + h) = \dfrac{f(a + h) - f(a)}{h}$. Suppose $\lim_{x \to a} F(x) = m$, and let $\varepsilon > 0$. There is $\delta > 0$ with
>
> $$
> 0 < |x - a| < \delta \quad\Longrightarrow\quad |F(x) - m| < \varepsilon .
> $$
>
> If $0 < |h| < \delta$, put $x = a + h$: then $0 < |x - a| < \delta$, so $|F(a + h) - m| < \varepsilon$. Hence $\lim_{h \to 0} F(a + h) = m$. Conversely, if $\lim_{h \to 0} F(a + h) = m$ with some $\delta$ for a given $\varepsilon$, then $0 < |x - a| < \delta$ gives $0 < |h| < \delta$ for $h = x - a$, so $|F(x) - m| = |F(a + h) - m| < \varepsilon$. The same $\delta$ works in both directions.

^pf-12-1

*Uses:* [[§12 Derivatives and Rates of Change#^def-12-1|Def. §12.1]], [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]] (precise definition of a limit)

![[m233-12-1.svg]]
*Theorem §12.1 in a picture. With $Q = (a + h, f(a + h))$ the secant $PQ$ (blue) has run $h$ and rise $f(a + h) - f(a)$ (green), so its slope is the difference quotient $\big(f(a + h) - f(a)\big)/h$; as $h \to 0$, $Q$ slides along the curve to $P$ and the secant turns into the tangent line at $P$ (red). (The concrete case $y = x^2$ at $(1, 1)$, with numerical secant slopes $3, 2.5, 2.2, \ldots \to 2$, is pictured after [[§6 The Tangent and Velocity Problems#^ex-6-1|Example §6.1]].)*

> [!example] Example §12.1: Tangent Lines from the Definition
> **(a)** Find an equation of the tangent line to the parabola $y = x^2$ at $P(1, 1)$.
>
> Here $a = 1$ and $f(x) = x^2$. By Definition §12.1,
>
> $$
> m = \lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} \frac{(x - 1)(x + 1)}{x - 1} = \lim_{x \to 1} (x + 1) = 1 + 1 = 2 .
> $$
>
> By the point-slope form $y - y_1 = m(x - x_1)$, the tangent line is $y - 1 = 2(x - 1)$, or $y = 2x - 1$. This confirms the guess made from secant slopes in [[§6 The Tangent and Velocity Problems#^ex-6-1|Example §6.1]]. Zooming in toward $(1, 1)$, the parabola becomes almost indistinguishable from this line.
>
> **(b)** Find an equation of the tangent line to the hyperbola $y = 3/x$ at $(3, 1)$.
>
> Let $f(x) = 3/x$. By Theorem §12.1,
>
> $$
> m = \lim_{h \to 0} \frac{f(3 + h) - f(3)}{h} = \lim_{h \to 0} \frac{\dfrac{3}{3 + h} - 1}{h} = \lim_{h \to 0} \frac{\dfrac{3 - (3 + h)}{3 + h}}{h} = \lim_{h \to 0} \frac{-h}{h(3 + h)} = \lim_{h \to 0} \frac{-1}{3 + h} = -\frac13 .
> $$
>
> The tangent line is $y - 1 = -\frac13 (x - 3)$, which simplifies to $x + 3y - 6 = 0$.
>
> *Stewart: Examples 2.7.1 and 2.7.2*

^ex-12-1

## Velocities

> [!definition] Definition §12.2: Average and Instantaneous Velocity
> Let an object move along a straight line according to an equation of motion $s = f(t)$, where $s$ is the displacement (directed distance) of the object from the origin at time $t$; $f$ is the **position function** of the object. Over the time interval from $t = a$ to $t = a + h$ the change in position is $f(a + h) - f(a)$, and the **average velocity** is
>
> $$
> \text{average velocity} = \frac{\text{displacement}}{\text{time}} = \frac{f(a + h) - f(a)}{h} ,
> $$
>
> the slope of the secant line $PQ$ on the graph of $f$. The **velocity** (or **instantaneous velocity**) of the object at time $t = a$ is
>
> $$
> v(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
> $$
>
> provided that this limit exists. By Theorem §12.1, $v(a)$ is the slope of the tangent line to the graph of $f$ at $P(a, f(a))$.
>
> *Stewart: 2.7, Definition 3*

^def-12-2

> [!example] Example §12.2: The Falling Ball
> A ball is dropped from the upper observation deck of the CN Tower, $450$ m above the ground. (a) What is its velocity after $5$ seconds? (b) How fast is it traveling when it hits the ground?
>
> The distance fallen after $t$ seconds is $s = f(t) = 4.9t^2$ meters ([[§6 The Tangent and Velocity Problems#^ex-6-3|Example §6.3]]). Two velocities are asked for, so first find the velocity at a general time $t = a$:
>
> $$
> \begin{aligned}
> v(a) &= \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} = \lim_{h \to 0} \frac{4.9(a + h)^2 - 4.9a^2}{h} = \lim_{h \to 0} \frac{4.9(a^2 + 2ah + h^2 - a^2)}{h} \\
> &= \lim_{h \to 0} \frac{4.9(2ah + h^2)}{h} = \lim_{h \to 0} \frac{4.9h(2a + h)}{h} = \lim_{h \to 0} 4.9(2a + h) = 9.8a .
> \end{aligned}
> $$
>
> **(a)** $v(5) = 9.8 \cdot 5 = 49$ m/s.
>
> **(b)** The ball hits the ground at the time $t_1$ when $s(t_1) = 450$, that is, $4.9t_1^2 = 450$. So $t_1^2 = 450/4.9$ and $t_1 = \sqrt{450/4.9} \approx 9.6$ s. The velocity at impact is
>
> $$
> v(t_1) = 9.8 \sqrt{\frac{450}{4.9}} \approx 94 \text{ m/s} .
> $$
>
> *Stewart: Example 2.7.3*

^ex-12-2

## Derivatives

The same limit computes the slope of a tangent line (Theorem §12.1) and a velocity (Definition §12.2), and it arises for every rate of change in the sciences and engineering (rate of reaction, marginal cost …). So it gets its own name.

> [!definition] Definition §12.3: Derivative at a Number
> The **derivative of a function $f$ at a number $a$**, denoted by $f'(a)$ (read "$f$ prime of $a$"), is
>
> $$
> f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
> $$
>
> if this limit exists. Equivalently (by the substitution $x = a + h$, exactly as in the proof of Theorem §12.1),
>
> $$
> f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a} .
> $$
>
> In practice the first form often leads to simpler computations.
>
> *Stewart: 2.7, Definition 4 and Equation 5*

^def-12-3

> [!remark]- Connections
> - Rigorous treatment: [[§28 Basic Properties of the Derivative#^def-28-1|451 Def. §28.1]] (the second form, for $f$ defined on an open interval containing $a$). Several variables, where the derivative becomes a linear map (the Jacobian matrix): [[§6 Differentiability#^def-6-2|452 Def. §6.2]].

> [!example] Example §12.3: A Derivative and a Tangent Line
> Let $f(x) = x^2 - 8x + 9$. Find (a) $f'(2)$; (b) $f'(a)$; (c) an equation of the tangent line to the parabola $y = x^2 - 8x + 9$ at $(3, -6)$.
>
> **(a)** By Definition §12.3, with $f(2) = 4 - 16 + 9 = -3$,
>
> $$
> \begin{aligned}
> f'(2) &= \lim_{h \to 0} \frac{f(2 + h) - f(2)}{h} = \lim_{h \to 0} \frac{(2 + h)^2 - 8(2 + h) + 9 - (-3)}{h} \\
> &= \lim_{h \to 0} \frac{4 + 4h + h^2 - 16 - 8h + 9 + 3}{h} = \lim_{h \to 0} \frac{h^2 - 4h}{h} = \lim_{h \to 0} (h - 4) = -4 .
> \end{aligned}
> $$
>
> **(b)**
>
> $$
> \begin{aligned}
> f'(a) &= \lim_{h \to 0} \frac{\big[(a + h)^2 - 8(a + h) + 9\big] - \big[a^2 - 8a + 9\big]}{h} \\
> &= \lim_{h \to 0} \frac{a^2 + 2ah + h^2 - 8a - 8h + 9 - a^2 + 8a - 9}{h} = \lim_{h \to 0} \frac{2ah + h^2 - 8h}{h} = \lim_{h \to 0} (2a + h - 8) = 2a - 8 .
> \end{aligned}
> $$
>
> As a check on (a): $a = 2$ gives $f'(2) = 2 \cdot 2 - 8 = -4$.
>
> **(c)** By (b) and Theorem §12.2 below, the slope of the tangent line at $(3, -6)$ is $f'(3) = 2 \cdot 3 - 8 = -2$, so the tangent line is
>
> $$
> y - (-6) = (-2)(x - 3) \qquad\text{or}\qquad y = -2x .
> $$
>
> *Stewart: Examples 2.7.4 and 2.7.6*

^ex-12-3

> [!example] Example §12.4: Using the Second Form
> Find the derivative of $f(x) = 1/\sqrt{x}$ at a number $a > 0$, using the form $f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$ of Definition §12.3.
>
> Clear the small fractions by multiplying by $\sqrt{x}\sqrt{a}$, then rationalize with $\sqrt{a} + \sqrt{x}$:
>
> $$
> \begin{aligned}
> f'(a) &= \lim_{x \to a} \frac{\dfrac{1}{\sqrt{x}} - \dfrac{1}{\sqrt{a}}}{x - a}
> = \lim_{x \to a} \frac{\dfrac{1}{\sqrt{x}} - \dfrac{1}{\sqrt{a}}}{x - a} \cdot \frac{\sqrt{x}\sqrt{a}}{\sqrt{x}\sqrt{a}}
> = \lim_{x \to a} \frac{\sqrt{a} - \sqrt{x}}{\sqrt{ax}\,(x - a)} \\
> &= \lim_{x \to a} \frac{\sqrt{a} - \sqrt{x}}{\sqrt{ax}\,(x - a)} \cdot \frac{\sqrt{a} + \sqrt{x}}{\sqrt{a} + \sqrt{x}}
> = \lim_{x \to a} \frac{-(x - a)}{\sqrt{ax}\,(x - a)\big(\sqrt{a} + \sqrt{x}\big)}
> = \lim_{x \to a} \frac{-1}{\sqrt{ax}\,\big(\sqrt{a} + \sqrt{x}\big)} \\
> &= \frac{-1}{\sqrt{a^2}\,\big(\sqrt{a} + \sqrt{a}\big)} = \frac{-1}{a \cdot 2\sqrt{a}} = -\frac{1}{2a^{3/2}} .
> \end{aligned}
> $$
>
> The last limit is by direct substitution, since $x \mapsto -1/\big(\sqrt{ax}(\sqrt a + \sqrt x)\big)$ is continuous at $a > 0$ ([[§10 Continuity#^thm-10-6|Theorem §10.6]]). The first form of the definition gives the same result.
>
> *Stewart: Example 2.7.5*

^ex-12-4

> [!theorem] Theorem §12.2: The Tangent Line Has Slope f′(a)
> The tangent line to $y = f(x)$ at $(a, f(a))$ is the line through $(a, f(a))$ whose slope is equal to $f'(a)$, the derivative of $f$ at $a$. In point-slope form, its equation is
>
> $$
> y - f(a) = f'(a)(x - a) .
> $$
>
> *Stewart: 2.7 (boxed text)*

^thm-12-2

> [!proof]+ Proof
> By Definition §12.1 the tangent line passes through $(a, f(a))$ and has slope $\lim_{x \to a} \frac{f(x) - f(a)}{x - a}$, which is $f'(a)$ by the second form in Definition §12.3. The line through $(x_1, y_1) = (a, f(a))$ with slope $m = f'(a)$ is $y - y_1 = m(x - x_1)$.

^pf-12-2

*Uses:* [[§12 Derivatives and Rates of Change#^def-12-1|Def. §12.1]], [[§12 Derivatives and Rates of Change#^def-12-3|Def. §12.3]]

## Rates of Change

> [!definition] Definition §12.4: Average and Instantaneous Rate of Change
> Let $y = f(x)$. If $x$ changes from $x_1$ to $x_2$, the change in $x$ (the **increment** of $x$) and the corresponding change in $y$ are
>
> $$
> \Delta x = x_2 - x_1, \qquad \Delta y = f(x_2) - f(x_1) .
> $$
>
> The difference quotient
>
> $$
> \frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}
> $$
>
> is the **average rate of change of $y$ with respect to $x$** over the interval $[x_1, x_2]$; it is the slope of the secant line through $P(x_1, f(x_1))$ and $Q(x_2, f(x_2))$. The limit of the average rates over smaller and smaller intervals,
>
> $$
> \text{instantaneous rate of change} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{x_2 \to x_1} \frac{f(x_2) - f(x_1)}{x_2 - x_1} ,
> $$
>
> is the **(instantaneous) rate of change of $y$ with respect to $x$** at $x = x_1$. By Definition §12.3 this limit is $f'(x_1)$. So:
>
> *The derivative $f'(a)$ is the instantaneous rate of change of $y = f(x)$ with respect to $x$ when $x = a$.*
>
> Its units are those of $\Delta y$ divided by those of $\Delta x$.
>
> *Stewart: 2.7, Equation 6, and boxed text*

^def-12-4

> [!remark] Remark: Two Readings of the Derivative
> The two interpretations, slope of the tangent and rate of change, are linked by the graph. Where $f'(a)$ is large the curve is steep and the $y$-values change rapidly; where $f'(a)$ is small the curve is relatively flat and the $y$-values change slowly. For a particle moving on a line with position $s = f(t)$, $f'(a)$ is the velocity at time $t = a$, and the **speed** is its absolute value $|f'(a)|$. Other rates of change: marginal cost (rate of change of production cost with respect to the number of items produced; if the cost of $x$ yards of fabric is $C = f(x)$ dollars, then $f'(1000) = 9$ means that the 1000th yard costs about \$9, in dollars per yard), power (rate of change of work with respect to time), rate of reaction (of concentration with respect to time), and growth rates of populations. Every problem about tangent lines is therefore also a problem about rates of change. More in [[§20 Rates of Change in the Natural and Social Sciences|§20]].

^rem-12-1

> [!example] Example §12.5: Estimating a Derivative from a Table
> Let $D(t)$ be the US national debt at time $t$, in billions of dollars (end-of-year estimates). Interpret and estimate $D'(2008)$.
>
> | $t$ | 2000 | 2004 | 2008 | 2012 | 2016 |
> |---|---|---|---|---|---|
> | $D(t)$ | 5662.2 | 7596.1 | 10,699.8 | 16,432.7 | 19,976.8 |
>
> $D'(2008)$ is the rate of change of $D$ with respect to $t$ when $t = 2008$: the rate at which the debt was increasing in 2008. By the second form of Definition §12.3,
>
> $$
> D'(2008) = \lim_{t \to 2008} \frac{D(t) - D(2008)}{t - 2008} .
> $$
>
> With only a table, compute the average rates of change (difference quotients) over the available intervals:
>
> | $t$ | interval | $\dfrac{D(t) - D(2008)}{t - 2008}$ |
> |---|---|---|
> | 2000 | $[2000, 2008]$ | $\dfrac{5662.2 - 10{,}699.8}{2000 - 2008} = \dfrac{-5037.6}{-8} = 629.7$ |
> | 2004 | $[2004, 2008]$ | $\dfrac{7596.1 - 10{,}699.8}{-4} \approx 775.93$ |
> | 2012 | $[2008, 2012]$ | $\dfrac{16{,}432.7 - 10{,}699.8}{4} \approx 1433.23$ |
> | 2016 | $[2008, 2016]$ | $\dfrac{19{,}976.8 - 10{,}699.8}{8} \approx 1159.63$ |
>
> Assuming the debt did not fluctuate wildly between 2004 and 2012, $D'(2008)$ lies between the two closest quotients, $775.93$ and $1433.23$. Their average is a good estimate:
>
> $$
> D'(2008) \approx \frac{775.93 + 1433.23}{2} \approx 1105 \text{ billion dollars per year} .
> $$
>
> The units of $\Delta D / \Delta t$, and hence of $D'(2008)$, are billions of dollars per year.
>
> *Stewart: Example 2.7.8*

^ex-12-5
