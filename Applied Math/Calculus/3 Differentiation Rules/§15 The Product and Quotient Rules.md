---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 15
stewart: "3.2"
aliases: ["Stewart 3.2"]
tags: [calculus]
---
← [[§14 Derivatives of Polynomials and Exponential Functions]] · ↑ [[· 3 Differentiation Rules]] · [[§16 Derivatives of Trigonometric Functions]] →

*Stewart, Section 3.2.*

The derivative of a sum is the sum of the derivatives ([[§14 Derivatives of Polynomials and Exponential Functions|§14]]), but the derivative of a product is *not* the product of the derivatives. This section finds the correct formulas for products and quotients. Both come from the same idea: write the change in $uv$ or $u/v$ in terms of the changes $\Delta u$ and $\Delta v$, divide by $\Delta x$, and let $\Delta x \to 0$. With them every rational function, and every product or quotient of functions with known derivatives, can be differentiated.

## The Product Rule

By analogy with the Sum Rule one might guess, as Leibniz first did, that $(fg)' = f'g'$. One example shows that this is wrong. Let $f(x) = x$ and $g(x) = x^2$. Then $f'(x) = 1$ and $g'(x) = 2x$, so $f'(x)g'(x) = 2x$. But $(fg)(x) = x^3$, so $(fg)'(x) = 3x^2$.

> [!theorem] Theorem §15.1: The Product Rule
> If $f$ and $g$ are both differentiable, then
>
> $$
> \frac{d}{dx}\big[f(x) g(x)\big] = f(x) \frac{d}{dx}\big[g(x)\big] + g(x) \frac{d}{dx}\big[f(x)\big] .
> $$
>
> In prime notation, $(fg)' = fg' + gf'$. In words: the derivative of a product of two functions is the first function times the derivative of the second plus the second function times the derivative of the first. With $u = f(x)$ and $v = g(x)$,
>
> $$
> \frac{d}{dx}(uv) = u \frac{dv}{dx} + v \frac{du}{dx} . \qquad (2)
> $$
>
> *Stewart: 3.2, The Product Rule and Equation 2*

^thm-15-1

> [!remark] Remark: Why It Works
> Suppose $u$ and $v$ are positive and read $uv$ as the area of a rectangle with sides $u$ and $v$. When $x$ changes by $\Delta x$, the sides change by $\Delta u$ and $\Delta v$, and the area grows by three pieces: a strip $u\,\Delta v$, a strip $v\,\Delta u$, and a corner $\Delta u\,\Delta v$ (figure below). The two strips give the two terms of the Product Rule. The corner is a product of two small changes, so it is negligible even after dividing by $\Delta x$.

^rem-15-1

![[m233-15-1.svg]]
*The change in the area $uv$ of a rectangle when its sides grow by $\Delta u$ and $\Delta v$: two strips $u\,\Delta v$ and $v\,\Delta u$ (blue and green) and a corner $\Delta u\,\Delta v$ (red). Divided by $\Delta x$, the strips tend to $u\,\frac{dv}{dx}$ and $v\,\frac{du}{dx}$, and the corner tends to $0 \cdot \frac{dv}{dx} = 0$.*

> [!proof]+ Proof
> Let $u = f(x)$ and $v = g(x)$, and let $x$ change by $\Delta x$. The corresponding changes in $u$ and $v$ are
>
> $$
> \Delta u = f(x + \Delta x) - f(x), \qquad \Delta v = g(x + \Delta x) - g(x) .
> $$
>
> The new value of the product is $(u + \Delta u)(v + \Delta v)$, so the change in the product is
>
> $$
> \Delta(uv) = (u + \Delta u)(v + \Delta v) - uv = u\,\Delta v + v\,\Delta u + \Delta u\,\Delta v . \qquad (1)
> $$
>
> This is pure algebra, valid whatever the signs of $u$, $v$, $\Delta u$ and $\Delta v$. Divide by $\Delta x$ and let $\Delta x \to 0$, using the Leibniz form $\dfrac{dy}{dx} = \lim_{\Delta x \to 0} \dfrac{\Delta y}{\Delta x}$ of the derivative:
>
> $$
> \begin{aligned}
> \frac{d}{dx}(uv) &= \lim_{\Delta x \to 0} \frac{\Delta(uv)}{\Delta x} = \lim_{\Delta x \to 0} \left( u \frac{\Delta v}{\Delta x} + v \frac{\Delta u}{\Delta x} + \Delta u \frac{\Delta v}{\Delta x} \right) \\
> &= u \lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x} + v \lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} + \Big( \lim_{\Delta x \to 0} \Delta u \Big) \Big( \lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x} \Big) \\
> &= u \frac{dv}{dx} + v \frac{du}{dx} + 0 \cdot \frac{dv}{dx} = u \frac{dv}{dx} + v \frac{du}{dx} .
> \end{aligned}
> $$
>
> The Limit Laws apply because each of the limits on the second line exists. In particular $\Delta u = f(x + \Delta x) - f(x) \to 0$ as $\Delta x \to 0$, because $f$ is differentiable at $x$ and therefore continuous there.

