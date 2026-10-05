---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 28
tags: [differentiable-manifolds, math591]
---
← [[§27 Coordinate Derivations and the Basis Theorem]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§29 Tangent Vectors as Velocities of Curves]] →

*Stage: abstract — In charts the differential $F_{\ast p}$ is the Jacobian of the coordinate representation, and the chain rule is matrix multiplication.*

*Lecture 9. The differential $F_{\ast p}$ is defined without coordinates; choosing charts on both sides turns it into a matrix, and the matrix is the Jacobian of the coordinate representation. “This should be very much reminiscent of the things we said about vector spaces — another instance of the same thing.”*

Let $F : M \to N$ be smooth, $\dim M = m$, $\dim N = n$, and $p \in M$. Choose smooth charts $(U, \varphi)$ of $M$ with $p \in U$ and $(V, \psi)$ of $N$ with $F(U) \subseteq V$ — possible because $F$ is smooth (Definition [[§18 Smooth Functions and Smooth Maps#^def-18-3|§18.3]]) — and write

$$
\varphi = (x^1, \ldots, x^m), \qquad \psi = (y^1, \ldots, y^n), \qquad \tilde F = \psi \circ F \circ \varphi^{-1}, \qquad F^j = y^j \circ F : U \to \mathbb{R}.
$$

By Theorem [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|§27.5]] there are bases

$$
\mathcal{B}_M = \Big\{ \frac{\partial}{\partial x^i}\Big|_p \Big\}_{i=1}^m \ \text{ of } T_pM, \qquad \mathcal{B}_N = \Big\{ \frac{\partial}{\partial y^j}\Big|_{F(p)} \Big\}_{j=1}^n \ \text{ of } T_{F(p)}N .
$$

![[m591-12-9.svg]] ![[m591-12-10.svg]]
*Left, the maps: upstairs $F$ between manifolds, downstairs its coordinate representation $\tilde F$ between open sets of Euclidean space. Right, their linearizations: upstairs the differential, intrinsic; downstairs the Jacobian matrix, and the vertical isomorphisms send $\partial/\partial x^i|_p \mapsto e_i$ and $\partial/\partial y^j|_{F(p)} \mapsto e_j$. Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] below says the right-hand square commutes. It is the square of [[§21 The Differential of a Map Between Vector Spaces|§21, The Differential of a Map Between Vector Spaces]] again, with abstract tangent spaces in place of abstract vector spaces and coordinate bases in place of linear coordinates.*

> [!theorem] Proposition §28.1: Partial Derivatives Upstairs and Downstairs
> Let $F : M \to N$ be smooth, with smooth charts $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ and $(V, \psi = (y^1, \ldots, y^n))$ of $N$ such that $F(U) \subseteq V$. Let $F^j = y^j \circ F : U \to \mathbb{R}$ be the components of $F$, functions on the manifold, and $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^n$ the coordinate representation, with components $\tilde F^j = r^j \circ \tilde F$, functions on Euclidean space. Then $F^j \circ \varphi^{-1} = \tilde F^j$, and therefore, for every $p \in U$,
>
> $$
> \underbrace{\frac{\partial F^j}{\partial x^i}(p)}_{\text{upstairs, on } M} \;=\; \underbrace{\frac{\partial \tilde F^j}{\partial r^i}\big(\varphi(p)\big)}_{\text{downstairs, in } \mathbb{R}^m} .
> $$

^prop-28-1

> [!proof]+ Proof
> $F^j \circ \varphi^{-1} = y^j \circ F \circ \varphi^{-1} = r^j \circ \psi \circ F \circ \varphi^{-1} = r^j \circ \tilde F = \tilde F^j$ on $\varphi(U)$, using $y^j = r^j \circ \psi$. So the coordinate representation of the function $F^j$ is $\tilde F^j$, and by Definition [[§27 Coordinate Derivations and the Basis Theorem#^def-27-2|§27.2]], $\partial F^j/\partial x^i(p) = \partial (F^j \circ \varphi^{-1})/\partial r^i(\varphi(p)) = \partial \tilde F^j/\partial r^i(\varphi(p))$.

^pf-28-1

*Uses:* [[§27 Coordinate Derivations and the Basis Theorem#^def-27-1|Def. §27.1]], [[§27 Coordinate Derivations and the Basis Theorem#^def-27-2|Def. §27.2]]

> [!remark] Remark: Why This Identity Carries So Much
> Uribe stated it in Lecture 10 and recalled it at the decisive moment of Lecture 11 — it is marked with “!!!” on page 30 of the handwritten notes. When a student asked whether the matrix in the proof of the normal form should be written with $\tilde F$, the answer was: “it's the same thing … that's how we define partials.” Partial derivatives on a manifold are *defined* by going downstairs, so the matrix of partials of the components $F^j$ upstairs is literally the ordinary Jacobian of $\tilde F$ downstairs. This is what turns every local computation on a manifold into calculus in $\mathbb{R}^m$, and it is used in:
> 1. the matrix of the differential (Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]]), which is a one-line proof because of it;
> 2. regular values in one chart (Proposition [[§28 The Differential in Coordinates#^prop-28-7|§28.7]]): the rank of $F_{*p}$ is the rank of $\tilde F'(\varphi(p))$;
> 3. the proof of the local normal form (Theorem [[§32 Submersions#^thm-32-4|§32.4]]), where the matrix $\big[\partial F^j/\partial x^i(p)\big]$ is built from the components $F^j$ but is the Jacobian of $\tilde F$;
> 4. [[§28 The Differential in Coordinates#^rem-28-5|Assignment 3, Problem 4]], whose “matching coefficients” step computes $F_{*p}(\partial/\partial u_k|_p)[x^j]$ as an ordinary partial derivative of $F_\varphi$.
>
> Both sides depend on the charts: changing $\varphi$ or $\psi$ changes the matrix (Corollary [[§28 The Differential in Coordinates#^cor-28-4|§28.4]]), while $F_{*p}$ itself does not.

^rem-28-1

> [!theorem] Theorem §28.2: The Matrix of the Differential
> $F_{*p}$ is linear, and
>
> $$
> F_{*p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = \sum_{j=1}^n \frac{\partial F^j}{\partial x^i}(p)\, \frac{\partial}{\partial y^j}\Big|_{F(p)} .
> $$
>
> So the matrix of $F_{*p}$ in the bases $\mathcal{B}_M$, $\mathcal{B}_N$ has the upstairs partials $\partial F^j/\partial x^i(p)$ as entries, and by Proposition [[§28 The Differential in Coordinates#^prop-28-1|§28.1]] it is the $n \times m$ Jacobian of the coordinate representation,
>
> $$
> \Big[\, \frac{\partial F^j}{\partial x^i}(p) \,\Big]_{j, i} = \tilde F'\big(\varphi(p)\big),
> $$
>
> with $j$ the row index and $i$ the column index.
>
> *Lee: Ch. 3, Computations in Coordinates*

^thm-28-2

> [!proof]+ Proof
> *(Lecture 10 — “once you think about it a little bit, it's a one-line proof.”)* Linearity is Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-5|§26.5]]. The $i$-th column of the matrix consists of the coefficients of $F_{\ast p}(\partial/\partial x^i|_p)$ in the basis $\mathcal{B}_N$, and the universal formula of Theorem [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|§27.5]], applied at $F(p)$ with the chart $\psi$, says the $j$-th coefficient of any derivation is its value on $[y^j]$. By the definition of the pushforward,
>
> $$
> F_{*p}\Big(\frac{\partial}{\partial x^i}\Big|_p\Big)\big[y^j\big] = \frac{\partial}{\partial x^i}\Big|_p\big[y^j \circ F\big] = \frac{\partial F^j}{\partial x^i}(p).
> $$
>
> That is the formula. For the identification with $\tilde F'(\varphi(p))$ — the “claim” of the lecture — this is Proposition [[§28 The Differential in Coordinates#^prop-28-1|§28.1]]: the partials are *defined* through the chart, and $F^j \circ \varphi^{-1} = \tilde F^j$, so $\partial F^j/\partial x^i(p) = \partial \tilde F^j/\partial r^i(\varphi(p))$, the $(j,i)$ entry of $\tilde F'(\varphi(p))$. “It's all the same.”

^pf-28-2

*Uses:* [[§26 Derivations and the Abstract Tangent Space#^prop-26-5|§26.5]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|§27.5]], [[§26 Derivations and the Abstract Tangent Space#^def-26-5|Def. §26.5]], [[§28 The Differential in Coordinates#^prop-28-1|§28.1]], [[§9 Matrices#^ladr-3-31|LADR 3.31]]

> [!remark]- Connections
> - The matrix of a linear map with respect to bases: [[§9 Matrices#^ladr-3-31|LADR 3.31]]; the Jacobian matrix of calculus: [[§6 Differentiability#^def-6-2|452 Def. §6.2]].
> - The same statement between vector spaces: [[§21 The Differential of a Map Between Vector Spaces#^def-21-4|Def. §21.4]].

> [!remark] Remark
> **Which index is the row.** Uribe's mnemonic, “from the mid-nineteenth century”: *gradients go across*. Row $j$ of the matrix is the gradient of the single function $F^j$, so moving along a row changes $i$; the column $i$ is the image of the $i$-th basis vector, as it must be for the matrix of a linear map.

^rem-28-2

**Transcription notes.** Page 26 of the handwritten notes calls $\mathcal{B}_N$ a basis “of $T_{F(p)}M$”. Page 27 (Lecture 10) repeats the lemma with the basis written $\{\partial/\partial y^j|_p,\ 1 \le j \le m\}$ “of $T_{F(p)}M$” — three slips at once: the base point is $F(p)$, the index runs to $n = \dim N$, and the space is $T_{F(p)}N$. In the same proof the universal formula is written with $\partial/\partial y^j|_p$ for $\partial/\partial y^j|_{F(p)}$. A student asked whether the index on $F^j$ belongs upstairs or downstairs; upstairs, as for coordinates, with $j$ the row index. Uribe also announced that the partials will from now on be written in calculus notation, $\partial F^j/\partial x^i(p)$ rather than $\partial/\partial x^i|_p[F^j]$.

> [!theorem] Corollary §28.3: The Chain Rule in Coordinates
> Let $F : M \to N$ and $G : N \to O$ be smooth, with charts $(U,\varphi)$ at $p$, $(V,\psi)$ at $F(p)$ and $(W,\chi)$ at $G(F(p))$ such that $F(U) \subseteq V$ and $G(V) \subseteq W$, and write $\tilde F = \psi \circ F \circ \varphi^{-1}$, $\tilde G = \chi \circ G \circ \psi^{-1}$ and $\widetilde{G \circ F} = \chi \circ (G \circ F) \circ \varphi^{-1}$ for the coordinate representations. Then $\widetilde{G \circ F} = \tilde G \circ \tilde F$ on $\varphi(U)$, and
>
> $$
> \big(\widetilde{G \circ F}\big)'\big(\varphi(p)\big) = \tilde G'\big(\psi(F(p))\big)\; \tilde F'\big(\varphi(p)\big):
> $$
>
> the matrix of $(G \circ F)_{*p}$ is the product of the matrices of $G_{*F(p)}$ and $F_{*p}$.
>
> *Lee: Ch. 3, Computations in Coordinates*

^cor-28-3

> [!proof]+ Proof
> $\chi \circ G \circ F \circ \varphi^{-1} = (\chi \circ G \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1})$ on $\varphi(U)$. By the Chain Rule (Theorem [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]]) the matrix of $(G\circ F)_{*p}$ is the product of the matrices of $G_{*F(p)}$ and $F_{*p}$, and by Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] the three matrices are the three Jacobians. The formula is also the Euclidean chain rule applied to $\tilde G \circ \tilde F$; the two routes agree, as they must.

^pf-28-3

*Uses:* [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§9 Matrices#^ladr-3-43|LADR 3.43]], [[Multivariable Chain Rule|452 §10.2]]

![[m591-12-11.svg]]
*Upstairs the composite of maps between manifolds; downstairs the composite of their coordinate representations. Each square commutes, so the outer rectangle does, and differentiating the bottom row at $\varphi(p)$ multiplies the Jacobians.*

> [!remark]- Connections
> - The Euclidean chain rule for Jacobians: [[§10 Composition of Functions and the Chain Rule#^rem-10-4|452 §10 (Chain Rule for Jacobians)]]; matrix of a product: [[§9 Matrices#^ladr-3-43|LADR 3.43]].

> [!theorem] Corollary §28.4: Change of Coordinates
> If $(U, \varphi)$ and $(\tilde U, \tilde\varphi)$ are two smooth charts at $p$, with coordinates $x^i$ and $\tilde x^j$, then
>
> $$
> \frac{\partial}{\partial \tilde x^j}\Big|_p = \sum_{i=1}^n \frac{\partial x^i}{\partial \tilde x^j}(p)\, \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> and the change-of-basis matrix is the Jacobian of the transition function $\varphi \circ \tilde\varphi^{-1}$ at $\tilde\varphi(p)$.
>
> *Lee: Ch. 3, Computations in Coordinates*

^cor-28-4

> [!proof]+ Proof
> Apply Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] to $F = \mathrm{id}_M$, with the chart $\tilde\varphi$ on the source and $\varphi$ on the target. Then $F^i = x^i$, the coordinate representation is the transition $\varphi \circ \tilde\varphi^{-1}$, and $(\mathrm{id}_M)_{*p} = \mathrm{id}$ by Proposition [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]].

^pf-28-4

*Uses:* [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§26 Derivations and the Abstract Tangent Space#^thm-26-6|§26.6]]

> [!remark]- Connections
> - The change-of-basis formula of linear algebra: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].
> - Transition functions: [[§2 Topological Manifolds#^def-2-4|Def. §2.4]].

> [!example] Example §28.1: Polar Coordinates
> On $M = \mathbb{R}^2 \setminus \{(x, 0) \mid x \le 0\}$ take the standard chart $(x, y)$ and the polar chart $(r, \theta)$, $0 < r$, $-\pi < \theta < \pi$, with $x = r\cos\theta$ and $y = r\sin\theta$. By Corollary [[§28 The Differential in Coordinates#^cor-28-4|§28.4]],
>
> $$
> \frac{\partial}{\partial r} = \cos\theta\, \frac{\partial}{\partial x} + \sin\theta\, \frac{\partial}{\partial y}, \qquad
> \frac{\partial}{\partial \theta} = -r\sin\theta\, \frac{\partial}{\partial x} + r\cos\theta\, \frac{\partial}{\partial y},
> $$
>
> the coefficients being $\partial x/\partial r$, $\partial y/\partial r$ and $\partial x/\partial\theta$, $\partial y/\partial\theta$.
>
> *Lee: cf. Example C.37*

^ex-28-1

![[m591-12-12.svg]]
*At a point $p$ at radius $r$, the four coordinate derivations — elements of the abstract tangent space $T_pM$ — drawn as the vectors of $T^{\mathrm{geo}}_pM = \mathbb{R}^2$ they correspond to under the identification $\partial_x \leftrightarrow e_1$, $\partial_y \leftrightarrow e_2$ of Proposition [[§28 The Differential in Coordinates#^prop-28-5|§28.5]] below (all at the common scale $0.7$). The polar ones are the radial and tangential directions, but $\partial_\theta$ is not a unit vector: it has length $r$, because it records the velocity of the curve $\theta \mapsto (r\cos\theta, r\sin\theta)$ along which the other coordinate is held fixed. A coordinate vector depends on the whole chart, not only on its own coordinate function — the same abstract tangent space, and a different matrix for every map out of it.*

> [!remark]- Connections
> - Polar coordinates in multivariable calculus (Jacobians, change of variables): [[Polar and spherical coordinates]].

> [!theorem] Proposition §28.5: Agreement with the Vector-Space Differential
> Let $W \subseteq \mathbb{R}^m$ be open, $F : W \to \mathbb{R}^n$ smooth, and $a \in W$, and identify the abstract tangent spaces $T_aW \cong \mathbb{R}^m$ and $T_{F(a)}\mathbb{R}^n \cong \mathbb{R}^n$ by $\partial/\partial r^i \mapsto e_i$ — that is, with the geometric tangent spaces $T^{\mathrm{geo}}_aW = \mathbb{R}^m$ and $T^{\mathrm{geo}}_{F(a)}\mathbb{R}^n = \mathbb{R}^n$. Then $F_{*a}$ corresponds to the Jacobian $F'(a)$, i.e. to the differential $dF_a$ of [[§21 The Differential of a Map Between Vector Spaces|§21, The Differential of a Map Between Vector Spaces]]. Under the same identification, $v = \sum_i v^i e_i$ corresponds to the derivation
>
> $$
> [g] \longmapsto \sum_i v^i\, \frac{\partial g}{\partial r^i}(a) = \frac{d}{dt}\Big|_{t=0} g(a + tv),
> $$
>
> the directional derivative $D_v$ of [[§23 The Geometric Tangent Space#From Tangent Vectors to Derivations|§23, From Tangent Vectors to Derivations]].
>
> *Lee: Proposition 3.13 and Corollary 3.3*

^prop-28-5

> [!proof]+ Proof
> Apply Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] with the identity charts: then $\tilde F = F$, and the matrix of $F_{*a}$ is $F'(a)$. The second statement is the chain rule applied to $t \mapsto g(a + tv)$.

^pf-28-5

*Uses:* [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[Multivariable Chain Rule|452 §10.2]]

> [!remark]- Connections
> - The differential between vector spaces: [[§21 The Differential of a Map Between Vector Spaces#^def-21-4|Def. §21.4]]; in calculus, [[§8 The Differential#^def-8-1|452 Def. §8.1]] and [[Directional Derivative Formula|452 §7.1 (Directional Derivative Formula)]].

> [!theorem] Corollary §28.6: The Tangent Space to a Vector Space
> Let $V$ be a finite-dimensional vector space with its standard smooth structure, and $a \in V$. The map
>
> $$
> V \to T_aV, \qquad v \mapsto D_v|_a, \qquad D_v|_a[f] = \frac{d}{dt}\Big|_{t=0} f(a + tv),
> $$
>
> is a linear isomorphism, defined without any choice of basis. For every linear map $L : V \to W$, $L_{*a}(D_v|_a) = D_{Lv}|_{La}$.
>
> *Lee: Proposition 3.13*

^cor-28-6

> [!proof]+ Proof
> For linear $L$, $L_{*a}(D_v|_a)[g] = D_v|_a[g \circ L] = \frac{d}{dt}\big|_0\, g(La + t\,Lv) = D_{Lv}|_{La}[g]$. Now take $L = L_0 : V \to \mathbb{R}^m$ a linear coordinate system. It is a chart, hence a diffeomorphism (Proposition [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]]), so $(L_0)_{*a}$ is an isomorphism, and it carries $D_v|_a$ to $D_{L_0 v}|_{L_0 a}$, which is $\sum_i (L_0 v)^i\,\partial/\partial r^i$ by Proposition [[§28 The Differential in Coordinates#^prop-28-5|§28.5]]. The composite $v \mapsto L_0 v \mapsto \sum_i (L_0v)^i\,\partial/\partial r^i$ is an isomorphism, hence so is $v \mapsto D_v|_a$. The defining formula mentions no basis.

^pf-28-6

*Uses:* [[§26 Derivations and the Abstract Tangent Space#^def-26-5|Def. §26.5]], [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]], [[§28 The Differential in Coordinates#^prop-28-5|§28.5]], [[§21 The Differential of a Map Between Vector Spaces#^def-21-1|Def. §21.1]], [[§21 The Differential of a Map Between Vector Spaces#^def-21-3|Def. §21.3]]

> [!remark] Remark
> This is what licenses the shared notation $dF_p$: on open subsets of Euclidean spaces the abstract differential *is* the Jacobian, and between vector spaces it is the map of Theorem [[§21 The Differential of a Map Between Vector Spaces#^thm-21-3|§21.3]]. It also closes a loop opened in [[§23 The Geometric Tangent Space#From Tangent Vectors to Derivations|§23, From Tangent Vectors to Derivations]], where a tangent vector $v$ was traded for the operator $D_v$; in $\mathbb{R}^n$ that trade is exactly the identification $e_i \leftrightarrow \partial/\partial r^i$.

^rem-28-3

> [!definition] Definition §28.1: Rank and Regular Values of a Smooth Map
> Let $F : M \to N$ be a smooth map. The **rank** of $F$ at $p$ is the rank of the linear map $F_{\ast p} : T_pM \to T_{F(p)}N$ of abstract tangent spaces; by Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]] it is the rank of the Jacobian of any coordinate representation. A point $p$ is a **regular point** of $F$ if $F_{\ast p}$ is surjective, and $c \in N$ is a **regular value** if every $p \in F^{-1}(c)$ is a regular point.
>
> *Lee: Ch. 4 and Ch. 5, p. 105*

^def-28-1

> [!remark]- Connections
> - The Euclidean definition it extends: [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]]; restated with critical points in [[§32 Submersions#^def-32-2|Def. §32.2]].
> - A regular point is a point where $F$ is a submersion: [[§32 Submersions#^def-32-1|Def. §32.1]].

> [!remark] Remark: The Map Is Intrinsic — the Matrix Is Not
> Uribe's closing point. The linear map $F_{\ast p}$ is defined with no choices, but its matrix depends on both charts: by Corollary [[§28 The Differential in Coordinates#^cor-28-4|§28.4]], changing them multiplies the matrix on each side by the Jacobian of a transition function. So only properties of $F_{\ast p}$ that survive such changes — its rank, kernel and image, injectivity and surjectivity — are properties of $F$, which is why the definition above is phrased through $F_{\ast p}$ rather than through a matrix. By Proposition [[§28 The Differential in Coordinates#^prop-28-5|§28.5]] it agrees with Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]] in the Euclidean case. A regular point is exactly a point at which $F$ is a *submersion*, in the sense of Definition [[§32 Submersions#^def-32-1|§32.1]]; maps with bijective, surjective and injective differentials are the subject of [[§31 Local Diffeomorphisms|§31]].

^rem-28-4

> [!theorem] Proposition §28.7: Regular Values Inside One Chart
> Let $F : M \to N$ be a smooth map between smooth manifolds of dimensions $m$ and $n$, and $c \in N$. Suppose there are smooth charts $(U, \varphi)$ of $M$ and $(V, \psi)$ of $N$ with
>
> $$
> F^{-1}(c) \subseteq U, \qquad c \in V, \qquad F(U) \subseteq V .
> $$
>
> Let $\tilde F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}^n$ be the coordinate representation of $F$, a smooth map on the open set $\varphi(U) \subseteq \mathbb{R}^m$, and put $\tilde c = \psi(c) \in \mathbb{R}^n$. Then:
> 1. $\varphi$ restricts to a homeomorphism from the level set $F^{-1}(c) \subseteq M$ onto the Euclidean level set $\tilde F^{-1}(\tilde c) \subseteq \varphi(U)$;
> 2. $c$ is a regular value of $F$ in the sense of Definition [[§28 The Differential in Coordinates#^def-28-1|§28.1]] if and only if $\tilde c$ is a regular value of $\tilde F$ in the sense of Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]];
> 3. in that case $F^{-1}(c)$ is a topological manifold of dimension $m - n$.

^prop-28-7

> [!proof]+ Proof
> (1) Let $x \in \varphi(U)$ and $q = \varphi^{-1}(x) \in U$. Since $F(U) \subseteq V$ and $\psi$ is injective on $V$,
>
> $$
> \tilde F(x) = \tilde c \iff \psi\big(F(q)\big) = \psi(c) \iff F(q) = c .
> $$
>
> So $\varphi\big(F^{-1}(c) \cap U\big) = \tilde F^{-1}(\tilde c)$, and $F^{-1}(c) \cap U = F^{-1}(c)$ by hypothesis. A homeomorphism restricts to a homeomorphism from any subset onto its image, both with the subspace topology.
>
> (2) Let $p \in F^{-1}(c)$. By Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], the matrix of $F_{*p}$ in the coordinate bases of the two charts is the Jacobian $\tilde F'(\varphi(p))$, and a linear map is surjective exactly when its matrix has rank equal to the dimension of the target (Proposition [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]]). So $p$ is a regular point of $F$ if and only if $\varphi(p)$ is a regular point of $\tilde F$. By (1), $p$ runs over $F^{-1}(c)$ exactly as $\varphi(p)$ runs over $\tilde F^{-1}(\tilde c)$.
>
> (3) By (2) and Corollary [[§7 The Regular Value Theorem#^cor-7-4|§7.4]], applied on the open set $\varphi(U) \subseteq \mathbb{R}^m$ with $k = n$, the Euclidean level set $\tilde F^{-1}(\tilde c)$ is a topological manifold of dimension $m - n$. By (1), $F^{-1}(c)$ is homeomorphic to it, and being a topological manifold is preserved by homeomorphisms.

^pf-28-7

*Uses:* [[§28 The Differential in Coordinates#^def-28-1|Def. §28.1]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§20 Linear Algebra Toolkit#^prop-20-1|§20.1]], [[§7 The Regular Value Theorem#^cor-7-4|§7.4]], [[§9 Continuous Functions#^prop-9-3|590 §9.3]]

![[m591-12-13.svg]]
*The proposition in one square. The level set upstairs is carried by the chart onto a level set downstairs, in Euclidean space, and the question “is $c$ regular?” is carried with it: surjectivity of $F_{\ast p}$ upstairs is the rank of $\tilde F'$ downstairs.*

> [!remark] Remark: The Strategy
> To show that $c$ is a regular value of a map between manifolds, and to see its level set:
> 1. *Locate the level set.* Show that $F^{-1}(c)$ lies inside a single chart domain $U$, and that $F(U)$ lies in a chart domain $V$ around $c$.
> 2. *Go downstairs.* Write the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$, an ordinary map between open subsets of Euclidean spaces.
> 3. *Compute as in [[§7 The Regular Value Theorem|§7]].* Check that the Jacobian of $\tilde F$ has full rank $n$ at every point of the Euclidean level set $\tilde F^{-1}(\tilde c)$.
> 4. *Come back up.* By Proposition [[§28 The Differential in Coordinates#^prop-28-7|§28.7]], $c$ is a regular value of $F$, and $F^{-1}(c)$ is homeomorphic, through the chart, to a Euclidean regular level set: a manifold of dimension $\dim M - \dim N$.
>
> Assignment 3, Problem 4 is exactly this. For the moment map $F : \mathbb{CP}^n \to \mathbb{R}^n$ and $c$ in the interior of the simplex, every point of $F^{-1}(c)$ has all homogeneous coordinates nonzero, so $F^{-1}(c) \subseteq U_0$ (step 1). The target chart is the identity of $\mathbb{R}^n$, and $\varphi_0(U_0) = \mathbb{C}^n \cong \mathbb{R}^{2n}$, so $\tilde F$ is an explicit rational map $\mathbb{R}^{2n} \to \mathbb{R}^n$ (step 2). Its Jacobian has rank $n$ on the level set (step 3). So the fibre is an $n$-dimensional manifold (step 4) — in this case a regular level set of $\mathbb{R}^{2n}$ itself, exactly the situation of [[§7 The Regular Value Theorem|§7]]. When a level set does not fit in one chart, the same argument applies around each of its points separately, as the next corollary shows.

^rem-28-5

Complex projective space through the course: the open quotient $S^{2n+1}/S^1$, Hausdorff, second countable and compact, in [[§9 Complex Projective Space|Complex Projective Space]]; the circle group $\mathrm{U}(1)$ acting there in [[§10 Topological Groups and Classical Matrix Groups#^ex-10-3|U(1) is the circle]]; an orbit space in [[§12 Group Actions and Orbit Spaces#^ex-12-3|projective space as an orbit space]]; a smooth and complex manifold through its standard atlas in [[§17 Projective Spaces as Smooth Manifolds|Projective Spaces as Smooth Manifolds]]; a homogeneous space of $\mathrm{U}(n+1)$ in [[§23 The Geometric Tangent Space#^rem-23-9|Dimension Checks through Homogeneous Spaces]]; the domain of the moment map in [[§28 The Differential in Coordinates#^rem-28-5|Remark: The Strategy]]; and the base of the Hopf fibration in [[§37 Projective Spaces and the Hopf Fibration|Projective Spaces and the Hopf Fibration]].

> [!theorem] Corollary §28.8: Regular Level Sets Are Topological Manifolds
> Let $F : M \to N$ be a smooth map between smooth manifolds of dimensions $m$ and $n$, and $c \in N$ a regular value of $F$. Then $F^{-1}(c)$, with the subspace topology, is a topological manifold of dimension $m - n$ (or empty).

^cor-28-8

> [!proof]+ Proof
> Hausdorffness and second countability are inherited from $M$ (Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]). For local Euclideanness, let $p \in F^{-1}(c)$. Choose smooth charts $(V, \psi)$ around $c$ and $(U_0, \varphi_0)$ around $p$, and put $U = U_0 \cap F^{-1}(V)$, an open neighbourhood of $p$ because $F$ is continuous; restricting $\varphi_0$ gives a smooth chart $(U, \varphi)$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]]). Apply Proposition [[§28 The Differential in Coordinates#^prop-28-7|§28.7]] to the restriction $F|_U : U \to N$, a smooth map on the open submanifold $U$: its level set $F^{-1}(c) \cap U$ lies in $U$, it maps $U$ into $V$, and $c$ is still a regular value, since $T_qU = T_qM$ and $(F|_U)_{*q} = F_{*q}$ for $q \in U$ (Lemma [[§26 Derivations and the Abstract Tangent Space#^lem-26-8|§26.8]]). So $F^{-1}(c) \cap U$, an open neighbourhood of $p$ in $F^{-1}(c)$, is a topological manifold of dimension $m - n$; in particular $p$ has a neighbourhood in $F^{-1}(c)$ homeomorphic to an open subset of $\mathbb{R}^{m-n}$.

^pf-28-8

*Uses:* [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§28 The Differential in Coordinates#^prop-28-7|§28.7]], [[§26 Derivations and the Abstract Tangent Space#^lem-26-8|§26.8]], [[§28 The Differential in Coordinates#^def-28-1|Def. §28.1]]

> [!remark]- Connections
> - The smooth half, $F^{-1}(c)$ a submanifold with tangent space $\ker F_{*p}$: [[§33 Submanifolds#^thm-33-6|§33.6]]; the Euclidean original: [[§7 The Regular Value Theorem#^thm-7-3|§7.3]].

This is the topological half of the regular value theorem for manifolds, and it is [[§7 The Regular Value Theorem|§7]] applied chart by chart. The smooth half — that $F^{-1}(c)$ is a smooth *submanifold* of $M$, with tangent space $\ker F_{\ast p}$ — came in Lecture 12, as Theorem [[§33 Submanifolds#^thm-33-6|§33.6]], proved with the local normal form for submersions (Theorem [[§32 Submersions#^thm-32-4|§32.4]]): near each point of the level set, $F$ is a projection, so the level set is a coordinate slice. It is Lee's Corollary 5.14 and Proposition 5.38. The corollary above is now a consequence of it, a submanifold being in particular a topological manifold, but its proof — [[§7 The Regular Value Theorem|§7]] applied chart by chart — is more elementary.

> [!theorem] Proposition §28.9: Maps with Zero Differential Are Constant
> Let $F : M \to N$ be smooth ([[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]]), with $M$ connected ([[§13 Connected Spaces#^def-13-1|590 Def. §13.1]]). If $F_{\ast p} = 0$ ([[§26 Derivations and the Abstract Tangent Space#^def-26-5|Def. §26.5]]) for every $p \in M$, then $F$ is constant.

^prop-28-9

> [!proof]+ Proof
> *(Assignment 4, Problem 1: the submitted solution, condensed.)* *$F$ is locally constant.* Fix $p_0 \in M$. Take a chart $(V, \psi)$ at $F(p_0)$ and a chart at $p_0$ whose domain $U_0$ satisfies $F(U_0) \subseteq V$ and whose image is an open ball $B$ — shrink by continuity of $F$, then to a ball. The coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1} : B \to \mathbb{R}^n$ has Jacobian $\tilde F'(\varphi(p))$, the matrix of $F_{\ast p}$ (Theorem [[§28 The Differential in Coordinates#^thm-28-2|§28.2]]), so $\tilde F' \equiv 0$ on $B$. For $p \in U_0$, the segment from $\varphi(p_0)$ to $\varphi(p)$ stays in the convex $B$, and the [[§29 The Mean Value Theorem#^thm-29-3|mean value theorem]] applied to each component of $\tilde F$ along it gives $\tilde F(\varphi(p)) = \tilde F(\varphi(p_0))$; since $\psi$ is injective, $F(p) = F(p_0)$.
>
> *$F$ is constant.* Let $c = F(p_0)$. The set $F^{-1}(c)$ is closed, since $F$ is continuous, and open, since $F$ is locally constant; it is nonempty. As $M$ is connected, $F^{-1}(c) = M$.

^pf-28-9

*Uses:* [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§28 The Differential in Coordinates#^thm-28-2|§28.2]], [[§29 The Mean Value Theorem#^thm-29-3|451 §29.3]], [[§9 Continuous Functions#^thm-9-1|590 §9.1]], [[§13 Connected Spaces#^lem-13-1|590 §13.1]]

> [!remark]- Connections
> - Connectedness via clopen sets: [[§13 Connected Spaces#^lem-13-1|590 Lem. §13.1]]; the one-variable original: [[§29 The Mean Value Theorem#^cor-29-4|451 §29.4]] (vanishing derivative means constant).

The hypothesis that $M$ is connected cannot be dropped: on a disconnected $M$, a map that takes different constant values on different components has zero differential everywhere. Locally, the proposition is the familiar fact from calculus that a function with zero derivative on an interval is constant.
