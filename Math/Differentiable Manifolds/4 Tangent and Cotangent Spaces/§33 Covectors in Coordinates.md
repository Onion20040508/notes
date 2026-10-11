---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 4
section: 33
tags: [differentiable-manifolds, math591]
---
← [[§32 The Cotangent Space]] · ↑ [[· 4 Tangent and Cotangent Spaces]] · [[§34 The Cotangent Space from Germs]] →

*Stage: abstract, dual — In a chart, the differentials $dx^i|_p$ of the coordinate functions form the basis of $T_p^{\ast}M$ dual to the coordinate derivations, and a covector is determined by its components.*

*Lecture 10, continued. The cotangent space and the differential of a function were defined in [[§32 The Cotangent Space|§32]] without coordinates; a chart now gives $T_p^{\ast}M$ a basis, and every covector components.*

> [!theorem] Lemma §33.1: The Differential in Coordinates
> Let $(x^1, \ldots, x^m)$ be coordinates near $p$, and write $dx^i|_p$ for the differential at $p$ of the coordinate function $x^i$. Then $\{dx^1|_p, \ldots, dx^m|_p\}$ is the dual basis of $\{\partial/\partial x^1|_p, \ldots, \partial/\partial x^m|_p\}$, so $\dim T_p^*M = m$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), and for every smooth $f$ defined near $p$,
>
> $$
> df_p = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p .
> $$
>
> *Lee: Ch. 11, Covectors*

^lem-33-1

> [!proof]+ Proof
> *(Lecture 10: “it suffices to check the identity on basis vectors.” In lecture the left side came from the matrix of $f_{\ast p}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]), a $1 \times m$ row — “remember, gradients are across”, after a student first proposed $m \times 1$ — whose $j$-th entry is $\partial f/\partial x^j(p)$. Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] gives the same value directly.)*
>
> *Step 1: the $dx^i|_p$ are the dual basis.* Let $\varphi = (x^1, \ldots, x^m)$ be the chart, so that $x^i \circ \varphi^{-1} = r^i$, the $i$-th standard coordinate of $\mathbb{R}^m$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]). For each $i$ and $j$, Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] with $f = x^i$ and $D = \partial/\partial x^j|_p$, followed by Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], gives
>
> $$
> dx^i|_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \frac{\partial}{\partial x^j}\Big|_p\big[x^i\big] = \frac{\partial (x^i \circ \varphi^{-1})}{\partial r^j}\big(\varphi(p)\big) = \frac{\partial r^i}{\partial r^j}\big(\varphi(p)\big) = \delta^i_j .
> $$
>
> This is the defining property of the dual basis (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]) of the basis $\{\partial/\partial x^j|_p\}$ of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). By Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]] the $dx^i|_p$ form a basis of $T_p^{\ast}M$, and $\dim T_p^{\ast}M = m$.
>
> *Step 2: the formula.* Both sides are linear functionals on $T_pM$, so by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2) it suffices that they agree on each basis vector $\partial/\partial x^j|_p$. The left side gives, by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]],
>
> $$
> df_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \frac{\partial}{\partial x^j}\Big|_p[f] = \frac{\partial f}{\partial x^j}(p) .
> $$
>
> The right side is a linear combination of covectors, evaluated pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]); by Step 1 only the term $i = j$ survives:
>
> $$
> \Big(\sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p\Big)\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, \delta^i_j = \frac{\partial f}{\partial x^j}(p) .
> $$
>
> The two values agree for every $j$, so the two covectors are equal.

^pf-33-1

