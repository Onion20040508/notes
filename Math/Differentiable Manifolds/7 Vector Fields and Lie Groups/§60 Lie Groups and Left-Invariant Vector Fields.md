---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 60
tags: [differentiable-manifolds, math591]
---
← [[§59 Related Vector Fields]] · ↑ [[· 7 Vector Fields and Lie Groups]] · [[§61 Lie Group Morphisms and Linear Groups]] →

*Stage: symmetry — Groups that are manifolds, and the vector fields that respect the group: the start of Lie theory.*

*Lecture 16, last three minutes, to be continued. References: Lee Ch. 7 and Ch. 8. “Lie algebras and Lie groups are related, and in one direction the relationship is very nice: any Lie group has a Lie algebra associated to it.”*

> [!definition] Definition §60.1: Lie Group
> A **Lie group** is a [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological group]] $G$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Definition §11.1]]) together with a [[§17 Differentiable Structures#^def-17-9|smooth structure]], such that multiplication $G \times G \to G$, $(g, h) \mapsto gh$, and inversion $G \to G$, $g \mapsto g^{-1}$, are [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth maps]].
>
> *Lee: Ch. 7, Basic Definitions*

^def-60-1

> [!remark]- Connections
> - The physicists' version, closed subgroups of $\mathrm{GL}(n,\mathbb{C})$: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|QFT Def. §CB.1.3]].

For a topological group the two maps had to be continuous; “now we ask that they be smooth maps, because we have a manifold structure, so we can make sense of that.”

> [!theorem] Proposition §60.1: The Classical Groups Are Lie Groups
> $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$ and $\mathrm{SU}(2)$, with the smooth structures of [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]] and [[§48 SU(2) → SO(3)꞉ The Double Cover|§48]], are [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie groups]].
>
> *Lee: Examples 7.3, 7.27–7.30*

^prop-60-1

> [!proof]+ Proof
> *(Stated in Lecture 16 — “all the matrix groups that we have seen … are Lie groups”; filled in.)* By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]], for each group $G$ of the list it has to be shown that multiplication $G \times G \to G$ and inversion $G \to G$ are smooth; they are then continuous, so $G$ is also a topological group (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|§11.1]]).
>
> *The setting.* Each group $G$ is an open subset or a submanifold of a space of matrices $\operatorname{Mat}$, which is $\operatorname{Mat}(n,\mathbb{R}) = \mathbb{R}^{n^2}$ or $\operatorname{Mat}(n,\mathbb{C}) \cong \mathbb{R}^{2n^2}$ (real and imaginary parts of the entries) (Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]; for $\mathrm{SU}(2)$, Proposition [[§47 The Unit Quaternions and SU(2)#^prop-47-5|§47.5]]). The inclusion $\iota : G \hookrightarrow \operatorname{Mat}$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]]). And a smooth map into $\operatorname{Mat}$ that lands in $G$ is smooth into $G$: by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2) for a submanifold; for an open subset because its chart is the restriction of the linear chart of $\operatorname{Mat}$ (proof of Theorem [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]]), so the map has the same coordinate representations as a map into $G$ and as a map into $\operatorname{Mat}$.
>
> *Multiplication* is the composite of $\iota \times \iota : G \times G \to \operatorname{Mat} \times \operatorname{Mat}$, $(g, h) \mapsto (g, h)$, with matrix multiplication $\operatorname{Mat} \times \operatorname{Mat} \to \operatorname{Mat}$.
> - $\iota \times \iota$ is smooth since its components are: they are $\iota \circ \pi_1$ and $\iota \circ \pi_2$, smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]] and Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], and a map into the Euclidean space $\operatorname{Mat} \times \operatorname{Mat}$ is smooth when its components are.
> - Matrix multiplication is smooth: the entries $(AB)_{ij} = \sum_k A_{ik} B_{kj}$ are polynomials in the real coordinates (in the complex case, the real and imaginary parts of $\sum_k A_{ik} B_{kj}$ are polynomials in the real and imaginary parts of the entries).
>
> So the composite $(g, h) \mapsto gh$ is smooth into $\operatorname{Mat}$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). It lands in $G$, because $G$ is a group under matrix multiplication; so it is smooth into $G$, by the last sentence of the setting.
>
> *Inversion* is the restriction of a smooth map on the open set of invertible matrices — $g \mapsto \operatorname{adj}(g)/\det g$ by the cofactor formula, a rational map with nonvanishing denominator — landing in $G$, hence smooth into $G$ in the same way. In detail: the set of invertible matrices in $\operatorname{Mat}$ is $\det^{-1}$ of the nonzero numbers, open since $\det$ is continuous. On it, the entries of $\operatorname{adj}(g)$ and $\det g$ are polynomials in the entries of $g$, and $\det g \ne 0$, so $g \mapsto \operatorname{adj}(g)/\det g = g^{-1}$ is smooth; in the complex case, dividing by $\det g$ is multiplying by $\overline{\det g}/|\det g|^2$, again rational in the real coordinates with nonvanishing denominator $|\det g|^2$. Every $G$ of the list consists of invertible matrices, so $g \mapsto g^{-1}$ on $G$ is this map composed with $\iota$, smooth into $\operatorname{Mat}$; it lands in $G$, because $G$ is closed under inverses; so it is smooth into $G$. (For $\mathrm{O}(n)$ and $\mathrm{U}(n)$ it is even linear: $g \mapsto g^{\mathsf T}$, $g \mapsto g^{\ast}$.)

