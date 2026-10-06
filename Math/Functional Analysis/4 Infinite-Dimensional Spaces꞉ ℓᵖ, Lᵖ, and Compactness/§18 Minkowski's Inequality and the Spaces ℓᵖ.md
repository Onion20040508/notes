---
type: section
subject: "[[Functional Analysis]]"
chapter: 4
section: 18
tags: [functional-analysis, math556]
---
← [[§17 Hölder's Inequality for Sequences]] · ↑ [[· 4 Infinite-Dimensional Spaces꞉ ℓᵖ, Lᵖ, and Compactness]] · [[§19 The Function Spaces Lᵖ(Ω)]] →

*Stage: norms — Thread: completeness. The first infinite-dimensional Banach spaces.*

## Minkowski's Inequality

> [!theorem] Theorem §18.1: Minkowski's Inequality for Sequences
> Let $1 \le p \le \infty$ and $a = (a_i), b = (b_i) \in \ell$. Then
>
> $$
> \|a + b\|_p \le \|a\|_p + \|b\|_p,
> $$
>
> where both sides are allowed to be $+\infty$.
>
> *Lax: §5.1, Thms 4–5*

^thm-18-1

Wu's proof for $1 < p < \infty$ runs in two stages: a computation, valid as an inequality in $[0,\infty]$, followed by a cancellation that needs $\|a+b\|_p < \infty$; when that is not yet known, the computation is applied to truncations. The order below follows hers.

> [!proof]+ Proof of Theorem §13.1
> **Case $p = 1$.** $\sum_i |a_i + b_i| \le \sum_i (|a_i| + |b_i|) = \|a\|_1 + \|b\|_1$, by the termwise triangle inequality and addition of series of non-negative terms.
>
> **Case $p = \infty$.** For every $i$, $|a_i + b_i| \le |a_i| + |b_i| \le \|a\|_\infty + \|b\|_\infty$; take the supremum over $i$.
>
> **Case $1 < p < \infty$.** If $\|a\|_p = \infty$ or $\|b\|_p = \infty$, the right side is $+\infty$ and there is nothing to prove. So assume both are finite. Let $q = p/(p-1)$ be the conjugate exponent, so that
>
> $$
> (p - 1)\, q = p, \qquad \frac{p}{q} = p - 1. \tag{4.1}
> $$
>
> *Step 1: split one factor off.* Writing $|a_i + b_i|^p = |a_i + b_i|^{p-1}\,|a_i + b_i|$ and using $|a_i + b_i| \le |a_i| + |b_i|$,
>
> $$
> \|a + b\|_p^p = \sum_i |a_i + b_i|^{p-1}\,|a_i + b_i| \le \underbrace{\sum_i |a_i + b_i|^{p-1}\,|a_i|}_{\mathrm{I}} + \underbrace{\sum_i |a_i + b_i|^{p-1}\,|b_i|}_{\mathrm{II}},
> $$
>
> an inequality between elements of $[0, \infty]$.
>
> *Step 2: Hölder on each piece.* Apply Theorem [[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]] to $\mathrm{I}$ with the exponent $q$ on the first factor and $p$ on the second:
>
> $$
> \mathrm{I} \le \Bigl( \sum_i \bigl(|a_i + b_i|^{p-1}\bigr)^{q} \Bigr)^{1/q} \Bigl( \sum_i |a_i|^p \Bigr)^{1/p} = \Bigl( \sum_i |a_i + b_i|^{p} \Bigr)^{1/q}\, \|a\|_p = \|a + b\|_p^{\,p/q}\, \|a\|_p,
> $$
>
> using $(p-1)q = p$ from (4.1). The same computation gives $\mathrm{II} \le \|a + b\|_p^{\,p/q}\, \|b\|_p$. Hence
>
> $$
> \|a + b\|_p^p \le \|a + b\|_p^{\,p-1} \bigl( \|a\|_p + \|b\|_p \bigr). \tag{4.2}
> $$
>
> *Step 3: cancel, if $\|a + b\|_p$ is finite.* If $\|a + b\|_p = 0$ there is nothing to prove. If $0 < \|a + b\|_p < \infty$, divide both sides of (4.2) by $\|a + b\|_p^{\,p-1}$ to obtain $\|a + b\|_p \le \|a\|_p + \|b\|_p$. If $\|a + b\|_p = \infty$, (4.2) reads $\infty \le \infty$ and cannot be cancelled.
>
> *Step 4: otherwise, truncate.* Let
>
> $$
> a^{(n)} = (a_1, \ldots, a_n, 0, 0, \ldots), \qquad b^{(n)} = (b_1, \ldots, b_n, 0, 0, \ldots).
> $$
>
> These are finitely supported, so all norms involved are finite sums, and Steps 1–3 apply to them:
>
> $$
> \Bigl( \sum_{i=1}^{n} |a_i + b_i|^p \Bigr)^{1/p} = \|a^{(n)} + b^{(n)}\|_p \le \|a^{(n)}\|_p + \|b^{(n)}\|_p \le \|a\|_p + \|b\|_p,
> $$
>
> the last step because a partial sum of non-negative terms is at most the full sum. The left side is increasing in $n$ and bounded by $\|a\|_p + \|b\|_p$; letting $n \to \infty$ gives $\|a + b\|_p \le \|a\|_p + \|b\|_p$. In particular $\|a + b\|_p < \infty$ whenever the right side is finite.

^pf-18-1

*Uses:* [[§17 Hölder's Inequality for Sequences#^def-17-1|Def. §17.1]], [[§17 Hölder's Inequality for Sequences#^def-17-3|Def. §17.3]], [[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]]

> [!remark]- Connections
> - The integral version, home in the vault: [[Minkowski's Inequality|551 §35.2]] (same split-and-Hölder computation; its series corollaries [[§35 Lᵖ as a Banach Space#^cor-35-5|551 §35.5]]–[[§35 Lᵖ as a Banach Space#^cor-35-6|§35.6]]); in this course [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-2|§19.2]] (cited) and Part 1 of the proof of [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-8|§19.8]] (continuous functions, HW3).
> - For $p = 2$ it is the inner-product [[Triangle inequality|triangle inequality (LADR 6.17)]].

> [!theorem] Lemma §18.2: Minkowski for Finitely Supported Sequences
> Let $1 < p < \infty$ and let $a, b \in \ell$ have only finitely many nonzero terms. Then $\|a + b\|_p \le \|a\|_p + \|b\|_p$.

^lem-18-2

> [!proof]+ Proof
> All three norms are finite sums, so Steps 1–3 of the [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^pf-18-1|proof of Theorem §18.1]] apply with no truncation: the computation gives (4.2), and the cancellation in Step 3 is legitimate.

^pf-18-2

*Uses:* [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|§18.1]]

> [!remark] Remark: Where the Finiteness is Used
> A student asked what happens if the sums are infinite. The answer is in the structure above: Steps 1–2 are valid as inequalities in $[0,\infty]$ regardless, but Step 3 divides by $\|a+b\|_p^{\,p-1}$, and “$\infty \le \infty \cdot C$” cannot be cancelled to “$\infty \le C$.” The truncation makes every quantity finite, and monotone convergence of the partial sums then carries the inequality to the full series. This is a general pattern: prove the estimate in a setting where everything is finite, then pass to the limit through an increasing family. Minkowski fails for $0 < p < 1$: the same computation cannot be run because [[§17 Hölder's Inequality for Sequences#^thm-17-1|Hölder]] needs $q \ge 1$, and in fact $\|\cdot\|_p$ is then not subadditive: for $a = e_1$ and $b = e_2$, $\|a + b\|_p = 2^{1/p} > 2 = \|a\|_p + \|b\|_p$.

^rem-18-1

## The Spaces ℓᵖ

> [!definition] Definition §18.1: $\ell^p$
> For $1 \le p \le \infty$,
>
> $$
> \ell^p = \{ a \in \ell : \|a\|_p < \infty \}.
> $$
>
> (Also written $\ell_p$; both notations occur on the board.)
>
> *Lax: §5.1, example (b)*

^def-18-1

> [!remark]- Connections
> - The function-space counterpart: [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-6|551 Def. §34.6]] ($L^p$), [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-8|551 Def. §34.8]] ($L^\infty$); in this course [[§19 The Function Spaces Lᵖ(Ω)#^def-19-1|Def. §19.1]].

> [!theorem] Proposition §18.3: $\ell^p$ is a Normed Linear Space
> For $1 \le p \le \infty$, $\ell^p$ is a linear subspace of $\ell$, and $\|\cdot\|_p$ is a norm on it.
>
> *Lax: §5.1, Thm 4*

^prop-18-3

> [!proof]+ Proof
> *Subspace.* If $a, b \in \ell^p$ then $\|a + b\|_p \le \|a\|_p + \|b\|_p < \infty$ by [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|Minkowski]], so $a + b \in \ell^p$; and $\|ca\|_p = |c|\,\|a\|_p < \infty$ (below), so $ca \in \ell^p$; $0 \in \ell^p$.
>
> *Positivity.* $\|a\|_p \ge 0$ as a sum (or supremum) of non-negative numbers, and $\|a\|_p = 0$ iff every $|a_i|^p = 0$ (resp. every $|a_i| = 0$) iff $a = 0$.
>
> *Homogeneity.* For $p < \infty$, $\|ca\|_p = \bigl(\sum_i |c|^p |a_i|^p\bigr)^{1/p} = |c|\,\|a\|_p$; for $p = \infty$, $\sup_i |c a_i| = |c| \sup_i |a_i|$.
>
> *Subadditivity.* Theorem [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|§18.1]].

^pf-18-3

*Uses:* [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|Def. §18.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|§18.1]]

> [!remark]- Connections
> - The function-space counterpart: [[§35 Lᵖ as a Banach Space#^thm-35-3|551 §35.3]] ($L^p$ is a normed linear space).

> [!remark] Remark
> $\ell^p$ is the first genuinely infinite-dimensional normed space in the course: it contains the linearly independent sequences $e_1 = (1,0,0,\ldots)$, $e_2 = (0,1,0,\ldots)$, …. Unlike the norms $\|\cdot\|_p$ on $\mathbb{R}^n$, the spaces $\ell^p$ for different $p$ are different sets, and their norms are not equivalent where both are defined.

^rem-18-2

> [!theorem] Proposition §18.4: Nesting of the $\ell^p$ Spaces
> Let $1 \le p < q \le \infty$.
> - (a) $\|a\|_q \le \|a\|_p$ for every $a \in \ell$; in particular $\ell^p \subset \ell^q$.
> - (b) The inclusion is strict: $\ell^p \neq \ell^q$.
> - (c) On $\ell^p$, the norms $\|\cdot\|_p$ and $\|\cdot\|_q$ are not equivalent.

^prop-18-4

> [!proof]+ Proof
> (Not covered in lecture.) (a) If $a = 0$ or $\|a\|_p = \infty$ there is nothing to prove; otherwise, by homogeneity, we may assume $\|a\|_p = 1$. Then $|a_i| \le 1$ for every $i$, a single term being at most the sum. If $q = \infty$, $\|a\|_\infty = \sup_i |a_i| \le 1$. If $q < \infty$, then $|a_i|^q \le |a_i|^p$ because $|a_i| \le 1$ and $q > p$, so $\|a\|_q^q \le \sum_i |a_i|^p = 1$.
>
> (b) If $q < \infty$, let $a_i = i^{-1/p}$: then $\sum_i |a_i|^p = \sum_i 1/i = \infty$, while $\sum_i |a_i|^q = \sum_i i^{-q/p} < \infty$ because $q/p > 1$. If $q = \infty$, the constant sequence $(1, 1, \ldots)$ lies in $\ell^\infty \setminus \ell^p$.
>
> (c) For $s_n = e_1 + \cdots + e_n$ we have $\|s_n\|_p = n^{1/p}$ and $\|s_n\|_q = n^{1/q}$ (with $1/\infty = 0$), so $\|s_n\|_p / \|s_n\|_q = n^{1/p - 1/q} \to \infty$, and no constant $C$ gives $\|a\|_p \le C\|a\|_q$ on $\ell^p$.

^pf-18-4

*Uses:* [[§17 Hölder's Inequality for Sequences#^def-17-1|Def. §17.1]], [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^def-18-1|Def. §18.1]], [[§14 New Normed Spaces from Old#^def-14-1|Def. §14.1]]

![[m556-13-1.svg]]
*The unit balls $\{\|x\|_p \le 1\}$ in $\mathbb{R}^2$ increase with $p$; this is (a) for vectors with two nonzero entries. All four norms are equivalent on $\mathbb{R}^2$ (Theorem [[§14 New Normed Spaces from Old#^thm-14-3|§14.3]]), and (c) is the statement that this fails on $\ell^p$.*

> [!remark]- Connections
> - For functions the inclusion runs the other way on sets of finite measure: [[§34 Normed Linear Spaces and Lᵖ Spaces#^cor-34-6|551 §34.6]].
> - The same unit-ball picture: [[§34 Normed Linear Spaces and Lᵖ Spaces#^ex-34-2|551 Ex. §34.2]].
> - (c) is cited in [[§14 New Normed Spaces from Old#^rem-14-2|Remark §12]] (Finite Dimension is Necessary).

## Completeness of ℓᵖ

> [!theorem] Theorem §18.5: $\ell^p$ is a Banach Space
> For $1 \le p \le \infty$, $(\ell^p, \|\cdot\|_p)$ is complete.
>
> *Lax: §5.1, examples (a)–(b)*

^thm-18-5

> [!remark] Note: Notation for the Proof
> A sequence in $\ell^p$ is a sequence of sequences. Write the $n$-th term as
>
> $$
> a^{(n)} = \bigl( a^{(n)}_1, a^{(n)}_2, a^{(n)}_3, \ldots \bigr) \in \ell^p,
> $$
>
> so the superscript indexes the term of the sequence in $\ell^p$ and the subscript the coordinate. Wu also used truncations $a^{(n,k)} = (a^{(n)}_1, \ldots, a^{(n)}_k) \in \mathbb{F}^k$.

^rem-18-3

> [!proof]+ Proof
> The proof follows the plan Wu stated for every completeness argument: *first find the candidate for the limit, then prove convergence to it*. Take $p < \infty$ first.
>
> Let $\{a^{(n)}\}_{n \ge 1}$ be Cauchy in $\ell^p$: for every $\varepsilon > 0$ there is $N$ such that
>
> $$
> \sum_{i=1}^{\infty} \bigl| a^{(n)}_i - a^{(m)}_i \bigr|^p < \varepsilon^p \qquad \text{for all } n, m \ge N. \tag{4.3}
> $$
>
> **Step 1: The candidate, through truncations.** For $k \in \mathbb{N}$ let
>
> $$
> a^{(n,k)} = \bigl( a^{(n)}_1, \ldots, a^{(n)}_k \bigr) \in \mathbb{F}^k,
> $$
>
> and give $\mathbb{F}^k$ the norm $\|(c_1, \ldots, c_k)\|_p = \bigl( \sum_{i=1}^k |c_i|^p \bigr)^{1/p}$. Fix $k$. A partial sum of non-negative terms is at most the full sum, so
>
> $$
> \bigl\| a^{(n,k)} - a^{(m,k)} \bigr\|_p = \Bigl( \sum_{i=1}^{k} \bigl| a^{(n)}_i - a^{(m)}_i \bigr|^p \Bigr)^{1/p} \le \bigl\| a^{(n)} - a^{(m)} \bigr\|_p \xrightarrow[n, m \to \infty]{} 0 .
> $$
>
> So $\{a^{(n,k)}\}_n$ is Cauchy in $(\mathbb{F}^k, \|\cdot\|_p)$, which is complete (Corollary [[§14 New Normed Spaces from Old#^cor-14-4|§14.4]]); hence there is $a^{(k)} \in \mathbb{F}^k$ with $\|a^{(n,k)} - a^{(k)}\|_p \to 0$ as $n \to \infty$.
>
> The limits are consistent. The first $k$ coordinates of $a^{(n,k+1)}$ form $a^{(n,k)}$, and convergence in $\mathbb{F}^{k+1}$ implies convergence of each coordinate (a single term is at most the sum). So the first $k$ coordinates of $a^{(k+1)}$ are the limits of the coordinates of $a^{(n,k)}$, which by uniqueness of limits are the coordinates of $a^{(k)}$:
>
> $$
> a^{(k+1)} = \bigl( a^{(k)},\, a_{k+1} \bigr) \qquad \text{for some scalar } a_{k+1}.
> $$
>
> Hence there is a single sequence $a = (a_1, a_2, \ldots) \in \ell$ with $a^{(k)} = (a_1, \ldots, a_k)$ for every $k$; in particular $a^{(n)}_i \to a_i$ as $n \to \infty$ for each $i$. This is the candidate. Nothing has been proved about it yet: it is not known that $a \in \ell^p$, nor that $a^{(n)} \to a$ in $\|\cdot\|_p$.
>
> **Step 2: A uniform tail estimate.** Fix $\varepsilon > 0$ and $N$ as in (4.3), and fix $n \ge N$. For any $k \in \mathbb{N}$ and any $m \ge N$, a partial sum is at most the full sum, so
>
> $$
> \sum_{i=1}^{k} \bigl| a^{(n)}_i - a^{(m)}_i \bigr|^p \le \sum_{i=1}^{\infty} \bigl| a^{(n)}_i - a^{(m)}_i \bigr|^p < \varepsilon^p.
> $$
>
> The left side is $\|a^{(n,k)} - a^{(m,k)}\|_p^p$, a *finite* sum of $k$ terms, each of which converges as $m \to \infty$ by Step 1 (to $|a^{(n)}_i - a_i|^p$, by continuity of $t \mapsto |t|^p$). A limit of finitely many convergent terms is the sum of the limits, and non-strict inequalities survive limits, so
>
> $$
> \sum_{i=1}^{k} \bigl| a^{(n)}_i - a_i \bigr|^p \le \varepsilon^p \qquad \text{for every } k \in \mathbb{N} \text{ and every } n \ge N.
> $$
>
> The left side is increasing in $k$ and bounded by $\varepsilon^p$ independently of $k$, so its limit exists and
>
> $$
> \sum_{i=1}^{\infty} \bigl| a^{(n)}_i - a_i \bigr|^p \le \varepsilon^p, \qquad \text{i.e.} \qquad \|a^{(n)} - a\|_p \le \varepsilon \qquad \text{for all } n \ge N. \tag{4.4}
> $$
>
> **Step 3: Conclusion.** By (4.4) with $n = N$, $a - a^{(N)} \in \ell^p$; since $a^{(N)} \in \ell^p$ and $\ell^p$ is a linear space (Proposition [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-3|§18.3]]), $a = a^{(N)} + (a - a^{(N)}) \in \ell^p$. And (4.4) says precisely that $\|a^{(n)} - a\|_p \to 0$ as $n \to \infty$. So the Cauchy sequence converges in $\ell^p$.
>
> **The case $p = \infty$.** The same three steps with sums replaced by suprema. Cauchy means $\sup_i |a^{(n)}_i - a^{(m)}_i| < \varepsilon$ for $n, m \ge N$; each coordinate is Cauchy, giving $a_i = \lim_n a^{(n)}_i$; for fixed $i$ and $n \ge N$, $|a^{(n)}_i - a^{(m)}_i| < \varepsilon$ for all $m \ge N$, and letting $m \to \infty$ gives $|a^{(n)}_i - a_i| \le \varepsilon$; taking the supremum over $i$ gives $\|a^{(n)} - a\|_\infty \le \varepsilon$ for $n \ge N$, whence $a \in \ell^\infty$ and $a^{(n)} \to a$.

^pf-18-5

*Uses:* [[§11 Normed Linear Spaces#^def-11-5|Def. §11.5]], [[§12 Completeness#^def-12-2|Def. §12.2]], [[§14 New Normed Spaces from Old#^cor-14-4|§14.4]], [[§11 Normed Linear Spaces#^prop-11-5|§11.5]], [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^prop-18-3|§18.3]], [[§10 Monotone Sequences and Cauchy Sequences#^thm-10-1|451 §10.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]]

> [!remark]- Connections
> - The function-space counterpart: [[Riesz–Fischer Theorem|551 §35.11]] (Riesz–Fischer), cited in this course as [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-3|§19.3]].
> - $\ell^2$ is the first infinite-dimensional Hilbert space: [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1|Ex. §23.1]].

> [!remark] Remark: The Two Limits
> The delicate point is Step 2, and it produced the longest discussion in lecture. Two limits are involved: $m \to \infty$ (to replace $a^{(m)}$ by the candidate $a$) and $k \to \infty$ (to pass from partial sums to the full series). A student proposed handling the infinite sum directly as a limit of partial sums and choosing, for each $k$, an $n$ large enough. That does not work: the $n$ obtained depends on $k$, and as $k \to \infty$ it may go to infinity with it, so nothing is proved for the full series with a single $n$. The proof avoids this by using the Cauchy condition in its full form (4.3) — with the *infinite* sum and $N$ independent of everything else — and only then truncating to a finite sum, where $m \to \infty$ can be taken termwise, and finally sending $k \to \infty$ through a monotone bounded sequence. The order matters: truncate, then $m \to \infty$, then $k \to \infty$, with $n \ge N$ fixed throughout. Interchanging limits requires justification; when two are present, arrange for one of them to be a finite sum.

^rem-18-4

![[m556-13-2.svg]]
*The order of limits in Step 2. Each row is one term $a^{(n)}$ of the Cauchy sequence, each column one coordinate $i$. (1) Compare rows $n$ and $m$ on the first $k$ coordinates only (red box), a finite sum $< \varepsilon^p$; (2) let $m \to \infty$ column by column inside the box, legitimate because there are only $k$ columns; (3) only then let $k \to \infty$, which is harmless because the bound $\varepsilon^p$ does not depend on $k$. Doing (3) before (2) would mean exchanging $m \to \infty$ with an infinite sum.*

> [!remark] Remark: The Coordinate Formulation
> Step 1 can be shortened by working with one coordinate at a time. Fix a coordinate $i$. A single term of a series of non-negative numbers is at most the sum, so
>
> $$
> \bigl| a^{(n)}_i - a^{(m)}_i \bigr| \le \Bigl( \sum_{j=1}^\infty \bigl| a^{(n)}_j - a^{(m)}_j \bigr|^p \Bigr)^{1/p} = \|a^{(n)} - a^{(m)}\|_p.
> $$
>
> Hence $\{a^{(n)}_i\}_{n \ge 1}$ is a Cauchy sequence of scalars, and since $\mathbb{R}$ and $\mathbb{C}$ are [[§10a Cauchy Sequences#^thm-10a-3|complete]] it converges:
>
> $$
> a_i := \lim_{n \to \infty} a^{(n)}_i \qquad (i = 1, 2, \ldots).
> $$
>
> Put $a = (a_1, a_2, \ldots) \in \ell$. This is the candidate. Nothing has been proved about it yet: it is not known that $a \in \ell^p$, nor that $a^{(n)} \to a$ in $\|\cdot\|_p$; only that each coordinate converges.
> As Wu noted at the end of the lecture, the two formulations are the same thing: convergence in $\mathbb{F}^k$ is coordinatewise convergence, and only the coordinates are used afterwards. A student's example of $e_1, e_2, e_1, e_2, \ldots$ (alternating) was raised as a worry for coordinatewise limits; it is not Cauchy in $\ell^p$ ($\|e_1 - e_2\|_p = 2^{1/p}$ does not go to $0$), so it is not a counterexample to anything.

^rem-18-5

> [!remark] Remark: Comparison with Lax
> Three differences of route in [[§17 Hölder's Inequality for Sequences|§17]]–[[§18 Minkowski's Inequality and the Spaces ℓᵖ|§18]]. Lax states Hölder's inequality without proof, referring to Courant; here it is proved from Young's inequality (Lemma [[§16 Means and Young's Inequality#^lem-16-3|§16.3]]). Lax obtains Minkowski's inequality from the *duality formula* $\|x\|_p = \max_{\|u\|_q = 1} |(x, u)|$ with $(x,u) = \sum_j a_j c_j$ (his Theorem 5): a maximum of sums is at most a sum of maxima, so subadditivity is immediate once the formula is known, and the formula itself rests on the equality case of Hölder. Wu's route (Theorem [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-1|§18.1]]) avoids the equality case at the price of the truncation argument. The duality formula is the first appearance of the dual-space theme that returns in Lax's Chapter 8. Finally, Lax asserts the completeness of $\ell^p$ and $\ell^\infty$ without proof (examples (a)–(b)); Theorem [[§18 Minkowski's Inequality and the Spaces ℓᵖ#^thm-18-5|§18.5]] proves it.

^rem-18-6
