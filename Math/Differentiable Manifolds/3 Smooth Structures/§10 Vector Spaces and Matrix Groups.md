---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 10
tags: [differentiable-manifolds, math591]
---
← [[§9 Manifolds in Euclidean Space]] · ↑ [[· 3 Smooth Structures]] · [[§11 Tangent Spaces I꞉ The Geometric Picture]] →

*Stage: linear — The tool both tangent spaces will need: linear algebra, and the differential of a map between vector spaces. The matrix groups become smooth level sets.*

## Linear Algebra Toolkit

*Not from lecture. From here on the course runs on linear algebra — differentials, bases of tangent spaces, dual spaces — and this subsection records, once, the facts used. The first box is imported from linear algebra without proof, as the point-set facts of [[§1 Point-Set Topology Review|§1]] were imported from 590; everything after it is proved.* Throughout, vector spaces are real.

> [!theorem] Proposition §10.1: Standing Facts from Linear Algebra
> Let $A : V \to W$ be linear, with $V$ and $W$ finite-dimensional.
> 1. *Rank–nullity.* $\dim V = \dim\ker A + \operatorname{rank} A$. Consequently: if $A$ is injective then $\dim V \le \dim W$; if $A$ is surjective then $\dim V \ge \dim W$; and if $\dim V = \dim W$, then $A$ is injective $\iff$ surjective $\iff$ bijective.
> 2. *Bases determine linear maps.* A linear map is determined by its values on a basis, and any assignment of values to the vectors of a basis extends uniquely to a linear map. In particular, two linear maps that agree on a basis are equal.
> 3. *Matrices.* Given bases $(e_1, \ldots, e_m)$ of $V$ and $(f_1, \ldots, f_n)$ of $W$, the matrix $[A] = (a_{ij})$ of $A$ is defined by $A e_j = \sum_i a_{ij} f_i$: its $j$-th *column* holds the coordinates of $Ae_j$. Composition corresponds to matrix multiplication, $[AB] = [A][B]$, and $\operatorname{rank} A$ is the rank of $[A]$, which equals the rank of its transpose.
> 4. *Change of basis.* If $e'_j = \sum_i P_{ij}\, e_i$ and $f'_l = \sum_k Q_{kl}\, f_k$ are new bases, with $P$ and $Q$ invertible, then the matrix of $A$ in the new bases is $Q^{-1} [A] P$.
>
> *Lee: Corollary B.21 and Proposition B.24*

^prop-10-1

> [!remark]- Connections
> - (1): [[Fundamental theorem of linear maps|LADR 3.21 (fundamental theorem of linear maps)]], [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]], [[§8 Null Spaces and Ranges#^ladr-3-24|3.24]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]].
> - (2): [[Linear map lemma|LADR 3.4 (linear map lemma)]]. (3): [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[§9 Matrices#^ladr-3-57|LADR 3.57 (column rank equals row rank)]]. (4): [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84 (change-of-basis formula)]].

> [!definition] Definition §10.1: Dual Space and Dual Basis
> The **dual space** of $V$ is $V^* = \{\lambda : V \to \mathbb{R} \mid \lambda \text{ linear}\}$, a vector space under pointwise operations; its elements are **linear functionals**, or **covectors**. If $(e_1, \ldots, e_n)$ is a basis of $V$, the **dual basis** $(\varepsilon^1, \ldots, \varepsilon^n)$ consists of the covectors with
>
> $$
> \varepsilon^i(e_j) = \delta^i_j ,
> $$
>
> which exist and are unique by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]](2).
>
> *Lee: Proposition 11.1*

^def-10-1

> [!remark]- Connections
> - Home in linear algebra (written $V'$ there): [[§12 Duality#^ladr-3-110|LADR 3.110 (dual space)]], [[§12 Duality#^ladr-3-112|LADR 3.112 (dual basis)]].
> - Applied to $T_pM$: the cotangent space, [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1|Def. §13.1]].

> [!theorem] Proposition §10.2: The Dual Basis
> Let $(e_1, \ldots, e_n)$ be a basis of $V$ with dual basis $(\varepsilon^1, \ldots, \varepsilon^n)$. Then $(\varepsilon^i)$ is a basis of $V^*$, so $\dim V^* = \dim V$, and for all $v \in V$ and $\lambda \in V^*$,
>
> $$
> v = \sum_{i=1}^n \varepsilon^i(v)\, e_i, \qquad\qquad \lambda = \sum_{i=1}^n \lambda(e_i)\, \varepsilon^i .
> $$
>
> *Lee: Proposition 11.1*

^prop-10-2

> [!proof]+ Proof
> If $v = \sum_j v^j e_j$, then $\varepsilon^i(v) = \sum_j v^j \delta^i_j = v^i$, which is the first formula: the dual basis *extracts the components* of a vector. The two sides of the second formula are covectors that agree on each $e_j$, both giving $\lambda(e_j)$, so they are equal by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]](2); hence the $\varepsilon^i$ span $V^*$. If $\sum_i c_i \varepsilon^i = 0$, applying it to $e_j$ gives $c_j = 0$; so they are independent.

^pf-10-2

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-1|Def. §10.1]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[Linear map lemma|LADR 3.4]]

> [!remark]- Connections
> - Home: [[§12 Duality#^ladr-3-114|LADR 3.114 (dual basis gives coefficients)]], [[§12 Duality#^ladr-3-116|LADR 3.116 (dual basis is a basis of the dual space)]], [[§12 Duality#^ladr-3-111|LADR 3.111]].

> [!theorem] Proposition §10.3: The Double Dual
> For a finite-dimensional $V$, the map
>
> $$
> \iota : V \to V^{**}, \qquad \iota(v)(\lambda) = \lambda(v),
> $$
>
> is a linear isomorphism. It is **canonical**: its definition involves no choice of basis.
>
> *Lee: Proposition 11.8*

^prop-10-3

> [!proof]+ Proof
> $\iota$ is linear, since each $\lambda$ is. If $v \ne 0$, extend $v$ to a basis $(v, e_2, \ldots, e_n)$; the first dual basis covector $\varepsilon^1$ has $\iota(v)(\varepsilon^1) = \varepsilon^1(v) = 1 \ne 0$. So $\iota$ is injective, and $\dim V^{**} = \dim V^* = \dim V$ by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-2|§10.2]], so $\iota$ is an isomorphism by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]](1).

