---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 73
stewart: "11.5"
aliases: ["Stewart 11.5"]
tags: [calculus]
---
← [[§72 The Comparison Tests]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§74 The Ratio and Root Tests]] →

*Stewart, Section 11.5.*

The tests so far apply only to series with positive terms. This section handles terms of both signs. For an *alternating* series, whose signs strictly alternate, decreasing terms tending to $0$ already force convergence, and the error of a partial sum is at most the first omitted term. For arbitrary signs the key notion is *absolute convergence*: if $\sum |a_n|$ converges, so does $\sum a_n$, so every positive-term test becomes a test for general series. Series that converge only conditionally, like the alternating harmonic series, are fragile: rearranging their terms can change the sum.

## Alternating Series

> [!definition] Definition §73.1: Alternating Series
> An **alternating series** is a series whose terms are alternately positive and negative, for example
>
> $$
> 1 - \frac12 + \frac13 - \frac14 + \cdots = \sum_{n=1}^{\infty} (-1)^{n-1} \frac1n , \qquad
> -\frac12 + \frac23 - \frac34 + \frac45 - \cdots = \sum_{n=1}^{\infty} (-1)^n \frac{n}{n+1} .
> $$
>
> Its $n$th term has the form $a_n = (-1)^{n-1} b_n$ or $a_n = (-1)^n b_n$, where $b_n = |a_n|$ is a positive number.
>
> *Stewart: 11.5 (text)*

^def-73-1

> [!theorem] Theorem §73.1: The Alternating Series Test
> If the alternating series
>
> $$
> \sum_{n=1}^{\infty} (-1)^{n-1} b_n = b_1 - b_2 + b_3 - b_4 + b_5 - b_6 + \cdots \qquad (b_n > 0)
> $$
>
> satisfies the conditions
>
> $$
> \text{(i)}\ \ b_{n+1} \le b_n \ \text{ for all } n \qquad\qquad \text{(ii)}\ \ \lim_{n \to \infty} b_n = 0 ,
> $$
>
> then the series is convergent.
>
> *Stewart: 11.5, Alternating Series Test*

^thm-73-1

> [!remark] Remark: Why It Works
> Plot the partial sums on a number line. $s_1 = b_1$; then $s_2 = s_1 - b_2$ lies to the left of $s_1$; then $s_3 = s_2 + b_3$ lies to the right of $s_2$, but to the left of $s_1$ because $b_3 \le b_2$; and so on. The partial sums oscillate back and forth with steps that shrink to $0$. The even partial sums $s_2, s_4, s_6, \ldots$ increase, the odd partial sums $s_1, s_3, s_5, \ldots$ decrease, and both close in on a number $s$, the sum of the series. So the proof treats the even and odd partial sums separately.

^rem-73-1

> [!proof]+ Proof
> **Even partial sums.**
>
> $$
> s_2 = b_1 - b_2 \ge 0 \quad\text{since } b_2 \le b_1, \qquad s_4 = s_2 + (b_3 - b_4) \ge s_2 \quad\text{since } b_4 \le b_3 ,
> $$
>
> and in general $s_{2n} = s_{2n-2} + (b_{2n-1} - b_{2n}) \ge s_{2n-2}$ since $b_{2n} \le b_{2n-1}$. Thus
>
> $$
> 0 \le s_2 \le s_4 \le s_6 \le \cdots \le s_{2n} \le \cdots
> $$
>
> But we can also write
>
> $$
> s_{2n} = b_1 - (b_2 - b_3) - (b_4 - b_5) - \cdots - (b_{2n-2} - b_{2n-1}) - b_{2n} .
> $$
>
> Every term in parentheses is $\ge 0$ and $b_{2n} > 0$, so $s_{2n} \le b_1$ for all $n$. The sequence $\{s_{2n}\}$ is increasing and bounded above, so it converges by the Monotonic Sequence Theorem. Call its limit $s$: $\lim_{n \to \infty} s_{2n} = s$.
>
> **Odd partial sums.** By condition (ii),
>
> $$
> \lim_{n \to \infty} s_{2n+1} = \lim_{n \to \infty} (s_{2n} + b_{2n+1}) = \lim_{n \to \infty} s_{2n} + \lim_{n \to \infty} b_{2n+1} = s + 0 = s .
> $$
>
> **All partial sums.** Both the even and the odd partial sums converge to $s$, so $\lim_{n \to \infty} s_n = s$. (Stewart cites Exercise 11.1.98(a); here is why: given $\varepsilon > 0$, choose $N_1$ with $|s_{2n} - s| < \varepsilon$ for $n > N_1$ and $N_2$ with $|s_{2n+1} - s| < \varepsilon$ for $n > N_2$. Every $m > 2\max\{N_1, N_2\} + 1$ is $2n$ with $n > N_1$ or $2n + 1$ with $n > N_2$, so $|s_m - s| < \varepsilon$.) Hence the series converges.

