---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 51
tags: [group-theory, math493]
---
← [[§50 Composition Series]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§52 The Jordan–Hölder Theorem]] →

*Source: Worksheet 12, WS 12.1–12.3 (Wed Oct 28) and WS 12.4–12.5 (Fri Oct 30), with the lectures of both days. The approach is taken from Ravi Vakil's *Foundations of Algebraic Geometry* (WS 12). Everything here prepares the proof of the Jordan–Hölder theorem in [[§52 The Jordan–Hölder Theorem|§52]].*

Throughout this section, $G$ is a group with two composition series (Definition [[§50 Composition Series#^def-50-2|§50.2]])

$$
\{e\} = X_0 \trianglelefteq X_1 \trianglelefteq \cdots \trianglelefteq X_m = G \quad\text{and}\quad \{e\} = Y_0 \trianglelefteq Y_1 \trianglelefteq \cdots \trianglelefteq Y_n = G,
$$

with simple quotients $S_i = X_i/X_{i-1}$ and $T_j = Y_j/Y_{j-1}$.

> [!definition] Definition §51.1: The Grid $Z_{ij}$
> Put
>
> $$
> Z_{ij} = X_i \cap Y_j \qquad (0 \leq i \leq m,\ 0 \leq j \leq n),
> $$
>
> arranged in a rectangular grid as on the worksheet: $i$ increasing to the right (east) and $j$ increasing upwards (north), so $Z_{00}$ is the bottom left corner and $Z_{mn} = G$ the top right.
>
> *Source: WS 12; lecture 10/28*

^def-51-1

> [!theorem] Lemma §51.1: Intersections in the Grid
> $Z_{ab} \cap Z_{cd} = Z_{\min(a,c)\,\min(b,d)}$. In particular $Z_{i0} = Z_{0j} = \{e\}$, $Z_{in} = X_i$ and $Z_{mj} = Y_j$.
>
> *Source: WS 12; lecture 10/28*

^lem-51-1

> [!proof]+ Proof
> Both series increase, so $X_a \cap X_c = X_{\min(a,c)}$ and $Y_b \cap Y_d = Y_{\min(b,d)}$; hence $Z_{ab} \cap Z_{cd} = (X_a \cap X_c) \cap (Y_b \cap Y_d) = X_{\min(a,c)} \cap Y_{\min(b,d)}$. For the special cases, $X_i \cap \{e\} = \{e\} \cap Y_j = \{e\}$, $X_i \cap G = X_i$, $G \cap Y_j = Y_j$.

^pf-51-1

> [!theorem] Proposition §51.2: Normality in the Grid
> $Z_{(i-1)j} \trianglelefteq Z_{ij}$ and $Z_{i(j-1)} \trianglelefteq Z_{ij}$.
>
> *Source: WS 12.2*

^prop-51-2

> [!proof]+ Proof
> *Idea:* conjugating by $z \in X_i \cap Y_j$ preserves $X_{i-1}$ (normal in $X_i$) and $Y_j$ (a group containing $z$).
>
> *(Worksheet session 10/28.)* Let $z \in Z_{ij} = X_i \cap Y_j$ and $w \in Z_{(i-1)j} = X_{i-1} \cap Y_j$. Then $zwz^{-1} \in X_{i-1}$, because $X_{i-1} \trianglelefteq X_i$ and $z \in X_i$; and $zwz^{-1} \in Y_j$, because $z, w \in Y_j$. So $zwz^{-1} \in Z_{(i-1)j}$. The second statement is symmetric.

^pf-51-2

> [!definition] Definition §51.2: Edge Quotients $H_{ij}$ and $V_{ij}$
> For $i, j \geq 1$ (and $H_{i0}$, $V_{0j}$ likewise) define, using Proposition [[§51 The Grid of Intersections#^prop-51-2|§51.2]],
>
> $$
> H_{ij} = Z_{ij}/Z_{(i-1)j} \quad \text{(horizontal edges)}, \qquad V_{ij} = Z_{ij}/Z_{i(j-1)} \quad \text{(vertical edges)}.
> $$
>
> A trivial $H_{ij}$ or $V_{ij}$ means that the two groups at the ends of the edge are equal; the worksheet labels such an edge “$=$”.
>
> *Source: WS 12; lecture 10/28*

^def-51-2

![[m493-56-1.svg]]

*(Figure from WS 12, redrawn.)* The grid $Z_{ij} = X_i \cap Y_j$. Arrows are inclusions, each normal (Proposition [[§51 The Grid of Intersections#^prop-51-2|§51.2]]). The bottom row and left column are trivial; the top row is the $X$-series ($Z_{in} = X_i$) and the right column the $Y$-series ($Z_{mj} = Y_j$). Horizontal edges carry the quotients $H_{ij}$, vertical edges the $V_{ij}$.

> [!remark] Remark: The Strategy
> Every path through the grid from $Z_{00}$ to $Z_{mn}$, travelling one step east or north at a time, is a chain of subgroups. The essence of the proof is to show that every such path is a quasi-composition series, with the same simple quotients in each case. The two extreme paths give the $S_i$ and the $T_j$ (WS 12.1).
>
> *Source: WS 12*

^rem-51-1

> [!theorem] Proposition §51.3: The Two Edge Paths
> $(Z_{00}, Z_{10}, \ldots, Z_{m0}, Z_{m1}, \ldots, Z_{mn})$ and $(Z_{00}, Z_{01}, \ldots, Z_{0n}, Z_{1n}, \ldots, Z_{mn})$ are quasi-composition series. The quotients of the first are $m$ trivial groups followed by $T_1, \ldots, T_n$; those of the second are $n$ trivial groups followed by $S_1, \ldots, S_m$.
>
> *Source: WS 12.1*

^prop-51-3

> [!proof]+ Proof
> *Idea:* the bottom row and left column are trivial, the right column and top row are the two series.
>
> *(Worksheet session 10/28.)* By Lemma [[§51 The Grid of Intersections#^lem-51-1|§51.1]], $Z_{i0} = \{e\}$ and $Z_{mj} = Y_j$, so the first path is $\{e\}, \ldots, \{e\}$ ($m + 1$ times) followed by $Y_1, \ldots, Y_n$: its quotients are trivial $m$ times, then $Y_j/Y_{j-1} = T_j$, each simple. The second is symmetric, with $Z_{0j} = \{e\}$ and $Z_{in} = X_i$.

^pf-51-3

*Uses:* [[§51 The Grid of Intersections#^lem-51-1|§51.1]]

> [!theorem] Proposition §51.4: Horizontal Edges Propagate
> 1. The inclusion $Z_{i(j-1)} \hookrightarrow Z_{ij}$ induces a well-defined injection $H_{i(j-1)} \hookrightarrow H_{ij}$.
> 2. The image of $H_{i(j-1)}$ is normal in $H_{ij}$.
> 3. Each $H_{ij}$ is trivial or isomorphic to $S_i$. More precisely, in each column $i$ there is $j_0$ with $H_{ij}$ trivial for $j < j_0$ and $H_{ij} \cong S_i$ for $j \geq j_0$.
>
> Similarly, each $V_{ij}$ is trivial or isomorphic to $T_j$.
>
> *Source: WS 12.3; board 10/28*

^prop-51-4

> [!proof]+ Proof
> *Idea:* restricting $Z_{ij} \to H_{ij}$ to $Z_{i(j-1)}$ has kernel $Z_{(i-1)(j-1)}$; so the column $H_{i0} \hookrightarrow \cdots \hookrightarrow H_{in} = S_i$ is a chain of normal subgroups ending in a simple group.
>
> *(Board 10/28.)* **(1), (2).** Let $\pi: Z_{ij} \to H_{ij} = Z_{ij}/Z_{(i-1)j}$ be the projection, and restrict it to $Z_{i(j-1)}$. By Restricting a Homomorphism (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]]), the restriction has kernel
>
> $$
> Z_{(i-1)j} \cap Z_{i(j-1)} = Z_{(i-1)(j-1)}
> $$
>
> (Lemma [[§51 The Grid of Intersections#^lem-51-1|§51.1]]), so by the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]) $\pi$ induces an injective homomorphism
>
> $$
> H_{i(j-1)} = Z_{i(j-1)}/Z_{(i-1)(j-1)} \;\xrightarrow{\ \sim\ }\; \pi(Z_{i(j-1)}) \;\subseteq\; H_{ij}, \qquad x Z_{(i-1)(j-1)} \mapsto x Z_{(i-1)j}.
> $$
>
> Since $Z_{i(j-1)} \trianglelefteq Z_{ij}$ (Proposition [[§51 The Grid of Intersections#^prop-51-2|§51.2]]) and $\pi$ is surjective, the image $\pi(Z_{i(j-1)})$ is normal in $H_{ij}$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], WS 6.6(3)).
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

^pf-51-4

*Uses:* [[§41 The First and Second Isomorphism Theorems#^lem-41-4|§41.4]], [[§51 The Grid of Intersections#^lem-51-1|§51.1]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§51 The Grid of Intersections#^prop-51-2|§51.2]], [[§39 Sources of Normal Subgroups#^prop-39-4|§39.4]], [[§48 Solvable Groups#^prop-48-4|§48.4]]

> [!remark] Remark: The Possible Squares
> Consider one square of the grid. To keep the subscripts out of the way, the lecture names its corners
>
> $$
> A = Z_{(i-1)(j-1)}, \qquad B = Z_{i(j-1)}, \qquad C = Z_{(i-1)j}, \qquad D = Z_{ij},
> $$
>
> so that $A \trianglelefteq B \trianglelefteq D$ and $A \trianglelefteq C \trianglelefteq D$ (Proposition [[§51 The Grid of Intersections#^prop-51-2|§51.2]]). In the grid, as on the board, $A$ is the bottom left corner, $B$ the bottom right, $C$ the top left and $D$ the top right. The four edges carry:
> - bottom $B/A = H_{i(j-1)}$ and top $D/C = H_{ij}$: each is “$=$” or $S_i$;
> - left $C/A = V_{(i-1)j}$ and right $D/B = V_{ij}$: each is “$=$” or $T_j$.
>
> By Proposition [[§51 The Grid of Intersections#^prop-51-4|§51.4]], a nontrivial bottom edge forces a nontrivial top edge, and a nontrivial left edge forces a nontrivial right edge. So (bottom, top) is $(=, =)$, $(=, S_i)$ or $(S_i, S_i)$, and (left, right) is $(=, =)$, $(=, T_j)$ or $(T_j, T_j)$: before any thinking, there are $3 \times 3 = 9$ kinds of square, drawn below.
>
> *Source: WS 12.4–12.5; lecture 10/30*

^rem-51-2

![[m493-50-1.svg]]

*(Figure after the lecture; pipes added.)* The nine kinds of square; the corners $A, B, C, D$ are as in the key. A dashed edge marked $=$ is a trivial quotient: its two corners are equal. $S$ stands for $S_i$ on the horizontal edges and $T$ for $T_j$ on the vertical ones. In the four impossible squares (a)–(d), exactly one of the two directions changes from trivial to nontrivial across the square (Proposition [[§51 The Grid of Intersections#^prop-51-5|§51.5]]). In the allowed squares (i)–(v), the coloured lines are the pipes of the remark *Changeover Squares and Pipes* below: a pipe runs through each pair of nontrivial opposite edges, and in the crossing square (v) it turns the corner, from $S$ on the top to $T$ on the right, where $S \cong T$ (Proposition [[§51 The Grid of Intersections#^prop-51-6|§51.6]]).

> [!theorem] Proposition §51.5: Four Impossible Squares
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

^prop-51-5

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

^pf-51-5

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

^rem-51-3

> [!theorem] Proposition §51.6: The Crossing Square
> Suppose a square has bottom and left edges trivial ($B = A$ and $C = A$), top edge $D/C \cong S_i$ and right edge $D/B \cong T_j$: the crossing square (v). Then $S_i \cong T_j$. (Worksheet hint: think about $Z_{ij}/Z_{(i-1)(j-1)}$.)
>
> *Source: WS 12.5; lecture 10/30*

^prop-51-6

> [!proof]+ Proof
> *Idea:* the two trivial edges say that $A$, $B$ and $C$ are one subgroup, so the two nontrivial edges are literally the same quotient.
>
> *(Board 10/30.)* Since $B = A$ and $C = A$, the three corners $A$, $B$, $C$ are the same subgroup of $D$. So the right edge $D/B$ and the top edge $D/C$ are the same group of cosets, and
>
> $$
> T_j \cong D/B = D/C \cong S_i.
> $$

^pf-51-6