^pf-10-3

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-1|Def. §10.1]], [[§10 Vector Spaces and Matrix Groups#^prop-10-2|§10.2]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[Every linearly independent list extends to a basis|LADR 2.32]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - In LADR the canonical $V \cong V''$ is mentioned in the remark after [[§12 Duality#^ladr-3-111|LADR 3.111]] (the non-canonical $V \cong V'$ goes through [[Dimension shows whether vector spaces are isomorphic|LADR 3.70]]).

> [!remark] Remark
> A finite-dimensional $V$ is also isomorphic to $V^*$, for instance by $e_i \mapsto \varepsilon^i$, but that isomorphism depends on the basis: change the basis and it changes. $V$ and $V^{**}$ are identified *canonically*. This is why tangent vectors and covectors must be kept apart, as [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1|Lecture 10]] did with $T_pM$ and $T_p^*M$, while the dual of $T_p^*M$ may be silently identified with $T_pM$.

^rem-10-1

> [!definition] Definition §10.2: Dual Map
> The **dual map**, or **transpose**, of a linear map $A : V \to W$ is
>
> $$
> A^* : W^* \to V^*, \qquad A^*(\lambda) = \lambda \circ A .
> $$
>
> *Lee: Proposition 11.4*

^def-10-2

![[m591-10-1.svg]]
*A linear map $A : V \to W$ carries vectors forward; its dual map $A^* : W^* \to V^*$ carries covectors backward.*

A covector on $W$ becomes a covector on $V$ by first applying $A$; so the dual map runs backwards. This is the linear-algebra shadow of the directions in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#Pushing Derivations Forward|§12, Pushing Derivations Forward]], where germs were pulled back and derivations pushed forward.

> [!theorem] Proposition §10.4: Properties of the Dual Map
> Let $A : V \to W$ and $B : W \to Z$ be linear.
> 1. $A^*$ is linear, $(\mathrm{id}_V)^* = \mathrm{id}_{V^*}$, and $(B \circ A)^* = A^* \circ B^*$. In particular, if $A$ is an isomorphism, so is $A^*$, with $(A^*)^{-1} = (A^{-1})^*$.
> 2. For finite-dimensional $V$ and $W$, the matrix of $A^*$ in the dual bases is the transpose of the matrix of $A$.
> 3. For finite-dimensional $V$ and $W$: $A$ is injective $\iff$ $A^*$ is surjective, and $A$ is surjective $\iff$ $A^*$ is injective.
>
> *Lee: Proposition 11.4*

^prop-10-4

> [!proof]+ Proof
> (1) $A^*(\lambda + c\mu) = (\lambda + c\mu) \circ A = A^*\lambda + c\,A^*\mu$, and $(B \circ A)^*(\lambda) = \lambda \circ B \circ A = A^*(B^*\lambda)$. For an isomorphism, apply this to $A^{-1} \circ A = \mathrm{id}$ and $A \circ A^{-1} = \mathrm{id}$.
>
> (2) Let $(e_j)$ and $(f_i)$ be bases of $V$ and $W$, with dual bases $(\varepsilon^j)$ and $(\varphi^k)$, and $Ae_j = \sum_i a_{ij} f_i$. Then $A^*(\varphi^k)(e_j) = \varphi^k(Ae_j) = a_{kj}$, so by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-2|§10.2]], $A^*(\varphi^k) = \sum_j a_{kj}\,\varepsilon^j$. The $k$-th column of the matrix of $A^*$ is therefore the $k$-th row of $[A]$.
>
> (3) By (2) and Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]](3), $\operatorname{rank} A^* = \operatorname{rank} A$. Now $A$ is surjective iff $\operatorname{rank} A = \dim W$, iff $\operatorname{rank} A^* = \dim W^*$, which by rank–nullity means $A^*$ is injective. Likewise $A$ is injective iff $\operatorname{rank} A = \dim V = \dim V^*$, iff $A^*$ is surjective.

^pf-10-4

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-2|Def. §10.2]], [[§10 Vector Spaces and Matrix Groups#^prop-10-2|§10.2]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[§9 Matrices#^ladr-3-57|LADR 3.57]], [[Fundamental theorem of linear maps|LADR 3.21]]

> [!remark]- Connections
> - Home: [[§12 Duality#^ladr-3-118|LADR 3.118 (dual map)]], [[§12 Duality#^ladr-3-120|LADR 3.120 (algebraic properties)]], [[§12 Duality#^ladr-3-132|LADR 3.132 (matrix of the dual map is the transpose)]]; (3) is [[§12 Duality#^ladr-3-128|LADR 3.128]] and [[§12 Duality#^ladr-3-130|LADR 3.130]] (null space and range of the dual map).

> [!definition] Definition §10.3: Bilinear Pairing
> A **bilinear pairing** is a map $B : V \times W \to \mathbb{R}$ that is linear in each argument separately. It induces linear maps
>
> $$
> B^\flat : V \to W^*, \ \ v \mapsto B(v, \cdot\,), \qquad\qquad B^\sharp : W \to V^*, \ \ w \mapsto B(\cdot\,, w).
> $$
>
> $B$ is **left non-degenerate** if $B(v, w) = 0$ for all $w$ implies $v = 0$, i.e. $B^\flat$ is injective; **right non-degenerate** if $B(v, w) = 0$ for all $v$ implies $w = 0$, i.e. $B^\sharp$ is injective; and **non-degenerate** if both.

^def-10-3

> [!theorem] Theorem §10.5: Non-Degenerate Pairings
> Let $B : V \times W \to \mathbb{R}$ be a non-degenerate bilinear pairing, and suppose $V$ or $W$ is finite-dimensional. Then both are finite-dimensional, $\dim V = \dim W$, and
>
> $$
> B^\flat : V \xrightarrow{\ \cong\ } W^*, \qquad\qquad B^\sharp : W \xrightarrow{\ \cong\ } V^*
> $$
>
> are isomorphisms.
>
> *Lee: no counterpart*

^thm-10-5

> [!proof]+ Proof
> Suppose $V$ is finite-dimensional, of dimension $n$; the other case is symmetric. Right non-degeneracy makes $B^\sharp : W \to V^*$ injective, so $W$ is isomorphic to a subspace of the $n$-dimensional $V^*$: it is finite-dimensional with $\dim W \le n$. Left non-degeneracy makes $B^\flat : V \to W^*$ injective, so $n \le \dim W^* = \dim W$. Hence $\dim V = \dim W$, and $B^\flat$, $B^\sharp$ are injective maps between spaces of equal finite dimension, hence isomorphisms by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]](1).

^pf-10-5

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-3|Def. §10.3]], [[§10 Vector Spaces and Matrix Groups#^prop-10-2|§10.2]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - Applied to the pairing of tangent vectors with germs: [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-6|§13.6]], [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7|§13.7]].
> - Bilinear forms on a single space in LADR: [[§32 Bilinear Forms and Quadratic Forms|9A Bilinear Forms and Quadratic Forms]].

> [!remark] Remark
> Each half of non-degeneracy gives one inequality of dimensions, and it is the *pair* of inequalities that forces the isomorphisms; neither half suffices alone. The finiteness hypothesis cannot be dropped: for an infinite-dimensional $V$, the evaluation pairing $V \times V^* \to \mathbb{R}$, $(v, \lambda) \mapsto \lambda(v)$, is non-degenerate, but its map $B^\flat = \iota : V \to V^{**}$ is injective without being onto. [[§13 Tangent Spaces III꞉ The Cotangent Space#^thm-13-7|Assignment 3, Problem 3]] is exactly a pairing $T_pM \times I_p/I_p^2 \to \mathbb{R}$ to which this theorem applies.

^rem-10-2

> [!definition] Definition §10.4: Quotient Vector Space
> Let $W \subseteq V$ be a linear subspace. The **quotient space** $V/W$ is the set of cosets $v + W = \{v + w \mid w \in W\}$, with
>
> $$
> (v + W) + (v' + W) = (v + v') + W, \qquad c\,(v + W) = cv + W,
> $$
>
> and the **projection** is $\pi : V \to V/W$, $\pi(v) = v + W$. Two vectors have the same coset iff their difference lies in $W$.
>
> *Lee: App. B, Vector Spaces*

^def-10-4

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99 (quotient space)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|LADR 3.102 (operations)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|LADR 3.104 (quotient map)]].

> [!theorem] Proposition §10.6: Quotient Spaces and Their Universal Property
> 1. The operations are well defined, $V/W$ is a vector space, and $\pi$ is linear and surjective with $\ker \pi = W$.
> 2. *Universal property.* If $A : V \to Z$ is linear with $W \subseteq \ker A$, there is a unique linear $\bar A : V/W \to Z$ with $\bar A \circ \pi = A$, namely $\bar A(v + W) = A(v)$.
> 3. If $V$ is finite-dimensional, $\dim V/W = \dim V - \dim W$.
>
> *Lee: App. B, Vector Spaces*

^prop-10-6

> [!proof]+ Proof
> (1) If $v - v' \in W$ and $u - u' \in W$, then $(v + u) - (v' + u') \in W$ and $cv - cv' \in W$, so the operations do not depend on representatives; the vector space axioms are inherited from $V$. $\pi$ is linear by the definition of the operations, surjective by construction, and $\pi(v) = 0 + W$ iff $v \in W$. (2) If $v - v' \in W$ then $A(v) - A(v') = A(v - v') = 0$, so $\bar A$ is well defined; it is linear because $A$ is; and it is unique because $\pi$ is surjective. (3) Rank–nullity for $\pi$.

^pf-10-6

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-4|Def. §10.4]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[Fundamental theorem of linear maps|LADR 3.21]]

