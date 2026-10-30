---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 50
tags: [group-theory, math493]
---
← [[§49 The Derived Series]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§51 S₃, S₄, Aₙ and GLₙ]] →

*Source: Lecture and Worksheet 12 (Wed Oct 28); lecture (Fri Oct 30), which finished the proof. Taught after the Sylow theorems and semidirect products, and placed here because a composition series is a subnormal series, like the chains that define solvable groups ([[§48 Solvable Groups|§48]]) and the derived series ([[§49 The Derived Series|§49]]). Reference: not covered in the Pinter chapters used so far.*

The course has used the analogy that simple groups are atoms and other groups are molecules built from them. For the analogy to be good, every group should have a well-defined “chemical formula”: a list of simple pieces that does not depend on how the group is taken apart. The Jordan–Hölder theorem says exactly this, for every group that can be taken apart into simple pieces at all, in particular every finite group.

> [!definition] Definition §50.1: Subnormal Series
> Let $G$ be any group. A **subnormal series** of $G$ is a chain of subgroups
>
> $$
> \{e\} = G_0 \trianglelefteq G_1 \trianglelefteq G_2 \trianglelefteq \cdots \trianglelefteq G_N = G
> $$
>
> in which each $G_{j-1}$ is normal in the next term $G_j$ (not necessarily in $G$). The groups $G_j/G_{j-1}$ are its **quotients** (or subquotients).
>
> *Source: lecture 10/28; WS 12*

^def-50-1

> [!definition] Definition §50.2: Composition Series
> A subnormal series $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ (Definition [[§50 Composition Series and the Jordan–Hölder Theorem#^def-50-1|§50.1]]) is a **composition series** if every quotient $G_j/G_{j-1}$ is simple (Definition [[§43 Simple Groups#^def-43-1|§43.1]]). One then thinks of $G$ as made from $G_1/G_0, G_2/G_1, \ldots, G_N/G_{N-1}$, its **composition factors**.
>
> *Source: lecture 10/28; WS 12*

^def-50-2

> [!definition] Definition §50.3: Quasi-Composition Series
> A subnormal series is a **quasi-composition series** if every quotient $G_j/G_{j-1}$ is simple or trivial.
>
> *Source: lecture 10/28; WS 12*

^def-50-3

> [!remark] Remark: Quasi-Composition Series
> The term is the lecturer's own and is not standard. (WS 12 says “a composition series where …”; a subnormal series is meant.) A trivial quotient $G_j/G_{j-1}$ just means $G_{j-1} = G_j$, a repeated term. Deleting the repeated terms turns a quasi-composition series into a composition series with the same simple quotients. Quasi-composition series are convenient in the proof below, where trivial quotients arise naturally.
>
> *Source: lecture 10/28*

^rem-50-1

> [!remark] Remark: Relation to Solvable Groups
> *(Not from class.)* The chain in the definition of a solvable group (Definition [[§48 Solvable Groups#^def-48-1|§48.1]]) is a subnormal series whose quotients are abelian; a composition series is one whose quotients are simple. Since the abelian simple groups are exactly the $\mathbb{Z}/p\mathbb{Z}$ (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]), a composition series all of whose factors are cyclic of prime order shows that $G$ is solvable. Conversely, a finite solvable group has such a composition series: refine each abelian quotient $G_j/G_{j-1}$ by a composition series of it (Lemma [[§50 Composition Series and the Jordan–Hölder Theorem#^lem-50-3|§50.3]]) and pull back, as in the proof of that lemma. Combined with the Jordan–Hölder theorem: *a finite group is solvable if and only if all of its composition factors are cyclic of prime order.* For example, $\{e\} \trianglelefteq \langle (1\,2)(3\,4) \rangle \trianglelefteq K \trianglelefteq A_4 \trianglelefteq S_4$, with $K$ the Klein four-group, has factors $\mathbb{Z}/2, \mathbb{Z}/2, \mathbb{Z}/3, \mathbb{Z}/2$, while $A_5$ has the single factor $A_5$.

^rem-50-2

> [!theorem] Theorem §50.1: Jordan–Hölder Theorem
> Let $G$ be any group, and let
>
> $$
> \{e\} = X_0 \trianglelefteq X_1 \trianglelefteq \cdots \trianglelefteq X_m = G \quad\text{and}\quad \{e\} = Y_0 \trianglelefteq Y_1 \trianglelefteq \cdots \trianglelefteq Y_n = G
> $$
>
> be two composition series, with quotients $S_i = X_i/X_{i-1}$ and $T_j = Y_j/Y_{j-1}$. Then $m = n$, and there is a permutation $\sigma \in S_n$ with $S_i \cong T_{\sigma(i)}$ for $1 \leq i \leq m$.
>
> *Source: lecture 10/28, 10/30; WS 12*

^thm-50-1

> [!proof]+ Proof (given at the end of [[§50 Composition Series and the Jordan–Hölder Theorem|§50]])
> The proof needs the grid of intersections of the two series, set up in [[§50 Composition Series and the Jordan–Hölder Theorem|§50]], and it is given there, after Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-10|§50.10]]. WS 12.1–12.3 were done on 10/28 and WS 12.4–12.6 on 10/30. The lecture's comment: the theorem justifies the program of studying groups through simple groups (the remark *Peeling Off Atoms* after the proof).

^pf-50-1

*Uses:* [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-10|§50.10]]

> [!theorem] Proposition §50.2: $\mathbb{Z}$ Has No Composition Series
> Not every group has a composition series: $\mathbb{Z}$ has none.
>
> *Source: lecture 10/28*

^prop-50-2

> [!proof]+ Proof
> *Idea:* the factors of a composition series of an abelian group are finite, so the group would be finite.
>
> *(Lecture 10/28, answering a student's question.)* Suppose $\{0\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = \mathbb{Z}$ were a composition series. Every quotient $G_j/G_{j-1}$ is a quotient of a subgroup of an abelian group, hence abelian, and simple, hence $\cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$ (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]). Then $|G_j| = |G_{j-1}| \cdot |G_j/G_{j-1}|$ (Lagrange, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]) shows by induction that every $G_j$ is finite, including $G_N = \mathbb{Z}$, a contradiction.

^pf-50-2

*Uses:* [[§43 Simple Groups#^thm-43-1|§43.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!theorem] Lemma §50.3: Finite Groups Have Composition Series
> Every finite group $G$ has a composition series.
>
> *Source: lecture 10/28*

^lem-50-3

> [!proof]+ Proof
> *Idea:* split $G$ at a proper nontrivial normal subgroup $N$ and stitch a series of $N$ to the preimage of a series of $G/N$.
>
> *(Board 10/28.)* Strong induction on $|G|$. If $G$ is trivial, $\{e\} = G_0 = G$ is a composition series (with no quotients); if $G$ is simple, $\{e\} \trianglelefteq G$ is one. Otherwise there is a normal subgroup $N$ with $\{e\} \subsetneq N \subsetneq G$. Then $|N| < |G|$ and $|G/N| < |G|$, so by induction there are composition series
>
> $$
> \{e\} = N_0 \trianglelefteq N_1 \trianglelefteq \cdots \trianglelefteq N_a = N, \qquad \{e\} = Q_0 \trianglelefteq Q_1 \trianglelefteq \cdots \trianglelefteq Q_b = G/N.
> $$
>
> Let $\pi: G \to G/N$ be the projection. The lecture's image: $N$ is an island in the middle of the stream, where the pylons of the bridge from $\{e\}$ to $G$ can be planted. Stitch the two series together:
>
> $$
> \{e\} = N_0 \trianglelefteq \cdots \trianglelefteq N_a = N = \pi^{-1}(Q_0) \trianglelefteq \pi^{-1}(Q_1) \trianglelefteq \cdots \trianglelefteq \pi^{-1}(Q_b) = G.
> $$
>
> The first half has simple quotients by assumption. For the second half, consider $\alpha_j: \pi^{-1}(Q_j) \to Q_j/Q_{j-1}$, $x \mapsto \pi(x)Q_{j-1}$. It is a homomorphism, it is surjective because $\pi$ maps $\pi^{-1}(Q_j)$ onto $Q_j$, and its kernel is $\{x : \pi(x) \in Q_{j-1}\} = \pi^{-1}(Q_{j-1})$. So $\pi^{-1}(Q_{j-1})$ is normal in $\pi^{-1}(Q_j)$ (Kernels Are Normal, Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]), and by the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]])
>
> $$
> \pi^{-1}(Q_j)/\pi^{-1}(Q_{j-1}) \cong Q_j/Q_{j-1},
> $$
>
> which is simple. (The board cites the Third Isomorphism Theorem, Theorem [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|§42.5]], or the correspondence theorem, Theorem [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]], for this isomorphism; the argument above gives it directly.) Hence the stitched chain is a composition series of $G$.

