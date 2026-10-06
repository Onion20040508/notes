---
type: section
subject: "[[Single Variable Analysis]]"
section: "9a"
aliases: ["Ross 9 (cont.)"]
chapter: 2
tags: [real-analysis, math451]
---
← [[§9 Limit Theorems for Sequences]] · ↑ [[· 2 Sequences]] · [[§10 Monotone Sequences and Cauchy Sequences]] →

Earlier we introduced the extended real numbers $[-\infty, +\infty]$ ([[§5 The Symbols +∞, −∞|§5]]). We now define the related notions $x_n \to +\infty$ and $x_n \to -\infty$. Compare two examples: $s_n = n$ and $t_n = (-1)^n n$. Both are divergent (both are unbounded — [[§9 Limit Theorems for Sequences#^thm-9-1|Theorem §9.1]]). But there is a difference: $s_n$ still has *some* convergence behavior — it goes steadily up — while $t_n$ jumps between $\pm\infty$ directions.

## Divergence to $\pm\infty$

> [!definition] Definition §9.1: Divergence to Infinity
> We say $s_n$ **diverges to $+\infty$**, written $s_n \to +\infty$ or $\lim_{n\to\infty} s_n = +\infty$, if for any positive number $M$ (usually large), there exists $N$ such that for all $n > N$,
>
> $$
> s_n > M.
> $$
>
> Similarly, $s_n \to -\infty$ if for any $M$ there exists $N$ such that $s_n < -M$ for all $n > N$.

^def-9-1

> [!remark]- Connections
> - Computational version: [[§69 Sequences#^def-69-4|Calc Def. §69.4]] (with worked examples).

> [!example] Example §9.8: Basic Examples
> $s_n = n^2 \to +\infty$ and $s_n = 3^{n-1} \to +\infty$ (given $M$, take $N > \sqrt{M}$, resp. use $3^{n-1} \geq n$ for $n \geq 1$, provable by induction). Meanwhile $t_n = (-1)^n n$ diverges but tends to neither $+\infty$ nor $-\infty$.

^ex-9-8

> [!theorem] Lemma §9.7: Squeezing to Infinity
> If $s_n \to +\infty$ and $t_n \geq s_n$ for all $n$, then $t_n \to +\infty$.

^lem-9-7

> [!proof]+ Proof
> Given $M$, take $N$ with $s_n > M$ for $n > N$; then $t_n \geq s_n > M$ for $n > N$. (The same proof gives the *eventual* version: it suffices that $t_n \geq s_n$ for $n > N_0$ — replace $N$ by $\max\{N, N_0\}$. Similarly, $t_n \to -\infty$ and $s_n \leq t_n$ eventually force $s_n \to -\infty$. Both refinements were HW.)

^pf-9-7

*Uses:* [[§9 Limit Theorems for Sequences#^def-9-1|Def. §9.1]]

> [!theorem] Proposition §9.8: Adding a Sequence Bounded Below (HW)
> If $s_n \to +\infty$ and $\inf\{t_n \mid n \in \mathbb{N}\} > -\infty$, then
>
> $$
> s_n + t_n \to +\infty.
> $$
>
> In particular, the conclusion holds whenever $(t_n)$ is bounded, or convergent, or $t_n \to +\infty$.

^prop-9-8

> [!proof]+ Proof
> Let $t_0 = \inf\{t_n\} \in \mathbb{R}$, so $t_n \geq t_0$ for all $n$. Given $M > 0$: since $s_n \to +\infty$, there is $N$ with $s_n > M - t_0$ for all $n > N$. Then for such $n$,
>
> $$
> s_n + t_n \geq s_n + t_0 > (M - t_0) + t_0 = M.
> $$
>
> For the particular cases, only $\inf t_n > -\infty$ must be checked: a bounded sequence satisfies it directly; a convergent one is bounded ([[§9 Limit Theorems for Sequences#^thm-9-1|Theorem §9.1]]); and if $t_n \to +\infty$, then all but finitely many terms exceed $0$, and a finite set of terms is bounded. (Compare the forbidden $(+\infty) - (+\infty)$ of §5: a lower bound on the perturbation is exactly what rules the bad case out.)

^pf-9-8

*Uses:* [[§9 Limit Theorems for Sequences#^def-9-1|Def. §9.1]], [[§9 Limit Theorems for Sequences#^thm-9-1|§9.1]]

> [!example] Example §9.9: The Recursion Again
> The sequence $x_1 = 1$, $x_{n+1} = 3 x_n^2$ ([[§9 Limit Theorems for Sequences#^ex-9-7|Example §9.7]]) diverges to $+\infty$. Compute: $x_2 = 3$, $x_3 = 3 x_2^2 = 27 > 3^2$. *Claim:* $x_n \geq 3^{n-1}$, by induction: true for $n = 1$; if $x_n \geq 3^{n-1}$, then
>
> $$
> x_{n+1} = 3 x_n^2 \geq 3 \cdot 3^{2n-2} = 3^{2n-1} \geq 3^n.
> $$
>
> Therefore $x_n \to +\infty$ by the squeezing lemma, since $3^{n-1} \to +\infty$.

^ex-9-9

> [!example] Example §9.10: Complete Classification of the Geometric Sequence
> For any $a \in \mathbb{R}$:
>
> 1. if $|a| < 1$, then $\lim_{n\to\infty} a^n = 0$;
>
> 2. if $a = 1$, then $\lim_{n\to\infty} a^n = 1$;
>
> 3. if $a > 1$, then $a^n \to +\infty$;
>
> 4. if $a \leq -1$, then $\lim_{n\to\infty} a^n$ does not exist (not even as $\pm\infty$).
>
> *Proofs.* (2) is clear. (1) By the [[Squeeze Theorem|Squeeze Theorem]]: $-|a|^n \leq a^n \leq |a|^n$, and $|a|^n \to 0$ ([[§9 Limit Theorems for Sequences#^ex-9-3|Example §9.3]]), hence $-|a|^n \to 0$ too. (3) Check by definition: write $a = 1 + b$, $b > 0$; then $a^n \geq 1 + nb > nb \to +\infty$, and apply the squeezing lemma. (4) For $a = -1$ this is [[§8 A Discussion About Proofs#^ex-8-6|Example §8.6]]. For $a < -1$: the terms satisfy $|a^n| = |a|^n \geq 1$ and alternate in sign, so by the same even/odd-subsequence argument as for $(-1)^n$, no finite limit exists; and neither $a^n \to +\infty$ nor $a^n \to -\infty$, since arbitrarily late terms are negative (resp. positive).

^ex-9-10

> [!remark]- Connections
> - Computational version: [[§69 Sequences#^thm-69-8|Calc Thm. §69.8]] (with worked examples).

## The Ratio Test

A simple criterion for convergence and divergence:

> [!theorem] Theorem §9.9: Ratio Test
> Assume $s_n \neq 0$ for all $n$ and that the limit $L = \displaystyle\lim_{n\to+\infty} \left| \frac{s_{n+1}}{s_n} \right|$ exists.
>
> - (a) If $L < 1$, then $\lim s_n = 0$.
>
> - (b) If $L > 1$, then $\lim |s_n| = +\infty$, and hence $(s_n)$ is divergent.

^thm-9-9

> [!proof]+ Proof
> (a) Pick $\varepsilon > 0$ such that $L + \varepsilon < 1$ (possible since $L < 1$). By assumption, there exists $N$ such that for $n \geq N$,
>
> $$
> \left| \left| \frac{s_{n+1}}{s_n} \right| - L \right| < \varepsilon, \qquad \text{which implies} \qquad \left| \frac{s_{n+1}}{s_n} \right| < L + \varepsilon.
> $$
>
> Let $a = L + \varepsilon$, so $0 < a < 1$ and
>
> $$
> |s_{n+1}| < a |s_n| \qquad \text{for all } n \geq N.
> $$
>
> By induction this gives, for all $n > N$,
>
> $$
> |s_n| < a^{n - N} |s_N|
> $$
>
> (base case $n = N+1$ is the display; the step multiplies by one more factor of $a$). Now $a^{n-N} |s_N| = (a^{-N} |s_N|) \, a^n \to 0$ since $0 < a < 1$, so $|s_n| \to 0$ by squeezing, and hence $s_n \to 0$ (§8).
>
> (b) Pick $\varepsilon > 0$ with $L - \varepsilon > 1$. By the same argument there exists $N$ such that $\left| \tfrac{s_{n+1}}{s_n} \right| > L - \varepsilon$ for $n \geq N$. Let $b = L - \varepsilon > 1$; then $|s_{n+1}| > b |s_n|$ for $n \geq N$, and by induction
>
> $$
> |s_n| > b^{n-N} |s_N| \qquad \text{for } n > N.
> $$
>
> Since $b > 1$ and $|s_N| > 0$, the right side tends to $+\infty$ (classification (3) above, scaled), so $|s_n| \to +\infty$ by the squeezing lemma. An unbounded sequence diverges.

^pf-9-9

*Uses:* [[§7 Limits of Sequences#^def-7-2|Def. §7.2]], [[§8 A Discussion About Proofs#^ex-8-5|Ex. §8.5]], [[§9 Limit Theorems for Sequences#^ex-9-10|Ex. §9.10]], [[§9 Limit Theorems for Sequences#^lem-9-7|§9.7]], [[Squeeze Theorem|§8.1]], [[§9 Limit Theorems for Sequences#^thm-9-1|§9.1]]

> [!example] Example §9.11: Powers versus Exponentials
> Let $a \in \mathbb{R}$ and $p \in \mathbb{R}$. Then:
>
> 1. if $|a| < 1$: $\lim_{n\to\infty} \dfrac{a^n}{n^p} = 0$;
>
> 2. if $a > 1$: $\dfrac{a^n}{n^p} \to +\infty$;
>
> 3. if $a < -1$: $\lim_{n\to\infty} \dfrac{a^n}{n^p}$ does not exist.
>
> For (1): if $p \geq 0$, compare $|a^n / n^p| \leq |a|^n \to 0$; if $p < 0$ (and $a \neq 0$; for $a = 0$ every term is $0$), apply the ratio test:
>
> $$
> \left| \frac{s_{n+1}}{s_n} \right| = |a| \left( \frac{n}{n+1} \right)^p \longrightarrow |a| < 1.
> $$
>
> For (2), the same ratio computation gives $L = a > 1$. For (3), the magnitudes $|a|^n / n^p \to +\infty$ by (2) while signs alternate.

^ex-9-11

> [!example] Example §9.12: Factorials Beat Exponentials
> For all $a \in \mathbb{R}$: $\displaystyle\lim_{n\to\infty} \frac{a^n}{n!} = 0$. Use the ratio test (for $a \neq 0$):
>
> $$
> \left| \frac{s_{n+1}}{s_n} \right| = \frac{|a|^{n+1}/(n+1)!}{|a|^n/n!} = \frac{|a|}{n+1} \longrightarrow 0 = L < 1. \tag*{$\blacksquare$}
> $$

^ex-9-12

> [!remark] Remark: A Scale of Growth Rates
> We have met different rates of growth, each of a strictly higher order than the previous:
>
> $$
> \underbrace{n^p \ (p > 0)}_{\text{power}} \quad \ll \quad \underbrace{a^n \ (a > 1)}_{\text{exponential}} \quad \ll \quad \underbrace{n!}_{\text{super-exponential}},
> $$
>
> where $\ll$ means the ratio of the earlier to the later tends to $0$ — exactly the content of the two examples above (with the important special cases $2^n$ and $e^n$). Is there something $\to +\infty$ but *slower than any power*? Answer: $s_n = \log n$. The lecture's argument that $\tfrac{\log n}{n} \to 0$: the ratio test does not work here; instead *change variables*, $t = \log n$, so $n = e^t$ and
>
> $$
> \frac{\log n}{n} = \frac{t}{e^t} \longrightarrow 0 \quad \text{as } t \to +\infty,
> $$
>
> since the exponential grows at a higher rate than the power $t$. (As with $\log$ in the earlier example, this argument borrows the functions $\log$ and $e^t$ — and limits along a continuous variable — before their rigorous development; the honest statement is that it will become fully rigorous once those tools are available.)

^rem-9-3
