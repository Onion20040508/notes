---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 11
tags: [differentiable-manifolds, math591]
---
← [[§10 The Line with Two Origins]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§12 The Classical Groups Are Topological Manifolds]] →

*Thread: equations — Topological groups and the classical matrix groups. That the classical groups are manifolds, as level sets of polynomial maps ([[§7 The Regular Value Theorem|§7]]), is [[§12 The Classical Groups Are Topological Manifolds|§12]]; acting on spaces, they then feed the quotient thread.*

*Reference: Lee Ch. 7 (“Lie Groups”). For the calculus: MATH 452 notes ([[§15 The Implicit Function Theorem|Implicit Function Theorem]]).*

> [!remark] Remark: Why This Section
> Topological groups are the precursor of *Lie groups*, one of the main topics later in the course; and the classical matrix groups introduced here “are going to be our friends for the semester, and hopefully for later on in life.” Besides being examples of manifolds in their own right ([[§12 The Classical Groups Are Topological Manifolds|§12, The Classical Groups Are Topological Manifolds]]), they are the groups whose *actions* produce the quotient manifolds of [[§13 Group Actions and Orbit Spaces|§13]]–[[§14 Homogeneous Spaces|§14]]: spheres, projective spaces, Grassmannians.

^rem-11-1

## Topological Groups

> [!definition] Definition §11.1: Topological Group
> A **topological group** is a group $G$ equipped with a topology such that the two structures are compatible, meaning that both maps
> 1. $G \times G \to G$, $(g, h) \mapsto gh$   (multiplication), and
> 2. $G \to G$, $g \mapsto g^{-1}$   (inversion)
>
> are continuous, where $G \times G$ carries the product topology.
>
> *Lee: Ch. 7, p. 151 (defined in passing)*

^def-11-1

