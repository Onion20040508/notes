---
subject: "[[Single Variable Analysis]]"
section: 10
chapter: 2
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §9 Limit Theorems for Sequences]] · ↑ [[Single Variable Analysis — 2 Sequences]] · [[Single Variable Analysis §11 Subsequences]] →

So far, mainly three ways to determine whether a sequence converges: (1) guess the limit and check the $(\varepsilon, N)$ definition; (2) use basic examples plus the limit theorems and the [[Squeeze Theorem|Squeeze Theorem]]; (3) sometimes, the ratio test. But we need criteria that work *without knowing the value of the limit* — sometimes we need the existence of $\lim s_n$ even when we cannot compute it. In one important case, we can do it.

## Monotone Sequences

> [!definition] Definition §10.1: Monotone Sequences
> A sequence $(s_n)$ is called **increasing** if $s_n \leq s_{n+1}$ for all $n$, and **decreasing** if $s_n \geq s_{n+1}$ for all $n$. It is called **monotone** if it is either increasing or decreasing (the term includes both).

^def-10-1

> [!example] Example §10.1: Monotone or not
> (1) $s_n = n$ and $s_n = n^2$ are increasing. (2) $s_n = 1 - \tfrac1n$ is also increasing. (3) $s_n = 1 + (-1)^n \tfrac{1}{n^2}$ is *not* monotone — consecutive differences alternate in sign.
>
> What is the difference between (1) and (2)? (1) is increasing but *not bounded above* — and not convergent. (2) is increasing *and bounded* — and converges to $1$.

^ex-10-1

> [!theorem] Theorem §10.1: Monotone Convergence Theorem
> If a sequence $(s_n)$ is monotone and bounded, then it is convergent.

^thm-10-1

> [!remark] Remark
> Both assumptions are needed. Is there a bounded sequence that is not convergent? Yes: $s_n = (-1)^n$ — the monotone condition is missing. And $s_n = n$ is monotone but unbounded.

^rem-10-1

> [!proof]+ Proof
> Assume $(s_n)$ is increasing; the decreasing case is the same (using $\inf$ in place of $\sup$).
>
> *What can we take as the limit $s$?* Since $s_n \leq s_{n+1} \leq \cdots$, the limit should be $\geq$ every $s_n$ — an upper bound of all the terms. And since the limit is unique, we do not want just *any* upper bound; the natural candidate is the *least* upper bound, which is unique.
>
> Define the set $S = \{s_n \mid n \geq 1\}$. It is bounded (that is exactly the boundedness assumption on the sequence), and nonempty. By the **[[Completeness Axiom|completeness axiom]]**, $s = \sup S$ exists and is a finite real number. We prove $s_n \to s$ by the $(\varepsilon, N)$ definition.
>
> For any $\varepsilon > 0$: since $s - \varepsilon < s$, the number $s - \varepsilon$ is *not* an upper bound of $S$ ([[Characterization of the Supremum|characterization of the supremum]], §4). Therefore there exists some element $s_N \in S$ with
>
> $$
> s_N > s - \varepsilon.
> $$
>
> Since $(s_n)$ is increasing, for any $n \geq N$ we have $s_n \geq s_N > s - \varepsilon$. Clearly also $s_n \leq s < s + \varepsilon$ ($s$ is an upper bound). So for all $n \geq N$,
>
> $$
> s - \varepsilon < s_n < s + \varepsilon, \qquad \text{i.e.} \qquad |s_n - s| < \varepsilon.
> $$

^pf-10-1

![[m451-10-1.svg]]
*The proof in one picture: an increasing sequence bounded above climbs toward the supremum of its own terms — and converges exactly there. Any upper bound $M$ sits at or above the dashed line; the supremum is the least one.*

The supremum also admits a *sequential* characterization — the limit-language form of the approximation property of §4, and the engine inside several later proofs (e.g. the [[Extreme Value Theorem|Extreme Value Theorem]], §18):

