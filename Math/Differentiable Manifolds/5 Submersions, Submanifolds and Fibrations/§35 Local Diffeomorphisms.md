---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 35
tags: [differentiable-manifolds, math591]
---
← [[§34 The Cotangent Space from Germs]] · ↑ [[· 5 Submersions, Submanifolds and Fibrations]] · [[§36 Submersions]] →

*Stage: maps — Properties of the linear maps $F_{\ast p}$ control the local behaviour of $F$ itself.*

*References: Lee Ch. 4. Lecture 10.*

Three special types of smooth maps $F : M \to N$ are singled out by the linear algebra of their differentials: *local diffeomorphisms*, whose differentials are bijective; *submersions*, whose differentials are surjective; and *immersions*, whose differentials are injective. The theme of the section is that in each case a property of the linear maps $F_{\ast p}$ — computable from a Jacobian — controls the behaviour of $F$ itself near $p$. Immersions, listed with the others in Lecture 10, were treated only in Lecture 13, after the tangent bundle, and have their own section, [[§43 Immersions|§43]]; everything up to the tangent bundle is the theory of submersions. “That's why we're discussing them in this context.”

> [!definition] Definition §35.1: Local Diffeomorphism
> A smooth map $F : M \to N$ is a **local diffeomorphism** if for every $p \in M$ there are neighbourhoods $U$ of $p$ and $V$ of $F(p)$ with $F(U) = V$ such that $F|_U^V : U \to V$ — the restriction of $F$ to $U$, regarded as a map onto $V$ — has a smooth inverse. Such an inverse $G : V \to U$ is a **local inverse** of $F$ at $p$.
>
> *Lee: Ch. 2 and Ch. 4*

^def-35-1

