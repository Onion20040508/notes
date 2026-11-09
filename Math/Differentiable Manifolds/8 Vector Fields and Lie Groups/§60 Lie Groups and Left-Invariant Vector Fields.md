---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 8
section: 60
tags: [differentiable-manifolds, math591]
---
← [[§59 Related Vector Fields]] · ↑ [[· 8 Vector Fields and Lie Groups]] · [[§61 Lie Group Morphisms and Linear Groups]] →

*Stage: symmetry — Groups that are manifolds, and the vector fields that respect the group: the start of Lie theory.*

*Lecture 16, last three minutes, to be continued. References: Lee Ch. 7 and Ch. 8. Lie algebras and Lie groups are related, and in one direction the relationship is very nice: every Lie group has a Lie algebra associated to it.*

> [!definition] Definition §60.1: Lie Group
> A **Lie group** is a [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological group]] $G$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Definition §11.1]]) together with a [[§17 Differentiable Structures#^def-17-9|smooth structure]], such that multiplication $G \times G \to G$, $(g, h) \mapsto gh$, and inversion $G \to G$, $g \mapsto g^{-1}$, are [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth maps]].
>
> *Lee: Ch. 7, Basic Definitions*

^def-60-1

> [!remark]- Connections
> - The physicists' version, closed subgroups of $\mathrm{GL}(n,\mathbb{C})$: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|QFT Def. §CB.1.3]].

For a topological group the two maps had to be continuous; now they are required to be smooth, which makes sense because $G$ has a manifold structure.

> [!theorem] Proposition §60.1: The Classical Groups Are Lie Groups
> $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$ and $\mathrm{SU}(2)$, with the smooth structures of [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]] and [[§48 SU(2) → SO(3)꞉ The Double Cover|§48]], are [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie groups]].
>
> *Lee: Examples 7.3, 7.27–7.30*

^prop-60-1

> [!proof]+ Proof
> *(Stated in Lecture 16 for all the matrix groups seen so far; filled in.)* By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]], for each group $G$ of the list it has to be shown that multiplication $G \times G \to G$ and inversion $G \to G$ are smooth; they are then continuous, so $G$ is also a topological group (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|§11.1]]).
>
> *The setting.* Each group $G$ is an open subset or a submanifold of a space of matrices $\operatorname{Mat}$, which is $\operatorname{Mat}(n,\mathbb{R}) = \mathbb{R}^{n^2}$ or $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ (real and imaginary parts of the entries) (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]; for $\mathrm{SU}(2)$, Proposition [[§47 The Unit Quaternions and SU(2)#^prop-47-5|§47.5]]). The inclusion $\iota : G \hookrightarrow \operatorname{Mat}$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]]). And a smooth map into $\operatorname{Mat}$ that lands in $G$ is smooth into $G$: by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2) for a submanifold; for an open subset because its chart is the restriction of the linear chart of $\operatorname{Mat}$ (proof of Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]), so the map has the same coordinate representations as a map into $G$ and as a map into $\operatorname{Mat}$.
>
> *Multiplication* is the composite of $\iota \times \iota : G \times G \to \operatorname{Mat} \times \operatorname{Mat}$, $(g, h) \mapsto (g, h)$, with matrix multiplication $\operatorname{Mat} \times \operatorname{Mat} \to \operatorname{Mat}$.
> - $\iota \times \iota$ is smooth since its components are: they are $\iota \circ \pi_1$ and $\iota \circ \pi_2$, smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]] and Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], and a map into the Euclidean space $\operatorname{Mat} \times \operatorname{Mat}$ is smooth when its components are.
> - Matrix multiplication is smooth: the entries $(AB)_{ij} = \sum_k A_{ik} B_{kj}$ are polynomials in the real coordinates (in the complex case, the real and imaginary parts of $\sum_k A_{ik} B_{kj}$ are polynomials in the real and imaginary parts of the entries).
>
> So the composite $(g, h) \mapsto gh$ is smooth into $\operatorname{Mat}$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). It lands in $G$, because $G$ is a group under matrix multiplication; so it is smooth into $G$, by the last sentence of the setting.
>
> *Inversion* is the restriction of a smooth map on the open set of invertible matrices — $g \mapsto \operatorname{adj}(g)/\det g$ by the cofactor formula, a rational map with nonvanishing denominator — landing in $G$, hence smooth into $G$ in the same way. In detail: the set of invertible matrices in $\operatorname{Mat}$ is $\det^{-1}$ of the nonzero numbers, open since $\det$ is continuous. On it, the entries of $\operatorname{adj}(g)$ and $\det g$ are polynomials in the entries of $g$, and $\det g \ne 0$, so $g \mapsto \operatorname{adj}(g)/\det g = g^{-1}$ is smooth; in the complex case, dividing by $\det g$ is multiplying by $\overline{\det g}/|\det g|^2$, again rational in the real coordinates with nonvanishing denominator $|\det g|^2$. Every $G$ of the list consists of invertible matrices, so $g \mapsto g^{-1}$ on $G$ is this map composed with $\iota$, smooth into $\operatorname{Mat}$; it lands in $G$, because $G$ is closed under inverses; so it is smooth into $G$. (For $\mathrm{O}(n)$ and $\mathrm{U}(n)$ it is even linear: $g \mapsto g^{\mathsf T}$, $g \mapsto g^{\ast}$.)

^pf-60-1

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§47 The Unit Quaternions and SU(2)#^prop-47-5|§47.5]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|235 Thm. §27.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Def. §11.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]]

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-6|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-7|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-5|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-3|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§48 SU(2) → SO(3)꞉ The Double Cover#^thm-48-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§58 Lie Bracket and Lie Algebra#^ex-58-3|Ex. §58.3]]; and Lie groups in [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-1|§60.1]].

The unit quaternions $S^3$ are a Lie group as well ([[§47 The Unit Quaternions and SU(2)#^prop-47-4|Proposition §47.4]]), isomorphic to $\mathrm{SU}(2)$ ([[§47 The Unit Quaternions and SU(2)#^prop-47-5|Proposition §47.5]]).

*Assignment 6, Problem 1: the differentials of multiplication and inversion at the identity. Not from lecture; the submitted solution, with the notation of these notes ($\mu$ for the multiplication, written $m$ in the assignment).*

> [!theorem] Proposition §60.2: The Differential of Multiplication at the Identity
> Let $G$ be a Lie group with identity $e$ and multiplication $\mu : G \times G \to G$, $\mu(g, h) = gh$. Under the identification $T_{(e,e)}(G \times G) = T_eG \oplus T_eG$ of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]],
>
> $$
> d\mu_{(e,e)}(A, B) = A + B, \qquad A, B \in T_eG .
> $$
>
> *Lee: Problem 7-2(a)*

^prop-60-2

> [!proof]+ Proof
> *(Assignment 6, Problem 1(a); the submitted solution.)* Let $\pi_1, \pi_2 : G \times G \to G$ be the projections and $\iota_1, \iota_2 : G \to G \times G$ the slice inclusions through $(e, e)$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]),
>
> $$
> \iota_1(g) = (g, e), \qquad \iota_2(g) = (e, g) .
> $$
>
> *The vectors $(A, 0)$ and $(0, B)$.* The identification of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]] sends $v \in T_{(e,e)}(G \times G)$ to $\big(d(\pi_1)_{(e,e)}(v),\, d(\pi_2)_{(e,e)}(v)\big)$. Since $\pi_1 \circ \iota_1 = \mathrm{id}_G$ and $\pi_2 \circ \iota_1$ is the constant map to $e$, the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]] give, for $A \in T_eG$,
>
> $$
> d(\pi_1)_{(e,e)}\big(d(\iota_1)_e(A)\big) = A, \qquad d(\pi_2)_{(e,e)}\big(d(\iota_1)_e(A)\big) = 0,
> $$
>
> so $d(\iota_1)_e(A) = (A, 0)$. In the same way, $d(\iota_2)_e(B) = (0, B)$ for $B \in T_eG$. With $n = \dim G$ and $I_n = \mathrm{id}_{T_eG}$, in block form with respect to $T_eG \oplus T_eG$,
>
> $$
> d(\iota_1)_e = \begin{pmatrix} I_n \\ 0 \end{pmatrix}, \qquad d(\iota_2)_e = \begin{pmatrix} 0 \\ I_n \end{pmatrix}.
> $$
>
> *Computing $d\mu_{(e,e)}(A, 0)$.* For $g \in G$, $\mu(\iota_1(g)) = \mu(g, e) = ge = g$, so $\mu \circ \iota_1 = \mathrm{id}_G$. By the chain rule,
>
> $$
> d\mu_{(e,e)} \circ d(\iota_1)_e = d(\mu \circ \iota_1)_e = d(\mathrm{id}_G)_e = \mathrm{id}_{T_eG},
> \qquad\text{so}\qquad
> d\mu_{(e,e)}(A, 0) = d\mu_{(e,e)}\big(d(\iota_1)_e(A)\big) = A .
> $$
>
> *Computing $d\mu_{(e,e)}(0, B)$.* Likewise $\mu(\iota_2(g)) = \mu(e, g) = eg = g$, so $\mu \circ \iota_2 = \mathrm{id}_G$, and the chain rule gives
>
> $$
> d\mu_{(e,e)}(0, B) = d\mu_{(e,e)}\big(d(\iota_2)_e(B)\big) = d(\mu \circ \iota_2)_e(B) = B .
> $$
>
> *Conclusion.* Since $(A, B) = (A, 0) + (0, B)$ in $T_eG \oplus T_eG$ and $d\mu_{(e,e)}$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]),
>
> $$
> d\mu_{(e,e)}(A, B) = d\mu_{(e,e)}(A, 0) + d\mu_{(e,e)}(0, B) = A + B .
> $$
>
> In block form,
>
> $$
> d\mu_{(e,e)} = \begin{pmatrix} I_n & I_n \end{pmatrix}, \qquad d\mu_{(e,e)}\begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix} I_n & I_n \end{pmatrix}\begin{pmatrix} A \\ B \end{pmatrix} = A + B .
> $$

