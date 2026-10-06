---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 83
stewart: "11.3"
aliases: ["Stewart 11.3"]
tags: [calculus]
---
← [[§82 Series]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§84 The Comparison Tests]] →

*Stewart, Section 11.3.*

Usually there is no formula for the partial sums of a series, so we need tests that decide convergence without finding the sum. The first test compares a series of positive, decreasing terms $a_n = f(n)$ with the improper integral $\int_1^{\infty} f(x)\,dx$: rectangles of width $1$ and height $a_n$ fit under or over the graph of $f$, so the series and the integral converge or diverge together. Applied to $f(x) = 1/x^p$, it settles the $p$-series, the standard against which most other series are compared ([[§84 The Comparison Tests|§84]]). The same rectangles also bound the error made by stopping at a partial sum.

## The Integral Test

> [!remark] Remark: Two Pictures
> **$\sum 1/n^2$ converges.** Put rectangles of width $1$ under the curve $y = 1/x^2$, with height equal to the value at the *right* endpoint of each interval $[n-1, n]$. Their areas are $\frac{1}{1^2}, \frac{1}{2^2}, \frac{1}{3^2}, \ldots$. Apart from the first, they lie under the curve for $x \ge 1$, whose area is $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ ([[§58 Improper Integrals#^thm-58-1|Theorem §58.1]]). So every partial sum is less than $\frac{1}{1^2} + 1 = 2$. The partial sums are increasing (all terms are positive) and bounded, so they converge by the Monotonic Sequence Theorem ([[§81 Monotonic and Bounded Sequences#^thm-81-1|Theorem §81.1]]), and $\sum_{n=1}^{\infty} 1/n^2 < 2$. (Numerically $s_{5000} \approx 1.6447$; Euler found the exact sum $\pi^2/6 \approx 1.6449$.)
>
> **$\sum 1/\sqrt{n}$ diverges.** Now take the height at the *left* endpoint of each interval $[n, n+1]$, so the rectangles stick out above the curve $y = 1/\sqrt{x}$. Their total area $\frac{1}{\sqrt1} + \frac{1}{\sqrt2} + \cdots$ exceeds the area under the curve for $x \ge 1$, which is $\int_1^{\infty} \frac{1}{\sqrt x}\,dx = \infty$ ([[§58 Improper Integrals#^thm-58-1|Theorem §58.1]], Stewart's Example 7.8.4). So the series diverges. (Numerically $s_{5000} \approx 139.97$.)

^rem-83-1

The same reasoning proves the general test.

> [!theorem] Theorem §96.1: The Integral Test
> Suppose $f$ is a continuous, positive, decreasing function on $[1, \infty)$ and let $a_n = f(n)$. Then the series $\sum_{n=1}^{\infty} a_n$ is convergent if and only if the improper integral $\int_1^{\infty} f(x)\,dx$ is convergent. In other words:
>
> (i) If $\displaystyle\int_1^{\infty} f(x)\,dx$ is convergent, then $\displaystyle\sum_{n=1}^{\infty} a_n$ is convergent.
>
> (ii) If $\displaystyle\int_1^{\infty} f(x)\,dx$ is divergent, then $\displaystyle\sum_{n=1}^{\infty} a_n$ is divergent.
>
> *Stewart: 11.3, The Integral Test*

^thm-83-1

> [!proof]+ Proof
> **Two inequalities.** Let $i \ge 2$. On $[i-1, i]$ we have $f(x) \ge f(i) = a_i$, because $f$ is decreasing, so the rectangle of height $a_i$ on $[i-1, i]$ lies under the graph: $a_i \le \int_{i-1}^{i} f(x)\,dx$. Adding these for $i = 2, \ldots, n$,
>
> $$
> a_2 + a_3 + \cdots + a_n \le \int_1^n f(x)\,dx . \qquad (4)
> $$
>
> Likewise, for $i \ge 1$, $f(x) \le f(i) = a_i$ on $[i, i+1]$, so $\int_i^{i+1} f(x)\,dx \le a_i$, and adding for $i = 1, \ldots, n - 1$,
>
> $$
> \int_1^n f(x)\,dx \le a_1 + a_2 + \cdots + a_{n-1} . \qquad (5)
> $$
>
> (Stewart reads (4) and (5) off Figures 5 and 6; both depend on $f$ being decreasing.)
>
> **(i)** If $\int_1^{\infty} f(x)\,dx$ is convergent, then (4) gives
>
> $$
> \sum_{i=2}^{n} a_i \le \int_1^n f(x)\,dx \le \int_1^{\infty} f(x)\,dx
> $$
>
> since $f(x) \ge 0$. Therefore
>
> $$
> s_n = a_1 + \sum_{i=2}^{n} a_i \le a_1 + \int_1^{\infty} f(x)\,dx = M, \text{ say.}
> $$
>
> So $\{s_n\}$ is bounded above. Also $s_{n+1} = s_n + a_{n+1} \ge s_n$, since $a_{n+1} = f(n+1) \ge 0$. Thus $\{s_n\}$ is an increasing bounded sequence, so it converges by the Monotonic Sequence Theorem, and $\sum a_n$ is convergent.
>
> **(ii)** If $\int_1^{\infty} f(x)\,dx$ is divergent, then $\int_1^n f(x)\,dx \to \infty$ as $n \to \infty$, because $f(x) \ge 0$. (The function $t \mapsto \int_1^t f(x)\,dx$ is increasing, so it either has a finite limit or tends to $\infty$.) But (5) gives
>
> $$
> \int_1^n f(x)\,dx \le \sum_{i=1}^{n-1} a_i = s_{n-1} ,
> $$
>
> and so $s_{n-1} \to \infty$. This implies that $s_n \to \infty$, and $\sum a_n$ diverges.

^pf-83-1

*Uses:* [[§81 Monotonic and Bounded Sequences#^thm-81-1|§81.1]], [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§58 Improper Integrals#^def-58-1|Def. §58.1]], [[§40 Properties of the Definite Integral#^thm-40-3|§40.3]] (comparison properties), [[§40 Properties of the Definite Integral#^thm-40-2|§40.2]] (adjacent intervals)

![[m233-71-1.svg]]
*The two inequalities in the proof of the Integral Test, for $n = 6$. Left, inequality (4): rectangles of height $a_i = f(i)$ on $[i-1, i]$ (right endpoints) fit under the decreasing curve. Right, inequality (5): rectangles of height $a_i$ on $[i, i+1]$ (left endpoints) cover the area under the curve from $1$ to $n$.*

> [!remark]- Connections
> - Rigorous treatment: [[§15 Alternating Series and Integral Tests#^thm-15-3|451 Thm. §15.3]] (for a decreasing $f \ge 0$; continuity is not needed there, since monotone functions are integrable).

> [!remark] Remark: Where the Series Starts; Ultimately Decreasing
> The series and the integral need not start at $n = 1$: to test $\sum_{n=4}^{\infty} \frac{1}{(n-3)^2}$, use $\int_4^{\infty} \frac{1}{(x-3)^2}\,dx$. Nor must $f$ be decreasing everywhere; it suffices that $f$ is *ultimately* decreasing, that is, decreasing for $x$ larger than some number $N$. Then the test applies to $\sum_{n=N}^{\infty} a_n$, and by [[§82 Series#^prop-82-7|Proposition §82.7]] $\sum_{n=1}^{\infty} a_n$ converges or diverges with it.

^rem-83-2

> [!example] Example §96.1: An Arctangent Integral
> Test $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2 + 1}$ for convergence or divergence.
>
> $f(x) = 1/(x^2 + 1)$ is continuous, positive and decreasing on $[1, \infty)$, so we use the Integral Test:
>
> $$
> \int_1^{\infty} \frac{1}{x^2 + 1}\,dx = \lim_{t \to \infty} \int_1^t \frac{1}{x^2 + 1}\,dx = \lim_{t \to \infty} \Big[ \tan^{-1} x \Big]_1^t = \lim_{t \to \infty} \left( \tan^{-1} t - \frac{\pi}{4} \right) = \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4} .
> $$
>
> The integral converges, so $\sum 1/(n^2 + 1)$ converges. To use the test we must be able to evaluate $\int_1^{\infty} f(x)\,dx$, which is often difficult or impossible; the next sections develop tests that avoid this.
>
> *Stewart: Example 11.3.1*

^ex-83-1

> [!theorem] Theorem §96.2: The p-Series
> The **$p$-series** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^p}$ is convergent if $p > 1$ and divergent if $p \le 1$.
>
> *Stewart: 11.3, Equation 1 (from Example 11.3.2)*

^thm-83-2

> [!proof]+ Proof
> **$p \le 0$.** If $p < 0$, then $\lim_{n \to \infty} (1/n^p) = \lim_{n \to \infty} n^{-p} = \infty$. If $p = 0$, then $1/n^p = 1 \to 1$. Either way $\lim_{n \to \infty} (1/n^p) \ne 0$, so the series diverges by the Test for Divergence ([[§82 Series#^cor-82-5|Corollary §82.5]]).
>
> **$p > 0$.** The function $f(x) = 1/x^p$ is continuous, positive and decreasing on $[1, \infty)$. By [[§58 Improper Integrals#^thm-58-1|Theorem §58.1]] (Stewart's Equation 7.8.2),
>
> $$
> \int_1^{\infty} \frac{1}{x^p}\,dx \quad \text{converges if } p > 1 \text{ and diverges if } p \le 1 .
> $$
>
> By the Integral Test, $\sum 1/n^p$ converges if $p > 1$ and diverges if $0 < p \le 1$. (For $p = 1$ this is the harmonic series, [[§82 Series#^thm-82-3|Theorem §82.3]].)

^pf-83-2

*Uses:* [[§83 The Integral Test and Estimates of Sums#^thm-83-1|§83.1]], [[§82 Series#^cor-82-5|§82.5]], [[§58 Improper Integrals#^thm-58-1|§58.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§15 Alternating Series and Integral Tests#^ex-15-3|451 Ex. §15.3]] (by the integral test, as here) and [[§14 Series#^ex-14-3|451 Ex. §14.3]]; the integrals themselves, [[§36 Improper Integrals#^ex-36-2|451 Ex. §36.2]].

> [!example] Example §96.2: Reading Off p
> **(a)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^3} = \frac{1}{1^3} + \frac{1}{2^3} + \frac{1}{3^3} + \cdots$ is convergent: it is a $p$-series with $p = 3 > 1$.
>
> **(b)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^{1/3}} = \sum_{n=1}^{\infty} \frac{1}{\sqrt[3]{n}} = 1 + \frac{1}{\sqrt[3]{2}} + \frac{1}{\sqrt[3]{3}} + \cdots$ is divergent: it is a $p$-series with $p = \frac13 < 1$.
>
> For $p > 0$ the terms $1/n^p$ always tend to $0$; whether the series converges depends on how *rapidly* they do, and they go to $0$ faster for larger $p$.
>
> *Stewart: Example 11.3.3*

^ex-83-2

> [!remark] Remark: The Sum Is Not the Integral
> The Integral Test says only that the series and the integral converge together; their values differ. For example,
>
> $$
> \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6} \qquad\text{whereas}\qquad \int_1^{\infty} \frac{1}{x^2}\,dx = 1 .
> $$
>
> So in general $\displaystyle\sum_{n=1}^{\infty} a_n \ne \int_1^{\infty} f(x)\,dx$. (Proving $\sum 1/n^2 = \pi^2/6$ is quite difficult.)

^rem-83-3

> [!example] Example §97.1: An Ultimately Decreasing Function
> Determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{\ln n}{n}$ converges or diverges.
>
> $f(x) = (\ln x)/x$ is positive and continuous for $x > 1$, since the logarithm is continuous. Whether $f$ is decreasing is not obvious, so compute its derivative:
>
> $$
> f'(x) = \frac{(1/x)x - \ln x}{x^2} = \frac{1 - \ln x}{x^2} .
> $$
>
> So $f'(x) < 0$ when $\ln x > 1$, that is, when $x > e$: $f$ is ultimately decreasing, and the Integral Test applies ([[§83 The Integral Test and Estimates of Sums#^rem-83-2|Remark: Where the Series Starts]]). With the substitution $u = \ln x$,
>
> $$
> \int_1^{\infty} \frac{\ln x}{x}\,dx = \lim_{t \to \infty} \int_1^t \frac{\ln x}{x}\,dx = \lim_{t \to \infty} \left[ \frac{(\ln x)^2}{2} \right]_1^t = \lim_{t \to \infty} \frac{(\ln t)^2}{2} = \infty .
> $$
>
> The integral diverges, so $\sum (\ln n)/n$ diverges.
>
> *Stewart: Example 11.3.4*

^ex-83-3

## Estimating the Sum of a Series

> [!definition] Definition §96.1: Remainder
> If $\sum a_n$ converges with sum $s$, the **remainder** after $n$ terms is
>
> $$
> R_n = s - s_n = a_{n+1} + a_{n+2} + a_{n+3} + \cdots ,
> $$
>
> the error made when the partial sum $s_n$ is used as an approximation to $s$.
>
> *Stewart: 11.3 (text)*

^def-83-1

> [!theorem] Theorem §96.3: Remainder Estimate for the Integral Test
> Suppose $f(k) = a_k$, where $f$ is a continuous, positive, decreasing function for $x \ge n$, and $\sum a_n$ is convergent. If $R_n = s - s_n$, then
>
> $$
> \int_{n+1}^{\infty} f(x)\,dx \le R_n \le \int_n^{\infty} f(x)\,dx .
> $$
>
> *Stewart: 11.3, Remainder Estimate 2*

^thm-83-3

> [!proof]+ Proof
> *Stewart reads this off Figures 3 and 4 (rectangles of heights $a_{n+1}, a_{n+2}, \ldots$ under and over the curve for $x \ge n$); written out:* both integrals converge, by the Integral Test applied to the convergent series $\sum_{k \ge n} a_k$. As in the proof of [[§83 The Integral Test and Estimates of Sums#^thm-83-1|Theorem §83.1]], since $f$ is decreasing on $[n, \infty)$, for every $k \ge 1$
>
> $$
> \int_{n+k}^{n+k+1} f(x)\,dx \le a_{n+k} \le \int_{n+k-1}^{n+k} f(x)\,dx .
> $$
>
> Adding for $k = 1, \ldots, m$,
>
> $$
> \int_{n+1}^{n+m+1} f(x)\,dx \le a_{n+1} + \cdots + a_{n+m} \le \int_n^{n+m} f(x)\,dx .
> $$
>
> The middle term is $s_{n+m} - s_n$. Letting $m \to \infty$, it tends to $s - s_n = R_n$, the left side to $\int_{n+1}^{\infty} f(x)\,dx$ and the right side to $\int_n^{\infty} f(x)\,dx$. Limits preserve weak inequalities, which gives the estimate.

^pf-83-3

*Uses:* [[§83 The Integral Test and Estimates of Sums#^thm-83-1|§83.1]], [[§83 The Integral Test and Estimates of Sums#^def-83-1|Def. §83.1]], [[§58 Improper Integrals#^def-58-1|Def. §58.1]], limits preserve weak inequalities ([[§9 Limit Theorems for Sequences#^prop-9-5|451 Prop. §9.5]])

> [!example] Example §97.2: How Many Terms?
> **(a)** Approximate the sum of $\sum 1/n^3$ by the sum of the first $10$ terms, and estimate the error.
> **(b)** How many terms are required to ensure that the sum is accurate to within $0.0005$?
>
> Both parts need $\int_n^{\infty} f(x)\,dx$ for $f(x) = 1/x^3$, which satisfies the conditions of the Integral Test:
>
> $$
> \int_n^{\infty} \frac{1}{x^3}\,dx = \lim_{t \to \infty} \left[ -\frac{1}{2x^2} \right]_n^t = \lim_{t \to \infty} \left( -\frac{1}{2t^2} + \frac{1}{2n^2} \right) = \frac{1}{2n^2} .
> $$
>
> **(a)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^3} \approx s_{10} = \frac{1}{1^3} + \frac{1}{2^3} + \cdots + \frac{1}{10^3} \approx 1.1975$. By [[§83 The Integral Test and Estimates of Sums#^thm-83-3|Theorem §83.3]],
>
> $$
> R_{10} \le \int_{10}^{\infty} \frac{1}{x^3}\,dx = \frac{1}{2(10)^2} = \frac{1}{200} ,
> $$
>
> so the error is at most $0.005$.
>
> **(b)** We need $n$ with $R_n \le 0.0005$. Since $R_n \le \dfrac{1}{2n^2}$, it suffices that $\dfrac{1}{2n^2} < 0.0005$, that is, $n^2 > \dfrac{1}{0.001} = 1000$, or $n > \sqrt{1000} \approx 31.6$. We need $32$ terms.
>
> *Stewart: Example 11.3.5*

^ex-83-4

> [!theorem] Corollary §96.4: Bounds for the Sum
> Under the hypotheses of [[§83 The Integral Test and Estimates of Sums#^thm-83-3|Theorem §83.3]],
>
> $$
> s_n + \int_{n+1}^{\infty} f(x)\,dx \le s \le s_n + \int_n^{\infty} f(x)\,dx .
> $$
>
> *Stewart: 11.3, Inequalities 3*

^cor-83-4

> [!proof]+ Proof
> Add $s_n$ to each side of the inequalities in [[§83 The Integral Test and Estimates of Sums#^thm-83-3|Theorem §83.3]] and use $s_n + R_n = s$.

^pf-83-4

*Uses:* [[§83 The Integral Test and Estimates of Sums#^thm-83-3|§83.3]]

These bounds give a more accurate approximation to $s$ than the partial sum $s_n$ alone.

> [!example] Example §97.3: Estimating the Sum of the p-Series with p = 3
> Use [[§83 The Integral Test and Estimates of Sums#^cor-83-4|Corollary §83.4]] with $n = 10$ to estimate $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^3}$.
>
> By [[§83 The Integral Test and Estimates of Sums#^ex-83-4|Example §83.4]], $\int_n^{\infty} x^{-3}\,dx = \frac{1}{2n^2}$, so the inequalities become
>
> $$
> s_{10} + \frac{1}{2(11)^2} \le s \le s_{10} + \frac{1}{2(10)^2} .
> $$
>
> With $s_{10} \approx 1.197532$, $\frac{1}{242} \approx 0.004132$ and $\frac{1}{200} = 0.005$,
>
> $$
> 1.201664 \le s \le 1.202532 .
> $$
>
> Approximating $s$ by the midpoint of this interval, the error is at most half its length, $\frac12 (0.000868) = 0.000434$:
>
> $$
> \sum_{n=1}^{\infty} \frac{1}{n^3} \approx 1.2021 \qquad \text{with error} < 0.0005 .
> $$
>
> [[§83 The Integral Test and Estimates of Sums#^ex-83-4|Example §83.4]] needed $32$ terms for this accuracy; here $10$ suffice. (The true value is $1.2020569\ldots$; unlike $\sum 1/n^2$, no closed form is known.)
>
> *Stewart: Example 11.3.6*

^ex-83-5
