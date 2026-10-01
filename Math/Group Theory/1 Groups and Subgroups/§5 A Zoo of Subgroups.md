---
type: section
subject: "[[Group Theory]]"
chapter: 1
section: 5
tags: [group-theory, math493]
---
← [[§4 Subgroups]] · ↑ [[· 1 Groups and Subgroups]] · [[§6 Divisibility and Congruence]] →

*Source: WS 1.7*

*Reference: Pinter Ch. 5, exercises.*

**WS 1.7** asks us to list as many subgroups as we can of $\mathbb{Z}$, $\mathbb{Z}^2$, $\mathbb{R}$, $S_3$, $GL_2(\mathbb{R})$, and $GL_3(\mathbb{R})$. For $\mathbb{Z}$, $\mathbb{R}$, and $S_3$ ([[§13 Subgroups of S₃#^prop-13-1|§13.1]]) we can do better than list subgroups: we can *classify* them completely; for $\mathbb{Z}^2$ and $GL_n(\mathbb{R})$ we give lists.

## Subgroups of $\mathbb{Z}$: Complete Classification

> [!theorem] Proposition §5.1: Subgroups of $\mathbb{Z}$
> The subgroups of $(\mathbb{Z}, +)$ are exactly the sets
>
> $$ n\mathbb{Z} = \{nk : k \in \mathbb{Z}\}, \qquad n = 0, 1, 2, 3, \ldots, $$
>
> and these are pairwise distinct ($n\mathbb{Z} = \langle n \rangle$ in additive notation, with $0\mathbb{Z} = \{0\}$ and $1\mathbb{Z} = \mathbb{Z}$).
>
> *Source: WS 1.7*

^prop-5-1

> [!proof]+ Proof
> **Each $n\mathbb{Z}$ is a subgroup:** it is $\langle n \rangle$ in additive notation, so this is [[§4 Subgroups#^prop-4-5|WS 1.5]] (or directly: $0 = n \cdot 0$; $-(nk) = n(-k)$; $nk + nl = n(k + l)$).
>
> **Every subgroup has this form:** Let $H \leq \mathbb{Z}$. If $H = \{0\}$, then $H = 0\mathbb{Z}$. Otherwise $H$ contains some $h \neq 0$; since $-h \in H$ as well, $H$ contains a positive integer. By [[§1 The Set ℕ of Natural Numbers#^thm-1-2|well-ordering]], let $n$ be the *smallest* positive element of $H$. Then $n\mathbb{Z} \subseteq H$ (closure under addition and negation, by induction). Conversely, let $h \in H$. By the [[§6 Divisibility and Congruence#^lem-6-1|division algorithm]], $h = qn + r$ with $0 \leq r < n$. Then
>
> $$ r = h - qn \in H $$
>
> (since $h \in H$ and $qn \in n\mathbb{Z} \subseteq H$, and $H$ is closed under subtraction). But $0 \leq r < n$ and $n$ is the smallest *positive* element of $H$, so $r = 0$, i.e. $h = qn \in n\mathbb{Z}$. Hence $H = n\mathbb{Z}$.
>
> **Distinctness:** for $n \geq 1$, $n$ is the smallest positive element of $n\mathbb{Z}$, and $0\mathbb{Z}$ has no positive elements.

^pf-5-1

*Uses:* [[§4 Subgroups#^prop-4-5|§4.5]], [[§4 Subgroups#^prop-4-6|§4.6]], [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§6 Divisibility and Congruence#^lem-6-1|§6.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-2|451 §1.2]]

> [!remark]- Connections
> - Generalized from ℤ to every cyclic group: [[§17 Cyclic Groups#^thm-17-4|Subgroups of Cyclic Groups Are Cyclic]]; the same division-algorithm argument is sketched in MATH 590, [[§21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 Proposition §21.1]] (2).

> [!theorem] Corollary §5.2: Generated Subgroups of $\mathbb{Z}$, and Bézout
> Let $a, b \in \mathbb{Z}$, not both zero, and let $d = \gcd(a, b)$. Then
>
> $$ \langle a, b \rangle = a\mathbb{Z} + b\mathbb{Z} = d\mathbb{Z}. $$
>
> In particular, there exist $x, y \in \mathbb{Z}$ with $ax + by = d$ (**Bézout's identity**), and $\langle a, b \rangle = \mathbb{Z}$ if and only if $\gcd(a, b) = 1$.
>
> *Source: cf. Pinter Ch. 5, Ex. E; Ch. 22, Thm. 3*

^cor-5-2

> [!proof]+ Proof
> In additive notation, the [[§4 Subgroups#^def-4-4|words of the generated subgroup]] are sums of copies of $\pm a$ and $\pm b$, so $\langle a, b \rangle = \{ax + by : x, y \in \mathbb{Z}\} = a\mathbb{Z} + b\mathbb{Z}$. This is a nonzero subgroup of $\mathbb{Z}$, so by [[§5 A Zoo of Subgroups#^prop-5-1|the classification]] it equals $e\mathbb{Z}$ for a unique $e > 0$. We show $e = d$. Since $a, b \in e\mathbb{Z}$, $e$ is a common divisor of $a$ and $b$, so $e \leq d$. Since $e \in a\mathbb{Z} + b\mathbb{Z}$, write $e = ax + by$; as $d \mid a$ and $d \mid b$, $d \mid e$, so $d \leq e$. Hence $e = d$, and $d = ax + by$ is Bézout. Finally $d\mathbb{Z} = \mathbb{Z}$ iff $d = 1$.

^pf-5-2

*Uses:* [[§4 Subgroups#^def-4-4|Def. §4.4]], [[§5 A Zoo of Subgroups#^prop-5-1|§5.1]], [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - Bézout is what makes the [[§8 Invertibility and Unit Groups#^prop-8-1|Invertibility Criterion]] and [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's Lemma]] work.
> - Linear-algebra analogue of $a\mathbb{Z} + b\mathbb{Z}$: [[§3 Subspaces#^ladr-1-40|Sum of subspaces is the smallest containing subspace]].

> [!remark] Remark: The Dependency of $U_n$ on Bézout
> The proof that $U_n$ is a group ([[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]]) invoked Bézout's identity. [[§5 A Zoo of Subgroups#^cor-5-2|Generated Subgroups of ℤ, and Bézout]] derives Bézout from the [[§5 A Zoo of Subgroups#^prop-5-1|classification of subgroups]] of $\mathbb{Z}$, which used only the [[§6 Divisibility and Congruence#^lem-6-1|division algorithm]] — so the dependency chain is: [[§1 The Set ℕ of Natural Numbers#^thm-1-2|well-ordering]] $\Rightarrow$ division algorithm $\Rightarrow$ subgroups of $\mathbb{Z}$ $\Rightarrow$ Bézout $\Rightarrow$ $U_n$ is a group. Pinter's Chapter 5 exercise “show $\mathbb{Z}$ is generated by $5$ and $7$” is the case $\gcd(5, 7) = 1$.

^rem-5-1

> [!remark]- Connections
> - The full chain, extended to Euclid, unique factorization and CRT: [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^rem-9-1|The Dependency Chain in ℤ]].

## Subgroups of $\mathbb{Z}^2$

> [!example] Example §5.1: Subgroups of $\mathbb{Z}^2$: a Partial List
> Unlike $\mathbb{Z}$, one generator no longer suffices. Some families:
> - The trivial subgroup $\{(0, 0)\}$ and $\mathbb{Z}^2$ itself.
> - **Cyclic subgroups** $\langle (a, b) \rangle = \{(ka, kb) : k \in \mathbb{Z}\}$: e.g. the diagonal $\langle (1, 1) \rangle$, or $\langle (2, 3) \rangle$. These are “lines of lattice points.”
> - **Products** $m\mathbb{Z} \times n\mathbb{Z}$ for $m, n \geq 0$ (a direct product of subgroups of the factors is a subgroup of the [[§3 Basic Examples of Groups#^def-3-2|direct product]] — check componentwise): e.g. $2\mathbb{Z} \times 3\mathbb{Z}$, $\mathbb{Z} \times \{0\}$ (the “$x$-axis”), $\{0\} \times 5\mathbb{Z}$.
> - **Rank-two lattices not of product form:** e.g. $\langle (2, 0), (1, 1) \rangle$, or
>
>   $$ \langle (1, 1), (1, -1) \rangle = \{(x, y) \in \mathbb{Z}^2 : x \equiv y \pmod 2\}. $$
>
>   *Verification of the last equality:* $a(1,1) + b(1,-1) = (a + b, a - b)$, and $(a+b) - (a-b) = 2b$ is even; conversely, if $x \equiv y \pmod 2$, take $a = \frac{x + y}{2}$, $b = \frac{x - y}{2} \in \mathbb{Z}$. This subgroup (index $2$ in $\mathbb{Z}^2$, the “checkerboard sublattice”) is not a product $m\mathbb{Z} \times n\mathbb{Z}$: it contains $(1,1)$ but not $(1, 0)$, while any product containing $(1,1)$ has $m = n = 1$.
>
> *Source: WS 1.7*

^ex-5-1

![[m493-5-1.svg]]
*The checkerboard subgroup $\{(x,y) \in \mathbb{Z}^2 : x \equiv y \pmod 2\} = \langle (1,1), (1,-1) \rangle$ (blue points) inside $\mathbb{Z}^2$, with its two generators in red. The hollow points are its translate by $(1,0)$, so it has index $2$; it contains $(1,1)$ but not $(1,0)$, which is why it is not a product $m\mathbb{Z} \times n\mathbb{Z}$.*

> [!remark] Remark: Forward Pointer: Rank
> It is a theorem (not yet available to us) that *every* subgroup of $\mathbb{Z}^2$ is generated by at most two elements — more generally, every subgroup of $\mathbb{Z}^n$ is free abelian of rank $\leq n$. This is part of the structure theory of finitely generated abelian groups, later in the course. The checkerboard sublattice above is, incidentally, exactly the index-2 bipartite decomposition underlying the quadrupole checkerboard analysis in the thesis — the same lattice, in its natural habitat.

^rem-5-2

## Subgroups of $\mathbb{R}$

> [!example] Example §5.2: Subgroups of $\mathbb{R}$: a List
> Examples of subgroups of $(\mathbb{R}, +)$:
> - $\{0\}$ and $\mathbb{R}$;
> - **cyclic subgroups** $a\mathbb{Z} = \{ak : k \in \mathbb{Z}\}$ for any real $a$ (e.g. $\mathbb{Z}$, $\pi\mathbb{Z}$);
> - $\mathbb{Q}$, and intermediate rings such as the dyadic rationals $\mathbb{Z}[\tfrac12] = \{m/2^k : m \in \mathbb{Z},\, k \geq 0\}$ (closed under subtraction: common denominators);
> - **two-generator subgroups** $a\mathbb{Z} + b\mathbb{Z} = \{am + bn\}$, e.g. $\mathbb{Z} + \sqrt{2}\,\mathbb{Z}$.
>
> *Source: WS 1.7*

^ex-5-2

> [!theorem] Proposition §5.3: Dichotomy for Subgroups of $\mathbb{R}$
> Let $H$ be a subgroup of $(\mathbb{R}, +)$ with $H \neq \{0\}$. Then exactly one of the following holds:
> 1. $H = a\mathbb{Z}$ for a unique $a > 0$; or
> 2. $H$ is dense in $\mathbb{R}$ (every open interval contains a point of $H$).

^prop-5-3

> [!proof]+ Proof
> Since $H \neq \{0\}$, pick $h \in H \setminus \{0\}$; as $-h \in H$, the set $P = \{h \in H : h > 0\}$ is nonempty and bounded below by $0$. Let $a = \inf P \geq 0$.
>
> **Case $a > 0$.** First, $a \in H$: if not, then $a \notin P$, so by definition of infimum there is $h \in P$ with $a < h < 2a$, and then again some $h' \in P$ with $a < h' < h$. Now $h - h' \in H$ and $0 < h - h' < 2a - a = a$, so $h - h' \in P$ is a positive element of $H$ smaller than $a = \inf P$ — contradiction. So $a \in H$, hence $a\mathbb{Z} \subseteq H$. Conversely, given $h \in H$, set $q = \lfloor h/a \rfloor$, so $r = h - qa \in [0, a)$. Since $h \in H$ and $qa \in a\mathbb{Z} \subseteq H$, we get $r \in H$; if $r > 0$ it would be an element of $P$ below $\inf P$, so $r = 0$ and $h = qa$. Hence $H = a\mathbb{Z}$. Uniqueness: $a$ is the smallest positive element.
>
> **Case $a = 0$.** Let $(x - \varepsilon, x + \varepsilon)$ be any open interval. Since $\inf P = 0$, choose $h \in P$ with $0 < h < \varepsilon$, and set $q = \lfloor x/h \rfloor$. Then $qh \in H$ and $x - qh \in [0, h) \subseteq [0, \varepsilon)$, so $qh \in (x - \varepsilon, x + \varepsilon)$. Hence $H$ is dense.
>
> The two cases are exclusive: $a\mathbb{Z}$ is not dense (it misses $(0, a)$).

^pf-5-3

*Uses:* [[§4 Subgroups#^def-4-1|Def. §4.1]], [[§4 Subgroups#^prop-4-6|§4.6]], [[§4 The Completeness Axiom#^cor-4-4|451 §4.4]], [[§4 The Completeness Axiom#^prop-4-3|451 §4.3]], [[§4 The Completeness Axiom#^thm-4-5|451 §4.5]]

> [!remark]- Connections
> - $\mathbb{Q}$ is a subgroup of the second kind: [[§4 The Completeness Axiom#^thm-4-7|Density of ℚ in ℝ]] (MATH 451).

> [!example] Example §5.3: $\mathbb{Z} + \sqrt{2}\,\mathbb{Z}$ Is Dense
> [[§5 A Zoo of Subgroups#^prop-5-3|The dichotomy]] has teeth: $H = \mathbb{Z} + \sqrt{2}\,\mathbb{Z}$ is not cyclic — if $H = a\mathbb{Z}$, then $1 = am$ and $\sqrt{2} = an$ for integers $m, n$, whence $\sqrt{2} = n/m \in \mathbb{Q}$, [[§2 The Set ℚ of Rational Numbers#^thm-2-1|contradiction]] — so it is dense in $\mathbb{R}$. (This density is the additive shadow of the equidistribution of $n\sqrt{2} \bmod 1$, and the same mechanism behind quasiperiodic structures.)

^ex-5-3

![[m493-5-2.svg]]
*The two cases of the dichotomy. Top: if $a = \inf P > 0$, then $a \in H$ and $H = a\mathbb{Z}$ is evenly spaced; the gap $(0, a)$ (red) holds no point of $H$, since a point there would be a positive element below $\inf P$. Bottom: $H = \mathbb{Z} + \sqrt2\,\mathbb{Z}$ (the points $m + n\sqrt2$ with $\vert n \vert \leq 6$ are shown) contains arbitrarily small positive elements such as $h = 3 - 2\sqrt2 \approx 0.17$. Its multiples $qh$ march along in steps $h < \varepsilon$, so one of them, $qh$ with $q = \lfloor x/h \rfloor$ (red dot), lands in any interval $(x - \varepsilon, x + \varepsilon)$.*

## Subgroups of $GL_2(\mathbb{R})$ and $GL_3(\mathbb{R})$

> [!example] Example §5.4: Subgroups of $GL_2(\mathbb{R})$ and $GL_3(\mathbb{R})$
> Here classification is hopeless; we settle for a long list. Each item comes with its closure/inverse verification in parentheses; $n \in \{2, 3\}$ throughout.
> - $\{I_n\}$ and $GL_n(\mathbb{R})$ itself.
> - *[[§3 Basic Examples of Groups#^def-3-7|Special linear group]]* $SL_n(\mathbb{R}) = \{A : \det A = 1\}$  ($\det(AB) = \det A \det B = 1$; $\det(A^{-1}) = (\det A)^{-1} = 1$; $\det I_n = 1$).
> - **Scalar matrices** $\{\lambda I_n : \lambda \in \mathbb{R}^\times\}$  ($\lambda I_n \cdot \mu I_n = \lambda\mu I_n$; inverse $\lambda^{-1} I_n$). This subgroup “is” $\mathbb{R}^\times$.
> - **Invertible diagonal matrices**  (products and inverses of diagonal matrices are diagonal, entrywise); this subgroup “is” $(\mathbb{R}^\times)^n$.
> - **Invertible upper-triangular matrices**  (the product of upper-triangulars is upper-triangular; the inverse of an invertible upper-triangular matrix is upper-triangular — solve $AX = I$ by back-substitution, column by column).
> - **Unipotent matrices**: upper-triangular with all diagonal entries $1$  (diagonal entries of a product of triangular matrices are the products of the diagonal entries, so $1$'s persist; same for the inverse by back-substitution).
> - Inside the unipotent group of $GL_2$: the **one-parameter subgroup** $\left\{ \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} : t \in \mathbb{R} \right\}$, which “is” $(\mathbb{R}, +)$: the product corresponds to $t + s$. So the additive real line embeds in $GL_2(\mathbb{R})$.
> - *[[§3 Basic Examples of Groups#^def-3-7|Orthogonal group]]* $O(n) = \{A : A^\mathsf{T} A = I_n\}$  (closure: $(AB)^\mathsf{T}(AB) = B^\mathsf{T} A^\mathsf{T} A B = B^\mathsf{T} B = I_n$; inverses: $A^\mathsf{T}A = I_n$ gives $A^{-1} = A^\mathsf{T}$, and $(A^\mathsf{T})^\mathsf{T} A^\mathsf{T} = A A^\mathsf{T} = A A^{-1} = I_n$).
> - *[[§3 Basic Examples of Groups#^def-3-7|Special orthogonal group]]* $SO(n) = O(n) \cap SL_n(\mathbb{R})$  ([[§4 Subgroups#^prop-4-3|an intersection of subgroups is a subgroup]]: each condition is preserved separately). For $n = 2$ these are the rotation matrices $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, with $R_\theta R_\varphi = R_{\theta + \varphi}$.
> - **Permutation matrices** ($0$/$1$ matrices with one $1$ per row and column)  (they compose like the permutations they encode); this subgroup “is” $S_n$ sitting inside $GL_n(\mathbb{R})$.
> - **Rational and integer points**: $GL_n(\mathbb{Q})$  (products of rational matrices are rational; inverses by Cramer's rule are rational), and $GL_n(\mathbb{Z}) = \{A \text{ integer}: \det A = \pm 1\}$  (Cramer: the inverse of an integer matrix is integer iff $\det A \mid 1$; closure since $\det(AB) = \pm 1$).
> - **Cyclic subgroups** $\langle A \rangle$ for any single $A$ ([[§4 Subgroups#^prop-4-5|WS 1.5]]), e.g. $\langle R_{2\pi/n} \rangle$, a copy of $C_n$ realized by rotations.
> - In $GL_3(\mathbb{R})$: **block copies of smaller groups**, e.g. $\left\{ \begin{pmatrix} A & 0 \\ 0 & 1 \end{pmatrix} : A \in GL_2(\mathbb{R}) \right\}$  (block multiplication is componentwise in the blocks), so every subgroup of $GL_2(\mathbb{R})$ reappears inside $GL_3(\mathbb{R})$.
>
> *Source: WS 1.7*

^ex-5-4

> [!remark]- Connections
> - The determinant facts used for $SL_n$ and $GL_n(\mathbb{Z})$: [[§34 Determinants#^ladr-9-49|Determinant is multiplicative]], [[§34 Determinants#^ladr-9-50|Invertible ⟺ nonzero determinant]]; a one-sided inverse of a square matrix is two-sided (used for $O(n)$): [[§10 Invertibility and Isomorphisms#^ladr-3-68|ST = I ⟺ TS = I]].
> - Permutation matrices made precise: [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]]; which of these subgroups are normal: [[§36 Sources of Normal Subgroups#^prop-36-8|Normal Subgroups of GL₂(ℝ)]].

> [!remark] Remark: Summary of WS 1.7
> The six groups display the full spectrum: $\mathbb{Z}$ and $S_3$ admit complete, short classifications; $\mathbb{Z}^2$ is classifiable but needs more theory ([[§5 A Zoo of Subgroups#^rem-5-2|rank]]); $\mathbb{R}$ obeys a clean dichotomy but contains wild dense subgroups; and $GL_n(\mathbb{R})$ is inexhaustible — it contains copies of essentially every group we will meet ($C_n$, $S_n$, $(\mathbb{R}, +)$, $\mathbb{R}^\times$, circle rotations, lattice groups). This last fact is the seed of [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6|representation theory]].

^rem-5-3
