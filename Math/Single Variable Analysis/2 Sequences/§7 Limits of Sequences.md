---
type: section
subject: "[[Single Variable Analysis]]"
section: 7
chapter: 2
tags: [real-analysis, math451]
---
← [[§6★ ℝ from Cauchy Sequences of Rationals]] · ↑ [[· 2 Sequences]] · [[§8 A Discussion About Proofs]] →

We have discussed the properties of $\mathbb{R}$, including the [[Completeness Axiom|completeness axiom]] and a construction of $\mathbb{R}$ from $\mathbb{Q}$ via Dedekind cuts. Now we are ready to introduce the very basic notion of *limits*. We deal first with limits of sequences.

## Sequences

> [!definition] Definition §7.1: Sequence
> A **sequence** $(s_n)$ of numbers is a list $s_m, s_{m+1}, s_{m+2}, \ldots$, where the index $n$ can start at any integer $m$ (usually $m = 0$ or $1$). Formally, it is a function (map)
>
> $$
> s : \{n \in \mathbb{Z} \mid n \geq m\} \to \mathbb{R},
> $$
>
> whose value at $n$ is denoted $s_n$ instead of $s(n)$. We also write $(s_n)_{n=m}^{\infty}$ — one convenient place where the symbol $\infty$ is used.

^def-7-1

