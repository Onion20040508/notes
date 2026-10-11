---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 21
tags: [differentiable-manifolds, math591]
---
← [[§20 Manifolds in Euclidean Space]] · ↑ [[· 3 Smooth Structures]] · [[§22 The Differential of a Map Between Vector Spaces]] →

*Stage: linear — The tool both tangent spaces will need: the linear algebra used from here on. The differential of a map between vector spaces ([[§22 The Differential of a Map Between Vector Spaces|§22]]) and the smooth matrix groups ([[§23 The Orthogonal and Unitary Groups as Smooth Manifolds|§23]]) follow.*

*Not from lecture. From here on the course runs on linear algebra — differentials, bases of tangent spaces, dual spaces — and this section records, once, the facts used. The first box is imported from linear algebra without proof, as the point-set facts of [[§1 Point-Set Topology Review|§1]] were imported from 590; everything after it is proved.* Throughout, vector spaces are real.

> [!theorem] Proposition §21.1: Standing Facts from Linear Algebra
> Let $A : V \to W$ be linear, with $V$ and $W$ finite-dimensional.
> 1. *Rank–nullity.* $\dim V = \dim\ker A + \operatorname{rank} A$. Consequently: if $A$ is injective then $\dim V \le \dim W$; if $A$ is surjective then $\dim V \ge \dim W$; and if $\dim V = \dim W$, then $A$ is injective $\iff$ surjective $\iff$ bijective.
> 2. *Bases determine linear maps.* A linear map is determined by its values on a basis, and any assignment of values to the vectors of a basis extends uniquely to a linear map. In particular, two linear maps that agree on a basis are equal.
> 3. *Matrices.* Given bases $(e_1, \ldots, e_m)$ of $V$ and $(f_1, \ldots, f_n)$ of $W$, the matrix $[A] = (a_{ij})$ of $A$ is defined by $A e_j = \sum_i a_{ij} f_i$: its $j$-th *column* holds the coordinates of $Ae_j$. Composition corresponds to matrix multiplication, $[AB] = [A][B]$, and $\operatorname{rank} A$ is the rank of $[A]$, which equals the rank of its transpose.
> 4. *Change of basis.* If $e'_j = \sum_i P_{ij}\, e_i$ and $f'_l = \sum_k Q_{kl}\, f_k$ are new bases, with $P$ and $Q$ invertible, then the matrix of $A$ in the new bases is $Q^{-1} [A] P$.
>
> *Lee: Corollary B.21 and Proposition B.24*

^prop-21-1

