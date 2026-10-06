---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 15
stewart: "2.8"
aliases: ["Stewart 2.8"]
tags: [calculus]
---
← [[§14 Derivatives and Rates of Change]] · ↑ [[· 2 Limits and Derivatives]] · [[§16 The Parabola y = x², the CN Tower Ball, (√(t² + 9) − 3)∕t² and x³ − x]] →

*Stewart, Section 2.8.*

In [[§14 Derivatives and Rates of Change|§14]] the derivative was computed at one number $a$ at a time. Letting $a$ vary turns it into a new function $f'$, whose value at $x$ is the slope of the graph of $f$ at $(x, f(x))$. This section computes $f'$ from the definition for several functions, introduces the Leibniz notation $dy/dx$, and proves that differentiability implies continuity. The converse fails, and the section lists the three ways a function can fail to be differentiable: a corner, a discontinuity, a vertical tangent. Differentiating again gives the second and higher derivatives; the second derivative of position is acceleration.

## The Derivative Function

> [!definition] Definition §15.1: The Derivative Function
> Replacing the fixed number $a$ in [[§14 Derivatives and Rates of Change#^def-14-3|Definition §14.3]] by a variable $x$ gives
>
> $$
> f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} .
> $$
>
> To each number $x$ for which this limit exists we assign the number $f'(x)$. The function $f'$ so defined is the **derivative of $f$**: it is "derived" from $f$ by this limiting operation. Its domain is the set $\{x \mid f'(x) \text{ exists}\}$, which may be smaller than the domain of $f$. Geometrically, $f'(x)$ is the slope of the tangent line to the graph of $f$ at $(x, f(x))$ ([[§14 Derivatives and Rates of Change#^thm-14-2|Theorem §14.2]]).
>
> *Stewart: 2.8, Equation 2*

^def-15-1

> [!remark] Remark: Method — Computing and Sketching a Derivative
> **From a formula** ([[§15 The Derivative as a Function#^def-15-1|Definition §15.1]]):
> 1. Write the difference quotient $\dfrac{f(x + h) - f(x)}{h}$. During the limit, $h$ is the variable and $x$ is temporarily a constant.
> 2. Simplify until the factor $h$ in the denominator cancels: expand powers (polynomials, [[§15 The Derivative as a Function#^ex-15-1|Example §15.1]]), rationalize the numerator (roots, [[§15 The Derivative as a Function#^ex-15-2|Example §15.2]]), or combine fractions over a common denominator (rational functions, [[§15 The Derivative as a Function#^ex-15-3|Example §15.3]]).
> 3. Let $h \to 0$, usually by direct substitution.
> 4. State the domain of $f'$: the $x$ for which the limit exists.
>
> **From a graph** (Stewart, Example 2.8.1): at several points estimate the slope of the tangent line and plot it directly beneath as the $y$-value of $f'$. Where $f$ has a horizontal tangent, the graph of $f'$ crosses the $x$-axis; where $f$ is increasing (tangents of positive slope), $f'$ is above the axis; where $f$ is decreasing, below; and where $f$ is steepest, $|f'|$ is largest.

^rem-15-1

> [!example] Example §18.1: A Polynomial
> If $f(x) = x^3 - x$, find a formula for $f'(x)$.
>
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{h \to 0} \frac{\big[(x + h)^3 - (x + h)\big] - \big[x^3 - x\big]}{h} \\
> &= \lim_{h \to 0} \frac{x^3 + 3x^2 h + 3x h^2 + h^3 - x - h - x^3 + x}{h} = \lim_{h \to 0} \frac{3x^2 h + 3x h^2 + h^3 - h}{h} \\
> &= \lim_{h \to 0} \big(3x^2 + 3xh + h^2 - 1\big) = 3x^2 - 1 .
> \end{aligned}
> $$
>
> Check against the graphs: $f'(x) = 0$ at $x = \pm 1/\sqrt3$, exactly where the graph of $f$ has horizontal tangents, and $f'(x) > 0$ (for $|x| > 1/\sqrt3$) exactly where the tangents have positive slope.
>
> *Stewart: Example 2.8.2*

^ex-15-1

> [!example] Example §18.2: The Square Root
> If $f(x) = \sqrt{x}$, find the derivative of $f$ and state the domain of $f'$.
>
> Rationalize the numerator:
>
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h} = \lim_{h \to 0} \left( \frac{\sqrt{x + h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x + h} + \sqrt{x}}{\sqrt{x + h} + \sqrt{x}} \right) \\
> &= \lim_{h \to 0} \frac{(x + h) - x}{h\big(\sqrt{x + h} + \sqrt{x}\big)} = \lim_{h \to 0} \frac{1}{\sqrt{x + h} + \sqrt{x}} = \frac{1}{\sqrt{x} + \sqrt{x}} = \frac{1}{2\sqrt{x}} .
> \end{aligned}
> $$
>
> The last step needs $\sqrt{x} > 0$: then $h \mapsto 1/(\sqrt{x + h} + \sqrt{x})$ is continuous at $h = 0$. So $f'(x)$ exists for $x > 0$, and the domain of $f'$ is $(0, \infty)$, slightly smaller than the domain $[0, \infty)$ of $f$. (At $x = 0$ the quotient is $\sqrt{h}/h = 1/\sqrt{h} \to \infty$ as $h \to 0^+$.) The result is reasonable: near $0$, $f'(x)$ is very large, matching the steep tangent lines near $(0, 0)$; for large $x$, $f'(x)$ is small, matching the flatter tangents far to the right.
>
> *Stewart: Example 2.8.3*

^ex-15-2

> [!example] Example §18.3: A Rational Function
> Find $f'$ if $f(x) = \dfrac{1 - x}{2 + x}$.
>
> Combine the fractions with $\dfrac{a/b - c/d}{e} = \dfrac{ad - bc}{bd} \cdot \dfrac1e$:
>
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{\dfrac{1 - (x + h)}{2 + (x + h)} - \dfrac{1 - x}{2 + x}}{h}
> = \lim_{h \to 0} \frac{(1 - x - h)(2 + x) - (1 - x)(2 + x + h)}{h(2 + x + h)(2 + x)} \\
> &= \lim_{h \to 0} \frac{(2 - x - 2h - x^2 - xh) - (2 - x + h - x^2 - xh)}{h(2 + x + h)(2 + x)}
> = \lim_{h \to 0} \frac{-3h}{h(2 + x + h)(2 + x)} \\
> &= \lim_{h \to 0} \frac{-3}{(2 + x + h)(2 + x)} = -\frac{3}{(2 + x)^2} .
> \end{aligned}
> $$
>
> The formula holds at every $x \ne -2$, the whole domain of $f$.
>
> *Stewart: Example 2.8.4*

^ex-15-3

## Other Notations

> [!definition] Definition §15.2: Leibniz Notation and Differentiation Operators
> If $y = f(x)$, with independent variable $x$ and dependent variable $y$, the following all denote the derivative:
>
> $$
> f'(x) = y' = \frac{dy}{dx} = \frac{df}{dx} = \frac{d}{dx} f(x) = D f(x) = D_x f(x) .
> $$
>
> The symbols $D$ and $d/dx$ are **differentiation operators**: they indicate the operation of **differentiation**, the process of calculating a derivative. In Leibniz's notation the definition of the derivative ([[§14 Derivatives and Rates of Change#^def-14-4|Definition §14.4]]) reads
>
> $$
> \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} ,
> $$
>
> and the value at a specific number $a$ is written
>
> $$
> \left. \frac{dy}{dx} \right|_{x = a} \qquad\text{or}\qquad \left. \frac{dy}{dx} \right]_{x = a} ,
> $$
>
> a synonym for $f'(a)$; the vertical bar means "evaluate at". For the time being $dy/dx$ is not a ratio, only a synonym for $f'(x)$, though a very suggestive one.
>
> *Stewart: 2.8 (text)*

^def-15-2

> [!definition] Definition §15.3: Differentiable
> A function $f$ is **differentiable at $a$** if $f'(a)$ exists. It is **differentiable on an open interval** $(a, b)$ [or $(a, \infty)$ or $(-\infty, a)$ or $(-\infty, \infty)$] if it is differentiable at every number in the interval.
>
> *Stewart: 2.8, Definition 3*

^def-15-3

> [!example] Example §18.4: The Absolute Value
> Where is $f(x) = |x|$ differentiable?
>
> **For $x > 0$.** Then $|x| = x$, and for $h$ small enough $x + h > 0$, so $|x + h| = x + h$. Therefore
>
> $$
> f'(x) = \lim_{h \to 0} \frac{|x + h| - |x|}{h} = \lim_{h \to 0} \frac{(x + h) - x}{h} = \lim_{h \to 0} \frac{h}{h} = \lim_{h \to 0} 1 = 1 .
> $$
>
> **For $x < 0$.** Then $|x| = -x$, and for $h$ small enough $x + h < 0$, so $|x + h| = -(x + h)$ and
>
> $$
> f'(x) = \lim_{h \to 0} \frac{-(x + h) - (-x)}{h} = \lim_{h \to 0} \frac{-h}{h} = \lim_{h \to 0} (-1) = -1 .
> $$
>
> **At $x = 0$.** We must investigate
>
> $$
> f'(0) = \lim_{h \to 0} \frac{|0 + h| - |0|}{h} = \lim_{h \to 0} \frac{|h|}{h} \qquad\text{(if it exists).}
> $$
>
> The one-sided limits are
>
> $$
> \lim_{h \to 0^+} \frac{|h|}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1, \qquad \lim_{h \to 0^-} \frac{|h|}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1 .
> $$
>
> They differ, so $f'(0)$ does not exist ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]]). Hence $|x|$ is differentiable at every $x$ except $0$, with
>
> $$
> f'(x) = \begin{cases} 1 & \text{if } x > 0 \\ -1 & \text{if } x < 0 . \end{cases}
> $$
>
> Geometrically, the curve $y = |x|$ has no tangent line at $(0, 0)$: it has a corner there.
>
> *Stewart: Example 2.8.5*

^ex-15-4

> [!theorem] Theorem §18.1: Differentiable Implies Continuous
> If $f$ is differentiable at $a$, then $f$ is continuous at $a$.
>
> *Stewart: 2.8, Theorem 4*

^thm-15-1

> [!proof]+ Proof
> We must show $\lim_{x \to a} f(x) = f(a)$ ([[§12 Continuity#^def-12-1|Definition §12.1]]). We first show that the difference $f(x) - f(a)$ approaches $0$. The hypothesis is that
>
> $$
> f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
> $$
>
> exists (the second form of [[§14 Derivatives and Rates of Change#^def-14-3|Definition §14.3]]). To connect the given and the unknown, divide and multiply $f(x) - f(a)$ by $x - a$, which is allowed for $x \ne a$:
>
> $$
> f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \, (x - a) .
> $$
>
> Both factors have limits as $x \to a$, so by the Product Law (Limit Law 4),
>
> $$
> \lim_{x \to a} \big[f(x) - f(a)\big] = \lim_{x \to a} \frac{f(x) - f(a)}{x - a} \cdot \lim_{x \to a} (x - a) = f'(a) \cdot 0 = 0 .
> $$
>
> Now add and subtract $f(a)$, and use the Sum Law (Limit Law 1) and the limit of a constant (Law 8):
>
> $$
> \lim_{x \to a} f(x) = \lim_{x \to a} \big[f(a) + \big(f(x) - f(a)\big)\big] = \lim_{x \to a} f(a) + \lim_{x \to a} \big[f(x) - f(a)\big] = f(a) + 0 = f(a) .
> $$
>
> Therefore $f$ is continuous at $a$.

^pf-15-1

*Uses:* [[§14 Derivatives and Rates of Change#^def-14-3|Def. §14.3]], [[§12 Continuity#^def-12-1|Def. §12.1]], [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]], [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|§9.2]] (Limit Laws 1, 4 and 8)

> [!remark]- Connections
> - Rigorous treatment: [[§28 Basic Properties of the Derivative#^thm-28-1|451 Thm. §28.1]] (same proof), with the derivative defined in [[§28 Basic Properties of the Derivative#^def-28-1|451 Def. §28.1]]; the converse fails, [[§28 Basic Properties of the Derivative#^rem-28-1|451 Remark: The converse fails]].
> - Complex-variables version: [[§19 Derivatives#^thm-19-1|342 Thm. §19.1]] (a function with a complex derivative at $z_0$ is continuous there).

> [!remark] Remark: The Converse Is False
> There are functions that are continuous but not differentiable. For instance, $f(x) = |x|$ is continuous at $0$, because $\lim_{x \to 0} |x| = 0 = f(0)$ (Stewart's Example 2.3.7: both one-sided limits are $0$, so [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]] applies), but it is not differentiable at $0$ by [[§15 The Derivative as a Function#^ex-15-4|Example §15.4]]. Read in the [[Contrapositive, Converse and Inverse|contrapositive]], [[§15 The Derivative as a Function#^thm-15-1|Theorem §15.1]] gives a test: if $f$ is not continuous at $a$, then $f$ is not differentiable at $a$.

^rem-15-2

## How Can a Function Fail to Be Differentiable?

> [!definition] Definition §15.4: Vertical Tangent Line
> The curve $y = f(x)$ has a **vertical tangent line** at $x = a$ if $f$ is continuous at $a$ and
>
> $$
> \lim_{x \to a} |f'(x)| = \infty .
> $$
>
> The tangent lines become steeper and steeper as $x \to a$.
>
> *Stewart: 2.8 (text)*

^def-15-4

> [!remark] Remark: Three Ways to Fail
> A function $f$ fails to be differentiable at $a$ in each of the following situations.
> 1. **A corner** (or kink): the graph changes direction abruptly at $a$, as $|x|$ does at $0$ ([[§15 The Derivative as a Function#^ex-15-4|Example §15.4]]). In trying to compute $f'(a)$, the left and right limits of the difference quotient are different.
> 2. **A discontinuity**, for instance a jump discontinuity: by [[§15 The Derivative as a Function#^thm-15-1|Theorem §15.1]], $f$ is not differentiable where it is not continuous.
> 3. **A vertical tangent** ([[§15 The Derivative as a Function#^def-15-4|Definition §15.4]]): the difference quotients become infinite, as for $\sqrt[3]{x}$ at $0$, or for $\sqrt{x}$ at $0$ from the right ([[§15 The Derivative as a Function#^ex-15-2|Example §15.2]]).
>
> There is also a visual test. If $f$ is differentiable at $a$, then zooming in toward $(a, f(a))$ the graph straightens out and looks more and more like a line (its tangent line). At a corner, no amount of zooming removes the sharp point.

^rem-15-3

![[m233-13-1.svg]]
*The three ways for $f$ not to be differentiable at $a$. (a) A corner: the one-sided slopes $\lim_{h \to 0^\pm} \frac{f(a + h) - f(a)}{h}$ (dashed) differ. (b) A jump discontinuity: by [[§15 The Derivative as a Function#^thm-15-1|Theorem §15.1]] there can be no derivative. (c) A vertical tangent: $f$ is continuous at $a$, but the tangent lines (dashed) steepen without bound, here for a graph of the form $y = c + k\sqrt[3]{x - a}$.*

## Higher Derivatives

> [!definition] Definition §15.5: Higher Derivatives
> If $f$ is differentiable, its derivative $f'$ is a function that may have a derivative of its own, $(f')' = f''$, the **second derivative** of $f$. In Leibniz notation, for $y = f(x)$,
>
> $$
> \frac{d}{dx}\left( \frac{dy}{dx} \right) = \frac{d^2 y}{dx^2} .
> $$
>
> The **third derivative** is $f''' = (f'')'$, written $y''' = f'''(x) = \dfrac{d}{dx}\Big(\dfrac{d^2 y}{dx^2}\Big) = \dfrac{d^3 y}{dx^3}$. In general the **$n$th derivative** $f^{(n)}$ is obtained from $f$ by differentiating $n$ times:
>
> $$
> y^{(n)} = f^{(n)}(x) = \frac{d^n y}{dx^n} .
> $$
>
> For the position function $s = s(t)$ of an object moving in a straight line, the velocity is $v(t) = s'(t) = ds/dt$, the **acceleration** is the rate of change of velocity with respect to time,
>
> $$
> a(t) = v'(t) = s''(t), \qquad a = \frac{dv}{dt} = \frac{d^2 s}{dt^2} ,
> $$
>
> and the **jerk** is the rate of change of acceleration, $j = \dfrac{da}{dt} = \dfrac{d^3 s}{dt^3}$. (A large jerk means a sudden change in acceleration, an abrupt movement.)
>
> *Stewart: 2.8 (text)*

^def-15-5

$f''(x)$ is the slope of the curve $y = f'(x)$ at $(x, f'(x))$: the rate of change of the slope of the original curve, a rate of change of a rate of change. The second derivative's information about the shape of a graph is the subject of [[§30 What Derivatives Tell Us About the Shape of a Graph|§30]] ([[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-3|Theorem §30.3]], the Concavity Test).

> [!example] Example §18.5: Higher Derivatives of a Cubic
> If $f(x) = x^3 - x$, find and interpret $f''(x)$, and find $f'''(x)$ and $f^{(4)}(x)$.
>
> By [[§15 The Derivative as a Function#^ex-15-1|Example §15.1]], $f'(x) = 3x^2 - 1$. So
>
> $$
> \begin{aligned}
> f''(x) &= \lim_{h \to 0} \frac{f'(x + h) - f'(x)}{h} = \lim_{h \to 0} \frac{\big[3(x + h)^2 - 1\big] - \big[3x^2 - 1\big]}{h} \\
> &= \lim_{h \to 0} \frac{3x^2 + 6xh + 3h^2 - 1 - 3x^2 + 1}{h} = \lim_{h \to 0} (6x + 3h) = 6x .
> \end{aligned}
> $$
>
> $f''(x)$ is the slope of the parabola $y = f'(x)$: it is negative for $x < 0$, where $f'$ decreases, and positive for $x > 0$, where $f'$ increases. The graph $y = 6x$ of $f''$ is a line of slope $6$, so
>
> $$
> f'''(x) = \lim_{h \to 0} \frac{6(x + h) - 6x}{h} = 6
> $$
>
> for all $x$. Thus $f'''$ is a constant function, its graph a horizontal line, and $f^{(4)}(x) = 0$ for all $x$.
>
> *Stewart: Examples 2.8.6 and 2.8.7*

^ex-15-5