*Uses:* [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§12 Duality#^ladr-3-112|LADR 3.112]], [[Linear map lemma|LADR 3.4]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]

> [!remark]- Connections
> - The dual basis and its coefficients: [[§12 Duality#^ladr-3-112|LADR 3.112]], [[§12 Duality#^ladr-3-114|LADR 3.114]], [[§12 Duality#^ladr-3-116|LADR 3.116]].

> [!theorem] Corollary §33.2: Components of a Covector
> In a chart $(x^1, \ldots, x^m)$ near $p$, every covector $\alpha \in T_p^*M$ is
>
> $$
> \alpha = \sum_{j=1}^m a_j\, dx^j\big|_p, \qquad a_j = \alpha\Big(\frac{\partial}{\partial x^j}\Big|_p\Big) .
> $$
>
> The numbers $a_1, \ldots, a_m$ are the **components** of $\alpha$ in the chart.
>
> *Lee: Ch. 11, Covectors*

^cor-33-2

> [!proof]+ Proof
> *(Lecture 15 recalled the basis $dx^j|_p$ — “a fact that I forgot to mention to remind you” — and read off the components by evaluation.)* By Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], $(dx^1|_p, \ldots, dx^m|_p)$ is a basis of $T_p^{\ast}M$, so $\alpha = \sum_j a_j\, dx^j|_p$ for unique numbers $a_1, \ldots, a_m$. To find $a_k$, evaluate both sides at $\partial/\partial x^k|_p$, using that covectors are added and scaled pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]) and that $dx^j|_p(\partial/\partial x^k|_p) = \delta^j_k$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]):
>
> $$
> \alpha\Big(\frac{\partial}{\partial x^k}\Big|_p\Big) = \sum_{j=1}^m a_j\, dx^j\big|_p\Big(\frac{\partial}{\partial x^k}\Big|_p\Big) = \sum_{j=1}^m a_j\, \delta^j_k = a_k .
> $$
>
> This is the second formula of Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], with $e_j = \partial/\partial x^j|_p$ and $\varepsilon^j = dx^j|_p$.

^pf-33-2

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]]

> [!remark]- Connections
> - The same expansion in LADR: [[§12 Duality#^ladr-3-112|LADR 3.112]] (dual basis). The components are what the local trivializations and charts of the cotangent bundle record, [[§48 The Cotangent Bundle#^def-48-4|Def. §48.4]], [[§48 The Cotangent Bundle#^def-48-5|Def. §48.5]].

> [!remark] Remark
> Equivalently, by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] with the coordinate $r$ on the target, the matrix of $f_{*p}$ is the $1 \times m$ row
>
> $$
> \Big( \frac{\partial f}{\partial x^1}(p) \ \ \cdots \ \ \frac{\partial f}{\partial x^m}(p) \Big).
> $$
>
> A student proposed $m \times 1$; it is $1 \times m$ — “gradients go across” — since the target is one-dimensional. The lecture's proof took this route and paused over the shape of the matrix; the version above goes through Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] instead, which avoids the question.

^rem-33-1

![[m591-13-2.svg]]
*The differential as a covector, for $f(x,y) = y + 0.3x^2$ near $p = (0.8, 0)$. Left: level curves of $f$ at equal spacing $\Delta$, and a tangent vector $v$ at $p$. Right: in $T_pM$, the level lines of the linear functional $df_p$ at the same spacing — the linearization of the curves on the left, straight and parallel. The value $df_p(v)$ counts, in units of $\Delta$, how many lines $v$ crosses: here exactly $2\Delta$, since $v$ ends on the line $df_p = 2\Delta$. On the left, $v$ crosses* approximately *two level curves; the curvature is what the linearization discards.*

> [!remark] Remark: Differential — Not Gradient
> “The standard formula from Calc 3 now has this manifold general interpretation.” The formula $df = \sum \partial f/\partial x^i\,dx^i$ of multivariable calculus is now a statement about covectors: the $dx^i|_p$ are not infinitesimals but the dual basis of the coordinate derivations, the coefficients are numbers, and the dual basis “extracts the components of a vector in the original basis.” What does *not* survive on a manifold is the gradient. A function on $M$ has no gradient *vector* — converting $df_p$ into a vector requires an inner product on $T_pM$, i.e. a Riemannian metric — but it always has its differential $df_p \in T_p^{\ast}M$, and that is where differentials of scalar functions live. Differential forms, later in the term, will be built from covectors, and will pull back as naturally as germs do. Uribe also announced that tangent vectors, written $D$ while thought of as derivations, will soon be written $v$.

^rem-33-2

> [!remark]- Connections
> - The Calc 3 formula and the gradient it replaces: [[§39 Closed and Exact Forms#^prop-39-1|452 §39.1]], [[§10 The Differential#^def-10-1|452 Def. §10.1]].
> - Converting a covector into a vector with an inner product: [[Riesz representation theorem|LADR 6.42]].
> - The same point for normal vectors: [[§37 Regular Submanifolds#^rem-37-1|No Normal Vectors Without a Metric]].