^pf-50-3

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|§42.5]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]]

![[m493-56-3.svg]]

*(Not from lecture; figure added, after the lecture's image.)* The proof of Lemma [[§50 Composition Series and the Jordan–Hölder Theorem#^lem-50-3|§50.3]]: the normal subgroup $N$ is the island in the stream from $\{e\}$ to $G$. A composition series of $N$ reaches the island, and the preimages $\pi^{-1}(Q_j)$ of a composition series of $G/N$ carry the bridge on to $G$; each new quotient is $\cong Q_j/Q_{j-1}$.

> [!example] Example §50.1: The Order of the Factors Is Not Arbitrary
> A student asked whether every ordering of the composition factors is realized by some composition series. On 10/30 the lecture gave a group in which every ordering occurs, $(\mathbb{Z}/p\mathbb{Z})^n$ (Example [[§50 Composition Series and the Jordan–Hölder Theorem#^ex-50-2|§50.2]]). In general the answer is no (not from class). $S_3$ has the composition series $\{e\} \trianglelefteq A_3 \trianglelefteq S_3$, with factors $\mathbb{Z}/3, \mathbb{Z}/2$ in that order, and no composition series with the factors in the order $\mathbb{Z}/2, \mathbb{Z}/3$.
>
> *Source: question from class 10/28; the example $(\mathbb{Z}/p\mathbb{Z})^n$ lecture 10/30; $S_3$ not from class*

^ex-50-1

> [!proof]+ Proof
> *(Not from class.)* A composition series with first factor $\mathbb{Z}/2$ and second $\mathbb{Z}/3$ would be $\{e\} \trianglelefteq G_1 \trianglelefteq S_3$ with $|G_1| = 2$ and $G_1$ normal in $S_3$. But the subgroups of order $2$ of $S_3$ are the $\langle (i\,j) \rangle$, and none is normal: $(1\,3)(1\,2)(1\,3) = (2\,3)$.

^pf-ex-50-1

> [!theorem] Lemma §50.4: Two Normal Subgroups with Simple Quotients
> Let $G$ be a finite group and $N_1 \neq N_2$ normal subgroups such that $G/N_1$ and $G/N_2$ are both simple. Then:
>
> 1. $N_1 N_2 = G$;
> 2. $G/N_1 \cong N_2/(N_1 \cap N_2)$ and $G/N_2 \cong N_1/(N_1 \cap N_2)$.
>
> *Source: PS 7.4; “I expect to use this lemma in Friday's class”*

^lem-50-4

> [!proof]+ Proof
> *Idea:* $N_1N_2/N_1$ is a normal subgroup of the simple group $G/N_1$, and likewise for $N_2$; they cannot both be trivial since $N_1 \neq N_2$, so $N_1N_2 = G$, and the Second Isomorphism Theorem gives the quotients.
>
> *(Problem Set 7, Problem 7.4, as submitted.)* **(1)** **$N_1N_2 = N_2N_1$.** Let $n_1 \in N_1$ and $n_2 \in N_2$. Since $N_1$ is normal, $n_2n_1n_2^{-1} \in N_1$, so
>
> $$
> n_2n_1 = (n_2n_1n_2^{-1})\,n_2 \in N_1N_2.
> $$
>
> Hence $N_2N_1 \subseteq N_1N_2$. Likewise, since $N_2$ is normal, $n_1n_2 = n_2\,(n_2^{-1}n_1n_2) \in N_2N_1$, so $N_1N_2 \subseteq N_2N_1$. Therefore $N_1N_2 = N_2N_1$.
>
> **$N_1N_2$ is a subgroup of $G$.** It contains $e = e \cdot e$. For $a_1, a_2 \in N_1$ and $b_1, b_2 \in N_2$, we have $b_1a_2 \in N_2N_1 = N_1N_2$, say $b_1a_2 = a'b'$ with $a' \in N_1$, $b' \in N_2$, so
>
> $$
> (a_1b_1)(a_2b_2) = a_1(b_1a_2)b_2 = (a_1a')(b'b_2) \in N_1N_2,
> $$
>
> and $(a_1b_1)^{-1} = b_1^{-1}a_1^{-1} \in N_2N_1 = N_1N_2$.
>
> **$N_1N_2$ is normal in $G$.** For $g \in G$, since $N_1$ and $N_2$ are normal,
>
> $$
> gN_1N_2g^{-1} = (gN_1g^{-1})(gN_2g^{-1}) = N_1N_2.
> $$
>
> **The quotients.** Since $N_1 \subseteq N_1N_2$ and $N_1$ is normal in $G$, hence in $N_1N_2$, the quotient $N_1N_2/N_1 = \{xN_1 : x \in N_1N_2\}$ is a subgroup of $G/N_1$. It is normal in $G/N_1$: for $gN_1 \in G/N_1$ and $x \in N_1N_2$,
>
> $$
> (gN_1)(xN_1)(gN_1)^{-1} = gxg^{-1}N_1 \in N_1N_2/N_1,
> $$
>
> since $gxg^{-1} \in N_1N_2$. Since $G/N_1$ is simple, $N_1N_2/N_1$ is either trivial or all of $G/N_1$. In the same way, $N_1N_2/N_2$ is a normal subgroup of $G/N_2$, so it is either trivial or all of $G/N_2$.
>
> **They cannot both be trivial.** Suppose $N_1N_2/N_1$ is trivial, that is, $xN_1 = N_1$ for every $x \in N_1N_2$. Since $xN_1 = N_1$ if and only if $x \in N_1$, this gives $N_1N_2 \subseteq N_1$; conversely $N_1 \subseteq N_1N_2$, as $n_1 = n_1e$. So $N_1N_2 = N_1$, and hence $N_2 \subseteq N_1N_2 = N_1$, as $n_2 = en_2$. In the same way, if $N_1N_2/N_2$ is trivial, then $N_1 \subseteq N_2$. If both were trivial, we would have $N_1 = N_2$, contradicting $N_1 \neq N_2$.
>
> **Conclusion.** Hence at least one of $N_1N_2/N_1 = G/N_1$ and $N_1N_2/N_2 = G/N_2$ holds. Since the hypotheses are symmetric in $N_1$ and $N_2$ and $N_1N_2 = N_2N_1$, we may assume without loss of generality that $N_1N_2/N_1 = G/N_1$. By Lagrange's theorem,
>
> $$
> \frac{|N_1N_2|}{|N_1|} = |N_1N_2/N_1| = |G/N_1| = \frac{|G|}{|N_1|},
> $$
>
> so $|N_1N_2| = |G|$. Since $N_1N_2$ is a subset of the finite group $G$, $N_1N_2 = G$.
>
> **(2)** Recall the second isomorphism theorem: if $H$ is a subgroup of $G$ and $N$ is a normal subgroup of $G$, then $HN$ is a subgroup of $G$, $H \cap N$ is normal in $H$, and
>
> $$
> H/(H \cap N) \cong HN/N.
> $$
>
> **$G/N_2 \cong N_1/(N_1 \cap N_2)$.** Take $H = N_1$ and $N = N_2$, which is normal in $G$. The second isomorphism theorem gives
>
> $$
> N_1/(N_1 \cap N_2) \cong N_1N_2/N_2 = G/N_2,
> $$
>
> using $N_1N_2 = G$ from (1).
>
> **$G/N_1 \cong N_2/(N_1 \cap N_2)$.** Take $H = N_2$ and $N = N_1$, which is normal in $G$. The second isomorphism theorem gives
>
> $$
> N_2/(N_2 \cap N_1) \cong N_2N_1/N_1 = G/N_1,
> $$
>
> using $N_2N_1 = N_1N_2 = G$ from (1). Since $N_2 \cap N_1 = N_1 \cap N_2$, this is $G/N_1 \cong N_2/(N_1 \cap N_2)$.

^pf-50-4

> [!remark] Remark: The Quotient by $N_1 \cap N_2$
> Speyer, on Problem 7.4: in this situation one can further show that $G/(N_1 \cap N_2) \cong N_1/(N_1 \cap N_2) \times N_2/(N_1 \cap N_2)$. *(Proof not from class.)* In $\bar G = G/(N_1 \cap N_2)$, the images $\bar N_i = N_i/(N_1 \cap N_2)$ are normal, they intersect trivially, since $\bar N_1 \cap \bar N_2 = (N_1 \cap N_2)/(N_1 \cap N_2)$, and $\bar N_1 \bar N_2 = \bar G$ because $N_1 N_2 = G$. So $\bar G \cong \bar N_1 \times \bar N_2$ by Internal Direct Products Are Direct Products (Theorem [[§55 Internal and External Direct Products#^thm-55-1|§55.1]], in Chapter 10).

^rem-50-3

## The Grid of Intersections

*The approach is taken from Ravi Vakil's *Foundations of Algebraic Geometry* (WS 12). Throughout, the two composition series are those of the Jordan–Hölder theorem (Theorem [[§50 Composition Series and the Jordan–Hölder Theorem#^thm-50-1|§50.1]]).*

> [!definition] Definition §50.4: The Grid $Z_{ij}$
> Put
>
> $$
> Z_{ij} = X_i \cap Y_j \qquad (0 \leq i \leq m,\ 0 \leq j \leq n),
> $$
>
> arranged in a rectangular grid as on the worksheet: $i$ increasing to the right (east) and $j$ increasing upwards (north), so $Z_{00}$ is the bottom left corner and $Z_{mn} = G$ the top right.
>
> *Source: WS 12; lecture 10/28*

^def-50-4

> [!theorem] Lemma §50.5: Intersections in the Grid
> $Z_{ab} \cap Z_{cd} = Z_{\min(a,c)\,\min(b,d)}$. In particular $Z_{i0} = Z_{0j} = \{e\}$, $Z_{in} = X_i$ and $Z_{mj} = Y_j$.
>
> *Source: WS 12; lecture 10/28*

^lem-50-5

> [!proof]+ Proof
> Both series increase, so $X_a \cap X_c = X_{\min(a,c)}$ and $Y_b \cap Y_d = Y_{\min(b,d)}$; hence $Z_{ab} \cap Z_{cd} = (X_a \cap X_c) \cap (Y_b \cap Y_d) = X_{\min(a,c)} \cap Y_{\min(b,d)}$. For the special cases, $X_i \cap \{e\} = \{e\} \cap Y_j = \{e\}$, $X_i \cap G = X_i$, $G \cap Y_j = Y_j$.

^pf-50-5

> [!theorem] Proposition §50.6: Normality in the Grid
> $Z_{(i-1)j} \trianglelefteq Z_{ij}$ and $Z_{i(j-1)} \trianglelefteq Z_{ij}$.
>
> *Source: WS 12.2*

^prop-50-6

> [!proof]+ Proof
> *Idea:* conjugating by $z \in X_i \cap Y_j$ preserves $X_{i-1}$ (normal in $X_i$) and $Y_j$ (a group containing $z$).
>
> *(Worksheet session 10/28.)* Let $z \in Z_{ij} = X_i \cap Y_j$ and $w \in Z_{(i-1)j} = X_{i-1} \cap Y_j$. Then $zwz^{-1} \in X_{i-1}$, because $X_{i-1} \trianglelefteq X_i$ and $z \in X_i$; and $zwz^{-1} \in Y_j$, because $z, w \in Y_j$. So $zwz^{-1} \in Z_{(i-1)j}$. The second statement is symmetric.

^pf-50-6

> [!definition] Definition §50.5: Edge Quotients $H_{ij}$ and $V_{ij}$
> For $i, j \geq 1$ (and $H_{i0}$, $V_{0j}$ likewise) define, using Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-6|§50.6]],
>
> $$
> H_{ij} = Z_{ij}/Z_{(i-1)j} \quad \text{(horizontal edges)}, \qquad V_{ij} = Z_{ij}/Z_{i(j-1)} \quad \text{(vertical edges)}.
> $$
>
> A trivial $H_{ij}$ or $V_{ij}$ means that the two groups at the ends of the edge are equal; the worksheet labels such an edge “$=$”.
>
> *Source: WS 12; lecture 10/28*

^def-50-5

![[m493-56-1.svg]]

*(Figure from WS 12, redrawn.)* The grid $Z_{ij} = X_i \cap Y_j$. Arrows are inclusions, each normal (Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-6|§50.6]]). The bottom row and left column are trivial; the top row is the $X$-series ($Z_{in} = X_i$) and the right column the $Y$-series ($Z_{mj} = Y_j$). Horizontal edges carry the quotients $H_{ij}$, vertical edges the $V_{ij}$.

> [!remark] Remark: The Strategy
> Every path through the grid from $Z_{00}$ to $Z_{mn}$, travelling one step east or north at a time, is a chain of subgroups. The essence of the proof is to show that every such path is a quasi-composition series, with the same simple quotients in each case. The two extreme paths give the $S_i$ and the $T_j$ (WS 12.1).
>
> *Source: WS 12*

^rem-50-4

> [!theorem] Proposition §50.7: The Two Edge Paths
> $(Z_{00}, Z_{10}, \ldots, Z_{m0}, Z_{m1}, \ldots, Z_{mn})$ and $(Z_{00}, Z_{01}, \ldots, Z_{0n}, Z_{1n}, \ldots, Z_{mn})$ are quasi-composition series. The quotients of the first are $m$ trivial groups followed by $T_1, \ldots, T_n$; those of the second are $n$ trivial groups followed by $S_1, \ldots, S_m$.
>
> *Source: WS 12.1*

^prop-50-7

> [!proof]+ Proof
> *Idea:* the bottom row and left column are trivial, the right column and top row are the two series.
>
> *(Worksheet session 10/28.)* By Lemma [[§50 Composition Series and the Jordan–Hölder Theorem#^lem-50-5|§50.5]], $Z_{i0} = \{e\}$ and $Z_{mj} = Y_j$, so the first path is $\{e\}, \ldots, \{e\}$ ($m + 1$ times) followed by $Y_1, \ldots, Y_n$: its quotients are trivial $m$ times, then $Y_j/Y_{j-1} = T_j$, each simple. The second is symmetric, with $Z_{0j} = \{e\}$ and $Z_{in} = X_i$.

^pf-50-7

*Uses:* [[§50 Composition Series and the Jordan–Hölder Theorem#^lem-50-5|§50.5]]

> [!theorem] Proposition §50.8: Horizontal Edges Propagate
> 1. The inclusion $Z_{i(j-1)} \hookrightarrow Z_{ij}$ induces a well-defined injection $H_{i(j-1)} \hookrightarrow H_{ij}$.
> 2. The image of $H_{i(j-1)}$ is normal in $H_{ij}$.
> 3. Each $H_{ij}$ is trivial or isomorphic to $S_i$. More precisely, in each column $i$ there is $j_0$ with $H_{ij}$ trivial for $j < j_0$ and $H_{ij} \cong S_i$ for $j \geq j_0$.
>
> Similarly, each $V_{ij}$ is trivial or isomorphic to $T_j$.
>
> *Source: WS 12.3; board 10/28*

^prop-50-8

> [!proof]+ Proof
> *Idea:* restricting $Z_{ij} \to H_{ij}$ to $Z_{i(j-1)}$ has kernel $Z_{(i-1)(j-1)}$; so the column $H_{i0} \hookrightarrow \cdots \hookrightarrow H_{in} = S_i$ is a chain of normal subgroups ending in a simple group.
>
> *(Board 10/28.)* **(1), (2).** Let $\pi: Z_{ij} \to H_{ij} = Z_{ij}/Z_{(i-1)j}$ be the projection, and restrict it to $Z_{i(j-1)}$. By Restricting a Homomorphism (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]), the restriction has kernel
>
> $$
> Z_{(i-1)j} \cap Z_{i(j-1)} = Z_{(i-1)(j-1)}
> $$
>
> (Lemma [[§50 Composition Series and the Jordan–Hölder Theorem#^lem-50-5|§50.5]]), so by the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]) $\pi$ induces an injective homomorphism
>
> $$
> H_{i(j-1)} = Z_{i(j-1)}/Z_{(i-1)(j-1)} \;\xrightarrow{\ \sim\ }\; \pi(Z_{i(j-1)}) \;\subseteq\; H_{ij}, \qquad x Z_{(i-1)(j-1)} \mapsto x Z_{(i-1)j}.
> $$
>
> Since $Z_{i(j-1)} \trianglelefteq Z_{ij}$ (Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-6|§50.6]]) and $\pi$ is surjective, the image $\pi(Z_{i(j-1)})$ is normal in $H_{ij}$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], WS 6.6(3)).
>
> This is part (1) of Proposition [[§48 Solvable Groups#^prop-48-4|§48.4]], applied in the group $Y_j$ to the chain $Z_{0j} \trianglelefteq \cdots \trianglelefteq Z_{mj} = Y_j$ and the subgroup $Y_{j-1}$, whose intersections with the chain are the $Z_{i(j-1)}$. The new ingredient is the normality in (2).
>
> **(3)** By (1) and (2), each $H_{i(j-1)}$ is isomorphic to a normal subgroup of $H_{ij}$, giving a chain up the column
>
> $$
> \{e\} = H_{i0} \hookrightarrow H_{i1} \hookrightarrow \cdots \hookrightarrow H_{in} = S_i,
> $$
>
> where $H_{i0} = Z_{i0}/Z_{(i-1)0} = \{e\}/\{e\}$ and $H_{in} = X_i/X_{i-1} = S_i$. Work down from the top of the column. $S_i$ is simple, so its normal subgroup $\pi(Z_{i(n-1)})$ is trivial or all of $S_i$; hence $H_{i(n-1)}$ is trivial or $\cong S_i$. If $H_{ij}$ is trivial or $\cong S_i$, the same argument applies to $H_{i(j-1)}$, a normal subgroup of $H_{ij}$ up to isomorphism. So every $H_{ij}$ is trivial or $\cong S_i$. Since $H_{i(j-1)}$ injects into $H_{ij}$, once some $H_{ij}$ is nontrivial so are all those above it in the column, which gives $j_0$. (The induction works one step at a time; it does not use transitivity of normality, which fails.) The statement for $V_{ij}$ is the same argument with the roles of $X$ and $Y$ exchanged.

^pf-50-8

*Uses:* [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]], [[§50 Composition Series and the Jordan–Hölder Theorem#^lem-50-5|§50.5]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-6|§50.6]], [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], [[§48 Solvable Groups#^prop-48-4|§48.4]]

> [!remark] Remark: The Possible Squares
> Consider one square of the grid. To keep the subscripts out of the way, the lecture names its corners
>
> $$
> A = Z_{(i-1)(j-1)}, \qquad B = Z_{i(j-1)}, \qquad C = Z_{(i-1)j}, \qquad D = Z_{ij},
> $$
>
> so that $A \trianglelefteq B \trianglelefteq D$ and $A \trianglelefteq C \trianglelefteq D$ (Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-6|§50.6]]). In the grid, as on the board, $A$ is the bottom left corner, $B$ the bottom right, $C$ the top left and $D$ the top right. The four edges carry:
> - bottom $B/A = H_{i(j-1)}$ and top $D/C = H_{ij}$: each is “$=$” or $S_i$;
> - left $C/A = V_{(i-1)j}$ and right $D/B = V_{ij}$: each is “$=$” or $T_j$.
>
> By Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-8|§50.8]], a nontrivial bottom edge forces a nontrivial top edge, and a nontrivial left edge forces a nontrivial right edge. So (bottom, top) is $(=, =)$, $(=, S_i)$ or $(S_i, S_i)$, and (left, right) is $(=, =)$, $(=, T_j)$ or $(T_j, T_j)$: before any thinking, there are $3 \times 3 = 9$ kinds of square, drawn below.
>
> *Source: WS 12.4–12.5; lecture 10/30*

^rem-50-5

![[m493-50-1.svg]]

*(Figure after the lecture; pipes added.)* The nine kinds of square; the corners $A, B, C, D$ are as in the key. A dashed edge marked $=$ is a trivial quotient: its two corners are equal. $S$ stands for $S_i$ on the horizontal edges and $T$ for $T_j$ on the vertical ones. In the four impossible squares (a)–(d), exactly one of the two directions changes from trivial to nontrivial across the square (Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-9|§50.9]]). In the allowed squares (i)–(v), the coloured lines are the pipes of the remark *Changeover Squares and Pipes* below: a pipe runs through each pair of nontrivial opposite edges, and in the crossing square (v) it turns the corner, from $S$ on the top to $T$ on the right, where $S \cong T$ (Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-10|§50.10]]).

