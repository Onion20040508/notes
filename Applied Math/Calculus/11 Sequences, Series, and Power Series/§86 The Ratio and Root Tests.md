---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 86
stewart: "11.6"
aliases: ["Stewart 11.6"]
tags: [calculus]
---
← [[§85 Alternating Series and Absolute Convergence]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§87 Strategy for Testing Series]] →

*Stewart, Section 11.6.*

For a geometric series $\sum a r^{n-1}$ the ratio of consecutive terms is constantly $r$, and the series converges when $|r| < 1$. The Ratio Test says that the same holds in the limit: if $|a_{n+1}/a_n|$ approaches a number less than $1$, the series converges absolutely, and if it approaches a number greater than $1$, it diverges. The Root Test does the same with $\sqrt[n]{|a_n|}$. Both are proved by comparison with a geometric series, both say nothing when the limit is $1$, and between them they handle the series built from exponentials, factorials and $n$th powers, which is exactly what power series ([[§88 Power Series|§88]]) require.

## The Ratio Test

> [!theorem] Theorem §86.1: The Ratio Test
> (i) If $\displaystyle\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L < 1$, then the series $\displaystyle\sum_{n=1}^{\infty} a_n$ is absolutely convergent (and therefore convergent).
>
> (ii) If $\displaystyle\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L > 1$ or $\displaystyle\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \infty$, then the series $\displaystyle\sum_{n=1}^{\infty} a_n$ is divergent.
>
> (iii) If $\displaystyle\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = 1$, the Ratio Test is inconclusive; that is, no conclusion can be drawn about the convergence or divergence of $\sum a_n$.
>
> *Stewart: 11.6, The Ratio Test*

^thm-86-1

