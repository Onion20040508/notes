---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 61
tags: [group-theory, math493]
---
← [[§60 Direct Sums and Maschke's Theorem]] · ↑ [[· 11 Representations]] · [[§62 Simple Representations]] →

*Source: Lecture and Worksheet 14 (Wed Nov 4); lecture (Fri Nov 6), with WS 14.7–14.8 presented by students. Reference for the linear algebra: Axler, Linear Algebra Done Right, Ch. 6 (orthonormal bases, orthogonal complements). Complex forms: also the MATH 420 slides *Complex inner products*, posted for this course.*

Over $\mathbb{R}$, Maschke's theorem (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-5|§60.5]]) has a geometric proof. If $G$ preserves an inner product, the orthogonal complement of a subrepresentation is again a subrepresentation; and an inner product that $G$ preserves always exists, obtained by averaging any inner product over $G$. The section ends with two consequences of averaging: a finite group acts by orthogonal matrices in a suitable basis, and, over $\mathbb{C}$, by unitary matrices, which preserve a positive definite Hermitian form. The last part sets up these complex forms: sesquilinear and Hermitian forms, their matrices, and orthonormal bases by Gram–Schmidt.

> [!definition] Definition §61.1: Inner Product
> An **inner product** on a real vector space $W$ is a positive definite symmetric bilinear form $\langle\ ,\ \rangle: W \times W \to \mathbb{R}$:
>
> 1. bilinear: linear in each argument when the other is fixed;
> 2. symmetric: $\langle v, w \rangle = \langle w, v \rangle$;
> 3. positive definite: $\langle v, v \rangle > 0$ for $v \neq 0$.
>
> *Source: WS 14*

^def-61-1

> [!remark]- Connections
> - Linear Algebra: [[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]] (inner products over $\mathbb{R}$ and $\mathbb{C}$).

> [!definition] Definition §61.2: Orthogonal Complement
> Let $W$ be a real vector space with an inner product $\langle\ ,\ \rangle$ and $U \subseteq W$ a subspace. The **orthogonal complement** of $U$ is
>
> $$
> U^\perp = \{ w \in W : \langle u, w \rangle = 0 \text{ for all } u \in U \}.
> $$
>
> *Source: WS 14*

^def-61-2

> [!remark]- Connections
> - Linear Algebra: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]].

> [!definition] Definition §61.3: $G$ Preserves an Inner Product
> Let $W$ be a real representation of $G$ with an inner product $\langle\ ,\ \rangle$. $G$ **preserves** $\langle\ ,\ \rangle$ if
>
> $$
> \langle gv, gw \rangle = \langle v, w \rangle \qquad \text{for all } g \in G \text{ and } v, w \in W,
> $$
>
> that is, each $\rho(g)$ is an orthogonal map.
>
> *Source: WS 14*

^def-61-3

> [!remark]- Connections
> - Linear Algebra: an orthogonal map is an isometry, [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]].

> [!theorem] Proposition §61.1: Direct Sum of a Subspace and Its Orthogonal Complement
> Let $W$ be a finite-dimensional real vector space with an inner product and $U \subseteq W$ a subspace. Then $W = U \oplus U^\perp$.
>
> *Source: WS 14.4; board 11/4*

^prop-61-1

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

^pf-61-1

> [!remark]- Connections
> - Linear Algebra: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]] (the same statement) and [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-57|LADR 6.57]] (properties of $P_U$, with the formula used here in part (i)).
> - Functional Analysis: in a Hilbert space the same decomposition holds for closed subspaces, [[§25 Projection and Orthogonal Decomposition#^thm-25-4|556 Thm. §25.4]].

![[m493-60-3.svg]]

*(Not from lecture; figure added.)* The proof of Proposition §60.5 in $\mathbb{R}^3$ with the dot product: $U$ is a plane with orthonormal basis $u_1, u_2$, and $U^\perp$ is the normal line. $P_U(w)$ is the foot of the perpendicular from $w$ to $U$, and the remainder $w - P_U(w)$ (red) is parallel to $U^\perp$.

> [!theorem] Proposition §61.2: Orthogonal Complements of Subrepresentations
> Let $W$ be a real representation of $G$ with an inner product preserved by $G$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-3|§61.3]]), and let $U$ be a subrepresentation. Then $U^\perp$ is a subrepresentation.
>
> *Source: WS 14.5; board 11/4*

^prop-61-2

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

^pf-61-2

> [!theorem] Corollary §61.3: Maschke for Representations Preserving an Inner Product
> Let $W$ be a finite-dimensional real representation of a group $G$ (finite or not) that preserves an inner product on $W$, and let $U$ be a subrepresentation. Then $V = U^\perp$ is a subrepresentation with $W = U \oplus V$.
>
> *Source: WS 14.6*

^cor-61-3

> [!proof]+ Proof
> *(Lecture 11/4.)* $W = U \oplus U^\perp$ by Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-1|§61.1]], and $U^\perp$ is a subrepresentation by Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-2|§61.2]].

^pf-61-3

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-1|§61.1]], [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-2|§61.2]]

**Transcription note (WS 14).** Problem 14.6 says “$W$ preserves an inner product”; “$G$ preserves” is meant (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-3|§61.3]]).

