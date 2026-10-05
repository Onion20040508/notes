---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 43
tags: [differentiable-manifolds, math591]
---
← [[§42 The Cotangent Bundle]] · ↑ [[· 6 Bundles and Vector Fields]] · [[§44 The Operator d and Pullbacks of One-Forms]] →

*Stage: fields — Smooth sections of $TM$ and of $T^{\ast}M$: a tangent vector, or a covector, at every point, chosen smoothly — and the coordinate test for smoothness.*

*Lectures 13 and 15. A section of a fibration ([[§34 Fibrations#^def-34-2|Definition §34.2]]) picks one point in every fibre; for the tangent and cotangent bundles that point is a vector, or a covector, at every point of $M$. Every vector bundle has sections, the zero section at least — unlike a general fibration: the Hopf fibration has none ([[§37 Projective Spaces and the Hopf Fibration#^rem-37-1|Remark in §37]]).*

## Vector Fields

> [!definition] Definition §43.1: Vector Field
> A **vector field** on $M$ is a section of the tangent bundle $\pi : TM \to M$: a smooth map $X : M \to TM$ with $X(p) \in T_pM$ for every $p$ — “for every point, [it] selects a tangent vector at that point.”
>
> *Lee: Ch. 8, Vector Fields*

^def-43-1

> [!remark]- Connections
> - Vector fields on open subsets of $\mathbb{R}^3$ in 452: [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §11]].

**Transcription note.** Page 36 of the handwritten notes writes “Section of $TM \xrightarrow{F} M$”; the map is the projection $\pi$.

> [!definition] Definition §43.2: The Space of Vector Fields
> A vector field on $M$ is a smooth section $X$ of the tangent bundle $TM \to M$ ([[§43 Vector Fields and One-Forms#^def-43-1|Definition §43.1]]); its value at $p$ is written $X_p \in T_pM$, again with $p$ as a subscript, to make room for the function a tangent vector acts on. The set of all vector fields on $M$ is denoted
>
> $$
> \mathfrak{X}(M) \qquad \big(\text{LaTeX: } \mathtt{\backslash mathfrak\{X\}}\big).
> $$
>
> It is a real vector space, and functions multiply vector fields pointwise: $(fX)_p = f(p) X_p$.
>
> *Lee: Ch. 8, Vector Fields on Manifolds*

^def-43-2

> [!theorem] Proposition §43.1: Vector Fields in Coordinates
> Let $X$ be a section of $TM$ (not assumed smooth) and $(U, \varphi = (x^j))$ a chart. Then on $U$
>
> $$
> X = \sum_{j=1}^m X^j\, \frac{\partial}{\partial x^j}, \qquad X^j(p) = X_p[x^j] = dx^j|_p(X_p),
> $$
>
> and $X$ is smooth on $U$ if and only if the coefficient functions $X^1, \ldots, X^m$ are smooth on $U$.
>
> *Lee: Proposition 8.1*

^prop-43-1

> [!proof]+ Proof
> *(Stated in Lecture 15, “analogously” to one-forms; filled in.)* The expansion is the basis theorem at each point, with coefficients $X_p[x^j]$ ([[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|Theorem §27.5]]). In the chart $\tilde\varphi$ of $TM$ ([[§41 The Tangent Bundle#^def-41-2|Definition §41.2]]) the coordinate representation of $X$ is $r \mapsto \big(r, X^1(\varphi^{-1}(r)), \ldots, X^m(\varphi^{-1}(r))\big)$, smooth exactly when every $X^j \circ \varphi^{-1}$ is.

^pf-43-1

*Uses:* [[§43 Vector Fields and One-Forms#^def-43-1|Def. §43.1]], [[§27 Coordinate Derivations and the Basis Theorem#^thm-27-5|§27.5]], [[§30 The Cotangent Space#^prop-30-1|§30.1]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§41 The Tangent Bundle#^def-41-2|Def. §41.2]], [[§41 The Tangent Bundle#^prop-41-2|§41.2]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§18 Smooth Functions and Smooth Maps#^prop-18-2|§18.2]]

## One-Forms

*Lecture 15. The sections of the cotangent bundle.*

> [!definition] Definition §43.3: One-Form
> A **one-form** (or *$1$-form*, or *covector field*) on $M$ is a smooth section $\theta : M \to T^{\ast}M$ of the cotangent bundle: $\pi \circ \theta = \mathrm{id}_M$, so that $\theta$ assigns to every $p \in M$ a covector in $T_p^{\ast}M$. This value is written $\theta_p$, not $\theta(p)$, and it is a linear function $\theta_p : T_pM \to \mathbb{R}$, $v \mapsto \theta_p(v)$. The space of one-forms on $M$ is written $C^\infty(M, T^{\ast}M)$ (Uribe's notation; also $\Omega^1(M)$).
>
> *Lee: Ch. 11, Covector Fields*

^def-43-3

> [!remark]- Connections
> - On open subsets of $\mathbb{R}^n$: [[§21 Introduction to Differential Forms#^def-21-1|452 Def. §21.1]] (differential forms, here in degree 1).
> - The value at one point is a covector, an element of a dual space: [[§30 The Cotangent Space#^def-30-1|Def. §30.1]], [[§12 Duality#^ladr-3-110|LADR 3.110]].

Uribe on the notation: “$\theta$ is really a function of two variables, a point and a vector, and you want to make room for the vector variable” — so the point goes into the subscript and the vector into the parentheses. A student asked where a $\theta_p$ comes from; the answer is that the definition describes *every* one-form, and the examples come next.

> [!theorem] Proposition §43.2: One-Forms in Coordinates
> Let $\theta$ be a section of $T^{\ast}M \to M$ (not assumed smooth) and $(U, \varphi = (x^i))$ a chart. Then on $U$
>
> $$
> \theta = \sum_{j=1}^m \theta_j\, dx^j, \qquad \theta_j(p) = \theta_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big),
> $$
>
> and $\theta$ is smooth on $U$ if and only if the coefficient functions $\theta_1, \ldots, \theta_m$ are smooth on $U$.
>
> *Lee: Proposition 11.11*

^prop-43-2

> [!proof]+ Proof
> *(Lecture 15 stated it — “smoothness of the form will translate into these functions being smooth”; the proof is filled in.)* At each $p$ the $dx^j|_p$ form a basis of $T_p^{\ast}M$ dual to the $\partial/\partial x^j|_p$, which gives the expansion and the formula for $\theta_j(p)$. In the chart of $T^{\ast}M$ over $U$ ([[§42 The Cotangent Bundle#^def-42-1|Definition §42.1]]) and the chart $\varphi$ of $M$, the coordinate representation of $\theta$ is $r \mapsto \big(r, \theta_1(\varphi^{-1}(r)), \ldots, \theta_m(\varphi^{-1}(r))\big)$, which is smooth exactly when every $\theta_j \circ \varphi^{-1}$ is.

^pf-43-2

*Uses:* [[§43 Vector Fields and One-Forms#^def-43-3|Def. §43.3]], [[§30 The Cotangent Space#^lem-30-2|§30.2]], [[§30 The Cotangent Space#^cor-30-3|§30.3]], [[§42 The Cotangent Bundle#^def-42-1|Def. §42.1]], [[§42 The Cotangent Bundle#^prop-42-1|§42.1]], [[§18 Smooth Functions and Smooth Maps#^def-18-3|Def. §18.3]], [[§18 Smooth Functions and Smooth Maps#^prop-18-2|§18.2]], [[§12 Duality#^ladr-3-112|LADR 3.112]]
