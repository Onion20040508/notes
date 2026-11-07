---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 60
tags: [group-theory, math493]
---
← [[§59 Representations and Subrepresentations]] · ↑ [[· 11 Representations]] · [[§61 Invariant Inner Products and Maschke over ℝ]] →

*Source: Lecture and Worksheet 14 (Wed Nov 4).*

> [!definition] Definition §60.1: Internal Direct Sum of Subspaces
> Let $W$ be a vector space and $U$, $V$ subspaces of $W$. $W$ is the **direct sum**, or **internal direct sum**, of $U$ and $V$, written $W = U \oplus V$, if
>
> $$
> U \cap V = \{0\} \qquad \text{and} \qquad U + V = W.
> $$
>
> *Source: WS 14*

^def-60-1

> [!remark]- Connections
> - Linear Algebra: [[§3 Subspaces#^ladr-1-41|LADR 1.41]] defines a direct sum by unique representation; for two subspaces this is equivalent to $U \cap V = \{0\}$ by [[§3 Subspaces#^ladr-1-46|LADR 1.46]].

This is the internal direct sum of the remark *Two Meanings of “Direct Sum”* in [[§57 Internal and External Direct Products|§57]], already used in Proposition [[§59 Representations and Subrepresentations#^prop-59-3|§59.3]]. Every $w \in W$ is then $u + v$ with $u \in U$, $v \in V$ in exactly one way: if $u + v = u' + v'$, then $u - u' = v' - v \in U \cap V = \{0\}$.

> [!example] Example §60.1: $S_3$ on $\mathbb{R}^3$ in Three Bases
> Let $S_3$ act on $\mathbb{R}^3$ by permuting coordinates (Definition [[§59 Representations and Subrepresentations#^def-59-2|§59.2]]), with the subrepresentations of Example [[§59 Representations and Subrepresentations#^ex-59-3|§59.3]]: $U = U_1 = \mathbb{R}u$, $u = (1,1,1)$, and $V = U_2$, the sum-zero plane, now with the lecture's basis
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
> All three are matrices of the same linear map in different bases, so they have the same trace ($0$), determinant ($1$) and characteristic polynomial (the remark *Checking Answers in Different Bases* in [[§59 Representations and Subrepresentations|§59]]). The lecture's slogan: in a first linear algebra course one diagonalizes a single matrix; here one wants to *block diagonalize a representation*, all the matrices $\rho(g)$ at once, and a direct sum decomposition into subrepresentations does exactly that.
>
> *Source: lecture 11/4*

^ex-60-1

![[m493-60-1.svg]]

*(Not from lecture; figure added.)* The three bases of Example §60.1 in one picture. $g = (1\,2\,3)$ fixes the line $U$ (orange) pointwise and maps the plane $V$ (blue) to itself, turning it by $120^\circ$, so a basis made of a basis of $U$ and a basis of $V$ gives a block diagonal matrix. The coordinate plane $\operatorname{span}(e_2, e_3)$ (red, solid) is not mapped to itself but to $\operatorname{span}(e_3, e_1)$ (dashed), so the basis $u, e_2, e_3$ gives only a block triangular matrix.

![[m493-60-a1.gif|600]]

*(Not from lecture; animation added, vault only.)* $g = (1\,2\,3)$ is the rotation of $\mathbb{R}^3$ by $120^\circ$ about $(1,1,1)$; the animation turns by $\theta$ from $0$ to $120^\circ$. The line $U$ stays put, the hexagon in the plane $V$ turns within its plane ($gv_1 = v_2$, $gv_2 = -v_1 - v_2$), and the red square in $\operatorname{span}(e_2, e_3)$ swings out of its plane (dotted: where it started) to $\operatorname{span}(e_3, e_1)$, with $ge_2 = e_3$ and $ge_3 = e_1$.

> [!theorem] Proposition §60.1: Bases of a Direct Sum
> Let $W = U \oplus V$ (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-1|§60.1]]). If $u_1, \ldots, u_m$ is a basis of $U$ and $v_1, \ldots, v_n$ a basis of $V$, then $u_1, \ldots, u_m, v_1, \ldots, v_n$ is a basis of $W$.
>
> *Source: WS 14.1*

^prop-60-1

> [!proof]+ Proof
> *Idea:* $U + V = W$ gives spanning; $U \cap V = \{0\}$ splits a dependence relation into one in $U$ and one in $V$.
>
> *(Worksheet session 11/4.)* *Spanning:* every $w \in W$ is $u + v$ with $u \in U$, $v \in V$, and $u$, $v$ are combinations of the $u_i$, $v_j$. *Independence:* if $\sum a_i u_i + \sum b_j v_j = 0$, then $\sum a_i u_i = -\sum b_j v_j \in U \cap V = \{0\}$, so $\sum a_i u_i = 0 = \sum b_j v_j$, and all $a_i, b_j$ vanish because each list is independent.

^pf-60-1

> [!theorem] Proposition §60.2: Direct Sums Give Block Diagonal Matrices
> Let $W$ be a finite-dimensional representation of $G$ that is the direct sum of subrepresentations $U$ and $V$, with bases as in Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-1|§60.1]]. Then in the basis $(u_1, \ldots, u_m, v_1, \ldots, v_n)$,
>
> $$
> \rho_W(g) = \begin{pmatrix} \rho_U(g) & 0 \\ 0 & \rho_V(g) \end{pmatrix} \qquad \text{for all } g \in G,
> $$
>
> where $\rho_U(g)$ and $\rho_V(g)$ are the matrices in the bases $(u_i)$ and $(v_j)$.
>
> *Source: WS 14.2; lecture 11/4*

^prop-60-2

> [!proof]+ Proof
> *Idea:* Column $k$ of a matrix records the image of the $k$-th basis vector, and subrepresentations are mapped into themselves.
>
> *(Lecture 11/4.)* Column $i \leq m$ records $gu_i$, which lies in $U$ because $U$ is a subrepresentation (Definition [[§59 Representations and Subrepresentations#^def-59-3|§59.3]]); so it is a combination of the $u$'s alone, with the coefficients of column $i$ of $\rho_U(g)$, and zeros in the $v$-rows. Likewise $gv_j \in V$ gives column $j$ of $\rho_V(g)$ with zeros in the $u$-rows.

^pf-60-2

*Uses:* [[§59 Representations and Subrepresentations#^def-59-3|Def. §59.3]]

> [!theorem] Proposition §60.3: A Subrepresentation Gives Block Triangular Matrices
> Let $W$ be a finite-dimensional representation of $G$ and $U$ a subrepresentation, with basis $u_1, \ldots, u_m$, extended by arbitrary vectors $v_1, \ldots, v_n$ to a basis of $W$. Then in the basis $(u_1, \ldots, u_m, v_1, \ldots, v_n)$,
>
> $$
> \rho_W(g) = \begin{pmatrix} \rho_U(g) & \ast \\ 0 & \ast \end{pmatrix} \qquad \text{for all } g \in G:
> $$
>
> the upper left block is the matrix of $\rho_U(g)$ in the basis $(u_i)$, and the lower left block is zero; the upper right block need not be zero.
>
> *Source: WS 14.3; lecture 11/4*

^prop-60-3

> [!proof]+ Proof
> *Idea:* Only the $U$-columns are controlled.
>
> *(Lecture 11/4.)* As in Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-2|§60.2]], $gu_i \in U$ gives the first $m$ columns: $\rho_U(g)$ on top, zeros below. Nothing is known about $gv_j$, which may have components along both the $u$'s and the $v$'s; in Example [[§60 Direct Sums and Maschke's Theorem#^ex-60-1|§60.1]](3), $ge_3 = u - e_2 - e_3$ has a $u$-component.

^pf-60-3

*Uses:* [[§60 Direct Sums and Maschke's Theorem#^prop-60-2|§60.2]], [[§60 Direct Sums and Maschke's Theorem#^ex-60-1|Ex. §60.1]]

![[m493-60-2.svg]]

> [!theorem] Proposition §60.4: The Lower Right Block Is the Quotient Representation
> Let $W$, $U$ and the basis $(u_1, \ldots, u_m, v_1, \ldots, v_n)$ be as in Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-3|§60.3]].
>
> 1. $g(w + U) := gw + U$ is a well-defined action of $G$ on the quotient space $W/U$ by linear maps, so $W/U$ is a representation of $G$.
> 2. The lower right block of $\rho_W(g)$ is the matrix of $g$ acting on $W/U$, in the basis $v_1 + U, \ldots, v_n + U$.
> 3. If $V$ is a subrepresentation with $W = U \oplus V$, then $v \mapsto v + U$ is an isomorphism of representations $V \to W/U$ (Definition [[§59 Representations and Subrepresentations#^def-59-5|§59.5]]).
>
> *Source: board 11/4; the quotient action not from class*

^prop-60-4

> [!proof]+ Proof
> *Idea:* $U$ is $G$-invariant, so $g$ passes to cosets of $U$; the $u$-components of $gv_j$ vanish modulo $U$.
>
> **(1)** *Well defined:* if $w + U = w' + U$, then $w - w' \in U$, so $gw - gw' = g(w - w') \in U$ because $U$ is $G$-invariant, i.e. $gw + U = gw' + U$. The action axioms and linearity hold in $W/U$ because they hold in $W$: $e(w + U) = w + U$, $g_1(g_2(w + U)) = g_1g_2w + U = (g_1g_2)(w + U)$, $g\big((w + U) + (w' + U)\big) = g(w + w') + U = (gw + U) + (gw' + U)$, and $g(c(w + U)) = c\,gw + U = c\,(g(w + U))$.
>
> **(2)** The cosets $v_1 + U, \ldots, v_n + U$ form a basis of $W/U$: they span, since $u_i + U = U$ is zero in $W/U$, and there are $n = \dim W - \dim U = \dim W/U$ of them. If $gv_j = \sum_i a_{ij}u_i + \sum_l c_{lj}v_l$, then $g(v_j + U) = gv_j + U = \sum_l c_{lj}(v_l + U)$, since the $u_i$ lie in $U$. So column $j$ of the matrix of $g$ on $W/U$ is $(c_{1j}, \ldots, c_{nj})^{\mathsf{T}}$, which is column $j$ of the lower right block of $\rho_W(g)$.
>
> **(3)** The map $\theta(v) = v + U$ is linear, and it commutes with the action: $\theta(gv) = gv + U = g(v + U) = g\,\theta(v)$. It is injective: $v + U = U$ means $v \in U \cap V = \{0\}$. It is surjective: every $w \in W$ is $u + v$ with $u \in U$, $v \in V$, so $w + U = v + U = \theta(v)$. So $\theta$ is an invertible homomorphism of representations.

^pf-60-4

> [!remark] Remark: The Lower Right Block
> The board labels the lower right block $\rho_{W/U}$ (Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-4|§60.4]]). So a subrepresentation alone gives a block triangular form with blocks $\rho_U$ and $\rho_{W/U}$, and a complementary subrepresentation $V$ is what kills the block $\ast$; then $V \cong W/U$ as representations.
>
> *Source: board 11/4*

^rem-60-1

*(Not from lecture; figure added.)* The two shapes side by side. Column $j$ of $\rho_W(g)$ holds the coordinates of $g$ applied to the $j$-th basis vector. If both $U$ and $V$ are subrepresentations, the $U$-columns stay in the $U$-rows and the $V$-columns in the $V$-rows (left). If only $U$ is, the $v_j$-columns may have entries anywhere: the red block $\ast$ is what a complementary subrepresentation removes, and the lower right block is $\rho_{W/U}(g)$ (the remark *The Lower Right Block*).

> [!theorem] Theorem §60.5: Maschke's Theorem
> Let $G$ be a finite group and $k$ a field in which $|G| \neq 0$. Let $W$ be a finite-dimensional representation of $G$ over $k$ and $U \subseteq W$ a subrepresentation. Then there is a subrepresentation $V \subseteq W$ with $W = U \oplus V$.
>
> *Source: WS 14; lecture 11/4*

^thm-60-5

> [!proof]+ Proof (to be filled)
> The general case is on the problem set; it is added here after the problem set is submitted. The case $k = \mathbb{R}$ is Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]], in [[§61 Invariant Inner Products and Maschke over ℝ|§61]].

^pf-60-5

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]]

“$|G| \neq 0$ in $k$” means that $1 + 1 + \cdots + 1$ ($|G|$ terms) is not $0$ in $k$, that is, the characteristic of $k$ does not divide $|G|$; it holds for every finite group when $k = \mathbb{Q}$, $\mathbb{R}$ or $\mathbb{C}$. *(Not from class.)* By Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-2|§60.2]], the theorem says that every subrepresentation can be split off, so that all the matrices $\rho_W(g)$ become block diagonal at once. For $S_3$ acting on $k\{1,2,3\}$ the condition means $6 \neq 0$ in $k$; compare Proposition [[§59 Representations and Subrepresentations#^prop-59-3|§59.3]], where the decomposition $U_1 \oplus U_2$ fails when $3 = 0$, and the remark *Why This Is “Tricky”* in [[§59 Representations and Subrepresentations|§59]].

**Transcription note (board 11/4).** The board states the theorem with “let $V$ be a finite dim rep of $G$ over $k$, let $U \subseteq V$ be a subrep”; the representation is $W$, as in the conclusion “$\exists$ subrep $V \subseteq W$ s.t. $W = U \oplus V$” and on the worksheet.
