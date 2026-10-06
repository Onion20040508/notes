---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 82
stewart: "11.2"
aliases: ["Stewart 11.2"]
tags: [calculus]
---
← [[§81 Monotonic and Bounded Sequences]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§83 The Integral Test and Estimates of Sums]] →

*Stewart, Section 11.2.*

We cannot add infinitely many numbers one by one, but we can add the first $n$ of them and ask what happens as $n \to \infty$. A series converges when its sequence of partial sums does, and its sum is that limit. Two series can be summed exactly: telescoping series, whose partial sums collapse, and geometric series, the most important series of all. The section also proves the Test for Divergence (if the terms do not tend to $0$, the series diverges), shows by the harmonic series that terms tending to $0$ are not enough, and records that convergent series can be added and multiplied by constants term by term.

## Infinite Series

> [!definition] Definition §95.1: Infinite Series
> Adding the terms of an infinite sequence $\{a_n\}_{n=1}^{\infty}$ gives an expression
>
> $$
> a_1 + a_2 + a_3 + \cdots + a_n + \cdots \qquad (1)
> $$
>
> called an **infinite series** (or just a **series**), denoted by
>
> $$
> \sum_{n=1}^{\infty} a_n \qquad\text{or}\qquad \sum a_n .
> $$
>
> *Stewart: 11.2, Equation 1*

^def-82-1

Some series obviously have no finite sum: the cumulative sums of $1 + 2 + 3 + \cdots + n + \cdots$ grow without bound. Others do: in Zeno's series $\frac12 + \frac14 + \frac18 + \cdots$ the sum of the first $n$ terms is $\frac{2^n - 1}{2^n} = 1 - \frac{1}{2^n}$, which can be made as close to $1$ as we like. The same idea defines the sum of any series.

> [!definition] Definition §95.2: Partial Sums
> Given a series $\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$, its **$n$th partial sum** is
>
> $$
> s_n = \sum_{i=1}^{n} a_i = a_1 + a_2 + \cdots + a_n .
> $$
>
> *Stewart: 11.2, Definition 2*

^def-82-2

> [!definition] Definition §95.3: Convergent Series and Its Sum
> Let $s_n$ be the $n$th partial sum of a series $\sum_{n=1}^{\infty} a_n$. If the sequence $\{s_n\}$ is convergent and $\lim_{n \to \infty} s_n = s$ exists as a real number, then the series $\sum a_n$ is **convergent**, and we write
>
> $$
> a_1 + a_2 + \cdots + a_n + \cdots = s \qquad\text{or}\qquad \sum_{n=1}^{\infty} a_n = s .
> $$
>
> The number $s$ is the **sum** of the series. If $\{s_n\}$ is divergent, the series is **divergent**. Thus
>
> $$
> \sum_{n=1}^{\infty} a_n = \lim_{n \to \infty} \sum_{i=1}^{n} a_i .
> $$
>
> *Stewart: 11.2, Definition 2*

^def-82-3

