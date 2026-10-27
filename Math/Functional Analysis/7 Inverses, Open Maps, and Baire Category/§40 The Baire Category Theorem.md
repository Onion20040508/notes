---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 40
tags: [functional-analysis, math556]
---
← [[§39 Solving Mx = y]] · ↑ [[· 7 Inverses, Open Maps, and Baire Category]] · [[§41 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Thread: completeness. A complete metric space is too large to be a countable union of nowhere dense sets.*

In this section $(X, d)$ is a metric space, $B(x_0, r) = \{ x \in X : d(x, x_0) < r \}$ is the open ball (written $B_r(x_0)$ in Definition [[§11 Normed Linear Spaces#^def-11-10|§11.10]]), and $\overline{B(x_0, r)}$ is its closure. A point $x_0$ is an **interior point** of a set $S$ if $B(x_0, r) \subset S$ for some $r > 0$ (Definition [[§11 Normed Linear Spaces#^def-11-11|§11.11]]).

> [!definition] Definition §40.1: Nowhere Dense; First and Second Category
> Let $(X, d)$ be a metric space.
>
> 1. $E \subset X$ is **nowhere dense** if $\overline{E}$, the closure of $E$, has no interior points.
> 2. $S \subset X$ is **of the first category** if $S$ is a countable union of nowhere dense subsets of $X$: $S = \bigcup_{n=1}^\infty E_n$ with each $E_n$ nowhere dense.
> 3. A set $S$ that is not of the first category is **of the second category**.
>
> *Lax: §15.5, end (sets of second category, Thm 16)*

^def-40-1

> [!example] Example §40.1: Nowhere Dense Sets; Sets of the First Category
> In $X = \mathbb{R}^n$: a finite set $E$ is nowhere dense; so is the set of integer points $\mathbb{Z}^n$. The set of rational points $\mathbb{Q}^n$ is of the first category.
> (A finite set and $\mathbb{Z}^n$ are closed, and contain no ball, since every ball contains points with an irrational coordinate. $\mathbb{Q}^n$ is countable, hence a countable union of one-point sets $\{q\}$, each closed with no interior. Note that $\mathbb{Q}^n$ itself is dense, so “first category” does not mean “small” in the sense of closure.)

^ex-40-1

The Baire category theorem says that a complete metric space must be of the second category: completeness means it contains “too many points” to be a countable union of nowhere dense sets. First a lemma.

> [!theorem] Lemma §40.1: Nowhere Dense via Balls
> Let $(X, d)$ be a metric space and $E \subset X$. Then $E$ is nowhere dense if and only if for every open ball $B(x_0, r) \subset X$ there is a ball $B(x_1, r_1)$, $r, r_1 > 0$, with
>
> $$
> \overline{B(x_1, r_1)} \subset B(x_0, r) \qquad \text{and} \qquad \overline{B(x_1, r_1)} \cap \overline{E} = \varnothing .
> $$

^lem-40-1

![[m556-40-1.svg]]

Inside any ball there is a smaller closed ball that misses $\overline{E}$ entirely. (The dots stand for $\overline{E}$; a nowhere dense set can be much larger than a discrete set, e.g. a Cantor set.)

> [!proof]+ Proof
> **($\Rightarrow$)** Assume $E$ is nowhere dense, and let $B(x_0, r)$ be an open ball. Then $\overline{E} \neq X$ (otherwise every point of $X$, e.g. $x_0$, would be an interior point of $\overline{E}$), so $\overline{E}^{\,c}$ is open and nonempty. Also $B(x_0, r) \cap \overline{E}^{\,c}$ is open and nonempty; otherwise $B(x_0, r) \subset \overline{E}$, and $x_0$ would be an interior point of $\overline{E}$. So there is an open ball with
>
> $$
> B(x_1, 2r_1) \subset B(x_0, r) \cap \overline{E}^{\,c} .
> $$
>
> (Take any $x_1$ in this open nonempty set; some $B(x_1, \rho)$ lies in it, and put $r_1 = \rho/2$.) Then
>
> $$
> \overline{B(x_1, r_1)} \subset B(x_1, 2r_1) \subset B(x_0, r) \cap \overline{E}^{\,c} ,
> $$
>
> which is the claim. (The first inclusion holds because if $x_k \in B(x_1, r_1)$ and $x_k \to x$, then $d(x, x_1) = \lim d(x_k, x_1) \le r_1 < 2r_1$.)
>
> **($\Leftarrow$)** We want to show $E$ is nowhere dense. If not, $\overline{E}$ has an interior point; name it $x_0$. Then there is an open ball $B(x_0, r) \subset \overline{E}$, and every ball $B(x_1, r_1) \subset B(x_0, r)$ satisfies $B(x_1, r_1) \subset \overline{E}$; in particular $x_1 \in \overline{B(x_1, r_1)} \cap \overline{E}$, which is then nonempty. This contradicts the assumption.

^pf-40-1

> [!remark] Remark: Two Facts About Nowhere Dense Sets
> Two facts are used below. (a) If the closed ball $\overline{B(x_1, r_1)}$ works in the lemma, so does $\overline{B(x_1, r_1')}$ for any $0 < r_1' \le r_1$, since it is a subset; so $r_1$ can be taken as small as we like. (b) $E$ and $\overline{E}$ have the same closure ($\overline{E}$ is closed, Proposition [[§11 Normed Linear Spaces#^prop-11-6|§11.6]]), so $E$ is nowhere dense if and only if $\overline{E}$ is. This is why, as Wu said, it makes no difference whether one writes $E_n$ or $\overline{E}_n$ in the proof below.

^rem-40-1

> [!theorem] Theorem §40.2: Baire Category Theorem
> Let $X$ be a (nonempty) complete metric space. Then $X$ is of the second category: $X$ is not a countable union of nowhere dense sets.
>
> *Lax: §15.5, proof of Thm 9 (“Baire category principle”), p. 169*

^thm-40-2

> [!proof]+ Proof
> ($X \neq \varnothing$ is needed: the empty space is a union of empty, nowhere dense sets.) If not, $X = \bigcup_{n=1}^\infty E_n$ with each $E_n$ nowhere dense. We want to show there is at least one point $x^{\ast} \in X$ with $x^{\ast} \notin \bigcup_{n=1}^\infty E_n$, a contradiction. The idea is to construct a sequence of nested closed balls avoiding $E_1, E_2, \ldots$ in turn, and to use completeness to find a point in all of them.
>
> **Nested balls.** Fix $x_0 \in X$ (Wu: “just take the unit ball” $B(0,1)$). Since $E_1$ is nowhere dense, by Lemma [[§40 The Baire Category Theorem#^lem-40-1|§40.1]] there is a ball $B(x_1, r_1)$ with
>
> $$
> \overline{B(x_1, r_1)} \subset B(x_0, 1), \qquad \overline{B(x_1, r_1)} \cap \overline{E}_1 = \varnothing .
> $$
>
> Since $E_2$ is nowhere dense, applied to the ball $B(x_1, r_1)$ the lemma gives $B(x_2, r_2)$ with
>
> $$
> \overline{B(x_2, r_2)} \subset B(x_1, r_1), \qquad \overline{B(x_2, r_2)} \cap \overline{E}_2 = \varnothing ,
> $$
>
> and then also $\overline{B(x_2, r_2)} \cap (\overline{E}_1 \cup \overline{E}_2) = \varnothing$, because $\overline{B(x_2, r_2)} \subset B(x_1, r_1)$ misses $\overline{E}_1$. Continuing, for every $n$ there is $B(x_n, r_n)$ with
>
> $$
> \overline{B(x_n, r_n)} \subset B(x_{n-1}, r_{n-1}) \subset \cdots \subset B(x_1, r_1) \qquad \text{and} \qquad \overline{B(x_n, r_n)} \cap \Bigl( \bigcup_{j=1}^n \overline{E}_j \Bigr) = \varnothing .
> $$
>
> By the remark above we may also take $r_n < 1/n$.
>
> **Completeness.** Since $X$ is complete, $\bigcap_{n=1}^\infty \overline{B(x_n, r_n)} \neq \varnothing$.
> (The centers form a Cauchy sequence: for $m \ge n$, $x_m \in \overline{B(x_m, r_m)} \subset B(x_n, r_n)$, so $d(x_m, x_n) < r_n < 1/n$. By completeness $x_m \to x^{\ast}$ for some $x^{\ast} \in X$. For each fixed $n$, the points $x_m$, $m \ge n$, lie in the closed set $\overline{B(x_n, r_n)}$, so their limit $x^{\ast}$ does too. Hence $x^{\ast} \in \bigcap_n \overline{B(x_n, r_n)}$.)
>
> **Conclusion.** Each $\overline{B(x_n, r_n)}$ misses $\overline{E}_1 \cup \cdots \cup \overline{E}_n$, and the balls are nested, so
>
> $$
> \Bigl( \bigcap_{n=1}^\infty \overline{B(x_n, r_n)} \Bigr) \cap \Bigl( \bigcup_{j=1}^\infty E_j \Bigr) = \varnothing .
> $$
>
> (If $x$ lies in every ball and in some $E_j$, then $x \in \overline{B(x_j, r_j)} \cap \overline{E}_j = \varnothing$.) So $x^{\ast} \notin \bigcup_j E_j = X$, which is impossible.

^pf-40-2

*Uses:* [[§40 The Baire Category Theorem#^lem-40-1|§40.1]]

![[m556-40-2.svg]]

Each closed ball sits inside the previous one and avoids one more $E_j$; completeness provides a point $x^{\ast}$ in all of them, which therefore lies in no $E_j$.
