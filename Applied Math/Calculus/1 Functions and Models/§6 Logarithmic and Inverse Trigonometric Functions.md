---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 6
stewart: "1.5"
aliases: ["Stewart 1.5 (cont.)"]
tags: [calculus]
---
← [[§5 Inverse Functions and Logarithms]] · ↑ [[· 1 Functions and Models]] · [[§7 The Tangent and Velocity Problems]] →

*Stewart, Section 1.5.*

If $b > 0$ and $b \ne 1$, the exponential function $f(x) = b^x$ is either increasing or decreasing ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]), so no horizontal line meets its graph twice, and it is one-to-one by the Horizontal Line Test ([[§5 Inverse Functions and Logarithms#^thm-5-1|Theorem §5.1]]). It therefore has an inverse function.

## Logarithmic Functions

> [!definition] Definition §7.1: Logarithmic Function with Base b
> Let $b > 0$, $b \ne 1$. The inverse of the exponential function $f(x) = b^x$ is the **logarithmic function with base $b$**, denoted $\log_b$. By the form (3) of [[§5 Inverse Functions and Logarithms#^def-5-2|Definition §5.2]],
>
> $$
> \log_b x = y \quad\Longleftrightarrow\quad b^y = x . \qquad (6)
> $$
>
> So for $x > 0$, $\log_b x$ is *the exponent to which the base $b$ must be raised to give $x$*. For example, $\log_{10} 0.001 = -3$ because $10^{-3} = 0.001$.
>
> *Stewart: 1.5, Equation 6*

^def-6-1

*Rigorous construction: [[§145 General Exponential and Logarithmic Functions#^def-145-2|Definition §145.2]] (Appendix G).*

> [!theorem] Theorem §6.1: Properties of the Logarithmic Function
> Let $b > 0$, $b \ne 1$.
> 1. **Cancellation equations:**
>
> $$
> \log_b(b^x) = x \quad \text{for every } x \in \mathbb{R}, \qquad\qquad b^{\log_b x} = x \quad \text{for every } x > 0 . \qquad (7)
> $$
>
> 2. $\log_b$ has domain $(0, \infty)$ and range $\mathbb{R}$, and its graph is the reflection of the graph of $y = b^x$ about the line $y = x$.
> 3. $\log_b 1 = 0$, so every graph $y = \log_b x$ passes through $(1, 0)$.
> 4. If $b > 1$, then $\log_b$ is increasing. (It increases very slowly for $x > 1$, reflecting the very rapid increase of $b^x$ for $x > 0$.)
>
> *Stewart: 1.5, Equation 7 and text*

^thm-6-1

> [!proof]+ Proof
> **1.** [[§5 Inverse Functions and Logarithms#^thm-5-2|Theorem §5.2]] for $f(x) = b^x$, whose domain is $\mathbb{R}$ and whose range is $(0, \infty)$ ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]).
>
> **2.** By [[§5 Inverse Functions and Logarithms#^def-5-2|Definition §5.2]] the domain of $\log_b$ is the range $(0, \infty)$ of $b^x$, and its range is the domain $\mathbb{R}$ of $b^x$. The statement about graphs is [[§5 Inverse Functions and Logarithms#^thm-5-3|Theorem §5.3]].
>
> **3.** $b^0 = 1$, so $\log_b 1 = 0$ by (6).
>
> **4.** Let $b > 1$ and $0 < x_1 < x_2$. Suppose $\log_b x_1 \ge \log_b x_2$. Since $b^x$ is increasing for $b > 1$ ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]), $b^{\log_b x_1} \ge b^{\log_b x_2}$, and by (7) this says $x_1 \ge x_2$, a contradiction. Hence $\log_b x_1 < \log_b x_2$.

^pf-6-1

*Uses:* [[§5 Inverse Functions and Logarithms#^thm-5-2|§5.2]], [[§5 Inverse Functions and Logarithms#^thm-5-3|§5.3]], [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]], [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-1|Def. §6.1]], [[§4 Exponential Functions#^prop-4-2|§4.2]]

> [!remark]- Connections
> - The logarithm is continuous as the inverse of a strictly monotone continuous function: [[§18 Properties of Continuous Functions#^thm-18-9|451 Thm. §18.9]], applied to $e^x$ in [[§18 Properties of Continuous Functions#^rem-18-8|451 Remark: Beyond closed intervals]] (Calculus version: [[§12 Continuity#^thm-12-5|Theorem §12.5]]).

The following properties of logarithms come from the Laws of Exponents of [[§4 Exponential Functions#^thm-4-1|Theorem §4.1]].

> [!theorem] Theorem §6.2: Laws of Logarithms
> Let $b > 0$, $b \ne 1$. If $x$ and $y$ are positive numbers, then
>
> $$
> 1.\ \log_b(xy) = \log_b x + \log_b y \qquad 2.\ \log_b\Big(\frac{x}{y}\Big) = \log_b x - \log_b y \qquad 3.\ \log_b(x^r) = r \log_b x \quad (r \text{ any real number}) .
> $$
>
> *Stewart: 1.5, Laws of Logarithms*

^thm-6-2

> [!proof]+ Proof
> *Stewart says only that these follow from the corresponding Laws of Exponents; here is the derivation.* Let $u = \log_b x$ and $v = \log_b y$. By (6), $b^u = x$ and $b^v = y$.
>
> 1. By Law 1 of [[§4 Exponential Functions#^thm-4-1|Theorem §4.1]], $xy = b^u b^v = b^{u + v}$. By (6), $\log_b(xy) = u + v = \log_b x + \log_b y$.
> 2. By Law 2, $\dfrac{x}{y} = \dfrac{b^u}{b^v} = b^{u - v}$, so $\log_b(x/y) = u - v$.
> 3. By Law 3, $x^r = (b^u)^r = b^{ur}$, so $\log_b(x^r) = ur = r \log_b x$.

^pf-6-2

*Uses:* [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-1|Def. §6.1]], [[§4 Exponential Functions#^thm-4-1|§4.1]]

*Appendix G proves the laws for $\ln$ from the integral ([[§144 The Logarithm Defined as an Integral#^thm-144-2|Theorem §144.2]], with Law 3 for real $r$ in [[§145 General Exponential and Logarithmic Functions#^thm-145-1|Theorem §145.1]]) and for $\log_b$ by change of base ([[§145 General Exponential and Logarithmic Functions#^thm-145-4|Theorem §145.4]]).*

> [!remark]- Connections
> - Complex-variables version: [[§34 Some Identities Involving Logarithms#^thm-34-1|342 Thm. §34.1]] (Law 1 for the multiple-valued $\log z$, which holds as an equality of sets of values).

> [!example] Example §7.1: Expanding and Combining Logarithms
> **(a)** Evaluate $\log_2 80 - \log_2 5$. By Law 2,
>
> $$
> \log_2 80 - \log_2 5 = \log_2 \frac{80}{5} = \log_2 16 = 4 \qquad \text{because } 2^4 = 16 .
> $$
>
> **(b)** Expand $\ln \dfrac{x^2 \sqrt{x^2 + 2}}{3x + 1}$ (with $\ln = \log_e$, [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-2|Definition §6.2]] below). By Laws 1, 2 and 3,
>
> $$
> \ln \frac{x^2 \sqrt{x^2 + 2}}{3x + 1} = \ln x^2 + \ln \sqrt{x^2 + 2} - \ln(3x + 1) = 2 \ln x + \tfrac12 \ln(x^2 + 2) - \ln(3x + 1) .
> $$
>
> The laws need positive arguments, so this holds for $x > 0$. (The left side is also defined for $-\frac13 < x < 0$; there $\ln x^2 = 2 \ln|x|$.)
>
> **(c)** Express $\ln a + \frac12 \ln b$ as a single logarithm. By Laws 3 and 1,
>
> $$
> \ln a + \tfrac12 \ln b = \ln a + \ln b^{1/2} = \ln a + \ln \sqrt{b} = \ln\big(a \sqrt{b}\,\big) .
> $$
>
> *Stewart: Examples 1.5.6, 1.5.9 and 1.5.10*

^ex-6-1

## Natural Logarithms

The most convenient base for calculus is the number $e$ of [[§4 Exponential Functions#^def-4-4|Definition §4.4]], as Chapter 3 will show.

> [!definition] Definition §7.2: Natural Logarithm
> The logarithm with base $e$ is called the **natural logarithm** and has a special notation:
>
> $$
> \log_e x = \ln x .
> $$
>
> *Stewart: 1.5 (text)*

^def-6-2

*Appendix G develops the natural logarithm the other way round, rigorously: $\ln x = \int_1^x dt/t$ ([[§144 The Logarithm Defined as an Integral#^def-144-1|Definition §144.1]]), whose laws ([[§144 The Logarithm Defined as an Integral#^thm-144-2|Theorem §144.2]]) are proved by differentiation; $e$ is defined by $\ln e = 1$ ([[§144 The Logarithm Defined as an Integral#^def-144-2|Definition §144.2]]), $e^x$ as the inverse of $\ln$ ([[§144 The Logarithm Defined as an Integral#^def-144-3|Definition §144.3]]), and $\log_b$ as the inverse of $b^x$ ([[§145 General Exponential and Logarithmic Functions#^def-145-2|Definition §145.2]]). This supplies the existence statements that Sections 1.4 and 1.5 take on trust.*

> [!remark]- Remark: Notation for Logarithms
> Most calculus and science textbooks, and calculators, write $\ln x$ for the natural logarithm and $\log x$ for the "common logarithm" $\log_{10} x$. In more advanced mathematical and scientific literature and in computer languages, $\log x$ usually denotes the natural logarithm (the analysis notes, 451, write $\log$ this way).

^rem-6-3

> [!theorem] Corollary §6.3: Defining Properties of the Natural Logarithm
> $$
> \ln x = y \quad\Longleftrightarrow\quad e^y = x , \qquad (8)
> $$
>
> $$
> \ln(e^x) = x \quad (x \in \mathbb{R}), \qquad\qquad e^{\ln x} = x \quad (x > 0) , \qquad (9)
> $$
>
> and in particular
>
> $$
> \ln e = 1 .
> $$
>
> *Stewart: 1.5, Equations 8 and 9*

^cor-6-3

> [!proof]+ Proof
> Equations (8) and (9) are (6) and (7) with $b = e$ ([[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-1|Definition §6.1]] and [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-1|Theorem §6.1]]). Setting $x = 1$ in the first equation of (9) gives $\ln e = \ln(e^1) = 1$.

^pf-6-3

*Uses:* [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-1|Def. §6.1]], [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-1|§6.1]], [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-2|Def. §6.2]]

*In Appendix G, (8) and (9) define $e^x$ as the inverse of the integral logarithm: [[§144 The Logarithm Defined as an Integral#^def-144-3|Definition §144.3]], [[§144 The Logarithm Defined as an Integral#^def-144-4|Definition §144.4]].*

> [!remark]- Connections
> - Complex-variables version: [[§31 The Logarithmic Function#^def-31-1|342 Def. §31.1]] (the solutions $w$ of $e^w = z$, infinitely many for each $z \ne 0$) and [[§31 The Logarithmic Function#^def-31-2|342 Def. §31.2]] (the principal value $\operatorname{Log} z$, equal to $\ln x$ for $z = x > 0$).

> [!theorem] Proposition §6.4: Powers in Exponential Form
> For $x > 0$ and every real number $r$,
>
> $$
> x^r = e^{r \ln x} . \qquad (10)
> $$
>
> So a power of $x$ can be written in exponential form, which will be useful in the chapters to come.
>
> *Stewart: 1.5, Equation 10*

^prop-6-4

> [!proof]+ Proof
> Since $x^r > 0$, the second equation of (9) applies to it, and then Law 3 of logarithms ([[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-2|Theorem §6.2]]) gives
>
> $$
> x^r = e^{\ln(x^r)} = e^{r \ln x} .
> $$

^pf-6-4

*Uses:* [[§6 Logarithmic and Inverse Trigonometric Functions#^cor-6-3|§6.3]], [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-2|§6.2]]

> [!theorem] Theorem §6.5: Change of Base Formula
> For any positive number $b$ with $b \ne 1$,
>
> $$
> \log_b x = \frac{\ln x}{\ln b} \qquad (x > 0) .
> $$
>
> So logarithms with any base can be expressed through the natural logarithm; this is how a calculator computes (and graphs) $\log_b$.
>
> *Stewart: 1.5, Formula 11*

^thm-6-5

> [!proof]+ Proof
> Let $y = \log_b x$. By (6), $b^y = x$. Taking natural logarithms of both sides and using Law 3 of [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-2|Theorem §6.2]],
>
> $$
> \ln x = \ln(b^y) = y \ln b .
> $$
>
> Since $b \ne 1$ and $\ln$ is one-to-one with $\ln 1 = 0$ ([[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-1|Theorem §6.1]]), $\ln b \ne 0$. (Stewart divides without comment; this is why it is allowed.) Dividing by $\ln b$ gives $y = \dfrac{\ln x}{\ln b}$.

^pf-6-5

*Uses:* [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-1|Def. §6.1]], [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-1|§6.1]], [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-2|§6.2]]

*The same formula from the integral definition of $\ln$ in Appendix G: [[§145 General Exponential and Logarithmic Functions#^thm-145-4|Theorem §145.4]].*

> [!example] Example §7.2: Solving Equations with ln
> **(a)** Find $x$ if $\ln x = 5$.
>
> *From (8):* $\ln x = 5$ means $e^5 = x$. (If the notation is confusing, write $\log_e x = 5$; by the definition of logarithm, $e^5 = x$.)
>
> *By cancellation:* apply the exponential function to both sides, $e^{\ln x} = e^5$. The second equation of (9) says $e^{\ln x} = x$. Therefore $x = e^5$.
>
> **(b)** Solve $e^{5 - 3x} = 10$.
>
> Take natural logarithms of both sides and use the first equation of (9):
>
> $$
> \ln\big(e^{5 - 3x}\big) = \ln 10, \qquad 5 - 3x = \ln 10, \qquad 3x = 5 - \ln 10, \qquad x = \tfrac13 (5 - \ln 10) .
> $$
>
> Numerically, $\ln 10 \approx 2.302585$, so $x \approx \frac13 (2.697415) \approx 0.8991$.
>
> **(c)** Evaluate $\log_8 5$ to six decimal places. By the Change of Base Formula ([[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-5|Theorem §6.5]]),
>
> $$
> \log_8 5 = \frac{\ln 5}{\ln 8} \approx \frac{1.609438}{2.079442} \approx 0.773976 .
> $$
>
> *Stewart: Examples 1.5.7, 1.5.8 and 1.5.11*

^ex-6-2

### Graph and Growth of the Natural Logarithm

> [!theorem] Proposition §6.6: The Graph of the Natural Logarithm
> The graph of $y = \ln x$ is the reflection of the graph of $y = e^x$ about the line $y = x$. Like every logarithm with base greater than $1$, $\ln$ is an increasing function defined on $(0, \infty)$, and the $y$-axis is a vertical asymptote: the values of $\ln x$ become very large negative as $x$ approaches $0$. Although it increases, $\ln x$ grows *very* slowly for $x > 1$: more slowly than any positive power of $x$. For example, $y = \ln x$ and $y = \sqrt{x}$ grow at comparable rates at first, but eventually the root far surpasses the logarithm.
>
> *Stewart: 1.5 (text)*

^prop-6-6

*The first two statements are [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-1|Theorem §6.1]] with $b = e$ (since $e > 1$). The asymptote and the comparison with powers Stewart reads off graphs; they are proved as limits: $\lim_{x \to 0^+} \ln x = -\infty$ in [[§8 The Limit of a Function#^thm-8-1|Theorem §8.1]], and $\ln x / \sqrt{x} \to 0$ as $x \to \infty$, with l'Hospital's Rule, in [[§31 Indeterminate Forms and L'Hospital's Rule#^ex-31-1|Example §31.1]](c). Appendix G proves the shape and the limits of $\ln$ from the integral: [[§144 The Logarithm Defined as an Integral#^thm-144-3|Theorem §144.3]].*

The graphs of other logarithmic functions follow by the transformations of [[§3 New Functions from Old Functions#^thm-3-1|Theorem §3.1]]. For instance (Stewart, Example 1.5.12), $y = \ln(x - 2) - 1$ is $y = \ln x$ shifted $2$ units right and $1$ unit down: it has the vertical asymptote $x = 2$ and passes through $(3, -1)$, the image of $(1, 0)$.

## Inverse Trigonometric Functions

The trigonometric functions are not one-to-one (they are periodic), so they have no inverse functions. The difficulty is overcome by restricting their domains to intervals on which they are one-to-one and still take all their values.

> [!definition] Definition §7.3: Inverse Sine
> The sine function restricted to $[-\pi/2, \pi/2]$ is one-to-one and takes every value in $[-1, 1]$. Its inverse is the **inverse sine function** or **arcsine function**, denoted $\sin^{-1}$ or $\arcsin$:
>
> $$
> \sin^{-1} x = y \quad\Longleftrightarrow\quad \sin y = x \ \text{ and } \ -\frac{\pi}{2} \le y \le \frac{\pi}{2} .
> $$
>
> So for $-1 \le x \le 1$, $\sin^{-1} x$ is *the number between $-\pi/2$ and $\pi/2$ whose sine is $x$*. As with $f^{-1}$, the $-1$ is not an exponent: $\sin^{-1} x \ne \dfrac{1}{\sin x}$.
>
> *Stewart: 1.5 (text and box)*

^def-6-3

> [!definition] Definition §6.4: Inverse Cosine
> The cosine function restricted to $[0, \pi]$ is one-to-one. Its inverse is the **inverse cosine function**, denoted $\cos^{-1}$ or $\arccos$:
>
> $$
> \cos^{-1} x = y \quad\Longleftrightarrow\quad \cos y = x \ \text{ and } \ 0 \le y \le \pi .
> $$
>
> *Stewart: 1.5 (text and box)*

^def-6-4

> [!definition] Definition §6.5: Inverse Tangent
> The tangent function restricted to $(-\pi/2, \pi/2)$ is one-to-one. Its inverse is the **inverse tangent function**, denoted $\tan^{-1}$ or $\arctan$:
>
> $$
> \tan^{-1} x = y \quad\Longleftrightarrow\quad \tan y = x \ \text{ and } \ -\frac{\pi}{2} < y < \frac{\pi}{2} .
> $$
>
> *Stewart: 1.5 (text and box)*

^def-6-5

> [!theorem] Proposition §6.7: Domains, Ranges and Cancellation Equations
> | function | domain | range |
> |---|---|---|
> | $\sin^{-1} = \arcsin$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ |
> | $\cos^{-1} = \arccos$ | $[-1, 1]$ | $[0, \pi]$ |
> | $\tan^{-1} = \arctan$ | $\mathbb{R}$ | $(-\pi/2, \pi/2)$ |
>
> The cancellation equations are
>
> $$
> \begin{aligned}
> \sin^{-1}(\sin x) &= x \quad \text{for } -\tfrac{\pi}{2} \le x \le \tfrac{\pi}{2}, & \sin(\sin^{-1} x) &= x \quad \text{for } -1 \le x \le 1, \\
> \cos^{-1}(\cos x) &= x \quad \text{for } 0 \le x \le \pi, & \cos(\cos^{-1} x) &= x \quad \text{for } -1 \le x \le 1 .
> \end{aligned}
> $$
>
> The graph of $\tan^{-1}$ has the horizontal asymptotes $y = \pi/2$ and $y = -\pi/2$.
>
> *Stewart: 1.5 (text and boxes)*

^prop-6-7

> [!proof]+ Proof
> Each inverse function is the inverse of a one-to-one restricted function, so [[§5 Inverse Functions and Logarithms#^def-5-2|Definition §5.2]] applies to it. Its domain is the range of the restricted function and its range is the restricted interval. On $[-\pi/2, \pi/2]$ the sine increases from $-1$ to $1$, and on $[0, \pi]$ the cosine decreases from $1$ to $-1$, taking all values in between; on $(-\pi/2, \pi/2)$ the tangent increases and takes every real value. This gives the table. The cancellation equations are [[§5 Inverse Functions and Logarithms#^thm-5-2|Theorem §5.2]] for the restricted sine and cosine.
>
> The lines $x = \pm\pi/2$ are vertical asymptotes of $\tan$. The graph of $\tan^{-1}$ is the reflection of the graph of the restricted tangent about $y = x$ ([[§5 Inverse Functions and Logarithms#^thm-5-3|Theorem §5.3]]), and the reflection of a vertical line $x = c$ is the horizontal line $y = c$. So $y = \pm\pi/2$ are horizontal asymptotes of $\tan^{-1}$.

^pf-6-7

*Uses:* [[§5 Inverse Functions and Logarithms#^def-5-2|Def. §5.2]], [[§5 Inverse Functions and Logarithms#^thm-5-2|§5.2]], [[§5 Inverse Functions and Logarithms#^thm-5-3|§5.3]], [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-3|Def. §6.3]], [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-4|Def. §6.4]], [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-5|Def. §6.5]]

![[m233-5-2.svg]]
*Each inverse trigonometric function (red) is the reflection about $y = x$ (green, dashed) of the restricted trigonometric function (gray). (a) $\sin^{-1}$ from sine on $[-\pi/2, \pi/2]$: domain $[-1, 1]$, range $[-\pi/2, \pi/2]$. (b) $\cos^{-1}$ from cosine on $[0, \pi]$: domain $[-1, 1]$, range $[0, \pi]$, decreasing. (c) $\tan^{-1}$ from tangent on $(-\pi/2, \pi/2)$: domain $\mathbb{R}$; the vertical asymptotes $x = \pm\pi/2$ of tangent (gray, dashed) become the horizontal asymptotes $y = \pm\pi/2$ (red, dashed).*

The remaining inverse trigonometric functions are used less often.

> [!definition] Definition §6.6: Inverse Cosecant, Secant and Cotangent
> $$
> \begin{aligned}
> y = \csc^{-1} x \ \ (|x| \ge 1) \quad&\Longleftrightarrow\quad \csc y = x \ \text{ and } \ y \in (0, \pi/2] \cup (\pi, 3\pi/2] , \\
> y = \sec^{-1} x \ \ (|x| \ge 1) \quad&\Longleftrightarrow\quad \sec y = x \ \text{ and } \ y \in [0, \pi/2) \cup [\pi, 3\pi/2) , \\
> y = \cot^{-1} x \ \ (x \in \mathbb{R}) \quad&\Longleftrightarrow\quad \cot y = x \ \text{ and } \ y \in (0, \pi) .
> \end{aligned}
> $$
>
> The intervals for $y$ in $\csc^{-1}$ and $\sec^{-1}$ are not universally agreed upon. Some authors use $y \in [0, \pi/2) \cup (\pi/2, \pi]$ for $\sec^{-1}$; the graph of the secant shows that this choice also gives a one-to-one restriction taking every value with $|x| \ge 1$. Check which convention a formula assumes.
>
> *Stewart: 1.5, Equation 12*

^def-6-6

> [!example] Example §7.3: Evaluating and Simplifying Inverse Trigonometric Expressions
> **(a)** $\sin^{-1}\big(\frac12\big) = \dfrac{\pi}{6}$, because $\sin(\pi/6) = \frac12$ and $\pi/6$ lies between $-\pi/2$ and $\pi/2$. (Also $\sin(5\pi/6) = \frac12$, but $5\pi/6$ is outside the range of $\sin^{-1}$.)
>
> **(b)** Evaluate $\tan\big(\arcsin\frac13\big)$. Let $\theta = \arcsin\frac13$, so $\sin\theta = \frac13$ and $-\pi/2 \le \theta \le \pi/2$; since $\sin\theta > 0$, in fact $0 < \theta < \pi/2$. In a right triangle with angle $\theta$, opposite side $1$ and hypotenuse $3$, the Pythagorean Theorem gives the adjacent side $\sqrt{9 - 1} = 2\sqrt2$. So
>
> $$
> \tan\Big(\arcsin\frac13\Big) = \tan\theta = \frac{1}{2\sqrt2} = \frac{\sqrt2}{4} .
> $$
>
> **(c)** Simplify $\cos(\tan^{-1} x)$. Let $y = \tan^{-1} x$. Then $\tan y = x$ and $-\pi/2 < y < \pi/2$. Since $\tan y$ is known, find $\sec y$ first:
>
> $$
> \sec^2 y = 1 + \tan^2 y = 1 + x^2, \qquad \sec y = \sqrt{1 + x^2} ,
> $$
>
> taking the positive root because $\cos y > 0$, hence $\sec y > 0$, for $-\pi/2 < y < \pi/2$. Thus
>
> $$
> \cos(\tan^{-1} x) = \cos y = \frac{1}{\sec y} = \frac{1}{\sqrt{1 + x^2}} .
> $$
>
> Alternatively (for $y > 0$), draw a right triangle with angle $y$, opposite side $x$ and adjacent side $1$; its hypotenuse is $\sqrt{1 + x^2}$, and $\cos y = 1/\sqrt{1 + x^2}$ can be read off.
>
> *Stewart: Examples 1.5.13 and 1.5.14*

^ex-6-3