^pf-60-1

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§47 The Unit Quaternions and SU(2)#^prop-47-5|§47.5]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|235 Thm. §27.2]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Def. §11.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§48 SU(2) → SO(3)꞉ The Double Cover#^thm-48-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§58 Lie Bracket and Lie Algebra#^ex-58-3|Ex. §58.3]]; and Lie groups in [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-1|§60.1]].

The unit quaternions $S^3$ are a Lie group as well ([[§47 The Unit Quaternions and SU(2)#^prop-47-4|Proposition §47.4]]), isomorphic to $\mathrm{SU}(2)$ ([[§47 The Unit Quaternions and SU(2)#^prop-47-5|Proposition §47.5]]).

> [!definition] Definition §60.2: Left Translation
> For $g$ in a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] $G$, **left translation** by $g$ is $L_g : G \to G$, $L_g(h) = gh$.
>
> *Lee: Ch. 7, Basic Definitions*

^def-60-2

> [!theorem] Lemma §60.2: Left Translations Are Diffeomorphisms
> $L_g$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], with inverse $L_{g^{-1}}$.
>
> *Lee: Ch. 7, Basic Definitions*

^lem-60-2

> [!proof]+ Proof
> *(Filled in, as for topological groups in Lemma [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]].)* By Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]], it has to be shown that $L_g$ is a smooth bijection with smooth inverse, and that the inverse is $L_{g^{-1}}$.
>
> *Smooth.* $L_g$ is smooth as the composite of $h \mapsto (g, h)$ with multiplication: $L_g(h) = gh = \mu\big(\iota^{g}(h)\big)$, where $\iota^{g} : G \to G \times G$, $h \mapsto (g, h)$, is the slice inclusion of Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]] (with $M_1 = M_2 = G$ and $p_1 = g$), smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], and $\mu : G \times G \to G$ is multiplication, smooth by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]. So $L_g = \mu \circ \iota^{g}$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). The same holds for every element of $G$, in particular for $g^{-1}$: $L_{g^{-1}}$ is smooth.
>
> *Inverse.* For $h \in G$, by associativity of the group product,
>
> $$
> L_g\big(L_{g^{-1}}(h)\big) = g\,(g^{-1}h) = (gg^{-1})\,h = h, \qquad L_{g^{-1}}\big(L_g(h)\big) = g^{-1}(gh) = (g^{-1}g)\,h = h .
> $$
>
> So $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$: $L_g$ is a bijection with inverse $L_{g^{-1}}$, and both are smooth, so $L_g$ is a diffeomorphism.

^pf-60-2

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|Def. §60.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]]

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