> [!remark]- Connections
> - The two ingredients: groups, [[§1 The Definition of a Group#^def-1-1|493 Def. §1.1]]; the product topology, [[§4 Product Topology#^def-4-1|590 Def. §4.1]] (591: [[§3 Subspaces and Products#^def-3-3|Def. §3.3]]).

> [!example] Example §11.1: Discrete Groups
> Any group $G$ with the discrete topology is a topological group: every subset is open, so every map out of $G$ or $G \times G$ (which is also discrete) is continuous. Uribe: mathematically immediate, but it “actually shows up in useful ways.”

^ex-11-1

> [!remark]- Connections
> - The discrete topology in 590: [[Discrete and indiscrete topologies]]; the product of discrete spaces is discrete, [[§4 Product Topology#^ex-4-2|590 Ex. §4.2]].

> [!theorem] Proposition §11.1: Subgroups Are Topological Groups
> If $G$ is a topological group and $H \le G$ is a subgroup, then $H$ with the subspace topology is a topological group.
>
> *Lee: cf. Ch. 7, Lie Subgroups*

^prop-11-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* The multiplication of $H$ is the composite $H \times H \hookrightarrow G \times G \to G$, where the first map is $\iota \times \iota$ (continuous by [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10]], since each component is $\iota \circ \pi$) and the second is the multiplication of $G$. This composite is continuous and takes values in $H$, so it is continuous as a map into $H$ by [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]]. Inversion on $H$ is the restriction of inversion on $G$, and the same argument applies.

^pf-11-1

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Def. §11.1]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§3 Subspaces and Products#^prop-3-3|§3.3]], [[§4 Subgroups#^def-4-1|493 Def. §4.1]], [[§10 Continuous Functions#^thm-10-4|590 §10.4]]

## Classical Matrix Groups

> [!definition] Definition §11.2: Matrices as a Euclidean Space
> Let $\operatorname{Mat}(n, \mathbb{R})$ be the set of all $n \times n$ real matrices, a real vector space under entrywise addition and scalar multiplication. For $1 \le i, j \le n$ let $E_{ij} \in \operatorname{Mat}(n,\mathbb{R})$ be the matrix with a $1$ in position $(i,j)$ and $0$ elsewhere. Every $g$ can be written uniquely as $g = \sum_{i,j} g_{ij} E_{ij}$, so $\{E_{ij}\}$ is a basis and $\dim \operatorname{Mat}(n,\mathbb{R}) = n^2$. Fix the coordinate map
>
> $$
> \operatorname{Mat}(n,\mathbb{R}) \longrightarrow \mathbb{R}^{n^2}, \qquad g \longmapsto (g_{11}, g_{12}, \ldots, g_{1n},\ g_{21}, \ldots, g_{2n},\ \ldots,\ g_{n1}, \ldots, g_{nn}),
> $$
>
> which reads the entries row by row (entry $(i,j)$ goes to coordinate number $n(i-1) + j$). This is a linear isomorphism, and we **define** the topology on $\operatorname{Mat}(n,\mathbb{R})$ by declaring it a homeomorphism onto $\mathbb{R}^{n^2}$ with the usual topology. Every subset of $\operatorname{Mat}(n,\mathbb{R})$ then carries the subspace topology. Concretely, a sequence of matrices converges iff each of its $n^2$ entries converges, and the Euclidean norm on $\mathbb{R}^{n^2}$ pulls back to $\|g\| = \big(\sum_{i,j} g_{ij}^2\big)^{1/2}$.
>
> *Lee: Example 1.25*

^def-11-2

> [!remark]- Connections
> - $\dim \mathbb{F}^{m,n} = mn$: [[§9 Matrices#^ladr-3-40|LADR 3.40]].
> - The coordinate-free version (any finite-dimensional vector space is a smooth manifold): [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]].

> [!definition] Definition §11.3: The Symmetric Group
> The **symmetric group** $S_n$ is the set of all bijections $\sigma : \{1, \ldots, n\} \to \{1, \ldots, n\}$, a group under composition, of order $n!$. A **transposition** is a permutation that swaps two symbols and fixes the rest.
>
> *Lee: App. B, The Determinant*

^def-11-3

> [!remark]- Connections
> - Home in 493: [[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]].

> [!definition] Definition §11.4: The Sign of a Permutation
> An **inversion** of $\sigma \in S_n$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-3|Definition §11.3]]) is a pair $i < j$ with $\sigma(i) > \sigma(j)$. The **sign** of $\sigma$ is
>
> $$
> \operatorname{sgn}(\sigma) = (-1)^{\#\{\text{inversions of } \sigma\}} \in \{\pm 1\}.
> $$
>
> *Lee: App. B, The Determinant*

^def-11-4

> [!remark]- Connections
> - Home in 493: inversions [[§21 The Sign Homomorphism and the Alternating Group#^def-21-1|493 Def. §21.1]], the sign [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|493 Def. §21.2]] (hub: [[The Sign Homomorphism]]).
> - In linear algebra: [[§36 Alternating Multilinear Forms#^ladr-9-32|LADR 9.32]].

> [!theorem] Proposition §11.2: Properties of the Sign
> 1. $\operatorname{sgn} : S_n \to \{\pm 1\}$ is a group homomorphism: $\operatorname{sgn}(\sigma\tau) = \operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$.
> 2. Every transposition has sign $-1$, and $\operatorname{sgn}(\mathrm{id}) = 1$.
> 3. Every $\sigma \in S_n$ is a product of transpositions; the number of factors is not unique, but its parity is, and $\operatorname{sgn}(\sigma) = (-1)^k$ for any factorization of $\sigma$ into $k$ transpositions.
> 4. If $\sigma$ fixes $n - 1$ of the $n$ symbols, then $\sigma = \mathrm{id}$.
>
> *Lee: App. B, The Determinant*

^prop-11-2

> [!proof]+ Proof
> (4) is elementary: if $\sigma(i) = i$ for all $i \neq j$, then $\sigma(j)$ must be the one remaining value $j$, since $\sigma$ is injective. (1)–(3) are proved in MATH 493 (Dummit–Foote §3.5); the standard route is to let $\sigma$ act on the polynomial $\Delta = \prod_{i<j}(x_i - x_j)$ by permuting variables, observe that $\sigma \cdot \Delta = \operatorname{sgn}(\sigma)\,\Delta$ with $\operatorname{sgn}$ as in [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Definition §11.4]], and read off (1) from the fact that this is a group action; (2) is a direct count; (3) follows from (1) and (2) once one knows transpositions generate $S_n$.

^pf-11-2

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Def. §11.4]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|493 §21.2]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|493 §21.3]], [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|493 §21.4]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|493 §21.7]]

