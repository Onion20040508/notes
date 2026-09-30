---
type: section
subject: "[[Group Theory]]"
chapter: 3
section: 13
tags: [group-theory, math493]
---
← [[Group Theory §12 Multiplying and Conjugating Cycles]] · ↑ [[Group Theory — 3 Permutations]] · [[Group Theory §14 Multiplication Tables]] →

*Reference: Pinter Ch. 5, Ch. 7.*

Recall from The Group $S_3$ in Detail ([[Group Theory §10 Cycle Notation and the Group S₃#^ex-10-1|Ex. §10.1]]): the six elements are the identity $e$; the three transpositions $(1\ 2), (1\ 3), (2\ 3)$ (each of which squares to $e$); and the two $3$-cycles $(1\ 2\ 3), (1\ 3\ 2)$, which are inverse to each other, with $(1\ 2\ 3)^2 = (1\ 3\ 2)$ and $(1\ 2\ 3)^3 = e$ (all visible in the multiplication table).

> [!theorem] Proposition §13.1: Subgroups of $S_3$
> $S_3$ has exactly six subgroups:
>
> $$ \{e\}, \qquad \langle (1\,2) \rangle, \quad \langle (1\,3) \rangle, \quad \langle (2\,3) \rangle, \qquad \langle (1\,2\,3) \rangle = \{e, (1\,2\,3), (1\,3\,2)\}, \qquad S_3, $$
>
> of orders $1, 2, 2, 2, 3, 6$ respectively.
>
> *Source: WS 1.7*

^prop-13-1

> [!proof]+ Proof
> Each listed set is a subgroup: $\{e\}$ and $S_3$ trivially, and the others by [[Group Theory §4 Subgroups#^prop-4-5|WS 1.5]] (each is $\langle g \rangle$ for some $g$; e.g. $\langle (1\,2) \rangle = \{e, (1\,2)\}$ since $(1\,2)^2 = e$).
>
> Conversely, let $H \leq S_3$ with $H \neq \{e\}$; we show $H$ is on the list.
>
> **Step 1: the product of two distinct transpositions is a 3-cycle.** Two distinct transpositions in $S_3$ share exactly one letter: write them as $(x\ y)$ and $(x\ z)$ with $\{x, y, z\} = \{1, 2, 3\}$. Compute $(x\,y)(x\,z)$ (right factor first): $x \to z \to z$, so $x \mapsto z$; $z \to x \to y$, so $z \mapsto y$; $y \to y \to x$, so $y \mapsto x$. Thus $(x\,y)(x\,z) = (x\ z\ y)$, a 3-cycle.
>
> **Step 2: if $H$ contains no 3-cycle, then $H = \langle \tau \rangle$ for a single transposition $\tau$.** All nonidentity elements of $H$ are transpositions. If $H$ contained two distinct transpositions, Step 1 would put a 3-cycle in $H$ (closure) — contradiction. So $H$ contains exactly one transposition $\tau$, and $H = \{e, \tau\} = \langle \tau \rangle$.
>
> **Step 3: if $H$ contains a 3-cycle $\sigma$ but no transposition, then $H = \langle \sigma \rangle$.** Since $\sigma^2 = \sigma^{-1} \in H$, we get $\{e, \sigma, \sigma^2\} = \langle (1\,2\,3) \rangle \subseteq H$ (both 3-cycles are powers of either one). There is nothing else available: the remaining elements of $S_3$ are transpositions, which $H$ excludes. So $H = \langle (1\,2\,3) \rangle$.
>
> **Step 4: if $H$ contains a 3-cycle $\sigma$ and a transposition $\tau$, then $H = S_3$.** By Step 3's argument, $e, \sigma, \sigma^2 \in H$, and by closure $\tau, \tau\sigma, \tau\sigma^2 \in H$. These six elements are pairwise distinct: $\sigma^i = \sigma^j$ forces $i = j$ (for $i, j \in \{0,1,2\}$); $\tau\sigma^i = \tau\sigma^j$ forces $\sigma^i = \sigma^j$ by cancellation ([[Group Theory §2 First Consequences of the Axioms#^prop-2-1|WS 1.1]]); and $\tau\sigma^i = \sigma^j$ would give $\tau = \sigma^{j-i}$, impossible since $\tau$ is a transposition (fixes one letter) while every power of $\sigma$ is the identity or a 3-cycle (fixes three letters or none). So $|H| \geq 6 = |S_3|$, hence $H = S_3$.

^pf-13-1

*Uses:* [[Group Theory §4 Subgroups#^def-4-1|Def. §4.1]], [[Group Theory §4 Subgroups#^prop-4-5|§4.5]], [[Group Theory §4 Subgroups#^lem-4-4|§4.4]], [[Group Theory §2 First Consequences of the Axioms#^prop-2-1|§2.1]], [[Group Theory §10 Cycle Notation and the Group S₃#^ex-10-1|Ex. §10.1]], [[Group Theory §11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]]

![[m493-13-1.svg]]
*The subgroup lattice of $S_3$, arranged by order; lines denote inclusion. Shaded: the normal subgroups ([[Group Theory §35 Normal Subgroups#^def-35-1|§35]]).*

> [!remark]- Connections
> - The worksheet summary alongside $\mathbb{Z}$, $\mathbb{Z}^2$, $\mathbb{R}$, $GL_n$: [[Group Theory §5 A Zoo of Subgroups#^rem-5-3|Summary of WS 1.7]].
> - Which of these are normal: [[Group Theory §35 Normal Subgroups#^ex-35-1|A Non-Normal Subgroup of S₃]], [[Group Theory §36 Sources of Normal Subgroups#^ex-36-3|Normal Subgroups of S₃ and S₄]].

> [!remark] Remark: Preview of Lagrange
> The subgroup orders $1, 2, 3, 6$ all divide $|S_3| = 6$ — and $S_3$ has no subgroup of order $4$ or $5$. This is no accident ([[Group Theory §27 The Index and Lagrange's Theorem#^thm-27-2|Lagrange's theorem]], coming soon), but note that our classification above did *not* use it: everything followed from closure and cancellation.

^rem-13-1