> [!theorem] Proposition §10.2: Sequential Characterization of the Supremum (HW)
> Let $S \subseteq \mathbb{R}$ be nonempty and bounded above. Then there exists a sequence $(s_n)$ of points of $S$ with
>
> $$
> \lim_{n\to\infty} s_n = \sup S.
> $$
>
> If moreover $\sup S \notin S$, the sequence can be chosen with $s_n < \sup S$ strictly for every $n$. In every case, the sequence can be chosen *increasing*.

^prop-10-2

> [!proof]+ Proof
> Write $s = \sup S$. If $s \in S$, the constant sequence $s_n = s$ works. Assume $s \notin S$. First, for any $\delta > 0$ there exists $s' \in S$ with $s - \delta < s' < s$: otherwise every $x \in S$ would satisfy $x \leq s - \delta$, making $s - \delta$ an upper bound smaller than the *least* upper bound — contradiction; and $s' < s$ is automatic, since $s' \leq s$ and $s' \neq s$ (as $s \notin S$ but $s' \in S$).
>
> Apply this with $\delta = \tfrac1n$ for each $n$: choose $s_n \in S$ with
>
> $$
> s - \frac1n < s_n < s.
> $$
>
> Then $|s_n - s| < \tfrac1n$, and given $\varepsilon > 0$, any $N > \tfrac1\varepsilon$ (Archimedean) gives $|s_n - s| < \tfrac1n \leq \tfrac1N < \varepsilon$ for $n \geq N$. Hence $s_n \to s$.
>
> *Increasing refinement* (also HW). In the case $s \in S$ the constant sequence is (weakly) increasing already. In the case $s \notin S$, make the choices recursively: having chosen $s_n < s$, note $\max\{s_n,\ s - \tfrac{1}{n+1}\} < s$, so the approximation step (applied with this maximum in place of $s - \delta$) provides
>
> $$
> s_{n+1} \in S, \qquad \max\left\{ s_n,\ s - \frac{1}{n+1} \right\} < s_{n+1} < s.
> $$
>
> The first bound forces $s_{n+1} > s_n$ (strictly increasing), and the second keeps $s_{n+1} > s - \tfrac{1}{n+1}$, so the same limit computation applies.

^pf-10-2

> [!example] Example §10.2: A recursion with no formula
> Let $s_1 = 1$ and $s_{n+1} = \sqrt{1 + s_n}$. Show $\lim s_n$ exists.
>
> We don't have an explicit formula for $s_n$, so it is not easy to guess the limit and check by $(\varepsilon, N)$. Instead we use the [[Monotone Convergence Theorem|Monotone Convergence Theorem]]: show *increasing* and *bounded*.
>
> **Experiment first.** $s_1 = 1$, $s_2 = \sqrt{1+1} = \sqrt2 > s_1$; one can also check $s_2 < s_3$. *Claim: $(s_n)$ is increasing.*
>
> *Proof of claim* (induction on the statement $s_{n+1} > s_n$). True for $n = 1$. Suppose $s_{n+1} > s_n$. Compare
>
> $$
> s_{n+2} = \sqrt{1 + s_{n+1}} \qquad \text{and} \qquad s_{n+1} = \sqrt{1 + s_n}:
> $$
>
> since $1 + s_{n+1} > 1 + s_n > 0$ and the square root is increasing on positive numbers ($0 < x < y \implies \sqrt{x} < \sqrt{y}$, else squaring gives a contradiction), we get $s_{n+2} > s_{n+1}$. Done.
>
> **Bounded above.** Take a guess for an upper bound $M$ — it should not be a random guess. The crucial point to check is that the bound *propagates through the recursion*:
>
> $$
> s_{n+1} = \sqrt{1 + s_n} \leq \sqrt{1 + M} \qquad \text{needs} \qquad \sqrt{1 + M} \leq M.
> $$
>
> Fortunately $M = 2$ satisfies this: $\sqrt{1+2} = \sqrt3 < 2$. Now induction: $s_1 = 1 \leq 2$; if $s_n \leq 2$ then $s_{n+1} = \sqrt{1+s_n} \leq \sqrt3 \leq 2$. So $s_n \leq 2$ for all $n$.
>
> By the Monotone Convergence Theorem, $s = \lim s_n$ exists.
>
> **What is the value?** From $s_{n+1} = \sqrt{1 + s_n}$ we get $s_{n+1}^2 = 1 + s_n$. One step deserves care before taking limits (HW): the shifted sequence $(s_{n+1})_n$ converges to the *same* limit $s$ — any $N$ witnessing the definition for $(s_n)$ works for the shift, since $n \geq N$ implies $n + 1 \geq N$. Granting this, the product rule gives $s_{n+1}^2 \to s^2$ and the sum rule gives $1 + s_n \to 1 + s$, so $s^2 = 1 + s$, i.e. $s^2 - s - 1 = 0$, so
>
> $$
> s = \frac{1 \pm \sqrt{1 + 4}}{2} = \frac{1 \pm \sqrt5}{2} \quad \text{--- two values.}
> $$
>
> *Claim: $s = \tfrac{1 + \sqrt5}{2}$.* Why? The other root is negative, while $s \geq s_1 = 1$. (One can also verify directly that $M = \tfrac{1+\sqrt5}{2}$ works as the upper bound in the induction — for this $M$, $\sqrt{1 + M} = M$ exactly.)

