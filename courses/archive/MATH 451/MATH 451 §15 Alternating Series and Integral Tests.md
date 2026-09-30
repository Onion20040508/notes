---
course: "[[MATH 451]]"
section: 15
chapter: 2
tags: [real-analysis, math451]
---
← [[MATH 451 §14 Series]] · [[MATH 451]] · [[MATH 451 §16 Decimal Expansions of Real Numbers (Not Covered)]] →

## Alternating Series

> [!theorem] Theorem §15.1: Alternating Series Test
> If $a_1 \geq a_2 \geq a_3 \geq \cdots$ and $a_n \to 0$, then
>
> $$
> \sum_{n=1}^{\infty} (-1)^n a_n \quad \text{converges.}
> $$

^thm-15-1

> [!remark] Remark
> Note first that the hypotheses force $a_n \geq 0$ for all $n$: a decreasing sequence dominates its limit ($a_n \geq \lim_m a_m = 0$; if some $a_n < 0$, all later terms would be $\leq a_n < 0$, contradicting $a_n \to 0$). Note also that the condition $a_n \to 0$ is necessary — why? — because the terms $(-1)^n a_n$ of any convergent series must tend to $0$ (§14).

^rem-15-1

> [!proof]+ Proof
> We check the Cauchy criterion: for any $\varepsilon > 0$ we need $N$ such that for $m \geq n \geq N$,
>
> $$
> \left| \sum_{k=n}^{m} (-1)^k a_k \right| < \varepsilon.
> $$
>
> *Claim:* for all $m \geq n$,
>
> $$
> \left| \sum_{k=n}^{m} (-1)^k a_k \right| \leq a_n.
> $$
>
> This will be enough: given $\varepsilon$, choose $N$ with $a_n < \varepsilon$ for $n \geq N$ (possible since $a_n \to 0$).
>
> *Proof of the claim.* Factoring out the sign $(-1)^n$, the sum in question has absolute value
>
> $$
> \left| a_n - a_{n+1} + a_{n+2} - \cdots \pm a_m \right|,
> $$
>
> an alternating sum starting with $+a_n$. Group it in two ways. Grouping from the left in consecutive pairs,
>
> $$
> (a_n - a_{n+1}) + (a_{n+2} - a_{n+3}) + \cdots \geq 0,
> $$
>
> since each bracket is $\geq 0$ (decreasing) and a possible unpaired final term $+a_m$ is also $\geq 0$. Grouping instead with $a_n$ alone in front,
>
> $$
> a_n - (a_{n+1} - a_{n+2}) - (a_{n+3} - a_{n+4}) - \cdots \leq a_n,
> $$
>
> since each subtracted bracket is $\geq 0$ and a possible unpaired final term $-a_m$ is $\leq 0$. (The lecture checked the two parities on the examples $m = n+3$ and $m = n+2$; the displays above are the general case, which is the same.) So the alternating sum lies in $[0,\, a_n]$, proving the claim — and the theorem. (The book has a different, longer proof.)

^pf-15-1

> [!example] Example §15.1: The alternating harmonic series
> $a_n = \tfrac1n$ satisfies the conditions (decreasing, $\to 0$), so
>
> $$
> \sum_{n=1}^{\infty} (-1)^n \frac1n \quad \text{converges}
> $$
>
> — while, as promised in §14, it does not converge absolutely. Similarly $\sum (-1)^n \tfrac{1}{\sqrt n}$ converges (and not absolutely: $p = \tfrac12 \leq 1$).

^ex-15-1

