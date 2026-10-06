---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 4
stewart: "1.4"
aliases: ["Stewart 1.4"]
tags: [calculus]
---
← [[§3 New Functions from Old Functions]] · ↑ [[· 1 Functions and Models]] · [[§5 Inverse Functions and Logarithms]] →

*Stewart, Section 1.4.*

An exponential function $b^x$ has the variable in the exponent. For integer and rational $x$ the meaning of $b^x$ comes from algebra; for irrational $x$ it is defined by filling in the holes of the graph, so that $b^x$ becomes an increasing (or decreasing) function on all of $\mathbb{R}$ with no gaps. The Laws of Exponents carry over to real exponents, and the graphs come in three kinds according to whether $b < 1$, $b = 1$ or $b > 1$. Exponentials model unlimited growth and decay, and one base, the number $e$, is singled out because the tangent line to $y = e^x$ at $(0, 1)$ has slope exactly $1$. The inverse of $b^x$, the logarithm, is the subject of [[§5 Inverse Functions and Logarithms|§5]].

## Exponential Functions and Their Graphs

> [!definition] Definition §4.1: Exponential Function
> An **exponential function** is a function of the form
>
> $$
> f(x) = b^x ,
> $$
>
> where the base $b$ is a positive constant. The variable is the *exponent*: $f(x) = 2^x$ is an exponential function, while $g(x) = x^2$, where the variable is the base, is a power function.
>
> *Stewart: 1.4 (text)*

^def-4-1

> [!definition] Definition §4.2: Integer and Rational Exponents
> Let $b > 0$.
> - If $n$ is a positive integer, $b^n = \underbrace{b \cdot b \cdots b}_{n \text{ factors}}$.
> - $b^0 = 1$, and $b^{-n} = \dfrac{1}{b^n}$ for every positive integer $n$.
> - If $x = p/q$ is rational, with $p$ and $q$ integers and $q > 0$, then
>
> $$
> b^x = b^{p/q} = \sqrt[q]{b^p} = \big(\sqrt[q]{b}\,\big)^p .
> $$
>
> *Stewart: 1.4 (text)*

^def-4-2

This gives $b^x$ for every rational $x$. Plotting $y = 2^x$ at the rational numbers only gives a graph full of holes, one at each irrational $x$. What should $2^{\sqrt3}$ or $5^\pi$ mean?

