---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 25
tags: [differentiable-manifolds, math591]
---
← [[§24 The Circle]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§26 Transversality]] →

*Stage: geometric — Tangent vectors as velocities inside the ambient space, $T^{\mathrm{geo}}_pM = \ker F'(p)$ — available only for manifolds presented by equations.*

*Reference: Lee Ch. 3, “Tangent Vectors.” Begun at the end of Lecture 7; the abstract definition is promised for Friday. Logistics: a grader (a doctoral student) has been assigned; HW3 Problem 1 is the diffeomorphism $\mathbb{R} \cong \widetilde{\mathbb{R}}$ of [[§19 Smooth Functions and Smooth Maps#^ex-19-1|Example §19.1]].*

> [!remark] Remark: Why This Section
> The goal is to attach to each point $p$ of a smooth manifold $M$ a vector space $T_pM$, the *abstract tangent space*, so that maps between manifolds acquire differentials $dF_p : T_pM \to T_{F(p)}N$ as in [[§22 The Differential of a Map Between Vector Spaces|§22]]. The obstacle is that the familiar picture — a plane resting on a surface — lives in an ambient space: “if you have a sphere you can think of the tangent plane, but that is a subspace of $\mathbb{R}^3$. If you do not have $\mathbb{R}^3$, then what do you do? You do not have room to put your vectors.” An abstract manifold has no ambient space, so the construction “is going to take a little while.” This section therefore treats the case where an ambient space *is* available, and defines there the *geometric tangent space* $T^{\mathrm{geo}}_pM$ — as motivation, and because it covers all the matrix groups. The abstract $T_pM$ is built in [[§27 Germs|§27]], and the cotangent space in [[§32 The Cotangent Space|§32]]. (Uribe noted that it is in some ways more natural to define the dual space first — the cotangent space — but follows Lee in not doing so.)

^rem-25-1

## The Geometric Tangent Space of a Regular Level Set

Throughout this subsection $W \subseteq \mathbb{R}^{n+k}$ is open, $F : W \to \mathbb{R}^k$ is smooth, $c \in \mathbb{R}^k$ is a regular value, and $M = F^{-1}(c)$, a smooth $n$-manifold by Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]. Fix $p \in M$.

> [!definition] Definition §25.1: Geometric Tangent Space
> The **geometric** (or **ambient**) **tangent space** to $M$ at $p$ is
>
> $$
> \begin{aligned}
> T^{\mathrm{geo}}_pM \;=\; \Big\{\, \gamma'(0) \;\Big|\;& \gamma : (-\varepsilon,\varepsilon) \to \mathbb{R}^{n+k} \text{ smooth},\ \varepsilon > 0, \\
> & \gamma\big((-\varepsilon,\varepsilon)\big) \subseteq M,\ \gamma(0) = p \,\Big\} \subseteq \mathbb{R}^{n+k},
> \end{aligned}
> $$
>
> where $\gamma'(0) = \frac{d\gamma}{dt}\big|_{t=0}$ is the ordinary derivative of a curve in $\mathbb{R}^{n+k}$. In words: $T^{\mathrm{geo}}_pM$ is the set of velocities at $p$ of smooth curves that pass through $p$ while staying on $M$. The same definition applies verbatim with $\mathbb{R}^{n+k}$ replaced by any finite-dimensional real vector space containing $M$, such as $\operatorname{Mat}(n,\mathbb{R})$, with $\gamma'(0)$ computed in that space.
>
> *Lee: Ch. 3 (geometric tangent vectors in $\mathbb{R}^n$) and Proposition 5.37*

^def-25-1

> [!remark]- Connections
> - The calculus picture: tangent vectors of constraint curves, [[§17 Optimization and Lagrange Multipliers#Geometric Insight: Tangent and Normal Vectors|452 §17]].
> - The abstract replacement: [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], identified with this one in [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Ambient and Abstract Agree, §29.6]]; velocities of curves return in [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]].

> [!remark] Remark
> **Notation.** Two different objects in this section are called “the tangent space at $p$”, and the notes keep them apart throughout. The *geometric* tangent space of [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1]] is written $T^{\mathrm{geo}}_pM$: it is a linear subspace of the Euclidean space $\mathbb{R}^{n+k}$ in which $M$ sits, and it exists only for manifolds presented inside a Euclidean space (here, regular level sets; also open subsets of $\mathbb{R}^N$ and of finite-dimensional vector spaces). The *abstract* tangent space of [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Definition §28.2]], built from derivations in [[§28 Derivations and the Abstract Tangent Space|§28]], is written plain $T_pM$: it exists for every smooth manifold, and is not a subset of anything. The phrase “tangent space” is always qualified by one of the two adjectives. The two are identified, for regular level sets, by [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6]] — but the identification is a theorem, not a definition. On the board they appeared as $(T_pM)^{\mathrm{ambient}}$ and $(T_pM)^{\mathrm{abstract}}$.

^rem-25-2

![[m591-11-1.svg]]
*A curve $\gamma$ on $M$ through $p$, its velocity $v = \gamma'(0)$, and the plane $T^{\mathrm{geo}}_pM$ swept out by all such velocities (drawn translated to $p$), orthogonal to the gradient $\nabla F(p)$.*