^pf-60-2

*Uses:* [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]

> [!theorem] Proposition §60.3: The Differential of Inversion at the Identity
> Let $G$ be a Lie group with identity $e$ and inversion $j : G \to G$, $j(g) = g^{-1}$. Then
>
> $$
> dj_e(A) = -A, \qquad A \in T_eG .
> $$
>
> *Lee: Problem 7-2(b)*

^prop-60-3

> [!proof]+ Proof
> *(Assignment 6, Problem 1(b), “a version of implicit differentiation”; the submitted solution.)* Define
>
> $$
> F = (\mathrm{id}_G, j) : G \to G \times G, \qquad F(g) = (g, j(g)),
> $$
>
> which is smooth since its components $\mathrm{id}_G$ and $j$ are (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]), with $\pi_1 \circ F = \mathrm{id}_G$ and $\pi_2 \circ F = j$. Since $j(e) = e^{-1} = e$, $F(e) = (e, e)$. For every $g \in G$,
>
> $$
> \mu(F(g)) = \mu(g, j(g)) = gg^{-1} = e,
> $$
>
> so $\mu \circ F = c_e$, the constant map $G \to G$ with value $e$.
>
> *The differential of $F$.* By the chain rule, for $A \in T_eG$,
>
> $$
> d(\pi_1)_{(e,e)}\big(dF_e(A)\big) = d(\mathrm{id}_G)_e(A) = A, \qquad d(\pi_2)_{(e,e)}\big(dF_e(A)\big) = dj_e(A),
> $$
>
> so under the identification of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], $dF_e(A) = (A, dj_e(A))$. In block form,
>
> $$
> dF_e = \begin{pmatrix} I_n \\ dj_e \end{pmatrix}.
> $$
>
> *The differential of $c_e$.* For $v \in T_eG$ and a smooth function $f$ defined near $e$, $f \circ c_e$ is constant, so $d(c_e)_e(v)f = v(f \circ c_e) = 0$. Hence $d(c_e)_e = 0$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]).
>
> *Conclusion.* Applying the chain rule to $\mu \circ F = c_e$ at $e$, and using Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-2|§60.2]],
>
> $$
> 0 = d(c_e)_e = d\mu_{(e,e)} \circ dF_e = \begin{pmatrix} I_n & I_n \end{pmatrix}\begin{pmatrix} I_n \\ dj_e \end{pmatrix} = I_n + dj_e .
> $$
>
> Therefore $dj_e = -I_n$, that is, $dj_e(A) = -A$ for all $A \in T_eG$.

^pf-60-3

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-2|§60.2]]

For a matrix group both are first-order expansions: $(I + tA)(I + tB) = I + t(A + B) + O(t^2)$ and $(I + tA)^{-1} = I - tA + O(t^2)$. At a general point the same proofs give the formulas of Propositions [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-12|§60.12]] and [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-14|§60.14]], in [[§60 Lie Groups and Left-Invariant Vector Fields|§60]], once right translations are available.

> [!definition] Definition §60.2: Left Translation
> For $g$ in a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] $G$, **left translation** by $g$ is $L_g : G \to G$, $L_g(h) = gh$.
>
> *Lee: Ch. 7, Basic Definitions*

^def-60-2

> [!theorem] Lemma §60.4: Left Translations Are Diffeomorphisms
> $L_g$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], with inverse $L_{g^{-1}}$.
>
> *Lee: Ch. 7, Basic Definitions*

^lem-60-4

> [!proof]+ Proof
> *(Filled in, as for topological groups in Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]].)* By Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]], it has to be shown that $L_g$ is a smooth bijection with smooth inverse, and that the inverse is $L_{g^{-1}}$.
>
> *Smooth.* $L_g$ is smooth as the composite of $h \mapsto (g, h)$ with multiplication: $L_g(h) = gh = \mu\big(\iota^{g}(h)\big)$, where $\iota^{g} : G \to G \times G$, $h \mapsto (g, h)$, is the slice inclusion of Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]] (with $M_1 = M_2 = G$ and $p_1 = g$), smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]], and $\mu : G \times G \to G$ is multiplication, smooth by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]. So $L_g = \mu \circ \iota^{g}$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). The same holds for every element of $G$, in particular for $g^{-1}$: $L_{g^{-1}}$ is smooth.
>
> *Inverse.* For $h \in G$, by associativity of the group product,
>
> $$
> L_g\big(L_{g^{-1}}(h)\big) = g\,(g^{-1}h) = (gg^{-1})\,h = h, \qquad L_{g^{-1}}\big(L_g(h)\big) = g^{-1}(gh) = (g^{-1}g)\,h = h .
> $$
>
> So $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$: $L_g$ is a bijection with inverse $L_{g^{-1}}$, and both are smooth, so $L_g$ is a diffeomorphism.

^pf-60-4

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|Def. §60.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]]

> [!definition] Definition §60.3: Left-Invariant Vector Field
> A [[§56 Vector Fields#^def-56-1|vector field]] $\mathbf{X} \in \mathfrak{X}(G)$ is **left-invariant** if for all $g, h \in G$
>
> $$
> (L_g)_{*h}\, \mathbf{X}_h = \mathbf{X}_{gh} .
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-60-3

![[m591-49-1.svg]]
*Left invariance as a diagram: the differential $(L_g)_{\ast h}$ of [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|left translation]] carries the value $\mathbf{X}_h$ of the field at $h$ to its value $\mathbf{X}_{gh}$ at $gh$.*

Left invariance in one line: pushing vectors of the field forward by left translations always gives the corresponding vectors of the field. The value at one point determines the field everywhere: taking $h = e$, $\mathbf{X}_g = (L_g)_{\ast e}\, \mathbf{X}_e$. This is the [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|left translation]] of tangent spaces from the discussion of moving the base point ([[§48 SU(2) → SO(3)꞉ The Double Cover#^lem-48-3|Lemma §48.3]]), applied to a whole field.

![[m591-49-a4.gif|640]]

*(Not from lecture; animation added, vault only.)* Invariant fields on the group $G$ of matrices $\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}$, $a > 0$ (chosen for the picture), drawn in the coordinates $(b, a)$, with $e = (a, b) = (1, 0)$ and $A = u\,\partial_a + v\,\partial_b \in T_eG$. Multiplying matrices, $(a, b)(a', b') = (aa',\ ab' + b)$. Left: for $g = (a, b)$, $L_g(a', b') = (aa', ab' + b)$ scales by $a$ and shifts, so the disc about $e$ is carried to a disc about $g$ and $d(L_g)_e(A) = aA$: the left-invariant field with value $A$ at $e$ is $\mathbf{X}^A_g = a\,(u\,\partial_a + v\,\partial_b)$, which is $gA$ of Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]] for these matrices. Right: the right translation $R_g(a', b') = (a'a,\ a'b + b')$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-7|§60.7]]) shears the disc, and the right-invariant extension of the same $A$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-9|§60.9]]) is $\mathbf{Y}^A_g = d(R_g)_e(A) = ua\,\partial_a + (ub + v)\,\partial_b$, a different field. In both panels the value at $e$ determines the whole field (grey).

> [!example] Example §60.1: Left-Invariant Fields on $\mathrm{GL}(n,\mathbb{R})$
> On $G = \mathrm{GL}(n,\mathbb{R})$, open in $\operatorname{Mat}(n,\mathbb{R})$, so that $T_gG = \operatorname{Mat}(n,\mathbb{R})$, the [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|left-invariant vector fields]] are exactly
>
> $$
> \mathbf{X}^A_g = gA, \qquad A \in \operatorname{Mat}(n,\mathbb{R}) = T_IG .
> $$

