---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 42
tags: [differentiable-manifolds, math591]
---
← [[§41 The Tangent Bundle]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§43 One-Forms]] →

*Stage: bundles — The cotangent spaces assembled into $T^{\ast}M$, with charts from the dual bases; covector components transform by the inverse transpose.*

*Lecture 13 defined the cotangent bundle — “completely analogous” to the tangent bundle, with the dual bases in place of the coordinate bases; Lecture 15 returned to it for the homework.*

> [!definition] Definition §42.1: The Cotangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **cotangent bundle** is the set
>
> $$
> T^*M = \bigcup_{p \in M} \{p\} \times T_p^*M = \{\, (p, \xi) : p \in M,\ \xi \in T_p^*M \,\},
> $$
>
> all the cotangent spaces ([[§30 The Cotangent Space#^def-30-1|Definition §30.1]]) put together.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-42-1

> [!definition] Definition §42.2: The Projection of $T^*M$
> The **projection** of the cotangent bundle is
>
> $$
> \pi : T^*M \longrightarrow M, \qquad \pi(p, \xi) = p .
> $$
>
> Its fibre over $p$, $\pi^{-1}(p) = \{p\} \times T_p^{\ast}M$, is identified with $T_p^{\ast}M$.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-42-2

> [!definition] Definition §42.3: The Zero Section of $T^*M$
> The **zero section** of the cotangent bundle is
>
> $$
> \zeta : M \longrightarrow T^*M, \qquad \zeta(p) = (p, 0) .
> $$
>
> It is one-to-one, as for $TM$ ([[§41 The Tangent Bundle#^def-41-3|Definition §41.3]]): every cotangent space has a distinguished element, its zero.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-42-3

> [!remark]- Connections
> - The fibre $T_p^*M$ is a dual space, [[§12 Duality#^ladr-3-110|LADR 3.110]], and the chart uses the dual basis, [[§12 Duality#^ladr-3-112|LADR 3.112]]. Counterpart in 452: differential forms on $\mathbb{R}^n$, [[§21 Introduction to Differential Forms#^def-21-new1|452 Def. §21.1]].

The definitions and results of this section run parallel to those for the tangent bundle in [[§41 The Tangent Bundle|§41]], item for item, with the dual bases $dx^i|_p$ in place of the coordinate bases $\partial/\partial x^i|_p$. Lecture 13 gave the charts and the transition maps; the rest is filled in, following [[§41 The Tangent Bundle|§41]].

## Trivializations and Charts

> [!definition] Definition §42.4: Local Trivializations of $T^*M$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $T^{\ast}U = \pi^{-1}(U) = \{(p, \xi) \in T^{\ast}M : p \in U\}$, the covectors at points of $U$. The **local trivialization** of $T^{\ast}M$ over $U$ is
>
> $$
> \Psi : T^*U \longrightarrow U \times \mathbb{R}^m, \qquad \Psi(p, \xi) = (p, \xi_1, \ldots, \xi_m), \qquad \text{where } \xi = \sum_{i=1}^m \xi_i\, dx^i\big|_p ,
> $$
>
> the components of $\xi$ in the dual basis. Because the bases $dx^i|_p$ and $\partial/\partial x^i|_p$ are dual to each other, the components are computed by evaluation, $\xi_i = \xi\big(\partial/\partial x^i|_p\big)$ ([[§30 The Cotangent Space#^cor-30-3|Corollary §30.3]]). $\Psi$ is a bijection, and $\mathrm{pr}_1 \circ \Psi = \pi$.
>
> *Lee: Proposition 11.9*

^def-42-4

> [!definition] Definition §42.5: Charts of $T^*M$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $\Psi$ the local trivialization over $U$ ([[§42 The Cotangent Bundle#^def-42-4|Definition §42.4]]). The **chart** of $T^{\ast}M$ over $U$ — the **standard coordinates** on $T^{\ast}U$ — is
>
> $$
> \hat\varphi = (\varphi \times \mathrm{id}) \circ \Psi : T^*U \longrightarrow \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}, \qquad (p, \xi) \longmapsto \big(x^1(p), \ldots, x^m(p), \xi_1, \ldots, \xi_m\big).
> $$
>
> It is a bijection, with inverse $(r, \xi) \mapsto \big(\varphi^{-1}(r), \sum_i \xi_i\, dx^i|_{\varphi^{-1}(r)}\big)$.
>
> *Lee: Proposition 11.9*

^def-42-5

> [!theorem] Proposition §42.1: The Topology of $T^*M$
> There is a unique topology on $T^{\ast}M$ for which every $T^{\ast}U$ is open and every chart $\hat\varphi : T^{\ast}U \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $T^{\ast}M$ is a topological manifold of dimension $2m$.
>
> *Lee: Lemma 1.35 and Proposition 11.9*

^prop-42-1

> [!proof]+ Proof
> *(Not from lecture — “completely analogous”; filled in.)* The proof of [[§41 The Tangent Bundle#^prop-41-1|Proposition §41.1]] uses only two facts about the charts $\tilde\varphi$: each is a bijection of $TU$ onto the open set $\varphi(U) \times \mathbb{R}^m$, and each transition map $\tilde\psi \circ \tilde\varphi^{-1}$ is a homeomorphism between the open sets $\varphi(U \cap V) \times \mathbb{R}^m$ and $\psi(U \cap V) \times \mathbb{R}^m$. Both hold for the charts $\hat\varphi$: the first by [[§42 The Cotangent Bundle#^def-42-5|Definition §42.5]], and the second by the computation in the proof of [[§42 The Cotangent Bundle#^prop-42-2|Proposition §42.2]] below, which uses only the definitions of the charts, not any topology on $T^{\ast}M$. With $\hat\varphi$, $\hat\psi$ and $T^{\ast}U$ in place of $\tilde\varphi$, $\tilde\psi$ and $TU$, the proof then goes through word for word:
> - declare $W \subseteq T^{\ast}M$ open if $\hat\varphi(W \cap T^{\ast}U)$ is open in $\mathbb{R}^{2m}$ for every chart $(U, \varphi)$; this is a topology, since each $\hat\varphi$ is a bijection;
> - each $T^{\ast}U$ is open, because $\hat\psi(T^{\ast}U \cap T^{\ast}V) = \psi(U \cap V) \times \mathbb{R}^m$ is open, and each $\hat\varphi$ is a homeomorphism onto its open image, because the transition maps are homeomorphisms;
> - any topology with these two properties has the same open sets, since $W = \bigcup_U (W \cap T^{\ast}U)$;
> - $T^{\ast}M$ is locally Euclidean of dimension $2m$, through the charts;
> - it is Hausdorff: two covectors at the same point lie in one $T^{\ast}U$, homeomorphic to a subset of $\mathbb{R}^{2m}$, and covectors at distinct points $p \neq q$ lie in the disjoint open sets $T^{\ast}U$, $T^{\ast}V$ for charts with disjoint domains $U \ni p$, $V \ni q$;
> - it is second countable: countably many chart domains $U_B$ cover $M$, so the countably many open sets $T^{\ast}U_B$, each with a countable basis, cover $T^{\ast}M$.

^pf-42-1

*Uses:* [[§41 The Tangent Bundle#^prop-41-1|§41.1]], [[§42 The Cotangent Bundle#^def-42-5|Def. §42.5]], [[§42 The Cotangent Bundle#^prop-42-2|§42.2]]

> [!theorem] Proposition §42.2: The Smooth Atlas of $T^*M$
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

^prop-42-2

> [!proof]+ Proof
> *(Lecture 13: “completely analogous”, with the change “we use the dual basis”, and the formula for $dx^i$ given; the rest is filled in.)* The formula for $dx^i|_p$ is [[§30 The Cotangent Space#^lem-30-2|Lemma §30.2]] applied to the function $x^i$ in the chart $\psi$. Substituting it into $\sum_i \xi_i\, dx^i|_p$ and comparing coefficients of $dy^j|_p$ gives $\eta_j$. The matrix $\big[\partial x^i/\partial y^j\big]$ is the inverse of $\big[\partial y^i/\partial x^j\big]$ (chain rule), so the tangent components transform by $A = \big[\partial y^i/\partial x^j\big]$ and the covector components by $(A^{-1})^{\mathsf T}$. Its entries are smooth functions of the base point, so the transition maps are smooth, as in [[§41 The Tangent Bundle#^prop-41-2|Proposition §41.2]]; the fibration and linearity statements follow as in [[§41 The Tangent Bundle#^cor-41-3|Corollary §41.3]].
> Explicitly, with $p = \varphi^{-1}(r)$, the matrix $\big[\partial y^i/\partial x^j(p)\big]$ is $\tau'(r)$ ([[§28 The Differential in Coordinates#^prop-28-1|Proposition §28.1]]), so $\big[\partial x^i/\partial y^j(p)\big] = \tau'(r)^{-1}$ and $\eta = \big(\tau'(r)^{-1}\big)^{\mathsf T}\xi$, which is the displayed transition map. Its entries are smooth in $r$: those of $\tau'(r)$ are, and the inverse of an invertible matrix is given by Cramer's rule, a quotient of polynomials in the entries by the nonzero determinant. The inverse transition map is the same formula with the two charts exchanged.

^pf-42-2

*Uses:* [[§42 The Cotangent Bundle#^def-42-5|Def. §42.5]], [[§30 The Cotangent Space#^def-30-1|Def. §30.1]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§28 The Differential in Coordinates#^cor-28-3|§28.3]], [[§41 The Tangent Bundle#^prop-41-2|§41.2]], [[§41 The Tangent Bundle#^cor-41-3|§41.3]], [[Multivariable Chain Rule|452 §10.2]], [[§12 Duality#^ladr-3-132|LADR 3.132]], [[§28 The Differential in Coordinates#^prop-28-1|§28.1]]

> [!remark]- Connections
> - The matrix of a dual map in dual bases is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].
> - The rule for $dx^i$ is the substitution step of the pullback in 452, [[§22 The Algebra of Differential Forms#^def-22-3|452 Def. §22.3]], applied to the transition map.

> [!theorem] Corollary §42.3: The Cotangent Bundle Is a Fibration
> With the smooth structure of [[§42 The Cotangent Bundle#^prop-42-2|Proposition §42.2]]:
> 1. $T^{\ast}M$ is a smooth manifold of dimension $2m$, and $\pi : T^{\ast}M \to M$ is smooth;
> 2. the $\Psi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Psi$ restricts on the fibre $T_p^{\ast}M$ to a linear isomorphism $T_p^{\ast}M \to \{p\} \times \mathbb{R}^m$; so $T^{\ast}M$ is a vector bundle;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $T^{\ast}M$ of codimension $m$.
>
> *Lee: Proposition 11.9*

^cor-42-3

> [!proof]+ Proof
> *(Not from lecture; filled in, as [[§41 The Tangent Bundle#^cor-41-3|Corollary §41.3]].)* (1) By [[§42 The Cotangent Bundle#^prop-42-1|Propositions §42.1]] and [[§42 The Cotangent Bundle#^prop-42-2|§42.2]]. In the charts $\hat\varphi$ and $\varphi$, $\pi$ is $(r, \xi) \mapsto r$, which is smooth. (2) $\Psi = (\varphi^{-1} \times \mathrm{id}) \circ \hat\varphi$ is a composite of diffeomorphisms ([[§26 Derivations and the Abstract Tangent Space#^prop-26-9|Proposition §26.9]]), and $\mathrm{pr}_1 \circ \Psi = \pi$; the $T^{\ast}U$ cover $T^{\ast}M$ and the $U$ cover $M$. On $T_p^{\ast}M$, $\Psi$ is $\xi \mapsto (p, \xi_1, \ldots, \xi_m)$, taking components in a basis, which is a linear isomorphism. (3) In the chart $\hat\varphi$, $\zeta(M) \cap T^{\ast}U = \{\xi_1 = \cdots = \xi_m = 0\}$, so the charts $\hat\varphi$ are adapted to $\zeta(M)$ ([[§33 Submanifolds#^def-33-1|Definition §33.1]]).

^pf-42-3

*Uses:* [[§42 The Cotangent Bundle#^prop-42-1|§42.1]], [[§42 The Cotangent Bundle#^prop-42-2|§42.2]], [[§42 The Cotangent Bundle#^def-42-4|Def. §42.4]], [[§42 The Cotangent Bundle#^def-42-5|Def. §42.5]], [[§26 Derivations and the Abstract Tangent Space#^prop-26-9|§26.9]], [[§33 Submanifolds#^def-33-1|Def. §33.1]], [[§34 Fibrations#^def-34-1|Def. §34.1]]

## Lecture 15 and the Standard Coordinates

*Lecture 15 returned to the cotangent bundle — “we did define it, but it was all very quick” — because the homework uses it: “the standard coordinates on $T^{\ast}M$, which are also trivializations”, with the components found by evaluating on the dual basis, as in [[§42 The Cotangent Bundle#^def-42-4|Definitions §42.4]] and [[§42 The Cotangent Bundle#^def-42-5|§42.5]]. He also recalled that the cotangent space has a description from germs, $T_p^{\ast}M \cong I_p/I_p^2$ ([[§30 The Cotangent Space#^thm-30-8|Theorem §30.8]]): “the cotangent space is, in a way, very extremely natural from the point of view of functions.”*

**Transcription note.** Page 40 of the handwritten notes writes the standard coordinates as a map on $T^{\ast}M$; they are defined on $T^{\ast}U$, the part of the bundle over the chart domain, as Uribe corrected in lecture.

“We'll see that the cotangent bundle has a natural structure that the tangent bundle doesn't have.” $TM$ and $T^*M$ are isomorphic as vector bundles, “but not naturally isomorphic — we have to make choices to construct an isomorphism” (a metric, for instance, as in the [[§33 Submanifolds#^rem-33-1|remark on conormal spaces]]). This is stated, not proved, here.
