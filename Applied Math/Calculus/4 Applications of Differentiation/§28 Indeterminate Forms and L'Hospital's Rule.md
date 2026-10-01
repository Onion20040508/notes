---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 28
stewart: "4.4"
aliases: ["Stewart 4.4"]
tags: [calculus]
---
← [[§27 What Derivatives Tell Us About the Shape of a Graph]] · ↑ [[· 4 Applications of Differentiation]] · [[§29 Summary of Curve Sketching]] →

*Stewart, Section 4.4.*

A limit such as $\lim_{x \to 1} \frac{\ln x}{x - 1}$ cannot be found with the Limit Laws, because numerator and denominator both tend to $0$, and cancelling a common factor does not work for it. L'Hospital's Rule handles such indeterminate forms of type $\frac00$ and $\frac{\infty}{\infty}$: under mild hypotheses, the limit of $f/g$ equals the limit of $f'/g'$. Its proof uses Cauchy's Mean Value Theorem, a version of the Mean Value Theorem ([[§26 The Mean Value Theorem#^thm-26-2|Theorem §26.2]]) for two functions. The other indeterminate forms, the products $0 \cdot \infty$, the differences $\infty - \infty$ and the powers $0^0$, $\infty^0$, $1^\infty$, are reduced to these two types by algebra or by taking logarithms.

## Indeterminate Forms (Types 0/0 and ∞/∞)

> [!definition] Definition §28.1: Indeterminate Forms of Type 0/0 and ∞/∞
> Consider a limit of the form
>
> $$
> \lim_{x \to a} \frac{f(x)}{g(x)} .
> $$
>
> If $f(x) \to 0$ and $g(x) \to 0$ as $x \to a$, this limit may or may not exist, and it is called an **indeterminate form of type $\frac00$**. If $f(x) \to \infty$ (or $-\infty$) and $g(x) \to \infty$ (or $-\infty$), it is called an **indeterminate form of type $\frac{\infty}{\infty}$**.
>
> *Stewart: 4.4 (text)*

^def-28-1