^ex-60-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *The identification.* $G$ is open in the vector space $\operatorname{Mat}(n,\mathbb{R})$, so $T_gG = T_g\operatorname{Mat}(n,\mathbb{R})$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), and $T_g\operatorname{Mat}(n,\mathbb{R}) \cong \operatorname{Mat}(n,\mathbb{R})$ by $v \leftrightarrow D_v|_g$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]); this is the identification $T_gG = \operatorname{Mat}(n,\mathbb{R})$ of the statement.
>
> *The differential of $L_g$.* $L_g$ is the restriction to $G$ of the linear map $\ell_g : \operatorname{Mat}(n,\mathbb{R}) \to \operatorname{Mat}(n,\mathbb{R})$, $h \mapsto gh$, so its differential at every point is that same linear map: $(L_g)_{\ast h}(v) = gv$. Indeed, $\iota \circ L_g = \ell_g \circ \iota$ for the inclusion $\iota : G \hookrightarrow \operatorname{Mat}(n,\mathbb{R})$, so by the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) $\iota_{\ast gh} \circ (L_g)_{\ast h} = (\ell_g)_{\ast h} \circ \iota_{\ast h}$, and $\iota_{\ast}$ is the identification of Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]; and by Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] for the linear map $\ell_g$, $(\ell_g)_{\ast h}(D_v|_h) = D_{gv}|_{gh}$.
>
> *Left-invariant fields are of the form $\mathbf{X}^A$.* By the last step, left invariance (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]) reads
>
> $$
> g\,\mathbf{X}_h = \mathbf{X}_{gh} \qquad \text{for all } g, h \in G,
> $$
>
> with $\mathbf{X}_h \in \operatorname{Mat}(n,\mathbb{R})$. Taking $h = I$ gives $\mathbf{X}_g = \mathbf{X}_{gI} = g\,\mathbf{X}_I$, so $\mathbf{X} = \mathbf{X}^A$ with $A = \mathbf{X}_I$.
>
> *Every $\mathbf{X}^A$ is a left-invariant field.* Conversely, let $A \in \operatorname{Mat}(n,\mathbb{R})$. By associativity of matrix multiplication,
>
> $$
> (L_g)_{\ast h}\big(\mathbf{X}^A_h\big) = g\,(hA) = (gh)A = \mathbf{X}^A_{gh},
> $$
>
> so every $\mathbf{X}^A$ is left-invariant. It is smooth because its entries are linear in those of $g$: in the global chart of $G$ given by the matrix entries $x^{ij}$, the coefficients of $\mathbf{X}^A$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]) are $\mathbf{X}^A_g[x^{ij}] = D_{gA}|_g[x^{ij}] = \frac{d}{dt}\big|_{t=0}\, x^{ij}(g + t\,gA) = (gA)_{ij} = \sum_k g_{ik} A_{kj}$, linear in the entries of $g$, hence smooth.

^pf-ex-60-1

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|Def. §60.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]

Compare [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]], where $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$ for the classical groups: a left-invariant field moves the tangent space at the identity around the group by left multiplication. Later in this section, $\mathbf{X}^A$ is the left-invariant extension of $A \in T_IG$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]): by the differential of $L_g$ computed in the proof above, $(L_g)_{\ast I}(A) = gA = \mathbf{X}^A_g$.

> [!definition] Definition §60.4: The Lie Algebra of a Lie Group
> The **Lie algebra** of a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] $G$ is
>
> $$
> \mathfrak{g} = \{\, \mathbf{X} \in \mathfrak{X}(G) \mid \mathbf{X} \text{ is left-invariant} \,\},
> $$
>
> with the [[§58 Lie Bracket and Lie Algebra#^def-58-1|Lie bracket of vector fields]].
>
> *Lee: Ch. 8, Lie Algebras*

^def-60-4

> [!remark]- Connections
> - The physicists' definition for matrix Lie groups, directly as $T_{\mathbb 1}G$ with the matrix commutator: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|QFT Def. §CB.1.11]].

*Status.* Defined in Lecture 16, where $\mathfrak{g}$ was announced to be soon identified with the tangent space at the identity; originally, though, its elements are a very special type of vector field, because that is where the Lie bracket comes from. For $\mathrm{GL}(n,\mathbb{R})$ the identification is $\mathbf{X}^A \mapsto A$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). The two facts announced then were proved in Lecture 17, in [[§60 Lie Groups and Left-Invariant Vector Fields|§60]] below: $\mathfrak{g}$ is closed under the bracket, and $\mathbf{X} \mapsto \mathbf{X}_e$ is an isomorphism onto $T_eG$ (its last step, smoothness, completed in Lecture 18).

## The Lie Algebra and the Tangent Space at the Identity

*Lecture 17. Back to Lie groups: with the language of [[§59 Related Vector Fields#^def-59-2|related fields]], some of the definitions can be rephrased.*

> [!theorem] Lemma §60.5: Left-Invariance as Relatedness
> A vector field $\mathbf{X} \in \mathfrak{X}(G)$ is [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|left-invariant]] ([[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Definition §60.3]]) if and only if, for every $g \in G$, $\mathbf{X}$ is *$L_g$-related to itself* ([[§59 Related Vector Fields#^def-59-2|Definition §59.2]] with $F = L_g$ and $\mathbf{Y} = \mathbf{X}$).

^lem-60-5

> [!proof]+ Proof
> *(Lecture 17, a rephrasing of the definition.)* Being $L_g$-related to itself means $d(L_g)_h(\mathbf{X}_h) = \mathbf{X}_{L_g(h)} = \mathbf{X}_{gh}$ for every $h \in G$, which is the condition of [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Definition §60.3]] for this $g$.

^pf-60-5

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|Def. §60.2]]

> [!remark] Remark: Why Left?
> Lecture 17 abbreviates “left-invariant” to l.i. Nothing is wrong with right: a choice has to be made, and left is the universal choice. Right-invariant fields, $R_g$-related to themselves for $R_g(h) = hg$, give an equivalent theory; the one place the choice shows is the sign of the bracket, at the end of this subsection ([[§60 Lie Groups and Left-Invariant Vector Fields#^rem-60-2|Remark: Left or Right]]). Right-invariant fields are worked out in [[§60 Lie Groups and Left-Invariant Vector Fields#Right-Invariant Vector Fields|§60, Right-Invariant Vector Fields]].

^rem-60-1

> [!theorem] Corollary §60.6: $\mathfrak{g}$ Is a Lie Subalgebra of $\mathfrak{X}(G)$
> If $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ then $[\mathbf{X}, \mathbf{Y}] \in \mathfrak{g}$. So $\mathfrak{g}$, a linear subspace of $\mathfrak{X}(G)$, is a [[§58 Lie Bracket and Lie Algebra#^def-58-2|Lie algebra]] under the [[§58 Lie Bracket and Lie Algebra#^def-58-1|bracket of vector fields]].
>
> *Lee: Proposition 8.33*

^cor-60-6

> [!proof]+ Proof
> *(Lecture 17: a consequence of Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]].)* *Closed under the bracket.* Let $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ and fix $g \in G$. By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], $\mathbf{X}$ is $L_g$-related to $\mathbf{X}$ and $\mathbf{Y}$ to $\mathbf{Y}$. So by Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]] with $F = L_g$, $\mathbf{X}_1 = \mathbf{Y}_1 = \mathbf{X}$ and $\mathbf{X}_2 = \mathbf{Y}_2 = \mathbf{Y}$, $[\mathbf{X}, \mathbf{Y}]$ is $L_g$-related to $[\mathbf{X}, \mathbf{Y}]$. This holds for every $g$, and by Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]] again (in the converse direction) this for every $g$ is left-invariance: $[\mathbf{X}, \mathbf{Y}] \in \mathfrak{g}$.
>
> *(Filled in.)* *A linear subspace.* $\mathfrak{g}$ is a linear subspace because each $d(L_g)_h$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). Explicitly, let $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ and $a, b \in \mathbb{R}$. For all $g, h \in G$, by the pointwise operations of Definition [[§56 Vector Fields#^def-56-2|§56.2]], the linearity of $d(L_g)_h$, and left-invariance of $\mathbf{X}$ and $\mathbf{Y}$,
>
> $$
> d(L_g)_h\big((a\mathbf{X} + b\mathbf{Y})_h\big) = d(L_g)_h\big(a\,\mathbf{X}_h + b\,\mathbf{Y}_h\big) = a\, d(L_g)_h(\mathbf{X}_h) + b\, d(L_g)_h(\mathbf{Y}_h) = a\,\mathbf{X}_{gh} + b\,\mathbf{Y}_{gh} = (a\mathbf{X} + b\mathbf{Y})_{gh} .
> $$
>
> So $a\mathbf{X} + b\mathbf{Y} \in \mathfrak{g}$; and the zero field is in $\mathfrak{g}$, since a linear map sends $0$ to $0$.
>
> *A Lie algebra.* By the first step the bracket of vector fields restricts to a map $\mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$. The bracket on $\mathfrak{g}$ is bilinear, skew and satisfies Jacobi because it does on $\mathfrak{X}(G)$ (Corollary [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]]): these are identities for all elements of $\mathfrak{X}(G)$, so in particular for all elements of $\mathfrak{g}$. So $\mathfrak{g}$ is a Lie algebra (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-2|§58.2]]).

^pf-60-6

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|Def. §60.4]], [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§56 Vector Fields#^def-56-2|Def. §56.2]], [[§58 Lie Bracket and Lie Algebra#^def-58-2|Def. §58.2]]

So $\mathfrak{g}$ is a Lie subalgebra of the infinite-dimensional Lie algebra of all vector fields on $G$. Vector fields can be added and scaled, so $\mathfrak{X}(G)$ is a [[§56 Vector Fields#^def-56-2|vector space]] (in fact a module over the smooth functions, but here it is regarded as a vector space). At this point it is not yet clear what $\mathfrak{g}$ is: a priori it could still be infinite-dimensional, or zero. [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|The theorem]] below settles it. Its proof rests on a construction, made in Lecture 17 and finished in Lecture 18, which comes first.

> [!definition] Definition §60.5: Left-Invariant Extension
> Let $G$ be a Lie group with identity $e$, and $v \in T_eG$. The **left-invariant extension** of $v$ is the map $\mathbf{X}^v : G \to TG$, $g \mapsto \mathbf{X}^v_g$, with
>
> $$
> \mathbf{X}^v_g = d(L_g)_e(v) \in T_gG, \qquad g \in G :
> $$
>
> the vector $v$ carried from $e$ to $g$ by the differential of the left translation $L_g$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|§60.2]]). It is a *rough* vector field (Lee's term), a tangent vector at every point, not yet known to be smooth.
>
> *Lee: proof of Theorem 8.37*

^def-60-5

As with vector fields on a vector space (Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]]), there is a unique left translation carrying $e$ to $g$, and $\mathbf{X}^v_g$ is $v$ carried along it.