> [!theorem] Proposition §50.9: Four Impossible Squares
> With the corners $A, B, C, D$ of a square as in the remark *The Possible Squares*, none of the following occurs (squares (a)–(d) of the figure):
>
> 1. bottom $=$, top $S_i$, left $T_j$, right $T_j$:  $B = A$, $D/C \cong S_i$, $C/A \cong T_j$, $D/B \cong T_j$;
> 2. bottom $S_i$, top $S_i$, left $=$, right $T_j$:  $B/A \cong S_i$, $D/C \cong S_i$, $C = A$, $D/B \cong T_j$;
> 3. bottom $=$, top $S_i$, left $=$, right $=$:  $B = A$, $D/C \cong S_i$, $C = A$, $D = B$;
> 4. bottom $=$, top $=$, left $=$, right $T_j$:  $B = A$, $D = C$, $C = A$, $D/B \cong T_j$.
>
> In words: across one square, the horizontal edges cannot change from trivial to $S_i$ unless the vertical edges also change from trivial to $T_j$, and conversely. (Worksheet hint: think about $Z_{ij}/Z_{(i-1)(j-1)} = D/A$.)
>
> *Source: WS 12.4; lecture 10/30*

^prop-50-9

> [!proof]+ Proof
> *Idea:* in (a), $D/A$ is the simple group $T_j$, and $C$ gives a normal subgroup $C/A$ of it that is neither trivial nor everything; (b) is the mirror image, and (c), (d) are degenerate.
>
> *(Board 10/30.)* Throughout, a trivial quotient means equal groups: $B/A$ trivial means $B = A$, and so on.
>
> **(a), Step 1: $D/A$ is simple.** Since $B = A$, the quotient $D/A$ is the quotient $D/B$, which is $T_j$, a simple group.
>
> **Step 2: $C/A$ is a normal subgroup of $D/A$.** We have $A \subseteq C$ and $C \trianglelefteq D$. The projection $D \to D/A$ is surjective and maps $C$ onto $C/A$; the image of a normal subgroup under a surjective homomorphism is normal (Proposition [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], WS 6.6(3)). So $C/A \trianglelefteq D/A$.
>
> **Step 3: both possibilities are contradictory.** By Steps 1 and 2, $C/A$ is trivial or all of $D/A$.
> - If $C/A$ is trivial, then $C = A$; but $C/A \cong T_j$ is not trivial.
> - If $C/A = D/A$, then each coset $dA$ with $d \in D$ equals some $cA$ with $c \in C$, so $d \in cA \subseteq C$. Hence $C = D$ and $D/C$ is trivial; but $D/C \cong S_i$ is not trivial.
>
> **(b)** This is (a) with the roles of $B$ and $C$ exchanged. Since $C = A$, the quotient $D/A = D/C \cong S_i$ is simple (Step 1). $B/A$ is a normal subgroup of it, because $B \trianglelefteq D$ (Step 2). If $B/A$ is trivial, this contradicts $B/A \cong S_i$; if $B/A = D/A$, then $B = D$, contradicting $D/B \cong T_j$ (Step 3).
>
> **(c)** $B = A = C$, so $D/C = D/B$, which is trivial since $D = B$. This contradicts $D/C \cong S_i$.
>
> **(d)** $B = A = C$, so $D/B = D/C$, which is trivial since $D = C$. This contradicts $D/B \cong T_j$.

