---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 60
tags: [group-theory, math493]
---
← [[§59 Representations and Subrepresentations]] · ↑ [[· 11 Representations]]

*Source: Lecture and Worksheet 14 (Wed Nov 4); WS 14.7–14.8 are to be presented Fri Nov 6. Reference for the linear algebra: Axler, Linear Algebra Done Right, Ch. 6 (orthonormal bases, orthogonal complements).*

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

*(Not from lecture; figure added.)* The two shapes side by side. Column $j$ of $\rho_W(g)$ holds the coordinates of $g$ applied to the $j$-th basis vector. If both $U$ and $V$ are subrepresentations, the $U$-columns stay in the $U$-rows and the $V$-columns in the $V$-rows (left). If only $U$ is, the $v_j$-columns may have entries anywhere: the red block $\ast$ is what a complementary subrepresentation removes, and the lower right block is $\rho_{W/U}(g)$ (the remark *The Lower Right Block*).

> [!remark] Remark: The Lower Right Block
> The board labels the lower right block $\rho_{W/U}$. Indeed $U$ is $G$-invariant, so $g(w + U) := gw + U$ is a well-defined action of $G$ on the quotient space $W/U$ (if $w - w' \in U$ then $gw - gw' = g(w - w') \in U$), by linear maps, and the lower right block is its matrix in the basis $v_1 + U, \ldots, v_n + U$: if $gv_j = \sum_i a_{ij}u_i + \sum_l c_{lj}v_l$, then $g(v_j + U) = \sum_l c_{lj}(v_l + U)$. So a subrepresentation alone gives a block triangular form with blocks $\rho_U$ and $\rho_{W/U}$, and a complementary subrepresentation $V$ is what kills the block $\ast$; then $V \cong W/U$ as representations, via $v \mapsto v + U$ (Definition [[§59 Representations and Subrepresentations#^def-59-5|§59.5]]).
>
> *Source: board 11/4; the quotient action not from class*

^rem-60-1

> [!theorem] Theorem §60.4: Maschke's Theorem
> Let $G$ be a finite group and $k$ a field in which $|G| \neq 0$. Let $W$ be a finite-dimensional representation of $G$ over $k$ and $U \subseteq W$ a subrepresentation. Then there is a subrepresentation $V \subseteq W$ with $W = U \oplus V$.
>
> *Source: WS 14; lecture 11/4*

^thm-60-4

> [!proof]+ Proof (to be filled)
> The general case is on the problem set; it is added here after the problem set is submitted. The case $k = \mathbb{R}$ is Corollary [[§60 Direct Sums and Maschke's Theorem#^cor-60-10|§60.10]] below.

^pf-60-4

*Uses:* [[§60 Direct Sums and Maschke's Theorem#^cor-60-10|§60.10]]

“$|G| \neq 0$ in $k$” means that $1 + 1 + \cdots + 1$ ($|G|$ terms) is not $0$ in $k$, that is, the characteristic of $k$ does not divide $|G|$; it holds for every finite group when $k = \mathbb{Q}$, $\mathbb{R}$ or $\mathbb{C}$. *(Not from class.)* By Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-2|§60.2]], the theorem says that every subrepresentation can be split off, so that all the matrices $\rho_W(g)$ become block diagonal at once. For $S_3$ acting on $k\{1,2,3\}$ the condition means $6 \neq 0$ in $k$; compare Proposition [[§59 Representations and Subrepresentations#^prop-59-3|§59.3]], where the decomposition $U_1 \oplus U_2$ fails when $3 = 0$, and the remark *Why This Is “Tricky”* in [[§59 Representations and Subrepresentations|§59]].

**Transcription note (board 11/4).** The board states the theorem with “let $V$ be a finite dim rep of $G$ over $k$, let $U \subseteq V$ be a subrep”; the representation is $W$, as in the conclusion “$\exists$ subrep $V \subseteq W$ s.t. $W = U \oplus V$” and on the worksheet.

> [!definition] Definition §60.2: Inner Product
> An **inner product** on a real vector space $W$ is a positive definite symmetric bilinear form $\langle\ ,\ \rangle: W \times W \to \mathbb{R}$:
>
> 1. bilinear: linear in each argument when the other is fixed;
> 2. symmetric: $\langle v, w \rangle = \langle w, v \rangle$;
> 3. positive definite: $\langle v, v \rangle > 0$ for $v \neq 0$.
>
> *Source: WS 14*

^def-60-2

> [!remark]- Connections
> - Linear Algebra: [[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]] (inner products over $\mathbb{R}$ and $\mathbb{C}$).

> [!definition] Definition §60.3: Orthogonal Complement
> Let $W$ be a real vector space with an inner product $\langle\ ,\ \rangle$ and $U \subseteq W$ a subspace. The **orthogonal complement** of $U$ is
>
> $$
> U^\perp = \{ w \in W : \langle u, w \rangle = 0 \text{ for all } u \in U \}.
> $$
>
> *Source: WS 14*

^def-60-3

> [!remark]- Connections
> - Linear Algebra: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]].

> [!definition] Definition §60.4: $G$ Preserves an Inner Product
> Let $W$ be a real representation of $G$ with an inner product $\langle\ ,\ \rangle$. $G$ **preserves** $\langle\ ,\ \rangle$ if
>
> $$
> \langle gv, gw \rangle = \langle v, w \rangle \qquad \text{for all } g \in G \text{ and } v, w \in W,
> $$
>
> that is, each $\rho(g)$ is an orthogonal map.
>
> *Source: WS 14*

^def-60-4

> [!remark]- Connections
> - Linear Algebra: an orthogonal map is an isometry, [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]].

> [!theorem] Proposition §60.5: Direct Sum of a Subspace and Its Orthogonal Complement
> Let $W$ be a finite-dimensional real vector space with an inner product and $U \subseteq W$ a subspace. Then $W = U \oplus U^\perp$.
>
> *Source: WS 14.4; board 11/4*

^prop-60-5

> [!proof]+ Proof
> *Idea:* Positive definiteness gives $U \cap U^\perp = \{0\}$; the orthogonal projection $P_U$ splits every $w$ as $P_U(w) + (w - P_U(w))$.
>
> *(Board 11/4.)* $U^\perp$ is a subspace, by bilinearity.
>
> *$U \cap U^\perp = \{0\}$.* If $u \in U \cap U^\perp$, then $\langle u, u \rangle = 0$, so $u = 0$ by positive definiteness.
>
> *$U + U^\perp = W$.* Let $u_1, \ldots, u_m$ be an orthonormal basis of $U$ (it exists by [[Gram–Schmidt procedure|Gram–Schmidt]]): $\langle u_i, u_j \rangle = 1$ if $i = j$ and $0$ otherwise. For $w \in W$ define the orthogonal projection
>
> $$
> P_U(w) = \sum_{j=1}^m \langle w, u_j \rangle\, u_j \in U.
> $$
>
> We claim $w - P_U(w) \in U^\perp$; by bilinearity it suffices to check against the basis vectors $u_i$:
>
> $$
> \langle u_i, w - P_U(w) \rangle = \langle u_i, w \rangle - \sum_j \langle w, u_j \rangle \langle u_i, u_j \rangle = \langle u_i, w \rangle - \langle w, u_i \rangle = 0,
> $$
>
> since only the term $j = i$ survives, and $\langle w, u_i \rangle = \langle u_i, w \rangle$ by symmetry. Hence $w = P_U(w) + \big(w - P_U(w)\big) \in U + U^\perp$.

^pf-60-5

> [!remark]- Connections
> - Linear Algebra: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]] (the same statement) and [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-57|LADR 6.57]] (properties of $P_U$, with the formula used here in part (i)).
> - Functional Analysis: in a Hilbert space the same decomposition holds for closed subspaces, [[§25 Projection and Orthogonal Decomposition#^thm-25-4|556 Thm. §25.4]].

![[m493-60-3.svg]]

*(Not from lecture; figure added.)* The proof of Proposition §60.5 in $\mathbb{R}^3$ with the dot product: $U$ is a plane with orthonormal basis $u_1, u_2$, and $U^\perp$ is the normal line. $P_U(w)$ is the foot of the perpendicular from $w$ to $U$, and the remainder $w - P_U(w)$ (red) is parallel to $U^\perp$.

> [!theorem] Proposition §60.6: Orthogonal Complements of Subrepresentations
> Let $W$ be a real representation of $G$ with an inner product preserved by $G$ (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-4|§60.4]]), and let $U$ be a subrepresentation. Then $U^\perp$ is a subrepresentation.
>
> *Source: WS 14.5; board 11/4*