> [!remark] Remark: Physical Meaning
> That $G$ preserves an inner product means that $G$ acts by orthogonal matrices, which preserve lengths and angles: a natural condition for symmetries of objects in space. The lecture noted that physicists also meet symmetries of space-time, which preserve a form that is not positive definite. The remaining step is to show that for a *finite* group such an inner product always exists, even if the given one is not preserved.
>
> *Source: lecture 11/4*

^rem-61-1

> [!definition] Definition §61.4: The Averaged Inner Product
> Let $W$ be a real representation of a finite group $G$, and let $(\ ,\ )$ be any inner product on $W$, not necessarily preserved by $G$. Define
>
> $$
> \langle v, w \rangle := \sum_{g \in G} (gv, gw) \qquad (v, w \in W).
> $$
>
> *Source: WS 14*

^def-61-4

**Transcription note (WS 14).** The worksheet prints the sum as $\sum_{g \in G} \langle gv, gw \rangle$, with the new brackets on both sides; the sum uses the original inner product $(\ ,\ )$.

> [!theorem] Proposition §61.4: Averaging Gives an Inner Product
> $\langle\ ,\ \rangle$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-4|§61.4]]) is an inner product on $W$.
>
> *Source: WS 14.7; presented by students 11/6*

^prop-61-4

> [!proof]+ Proof
> *Idea:* each axiom holds for every term $(gu, gv)$ of the sum, hence for the sum.
>
> We check the three conditions of Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-1|§61.1]]; each follows from the corresponding property of $(\ ,\ )$, term by term.
>
> *Symmetric.* $\langle u, v \rangle = \sum_g (gu, gv) = \sum_g (gv, gu) = \langle v, u \rangle$, by symmetry of $(\ ,\ )$ in each term.
>
> *Positive definite.* Let $u \neq 0$. Each $\rho(g)$ is invertible, so $gu \neq 0$ and $(gu, gu) > 0$ for every $g$. Hence $\langle u, u \rangle = \sum_g (gu, gu)$ is a sum of $|G| \geq 1$ positive numbers, and is positive.
>
> *Bilinear.* For $a, b \in \mathbb{R}$, using first that each $g$ acts linearly and then that $(\ ,\ )$ is bilinear,
>
> $$
> \langle au_1 + bu_2, v \rangle = \sum_g \big(a\,gu_1 + b\,gu_2,\ gv\big) = a\sum_g (gu_1, gv) + b\sum_g (gu_2, gv) = a\langle u_1, v \rangle + b\langle u_2, v \rangle;
> $$
>
> linearity in the second variable follows from this and symmetry.

^pf-61-4

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-1|Def. §61.1]]

> [!theorem] Proposition §61.5: $G$ Preserves the Averaged Inner Product
> $\langle hv, hw \rangle = \langle v, w \rangle$ for all $h \in G$ and $v, w \in W$.
>
> *Source: WS 14.8; presented by a student 11/6*

^prop-61-5

> [!proof]+ Proof
> *Idea:* re-index the sum by $k = gh$.
>
> Let $h \in G$ and $v, w \in W$. Since $g(hv) = (gh)v$,
>
> $$
> \langle hv, hw \rangle = \sum_{g \in G} \big((gh)v, (gh)w\big) = \sum_{k \in G} (kv, kw) = \langle v, w \rangle,
> $$
>
> because as $g$ runs over $G$, so does $k = gh$: right multiplication $g \mapsto gh$ is a bijection $G \to G$, with inverse $k \mapsto kh^{-1}$. Equivalently, the right coset $Gh$ is all of $G$.

^pf-61-5

**Transcription note (board 11/6).** The handwritten notes write $\langle g'u, g'v \rangle = \sum_{g} \langle g'gu, g'gv \rangle = \sum_{k} \langle ku, kv \rangle$, with the new brackets inside the sum and the bijection $g \mapsto hg$. By Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-4|§61.4]] the terms are $\big((gg')u, (gg')v\big)$, with the original inner product, and the re-indexing uses right multiplication by $g'$; left multiplication is also a bijection of $G$, but it is not the one that occurs here.

![[m493-60-4.svg]]

*(Not from lecture; figure added.)* The averaged inner product for $S_3$ acting on $U_2$ (Example [[§59 Representations and Subrepresentations#^ex-59-3|§59.3]]), drawn in the coordinates $x_1, x_2$ of the basis $f_1, f_2$. Take for $(\ ,\ )$ the dot product of coordinates. It is not preserved: the grey ellipses $\{v : (gv, gv) = 1\}$ for $g \neq e$ differ from the red unit circle. The level set $\langle v, v \rangle = 6$ of the averaged form (blue) is mapped to itself by all six matrices of the table in §59, as WS 14.8 asserts.

> [!remark] Remark: Symmetrizing
> Propositions [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]] and [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]] are an instance of a general *symmetrizing* construction: given something with less symmetry than wanted, add it up over the group (in other contexts, multiply or average it), and the result is invariant. They also show the benefit of treating symmetric bilinear forms as objects in their own right, rather than always working with one favourite dot product: the inner product that does the work here is not the one chosen at the start.
>
> *Source: lecture 11/6*

^rem-61-2

> [!theorem] Corollary §61.6: Maschke's Theorem over $\mathbb{R}$
> Let $G$ be finite and $W$ a finite-dimensional real representation of $G$. Every subrepresentation $U$ of $W$ has a complementary subrepresentation $V$, with $W = U \oplus V$.
>
> *Source: WS 14; lecture 11/6*

^cor-61-6

> [!proof]+ Proof
> *Idea:* Make $G$ preserve an inner product by averaging, then take the orthogonal complement.
>
> Choose any inner product on $W$ (for instance, the dot product of coordinates in some basis). By Propositions [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]] and [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]], the averaged form $\langle\ ,\ \rangle$ is an inner product preserved by $G$, so Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-3|§61.3]] applies with $V = U^\perp$, the orthogonal complement for $\langle\ ,\ \rangle$. Since $|G| \neq 0$ in $\mathbb{R}$, this is the case $k = \mathbb{R}$ of Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-5|§60.5]].

