---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 27
tags: [functional-analysis, math556]
---
← [[§26 Bounded Linear Functionals and the Riesz Representation Theorem]] · ↑ [[· 5 Inner Product Spaces]] · [[§28 Existence of Orthonormal Bases and Separability]] →

*Stage: inner products — Threads: dimension, completeness. Countable support, Bessel and Parseval: bases in infinite dimensions.*

## Orthonormal Sets

> [!definition] Definition §27.1: Orthogonal and Orthonormal Sets
> Let $X$ be an inner product space and $\{e_\alpha\}_{\alpha \in \Lambda} \subset X$, indexed by an arbitrary set $\Lambda$. The family is **orthogonal** if $e_\alpha \perp e_\beta$ for all $\alpha, \beta \in \Lambda$ with $\alpha \neq \beta$. It is **orthonormal** if in addition $\|e_\alpha\| = 1$ for every $\alpha \in \Lambda$.
>
> *Lax: §6.4, definition of orthonormal set*

^def-27-1

> [!remark]- Connections
> - The finite-dimensional version (orthonormal lists): [[§21 Orthonormal Bases#^ladr-6-22|LADR 6.22]].
> - Computational version: [[§51 Orthogonal Sets#^def-51-1|235 Def. §51.1]] (orthogonal sets in ℝⁿ), [[§51 Orthogonal Sets#^def-51-4|235 Def. §51.4]] (orthonormal sets and bases).
> - Computational version: orthogonal families of functions computed by hand: the trigonometric system, [[§9 Periodic Functions and Fourier Series#^prop-9-3|341 Prop. §9.3]]; the eigenfunctions of a Sturm–Liouville problem, orthogonal with weight $p$, [[§29 Sturm–Liouville Problems#^thm-29-2|341 Thm. §29.2]]; the Bessel functions $J_0(\lambda_nr)$, orthogonal with weight $r$, [[§57★ Temperature in a Cylinder#^prop-57-2|341 Prop. §57.2]].

> [!definition] Definition §27.2: Complete Orthogonal Set
> An orthogonal set $\{e_\alpha\}_{\alpha \in \Lambda}$ in $X$ is **complete** if the only vector orthogonal to all of its members is $0$:
>
> $$
> (x, e_\alpha) = 0 \ \text{ for all } \alpha \in \Lambda \quad \Longrightarrow \quad x = 0 .
> $$

^def-27-2

> [!remark] Remark
> Completeness of an orthogonal set is unrelated to completeness of a space. It means the set cannot be enlarged: if some nonzero $x$ were orthogonal to every $e_\alpha$, it could be added to the set, which therefore could not be a basis. In $\mathbb{R}^n$, a complete orthonormal set $\{e_1, \ldots, e_n\}$ is a basis, and every $x$ is $x = \sum_{j=1}^n (x, e_j)\, e_j$. The question is whether the same is true in a Hilbert space.

^rem-27-1

> [!remark] Remark: What Should “Basis” Mean
> The natural definition is that every $x \in H$ satisfies $x = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$. But the right side need not make sense a priori. Adding finitely many vectors is part of the linear structure; adding infinitely many requires a limit (compare [[§1 Linear Spaces#^rem-1-5|the remark on finite sums]] in [[§1 Linear Spaces#Linear Span|§1]]); and $\Lambda$ may be uncountable, in which case it is not even clear in what order to add. The following results make sense of it in three steps: for each $x$ only countably many coefficients $(x, e_\alpha)$ are nonzero ([[§27 Orthonormal Sets and Bases#^prop-27-4|§27.4]]); the sum of their squares is at most $\|x\|^2$ ([[§27 Orthonormal Sets and Bases#^thm-27-5|Bessel]]); and the vector series then converges in $H$ ([[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]]). Only the last step uses completeness of $H$; the first two hold in any inner product space.

^rem-27-2

## Pythagoras and Bessel's Inequality

> [!theorem] Lemma §27.1: Pythagoras
> Let $X$ be an inner product space.
> - (a) If $u \perp v$, then $\|u + v\|^2 = \|u\|^2 + \|v\|^2$.
> - (b) If $e_1, \ldots, e_k$ are orthonormal and $c_1, \ldots, c_k \in \mathbb{F}$, then $\bigl\| \sum_{j=1}^k c_j e_j \bigr\|^2 = \sum_{j=1}^k |c_j|^2$.

^lem-27-1

> [!proof]+ Proof
> (a) By [[§23 Cauchy–Schwarz and the Induced Norm#^pf-23-1|(5.1)]] with $t = 1$, $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}(v, u) + \|v\|^2$, and $(v, u) = 0$.
>
> (b) Induction on $k$; the case $k = 1$ is $\|c_1 e_1\|^2 = |c_1|^2$. For the step, $u = \sum_{j < k} c_j e_j$ and $v = c_k e_k$ are orthogonal, since $(u, v) = \sum_{j<k} c_j \bar{c}_k (e_j, e_k) = 0$; so by (a) and the induction hypothesis, $\|u + v\|^2 = \sum_{j<k} |c_j|^2 + |c_k|^2$.

^pf-27-1

*Uses:* [[§23 Cauchy–Schwarz and the Induced Norm#^pf-23-1|§23.1 (5.1)]], [[§27 Orthonormal Sets and Bases#^def-27-1|Def. §27.1]]

> [!remark]- Connections
> - Finite-dimensional home: (a) is [[§20 Inner Products and Norms#^ladr-6-12|LADR 6.12]], (b) is [[§21 Orthonormal Bases#^ladr-6-24|LADR 6.24]].
> - Computational version: (a) in ℝⁿ is [[§49 Inner Product, Length, and Orthogonality#^thm-49-4|235 Thm. §49.4]].

> [!theorem] Lemma §27.2: Finite Bessel Inequality
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal in an inner product space $X$, let $e_1, \ldots, e_k$ be finitely many distinct members of it, and $x \in X$. Put $y = x - \sum_{j=1}^k (x, e_j)\, e_j$. Then $y \perp e_i$ for $i = 1, \ldots, k$, and
>
> $$
> \|x\|^2 = \|y\|^2 + \sum_{j=1}^k |(x, e_j)|^2 ; \qquad \text{in particular} \qquad \sum_{j=1}^k |(x, e_j)|^2 \le \|x\|^2 .
> $$

^lem-27-2

> [!proof]+ Proof
> For each $i$, taking the scalars $(x, e_j)$ out of the first slot,
>
> $$
> (y, e_i) = (x, e_i) - \sum_{j=1}^k (x, e_j)\,(e_j, e_i) = (x, e_i) - (x, e_i) = 0,
> $$
>
> since $(e_j, e_i) = 0$ for $j \neq i$ and $(e_i, e_i) = 1$. Hence $y$ is orthogonal to $\sum_j (x, e_j) e_j$ (conjugate-linearity in the second slot), and $x = y + \sum_j (x, e_j) e_j$. By Lemma [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]](a) and then (b), $\|x\|^2 = \|y\|^2 + \bigl\|\sum_j (x, e_j) e_j\bigr\|^2 = \|y\|^2 + \sum_j |(x, e_j)|^2$.

^pf-27-2

*Uses:* [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]], [[§27 Orthonormal Sets and Bases#^def-27-1|Def. §27.1]]

> [!remark]- Connections
> - Finite-dimensional home: [[§21 Orthonormal Bases#^ladr-6-26|LADR 6.26]] (Bessel's inequality for an orthonormal list).
> - Computational version: [[§56 Inner Product Spaces#^prop-56-3|235 Prop. §56.3]] (the projection onto a finite-dimensional subspace is shorter, the step to Cauchy–Schwarz there) with [[§52 Orthogonal Projections#^thm-52-4|235 Thm. §52.4]] (projection from an orthonormal basis).
> - Computational version: [[§15★ Mean Error and Convergence in Mean#^thm-15-2|341 Thm. §15.2]] (the truncated Fourier series has the smallest mean square error, and the minimum is $\int f^2$ minus the weighted sum of the squared coefficients).

![[m556-20-1.svg]]
*$x$ split into its component $\sum_j (x, e_j) e_j$ (red) in $\operatorname{span}\{e_1, \ldots, e_k\}$ and the remainder $y$ (blue) perpendicular to it. Pythagoras across the right angle is the identity $\|x\|^2 = \|y\|^2 + \sum_j |(x, e_j)|^2$; dropping the blue leg is Bessel.*

The picture Wu described: $\sum_j (x, e_j) e_j$ is the orthogonal projection of $x$ onto $\operatorname{span}\{e_1, \ldots, e_k\}$, and $y$ is the perpendicular remainder. Pythagoras ([[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]]) applied to $k + 1$ orthogonal pieces gives the identity; dropping $\|y\|^2$ gives the inequality.

> [!definition] Definition §27.3: Sums of Non-Negative Families
> Let $(t_\alpha)_{\alpha \in \Lambda}$ be real numbers with $t_\alpha \ge 0$ whose **support** $S = \{ \alpha \in \Lambda : t_\alpha \neq 0 \}$ is countable. Define
>
> $$
> \sum_{\alpha \in \Lambda} t_\alpha := \sum_{n} t_{\alpha_n} \in [0, \infty],
> $$
>
> where $\alpha_1, \alpha_2, \ldots$ is an enumeration of $S$ (a finite sum if $S$ is finite, and $0$ if $S = \varnothing$).

^def-27-3

> [!theorem] Lemma §27.3: The Sum Does Not Depend on the Enumeration
> In Definition [[§27 Orthonormal Sets and Bases#^def-27-3|§27.3]],
>
> $$
> \sum_{\alpha \in \Lambda} t_\alpha = \sup \Bigl\{ \sum_{\alpha \in F} t_\alpha : F \subset \Lambda \text{ finite} \Bigr\} ;
> $$
>
> in particular the sum is independent of the enumeration of $S$.

^lem-27-3

> [!proof]+ Proof
> (Not covered in lecture.) Let $T$ be the supremum. Each partial sum $\sum_{n \le N} t_{\alpha_n}$ is a sum over a finite subset of $\Lambda$, so it is at most $T$, and hence so is the limit of these increasing partial sums. Conversely, for finite $F \subset \Lambda$, the finite set $F \cap S$ is contained in $\{\alpha_1, \ldots, \alpha_N\}$ for some $N$, and terms outside $S$ vanish; so $\sum_{\alpha \in F} t_\alpha \le \sum_{n \le N} t_{\alpha_n} \le \sum_n t_{\alpha_n}$. Taking the supremum over $F$ gives $T \le \sum_n t_{\alpha_n}$.

^pf-27-3

*Uses:* [[§27 Orthonormal Sets and Bases#^def-27-3|Def. §27.3]]

> [!theorem] Proposition §27.4: Only Countably Many Coefficients are Nonzero
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal in an inner product space $X$, and $x \in X$. Then the set
>
> $$
> S_x = \{ \alpha \in \Lambda : (x, e_\alpha) \neq 0 \}
> $$
>
> is countable (finite or countably infinite).

^prop-27-4

> [!proof]+ Proof
> For $k \in \mathbb{N}$ let $\Lambda_k = \{ \alpha \in \Lambda : |(x, e_\alpha)| \ge 1/k \}$.
>
> *Each $\Lambda_k$ is finite, with at most $k^2\|x\|^2$ elements.* Let $e_1, \ldots, e_l$ be any finitely many distinct members with indices in $\Lambda_k$. By Lemma [[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]],
>
> $$
> \frac{l}{k^2} \le \sum_{i=1}^l |(x, e_i)|^2 \le \|x\|^2, \qquad \text{so} \qquad l \le k^2\|x\|^2 .
> $$
>
> Thus every finite subset of $\Lambda_k$ has at most $k^2\|x\|^2$ elements, so $\Lambda_k$ itself is finite with at most that many. (Only finite subsets can be fed into Lemma [[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]]; the bound on all of them is what shows $\Lambda_k$ is not infinite.)
>
> *Conclusion.* If $(x, e_\alpha) \neq 0$ then $|(x, e_\alpha)| \ge 1/k$ for some $k$, so $S_x = \bigcup_{k=1}^\infty \Lambda_k$, a countable union of finite sets, hence countable.

^pf-27-4

*Uses:* [[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]], [[Countable Union of Countable Sets is Countable|551 §3.1]]

![[m556-20-5.svg]]
*The coefficients $|(x, e_\alpha)|$ over an index set $\Lambda$ that may be uncountable. The finite Bessel inequality caps how many can reach any level: at most $k^2\|x\|^2$ of them lie on or above $\tfrac1k$ (red, the set $\Lambda_k$). Every nonzero coefficient clears some level $\tfrac1k$, so the support $S_x = \bigcup_k \Lambda_k$ is a countable union of finite sets, however large $\Lambda$ is.*

> [!remark] Remark
> A student read this as saying that every vector “lives in a countably-infinite-dimensional part” of $H$; Wu separated the two concepts. The proposition is about one fixed $x$: its coefficients vanish outside a countable set $S_x$. Different $x$ can have different, even disjoint, supports, and $\Lambda$ itself can be uncountable. Nothing about bases or dimension is being asserted yet. Another question: the norm $\|x\|$ is a real number, finite by definition, so the bound $k^2\|x\|^2$ is finite.

^rem-27-3

> [!theorem] Theorem §27.5: Bessel's Inequality
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal in an inner product space $X$. For every $x \in X$,
>
> $$
> \sum_{\alpha \in \Lambda} |(x, e_\alpha)|^2 \le \|x\|^2 .
> $$
>
> The left side is defined by Definition [[§27 Orthonormal Sets and Bases#^def-27-3|§27.3]], whose hypothesis holds by Proposition [[§27 Orthonormal Sets and Bases#^prop-27-4|§27.4]].

^thm-27-5

> [!proof]+ Proof
> Enumerate $S_x$ as $\alpha_1, \alpha_2, \ldots$ and write $e_n = e_{\alpha_n}$. By Lemma [[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]], $\sum_{j=1}^n |(x, e_j)|^2 \le \|x\|^2$ for every $n$. If $S_x$ is finite this is the claim. Otherwise the partial sums form an increasing sequence bounded by $\|x\|^2$; letting $n \to \infty$ gives $\sum_{j=1}^\infty |(x, e_j)|^2 \le \|x\|^2$, which is the claim. (Equivalently, by Lemma [[§27 Orthonormal Sets and Bases#^lem-27-3|§27.3]]: the sum is a supremum of finite sums, each at most $\|x\|^2$.)

^pf-27-5

*Uses:* [[§27 Orthonormal Sets and Bases#^prop-27-4|§27.4]], [[§27 Orthonormal Sets and Bases#^def-27-3|Def. §27.3]], [[§27 Orthonormal Sets and Bases#^lem-27-2|§27.2]], [[§27 Orthonormal Sets and Bases#^lem-27-3|§27.3]]

> [!remark]- Connections
> - Finite-dimensional home: [[§21 Orthonormal Bases#^ladr-6-26|LADR 6.26]].
> - Equality holds exactly for complete sets: Parseval, [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]].
> - Computational version: [[§15★ Mean Error and Convergence in Mean#^thm-15-3|341 Thm. §15.3]] (Bessel's inequality for Fourier series); its consequence that the coefficients tend to 0, [[§15★ Mean Error and Convergence in Mean#^cor-15-5|341 Cor. §15.5]], is the step that proves pointwise convergence, [[§16★ Proof of Convergence#^lem-16-3|341 Lemma §16.3]].

## Orthonormal Expansions

> [!theorem] Proposition §27.6: The Orthonormal Expansion Converges
> Let $H$ be a Hilbert space, $\{e_\alpha\}_{\alpha \in \Lambda}$ an orthonormal set, and $x \in H$. Enumerate $S_x = \{\alpha : (x, e_\alpha) \neq 0\}$ as $\alpha_1, \alpha_2, \ldots$ and write $e_n = e_{\alpha_n}$. Then the partial sums
>
> $$
> s_n = \sum_{j=1}^n (x, e_j)\, e_j
> $$
>
> converge in $H$, and the limit does not depend on the enumeration. It is denoted $\sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$. (If $S_x$ is finite this is a finite sum.)

^prop-27-6

> [!proof]+ Proof
> Assume $S_x$ is countably infinite; otherwise there is nothing to prove.
>
> *Convergence.* By completeness of $H$ it suffices to show that $\{s_n\}$ is Cauchy. For $m < n$, Lemma [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]](b) gives
>
> $$
> \|s_n - s_m\|^2 = \Bigl\| \sum_{j=m+1}^n (x, e_j)\, e_j \Bigr\|^2 = \sum_{j=m+1}^n |(x, e_j)|^2 .
> $$
>
> The series $\sum_{j=1}^\infty |(x, e_j)|^2$ converges, by Bessel's inequality (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-5|§27.5]]): it is a series of non-negative terms with partial sums bounded by $\|x\|^2$. So its tails tend to $0$, and $\|s_n - s_m\| \to 0$ as $m, n \to \infty$.
>
> *Independence of the enumeration.* (Not covered in lecture.) Write $c_\alpha = (x, e_\alpha)$. Let $\beta_1, \beta_2, \ldots$ be a second enumeration of $S_x$, with partial sums $t_m$; let $s = \lim s_n$, $t = \lim t_m$. Given $\varepsilon > 0$, choose $N_0$ with $\sum_{j > N_0} |c_{\alpha_j}|^2 < \varepsilon$, and let $F = \{\alpha_1, \ldots, \alpha_{N_0}\}$. For all large $n$ and $m$, both $A = \{\alpha_1, \ldots, \alpha_n\}$ and $B = \{\beta_1, \ldots, \beta_m\}$ contain $F$. Then $s_n - t_m = \sum_{\alpha \in A \setminus B} c_\alpha e_\alpha - \sum_{\alpha \in B \setminus A} c_\alpha e_\alpha$ is a finite combination of distinct $e_\alpha$ with indices in $S_x \setminus F$, so by Lemma [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]](b),
>
> $$
> \|s_n - t_m\|^2 = \sum_{\alpha \in A \triangle B} |c_\alpha|^2 \le \sum_{j > N_0} |c_{\alpha_j}|^2 < \varepsilon .
> $$
>
> Letting $n, m \to \infty$ and using [[§11 Normed Linear Spaces#^prop-11-4|continuity of the norm]], $\|s - t\|^2 \le \varepsilon$. As $\varepsilon$ was arbitrary, $s = t$.

^pf-27-6

*Uses:* [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Def. §23.1]], [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]], [[§27 Orthonormal Sets and Bases#^thm-27-5|§27.5]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]

> [!remark] Remark
> Completeness of $H$ is used exactly once, to turn the Cauchy sequence of partial sums into a limit; everything before it (countable support, Bessel) holds in any inner product space. The independence of the enumeration was not addressed in lecture, but it is needed for the notation $\sum_{\alpha \in \Lambda}$ to mean anything: a series of vectors, like a conditionally convergent series of numbers, could in principle depend on the order of summation. Orthogonality prevents this.

^rem-27-4

> [!theorem] Lemma §27.7: Coefficients and Norm of the Expansion
> Let $H$ be a Hilbert space, $\{e_\alpha\}_{\alpha \in \Lambda}$ orthonormal, $x \in H$, and $s = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$. Then
> - (a) $(s, e_\beta) = (x, e_\beta)$ for every $\beta \in \Lambda$;
> - (b) $\|s\|^2 = \sum_{\alpha \in \Lambda} |(x, e_\alpha)|^2$.

^lem-27-7

> [!proof]+ Proof
> With $s_n$ as in Proposition [[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]], $s_n \to s$. (If $S_x$ is finite, take $s_n = s$ for all large $n$.)
>
> (a) Fix $\beta \in \Lambda$. By orthonormality, $(s_n, e_\beta) = \sum_{j \le n} (x, e_j)(e_j, e_\beta)$ equals $(x, e_\beta)$ if $\beta \in \{\alpha_1, \ldots, \alpha_n\}$ and $0$ otherwise. If $\beta \in S_x$, then $\beta = \alpha_j$ for some $j$, and $(s_n, e_\beta) = (x, e_\beta)$ for all $n \ge j$. If $\beta \notin S_x$, then $(s_n, e_\beta) = 0 = (x, e_\beta)$ for all $n$. In both cases $(s_n, e_\beta) \to (x, e_\beta)$, while $(s_n, e_\beta) \to (s, e_\beta)$ by continuity of the inner product (Lemma [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]]). So $(s, e_\beta) = (x, e_\beta)$.
>
> (b) By Lemma [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]](b), $\|s_n\|^2 = \sum_{j \le n} |(x, e_j)|^2$. Let $n \to \infty$: the left side tends to $\|s\|^2$ by [[§11 Normed Linear Spaces#^prop-11-4|continuity of the norm]], and the right side to $\sum_\alpha |(x, e_\alpha)|^2$ by Definition [[§27 Orthonormal Sets and Bases#^def-27-3|§27.3]].

^pf-27-7

*Uses:* [[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]], [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]], [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]], [[§27 Orthonormal Sets and Bases#^def-27-3|Def. §27.3]]

> [!remark]- Connections
> - Computational version: [[§30 Expansion in Series of Eigenfunctions#^prop-30-1|341 Prop. §30.1]] (the coefficients of an eigenfunction expansion, found by taking the weighted inner product with $\phi_m$ term by term).

> [!remark] Remark
> Part (a) is the step Wu flagged as “the only non-trivial part”: taking the inner product with $e_\beta$ term by term through an infinite sum. It is legitimate because the sum is a limit of finite sums and the inner product is continuous; her advice, “if you are not sure, start with a finite sum and take the limit,” is exactly this proof.

^rem-27-5

## Orthonormal Bases

> [!definition] Definition §27.4: Orthonormal Basis
> An orthonormal set $\{e_\alpha\}_{\alpha \in \Lambda}$ in a Hilbert space $H$ is an **orthonormal basis** of $H$ if
>
> $$
> x = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha \qquad \text{for every } x \in H,
> $$
>
> the sum being understood as in Proposition [[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]].
>
> *Lax: §6.4, definition of orthonormal base (via closed linear span; see Proposition [[§27 Orthonormal Sets and Bases#^prop-27-9|§27.9]])*

^def-27-4

> [!remark]- Connections
> - Finite-dimensional home: [[§21 Orthonormal Bases#^ladr-6-27|LADR 6.27]], where an orthonormal basis is an orthonormal list that is also a basis; here the expansion is a series, not a finite linear combination.
> - Computational version: [[§51 Orthogonal Sets#^def-51-4|235 Def. §51.4]] (orthonormal basis of a subspace of ℝⁿ, a finite basis).
> - Computational version: eigenfunction expansions with generalized Fourier coefficients, [[§30 Expansion in Series of Eigenfunctions#^def-30-2|341 Def. §30.2]]; their convergence for a regular Sturm–Liouville problem, [[§30 Expansion in Series of Eigenfunctions#^thm-30-2|341 Thm. §30.2]], is stated there without proof.

> [!theorem] Theorem §27.8: Characterizations of an Orthonormal Basis
> Let $H$ be a Hilbert space and $\{e_\alpha\}_{\alpha \in \Lambda}$ an orthonormal set. The following are equivalent:
> - (1) $\{e_\alpha\}_{\alpha \in \Lambda}$ is complete;
> - (2) $\{e_\alpha\}_{\alpha \in \Lambda}$ is an orthonormal basis of $H$;
> - (3) (**Parseval's equality**) $\|x\|^2 = \sum_{\alpha \in \Lambda} |(x, e_\alpha)|^2$ for every $x \in H$.
>
> *Lax: §6.4, Lemma 8*

^thm-27-8

> [!proof]+ Proof
> Write $s(x) = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$ (Proposition [[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]]).
>
> (1)$\Rightarrow$(2). Let $x \in H$ and $y = x - s(x)$. For every $\beta \in \Lambda$, Lemma [[§27 Orthonormal Sets and Bases#^lem-27-7|§27.7]](a) gives $(y, e_\beta) = (x, e_\beta) - (s(x), e_\beta) = 0$. So $y$ is orthogonal to every $e_\beta$, and completeness gives $y = 0$, i.e. $x = s(x)$.
>
> (2)$\Rightarrow$(3). $x = s(x)$, so by Lemma [[§27 Orthonormal Sets and Bases#^lem-27-7|§27.7]](b), $\|x\|^2 = \|s(x)\|^2 = \sum_\alpha |(x, e_\alpha)|^2$.
>
> (3)$\Rightarrow$(1). If $(x, e_\alpha) = 0$ for all $\alpha$, then Parseval's equality gives $\|x\|^2 = 0$, so $x = 0$.

^pf-27-8

*Uses:* [[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]], [[§27 Orthonormal Sets and Bases#^lem-27-7|§27.7]], [[§27 Orthonormal Sets and Bases#^def-27-2|Def. §27.2]], [[§27 Orthonormal Sets and Bases#^def-27-4|Def. §27.4]]

> [!remark]- Connections
> - Finite-dimensional home (expansion and Parseval in an orthonormal basis): [[§21 Orthonormal Bases#^ladr-6-30|LADR 6.30]].
> - Restated in Dirac notation as the completeness relation: [[§35 The Completeness Relation#^thm-35-2|§35.2]], [[§35 The Completeness Relation#^cor-35-4|§35.4]].
> - Used in Electromagnetism: the completeness of the Legendre polynomials in $L^2[-1, 1]$, which justifies expanding boundary potentials in Legendre series — [[§B3.4 Separation of Variables in Spherical Coordinates#^thm-b3-4-2|EM Theorem §B3.4.2]]. At level C: orthonormality, completeness and closure of the separated eigenfunctions of electrostatics — [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]].
> - Computational version: the finite expansion with the same coefficients, [[§51 Orthogonal Sets#^thm-51-2|235 Thm. §51.2]]; why the 235 lectures’ “basis” of harmonics is one only in this series sense, [[§31 Linearly Independent Sets; Bases#^rem-31-4|235 Remark §25.4]].
> - Computational version: Parseval's equality for Fourier series, [[§15★ Mean Error and Convergence in Mean#^thm-15-4|341 Thm. §15.4]] (used to sum series such as $\sum1/n^4$), and for normalized eigenfunctions, [[§30 Expansion in Series of Eigenfunctions#^rem-30-1|341 Remark §24.1]].

> [!remark] Remark
> In finite dimensions these are the familiar facts: a complete orthonormal set is a basis, every vector is the sum of its components, and its squared length is the sum of the squared components. The theorem says that all three survive in any Hilbert space once the sums are interpreted correctly — countable support, then convergence — and that [[§27 Orthonormal Sets and Bases#^thm-27-5|Bessel's inequality]] becomes an equality exactly for complete sets.

^rem-27-6

> [!theorem] Proposition §27.9: Lax's Definition of Orthonormal Base Agrees
> An orthonormal set $E = \{e_\alpha\}_{\alpha \in \Lambda}$ in a Hilbert space $H$ is complete if and only if its closed linear span is $H$. Consequently the following are equivalent: $E$ is an orthonormal basis in the sense of Definition [[§27 Orthonormal Sets and Bases#^def-27-4|§27.4]]; $\overline{\operatorname{span}}\, E = H$ (Lax's definition).
>
> *Lax: §6.4, definition of orthonormal base and Thm 7*

^prop-27-9

> [!proof]+ Proof
> (Not covered in lecture.) Let $Y = \overline{\operatorname{span}}\, E$, a closed linear subspace (Definition [[§11 Normed Linear Spaces#^def-11-9|§11.9]]). We claim $E^\perp = Y^\perp$. Since $E \subset Y$, every vector orthogonal to $Y$ is orthogonal to $E$. Conversely, if $v \perp e_\alpha$ for all $\alpha$, then $v$ is orthogonal to every finite linear combination of the $e_\alpha$ (conjugate-linearity in the second slot), and to every limit $y$ of such combinations $y_n$, since $(v, y) = \lim (v, y_n) = 0$ by Lemma [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]]; so $v \in Y^\perp$.
>
> By Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]], $H = Y \oplus Y^\perp$. If $Y^\perp = \{0\}$, then every $x \in H$ lies in $Y$, so $Y = H$. If $Y = H$, then $Y^\perp = \{0\}$, since $v \perp v$ forces $v = 0$. Hence $E$ is complete ($E^\perp = \{0\}$) iff $Y^\perp = \{0\}$ iff $Y = H$. The last sentence follows by Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]].

^pf-27-9

*Uses:* [[§11 Normed Linear Spaces#^def-11-9|Def. §11.9]], [[§25 Projection and Orthogonal Decomposition#^def-25-1|Def. §25.1]], [[§25 Projection and Orthogonal Decomposition#^def-25-2|Def. §25.2]], [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]], [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]], [[§27 Orthonormal Sets and Bases#^def-27-2|Def. §27.2]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]

> [!remark]- Connections
> - The same two steps proved earlier for arbitrary sets: $E^\perp = Y^\perp$ is [[§25 Projection and Orthogonal Decomposition#^lem-25-5|§25.5]], and $\overline{\operatorname{span}}\,E = (E^\perp)^\perp$ is [[§25 Projection and Orthogonal Decomposition#^thm-25-6|§25.6]].

> [!remark] Remark: Comparison with Lax
> Lax defines an orthonormal base by the condition $\overline{\operatorname{span}}\, E = H$, and his Lemma 8 then describes the closed linear span as the set of sums $\sum_j a_j e_j$ with $\sum_j |a_j|^2 < \infty$, for a countable orthonormal set. Wu defines a basis by the expansion $x = \sum_\alpha (x, e_\alpha) e_\alpha$ and proves the equivalence with completeness (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]); the proposition above connects the two. Lax also constructs orthonormal bases by [[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|Gram–Schmidt]] (Theorem $9'$) and identifies the isometries of $H$ (Theorem 10); neither was covered in lecture.

^rem-27-7

> [!theorem] Proposition §27.10: Small Perturbations of a Complete Orthonormal Set
> Let $\{e_n\}_{n \ge 1}$ and $\{f_n\}_{n \ge 1}$ be orthonormal sets in a Hilbert space $H$ with $\sum_{n=1}^\infty \|e_n - f_n\|^2 < 1$. If $\{e_n\}$ is complete, so is $\{f_n\}$.
>
> *Source: HW4, Problem 3*

^prop-27-10

> [!proof]+ Proof
> (HW4, Problem 3.) Let $c = \sum_n \|e_n - f_n\|^2 < 1$ and suppose $(x, f_n) = 0$ for all $n$. Then $(x, e_n) = (x, e_n - f_n)$, so $|(x, e_n)| \le \|x\|\,\|e_n - f_n\|$ by [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]]. By Parseval's equality for the complete set $\{e_n\}$ (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]),
>
> $$
> \|x\|^2 = \sum_n |(x, e_n)|^2 \le \|x\|^2 \sum_n \|e_n - f_n\|^2 = c\,\|x\|^2,
> $$
>
> so $(1 - c)\|x\|^2 \le 0$ and $x = 0$.

^pf-27-10

*Uses:* [[§27 Orthonormal Sets and Bases#^def-27-2|Def. §27.2]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]

> [!remark] Remark
> The proof never uses that the $f_n$ are orthonormal beyond making completeness of $\{f_n\}$ a meaningful notion; the mechanism is that $x \perp f_n$ makes each coefficient $(x, e_n)$ small, and Parseval turns “all coefficients small in $\ell^2$” into “$\|x\|$ smaller than itself”. Some hypothesis of this kind is needed: in $\ell^2$ the shifted sequence $f_n = e_{n+1}$ is orthonormal but not complete ($e_1 \perp f_n$ for all $n$), and there $\sum_n \|e_n - f_n\|^2 = \infty$.

^rem-27-8

## Examples

> [!example] Example §27.1: The Standard Basis of $\ell^2$
> In $\ell^2$ with $(a, b) = \sum_j a_j \overline{b_j}$, let $e_j = (0, \ldots, 0, 1, 0, \ldots)$ with the $1$ in the $j$-th place. Then $(e_i, e_j) = \delta_{ij}$, so $\{e_j\}_{j \ge 1}$ is orthonormal, and $(a, e_j) = a_j$. It is complete: if $(a, e_j) = a_j = 0$ for all $j$ then $a = 0$. By Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]] it is an orthonormal basis: $a = \sum_j a_j e_j$ in $\ell^2$, and Parseval's equality is $\|a\|_2^2 = \sum_j |a_j|^2$, the definition of the norm.

^ex-27-1

> [!theorem] Theorem §27.11: The Fourier Basis of $L^2[0,2\pi]$
> In the complex space $L^2[0,2\pi]$, the functions
>
> $$
> e_n(x) = \frac{1}{\sqrt{2\pi}}\, e^{inx}, \qquad n \in \mathbb{Z},
> $$
>
> form an orthonormal basis.

^thm-27-11

> [!proof]+ Proof
> *Orthonormality.* $\|e_n\|^2 = \frac{1}{2\pi}\int_0^{2\pi} e^{inx}\, \overline{e^{inx}}\, dx = \frac{1}{2\pi}\int_0^{2\pi} 1\, dx = 1$. For $k \neq j$,
>
> $$
> (e_k, e_j) = \frac{1}{2\pi}\int_0^{2\pi} e^{i(k-j)x}\, dx = \frac{1}{2\pi}\Bigl[ \frac{e^{i(k-j)x}}{i(k-j)} \Bigr]_0^{2\pi} = 0,
> $$
>
> since $e^{i(k-j)2\pi} = 1$.
>
> *Completeness.* Deferred: not proved in lecture (“I don't think I want to prove this”). It is the completeness of Fourier series, proved for instance by showing that trigonometric polynomials are dense in $L^2[0,2\pi]$ (Fejér's theorem gives uniform approximation of continuous periodic functions, and continuous periodic functions are dense in $L^2$). Given completeness, Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]] makes it a basis.

^pf-27-11

*Uses:* [[§27 Orthonormal Sets and Bases#^def-27-1|Def. §27.1]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]

> [!remark]- Connections
> - The real trigonometric orthonormal list on $[-\pi, \pi]$ in finite dimensions: [[§21 Orthonormal Bases#^ladr-6-23|LADR 6.23]](d).
> - Used for the particle on a ring: [[§35 The Completeness Relation#^ex-35-2|Ex. §35.2]].
> - Used in Quantum Mechanics: the completeness of the infinite-well states, proved from this basis — [[§B1.3 Stationary States and Expansion in Energy Eigenstates#^thm-b1-3-3|QM Theorem §B1.3.3]].
> - The density step it needs (continuous functions vanishing at the endpoints are dense in $L^2[0,2\pi]$) follows from [[§35 Lᵖ as a Banach Space#^thm-35-12|551 Thm. §35.12]](iii) by cutting the approximant off near the endpoints.
> - Computational version, real form on C[0, 2π]: orthogonality of the trigonometric system [[§57 Applications of Inner Product Spaces#^prop-57-2|235 Prop. §57.2]], the coefficient formulas [[§57 Applications of Inner Product Spaces#^thm-57-3|235 Thm. §57.3]], and convergence in the mean [[§57 Applications of Inner Product Spaces#^thm-57-4|235 Thm. §57.4]], with worked Fourier approximations.
> - Computational version: convergence in the mean of the Fourier series of any $f$ with $\int f^2<\infty$, [[§15★ Mean Error and Convergence in Mean#^thm-15-6|341 Thm. §15.6]], and pointwise convergence for sectionally smooth $f$, [[§16★ Proof of Convergence#^thm-16-4|341 Thm. §16.4]], with worked examples.
> - Used in Electromagnetism: the Fourier modes of separation of variables in Cartesian coordinates, their closure as a Dirac comb, and the field of a mesh of charged wires — [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]], [[§C6.2 Separation in Cartesian and Spherical Coordinates#^ex-c6-2-2|EM Example §C6.2.2]].

> [!remark] Remark: Fourier Series
> Read through Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]], this is the theory of Fourier series in $L^2$: every $f \in L^2[0,2\pi]$ is $f = \sum_{n \in \mathbb{Z}} c_n e_n$ with $c_n = (f, e_n) = \frac{1}{\sqrt{2\pi}} \int_0^{2\pi} f(x)\, e^{-inx}\, dx$, the series converging in the $L^2$ norm (not necessarily pointwise), and Parseval's equality reads $\int_0^{2\pi} |f|^2 = \sum_n |c_n|^2$.

^rem-27-9

> [!remark]- Connections
> - Computational version: real Fourier series and their coefficients, [[§9 Periodic Functions and Fourier Series#^def-9-3|341 Def. §9.3]], and the complex coefficients $c_n$, [[§19★ Complex Methods#^def-19-1|341 Def. §19.1]], with worked examples.