> [!proof]+ Proof
> (The ratios are assumed defined, that is, $a_n \ne 0$, at least for large $n$.)
>
> **(i)** The idea is to compare the given series with a convergent geometric series. Since $L < 1$, we can choose a number $r$ with $L < r < 1$. Since $|a_{n+1}/a_n| \to L$ and $L < r$, the ratio $|a_{n+1}/a_n|$ is eventually less than $r$ (take $\varepsilon = r - L$ in [[§80 Sequences#^def-80-3|Definition §80.3]]): there is an integer $N$ such that
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| < r \quad\text{whenever } n \ge N, \qquad\text{or equivalently}\qquad |a_{n+1}| < |a_n|\, r \quad\text{whenever } n \ge N . \qquad (1)
> $$
>
> Putting $n$ successively equal to $N, N+1, N+2, \ldots$ in (1),
>
> $$
> |a_{N+1}| < |a_N| r , \qquad |a_{N+2}| < |a_{N+1}| r < |a_N| r^2 , \qquad |a_{N+3}| < |a_{N+2}| r < |a_N| r^3 ,
> $$
>
> and in general
>
> $$
> |a_{N+k}| < |a_N| r^k \qquad \text{for all } k \ge 1 . \qquad (2)
> $$
>
> The series $\sum_{k=1}^{\infty} |a_N| r^k = |a_N| r + |a_N| r^2 + |a_N| r^3 + \cdots$ is a convergent geometric series, since $0 < r < 1$. So (2) and the Direct Comparison Test show that
>
> $$
> \sum_{n=N+1}^{\infty} |a_n| = \sum_{k=1}^{\infty} |a_{N+k}| = |a_{N+1}| + |a_{N+2}| + |a_{N+3}| + \cdots
> $$
>
> is convergent. A finite number of terms does not affect convergence, so $\sum_{n=1}^{\infty} |a_n|$ is convergent: $\sum a_n$ is absolutely convergent, hence convergent.
>
> **(ii)** If $|a_{n+1}/a_n| \to L > 1$ or $|a_{n+1}/a_n| \to \infty$, the ratio is eventually greater than $1$: there is an integer $N$ such that $|a_{n+1}/a_n| > 1$ whenever $n \ge N$. So $|a_{n+1}| > |a_n|$ whenever $n \ge N$, hence $|a_n| \ge |a_N| > 0$ for all $n \ge N$, and $\lim_{n \to \infty} a_n \ne 0$. Therefore $\sum a_n$ diverges by the Test for Divergence.
>
> **(iii)** [[§86 The Ratio and Root Tests#^ex-86-3|Example §86.3]] below exhibits two series with ratio limit $1$, one divergent and one convergent.

^pf-86-1

*Uses:* [[§82 Series#^thm-82-1|§82.1]], [[§84 The Comparison Tests#^thm-84-1|§84.1]], [[§82 Series#^prop-82-7|§82.7]], [[§85 Alternating Series and Absolute Convergence#^thm-85-3|§85.3]], [[§82 Series#^cor-82-5|§82.5]], [[§80 Sequences#^def-80-3|Def. §80.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^thm-14-9|451 Thm. §14.9]], in the stronger form with $\limsup |a_{n+1}/a_n| < 1$ and $\liminf |a_{n+1}/a_n| > 1$, so that the limit need not exist. For sequences, [[§9a Divergence to ±∞ and the Ratio Test#^thm-9a-3|451 Thm. §9a.3]].

> [!example] Example §86.1: An Alternating Series by the Ratio Test
> Test $\displaystyle\sum_{n=1}^{\infty} (-1)^n \frac{n^3}{3^n}$ for absolute convergence.
>
> With $a_n = (-1)^n n^3 / 3^n$,
>
> $$
> \left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{\dfrac{(-1)^{n+1} (n+1)^3}{3^{n+1}}}{\dfrac{(-1)^n n^3}{3^n}} \right| = \frac{(n+1)^3}{3^{n+1}} \cdot \frac{3^n}{n^3} = \frac13 \left( \frac{n+1}{n} \right)^3 = \frac13 \left( 1 + \frac1n \right)^3 \to \frac13 < 1 .
> $$
>
> By the Ratio Test, the series is absolutely convergent.
>
> *Stewart: Example 11.6.1*

^ex-86-1

> [!example] Example §86.2: A Limit Equal to e
> Test the convergence of $\displaystyle\sum_{n=1}^{\infty} \frac{n^n}{n!}$.
>
> The terms $a_n = n^n/n!$ are positive, so no absolute values are needed. Using $(n+1)! = (n+1)\,n!$,
>
> $$
> \frac{a_{n+1}}{a_n} = \frac{(n+1)^{n+1}}{(n+1)!} \cdot \frac{n!}{n^n} = \frac{(n+1)(n+1)^n}{(n+1)\,n!} \cdot \frac{n!}{n^n} = \left( \frac{n+1}{n} \right)^n = \left( 1 + \frac1n \right)^n \to e
> $$
>
> as $n \to \infty$ (Equation 3.6.6, [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-7|Theorem §22.7]]). Since $e > 1$, the series diverges by the Ratio Test.
>
> **An easier route.** The Test for Divergence suffices:
>
> $$
> a_n = \frac{n^n}{n!} = \frac{n \cdot n \cdot n \cdots n}{1 \cdot 2 \cdot 3 \cdots n} \ge n ,
> $$
>
> since each factor $n/k$ ($k = 1, \ldots, n$) is $\ge 1$ and the first is $n$. So $a_n \not\to 0$ and the series diverges.
>
> *Stewart: Example 11.6.2*

^ex-86-2

> [!example] Example §86.3: The Ratio Test Is Inconclusive for p-Series
> Apply the Ratio Test to $\displaystyle\sum_{n=1}^{\infty} \frac1n$ and $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2}$.
>
> For $a_n = 1/n$: $\displaystyle\left| \frac{a_{n+1}}{a_n} \right| = \frac{1/(n+1)}{1/n} = \frac{n}{n+1} \to 1$.
>
> For $a_n = 1/n^2$: $\displaystyle\left| \frac{a_{n+1}}{a_n} \right| = \frac{1/(n+1)^2}{1/n^2} = \left( \frac{n}{n+1} \right)^2 \to 1$.
>
> In both cases the Ratio Test gives no answer. The first series is the harmonic series, which diverges; the second is a $p$-series with $p > 1$, which converges. So a ratio limit of $1$ is compatible with either behavior, which proves part (iii). The Ratio Test always fails for $p$-series, and is usually conclusive when $a_n$ contains an exponential or a factorial, as in [[§86 The Ratio and Root Tests#^ex-86-1|Examples §86.1]] and [[§86 The Ratio and Root Tests#^ex-86-2|§86.2]].
>
> *Stewart: Example 11.6.3*

^ex-86-3

> [!remark]- Remark: Estimating Sums
> How the sum of a series is estimated depends on the test that proved convergence. If the Ratio Test works and the series happens to be alternating, use the Alternating Series Estimation Theorem ([[§85 Alternating Series and Absolute Convergence#^thm-85-2|Theorem §85.2]]). If all terms are positive, the proof of the Ratio Test suggests comparing the remainder with a geometric series: with $r_n = a_{n+1}/a_n$, if $\{r_n\}$ decreases and $r_{n+1} < 1$, then $R_n \le a_{n+1}/(1 - r_{n+1})$, and if $\{r_n\}$ increases to $L < 1$, then $R_n \le a_{n+1}/(1 - L)$ (Stewart, Exercise 42).

^rem-86-1

## The Root Test

> [!theorem] Theorem §86.2: The Root Test
> (i) If $\displaystyle\lim_{n \to \infty} \sqrt[n]{|a_n|} = L < 1$, then the series $\displaystyle\sum_{n=1}^{\infty} a_n$ is absolutely convergent (and therefore convergent).
>
> (ii) If $\displaystyle\lim_{n \to \infty} \sqrt[n]{|a_n|} = L > 1$ or $\displaystyle\lim_{n \to \infty} \sqrt[n]{|a_n|} = \infty$, then the series $\displaystyle\sum_{n=1}^{\infty} a_n$ is divergent.
>
> (iii) If $\displaystyle\lim_{n \to \infty} \sqrt[n]{|a_n|} = 1$, the Root Test is inconclusive.
>
> *Stewart: 11.6, The Root Test*

^thm-86-2

> [!proof]+ Proof
> (Stewart says the proof "is similar to the proof of the Ratio Test and is left as Exercise 45"; here it is.)
>
> **(i)** Choose $r$ with $L < r < 1$. Since $\sqrt[n]{|a_n|} \to L < r$, there is an integer $N$ such that $\sqrt[n]{|a_n|} < r$ whenever $n \ge N$, that is,
>
> $$
> |a_n| < r^n \qquad \text{whenever } n \ge N .
> $$
>
> $\sum_{n=N}^{\infty} r^n$ is a convergent geometric series ($0 < r < 1$), so $\sum_{n=N}^{\infty} |a_n|$ converges by the Direct Comparison Test (for terms $\ge 0$), and so does $\sum_{n=1}^{\infty} |a_n|$. Hence $\sum a_n$ is absolutely convergent.
>
> **(ii)** If $\sqrt[n]{|a_n|} \to L > 1$ or $\to \infty$, there is $N$ with $\sqrt[n]{|a_n|} > 1$, that is, $|a_n| > 1$, for $n \ge N$. So $a_n \not\to 0$, and $\sum a_n$ diverges by the Test for Divergence.
>
> **(iii)** For $a_n = 1/n$ and $a_n = 1/n^2$, $\sqrt[n]{|a_n|} = n^{-1/n}$ and $n^{-2/n}$, which both tend to $1$ because $\ln n^{1/n} = (\ln n)/n \to 0$ ([[§80 Sequences#^ex-80-2|Example §80.2]]) and $e^x$ is continuous. The first series diverges and the second converges.

^pf-86-2

*Uses:* [[§82 Series#^thm-82-1|§82.1]], [[§84 The Comparison Tests#^thm-84-1|§84.1]], [[§82 Series#^prop-82-7|§82.7]], [[§85 Alternating Series and Absolute Convergence#^thm-85-3|§85.3]], [[§82 Series#^cor-82-5|§82.5]], [[§80 Sequences#^thm-80-6|§80.6]], [[§80 Sequences#^ex-80-2|Ex. §80.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^thm-14-10|451 Thm. §14.10]], with $\limsup \sqrt[n]{|a_n|}$ in place of the limit; that form gives the radius of convergence of a power series, [[§23 Power Series#^thm-23-2|451 Thm. §23.2]].

If $L = 1$ in the Ratio Test, don't try the Root Test: $L$ will again be $1$. And if $L = 1$ in the Root Test, the Ratio Test will fail too.

> [!example] Example §86.4: nth Powers
> Test the convergence of $\displaystyle\sum_{n=1}^{\infty} \left( \frac{2n + 3}{3n + 2} \right)^n$.
>
> With $a_n = \left( \dfrac{2n+3}{3n+2} \right)^n$,
>
> $$
> \sqrt[n]{|a_n|} = \frac{2n + 3}{3n + 2} = \frac{2 + \dfrac3n}{3 + \dfrac2n} \to \frac23 < 1 .
> $$
>
> So the series is absolutely convergent (and therefore convergent) by the Root Test.
>
> *Stewart: Example 11.6.4*

^ex-86-4

> [!example] Example §86.5: Try the Test for Divergence First
> Determine whether $\displaystyle\sum_{n=1}^{\infty} \left( \frac{n}{n+1} \right)^n$ converges or diverges.
>
> The Root Test seems natural, but $\sqrt[n]{|a_n|} = \dfrac{n}{n+1} \to 1$, so it is inconclusive. However, by Equation 3.6.6 ([[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-7|Theorem §22.7]]),
>
> $$
> a_n = \left( \frac{n}{n+1} \right)^n = \frac{1}{\left( \dfrac{n+1}{n} \right)^n} = \frac{1}{\left( 1 + \dfrac1n \right)^n} \to \frac1e \qquad \text{as } n \to \infty .
> $$
>
> Since this limit is not $0$, the series diverges by the Test for Divergence. When testing a series, it often pays to apply the Test for Divergence before attempting other tests.
>
> *Stewart: Example 11.6.5*

^ex-86-5