^pf-61-6

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]], [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]], [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-3|§61.3]], [[§60 Direct Sums and Maschke's Theorem#^thm-60-5|§60.5]]

> [!theorem] Corollary §61.7: Finite Groups Act by Orthogonal Matrices
> Let $G$ be a finite group and $W$ a finite-dimensional real representation of $G$. Then $G$ preserves some inner product on $W$, and in a suitable basis every $\rho(g)$ is an orthogonal matrix: $M^T M = I$. In words: a finite group may always be taken to act by rotations and reflections.
>
> *Source: lecture 11/6*

^cor-61-7

> [!proof]+ Proof
> *Idea:* write the matrices in a basis that is orthonormal for an inner product $G$ preserves.
>
> Choose any inner product $(\ ,\ )$ on $W$. By Propositions [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]] and [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]], the averaged form $\langle\ ,\ \rangle$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-4|§61.4]]) is an inner product preserved by $G$. Choose a basis $w_1, \ldots, w_n$ of $W$ orthonormal for $\langle\ ,\ \rangle$ (it exists by Gram–Schmidt), so that every $x \in W$ is $x = \sum_k \langle x, w_k \rangle w_k$. Fix $g \in G$ and let $M$ be the matrix of $\rho(g)$ in this basis: column $j$ holds the coordinates of $gw_j$, so $M_{kj} = \langle gw_j, w_k \rangle$. Then, expanding $gw_i$ and $gw_j$ in the orthonormal basis,
>
> $$
> (M^TM)_{ij} = \sum_k M_{ki} M_{kj} = \sum_k \langle gw_i, w_k \rangle \langle gw_j, w_k \rangle = \langle gw_i, gw_j \rangle = \langle w_i, w_j \rangle = \begin{cases} 1 & i = j, \\ 0 & i \neq j, \end{cases}
> $$
>
> where the third equality is bilinearity together with $\langle w_k, w_l \rangle = 0$ for $k \neq l$ and $= 1$ for $k = l$, and the fourth is Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]]. So $M^TM = I$. Preserving an inner product is thus the basis-free way of saying “acting by orthogonal matrices”.

^pf-61-7

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]], [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]], [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-4|Def. §61.4]]

> [!example] Example §61.1: $S_3$ in an Orthonormal Basis
> Return to $S_3$ acting on $\mathbb{R}^3 = U \oplus V$ as in Example [[§60 Direct Sums and Maschke's Theorem#^ex-60-1|§60.1]]: $U = \mathbb{R}(1,1,1)$, and $V = U^\perp$ is the sum-zero plane. $S_3$ preserves the dot product, since it permutes coordinates. The bases of $V$ used so far, $f_1, f_2$ (Example [[§59 Representations and Subrepresentations#^ex-59-3|§59.3]]) and $v_1, v_2$ (Example [[§60 Direct Sums and Maschke's Theorem#^ex-60-1|§60.1]]), are not orthonormal, and neither is the orthogonal basis $(1,-1,0), (1,1,-2)$. Normalizing the last one gives an orthonormal basis of $V$, less convenient for hand computation:
>
> $$
> b_1 = \tfrac{1}{\sqrt{2}}(1, -1, 0), \qquad b_2 = \tfrac{1}{\sqrt{6}}(1, 1, -2).
> $$
>
> In this basis the matrices are orthogonal, as Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-7|§61.7]] predicts:
>
> $$
> \rho_V\big((1\,2)\big) = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \rho_V\big((1\,2\,3)\big) = \begin{pmatrix} -\tfrac12 & -\tfrac{\sqrt3}{2} \\ \tfrac{\sqrt3}{2} & -\tfrac12 \end{pmatrix}.
> $$
>
> $(1\,2)$ swaps the first two coordinates, so it negates $b_1$ and fixes $b_2$: it is the reflection in the line $\mathbb{R}b_2$. For $(1\,2\,3)$, which sends $(x_1, x_2, x_3)$ to $(x_3, x_1, x_2)$: $gb_1 = \tfrac{1}{\sqrt2}(0, 1, -1) = -\tfrac12 b_1 + \tfrac{\sqrt3}{2} b_2$ and $gb_2 = \tfrac{1}{\sqrt6}(-2, 1, 1) = -\tfrac{\sqrt3}{2} b_1 - \tfrac12 b_2$ (the coefficients are the dot products with $b_1$ and $b_2$), so $(1\,2\,3)$ is the rotation by $120^\circ$.
>
> *Source: lecture 11/6; the matrices not from class*

^ex-61-1

![[m493-60-5.svg]]

