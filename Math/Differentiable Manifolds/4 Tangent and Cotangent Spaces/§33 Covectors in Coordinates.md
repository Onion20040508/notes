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
> This is the defining property of the dual basis (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]) of the basis $\{\partial/\partial x^j|_p\}$ of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). By Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]] the $dx^i|_p$ form a basis of $T_p^{\ast}M$, and $\dim T_p^{\ast}M = m$.
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

*Uses:* [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§12 Duality#^ladr-3-112|LADR 3.112]], [[Linear map lemma|LADR 3.4]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]

> [!remark]- Connections
> - The dual basis and its coefficients: [[§12 Duality#^ladr-3-112|LADR 3.112]], [[§12 Duality#^ladr-3-114|LADR 3.114]], [[§12 Duality#^ladr-3-116|LADR 3.116]].

> [!definition] Definition §33.1: Components of a Covector
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a chart at $p$ and $\xi \in T_p^{\ast}M$. The **components** of $\xi$ in the chart are the numbers
>
> $$
> \xi_i = \xi\Big(\frac{\partial}{\partial x^i}\Big|_p\Big), \qquad i = 1, \ldots, m,
> $$
>
> the values of $\xi$ on the coordinate basis of $T_pM$. They are the covector counterpart of the components $v^i = v[x^i]$ of a tangent vector $v \in T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). The letters $\xi$ and $\xi_i$ are used for a covector and its components from here on, as in the coordinates $(x^1, \ldots, x^m, \xi_1, \ldots, \xi_m)$ of $T^{\ast}M$ ([[§52 The Cotangent Bundle|§52]]).

^def-33-1

> [!theorem] Corollary §33.2: Covectors in the Dual Basis
> In a chart $(x^1, \ldots, x^m)$ near $p$, every covector $\xi \in T_p^{\ast}M$ is the combination of the dual basis $dx^1|_p, \ldots, dx^m|_p$ whose coefficients are its components (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]):
>
> $$
> \xi = \sum_{j=1}^m \xi_j\, dx^j\big|_p, \qquad \xi_j = \xi\Big(\frac{\partial}{\partial x^j}\Big|_p\Big),
> $$
>
> and these are the only coefficients for which the expansion holds.
>
> *Lee: Ch. 11, Covectors*

^cor-33-2

> [!proof]+ Proof
> *(Lecture 15 recalled the basis $dx^j|_p$ — “a fact that I forgot to mention to remind you” — and read off the components by evaluation.)* Two things are claimed: the expansion, and the uniqueness of its coefficients.
>
> *The expansion.* By Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], $(dx^1|_p, \ldots, dx^m|_p)$ is the dual basis (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]) of the basis $(\partial/\partial x^1|_p, \ldots, \partial/\partial x^m|_p)$ of $T_pM$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). So the second formula of Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]] applies, with $V = T_pM$, $e_j = \partial/\partial x^j|_p$, $\varepsilon^j = dx^j|_p$ and $\lambda = \xi$; with Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]] it reads
>
> $$
> \xi = \sum_{j=1}^m \xi\Big(\frac{\partial}{\partial x^j}\Big|_p\Big)\, dx^j\big|_p = \sum_{j=1}^m \xi_j\, dx^j\big|_p .
> $$
>
> *Uniqueness.* By the same proposition the $dx^j|_p$ form a basis of $T_p^{\ast}M$, so the coefficients are unique. Explicitly: if $\xi = \sum_j c_j\, dx^j|_p$, evaluate both sides at $\partial/\partial x^k|_p$, using that covectors are added and scaled pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]) and that $dx^j|_p(\partial/\partial x^k|_p) = \delta^j_k$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]):
>
> $$
> \xi_k = \xi\Big(\frac{\partial}{\partial x^k}\Big|_p\Big) = \sum_{j=1}^m c_j\, dx^j\big|_p\Big(\frac{\partial}{\partial x^k}\Big|_p\Big) = \sum_{j=1}^m c_j\, \delta^j_k = c_k .
> $$
>
> So the coefficients are the components, $c_k = \xi_k$.

^pf-33-2

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§33 Covectors in Coordinates#^def-33-1|Def. §33.1]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]]