> [!remark]- Connections
> - Home in 493: [[The Sign Homomorphism]] ([[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|493 §21.3]]); parity of factorizations, [[§21 The Sign Homomorphism and the Alternating Group#^cor-21-4|493 §21.4]]; transpositions generate $S_n$, [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-7|493 §21.7]].

> [!example] Example §11.2: Small Cases: Two and Three
> $S_2 = \{\mathrm{id}, (1\,2)\}$ with signs $+1, -1$, and the Leibniz formula below ([[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]]) reads $\det = x_{11}x_{22} - x_{12}x_{21}$. $S_3$ has six elements: the identity and the two $3$-cycles $(1\,2\,3)$, $(1\,3\,2)$ have sign $+1$ (each $3$-cycle is a product of two transpositions, e.g. $(1\,2\,3) = (1\,3)(1\,2)$), and the three transpositions $(1\,2)$, $(1\,3)$, $(2\,3)$ have sign $-1$; this is the six-term formula for a $3 \times 3$ determinant, with three plus and three minus signs.

^ex-11-2

> [!remark]- Connections
> - [[The symmetric group S₃]] in 493; the explicit $2 \times 2$ and $3 \times 3$ formulas in LADR: [[§37 Determinants#^ladr-9-47|LADR 9.47]].

> [!remark] Remark
> The facts used in the determinant computation of [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|Proposition §12.1]] are exactly (2) and (4) above: the identity permutation contributes with sign $+1$ (which is why the answer is $+\operatorname{tr} V$), and a permutation fixing all but one symbol is the identity (which is why only that one term survives).

^rem-11-2

> [!theorem] Proposition §11.3: Determinant Is Continuous
> $\det : \operatorname{Mat}(n,\mathbb{R}) \to \mathbb{R}$ is continuous.
>
> *Lee: App. B, The Determinant*

^prop-11-3

> [!proof]+ Proof
> *(Implicit in Lecture 3, which used that $\mathrm{GL}(n,\mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ is open; filled in.)* By the Leibniz formula $\det(x) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n x_{i,\sigma(i)}$ (with $S_n$ and $\operatorname{sgn}$ as in Definitions [[§11 Topological Groups and Classical Matrix Groups#^def-11-3|§11.3]] and [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]; each $\sigma$ selects one entry from every row, $x_{i,\sigma(i)}$ from row $i$, and bijectivity of $\sigma$ means every column is used exactly once), $\det$ is a polynomial in the $n^2$ coordinates, and polynomials are continuous.

^pf-11-3

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Def. §11.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Def. §11.4]], [[§37 Determinants#^ladr-9-46|LADR 9.46]], [[§37 Determinants#^ladr-9-56|LADR 9.56]], [[§3 Continuity and Limits of Functions#^thm-3-1|452 §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-2|452 §3.2]]

> [!definition] Definition §11.5: General Linear Group
> The **general linear group** is
>
> $$
> \mathrm{GL}(n, \mathbb{R}) = \det{}^{-1}\big(\mathbb{R} \setminus \{0\}\big) = \{\, g \in \operatorname{Mat}(n,\mathbb{R}) \mid g \text{ is invertible} \,\},
> $$
>
> with the subspace topology. Being the preimage of an open set under a continuous map, it is an **open subset** of $\operatorname{Mat}(n,\mathbb{R}) \cong \mathbb{R}^{n^2}$.
>
> *Lee: Example 1.27*

^def-11-5

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[Invertible ⟺ nonzero determinant|LADR 9.50]], [[§10 Continuous Functions#^def-10-1|590 Def. §10.1]]

> [!remark]- Connections
> - The group in 493: [[§3 Basic Examples of Groups#^def-3-6|493 Def. §3.6]], workhorse example [[Matrix groups GLₙ, SLₙ and O(n)]].

> [!theorem] Proposition §11.4: $\mathrm{GL}(n,\mathbb{R})$ Is a Topological Group
> $\mathrm{GL}(n,\mathbb{R})$ with the subspace topology is a topological group.
>
> *Lee: Examples 1.27 and 7.3*

^prop-11-4

> [!proof]+ Proof
> *(Lecture 3: the formulas are algebraic — the product in the coordinates, the inverse “using cofactors and determinants” — “so one and two are algebraic maps, hence continuous.” The details are filled in below.)* Multiplication: $(gh)_{ik} = \sum_j g_{ij} h_{jk}$ is a polynomial in the entries of $(g,h) \in \mathbb{R}^{n^2} \times \mathbb{R}^{n^2} = \mathbb{R}^{2n^2}$, so $\operatorname{Mat} \times \operatorname{Mat} \to \operatorname{Mat}$ is continuous; its restriction to $\mathrm{GL} \times \mathrm{GL}$ (subspace of the product, which is the product of the subspaces) is continuous and lands in $\mathrm{GL}$, hence is continuous into $\mathrm{GL}$ by [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]]. Inversion: by the cofactor formula, $g^{-1} = \operatorname{adj}(g)/\det(g)$, where each entry of the adjugate $\operatorname{adj}(g)$ is a polynomial in the entries of $g$ and $\det(g) \neq 0$ on $\mathrm{GL}$; so each entry of $g^{-1}$ is a rational function with nonvanishing denominator, hence continuous on $\mathrm{GL}$. Uribe's summary: “one and two are algebraic maps, hence continuous.”

^pf-11-4

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Def. §11.1]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Def. §11.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-5|Def. §11.5]], [[§3 Subspaces and Products#^prop-3-3|§3.3]], [[§9 Matrices#^ladr-3-46|LADR 3.46]], [[§3 Continuity and Limits of Functions#^thm-3-2|452 §3.2]], [[§3 Continuity and Limits of Functions#^thm-3-3|452 §3.3]], [[§11 Product Topology on Arbitrary Products#^thm-11-1|590 §11.1]]

> [!remark]- Connections
> - The smooth structure on $\operatorname{Mat}(n,\mathbb{R})$, of which $\mathrm{GL}(n,\mathbb{R})$ is an open subset: [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]; all the classical groups together: [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]].
> - The inverse by cofactors, $g^{-1} = \operatorname{adj}(g)/\det(g)$, used for continuity of inversion: [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|235 Thm. §27.2]], with the adjugate of [[§27 Cramer’s Rule, Volume, and Linear Transformations#^def-27-2|235 Def. §27.2]].

The disconnectedness of $\mathrm{GL}(n,\mathbb{R})$ and of $\mathrm{O}(n)$, why $\mathrm{SO}(n)$ is a proper subgroup of $\mathrm{O}(n)$, and $\mathrm{U}(1) = S^1$ are collected in [[§16 The Classical Groups|§16]].

> [!definition] Definition §11.6: Special Linear Group
> $\mathrm{SL}(n,\mathbb{R}) = \det^{-1}(1) \subseteq \mathrm{GL}(n,\mathbb{R})$, the matrices of determinant $1$. It is a subgroup ($\det$ is multiplicative), hence a topological group with the subspace topology ([[§11 Topological Groups and Classical Matrix Groups#^prop-11-1|Proposition §11.1]]), and it is closed in $\operatorname{Mat}(n,\mathbb{R})$ (preimage of the closed set $\{1\}$).

^def-11-6

*Uses:* [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-1|§11.1]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4|§11.4]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[Equivalent Conditions for Continuity|590 §10.1]]

> [!remark]- Connections
> - The group in 493: [[§3 Basic Examples of Groups#^def-3-7|493 Def. §3.7]]; $\mathrm{SL}_n = \ker\det$, [[§15 Homomorphisms#^ex-15-1|493 Ex. §15.1]].
> - $\mathrm{SL}(n,\mathbb{R})$ is a manifold: [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]] below.

> [!definition] Definition §11.7: Orthogonal Group
> The **orthogonal group** is
>
> $$
> \mathrm{O}(n,\mathbb{R}) = \{\, g \in \mathrm{GL}(n,\mathbb{R}) \mid (gx) \cdot (gy) = x \cdot y \ \text{ for all } x, y \in \mathbb{R}^n \,\},
> $$
>
> the linear maps preserving the dot product.

^def-11-7

> [!remark]- Connections
> - In linear algebra, the isometries of $\mathbb{R}^n$: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]]; in 493, [[§3 Basic Examples of Groups#^def-3-7|493 Def. §3.7]].
> - $\mathrm{O}(n)$ is a manifold of dimension $\tfrac{n(n-1)}{2}$: [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]].
> - Used in Relativity: the Lorentz group $O(1, 3)$, the matrices preserving the form $\eta$, and its four pieces — [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]].

> [!theorem] Proposition §11.5: Equivalent Description of $\mathrm{O}(n,\mathbb{R})$
> For $g \in \mathrm{GL}(n,\mathbb{R})$ the following are equivalent: (i) $g \in \mathrm{O}(n,\mathbb{R})$; (ii) $g^T g = I$; (iii) $g^{-1} = g^T$. Consequently $\det(g)^2 = 1$, i.e. $\det g = \pm 1$, for every $g \in \mathrm{O}(n,\mathbb{R})$.
>
> *Lee: Example 7.27*

^prop-11-5

> [!proof]+ Proof
> *(Stated in Lecture 3 — “$g \in \mathrm{O}(n) \iff g^{-1} = g^{\mathsf T}$”; filled in.)* Writing the dot product as $x \cdot y = x^T y$, we have $(gx)\cdot(gy) = x^T g^T g\, y$. If $g^T g = I$ this equals $x^T y$, so (ii) $\Rightarrow$ (i). Conversely, if (i) holds, take $x = e_i$, $y = e_j$: then $(g^T g)_{ij} = e_i^T g^T g\, e_j = e_i \cdot e_j = \delta_{ij}$, so $g^T g = I$. (ii) $\iff$ (iii) since for square matrices a one-sided inverse is two-sided. Finally $1 = \det(I) = \det(g^T g) = \det(g^T)\det(g) = \det(g)^2$.

^pf-11-5

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|Def. §11.7]], [[§10 Invertibility and Isomorphisms#^ladr-3-68|LADR 3.68]], [[§37 Determinants#^ladr-9-49|LADR 9.49]], [[§37 Determinants#^ladr-9-56|LADR 9.56]]

> [!remark]- Connections
> - The real case of [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]] (characterizations of unitary matrices).

> [!definition] Definition §11.8: Special Orthogonal Group
> $\mathrm{SO}(n,\mathbb{R}) = \mathrm{O}(n,\mathbb{R}) \cap \mathrm{SL}(n,\mathbb{R}) = \{\, g \in \mathrm{O}(n,\mathbb{R}) \mid \det g = 1 \,\}$.

^def-11-8

> [!remark]- Connections
> - The group in 493: [[§3 Basic Examples of Groups#^def-3-7|493 Def. §3.7]]; the rotation group of the cube, a finite subgroup of SO(3), is isomorphic to S₄, [[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|493 Thm. §32.5]].
> - Used in Quantum Mechanics: the rotation group $SO(3)$ and its action on kets — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^def-c5-1-1|QM Def. §C5.1.1]].

> [!definition] Definition §11.9: Complex Matrices and $\mathrm{GL}(n,\mathbb{C})$
> Once and for all, fix the $\mathbb{R}$-linear identification $\mathbb{C} \cong \mathbb{R}^2$, $x + iy \mapsto (x, y)$, and hence $\mathbb{C}^n \cong \mathbb{R}^{2n}$: explicitly, writing $z_j = x_j + i y_j$,
>
> $$
> (z_1, \ldots, z_n) \longmapsto (x_1, y_1, x_2, y_2, \ldots, x_n, y_n).
> $$
>
> (Any other ordering of the real coordinates, e.g. all $x$'s first, differs by a linear homeomorphism and changes nothing topologically; the choice made in [[§9 Complex Projective Space|§9]] was of the latter kind.) Applying this to each entry of a complex matrix, in the row-by-row order of [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Definition §11.2]], gives the coordinate map
>
> $$
> \operatorname{Mat}(n,\mathbb{C}) \longrightarrow \mathbb{R}^{2n^2}, \qquad g \longmapsto \big(\operatorname{Re} g_{11}, \operatorname{Im} g_{11},\ \operatorname{Re} g_{12}, \operatorname{Im} g_{12},\ \ldots,\ \operatorname{Re} g_{nn}, \operatorname{Im} g_{nn}\big),
> $$
>
> which defines the topology on $\operatorname{Mat}(n,\mathbb{C})$. Then $\det : \operatorname{Mat}(n,\mathbb{C}) \to \mathbb{C} \cong \mathbb{R}^2$ is continuous (its real and imaginary parts are polynomials in these $2n^2$ real coordinates, since $\det$ is a polynomial in the complex entries), and
>
> $$
> \mathrm{GL}(n,\mathbb{C}) = \det{}^{-1}(\mathbb{C} \setminus \{0\}) = \{\text{invertible complex } n \times n \text{ matrices}\}
> $$
>
> is open in $\operatorname{Mat}(n,\mathbb{C})$ and is a topological group by the same algebraic argument as over $\mathbb{R}$.
>
> *Lee: Examples 7.29 and 7.30*

^def-11-9

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-2|Def. §11.2]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-4|§11.4]], [[Invertible ⟺ nonzero determinant|LADR 9.50]]

> [!remark]- Connections
> - $\mathbb{C} \cong \mathbb{R}^2$ in 590: [[§10 Continuous Functions#^ex-10-5|590 Ex. §10.5]].

> [!definition] Definition §11.10: Unitary Group
> The **unitary group**, a subgroup of $\mathrm{GL}(n,\mathbb{C})$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Definition §11.9]]), is
>
> $$
> \mathrm{U}(n) = \{\, g \in \mathrm{GL}(n,\mathbb{C}) \mid g^{-1} = \bar{g}^{\,T} \,\},
> $$
>
> where $\bar g$ is the entrywise complex conjugate; $\bar g^{\,T}$ is also written $g^\dagger$ or $g^*$. It is the analogue of $\mathrm{O}(n)$ with the dot product replaced by the Hermitian inner product $\langle z, w \rangle = \sum_j z_j \bar w_j$: $g \in \mathrm{U}(n)$ iff $\langle gz, gw \rangle = \langle z, w \rangle$ for all $z, w$ (same proof as [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|Proposition §11.5]], with $e_i^T \bar{g}^{\,T} g\, e_j$ in place of $e_i^T g^T g\, e_j$).
>
> *Lee: Examples 7.29 and 7.30*

^def-11-10

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^def-11-9|Def. §11.9]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-5|§11.5]]