> [!theorem] Lemma §60.7: The Left-Invariant Extension Is Left-Invariant
> Let $G$ be a Lie group with identity $e$.
>
> 1. For $v \in T_eG$, $\mathbf{X}^v_g \in T_gG$ for every $g \in G$, and $\mathbf{X}^v_e = v$.
> 2. For $v \in T_eG$, $\mathbf{X}^v$ satisfies the identity of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]: $d(L_g)_h\big(\mathbf{X}^v_h\big) = \mathbf{X}^v_{gh}$ for all $g, h \in G$.
> 3. Every $\mathbf{X} \in \mathfrak{g}$ is the left-invariant extension of its value at $e$: $\mathbf{X}_g = d(L_g)_e(\mathbf{X}_e)$ for every $g \in G$, that is, $\mathbf{X} = \mathbf{X}^{\mathbf{X}_e}$.
>
> *Lee: proof of Theorem 8.37*

^lem-60-7

> [!proof]+ Proof
> *(Lecture 17, steps of the proof that $\mathfrak{g}$ is $T_eG$; (2) was left to check, and done in the review at the start of Lecture 19.)*
>
> *(1)* $L_g$ maps $e$ to $g$, so $d(L_g)_e : T_eG \to T_{L_g(e)}G = T_{ge}G = T_gG$, and $\mathbf{X}^v_g = d(L_g)_e(v)$ lies in $T_gG$. And $L_e = \mathrm{id}_G$ (as $eh = h$), so $\mathbf{X}^v_e = (\mathrm{id}_G)_{\ast e}(v) = v$ by Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]].
>
> *(2)* *(Lecture 19.)* Fix $h, g \in G$. To end up at $g$ one has to start at $h^{-1}g$: $L_h$ maps $h^{-1}g$ to $g$. By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] and the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]),
>
> $$
> d(L_h)_{h^{-1}g}\big(\mathbf{X}^v_{h^{-1}g}\big) = d(L_h)_{h^{-1}g}\, d(L_{h^{-1}g})_e(v) = d\big(L_h \circ L_{h^{-1}g}\big)_e(v) = d(L_g)_e(v) = \mathbf{X}^v_g ,
> $$
>
> because $L_h \circ L_{h^{-1}g} = L_g$: multiplying on the left by $h^{-1}g$ and then on the left by $h$, the $h$ and the $h^{-1}$ cancel. Writing $k = h^{-1}g$, this says $d(L_h)_k(\mathbf{X}^v_k) = \mathbf{X}^v_{hk}$ for all $h, k \in G$, the identity of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]].
>
> *(3)* Let $\mathbf{X} \in \mathfrak{g}$ and $g \in G$. Left-invariance (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]) with $h = e$ reads $d(L_g)_e(\mathbf{X}_e) = \mathbf{X}_{ge} = \mathbf{X}_g$, and by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] with $v = \mathbf{X}_e$ the left side is $\mathbf{X}^{\mathbf{X}_e}_g$.

^pf-60-7

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]]

> [!theorem] Proposition §60.8: The Left-Invariant Extension Is Smooth
> Let $G$ be a Lie group with identity $e$ and $v \in T_eG$. For $f \in C^\infty(G)$ let $\varphi : G \times G \to \mathbb{R}$, $\varphi(g, x) = f(gx)$. Then $\varphi$ is smooth, and
>
> $$
> \mathbf{X}^v f = \partial_v\varphi \in C^\infty(G),
> $$
>
> the partial derivative of $\varphi$ in the second variable in the direction $v$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-4|§31.4]]). Hence $\mathbf{X}^v$ is smooth: $\mathbf{X}^v \in \mathfrak{g}$, a left-invariant vector field with $\mathbf{X}^v_e = v$.
>
> *Lee: proof of Theorem 8.37*

^prop-60-8

> [!proof]+ Proof
> *(Lecture 18, completing the proof of Lecture 17.)* Lecture 17 stopped here: what was missing is that $\mathbf{X}^v$ is $C^\infty$, an important technical point for which the tools were not yet available. Lecture 18 finished it with the partial derivative construction (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-4|§31.4]]). So far $\mathbf{X}^v$ is a left-invariant *rough* field (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](1) and (2)), Lee's term for a section not yet known to be smooth; the piece of the construction not yet justified is its smoothness.
>
> *The claim.* It suffices to show that for every $f \in C^\infty(G)$ the function $\mathbf{X}^v f : g \mapsto \mathbf{X}^v_g[f]$ is smooth. This function is well defined whether or not $\mathbf{X}^v$ is smooth, because there is a vector at every point, and it can act on any function. The lecture's proof of the claim: in local coordinates $(x^1, \ldots, x^m)$, $m = \dim G$, there is still a pointwise expansion $\mathbf{X}^v = \sum_j a^j\, \partial/\partial x^j$, and $\mathbf{X}^v$ is smooth exactly when the $a^j$ are (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]); and $a^j$ is precisely the action of $\mathbf{X}^v$ on the coordinate $x^j$. This is Lemma [[§56 Vector Fields#^lem-56-8|§56.8]], whose proof also handles the point that $x^j$ is defined only on the chart, by extending it with a bump function.
>
> *The construction.* Let $f \in C^\infty(G)$ and $g \in G$. By the definition of $\mathbf{X}^v$ and of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]),
>
> $$
> (\mathbf{X}^v f)(g) = d(L_g)_e(v)[f] = v[f \circ L_g] \in \mathbb{R},
> $$
>
> and the point is that, as a function of $g$, this is smooth. The trick is to construct
>
> $$
> \varphi : G \times G \xrightarrow{\ \text{multiplication}\ } G \xrightarrow{\ f\ } \mathbb{R}, \qquad \varphi(g, x) = f(gx) = (f \circ L_g)(x).
> $$
>
> It is smooth, as the composite of the multiplication, smooth by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]], with $f$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). Fixing $g$ in the first variable, $f \circ L_g = \varphi(g, \cdot)$, so by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-4|§31.4]], in the second variable with $w = v \in T_eG$,
>
> $$
> (\mathbf{X}^v f)(g) = v\big[\varphi(g, \cdot)\big] = \partial_v\varphi(g) .
> $$
>
> Here $v$ acts on the second variable, and so the result is smooth: $\partial_v\varphi \in C^\infty(G)$ by Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-10|§31.10]](3). By the claim, $\mathbf{X}^v$ is smooth. It is left-invariant (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](2)), so $\mathbf{X}^v \in \mathfrak{g}$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|§60.4]]), and $\mathbf{X}^v_e = v$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](1)).

^pf-60-8

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-4|Def. §31.4]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§56 Vector Fields#^lem-56-8|§56.8]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§31 Tangent Vectors as Velocities of Curves#^prop-31-10|§31.10]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|Def. §60.4]]

> [!theorem] Theorem §60.9: The Lie Algebra Is the Tangent Space at the Identity
> Let $G$ be a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] with identity $e$. The evaluation map
>
> $$
> \mathrm{ev} : \mathfrak{g} \to T_eG, \qquad \mathbf{X} \mapsto \mathbf{X}_e ,
> $$
>
> is a linear isomorphism. In particular $\dim \mathfrak{g} = \dim G$.
>
> *Lee: Theorem 8.37*

^thm-60-9

> [!proof]+ Proof
> *(Lecture 17, incomplete by one detail that could not yet be proved there; completed in Lecture 18. The lecture's steps.)* $\mathrm{ev}$ is linear: for $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ and $a, b \in \mathbb{R}$, $\mathrm{ev}(a\mathbf{X} + b\mathbf{Y}) = (a\mathbf{X} + b\mathbf{Y})_e = a\,\mathbf{X}_e + b\,\mathbf{Y}_e$ by Definition [[§56 Vector Fields#^def-56-2|§56.2]]. It remains to show that $\mathrm{ev}$ is injective and surjective.
>
> *The basic idea.* For $g \in G$, $L_g$ maps $e$ to $g$, so $d(L_g)_e : T_eG \to T_gG$, and for $\mathbf{X} \in \mathfrak{g}$, left-invariance (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]) with $h = e$ reads
>
> $$
> d(L_g)_e(\mathbf{X}_e) = \mathbf{X}_g ;
> $$
>
> more generally $d(L_g)_h(\mathbf{X}_h) = \mathbf{X}_{gh}$ for all $h$. So there is only one choice: $\mathbf{X}$ is the left-invariant extension of $\mathbf{X}_e$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](3)).
>
> *Injective.* By the basic idea, $\mathbf{X}$ is determined by its value at $e$. So $\mathbf{X}_e = 0$ forces $\mathbf{X}_g = d(L_g)_e(0) = 0$ for all $g$, since $d(L_g)_e$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). So the kernel of the linear map $\mathrm{ev}$ is $\{\mathbf{0}\}$, and $\mathrm{ev}$ is injective.
>
> *Surjective.* Start with $v \in T_eG$; we want a left-invariant $\mathbf{X}$ with $\mathbf{X}_e = v$. The basic idea says there is no choice: we must take the left-invariant extension of $v$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]),
>
> $$
> \mathbf{X}^v_g = d(L_g)_e(v), \qquad g \in G .
> $$
>
> By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](1) and (2), which are Lecture 17's steps, $\mathbf{X}^v$ is a rough vector field, a tangent vector at every point, with $\mathbf{X}^v_e = v$ and satisfying the left-invariance identity. *Smooth.* This is where Lecture 17 stopped; Lecture 18 finished it, and by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]] $\mathbf{X}^v$ is smooth, through $\mathbf{X}^v f = \partial_v\varphi$ for $\varphi(g, x) = f(gx)$. So $\mathbf{X}^v \in \mathfrak{g}$ and $\mathrm{ev}(\mathbf{X}^v) = v$.
>
> Finally, a linear isomorphism preserves dimension, so $\dim \mathfrak{g} = \dim T_eG = \dim G$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-10|§29.10]]).

