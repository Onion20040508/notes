---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 61
tags: [group-theory, math493]
---
← [[§60 Direct Sums and Maschke's Theorem]] · ↑ [[· 11 Representations]] · [[§62 Simple Representations]] →

*Source: Lecture and Worksheet 14 (Wed Nov 4); lecture (Fri Nov 6), with WS 14.7–14.8 presented by students. Reference for the linear algebra: Axler, Linear Algebra Done Right, Ch. 6 (orthonormal bases, orthogonal complements).*

Over $\mathbb{R}$, Maschke's theorem (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-4|§60.4]]) has a geometric proof. If $G$ preserves an inner product, the orthogonal complement of a subrepresentation is again a subrepresentation; and an inner product that $G$ preserves always exists, obtained by averaging any inner product over $G$. The section ends with two consequences of averaging: a finite group acts by orthogonal matrices in a suitable basis, and, over $\mathbb{C}$, by unitary matrices, which preserve a positive definite Hermitian form.

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
> Choose any inner product on $W$ (for instance, the dot product of coordinates in some basis). By Propositions [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]] and [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]], the averaged form $\langle\ ,\ \rangle$ is an inner product preserved by $G$, so Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-3|§61.3]] applies with $V = U^\perp$, the orthogonal complement for $\langle\ ,\ \rangle$. Since $|G| \neq 0$ in $\mathbb{R}$, this is the case $k = \mathbb{R}$ of Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-4|§60.4]].

^pf-61-6

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]], [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]], [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-3|§61.3]], [[§60 Direct Sums and Maschke's Theorem#^thm-60-4|§60.4]]

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
> - *Other fields.* Maschke's theorem in full (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-4|§60.4]]) needs only $|G| \neq 0$ in $k$; for $S_3$, of order $6$, this excludes the fields of characteristic $2$ and $3$. Its proof, and counterexamples when $|G| = 0$ in $k$, are on the upcoming problem set.
> - *Compact Lie groups.* Beyond this course, which has no manifold prerequisite: for a compact Lie group the same proof works, with the sum over $G$ replaced by an integral over $G$ against an invariant measure.
>
> *Source: lecture 11/6*

^rem-61-3

> [!definition] Definition §61.5: Sesquilinear Form
> Let $V$ be a complex vector space. A **sesquilinear form** (“one and a half times linear”) is a map $\langle\ ,\ \rangle: V \times V \to \mathbb{C}$ that is additive in each variable,
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
> Authors disagree about which variable carries the complex conjugate; here it is the second.
>
> *Source: board 11/6*

^def-61-5

> [!definition] Definition §61.6: Hermitian Form
> A sesquilinear form $\langle\ ,\ \rangle$ on a complex vector space $V$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-5|§61.5]]) is **Hermitian** if $\langle u, v \rangle = \overline{\langle v, u \rangle}$ for all $u, v \in V$. Then $\langle u, u \rangle \in \mathbb{R}$ for every $u$, since $\langle u, u \rangle$ equals its own complex conjugate. Hermitian is the complex counterpart of symmetric.
>
> *Source: board 11/6*

^def-61-6

> [!definition] Definition §61.7: Positive Definite Hermitian Form
> A Hermitian form $\langle\ ,\ \rangle$ on $V$ (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-6|§61.6]]) is **positive definite** if $\langle u, u \rangle > 0$ for every $u \neq 0$; the inequality makes sense because $\langle u, u \rangle$ is real. A positive definite Hermitian form is the complex counterpart of an inner product (Definition [[§61 Invariant Inner Products and Maschke over ℝ#^def-61-1|§61.1]]).
>
> *Source: board 11/6*

^def-61-7

> [!remark] Remark: Why Not Bilinear, and Unitary Matrices
> A bilinear form on a complex vector space cannot be positive definite: $\langle iv, iv \rangle = i^2 \langle v, v \rangle = -\langle v, v \rangle$, so $\langle v, v \rangle$ and $\langle iv, iv \rangle$ cannot both be positive. Positive definite Hermitian forms are the complex replacement for inner products. The whole theory carries over, with complex conjugates in the right places: orthonormal bases exist, and the matrices preserving the form are the **unitary** matrices, $\bar M^T M = I$, the analogue of orthogonal matrices (compare the unitary group $U_n(\mathbb{C})$ in the remark *Where the Groups of Lie Type Come From* in [[§56 Simple Groups of Small Order|§56]]). The averaging argument of Propositions [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-4|§61.4]] and [[§61 Invariant Inner Products and Maschke over ℝ#^prop-61-5|§61.5]] works verbatim: a finite group acting on a finite-dimensional complex vector space preserves a positive definite Hermitian form and acts by unitary matrices in a suitable basis, and Maschke's theorem over $\mathbb{C}$ follows in the same way. This is a side topic of the course; notes on sesquilinear forms are linked on the course Canvas site.
>
> *Source: lecture 11/6*

^rem-61-4