> [!remark]- Connections
> - Unitary matrices in linear algebra: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-56|LADR 7.56]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR 7.57]].
> - $\mathrm{U}(n)$ is a manifold of dimension $n^2$: [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]].
> - Used in Quantum Mechanics: $U(2)$ and $SU(2)$ as the groups of spin-½ rotations, $SU(2) \cong S^3$, a double cover of $SO(3)$ — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^def-c5-2-1|QM Def. §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]].
> - Used in Quantum Field Theory: $SU(2)$, identified with the sphere $S^3$, is compact, and averaging over it makes every finite-dimensional representation of $SU(2)$ and $SO(3)$ unitary and completely reducible; for the non-compact Lorentz group no nontrivial finite-dimensional representation is unitary — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-5|QFT Theorem §C3.1.5]], [[§C3.2 The Lorentz Algebra and Its Finite-Dimensional Representations#^thm-c3-2-12|QFT Theorem §C3.2.12]].

> [!example] Example §11.3: $\mathrm{U}(1)$ Is the Circle
> A $1 \times 1$ complex matrix is a number $\xi \in \mathbb{C}$, all such matrices are symmetric, and the condition $\xi^{-1} = \bar\xi$ reads $\xi \bar\xi = |\xi|^2 = 1$. So
>
> $$
> \mathrm{U}(1) = \{\, \xi \in \mathbb{C} \setminus \{0\} \mid |\xi| = 1 \,\} = S^1,
> $$
>
> the unit circle, which is the notation “everybody uses.” This is the group acting in the construction of $\mathbb{CP}^n$ ([[§9 Complex Projective Space|§9]]).

^ex-11-3

> [!remark]- Connections
> - The circle group in 590: [[§10 Continuous Functions#^ex-10-5|590 Ex. §10.5]]; $\mathbb{CP}^n = S^{2n+1}/\mathrm{U}(1)$ as an orbit space: [[§13 Group Actions and Orbit Spaces#^ex-13-3|Ex. §13.3]].

The circle through the course: the circle group $\mathrm{U}(1)$ in [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|U(1) is the circle]]; the homogeneous space $\mathbb{R}/\mathbb{Z}$ in [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1|the circle as R/Z]]; three atlases — four charts, stereographic and angle — in [[§17 Differentiable Structures#^ex-17-2|the four-chart atlas]], [[§17 Differentiable Structures#^ex-17-3|the stereographic atlas]] and [[§17 Differentiable Structures#^ex-17-4|the angle atlas]], with [[§17 Differentiable Structures#^rem-17-9|three atlases and one structure]]; $\mathbb{RP}^1$ homeomorphic to it in [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]]; its external, graph and internal descriptions, and the one smooth structure of its three atlases, in [[§24 The Circle|The Circle]]; and covered by a line, a local diffeomorphism that is not injective, in [[§33 Local Diffeomorphisms#^ex-33-1|the circle covered by a line]].