Some limits of these types were found earlier by algebra. For rational functions one cancels common factors, $\lim_{x \to 1} \frac{x^2 - x}{x^2 - 1} = \lim_{x \to 1} \frac{x}{x + 1} = \frac12$ ([[§8 Calculating Limits Using the Limit Laws#^thm-8-4|Theorem §8.4]]), or divides by the highest power of $x$ in the denominator, $\lim_{x \to \infty} \frac{x^2 - 1}{2x^2 + 1} = \lim_{x \to \infty} \frac{1 - 1/x^2}{2 + 1/x^2} = \frac12$ ([[§11 Limits at Infinity; Horizontal Asymptotes#^rem-11-2|Remark: Method — Limits at Infinity of Algebraic Expressions]]). A geometric argument gave $\lim_{x \to 0} \frac{\sin x}{x} = 1$ ([[§16 Derivatives of Trigonometric Functions#^thm-16-6|Theorem §16.6]]). None of these methods works for $\lim_{x \to 1} \frac{\ln x}{x - 1}$ or $\lim_{x \to \infty} \frac{\ln x}{x - 1}$. In a limit of type $\frac{\infty}{\infty}$ there is a contest: if the numerator grows significantly faster the limit is $\infty$, if the denominator does it is $0$, and there may be a compromise at a finite positive number.

## L'Hospital's Rule

The proof of l'Hospital's Rule, given in Stewart's Appendix F, rests on a generalization of the Mean Value Theorem to two functions, due to Cauchy. We state and prove it first.

> [!theorem] Theorem §28.1: Cauchy's Mean Value Theorem
> Suppose that the functions $f$ and $g$ are continuous on $[a, b]$ and differentiable on $(a, b)$, and $g'(x) \ne 0$ for all $x$ in $(a, b)$. Then there is a number $c$ in $(a, b)$ such that
>
> $$
> \frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)} .
> $$
>
> With $g(x) = x$, so that $g'(c) = 1$, this is the ordinary Mean Value Theorem.
>
> *Stewart: Appendix F, Theorem 1*

^thm-28-1

> [!proof]+ Proof
> Stewart: "proved in a similar manner" to the Mean Value Theorem, with a different auxiliary function. First, $g(b) \ne g(a)$, so the right side makes sense. (Stewart does not mention this; here is why.) If $g(b) = g(a)$, then Rolle's Theorem applied to $g$ would give a number in $(a, b)$ where $g' = 0$, contrary to the hypothesis. Now let
>
> $$
> h(x) = f(x) - f(a) - \frac{f(b) - f(a)}{g(b) - g(a)}\,[g(x) - g(a)] .
> $$
>
> $h$ is continuous on $[a, b]$ and differentiable on $(a, b)$, since $f$ and $g$ are and the other terms are constants. Also $h(a) = 0$ and
>
> $$
> h(b) = f(b) - f(a) - \frac{f(b) - f(a)}{g(b) - g(a)}\,[g(b) - g(a)] = 0 .
> $$
>
> By Rolle's Theorem there is $c \in (a, b)$ with
>
> $$
> 0 = h'(c) = f'(c) - \frac{f(b) - f(a)}{g(b) - g(a)}\,g'(c) .
> $$
>
> Dividing by $g'(c) \ne 0$ gives the formula.

^pf-28-1

*Uses:* [[§26 The Mean Value Theorem#^thm-26-1|§26.1]] (Rolle's Theorem, twice)

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^thm-29-2|451 Thm. §29.2]] gives Rolle's Theorem; the two-function theorem is [[§30 L'Hospital's Rule#^thm-30-2|451 Thm. §30.2]] (Generalized Mean Value Theorem), stated there in the symmetric form $(f(b) - f(a))\,g'(c) = (g(b) - g(a))\,f'(c)$, which needs no hypothesis on $g'$.

> [!theorem] Theorem §28.2: L'Hospital's Rule
> Suppose $f$ and $g$ are differentiable and $g'(x) \ne 0$ on an open interval $I$ that contains $a$ (except possibly at $a$). Suppose that
>
> $$
> \lim_{x \to a} f(x) = 0 \quad\text{and}\quad \lim_{x \to a} g(x) = 0
> $$
>
> or that
>
> $$
> \lim_{x \to a} f(x) = \pm\infty \quad\text{and}\quad \lim_{x \to a} g(x) = \pm\infty .
> $$
>
> (In other words, we have an indeterminate form of type $\frac00$ or $\frac{\infty}{\infty}$.) Then
>
> $$
> \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
> $$
>
> if the limit on the right side exists (or is $\infty$ or $-\infty$).
>
> The rule is also valid for one-sided limits and for limits at infinity or negative infinity: "$x \to a$" can be replaced by any of $x \to a^+$, $x \to a^-$, $x \to \infty$, $x \to -\infty$.
>
> *Stewart: 4.4, L'Hospital's Rule and Note 2; proof in Appendix F*

^thm-28-2

> [!remark] Remark: Why It Works
> Suppose $f(a) = g(a) = 0$. Zooming in toward the point $(a, 0)$, the graphs of $f$ and $g$ look almost linear, like their tangent lines $y = f'(a)(x - a)$ and $y = g'(a)(x - a)$. If they actually were linear, their ratio would be $\frac{f'(a)(x - a)}{g'(a)(x - a)} = \frac{f'(a)}{g'(a)}$, the ratio of the derivatives.
>
> This becomes a proof in a special case (Stewart's Note 3): $f(a) = g(a) = 0$, $f'$ and $g'$ continuous, and $g'(a) \ne 0$. Then, by continuity of $f'$ and $g'$ and the alternative form of the definition of the derivative ([[§12 Derivatives and Rates of Change#^def-12-3|Def. §12.3]]),
>
> $$
> \lim_{x \to a} \frac{f'(x)}{g'(x)} = \frac{f'(a)}{g'(a)}
> = \frac{\displaystyle\lim_{x \to a} \frac{f(x) - f(a)}{x - a}}{\displaystyle\lim_{x \to a} \frac{g(x) - g(a)}{x - a}}
> = \lim_{x \to a} \frac{f(x) - f(a)}{g(x) - g(a)}
> = \lim_{x \to a} \frac{f(x)}{g(x)} ,
> $$
>
> using the Quotient Law and $f(a) = g(a) = 0$. The general version needs Cauchy's Mean Value Theorem.

^rem-28-1

> [!proof]+ Proof
> Stewart proves the case of type $\frac00$.
>
> **Finite $a$.** Assume $\lim_{x \to a} f(x) = 0 = \lim_{x \to a} g(x)$, and let $L = \lim_{x \to a} \frac{f'(x)}{g'(x)}$. We must show that $\lim_{x \to a} \frac{f(x)}{g(x)} = L$. Define
>
> $$
> F(x) = \begin{cases} f(x) & \text{if } x \ne a \\ 0 & \text{if } x = a \end{cases}
> \qquad\qquad
> G(x) = \begin{cases} g(x) & \text{if } x \ne a \\ 0 & \text{if } x = a . \end{cases}
> $$
>
> Then $F$ is continuous on $I$: $f$ is continuous on $\{x \in I \mid x \ne a\}$ (it is differentiable there), and $\lim_{x \to a} F(x) = \lim_{x \to a} f(x) = 0 = F(a)$. Likewise $G$ is continuous on $I$.
>
> Let $x \in I$ with $x > a$. Then $F$ and $G$ are continuous on $[a, x]$ and differentiable on $(a, x)$, with $F' = f'$, $G' = g'$, and $G' \ne 0$ there. By Cauchy's Mean Value Theorem there is a number $y$ with $a < y < x$ and
>
> $$
> \frac{F'(y)}{G'(y)} = \frac{F(x) - F(a)}{G(x) - G(a)} = \frac{F(x)}{G(x)} ,
> $$
>
> since $F(a) = G(a) = 0$. (In particular $g(x) = G(x) \ne 0$, by the first step of that proof.) So $\frac{f(x)}{g(x)} = \frac{f'(y)}{g'(y)}$. If we let $x \to a^+$, then $y \to a^+$ (since $a < y < x$), so
>
> $$
> \lim_{x \to a^+} \frac{f(x)}{g(x)} = \lim_{x \to a^+} \frac{F(x)}{G(x)} = \lim_{y \to a^+} \frac{F'(y)}{G'(y)} = \lim_{y \to a^+} \frac{f'(y)}{g'(y)} = L .
> $$
>
> (Stewart passes from $x$ to $y$ in one step; in detail, for finite $L$: given $\varepsilon > 0$, choose $\delta > 0$ such that $\big|\frac{f'(t)}{g'(t)} - L\big| < \varepsilon$ for $a < t < a + \delta$. If $a < x < a + \delta$, the number $y$ belonging to $x$ also satisfies $a < y < a + \delta$, so $\big|\frac{f(x)}{g(x)} - L\big| = \big|\frac{f'(y)}{g'(y)} - L\big| < \varepsilon$. For $L = \pm\infty$ replace "within $\varepsilon$ of $L$" by "$> M$" or "$< -M$".)
>
> A similar argument, with $x < a$ and Cauchy's Mean Value Theorem on $[x, a]$, shows that the left-hand limit is also $L$. Therefore $\lim_{x \to a} \frac{f(x)}{g(x)} = L$. The argument for each side used the hypotheses only on that side of $a$, so it also proves the one-sided versions.
>
> **Infinite $a$.** Let $t = 1/x$. Then $t \to 0^+$ as $x \to \infty$. The functions $f(1/t)$ and $g(1/t)$ tend to $0$ as $t \to 0^+$ and, by the Chain Rule, are differentiable for small $t > 0$ with derivatives $f'(1/t)(-1/t^2)$ and $g'(1/t)(-1/t^2) \ne 0$. So the one-sided rule for finite $a$ (at $0^+$) applies:
>
> $$
> \lim_{x \to \infty} \frac{f(x)}{g(x)} = \lim_{t \to 0^+} \frac{f(1/t)}{g(1/t)}
> = \lim_{t \to 0^+} \frac{f'(1/t)(-1/t^2)}{g'(1/t)(-1/t^2)}
> = \lim_{t \to 0^+} \frac{f'(1/t)}{g'(1/t)} = \lim_{x \to \infty} \frac{f'(x)}{g'(x)} .
> $$
>
> The case $x \to -\infty$ is the same with $t \to 0^-$.

^pf-28-2

*Uses:* [[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-1|§28.1]], [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]], [[§13 The Derivative as a Function#^thm-13-1|§13.1]] (differentiable implies continuous), [[§17 The Chain Rule#^thm-17-2|§17.2]]

*Stewart proves only the type $\frac00$ (his Appendix F proof assumes $f, g \to 0$ and says nothing about the other type). The type $\frac{\infty}{\infty}$ needs a different estimate (Cauchy's theorem on $[x, x_1]$ with $x_1$ fixed near $a$, then $x \to a$); it is proved neither in Stewart nor elsewhere in the vault: [[§30 L'Hospital's Rule#^thm-30-1|451 Thm. §30.1]] states it, in the stronger form that only the denominator needs to tend to infinity, but proves only the type $\frac00$.*

![[m233-28-1.svg]]
*Why l'Hospital's Rule is plausible. Near $(a, 0)$ the graphs of $f$ (red) and $g$ (blue) are close to their tangent lines $y = m_1(x - a)$ and $y = m_2(x - a)$ (dashed), where $m_1 = f'(a)$ and $m_2 = g'(a)$. For the lines, the ratio of heights above any $x$ is $m_1/m_2$, the ratio of the derivatives.*

> [!remark]- Connections
> - Rigorous treatment: [[§30 L'Hospital's Rule#^thm-30-1|451 Thm. §30.1]], with an $\varepsilon$-proof of the case $\frac00$, $x \to a^-$, by the same route (Generalized Mean Value Theorem, then letting the second point tend to $a$).

> [!remark] Remark: Using the Rule Correctly
> - Differentiate the numerator and the denominator **separately**. Do not use the Quotient Rule.
> - **Check the form first.** The rule says nothing about limits that are not indeterminate. For example, as $x \to \pi^-$, $\sin x \to 0$ but $1 - \cos x \to 2$, so $\frac{\sin x}{1 - \cos x}$ is not indeterminate. Blindly differentiating would give $\lim_{x \to \pi^-} \frac{\cos x}{\sin x} = -\infty$, which is **wrong**. Since the function is continuous at $\pi$ and the denominator is nonzero there, direct substitution gives the correct value: $\frac{\sin \pi}{1 - \cos \pi} = \frac{0}{1 - (-1)} = 0$ (Stewart's Example 4.4.5).
> - Some limits can be found by l'Hospital's Rule but are more easily found by other methods (factoring, dividing by the highest power, known limits). Consider those first.

^rem-28-2

> [!example] Example §28.1: Types 0/0 and ∞/∞
> **(a)** Find $\displaystyle\lim_{x \to 1} \frac{\ln x}{x - 1}$.
>
> Since $\lim_{x \to 1} \ln x = \ln 1 = 0$ and $\lim_{x \to 1}(x - 1) = 0$, this is of type $\frac00$, and l'Hospital's Rule gives
>
> $$
> \lim_{x \to 1} \frac{\ln x}{x - 1} = \lim_{x \to 1} \frac{\frac{d}{dx}(\ln x)}{\frac{d}{dx}(x - 1)} = \lim_{x \to 1} \frac{1/x}{1} = \lim_{x \to 1} \frac{1}{x} = 1 .
> $$
>
> **(b)** Calculate $\displaystyle\lim_{x \to \infty} \frac{e^x}{x^2}$.
>
> $e^x \to \infty$ and $x^2 \to \infty$, so this is of type $\frac{\infty}{\infty}$:
>
> $$
> \lim_{x \to \infty} \frac{e^x}{x^2} = \lim_{x \to \infty} \frac{e^x}{2x} .
> $$
>
> The right side is again of type $\frac{\infty}{\infty}$, so apply the rule a second time:
>
> $$
> \lim_{x \to \infty} \frac{e^x}{x^2} = \lim_{x \to \infty} \frac{e^x}{2x} = \lim_{x \to \infty} \frac{e^x}{2} = \infty .
> $$
>
> **(c)** Calculate $\displaystyle\lim_{x \to \infty} \frac{\ln x}{\sqrt{x}}$.
>
> $\ln x \to \infty$ and $\sqrt{x} \to \infty$, so
>
> $$
> \lim_{x \to \infty} \frac{\ln x}{\sqrt{x}} = \lim_{x \to \infty} \frac{1/x}{\frac12 x^{-1/2}} = \lim_{x \to \infty} \frac{1/x}{1/(2\sqrt{x})} .
> $$
>
> This is now of type $\frac00$, but instead of a second application, simplify:
>
> $$
> \lim_{x \to \infty} \frac{1/x}{1/(2\sqrt{x})} = \lim_{x \to \infty} \frac{2\sqrt{x}}{x} = \lim_{x \to \infty} \frac{2}{\sqrt{x}} = 0 .
> $$
>
> Both (b) and (c) are of type $\frac{\infty}{\infty}$, with opposite outcomes. In (b) the numerator $e^x$ grows significantly faster than $x^2$; in fact $e^x$ grows faster than every power $x^n$. In (c) the denominator $\sqrt{x}$ outpaces $\ln x$.
>
> *Stewart: Examples 4.4.1, 4.4.2 and 4.4.3*

^ex-28-1

> [!example] Example §28.2: Repeated Application, with Simplification
> Find $\displaystyle\lim_{x \to 0} \frac{\tan x - x}{x^3}$.
>
> Both $\tan x - x \to 0$ and $x^3 \to 0$ as $x \to 0$, so
>
> $$
> \lim_{x \to 0} \frac{\tan x - x}{x^3} = \lim_{x \to 0} \frac{\sec^2 x - 1}{3x^2} .
> $$
>
> This is still of type $\frac00$ (since $\sec^2 0 = 1$), so apply the rule again:
>
> $$
> \lim_{x \to 0} \frac{\sec^2 x - 1}{3x^2} = \lim_{x \to 0} \frac{2\sec^2 x \tan x}{6x} ,
> $$
>
> using $\frac{d}{dx}\sec^2 x = 2\sec x \cdot \sec x \tan x$. Because $\lim_{x \to 0} \sec^2 x = 1$, simplify by splitting off that factor (Product Law):
>
> $$
> \lim_{x \to 0} \frac{2\sec^2 x \tan x}{6x} = \frac13 \lim_{x \to 0} \sec^2 x \cdot \lim_{x \to 0} \frac{\tan x}{x} = \frac13 \lim_{x \to 0} \frac{\tan x}{x} .
> $$
>
> The last limit is of type $\frac00$; a third application gives $\lim_{x \to 0} \frac{\sec^2 x}{1} = 1$. (Alternatively, $\frac{\tan x}{x} = \frac{\sin x}{x} \cdot \frac{1}{\cos x} \to 1 \cdot 1$.) Altogether,
>
> $$
> \lim_{x \to 0} \frac{\tan x - x}{x^3} = \frac13 .
> $$
>
> *Stewart: Example 4.4.4*

^ex-28-2

## Indeterminate Products (Type 0 · ∞)

> [!definition] Definition §28.2: Indeterminate Form of Type 0 · ∞
> If $\lim_{x \to a} f(x) = 0$ and $\lim_{x \to a} g(x) = \infty$ (or $-\infty$), then $\lim_{x \to a}[f(x)g(x)]$ is called an **indeterminate form of type $0 \cdot \infty$**.
>
> *Stewart: 4.4 (text)*

^def-28-2

It is not clear in advance what the limit is, if any: if $f$ wins it is $0$, if $g$ wins it is $\infty$ (or $-\infty$), and there may be a compromise. As $x \to 0^+$,
$x^2 \cdot \frac1x = x \to 0$, $\ x \cdot \frac{1}{x^2} = \frac1x \to \infty$, and $\ x \cdot \frac1x = 1 \to 1$. One deals with such a limit by writing the product as a quotient,

$$
fg = \frac{f}{1/g} \qquad\text{or}\qquad fg = \frac{g}{1/f} ,
$$

which turns it into a limit of type $\frac00$ or $\frac{\infty}{\infty}$.

> [!example] Example §28.3: An Indeterminate Product
> Evaluate $\displaystyle\lim_{x \to 0^+} x \ln x$.
>
> As $x \to 0^+$, the first factor $x$ tends to $0$ while $\ln x \to -\infty$: type $0 \cdot \infty$. Writing $x = 1/(1/x)$, with $1/x \to \infty$, gives a limit of type $\frac{\infty}{\infty}$ (here $-\infty$ over $\infty$), and l'Hospital's Rule gives
>
> $$
> \lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x} = \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0 .
> $$
>
> The other choice, $\lim_{x \to 0^+} \frac{x}{1/\ln x}$, is of type $\frac00$, but l'Hospital's Rule produces a more complicated expression than the one we started with. In general, choose the rewriting that leads to the simpler limit.
>
> *Stewart: Example 4.4.6 and the Note following it*

^ex-28-3

## Indeterminate Differences (Type ∞ − ∞)

> [!definition] Definition §28.3: Indeterminate Form of Type ∞ − ∞
> If $\lim_{x \to a} f(x) = \infty$ and $\lim_{x \to a} g(x) = \infty$, then $\lim_{x \to a}[f(x) - g(x)]$ is called an **indeterminate form of type $\infty - \infty$**.
>
> *Stewart: 4.4 (text)*

^def-28-3

Again there is a contest: the answer may be $\infty$ ($f$ wins), $-\infty$ ($g$ wins), or a finite compromise. To find out, convert the difference into a quotient (by a common denominator, by rationalizing, or by factoring out a common factor) so as to get a form of type $\frac00$ or $\frac{\infty}{\infty}$. For instance, $e^x - x = x\big(\frac{e^x}{x} - 1\big)$, and $\frac{e^x}{x} \to \infty$ by l'Hospital's Rule, so $\lim_{x \to \infty}(e^x - x) = \infty$ (Stewart's Example 4.4.8).

> [!example] Example §28.4: An Indeterminate Difference
> Compute $\displaystyle\lim_{x \to 1^+} \Big(\frac{1}{\ln x} - \frac{1}{x - 1}\Big)$.
>
> As $x \to 1^+$, $\frac{1}{\ln x} \to \infty$ and $\frac{1}{x - 1} \to \infty$: type $\infty - \infty$. With a common denominator,
>
> $$
> \lim_{x \to 1^+} \Big(\frac{1}{\ln x} - \frac{1}{x - 1}\Big) = \lim_{x \to 1^+} \frac{x - 1 - \ln x}{(x - 1)\ln x} .
> $$
>
> Numerator and denominator both tend to $0$, so l'Hospital's Rule applies. The derivative of the denominator is $(x - 1)\cdot\frac1x + \ln x$ (Product Rule); multiplying top and bottom by $x$,
>
> $$
> \lim_{x \to 1^+} \frac{x - 1 - \ln x}{(x - 1)\ln x} = \lim_{x \to 1^+} \frac{1 - \frac1x}{(x - 1)\cdot\frac1x + \ln x} = \lim_{x \to 1^+} \frac{x - 1}{x - 1 + x\ln x} .
> $$
>
> This is again of type $\frac00$, so apply the rule a second time, using $\frac{d}{dx}(x \ln x) = \ln x + 1$:
>
> $$
> \lim_{x \to 1^+} \frac{x - 1}{x - 1 + x\ln x} = \lim_{x \to 1^+} \frac{1}{1 + 1 + \ln x} = \lim_{x \to 1^+} \frac{1}{2 + \ln x} = \frac12 .
> $$
>
> *Stewart: Example 4.4.7*

^ex-28-4

## Indeterminate Powers (Types 0⁰, ∞⁰, 1^∞)

> [!definition] Definition §28.4: Indeterminate Powers
> The limit $\lim_{x \to a}[f(x)]^{g(x)}$ is an indeterminate form
> 1. of **type $0^0$** if $\lim_{x \to a} f(x) = 0$ and $\lim_{x \to a} g(x) = 0$;
> 2. of **type $\infty^0$** if $\lim_{x \to a} f(x) = \infty$ and $\lim_{x \to a} g(x) = 0$;
> 3. of **type $1^\infty$** if $\lim_{x \to a} f(x) = 1$ and $\lim_{x \to a} g(x) = \pm\infty$.
>
> (The form $0^\infty$ is *not* indeterminate: such a limit is $0$; Stewart's Exercise 88.)
>
> *Stewart: 4.4 (text)*

^def-28-4

Each case is treated either by taking the natural logarithm, $y = [f(x)]^{g(x)} \Rightarrow \ln y = g(x)\ln f(x)$, or by writing the function as an exponential ([[§5 Inverse Functions and Logarithms#^prop-5-7|Proposition §5.7]]),

$$
[f(x)]^{g(x)} = e^{g(x)\ln f(x)} .
$$

Either way one is led to the indeterminate product $g(x)\ln f(x)$, of type $0 \cdot \infty$. (Both methods were used for differentiating such functions, in [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^rem-19-2|Remark: Method — Logarithmic Differentiation]].) The last step uses the continuity of $e^x$: if $\ln y \to L$, then $y = e^{\ln y} \to e^L$ ([[§10 Continuity#^thm-10-7|Theorem §10.7]]).

> [!example] Example §28.5: Indeterminate Powers
> **(a)** Calculate $\displaystyle\lim_{x \to 0^+} (1 + \sin 4x)^{\cot x}$.
>
> As $x \to 0^+$, $1 + \sin 4x \to 1$ and $\cot x \to \infty$: type $1^\infty$. Let $y = (1 + \sin 4x)^{\cot x}$. Then
>
> $$
> \ln y = \ln\big[(1 + \sin 4x)^{\cot x}\big] = \cot x \,\ln(1 + \sin 4x) = \frac{\ln(1 + \sin 4x)}{\tan x} ,
> $$
>
> which is of type $\frac00$. By l'Hospital's Rule and the Chain Rule,
>
> $$
> \lim_{x \to 0^+} \ln y = \lim_{x \to 0^+} \frac{\ln(1 + \sin 4x)}{\tan x} = \lim_{x \to 0^+} \frac{\dfrac{4\cos 4x}{1 + \sin 4x}}{\sec^2 x} = \frac{4 \cdot 1/(1 + 0)}{1} = 4 .
> $$
>
> So far we have the limit of $\ln y$. Since $y = e^{\ln y}$,
>
> $$
> \lim_{x \to 0^+} (1 + \sin 4x)^{\cot x} = \lim_{x \to 0^+} e^{\ln y} = e^4 .
> $$
>
> **(b)** Find $\displaystyle\lim_{x \to 0^+} x^x$.
>
> This is of type $0^0$: $0^x = 0$ for every $x > 0$ but $x^0 = 1$ for every $x \ne 0$ (and $0^0$ is undefined). Write the function as an exponential, $x^x = (e^{\ln x})^x = e^{x \ln x}$. By Example §28.3, $\lim_{x \to 0^+} x \ln x = 0$. Therefore
>
> $$
> \lim_{x \to 0^+} x^x = \lim_{x \to 0^+} e^{x \ln x} = e^0 = 1 .
> $$
>
> *Stewart: Examples 4.4.9 and 4.4.10*

^ex-28-5

> [!remark] Remark: Method — Evaluating an Indeterminate Form
> 1. **Identify the type** by computing the limits of the pieces. If the limit is not indeterminate, use the Limit Laws or continuity instead ([[§28 Indeterminate Forms and L'Hospital's Rule#^rem-28-2|Remark: Using the Rule Correctly]]).
> 2. **Types $\frac00$, $\frac{\infty}{\infty}$:** apply l'Hospital's Rule ([[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-2|Theorem §28.2]]), differentiating numerator and denominator separately.
> 3. **Type $0 \cdot \infty$:** write $fg = \frac{f}{1/g}$ or $\frac{g}{1/f}$, choosing the version whose derivatives are simpler (usually keep the logarithm in the numerator).
> 4. **Type $\infty - \infty$:** convert to a quotient by a common denominator, rationalizing, or factoring out a common factor.
> 5. **Types $0^0$, $\infty^0$, $1^\infty$:** take $\ln y = g \ln f$ (type $0 \cdot \infty$), find its limit $L$, and conclude $y \to e^L$.
> 6. After each application, **simplify** and **re-check the type** before applying the rule again; split off factors with a known nonzero limit.

^rem-28-3
