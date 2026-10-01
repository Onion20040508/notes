---
type: section
subject: "[[Group Theory]]"
chapter: 1
section: 3
tags: [group-theory, math493]
---
← [[§2 First Consequences of the Axioms]] · ↑ [[· 1 Groups and Subgroups]] · [[§4 Subgroups]] →

*Reference: Pinter Ch. 3 (examples of groups), Ch. 7 (groups of permutations), Ch. 4, Ex. G (direct products).*

In each example, associativity is inherited from a known associative operation (arithmetic, function composition); the nontrivial points are *well-definedness* (for $\mathbb{Z}/n\mathbb{Z}$ ([[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]) and $U_n$ ([[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]])) and *closure* (for $U_n$, $S_X$, $GL_n$).

> [!definition] Definition §3.1: The Additive Groups $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$
> Each of $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ is a group under addition: the operation is $(a, b) \mapsto a + b$ (which lands in the same set, so closure holds); the identity is $0$; the inverse of $a$ is $-a$. Associativity is a basic property of arithmetic. All three are abelian. *(Note: none of them is a group under multiplication — $0$ has no inverse, and in $\mathbb{Z}$ even $2$ has no inverse.)*

^def-3-1

> [!definition] Definition §3.2: Direct Products
> Let $G$ and $H$ be groups. The **direct product** $G \times H$ is the set of pairs $\{(g, h) : g \in G, h \in H\}$ with componentwise operation
>
> $$ (g_1, h_1) * (g_2, h_2) = (g_1 g_2, h_1 h_2). $$
>
> This is a group: identity $(e_G, e_H)$, inverse $(g, h)^{-1} = (g^{-1}, h^{-1})$, and each axiom holds componentwise because it holds in $G$ and in $H$. Iterating gives $G_1 \times \cdots \times G_n$; in particular $\mathbb{Z}^n$, $\mathbb{Q}^n$, $\mathbb{R}^n$ (componentwise addition, identity $(0, \ldots, 0)$) and mixed products like $\mathbb{Z} \times \mathbb{R}$.

^def-3-2

> [!remark]- Connections
> - MATH 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^def-21-5|Direct Product of Groups]]; the vector-space version: [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|Product of vector spaces]].
> - Characterized by its universal property in [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|The Product and Its Universal Property]].

