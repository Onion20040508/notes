---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 52
tags: [group-theory, math493]
---
← [[§51 The Grid of Intersections]] · ↑ [[· 9 Commutators, Solvable Groups and the Sylow Theorems]] · [[§53 S₃, S₄, Aₙ and GLₙ]] →

*Source: Lecture and Worksheet 12 (Wed Oct 28, the statement); lecture (Fri Oct 30), which finished the proof (WS 12.6). The proof uses the grid of [[§51 The Grid of Intersections|§51]].*

> [!theorem] Theorem §52.1: Jordan–Hölder Theorem
> Let $G$ be any group, and let
>
> $$
> \{e\} = X_0 \trianglelefteq X_1 \trianglelefteq \cdots \trianglelefteq X_m = G \quad\text{and}\quad \{e\} = Y_0 \trianglelefteq Y_1 \trianglelefteq \cdots \trianglelefteq Y_n = G
> $$
>
> be two composition series, with quotients $S_i = X_i/X_{i-1}$ and $T_j = Y_j/Y_{j-1}$. Then $m = n$, and there is a permutation $\sigma \in S_n$ with $S_i \cong T_{\sigma(i)}$ for $1 \leq i \leq m$.
>
> *Source: lecture 10/28, 10/30; WS 12*

^thm-52-1