*(Not from lecture; figure added.)* The plane $V$ of Example [[§61 Invariant Inner Products and Maschke over ℝ#^ex-61-1|§61.1]], drawn in the orthonormal basis $b_1, b_2$. The projections $\bar e_i = e_i - \tfrac13(1,1,1)$ of the standard basis vectors form an equilateral triangle, and $S_3$ acts on $V$ as its symmetry group: the transpositions are the reflections in the three dashed mirror lines (each through the vertex it fixes), the $3$-cycles are the rotations by $\pm 120^\circ$. Rotations and reflections are exactly what orthogonal $2 \times 2$ matrices are.

> [!remark] Remark: Beyond $\mathbb{R}$ and Beyond Finite Groups
> - *Other fields.* Maschke's theorem in full (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-5|§60.5]]) needs only $|G| \neq 0$ in $k$; for $S_3$, of order $6$, this excludes the fields of characteristic $2$ and $3$. Its proof, and counterexamples when $|G| = 0$ in $k$, are on the upcoming problem set.
> - *Compact Lie groups.* Beyond this course, which has no manifold prerequisite: for a compact Lie group the same proof works, with the sum over $G$ replaced by an integral over $G$ against an invariant measure.
>
> *Source: lecture 11/6*

^rem-61-3

> [!example] Example §61.2: The Dot Product on $\mathbb{C}^2$
> Bilinear forms and symmetric bilinear forms make sense over $\mathbb{C}$, with the same definitions as over $\mathbb{R}$. The dot product $x \cdot y = x_1 y_1 + x_2 y_2$ on $\mathbb{C}^2$ is one. Two facts from the real case fail for it.
>
> 1. *A line without an orthonormal basis.* $(1, i) \cdot (1, i) = 1 + i^2 = 0$, so every vector of the line $\mathbb{C}(1, i)$ has length $0$: $\lambda(1, i) \cdot \lambda(1, i) = \lambda^2 \cdot 0 = 0$. No vector $u$ of this line has $u \cdot u = 1$.
> 2. *A symmetric matrix that is not diagonalizable.* The matrix $A = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ satisfies $A^{\mathsf{T}} = A$, and
>
> $$
> \det(xI - A) = \det\begin{pmatrix} x - 1 & -i \\ -i & x + 1 \end{pmatrix} = (x - 1)(x + 1) - (-i)^2 = x^2 - 1 + 1 = x^2,
> $$
>
> so $0$ is its only eigenvalue. The second row of $A$ is $i$ times the first, $(i, -1) = i\,(1, i)$, so $A$ has rank $1$ and its $0$-eigenspace $\ker A$ is $1$-dimensional; it is spanned by $(-i, 1) = -i\,(1, i)$, the line of item 1. A diagonalizable $2 \times 2$ matrix whose only eigenvalue is $0$ is the zero matrix, so $A$ is not diagonalizable. Over $\mathbb{R}$, by contrast, every symmetric matrix is diagonalizable (the real spectral theorem; Axler, Ch. 7).
>
> Sesquilinear forms, defined next, repair the first failure: for the standard Hermitian form, $(1, i)$ has $\langle (1, i), (1, i) \rangle = 2$ (Example [[§61 Invariant Inner Products and Maschke over ℝ#^ex-61-4|§61.4]]). For the second, the complex counterparts of symmetric matrices are the Hermitian matrices $Q = Q^\dagger$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-9|§61.9]]), and $A$ is not one: $A^\dagger = \begin{pmatrix} 1 & -i \\ -i & -1 \end{pmatrix} \neq A$. (Hermitian matrices are diagonalizable, by the complex spectral theorem, Axler, Ch. 7; it is not proved in these notes.)
>
> *Source: MATH 420 slides*

^ex-61-2

> [!definition] Definition §61.5: Sesquilinear Form
> Let $V$ be a complex vector space. A **sesquilinear form** (Latin *sesqui-*, one and a half, as in *sesquicentennial*: linear in one variable and “half linear” in the other) is a map $\langle\ ,\ \rangle: V \times V \to \mathbb{C}$ that is additive in each variable,
>
> $$
> \langle u_1 + u_2, v \rangle = \langle u_1, v \rangle + \langle u_2, v \rangle, \qquad \langle u, v_1 + v_2 \rangle = \langle u, v_1 \rangle + \langle u, v_2 \rangle,
> $$
>
> and satisfies, for $\lambda \in \mathbb{C}$,
>
> $$
> \langle \lambda u, v \rangle = \lambda \langle u, v \rangle, \qquad \langle u, \lambda v \rangle = \bar\lambda \langle u, v \rangle.
> $$
>
> Authors disagree about which variable carries the complex conjugate; here it is the second (the remark *Which Variable Is Conjugate-Linear* at the end of this section compares the two conventions).
>
> *Source: board 11/6; MATH 420 slides*

^def-61-5

> [!definition] Definition §61.6: Hermitian Form
> A sesquilinear form $\langle\ ,\ \rangle$ on a complex vector space $V$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]) is **Hermitian** if $\langle u, v \rangle = \overline{\langle v, u \rangle}$ for all $u, v \in V$. Then $\langle u, u \rangle \in \mathbb{R}$ for every $u$, since $\langle u, u \rangle$ equals its own complex conjugate. Hermitian is the complex counterpart of symmetric.
>
> *Source: board 11/6; MATH 420 slides*

^def-61-6

> [!definition] Definition §61.7: Positive Definite Hermitian Form
> A Hermitian form $\langle\ ,\ \rangle$ on $V$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-6|§61.6]]) is **positive definite** if $\langle u, u \rangle > 0$ for every $u \neq 0$; the inequality makes sense because $\langle u, u \rangle$ is real. A positive definite Hermitian form is the complex counterpart of an inner product (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-1|§61.1]]).
>
> *Source: board 11/6; MATH 420 slides*

