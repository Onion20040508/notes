---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 7
section: 52
tags: [differentiable-manifolds, math591]
---
← [[§51 Related Vector Fields]] · ↑ [[· 7 Vector Fields and Lie Groups]]

*Stage: symmetry — Groups that are manifolds, and the vector fields that respect the group: the start of Lie theory.*

*Lecture 16, last three minutes, to be continued. References: Lee Ch. 7 and Ch. 8. “Lie algebras and Lie groups are related, and in one direction the relationship is very nice: any Lie group has a Lie algebra associated to it.”*

> [!definition] Definition §52.1: Lie Group
> A **Lie group** is a [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological group]] $G$ ([[§11 Topological Groups and Classical Matrix Groups#^def-11-1|Definition §11.1]]) together with a [[§17 Differentiable Structures#^def-17-9|smooth structure]], such that multiplication $G \times G \to G$, $(g, h) \mapsto gh$, and inversion $G \to G$, $g \mapsto g^{-1}$, are [[§19 Smooth Functions and Smooth Maps#^def-19-3|smooth maps]].
>
> *Lee: Ch. 7, Basic Definitions*

^def-52-1

> [!remark]- Connections
> - The physicists' version, closed subgroups of $\mathrm{GL}(n,\mathbb{C})$: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-3|QFT Def. §CB.1.3]].

For a topological group the two maps had to be continuous; “now we ask that they be smooth maps, because we have a manifold structure, so we can make sense of that.”

> [!theorem] Proposition §52.1: The Classical Groups Are Lie Groups
> $\mathrm{GL}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$, $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$ and $\mathrm{SU}(2)$, with the smooth structures of [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]] and [[§42 SU(2) → SO(3)꞉ The Double Cover|§42]], are [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Lie groups]].
>
> *Lee: Examples 7.3, 7.27–7.30*

^prop-52-1

> [!proof]+ Proof
> *(Stated in Lecture 16 — “all the matrix groups that we have seen … are Lie groups”; filled in.)* Each group $G$ is an open subset or a submanifold of a space of matrices $\operatorname{Mat}$ ([[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]]; for $\mathrm{SU}(2)$, [[§41 The Unit Quaternions and SU(2)#^prop-41-5|Proposition §41.5]]), with $\iota : G \hookrightarrow \operatorname{Mat}$ smooth ([[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3]]). *Multiplication* is the composite of $\iota \times \iota : G \times G \to \operatorname{Mat} \times \operatorname{Mat}$, smooth since its components are, with matrix multiplication, whose entries are polynomials in the real coordinates; it lands in $G$, so it is smooth into $G$ ([[§35 Regular Submanifolds#^lem-35-3|Lemma §35.3]](2)). *Inversion* is the restriction of a smooth map on the open set of invertible matrices — $g \mapsto \operatorname{adj}(g)/\det g$ by the [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|cofactor formula]], a rational map with nonvanishing denominator — landing in $G$, hence smooth into $G$ in the same way. (For $\mathrm{O}(n)$ and $\mathrm{U}(n)$ it is even linear: $g \mapsto g^{\mathsf T}$, $g \mapsto g^{\ast}$.)

^pf-52-1

*Uses:* [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Def. §52.1]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§41 The Unit Quaternions and SU(2)#^prop-41-5|§41.5]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§27 Cramer’s Rule, Volume, and Linear Transformations#^thm-27-2|235 Thm. §27.2]]

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|The Double Cover]]; the Lie algebra $\mathfrak{so}(3)$ and the cross product in [[§50 Lie Bracket and Lie Algebra#^ex-50-3|Ex. §50.3]]; and Lie groups in [[§52 Lie Groups and Left-Invariant Vector Fields#^prop-52-1|§52.1]].

The unit quaternions $S^3$ are a Lie group as well ([[§41 The Unit Quaternions and SU(2)#^prop-41-4|Proposition §41.4]]), isomorphic to $\mathrm{SU}(2)$ ([[§41 The Unit Quaternions and SU(2)#^prop-41-5|Proposition §41.5]]).

> [!definition] Definition §52.2: Left Translation
> For $g$ in a [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Lie group]] $G$, **left translation** by $g$ is $L_g : G \to G$, $L_g(h) = gh$.
>
> *Lee: Ch. 7, Basic Definitions*

^def-52-2

> [!theorem] Lemma §52.2: Left Translations Are Diffeomorphisms
> $L_g$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], with inverse $L_{g^{-1}}$.
>
> *Lee: Ch. 7, Basic Definitions*

^lem-52-2

> [!proof]+ Proof
> *(Filled in, as for [[§11 Topological Groups and Classical Matrix Groups#^def-11-1|topological groups]] in [[§13 Group Actions and Orbit Spaces#^lem-13-2|Lemma §13.2]].)* $L_g$ is smooth as the composite of $h \mapsto (g, h)$ with multiplication, and $L_g \circ L_{g^{-1}} = L_{g^{-1}} \circ L_g = \mathrm{id}$.

^pf-52-2

*Uses:* [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Def. §52.1]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|Def. §52.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§13 Group Actions and Orbit Spaces#^lem-13-2|§13.2]]

> [!definition] Definition §52.3: Left-Invariant Vector Field
> A [[§48 Vector Fields#^def-48-1|vector field]] $\mathbf{X} \in \mathfrak{X}(G)$ is **left-invariant** if for all $g, h \in G$
>
> $$
> (L_g)_{*h}\, \mathbf{X}_h = \mathbf{X}_{gh} .
> $$
>
> *Lee: Ch. 8, Lie Algebras*

^def-52-3

![[m591-49-1.svg]]
*Left invariance as a diagram: the differential $(L_g)_{\ast h}$ of [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|left translation]] carries the value $\mathbf{X}_h$ of the field at $h$ to its value $\mathbf{X}_{gh}$ at $gh$.*

Left invariance in one line: “using [left translations], you can push vectors of the field to get other vectors; and whenever you do that, you get the corresponding vector of the field.” The value at one point determines the field everywhere: taking $h = e$, $\mathbf{X}_g = (L_g)_{\ast e}\, \mathbf{X}_e$. This is the [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|left translation]] of tangent spaces from the discussion of moving the base point ([[§42 SU(2) → SO(3)꞉ The Double Cover#^lem-42-3|Lemma §42.3]]), applied to a whole field.

> [!example] Example §52.1: Left-Invariant Fields on $\mathrm{GL}(n,\mathbb{R})$
> On $G = \mathrm{GL}(n,\mathbb{R})$, open in $\operatorname{Mat}(n,\mathbb{R})$, so that $T_gG = \operatorname{Mat}(n,\mathbb{R})$, the [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|left-invariant vector fields]] are exactly
>
> $$
> \mathbf{X}^A_g = gA, \qquad A \in \operatorname{Mat}(n,\mathbb{R}) = T_IG .
> $$

^ex-52-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $L_g$ is the restriction of the linear map $h \mapsto gh$, so its [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|differential]] at every point is that same linear map: $(L_g)_{\ast h}(v) = gv$. Left invariance therefore reads $g\,\mathbf{X}_h = \mathbf{X}_{gh}$ for all $g, h$. Taking $h = I$ gives $\mathbf{X}_g = g\,\mathbf{X}_I$, so $\mathbf{X} = \mathbf{X}^A$ with $A = \mathbf{X}_I$; conversely $g\,(hA) = (gh)A$, so every $\mathbf{X}^A$ is left-invariant, and it is smooth because its entries are linear in those of $g$.

^pf-ex-52-1

*Uses:* [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|Def. §52.2]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|Def. §52.3]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Def. §22.5]], [[§48 Vector Fields#^prop-48-1|§48.1]]

Compare [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]], where $T^{\mathrm{geo}}_g G = g \cdot T^{\mathrm{geo}}_I G$ for the classical groups: a left-invariant field moves the tangent space at the identity around the group by left multiplication.

> [!definition] Definition §52.4: The Lie Algebra of a Lie Group
> The **Lie algebra** of a [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Lie group]] $G$ is
>
> $$
> \mathfrak{g} = \{\, \mathbf{X} \in \mathfrak{X}(G) \mid \mathbf{X} \text{ is left-invariant} \,\},
> $$
>
> with the [[§50 Lie Bracket and Lie Algebra#^def-50-1|Lie bracket of vector fields]].
>
> *Lee: Ch. 8, Lie Algebras*

^def-52-4

> [!remark]- Connections
> - The physicists' definition for matrix Lie groups, directly as $T_{\mathbb 1}G$ with the matrix commutator: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-11|QFT Def. §CB.1.11]].

*Status.* Defined in Lecture 16 — “this is going to be quickly identified with the tangent space at the identity. But originally we think of them as a certain very special type of vector field, because that's where the Lie bracket comes from.” For $\mathrm{GL}(n,\mathbb{R})$ the identification is $\mathbf{X}^A \mapsto A$ ([[§52 Lie Groups and Left-Invariant Vector Fields#^ex-52-1|Example §52.1]]). The two facts announced then were proved in Lecture 17, in [[§52 Lie Groups and Left-Invariant Vector Fields#The Lie Algebra and the Tangent Space at the Identity|§52, The Lie Algebra and the Tangent Space at the Identity]] below: $\mathfrak{g}$ is closed under the bracket ([[§52 Lie Groups and Left-Invariant Vector Fields#^cor-52-4|Corollary §52.4]]), and $\mathbf{X} \mapsto \mathbf{X}_e$ is an isomorphism onto $T_eG$ ([[§52 Lie Groups and Left-Invariant Vector Fields#^thm-52-5|Theorem §52.5]]).

## The Lie Algebra and the Tangent Space at the Identity

*Lecture 17. “Back to Lie groups.” With the language of [[§51 Related Vector Fields#^def-51-2|related fields]], “we can rephrase some of the definitions.”*

> [!theorem] Lemma §52.3: Left-Invariance as Relatedness
> A vector field $\mathbf{X} \in \mathfrak{X}(G)$ is [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|left-invariant]] ([[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|Definition §52.3]]) if and only if, for every $g \in G$, $\mathbf{X}$ is *$L_g$-related to itself* ([[§51 Related Vector Fields#^def-51-2|Definition §51.2]] with $F = L_g$ and $\mathbf{Y} = \mathbf{X}$).

^lem-52-3

> [!proof]+ Proof
> *(Lecture 17, a rephrasing of the definition: “we can rephrase some of the definitions”.)* Being $L_g$-related to itself means $d(L_g)_h(\mathbf{X}_h) = \mathbf{X}_{L_g(h)} = \mathbf{X}_{gh}$ for every $h \in G$, which is the condition of [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|Definition §52.3]] for this $g$.

^pf-52-3

*Uses:* [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|Def. §52.3]], [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|Def. §52.2]]

> [!remark] Remark: Why Left?
> Lecture 17 abbreviates “left-invariant” to l.i. “And you can ask why left. What's wrong with right? There's nothing wrong with right. You have to choose … and this is the universal choice.” Right-invariant fields, $R_g$-related to themselves for $R_g(h) = hg$, give an equivalent theory; the one place the choice shows is the sign of the bracket, at the end of this subsection ([[§52 Lie Groups and Left-Invariant Vector Fields#^rem-52-2|Remark: Left or Right]]).

^rem-52-1

> [!theorem] Corollary §52.4: $\mathfrak{g}$ Is a Lie Subalgebra of $\mathfrak{X}(G)$
> If $\mathbf{X}, \mathbf{Y} \in \mathfrak{g}$ then $[\mathbf{X}, \mathbf{Y}] \in \mathfrak{g}$. So $\mathfrak{g}$, a linear subspace of $\mathfrak{X}(G)$, is a [[§50 Lie Bracket and Lie Algebra#^def-50-2|Lie algebra]] under the [[§50 Lie Bracket and Lie Algebra#^def-50-1|bracket of vector fields]].
>
> *Lee: Proposition 8.33*

^cor-52-4

> [!proof]+ Proof
> *(Lecture 17: “the big observation, which is actually a consequence of” [[§51 Related Vector Fields#^prop-51-3|Proposition §51.3]].)* Fix $g \in G$. $\mathbf{X}$ is $L_g$-related to $\mathbf{X}$ and $\mathbf{Y}$ to $\mathbf{Y}$, so by [[§51 Related Vector Fields#^prop-51-3|Proposition §51.3]] with $F = L_g$, $[\mathbf{X}, \mathbf{Y}]$ is $L_g$-related to $[\mathbf{X}, \mathbf{Y}]$; this for every $g$ is left-invariance. *(Filled in.)* $\mathfrak{g}$ is a linear subspace because each $d(L_g)_h$ is linear; and the bracket on $\mathfrak{g}$ is bilinear, skew and satisfies Jacobi because it does on $\mathfrak{X}(G)$ ([[§50 Lie Bracket and Lie Algebra#^cor-50-4|Corollary §50.4]]).

^pf-52-4

*Uses:* [[§52 Lie Groups and Left-Invariant Vector Fields#^lem-52-3|§52.3]], [[§51 Related Vector Fields#^def-51-2|Def. §51.2]], [[§51 Related Vector Fields#^prop-51-3|§51.3]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|Def. §52.3]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-4|Def. §52.4]], [[§50 Lie Bracket and Lie Algebra#^cor-50-4|§50.4]]

“It's a Lie subalgebra of the infinite-dimensional algebra of all vector fields on $G$.” Vector fields can be added and scaled, so $\mathfrak{X}(G)$ is a [[§48 Vector Fields#^def-48-2|vector space]] (“in fact, it's an algebra over the smooth functions, but I want to think of it as a vector space”). “At this point, maybe it's not clear what [$\mathfrak{g}$] is. It could be, I don't know, still infinite-dimensional, or something, or empty.” [[§52 Lie Groups and Left-Invariant Vector Fields#^thm-52-5|The theorem]] settles it.

> [!theorem] Theorem §52.5: The Lie Algebra Is the Tangent Space at the Identity
> Let $G$ be a [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Lie group]] with identity $e$. The evaluation map
>
> $$
> \mathrm{ev} : \mathfrak{g} \to T_eG, \qquad \mathbf{X} \mapsto \mathbf{X}_e ,
> $$
>
> is a linear isomorphism. In particular $\dim \mathfrak{g} = \dim G$.
>
> *Lee: Theorem 8.37*

^thm-52-5

> [!proof]+ Proof
> *(Lecture 17 — “it'll be an incomplete proof … there is one detail that we're not prepared to prove.” The lecture's steps, then that detail.)* $\mathrm{ev}$ is linear. *The basic idea.* For $g \in G$, $L_g$ maps $e$ to $g$, so $d(L_g)_e : T_eG \to T_gG$, and for $\mathbf{X} \in \mathfrak{g}$, [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|left-invariance]] with $h = e$ reads
>
> $$
> d(L_g)_e(\mathbf{X}_e) = \mathbf{X}_g ;
> $$
>
> more generally $d(L_g)_h(\mathbf{X}_h) = \mathbf{X}_{gh}$ for all $h$. “There's only one choice really.”
>
> *Injective.* By the basic idea, $\mathbf{X}$ is determined by its value at $e$. So $\mathbf{X}_e = 0$ forces $\mathbf{X}_g = 0$ for all $g$.
>
> *Surjective.* Start with $v \in T_eG$; we want a left-invariant $\mathbf{X}$ with $\mathbf{X}_e = v$. The basic idea says there is no choice: we must define
>
> $$
> \mathbf{X}^v_g = d(L_g)_e(v), \qquad g \in G .
> $$
>
> “Just as with vector fields” on a vector space ([[§30 The Differential in Coordinates#^rem-30-4|§30, Remark: Translations Identify the Tangent Spaces of a Vector Space]]), there is a unique [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|left translation]] carrying $e$ to $g$, and $\mathbf{X}^v_g$ is $v$ carried along it. This defines $\mathbf{X}^v$ as a [[§36 Fibrations#^def-36-2|section]] of $TG$ with $\mathbf{X}^v_e = v$. *(Filled in.)* It is left-invariant: $L_g \circ L_h = L_{gh}$, so by the chain rule ([[§28 Derivations and the Abstract Tangent Space#^thm-28-6|Theorem §28.6]])
>
> $$
> d(L_g)_h\big(\mathbf{X}^v_h\big) = d(L_g)_h\, d(L_h)_e(v) = d(L_{gh})_e(v) = \mathbf{X}^v_{gh} .
> $$
>
> *Smooth.* “The incompleteness in the proof is that we want to show that this is $C^\infty$. It's an important technical point … and we don't have the tools to do that at this point.” *(Not from lecture: Lee's argument, filled in; it uses only [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2]] and [[§48 Vector Fields#^lem-48-8|Lemma §48.8]]. The argument Uribe has in mind, for later, may be different.)* By [[§48 Vector Fields#^lem-48-8|Lemma §48.8]] it suffices that $\mathbf{X}^v f$ is smooth for every $f \in C^\infty(G)$. By [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|Theorem §31.2]] choose a [[§31 Tangent Vectors as Velocities of Curves#^def-31-1|smooth curve]] $\gamma : (-\varepsilon, \varepsilon) \to G$ with $\gamma(0) = e$ and $D_\gamma = v$. Then
>
> $$
> (\mathbf{X}^v f)(g) = d(L_g)_e(D_\gamma)[f] = D_\gamma[f \circ L_g] = \frac{d}{dt}\Big|_{t=0} f\big(g\,\gamma(t)\big).
> $$
>
> Put $\phi(t, g) = f(g\,\gamma(t))$ on $(-\varepsilon, \varepsilon) \times G$. It is smooth, as the composite of $(t, g) \mapsto (g, \gamma(t))$, multiplication and $f$. So $(\mathbf{X}^v f)(g) = \partial\phi/\partial t\,(0, g)$; in a chart of $G$ this is a partial derivative of a smooth function of $(t, x)$, evaluated at $t = 0$, hence smooth in $x$. So $\mathbf{X}^v \in \mathfrak{g}$ and $\mathrm{ev}(\mathbf{X}^v) = v$.
>
> Finally $\dim \mathfrak{g} = \dim T_eG = \dim G$ ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|Theorem §29.8]]).

^pf-52-5

*Uses:* [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Def. §52.1]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-2|Def. §52.2]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|Def. §52.3]], [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-4|Def. §52.4]], [[§30 The Differential in Coordinates#^rem-30-4|§30, Remark: Translations Identify the Tangent Spaces of a Vector Space]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§48 Vector Fields#^lem-48-8|§48.8]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]

> [!remark]- Connections
> - The matrix-group version, with $\mathfrak g$ defined through the exponential and identified with $T_{\mathbb 1}G$ and with the left-invariant fields: [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|QFT Theorem §CB.1.16]].

![[m591-50-1.svg]]
*The left-invariant field $\mathbf{X}^v$: the vector $v \in T_eG$ carried to $g$ by the differential of the left translation $L_g$.*

> [!example] Example §52.2: The Additive Group of a Vector Space
> Let $V$ be a finite-dimensional vector space, a [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Lie group]] under addition with identity $0$, so that $L_p = \tau_p$ is translation by $p$. Its [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-3|left-invariant vector fields]] are the constant fields $\mathbf{X}^v : p \mapsto D_v|_p$, $v \in V$, and all their [[§50 Lie Bracket and Lie Algebra#^def-50-1|brackets]] vanish: $\mathfrak{g} \cong V$ with the zero bracket.

^ex-52-2

> [!proof]+ Proof
> *(Not from lecture; filled in, after the remark in Lecture 17 that the translations of a vector space give “a left-invariant vector field”.)* By [[§30 The Differential in Coordinates#^rem-30-4|§30, Remark: Translations Identify the Tangent Spaces of a Vector Space]], $d(\tau_p)_0(D_v|_0) = D_v|_p$, so the field $\mathbf{X}^v$ of [[§52 Lie Groups and Left-Invariant Vector Fields#^thm-52-5|the theorem]], with $\mathbf{X}^v_0 = D_v|_0$, is $p \mapsto D_v|_p$; by the theorem these are all the left-invariant fields. In [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|linear coordinates]] $\mathbf{X}^v = \sum_i v^i\, \partial_i$ has constant coefficients, so $[\mathbf{X}^v, \mathbf{X}^w] = 0$ by [[§50 Lie Bracket and Lie Algebra#^prop-50-2|Proposition §50.2]].

^pf-ex-52-2

*Uses:* [[§30 The Differential in Coordinates#^rem-30-4|§30, Remark: Translations Identify the Tangent Spaces of a Vector Space]], [[§52 Lie Groups and Left-Invariant Vector Fields#^thm-52-5|§52.5]], [[§22 The Differential of a Map Between Vector Spaces#^def-22-1|Def. §22.1]], [[§50 Lie Bracket and Lie Algebra#^prop-50-2|§50.2]]

> [!definition] Definition §52.5: The Lie Bracket on $T_eG$
> Let $G$ be a [[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-1|Lie group]] and, for $v \in T_eG$, let $\mathbf{X}^v \in \mathfrak{g}$ be the left-invariant field with $\mathbf{X}^v_e = v$ ([[§52 Lie Groups and Left-Invariant Vector Fields#^thm-52-5|Theorem §52.5]]). The **Lie bracket** on $T_eG$ is
>
> $$
> [v, w] = \big[\mathbf{X}^v, \mathbf{X}^w\big]_e , \qquad v, w \in T_eG .
> $$

^def-52-5

By construction $\mathrm{ev}$ is then an isomorphism of [[§50 Lie Bracket and Lie Algebra#^def-50-2|Lie algebras]]: $T_eG$ inherits the bracket that makes it one. The question is what this bracket is.

> [!theorem] Theorem §52.6: The Lie Algebra of $\mathrm{GL}(d,\mathbb{R})$
> Let $G = \mathrm{GL}(d, \mathbb{R})$, the $d \times d$ invertible matrices, an open subset of $\operatorname{Mat}(d, \mathbb{R}) \cong \mathbb{R}^{d^2}$, so that $T_IG = \operatorname{Mat}(d,\mathbb{R})$. The Lie bracket on $T_IG$ ([[§52 Lie Groups and Left-Invariant Vector Fields#^def-52-5|Definition §52.5]]) is the matrix commutator
>
> $$
> [A, B] = AB - BA .
> $$

^thm-52-6

> [!proof]- Proof (to be filled)
> Stated in Lecture 17 — “for all matrix groups, the answer … is just the matrix commutator”; “that requires computation. You actually have to compute something” — to begin on Monday (Lecture 18). The left-invariant fields are already known ([[§52 Lie Groups and Left-Invariant Vector Fields#^ex-52-1|Example §52.1]]: $\mathbf{X}^A_g = gA$).

^pf-52-6

> [!remark]- Connections
> - The commutator Lie algebra of matrices: [[§50 Lie Bracket and Lie Algebra#^ex-50-2|Ex. §50.2]].
> - For matrix Lie groups the physics notes prove the answer: the bracket of left-invariant fields becomes $XY - YX$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|QFT Theorem §CB.1.16]], part 3), and $\mathfrak g$ is closed under it ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-12|QFT Theorem §CB.1.12]]).

> [!remark] Remark: Left or Right: The Sign of the Bracket
> “This is the case because we use left-invariant fields. If we use right-invariant fields, we would have minus that.” Why left, then? An aside: “Did you ever think what the world would look like if, instead of writing $f(x)$ … we would have written $(x)f$? … Imagine composing functions with that rule. … Everything works much better if you write $(x)f$”: in that notation, composites read in the order the maps are applied.

^rem-52-2

**Transcription note (Lecture 17).** Page 46 of the handwritten notes says the construction gives “$\mathbf{X} : M \to TM$”; the manifold is the group, $\mathbf{X} : G \to TG$.
