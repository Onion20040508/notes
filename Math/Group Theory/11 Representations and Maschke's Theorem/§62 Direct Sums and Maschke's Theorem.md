---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 62
tags: [group-theory, math493]
---
← [[§61 Representations and Subrepresentations]] · ↑ [[· 11 Representations and Maschke's Theorem]] · [[§63 Invariant Inner Products and Maschke over ℝ]] →

*Source: Lecture and Worksheet 14 (Wed Nov 4).*

> [!definition] Definition §62.1: Internal Direct Sum of Subspaces
> Let $W$ be a vector space and $U$, $V$ subspaces of $W$. $W$ is the **direct sum**, or **internal direct sum**, of $U$ and $V$, written $W = U \oplus V$, if
>
> $$
> U \cap V = \{0\} \qquad \text{and} \qquad U + V = W.
> $$
>
> *Source: WS 14*

^def-62-1

> [!remark]- Connections
> - Linear Algebra: [[§3 Subspaces#^ladr-1-41|LADR 1.41]] defines a direct sum by unique representation; for two subspaces this is equivalent to $U \cap V = \{0\}$ by [[§3 Subspaces#^ladr-1-46|LADR 1.46]].

This is the internal direct sum of the remark *Two Meanings of “Direct Sum”* in [[§57 Internal and External Direct Products|§57]], already used in Proposition [[§61 Representations and Subrepresentations#^prop-61-3|§61.3]]. Every $w \in W$ is then $u + v$ with $u \in U$, $v \in V$ in exactly one way: if $u + v = u' + v'$, then $u - u' = v' - v \in U \cap V = \{0\}$.

> [!example] Example §62.1: $S_3$ on $\mathbb{R}^3$ in Three Bases
> Let $S_3$ act on $\mathbb{R}^3$ by permuting coordinates (Definition [[§61 Representations and Subrepresentations#^def-61-2|§61.2]]), with the subrepresentations of Example [[§61 Representations and Subrepresentations#^ex-61-3|§61.3]]: $U = U_1 = \mathbb{R}u$, $u = (1,1,1)$, and $V = U_2$, the sum-zero plane, now with the lecture's basis
>
> $$
> v_1 = (1,-1,0) = f_1, \qquad v_2 = (0,1,-1) = f_2 - f_1.
> $$
>
> Here are three matrices of $g = (1\,2\,3)$, which sends $e_1 \mapsto e_2 \mapsto e_3 \mapsto e_1$.
>
> 1. *Standard basis* $e_1, e_2, e_3$: the permutation matrix $\left(\begin{smallmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{smallmatrix}\right)$. It does not reflect the subrepresentations at all.
> 2. *Basis $u, v_1, v_2$, adapted to $\mathbb{R}^3 = U \oplus V$.* $gu = u$; $gv_1 = e_2 - e_3 = v_2$ and $gv_2 = e_3 - e_1 = -v_1 - v_2$, so on $V$, in the basis $v_1, v_2$, $g$ acts by $\left(\begin{smallmatrix} 0 & -1 \\ 1 & -1 \end{smallmatrix}\right)$. Together:
>
> $$
> \left(\begin{array}{c|cc} 1 & 0 & 0 \\ \hline 0 & 0 & -1 \\ 0 & 1 & -1 \end{array}\right) \qquad \text{(block diagonal)}.
> $$
>
> 3. *Basis $u, e_2, e_3$, adapted to $U$ only.* $gu = u$, $ge_2 = e_3$, $ge_3 = e_1 = u - e_2 - e_3$, so
>
> $$
> \left(\begin{array}{c|cc} 1 & 0 & 1 \\ \hline 0 & 0 & -1 \\ 0 & 1 & -1 \end{array}\right) \qquad \text{(block upper triangular)}.
> $$
>
> The zeros below the first entry say that $U$ is mapped into $U$; there are no zeros to its right, because $\operatorname{span}(e_2, e_3)$ is not a subrepresentation ($ge_3 = e_1 \notin \operatorname{span}(e_2, e_3)$).
>
> All three are matrices of the same linear map in different bases, so they have the same trace ($0$), determinant ($1$) and characteristic polynomial (the remark *Checking Answers in Different Bases* in [[§61 Representations and Subrepresentations|§61]]). The lecture's slogan: in a first linear algebra course one diagonalizes a single matrix; here one wants to *block diagonalize a representation*, all the matrices $\rho(g)$ at once, and a direct sum decomposition into subrepresentations does exactly that.
>
> *Source: lecture 11/4*

^ex-62-1

![[m493-60-1.svg]]

*(Not from lecture; figure added.)* The three bases of Example [[§62 Direct Sums and Maschke's Theorem#^ex-62-1|§62.1]] in one picture. $g = (1\,2\,3)$ fixes the line $U$ (orange) pointwise and maps the plane $V$ (blue) to itself, turning it by $120^\circ$, so a basis made of a basis of $U$ and a basis of $V$ gives a block diagonal matrix. The coordinate plane $\operatorname{span}(e_2, e_3)$ (red, solid) is not mapped to itself but to $\operatorname{span}(e_3, e_1)$ (dashed), so the basis $u, e_2, e_3$ gives only a block triangular matrix.

![[m493-60-a1.gif|600]]

*(Not from lecture; animation added, vault only.)* $g = (1\,2\,3)$ is the rotation of $\mathbb{R}^3$ by $120^\circ$ about $(1,1,1)$; the animation turns by $\theta$ from $0$ to $120^\circ$. The line $U$ stays put, the hexagon in the plane $V$ turns within its plane ($gv_1 = v_2$, $gv_2 = -v_1 - v_2$), and the red square in $\operatorname{span}(e_2, e_3)$ swings out of its plane (dotted: where it started) to $\operatorname{span}(e_3, e_1)$, with $ge_2 = e_3$ and $ge_3 = e_1$.

> [!theorem] Proposition §62.1: Bases of a Direct Sum
> Let $W = U \oplus V$ (Definition [[§62 Direct Sums and Maschke's Theorem#^def-62-1|§62.1]]). If $u_1, \ldots, u_m$ is a basis of $U$ and $v_1, \ldots, v_n$ a basis of $V$, then $u_1, \ldots, u_m, v_1, \ldots, v_n$ is a basis of $W$.
>
> *Source: WS 14.1*

^prop-62-1

> [!proof]+ Proof
> *Idea:* $U + V = W$ gives spanning; $U \cap V = \{0\}$ splits a dependence relation into one in $U$ and one in $V$.
>
> *(Worksheet session 11/4.)* *Spanning:* every $w \in W$ is $u + v$ with $u \in U$, $v \in V$, and $u$, $v$ are combinations of the $u_i$, $v_j$. *Independence:* if $\sum a_i u_i + \sum b_j v_j = 0$, then $\sum a_i u_i = -\sum b_j v_j \in U \cap V = \{0\}$, so $\sum a_i u_i = 0 = \sum b_j v_j$, and all $a_i, b_j$ vanish because each list is independent.

^pf-62-1

> [!theorem] Proposition §62.2: Direct Sums Give Block Diagonal Matrices
> Let $W$ be a finite-dimensional representation of $G$ that is the direct sum of subrepresentations $U$ and $V$, with bases as in Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]. Then in the basis $(u_1, \ldots, u_m, v_1, \ldots, v_n)$,
>
> $$
> \rho_W(g) = \begin{pmatrix} \rho_U(g) & 0 \\ 0 & \rho_V(g) \end{pmatrix} \qquad \text{for all } g \in G,
> $$
>
> where $\rho_U(g)$ and $\rho_V(g)$ are the matrices in the bases $(u_i)$ and $(v_j)$.
>
> *Source: WS 14.2; lecture 11/4*

^prop-62-2

> [!proof]+ Proof
> *Idea:* Column $k$ of a matrix records the image of the $k$-th basis vector, and subrepresentations are mapped into themselves.
>
> *(Lecture 11/4.)* Column $i \leq m$ records $gu_i$, which lies in $U$ because $U$ is a subrepresentation (Definition [[§61 Representations and Subrepresentations#^def-61-3|§61.3]]); so it is a combination of the $u$'s alone, with the coefficients of column $i$ of $\rho_U(g)$, and zeros in the $v$-rows. Likewise $gv_j \in V$ gives column $j$ of $\rho_V(g)$ with zeros in the $u$-rows.

^pf-62-2

*Uses:* [[§61 Representations and Subrepresentations#^def-61-3|Def. §61.3]]

> [!theorem] Proposition §62.3: A Subrepresentation Gives Block Triangular Matrices
> Let $W$ be a finite-dimensional representation of $G$ and $U$ a subrepresentation, with basis $u_1, \ldots, u_m$, extended by arbitrary vectors $v_1, \ldots, v_n$ to a basis of $W$. Then in the basis $(u_1, \ldots, u_m, v_1, \ldots, v_n)$,
>
> $$
> \rho_W(g) = \begin{pmatrix} \rho_U(g) & \ast \\ 0 & \ast \end{pmatrix} \qquad \text{for all } g \in G:
> $$
>
> the upper left block is the matrix of $\rho_U(g)$ in the basis $(u_i)$, and the lower left block is zero; the upper right block need not be zero.
>
> *Source: WS 14.3; lecture 11/4*

^prop-62-3

> [!proof]+ Proof
> *Idea:* Only the $U$-columns are controlled.
>
> *(Lecture 11/4.)* As in Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]], $gu_i \in U$ gives the first $m$ columns: $\rho_U(g)$ on top, zeros below. Nothing is known about $gv_j$, which may have components along both the $u$'s and the $v$'s; in Example [[§62 Direct Sums and Maschke's Theorem#^ex-62-1|§62.1]](3), $ge_3 = u - e_2 - e_3$ has a $u$-component.

^pf-62-3

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]], [[§62 Direct Sums and Maschke's Theorem#^ex-62-1|Ex. §62.1]]

![[m493-60-2.svg]]

*(Not from lecture; figure added.)* The two shapes side by side. Column $j$ of $\rho_W(g)$ holds the coordinates of $g$ applied to the $j$-th basis vector. If both $U$ and $V$ are subrepresentations, the $U$-columns stay in the $U$-rows and the $V$-columns in the $V$-rows (left). If only $U$ is, the $v_j$-columns may have entries anywhere: the red block $\ast$ is what a complementary subrepresentation removes, and the lower right block is $\rho_{W/U}(g)$ (the remark *The Lower Right Block*).

> [!theorem] Proposition §62.4: The Lower Right Block Is the Quotient Representation
> Let $W$, $U$ and the basis $(u_1, \ldots, u_m, v_1, \ldots, v_n)$ be as in Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-3|§62.3]].
>
> 1. $g(w + U) := gw + U$ is a well-defined action of $G$ on the quotient space $W/U$ by linear maps, so $W/U$ is a representation of $G$.
> 2. The lower right block of $\rho_W(g)$ is the matrix of $g$ acting on $W/U$, in the basis $v_1 + U, \ldots, v_n + U$.
> 3. If $V$ is a subrepresentation with $W = U \oplus V$, then $v \mapsto v + U$ is an isomorphism of representations $V \to W/U$ (Definition [[§61 Representations and Subrepresentations#^def-61-5|§61.5]]).
>
> *Source: board 11/4; the quotient action not from class*

^prop-62-4

> [!proof]+ Proof
> *Idea:* $U$ is $G$-invariant, so $g$ passes to cosets of $U$; the $u$-components of $gv_j$ vanish modulo $U$.
>
> **(1)** *Well defined:* if $w + U = w' + U$, then $w - w' \in U$, so $gw - gw' = g(w - w') \in U$ because $U$ is $G$-invariant, i.e. $gw + U = gw' + U$. The action axioms and linearity hold in $W/U$ because they hold in $W$: $e(w + U) = w + U$, $g_1(g_2(w + U)) = g_1g_2w + U = (g_1g_2)(w + U)$, $g\big((w + U) + (w' + U)\big) = g(w + w') + U = (gw + U) + (gw' + U)$, and $g(c(w + U)) = c\,gw + U = c\,(g(w + U))$.
>
> **(2)** The cosets $v_1 + U, \ldots, v_n + U$ form a basis of $W/U$: they span, since $u_i + U = U$ is zero in $W/U$, and there are $n = \dim W - \dim U = \dim W/U$ of them. If $gv_j = \sum_i a_{ij}u_i + \sum_l c_{lj}v_l$, then $g(v_j + U) = gv_j + U = \sum_l c_{lj}(v_l + U)$, since the $u_i$ lie in $U$. So column $j$ of the matrix of $g$ on $W/U$ is $(c_{1j}, \ldots, c_{nj})^{\mathsf{T}}$, which is column $j$ of the lower right block of $\rho_W(g)$.
>
> **(3)** The map $\theta(v) = v + U$ is linear, and it commutes with the action: $\theta(gv) = gv + U = g(v + U) = g\,\theta(v)$. It is injective: $v + U = U$ means $v \in U \cap V = \{0\}$. It is surjective: every $w \in W$ is $u + v$ with $u \in U$, $v \in V$, so $w + U = v + U = \theta(v)$. So $\theta$ is an invertible homomorphism of representations.

^pf-62-4

> [!remark] Remark: The Lower Right Block
> The board labels the lower right block $\rho_{W/U}$ (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-4|§62.4]]). So a subrepresentation alone gives a block triangular form with blocks $\rho_U$ and $\rho_{W/U}$, and a complementary subrepresentation $V$ is what kills the block $\ast$; then $V \cong W/U$ as representations.
>
> *Source: board 11/4*

^rem-62-1

## Idempotents

*Source: Problem Set 9, Problems 9.2 and 9.3(1) (submitted); Worksheet 15 (Mon Nov 9).*

Maschke's theorem is proved by building a projection onto $U$ that commutes with $G$. The linear algebra behind it is the theory of idempotents, which Problem Set 9 and Worksheet 15 both start from.

> [!definition] Definition §62.2: Idempotent
> Let $V$ be a vector space. A linear map $\pi: V \to V$ is **idempotent** if $\pi^2 = \pi$, i.e. $\pi(\pi(v)) = \pi(v)$ for all $v \in V$.
>
> *Source: PS 9.2; WS 15*

^def-62-2

> [!remark]- Connections
> - Linear Algebra: the orthogonal projection $P_U$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]]) is an idempotent whose kernel is $U^\perp$, [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-57|LADR 6.57]]; Example [[§62 Direct Sums and Maschke's Theorem#^ex-62-2|§62.2]] is one whose kernel is not perpendicular to its image.

> [!theorem] Lemma §62.5: An Idempotent Fixes Its Image
> If $\pi: V \to V$ is idempotent, then $\pi(w) = w$ for every $w \in \operatorname{Im}\pi$.
>
> *Source: PS 9.2*

^lem-62-5

> [!proof]+ Proof
> *(Problem Set 9, Problem 9.2, first step, as submitted.)* Let $w \in \operatorname{Im}(\pi)$, say $w = \pi(v)$ for some $v \in V$. Then
>
> $$
> \pi(w) = \pi^2(v) = \pi(v) = w.
> $$

^pf-62-5

> [!theorem] Proposition §62.6: An Idempotent Splits the Space
> If $\pi: V \to V$ is idempotent, then $V$ is the direct sum of $\operatorname{Ker}(\pi)$ and $\operatorname{Im}(\pi)$ (Definition [[§62 Direct Sums and Maschke's Theorem#^def-62-1|§62.1]]):
>
> $$
> V = \operatorname{Ker}(\pi) \oplus \operatorname{Im}(\pi), \qquad v = \big(v - \pi(v)\big) + \pi(v).
> $$
>
> *Source: PS 9.2; WS 15.1*

^prop-62-6

> [!proof]+ Proof
> *Idea:* $v - \pi(v)$ is killed by $\pi$, and a vector in both pieces satisfies $v = \pi(v) = 0$.
>
> *(Problem Set 9, Problem 9.2, as submitted; its first step is Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]].)* Since $\pi$ is linear, $\operatorname{Ker}(\pi)$ and $\operatorname{Im}(\pi)$ are subspaces of $V$. Throughout, $v$ denotes an arbitrary element of $V$, $u$ an element of $\operatorname{Ker}(\pi)$, and $w$ an element of $\operatorname{Im}(\pi)$.
>
> **$V = \operatorname{Ker}(\pi) + \operatorname{Im}(\pi)$.** Let $v \in V$, and set $u = v - \pi(v)$ and $w = \pi(v)$. Then $w \in \operatorname{Im}(\pi)$, and
>
> $$
> \pi(u) = \pi(v) - \pi^2(v) = \pi(v) - \pi(v) = 0,
> $$
>
> so $u \in \operatorname{Ker}(\pi)$. Hence $v = u + w$ with $u \in \operatorname{Ker}(\pi)$ and $w \in \operatorname{Im}(\pi)$.
>
> **$\operatorname{Ker}(\pi) \cap \operatorname{Im}(\pi) = \{0\}$.** Let $v \in \operatorname{Ker}(\pi) \cap \operatorname{Im}(\pi)$. Since $v \in \operatorname{Im}(\pi)$, $\pi(v) = v$ by Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]]; since $v \in \operatorname{Ker}(\pi)$, $\pi(v) = 0$. Hence $v = 0$.
>
> Since $V = \operatorname{Ker}(\pi) + \operatorname{Im}(\pi)$ and $\operatorname{Ker}(\pi) \cap \operatorname{Im}(\pi) = \{0\}$, by the criterion for a direct sum of two subspaces (Axler 1.46), $V = \operatorname{Ker}(\pi) \oplus \operatorname{Im}(\pi)$.

^pf-62-6

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]]

> [!remark]- Connections
> - The criterion used at the end: [[§3 Subspaces#^ladr-1-46|LADR 1.46]].

> [!theorem] Lemma §62.7: The Complementary Idempotent
> If $\pi: V \to V$ is idempotent, then so is $\mathrm{id}_V - \pi$, and
>
> $$
> \operatorname{Im}(\mathrm{id}_V - \pi) = \operatorname{Ker}(\pi), \qquad \operatorname{Ker}(\mathrm{id}_V - \pi) = \operatorname{Im}(\pi).
> $$
>
> So the decomposition of Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-6|§62.6]] is $v = (\mathrm{id}_V - \pi)(v) + \pi(v)$, with the roles of the two idempotents exchanged when $\pi$ is replaced by $\mathrm{id}_V - \pi$.
>
> *Source: not from class*

^lem-62-7

> [!proof]+ Proof
> *(Not from class; filled in.)* *Idempotent:* $(\mathrm{id}_V - \pi)^2 = \mathrm{id}_V - 2\pi + \pi^2 = \mathrm{id}_V - 2\pi + \pi = \mathrm{id}_V - \pi$.
>
> *Image.* For $v \in V$, $\pi\big((\mathrm{id}_V - \pi)(v)\big) = \pi(v) - \pi^2(v) = 0$, so $\operatorname{Im}(\mathrm{id}_V - \pi) \subseteq \operatorname{Ker}(\pi)$. Conversely, if $v \in \operatorname{Ker}(\pi)$, then $v = v - \pi(v) = (\mathrm{id}_V - \pi)(v) \in \operatorname{Im}(\mathrm{id}_V - \pi)$.
>
> *Kernel.* $(\mathrm{id}_V - \pi)(v) = 0$ means $v = \pi(v)$. If $v = \pi(v)$, then $v \in \operatorname{Im}(\pi)$. Conversely, if $v \in \operatorname{Im}(\pi)$, then $\pi(v) = v$ by Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]].

^pf-62-7

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]]

> [!example] Example §62.2: An Idempotent That Is Not an Orthogonal Projection
> *(Not from class.)* On $\mathbb{R}^2$ let $\pi(x, y) = (x - y, 0)$. Then $\pi(\pi(x, y)) = \pi(x - y, 0) = (x - y, 0)$, so $\pi$ is idempotent, with image the $x$-axis and kernel the line $y = x$. Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-6|§62.6]] splits $(x, y) = (y, y) + (x - y, 0)$. The kernel is not perpendicular to the image, so $\pi$ is not the orthogonal projection onto the $x$-axis for the dot product ([[§63 Invariant Inner Products and Maschke over ℝ|§63]]). An idempotent is a projection onto its image *along* its kernel, and the kernel can be any complement of the image.

^ex-62-2

> [!theorem] Lemma §62.8: Every Subspace Is the Image of an Idempotent
> Let $W$ be a finite-dimensional vector space and $U \subseteq W$ a subspace. Then there is an idempotent $P: W \to W$ with $\operatorname{Im}(P) = U$.
>
> *Source: PS 9.3(1)*

^lem-62-8

> [!proof]+ Proof
> *Idea:* Extend a basis of $U$ to a basis of $W$; keep the vectors of $U$ and send the others to $0$.
>
> *(Problem Set 9, Problem 9.3(1), as submitted.)* Let $e_1, \ldots, e_m$ be a basis of $U$. Since every linearly independent list in $W$ extends to a basis of $W$ (Axler 2.32), we may extend it to a basis $e_1, \ldots, e_n$ of $W$. Since a linear map is determined by its values on a basis (Axler 3.4), there is a unique linear map $P: W \to W$ with
>
> $$
> P(e_i) = e_i \quad (1 \leq i \leq m), \qquad P(e_i) = 0 \quad (m < i \leq n).
> $$
>
> *$\operatorname{Im}(P) = U$.* Each $P(e_i)$ is either $e_i$ with $i \leq m$ or $0$, so it lies in $U$; since the $e_i$ span $W$ and $U$ is a subspace, $P(w) \in U$ for all $w \in W$, i.e. $\operatorname{Im}(P) \subseteq U$. Conversely, $P$ fixes $e_1, \ldots, e_m$, so by linearity $P(u) = u$ for all $u \in U$; hence $U \subseteq \operatorname{Im}(P)$.
>
> *$P$ is idempotent.* For $i \leq m$, $P^2(e_i) = P(e_i) = e_i$, and for $i > m$, $P^2(e_i) = P(0) = 0 = P(e_i)$. Thus the linear maps $P^2$ and $P$ agree on a basis of $W$, so $P^2 = P$.
>
> If $W$ is infinite-dimensional, the same construction applies: by Zorn's lemma, every basis of $U$ extends to a basis of $W$, and a linear map is still determined by its values on a basis.

^pf-62-8

> [!remark]- Connections
> - The two facts quoted in the proof: [[§5 Bases#^ladr-2-32|LADR 2.32]] (extending to a basis) and [[§7 Vector Space of Linear Maps#^ladr-3-4|LADR 3.4]] (a linear map is determined by a basis).

Such a $P$ depends on the choice of the extra basis vectors $e_{m+1}, \ldots, e_n$, which span its kernel. When $W$ is a representation and $U$ a subrepresentation, $\operatorname{Ker}(P)$ is in general not a subrepresentation: in Example [[§62 Direct Sums and Maschke's Theorem#^ex-62-3|§62.3]] below no complement of $U$ is. Averaging over $G$ repairs this.

> [!remark] Remark: Which Statements Need a Basis
> An Idempotent Splits the Space (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-6|§62.6]], WS 15.1) needs no finite-dimensionality: its proof never chooses a basis. The converse construction, every subspace is the image of an idempotent (Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-8|§62.8]]), chooses a basis of $W$ extending one of $U$. In infinite dimensions this probably needs a weak form of the axiom of choice, such as every vector space having a basis; the submitted proof uses Zorn's lemma. In finite dimensions this is no issue.
>
> *Source: lecture 11/9, while clarifying the problem set*

^rem-62-2

> [!theorem] Lemma §62.9: Averaging a Linear Map over $G$
> Let $G$ be a finite group and $k$ a field in which $|G| \neq 0$. Let $W$ and $W'$ be representations of $G$ over $k$ and $P: W \to W'$ a linear map. Then
>
> $$
> \pi(w) = \frac{1}{|G|}\sum_{h \in G} h^{-1}P(hw)
> $$
>
> is a homomorphism of representations $W \to W'$ (Definition [[§61 Representations and Subrepresentations#^def-61-4|§61.4]]). If $P$ is already a homomorphism of representations, then $\pi = P$.
>
> *Source: PS 9.3(2)–(3)*

^lem-62-9

> [!proof]+ Proof
> *Idea:* Moving $g$ inside the sum re-indexes it by $h \mapsto hg$.
>
> *(Problem Set 9, Problem 9.3(2) and (3), as submitted. The computation uses neither that $P$ is idempotent nor that $W' = W$.)* *$\pi$ is linear.* For each $h \in G$, the map $w \mapsto h^{-1}P(hw)$ is the composition of the linear maps $w \mapsto hw$, $P$, and $v \mapsto h^{-1}v$, hence linear. Since $|G| \neq 0$ in $k$, the scalar $\frac{1}{|G|}$ exists, and $\pi$ is a scalar multiple of a finite sum of linear maps, hence linear.
>
> *$\pi$ is a homomorphism of representations.* Let $g \in G$ and $w \in W$. Since $g$ acts linearly on $W'$, it commutes with finite sums and with the scalar $\frac{1}{|G|}$, so, writing the summation index as $h'$,
>
> $$
> g\pi(w) = \frac{1}{|G|} \sum_{h' \in G} g\big(h'^{-1} P(h'w)\big) = \frac{1}{|G|} \sum_{h' \in G} (g h'^{-1}) P(h'w),
> $$
>
> using the compatibility axiom of the action. Right multiplication $h \mapsto hg$ is a bijection $G \to G$, with inverse $h' \mapsto h'g^{-1}$, so we may substitute $h' = hg$ and sum over $h \in G$. Since $g(hg)^{-1} = gg^{-1}h^{-1} = h^{-1}$ and $(hg)w = h(gw)$,
>
> $$
> g\pi(w) = \frac{1}{|G|} \sum_{h \in G} \big(g(hg)^{-1}\big) P\big((hg)w\big) = \frac{1}{|G|} \sum_{h \in G} h^{-1} P\big(h(gw)\big) = \pi(gw).
> $$
>
> Since $g \in G$ and $w \in W$ were arbitrary, $\pi(gw) = g\pi(w)$ for all $g \in G$ and $w \in W$.
>
> *If $P$ is a homomorphism.* *(Not from class; filled in.)* Then $h^{-1}P(hw) = h^{-1}hP(w) = P(w)$ for every $h$, so $\pi(w) = \frac{1}{|G|}\big(|G| \cdot 1_k\big)P(w) = P(w)$.

^pf-62-9

## Maschke's Theorem

> [!theorem] Theorem §62.10: Maschke's Theorem
> Let $G$ be a finite group and $k$ a field in which $|G| \neq 0$. Let $W$ be a finite-dimensional representation of $G$ over $k$ and $U \subseteq W$ a subrepresentation. Then there is a subrepresentation $V \subseteq W$ with $W = U \oplus V$.
>
> *Source: WS 14; lecture 11/4; proof PS 9.3*

^thm-62-10

> [!proof]+ Proof
> *Idea:* Start from any idempotent $P$ with image $U$ and average it over $G$. The average $\pi$ is still an idempotent with image $U$, and it commutes with $G$, so its kernel is a complementary subrepresentation.
>
> *(Problem Set 9, Problem 9.3, as submitted.)* **Step 1: an idempotent with image $U$.** By Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-8|§62.8]] (PS 9.3(1)) there is an idempotent linear map $P: W \to W$ with image $U$. It is not required to be a homomorphism of representations. Define
>
> $$
> \pi(w) = \frac{1}{|G|}\sum_{h \in G} h^{-1}P(hw).
> $$
>
> By Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-9|§62.9]], $\pi$ is linear.
>
> **Step 2: $\pi$ is an idempotent with image $U$** (PS 9.3(2)). *$\pi(u) = u$ for $u \in U$.* Let $u \in U$ and $h \in G$. Since $U$ is a subrepresentation, $hu \in U = \operatorname{Im}(P)$. Since $P$ is idempotent, it is the identity on $\operatorname{Im}(P)$ (Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]]); hence $P(hu) = hu$. By the axioms of a group action, $h^{-1}(hu) = (h^{-1}h)u = eu = u$. Hence
>
> $$
> \pi(u) = \frac{1}{|G|} \sum_{h \in G} h^{-1}P(hu) = \frac{1}{|G|} \sum_{h \in G} u = \frac{1}{|G|}\big(|G| \cdot 1_k\big)\, u = u,
> $$
>
> where the last step uses $|G| \cdot 1_k \neq 0$.
>
> *$\operatorname{Im}(\pi) = U$.* Let $w \in W$ and $h \in G$. Then $P(hw) \in \operatorname{Im}(P) = U$, and since $U$ is a subrepresentation, $h^{-1}P(hw) \in U$. Since $U$ is a subspace, the scalar multiple $\pi(w)$ of the sum of these elements lies in $U$; hence $\operatorname{Im}(\pi) \subseteq U$. Conversely, every $u \in U$ satisfies $u = \pi(u) \in \operatorname{Im}(\pi)$, so $U \subseteq \operatorname{Im}(\pi)$.
>
> *$\pi$ is idempotent.* For $w \in W$, $\pi(w) \in \operatorname{Im}(\pi) = U$, so $\pi^2(w) = \pi(\pi(w)) = \pi(w)$ since $\pi$ fixes every element of $U$. Hence $\pi^2 = \pi$.
>
> **Step 3: the complement** (PS 9.3(3)). By Lemma [[§62 Direct Sums and Maschke's Theorem#^lem-62-9|§62.9]] with $W' = W$, $\pi(gw) = g\pi(w)$ for all $g \in G$ and $w \in W$: $\pi$ is a homomorphism of representations. So $\operatorname{Ker}(\pi)$ is a subrepresentation of $W$ (Kernels and Images Are Subrepresentations, Proposition [[§61 Representations and Subrepresentations#^prop-61-4|§61.4]](1), whose proof is the submitted argument).
>
> Finally, by Step 2 and Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-6|§62.6]] (PS 9.2), $W = \operatorname{Ker}(\pi) \oplus \operatorname{Im}(\pi) = \operatorname{Ker}(\pi) \oplus U$, so $V = \operatorname{Ker}(\pi)$ is a subrepresentation of $W$ with $W = U \oplus V$.

^pf-62-10

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^lem-62-8|§62.8]], [[§62 Direct Sums and Maschke's Theorem#^lem-62-9|§62.9]], [[§62 Direct Sums and Maschke's Theorem#^lem-62-5|§62.5]], [[§61 Representations and Subrepresentations#^prop-61-4|§61.4]], [[§62 Direct Sums and Maschke's Theorem#^prop-62-6|§62.6]]

For $k = \mathbb{R}$ there is a second, geometric proof, by averaging an inner product instead of an idempotent: Corollary [[§63 Invariant Inner Products and Maschke over ℝ#^cor-63-6|§63.6]], in [[§63 Invariant Inner Products and Maschke over ℝ|§63]].

“$|G| \neq 0$ in $k$” means that $1 + 1 + \cdots + 1$ ($|G|$ terms) is not $0$ in $k$, that is, the characteristic of $k$ does not divide $|G|$; it holds for every finite group when $k = \mathbb{Q}$, $\mathbb{R}$ or $\mathbb{C}$. *(Not from class.)* By Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]], the theorem says that every subrepresentation can be split off, so that all the matrices $\rho_W(g)$ become block diagonal at once. For $S_3$ acting on $k\{1,2,3\}$ the condition means $6 \neq 0$ in $k$; compare Proposition [[§61 Representations and Subrepresentations#^prop-61-3|§61.3]], where the decomposition $U_1 \oplus U_2$ fails when $3 = 0$, and the remark *Why This Is “Tricky”* in [[§61 Representations and Subrepresentations|§61]].

**Transcription note (board 11/4).** The board states the theorem with “let $V$ be a finite dim rep of $G$ over $k$, let $U \subseteq V$ be a subrep”; the representation is $W$, as in the conclusion “$\exists$ subrep $V \subseteq W$ s.t. $W = U \oplus V$” and on the worksheet.

## When Maschke's Theorem Fails

*Source: Problem Set 9, Problem 9.4 (submitted).*

Neither hypothesis of Maschke's theorem can be dropped: one shear matrix gives a counterexample both for an infinite group and for a finite group whose order is $0$ in $k$.

> [!example] Example §62.3: Maschke Fails for the Infinite Group $\mathbb{Z}$
> Let $G = \mathbb{Z}$ and define $\rho: \mathbb{Z} \to GL_2(\mathbb{R})$ by $\rho(x) = \left(\begin{smallmatrix} 1 & x \\ 0 & 1 \end{smallmatrix}\right)$. This is a homomorphism, since $\left(\begin{smallmatrix} 1 & x \\ 0 & 1 \end{smallmatrix}\right)\left(\begin{smallmatrix} 1 & y \\ 0 & 1 \end{smallmatrix}\right) = \left(\begin{smallmatrix} 1 & x + y \\ 0 & 1 \end{smallmatrix}\right)$. With $e_1 = (1, 0)$, the line $\mathbb{R}e_1$ is a subrepresentation of $\mathbb{R}^2$, but there is no subrepresentation $V$ with $\mathbb{R}^2 = \mathbb{R}e_1 \oplus V$.
>
> *Source: PS 9.4(1)*

^ex-62-3

> [!proof]+ Proof
> *Idea:* A complement is a line $\mathbb{R}(a, 1)$, and $\rho(1)$ slides $(a, 1)$ to $(a + 1, 1)$, off that line.
>
> *(Problem Set 9, Problem 9.4(1), as submitted.)* *$\mathbb{R}e_1$ is a subrepresentation.* $\mathbb{R}e_1$ is a subspace of $\mathbb{R}^2$, and for $x \in \mathbb{Z}$ and $a \in \mathbb{R}$,
>
> $$
> \rho(x)\begin{pmatrix} a \\ 0 \end{pmatrix} = \begin{pmatrix} 1 & x \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ 0 \end{pmatrix} \in \mathbb{R}e_1.
> $$
>
> *No complementary subrepresentation.* Suppose $V \subseteq \mathbb{R}^2$ is a subspace with $\mathbb{R}^2 = \mathbb{R}e_1 \oplus V$. Then $\dim V = 2 - 1 = 1$, so $V = \mathbb{R}v$ for some $v = (b, c) \neq 0$. Since $\mathbb{R}e_1 \cap V = \{0\}$, $v \notin \mathbb{R}e_1$, so $c \neq 0$, and replacing $v$ by $c^{-1}v$ we may take $v = (a, 1)$ with $a = b/c$. Every element of $V$ has the form $\lambda v = (\lambda a, \lambda)$, so the only element of $V$ with second coordinate $1$ is $v$. Now
>
> $$
> \rho(1)\, v = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a \\ 1 \end{pmatrix} = \begin{pmatrix} a + 1 \\ 1 \end{pmatrix} \neq v,
> $$
>
> so $\rho(1)v \notin V$. Hence $V$ is not a subrepresentation, and no subrepresentation $V$ satisfies $\mathbb{R}^2 = \mathbb{R}e_1 \oplus V$.

^pf-ex-62-3

> [!example] Example §62.4: Maschke Fails When $|G| = 0$ in $k$
> Let $p$ be prime, $G = \mathbb{Z}/p\mathbb{Z}$ and $\mathbb{F} = \mathbb{Z}/p\mathbb{Z}$, and define $\rho: G \to GL_2(\mathbb{F})$ by the same matrices $\rho(x) = \left(\begin{smallmatrix} 1 & x \\ 0 & 1 \end{smallmatrix}\right)$, now with $x \in \mathbb{F}$; the product rule above shows again that $\rho$ is a homomorphism. Then $\mathbb{F}e_1$ is a subrepresentation of $\mathbb{F}^2$, but there is no subrepresentation $V$ with $\mathbb{F}^2 = \mathbb{F}e_1 \oplus V$. Here $G$ is finite, but $|G| = p = 0$ in $\mathbb{F}$.
>
> *Source: PS 9.4(2)*

^ex-62-4

> [!proof]+ Proof
> *(Problem Set 9, Problem 9.4(2), as submitted.)* *$\mathbb{F}e_1$ is a subrepresentation.* $\mathbb{F}e_1$ is a subspace of $\mathbb{F}^2$, and for $x \in \mathbb{Z}/p\mathbb{Z}$ and $a \in \mathbb{F}$,
>
> $$
> \rho(x)\begin{pmatrix} a \\ 0 \end{pmatrix} = \begin{pmatrix} 1 & x \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ 0 \end{pmatrix} \in \mathbb{F}e_1.
> $$
>
> *No complementary subrepresentation.* Suppose $V \subseteq \mathbb{F}^2$ is a subspace with $\mathbb{F}^2 = \mathbb{F}e_1 \oplus V$. Then $\dim V = 1$, so $V = \mathbb{F}v$ for some $v = (b, c) \neq 0$. Since $\mathbb{F}e_1 \cap V = \{0\}$, $c \neq 0$; since $\mathbb{F}$ is a field, $c$ is invertible, and replacing $v$ by $c^{-1}v$ we may take $v = (a, 1)$. As before, the only element of $V$ with second coordinate $1$ is $v$. Since $1 \neq 0$ in $\mathbb{Z}/p\mathbb{Z}$,
>
> $$
> \rho(1)\, v = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} a \\ 1 \end{pmatrix} = \begin{pmatrix} a + 1 \\ 1 \end{pmatrix} \neq v,
> $$
>
> so $\rho(1)v \notin V$. Hence no subrepresentation $V$ satisfies $\mathbb{F}^2 = \mathbb{F}e_1 \oplus V$.

^pf-ex-62-4

> [!proof]+ Second proof of both examples (block diagonal form)
> *(Not from class.)* Let $k$ be $\mathbb{R}$ or $\mathbb{F}$, and suppose $k^2 = ke_1 \oplus V$ with $V$ a subrepresentation, say $V = kv$. By Bases of a Direct Sum (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]), $(e_1, v)$ is a basis of $k^2$, and by Direct Sums Give Block Diagonal Matrices (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]) the matrix of $\rho(1)$ in this basis is diagonal: $\rho(1)e_1 = e_1$ and $\rho(1)v = cv$ for some $c \in k$. The trace does not depend on the basis (the remark *Checking Answers in Different Bases* in [[§61 Representations and Subrepresentations|§61]]), and in the standard basis $\operatorname{Tr}\rho(1) = 1 + 1$. So $1 + c = 1 + 1$, and $c = 1$. Then $\rho(1)$ fixes both basis vectors, so $\rho(1) = I$. But $\rho(1) = \left(\begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix}\right) \neq I$, since $1 \neq 0$ in $k$. In other words, a complement would make the shear $\rho(1)$ diagonalizable, and a diagonalizable matrix whose eigenvalues are all $1$ is $I$.

^pf-ex-62-4-2

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]], [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]

