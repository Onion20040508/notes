---
type: section
subject: "[[Single Variable Analysis]]"
section: 14
chapter: 2
tags: [real-analysis, math451]
---
← [[§13 Some Topological Concepts in Metric Spaces]] · ↑ [[· 2 Sequences]] · [[§15 Alternating Series and Integral Tests]] →

We know how to add up finitely many numbers:

$$
a_1 + a_2, \qquad a_1 + a_2 + a_3, \qquad a_1 + \cdots + a_n = \sum_{k=1}^n a_k
$$

— the $\Sigma$-notation being convenient, e.g. $\sum_{k=4}^{9} a_k = a_4 + a_5 + a_6 + a_7 + a_8 + a_9$.

**Question:** can we add up *infinitely* many numbers, $a_1 + \cdots + a_n + \cdots$? People started thinking about this a long time ago; at the beginning, they thought it was impossible — Zeno's paradox of Achilles and the tortoise. A long time later, it became clear. That is what we do now. Three test examples to keep in mind:

$$
\text{(1)} \quad 1 + 1 + 1 + \cdots \qquad
\text{(2)} \quad 1 + \frac12 + \frac1{2^2} + \frac1{2^3} + \cdots \qquad
\text{(3)} \quad 1 + \frac12 + \frac13 + \frac14 + \cdots
$$

Does each sum to a finite number? Example (2) is what resolves Zeno's paradox; in example (3) we are adding terms that become smaller and smaller — does that suffice?

> [!definition] Definition §14.1: Series and Partial Sums
> An **infinite series** (or a **series**) is an infinite sum
>
> $$
> a_1 + a_2 + \cdots = \sum_{n=1}^{\infty} a_n, \qquad a_n \in \mathbb{R}
> $$
>
> (it can also start at any index $m$: $\sum_{n=m}^\infty a_n$; we concentrate on $m = 1$). Its **partial sums** are
>
> $$
> s_n = \sum_{k=1}^{n} a_k,
> $$
>
> which form a sequence $(s_n)$.

^def-14-1

> [!definition] Definition §14.2: Convergence of a Series
> If the sequence $(s_n)$ of partial sums converges to a limit $s$, we say the series $\sum_{n=1}^\infty a_n$ **converges** to $s$ and write $\sum_{n=1}^\infty a_n = s$. If $(s_n)$ diverges, we say the series **diverges**; in the special case $s_n \to +\infty$ we say the series diverges to $+\infty$ and write $\sum_{n=1}^\infty a_n = +\infty$.

^def-14-2

