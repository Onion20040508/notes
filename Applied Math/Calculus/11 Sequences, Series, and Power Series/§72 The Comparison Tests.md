---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 72
stewart: "11.4"
aliases: ["Stewart 11.4"]
tags: [calculus]
---
← [[§71 The Integral Test and Estimates of Sums]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§73 Alternating Series and Absolute Convergence]] →

*Stewart, Section 11.4.*

A series with positive terms converges exactly when its partial sums are bounded, so it can be judged by comparing it with a series whose behavior is known, usually a $p$-series ([[§71 The Integral Test and Estimates of Sums#^thm-71-2|Theorem §71.2]]) or a geometric series ([[§70 Series#^thm-70-1|Theorem §70.1]]). The Direct Comparison Test compares the terms one by one: smaller than a convergent series means convergent, larger than a divergent series means divergent. When the inequality goes the wrong way, the Limit Comparison Test compares the *ratio* of the terms instead, which formalizes the habit of keeping only the dominant powers. A comparison also bounds the remainder, and so gives error estimates.

## The Direct Comparison Test

> [!remark] Remark: The Idea
> Compare $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n + 1}$ with the geometric series $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n}$ ($a = r = \frac12$), whose sum is $1$. Since $\dfrac{1}{2^n + 1} < \dfrac{1}{2^n}$, every partial sum of the first series is smaller than the corresponding partial sum of the second, hence smaller than $1$. The partial sums of the first series therefore form a bounded increasing sequence, which converges, and $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n + 1} < 1$.

^rem-72-1

> [!theorem] Theorem §72.1: The Direct Comparison Test
> Suppose that $\sum a_n$ and $\sum b_n$ are series with positive terms.
>
> (i) If $\sum b_n$ is convergent and $a_n \le b_n$ for all $n$, then $\sum a_n$ is also convergent.
>
> (ii) If $\sum b_n$ is divergent and $a_n \ge b_n$ for all $n$, then $\sum a_n$ is also divergent.
>
> *Stewart: 11.4, The Direct Comparison Test*

^thm-72-1

> [!proof]+ Proof
> Let
>
> $$
> s_n = \sum_{i=1}^{n} a_i , \qquad t_n = \sum_{i=1}^{n} b_i , \qquad t = \sum_{n=1}^{\infty} b_n .
> $$
>
> Since both series have positive terms, $\{s_n\}$ and $\{t_n\}$ are increasing: $s_{n+1} = s_n + a_{n+1} \ge s_n$.
>
> **(i)** $t_n \to t$ and $\{t_n\}$ is increasing, so $t_n \le t$ for all $n$. Since $a_i \le b_i$, we have $s_n \le t_n \le t$ for all $n$. So $\{s_n\}$ is increasing and bounded above, and it converges by the Monotonic Sequence Theorem. Thus $\sum a_n$ converges.
>
> **(ii)** If $\sum b_n$ is divergent, then $t_n \to \infty$, since $\{t_n\}$ is increasing. (An increasing sequence that is bounded above converges, so $\{t_n\}$ is not bounded above: for every $M$ some $t_N > M$, and then $t_n \ge t_N > M$ for all $n \ge N$.) But $a_i \ge b_i$, so $s_n \ge t_n$. Thus $s_n \to \infty$, and $\sum a_n$ diverges.

^pf-72-1

