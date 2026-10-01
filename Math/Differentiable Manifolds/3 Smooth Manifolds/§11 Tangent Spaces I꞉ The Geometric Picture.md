---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 3
section: 11
tags: [differentiable-manifolds, math591]
---
← [[§10 Vector Spaces and Matrix Groups]] · ↑ [[3 Smooth Manifolds]] · [[§12 Tangent Spaces II꞉ The Abstract Tangent Space]] →

*Stage: geometric — Tangent vectors as velocities inside the ambient space, $T^{\mathrm{geo}}_pM = \ker F'(p)$ — available only for manifolds presented by equations.*

*Reference: Lee Ch. 3, “Tangent Vectors.” Begun at the end of Lecture 7; the abstract definition is promised for Friday. Logistics: a grader (a doctoral student) has been assigned; HW3 Problem 1 is the diffeomorphism $\mathbb{R} \cong \widetilde{\mathbb{R}}$ of [[§8 Differentiable Structures#^ex-8-5|Example §8.5]].*

> [!remark] Remark: Why This Section
> The goal is to attach to each point $p$ of a smooth manifold $M$ a vector space $T_pM$, the *abstract tangent space*, so that maps between manifolds acquire differentials $dF_p : T_pM \to T_{F(p)}N$ as in [[§10 Vector Spaces and Matrix Groups|§10]]. The obstacle is that the familiar picture — a plane resting on a surface — lives in an ambient space: “if you have a sphere you can think of the tangent plane, but that is a subspace of $\mathbb{R}^3$. If you do not have $\mathbb{R}^3$, then what do you do? You do not have room to put your vectors.” An abstract manifold has no ambient space, so the construction “is going to take a little while.” This section therefore treats the case where an ambient space *is* available, and defines there the *geometric tangent space* $T^{\mathrm{geo}}_pM$ — as motivation, and because it covers all the matrix groups. The abstract $T_pM$ is built in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space|§12]], and the cotangent space in [[§13 Tangent Spaces III꞉ The Cotangent Space|§13]]. (Uribe noted that it is in some ways more natural to define the dual space first — the cotangent space — but follows Lee in not doing so.)

^rem-11-1

## The Geometric Tangent Space of a Regular Level Set

Throughout this subsection $W \subseteq \mathbb{R}^{n+k}$ is open, $F : W \to \mathbb{R}^k$ is smooth, $c \in \mathbb{R}^k$ is a regular value, and $M = F^{-1}(c)$, a smooth $n$-manifold by Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]]. Fix $p \in M$.

> [!definition] Definition §11.1: Geometric Tangent Space
> The **geometric** (or **ambient**) **tangent space** to $M$ at $p$ is
>
> $$
> T^{\mathrm{geo}}_pM \;=\; \Big\{\, \gamma'(0) \;\Big|\; \gamma : (-\varepsilon,\varepsilon) \to \mathbb{R}^{n+k} \text{ smooth},\ \varepsilon > 0,\ \gamma\big((-\varepsilon,\varepsilon)\big) \subseteq M,\ \gamma(0) = p \,\Big\} \subseteq \mathbb{R}^{n+k},
> $$
>
> where $\gamma'(0) = \frac{d\gamma}{dt}\big|_{t=0}$ is the ordinary derivative of a curve in $\mathbb{R}^{n+k}$. In words: $T^{\mathrm{geo}}_pM$ is the set of velocities at $p$ of smooth curves that pass through $p$ while staying on $M$. The same definition applies verbatim with $\mathbb{R}^{n+k}$ replaced by any finite-dimensional real vector space containing $M$, such as $\operatorname{Mat}(n,\mathbb{R})$, with $\gamma'(0)$ computed in that space.
>
> *Lee: Ch. 3 (geometric tangent vectors in $\mathbb{R}^n$) and Proposition 5.37*

^def-11-1

> [!remark]- Connections
> - The calculus picture: tangent vectors of constraint curves, [[§14 Optimization and Lagrange Multipliers#Geometric Insight: Tangent and Normal Vectors|452 §14]].
> - The abstract replacement: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-7|Def. §12.7]], identified with this one in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|Ambient and Abstract Agree, §12.8]]; velocities of curves return in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-30|§12.30]].

> [!remark] Remark
> **Notation.** Two different objects in this section are called “the tangent space at $p$”, and the notes keep them apart throughout. The *geometric* tangent space of [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1]] is written $T^{\mathrm{geo}}_pM$: it is a linear subspace of the Euclidean space $\mathbb{R}^{n+k}$ in which $M$ sits, and it exists only for manifolds presented inside a Euclidean space (here, regular level sets; also open subsets of $\mathbb{R}^N$ and of finite-dimensional vector spaces). The *abstract* tangent space of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^def-12-7|Definition §12.7]], built from derivations in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space|§12]], is written plain $T_pM$: it exists for every smooth manifold, and is not a subset of anything. The phrase “tangent space” is always qualified by one of the two adjectives. The two are identified, for regular level sets, by [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|Theorem §12.8]] — but the identification is a theorem, not a definition. On the board they appeared as $(T_pM)^{\mathrm{ambient}}$ and $(T_pM)^{\mathrm{abstract}}$.

^rem-11-2

![[m591-11-1.svg]]
*A curve $\gamma$ on $M$ through $p$, its velocity $v = \gamma'(0)$, and the plane $T^{\mathrm{geo}}_pM$ swept out by all such velocities (drawn translated to $p$), orthogonal to the gradient $\nabla F(p)$.*

“Smooth” for $\gamma$ means smooth as a map into the Euclidean space $\mathbb{R}^{n+k}$; the constraint that it take values in $M$ is a separate condition. The derivative $\gamma'(0)$ is computed with the vector space structure of $\mathbb{R}^{n+k}$, which is exactly what an abstract manifold lacks. The figure shows the definition: a curve $\gamma$ drawn on $M$ through $p$, its velocity $v$ at $t=0$ (a vector of the ambient space, drawn from $p$), and the plane these velocities sweep out as $\gamma$ ranges over all such curves — which [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]] identifies as $\ker F'(p)$, and which is therefore orthogonal to the gradient $\nabla F(p)$, shown in grey for contrast. Note that $T^{\mathrm{geo}}_pM$ is drawn as a plane through $p$ only as an aid: as a subspace of $\mathbb{R}^{n+k}$ it passes through the origin, and it is the *translate* to $p$ that is tangent to $M$.

It is not obvious from [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1]] that $T^{\mathrm{geo}}_pM$ is closed under addition: given two curves through $p$ with velocities $v$ and $w$, there is no evident curve with velocity $v + w$. “How do I add two curves?” Both this and the dimension follow from an algebraic description.