> [!definition] Definition §3.3: Field (provisional definition)
> A **field** is a set $k$ with two operations $+$ and $\cdot$ such that:
> 1. $(k, +)$ is an abelian group, with identity written $0$;
> 2. $(k \setminus \{0\}, \cdot)$ is an abelian group, with identity written $1$;
> 3. multiplication distributes over addition: $a(b + c) = ab + ac$ for all $a, b, c \in k$.
>
> Examples: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$; also $\mathbb{Z}/p\mathbb{Z}$ for $p$ prime (see [[§8 Invertibility and Unit Groups#^prop-8-4|the unit-group discussion below]]). Non-examples: $\mathbb{Z}$ (no multiplicative inverses). Fields will be treated properly later in the course; this definition suffices for now.

^def-3-3

> [!remark]- Connections
> - The example ℚ is constructed in 250 and checked to be a field: [[§22 Partitions and Equivalence Relations#^thm-22-9|250 Thm. §22.9]].
> - The field axioms listed one by one: [[§3 The Set ℝ of Real Numbers#^def-3-1|451 Def. §3.1]].

> [!definition] Definition §3.4: Multiplicative Group of a Field: $k^\times$
> For a field $k$, set $k^\times = (k \setminus \{0\}, \cdot)$; this is a group directly by condition (2) of the [[§3 Basic Examples of Groups#^def-3-3|field definition]], e.g. $\mathbb{Q}^\times$, $\mathbb{R}^\times$, $\mathbb{C}^\times$.

^def-3-4

> [!theorem] Proposition §3.1: No Zero Divisors in a Field
> Let $k$ be a field. Then $a \cdot 0 = 0$ for every $a \in k$, and if $ab = 0$ then $a = 0$ or $b = 0$. In particular the product of two nonzero elements is nonzero.

^prop-3-1

> [!proof]+ Proof
> $a \cdot 0 = a(0 + 0) = a \cdot 0 + a \cdot 0$, and cancelling $a \cdot 0$ in the group $(k, +)$ gives $a \cdot 0 = 0$. If $ab = 0$ and $a \neq 0$, then $b = 1 \cdot b = (a^{-1}a)b = a^{-1}(ab) = a^{-1} \cdot 0 = 0$.

^pf-3-1

*Uses:* [[§3 Basic Examples of Groups#^def-3-3|Def. §3.3]], [[§2 First Consequences of the Axioms#^prop-2-1|§2.1]]

> [!remark] Remark: Consistency of the Field Axioms
> With the [[§3 Basic Examples of Groups#^def-3-3|definition of a field]] above, closure of $k \setminus \{0\}$ under multiplication is built into condition (2) ($\cdot$ is a binary operation *on* $k \setminus \{0\}$); [[§3 Basic Examples of Groups#^prop-3-1|the proposition]] shows this is consistent with the remaining axioms rather than an extra assumption in disguise.

^rem-3-1

> [!definition] Definition §3.5: Symmetric Groups $S_X$ and $S_n$
> For any set $X$, let $S_X$ be the set of bijections $\sigma: X \to X$, with operation composition: $(\sigma \tau)(x) = \sigma(\tau(x))$ (**convention:** apply the right factor first). Then $S_X$ is a group with identity $\operatorname{id}_X$ and inverse the inverse function $\sigma^{-1}$. If $X = \{1, 2, \ldots, n\}$, we call this group the **symmetric group** and denote it $S_n$; it has $n!$ elements and is non-abelian for $n \geq 3$.

^def-3-5

> [!proof]+ Verification
> **Closure:** A composition of bijections is a bijection: if $\sigma, \tau$ have inverse functions $\sigma^{-1}, \tau^{-1}$, then $\tau^{-1} \sigma^{-1}$ is a two-sided inverse of $\sigma\tau$ (note the socks–shoes reversal, exactly [[§2 First Consequences of the Axioms#^prop-2-4|WS 1.4]]), and a function with a two-sided inverse is a bijection.
>
> **Associativity:** Function composition is associative: for every $x$,
>
> $$ ((\sigma\tau)\rho)(x) = (\sigma\tau)(\rho(x)) = \sigma(\tau(\rho(x))) = \sigma((\tau\rho)(x)) = (\sigma(\tau\rho))(x). $$
>
> **Identity and inverses:** $\operatorname{id}_X \circ \sigma = \sigma \circ \operatorname{id}_X = \sigma$, and the inverse *function* $\sigma^{-1}$ (which exists precisely because $\sigma$ is a bijection) satisfies $\sigma \sigma^{-1} = \sigma^{-1} \sigma = \operatorname{id}_X$.
>
> **Non-abelian for $n \geq 3$:** With $g_1 = (1\,2)$, $g_2 = (2\,3)$: $g_1 g_2$ sends $1 \to 2$, while $g_2 g_1$ sends $1 \to 3$ (see [[§10 Cycle Notation and the Group S₃#^ex-10-1|The Group S₃ in Detail, §10.1]]).
>
> **Order:** A bijection of $\{1, \ldots, n\}$ is determined by choosing $\sigma(1)$ ($n$ ways), then $\sigma(2)$ ($n - 1$ remaining values), etc., giving $n!$.

^pf-def-3-5

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|590 §21.4]], [[§10 Cycle Notation and the Group S₃#^ex-10-1|Ex. §10.1]]

> [!remark]- Connections
> - Elementary versions: [[§12★ Counting Functions and Subsets#^def-12-3|250 Def. §12.3]] (permutation), [[§12★ Counting Functions and Subsets#^cor-12-3|250 Cor. §12.3]] (there are $n!$ of them), [[§9 Injections, Surjections and Bijections#^ex-9-9|250 Ex. §9.9]] (inverse of a composite, the closure step).

> [!definition] Definition §3.6: General Linear Groups $GL_n(k)$
> For a field $k$ and integer $n \geq 1$, let
>
> $$ GL_n(k) = \{ A \in \operatorname{Mat}_{n \times n}(k) : A \text{ is invertible} \}, $$
>
> with operation matrix multiplication. Then $GL_n(k)$ is a group with identity the identity matrix $I_n$ and inverse the matrix inverse $A^{-1}$, called the **general linear group**. It is non-abelian for $n \geq 2$.

^def-3-6

> [!proof]+ Verification
> **Closure:** If $A, B$ are invertible, then $B^{-1}A^{-1}$ is a two-sided inverse of $AB$ ([[§2 First Consequences of the Axioms#^prop-2-4|WS 1.4]] again: $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = I_n$ and symmetrically), so $AB \in GL_n(k)$. *(Equivalently, once determinants are available: $A$ is invertible iff $\det A \neq 0$ ([[§34 Determinants#^ladr-9-50|LADR 9.50]]), and $\det(AB) = \det A \det B \neq 0$ ([[§34 Determinants#^ladr-9-49|LADR 9.49]]).)*
>
> **Associativity:** Matrix multiplication is associative — either by direct computation with the entry formula $\left( (AB)C \right)_{il} = \sum_{j,\,m} A_{ij} B_{jm} C_{ml} = \left( A(BC) \right)_{il}$ (both orders of summation give the same double sum), or conceptually: matrices represent linear maps $k^n \to k^n$, matrix multiplication represents composition ([[§9 Matrices#^ladr-3-43|LADR 3.43]]), and composition of functions is associative (as verified for $S_X$, [[§3 Basic Examples of Groups#^pf-def-3-5|Def. §3.5]]).
>
> **Identity and inverses:** $I_n A = A I_n = A$, and $A^{-1} \in GL_n(k)$ since $A^{-1}$ has the two-sided inverse $A$.
>
> **Non-abelian for $n \geq 2$:**
> $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ but
> $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$
> (in any field where $2 \neq 0$ these differ in the $(1,1)$ entry; over $\mathbb{F}_2$ they still differ in the off-diagonal entries).

^pf-def-3-6

*Uses:* [[§2 First Consequences of the Axioms#^prop-2-4|§2.4]], [[§3 Basic Examples of Groups#^def-3-5|Def. §3.5]], [[§34 Determinants#^ladr-9-50|LADR 9.50]], [[§34 Determinants#^ladr-9-49|LADR 9.49]], [[§9 Matrices#^ladr-3-43|LADR 3.43]]

![[m493-3-1.svg]]
*The two shears of the verification above, $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, applied to the unit square (dashed): $AB$ carries it to the parallelogram spanned by its columns $(2,1)$ and $(1,1)$ (blue), $BA$ to the one spanned by $(1,1)$ and $(1,2)$ (red). Different images, so $AB \neq BA$ and $GL_2$ is non-abelian.*

> [!remark]- Connections
> - Invertible matrices in LADR: [[§10 Invertibility and Isomorphisms#^ladr-3-80|Invertible, inverse, A⁻¹]]; associativity of composing linear maps: [[§7 Vector Space of Linear Maps#^ladr-3-8|Algebraic properties of products of linear maps]].
> - $S_n$ sits inside $GL_n(k)$ via permutation matrices: [[§19 Polynomial Rings, Permutation Matrices, and Representations#^prop-19-5|§19.5]].
> - As a topological group: [[§5 Topological Groups and Classical Matrix Groups#^def-5-4|591 Def. §5.4]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-4|591 Prop. §5.4]]; over ℝ it has exactly two components, separated by the sign of det, [[§5 Topological Groups and Classical Matrix Groups#^thm-5-6|591 Thm. §5.6]].
> - Computational version: invertible matrices and their inverses by row reduction, [[§12 The Inverse of a Matrix#^def-12-1|235 Def. §12.1]]; the determinant facts used, [[§21 Properties of Determinants#^thm-21-3|235 Thm. §21.3]] (invertible iff det ≠ 0) and [[§21 Properties of Determinants#^thm-21-9|235 Thm. §21.9]] (det is multiplicative).

> [!definition] Definition §3.7: Special Linear, Orthogonal, and Special Orthogonal Groups
> For a field $k$ and $n \geq 1$:
> - the **special linear group** is $SL_n(k) = \{A \in GL_n(k) : \det A = 1\}$;
> - the **orthogonal group** is $O(n) = O_n(\mathbb{R}) = \{A \in GL_n(\mathbb{R}) : A^{\mathsf{T}}A = I_n\}$;
> - the **special orthogonal group** is $SO(n) = O(n) \cap SL_n(\mathbb{R})$.
>
> Each is a subgroup of the corresponding general linear group (verified in [[§5 A Zoo of Subgroups#^ex-5-4|Ex. §5.4]], where $SO(2)$ is identified with the rotations of the plane).

^def-3-7

> [!remark]- Connections
> - Real orthogonal matrices are the real unitary matrices: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|Characterizations of unitary matrices]] (condition $Q^*Q = QQ^* = I$); rotations: [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-52|Rotation of R²]].
> - The same groups as topological groups and manifolds in 591: [[§5 Topological Groups and Classical Matrix Groups#^def-5-5|591 Def. §5.5]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-6|591 Def. §5.6]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-7|591 Def. §5.7]], and [[Classical Groups Are Manifolds]] (591 Thm. §5.8; workhorse example [[Classical groups O(n), U(n), SL(n,ℝ)]]).
> - Used in Relativity: the Lorentz group is defined as $O(n)$ is, with the metric $\eta$ in place of the identity — [[§B1.2 Lorentz Transformations and the Lorentz Group#^def-b1-2-1|REL Def. §B1.2.1]]; the rotations sit inside it, with $R^{\mathsf T}R = 1$ — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-5|REL Theorem §B1.2.5]].
> - Computational version: [[§41 Orthogonal Sets#^def-41-5|235 Def. §41.5]] and [[§41 Orthogonal Sets#^prop-41-6|235 Prop. §41.6]] (orthogonal matrices have orthonormal columns and rows and det ±1, with worked examples).

> [!example] Example §3.1: Groups and Non-Groups
> Deciding whether $(G, \cdot)$ is a group usually comes down to identity and inverses; associativity is inherited from arithmetic or composition.
>
> | | | |
> |---|---|---|
> | $(\mathbb{N}, +)$: no (no inverses) | $(\mathbb{N}, \times)$: no | $(\mathbb{Z}, +)$: yes |
> | $(\mathbb{Z}, \times)$: no ($2$ has no inverse) | $(\mathbb{R}_{\geq 0}, +)$: no | $(\mathbb{R}, +)$: yes |
> | $(\mathbb{R}_{\geq 0}, \times)$: no ($0$) | $(\mathbb{R}, \times)$: no ($0$) | $(\mathbb{R}\setminus\{0\}, \times)$: yes |
> | $(\mathbb{Z}/n\mathbb{Z}, +)$: yes | $(\mathbb{Z}/n\mathbb{Z}, \times)$: no ($[0]$) | $(\mathbb{Z}/n\mathbb{Z} \setminus \{[0]\}, \times)$: iff $n$ prime |
> | $(GL_n(\mathbb{R}), \times)$: yes | $(SL_n(\mathbb{R}), \times)$: yes | $(\mathbb{R}_{>0}, \times)$: yes |
>
> *Source: cf. MATH 412*

^ex-3-1

> [!remark] Remark: $S_n$ and $GL_n(k)$
> $S_n$ and $GL_n(k)$ are the two fundamental families of non-abelian groups. $S_n$ acts by permuting a finite set; $GL_n(k)$ acts linearly on a vector space. [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-6|Representation theory]] (second half of the course) is precisely the study of homomorphisms $G \to GL_n(k)$, i.e. of realizing abstract groups inside the second family.

^rem-3-2