> [!remark]- Connections
> - Elementary version: a sequence as a function on ℤ⁺, [[§8 Functions#^def-8-7|250 Def. §8.7]].
> - Computational version: [[§69 Sequences#^def-69-1|Calc Def. §69.1]] (with worked examples).

> [!example] Example §7.1: First Examples
> 1. $s_n = 1$: a constant sequence.
>
> 2. $s_n = n$.
>
> 3. $s_n = \dfrac{1}{n}$, $n \geq 1$.
>
> 4. $s_n = (-1)^n \dfrac{1}{n}$, $n \geq 1$.
>
> What behaviors do we observe? The constant sequence stays put; $s_n = n$ grows without bound; $\tfrac1n$ shrinks toward $0$ from above; $(-1)^n \tfrac1n$ shrinks toward $0$ while oscillating in sign. We are interested in such *long-time behaviors* — this is the basic issue, and to discuss it we need a precise definition.

^ex-7-1

## The $(\varepsilon, N)$ Definition

> [!definition] Definition §7.2: Convergence of a Sequence
> A sequence $(s_n)$ of real numbers is said to **converge** to a number $s$ if for any $\varepsilon > 0$ (usually small), there exists an integer $N$ (usually large) such that for every $n \geq N$,
>
> $$
> |s_n - s| < \varepsilon.
> $$
>
> In this case we write $s_n \to s$, or $\displaystyle\lim_{n \to \infty} s_n = s$, and call $s$ the **limit** of $(s_n)$.

^def-7-2

![[m451-7-1.svg]]
*The $(\varepsilon, N)$ picture: however narrow the band $s \pm \varepsilon$, some stage $N$ exists beyond which every dot (blue) lies inside; the early terms (gray) may wander freely — convergence is a statement about tails. (Compare §24: uniform convergence of functions is this same picture with dots replaced by whole graphs.)*

> [!remark]- Connections
> - Computational version: [[§60 Convergence of Sequences#^def-60-1|342 Def. §60.1]] (convergence of complex sequences, with the modulus in place of the absolute value).
> - Several-variable version: [[§1 Sequences and Limits in ℝⁿ#^def-1-1|452 Def. §1.1]] (convergence in ℝⁿ, with the Euclidean norm in place of the absolute value).

> [!remark] Remark: What Does the Definition Catch?
> The condition $|s_n - s| < \varepsilon$ says $s_n$ approximates $s$ with error less than $\varepsilon$. The definition demands: *no matter how small an error tolerance $\varepsilon$ is prescribed, from some stage $N$ onward, every term of the sequence meets that tolerance.* The order of quantifiers is essential: $\varepsilon$ is given first (arbitrarily), and $N$ is allowed to depend on $\varepsilon$.

^rem-7-1

> [!remark]- Connections
> - The case s = 0 in 250: null sequences, [[§8 Functions#^def-8-8|250 Def. §8.8]], with the order of the quantifiers ∀ε ∃N discussed in [[§8 Functions#^ex-8-8|250 Ex. §8.8]].

> [!definition] Definition §7.3: Divergence
> If there exists no real number $s$ such that $(s_n)$ converges to $s$, we say $(s_n)$ **diverges**. For example, $s_n = 2^n$ diverges (it is unbounded; see §9).

^def-7-3

> [!example] Example §7.2: Constant Sequence
> If $s_n = 1$ for all $n$, then $\lim_{n\to\infty} s_n = 1$. Checking the definition: given $\varepsilon > 0$, take $N = 1$; for every $n \geq N$, $|s_n - 1| = 0 < \varepsilon$.

^ex-7-2

> [!example] Example §7.3: $1/n \to 0$
> If $s_n = \tfrac1n$ for $n \geq 1$, then $\lim_{n\to\infty} s_n = 0$.
>
> *Proof.* For $\varepsilon > 0$, we need to find $N$. Take $N$ such that $N > \tfrac{1}{\varepsilon}$ — why can we do this? By the *[[Archimedean Property|Archimedean Property]]* (§4). When $n \geq N$, we have $n > \tfrac1\varepsilon$, hence
>
> $$
> |s_n - 0| = \frac1n < \varepsilon. \tag*{$\blacksquare$}
> $$

^ex-7-3

> [!remark] Remark: How Did We Find $N$?
> Usually we *solve the inequality* $|s_n - s| < \varepsilon$ for $n$. In the example above: we want $\tfrac1n < \varepsilon$, i.e. $n > \tfrac1\varepsilon$; so we take any positive integer $N > \tfrac1\varepsilon$. The same method handles $s_n = (-1)^n \tfrac1n$ (since $|s_n - 0| = \tfrac1n$, the same $N$ works) and $s_n = \tfrac{1}{n^2}$: solving $\tfrac{1}{n^2} < \varepsilon$ gives $n^2 > \tfrac1\varepsilon$, i.e. $n > \sqrt{1/\varepsilon}$, so take $N > \sqrt{1/\varepsilon}$. There are several valid choices of $N$ — any sufficiently large one works.

^rem-7-2

> [!example] Example §7.4: Simplifying before Solving
> Let $s_n = \dfrac{n}{n+1}$. Prove $s_n \to 1$.
>
> *Proof.* Compute
>
> $$
> \left| \frac{n}{n+1} - 1 \right| = \left| \frac{n - 1 - n}{1+n} \right| = \frac{1}{1+n}.
> $$
>
> We could solve $\tfrac{1}{1+n} < \varepsilon$ directly, but we can also *simplify first*:
>
> $$
> \frac{1}{1+n} < \frac1n,
> $$
>
> so it is good enough to have $\tfrac1n < \varepsilon$, and we can take $N > \tfrac1\varepsilon$.

^ex-7-4

> [!example] Example §7.5: When the Naive Simplification Fails
> Let $s_n = \dfrac{n}{n-1}$, $n \geq 2$. Prove $s_n \to 1$.
>
> Here $\left| \tfrac{n}{n-1} - 1 \right| = \left| \tfrac{n - (n-1)}{n-1} \right| = \tfrac{1}{n-1}$. Can we simplify by replacing $\tfrac{1}{n-1}$ by $\tfrac1n$? **No:** $\tfrac{1}{n-1} > \tfrac1n$, so $\tfrac1n < \varepsilon$ does *not* imply $\tfrac{1}{n-1} < \varepsilon$ — an upper bound must be replaced by something *larger*, not smaller. Two correct ways:
>
> 1. *Directly:* $\tfrac{1}{n-1} < \varepsilon \iff n - 1 > \tfrac1\varepsilon \iff n > \tfrac1\varepsilon + 1$. Take $N > \tfrac1\varepsilon + 1$.
>
> 2. *Bound by a simpler expression:* for $n \geq 2$, $n - 1 \geq \tfrac{n}{2}$, so $\tfrac{1}{n-1} \leq \tfrac2n$. It suffices to have $\tfrac2n < \varepsilon$, i.e. $n > \tfrac2\varepsilon$. Take $N > \tfrac2\varepsilon$.

^ex-7-5

## Uniqueness of the Limit

The first property of limits — and our first theorem with a real proof about them.

> [!theorem] Theorem §7.1: Uniqueness of Limits
> If a sequence $(s_n)$ has a limit, then the limit is unique: if $\lim_{n\to\infty} s_n = s$ and $\lim_{n\to\infty} s_n = t$, then $s = t$.

^thm-7-1

> [!proof]+ Proof
> Suppose not: $s \neq t$. Then $s - t \neq 0$, hence $|s - t| > 0$. We look for a contradiction.
>
> Take $\varepsilon$ with $0 < \varepsilon < \tfrac12 |s - t|$. By the definition of $s_n \to s$, there exists $N_1$ such that $|s_n - s| < \varepsilon$ for $n \geq N_1$. Similarly, there exists $N_2$ such that $|s_n - t| < \varepsilon$ for $n \geq N_2$. Take $N = \max\{N_1, N_2\}$; then for $n \geq N$ *both* inequalities hold. By the [[§3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]], for any such $n$,
>
> $$
> |s - t| = |(s - s_n) - (t - s_n)| \leq |s - s_n| + |t - s_n| < \varepsilon + \varepsilon = 2\varepsilon < |s - t|.
> $$
>
> So $|s - t| < |s - t|$ — a contradiction. Where does it come from? From the assumption $s \neq t$, which gave $|s-t| > 0$ and allowed the choice of $\varepsilon$. Hence $s = t$.

^pf-7-1

*Uses:* [[§7 Limits of Sequences#^def-7-2|Def. §7.2]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

![[m451-7-2.svg]]
*Why limits are unique: with $\varepsilon < \tfrac12|s-t|$ the bands $(s-\varepsilon, s+\varepsilon)$ (blue) and $(t-\varepsilon, t+\varepsilon)$ (red) are disjoint. From $N = \max\{N_1, N_2\}$ on, every $s_n$ would have to lie in both — impossible.*

> [!remark]- Connections
> - Computational version: [[§60 Convergence of Sequences#^prop-60-1|342 Prop. §60.1]] (uniqueness for complex sequences); the same argument for limits of complex functions is [[§15 Limits#^thm-15-1|342 Thm. §15.1]].

> [!remark] Remark: Summary of the Method
> To determine whether $(s_n)$ is convergent, we determine whether it has a limit, in two steps:
>
> 1. **guess** a limit $s$;
>
> 2. **prove** it by the $(\varepsilon, N)$ definition — the key point being to solve $N$ in terms of $\varepsilon$.

^rem-7-3

> [!remark]- Connections
> - In topological spaces limits are unique when the space is Hausdorff: [[§8 Hausdorff Spaces#^thm-8-3|590 Thm. §8.3]].
