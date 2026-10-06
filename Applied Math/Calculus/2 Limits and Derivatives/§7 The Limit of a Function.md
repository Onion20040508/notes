---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 7
stewart: "2.2"
aliases: ["Stewart 2.2"]
tags: [calculus]
---
← [[§6 The Tangent and Velocity Problems]] · ↑ [[· 2 Limits and Derivatives]] · [[§8 Calculating Limits Using the Limit Laws]] →

*Stewart, Section 2.2.*

The tangent and velocity problems of [[§6 The Tangent and Velocity Problems|§6]] both ask what a quantity approaches. This section says what "the limit of $f(x)$ as $x$ approaches $a$" means, intuitively: the values $f(x)$ can be made as close to $L$ as we like by taking $x$ close enough to $a$, with $x \ne a$. Tables of values and graphs suggest limits, but the examples show how they can mislead, which is why [[§8 Calculating Limits Using the Limit Laws|§8]] computes limits exactly and [[§9 The Precise Definition of a Limit|§9]] makes the definition precise. One-sided limits (approach from one side only) and infinite limits (values growing without bound) describe the ways a limit can fail to exist. Infinite limits locate the vertical asymptotes of a graph.

## Finding Limits Numerically and Graphically

For $f(x) = (x - 1)/(x^2 - 1)$, the values at $x = 0.9, 0.99, 0.999$ are $0.526316$, $0.502513$, $0.500250$, and at $x = 1.1, 1.01, 1.001$ they are $0.476190$, $0.497512$, $0.499750$. The closer $x$ is to $1$, from either side, the closer $f(x)$ is to $0.5$, although $f(1)$ is not defined. (Indeed $f(x) = 1/(x + 1)$ for $x \ne \pm 1$.) We write $\lim_{x \to 1} f(x) = 0.5$.

> [!definition] Definition §7.1: The Limit of a Function (Intuitive)
> Suppose $f(x)$ is defined when $x$ is near the number $a$, that is, on some open interval that contains $a$, except possibly at $a$ itself. We write
>
> $$
> \lim_{x \to a} f(x) = L
> $$
>
> and say "the limit of $f(x)$, as $x$ approaches $a$, equals $L$" if we can make the values of $f(x)$ arbitrarily close to $L$ (as close to $L$ as we like) by restricting $x$ to be sufficiently close to $a$ (on either side of $a$) but not equal to $a$.
>
> Another notation is $f(x) \to L$ as $x \to a$, read "$f(x)$ approaches $L$ as $x$ approaches $a$."
>
> *Stewart: 2.2, Definition 1*

^def-7-1

