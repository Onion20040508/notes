---
subject: "[[Single Variable Analysis]]"
section: 11
chapter: 2
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §10 Monotone Sequences and Cauchy Sequences]] · ↑ [[Single Variable Analysis — 2 Sequences]] · [[Single Variable Analysis §12 Lim Sup and Lim Inf Continued (Skipped)]] →

We now want to understand the structure of sequences better. Recall: monotone $+$ bounded $\implies$ convergent, and both conditions are needed. If we remove boundedness, we still know what happens: an unbounded increasing sequence tends to $+\infty$, an unbounded decreasing one to $-\infty$. But what can we say about a *bounded* sequence that is not monotone?

Consider $s_n = (-1)^n$, bounded but not convergent. All *even* terms $s_{2n} = 1$ form a convergent sequence; all *odd* terms $s_{2n+1} = -1$ form another. These are examples of *subsequences* — picking out only some of the terms.

> [!definition] Definition §11.1: Subsequence
> Given a sequence $(s_n)$, a **subsequence** is a sequence $(t_k)$ of the form
>
> $$
> t_k = s_{n_k}, \qquad \text{where} \quad n_1 < n_2 < n_3 < \cdots.
> $$
>
> Usually we denote it by $(s_{n_k})$. Note that $n_k \to +\infty$ as $k \to +\infty$; in fact $n_k \geq k$ for all $k$ (by induction: $n_1 \geq 1$, and $n_{k+1} > n_k \geq k$ forces $n_{k+1} \geq k+1$).

^def-11-1

> [!example] Example §11.1: Subsequences of simple sequences
> For $s_n = n$: the even terms $(2k)$, the squares $(k^2)$, the primes, … are all subsequences. For $s_n = 1 + (-1)^n \tfrac1n$: the sequence is not monotone, but the even-indexed subsequence $1 + \tfrac{1}{2k}$ is decreasing and the odd-indexed one $1 - \tfrac{1}{2k+1}$ is increasing — monotone subsequences extracted from a non-monotone sequence.

^ex-11-1

> [!theorem] Theorem §11.1: Subsequences of a Convergent Sequence
> If $(s_n)$ converges, then every subsequence $(s_{n_k})$ also converges, to the same limit.

^thm-11-1

> [!proof]+ Proof
> Let $s = \lim s_n$. We must show: for any $\varepsilon > 0$ there exists $K$ such that $|s_{n_k} - s| < \varepsilon$ for $k \geq K$. By definition, there exists $N$ such that $|s_n - s| < \varepsilon$ for $n \geq N$. Since $n_k$ is strictly increasing and diverges to $+\infty$, there exists $K$ such that $n_k \geq N$ for all $k \geq K$; hence $|s_{n_k} - s| < \varepsilon$ for such $k$. (More directly: since $n_k \geq k$, we can simply take $K = N$.)

^pf-11-1

> [!theorem] Corollary §11.2: A Divergence Criterion
> If $(s_n)$ has two convergent subsequences converging to *different* limits, then $(s_n)$ does not converge.

^cor-11-2

> [!proof]+ Proof
> By contradiction: if $s_n \to s$, then by the theorem *every* convergent subsequence converges to $s$ — the two different limits would both equal $s$.

^pf-11-2

Two useful strengthenings, both needed silently in arguments that “pass to a further subsequence”:

> [!theorem] Proposition §11.3: Subsequences of Subsequences (HW)
> A subsequence of a subsequence of $(s_n)$ is itself a subsequence of $(s_n)$.

^prop-11-3

> [!proof]+ Proof
> Let $(t_k) = (s_{n_k})$ be a subsequence of $(s_n)$, and $(u_j) = (t_{k_j})$ a subsequence of $(t_k)$. Then
>
> $$
> u_j = t_{k_j} = s_{n_{k_j}},
> $$
>
> and the index map $j \mapsto n_{k_j}$ is strictly increasing: $j_1 < j_2$ gives $k_{j_1} < k_{j_2}$ ($(k_j)$ strictly increasing), which gives $n_{k_{j_1}} < n_{k_{j_2}}$ ($(n_k)$ strictly increasing). So $(u_j)$ is a subsequence of $(s_n)$ with indices $n_{k_j}$. (In functional language: a subsequence is a composition $s \circ \sigma$ with $\sigma: \mathbb{N} \to \mathbb{N}$ strictly increasing, and the composition $\sigma \circ \rho$ of two strictly increasing maps is strictly increasing.)