> [!remark] Remark: Two Sequences, and the Analogy with Improper Integrals
> With every series $\sum a_n$ come two sequences: the sequence $\{a_n\}$ of its *terms* and the sequence $\{s_n\}$ of its *partial sums*. Convergence of the series is about $\{s_n\}$. Compare the improper integral $\int_1^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_1^t f(x)\,dx$ ([[§58 Improper Integrals#^def-58-1|Definition §58.1]]): there we integrate from $1$ to $t$ and let $t \to \infty$; for a series we sum from $1$ to $n$ and let $n \to \infty$.

^rem-82-1

> [!example] Example §95.1: Sums from Partial Sums; a Telescoping Sum
> **(a)** If the partial sums of $\sum a_n$ are $s_n = \dfrac{2n}{3n + 5}$, then
>
> $$
> \sum_{n=1}^{\infty} a_n = \lim_{n \to \infty} \frac{2n}{3n + 5} = \lim_{n \to \infty} \frac{2}{3 + \dfrac5n} = \frac23 .
> $$
>
> **(b)** Show that $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$ is convergent, and find its sum.
>
> Here we must find $s_n$ ourselves. The partial fraction decomposition ([[§54 Integration of Rational Functions by Partial Fractions|§54]]) is $\dfrac{1}{i(i+1)} = \dfrac1i - \dfrac{1}{i+1}$, so
>
> $$
> \begin{aligned}
> s_n = \sum_{i=1}^{n} \frac{1}{i(i+1)} &= \sum_{i=1}^{n} \left( \frac1i - \frac{1}{i+1} \right) \\
> &= \left( 1 - \frac12 \right) + \left( \frac12 - \frac13 \right) + \left( \frac13 - \frac14 \right) + \cdots + \left( \frac1n - \frac{1}{n+1} \right) = 1 - \frac{1}{n+1} .
> \end{aligned}
> $$
>
> The terms cancel in pairs: this is a **telescoping sum**, which collapses to two terms. Hence $\lim_{n \to \infty} s_n = 1 - 0 = 1$, and
>
> $$
> \sum_{n=1}^{\infty} \frac{1}{n(n+1)} = 1 .
> $$
>
> Note that both $a_n \to 0$ and $s_n \to 1$.
>
> *Stewart: Examples 11.2.1 and 11.2.2*

^ex-82-1

## Sum of a Geometric Series

> [!theorem] Theorem §95.1: The Geometric Series
> The **geometric series** with first term $a \ne 0$ and **common ratio** $r$,
>
> $$
> \sum_{n=1}^{\infty} a r^{n-1} = a + ar + ar^2 + \cdots ,
> $$
>
> has partial sums
>
> $$
> s_n = a + ar + \cdots + ar^{n-1} = \frac{a(1 - r^n)}{1 - r} \qquad (r \ne 1). \qquad (3)
> $$
>
> It is convergent if $|r| < 1$, and its sum is
>
> $$
> \sum_{n=1}^{\infty} a r^{n-1} = \frac{a}{1 - r} \qquad |r| < 1 . \qquad (4)
> $$
>
> If $|r| \ge 1$, the geometric series is divergent. In words: the sum of a convergent geometric series is $\dfrac{\text{first term}}{1 - \text{common ratio}}$.
>
> *Stewart: 11.2, Equations 3 and 4*

^thm-82-1

> [!proof]+ Proof
> **$r = 1$.** Then $s_n = a + a + \cdots + a = na \to \pm\infty$ (as $a \ne 0$), so $\lim s_n$ does not exist and the series diverges.
>
> **$r \ne 1$.** Write $s_n$ and $r s_n$ one above the other:
>
> $$
> \begin{aligned}
> s_n &= a + ar + ar^2 + \cdots + ar^{n-1} \\
> r s_n &= \phantom{a + {}} ar + ar^2 + \cdots + ar^{n-1} + ar^n .
> \end{aligned}
> $$
>
> Subtracting, everything cancels except $s_n - r s_n = a - ar^n$, so $s_n = \dfrac{a(1 - r^n)}{1 - r}$, which is (3).
>
> **$|r| < 1$.** Then $r^n \to 0$ ([[§80 Sequences#^thm-80-8|Theorem §80.8]]), so by the Limit Laws
>
> $$
> \lim_{n \to \infty} s_n = \lim_{n \to \infty} \frac{a(1 - r^n)}{1 - r} = \frac{a}{1 - r} - \frac{a}{1 - r} \lim_{n \to \infty} r^n = \frac{a}{1 - r} .
> $$
>
> **$r \le -1$ or $r > 1$.** Then $\{r^n\}$ is divergent ([[§80 Sequences#^thm-80-8|Theorem §80.8]]). By (3), $r^n = 1 - \frac{(1 - r)}{a} s_n$, so if $\{s_n\}$ converged, so would $\{r^n\}$. Hence $\lim s_n$ does not exist. (Stewart: "by Equation 3, $\lim s_n$ does not exist"; the displayed solution for $r^n$ is why.)

^pf-82-1

*Uses:* [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§80 Sequences#^thm-80-8|§80.8]], [[§80 Sequences#^thm-80-3|§80.3]]

> [!remark]- Remark: A Geometric Picture
> Stewart's Figure 3 (for $0 < r < 1$): on the right side of a square of side $a$, stack segments of lengths $ar, ar^2, ar^3, \ldots$ above it, the sides of smaller squares placed against the right edge, each on top of the previous one, so the total height is $s = a + ar + ar^2 + \cdots$. The line from the bottom-left corner of the first square through the bottom-left corners of the smaller squares crosses the top side of the first square at distance $a - ar$ from the left and reaches height $s$ above the bottom-right corner. The right triangles with legs $(a - ar, a)$ and $(a, s)$ are similar, so
>
> $$
> \frac{s}{a} = \frac{a}{a - ar}, \qquad s = \frac{a}{1 - r} .
> $$

^rem-82-2

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^ex-14-4|451 Ex. §14.4]] (the same computation); every use in 451 is collected in [[Geometric series]].
> - Matrix version: [[§19 The Leontief Input–Output Model#^prop-19-1|235 Prop. §19.1]] ($(I - C)^{-1} = I + C + C^2 + \cdots$ for a nonnegative matrix with column sums less than 1, the same telescoping identity), applied to the Leontief model.

> [!example] Example §95.2: Identifying a and r
> **(a)** Find the sum of $5 - \frac{10}{3} + \frac{20}{9} - \frac{40}{27} + \cdots$.
>
> The first term is $a = 5$ and each term is the preceding one times $r = -\frac23$. Since $|r| = \frac23 < 1$, the series converges by [[§82 Series#^thm-82-1|Theorem §82.1]], and
>
> $$
> 5 - \frac{10}{3} + \frac{20}{9} - \frac{40}{27} + \cdots = \frac{5}{1 - \left( -\frac23 \right)} = \frac{5}{\frac53} = 3 .
> $$
>
> The partial sums $5,\ 1.667,\ 3.889,\ 2.407,\ 3.395,\ \ldots$ jump alternately above and below $3$ and close in on it.
>
> **(b)** Is $\displaystyle\sum_{n=1}^{\infty} 2^{2n} 3^{1-n}$ convergent or divergent?
>
> Rewrite the $n$th term in the form $a r^{n-1}$:
>
> $$
> \sum_{n=1}^{\infty} 2^{2n} 3^{1-n} = \sum_{n=1}^{\infty} (2^2)^n 3^{-(n-1)} = \sum_{n=1}^{\infty} \frac{4^n}{3^{n-1}} = \sum_{n=1}^{\infty} 4 \left( \frac43 \right)^{n-1} .
> $$
>
> (Writing out the first terms, $4 + \frac{16}{3} + \frac{64}{9} + \cdots$, gives the same $a$ and $r$.) This is geometric with $a = 4$ and $r = \frac43 > 1$, so it diverges.
>
> *Stewart: Examples 11.2.3 and 11.2.4*

^ex-82-2

> [!example] Example §95.3: A Repeating Decimal
> Write $2.3\overline{17} = 2.3171717\ldots$ as a ratio of integers.
>
> $$
> 2.3171717\ldots = 2.3 + \frac{17}{10^3} + \frac{17}{10^5} + \frac{17}{10^7} + \cdots
> $$
>
> After the first term we have a geometric series with $a = 17/10^3$ and $r = 1/10^2$. Therefore
>
> $$
> 2.3\overline{17} = 2.3 + \frac{\dfrac{17}{10^3}}{1 - \dfrac{1}{10^2}} = 2.3 + \frac{\dfrac{17}{1000}}{\dfrac{99}{100}} = \frac{23}{10} + \frac{17}{990} = \frac{2277 + 17}{990} = \frac{2294}{990} = \frac{1147}{495} .
> $$
>
> *Stewart: Example 11.2.6*

^ex-82-3

Stewart's Example 5 is an application of the finite formula (3): if a daily dose raises a drug concentration by $0.2$ mg/mL and $30\%$ survives each day, the concentration after the $n$th dose is $C_n = 0.2 + 0.2(0.3) + \cdots + 0.2(0.3)^{n-1} = \frac27 [1 - (0.3)^n]$, which tends to $\frac27$ mg/mL.

> [!theorem] Corollary §95.2: The Geometric Series in x
> $$
> \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots = \frac{1}{1 - x} \qquad |x| < 1 . \qquad (5)
> $$
>
> Here, as always with series, $x^0 = 1$ even when $x = 0$.
>
> *Stewart: 11.2, Equation 5 (Example 11.2.7)*

^cor-82-2

> [!proof]+ Proof
> The series starts with $n = 0$, so its first term is $x^0 = 1$; it is the geometric series with $a = 1$ and $r = x$. Since $|r| = |x| < 1$, [[§82 Series#^thm-82-1|Theorem §82.1]] gives the sum $\dfrac{1}{1 - x}$.

^pf-82-2

*Uses:* [[§82 Series#^thm-82-1|§82.1]]

## Test for Divergence

> [!theorem] Theorem §95.3: The Harmonic Series Diverges
> The **harmonic series**
>
> $$
> \sum_{n=1}^{\infty} \frac1n = 1 + \frac12 + \frac13 + \frac14 + \cdots
> $$
>
> is divergent.
>
> *Stewart: Example 11.2.8*

^thm-82-3

> [!proof]+ Proof
> Consider the partial sums $s_2, s_4, s_8, s_{16}, s_{32}, \ldots$ and replace each term by a smaller (or equal) power of $\frac12$:
>
> $$
> \begin{aligned}
> s_2 &= 1 + \tfrac12 , \\
> s_4 &= 1 + \tfrac12 + \left( \tfrac13 + \tfrac14 \right) > 1 + \tfrac12 + \left( \tfrac14 + \tfrac14 \right) = 1 + \tfrac22 , \\
> s_8 &= 1 + \tfrac12 + \left( \tfrac13 + \tfrac14 \right) + \left( \tfrac15 + \tfrac16 + \tfrac17 + \tfrac18 \right) \\
> &> 1 + \tfrac12 + \left( \tfrac14 + \tfrac14 \right) + \left( \tfrac18 + \tfrac18 + \tfrac18 + \tfrac18 \right) = 1 + \tfrac12 + \tfrac12 + \tfrac12 = 1 + \tfrac32 , \\
> s_{16} &> 1 + \tfrac12 + \left( \tfrac14 + \tfrac14 \right) + \left( \tfrac18 + \cdots + \tfrac18 \right) + \left( \tfrac{1}{16} + \cdots + \tfrac{1}{16} \right) = 1 + \tfrac42 .
> \end{aligned}
> $$
>
> In general, the block $\frac{1}{2^{k-1} + 1} + \cdots + \frac{1}{2^k}$ has $2^{k-1}$ terms, each at least $\frac{1}{2^k}$, so it is at least $2^{k-1} \cdot \frac{1}{2^k} = \frac12$. Adding the first term $1$ and the blocks $k = 1, \ldots, n$,
>
> $$
> s_{2^n} \ge 1 + \frac n2 ,
> $$
>
> with strict inequality for $n \ge 2$. (Stewart writes $s_{2^n} > 1 + \frac n2$ "in general"; for $n = 1$ it is an equality.) Hence $s_{2^n} \to \infty$. Since all terms are positive, $\{s_n\}$ is increasing, so for any $M$ we can pick $k$ with $1 + \frac k2 > M$, and then $s_n \ge s_{2^k} > M$ for all $n \ge 2^k$. So $s_n \to \infty$, and the harmonic series diverges.

^pf-82-3

*Uses:* [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§80 Sequences#^def-80-4|Def. §80.4]]

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^thm-14-5|451 Thm. §14.5]]; the integral test gives a second proof, [[§15 Alternating Series and Integral Tests#^ex-15-3|451 Ex. §15.3]] (and [[§83 The Integral Test and Estimates of Sums#^thm-83-2|Theorem §83.2]] with $p = 1$). The grouping argument is due to Nicole Oresme (1323–1382).

> [!theorem] Theorem §95.4: Terms of a Convergent Series Tend to Zero
> If the series $\displaystyle\sum_{n=1}^{\infty} a_n$ is convergent, then $\displaystyle\lim_{n \to \infty} a_n = 0$.
>
> *Stewart: 11.2, Theorem 6*

^thm-82-4

> [!proof]+ Proof
> Let $s_n = a_1 + a_2 + \cdots + a_n$. Then $a_n = s_n - s_{n-1}$. Since $\sum a_n$ is convergent, $\{s_n\}$ is convergent; let $\lim_{n \to \infty} s_n = s$. Since $n - 1 \to \infty$ as $n \to \infty$, also $\lim_{n \to \infty} s_{n-1} = s$ (if $|s_m - s| < \varepsilon$ for $m > N$, then $|s_{n-1} - s| < \varepsilon$ for $n > N + 1$). Therefore
>
> $$
> \lim_{n \to \infty} a_n = \lim_{n \to \infty} (s_n - s_{n-1}) = \lim_{n \to \infty} s_n - \lim_{n \to \infty} s_{n-1} = s - s = 0 .
> $$

^pf-82-4

*Uses:* [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§80 Sequences#^thm-80-3|§80.3]] (Difference Law)

> [!remark] Remark: Warning — The Converse Is False
> If $\lim_{n \to \infty} a_n = 0$, we *cannot* conclude that $\sum a_n$ converges. The harmonic series has $a_n = 1/n \to 0$, but $\sum 1/n$ diverges ([[§82 Series#^thm-82-3|Theorem §82.3]]).

^rem-82-3

> [!theorem] Corollary §95.5: Test for Divergence
> If $\displaystyle\lim_{n \to \infty} a_n$ does not exist or if $\displaystyle\lim_{n \to \infty} a_n \ne 0$, then the series $\displaystyle\sum_{n=1}^{\infty} a_n$ is divergent.
>
> *Stewart: 11.2, Test for Divergence 7*

^cor-82-5

> [!proof]+ Proof
> This is the [[Contrapositive, Converse and Inverse|contrapositive]] of [[§82 Series#^thm-82-4|Theorem §82.4]]: if the series is not divergent, then it is convergent, and so $\lim_{n \to \infty} a_n = 0$.

^pf-82-5

*Uses:* [[§82 Series#^thm-82-4|§82.4]]

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^cor-14-2|451 Cor. §14.2]], where it follows from the Cauchy criterion for series, [[§14 Series#^thm-14-1|451 Thm. §14.1]].

> [!example] Example §95.4: Using the Test for Divergence
> Show that $\displaystyle\sum_{n=1}^{\infty} \frac{n^2}{5n^2 + 4}$ diverges.
>
> $$
> \lim_{n \to \infty} a_n = \lim_{n \to \infty} \frac{n^2}{5n^2 + 4} = \lim_{n \to \infty} \frac{1}{5 + 4/n^2} = \frac15 \ne 0 ,
> $$
>
> so the series diverges by the Test for Divergence.
>
> The test works in one direction only. If $\lim a_n \ne 0$, then $\sum a_n$ diverges. If $\lim a_n = 0$, the test tells us *nothing*: $\sum a_n$ might converge ([[§82 Series#^ex-82-1|Example §82.1]](b)) or diverge (the harmonic series).
>
> *Stewart: Example 11.2.9*

^ex-82-4

## Properties of Convergent Series

> [!theorem] Theorem §95.6: Sums, Differences and Constant Multiples of Series
> If $\sum a_n$ and $\sum b_n$ are convergent series, then so are the series $\sum c a_n$ (where $c$ is a constant), $\sum (a_n + b_n)$ and $\sum (a_n - b_n)$, and
>
> $$
> \text{(i)}\ \sum_{n=1}^{\infty} c a_n = c \sum_{n=1}^{\infty} a_n \qquad
> \text{(ii)}\ \sum_{n=1}^{\infty} (a_n + b_n) = \sum_{n=1}^{\infty} a_n + \sum_{n=1}^{\infty} b_n \qquad
> \text{(iii)}\ \sum_{n=1}^{\infty} (a_n - b_n) = \sum_{n=1}^{\infty} a_n - \sum_{n=1}^{\infty} b_n
> $$
>
> *Stewart: 11.2, Theorem 8*

^thm-82-6

> [!proof]+ Proof
> Let
>
> $$
> s_n = \sum_{i=1}^{n} a_i , \qquad s = \sum_{n=1}^{\infty} a_n , \qquad t_n = \sum_{i=1}^{n} b_i , \qquad t = \sum_{n=1}^{\infty} b_n .
> $$
>
> **(ii)** The $n$th partial sum of $\sum (a_n + b_n)$ is $u_n = \sum_{i=1}^{n} (a_i + b_i)$. A finite sum can be split ([[§39 The Definite Integral#^thm-39-3|Theorem §39.3]], Stewart's Equation 5.2.10), so by the Sum Law for sequences
>
> $$
> \lim_{n \to \infty} u_n = \lim_{n \to \infty} \left( \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i \right) = \lim_{n \to \infty} s_n + \lim_{n \to \infty} t_n = s + t .
> $$
>
> So $\sum (a_n + b_n)$ is convergent with sum $s + t$.
>
> **(i) and (iii)** (Stewart leaves these as exercises.) The $n$th partial sum of $\sum c a_n$ is $\sum_{i=1}^{n} c a_i = c s_n \to c s$ by the Constant Multiple Law. The $n$th partial sum of $\sum (a_n - b_n)$ is $s_n - t_n \to s - t$ by the Difference Law.

^pf-82-6

*Uses:* [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§80 Sequences#^thm-80-3|§80.3]], [[§39 The Definite Integral#^thm-39-3|§39.3]]

> [!example] Example §95.5: Combining Known Sums
> Find the sum of $\displaystyle\sum_{n=1}^{\infty} \left( \frac{3}{n(n+1)} + \frac{1}{2^n} \right)$.
>
> $\sum 1/2^n$ is geometric with $a = \frac12$ and $r = \frac12$, so $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n} = \frac{\frac12}{1 - \frac12} = 1$. By [[§82 Series#^ex-82-1|Example §82.1]](b), $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+1)} = 1$. Both series converge, so by [[§82 Series#^thm-82-6|Theorem §82.6]] the given series converges and
>
> $$
> \sum_{n=1}^{\infty} \left( \frac{3}{n(n+1)} + \frac{1}{2^n} \right) = 3 \sum_{n=1}^{\infty} \frac{1}{n(n+1)} + \sum_{n=1}^{\infty} \frac{1}{2^n} = 3 \cdot 1 + 1 = 4 .
> $$
>
> *Stewart: Example 11.2.10*

^ex-82-5

> [!theorem] Proposition §95.7: Finitely Many Terms Do Not Matter
> For any $N$, the series $\sum_{n=1}^{\infty} a_n$ converges if and only if $\sum_{n=N+1}^{\infty} a_n$ converges, and then
>
> $$
> \sum_{n=1}^{\infty} a_n = \sum_{n=1}^{N} a_n + \sum_{n=N+1}^{\infty} a_n .
> $$
>
> So changing, adding or deleting finitely many terms does not affect whether a series converges (it does affect the sum). For example, if $\sum_{n=4}^{\infty} n/(n^3 + 1)$ converges, so does $\sum_{n=1}^{\infty} \frac{n}{n^3 + 1} = \frac12 + \frac29 + \frac{3}{28} + \sum_{n=4}^{\infty} \frac{n}{n^3 + 1}$.
>
> *Stewart: 11.2 (text)*

^prop-82-7

> [!proof]+ Proof
> Let $s_n$ be the partial sums of $\sum_{n=1}^{\infty} a_n$, let $C = \sum_{n=1}^{N} a_n$, and for $n > N$ let $t_n = \sum_{i=N+1}^{n} a_i$ be the partial sums of the tail. Then $s_n = C + t_n$ for $n > N$. A constant sequence converges, so by the Sum and Difference Laws $\{s_n\}$ converges if and only if $\{t_n\}$ does, and then $\lim s_n = C + \lim t_n$.

^pf-82-7

*Uses:* [[§82 Series#^def-82-2|Def. §82.2]], [[§82 Series#^def-82-3|Def. §82.3]], [[§80 Sequences#^thm-80-3|§80.3]]