^ex-10-2

> [!theorem] Theorem §10.3: Unbounded Monotone Sequences
> If $(s_n)$ is increasing but not bounded above, then $\lim s_n = +\infty$. If $(s_n)$ is decreasing but not bounded below, then $\lim s_n = -\infty$.

^thm-10-3

> [!proof]+ Proof
> Check by definition. Let $M > 0$. Since $(s_n)$ is not bounded above, $M$ is not an upper bound: there exists $N$ with $s_N > M$. Since $(s_n)$ is increasing, $s_n \geq s_N > M$ for all $n \geq N$. Hence $s_n \to +\infty$. The decreasing case is symmetric.

^pf-10-3

Combining the two theorems: *a monotone sequence always has a limit in $[-\infty, +\infty]$.*

## Lim Sup and Lim Inf

In general a sequence is neither increasing nor decreasing, so the theorem above does not apply directly. **Question:** how to produce monotone sequences from an arbitrary given sequence?

> [!definition] Definition §10.2: Tail Suprema and Infima
> For any sequence $(s_n)$, define two new sequences indexed by $N$:
>
> $$
> \overline{s}_N = \sup \{ s_n \mid n \geq N \}, \qquad \underline{s}_N = \inf \{ s_n \mid n \geq N \}.
> $$
>
> If $(s_n)$ is bounded, these are finite numbers; otherwise we use the values $\pm\infty$ — another place where the extended real numbers are convenient.

^def-10-2

> [!theorem] Lemma §10.4: Monotonicity of the Tails
> $(\overline{s}_N)$ is decreasing, and $(\underline{s}_N)$ is increasing.

^lem-10-4

> [!proof]+ Proof
> We want $\overline{s}_{N+1} \leq \overline{s}_N$. The set for $\overline{s}_{N+1}$ — the tail starting at $N+1$ — is a subset of the set for $\overline{s}_N$ — the tail starting at $N$. And the supremum over a smaller set is at most the supremum over the larger: if $A \subseteq B$, every element of $A$ is $\leq \sup B$, so $\sup B$ is an upper bound of $A$, whence $\sup A \leq \sup B$. Similarly, the infimum over a smaller set is $\geq$, so $(\underline{s}_N)$ is increasing.

^pf-10-4

> [!definition] Definition §10.3: Lim Sup and Lim Inf
> Assume $(s_n)$ is bounded. Then $(\overline{s}_N)$ and $(\underline{s}_N)$ are bounded and monotone, so by the Monotone Convergence Theorem their limits exist; we denote them
>
> $$
> \limsup_{n \to +\infty} s_n = \lim_{N \to +\infty} \overline{s}_N, \qquad \liminf_{n \to +\infty} s_n = \lim_{N \to +\infty} \underline{s}_N.
> $$
>
> For unbounded sequences the same definitions are used with values in $[-\infty, +\infty]$.