“Smooth” for $\gamma$ means smooth as a map into the Euclidean space $\mathbb{R}^{n+k}$; the constraint that it take values in $M$ is a separate condition. The derivative $\gamma'(0)$ is computed with the vector space structure of $\mathbb{R}^{n+k}$, which is exactly what an abstract manifold lacks. The figure shows the definition: a curve $\gamma$ drawn on $M$ through $p$, its velocity $v$ at $t=0$ (a vector of the ambient space, drawn from $p$), and the plane these velocities sweep out as $\gamma$ ranges over all such curves — which [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] identifies as $\ker F'(p)$, and which is therefore orthogonal to the gradient $\nabla F(p)$, shown in grey for contrast. Note that $T^{\mathrm{geo}}_pM$ is drawn as a plane through $p$ only as an aid: as a subspace of $\mathbb{R}^{n+k}$ it passes through the origin, and it is the *translate* to $p$ that is tangent to $M$.

It is not obvious from [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1]] that $T^{\mathrm{geo}}_pM$ is closed under addition: given two curves through $p$ with velocities $v$ and $w$, there is no evident curve with velocity $v + w$. “How do I add two curves?” Both this and the dimension follow from an algebraic description.

> [!theorem] Lemma §25.1: Locality of the Geometric Tangent Space
> If $M' \subseteq M$ is open in $M$ and $p \in M'$, then $T^{\mathrm{geo}}_pM' = T^{\mathrm{geo}}_pM$.

^lem-25-1

