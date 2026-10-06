---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 15
tags: [functional-analysis, math556]
---
← [[§14 Means and Young's Inequality]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§16 Minkowski's Inequality and the Spaces ℓᵖ]] →

*Stage: norms — Tools. Hölder's inequality, from Young's.*

> [!definition] Definition §15.1: The Sequence Space $\ell$ and the $p$-Norms
> Let $\ell$ denote the set of all infinite sequences $a = (a_1, a_2, \ldots)$ with $a_i \in \mathbb{F}$ ($= \mathbb{R}$ or $\mathbb{C}$). With termwise addition and scalar multiplication, $\ell$ is a linear space. For $a \in \ell$ define
>
> $$
> \|a\|_p = \Bigl( \sum_{i=1}^{\infty} |a_i|^p \Bigr)^{1/p} \quad (1 \le p < \infty), \qquad \|a\|_\infty = \sup_{i} |a_i|,
> $$
>
> with values in $[0, \infty]$.

^def-15-1

> [!remark] Remark
> On all of $\ell$ these are not norms: $\|a\|_p$ may be $+\infty$. They become norms on the subspace where they are finite, which is the space $\ell^p$ (to be [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|defined]] once [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-1|Minkowski's inequality]] is available). The name “$p$-norm” is used in advance, by abuse of language. For $\|\cdot\|_\infty$ the supremum, not the maximum, is needed: an infinite sequence need not attain its largest modulus.

^rem-15-1

> [!definition] Definition §15.2: Conjugate Exponents
> For $1 \le p \le \infty$, the **conjugate exponent** $q$ is defined by
>
> $$
> \frac{1}{p} + \frac{1}{q} = 1, \qquad \text{i.e. } \frac{1}{q} = 1 - \frac{1}{p},
> $$
>
> with the conventions $1/\infty = 0$; so $q = \infty$ when $p = 1$, $q = 1$ when $p = \infty$, and $q = 2$ when $p = 2$. As $p$ ranges over $[1, \infty]$ so does $q$.

^def-15-2

> [!remark]- Connections
> - Same definition in Measure Theory: [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|551 Def. §34.10]] (written $p'$ there).

> [!theorem] Theorem §15.1: Hölder's Inequality for Sequences
> Let $1 \le p \le \infty$ and let $q$ be the conjugate exponent. For all $a = (a_i), b = (b_i) \in \ell$,
>
> $$
> \sum_{i=1}^{\infty} |a_i b_i| \;\le\; \|a\|_p\, \|b\|_q,
> $$
>
> with the convention $0 \cdot \infty = 0$ on the right.
>
> *Lax: §5.1, (19)*

^thm-15-1

For $p = q = 2$ this is the Cauchy–Schwarz inequality (Proposition [[§14 Means and Young's Inequality#^prop-14-1|§14.1]]) for infinite sequences.

> [!proof]+ Proof
> **Case $p = 1$, $q = \infty$.** For every $i$, $|b_i| \le \sup_j |b_j| = \|b\|_\infty$, so
>
> $$
> \sum_{i} |a_i b_i| \le \sum_i |a_i|\, \|b\|_\infty = \|b\|_\infty\, \|a\|_1.
> $$
>
> The case $p = \infty$, $q = 1$ is the same with the roles of $a$ and $b$ exchanged.
>
> **Case $1 < p < \infty$ (so $1 < q < \infty$).** (Lecture 5.)
>
> *Degenerate cases.* If $\|a\|_p = 0$ then every $a_i = 0$, the left side is $0$, and the inequality holds (with the convention $0 \cdot \infty = 0$ if $\|b\|_q = \infty$); likewise if $\|b\|_q = 0$. If $\|a\|_p = \infty$ or $\|b\|_q = \infty$ with the other factor nonzero, the right side is $+\infty$ and there is nothing to prove. So assume
>
> $$
> 0 < \|a\|_p < \infty, \qquad 0 < \|b\|_q < \infty.
> $$
>
> *Normalization.* Put
>
> $$
> a_i' = \frac{a_i}{\|a\|_p}, \qquad b_i' = \frac{b_i}{\|b\|_q}, \qquad a' = (a_i')_{i \ge 1},\ b' = (b_i')_{i \ge 1}.
> $$
>
> Then $\|a'\|_p = \|a\|_p / \|a\|_p = 1$ and $\|b'\|_q = 1$, by homogeneity of the $p$-norms (pull the positive constant out of the sum). Since $\sum_i |a_i b_i| = \|a\|_p \|b\|_q \sum_i |a_i' b_i'|$, it suffices to show
>
> $$
> \sum_{i=1}^\infty |a_i' b_i'| \le 1.
> $$
>
> *Young's inequality termwise.* Set $1 - \theta = 1/p$ and $\theta = 1/q$; these are in $(0,1)$ and sum to $1$ by conjugacy. For each $i$, rewrite
>
> $$
> |a_i' b_i'| = |a_i'|\,|b_i'| = \bigl(|a_i'|^p\bigr)^{1/p} \bigl(|b_i'|^q\bigr)^{1/q} = \bigl(|a_i'|^p\bigr)^{1 - \theta} \bigl(|b_i'|^q\bigr)^{\theta}.
> $$
>
> Young's inequality (Lemma [[§14 Means and Young's Inequality#^lem-14-3|§14.3]], for non-negative $|a_i'|^p$ and $|b_i'|^q$) gives
>
> $$
> |a_i' b_i'| \le (1 - \theta)\,|a_i'|^p + \theta\,|b_i'|^q = \frac{1}{p}|a_i'|^p + \frac{1}{q}|b_i'|^q.
> $$
>
> *Sum.* Summing over $i$ (all terms non-negative, so the sums exist in $[0,\infty]$),
>
> $$
> \sum_{i=1}^\infty |a_i' b_i'| \le \frac{1}{p} \sum_{i=1}^\infty |a_i'|^p + \frac{1}{q} \sum_{i=1}^\infty |b_i'|^q = \frac{1}{p}\,\|a'\|_p^p + \frac{1}{q}\,\|b'\|_q^q = \frac{1}{p} + \frac{1}{q} = 1.
> $$

^pf-15-1

*Uses:* [[§15 Hölder's Inequality for Sequences#^def-15-1|Def. §15.1]], [[§15 Hölder's Inequality for Sequences#^def-15-2|Def. §15.2]], [[§14 Means and Young's Inequality#^lem-14-3|§14.3]]

> [!remark]- Connections
> - The integral version, home of the inequality in the vault: [[Hölder's Inequality|551 §34.5]], proved by the same normalize–Young–integrate argument; in this course [[§17 The Function Spaces Lᵖ(Ω)#^thm-17-1|§17.1]] (cited) and [[§17 The Function Spaces Lᵖ(Ω)#^lem-17-7|§17.7]] (continuous functions, HW3).
> - Used for Minkowski's inequality [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-1|§16.1]] and for the convergence of the $\ell^2$ inner product in [[§20 Definition and Examples#^ex-20-2|Ex. §20.2]].

> [!remark] Remark
> The proof is an “appropriate application of Young”: the normalization makes the right-hand side of Young sum to exactly $1$, and the exponents $p, q$ are chosen so that $|a_i'|^p$ and $|b_i'|^q$ are the two numbers being averaged. The finite-dimensional inequality $\sum_{i=1}^n |a_i b_i| \le \|a\|_p \|b\|_q$ on $\mathbb{R}^n$ or $\mathbb{C}^n$ is the special case of sequences with $a_i = b_i = 0$ for $i > n$. Nothing in the argument needed the sums to be finite in advance; that is why the theorem is stated on all of $\ell$.

^rem-15-2