> [!definition] Definition §4.3: Irrational Exponents
> Let $b > 1$ and let $x$ be irrational. There is exactly one number that is greater than $b^r$ for every rational $r < x$ and less than $b^s$ for every rational $s > x$. This number is defined to be $b^x$. (For $0 < b < 1$ the inequalities are reversed, and $1^x = 1$.)
>
> In practice one squeezes $x$ between finite decimals. For $2^{\sqrt3}$:
>
> $$
> \begin{aligned}
> 1.7 < \sqrt3 < 1.8 \quad&\Longrightarrow\quad 2^{1.7} < 2^{\sqrt3} < 2^{1.8}, \\
> 1.73 < \sqrt3 < 1.74 \quad&\Longrightarrow\quad 2^{1.73} < 2^{\sqrt3} < 2^{1.74}, \\
> 1.732 < \sqrt3 < 1.733 \quad&\Longrightarrow\quad 2^{1.732} < 2^{\sqrt3} < 2^{1.733}, \\
> 1.7320 < \sqrt3 < 1.7321 \quad&\Longrightarrow\quad 2^{1.7320} < 2^{\sqrt3} < 2^{1.7321}, \\
> 1.73205 < \sqrt3 < 1.73206 \quad&\Longrightarrow\quad 2^{1.73205} < 2^{\sqrt3} < 2^{1.73206},
> \end{aligned}
> $$
>
> and so on. The exponents on the left and right are rational, so all these bounds are already defined, and $2^{\sqrt3}$ is the one number caught between them: $2^{\sqrt3} \approx 3.321997$.
>
> The definition is made so that $f(x) = b^x$, $x \in \mathbb{R}$, is an increasing function for $b > 1$ (decreasing for $b < 1$): every hole of the rational graph is filled by the only value that keeps the order. The completed graph has no holes or breaks, which is why $b^x$ is continuous on $\mathbb{R}$ ([[§12 Continuity#^thm-12-6|Theorem §12.6]]).
>
> *Stewart: 1.4 (text)*

^def-4-3

*Stewart omits the proof that exactly one such number exists, citing J. Marsden and A. Weinstein, "Calculus Unlimited" (1981). An alternative construction of $b^x$, through the logarithm defined as an integral, is in Appendix G: $\ln$ is defined as an integral in [[§144 The Logarithm Defined as an Integral#^def-144-1|Definition §144.1]], $e^x$ as its inverse in [[§144 The Logarithm Defined as an Integral#^def-144-3|Definition §144.3]], and $b^x = e^{x \ln b}$ in [[§145 General Exponential and Logarithmic Functions#^def-145-1|Definition §145.1]], which agrees with [[§4 Exponential Functions#^def-4-2|Definition §4.2]] for rational $x$ ([[§144 The Logarithm Defined as an Integral#^prop-144-4|Proposition §144.4]]) and with [[§4 Exponential Functions#^def-4-3|Definition §4.3]] for irrational $x$ ([[§145 General Exponential and Logarithmic Functions#^rem-145-1|Remark: Dictionary with Chapters 1 and 3]]).*

![[m233-4-2.svg]]
*(a) $y = 2^x$ plotted at rational $x$ only (here at multiples of $\frac18$); between any two plotted points there are holes at the irrational numbers. (b) Filling the hole at $\sqrt3$: the rational bounds $1.7 < \sqrt3 < 1.8$ (orange) trap $2^{\sqrt3}$ between $2^{1.7} \approx 3.249$ and $2^{1.8} \approx 3.482$, and the finer bounds $1.73 < \sqrt3 < 1.74$ (red) trap it between $2^{1.73} \approx 3.317$ and $2^{1.74} \approx 3.340$. The nested ranges on the $y$-axis shrink to the single value $2^{\sqrt3} \approx 3.322$ (black dot).*

> [!remark]- Connections
> - For $b > 1$, existence is the completeness axiom ([[§4 The Completeness Axiom#^def-4-4|451 Def. §4.4]]): $b^x = \sup\{b^r \mid r \in \mathbb{Q},\ r < x\}$. A continuous function on an interval is determined by its values at the rationals ([[§17 Continuous Functions#^prop-17-6|451 Prop. §17.6]]), so there is at most one continuous way to fill the holes.
> - 451 itself never constructs $b^x$ or $e^x$: it uses them on credit, as recorded in [[§34 Fundamental Theorem of Calculus#^rem-34-4|451 Remark: Closing the ledger]].

> [!theorem] Theorem §4.1: Laws of Exponents
> If $a$ and $b$ are positive numbers and $x$ and $y$ are any real numbers, then
>
> $$
> 1.\ b^{x+y} = b^x b^y \qquad 2.\ b^{x-y} = \frac{b^x}{b^y} \qquad 3.\ (b^x)^y = b^{xy} \qquad 4.\ (ab)^x = a^x b^x .
> $$
>
> *Stewart: 1.4, Laws of Exponents*

^thm-4-1

*For rational $x$ and $y$ these are the laws of elementary algebra; Stewart states that they remain true for all real $x$ and $y$ ("it can be proved") but gives no proof in 1.4. Appendix G proves them from the integral definition of $\ln$: [[§144 The Logarithm Defined as an Integral#^thm-144-6|Theorem §144.6]] (for base $e$) and [[§145 General Exponential and Logarithmic Functions#^thm-145-2|Theorem §145.2]] (any base).*

> [!theorem] Proposition §4.2: The Three Kinds of Exponential Functions
> Let $b > 0$.
> 1. Every graph $y = b^x$ passes through $(0, 1)$, since $b^0 = 1$.
> 2. If $0 < b < 1$, then $b^x$ is decreasing; if $b = 1$, it is the constant $1$; if $b > 1$, it is increasing. The larger the base $b > 1$, the faster $b^x$ grows for $x > 0$.
> 3. If $b \ne 1$, then $y = b^x$ has domain $\mathbb{R}$ and range $(0, \infty)$.
> 4. Since $(1/b)^x = 1/b^x = b^{-x}$, the graph of $y = (1/b)^x$ is the reflection of the graph of $y = b^x$ about the $y$-axis.
>
> In both cases $b \ne 1$ the $x$-axis is a horizontal asymptote: $b^x \to 0$ as $x \to \infty$ if $b < 1$, and as $x \to -\infty$ if $b > 1$ ([[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-2|Definition §13.2]]; for $b = e$, [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-4|Theorem §13.4]]).
>
> *Stewart: 1.4 (text)*

^prop-4-2

*Stewart reads parts 2 and 3 off the graphs (his Figures 3 and 4). Appendix G proves the monotonicity from the derivative $\frac{d}{dx} b^x = b^x \ln b$: [[§145 General Exponential and Logarithmic Functions#^thm-145-3|Theorem §145.3]].*

> [!proof]+ Proof
> *Of part 4, the only part Stewart justifies.* By [[§4 Exponential Functions#^def-4-2|Definition §4.2]], $1/b > 0$ and $1/b = b^{-1}$. Law 3 of [[§4 Exponential Functions#^thm-4-1|Theorem §4.1]] gives $(1/b)^x = (b^{-1})^x = b^{-x}$. Law 1 gives $b^x \cdot b^{-x} = b^{0} = 1$, so $b^{-x} = 1/b^x$. Hence the point $(x, y)$ is on the graph of $y = b^x$ exactly when $(-x, y)$ is on the graph of $y = (1/b)^x$: the two graphs are mirror images in the $y$-axis.

^pf-4-2

*Uses:* [[§4 Exponential Functions#^def-4-2|Def. §4.2]], [[§4 Exponential Functions#^thm-4-1|§4.1]]

> [!example] Example §4.1: Reflecting and Shifting an Exponential
> Sketch the graph of $y = 3 - 2^x$ and determine its domain and range.
>
> Build the graph from $y = 2^x$ with the transformations of [[§3 New Functions from Old Functions#^thm-3-2|Theorem §3.2]] (reflection) and [[§3 New Functions from Old Functions#^thm-3-1|Theorem §3.1]] (shift):
> 1. Reflect $y = 2^x$ about the $x$-axis to get $y = -2^x$. It passes through $(0, -1)$, decreases, and approaches $0$ from below as $x \to -\infty$.
> 2. Shift up $3$ units to get $y = 3 - 2^x$. It passes through $(0, 2)$, crosses the $x$-axis where $2^x = 3$, and approaches the horizontal asymptote $y = 3$ from below as $x \to -\infty$.
>
> **Domain and range.** $2^x$ is defined for every $x$, so the domain is $\mathbb{R}$. By [[§4 Exponential Functions#^prop-4-2|Proposition §4.2]], $2^x$ takes exactly the values in $(0, \infty)$, so $-2^x$ takes the values in $(-\infty, 0)$ and $3 - 2^x$ the values in $(-\infty, 3)$. The range is $(-\infty, 3)$.
>
> *Stewart: Example 1.4.1*

^ex-4-1

> [!example] Example §4.2: Exponential Versus Power Growth
> Compare $f(x) = 2^x$ with $g(x) = x^2$. Which grows more quickly when $x$ is large?
>
> A table of values:
>
> | $x$ | $-1$ | $0$ | $2$ | $3$ | $4$ | $5$ | $6$ | $10$ | $20$ |
> |---|---|---|---|---|---|---|---|---|---|
> | $2^x$ | $0.5$ | $1$ | $4$ | $8$ | $16$ | $32$ | $64$ | $1024$ | $1\,048\,576$ |
> | $x^2$ | $1$ | $0$ | $4$ | $9$ | $16$ | $25$ | $36$ | $100$ | $400$ |
>
> The graphs cross three times: at $x = 2$, at $x = 4$, and once between $-1$ and $0$ (a graphing device gives $x \approx -0.767$). Between $2$ and $4$ the parabola is on top, but for $x > 4$ the exponential stays above, and the gap explodes. Stewart reads this off a graph. For integers it is a short induction: if $2^n > n^2$ for some $n \ge 5$, then
>
> $$
> 2^{n+1} = 2 \cdot 2^n > 2n^2 = (n+1)^2 + (n^2 - 2n - 1) > (n+1)^2 ,
> $$
>
> since $n^2 - 2n - 1 = (n - 1)^2 - 2 > 0$ for $n \ge 3$; and $2^5 = 32 > 25 = 5^2$ starts the induction.
>
> Stewart's margin illustration: a sheet of paper $\frac{1}{1000}$ inch thick folded in half $50$ times would be $2^{50}/1000 \approx 1.126 \times 10^{12}$ inches thick, and since a mile is $63\,360$ inches, that is about $1.78 \times 10^7$ miles, more than $17$ million miles.
>
> *Stewart: Example 1.4.2*

^ex-4-2

## Applications of Exponential Functions

> [!example] Example §4.3: Bacteria That Double Every Hour
> A population of bacteria doubles every hour, starting from $p(0) = 1000$ at time $t = 0$ ($t$ in hours). Then
>
> $$
> p(1) = 2p(0) = 2 \times 1000, \qquad p(2) = 2p(1) = 2^2 \times 1000, \qquad p(3) = 2p(2) = 2^3 \times 1000 ,
> $$
>
> and the pattern suggests $p(t) = 1000 \cdot 2^t$. This is a constant multiple of $y = 2^t$, so it grows as fast as [[§4 Exponential Functions#^ex-4-2|Example §4.2]] showed. Under ideal conditions (unlimited space and nutrition, no disease) this exponential growth is what actually happens in nature.
>
> *Stewart: 1.4 (text)*

^ex-4-3

*Chain:* [[§23 Rates of Change in the Natural and Social Sciences#^ex-23-3|Chapter 3]] →

> [!remark]- Remark: Exponential Models from Data
> Data that grow or decay like an exponential are fitted by a model $y = a \cdot b^t$ (by least squares, with technology). Stewart's two examples:
> - World population in the 20th century ($t$ = years since 1900): $P(t) = (1.43653 \times 10^9) \cdot (1.01395)^t$. Here $b > 1$: growth. The slow stretch of the data is explained by the two world wars and the Great Depression. (Example 1.4.3)
> - Plasma viral load of an HIV patient $t$ days after starting the protease inhibitor ABT-538 (D. Ho et al., *Nature* 373, 1995): $V = 96.39785 \cdot (0.818656)^t$ RNA copies/mL. Here $b < 1$: decay. It fits well for the first month of treatment. (Example 1.4.4)
>
> Compound interest and radioactive decay follow in Section 3.8 ([[§24 Exponential Growth and Decay|§24]]).

^rem-4-1

## The Number e

Of all bases, one is most convenient for calculus. The choice is governed by how the graph $y = b^x$ crosses the $y$-axis: the tangent line to $y = 2^x$ at $(0, 1)$ has slope $m \approx 0.7$, and the one to $y = 3^x$ has slope $m \approx 1.1$. (Tangent lines are defined precisely in Section 2.7, [[§14 Derivatives and Rates of Change#^def-14-1|Definition §14.1]]; for now, think of the line that touches the graph only at that point. See [[§7 The Tangent and Velocity Problems#^def-7-2|Definition §7.2]].) The formulas of calculus become simplest when this slope is exactly $1$.

> [!definition] Definition §4.4: The Number e
> The number $e$ is the base $b$ for which the tangent line to $y = b^x$ at the point $(0, 1)$ has slope exactly $1$. Correct to five decimal places,
>
> $$
> e \approx 2.71828 .
> $$
>
> The function $f(x) = e^x$ is called the **natural exponential function**.
>
> Since the slope at $(0, 1)$ is about $0.7$ for base $2$ and about $1.1$ for base $3$, we expect $2 < e < 3$, and the graph of $y = e^x$ lies between those of $y = 2^x$ and $y = 3^x$. The name $e$ is due to Euler (1727), probably for "exponential".
>
> *Stewart: 1.4 (text)*

^def-4-4

*Stewart only asserts that such a base exists. Chapter 3 restates the definition as $\lim_{h \to 0} (e^h - 1)/h = 1$ ([[§17 Derivatives of Polynomials and Exponential Functions#^def-17-2|Definition §17.2]]) and obtains the value $2.71828$ from $e = \lim_{x \to 0}(1 + x)^{1/x}$ ([[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-7|Theorem §22.7]]). A rigorous construction is in Appendix G: $e$ is the number with $\ln e = 1$ ([[§144 The Logarithm Defined as an Integral#^def-144-2|Definition §144.2]]), $\frac{d}{dx} e^x = e^x$ ([[§144 The Logarithm Defined as an Integral#^thm-144-7|Theorem §144.7]]), and $e = \lim_{x \to 0}(1 + x)^{1/x}$ ([[§145 General Exponential and Logarithmic Functions#^thm-145-5|Theorem §145.5]]).*

![[m233-4-1.svg]]
*Tangent lines (red) to $y = 2^x$, $y = e^x$ and $y = 3^x$ (blue) at the common point $(0, 1)$. Their slopes increase with the base: about $0.69$, exactly $1$, about $1.10$. (Chapter 3 shows that the slope for base $b$ is $\ln b$.) The base $e$ is the one in between whose tangent line is $y = x + 1$.*

> [!remark]- Connections
> - In 451, $e^x$ appears as the power series $\sum_{n \ge 0} x^n/n!$ with radius of convergence $+\infty$ ([[§23 Power Series#^rem-23-2|451 Remark: Why centered series?]]); it is continuous by [[§26 Differentiation and Integration of Power Series#^cor-26-2|451 Cor. §26.2]], and its derivative at $0$ is $1$ by term-by-term differentiation ([[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]]), which is [[§4 Exponential Functions#^def-4-4|Definition §4.4]].

> [!example] Example §4.4: Transforming the Natural Exponential
> Graph $y = \frac12 e^{-x} - 1$ and state the domain and range.
>
> Start from $y = e^x$ and use the transformations of [[§3 New Functions from Old Functions#^thm-3-2|Theorem §3.2]] (reflection, compression) and [[§3 New Functions from Old Functions#^thm-3-1|Theorem §3.1]] (shift):
> 1. Reflect about the $y$-axis: $y = e^{-x}$. It is decreasing, passes through $(0, 1)$, and its tangent line there has slope $-1$ (the mirror image of the slope-$1$ tangent of $e^x$).
> 2. Compress vertically by a factor of $2$: $y = \frac12 e^{-x}$, through $(0, \frac12)$.
> 3. Shift down $1$ unit: $y = \frac12 e^{-x} - 1$, through $(0, -\frac12)$, with horizontal asymptote $y = -1$ as $x \to \infty$.
>
> **Domain and range.** The domain is $\mathbb{R}$. Since $e^{-x}$ takes all values in $(0, \infty)$ ([[§4 Exponential Functions#^prop-4-2|Proposition §4.2]], part 3, with $x$ replaced by $-x$), $\frac12 e^{-x}$ takes all values in $(0, \infty)$ as well, and $\frac12 e^{-x} - 1$ takes all values in $(-1, \infty)$. The range is $(-1, \infty)$.
>
> *Stewart: Example 1.4.5*

^ex-4-4

> [!example] Example §4.5: When Does the Exponential Pass a Million?
> Find the values of $x$ for which $e^x > 1\,000\,000$.
>
> Stewart graphs $y = e^x$ and $y = 10^6$ together: the curves cross at $x \approx 13.8$, so $e^x > 10^6$ when $x > 13.8$. The exponential has passed a million already at $x = 14$.
>
> With the natural logarithm of [[§5 Inverse Functions and Logarithms|§5]] the answer is exact. Since $\ln$ is increasing, $e^x > 10^6$ if and only if $x = \ln(e^x) > \ln 10^6 = 6 \ln 10$ ([[§6 Logarithmic and Inverse Trigonometric Functions#^cor-6-3|Corollary §6.3]] and Law 3 of [[§6 Logarithmic and Inverse Trigonometric Functions#^thm-6-2|Theorem §6.2]]). So the answer is $x > 6 \ln 10 \approx 6 \times 2.302585 \approx 13.8155$.
>
> *Stewart: Example 1.4.6*

^ex-4-5
