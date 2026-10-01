---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 20
tags: [functional-analysis, math556]
---
← [[§19 Bounded Linear Functionals and the Riesz Representation Theorem]] · ↑ [[· 5 Inner Product Spaces]] · [[§21 Boundedness and Continuity]] →

*Stage: inner products — Threads: dimension, completeness. Countable support, Bessel and Parseval: bases in infinite dimensions.*

## Orthonormal Sets

> [!definition] Definition §20.1: Orthogonal and Orthonormal Sets
> Let $X$ be an inner product space and $\{e_\alpha\}_{\alpha \in \Lambda} \subset X$, indexed by an arbitrary set $\Lambda$. The family is **orthogonal** if $e_\alpha \perp e_\beta$ for all $\alpha, \beta \in \Lambda$ with $\alpha \neq \beta$. It is **orthonormal** if in addition $\|e_\alpha\| = 1$ for every $\alpha \in \Lambda$.
>
> *Lax: §6.4, definition of orthonormal set*

^def-20-1

> [!remark]- Connections
> - The finite-dimensional version (orthonormal lists): [[§20 Orthonormal Bases#^ladr-6-22|LADR 6.22]].

> [!definition] Definition §20.2: Complete Orthogonal Set
> An orthogonal set $\{e_\alpha\}_{\alpha \in \Lambda}$ in $X$ is **complete** if the only vector orthogonal to all of its members is $0$:
>
> $$
> (x, e_\alpha) = 0 \ \text{ for all } \alpha \in \Lambda \quad \Longrightarrow \quad x = 0 .
> $$

^def-20-2

> [!remark] Remark
> Completeness of an orthogonal set is unrelated to completeness of a space. It means the set cannot be enlarged: if some nonzero $x$ were orthogonal to every $e_\alpha$, it could be added to the set, which therefore could not be a basis. In $\mathbb{R}^n$, a complete orthonormal set $\{e_1, \ldots, e_n\}$ is a basis, and every $x$ is $x = \sum_{j=1}^n (x, e_j)\, e_j$. The question is whether the same is true in a Hilbert space.

^rem-20-1

> [!remark] Remark: What Should “Basis” Mean
> The natural definition is that every $x \in H$ satisfies $x = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$. But the right side need not make sense a priori. Adding finitely many vectors is part of the linear structure; adding infinitely many requires a limit (compare [[§1 Linear Spaces#^rem-1-5|the remark on finite sums]] in [[§1 Linear Spaces#Linear Span|§1]]); and $\Lambda$ may be uncountable, in which case it is not even clear in what order to add. The following results make sense of it in three steps: for each $x$ only countably many coefficients $(x, e_\alpha)$ are nonzero ([[§20 Orthonormal Sets and Bases#^prop-20-4|§20.4]]); the sum of their squares is at most $\|x\|^2$ ([[§20 Orthonormal Sets and Bases#^thm-20-5|Bessel]]); and the vector series then converges in $H$ ([[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]]). Only the last step uses completeness of $H$; the first two hold in any inner product space.

^rem-20-2

## Pythagoras and Bessel's Inequality

> [!theorem] Lemma §20.1: Pythagoras
> Let $X$ be an inner product space.
> - (a) If $u \perp v$, then $\|u + v\|^2 = \|u\|^2 + \|v\|^2$.
> - (b) If $e_1, \ldots, e_k$ are orthonormal and $c_1, \ldots, c_k \in \mathbb{F}$, then $\bigl\| \sum_{j=1}^k c_j e_j \bigr\|^2 = \sum_{j=1}^k |c_j|^2$.

^lem-20-1

> [!proof]+ Proof
> (a) By [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|(5.1)]] with $t = 1$, $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}(v, u) + \|v\|^2$, and $(v, u) = 0$.
>
> (b) Induction on $k$; the case $k = 1$ is $\|c_1 e_1\|^2 = |c_1|^2$. For the step, $u = \sum_{j < k} c_j e_j$ and $v = c_k e_k$ are orthogonal, since $(u, v) = \sum_{j<k} c_j \bar{c}_k (e_j, e_k) = 0$; so by (a) and the induction hypothesis, $\|u + v\|^2 = \sum_{j<k} |c_j|^2 + |c_k|^2$.

^pf-20-1

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^pf-17-1|§17.1 (5.1)]], [[§20 Orthonormal Sets and Bases#^def-20-1|Def. §20.1]]

> [!remark]- Connections
> - Finite-dimensional home: (a) is [[§19 Inner Products and Norms#^ladr-6-12|LADR 6.12]], (b) is [[§20 Orthonormal Bases#^ladr-6-24|LADR 6.24]].

> [!theorem] Lemma §20.2: Finite Bessel Inequality
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal in an inner product space $X$, let $e_1, \ldots, e_k$ be finitely many distinct members of it, and $x \in X$. Put $y = x - \sum_{j=1}^k (x, e_j)\, e_j$. Then $y \perp e_i$ for $i = 1, \ldots, k$, and
>
> $$
> \|x\|^2 = \|y\|^2 + \sum_{j=1}^k |(x, e_j)|^2 ; \qquad \text{in particular} \qquad \sum_{j=1}^k |(x, e_j)|^2 \le \|x\|^2 .
> $$

^lem-20-2

> [!proof]+ Proof
> For each $i$, taking the scalars $(x, e_j)$ out of the first slot,
>
> $$
> (y, e_i) = (x, e_i) - \sum_{j=1}^k (x, e_j)\,(e_j, e_i) = (x, e_i) - (x, e_i) = 0,
> $$
>
> since $(e_j, e_i) = 0$ for $j \neq i$ and $(e_i, e_i) = 1$. Hence $y$ is orthogonal to $\sum_j (x, e_j) e_j$ (conjugate-linearity in the second slot), and $x = y + \sum_j (x, e_j) e_j$. By Lemma [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]](a) and then (b), $\|x\|^2 = \|y\|^2 + \bigl\|\sum_j (x, e_j) e_j\bigr\|^2 = \|y\|^2 + \sum_j |(x, e_j)|^2$.

^pf-20-2

*Uses:* [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]], [[§20 Orthonormal Sets and Bases#^def-20-1|Def. §20.1]]

> [!remark]- Connections
> - Finite-dimensional home: [[§20 Orthonormal Bases#^ladr-6-26|LADR 6.26]] (Bessel's inequality for an orthonormal list).

![[m556-20-1.svg]]
*$x$ split into its component $\sum_j (x, e_j) e_j$ (red) in $\operatorname{span}\{e_1, \ldots, e_k\}$ and the remainder $y$ (blue) perpendicular to it. Pythagoras across the right angle is the identity $\|x\|^2 = \|y\|^2 + \sum_j |(x, e_j)|^2$; dropping the blue leg is Bessel.*

The picture Wu described: $\sum_j (x, e_j) e_j$ is the orthogonal projection of $x$ onto $\operatorname{span}\{e_1, \ldots, e_k\}$, and $y$ is the perpendicular remainder. Pythagoras ([[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]]) applied to $k + 1$ orthogonal pieces gives the identity; dropping $\|y\|^2$ gives the inequality.

> [!definition] Definition §20.3: Sums of Non-Negative Families
> Let $(t_\alpha)_{\alpha \in \Lambda}$ be real numbers with $t_\alpha \ge 0$ whose **support** $S = \{ \alpha \in \Lambda : t_\alpha \neq 0 \}$ is countable. Define
>
> $$
> \sum_{\alpha \in \Lambda} t_\alpha := \sum_{n} t_{\alpha_n} \in [0, \infty],
> $$
>
> where $\alpha_1, \alpha_2, \ldots$ is an enumeration of $S$ (a finite sum if $S$ is finite, and $0$ if $S = \varnothing$).

^def-20-3

> [!theorem] Lemma §20.3: The Sum Does Not Depend on the Enumeration
> In Definition [[§20 Orthonormal Sets and Bases#^def-20-3|§20.3]],
>
> $$
> \sum_{\alpha \in \Lambda} t_\alpha = \sup \Bigl\{ \sum_{\alpha \in F} t_\alpha : F \subset \Lambda \text{ finite} \Bigr\} ;
> $$
>
> in particular the sum is independent of the enumeration of $S$.

^lem-20-3

> [!proof]+ Proof
> (Not covered in lecture.) Let $T$ be the supremum. Each partial sum $\sum_{n \le N} t_{\alpha_n}$ is a sum over a finite subset of $\Lambda$, so it is at most $T$, and hence so is the limit of these increasing partial sums. Conversely, for finite $F \subset \Lambda$, the finite set $F \cap S$ is contained in $\{\alpha_1, \ldots, \alpha_N\}$ for some $N$, and terms outside $S$ vanish; so $\sum_{\alpha \in F} t_\alpha \le \sum_{n \le N} t_{\alpha_n} \le \sum_n t_{\alpha_n}$. Taking the supremum over $F$ gives $T \le \sum_n t_{\alpha_n}$.

^pf-20-3

*Uses:* [[§20 Orthonormal Sets and Bases#^def-20-3|Def. §20.3]]

> [!theorem] Proposition §20.4: Only Countably Many Coefficients are Nonzero
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal in an inner product space $X$, and $x \in X$. Then the set
>
> $$
> S_x = \{ \alpha \in \Lambda : (x, e_\alpha) \neq 0 \}
> $$
>
> is countable (finite or countably infinite).

^prop-20-4

> [!proof]+ Proof
> For $k \in \mathbb{N}$ let $\Lambda_k = \{ \alpha \in \Lambda : |(x, e_\alpha)| \ge 1/k \}$.
>
> *Each $\Lambda_k$ is finite, with at most $k^2\|x\|^2$ elements.* Let $e_1, \ldots, e_l$ be any finitely many distinct members with indices in $\Lambda_k$. By Lemma [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]],
>
> $$
> \frac{l}{k^2} \le \sum_{i=1}^l |(x, e_i)|^2 \le \|x\|^2, \qquad \text{so} \qquad l \le k^2\|x\|^2 .
> $$
>
> Thus every finite subset of $\Lambda_k$ has at most $k^2\|x\|^2$ elements, so $\Lambda_k$ itself is finite with at most that many. (Only finite subsets can be fed into Lemma [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]]; the bound on all of them is what shows $\Lambda_k$ is not infinite.)
>
> *Conclusion.* If $(x, e_\alpha) \neq 0$ then $|(x, e_\alpha)| \ge 1/k$ for some $k$, so $S_x = \bigcup_{k=1}^\infty \Lambda_k$, a countable union of finite sets, hence countable.

^pf-20-4

*Uses:* [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]], [[Countable Union of Countable Sets is Countable|551 §3.1]]

![[m556-20-5.svg]]
*The coefficients $|(x, e_\alpha)|$ over an index set $\Lambda$ that may be uncountable. The finite Bessel inequality caps how many can reach any level: at most $k^2\|x\|^2$ of them lie on or above $\tfrac1k$ (red, the set $\Lambda_k$). Every nonzero coefficient clears some level $\tfrac1k$, so the support $S_x = \bigcup_k \Lambda_k$ is a countable union of finite sets, however large $\Lambda$ is.*

> [!remark] Remark
> A student read this as saying that every vector “lives in a countably-infinite-dimensional part” of $H$; Wu separated the two concepts. The proposition is about one fixed $x$: its coefficients vanish outside a countable set $S_x$. Different $x$ can have different, even disjoint, supports, and $\Lambda$ itself can be uncountable. Nothing about bases or dimension is being asserted yet. Another question: the norm $\|x\|$ is a real number, finite by definition, so the bound $k^2\|x\|^2$ is finite.

^rem-20-3

> [!theorem] Theorem §20.5: Bessel's Inequality
> Let $\{e_\alpha\}_{\alpha \in \Lambda}$ be orthonormal in an inner product space $X$. For every $x \in X$,
>
> $$
> \sum_{\alpha \in \Lambda} |(x, e_\alpha)|^2 \le \|x\|^2 .
> $$
>
> The left side is defined by Definition [[§20 Orthonormal Sets and Bases#^def-20-3|§20.3]], whose hypothesis holds by Proposition [[§20 Orthonormal Sets and Bases#^prop-20-4|§20.4]].

^thm-20-5

> [!proof]+ Proof
> Enumerate $S_x$ as $\alpha_1, \alpha_2, \ldots$ and write $e_n = e_{\alpha_n}$. By Lemma [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]], $\sum_{j=1}^n |(x, e_j)|^2 \le \|x\|^2$ for every $n$. If $S_x$ is finite this is the claim. Otherwise the partial sums form an increasing sequence bounded by $\|x\|^2$; letting $n \to \infty$ gives $\sum_{j=1}^\infty |(x, e_j)|^2 \le \|x\|^2$, which is the claim. (Equivalently, by Lemma [[§20 Orthonormal Sets and Bases#^lem-20-3|§20.3]]: the sum is a supremum of finite sums, each at most $\|x\|^2$.)

^pf-20-5

*Uses:* [[§20 Orthonormal Sets and Bases#^prop-20-4|§20.4]], [[§20 Orthonormal Sets and Bases#^def-20-3|Def. §20.3]], [[§20 Orthonormal Sets and Bases#^lem-20-2|§20.2]], [[§20 Orthonormal Sets and Bases#^lem-20-3|§20.3]]

> [!remark]- Connections
> - Finite-dimensional home: [[§20 Orthonormal Bases#^ladr-6-26|LADR 6.26]].
> - Equality holds exactly for complete sets: Parseval, [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]].

## Orthonormal Expansions

> [!theorem] Proposition §20.6: The Orthonormal Expansion Converges
> Let $H$ be a Hilbert space, $\{e_\alpha\}_{\alpha \in \Lambda}$ an orthonormal set, and $x \in H$. Enumerate $S_x = \{\alpha : (x, e_\alpha) \neq 0\}$ as $\alpha_1, \alpha_2, \ldots$ and write $e_n = e_{\alpha_n}$. Then the partial sums
>
> $$
> s_n = \sum_{j=1}^n (x, e_j)\, e_j
> $$
>
> converge in $H$, and the limit does not depend on the enumeration. It is denoted $\sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$. (If $S_x$ is finite this is a finite sum.)

^prop-20-6

> [!proof]+ Proof
> Assume $S_x$ is countably infinite; otherwise there is nothing to prove.
>
> *Convergence.* By completeness of $H$ it suffices to show that $\{s_n\}$ is Cauchy. For $m < n$, Lemma [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]](b) gives
>
> $$
> \|s_n - s_m\|^2 = \Bigl\| \sum_{j=m+1}^n (x, e_j)\, e_j \Bigr\|^2 = \sum_{j=m+1}^n |(x, e_j)|^2 .
> $$
>
> The series $\sum_{j=1}^\infty |(x, e_j)|^2$ converges, by Bessel's inequality (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-5|§20.5]]): it is a series of non-negative terms with partial sums bounded by $\|x\|^2$. So its tails tend to $0$, and $\|s_n - s_m\| \to 0$ as $m, n \to \infty$.
>
> *Independence of the enumeration.* (Not covered in lecture.) Write $c_\alpha = (x, e_\alpha)$. Let $\beta_1, \beta_2, \ldots$ be a second enumeration of $S_x$, with partial sums $t_m$; let $s = \lim s_n$, $t = \lim t_m$. Given $\varepsilon > 0$, choose $N_0$ with $\sum_{j > N_0} |c_{\alpha_j}|^2 < \varepsilon$, and let $F = \{\alpha_1, \ldots, \alpha_{N_0}\}$. For all large $n$ and $m$, both $A = \{\alpha_1, \ldots, \alpha_n\}$ and $B = \{\beta_1, \ldots, \beta_m\}$ contain $F$. Then $s_n - t_m = \sum_{\alpha \in A \setminus B} c_\alpha e_\alpha - \sum_{\alpha \in B \setminus A} c_\alpha e_\alpha$ is a finite combination of distinct $e_\alpha$ with indices in $S_x \setminus F$, so by Lemma [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]](b),
>
> $$
> \|s_n - t_m\|^2 = \sum_{\alpha \in A \triangle B} |c_\alpha|^2 \le \sum_{j > N_0} |c_{\alpha_j}|^2 < \varepsilon .
> $$
>
> Letting $n, m \to \infty$ and using [[§8 Normed Linear Spaces#^prop-8-4|continuity of the norm]], $\|s - t\|^2 \le \varepsilon$. As $\varepsilon$ was arbitrary, $s = t$.

^pf-20-6

*Uses:* [[§17 Cauchy–Schwarz and the Induced Norm#^def-17-1|Def. §17.1]], [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]], [[§20 Orthonormal Sets and Bases#^thm-20-5|§20.5]], [[§8 Normed Linear Spaces#^prop-8-4|§8.4]]

> [!remark] Remark
> Completeness of $H$ is used exactly once, to turn the Cauchy sequence of partial sums into a limit; everything before it (countable support, Bessel) holds in any inner product space. The independence of the enumeration was not addressed in lecture, but it is needed for the notation $\sum_{\alpha \in \Lambda}$ to mean anything: a series of vectors, like a conditionally convergent series of numbers, could in principle depend on the order of summation. Orthogonality prevents this.

^rem-20-4

> [!theorem] Lemma §20.7: Coefficients and Norm of the Expansion
> Let $H$ be a Hilbert space, $\{e_\alpha\}_{\alpha \in \Lambda}$ orthonormal, $x \in H$, and $s = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$. Then
> - (a) $(s, e_\beta) = (x, e_\beta)$ for every $\beta \in \Lambda$;
> - (b) $\|s\|^2 = \sum_{\alpha \in \Lambda} |(x, e_\alpha)|^2$.

^lem-20-7

> [!proof]+ Proof
> With $s_n$ as in Proposition [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]], $s_n \to s$. (If $S_x$ is finite, take $s_n = s$ for all large $n$.)
>
> (a) Fix $\beta \in \Lambda$. By orthonormality, $(s_n, e_\beta) = \sum_{j \le n} (x, e_j)(e_j, e_\beta)$ equals $(x, e_\beta)$ if $\beta \in \{\alpha_1, \ldots, \alpha_n\}$ and $0$ otherwise. If $\beta \in S_x$, then $\beta = \alpha_j$ for some $j$, and $(s_n, e_\beta) = (x, e_\beta)$ for all $n \ge j$. If $\beta \notin S_x$, then $(s_n, e_\beta) = 0 = (x, e_\beta)$ for all $n$. In both cases $(s_n, e_\beta) \to (x, e_\beta)$, while $(s_n, e_\beta) \to (s, e_\beta)$ by continuity of the inner product (Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]). So $(s, e_\beta) = (x, e_\beta)$.
>
> (b) By Lemma [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]](b), $\|s_n\|^2 = \sum_{j \le n} |(x, e_j)|^2$. Let $n \to \infty$: the left side tends to $\|s\|^2$ by [[§8 Normed Linear Spaces#^prop-8-4|continuity of the norm]], and the right side to $\sum_\alpha |(x, e_\alpha)|^2$ by Definition [[§20 Orthonormal Sets and Bases#^def-20-3|§20.3]].

^pf-20-7

*Uses:* [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]], [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]], [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]], [[§8 Normed Linear Spaces#^prop-8-4|§8.4]], [[§20 Orthonormal Sets and Bases#^def-20-3|Def. §20.3]]

> [!remark] Remark
> Part (a) is the step Wu flagged as “the only non-trivial part”: taking the inner product with $e_\beta$ term by term through an infinite sum. It is legitimate because the sum is a limit of finite sums and the inner product is continuous; her advice, “if you are not sure, start with a finite sum and take the limit,” is exactly this proof.

^rem-20-5

## Orthonormal Bases

> [!definition] Definition §20.4: Orthonormal Basis
> An orthonormal set $\{e_\alpha\}_{\alpha \in \Lambda}$ in a Hilbert space $H$ is an **orthonormal basis** of $H$ if
>
> $$
> x = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha \qquad \text{for every } x \in H,
> $$
>
> the sum being understood as in Proposition [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]].
>
> *Lax: §6.4, definition of orthonormal base (via closed linear span; see Proposition [[§20 Orthonormal Sets and Bases#^prop-20-9|§20.9]])*

^def-20-4

> [!theorem] Theorem §20.8: Characterizations of an Orthonormal Basis
> Let $H$ be a Hilbert space and $\{e_\alpha\}_{\alpha \in \Lambda}$ an orthonormal set. The following are equivalent:
> - (1) $\{e_\alpha\}_{\alpha \in \Lambda}$ is complete;
> - (2) $\{e_\alpha\}_{\alpha \in \Lambda}$ is an orthonormal basis of $H$;
> - (3) (**Parseval's equality**) $\|x\|^2 = \sum_{\alpha \in \Lambda} |(x, e_\alpha)|^2$ for every $x \in H$.
>
> *Lax: §6.4, Lemma 8*

^thm-20-8

> [!proof]+ Proof
> Write $s(x) = \sum_{\alpha \in \Lambda} (x, e_\alpha)\, e_\alpha$ (Proposition [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]]).
>
> (1)$\Rightarrow$(2). Let $x \in H$ and $y = x - s(x)$. For every $\beta \in \Lambda$, Lemma [[§20 Orthonormal Sets and Bases#^lem-20-7|§20.7]](a) gives $(y, e_\beta) = (x, e_\beta) - (s(x), e_\beta) = 0$. So $y$ is orthogonal to every $e_\beta$, and completeness gives $y = 0$, i.e. $x = s(x)$.
>
> (2)$\Rightarrow$(3). $x = s(x)$, so by Lemma [[§20 Orthonormal Sets and Bases#^lem-20-7|§20.7]](b), $\|x\|^2 = \|s(x)\|^2 = \sum_\alpha |(x, e_\alpha)|^2$.
>
> (3)$\Rightarrow$(1). If $(x, e_\alpha) = 0$ for all $\alpha$, then Parseval's equality gives $\|x\|^2 = 0$, so $x = 0$.

^pf-20-8

*Uses:* [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]], [[§20 Orthonormal Sets and Bases#^lem-20-7|§20.7]], [[§20 Orthonormal Sets and Bases#^def-20-2|Def. §20.2]], [[§20 Orthonormal Sets and Bases#^def-20-4|Def. §20.4]]

> [!remark]- Connections
> - Finite-dimensional home (expansion and Parseval in an orthonormal basis): [[§20 Orthonormal Bases#^ladr-6-30|LADR 6.30]].
> - Restated in Dirac notation as the completeness relation: [[§23 The Completeness Relation#^thm-23-2|§23.2]], [[§23 The Completeness Relation#^cor-23-4|§23.4]].

> [!remark] Remark
> In finite dimensions these are the familiar facts: a complete orthonormal set is a basis, every vector is the sum of its components, and its squared length is the sum of the squared components. The theorem says that all three survive in any Hilbert space once the sums are interpreted correctly — countable support, then convergence — and that [[§20 Orthonormal Sets and Bases#^thm-20-5|Bessel's inequality]] becomes an equality exactly for complete sets.

^rem-20-6

> [!theorem] Proposition §20.9: Lax's Definition of Orthonormal Base Agrees
> An orthonormal set $E = \{e_\alpha\}_{\alpha \in \Lambda}$ in a Hilbert space $H$ is complete if and only if its closed linear span is $H$. Consequently the following are equivalent: $E$ is an orthonormal basis in the sense of Definition [[§20 Orthonormal Sets and Bases#^def-20-4|§20.4]]; $\overline{\operatorname{span}}\, E = H$ (Lax's definition).
>
> *Lax: §6.4, definition of orthonormal base and Thm 7*

^prop-20-9

> [!proof]+ Proof
> (Not covered in lecture.) Let $Y = \overline{\operatorname{span}}\, E$, a closed linear subspace (Definition [[§8 Normed Linear Spaces#^def-8-8|§8.8]]). We claim $E^\perp = Y^\perp$. Since $E \subset Y$, every vector orthogonal to $Y$ is orthogonal to $E$. Conversely, if $v \perp e_\alpha$ for all $\alpha$, then $v$ is orthogonal to every finite linear combination of the $e_\alpha$ (conjugate-linearity in the second slot), and to every limit $y$ of such combinations $y_n$, since $(v, y) = \lim (v, y_n) = 0$ by Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]; so $v \in Y^\perp$.
>
> By Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], $H = Y \oplus Y^\perp$. If $Y^\perp = \{0\}$, then every $x \in H$ lies in $Y$, so $Y = H$. If $Y = H$, then $Y^\perp = \{0\}$, since $v \perp v$ forces $v = 0$. Hence $E$ is complete ($E^\perp = \{0\}$) iff $Y^\perp = \{0\}$ iff $Y = H$. The last sentence follows by Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]].

^pf-20-9

*Uses:* [[§8 Normed Linear Spaces#^def-8-8|Def. §8.8]], [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], [[§20 Orthonormal Sets and Bases#^def-20-2|Def. §20.2]], [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]

> [!remark]- Connections
> - The same two steps proved earlier for arbitrary sets: $E^\perp = Y^\perp$ is [[§18 Projection and Orthogonal Decomposition#^lem-18-5|§18.5]], and $\overline{\operatorname{span}}\,E = (E^\perp)^\perp$ is [[§18 Projection and Orthogonal Decomposition#^thm-18-6|§18.6]].

> [!remark] Remark: Comparison with Lax
> Lax defines an orthonormal base by the condition $\overline{\operatorname{span}}\, E = H$, and his Lemma 8 then describes the closed linear span as the set of sums $\sum_j a_j e_j$ with $\sum_j |a_j|^2 < \infty$, for a countable orthonormal set. Wu defines a basis by the expansion $x = \sum_\alpha (x, e_\alpha) e_\alpha$ and proves the equivalence with completeness (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]); the proposition above connects the two. Lax also constructs orthonormal bases by [[§20 Orthonormal Sets and Bases#^lem-20-18|Gram–Schmidt]] (Theorem $9'$) and identifies the isometries of $H$ (Theorem 10); neither was covered in lecture.

^rem-20-7

> [!theorem] Proposition §20.10: Small Perturbations of a Complete Orthonormal Set
> Let $\{e_n\}_{n \ge 1}$ and $\{f_n\}_{n \ge 1}$ be orthonormal sets in a Hilbert space $H$ with $\sum_{n=1}^\infty \|e_n - f_n\|^2 < 1$. If $\{e_n\}$ is complete, so is $\{f_n\}$.
>
> *Source: HW4, Problem 3*

^prop-20-10

> [!proof]+ Proof
> (HW4, Problem 3.) Let $c = \sum_n \|e_n - f_n\|^2 < 1$ and suppose $(x, f_n) = 0$ for all $n$. Then $(x, e_n) = (x, e_n - f_n)$, so $|(x, e_n)| \le \|x\|\,\|e_n - f_n\|$ by [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Cauchy–Schwarz]]. By Parseval's equality for the complete set $\{e_n\}$ (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]),
>
> $$
> \|x\|^2 = \sum_n |(x, e_n)|^2 \le \|x\|^2 \sum_n \|e_n - f_n\|^2 = c\,\|x\|^2,
> $$
>
> so $(1 - c)\|x\|^2 \le 0$ and $x = 0$.

^pf-20-10

*Uses:* [[§20 Orthonormal Sets and Bases#^def-20-2|Def. §20.2]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]

> [!remark] Remark
> The proof never uses that the $f_n$ are orthonormal beyond making completeness of $\{f_n\}$ a meaningful notion; the mechanism is that $x \perp f_n$ makes each coefficient $(x, e_n)$ small, and Parseval turns “all coefficients small in $\ell^2$” into “$\|x\|$ smaller than itself”. Some hypothesis of this kind is needed: in $\ell^2$ the shifted sequence $f_n = e_{n+1}$ is orthonormal but not complete ($e_1 \perp f_n$ for all $n$), and there $\sum_n \|e_n - f_n\|^2 = \infty$.

^rem-20-8

## Examples

> [!example] Example §20.1: The Standard Basis of $\ell^2$
> In $\ell^2$ with $(a, b) = \sum_j a_j \overline{b_j}$, let $e_j = (0, \ldots, 0, 1, 0, \ldots)$ with the $1$ in the $j$-th place. Then $(e_i, e_j) = \delta_{ij}$, so $\{e_j\}_{j \ge 1}$ is orthonormal, and $(a, e_j) = a_j$. It is complete: if $(a, e_j) = a_j = 0$ for all $j$ then $a = 0$. By Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]] it is an orthonormal basis: $a = \sum_j a_j e_j$ in $\ell^2$, and Parseval's equality is $\|a\|_2^2 = \sum_j |a_j|^2$, the definition of the norm.

^ex-20-1

> [!theorem] Theorem §20.11: The Fourier Basis of $L^2[0,2\pi]$
> In the complex space $L^2[0,2\pi]$, the functions
>
> $$
> e_n(x) = \frac{1}{\sqrt{2\pi}}\, e^{inx}, \qquad n \in \mathbb{Z},
> $$
>
> form an orthonormal basis.

^thm-20-11

> [!proof]+ Proof
> *Orthonormality.* $\|e_n\|^2 = \frac{1}{2\pi}\int_0^{2\pi} e^{inx}\, \overline{e^{inx}}\, dx = \frac{1}{2\pi}\int_0^{2\pi} 1\, dx = 1$. For $k \neq j$,
>
> $$
> (e_k, e_j) = \frac{1}{2\pi}\int_0^{2\pi} e^{i(k-j)x}\, dx = \frac{1}{2\pi}\Bigl[ \frac{e^{i(k-j)x}}{i(k-j)} \Bigr]_0^{2\pi} = 0,
> $$
>
> since $e^{i(k-j)2\pi} = 1$.
>
> *Completeness.* Deferred: not proved in lecture (“I don't think I want to prove this”). It is the completeness of Fourier series, proved for instance by showing that trigonometric polynomials are dense in $L^2[0,2\pi]$ (Fejér's theorem gives uniform approximation of continuous periodic functions, and continuous periodic functions are dense in $L^2$). Given completeness, Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]] makes it a basis.

^pf-20-11

*Uses:* [[§20 Orthonormal Sets and Bases#^def-20-1|Def. §20.1]], [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]

> [!remark]- Connections
> - The real trigonometric orthonormal list on $[-\pi, \pi]$ in finite dimensions: [[§20 Orthonormal Bases#^ladr-6-23|LADR 6.23]](d).
> - Used for the particle on a ring: [[§23 The Completeness Relation#^ex-23-2|Ex. §23.2]].
> - Used in Quantum Mechanics: the completeness of the infinite-well states, proved from this basis — [[§B1.3 Stationary States and Expansion in Energy Eigenstates#^thm-b1-3-3|QM Theorem §B1.3.3]].

> [!remark] Remark: Fourier Series
> Read through Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]], this is the theory of Fourier series in $L^2$: every $f \in L^2[0,2\pi]$ is $f = \sum_{n \in \mathbb{Z}} c_n e_n$ with $c_n = (f, e_n) = \frac{1}{\sqrt{2\pi}} \int_0^{2\pi} f(x)\, e^{-inx}\, dx$, the series converging in the $L^2$ norm (not necessarily pointwise), and Parseval's equality reads $\int_0^{2\pi} |f|^2 = \sum_n |c_n|^2$.

^rem-20-9

## Existence of Orthonormal Bases and Separability

Both examples have *countable* orthonormal bases. Wu announced for next lecture that every Hilbert space has an orthonormal basis — which by itself is “almost useless, because there are too many” — and, more usefully, that the countable ones are exactly the bases of separable spaces.

> [!remark] Remark: The Idea: Keep Adding Orthogonal Directions
> Wu first described the construction informally. Assume $H \neq \{0\}$ and take $e_1 \in H$ with $\|e_1\| = 1$. If $H = \operatorname{span}\{e_1\}$, then $\{e_1\}$ is an orthonormal basis. If not, take $y_2 \in H$ with $y_2 \notin \operatorname{span}\{e_1\}$ and remove its component along $e_1$:
>
> $$
> x_2 = y_2 - (y_2, e_1)\, e_1, \qquad (x_2, e_1) = (y_2, e_1) - (y_2, e_1)(e_1, e_1) = 0,
> $$
>
> so $x_2 \perp e_1$; put $e_2 = x_2 / \|x_2\|$. If $H = \operatorname{span}\{e_1, e_2\}$ we are done; if not, take $y_3 \notin \operatorname{span}\{e_1, e_2\}$ and continue.
>
> ![[m556-20-2.svg]]
> *The first step: $y_2$ minus its component $(y_2, e_1)\,e_1$ along $e_1$ leaves $x_2 \perp e_1$, and normalizing gives $e_2$.*
>
> The step-by-step description looks countable, but it need not be: an orthonormal basis $\{e_\alpha\}_{\alpha \in \Lambda}$ need not be countable. The precise argument is [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|Zorn's lemma]], which says “keep adding until nothing more can be added” without any enumeration.

^rem-20-10

> [!theorem] Theorem §20.12: Existence of Orthonormal Bases
> Every Hilbert space $H$ has an orthonormal basis.
>
> *Lax: §6.4, Thm 9*

^thm-20-12

> [!proof]+ Proof
> If $H = \{0\}$, the empty set is an orthonormal basis: it is complete, since every $x \in H$ is $0$. Assume $H \neq \{0\}$.
>
> **Step 1: the partially ordered set.** Let $S$ be the set of all orthonormal sets in $H$, partially ordered by inclusion: for $O_1, O_2 \in S$, $O_1 \prec O_2$ if $O_1 \subset O_2$. Two orthonormal sets need not be comparable. $S \neq \varnothing$: for any $x \neq 0$, $\{x/\|x\|\} \in S$.
>
> **Step 2: every chain has an upper bound.** Let $C = \{O_\beta\}_{\beta \in I}$ be a chain in $S$ (if $C$ is empty, any element of $S$ is an upper bound), and let $U = \bigcup_{\beta \in I} O_\beta$. Then $U \in S$: each $u \in U$ lies in some $O_\beta$, so $\|u\| = 1$; and if $u \neq v$ in $U$, say $u \in O_{\beta_1}$ and $v \in O_{\beta_2}$, then since $C$ is a chain one of $O_{\beta_1}, O_{\beta_2}$ contains the other, so $u$ and $v$ lie in a single orthonormal set and $(u, v) = 0$. Since $O_\beta \subset U$ for every $\beta$, $U$ is an upper bound of $C$.
>
> **Step 3: a maximal orthonormal set.** By Zorn's lemma (Theorem [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|§4.2]]), $S$ has a maximal element $O = \{e_\alpha\}_{\alpha \in \Lambda}$.
>
> **Step 4: $O$ is complete.** Suppose not. Then there is $x \in H$, $x \neq 0$, with $(x, e_\alpha) = 0$ for all $\alpha \in \Lambda$. Put $e = x/\|x\|$. Then $\|e\| = 1$ and $(e, e_\alpha) = 0$ for every $\alpha$; in particular $e \notin O$, since $(e, e) = 1 \neq 0$. So $O \cup \{e\}$ is an orthonormal set strictly containing $O$, contradicting the maximality of $O$. Hence $O$ is complete, and by Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]] it is an orthonormal basis.

^pf-20-12

*Uses:* [[§20 Orthonormal Sets and Bases#^def-20-1|Def. §20.1]], [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|§4.2]], [[§20 Orthonormal Sets and Bases#^def-20-2|Def. §20.2]], [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]

> [!remark]- Connections
> - Finite-dimensional home, where Gram–Schmidt suffices: [[§20 Orthonormal Bases#^ladr-6-35|LADR 6.35]].

> [!definition] Definition §20.5: Separable Space
> A normed linear space $X$ is **separable** if it has a countable dense subset: a countable $D \subset X$ such that every $x \in X$ is a limit of a sequence in $D$. Completeness is not required.
>
> *Lax: §5.1, definition of separable space*

^def-20-5

> [!remark]- Connections
> - Same definition for metric spaces: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-9|551 Def. §19.9]]; for topological spaces: [[§18 Countability Axioms#^def-18-5|590 Def. §18.5]].

### Examples of Separable and Non-Separable Spaces

> [!theorem] Proposition §20.13: $\ell^p$ is Separable for $1 \le p < \infty$
> Let $1 \le p < \infty$, and let $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q}$ if $\mathbb{F} = \mathbb{R}$ and $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q} + i\mathbb{Q}$ if $\mathbb{F} = \mathbb{C}$. The set
>
> $$
> D = \bigcup_{J = 1}^\infty \bigl\{ (p_1, \ldots, p_J, 0, 0, \ldots) : p_j \in \mathbb{Q}_{\mathbb{F}} \bigr\}
> $$
>
> is countable and dense in $\ell^p$. Hence $\ell^p$ is separable.

^prop-20-13

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

^pf-20-13

*Uses:* [[§13 Minkowski's Inequality and the Spaces ℓᵖ#^def-13-1|Def. §13.1]], [[§20 Orthonormal Sets and Bases#^def-20-5|Def. §20.5]], [[Countable Union of Countable Sets is Countable|551 §3.1]], [[§3 Countability of Rationals and Unions#^cor-3-2|551 §3.2]]

![[m556-20-3.svg]]
*Approximating $a \in \ell^p$ by an element of $D$: the coordinates beyond $J$ (blue) are set to $0$, and the first $J$ (gray) are replaced by nearby rationals (red dots).*

The two moves of the proof: cut off the tail, which is small because the series converges, and replace the finitely many remaining coordinates by nearby rationals. Both need $p < \infty$: the tail of a convergent series is small, but a bounded sequence need not have a small tail in the supremum norm.

> [!theorem] Proposition §20.14: $\ell^\infty$ is Not Separable
> $\ell^\infty$ is not separable.
>
> *Source: HW5*

^prop-20-14

> [!proof]+ Proof
> Homework (HW5); to be added after submission.

^pf-20-14

> [!theorem] Proposition §20.15: $L^p(E)$ is Separable for $1 \le p < \infty$
> Let $E \subset \mathbb{R}^n$ be measurable and $1 \le p < \infty$. Let $D$ be the set of functions on $E$ of the form
>
> $$
> \varphi = \sum_{j=1}^N a_j\, \chi_{R_j \cap E}, \qquad N \in \mathbb{N},\ a_j \in \mathbb{Q}_{\mathbb{F}},\ R_j \text{ a rectangle with rational endpoints},
> $$
>
> where a rectangle is a product $\prod_{i=1}^n [\alpha_i, \beta_i)$. Then $D$ is countable and dense in $L^p(E)$. Hence $L^p(E)$ is separable.

^prop-20-15

> [!proof]+ Proof
> Wu's route: continuous functions are dense in $L^p$ (taken for granted), a continuous function is approximated by step functions, and the step functions can be taken with rational heights and rational rectangles. The details:
>
> *Countable.* A rectangle with rational endpoints is determined by $2n$ rationals, so there are countably many; for fixed $N$ the choices of $(a_1, \ldots, a_N, R_1, \ldots, R_N)$ form a finite product of countable sets; take the union over $N$.
>
> *Dense.* Let $f \in L^p(E)$ and $\varepsilon > 0$. Extend $f$ by $0$ to $\tilde{f}$ on $\mathbb{R}^n$; then $\tilde{f} \in L^p(\mathbb{R}^n)$ with the same norm.
>
> *Step 1: a continuous function.* By Theorem [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-4|§14.4]] (with $\Omega = \mathbb{R}^n$) there is a continuous $g$ with compact support and $\|\tilde{f} - g\|_{L^p(\mathbb{R}^n)} < \varepsilon/3$. Choose $K \in \mathbb{N}$ with the support of $g$ inside $Q = [-K, K)^n$.
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

^pf-20-15

*Uses:* [[§14 The Function Spaces Lᵖ(Ω)#^def-14-1|Def. §14.1]], [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-4|§14.4]], [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]], [[Minkowski's Inequality|551 §19.9]], [[Countable Union of Countable Sets is Countable|551 §3.1]], [[§20 Orthonormal Sets and Bases#^def-20-5|Def. §20.5]]

> [!remark]- Connections
> - Vault home: [[§19 Normed Linear Spaces and Lᵖ Spaces#^cor-19-20|551 §19.20]], via density of step functions and of $C_c$ in $L^p$, [[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 §19.19]] (its (iii) is the compactly supported density used in Step 1).
> - The companion chapter's case $L^2(\mathbb{R}^n)$: [[§24 Position Eigenstates and Continuous Resolutions#^thm-24-2|§24.2]].

![[m556-20-4.svg]]
*Step 2 and Step 3 for $n = 1$: a continuous $g$ and the step function $\varphi$ on dyadic intervals with rational heights.*

A continuous $g$ and a step function on cubes with rational endpoints and rational heights (here $n = 1$, heights rounded to quarters). The $L^p$ distance is small because it is an *integral* of a small difference over a bounded set. In $L^\infty$ the distance is a supremum, and this argument breaks down.

> [!theorem] Proposition §20.16: $L^\infty(E)$ is Not Separable
> If $E \subset \mathbb{R}^n$ is measurable with $m(E) > 0$, then $L^\infty(E)$ is not separable.

^prop-20-16

> [!proof]+ Proof
> Stated in lecture without proof; the argument is close to the homework on $\ell^\infty$ (Proposition [[§20 Orthonormal Sets and Bases#^prop-20-14|§20.14]]) and will be added after that is submitted.

^pf-20-16

> [!remark] Remark
> The hypothesis $m(E) > 0$ is added here: if $m(E) = 0$, then $L^\infty(E) = \{0\}$, which is separable. Wu stressed that measure theory supplies the examples of functional analysis (“I would suggest you really study real methods … measure theory is becoming very useful now”): without $L^p$ the course has few examples beyond sequence spaces.

^rem-20-11

### Countable Orthonormal Bases

> [!theorem] Theorem §20.17: Separable Hilbert Spaces and Countable Bases
> A Hilbert space $H$ has a countable orthonormal basis if and only if it is separable.
>
> *Lax: §6.4, Thm $9'$*

^thm-20-17

> [!proof]+ Proof of (⇒)
> Assume $H$ has a countable orthonormal basis $\{e_1, e_2, \ldots\}$ (finite or infinite). Then $H = \overline{\operatorname{span}}\{e_1, e_2, \ldots\}$: every $x \in H$ is $x = \sum_j (x, e_j)\, e_j$ (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]), a finite sum if the basis is finite and a limit of partial sums otherwise. Let
>
> $$
> D = \bigcup_{n} \Bigl\{ \sum_{j=1}^n a_j e_j : a_j \in \mathbb{Q}_{\mathbb{F}} \Bigr\},
> $$
>
> the union over $n = 1, 2, \ldots$ (only up to the number of basis vectors if the basis is finite). Each set in the union is in bijection with $\mathbb{Q}_{\mathbb{F}}^n$, so $D$ is countable.
>
> *$D$ is dense.* Let $x \in H$ and $\varepsilon > 0$. The partial sums of the expansion converge to $x$, so there is $n$ with $\bigl\| x - \sum_{j=1}^n (x, e_j) e_j \bigr\| < \varepsilon/2$ (if the basis is finite, take $n$ its size, and this term is $0$). Choose $a_j \in \mathbb{Q}_{\mathbb{F}}$ with $|(x, e_j) - a_j| < \frac{\varepsilon}{2\sqrt{n}}$. By Pythagoras (Lemma [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]]),
>
> $$
> \Bigl\| \sum_{j=1}^n \bigl( (x, e_j) - a_j \bigr) e_j \Bigr\|^2 = \sum_{j=1}^n |(x, e_j) - a_j|^2 < n \cdot \frac{\varepsilon^2}{4n} = \frac{\varepsilon^2}{4},
> $$
>
> so $\bigl\| x - \sum_{j=1}^n a_j e_j \bigr\| < \varepsilon/2 + \varepsilon/2 = \varepsilon$. The tail of the expansion is small, as for $\ell^p$ ([[§20 Orthonormal Sets and Bases#^prop-20-13|§20.13]]).

^pf-20-17

*Uses:* [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]], [[§20 Orthonormal Sets and Bases#^prop-20-6|§20.6]], [[§20 Orthonormal Sets and Bases#^lem-20-1|§20.1]], [[§20 Orthonormal Sets and Bases#^def-20-5|Def. §20.5]], [[Countable Union of Countable Sets is Countable|551 §3.1]]

For the converse, the countable dense set has to be turned into an orthonormal set, which is the Gram–Schmidt process.

> [!theorem] Lemma §20.18: Gram–Schmidt
> Let $y_1, y_2, \ldots$ be a finite or infinite sequence of linearly independent vectors in an inner product space $X$. Then there is an orthonormal sequence $e_1, e_2, \ldots$ (of the same length) with
>
> $$
> \operatorname{span}\{y_1, \ldots, y_j\} = \operatorname{span}\{e_1, \ldots, e_j\} \qquad \text{for every } j.
> $$
>
> *Lax: §6.4, Thm $9'$*

^lem-20-18

> [!proof]+ Proof
> Define recursively
>
> $$
> e_1 = \frac{y_1}{\|y_1\|}, \qquad x_j = y_j - \sum_{i=1}^{j-1} (y_j, e_i)\, e_i, \qquad e_j = \frac{x_j}{\|x_j\|} \quad (j \ge 2),
> $$
>
> exactly as in the informal construction in [[§20 Orthonormal Sets and Bases#^rem-20-10|the remark before Theorem §20.12]]: subtract from $y_j$ its components along the directions already built, and normalize. We check by induction on $j$ that the recursion is well defined and that $\{e_1, \ldots, e_j\}$ is orthonormal with $\operatorname{span}\{e_1, \ldots, e_j\} = \operatorname{span}\{y_1, \ldots, y_j\}$.
>
> *$j = 1$.* $y_1 \neq 0$ by linear independence, so $e_1$ is defined, $\|e_1\| = 1$, and $\operatorname{span}\{e_1\} = \operatorname{span}\{y_1\}$.
>
> *From $j - 1$ to $j$.* *$x_j \neq 0$:* otherwise $y_j = \sum_{i<j} (y_j, e_i) e_i \in \operatorname{span}\{e_1, \ldots, e_{j-1}\} = \operatorname{span}\{y_1, \ldots, y_{j-1}\}$, contradicting linear independence. So $e_j$ is defined and $\|e_j\| = 1$. *Orthogonality:* for $k < j$, using $(e_i, e_k) = \delta_{ik}$ for $i, k < j$,
>
> $$
> (x_j, e_k) = (y_j, e_k) - \sum_{i=1}^{j-1} (y_j, e_i)(e_i, e_k) = (y_j, e_k) - (y_j, e_k) = 0,
> $$
>
> so $(e_j, e_k) = 0$. *Spans:* $e_j$ is a combination of $y_j$ and $e_1, \ldots, e_{j-1} \in \operatorname{span}\{y_1, \ldots, y_{j-1}\}$, so $e_j \in \operatorname{span}\{y_1, \ldots, y_j\}$; conversely $y_j = \|x_j\|\, e_j + \sum_{i<j} (y_j, e_i) e_i \in \operatorname{span}\{e_1, \ldots, e_j\}$. With the induction hypothesis, the two spans are equal.
>
> Since $e_j$ depends only on $y_1, \ldots, y_j$, the recursion runs through an infinite sequence as well.

^pf-20-18

*Uses:* [[§20 Orthonormal Sets and Bases#^def-20-1|Def. §20.1]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]]

> [!remark]- Connections
> - Finite-dimensional home: [[Gram–Schmidt procedure|LADR 6.32]].

> [!proof]+ Proof of (⇐) in Theorem §20.17
> Assume $D = \{y_1, y_2, \ldots\}$ is a countable dense subset of $H$. If $H = \{0\}$, the empty set is a countable orthonormal basis; assume $H \neq \{0\}$, so $D$ contains a nonzero element.
>
> **Step 1: a linearly independent subsequence.** Discard elements that depend linearly on earlier ones. Precisely: let $n_1$ be the first index with $y_{n_1} \neq 0$, and put $y_1' = y_{n_1}$. Having chosen $n_1 < \cdots < n_k$, let $n_{k+1}$ be the first index $n > n_k$ with $y_n \notin \operatorname{span}\{y_1', \ldots, y_k'\}$, and put $y_{k+1}' = y_{n_{k+1}}$; if there is no such index, stop. Wu: “we just take the first linearly independent one, name it $y_2'$, then continue.” The result $D' = \{y_1', y_2', \ldots\}$ (finite or infinite) is linearly independent by construction, and every element of $D$ is a linear combination of elements of $D'$: an element $y_j$ that was discarded, with $n_k < j < n_{k+1}$ (or $j > n_k$ if the process stopped at $k$), lies in $\operatorname{span}\{y_1', \ldots, y_k'\}$, and $y_j = 0$ if $j < n_1$. So
>
> $$
> \text{for every } y_j \in D \text{ there is } k \text{ with } y_j \in \operatorname{span}\{y_1', \ldots, y_k'\}. \tag{5.4}
> $$
>
> **Step 2: Gram–Schmidt.** Lemma [[§20 Orthonormal Sets and Bases#^lem-20-18|§20.18]] gives an orthonormal sequence $\{e_1, e_2, \ldots\}$ with
>
> $$
> \operatorname{span}\{e_1, \ldots, e_j\} = \operatorname{span}\{y_1', \ldots, y_j'\} \qquad \text{for every } j.
> $$
>
> It is countable; it remains to show it is complete, hence (Theorem [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]]) an orthonormal basis.
>
> **Step 3: completeness.** Let $x \in H$ with $(x, e_j) = 0$ for all $j$; we show $x = 0$. Since $D$ is dense in $H$, there is a sequence $y_{n_k} \in D$ with $\lim_{k \to \infty} y_{n_k} = x$. By (5.4) and Step 2, each $y_{n_k}$ lies in $\operatorname{span}\{e_1, \ldots, e_{j_k}\}$ for some $j_k$, say $y_{n_k} = \sum_{j=1}^{j_k} a_j^{(k)} e_j$. Then
>
> $$
> (x, y_{n_k}) = \sum_{j=1}^{j_k} \overline{a_j^{(k)}}\, (x, e_j) = 0 \qquad \text{for all } k,
> $$
>
> and by continuity of the inner product (Lemma [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]),
>
> $$
> (x, x) = \lim_{k \to \infty} (x, y_{n_k}) = 0 .
> $$
>
> Hence $x = 0$, and $\{e_j\}$ is complete.

^pf-20-17-2

*Uses:* [[§20 Orthonormal Sets and Bases#^def-20-5|Def. §20.5]], [[§20 Orthonormal Sets and Bases#^lem-20-18|§20.18]], [[§20 Orthonormal Sets and Bases#^def-20-2|Def. §20.2]], [[§20 Orthonormal Sets and Bases#^thm-20-8|§20.8]], [[§18 Projection and Orthogonal Decomposition#^lem-18-1|§18.1]]

> [!remark]- Connections
> - Every orthonormal set in a separable Hilbert space is countable, not just this one: [[§24 Position Eigenstates and Continuous Resolutions#^prop-24-1|§24.1]].

> [!remark] Remark
> The dense set $D$ is used twice, for different purposes: its span supplies the orthonormal vectors, and its density supplies the approximating sequence in Step 3. Only finite linear combinations appear anywhere — the limit is taken in the inner product, not in the expansion. Compare Proposition [[§24 Position Eigenstates and Continuous Resolutions#^prop-24-1|§24.1]]: in a separable Hilbert space *every* orthonormal set is countable, not just the one constructed here.

^rem-20-12

### Classification of Separable Hilbert Spaces

> [!definition] Definition §20.6: Isomorphic Hilbert Spaces
> Let $H_1$ and $H_2$ be Hilbert spaces over the same field, with inner products $(\cdot, \cdot)_1$ and $(\cdot, \cdot)_2$. $H_1$ is **isomorphic** to $H_2$ if there is a map $T : H_1 \to H_2$ that is linear, one-to-one and onto, and preserves the inner product:
>
> $$
> (Tx, Ty)_2 = (x, y)_1 \qquad \text{for all } x, y \in H_1 .
> $$

^def-20-6

> [!remark] Remark: Isomorphic or Isometric?
> A student asked whether “isomorphic” here means the map preserves distance. It does: $\|Tx - Ty\|_2^2 = (T(x-y), T(x-y))_2 = \|x - y\|_1^2$, so $T$ is an *isometry*. Preserving the inner product already forces one-to-one ($Tx = 0$ gives $\|x\|_1 = \|Tx\|_2 = 0$). What it does not force is *onto*, which is why the definition requires a bijection; the next example shows the difference. (The example is not from lecture.)

^rem-20-13

> [!remark]- Connections
> - Isometries between finite-dimensional inner product spaces, and why they are injective: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]].

> [!example] Example §20.2: An Isometry That is Not an Isomorphism
> On $\ell^2$ let $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$. $S$ is linear and $(Sa, Sb) = \sum_{j \ge 1} a_j \overline{b_j} = (a, b)$, so $S$ preserves the inner product. It is not onto: every $Sa$ has first coordinate $0$, so $e_1 = (1, 0, 0, \ldots)$ is not in the range.

^ex-20-2

> [!theorem] Theorem §20.19: Classification of Separable Hilbert Spaces
> Every separable Hilbert space $H$ over $\mathbb{F}$ is isomorphic either to $\mathbb{F}^n$ for some $n \in \{0, 1, 2, \ldots\}$, or to $\ell^2$.
>
> *Source: HW5*
>
> *Lax: §6.4, Exercise 10*

^thm-20-19

> [!proof]+ Proof
> Homework (HW5); to be added after submission.

^pf-20-19

> [!remark] Remark
> On the board: “isomorphic either to $\mathbb{R}^n$, $n \in \mathbb{N}$, or $\ell^2$” — the real case. Over $\mathbb{C}$ the finite-dimensional models are $\mathbb{C}^n$, and $n = 0$ covers $H = \{0\}$. By Theorem [[§20 Orthonormal Sets and Bases#^thm-20-17|§20.17]] a separable $H$ has a countable orthonormal basis; the finite case gives $\mathbb{F}^n$ and the infinite case $\ell^2$.

^rem-20-14