^def-61-7

> [!theorem] Lemma §61.8: No Bilinear Form on a Complex Space Is Positive Definite
> Let $V \neq \{0\}$ be a complex vector space. There is no bilinear form $\langle\ ,\ \rangle$ on $V$ with $\langle v, v \rangle$ a positive real number for every $v \neq 0$.
>
> *Source: lecture 11/6*

^lem-61-8

> [!proof]+ Proof
> *Idea:* scaling by $i$ multiplies $\langle v, v \rangle$ by $i^2 = -1$.
>
> Let $\langle\ ,\ \rangle$ be bilinear and $v \neq 0$. Then $iv \neq 0$ and, by bilinearity, $\langle iv, iv \rangle = i^2 \langle v, v \rangle = -\langle v, v \rangle$. So $\langle v, v \rangle$ and $\langle iv, iv \rangle$ cannot both be positive.

^pf-61-8

> [!remark] Remark: Why Not Bilinear, and Unitary Matrices
> A bilinear form on a complex vector space cannot be positive definite (Lemma [[§61 Invariant Inner Products and Maschke over ℝ#^lem-61-8|§61.8]]). Positive definite Hermitian forms are the complex replacement for inner products. The whole theory carries over, with complex conjugates in the right places: orthonormal bases exist (Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-11|§61.11]] below), and the matrices preserving the form are the **unitary** matrices, $\bar M^T M = I$, that is $M^\dagger M = I$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-8|§61.8]]), the analogue of orthogonal matrices (compare the unitary group $U_n(\mathbb{C})$ in the remark *Where the Groups of Lie Type Come From* in [[§56 Simple Groups of Small Order|§56]]). The averaging argument of Propositions [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]] and [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]] works verbatim: a finite group acting on a finite-dimensional complex vector space preserves a positive definite Hermitian form and acts by unitary matrices in a suitable basis, and Maschke's theorem over $\mathbb{C}$ follows in the same way. This is a side topic of the course; the MATH 420 slides on complex inner products, posted on Canvas, are worked out in the rest of this section.
>
> *Source: lecture 11/6*

^rem-61-4

![[m493-61-3.svg]]

*(Not from lecture; figure added.)* Why a bilinear form on a complex vector space cannot be positive definite. Fix $v$ with $B(v, v) = 1$ and multiply $v$ by the unit scalars $e^{i\theta}$. A bilinear $B$ gives $B(e^{i\theta}v, e^{i\theta}v) = e^{2i\theta}$: as $\theta$ goes from $0^\circ$ to $180^\circ$, the value runs once around the unit circle of $\mathbb{C}$, and at $\theta = 90^\circ$, the vector $iv$, it is $-1$. A sesquilinear form gives $\langle e^{i\theta}v, e^{i\theta}v \rangle = e^{i\theta}\,\overline{e^{i\theta}}\,\langle v, v \rangle = 1$ for every $\theta$.

The rest of the section works out the complex theory along the MATH 420 slides on complex inner products: forms on $\mathbb{C}^n$ as matrices, the standard Hermitian form, and orthonormal bases.

> [!definition] Definition §61.8: Conjugate Transpose
> For an $m \times n$ complex matrix $A$, the **conjugate transpose** is the $n \times m$ matrix $A^\dagger = \bar A^{\mathsf{T}}$, obtained by transposing $A$ and replacing each entry by its complex conjugate: $(A^\dagger)_{ij} = \overline{A_{ji}}$. For a column vector $y \in \mathbb{C}^n$, $y^\dagger = (\bar y_1, \ldots, \bar y_n)$ is a row vector.
>
> *Source: MATH 420 slides*

^def-61-8

> [!definition] Definition §61.9: Hermitian Matrix
> A complex $n \times n$ matrix $Q$ is **Hermitian** if $Q = Q^\dagger$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-8|§61.8]]), that is, $Q_{ij} = \overline{Q_{ji}}$ for all $i, j$. Hermitian is the complex counterpart of symmetric; a real matrix is Hermitian exactly when it is symmetric.
>
> *Source: MATH 420 slides*

^def-61-9

> [!theorem] Proposition §61.9: Sesquilinear Forms on $\mathbb{C}^n$ Are Matrices
> Write vectors of $\mathbb{C}^n$ as columns, and let $e_1, \ldots, e_n$ be the standard basis.
>
> 1. For every complex $n \times n$ matrix $Q$, $\langle x, y \rangle = y^\dagger Q x$ is a sesquilinear form on $\mathbb{C}^n$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]). Every sesquilinear form on $\mathbb{C}^n$ is of this form for exactly one $Q$, namely $Q_{ij} = \langle e_j, e_i \rangle$.
> 2. The form $\langle x, y \rangle = y^\dagger Q x$ is Hermitian (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-6|§61.6]]) if and only if $Q$ is a Hermitian matrix (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-9|§61.9]]).
>
> *Source: MATH 420 slides, in the convention of Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]*

^prop-61-9

