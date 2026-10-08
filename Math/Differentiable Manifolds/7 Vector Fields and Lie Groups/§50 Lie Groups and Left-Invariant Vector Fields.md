---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 50
tags: [differentiable-manifolds, math591]
---
← [[§49 Lie Bracket and Lie Algebra]] · ↑ [[· 7 Vector Fields and Lie Groups]]

*Stage: symmetry — Groups that are manifolds, and the vector fields that respect the group: the start of Lie theory.*

*Lecture 16, last three minutes, to be continued. References: Lee Ch. 7 and Ch. 8. “Lie algebras and Lie groups are related, and in one direction the relationship is very nice: any Lie group has a Lie algebra associated to it.”*

> [!definition] Definition §50.1: Lie Group
> A **Lie group** is a [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological group]] $G$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Definition §11.1]]) together with a [[§17 Differentiable Structures#^def-17-9|smooth structure]], such that multiplication $G \times G \to G$, $(g, h) \mapsto gh$, and inversion $G \to G$, $g \mapsto g^{-1}$, are [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth maps]].
>
> *Lee: Ch. 7, Basic Definitions*

^def-50-1

> [!remark]- Connections
> - The physicists' version, closed subgroups of $\mathrm{GL}(n,\mathbb{C})$: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|QFT Def. §CB.1.1]].

For a topological group the two maps had to be continuous; “now we ask that they be smooth maps, because we have a manifold structure, so we can make sense of that.”

> [!theorem] Proposition §50.1: The Classical Groups Are Lie Groups
> $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$ and $\mathrm{SU}(2)$, with the smooth structures of [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]] and [[§42 SU(2) → SO(3)꞉ The Double Cover|§42]], are [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|Lie groups]].
>
> *Lee: Examples 7.3, 7.27–7.30*

^prop-50-1

