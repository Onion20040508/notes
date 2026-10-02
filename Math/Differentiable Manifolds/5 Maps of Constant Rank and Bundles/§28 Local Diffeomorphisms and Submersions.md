---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 28
tags: [differentiable-manifolds, math591]
---
← [[§27 Tangent Spaces III꞉ The Cotangent Space]] · ↑ [[· 5 Maps of Constant Rank and Bundles]] · [[§29 Submanifolds]] →

*Stage: maps — Properties of the linear maps $F_{*p}$ control the local behaviour of $F$ itself.*

*References: Lee Ch. 4. Lecture 10.*

Three special types of smooth maps $F : M \to N$ are singled out by the linear algebra of their differentials: *local diffeomorphisms*, whose differentials are bijective; *submersions*, whose differentials are surjective; and *immersions*, whose differentials are injective. The theme of the section is that in each case a property of the linear maps $F_{*p}$ — computable from a Jacobian — controls the behaviour of $F$ itself near $p$. Immersions, listed with the others in Lecture 10, were treated only in Lecture 13, after the tangent bundle, and have their own section, [[§32 Immersions|§32]]; everything up to the tangent bundle is the theory of submersions. “That's why we're discussing them in this context.”

## Local Diffeomorphisms

> [!definition] Definition §28.1: Local Diffeomorphism
> A smooth map $F : M \to N$ is a **local diffeomorphism** if for every $p \in M$ there are neighbourhoods $U$ of $p$ and $V$ of $F(p)$ with $F(U) = V$ such that $F|_U^V : U \to V$ — the restriction of $F$ to $U$, regarded as a map onto $V$ — has a smooth inverse. Such an inverse $G : V \to U$ is a **local inverse** of $F$ at $p$.
>
> *Lee: Ch. 2 and Ch. 4*

^def-28-1

