---
type: section
subject: "[[Single Variable Analysis]]"
section: 24
chapter: 4
tags: [real-analysis, math451]
---
← [[§23 Power Series]] · ↑ [[· 4 Sequences and Series of Functions]] · [[§25 More on Uniform Convergence]] →

The problem with the examples above: convergence $f_n(x) \to f(x)$ *at every point separately* is not sufficient. We need something stronger.

> [!definition] Definition §24.1: Pointwise Convergence
> Let $S \subseteq \mathbb{R}$ and $f_n$ functions defined on $S$. The sequence $(f_n)$ **converges to $f$ pointwise on $S$** if for every $x \in S$, $f_n(x) \to f(x)$. In $(\varepsilon, N)$ terms: for every $x \in S$ and every $\varepsilon > 0$, there exists $N = N(x)$ such that $|f_n(x) - f(x)| < \varepsilon$ for $n \geq N(x)$ — the integer $N(x)$ *depends on $x$*. All the examples above are pointwise convergence.

^def-24-1

> [!remark]- Connections
> - 551 weakens it to convergence outside a null set (almost everywhere convergence): [[§12 Measurable Functions#^def-12-8|551 Def. §12.8]].

> [!definition] Definition §24.2: Uniform Convergence
> $(f_n)$ **converges uniformly to $f$ on $S$** if for every $\varepsilon > 0$ there exists $N$ such that for all $n \geq N$ *and all $x \in S$*,
>
> $$
> |f_n(x) - f(x)| < \varepsilon.
> $$
>
> The difference: $N$ is independent of $x$ — one $N$ works for all points. (Compare the passage from continuity to *uniform* continuity in §19: the same quantifier move.)

^def-24-2

![[m451-24-1.svg]]
*The $\varepsilon$-tube around the limit $f \equiv 0$: uniform convergence means the whole graph of $f_n$ eventually enters the tube. The blue curve is inside; the peak of $n x^n(1-x)$ (height $\to \tfrac1e$ at $x = \tfrac{n}{n+1}$) escapes for every $n$ — the picture behind “Locating the worst point” below.*

> [!remark]- Connections
> - Restated in 551 as [[§12 Measurable Functions#^def-12-9|551 Def. §12.9]]; on a set of finite measure, a.e. convergence is uniform off a set of arbitrarily small measure by [[§13 Egorov's and Lusin's Theorems#^thm-13-1|551 Thm. §13.1]] (Egorov).
> - Computational version: [[§9 Uniform Convergence#^def-9-1|341 Def. §9.1]] (pointwise versus uniform convergence, with worked examples for Fourier series).
> - Computational version: [[§69★ Absolute and Uniform Convergence of Power Series#^def-69-2|342 Def. §69.2]] (uniform convergence of complex series, in remainder form).

## Examples and Non-Examples

> [!example] Example §24.1: The Geometric Series Converges Pointwise but Not Uniformly
> Let $f_n(x) = \sum_{k=0}^n x^k = \dfrac{1 - x^{n+1}}{1-x}$ on $S = (-1,1)$. Pointwise, $f_n(x) \to f(x) = \tfrac{1}{1-x}$ for every $x \in S$. But the convergence is *not uniform*.
>
> *Proof.* Suppose it were. Then for every $\varepsilon > 0$ there is $N$ such that for all $n \geq N$ and all $x \in (-1,1)$,
>
> $$
> |f_n(x) - f(x)| = \left| \frac{x^{n+1}}{1-x} \right| < \varepsilon, \qquad \text{i.e.} \qquad |x|^{n+1} < \varepsilon\,|1-x|.
> $$
>
> Fix any $n \geq N$ and let $x \to 1^-$: the left side tends to $1$, the right side to $0$, giving $1 \leq 0$ — impossible.
>
> The reason: as $x$ gets close to $1$, the pointwise $N(x)$ blows up, so no uniform $N$ exists.

^ex-24-1

![[m451-24-2.svg]]
*The partial sums peel off near $x = 1$: each $f_n$ eventually flattens (it is a polynomial, bounded on $[0,1]$) while $\tfrac{1}{1-x}$ climbs without bound, so $\sup_x |f_n - f|$ is infinite for every $n$ — pointwise convergence at each fixed $x$, no uniformity.*

> [!example] Example §24.2: The Power Sequence on the Closed Interval
> $f_n(x) = x^n$ on $[0,1]$ converges pointwise to the discontinuous $f$ computed above, but not uniformly. If it did: take $\varepsilon = \tfrac12$; then for $n \geq N$ and all $x \in [0,1)$, $|x^n| < \tfrac12$. Fix $n$ and let $x \to 1^-$: $x^n \to 1$, giving $1 \leq \tfrac12$. Impossible.

^ex-24-2

> [!remark]- Connections
> - Same sequence in 551, where it converges uniformly on every $[0, 1-\delta]$, illustrating Egorov's theorem: [[§13 Egorov's and Lusin's Theorems#^ex-13-1|551 Ex. §13.1]].
> - Computational version: [[§9 Uniform Convergence#^ex-9-1|341 Ex. §9.1]] (continuous functions converging pointwise, not uniformly, to a step).

> [!example] Example §24.3: A Uniform Example
> $f_n(x) = \tfrac1n \sin x$ converges uniformly to $f \equiv 0$ on $\mathbb{R}$: given $\varepsilon > 0$, take $N > \tfrac1\varepsilon$; then for all $n \geq N$ and *all* $x \in \mathbb{R}$,
>
> $$
> |f_n(x) - 0| = \left| \frac{\sin x}{n} \right| \leq \frac1n \leq \frac1N < \varepsilon. \tag*{$\blacksquare$}
> $$

^ex-24-3

> [!example] Example §24.4: A Two-Plateau Limit
> Let $f_n(x) = \dfrac{x^n}{n + x^n}$ on $[0, +\infty)$. *Pointwise limit:* for $0 \leq x \leq 1$, $x^n \leq 1$, so for $n \geq 2$, $|f_n(x)| \leq \tfrac1n \to 0$; for $x > 1$, $x^n \to \infty$ faster than $n$ ($n/x^n \to 0$, growth scale), so
>
> $$
> f_n(x) = \frac{1}{n/x^n + 1} \longrightarrow \frac{1}{0+1} = 1.
> $$
>
> So $f = 0$ on $[0,1]$ and $f = 1$ on $(1,+\infty)$. *Not uniform:* the trouble point is $x = 1$, where $f$ jumps — a hint. Suppose uniform: for $\varepsilon = \tfrac12$ there is $N$ with, for all $n \geq N$ and all $x > 1$,
>
> $$
> |f_n(x) - 1| = \frac{n}{n + x^n} < \frac12.
> $$
>
> Fix $n \geq N$ and let $x \to 1^+$: the left side tends to $\tfrac{n}{n+1} \geq \tfrac12$ — contradiction.

^ex-24-4

> [!example] Example §24.5: Shifted Parabolas Converge Uniformly
> $f_n(x) = \left(x - \tfrac1n\right)^2$ on $[0,1]$: pointwise limit $f(x) = x^2$, and the convergence is uniform — bound the difference independently of $x$:
>
> $$
> |f_n(x) - f(x)| = \left| -\frac{2x}{n} + \frac{1}{n^2} \right| \leq \frac{2x}{n} + \frac{1}{n^2} \leq \frac2n + \frac{1}{n^2} \longrightarrow 0. \tag*{$\blacksquare$}
> $$

^ex-24-5

> [!example] Example §24.6: Locating the Worst Point
> $f_n(x) = n x^n (1-x)$ on $[0,1]$: pointwise, $f \equiv 0$ (for $x \in [0,1)$, $nx^n \to 0$ by the growth scale; $f_n(0) = f_n(1) = 0$). But the convergence is *not* uniform — harder to prove. We want $\varepsilon_0$ and points $x_n$ (depending on $n$!) with $f_n(x_n) \geq \varepsilon_0$. Which points? *The maximum point of $f_n$ — the worst case.* Calculus locates it: $f_n'(x) = n^2 x^{n-1} - n(n+1)x^n = 0$ gives $x_n = \tfrac{n}{n+1}$. (The derivative is only a *search tool*; the proof below needs nothing but the evaluation.) Compute:
>
> $$
> f_n\left(\frac{n}{n+1}\right) = n \left(\frac{n}{n+1}\right)^n \frac{1}{n+1}
> = \frac{n}{n+1} \left(\frac{1}{1 + \tfrac1n}\right)^n
> \longrightarrow 1 \cdot \frac1e = \frac1e,
> $$
>
> using the standard limit $\left(1 + \tfrac1n\right)^n \to e$ (provable with monotone convergence; accepted here). So taking $\varepsilon_0 = \tfrac{1}{2e}$: for all large $n$,
>
> $$
> \left| f_n\left( \tfrac{n}{n+1} \right) - 0 \right| \geq \varepsilon_0,
> $$
>
> which rules out uniform convergence.

^ex-24-6

## The Supremum Criterion

The last example generalizes:

> [!theorem] Theorem §24.1: Supremum Criterion for Uniform Convergence
> $f_n \to f$ uniformly on $S$ if and only if
>
> $$
> \lim_{n\to\infty} M_n = 0, \qquad \text{where} \quad M_n = \sup\{ |f_n(x) - f(x)| \mid x \in S \}.
> $$

^thm-24-1

> [!proof]+ Proof
> ($\Leftarrow$) If $M_n \to 0$: for every $\varepsilon > 0$ there is $N$ with $M_n < \varepsilon$ for $n \geq N$; then for all $x \in S$, $|f_n(x) - f(x)| \leq M_n < \varepsilon$.
>
> ($\Rightarrow$) If $f_n \to f$ uniformly: for every $\varepsilon > 0$ there is $N$ such that $|f_n(x) - f(x)| < \varepsilon$ for all $n \geq N$ and all $x \in S$; taking the supremum over $x$, $M_n \leq \varepsilon$ for $n \geq N$. Hence $M_n \to 0$.

^pf-24-1

*Uses:* [[§24 Uniform Convergence#^def-24-2|Def. §24.2]]

> [!remark]- Connections
> - Computational version: [[§9 Uniform Convergence#^def-9-2|341 Def. §9.2]] (uniform convergence of a Fourier series defined by this criterion: the maximum deviation $\delta_N$ tends to 0).

The two proof strategies, summarized: to prove uniform convergence, bound $|f_n(x) - f(x)|$ *independently of $x$* by something $\to 0$; to disprove it, find points $x_n$ (usually depending on $n$) where $|f_n(x_n) - f(x_n)|$ stays above a fixed $\varepsilon_0$.

## Uniform Limits of Continuous Functions

Now we reap the applications.

> [!theorem] Theorem §24.2: Uniform Limits Preserve Continuity
> If every $f_n$ is continuous on $S$ and $f_n \to f$ *uniformly* on $S$, then $f$ is continuous on $S$.

^thm-24-2

> [!proof]+ Proof
> Fix $x_0 \in S$ and $\varepsilon > 0$; we need $\delta > 0$ such that $|x - x_0| < \delta$ (with $x \in S$) implies $|f(x) - f(x_0)| < \varepsilon$. *Idea: approximate $f$ by one continuous $f_N$.*
>
> By uniform convergence, there exists $N$ such that for all $x \in S$,
>
> $$
> |f_N(x) - f(x)| < \frac\varepsilon3.
> $$
>
> Since $f_N$ is continuous at $x_0$, there exists $\delta > 0$ such that $|x - x_0| < \delta$, $x \in S$, implies
>
> $$
> |f_N(x) - f_N(x_0)| < \frac\varepsilon3.
> $$
>
> Now, for such $x$, insert $f_N$ twice:
>
> $$
> |f(x) - f(x_0)| \leq \underbrace{|f(x) - f_N(x)|}_{< \varepsilon/3} + \underbrace{|f_N(x) - f_N(x_0)|}_{< \varepsilon/3} + \underbrace{|f_N(x_0) - f(x_0)|}_{< \varepsilon/3} < \varepsilon.
> $$
>
> The first and third bounds come from uniform convergence, the middle from continuity of $f_N$ — exactly the idea of approximation. So $f$ is continuous at $x_0$.

^pf-24-2

*Uses:* [[§24 Uniform Convergence#^def-24-2|Def. §24.2]], [[§17 Continuous Functions#^thm-17-1|§17.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

![[m451-24-3.svg]]
*The $\tfrac\varepsilon3$ argument. Uniform convergence puts the graph of one $f_N$ (blue) inside the band $f \pm \tfrac\varepsilon3$ (gray) at every point at once — in particular at $x_0$ and at $x$ (red gaps). Continuity of $f_N$ bounds the middle step from $f_N(x_0)$ to $f_N(x)$ (orange). Chaining the three steps gets from $f(x_0)$ to $f(x)$ with total change $< \varepsilon$.*

> [!remark]- Connections
> - Special case for complex power series: [[§70★ Continuity of Sums of Power Series#^thm-70-1|342 Thm. §70.1]] (the sum of a power series is continuous inside its circle of convergence).
> - Restated in 551 for functions on a measurable set, where it is a step in the proof of Lusin's theorem: [[§12 Measurable Functions#^thm-12-16|551 Thm. §12.16]], [[§13 Egorov's and Lusin's Theorems#^thm-13-3|551 Thm. §13.3]].
> - Used in ODEs: the Picard iterates for $y' = f(t, y)$ converge uniformly, so their limit is continuous, a step in the existence proof of [[§11 The Existence and Uniqueness Theorem#^thm-11-7|331 Thm. §11.7]].

> [!remark] Remark
> This retroactively explains several examples: $x^n$ on $[0,1]$ and $\tfrac{x^n}{n+x^n}$ on $[0,\infty)$ could not converge uniformly, because their limit functions are discontinuous while every $f_n$ is continuous. The contrapositive of the theorem is a quick non-uniformity test.

^rem-24-1

Continuity is not the only property that survives passage to a uniform limit:

> [!theorem] Proposition §24.3: Uniform Limits Preserve Boundedness (HW)
> If every $f_n$ is bounded on $S$ and $f_n \to f$ uniformly on $S$, then $f$ is bounded on $S$.

^prop-24-3

> [!proof]+ Proof
> One term of the sequence suffices. By uniform convergence (with tolerance $1$, say) there is $N$ such that $|f_N(x) - f(x)| < 1$ for *all* $x \in S$; and $f_N$ is bounded, say $|f_N| \leq M_N$ on $S$. Then for every $x \in S$,
>
> $$
> |f(x)| \leq |f(x) - f_N(x)| + |f_N(x)| < 1 + M_N,
> $$
>
> a bound independent of $x$.

^pf-24-3

*Uses:* [[§24 Uniform Convergence#^def-24-2|Def. §24.2]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

> [!remark] Remark
> This is the function-space analogue of “convergent sequences of numbers are bounded” (§9) — there too, one tail estimate plus one fixed term produced the bound. Uniformity is essential: on $(0,1]$ the truncations $f_n(x) = \min\left\{ n, \tfrac1x \right\}$ are each bounded (by $n$) and converge *pointwise* to $\tfrac1x$, which is unbounded; the convergence cannot be uniform, and the proposition is precisely what forbids it.

^rem-24-2

> [!example] Example §24.7: Products Do Not Preserve Uniform Convergence (HW)
> Sums do, trivially: if $f_n \to f$ and $g_n \to g$ uniformly on $S$, then $|(f_n + g_n) - (f+g)| \leq |f_n - f| + |g_n - g|$ gives $f_n + g_n \to f + g$ uniformly. But *products fail*. Take on $\mathbb{R}$:
>
> $$
> f_n(x) = x, \qquad g_n(x) = \frac1n,
> $$
>
> so $f_n \to f(x) = x$ uniformly (the differences are $0$) and $g_n \to g \equiv 0$ uniformly ($|g_n - g| = \tfrac1n$, independent of $x$). Yet $(f_n g_n)(x) = \tfrac{x}{n}$ does not converge uniformly to $fg \equiv 0$: for $\varepsilon_0 = 1$ and any $n$, the point $x = n$ gives $\left|\tfrac{x}{n}\right| = 1$. The culprit is the *unbounded* factor $x$, which amplifies the innocent error $\tfrac1n$ without limit; if $f$, $g$ and all $f_n$, $g_n$ are bounded, the product does converge uniformly (and the proposition above says the limits' boundedness comes for free from the $f_n$'s).

^ex-24-7