^pf-60-9

*Uses:* [[§56 Vector Fields#^def-56-2|Def. §56.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-10|§29.10]]

> [!remark]- Connections
> - The matrix-group version, with $\mathfrak g$ defined through the exponential and identified with $T_{\mathbb 1}G$ and with the left-invariant fields: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|QFT Theorem §CB.1.16]].

![[m591-50-1.svg]]
*The left-invariant field $\mathbf{X}^v$: the vector $v \in T_eG$ carried to $g$ by the differential of the left translation $L_g$.*

**Comparison with Lee.** Lee's proof (Theorem 8.37) differentiates $f(g\,\gamma(t))$ along a curve $\gamma$ adapted to $v$, which is Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-10|§31.10]](1) applied to the function $\varphi(g, x) = f(gx)$ of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]]: $(\mathbf{X}^v f)(g) = \frac{d}{dt}\big|_{t=0} \varphi(g, \gamma(t))$. The course packages that step once and for all as the partial derivative $\partial_v\varphi$.

> [!example] Example §60.2: The Additive Group of a Vector Space
> Let $V$ be a finite-dimensional vector space, a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] under addition with identity $0$, so that $L_p = \tau_p$ is translation by $p$. Its [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|left-invariant vector fields]] are the constant fields $\mathbf{X}^v : p \mapsto D_v|_p$, $v \in V$, and all their [[§58 Lie Bracket and Lie Algebra#^def-58-1|brackets]] vanish: $\mathfrak{g} \cong V$ with the zero bracket.

^ex-60-2

> [!proof]+ Proof
> *(Not from lecture; filled in, after the remark in Lecture 17 that the translations of a vector space give a left-invariant vector field.)* *$V$ is a Lie group.* In linear coordinates (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]), addition $(p, q) \mapsto p + q$ and inversion $p \mapsto -p$ are linear, hence smooth; so $V$ is a Lie group (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]), with $L_p(q) = p + q = \tau_p(q)$.
>
> *The left-invariant fields.* By Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], every element of $T_0V$ is $D_v|_0$ for a unique $v \in V$. By Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]] and Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]](3), the left-invariant fields are exactly the left-invariant extensions $\mathbf{X}^w$, $w \in T_0V$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]), with $\mathbf{X}^w_p = d(L_p)_0(w)$. For $w = D_v|_0$, Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]](2) gives
>
> $$
> \mathbf{X}^{w}_p = d(\tau_p)_0\big(D_v|_0\big) = D_v|_p ,
> $$
>
> so the field $\mathbf{X}^v$ of the example, the left-invariant extension of $D_v|_0$, is $p \mapsto D_v|_p$; by the theorem these are all the left-invariant fields. The map $v \mapsto \mathbf{X}^v$ is the composite of the isomorphism $v \mapsto D_v|_0$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] with $\mathrm{ev}^{-1}$, so it is a linear isomorphism $V \cong \mathfrak{g}$.
>
> *The brackets vanish.* Choose a basis of $V$ and the corresponding linear coordinates $x^1, \ldots, x^n$, a global chart, and write $v = \sum_i v^i e_i$. The coefficients of $\mathbf{X}^v$ (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]) are, using Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]] and the linearity of $x^i$,
>
> $$
> \mathbf{X}^v_p[x^i] = D_v|_p[x^i] = \frac{d}{dt}\Big|_{t=0} x^i(p + tv) = \frac{d}{dt}\Big|_{t=0} \big(x^i(p) + t\,v^i\big) = v^i .
> $$
>
> So in linear coordinates $\mathbf{X}^v = \sum_i v^i\, \partial_i$ has constant coefficients, and likewise $\mathbf{X}^w = \sum_i w^i\, \partial_i$. By Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], the $j$-th coefficient of $[\mathbf{X}^v, \mathbf{X}^w]$ is $\sum_i \big(v^i\, \partial w^j/\partial x^i - w^i\, \partial v^j/\partial x^i\big) = 0$, since the partial derivatives of constants vanish. So $[\mathbf{X}^v, \mathbf{X}^w] = 0$ for all $v, w$: $\mathfrak{g} \cong V$ with the zero bracket.

^pf-ex-60-2

*Uses:* [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§30 The Differential in Coordinates#^prop-30-7|§30.7]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]]

> [!definition] Definition §60.6: The Lie Bracket on $T_eG$
> Let $G$ be a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] and, for $v \in T_eG$, let $\mathbf{X}^v \in \mathfrak{g}$ be its left-invariant extension (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]]), the left-invariant field with $\mathbf{X}^v_e = v$, unique by Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]. The **Lie bracket** on $T_eG$ is
>
> $$
> [v, w] = \big[\mathbf{X}^v, \mathbf{X}^w\big]_e , \qquad v, w \in T_eG .
> $$

^def-60-6

By construction $\mathrm{ev}$ is then an isomorphism of [[§58 Lie Bracket and Lie Algebra#^def-58-2|Lie algebras]]: $T_eG$ inherits the bracket that makes it one. The question is what this bracket is.

> [!theorem] Theorem §60.10: The Lie Algebra of $\mathrm{GL}(d,\mathbb{R})$
> Let $G = \mathrm{GL}(d, \mathbb{R})$, the $d \times d$ invertible matrices, an open subset of $\operatorname{Mat}(d, \mathbb{R}) \cong \mathbb{R}^{d^2}$, so that $T_IG = \operatorname{Mat}(d,\mathbb{R})$. The Lie bracket on $T_IG$ ([[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Definition §60.6]]) is the matrix commutator
>
> $$
> [A, B] = AB - BA .
> $$

^thm-60-10

> [!proof]+ Proof
> *(Lecture 19: here diagram chasing no longer suffices, and something has to be computed. The lecture's computation, with the index bookkeeping written out. Lecture 19 proved this together with Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-3|§61.3]], which reduces every linear group to this case.)*
>
> *Coordinates.* Write $A = (a^i_j)$, with $i$ the row index and $j$ the column index, and call a general group element $X = (x^i_j) \in \mathrm{GL}(d, \mathbb{R})$ rather than $g$, to think of it as a variable. Written out,
>
> $$
> A = \begin{pmatrix} a^1_1 & \cdots & a^1_d \\ \vdots & \ddots & \vdots \\ a^d_1 & \cdots & a^d_d \end{pmatrix},
> \qquad
> X = \begin{pmatrix} x^1_1 & \cdots & x^1_d \\ \vdots & \ddots & \vdots \\ x^d_1 & \cdots & x^d_d \end{pmatrix},
> $$
>
> the upper index numbering the rows and the lower index the columns. The entries $x^i_j$ are the standard coordinates of $\operatorname{Mat}(d,\mathbb{R}) \cong \mathbb{R}^{d^2}$, indexed by pairs, and a tangent vector $V = (V^i_j) \in \operatorname{Mat}(d, \mathbb{R}) = T_X\mathrm{GL}(d,\mathbb{R})$ is $\sum_{i,j} V^i_j\, \partial/\partial x^i_j|_X$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]). The basic computation is
>
> $$
> \frac{\partial}{\partial x^i_j}\big(x^l_n\big) = \delta_{il}\, \delta_{jn} ,
> $$
>
> one or zero according to whether the coordinate being differentiated is the one the partial is taken with respect to.
>
> *The left-invariant field.* $\mathbf{X}^A_X = d(L_X)_I(A)$, and $L_X : \mathbb{R}^{d^2} \to \mathbb{R}^{d^2}$, $Y \mapsto XY$, is linear, so it is its own differential (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]): $\mathbf{X}^A_X = XA$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). The $(i,j)$ entry of $XA$ is $\sum_k x^i_k a^k_j$, so
>
> $$
> \mathbf{X}^A = \sum_{i,j} \Big( \sum_k x^i_k\, a^k_j \Big) \frac{\partial}{\partial x^i_j}, \qquad
> \mathbf{X}^B = \sum_{l,n} \Big( \sum_m x^l_m\, b^m_n \Big) \frac{\partial}{\partial x^l_n},
> $$
>
> with independent indices for the second field, since the two sums are independent. The $a^k_j$ and $b^m_n$ are constants; the $x$'s are functions. (So the sums can be taken out of the commutator, which is bilinear over constants, but the $x$'s cannot be pulled out, because they are functions.)
>
> *The bracket.* The second derivatives can be ignored, because they cancel in the bracket (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]): by Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], the coefficient of $\partial/\partial x^l_n$ in $[\mathbf{X}^A, \mathbf{X}^B]$ is $\mathbf{X}^A$ applied to the coefficient of $\mathbf{X}^B$, minus the same with $A$ and $B$ exchanged. Applying the basic computation,
>
> $$
> \mathbf{X}^A\Big( \sum_m x^l_m\, b^m_n \Big) = \sum_{i,j,k,m} x^i_k\, a^k_j\, b^m_n\, \delta_{il}\, \delta_{jm} = \sum_{k} x^l_k \Big( \sum_j a^k_j\, b^j_n \Big) = \sum_k x^l_k\, (AB)^k_n :
> $$
>
> setting $i = l$ and $m = j$ is all that happens, and then $\sum_j a^k_j\, b^j_n$ is an entry of a matrix, the $(k, n)$ entry of $AB$. So
>
> $$
> [\mathbf{X}^A, \mathbf{X}^B] = \sum_{l,n} \Big( \sum_k x^l_k\, (AB)^k_n \Big) \frac{\partial}{\partial x^l_n} - \big(\text{the same with } A \text{ and } B \text{ exchanged}\big) = \mathbf{X}^{AB} - \mathbf{X}^{BA},
> $$
>
> comparing with the formula for $\mathbf{X}^A$ with $AB$, resp. $BA$, in place of $A$.
>
> *Evaluate at the identity.* By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]] and $\mathbf{X}^C_I = C$,
>
> $$
> [A, B] = [\mathbf{X}^A, \mathbf{X}^B]_I = \mathbf{X}^{AB}_I - \mathbf{X}^{BA}_I = AB - BA .
> $$

