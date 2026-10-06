---
type: section
subject: "[[Measure Theory]]"
chapter: 6
section: 35
tags: [measure-theory, math551]
---
← [[§34 Normed Linear Spaces and Lᵖ Spaces]] · ↑ [[· 6 Lᵖ Spaces]] · [[§36 Power Singularities 1∕xᵃ and ℚ]] →

Minkowski's inequality makes $\|\cdot\|_p$ a norm, the [[Riesz–Fischer Theorem|Riesz–Fischer theorem]] makes $L^p(E)$ complete, so that $(L^p(E), \|\cdot\|_p)$ is a Banach space for $1 \leq p \leq \infty$; simple, step and compactly supported continuous functions are dense in it for $p < \infty$.

## $L^p$ is a Normed Linear Space

> [!theorem] Proposition §35.1: $L^p$ is a Linear Space
> Let $1 \leq p \leq \infty$. Then $L^p(E)$ is a [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-1|linear space]]: if $f, g \in L^p(E)$ and $c \in \mathbb{R}$, then $cf \in L^p(E)$ and $f + g \in L^p(E)$.

^prop-35-1

> [!proof]+ Proof
> **Scalar multiplication.** For $p = \infty$: $|cf(x)| = |c||f(x)| \leq |c|\|f\|_\infty$ a.e., so $cf \in L^\infty$ with $\|cf\|_\infty \leq |c|\|f\|_\infty$. For $1 \leq p < \infty$: $\int |cf|^p = |c|^p \int |f|^p < \infty$, so $cf \in L^p$.
>
> **Addition.** For $p = \infty$: $|f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty$ a.e., so $f + g \in L^\infty$. For $1 \leq p < \infty$: since $|f + g|^p \leq 2^p(|f|^p + |g|^p)$ (by convexity, or $(a + b)^p \leq 2^{p-1}(a^p + b^p)$ for $a, b \geq 0$):
>
> $$
> \int_E |f + g|^p \leq 2^p \int_E |f|^p + 2^p \int_E |g|^p < \infty.
> $$

^pf-35-1

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]]

> [!theorem] Theorem §35.2: Minkowski's Inequality
> Let $1 \leq p \leq \infty$, $E \in \mathcal{M}(\mathbb{R}^n)$. For all $f, g$ a.e. finite measurable on $E$:
>
> $$
> \|f + g\|_p \leq \|f\|_p + \|g\|_p.
> $$

^thm-35-2

