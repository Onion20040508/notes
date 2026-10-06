---
type: section
subject: "[[Calculus]]"
chapter: 17
section: 121
stewart: "Appendix G"
aliases: ["Stewart Appendix G"]
tags: [calculus]
---
← [[§120 Sigma Notation]] · ↑ [[· 17 Background from the Appendices]]

*Stewart, Appendix G.*

This appendix is the rigorous development of the exponential and logarithmic functions introduced in Chapter 1, where everything rested on intuition and numerical evidence: $b^x$ was defined by roots for rational $x$ and by filling in the holes of the graph for irrational $x$ ([[§4 Exponential Functions#^def-4-2|Definition §4.2]], [[§4 Exponential Functions#^def-4-3|Definition §4.3]]), $e$ as the base whose exponential has slope $1$ at $0$ ([[§4 Exponential Functions#^def-4-4|Definition §4.4]]), and $\log_b$ as the inverse of $b^x$, with $\ln = \log_e$ ([[§5a Logarithmic and Inverse Trigonometric Functions#^def-5-3|Definition §5.3]], [[§5a Logarithmic and Inverse Trigonometric Functions#^def-5-4|Definition §5.4]]); the laws of exponents and logarithms were stated without proof for real exponents ([[§4 Exponential Functions#^thm-4-1|Theorem §4.1]], [[§5a Logarithmic and Inverse Trigonometric Functions#^thm-5-5|Theorem §5.5]]), and Chapter 3 took the derivatives and the limit formula for $e$ on credit ([[§14 Derivatives of Polynomials and Exponential Functions#^def-14-2|Definition §14.2]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Theorem §19.7]]). Here the order is reversed and the Fundamental Theorem of Calculus does the work: $\ln x$ is *defined* as $\int_1^x dt/t$ ([[§121 The Logarithm Defined as an Integral#^def-121-1|Definition §121.1]]), $e^x$ as its inverse ([[§121 The Logarithm Defined as an Integral#^def-121-3|Definition §121.3]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Definition §121.4]]), and $b^x$ and $\log_b x$ from these ([[§121a General Exponential and Logarithmic Functions#^def-121-5|Definition §121.5]], [[§121a General Exponential and Logarithmic Functions#^def-121-6|Definition §121.6]]). **No previous definition or result about exponential or logarithmic functions is used.** Every law of logarithms and exponents and every differentiation formula is then proved, and the new definitions agree with the old ones ([[§121 The Logarithm Defined as an Integral#^prop-121-4|Proposition §121.4]], [[§121a General Exponential and Logarithmic Functions#^thm-121-12|Theorem §121.12]], and [[§121a General Exponential and Logarithmic Functions#^rem-121-2|the closing remark]]).

## The Natural Logarithm

> [!definition] Definition §121.1: The Natural Logarithm
> The **natural logarithmic function** is the function defined by
>
> $$
> \ln x = \int_1^x \frac1t\,dt , \qquad x > 0 .
> $$
>
> *Stewart: Appendix G, Definition 1*

^def-121-1

> [!remark] Remark: What the Definition Says
> The function exists because the integral of a continuous function always exists ([[§35 The Definite Integral#^thm-35-1|Theorem §35.1]]), and $1/t$ is continuous on $(0, \infty)$, which contains the interval between $1$ and $x$. If $x > 1$, $\ln x$ is the area under the hyperbola $y = 1/t$ from $t = 1$ to $t = x$. For $x = 1$, $\ln 1 = \int_1^1 \frac1t\,dt = 0$. For $0 < x < 1$,
>
> $$
> \ln x = \int_1^x \frac1t\,dt = -\int_x^1 \frac1t\,dt < 0 ,
> $$
>
> the negative of the area under the hyperbola from $x$ to $1$.

^rem-121-1

> [!remark]- Connections
> - 451 builds the same functions in the other order: $e^x$ by its power series and $\log$ as its inverse ([[§26 Differentiation and Integration of Power Series#^rem-26-1|451 Remark: Repaying the trigonometric debt]], [[§18 Properties of Continuous Functions#^thm-18-9|451 Thm. §18.9]] for the continuous inverse). With the rigorous Riemann integral and FTC of 451 ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]), the construction of this appendix is itself fully rigorous.

> [!example] Example §121.1: Estimating ln 2
> **(a)** Show that $\frac12 < \ln 2 < \frac34$ by comparing areas. $\ln 2$ is the area under $y = 1/t$ from $1$ to $2$. On $(1, 2)$ the curve lies above the horizontal line $y = \frac12$ (since $1/t > 1/2$ for $t < 2$) and below the chord from $A(1, 1)$ to $D(2, \frac12)$, whose equation is $y = \frac{3 - t}{2}$: indeed
>
> $$
> \frac1t - \frac{3 - t}{2} = \frac{t^2 - 3t + 2}{2t} = \frac{(t - 1)(t - 2)}{2t} < 0 \qquad (1 < t < 2) .
> $$
>
> So the area is larger than that of the rectangle with base $[1, 2]$ and height $\frac12$, and smaller than that of the trapezoid under the chord:
>
> $$
> \tfrac12 \cdot 1 < \ln 2 < 1 \cdot \tfrac12\big(1 + \tfrac12\big), \qquad\text{that is,}\qquad \tfrac12 < \ln 2 < \tfrac34 .
> $$
>
> **(b)** By the Midpoint Rule ([[§50 Approximate Integration#^def-50-2|Definition §50.2]]) with $f(t) = 1/t$, $n = 10$, $\Delta t = 0.1$:
>
> $$
> \ln 2 = \int_1^2 \frac1t\,dt \approx (0.1)\big[f(1.05) + f(1.15) + \cdots + f(1.95)\big] = (0.1)\Big(\frac{1}{1.05} + \frac{1}{1.15} + \cdots + \frac{1}{1.95}\Big) \approx 0.693 .
> $$
>
> (The sum is $0.69284$; the true value is $0.69315$.)
>
> *Stewart: Appendix G, Example 1*

^ex-121-1

![[m233-121-1.svg]]
*Left: for $x > 1$, $\ln x$ is the area under $y = 1/t$ from $1$ to $x$. Right: [[§121 The Logarithm Defined as an Integral#^ex-121-1|Example §121.1]](a). The area $\ln 2$ (blue) lies between the rectangle of height $\frac12$ (green, area $\frac12$) and the trapezoid under the chord $AD$ (red dashed, area $\frac34$).*

> [!theorem] Theorem §121.1: Derivative of the Natural Logarithm
> $$
> \frac{d}{dx}(\ln x) = \frac1x \qquad (x > 0) .
> $$
>
> *Stewart: Appendix G, Equation 2*

^thm-121-1

> [!proof]+ Proof
> The integral defining $\ln x$ is exactly of the type in Part 1 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]): $1/t$ is continuous on $(0, \infty)$, so $\dfrac{d}{dx}\displaystyle\int_1^x \frac1t\,dt = \frac1x$ for every $x > 0$.

^pf-121-1

*Uses:* [[§121 The Logarithm Defined as an Integral#^def-121-1|Def. §121.1]], [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]] (FTC Part 1)

> [!remark]- Connections
> - Rigorous FTC Part 1: [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]].

> [!theorem] Theorem §121.2: Laws of Logarithms
> If $x$ and $y$ are positive numbers and $r$ is a rational number, then
>
> $$
> 1.\ \ln(xy) = \ln x + \ln y \qquad 2.\ \ln\Big(\frac xy\Big) = \ln x - \ln y \qquad 3.\ \ln(x^r) = r\ln x
> $$
>
> *Stewart: Appendix G, (3) Laws of Logarithms*

^thm-121-2

> [!proof]+ Proof
> **Law 1.** Let $a > 0$ be a constant and $f(x) = \ln(ax)$ for $x > 0$. By [[§121 The Logarithm Defined as an Integral#^thm-121-1|Theorem §121.1]] and the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]),
>
> $$
> f'(x) = \frac{1}{ax} \cdot \frac{d}{dx}(ax) = \frac{1}{ax} \cdot a = \frac1x .
> $$
>
> So $f(x)$ and $\ln x$ have the same derivative on the interval $(0, \infty)$, and therefore differ by a constant ([[§26 The Mean Value Theorem#^cor-26-4|Corollary §26.4]]): $\ln(ax) = \ln x + C$. Putting $x = 1$: $\ln a = \ln 1 + C = C$. Thus $\ln(ax) = \ln x + \ln a$ for all $x > 0$; since $a > 0$ was arbitrary, replacing $a$ by $y$ gives Law 1.
>
> **Law 2.** By Law 1 with $x = 1/y$: $\ln\frac1y + \ln y = \ln\big(\frac1y \cdot y\big) = \ln 1 = 0$, so $\ln\frac1y = -\ln y$. Then by Law 1 again, $\ln\frac xy = \ln\big(x \cdot \frac1y\big) = \ln x + \ln\frac1y = \ln x - \ln y$.
>
> **Law 3** (Stewart leaves this as Exercise 5; here is a proof that needs no derivative of $x^r$). For integers $n \ge 0$, by induction: $\ln(x^0) = \ln 1 = 0$, and $\ln(x^{n+1}) = \ln(x^n \cdot x) = \ln(x^n) + \ln x = n\ln x + \ln x = (n + 1)\ln x$ by Law 1. For $n = -m < 0$: $\ln(x^{-m}) = \ln\frac{1}{x^m} = -\ln(x^m) = -m\ln x$ by Law 2. For $r = p/q$ with $p$, $q$ integers, $q > 0$: $x^{p/q} = \sqrt[q]{x^p} > 0$ (a root, [[§4 Exponential Functions#^def-4-2|Definition §4.2]], not an exponential function) and $(x^{p/q})^q = x^p$, so by the integer case
>
> $$
> q\ln(x^{p/q}) = \ln\big((x^{p/q})^q\big) = \ln(x^p) = p\ln x , \qquad\text{hence}\qquad \ln(x^{p/q}) = \tfrac pq\ln x .
> $$
>
> (Stewart's hint is to show that both sides have the same derivative, as for Law 1; that route needs the Power Rule for rational exponents.)

^pf-121-2

*Uses:* [[§121 The Logarithm Defined as an Integral#^thm-121-1|§121.1]], [[§17 The Chain Rule#^thm-17-2|§17.2]] (Chain Rule), [[§26 The Mean Value Theorem#^cor-26-4|§26.4]] (functions with equal derivatives differ by a constant), induction ([[§120 Sigma Notation#^def-120-2|Def. §120.2]]), [[§4 Exponential Functions#^def-4-2|Def. §4.2]] (rational exponents)

> [!remark]- Connections
> - Complex-variables version: [[§34 Some Identities Involving Logarithms#^thm-34-1|342 Thm. §34.1]] (the law for the product with the multiple-valued $\log z$, valid as an equality of sets of values).

> [!theorem] Theorem §121.3: Shape and Limits of ln
> $\ln$ is continuous, increasing and concave downward on $(0, \infty)$, and
>
> $$
> \text{(a)}\ \lim_{x \to \infty} \ln x = \infty, \qquad \text{(b)}\ \lim_{x \to 0^+} \ln x = -\infty . \qquad (4)
> $$
>
> Its range is $(-\infty, \infty)$.
>
> *Stewart: Appendix G, (4) and text*

^thm-121-3

> [!proof]+ Proof
> **Shape.** $\ln$ is differentiable ([[§121 The Logarithm Defined as an Integral#^thm-121-1|Theorem §121.1]]), hence continuous. For $y = \ln x$, $\dfrac{dy}{dx} = \dfrac1x > 0$ and $\dfrac{d^2y}{dx^2} = -\dfrac{1}{x^2} < 0$, so $\ln$ is increasing and concave downward on $(0, \infty)$ ([[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]], [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-3|Theorem §27.3]]).
>
> **(a)** By Law 3 with $x = 2$ and $r = n$ a positive integer, $\ln(2^n) = n\ln 2$. Since $\ln 2 > 0$ ([[§121 The Logarithm Defined as an Integral#^ex-121-1|Example §121.1]], or because $\ln$ is increasing and $\ln 1 = 0$), $\ln(2^n) \to \infty$ as $n \to \infty$. As $\ln$ is increasing, for any $M$ choose $n$ with $n\ln 2 > M$; then $\ln x > M$ for all $x > 2^n$. So $\ln x \to \infty$ as $x \to \infty$.
>
> **(b)** Let $t = 1/x$. Then $t \to \infty$ as $x \to 0^+$, and by Law 2 and (a),
>
> $$
> \lim_{x \to 0^+} \ln x = \lim_{t \to \infty} \ln\Big(\frac1t\Big) = \lim_{t \to \infty} (-\ln t) = -\infty .
> $$
>
> **Range.** For any real $y$, (a) and (b) give $0 < x_1 < x_2$ with $\ln x_1 < y < \ln x_2$, and by the Intermediate Value Theorem ([[§10 Continuity#^thm-10-10|Theorem §10.10]]) on $[x_1, x_2]$, $\ln x = y$ for some $x$.

^pf-121-3

*Uses:* [[§121 The Logarithm Defined as an Integral#^thm-121-1|§121.1]], [[§121 The Logarithm Defined as an Integral#^thm-121-2|§121.2]], [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|§27.1]], [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-3|§27.3]] (increasing/decreasing and concavity tests), [[§10 Continuity#^thm-10-10|§10.10]] (Intermediate Value Theorem), [[§11 Limits at Infinity; Horizontal Asymptotes#^def-11-3|Def. §11.3]] (infinite limits at infinity)

> [!definition] Definition §121.2: The Number e
> $e$ is the number such that $\ln e = 1$.
>
> It exists by the Intermediate Value Theorem, since $\ln$ is continuous with $\ln 1 = 0$ and takes arbitrarily large values ([[§121 The Logarithm Defined as an Integral#^thm-121-3|Theorem §121.3]]), and it is unique because $\ln$ is increasing. [[§121a General Exponential and Logarithmic Functions#^thm-121-12|Theorem §121.12]] shows that it is the number $e$ of Chapters 1 and 3 ([[§4 Exponential Functions#^def-4-4|Definition §4.4]], [[§14 Derivatives of Polynomials and Exponential Functions#^def-14-2|Definition §14.2]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Theorem §19.7]]).
>
> *Stewart: Appendix G, Definition 5*

^def-121-2

## The Natural Exponential Function

> [!definition] Definition §121.3: The Natural Exponential Function
> Since $\ln$ is increasing, it is one-to-one, so it has an inverse function, denoted $\exp$:
>
> $$
> \exp(x) = y \iff \ln y = x . \qquad (6)
> $$
>
> The cancellation equations are
>
> $$
> \exp(\ln x) = x \ (x > 0) \qquad\text{and}\qquad \ln(\exp x) = x \ (x \in \mathbb{R}) . \qquad (7)
> $$
>
> In particular $\exp(0) = 1$ since $\ln 1 = 0$, and $\exp(1) = e$ since $\ln e = 1$. The graph of $\exp$ is the reflection of the graph of $\ln$ in the line $y = x$; its domain is the range of $\ln$, $(-\infty, \infty)$, and its range is the domain of $\ln$, $(0, \infty)$.
>
> *Stewart: Appendix G, Equations 6 and 7*

^def-121-3

> [!theorem] Proposition §121.4: exp(r) = e^r for Rational r
> If $r$ is any rational number, then $\exp(r) = e^r$.
>
> *Stewart: Appendix G (text)*

^prop-121-4

> [!proof]+ Proof
> By Law 3 of [[§121 The Logarithm Defined as an Integral#^thm-121-2|Theorem §121.2]], $\ln(e^r) = r\ln e = r$. By (6), $\exp(r) = e^r$.

^pf-121-4

*Uses:* [[§121 The Logarithm Defined as an Integral#^thm-121-2|§121.2]], [[§121 The Logarithm Defined as an Integral#^def-121-3|Def. §121.3]]

> [!definition] Definition §121.4: e to the x
> For every real number $x$, rational or not, define
>
> $$
> e^x = \exp(x) .
> $$
>
> By [[§121 The Logarithm Defined as an Integral#^prop-121-4|Proposition §121.4]] this agrees with the usual power when $x$ is rational. In this notation $e^x$ is the inverse of $\ln x$, and (6) and (7) become
>
> $$
> e^x = y \iff \ln y = x \qquad (8), \qquad\qquad e^{\ln x} = x \ \ (x > 0) \qquad (9), \qquad\qquad \ln(e^x) = x \ \ \text{for all } x \qquad (10).
> $$
>
> *Stewart: Appendix G, Equations 8, 9, 10*

^def-121-4

> [!theorem] Theorem §121.5: Properties of the Exponential Function
> The exponential function $f(x) = e^x$ is an increasing continuous function with domain $\mathbb{R}$ and range $(0, \infty)$. Thus $e^x > 0$ for all $x$. Also
>
> $$
> \lim_{x \to -\infty} e^x = 0, \qquad \lim_{x \to \infty} e^x = \infty ,
> $$
>
> so the $x$-axis is a horizontal asymptote of $f(x) = e^x$.
>
> *Stewart: Appendix G, Properties of the Exponential Function*

^thm-121-5

> [!proof]+ Proof
> Stewart: these "follow from the fact that it is the inverse of the natural logarithmic function". In detail: the inverse of an increasing function is increasing (if $x_1 < x_2$ but $e^{x_1} \ge e^{x_2}$, applying the increasing function $\ln$ gives $x_1 \ge x_2$). The inverse of a one-to-one continuous function on an interval is continuous ([[§10 Continuity#^thm-10-5|Theorem §10.5]]). The domain and range were found in [[§121 The Logarithm Defined as an Integral#^def-121-3|Definition §121.3]]. For the limits: given $\varepsilon > 0$, if $x < \ln\varepsilon$ then $0 < e^x < e^{\ln\varepsilon} = \varepsilon$, so $e^x \to 0$ as $x \to -\infty$; given $M > 0$, if $x > \ln M$ then $e^x > M$, so $e^x \to \infty$ as $x \to \infty$.

^pf-121-5

*Uses:* [[§121 The Logarithm Defined as an Integral#^def-121-3|Def. §121.3]], [[§121 The Logarithm Defined as an Integral#^thm-121-3|§121.3]], [[§10 Continuity#^thm-10-5|§10.5]] (continuity of inverse functions)

> [!theorem] Theorem §121.6: Laws of Exponents for e^x
> If $x$ and $y$ are real numbers and $r$ is rational, then
>
> $$
> 1.\ e^{x + y} = e^xe^y \qquad 2.\ e^{x - y} = \frac{e^x}{e^y} \qquad 3.\ (e^x)^r = e^{rx}
> $$
>
> *Stewart: Appendix G, (11) Laws of Exponents*

^thm-121-6

> [!proof]+ Proof
> **Law 1.** By Law 1 of logarithms and (10),
>
> $$
> \ln(e^xe^y) = \ln(e^x) + \ln(e^y) = x + y = \ln(e^{x + y}) .
> $$
>
> Since $\ln$ is one-to-one, $e^xe^y = e^{x + y}$.
>
> **Law 2** (Stewart's Exercise 6). By Law 2 of logarithms, $\ln\dfrac{e^x}{e^y} = \ln(e^x) - \ln(e^y) = x - y = \ln(e^{x - y})$, so $\dfrac{e^x}{e^y} = e^{x - y}$.
>
> **Law 3** (Stewart's Exercise 7). By Law 3 of logarithms (for rational $r$), $\ln\big((e^x)^r\big) = r\ln(e^x) = rx = \ln(e^{rx})$, so $(e^x)^r = e^{rx}$.
>
> Law 3 holds for every real $r$ once $b^r$ is defined for irrational $r$ ([[§121a General Exponential and Logarithmic Functions#^thm-121-9|Theorem §121.9]]).

^pf-121-6

*Uses:* [[§121 The Logarithm Defined as an Integral#^thm-121-2|§121.2]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Def. §121.4]]

> [!theorem] Theorem §121.7: Derivative of the Exponential Function
> $$
> \frac{d}{dx}(e^x) = e^x .
> $$
>
> *Stewart: Appendix G, Equation 12*

^thm-121-7

> [!proof]+ Proof
> The function $y = e^x$ is differentiable because it is the inverse function of $y = \ln x$, which is differentiable with nonzero derivative $1/x$ (the derivative of an inverse function, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]]). To find the derivative, let $y = e^x$. Then $\ln y = x$, and differentiating this implicitly with respect to $x$ ([[§18 Implicit Differentiation|§18]]), using [[§121 The Logarithm Defined as an Integral#^thm-121-1|Theorem §121.1]] and the Chain Rule,
>
> $$
> \frac1y\,\frac{dy}{dx} = 1, \qquad\text{so}\qquad \frac{dy}{dx} = y = e^x .
> $$

^pf-121-7

*Uses:* [[§121 The Logarithm Defined as an Integral#^thm-121-1|§121.1]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Def. §121.4]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|§19.1]] (differentiability of an inverse function), [[§18 Implicit Differentiation|§18]] (implicit differentiation), [[§17 The Chain Rule#^thm-17-2|§17.2]]

> [!remark]- Connections
> - The differentiability of the inverse, which Stewart quotes, is the one-variable inverse function theorem: [[§29 The Mean Value Theorem#^thm-29-10|451 Thm. §29.10]], which also gives the derivative directly: $(e^x)' = 1/(\ln)'(e^x) = 1/(1/e^x) = e^x$.

*The section continues in [[§121a General Exponential and Logarithmic Functions]].*
