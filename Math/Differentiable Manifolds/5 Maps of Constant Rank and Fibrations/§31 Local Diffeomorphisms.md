---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 31
tags: [differentiable-manifolds, math591]
---
← [[§30 The Cotangent Space]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§32 Submersions]] →

*Stage: maps — Properties of the linear maps $F_{\ast p}$ control the local behaviour of $F$ itself.*

*References: Lee Ch. 4. Lecture 10.*

Three special types of smooth maps $F : M \to N$ are singled out by the linear algebra of their differentials: *local diffeomorphisms*, whose differentials are bijective; *submersions*, whose differentials are surjective; and *immersions*, whose differentials are injective. The theme of the section is that in each case a property of the linear maps $F_{\ast p}$ — computable from a Jacobian — controls the behaviour of $F$ itself near $p$. Immersions, listed with the others in Lecture 10, were treated only in Lecture 13, after the tangent bundle, and have their own section, [[§35 Immersions|§35]]; everything up to the tangent bundle is the theory of submersions. “That's why we're discussing them in this context.”

> [!definition] Definition §31.1: Local Diffeomorphism
> A smooth map $F : M \to N$ is a **local diffeomorphism** if for every $p \in M$ there are neighbourhoods $U$ of $p$ and $V$ of $F(p)$ with $F(U) = V$ such that $F|_U^V : U \to V$ — the restriction of $F$ to $U$, regarded as a map onto $V$ — has a smooth inverse. Such an inverse $G : V \to U$ is a **local inverse** of $F$ at $p$.
>
> *Lee: Ch. 2 and Ch. 4*

^def-31-1