Left invariance in one line: “using [left translations], you can push vectors of the field to get other vectors; and whenever you do that, you get the corresponding vector of the field.” The value at one point determines the field everywhere: taking $h = e$, $\mathbf{X}_g = (L_g)_{\ast e}\, \mathbf{X}_e$. This is the [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|left translation]] of tangent spaces from the discussion of moving the base point ([[§48 SU(2) → SO(3)꞉ The Double Cover#^lem-48-3|Lemma §48.3]]), applied to a whole field.

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

*Status.* Defined in Lecture 16 — “this is going to be quickly identified with the tangent space at the identity. But originally we think of them as a certain very special type of vector field, because that's where the Lie bracket comes from.” For $\mathrm{GL}(n,\mathbb{R})$ the identification is $\mathbf{X}^A \mapsto A$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). The two facts announced then were proved in Lecture 17, in [[§60 Lie Groups and Left-Invariant Vector Fields|§60]] below: $\mathfrak{g}$ is closed under the bracket, and $\mathbf{X} \mapsto \mathbf{X}_e$ is an isomorphism onto $T_eG$ (its last step, smoothness, completed in Lecture 18).

## The Lie Algebra and the Tangent Space at the Identity

*Lecture 17. “Back to Lie groups.” With the language of [[§59 Related Vector Fields#^def-59-2|related fields]], “we can rephrase some of the definitions.”*

> [!theorem] Lemma §60.3: Left-Invariance as Relatedness
> A vector field $\mathbf{X} \in \mathfrak{X}(G)$ is [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|left-invariant]] ([[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Definition §60.3]]) if and only if, for every $g \in G$, $\mathbf{X}$ is *$L_g$-related to itself* ([[§59 Related Vector Fields#^def-59-2|Definition §59.2]] with $F = L_g$ and $\mathbf{Y} = \mathbf{X}$).

^lem-60-3

> [!proof]+ Proof
> *(Lecture 17, a rephrasing of the definition: “we can rephrase some of the definitions”.)* Being $L_g$-related to itself means $d(L_g)_h(\mathbf{X}_h) = \mathbf{X}_{L_g(h)} = \mathbf{X}_{gh}$ for every $h \in G$, which is the condition of [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Definition §60.3]] for this $g$.

^pf-60-3

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-2|Def. §60.2]]

> [!remark] Remark: Why Left?
> Lecture 17 abbreviates “left-invariant” to l.i. “And you can ask why left. What's wrong with right? There's nothing wrong with right. You have to choose … and this is the universal choice.” Right-invariant fields, $R_g$-related to themselves for $R_g(h) = hg$, give an equivalent theory; the one place the choice shows is the sign of the bracket, at the end of this subsection ([[§60 Lie Groups and Left-Invariant Vector Fields#^rem-60-2|Remark: Left or Right]]).

^rem-60-1

> [!theorem] Corollary §60.4: $\mathfrak{g}$ Is a Lie Subalgebra of $\mathfrak{X}(G)$
> If $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ then $[\mathbf{X}, \mathbf{Y}] \in \mathfrak{g}$. So $\mathfrak{g}$, a linear subspace of $\mathfrak{X}(G)$, is a [[§58 Lie Bracket and Lie Algebra#^def-58-2|Lie algebra]] under the [[§58 Lie Bracket and Lie Algebra#^def-58-1|bracket of vector fields]].
>
> *Lee: Proposition 8.33*

^cor-60-4

> [!proof]+ Proof
> *(Lecture 17: “the big observation, which is actually a consequence of” Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]].)* *Closed under the bracket.* Let $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ and fix $g \in G$. By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-3|§60.3]], $\mathbf{X}$ is $L_g$-related to $\mathbf{X}$ and $\mathbf{Y}$ to $\mathbf{Y}$. So by Proposition [[§59 Related Vector Fields#^prop-59-3|§59.3]] with $F = L_g$, $\mathbf{X}_1 = \mathbf{Y}_1 = \mathbf{X}$ and $\mathbf{X}_2 = \mathbf{Y}_2 = \mathbf{Y}$, $[\mathbf{X}, \mathbf{Y}]$ is $L_g$-related to $[\mathbf{X}, \mathbf{Y}]$. This holds for every $g$, and by Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-3|§60.3]] again (in the converse direction) this for every $g$ is left-invariance: $[\mathbf{X}, \mathbf{Y}] \in \mathfrak{g}$.
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

^pf-60-4

*Uses:* [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-3|§60.3]], [[§59 Related Vector Fields#^def-59-2|Def. §59.2]], [[§59 Related Vector Fields#^prop-59-3|§59.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|Def. §60.4]], [[§58 Lie Bracket and Lie Algebra#^cor-58-5|§58.5]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§56 Vector Fields#^def-56-2|Def. §56.2]], [[§58 Lie Bracket and Lie Algebra#^def-58-2|Def. §58.2]]

“It's a Lie subalgebra of the infinite-dimensional algebra of all vector fields on $G$.” Vector fields can be added and scaled, so $\mathfrak{X}(G)$ is a [[§56 Vector Fields#^def-56-2|vector space]] (“in fact, it's an algebra over the smooth functions, but I want to think of it as a vector space”). “At this point, maybe it's not clear what [$\mathfrak{g}$] is. It could be, I don't know, still infinite-dimensional, or something, or empty.” [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|The theorem]] below settles it. Its proof rests on a construction, made in Lecture 17 and finished in Lecture 18, which comes first.

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

“Just as with vector fields” on a vector space (Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]]), there is a unique left translation carrying $e$ to $g$, and $\mathbf{X}^v_g$ is $v$ carried along it.

> [!theorem] Lemma §60.5: The Left-Invariant Extension Is Left-Invariant
> Let $G$ be a Lie group with identity $e$.
>
> 1. For $v \in T_eG$, $\mathbf{X}^v_g \in T_gG$ for every $g \in G$, and $\mathbf{X}^v_e = v$.
> 2. For $v \in T_eG$, $\mathbf{X}^v$ satisfies the identity of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]: $d(L_g)_h\big(\mathbf{X}^v_h\big) = \mathbf{X}^v_{gh}$ for all $g, h \in G$.
> 3. Every $\mathbf{X} \in \mathfrak{g}$ is the left-invariant extension of its value at $e$: $\mathbf{X}_g = d(L_g)_e(\mathbf{X}_e)$ for every $g \in G$, that is, $\mathbf{X} = \mathbf{X}^{\mathbf{X}_e}$.
>
> *Lee: proof of Theorem 8.37*

^lem-60-5

> [!proof]+ Proof
> *(Lecture 17, steps of the proof that $\mathfrak{g}$ is $T_eG$; (2) was left to check — “not a bad thing to do” — and done in the review at the start of Lecture 19.)*
>
> *(1)* $L_g$ maps $e$ to $g$, so $d(L_g)_e : T_eG \to T_{L_g(e)}G = T_{ge}G = T_gG$, and $\mathbf{X}^v_g = d(L_g)_e(v)$ lies in $T_gG$. And $L_e = \mathrm{id}_G$ (as $eh = h$), so $\mathbf{X}^v_e = (\mathrm{id}_G)_{\ast e}(v) = v$ by Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]].
>
> *(2)* *(Lecture 19.)* Fix $h, g \in G$. “If I want to end up at $g$, I have to start at $h^{-1}g$”: $L_h$ maps $h^{-1}g$ to $g$. By Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] and the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]),
>
> $$
> d(L_h)_{h^{-1}g}\big(\mathbf{X}^v_{h^{-1}g}\big) = d(L_h)_{h^{-1}g}\, d(L_{h^{-1}g})_e(v) = d\big(L_h \circ L_{h^{-1}g}\big)_e(v) = d(L_g)_e(v) = \mathbf{X}^v_g ,
> $$
>
> because $L_h \circ L_{h^{-1}g} = L_g$: “you multiply on the left by $h^{-1}g$, and then you multiply on the left by $h$, so the $h$ and the $h^{-1}$ cancel.” Writing $k = h^{-1}g$, this says $d(L_h)_k(\mathbf{X}^v_k) = \mathbf{X}^v_{hk}$ for all $h, k \in G$, the identity of Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]].
>
> *(3)* Let $\mathbf{X} \in \mathfrak{g}$ and $g \in G$. Left-invariance (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]) with $h = e$ reads $d(L_g)_e(\mathbf{X}_e) = \mathbf{X}_{ge} = \mathbf{X}_g$, and by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] with $v = \mathbf{X}_e$ the left side is $\mathbf{X}^{\mathbf{X}_e}_g$.