> [!example] Example §15.2: Convergence forces terms to die faster
> Assume $(a_n)$ is decreasing and $\sum a_n$ converges. Then
>
> $$
> \lim_{n\to\infty} n a_n = 0
> $$
>
> — stronger than $\lim a_n = 0$.
>
> *Proof.* As above, decreasing $+$ summable forces $a_n \geq 0$. The series is Cauchy: for any $\varepsilon > 0$ there exists $N$ such that for $m \geq n \geq N$,
>
> $$
> a_{n+1} + \cdots + a_m < \varepsilon.
> $$
>
> Take $m = 2n$: since $(a_n)$ is decreasing, each of the $n$ terms $a_{n+1}, \ldots, a_{2n}$ is $\geq a_{2n}$, so
>
> $$
> \varepsilon > a_{n+1} + \cdots + a_{2n} \geq n\, a_{2n}, \qquad \text{hence} \qquad 2n\, a_{2n} < 2\varepsilon.
> $$
>
> So the even-indexed sequence $2n\, a_{2n} \to 0$. For the odd indices, $a_{2n+1} \leq a_{2n}$ gives
>
> $$
> (2n+1) a_{2n+1} \leq (2n+1) a_{2n} = 2n\, a_{2n} + a_{2n} \longrightarrow 0.
> $$
>
> Both subsequences of $(n a_n)$ covering all indices tend to $0$, hence $n a_n \to 0$.
>
> Read contrapositively, this re-proves the divergence of the harmonic series in one line (HW): $\tfrac1n$ is decreasing, yet $n \cdot \tfrac1n = 1 \not\to 0$.

^ex-15-2

> [!theorem] Proposition §15.2: Squares of a Nonnegative Convergent Series (HW)
> If $\sum a_n$ converges with $a_n \geq 0$ for all $n$, then $\sum a_n^2$ converges.

^prop-15-2

> [!proof]+ Proof
> Since $\sum a_n$ converges, $a_n \to 0$ (§14), so there is $N$ with $0 \leq a_n < 1$ for $n \geq N$; for such $n$, $a_n^2 \leq a_n$. The tail $\sum_{n \geq N} a_n^2$ then converges by comparison with the convergent tail $\sum_{n \geq N} a_n$, and prepending the finitely many terms $a_1^2, \ldots, a_{N-1}^2$ does not affect convergence.

^pf-15-2

> [!remark] Remark: Neither converse holds (HW)
> Both implications between $\sum a_n$ and $\sum a_n^2$ fail in general:
>
> 1. $\sum a_n^2$ convergent $\not\Rightarrow$ $\sum a_n$ convergent: take $a_n = \tfrac1n$ ($\sum \tfrac{1}{n^2}$ converges, harmonic diverges).
>
> 2. Without the sign condition, $\sum a_n$ convergent $\not\Rightarrow$ $\sum a_n^2$ convergent: take
>
>    $$
>    a_n = \frac{(-1)^n}{\sqrt n},
>    $$
>
>    convergent by the Alternating Series Theorem just proved ($\tfrac{1}{\sqrt n}$ decreasing to $0$) — but $a_n^2 = \tfrac1n$, and the squares form the divergent harmonic series. *Squaring destroys the sign cancellation that conditional convergence lives on.*

^rem-15-2

## The Integral Test

> [!theorem] Theorem §15.3: Integral Test
> Let $f: [1, +\infty) \to [0, +\infty)$ be a decreasing function. Then
>
> $$
> \sum_{n=1}^{\infty} f(n) \ \text{ converges} \qquad \Longleftrightarrow \qquad \int_1^{\infty} f(x)\, dx \ \text{ converges},
> $$
>
> and likewise the series diverges if and only if the integral diverges.

^thm-15-3

> [!proof]+ Proof
> The idea is to compare $\sum_{k=1}^n f(k)$ with $\int_1^n f(x)\,dx = \sum_{k=1}^{n-1} \int_k^{k+1} f(x)\,dx$. On each interval $[k, k+1]$, since $f$ is decreasing,
>
> $$
> f(k) \geq \int_k^{k+1} f(x)\, dx \geq f(k+1)
> $$
>
> (the integrand is trapped between its endpoint values on an interval of length $1$; e.g. $f(1) \geq \int_1^2 f \geq f(2)$). Summing over $k = 1, \ldots, n-1$ — note the shift in index on the right:
>
> $$
> \sum_{k=1}^{n-1} f(k) \ \geq\ \int_1^n f(x)\, dx \ \geq\ \sum_{k=2}^{n} f(k) = s_n - f(1),
> $$
>
> where $s_n = \sum_{k=1}^n f(k)$. Since $f \geq 0$, both $(s_n)$ and $\left( \int_1^n f \right)$ are increasing, so each converges if and only if it is bounded (§10). The left inequality shows: $(s_n)$ bounded $\implies$ the integrals bounded. The right inequality shows: integrals bounded $\implies$ $s_n \leq f(1) + \int_1^n f$ bounded. Hence the two convergences are equivalent.