> [!theorem] Lemma §11.1: Locality of the Geometric Tangent Space
> If $M' \subseteq M$ is open in $M$ and $p \in M'$, then $T^{\mathrm{geo}}_pM' = T^{\mathrm{geo}}_pM$.

^lem-11-1

> [!proof]+ Proof
> $\subseteq$ is clear, a curve in $M'$ being a curve in $M$. For $\supseteq$, let $\gamma : (-\varepsilon,\varepsilon) \to M$ be smooth with $\gamma(0) = p$. Since $\gamma$ is continuous and $M'$ is open in $M$, the set $\gamma^{-1}(M')$ is open in $(-\varepsilon,\varepsilon)$ and contains $0$, so it contains an interval $(-\delta,\delta)$. The restriction $\gamma|_{(-\delta,\delta)}$ takes values in $M'$ and has the same velocity at $0$.

^pf-11-1

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]], [[§9 Continuous Functions#^def-9-1|590 §9.1]]

> [!theorem] Lemma §11.2: The Geometric Tangent Space of a Graph
> Let $A \subseteq \mathbb{R}^n$ be open, $G : A \to \mathbb{R}^k$ smooth, and
>
> $$
> M = \{\, (x, G(x)) \mid x \in A \,\} \subseteq \mathbb{R}^{n+k}
> $$
>
> its graph. For $p = (x_0, G(x_0))$ with $x_0 \in A$,
>
> $$
> T^{\mathrm{geo}}_pM \;=\; \{\, (u,\; G'(x_0)\,u) \mid u \in \mathbb{R}^n \,\},
> $$
>
> the graph of the linear map $G'(x_0) : \mathbb{R}^n \to \mathbb{R}^k$. In particular $T^{\mathrm{geo}}_pM$ is a linear subspace of $\mathbb{R}^{n+k}$ of dimension $n$.

^lem-11-2

> [!proof]+ Proof
> *(Set in Lecture 8 as an exercise — “not a trivial exercise”; filled in.)* $\subseteq$: let $\gamma : (-\varepsilon,\varepsilon) \to M$ be smooth with $\gamma(0) = p$, and write $\gamma = (\gamma_1, \gamma_2)$ with $\gamma_1$ into $\mathbb{R}^n$ and $\gamma_2$ into $\mathbb{R}^k$. Both components are smooth, and since $\gamma(t) \in M$ for every $t$ we have $\gamma_2 = G \circ \gamma_1$ and $\gamma_1(0) = x_0$. By the chain rule
>
> $$
> \gamma'(0) = \big(\gamma_1'(0),\; G'(x_0)\,\gamma_1'(0)\big),
> $$
>
> which lies in the graph of $G'(x_0)$.
>
> $\supseteq$: given $u \in \mathbb{R}^n$, choose $\varepsilon > 0$ with $x_0 + tu \in A$ for $|t| < \varepsilon$, possible since $A$ is open, and set
>
> $$
> \gamma(t) = \big(x_0 + tu,\; G(x_0 + tu)\big).
> $$
>
> This is smooth into $\mathbb{R}^{n+k}$, takes values in $M$, has $\gamma(0) = p$, and $\gamma'(0) = (u, G'(x_0)u)$ by the chain rule.
>
> Finally, the graph of a linear map $\mathbb{R}^n \to \mathbb{R}^k$ is a linear subspace of $\mathbb{R}^{n+k}$, and $u \mapsto (u, G'(x_0)u)$ is an injective linear map onto it, so its dimension is $n$.

^pf-11-2

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]], [[Multivariable Chain Rule|452 §10.2]], [[Fundamental theorem of linear maps|LADR 3.21]]

> [!remark] Remark
> Uribe stated this lemma and left it as an exercise, calling it “not a trivial exercise”; the proof above is short but both inclusions are needed, and the $\supseteq$ half — lifting a straight line from the chart — is the construction that reappears in [[§12 Tangent Spaces II꞉ The Abstract Tangent Space|§12]] as the curve defining $D_v$. In words: *the geometric tangent space to a graph is the graph of the differential.*

^rem-11-3

> [!theorem] Theorem §11.3: The Geometric Tangent Space Is the Kernel of the Jacobian
> $T^{\mathrm{geo}}_pM = \ker F'(p)$, where $F'(p) : \mathbb{R}^{n+k} \to \mathbb{R}^k$ is the Jacobian at $p$. In particular $T^{\mathrm{geo}}_pM$ is a linear subspace of $\mathbb{R}^{n+k}$ of dimension $n = \dim M$.
>
> *Lee: Proposition 5.38*

^thm-11-3

> [!proof]+ Proof
> The order is Lecture 8's sketch, which built on an inclusion proved in Lecture 7.
>
> *1. The inclusion (Lecture 7: “last time we saw this inclusion”).* $T^{\mathrm{geo}}_pM \subseteq \ker F'(p)$. Let $v \in T^{\mathrm{geo}}_pM$ with $\gamma$ as in [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1]]. The composite $F \circ \gamma : (-\varepsilon,\varepsilon) \to \mathbb{R}^k$ is smooth, being a composite of smooth maps between Euclidean spaces, and since $\gamma(t) \in M = F^{-1}(c)$ for every $t$ it is the constant $c$. Differentiating at $t = 0$ and applying the [[Multivariable Chain Rule|chain rule]],
>
> $$
> \vec 0 = \frac{d}{dt}\Big|_{t=0} F(\gamma(t)) = F'(\gamma(0))\,\gamma'(0) = F'(p)\, v ,
> $$
>
> so $v \in \ker F'(p)$.
>
> *2. Everything is local near $p$, so WLOG $M$ is a graph.* “Since everything is local near $p$ … these regular level sets are locally graphs of functions, for various choices of variables.” *(Completion.)* By the proof of Theorem [[§4 The Regular Value Theorem#^thm-4-3|§4.3]], after permuting coordinates there is an open box $V \times V'$ containing $p$ and a smooth $G : V \to V'$ with $M \cap (V \times V') = \{(x, G(x)) \mid x \in V\}$. By Lemma [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-1|§11.1]] the geometric tangent space is unchanged on passing to this open piece.
>
> *3. The claim: the tangent space to a graph is the graph of the derivative.* $T^{\mathrm{geo}}_pM$ is the graph of $G'(x_0)$, where $p = (x_0, G(x_0))$ — set in lecture as “not a trivial exercise” and proved in Lemma [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]]. So $T^{\mathrm{geo}}_pM$ is a subspace of dimension $n$.
>
> *4. The kernel has dimension $n$, by rank–nullity.* Since $c$ is a regular value, $F'(p) : \mathbb{R}^{n+k} \to \mathbb{R}^k$ has rank $k$, so [[Fundamental theorem of linear maps|rank–nullity]] gives $\dim \ker F'(p) = (n+k) - k = n$.
>
> *5. “We must have equality.”* $T^{\mathrm{geo}}_pM$ is an $n$-dimensional subspace contained in the $n$-dimensional subspace $\ker F'(p)$, so the two are equal.

^pf-11-3

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]], [[§4 The Regular Value Theorem#^thm-4-3|§4.3]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-1|§11.1]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-2|§11.2]], [[Multivariable Chain Rule|452 §10.2]], [[Fundamental theorem of linear maps|LADR 3.21]], [[2C Dimension#^ladr-2-39|LADR 2.39]]

> [!remark]- Connections
> - Identified with the abstract tangent space: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-8|Ambient and Abstract Agree, §12.8]]; for submanifolds, [[§15 Submanifolds#^prop-15-4|§15.4]].
> - Orthogonality to the gradients is the geometry behind [[Method of Lagrange Multipliers|452 §14.2 (Lagrange multipliers)]].

> [!remark] Remark
> The structure is worth noticing, because it is not the obvious one. Only the *easy* inclusion is proved directly; the reverse inclusion is never constructed, but forced by a dimension count. Uribe: “it's best actually to prove something else” — namely the graph lemma, from which both the vector space structure and the dimension of $T^{\mathrm{geo}}_pM$ are immediate, after which “we must have equality.”

^rem-11-4

> [!theorem] Corollary §11.4: Three Descriptions of the Geometric Tangent Space
> In the notation of [[§11 Tangent Spaces I꞉ The Geometric Picture#^pf-11-3|the proof]], with $\alpha : V \to \mathbb{R}^{n+k}$, $\alpha(x) = (x, h(x))$ the parametrization inverse to the graph chart,
>
> $$
> T^{\mathrm{geo}}_pM \;=\; \{\text{velocities of curves in } M \text{ through } p\} \;=\; \ker F'(p) \;=\; \operatorname{im} D\alpha_a ,
> $$
>
> and $D\alpha_a : \mathbb{R}^n \to \mathbb{R}^{n+k}$, $u \mapsto (u, Dh_a u)$, is an isomorphism onto $T^{\mathrm{geo}}_pM$.
>
> *Lee: Propositions 5.37 and 5.38*

^cor-11-4

> [!proof]+ Proof
> The first equality is the definition and the second is [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]]. Step 2 of that proof shows every $v \in \ker F'(p)$ has the form $(v_1, Dh_a v_1) = D\alpha_a(v_1)$, so $\ker F'(p) \subseteq \operatorname{im} D\alpha_a$; and differentiating $F \circ \alpha \equiv c$ gives $F'(p) \circ D\alpha_a = 0$, so $\operatorname{im} D\alpha_a \subseteq \ker F'(p)$. $D\alpha_a$ is injective because its first $n$ components are the identity, and both spaces have dimension $n$.

^pf-11-4

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[Multivariable Chain Rule|452 §10.2]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark] Remark
> The corollary is the infinitesimal form of [[§9 Manifolds in Euclidean Space|§9]]: the geometric tangent space can be read off from the *external* description as the kernel of the constraint map, or from the *internal* description as the image of the derivative of a parametrization, and the two agree. The geometric definition, via curves, is the one that makes no reference to either presentation — which is why it is the one that will generalize.

^rem-11-5

## Examples

> [!example] Example §11.1: The Sphere
> For $S^n = F^{-1}(1)$ with $F(x) = |x|^2 = \sum x_i^2$ on $\mathbb{R}^{n+1}$, the Jacobian at $p$ is the row vector $F'(p) = 2p^{\mathsf T}$, and $1$ is a regular value since $p \neq 0$ on $S^n$. Hence
>
> $$
> T^{\mathrm{geo}}_pS^n = \ker\big(2p^{\mathsf T}\big) = \{\, v \in \mathbb{R}^{n+1} \mid p \cdot v = 0 \,\} = p^{\perp},
> $$
>
> the hyperplane orthogonal to the position vector — the tangent plane of calculus, now as a theorem. Directly from the definition: any curve $\gamma$ on the sphere satisfies $\gamma(t)\cdot\gamma(t) = 1$, so $2\,\gamma(t)\cdot\gamma'(t) = 0$, and at $t = 0$ this is $p \cdot v = 0$.

^ex-11-1

> [!remark]- Connections
> - The sphere in 452: [[Unit circle and unit sphere]].

> [!example] Example §11.2: The Orthogonal Group
> For $\mathrm{O}(n) = F^{-1}(I)$ with $F : \operatorname{Mat}(n,\mathbb{R}) \to \operatorname{Sym}(n,\mathbb{R})$, $F(g) = gg^{\mathsf T}$, [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]] applies after identifying both spaces with Euclidean spaces by linear coordinates, under which the Jacobian corresponds to the differential $dF_g$ of [[§10 Vector Spaces and Matrix Groups#^def-10-9|Definition §10.9]]. Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-12|§10.12]] then gives
>
> $$
> T^{\mathrm{geo}}_g\mathrm{O}(n) = \ker dF_g = g \cdot \operatorname{Skew}(n,\mathbb{R}), \qquad T^{\mathrm{geo}}_I \mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R}),
> $$
>
> of dimension $\tfrac{n(n-1)}{2}$, as it must be. Directly from the definition, at $g = I$: if $\gamma$ is a curve of orthogonal matrices with $\gamma(0) = I$, then $\gamma(t)\gamma(t)^{\mathsf T} = I$ for all $t$; differentiating at $0$ gives $\gamma'(0) + \gamma'(0)^{\mathsf T} = 0$, so the velocity is skew-symmetric. This geometric tangent space at the identity is the object that will later be called the *Lie algebra* $\mathfrak{so}(n)$.

^ex-11-2

> [!remark] Remark
> For $\mathrm{O}(n)$ the ambient space is $\operatorname{Mat}(n,\mathbb{R})$ rather than $\mathbb{R}^{n^2}$; [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1]] is used in its vector-space form, and [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]] transfers across the linear isomorphism of Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-9|§10.9]]. The description $T^{\mathrm{geo}}_g\mathrm{O}(n) = g \cdot T^{\mathrm{geo}}_I\mathrm{O}(n)$ — every geometric tangent space is a translate of the one at the identity — is the first sign that a group structure simplifies the tangent bundle; it will be a general fact about Lie groups.