^pf-60-5

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]]

> [!theorem] Proposition §60.6: The Left-Invariant Extension Is Smooth
> Let $G$ be a Lie group with identity $e$ and $v \in T_eG$. For $f \in C^\infty(G)$ let $\varphi : G \times G \to \mathbb{R}$, $\varphi(g, x) = f(gx)$. Then $\varphi$ is smooth, and
>
> $$
> \mathbf{X}^v f = \partial_v\varphi \in C^\infty(G),
> $$
>
> the partial derivative of $\varphi$ in the second variable in the direction $v$ (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]). Hence $\mathbf{X}^v$ is smooth: $\mathbf{X}^v \in \mathfrak{g}$, a left-invariant vector field with $\mathbf{X}^v_e = v$.
>
> *Lee: proof of Theorem 8.37*

^prop-60-6

> [!proof]+ Proof
> *(Lecture 18, completing the proof of Lecture 17.)* Lecture 17 stopped here: “The incompleteness in the proof is that we want to show that this is $C^\infty$. It's an important technical point … and we don't have the tools to do that at this point.” Lecture 18 finished it — “in fact, we can just use this partial derivative construction” (Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]]). So far $\mathbf{X}^v$ is a left-invariant *rough* field (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](1) and (2)), Lee's term for a section not yet known to be smooth: “the piece of the construction that has not been justified is that this thing is smooth.”
>
> *The claim.* It suffices to show that for every $f \in C^\infty(G)$ the function $\mathbf{X}^v f : g \mapsto \mathbf{X}^v_g[f]$ is smooth. “This function is still well defined regardless of whether $\mathbf{X}^v$ is smooth or not … because I have a vector at every point, and I can let that act on any function.” The lecture's proof of the claim: in local coordinates $(x^1, \ldots, x^m)$, $m = \dim G$, there is still a pointwise expansion $\mathbf{X}^v = \sum_j a^j\, \partial/\partial x^j$, and $\mathbf{X}^v$ is smooth exactly when the $a^j$ are (Proposition [[§56 Vector Fields#^prop-56-1|§56.1]]); “but the $a^j$ are precisely the action of $\mathbf{X}^v$ on the coordinate $x^j$.” This is Lemma [[§56 Vector Fields#^lem-56-8|§56.8]], whose proof also handles the point that $x^j$ is defined only on the chart, by extending it with a bump function.
>
> *The construction.* Let $f \in C^\infty(G)$ and $g \in G$. By the definition of $\mathbf{X}^v$ and of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]),
>
> $$
> (\mathbf{X}^v f)(g) = d(L_g)_e(v)[f] = v[f \circ L_g] \in \mathbb{R},
> $$
>
> and “we want to show that as a function of $g$, this is smooth.” Construct “a trick that occurred to me”
>
> $$
> \varphi : G \times G \xrightarrow{\ \text{multiplication}\ } G \xrightarrow{\ f\ } \mathbb{R}, \qquad \varphi(g, x) = f(gx) = (f \circ L_g)(x).
> $$
>
> It is smooth, as the composite of the multiplication, smooth by Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]], with $f$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). Fixing $g$ in the first variable, $f \circ L_g = \varphi(g, \cdot)$, so by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|§31.3]], in the second variable with $w = v \in T_eG$,
>
> $$
> (\mathbf{X}^v f)(g) = v\big[\varphi(g, \cdot)\big] = \partial_v\varphi(g) .
> $$
>
> “We're letting $v$ act on the second variable, and so that means that it is smooth”: $\partial_v\varphi \in C^\infty(G)$ by Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-7|§31.7]](3). By the claim, $\mathbf{X}^v$ is smooth. It is left-invariant (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](2)), so $\mathbf{X}^v \in \mathfrak{g}$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|§60.4]]), and $\mathbf{X}^v_e = v$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](1)).