![[m591-10-2.svg]]
*The universal property of the quotient: a linear map $A$ with $W \subseteq \ker A$ factors uniquely as $A = \bar A \circ \pi$.*

The universal property as a triangle: a linear map that kills $W$ descends to $V/W$. It is the linear counterpart of the universal property of quotient maps, Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]], with “vanishes on $W$” in place of “constant on the fibres” — and the proof is the same: define the map on a class by choosing a representative, and check the choice does not matter. [[§13 Tangent Spaces III꞉ The Cotangent Space#^prop-13-6|Assignment 3, Problem 3(a)]] is an instance: a derivation kills $I_p^2$, so its restriction to $I_p$ descends to $I_p/I_p^2$.

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103 (quotient space is a vector space)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105 (dimension)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-106|LADR 3.106]] and [[First isomorphism theorem|LADR 3.107 (first isomorphism theorem)]] for the induced map.
> - Topological counterpart: [[Universal Property of Quotient Maps|590 §12 (universal property of quotient maps)]]; applied in [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-2|Def. §13.2]].

> [!definition] Definition §10.5: Direct Sum
> The **direct sum** of vector spaces $V$ and $W$ is $V \oplus W = V \times W$ with the componentwise operations $(v, w) + (v', w') = (v + v', w + w')$ and $c(v, w) = (cv, cw)$. It comes with the **inclusions** $\iota_V(v) = (v, 0)$, $\iota_W(w) = (0, w)$ and the **projections** $\pi_V(v, w) = v$, $\pi_W(v, w) = w$, all linear. A vector space $U$ is the **internal direct sum** of subspaces $U_1, U_2$, written $U = U_1 \oplus U_2$, if every $u \in U$ is $u_1 + u_2$ for unique $u_1 \in U_1$, $u_2 \in U_2$.

^def-10-5

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|LADR 3.87 (product of vector spaces)]], [[§3 Subspaces#^ladr-1-41|LADR 1.41 (internal direct sum)]].

> [!theorem] Proposition §10.7: Direct Sums
> 1. $\pi_V \iota_V = \mathrm{id}_V$, $\pi_W \iota_W = \mathrm{id}_W$, $\pi_W \iota_V = 0$ and $\pi_V \iota_W = 0$. So $\iota_V$, $\iota_W$ are injective, and $V \oplus W$ is the internal direct sum of $V \oplus \{0\} = \iota_V(V)$ and $\{0\} \oplus W = \iota_W(W)$.
> 2. If $(e_i)$ and $(f_j)$ are bases of $V$ and $W$, then the vectors $(e_i, 0)$ and $(0, f_j)$ together form a basis of $V \oplus W$. In particular $\dim (V \oplus W) = \dim V + \dim W$.
>
> *Lee: App. B, Vector Spaces*

^prop-10-7

> [!proof]+ Proof
> (1) Direct from the formulas; each $(v, w)$ is $\iota_V(v) + \iota_W(w)$, and $v = \pi_V(v, w)$, $w = \pi_W(v, w)$ are forced. (2) $(v, w) = \sum_i v^i (e_i, 0) + \sum_j w^j (0, f_j)$ for the coordinates $v^i$, $w^j$ of $v$ and $w$, and such a combination vanishes only if all $v^i$ and all $w^j$ do.

^pf-10-7

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-5|Def. §10.5]]

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|LADR 3.92 (dimension of a product)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|LADR 3.93 (products and direct sums)]], [[Condition for a direct sum|LADR 1.45]].
> - Used for the tangent space of a product: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-32|§12.32]].

> [!remark] Remark: Direct Sum and Product
> For two summands, or finitely many, the direct sum *is* the Cartesian product with componentwise operations — the point Uribe said in Lecture 11 he had forgotten the reason for. The two notions differ only for infinitely many summands: the product $\prod_\alpha V_\alpha$ contains all families $(v_\alpha)$, while the direct sum $\bigoplus_\alpha V_\alpha$ contains only those with finitely many nonzero entries.

^rem-10-3

## The Differential of a Map Between Vector Spaces

*Lecture 7. “A careful analysis of what we did last time — last time I was rushing.” The $\mathrm{O}(n)$ argument computed a derivative by differentiating along straight lines and read off surjectivity from the result, without ever writing a Jacobian matrix. This subsection says exactly what that computes and why it is legitimate. “For now it's all linear algebra,” but it is also the template for the differential of a map between manifolds, to come.*

Throughout, $X$ and $Y$ are finite-dimensional real vector spaces, of dimensions $m$ and $n$, and $F : X \to Y$ is a map of sets.

> [!definition] Definition §10.6: Linear Coordinates and Coordinate Representation
> A **linear coordinate system** on $X$ is a linear isomorphism $L : X \to \mathbb{R}^m$ — equivalently, a choice of basis, $L$ sending a vector to its coordinate column. Given linear coordinate systems $L$ on $X$ and $K$ on $Y$, the **coordinate representation** of $F$ is
>
> $$
> \widetilde F = K \circ F \circ L^{-1} : \mathbb{R}^m \to \mathbb{R}^n .
> $$
>
> *Lee: Example 1.24*

^def-10-6

Since $L$ and $K$ are bijections, $\widetilde F$ is the unique map making the square commute:

![[m591-10-3.svg]]
*The coordinate representation $\widetilde F$ is $F$ read through the linear coordinate systems $L$ and $K$.*

$$
\widetilde F = K \circ F \circ L^{-1}.
$$

Commutativity means: apply $F$ and then take coordinates, or take coordinates and then apply $\widetilde F$; the result is the same. “$\widetilde F$ is just $F$ expressed in coordinates.”