> [!remark]- Connections
> - Computational version: [[§61 Convergence of Series#^def-61-1|342 Def. §61.1]] (series of complex numbers), reduced to real series by [[§61 Convergence of Series#^thm-61-1|342 Thm. §61.1]].

> [!remark] Remark: Why Is This Definition Reasonable?
> Only *finite* sums are defined by the field operations of $\mathbb{R}$. An infinite sum must therefore be *defined* in terms of finite ones — and the natural way is as the limit of the finite approximations $s_n$, using the machinery of Chapter 2. This is also why series appear as a section of the chapter on sequences: a series *is* a sequence, namely its sequence of partial sums.

^rem-14-1

> [!example] Example §14.1: The Three Test Examples
> **(1)** $a_n = 1$: then $s_n = n \to +\infty$, so $\sum_{n=1}^\infty 1 = +\infty$.
>
> **(2)** $a_n = \dfrac{1}{2^{n-1}}$: the partial sum is a geometric sum,
>
> $$
> s_n = 1 + \frac12 + \cdots + \frac{1}{2^{n-1}} = \frac{1 - 2^{-n}}{1 - \tfrac12} = 2\left(1 - 2^{-n}\right).
> $$
>
> Is $(s_n)$ convergent? Yes: $2^{-n} \to 0$, so $\lim s_n = 2$, and
>
> $$
> \sum_{n=1}^\infty \frac{1}{2^{n-1}} = 2.
> $$
>
> The series converges — Achilles does catch the tortoise.
>
> **(3)** $a_n = \dfrac1n$ (the *harmonic series*): now
>
> $$
> s_n = 1 + \frac12 + \frac13 + \cdots + \frac1n,
> $$
>
> and we cannot find a closed formula — the situation is more complicated. We will need some tricks or theorems to show that in fact $s_n \to +\infty$: the harmonic series *diverges*, even though its terms tend to $0$.

^ex-14-1

![[m451-14-2.svg]]
*Example (2) as Zeno's walk: each term covers half of the remaining distance to $2$, so the partial sums $s_n = 2(1 - 2^{-n})$ march toward $2$ while the gap $2 - s_n = 2^{1-n}$ halves at every step (shown: $2 - s_3 = \tfrac14$).*

## The Cauchy Criterion for Series

For the harmonic series we cannot find a closed formula for $s_n$, so we need to study general properties of series. Since a series *is* the sequence of its partial sums, every convergence criterion for sequences transfers.

> [!definition] Definition §14.3: Cauchy Criterion
> A series $\sum a_n$ is said to satisfy the **Cauchy criterion** if its sequence $(s_n)$ of partial sums is a Cauchy sequence. Explicitly, since for $m \geq n$
>
> $$
> s_m - s_{n-1} = a_n + a_{n+1} + \cdots + a_m,
> $$
>
> the criterion reads: for any $\varepsilon > 0$ there exists $N$ such that for all $m \geq n \geq N$,
>
> $$
> |a_n + a_{n+1} + \cdots + a_m| < \varepsilon.
> $$

^def-14-3

> [!theorem] Theorem §14.1: Cauchy Criterion for Series
> A series $\sum a_n$ converges if and only if it satisfies the Cauchy criterion.

^thm-14-1

> [!proof]+ Proof
> This is exactly the Cauchy condition for the convergence of the sequence $(s_n)$ (§10): convergent $\iff$ Cauchy.

^pf-14-1

*Uses:* [[§14 Series#^def-14-3|Def. §14.3]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-7|§10.7]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-8|§10.8]]

> [!theorem] Corollary §14.2: Terms of a Convergent Series Tend to Zero
> If $\sum a_n$ converges, then $a_n \to 0$.

^cor-14-2

> [!proof]+ Proof
> Take $m = n$ in the Cauchy criterion: for $n \geq N$, $|a_n| < \varepsilon$.

^pf-14-2

*Uses:* [[§14 Series#^thm-14-1|§14.1]]

> [!remark]- Connections
> - Its logic in 250: [[§2 Implications#^ex-2-10|250 Ex. §2.10]] (a necessary condition; the contrapositive is the divergence test; the converse fails).
> - Computational version: [[§70 Series#^thm-70-4|Calc Thm. §70.4]] and the Test for Divergence, [[§70 Series#^cor-70-5|Calc Cor. §70.5]] (with worked examples).
> - Computational version: [[§61 Convergence of Series#^cor-61-2|342 Cor. §61.2]] (the same statement for complex series).

> [!theorem] Proposition §14.3: Linearity of Series
> If $\sum a_n$ and $\sum b_n$ converge and $c \in \mathbb{R}$, then
>
> $$
> \sum_{n=1}^\infty (a_n + b_n) = \sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n
> \qquad \text{and} \qquad
> \sum_{n=1}^\infty c\,a_n = c \sum_{n=1}^\infty a_n.
> $$

^prop-14-3

> [!proof]+ Proof
> The partial sums obey $\sum_{k=1}^n (a_k + b_k) = s_n + t_n$ and $\sum_{k=1}^n c\,a_k = c\,s_n$ exactly (finite sums); now apply the limit theorems of §9 to the sequences $(s_n)$, $(t_n)$.

^pf-14-3

*Uses:* [[§9 Limit Theorems for Sequences#^thm-9-2|§9.2]], [[§9 Limit Theorems for Sequences#^thm-9-3|§9.3]]

> [!theorem] Corollary §14.4: Convergent Plus Divergent Is Divergent (HW)
> If $\sum a_n$ converges and $\sum b_n$ diverges, then $\sum (a_n + b_n)$ diverges.

^cor-14-4

> [!proof]+ Proof
> If $\sum(a_n + b_n)$ converged, then by linearity $\sum b_n = \sum\bigl((a_n + b_n) - a_n\bigr)$ would converge — contradiction.

^pf-14-4

*Uses:* [[§14 Series#^prop-14-3|§14.3]]

> [!remark] Remark
> No conclusion holds for divergent plus divergent: $\sum \tfrac1n$ and $\sum\bigl(-\tfrac1n\bigr)$ both diverge, yet their sum is $\sum 0 = 0$. Typical use of the corollary: $\sum \tfrac{n-1}{n^2} = \sum\bigl( \tfrac1n - \tfrac1{n^2} \bigr)$ diverges, being (divergent harmonic) plus (convergent p-series with the sign flipped).

^rem-14-2

> [!remark] Remark: Warning
> The converse is **not** true: $a_n \to 0$ does not imply that $\sum a_n$ converges. The counterexample is the harmonic series $\sum \tfrac1n$, as we now show.

^rem-14-3

> [!theorem] Theorem §14.5: Divergence of the Harmonic Series
> $\displaystyle\sum_{n=1}^{\infty} \frac1n = +\infty$, even though $\tfrac1n \to 0$.

^thm-14-5

> [!proof]+ Proof
> We show $s_n \to +\infty$ directly. First note $(s_n)$ is *increasing* — we add a positive amount at every step: $s_{n+1} = s_n + \tfrac{1}{n+1}$. Therefore it suffices to show that some *subsequence* $s_{n_k} \to +\infty$ (an increasing sequence dominates its earlier terms, so the whole sequence follows its subsequence upward; for general sequences this implication fails!).
>
> Try $n_k = 2^k$, dividing the sum into dyadic segments. Experiments first:
>
> $$
> s_{2} = 1 + \frac12 > \frac12, \qquad
> s_{4} = 1 + \frac12 + \left(\frac13 + \frac14\right) > \frac12 + \left(\frac14 + \frac14\right) = \frac12 \cdot 2,
> $$
>
> $$
> s_{8} = s_4 + \left(\frac15 + \frac16 + \frac17 + \frac18\right) > \frac12\cdot 2 + \left(\frac18 \cdot 4\right) = \frac12 \cdot 3.
> $$
>
> In general, the segment from $\tfrac{1}{2^{k-1}+1}$ to $\tfrac{1}{2^k}$ has $2^k - 2^{k-1} = 2^{k-1}$ terms, each $\geq \tfrac{1}{2^k}$, so the segment sums to at least
>
> $$
> \frac{1}{2^k} \cdot 2^{k-1} = \frac12.
> $$
>
> By induction, using $s_{2^{k-1}} > \tfrac12 (k-1)$, we get
>
> $$
> s_{2^k} > \frac12\, k.
> $$
>
> Hence $s_{2^k} \to +\infty$, and therefore $s_n \to +\infty$. This proof is a bit tricky; we will have more systematic proofs later (the integral test, §15).

^pf-14-5

![[m451-14-1.svg]]
*The dyadic estimate as areas: term $n$ is a bar of area $\tfrac1n$ on $[n-1, n]$ (term $1$ gray). Under each block of terms $(2^k, 2^{k+1}]$ sits a red dashed box of height $\tfrac{1}{2^{k+1}}$ (the block's smallest term) and width $2^k$ — area exactly $\tfrac12$. Every bar reaches at least its box's roof, so each block sums to at least $\tfrac12$, and the partial sums gain half a unit per block, forever.*

> [!remark]- Connections
> - Used in [[§2 Implications#^ex-2-10|250 Ex. §2.10]](c) as the counterexample to the converse of [[§14 Series#^cor-14-2|Corollary §14.2]].
> - Computational version: [[§70 Series#^thm-70-3|Calc Thm. §70.3]].

## Absolute Convergence

> [!definition] Definition §14.4: Absolute Convergence
> Given a series $\sum a_n$: if the series $\sum_{n=1}^\infty |a_n|$ converges, we say $\sum a_n$ **converges absolutely**.

^def-14-4

> [!remark]- Connections
> - Computational version: [[§73 Alternating Series and Absolute Convergence#^def-73-2|Calc Def. §73.2]] (with worked examples).
> - Computational version: [[§61 Convergence of Series#^def-61-2|342 Def. §61.2]] (absolute convergence of complex series).

> [!theorem] Proposition §14.6: Absolute Convergence Implies Convergence
> If $\sum a_n$ converges absolutely, then it converges.

^prop-14-6

> [!proof]+ Proof
> The only available proof is via the Cauchy criterion — we cannot use the $(\varepsilon,N)$ definition directly, since we do not know the value of $\sum a_n$. Since $\sum |a_n|$ converges, it satisfies the Cauchy criterion: for any $\varepsilon > 0$ there is $N$ with
>
> $$
> |a_n| + \cdots + |a_m| < \varepsilon \qquad (m \geq n \geq N).
> $$
>
> *Claim:* this implies $\sum a_n$ satisfies the Cauchy criterion too. Why? The [[§3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]]:
>
> $$
> |a_n + \cdots + a_m| \leq |a_n| + \cdots + |a_m| < \varepsilon.
> $$
>
> Hence $\sum a_n$ converges.

^pf-14-6

*Uses:* [[§14 Series#^thm-14-1|§14.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|§3.3]]

> [!remark]- Connections
> - Computational version: [[§61 Convergence of Series#^cor-61-3|342 Cor. §61.3]] (complex series, via real and imaginary parts).

> [!remark] Remark: Warning
> The converse is not true. The example to keep in mind: $a_n = (-1)^n \tfrac1n$. This series does *not* converge absolutely — $\sum |(-1)^n \tfrac1n| = \sum \tfrac1n$ diverges — but we will show in §15 that $\sum (-1)^n \tfrac1n$ *does* converge.

^rem-14-4

> [!remark]- Connections
> - The same principle for series of functions: a series with $\sum \|f_k\|_p < \infty$ converges a.e. to a function in $L^p$, [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-14|551 Cor. §19.14]] (for $p = 1$: [[§15 The General Lebesgue Integral#^cor-15-9|551 Cor. §15.9]]).
> - Computational version: [[§73 Alternating Series and Absolute Convergence#^thm-73-3|Calc Thm. §73.3]] (with worked examples).

## The Comparison Test

> [!theorem] Theorem §14.7: Comparison Test
> 1. Assume $a_n \geq 0$ and $|b_n| \leq a_n$ for all $n$. If $\sum a_n$ converges, then $\sum b_n$ converges (absolutely).
>
> 2. Assume $a_n \geq 0$ and $b_n \geq a_n$ for all $n$. If $\sum a_n$ diverges, then $\sum b_n$ diverges.

^thm-14-7

> [!proof]+ Proof
> (1) By the Cauchy criterion for $\sum a_n$ and
>
> $$
> |b_n| + \cdots + |b_m| \leq a_n + \cdots + a_m < \varepsilon,
> $$
>
> the series $\sum |b_n|$ is Cauchy, hence converges; so $\sum b_n$ converges absolutely, and hence converges.
>
> (2) Let $s_n = \sum_{k=1}^n a_k$ and $t_n = \sum_{k=1}^n b_k$. Then $t_n \geq s_n$ for all $n$. Since $a_n \geq 0$, the sequence $(s_n)$ is increasing, and divergence means $s_n \to +\infty$ (§10: an increasing sequence either converges or tends to $+\infty$). By the squeezing-to-infinity lemma (§9), $t_n \to +\infty$, so $\sum b_n$ diverges.

^pf-14-7

*Uses:* [[§14 Series#^thm-14-1|§14.1]], [[§14 Series#^prop-14-6|§14.6]], [[Monotone Convergence Theorem|§10.1]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-3|§10.3]], [[§9 Limit Theorems for Sequences#^lem-9-7|§9.7]]

> [!remark]- Connections
> - Computational version: [[§72 The Comparison Tests#^thm-72-1|Calc Thm. §72.1]] (with worked examples).
> - Used in ODEs: comparison with $\sum_k (nK|t|)^k/k!$ shows that every entry of the matrix exponential $e^{\mathbf{A}t}$ converges, [[§33★ Fundamental Matrices#^thm-33-3|331 Thm. §33.3]].

> [!theorem] Proposition §14.8: Bounded Multipliers Preserve Absolute Convergence (HW)
> If $\sum |a_n|$ converges and $(b_n)$ is a bounded sequence, then $\sum a_n b_n$ converges — absolutely, in fact.

^prop-14-8

> [!proof]+ Proof
> Let $|b_n| \leq M$ for all $n$. Then $|a_n b_n| \leq M |a_n|$, and $\sum M|a_n|$ converges; the comparison test finishes.

^pf-14-8

*Uses:* [[§14 Series#^thm-14-7|§14.7]]

> [!remark] Remark
> Three remarks. (1) Taking $b_n \equiv 1$ recovers “absolute convergence implies convergence” — the proposition above becomes a special case. (2) This is the series analogue of the sequence fact “null times bounded is null” (§8). (3) It is also the germ of the *[[§25 More on Uniform Convergence#^thm-25-3|Weierstrass M-test]]* of §25: there, $a_n$ becomes a convergent numerical majorant $M_n$ and $b_n$ a bounded family of function values, and the Cauchy-tail estimate $\left|\sum_{k=n+1}^m a_k b_k\right| \leq M \sum_{k=n+1}^m |a_k|$ — an equally valid proof of this proposition — reappears verbatim as the M-test's proof.

^rem-14-5

> [!example] Example §14.2: Making the Comparison Go the Right Way
> Decide whether $\displaystyle\sum_{n=1}^{\infty} \frac{n}{n^2+2}$ converges or diverges.
>
> *Guess first:* the term is comparable to $\tfrac{n}{n^2} = \tfrac1n$, so it should diverge. But
>
> $$
> \frac{n}{n^2+2} < \frac{n}{n^2} = \frac1n,
> $$
>
> and a direct comparison with the divergent $\sum\tfrac1n$ goes the *wrong way* — being below a divergent series proves nothing. Instead bound from *below*: for $n \geq 2$ (so that $n^2 \geq 2$),
>
> $$
> \frac{n}{n^2+2} \geq \frac{n}{n^2+n^2} = \frac{1}{2n}.
> $$
>
> Now $\sum \tfrac{1}{2n}$ diverges (scalar multiple of the harmonic series), so by comparison (2), our series diverges. Done!

^ex-14-2

To use the comparison test, we need a stock of basic series.

> [!example] Example §14.3: The p-Series
> For $p > 0$, the series
>
> $$
> \sum_{n=1}^\infty \frac{1}{n^p} \qquad \text{converges if and only if} \qquad p > 1.
> $$
>
> We proved divergence for $p = 1$; hence for $p < 1$ divergence follows by comparison, since $\tfrac{1}{n^p} \geq \tfrac1n$ when $p \leq 1$. The convergence for $p > 1$ will be proved by the integral test in §15. (The dyadic-block argument for the harmonic series was itself secretly a comparison — we compared each block with a constant block from below.)

^ex-14-3

> [!remark]- Connections
> - Computational version: the p-series by the Integral Test, [[§71 The Integral Test and Estimates of Sums#^thm-71-2|Calc Thm. §71.2]] (with worked examples).

> [!example] Example §14.4: The Geometric Series
> For $a \in \mathbb{R}$, the geometric series $\sum_{n=0}^\infty a^n$ converges if and only if $|a| < 1$, with
>
> $$
> \sum_{n=0}^\infty a^n = \frac{1}{1-a}, \qquad |a| < 1.
> $$
>
> Indeed $s_n = \tfrac{1 - a^{n+1}}{1 - a} \to \tfrac{1}{1-a}$ since $a^{n+1} \to 0$; while for $|a| \geq 1$ the terms do not tend to $0$, so the series diverges by the corollary above. This is the basic series against which the next two tests compare.

^ex-14-4

> [!remark]- Connections
> - Computational version: [[§70 Series#^thm-70-1|Calc Thm. §70.1]] (with worked examples).

## The Ratio and Root Tests

> [!theorem] Theorem §14.9: Ratio Test for Series
> Let $\sum a_n$ be a series with $a_n \neq 0$.
>
> 1. If $\limsup \left| \tfrac{a_{n+1}}{a_n} \right| < 1$, then $\sum a_n$ converges absolutely.
>
> 2. If $\liminf \left| \tfrac{a_{n+1}}{a_n} \right| > 1$, then $\sum a_n$ diverges.
>
> 3. If $\liminf \left| \tfrac{a_{n+1}}{a_n} \right| \leq 1 \leq \limsup \left| \tfrac{a_{n+1}}{a_n} \right|$: no information.
>
> Note the change from $\limsup$ (for convergence) to $\liminf$ (for divergence) — using $\limsup$ and $\liminf$, no assumption that the ratio has a limit is needed.

^thm-14-9

> [!proof]+ Proof
> We compare with the geometric series.
>
> (1) Pick $a$ with $\limsup |a_{n+1}/a_n| < a < 1$. Since the tail-sups decrease to the $\limsup$, there exists $N$ with $\sup_{n \geq N} |a_{n+1}/a_n| < a$, i.e.
>
> $$
> |a_{n+1}| < a\, |a_n| \qquad \text{for all } n \geq N.
> $$
>
> By induction, $|a_n| \leq a^{n-N} |a_N|$ for $n \geq N$. The series $\sum_n a^{n-N}|a_N|$ is a convergent geometric series ($0 < a < 1$), so $\sum |a_n|$ converges by comparison: $\sum a_n$ converges absolutely.
>
> (2) Pick $b$ with $\liminf |a_{n+1}/a_n| > b > 1$. Since the tail-infs increase to the $\liminf$, there exists $N$ with $|a_{n+1}| > b |a_n| > |a_n|$ for all $n \geq N$. Then $|a_n| \geq |a_N| > 0$ for all $n \geq N$, so $a_n \not\to 0$, and the series diverges by the corollary (terms of a convergent series tend to $0$).
>
> (3) Both $\sum \tfrac1n$ (divergent) and $\sum \tfrac1{n^2}$ (convergent) have ratio $\to 1$.

^pf-14-9

*Uses:* [[§14 Series#^ex-14-4|Ex. §14.4]], [[§14 Series#^thm-14-7|§14.7]], [[§14 Series#^cor-14-2|§14.2]], [[§10 Monotone Sequences and Cauchy Sequences#^lem-10-4|§10.4]]

> [!remark]- Connections
> - Computational version: [[§74 The Ratio and Root Tests#^thm-74-1|Calc Thm. §74.1]] (with worked examples).

> [!theorem] Theorem §14.10: Root Test
> Let $r = \limsup_{n\to\infty} |a_n|^{1/n}$.
>
> 1. If $r < 1$, then $\sum a_n$ converges absolutely.
>
> 2. If $r > 1$, then $\sum a_n$ diverges.
>
> 3. If $r = 1$: no information.

^thm-14-10

> [!proof]+ Proof
> (1) Pick $a$ with $r < a < 1$. As above, there is $N$ with $|a_n|^{1/n} < a$, i.e. $|a_n| < a^n$, for all $n \geq N$; compare with the geometric series $\sum a^n$.
>
> (2) If $r > 1$, then $|a_n|^{1/n} > 1$ — i.e. $|a_n| > 1$ — for infinitely many $n$ (a tail with all $|a_n|^{1/n} \leq 1$ would force $r \leq 1$). So $a_n \not\to 0$ and the series diverges.
>
> (3) The same pair $\sum \tfrac1n$, $\sum \tfrac1{n^2}$: in both cases $|a_n|^{1/n} \to 1$ (using $n^{1/n} \to 1$ from §9).

^pf-14-10

*Uses:* [[§14 Series#^ex-14-4|Ex. §14.4]], [[§14 Series#^thm-14-7|§14.7]], [[§14 Series#^cor-14-2|§14.2]], [[§9 Limit Theorems for Sequences#^ex-9-4|Ex. §9.4]]

> [!remark]- Connections
> - Computational version: [[§74 The Ratio and Root Tests#^thm-74-2|Calc Thm. §74.2]] (with worked examples).

> [!example] Example §14.5: Three Quick Applications
> Decide convergence or divergence, by any means:
>
> 1. $\displaystyle\sum \frac{3^n}{n^2}$: diverges — the terms $\to +\infty$ (growth scale, §9); or ratio test: $\left|\tfrac{a_{n+1}}{a_n}\right| = 3 \left( \tfrac{n}{n+1} \right)^2 \to 3 > 1$.
>
> 2. $\displaystyle\sum \frac{n^2}{3^n}$: converges absolutely — ratio $\tfrac13 \left( \tfrac{n+1}{n} \right)^2 \to \tfrac13 < 1$.
>
> 3. $\displaystyle\sum \frac{3^n}{n!}$: converges absolutely — ratio $\tfrac{3}{n+1} \to 0 < 1$.

^ex-14-5