^pf-60-10

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^thm-61-3|§61.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Def. §60.6]]

Coordinate-free, the computation says: a field $X \mapsto XC$ on an open subset of $\operatorname{Mat}(d,\mathbb{R})$ is linear in $X$, and the bracket of the linear fields $X \mapsto XA$ and $X \mapsto XB$ is the linear field $X \mapsto X(AB - BA)$.

> [!remark]- Connections
> - The commutator Lie algebra of matrices: [[§58 Lie Bracket and Lie Algebra#^ex-58-2|Ex. §58.2]].
> - For matrix Lie groups the physics notes prove the answer: the bracket of left-invariant fields becomes $XY - YX$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|QFT Theorem §CB.1.16]], part 3), and $\mathfrak g$ is closed under it ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|QFT Theorem §CB.1.12]]).

> [!remark] Remark: Left or Right: The Sign of the Bracket
> The formula $[A, B] = AB - BA$ holds because left-invariant fields are used; with right-invariant fields the bracket would be minus that. Why left, then? Many things would work better if functions were written to the right of their arguments, $(x)f$ instead of $f(x)$: in that notation, composites read in the order the maps are applied. *(Proved in [[§60 Lie Groups and Left-Invariant Vector Fields|§60]]: Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-19|§60.19]], Assignment 6, Problem 2(b).)*

^rem-60-2

**Transcription note (Lecture 17).** Page 46 of the handwritten notes says the construction gives “$\mathbf{X} : M \to TM$”; the manifold is the group, $\mathbf{X} : G \to TG$.

## Right-Invariant Vector Fields

*Assignment 6, Problem 2, with what its solution contains. Not from lecture. Lecture 17 said there is nothing wrong with right (the remark *Why Left?*) and Lecture 19 that right-invariant fields give the bracket with the opposite sign (the remark *Left or Right: The Sign of the Bracket*); this subsection proves both. Elements of $T_eG$ are written $A, B$, as in the assignment. The general formulas for the differentials of multiplication and inversion, which need right translations, are filled in here as well.*

> [!definition] Definition §60.7: Right Translation
> For $g$ in a Lie group $G$, **right translation** by $g$ is $R_g : G \to G$, $R_g(k) = kg$.
>
> *Lee: Ch. 7, Basic Definitions*

^def-60-7

> [!theorem] Lemma §60.11: Right Translations
> Let $G$ be a Lie group with identity $e$ and $g, h \in G$.
>
> 1. $R_g \circ R_h = R_{hg}$ and $R_e = \mathrm{id}_G$. Note the order: first $h$, then $g$.
> 2. $R_g$ is a diffeomorphism, with inverse $R_{g^{-1}}$.
> 3. Left and right translations commute: $L_g \circ R_h = R_h \circ L_g$.

^lem-60-11

> [!proof]+ Proof
> *(1)* *(The submitted solution.)* For $k \in G$, $(R_g \circ R_h)(k) = R_g(kh) = khg = R_{hg}(k)$, so $R_g \circ R_h = R_{hg}$. Also $R_e(k) = ke = k$, so $R_e = \mathrm{id}_G$.
>
> *(Filled in.)* *(2)* As in Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-4|§60.4]]: $R_g = \mu \circ \iota^{g}$, where $\iota^{g} : G \to G \times G$, $k \mapsto (k, g)$, is the slice inclusion (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]], with $p_2 = g$), smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]], and $\mu$ is the multiplication, smooth by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]; so $R_g$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), and so is $R_{g^{-1}}$. By (1), $R_g \circ R_{g^{-1}} = R_{g^{-1}g} = R_e = \mathrm{id}_G$ and $R_{g^{-1}} \circ R_g = R_{gg^{-1}} = \mathrm{id}_G$. So $R_g$ is a smooth bijection with smooth inverse $R_{g^{-1}}$, a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]).
>
> *(3)* For $k \in G$, by associativity, $L_g(R_h(k)) = g(kh) = (gk)h = R_h(L_g(k))$.

^pf-60-11

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-4|§60.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]], [[§19 Smooth Functions and Smooth Maps#^prop-19-12|§19.12]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]]

> [!theorem] Proposition §60.12: The Differential of Multiplication
> Let $G$ be a Lie group with multiplication $\mu$, and $g, h \in G$. Under the identification $T_{(g,h)}(G \times G) = T_gG \oplus T_hG$ of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]],
>
> $$
> d\mu_{(g,h)}(v, w) = d(R_h)_g(v) + d(L_g)_h(w), \qquad v \in T_gG,\ w \in T_hG .
> $$
>
> At $(g, h) = (e, e)$, where $R_e = L_e = \mathrm{id}_G$, this is Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-2|§60.2]].

^prop-60-12

> [!proof]+ Proof
> *(Not from the assignment; the proof of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-2|§60.2]] at the point $(g, h)$.)* Let $\iota_1(x) = (x, h)$ and $\iota_2(y) = (g, y)$ be the slice inclusions through $(g, h)$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]), so that $(v, w)$ stands for $\Theta(v, w) = d(\iota_1)_g(v) + d(\iota_2)_h(w)$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]]). For $x, y \in G$,
>
> $$
> (\mu \circ \iota_1)(x) = xh = R_h(x), \qquad (\mu \circ \iota_2)(y) = gy = L_g(y),
> $$
>
> so $\mu \circ \iota_1 = R_h$ and $\mu \circ \iota_2 = L_g$. By the linearity of $d\mu_{(g,h)}$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]) and the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]),
>
> $$
> d\mu_{(g,h)}(v, w) = d\mu_{(g,h)}\big(d(\iota_1)_g(v)\big) + d\mu_{(g,h)}\big(d(\iota_2)_h(w)\big) = d(\mu \circ \iota_1)_g(v) + d(\mu \circ \iota_2)_h(w) = d(R_h)_g(v) + d(L_g)_h(w) .
> $$

^pf-60-12

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-2|§60.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-7|§31.7]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]

> [!theorem] Lemma §60.13: Inversion Exchanges Left and Right Translations
> Let $G$ be a Lie group with inversion $j$, and $g \in G$.
>
> 1. $j \circ L_g = R_{g^{-1}} \circ j$.
> 2. $j$ is a diffeomorphism, and $j^{-1} = j$.

^lem-60-13

> [!proof]+ Proof
> *(1)* *(Assignment 6, Problem 2(a): the submitted solution's “key identity”.)* For $k \in G$,
>
> $$
> (j \circ L_g)(k) = j(gk) = (gk)^{-1} = k^{-1}g^{-1} = R_{g^{-1}}(k^{-1}) = (R_{g^{-1}} \circ j)(k) .
> $$
>
> *(2)* *(Filled in.)* $j$ is smooth (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]), and $j(j(k)) = (k^{-1})^{-1} = k$, so $j \circ j = \mathrm{id}_G$: $j$ is a smooth bijection whose inverse $j$ is smooth.

^pf-60-13

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]]

> [!theorem] Proposition §60.14: The Differential of Inversion
> Let $G$ be a Lie group with identity $e$ and inversion $j$, and $g \in G$. Then
>
> $$
> dj_g = -\,d(R_{g^{-1}})_e \circ d(L_{g^{-1}})_g : T_gG \longrightarrow T_{g^{-1}}G .
> $$
>
> At $g = e$ this is Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-3|§60.3]].

^prop-60-14

> [!proof]+ Proof
> *(Not from the assignment.)* By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-13|§60.13]](1), $j \circ L_g = R_{g^{-1}} \circ j$. Both sides map $e$ to $g^{-1}$; by the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) at $e$, with $L_g(e) = g$, $j(e) = e$ and $dj_e = -\mathrm{id}$ (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-3|§60.3]]),
>
> $$
> dj_g \circ d(L_g)_e = d(R_{g^{-1}})_e \circ dj_e = -\,d(R_{g^{-1}})_e .
> $$
>
> By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-4|§60.4]], $L_{g^{-1}} \circ L_g = \mathrm{id}_G$ and $L_g \circ L_{g^{-1}} = \mathrm{id}_G$, so by the chain rule $d(L_g)_e$ is invertible with inverse $d(L_{g^{-1}})_g$. Composing the display on the right with $d(L_{g^{-1}})_g$ gives the formula.

