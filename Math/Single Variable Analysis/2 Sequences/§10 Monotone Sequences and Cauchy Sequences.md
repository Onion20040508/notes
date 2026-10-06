---
type: section
subject: "[[Single Variable Analysis]]"
section: 10
chapter: 2
tags: [real-analysis, math451]
---
← [[§9 Limit Theorems for Sequences]] · ↑ [[· 2 Sequences]] · [[§10a Cauchy Sequences]] →

So far, mainly three ways to determine whether a sequence converges: (1) guess the limit and check the $(\varepsilon, N)$ definition; (2) use basic examples plus the limit theorems and the [[Squeeze Theorem|Squeeze Theorem]]; (3) sometimes, the ratio test. But we need criteria that work *without knowing the value of the limit* — sometimes we need the existence of $\lim s_n$ even when we cannot compute it. In one important case, we can do it.

## Monotone Sequences

> [!definition] Definition §10.1: Monotone Sequences
> A sequence $(s_n)$ is called **increasing** if $s_n \leq s_{n+1}$ for all $n$, and **decreasing** if $s_n \geq s_{n+1}$ for all $n$. It is called **monotone** if it is either increasing or decreasing (the term includes both).

^def-10-1

> [!example] Example §10.1: Monotone or Not
> (1) $s_n = n$ and $s_n = n^2$ are increasing. (2) $s_n = 1 - \tfrac1n$ is also increasing. (3) $s_n = 1 + (-1)^n \tfrac{1}{n^2}$ is *not* monotone — consecutive differences alternate in sign.
>
> What is the difference between (1) and (2)? (1) is increasing but *not bounded above* — and not convergent. (2) is increasing *and bounded* — and converges to $1$.

^ex-10-1

> [!theorem] Theorem §10.1: Monotone Convergence Theorem
> If a sequence $(s_n)$ is monotone and bounded, then it is convergent.

^thm-10-1

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

*Uses:* [[Completeness Axiom|Def. §4.4]], [[Characterization of the Supremum|§4.3]]

![[m451-10-1.svg]]
*The proof in one picture: $s = \sup\{s_n\}$ (blue line) is the least upper bound, at or below any other upper bound $M$. Since $s - \varepsilon$ is not an upper bound, some $s_N$ (red) exceeds it — and because the sequence increases, every later term is trapped in the band between $s - \varepsilon$ and $s$.*

> [!remark]- Connections
> - Computational version: [[§69 Sequences#^thm-69-9|Calc Thm. §69.9]] (with worked examples).

> [!remark] Remark
> Both assumptions are needed. Is there a bounded sequence that is not convergent? Yes: $s_n = (-1)^n$ — the monotone condition is missing. And $s_n = n$ is monotone but unbounded.

^rem-10-1

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

*Uses:* [[Archimedean Property|§4.5]], [[§4 The Completeness Axiom#^def-4-3|Def. §4.3]]

> [!example] Example §10.2: A Recursion with No Formula
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
> **What is the value?** From $s_{n+1} = \sqrt{1 + s_n}$ we get $s_{n+1}^2 = 1 + s_n$. One step deserves care before taking limits (HW): the shifted sequence $(s_{n+1})_n$ converges to the *same* limit $s$ — any $N$ witnessing the definition for $(s_n)$ works for the shift, since $n \geq N$ implies $n + 1 \geq N$. Granting this, the [[§9 Limit Theorems for Sequences#^thm-9-3|product rule]] gives $s_{n+1}^2 \to s^2$ and the sum rule gives $1 + s_n \to 1 + s$, so $s^2 = 1 + s$, i.e. $s^2 - s - 1 = 0$, so
>
> $$
> s = \frac{1 \pm \sqrt{1 + 4}}{2} = \frac{1 \pm \sqrt5}{2} \quad \text{--- two values.}
> $$
>
> *Claim: $s = \tfrac{1 + \sqrt5}{2}$.* Why? The other root is negative, while $s \geq s_1 = 1$. (One can also verify directly that $M = \tfrac{1+\sqrt5}{2}$ works as the upper bound in the induction — for this $M$, $\sqrt{1 + M} = M$ exactly.)

^ex-10-2

![[m451-10-3.svg]]
*The recursion $s_{n+1} = \sqrt{1+s_n}$ as a staircase (red) between the graph $y = \sqrt{1+x}$ (blue) and the diagonal $y = x$: from $s_1 = 1$ the steps climb (the sequence increases) toward the crossing point $\tfrac{1+\sqrt5}{2}$. The bound $M = 2$ propagates because the graph lies below the diagonal at $x = 2$: $\sqrt{1+2} = \sqrt3 < 2$.*

> [!theorem] Theorem §10.3: Unbounded Monotone Sequences
> If $(s_n)$ is increasing but not bounded above, then $\lim s_n = +\infty$. If $(s_n)$ is decreasing but not bounded below, then $\lim s_n = -\infty$.

^thm-10-3

> [!proof]+ Proof
> Check by definition. Let $M > 0$. Since $(s_n)$ is not bounded above, $M$ is not an upper bound: there exists $N$ with $s_N > M$. Since $(s_n)$ is increasing, $s_n \geq s_N > M$ for all $n \geq N$. Hence $s_n \to +\infty$. The decreasing case is symmetric.

^pf-10-3

*Uses:* [[§9 Limit Theorems for Sequences#^def-9-1|Def. §9.1]]

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
> If $(s_n)$ is bounded, these are finite numbers; otherwise we use the values $\pm\infty$ — another place where the extended real numbers ([[§5 The Symbols +∞, −∞|§5]]) are convenient.

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
*The envelopes at work for $s_n = (-1)^n\left(1 + \tfrac2n\right)$: the sequence (dots) has no limit, but the tail-suprema $\overline{s}_N$ (red, decreasing) and tail-infima $\underline{s}_N$ (blue, increasing) are monotone and bounded, so each converges — to $\limsup = 1$ and $\liminf = -1$.*

> [!theorem] Proposition §10.5: Lim Inf Is at Most Lim Sup
> $\displaystyle \liminf_{n\to+\infty} s_n \leq \limsup_{n\to+\infty} s_n$.

^prop-10-5

> [!proof]+ Proof
> Why? Because $\underline{s}_N \leq \overline{s}_N$ for every $N$: the two are the $\inf$ and the $\sup$ of *the same set* $\{s_n \mid n \geq N\}$, and for a nonempty set the infimum is $\leq$ the supremum (both compare with any single element). Passing to the limit in $N$ preserves $\leq$.

^pf-10-5

*Uses:* [[§5 The Symbols +∞, −∞#^prop-5-1|§5.1]], [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]]

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
> We are done. (Alternatively and more directly: $\underline{s}_n \leq s_n \leq \overline{s}_n$ with both outer sequences converging to $s$ — apply the [[Squeeze Theorem|Squeeze Theorem]].)

^pf-10-6

*Uses:* [[§9 Limit Theorems for Sequences#^prop-9-5|§9.5]], [[Squeeze Theorem|§8.1]]

*Cauchy sequences continue in [[§10a Cauchy Sequences]].*
