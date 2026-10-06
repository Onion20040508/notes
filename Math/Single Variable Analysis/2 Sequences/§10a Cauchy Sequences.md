---
type: section
subject: "[[Single Variable Analysis]]"
section: "10a"
aliases: ["Ross 10 (cont.)"]
chapter: 2
tags: [real-analysis, math451]
---
← [[§10 Monotone Sequences and Cauchy Sequences]] · ↑ [[· 2 Sequences]] · [[§11 Subsequences]] →

The concepts above (lim sup and lim inf, [[§10 Monotone Sequences and Cauchy Sequences#Lim Sup and Lim Inf|§10]]) give another way to prove convergence, but they still involve computing the limits $\limsup s_n$, $\liminf s_n$. **Question:** is there a way to decide convergence *purely in terms of the sequence $(s_n)$ itself* — no candidate limit, no auxiliary limits? **Answer: yes** — the notion of Cauchy sequences.

## Cauchy Sequences

> [!definition] Definition §10.4: Cauchy Sequence
> A sequence $(s_n)$ is called **Cauchy** if for any $\varepsilon > 0$ there exists $N$ such that for any pair $m, n \geq N$,
>
> $$
> |s_n - s_m| < \varepsilon.
> $$
>
> Compare with the $(\varepsilon, N)$ definition of the limit: instead of comparing $s_n$ with a limit $s$, we compare the terms *with each other*. The important point: the condition is purely in terms of $(s_n)$.

^def-10-4

> [!remark]- Connections
> - The same condition with a norm in place of the absolute value: [[§10 Normed Linear Spaces#^def-10-5|556 Def. §10.5]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-new1|551 Def. §19.4]]; in a metric space, [[§13 Some Topological Concepts in Metric Spaces#^def-13-new1|Def. §13.2]].

> [!theorem] Theorem §10.7: Convergent Implies Cauchy
> Every convergent sequence is a Cauchy sequence.

^thm-10-7

> [!proof]+ Proof
> Let $s = \lim s_n$. For any $\varepsilon > 0$ there exists $N$ such that $|s_n - s| < \tfrac\varepsilon2$ for all $n \geq N$. Then for any pair $m, n \geq N$,
>
> $$
> |s_n - s_m| = |s_n - s + s - s_m| \leq |s_n - s| + |s - s_m| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon.
> $$
>
> So being Cauchy is a *necessary* condition for convergence.

^pf-10-7

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

Conversely, is every Cauchy sequence convergent ([[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|Theorem §10.8]] below)? How to prove it? Not clear at first — we must produce a limit out of nothing. Let us analyze: first check boundedness.

> [!theorem] Lemma §10.9: Cauchy Implies Bounded
> If $(s_n)$ is Cauchy, then $(s_n)$ is bounded.

^lem-10-9

> [!proof]+ Proof
> Let $\varepsilon = 1$: there exists $N$ such that $|s_n - s_m| < 1$ for all $m, n \geq N$. In particular, taking $m = N$: for all $n \geq N$,
>
> $$
> |s_n - s_N| < 1, \qquad \text{so} \qquad |s_n| < 1 + |s_N|.
> $$
>
> Do we have a bound yet? Not yet — the initial terms again. Take
>
> $$
> M = \max\{|s_1|, \ldots, |s_{N-1}|,\ 1 + |s_N|\}.
> $$
>
> Then $|s_n| \leq M$ for all $n \geq 1$.

^pf-10-9

*Uses:* [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]], [[§4 The Completeness Axiom#^ex-4-1|Ex. §4.1]]

> [!theorem] Theorem §10.8: Cauchy Implies Convergent
> If $(s_n)$ is a Cauchy sequence of real numbers, then $(s_n)$ is convergent. Combining with the previous theorem: *$(s_n)$ is convergent if and only if it is Cauchy.*

^thm-10-8

> [!proof]+ Proof
> Since $(s_n)$ is bounded, $\liminf s_n$ and $\limsup s_n$ are finite. We use the criterion of [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|Theorem §10.6]]: it suffices to show they are equal — so we try to get information on $\underline{s}_N$, $\overline{s}_N$.
>
> For any $\varepsilon > 0$ there exists $N$ such that for all $m, n \geq N$,
>
> $$
> -\varepsilon < s_n - s_m < \varepsilon.
> $$
>
> Taking $m = N$: for all $n \geq N$,
>
> $$
> s_N - \varepsilon < s_n < s_N + \varepsilon.
> $$
>
> Since this holds for *every* $n \geq N$, we get — crucially — bounds on the whole tail:
>
> $$
> s_N - \varepsilon \leq \underline{s}_N \leq \overline{s}_N \leq s_N + \varepsilon.
> $$
>
> Since $(\underline{s}_N)$ is increasing and $(\overline{s}_N)$ is decreasing, for all $N' \geq N$ we retain $\underline{s}_{N} \leq \underline{s}_{N'} \leq \overline{s}_{N'} \leq \overline{s}_{N}$; letting $N' \to \infty$,
>
> $$
> s_N - \varepsilon \leq \liminf_{n\to\infty} s_n \leq \limsup_{n\to\infty} s_n \leq s_N + \varepsilon,
> $$
>
> hence
>
> $$
> 0 \leq \limsup_{n\to\infty} s_n - \liminf_{n\to\infty} s_n \leq 2\varepsilon.
> $$
>
> Since $\varepsilon$ is arbitrary, squeezing between $0$ and $2\varepsilon$ forces
>
> $$
> \limsup_{n\to\infty} s_n = \liminf_{n\to\infty} s_n,
> $$
>
> and by [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|Theorem §10.6]](2), $(s_n)$ is convergent.

^pf-10-8

*Uses:* [[§10 Monotone Sequences and Cauchy Sequences#^lem-10-9|§10.9]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-6|§10.6]], [[§10 Monotone Sequences and Cauchy Sequences#^lem-10-4|§10.4]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]]

![[m451-10-4.svg]]
*Cauchy implies convergent, with no limit in sight: the band is anchored at a *term* $s_N$ (red), not at a limit. Every later term lies within $\varepsilon$ of $s_N$, so the whole tail — and with it $\underline{s}_N \leq \overline{s}_N$, hence $\liminf s_n$ and $\limsup s_n$ — is caught in an interval of length $2\varepsilon$.*

> [!example] Example §10.3: A Contraction-Type Estimate
> Assume $(s_n)$ satisfies $|s_{n+1} - s_n| < 2^{-n}$ for all $n \geq 1$. Prove $(s_n)$ is a Cauchy sequence, and hence convergent.
>
> We need to see how big $|s_m - s_n|$ is for $m > n$. Telescope through the intermediate terms and apply the [[§3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]]:
>
> $$
> |s_m - s_n| \leq |s_m - s_{m-1}| + |s_{m-1} - s_{m-2}| + \cdots + |s_{n+1} - s_n|
> \leq 2^{-(m-1)} + \cdots + 2^{-n}.
> $$
>
> Summing the geometric progression,
>
> $$
> 2^{-n} + \cdots + 2^{-(m-1)} = \frac{2^{-n} - 2^{-m}}{1 - \tfrac12} < \frac{2^{-n}}{1 - \tfrac12} = 2^{-n+1}.
> $$
>
> Note the right-hand side is *independent of $m$*. Now, for any $\varepsilon > 0$, choose $N$ such that $2^{-N+1} < \varepsilon$ (possible since $2^{-N+1} \to 0$). Then for all $m \geq n \geq N$,
>
> $$
> |s_m - s_n| < 2^{-n+1} \leq 2^{-N+1} < \varepsilon,
> $$
>
> and we are done: $(s_n)$ is Cauchy, hence convergent.

^ex-10-3

> [!remark] Remark: The Geometric Rate Is Doing the Work (HW)
> It is *not* enough that consecutive differences tend to $0$: the weaker hypothesis $|s_{n+1} - s_n| < \tfrac1n$ does not imply Cauchy. Counterexample:
>
> $$
> s_n = 1 + \frac12 + \frac13 + \cdots + \frac1n, \qquad |s_{n+1} - s_n| = \frac{1}{n+1} < \frac1n,
> $$
>
> yet $(s_n)$ is unbounded: grouping the terms in dyadic blocks,
>
> $$
> s_{2^k} = 1 + \frac12 + \underbrace{\left(\frac13 + \frac14\right)}_{>\, 2\cdot\frac14} + \underbrace{\left(\frac15 + \cdots + \frac18\right)}_{>\, 4\cdot\frac18} + \cdots \ \geq\ 1 + \frac k2,
> $$
>
> and since $(s_n)$ is increasing, it exceeds any $M$ from some point on. Unbounded sequences are not Cauchy. (These are the partial sums of the *harmonic series*; the same dyadic estimate returns in §14.) The moral: in the example above, the increments were *summable* — the geometric tail $2^{-n+1}$ stayed uniformly small — whereas mere decay of single increments controls nothing about the accumulated drift.

^rem-10-3

> [!remark] Remark: Cauchy Sequences and the Construction of the Reals
> Cauchy sequences can be used to construct $\mathbb{R}$ from $\mathbb{Q}$: real numbers can be identified with equivalence classes of Cauchy sequences of rational numbers (two sequences being equivalent when their difference tends to $0$). This is the second standard construction of $\mathbb{R}$, alongside the [[§6 Dedekind Cuts#^def-6-1|Dedekind cuts]] of §6. Note the logical order in this course, however: we *assumed* $\mathbb{R}$ with completeness, and the theorem above (Cauchy $\Rightarrow$ convergent) is a *consequence* — indeed an equivalent form — of the [[Completeness Axiom|completeness axiom]].
>
> ★ The construction is carried out, with proofs, in [[§6★ ℝ from Cauchy Sequences of Rationals]].

^rem-10-4