> [!remark] Remark
> Neighbourhoods are open ([[§1 Point-Set Topology Review#^rem-1-4|§1]]). A local diffeomorphism need not be injective: the local inverses are local, and different ones need not fit together. The examples show both finite-to-one and infinite-to-one behaviour.

^rem-35-1

> [!example] Example §35.1: The Circle Covered by a Line
> $F : \mathbb{R} \to S^1$, $F(t) = (\cos t, \sin t)$, is a local diffeomorphism, and so is its restriction to $(0, 4\pi)$. Neither is injective.
>
> *Lee: cf. Ch. 4, Smooth Covering Maps*

^ex-35-1

> [!proof]+ Proof
> *(Stated in Lecture 10 as an example, without proof — the covering-map distinction was “postponed”; filled in.)* Three things are claimed: $F$ is a local diffeomorphism (Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]), so is its restriction to $(0, 4\pi)$, and neither map is injective. Two elementary facts about $F$ are used throughout: $F(t) = F(t')$ if and only if $t - t' \in 2\pi\mathbb{Z}$, since cosine and sine together determine an angle up to a multiple of $2\pi$; and every point of $S^1$ is $F(s)$ for exactly one $s$ in any half-open interval of length $2\pi$.
>
> *$F$ is smooth into $S^1$.* Its components $\cos t$ and $\sin t$ are smooth, so $F$ is smooth as a map $\mathbb{R} \to \mathbb{R}^2$; and $\cos^2 t + \sin^2 t = 1$, so its values lie in the regular level set $S^1$, with the smooth structure of Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]. By Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2), with $P = \mathbb{R}$ and $G = F$, $F$ is therefore smooth into $S^1$.
>
> *The neighbourhoods.* Fix $t_0 \in \mathbb{R}$; Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]] asks for neighbourhoods $U \ni t_0$ and $V \ni F(t_0)$ with $F(U) = V$ and $F|_U^V$ smoothly invertible. Let $U = (t_0 - \pi, t_0 + \pi)$ and $V = S^1 \setminus \{F(t_0 + \pi)\}$, which is open in $S^1$ because points of the Hausdorff space $S^1$ are closed. Then $F$ maps $U$ bijectively onto $V$:
> - *injective:* if $t, t' \in U$ and $F(t) = F(t')$, then $t - t' \in 2\pi\mathbb{Z}$ and $|t - t'| < 2\pi$, so $t = t'$;
> - *into $V$:* for $t \in U$, $t - (t_0 + \pi) \in (-2\pi, 0)$ is not a multiple of $2\pi$, so $F(t) \neq F(t_0 + \pi)$;
> - *onto $V$:* a point of $V$ is $F(s)$ for some $s \in [t_0 - \pi, t_0 + \pi)$, and $s \neq t_0 - \pi$ because $F(t_0 - \pi) = F(t_0 + \pi) \notin V$; so $s \in U$.
>
> In particular $F(t_0) \in V$, and $F(U) = V$.
>
> *The local inverse.* The inverse of $F|_U^V$ is the angle chart $\theta : V \to U$ taking values in $U$, which belongs to the smooth structure of $S^1$ (Proposition [[§24 The Circle#^prop-24-1|§24.1]] and the remark on ranges in its proof); here $\theta(q)$ is the unique $s \in U$ with $F(s) = q$. Explicitly, this is the remark's “rotate and add a constant”: let $R$ be the rotation of $\mathbb{R}^2$ by the angle $\alpha = \pi - t_0$, so that $R(F(s)) = F(s + \alpha)$ for all $s$, and let $\varphi_a : U_a = S^1 \setminus \{(1,0)\} \to (0, 2\pi)$ be the angle chart of Example [[§17 Differentiable Structures#^ex-17-4|§17.4]]. Then $R$ maps $V$ onto $S^1 \setminus \{F(t_0 + \pi + \alpha)\} = S^1 \setminus \{F(2\pi)\} = U_a$, and for $q = F(s)$ with $s \in U$ we have $R(q) = F(s + \alpha)$ with $s + \alpha \in (0, 2\pi)$, so
>
> $$
> \varphi_a\big(R(q)\big) - \alpha = (s + \alpha) - \alpha = s = \theta(q) ;
> $$
>
> that is, $\theta = \varphi_a \circ R|_V + (t_0 - \pi)$. So $F|_U^V = \theta^{-1}$, and since the chart $\theta : V \to U$ is a diffeomorphism by Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], so is its inverse $F|_U^V$; its smooth inverse $\theta$ is a local inverse of $F$ at $t_0$.
>
> *The restriction to $(0, 4\pi)$.* It is smooth, as the restriction of the smooth map $F$ to an open subset. For $t_0 \in (0,4\pi)$, replace $U$ by $U' = U \cap (0, 4\pi)$, an open interval containing $t_0$, and $V$ by its image $V' = F(U')$, which is open in $V$ — hence in $S^1$, $V$ being open — because $F|_U^V$ is a homeomorphism (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](3)). Then $F$ maps $U'$ bijectively onto $V'$, with inverse $\theta|_{V'}$, smooth as the restriction of $\theta$ to an open subset.
>
> *Not injective.* Finally $F(t + 2\pi) = F(t)$ for every $t$, since cosine and sine have period $2\pi$; so $F$ is not injective. Nor is its restriction: $\pi$ and $3\pi$ both lie in $(0, 4\pi)$, and $F(\pi) = F(3\pi) = (-1, 0)$.

^pf-ex-35-1

*Uses:* [[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§24 The Circle#^prop-24-1|§24.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]]

![[m591-14-1.svg]]
*The helix is the interval $(0, 4\pi)$, lifted so that $F$ becomes the vertical projection onto the circle. On the orange interval $U$ the projection is a diffeomorphism onto the arc $V$; but the point $q \in V$ has a second preimage $t_1 + 2\pi$, on the other turn and outside $U$. Local invertibility does not see it.*

![[m591-14-a1.gif|420]]

*(Not from lecture; animation added, vault only.)* The point $t$ runs along the helix over $(0, 4\pi)$ and its image $F(t) = (\cos t, \sin t)$ along the circle. On $U$ (orange) $F$ is a diffeomorphism onto the arc $V$, but the same point of $V$ is also $F(t \pm 2\pi)$ (red), on the other turn: a local diffeomorphism that is not injective.

> [!remark]- Connections
> - As a covering map of topological spaces: [[§31 Covering Spaces#^thm-31-2|590 §31.2]] ($\mathbb{R} \to S^1$ is a covering map).

The circle through the course: the circle group $\mathrm{U}(1)$ in [[§11 Topological Groups and Classical Matrix Groups#^ex-11-3|U(1) is the circle]]; the homogeneous space $\mathbb{R}/\mathbb{Z}$ in [[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1|the circle as R/Z]]; three atlases — four charts, stereographic and angle — in [[§17 Differentiable Structures#^ex-17-2|the four-chart atlas]], [[§17 Differentiable Structures#^ex-17-3|the stereographic atlas]] and [[§17 Differentiable Structures#^ex-17-4|the angle atlas]], with [[§17 Differentiable Structures#^rem-17-10|three atlases and one structure]]; $\mathbb{RP}^1$ homeomorphic to it in [[§18 Projective Spaces as Smooth Manifolds#^prop-18-6|The Two Topologies on RPⁿ Agree]]; its external, graph and internal descriptions, and the one smooth structure of its three atlases, in [[§24 The Circle|The Circle]]; and covered by a line, a local diffeomorphism that is not injective, in [[§35 Local Diffeomorphisms#^ex-35-1|the circle covered by a line]].

The projection $S^n \to \mathbb{RP}^n$, a two-to-one local diffeomorphism, is collected in [[§46 Projective Spaces and the Hopf Fibration|§46]].

> [!remark] Remark: Covering Maps
> Uribe noted that $\mathbb{R} \to S^1$ and $S^n \to \mathbb{RP}^n$ are *covering maps*, while $(0, 4\pi) \to S^1$ is a local diffeomorphism that is not: over the point $F(0) = (1,0)$ it has a single preimage, $2\pi$, where every other point of the circle has two. Covering maps were not defined in lecture and the distinction was postponed (“we're running a little bit behind schedule”); it is Lee Ch. 4.

^rem-35-2

> [!remark]- Connections
> - Covering maps are defined in [[§31 Covering Spaces#^def-31-2|590 Def. §31.2]]; the same failure for a half-line, $\mathbb{R}_+ \to S^1$, is [[§31 Covering Spaces#^ex-31-2|590 Ex. §31.2]].
> - Used in Quantum Mechanics: $S^3 \to \mathbb{RP}^3$ is $SU(2) \to SO(3)$; because $SU(2)$ is simply connected ([[Sⁿ is Simply Connected for n ≥ 2|590 §37.3]]) and $SO(3)$ is not ([[§38 Fundamental Group of Some Surfaces#^thm-38-3|590 §38.3]]), the sign of a spinor under a rotation by $2\pi$ cannot be removed — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^rem-c5-2-6|QM ★ Remark: Why the sign cannot be removed]].

The converse direction of the main theorem rests on one theorem from analysis — “that's really what's paying the bills here.”

> [!theorem] Theorem §35.1: Inverse Function Theorem
> Let $W \subseteq \mathbb{R}^n$ be open, $\Phi : W \to \mathbb{R}^n$ smooth, and $a \in W$ with $\Phi'(a)$ invertible. Then there are open sets $U_0 \ni a$ in $W$ and $V_0 \ni \Phi(a)$ in $\mathbb{R}^n$ such that $\Phi(U_0) = V_0$ and $\Phi|_{U_0} : U_0 \to V_0$ is bijective with smooth inverse.
>
> *Lee: Theorem C.34*

^thm-35-1

> [!proof]+ Proof (to be filled)
> Taken from analysis, not proved in this course (Lee, Theorem C.34; [[Inverse Function Theorem (several variables)|452 §16.2]] proves the two-variable case). To be filled.

^pf-35-1

> [!remark]- Connections
> - Home in analysis (the two-variable version): [[Inverse Function Theorem (several variables)|452 §16.2]].
> - The implicit function theorem it should not be confused with: [[§7 The Regular Value Theorem#^thm-7-1|§7.1]].

Lee, Theorem C.34; taken from analysis, not proved in the course. It should not be confused with the *implicit* function theorem of [[§7 The Regular Value Theorem|§7]] — the board's “IFT” now means the inverse one. Each theorem can be derived from the other.

> [!theorem] Theorem §35.2: Local Diffeomorphisms Are Detected by the Differential
> A smooth map $F : M \to N$ is a local diffeomorphism if and only if $F_{*p} : T_pM \to T_{F(p)}N$ is bijective for every $p \in M$.
>
> *Lee: Theorem 4.5 and Proposition 4.8*

^thm-35-2

> [!proof]+ Proof
> *(Lecture 10. The forward direction was supplied by a student at Uribe's prompting — use the local inverse and the chain rule; for the converse the inverse function theorem “is really what's paying the bills here.” The identification of $(F|_U^V)_{\ast p}$ with $F_{\ast p}$ is a completion.)* ($\Rightarrow$) Fix $p \in M$, and let $U$, $V$ and the local inverse $G : V \to U$ at $p$ be as in Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]], so that $G \circ F|_U^V = \mathrm{id}_U$ and $F|_U^V \circ G = \mathrm{id}_V$. By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), applied to these two composites at $p$ and at $F(p)$ respectively, together with $(\mathrm{id})_\ast = \mathrm{id}$,
>
> $$
> G_{\ast F(p)} \circ (F|_U^V)_{\ast p} = (\mathrm{id}_U)_{\ast p} = \mathrm{id}, \qquad (F|_U^V)_{\ast p} \circ G_{\ast F(p)} = (\mathrm{id}_V)_{\ast F(p)} = \mathrm{id},
> $$
>
> so $(F|_U^V)_{\ast p} : T_pU \to T_{F(p)}V$ is bijective with inverse $G_{\ast F(p)}$. Under the identifications $T_pU = T_pM$ and $T_{F(p)}V = T_{F(p)}N$ of Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], $(F|_U^V)_{\ast p}$ is $F_{\ast p}$, again by the Chain Rule applied to $F \circ \iota_U = \iota_V \circ F|_U^V$, where $\iota_U : U \hookrightarrow M$ and $\iota_V : V \hookrightarrow N$ are the inclusions. Explicitly, the Chain Rule gives $F_{\ast p} \circ (\iota_U)_{\ast p} = (\iota_V)_{\ast F(p)} \circ (F|_U^V)_{\ast p}$, and $(\iota_U)_{\ast p}$ is invertible (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), so
>
> $$
> F_{\ast p} = (\iota_V)_{\ast F(p)} \circ (F|_U^V)_{\ast p} \circ \big((\iota_U)_{\ast p}\big)^{-1},
> $$
>
> a composite of three bijections (the outer two by Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]). So $F_{\ast p}$ is bijective, for every $p \in M$.
>
> ($\Leftarrow$) Fix $p$; we must produce neighbourhoods $U' \ni p$, $V' \ni F(p)$ with $F(U') = V'$ and a smooth inverse of $F|_{U'}^{V'}$. Choose smooth charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ with $F(U) \subseteq V$, by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]]: take any chart $(V, \psi)$ at $F(p)$ and any chart $(U_1, \varphi_1)$ at $p$, and restrict $\varphi_1$ to the open set $U = U_1 \cap F^{-1}(V)$, open because $F$ is continuous. Let $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$, smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]].
>
> A bijective linear map forces $\dim M = \dim N$: $F_{\ast p}$ is a bijection $T_pM \to T_{F(p)}N$ between spaces of dimensions $m = \dim M$ and $n = \dim N$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), and rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) gives $m = \dim\ker F_{\ast p} + \operatorname{rank} F_{\ast p} = 0 + n$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] the matrix of $F_{\ast p}$ is the square matrix $\tilde F'(\varphi(p))$, written out in the standard coordinates $r^1, \ldots, r^n$ of $\varphi(U)$ as
>
> $$
> \tilde F'\big(\varphi(p)\big) = \begin{pmatrix} \dfrac{\partial \tilde F^1}{\partial r^1}\big(\varphi(p)\big) & \cdots & \dfrac{\partial \tilde F^1}{\partial r^n}\big(\varphi(p)\big) \\ \vdots & \ddots & \vdots \\ \dfrac{\partial \tilde F^n}{\partial r^1}\big(\varphi(p)\big) & \cdots & \dfrac{\partial \tilde F^n}{\partial r^n}\big(\varphi(p)\big) \end{pmatrix} ;
> $$
> so the latter is invertible, since its rank is the rank of $F_{\ast p}$, namely $n$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)).
>
> By the Inverse Function Theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]), applied to $\Phi = \tilde F$ on $W = \varphi(U)$ at $a = \varphi(p)$, there are open sets $\tilde A \ni \varphi(p)$ in $\varphi(U)$ and $\tilde B \ni \tilde F(\varphi(p))$ such that $\tilde F(\tilde A) = \tilde B$ and $\tilde F|_{\tilde A} : \tilde A \to \tilde B$ is bijective with smooth inverse; note $\tilde B = \tilde F(\tilde A) \subseteq \psi(V)$. Put $U' = \varphi^{-1}(\tilde A)$ and $V' = \psi^{-1}(\tilde B)$, neighbourhoods of $p$ and $F(p)$: they are open because $\varphi$ and $\psi$ are homeomorphisms onto open sets — “shrinking $\varphi(U)$ is the same as shrinking $U$.” On $U$ we have $F = \psi^{-1} \circ \tilde F \circ \varphi$, by the definition of $\tilde F$ and $F(U) \subseteq V$; so
>
> $$
> F(U') = \psi^{-1}\big(\tilde F(\varphi(U'))\big) = \psi^{-1}\big(\tilde F(\tilde A)\big) = \psi^{-1}(\tilde B) = V' ,
> $$
>
> and the map $G = \varphi^{-1} \circ (\tilde F|_{\tilde A})^{-1} \circ \psi|_{V'} : V' \to U'$ is the inverse of $F|_{U'}^{V'}$. Indeed, for $y \in V'$ and $x \in U'$ (so that $\psi(y) \in \tilde B$ and $\varphi(x) \in \tilde A$),
>
> $$
> F\big(G(y)\big) = \psi^{-1}\Big(\tilde F\big((\tilde F|_{\tilde A})^{-1}(\psi(y))\big)\Big) = \psi^{-1}\big(\psi(y)\big) = y, \qquad G\big(F(x)\big) = \varphi^{-1}\Big((\tilde F|_{\tilde A})^{-1}\big(\tilde F(\varphi(x))\big)\Big) = \varphi^{-1}\big(\varphi(x)\big) = x .
> $$
>
> So
>
> $$
> \big(F|_{U'}^{V'}\big)^{-1} = \varphi^{-1} \circ \big(\tilde F|_{\tilde A}\big)^{-1} \circ \psi|_{V'},
> $$
>
> a composite of diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), hence smooth: $\psi|_{V'} : V' \to \tilde B$ and $\varphi^{-1} : \tilde A \to U'$ are restrictions of the chart diffeomorphisms $\psi$ and $\varphi^{-1}$ to open sets, $(\tilde F|_{\tilde A})^{-1}$ is smooth in the Euclidean sense and hence as a map of manifolds (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]), and a composite of smooth maps is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). So $G$ is a local inverse at $p$, and as $p$ was arbitrary, $F$ is a local diffeomorphism.

^pf-35-2

*Uses:* [[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§19 Smooth Functions and Smooth Maps#^lem-19-3|§19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]

![[m591-14-2.svg]]
*The converse in one picture. Downstairs the Inverse Function Theorem supplies $\tilde F^{-1}$; the charts carry it upstairs as the local inverse $G = \varphi^{-1} \circ \tilde F^{-1} \circ \psi$. The only input from the hypothesis is that the bottom arrow has an invertible Jacobian at $\varphi(p)$ — which is where Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] enters.*

A student asked why $\tilde F'(\varphi(p))$ is invertible; Uribe's answer was the lemma just cited: the Jacobian *is* the matrix of $F_{\ast p}$ in coordinate bases, and $F_{\ast p}$ is bijective by hypothesis. The practical content of the theorem is that “being a local diffeomorphism is detectable” by computing one Jacobian at each point, rather than by exhibiting local inverses.

> [!theorem] Corollary §35.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms
> A smooth map $F : M \to N$ is a diffeomorphism if and only if it is a bijective local diffeomorphism. Consequently, a smooth bijection with $F_{*p}$ bijective at every $p \in M$ is a diffeomorphism.
>
> *Lee: Proposition 4.6*

^cor-35-3

> [!proof]+ Proof
> *($\Rightarrow$)* A diffeomorphism is a local diffeomorphism with $U = M$ and $V = N$: these are neighbourhoods of every $p$ and $F(p)$, $F(M) = N$ because $F$ is surjective, and $F|_M^N = F$ has the smooth inverse $F^{-1}$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]). It is bijective by definition.
>
> *($\Leftarrow$)* Conversely, let $F$ be a bijective local diffeomorphism; $F$ is smooth and bijective, so by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]] it remains to show that $F^{-1} : N \to M$ is smooth. Given $q \in N$, let $p = F^{-1}(q)$ and let $G : V \to U$ be a local inverse at $p$ (Definition [[§35 Local Diffeomorphisms#^def-35-1|§35.1]]), so $V$ is an open neighbourhood of $q = F(p)$. For $y \in V$, $G(y) \in U$ and $F(G(y)) = (F|_U^V \circ G)(y) = y$; also $F(F^{-1}(y)) = y$; so $G(y) = F^{-1}(y)$ because $F$ is injective. Thus $F^{-1}$ agrees on the open neighbourhood $V$ of $q$ with the smooth map $G$.
>
> As $q$ was arbitrary, the sets $V$ obtained in this way form an open cover of $N$, on each of which $F^{-1}$ equals a smooth, in particular continuous, map. So $F^{-1}$ is continuous and smooth, since both properties are local: for continuity, the preimage under $F^{-1}$ of an open $O \subseteq M$ is the union over the cover of the sets $G^{-1}(O \cap U)$, each open in an open $V$; for smoothness, Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]] is checked with charts at each point, and on a chart domain inside $V$ the coordinate representations of $F^{-1}$ and of $G$ coincide, so they are smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]. Hence $F$ is a diffeomorphism.
>
> *The last sentence.* A smooth bijection with $F_{\ast p}$ bijective at every $p$ is a local diffeomorphism by Theorem [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]]; being bijective, it is a diffeomorphism by the equivalence just proved.

^pf-35-3

*Uses:* [[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]], [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]

> [!remark] Remark
> Not stated in lecture. Injectivity is the entire difference between the two notions, as the helix of Example [[§35 Local Diffeomorphisms#^ex-35-1|§35.1]] shows: there every local inverse exists, but they cannot be assembled into a global one, because the second preimage of $q$ lies outside the domain of the local inverse. The same argument shows that a bijective local homeomorphism is a homeomorphism.

^rem-35-3
