---
course: "[[MATH 451]]"
section: 25
chapter: 4
tags: [real-analysis, math451]
---
← [[MATH 451 §24 Uniform Convergence]] · [[MATH 451]] · [[MATH 451 §26 Differentiation and Integration of Power Series]] →

## Exchanging Limits and Integrals

Return to the integral question. Our earlier counterexample $(n+1)x^n$ had a flaw for the refined question: $f_n$ was not continuous at $x = 1$. Could continuity of all $f_n$ *and* of $f$ rescue $\int f_n \to \int f$ under pointwise convergence? Still no:

> [!example] Example §25.1: The escaping triangle
> Define $f_n: [0,1] \to \mathbb{R}$ with a thin tall triangular graph — base $[0, \tfrac2n]$, height $n$, zero elsewhere:
>
> $$
> f_n(x) = n^2 x \ \left(0 \leq x \leq \tfrac1n\right), \qquad
> f_n(x) = n^2\left(\tfrac2n - x\right) \ \left(\tfrac1n \leq x \leq \tfrac2n\right), \qquad
> f_n(x) = 0 \ \text{ otherwise}.
> $$
>
> Each $f_n$ is continuous, and by the area formula for triangles,
>
> $$
> \int_0^1 f_n(x)\,dx = \frac12 \cdot \frac2n \cdot n = 1.
> $$
>
> But $f(x) = \lim f_n(x) = 0$ for *all* $x \in [0,1]$: for $x > 0$, once $\tfrac2n < x$ the triangle has slid past $x$ and $f_n(x) = 0$; and $f_n(0) = 0$ always. The triangle becomes skinnier and skinnier and escapes. So $\int_0^1 f_n = 1 \not\to 0 = \int_0^1 f$, with all continuity conditions satisfied.

^ex-25-1

![[m451-25-1.svg]]
*The escaping triangle for $n = 2, 4, 8$: base $[0, \tfrac2n]$ shrinks, peak $n$ grows, area stays exactly $1$. Pointwise the limit is $0$ everywhere, yet the integrals refuse to follow.*

> [!theorem] Theorem §25.1: Uniform Convergence Allows Exchanging Limit and Integral
> If $f_n \to f$ uniformly on $[a,b]$ (with each $f_n$ continuous, so that $f$ is continuous and all integrals are defined), then
>
> $$
> \lim_{n\to\infty} \int_a^b f_n(x)\,dx = \int_a^b f(x)\,dx = \int_a^b \lim_{n\to\infty} f_n(x)\,dx
> $$
>
> — the limit and the integration can be exchanged. This is one of the problems that motivated uniform convergence.

^thm-25-1

> [!proof]+ Proof
> Given $\varepsilon > 0$, uniform convergence provides $N$ such that for all $n \geq N$ and all $x \in [a,b]$,
>
> $$
> |f_n(x) - f(x)| < \frac{\varepsilon}{b-a}.
> $$
>
> Therefore, using the basic bounds $\left|\int g\right| \leq \int |g|$ and monotonicity of the integral (familiar from calculus; rigorous in Part III),
>
> $$
> \left| \int_a^b f_n - \int_a^b f \right| = \left| \int_a^b (f_n - f) \right| \leq \int_a^b |f_n - f| \leq \int_a^b \frac{\varepsilon}{b-a}\,dx = \varepsilon.
> $$

^pf-25-1

> [!example] Example §25.2: Computing a limit of integrals
> Compute $\displaystyle\lim_{n\to\infty} \int_0^1 \frac{n + \cos x}{2n + \sin^2 x}\,dx$.
>
> Computing $\int_0^1 f_n$ directly is difficult — so try exchanging: divide through by $n$,
>
> $$
> f_n(x) = \frac{1 + \tfrac{\cos x}{n}}{2 + \tfrac{\sin^2 x}{n}} \longrightarrow \frac12 \qquad \text{for every } x.
> $$
>
> To justify the exchange, show the convergence is uniform:
>
> $$
> \left| f_n(x) - \frac12 \right|
> = \frac{\left| 2\left(1 + \tfrac{\cos x}{n}\right) - \left(2 + \tfrac{\sin^2 x}{n}\right) \right|}{2\left(2 + \tfrac{\sin^2 x}{n}\right)}
> = \frac{\left| \tfrac{2\cos x}{n} - \tfrac{\sin^2 x}{n} \right|}{2\left(2 + \tfrac{\sin^2 x}{n}\right)}
> \leq \frac{\tfrac2n + \tfrac1n}{4} = \frac{3}{4n},
> $$
>
> a bound independent of $x$ tending to $0$. By the supremum criterion the convergence is uniform, and by the theorem,
>
> $$
> \lim_{n\to\infty} \int_0^1 f_n(x)\,dx = \int_0^1 \frac12\,dx = \frac12. \tag*{$\blacksquare$}
> $$

^ex-25-2