^prop-60-6

> [!proof]+ Proof
> *Idea:* Move $g$ to the other side of the inner product as $g^{-1}$.
>
> *(Board 11/4.)* Let $w \in U^\perp$ and $g \in G$; we must show $\langle u, gw \rangle = 0$ for all $u \in U$. Write $u = g(g^{-1}u)$. Since $G$ preserves the inner product,
>
> $$
> \langle u, gw \rangle = \langle g(g^{-1}u), gw \rangle = \langle g^{-1}u, w \rangle = 0,
> $$
>
> because $g^{-1}u \in U$ ($U$ is a subrepresentation) and $w \in U^\perp$.

^pf-60-6

> [!theorem] Corollary §60.7: Maschke for Representations Preserving an Inner Product
> Let $W$ be a finite-dimensional real representation of a group $G$ (finite or not) that preserves an inner product on $W$, and let $U$ be a subrepresentation. Then $V = U^\perp$ is a subrepresentation with $W = U \oplus V$.
>
> *Source: WS 14.6*

^cor-60-7

> [!proof]+ Proof
> *(Lecture 11/4.)* $W = U \oplus U^\perp$ by Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-5|§60.5]], and $U^\perp$ is a subrepresentation by Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]].

^pf-60-7

*Uses:* [[§60 Direct Sums and Maschke's Theorem#^prop-60-5|§60.5]], [[§60 Direct Sums and Maschke's Theorem#^prop-60-6|§60.6]]

**Transcription note (WS 14).** Problem 14.6 says “$W$ preserves an inner product”; “$G$ preserves” is meant (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-4|§60.4]]).