> [!proof]+ Proof
> $\subseteq$ is clear, a curve in $M'$ being a curve in $M$. For $\supseteq$, let $\gamma : (-\varepsilon,\varepsilon) \to M$ be smooth with $\gamma(0) = p$. Since $\gamma$ is continuous and $M'$ is open in $M$, the set $\gamma^{-1}(M')$ is open in $(-\varepsilon,\varepsilon)$ and contains $0$, so it contains an interval $(-\delta,\delta)$. The restriction $\gamma|_{(-\delta,\delta)}$ takes values in $M'$ and has the same velocity at $0$.

^pf-25-1

*Uses:* [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[§10 Continuous Functions#^def-10-1|590 Def. §10.1]]

> [!theorem] Lemma §25.2: The Geometric Tangent Space of a Graph
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

^lem-25-2

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

^pf-25-2

*Uses:* [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[Multivariable Chain Rule|452 §12.2]], [[Fundamental theorem of linear maps|LADR 3.21]]

> [!remark] Remark
> Uribe stated this lemma and left it as an exercise, calling it “not a trivial exercise”; the proof above is short but both inclusions are needed, and the $\supseteq$ half — lifting a straight line from the chart — is the construction that reappears in [[§27 Germs|§27]] as the curve defining $D_v$. In words: *the geometric tangent space to a graph is the graph of the differential.*

^rem-25-3

> [!remark]- Connections
> - For $n = 2$, $k = 1$ this is the tangent plane to a graph $z = f(x, y)$, [[§7 Differentiability#^def-7-4|452 Def. §7.4]].

> [!theorem] Theorem §25.3: The Geometric Tangent Space Is the Kernel of the Jacobian
> $T^{\mathrm{geo}}_pM = \ker F'(p)$, where $F'(p) : \mathbb{R}^{n+k} \to \mathbb{R}^k$ is the Jacobian at $p$. In particular $T^{\mathrm{geo}}_pM$ is a linear subspace of $\mathbb{R}^{n+k}$ of dimension $n = \dim M$.
>
> *Lee: Proposition 5.38*

^thm-25-3

> [!proof]+ Proof
> The order is Lecture 8's sketch, which built on an inclusion proved in Lecture 7.
>
> *1. The inclusion (Lecture 7: “last time we saw this inclusion”).* $T^{\mathrm{geo}}_pM \subseteq \ker F'(p)$. Let $v \in T^{\mathrm{geo}}_pM$ with $\gamma$ as in [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1]]. The composite $F \circ \gamma : (-\varepsilon,\varepsilon) \to \mathbb{R}^k$ is smooth, being a composite of smooth maps between Euclidean spaces, and since $\gamma(t) \in M = F^{-1}(c)$ for every $t$ it is the constant $c$. Differentiating at $t = 0$ and applying the [[Multivariable Chain Rule|chain rule]],
>
> $$
> \vec 0 = \frac{d}{dt}\Big|_{t=0} F(\gamma(t)) = F'(\gamma(0))\,\gamma'(0) = F'(p)\, v ,
> $$
>
> so $v \in \ker F'(p)$.
>
> *2. Everything is local near $p$, so WLOG $M$ is a graph.* “Since everything is local near $p$ … these regular level sets are locally graphs of functions, for various choices of variables.” *(Completion.)* By the proof of Theorem [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], after permuting coordinates there is an open box $V \times V'$ containing $p$ and a smooth $G : V \to V'$ with $M \cap (V \times V') = \{(x, G(x)) \mid x \in V\}$. By Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]] the geometric tangent space is unchanged on passing to this open piece.
>
> *3. The claim: the tangent space to a graph is the graph of the derivative.* $T^{\mathrm{geo}}_pM$ is the graph of $G'(x_0)$, where $p = (x_0, G(x_0))$ — set in lecture as “not a trivial exercise” and proved in Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]]. So $T^{\mathrm{geo}}_pM$ is a subspace of dimension $n$.
>
> *4. The kernel has dimension $n$, by rank–nullity.* Since $c$ is a regular value, $F'(p) : \mathbb{R}^{n+k} \to \mathbb{R}^k$ has rank $k$, so [[Fundamental theorem of linear maps|rank–nullity]] gives $\dim \ker F'(p) = (n+k) - k = n$.
>
> *5. “We must have equality.”* $T^{\mathrm{geo}}_pM$ is an $n$-dimensional subspace contained in the $n$-dimensional subspace $\ker F'(p)$, so the two are equal.

^pf-25-3

*Uses:* [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]], [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]], [[Multivariable Chain Rule|452 §12.2]], [[Fundamental theorem of linear maps|LADR 3.21]], [[§6 Dimension#^ladr-2-39|LADR 2.39]]

> [!remark]- Connections
> - Identified with the abstract tangent space: [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Ambient and Abstract Agree, §29.6]]; for submanifolds, [[§35 Submanifolds#^prop-35-4|§35.4]].
> - Orthogonality to the gradients is the geometry behind [[Method of Lagrange Multipliers|452 §17.2 (Lagrange multipliers)]].

> [!remark] Remark
> The structure is worth noticing, because it is not the obvious one. Only the *easy* inclusion is proved directly; the reverse inclusion is never constructed, but forced by a dimension count. Uribe: “it's best actually to prove something else” — namely the graph lemma, from which both the vector space structure and the dimension of $T^{\mathrm{geo}}_pM$ are immediate, after which “we must have equality.”

^rem-25-4

> [!theorem] Corollary §25.4: Three Descriptions of the Geometric Tangent Space
> In the notation of [[§25 The Geometric Tangent Space#^pf-25-3|the proof]], with $\alpha : V \to \mathbb{R}^{n+k}$, $\alpha(x) = (x, h(x))$ the parametrization inverse to the graph chart,
>
> $$
> T^{\mathrm{geo}}_pM \;=\; \{\text{velocities of curves in } M \text{ through } p\} \;=\; \ker F'(p) \;=\; \operatorname{im} D\alpha_a ,
> $$
>
> and $D\alpha_a : \mathbb{R}^n \to \mathbb{R}^{n+k}$, $u \mapsto (u, Dh_a u)$, is an isomorphism onto $T^{\mathrm{geo}}_pM$.
>
> *Lee: Propositions 5.37 and 5.38*

^cor-25-4

> [!proof]+ Proof
> The first equality is the definition and the second is [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]]. Step 2 of that proof shows every $v \in \ker F'(p)$ has the form $(v_1, Dh_a v_1) = D\alpha_a(v_1)$, so $\ker F'(p) \subseteq \operatorname{im} D\alpha_a$; and differentiating $F \circ \alpha \equiv c$ gives $F'(p) \circ D\alpha_a = 0$, so $\operatorname{im} D\alpha_a \subseteq \ker F'(p)$. $D\alpha_a$ is injective because its first $n$ components are the identity, and both spaces have dimension $n$.

^pf-25-4

*Uses:* [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[Multivariable Chain Rule|452 §12.2]], [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]

> [!remark] Remark
> The corollary is the infinitesimal form of [[§20 Manifolds in Euclidean Space|§20]]: the geometric tangent space can be read off from the *external* description as the kernel of the constraint map, or from the *internal* description as the image of the derivative of a parametrization, and the two agree. The geometric definition, via curves, is the one that makes no reference to either presentation — which is why it is the one that will generalize.

^rem-25-5

> [!remark]- Connections
> - The image description for surfaces in ℝ³, where $D\mathbf{X}$ has columns $\mathbf{X}_u, \mathbf{X}_v$: [[§31 Surface Integrals#^def-31-2|452 Def. §31.2]] and [[§31 Surface Integrals#^rem-31-3|452 §31, Regularity as a Rank Condition on the Derivative]].

## Examples

> [!example] Example §25.1: The Sphere
> For $S^n = F^{-1}(1)$ with $F(x) = |x|^2 = \sum x_i^2$ on $\mathbb{R}^{n+1}$, the Jacobian at $p$ is the row vector $F'(p) = 2p^{\mathsf T}$, and $1$ is a regular value since $p \neq 0$ on $S^n$. Hence
>
> $$
> T^{\mathrm{geo}}_pS^n = \ker\big(2p^{\mathsf T}\big) = \{\, v \in \mathbb{R}^{n+1} \mid p \cdot v = 0 \,\} = p^{\perp},
> $$
>
> the hyperplane orthogonal to the position vector — the tangent plane of calculus, now as a theorem. Directly from the definition: any curve $\gamma$ on the sphere satisfies $\gamma(t)\cdot\gamma(t) = 1$, so $2\,\gamma(t)\cdot\gamma'(t) = 0$, and at $t = 0$ this is $p \cdot v = 0$.

^ex-25-1

> [!remark]- Connections
> - The sphere in 452: [[Unit circle and unit sphere]].

The sphere through the course: a topological manifold with hemisphere charts in [[§8 Spheres|Spheres]]; the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$ in [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; the Riemann sphere $\mathbb{CP}^1$ in [[§18 Projective Spaces as Smooth Manifolds#^prop-18-4|the Riemann sphere]]; its geometric tangent spaces in [[§25 The Geometric Tangent Space#^ex-25-1|the tangent space of the sphere]] and its transverse intersection with a plane in [[§26 Transversality#^ex-26-1|the sphere and the plane re-read]]; the double cover $S^n \to \mathbb{RP}^n$ and the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ in [[§39 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]]; and $S^3 = \mathrm{SU}(2)$ in [[§40 The Unit Quaternions and SU(2)#^prop-40-5|the unit quaternions as SU(2)]].

> [!example] Example §25.2: The Orthogonal Group
> For $\mathrm{O}(n) = F^{-1}(I)$ with $F : \operatorname{Mat}(n,\mathbb{R}) \to \operatorname{Sym}(n,\mathbb{R})$, $F(g) = gg^{\mathsf T}$, [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] applies after identifying both spaces with Euclidean spaces by linear coordinates, under which the Jacobian corresponds to the differential $dF_g$ of [[§22 The Differential of a Map Between Vector Spaces#^def-22-5|Definition §22.5]]. Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]] then gives
>
> $$
> T^{\mathrm{geo}}_g\mathrm{O}(n) = \ker dF_g = g \cdot \operatorname{Skew}(n,\mathbb{R}), \qquad T^{\mathrm{geo}}_I \mathrm{O}(n) = \operatorname{Skew}(n,\mathbb{R}),
> $$
>
> of dimension $\tfrac{n(n-1)}{2}$, as it must be. Directly from the definition, at $g = I$: if $\gamma$ is a curve of orthogonal matrices with $\gamma(0) = I$, then $\gamma(t)\gamma(t)^{\mathsf T} = I$ for all $t$; differentiating at $0$ gives $\gamma'(0) + \gamma'(0)^{\mathsf T} = 0$, so the velocity is skew-symmetric. This geometric tangent space at the identity is the object that will later be called the *Lie algebra* $\mathfrak{so}(n)$.

^ex-25-2

> [!remark] Remark
> For $\mathrm{O}(n)$ the ambient space is $\operatorname{Mat}(n,\mathbb{R})$ rather than $\mathbb{R}^{n^2}$; [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1]] is used in its vector-space form, and [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] transfers across the linear isomorphism of Proposition [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]]. The description $T^{\mathrm{geo}}_g\mathrm{O}(n) = g \cdot T^{\mathrm{geo}}_I\mathrm{O}(n)$ — every geometric tangent space is a translate of the one at the identity — is the first sign that a group structure simplifies the tangent bundle; it will be a general fact about Lie groups.

^rem-25-6

> [!example] Example §25.3: The Unitary Group
> By Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|§23.4]] and [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] (transferred to the real vector space $\operatorname{Mat}(n,\mathbb{C})$ as in [[§25 The Geometric Tangent Space#^rem-25-6|the note above]]),
>
> $$
> T^{\mathrm{geo}}_g\mathrm{U}(n) = \ker dF_g = \mathfrak{u}(n)\cdot g = g\cdot\mathfrak{u}(n), \qquad T^{\mathrm{geo}}_I\mathrm{U}(n) = \mathfrak{u}(n).
> $$
>
> Directly from the definition at $g = I$: a curve of unitary matrices with $\gamma(0) = I$ satisfies $\gamma(t)\gamma(t)^* = I$, and differentiating at $0$ gives $\gamma'(0) + \gamma'(0)^* = 0$.

^ex-25-3

> [!theorem] Theorem §25.5: The Classical Groups
> Each classical group of [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Theorem §12.6]] is a smooth manifold, of the dimension and with the geometric tangent space at the identity given below. Moreover, for $G = \mathrm{SL}(n,\mathbb{R}), \mathrm{O}(n), \mathrm{SO}(n), \mathrm{U}(n)$ and every $g \in G$,
>
> $$
> T^{\mathrm{geo}}_g G \;=\; g \cdot T^{\mathrm{geo}}_I G \;=\; T^{\mathrm{geo}}_I G \cdot g .
> $$
>
> *Lee: Examples 7.27–7.30*

^thm-25-5

| Group $G$ | Presentation | $\dim G$ | $T^{\mathrm{geo}}_I G$ |
|---|---|:---:|---|
| $\mathrm{GL}(n,\mathbb{R})$ | open in $\operatorname{Mat}(n,\mathbb{R})$ | $n^2$ | $\operatorname{Mat}(n,\mathbb{R})$ |
| $\mathrm{GL}(n,\mathbb{C})$ | open in $\operatorname{Mat}(n,\mathbb{C})$ | $2n^2$ | $\operatorname{Mat}(n,\mathbb{C})$ |
| $\mathrm{SL}(n,\mathbb{R})$ | $\det^{-1}(1)$ | $n^2 - 1$ | $\mathfrak{sl}(n) = \{A \mid \operatorname{tr} A = 0\}$ |
| $\mathrm{O}(n)$ | $F^{-1}(I)$, $F(g) = gg^{\mathsf T} \in \operatorname{Sym}(n,\mathbb{R})$ | $\tfrac{n(n-1)}{2}$ | $\mathfrak{so}(n) = \operatorname{Skew}(n,\mathbb{R})$ |
| $\mathrm{SO}(n)$ | open in $\mathrm{O}(n)$ | $\tfrac{n(n-1)}{2}$ | $\mathfrak{so}(n)$ |
| $\mathrm{U}(n)$ | $F^{-1}(I)$, $F(g) = gg^* \in \operatorname{Herm}(n)$ | $n^2$ | $\mathfrak{u}(n) = \{X \mid X^* = -X\}$ |

> [!proof]+ Proof
> *The general linear groups.* An open subset $U$ of a finite-dimensional vector space $V$ is a smooth manifold of dimension $\dim V$ (one chart, the restriction of a linear chart). [[§25 The Geometric Tangent Space#^def-25-1|Definition §25.1]] makes sense verbatim for $U \subseteq V$, and every $v \in V$ is the velocity of the curve $t \mapsto p + tv$, which stays in $U$ for small $|t|$; so $T^{\mathrm{geo}}_pU = V$.
>
> *$\mathrm{SL}(n,\mathbb{R})$.* Smoothness and dimension are Corollary [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]] with Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]. By Proposition [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], $d(\det)_g(A) = \det(g)\,\operatorname{tr}(g^{-1}A)$, so for $g \in \mathrm{SL}(n,\mathbb{R})$ [[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]] gives $T^{\mathrm{geo}}_g\mathrm{SL} = \{A \mid \operatorname{tr}(g^{-1}A) = 0\}$. Writing $A = gB$ this is $g\cdot\mathfrak{sl}(n)$; writing $A = Bg$ and using $\operatorname{tr}(g^{-1}Bg) = \operatorname{tr} B$, it is $\mathfrak{sl}(n)\cdot g$. The trace condition removes one dimension, consistently with $n^2 - 1$.
>
> *$\mathrm{O}(n)$ and $\mathrm{SO}(n)$.* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Example §23.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|Corollary §23.2]], and [[§25 The Geometric Tangent Space#^ex-25-2|Example §25.2]]; since $\mathrm{SO}(n)$ is open in $\mathrm{O}(n)$ its geometric tangent spaces are those of $\mathrm{O}(n)$ ([[§25 The Geometric Tangent Space#^lem-25-1|Lemma §25.1]]). For the right translate, $\operatorname{Skew}(n,\mathbb{R})$ is preserved by conjugation by orthogonal $g$, exactly as in the proof of Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|§23.4]].
>
> *$\mathrm{U}(n)$.* [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Example §23.2]] and [[§25 The Geometric Tangent Space#^ex-25-3|Example §25.3]].

^pf-25-5

*Uses:* [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|§12.6]], [[§22 The Differential of a Map Between Vector Spaces#^prop-22-2|§22.2]], [[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]], [[§12 The Classical Groups Are Topological Manifolds#^cor-12-5|§12.5]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|§12.1]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|Ex. §23.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^cor-23-2|§23.2]], [[§25 The Geometric Tangent Space#^ex-25-2|Ex. §25.2]], [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|§23.4]], [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|Ex. §23.2]], [[§25 The Geometric Tangent Space#^ex-25-3|Ex. §25.3]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]

> [!remark]- Connections
> - Used in Relativity: the Lorentz analogue: infinitesimal Lorentz transformations are the matrices antisymmetric with respect to $\eta$, six generators for three rotations and three boosts — [[§B1.2 Lorentz Transformations and the Lorentz Group#^rem-b1-2-6|REL Remark: Infinitesimal Lorentz transformations]].
> - Used in Quantum Mechanics: the Lie algebra of $SO(3)$, the antisymmetric matrices with the commutator, is $\mathbb R^3$ with the cross product — [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^rem-c5-1-1|QM ★ Remark: The Lie algebra of SO(3)]].
> - Used in Quantum Field Theory: the tangent space at the identity of a matrix Lie group as its Lie algebra, with generators and structure constants; $\mathfrak{so}(3)$ and $\mathfrak{su}(2) \subset \mathfrak u(2)$ are isomorphic although the groups are not — [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|QFT Def. §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|QFT Theorem §C3.1.1]].

> [!definition] Definition §25.2: Adjoint Action
> Let $G$ be one of $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$, and $\mathfrak{g} = T^{\mathrm{geo}}_I G$. For $g \in G$, **conjugation** by $g$ is $\mathrm{Ad}_g(X) = gXg^{-1}$. The **adjoint action** of $G$ on $\mathfrak{g}$ is $g \mapsto \mathrm{Ad}_g|_{\mathfrak{g}}$; that each $\mathrm{Ad}_g$ maps $\mathfrak{g}$ onto itself is part of [[§25 The Geometric Tangent Space#^prop-25-6|the next proposition]].

^def-25-2

> [!remark]- Connections
> - Conjugation as a group action on the group itself: [[§34 Conjugation as an Action and the Class Equation#^prop-34-1|493 §34.1]]; $\mathrm{Ad}_g$ is conjugation acting on $T^{\mathrm{geo}}_IG$.

> [!theorem] Proposition §25.6: The Adjoint Action
> Let $G$ be one of $\mathrm{SL}(n,\mathbb{R})$, $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{U}(n)$, and $\mathfrak{g} = T^{\mathrm{geo}}_I G$. For $g \in G$ the conjugation
>
> $$
> \mathrm{Ad}_g : \mathfrak{g} \to \mathfrak{g}, \qquad \mathrm{Ad}_g(X) = gXg^{-1},
> $$
>
> is a linear isomorphism, with $\mathrm{Ad}_{gh} = \mathrm{Ad}_g \circ \mathrm{Ad}_h$. Left and right multiplication $L_g(X) = gX$ and $R_g(X) = Xg$ satisfy $L_g = R_g \circ \mathrm{Ad}_g$.

^prop-25-6

> [!proof]+ Proof
> That $\mathrm{Ad}_g$ maps $\mathfrak{g}$ into itself is checked case by case, with $\mathfrak{g}$ as in [[§25 The Geometric Tangent Space#^thm-25-5|Theorem §25.5]]. For $\mathfrak{sl}(n)$: $\operatorname{tr}(gXg^{-1}) = \operatorname{tr} X$. For $g$ orthogonal and $X$ skew: $(gXg^{-1})^{\mathsf T} = (gXg^{\mathsf T})^{\mathsf T} = gX^{\mathsf T}g^{\mathsf T} = -gXg^{-1}$. For $g$ unitary and $X$ skew-Hermitian: $(gXg^*)^* = gX^*g^* = -gXg^{-1}$. $\mathrm{Ad}_g$ is linear, $\mathrm{Ad}_{gh}X = ghXh^{-1}g^{-1} = \mathrm{Ad}_g(\mathrm{Ad}_h X)$, and $\mathrm{Ad}_{g^{-1}}$ is an inverse. Finally $R_g(\mathrm{Ad}_g X) = gXg^{-1}g = gX$.

^pf-25-6

*Uses:* [[§25 The Geometric Tangent Space#^def-25-2|Def. §25.2]], [[§25 The Geometric Tangent Space#^thm-25-5|§25.5]], [[§33 Trace꞉ A Connection Between Matrices and Operators#^ladr-8-49|LADR 8.49]]

> [!remark] Remark: Left and Right Translates
> The notes computed $T^{\mathrm{geo}}_g\mathrm{O}(n) = g\cdot\operatorname{Skew}(n)$ by writing $A = gB$ (Proposition [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-1|§23.1]]); [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^prop-23-4|Assignment 2]] computed $T^{\mathrm{geo}}_g\mathrm{U}(n) = \mathfrak{u}(n)\cdot g$ by writing $h = Xg$. Neither choice is privileged, and by [[§25 The Geometric Tangent Space#^prop-25-6|the proposition]] the two agree, $g \cdot \mathfrak{g} = \mathrm{Ad}_g(\mathfrak{g}) \cdot g = \mathfrak{g} \cdot g$. This is the first structural fact about Lie groups to appear in the course: the geometric tangent space at the identity, carried to every other point by left or right multiplication, determines all the geometric tangent spaces. The spaces $\mathfrak{sl}(n)$, $\mathfrak{so}(n)$, $\mathfrak{u}(n)$ in the table will reappear as *Lie algebras*.

^rem-25-7

![[m591-11-2.svg]]
*Left multiplication $L_g$ and right multiplication $R_g$ both carry $T^{\mathrm{geo}}_IG$ onto $T^{\mathrm{geo}}_gG$, and the triangle commutes: $L_g = R_g \circ \mathrm{Ad}_g$.*

Left and right multiplication by $g$ both carry $T^{\mathrm{geo}}_IG$ isomorphically onto $T^{\mathrm{geo}}_gG$, and they differ by the adjoint action: $L_g = R_g \circ \mathrm{Ad}_g$, since $(gXg^{-1})g = gX$. The two descriptions of $T^{\mathrm{geo}}_gG$ agree precisely because $\mathrm{Ad}_g$ maps $T^{\mathrm{geo}}_IG$ onto itself.

> [!definition] Definition §25.3: The Hat Map
> The **hat map** $\mathbb{R}^3 \to \operatorname{Skew}(3,\mathbb{R})$ sends $v = (v_1, v_2, v_3)$ to
>
> $$
> \hat v = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix},
> $$
>
> a linear isomorphism, characterized by $\hat v\, x = v \times x$ for all $x \in \mathbb{R}^3$.

^def-25-3

> [!example] Example §25.4: $\mathrm{SO}(3)$ and Infinitesimal Rotations
> $T^{\mathrm{geo}}_I\mathrm{SO}(3) = \operatorname{Skew}(3,\mathbb{R})$ is $3$-dimensional, and it is identified with $\mathbb{R}^3$ by the hat map of [[§25 The Geometric Tangent Space#^def-25-3|Definition §25.3]]
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
> For a unit vector $n$, choose $Q \in \mathrm{SO}(3)$ with $Qe_3 = n$ (possible by [[§14 Homogeneous Spaces#^ex-14-3|Example §14.3]]); the rotation about $n$ by angle $t$ is $QR(t)Q^{\mathsf T}$, with velocity $Q\hat e_3 Q^{\mathsf T} = \widehat{Qe_3} = \hat n$ at $t = 0$, using the identity $\widehat{Qv} = Q\hat vQ^{\mathsf T}$ for $Q \in \mathrm{SO}(3)$, which holds because rotations preserve the cross product. Scaling the speed, every $\hat v$ is attained: *a tangent vector to $\mathrm{SO}(3)$ at the identity is an angular velocity*, with direction the axis and length the rate of rotation.

^ex-25-4

> [!remark] Remark
> This connects the $\mathrm{SO}(3)$ material of [[§13 Group Actions and Orbit Spaces|§13]] and [[§14 Homogeneous Spaces|§14]] with the geometric tangent space. The three dimensions of $\mathrm{SO}(3)$ are the two needed to specify an axis, a point of $S^2$, and one for the angle about it — matching $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ of [[§14 Homogeneous Spaces#^ex-14-3|Example §14.3]], with the isotropy $\mathrm{SO}(2)$ being exactly the rotations about the fixed axis.

^rem-25-8

The classical groups through the course: defined in [[§11 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§16 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§12 The Classical Groups Are Topological Manifolds#^thm-12-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§13 Group Actions and Orbit Spaces#^ex-13-4|the rotations of the plane]] and [[§13 Group Actions and Orbit Spaces#^ex-13-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§14 Homogeneous Spaces#^ex-14-2|the isotropy of the north pole]] and [[§14 Homogeneous Spaces#^ex-14-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§15 The Topology of G∕H and Real Grassmannians#^cor-15-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-1|the orthogonal group]] and [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|the unitary group]]; their tangent spaces at the identity in [[§25 The Geometric Tangent Space#^thm-25-5|The Classical Groups]], with [[§25 The Geometric Tangent Space#^ex-25-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|The Double Cover]].

> [!remark] Remark: Dimension Checks through Homogeneous Spaces
> In every homogeneous space met so far, $\dim G/H = \dim G - \dim H$:
> - $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$:  $3 - 1 = 2$;
> - $\mathrm{Gr}_k(\mathbb{R}^n) = \mathrm{O}(n)/\big(\mathrm{O}(k)\times\mathrm{O}(n-k)\big)$:  $\tfrac{n(n-1)}{2} - \tfrac{k(k-1)}{2} - \tfrac{(n-k)(n-k-1)}{2} = k(n-k)$;
> - $S^{2n+1} = \mathrm{U}(n+1)/\mathrm{U}(n)$:  $(n+1)^2 - n^2 = 2n+1$;
> - $\mathbb{CP}^n = \mathrm{U}(n+1)/\big(\mathrm{U}(1)\times\mathrm{U}(n)\big)$:  $(n+1)^2 - 1 - n^2 = 2n$, the real dimension found from charts in [[§18 Projective Spaces as Smooth Manifolds#^thm-18-2|Theorem §18.2]].
>
> The first two identifications are proved in [[§14 Homogeneous Spaces|§14]]–[[§15 The Topology of G∕H and Real Grassmannians|§15]]; the last two are their complex analogues — $\mathrm{U}(n+1)$ acts transitively on unit vectors of $\mathbb{C}^{n+1}$ and on complex lines — and are not proved here. The formula itself is heuristic until quotient manifolds are available, when it becomes a theorem; for now it is a consistency check linking four separate computations.

^rem-25-9

## The Dimension of the Geometric Tangent Space

> [!theorem] Theorem §25.7: Dimension of the Geometric Tangent Space
> Let $M = F^{-1}(c) \subseteq \mathbb{R}^{n+k}$ be as in Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], a manifold of dimension $n$. Then for every $p \in M$,
>
> $$
> \dim T^{\mathrm{geo}}_pM = n = \dim M .
> $$
>
> The geometric tangent space ([[§25 The Geometric Tangent Space#^def-25-1|Def. §25.1]]) has the same dimension at every point, and it is the dimension of the manifold.

^thm-25-7

> [!proof]+ Proof
> *(The last sentence of Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], recorded as a theorem in its own right.)* By Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], $T^{\mathrm{geo}}_pM = \ker F'(p)$. Since $c$ is a regular value, the $k \times (n+k)$ matrix $F'(p)$ has rank $k$, so by rank–nullity ([[Fundamental theorem of linear maps|LADR 3.21]]) $\dim \ker F'(p) = (n + k) - k = n$.

^pf-25-7

*Uses:* [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§7 The Regular Value Theorem#^def-7-3|Def. §7.3]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[Fundamental theorem of linear maps|LADR 3.21]]

The count is the geometric meaning of “$k$ independent equations in $n + k$ unknowns”: each equation removes one tangent direction, and $n$ remain at every point. Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]] gives the same number for the abstract tangent space, as it must, since the two spaces are isomorphic (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]).

## From Tangent Vectors to Derivations

*Motivation only; nothing in this subsection is used later, but it is where the abstract definition comes from.*

Keep $M = F^{-1}(c)$ and, by Lemmas [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]] and [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]], assume $M$ is the graph of a smooth $G : A \to \mathbb{R}^k$ over an open $A \subseteq \mathbb{R}^n$, with chart $\varphi : M \to A$ the projection $(x, G(x)) \mapsto x$ and $p = (x_0, G(x_0))$. Let $f : M \to \mathbb{R}$ be smooth, so that $f_\varphi = f \circ \varphi^{-1} : A \to \mathbb{R}$ is smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-2|§19.2]]).

Given $v \in T^{\mathrm{geo}}_pM$, Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]] provides a unique $u \in \mathbb{R}^n$ with $v = (u, G'(x_0)u)$. Lift the straight line $t \mapsto x_0 + tu$ from the chart to the manifold:

$$
\gamma(t) = \big(x_0 + tu,\; G(x_0 + tu)\big), \qquad \gamma(0) = p, \quad \gamma'(0) = v .
$$

![[m591-12-1.svg]]
*The chart triangle for the graph case, as drawn on the board. Downstairs is the open set $A \subseteq \mathbb{R}^n$; upstairs is the manifold. The chart $\varphi(x, G(x)) = x$ and its inverse $\varphi^{-1}(x) = (x, G(x))$ pass between them, and the triangle commutes: $f = f_\varphi \circ \varphi$. Smoothness of $f$* means *smoothness of $f_\varphi$, so every computation with $f$ can be pushed downstairs, done in ordinary calculus, and read back. That is the manoeuvre in the next definition: the curve is built downstairs as a straight line, lifted upstairs by $\varphi^{-1}$, and the derivative taken downstairs again. “Upstairs and downstairs are very useful terminologies.”*

> [!definition] Definition §25.4: The Directional Derivative Attached to a Tangent Vector
> Let $M \subseteq \mathbb{R}^{n+k}$ be the graph of a smooth $G : A \to \mathbb{R}^k$ on an open $A \subseteq \mathbb{R}^n$, with chart $\varphi(x, G(x)) = x$, and $p = (x_0, G(x_0))$. Let $v \in T^{\mathrm{geo}}_pM$, let $u \in \mathbb{R}^n$ be the vector with $v = (u, G'(x_0)u)$ (Lemma [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]]), and let $\gamma(t) = (x_0 + tu, G(x_0 + tu))$ be the lifted line, a curve in $M$ with $\gamma(0) = p$ and $\gamma'(0) = v$. For $f$ a smooth real-valued function on a neighbourhood of $p$ in $M$, set
>
> $$
> D_v(f) \;=\; \frac{d}{dt}\Big|_{t=0} f(\gamma(t)) \;=\; \frac{d}{dt}\Big|_{t=0} f_\varphi(x_0 + tu) \;=\; u \cdot \nabla f_\varphi(x_0),
> $$
>
> the second equality because $\varphi(\gamma(t)) = x_0 + tu$ and $f = f_\varphi \circ \varphi$, the third by the [[Multivariable Chain Rule|chain rule]]. So $D_v$ takes a smooth function defined near $p$ and returns a real number, and it depends only on the values of $f$ near $p$ — which is what the germs of the next subsection make precise.
>
> *Lee: Proposition 3.2 (in $\mathbb{R}^n$)*

^def-25-4

> [!remark]- Connections
> - The Euclidean directional derivative and its gradient formula: [[Directional Derivative Formula|452 §9.1 (Directional Derivative Formula)]].
> - In $\mathbb{R}^n$ the trade $v \leftrightarrow D_v$ is exactly the identification of [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]; on an arbitrary manifold, velocities of curves: [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]].

> [!theorem] Proposition §25.8: Basic Properties of $D_v$
> In the setting of Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]]:
> 1. $D_v(f)$ depends only on the germ of $f$ at $p$;
> 2. if $\sigma$ is *any* smooth curve in $M$ with $\sigma(0) = p$ and $\sigma'(0) = v$, then $D_v(f) = \frac{d}{dt}\big|_{t=0} f(\sigma(t))$; so $D_v$ depends on $v$ alone, not on the curve used to define it;
> 3. $D_v$ is linear and obeys the product rule $D_v(fg) = f(p)\,D_v(g) + g(p)\,D_v(f)$.

^prop-25-8

> [!proof]+ Proof
> (1) $\gamma(t)$ lies in any given neighbourhood of $p$ for $|t|$ small, so only the values of $f$ near $p$ enter — “we don't need the whole manifold.” (2) The chart $\varphi$ is the restriction to $M$ of the linear projection $(x,y) \mapsto x$, so $\varphi \circ \sigma$ is a smooth curve in $A$ whose velocity at $0$ is the first component $u$ of $v$. Since $f \circ \sigma = f_\varphi \circ (\varphi \circ \sigma)$, the chain rule gives $\frac{d}{dt}\big|_0 f(\sigma(t)) = \nabla f_\varphi(x_0) \cdot u = D_v(f)$. (3) Linearity and the product rule are inherited from those of the gradient, $\nabla(f_\varphi g_\varphi) = f_\varphi \nabla g_\varphi + g_\varphi \nabla f_\varphi$, evaluated at $x_0$, where $f_\varphi(x_0) = f(p)$.

^pf-25-8

*Uses:* [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]], [[Multivariable Chain Rule|452 §12.2]], [[§8 Algebra of Differentiable Functions#^thm-8-2|452 §8.2]]

> [!theorem] Proposition §25.9: $D_v$ Determines $v$
> The map $v \mapsto D_v$ is injective on $T^{\mathrm{geo}}_pM$: if $D_v = D_{v'}$ then $v = v'$.
>
> *Lee: Proposition 3.2(b)*

^prop-25-9

> [!proof]+ Proof
> Write $v = (u, G'(x_0)u)$ and $v' = (u', G'(x_0)u')$. For $i = 1, \ldots, n$ let $x^i : M \to \mathbb{R}$ be the $i$-th coordinate of the chart, so $(x^i)_\varphi = r^i$ is the $i$-th coordinate function on $A$ and $\nabla (x^i)_\varphi = e_i$. Then $D_v(x^i) = u \cdot e_i = u^i$. If $D_v = D_{v'}$, applying both to $x^i$ gives $u^i = (u')^i$ for every $i$, so $u = u'$ and hence $v = v'$.

^pf-25-9

*Uses:* [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§25 The Geometric Tangent Space#^lem-25-2|§25.2]]

> [!remark] Remark
> Uribe's version of this argument: the numbers $D_v(f) = u \cdot \nabla f_\varphi(x_0)$ range over the dot products of $u$ with an arbitrary vector, because the gradient of a function at a point can be prescribed freely; so knowing all of them determines $u$. Taking $f$ to be the coordinate functions is the cheapest way to prescribe it.
>
> The conclusion is that a tangent vector loses nothing by being replaced by the operator it defines — and the operator, unlike the vector, makes sense with no ambient space in sight. *Tangent vectors will be defined as operators:* you feed them a function and they return a number.

^rem-25-10