> [!proof]+ Proof
> *(Stated in Lecture 16 — “all the matrix groups that we have seen … are Lie groups”; filled in.)* Each group $G$ is an open subset or a submanifold of a space of matrices $\operatorname{Mat}$ ([[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]]; for $\mathrm{SU}(2)$, [[§41 The Unit Quaternions and SU(2)#^prop-41-5|Proposition §41.5]]), with $\iota : G \hookrightarrow \operatorname{Mat}$ smooth ([[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3]]). *Multiplication* is the composite of $\iota \times \iota : G \times G \to \operatorname{Mat} \times \operatorname{Mat}$, smooth since its components are, with matrix multiplication, whose entries are polynomials in the real coordinates; it lands in $G$, so it is smooth into $G$ ([[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3]](2)). *Inversion* is the restriction of a smooth map on the open set of invertible matrices — $g \mapsto \operatorname{adj}(g)/\det g$ by the [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|cofactor formula]], a rational map with nonvanishing denominator — landing in $G$, hence smooth into $G$ in the same way. (For $\mathrm{O}(n)$ and $\mathrm{U}(n)$ it is even linear: $g \mapsto g^{\mathsf T}$, $g \mapsto g^{\ast}$.)

^pf-50-1

*Uses:* [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|Def. §50.1]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§41 The Unit Quaternions and SU(2)#^prop-41-5|§41.5]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|235 Thm. §27.2]]

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§49 Lie Bracket and Lie Algebra#^ex-49-3|Ex. §49.3]]; and Lie groups in [[§50 Lie Groups and Left-Invariant Vector Fields#^prop-50-1|§50.1]].

The unit quaternions $S^3$ are a Lie group as well ([[§41 The Unit Quaternions and SU(2)#^prop-41-4|Proposition §41.4]]), isomorphic to $\mathrm{SU}(2)$ ([[§41 The Unit Quaternions and SU(2)#^prop-41-5|Proposition §41.5]]).

> [!definition] Definition §50.2: Left Translation
> For $g$ in a [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|Lie group]] $G$, **left translation** by $g$ is $L_g : G \to G$, $L_g(h) = gh$.
>
> *Lee: Ch. 7, Basic Definitions*

^def-50-2

> [!theorem] Lemma §50.2: Left Translations Are Diffeomorphisms
> $L_g$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], with inverse $L_{g^{-1}}$.
>
> *Lee: Ch. 7, Basic Definitions*

^lem-50-2

> [!proof]+ Proof
> *(Filled in, as for [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological groups]] in [[§13 Group Actions and Orbit Spaces#^lem-13-2|Lemma §13.2]].)* $L_g$ is smooth as the composite of $h \mapsto (g, h)$ with multiplication, and $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$.

^pf-50-2

*Uses:* [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|Def. §50.1]], [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-2|Def. §50.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]]

> [!definition] Definition §50.3: Left-Invariant Vector Field
> A [[§48 Vector Fields#^def-48-1|vector field]] $\mathbf{X} \in \mathfrak{X}(G)$ is **left-invariant** if for all $g, h \in G$
>
> $$
> (L_g)_{*h}\, \mathbf{X}_h = \mathbf{X}_{gh} .
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-50-3

![[m591-49-1.svg]]
*Left invariance as a diagram: the differential $(L_g)_{\ast h}$ of [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-2|left translation]] carries the value $\mathbf{X}_h$ of the field at $h$ to its value $\mathbf{X}_{gh}$ at $gh$.*

Left invariance in one line: “using [left translations], you can push vectors of the field to get other vectors; and whenever you do that, you get the corresponding vector of the field.” The value at one point determines the field everywhere: taking $h = e$, $\mathbf{X}_g = (L_g)_{\ast e}\, \mathbf{X}_e$. This is the [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-2|left translation]] of tangent spaces from the discussion of moving the base point ([[§42 SU(2) → SO(3)꞉ The Double Cover#^lem-42-3|Lemma §42.3]]), applied to a whole field.

> [!example] Example §50.1: Left-Invariant Fields on $\mathrm{GL}(n,\mathbb{R})$
> On $G = \mathrm{GL}(n,\mathbb{R})$, open in $\operatorname{Mat}(n,\mathbb{R})$, so that $T_gG = \operatorname{Mat}(n,\mathbb{R})$, the [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-3|left-invariant vector fields]] are exactly
>
> $$
> \mathbf{X}^A_g = gA, \qquad A \in \operatorname{Mat}(n,\mathbb{R}) = T_IG .
> $$

^ex-50-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $L_g$ is the restriction of the linear map $h \mapsto gh$, so its [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|differential]] at every point is that same linear map: $(L_g)_{\ast h}(v) = gv$. Left invariance therefore reads $g\,\mathbf{X}_h = \mathbf{X}_{gh}$ for all $g, h$. Taking $h = I$ gives $\mathbf{X}_g = g\,\mathbf{X}_I$, so $\mathbf{X} = \mathbf{X}^A$ with $A = \mathbf{X}_I$; conversely $g\,(hA) = (gh)A$, so every $\mathbf{X}^A$ is left-invariant, and it is smooth because its entries are linear in those of $g$.

^pf-ex-50-1

*Uses:* [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-2|Def. §50.2]], [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-3|Def. §50.3]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]], [[§48 Vector Fields#^prop-48-1|§48.1]]

Compare [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]], where $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$ for the classical groups: a left-invariant field moves the tangent space at the identity around the group by left multiplication.

> [!definition] Definition §50.4: The Lie Algebra of a Lie Group
> The **Lie algebra** of a [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-1|Lie group]] $G$ is
>
> $$
> \mathfrak{g} = \{\, \mathbf{X} \in \mathfrak{X}(G) \mid \mathbf{X} \text{ is left-invariant} \,\},
> $$
>
> with the [[§49 Lie Bracket and Lie Algebra#^def-49-1|Lie bracket of vector fields]].
>
> *Lee: Ch. 8, Lie Algebras*

^def-50-4

> [!remark]- Connections
> - The physicists' definition for matrix Lie groups, directly as $T_{\mathbb 1}G$ with the matrix commutator: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|QFT Def. §CB.1.9]].

*Status.* Defined in Lecture 16, with two facts announced for next time: that the bracket of two [[§50 Lie Groups and Left-Invariant Vector Fields#^def-50-3|left-invariant]] fields is again left-invariant, so that $\mathfrak{g}$ is a Lie subalgebra of $\mathfrak{X}(G)$ ([[§49 Lie Bracket and Lie Algebra#^cor-49-4|Corollary §49.4]]; Lee, Proposition 8.33); and that $\mathbf{X} \mapsto \mathbf{X}_e$ identifies $\mathfrak{g}$ with $T_eG$ — “this is going to be quickly identified with the tangent space at the identity. But originally we think of them as a certain very special type of vector field, because that's where the Lie bracket comes from.” For $\mathrm{GL}(n,\mathbb{R})$ the identification is $\mathbf{X}^A \mapsto A$ ([[§50 Lie Groups and Left-Invariant Vector Fields#^ex-50-1|Example §50.1]]). “We'll come back to this in detail next time.”