^pf-60-14

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-13|§60.13]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-3|§60.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-4|§60.4]]

For a matrix group, where $d(L_g)$ and $d(R_g)$ are multiplication by $g$ on the left and on the right (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]] and Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-3|§60.3]] below), this reads $d\mu_{(g,h)}(v, w) = vh + gw$ and $dj_g(v) = -g^{-1}vg^{-1}$: the product rule and the derivative of the inverse matrix.

> [!definition] Definition §60.8: Right-Invariant Vector Field
> A vector field $\mathbf{Y}$ on a Lie group $G$ is **right-invariant** if it is $R_g$-related to itself for every $g \in G$ (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]): for all $g, h \in G$,
>
> $$
> d(R_g)_h\, \mathbf{Y}_h = \mathbf{Y}_{R_g(h)} = \mathbf{Y}_{hg} .
> $$
>
> The same identity defines a right-invariant *rough* field, a tangent vector at every point not yet known to be smooth (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]).

^def-60-8

> [!definition] Definition §60.9: Right-Invariant Extension
> Let $G$ be a Lie group with identity $e$ and $A \in T_eG$. The **right-invariant extension** of $A$ is the rough field $\mathbf{Y}^A : G \to TG$,
>
> $$
> \mathbf{Y}^A_g = d(R_g)_e(A) \in T_gG, \qquad g \in G,
> $$
>
> which makes sense since $R_g(e) = g$. Beside it, $\mathbf{X}^A_g = d(L_g)_e(A)$ is the left-invariant extension (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]).

^def-60-9

> [!theorem] Proposition §60.15: Right-Invariant Fields and the Tangent Space at the Identity
> Let $G$ be a Lie group with identity $e$.
>
> 1. For $A \in T_eG$, $\mathbf{Y}^A$ is right-invariant and $\mathbf{Y}^A_e = A$.
> 2. Every right-invariant (rough) field $\mathbf{Y}$ is $\mathbf{Y}^A$ for $A = \mathbf{Y}_e$.
> 3. The map $A \mapsto \mathbf{Y}^A$ is linear, and it is a bijection from $T_eG$ onto the right-invariant rough fields, with inverse $\mathbf{Y} \mapsto \mathbf{Y}_e$. In particular $\mathbf{Y}^{-A} = -\mathbf{Y}^A$.

^prop-60-15

> [!proof]+ Proof
> *(Assignment 6, Problem 2(a), “following what we did in class” (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]]); the submitted solution. The linearity in (3) is from its part (b).)*
>
> *(1) $\mathbf{Y}^A$ is right-invariant.* For $g, h \in G$, by the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], as $R_h(e) = h$) and Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-11|§60.11]](1),
>
> $$
> d(R_g)_h\,\mathbf{Y}^A_h = d(R_g)_h\, d(R_h)_e(A) = d(R_g \circ R_h)_e(A) = d(R_{hg})_e(A) = \mathbf{Y}^A_{hg} .
> $$
>
> *$\mathbf{Y}^A_e = A$.* Since $R_e = \mathrm{id}_G$, $\mathbf{Y}^A_e = d(R_e)_e(A) = d(\mathrm{id}_G)_e(A) = A$.
>
> *(2) Every right-invariant field is of this form.* Let $\mathbf{Y}$ be right-invariant and $A = \mathbf{Y}_e$. Taking $h = e$ in the right-invariance identity, for every $g \in G$,
>
> $$
> \mathbf{Y}_g = \mathbf{Y}_{eg} = d(R_g)_e\,\mathbf{Y}_e = d(R_g)_e(A) = \mathbf{Y}^A_g,
> $$
>
> so $\mathbf{Y} = \mathbf{Y}^A$.
>
> *(3)* By (1) and (2), $A \mapsto \mathbf{Y}^A$ and $\mathbf{Y} \mapsto \mathbf{Y}_e$ are mutually inverse. The map $A \mapsto \mathbf{Y}^A$ is linear since each $d(R_g)_e$ is (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]); in particular $\mathbf{Y}^{-A}_g = d(R_g)_e(-A) = -\mathbf{Y}^A_g$ for all $g$.

^pf-60-15

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-7|§60.7]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-11|§60.11]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]

> [!theorem] Proposition §60.16: Inversion Carries Left-Invariant to Right-Invariant Fields
> Let $G$ be a Lie group with inversion $j$, and $A \in T_eG$. For every $g \in G$,
>
> $$
> dj_g\big(\mathbf{X}^A_g\big) = \mathbf{Y}^{-A}_{j(g)} = \mathbf{Y}^{-A}_{g^{-1}} .
> $$

^prop-60-16

> [!proof]+ Proof
> *(Assignment 6, Problem 2(a); the submitted solution.)* *The right-hand side.* Since $j(g) = g^{-1}$ and $d(R_{g^{-1}})_e$ is linear,
>
> $$
> \mathbf{Y}^{-A}_{j(g)} = \mathbf{Y}^{-A}_{g^{-1}} = d(R_{g^{-1}})_e(-A).
> $$
>
> *The left-hand side.* By the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), using $L_g(e) = g$, $j(e) = e$, Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-13|§60.13]](1), and $dj_e(A) = -A$ (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-3|§60.3]]),
>
> $$
> dj_g\,\mathbf{X}^A_g = dj_g\, d(L_g)_e(A) = d(j \circ L_g)_e(A) = d(R_{g^{-1}} \circ j)_e(A) = d(R_{g^{-1}})_e\, dj_e(A) = d(R_{g^{-1}})_e(-A).
> $$
>
> Comparing the two sides, $dj_g\,\mathbf{X}^A_g = \mathbf{Y}^{-A}_{j(g)}$ for every $g \in G$.

^pf-60-16

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-13|§60.13]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-3|§60.3]]

> [!theorem] Corollary §60.17: Right-Invariant Extensions Are Smooth
> Let $G$ be a Lie group with inversion $j$, and $A \in T_eG$. Then $\mathbf{Y}^{-A} = j_\ast\mathbf{X}^A$, the pushforward of the left-invariant field $\mathbf{X}^A$ by the diffeomorphism $j$ (Definition [[§59 Related Vector Fields#^def-59-1|§59.1]]). Hence every $\mathbf{Y}^A$ is smooth, and $\mathbf{X}^A$ and $\mathbf{Y}^{-A}$ are $j$-related (Definition [[§59 Related Vector Fields#^def-59-2|§59.2]]).

^cor-60-17

> [!proof]+ Proof
> *(Not from the assignment, which did not ask for smoothness: “You do not have to prove that $Y^A$ is smooth.” It follows from its part (a).)* By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-13|§60.13]](2), $j$ is a diffeomorphism with $j^{-1} = j$. For $q \in G$, by Definition [[§59 Related Vector Fields#^def-59-1|§59.1]] and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-16|§60.16]] at $g = j^{-1}(q) = q^{-1}$,
>
> $$
> (j_\ast\mathbf{X}^A)_q = dj_{q^{-1}}\big(\mathbf{X}^A_{q^{-1}}\big) = \mathbf{Y}^{-A}_{j(q^{-1})} = \mathbf{Y}^{-A}_q .
> $$
>
> $\mathbf{X}^A$ is smooth (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]]), so $\mathbf{Y}^{-A} = j_\ast\mathbf{X}^A$ is smooth by Proposition [[§59 Related Vector Fields#^prop-59-2|§59.2]]. As $A$ ranges over $T_eG$, so does $-A$: every $\mathbf{Y}^A$ is smooth. Now both are vector fields, and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-16|§60.16]] is the $j$-relatedness condition of Definition [[§59 Related Vector Fields#^def-59-2|§59.2]].

^pf-60-17

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-13|§60.13]], [[§59 Related Vector Fields#^def-59-1|Def. §59.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-16|§60.16]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]], [[§59 Related Vector Fields#^prop-59-2|§59.2]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]]

So the right-invariant vector fields are exactly the $\mathbf{Y}^A$, $A \in T_eG$ (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]]), and they are smooth: the right-handed version of Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]], here obtained from the left-handed one through $j$ rather than by repeating Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-8|§60.8]].

> [!definition] Definition §60.10: The Right Bracket
> Let $G$ be a Lie group with identity $e$. For $A, B \in T_eG$, the **right bracket** is
>
> $$
> [A, B]^R = \big[\mathbf{Y}^A, \mathbf{Y}^B\big]_e \in T_eG,
> $$
>
> with $\mathbf{Y}^A, \mathbf{Y}^B$ the right-invariant extensions (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-9|§60.9]]).

^def-60-10