> [!remark] Remark: Only the Values Near a Matter
> Because of "but not equal to $a$", the value $f(a)$ plays no role: $f(a)$ may equal $L$, may be some other number, or may not be defined at all, and in each case $\lim_{x \to a} f(x) = L$ can hold. Only how $f$ is defined *near* $a$ matters. The word "arbitrarily" is what the precise definition ([[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]) turns into "for every $\varepsilon > 0$".

^rem-7-1

> [!remark]- Connections
> - Rigorous treatment: 451 defines the limit through sequences, [[§20 Limits of Functions#^def-20-1|451 Def. §20.1]] ($f(x_n) \to L$ for every sequence $x_n \to a$ with $x_n \ne a$), and gives the equivalent $\varepsilon$–$\delta$ form in [[§20 Limits of Functions#^rem-20-1|451 Remark: The epsilon-delta version]].

> [!example] Example §7.1: Guessing a Limit from a Table
> **(a)** Estimate $\displaystyle\lim_{t \to 0} \frac{\sqrt{t^2 + 9} - 3}{t^2}$.
>
> | $t$ | $\pm 1.0$ | $\pm 0.5$ | $\pm 0.1$ | $\pm 0.05$ | $\pm 0.01$ |
> |---|---|---|---|---|---|
> | value | $0.162277\ldots$ | $0.165525\ldots$ | $0.166620\ldots$ | $0.166655\ldots$ | $0.166666\ldots$ |
>
> The values seem to approach $0.1666\ldots$, so we guess that the limit is $\frac16$. (The function is even, so $t$ and $-t$ give the same value.)
>
> A calculator taken further gives $0.166667$, $0.166670$, $0.167000$ and finally $0.000000$ at $t = \pm 0.000001$. The limit is not $0$; it is $\frac16$, as [[§8 Calculating Limits Using the Limit Laws#^ex-8-3|Example §8.3]] proves. For very small $t$, $\sqrt{t^2 + 9}$ is so close to $3$ that the calculator stores it as $3.000\ldots0$ to all the digits it carries, and the subtraction $\sqrt{t^2 + 9} - 3$ returns $0$. Graphs zoomed in too far fail in the same way.
>
> **(b)** Guess $\displaystyle\lim_{x \to 0} \frac{\sin x}{x}$.
>
> The function is not defined at $0$. With $x$ in radians:
>
> | $x$ | $\pm 1.0$ | $\pm 0.5$ | $\pm 0.1$ | $\pm 0.01$ | $\pm 0.001$ |
> |---|---|---|---|---|---|
> | $\frac{\sin x}{x}$ | $0.84147098$ | $0.95885108$ | $0.99833417$ | $0.99998333$ | $0.99999983$ |
>
> We guess $\lim_{x \to 0} \frac{\sin x}{x} = 1$. The guess is correct; it is proved geometrically in Section 3.3 ([[§16 Derivatives of Trigonometric Functions#^thm-16-6|Theorem §16.6]]).
>
> *Stewart: Examples 2.2.1 and 2.2.2*

^ex-7-1

> [!example] Example §7.2: When Guessing Fails
> **(a)** Find $\displaystyle\lim_{x \to 0} \Big(x^3 + \frac{\cos 5x}{10{,}000}\Big)$.
>
> | $x$ | $1$ | $0.5$ | $0.1$ | $0.05$ | $0.01$ | $0.005$ | $0.001$ |
> |---|---|---|---|---|---|---|---|
> | value | $1.000028$ | $0.124920$ | $0.001088$ | $0.000222$ | $0.000101$ | $0.00010009$ | $0.00010000$ |
>
> The first five values suggest the limit $0$. Smaller $x$ show that it is $0.0001$. Indeed, $x^3 \to 0$ and $\cos 5x \to 1$ as $x \to 0$ (cosine is continuous, [[§10 Continuity#^thm-10-6|Theorem §10.6]]), so the limit is $\frac{1}{10{,}000} = 0.0001$. The lesson: one cannot know when to stop computing values.
>
> **(b)** Investigate $\displaystyle\lim_{x \to 0} \sin\frac{\pi}{x}$.
>
> The function $f(x) = \sin(\pi/x)$ is undefined at $0$. Its values at $x = 1, \frac12, \frac13, \frac14, 0.1, 0.01$ are
>
> $$
> \sin\pi = \sin 2\pi = \sin 3\pi = \sin 4\pi = \sin 10\pi = \sin 100\pi = 0 ,
> $$
>
> and in general $f(1/n) = \sin n\pi = 0$ for every integer $n$. This suggests the limit $0$, and the guess is **wrong**. At $x = \frac{2}{4k + 1}$ ($k = 1, 2, \ldots$), for instance $x = \frac25$ or $\frac{2}{101}$, we get $f(x) = \sin\big(2k\pi + \frac{\pi}{2}\big) = 1$, and these $x$ also approach $0$. As $x \to 0$, $\pi/x$ runs through infinitely many full periods of sine, so $\sin(\pi/x)$ oscillates between $-1$ and $1$ infinitely often. Its values approach no fixed number, and
>
> $$
> \lim_{x \to 0} \sin\frac{\pi}{x} \quad \text{does not exist.}
> $$
>
> The lesson: the sample points can be badly chosen. Calculus software therefore does not guess limits from values; [[§8 Calculating Limits Using the Limit Laws|§8]] gives methods that do not depend on them.
>
> *Stewart: Examples 2.2.3 and 2.2.5*

^ex-7-2

## One-Sided Limits

The Heaviside function $H(t) = 0$ for $t < 0$ and $H(t) = 1$ for $t \ge 0$ (a current switched on at time $t = 0$) approaches no single number as $t \to 0$, so $\lim_{t \to 0} H(t)$ does not exist. But as $t$ approaches $0$ from the left, $H(t)$ approaches $0$, and from the right it approaches $1$. We write $\lim_{t \to 0^-} H(t) = 0$ and $\lim_{t \to 0^+} H(t) = 1$.

> [!definition] Definition §7.2: One-Sided Limits (Intuitive)
> We write
>
> $$
> \lim_{x \to a^-} f(x) = L
> $$
>
> and say that the **left-hand limit** of $f(x)$ as $x$ approaches $a$ (the limit of $f(x)$ as $x$ approaches $a$ *from the left*) is $L$, if we can make the values of $f(x)$ arbitrarily close to $L$ by restricting $x$ to be sufficiently close to $a$ with $x$ less than $a$.
>
> Likewise
>
> $$
> \lim_{x \to a^+} f(x) = L
> $$
>
> says that the **right-hand limit** of $f(x)$ as $x$ approaches $a$ (from the right) is $L$: the values of $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $a$ with $x$ greater than $a$.
>
> So $x \to 5^-$ means that only $x < 5$ are considered, and $x \to 5^+$ that only $x > 5$ are.
>
> *Stewart: 2.2, Definition 2*

^def-7-2

> [!remark]- Connections
> - In 451 a one-sided limit is a limit through the interval on one side of $a$, [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]]; the Heaviside function is [[§20 Limits of Functions#^ex-20-2|451 Ex. §20.2]].

[[§7 The Limit of a Function#^def-7-2|Definition §7.2]] differs from [[§7 The Limit of a Function#^def-7-1|Definition §7.1]] only in requiring $x < a$ (or $x > a$). Comparing the two shows that $\lim_{x \to a} f(x) = L$ holds exactly when both one-sided limits exist and equal $L$. This is [[§8 Calculating Limits Using the Limit Laws#^thm-8-5|Theorem §8.5]], proved there from the precise definitions.

> [!example] Example §7.3: Reading One-Sided Limits from a Graph
> Let
>
> $$
> g(x) = \begin{cases} 3 - \frac12 (x - 2)^2 & \text{if } x < 2 \\[3pt] 2 - \frac19 (x - 5)^2 & \text{if } x > 2,\ x \ne 5 \\[3pt] 1 & \text{if } x = 5, \end{cases}
> $$
>
> graphed in the figure below. Find, if they exist: (a) $\lim_{x \to 2^-} g(x)$, (b) $\lim_{x \to 2^+} g(x)$, (c) $\lim_{x \to 2} g(x)$, (d) $\lim_{x \to 5^-} g(x)$, (e) $\lim_{x \to 5^+} g(x)$, (f) $\lim_{x \to 5} g(x)$.
>
> **(a), (b)** As $x$ approaches $2$ from the left, $g(x) = 3 - \frac12 (x - 2)^2$ approaches $3$. From the right, $g(x) = 2 - \frac19 (x - 5)^2$ approaches $2 - \frac19 (2 - 5)^2 = 2 - 1 = 1$. So $\lim_{x \to 2^-} g(x) = 3$ and $\lim_{x \to 2^+} g(x) = 1$.
>
> **(c)** The one-sided limits at $2$ are different, so $\lim_{x \to 2} g(x)$ does not exist ([[§8 Calculating Limits Using the Limit Laws#^thm-8-5|Theorem §8.5]]). ($g(2)$ is not even defined.)
>
> **(d), (e)** Near $5$, on both sides, $g(x) = 2 - \frac19 (x - 5)^2$, which approaches $2$. So both one-sided limits at $5$ equal $2$.
>
> **(f)** The one-sided limits agree, so $\lim_{x \to 5} g(x) = 2$. Notice that $g(5) = 1 \ne 2$: the value at $5$ does not affect the limit.
>
> *Stewart: Example 2.2.4 (with a formula for $g$ in place of Stewart's graph)*

^ex-7-3

![[m233-7-1.svg]]
*The function $g$ of [[§7 The Limit of a Function#^ex-7-3|Example §7.3]]. At $x = 2$ the graph breaks: from the left it runs into the open circle at height $3$, from the right into the open circle at height $1$, so the two one-sided limits differ and $\lim_{x \to 2} g(x)$ does not exist. At $x = 5$ both sides run into the open circle at height $2$, so $\lim_{x \to 5} g(x) = 2$, even though the value $g(5) = 1$ (red dot) lies elsewhere.*

## How Can a Limit Fail to Exist?

A limit at $a$ fails to exist if the one-sided limits differ ([[§7 The Limit of a Function#^ex-7-3|Example §7.3]](c)), or if the values oscillate without settling down ([[§7 The Limit of a Function#^ex-7-2|Example §7.2]](b)). A third way is that the values grow without bound.

> [!example] Example §7.4: Values That Grow Without Bound
> Find $\displaystyle\lim_{x \to 0} \frac{1}{x^2}$ if it exists.
>
> | $x$ | $\pm 1$ | $\pm 0.5$ | $\pm 0.2$ | $\pm 0.1$ | $\pm 0.05$ | $\pm 0.01$ | $\pm 0.001$ |
> |---|---|---|---|---|---|---|---|
> | $1/x^2$ | $1$ | $4$ | $25$ | $100$ | $400$ | $10{,}000$ | $1{,}000{,}000$ |
>
> As $x$ approaches $0$, $x^2$ approaches $0$ and $1/x^2$ becomes very large. In fact $1/x^2$ exceeds any given number once $x$ is close enough to $0$ (for instance $1/x^2 > 10^6$ when $0 < |x| < 0.001$). The values do not approach a number, so $\lim_{x \to 0} (1/x^2)$ does not exist.
>
> *Stewart: Example 2.2.6*

^ex-7-4

## Infinite Limits; Vertical Asymptotes

To describe the behavior in [[§7 The Limit of a Function#^ex-7-4|Example §7.4]] we write $\lim_{x \to 0} \frac{1}{x^2} = \infty$. This does not treat $\infty$ as a number, and it does not say that the limit exists. It records the particular way in which the limit fails to exist.

> [!definition] Definition §7.3: Infinite Limit
> Let $f$ be a function defined on both sides of $a$, except possibly at $a$ itself. Then
>
> $$
> \lim_{x \to a} f(x) = \infty
> $$
>
> means that the values of $f(x)$ can be made arbitrarily large (as large as we please) by taking $x$ sufficiently close to $a$, but not equal to $a$.
>
> Other notation: $f(x) \to \infty$ as $x \to a$. It is read "the limit of $f(x)$, as $x$ approaches $a$, is infinity", or "$f(x)$ becomes infinite as $x$ approaches $a$", or "$f(x)$ increases without bound as $x$ approaches $a$".
>
> *Stewart: 2.2, Definition 4*

^def-7-3

> [!definition] Definition §7.4: Negative Infinite Limit
> Let $f$ be a function defined on both sides of $a$, except possibly at $a$ itself. Then
>
> $$
> \lim_{x \to a} f(x) = -\infty
> $$
>
> means that the values of $f(x)$ can be made arbitrarily large negative (negative with absolute value as large as we please) by taking $x$ sufficiently close to $a$, but not equal to $a$. It is read "the limit of $f(x)$, as $x$ approaches $a$, is negative infinity", or "$f(x)$ decreases without bound as $x$ approaches $a$". For example, $\lim_{x \to 0} (-1/x^2) = -\infty$.
>
> *Stewart: 2.2, Definition 5 and text*

^def-7-4

> [!definition] Definition §7.4: One-Sided Infinite Limits
> The **one-sided infinite limits**
>
> $$
> \lim_{x \to a^-} f(x) = \infty, \qquad \lim_{x \to a^+} f(x) = \infty, \qquad \lim_{x \to a^-} f(x) = -\infty, \qquad \lim_{x \to a^+} f(x) = -\infty
> $$
>
> are defined in the same way, considering only $x < a$ (for $x \to a^-$) or only $x > a$ (for $x \to a^+$).
>
> *Stewart: 2.2, Definition 5 and text*

^def-7-new1

> [!remark]- Connections
> - Rigorous treatment: 451 allows $L = \pm\infty$ in [[§20 Limits of Functions#^def-20-1|451 Def. §20.1]]; its first example is $1/x$ at its four ends, [[§20 Limits of Functions#^ex-20-3|451 Ex. §20.3]] ($\infty$ from the right of $0$, $-\infty$ from the left). For sequences: [[§9 Limit Theorems for Sequences#^def-9-1|451 Def. §9.1]].

> [!definition] Definition §7.5: Vertical Asymptote
> The vertical line $x = a$ is called a **vertical asymptote** of the curve $y = f(x)$ if at least one of the following statements is true:
>
> $$
> \lim_{x \to a} f(x) = \infty, \quad \lim_{x \to a^-} f(x) = \infty, \quad \lim_{x \to a^+} f(x) = \infty, \quad
> \lim_{x \to a} f(x) = -\infty, \quad \lim_{x \to a^-} f(x) = -\infty, \quad \lim_{x \to a^+} f(x) = -\infty .
> $$
>
> For instance, the $y$-axis is a vertical asymptote of $y = 1/x^2$, because $\lim_{x \to 0} (1/x^2) = \infty$.
>
> *Stewart: 2.2, Definition 6*

^def-7-5

> [!example] Example §7.5: Finding Vertical Asymptotes
> **(a)** Does the curve $y = \dfrac{2x}{x - 3}$ have a vertical asymptote?
>
> The candidate is $x = 3$, where the denominator is $0$; examine the one-sided limits there. If $x$ is close to $3$ but larger, then $x - 3$ is a small positive number and $2x$ is close to $6$, so $2x/(x - 3)$ is a large *positive* number (at $x = 3.01$ it is $6.02/0.01 = 602$). If $x$ is close to $3$ but smaller, $x - 3$ is a small negative number while $2x$ is still close to $6$, so the quotient is a large *negative* number. Thus
>
> $$
> \lim_{x \to 3^+} \frac{2x}{x - 3} = \infty, \qquad \lim_{x \to 3^-} \frac{2x}{x - 3} = -\infty ,
> $$
>
> and by [[§7 The Limit of a Function#^def-7-5|Definition §7.5]] the line $x = 3$ is a vertical asymptote.
>
> Compare [[§7 The Limit of a Function#^ex-7-4|Example §7.4]]. There $1/x^2 \to \infty$ from both sides, and we write $\lim_{x \to 0} (1/x^2) = \infty$. Here the two sides go to $\infty$ and $-\infty$, so we can only say that $\lim_{x \to 3} \frac{2x}{x - 3}$ does not exist.
>
> **(b)** Find the vertical asymptotes of $f(x) = \tan x$.
>
> Since $\tan x = \dfrac{\sin x}{\cos x}$, the candidates are the zeros of $\cos x$. As $x \to (\pi/2)^-$, $\cos x \to 0$ through positive values, and as $x \to (\pi/2)^+$, through negative values, while $\sin x$ is positive (near $1$) for $x$ near $\pi/2$. Hence
>
> $$
> \lim_{x \to (\pi/2)^-} \tan x = \infty, \qquad \lim_{x \to (\pi/2)^+} \tan x = -\infty ,
> $$
>
> and $x = \pi/2$ is a vertical asymptote. The same reasoning applies at every zero of cosine: the lines $x = \pi/2 + n\pi$, $n$ an integer, are all vertical asymptotes of $y = \tan x$.
>
> *Stewart: Examples 2.2.7 and 2.2.8*

^ex-7-5

> [!theorem] Theorem §7.1: The Logarithm Near 0
> $$
> \lim_{x \to 0^+} \ln x = -\infty ,
> $$
>
> so the $y$-axis $x = 0$ is a vertical asymptote of $y = \ln x$. The same holds for $y = \log_b x$ whenever $b > 1$.
>
> *Stewart: 2.2 (text)*

^thm-7-1

> [!proof]+ Proof
> *Stewart reads this off the graph of $\ln x$ and leaves the $\varepsilon$–$\delta$ proof as Exercise 2.4.43; here it is, using the one-sided form of [[§9 The Precise Definition of a Limit#^def-9-4|Definition §9.4]].*
>
> Let $N$ be any negative number and put $\delta = e^N > 0$. Since $\ln$ is increasing ([[§5 Inverse Functions and Logarithms#^thm-5-4|Theorem §5.4]], part 4, with $b = e > 1$), $0 < x < \delta$ implies $\ln x < \ln e^N = N$ ([[§5 Inverse Functions and Logarithms#^cor-5-6|Corollary §5.6]]). So $\ln x$ is below any given $N$ once $x > 0$ is close enough to $0$, which is $\lim_{x \to 0^+} \ln x = -\infty$.
>
> For $b > 1$, $\log_b x = \dfrac{\ln x}{\ln b}$ ([[§5 Inverse Functions and Logarithms#^thm-5-8|Theorem §5.8]]) with $\ln b > \ln 1 = 0$. Given $N < 0$, the first part (applied to $N \ln b < 0$) gives $\delta > 0$ such that $\ln x < N \ln b$, that is, $\log_b x < N$, for $0 < x < \delta$.

^pf-7-1

*Uses:* [[§9 The Precise Definition of a Limit#^def-9-4|Def. §9.4]], [[§5 Inverse Functions and Logarithms#^thm-5-4|§5.4]], [[§5 Inverse Functions and Logarithms#^cor-5-6|§5.6]], [[§5 Inverse Functions and Logarithms#^thm-5-8|§5.8]]