![[m493-60-6.svg]]

*(Not from lecture; figure added.)* The shear $\rho(1)$ of Examples [[§62 Direct Sums and Maschke's Theorem#^ex-62-3|§62.3]] and [[§62 Direct Sums and Maschke's Theorem#^ex-62-4|§62.4]]. A line through $0$ other than the $x$-axis meets the line $y = 1$ in one point $v = (a, 1)$, and $\rho(1)$ slides that point to $(a + 1, 1)$, which lies on a different line (left: $v = (-1, 1)$, $\rho(1)v = (0, 1)$, $\rho(1)^2v = (1, 1)$). So the red $x$-axis $\mathbb{R}e_1$ is the only line that $\rho(1)$ maps to itself, and no line can serve as a complement. Over $\mathbb{F}_3$ (right) the plane has nine points and four lines through $0$. The red points form $\mathbb{F}e_1$, and the row $y = 1$ contains one point of each other line. $\rho(1)$ slides that row by $e_1$, cyclically mod $3$, so it permutes the lines $L_0 \to L_1 \to L_2 \to L_0$ and fixes none of them.

> [!remark] Remark: Where Each Hypothesis Is Used
> *(Not from class.)* In the proof of Maschke's theorem, $G$ finite makes $\sum_{h \in G}$ a finite sum, and $|G| \neq 0$ in $k$ allows the division by $|G|$ that gives $\pi(u) = u$ in Step 2. For $G = \mathbb{Z}$ there is no finite average to take. For $G = \mathbb{Z}/p\mathbb{Z}$ over $\mathbb{F}_p$ the sum $\sum_h h^{-1}P(hu) = p \cdot u$ is $0$ for every $u \in U$. In both cases the examples show that no other construction can help either.

^rem-62-3