> [!remark]- Connections
> - (1): [[Fundamental theorem of linear maps|LADR 3.21 (fundamental theorem of linear maps)]], [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]], [[§8 Null Spaces and Ranges#^ladr-3-24|3.24]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]].
> - (2): [[Linear map lemma|LADR 3.4 (linear map lemma)]]. (3): [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[§9 Matrices#^ladr-3-57|LADR 3.57 (column rank equals row rank)]]. (4): [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84 (change-of-basis formula)]].

> [!proof]+ Proof (to be filled)
> Imported from linear algebra without proof; proved in Axler, *Linear Algebra Done Right* — see the [[Linear Algebra]] notes and the links under Connections above (also Lee, Corollary B.21 and Proposition B.24). To be filled.

^pf-21-1

> [!definition] Definition §21.1: Dual Space
> The **dual space** of $V$ is $V^{\ast} = \{\lambda : V \to \mathbb{R} \mid \lambda \text{ linear}\}$, a vector space under pointwise operations; its elements are **linear functionals**, or **covectors**.
>
> *Lee: Proposition 11.1*

^def-21-1

> [!definition] Definition §21.2: Dual Basis
> If $(e_1, \ldots, e_n)$ is a basis of $V$, the **dual basis** $(\varepsilon^1, \ldots, \varepsilon^n)$ consists of the covectors ([[§21 Linear Algebra Toolkit#^def-21-1|Definition §21.1]]) with
>
> $$
> \varepsilon^i(e_j) = \delta^i_j ,
> $$
>
> which exist and are unique by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2).
>
> *Lee: Proposition 11.1*

^def-21-2

> [!remark]- Connections
> - Home in linear algebra (written $V'$ there): [[§12 Duality#^ladr-3-110|LADR 3.110 (dual space)]], [[§12 Duality#^ladr-3-112|LADR 3.112 (dual basis)]].
> - Applied to $T_pM$: the cotangent space, [[§32 The Cotangent Space#^def-32-4|Def. §32.4]].

> [!theorem] Proposition §21.2: The Dual Basis
> Let $(e_1, \ldots, e_n)$ be a basis of $V$ with dual basis $(\varepsilon^1, \ldots, \varepsilon^n)$. Then $(\varepsilon^i)$ is a basis of $V^*$, so $\dim V^* = \dim V$, and for all $v \in V$ and $\lambda \in V^*$,
>
> $$
> v = \sum_{i=1}^n \varepsilon^i(v)\, e_i, \qquad\qquad \lambda = \sum_{i=1}^n \lambda(e_i)\, \varepsilon^i .
> $$
>
> *Lee: Proposition 11.1*

^prop-21-2

> [!proof]+ Proof
> Three things are to be shown: the two formulas, and that $(\varepsilon^i)$ is a basis of $V^{\ast}$. Throughout, the defining property $\varepsilon^i(e_j) = \delta^i_j$ (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]) and the pointwise operations of $V^{\ast}$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]) are used.
>
> *First formula.* Let $v \in V$. Since $(e_j)$ is a basis, $v = \sum_j v^j e_j$ for unique numbers $v^j$. Applying the linear map $\varepsilon^i$,
>
> $$
> \varepsilon^i(v) = \varepsilon^i\Big(\sum_{j=1}^n v^j e_j\Big) = \sum_{j=1}^n v^j\, \varepsilon^i(e_j) = \sum_{j=1}^n v^j \delta^i_j = v^i ,
> $$
>
> which is the first formula: substituting $v^i = \varepsilon^i(v)$ into $v = \sum_i v^i e_i$ gives $v = \sum_i \varepsilon^i(v)\, e_i$. The dual basis *extracts the components* of a vector.
>
> *Second formula.* Let $\lambda \in V^{\ast}$ and put $\mu = \sum_i \lambda(e_i)\, \varepsilon^i$, a linear combination of covectors, hence a covector. Both $\lambda$ and $\mu$ are linear maps $V \to \mathbb{R}$, so by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2) it suffices that they agree on each $e_j$. Evaluating pointwise,
>
> $$
> \mu(e_j) = \sum_{i=1}^n \lambda(e_i)\, \varepsilon^i(e_j) = \sum_{i=1}^n \lambda(e_i)\, \delta^i_j = \lambda(e_j) .
> $$
>
> So $\lambda = \mu = \sum_i \lambda(e_i)\, \varepsilon^i$; hence the $\varepsilon^i$ span $V^{\ast}$.
>
> *Independence.* Suppose $\sum_i c_i \varepsilon^i = 0$, the zero covector. Applying it to $e_j$,
>
> $$
> 0 = \Big(\sum_{i=1}^n c_i \varepsilon^i\Big)(e_j) = \sum_{i=1}^n c_i\, \delta^i_j = c_j ,
> $$
>
> for every $j$; so they are independent. Being independent and spanning, the $n$ covectors $\varepsilon^1, \ldots, \varepsilon^n$ form a basis of $V^{\ast}$, and $\dim V^{\ast} = n = \dim V$.

^pf-21-2

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[Linear map lemma|LADR 3.4]], [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]]

> [!remark]- Connections
> - Home: [[§12 Duality#^ladr-3-114|LADR 3.114 (dual basis gives coefficients)]], [[§12 Duality#^ladr-3-116|LADR 3.116 (dual basis is a basis of the dual space)]], [[§12 Duality#^ladr-3-111|LADR 3.111]].
> - Applied to $V = T_pM$ with the coordinate basis $e_j = \partial/\partial x^j|_p$: the dual basis is $\varepsilon^i = dx^i|_p$, the differentials of the coordinate functions. This identification is **not** a consequence of duality — the $dx^i|_p$ are defined independently, as differentials ([[§32 The Cotangent Space#^def-32-5|Def. §32.5]]), and the relation $dx^i|_p(\partial/\partial x^j|_p) = \delta^i_j$ is computed from $df_p(D) = D[f]$ and $x^i \circ \varphi^{-1} = r^i$ in Step 1 of [[§33 Covectors in Coordinates#^lem-33-1|Lemma §33.1]]. Everything after that is this proposition.
> - The second formula, $\lambda = \sum_i \lambda(e_i)\,\varepsilon^i$, with $\lambda = \xi \in T_p^{\ast}M$: a covector is the combination of the $dx^i|_p$ with its components $\xi_i = \xi(\partial/\partial x^i|_p)$ as coefficients, [[§33 Covectors in Coordinates#^def-33-1|Def. §33.1]] and [[§33 Covectors in Coordinates#^cor-33-2|Cor. §33.2]].
> - Those components are the fibre coordinates of the standard chart $(p, \xi) \mapsto (x^1(p), \ldots, x^m(p), \xi_1, \ldots, \xi_m)$ of $T^{\ast}M$, [[§49 The Cotangent Bundle#^def-49-5|Def. §49.5]]; the first formula, $v = \sum_i \varepsilon^i(v)\,e_i$, gives the fibre coordinates of $TM$ in the same way, [[§48 The Tangent Bundle#^def-48-5|Def. §48.5]].

> [!theorem] Proposition §21.3: The Double Dual
> For a finite-dimensional $V$, the map
>
> $$
> \iota : V \to V^{**}, \qquad \iota(v)(\lambda) = \lambda(v),
> $$
>
> is a linear isomorphism. It is **canonical**: its definition involves no choice of basis.
>
> *Lee: Proposition 11.8*

^prop-21-3

> [!proof]+ Proof
> To be shown: each $\iota(v)$ lies in $V^{\ast \ast }$, the map $\iota$ is linear, injective, and (by a dimension count) bijective. Canonicity is visible in the formula $\iota(v)(\lambda) = \lambda(v)$, which uses only $v$ and $\lambda$.
>
> *$\iota(v) \in V^{\ast \ast }$.* For $\lambda, \mu \in V^{\ast}$ and $c \in \mathbb{R}$, since the operations of $V^{\ast}$ are pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]),
>
> $$
> \iota(v)(\lambda + c\mu) = (\lambda + c\mu)(v) = \lambda(v) + c\,\mu(v) = \iota(v)(\lambda) + c\,\iota(v)(\mu) ,
> $$
>
> so $\iota(v) : V^{\ast} \to \mathbb{R}$ is linear.
>
> *$\iota$ is linear*, since each $\lambda$ is: for $v, w \in V$, $c \in \mathbb{R}$ and every $\lambda \in V^{\ast}$,
>
> $$
> \iota(v + cw)(\lambda) = \lambda(v + cw) = \lambda(v) + c\,\lambda(w) = \iota(v)(\lambda) + c\,\iota(w)(\lambda) = \big(\iota(v) + c\,\iota(w)\big)(\lambda) ,
> $$
>
> the last step by the pointwise operations of $V^{\ast \ast }$. As this holds for every $\lambda$, $\iota(v + cw) = \iota(v) + c\,\iota(w)$.
>
> *$\iota$ is injective.* It suffices that $\iota(v) \ne 0$ whenever $v \ne 0$ (then $\iota(v) = \iota(w)$ gives $\iota(v - w) = 0$, so $v = w$). If $v \ne 0$, the list $(v)$ is linearly independent, so it extends to a basis $(v, e_2, \ldots, e_n)$ of $V$; let $(\varepsilon^1, \ldots, \varepsilon^n)$ be the dual basis (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]), whose first covector satisfies $\varepsilon^1(v) = 1$ because $v$ is the first basis vector. Then
>
> $$
> \iota(v)(\varepsilon^1) = \varepsilon^1(v) = 1 \ne 0 ,
> $$
>
> so $\iota(v) \ne 0$.
>
> *$\iota$ is an isomorphism.* By Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]] applied to $V$, $\dim V^{\ast} = \dim V$, and applied again to the finite-dimensional space $V^{\ast}$, $\dim V^{\ast \ast } = \dim V^{\ast}$. So $\iota : V \to V^{\ast \ast }$ is an injective linear map between spaces of the same finite dimension, hence bijective by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1), i.e. a linear isomorphism.

^pf-21-3

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[Every linearly independent list extends to a basis|LADR 2.32]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]], [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]]

> [!remark]- Connections
> - In LADR the canonical $V \cong V''$ is mentioned in the remark after [[§12 Duality#^ladr-3-111|LADR 3.111]] (the non-canonical $V \cong V'$ goes through [[Dimension shows whether vector spaces are isomorphic|LADR 3.70]]).

> [!remark] Remark
> A finite-dimensional $V$ is also isomorphic to $V^{\ast}$, for instance by $e_i \mapsto \varepsilon^i$, but that isomorphism depends on the basis: change the basis and it changes. $V$ and $V^{\ast \ast}$ are identified *canonically*. This is why tangent vectors and covectors must be kept apart, as [[§32 The Cotangent Space#^def-32-4|Lecture 10]] did with $T_pM$ and $T_p^{\ast}M$, while the dual of $T_p^{\ast}M$ may be silently identified with $T_pM$.

^rem-21-1

> [!definition] Definition §21.3: Dual Map
> The **dual map**, or **transpose**, of a linear map $A : V \to W$ is
>
> $$
> A^* : W^* \to V^*, \qquad A^*(\lambda) = \lambda \circ A .
> $$
>
> *Lee: Proposition 11.4*

^def-21-3

![[m591-10-1.svg]]
*A linear map $A : V \to W$ carries vectors forward; its dual map $A^{\ast} : W^{\ast} \to V^{\ast}$ carries covectors backward.*

A covector on $W$ becomes a covector on $V$ by first applying $A$; so the dual map runs backwards. This is the linear-algebra shadow of the directions in [[§28 Derivations and the Abstract Tangent Space#Pushing Derivations Forward|§28, Pushing Derivations Forward]], where germs were pulled back and derivations pushed forward.

> [!theorem] Proposition §21.4: Properties of the Dual Map
> Let $A : V \to W$ and $B : W \to Z$ be linear.
> 1. $A^*$ is linear, $(\mathrm{id}_V)^* = \mathrm{id}_{V^*}$, and $(B \circ A)^* = A^* \circ B^*$. In particular, if $A$ is an isomorphism, so is $A^*$, with $(A^*)^{-1} = (A^{-1})^*$.
> 2. For finite-dimensional $V$ and $W$, the matrix of $A^*$ in the dual bases is the transpose of the matrix of $A$.
> 3. For finite-dimensional $V$ and $W$: $A$ is injective $\iff$ $A^*$ is surjective, and $A$ is surjective $\iff$ $A^*$ is injective.
>
> *Lee: Proposition 11.4*

^prop-21-4

> [!proof]+ Proof
> Throughout, two elements of a dual space are equal when they take the same value at every vector, and their operations are pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]).
>
> *(1)* *$A^{\ast}\lambda$ is a covector:* $\lambda \circ A$ is a composite of linear maps, hence linear. *$A^{\ast}$ is linear:* for $\lambda, \mu \in W^{\ast}$, $c \in \mathbb{R}$ and $v \in V$,
>
> $$
> A^{\ast}(\lambda + c\mu)(v) = (\lambda + c\mu)(Av) = \lambda(Av) + c\,\mu(Av) = (A^{\ast}\lambda)(v) + c\,(A^{\ast}\mu)(v) = \big(A^{\ast}\lambda + c\,A^{\ast}\mu\big)(v) ,
> $$
>
> so $A^{\ast}(\lambda + c\mu) = (\lambda + c\mu) \circ A = A^{\ast}\lambda + c\,A^{\ast}\mu$. *Identity:* $(\mathrm{id}_V)^{\ast}(\lambda) = \lambda \circ \mathrm{id}_V = \lambda$ for every $\lambda \in V^{\ast}$. *Composition:* for $\lambda \in Z^{\ast}$, by associativity of composition, $(B \circ A)^{\ast}(\lambda) = \lambda \circ B \circ A = (\lambda \circ B) \circ A = A^{\ast}(B^{\ast}\lambda)$. *Isomorphisms:* let $A$ have inverse $A^{-1} : W \to V$. Applying the composition rule to $A^{-1} \circ A = \mathrm{id}_V$ and to $A \circ A^{-1} = \mathrm{id}_W$, and then the identity rule,
>
> $$
> A^{\ast} \circ (A^{-1})^{\ast} = (A^{-1} \circ A)^{\ast} = (\mathrm{id}_V)^{\ast} = \mathrm{id}_{V^{\ast}}, \qquad (A^{-1})^{\ast} \circ A^{\ast} = (A \circ A^{-1})^{\ast} = (\mathrm{id}_W)^{\ast} = \mathrm{id}_{W^{\ast}} .
> $$
>
> So $(A^{-1})^{\ast} : V^{\ast} \to W^{\ast}$ is a two-sided inverse of $A^{\ast}$: $A^{\ast}$ is an isomorphism with $(A^{\ast})^{-1} = (A^{-1})^{\ast}$.
>
> *(2)* Let $(e_j)$ and $(f_i)$ be bases of $V$ and $W$, with dual bases $(\varepsilon^j)$ and $(\varphi^k)$, and $Ae_j = \sum_i a_{ij} f_i$, so that $[A] = (a_{ij})$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)). Then, by linearity of $\varphi^k$ and $\varphi^k(f_i) = \delta^k_i$,
>
> $$
> A^{\ast}(\varphi^k)(e_j) = \varphi^k(Ae_j) = \varphi^k\Big(\sum_i a_{ij} f_i\Big) = \sum_i a_{ij}\, \delta^k_i = a_{kj} .
> $$
>
> By the second formula of Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], applied to the covector $A^{\ast}(\varphi^k) \in V^{\ast}$, $A^{\ast}(\varphi^k) = \sum_j A^{\ast}(\varphi^k)(e_j)\,\varepsilon^j = \sum_j a_{kj}\,\varepsilon^j$. By Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3), the $k$-th column of the matrix of $A^{\ast}$ (in the bases $(\varphi^k)$ of $W^{\ast}$ and $(\varepsilon^j)$ of $V^{\ast}$) holds the coordinates of $A^{\ast}(\varphi^k)$, namely $a_{k1}, \ldots, a_{km}$. The $k$-th column of the matrix of $A^{\ast}$ is therefore the $k$-th row of $[A]$: the matrix of $A^{\ast}$ is $[A]^{\mathsf T}$.
>
> *(3)* By (2) and Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3), $\operatorname{rank} A^{\ast} = \operatorname{rank} [A]^{\mathsf T} = \operatorname{rank} [A] = \operatorname{rank} A$. Also $\dim W^{\ast} = \dim W$ and $\dim V^{\ast} = \dim V$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]). A linear map is surjective exactly when its rank, the dimension of its image, equals the dimension of its target (a subspace of full dimension is the whole space), and injective exactly when its kernel is $0$, which by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) means its rank equals the dimension of its source. Now $A$ is surjective iff $\operatorname{rank} A = \dim W$, iff $\operatorname{rank} A^{\ast} = \dim W^{\ast}$, which by rank–nullity for $A^{\ast} : W^{\ast} \to V^{\ast}$ means $A^{\ast}$ is injective. Likewise $A$ is injective iff $\operatorname{rank} A = \dim V = \dim V^{\ast}$, iff $\operatorname{rank} A^{\ast} = \dim V^{\ast}$, iff $A^{\ast}$ is surjective.