^def-10-3

> [!remark] Remark
> The important thing: $\lim_{n\to\infty} s_n$ may not exist, but $\limsup s_n$ and $\liminf s_n$ *always* exist (in $[-\infty,+\infty]$). This gives a definite answer for every sequence.

^rem-10-2

![[m451-10-2.svg]]
*The envelopes at work for $s_n = (-1)^n\left(1 + \tfrac2n\right)$: the sequence (dots) has no limit, but the tail-suprema $\overline{s}_N$ (red, decreasing) and tail-infima $s_N$ (blue, increasing) are monotone and bounded, so each converges — to $\limsup = 1$ and $\liminf = -1$.*

> [!theorem] Proposition §10.5: Lim Inf Is at Most Lim Sup
> $\displaystyle \liminf_{n\to+\infty} s_n \leq \limsup_{n\to+\infty} s_n$.

^prop-10-5

> [!proof]+ Proof
> Why? Because $\underline{s}_N \leq \overline{s}_N$ for every $N$: the two are the $\inf$ and the $\sup$ of *the same set* $\{s_n \mid n \geq N\}$, and for a nonempty set the infimum is $\leq$ the supremum (both compare with any single element). Passing to the limit in $N$ preserves $\leq$.

^pf-10-5

If $\lim s_n$ exists, what is the relation? We expect $\liminf s_n \leq \lim s_n \leq \limsup s_n$. In fact, something stronger holds:

> [!theorem] Theorem §10.6: Convergence via Lim Sup and Lim Inf
> 1. If $\lim_{n\to+\infty} s_n$ exists, then
>
>    $$
>    \liminf_{n\to+\infty} s_n = \limsup_{n\to+\infty} s_n = \lim_{n\to+\infty} s_n.
>    $$
>
> 2. Conversely, if $\liminf_{n\to+\infty} s_n = \limsup_{n\to+\infty} s_n$ (finite), then $\lim_{n\to+\infty} s_n$ exists — $(s_n)$ is convergent, with this common value as limit.
>
> Part (2) gives another way to prove convergence of a sequence.

^thm-10-6

> [!proof]+ Proof
> (1) Let $s = \lim s_n$. For any $\varepsilon > 0$ there exists $N_0$ such that for all $n \geq N_0$,
>
> $$
> s - \varepsilon < s_n < s + \varepsilon.
> $$
>
> Taking the supremum and infimum over the tail $\{s_n \mid n \geq N\}$ for any $N \geq N_0$ (all its elements lie in $(s-\varepsilon,\, s+\varepsilon)$):
>
> $$
> s - \varepsilon \leq \underline{s}_N \leq \overline{s}_N \leq s + \varepsilon.
> $$
>
> Letting $N \to \infty$ (limits preserve $\leq$):
>
> $$
> s - \varepsilon \leq \liminf_{n\to\infty} s_n \leq \limsup_{n\to\infty} s_n \leq s + \varepsilon.
> $$
>
> Since $\varepsilon > 0$ is arbitrary, both $\liminf s_n$ and $\limsup s_n$ are squeezed to equal $s$.
>
> (2) Let $s$ denote the common value. Given $\varepsilon > 0$: since $\underline{s}_N \to s$ and $\overline{s}_N \to s$, there exists $N'$ such that for all $N \geq N'$,
>
> $$
> s - \varepsilon < \underline{s}_N \qquad \text{and} \qquad \overline{s}_N < s + \varepsilon.
> $$
>
> Now for any $n \geq N'$, the term $s_n$ belongs to the tail starting at $n$, so $\underline{s}_n \leq s_n \leq \overline{s}_n$, giving
>
> $$
> s - \varepsilon < \underline{s}_n \leq s_n \leq \overline{s}_n < s + \varepsilon, \qquad \text{i.e.} \qquad |s_n - s| < \varepsilon.
> $$
>
> We are done. (Alternatively and more directly: $\underline{s}_n \leq s_n \leq \overline{s}_n$ with both outer sequences converging to $s$ — apply the *Squeeze Theorem*.)

