---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 17
stewart: "3.1"
aliases: ["Stewart 3.1"]
tags: [calculus]
---
← [[§16 The Parabola y = x², the CN Tower Ball, (√(t² + 9) − 3)∕t² and x³ − x]] · ↑ [[· 3 Differentiation Rules]] · [[§18 The Product and Quotient Rules]] →

*Stewart, Section 3.1.*

Computing every derivative from the limit definition ([[§15 The Derivative as a Function|§15]]) is slow. This section starts a list of rules that replace the limit: constants have derivative $0$, $x^n$ has derivative $nx^{n-1}$, and differentiation respects constant multiples, sums and differences. Together they differentiate every polynomial. The section then turns to $b^x$: its derivative is proportional to $b^x$ itself, and the base $e$ is chosen to make the constant of proportionality $1$, so that $e^x$ is its own derivative.

## Constant Functions

> [!theorem] Theorem §20.1: Derivative of a Constant Function
> If $f(x) = c$ for a constant $c$, then $f'(x) = 0$. In Leibniz notation,
>
> $$
> \frac{d}{dx}(c) = 0 .
> $$
>
> *Stewart: 3.1, Derivative of a Constant Function*

^thm-17-1

> [!proof]+ Proof
> The graph of $f$ is the horizontal line $y = c$, which has slope $0$. Formally, from the definition of the derivative,
>
> $$
> f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{h \to 0} \frac{c - c}{h} = \lim_{h \to 0} 0 = 0 .
> $$

^pf-17-1