^pf-50-9

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]]

![[m493-50-2.svg]]

*(Not from lecture; figure added.)* Case (a) of the proof. Left: the square. Right: the subgroups between $A$ and $D$, with the quotients on the edges. Since $B = A$, the whole quotient $D/A$ is the simple group $T_j$. But $C$ lies strictly between $A$ and $D$ (both $C/A$ and $D/C$ are nontrivial), so $C/A$ would be a normal subgroup of $D/A$ that is neither trivial nor everything.

> [!remark] Remark: The Same Argument by Counting
> For finite $G$, case (a) is also a count of indices, as a student suggested on the board. By Lagrange's theorem along the two paths from $A$ to $D$,
>
> $$
> [D : A] = [D : C]\,[C : A] = |S_i| \cdot |T_j|, \qquad [D : A] = [D : B]\,[B : A] = |T_j| \cdot 1,
> $$
>
> so $|S_i| = 1$, impossible for a simple group. The quotient argument above works for infinite groups too. Another student proposed comparing $(D/A)/(B/A) \cong D/B$ and $(D/A)/(C/A) \cong D/C$ (Third Isomorphism Theorem, Theorem [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|§42.5]]), which is the same argument in other words. In the crossing square the count gives only $|S_i| = |T_j|$: this suggests the isomorphism of the next proposition, but does not prove it.
>
> *Source: lecture 10/30*