*Uses:* [[§69 Sequences#^thm-69-9|§69.9]], [[§70 Series#^def-70-2|Def. §70.2]], [[§70 Series#^def-70-new1|Def. §70.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^thm-14-7|451 Thm. §14.7]] (Comparison Test, for $|a_n| \le b_n$, proved with the Cauchy criterion so that the $a_n$ need not be positive).

The test needs a known series $\sum b_n$ to compare with. Most of the time it is a $p$-series ($\sum 1/n^p$ converges if $p > 1$ and diverges if $p \le 1$, [[§71 The Integral Test and Estimates of Sums#^thm-71-2|Theorem §71.2]]) or a geometric series ($\sum a r^{n-1}$ converges if $|r| < 1$ and diverges if $|r| \ge 1$, [[§70 Series#^thm-70-1|Theorem §70.1]]).

> [!example] Example §72.1: Comparing with a p-Series
> Determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{5}{2n^2 + 4n + 3}$ converges or diverges.
>
> For large $n$ the dominant term in the denominator is $2n^2$, so compare with $\sum 5/(2n^2)$:
>
> $$
> \frac{5}{2n^2 + 4n + 3} < \frac{5}{2n^2}
> $$
>
> because the left side has the bigger denominator. (In the notation of the test, $a_n$ is the left side and $b_n$ the right side.) Now
>
> $$
> \sum_{n=1}^{\infty} \frac{5}{2n^2} = \frac52 \sum_{n=1}^{\infty} \frac{1}{n^2}
> $$
>
> is convergent, a constant times a $p$-series with $p = 2 > 1$ ([[§70 Series#^thm-70-6|Theorem §70.6]]). By part (i) of the Direct Comparison Test, the given series converges.
>
> *Stewart: Example 11.4.1*

^ex-72-1

> [!remark] Remark: Only the Tail Matters
> The condition $a_n \le b_n$ or $a_n \ge b_n$ needs to hold only for $n \ge N$, for some fixed integer $N$: the test then applies to the tails $\sum_{n \ge N} a_n$ and $\sum_{n \ge N} b_n$, and finitely many terms do not affect convergence ([[§70 Series#^prop-70-7|Proposition §70.7]]).

^rem-72-2

> [!example] Example §72.2: Comparing with the Harmonic Series
> Test $\displaystyle\sum_{k=1}^{\infty} \frac{\ln k}{k}$ for convergence or divergence.
>
> [[§71 The Integral Test and Estimates of Sums#^ex-71-3|Example §71.3]] settled this with the Integral Test; a comparison is quicker. Since $\ln k > 1$ for $k \ge 3$ (as $3 > e$),
>
> $$
> \frac{\ln k}{k} > \frac1k \qquad k \ge 3 .
> $$
>
> $\sum 1/k$ is divergent (the $p$-series with $p = 1$), so the given series diverges by part (ii) of the Direct Comparison Test, applied for $k \ge 3$.
>
> *Stewart: Example 11.4.2*

^ex-72-2

## Limit Comparison Test

The Direct Comparison Test is conclusive only if the terms are smaller than those of a convergent series or larger than those of a divergent series. For $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n - 1}$ the obvious inequality $\dfrac{1}{2^n - 1} > \dfrac{1}{2^n}$ goes the wrong way, since $\sum (\frac12)^n$ is convergent. Still, the series ought to converge, because it is so similar to $\sum (\frac12)^n$.

> [!theorem] Theorem §72.2: The Limit Comparison Test
> Suppose that $\sum a_n$ and $\sum b_n$ are series with positive terms. If
>
> $$
> \lim_{n \to \infty} \frac{a_n}{b_n} = c ,
> $$
>
> where $c$ is a finite number and $c > 0$, then either both series converge or both diverge.
>
> *Stewart: 11.4, The Limit Comparison Test*

^thm-72-2

> [!proof]+ Proof
> Let $m$ and $M$ be positive numbers such that $m < c < M$. Because $a_n / b_n$ is close to $c$ for large $n$, there is an integer $N$ such that
>
> $$
> m < \frac{a_n}{b_n} < M \qquad \text{when } n > N .
> $$
>
> (Take $\varepsilon = \min\{c - m, M - c\} > 0$ in [[§69 Sequences#^def-69-3|Definition §69.3]].) Since $b_n > 0$,
>
> $$
> m b_n < a_n < M b_n \qquad \text{when } n > N .
> $$
>
> If $\sum b_n$ converges, so does $\sum M b_n$ ([[§70 Series#^thm-70-6|Theorem §70.6]]). Thus $\sum a_n$ converges by part (i) of the Direct Comparison Test (for $n > N$; Remark above). If $\sum b_n$ diverges, so does $\sum m b_n$ (otherwise $\sum b_n = \frac1m \sum m b_n$ would converge), and part (ii) of the Direct Comparison Test shows that $\sum a_n$ diverges.

^pf-72-2

*Uses:* [[§72 The Comparison Tests#^thm-72-1|§72.1]], [[§69 Sequences#^def-69-3|Def. §69.3]], [[§70 Series#^thm-70-6|§70.6]], [[§70 Series#^prop-70-7|§70.7]]

> [!remark]- Remark: The Cases c = 0 and c = ∞
> Stewart's Exercises 48 and 49 treat the boundary cases. If $a_n / b_n \to 0$ and $\sum b_n$ converges, then $\sum a_n$ converges (eventually $a_n < b_n$). If $a_n / b_n \to \infty$ and $\sum b_n$ diverges, then $\sum a_n$ diverges (eventually $a_n > b_n$). The other two combinations give no information.

^rem-72-3

> [!example] Example §72.3: The Wrong-Way Inequality Repaired
> Test $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n - 1}$ for convergence or divergence.
>
> Use the Limit Comparison Test with $a_n = \dfrac{1}{2^n - 1}$ and $b_n = \dfrac{1}{2^n}$:
>
> $$
> \lim_{n \to \infty} \frac{a_n}{b_n} = \lim_{n \to \infty} \frac{1/(2^n - 1)}{1/2^n} = \lim_{n \to \infty} \frac{2^n}{2^n - 1} = \lim_{n \to \infty} \frac{1}{1 - 1/2^n} = 1 > 0 .
> $$
>
> The limit exists and $\sum 1/2^n$ is a convergent geometric series, so the given series converges.
>
> *Stewart: Example 11.4.3*

^ex-72-3

> [!example] Example §72.4: Keeping the Dominant Powers
> Determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{2n^2 + 3n}{\sqrt{5 + n^5}}$ converges or diverges.
>
> The dominant part of the numerator is $2n^2$ and of the denominator $\sqrt{n^5} = n^{5/2}$. So take
>
> $$
> a_n = \frac{2n^2 + 3n}{\sqrt{5 + n^5}} , \qquad b_n = \frac{2n^2}{n^{5/2}} = \frac{2}{n^{1/2}} .
> $$
>
> Then
>
> $$
> \lim_{n \to \infty} \frac{a_n}{b_n} = \lim_{n \to \infty} \frac{2n^2 + 3n}{\sqrt{5 + n^5}} \cdot \frac{n^{1/2}}{2} = \lim_{n \to \infty} \frac{2n^{5/2} + 3n^{3/2}}{2\sqrt{5 + n^5}} = \lim_{n \to \infty} \frac{2 + \dfrac3n}{2\sqrt{\dfrac{5}{n^5} + 1}} = \frac{2 + 0}{2\sqrt{0 + 1}} = 1 ,
> $$
>
> dividing numerator and denominator by $n^{5/2}$. Since $\sum b_n = 2 \sum 1/n^{1/2}$ is divergent ($p$-series with $p = \frac12 < 1$), the given series diverges by the Limit Comparison Test.
>
> *Stewart: Example 11.4.4*

^ex-72-4

> [!remark] Remark: Method — Choosing a Comparison Series
> 1. For a series with positive terms built from powers of $n$ (rational functions, roots), keep only the highest power of $n$ in the numerator and in the denominator. The result is a constant times a $p$-series; take it as $b_n$.
> 2. If the terms involve $r^n$, keep the dominant exponential and compare with a geometric series.
> 3. Try the Direct Comparison Test if the inequality between $a_n$ and $b_n$ goes the useful way (smaller than a convergent series, larger than a divergent one); this is often the case when the discarded terms are added in the denominator ([[§72 The Comparison Tests#^ex-72-1|Example §72.1]]).
> 4. Otherwise compute $\lim a_n / b_n$; if it is a positive number, the Limit Comparison Test decides ([[§72 The Comparison Tests#^ex-72-4|Example §72.4]]).
> 5. Factors such as $\ln n$ or $\sin^2 n$ are handled by an inequality: $\ln n > 1$ for $n \ge 3$, $0 \le \sin^2 n \le 1$, and $\ln n < n^{\varepsilon}$ for large $n$, for any $\varepsilon > 0$.

^rem-72-4

## Estimating Sums

> [!theorem] Proposition §72.3: Comparing Remainders
> Suppose $0 < a_n \le b_n$ for all $n$ and $\sum b_n$ converges. Let $R_n = s - s_n = a_{n+1} + a_{n+2} + \cdots$ be the remainder of $\sum a_n$ ([[§71 The Integral Test and Estimates of Sums#^def-71-1|Definition §71.1]]) and $T_n = t - t_n = b_{n+1} + b_{n+2} + \cdots$ that of $\sum b_n$. Then
>
> $$
> R_n \le T_n .
> $$
>
> If $\sum b_n$ is a $p$-series, $T_n$ can be estimated as in [[§71 The Integral Test and Estimates of Sums#^thm-71-3|Theorem §71.3]]; if it is geometric, $T_n$ is the sum of a geometric series and can be computed exactly.
>
> *Stewart: 11.4 (text)*

^prop-72-3

> [!proof]+ Proof
> Both series converge (the first by the Direct Comparison Test). For each $m$, $a_{n+1} + \cdots + a_{n+m} \le b_{n+1} + \cdots + b_{n+m}$, that is, $s_{n+m} - s_n \le t_{n+m} - t_n$. Letting $m \to \infty$ gives $s - s_n \le t - t_n$.

^pf-72-3

*Uses:* [[§72 The Comparison Tests#^thm-72-1|§72.1]], [[§71 The Integral Test and Estimates of Sums#^def-71-1|Def. §71.1]]

> [!example] Example §72.5: An Error Estimate by Comparison
> Use the sum of the first $100$ terms to approximate the sum of $\sum 1/(n^3 + 1)$. Estimate the error involved.
>
> Since $\dfrac{1}{n^3 + 1} < \dfrac{1}{n^3}$, the series converges by the Direct Comparison Test. For the comparison series $\sum 1/n^3$, [[§71 The Integral Test and Estimates of Sums#^ex-71-4|Example §71.4]] found with the Remainder Estimate for the Integral Test that
>
> $$
> T_n \le \int_n^{\infty} \frac{1}{x^3}\,dx = \frac{1}{2n^2} .
> $$
>
> By [[§72 The Comparison Tests#^prop-72-3|Proposition §72.3]], $R_n \le T_n \le \dfrac{1}{2n^2}$. With $n = 100$,
>
> $$
> R_{100} \le \frac{1}{2(100)^2} = 0.00005 .
> $$
>
> A computer gives $\displaystyle\sum_{n=1}^{100} \frac{1}{n^3 + 1} \approx 0.6864538$, so
>
> $$
> \sum_{n=1}^{\infty} \frac{1}{n^3 + 1} \approx 0.6864538 \qquad \text{with error less than } 0.00005 .
> $$
>
> *Stewart: Example 11.4.5*

^ex-72-5