## Series of Functions and the Weierstrass M-Test

Now we return toward power series — via general series of functions.

> [!definition] Definition §25.1: Convergence of a Series of Functions
> Let $g_k$ be functions defined on a common set $S \subseteq \mathbb{R}$, with partial sums $s_n(x) = \sum_{k=1}^n g_k(x)$. If $s_n(x) \to g(x)$ pointwise on $S$, we say the series $\sum_{k=1}^\infty g_k(x)$ **converges pointwise** and write $g(x) = \sum_{k=1}^\infty g_k(x)$. If $s_n \to g$ uniformly on $S$, we say the series **converges uniformly**.

^def-25-1

> [!theorem] Theorem §25.2: Continuity of Uniformly Convergent Series
> If each $g_k$ is continuous on $S$ and $\sum_{k=1}^\infty g_k$ converges uniformly on $S$, then the sum $\sum_{k=1}^\infty g_k(x)$ is a continuous function on $S$.

^thm-25-2

> [!proof]+ Proof
> Each partial sum $s_n$ is continuous (finite sum of continuous functions, §17), and $s_n \to g$ uniformly; apply the theorem of §24.

^pf-25-2

> [!theorem] Theorem §25.3: Weierstrass M-Test
> Let $(M_k)$ be a sequence of positive numbers with $\sum_{k=1}^\infty M_k < +\infty$. If $|g_k(x)| \leq M_k$ for all $x \in S$ and all $k$, then $\sum_k g_k(x)$ converges uniformly on $S$.

^thm-25-3

> [!proof]+ Proof
> First, the series converges pointwise, absolutely: for each $x$, $\sum |g_k(x)| \leq \sum M_k < \infty$ (comparison test, §14); call the sum $g(x)$. Now estimate the tail uniformly:
>
> $$
> \left| s_n(x) - g(x) \right| = \left| \sum_{k=n+1}^{\infty} g_k(x) \right| \leq \sum_{k=n+1}^\infty |g_k(x)| \leq \sum_{k=n+1}^\infty M_k,
> $$
>
> a bound independent of $x$. Since $\sum M_k$ converges, its tails $\sum_{k > n} M_k \to 0$ as $n \to \infty$ (Cauchy criterion). By the supremum criterion, $s_n \to g$ uniformly.

^pf-25-3

> [!example] Example §25.3: Three applications of the M-test
> **(1)** $\displaystyle\sum_{n=1}^\infty \frac{\cos nx}{n^2}$ converges uniformly on $\mathbb{R}$ — take $M_k = \tfrac{1}{k^2}$ — and hence defines a continuous function on $\mathbb{R}$.
>
> **(2)** $\sum_{n=0}^\infty x^n$ converges uniformly on $[-a, a]$ for every $a < 1$: take $M_k = a^k$, $\sum a^k < \infty$. But it does *not* converge uniformly on all of $(-1,1)$, as proved at the start of §24. Uniformity can hold on every smaller closed subinterval yet fail on the open interval itself.
>
> **(3)** The power series $\displaystyle\sum_{n=1}^\infty \frac{x^n}{n^2 2^n}$ has interval of convergence $[-2,2]$ and converges uniformly there — hence its sum is continuous on $[-2,2]$. Steps: (i) $\beta = \limsup \left(\tfrac{1}{n^2 2^n}\right)^{1/n} = \tfrac12$, so $R = 2$; (ii) at the endpoints $x = \pm2$ the series is $\sum \tfrac{(\pm1)^n}{n^2}$, convergent; (iii) M-test on $[-2,2]$ with
>
> $$
> \left| \frac{x^n}{n^2 2^n} \right| \leq \frac{2^n}{n^2 2^n} = \frac{1}{n^2} = M_n. \tag*{$\blacksquare$}
> $$

^ex-25-3

> [!example] Example §25.4: When the M-test has no chance
> Show $\displaystyle\sum_{n=1}^\infty \frac{x^n}{1+x^n}$ converges pointwise on $(0,1)$. Does it converge uniformly there?
>
> *Pointwise:* for $x \in (0,1)$, $0 < \tfrac{x^n}{1+x^n} \leq x^n$, and $\sum x^n$ converges (geometric); apply comparison.
>
> *Not uniform.* First a small general fact: if $\sum g_k$ converges uniformly on $S$, then the terms tend to $0$ *uniformly*: $g_n = s_n - s_{n-1}$, and both $s_n, s_{n-1} \to g$ uniformly, so $\sup_S |g_n| \to 0$. Here, however,
>
> $$
> \sup_{x \in (0,1)} \frac{x^n}{1+x^n} \geq \lim_{x \to 1^-} \frac{x^n}{1+x^n} = \frac12 \qquad \text{for every } n,
> $$
>
> so the terms do not tend to $0$ uniformly, and the series cannot converge uniformly on $(0,1)$.

^ex-25-4