> [!proof]+ Proof
> *Idea:* expand both vectors in the standard basis; the form is determined by its values $\langle e_j, e_i \rangle$.
>
> *(Not from the slides; filled in.)*
>
> (1) *$y^\dagger Q x$ is sesquilinear.* Written out, $y^\dagger Q x = \sum_{i,j} \bar y_i Q_{ij} x_j$. Each term is additive in $x$ and in $y$, and for $\lambda \in \mathbb{C}$
>
> $$
> \bar y_i Q_{ij} (\lambda x_j) = \lambda\, \bar y_i Q_{ij} x_j, \qquad \overline{\lambda y_i}\, Q_{ij} x_j = \bar\lambda\, \bar y_i Q_{ij} x_j;
> $$
>
> so the sum satisfies the conditions of Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]], with $x$ as the first variable and $y$ as the second.
>
> *Every sesquilinear form is of this form.* Let $\langle\ ,\ \rangle$ be sesquilinear and put $Q_{ij} = \langle e_j, e_i \rangle$. For $x = \sum_j x_j e_j$ and $y = \sum_i y_i e_i$, additivity in each variable, linearity in the first and conjugate-linearity in the second give
>
> $$
> \langle x, y \rangle = \Big\langle \sum_j x_j e_j,\ \sum_i y_i e_i \Big\rangle = \sum_{i,j} x_j\, \bar y_i\, \langle e_j, e_i \rangle = \sum_{i,j} \bar y_i Q_{ij} x_j = y^\dagger Q x.
> $$
>
> *Uniqueness.* If also $\langle x, y \rangle = y^\dagger Q' x$ for all $x, y$, then $Q'_{ij} = e_i^\dagger Q' e_j = \langle e_j, e_i \rangle = Q_{ij}$ for all $i, j$, so $Q' = Q$.
>
> (2) By (1), $Q_{ij} = \langle e_j, e_i \rangle$. If the form is Hermitian, then for all $i, j$
>
> $$
> Q_{ij} = \langle e_j, e_i \rangle = \overline{\langle e_i, e_j \rangle} = \overline{Q_{ji}} = (Q^\dagger)_{ij},
> $$
>
> so $Q = Q^\dagger$. Conversely, let $Q = Q^\dagger$, i.e. $\overline{Q_{ij}} = Q_{ji}$. Then for all $x, y$
>
> $$
> \overline{\langle y, x \rangle} = \overline{\sum_{i,j} \bar x_i Q_{ij} y_j} = \sum_{i,j} x_i\, \overline{Q_{ij}}\, \bar y_j = \sum_{i,j} \bar y_j\, Q_{ji}\, x_i = y^\dagger Q x = \langle x, y \rangle,
> $$
>
> where the fourth equality is the formula $y^\dagger Q x = \sum_{a,b} \bar y_a Q_{ab} x_b$ with $a = j$, $b = i$. So the form is Hermitian.

^pf-61-9

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|Def. §61.5]]

> [!example] Example §61.3: A Hermitian Matrix
> The matrix
>
> $$
> Q = \begin{pmatrix} 3 & 5 + 3i & -2 + 3i \\ 5 - 3i & 7 & -4i \\ -2 - 3i & 4i & 11 \end{pmatrix}
> $$
>
> is Hermitian (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-9|§61.9]]): the diagonal entries $3, 7, 11$ are real, and each entry below the diagonal is the conjugate of its mirror image above it, $\overline{5 + 3i} = 5 - 3i$, $\overline{-2 + 3i} = -2 - 3i$, $\overline{-4i} = 4i$. So $\langle x, y \rangle = y^\dagger Q x$ is a Hermitian form on $\mathbb{C}^3$ (Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-9|§61.9]]). The diagonal of every Hermitian matrix is real, since $Q_{ii} = \overline{Q_{ii}}$.
>
> Hermitian does not imply positive definite. For $x = (5 + 3i, -3, 0)$ only the upper left $2 \times 2$ block of $Q$ contributes, and its two off-diagonal terms $\bar x_1 Q_{12} x_2$ and $\bar x_2 Q_{21} x_1$ are complex conjugates of each other:
>
> $$
> \langle x, x \rangle = x^\dagger Q x = 3\,|5 + 3i|^2 + 7 \cdot |{-3}|^2 + 2 \operatorname{Re}\!\big(\overline{(5 + 3i)}\,(5 + 3i)(-3)\big) = 3 \cdot 34 + 63 - 204 = -39 < 0.
> $$
>
> *Source: MATH 420 slides; the vector $x$ not from the slides*

^ex-61-3