> [!remark] Remark
> Neighbourhoods are open ([[§1 Point-Set Topology Review#^rem-1-4|§1]]). A local diffeomorphism need not be injective: the local inverses are local, and different ones need not fit together. The examples show both finite-to-one and infinite-to-one behaviour.

^rem-31-1

> [!example] Example §31.1: The Circle Covered by a Line
> $F : \mathbb{R} \to S^1$, $F(t) = (\cos t, \sin t)$, is a local diffeomorphism, and so is its restriction to $(0, 4\pi)$. Neither is injective.
>
> *Lee: cf. Ch. 4, Smooth Covering Maps*

^ex-31-1

> [!proof]+ Proof
> *(Stated in Lecture 10 as an example, without proof — the covering-map distinction was “postponed”; filled in.)* $F$ is smooth into $\mathbb{R}^2$ with values in $S^1$; by Lemma [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]](2) it is therefore smooth into $S^1$. Fix $t_0$ and let $U = (t_0 - \pi, t_0 + \pi)$ and $V = S^1 \setminus \{F(t_0 + \pi)\}$. Then $F$ maps $U$ bijectively onto $V$, and its inverse is the angle chart $\theta : V \to U$ taking values in $U$, which belongs to the smooth structure of $S^1$ (Proposition [[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]] and the remark on ranges in its proof). So $F|_U^V = \theta^{-1}$ is a diffeomorphism by Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]. For $t_0 \in (0,4\pi)$, replace $U$ by $U \cap (0, 4\pi)$ and $V$ by its image, which is open because $F|_U^V$ is a homeomorphism. Finally $F(t + 2\pi) = F(t)$.

^pf-ex-31-1

*Uses:* [[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]], [[§19 Manifolds in Euclidean Space#^lem-19-3|§19.3]], [[§19 Manifolds in Euclidean Space#^prop-19-4|§19.4]], [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]

![[m591-14-1.svg]]
*The helix is the interval $(0, 4\pi)$, lifted so that $F$ becomes the vertical projection onto the circle. On the orange interval $U$ the projection is a diffeomorphism onto the arc $V$; but the point $q \in V$ has a second preimage $t_1 + 2\pi$, on the other turn and outside $U$. Local invertibility does not see it.*

> [!remark]- Connections
> - As a covering map of topological spaces: [[§31 Covering Spaces#^thm-31-2|590 §31.2]] ($\mathbb{R} \to S^1$ is a covering map).

The projection $S^n \to \mathbb{RP}^n$, a two-to-one local diffeomorphism, is collected in [[§37 Projective Spaces and the Hopf Fibration|§37]].

> [!remark] Remark: Covering Maps
> Uribe noted that $\mathbb{R} \to S^1$ and $S^n \to \mathbb{RP}^n$ are *covering maps*, while $(0, 4\pi) \to S^1$ is a local diffeomorphism that is not: over the point $F(0) = (1,0)$ it has a single preimage, $2\pi$, where every other point of the circle has two. Covering maps were not defined in lecture and the distinction was postponed (“we're running a little bit behind schedule”); it is Lee Ch. 4.

^rem-31-2

> [!remark]- Connections
> - Covering maps are defined in [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]; the same failure for a half-line, $\mathbb{R}_+ \to S^1$, is [[§31 Covering Spaces#^ex-31-2|590 Ex. §31.2]].
> - Used in Quantum Mechanics: $S^3 \to \mathbb{RP}^3$ is $SU(2) \to SO(3)$; because $SU(2)$ is simply connected ([[Sⁿ is Simply Connected for n ≥ 2|590 §37.3]]) and $SO(3)$ is not ([[§38 Fundamental Group of Some Surfaces#^thm-38-3|590 §38.3]]), the sign of a spinor under a rotation by $2\pi$ cannot be removed — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^rem-c5-2-6|QM ★ Remark: Why the sign cannot be removed]].

The converse direction of the main theorem rests on one theorem from analysis — “that's really what's paying the bills here.”

> [!theorem] Theorem §31.1: Inverse Function Theorem
> Let $W \subseteq \mathbb{R}^n$ be open, $\Phi : W \to \mathbb{R}^n$ smooth, and $a \in W$ with $\Phi'(a)$ invertible. Then there are open sets $U_0 \ni a$ in $W$ and $V_0 \ni \Phi(a)$ in $\mathbb{R}^n$ such that $\Phi(U_0) = V_0$ and $\Phi|_{U_0} : U_0 \to V_0$ is bijective with smooth inverse.
>
> *Lee: Theorem C.34*

^thm-31-1

> [!proof]+ Proof (to be filled)
> Taken from analysis, not proved in this course (Lee, Theorem C.34; [[Inverse Function Theorem (several variables)|452 §16.2]] proves the two-variable case). To be filled.

^pf-31-1

> [!remark]- Connections
> - Home in analysis (the two-variable version): [[Inverse Function Theorem (several variables)|452 §16.2]].
> - The implicit function theorem it should not be confused with: [[§7 The Regular Value Theorem#^thm-7-1|§7.1]].

Lee, Theorem C.34; taken from analysis, not proved in the course. It should not be confused with the *implicit* function theorem of [[§7 The Regular Value Theorem|§7]] — the board's “IFT” now means the inverse one. Each theorem can be derived from the other.

> [!theorem] Theorem §31.2: Local Diffeomorphisms Are Detected by the Differential
> A smooth map $F : M \to N$ is a local diffeomorphism if and only if $F_{*p} : T_pM \to T_{F(p)}N$ is bijective for every $p \in M$.
>
> *Lee: Theorem 4.5 and Proposition 4.8*

^thm-31-2

> [!proof]+ Proof
> *(Lecture 10. The forward direction was supplied by a student at Uribe's prompting — use the local inverse and the chain rule; for the converse the inverse function theorem “is really what's paying the bills here.” The identification of $(F|_U^V)_{\ast p}$ with $F_{\ast p}$ is a completion.)* ($\Rightarrow$) Let $G : V \to U$ be a local inverse at $p$, so that $G \circ F|_U^V = \mathrm{id}_U$ and $F|_U^V \circ G = \mathrm{id}_V$. By the Chain Rule (Theorem [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]]),
>
> $$
> G_{*F(p)} \circ (F|_U^V)_{*p} = \mathrm{id}, \qquad (F|_U^V)_{*p} \circ G_{*F(p)} = \mathrm{id},
> $$
>
> so $(F|_U^V)_{*p}$ is bijective with inverse $G_{*F(p)}$. Under the identifications $T_pU = T_pM$ and $T_{F(p)}V = T_{F(p)}N$ of Lemma [[§26 Derivations and the Abstract Tangent Space#^lem-26-8|§26.8]], $(F|_U^V)_{*p}$ is $F_{*p}$, again by the Chain Rule applied to $F \circ \iota_U = \iota_V \circ F|_U^V$.
>
> ($\Leftarrow$) Fix $p$, and choose charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ with $F(U) \subseteq V$. A bijective linear map forces $\dim M = \dim N$, and by Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] the matrix of $F_{*p}$ is the square matrix $\tilde F'(\varphi(p))$; so the latter is invertible. By the Inverse Function Theorem there are open sets $\tilde A \ni \varphi(p)$ in $\varphi(U)$ and $\tilde B \ni \tilde F(\varphi(p))$ such that $\tilde F|_{\tilde A} : \tilde A \to \tilde B$ is bijective with smooth inverse. Put $U' = \varphi^{-1}(\tilde A)$ and $V' = \psi^{-1}(\tilde B)$, neighbourhoods of $p$ and $F(p)$; since $\varphi$ is a homeomorphism, “shrinking $\varphi(U)$ is the same as shrinking $U$.” On $U'$ we have $F = \psi^{-1} \circ \tilde F \circ \varphi$, so $F(U') = V'$ and
>
> $$
> \big(F|_{U'}^{V'}\big)^{-1} = \varphi^{-1} \circ \big(\tilde F|_{\tilde A}\big)^{-1} \circ \psi|_{V'},
> $$
>
> a composite of diffeomorphisms (Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]), hence smooth.

^pf-31-2

*Uses:* [[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]], [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]], [[§26 Derivations and the Abstract Tangent Space#^lem-26-8|§26.8]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§31 Local Diffeomorphisms#^thm-31-1|§31.1]], [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]

![[m591-14-2.svg]]
*The converse in one picture. Downstairs the Inverse Function Theorem supplies $\tilde F^{-1}$; the charts carry it upstairs as the local inverse $G = \varphi^{-1} \circ \tilde F^{-1} \circ \psi$. The only input from the hypothesis is that the bottom arrow has an invertible Jacobian at $\varphi(p)$ — which is where Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] enters.*

A student asked why $\tilde F'(\varphi(p))$ is invertible; Uribe's answer was the lemma just cited: the Jacobian *is* the matrix of $F_{\ast p}$ in coordinate bases, and $F_{\ast p}$ is bijective by hypothesis. The practical content of the theorem is that “being a local diffeomorphism is detectable” by computing one Jacobian at each point, rather than by exhibiting local inverses.

> [!theorem] Corollary §31.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms
> A smooth map $F : M \to N$ is a diffeomorphism if and only if it is a bijective local diffeomorphism. Consequently, a smooth bijection with $F_{*p}$ bijective at every $p \in M$ is a diffeomorphism.
>
> *Lee: Proposition 4.6*

^cor-31-3

> [!proof]+ Proof
> A diffeomorphism is a local diffeomorphism with $U = M$ and $V = N$. Conversely, let $F$ be a bijective local diffeomorphism. Given $q \in N$, let $p = F^{-1}(q)$ and let $G : V \to U$ be a local inverse at $p$. For $y \in V$, $G(y) \in U$ and $F(G(y)) = y$, so $G(y) = F^{-1}(y)$ because $F$ is injective. Thus $F^{-1}$ agrees on the open neighbourhood $V$ of $q$ with the smooth map $G$. As $q$ was arbitrary, $F^{-1}$ is continuous and smooth, since both properties are local. The last sentence follows from Theorem [[§31 Local Diffeomorphisms#^thm-31-2|§31.2]].

^pf-31-3

*Uses:* [[§31 Local Diffeomorphisms#^def-31-1|Def. §31.1]], [[§31 Local Diffeomorphisms#^thm-31-2|§31.2]]

> [!remark] Remark
> Not stated in lecture. Injectivity is the entire difference between the two notions, as the helix of Example [[§31 Local Diffeomorphisms#^ex-31-1|§31.1]] shows: there every local inverse exists, but they cannot be assembled into a global one, because the second preimage of $q$ lies outside the domain of the local inverse. The same argument shows that a bijective local homeomorphism is a homeomorphism.

^rem-31-3