> [!remark] Remark
> Neighbourhoods are open ([[§1 Point-Set Topology Review#^rem-1-4|§1]]). A local diffeomorphism need not be injective: the local inverses are local, and different ones need not fit together. The examples show both finite-to-one and infinite-to-one behaviour.

^rem-28-1

> [!example] Example §28.1: The Circle Covered by a Line
> $F : \mathbb{R} \to S^1$, $F(t) = (\cos t, \sin t)$, is a local diffeomorphism, and so is its restriction to $(0, 4\pi)$. Neither is injective.
>
> *Lee: cf. Ch. 4, Smooth Covering Maps*

^ex-28-1

> [!proof]+ Proof
> *(Stated in Lecture 10 as an example, without proof — the covering-map distinction was “postponed”; filled in.)* $F$ is smooth into $\mathbb{R}^2$ with values in $S^1$, hence smooth into $S^1$ by Lemma [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]](2). Fix $t_0$ and let $U = (t_0 - \pi, t_0 + \pi)$ and $V = S^1 \setminus \{F(t_0 + \pi)\}$. Then $F$ maps $U$ bijectively onto $V$, and its inverse is the angle chart $\theta : V \to U$ taking values in $U$, which belongs to the smooth structure of $S^1$ (Proposition [[§16 Manifolds in Euclidean Space#^prop-16-4|§16.4]] and the remark on ranges in its proof). So $F|_U^V = \theta^{-1}$ is a diffeomorphism by Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]. For $t_0 \in (0,4\pi)$, replace $U$ by $U \cap (0, 4\pi)$ and $V$ by its image, which is open because $F|_U^V$ is a homeomorphism. Finally $F(t + 2\pi) = F(t)$.

^pf-ex-28-1

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-1|Def. §28.1]], [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]], [[§16 Manifolds in Euclidean Space#^prop-16-4|§16.4]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]

![[m591-14-1.svg]]
*The helix is the interval $(0, 4\pi)$, lifted so that $F$ becomes the vertical projection onto the circle. On the orange interval $U$ the projection is a diffeomorphism onto the arc $V$; but the point $q \in V$ has a second preimage $t_1 + 2\pi$, on the other turn and outside $U$. Local invertibility does not see it.*

> [!remark]- Connections
> - As a covering map of topological spaces: [[§24 Covering Spaces#^thm-24-2|590 §24.2]] ($\mathbb{R} \to S^1$ is a covering map).

> [!example] Example §28.2: Spheres Cover Projective Spaces
> The projection $\pi : S^n \to \mathbb{RP}^n$, $x \mapsto [x]$, is a local diffeomorphism, exactly two-to-one.

^ex-28-2

> [!proof]+ Proof
> *(Stated in Lecture 10 as an example, without proof — the covering-map distinction was “postponed”; filled in.)* Use coordinates $x_0, \ldots, x_n$ on $\mathbb{R}^{n+1}$, matching the charts $(U_i, \varphi_i)$ of Corollary [[§14 Projective Spaces as Smooth Manifolds#^cor-14-5|§14.5]], and give $S^n = \{|x|^2 = 1\}$ its level-set structure. For each $i$ and $\varepsilon = \pm 1$, the open hemisphere $U_i^\varepsilon = \{x \in S^n \mid \varepsilon x_i > 0\}$ is mapped by $\pi$ bijectively onto $U_i = \{[x] \mid x_i \neq 0\}$, since a line not contained in $\{x_i = 0\}$ meets $U_i^\varepsilon$ exactly once. In the chart $\varphi_i$,
>
> $$
> \varphi_i \circ \pi(x) = (x_k/x_i)_{k \neq i},
> $$
>
> the restriction of a smooth map on the open set $\{x_i \neq 0\} \subseteq \mathbb{R}^{n+1}$, hence smooth by Lemma [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]](1). Its inverse is $y \mapsto \varepsilon\,\hat y/|\hat y|$, where $\hat y$ is $y$ with a $1$ inserted in slot $i$. This is smooth into $\mathbb{R}^{n+1}$ with values in $U_i^\varepsilon$, hence smooth into $S^n$ by Lemma [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]](2). So $\varphi_i \circ \pi$ is a diffeomorphism of $U_i^\varepsilon$ onto $\mathbb{R}^n$, and $\pi|_{U_i^\varepsilon} = \varphi_i^{-1} \circ (\varphi_i \circ \pi)$ is a diffeomorphism onto $U_i$ by Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]. The hemispheres cover $S^n$, and $\pi(x) = \pi(-x)$.

^pf-ex-28-2

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-1|Def. §28.1]], [[§14 Projective Spaces as Smooth Manifolds#^cor-14-5|§14.5]], [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]

> [!remark]- Connections
> - As a covering map of topological spaces, for $n = 2$: [[§28 Fundamental Group of Some Surfaces#^thm-28-1|590 §28.1]] ($S^2 \to P^2$ is a covering map).

> [!remark] Remark: Covering Maps
> Uribe noted that $\mathbb{R} \to S^1$ and $S^n \to \mathbb{RP}^n$ are *covering maps*, while $(0, 4\pi) \to S^1$ is a local diffeomorphism that is not: over the point $F(0) = (1,0)$ it has a single preimage, $2\pi$, where every other point of the circle has two. Covering maps were not defined in lecture and the distinction was postponed (“we're running a little bit behind schedule”); it is Lee Ch. 4.

^rem-28-2

> [!remark]- Connections
> - Covering maps are defined in [[§24 Covering Spaces#^def-24-2|590 Def. §24.2]]; the same failure for a half-line, $\mathbb{R}_+ \to S^1$, is [[§24 Covering Spaces#^ex-24-2|590 Ex. §24.2]].
> - Used in Quantum Mechanics: $S^3 \to \mathbb{RP}^3$ is $SU(2) \to SO(3)$; because $SU(2)$ is simply connected and $SO(3)$ is not, the sign of a spinor under a rotation by $2\pi$ cannot be removed — [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^rem-c5-2-6|QM ★ Remark: Why the sign cannot be removed]].

The converse direction of the main theorem rests on one theorem from analysis — “that's really what's paying the bills here.”

> [!theorem] Theorem §28.1: Inverse Function Theorem
> Let $W \subseteq \mathbb{R}^n$ be open, $\Phi : W \to \mathbb{R}^n$ smooth, and $a \in W$ with $\Phi'(a)$ invertible. Then there are open sets $U_0 \ni a$ in $W$ and $V_0 \ni \Phi(a)$ in $\mathbb{R}^n$ such that $\Phi(U_0) = V_0$ and $\Phi|_{U_0} : U_0 \to V_0$ is bijective with smooth inverse.
>
> *Lee: Theorem C.34*

^thm-28-1

> [!remark]- Connections
> - Home in analysis (the two-variable version): [[Inverse Function Theorem (several variables)|452 §13.2]].
> - The implicit function theorem it should not be confused with: [[§7 The Regular Value Theorem#^thm-7-1|§7.1]].

> [!proof]+ Proof (to be filled)
> Taken from analysis, not proved in this course (Lee, Theorem C.34; [[Inverse Function Theorem (several variables)|452 §13.2]] proves the two-variable case). To be filled.

^pf-28-1

Lee, Theorem C.34; taken from analysis, not proved in the course. It should not be confused with the *implicit* function theorem of [[§7 The Regular Value Theorem|§7]] — the board's “IFT” now means the inverse one. Each theorem can be derived from the other.

> [!theorem] Theorem §28.2: Local Diffeomorphisms Are Detected by the Differential
> A smooth map $F : M \to N$ is a local diffeomorphism if and only if $F_{*p} : T_pM \to T_{F(p)}N$ is bijective for every $p \in M$.
>
> *Lee: Theorem 4.5 and Proposition 4.8*

^thm-28-2

> [!proof]+ Proof
> *(Lecture 10. The forward direction was supplied by a student at Uribe's prompting — use the local inverse and the chain rule; for the converse the inverse function theorem “is really what's paying the bills here.” The identification of $(F|_U^V)_{*p}$ with $F_{*p}$ is a completion.)* ($\Rightarrow$) Let $G : V \to U$ be a local inverse at $p$, so that $G \circ F|_U^V = \mathrm{id}_U$ and $F|_U^V \circ G = \mathrm{id}_V$. By the Chain Rule (Theorem [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]]),
>
> $$
> G_{*F(p)} \circ (F|_U^V)_{*p} = \mathrm{id}, \qquad (F|_U^V)_{*p} \circ G_{*F(p)} = \mathrm{id},
> $$
>
> so $(F|_U^V)_{*p}$ is bijective with inverse $G_{*F(p)}$. Under the identifications $T_pU = T_pM$ and $T_{F(p)}V = T_{F(p)}N$ of Lemma [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|§23.8]], $(F|_U^V)_{*p}$ is $F_{*p}$, again by the Chain Rule applied to $F \circ \iota_U = \iota_V \circ F|_U^V$.
>
> ($\Leftarrow$) Fix $p$, and choose charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ with $F(U) \subseteq V$. A bijective linear map forces $\dim M = \dim N$, and by Theorem [[§25 The Differential in Coordinates#^thm-25-2|§25.2]] the matrix of $F_{*p}$ is the square matrix $\tilde F'(\varphi(p))$; so the latter is invertible. By the Inverse Function Theorem there are open sets $\tilde A \ni \varphi(p)$ in $\varphi(U)$ and $\tilde B \ni \tilde F(\varphi(p))$ such that $\tilde F|_{\tilde A} : \tilde A \to \tilde B$ is bijective with smooth inverse. Put $U' = \varphi^{-1}(\tilde A)$ and $V' = \psi^{-1}(\tilde B)$, neighbourhoods of $p$ and $F(p)$; since $\varphi$ is a homeomorphism, “shrinking $\varphi(U)$ is the same as shrinking $U$.” On $U'$ we have $F = \psi^{-1} \circ \tilde F \circ \varphi$, so $F(U') = V'$ and
>
> $$
> \big(F|_{U'}^{V'}\big)^{-1} = \varphi^{-1} \circ \big(\tilde F|_{\tilde A}\big)^{-1} \circ \psi|_{V'},
> $$
>
> a composite of diffeomorphisms (Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]), hence smooth.

^pf-28-2

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-1|Def. §28.1]], [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§23 Derivations and the Abstract Tangent Space#^lem-23-8|§23.8]], [[§25 The Differential in Coordinates#^thm-25-2|§25.2]], [[§28 Local Diffeomorphisms and Submersions#^thm-28-1|§28.1]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]]

![[m591-14-2.svg]]
*The converse in one picture. Downstairs the Inverse Function Theorem supplies $\tilde F^{-1}$; the charts carry it upstairs as the local inverse $G = \varphi^{-1} \circ \tilde F^{-1} \circ \psi$. The only input from the hypothesis is that the bottom arrow has an invertible Jacobian at $\varphi(p)$ — which is where Theorem [[§25 The Differential in Coordinates#^thm-25-2|§25.2]] enters.*

A student asked why $\tilde F'(\varphi(p))$ is invertible; Uribe's answer was the lemma just cited: the Jacobian *is* the matrix of $F_{*p}$ in coordinate bases, and $F_{*p}$ is bijective by hypothesis. The practical content of the theorem is that “being a local diffeomorphism is detectable” by computing one Jacobian at each point, rather than by exhibiting local inverses.

> [!theorem] Corollary §28.3: Diffeomorphisms Are the Bijective Local Diffeomorphisms
> A smooth map $F : M \to N$ is a diffeomorphism if and only if it is a bijective local diffeomorphism. Consequently, a smooth bijection with $F_{*p}$ bijective at every $p \in M$ is a diffeomorphism.
>
> *Lee: Proposition 4.6*

^cor-28-3

> [!proof]+ Proof
> A diffeomorphism is a local diffeomorphism with $U = M$ and $V = N$. Conversely, let $F$ be a bijective local diffeomorphism. Given $q \in N$, let $p = F^{-1}(q)$ and let $G : V \to U$ be a local inverse at $p$. For $y \in V$, $G(y) \in U$ and $F(G(y)) = y$, so $G(y) = F^{-1}(y)$ because $F$ is injective. Thus $F^{-1}$ agrees on the open neighbourhood $V$ of $q$ with the smooth map $G$. As $q$ was arbitrary, $F^{-1}$ is continuous and smooth, since both properties are local. The last sentence follows from Theorem [[§28 Local Diffeomorphisms and Submersions#^thm-28-2|§28.2]].

^pf-28-3

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-1|Def. §28.1]], [[§28 Local Diffeomorphisms and Submersions#^thm-28-2|§28.2]]

> [!remark] Remark
> Not stated in lecture. Injectivity is the entire difference between the two notions, as the helix of Example [[§28 Local Diffeomorphisms and Submersions#^ex-28-1|§28.1]] shows: there every local inverse exists, but they cannot be assembled into a global one, because the second preimage of $q$ lies outside the domain of the local inverse. The same argument shows that a bijective local homeomorphism is a homeomorphism.

^rem-28-3

## Submersions

> [!definition] Definition §28.2: Submersion and Immersion
> Let $F : M \to N$ be smooth and $p \in M$. $F$ is a **submersion at $p$** if $F_{*p}$ is onto, and a **submersion** if it is a submersion at every point. $F$ is an **immersion at $p$** if $F_{*p}$ is injective, and an **immersion** if it is one at every point.
>
> *Lee: Ch. 4, Maps of Constant Rank*

^def-28-2

> [!remark]- Connections
> - The lecture's definition of immersion, with its normal form: [[§32 Immersions#^def-32-1|Def. §32.1]], [[§32 Immersions#^thm-32-1|§32.1]].
> - Submersion at $p$ = regular point: [[§25 The Differential in Coordinates#^def-25-1|Def. §25.1]], [[§28 Local Diffeomorphisms and Submersions#^def-28-3|Def. §28.3]].

The submersion half is the lecture's definition. Immersions were listed as the third special type and treated in Lecture 13 ([[§32 Immersions|§32]]); the definition is recorded here in Lee's form so that the three types can be compared. In the language of Definition [[§25 The Differential in Coordinates#^def-25-1|§25.1]], $F$ is a submersion at $p$ exactly when $p$ is a regular point.

> [!theorem] Proposition §28.4: Dimension Constraints
> Let $F : M \to N$ be smooth, $m = \dim M$, $n = \dim N$, and $p \in M$.
> 1. If $F$ is a submersion at $p$ then $n \le m$; if $F$ is an immersion at $p$ then $m \le n$.
> 2. $F$ is a local diffeomorphism if and only if it is both a submersion and an immersion; in that case $m = n$.
> 3. If $m = n$ and $F$ is a submersion, or an immersion, at every point, then $F$ is a local diffeomorphism.
>
> *Lee: Proposition 4.8*

^prop-28-4

> [!proof]+ Proof
> (1) By rank–nullity (Proposition [[§17 Linear Algebra Toolkit#^prop-17-1|§17.1]](1)), a surjective linear map $T_pM \to T_{F(p)}N$ forces $n \le m$, and an injective one forces $m \le n$. (2) A linear map is bijective if and only if it is injective and surjective, so this is Theorem [[§28 Local Diffeomorphisms and Submersions#^thm-28-2|§28.2]]; then (1) gives $m = n$. (3) Between spaces of the same finite dimension, a linear map is injective iff surjective iff bijective (Proposition [[§17 Linear Algebra Toolkit#^prop-17-1|§17.1]](1)); apply Theorem [[§28 Local Diffeomorphisms and Submersions#^thm-28-2|§28.2]].

^pf-28-4

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-2|Def. §28.2]], [[§17 Linear Algebra Toolkit#^prop-17-1|§17.1]], [[§28 Local Diffeomorphisms and Submersions#^thm-28-2|§28.2]], [[Fundamental theorem of linear maps|LADR 3.21]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!example] Example §28.3: Projections Are Submersions
> The projection $\pi : \mathbb{R}^k \times \mathbb{R}^l \to \mathbb{R}^k$, $(x, y) \mapsto x$, is a submersion.

^ex-28-3

> [!proof]+ Proof
> By Proposition [[§25 The Differential in Coordinates#^prop-25-5|§25.5]] the differential is the Jacobian $\big(I_k \mid 0\big)$, a $k \times (k+l)$ matrix of rank $k$.

^pf-ex-28-3

*Uses:* [[§25 The Differential in Coordinates#^prop-25-5|§25.5]], [[§28 Local Diffeomorphisms and Submersions#^def-28-2|Def. §28.2]]

**Transcription note.** Page 28 of the handwritten notes writes the projection as $\mathbb{R}^m \times \mathbb{R}^l \to \mathbb{R}^k$; for a projection onto a factor the factor must be the target, $\mathbb{R}^k \times \mathbb{R}^l \to \mathbb{R}^k$. Projections of *product manifolds* $M_1 \times M_2 \to M_1$ are submersions for the same reason, but that needs the tangent space of a product — “they will be direct sums of tangent spaces” — which Uribe postponed to the next lecture.

Lecture 11 supplied it (Theorem [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|§26.4]]):

> [!example] Example §28.4: Projections of Product Manifolds Are Submersions
> The projection $\pi_1 : M_1 \times M_2 \to M_1$ is a submersion, and so is $\pi_2$.
>
> *Lee: Proposition 3.14*

^ex-28-4

> [!proof]+ Proof
> $\pi_{1*}\big(\Theta(v, w)\big) = \pi_{1*}\iota_{1*}v + \pi_{1*}\iota_{2*}w = v$, by the proof of Theorem [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|§26.4]]; so $\pi_{1*}$ is onto $T_{p_1}M_1$.

^pf-ex-28-4

*Uses:* [[§26 Tangent Vectors as Velocities of Curves#^thm-26-4|§26.4]], [[§28 Local Diffeomorphisms and Submersions#^def-28-2|Def. §28.2]]

> [!example] Example §28.5: The Projection $S^{2n+1} \to \mathbb{CP}^n$
> The projection $S^{2n+1} \to \mathbb{CP}^n$ of [[§3 Subspaces and Products|§3]] is a submersion.
>
> *Lee: Problem 4-5(a)*

^ex-28-5

*Uses:* [[§30 Fibrations#^ex-30-1|Ex. §30.1]], [[§30 Fibrations#^prop-30-1|§30.1]]

> [!remark]- Connections
> - Proved in §30, as a consequence of the local triviality of the Hopf fibration: [[§30 Fibrations#^ex-30-1|Ex. §30.1]] with [[§30 Fibrations#^prop-30-1|§30.1]](2).

Stated in lecture as an example (“the projection you worked with from a sphere to complex projective space”); not yet proved. The dimensions are consistent, $2n \le 2n+1$. A proof needs the differential of a map *out of* a level set in terms of the ambient Jacobian, which Lemma [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]] makes available for smoothness but not yet for differentials.

> [!definition] Definition §28.3: Regular Points and Critical Points
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$.
> 1. $p \in M$ is a **regular point** of $F$ if $F$ is a submersion at $p$, i.e. $F_{*p}$ is onto — which forces $n \le m$. Otherwise $p$ is a **critical point**, also called a **singular point**.
> 2. $q \in N$ is a **regular value** of $F$ if $F$ is a submersion at every $p \in F^{-1}(q)$, and a **critical value** otherwise.
> 3. In particular every $q \notin F(M)$ is a regular value: its preimage is empty, and “everything is true for the empty set.”
>
> These are the notions of Definition [[§25 The Differential in Coordinates#^def-25-1|§25.1]], now with critical points and the empty-preimage convention made explicit; for maps between open subsets of Euclidean spaces they are those of Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]].

^def-28-3

> [!remark]- Connections
> - The two earlier definitions of regular point/value: [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]] (Euclidean, Lecture 3) and [[§25 The Differential in Coordinates#^def-25-1|Def. §25.1]] (manifolds, via rank).

Uribe called (3) “kind of a trivial way to be [regular], but important”: it matters in Sard's theorem, about the set of regular values, which is still to come. **Transcription note.** Page 29 of the handwritten notes has “if $q \in \operatorname{Im} F$, then $q$ is regular”; the audio has “if $q$ is not in the image of $F$”, as in (3). The same page writes the preimage in (2) as $F^{-1}(p)$ for $F^{-1}(q)$.

> [!theorem] Proposition §28.5: Critical Points of Real-Valued Functions
> Let $f : M \to \mathbb{R}$ be smooth. Then $df_p$ is either onto or zero, so
>
> $$
> p \text{ is a critical point of } f \iff df_p = 0 \iff \frac{\partial f}{\partial x^i}(p) = 0 \text{ for all } i,
> $$
>
> in any chart at $p$.
>
> *Lee: Exercise 11.24*

^prop-28-5

> [!proof]+ Proof
> The image of the linear map $df_p$ is a subspace of the one-dimensional $T_{f(p)}\mathbb{R} \cong \mathbb{R}$ (Definition [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|§27.1]]), so it is $0$ or everything — “dimensions of images cannot be fractional.” The second equivalence is Lemma [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]].

^pf-28-5

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-3|Def. §28.3]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^def-27-1|Def. §27.1]], [[§27 Tangent Spaces III꞉ The Cotangent Space#^lem-27-2|§27.2]]

> [!remark]- Connections
> - In $\mathbb{R}^n$, critical points are where extrema can occur: [[§14 Optimization and Lagrange Multipliers#^thm-14-1|452 §14.1]] (Fermat's theorem).

This is the definition of critical point Uribe sent to the class by email, and it agrees with Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]] for $m = 1$: there $p$ is regular iff $\nabla F(p) \ne 0$.

> [!theorem] Lemma §28.6: Diffeomorphisms onto Open Sets Are Charts
> Let $U \subseteq M$ be open and $\hat\varphi : U \to \mathbb{R}^m$ smooth, with $\hat\varphi(U)$ open and $\hat\varphi : U \to \hat\varphi(U)$ a diffeomorphism. Then $(U, \hat\varphi)$ is a smooth chart of $M$.
>
> *Lee: cf. Ch. 2, Diffeomorphisms*

^lem-28-6

> [!proof]+ Proof
> It is a homeomorphism onto an open subset of $\mathbb{R}^m$, so it is a chart. For any smooth chart $(W, \chi)$ of $M$, the transition maps $\hat\varphi \circ \chi^{-1}$ and $\chi \circ \hat\varphi^{-1}$ are coordinate representations of $\hat\varphi$ and $\hat\varphi^{-1}$, smooth because these maps are (Proposition [[§15 Smooth Functions and Smooth Maps#^prop-15-2|§15.2]]). So $(U, \hat\varphi)$ is compatible with every chart of the maximal atlas, and therefore belongs to it (Theorem [[§13 Differentiable Structures#^thm-13-5|§13.5]]).

^pf-28-6

*Uses:* [[§15 Smooth Functions and Smooth Maps#^prop-15-2|§15.2]], [[§13 Differentiable Structures#^thm-13-5|§13.5]]

> [!theorem] Theorem §28.7: Local Normal Form for Submersions
> Let $F : M \to N$ be a submersion at $p$, with $\dim M = m$ and $\dim N = n$. Then there are charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $F(p)$ with $F(U) \subseteq V$ in which the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$ is the projection onto the first $n$ coordinates:
>
> $$
> \tilde F\big(r^1, \ldots, r^m\big) = \big(r^1, \ldots, r^n\big).
> $$
>
> Equivalently, with coordinate functions $x^i = r^i \circ \varphi$ on $U$ and $y^j = r^j \circ \psi$ on $V$: $\;y^j \circ F = x^j$ on $U$ for $j = 1, \ldots, n$. In particular $n \le m$.
>
> *Lee: Theorem 4.12, the rank theorem*

^thm-28-7

> [!remark]- Connections
> - The counterpart for immersions: [[§32 Immersions#^thm-32-1|§32.1]]. The main application: the regular value theorem for manifolds, [[§29 Submanifolds#^thm-29-6|§29.6]].

Stated in Lecture 10 and proved in Lecture 11, below. The inequality $n \le m$ needs no theorem — a surjective linear map cannot raise dimension — but the normal form does: it says that every submersion, in suitable coordinates, *is* a projection.

![[m591-14-3.svg]]
*The normal form as a square: in the charts $\varphi$ and $\psi$ of the theorem, $F$ becomes the projection $(r^1, \ldots, r^m) \mapsto (r^1, \ldots, r^n)$.*

![[m591-14-4.svg]]
*What the normal form says, for $m = 2$ and $n = 1$. Left: near $p$ the fibres $F^{-1}(c)$ of a submersion are curves, one through each point, which $F$ collapses to the points of an interval. Right: in the charts of the theorem the fibres are straightened into vertical lines, and $\tilde F$ forgets the second coordinate. Every submersion looks, locally and up to a change of coordinates, like the projection of Example [[§28 Local Diffeomorphisms and Submersions#^ex-28-3|§28.3]].*

*Lecture 11. “Back to submersions.” Uribe now made the vocabulary official, with the letters matched to the dimensions: $\dim M = m$ and $\dim N = n$. (In [[§7 The Regular Value Theorem|§7]], following the earlier lecture, $F : \mathbb{R}^N \to \mathbb{R}^m$ had $m$ as the dimension of the target.)*

Uribe singled out Lemma [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|§28.6]] as “an intellectual step that should not be overlooked”: in the proof below, a map is shown to be a local diffeomorphism, and this lemma is what makes it a coordinate system.

> [!proof]+ Proof (Lecture 11)
> The steps are the lecture's, in the lecture's order. Sentences marked *(Completion.)* fill in details the lecture passed over.
>
> *1. Start with any coordinates.* “I start with any coordinates”: smooth charts $(U_0, \varphi_0 = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U_0) \subseteq V$. *(Completion.)* Such charts exist: take any charts and replace $U_0$ by the open set $U_0 \cap F^{-1}(V)$.
>
> *2. The components and their matrix.* As before, define the components of $F$, $F^j = y^j \circ F : U_0 \to \mathbb{R}$. The submersion condition says that the matrix
>
> $$
> J = \Big[\frac{\partial F^j}{\partial x^i}(p)\Big]
> $$
>
> has rank $n$. It “has $m$ columns, which are the $x$'s, and $n$ rows, that are the gradients” of the $F^j$. *(Completion.)* By Theorem [[§25 The Differential in Coordinates#^thm-25-2|§25.2]], $J$ is the matrix of $F_{*p}$ in the coordinate bases, and $F_{*p}$ is onto, so $J$ has rank $n$.
>
> *3. “It's the same matrix.”* A student asked whether the matrix should be written with $\tilde F$. Uribe: “It's the same thing… That's how we define partials. We define them by going downstairs and taking the ordinary partial derivative downstairs. So it's the same matrix.” That is Proposition [[§25 The Differential in Coordinates#^prop-25-1|§25.1]]: writing $G = \psi \circ F \circ \varphi_0^{-1}$ for the coordinate representation in these first charts (the lecture's $\tilde F$ at this stage),
>
> $$
> \frac{\partial F^j}{\partial x^i}(p) = \frac{\partial G^j}{\partial r^i}\big(\varphi_0(p)\big), \qquad J = G'\big(\varphi_0(p)\big).
> $$
>
> *4. Reindex — “the only thing we need to do.”* $J$ has $n$ linearly independent columns; “I just put them at the beginning.” Rearranging the $x^i$, we can write $J$ in block form
>
> $$
> J = \big(\, A \ \big|\ B \,\big), \qquad A \text{ an } n \times n \text{ non-singular matrix}, \quad B \text{ of size } n \times (m - n),
> $$
>
> where $B$ is “the stuff that remains here that I'm not going to care about.” *(Completion.)* Rearranging the coordinates replaces $\varphi_0$ by $P \circ \varphi_0$ for a permutation $P$ of $\mathbb{R}^m$. This is again a smooth chart: a chart by Lemma [[§2 Topological Manifolds#^lem-2-11|§2.11]], and its transition maps are those of $\varphi_0$ composed with the linear map $P$ or $P^{-1}$, hence smooth. It permutes the columns of $J$ in the same way.
>
> *5. The coordinates we want.* “The thing to do, you see, is to take the first $n$ components of $F$ as the first $n$ coordinate functions, and then we keep the remaining ones”:
>
> $$
> \hat\varphi = \big(F^1, \ldots, F^n, x^{n+1}, \ldots, x^m\big) : U_0 \to \mathbb{R}^m .
> $$
>
> *(Completion.)* This makes sense because $n \le m$ — the theorem's “in particular”, true since $F_{*p}$ is onto (Proposition [[§28 Local Diffeomorphisms and Submersions#^prop-28-4|§28.4]]) — so there are $m - n \ge 0$ remaining coordinates. $\hat\varphi$ is smooth because its components are. It has $m$ components, so it maps into $\mathbb{R}^m$ (see the transcription note below).
>
> *6. The claim.* $\hat\varphi$ is a local diffeomorphism in a neighbourhood of $p$.
>
> *7. The Jacobian of $\hat\varphi$ in the old coordinates.* “Gradient across”: the first $n$ rows are the gradients of $F^1, \ldots, F^n$, which give the matrix $J = (A \mid B)$; the last $m - n$ rows are the gradients of $x^{n+1}, \ldots, x^m$. These give the $(m-n) \times (m-n)$ identity, and zero in the first $n$ columns, “because I would be taking partials of these $x$'s with respect to $x$'s that come before.” So
>
> $$
> \begin{pmatrix} A & B \\ 0 & I_{m-n} \end{pmatrix},
> $$
>
> and “by the block nature, the fact that we have a big zero there, this is non-degenerate” at $p$: its determinant is $\det A \ne 0$. *(Completion.)* “The Jacobian of $\hat\varphi$ in the $x$-coordinates” is the Jacobian at $\varphi_0(p)$ of the ordinary map $H = \hat\varphi \circ \varphi_0^{-1} : \varphi_0(U_0) \to \mathbb{R}^m$. Its rows are the partials of the components of $\hat\varphi$ by Proposition [[§25 The Differential in Coordinates#^prop-25-1|§25.1]], applied with the identity chart on $\mathbb{R}^m$, and $\partial x^k/\partial x^i = \delta^k_i$ gives the identity and zero blocks.
>
> *8. The inverse function theorem, “possibly after shrinking $U$.”* By the inverse function theorem (Theorem [[§28 Local Diffeomorphisms and Submersions#^thm-28-1|§28.1]]), possibly after shrinking, $\hat\varphi$ is a diffeomorphism onto $\hat\varphi(U)$. *(Completion.)* The theorem gives an open $W \ni \varphi_0(p)$, contained in $\varphi_0(U_0)$, with $H|_W$ a diffeomorphism onto the open set $H(W) \subseteq \mathbb{R}^m$. Put $U = \varphi_0^{-1}(W)$, an open neighbourhood of $p$. Then $\hat\varphi|_U = H|_W \circ \varphi_0|_U$ is a composite of diffeomorphisms (Proposition [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]], Lemma [[§15 Smooth Functions and Smooth Maps#^lem-15-4|§15.4]]), mapping $U$ onto the open set $\hat\varphi(U) = H(W)$.
>
> *9. The intellectual step: $\hat\varphi$ is a chart.* “There's an intellectual step here that should not be overlooked. If I have a local diffeomorphism like this from an open set in $M$ into its image, which is open in $\mathbb{R}^m$, that is a chart”: it is a homeomorphism, and being smooth with smooth inverse makes it compatible with every other smooth chart, so it lies in the maximal atlas. This is Lemma [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|§28.6]]. So $(U, \hat\varphi)$ is a smooth chart at $p$, and $F(U) \subseteq F(U_0) \subseteq V$.
>
> *10. Do not change the $y$-coordinates.* The chart $(V, \psi)$ on $N$ stays as it was. Only the chart on $M$ is new.
>
> *11. Going up and coming down.* Let $\tilde F = \psi \circ F \circ \hat\varphi^{-1} : \hat\varphi(U) \to \psi(V)$ be the coordinate representation of $F$ in the new chart. “I take a point down here, $r^1$ up to $r^m$, and I go upstairs”: going up means finding the point $q = \hat\varphi^{-1}(r)$ of $U$ whose values of the first $n$ functions $F^1, \ldots, F^n$ are the first $n$ coordinates of $r$. By the definition of $\hat\varphi$,
>
> $$
> F^i\big(\hat\varphi^{-1}(r^1, \ldots, r^m)\big) = r^i \qquad (i = 1, \ldots, n).
> $$
>
> Coming back down by $\psi$, the $i$-th coordinate of $\tilde F(r)$ is $y^i(F(q)) = F^i(q) = r^i$. So $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$: “this coordinate system labels every point in $U$; the first $n$ labels are the values of the $F$'s at that point.”

^pf-28-7

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^def-28-2|Def. §28.2]], [[§25 The Differential in Coordinates#^thm-25-2|§25.2]], [[§25 The Differential in Coordinates#^prop-25-1|§25.1]], [[§2 Topological Manifolds#^lem-2-11|§2.11]], [[§28 Local Diffeomorphisms and Submersions#^prop-28-4|§28.4]], [[§28 Local Diffeomorphisms and Submersions#^thm-28-1|§28.1]], [[§23 Derivations and the Abstract Tangent Space#^prop-23-9|§23.9]], [[§15 Smooth Functions and Smooth Maps#^lem-15-4|§15.4]], [[§28 Local Diffeomorphisms and Submersions#^lem-28-6|§28.6]], [[Invertible ⟺ nonzero determinant|LADR 9.50]]

![[m591-14-5.svg]]
*The change of chart in one diagram. The first chart $\varphi_0$ and the new chart $\hat\varphi$ differ by $H$, a diffeomorphism near $\varphi_0(p)$ by step 8. In the new chart, $F$ becomes $\tilde F$, the projection (step 11). The lecture used the letters $\phi$ and $\tilde F$ both for the first charts and for the new ones. The notes write $\varphi_0$ and $G$ for the first, and $\hat\varphi$ and $\tilde F$ for the new, to keep the two stages apart.*

**Transcription note.** In the lecture, $\hat\varphi$ was twice called “a map from $U$ into $\mathbb{R}^n$”, and page 30 of the handwritten notes writes $\phi : U \to \mathbb{R}$; it has $m$ components, so $\hat\varphi : U \to \mathbb{R}^m$. The matrix of partials was spoken as “$\partial x^j/\partial x^i$”, for $\partial F^j/\partial x^i$.

> [!theorem] Corollary §28.8: Being a Submersion Is an Open Condition
> If $F : M \to N$ is a submersion at $p$, then $F$ is a submersion at every point of some neighbourhood of $p$.
>
> *Lee: Proposition 4.1*

^cor-28-8

> [!proof]+ Proof
> In the charts of the theorem, $\tilde F$ is the projection, whose Jacobian $(I_n \mid 0)$ has rank $n$ at every point of $\hat\varphi(U)$. By Theorem [[§25 The Differential in Coordinates#^thm-25-2|§25.2]], $F_{*q}$ is onto for every $q \in U$.

^pf-28-8

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^thm-28-7|§28.7]], [[§25 The Differential in Coordinates#^thm-25-2|§25.2]]

> [!theorem] Corollary §28.9: Submersions Are Open Maps
> If $F : M \to N$ is a submersion, then $F(W)$ is open in $N$ for every open $W \subseteq M$.
>
> *Lee: Proposition 4.28*

^cor-28-9

> [!proof]+ Proof
> Let $q = F(p)$ with $p \in W$, and take the charts of the theorem at $p$, shrinking $U$ to $U \cap W$. Then $F(U) = \psi^{-1}\big(\mathrm{pr}(\hat\varphi(U))\big)$, where $\mathrm{pr} : \mathbb{R}^m \to \mathbb{R}^n$ is the projection onto the first $n$ coordinates. Projections are open (Example [[§4 Quotient Spaces and Open Maps#^ex-4-2|§4.2]]), and $\hat\varphi(U)$ is open, so $\mathrm{pr}(\hat\varphi(U))$ is an open subset of $\psi(V)$, and $F(U)$ is open in $N$. It contains $q$ and lies in $F(W)$.

^pf-28-9

*Uses:* [[§28 Local Diffeomorphisms and Submersions#^thm-28-7|§28.7]], [[§4 Quotient Spaces and Open Maps#^ex-4-2|Ex. §4.2]]
