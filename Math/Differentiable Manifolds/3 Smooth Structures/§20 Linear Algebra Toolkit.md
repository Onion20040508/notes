---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 20
tags: [differentiable-manifolds, math591]
---
← [[§19 Manifolds in Euclidean Space]] · ↑ [[· 3 Smooth Structures]] · [[§21 The Differential of a Map Between Vector Spaces]] →

*Stage: linear — The tool both tangent spaces will need: the linear algebra used from here on. The differential of a map between vector spaces ([[§21 The Differential of a Map Between Vector Spaces|§21]]) and the smooth matrix groups ([[§22 The Orthogonal and Unitary Groups as Smooth Manifolds|§22]]) follow.*

*Not from lecture. From here on the course runs on linear algebra — differentials, bases of tangent spaces, dual spaces — and this section records, once, the facts used. The first box is imported from linear algebra without proof, as the point-set facts of [[§1 Point-Set Topology Review|§1]] were imported from 590; everything after it is proved.* Throughout, vector spaces are real.

> [!theorem] Proposition §20.1: Standing Facts from Linear Algebra
> Let $A : V \to W$ be linear, with $V$ and $W$ finite-dimensional.
> 1. *Rank–nullity.* $\dim V = \dim\ker A + \operatorname{rank} A$. Consequently: if $A$ is injective then $\dim V \le \dim W$; if $A$ is surjective then $\dim V \ge \dim W$; and if $\dim V = \dim W$, then $A$ is injective $\iff$ surjective $\iff$ bijective.
> 2. *Bases determine linear maps.* A linear map is determined by its values on a basis, and any assignment of values to the vectors of a basis extends uniquely to a linear map. In particular, two linear maps that agree on a basis are equal.
> 3. *Matrices.* Given bases $(e_1, \ldots, e_m)$ of $V$ and $(f_1, \ldots, f_n)$ of $W$, the matrix $[A] = (a_{ij})$ of $A$ is defined by $A e_j = \sum_i a_{ij} f_i$: its $j$-th *column* holds the coordinates of $Ae_j$. Composition corresponds to matrix multiplication, $[AB] = [A][B]$, and $\operatorname{rank} A$ is the rank of $[A]$, which equals the rank of its transpose.
> 4. *Change of basis.* If $e'_j = \sum_i P_{ij}\, e_i$ and $f'_l = \sum_k Q_{kl}\, f_k$ are new bases, with $P$ and $Q$ invertible, then the matrix of $A$ in the new bases is $Q^{-1} [A] P$.
>
> *Lee: Corollary B.21 and Proposition B.24*

^prop-20-1

