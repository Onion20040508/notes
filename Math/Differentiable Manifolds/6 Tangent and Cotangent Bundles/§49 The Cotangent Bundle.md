---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 49
tags: [differentiable-manifolds, math591]
---
← [[§48 The Tangent Bundle]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§50 One-Forms]] →

*Stage: bundles — The cotangent spaces assembled into $T^{\ast}M$, with charts from the dual bases; covector components transform by the inverse transpose.*

*Lecture 13 defined the cotangent bundle — “completely analogous” to the tangent bundle, with the dual bases in place of the coordinate bases; Lecture 15 returned to it for the homework.*

> [!definition] Definition §49.1: The Cotangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **cotangent bundle** is the set
>
> $$
> T^*M = \bigcup_{p \in M} \{p\} \times T_p^*M = \{\, (p, \xi) : p \in M,\ \xi \in T_p^*M \,\},
> $$
>
> all the cotangent spaces ([[§32 The Cotangent Space#^def-32-4|Definition §32.4]]) put together.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-49-1

> [!definition] Definition §49.2: The Projection of $T^*M$
> The **projection** of the cotangent bundle is
>
> $$
> \pi : T^*M \longrightarrow M, \qquad \pi(p, \xi) = p .
> $$
>
> Its fibre over $p$, $\pi^{-1}(p) = \{p\} \times T_p^{\ast}M$, is identified with $T_p^{\ast}M$.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-49-2

> [!definition] Definition §49.3: The Zero Section of $T^*M$
> The **zero section** of the cotangent bundle is
>
> $$
> \zeta : M \longrightarrow T^*M, \qquad \zeta(p) = (p, 0) .
> $$
>
> It is one-to-one, as for $TM$ ([[§48 The Tangent Bundle#^def-48-3|Definition §48.3]]): every cotangent space has a distinguished element, its zero.
>
> *Lee: Ch. 11, The Cotangent Bundle*

^def-49-3

> [!remark]- Connections
> - The fibre $T_p^*M$ is a dual space, [[§12 Duality#^ladr-3-110|LADR 3.110]], and the chart uses the dual basis, [[§12 Duality#^ladr-3-112|LADR 3.112]]. Counterpart in 452: differential forms on $\mathbb{R}^n$, [[§36 Introduction to Differential Forms#^def-36-2|452 Def. §36.2]].

The definitions and results of this section run parallel to those for the tangent bundle in [[§48 The Tangent Bundle|§48]], item for item, with the dual bases $dx^i|_p$ in place of the coordinate bases $\partial/\partial x^i|_p$. Lecture 13 gave the charts and the transition maps; the rest is filled in, following [[§48 The Tangent Bundle|§48]].

## Trivializations and Charts

> [!definition] Definition §49.4: Local Trivializations of $T^*M$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $T^{\ast}U = \pi^{-1}(U) = \{(p, \xi) \in T^{\ast}M : p \in U\}$, the covectors at points of $U$. The **local trivialization** of $T^{\ast}M$ over $U$ is
>
> $$
> \Psi : T^*U \longrightarrow U \times \mathbb{R}^m, \qquad \Psi(p, \xi) = (p, \xi_1, \ldots, \xi_m), \qquad \text{where } \xi = \sum_{i=1}^m \xi_i\, dx^i\big|_p ,
> $$
>
> the components of $\xi$ in the dual basis. Because the bases $dx^i|_p$ and $\partial/\partial x^i|_p$ are dual to each other, the components are computed by evaluation, $\xi_i = \xi\big(\partial/\partial x^i|_p\big)$ ([[§33 Covectors in Coordinates#^cor-33-2|Corollary §33.2]]). $\Psi$ is a bijection, and $\mathrm{pr}_1 \circ \Psi = \pi$.
>
> *Lee: Proposition 11.9*

^def-49-4

> [!definition] Definition §49.5: Charts of $T^*M$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $\Psi$ the local trivialization over $U$ ([[§49 The Cotangent Bundle#^def-49-4|Definition §49.4]]). The **chart** of $T^{\ast}M$ over $U$ — the **standard coordinates** on $T^{\ast}U$ — is
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
> ([[§33 Covectors in Coordinates#^cor-33-2|Corollary §33.2]]). So the first $m$ coordinates of $\hat\varphi(p, \xi)$ locate the point $p$, and the last $m$ list the components of the covector $\xi$. $\hat\varphi$ is a bijection, with inverse
>
> $$
> (r, b_1, \ldots, b_m) \longmapsto \Big(\varphi^{-1}(r),\ \sum_{i=1}^m b_i\, dx^i\big|_{\varphi^{-1}(r)}\Big), \qquad r \in \varphi(U),\ (b_1, \ldots, b_m) \in \mathbb{R}^m .
> $$
>
> *Lee: Proposition 11.9*

^def-49-5

> [!theorem] Proposition §49.1: The Topology of $T^*M$
> There is a unique topology on $T^{\ast}M$ for which every $T^{\ast}U$ is open and every chart $\hat\varphi : T^{\ast}U \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $T^{\ast}M$ is a topological manifold of dimension $2m$.
>
> *Lee: Lemma 1.35 and Proposition 11.9*

^prop-49-1

> [!proof]+ Proof
> *(Not from lecture — “completely analogous”; filled in.)* The proof of [[§48 The Tangent Bundle#^prop-48-1|Proposition §48.1]] uses only two facts about the charts $\tilde\varphi$: each is a bijection of $TU$ onto the open set $\varphi(U) \times \mathbb{R}^m$, and each transition map $\tilde\psi \circ \tilde\varphi^{-1}$ is a homeomorphism between the open sets $\varphi(U \cap V) \times \mathbb{R}^m$ and $\psi(U \cap V) \times \mathbb{R}^m$. Both hold for the charts $\hat\varphi$: the first by [[§49 The Cotangent Bundle#^def-49-5|Definition §49.5]], and the second by the computation in the proof of [[§49 The Cotangent Bundle#^prop-49-2|Proposition §49.2]] below, which uses only the definitions of the charts, not any topology on $T^{\ast}M$. With $\hat\varphi$, $\hat\psi$ and $T^{\ast}U$ in place of $\tilde\varphi$, $\tilde\psi$ and $TU$, the proof then goes through word for word:
> - declare $W \subseteq T^{\ast}M$ open if $\hat\varphi(W \cap T^{\ast}U)$ is open in $\mathbb{R}^{2m}$ for every chart $(U, \varphi)$; this is a topology, since each $\hat\varphi$ is a bijection;
> - each $T^{\ast}U$ is open, because $\hat\psi(T^{\ast}U \cap T^{\ast}V) = \psi(U \cap V) \times \mathbb{R}^m$ is open, and each $\hat\varphi$ is a homeomorphism onto its open image, because the transition maps are homeomorphisms;
> - any topology with these two properties has the same open sets, since $W = \bigcup_U (W \cap T^{\ast}U)$;
> - $T^{\ast}M$ is locally Euclidean of dimension $2m$, through the charts;
> - it is Hausdorff: two covectors at the same point lie in one $T^{\ast}U$, homeomorphic to a subset of $\mathbb{R}^{2m}$, and covectors at distinct points $p \neq q$ lie in the disjoint open sets $T^{\ast}U$, $T^{\ast}V$ for charts with disjoint domains $U \ni p$, $V \ni q$;
> - it is second countable: countably many chart domains $U_B$ cover $M$, so the countably many open sets $T^{\ast}U_B$, each with a countable basis, cover $T^{\ast}M$.

^pf-49-1

*Uses:* [[§48 The Tangent Bundle#^prop-48-1|§48.1]], [[§49 The Cotangent Bundle#^def-49-5|Def. §49.5]], [[§49 The Cotangent Bundle#^prop-49-2|§49.2]]

> [!theorem] Proposition §49.2: The Smooth Atlas of $T^*M$
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

^prop-49-2

> [!proof]+ Proof
> *(Lecture 13: “completely analogous”, with the change “we use the dual basis”, and the formula for $dx^i$ given; the rest is filled in.)* Fix $p \in U \cap V$. Four things are to be shown, in order: the formula for $dx^i|_p$; the formula for $\eta_j$; that $\big[\partial x^i/\partial y^j(p)\big]$ is the inverse of $\big[\partial y^i/\partial x^j(p)\big]$, which gives the transition map; and that the transition maps are smooth, so the charts form a smooth atlas.
>
> *The formula for $dx^i|_p$.* It is Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] applied to the function $f = x^i$, smooth near $p$, in the chart $\psi = (y^1, \ldots, y^m)$ at $p$: the lemma gives $d(x^i)_p = \sum_j \partial x^i/\partial y^j(p)\, dy^j|_p$.
>
> *The formula for $\eta_j$.* Substituting it into $\sum_i \xi_i\, dx^i|_p$ and collecting terms (covectors are added and scaled pointwise, Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]),
>
> $$
> \xi = \sum_i \xi_i\, dx^i\big|_p = \sum_i \xi_i \sum_j \frac{\partial x^i}{\partial y^j}(p)\, dy^j\big|_p = \sum_j \Big( \sum_i \frac{\partial x^i}{\partial y^j}(p)\, \xi_i \Big)\, dy^j\big|_p .
> $$
>
> The $dy^j|_p$ form a basis of $T_p^{\ast}M$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] for the chart $\psi$), so the coefficients of $\xi$ in it are unique; comparing coefficients of $dy^j|_p$ with $\xi = \sum_j \eta_j\, dy^j|_p$ gives $\eta_j = \sum_i \partial x^i/\partial y^j(p)\, \xi_i$.
>
> *The inverse matrix.* Write $A = \big[\partial y^i/\partial x^j(p)\big]$ (row $i$, column $j$) and $B = \big[\partial x^i/\partial y^j(p)\big]$. That $B = A^{-1}$ is the chain rule; written out, evaluate $dx^i|_p$ on $\partial/\partial x^k|_p$ in two ways. Directly, it is $\delta^i_k$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]). Through the formula for $dx^i|_p$, evaluating pointwise and using $dy^j|_p(\partial/\partial x^k|_p) = \partial y^j/\partial x^k(p)$ (Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]]),
>
> $$
> \delta^i_k = dx^i\big|_p\Big(\frac{\partial}{\partial x^k}\Big|_p\Big) = \sum_j \frac{\partial x^i}{\partial y^j}(p)\, dy^j\big|_p\Big(\frac{\partial}{\partial x^k}\Big|_p\Big) = \sum_j \frac{\partial x^i}{\partial y^j}(p)\, \frac{\partial y^j}{\partial x^k}(p) = (BA)_{ik} .
> $$
>
> So $BA = I$; for square matrices a left inverse is the inverse (an $m \times m$ matrix $A$ with $BA = I$ is injective, hence invertible by Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1), and then $B = B A A^{-1} = A^{-1}$). By Proposition [[§48 The Tangent Bundle#^prop-48-2|§48.2]] the tangent components transform by $A$, $w = Av$; and the formula for $\eta_j$ reads $\eta_j = \sum_i B_{ij}\, \xi_i = (B^{\mathsf T} \xi)_j$, so the covector components transform by $B^{\mathsf T} = (A^{-1})^{\mathsf T}$.
>
> *The transition map.* Explicitly, let $(r, \xi) \in \hat\varphi(T^{\ast}U \cap T^{\ast}V) = \varphi(U \cap V) \times \mathbb{R}^m$ (an open set, by the same argument as for $TM$ in the proof of Proposition [[§48 The Tangent Bundle#^prop-48-2|§48.2]], with Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] giving the basis $dx^i|_p$) and $p = \varphi^{-1}(r)$. By the inverse formula of Definition [[§49 The Cotangent Bundle#^def-49-5|§49.5]], $\hat\varphi^{-1}(r, \xi) = \big(p, \sum_i \xi_i\, dx^i|_p\big)$, and by the same definition for $\psi$ and the formula for $\eta$, $\hat\psi$ sends this point to $(\psi(p), \eta) = (\tau(r), B^{\mathsf T}\xi)$. With $p = \varphi^{-1}(r)$, the matrix $A = \big[\partial y^i/\partial x^j(p)\big]$ is $\tau'(r)$ (Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], applied to $F = \mathrm{id}_M$ exactly as in the proof of Proposition [[§48 The Tangent Bundle#^prop-48-2|§48.2]]), so $B = \big[\partial x^i/\partial y^j(p)\big] = \tau'(r)^{-1}$ and $\eta = \big(\tau'(r)^{-1}\big)^{\mathsf T}\xi$, which is the displayed transition map.
>
> *Smoothness and the atlas.* Its entries are smooth in $r$: those of $\tau'(r)$ are, since $\tau$ is smooth (the charts of $M$ are compatible); $\det \tau'(r) \ne 0$ because $\tau'(r)$ is invertible; and the inverse of an invertible matrix is given by Cramer's rule, each entry a polynomial in the entries (a cofactor) divided by the nonzero determinant, hence smooth in $r$. So the first $m$ components $\tau^i(r)$ and the last $m$ components $\sum_i \big(\tau'(r)^{-1}\big)_{ij}\, \xi_i$ of the transition map are smooth in $(r, \xi)$, and the transition maps are smooth, as in Proposition [[§48 The Tangent Bundle#^prop-48-2|§48.2]]. The inverse transition map $\hat\varphi \circ \hat\psi^{-1}$ is the same formula with the two charts exchanged (rename $(U, \varphi, x^i) \leftrightarrow (V, \psi, y^j)$), hence smooth too, so each transition map is a diffeomorphism (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]). The charts $\hat\varphi$ are homeomorphisms of the open sets $T^{\ast}U$ onto open subsets of $\mathbb{R}^{2m}$ (Proposition [[§49 The Cotangent Bundle#^prop-49-1|§49.1]]), and the $T^{\ast}U$ cover $T^{\ast}M$; so they form a smooth atlas (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]). The fibration and linearity statements follow as in Corollary [[§48 The Tangent Bundle#^cor-48-3|§48.3]]; they are written out in the next corollary.

^pf-49-2

*Uses:* [[§49 The Cotangent Bundle#^def-49-5|Def. §49.5]], [[§32 The Cotangent Space#^def-32-4|Def. §32.4]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§30 The Differential in Coordinates#^cor-30-3|§30.3]], [[§48 The Tangent Bundle#^prop-48-2|§48.2]], [[§48 The Tangent Bundle#^cor-48-3|§48.3]], [[Multivariable Chain Rule|452 §12.2]], [[§12 Duality#^ladr-3-132|LADR 3.132]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§49 The Cotangent Bundle#^prop-49-1|§49.1]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]]

> [!remark]- Connections
> - The matrix of a dual map in dual bases is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].
> - The rule for $dx^i$ is the substitution step of the pullback in 452, [[§37 The Algebra of Differential Forms#^def-37-3|452 Def. §37.3]], applied to the transition map.

> [!theorem] Corollary §49.3: The Cotangent Bundle Is a Fibration
> With the smooth structure of [[§49 The Cotangent Bundle#^prop-49-2|Proposition §49.2]]:
> 1. $T^{\ast}M$ is a smooth manifold of dimension $2m$, and $\pi : T^{\ast}M \to M$ is smooth;
> 2. the $\Psi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Psi$ restricts on the fibre $T_p^{\ast}M$ to a linear isomorphism $T_p^{\ast}M \to \{p\} \times \mathbb{R}^m$; so $T^{\ast}M$ is a vector bundle;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $T^{\ast}M$ of codimension $m$.
>
> *Lee: Proposition 11.9*

^cor-49-3

> [!proof]+ Proof
> *(Not from lecture; filled in, as Corollary [[§48 The Tangent Bundle#^cor-48-3|§48.3]].)*
>
> *(1)* By Propositions [[§49 The Cotangent Bundle#^prop-49-1|§49.1]] and [[§49 The Cotangent Bundle#^prop-49-2|§49.2]], $T^{\ast}M$ is a topological manifold of dimension $2m$ with a smooth atlas, hence a smooth manifold of dimension $2m$. To see that $\pi$ is smooth, check Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]. *Continuity:* on each open set $T^{\ast}U$, $\pi = \varphi^{-1} \circ \mathrm{pr}_1 \circ \hat\varphi$ (Definitions [[§49 The Cotangent Bundle#^def-49-2|§49.2]] and [[§49 The Cotangent Bundle#^def-49-5|§49.5]]), a composite of continuous maps, and the $T^{\ast}U$ cover $T^{\ast}M$. *Coordinate representation:* for $(p, \xi) \in T^{\ast}M$ take a chart $(U, \varphi)$ at $p$; then $(T^{\ast}U, \hat\varphi)$ is a chart at $(p, \xi)$ with $\pi(T^{\ast}U) \subseteq U$, and, as $\hat\varphi^{-1}(r, \xi) = \big(\varphi^{-1}(r), \sum_i \xi_i\, dx^i|_{\varphi^{-1}(r)}\big)$,
>
> $$
> \varphi \circ \pi \circ \hat\varphi^{-1}(r, \xi) = \varphi\big(\varphi^{-1}(r)\big) = r .
> $$
>
> So in the charts $\hat\varphi$ and $\varphi$, $\pi$ is $(r, \xi) \mapsto r$, which is smooth.
>
> *(2)* By Definition [[§38 Fibrations#^def-38-1|§38.1]], take the open cover of $M$ by chart domains $U$ and the maps $\Psi$ of Definition [[§49 The Cotangent Bundle#^def-49-4|§49.4]]. Since $\hat\varphi = (\varphi \times \mathrm{id}) \circ \Psi$ (Definition [[§49 The Cotangent Bundle#^def-49-5|§49.5]]),
>
> $$
> \Psi = (\varphi^{-1} \times \mathrm{id}) \circ \hat\varphi ,
> $$
>
> a composite of diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]: $\hat\varphi$ is a chart of $T^{\ast}U$, and $\varphi^{-1} \times \mathrm{id}$ is the inverse of the product chart $\varphi \times \mathrm{id}$ of $U \times \mathbb{R}^m$), hence a diffeomorphism (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], applied to the composite and to its inverse). For $(p, \xi) \in T^{\ast}U$, $\mathrm{pr}_1(\Psi(p, \xi)) = \mathrm{pr}_1(p, \xi_1, \ldots, \xi_m) = p = \pi(p, \xi)$, so $\mathrm{pr}_1 \circ \Psi = \pi$; the $T^{\ast}U$ cover $T^{\ast}M$ and the $U$ cover $M$. So $\pi$ is a fibration with fibre $\mathbb{R}^m$.
>
> *Linearity on fibres.* Fix $p \in U$. On $T_p^{\ast}M$, $\Psi$ is $\xi \mapsto (p, \xi_1, \ldots, \xi_m)$ with $\xi_i = \xi(\partial/\partial x^i|_p)$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]), taking components in a basis. Each $\xi \mapsto \xi(\partial/\partial x^i|_p)$ is linear, since covectors are added and scaled pointwise (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]): $(a\xi + b\zeta)(\partial/\partial x^i|_p) = a\,\xi(\partial/\partial x^i|_p) + b\,\zeta(\partial/\partial x^i|_p)$. It is bijective onto $\mathbb{R}^m$ because the $dx^i|_p$ form a basis of $T_p^{\ast}M$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]): the components of $\xi$ exist and are unique, and every list $(b_1, \ldots, b_m)$ is the list of components of $\sum_i b_i\, dx^i|_p$. So $\Psi$ restricts to a linear isomorphism $T_p^{\ast}M \to \{p\} \times \mathbb{R}^m$. The fibres are vector spaces and the trivializations are fibrewise linear isomorphisms — the two features of a vector bundle (Remark [[§48 The Tangent Bundle#^rem-48-2|remark]]); so $T^{\ast}M$ is a vector bundle.
>
> *(3)* A point of $\zeta(M)$ is $\zeta(p) = (p, 0)$; take a chart $(U, \varphi)$ at $p$, so $(p, 0) \in T^{\ast}U$, and $\zeta(M) \cap T^{\ast}U = \{(q, 0) : q \in U\}$. For $(q, \xi) \in T^{\ast}U$, the last $m$ coordinates of $\hat\varphi(q, \xi)$ are the components $\xi_i$, and $\xi = \sum_i \xi_i\, dx^i|_q$, so $\xi = 0$ exactly when $\xi_1 = \cdots = \xi_m = 0$. Hence, in the chart $\hat\varphi$,
>
> $$
> \zeta(M) \cap T^{\ast}U = \{\, (q, \xi) \in T^{\ast}U : \xi_1 = \cdots = \xi_m = 0 \,\},
> $$
>
> so the charts $\hat\varphi$ are adapted to $\zeta(M)$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), and $\zeta(M)$ is a submanifold of codimension $m$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]], with $2m$ coordinates and $k = m$).

^pf-49-3

*Uses:* [[§49 The Cotangent Bundle#^prop-49-1|§49.1]], [[§49 The Cotangent Bundle#^prop-49-2|§49.2]], [[§49 The Cotangent Bundle#^def-49-4|Def. §49.4]], [[§49 The Cotangent Bundle#^def-49-5|Def. §49.5]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§48 The Tangent Bundle#^cor-48-3|§48.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§49 The Cotangent Bundle#^def-49-2|Def. §49.2]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§21 Linear Algebra Toolkit#^def-21-1|Def. §21.1]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§48 The Tangent Bundle#^rem-48-2|§48.2]]

## Lecture 15 and the Standard Coordinates

*Lecture 15 returned to the cotangent bundle — “we did define it, but it was all very quick” — because the homework uses it: “the standard coordinates on $T^{\ast}M$, which are also trivializations”, with the components found by evaluating on the dual basis, as in [[§49 The Cotangent Bundle#^def-49-4|Definitions §49.4]] and [[§49 The Cotangent Bundle#^def-49-5|§49.5]]. He also recalled that the cotangent space has a description from germs, $T_p^{\ast}M \cong I_p/I_p^2$ ([[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4]]): “the cotangent space is, in a way, very extremely natural from the point of view of functions.”*

**Transcription note.** Page 40 of the handwritten notes writes the standard coordinates as a map on $T^{\ast}M$; they are defined on $T^{\ast}U$, the part of the bundle over the chart domain, as Uribe corrected in lecture.

“We'll see that the cotangent bundle has a natural structure that the tangent bundle doesn't have.” $TM$ and $T^*M$ are isomorphic as vector bundles, “but not naturally isomorphic — we have to make choices to construct an isomorphism” (a metric, for instance, as in the [[§37 Regular Submanifolds#^rem-37-1|remark on conormal spaces]]). This is stated, not proved, here.
