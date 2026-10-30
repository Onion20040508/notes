---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 50
tags: [group-theory, math493]
---
← [[§49 The Derived Series]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§51 The Grid of Intersections]] →

*Source: Lecture and Worksheet 12 (Wed Oct 28). Taught after the Sylow theorems and semidirect products, and placed here because a composition series is a subnormal series, like the chains that define solvable groups ([[§48 Solvable Groups|§48]]) and the derived series ([[§49 The Derived Series|§49]]). Reference: not covered in the Pinter chapters used so far.*

The course has used the analogy that simple groups are atoms and other groups are molecules built from them. For the analogy to be good, every group should have a well-defined “chemical formula”: a list of simple pieces that does not depend on how the group is taken apart. The Jordan–Hölder theorem says exactly this, for every group that can be taken apart into simple pieces at all, in particular every finite group. This section sets up composition series; [[§51 The Grid of Intersections|§51]] builds the grid of intersections that the proof uses, and [[§52 The Jordan–Hölder Theorem|§52]] states and proves the theorem.

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
> A subnormal series $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ (Definition [[§50 Composition Series#^def-50-1|§50.1]]) is a **composition series** if every quotient $G_j/G_{j-1}$ is simple (Definition [[§43 Simple Groups#^def-43-1|§43.1]]). One then thinks of $G$ as made from $G_1/G_0, G_2/G_1, \ldots, G_N/G_{N-1}$, its **composition factors**.
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
> *(Not from class.)* The chain in the definition of a solvable group (Definition [[§48 Solvable Groups#^def-48-1|§48.1]]) is a subnormal series whose quotients are abelian; a composition series is one whose quotients are simple. Since the abelian simple groups are exactly the $\mathbb{Z}/p\mathbb{Z}$ (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]), a composition series all of whose factors are cyclic of prime order shows that $G$ is solvable. Conversely, a finite solvable group has such a composition series: refine each abelian quotient $G_j/G_{j-1}$ by a composition series of it (Lemma [[§50 Composition Series#^lem-50-2|§50.2]]) and pull back, as in the proof of that lemma. Combined with the Jordan–Hölder theorem: *a finite group is solvable if and only if all of its composition factors are cyclic of prime order.* For example, $\{e\} \trianglelefteq \langle (1\,2)(3\,4) \rangle \trianglelefteq K \trianglelefteq A_4 \trianglelefteq S_4$, with $K$ the Klein four-group, has factors $\mathbb{Z}/2, \mathbb{Z}/2, \mathbb{Z}/3, \mathbb{Z}/2$, while $A_5$ has the single factor $A_5$.

^rem-50-2

> [!theorem] Proposition §50.1: $\mathbb{Z}$ Has No Composition Series
> Not every group has a composition series: $\mathbb{Z}$ has none.
>
> *Source: lecture 10/28*

^prop-50-1

> [!proof]+ Proof
> *Idea:* the factors of a composition series of an abelian group are finite, so the group would be finite.
>
> *(Lecture 10/28, answering a student's question.)* Suppose $\{0\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = \mathbb{Z}$ were a composition series. Every quotient $G_j/G_{j-1}$ is a quotient of a subgroup of an abelian group, hence abelian, and simple, hence $\cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$ (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]). Then $|G_j| = |G_{j-1}| \cdot |G_j/G_{j-1}|$ (Lagrange, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]) shows by induction that every $G_j$ is finite, including $G_N = \mathbb{Z}$, a contradiction.

^pf-50-1

*Uses:* [[§43 Simple Groups#^thm-43-1|§43.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!theorem] Lemma §50.2: Finite Groups Have Composition Series
> Every finite group $G$ has a composition series.
>
> *Source: lecture 10/28*

^lem-50-2

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

^pf-50-2

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|§42.5]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]]

![[m493-56-3.svg]]

*(Not from lecture; figure added, after the lecture's image.)* The proof of Lemma [[§50 Composition Series#^lem-50-2|§50.2]]: the normal subgroup $N$ is the island in the stream from $\{e\}$ to $G$. A composition series of $N$ reaches the island, and the preimages $\pi^{-1}(Q_j)$ of a composition series of $G/N$ carry the bridge on to $G$; each new quotient is $\cong Q_j/Q_{j-1}$.

> [!theorem] Lemma §50.3: Two Normal Subgroups with Simple Quotients
> Let $G$ be a finite group and $N_1 \neq N_2$ normal subgroups such that $G/N_1$ and $G/N_2$ are both simple. Then:
>
> 1. $N_1 N_2 = G$;
> 2. $G/N_1 \cong N_2/(N_1 \cap N_2)$ and $G/N_2 \cong N_1/(N_1 \cap N_2)$.
>
> *Source: PS 7.4; “I expect to use this lemma in Friday's class”*

^lem-50-3

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

^pf-50-3

> [!remark] Remark: The Quotient by $N_1 \cap N_2$
> Speyer, on Problem 7.4: in this situation one can further show that $G/(N_1 \cap N_2) \cong N_1/(N_1 \cap N_2) \times N_2/(N_1 \cap N_2)$. *(Proof not from class.)* In $\bar G = G/(N_1 \cap N_2)$, the images $\bar N_i = N_i/(N_1 \cap N_2)$ are normal, they intersect trivially, since $\bar N_1 \cap \bar N_2 = (N_1 \cap N_2)/(N_1 \cap N_2)$, and $\bar N_1 \bar N_2 = \bar G$ because $N_1 N_2 = G$. So $\bar G \cong \bar N_1 \times \bar N_2$ by Internal Direct Products Are Direct Products (Theorem [[§57 Internal and External Direct Products#^thm-57-1|§57.1]], in Chapter 10).

^rem-50-3