^pf-11-3

> [!theorem] Proposition §11.4: Subsequences and Infinite Limits (HW)
> If $s_n \to +\infty$, then every subsequence $(s_{n_k})$ also satisfies $s_{n_k} \to +\infty$; similarly for $-\infty$.

^prop-11-4

> [!proof]+ Proof
> Given $M$, there is $N$ with $s_n > M$ for $n > N$. Since $n_k \geq k$ (proved with the definition), for all $k > N$ we have $n_k \geq k > N$, hence $s_{n_k} > M$. The case $-\infty$ is symmetric.

^pf-11-4

> [!remark] Remark
> The converse of the theorem fails: convergence of *a* subsequence does not imply convergence of the sequence — $s_n = (-1)^n$ again.

^rem-11-1

## The Bolzano–Weierstrass Theorem

The goal of this section:

> [!theorem] Theorem §11.5: Bolzano–Weierstrass
> Every bounded sequence $(s_n)$ has a convergent subsequence.

^thm-11-5

This is what the example $s_n = (-1)^n$ leads us to expect.

> [!proof]+ Proof
> (This proof is different from the book's.) Since $(s_n)$ is bounded, the tail-sup sequence $(\overline{s}_N)$ is also bounded, so
>
> $$
> \overline{s} = \limsup_{n\to\infty} s_n = \lim_{N\to\infty} \overline{s}_N
> $$
>
> is finite. We extract a subsequence converging to $\overline{s}$.
>
> Fix $k \geq 1$ and use $\varepsilon = \tfrac1k$. Since $\overline{s}_N \downarrow \overline{s}$ (decreasing, §10), for every sufficiently large $n'$,
>
> $$
> \overline{s} \leq \overline{s}_{n'} \leq \overline{s} + \frac1k,
> $$
>
> and by monotonicity this holds for *all larger* $n'$ as well — so we may take $n'$ as large as we wish. Since $\overline{s}_{n'} = \sup\{s_n \mid n \geq n'\}$, the [[Characterization of the Supremum|characterization of the supremum]] gives some index $N' \geq n'$ with
>
> $$
> s_{N'} \geq \overline{s}_{n'} - \frac1k.
> $$
>
> Combining the two displays,
>
> $$
> \overline{s} - \frac1k \leq \overline{s}_{n'} - \frac1k \leq s_{N'} \leq \overline{s}_{n'} \leq \overline{s} + \frac1k.
> $$
>
> Now do induction on $k$. For $k = 1$, get $n_1 = N'$. For $k = 2$, repeat the construction with $n'$ chosen *bigger than $n_1$* — this is important, and possible by the freedom in choosing $n'$ noted above — to get $n_2 = N' > n_1$. And so on. We obtain a subsequence $(s_{n_k})$ satisfying
>
> $$
> \overline{s} - \frac1k \leq s_{n_k} \leq \overline{s} + \frac1k,
> $$
>
> and therefore $s_{n_k} \to \overline{s}$ by the [[Squeeze Theorem|Squeeze Theorem]].
>
> We could equally start with $\underline{s} = \liminf s_n$ and get another subsequence converging to it.

^pf-11-5

## Subsequence Limits

> [!definition] Definition §11.2: Subsequence Limit
> Given a sequence $(s_n)$, a **subsequence limit** is any extended real number (including $\pm\infty$) that is the limit of some subsequence $(s_{n_k})$. We write $S$ for the set of all subsequence limits of $(s_n)$.

^def-11-2

> [!example] Example §11.2: Two subsequence limits
> For $s_n = (-1)^n$: $\overline{s} = 1$ and $\underline{s} = -1$, and $S = \{1, -1\}$ — there are no other subsequence limits, by the argument in the next example.

^ex-11-2

> [!example] Example §11.3: A limit at infinity
> Let $s_n = e^{(-1)^n n}$. Find all subsequence limits. The even terms $e^{2k} \to +\infty$; the odd terms $e^{-(2k+1)} \to 0$. So $0, +\infty \in S$. *Why no more?* Every subsequence must contain infinitely many terms from at least one of these two special subsequences. A *convergent* (in $[-\infty,+\infty]$) subsequence must contain infinitely many from *only one* of them — otherwise it contains two sub-subsequences with the different limits $0$ and $+\infty$, contradicting the subsequence theorem — invoked here through both HW lemmas above: a sub-subsequence *is* a subsequence of the original, and the theorem extends to the limit $+\infty$. And a subsequence drawing infinitely many terms from only one of the two behaves like that one. Hence $S = \{0, +\infty\}$.

^ex-11-3

> [!example] Example §11.4: All of an interval
> The set of rational numbers in $[0,1]$ is countable (§2); make a list $(s_n)$ of them. Then $S = [0,1]$.
>
> Two things to prove. *Every subsequence limit belongs to $[0,1]$:* all terms lie in $[0,1]$, and limits preserve the inequalities $0 \leq s_{n_k} \leq 1$. *Every $x \in [0,1]$ is a subsequence limit*, by the density of $\mathbb{Q}$ in $\mathbb{R}$ (§4): for each $k$, the interval $(x - \tfrac1k,\, x + \tfrac1k) \cap [0,1]$ contains infinitely many rationals, hence contains terms $s_n$ with $n$ arbitrarily large; choose inductively $n_k > n_{k-1}$ with $|s_{n_k} - x| < \tfrac1k$. Then $s_{n_k} \to x$.

^ex-11-4

> [!example] Example §11.5: Designing the set of subsequence limits
> Produce a sequence whose set of subsequence limits is $[0, \tfrac12] \cup \{1\}$. List all rational numbers in $[0, \tfrac12]$ as the odd terms $s_{2n+1}$, and define all even terms $s_{2n} = 1$. By the arguments above, the odd part contributes exactly $[0, \tfrac12]$ and the even part contributes $\{1\}$.

^ex-11-5

> [!theorem] Theorem §11.6: Structure of the Set of Subsequence Limits
> For any sequence $(s_n)$, with $S$ its set of subsequence limits (in $[-\infty, +\infty]$):
>
> 1. $S$ is nonempty;
>
> 2. $\sup S = \limsup_{n\to\infty} s_n$ and $\inf S = \liminf_{n\to\infty} s_n$;
>
> 3. if $(s_n)$ is bounded, then $\max S$ exists and equals $\sup S$, and $\min S$ exists and equals $\inf S$.
>
> In particular, if $\limsup s_n = \liminf s_n$, then $S$ consists of a single element — all convergent subsequences have the same limit.

^thm-11-6

> [!proof]+ Proof
> (1) If $(s_n)$ is bounded, the [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass]] proof puts $\limsup s_n$ (and $\liminf s_n$) in $S$ already. If $(s_n)$ is not bounded — say not bounded above — then every tail is unbounded above, so we may choose inductively $n_1 < n_2 < \cdots$ with $s_{n_k} > k$; this subsequence tends to $+\infty$, so $+\infty \in S$. (Similarly $-\infty \in S$ if unbounded below.)
>
> (2) We show $\limsup s_n$ is an upper bound of $S$. Let $s_0 \in S$, with subsequence $s_{n_k} \to s_0$. For every $k$, the term $s_{n_k}$ belongs to the tail starting at $n_k$, so
>
> $$
> s_{n_k} \leq \overline{s}_{n_k}.
> $$
>
> Now $(\overline{s}_{n_k})_k$ is a subsequence of $(\overline{s}_N)_N$, which converges to $\limsup s_n$ — so it converges to the same limit (subsequence theorem; this answers the “why”). Passing to the limit in the inequality,
>
> $$
> s_0 = \lim_k s_{n_k} \leq \lim_k \overline{s}_{n_k} = \limsup_{n\to\infty} s_n.
> $$
>
> So $\limsup s_n$ is an upper bound of $S$. Why is it *equal* to $\sup S$? Because it happens to *belong* to $S$ — that is the content of the Bolzano–Weierstrass construction (and of (1) in the unbounded case, where $\limsup s_n = +\infty$). An upper bound that lies in the set is its supremum — and its maximum. Similarly $\inf S = \liminf s_n$, attained as $\min S$; this also proves (3).

^pf-11-6

> [!remark] Remark
> Using terms from topology (next section): $S$ is always a *closed* subset of $\mathbb{R}$. Hence $S$ can never be, e.g., an open interval $(0,1)$; but $[0,1]$ or $[0,\tfrac12] \cup \{1\}$ are fine, as the examples showed.

^rem-11-2