^rem-11-6

> [!example] Example §11.3: The Unitary Group
> By Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-15|§10.15]] and [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]] (transferred to the real vector space $\operatorname{Mat}(n,\mathbb{C})$ as in [[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-6|the note above]]),
>
> $$
> T^{\mathrm{geo}}_g\mathrm{U}(n) = \ker dF_g = \mathfrak{u}(n)\cdot g = g\cdot\mathfrak{u}(n), \qquad T^{\mathrm{geo}}_I\mathrm{U}(n) = \mathfrak{u}(n).
> $$
>
> Directly from the definition at $g = I$: a curve of unitary matrices with $\gamma(0) = I$ satisfies $\gamma(t)\gamma(t)^* = I$, and differentiating at $0$ gives $\gamma'(0) + \gamma'(0)^* = 0$.

^ex-11-3

> [!theorem] Theorem §11.5: The Classical Groups
> Each classical group of [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8|Theorem §5.8]] is a smooth manifold, of the dimension and with the geometric tangent space at the identity given below. Moreover, for $G = \mathrm{SL}(n,\mathbb{R}), \mathrm{O}(n), \mathrm{SO}(n), \mathrm{U}(n)$ and every $g \in G$,
>
> $$
> T^{\mathrm{geo}}_g G \;=\; g \cdot T^{\mathrm{geo}}_I G \;=\; T^{\mathrm{geo}}_I G \cdot g .
> $$
>
> *Lee: Examples 7.27–7.30*