^pf-15-3

![[m451-15-1.svg]]
*The integral test for a decreasing $f$ (drawn: $f(x) = \tfrac1x$): the upper staircase (red, height $f(n)$ on $[n, n+1]$) and the lower staircase (blue, height $f(n+1)$) squeeze the curve, so partial sums and partial integrals are bounded together. The figure is the proof.*

> [!example] Example §15.3: The p-series settled
> Let $f(x) = \tfrac{1}{x^p}$, $p > 0$ — decreasing and nonnegative on $[1,\infty)$. From calculus,
>
> $$
> \int_1^n \frac{dx}{x^p} =
> \begin{cases}
> \ \dfrac{n^{1-p} - 1}{1-p} & p \neq 1, \\[2mm]
> \ \log n & p = 1,
> \end{cases}
> $$
>
> which stays bounded as $n \to \infty$ if and only if $1 - p < 0$. So $\int_1^\infty \tfrac{dx}{x^p}$ converges if and only if $p > 1$, and by the integral test,
>
> $$
> \sum_{n=1}^\infty \frac{1}{n^p} \ \text{ converges} \quad \Longleftrightarrow \quad p > 1,
> $$
>
> completing the claim of §14 (and re-proving the divergence of the harmonic series systematically).

^ex-15-3

> [!remark] Remark
> Like the logarithm in §9, the integral $\int_1^\infty f(x)\,dx$ is borrowed from the future: integration will be defined rigorously only in Part III. The comparison inequality $f(k) \geq \int_k^{k+1} f \geq f(k+1)$ and the computation of $\int \tfrac{dx}{x^p}$ are familiar from calculus and will be fully justified then; the logic of the test itself — monotone partial sums, bounded iff convergent — is already rigorous.

^rem-15-3

> [!example] Example §15.4: The logarithmic ladder at the boundary (HW)
> How fine is the boundary $p = 1$? **First, comparison handles the easy cases.** Since $\log n \leq \sqrt n$ eventually (§9 scale), for large $n$
>
> $$
> \frac{1}{\sqrt n \log n} \geq \frac{1}{\sqrt n \cdot \sqrt n} = \frac1n, \qquad \frac{\log n}{n} \geq \frac1n,
> $$
>
> so $\sum \tfrac{1}{\sqrt n \log n}$ and $\sum \tfrac{\log n}{n}$ both diverge by comparison with the harmonic series — no integral needed.
>
> **The integral test is for the genuine boundary zone**, where the terms sit *between* $\tfrac1n$ and every $\tfrac{1}{n^p}$ ($p > 1$), so no p-series comparison can decide. There the substitution $u = \log x$ exhibits a self-similar ladder:
>
> $$
> \int \frac{dx}{x \log x} = \log\log x \to \infty, \qquad
> \int \frac{dx}{x \log x \, \log\log x} = \log\log\log x \to \infty, \qquad \ldots
> $$
>
> (each substitution turns a rung into the previous one), so
>
> $$
> \sum_{n\geq2} \frac{1}{n \log n}, \qquad \sum_{n\geq4} \frac{1}{n \log n \, \log\log n}, \qquad \ldots \quad \text{all diverge}
> $$
>
> — divergence can be made arbitrarily slow, echoing the growth-scale remark of §9. By contrast, one extra *power* rescues convergence immediately:
>
> $$
> \int_2^\infty \frac{\log x}{x^2}\,dx = \left[ -\frac{\log x}{x} - \frac1x \right]_2^\infty = \frac{\log 2 + 1}{2} < \infty
> $$
>
> (integration by parts; $\tfrac{\log x}{x} \to 0$ by the scale of §9), so $\sum \tfrac{\log n}{n^2}$ converges: a logarithm never overturns a power.

^ex-15-4