> [!proof]+ Proof
> *Idea:* each column and each row changes exactly once; the impossible squares force every column changeover to be a row changeover, so the changeovers form a permutation, and at each of them the crossing square gives $S_i \cong T_j$.
>
> *(WS 12.6; lecture 10/30.)*
>
> **Step 1: each column changes once.** Fix a column $i \in \{1, \ldots, m\}$. By Proposition [[§51 The Grid of Intersections#^prop-51-4|§51.4]](3) there is $j_0$ with $H_{ij}$ trivial for $j < j_0$ and $H_{ij} \cong S_i$ for $j \geq j_0$. Since $H_{i0} = \{e\}$ and $H_{in} = S_i \neq \{e\}$, we have $1 \leq j_0 \leq n$. Put $\tau(i) = j_0$. Then the square of column $i$ between rows $\tau(i) - 1$ and $\tau(i)$ has bottom edge “$=$” and top edge $S_i$, and it is the only square of the column with this property. This defines a map $\tau : \{1, \ldots, m\} \to \{1, \ldots, n\}$.
>
> **Step 2: each row changes once.** In the same way (the statement for the $V_{ij}$ in Proposition [[§51 The Grid of Intersections#^prop-51-4|§51.4]]), for each row $j \in \{1, \ldots, n\}$ there is exactly one $\rho(j) \in \{1, \ldots, m\}$ such that the square of row $j$ between columns $\rho(j) - 1$ and $\rho(j)$ has left edge “$=$” and right edge $T_j$.
>
> **Step 3: a column changeover is a row changeover.** Take the changeover square of column $i$ from Step 1: bottom “$=$”, top $S_i$. Among the nine kinds of square, those with this bottom and top are (a), (c) and the crossing square (v). By Proposition [[§51 The Grid of Intersections#^prop-51-5|§51.5]], (a) and (c) do not occur, so it is the crossing square: its left edge is “$=$” and its right edge is $T_{\tau(i)}$. It lies in row $\tau(i)$, between columns $i - 1$ and $i$, so by Step 2 it is the changeover square of row $\tau(i)$: $\rho(\tau(i)) = i$.
>
> **Step 4: a row changeover is a column changeover.** Symmetrically, the changeover square of row $j$ has left edge “$=$” and right edge $T_j$. The squares with these vertical edges are (b), (d) and (v), and (b), (d) do not occur. So it is the crossing square: bottom “$=$”, top $S_{\rho(j)}$, the changeover square of column $\rho(j)$. Hence $\tau(\rho(j)) = j$.
>
> **Step 5: $m = n$.** By Steps 3 and 4, $\tau$ and $\rho$ are inverse maps, so $\tau$ is a bijection from $\{1, \ldots, m\}$ to $\{1, \ldots, n\}$. Hence $m = n$, and $\sigma := \tau$ is a permutation in $S_n$.
>
> **Step 6: the isomorphisms.** For each $i$, the changeover square of column $i$ is a crossing square with top edge $S_i$ and right edge $T_{\sigma(i)}$. By Proposition [[§51 The Grid of Intersections#^prop-51-6|§51.6]], $S_i \cong T_{\sigma(i)}$.

^pf-52-1

*Uses:* [[§51 The Grid of Intersections#^prop-51-4|§51.4]], [[§51 The Grid of Intersections#^prop-51-5|§51.5]], [[§51 The Grid of Intersections#^prop-51-6|§51.6]]

> [!remark] Remark: Changeover Squares and Pipes
> By Proposition [[§51 The Grid of Intersections#^prop-51-4|§51.4]](3), the horizontal edges of column $i$ read, from the bottom up,
>
> $$
> =,\ \ldots,\ =,\ S_i,\ \ldots,\ S_i :
> $$
>
> the column starts with $H_{i0} = \{e\}$, ends with $H_{in} = S_i$ on the top row, and changes exactly once. The square where it changes is the **changeover square** of column $i$: its bottom edge is “$=$” and its top edge $S_i$. Likewise the vertical edges of row $j$ read $=, \ldots, =, T_j, \ldots, T_j$ from left to right, and row $j$ has one changeover square, with left edge “$=$” and right edge $T_j$. The impossible squares say that the changeover square of a column is the changeover square of a row, and conversely: the changeovers line up. The lecture records this with **pipes**. Along each column a pipe runs through its $S_i$ edges, from $S_i$ on the top row down to the changeover square; along each row a pipe runs through its $T_j$ edges, from $T_j$ on the right column back to the changeover square. The two meet in a crossing square, so each pipe joins one $S_i$ (top) to one $T_j$ (right), and carries a single simple group along its whole length. The figure below builds this in three steps; it is the proof above, as a picture.
>
> *Source: lecture 10/30; WS 12*

^rem-52-1

![[m493-50-3.svg]]

*(Figure after the board, in three steps.)* The case $m = n = 3$; the top row of the grid is the $X$-series and the right column the $Y$-series. (a) The horizontal edges: in each column, “$=$” (dashed) up to the changeover, then $S_i$. (b) The vertical edges: in each row, “$=$” up to the changeover, then $T_j$. (c) The changeover squares (shaded) coincide; they are crossing squares, one in each row and each column, like the $1$s of a permutation matrix. Each pipe comes down from $S_i$ and turns right to $T_{\sigma(i)}$; here $S_1 \cong T_2$, $S_2 \cong T_3$, $S_3 \cong T_1$, the matching drawn on the board. Where two pipes cross (a square of type (i)), nothing happens.

> [!remark] Remark: Peeling Off Atoms
> Read a composition series from the top: $G = G_N \trianglerighteq G_{N-1} \trianglerighteq \cdots \trianglerighteq G_0 = \{e\}$ peels off one simple quotient $G_N/G_{N-1}$ at a time, each step passing to a smaller normal subgroup. The theorem says that in whatever order the pieces are peeled off, the same atoms come off, with the same multiplicities. This is the lecture's justification for treating simple groups as the right objects to understand first.
>
> *Source: lecture 10/30*

^rem-52-2

> [!example] Example §52.1: The Order of the Factors Is Not Arbitrary
> A student asked whether every ordering of the composition factors is realized by some composition series. On 10/30 the lecture gave a group in which every ordering occurs, $(\mathbb{Z}/p\mathbb{Z})^n$ (Example [[§52 The Jordan–Hölder Theorem#^ex-52-2|§52.2]]). In general the answer is no (not from class). $S_3$ has the composition series $\{e\} \trianglelefteq A_3 \trianglelefteq S_3$, with factors $\mathbb{Z}/3, \mathbb{Z}/2$ in that order, and no composition series with the factors in the order $\mathbb{Z}/2, \mathbb{Z}/3$.
>
> *Source: question from class 10/28; the example $(\mathbb{Z}/p\mathbb{Z})^n$ lecture 10/30; $S_3$ not from class*

^ex-52-1

> [!proof]+ Proof
> *(Not from class.)* A composition series with first factor $\mathbb{Z}/2$ and second $\mathbb{Z}/3$ would be $\{e\} \trianglelefteq G_1 \trianglelefteq S_3$ with $|G_1| = 2$ and $G_1$ normal in $S_3$. But the subgroups of order $2$ of $S_3$ are the $\langle (i\,j) \rangle$, and none is normal: $(1\,3)(1\,2)(1\,3) = (2\,3)$.

^pf-ex-52-1

> [!example] Example §52.2: Flags in $(\mathbb{Z}/p\mathbb{Z})^n$
> Let $G = (\mathbb{Z}/p\mathbb{Z})^n$, an $n$-dimensional vector space over $\mathbb{F}_p$, with standard basis $e_1, \ldots, e_n$. Every subgroup is normal ($G$ is abelian), and a chain of subspaces increasing one dimension at a time is a composition series, with every factor $\cong \mathbb{Z}/p\mathbb{Z}$. For a permutation $\sigma \in S_n$ take
>
> $$
> X_i = \langle e_1, \ldots, e_i \rangle, \qquad Y_j = \langle e_{\sigma(1)}, \ldots, e_{\sigma(j)} \rangle .
> $$
>
> Then $Y_j$ is spanned by the $e_k$ with $\sigma^{-1}(k) \leq j$, so $Z_{ij} = X_i \cap Y_j$ is spanned by the $e_k$ with $k \leq i$ and $\sigma^{-1}(k) \leq j$. Hence $H_{ij} = Z_{ij}/Z_{(i-1)j}$ is nontrivial exactly when $e_i \in Z_{ij}$, that is, when $j \geq \sigma^{-1}(i)$. The changeover of column $i$ is at row $\tau(i) = \sigma^{-1}(i)$: the pipes recover the permutation that defined the second flag (the lecture's “very nice exercise”; with these conventions it comes out as $\sigma^{-1}$). So in this group every matching of the factors occurs.
>
> *Source: lecture 10/30; the computation not from class*

^ex-52-2

![[m493-50-4.svg]]

*(Figure after the board's cube, with the grid added.)* The lecture's three-dimensional picture, $n = 3$ and $\sigma = (2\,3)$: the line $X_1 = Y_1 = \langle e_1 \rangle$ lies in two different planes, $X_2 = \langle e_1, e_2 \rangle$ and $Y_2 = \langle e_1, e_3 \rangle$. In the grid (right; $X$-series on the top row, $Y$-series on the right column) equalities appear inside the grid even though none occur along its edges: for instance $Z_{22} = X_2 \cap Y_2 = \langle e_1 \rangle = Z_{11}$. The column changeovers are at rows $\tau(1) = 1$, $\tau(2) = 3$, $\tau(3) = 2$, which is $\sigma^{-1} = (2\,3)$.