> [!example] Example §61.4: The Standard Hermitian Form on $\mathbb{C}^n$
> The standard positive definite Hermitian form on $\mathbb{C}^n$ is
>
> $$
> \langle p, q \rangle = p_1 \bar q_1 + p_2 \bar q_2 + \cdots + p_n \bar q_n = q^\dagger p,
> $$
>
> the form of Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-9|§61.9]] with $Q = I$; it is Hermitian since $I^\dagger = I$. Writing $p_k = x_k + y_k i$ with $x_k, y_k \in \mathbb{R}$,
>
> $$
> \langle p, p \rangle = (x_1 + y_1 i)(x_1 - y_1 i) + \cdots + (x_n + y_n i)(x_n - y_n i) = x_1^2 + y_1^2 + \cdots + x_n^2 + y_n^2 \geq 0,
> $$
>
> with equality only if every $x_k$ and $y_k$ is $0$, i.e. $p = 0$. So the form is positive definite, and $\langle p, p \rangle$ is the squared Euclidean length of $p$ read as the vector $(x_1, y_1, \ldots, x_n, y_n) \in \mathbb{R}^{2n}$. The standard basis is orthonormal. The vector $(1, i)$ of Example [[§61 Invariant Inner Products and Maschke over ℝ#^ex-61-2|§61.2]], of length $0$ for the dot product, has
>
> $$
> \langle (1, i), (1, i) \rangle = 1 \cdot \bar 1 + i \cdot \bar i = 1 + i(-i) = 2,
> $$
>
> so $\tfrac{1}{\sqrt2}(1, i)$ is an orthonormal basis of the line $\mathbb{C}(1, i)$.
>
> *Source: MATH 420 slides, there written $\bar p_1 q_1 + \cdots + \bar p_n q_n$ (see the remark *Which Variable Is Conjugate-Linear* below)*

^ex-61-4

> [!theorem] Proposition §61.10: Orthogonal Projection for a Positive Definite Hermitian Form
> Let $V$ be a complex vector space with a positive definite Hermitian form $\langle\ ,\ \rangle$, and let $u_1, \ldots, u_k$ be an orthogonal basis of a subspace $L$: the $u_i$ are nonzero and $\langle u_i, u_j \rangle = 0$ for $i \neq j$. Define
>
> $$
> P_L(v) = \sum_{i=1}^k \frac{\langle v, u_i \rangle}{\langle u_i, u_i \rangle}\, u_i \qquad (v \in V).
> $$
>
> 1. $P_L: V \to V$ is linear, its image lies in $L$, and $P_L(v) = v$ for $v \in L$.
> 2. $v - P_L(v)$ is orthogonal to $L$: $\langle v - P_L(v), u \rangle = 0$ for every $u \in L$.
>
> This is the formula of the real case (proof of Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-1|§61.1]]), written for an orthogonal rather than an orthonormal basis.
>
> *Source: MATH 420 slides, in the convention of Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]*

^prop-61-10

> [!proof]+ Proof
> *Idea:* the coefficient of $u_i$ is chosen so that $v - P_L(v)$ has no $u_i$-component; the other $u_j$ do not interfere, being orthogonal to $u_i$.
>
> *(Not from the slides; filled in.)* The denominators $\langle u_i, u_i \rangle$ are positive real numbers, since $u_i \neq 0$ and the form is positive definite (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-7|§61.7]]).
>
> (1) Each coefficient $v \mapsto \langle v, u_i \rangle / \langle u_i, u_i \rangle$ is linear in $v$, because the form is linear in its first variable (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]); hence $P_L$ is linear, and $P_L(v)$, a linear combination of $u_1, \ldots, u_k$, lies in $L$. If $v = \sum_j a_j u_j \in L$, then by orthogonality $\langle v, u_i \rangle = \sum_j a_j \langle u_j, u_i \rangle = a_i \langle u_i, u_i \rangle$, so the coefficient of $u_i$ in $P_L(v)$ is $a_i$, and $P_L(v) = v$.
>
> (2) For each $j$, by linearity in the first variable and $\langle u_i, u_j \rangle = 0$ for $i \neq j$,
>
> $$
> \langle v - P_L(v), u_j \rangle = \langle v, u_j \rangle - \sum_{i=1}^k \frac{\langle v, u_i \rangle}{\langle u_i, u_i \rangle} \langle u_i, u_j \rangle = \langle v, u_j \rangle - \frac{\langle v, u_j \rangle}{\langle u_j, u_j \rangle} \langle u_j, u_j \rangle = 0.
> $$
>
> A general $u \in L$ is $u = \sum_j c_j u_j$, and by conjugate-linearity in the second variable $\langle v - P_L(v), u \rangle = \sum_j \bar c_j \langle v - P_L(v), u_j \rangle = 0$.

^pf-61-10

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-7|Def. §61.7]], [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|Def. §61.5]]

> [!theorem] Proposition §61.11: Orthonormal Bases for a Positive Definite Hermitian Form
> Let $V$ be a finite-dimensional complex vector space with a positive definite Hermitian form $\langle\ ,\ \rangle$. Then $V$ has an orthonormal basis, i.e. a basis $w_1, \ldots, w_n$ with $\langle w_i, w_j \rangle = 1$ if $i = j$ and $0$ otherwise. It is obtained from any basis by the Gram–Schmidt algorithm, exactly as over $\mathbb{R}$.
>
> *Source: MATH 420 slides*

^prop-61-11