^rem-50-6

> [!theorem] Proposition §50.10: The Crossing Square
> Suppose a square has bottom and left edges trivial ($B = A$ and $C = A$), top edge $D/C \cong S_i$ and right edge $D/B \cong T_j$: the crossing square (v). Then $S_i \cong T_j$. (Worksheet hint: think about $Z_{ij}/Z_{(i-1)(j-1)}$.)
>
> *Source: WS 12.5; lecture 10/30*

^prop-50-10

> [!proof]+ Proof
> *Idea:* the two trivial edges say that $A$, $B$ and $C$ are one subgroup, so the two nontrivial edges are literally the same quotient.
>
> *(Board 10/30.)* Since $B = A$ and $C = A$, the three corners $A$, $B$, $C$ are the same subgroup of $D$. So the right edge $D/B$ and the top edge $D/C$ are the same group of cosets, and
>
> $$
> T_j \cong D/B = D/C \cong S_i.
> $$

^pf-50-10

> [!remark] Remark: Changeover Squares and Pipes
> By Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-8|§50.8]](3), the horizontal edges of column $i$ read, from the bottom up,
>
> $$
> =,\ \ldots,\ =,\ S_i,\ \ldots,\ S_i :
> $$
>
> the column starts with $H_{i0} = \{e\}$, ends with $H_{in} = S_i$ on the top row, and changes exactly once. The square where it changes is the **changeover square** of column $i$: its bottom edge is “$=$” and its top edge $S_i$. Likewise the vertical edges of row $j$ read $=, \ldots, =, T_j, \ldots, T_j$ from left to right, and row $j$ has one changeover square, with left edge “$=$” and right edge $T_j$. The impossible squares say that the changeover square of a column is the changeover square of a row, and conversely: the changeovers line up. The lecture records this with **pipes**. Along each column a pipe runs through its $S_i$ edges, from $S_i$ on the top row down to the changeover square; along each row a pipe runs through its $T_j$ edges, from $T_j$ on the right column back to the changeover square. The two meet in a crossing square, so each pipe joins one $S_i$ (top) to one $T_j$ (right), and carries a single simple group along its whole length. The figure below builds this in three steps.
>
> *Source: lecture 10/30; WS 12*