> [!remark]- Connections
> - (1): [[Fundamental theorem of linear maps|LADR 3.21 (fundamental theorem of linear maps)]], [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]], [[§8 Null Spaces and Ranges#^ladr-3-24|3.24]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]].
> - (2): [[Linear map lemma|LADR 3.4 (linear map lemma)]]. (3): [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[§9 Matrices#^ladr-3-57|LADR 3.57 (column rank equals row rank)]]. (4): [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84 (change-of-basis formula)]].

> [!proof]+ Proof (to be filled)
> Imported from linear algebra without proof; proved in Axler, *Linear Algebra Done Right* — see the [[Linear Algebra]] notes and the links under Connections above (also Lee, Corollary B.21 and Proposition B.24). To be filled.

^pf-20-1

> [!definition] Definition §20.1: Dual Space
> The **dual space** of $V$ is $V^{\ast} = \{\lambda : V \to \mathbb{R} \mid \lambda \text{ linear}\}$, a vector space under pointwise operations; its elements are **linear functionals**, or **covectors**.
>
> *Lee: Proposition 11.1*

^def-20-1

> [!definition] Definition §20.2: Dual Basis
> If $(e_1, \ldots, e_n)$ is a basis of $V$, the **dual basis** $(\varepsilon^1, \ldots, \varepsilon^n)$ consists of the covectors ([[§20 Linear Algebra Toolkit#^def-20-1|Definition §20.1]]) with
>
> $$
> \varepsilon^i(e_j) = \delta^i_j ,
> $$
>
> which exist and are unique by Proposition [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]](2).
>
> *Lee: Proposition 11.1*

^def-20-2

> [!remark]- Connections
> - Home in linear algebra (written $V'$ there): [[§12 Duality#^ladr-3-110|LADR 3.110 (dual space)]], [[§12 Duality#^ladr-3-112|LADR 3.112 (dual basis)]].
> - Applied to $T_pM$: the cotangent space, [[§30 The Cotangent Space#^def-30-1|Def. §30.1]].

> [!theorem] Proposition §20.2: The Dual Basis
> Let $(e_1, \ldots, e_n)$ be a basis of $V$ with dual basis $(\varepsilon^1, \ldots, \varepsilon^n)$. Then $(\varepsilon^i)$ is a basis of $V^*$, so $\dim V^* = \dim V$, and for all $v \in V$ and $\lambda \in V^*$,
>
> $$
> v = \sum_{i=1}^n \varepsilon^i(v)\, e_i, \qquad\qquad \lambda = \sum_{i=1}^n \lambda(e_i)\, \varepsilon^i .
> $$
>
> *Lee: Proposition 11.1*

^prop-20-2

> [!proof]+ Proof
> If $v = \sum_j v^j e_j$, then $\varepsilon^i(v) = \sum_j v^j \delta^i_j = v^i$, which is the first formula: the dual basis *extracts the components* of a vector. The two sides of the second formula are covectors that agree on each $e_j$, both giving $\lambda(e_j)$, so they are equal by Proposition [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]](2); hence the $\varepsilon^i$ span $V^{\ast}$. If $\sum_i c_i \varepsilon^i = 0$, applying it to $e_j$ gives $c_j = 0$; so they are independent.

^pf-20-2

*Uses:* [[§20 Linear Algebra Toolkit#^def-20-1|Def. §20.1]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]], [[Linear map lemma|LADR 3.4]]

> [!remark]- Connections
> - Home: [[§12 Duality#^ladr-3-114|LADR 3.114 (dual basis gives coefficients)]], [[§12 Duality#^ladr-3-116|LADR 3.116 (dual basis is a basis of the dual space)]], [[§12 Duality#^ladr-3-111|LADR 3.111]].

> [!theorem] Proposition §20.3: The Double Dual
> For a finite-dimensional $V$, the map
>
> $$
> \iota : V \to V^{**}, \qquad \iota(v)(\lambda) = \lambda(v),
> $$
>
> is a linear isomorphism. It is **canonical**: its definition involves no choice of basis.
>
> *Lee: Proposition 11.8*

^prop-20-3

> [!proof]+ Proof
> $\iota$ is linear, since each $\lambda$ is. If $v \ne 0$, extend $v$ to a basis $(v, e_2, \ldots, e_n)$; the first dual basis covector $\varepsilon^1$ has $\iota(v)(\varepsilon^1) = \varepsilon^1(v) = 1 \ne 0$. So $\iota$ is injective, and $\dim V^{**} = \dim V^* = \dim V$ by Proposition [[§20 Linear Algebra Toolkit#^prop-20-2|§20.2]], so $\iota$ is an isomorphism by Proposition [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]](1).

^pf-20-3

*Uses:* [[§20 Linear Algebra Toolkit#^def-20-1|Def. §20.1]], [[§20 Linear Algebra Toolkit#^prop-20-2|§20.2]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]], [[Every linearly independent list extends to a basis|LADR 2.32]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - In LADR the canonical $V \cong V''$ is mentioned in the remark after [[§12 Duality#^ladr-3-111|LADR 3.111]] (the non-canonical $V \cong V'$ goes through [[Dimension shows whether vector spaces are isomorphic|LADR 3.70]]).

> [!remark] Remark
> A finite-dimensional $V$ is also isomorphic to $V^{\ast}$, for instance by $e_i \mapsto \varepsilon^i$, but that isomorphism depends on the basis: change the basis and it changes. $V$ and $V^{\ast \ast}$ are identified *canonically*. This is why tangent vectors and covectors must be kept apart, as [[§30 The Cotangent Space#^def-30-1|Lecture 10]] did with $T_pM$ and $T_p^{\ast}M$, while the dual of $T_p^{\ast}M$ may be silently identified with $T_pM$.

^rem-20-1

> [!definition] Definition §20.3: Dual Map
> The **dual map**, or **transpose**, of a linear map $A : V \to W$ is
>
> $$
> A^* : W^* \to V^*, \qquad A^*(\lambda) = \lambda \circ A .
> $$
>
> *Lee: Proposition 11.4*

^def-20-3

![[m591-10-1.svg]]
*A linear map $A : V \to W$ carries vectors forward; its dual map $A^{\ast} : W^{\ast} \to V^{\ast}$ carries covectors backward.*

A covector on $W$ becomes a covector on $V$ by first applying $A$; so the dual map runs backwards. This is the linear-algebra shadow of the directions in [[§26 Derivations and the Abstract Tangent Space#Pushing Derivations Forward|§26, Pushing Derivations Forward]], where germs were pulled back and derivations pushed forward.

> [!theorem] Proposition §20.4: Properties of the Dual Map
> Let $A : V \to W$ and $B : W \to Z$ be linear.
> 1. $A^*$ is linear, $(\mathrm{id}_V)^* = \mathrm{id}_{V^*}$, and $(B \circ A)^* = A^* \circ B^*$. In particular, if $A$ is an isomorphism, so is $A^*$, with $(A^*)^{-1} = (A^{-1})^*$.
> 2. For finite-dimensional $V$ and $W$, the matrix of $A^*$ in the dual bases is the transpose of the matrix of $A$.
> 3. For finite-dimensional $V$ and $W$: $A$ is injective $\iff$ $A^*$ is surjective, and $A$ is surjective $\iff$ $A^*$ is injective.
>
> *Lee: Proposition 11.4*

^prop-20-4

> [!proof]+ Proof
> (1) $A^*(\lambda + c\mu) = (\lambda + c\mu) \circ A = A^*\lambda + c\,A^*\mu$, and $(B \circ A)^*(\lambda) = \lambda \circ B \circ A = A^*(B^*\lambda)$. For an isomorphism, apply this to $A^{-1} \circ A = \mathrm{id}$ and $A \circ A^{-1} = \mathrm{id}$.
>
> (2) Let $(e_j)$ and $(f_i)$ be bases of $V$ and $W$, with dual bases $(\varepsilon^j)$ and $(\varphi^k)$, and $Ae_j = \sum_i a_{ij} f_i$. Then $A^*(\varphi^k)(e_j) = \varphi^k(Ae_j) = a_{kj}$, so by Proposition [[§20 Linear Algebra Toolkit#^prop-20-2|§20.2]], $A^*(\varphi^k) = \sum_j a_{kj}\,\varepsilon^j$. The $k$-th column of the matrix of $A^*$ is therefore the $k$-th row of $[A]$.
>
> (3) By (2) and Proposition [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]](3), $\operatorname{rank} A^* = \operatorname{rank} A$. Now $A$ is surjective iff $\operatorname{rank} A = \dim W$, iff $\operatorname{rank} A^* = \dim W^*$, which by rank–nullity means $A^*$ is injective. Likewise $A$ is injective iff $\operatorname{rank} A = \dim V = \dim V^*$, iff $A^*$ is surjective.

^pf-20-4

*Uses:* [[§20 Linear Algebra Toolkit#^def-20-3|Def. §20.3]], [[§20 Linear Algebra Toolkit#^prop-20-2|§20.2]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]], [[§9 Matrices#^ladr-3-57|LADR 3.57]], [[Fundamental theorem of linear maps|LADR 3.21]]

> [!remark]- Connections
> - Home: [[§12 Duality#^ladr-3-118|LADR 3.118 (dual map)]], [[§12 Duality#^ladr-3-120|LADR 3.120 (algebraic properties)]], [[§12 Duality#^ladr-3-132|LADR 3.132 (matrix of the dual map is the transpose)]]; (3) is [[§12 Duality#^ladr-3-128|LADR 3.128]] and [[§12 Duality#^ladr-3-130|LADR 3.130]] (null space and range of the dual map).

> [!definition] Definition §20.4: Bilinear Pairing
> A **bilinear pairing** is a map $B : V \times W \to \mathbb{R}$ that is linear in each argument separately. It induces linear maps
>
> $$
> B^\flat : V \to W^*, \ \ v \mapsto B(v, \cdot\,), \qquad\qquad B^\sharp : W \to V^*, \ \ w \mapsto B(\cdot\,, w).
> $$
>
> $B$ is **left non-degenerate** if $B(v, w) = 0$ for all $w$ implies $v = 0$, i.e. $B^\flat$ is injective; **right non-degenerate** if $B(v, w) = 0$ for all $v$ implies $w = 0$, i.e. $B^\sharp$ is injective; and **non-degenerate** if both.

^def-20-4

> [!remark]- Connections
> - Same notion in LADR: [[§35 Tensor Products#^ladr-9-68|LADR 9.68]] (bilinear functionals on V × W); the case W = V is a bilinear form, [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-1|LADR 9.1]].

> [!theorem] Theorem §20.5: Non-Degenerate Pairings
> Let $B : V \times W \to \mathbb{R}$ be a non-degenerate bilinear pairing, and suppose $V$ or $W$ is finite-dimensional. Then both are finite-dimensional, $\dim V = \dim W$, and
>
> $$
> B^\flat : V \xrightarrow{\ \cong\ } W^*, \qquad\qquad B^\sharp : W \xrightarrow{\ \cong\ } V^*
> $$
>
> are isomorphisms.
>
> *Lee: no counterpart*

^thm-20-5

> [!proof]+ Proof
> Suppose $V$ is finite-dimensional, of dimension $n$; the other case is symmetric. Right non-degeneracy makes $B^\sharp : W \to V^*$ injective, so $W$ is isomorphic to a subspace of the $n$-dimensional $V^*$: it is finite-dimensional with $\dim W \le n$. Left non-degeneracy makes $B^\flat : V \to W^*$ injective, so $n \le \dim W^* = \dim W$. Hence $\dim V = \dim W$, and $B^\flat$, $B^\sharp$ are injective maps between spaces of equal finite dimension, hence isomorphisms by Proposition [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]](1).

^pf-20-5

*Uses:* [[§20 Linear Algebra Toolkit#^def-20-4|Def. §20.4]], [[§20 Linear Algebra Toolkit#^prop-20-2|§20.2]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - Applied to the pairing of tangent vectors with germs: [[§30 The Cotangent Space#^prop-30-7|§30.7]], [[§30 The Cotangent Space#^thm-30-8|§30.8]].
> - Bilinear forms on a single space in LADR: [[§32 Bilinear Forms and Quadratic Forms|9A Bilinear Forms and Quadratic Forms]].

> [!remark] Remark
> Each half of non-degeneracy gives one inequality of dimensions, and it is the *pair* of inequalities that forces the isomorphisms; neither half suffices alone. The finiteness hypothesis cannot be dropped: for an infinite-dimensional $V$, the evaluation pairing $V \times V^{\ast} \to \mathbb{R}$, $(v, \lambda) \mapsto \lambda(v)$, is non-degenerate, but its map $B^\flat = \iota : V \to V^{\ast \ast}$ is injective without being onto. [[§30 The Cotangent Space#^thm-30-8|Assignment 3, Problem 3]] is exactly a pairing $T_pM \times I_p/I_p^2 \to \mathbb{R}$ to which this theorem applies.

^rem-20-2

> [!definition] Definition §20.5: Quotient Vector Space
> Let $W \subseteq V$ be a linear subspace. The **quotient space** $V/W$ is the set of cosets $v + W = \{v + w \mid w \in W\}$, with
>
> $$
> (v + W) + (v' + W) = (v + v') + W, \qquad c\,(v + W) = cv + W,
> $$
>
> and the **projection** is $\pi : V \to V/W$, $\pi(v) = v + W$. Two vectors have the same coset iff their difference lies in $W$.
>
> *Lee: App. B, Vector Spaces*

^def-20-5

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99 (quotient space)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|LADR 3.102 (operations)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|LADR 3.104 (quotient map)]].

> [!theorem] Proposition §20.6: Quotient Spaces and Their Universal Property
> 1. The operations are well defined, $V/W$ is a vector space, and $\pi$ is linear and surjective with $\ker \pi = W$.
> 2. *Universal property.* If $A : V \to Z$ is linear with $W \subseteq \ker A$, there is a unique linear $\bar A : V/W \to Z$ with $\bar A \circ \pi = A$, namely $\bar A(v + W) = A(v)$.
> 3. If $V$ is finite-dimensional, $\dim V/W = \dim V - \dim W$.
>
> *Lee: App. B, Vector Spaces*

^prop-20-6

> [!proof]+ Proof
> (1) If $v - v' \in W$ and $u - u' \in W$, then $(v + u) - (v' + u') \in W$ and $cv - cv' \in W$, so the operations do not depend on representatives; the vector space axioms are inherited from $V$. $\pi$ is linear by the definition of the operations, surjective by construction, and $\pi(v) = 0 + W$ iff $v \in W$. (2) If $v - v' \in W$ then $A(v) - A(v') = A(v - v') = 0$, so $\bar A$ is well defined; it is linear because $A$ is; and it is unique because $\pi$ is surjective. (3) Rank–nullity for $\pi$.

^pf-20-6

*Uses:* [[§20 Linear Algebra Toolkit#^def-20-5|Def. §20.5]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]], [[Fundamental theorem of linear maps|LADR 3.21]]

![[m591-10-2.svg]]
*The universal property of the quotient: a linear map $A$ with $W \subseteq \ker A$ factors uniquely as $A = \bar A \circ \pi$.*

The universal property as a triangle: a linear map that kills $W$ descends to $V/W$. It is the linear counterpart of the universal property of quotient maps, Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]], with “vanishes on $W$” in place of “constant on the fibres” — and the proof is the same: define the map on a class by choosing a representative, and check the choice does not matter. [[§30 The Cotangent Space#^prop-30-7|Assignment 3, Problem 3(a)]] is an instance: a derivation kills $I_p^2$, so its restriction to $I_p$ descends to $I_p/I_p^2$.

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103 (quotient space is a vector space)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105 (dimension)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-106|LADR 3.106]] and [[First isomorphism theorem|LADR 3.107 (first isomorphism theorem)]] for the induced map.
> - Topological counterpart: [[Universal Property of Quotient Maps|590 §12 (universal property of quotient maps)]]; applied in [[§30 The Cotangent Space#^def-30-3|Def. §30.3]].

> [!definition] Definition §20.6: Direct Sum
> The **direct sum** of vector spaces $V$ and $W$ is $V \oplus W = V \times W$ with the componentwise operations $(v, w) + (v', w') = (v + v', w + w')$ and $c(v, w) = (cv, cw)$. It comes with the **inclusions** $\iota_V(v) = (v, 0)$, $\iota_W(w) = (0, w)$ and the **projections** $\pi_V(v, w) = v$, $\pi_W(v, w) = w$, all linear. A vector space $U$ is the **internal direct sum** of subspaces $U_1, U_2$, written $U = U_1 \oplus U_2$, if every $u \in U$ is $u_1 + u_2$ for unique $u_1 \in U_1$, $u_2 \in U_2$.

^def-20-6

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|LADR 3.87 (product of vector spaces)]], [[§3 Subspaces#^ladr-1-41|LADR 1.41 (internal direct sum)]].

> [!theorem] Proposition §20.7: Direct Sums
> 1. $\pi_V \iota_V = \mathrm{id}_V$, $\pi_W \iota_W = \mathrm{id}_W$, $\pi_W \iota_V = 0$ and $\pi_V \iota_W = 0$. So $\iota_V$, $\iota_W$ are injective, and $V \oplus W$ is the internal direct sum of $V \oplus \{0\} = \iota_V(V)$ and $\{0\} \oplus W = \iota_W(W)$.
> 2. If $(e_i)$ and $(f_j)$ are bases of $V$ and $W$, then the vectors $(e_i, 0)$ and $(0, f_j)$ together form a basis of $V \oplus W$. In particular $\dim (V \oplus W) = \dim V + \dim W$.
>
> *Lee: App. B, Vector Spaces*

^prop-20-7

> [!proof]+ Proof
> (1) Direct from the formulas; each $(v, w)$ is $\iota_V(v) + \iota_W(w)$, and $v = \pi_V(v, w)$, $w = \pi_W(v, w)$ are forced. (2) $(v, w) = \sum_i v^i (e_i, 0) + \sum_j w^j (0, f_j)$ for the coordinates $v^i$, $w^j$ of $v$ and $w$, and such a combination vanishes only if all $v^i$ and all $w^j$ do.

^pf-20-7

*Uses:* [[§20 Linear Algebra Toolkit#^def-20-6|Def. §20.6]]

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|LADR 3.92 (dimension of a product)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|LADR 3.93 (products and direct sums)]], [[Condition for a direct sum|LADR 1.45]].
> - Used for the tangent space of a product: [[§29 Tangent Vectors as Velocities of Curves#^thm-29-4|§29.4]].

> [!remark] Remark: Direct Sum and Product
> For two summands, or finitely many, the direct sum *is* the Cartesian product with componentwise operations — the point Uribe said in Lecture 11 he had forgotten the reason for. The two notions differ only for infinitely many summands: the product $\prod_\alpha V_\alpha$ contains all families $(v_\alpha)$, while the direct sum $\bigoplus_\alpha V_\alpha$ contains only those with finitely many nonzero entries.

^rem-20-3
