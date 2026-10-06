---
type: section
subject: "[[Logic and Proofs]]"
chapter: 3
section: 10
eccles: "Ch. 10"
aliases: ["Eccles 10"]
tags: [logic-and-proofs, mat250]
---
← [[§9 Injections, Surjections and Bijections]] · ↑ [[· 3 Numbers and Counting]] · [[§11 Properties of Finite Sets]] →

*Eccles, Chapter 10 and Problems III (Q4) · MAT 200 lecture (syllabus week 14).*

Counting a set means pairing its elements off, one by one, with $1, 2, \ldots, n$, which is to say constructing a bijection from $\{1, \ldots, n\}$ to the set. This section makes that the definition of the number of elements, proves that the number does not depend on the order of counting (using a lemma proved by induction: [[§10 Counting#^pf-10-2|proof of Lemma §10.2]]), and derives the two basic counting principles (disjoint unions and products) and the inclusion–exclusion principle.

## 10.1 Counting Finite Sets

> [!definition] Definition §10.1: Cardinality
> For a positive integer $n$ let
>
> $$
> \N_n = \{1, 2, \ldots, n\} = \{ i \in \Z \mid 1 \le i \le n \}.
> $$
>
> Given a set $X$, if there is a bijection $f : \N_n \to X$, then the **cardinality** of $X$, or the **number of elements** of $X$, is $n$, written $|X| = n$. The cardinality of the empty set is defined to be $0$: $|\emptyset| = 0$.
>
> *Eccles: Definition 10.1.1*

^def-10-1

The standard set $\N_n$ is Eccles's notation and starts at $1$: it is a subset of $\Z^+$, and not the first $n$ elements $\{0, 1, \ldots, n - 1\}$ of $\N = \{0, 1, 2, \ldots\}$ ([[§1 The Language of Mathematics#^def-1-1|Definition §1.1]]). Counting $X$ in a particular order defines such a bijection: $f(1)$ is the element counted first, $f(2)$ the element counted second, and so on. Writing $x_i = f(i)$ lists $X = \{x_1, x_2, \ldots, x_n\}$, each element exactly once: $f$ is injective because nothing is counted twice and surjective because everything is counted.

> [!example] Example §10.1: Two Ways of Counting
> (a) $A = \{ k \in \Z \mid 25 < k \le 30 \}$ has $|A| = 5$. Listing it as $\{29, 26, 30, 27, 28\}$ is the bijection $f : \N_5 \to A$
>
> | $i$ | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|
> | $f(i)$ | 29 | 26 | 30 | 27 | 28 |
>
> while the obvious count is $g : \N_5 \to A$, $g(i) = 25 + i$.
>
> (b) $|\N_n| = n$, by the identity map $\N_n \to \N_n$. Another bijection $\N_n \to \N_n$ is $i \mapsto n + 1 - i$ (counting backwards).
>
> *Eccles: Examples 10.1.2*

^ex-10-1

For the definition to make sense, two different counts of the same set must give the same number. This needs a proof.

> [!remark] Remark: Constructing the Proof
> The difficulty is that the proposition involves a set $X$ about which nothing is known. But $f$ and $g$ are invertible, so $g^{-1} \circ f : \N_m \to X \to \N_n$ is a bijection, and the statement "there is a bijection $\N_m \to \N_n$" no longer mentions $X$. So it suffices to prove the special case $X = \N_n$. Next, a bijection is an injection and a surjection; injectivity alone should force $m \le n$, which is the lemma. Applied to a bijection and to its inverse, the lemma gives $m \le n$ and $n \le m$. Reducing a statement to successively simpler, more concrete ones, and recording the stepping stones as lemmas, is a standard way of building a proof.

^rem-10-1

> [!remark] Remark: Constructing the Proof
> A statement about positive integers suggests induction, and here there are two variables. Inducting on $n$, the predicate is
>
> $$
> P(n) : \quad \forall m \in \Z^+ \ \bigl( \text{there is an injection } \N_m \to \N_n \Rightarrow m \le n \bigr).
> $$
>
> In the inductive step the given statement is $P(k)$ and the goal $P(k+1)$; the $m$ in each is a dummy variable, so rename it $m_1$ in the goal. We are handed an injection $f : \N_{m_1} \to \N_{k+1}$ and must show $m_1 \le k + 1$. The hypothesis $P(k)$ only applies to injections *into $\N_k$*, so the work is to manufacture one from $f$, if necessary by shrinking the domain. (Induction on $m$ also works: Eccles Problems III Q8.)

^rem-11-1

> [!theorem] Lemma §10.2: Injections Between Standard Sets
> If there is an injection $\N_m \to \N_n$, then $m \le n$.
>
> *Eccles: Lemma 10.1.4 (proved in Chapter 11)*

^lem-10-2

> [!proof]+ Proof
> Induction on $n$.
>
> *Base case $n = 1$.* If $f : \N_m \to \N_1$, then $f(i) = 1$ for every $i$; if $m > 1$ then $f(1) = f(2)$, so $f$ is not injective. Hence if $f$ is injective, $m = 1 = n$. (This is really a proof of the contrapositive "$m > 1 \Rightarrow f$ is not injective".)
>
> *Inductive step.* Suppose $P(k)$ holds for some $k \ge 1$, and let $f : \N_{m_1} \to \N_{k+1}$ be an injection. There are two cases.
>
> (i) $f(i) < k + 1$ for all $i \in \N_{m_1}$. Then restricting the codomain gives $f_1 : \N_{m_1} \to \N_k$, $f_1(i) = f(i)$, still injective: $f_1(i_1) = f_1(i_2) \Rightarrow f(i_1) = f(i_2) \Rightarrow i_1 = i_2$. By $P(k)$, $m_1 \le k$, so certainly $m_1 \le k + 1$.
>
> (ii) $f(i_0) = k + 1$ for some $i_0 \in \N_{m_1}$. If $m_1 = 1$ then $m_1 \le k + 1$ and there is nothing to prove; so let $m_1 \ge 2$. Define $g : \N_{m_1 - 1} \to \N_{m_1}$ by
>
> $$
> g(i) = \begin{cases} i & \text{for } i < i_0, \\ i + 1 & \text{for } i \ge i_0, \end{cases}
> $$
>
> an injection whose image misses exactly $i_0$. For $i \ne i_0$ we have $f(i) \ne f(i_0) = k + 1$ because $f$ is injective, so $f(i) \in \N_k$. Hence $f_1 = f \circ g$ can be regarded as a function $\N_{m_1 - 1} \to \N_k$, and it is injective as a composite of injections. By $P(k)$, $m_1 - 1 \le k$, that is, $m_1 \le k + 1$.
>
> One of the cases holds for every $f$, so $P(k+1)$ follows. By induction $P(n)$ holds for all $n \in \Z^+$.

^pf-10-2

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§9 Injections, Surjections and Bijections#^ex-9-8|Ex. §9.8]] (composites of injections)

![[m250-11-1.svg]]
*Case (ii) of the inductive step with $m_1 = 4$, $k + 1 = 5$: $f$ (black) sends $i_0 = 2$ to the top value $5$ (red). The map $g$ (blue) skips $i_0$, so $f \circ g : \N_3 \to \N_5$ never takes the value $5$ and is an injection into $\N_4$, to which the inductive hypothesis applies.*

> [!theorem] Proposition §10.1: Cardinality Is Well Defined
> If $f : \N_m \to X$ and $g : \N_n \to X$ are bijections with the same codomain, then $m = n$.
>
> *Eccles: Proposition 10.1.3*

^prop-10-1

> [!proof]+ Proof
> Since $f$ and $g$ are bijections they have inverses $f^{-1} : X \to \N_m$ and $g^{-1} : X \to \N_n$, which are bijections. So $g^{-1} \circ f : \N_m \to \N_n$ is a bijection, in particular an injection, and Lemma [[§10 Counting#^lem-10-2|§10.2]] gives $m \le n$. Reversing the roles of $f$ and $g$, $f^{-1} \circ g : \N_n \to \N_m$ is an injection, so $n \le m$. Hence $m = n$ ([[§4 Proof by Contradiction#^ex-4-4|Example §4.4]]).

^pf-10-1

*Uses:* [[§10 Counting#^lem-10-2|§10.2]], [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]], [[§9 Injections, Surjections and Bijections#^ex-9-8|Ex. §9.8]], [[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]]

> [!definition] Definition §10.2: Finite and Infinite Sets
> A set $X$ is **finite** if $|X| = n$ for some non-negative integer $n$, that is, if $X = \emptyset$ or there is a bijection $\N_n \to X$ for some $n \in \Z^+$. Otherwise $X$ is **infinite**.
>
> *Eccles: Definition 10.1.5*

^def-10-2

> [!theorem] Proposition §10.3: Equal Cardinality Means a Bijection
> Let $X$ be a finite set with $|X| = n$. A set $Y$ has $|Y| = n$ if and only if there is a bijection $X \to Y$.
>
> *Eccles: Exercise 10.1*

^prop-10-3

> [!proof]+ Proof
> If $n = 0$ then $X = \emptyset$; the only function $\emptyset \to Y$ is the empty function, which is injective and is surjective exactly when $Y = \emptyset$, i.e. when $|Y| = 0$.
>
> Let $n \ge 1$ and let $f : \N_n \to X$ be a bijection. If $|Y| = n$, choose a bijection $g : \N_n \to Y$; then $g \circ f^{-1} : X \to \N_n \to Y$ is a bijection. Conversely, if $h : X \to Y$ is a bijection, then $h \circ f : \N_n \to X \to Y$ is a bijection, so $|Y| = n$.

^pf-10-3

*Uses:* [[§10 Counting#^def-10-1|Def. §10.1]], [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]], [[§9 Injections, Surjections and Bijections#^ex-9-8|Ex. §9.8]]

> [!remark]- Connections
> - The same statement in 451: [[§2 The Set ℚ of Rational Numbers#^thm-2-3|451 Thm. §2.3]]; for infinite sets it becomes the definition of "same cardinality" ([[§14 Counting Infinite Sets#^def-14-1|Def. §14.1]], [[§14 Counting Infinite Sets#^def-14-3|Def. §14.3]]).

## 10.2 Two Basic Counting Principles

> [!theorem] Theorem §10.4: The Addition Principle
> Let $X$ and $Y$ be disjoint finite sets. Then $X \cup Y$ is finite and
>
> $$
> |X \cup Y| = |X| + |Y|.
> $$
>
> *Eccles: Theorem 10.2.1*

^thm-10-4

The conclusion is an "and" statement, but the first part follows from the second: the only way to show that a set is finite is to show that its cardinality is some non-negative integer, here $|X| + |Y|$. The idea is to count $X$ first and then carry on counting $Y$ from $|X| + 1$.

> [!proof]+ Proof
> Let $|X| = n$ and $|Y| = m$. If $n = 0$ then $X = \emptyset$ and $X \cup Y = Y$, so $|X \cup Y| = m = 0 + m$; similarly if $m = 0$. So let $n, m \ge 1$, with bijections $f : \N_n \to X$ and $g : \N_m \to Y$. Define $h : \N_{n+m} \to X \cup Y$ by
>
> $$
> h(i) = \begin{cases} f(i) & \text{if } 1 \le i \le n, \\ g(i - n) & \text{if } n + 1 \le i \le n + m, \end{cases}
> $$
>
> which makes sense because $1 \le i - n \le m$ in the second case.
>
> *$h$ is injective.* Let $h(i) = h(j)$. If $i, j \le n$ then $f(i) = f(j)$, so $i = j$ as $f$ is injective; if $i, j > n$ then $g(i - n) = g(j - n)$, so $i = j$ as $g$ is injective. If $i \le n < j$, then $h(i) \in X$ and $h(j) \in Y$, and $h(i) = h(j)$ would be an element of $X \cap Y = \emptyset$; so this case does not occur.
>
> *$h$ is surjective.* An element of $X$ is $f(i) = h(i)$ for some $i \in \N_n$, since $f$ is surjective; an element of $Y$ is $g(j) = h(j + n)$ for some $j \in \N_m$, since $g$ is surjective.
>
> So $h$ is a bijection and $|X \cup Y| = n + m$. The hypothesis $X \cap Y = \emptyset$ is used exactly once, for injectivity.

^pf-10-4

*Uses:* [[§10 Counting#^def-10-1|Def. §10.1]]

> [!theorem] Corollary §10.5: Unions of Pairwise Disjoint Finite Sets
> Let $n \in \Z^+$ and let $X_1, X_2, \ldots, X_n$ be pairwise disjoint finite sets ($i \ne j \Rightarrow X_i \cap X_j = \emptyset$). Then $X_1 \cup X_2 \cup \cdots \cup X_n = \bigcup_{i=1}^n X_i$ is finite and
>
> $$
> |X_1 \cup X_2 \cup \cdots \cup X_n| = |X_1| + |X_2| + \cdots + |X_n|.
> $$
>
> *Eccles: Corollary 10.2.2 (proof: Exercise 10.2)*

^cor-10-5

> [!proof]+ Proof
> Induction on $n$, the statement $P(n)$ being the corollary for every collection of $n$ pairwise disjoint finite sets. For $n = 1$ it says $|X_1| = |X_1|$. Suppose $P(k)$ holds and let $X_1, \ldots, X_{k+1}$ be pairwise disjoint and finite. By $P(k)$, $U = X_1 \cup \cdots \cup X_k$ is finite with $|U| = |X_1| + \cdots + |X_k|$. Moreover $U \cap X_{k+1} = \emptyset$: an element of both would lie in some $X_i \cap X_{k+1}$ with $i \le k$. By the addition principle $U \cup X_{k+1} = X_1 \cup \cdots \cup X_{k+1}$ is finite with cardinality $|U| + |X_{k+1}| = |X_1| + \cdots + |X_{k+1}|$, which is $P(k+1)$.

^pf-10-5

*Uses:* [[§10 Counting#^thm-10-4|§10.4]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

> [!theorem] Theorem §10.6: The Multiplication Principle
> Let $X$ and $Y$ be finite sets with $|X| = n$ and $|Y| = m$. Then the [[§7 Quantifiers#^def-7-5|Cartesian product]] $X \times Y$ is finite and $|X \times Y| = mn$.
>
> *Eccles: Theorem 10.2.3*

^thm-10-6

> [!proof]+ Proof
> If $X$ or $Y$ is empty, so is $X \times Y$, and $|X \times Y| = 0 = mn$. Otherwise let $f : \N_n \to X$ be a bijection and $x_i = f(i)$, so $X = \{x_1\} \cup \{x_2\} \cup \cdots \cup \{x_n\}$ and
>
> $$
> X \times Y = (\{x_1\} \times Y) \cup (\{x_2\} \times Y) \cup \cdots \cup (\{x_n\} \times Y).
> $$
>
> These sets are pairwise disjoint, since elements of different ones have different first coordinates. If $g : \N_m \to Y$ is a bijection, then $i \mapsto (x_k, g(i))$ is a bijection $\N_m \to \{x_k\} \times Y$ (injective and surjective because $g$ is), so $|\{x_k\} \times Y| = m$ for each $k$. By Corollary [[§10 Counting#^cor-10-5|§10.5]], $|X \times Y| = m + m + \cdots + m = mn$.

^pf-10-6

*Uses:* [[§10 Counting#^cor-10-5|§10.5]], [[§10 Counting#^def-10-1|Def. §10.1]]

> [!example] Example §10.2: Ordered and Unordered Pairs
> (a) By the multiplication principle, $\N_9 \times \N_9$, the set of ordered pairs of positive integers at most $9$, has $9 \times 9 = 81$ elements.
>
> (b) The **diagonal** $\Delta(\N_9) = \{(n, n) \mid n \in \N_9\}$ has $9$ elements, by the bijection $n \mapsto (n, n)$ from $\N_9$. Its complement $\N_9 \times \N_9 - \Delta(\N_9)$ is finite (a subset of a finite set, [[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]], proved in §11), and $\N_9 \times \N_9$ is the disjoint union of the two, so by the addition principle
>
> $$
> 81 = |\Delta(\N_9)| + |\N_9 \times \N_9 - \Delta(\N_9)| = 9 + |\N_9 \times \N_9 - \Delta(\N_9)|.
> $$
>
> So there are $81 - 9 = 72$ ordered pairs of *distinct* positive integers at most $9$. (Directly: $9$ choices for the first coordinate, then $8$ for the second.) Each unordered pair $\{a, b\}$ with $a \ne b$ comes from exactly the two ordered pairs $(a, b)$ and $(b, a)$, so the $72$ ordered pairs fall into disjoint blocks of two, and there are $72 / 2 = 36$ unordered pairs.
>
> *Eccles: Examples 10.2.4*

^ex-10-2

*Uses:* [[§10 Counting#^thm-10-6|§10.6]], [[§10 Counting#^thm-10-4|§10.4]], [[§10 Counting#^cor-10-5|§10.5]], [[§11 Properties of Finite Sets#^cor-11-4|§11.4]]

## 10.3 The Inclusion–Exclusion Principle

For sets that are not disjoint, adding the cardinalities counts the common elements more than once; inclusion–exclusion corrects for this.

> [!theorem] Proposition §10.7: Inclusion–Exclusion for Two Sets
> Let $X$ and $Y$ be finite sets (not necessarily disjoint). Then $X \cup Y$ is finite and
>
> $$
> |X \cup Y| = |X| + |Y| - |X \cap Y|.
> $$
>
> *Eccles: Proposition 10.3.1*

^prop-10-7

> [!proof]+ Proof
> The sets $X - Y$, $Y - X$ and $X \cap Y$ are subsets of finite sets, hence finite ([[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]], proved in §11 from the addition principle, without this proposition), and $X \cup Y = (X - Y) \cup (Y - X) \cup (X \cap Y)$ is a union of pairwise disjoint sets ([[§6 The Language of Set Theory#^prop-6-2|Proposition §6.2]]). By Corollary [[§10 Counting#^cor-10-5|§10.5]],
>
> $$
> |X \cup Y| = |X - Y| + |Y - X| + |X \cap Y|.
> $$
>
> Similarly $X = (X - Y) \cup (X \cap Y)$ and $Y = (Y - X) \cup (X \cap Y)$ are disjoint unions, so $|X| = |X - Y| + |X \cap Y|$ and $|Y| = |Y - X| + |X \cap Y|$. Substituting $|X - Y| = |X| - |X \cap Y|$ and $|Y - X| = |Y| - |X \cap Y|$ gives the result.

^pf-10-7

*Uses:* [[§10 Counting#^cor-10-5|§10.5]], [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], [[§6 The Language of Set Theory#^prop-6-2|§6.2]]

In the Venn diagram of $X$ and $Y$: counting $X$ and then $Y$ counts the region $X \cap Y$ twice, so it is subtracted once.

> [!remark]- Connections
> - The same formula for subspaces, with dimension in place of cardinality: [[§6 Dimension#^ladr-2-43|LADR 2.43]] (dimension of a sum); there the three-set version fails.

> [!theorem] Proposition §10.8: Inclusion–Exclusion for Three Sets
> Let $X$, $Y$ and $Z$ be finite sets. Then $X \cup Y \cup Z$ is finite and
>
> $$
> |X \cup Y \cup Z| = |X| + |Y| + |Z| - |X \cap Y| - |X \cap Z| - |Y \cap Z| + |X \cap Y \cap Z|.
> $$
>
> *Eccles: Proposition 10.3.2*

^prop-10-8

> [!proof]+ Proof
> Apply Proposition [[§10 Counting#^prop-10-7|§10.7]] to $X \cup Y \cup Z = (X \cup Y) \cup Z$, and again to the sets that arise:
>
> $$
> \begin{aligned}
> |(X \cup Y) \cup Z| &= |X \cup Y| + |Z| - |(X \cup Y) \cap Z|, \\
> |X \cup Y| &= |X| + |Y| - |X \cap Y|, \\
> |(X \cup Y) \cap Z| &= |(X \cap Z) \cup (Y \cap Z)| \\
> &= |X \cap Z| + |Y \cap Z| - |(X \cap Z) \cap (Y \cap Z)| \\
> &= |X \cap Z| + |Y \cap Z| - |X \cap Y \cap Z|,
> \end{aligned}
> $$
>
> using the distributive law $(X \cup Y) \cap Z = (X \cap Z) \cup (Y \cap Z)$ ([[§6 The Language of Set Theory#^thm-6-3|Theorem §6.3]]). Substituting the second and third lines into the first gives the formula.

^pf-10-8

*Uses:* [[§10 Counting#^prop-10-7|§10.7]], [[§6 The Language of Set Theory#^thm-6-3|§6.3]] (distributive law)

![[m250-10-1.svg]]
*Each region is labelled by how often the right-hand side of the formula counts its elements: a point of exactly one set is counted once by the single terms; a point of exactly two sets twice by them and once by an intersection term, $2 - 1$; a point of all three, $3 - 3 + 1$. Every element of the union is counted exactly once.*

The general principle is proved by induction, with the three-set proof as the model for the inductive step.

> [!theorem] Theorem §10.9: The Inclusion–Exclusion Principle
> Let $A_1, A_2, \ldots, A_n$ be finite sets ($n \in \Z^+$). For a non-empty $I = \{i_1, \ldots, i_r\} \subseteq \N_n$ write
>
> $$
> A_I = \bigcap_{i \in I} A_i = A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_r}.
> $$
>
> Then $\bigcup_{i=1}^n A_i$ is finite and
>
> $$
> \Bigl| \bigcup_{i=1}^n A_i \Bigr| = \sum_{\emptyset \ne I \subseteq \N_n} (-1)^{|I| - 1} \, |A_I|,
> $$
>
> the sum running over all non-empty subsets $I$ of $\N_n$.
>
> *Eccles: Problems III Q4*
> *Source: MAT 200 lecture (syllabus week 14)*

^thm-10-9

> [!proof]+ Proof
> Induction on $n$, the statement $P(n)$ being the theorem for every family of $n$ finite sets. For $n = 1$ the only $I$ is $\{1\}$ and both sides are $|A_1|$.
>
> Suppose $P(k)$ holds and let $A_1, \ldots, A_{k+1}$ be finite. Put $B = A_1 \cup \cdots \cup A_k$, finite by $P(k)$. By Proposition [[§10 Counting#^prop-10-7|§10.7]], $B \cup A_{k+1} = \bigcup_{i=1}^{k+1} A_i$ is finite and
>
> $$
> \Bigl| \bigcup_{i=1}^{k+1} A_i \Bigr| = |B| + |A_{k+1}| - |B \cap A_{k+1}|.
> $$
>
> By the distributive law $B \cap A_{k+1} = \bigcup_{i=1}^k (A_i \cap A_{k+1})$, a union of $k$ finite sets, whose intersections are $\bigcap_{i \in I} (A_i \cap A_{k+1}) = A_{I \cup \{k+1\}}$. Applying $P(k)$ to both families,
>
> $$
> |B| = \sum_{\emptyset \ne I \subseteq \N_k} (-1)^{|I|-1} |A_I|, \qquad |B \cap A_{k+1}| = \sum_{\emptyset \ne I \subseteq \N_k} (-1)^{|I|-1} |A_{I \cup \{k+1\}}|.
> $$
>
> Now every non-empty $J \subseteq \N_{k+1}$ is of exactly one of three kinds: $J = I \subseteq \N_k$; $J = \{k+1\}$; or $J = I \cup \{k+1\}$ with $\emptyset \ne I \subseteq \N_k$, in which case $|J| = |I| + 1$ and $(-1)^{|J|-1} = -(-1)^{|I|-1}$. The three terms $|B|$, $|A_{k+1}|$ and $-|B \cap A_{k+1}|$ are exactly the sums of $(-1)^{|J|-1}|A_J|$ over the three kinds, so their total is $\sum_{\emptyset \ne J \subseteq \N_{k+1}} (-1)^{|J|-1} |A_J|$. This is $P(k+1)$.

^pf-10-9

*Uses:* [[§10 Counting#^prop-10-7|§10.7]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§6 The Language of Set Theory#^thm-6-3|§6.3]] (distributive law)

For $n = 2$ and $n = 3$ this is Propositions [[§10 Counting#^prop-10-7|§10.7]] and [[§10 Counting#^prop-10-8|§10.8]]. The figure's pattern persists: an element lying in exactly $r$ of the sets is counted $\binom{r}{1} - \binom{r}{2} + \cdots + (-1)^{r-1}\binom{r}{r} = 1$ times, by the binomial theorem ([[§12★ Counting Functions and Subsets#^thm-12-10|Theorem §12.10]], proved in §12★; see [[§12★ Counting Functions and Subsets#^cor-12-11|Corollary §12.11]]) applied to $(1 - 1)^r = 0$.

> [!example] Example §10.3: Tiles
> Each of $144$ tiles is triangular or square, red or blue, wooden or plastic. There are $68$ wooden, $69$ red and $75$ triangular tiles; $36$ are red and wooden, $40$ triangular and wooden, $38$ red and triangular, and $23$ red, wooden and triangular. How many tiles are blue, plastic and square?
>
> Let $W$, $R$, $T$ be the sets of wooden, red and triangular tiles. A tile is blue, plastic and square exactly when it lies in none of them, so the answer is $144 - |W \cup R \cup T|$. By Proposition [[§10 Counting#^prop-10-8|§10.8]],
>
> $$
> |W \cup R \cup T| = 68 + 69 + 75 - 36 - 40 - 38 + 23 = 121,
> $$
>
> and by the addition principle there are $144 - 121 = 23$ blue plastic square tiles.
>
> *Eccles: Exercise 10.4*

^ex-10-3

*Uses:* [[§10 Counting#^prop-10-8|§10.8]], [[§10 Counting#^thm-10-4|§10.4]]