^pf-10-6

## Cauchy Sequences

The concepts above give another way to prove convergence, but they still involve computing the limits $\limsup s_n$, $\liminf s_n$. **Question:** is there a way to decide convergence *purely in terms of the sequence $(s_n)$ itself* — no candidate limit, no auxiliary limits? **Answer: yes** — the notion of Cauchy sequences.

> [!definition] Definition §10.4: Cauchy Sequence
> A sequence $(s_n)$ is called **Cauchy** if for any $\varepsilon > 0$ there exists $N$ such that for any pair $m, n \geq N$,
>
> $$
> |s_n - s_m| < \varepsilon.
> $$
>
> Compare with the $(\varepsilon, N)$ definition of the limit: instead of comparing $s_n$ with a limit $s$, we compare the terms *with each other*. The important point: the condition is purely in terms of $(s_n)$.

^def-10-4

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

> [!theorem] Theorem §10.8: Cauchy Implies Convergent
> If $(s_n)$ is a Cauchy sequence of real numbers, then $(s_n)$ is convergent. Combining with the previous theorem: *$(s_n)$ is convergent if and only if it is Cauchy.*

^thm-10-8

How to prove it? Not clear at first — we must produce a limit out of nothing. Let us analyze: first check boundedness.

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

> [!proof]+ Proof
> Since $(s_n)$ is bounded, $\liminf s_n$ and $\limsup s_n$ are finite. We use the criterion of the previous subsection: it suffices to show they are equal — so we try to get information on $\underline{s}_N$, $\overline{s}_N$.
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
> and by the theorem of the previous subsection, $(s_n)$ is convergent.

^pf-10-9

> [!example] Example §10.3: A contraction-type estimate
> Assume $(s_n)$ satisfies $|s_{n+1} - s_n| < 2^{-n}$ for all $n \geq 1$. Prove $(s_n)$ is a Cauchy sequence, and hence convergent.
>
> We need to see how big $|s_m - s_n|$ is for $m > n$. Telescope through the intermediate terms and apply the [[Triangle inequality|triangle inequality]]:
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

> [!remark] Remark: The geometric rate is doing the work (HW)
> It is *not* enough that consecutive differences tend to $0$: the weaker hypothesis $|s_{n+1} - s_n| < \tfrac1n$ does not imply Cauchy. Counterexample:
>
> $$
> s_n = 1 + \frac12 + \frac13 + \cdots + \frac1n, \qquad |s_{n+1} - s_n| = \frac{1}{n+1} < \frac1n,
> $$
>
> yet $(s_n)$ is unbounded: grouping the terms in dyadic blocks,
>
> $$
> s_{2^k} = 1 + \frac12 + \underbrace{\left(\frac13 + \frac14\right)}_{>\, 2\cdot\frac14} + \underbrace{\left(\frac15 + \cdots + \frac18\right)}_{>\, 4\cdot\frac18} + \cdots \ >\ 1 + \frac k2,
> $$
>
> and since $(s_n)$ is increasing, it exceeds any $M$ from some point on. Unbounded sequences are not Cauchy. (These are the partial sums of the *harmonic series*; the same dyadic estimate returns in §14.) The moral: in the example above, the increments were *summable* — the geometric tail $2^{-n+1}$ stayed uniformly small — whereas mere decay of single increments controls nothing about the accumulated drift.

^rem-10-3

> [!remark] Remark: Cauchy sequences and the construction of the reals
> Cauchy sequences can be used to construct $\mathbb{R}$ from $\mathbb{Q}$: real numbers can be identified with equivalence classes of Cauchy sequences of rational numbers (two sequences being equivalent when their difference tends to $0$). This is the second standard construction of $\mathbb{R}$, alongside the Dedekind cuts of §6. Note the logical order in this course, however: we *assumed* $\mathbb{R}$ with completeness, and the theorem above (Cauchy $\Rightarrow$ convergent) is a *consequence* — indeed an equivalent form — of the completeness axiom.

^rem-10-4