^pf-60-6

*Uses:* [[§31 Tangent Vectors as Velocities of Curves#^def-31-3|Def. §31.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§56 Vector Fields#^lem-56-8|§56.8]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§31 Tangent Vectors as Velocities of Curves#^prop-31-7|§31.7]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-4|Def. §60.4]]

> [!theorem] Theorem §60.7: The Lie Algebra Is the Tangent Space at the Identity
> Let $G$ be a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] with identity $e$. The evaluation map
>
> $$
> \mathrm{ev} : \mathfrak{g} \to T_eG, \qquad \mathbf{X} \mapsto \mathbf{X}_e ,
> $$
>
> is a linear isomorphism. In particular $\dim \mathfrak{g} = \dim G$.
>
> *Lee: Theorem 8.37*

^thm-60-7

> [!proof]+ Proof
> *(Lecture 17 — “it'll be an incomplete proof … there is one detail that we're not prepared to prove” — completed in Lecture 18. The lecture's steps.)* $\mathrm{ev}$ is linear: for $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ and $a, b \in \mathbb{R}$, $\mathrm{ev}(a\mathbf{X} + b\mathbf{Y}) = (a\mathbf{X} + b\mathbf{Y})_e = a\,\mathbf{X}_e + b\,\mathbf{Y}_e$ by Definition [[§56 Vector Fields#^def-56-2|§56.2]]. It remains to show that $\mathrm{ev}$ is injective and surjective.
>
> *The basic idea.* For $g \in G$, $L_g$ maps $e$ to $g$, so $d(L_g)_e : T_eG \to T_gG$, and for $\mathbf{X} \in \mathfrak{g}$, left-invariance (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|§60.3]]) with $h = e$ reads
>
> $$
> d(L_g)_e(\mathbf{X}_e) = \mathbf{X}_g ;
> $$
>
> more generally $d(L_g)_h(\mathbf{X}_h) = \mathbf{X}_{gh}$ for all $h$. “There's only one choice really”: $\mathbf{X}$ is the left-invariant extension of $\mathbf{X}_e$ (Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](3)).
>
> *Injective.* By the basic idea, $\mathbf{X}$ is determined by its value at $e$. So $\mathbf{X}_e = 0$ forces $\mathbf{X}_g = d(L_g)_e(0) = 0$ for all $g$, since $d(L_g)_e$ is linear (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]]). So the kernel of the linear map $\mathrm{ev}$ is $\{\mathbf{0}\}$, and $\mathrm{ev}$ is injective.
>
> *Surjective.* Start with $v \in T_eG$; we want a left-invariant $\mathbf{X}$ with $\mathbf{X}_e = v$. The basic idea says there is no choice: we must take the left-invariant extension of $v$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]),
>
> $$
> \mathbf{X}^v_g = d(L_g)_e(v), \qquad g \in G .
> $$
>
> By Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](1) and (2), which are Lecture 17's steps, $\mathbf{X}^v$ is a rough vector field, a tangent vector at every point, with $\mathbf{X}^v_e = v$ and satisfying the left-invariance identity. *Smooth.* This is where Lecture 17 stopped; Lecture 18 finished it, and by Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]] $\mathbf{X}^v$ is smooth, through $\mathbf{X}^v f = \partial_v\varphi$ for $\varphi(g, x) = f(gx)$. So $\mathbf{X}^v \in \mathfrak{g}$ and $\mathrm{ev}(\mathbf{X}^v) = v$. “So this finishes completely the proof of that theorem.”
>
> Finally, a linear isomorphism preserves dimension, so $\dim \mathfrak{g} = \dim T_eG = \dim G$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]).