^rem-50-7

![[m493-50-3.svg]]

*(Figure after the board, in three steps.)* The case $m = n = 3$; the top row of the grid is the $X$-series and the right column the $Y$-series. (a) The horizontal edges: in each column, “$=$” (dashed) up to the changeover, then $S_i$. (b) The vertical edges: in each row, “$=$” up to the changeover, then $T_j$. (c) The changeover squares (shaded) coincide; they are crossing squares, one in each row and each column, like the $1$s of a permutation matrix. Each pipe comes down from $S_i$ and turns right to $T_{\sigma(i)}$; here $S_1 \cong T_2$, $S_2 \cong T_3$, $S_3 \cong T_1$, the matching drawn on the board. Where two pipes cross (a square of type (i)), nothing happens.

> [!proof]+ Proof of the Jordan–Hölder Theorem (Theorem [[§50 Composition Series and the Jordan–Hölder Theorem#^thm-50-1|§50.1]])
> *Idea:* each column and each row changes exactly once; the impossible squares force every column changeover to be a row changeover, so the changeovers form a permutation, and at each of them the crossing square gives $S_i \cong T_j$.
>
> *(WS 12.6; lecture 10/30.)*
>
> **Step 1: each column changes once.** Fix a column $i \in \{1, \ldots, m\}$. By Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-8|§50.8]](3) there is $j_0$ with $H_{ij}$ trivial for $j < j_0$ and $H_{ij} \cong S_i$ for $j \geq j_0$. Since $H_{i0} = \{e\}$ and $H_{in} = S_i \neq \{e\}$, we have $1 \leq j_0 \leq n$. Put $\tau(i) = j_0$. Then the square of column $i$ between rows $\tau(i) - 1$ and $\tau(i)$ has bottom edge “$=$” and top edge $S_i$, and it is the only square of the column with this property. This defines a map $\tau : \{1, \ldots, m\} \to \{1, \ldots, n\}$.
>
> **Step 2: each row changes once.** In the same way (the statement for the $V_{ij}$ in Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-8|§50.8]]), for each row $j \in \{1, \ldots, n\}$ there is exactly one $\rho(j) \in \{1, \ldots, m\}$ such that the square of row $j$ between columns $\rho(j) - 1$ and $\rho(j)$ has left edge “$=$” and right edge $T_j$.
>
> **Step 3: a column changeover is a row changeover.** Take the changeover square of column $i$ from Step 1: bottom “$=$”, top $S_i$. Among the nine kinds of square, those with this bottom and top are (a), (c) and the crossing square (v). By Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-9|§50.9]], (a) and (c) do not occur, so it is the crossing square: its left edge is “$=$” and its right edge is $T_{\tau(i)}$. It lies in row $\tau(i)$, between columns $i - 1$ and $i$, so by Step 2 it is the changeover square of row $\tau(i)$: $\rho(\tau(i)) = i$.
>
> **Step 4: a row changeover is a column changeover.** Symmetrically, the changeover square of row $j$ has left edge “$=$” and right edge $T_j$. The squares with these vertical edges are (b), (d) and (v), and (b), (d) do not occur. So it is the crossing square: bottom “$=$”, top $S_{\rho(j)}$, the changeover square of column $\rho(j)$. Hence $\tau(\rho(j)) = j$.
>
> **Step 5: $m = n$.** By Steps 3 and 4, $\tau$ and $\rho$ are inverse maps, so $\tau$ is a bijection from $\{1, \ldots, m\}$ to $\{1, \ldots, n\}$. Hence $m = n$, and $\sigma := \tau$ is a permutation in $S_n$.
>
> **Step 6: the isomorphisms.** For each $i$, the changeover square of column $i$ is a crossing square with top edge $S_i$ and right edge $T_{\sigma(i)}$. By Proposition [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-10|§50.10]], $S_i \cong T_{\sigma(i)}$.