*Uses:* [[§15 The Derivative as a Function#^def-15-1|Def. §15.1]] (definition of $f'(x)$)

## Power Functions

For $f(x) = x$ the graph is the line $y = x$ of slope $1$, so $\frac{d}{dx}(x) = 1$ (Equation 1). In [[§15 The Derivative as a Function|§15]] ([[§15 The Derivative as a Function#^ex-15-1|Example §15.1]] and Stewart's Example 2.8.2) we found $\frac{d}{dx}(x^2) = 2x$ and $\frac{d}{dx}(x^3) = 3x^2$ (Equation 2). For $n = 4$, expanding $(x + h)^4$,

$$
\begin{aligned}
\frac{d}{dx}(x^4) &= \lim_{h \to 0} \frac{(x + h)^4 - x^4}{h} = \lim_{h \to 0} \frac{4x^3 h + 6x^2 h^2 + 4x h^3 + h^4}{h} \\
&= \lim_{h \to 0} \big(4x^3 + 6x^2 h + 4x h^2 + h^3\big) = 4x^3
\end{aligned}
$$

(Equation 3). The pattern is $nx^{n-1}$.

> [!theorem] Theorem §20.2: The Power Rule
> If $n$ is a positive integer, then
>
> $$
> \frac{d}{dx}(x^n) = n x^{n-1} .
> $$
>
> The cases $n = 1, 2, 3, 4$ are Equations 1–3 above.
>
> *Stewart: 3.1, The Power Rule (and Equations 1–3)*

^thm-17-2

> [!proof]+ Proof
> Stewart gives two proofs.
>
> **First proof.** Multiplying out the right-hand side (the terms telescope) verifies
>
> $$
> x^n - a^n = (x - a)\big(x^{n-1} + x^{n-2} a + \cdots + x a^{n-2} + a^{n-1}\big) .
> $$
>
> With $f(x) = x^n$ and the form $f'(a) = \lim_{x \to a} \dfrac{f(x) - f(a)}{x - a}$ of the derivative ([[§14 Derivatives and Rates of Change#^def-14-3|Definition §14.3]], Equation 2.7.5), cancel $x - a$ (allowed, since $x \ne a$ in the limit):
>
> $$
> \begin{aligned}
> f'(a) &= \lim_{x \to a} \frac{x^n - a^n}{x - a} = \lim_{x \to a} \big(x^{n-1} + x^{n-2} a + \cdots + x a^{n-2} + a^{n-1}\big) \\
> &= a^{n-1} + a^{n-2} a + \cdots + a\,a^{n-2} + a^{n-1} = n a^{n-1} .
> \end{aligned}
> $$
>
> The limit is found by direct substitution, since the bracket is a polynomial in $x$ ([[§12 Continuity#^thm-12-2|Theorem §12.2]]), and each of its $n$ terms becomes $a^{n-1}$.
>
> **Second proof.** By the Binomial Theorem ([[Binomial Theorem|250 Thm. §12.10]]),
>
> $$
> (x + h)^n = x^n + n x^{n-1} h + \frac{n(n-1)}{2} x^{n-2} h^2 + \cdots + n x h^{n-1} + h^n .
> $$
>
> So
>
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{(x + h)^n - x^n}{h} = \lim_{h \to 0} \frac{n x^{n-1} h + \frac{n(n-1)}{2} x^{n-2} h^2 + \cdots + n x h^{n-1} + h^n}{h} \\
> &= \lim_{h \to 0} \Big[ n x^{n-1} + \frac{n(n-1)}{2} x^{n-2} h + \cdots + n x h^{n-2} + h^{n-1} \Big] = n x^{n-1} ,
> \end{aligned}
> $$
>
> because every term except the first has $h$ as a factor and therefore tends to $0$.

^pf-17-2

*Uses:* [[§14 Derivatives and Rates of Change#^def-14-3|Def. §14.3]] (Equation 2.7.5), [[§15 The Derivative as a Function#^def-15-1|Def. §15.1]] (definition of $f'(x)$), [[§12 Continuity#^thm-12-2|§12.2]], [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]] (Limit Laws)

> [!remark]- Connections
> - Rigorous treatment: [[§28 Basic Properties of the Derivative#^ex-28-2|451 Ex. §28.2]], with the same factorization as the first proof.
> - Complex-variables version: [[§20 Rules for Differentiation#^thm-20-3|342 Thm. §20.3]] ($\frac{d}{dz} z^n = n z^{n-1}$ for positive integers $n$).

The rule holds for other exponents too. From the definition, $\frac{d}{dx}\big(\frac1x\big) = -\frac{1}{x^2}$ (Stewart, Exercise 69), that is, $\frac{d}{dx}(x^{-1}) = (-1)x^{-2}$. Every negative integer follows from the Quotient Rule ([[§18 The Product and Quotient Rules#^cor-18-3|Corollary §18.3]]). And $\frac{d}{dx}\sqrt{x} = \frac{1}{2\sqrt{x}}$ ([[§15 The Derivative as a Function#^ex-15-2|Example §15.2]]) says $\frac{d}{dx}(x^{1/2}) = \frac12 x^{-1/2}$. In fact:

**The Power Rule (General Version).** If $n$ is any real number, then $\dfrac{d}{dx}(x^n) = n x^{n-1}$.

This is proved with logarithmic differentiation in [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-6|Theorem §22.6]] (Stewart 3.6). It is used freely from here on.

> [!example] Example §20.1: Negative and Fractional Exponents
> Differentiate (a) $f(x) = \dfrac{1}{x^2}$ and (b) $y = \sqrt[3]{x^2}$.
>
> In each case, first rewrite the function as a power of $x$.
>
> **(a)** $f(x) = x^{-2}$, so with $n = -2$,
>
> $$
> f'(x) = \frac{d}{dx}(x^{-2}) = -2x^{-2-1} = -2x^{-3} = -\frac{2}{x^3} .
> $$
>
> **(b)** $y = x^{2/3}$, so with $n = \frac23$,
>
> $$
> \frac{dy}{dx} = \frac{d}{dx}\big(x^{2/3}\big) = \tfrac23 x^{(2/3) - 1} = \tfrac23 x^{-1/3} .
> $$
>
> The derivative $\frac23 x^{-1/3}$ is not defined at $0$: the graph of $y = \sqrt[3]{x^2}$ has a cusp there, and $y$ is not differentiable at $0$. Note also that $y' < 0$ for $x < 0$, where $y$ decreases, and $y' > 0$ for $x > 0$, where $y$ increases. That a function increases where its derivative is positive is proved in [[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-1|Theorem §30.1]].
>
> *Stewart: Example 3.1.2*

^ex-17-1

With the Power Rule, tangent lines no longer need the limit definition. A second line is also useful.

> [!definition] Definition §17.1: Normal Line
> The **normal line** to a curve $C$ at a point $P$ is the line through $P$ that is perpendicular to the tangent line at $P$. If the tangent line has slope $m \ne 0$, the normal line has slope $-1/m$.
>
> *Stewart: 3.1 (text)*

^def-17-1

> [!example] Example §20.2: Tangent and Normal Lines
> Find equations of the tangent line and the normal line to the curve $y = x\sqrt{x}$ at the point $(1, 1)$.
>
> Write $f(x) = x\sqrt{x} = x \cdot x^{1/2} = x^{3/2}$. By the Power Rule,
>
> $$
> f'(x) = \tfrac32 x^{(3/2) - 1} = \tfrac32 x^{1/2} = \tfrac32 \sqrt{x} .
> $$
>
> So the tangent line at $(1, 1)$ has slope $f'(1) = \frac32$, and its equation is
>
> $$
> y - 1 = \tfrac32 (x - 1) \qquad\text{or}\qquad y = \tfrac32 x - \tfrac12 .
> $$
>
> The normal line is perpendicular to the tangent line, so its slope is the negative reciprocal of $\frac32$, namely $-\frac23$:
>
> $$
> y - 1 = -\tfrac23 (x - 1) \qquad\text{or}\qquad y = -\tfrac23 x + \tfrac53 .
> $$
>
> *Stewart: Example 3.1.3*

^ex-17-2

## New Derivatives from Old

> [!remark] Remark: Why It Works
> Multiplying by $c$ stretches the graph of $f$ vertically by the factor $c$. Every rise is multiplied by $c$ while the runs stay the same, so every slope is multiplied by $c$.

^rem-17-1

> [!theorem] Theorem §20.3: The Constant Multiple Rule
> If $c$ is a constant and $f$ is a differentiable function, then
>
> $$
> \frac{d}{dx}\big[c f(x)\big] = c \frac{d}{dx} f(x) .
> $$
>
> *Stewart: 3.1, The Constant Multiple Rule*

^thm-17-3

> [!proof]+ Proof
> Let $g(x) = c f(x)$. Then
>
> $$
> \begin{aligned}
> g'(x) &= \lim_{h \to 0} \frac{g(x + h) - g(x)}{h} = \lim_{h \to 0} \frac{c f(x + h) - c f(x)}{h} = \lim_{h \to 0} c \left[ \frac{f(x + h) - f(x)}{h} \right] \\
> &= c \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = c f'(x) ,
> \end{aligned}
> $$
>
> where the limit of the difference quotient exists because $f$ is differentiable, so Limit Law 3 applies.

^pf-17-3

*Uses:* [[§15 The Derivative as a Function#^def-15-1|Def. §15.1]] (definition of $f'(x)$), [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]] (Limit Law 3)

For instance, $\frac{d}{dx}(3x^4) = 3 \cdot 4x^3 = 12x^3$, and $\frac{d}{dx}(-x) = \frac{d}{dx}[(-1)x] = (-1) \cdot 1 = -1$.

> [!theorem] Theorem §20.4: The Sum and Difference Rules
> If $f$ and $g$ are both differentiable, then
>
> $$
> \frac{d}{dx}\big[f(x) + g(x)\big] = \frac{d}{dx} f(x) + \frac{d}{dx} g(x), \qquad
> \frac{d}{dx}\big[f(x) - g(x)\big] = \frac{d}{dx} f(x) - \frac{d}{dx} g(x) .
> $$
>
> In prime notation: $(f + g)' = f' + g'$ and $(f - g)' = f' - g'$. The Sum Rule extends to any finite number of functions, e.g. $(f + g + h)' = [(f + g) + h]' = (f + g)' + h' = f' + g' + h'$.
>
> *Stewart: 3.1, The Sum and Difference Rules*

^thm-17-4

> [!proof]+ Proof
> **Sum Rule.** Let $F(x) = f(x) + g(x)$. Then
>
> $$
> \begin{aligned}
> F'(x) &= \lim_{h \to 0} \frac{[f(x + h) + g(x + h)] - [f(x) + g(x)]}{h} = \lim_{h \to 0} \left[ \frac{f(x + h) - f(x)}{h} + \frac{g(x + h) - g(x)}{h} \right] \\
> &= \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} + \lim_{h \to 0} \frac{g(x + h) - g(x)}{h} = f'(x) + g'(x)
> \end{aligned}
> $$
>
> by Limit Law 1, since both limits exist.
>
> **Difference Rule.** Write $f - g = f + (-1)g$ and apply the Sum Rule and the Constant Multiple Rule ([[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-3|Theorem §17.3]]): $(f - g)' = f' + (-1)g' = f' - g'$.
>
> **More terms.** Induction on the number of terms, grouping as in the statement.

^pf-17-4

*Uses:* [[§15 The Derivative as a Function#^def-15-1|Def. §15.1]] (definition of $f'(x)$), [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]] (Limit Law 1), [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-3|§17.3]]

> [!remark]- Connections
> - Rigorous treatment of the sum rule (and of the product and quotient rules, [[§18 The Product and Quotient Rules#^thm-18-1|Theorems §18.1]] and [[§18 The Product and Quotient Rules#^thm-18-2|§18.2]]): [[§28 Basic Properties of the Derivative#^thm-28-2|451 Thm. §28.2]].

Combining Theorems [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-1|§17.1]]–[[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-4|§17.4]] differentiates any polynomial term by term.

> [!example] Example §20.3: A Polynomial and Its Horizontal Tangents
> **(a)** By the Sum, Difference, Constant Multiple and Power Rules,
>
> $$
> \begin{aligned}
> \frac{d}{dx}\big(x^8 + 12x^5 - 4x^4 + 10x^3 - 6x + 5\big)
> &= \frac{d}{dx}(x^8) + 12\frac{d}{dx}(x^5) - 4\frac{d}{dx}(x^4) + 10\frac{d}{dx}(x^3) - 6\frac{d}{dx}(x) + \frac{d}{dx}(5) \\
> &= 8x^7 + 12(5x^4) - 4(4x^3) + 10(3x^2) - 6(1) + 0 \\
> &= 8x^7 + 60x^4 - 16x^3 + 30x^2 - 6 .
> \end{aligned}
> $$
>
> **(b)** Find the points on the curve $y = x^4 - 6x^2 + 4$ where the tangent line is horizontal.
>
> Horizontal tangents occur where the derivative is $0$:
>
> $$
> \frac{dy}{dx} = \frac{d}{dx}(x^4) - 6\frac{d}{dx}(x^2) + \frac{d}{dx}(4) = 4x^3 - 12x + 0 = 4x(x^2 - 3) .
> $$
>
> So $dy/dx = 0$ when $x = 0$ or $x^2 = 3$, that is, $x = 0, \pm\sqrt{3}$. Since $y(0) = 4$ and $y(\pm\sqrt3) = 9 - 18 + 4 = -5$, the curve has horizontal tangents at $(0, 4)$, $(\sqrt3, -5)$ and $(-\sqrt3, -5)$: a local maximum between two minima.
>
> *Stewart: Examples 3.1.5 and 3.1.6*

^ex-17-3

## Exponential Functions

Try the definition on $f(x) = b^x$ ($b > 0$). By the law $b^{x+h} = b^x b^h$ ([[§4 Exponential Functions#^thm-4-1|Theorem §4.1]]),

$$
f'(x) = \lim_{h \to 0} \frac{b^{x+h} - b^x}{h} = \lim_{h \to 0} \frac{b^x b^h - b^x}{h} = \lim_{h \to 0} \frac{b^x (b^h - 1)}{h} .
$$

The factor $b^x$ does not depend on $h$, so it comes out of the limit, and what remains is the derivative of $f$ at $0$:

$$
\lim_{h \to 0} \frac{b^h - 1}{h} = \lim_{h \to 0} \frac{b^{0+h} - b^0}{h} = f'(0) .
$$

> [!theorem] Theorem §20.5: Derivative of an Exponential Function
> If the exponential function $f(x) = b^x$ is differentiable at $0$, then it is differentiable everywhere and
>
> $$
> f'(x) = f'(0)\, b^x .
> $$
>
> The rate of change of an exponential function is proportional to the function itself: the slope is proportional to the height.
>
> *Stewart: 3.1, Equation 4*

^thm-17-5

> [!proof]+ Proof
> Suppose $f'(0) = \lim_{h \to 0} (b^h - 1)/h$ exists. For each fixed $x$, Limit Law 3 (with the constant $b^x$) gives
>
> $$
> \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{h \to 0} b^x \cdot \frac{b^h - 1}{h} = b^x \lim_{h \to 0} \frac{b^h - 1}{h} = b^x f'(0) .
> $$
>
> So the limit defining $f'(x)$ exists and equals $f'(0)\, b^x$.

^pf-17-5

*Uses:* [[§4 Exponential Functions#^thm-4-1|§4.1]] (laws of exponents), [[§15 The Derivative as a Function#^def-15-1|Def. §15.1]] (definition of $f'(x)$), [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]] (Limit Law 3)

> [!remark] Remark: The Constants for Base 2 and Base 3
> A table of values of $(b^h - 1)/h$ for $h = 0.1, 0.01, \ldots, 0.00001$ suggests (correct to three decimal places)
>
> $$
> \lim_{h \to 0} \frac{2^h - 1}{h} \approx 0.693, \qquad \lim_{h \to 0} \frac{3^h - 1}{h} \approx 1.099 ,
> $$
>
> so by [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-5|Theorem §17.5]],
>
> $$
> \frac{d}{dx}(2^x) \approx (0.693)\,2^x, \qquad \frac{d}{dx}(3^x) \approx (1.099)\,3^x \qquad (5)
> $$
>
> Stewart states that these limits exist ("it can be proved") without proof here. [[§20 The Chain Rule#^thm-20-5|Theorem §20.5]] identifies them: $f'(0) = \ln b$, so $\ln 2 \approx 0.693$ and $\ln 3 \approx 1.099$.

^rem-17-2

The simplest formula would have $f'(0) = 1$. Since $f'(0) < 1$ for $b = 2$ and $f'(0) > 1$ for $b = 3$, it is reasonable that some base between $2$ and $3$ gives exactly $1$. This is how $e$ was introduced in [[§4 Exponential Functions#^def-4-4|Definition §4.4]].

> [!definition] Definition §17.2: The Number e
> $e$ is the number such that
>
> $$
> \lim_{h \to 0} \frac{e^h - 1}{h} = 1 .
> $$
>
> Geometrically: of all exponential functions $y = b^x$, $y = e^x$ is the one whose tangent line at $(0, 1)$ has slope exactly $1$. Correct to five decimal places, $e \approx 2.71828$ (Stewart, Exercise 1, shows $2.7 < e < 2.8$).
>
> *Stewart: 3.1, Definition of the Number e*

^def-17-2

*Stewart asserts that such a number exists. Appendix G constructs $e$ as the number with $\ln e = 1$ ([[§144 The Logarithm Defined as an Integral#^def-144-2|Definition §144.2]]).*

![[m233-14-1.svg]]
*The exponential functions $2^x$, $e^x$ and $3^x$ all pass through $(0, 1)$. Their tangent lines there (dashed) have slopes $f'(0) \approx 0.693$, exactly $1$, and $\approx 1.099$. The number $e$ is the base for which the slope is exactly $1$; by [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-5|Theorem §17.5]] the slope of $b^x$ at every other point is then $f'(0)$ times the height.*

> [!theorem] Theorem §17.6: Derivative of the Natural Exponential Function
> $$
> \frac{d}{dx}(e^x) = e^x .
> $$
>
> So $e^x$ is its own derivative: the slope of the tangent line to $y = e^x$ at the point $(x, e^x)$ equals the $y$-coordinate of the point.
>
> *Stewart: 3.1, Derivative of the Natural Exponential Function*

^thm-17-6

> [!proof]+ Proof
> Take $b = e$ in [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-5|Theorem §17.5]]. By [[§17 Derivatives of Polynomials and Exponential Functions#^def-17-2|Definition §17.2]], $f'(0) = \lim_{h \to 0} (e^h - 1)/h = 1$ exists, so $f(x) = e^x$ is differentiable everywhere with $f'(x) = 1 \cdot e^x = e^x$.

^pf-17-6

*Uses:* [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-5|§17.5]], [[§17 Derivatives of Polynomials and Exponential Functions#^def-17-2|Def. §17.2]]

*From the integral definition of $\ln$: [[§144 The Logarithm Defined as an Integral#^thm-144-7|Theorem §144.7]].*

> [!example] Example §20.4: First and Second Derivatives
> If $f(x) = e^x - x$, find $f'$ and $f''$, and compare the graphs of $f$ and $f'$.
>
> By the Difference Rule and [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-6|Theorem §17.6]],
>
> $$
> f'(x) = \frac{d}{dx}(e^x) - \frac{d}{dx}(x) = e^x - 1 .
> $$
>
> The second derivative is the derivative of $f'$ ([[§15 The Derivative as a Function#^def-15-5|Definition §15.5]]):
>
> $$
> f''(x) = \frac{d}{dx}(e^x) - \frac{d}{dx}(1) = e^x .
> $$
>
> $f'(0) = e^0 - 1 = 0$, so $f$ has a horizontal tangent at $x = 0$. For $x > 0$, $e^x > 1$, so $f'(x) > 0$ and $f$ increases. For $x < 0$, $e^x < 1$, so $f'(x) < 0$ and $f$ decreases.
>
> *Stewart: Example 3.1.8*

^ex-17-4

> [!example] Example §20.5: A Tangent Line Parallel to a Given Line
> At what point on the curve $y = e^x$ is the tangent line parallel to the line $y = 2x$?
>
> Since $y = e^x$, $y' = e^x$. If the point has $x$-coordinate $a$, the tangent line there has slope $e^a$. It is parallel to $y = 2x$ exactly when the slopes agree:
>
> $$
> e^a = 2 \qquad\Longleftrightarrow\qquad a = \ln 2 .
> $$
>
> So the required point is $(a, e^a) = (\ln 2, 2)$.
>
> *Stewart: Example 3.1.9*

^ex-17-5