^thm-11-5

| Group $G$ | Presentation | $\dim G$ | $T^{\mathrm{geo}}_I G$ |
|---|---|:---:|---|
| $\mathrm{GL}(n,\mathbb{R})$ | open in $\operatorname{Mat}(n,\mathbb{R})$ | $n^2$ | $\operatorname{Mat}(n,\mathbb{R})$ |
| $\mathrm{GL}(n,\mathbb{C})$ | open in $\operatorname{Mat}(n,\mathbb{C})$ | $2n^2$ | $\operatorname{Mat}(n,\mathbb{C})$ |
| $\mathrm{SL}(n,\mathbb{R})$ | $\det^{-1}(1)$ | $n^2 - 1$ | $\mathfrak{sl}(n) = \{A \mid \operatorname{tr} A = 0\}$ |
| $\mathrm{O}(n)$ | $F^{-1}(I)$, $F(g) = gg^{\mathsf T} \in \operatorname{Sym}(n,\mathbb{R})$ | $\tfrac{n(n-1)}{2}$ | $\mathfrak{so}(n) = \operatorname{Skew}(n,\mathbb{R})$ |
| $\mathrm{SO}(n)$ | open in $\mathrm{O}(n)$ | $\tfrac{n(n-1)}{2}$ | $\mathfrak{so}(n)$ |
| $\mathrm{U}(n)$ | $F^{-1}(I)$, $F(g) = gg^* \in \operatorname{Herm}(n)$ | $n^2$ | $\mathfrak{u}(n) = \{X \mid X^* = -X\}$ |