^pf-50-1-2

*Uses:* [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-8|§50.8]], [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-9|§50.9]], [[§50 Composition Series and the Jordan–Hölder Theorem#^prop-50-10|§50.10]]

> [!remark] Remark: Peeling Off Atoms
> Read a composition series from the top: $G = G_N \trianglerighteq G_{N-1} \trianglerighteq \cdots \trianglerighteq G_0 = \{e\}$ peels off one simple quotient $G_N/G_{N-1}$ at a time, each step passing to a smaller normal subgroup. The theorem says that in whatever order the pieces are peeled off, the same atoms come off, with the same multiplicities. This is the lecture's justification for treating simple groups as the right objects to understand first.
>
> *Source: lecture 10/30*

^rem-50-8

> [!example] Example §50.2: Flags in $(\mathbb{Z}/p\mathbb{Z})^n$
> Let $G = (\mathbb{Z}/p\mathbb{Z})^n$, an $n$-dimensional vector space over $\mathbb{F}_p$, with standard basis $e_1, \ldots, e_n$. Every subgroup is normal ($G$ is abelian), and a chain of subspaces increasing one dimension at a time is a composition series, with every factor $\cong \mathbb{Z}/p\mathbb{Z}$. For a permutation $\sigma \in S_n$ take
>
> $$
> X_i = \langle e_1, \ldots, e_i \rangle, \qquad Y_j = \langle e_{\sigma(1)}, \ldots, e_{\sigma(j)} \rangle .
> $$
>
> Then $Y_j$ is spanned by the $e_k$ with $\sigma^{-1}(k) \leq j$, so $Z_{ij} = X_i \cap Y_j$ is spanned by the $e_k$ with $k \leq i$ and $\sigma^{-1}(k) \leq j$. Hence $H_{ij} = Z_{ij}/Z_{(i-1)j}$ is nontrivial exactly when $e_i \in Z_{ij}$, that is, when $j \geq \sigma^{-1}(i)$. The changeover of column $i$ is at row $\tau(i) = \sigma^{-1}(i)$: the pipes recover the permutation that defined the second flag (the lecture's “very nice exercise”; with these conventions it comes out as $\sigma^{-1}$). So in this group every matching of the factors occurs.
>
> *Source: lecture 10/30; the computation not from class*

^ex-50-2

![[m493-50-4.svg]]

*(Figure after the board's cube, with the grid added.)* The lecture's three-dimensional picture, $n = 3$ and $\sigma = (2\,3)$: the line $X_1 = Y_1 = \langle e_1 \rangle$ lies in two different planes, $X_2 = \langle e_1, e_2 \rangle$ and $Y_2 = \langle e_1, e_3 \rangle$. In the grid (right; $X$-series on the top row, $Y$-series on the right column) equalities appear inside the grid even though none occur along its edges: for instance $Z_{22} = X_2 \cap Y_2 = \langle e_1 \rangle = Z_{11}$. The column changeovers are at rows $\tau(1) = 1$, $\tau(2) = 3$, $\tau(3) = 2$, which is $\sigma^{-1} = (2\,3)$.
