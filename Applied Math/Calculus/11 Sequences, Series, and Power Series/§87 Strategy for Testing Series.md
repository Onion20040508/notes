---
type: section
subject: "[[Calculus]]"
chapter: 11
section: 87
stewart: "11.7"
aliases: ["Stewart 11.7"]
tags: [calculus]
---
← [[§86 The Ratio and Root Tests]] · ↑ [[· 11 Sequences, Series, and Power Series]] · [[§88 Power Series]] →

*Stewart, Section 11.7.*

With the tests of [[§82 Series|§82]]–[[§86 The Ratio and Root Tests|§86]] in hand, the problem is to decide which test to use on which series. As with integration ([[§55 Strategy for Integration#^rem-55-1|the strategy for integration in §55]]), there are no hard and fast rules, and applying the tests in a fixed order until one works wastes effort. The strategy is to classify the series by its *form*, which usually points to the right test at once. This section collects that advice and works through one series of each kind.

## The Strategy

> [!remark] Remark: Method — Testing a Series
> Classify the series according to its form.
> 1. **Test for Divergence.** If you can see that $\lim_{n \to \infty} a_n$ may be different from $0$, apply the Test for Divergence ([[§82 Series#^cor-82-5|Corollary §82.5]]).
> 2. **$p$-series.** If the series has the form $\sum 1/n^p$, it is a $p$-series: convergent if $p > 1$ and divergent if $p \le 1$ ([[§83 The Integral Test and Estimates of Sums#^thm-83-2|Theorem §83.2]]).
> 3. **Geometric series.** If the series has the form $\sum a r^{n-1}$ or $\sum a r^n$, it is geometric: convergent if $|r| < 1$ and divergent if $|r| \ge 1$ ([[§82 Series#^thm-82-1|Theorem §82.1]]). Some algebraic manipulation may be required to bring the series into this form.
> 4. **Comparison Tests.** If the series has a form similar to a $p$-series or a geometric series, consider one of the comparison tests ([[§84 The Comparison Tests#^thm-84-1|Theorem §84.1]], [[§84 The Comparison Tests#^thm-84-2|Theorem §84.2]]). In particular, if $a_n$ is a rational or algebraic function of $n$ (involving roots of polynomials), compare with a $p$-series, choosing $p$ by keeping only the highest powers of $n$ in numerator and denominator. The comparison tests apply only to series with positive terms; if $\sum a_n$ has some negative terms, apply a comparison test to $\sum |a_n|$ and test for [[§85 Alternating Series and Absolute Convergence#^def-85-2|absolute convergence]].
> 5. **Alternating Series Test.** If the series has the form $\sum (-1)^{n-1} b_n$ or $\sum (-1)^n b_n$, the Alternating Series Test ([[§85 Alternating Series and Absolute Convergence#^thm-85-1|Theorem §85.1]]) is an obvious possibility. If $\sum b_n$ converges, the series is absolutely convergent and therefore convergent.
> 6. **Ratio Test.** Series that involve factorials or other products (including a constant raised to the $n$th power) are often conveniently tested with the Ratio Test ([[§86 The Ratio and Root Tests#^thm-86-1|Theorem §86.1]]). Since $|a_{n+1}/a_n| \to 1$ for all $p$-series, and therefore for all rational or algebraic functions of $n$, the Ratio Test should not be used for such series.
> 7. **Root Test.** If $a_n$ has the form $(b_n)^n$, the Root Test ([[§86 The Ratio and Root Tests#^thm-86-2|Theorem §86.2]]) may be useful.
> 8. **Integral Test.** If $a_n = f(n)$, where $\int_1^{\infty} f(x)\,dx$ is easily evaluated, the Integral Test ([[§83 The Integral Test and Estimates of Sums#^thm-83-1|Theorem §83.1]]) is effective, provided $f$ is positive, continuous and (ultimately) decreasing.
>
> *Stewart: 11.7 (text)*

^rem-87-1

## Examples

Stewart only names the test for each of the following series; here each is carried out.

> [!example] Example §87.1: Divergence Test and Limit Comparison
> **(a)** $\displaystyle\sum_{n=1}^{\infty} \frac{n - 1}{2n + 1}$. Since $a_n = \dfrac{1 - 1/n}{2 + 1/n} \to \dfrac12 \ne 0$, the series diverges by the Test for Divergence.
>
> **(b)** $\displaystyle\sum_{n=1}^{\infty} \frac{\sqrt{n^3 + 1}}{3n^3 + 4n^2 + 2}$. Here $a_n$ is an algebraic function of $n$, so compare with a $p$-series. Keeping the highest powers,
>
> $$
> b_n = \frac{\sqrt{n^3}}{3n^3} = \frac{n^{3/2}}{3n^3} = \frac{1}{3n^{3/2}} .
> $$
>
> Then, dividing numerator and denominator by $n^3$,
>
> $$
> \frac{a_n}{b_n} = \frac{3n^{3/2} \sqrt{n^3 + 1}}{3n^3 + 4n^2 + 2} = \frac{3\sqrt{n^3 (n^3 + 1)}}{3n^3 + 4n^2 + 2} = \frac{3\sqrt{1 + 1/n^3}}{3 + 4/n + 2/n^3} \to \frac{3}{3} = 1 > 0 .
> $$
>
> $\sum b_n = \frac13 \sum 1/n^{3/2}$ converges ($p = \frac32 > 1$), so the given series converges by the Limit Comparison Test.
>
> *Stewart: Examples 11.7.1 and 11.7.2*

^ex-87-1

> [!example] Example §87.2: An Easy Integral
> $\displaystyle\sum_{n=1}^{\infty} n e^{-n^2}$.
>
> **Integral Test.** $f(x) = x e^{-x^2}$ is positive and continuous on $[1, \infty)$, and $f'(x) = e^{-x^2} - 2x^2 e^{-x^2} = e^{-x^2} (1 - 2x^2) < 0$ for $x \ge 1$, so $f$ is decreasing. With $u = x^2$,
>
> $$
> \int_1^{\infty} x e^{-x^2}\,dx = \lim_{t \to \infty} \left[ -\tfrac12 e^{-x^2} \right]_1^t = \lim_{t \to \infty} \left( \tfrac{1}{2e} - \tfrac12 e^{-t^2} \right) = \frac{1}{2e} .
> $$
>
> The integral converges, so the series converges.
>
> **Ratio Test** (also works).
>
> $$
> \frac{a_{n+1}}{a_n} = \frac{(n+1) e^{-(n+1)^2}}{n e^{-n^2}} = \left( 1 + \frac1n \right) e^{n^2 - (n+1)^2} = \left( 1 + \frac1n \right) e^{-2n - 1} \to 1 \cdot 0 = 0 < 1 .
> $$
>
> *Stewart: Example 11.7.3*

^ex-87-2

> [!example] Example §87.3: Alternating, and Absolutely Convergent
> $\displaystyle\sum_{n=1}^{\infty} (-1)^n \frac{n^2}{n^4 + 1}$.
>
> **Alternating Series Test.** $b_n = \dfrac{n^2}{n^4 + 1} = \dfrac{1/n^2}{1 + 1/n^4} \to 0$. For $f(x) = x^2/(x^4 + 1)$,
>
> $$
> f'(x) = \frac{2x(x^4 + 1) - x^2 \cdot 4x^3}{(x^4 + 1)^2} = \frac{2x(1 - x^4)}{(x^4 + 1)^2} < 0 \qquad \text{for } x > 1 ,
> $$
>
> so $b_{n+1} < b_n$ for $n \ge 1$ ($f$ is decreasing on $[1, \infty)$). The series converges.
>
> **Absolute convergence.** Better: $|a_n| = \dfrac{n^2}{n^4 + 1} < \dfrac{n^2}{n^4} = \dfrac{1}{n^2}$, and $\sum 1/n^2$ converges, so $\sum |a_n|$ converges by the Direct Comparison Test. The series converges absolutely, hence converges.
>
> *Stewart: Example 11.7.4*

^ex-87-3

> [!example] Example §87.4: A Factorial
> $\displaystyle\sum_{k=1}^{\infty} \frac{2^k}{k!}$.
>
> The series involves $k!$, so use the Ratio Test:
>
> $$
> \frac{a_{k+1}}{a_k} = \frac{2^{k+1}}{(k+1)!} \cdot \frac{k!}{2^k} = \frac{2}{k+1} \to 0 < 1 .
> $$
>
> The series converges. (Its sum is $e^2 - 1$, by the Maclaurin series of $e^x$, [[§90 Taylor and Maclaurin Series#^thm-90-6|Theorem §90.6]].)
>
> *Stewart: Example 11.7.5*

^ex-87-4

> [!example] Example §87.5: Close to a Geometric Series
> $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2 + 3^n}$.
>
> The series is closely related to the geometric series $\sum 1/3^n$. **Direct Comparison:**
>
> $$
> \frac{1}{2 + 3^n} < \frac{1}{3^n} = \left( \frac13 \right)^n ,
> $$
>
> and $\sum (\frac13)^n$ is geometric with $|r| = \frac13 < 1$, so it converges, and so does the given series. **Limit Comparison** works too: $\dfrac{1/(2 + 3^n)}{1/3^n} = \dfrac{3^n}{2 + 3^n} = \dfrac{1}{2/3^n + 1} \to 1 > 0$.
>
> *Stewart: Example 11.7.6*

^ex-87-5