^pf-73-1

*Uses:* [[§69a Monotonic and Bounded Sequences#^thm-69-9|§69.9]], [[§69 Sequences#^thm-69-3|§69.3]], [[§69 Sequences#^def-69-3|Def. §69.3]], [[§70 Series#^def-70-2|Def. §70.2]], [[§70 Series#^def-70-new1|Def. §70.3]]

![[m233-73-1.svg]]
*Partial sums of the alternating harmonic series $1 - \frac12 + \frac13 - \cdots$. The odd partial sums (red) decrease and the even ones (green) increase, both towards $s = \ln 2 \approx 0.693$. The sum always lies between two consecutive partial sums, so the error $|s - s_n|$ is less than the next step $b_{n+1}$ (orange, for $n = 8$): this is [[§73 Alternating Series and Absolute Convergence#^thm-73-2|Theorem §73.2]].*

> [!remark]- Connections
> - Rigorous treatment: [[§15 Alternating Series and Integral Tests#^thm-15-1|451 Thm. §15.1]], proved there with the [[§14 Series#^def-14-3|Cauchy criterion]] via the estimate $\big|\sum_{k=n}^{m} (-1)^k a_k\big| \le a_n$, which is also the content of [[§73 Alternating Series and Absolute Convergence#^thm-73-2|Theorem §73.2]].

> [!example] Example §73.1: Checking the Two Conditions
> **(a)** The **alternating harmonic series** $\displaystyle 1 - \frac12 + \frac13 - \frac14 + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$ satisfies
>
> $$
> \text{(i)}\ \ b_{n+1} < b_n \ \text{ because } \frac{1}{n+1} < \frac1n , \qquad \text{(ii)}\ \ \lim_{n \to \infty} b_n = \lim_{n \to \infty} \frac1n = 0 ,
> $$
>
> so it is convergent by the Alternating Series Test. Its partial sums zigzag across a value near $0.7$; the exact sum is $\ln 2 \approx 0.693$ (Stewart's Exercise 50; see [[§77 Representations of Functions as Power Series#^rem-77-2|the remark on Gregory's series in §77]]).
>
> **(b)** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n 3n}{4n - 1}$ is alternating, but
>
> $$
> \lim_{n \to \infty} b_n = \lim_{n \to \infty} \frac{3n}{4n - 1} = \lim_{n \to \infty} \frac{3}{4 - \dfrac1n} = \frac34 ,
> $$
>
> so condition (ii) fails and the test does not apply. Instead look at the $n$th term: $a_n = (-1)^n \frac{3n}{4n-1}$ is close to $\frac34$ for large even $n$ and to $-\frac34$ for large odd $n$, so $\lim_{n \to \infty} a_n$ does not exist, and the series diverges by the Test for Divergence ([[§70 Series#^cor-70-5|Corollary §70.5]]).
>
> *Stewart: Examples 11.5.1 and 11.5.2*

^ex-73-1

> [!example] Example §73.2: Decreasing Only Eventually
> Test $\displaystyle\sum_{n=1}^{\infty} (-1)^{n+1} \frac{n^2}{n^3 + 1}$ for convergence or divergence.
>
> The series is alternating, with $b_n = n^2/(n^3 + 1)$.
>
> **Condition (i).** It is not obvious that $b_n$ decreases, so consider $f(x) = x^2/(x^3 + 1)$. By the Quotient Rule,
>
> $$
> f'(x) = \frac{2x(x^3 + 1) - x^2 \cdot 3x^2}{(x^3 + 1)^2} = \frac{2x - x^4}{(x^3 + 1)^2} = \frac{x(2 - x^3)}{(x^3 + 1)^2} .
> $$
>
> For $x > 0$, $f'(x) < 0$ when $2 - x^3 < 0$, that is, $x > \sqrt[3]{2} \approx 1.26$. So $f$ is decreasing on $(\sqrt[3]{2}, \infty)$, and $b_{n+1} = f(n+1) < f(n) = b_n$ for $n \ge 2$. ($b_2 = \frac49 < \frac12 = b_1$ can be checked directly, but all that matters is that $\{b_n\}$ is eventually decreasing: the test applies to the tail from $n = 2$, and [[§70 Series#^prop-70-7|Proposition §70.7]] does the rest.) Alternatively, $b_{n+1} < b_n$ can be checked by cross-multiplying, as in [[§69a Monotonic and Bounded Sequences#^ex-69-4|Example §69.4]].
>
> **Condition (ii).**
>
> $$
> \lim_{n \to \infty} b_n = \lim_{n \to \infty} \frac{n^2}{n^3 + 1} = \lim_{n \to \infty} \frac{1/n}{1 + 1/n^3} = 0 .
> $$
>
> So the series converges by the Alternating Series Test.
>
> *Stewart: Example 11.5.3*

^ex-73-2

## Estimating Sums of Alternating Series

For a series satisfying the conditions of the Alternating Series Test, the error made in using $s_n$ for $s$, the remainder $R_n = s - s_n$, is smaller than the first neglected term.

> [!theorem] Theorem §73.2: Alternating Series Estimation Theorem
> If $s = \sum (-1)^{n-1} b_n$, where $b_n > 0$, is the sum of an alternating series that satisfies
>
> $$
> \text{(i)}\ \ b_{n+1} \le b_n \qquad\text{and}\qquad \text{(ii)}\ \ \lim_{n \to \infty} b_n = 0 ,
> $$
>
> then
>
> $$
> |R_n| = |s - s_n| \le b_{n+1} .
> $$
>
> *Stewart: 11.5, Alternating Series Estimation Theorem*

^thm-73-2

> [!proof]+ Proof
> We show that $s$ lies between any two consecutive partial sums $s_n$ and $s_{n+1}$. In the proof of [[§73 Alternating Series and Absolute Convergence#^thm-73-1|Theorem §73.1]], the even partial sums increase to $s$, so $s_{2k} \le s$ for every $k$. Similarly the odd partial sums decrease to $s$: $s_{2k+1} = s_{2k-1} - (b_{2k} - b_{2k+1}) \le s_{2k-1}$ by condition (i), and $s_{2k+1} \to s$, so $s_{2k+1} \ge s$ for every $k$. (Stewart: "a similar argument shows that $s$ is smaller than all the odd sums.") Consecutive partial sums have one even and one odd index, so $s$ lies between $s_n$ and $s_{n+1}$. It follows that
>
> $$
> |s - s_n| \le |s_{n+1} - s_n| = b_{n+1} .
> $$

^pf-73-2

*Uses:* [[§73 Alternating Series and Absolute Convergence#^thm-73-1|§73.1]] (and its proof), [[§71 The Integral Test and Estimates of Sums#^def-71-1|Def. §71.1]]

> [!example] Example §73.3: Three Decimal Places
> Find the sum of $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{n!}$ correct to three decimal places. (By definition $0! = 1$.)
>
> **Convergence.** The series is alternating with $b_n = 1/n!$, and
>
> $$
> \text{(i)}\ \ b_{n+1} = \frac{1}{(n+1)!} = \frac{1}{n!\,(n+1)} < \frac{1}{n!} = b_n , \qquad
> \text{(ii)}\ \ 0 < \frac{1}{n!} \le \frac1n \to 0 , \text{ so } b_n \to 0
> $$
>
> by the [[§69 Sequences#^thm-69-4|Squeeze Theorem]]. So the series converges by the Alternating Series Test.
>
> **How many terms.** Write out the first terms:
>
> $$
> s = \frac{1}{0!} - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!} - \frac{1}{5!} + \frac{1}{6!} - \frac{1}{7!} + \cdots
> = 1 - 1 + \frac12 - \frac16 + \frac{1}{24} - \frac{1}{120} + \frac{1}{720} - \frac{1}{5040} + \cdots
> $$
>
> Here $b_7 = \frac{1}{5040} < \frac{1}{5000} = 0.0002$ and
>
> $$
> s_6 = 1 - 1 + \frac12 - \frac16 + \frac{1}{24} - \frac{1}{120} + \frac{1}{720} \approx 0.368056 ,
> $$
>
> where $s_6$ denotes the sum of the terms up to $n = 6$ (the first seven terms). By the Alternating Series Estimation Theorem, $|s - s_6| \le b_7 < 0.0002$, so $0.367856 < s < 0.368256$, and $s \approx 0.368$ correct to three decimal places.
>
> In [[§78 Taylor and Maclaurin Series#^thm-78-6|Theorem §78.6]] it is shown that $e^x = \sum_{n=0}^{\infty} x^n/n!$ for all $x$, so this is an approximation of $e^{-1} = 0.367879\ldots$.
>
> *Stewart: Example 11.5.4*

^ex-73-3

> [!remark] Remark: Warning — Only for Alternating Series
> The rule that the error is smaller than the first neglected term is valid, in general, only for alternating series that satisfy the conditions of [[§73 Alternating Series and Absolute Convergence#^thm-73-2|Theorem §73.2]]. It does not apply to other types of series: for $\sum 1/n^2$, the error after $n$ terms is about $1/n$ ([[§71 The Integral Test and Estimates of Sums#^thm-71-3|Theorem §71.3]]), much larger than the first neglected term $1/(n+1)^2$.

^rem-73-2

## Absolute Convergence and Conditional Convergence

> [!definition] Definition §73.2: Absolutely Convergent
> A series $\sum a_n$ is **absolutely convergent** if the series of absolute values
>
> $$
> \sum_{n=1}^{\infty} |a_n| = |a_1| + |a_2| + |a_3| + \cdots
> $$
>
> is convergent. If $\sum a_n$ has positive terms, then $|a_n| = a_n$ and absolute convergence is the same as convergence. For example, $\sum_{n=1}^{\infty} (-1)^{n-1}/n^2 = 1 - \frac{1}{2^2} + \frac{1}{3^2} - \cdots$ is absolutely convergent, because $\sum 1/n^2$ is a convergent $p$-series ($p = 2$).
>
> *Stewart: 11.5, Definition 1; Example 11.5.5*

^def-73-2

> [!definition] Definition §73.3: Conditionally Convergent
> A series $\sum a_n$ is **conditionally convergent** if it is convergent but not absolutely convergent, that is, if $\sum a_n$ converges but $\sum |a_n|$ diverges. For example, the alternating harmonic series $\sum (-1)^{n-1}/n$ converges ([[§73 Alternating Series and Absolute Convergence#^ex-73-1|Example §73.1]]), but its series of absolute values is the harmonic series $\sum 1/n$, which diverges: it is conditionally convergent.
>
> *Stewart: 11.5, Definition 2; Example 11.5.6*

^def-73-3

> [!theorem] Theorem §73.3: Absolute Convergence Implies Convergence
> If a series $\sum a_n$ is absolutely convergent, then it is convergent.
>
> *Stewart: 11.5, Theorem 3*

^thm-73-3

> [!proof]+ Proof
> The inequality
>
> $$
> 0 \le a_n + |a_n| \le 2|a_n|
> $$
>
> is true because $|a_n|$ is either $a_n$ or $-a_n$. If $\sum a_n$ is absolutely convergent, then $\sum |a_n|$ is convergent, so $\sum 2|a_n|$ is convergent ([[§70 Series#^thm-70-6|Theorem §70.6]]). Therefore, by the Direct Comparison Test, $\sum (a_n + |a_n|)$ is convergent. (The test was stated for positive terms; its proof works without change for terms $\ge 0$, since the partial sums are still increasing.) Then
>
> $$
> \sum a_n = \sum (a_n + |a_n|) - \sum |a_n|
> $$
>
> is the difference of two convergent series and is therefore convergent, by [[§70 Series#^thm-70-6|Theorem §70.6]].

^pf-73-3

*Uses:* [[§72 The Comparison Tests#^thm-72-1|§72.1]], [[§70 Series#^thm-70-6|§70.6]], [[§73 Alternating Series and Absolute Convergence#^def-73-2|Def. §73.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§14 Series#^prop-14-6|451 Prop. §14.6]] (via the [[§14 Series#^def-14-3|Cauchy criterion]]), with [[§14 Series#^def-14-4|451 Def. §14.4]].
> - Complex-variables version: [[§61 Convergence of Series#^cor-61-3|342 Cor. §61.3]] (the same statement for series of complex numbers).

Absolute convergence is a stronger type of convergence. An absolutely convergent series converges whatever the signs of its terms; the alternating harmonic series would diverge if all its negative terms were made positive. This makes [[§73 Alternating Series and Absolute Convergence#^thm-73-3|Theorem §73.3]] useful when the signs change irregularly.

> [!example] Example §73.4: Irregular Signs
> Determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{\cos n}{n^2} = \frac{\cos 1}{1^2} + \frac{\cos 2}{2^2} + \frac{\cos 3}{3^2} + \cdots$ is convergent or divergent.
>
> The series has positive and negative terms, but it is not alternating: the first term is positive, the next three are negative, the following three positive. The signs change irregularly. Apply the Direct Comparison Test to the series of absolute values $\sum |\cos n|/n^2$. Since $|\cos n| \le 1$ for all $n$,
>
> $$
> \frac{|\cos n|}{n^2} \le \frac{1}{n^2} .
> $$
>
> $\sum 1/n^2$ is a convergent $p$-series ($p = 2$), so $\sum |\cos n|/n^2$ converges by the Direct Comparison Test (in its version for terms $\ge 0$). Thus $\sum (\cos n)/n^2$ is absolutely convergent, and therefore convergent by [[§73 Alternating Series and Absolute Convergence#^thm-73-3|Theorem §73.3]].
>
> *Stewart: Example 11.5.7*

^ex-73-4

> [!example] Example §73.5: Absolutely, Conditionally, or Not at All
> Determine whether each series is absolutely convergent, conditionally convergent, or divergent.
>
> $$
> \text{(a)}\ \sum_{n=1}^{\infty} \frac{(-1)^n}{n^3} \qquad \text{(b)}\ \sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt[3]{n}} \qquad \text{(c)}\ \sum_{n=1}^{\infty} (-1)^n \frac{n}{2n + 1}
> $$
>
> **(a)** $\displaystyle\sum_{n=1}^{\infty} \left| \frac{(-1)^n}{n^3} \right| = \sum_{n=1}^{\infty} \frac{1}{n^3}$ converges ($p$-series with $p = 3$), so the series is absolutely convergent.
>
> **(b)** First test for absolute convergence: $\displaystyle\sum_{n=1}^{\infty} \left| \frac{(-1)^n}{\sqrt[3]{n}} \right| = \sum_{n=1}^{\infty} \frac{1}{\sqrt[3]{n}}$ diverges ($p$-series with $p = \frac13$), so the series is *not* absolutely convergent. It converges by the Alternating Series Test: $b_n = 1/\sqrt[3]{n}$ decreases and tends to $0$. Since it converges but not absolutely, it is conditionally convergent.
>
> **(c)** The series is alternating, but $\dfrac{n}{2n+1} \to \dfrac12$, so the terms are alternately close to $\frac12$ and $-\frac12$, and $\lim_{n \to \infty} (-1)^n \frac{n}{2n+1}$ does not exist. The series diverges by the Test for Divergence.
>
> *Stewart: Example 11.5.8*

^ex-73-5

## Rearrangements

Whether a convergent series is absolutely or conditionally convergent decides whether infinite sums behave like finite sums. The order of the terms in a finite sum does not matter. For infinite series it can.

> [!definition] Definition §73.4: Rearrangement
> A **rearrangement** of an infinite series $\sum a_n$ is a series obtained by changing the order of the terms (each term used exactly once), for instance
>
> $$
> a_1 + a_2 + a_5 + a_3 + a_4 + a_{15} + a_6 + a_7 + a_{20} + \cdots
> $$
>
> *Stewart: 11.5 (text)*

^def-73-4

> [!theorem] Theorem §73.4: Rearranging Series
> (a) If $\sum a_n$ is an absolutely convergent series with sum $s$, then any rearrangement of $\sum a_n$ has the same sum $s$.
>
> (b) (Riemann) If $\sum a_n$ is a conditionally convergent series and $r$ is any real number whatsoever, then there is a rearrangement of $\sum a_n$ that has a sum equal to $r$.
>
> *Stewart: 11.5 (text)*

^thm-73-4

*Stewart does not prove (a) ("it turns out that") and outlines a proof of (b) in Exercise 52; neither is proved in 451.*

> [!remark] Remark: Rearranging the Alternating Harmonic Series
> Stewart's Exercise 50 shows that
>
> $$
> 1 - \tfrac12 + \tfrac13 - \tfrac14 + \tfrac15 - \tfrac16 + \tfrac17 - \tfrac18 + \cdots = \ln 2 . \qquad (4)
> $$
>
> Multiplying by $\frac12$ ([[§70 Series#^thm-70-6|Theorem §70.6]]) gives $\frac12 - \frac14 + \frac16 - \frac18 + \cdots = \frac12 \ln 2$. Inserting zeros between the terms does not change the sum (each partial sum is repeated, but the limit is the same):
>
> $$
> 0 + \tfrac12 + 0 - \tfrac14 + 0 + \tfrac16 + 0 - \tfrac18 + \cdots = \tfrac12 \ln 2 . \qquad (5)
> $$
>
> Adding (4) and (5) term by term with [[§70 Series#^thm-70-6|Theorem §70.6]]:
>
> $$
> 1 + \tfrac13 - \tfrac12 + \tfrac15 + \tfrac17 - \tfrac14 + \cdots = \tfrac32 \ln 2 . \qquad (6)
> $$
>
> (The $n$th terms add as $1 + 0$, $-\frac12 + \frac12 = 0$, $\frac13 + 0$, $-\frac14 - \frac14 = -\frac12$, $\frac15 + 0$, $-\frac16 + \frac16 = 0$, $\frac17 + 0$, $-\frac18 - \frac18 = -\frac14$, …; dropping the zeros leaves (6).) The series (6) contains the same terms as (4), rearranged so that one negative term follows each pair of positive terms, but its sum is different.

^rem-73-3
