---
type: section
subject: "[[Functional Analysis]]"
chapter: 7
section: 40
tags: [functional-analysis, math556]
---
← [[§39 Solving Mx = y]] · ↑ [[· 7 Inverses, Open Maps, and Baire Category]] · [[§41 The Open Mapping Theorem and Its Consequences]] →

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
> ($X \neq \varnothing$ is needed: the empty space is a union of empty, nowhere dense sets.) If not, assume $(X, d)$ is complete and
>
> $$
> X = \bigcup_{n=1}^\infty E_n, \qquad E_n \subset X \text{ nowhere dense for every } n .
> $$
>
> We want to show there is at least one point of $X$ that lies in no $E_n$, a contradiction. The idea is to construct a sequence of nested closed balls, the $n$-th one avoiding $E_n$, and to use completeness to find a point in all of them.
>
> **Step 1: nested balls.** Take the open ball $B(x_0, 1)$ with radius $1$ about some $x_0 \in X$ (Wu: $B(0,1)$, thinking of a normed space;
> in a metric space any center will do). By Lemma [[§40 The Baire Category Theorem#^lem-40-1|§40.1]] there is $B(x_1, r_1)$, $r_1 > 0$, with $\overline{B(x_1, r_1)} \subset B(x_0, 1) \cap \overline{E}_1^{\,c}$, i.e.
>
> $$
> \overline{B(x_1, r_1)} \subset B(x_0, 1), \qquad \overline{B(x_1, r_1)} \cap \overline{E}_1 = \varnothing .
> $$
>
> (The lemma's proof produces the closed ball inside $B(x_0, 1) \cap \overline{E}_1^{\,c}$, which is open, and nonempty because $E_1$ is nowhere dense.) Now consider $E_2$. By the lemma there is $B(x_2, r_2)$ with $0 < r_2 < \frac12$ such that
>
> $$
> \overline{B(x_2, r_2)} \subset B(x_1, r_1), \qquad \overline{B(x_2, r_2)} \cap \overline{E}_2 = \varnothing .
> $$
>
> (The radius can always be made smaller: if a closed ball works, so does any smaller closed ball with the same center, fact (a) of the remark *Two Facts About Nowhere Dense Sets*.) Continue. Assume we have obtained
>
> $$
> B(x_{n-1}, r_{n-1}) \subset \cdots \subset B(x_2, r_2) \subset B(x_1, r_1) \subset B(x_0, 1)
> $$
>
> with $r_j < \frac1j$ and $\overline{B(x_j, r_j)} \cap \overline{E}_j = \varnothing$ for $j \le n - 1$. Since $E_n$ is nowhere dense, by the lemma there is $B(x_n, r_n)$ with
>
> $$
> \overline{B(x_n, r_n)} \subset B(x_{n-1}, r_{n-1}), \qquad 0 < r_n < \tfrac1n, \qquad \overline{B(x_n, r_n)} \cap \overline{E}_n = \varnothing .
> $$
>
> We have obtained a sequence of balls $\{B(x_n, r_n)\}_{n=1}^\infty$ with $0 < r_n < \frac1n$ and $B(x_{n+1}, r_{n+1}) \subset B(x_n, r_n)$.
>
> **Step 2: the intersection is empty.** Let
>
> $$
> A = \bigcap_{n=1}^\infty \overline{B(x_n, r_n)} .
> $$
>
> Since $A \subset \overline{B(x_n, r_n)}$ and $\overline{B(x_n, r_n)} \cap \overline{E}_n = \varnothing$, we get $A \cap \overline{E}_n = \varnothing$ for every $n$. Hence
>
> $$
> A \cap \Bigl( \bigcup_{n=1}^\infty \overline{E}_n \Bigr) = \varnothing ,
> $$
>
> and the union contains $\bigcup_n E_n = X$. So $A \cap X = \varnothing$, i.e. $A = \varnothing$.
>
> **Step 3: completeness makes the intersection nonempty.** Wu: this is where completeness is used; without it the balls could shrink to a missing point. For $j > n$, $x_j \in B(x_j, r_j) \subset B(x_n, r_n)$ by the nesting, so
>
> $$
> d(x_j, x_n) < r_n < \tfrac1n \qquad \text{for all } j > n .
> $$
>
> Hence $\{x_j\}_{j=1}^\infty$ is Cauchy (for $j, k > n$, $d(x_j, x_k) \le d(x_j, x_n) + d(x_n, x_k) < \frac2n$). Since $X$ is complete, $x_j \to x^{\ast}$ as $j \to \infty$ for some $x^{\ast} \in X$. Now fix $n$. The sequence $\{x_j\}_{j=n}^\infty$ lies in the closed set $\overline{B(x_n, r_n)}$, so its limit $x^{\ast}$ lies in $\overline{B(x_n, r_n)}$ (Definition [[§11 Normed Linear Spaces#^def-11-6|§11.6]]). This holds for every $n$, so
>
> $$
> x^{\ast} \in \bigcap_{n=1}^\infty \overline{B(x_n, r_n)} = A ,
> $$
>
> and $A \neq \varnothing$, contradicting Step 2.

^pf-40-2

*Uses:* [[§40 The Baire Category Theorem#^lem-40-1|§40.1]]

![[m556-40-2.svg]]

Each closed ball sits inside the previous one and avoids one more $E_j$; completeness provides a point $x^{\ast}$ in all of them, which therefore lies in no $E_j$.