^pf-60-7

*Uses:* [[§56 Vector Fields#^def-56-2|Def. §56.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|Def. §60.3]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-5|§28.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]

> [!remark]- Connections
> - The matrix-group version, with $\mathfrak g$ defined through the exponential and identified with $T_{\mathbb 1}G$ and with the left-invariant fields: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|QFT Theorem §CB.1.16]].

![[m591-50-1.svg]]
*The left-invariant field $\mathbf{X}^v$: the vector $v \in T_eG$ carried to $g$ by the differential of the left translation $L_g$.*

**Comparison with Lee.** Lee's proof (Theorem 8.37) differentiates $f(g\,\gamma(t))$ along a curve $\gamma$ adapted to $v$, which is Proposition [[§31 Tangent Vectors as Velocities of Curves#^prop-31-7|§31.7]](1) applied to the function $\varphi(g, x) = f(gx)$ of Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]]: $(\mathbf{X}^v f)(g) = \frac{d}{dt}\big|_{t=0} \varphi(g, \gamma(t))$. The course packages that step once and for all as the partial derivative $\partial_v\varphi$.

On the proof as a whole, Uribe passed on a remark a student made in office hours: “this subject is not so much about solving problems … it's about constructing an architecture inside one's brain.”

> [!example] Example §60.2: The Additive Group of a Vector Space
> Let $V$ be a finite-dimensional vector space, a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] under addition with identity $0$, so that $L_p = \tau_p$ is translation by $p$. Its [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-3|left-invariant vector fields]] are the constant fields $\mathbf{X}^v : p \mapsto D_v|_p$, $v \in V$, and all their [[§58 Lie Bracket and Lie Algebra#^def-58-1|brackets]] vanish: $\mathfrak{g} \cong V$ with the zero bracket.

^ex-60-2

> [!proof]+ Proof
> *(Not from lecture; filled in, after the remark in Lecture 17 that the translations of a vector space give “a left-invariant vector field”.)* *$V$ is a Lie group.* In linear coordinates (Definition [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|§22.4]]), addition $(p, q) \mapsto p + q$ and inversion $p \mapsto -p$ are linear, hence smooth; so $V$ is a Lie group (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|§60.1]]), with $L_p(q) = p + q = \tau_p(q)$.
>
> *The left-invariant fields.* By Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], every element of $T_0V$ is $D_v|_0$ for a unique $v \in V$. By Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|§60.7]] and Lemma [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]](3), the left-invariant fields are exactly the left-invariant extensions $\mathbf{X}^w$, $w \in T_0V$ (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]]), with $\mathbf{X}^w_p = d(L_p)_0(w)$. For $w = D_v|_0$, Proposition [[§30 The Differential in Coordinates#^prop-30-7|§30.7]](2) gives
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

*Uses:* [[§22 The Differential of a Map Between Vector Spaces#^def-22-4|Def. §22.4]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Def. §60.1]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|§60.7]], [[§60 Lie Groups and Left-Invariant Vector Fields#^lem-60-5|§60.5]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|Def. §60.5]], [[§30 The Differential in Coordinates#^prop-30-7|§30.7]], [[§56 Vector Fields#^prop-56-1|§56.1]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]]

> [!definition] Definition §60.6: The Lie Bracket on $T_eG$
> Let $G$ be a [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-1|Lie group]] and, for $v \in T_eG$, let $\mathbf{X}^v \in \mathfrak{g}$ be its left-invariant extension (Definition [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-5|§60.5]] and Proposition [[§60 Lie Groups and Left-Invariant Vector Fields#^prop-60-6|§60.6]]), the left-invariant field with $\mathbf{X}^v_e = v$, unique by Theorem [[§60 Lie Groups and Left-Invariant Vector Fields#^thm-60-7|§60.7]]. The **Lie bracket** on $T_eG$ is
>
> $$
> [v, w] = \big[\mathbf{X}^v, \mathbf{X}^w\big]_e , \qquad v, w \in T_eG .
> $$

^def-60-6

By construction $\mathrm{ev}$ is then an isomorphism of [[§58 Lie Bracket and Lie Algebra#^def-58-2|Lie algebras]]: $T_eG$ inherits the bracket that makes it one. The question is what this bracket is.

> [!theorem] Theorem §60.8: The Lie Algebra of $\mathrm{GL}(d,\mathbb{R})$
> Let $G = \mathrm{GL}(d, \mathbb{R})$, the $d \times d$ invertible matrices, an open subset of $\operatorname{Mat}(d, \mathbb{R}) \cong \mathbb{R}^{d^2}$, so that $T_IG = \operatorname{Mat}(d,\mathbb{R})$. The Lie bracket on $T_IG$ ([[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Definition §60.6]]) is the matrix commutator
>
> $$
> [A, B] = AB - BA .
> $$

^thm-60-8

> [!proof]+ Proof
> *(Lecture 19 — “we have run out of diagrams to chase. We actually have to compute something.” The lecture's computation, with the index bookkeeping written out. Lecture 19 proved this together with Theorem [[§61 Lie Group Morphisms and Linear Groups#^thm-61-3|§61.3]], which reduces every linear group to this case.)*
>
> *Coordinates.* Write $A = (a^i_j)$, with $i$ the row index and $j$ the column index, and call a general group element $X = (x^i_j) \in \mathrm{GL}(d, \mathbb{R})$ rather than $g$, “because I want to think of it as a variable.” Written out,
>
> $$
> A = \begin{pmatrix} a^1_1 & \cdots & a^1_d \\ \vdots & \ddots & \vdots \\ a^d_1 & \cdots & a^d_d \end{pmatrix},
> \qquad
> X = \begin{pmatrix} x^1_1 & \cdots & x^1_d \\ \vdots & \ddots & \vdots \\ x^d_1 & \cdots & x^d_d \end{pmatrix},
> $$
>
> the upper index numbering the rows and the lower index the columns. The entries $x^i_j$ are the standard coordinates of $\operatorname{Mat}(d,\mathbb{R}) \cong \mathbb{R}^{d^2}$, “indexed in a funny way”, and a tangent vector $V = (V^i_j) \in \operatorname{Mat}(d, \mathbb{R}) = T_X\mathrm{GL}(d,\mathbb{R})$ is $\sum_{i,j} V^i_j\, \partial/\partial x^i_j|_X$ (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]). The basic computation is
>
> $$
> \frac{\partial}{\partial x^i_j}\big(x^l_n\big) = \delta_{il}\, \delta_{jn} ,
> $$
>
> “one or zero depending on whether I'm differentiating the same coordinate as I'm taking the partial.”
>
> *The left-invariant field.* $\mathbf{X}^A_X = d(L_X)_I(A)$, and $L_X : \mathbb{R}^{d^2} \to \mathbb{R}^{d^2}$, $Y \mapsto XY$, is linear, “so it's its own differential” (Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]): $\mathbf{X}^A_X = XA$ (Example [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|§60.1]]). The $(i,j)$ entry of $XA$ is $\sum_k x^i_k a^k_j$, so
>
> $$
> \mathbf{X}^A = \sum_{i,j} \Big( \sum_k x^i_k\, a^k_j \Big) \frac{\partial}{\partial x^i_j}, \qquad
> \mathbf{X}^B = \sum_{l,n} \Big( \sum_m x^l_m\, b^m_n \Big) \frac{\partial}{\partial x^l_n},
> $$
>
> with independent indices for the second field, “because these are independent.” The $a^k_j$ and $b^m_n$ are constants; the $x$'s are functions. (A student asked why the sums can come out of the commutator: “because the commutator is bilinear … over constants, … but you cannot pull the $x$'s out, because those are functions.”)
>
> *The bracket.* “We know that we don't care about the second derivatives because they're going to go away” (Lemma [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]]): by Proposition [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], the coefficient of $\partial/\partial x^l_n$ in $[\mathbf{X}^A, \mathbf{X}^B]$ is $\mathbf{X}^A$ applied to the coefficient of $\mathbf{X}^B$, minus the same with $A$ and $B$ exchanged. Applying the basic computation,
>
> $$
> \mathbf{X}^A\Big( \sum_m x^l_m\, b^m_n \Big) = \sum_{i,j,k,m} x^i_k\, a^k_j\, b^m_n\, \delta_{il}\, \delta_{jm} = \sum_{k} x^l_k \Big( \sum_j a^k_j\, b^j_n \Big) = \sum_k x^l_k\, (AB)^k_n :
> $$
>
> setting $i = l$ and $m = j$ is all that happens, and then “these two guys together … it's an entry of a matrix”, the $(k, n)$ entry of $AB$. So
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

^pf-60-8

*Uses:* [[§61 Lie Group Morphisms and Linear Groups#^thm-61-3|§61.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§60 Lie Groups and Left-Invariant Vector Fields#^ex-60-1|Ex. §60.1]], [[§58 Lie Bracket and Lie Algebra#^lem-58-1|§58.1]], [[§58 Lie Bracket and Lie Algebra#^prop-58-2|§58.2]], [[§60 Lie Groups and Left-Invariant Vector Fields#^def-60-6|Def. §60.6]]

“You have to think about this on your own … think about indices and so on. But this is essentially the reason.” Coordinate-free, the computation says: a field $X \mapsto XC$ on an open subset of $\operatorname{Mat}(d,\mathbb{R})$ is linear in $X$, and the bracket of the linear fields $X \mapsto XA$ and $X \mapsto XB$ is the linear field $X \mapsto X(AB - BA)$.

> [!remark]- Connections
> - The commutator Lie algebra of matrices: [[§58 Lie Bracket and Lie Algebra#^ex-58-2|Ex. §58.2]].
> - For matrix Lie groups the physics notes prove the answer: the bracket of left-invariant fields becomes $XY - YX$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|QFT Theorem §CB.1.16]], part 3), and $\mathfrak g$ is closed under it ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|QFT Theorem §CB.1.12]]).

> [!remark] Remark: Left or Right: The Sign of the Bracket
> “This is the case because we use left-invariant fields. If we use right-invariant fields, we would have minus that.” Why left, then? An aside: “Did you ever think what the world would look like if, instead of writing $f(x)$ … we would have written $(x)f$? … Imagine composing functions with that rule. … Everything works much better if you write $(x)f$”: in that notation, composites read in the order the maps are applied.

^rem-60-2

**Transcription note (Lecture 17).** Page 46 of the handwritten notes says the construction gives “$\mathbf{X} : M \to TM$”; the manifold is the group, $\mathbf{X} : G \to TG$.
