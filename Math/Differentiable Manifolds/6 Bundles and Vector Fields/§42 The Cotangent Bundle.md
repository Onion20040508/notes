---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 42
tags: [differentiable-manifolds, math591]
---
← [[§41 The Tangent Bundle]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§43 Vector Fields and One-Forms]] →

*Stage: bundles — The cotangent spaces assembled into $T^{\ast}M$, with charts from the dual bases; covector components transform by the inverse transpose.*

*Lecture 13 defined the cotangent bundle — “completely analogous” to the tangent bundle, with the dual bases in place of the coordinate bases; Lecture 15 returned to it for the homework.*

> [!definition] Definition §42.1: The Cotangent Bundle
> The **cotangent bundle** of $M$ is
>
> $$
> T^*M = \bigcup_{p \in M} \{p\} \times T_p^*M,
> $$
>
> with projection $\pi(p, \xi) = p$. For a chart $(U, \varphi = (x^i))$ of $M$, its chart is
>
> $$
> T^*U \longrightarrow \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}, \qquad (p, \xi) \longmapsto \big(x^1(p), \ldots, x^m(p), \xi_1, \ldots, \xi_m\big),
> $$
>
> where $T^*U = \pi^{-1}(U)$ and $\xi = \sum_i \xi_i\, dx^i|_p$ in the dual basis ([[§30 The Cotangent Space#^def-30-1|Definition §30.1]]). Because the bases $dx^i|_p$ and $\partial/\partial x^i|_p$ are dual to each other, the components are computed by evaluation, $\xi_i = \xi\big(\partial/\partial x^i|_p\big)$ ([[§30 The Cotangent Space#^cor-30-3|Corollary §30.3]]). Keeping $p$ instead of its coordinates, $(p, \xi) \mapsto (p, \xi_1, \ldots, \xi_m)$ is a local trivialization $T^*U \to U \times \mathbb{R}^m$.
>
> *Lee: Proposition 11.9*

^def-42-1

> [!remark]- Connections
> - The fibre $T_p^*M$ is a dual space, [[§12 Duality#^ladr-3-110|LADR 3.110]], and the chart uses the dual basis, [[§12 Duality#^ladr-3-112|LADR 3.112]]. Counterpart in 452: differential forms on $\mathbb{R}^n$, [[§21 Introduction to Differential Forms#^def-21-1|452 Def. §21.1]].

> [!theorem] Proposition §42.1: The Cotangent Transition Maps
> For charts $\varphi = (x^i)$ and $\psi = (y^j)$, if $\xi = \sum_i \xi_i\, dx^i|_p = \sum_j \eta_j\, dy^j|_p$, then
>
> $$
> dx^i|_p = \sum_j \frac{\partial x^i}{\partial y^j}(p)\, dy^j|_p, \qquad \eta_j = \sum_i \frac{\partial x^i}{\partial y^j}(p)\, \xi_i .
> $$
>
> So the covector components transform by the transpose of the inverse of the matrix that transforms tangent components, and the charts of $T^*M$ form a smooth atlas making $\pi : T^*M \to M$ a vector bundle with fibre $\mathbb{R}^m$.
>
> *Lee: Proposition 11.9*

^prop-42-1

> [!proof]+ Proof
> *(Lecture 13: “completely analogous”, with the change “we use the dual basis”, and the formula for $dx^i$ given; the rest is filled in.)* The formula for $dx^i|_p$ is [[§30 The Cotangent Space#^lem-30-2|Lemma §30.2]] applied to the function $x^i$ in the chart $\psi$. Substituting it into $\sum_i \xi_i\, dx^i|_p$ and comparing coefficients of $dy^j|_p$ gives $\eta_j$. The matrix $\big[\partial x^i/\partial y^j\big]$ is the inverse of $\big[\partial y^i/\partial x^j\big]$ (chain rule), so the tangent components transform by $A = \big[\partial y^i/\partial x^j\big]$ and the covector components by $(A^{-1})^{\mathsf T}$. Its entries are smooth functions of the base point, so the transition maps are smooth, as in [[§41 The Tangent Bundle#^prop-41-2|Proposition §41.2]]; the fibration and linearity statements follow as in [[§41 The Tangent Bundle#^cor-41-3|Corollary §41.3]].

^pf-42-1

*Uses:* [[§42 The Cotangent Bundle#^def-42-1|Def. §42.1]], [[§30 The Cotangent Space#^def-30-1|Def. §30.1]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§28 The Differential in Coordinates#^cor-28-3|§28.3]], [[§41 The Tangent Bundle#^prop-41-2|§41.2]], [[§41 The Tangent Bundle#^cor-41-3|§41.3]], [[Multivariable Chain Rule|452 §10.2]], [[§12 Duality#^ladr-3-132|LADR 3.132]]

> [!remark]- Connections
> - The matrix of a dual map in dual bases is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].
> - The rule for $dx^i$ is the substitution step of the pullback in 452, [[§22 The Algebra of Differential Forms#^def-22-3|452 Def. §22.3]], applied to the transition map.

*Lecture 15 returned to the cotangent bundle — “we did define it, but it was all very quick” — because the homework uses it: “the standard coordinates on $T^{\ast}M$, which are also trivializations”, with the components found by evaluating on the dual basis, as in [[§42 The Cotangent Bundle#^def-42-1|Definition §42.1]]. He also recalled that the cotangent space has a description from germs, $T_p^{\ast}M \cong I_p/I_p^2$ ([[§30 The Cotangent Space#^thm-30-8|Theorem §30.8]]): “the cotangent space is, in a way, very extremely natural from the point of view of functions.”*

**Transcription note.** Page 40 of the handwritten notes writes the standard coordinates as a map on $T^{\ast}M$; they are defined on $T^{\ast}U$, the part of the bundle over the chart domain, as Uribe corrected in lecture.

“We'll see that the cotangent bundle has a natural structure that the tangent bundle doesn't have.” $TM$ and $T^*M$ are isomorphic as vector bundles, “but not naturally isomorphic — we have to make choices to construct an isomorphism” (a metric, for instance, as in the [[§33 Submanifolds#^rem-33-1|remark on conormal spaces]]). This is stated, not proved, here.
