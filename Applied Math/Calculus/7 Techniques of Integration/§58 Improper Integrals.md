---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 58
stewart: "7.8"
aliases: ["Stewart 7.8"]
tags: [calculus]
---
← [[§57 Approximate Integration]] · ↑ [[· 7 Techniques of Integration]] · [[§59 The Integral of 1∕x from 1 to 2]] →

*Stewart, Section 7.8.*

The definite integral of [[§39 The Definite Integral#^def-39-1|Definition §39.1]] requires a finite interval $[a, b]$ and a function without infinite discontinuities. An **improper integral** drops one of these requirements: the interval is infinite (Type 1), or the integrand has an infinite discontinuity (Type 2). In both cases it is defined as a limit of ordinary integrals over smaller intervals, and it *converges* if the limit exists. The region under $y = 1/x^2$ to the right of $x = 1$ has area $1$, but the region under $y = 1/x$ has infinite area: the dividing line is the $p$-integral, $\int_1^\infty x^{-p}\,dx$ converges exactly when $p > 1$. When an antiderivative cannot be found, a Comparison Theorem can still decide convergence. Improper integrals are needed for probability distributions ([[§65 Probability#^def-65-2|Def. §65.2]]) and the Integral Test for series ([[§83 The Integral Test and Estimates of Sums#^thm-83-1|Theorem §83.1]]).

## Type 1: Infinite Intervals

Let $S$ be the region under $y = 1/x^2$, above the $x$-axis and to the right of $x = 1$. The part of $S$ to the left of $x = t$ has area

$$
A(t) = \int_1^t \frac{1}{x^2}\,dx = -\frac1x\Big]_1^t = 1 - \frac1t .
$$

$A(t) < 1$ however large $t$ is, and $\lim_{t \to \infty} A(t) = 1$. So we say that the infinite region $S$ has area $1$, and write $\int_1^\infty \frac{1}{x^2}\,dx = \lim_{t \to \infty} \int_1^t \frac{1}{x^2}\,dx = 1$.

> [!definition] Definition §58.1: Improper Integral of Type 1
> **(a)** If $\int_a^t f(x)\,dx$ exists for every number $t \ge a$, then
>
> $$
> \int_a^\infty f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx ,
> $$
>
> provided this limit exists (as a finite number).
>
> **(b)** If $\int_t^b f(x)\,dx$ exists for every number $t \le b$, then
>
> $$
> \int_{-\infty}^b f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx ,
> $$
>
> provided this limit exists (as a finite number).
>
> The improper integrals $\int_a^\infty f(x)\,dx$ and $\int_{-\infty}^b f(x)\,dx$ are called **convergent** if the corresponding limit exists and **divergent** if it does not.
>
> **(c)** If both $\int_a^\infty f(x)\,dx$ and $\int_{-\infty}^a f(x)\,dx$ are convergent, then
>
> $$
> \int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^a f(x)\,dx + \int_a^\infty f(x)\,dx .
> $$
>
> Any real number $a$ can be used in (c); the value does not depend on it (Exercise 88).
>
> If $f \ge 0$ and $\int_a^\infty f(x)\,dx$ converges, the **area** of $S = \{(x, y) \mid x \ge a,\ 0 \le y \le f(x)\}$ is defined to be $A(S) = \int_a^\infty f(x)\,dx$, the limit as $t \to \infty$ of the area under the graph from $a$ to $t$.
>
> *Stewart: 7.8, Definition 1*

^def-58-1

> [!remark]- Connections
> - Rigorous treatment: [[§36 Improper Integrals#^def-36-1|451 Def. §36.1]] and [[§36 Improper Integrals#^def-36-2|451 Def. §36.2]], which treat Types 1 and 2 at once (an interval open at an end, finite or infinite) and also allow the values $\pm\infty$ ("diverges to $\infty$"). 451 [[§36 Improper Integrals#^ex-36-3|Ex. §36.3]] shows why (c) takes the two limits *independently*: $\int_{-t}^{t} \sin x\,dx = 0$ for every $t$, yet $\int_{-\infty}^\infty \sin x\,dx$ diverges.
> - In the Lebesgue theory an integral over an infinite interval needs no limit, but it exists only if $\int |f| < \infty$: [[§22 The General Lebesgue Integral#^rem-22-1|551 Remark: Characterization of Integrability]].
> - ODE version: [[§26 Definition of the Laplace Transform#^def-26-1|331 Def. §26.1]] (the same definition, as the first step toward the Laplace transform), with three examples in [[§26 Definition of the Laplace Transform#^ex-26-1|331 Ex. §26.1]].
> - See also: [[§85 Evaluation of Improper Integrals#^def-85-1|342 Def. §85.1]] (the same definitions on $(0, \infty)$ and $(-\infty, \infty)$, with the Cauchy principal value [[§85 Evaluation of Improper Integrals#^def-85-2|342 Def. §85.2]]) and [[§85 Evaluation of Improper Integrals#^prop-85-4|342 Prop. §85.4]] (integrals of rational functions with $\deg q \ge \deg p + 2$ evaluated by residues).

> [!example] Example §58.1: The Reciprocal Diverges
> Determine whether $\displaystyle\int_1^\infty \frac1x\,dx$ is convergent or divergent.
>
> By [[§58 Improper Integrals#^def-58-1|Definition §58.1]](a),
>
> $$
> \int_1^\infty \frac1x\,dx = \lim_{t \to \infty} \int_1^t \frac1x\,dx = \lim_{t \to \infty} \ln|x|\Big]_1^t = \lim_{t \to \infty} (\ln t - \ln 1) = \lim_{t \to \infty} \ln t = \infty .
> $$
>
> The limit is not a finite number, so the integral is divergent.
>
> Compare: $\int_1^\infty \frac{1}{x^2}\,dx$ converges and $\int_1^\infty \frac1x\,dx$ diverges. The curves $y = 1/x^2$ and $y = 1/x$ look alike for $x > 0$, and both tend to $0$ as $x \to \infty$, but $1/x^2$ tends to $0$ faster. The values of $1/x$ do not decrease fast enough for the area to be finite.
>
> *Stewart: Example 7.8.1 and the text before Definition 1*

^ex-58-1

![[m233-51-1.svg]]
*Up to $x = t$, the area under $y = 1/x^2$ (blue) is $1 - \frac1t < 1$, while the area under $y = 1/x$ is $\ln t$, which exceeds it by the red area and grows without bound. Both curves tend to $0$; only the faster one encloses a finite area.*

> [!example] Example §58.2: Evaluating Type 1 Integrals
> Evaluate **(a)** $\displaystyle\int_{-\infty}^0 x e^x\,dx$ and **(b)** $\displaystyle\int_{-\infty}^\infty \frac{1}{1 + x^2}\,dx$.
>
> **(a)** By [[§58 Improper Integrals#^def-58-1|Definition §58.1]](b), $\int_{-\infty}^0 xe^x\,dx = \lim_{t \to -\infty} \int_t^0 xe^x\,dx$. Integrate by parts ([[§51 Integration by Parts#^thm-51-2|Theorem §51.2]]) with $u = x$, $dv = e^x\,dx$, $du = dx$, $v = e^x$:
>
> $$
> \int_t^0 xe^x\,dx = xe^x\Big]_t^0 - \int_t^0 e^x\,dx = -te^t - 1 + e^t .
> $$
>
> As $t \to -\infty$, $e^t \to 0$, and by l'Hospital's Rule ([[§31 Indeterminate Forms and L'Hospital's Rule#^thm-31-2|Theorem §31.2]]), for the form $\infty/\infty$,
>
> $$
> \lim_{t \to -\infty} te^t = \lim_{t \to -\infty} \frac{t}{e^{-t}} = \lim_{t \to -\infty} \frac{1}{-e^{-t}} = \lim_{t \to -\infty} (-e^t) = 0 .
> $$
>
> Therefore $\displaystyle\int_{-\infty}^0 xe^x\,dx = \lim_{t \to -\infty} (-te^t - 1 + e^t) = -0 - 1 + 0 = -1$.
>
> **(b)** Use [[§58 Improper Integrals#^def-58-1|Definition §58.1]](c) with $a = 0$, and evaluate the two halves separately:
>
> $$
> \begin{aligned}
> \int_0^\infty \frac{dx}{1 + x^2} &= \lim_{t \to \infty} \tan^{-1} x\Big]_0^t = \lim_{t \to \infty} (\tan^{-1} t - \tan^{-1} 0) = \lim_{t \to \infty} \tan^{-1} t = \frac{\pi}{2} , \\
> \int_{-\infty}^0 \frac{dx}{1 + x^2} &= \lim_{t \to -\infty} \tan^{-1} x\Big]_t^0 = \lim_{t \to -\infty} (\tan^{-1} 0 - \tan^{-1} t) = 0 - \Big(-\frac{\pi}{2}\Big) = \frac{\pi}{2} .
> \end{aligned}
> $$
>
> Both converge, so the given integral converges and $\displaystyle\int_{-\infty}^\infty \frac{dx}{1 + x^2} = \frac{\pi}{2} + \frac{\pi}{2} = \pi$. Since $1/(1 + x^2) > 0$, this is the area of the infinite region under the curve and above the $x$-axis.
>
> *Stewart: Examples 7.8.2 and 7.8.3*

^ex-58-2

> [!theorem] Theorem §58.1: The p-Integrals
> $$
> \int_1^\infty \frac{1}{x^p}\,dx \quad\text{is convergent if } p > 1 \text{ and divergent if } p \le 1 .
> $$
>
> For $p > 1$ its value is $\dfrac{1}{p - 1}$.
>
> *Stewart: 7.8, Box 2 (Example 7.8.4)*

^thm-58-1

> [!proof]+ Proof
> For $p = 1$ the integral diverges by [[§58 Improper Integrals#^ex-58-1|Example §58.1]]. Let $p \ne 1$. Then
>
> $$
> \int_1^\infty \frac{1}{x^p}\,dx = \lim_{t \to \infty} \int_1^t x^{-p}\,dx = \lim_{t \to \infty} \frac{x^{-p+1}}{-p + 1}\Big]_{x=1}^{x=t} = \lim_{t \to \infty} \frac{1}{1 - p}\Big[\frac{1}{t^{p-1}} - 1\Big] .
> $$
>
> If $p > 1$, then $p - 1 > 0$, so $t^{p-1} \to \infty$ and $1/t^{p-1} \to 0$ as $t \to \infty$; the limit is $\frac{1}{1 - p}(0 - 1) = \frac{1}{p - 1}$, and the integral converges. If $p < 1$, then $p - 1 < 0$ and $\frac{1}{t^{p-1}} = t^{1-p} \to \infty$ as $t \to \infty$, so the integral diverges.

^pf-58-1

*Uses:* [[§58 Improper Integrals#^def-58-1|Def. §58.1]], [[§58 Improper Integrals#^ex-58-1|Ex. §58.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§36 Improper Integrals#^ex-36-2|451 Ex. §36.2]], where the dichotomy feeds the Integral Test to give the $p$-series theorem ([[§83 The Integral Test and Estimates of Sums#^thm-83-2|Theorem §83.2]] here).

## Type 2: Discontinuous Integrands

Suppose $f$ is positive and continuous on a finite interval $[a, b)$ but has a vertical asymptote at $b$. The area of the unbounded region $S$ under the graph between $a$ and $t < b$ is $A(t) = \int_a^t f(x)\,dx$. If $A(t)$ approaches a definite number $A$ as $t \to b^-$, then we say that $S$ has area $A$ and write $\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$. (For Type 1 integrals the region extends indefinitely in a horizontal direction; here it is infinite in a vertical direction.) The same equation is used to *define* the integral whether or not $f$ is positive, and whatever kind of discontinuity $f$ has at $b$.

> [!definition] Definition §58.2: Improper Integral of Type 2
> **(a)** If $f$ is continuous on $[a, b)$ and discontinuous at $b$, then
>
> $$
> \int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx
> $$
>
> if this limit exists (as a finite number).
>
> **(b)** If $f$ is continuous on $(a, b]$ and discontinuous at $a$, then
>
> $$
> \int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx
> $$
>
> if this limit exists (as a finite number).
>
> The improper integral $\int_a^b f(x)\,dx$ is **convergent** if the corresponding limit exists and **divergent** if it does not.
>
> **(c)** If $f$ has a discontinuity at $c$, where $a < c < b$, and both $\int_a^c f(x)\,dx$ and $\int_c^b f(x)\,dx$ are convergent, then
>
> $$
> \int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx .
> $$
>
> *Stewart: 7.8, Definition 3*

^def-58-2

> [!example] Example §58.3: An Infinite Discontinuity at an Endpoint
> **(a)** Find $\displaystyle\int_2^5 \frac{1}{\sqrt{x - 2}}\,dx$. **(b)** Determine whether $\displaystyle\int_0^{\pi/2} \sec x\,dx$ converges. **(c)** Evaluate $\displaystyle\int_0^1 \ln x\,dx$.
>
> **(a)** $f(x) = 1/\sqrt{x - 2}$ has the vertical asymptote $x = 2$, at the left endpoint of $[2, 5]$. By [[§58 Improper Integrals#^def-58-2|Definition §58.2]](b),
>
> $$
> \int_2^5 \frac{dx}{\sqrt{x - 2}} = \lim_{t \to 2^+} \int_t^5 \frac{dx}{\sqrt{x - 2}} = \lim_{t \to 2^+} 2\sqrt{x - 2}\Big]_t^5 = \lim_{t \to 2^+} 2\big(\sqrt3 - \sqrt{t - 2}\big) = 2\sqrt3 .
> $$
>
> The integral converges; since the integrand is positive, $2\sqrt3$ is the area of the unbounded region under the curve from $2$ to $5$.
>
> **(b)** The integral is improper because $\lim_{x \to (\pi/2)^-} \sec x = \infty$. By [[§58 Improper Integrals#^def-58-2|Definition §58.2]](a) and the integral of secant ([[§52 Trigonometric Integrals#^thm-52-3|Theorem §52.3]]),
>
> $$
> \int_0^{\pi/2} \sec x\,dx = \lim_{t \to (\pi/2)^-} \ln|\sec x + \tan x|\Big]_0^t = \lim_{t \to (\pi/2)^-} \big[\ln(\sec t + \tan t) - \ln 1\big] = \infty ,
> $$
>
> because $\sec t \to \infty$ and $\tan t \to \infty$ as $t \to (\pi/2)^-$. The integral is divergent.
>
> **(c)** $\lim_{x \to 0^+} \ln x = -\infty$, so the integral is improper at $0$: $\int_0^1 \ln x\,dx = \lim_{t \to 0^+} \int_t^1 \ln x\,dx$. By parts with $u = \ln x$, $dv = dx$, $du = dx/x$, $v = x$ ([[§51 Integration by Parts#^ex-51-4|Example §51.4]]),
>
> $$
> \int_t^1 \ln x\,dx = x\ln x\Big]_t^1 - \int_t^1 dx = 1\ln 1 - t\ln t - (1 - t) = -t\ln t - 1 + t .
> $$
>
> By l'Hospital's Rule,
>
> $$
> \lim_{t \to 0^+} t\ln t = \lim_{t \to 0^+} \frac{\ln t}{1/t} = \lim_{t \to 0^+} \frac{1/t}{-1/t^2} = \lim_{t \to 0^+} (-t) = 0 ,
> $$
>
> so $\displaystyle\int_0^1 \ln x\,dx = \lim_{t \to 0^+} (-t\ln t - 1 + t) = -0 - 1 + 0 = -1$. Geometrically, the region above $y = \ln x$ and below the $x$-axis, between $0$ and $1$, has area $1$.
>
> *Stewart: Examples 7.8.5, 7.8.6 and 7.8.8*

^ex-58-3

> [!example] Example §58.4: A Discontinuity Inside the Interval
> Evaluate $\displaystyle\int_0^3 \frac{dx}{x - 1}$ if possible.
>
> The line $x = 1$ is a vertical asymptote of the integrand, in the middle of $[0, 3]$. So [[§58 Improper Integrals#^def-58-2|Definition §58.2]](c) with $c = 1$ applies:
>
> $$
> \int_0^3 \frac{dx}{x - 1} = \int_0^1 \frac{dx}{x - 1} + \int_1^3 \frac{dx}{x - 1} ,
> $$
>
> where
>
> $$
> \int_0^1 \frac{dx}{x - 1} = \lim_{t \to 1^-} \ln|x - 1|\Big]_0^t = \lim_{t \to 1^-} \big(\ln|t - 1| - \ln|-1|\big) = \lim_{t \to 1^-} \ln(1 - t) = -\infty ,
> $$
>
> because $1 - t \to 0^+$ as $t \to 1^-$. So $\int_0^1 \frac{dx}{x - 1}$ is divergent, and therefore $\int_0^3 \frac{dx}{x - 1}$ is divergent. (There is no need to evaluate $\int_1^3 \frac{dx}{x - 1}$.)
>
> **Warning.** Had we not noticed the asymptote and treated the integral as an ordinary one, we would have "computed" $\ln|x - 1|\Big]_0^3 = \ln 2 - \ln 1 = \ln 2$. This is wrong: the Fundamental Theorem of Calculus needs a continuous integrand on $[0, 3]$, and this integral is improper and must be calculated with limits. Whenever you meet $\int_a^b f(x)\,dx$, decide by looking at $f$ on $[a, b]$ whether it is an ordinary definite integral or an improper one.
>
> *Stewart: Example 7.8.7*

^ex-58-4

## A Comparison Test for Improper Integrals

Sometimes the exact value of an improper integral cannot be found, yet it matters whether it converges.

> [!theorem] Theorem §58.2: Comparison Theorem
> Suppose that $f$ and $g$ are continuous functions with $f(x) \ge g(x) \ge 0$ for $x \ge a$.
>
> **(a)** If $\int_a^\infty f(x)\,dx$ is convergent, then $\int_a^\infty g(x)\,dx$ is convergent.
>
> **(b)** If $\int_a^\infty g(x)\,dx$ is divergent, then $\int_a^\infty f(x)\,dx$ is divergent.
>
> A similar theorem holds for Type 2 integrals.
>
> *Stewart: 7.8, Comparison Theorem*

^thm-58-2

*Stewart omits the proof. It rests on the completeness of the real numbers: $t \mapsto \int_a^t g(x)\,dx$ is increasing (as $g \ge 0$) and bounded by $\int_a^\infty f(x)\,dx$, so it has a limit. The fact that an increasing function either converges or tends to $+\infty$ is [[§36 Improper Integrals#^thm-36-1|451 Thm. §36.1]].*

> [!remark]- Connections
> - ODE version: [[§26 Definition of the Laplace Transform#^thm-26-1|331 Thm. §26.1]] (the comparison test for piecewise continuous $f$ with $|f| \le g$), which shows that Laplace transforms exist, [[§26 Definition of the Laplace Transform#^thm-26-2|331 Thm. §26.2]].

> [!remark] Remark: Why It Works
> If the area under the upper curve $y = f(x)$ is finite, then so is the area under the lower curve $y = g(x)$. If the area under $y = g(x)$ is infinite, then so is the area under $y = f(x)$. The converses fail: if $\int_a^\infty g(x)\,dx$ converges, $\int_a^\infty f(x)\,dx$ may or may not converge, and if $\int_a^\infty f(x)\,dx$ diverges, $\int_a^\infty g(x)\,dx$ may or may not diverge. Comparison functions are typically $1/x^p$ ([[§58 Improper Integrals#^thm-58-1|Theorem §58.1]]) or $e^{-x}$.

^rem-58-1

> [!example] Example §58.5: Comparison
> **(a)** Show that $\displaystyle\int_0^\infty e^{-x^2}\,dx$ is convergent. **(b)** Show that $\displaystyle\int_1^\infty \frac{1 + e^{-x}}{x}\,dx$ is divergent.
>
> **(a)** The antiderivative of $e^{-x^2}$ is not elementary ([[§55 Strategy for Integration#^thm-55-2|Theorem §55.2]]), so the integral cannot be evaluated directly. Split it:
>
> $$
> \int_0^\infty e^{-x^2}\,dx = \int_0^1 e^{-x^2}\,dx + \int_1^\infty e^{-x^2}\,dx .
> $$
>
> The first integral is an ordinary definite integral with a finite value. For the second: if $x \ge 1$, then $x^2 \ge x$, so $-x^2 \le -x$ and $e^{-x^2} \le e^{-x}$. And
>
> $$
> \int_1^\infty e^{-x}\,dx = \lim_{t \to \infty} \int_1^t e^{-x}\,dx = \lim_{t \to \infty} (e^{-1} - e^{-t}) = e^{-1} .
> $$
>
> By [[§58 Improper Integrals#^thm-58-2|Theorem §58.2]](a) with $f(x) = e^{-x}$ and $g(x) = e^{-x^2}$, $\int_1^\infty e^{-x^2}\,dx$ converges, and hence so does $\int_0^\infty e^{-x^2}\,dx$. Its value is about $0.8862$; with double integrals in polar coordinates one shows that it is exactly $\sqrt{\pi}/2$ ([[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]]; worked out in [[§25 Change of Variables on General Domains#^ex-25-4|452 Ex. §25.4]]). It matters in probability ([[§65 Probability#^prop-65-3|Proposition §65.3]]). Numerically, $\int_0^t e^{-x^2}\,dx = 0.7468$, $0.8821$, $0.8862$ for $t = 1, 2, 3$: the values settle quickly, because $e^{-x^2} \to 0$ very rapidly.
>
> **(b)** For $x \ge 1$, $\dfrac{1 + e^{-x}}{x} > \dfrac1x$, and $\int_1^\infty \frac1x\,dx$ diverges ([[§58 Improper Integrals#^ex-58-1|Example §58.1]], or [[§58 Improper Integrals#^thm-58-1|Theorem §58.1]] with $p = 1$). By [[§58 Improper Integrals#^thm-58-2|Theorem §58.2]](b) the integral diverges. Numerically, $\int_1^t \frac{1 + e^{-x}}{x}\,dx \approx 0.86, 1.83, 2.52, 4.82, 7.13, 9.43$ for $t = 2, 5, 10, 100, 1000, 10000$: the values keep growing, roughly like $\ln t$.
>
> *Stewart: Examples 7.8.9 and 7.8.10*

^ex-58-5

![[m233-51-2.svg]]
*[[§58 Improper Integrals#^ex-58-5|Example §58.5]](a): for $x \ge 1$ the graph of $e^{-x^2}$ (red) lies below that of $e^{-x}$ (blue). The whole shaded region under $e^{-x}$ to the right of $1$ has finite area $e^{-1}$, so the red part, the area under $e^{-x^2}$, is finite too.*