> [!proof]+ Proof
> **Case 1: $p = 1$.** $\int_E |f + g| \leq \int_E (|f| + |g|) = \int_E |f| + \int_E |g|$. $\checkmark$
>
> **Case 2: $p = \infty$.** $|f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty$ a.e., so $\|f + g\|_\infty \leq \|f\|_\infty + \|g\|_\infty$. $\checkmark$
>
> **Case 3: $1 < p < \infty$.** Write $1/p' = 1 - 1/p = (p-1)/p$. Then:
>
> $$
> \int_E |f + g|^p = \int_E |f + g|^{p-1} \cdot |f + g| \leq \int_E |f + g|^{p-1}|f|\,dx + \int_E |f + g|^{p-1}|g|\,dx.
> $$
>
> Apply [[Hölder's Inequality|Hölder]] to each term with exponents $p$ and $p'$. For the first:
>
> $$
> \int_E |f + g|^{p-1}|f|\,dx \leq \left(\int_E |f + g|^{(p-1)p'}\,dx\right)^{1/p'} \|f\|_p = \left(\int_E |f + g|^p\,dx\right)^{1/p'} \|f\|_p,
> $$
>
> since $(p-1)p' = (p-1) \cdot p/(p-1) = p$. Similarly for the second term. Therefore:
>
> $$
> \int_E |f + g|^p \leq \left(\int_E |f + g|^p\right)^{1/p'} (\|f\|_p + \|g\|_p).
> $$
>
> If $\|f\|_p$ or $\|g\|_p$ is infinite there is nothing to prove; otherwise $\int_E |f + g|^p < \infty$ by [[§35 Lᵖ as a Banach Space#^prop-35-1|Proposition §35.1]], and if $\int_E |f + g|^p = 0$ there is again nothing to prove. Dividing both sides by $(\int_E |f + g|^p)^{1/p'}$, which is therefore finite and nonzero:
>
> $$
> \left(\int_E |f + g|^p\right)^{1 - 1/p'} = \left(\int_E |f + g|^p\right)^{1/p} = \|f + g\|_p \leq \|f\|_p + \|g\|_p.
> $$

^pf-35-2

*Uses:* [[§22 The General Lebesgue Integral#^prop-22-3|§22.3]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-10|Def. §34.10]], [[Hölder's Inequality|§34.5]], [[§21 Consequences of the Monotone Convergence Theorem#^thm-21-1|§21.1]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§35 Lᵖ as a Banach Space#^prop-35-1|§35.1]]

> [!remark]- Connections
> - For $p = 2$ the norm comes from the $L^2$ inner product, and Minkowski is the inner-product [[Triangle inequality|triangle inequality (LADR 6.17)]]; the case $p = 1$ is [[§22 The General Lebesgue Integral#^prop-22-3|Proposition §22.3]].
> - Sequence version, proved by the same split-and-Hölder computation: [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-1|556 Thm. §16.1]].

> [!theorem] Theorem §35.3: $L^p$ is a Normed Linear Space
> Let $1 \leq p \leq \infty$. Then $(L^p(E), \|\cdot\|_p)$ is a [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-2|normed linear space]].

^thm-35-3

> [!proof]+ Proof
> We verify the three norm axioms:
> - (i) *Positive definiteness:* $\|f\|_p \geq 0$ is clear. $\|f\|_p = 0 \implies f = 0$ a.e. on $E$ (for $p < \infty$: $\int |f|^p = 0$ with $|f|^p \geq 0$ implies $|f|^p = 0$ a.e. ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|Proposition §21.4]]); for $p = \infty$: $\operatorname{ess\,sup}|f| = 0$ means $|f| \leq 0$ a.e.). This is why we work with $L^p$ (equivalence classes mod a.e. equality) rather than $\mathcal{L}^p$.
> - (ii) *Homogeneity:* $\|cf\|_p = |c|\,\|f\|_p$ (from the [[§35 Lᵖ as a Banach Space#^prop-35-1|scalar multiplication calculation above]]).
> - (iii) *Triangle inequality:* $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ ([[Minkowski's Inequality|Minkowski's inequality]]).

^pf-35-3

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-2|Def. §34.2]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-4|§21.4]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§35 Lᵖ as a Banach Space#^prop-35-1|§35.1]], [[Minkowski's Inequality|§35.2]]

> [!remark]- Connections
> - The case $p = 1$: [[§24 The L¹ Space and Density Theorems#^thm-24-4|Theorem §24.4]].
> - Passing to equivalence classes mod a.e. equality is a quotient by the subspace of null functions, as in [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].
> - Sequence analogue: [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^prop-16-3|556 Prop. §16.3]] ($\ell^p$ is a normed linear space).

> [!theorem] Corollary §35.4: Minkowski for Finite Sums
> Let $\{f_k\}_{k=1}^m \subseteq L^p(E)$. Then $\left\|\sum_{k=1}^{m} f_k\right\|_p \leq \sum_{k=1}^{m} \|f_k\|_p$.

^cor-35-4

This follows by induction on $m$ from the two-function case ([[Minkowski's Inequality|Theorem §35.2]]).

*Uses:* [[Minkowski's Inequality|§35.2]]

> [!theorem] Corollary §35.5: Minkowski for Nonnegative Series
> Let $\{f_k\}_{k=1}^{\infty}$ be a sequence of nonnegative measurable functions on $E$. Then:
>
> $$
> \left\|\sum_{k=1}^{\infty} f_k\right\|_p \leq \sum_{k=1}^{\infty} \|f_k\|_p.
> $$

^cor-35-5

> [!proof]+ Proof
> For $1 \leq p < \infty$: let $S_m(x) = \sum_{k=1}^m f_k(x)$. Since $f_k \geq 0$, $\{|S_m|^p\}$ is an increasing sequence of nonneg measurable functions with $|S_m|^p \nearrow |\sum f_k|^p$. By [[Monotone Convergence Theorem (Lebesgue)|MCT]]:
>
> $$
> \int_E \left|\sum_{k=1}^{\infty} f_k\right|^p dx = \lim_{m \to \infty} \int_E |S_m|^p\,dx \leq \lim_{m \to \infty} \left(\sum_{k=1}^{m} \|f_k\|_p\right)^p = \left(\sum_{k=1}^{\infty} \|f_k\|_p\right)^p,
> $$
>
> where the inequality uses the [[§35 Lᵖ as a Banach Space#^cor-35-4|finite sum corollary]]. Taking $p$-th roots gives the result.
>
> For $p = \infty$: $|\sum f_k(x)| \leq \sum |f_k(x)| \leq \sum \|f_k\|_\infty$ a.e. (each inequality holding a.e.), so $\|\sum f_k\|_\infty \leq \sum \|f_k\|_\infty$.

^pf-35-5

*Uses:* [[Monotone Convergence Theorem (Lebesgue)|§20.7]], [[§35 Lᵖ as a Banach Space#^cor-35-4|§35.4]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]]

> [!theorem] Corollary §35.6: Minkowski for General Measurable Series
> Let $\{f_k\}_{k=1}^{\infty}$ be a sequence of measurable functions on $E$, and assume $\sum_{k=1}^{\infty} f_k(x)$ converges for a.e. $x \in E$. Then:
>
> $$
> \left\|\sum_{k=1}^{\infty} f_k\right\|_p \leq \sum_{k=1}^{\infty} \|f_k\|_p.
> $$

^cor-35-6

> [!proof]+ Proof
> We have $|\sum_{k=1}^{\infty} f_k(x)| \leq \sum_{k=1}^{\infty} |f_k(x)|$ for a.e. $x \in E$. By the [[§35 Lᵖ as a Banach Space#^cor-35-5|nonnegative series corollary]] applied to $|f_k|$: $\|\sum |f_k|\|_p \leq \sum \|f_k\|_p$. Therefore $\|\sum f_k\|_p \leq \|\sum |f_k|\|_p \leq \sum \|f_k\|_p$.

^pf-35-6

*Uses:* [[§35 Lᵖ as a Banach Space#^cor-35-5|§35.5]], [[§20 The Lebesgue Integral for Simple Functions#^prop-20-3|§20.3]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]]

> [!theorem] Corollary §35.7: $L^p$ Absolute Series Test
> Let $\{f_k\}_{k=1}^{\infty} \subseteq L^p(E)$ with $\sum_{k=1}^{\infty} \|f_k\|_p < \infty$. Then:
> - (i) $\sum_{k=1}^{\infty} f_k(x)$ converges absolutely for a.e. $x \in E$.
> - (ii) $\sum_{k=1}^{\infty} f_k \in L^p(E)$ with $\|\sum_{k=1}^{\infty} f_k\|_p \leq \sum_{k=1}^{\infty} \|f_k\|_p$.

^cor-35-7

> [!proof]+ Proof
> **A.e. convergence:** For $1 \leq p < \infty$: by the [[§35 Lᵖ as a Banach Space#^cor-35-5|nonnegative series corollary]], $\|\sum |f_k|\|_p \leq \sum \|f_k\|_p < \infty$, so $\sum |f_k(x)|$ is a.e. finite ([[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|integrability implies a.e. finiteness]]), hence $\sum f_k(x)$ converges absolutely a.e.
>
> For $p = \infty$: $\sum |f_k(x)| \leq \sum \|f_k\|_\infty < \infty$ a.e., so $\sum f_k$ converges absolutely a.e.
>
> **Norm bound:** Follows from the [[§35 Lᵖ as a Banach Space#^cor-35-6|general measurable series corollary]].

^pf-35-7

*Uses:* [[§35 Lᵖ as a Banach Space#^cor-35-5|§35.5]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-3|§21.3]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[§35 Lᵖ as a Banach Space#^cor-35-6|§35.6]]

> [!remark]- Connections
> - The case $p = 1$: [[§23 The Dominated Convergence Theorem#^cor-23-4|Corollary §23.4]].
> - The $L^p$ analogue of [[§14 Series#^prop-14-6|absolute convergence implies convergence (451 §14.6)]]; in a normed space this property is equivalent to completeness, which is how it drives [[Riesz–Fischer Theorem|Riesz–Fischer]].

## $L^p$ Convergence and Completeness

> [!definition] Definition §35.1: $L^p$ Convergence
> Let $1 \leq p \leq \infty$ and $\{f_k\}_{k \in \mathbb{N}} \subseteq L^p(E)$.
> - (i) We say $\{f_k\}$ **converges to $f$ in $L^p$** if $f \in L^p(E)$ and $\lim_{k \to \infty} \|f_k - f\|_p = 0$. We write $\lim_{k \to \infty} f_k = f$ in $L^p(E)$.

^def-35-1

> [!remark]- Connections
> - The special case of [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-3|Def. §34.3]]–[[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-5|Def. §34.5]] for $\|\cdot\|_p$; for $p = 1$ it is [[§24 The L¹ Space and Density Theorems#^def-24-4|Def. §24.4]].
> - Computational version: for $p=2$ on an interval this is convergence in the mean, [[§15★ Mean Error and Convergence in Mean#^def-15-2|341 Def. §15.2]], in which the Fourier series of every $f$ with $\int f^2<\infty$ converges, [[§15★ Mean Error and Convergence in Mean#^thm-15-6|341 Thm. §15.6]].

> [!definition] Definition §35.2: Cauchy Sequences in $L^p$
> Let $1 \leq p \leq \infty$ and $\{f_k\}_{k \in \mathbb{N}} \subseteq L^p(E)$.
> - (ii) We say $\{f_k\}$ is **Cauchy in $L^p$** if for every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that $\|f_k - f_m\|_p < \varepsilon$ for all $k, m \geq N$.

^def-35-2

> [!definition] Definition §35.3: Completeness of $L^p$
> Let $1 \leq p \leq \infty$.
> - (iii) We say $L^p(E)$ is **complete** if every Cauchy sequence in $L^p(E)$ converges to some $f \in L^p(E)$.

^def-35-3

> [!remark] Remark
> The metric $d(f, g) = \|f - g\|_p$ makes $(L^p(E), d)$ a metric space ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-1|Proposition §34.1]]; this follows from the norm axioms verified [[§35 Lᵖ as a Banach Space#^thm-35-3|above]]). Completeness of $L^p$ in this metric is the content of the [[Riesz–Fischer Theorem|Riesz–Fischer theorem]] below.

^rem-35-3

> [!theorem] Proposition §35.8: Basic Properties of $L^p$ Convergence
> - (i) *Uniqueness:* If $f_k \to f$ in $L^p(E)$ and $f_k \to g$ in $L^p(E)$, then $f = g$ a.e. on $E$.
> - (ii) *Norm convergence:* If $f_k \to f$ in $L^p(E)$, then $\|f_k\|_p \to \|f\|_p$.

^prop-35-8

> [!proof]+ Proof
> **(i)** $\|f - g\|_p = \|f - f_k + f_k - g\|_p \leq \|f - f_k\|_p + \|f_k - g\|_p \to 0$, so $\|f - g\|_p = 0$, i.e., $f = g$ a.e.
>
> **(ii)** By [[Minkowski's Inequality|Minkowski]]: $|\,\|f_k\|_p - \|f\|_p\,| \leq \|f_k - f\|_p \to 0$.

^pf-35-8

*Uses:* [[Minkowski's Inequality|§35.2]], [[§35 Lᵖ as a Banach Space#^thm-35-3|§35.3]]

> [!remark]- Connections
> - (i) is uniqueness of limits in a metric space ([[§13 Some Topological Concepts in Metric Spaces#^rem-13-4|451 Rem. §13.4]]; [[§9 Hausdorff Spaces#^thm-9-3|590 §9.3]]), with “equal” meaning equal a.e.

## The Riesz–Fischer Theorem

> [!theorem] Lemma §35.9: Cauchy Subsequence Lemma
> Let $1 \leq p < \infty$ and $\{f_k\}$ be a Cauchy sequence in $L^p(E)$. Then there exists a subsequence $\{f_{k_j}\}_{j \in \mathbb{N}}$ and a function $f \in L^p(E)$ such that $f_{k_j}(x) \to f(x)$ for a.e. $x \in E$.

^lem-35-9

> [!proof]+ Proof
> Since $\{f_k\}$ is Cauchy in $L^p$, for each $j \geq 1$ there exists $k_j \in \mathbb{N}$ with $k_1 < k_2 < \cdots$ such that $\|f_k - f_m\|_p < 1/2^j$ for all $k, m \geq k_j$. In particular, $\|f_{k_{j+1}} - f_{k_j}\|_p < 1/2^j$.
>
> Let $g_0 = f_{k_1}$ and $g_j = f_{k_{j+1}} - f_{k_j}$ for $j \geq 1$. Then:
>
> $$
> \sum_{j=0}^{\infty} \|g_j\|_p \leq \|f_{k_1}\|_p + \sum_{j=1}^{\infty} \frac{1}{2^j} < \infty.
> $$
>
> By the $L^p$ absolute series test ([[§35 Lᵖ as a Banach Space#^cor-35-7|Corollary §35.7]]), $\sum_{j=0}^{\infty} g_j(x)$ converges absolutely for a.e. $x \in E$. Define $f(x) = \sum_{j=0}^{\infty} g_j(x)$ where the series converges (and $f(x) = 0$ elsewhere). Since the partial sums telescope:
>
> $$
> f_{k_{l+1}}(x) = \sum_{j=0}^{l} g_j(x) \to f(x) \quad \text{a.e. on } E.
> $$
>
> Moreover, $f \in L^p$: by the $L^p$ absolute series test ([[§35 Lᵖ as a Banach Space#^cor-35-7|Corollary §35.7]]), $\|f\|_p = \|\sum g_j\|_p \leq \sum \|g_j\|_p < \infty$.

^pf-35-9

*Uses:* [[§35 Lᵖ as a Banach Space#^def-35-2|Def. §35.2]], [[§35 Lᵖ as a Banach Space#^cor-35-7|§35.7]]

> [!theorem] Corollary §35.10: $L^p$ Convergence Implies A.E. Convergent Subsequence
> If $f_k \to f$ in $L^p(E)$ ($1 \leq p < \infty$), then there exists a subsequence $\{f_{k_j}\}$ with $f_{k_j}(x) \to f(x)$ for a.e. $x \in E$.

^cor-35-10

> [!proof]+ Proof
> Since $f_k \to f$ in $L^p$, $\{f_k\}$ is Cauchy in $L^p$. By [[§35 Lᵖ as a Banach Space#^lem-35-9|the lemma]], there exists a subsequence $\{f_{k_j}\}$ converging a.e. to some $g \in L^p$. By uniqueness of $L^p$ limits ([[§35 Lᵖ as a Banach Space#^prop-35-8|Proposition §35.8]]), $f = g$ a.e., so $f_{k_j} \to f$ a.e.

^pf-35-10

*Uses:* [[Minkowski's Inequality|§35.2]], [[§35 Lᵖ as a Banach Space#^lem-35-9|§35.9]], [[§35 Lᵖ as a Banach Space#^prop-35-8|§35.8]]

> [!remark]- Connections
> - The case $p = 1$ is the step “every $L^1$-convergent sequence has a pointwise a.e. convergent subsequence” in [[§30 Differentiating the Integral#^thm-30-7|Differentiation of the Integral (§30.7)]].
> - Only a subsequence: $L^p$ convergence does not imply a.e. convergence, and a.e. convergence upgrades to $L^1$ convergence under domination ([[Dominated Convergence Theorem|DCT]]).

> [!theorem] Theorem §35.11: Riesz–Fischer Theorem
> Let $1 \leq p \leq \infty$. Then $L^p(E)$ is a complete metric space (Banach space).

^thm-35-11

> [!proof]+ Proof
> **Case 1: $p = \infty$.** Let $\{f_k\}$ be Cauchy in $L^\infty(E)$: for every $\varepsilon > 0$, there exists $N$ such that $\|f_k - f_m\|_\infty < \varepsilon$ for all $k, m \geq N$.
>
> For each pair $k, m$, let $Z_{k,m} = \{x \in E : |f_k(x) - f_m(x)| > \|f_k - f_m\|_\infty\}$, so $m(Z_{k,m}) = 0$ ([[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|Proposition §34.2]]). Also let $Z_k = \{x \in E : |f_k(x)| > \|f_k\|_\infty\}$, again a null set, and let $Z = \bigcup_{k,m=1}^{\infty} Z_{k,m} \cup \bigcup_{k=1}^{\infty} Z_k$, so that each $f_k$ is bounded on $E \setminus Z$. Then $m(Z) = 0$, and on $E \setminus Z$:
>
> $$
> |f_k(x) - f_m(x)| \leq \|f_k - f_m\|_\infty < \varepsilon \quad \text{for all } k, m \geq N.
> $$
>
> So $\{f_k\}$ is uniformly Cauchy on $E \setminus Z$. By completeness of $\mathbb{R}$ ([[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]]), there exists a bounded function $f$ on $E \setminus Z$ such that $f_k \to f$ [[§24 Uniform Convergence#^def-24-2|uniformly]] on $E \setminus Z$. Set $f = 0$ on $Z$. Then $f \in L^\infty(E)$ and $\|f_k - f\|_\infty \to 0$.
>
> **Case 2: $1 \leq p < \infty$.** Let $\{f_k\}$ be Cauchy in $L^p(E)$. By the [[§35 Lᵖ as a Banach Space#^lem-35-9|Cauchy subsequence lemma]], there exists a subsequence $\{f_{k_j}\}$ and $f \in L^p(E)$ with $f_{k_j} \to f$ a.e.
>
> It remains to show $f_k \to f$ in $L^p$. For every $\varepsilon > 0$, there exists $N$ such that $\|f_k - f_m\|_p < \varepsilon$ for all $k, m \geq N$. Fix $k \geq N$. For any $k_j \geq N$:
>
> $$
> \int_E |f_k - f_{k_j}|^p\,dx \leq \varepsilon^p.
> $$
>
> Since $f_{k_j} \to f$ a.e., by [[Fatou's Lemma|Fatou's lemma]]:
>
> $$
> \int_E |f_k - f|^p\,dx = \int_E \liminf_{j \to \infty} |f_k - f_{k_j}|^p\,dx \leq \liminf_{j \to \infty} \int_E |f_k - f_{k_j}|^p\,dx \leq \varepsilon^p.
> $$
>
> Hence $\|f_k - f\|_p \leq \varepsilon$ for all $k \geq N$, so $f_k \to f$ in $L^p$.

^pf-35-11

*Uses:* [[§35 Lᵖ as a Banach Space#^def-35-1|Def. §35.1]], [[§35 Lᵖ as a Banach Space#^def-35-2|Def. §35.2]], [[§35 Lᵖ as a Banach Space#^def-35-3|Def. §35.3]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^prop-34-2|§34.2]], [[Properties of Lebesgue Outer Measure|§10.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]], [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]], [[§35 Lᵖ as a Banach Space#^lem-35-9|§35.9]], [[Fatou's Lemma|§21.8]], [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|§21.2]]

> [!remark]- Connections
> - $L^p(E)$ is thus a [[§13 Some Topological Concepts in Metric Spaces#^def-13-4|complete metric space (451 Def. §13.4)]], like $\mathbb{R}^n$ ([[§13 Some Topological Concepts in Metric Spaces#^thm-13-2|451 §13.2]]); for $p = 2$, a complete inner product space (Hilbert space) extending [[§20 Inner Products and Norms#^ladr-6-4|LADR 6.4]].
> - The engine is the absolute series test ([[§35 Lᵖ as a Banach Space#^cor-35-7|§35.7]]), itself built on [[Monotone Convergence Theorem (Lebesgue)|MCT]]; the upgrade from subsequence to full sequence is [[Fatou's Lemma|Fatou]].
> - Sequence analogue: [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^thm-16-5|556 Thm. §16.5]] ($\ell^p$ is a Banach space); for $p = 2$ it makes $L^2$ a Hilbert space in the sense of [[§21 Cauchy–Schwarz and the Induced Norm#^def-21-1|556 Def. §21.1]].

## Density and Separability

> [!definition] Definition §35.4: Dense Sets
> Let $(X, d)$ be a metric space. A subset $\mathcal{D} \subseteq X$ is **dense** in $X$ if for every $x \in X$, there exists a sequence $\{d_j\} \subseteq \mathcal{D}$ with $d(d_j, x) \to 0$.

^def-35-4

> [!remark]- Connections
> - Topological versions: [[§22 Countability Axioms#^def-22-4|dense (590 Def. §22.4)]]; the sequential form agrees with $\overline{\mathcal{D}} = X$ in a metric space by [[§13 Some Topological Concepts in Metric Spaces#^prop-13-6|451 §13.6]].
> - 556 versions: [[§10 Normed Linear Spaces#^def-10-7|556 Def. §10.7]] (dense, via the closure).

> [!definition] Definition §35.5: Separability
> Let $(X, d)$ be a metric space. We say $(X, d)$ is **separable** if there exists a countable dense subset.

^def-35-5

> [!remark]- Connections
> - Topological version: [[§22 Countability Axioms#^def-22-5|separable (590 Def. §22.5)]].
> - In metric spaces, separable $\iff$ second countable: [[§22 Countability Axioms#^prop-22-4|590 §22.4]].
> - 556 version: [[§24 Orthonormal Sets and Bases#^def-24-5|556 Def. §24.5]] (separable).

> [!example] Example §35.1
> $\mathbb{R}^n$ is separable: $\mathbb{Q}^n$ is a countable dense subset.

^ex-35-1

> [!remark]- Connections
> - Same example in Topology: [[§22 Countability Axioms#^ex-22-8|590 Ex. §22.8]]; countability of $\mathbb{Q}$: [[§3 Countability of Rationals and Unions#^cor-3-2|Corollary §3.2]].

> [!theorem] Theorem §35.12: Density in $L^p$
> Let $1 \leq p < \infty$. Then:
> - (i) The set of simple functions is dense in $L^p(E)$.
> - (ii) The set of step functions is dense in $L^p(E)$.
> - (iii) The set $C_c(\mathbb{R}^n)$ of compactly supported continuous functions is dense in $L^p(E)$.

^thm-35-12

> [!proof]+ Proof
> **(i) Simple functions are dense in $L^p$.** Let $f \in L^p(E)$. By the [[§17 Simple Functions and Modes of Convergence#^thm-17-3|Simple Function Approximation Theorem]], there exists a sequence of simple functions $\varphi_k$ with $|\varphi_k(x)| \leq |f(x)|$ for all $x$ and $\varphi_k(x) \to f(x)$ pointwise.
>
> Then $|\varphi_k - f|^p \leq (|\varphi_k| + |f|)^p \leq (2|f|)^p = 2^p|f|^p$. Since $f \in L^p$, $2^p|f|^p \in L^1(E)$. By [[Dominated Convergence Theorem|DCT]]:
>
> $$
> \int_E |\varphi_k - f|^p\,dx \to 0, \qquad \text{i.e.,} \quad \|\varphi_k - f\|_p \to 0.
> $$
>
> **(ii) Step functions are dense in $L^p$.** By (i), it suffices to approximate simple functions by [[§23 The Dominated Convergence Theorem#^def-23-1|step functions]]. Let $\varphi = \sum_{j=1}^{m} a_j \chi_{S_j}$ with $m(S_j) < \infty$ and the $S_j$ disjoint.
>
> It suffices to approximate each $\chi_S$ (with $m(S) < \infty$) by a step function in $\|\cdot\|_p$. By the approximation theorem ([[§13 Approximation and Continuity of Measure#^thm-13-6|§13.6]]), for any $\delta > 0$ there exist disjoint rectangles $I_1, \ldots, I_q$ with $m(S \triangle \bigcup I_j) < \delta$ ([[§13 Approximation and Continuity of Measure#^def-13-3|symmetric difference]]). Let $\psi = \sum \chi_{I_j}$. Then:
>
> $$
> \|\chi_S - \psi\|_p^p = \int |\chi_S - \chi_{\bigcup I_j}|^p\,dx = m(S \triangle \textstyle\bigcup I_j) < \delta,
> $$
>
> since $|\chi_S - \psi|^p = |\chi_S - \psi| = \chi_{S \triangle \bigcup I_j}$. Take $\delta = \varepsilon^p$.
>
> For the general simple function: approximate each $\chi_{S_j}$ by a step function $\psi_j$ with $\|\chi_{S_j} - \psi_j\|_p < \varepsilon/(m \max |a_j|)$, then $\psi = \sum a_j \psi_j$ satisfies $\|\varphi - \psi\|_p \leq \sum |a_j| \|\chi_{S_j} - \psi_j\|_p < \varepsilon$.
>
> **(iii) $C_c(\mathbb{R}^n)$ is dense in $L^p$.** By (ii), it suffices to approximate step functions. By linearity, it suffices to approximate $\chi_R$ for a rectangle $R$ with $m(R) < \infty$.
>
> Construct the same “trapezoidal” continuous approximation $g$ as in the $L^1$ proof ([[Continuous Functions of Compact Support are Dense in L¹|§24.7]]): $g$ is continuous, compactly supported, $0 \leq g \leq 1$, and $|\chi_R(x) - g(x)| \leq 1$, and $\chi_R - g$ vanishes outside transition regions of total measure $\leq C\varepsilon'$. Since $|\chi_R - g|^p \leq |\chi_R - g| \leq 1$ (as $0 \leq g \leq 1$):
>
> $$
> \|\chi_R - g\|_p^p = \int |\chi_R - g|^p\,dx \leq \int |\chi_R - g|\,dx = \|\chi_R - g\|_1 < C\varepsilon'.
> $$
>
> Choose $\varepsilon'$ small enough so that $C\varepsilon' < \varepsilon^p$.

^pf-35-12

*Uses:* [[§17 Simple Functions and Modes of Convergence#^thm-17-3|§17.3]], [[Dominated Convergence Theorem|§23.3]], [[§23 The Dominated Convergence Theorem#^def-23-1|Def. §23.1]], [[§13 Approximation and Continuity of Measure#^thm-13-6|§13.6]], [[§13 Approximation and Continuity of Measure#^def-13-3|Def. §13.3]], [[§35 Lᵖ as a Banach Space#^cor-35-4|§35.4]], [[Continuous Functions of Compact Support are Dense in L¹|§24.7]]

> [!remark]- Connections
> - The $L^1$ versions: [[§24 The L¹ Space and Density Theorems#^thm-24-5|§24.5]], [[§24 The L¹ Space and Density Theorems#^thm-24-6|§24.6]], [[Continuous Functions of Compact Support are Dense in L¹|§24.7]].
> - 556 strengthens (iii) to smooth compactly supported approximants, [[§17 The Function Spaces Lᵖ(Ω)#^thm-17-4|556 Thm. §17.4]]; the failure for $p = \infty$ is [[§17 The Function Spaces Lᵖ(Ω)#^prop-17-5|556 Prop. §17.5]].
> - Used in PDEs: with Weierstrass's approximation theorem, (iii) shows that polynomials are dense in $L^2[-1,1]$, so Legendre series converge in the mean; see the Connections of [[§61★ Legendre Series and Zonal Harmonics#^thm-61-1|341 Thm. §61.1]].

> [!remark] Remark: The Approximation Chain for $L^p$
> We have:
>
> $$
> C_c(\mathbb{R}^n) \;\longrightarrow\; \text{step functions} \;\longrightarrow\; \text{simple functions} \;\longrightarrow\; L^p(E),
> $$
>
> with each class dense in the next in the $L^p$ norm ($1 \leq p < \infty$). This chain fails for $p = \infty$, but not at the last step: simple functions are dense in $L^\infty$ (uniform approximation of bounded functions, [[§17 Simple Functions and Modes of Convergence#^thm-17-5|Theorem §17.5]], applied off a null set). It breaks at step functions and $C_c$: for $L^\infty$, continuous functions are *not* dense (e.g., $\chi_{[0,1]}$ cannot be uniformly approximated by continuous functions on $\mathbb{R}$).

^rem-35-4

> [!remark]- Connections
> - The $L^1$ chain: [[§24 The L¹ Space and Density Theorems#^rem-24-1|Remark §16.1]]. Why $\chi_{[0,1]}$ fails in $L^\infty$: a uniform limit of continuous functions is continuous ([[§17 Simple Functions and Modes of Convergence#^thm-17-4|§17.4]], [[§24 Uniform Convergence#^thm-24-2|451 §24.2]]).

> [!theorem] Corollary §35.13: $L^p$ is Separable for $1 \leq p < \infty$
> Let $1 \leq p < \infty$. Then $L^p(E)$ is [[§35 Lᵖ as a Banach Space#^def-35-5|separable]].

^cor-35-13

> [!proof]+ Proof
> Let $\mathcal{D} = \{\sum_{j=1}^{n} c_j \chi_{I_j} : c_j \in \mathbb{Q},\; I_j \text{ intervals with rational endpoints, mutually disjoint}, \; n \in \mathbb{N}\}$. Then $\mathcal{D}$ is countable (rational coefficients, rational endpoints, finite sums). By density of step functions in $L^p$ ([[§35 Lᵖ as a Banach Space#^thm-35-12|Theorem §35.12]]), any $f \in L^p$ can be approximated by step functions, which can in turn be approximated by elements of $\mathcal{D}$ (replace real coefficients and endpoints by rational ones). Hence $\mathcal{D}$ is dense.

^pf-35-13

*Uses:* [[§35 Lᵖ as a Banach Space#^def-35-4|Def. §35.4]], [[§35 Lᵖ as a Banach Space#^def-35-5|Def. §35.5]], [[§3 Countability of Rationals and Unions#^cor-3-2|§3.2]], [[Countable Union of Countable Sets is Countable|§3.1]], [[§1 Countability and Set Theory#^ex-1-3|Ex. §1.3]], [[§35 Lᵖ as a Banach Space#^thm-35-12|§35.12]]

> [!remark]- Connections
> - Same result in 556, proved with rational rectangles in ℝⁿ: [[§25 Sequence and Function Spaces#^prop-25-4|556 Prop. §25.4]]; the case $L^2(\mathbb{R}^n)$ is [[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|556 Thm. §32.2]].

> [!theorem] Theorem §35.14: $L^\infty$ is Not Separable
> $L^\infty(E)$ is not separable (when $E$ has positive measure).

^thm-35-14

> [!proof]+ Proof
> Consider $E = (0, 1)$ and for each $t \in (0, 1)$, define $f_t = \chi_{(0, t)}$. For $s \neq t$:
>
> $$
> \|f_s - f_t\|_\infty = \|\chi_{(\min(s,t),\, \max(s,t))}\|_\infty = 1.
> $$
>
> So $\{f_t\}_{t \in (0,1)}$ is an [[§4 Uncountability#^ex-4-2|uncountable]] family with pairwise distance $1$. Any dense subset must contain a point within distance $1/2$ of each $f_t$, and since the $1/2$-balls around distinct $f_t$'s are disjoint, the dense subset must be uncountable. For a general $E$ with $m(E) > 0$, the same argument works with $f_t = \chi_{E_0 \cap \{x_1 < t\}}$, where $E_0 \subseteq E$ has $0 < m(E_0) < \infty$: by [[Continuity of Measure|continuity of measure]] from below and [[§13 Approximation and Continuity of Measure#^prop-13-5|from above]] (using $m(E_0) < \infty$ and that each hyperplane $\{x_1 = t\}$ is null), $t \mapsto m(E_0 \cap \{x_1 < t\})$ is continuous and increasing, so it takes uncountably many values, and two $f_t$ with different values are at distance $1$.

^pf-35-14

*Uses:* [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-8|Def. §34.8]], [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-9|Def. §34.9]], [[§4 Uncountability#^ex-4-2|Ex. §4.2]], [[§35 Lᵖ as a Banach Space#^def-35-4|Def. §35.4]], [[§35 Lᵖ as a Banach Space#^def-35-5|Def. §35.5]], [[Continuity of Measure|§13.4]], [[§13 Approximation and Continuity of Measure#^prop-13-5|§13.5]]

> [!remark]- Connections
> - Same uncountable-versus-countable counting as in [[§22 Countability Axioms#^prop-22-4|590 §22.4]](2) ($\mathbb{R}_l$ not second countable); by [[§22 Countability Axioms#^prop-22-4|590 §22.4]](3), $L^\infty$ is also not second countable.
