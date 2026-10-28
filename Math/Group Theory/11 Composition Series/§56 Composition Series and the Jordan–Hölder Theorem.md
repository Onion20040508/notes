---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 56
tags: [group-theory, math493]
---
← [[§55 Semidirect Products]] · ↑ [[· 11 Composition Series]]

*Reference: not covered in the Pinter chapters used so far.*

> [!definition] Definition §56.1: Subnormal Series
> Let $G$ be any group. A **subnormal series** of $G$ is a chain of subgroups
>
> $$
> \{e\} = G_0 \trianglelefteq G_1 \trianglelefteq G_2 \trianglelefteq \cdots \trianglelefteq G_N = G
> $$
>
> in which each $G_{j-1}$ is normal in the next term $G_j$ (not necessarily in $G$). The groups $G_j/G_{j-1}$ are its **quotients** (or subquotients).
>
> *Source: lecture 10/28; WS 12*

^def-56-1

> [!definition] Definition §56.2: Composition Series
> A subnormal series $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = G$ (Definition [[§56 Composition Series and the Jordan–Hölder Theorem#^def-56-1|§56.1]]) is a **composition series** if every quotient $G_j/G_{j-1}$ is simple (Definition [[§43 Simple Groups#^def-43-1|§43.1]]). One then thinks of $G$ as made from $G_1/G_0, G_2/G_1, \ldots, G_N/G_{N-1}$, its **composition factors**.
>
> *Source: lecture 10/28; WS 12*

^def-56-2

> [!definition] Definition §56.3: Quasi-Composition Series
> A subnormal series is a **quasi-composition series** if every quotient $G_j/G_{j-1}$ is simple or trivial.
>
> *Source: lecture 10/28; WS 12*

^def-56-3

> [!remark] Remark: Quasi-Composition Series
> The term is the lecturer's own and is not standard. (WS 12 says “a composition series where \ldots”; a subnormal series is meant.) A trivial quotient $G_j/G_{j-1}$ just means $G_{j-1} = G_j$, a repeated term. Deleting the repeated terms turns a quasi-composition series into a composition series with the same simple quotients. Quasi-composition series are convenient in the proof below, where trivial quotients arise naturally.
>
> *Source: lecture 10/28*

^rem-56-1

> [!remark] Remark: Relation to Solvable Groups
> *(Not from class.)* The chain in the definition of a solvable group (Definition [[§48 Solvable Groups#^def-48-1|§48.1]]) is a subnormal series whose quotients are abelian; a composition series is one whose quotients are simple. Since the abelian simple groups are exactly the $\mathbb{Z}/p\mathbb{Z}$ (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]), a composition series all of whose factors are cyclic of prime order shows that $G$ is solvable. Conversely, a finite solvable group has such a composition series: refine each abelian quotient $G_j/G_{j-1}$ by a composition series of it (Lemma [[§56 Composition Series and the Jordan–Hölder Theorem#^lem-56-3|§56.3]]) and pull back, as in the proof of that lemma. Combined with the Jordan–Hölder theorem: *a finite group is solvable if and only if all of its composition factors are cyclic of prime order.* For example, $\{e\} \trianglelefteq \langle (1\,2)(3\,4) \rangle \trianglelefteq K \trianglelefteq A_4 \trianglelefteq S_4$, with $K$ the Klein four-group, has factors $\mathbb{Z}/2, \mathbb{Z}/2, \mathbb{Z}/3, \mathbb{Z}/2$, while $A_5$ has the single factor $A_5$.

^rem-56-2

> [!theorem] Theorem §56.1: Jordan–Hölder Theorem
> Let $G$ be any group, and let
>
> $$
> \{e\} = X_0 \trianglelefteq X_1 \trianglelefteq \cdots \trianglelefteq X_m = G \quad\text{and}\quad \{e\} = Y_0 \trianglelefteq Y_1 \trianglelefteq \cdots \trianglelefteq Y_n = G
> $$
>
> be two composition series, with quotients $S_i = X_i/X_{i-1}$ and $T_j = Y_j/Y_{j-1}$. Then $m = n$, and there is a permutation $\sigma \in S_n$ with $S_i \cong T_{\sigma(i)}$ for $1 \leq i \leq m$.
>
> *Source: lecture 10/28; WS 12*

^thm-56-1

> [!proof]+ Proof (to be filled)
> The proof occupies [[§56 Composition Series and the Jordan–Hölder Theorem|§56]]: the steps through WS 12.3 were done on 10/28, and WS 12.4–12.6 are to be finished on Fri Oct 30. The lecture's comment: the theorem justifies the program of studying groups through simple groups.

^pf-56-1

> [!theorem] Proposition §56.2: $\mathbb{Z}$ Has No Composition Series
> Not every group has a composition series: $\mathbb{Z}$ has none.
>
> *Source: lecture 10/28*

^prop-56-2

> [!proof]+ Proof
> *Idea:* the factors of a composition series of an abelian group are finite, so the group would be finite.
>
> *(Lecture 10/28, answering a student's question.)* Suppose $\{0\} = G_0 \trianglelefteq \cdots \trianglelefteq G_N = \mathbb{Z}$ were a composition series. Every quotient $G_j/G_{j-1}$ is a quotient of a subgroup of an abelian group, hence abelian, and simple, hence $\cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$ (Theorem [[§43 Simple Groups#^thm-43-1|§43.1]]). Then $|G_j| = |G_{j-1}| \cdot |G_j/G_{j-1}|$ (Lagrange, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]) shows by induction that every $G_j$ is finite, including $G_N = \mathbb{Z}$, a contradiction.

^pf-56-2

*Uses:* [[§43 Simple Groups#^thm-43-1|§43.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]

> [!theorem] Lemma §56.3: Finite Groups Have Composition Series
> Every finite group $G$ has a composition series.
>
> *Source: lecture 10/28*

^lem-56-3

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

^pf-56-3

*Uses:* [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-5|§42.5]], [[§42 The Correspondence and Third Isomorphism Theorems#^thm-42-3|§42.3]]

![[m493-56-3.svg]]

*(Not from lecture; figure added, after the lecture's image.)* The proof of Lemma [[§56 Composition Series and the Jordan–Hölder Theorem#^lem-56-3|§56.3]]: the normal subgroup $N$ is the island in the stream from $\{e\}$ to $G$. A composition series of $N$ reaches the island, and the preimages $\pi^{-1}(Q_j)$ of a composition series of $G/N$ carry the bridge on to $G$; each new quotient is $\cong Q_j/Q_{j-1}$.

> [!example] Example §56.1: The Order of the Factors Is Not Arbitrary
> A student asked whether every ordering of the composition factors is realized by some composition series. The question was left open in class; the answer is no. $S_3$ has the composition series $\{e\} \trianglelefteq A_3 \trianglelefteq S_3$, with factors $\mathbb{Z}/3, \mathbb{Z}/2$ in that order, and no composition series with the factors in the order $\mathbb{Z}/2, \mathbb{Z}/3$.
>
> *Source: question from class 10/28; answer not from class*

^ex-56-1

> [!proof]+ Proof
> *(Not from class.)* A composition series with first factor $\mathbb{Z}/2$ and second $\mathbb{Z}/3$ would be $\{e\} \trianglelefteq G_1 \trianglelefteq S_3$ with $|G_1| = 2$ and $G_1$ normal in $S_3$. But the subgroups of order $2$ of $S_3$ are the $\langle (i\,j) \rangle$, and none is normal: $(1\,3)(1\,2)(1\,3) = (2\,3)$.

^pf-ex-56-1

## The Grid of Intersections

*The approach is taken from Ravi Vakil's *Foundations of Algebraic Geometry* (WS 12). Throughout, the two composition series are those of the Jordan–Hölder theorem (Theorem [[§56 Composition Series and the Jordan–Hölder Theorem#^thm-56-1|§56.1]]).*

> [!definition] Definition §56.4: The Grid $Z_{ij}$
> Put
>
> $$
> Z_{ij} = X_i \cap Y_j \qquad (0 \leq i \leq m,\ 0 \leq j \leq n),
> $$
>
> arranged in a rectangular grid as on the worksheet: $i$ increasing to the right (east) and $j$ increasing upwards (north), so $Z_{00}$ is the bottom left corner and $Z_{mn} = G$ the top right.
>
> *Source: WS 12; lecture 10/28*

^def-56-4

> [!theorem] Lemma §56.4: Intersections in the Grid
> $Z_{ab} \cap Z_{cd} = Z_{\min(a,c)\,\min(b,d)}$. In particular $Z_{i0} = Z_{0j} = \{e\}$, $Z_{in} = X_i$ and $Z_{mj} = Y_j$.
>
> *Source: WS 12; lecture 10/28*

^lem-56-4

> [!proof]+ Proof
> Both series increase, so $X_a \cap X_c = X_{\min(a,c)}$ and $Y_b \cap Y_d = Y_{\min(b,d)}$; hence $Z_{ab} \cap Z_{cd} = (X_a \cap X_c) \cap (Y_b \cap Y_d) = X_{\min(a,c)} \cap Y_{\min(b,d)}$. For the special cases, $X_i \cap \{e\} = \{e\} \cap Y_j = \{e\}$, $X_i \cap G = X_i$, $G \cap Y_j = Y_j$.

^pf-56-4

> [!theorem] Proposition §56.5: Normality in the Grid
> $Z_{(i-1)j} \trianglelefteq Z_{ij}$ and $Z_{i(j-1)} \trianglelefteq Z_{ij}$.
>
> *Source: WS 12.2*

^prop-56-5

> [!proof]+ Proof
> *Idea:* conjugating by $z \in X_i \cap Y_j$ preserves $X_{i-1}$ (normal in $X_i$) and $Y_j$ (a group containing $z$).
>
> *(Worksheet session 10/28.)* Let $z \in Z_{ij} = X_i \cap Y_j$ and $w \in Z_{(i-1)j} = X_{i-1} \cap Y_j$. Then $zwz^{-1} \in X_{i-1}$, because $X_{i-1} \trianglelefteq X_i$ and $z \in X_i$; and $zwz^{-1} \in Y_j$, because $z, w \in Y_j$. So $zwz^{-1} \in Z_{(i-1)j}$. The second statement is symmetric.

^pf-56-5

> [!definition] Definition §56.5: Edge Quotients $H_{ij}$ and $V_{ij}$
> For $i, j \geq 1$ (and $H_{i0}$, $V_{0j}$ likewise) define, using Proposition [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-5|§56.5]],
>
> $$
> H_{ij} = Z_{ij}/Z_{(i-1)j} \quad \text{(horizontal edges)}, \qquad V_{ij} = Z_{ij}/Z_{i(j-1)} \quad \text{(vertical edges)}.
> $$
>
> A trivial $H_{ij}$ or $V_{ij}$ means that the two groups at the ends of the edge are equal; the worksheet labels such an edge “$=$”.
>
> *Source: WS 12; lecture 10/28*

^def-56-5

![[m493-56-1.svg]]

*(Figure from WS 12, redrawn.)* The grid $Z_{ij} = X_i \cap Y_j$. Arrows are inclusions, each normal (Proposition [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-5|§56.5]]). The bottom row and left column are trivial; the top row is the $X$-series ($Z_{in} = X_i$) and the right column the $Y$-series ($Z_{mj} = Y_j$). Horizontal edges carry the quotients $H_{ij}$, vertical edges the $V_{ij}$.

> [!remark] Remark: The Strategy
> Every path through the grid from $Z_{00}$ to $Z_{mn}$, travelling one step east or north at a time, is a chain of subgroups. The essence of the proof is to show that every such path is a quasi-composition series, with the same simple quotients in each case. The two extreme paths give the $S_i$ and the $T_j$ (WS 12.1).
>
> *Source: WS 12*

^rem-56-3

> [!theorem] Proposition §56.6: The Two Edge Paths
> $(Z_{00}, Z_{10}, \ldots, Z_{m0}, Z_{m1}, \ldots, Z_{mn})$ and $(Z_{00}, Z_{01}, \ldots, Z_{0n}, Z_{1n}, \ldots, Z_{mn})$ are quasi-composition series. The quotients of the first are $m$ trivial groups followed by $T_1, \ldots, T_n$; those of the second are $n$ trivial groups followed by $S_1, \ldots, S_m$.
>
> *Source: WS 12.1*

^prop-56-6

> [!proof]+ Proof
> *Idea:* the bottom row and left column are trivial, the right column and top row are the two series.
>
> *(Worksheet session 10/28.)* By Lemma [[§56 Composition Series and the Jordan–Hölder Theorem#^lem-56-4|§56.4]], $Z_{i0} = \{e\}$ and $Z_{mj} = Y_j$, so the first path is $\{e\}, \ldots, \{e\}$ ($m + 1$ times) followed by $Y_1, \ldots, Y_n$: its quotients are trivial $m$ times, then $Y_j/Y_{j-1} = T_j$, each simple. The second is symmetric, with $Z_{0j} = \{e\}$ and $Z_{in} = X_i$.

^pf-56-6

*Uses:* [[§56 Composition Series and the Jordan–Hölder Theorem#^lem-56-4|§56.4]]

> [!theorem] Proposition §56.7: Horizontal Edges Propagate
> 1. The inclusion $Z_{i(j-1)} \hookrightarrow Z_{ij}$ induces a well-defined injection $H_{i(j-1)} \hookrightarrow H_{ij}$.
> 2. The image of $H_{i(j-1)}$ is normal in $H_{ij}$.
> 3. Each $H_{ij}$ is trivial or isomorphic to $S_i$. More precisely, in each column $i$ there is $j_0$ with $H_{ij}$ trivial for $j < j_0$ and $H_{ij} \cong S_i$ for $j \geq j_0$.
>
> Similarly, each $V_{ij}$ is trivial or isomorphic to $T_j$.
>
> *Source: WS 12.3; board 10/28*

^prop-56-7

> [!proof]+ Proof
> *Idea:* restricting $Z_{ij} \to H_{ij}$ to $Z_{i(j-1)}$ has kernel $Z_{(i-1)(j-1)}$; so the column $H_{i0} \hookrightarrow \cdots \hookrightarrow H_{in} = S_i$ is a chain of normal subgroups ending in a simple group.
>
> *(Board 10/28.)* **(1), (2).** Let $\pi: Z_{ij} \to H_{ij} = Z_{ij}/Z_{(i-1)j}$ be the projection, and restrict it to $Z_{i(j-1)}$. By Restricting a Homomorphism (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]), the restriction has kernel
>
> $$
> Z_{(i-1)j} \cap Z_{i(j-1)} = Z_{(i-1)(j-1)}
> $$
>
> (Lemma [[§56 Composition Series and the Jordan–Hölder Theorem#^lem-56-4|§56.4]]), so by the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]) $\pi$ induces an injective homomorphism
>
> $$
> H_{i(j-1)} = Z_{i(j-1)}/Z_{(i-1)(j-1)} \;\xrightarrow{\ \sim\ }\; \pi(Z_{i(j-1)}) \;\subseteq\; H_{ij}, \qquad x Z_{(i-1)(j-1)} \mapsto x Z_{(i-1)j}.
> $$
>
> Since $Z_{i(j-1)} \trianglelefteq Z_{ij}$ (Proposition [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-5|§56.5]]) and $\pi$ is surjective, the image $\pi(Z_{i(j-1)})$ is normal in $H_{ij}$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], WS 6.6(3)).
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

^pf-56-7

*Uses:* [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]], [[§56 Composition Series and the Jordan–Hölder Theorem#^lem-56-4|§56.4]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-5|§56.5]], [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], [[§48 Solvable Groups#^prop-48-4|§48.4]]

> [!remark] Remark: The Possible Squares
> Consider one square of the grid, with corners $Z_{(i-1)(j-1)}$ (bottom left), $Z_{i(j-1)}$ (bottom right), $Z_{(i-1)j}$ (top left), $Z_{ij}$ (top right). Its bottom and top edges carry $H_{i(j-1)}$ and $H_{ij}$, its left and right edges $V_{(i-1)j}$ and $V_{ij}$. By Proposition [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-7|§56.7]], each edge is “$=$” (trivial) or carries $S_i$ (horizontal) or $T_j$ (vertical), and a nontrivial bottom edge forces a nontrivial top edge, a nontrivial left edge a nontrivial right edge. This leaves $3 \times 3 = 9$ kinds of square.
>
> *Source: WS 12.4–12.5*

^rem-56-4

> [!theorem] Proposition §56.8: Four Impossible Squares
> The following squares do not occur (top, bottom; left, right):
>
> 1. $S_i$, $=$;  $T_j$, $T_j$;
> 2. $S_i$, $S_i$;  $=$, $T_j$;
> 3. $S_i$, $=$;  $=$, $=$;
> 4. $=$, $=$;  $=$, $T_j$.
>
> Hint: think about $Z_{ij}/Z_{(i-1)(j-1)}$.
>
> *Source: WS 12.4*

^prop-56-8

> [!proof]+ Proof (to be filled)
> WS 12.4, to be done Fri Oct 30.

^pf-56-8

> [!theorem] Proposition §56.9: The Crossing Square
> If a square has top $S_i$, bottom $=$, left $=$, right $T_j$, then $S_i \cong T_j$. Hint: think about $Z_{ij}/Z_{(i-1)(j-1)}$.
>
> *Source: WS 12.5*

^prop-56-9

> [!proof]+ Proof (to be filled)
> WS 12.5, to be done Fri Oct 30.

^pf-56-9

> [!remark] Remark: Pipes
> So only five squares remain: both pairs nontrivial; only the left and right edges nontrivial; only the top and bottom edges nontrivial; all four edges trivial; and the crossing square of WS 12.5. Draw a “pipe” through each nontrivial pair of opposite edges, and in the crossing square a pipe entering through the top edge and leaving through the right edge. Each pipe then carries a single simple group from the top row ($S_i$) to the right column ($T_j$), which is how the permutation $\sigma$ arises. WS 12.6 asks to turn this into a proof of the Jordan–Hölder theorem; it is to be finished on Fri Oct 30.
>
> *Source: WS 12*

^rem-56-5

![[m493-56-2.svg]]

*(Not from lecture; figure added, after WS 12.)* The five squares left by Propositions [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-8|§56.8]] and [[§56 Composition Series and the Jordan–Hölder Theorem#^prop-56-9|§56.9]], with their pipes. A pipe through the top and bottom edges carries $S_i$ (blue), one through the left and right edges carries $T_j$ (red); in the crossing square the pipe turns, from $S_i$ on the top to $T_j \cong S_i$ on the right.