> [!remark] Remark: Physical Meaning
> That $G$ preserves an inner product means that $G$ acts by orthogonal matrices, which preserve lengths and angles: a natural condition for symmetries of objects in space. The lecture noted that physicists also meet symmetries of space-time, which preserve a form that is not positive definite. The remaining step is to show that for a *finite* group such an inner product always exists, even if the given one is not preserved.
>
> *Source: lecture 11/4*

^rem-60-2

> [!definition] Definition §60.5: The Averaged Inner Product
> Let $W$ be a real representation of a finite group $G$, and let $(\ ,\ )$ be any inner product on $W$, not necessarily preserved by $G$. Define
>
> $$
> \langle v, w \rangle := \sum_{g \in G} (gv, gw) \qquad (v, w \in W).
> $$
>
> *Source: WS 14*

^def-60-5

**Transcription note (WS 14).** The worksheet prints the sum as $\sum_{g \in G} \langle gv, gw \rangle$, with the new brackets on both sides; the sum uses the original inner product $(\ ,\ )$.

> [!theorem] Proposition §60.8: Averaging Gives an Inner Product
> $\langle\ ,\ \rangle$ (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-5|§60.5]]) is an inner product on $W$.
>
> *Source: WS 14.7*

^prop-60-8

> [!proof]+ Proof (to be filled)
> WS 14.7 is to be presented in class on Fri Nov 6.

^pf-60-8

> [!theorem] Proposition §60.9: $G$ Preserves the Averaged Inner Product
> $\langle hv, hw \rangle = \langle v, w \rangle$ for all $h \in G$ and $v, w \in W$.
>
> *Source: WS 14.8*

^prop-60-9

> [!proof]+ Proof (to be filled)
> WS 14.8 is to be presented in class on Fri Nov 6.

^pf-60-9

![[m493-60-4.svg]]

*(Not from lecture; figure added.)* The averaged inner product for $S_3$ acting on $U_2$ (Example [[§59 Representations and Subrepresentations#^ex-59-3|§59.3]]), drawn in the coordinates $x_1, x_2$ of the basis $f_1, f_2$. Take for $(\ ,\ )$ the dot product of coordinates. It is not preserved: the grey ellipses $\{v : (gv, gv) = 1\}$ for $g \neq e$ differ from the red unit circle. The level set $\langle v, v \rangle = 6$ of the averaged form (blue) is mapped to itself by all six matrices of the table in §59, as WS 14.8 asserts.

> [!theorem] Corollary §60.10: Maschke's Theorem over $\mathbb{R}$
> Let $G$ be finite and $W$ a finite-dimensional real representation of $G$. Every subrepresentation $U$ of $W$ has a complementary subrepresentation $V$, with $W = U \oplus V$.
>
> *Source: WS 14*

^cor-60-10

> [!proof]+ Proof
> *Idea:* Make $G$ preserve an inner product by averaging, then take the orthogonal complement.
>
> Choose any inner product on $W$ (for instance, the dot product of coordinates in some basis). By Propositions [[§60 Direct Sums and Maschke's Theorem#^prop-60-8|§60.8]] and [[§60 Direct Sums and Maschke's Theorem#^prop-60-9|§60.9]], the averaged form $\langle\ ,\ \rangle$ is an inner product preserved by $G$, so Corollary [[§60 Direct Sums and Maschke's Theorem#^cor-60-7|§60.7]] applies with $V = U^\perp$, the orthogonal complement for $\langle\ ,\ \rangle$. (This rests on WS 14.7 and 14.8, to be presented Fri Nov 6.) Since $|G| \neq 0$ in $\mathbb{R}$, this is the case $k = \mathbb{R}$ of Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-4|§60.4]].

^pf-60-10

*Uses:* [[§60 Direct Sums and Maschke's Theorem#^prop-60-8|§60.8]], [[§60 Direct Sums and Maschke's Theorem#^prop-60-9|§60.9]], [[§60 Direct Sums and Maschke's Theorem#^cor-60-7|§60.7]], [[§60 Direct Sums and Maschke's Theorem#^thm-60-4|§60.4]]
