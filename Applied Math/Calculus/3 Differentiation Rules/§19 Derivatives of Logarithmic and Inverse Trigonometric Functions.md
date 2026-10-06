---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 19
stewart: "3.6"
aliases: ["Stewart 3.6"]
tags: [calculus]
---
← [[§18 Implicit Differentiation]] · ↑ [[· 3 Differentiation Rules]] · [[§20 Rates of Change in the Natural and Social Sciences]] →

*Stewart, Section 3.6 · Appendix F.*

The logarithms and the inverse trigonometric functions are inverse functions ([[§5 Inverse Functions and Logarithms#^def-5-3|Definition §5.3]], [[§5 Inverse Functions and Logarithms#^def-5-5|Definitions §5.5]]–[[§5 Inverse Functions and Logarithms#^def-5-8|§5.8]]). An inverse of a differentiable function is differentiable wherever its graph has no vertical tangent, and once that is known, implicit differentiation ([[§18 Implicit Differentiation#^rem-18-1|Remark: Method — Implicit Differentiation]]) finds the derivative: $\ln x$ has derivative $1/x$, $\sin^{-1} x$ has derivative $1/\sqrt{1 - x^2}$, and so on. Logarithms also give a technique, *logarithmic differentiation*, for products, quotients and powers. With it Stewart proves the Power Rule for every real exponent, promised in [[§14 Derivatives of Polynomials and Exponential Functions|§14]] (after [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|Theorem §14.2]]), and differentiates functions such as $x^{\sqrt x}$ whose base and exponent both vary. The section also expresses $e$ as the limit $\lim_{x \to 0} (1 + x)^{1/x}$.

## Derivatives of Logarithmic Functions

> [!remark] Remark: Why It Works
> A differentiable function has a graph with no corner or cusp. The graph of $f^{-1}$ is the reflection of the graph of $f$ about the line $y = x$, so it has no corner or cusp either. Reflection swaps rise and run, so a tangent of slope $m$ at $(b, a)$ on the graph of $f$ becomes a tangent of slope $1/m$ at $(a, b)$ on the graph of $f^{-1}$. If $f$ has a horizontal tangent ($m = 0$), the reflected tangent is vertical, and $f^{-1}$ is not differentiable there.

^rem-19-1

> [!theorem] Theorem §19.1: Derivative of an Inverse Function
> Let $f$ be a one-to-one differentiable function on an open interval, with inverse function $f^{-1}$. If $f'(f^{-1}(a)) \ne 0$, then $f^{-1}$ is differentiable at $a$ and
>
> $$
> (f^{-1})'(a) = \frac{1}{f'(f^{-1}(a))} .
> $$
>
> *Stewart: 3.6 (text); proof in Appendix F*

^thm-19-1

> [!proof]+ Proof
> Let $b = f^{-1}(a)$, so $f(b) = a$. Write the definition of the derivative in the second form of [[§12 Derivatives and Rates of Change#^def-12-3|Definition §12.3]] (Equation 2.7.5):
>
> $$
> (f^{-1})'(a) = \lim_{x \to a} \frac{f^{-1}(x) - f^{-1}(a)}{x - a} .
> $$
>
> Put $y = f^{-1}(x)$, so $f(y) = x$. Since $f$ is differentiable, it is continuous, and so $f^{-1}$ is continuous ([[§10 Continuity#^thm-10-5|Theorem §10.5]]). Thus if $x \to a$, then $y = f^{-1}(x) \to f^{-1}(a) = b$. Also $y \ne b$ when $x \ne a$, because $f^{-1}$ is one-to-one. Therefore
>
> $$
> (f^{-1})'(a) = \lim_{x \to a} \frac{f^{-1}(x) - f^{-1}(a)}{x - a} = \lim_{x \to a} \frac{y - b}{f(y) - f(b)}
> = \lim_{y \to b} \frac{1}{\dfrac{f(y) - f(b)}{y - b}} = \frac{1}{\displaystyle\lim_{y \to b} \frac{f(y) - f(b)}{y - b}} = \frac{1}{f'(b)} = \frac{1}{f'(f^{-1}(a))} .
> $$
>
> The change from "$x \to a$" to "$y \to b$" in the third step needs a word (Stewart does not comment on it; his Appendix F also writes "$x \to b$" there, a misprint for $y \to b$). Let $G(y) = \dfrac{y - b}{f(y) - f(b)}$ for $y \ne b$ and $G(b) = \dfrac{1}{f'(b)}$. By Limit Law 5 (since $f'(b) \ne 0$), $\lim_{y \to b} G(y) = 1/f'(b) = G(b)$, so $G$ is continuous at $b$. Since $\lim_{x \to a} f^{-1}(x) = b$, [[§10 Continuity#^thm-10-7|Theorem §10.7]] gives $\lim_{x \to a} G(f^{-1}(x)) = G(b)$, and $G(f^{-1}(x))$ is exactly the difference quotient of $f^{-1}$ for $x \ne a$.

^pf-19-1

*Uses:* [[§12 Derivatives and Rates of Change#^def-12-3|Def. §12.3]] (definition of the derivative), [[§10 Continuity#^thm-10-5|§10.5]], [[§10 Continuity#^thm-10-7|§10.7]], [[§13 The Derivative as a Function#^thm-13-1|§13.1]] (differentiable implies continuous), [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Limit Law 5)

![[m233-19-1.svg]]
*[[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]] for $f(x) = e^x$ and $f^{-1}(x) = \ln x$. Reflection in $y = x$ carries the point $(1, e)$ to $(e, 1)$ and the tangent line of slope $f'(1) = e$ to a tangent line of slope $1/e$: rise and run trade places. So $(\ln)'(e) = 1/f'(\ln e) = 1/e$, as [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|Corollary §19.3]] confirms.*

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^thm-29-10|451 Thm. §29.10]] (the Inverse Function Theorem), with the same argument through the sequential definition of the limit. Its example $f(x) = x^3$ at $0$ shows why $f' \ne 0$ is needed.

The logarithmic function $y = \log_b x$ is the inverse of $y = b^x$, which is differentiable with derivative $b^x \ln b \ne 0$ ([[§17 The Chain Rule#^thm-17-5|Theorem §17.5]]; $b > 0$, $b \ne 1$). So by [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]] the logarithmic functions are differentiable.

> [!theorem] Theorem §19.2: Derivative of a Logarithmic Function
> For $b > 0$, $b \ne 1$ and $x > 0$,
>
> $$
> \frac{d}{dx}(\log_b x) = \frac{1}{x \ln b} .
> $$
>
> *Stewart: 3.6, Formula 1*

^thm-19-2

> [!proof]+ Proof
> Let $y = \log_b x$. Then $b^y = x$. Differentiate this equation implicitly with respect to $x$, using $\frac{d}{dy}(b^y) = b^y \ln b$ ([[§17 The Chain Rule#^thm-17-5|Theorem §17.5]]) and the Chain Rule:
>
> $$
> (b^y \ln b)\,\frac{dy}{dx} = 1, \qquad\text{so}\qquad \frac{dy}{dx} = \frac{1}{b^y \ln b} = \frac{1}{x \ln b} .
> $$

^pf-19-2

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|§19.1]], [[§17 The Chain Rule#^thm-17-5|§17.5]], [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§18 Implicit Differentiation#^rem-18-1|§18]] (implicit differentiation)

*From the integral definition of $\ln$ in Appendix G: [[§121 The Logarithm Defined as an Integral#^thm-121-11|Theorem §121.11]].*

> [!theorem] Corollary §19.3: Derivative of the Natural Logarithm
> $$
> \frac{d}{dx}(\ln x) = \frac{1}{x} .
> $$
>
> *Stewart: 3.6, Formula 2*

^cor-19-3

> [!proof]+ Proof
> Put $b = e$ in [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-2|Theorem §19.2]]: $\log_e x = \ln x$ and $\ln e = 1$.

^pf-19-3

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-2|§19.2]]

*Appendix G takes the integral $\int_1^x dt/t$ as the definition of $\ln x$, so that this formula holds by the Fundamental Theorem of Calculus: [[§121 The Logarithm Defined as an Integral#^thm-121-1|Theorem §121.1]].*

> [!remark]- Connections
> - Complex-variables version: [[§33 Branches and Derivatives of Logarithms#^thm-33-1|342 Thm. §33.1]] (each branch of $\log z$ is analytic, with derivative $1/z$).

Comparing [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-2|Theorem §19.2]] and [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|Corollary §19.3]] shows one of the main reasons that natural logarithms (base $e$) are used in calculus: the differentiation formula is simplest when $b = e$, because $\ln e = 1$.

> [!theorem] Corollary §19.4: The Logarithm of a Function
> If $u = g(x)$ is differentiable and positive, then
>
> $$
> \frac{d}{dx}(\ln u) = \frac1u\,\frac{du}{dx}, \qquad\text{or}\qquad \frac{d}{dx}[\ln g(x)] = \frac{g'(x)}{g(x)} .
> $$
>
> *Stewart: 3.6, Formula 3*

^cor-19-4

> [!proof]+ Proof
> With $y = \ln u$, the Chain Rule and [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|Corollary §19.3]] give $\dfrac{dy}{dx} = \dfrac{dy}{du}\,\dfrac{du}{dx} = \dfrac1u\,\dfrac{du}{dx}$. For example, $\dfrac{d}{dx}\ln(x^3 + 1) = \dfrac{1}{x^3 + 1}(3x^2) = \dfrac{3x^2}{x^3 + 1}$ (Stewart, Example 3.6.1).

^pf-19-4

*Uses:* [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|§19.3]]

> [!example] Example §19.1: Logarithm Outside, Logarithm Inside
> **(a)** Find $\dfrac{d}{dx}\ln(\sin x)$. The logarithm is the outer function, so by [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-4|Corollary §19.4]]
>
> $$
> \frac{d}{dx}\ln(\sin x) = \frac{1}{\sin x}\,\frac{d}{dx}(\sin x) = \frac{1}{\sin x}\cos x = \cot x .
> $$
>
> **(b)** Differentiate $f(x) = \sqrt{\ln x}$. Now the logarithm is the inner function, so
>
> $$
> f'(x) = \tfrac12 (\ln x)^{-1/2} \frac{d}{dx}(\ln x) = \frac{1}{2\sqrt{\ln x}} \cdot \frac1x = \frac{1}{2x\sqrt{\ln x}} .
> $$
>
> (Similarly, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-2|Theorem §19.2]] with $b = 10$ gives $\dfrac{d}{dx}\log_{10}(2 + \sin x) = \dfrac{\cos x}{(2 + \sin x)\ln 10}$.)
>
> *Stewart: Examples 3.6.2, 3.6.3 and 3.6.4*

^ex-19-1

> [!example] Example §19.2: Expand with the Laws of Logarithms First
> Find $\dfrac{d}{dx}\ln\dfrac{x + 1}{\sqrt{x - 2}}$.
>
> **Solution 1.** By [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-4|Corollary §19.4]] and the Quotient Rule,
>
> $$
> \begin{aligned}
> \frac{d}{dx}\ln\frac{x + 1}{\sqrt{x - 2}} &= \frac{\sqrt{x - 2}}{x + 1} \cdot \frac{\sqrt{x - 2} \cdot 1 - (x + 1)\big(\tfrac12\big)(x - 2)^{-1/2}}{x - 2} \\
> &= \frac{x - 2 - \frac12 (x + 1)}{(x + 1)(x - 2)} = \frac{x - 5}{2(x + 1)(x - 2)} ,
> \end{aligned}
> $$
>
> where the second step multiplies out $\sqrt{x - 2} \cdot \big[\sqrt{x - 2} - \tfrac12 (x + 1)(x - 2)^{-1/2}\big] = (x - 2) - \tfrac12 (x + 1)$.
>
> **Solution 2.** Expand first, using the laws of logarithms:
>
> $$
> \frac{d}{dx}\ln\frac{x + 1}{\sqrt{x - 2}} = \frac{d}{dx}\big[\ln(x + 1) - \tfrac12 \ln(x - 2)\big] = \frac{1}{x + 1} - \frac12 \left( \frac{1}{x - 2} \right) .
> $$
>
> Over the common denominator $2(x + 1)(x - 2)$ this is $\dfrac{2(x - 2) - (x + 1)}{2(x + 1)(x - 2)} = \dfrac{x - 5}{2(x + 1)(x - 2)}$, as in Solution 1.
>
> *Stewart: Example 3.6.5*

^ex-19-2

> [!theorem] Theorem §19.5: Derivative of ln|x|
> For all $x \ne 0$,
>
> $$
> \frac{d}{dx}\ln|x| = \frac1x .
> $$
>
> *Stewart: 3.6, Formula 4 (Example 3.6.6)*

^thm-19-5

> [!proof]+ Proof
> Since
>
> $$
> f(x) = \ln|x| = \begin{cases} \ln x & \text{if } x > 0 \\ \ln(-x) & \text{if } x < 0 \end{cases}
> $$
>
> it follows from Corollaries [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|§19.3]] and [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-4|§19.4]] that
>
> $$
> f'(x) = \begin{cases} \dfrac1x & \text{if } x > 0 \\[6pt] \dfrac{1}{-x}(-1) = \dfrac1x & \text{if } x < 0 . \end{cases}
> $$
>
> (On each side of $0$, $f$ agrees with one of the two formulas on an open interval, so it has the same derivative there.) Thus $f'(x) = 1/x$ for all $x \ne 0$.

^pf-19-5

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|§19.3]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-4|§19.4]]

## Logarithmic Differentiation

> [!remark] Remark: Method — Logarithmic Differentiation
> To differentiate a complicated product, quotient or power $y = f(x)$:
> 1. Take natural logarithms of both sides of $y = f(x)$ and use the Laws of Logarithms to expand the expression.
> 2. Differentiate implicitly with respect to $x$.
> 3. Solve the resulting equation for $y'$ and replace $y$ by $f(x)$.
>
> If $f(x) < 0$ for some values of $x$, then $\ln f(x)$ is not defined; take logarithms of $|y| = |f(x)|$ instead and use [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|Theorem §19.5]]. The left side differentiates to $y'/y$ in both cases.
>
> *Stewart: 3.6, Steps in Logarithmic Differentiation*

^rem-19-2

> [!example] Example §19.3: Logarithmic Differentiation
> Differentiate $y = \dfrac{x^{3/4}\sqrt{x^2 + 1}}{(3x + 2)^5}$.
>
> Take logarithms of both sides and use the Laws of Logarithms:
>
> $$
> \ln y = \tfrac34 \ln x + \tfrac12 \ln(x^2 + 1) - 5\ln(3x + 2) .
> $$
>
> Differentiate implicitly with respect to $x$:
>
> $$
> \frac1y\,\frac{dy}{dx} = \frac34 \cdot \frac1x + \frac12 \cdot \frac{2x}{x^2 + 1} - 5 \cdot \frac{3}{3x + 2} .
> $$
>
> Solve for $dy/dx$ and substitute the expression for $y$:
>
> $$
> \frac{dy}{dx} = y \left( \frac{3}{4x} + \frac{x}{x^2 + 1} - \frac{15}{3x + 2} \right) = \frac{x^{3/4}\sqrt{x^2 + 1}}{(3x + 2)^5} \left( \frac{3}{4x} + \frac{x}{x^2 + 1} - \frac{15}{3x + 2} \right) .
> $$
>
> Without logarithmic differentiation this would need the Quotient Rule and the Product Rule, and the calculation would be much longer.
>
> *Stewart: Example 3.6.7*

^ex-19-3

> [!theorem] Theorem §19.6: The Power Rule (General Version)
> If $n$ is any real number and $f(x) = x^n$, then
>
> $$
> f'(x) = n x^{n-1} .
> $$
>
> *Stewart: 3.1, The Power Rule (General Version); proved in 3.6*

^thm-19-6

> [!proof]+ Proof
> Let $y = x^n$ and use logarithmic differentiation with $|y|$:
>
> $$
> \ln|y| = \ln|x|^n = n\ln|x|, \qquad x \ne 0 .
> $$
>
> By [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|Theorem §19.5]] (with the Chain Rule on the left),
>
> $$
> \frac{y'}{y} = \frac{n}{x}, \qquad\text{hence}\qquad y' = n\,\frac{y}{x} = n\,\frac{x^n}{x} = n x^{n-1} .
> $$
>
> Differentiating $\ln|y|$ presupposes that $y$ is differentiable, which Stewart leaves implicit. For $x > 0$ it holds because $x^n = e^{n\ln x}$ is a composite of differentiable functions ([[§17 The Chain Rule#^cor-17-4|Corollary §17.4]]). For $x < 0$, where $x^n$ is defined only for special $n$ (such as $n = p/q$ with $q$ odd), $x^n = \pm|x|^n = \pm e^{n\ln|x|}$ with a fixed sign, again differentiable.
>
> At $x = 0$ (when $n > 1$), the definition of the derivative gives $f'(0) = \lim_{h \to 0} \dfrac{h^n - 0}{h} = \lim_{h \to 0} h^{n-1} = 0 = n \cdot 0^{n-1}$ directly.

^pf-19-6

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|§19.5]], [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§17 The Chain Rule#^cor-17-4|§17.4]], [[§13 The Derivative as a Function#^def-13-1|Def. §13.1]] (definition of $f'(x)$)

> [!remark] Remark: Bases and Exponents
> Distinguish the Power Rule $[(x^n)' = nx^{n-1}]$, where the base is variable and the exponent is constant, from the rule for exponential functions $[(b^x)' = b^x \ln b]$, where the base is constant and the exponent is variable. In general there are four cases:
> 1. Constant base, constant exponent: $\dfrac{d}{dx}(b^n) = 0$.
> 2. Variable base, constant exponent: $\dfrac{d}{dx}[f(x)]^n = n[f(x)]^{n-1} f'(x)$ ([[§17 The Chain Rule#^cor-17-3|Corollary §17.3]]).
> 3. Constant base, variable exponent: $\dfrac{d}{dx}\big[b^{g(x)}\big] = b^{g(x)}(\ln b)\,g'(x)$ ([[§17 The Chain Rule#^thm-17-5|Theorem §17.5]] and the Chain Rule).
> 4. Variable base, variable exponent: for $\dfrac{d}{dx}[f(x)]^{g(x)}$ use logarithmic differentiation, as in the next example.

^rem-19-3

> [!example] Example §19.4: Variable Base and Variable Exponent
> Differentiate $y = x^{\sqrt{x}}$ (for $x > 0$).
>
> **Solution 1 (logarithmic differentiation).**
>
> $$
> \ln y = \ln x^{\sqrt{x}} = \sqrt{x}\,\ln x, \qquad
> \frac{y'}{y} = \sqrt{x} \cdot \frac1x + (\ln x)\,\frac{1}{2\sqrt{x}} = \frac{1}{\sqrt{x}} + \frac{\ln x}{2\sqrt{x}} ,
> $$
>
> $$
> y' = y \left( \frac{1}{\sqrt{x}} + \frac{\ln x}{2\sqrt{x}} \right) = x^{\sqrt{x}} \left( \frac{2 + \ln x}{2\sqrt{x}} \right) .
> $$
>
> **Solution 2.** By Equation 1.5.10, $x^{\sqrt{x}} = e^{\sqrt{x}\ln x}$, so by [[§17 The Chain Rule#^cor-17-4|Corollary §17.4]]
>
> $$
> \frac{d}{dx}\big(x^{\sqrt{x}}\big) = e^{\sqrt{x}\ln x} \frac{d}{dx}\big(\sqrt{x}\ln x\big) = x^{\sqrt{x}} \left( \frac{2 + \ln x}{2\sqrt{x}} \right) ,
> $$
>
> computing $\frac{d}{dx}(\sqrt{x}\ln x)$ by the Product Rule as in Solution 1.
>
> *Stewart: Example 3.6.8*

^ex-19-4

## The Number e as a Limit

> [!theorem] Theorem §19.7: The Number e as a Limit
> $$
> e = \lim_{x \to 0} (1 + x)^{1/x} \qquad (5) \qquad\qquad\text{and}\qquad\qquad e = \lim_{n \to \infty} \left( 1 + \frac1n \right)^n . \qquad (6)
> $$
>
> A table of values of $(1 + x)^{1/x}$ for $x = 0.1, 0.01, \ldots, 0.00000001$ (the last is $2.71828181$) illustrates that, correct to seven decimal places, $e \approx 2.7182818$.
>
> *Stewart: 3.6, Formulas 5 and 6*

^thm-19-7

> [!proof]+ Proof
> Let $f(x) = \ln x$. By [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|Corollary §19.3]], $f'(x) = 1/x$, so $f'(1) = 1$. From the definition of the derivative,
>
> $$
> \begin{aligned}
> f'(1) &= \lim_{h \to 0} \frac{f(1 + h) - f(1)}{h} = \lim_{x \to 0} \frac{f(1 + x) - f(1)}{x} = \lim_{x \to 0} \frac{\ln(1 + x) - \ln 1}{x} \\
> &= \lim_{x \to 0} \frac1x \ln(1 + x) = \lim_{x \to 0} \ln(1 + x)^{1/x} .
> \end{aligned}
> $$
>
> So $\lim_{x \to 0} \ln(1 + x)^{1/x} = 1$. The exponential function is continuous, so by [[§10 Continuity#^thm-10-7|Theorem §10.7]] (Theorem 2.5.8),
>
> $$
> e = e^1 = e^{\lim_{x \to 0} \ln(1 + x)^{1/x}} = \lim_{x \to 0} e^{\ln(1 + x)^{1/x}} = \lim_{x \to 0} (1 + x)^{1/x} .
> $$
>
> This is Formula 5. For Formula 6, put $n = 1/x$: as $x \to 0^+$, $n \to \infty$, and $(1 + x)^{1/x} = (1 + 1/n)^n$. Since the two-sided limit (5) exists, so does the right-hand limit, and $\lim_{n \to \infty} (1 + 1/n)^n = \lim_{x \to 0^+} (1 + x)^{1/x} = e$.

^pf-19-7

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|§19.3]], [[§10 Continuity#^thm-10-7|§10.7]], [[§10 Continuity#^thm-10-6|§10.6]] (continuity of $e^x$), [[§11 Limits at Infinity; Horizontal Asymptotes#^def-11-4|Def. §11.4]] (limits at infinity)

*The same proof from the integral definition of $\ln$: [[§121 The Logarithm Defined as an Integral#^thm-121-12|Theorem §121.12]].*

> [!remark]- Connections
> - See also: [[§6 Modeling with First-Order Differential Equations#^prop-6-2|331 Prop. §6.2]] (the limit in the form $(1 + r/m)^{mt} \to e^{rt}$, for compound interest) and [[§10 Numerical Approximations꞉ Euler's Method#^prop-10-1|331 Prop. §10.1]], where the Euler approximation after $n$ steps contains the factor $(1 + a/n)^n$ and converges to the exact solution because $(1 + a/n)^n \to e^a$ (for $y' = y$, $y(0) = 1$ this is Euler's own approximation to $e^t$).

## Derivatives of Inverse Trigonometric Functions

The inverse trigonometric functions were defined in [[§5 Inverse Functions and Logarithms#^def-5-5|Definitions §5.5]]–[[§5 Inverse Functions and Logarithms#^def-5-8|§5.8]]. The trigonometric functions, restricted to the intervals used to define their inverses, are one-to-one and differentiable, so by [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]] the inverse trigonometric functions are differentiable (except where the tangents are vertical, at $x = \pm 1$ for $\sin^{-1}$ and $\cos^{-1}$). Implicit differentiation finds the derivatives.

> [!theorem] Theorem §19.8: Derivatives of Inverse Trigonometric Functions
> $$
> \begin{aligned}
> \frac{d}{dx}(\sin^{-1} x) &= \frac{1}{\sqrt{1 - x^2}} & \frac{d}{dx}(\csc^{-1} x) &= -\frac{1}{x\sqrt{x^2 - 1}} \\
> \frac{d}{dx}(\cos^{-1} x) &= -\frac{1}{\sqrt{1 - x^2}} & \frac{d}{dx}(\sec^{-1} x) &= \frac{1}{x\sqrt{x^2 - 1}} \\
> \frac{d}{dx}(\tan^{-1} x) &= \frac{1}{1 + x^2} & \frac{d}{dx}(\cot^{-1} x) &= -\frac{1}{1 + x^2}
> \end{aligned}
> $$
>
> for $|x| < 1$ in the first two and $|x| > 1$ for $\csc^{-1}$ and $\sec^{-1}$. The formulas for $\csc^{-1}$ and $\sec^{-1}$ depend on the definitions used for these functions (Stewart, Exercise 82); these are Stewart's definitions from Section 1.5.
>
> *Stewart: 3.6, Derivatives of Inverse Trigonometric Functions*

^thm-19-8

> [!proof]+ Proof
> **Arcsine.** $y = \sin^{-1} x$ means $\sin y = x$ and $-\pi/2 \le y \le \pi/2$. Differentiating $\sin y = x$ implicitly with respect to $x$,
>
> $$
> \cos y\,\frac{dy}{dx} = 1, \qquad \frac{dy}{dx} = \frac{1}{\cos y} .
> $$
>
> Now $\cos y \ge 0$ because $-\pi/2 \le y \le \pi/2$, so $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$. Therefore $\dfrac{dy}{dx} = \dfrac{1}{\sqrt{1 - x^2}}$ (for $|x| < 1$, where $\cos y > 0$).
>
> **Arctangent.** If $y = \tan^{-1} x$, then $\tan y = x$ with $-\pi/2 < y < \pi/2$. Differentiating implicitly,
>
> $$
> \sec^2 y\,\frac{dy}{dx} = 1, \qquad \frac{dy}{dx} = \frac{1}{\sec^2 y} = \frac{1}{1 + \tan^2 y} = \frac{1}{1 + x^2} .
> $$
>
> Stewart leaves the other four as exercises; they go the same way.
>
> **Arccosine.** $\cos y = x$ with $0 \le y \le \pi$ gives $-\sin y\,y' = 1$. On $[0, \pi]$, $\sin y \ge 0$, so $\sin y = \sqrt{1 - x^2}$ and $y' = -1/\sqrt{1 - x^2}$.
>
> **Arccosecant.** $\csc y = x$ with $y \in (0, \pi/2] \cup (\pi, 3\pi/2]$ gives $-\csc y \cot y\,y' = 1$. On these intervals $\cot y \ge 0$, so $\cot y = \sqrt{\csc^2 y - 1} = \sqrt{x^2 - 1}$ and $y' = -1/\big(x\sqrt{x^2 - 1}\big)$.
>
> **Arcsecant.** $\sec y = x$ with $y \in [0, \pi/2) \cup [\pi, 3\pi/2)$ gives $\sec y \tan y\,y' = 1$. On these intervals $\tan y \ge 0$, so $\tan y = \sqrt{\sec^2 y - 1} = \sqrt{x^2 - 1}$ and $y' = 1/\big(x\sqrt{x^2 - 1}\big)$.
>
> **Arccotangent.** $\cot y = x$ with $0 < y < \pi$ gives $-\csc^2 y\,y' = 1$, and $\csc^2 y = 1 + \cot^2 y = 1 + x^2$, so $y' = -1/(1 + x^2)$.

^pf-19-8

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|§19.1]], [[§16 Derivatives of Trigonometric Functions#^thm-16-4|§16.4]], [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§5 Inverse Functions and Logarithms#^def-5-5|Def. §5.5]]–[[§5 Inverse Functions and Logarithms#^def-5-8|§5.8]] (definitions of the inverse trigonometric functions)

> [!remark]- Connections
> - 451 uses $\arctan' = 1/(1 + x^2)$, obtained there from the Inverse Function Theorem, to find the power series of $\arctan$: [[§26 Differentiation and Integration of Power Series#^ex-26-3|451 Ex. §26.3]].
> - Complex-variables version: [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-3|342 Prop. §40.3]] (the same derivatives for branches of $\sin^{-1}z$, $\cos^{-1}z$ and $\tan^{-1}z$).

> [!example] Example §19.5: Inverse Trigonometric Functions in Combinations
> **(a)** Differentiate $y = \dfrac{1}{\sin^{-1} x}$. By the Chain Rule (power $-1$),
>
> $$
> \frac{dy}{dx} = \frac{d}{dx}(\sin^{-1} x)^{-1} = -(\sin^{-1} x)^{-2} \frac{d}{dx}(\sin^{-1} x) = -\frac{1}{(\sin^{-1} x)^2 \sqrt{1 - x^2}} .
> $$
>
> **(b)** Differentiate $f(x) = x\arctan\sqrt{x}$ ($\arctan$ is another notation for $\tan^{-1}$). By the Product Rule and the Chain Rule,
>
> $$
> f'(x) = x\,\frac{1}{1 + (\sqrt{x})^2} \left( \tfrac12 x^{-1/2} \right) + \arctan\sqrt{x} = \frac{\sqrt{x}}{2(1 + x)} + \arctan\sqrt{x} .
> $$
>
> **(c)** Differentiate $g(x) = \sec^{-1}(x^2)$. By the Chain Rule,
>
> $$
> g'(x) = \frac{1}{x^2 \sqrt{(x^2)^2 - 1}}\,(2x) = \frac{2}{x\sqrt{x^4 - 1}} .
> $$
>
> *Stewart: Examples 3.6.9 and 3.6.10*

^ex-19-5