> [!definition] Definition §10.7: Smooth Map Between Vector Spaces
> $F : X \to Y$ is **smooth** if $\widetilde F = K \circ F \circ L^{-1} : \mathbb{R}^m \to \mathbb{R}^n$ is smooth for any choice of linear coordinates $L, K$ — equivalently, by Lemma [[§10 Vector Spaces and Matrix Groups#^lem-10-8|§10.8]], for some choice.

^def-10-7

> [!theorem] Lemma §10.8: Independence of Coordinates
> If the coordinate representation $\widetilde F = K \circ F \circ L^{-1}$ of [[§10 Vector Spaces and Matrix Groups#^def-10-6|Def. §10.6]] is smooth for one choice of linear coordinates $L$ on $X$ and $K$ on $Y$, it is smooth for every choice. Hence “any” in [[§10 Vector Spaces and Matrix Groups#^def-10-7|Def. §10.7]] may be replaced by “some” — Uribe's “little observation” in Lecture 7.

^lem-10-8

> [!proof]+ Proof
> *(Not proved in lecture, where it was called “a little observation”; filled in.)* Let $L', K'$ be another choice, with $\widetilde F' = K' F L'^{-1}$. Then
>
> $$
> \widetilde F' = (K' K^{-1}) \circ \widetilde F \circ (L L'^{-1}),
> $$
>
> and $K'K^{-1} : \mathbb{R}^n \to \mathbb{R}^n$, $LL'^{-1} : \mathbb{R}^m \to \mathbb{R}^m$ are linear isomorphisms, hence smooth. A composite of smooth maps is smooth.

^pf-10-8

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Vector Spaces and Matrix Groups#^def-10-7|Def. §10.7]], [[Multivariable Chain Rule|452 §10.2]]

> [!theorem] Proposition §10.9: A Vector Space Is a Smooth Manifold
> Any two linear coordinate systems $L, L' : X \to \mathbb{R}^m$ on a finite-dimensional real vector space are $C^\infty$-compatible charts. Consequently $X$ carries a canonical smooth structure, the one generated by any single linear chart $(X, L)$, and a map $F : X \to Y$ is smooth in the sense of [[§10 Vector Spaces and Matrix Groups#^def-10-7|Def. §10.7]] iff it is smooth in the sense of [[§8 Differentiable Structures#^def-8-14|Def. §8.14]] for these structures.
>
> *Lee: Example 1.24*

^prop-10-9

> [!proof]+ Proof
> $L$ is a homeomorphism of $X$ (with the topology transported from $\mathbb{R}^m$, which is independent of $L$ since all norms on $\mathbb{R}^m$ are equivalent) onto the open set $\mathbb{R}^m$, so $(X, L)$ is a chart. The transition function $L' \circ L^{-1} : \mathbb{R}^m \to \mathbb{R}^m$ is a linear isomorphism, hence a diffeomorphism, so any two linear charts are compatible. By Theorem [[§8 Differentiable Structures#^thm-8-5|§8.5]] the one-chart atlas $\{(X,L)\}$ determines a smooth structure, and by compatibility it is the same structure for every $L$. For the last claim, the coordinate representation of $F$ in the linear charts $L$ and $K$ is precisely $K \circ F \circ L^{-1} = \widetilde F$.

^pf-10-9

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Vector Spaces and Matrix Groups#^def-10-7|Def. §10.7]], [[§8 Differentiable Structures#^def-8-1|Def. §8.1]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^thm-8-5|§8.5]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]]

> [!remark]- Connections
> - The one-chart atlas on $\mathbb{R}^n$: [[§8 Differentiable Structures#^ex-8-1|Ex. §8.1]]; its tangent spaces are the vector space itself, [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-26|§12.26]].

> [!definition] Definition §10.8: The Standard Smooth Structure on a Vector Space
> A finite-dimensional real vector space $X$ of dimension $m$ is given the topology for which one, hence every, linear coordinate system $L : X \to \mathbb{R}^m$ is a homeomorphism, and the smooth structure generated by one, hence every, **linear chart** $(X, L)$ — “hence every” by Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-9|§10.9]]. With these, $X$ is a smooth manifold of dimension $m$ whose linear coordinate systems are smooth charts.
>
> *Lee: Example 1.24*

^def-10-8

> [!remark] Remark
> This is the sense in which $\operatorname{Mat}(n,\mathbb{R})$, $\operatorname{Sym}(n,\mathbb{R})$, and $\operatorname{Mat}(n,\mathbb{C})$ are smooth manifolds without anyone having chosen coordinates on them. Uribe: “you can think of this as an abstract vector space that I make into a manifold by choosing a linear chart, and it won't matter which linear chart I choose — they are all smoothly compatible.”

^rem-10-4

Now suppose $F$ is smooth and fix $p \in X$. There is a second square, with the same vertical arrows but a *linear* map along the bottom: the linear map $\mathbb{R}^m \to \mathbb{R}^n$ given by the Jacobian matrix $\widetilde F'(\tilde p)$, where $\tilde p = L(p)$ is the coordinate vector of $p$.

> [!definition] Definition §10.9: The Differential
> Let $F : X \to Y$ be smooth and $p \in X$. Choose linear coordinates $L$ on $X$ and $K$ on $Y$, let $\widetilde F = K \circ F \circ L^{-1}$ be the coordinate representation ([[§10 Vector Spaces and Matrix Groups#^def-10-6|Def. §10.6]]), and put $\tilde p = L(p)$. The **differential** of $F$ at $p$ is the unique linear map $dF_p : X \to Y$ making the square commute:
>
> ![[m591-10-4.svg]]
>
> $$
> dF_p = K^{-1} \circ \widetilde F'(\tilde p) \circ L.
> $$

^def-10-9

> [!theorem] Theorem §10.10: Coordinate-Free Formula for the Differential
> Let $F : X \to Y$ be smooth and $p, v \in X$. Then
>
> $$
> dF_p(v) \;=\; \frac{d}{dt}\Big|_{t=0} F(p + tv) \;=\; \lim_{t \to 0} \frac{1}{t}\big( F(p+tv) - F(p) \big).
> $$
>
> In particular $dF_p$ does not depend on the choice of bases used to define it.
>
> *Lee: cf. Corollary 3.25*

^thm-10-10

> [!proof]+ Proof
> The curve $t \mapsto p + tv$ in $X$ has coordinate curve $t \mapsto L(p+tv) = \tilde p + t\,L(v)$ in $\mathbb{R}^m$, by linearity of $L$. Hence, writing $\tilde v = L(v)$,
>
> $$
> F(p+tv) = K^{-1}\big( \widetilde F(\tilde p + t \tilde v) \big).
> $$
>
> The map $t \mapsto \widetilde F(\tilde p + t\tilde v)$ is a smooth curve in $\mathbb{R}^n$, and by the [[Multivariable Chain Rule|chain rule]] its velocity at $t = 0$ is the Jacobian applied to the direction: $\frac{d}{dt}\big|_0 \widetilde F(\tilde p + t\tilde v) = \widetilde F'(\tilde p)\,\tilde v$. Since $K^{-1}$ is linear, it commutes with differentiation of curves, so
>
> $$
> \frac{d}{dt}\Big|_{t=0} F(p+tv) = K^{-1}\Big( \frac{d}{dt}\Big|_{t=0} \widetilde F(\tilde p + t\tilde v) \Big) = K^{-1}\big( \widetilde F'(\tilde p) L(v) \big) = dF_p(v).
> $$
>
> The second expression for $dF_p(v)$ is the definition of the derivative of the $Y$-valued curve $t \mapsto F(p+tv)$ at $t = 0$. The right-hand side of the displayed formula makes no reference to $L$ or $K$, so neither does $dF_p$.

^pf-10-10

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark]- Connections
> - In $\mathbb{R}^n$ this is the [[Directional Derivative Formula|directional derivative formula, 452 §7.1]], with the differential of [[§8 The Differential#^def-8-1|452 Def. §8.1]].
> - On manifolds: agreement with the abstract differential, [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]]; computing differentials by curves, [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-31|§12.31]].

> [!remark] Remark
> Two things are worth isolating. First, the hypothesis that $F$ is smooth is used: it is what makes $\widetilde F$ differentiable so that the chain rule applies. A map can have all directional derivatives $\frac{d}{dt}\big|_0 F(p+tv)$ at a point without being differentiable there, and for such a map the formula defines nothing linear. Second, the formula uses the vector space structure of *both* spaces, in two different places: that of $X$ to form the line $p + tv$, and that of $Y$ to form the difference quotient $\frac1t\big(F(p+tv) - F(p)\big)$. Uribe stopped to ask the class where $Y$'s structure enters, and this is the answer. Neither can be dropped, which is why the same formula will *not* serve as the definition of the differential on a general manifold: there is no “$p + tv$” and no “$F(p+tv) - F(p)$.” That is the problem [[§11 Tangent Spaces I꞉ The Geometric Picture|§11]] begins to address.

^rem-10-5

> [!theorem] Corollary §10.11: Regular Values Without Coordinates
> Suppose $\dim X \ge \dim Y$ and $F : X \to Y$ is smooth, and let $\widetilde F = K \circ F \circ L^{-1}$ and $\tilde p = L(p)$ be taken in linear coordinates $L$, $K$, as in [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]]. Then for $p \in X$,
>
> $$
> \widetilde F'(\tilde p) \text{ has maximal rank } (= \dim Y) \iff dF_p : X \to Y \text{ is surjective},
> $$
>
> and this holds for one choice of coordinates iff for all. Hence $c \in Y$ is a regular value of $F$ iff $dF_p$ is surjective for every $p \in F^{-1}(c)$, a statement that involves no bases.

^cor-10-11

> [!proof]+ Proof
> Since $m \ge n$, the maximal possible rank of an $n \times m$ matrix is $n$, and $\widetilde F'(\tilde p)$ has rank $n$ iff the linear map $\mathbb{R}^m \to \mathbb{R}^n$ it defines is surjective. In the square of [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]] the vertical arrows are bijections, so the bottom arrow is surjective iff the top arrow $dF_p$ is. The top arrow is independent of coordinates by Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]], so surjectivity of $\widetilde F'(\tilde p)$ is too.

^pf-10-11

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]], [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]]

> [!remark]- Connections
> - The manifold versions of this definition of regular value: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-13|Def. §12.13]], [[§14 Local Diffeomorphisms and Submersions#^def-14-3|Def. §14.3]].

> [!remark] Remark: What the Curve Method Computes
> Read together, Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]] and Corollary [[§10 Vector Spaces and Matrix Groups#^cor-10-11|§10.11]] are the license for the computation in [[§10 Vector Spaces and Matrix Groups#The Orthogonal Group as a Smooth Manifold|The Orthogonal Group as a Smooth Manifold]]. The board computation $\frac{d}{dt}\big|_0 F(g + tA)$ is not a shortcut around the Jacobian — it *is* the Jacobian, packaged as the linear map $A \mapsto dF_g(A)$ and read off without coordinates; and the surjectivity of that linear map *is* the maximal-rank condition, likewise without coordinates. Written as a matrix, $dF_g$ for $\mathrm{O}(n)$ would have $n(n+1)/2$ rows and $n^2$ columns of partial derivatives. None of it is needed. “Using curves to compute differentials is a basic technique in this subject.”

^rem-10-6

## The Orthogonal Group as a Smooth Manifold

The promise of [[§5 Topological Groups and Classical Matrix Groups#The Classical Groups Are Topological Manifolds|§5, The Classical Groups Are Topological Manifolds]] can now be kept, with [[§10 Vector Spaces and Matrix Groups#The Differential of a Map Between Vector Spaces|The Differential of a Map Between Vector Spaces]] supplying the meaning of every step.

> [!definition] Definition §10.10: Symmetric Matrices as a Euclidean Space
> Let $\operatorname{Sym}(n,\mathbb{R}) = \{\, S \in \operatorname{Mat}(n,\mathbb{R}) \mid S^{\mathsf T} = S \,\}$. It is a linear subspace of $\operatorname{Mat}(n,\mathbb{R})$, and the entries on and above the diagonal are free while those below are determined, so
>
> $$
> \dim \operatorname{Sym}(n,\mathbb{R}) = n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}.
> $$
>
> Reading off those entries in a fixed order gives a linear isomorphism $\operatorname{Sym}(n,\mathbb{R}) \cong \mathbb{R}^{n(n+1)/2}$, which we use to regard maps into $\operatorname{Sym}(n,\mathbb{R})$ as maps into a Euclidean space. Being linear, it changes neither smoothness nor rank.

^def-10-10

> [!example] Example §10.1: $\mathrm{O}(n)$ Is a Smooth Manifold of Dimension $\tfrac{n(n-1)}{2}$
> Define
>
> $$
> F : \operatorname{Mat}(n,\mathbb{R}) \longrightarrow \operatorname{Sym}(n,\mathbb{R}), \qquad F(g) = g\, g^{\mathsf T}.
> $$
>
> Then $\mathrm{O}(n) = F^{-1}(I)$, the identity $I$ is a regular value of $F$, and consequently $\mathrm{O}(n)$ is a smooth manifold of dimension $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$.
>
> *Lee: Example 7.27*

^ex-10-1

> [!proof]+ Proof
> *$F$ is well defined and smooth.* $(gg^{\mathsf T})^{\mathsf T} = g^{\mathsf T\mathsf T} g^{\mathsf T} = g g^{\mathsf T}$, so $F$ does land in $\operatorname{Sym}(n,\mathbb{R})$. Each entry $(gg^{\mathsf T})_{ij} = \sum_m g_{im}g_{jm}$ is a quadratic polynomial in the coordinates of [[§5 Topological Groups and Classical Matrix Groups#^def-5-2|Def. §5.2]], so $F$ is smooth.
>
> *$\mathrm{O}(n) = F^{-1}(I)$.* By Proposition [[§5 Topological Groups and Classical Matrix Groups#^prop-5-7|§5.7]], $g \in \mathrm{O}(n) \iff g^{-1} = g^{\mathsf T} \iff gg^{\mathsf T} = I$.
>
> *The differential as a linear map.* *(Lecture 6: “We're not going to compute [the] Jacobian of this thing… You use curves” — a technique he could “not emphasize enough”.)* $\operatorname{Mat}(n,\mathbb{R})$ and $\operatorname{Sym}(n,\mathbb{R})$ are finite-dimensional vector spaces and $F$ is smooth between them, so by Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]] the differential is computed along lines: for $g \in F^{-1}(I)$ and any $A \in \operatorname{Mat}(n,\mathbb{R})$, $dF_g(A) = \frac{d}{dt}\big|_{t=0} F(g+tA)$. Expanding,
>
> $$
> F(g+tA) = (g+tA)(g^{\mathsf T} + tA^{\mathsf T}) = g g^{\mathsf T} + t\big(A g^{\mathsf T} + g A^{\mathsf T}\big) + t^2 A A^{\mathsf T},
> $$
>
> so
>
> $$
> dF_g(A) = A g^{\mathsf T} + g A^{\mathsf T}.
> $$
>
> This is visibly symmetric, as it must be: $(Ag^{\mathsf T} + gA^{\mathsf T})^{\mathsf T} = gA^{\mathsf T} + Ag^{\mathsf T}$.
>
> *$dF_g$ is surjective.* *(Lecture 6 observed that the left side is twice the symmetric part of a matrix, which is the substitution below; Lecture 7 finished with the explicit choice $A = \tfrac12 Sg$ — the equation “looks like a hard equation to solve until you realize that you have to use the fact that $S$ is symmetric and that $g$ is orthogonal.”)* Put $X = Ag^{\mathsf T}$, so that $dF_g(A) = X + X^{\mathsf T}$. Since $g$ is invertible, $A \mapsto Ag^{\mathsf T}$ is a linear *bijection* of $\operatorname{Mat}(n,\mathbb{R})$, and therefore
>
> $$
> \operatorname{im} F'(g) = \{\, X + X^{\mathsf T} \mid X \in \operatorname{Mat}(n,\mathbb{R}) \,\} = \operatorname{Sym}(n,\mathbb{R}),
> $$
>
> the last equality because $X + X^{\mathsf T}$ is always symmetric, and conversely any symmetric $S$ arises from $X = \tfrac12 S$. Unwinding the substitution gives the matrix explicitly: $A = X (g^{\mathsf T})^{-1} = \tfrac12 S g$, using $(g^{\mathsf T})^{-1} = g$ for orthogonal $g$. Directly, with $A = \tfrac12 Sg$:
>
> $$
> A g^{\mathsf T} = \tfrac12 S g g^{\mathsf T} = \tfrac12 S, \qquad
> g A^{\mathsf T} = g \big(\tfrac12 S g\big)^{\mathsf T} = \tfrac12 g\, g^{\mathsf T} S^{\mathsf T} = \tfrac12 S,
> $$
>
> using $gg^{\mathsf T} = I$ and $S^{\mathsf T} = S$; adding gives $dF_g(A) = S$.
>
> ![[m591-10-5.svg]]
>
> The same argument as a diagram: a bijection followed by symmetrization, which is onto. The unitary case in [[§10 Vector Spaces and Matrix Groups#The Unitary Group as a Smooth Manifold|The Unitary Group as a Smooth Manifold]] has exactly this shape, with ${}^{\mathsf T}$ replaced by ${}^*$.
>
> *Conclusion.* $dF_g$ is surjective onto $\operatorname{Sym}(n,\mathbb{R})$ for every $g \in F^{-1}(I)$. By Corollary [[§10 Vector Spaces and Matrix Groups#^cor-10-11|§10.11]] (here $\dim \operatorname{Mat} = n^2 \ge \tfrac{n(n+1)}{2} = \dim \operatorname{Sym}$), this says that in any linear coordinates the Jacobian has maximal rank $k = \tfrac{n(n+1)}{2}$ at every point of $F^{-1}(I)$, i.e. $I$ is a regular value ([[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]]). Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]] applies with $n + k = n^2$: $\mathrm{O}(n)$ is a smooth manifold of dimension $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$.

^pf-ex-10-1

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-10|Def. §10.10]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-2|Def. §5.2]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-6|Def. §5.6]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-7|§5.7]], [[§10 Vector Spaces and Matrix Groups#^def-10-8|Def. §10.8]], [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]], [[§10 Vector Spaces and Matrix Groups#^cor-10-11|§10.11]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]], [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]]

> [!remark]- Connections
> - $\mathrm{O}(n)$ as a group in 493: [[Matrix groups GLₙ, SLₙ and O(n)]]; the analogous level-set argument for $\mathrm{SL}(n,\mathbb{R})$: [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5.13]].
> - Its tangent spaces: [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|Ex. §11.2]]; all classical groups: [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]].

> [!remark] Remark
> **The codomain is not a cosmetic choice.** It is essential that $F$ be regarded as a map into $\operatorname{Sym}(n,\mathbb{R})$ and not into $\operatorname{Mat}(n,\mathbb{R})$. Since $F(g)$ is always symmetric, $\operatorname{im} F \subseteq \operatorname{Sym}(n,\mathbb{R}) \subsetneq \operatorname{Mat}(n,\mathbb{R})$, so $F'(g)$ could never be surjective onto $\operatorname{Mat}(n,\mathbb{R})$; with that codomain $I$ would fail to be a regular value at every point and the theorem would yield nothing. Choosing the codomain to be exactly the space the map lands in is what makes the rank condition attainable — and it is also what produces the right dimension count, since $\dim \mathrm{O}(n) = n^2 - \dim(\text{codomain})$.

^rem-10-7

> [!remark] Remark
> The smooth structure obtained is independent of the linear coordinates used to identify $\operatorname{Mat}(n,\mathbb{R})$ with $\mathbb{R}^{n^2}$ and $\operatorname{Sym}(n,\mathbb{R})$ with $\mathbb{R}^{n(n+1)/2}$: two such identifications differ by linear isomorphisms, which are diffeomorphisms, so the level set $F^{-1}(I)$ and its graph charts transport across them without change (Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-9|§10.9]]). “There's no ambiguity.”

^rem-10-8

> [!theorem] Proposition §10.12: The Kernel of the Differential
> With $F(g) = gg^{\mathsf T}$ as above, for every $g \in \mathrm{O}(n)$,
>
> $$
> \ker dF_g = \{\, A \in \operatorname{Mat}(n,\mathbb{R}) \mid gA^{\mathsf T} + Ag^{\mathsf T} = 0 \,\} = g \cdot \operatorname{Skew}(n,\mathbb{R}),
> $$
>
> where $\operatorname{Skew}(n,\mathbb{R}) = \{B \mid B^{\mathsf T} = -B\}$. In particular $\ker dF_I = \operatorname{Skew}(n,\mathbb{R})$, and $\dim \ker dF_g = \tfrac{n(n-1)}{2}$ for every $g$.

^prop-10-12

> [!proof]+ Proof
> The first equality is the definition of the kernel. For the second, since $g$ is invertible every $A$ can be written uniquely as $A = gB$ with $B = g^{-1}A$. Substituting, and using $A^{\mathsf T} = B^{\mathsf T} g^{\mathsf T}$,
>
> $$
> gA^{\mathsf T} + Ag^{\mathsf T} = g B^{\mathsf T} g^{\mathsf T} + g B g^{\mathsf T} = g\,(B^{\mathsf T} + B)\,g^{\mathsf T}.
> $$
>
> As $g$ and $g^{\mathsf T}$ are invertible, this vanishes iff $B + B^{\mathsf T} = 0$, i.e. iff $B$ is skew-symmetric. Hence $\ker dF_g = \{gB \mid B \in \operatorname{Skew}(n,\mathbb{R})\}$. At $g = I$ the description reads $\ker dF_I = \operatorname{Skew}(n,\mathbb{R})$ directly: $dF_I(A) = A^{\mathsf T} + A$. Left multiplication by $g$ is a linear isomorphism of $\operatorname{Mat}(n,\mathbb{R})$, so $\dim \ker dF_g = \dim \operatorname{Skew}(n,\mathbb{R})$ for every $g$.
>
> *Counting.* A skew-symmetric matrix has zero diagonal ($B_{ii} = -B_{ii}$) and its entries below the diagonal are the negatives of those above, so it is determined by the $\tfrac{n(n-1)}{2}$ entries strictly above the diagonal, which may be chosen freely:
>
> $$
> B = \begin{pmatrix} 0 & \ast \\ -(\ast)^{\mathsf T} & \ddots \end{pmatrix}, \qquad \dim \operatorname{Skew}(n,\mathbb{R}) = \binom{n}{2} = \frac{n(n-1)}{2}.
> $$

^pf-10-12

*Uses:* [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Ex. §10.1]], [[§10 Vector Spaces and Matrix Groups#^def-10-9|Def. §10.9]]

> [!remark]- Connections
> - This kernel is the geometric tangent space $T^{\mathrm{geo}}_g\mathrm{O}(n)$: [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|Ex. §11.2]].

> [!remark] Remark: Two Readings of the Dimension
> A student asked for a combinatorial reason that $\dim \mathrm{O}(n) = \tfrac{n(n-1)}{2}$, “like choosing two out of $n$.” There are now two: the level-set count $n^2 - \tfrac{n(n+1)}{2}$ from the regular value theorem, and the kernel count $\binom{n}{2}$ from Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-12|§10.12]]. They agree by [[§10 Vector Spaces and Matrix Groups#^prop-10-1|rank–nullity]]: $dF_g$ is surjective onto a space of dimension $\tfrac{n(n+1)}{2}$, so its kernel has dimension $n^2 - \tfrac{n(n+1)}{2}$. The kernel is not yet officially anything, but Uribe named it ahead of time: it is the *geometric tangent space* $T^{\mathrm{geo}}_g\mathrm{O}(n)$ to $\mathrm{O}(n)$ at $g$ (see [[§11 Tangent Spaces I꞉ The Geometric Picture|§11]]), and at $g = I$ the skew-symmetric matrices will be the *Lie algebra* $\mathfrak{so}(n)$, “in some number of weeks.” The same move produced $\nabla\det$ in Proposition [[§5 Topological Groups and Classical Matrix Groups#^prop-5-9|§5.9]], and it will recur whenever a classical group is presented as a level set.

^rem-10-9

> [!theorem] Corollary §10.13: Consequences
> $\mathrm{SO}(n)$ is a smooth manifold of dimension $\tfrac{n(n-1)}{2}$, and $\mathrm{O}(n)$ is compact.
>
> *Lee: Example 7.27*

^cor-10-13

> [!proof]+ Proof
> $\mathrm{SO}(n) = \mathrm{O}(n) \cap \det^{-1}(0,\infty)$ is an open subset of $\mathrm{O}(n)$ ($\det$ is continuous and takes only the values $\pm1$ on $\mathrm{O}(n)$, so $\mathrm{SO}(n)$ is also closed), and an open subset of a smooth $m$-manifold is a smooth $m$-manifold, its charts being restrictions of the given ones. Compactness of $\mathrm{O}(n)$ was shown in Corollary [[§7 Homogeneous Spaces#^cor-7-13|§7.13]]: it is closed as $F^{-1}(I)$ with $F$ continuous, and bounded because every column of an orthogonal matrix is a unit vector.

^pf-10-13

*Uses:* [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Ex. §10.1]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-7|Def. §5.7]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-3|§5.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-6|§3.6]], [[§7 Homogeneous Spaces#^cor-7-13|§7.13]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §15.12]]

> [!remark]- Connections
> - Compactness is [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]].

**Transcription note.** Page 20 of the handwritten notes writes “$\ker dF_g(A) = \{A \mid gA^{\mathsf T} + Ag^{\mathsf T} = 0\}$”; the kernel is of the linear map $dF_g$, and the “$(A)$” does not belong. The transposes sit to the right of $g$ throughout because that is how $F$ was written ($gg^{\mathsf T}$, not $g^{\mathsf T}g$); either convention defines $\mathrm{O}(n)$.

The unitary group $\mathrm{U}(n)$ is treated the same way, with $F(g) = gg^*$ mapping into the Hermitian matrices, in [[§10 Vector Spaces and Matrix Groups#The Unitary Group as a Smooth Manifold|The Unitary Group as a Smooth Manifold]]. The analogue for $\mathrm{SL}(n,\mathbb{R})$ was Corollary [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5.13]], which Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]] now upgrades from a topological to a smooth manifold.

> [!remark] Remark: Where This Leaves Us
> Every level set met so far is now a smooth manifold: $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, the spheres, and any surface cut out by a regular value. What remains owed is the global half of the internal picture: a manifold defined abstractly, not sitting inside any $\mathbb{R}^N$, has no external description until one knows it can be embedded in a Euclidean space at all. That is Whitney's embedding theorem, later in the course.

^rem-10-10

## The Unitary Group as a Smooth Manifold

*Assignment 2, Problem 4. The argument is that of [[§10 Vector Spaces and Matrix Groups#The Orthogonal Group as a Smooth Manifold|The Orthogonal Group as a Smooth Manifold]] with one change that is easy to get wrong: the spaces involved are complex, but the map is not complex-linear, so everything must be done over $\mathbb{R}$.*

Write $A^* = \bar A^{\mathsf T}$ for the conjugate transpose, so that $\mathrm{U}(n) = \{g \in \operatorname{Mat}(n,\mathbb{C}) \mid g^* g = I\}$. Throughout, $\operatorname{Mat}(n,\mathbb{C})$ is regarded as a *real* vector space of dimension $2n^2$ ([[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]]).

> [!definition] Definition §10.11: Hermitian Matrices as a Real Vector Space
> Let $\operatorname{Herm}(n) = \{A \in \operatorname{Mat}(n,\mathbb{C}) \mid A^* = A\}$. It is closed under addition and under multiplication by *real* scalars, so it is a real vector space; it is *not* a complex subspace, since $(iA)^* = -iA$. A Hermitian matrix has real diagonal entries ($a_{jj} = \overline{a_{jj}}$), arbitrary complex entries above the diagonal, and entries below the diagonal determined by $a_{kj} = \overline{a_{jk}}$. Hence
>
> $$
> \dim_{\mathbb{R}} \operatorname{Herm}(n) = n + 2\binom{n}{2} = n^2 ,
> $$
>
> and reading off the real diagonal entries and the real and imaginary parts of the entries above the diagonal gives a linear isomorphism $\operatorname{Herm}(n) \cong \mathbb{R}^{n^2}$.

^def-10-11

> [!remark]- Connections
> - Hermitian matrices are the matrices of self-adjoint operators: [[§22 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]], with the conjugate transpose of [[§22 Self-Adjoint and Normal Operators#^ladr-7-7|LADR 7.7]].

> [!theorem] Lemma §10.14: A One-Sided Inverse Suffices
> If $g \in \operatorname{Mat}(n,\mathbb{C})$ satisfies $gg^* = I$, then also $g^*g = I$. Consequently $\mathrm{U}(n) = \{g \mid gg^* = I\}$.

^lem-10-14

> [!proof]+ Proof
> Taking determinants, $\det(g)\det(g^*) = 1$, so $\det g \neq 0$ and $g$ is invertible. Multiplying $gg^* = I$ on the left by $g^{-1}$ gives $g^* = g^{-1}$, hence $g^*g = I$.

^pf-10-14

*Uses:* [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[Invertible ⟺ nonzero determinant|LADR 9.50]]

> [!remark]- Connections
> - The general linear-algebra fact: [[§10 Invertibility and Isomorphisms#^ladr-3-68|LADR 3.68 (ST = I ⟺ TS = I)]]; unitary matrices in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].

> [!example] Example §10.2: $\mathrm{U}(n)$ Is a Smooth Manifold of Dimension $n^2$
> Define
>
> $$
> F : \operatorname{Mat}(n,\mathbb{C}) \longrightarrow \operatorname{Herm}(n), \qquad F(g) = g g^*,
> $$
>
> both regarded as real vector spaces. Then $\mathrm{U}(n) = F^{-1}(I)$, the identity is a regular value, and $\mathrm{U}(n)$ is a smooth manifold of dimension $2n^2 - n^2 = n^2$.
>
> *Lee: Example 7.29*

^ex-10-2

![[m591-10-6.svg]]
*The map $F(g) = gg^*$ and its coordinate representation $\widehat F$ under the real-linear identifications $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ and $\operatorname{Herm}(n) \cong \mathbb{R}^{n^2}$.*

The vertical arrows are the real-linear identifications of [[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]] and [[§10 Vector Spaces and Matrix Groups#^def-10-11|Def. §10.11]]. This is the square of [[§10 Vector Spaces and Matrix Groups#The Differential of a Map Between Vector Spaces|The Differential of a Map Between Vector Spaces]] with $X = \operatorname{Mat}(n,\mathbb{C})$ and $Y = \operatorname{Herm}(n)$ regarded as real vector spaces: $F$ is smooth, and $I$ is a regular value, exactly when the same holds for $\widehat F$ (Lemma [[§10 Vector Spaces and Matrix Groups#^lem-10-8|§10.8]], Corollary [[§10 Vector Spaces and Matrix Groups#^cor-10-11|§10.11]]). Nothing is computed in the bottom row; it only certifies that the top row may be used.

> [!proof]+ Proof
> *$F$ is well defined and smooth.* $(gg^*)^* = g^{**}g^* = gg^*$, so $F$ lands in $\operatorname{Herm}(n)$. Each entry $(gg^*)_{jk} = \sum_m g_{jm}\overline{g_{km}}$ has real and imaginary parts that are quadratic polynomials in the real coordinates of $g$, so $F$ is smooth ([[§10 Vector Spaces and Matrix Groups#^def-10-7|Def. §10.7]]).
>
> *$\mathrm{U}(n) = F^{-1}(I)$.* Lemma [[§10 Vector Spaces and Matrix Groups#^lem-10-14|§10.14]].
>
> *The differential.* By Theorem [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]], for $g \in F^{-1}(I)$ and $h \in \operatorname{Mat}(n,\mathbb{C})$, $dF_g(h) = \frac{d}{dt}\big|_{t=0} F(g+th)$ with $t$ *real*. Since $(th)^* = t h^*$ for real $t$,
>
> $$
> F(g+th) = (g+th)(g^* + th^*) = gg^* + t\big(hg^* + gh^*\big) + t^2\, hh^*,
> \qquad\text{so}\qquad
> dF_g(h) = hg^* + gh^* ,
> $$
>
> which is Hermitian, as it must be.
>
> *$dF_g$ is surjective.* Put $X = hg^*$; then $gh^* = (hg^*)^* = X^*$, so $dF_g(h) = X + X^*$. As $g$ is invertible, $h \mapsto hg^*$ is a real-linear bijection of $\operatorname{Mat}(n,\mathbb{C})$, with inverse $X \mapsto Xg$. Hence $\operatorname{im} dF_g = \{X + X^* \mid X \in \operatorname{Mat}(n,\mathbb{C})\} = \operatorname{Herm}(n)$, since any Hermitian $A$ arises from $X = \tfrac12 A$. Explicitly $h = \tfrac12 Ag$:
>
> $$
> hg^* = \tfrac12 A gg^* = \tfrac12 A, \qquad gh^* = \tfrac12\, g g^* A^* = \tfrac12 A .
> $$
>
> ![[m591-10-7.svg]]
>
> The surjectivity argument as a diagram: $dF_g$ factors as a bijection followed by $X \mapsto X + X^*$, and the second map is onto $\operatorname{Herm}(n)$, hitting $A$ at $X = \tfrac12 A$. Hence $dF_g$ is onto.
>
> *Conclusion.* $\dim_{\mathbb{R}}\operatorname{Mat}(n,\mathbb{C}) = 2n^2 \ge n^2 = \dim_{\mathbb{R}}\operatorname{Herm}(n)$, so by Corollary [[§10 Vector Spaces and Matrix Groups#^cor-10-11|§10.11]] surjectivity of $dF_g$ at every $g \in F^{-1}(I)$ is exactly the statement that $I$ is a regular value. Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]] makes $\mathrm{U}(n)$ a smooth manifold of dimension $2n^2 - n^2 = n^2$.

^pf-ex-10-2

*Uses:* [[§10 Vector Spaces and Matrix Groups#^def-10-11|Def. §10.11]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]], [[§10 Vector Spaces and Matrix Groups#^def-10-7|Def. §10.7]], [[§10 Vector Spaces and Matrix Groups#^lem-10-8|§10.8]], [[§10 Vector Spaces and Matrix Groups#^lem-10-14|§10.14]], [[§10 Vector Spaces and Matrix Groups#^thm-10-10|§10.10]], [[§10 Vector Spaces and Matrix Groups#^cor-10-11|§10.11]], [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]]

> [!remark]- Connections
> - Unitary matrices in LADR: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]]; $\mathrm{U}(1)$ is the circle, [[§5 Topological Groups and Classical Matrix Groups#^ex-5-4|Ex. §5.4]].
> - Its tangent spaces: [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3|Ex. §11.3]].

> [!remark] Remark
> **Why over $\mathbb{R}$.** The derivative $h \mapsto hg^* + gh^*$ is real-linear but not complex-linear: $dF_g(ih) = i\,hg^* - i\,gh^*$, which differs from $i\,dF_g(h)$ unless $gh^* = 0$. This is the conjugation in $g^*$ at work, and it is why Problem 4 insists that both spaces be regarded as real vector spaces. It is also why the holomorphic regular value theorem of [[§4 The Regular Value Theorem#Holomorphic Level Sets|§4, Holomorphic Level Sets]] does not apply, and why $\dim \mathrm{U}(n) = n^2$ can be odd, which no holomorphic level set can.

^rem-10-11

> [!theorem] Proposition §10.15: The Kernel of the Differential
> For $g \in \mathrm{U}(n)$,
>
> $$
> \ker dF_g = \mathfrak{u}(n)\cdot g = g \cdot \mathfrak{u}(n), \qquad \mathfrak{u}(n) = \{X \in \operatorname{Mat}(n,\mathbb{C}) \mid X^* = -X\},
> $$
>
> the skew-Hermitian matrices, and $\dim_{\mathbb{R}} \mathfrak{u}(n) = n^2$.

^prop-10-15

> [!proof]+ Proof
> Every $h$ can be written uniquely as $h = Xg$ with $X = hg^*$, and then $dF_g(Xg) = Xgg^* + gg^*X^* = X + X^*$, which vanishes iff $X \in \mathfrak{u}(n)$. So $\ker dF_g = \mathfrak{u}(n)\cdot g$. For the second description, conjugation by $g$ preserves $\mathfrak{u}(n)$: if $X^* = -X$ then $(gXg^*)^* = gX^*g^* = -gXg^*$; so $g \cdot \mathfrak{u}(n) = (g\,\mathfrak{u}(n)\,g^{-1})\cdot g = \mathfrak{u}(n)\cdot g$. A skew-Hermitian matrix has purely imaginary diagonal ($n$ real parameters) and arbitrary complex entries above the diagonal ($2\binom n2$ real parameters), so $\dim_{\mathbb{R}}\mathfrak{u}(n) = n^2$ — agreeing with $\dim \mathrm{U}(n)$ by [[§10 Vector Spaces and Matrix Groups#^prop-10-1|rank–nullity]], $2n^2 - n^2$.

^pf-10-15

*Uses:* [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Ex. §10.2]], [[§10 Vector Spaces and Matrix Groups#^lem-10-14|§10.14]], [[§10 Vector Spaces and Matrix Groups#^prop-10-1|§10.1]]

> [!remark]- Connections
> - The geometric tangent space of $\mathrm{U}(n)$: [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3|Ex. §11.3]]; the orthogonal analogue: [[§10 Vector Spaces and Matrix Groups#^prop-10-12|§10.12]].

> [!theorem] Corollary §10.16: $\mathrm{U}(n)$ Is Compact
> $\mathrm{U}(n)$ is a compact smooth manifold of dimension $n^2$.
>
> *Lee: Example 7.29*

^cor-10-16

> [!proof]+ Proof
> It is closed in $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ as $F^{-1}(I)$ with $F$ continuous, and bounded because the columns of a unitary matrix are unit vectors of $\mathbb{C}^n$, so every entry has modulus at most $1$. Apply Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](1).

^pf-10-16

*Uses:* [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Ex. §10.2]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem|590 §15.12]]

> [!remark]- Connections
> - Proposition §1.8(1) is [[Heine–Borel Theorem|590 §15.12 (Heine–Borel)]]; columns of unitary matrices are orthonormal by [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].