> [!remark]- Connections
> - The same expansion in LADR: [[§12 Duality#^ladr-3-112|LADR 3.112]] (dual basis). The components are what the local trivializations and charts of the cotangent bundle record, [[§52 The Cotangent Bundle#^def-52-4|Def. §52.4]], [[§52 The Cotangent Bundle#^def-52-5|Def. §52.5]].

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
> “The standard formula from Calc 3 now has this manifold general interpretation.” The formula $df = \sum \partial f/\partial x^i\,dx^i$ of multivariable calculus is now a statement about covectors: the $dx^i|_p$ are not infinitesimals but the dual basis of the coordinate derivations, the coefficients are numbers, and the dual basis “extracts the components of a vector in the original basis.” What does *not* survive on a manifold is the gradient. A function on $M$ has no gradient *vector* — converting $df_p$ into a vector requires an inner product on $T_pM$, i.e. a Riemannian metric — but it always has its differential $df_p \in T_p^{\ast}M$, and that is where differentials of scalar functions live. Differential forms, later in the term, will be built from covectors, and will pull back as naturally as germs do. Uribe also announced that tangent vectors, written $D$ while thought of as derivations, will soon be written $v$. On $\mathbb{R}^n$ there is such an inner product, the dot product: Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]] and Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]] below make the conversion between the gradient and the differential precise. They are used later, for Lagrange multipliers (Theorem [[§39 Transversality and Lagrange Multipliers#^thm-39-6|§39.6]]) and for the normal bundle ([[§42 The Normal Bundle of a Submanifold of Euclidean Space|§42]]).

^rem-33-2

*Not from lecture: the gradient of calculus, used informally since [[§7 The Regular Value Theorem|§7]], and the dot-product identification of vectors with covectors on open subsets of $\mathbb{R}^n$, which turns the gradient into the differential.*

> [!remark]- Connections
> - The Calc 3 formula and the gradient it replaces: [[§39 Closed and Exact Forms#^prop-39-1|452 §39.1]], [[§10 The Differential#^def-10-1|452 Def. §10.1]].
> - Converting a covector into a vector with an inner product: [[Riesz representation theorem|LADR 6.42]].
> - The same point for normal vectors: [[§37 Regular Submanifolds#^rem-37-1|No Normal Vectors Without a Metric]].

> [!definition] Definition §33.2: Gradient
> Let $U \subseteq \mathbb{R}^n$ be open, $p \in U$, and $h$ a smooth function defined near $p$. The **gradient** of $h$ at $p$ is the vector of its ordinary partial derivatives,
>
> $$
> \nabla h(p) = \Big( \frac{\partial h}{\partial r^1}(p), \ldots, \frac{\partial h}{\partial r^n}(p) \Big) \in \mathbb{R}^n ,
> $$
>
> the single row of the Jacobian of $h$ at $p$ (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]), read as a vector of $\mathbb{R}^n$. Each $\partial h/\partial r^i(p)$ is also the coordinate derivation $\partial/\partial r^i|_p[h]$ of the identity chart (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]), in which $h$ is its own coordinate representation.

^def-33-2

> [!remark]- Connections
> - The gradient of calculus: [[§111 Directional Derivatives and the Gradient Vector#^def-111-2|Calc Def. §111.2]]; on a manifold there is no gradient without a metric (the remark [[§33 Covectors in Coordinates#^rem-33-2|Differential — Not Gradient]]).

> [!theorem] Proposition §33.3: Vectors as Covectors through the Dot Product
> Let $U \subseteq \mathbb{R}^n$ be open and $p \in U$, with $T_pU = T_p\mathbb{R}^n$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), and for $w \in \mathbb{R}^n$ let $D_w|_p \in T_p\mathbb{R}^n$ be the directional derivative of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]. For $v \in \mathbb{R}^n$ define $\xi_v : T_pU \to \mathbb{R}$ by
>
> $$
> \xi_v\big(D_w|_p\big) = v \cdot w \qquad (w \in \mathbb{R}^n).
> $$
>
> 1. $\xi_v \in T_p^{\ast}U$, and $\mathbb{R}^n \to T_p^{\ast}U$, $v \mapsto \xi_v$, is a linear isomorphism.
> 2. In the identity chart, with coordinates $r^1, \ldots, r^n$, $\xi_v = \sum_{i=1}^n v^i\, dr^i|_p$: the components of $\xi_v$ are the entries of $v$.
> 3. For $h$ smooth near $p$, $\xi_{\nabla h(p)} = dh_p$ (Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]). That is, $dh_p(D_w|_p) = \nabla h(p) \cdot w$ for every $w \in \mathbb{R}^n$, and the components of $dh_p$ in the identity chart are the entries of $\nabla h(p)$.

^prop-33-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Two facts about the vectors $D_w|_p$ are used throughout. By Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], with $V = \mathbb{R}^n$ and $a = p$, the map $w \mapsto D_w|_p$ is a linear isomorphism $\mathbb{R}^n \to T_p\mathbb{R}^n$, so every tangent vector at $p$ is $D_w|_p$ for exactly one $w \in \mathbb{R}^n$. And by Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]] (its second statement, with $W = U$ and $a = p$), $D_w|_p[g] = \frac{d}{dt}\big|_{t=0}\, g(p + tw) = \sum_i w^i\, \partial g/\partial r^i(p)$ for every germ $[g]$ at $p$, the partial derivatives being the coordinate derivations of the identity chart; two derivations that agree on every germ are equal, so
>
> $$
> D_w|_p = \sum_{i=1}^n w^i\, \frac{\partial}{\partial r^i}\Big|_p, \qquad\text{in particular}\qquad D_{e_i}|_p = \frac{\partial}{\partial r^i}\Big|_p .
> $$
>
> *(1) $\xi_v$ is a covector.* $\xi_v$ is the composite of the inverse isomorphism $T_p\mathbb{R}^n \to \mathbb{R}^n$, $D_w|_p \mapsto w$, with the linear map $w \mapsto v \cdot w$; so it is well defined and linear, $\xi_v \in T_p^{\ast}U$ (Definition [[§32 The Cotangent Space#^def-32-4|§32.4]]).
>
> *(1) Linearity in $v$.* For $v, v' \in \mathbb{R}^n$ and $a, b \in \mathbb{R}$, at every $D_w|_p$, by the bilinearity of the dot product and the pointwise operations of $T_p^{\ast}U$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]),
>
> $$
> \xi_{av + bv'}\big(D_w|_p\big) = (av + bv') \cdot w = a\, v \cdot w + b\, v' \cdot w = \big(a\,\xi_v + b\,\xi_{v'}\big)\big(D_w|_p\big) .
> $$
>
> Every tangent vector at $p$ is some $D_w|_p$, so $\xi_{av + bv'} = a\,\xi_v + b\,\xi_{v'}$.
>
> *(1) Isomorphism.* If $\xi_v = 0$, then $0 = \xi_v(D_v|_p) = v \cdot v = |v|^2$, so $v = 0$: the map is injective. Both spaces have dimension $n$: $\mathbb{R}^n$, and $T_p^{\ast}U$ by Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] in the identity chart. An injective linear map between spaces of the same finite dimension is bijective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), so $v \mapsto \xi_v$ is a linear isomorphism: the dot product identifies vectors with covectors.
>
> *(2)* By $D_{e_i}|_p = \partial/\partial r^i|_p$, the components of $\xi_v$ (Definition [[§33 Covectors in Coordinates#^def-33-1|§33.1]]) are
>
> $$
> \xi_v\Big(\frac{\partial}{\partial r^i}\Big|_p\Big) = \xi_v\big(D_{e_i}|_p\big) = v \cdot e_i = v^i ,
> $$
>
> and Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], in the identity chart, gives $\xi_v = \sum_i v^i\, dr^i|_p$.
>
> *(3)* Let $w \in \mathbb{R}^n$. By Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], the formula for $D_w|_p$ above (derivations are added and scaled pointwise, Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]), and Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]],
>
> $$
> dh_p\big(D_w|_p\big) = D_w|_p[h] = \sum_{i=1}^n w^i\, \frac{\partial}{\partial r^i}\Big|_p[h] = \sum_{i=1}^n \frac{\partial h}{\partial r^i}(p)\, w^i = \nabla h(p) \cdot w = \xi_{\nabla h(p)}\big(D_w|_p\big) .
> $$
>
> The covectors $dh_p$ and $\xi_{\nabla h(p)}$ agree at every $D_w|_p$, that is, at every tangent vector at $p$, so they are equal. By (2), the components of $dh_p = \xi_{\nabla h(p)}$ are the entries $\partial h/\partial r^i(p)$ of $\nabla h(p)$ — which is also Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] in the identity chart, $dh_p = \sum_i \partial h/\partial r^i(p)\, dr^i|_p$.

^pf-33-3

*Uses:* [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§32 The Cotangent Space#^def-32-4|Def. §32.4]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§33 Covectors in Coordinates#^def-33-1|Def. §33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§33 Covectors in Coordinates#^def-33-2|Def. §33.2]]