^pf-21-4

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-3|Def. §21.3]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§9 Matrices#^ladr-3-57|LADR 3.57]], [[Fundamental theorem of linear maps|LADR 3.21]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]]

> [!remark]- Connections
> - Home: [[§12 Duality#^ladr-3-118|LADR 3.118 (dual map)]], [[§12 Duality#^ladr-3-120|LADR 3.120 (algebraic properties)]], [[§12 Duality#^ladr-3-132|LADR 3.132 (matrix of the dual map is the transpose)]]; (3) is [[§12 Duality#^ladr-3-128|LADR 3.128]] and [[§12 Duality#^ladr-3-130|LADR 3.130]] (null space and range of the dual map).

> [!definition] Definition §21.4: Bilinear Pairing
> A **bilinear pairing** is a map $B : V \times W \to \mathbb{R}$ that is linear in each argument separately. It induces linear maps
>
> $$
> B^\flat : V \to W^*, \ \ v \mapsto B(v, \cdot\,), \qquad\qquad B^\sharp : W \to V^*, \ \ w \mapsto B(\cdot\,, w).
> $$

^def-21-4

> [!remark]- Connections
> - Same notion in LADR: [[§38 Tensor Products#^ladr-9-68|LADR 9.68]] (bilinear functionals on V × W); the case W = V is a bilinear form, [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-1|LADR 9.1]].

> [!definition] Definition §21.5: Non-Degenerate Pairing
> A bilinear pairing $B : V \times W \to \mathbb{R}$ ([[§21 Linear Algebra Toolkit#^def-21-4|Definition §21.4]]) is **left non-degenerate** if $B(v, w) = 0$ for all $w$ implies $v = 0$, i.e. $B^\flat$ is injective; **right non-degenerate** if $B(v, w) = 0$ for all $v$ implies $w = 0$, i.e. $B^\sharp$ is injective; and **non-degenerate** if both.

^def-21-5

> [!theorem] Theorem §21.5: Non-Degenerate Pairings
> Let $B : V \times W \to \mathbb{R}$ be a non-degenerate bilinear pairing, and suppose $V$ or $W$ is finite-dimensional. Then both are finite-dimensional, $\dim V = \dim W$, and
>
> $$
> B^\flat : V \xrightarrow{\ \cong\ } W^*, \qquad\qquad B^\sharp : W \xrightarrow{\ \cong\ } V^*
> $$
>
> are isomorphisms.
>
> *Lee: no counterpart*

^thm-21-5

> [!proof]+ Proof
> Suppose $V$ is finite-dimensional, of dimension $n$; the other case is symmetric, as explained at the end. By Definition [[§21 Linear Algebra Toolkit#^def-21-5|§21.5]], right non-degeneracy means $B^\sharp$ is injective and left non-degeneracy means $B^\flat$ is injective.
>
> *$W$ is finite-dimensional and $\dim W \le n$.* Right non-degeneracy makes $B^\sharp : W \to V^{\ast}$ injective, so $B^\sharp$ is a linear isomorphism of $W$ onto the subspace $B^\sharp(W)$ of $V^{\ast}$. The space $V^{\ast}$ has dimension $n$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), so its subspace $B^\sharp(W)$ is finite-dimensional of dimension $\le n$, and so is $W$, being isomorphic to it: $W$ is finite-dimensional with $\dim W \le n$.
>
> *$n \le \dim W$.* Now $W$ is finite-dimensional, so $\dim W^{\ast} = \dim W$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]). Left non-degeneracy makes $B^\flat : V \to W^{\ast}$ injective, so by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1) (an injective map has source dimension at most target dimension) $n = \dim V \le \dim W^{\ast} = \dim W$.
>
> *The isomorphisms.* Hence $\dim V = \dim W = n$, and also $\dim V^{\ast} = \dim W^{\ast} = n$. So $B^\flat : V \to W^{\ast}$ and $B^\sharp : W \to V^{\ast}$ are injective maps between spaces of equal finite dimension $n$, hence isomorphisms by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1).
>
> *The case $W$ finite-dimensional.* This is the case above after the renaming that swaps the two arguments: put $B'(w, v) = B(v, w)$, a bilinear pairing $W \times V \to \mathbb{R}$. Then $B'^\flat(w) = B'(w, \cdot\,) = B(\cdot\,, w) = B^\sharp(w)$ and $B'^\sharp(v) = B'(\cdot\,, v) = B(v, \cdot\,) = B^\flat(v)$, so $B'$ is non-degenerate because $B$ is, and the case already proved, applied to $B'$ with $W$ in the role of $V$, gives $\dim W = \dim V$ and that $B'^\flat = B^\sharp$ and $B'^\sharp = B^\flat$ are isomorphisms.

^pf-21-5

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-4|Def. §21.4]], [[§21 Linear Algebra Toolkit#^def-21-5|Def. §21.5]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark]- Connections
> - Applied to the pairing of tangent vectors with germs: [[§34 The Cotangent Space from Germs#^prop-34-3|§34.3]], [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]].
> - Bilinear forms on a single space in LADR: [[§35 Bilinear Forms and Quadratic Forms|9A Bilinear Forms and Quadratic Forms]].

> [!remark] Remark
> Each half of non-degeneracy gives one inequality of dimensions, and it is the *pair* of inequalities that forces the isomorphisms; neither half suffices alone. The finiteness hypothesis cannot be dropped: for an infinite-dimensional $V$, the evaluation pairing $V \times V^{\ast} \to \mathbb{R}$, $(v, \lambda) \mapsto \lambda(v)$, is non-degenerate, but its map $B^\flat = \iota : V \to V^{\ast \ast}$ is injective without being onto. [[§34 The Cotangent Space from Germs#^thm-34-4|Assignment 3, Problem 3]] is exactly a pairing $T_pM \times I_p/I_p^2 \to \mathbb{R}$ to which this theorem applies.

^rem-21-2

> [!definition] Definition §21.6: Quotient Vector Space
> Let $W \subseteq V$ be a linear subspace. The **quotient space** $V/W$ is the set of cosets $v + W = \{v + w \mid w \in W\}$, with
>
> $$
> (v + W) + (v' + W) = (v + v') + W, \qquad c\,(v + W) = cv + W,
> $$
>
> and the **projection** is $\pi : V \to V/W$, $\pi(v) = v + W$. Two vectors have the same coset iff their difference lies in $W$.
>
> *Lee: App. B, Vector Spaces*

^def-21-6

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99 (quotient space)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|LADR 3.102 (operations)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-104|LADR 3.104 (quotient map)]].

> [!theorem] Proposition §21.6: Quotient Spaces and Their Universal Property
> 1. The operations are well defined, $V/W$ is a vector space, and $\pi$ is linear and surjective with $\ker \pi = W$.
> 2. *Universal property.* If $A : V \to Z$ is linear with $W \subseteq \ker A$, there is a unique linear $\bar A : V/W \to Z$ with $\bar A \circ \pi = A$, namely $\bar A(v + W) = A(v)$.
> 3. If $V$ is finite-dimensional, $\dim V/W = \dim V - \dim W$.
>
> *Lee: App. B, Vector Spaces*

^prop-21-6

> [!proof]+ Proof
> Throughout, two vectors have the same coset iff their difference lies in $W$ (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]]), and $W$, being a subspace, is closed under addition and scalar multiplication.
>
> *(1)* *Well defined.* Suppose $v + W = v' + W$ and $u + W = u' + W$, i.e. $v - v' \in W$ and $u - u' \in W$. Then
>
> $$
> (v + u) - (v' + u') = (v - v') + (u - u') \in W, \qquad cv - cv' = c\,(v - v') \in W,
> $$
>
> so $(v + u) + W = (v' + u') + W$ and $cv + W = cv' + W$: the operations do not depend on representatives. *Vector space.* The vector space axioms are inherited from $V$: each axiom, written out with the defining formulas, becomes the same axiom in $V$ inside a coset; for instance $\big((v+W) + (u+W)\big) + (x+W) = \big((v+u)+x\big) + W = \big(v+(u+x)\big) + W = (v+W) + \big((u+W)+(x+W)\big)$. The zero is $0 + W = W$ and the negative of $v + W$ is $(-v) + W$. *$\pi$ is linear* by the definition of the operations: $\pi(v + cu) = (v + cu) + W = (v + W) + c\,(u + W) = \pi(v) + c\,\pi(u)$. It is *surjective* by construction, every coset $v + W$ being $\pi(v)$. *Kernel:* $\pi(v) = 0 + W$ iff $v - 0 \in W$, i.e. iff $v \in W$; so $\ker \pi = W$.
>
> *(2)* *Well defined.* If $v + W = v' + W$, then $v - v' \in W \subseteq \ker A$, so $A(v) - A(v') = A(v - v') = 0$: the value $A(v)$ does not depend on the representative. *Linear*, because $A$ is: $\bar A\big((v + W) + c\,(u + W)\big) = \bar A\big((v + cu) + W\big) = A(v + cu) = A(v) + c\,A(u) = \bar A(v + W) + c\,\bar A(u + W)$. *$\bar A \circ \pi = A$:* $\bar A(\pi(v)) = \bar A(v + W) = A(v)$. *Unique*, because $\pi$ is surjective: if $\bar A'$ is linear with $\bar A' \circ \pi = A$, then every element of $V/W$ is $\pi(v)$ for some $v$, and $\bar A'(\pi(v)) = A(v) = \bar A(\pi(v))$, so $\bar A' = \bar A$.
>
> *(3)* Rank–nullity for $\pi$. The space $V/W$ is finite-dimensional, spanned by the images $\pi(e_i)$ of a basis $(e_i)$ of $V$ since $\pi$ is linear and surjective. By Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1) for $\pi : V \to V/W$, with $\ker \pi = W$ and $\operatorname{rank} \pi = \dim V/W$ (surjectivity) from (1),
>
> $$
> \dim V = \dim \ker \pi + \operatorname{rank} \pi = \dim W + \dim V/W .
> $$

^pf-21-6

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-6|Def. §21.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[Fundamental theorem of linear maps|LADR 3.21]]

![[m591-10-2.svg]]
*The universal property of the quotient: a linear map $A$ with $W \subseteq \ker A$ factors uniquely as $A = \bar A \circ \pi$.*

The universal property as a triangle: a linear map that kills $W$ descends to $V/W$. It is the linear counterpart of the universal property of quotient maps, Theorem [[§5 Quotient Maps#^thm-5-1|§5.1]], with “vanishes on $W$” in place of “constant on the fibres” — and the proof is the same: define the map on a class by choosing a representative, and check the choice does not matter. [[§34 The Cotangent Space from Germs#^prop-34-3|Assignment 3, Problem 3(a)]] is an instance: a derivation kills $I_p^2$, so its restriction to $I_p$ descends to $I_p/I_p^2$.

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103 (quotient space is a vector space)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105 (dimension)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-106|LADR 3.106]] and [[First isomorphism theorem|LADR 3.107 (first isomorphism theorem)]] for the induced map.
> - Topological counterpart: [[Universal Property of Quotient Maps|590 §12 (universal property of quotient maps)]]; applied in [[§34 The Cotangent Space from Germs#^def-34-1|Def. §34.1]].

> [!definition] Definition §21.7: Direct Sum
> The **direct sum** of vector spaces $V$ and $W$ is $V \oplus W = V \times W$ with the componentwise operations $(v, w) + (v', w') = (v + v', w + w')$ and $c(v, w) = (cv, cw)$. It comes with the **inclusions** $\iota_V(v) = (v, 0)$, $\iota_W(w) = (0, w)$ and the **projections** $\pi_V(v, w) = v$, $\pi_W(v, w) = w$, all linear.

^def-21-7

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|LADR 3.87 (product of vector spaces)]].

> [!definition] Definition §21.8: Internal Direct Sum
> A vector space $U$ is the **internal direct sum** of subspaces $U_1, U_2$, written $U = U_1 \oplus U_2$, if every $u \in U$ is $u_1 + u_2$ for unique $u_1 \in U_1$, $u_2 \in U_2$.

^def-21-8

> [!remark]- Connections
> - Home: [[§3 Subspaces#^ladr-1-41|LADR 1.41 (internal direct sum)]].

> [!theorem] Proposition §21.7: Direct Sums
> 1. $\pi_V \iota_V = \mathrm{id}_V$, $\pi_W \iota_W = \mathrm{id}_W$, $\pi_W \iota_V = 0$ and $\pi_V \iota_W = 0$. So $\iota_V$, $\iota_W$ are injective, and $V \oplus W$ is the internal direct sum of $V \oplus \{0\} = \iota_V(V)$ and $\{0\} \oplus W = \iota_W(W)$.
> 2. If $(e_i)$ and $(f_j)$ are bases of $V$ and $W$, then the vectors $(e_i, 0)$ and $(0, f_j)$ together form a basis of $V \oplus W$. In particular $\dim (V \oplus W) = \dim V + \dim W$.
>
> *Lee: App. B, Vector Spaces*

^prop-21-7

> [!proof]+ Proof
> *(1)* Direct from the formulas of Definition [[§21 Linear Algebra Toolkit#^def-21-7|§21.7]]: for $v \in V$ and $w \in W$,
>
> $$
> \pi_V \iota_V(v) = \pi_V(v, 0) = v, \quad \pi_W \iota_W(w) = \pi_W(0, w) = w, \quad \pi_W \iota_V(v) = \pi_W(v, 0) = 0, \quad \pi_V \iota_W(w) = \pi_V(0, w) = 0 .
> $$
>
> *Injectivity.* If $\iota_V(v) = \iota_V(v')$, apply $\pi_V$: $v = \pi_V\iota_V(v) = \pi_V\iota_V(v') = v'$. Likewise $\iota_W$ is injective, using $\pi_W$ as a left inverse. *Internal direct sum* (Definition [[§21 Linear Algebra Toolkit#^def-21-8|§21.8]]). Existence: by componentwise addition each $(v, w)$ is $(v, 0) + (0, w) = \iota_V(v) + \iota_W(w)$. Uniqueness: suppose $(v, w) = \iota_V(v') + \iota_W(w')$ for some $v' \in V$, $w' \in W$. Applying the linear maps $\pi_V$ and $\pi_W$ and the four identities above,
>
> $$
> v = \pi_V(v, w) = \pi_V\iota_V(v') + \pi_V\iota_W(w') = v' + 0, \qquad w = \pi_W(v, w) = \pi_W\iota_V(v') + \pi_W\iota_W(w') = 0 + w' ,
> $$
>
> so $v = \pi_V(v, w)$ and $w = \pi_W(v, w)$ are forced, and the summands $\iota_V(v)$, $\iota_W(w)$ are unique.
>
> *(2)* Let $(e_1, \ldots, e_m)$ and $(f_1, \ldots, f_n)$ be the bases. *Spanning.* Given $(v, w)$, write $v = \sum_i v^i e_i$ and $w = \sum_j w^j f_j$ with the coordinates $v^i$, $w^j$ of $v$ and $w$. By the componentwise operations,
>
> $$
> \sum_{i=1}^m v^i (e_i, 0) + \sum_{j=1}^n w^j (0, f_j) = \Big(\sum_{i=1}^m v^i e_i,\ 0\Big) + \Big(0,\ \sum_{j=1}^n w^j f_j\Big) = (v, w) .
> $$
>
> *Independence.* If $\sum_i a^i (e_i, 0) + \sum_j b^j (0, f_j) = (0, 0)$, the same computation gives $\big(\sum_i a^i e_i,\ \sum_j b^j f_j\big) = (0, 0)$, so $\sum_i a^i e_i = 0$ in $V$ and $\sum_j b^j f_j = 0$ in $W$; by the independence of the two bases all $a^i$ and all $b^j$ vanish. So the $m + n$ vectors form a basis, and $\dim(V \oplus W) = m + n = \dim V + \dim W$.

^pf-21-7

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-7|Def. §21.7]], [[§21 Linear Algebra Toolkit#^def-21-8|Def. §21.8]]

> [!remark]- Connections
> - Home: [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|LADR 3.92 (dimension of a product)]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-93|LADR 3.93 (products and direct sums)]], [[Condition for a direct sum|LADR 1.45]].
> - Used for the tangent space of a product: [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]].

> [!remark] Remark: Direct Sum and Product
> For two summands, or finitely many, the direct sum *is* the Cartesian product with componentwise operations — the point Uribe said in Lecture 11 he had forgotten the reason for. The two notions differ only for infinitely many summands: the product $\prod_\alpha V_\alpha$ contains all families $(v_\alpha)$, while the direct sum $\bigoplus_\alpha V_\alpha$ contains only those with finitely many nonzero entries.

^rem-21-3
