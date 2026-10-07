---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 45
tags: [differentiable-manifolds, math591]
---
← [[§44 The Tangent Bundle]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§46 One-Forms]] →

*Stage: bundles — The cotangent spaces assembled into $T^{\ast}M$, with charts from the dual bases; covector components transform by the inverse transpose.*

*Lecture 13 defined the cotangent bundle — “completely analogous” to the tangent bundle, with the dual bases in place of the coordinate bases; Lecture 15 returned to it for the homework.*

> [!definition] Definition §45.1: The Cotangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **cotangent bundle** is the set
>
> $$
> T^*M = \bigcup_{p \in M} \{p\} \times T_p^*M = \{\, (p, \xi) : p \in M,\ \xi \in T_p^*M \,\},
> $$
>
> all the cotangent spaces ([[§32 The Cotangent Space#^def-32-1|Definition §32.1]]) put together.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-45-1

> [!definition] Definition §45.2: The Projection of $T^*M$
> The **projection** of the cotangent bundle is
>
> $$
> \pi : T^*M \longrightarrow M, \qquad \pi(p, \xi) = p .
> $$
>
> Its fibre over $p$, $\pi^{-1}(p) = \{p\} \times T_p^{\ast}M$, is identified with $T_p^{\ast}M$.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-45-2

> [!definition] Definition §45.3: The Zero Section of $T^*M$
> The **zero section** of the cotangent bundle is
>
> $$
> \zeta : M \longrightarrow T^*M, \qquad \zeta(p) = (p, 0) .
> $$
>
> It is one-to-one, as for $TM$ ([[§44 The Tangent Bundle#^def-44-3|Definition §44.3]]): every cotangent space has a distinguished element, its zero.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-45-3

> [!remark]- Connections
> - The fibre $T_p^*M$ is a dual space, [[§12 Duality#^ladr-3-110|LADR 3.110]], and the chart uses the dual basis, [[§12 Duality#^ladr-3-112|LADR 3.112]]. Counterpart in 452: differential forms on $\mathbb{R}^n$, [[§36 Introduction to Differential Forms#^def-36-2|452 Def. §36.2]].

The definitions and results of this section run parallel to those for the tangent bundle in [[§44 The Tangent Bundle|§44]], item for item, with the dual bases $dx^i|_p$ in place of the coordinate bases $\partial/\partial x^i|_p$. Lecture 13 gave the charts and the transition maps; the rest is filled in, following [[§44 The Tangent Bundle|§44]].

## Trivializations and Charts

> [!definition] Definition §45.4: Local Trivializations of $T^*M$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $T^{\ast}U = \pi^{-1}(U) = \{(p, \xi) \in T^{\ast}M : p \in U\}$, the covectors at points of $U$. The **local trivialization** of $T^{\ast}M$ over $U$ is
>
> $$
> \Psi : T^*U \longrightarrow U \times \mathbb{R}^m, \qquad \Psi(p, \xi) = (p, \xi_1, \ldots, \xi_m), \qquad \text{where } \xi = \sum_{i=1}^m \xi_i\, dx^i\big|_p ,
> $$
>
> the components of $\xi$ in the dual basis. Because the bases $dx^i|_p$ and $\partial/\partial x^i|_p$ are dual to each other, the components are computed by evaluation, $\xi_i = \xi\big(\partial/\partial x^i|_p\big)$ ([[§32 The Cotangent Space#^cor-32-3|Corollary §32.3]]). $\Psi$ is a bijection, and $\mathrm{pr}_1 \circ \Psi = \pi$.
>
> *Lee: Proposition 11.9*

^def-45-4

> [!definition] Definition §45.5: Charts of $T^*M$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $\Psi$ the local trivialization over $U$ ([[§45 The Cotangent Bundle#^def-45-4|Definition §45.4]]). The **chart** of $T^{\ast}M$ over $U$ — the **standard coordinates** on $T^{\ast}U$ — is
>
> $$
> \hat\varphi = (\varphi \times \mathrm{id}) \circ \Psi : T^*U \longrightarrow \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m},
> $$
>
> which acts in two steps:
>
> $$
> (p, \xi) \;\overset{\Psi}{\longmapsto}\; (p,\, \xi_1, \ldots, \xi_m) \;\overset{\varphi \times \mathrm{id}}{\longmapsto}\; \big(x^1(p), \ldots, x^m(p),\, \xi_1, \ldots, \xi_m\big),
> $$
>
> where $\xi_1, \ldots, \xi_m$ are the components of $\xi$ in the dual basis at $p$,
>
> $$
> \xi = \sum_{i=1}^m \xi_i\, dx^i\big|_p, \qquad \xi_i = \xi\Big(\frac{\partial}{\partial x^i}\Big|_p\Big)
> $$
>
> ([[§32 The Cotangent Space#^cor-32-3|Corollary §32.3]]). So the first $m$ coordinates of $\hat\varphi(p, \xi)$ locate the point $p$, and the last $m$ list the components of the covector $\xi$. $\hat\varphi$ is a bijection, with inverse
>
> $$
> (r, b_1, \ldots, b_m) \longmapsto \Big(\varphi^{-1}(r),\ \sum_{i=1}^m b_i\, dx^i\big|_{\varphi^{-1}(r)}\Big), \qquad r \in \varphi(U),\ (b_1, \ldots, b_m) \in \mathbb{R}^m .
> $$
>
> *Lee: Proposition 11.9*

^def-45-5

> [!theorem] Proposition §45.1: The Topology of $T^*M$
> There is a unique topology on $T^{\ast}M$ for which every $T^{\ast}U$ is open and every chart $\hat\varphi : T^{\ast}U \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $T^{\ast}M$ is a topological manifold of dimension $2m$.
>
> *Lee: Lemma 1.35 and Proposition 11.9*

^prop-45-1

> [!proof]+ Proof
> *(Not from lecture — “completely analogous”; filled in.)* The proof of [[§44 The Tangent Bundle#^prop-44-1|Proposition §44.1]] uses only two facts about the charts $\tilde\varphi$: each is a bijection of $TU$ onto the open set $\varphi(U) \times \mathbb{R}^m$, and each transition map $\tilde\psi \circ \tilde\varphi^{-1}$ is a homeomorphism between the open sets $\varphi(U \cap V) \times \mathbb{R}^m$ and $\psi(U \cap V) \times \mathbb{R}^m$. Both hold for the charts $\hat\varphi$: the first by [[§45 The Cotangent Bundle#^def-45-5|Definition §45.5]], and the second by the computation in the proof of [[§45 The Cotangent Bundle#^prop-45-2|Proposition §45.2]] below, which uses only the definitions of the charts, not any topology on $T^{\ast}M$. With $\hat\varphi$, $\hat\psi$ and $T^{\ast}U$ in place of $\tilde\varphi$, $\tilde\psi$ and $TU$, the proof then goes through word for word:
> - declare $W \subseteq T^{\ast}M$ open if $\hat\varphi(W \cap T^{\ast}U)$ is open in $\mathbb{R}^{2m}$ for every chart $(U, \varphi)$; this is a topology, since each $\hat\varphi$ is a bijection;
> - each $T^{\ast}U$ is open, because $\hat\psi(T^{\ast}U \cap T^{\ast}V) = \psi(U \cap V) \times \mathbb{R}^m$ is open, and each $\hat\varphi$ is a homeomorphism onto its open image, because the transition maps are homeomorphisms;
> - any topology with these two properties has the same open sets, since $W = \bigcup_U (W \cap T^{\ast}U)$;
> - $T^{\ast}M$ is locally Euclidean of dimension $2m$, through the charts;
> - it is Hausdorff: two covectors at the same point lie in one $T^{\ast}U$, homeomorphic to a subset of $\mathbb{R}^{2m}$, and covectors at distinct points $p \neq q$ lie in the disjoint open sets $T^{\ast}U$, $T^{\ast}V$ for charts with disjoint domains $U \ni p$, $V \ni q$;
> - it is second countable: countably many chart domains $U_B$ cover $M$, so the countably many open sets $T^{\ast}U_B$, each with a countable basis, cover $T^{\ast}M$.

^pf-45-1

*Uses:* [[§44 The Tangent Bundle#^prop-44-1|§44.1]], [[§45 The Cotangent Bundle#^def-45-5|Def. §45.5]], [[§45 The Cotangent Bundle#^prop-45-2|§45.2]]

> [!theorem] Proposition §45.2: The Smooth Atlas of $T^*M$
> The charts $(T^{\ast}U, \hat\varphi)$, as $(U, \varphi)$ ranges over the smooth charts of $M$, form a smooth atlas on $T^{\ast}M$. For charts $\varphi = (x^i)$ and $\psi = (y^j)$, if $\xi = \sum_i \xi_i\, dx^i|_p = \sum_j \eta_j\, dy^j|_p$, then
>
> $$
> dx^i|_p = \sum_j \frac{\partial x^i}{\partial y^j}(p)\, dy^j|_p, \qquad \eta_j = \sum_i \frac{\partial x^i}{\partial y^j}(p)\, \xi_i .
> $$
>
> So the covector components transform by the transpose of the inverse of the matrix that transforms tangent components: with $\tau = \psi \circ \varphi^{-1}$, the transition map is
>
> $$
> \hat\psi \circ \hat\varphi^{-1}(r, \xi) = \Big( \tau(r),\ \big(\tau'(r)^{-1}\big)^{\mathsf T} \xi \Big) .
> $$
>
> *Lee: Proposition 11.9*

^prop-45-2

> [!proof]+ Proof
> *(Lecture 13: “completely analogous”, with the change “we use the dual basis”, and the formula for $dx^i$ given; the rest is filled in.)* The formula for $dx^i|_p$ is [[§32 The Cotangent Space#^lem-32-2|Lemma §32.2]] applied to the function $x^i$ in the chart $\psi$. Substituting it into $\sum_i \xi_i\, dx^i|_p$ and comparing coefficients of $dy^j|_p$ gives $\eta_j$. The matrix $\big[\partial x^i/\partial y^j\big]$ is the inverse of $\big[\partial y^i/\partial x^j\big]$ (chain rule), so the tangent components transform by $A = \big[\partial y^i/\partial x^j\big]$ and the covector components by $(A^{-1})^{\mathsf T}$. Its entries are smooth functions of the base point, so the transition maps are smooth, as in [[§44 The Tangent Bundle#^prop-44-2|Proposition §44.2]]; the fibration and linearity statements follow as in [[§44 The Tangent Bundle#^cor-44-3|Corollary §44.3]].
> Explicitly, with $p = \varphi^{-1}(r)$, the matrix $\big[\partial y^i/\partial x^j(p)\big]$ is $\tau'(r)$ ([[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1]]), so $\big[\partial x^i/\partial y^j(p)\big] = \tau'(r)^{-1}$ and $\eta = \big(\tau'(r)^{-1}\big)^{\mathsf T}\xi$, which is the displayed transition map. Its entries are smooth in $r$: those of $\tau'(r)$ are, and the inverse of an invertible matrix is given by Cramer's rule, a quotient of polynomials in the entries by the nonzero determinant. The inverse transition map is the same formula with the two charts exchanged.

^pf-45-2

*Uses:* [[§45 The Cotangent Bundle#^def-45-5|Def. §45.5]], [[§32 The Cotangent Space#^def-32-1|Def. §32.1]], [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§44 The Tangent Bundle#^prop-44-2|§44.2]], [[§44 The Tangent Bundle#^cor-44-3|§44.3]], [[Multivariable Chain Rule|452 §12.2]], [[§12 Duality#^ladr-3-132|LADR 3.132]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]

> [!remark]- Connections
> - The matrix of a dual map in dual bases is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].
> - The rule for $dx^i$ is the substitution step of the pullback in 452, [[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]], applied to the transition map.

> [!theorem] Corollary §45.3: The Cotangent Bundle Is a Fibration
> With the smooth structure of [[§45 The Cotangent Bundle#^prop-45-2|Proposition §45.2]]:
> 1. $T^{\ast}M$ is a smooth manifold of dimension $2m$, and $\pi : T^{\ast}M \to M$ is smooth;
> 2. the $\Psi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Psi$ restricts on the fibre $T_p^{\ast}M$ to a linear isomorphism $T_p^{\ast}M \to \{p\} \times \mathbb{R}^m$; so $T^{\ast}M$ is a vector bundle;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $T^{\ast}M$ of codimension $m$.
>
> *Lee: Proposition 11.9*

^cor-45-3

> [!proof]+ Proof
> *(Not from lecture; filled in, as [[§44 The Tangent Bundle#^cor-44-3|Corollary §44.3]].)* (1) By [[§45 The Cotangent Bundle#^prop-45-1|Propositions §45.1]] and [[§45 The Cotangent Bundle#^prop-45-2|§45.2]]. In the charts $\hat\varphi$ and $\varphi$, $\pi$ is $(r, \xi) \mapsto r$, which is smooth. (2) $\Psi = (\varphi^{-1} \times \mathrm{id}) \circ \hat\varphi$ is a composite of diffeomorphisms ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9]]), and $\mathrm{pr}_1 \circ \Psi = \pi$; the $T^{\ast}U$ cover $T^{\ast}M$ and the $U$ cover $M$. On $T_p^{\ast}M$, $\Psi$ is $\xi \mapsto (p, \xi_1, \ldots, \xi_m)$, taking components in a basis, which is a linear isomorphism. (3) In the chart $\hat\varphi$, $\zeta(M) \cap T^{\ast}U = \{\xi_1 = \cdots = \xi_m = 0\}$, so the charts $\hat\varphi$ are adapted to $\zeta(M)$ ([[§35 Submanifolds#^def-35-2|Definition §35.2]]).

^pf-45-3

*Uses:* [[§45 The Cotangent Bundle#^prop-45-1|§45.1]], [[§45 The Cotangent Bundle#^prop-45-2|§45.2]], [[§45 The Cotangent Bundle#^def-45-4|Def. §45.4]], [[§45 The Cotangent Bundle#^def-45-5|Def. §45.5]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§35 Submanifolds#^def-35-1|Def. §35.1]], [[§35 Submanifolds#^def-35-2|Def. §35.2]], [[§36 Fibrations#^def-36-1|Def. §36.1]]

## Lecture 15 and the Standard Coordinates

*Lecture 15 returned to the cotangent bundle — “we did define it, but it was all very quick” — because the homework uses it: “the standard coordinates on $T^{\ast}M$, which are also trivializations”, with the components found by evaluating on the dual basis, as in [[§45 The Cotangent Bundle#^def-45-4|Definitions §45.4]] and [[§45 The Cotangent Bundle#^def-45-5|§45.5]]. He also recalled that the cotangent space has a description from germs, $T_p^{\ast}M \cong I_p/I_p^2$ ([[§32 The Cotangent Space#^thm-32-8|Theorem §32.8]]): “the cotangent space is, in a way, very extremely natural from the point of view of functions.”*

**Transcription note.** Page 40 of the handwritten notes writes the standard coordinates as a map on $T^{\ast}M$; they are defined on $T^{\ast}U$, the part of the bundle over the chart domain, as Uribe corrected in lecture.

“We'll see that the cotangent bundle has a natural structure that the tangent bundle doesn't have.” $TM$ and $T^*M$ are isomorphic as vector bundles, “but not naturally isomorphic — we have to make choices to construct an isomorphism” (a metric, for instance, as in the [[§35 Submanifolds#^rem-35-1|remark on conormal spaces]]). This is stated, not proved, here.
