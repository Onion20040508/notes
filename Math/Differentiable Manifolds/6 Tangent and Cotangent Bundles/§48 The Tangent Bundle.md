---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 48
tags: [differentiable-manifolds, math591]
---
← [[§47 Recap꞉ Covectors and the Four Differentials]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§49 The Cotangent Bundle]] →

*Stage: bundles — All the tangent spaces of $M$, assembled into a single manifold that fibres over $M$.*

*Lecture 12. “Again, these constructions, especially the cotangent [bundle], are basic parts of the basic theory.” The tangent bundle was introduced as a set, with its projection and zero section; its topology, smooth structure and charts come next lecture.*

> [!definition] Definition §48.1: The Tangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **tangent bundle** is the set
>
> $$
> TM = \bigcup_{p \in M} \{p\} \times T_pM = \{\, (p, v) : p \in M,\ v \in T_pM \,\},
> $$
>
> all the tangent spaces “put together in one big set.”
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-48-1

> [!definition] Definition §48.2: The Projection of $TM$
> The **projection** of the tangent bundle is
>
> $$
> \pi : TM \longrightarrow M, \qquad \pi(p, v) = p .
> $$
>
> Its fibre over $p$, $\pi^{-1}(p) = \{p\} \times T_pM$, is identified with $T_pM$.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-48-2

> [!definition] Definition §48.3: The Zero Section of $TM$
> The **zero section** of the tangent bundle is
>
> $$
> \zeta : M \longrightarrow TM, \qquad \zeta(p) = (p, 0) .
> $$
>
> It is one-to-one because every tangent space has a distinguished element, its zero.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-48-3

> [!remark] Remark: The Picture Changes
> “There are several psychological inflection steps that one needs to make. The most important one is that we're going to think of $TM$ as fibering over $M$.” A tangent space is usually drawn touching $M$, lying along it. In the bundle picture it stands *vertically*, as the fibre over its point, and $M$ itself sits horizontally inside $TM$ as the zero section — the tangent spaces become “transversal” to it.

^rem-48-1

![[m591-17-1.svg]]
*The tangent bundle as a fibration. Each fibre $\pi^{-1}(p) = T_pM$ is a vertical line over $p$ (in general a copy of $\mathbb{R}^m$); the point $(p, v)$ lies on it, and the zero section $\zeta$ lifts each $p$ straight up to $(p, 0)$, placing a copy of $M$ horizontally inside $TM$.*

