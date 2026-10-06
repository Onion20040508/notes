---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 25
tags: [functional-analysis, math556]
---
← [[§24 Orthonormal Sets and Bases]] · ↑ [[· 5 Inner Product Spaces]] · [[§26 Boundedness and Continuity]] →

*Stage: inner products — Examples revisited. The spaces of Chapter 5, with the separable and non-separable examples.*

## ℝⁿ and ℂⁿ

The dot product is the model inner product, with the conjugate on the second slot over $\mathbb{C}$. Being finite-dimensional, $\mathbb{R}^n$ and $\mathbb{C}^n$ are Hilbert spaces, and for $n \ge 2$ the norm $\|\cdot\|_p$ comes from an inner product only for $p = 2$. In $\mathbb{R}^n$ a complete orthonormal set is a basis ([[§24 Orthonormal Sets and Bases#^rem-24-1|remark]]); [[§24 Orthonormal Sets and Bases|the section on orthonormal bases]] asks what replaces this in a Hilbert space.

![[§20 Definition and Examples#^ex-20-1]]

![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1]]

![[§21 Cauchy–Schwarz and the Induced Norm#^cor-21-5]]

*Chain:* ← [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]] →

## C[a,b] and C²[a,b]

The $L^2$ inner product restricted to $C[a,b]$ proves a sharp integral inequality for $C^2$ functions by Cauchy–Schwarz; [[§22 Projection and Orthogonal Decomposition#^rem-22-8|the remark after it]] finds the test function by orthogonal projection onto $\operatorname{span}\{1, x\}$.

![[§22 Projection and Orthogonal Decomposition#^prop-22-8]]

*Chain:* ← [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]] →

## ℓᵖ, ℓ², ℓ∞ and c₀

$\ell^2$ is the one $\ell^p$ whose norm comes from an inner product (and [[§21 Cauchy–Schwarz and the Induced Norm#^cor-21-5|only p = 2]] does), and it is a Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-1|example]]). The sequence spaces supply the counterexamples: in $\ell^1$ closest points need not be unique ([[§22 Projection and Orthogonal Decomposition#^rem-22-2|remark]]); $c_{00} \subset \ell^2$ shows that orthogonal decomposition needs a closed subspace; and the shifted vectors $e_{n+1}$ are orthonormal but not complete ([[§24 Orthonormal Sets and Bases#^rem-24-8|remark]]), while the standard basis is an orthonormal basis.

![[§20 Definition and Examples#^ex-20-2]]

![[§22 Projection and Orthogonal Decomposition#^rem-22-5]]

![[§24 Orthonormal Sets and Bases#^ex-24-1]]

[[§24 Orthonormal Sets and Bases#^def-24-5|Separability]] sorts the sequence spaces: $\ell^p$ for $p < \infty$ and $c_0$ are separable, $\ell^\infty$ is not.

> [!theorem] Proposition §25.1: $\ell^p$ is Separable for $1 \le p < \infty$
> Let $1 \le p < \infty$, and let $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q}$ if $\mathbb{F} = \mathbb{R}$ and $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q} + i\mathbb{Q}$ if $\mathbb{F} = \mathbb{C}$. The set
>
> $$
> D = \bigcup_{J = 1}^\infty \bigl\{ (p_1, \ldots, p_J, 0, 0, \ldots) : p_j \in \mathbb{Q}_{\mathbb{F}} \bigr\}
> $$
>
> is countable and dense in $\ell^p$. Hence $\ell^p$ is separable.

^prop-25-1

> [!proof]+ Proof
> *Countable.* For fixed $J$ the $J$-th set is in bijection with $\mathbb{Q}_{\mathbb{F}}^J$, a finite product of countable sets, hence countable; a countable union of countable sets is countable.
>
> *Dense.* Let $a = (a_j) \in \ell^p$ and $\varepsilon > 0$. Since $\sum_j |a_j|^p < \infty$, its tail is small: there is $J$ with $\sum_{j > J} |a_j|^p < (\varepsilon/2)^p$. Since $\mathbb{Q}_{\mathbb{F}}$ is dense in $\mathbb{F}$, choose $p_j \in \mathbb{Q}_{\mathbb{F}}$ with $|a_j - p_j| < \frac{\varepsilon}{2} J^{-1/p}$ for $j = 1, \ldots, J$, and let $d = (p_1, \ldots, p_J, 0, \ldots) \in D$. Then
>
> $$
> \|a - d\|_p^p = \sum_{j=1}^J |a_j - p_j|^p + \sum_{j > J} |a_j|^p < J \cdot \frac{(\varepsilon/2)^p}{J} + \Bigl(\frac{\varepsilon}{2}\Bigr)^p \le \varepsilon^p,
> $$
>
> so $\|a - d\|_p < \varepsilon$.

^pf-25-1

*Uses:* [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|Def. §16.1]], [[§24 Orthonormal Sets and Bases#^def-24-5|Def. §24.5]], [[Countable Union of Countable Sets is Countable|551 §3.1]], [[§3 Countability of Rationals and Unions#^cor-3-2|551 §3.2]]

![[m556-20-3.svg]]
*Approximating $a \in \ell^p$ by an element of $D$: the coordinates beyond $J$ (blue) are set to $0$, and the first $J$ (gray) are replaced by nearby rationals (red dots).*

The two moves of the proof: cut off the tail, which is small because the series converges, and replace the finitely many remaining coordinates by nearby rationals. Both need $p < \infty$: the tail of a convergent series is small, but a bounded sequence need not have a small tail in the supremum norm.

> [!theorem] Proposition §25.2: $c_0$ is a Separable Banach Space
> Let $c_0 = \ell^\infty_0 = \{ a = \{a_n\}_{n \in \mathbb{N}} : a_n \in \mathbb{F},\ \lim_{n \to \infty} a_n = 0 \}$ with $|a| = \max_n |a_n|$. Then $(c_0, |\cdot|)$ is a [[§11 Completeness#^def-11-2|Banach space]], and it is [[§24 Orthonormal Sets and Bases#^def-24-5|separable]].
>
> *Source: HW5, Problem 1(a)*

^prop-25-2

> [!proof]+ Proof
> (HW5, Problem 1(a).) **Step 1: the maximum exists.** Let $a \in c_0$. If $a_n = 0$ for all $n$, then $\max_n |a_n| = 0$. Otherwise choose $m$ with $\delta = |a_m| > 0$. Since $a_n \to 0$, there is $N$ with $|a_n| < \delta$ for all $n > N$. The finite set $\{|a_1|, \ldots, |a_N|\}$ contains $|a_m| = \delta$ (as $m \le N$), so it has a maximum $M \ge \delta$, and $|a_n| < \delta \le M$ for $n > N$. Hence $\max_n |a_n| = M$ exists, and $|a_n| \le |a|$ for every $n$.
>
> **Step 2: $c_0$ is a linear space.** The set of all sequences in $\mathbb{F}$ with termwise operations is a linear space: each axiom, evaluated at an index $n$, is the corresponding axiom of $\mathbb{F}$. $c_0$ is a linear subspace of it: the zero sequence tends to $0$, and if $a_n \to 0$, $b_n \to 0$ and $\alpha, \beta \in \mathbb{F}$, then $|\alpha a_n + \beta b_n| \le |\alpha|\,|a_n| + |\beta|\,|b_n| \to 0$.
>
> **Step 3: $|\cdot|$ is a norm.** *Positivity:* $|a| \ge 0$, and if $|a| = 0$ then $0 \le |a_n| \le |a| = 0$ for all $n$, so $a = 0$. *Homogeneity:* for $\alpha \in \mathbb{F}$, $|\alpha a_n| = |\alpha|\,|a_n| \le |\alpha|\,|a|$ for all $n$, with equality at an index where $|a_n| = |a|$; so $|\alpha a| = |\alpha|\,|a|$. *Triangle inequality:* for every $n$, $|a_n + b_n| \le |a_n| + |b_n| \le |a| + |b|$; taking the maximum over $n$, $|a + b| \le |a| + |b|$.
>
> **Step 4: completeness.** Let $\{a^{(k)}\}_{k \ge 1}$ be a Cauchy sequence in $c_0$, $a^{(k)} = \{a^{(k)}_n\}_n$. For each $n$ and all $k, m$, $|a^{(k)}_n - a^{(m)}_n| \le |a^{(k)} - a^{(m)}|$, so $\{a^{(k)}_n\}_k$ is a Cauchy sequence in $\mathbb{F}$; since $\mathbb{F}$ is complete it converges, and we put $a_n = \lim_{k \to \infty} a^{(k)}_n$ and $a = \{a_n\}$.
>
> *A uniform estimate.* Let $\varepsilon > 0$ and choose $N$ with $|a^{(k)} - a^{(m)}| < \varepsilon$ for all $k, m \ge N$. Then $|a^{(k)}_n - a^{(m)}_n| < \varepsilon$ for all $n$ and all $k, m \ge N$. Fix $n$ and $k \ge N$ and let $m \to \infty$; since $a^{(m)}_n \to a_n$ and non-strict inequalities survive limits,
>
> $$
> |a^{(k)}_n - a_n| \le \varepsilon \qquad \text{for all } n \text{ and all } k \ge N. \tag{5.4}
> $$
>
> *$a \in c_0$.* With $\varepsilon$ and $N$ as above, $a^{(N)} \in c_0$, so there is $n_0$ with $|a^{(N)}_n| < \varepsilon$ for $n > n_0$. By (5.4), for $n > n_0$,
>
> $$
> |a_n| \le |a_n - a^{(N)}_n| + |a^{(N)}_n| < \varepsilon + \varepsilon = 2\varepsilon .
> $$
>
> As $\varepsilon > 0$ was arbitrary, $a_n \to 0$, i.e. $a \in c_0$.
>
> *Convergence.* For $k \ge N$, $a^{(k)} - a \in c_0$ by Step 2, and by (5.4) every term of it has modulus at most $\varepsilon$; so $|a^{(k)} - a| \le \varepsilon$. Hence $a^{(k)} \to a$ in $c_0$, and $(c_0, |\cdot|)$ is a Banach space.
>
> **Step 5: $c_0$ is separable.** Let
>
> $$
> D = \bigcup_{J=1}^\infty \bigl\{ (q_1, \ldots, q_J, 0, 0, \ldots) : q_j \in \mathbb{Q}_{\mathbb{F}} \bigr\}.
> $$
>
> Each element of $D$ is eventually $0$, so $D \subset c_0$. For fixed $J$ the $J$-th set is in bijection with $\mathbb{Q}_{\mathbb{F}}^J$, which is countable, and a countable union of countable sets is countable; so $D$ is countable.
>
> Let $a \in c_0$ and $\varepsilon > 0$. Choose $J$ with $|a_n| < \varepsilon$ for all $n > J$, and, since $\mathbb{Q}_{\mathbb{F}}$ is dense in $\mathbb{F}$, choose $q_j \in \mathbb{Q}_{\mathbb{F}}$ with $|a_j - q_j| < \varepsilon$ for $j = 1, \ldots, J$. For $d = (q_1, \ldots, q_J, 0, \ldots) \in D$, every term of $a - d$ has modulus $< \varepsilon$: $|a_j - q_j| < \varepsilon$ for $j \le J$ and $|a_n - 0| < \varepsilon$ for $n > J$. Since the maximum in Step 1 is attained at some index, $|a - d| < \varepsilon$. Hence $D$ is dense, and $c_0$ is separable.

^pf-25-2

*Uses:* [[§1 Linear Spaces#^def-1-1|Def. §1.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§10 Normed Linear Spaces#^def-10-1|Def. §10.1]], [[§10 Normed Linear Spaces#^def-10-5|Def. §10.5]], [[§11 Completeness#^def-11-2|Def. §11.2]], [[§24 Orthonormal Sets and Bases#^def-24-5|Def. §24.5]], [[§25 Sequence and Function Spaces#^prop-25-1|§25.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]], [[§4 The Completeness Axiom#^thm-4-7|451 §4.7]], [[Countable Union of Countable Sets is Countable|551 §3.1]], [[§3 Countability of Rationals and Unions#^cor-3-2|551 §3.2]]

> [!remark] Remark
> $c_0$ sits inside $\ell^\infty$ ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|Def. §16.1]]) with the same norm (on $c_0$ the supremum is a maximum), and it is closed there: Step 4 is exactly the statement that a uniform limit of sequences tending to $0$ tends to $0$. The truncation argument of [[Functional Analysis Problem-Solving Techniques#^rem-t15|Technique 15]] works for $c_0$ because the tail of an element of $c_0$ is small in the supremum norm — which is precisely what fails for a general bounded sequence.

^rem-25-1

> [!theorem] Proposition §25.3: $\ell^\infty$ is Not Separable
> $\ell^\infty$ ([[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|Def. §16.1]]) is not [[§24 Orthonormal Sets and Bases#^def-24-5|separable]].

^prop-25-3

> [!proof]+ Proof
> (Not covered in lecture; the argument of HW5, Problem 1(b).) For a subset $S \subset \mathbb{N}$ let $\chi_S \in \ell^\infty$ be the sequence with $n$-th term $1$ if $n \in S$ and $0$ otherwise. If $S \neq T$, some $n$ lies in exactly one of them, so $|(\chi_S)_n - (\chi_T)_n| = 1$, while every term of $\chi_S - \chi_T$ has modulus at most $1$; hence $\|\chi_S - \chi_T\|_\infty = 1$. The set of subsets of $\mathbb{N}$ is uncountable ([[§4 Uncountability#^thm-4-1|Cantor]]). If $D$ were a countable dense subset of $\ell^\infty$, choose for each $S$ some $d_S \in D$ with $\|\chi_S - d_S\|_\infty < \frac12$. For $S \neq T$, $d_S = d_T$ would give $1 = \|\chi_S - \chi_T\|_\infty < \frac12 + \frac12$, which is impossible; so $S \mapsto d_S$ would map an uncountable set one-to-one into the countable set $D$. Hence $\ell^\infty$ is not separable.

^pf-25-3

*Uses:* [[§16 Minkowski's Inequality and the Spaces ℓᵖ#^def-16-1|Def. §16.1]], [[§24 Orthonormal Sets and Bases#^def-24-5|Def. §24.5]], [[§10 Normed Linear Spaces#^def-10-7|Def. §10.7]], [[§4 Uncountability#^thm-4-1|551 §4.1]]

> [!remark]- Connections
> - The same separated-family argument for functions: [[§25 Sequence and Function Spaces#^prop-25-5|§25.5]], and in the vault home [[§35 Lᵖ as a Banach Space#^thm-35-14|551 §35.14]]; as a technique: [[Functional Analysis Problem-Solving Techniques#^rem-t16|Technique 16]].

The shift on $\ell^2$ preserves the inner product without being onto, and every infinite-dimensional separable Hilbert space is isomorphic to $\ell^2$.

![[§24 Orthonormal Sets and Bases#^ex-24-2]]

![[§24 Orthonormal Sets and Bases#^thm-24-15]]

*Chain:* ← [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]] →

## Lᵖ and L²

$L^2(\Omega)$ carries the integral inner product and is a Hilbert space. $C_c(\mathbb{R}^n)$ with the same inner product is not complete, and its completion is $L^2(\mathbb{R}^n)$; the Sobolev spaces complete $C_c^\infty(\Omega)$ in a norm that adds the $L^2$ norms of derivatives.

![[§20 Definition and Examples#^ex-20-3]]

![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-2]]

![[§21 Cauchy–Schwarz and the Induced Norm#^ex-21-3]]

Separability splits the $L^p$ as it split the $\ell^p$:

> [!theorem] Proposition §25.4: $L^p(E)$ is Separable for $1 \le p < \infty$
> Let $E \subset \mathbb{R}^n$ be measurable and $1 \le p < \infty$. Let $D$ be the set of functions on $E$ of the form
>
> $$
> \varphi = \sum_{j=1}^N a_j\, \chi_{R_j \cap E}, \qquad N \in \mathbb{N},\ a_j \in \mathbb{Q}_{\mathbb{F}},\ R_j \text{ a rectangle with rational endpoints},
> $$
>
> where a rectangle is a product $\prod_{i=1}^n [\alpha_i, \beta_i)$. Then $D$ is countable and dense in $L^p(E)$. Hence $L^p(E)$ is separable.

^prop-25-4

> [!proof]+ Proof
> Wu's route: continuous functions are dense in $L^p$ (taken for granted), a continuous function is approximated by step functions, and the step functions can be taken with rational heights and rational rectangles. The details:
>
> *Countable.* A rectangle with rational endpoints is determined by $2n$ rationals, so there are countably many; for fixed $N$ the choices of $(a_1, \ldots, a_N, R_1, \ldots, R_N)$ form a finite product of countable sets; take the union over $N$.
>
> *Dense.* Let $f \in L^p(E)$ and $\varepsilon > 0$. Extend $f$ by $0$ to $\tilde{f}$ on $\mathbb{R}^n$; then $\tilde{f} \in L^p(\mathbb{R}^n)$ with the same norm.
>
> *Step 1: a continuous function.* By Theorem [[§17 The Function Spaces Lᵖ(Ω)#^thm-17-4|§17.4]] (with $\Omega = \mathbb{R}^n$) there is a continuous $g$ with compact support and $\|\tilde{f} - g\|_{L^p(\mathbb{R}^n)} < \varepsilon/3$. Choose $K \in \mathbb{N}$ with the support of $g$ inside $Q = [-K, K)^n$.
>
> *Step 2: a step function.* $g$ is uniformly continuous on the compact set $[-K,K]^n$. Let $\eta > 0$ with $\eta\,(2K)^{n/p} < \varepsilon/3$, and choose $\delta > 0$ with $|g(x) - g(y)| < \eta$ whenever $|x - y| < \delta$. Choose $m$ with $\sqrt{n}\,2^{-m} < \delta$ and partition $Q$ into the cubes $C_1, \ldots, C_M$ of the form $\prod_i [k_i 2^{-m}, (k_i + 1) 2^{-m})$, $k_i \in \mathbb{Z}$; they have rational endpoints. Let $c_k = g(z_k)$, $z_k$ the lower corner of $C_k$, and $\psi = \sum_k c_k \chi_{C_k}$. For $x \in C_k$, $|x - z_k| < \delta$, so $|g(x) - \psi(x)| < \eta$; outside $Q$ both vanish. Hence
>
> $$
> \|g - \psi\|_{L^p(\mathbb{R}^n)}^p = \int_Q |g - \psi|^p < \eta^p (2K)^n, \qquad \|g - \psi\|_{L^p(\mathbb{R}^n)} < \eta\,(2K)^{n/p} < \frac{\varepsilon}{3}.
> $$
>
> *Step 3: rational heights.* Choose $q_k \in \mathbb{Q}_{\mathbb{F}}$ with $|c_k - q_k| < \eta$ and let $\tilde{\varphi} = \sum_k q_k \chi_{C_k}$. As in Step 2, $|\psi - \tilde{\varphi}| < \eta$ on $Q$ and $0$ outside, so $\|\psi - \tilde{\varphi}\|_{L^p(\mathbb{R}^n)} < \varepsilon/3$.
>
> *Step 4: restrict to $E$.* $\varphi = \tilde{\varphi}|_E = \sum_k q_k \chi_{C_k \cap E} \in D$, and since $\tilde{f} = f$ on $E$,
>
> $$
> \|f - \varphi\|_{L^p(E)} \le \|\tilde{f} - \tilde{\varphi}\|_{L^p(\mathbb{R}^n)} \le \|\tilde{f} - g\| + \|g - \psi\| + \|\psi - \tilde{\varphi}\| < \varepsilon.
> $$

^pf-25-4

*Uses:* [[§17 The Function Spaces Lᵖ(Ω)#^def-17-1|Def. §17.1]], [[§17 The Function Spaces Lᵖ(Ω)#^thm-17-4|§17.4]], [[§35 Lᵖ as a Banach Space#^thm-35-12|551 §35.12]], [[Minkowski's Inequality|551 §35.2]], [[Countable Union of Countable Sets is Countable|551 §3.1]], [[§24 Orthonormal Sets and Bases#^def-24-5|Def. §24.5]]

> [!remark]- Connections
> - Vault home: [[§35 Lᵖ as a Banach Space#^cor-35-13|551 §35.13]], via density of step functions and of $C_c$ in $L^p$, [[§35 Lᵖ as a Banach Space#^thm-35-12|551 §35.12]] (its (iii) is the compactly supported density used in Step 1).
> - The companion chapter's case $L^2(\mathbb{R}^n)$: [[§32 Position Eigenstates and Continuous Resolutions#^thm-32-2|§32.2]].

![[m556-20-4.svg]]
*Step 2 and Step 3 for $n = 1$: a continuous $g$ and the step function $\varphi$ on dyadic intervals with rational heights.*

A continuous $g$ and a step function on cubes with rational endpoints and rational heights (here $n = 1$, heights rounded to quarters). The $L^p$ distance is small because it is an *integral* of a small difference over a bounded set. In $L^\infty$ the distance is a supremum, and this argument breaks down.

> [!theorem] Proposition §25.5: $L^\infty(E)$ is Not Separable
> If $E \subset \mathbb{R}^n$ is measurable with $m(E) > 0$, then $L^\infty(E)$ is not [[§24 Orthonormal Sets and Bases#^def-24-5|separable]].
>
> *Source: HW5, Problem 1(b)*

^prop-25-5

> [!proof]+ Proof
> (Stated in lecture without proof. HW5, Problem 1(b) is the case $E = [0,1]$; the general case below is Claude's.) Here $\|f\|_\infty = \inf\{M \ge 0 : |f| \le M \text{ a.e.}\}$, functions equal almost everywhere being identified.
>
> **Step 1: the case $E = [0,1]$ (HW5).** For $t \in (0,1]$ let $f_t = \chi_{[0,t]}$. Let $0 < s < t \le 1$. Then $|f_t - f_s| = \chi_{(s,t]}$, which is at most $1$ everywhere, so $\|f_t - f_s\|_\infty \le 1$. It equals $1$ on $(s,t]$, a set of measure $t - s > 0$; so for any $M < 1$ the inequality $|f_t - f_s| \le M$ fails on a set of positive measure, and $\|f_t - f_s\|_\infty \ge 1$. Hence $\|f_t - f_s\|_\infty = 1$ for $s \neq t$.
>
> Suppose $D$ is dense. For each $t \in (0,1]$ choose $d_t \in D$ with $\|f_t - d_t\|_\infty < \frac12$. If $s \neq t$ and $d_s = d_t$, then
>
> $$
> 1 = \|f_s - f_t\|_\infty \le \|f_s - d_s\|_\infty + \|d_t - f_t\|_\infty < \tfrac12 + \tfrac12 = 1,
> $$
>
> a contradiction. So $t \mapsto d_t$ is one-to-one from the [[§4 Uncountability#^ex-4-2|uncountable]] set $(0,1]$ into $D$, and $D$ is uncountable.
>
> **Step 2: general $E$ with $m(E) > 0$.** (Not part of the homework.) Let $Q_t = [-t,t]^n$ and $\varphi(t) = m(E \cap Q_t)$ for $t \ge 0$. $\varphi$ is non-decreasing and finite. It is continuous: if $t_k \uparrow t$, then $\bigcup_k Q_{t_k} = (-t,t)^n$, which differs from $Q_t$ by a null set, so $\varphi(t_k) \to \varphi(t)$ by [[§13 Approximation and Continuity of Measure#^prop-13-4|continuity of measure from below]]; if $t_k \downarrow t$, then $\bigcap_k Q_{t_k} = Q_t$ and the measures are finite, so $\varphi(t_k) \to \varphi(t)$ [[§13 Approximation and Continuity of Measure#^prop-13-5|from above]]. Also $\varphi(0) = 0$ and $\varphi(t) \to m(E) > 0$ as $t \to \infty$. Let $\gamma = m(E)$ if $m(E) < \infty$ and $\gamma = 1$ otherwise. By the [[Intermediate Value Theorem|intermediate value theorem]], for each $c \in (0, \gamma)$ there is $t_c$ with $\varphi(t_c) = c$; let $f_c = \chi_{E \cap Q_{t_c}}$. For $c < c'$, $\varphi(t_c) < \varphi(t_{c'})$ forces $t_c < t_{c'}$, so $f_{c'} - f_c = \chi_{E \cap (Q_{t_{c'}} \setminus Q_{t_c})}$, the indicator of a set of measure $c' - c > 0$. As in Step 1, $\|f_{c'} - f_c\|_\infty = 1$, and the argument of Step 1, with the uncountable index set $(0, \gamma)$, shows that no countable set is dense in $L^\infty(E)$.
>
> With the working definition of $L^\infty$ in Definition [[§17 The Function Spaces Lᵖ(Ω)#^def-17-1|§17.1]] (bounded functions with the supremum norm) the same families work verbatim, since then $\|\chi_A\| = 1$ for every nonempty $A$.

^pf-25-5

*Uses:* [[§17 The Function Spaces Lᵖ(Ω)#^def-17-1|Def. §17.1]], [[§24 Orthonormal Sets and Bases#^def-24-5|Def. §24.5]], [[§10 Normed Linear Spaces#^def-10-7|Def. §10.7]], [[§4 Uncountability#^ex-4-2|551 Ex. §4.2]], [[§13 Approximation and Continuity of Measure#^prop-13-4|551 §13.4]], [[§13 Approximation and Continuity of Measure#^prop-13-5|551 §13.5]], [[Intermediate Value Theorem|451 §18.3]]

> [!remark]- Connections
> - Vault home: [[§35 Lᵖ as a Banach Space#^thm-35-14|551 §35.14]], with the family of indicators of $(0, t)$ and, for general $E$, continuity of measure.
> - The sequence version: [[§25 Sequence and Function Spaces#^prop-25-3|§25.3]]; as a technique: [[Functional Analysis Problem-Solving Techniques#^rem-t16|Technique 16]].

![[m556-20-6.svg]]
*Step 1: $f_s = \chi_{[0,s]}$ (blue) and $f_t = \chi_{[0,t]}$ (black) differ by $1$ on $(s,t]$ (shaded).*

Any two of the functions $f_t = \chi_{[0,t]}$ differ by $1$ on an interval of positive length, so they are at $L^\infty$-distance $1$: uncountably many points, pairwise $1$ apart. Balls of radius $\frac12$ about them are disjoint, and a dense set would need a point in each. In $L^p$, $p < \infty$, the same two functions are at distance $(t-s)^{1/p}$, which is small when $t$ is close to $s$.

> [!remark] Remark
> The hypothesis $m(E) > 0$ is added here: if $m(E) = 0$, then $L^\infty(E) = \{0\}$, which is separable. Wu stressed that measure theory supplies the examples of functional analysis (“I would suggest you really study real methods … measure theory is becoming very useful now”): without $L^p$ the course has few examples beyond sequence spaces.

^rem-25-2

*Chain:* ← [[§19 ℝⁿ, C［a,b］, ℓᵖ and Lᵖ|Chapter 4]] · [[§29 ℝⁿ, Cᵐ and Lᵖ|Chapter 6]] →

## Even and Odd Functions

In $L^2[-1,1]$ the even and the odd functions are closed subspaces, each the orthogonal complement of the other, and $f = f_e + f_o$ is the orthogonal decomposition.

![[§22 Projection and Orthogonal Decomposition#^prop-22-7]]

*Chain:* [[§31 The Completeness Relation#^ex-31-1|Chapter 7 (parity)]] →

## The Fourier Basis

The functions $e^{inx}/\sqrt{2\pi}$, $n \in \mathbb{Z}$, form an orthonormal basis of $L^2[0,2\pi]$. Read through [[§24 Orthonormal Sets and Bases#^thm-24-8|the characterization of orthonormal bases]], this is the $L^2$ theory of Fourier series, and taking coefficients identifies $L^2[0,2\pi]$ with $\ell^2(\mathbb{Z})$ ([[§24 Orthonormal Sets and Bases#^rem-24-13|remark]]).

![[§24 Orthonormal Sets and Bases#^thm-24-11]]

![[§24 Orthonormal Sets and Bases#^rem-24-9]]

*Chain:* [[§26 Boundedness and Continuity#^ex-26-2|Chapter 6 (the Fourier transform)]] · [[§31 The Completeness Relation#^ex-31-2|Chapter 7 (a particle on a ring)]] →