> [!proof]+ Proof
> *The general linear groups.* An open subset $U$ of a finite-dimensional vector space $V$ is a smooth manifold of dimension $\dim V$ (one chart, the restriction of a linear chart). [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1]] makes sense verbatim for $U \subseteq V$, and every $v \in V$ is the velocity of the curve $t \mapsto p + tv$, which stays in $U$ for small $|t|$; so $T^{\mathrm{geo}}_pU = V$.
>
> *$\mathrm{SL}(n,\mathbb{R})$.* Smoothness and dimension are Corollary [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5.13]] with Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]]. By Proposition [[§5 Topological Groups and Classical Matrix Groups#^prop-5-9|§5.9]], $d(\det)_g(A) = \det(g)\,\operatorname{tr}(g^{-1}A)$, so for $g \in \mathrm{SL}(n,\mathbb{R})$ [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]] gives $T^{\mathrm{geo}}_g\mathrm{SL} = \{A \mid \operatorname{tr}(g^{-1}A) = 0\}$. Writing $A = gB$ this is $g\cdot\mathfrak{sl}(n)$; writing $A = Bg$ and using $\operatorname{tr}(g^{-1}Bg) = \operatorname{tr} B$, it is $\mathfrak{sl}(n)\cdot g$. The trace condition removes one dimension, consistently with $n^2 - 1$.
>
> *$\mathrm{O}(n)$ and $\mathrm{SO}(n)$.* [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Example §10.1]], [[§10 Vector Spaces and Matrix Groups#^cor-10-13|Corollary §10.13]], and [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|Example §11.2]]; since $\mathrm{SO}(n)$ is open in $\mathrm{O}(n)$ its geometric tangent spaces are those of $\mathrm{O}(n)$ ([[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-1|Lemma §11.1]]). For the right translate, $\operatorname{Skew}(n,\mathbb{R})$ is preserved by conjugation by orthogonal $g$, exactly as in the proof of Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-15|§10.15]].
>
> *$\mathrm{U}(n)$.* [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Example §10.2]] and [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3|Example §11.3]].

^pf-11-5

*Uses:* [[§5 Topological Groups and Classical Matrix Groups#^thm-5-8|§5.8]], [[§10 Vector Spaces and Matrix Groups#^prop-10-9|§10.9]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Def. §11.1]], [[§5 Topological Groups and Classical Matrix Groups#^cor-5-13|§5.13]], [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-9|§5.9]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Ex. §10.1]], [[§10 Vector Spaces and Matrix Groups#^cor-10-13|§10.13]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-2|Ex. §11.2]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^lem-11-1|§11.1]], [[§10 Vector Spaces and Matrix Groups#^prop-10-15|§10.15]], [[§10 Vector Spaces and Matrix Groups#^ex-10-2|Ex. §10.2]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-3|Ex. §11.3]], [[8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]

> [!definition] Definition §11.2: Adjoint Action
> Let $G$ be one of $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$, and $\mathfrak{g} = T^{\mathrm{geo}}_I G$. For $g \in G$, **conjugation** by $g$ is $\mathrm{Ad}_g(X) = gXg^{-1}$. The **adjoint action** of $G$ on $\mathfrak{g}$ is $g \mapsto \mathrm{Ad}_g|_{\mathfrak{g}}$; that each $\mathrm{Ad}_g$ maps $\mathfrak{g}$ onto itself is part of [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-6|the next proposition]].

^def-11-2

> [!remark]- Connections
> - Conjugation as a group action on the group itself: [[§32 Conjugation as an Action and the Class Equation#^prop-32-1|493 §32.1]]; $\mathrm{Ad}_g$ is conjugation acting on $T^{\mathrm{geo}}_IG$.

> [!theorem] Proposition §11.6: The Adjoint Action
> Let $G$ be one of $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$, and $\mathfrak{g} = T^{\mathrm{geo}}_I G$. For $g \in G$ the conjugation
>
> $$
> \mathrm{Ad}_g : \mathfrak{g} \to \mathfrak{g}, \qquad \mathrm{Ad}_g(X) = gXg^{-1},
> $$
>
> is a linear isomorphism, with $\mathrm{Ad}_{gh} = \mathrm{Ad}_g \circ \mathrm{Ad}_h$. Left and right multiplication $L_g(X) = gX$ and $R_g(X) = Xg$ satisfy $L_g = R_g \circ \mathrm{Ad}_g$.

^prop-11-6

> [!proof]+ Proof
> That $\mathrm{Ad}_g$ maps $\mathfrak{g}$ into itself is checked case by case, with $\mathfrak{g}$ as in [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|Theorem §11.5]]. For $\mathfrak{sl}(n)$: $\operatorname{tr}(gXg^{-1}) = \operatorname{tr} X$. For $g$ orthogonal and $X$ skew: $(gXg^{-1})^{\mathsf T} = (gXg^{\mathsf T})^{\mathsf T} = gX^{\mathsf T}g^{\mathsf T} = -gXg^{-1}$. For $g$ unitary and $X$ skew-Hermitian: $(gXg^*)^* = gX^*g^* = -gXg^{-1}$. $\mathrm{Ad}_g$ is linear, $\mathrm{Ad}_{gh}X = ghXh^{-1}g^{-1} = \mathrm{Ad}_g(\mathrm{Ad}_h X)$, and $\mathrm{Ad}_{g^{-1}}$ is an inverse. Finally $R_g(\mathrm{Ad}_g X) = gXg^{-1}g = gX$.

^pf-11-6

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-2|Def. §11.2]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-5|§11.5]], [[8D Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]

> [!remark] Remark: Left and Right Translates
> The notes computed $T^{\mathrm{geo}}_g\mathrm{O}(n) = g\cdot\operatorname{Skew}(n)$ by writing $A = gB$ (Proposition [[§10 Vector Spaces and Matrix Groups#^prop-10-12|§10.12]]); [[§10 Vector Spaces and Matrix Groups#^prop-10-15|Assignment 2]] computed $T^{\mathrm{geo}}_g\mathrm{U}(n) = \mathfrak{u}(n)\cdot g$ by writing $h = Xg$. Neither choice is privileged, and by [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-6|the proposition]] the two agree, $g \cdot \mathfrak{g} = \mathrm{Ad}_g(\mathfrak{g}) \cdot g = \mathfrak{g} \cdot g$. This is the first structural fact about Lie groups to appear in the course: the geometric tangent space at the identity, carried to every other point by left or right multiplication, determines all the geometric tangent spaces. The spaces $\mathfrak{sl}(n)$, $\mathfrak{so}(n)$, $\mathfrak{u}(n)$ in the table will reappear as *Lie algebras*.

^rem-11-7

![[m591-11-2.svg]]
*Left multiplication $L_g$ and right multiplication $R_g$ both carry $T^{\mathrm{geo}}_IG$ onto $T^{\mathrm{geo}}_gG$, and the triangle commutes: $L_g = R_g \circ \mathrm{Ad}_g$.*

Left and right multiplication by $g$ both carry $T^{\mathrm{geo}}_IG$ isomorphically onto $T^{\mathrm{geo}}_gG$, and they differ by the adjoint action: $L_g = R_g \circ \mathrm{Ad}_g$, since $(gXg^{-1})g = gX$. The two descriptions of $T^{\mathrm{geo}}_gG$ agree precisely because $\mathrm{Ad}_g$ maps $T^{\mathrm{geo}}_IG$ onto itself.

> [!definition] Definition §11.3: The Hat Map
> The **hat map** $\mathbb{R}^3 \to \operatorname{Skew}(3,\mathbb{R})$ sends $v = (v_1, v_2, v_3)$ to
>
> $$
> \hat v = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix},
> $$
>
> a linear isomorphism, characterized by $\hat v\, x = v \times x$ for all $x \in \mathbb{R}^3$.

^def-11-3

> [!example] Example §11.4: $\mathrm{SO}(3)$ and Infinitesimal Rotations
> $T^{\mathrm{geo}}_I\mathrm{SO}(3) = \operatorname{Skew}(3,\mathbb{R})$ is $3$-dimensional, and it is identified with $\mathbb{R}^3$ by the hat map of [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-3|Definition §11.3]]
>
> $$
> v = (v_1,v_2,v_3) \longmapsto \hat v = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix},
> \qquad \hat v\, x = v \times x .
> $$
>
> Every tangent vector at the identity is the velocity of a family of rotations. For the axis $e_3$,
>
> $$
> R(t) = \begin{pmatrix} \cos t & -\sin t & 0 \\ \sin t & \cos t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad R(0) = I, \qquad R'(0) = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \hat e_3 .
> $$
>
> For a unit vector $n$, choose $Q \in \mathrm{SO}(3)$ with $Qe_3 = n$ (possible by [[§7 Homogeneous Spaces#^ex-7-3|Example §7.3]]); the rotation about $n$ by angle $t$ is $QR(t)Q^{\mathsf T}$, with velocity $Q\hat e_3 Q^{\mathsf T} = \widehat{Qe_3} = \hat n$ at $t = 0$, using the identity $\widehat{Qv} = Q\hat vQ^{\mathsf T}$ for $Q \in \mathrm{SO}(3)$, which holds because rotations preserve the cross product. Scaling the speed, every $\hat v$ is attained: *a tangent vector to $\mathrm{SO}(3)$ at the identity is an angular velocity*, with direction the axis and length the rate of rotation.

^ex-11-4

> [!remark] Remark
> This connects the $\mathrm{SO}(3)$ material of [[§6 Group Actions and Orbit Spaces|§6]] and [[§7 Homogeneous Spaces|§7]] with the geometric tangent space. The three dimensions of $\mathrm{SO}(3)$ are the two needed to specify an axis, a point of $S^2$, and one for the angle about it — matching $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ of [[§7 Homogeneous Spaces#^ex-7-3|Example §7.3]], with the isotropy $\mathrm{SO}(2)$ being exactly the rotations about the fixed axis.

^rem-11-8

> [!remark] Remark: Dimension Checks through Homogeneous Spaces
> In every homogeneous space met so far, $\dim G/H = \dim G - \dim H$:
> - $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$:  $3 - 1 = 2$;
> - $\mathrm{Gr}_k(\mathbb{R}^n) = \mathrm{O}(n)/\big(\mathrm{O}(k)\times\mathrm{O}(n-k)\big)$:  $\tfrac{n(n-1)}{2} - \tfrac{k(k-1)}{2} - \tfrac{(n-k)(n-k-1)}{2} = k(n-k)$;
> - $S^{2n+1} = \mathrm{U}(n+1)/\mathrm{U}(n)$:  $(n+1)^2 - n^2 = 2n+1$;
> - $\mathbb{CP}^n = \mathrm{U}(n+1)/\big(\mathrm{U}(1)\times\mathrm{U}(n)\big)$:  $(n+1)^2 - 1 - n^2 = 2n$, the real dimension found from charts in [[§8 Differentiable Structures#^thm-8-7|Theorem §8.7]].
>
> The first two identifications are proved in [[§7 Homogeneous Spaces|§7]]; the last two are their complex analogues — $\mathrm{U}(n+1)$ acts transitively on unit vectors of $\mathbb{C}^{n+1}$ and on complex lines — and are not proved here. The formula itself is heuristic until quotient manifolds are available, when it becomes a theorem; for now it is a consistency check linking four separate computations.

^rem-11-9

## Transversality

*Assignment 2, Problem 5. The problem ends with a parenthetical that is the point of the whole exercise: the transversality condition “does not mention $G$ explicitly — keep this in mind, for the future.”*

Throughout this subsection $F : \mathbb{R}^N \to \mathbb{R}^k$ and $G : \mathbb{R}^k \to \mathbb{R}^\ell$ are smooth, $0$ is a regular value of $G$, and

$$
S = G^{-1}(0) \subseteq \mathbb{R}^k ,
$$

a smooth manifold of dimension $k - \ell$ with $T^{\mathrm{geo}}_qS = \ker G'(q)$ for $q \in S$ ([[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]]). Its codimension, in the sense of the next definition, is $\operatorname{codim} S = k - \dim S = \ell$, the number of equations cutting it out.

> [!definition] Definition §11.4: Codimension
> If $S \subseteq \mathbb{R}^k$ is a manifold of dimension $s$ — for instance a regular level set — its **codimension** in $\mathbb{R}^k$ is $\operatorname{codim} S = k - s$.
>
> *Lee: Ch. 5, Embedded Submanifolds*

^def-11-4

(Everything below works verbatim with $F$ and $G$ defined only on open subsets.)

> [!definition] Definition §11.5: Transversality
> $F$ is **transverse** to $S$, written $F \pitchfork S$, if
>
> $$
> \operatorname{im} F'(p) \;+\; T^{\mathrm{geo}}_{F(p)}S \;=\; \mathbb{R}^k \qquad \text{for every } p \in F^{-1}(S).
> $$
>
> The condition is imposed only at points of the preimage, and holds vacuously if $F^{-1}(S) = \emptyset$.

^def-11-5

> [!remark] Remark
> In words: at each point where $F$ meets $S$, the directions $F$ can move in, together with the directions along $S$, fill up the whole ambient space. The condition involves $F$ and $S$ only — not the function $G$ used to cut $S$ out.

^rem-11-10

> [!theorem] Theorem §11.7: Preimages of Transverse Level Sets
> If $F \pitchfork S$, then $M = F^{-1}(S)$ is a smooth manifold of dimension $N - \ell$ (or empty), and for $p \in M$
>
> $$
> T^{\mathrm{geo}}_pM = F'(p)^{-1}\big(T^{\mathrm{geo}}_{F(p)}S\big) = \{\, v \in \mathbb{R}^N \mid F'(p)v \in T^{\mathrm{geo}}_{F(p)}S \,\}.
> $$
>
> In particular $\operatorname{codim} M = \operatorname{codim} S = \ell$.
>
> *Lee: Theorem 6.30(a)*

^thm-11-7

![[m591-11-3.svg]]
*The spaces: $M = F^{-1}(S)$ inside $\mathbb{R}^N$ over $S$ inside $\mathbb{R}^k$, and the composite $G \circ F$ that cuts $M$ out.*

![[m591-11-4.svg]]
*Their linearizations at $p$ and $q = F(p)$.*

Top, the spaces; bottom, their linearizations at $p$ and $q = F(p)$. In each, the square says the top-left corner is everything upstairs that lands in the bottom-left corner — $M = F^{-1}(S)$ and $T^{\mathrm{geo}}_pM = F'(p)^{-1}(T^{\mathrm{geo}}_qS)$ — and the triangle says the same set is cut out by the composite, $M = (G\circ F)^{-1}(0)$ and $T^{\mathrm{geo}}_pM = \ker (G\circ F)'(p)$. The theorem asserts that the preimage in the lower diagram is the geometric tangent space of the preimage in the upper one; [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-6|Example §11.6]](b) shows this can fail without transversality.

> [!proof]+ Proof
> If $M = \emptyset$ there is nothing to prove, so assume otherwise; then $S \neq \emptyset$, and surjectivity of $G'(q) : \mathbb{R}^k \to \mathbb{R}^\ell$ at some $q \in S$ gives $k \ge \ell$.
>
> *$M$ is a level set.* $p \in F^{-1}(S) \iff F(p) \in G^{-1}(0) \iff G(F(p)) = 0$, so $M = (G \circ F)^{-1}(0)$, with $G \circ F : \mathbb{R}^N \to \mathbb{R}^\ell$ smooth.
>
> *$0$ is a regular value of $G \circ F$.* Let $p \in M$ and $q = F(p)$. By the [[Multivariable Chain Rule|chain rule]] $(G \circ F)'(p) = G'(q)\,F'(p)$. Given $w \in \mathbb{R}^\ell$, choose $u \in \mathbb{R}^k$ with $G'(q)u = w$, possible as $G'(q)$ is surjective. By transversality write $u = F'(p)v + t$ with $v \in \mathbb{R}^N$ and $t \in T^{\mathrm{geo}}_qS = \ker G'(q)$. Then
>
> $$
> w = G'(q)u = G'(q)F'(p)v + G'(q)t = G'(q)F'(p)v ,
> $$
>
> so $(G\circ F)'(p)$ is surjective. As $p \in M$ was arbitrary, $0$ is a regular value, and surjectivity at a point of $M$ forces $N \ge \ell$.
>
> *Conclusion.* By Theorem [[§4 The Regular Value Theorem#^thm-4-3|§4.3]] and Proposition [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]], $M$ is a smooth manifold of dimension $N - \ell$, so $\operatorname{codim} M = N - (N - \ell) = \ell = \operatorname{codim} S$. By [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]],
>
> $$
> T^{\mathrm{geo}}_pM = \ker\big(G'(q)F'(p)\big) = \{v \mid F'(p)v \in \ker G'(q)\} = F'(p)^{-1}(T^{\mathrm{geo}}_qS).
> $$

^pf-11-7

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-5|Def. §11.5]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-4|Def. §11.4]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]], [[§4 The Regular Value Theorem#^thm-4-3|§4.3]], [[§9 Manifolds in Euclidean Space#^prop-9-2|§9.2]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[Multivariable Chain Rule|452 §10.2]]

**Comparison with Lee.** Lee's Theorem 6.30 states this for a smooth map transverse to an *embedded submanifold* $S \subseteq M$, after the theory of submanifolds (Chapter 5). The course's version, for level sets in Euclidean space, needs only the regular value theorem. It is the case where $S$ is cut out by a single global defining map $G$, and the proof — pull $G$ back along $F$ — is the one Lee uses locally.

> [!theorem] Proposition §11.8: Transversality Is the Regular Value Condition
> For $p \in F^{-1}(S)$ with $q = F(p)$,
>
> $$
> \operatorname{im} F'(p) + T^{\mathrm{geo}}_qS = \mathbb{R}^k \iff (G \circ F)'(p) \text{ is surjective.}
> $$
>
> Consequently $F \pitchfork S$ if and only if $0$ is a regular value of $G \circ F$.

^prop-11-8

> [!proof]+ Proof
> ($\Rightarrow$) is the middle step of the proof of [[§11 Tangent Spaces I꞉ The Geometric Picture#^pf-11-7|Theorem §11.7]]. ($\Leftarrow$) Suppose $G'(q)F'(p)$ is surjective and let $u \in \mathbb{R}^k$. Then $G'(q)u = G'(q)F'(p)v$ for some $v \in \mathbb{R}^N$, so $u - F'(p)v \in \ker G'(q) = T^{\mathrm{geo}}_qS$, and
>
> $$
> u = F'(p)v + \big(u - F'(p)v\big) \in \operatorname{im} F'(p) + T^{\mathrm{geo}}_qS.
> $$

^pf-11-8

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-5|Def. §11.5]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|§11.7]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]]

> [!remark] Remark: An Intrinsic Statement with a Chosen Proof
> [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-8|Proposition §11.8]] is the precise content of the parenthetical. Transversality is not merely a sufficient condition: it *is* the regular value condition for $G \circ F$, rewritten so that $G$ disappears. The hypothesis of [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7]] and both of its conclusions — that $M$ is a manifold, and the formula for $T^{\mathrm{geo}}_pM$ — involve only $F$ and $S$; only the proof picks a defining function $G$. This is the same pattern as for charts: a statement that does not depend on a choice, proved by making one. Two things remain for later. The smooth structure on $M$ is built through $G$, and its independence of $G$ is a statement about submanifolds. And $S$ need only be cut out by some $G$ *near each point*, which will turn out to hold for every embedded submanifold, so the theorem localizes.

^rem-11-11

> [!theorem] Corollary §11.9: The Regular Value Theorem as a Special Case
> Let $c \in \mathbb{R}^k$ and $S = \{c\}$. Then $F \pitchfork \{c\}$ if and only if $c$ is a regular value of $F$, and in that case [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7]] returns [[§4 The Regular Value Theorem#^thm-4-3|Theorem §4.3]] together with $T^{\mathrm{geo}}_pM = \ker F'(p)$.

^cor-11-9

> [!proof]+ Proof
> $\{c\} = G^{-1}(0)$ for $G(y) = y - c$, whose Jacobian is the identity, so $0$ is a regular value of $G$ with $\ell = k$, and $T^{\mathrm{geo}}_c\{c\} = \ker I = 0$. Transversality then reads $\operatorname{im} F'(p) = \mathbb{R}^k$ at every $p \in F^{-1}(c)$ — the [[§4 The Regular Value Theorem#^def-4-2|definition of a regular value]]. The conclusions are $\dim M = N - k$ and $T^{\mathrm{geo}}_pM = F'(p)^{-1}(0) = \ker F'(p)$.

^pf-11-9

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-5|Def. §11.5]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|§11.7]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]], [[§4 The Regular Value Theorem#^thm-4-3|§4.3]]

> [!remark]- Connections
> - The regular value theorem for maps between manifolds: [[§15 Submanifolds#^thm-15-6|§15.6]], compared with this version in [[§15 Submanifolds#^prop-15-8|§15.8]].

> [!definition] Definition §11.6: Transverse Intersection
> Regular level sets $S_1, S_2 \subseteq \mathbb{R}^k$ **intersect transversally** if
>
> $$
> T^{\mathrm{geo}}_qS_1 + T^{\mathrm{geo}}_qS_2 = \mathbb{R}^k \qquad\text{for every } q \in S_1 \cap S_2 ,
> $$
>
> a condition that holds vacuously when $S_1 \cap S_2 = \emptyset$.
>
> *Lee: Theorem 6.30(b)*

^def-11-6

> [!theorem] Proposition §11.10: Transverse Intersections
> Let $G_i : \mathbb{R}^k \to \mathbb{R}^{\ell_i}$, $i = 1,2$, be smooth with $0$ a regular value, and $S_i = G_i^{-1}(0)$. For $q \in S_1 \cap S_2$,
>
> $$
> T^{\mathrm{geo}}_qS_1 + T^{\mathrm{geo}}_qS_2 = \mathbb{R}^k \iff (G_1, G_2)'(q) : \mathbb{R}^k \to \mathbb{R}^{\ell_1 + \ell_2} \text{ is surjective.}
> $$
>
> If $S_1$ and $S_2$ intersect transversally ([[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-6|Definition §11.6]]), then $S_1 \cap S_2$ is a smooth manifold with
>
> $$
> \operatorname{codim}(S_1 \cap S_2) = \operatorname{codim} S_1 + \operatorname{codim} S_2, \qquad T^{\mathrm{geo}}_q(S_1 \cap S_2) = T^{\mathrm{geo}}_qS_1 \cap T^{\mathrm{geo}}_qS_2 .
> $$
>
> *Lee: Theorem 6.30(b)*

^prop-11-10

> [!proof]+ Proof
> Write $T_i = T^{\mathrm{geo}}_qS_i = \ker G_i'(q)$, of dimension $k - \ell_i$. The kernel of the stacked map $(G_1,G_2)'(q) = \begin{pmatrix} G_1'(q) \\ G_2'(q)\end{pmatrix}$ is $T_1 \cap T_2$, so by [[Fundamental theorem of linear maps|rank–nullity]] it is surjective iff $\dim(T_1 \cap T_2) = k - \ell_1 - \ell_2$. On the other hand
>
> $$
> \dim(T_1 + T_2) = \dim T_1 + \dim T_2 - \dim(T_1 \cap T_2) = (k - \ell_1) + (k - \ell_2) - \dim(T_1 \cap T_2),
> $$
>
> which equals $k$ iff $\dim(T_1 \cap T_2) = k - \ell_1 - \ell_2$. The two conditions coincide. When they hold throughout $S_1 \cap S_2 = (G_1,G_2)^{-1}(0)$, the point $0$ is a regular value of $(G_1, G_2)$, and Theorems [[§4 The Regular Value Theorem#^thm-4-3|§4.3]] and [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]] give a manifold of codimension $\ell_1 + \ell_2$ with geometric tangent space $\ker(G_1,G_2)'(q) = T_1 \cap T_2$.

^pf-11-10

*Uses:* [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-6|Def. §11.6]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-4|Def. §11.4]], [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|§11.3]], [[§4 The Regular Value Theorem#^def-4-2|Def. §4.2]], [[§4 The Regular Value Theorem#^thm-4-3|§4.3]], [[Fundamental theorem of linear maps|LADR 3.21]], [[2C Dimension#^ladr-2-43|LADR 2.43]]

> [!example] Example §11.5: The Sphere and the Plane Re-read
> The figure in [[§4 The Regular Value Theorem#^rem-4-3|§4]] was a transversality picture. Let $S_1 = S^2$ and $S_2 = \{z = c\}$ in $\mathbb{R}^3$, so $T^{\mathrm{geo}}_qS_1 = q^\perp$ and $T^{\mathrm{geo}}_qS_2 = e_3^\perp$, the horizontal plane. Two planes through the origin in $\mathbb{R}^3$ sum to $\mathbb{R}^3$ iff they are distinct, so the intersection is transverse at $q$ iff $q^\perp \neq e_3^\perp$, i.e. iff $q \neq \pm e_3$ — iff the two normals $q$ and $e_3$ are independent, which is what the figure's caption said in the language of gradients.
> - $|c| < 1$: every point of $S_1 \cap S_2$ has $x^2 + y^2 = 1 - c^2 > 0$, so $q \neq \pm e_3$ and the intersection is transverse. Codimensions add, $1 + 1 = 2$, and $S_1 \cap S_2$ is a curve: the circle of radius $\sqrt{1-c^2}$.
> - $c = \pm 1$: $S_1 \cap S_2 = \{\pm e_3\}$, where $T^{\mathrm{geo}}_qS_1 = T^{\mathrm{geo}}_qS_2$. Not transverse, and the intersection is a point rather than the predicted curve.
> - $|c| > 1$: the intersection is empty, and transversality holds vacuously.

^ex-11-5

> [!example] Example §11.6: Two Ways Transversality Can Fail
> Let $S$ be the $x$-axis in $\mathbb{R}^2$, cut out by $G(x,y) = y$, so $T^{\mathrm{geo}}_qS$ is the $x$-axis at every $q \in S$, and $\ell = 1$. For $F : \mathbb{R} \to \mathbb{R}^2$ the theorem predicts $\dim F^{-1}(S) = 1 - 1 = 0$.
> - (a) $F(t) = (t, 0)$. Then $F^{-1}(S) = \mathbb{R}$, of dimension $1$: the *dimension* is wrong. Here $\operatorname{im} F'(t)$ is the $x$-axis, so $\operatorname{im} F'(t) + T S$ is the $x$-axis, not $\mathbb{R}^2$.
> - (b) $F(t) = (t, t^2)$. Then $F^{-1}(S) = \{0\}$, which has the predicted dimension $0$; but $F'(0) = (1,0)$ lies in $T^{\mathrm{geo}}_0S$, so $F'(0)^{-1}(T^{\mathrm{geo}}_0S) = \mathbb{R}$, while the geometric tangent space of a point is $0$: the *tangent formula* is wrong. Correspondingly $(G \circ F)(t) = t^2$ has $(G\circ F)'(0) = 0$, as [[§11 Tangent Spaces I꞉ The Geometric Picture#^prop-11-8|Proposition §11.8]] predicts.
> - (c) $F(t) = (t, t^2 - \varepsilon)$ with $\varepsilon > 0$. Now $F^{-1}(S) = \{\pm\sqrt\varepsilon\}$, and at these points $F'(t) = (1, 2t)$ has nonzero second component, so $\operatorname{im} F'(t) + TS = \mathbb{R}^2$: transverse, two points, and every conclusion of the theorem holds.

^ex-11-6

![[m591-11-5.svg]]
*The three maps of the example against the $x$-axis $S$ (blue): (a) the image lies in $S$; (b) the parabola is tangent to $S$ at the origin, its velocity (orange) lying in $S$; (c) the lowered parabola crosses $S$ transversally at two points.*

> [!remark] Remark
> Transversality protects the dimension and the tangent formula *independently*: (a) loses the first, (b) keeps the first and loses the second. And (c) shows what happens to the tangency of (b) under an arbitrarily small perturbation: it disappears, replaced by two transverse crossings (for $\varepsilon > 0$) or by no intersection at all (for $\varepsilon < 0$). The same happens to the tangent plane of [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-5|Example §11.5]] when it is moved slightly up or down.

^rem-11-12

> [!remark] Remark: Looking Ahead: Transversality Is Generic
> Two points of [[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-12|the remark above]] will be taken up once abstract manifolds and submanifolds are in place. First, the definition makes sense verbatim for a smooth map $F : X \to Y$ between abstract manifolds and a submanifold $S \subseteq Y$, with *abstract* tangent spaces and the differential of [[§12 Tangent Spaces II꞉ The Abstract Tangent Space|§12]] in place of $T^{\mathrm{geo}}$ and the Jacobian:
>
> $$
> dF_p(T_pX) + T_{F(p)}S = T_{F(p)}Y \qquad \text{for all } p \in F^{-1}(S),
> $$
>
> and [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-7|Theorem §11.7]] becomes the statement that *the preimage of a submanifold under a transverse map is a submanifold of the same codimension*. Second, as [[§11 Tangent Spaces I꞉ The Geometric Picture#^ex-11-6|Example §11.6]](c) suggests, transversality is the *typical* situation: any smooth map can be made transverse to a given submanifold by an arbitrarily small perturbation, and tangencies are non-generic accidents. This is the transversality theorem of Thom, and it is the entry point to intersection theory (Guillemin–Pollack, Ch. 2). Neither is part of the course yet.

^rem-11-13

> [!remark] Remark: What Is Still Missing
> Everything above presupposes an ambient $\mathbb{R}^{n+k}$: [[§11 Tangent Spaces I꞉ The Geometric Picture#^def-11-1|Definition §11.1]] of the geometric tangent space $T^{\mathrm{geo}}_pM$ uses its vector space structure to differentiate $\gamma$, and [[§11 Tangent Spaces I꞉ The Geometric Picture#^thm-11-3|Theorem §11.3]] uses the Jacobian of the defining map $F$. For an abstract smooth manifold neither is available — “if you have a sphere you can think of the tangent plane, but that is a subspace of $\mathbb{R}^3$. If you do not have $\mathbb{R}^3$, then what do you do? You do not have room to put your vectors.” [[§12 Tangent Spaces II꞉ The Abstract Tangent Space|The rest of this section]] builds the *abstract* tangent space $T_pM$ from the charts alone.

^rem-11-14