![[m591-17-6.svg]]
*$TS^1$ as a cylinder. Left: the usual picture, each tangent line touching the circle at its point. Right: the bundle picture of the remark — each tangent line $T_pS^1$ (red) stands upright over $p$, and the zero section $\zeta(S^1)$ (blue) runs around the waist. Here the bundle is a genuine product $S^1 \times \mathbb{R}$: two angle charts ([[§24 The Circle#^prop-24-1|§24.1]]) differ by a constant on each piece of their overlap, so their coordinate vectors $\partial/\partial\theta$ agree, and $c\,\partial/\partial\theta|_p \mapsto (p, c)$ is a global trivialization. The green circle is the vector field $\partial/\partial\theta$ ([[§51 Vector Fields#^def-51-1|Definition §51.1]]), a section that never meets the zero section.*

*Status.* [[§48 The Tangent Bundle#^prop-48-4|Proposition §48.4]], below, was stated in Lecture 12 — “the claim, which takes a lot of detail to prove” — and made precise in Lecture 13 ([[§48 The Tangent Bundle#Trivializations and Charts|Trivializations and Charts]]), which wrote down the charts. Their idea was given: a chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ gives the basis $\partial/\partial x^i|_p$ of every $T_pM$, $p \in U$, hence an identification of each of these tangent spaces with $\mathbb{R}^m$; “putting all that together gives us a map” $\pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}$, the chart of $TM$. The dimension $2m$ is $m$ coordinates for the point and $m$ for the vector.

## Trivializations and Charts

*Lecture 13. “Back to the tangent bundle.” $TM$ has been defined as a set; its charts come from charts of $M$ and the coordinate bases.*

> [!definition] Definition §48.4: Local Trivializations of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $TU = \pi^{-1}(U) = \{(p, v) \in TM : p \in U\}$, the tangent vectors at points of $U$. The **local trivialization** over $U$ is
>
> $$
> \Phi : TU \longrightarrow U \times \mathbb{R}^m, \qquad \Phi(p, v) = (p, v^1, \ldots, v^m), \qquad \text{where } v = \sum_{i=1}^m v^i \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> the components of $v$ in the coordinate basis ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]). It is a bijection, and $\mathrm{pr}_1 \circ \Phi = \pi$ — “that's why I call it a trivialization.”
>
> *Lee: Proposition 3.18*

^def-48-4

> [!definition] Definition §48.5: Charts of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $\Phi$ the local trivialization over $U$ ([[§48 The Tangent Bundle#^def-48-4|Definition §48.4]]). The **chart** of $TM$ over $U$ is
>
> $$
> \tilde\varphi = (\varphi \times \mathrm{id}) \circ \Phi : TU \longrightarrow \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m},
> $$
>
> which acts in two steps:
>
> $$
> (p, v) \;\overset{\Phi}{\longmapsto}\; (p,\, v^1, \ldots, v^m) \;\overset{\varphi \times \mathrm{id}}{\longmapsto}\; \big(x^1(p), \ldots, x^m(p),\, v^1, \ldots, v^m\big),
> $$
>
> where $v^1, \ldots, v^m$ are the components of $v$ in the coordinate basis at $p$,
>
> $$
> v = \sum_{i=1}^m v^i \frac{\partial}{\partial x^i}\Big|_p, \qquad v^i = v[x^i]
> $$
>
> (the universal formula, [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]). So the first $m$ coordinates of $\tilde\varphi(p, v)$ locate the point $p$, and the last $m$ list the components of the vector $v$. $\tilde\varphi$ is a bijection, with inverse
>
> $$
> (r, a^1, \ldots, a^m) \longmapsto \Big(\varphi^{-1}(r),\ \sum_{i=1}^m a^i\, \frac{\partial}{\partial x^i}\Big|_{\varphi^{-1}(r)}\Big), \qquad r \in \varphi(U),\ (a^1, \ldots, a^m) \in \mathbb{R}^m .
> $$
>
> *Lee: Proposition 3.18*

^def-48-5

![[m591-17-2.svg]]
*The trivialization and the chart, as on the board. The triangle commutes, $\mathrm{pr}_1 \circ \Phi = \pi$ — the fibration diagram of [[§38 Fibrations#^def-38-1|Definition §38.1]] — and the chart $\tilde\varphi$ is $\Phi$ followed by $\varphi$ on the first factor.*

> [!theorem] Proposition §48.1: The Topology of $TM$
> There is a unique topology on $TM$ for which every $TU$ is open and every chart $\tilde\varphi : TU \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $TM$ is a topological manifold of dimension $2m$.
>
> *Lee: Lemma 1.35 and Proposition 3.18*

^prop-48-1

> [!proof]+ Proof
> *(Stated in Lecture 13 without proof — “it's all point-set topology, and of course everything is in Lee \ldots see Lee”; filled in, following Lee's smooth manifold chart lemma.)* Throughout, $(U, \varphi)$ and $(V, \psi)$ denote smooth charts of $M$. Three things have to be shown: a topology on $TM$ with the two stated properties exists; it is the only one; and with it $TM$ is second countable, Hausdorff and locally Euclidean of dimension $2m$, that is, a topological manifold of dimension $2m$ (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]).
>
> *Two set-theoretic facts.* First, a point $(p, v)$ lies in $TU \cap TV$ exactly when $p \in U$ and $p \in V$, so $TU \cap TV = \pi^{-1}(U \cap V)$. Second, by Definition [[§48 The Tangent Bundle#^def-48-5|§48.5]], $\tilde\varphi(p, v) = (\varphi(p), v^1, \ldots, v^m)$, and for each $p \in U \cap V$ every $(a^1, \ldots, a^m) \in \mathbb{R}^m$ occurs as the list of components of some $v \in T_pM$, namely of $v = \sum_i a^i\, \partial/\partial x^i|_p$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). Hence
>
> $$
> \tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m ,
> $$
>
> and this set is open in $\mathbb{R}^{2m}$: $\varphi(U \cap V)$ is open in $\mathbb{R}^m$ (Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]]), and a product of open sets is open. Taking $V = U$ gives $\tilde\varphi(TU) = \varphi(U) \times \mathbb{R}^m$, also open.
>
> *The transition maps.* The computation in the proof of Proposition [[§48 The Tangent Bundle#^prop-48-2|§48.2]] below uses only the definitions of the charts, not any topology on $TM$. It shows that $\tilde\psi \circ \tilde\varphi^{-1}$ maps the open set $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$ bijectively onto the open set $\psi(U \cap V) \times \mathbb{R}^m$, by a smooth map whose inverse, $\tilde\varphi \circ \tilde\psi^{-1}$, is given by the same formula with the two charts exchanged. Both maps are smooth, hence continuous, and they are inverse to each other because $\tilde\varphi$ and $\tilde\psi$ are bijections on $TU \cap TV$. So each transition map is a homeomorphism between open subsets of $\mathbb{R}^{2m}$.
>
> *The topology.* Declare $W \subseteq TM$ open if $\tilde\varphi(W \cap TU)$ is open in $\mathbb{R}^{2m}$ for every chart $(U, \varphi)$, and call the collection of these sets $\tau$. It is a topology; the three axioms are checked chart by chart.
> - $\emptyset \in \tau$, since $\tilde\varphi(\emptyset) = \emptyset$; and $TM \in \tau$, since $\tilde\varphi(TM \cap TU) = \tilde\varphi(TU) = \varphi(U) \times \mathbb{R}^m$ is open.
> - For any family $W_\alpha \in \tau$, images under any map commute with unions, so $\tilde\varphi\big((\bigcup_\alpha W_\alpha) \cap TU\big) = \bigcup_\alpha \tilde\varphi(W_\alpha \cap TU)$, a union of open sets.
> - For $W_1, W_2 \in \tau$, an injective map carries intersections to intersections, and $\tilde\varphi$ is injective on $TU$, so $\tilde\varphi(W_1 \cap W_2 \cap TU) = \tilde\varphi(W_1 \cap TU) \cap \tilde\varphi(W_2 \cap TU)$, an intersection of two open sets.
>
> *Each $TU$ is open.* For any chart $(V, \psi)$, the second set-theoretic fact with the roles of the charts exchanged gives $\tilde\psi(TU \cap TV) = \psi(U \cap V) \times \mathbb{R}^m$, which is open. So $TU \in \tau$.
>
> *Each $\tilde\varphi$ is a homeomorphism onto the open set $\varphi(U) \times \mathbb{R}^m$.* Give $TU$ the subspace topology. By Definition [[§48 The Tangent Bundle#^def-48-5|§48.5]], $\tilde\varphi : TU \to \varphi(U) \times \mathbb{R}^m$ is a bijection; it remains to show that it is open and continuous.
>
> *Open:* if $W \subseteq TU$ is open in $TU$, then $W$ is open in $TM$, because $TU$ is open (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]); so, by the definition of $\tau$ applied with the chart $(U, \varphi)$, $\tilde\varphi(W) = \tilde\varphi(W \cap TU)$ is open.
>
> *Continuous:* let $O \subseteq \varphi(U) \times \mathbb{R}^m$ be open and $W = \tilde\varphi^{-1}(O) \subseteq TU$. For any chart $(V, \psi)$, the set $W \cap TV$ consists of the points of $TU \cap TV$ whose image under $\tilde\varphi$ lies in $O$, so $\tilde\varphi(W \cap TV) = O \cap \tilde\varphi(TU \cap TV) = O \cap \big(\varphi(U \cap V) \times \mathbb{R}^m\big)$, and therefore
>
> $$
> \tilde\psi(W \cap TV) = \big(\tilde\psi \circ \tilde\varphi^{-1}\big)\Big(O \cap \big(\varphi(U \cap V) \times \mathbb{R}^m\big)\Big).
> $$
>
> The set in parentheses is open (an intersection of two open sets) and lies in the domain of the transition map; a homeomorphism carries it to a set open in the target $\psi(U \cap V) \times \mathbb{R}^m$, which is open in $\mathbb{R}^{2m}$, so the image is open in $\mathbb{R}^{2m}$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). This holds for every chart, so $W \in \tau$; as $W \subseteq TU$, it is open in $TU$. A continuous open bijection is a homeomorphism.
>
> *Uniqueness.* Let $\tau'$ be any topology in which every $TU$ is open and every $\tilde\varphi$ is a homeomorphism; we show $\tau' = \tau$. If $W \in \tau'$, then for each chart $W \cap TU$ is open in $TU$ (subspace topology of $\tau'$), so its image $\tilde\varphi(W \cap TU)$ under the homeomorphism $\tilde\varphi$ is open in $\varphi(U) \times \mathbb{R}^m$, hence in $\mathbb{R}^{2m}$; so $W \in \tau$. Conversely, let $W \in \tau$. For each chart, $\tilde\varphi(W \cap TU)$ is open, so $W \cap TU = \tilde\varphi^{-1}\big(\tilde\varphi(W \cap TU)\big)$ is open in $TU$ for $\tau'$, by continuity of $\tilde\varphi$; it is then open in $TM$ for $\tau'$, since $TU \in \tau'$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). Every point $(p, v)$ of $TM$ lies in $TU$ for any chart $(U, \varphi)$ at $p$, so $W = \bigcup_U (W \cap TU)$, a union of members of $\tau'$; hence $W \in \tau'$.
>
> *Locally Euclidean.* Let $(p, v) \in TM$ and choose a chart $(U, \varphi)$ of $M$ at $p$. Then $(p, v) \in TU$, which is open, and $\tilde\varphi$ is a homeomorphism of $TU$ onto the open subset $\varphi(U) \times \mathbb{R}^m$ of $\mathbb{R}^{2m}$. This is Definition [[§2 Topological Manifolds#^def-2-1|§2.1]] with $n = 2m$.
>
> *Hausdorff.* Let $(p, v) \ne (q, w)$; we need disjoint open sets containing them (Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]]). *Case $p = q$*, so $v \ne w$. Both points lie in $TU$ for a chart $(U, \varphi)$ at $p$, and their images under the injective map $\tilde\varphi$ are distinct points of the Hausdorff space $\mathbb{R}^{2m}$, so they have disjoint open neighbourhoods $O_1$, $O_2$. The sets $\tilde\varphi^{-1}(O_1 \cap \tilde\varphi(TU))$ and $\tilde\varphi^{-1}(O_2 \cap \tilde\varphi(TU))$ are disjoint, contain $(p, v)$ and $(p, w)$ respectively, and are open in $TU$ by continuity of $\tilde\varphi$, hence open in $TM$ because $TU$ is (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). *Case $p \ne q$.* $M$ is Hausdorff, so there are disjoint open sets $U_0 \ni p$ and $V_0 \ni q$. Take charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $q$ and shrink their domains to $U \cap U_0$ and $V \cap V_0$; the restrictions are still smooth charts (shrink the domains, Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1); their transition maps are restrictions of those of $\varphi$ and $\psi$ to open subsets). Now $T(U \cap U_0)$ and $T(V \cap V_0)$ are open, contain $(p, v)$ and $(q, w)$, and are disjoint: a common point $(x, u)$ would have $x \in U_0 \cap V_0 = \emptyset$.
>
> *Second countable.* Let $\mathcal{B}$ be a countable basis of $M$ (Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]). For each $B \in \mathcal{B}$ contained in some chart domain, choose one such chart $(U_B, \varphi_B)$, so $B \subseteq U_B$. These countably many charts cover $M$: each $p$ lies in some chart domain $U$, and then, by Definition [[§1 Point-Set Topology Review#^def-1-1|§1.1]], in some $B \in \mathcal{B}$ with $p \in B \subseteq U$; this $B$ is contained in a chart domain, so $(U_B, \varphi_B)$ was chosen, and $p \in B \subseteq U_B$. So the countably many open sets $TU_B$ cover $TM$. Each $TU_B$ is homeomorphic to an open subset of $\mathbb{R}^{2m}$, which has a countable basis (for instance the balls with rational centres and rational radii contained in it), so $TU_B$ has a countable basis $\mathcal{C}_B$, whose members are open in $TU_B$ and hence in $TM$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). The union $\mathcal{C} = \bigcup_B \mathcal{C}_B$ is a countable union of countable sets, so countable. It is a basis of $TM$: if $W$ is open in $TM$ and $(p, v) \in W$, choose $B$ with $(p, v) \in TU_B$; then $W \cap TU_B$ is open in $TU_B$ and contains $(p, v)$, so some $C \in \mathcal{C}_B$ has $(p, v) \in C \subseteq W \cap TU_B \subseteq W$.

^pf-48-1

*Uses:* [[§48 The Tangent Bundle#^def-48-4|Def. §48.4]], [[§48 The Tangent Bundle#^prop-48-2|§48.2]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§2 Basis for a Topology#^def-2-1|590 Def. §2.1]], [[§9 Hausdorff Spaces#^def-9-1|590 Def. §9.1]], [[§22 Countability Axioms#^def-22-3|590 Def. §22.3]], [[§48 The Tangent Bundle#^def-48-5|Def. §48.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§2 Topological Manifolds#^prop-2-11|§2.11]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

The same argument, word for word, builds the topology of the cotangent bundle ([[§49 The Cotangent Bundle|§49]]), with the dual bases in place of the coordinate bases.

> [!theorem] Proposition §48.2: The Smooth Atlas of $TM$
> The charts $(TU, \tilde\varphi)$, as $(U, \varphi)$ ranges over the smooth charts of $M$, form a smooth atlas on $TM$. For charts $\varphi = (x^i)$ and $\psi = (y^j)$ of $M$, the transition map is
>
> $$
> \tilde\psi \circ \tilde\varphi^{-1}(r, v) = \Big( \psi \circ \varphi^{-1}(r), \ \ \sum_{j=1}^m \frac{\partial y^1}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j, \ \ldots, \ \sum_{j=1}^m \frac{\partial y^m}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j \Big) .
> $$
>
> *Lee: Proposition 3.18*

^prop-48-2

> [!proof]+ Proof
> *(Lecture 13: “the only thing that I want to have a look at is \ldots the transition functions of the atlas, because this is how people handle tangent vectors.” Completed here.)* By Definition [[§17 Differentiable Structures#^def-17-6|§17.6]], three things have to be shown: each $(TU, \tilde\varphi)$ is a chart of the topological manifold $TM$; their domains cover $TM$; and any two of them are $C^\infty$-compatible, that is (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), each transition map $\tilde\psi \circ \tilde\varphi^{-1}$ is a diffeomorphism between open subsets of $\mathbb{R}^{2m}$. Along the way the formula for the transition map is derived.
>
> *Charts that cover.* By Proposition [[§48 The Tangent Bundle#^prop-48-1|§48.1]], each $TU$ is open and $\tilde\varphi$ is a homeomorphism of $TU$ onto the open set $\varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}$, so $(TU, \tilde\varphi)$ is a chart. Every $(p, v) \in TM$ lies in $TU$ for any chart $(U, \varphi)$ of $M$ at $p$, so the domains cover $TM$.
>
> *The domain of the transition map.* A point $(p, v)$ lies in $TU \cap TV$ exactly when $p \in U \cap V$; for such $p$ every list of components $(v^1, \ldots, v^m) \in \mathbb{R}^m$ occurs (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). So the domain is $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$, open in $\mathbb{R}^{2m}$ since $\varphi(U \cap V)$ is open (Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]]); likewise the target is $\psi(U \cap V) \times \mathbb{R}^m$.
>
> *The formula.* Let $(r, v) = (r, v^1, \ldots, v^m)$ be a point of the domain and $p = \varphi^{-1}(r) \in U \cap V$. By the inverse formula of Definition [[§48 The Tangent Bundle#^def-48-5|§48.5]], $\tilde\varphi^{-1}(r, v) = (p, u)$ with $u \in T_pM$ the tangent vector whose components in the basis $\partial/\partial x^j|_p$ are the $v^j$. Write $u$ in both bases (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]):
>
> $$
> u = \sum_j v^j \frac{\partial}{\partial x^j}\Big|_p = \sum_i w^i \frac{\partial}{\partial y^i}\Big|_p .
> $$
>
> By Definition [[§48 The Tangent Bundle#^def-48-5|§48.5]] for the chart $\psi$, $\tilde\psi(p, u) = \big(\psi(p), w^1, \ldots, w^m\big)$, and $\psi(p) = \psi \circ \varphi^{-1}(r)$; so the first component of the transition is $\psi \circ \varphi^{-1}$, smooth because the charts of $M$ are compatible. For the rest we need the $w$'s in terms of the $v$'s: “a change of basis formula from 217, which I always forget.” By the universal formula (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]) in the chart $\psi$, the $i$-th coefficient of a derivation $D$ in the basis $\partial/\partial y^i|_p$ is $D[y^i]$. Applied to $D = \partial/\partial x^j|_p$, whose value on $y^i$ is $\partial y^i/\partial x^j(p)$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]), it gives the change of basis formula
>
> $$
> \frac{\partial}{\partial x^j}\Big|_p = \sum_i \frac{\partial y^i}{\partial x^j}(p) \frac{\partial}{\partial y^i}\Big|_p .
> $$
>
> Substitute this into the first expression for $u$ and collect terms, using that derivations are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]):
>
> $$
> u = \sum_j v^j \sum_i \frac{\partial y^i}{\partial x^j}(p) \frac{\partial}{\partial y^i}\Big|_p = \sum_i \Big( \sum_j \frac{\partial y^i}{\partial x^j}(p)\, v^j \Big) \frac{\partial}{\partial y^i}\Big|_p .
> $$
>
> The coefficients of $u$ in the basis $\partial/\partial y^i|_p$ are unique, so comparing with $u = \sum_i w^i\, \partial/\partial y^i|_p$,
>
> $$
> w^i = \sum_j \frac{\partial y^i}{\partial x^j}(p)\, v^j .
> $$
>
> (In lecture Uribe expanded $\partial/\partial y^j$ in the other basis and first solved for the $v$'s — “I did it backwards” — then took the other direction “by the same argument”.) With $p = \varphi^{-1}(r)$ this is the displayed formula.
>
> *Smoothness.* The coefficients are smooth functions of $r$. Apply Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]] to $F = \mathrm{id}_M$, with the chart $(U \cap V, \varphi|_{U \cap V})$ on the source and $(V, \psi)$ on the target (so $F(U \cap V) \subseteq V$): then $F^i = y^i$ and the coordinate representation is $\tau = \psi \circ \varphi^{-1}$ on $\varphi(U \cap V)$, and it gives
>
> $$
> \frac{\partial y^i}{\partial x^j}\big(\varphi^{-1}(r)\big) = \frac{\partial \tau^i}{\partial r^j}(r) ,
> $$
>
> the entries of the Jacobian $\tau'(r)$ of the transition map of $M$. (Restricting the chart to $U \cap V$ does not change partial derivatives at points of $U \cap V$: the coordinate representation of a function only gets restricted to an open set around $\varphi(p)$.) So the transition map of $TM$ is
>
> $$
> (r, v) \longmapsto \big(\tau(r),\ \tau'(r)\, v\big), \qquad \tau = \psi \circ \varphi^{-1} .
> $$
>
> Its first $m$ components $\tau^i(r)$ are smooth because $\tau$ is; its last $m$ components $\sum_j \partial\tau^i/\partial r^j(r)\, v^j$ are sums of products of the smooth functions $\partial\tau^i/\partial r^j(r)$ with the coordinate functions $v^j$, hence smooth in $(r, v)$. A map into $\mathbb{R}^{2m}$ is smooth if all its components are, so $\tilde\psi \circ \tilde\varphi^{-1}$ is smooth.
>
> *Compatibility.* The inverse of $\tilde\psi \circ \tilde\varphi^{-1}$ is $\tilde\varphi \circ \tilde\psi^{-1}$, and the computation above with the names exchanged — $(U, \varphi, x^i)$ and $(V, \psi, y^i)$ swapped — shows that it is $(s, w) \mapsto \big(\varphi \circ \psi^{-1}(s), (\varphi \circ \psi^{-1})'(s)\, w\big)$, smooth. So every transition map is a smooth bijection with smooth inverse, a diffeomorphism (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]), and the charts $(TU, \tilde\varphi)$ form a smooth atlas.

^pf-48-2

*Uses:* [[§48 The Tangent Bundle#^def-48-4|Def. §48.4]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]], [[§48 The Tangent Bundle#^prop-48-1|§48.1]], [[§2 Topological Manifolds#^prop-2-11|§2.11]], [[§48 The Tangent Bundle#^def-48-5|Def. §48.5]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]]

![[m591-17-3.svg]]
*The transition map of the charts $\tilde\varphi$ and $\tilde\psi$ of $TM$, as drawn in lecture over a point $(p, v)$ of $TU \cap TV$.*

> [!remark]- Connections
> - The same expansion of coordinate derivations: [[§30 The Differential in Coordinates#^cor-30-4|Change of Coordinates, §30.4]]; the Jacobian matrix in 452: [[§16 The Inverse Function Theorem#^def-16-1|452 Def. §16.1]]; change of basis: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].

The transition map of $TM$, in one line: the base point moves by the transition map of $M$, and the vector by its Jacobian. This is Uribe's identity at work once more — the partials $\partial y^i/\partial x^j$, taken upstairs on $M$, are the Jacobian downstairs.

> [!theorem] Corollary §48.3: The Tangent Bundle Is a Fibration
> With the smooth structure of [[§48 The Tangent Bundle#^prop-48-2|Proposition §48.2]]:
> 1. $TM$ is a smooth manifold of dimension $2m$, and $\pi : TM \to M$ is smooth;
> 2. the $\Phi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Phi$ restricts on the fibre $T_pM$ to a linear isomorphism $T_pM \to \{p\} \times \mathbb{R}^m$;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $TM$ of codimension $m$.
>
> With [[§48 The Tangent Bundle#^prop-48-1|Proposition §48.1]], this proves [[§48 The Tangent Bundle#^prop-48-4|Proposition §48.4]] below in full.

^cor-48-3

> [!proof]+ Proof
> *((1) and (2) are the lecture's observations — “in these coordinates, the projection is just projection onto the first $m$ components \ldots so we get a beautiful fibration”; the details and (3) are filled in.)*
>
> *(1)* By Proposition [[§48 The Tangent Bundle#^prop-48-1|§48.1]], $TM$ is a topological manifold of dimension $2m$, and by Proposition [[§48 The Tangent Bundle#^prop-48-2|§48.2]] the charts $(TU, \tilde\varphi)$ form a smooth atlas on it; so $TM$ is a smooth manifold of dimension $2m$, with the smooth structure determined by this atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). To see that $\pi$ is smooth, check Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]. *Continuity:* on each open set $TU$, by Definitions [[§48 The Tangent Bundle#^def-48-2|§48.2]] and [[§48 The Tangent Bundle#^def-48-5|§48.5]], $\pi = \varphi^{-1} \circ \mathrm{pr}_1 \circ \tilde\varphi$ with $\mathrm{pr}_1(r, v) = r$, a composite of continuous maps; the open sets $TU$ cover $TM$, so $\pi$ is continuous. *Coordinate representation:* for $(p, v) \in TM$ take a chart $(U, \varphi)$ of $M$ at $p$; then $(TU, \tilde\varphi)$ is a chart at $(p, v)$ with $\pi(TU) \subseteq U$, and for $(r, v) \in \varphi(U) \times \mathbb{R}^m$, with $\tilde\varphi^{-1}(r, v) = (\varphi^{-1}(r), u)$ for some $u$ (Definition [[§48 The Tangent Bundle#^def-48-5|§48.5]]),
>
> $$
> \varphi \circ \pi \circ \tilde\varphi^{-1}(r, v) = \varphi\big(\pi(\varphi^{-1}(r), u)\big) = \varphi\big(\varphi^{-1}(r)\big) = r .
> $$
>
> So in the charts $\tilde\varphi$ and $\varphi$, $\pi$ is $(r, v) \mapsto r$, a linear projection, which is smooth.
>
> *(2)* By Definition [[§38 Fibrations#^def-38-1|§38.1]] we need an open cover of $M$ and, over each member $U$, a diffeomorphism $\pi^{-1}(U) = TU \to U \times \mathbb{R}^m$ commuting with the projections. Take the chart domains $U$, which cover $M$, and the maps $\Phi$ of Definition [[§48 The Tangent Bundle#^def-48-4|§48.4]]. Since $\tilde\varphi = (\varphi \times \mathrm{id}) \circ \Phi$ (Definition [[§48 The Tangent Bundle#^def-48-5|§48.5]]) and $\varphi \times \mathrm{id} : U \times \mathbb{R}^m \to \varphi(U) \times \mathbb{R}^m$ is a bijection with inverse $\varphi^{-1} \times \mathrm{id}$,
>
> $$
> \Phi = (\varphi^{-1} \times \mathrm{id}) \circ \tilde\varphi .
> $$
>
> Both factors are diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]): $\tilde\varphi$ is a chart of the smooth manifold $TU$, and $\varphi^{-1} \times \mathrm{id}$ is the inverse of the product chart $\varphi \times \mathrm{id}$ of the product manifold $U \times \mathbb{R}^m$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]], with the chart $\mathrm{id}$ of $\mathbb{R}^m$). A composite of diffeomorphisms is a diffeomorphism, since the composite and its inverse are composites of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]). And for $(p, v) \in TU$, $\mathrm{pr}_1(\Phi(p, v)) = \mathrm{pr}_1(p, v^1, \ldots, v^m) = p = \pi(p, v)$, so $\mathrm{pr}_1 \circ \Phi = \pi$ on $TU$. Hence $\pi$ is a fibration with fibre $\mathbb{R}^m$.
>
> *Linearity on fibres.* Fix $p \in U$. On $T_pM$ (that is, on the fibre $\{p\} \times T_pM$), $\Phi$ is $v \mapsto (p, v^1, \ldots, v^m)$ with $v^i = v[x^i]$ (universal formula, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]). Each $v \mapsto v[x^i]$ is linear, because tangent vectors are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]): $(av + bw)[x^i] = a\,v[x^i] + b\,w[x^i]$. It is bijective onto $\mathbb{R}^m$ because the $\partial/\partial x^i|_p$ form a basis (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]): the components of $v$ exist and are unique, and every list $(a^1, \ldots, a^m)$ is the list of components of $\sum_i a^i\, \partial/\partial x^i|_p$. So taking components in a basis is a linear isomorphism $T_pM \to \{p\} \times \mathbb{R}^m$.
>
> *(3)* By Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] (with $2m$ coordinates and $k = m$), it suffices to find, around each point of $\zeta(M)$, a smooth chart of $TM$ in which $\zeta(M)$ is cut out by the vanishing of the last $m$ coordinates. A point of $\zeta(M)$ is $\zeta(p) = (p, 0)$; take a chart $(U, \varphi)$ of $M$ at $p$, so $(p, 0) \in TU$. A point $\zeta(q) = (q, 0)$ lies in $TU$ exactly when $q \in U$, so $\zeta(M) \cap TU = \{(q, 0) : q \in U\}$. For $(q, v) \in TU$, the last $m$ coordinates of $\tilde\varphi(q, v)$ are $v^i = v[x^i]$, and by the universal formula $v = \sum_i v^i\, \partial/\partial x^i|_q$, so $v = 0$ exactly when $v^1 = \cdots = v^m = 0$. Hence
>
> $$
> \zeta(M) \cap TU = \{\, (q, v) \in TU : v^1 = \cdots = v^m = 0 \,\},
> $$
>
> so the charts $\tilde\varphi$ are adapted to $\zeta(M)$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), and $\zeta(M)$ is a submanifold of codimension $m$.

^pf-48-3

*Uses:* [[§48 The Tangent Bundle#^def-48-4|Def. §48.4]], [[§48 The Tangent Bundle#^prop-48-1|§48.1]], [[§48 The Tangent Bundle#^prop-48-2|§48.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§48 The Tangent Bundle#^def-48-2|Def. §48.2]], [[§48 The Tangent Bundle#^def-48-5|Def. §48.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

> [!theorem] Proposition §48.4: The Tangent Bundle Is a Manifold (Claim)
> $TM$ has a natural topology and smooth structure making it a smooth manifold of dimension $2m$, for which $\pi : TM \to M$ is a fibration with fibre $\mathbb{R}^m$, and the image $\zeta(M)$ of the zero section is a submanifold of $TM$.
>
> *Lee: Proposition 3.18*

^prop-48-4

> [!proof]+ Proof
> [[§48 The Tangent Bundle#^prop-48-1|Proposition §48.1]] gives the topology, and [[§48 The Tangent Bundle#^cor-48-3|Corollary §48.3]] the smooth structure, the fibration with fibre $\mathbb{R}^m$, and the zero section as a submanifold.

^pf-48-4

*Uses:* [[§48 The Tangent Bundle#^prop-48-1|§48.1]], [[§48 The Tangent Bundle#^prop-48-2|§48.2]], [[§48 The Tangent Bundle#^cor-48-3|§48.3]]

> [!remark] Remark: Vector Bundles
> $TM$ is in fact a *vector bundle*: a fibration whose fibres are vector spaces, with trivializations that are linear isomorphisms on each fibre. Uribe postponed the general definition — “it takes another 10 minutes of axioms” — but these are the two features: “the fibres are abstract vector spaces, and you can find trivializations which restrict to linear isomorphisms fibrewise.” Vector bundles are “fun objects” in their own right; K-theory is built from them.

^rem-48-2

> [!remark] Remark: Trivializations and Frames
> [[§38 Fibrations#^prop-38-4|Proposition §38.4]] turns local trivializations into local sections. For the tangent bundle the dictionary is between trivializations and *frames*: the trivialization $\Phi$ of a chart (Definition [[§48 The Tangent Bundle#^def-48-4|§48.4]]) corresponds to the $m$ local sections ([[§38 Fibrations#^def-38-4|Def. §38.4]]) $u \mapsto \partial/\partial x^i|_u$, since $\Phi^{-1}(u, e_i) = \partial/\partial x^i|_u$; for a vector bundle ([[§48 The Tangent Bundle#^rem-48-2|Rem. in §48]]) of rank $m$ one local section is not enough, and it takes $m$ sections that are linearly independent at every point (Lee, Example 10.18 and Proposition 10.19). For the Hopf fibration one section suffices because the fibre is a single orbit ([[§13 Group Actions and Orbit Spaces#^def-13-3|Def. §13.3]]) of the free $S^1$-action. That is the general pattern of *principal bundles*, where a group acts freely and transitively on each fibre; it is stated here, not proved.

^rem-48-3