> [!proof]+ Proof
> *Idea:* subtract from each basis vector its projection onto the span of the previous ones, then scale to length $1$.
>
> *(Not from the slides; filled in.)* If $V = \{0\}$, the empty basis is orthonormal. Otherwise let $v_1, \ldots, v_n$ be a basis of $V$ and define recursively
>
> $$
> u_1 = v_1, \qquad u_k = v_k - P_{L_{k-1}}(v_k) \quad (2 \leq k \leq n), \qquad \text{where } L_{k-1} = \operatorname{span}(u_1, \ldots, u_{k-1})
> $$
>
> and $P_{L_{k-1}}$ is the projection of Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-10|§61.10]]. We show by induction on $k$ that $u_1, \ldots, u_k$ are nonzero and pairwise orthogonal, with $\operatorname{span}(u_1, \ldots, u_k) = \operatorname{span}(v_1, \ldots, v_k)$. (The statement for $k - 1$ makes $u_1, \ldots, u_{k-1}$ an orthogonal basis of $L_{k-1}$, so $P_{L_{k-1}}$ is defined.)
>
> *$k = 1$.* $u_1 = v_1 \neq 0$, since $v_1$ belongs to a basis.
>
> *From $k - 1$ to $k$.* By Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-10|§61.10]](2), $u_k = v_k - P_{L_{k-1}}(v_k)$ is orthogonal to $L_{k-1}$, so $\langle u_k, u_i \rangle = 0$ for $i < k$, and $\langle u_i, u_k \rangle = \overline{\langle u_k, u_i \rangle} = 0$ by the Hermitian property. Next, $P_{L_{k-1}}(v_k)$ lies in $L_{k-1}$, which equals $\operatorname{span}(v_1, \ldots, v_{k-1})$ by the induction hypothesis; so $u_k \in \operatorname{span}(v_1, \ldots, v_k)$ and $v_k = u_k + P_{L_{k-1}}(v_k) \in \operatorname{span}(u_1, \ldots, u_k)$, which gives $\operatorname{span}(u_1, \ldots, u_k) = \operatorname{span}(v_1, \ldots, v_k)$. Finally, if $u_k = 0$, then $v_k = P_{L_{k-1}}(v_k)$ would lie in $\operatorname{span}(v_1, \ldots, v_{k-1})$, contradicting the linear independence of $v_1, \ldots, v_k$; so $u_k \neq 0$.
>
> *Normalizing.* Each $\langle u_k, u_k \rangle$ is a positive real number (positive definiteness), so $w_k = u_k / \sqrt{\langle u_k, u_k \rangle}$ is defined. For a real scalar $r$, $\langle r u, r u \rangle = r \bar r \langle u, u \rangle = r^2 \langle u, u \rangle$, so $\langle w_k, w_k \rangle = 1$; scaling keeps $\langle w_i, w_j \rangle = 0$ for $i \neq j$. The $w_1, \ldots, w_n$ span $\operatorname{span}(v_1, \ldots, v_n) = V$, and $n$ vectors spanning the $n$-dimensional space $V$ form a basis.

^pf-61-11

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-10|§61.10]]

![[m493-61-4.svg]]

*(Not from lecture; figure added.)* One step of the Gram–Schmidt algorithm in the proof of Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-11|§61.11]]: $u_2$ is $v_2$ minus its projection onto the span of $u_1$, so it is orthogonal to $u_1$, and $u_1, u_2$ span the same subspace as $v_1, v_2$. The picture is drawn in a real plane; over $\mathbb{C}$ the coefficient $\langle v_2, u_1 \rangle / \langle u_1, u_1 \rangle$ is a complex number, and $\operatorname{span}(u_1)$ is a complex line.

> [!remark] Remark: Which Variable Is Conjugate-Linear
> These notes follow the board of 11/6: $\langle\ ,\ \rangle$ is linear in the first variable and conjugate-linear in the second (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]). The MATH 420 slides on complex inner products, posted for this course, use the opposite convention: a form $B$ with $B(v, cw) = c\,B(v, w)$ and $B(cv, w) = \bar c\,B(v, w)$. The two are related by $B(v, w) = \langle w, v \rangle$, and the translation changes nothing else:
> - $B$ is Hermitian, or positive definite, exactly when $\langle\ ,\ \rangle$ is, and for Hermitian forms $B(v, w) = 0$ exactly when $\langle v, w \rangle = 0$, so orthogonality means the same;
> - on $\mathbb{C}^n$ the two use the same matrix $Q$: $B(x, y) = x^\dagger Q y$ and $\langle x, y \rangle = y^\dagger Q x$ (Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-9|§61.9]]);
> - the standard form of Example [[§61 Invariant Inner Products and Maschke over ℝ#^ex-61-4|§61.4]] is $B(p, q) = \bar p_1 q_1 + \cdots + \bar p_n q_n$;
> - the coefficient $\langle v, u_i \rangle$ in the projection of Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-10|§61.10]] is $B(u_i, v)$.
>
> Both conventions are common. Linear in the first variable (as here, and in Axler) is more usual in pure mathematics; linear in the second is more usual in applied mathematics, physics and engineering. Many texts write $A^\ast$ for $A^\dagger$, and $\ast$ also denotes the dual space $V^\ast$, so the meaning of $\ast$ has to be read from the context.
>
> *Source: MATH 420 slides*

^rem-61-5

> [!remark]- Connections
> - Linear Algebra: Axler's inner product ([[§20 Inner Products and Norms#^ladr-6-2|LADR 6.2]]) is a positive definite Hermitian form in the convention of Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]] (linear in the first slot). The Gram–Schmidt procedure ([[§21 Orthonormal Bases#^ladr-6-32|LADR 6.32]]) and the existence of orthonormal bases ([[§21 Orthonormal Bases#^ladr-6-35|LADR 6.35]]) are Proposition [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-11|§61.11]].
> - Spectral theorems quoted in Example [[§61 Invariant Inner Products and Maschke over ℝ#^ex-61-2|§61.2]]: real symmetric matrices ([[§24 Spectral Theorem#^ladr-7-29|LADR 7.29]]) and complex normal, in particular Hermitian, matrices ([[§24 Spectral Theorem#^ladr-7-31|LADR 7.31]]) are diagonalizable in an orthonormal basis.