^pf-15-1

*Uses:* [[§13 The Derivative as a Function|§13]] (Leibniz notation; differentiable implies continuous, Theorem 2.8.4), [[§8 Calculating Limits Using the Limit Laws|§8]] (Limit Laws 1, 3, 4)

> [!remark]- Connections
> - Rigorous treatment: [[§28 Basic Properties of the Derivative#^thm-28-2|451 Thm. §28.2]], which proves the product rule by inserting the mixed term $f(a)g(x)$ and states the quotient rule.

> [!example] Example §15.1: The nth Derivative of x e^x
> (a) If $f(x) = xe^x$, find $f'(x)$. (b) Find the $n$th derivative $f^{(n)}(x)$.
>
> **(a)** By the Product Rule and $\frac{d}{dx}(e^x) = e^x$,
>
> $$
> f'(x) = x \frac{d}{dx}(e^x) + e^x \frac{d}{dx}(x) = xe^x + e^x \cdot 1 = (x + 1)e^x .
> $$
>
> **(b)** Using the Product Rule a second time,
>
> $$
> f''(x) = (x + 1) \frac{d}{dx}(e^x) + e^x \frac{d}{dx}(x + 1) = (x + 1)e^x + e^x \cdot 1 = (x + 2)e^x .
> $$
>
> Further applications give $f'''(x) = (x + 3)e^x$ and $f^{(4)}(x) = (x + 4)e^x$: each differentiation adds another term $e^x$. So
>
> $$
> f^{(n)}(x) = (x + n)e^x .
> $$
>
> (By induction on $n$: if $f^{(n)}(x) = (x + n)e^x$, then by the same computation as in (b), $f^{(n+1)}(x) = (x + n)e^x + e^x = (x + n + 1)e^x$.) Here the Product Rule is the only available method; Example §15.2 shows a case where it can be avoided.
>
> *Stewart: Example 3.2.1*

^ex-15-1

> [!example] Example §15.2: Simplify or Use the Product Rule
> Differentiate $f(t) = \sqrt{t}\,(a + bt)$, where $a$ and $b$ are constants.
>
> **Solution 1 (Product Rule).**
>
> $$
> \begin{aligned}
> f'(t) &= \sqrt{t} \frac{d}{dt}(a + bt) + (a + bt) \frac{d}{dt}\big(\sqrt{t}\big) = \sqrt{t} \cdot b + (a + bt) \cdot \tfrac12 t^{-1/2} \\
> &= b\sqrt{t} + \frac{a + bt}{2\sqrt{t}} = \frac{2bt + a + bt}{2\sqrt{t}} = \frac{a + 3bt}{2\sqrt{t}} .
> \end{aligned}
> $$
>
> **Solution 2 (simplify first).** By the laws of exponents, $f(t) = a\sqrt{t} + bt\sqrt{t} = at^{1/2} + bt^{3/2}$, so by the Power Rule
>
> $$
> f'(t) = \tfrac12 a t^{-1/2} + \tfrac32 b t^{1/2} .
> $$
>
> The two answers agree: $\dfrac{a + 3bt}{2\sqrt{t}} = \dfrac{a}{2\sqrt t} + \dfrac{3bt}{2\sqrt t} = \tfrac12 a t^{-1/2} + \tfrac32 b t^{1/2}$.
>
> *Stewart: Example 3.2.2*

^ex-15-2

> [!example] Example §15.3: Using Only Values of g and g′
> If $f(x) = \sqrt{x}\,g(x)$, where $g(4) = 2$ and $g'(4) = 3$, find $f'(4)$.
>
> Nothing is known about $g$ except these two numbers, and that is enough. By the Product Rule,
>
> $$
> f'(x) = \sqrt{x}\,g'(x) + g(x) \cdot \tfrac12 x^{-1/2} = \sqrt{x}\,g'(x) + \frac{g(x)}{2\sqrt{x}} ,
> $$
>
> so
>
> $$
> f'(4) = \sqrt4\,g'(4) + \frac{g(4)}{2\sqrt4} = 2 \cdot 3 + \frac{2}{2 \cdot 2} = 6.5 .
> $$
>
> *Stewart: Example 3.2.3*

^ex-15-3

## The Quotient Rule

> [!theorem] Theorem §15.2: The Quotient Rule
> If $f$ and $g$ are differentiable, then at every $x$ with $g(x) \ne 0$,
>
> $$
> \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x) \dfrac{d}{dx}\big[f(x)\big] - f(x) \dfrac{d}{dx}\big[g(x)\big]}{[g(x)]^2} .
> $$
>
> In prime notation, $\left(\dfrac{f}{g}\right)' = \dfrac{gf' - fg'}{g^2}$. In words: the derivative of a quotient is the denominator times the derivative of the numerator minus the numerator times the derivative of the denominator, all divided by the square of the denominator.
>
> *Stewart: 3.2, The Quotient Rule*

^thm-15-2

> [!proof]+ Proof
> Let $u = f(x)$ and $v = g(x)$ with $v \ne 0$, and let $x$, $u$ and $v$ change by $\Delta x$, $\Delta u$ and $\Delta v$. Since $g$ is differentiable at $x$, it is continuous there, so $\Delta v \to 0$ as $\Delta x \to 0$; in particular $v + \Delta v \ne 0$ for all small enough $\Delta x$ (Stewart leaves this implicit), and the quotient below is defined. The change in $u/v$ is
>
> $$
> \Delta\left(\frac{u}{v}\right) = \frac{u + \Delta u}{v + \Delta v} - \frac{u}{v} = \frac{(u + \Delta u)v - u(v + \Delta v)}{v(v + \Delta v)} = \frac{v\,\Delta u - u\,\Delta v}{v(v + \Delta v)} .
> $$
>
> Dividing by $\Delta x$,
>
> $$
> \frac{d}{dx}\left(\frac{u}{v}\right) = \lim_{\Delta x \to 0} \frac{\Delta(u/v)}{\Delta x} = \lim_{\Delta x \to 0} \frac{v \dfrac{\Delta u}{\Delta x} - u \dfrac{\Delta v}{\Delta x}}{v(v + \Delta v)} .
> $$
>
> The numerator tends to $v\,\frac{du}{dx} - u\,\frac{dv}{dx}$ and the denominator to $v \lim_{\Delta x \to 0}(v + \Delta v) = v^2 \ne 0$. By the Limit Laws (including Law 5 for the quotient),
>
> $$
> \frac{d}{dx}\left(\frac{u}{v}\right) = \frac{v \displaystyle\lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} - u \lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x}}{v \displaystyle\lim_{\Delta x \to 0} (v + \Delta v)} = \frac{v \dfrac{du}{dx} - u \dfrac{dv}{dx}}{v^2} .
> $$

^pf-15-2

*Uses:* [[§13 The Derivative as a Function|§13]] (Leibniz notation; differentiable implies continuous), [[§8 Calculating Limits Using the Limit Laws|§8]] (Limit Laws 1–5)

> [!theorem] Corollary §15.3: The Power Rule for Negative Integers
> If $n$ is a positive integer, then for $x \ne 0$
>
> $$
> \frac{d}{dx}\big(x^{-n}\big) = -n x^{-n-1} .
> $$
>
> So the Power Rule $\frac{d}{dx}(x^m) = mx^{m-1}$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|Theorem §14.2]]) holds for every integer $m$ (for $m = 0$ it is Theorem §14.1).
>
> *Stewart: 3.1 (text); Exercise 3.2.66(c)*

^cor-15-3

> [!proof]+ Proof
> Write $x^{-n} = \dfrac{1}{x^n}$ and apply the Quotient Rule with $f(x) = 1$, $g(x) = x^n$ (so $g(x) \ne 0$ for $x \ne 0$):
>
> $$
> \frac{d}{dx}\left(\frac{1}{x^n}\right) = \frac{x^n \cdot 0 - 1 \cdot n x^{n-1}}{(x^n)^2} = \frac{-n x^{n-1}}{x^{2n}} = -n x^{-n-1} .
> $$

^pf-15-3

*Uses:* [[§15 The Product and Quotient Rules#^thm-15-2|§15.2]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-1|§14.1]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|§14.2]]

With the Quotient Rule, every rational function can be differentiated.

> [!example] Example §15.4: A Rational Function
> Let $y = \dfrac{x^2 + x - 2}{x^3 + 6}$. Then
>
> $$
> \begin{aligned}
> y' &= \frac{(x^3 + 6) \dfrac{d}{dx}(x^2 + x - 2) - (x^2 + x - 2) \dfrac{d}{dx}(x^3 + 6)}{(x^3 + 6)^2}
> = \frac{(x^3 + 6)(2x + 1) - (x^2 + x - 2)(3x^2)}{(x^3 + 6)^2} \\
> &= \frac{(2x^4 + x^3 + 12x + 6) - (3x^4 + 3x^3 - 6x^2)}{(x^3 + 6)^2}
> = \frac{-x^4 - 2x^3 + 6x^2 + 12x + 6}{(x^3 + 6)^2} .
> \end{aligned}
> $$
>
> *Stewart: Example 3.2.4*

^ex-15-4

> [!example] Example §15.5: A Horizontal Tangent Line
> Find an equation of the tangent line to the curve $y = e^x/(1 + x^2)$ at the point $\big(1, \tfrac12 e\big)$.
>
> By the Quotient Rule,
>
> $$
> \frac{dy}{dx} = \frac{(1 + x^2) \dfrac{d}{dx}(e^x) - e^x \dfrac{d}{dx}(1 + x^2)}{(1 + x^2)^2}
> = \frac{(1 + x^2)e^x - e^x(2x)}{(1 + x^2)^2}
> = \frac{e^x(1 - 2x + x^2)}{(1 + x^2)^2} = \frac{e^x(1 - x)^2}{(1 + x^2)^2} .
> $$
>
> At $x = 1$ the factor $(1 - x)^2$ is $0$, so the slope is $\dfrac{dy}{dx}\Big|_{x=1} = 0$. The tangent line at $\big(1, \frac12 e\big)$ is horizontal: $y = \frac12 e$. (Since $dy/dx \ge 0$ everywhere, the curve rises, levels off at $x = 1$, and rises again.)
>
> *Stewart: Example 3.2.5*

^ex-15-5

> [!remark] Remark: Simplify First
> The Quotient Rule is not always the best route for a quotient. For example,
>
> $$
> F(x) = \frac{3x^2 + 2\sqrt{x}}{x}
> $$
>
> can be differentiated with the Quotient Rule, but it is much easier to divide first: $F(x) = 3x + 2x^{-1/2}$, so $F'(x) = 3 - x^{-3/2}$. Example §15.2 makes the same point for products.

^rem-15-2

> [!remark] Remark: Table of Differentiation Formulas
> Stewart's summary of the rules so far:
>
> | | | |
> |---|---|---|
> | $\dfrac{d}{dx}(c) = 0$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-1\|§14.1]]) | $\dfrac{d}{dx}(x^n) = nx^{n-1}$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2\|§14.2]]) | $\dfrac{d}{dx}(e^x) = e^x$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6\|§14.6]]) |
> | $(cf)' = cf'$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-3\|§14.3]]) | $(f + g)' = f' + g'$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-4\|§14.4]]) | $(f - g)' = f' - g'$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-4\|§14.4]]) |
> | $(fg)' = fg' + gf'$ ([[§15 The Product and Quotient Rules#^thm-15-1\|§15.1]]) | $\left(\dfrac{f}{g}\right)' = \dfrac{gf' - fg'}{g^2}$ ([[§15 The Product and Quotient Rules#^thm-15-2\|§15.2]]) | |

^rem-15-3