> [!theorem] Proposition §60.18: The Right Bracket Is a Lie Bracket
> Let $G$ be a Lie group and $A, B \in T_eG$. The bracket $[\mathbf{Y}^A, \mathbf{Y}^B]$ is right-invariant, and
>
> $$
> \big[\mathbf{Y}^A, \mathbf{Y}^B\big] = \mathbf{Y}^{[A,B]^R} .
> $$
>
> $[\ ,\ ]^R$ is a Lie bracket on $T_eG$ (Definition [[§58 Lie Bracket and Lie Algebra#^def-58-2|§58.2]]).

^prop-60-18

> [!proof]+ Proof
> *(Assignment 6, Problem 2(b); the submitted solution.)* *The bracket is right-invariant.* Let $g \in G$. Since $\mathbf{Y}^A$ and $\mathbf{Y}^B$ are right-invariant, each is $R_g$-related to itself (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-8|§60.8]]); they are smooth (Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]]), so by the naturality of the bracket (Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]]) $[\mathbf{Y}^A, \mathbf{Y}^B]$ is $R_g$-related to itself. As $g$ is arbitrary, $[\mathbf{Y}^A, \mathbf{Y}^B]$ is right-invariant, and by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]](2) it is $\mathbf{Y}^C$ with $C = [\mathbf{Y}^A, \mathbf{Y}^B]_e = [A, B]^R$.
>
> *A Lie bracket.* The map $A \mapsto \mathbf{Y}^A$ is linear and injective (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]](3)), and it carries $[\ ,\ ]^R$ to the bracket of vector fields. Hence bilinearity, antisymmetry and the Jacobi identity for $[\ ,\ ]^R$ follow from those of the bracket on $\mathfrak{X}(G)$ (Corollary [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]]). *(Filled in.)* For instance, for bilinearity in the first slot, with $a, a' \in \mathbb{R}$,
>
> $$
> \mathbf{Y}^{[aA + a'A', B]^R} = \big[a\mathbf{Y}^A + a'\mathbf{Y}^{A'}, \mathbf{Y}^B\big] = a\,\mathbf{Y}^{[A,B]^R} + a'\,\mathbf{Y}^{[A',B]^R} = \mathbf{Y}^{a[A,B]^R + a'[A',B]^R},
> $$
>
> and injectivity gives $[aA + a'A', B]^R = a[A,B]^R + a'[A',B]^R$; antisymmetry and Jacobi are the same three steps.

^pf-60-18

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-8|Def. §60.8]], [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]], [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]], [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]]

> [!theorem] Theorem §60.19: The Right Bracket Is the Negative of the Left Bracket
> Let $G$ be a Lie group, and $[\ ,\ ]$ the Lie bracket on $T_eG$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]]). For all $A, B \in T_eG$,
>
> $$
> [A, B]^R = -[A, B] .
> $$

^thm-60-19

> [!proof]+ Proof
> *(Assignment 6, Problem 2(b); the submitted solution.)* By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|§60.6]], $[\mathbf{X}^A, \mathbf{X}^B] = \mathbf{X}^{[A,B]}$ (both are left-invariant, Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-6|§60.6]], with the same value at $e$, Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]]). By Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]], $\mathbf{X}^A$ is $j$-related to $\mathbf{Y}^{-A}$ and $\mathbf{X}^B$ is $j$-related to $\mathbf{Y}^{-B}$, so by the naturality of the bracket (Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]])
>
> $$
> [\mathbf{X}^A, \mathbf{X}^B] = \mathbf{X}^{[A,B]} \text{ is $j$-related to } [\mathbf{Y}^{-A}, \mathbf{Y}^{-B}] .
> $$
>
> Since $\mathbf{Y}^{-A} = -\mathbf{Y}^A$ and $\mathbf{Y}^{-B} = -\mathbf{Y}^B$ (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]](3)), by bilinearity of the bracket and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-18|§60.18]],
>
> $$
> [\mathbf{Y}^{-A}, \mathbf{Y}^{-B}] = [-\mathbf{Y}^A, -\mathbf{Y}^B] = (-1)(-1)[\mathbf{Y}^A, \mathbf{Y}^B] = \mathbf{Y}^{[A,B]^R} .
> $$
>
> On the other hand, Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]] applied to $[A, B] \in T_eG$ shows that $\mathbf{X}^{[A,B]}$ is $j$-related to $\mathbf{Y}^{-[A,B]}$. So $\mathbf{X}^{[A,B]}$ is $j$-related to both $\mathbf{Y}^{[A,B]^R}$ and $\mathbf{Y}^{-[A,B]}$; that is, for every $p \in G$,
>
> $$
> \mathbf{Y}^{[A,B]^R}_{j(p)} = dj_p\,\mathbf{X}^{[A,B]}_p = \mathbf{Y}^{-[A,B]}_{j(p)} .
> $$
>
> Since $j$ is a bijection, every point of $G$ is of the form $j(p)$, so $\mathbf{Y}^{[A,B]^R} = \mathbf{Y}^{-[A,B]}$. Evaluating at $e$ and using $\mathbf{Y}^C_e = C$ (Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]](1)),
>
> $$
> [A, B]^R = -[A, B] .
> $$

^pf-60-19

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Def. §60.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-6|§60.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-9|§60.9]], [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]], [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-15|§60.15]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-18|§60.18]]

> [!proof]+ Second proof
> *(Not from the assignment.)* $j$ is a diffeomorphism, so pushing forward by it preserves brackets (Corollary [[§59 Related Vector Fields#^cor-59-4|§59.4]]). With $j_\ast\mathbf{X}^C = \mathbf{Y}^{-C}$ for every $C \in T_eG$ (Corollary [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]]) and $\mathbf{Y}^{-C} = -\mathbf{Y}^C$,
>
> $$
> \mathbf{Y}^{-[A,B]} = j_\ast\mathbf{X}^{[A,B]} = j_\ast[\mathbf{X}^A, \mathbf{X}^B] = [j_\ast\mathbf{X}^A, j_\ast\mathbf{X}^B] = [-\mathbf{Y}^A, -\mathbf{Y}^B] = [\mathbf{Y}^A, \mathbf{Y}^B] .
> $$
>
> Evaluating at $e$: $-[A, B] = [A, B]^R$.

^pf-60-19-2

*Uses:* [[§59 Related Vector Fields#^cor-59-4|§59.4]], [[§60 Lie Groups and Left-Invariant Vector Fields#^cor-60-17|§60.17]]

> [!theorem] Corollary §60.20: Abelian Lie Groups Have Zero Bracket
> If the Lie group $G$ is abelian, its Lie bracket on $T_eG$ is identically zero.

^cor-60-20

> [!proof]+ Proof
> *(Assignment 6, Problem 2(c), “use the result of part (b)”; the submitted solution.)* Suppose $G$ is abelian. For $g, k \in G$, $L_g(k) = gk = kg = R_g(k)$, so $L_g = R_g$. Hence for $A \in T_eG$ and $g \in G$,
>
> $$
> \mathbf{X}^A_g = d(L_g)_e(A) = d(R_g)_e(A) = \mathbf{Y}^A_g,
> $$
>
> so $\mathbf{X}^A = \mathbf{Y}^A$. Therefore, for $A, B \in T_eG$,
>
> $$
> [A, B]^R = [\mathbf{Y}^A, \mathbf{Y}^B]_e = [\mathbf{X}^A, \mathbf{X}^B]_e = [A, B].
> $$
>
> Combining with Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-19|§60.19]], $[A, B] = [A, B]^R = -[A, B]$, so $2[A, B] = 0$. Since $T_eG$ is a real vector space, $[A, B] = 0$ for all $A, B \in T_eG$.

^pf-60-20

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-19|§60.19]]

This agrees with Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-2|§60.2]], where the bracket of the additive group of a vector space was computed to vanish, and it applies as well to the torus $S^1 \times \cdots \times S^1$, a product of the abelian Lie group $S^1 = \mathrm{U}(1)$. *(Not from the assignment.)* The converse needs connectedness: $\mathrm{O}(2)$ is not abelian, but its tangent space at $I$ is that of $\mathrm{SO}(2) \cong S^1$, one-dimensional, so its bracket vanishes by antisymmetry. For connected groups the converse holds, a fact that needs the exponential map (Lee, Ch. 20).

> [!example] Example §60.3: Right-Invariant Fields on $\mathrm{GL}({n,\mathbb{R}})$
> On $G = \mathrm{GL}(n,\mathbb{R})$, with $T_gG = \operatorname{Mat}(n,\mathbb{R})$ as in Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]], the right-invariant extension of $A \in \operatorname{Mat}(n,\mathbb{R}) = T_IG$ is
>
> $$
> \mathbf{Y}^A_g = Ag ,
> $$
>
> and the left- and right-invariant extensions are related by the adjoint action (Proposition [[§25 The Geometric Tangent Space#^prop-25-6|§25.6]]): $\mathbf{X}^A_g = gA = (gAg^{-1})\,g = \mathbf{Y}^{gAg^{-1}}_g$. The right bracket is $[A, B]^R = BA - AB$.

^ex-60-3

> [!proof]+ Proof
> *(Not from the assignment.)* $R_g$ is the restriction to $G$ of the linear map $h \mapsto hg$ of $\operatorname{Mat}(n,\mathbb{R})$, so, exactly as for $L_g$ in the proof of Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]], $d(R_g)_h(v) = vg$; at $h = I$, $\mathbf{Y}^A_g = d(R_g)_I(A) = Ag$. Then $\mathbf{X}^A_g = gA = gAg^{-1}g = \mathbf{Y}^{gAg^{-1}}_g$. Finally $[A, B]^R = -[A, B] = -(AB - BA) = BA - AB$ by Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-19|§60.19]] and Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]]. As a check without the theorem: the fields $X \mapsto AX$ are the column-vector linear fields of Proposition [[§61 Lie Group Morphisms and Linear Groups#^prop-61-6|§61.6]], applied to each column of $X$, and their brackets carry the same sign $BA - AB$.

^pf-ex-60-3

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-19|§60.19]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-10|§60.10]], [[§61 Lie Group Morphisms and Linear Groups#^prop-61-6|§61.6]]
