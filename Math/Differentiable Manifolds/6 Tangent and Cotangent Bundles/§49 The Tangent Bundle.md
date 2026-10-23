---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 49
tags: [differentiable-manifolds, math591]
---
← [[§48 Recap꞉ Covectors and the Four Differentials]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§50 The Cotangent Bundle]] →

*Stage: bundles — All the tangent spaces of $M$, assembled into a single manifold that fibres over $M$.*

*Lecture 12. “Again, these constructions, especially the cotangent [bundle], are basic parts of the basic theory.” The tangent bundle was introduced as a set, with its projection and zero section; its topology, smooth structure and charts come next lecture.*

> [!definition] Definition §49.1: The Tangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **tangent bundle** is the set
>
> $$
> TM = \bigcup_{p \in M} \{p\} \times T_pM = \{\, (p, v) : p \in M,\ v \in T_pM \,\},
> $$
>
> all the tangent spaces “put together in one big set.”
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-49-1

> [!definition] Definition §49.2: The Projection of $TM$
> The **projection** of the tangent bundle is
>
> $$
> \pi : TM \longrightarrow M, \qquad \pi(p, v) = p .
> $$
>
> Its fibre over $p$, $\pi^{-1}(p) = \{p\} \times T_pM$, is identified with $T_pM$.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-49-2

> [!definition] Definition §49.3: The Zero Section of $TM$
> The **zero section** of the tangent bundle is
>
> $$
> \zeta : M \longrightarrow TM, \qquad \zeta(p) = (p, 0) .
> $$
>
> It is one-to-one because every tangent space has a distinguished element, its zero.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-49-3

> [!remark] Remark: The Picture Changes
> “There are several psychological inflection steps that one needs to make. The most important one is that we're going to think of $TM$ as fibering over $M$.” A tangent space is usually drawn touching $M$, lying along it. In the bundle picture it stands *vertically*, as the fibre over its point, and $M$ itself sits horizontally inside $TM$ as the zero section — the tangent spaces become “transversal” to it.

^rem-49-1

![[m591-17-1.svg]]
*The tangent bundle as a fibration. Each fibre $\pi^{-1}(p) = T_pM$ is a vertical line over $p$ (in general a copy of $\mathbb{R}^m$); the point $(p, v)$ lies on it, and the zero section $\zeta$ lifts each $p$ straight up to $(p, 0)$, placing a copy of $M$ horizontally inside $TM$.*

![[m591-17-6.svg]]
*$TS^1$ as a cylinder. Left: the usual picture, each tangent line touching the circle at its point. Right: the bundle picture of the remark — each tangent line $T_pS^1$ (red) stands upright over $p$, and the zero section $\zeta(S^1)$ (blue) runs around the waist. Here the bundle is a genuine product $S^1 \times \mathbb{R}$: two angle charts ([[§24 The Circle#^prop-24-1|§24.1]]) differ by a constant on each piece of their overlap, so their coordinate vectors $\partial/\partial\theta$ agree, and $c\,\partial/\partial\theta|_p \mapsto (p, c)$ is a global trivialization. The green circle is the vector field $\partial/\partial\theta$ ([[§53 Vector Fields#^def-53-1|Definition §53.1]]), a section that never meets the zero section.*

*Status.* [[§49 The Tangent Bundle#^prop-49-5|Proposition §49.5]], below, was stated in Lecture 12 — “the claim, which takes a lot of detail to prove” — and made precise in Lecture 13 ([[§49 The Tangent Bundle#Trivializations and Charts|Trivializations and Charts]]), which wrote down the charts. Their idea was given: a chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ gives the basis $\partial/\partial x^i|_p$ of every $T_pM$, $p \in U$, hence an identification of each of these tangent spaces with $\mathbb{R}^m$; “putting all that together gives us a map” $\pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}$, the chart of $TM$. The dimension $2m$ is $m$ coordinates for the point and $m$ for the vector.

## Trivializations and Charts

*Lecture 13. “Back to the tangent bundle.” $TM$ has been defined as a set; its charts come from charts of $M$ and the coordinate bases.*

> [!definition] Definition §49.4: Local Trivializations of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $TU = \pi^{-1}(U) = \{(p, v) \in TM : p \in U\}$, the tangent vectors at points of $U$. The **local trivialization** over $U$ is
>
> $$
> \Phi : TU \longrightarrow U \times \mathbb{R}^m, \qquad \Phi(p, v) = (p, v^1, \ldots, v^m), \qquad \text{where } v = \sum_{i=1}^m v^i \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> the components of $v$ in the coordinate basis ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6]]). It is a bijection, and $\mathrm{pr}_1 \circ \Phi = \pi$ — “that's why I call it a trivialization.”
>
> *Lee: Proposition 3.18*

^def-49-4

> [!definition] Definition §49.5: Charts of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $\Phi$ the local trivialization over $U$ ([[§49 The Tangent Bundle#^def-49-4|Definition §49.4]]). The **chart** of $TM$ over $U$ is
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
> (the universal formula, [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|Theorem §29.6]]). So the first $m$ coordinates of $\tilde\varphi(p, v)$ locate the point $p$, and the last $m$ list the components of the vector $v$. $\tilde\varphi$ is a bijection, with inverse
>
> $$
> (r, a^1, \ldots, a^m) \longmapsto \Big(\varphi^{-1}(r),\ \sum_{i=1}^m a^i\, \frac{\partial}{\partial x^i}\Big|_{\varphi^{-1}(r)}\Big), \qquad r \in \varphi(U),\ (a^1, \ldots, a^m) \in \mathbb{R}^m .
> $$
>
> *Lee: Proposition 3.18*

^def-49-5

![[m591-17-2.svg]]
*The trivialization and the chart, as on the board. The triangle commutes, $\mathrm{pr}_1 \circ \Phi = \pi$ — the fibration diagram of [[§38 Fibrations#^def-38-1|Definition §38.1]] — and the chart $\tilde\varphi$ is $\Phi$ followed by $\varphi$ on the first factor.*

> [!theorem] Lemma §49.1: Building a Manifold from Charts
> Let $X$ be a set and $n \ge 0$ an integer. Suppose given subsets $U_\alpha \subseteq X$, indexed by $\alpha$ in some set $A$, and injective maps $\varphi_\alpha : U_\alpha \to \mathbb{R}^n$, such that:
>
> 1. each $\varphi_\alpha(U_\alpha)$ is open in $\mathbb{R}^n$;
> 2. each $\varphi_\alpha(U_\alpha \cap U_\beta)$, $\alpha, \beta \in A$, is open in $\mathbb{R}^n$;
> 3. each map $\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$, $\alpha, \beta \in A$, is smooth;
> 4. countably many of the sets $U_\alpha$ cover $X$;
> 5. for distinct points $p, q \in X$, either some $U_\alpha$ contains both, or there are disjoint sets $U_\alpha \ni p$ and $U_\beta \ni q$.
>
> Then $X$ has a unique topology for which every $U_\alpha$ is open and every $\varphi_\alpha$ is a homeomorphism of $U_\alpha$ onto $\varphi_\alpha(U_\alpha)$. With it, $X$ is a topological manifold of dimension $n$, and the charts $(U_\alpha, \varphi_\alpha)$ form a smooth atlas on $X$, so they determine a smooth structure (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> *Lee: Lemma 1.35*

^lem-49-1

> [!proof]+ Proof
> *(Not from lecture: Lee's smooth manifold chart lemma. Lecture 13 called the construction of the topology of $TM$ “all point-set topology … see Lee”. The argument is written once here, in general, and applied to $TM$ in Proposition [[§49 The Tangent Bundle#^prop-49-3|§49.3]] and to $T^{\ast}M$ in Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]].)* Three things have to be shown: a topology with the two stated properties exists; it is the only one; and with it $X$ is second countable, Hausdorff and locally Euclidean of dimension $n$ (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]), with the $(U_\alpha, \varphi_\alpha)$ a smooth atlas.
>
> *The transition maps are homeomorphisms.* Let $\alpha, \beta \in A$. Since $\varphi_\alpha$ and $\varphi_\beta$ are injective, $\varphi_\beta \circ \varphi_\alpha^{-1}$ is a bijection of $\varphi_\alpha(U_\alpha \cap U_\beta)$ onto $\varphi_\beta(U_\alpha \cap U_\beta)$, both open by (2), with inverse $\varphi_\alpha \circ \varphi_\beta^{-1}$. Both maps are smooth by (3) (the second with $\alpha$ and $\beta$ exchanged), hence continuous; so each transition map is a homeomorphism between open subsets of $\mathbb{R}^n$.
>
> *The topology.* Declare $W \subseteq X$ open if $\varphi_\alpha(W \cap U_\alpha)$ is open in $\mathbb{R}^n$ for every $\alpha \in A$, and call the collection of these sets $\tau$. It is a topology; the three axioms are checked chart by chart.
> - $\emptyset \in \tau$, since $\varphi_\alpha(\emptyset) = \emptyset$; and $X \in \tau$, since $\varphi_\alpha(X \cap U_\alpha) = \varphi_\alpha(U_\alpha)$ is open by (1).
> - For any family $W_\lambda \in \tau$, images under any map commute with unions, so $\varphi_\alpha\big((\bigcup_\lambda W_\lambda) \cap U_\alpha\big) = \bigcup_\lambda \varphi_\alpha(W_\lambda \cap U_\alpha)$, a union of open sets.
> - For $W_1, W_2 \in \tau$, an injective map carries intersections to intersections, and $\varphi_\alpha$ is injective, so $\varphi_\alpha(W_1 \cap W_2 \cap U_\alpha) = \varphi_\alpha(W_1 \cap U_\alpha) \cap \varphi_\alpha(W_2 \cap U_\alpha)$, an intersection of two open sets.
>
> *Each $U_\alpha$ is open.* For every $\beta \in A$, $\varphi_\beta(U_\alpha \cap U_\beta)$ is open by (2). So $U_\alpha \in \tau$.
>
> *Each $\varphi_\alpha$ is a homeomorphism onto the open set $\varphi_\alpha(U_\alpha)$.* Give $U_\alpha$ the subspace topology. $\varphi_\alpha : U_\alpha \to \varphi_\alpha(U_\alpha)$ is a bijection; it remains to show that it is open and continuous.
>
> *Open:* if $W \subseteq U_\alpha$ is open in $U_\alpha$, then $W$ is open in $X$, because $U_\alpha$ is open (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]); so, by the definition of $\tau$ applied with $\alpha$, $\varphi_\alpha(W) = \varphi_\alpha(W \cap U_\alpha)$ is open.
>
> *Continuous:* let $O \subseteq \varphi_\alpha(U_\alpha)$ be open and $W = \varphi_\alpha^{-1}(O) \subseteq U_\alpha$. For any $\beta \in A$, the set $W \cap U_\beta$ consists of the points of $U_\alpha \cap U_\beta$ whose image under $\varphi_\alpha$ lies in $O$, so $\varphi_\alpha(W \cap U_\beta) = O \cap \varphi_\alpha(U_\alpha \cap U_\beta)$, and therefore
>
> $$
> \varphi_\beta(W \cap U_\beta) = \big(\varphi_\beta \circ \varphi_\alpha^{-1}\big)\Big(O \cap \varphi_\alpha(U_\alpha \cap U_\beta)\Big).
> $$
>
> The set in parentheses is open (an intersection of two open sets) and lies in the domain of the transition map; a homeomorphism carries it to a set open in the target $\varphi_\beta(U_\alpha \cap U_\beta)$, which is open in $\mathbb{R}^n$, so the image is open in $\mathbb{R}^n$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). This holds for every $\beta$, so $W \in \tau$; as $W \subseteq U_\alpha$, it is open in $U_\alpha$. A continuous open bijection is a homeomorphism.
>
> *Uniqueness.* Let $\tau'$ be any topology in which every $U_\alpha$ is open and every $\varphi_\alpha$ is a homeomorphism onto its image; we show $\tau' = \tau$. If $W \in \tau'$, then for each $\alpha$, $W \cap U_\alpha$ is open in $U_\alpha$ (subspace topology of $\tau'$), so its image $\varphi_\alpha(W \cap U_\alpha)$ under the homeomorphism $\varphi_\alpha$ is open in $\varphi_\alpha(U_\alpha)$, hence in $\mathbb{R}^n$; so $W \in \tau$. Conversely, let $W \in \tau$. For each $\alpha$, $\varphi_\alpha(W \cap U_\alpha)$ is open, so $W \cap U_\alpha = \varphi_\alpha^{-1}\big(\varphi_\alpha(W \cap U_\alpha)\big)$ is open in $U_\alpha$ for $\tau'$, by continuity of $\varphi_\alpha$; it is then open in $X$ for $\tau'$, since $U_\alpha \in \tau'$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). The $U_\alpha$ cover $X$ by (4), so $W = \bigcup_\alpha (W \cap U_\alpha)$, a union of members of $\tau'$; hence $W \in \tau'$.
>
> *Locally Euclidean.* Let $p \in X$. By (4), $p$ lies in some $U_\alpha$, which is open, and $\varphi_\alpha$ is a homeomorphism of $U_\alpha$ onto the open subset $\varphi_\alpha(U_\alpha)$ of $\mathbb{R}^n$. This is Definition [[§2 Topological Manifolds#^def-2-1|§2.1]].
>
> *Hausdorff.* Let $p \ne q$ in $X$; we need disjoint open sets containing them (Definition [[§1 Point-Set Topology Review#^def-1-8|§1.8]]). By (5) there are two cases. *Both lie in one $U_\alpha$.* Their images under the injective map $\varphi_\alpha$ are distinct points of the Hausdorff space $\mathbb{R}^n$, so they have disjoint open neighbourhoods $O_1$, $O_2$. The sets $\varphi_\alpha^{-1}(O_1 \cap \varphi_\alpha(U_\alpha))$ and $\varphi_\alpha^{-1}(O_2 \cap \varphi_\alpha(U_\alpha))$ are disjoint, contain $p$ and $q$ respectively, and are open in $U_\alpha$ by continuity of $\varphi_\alpha$, hence open in $X$ because $U_\alpha$ is (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). *Disjoint $U_\alpha \ni p$ and $U_\beta \ni q$.* These are the required open sets.
>
> *Second countable.* By (4) there are $\alpha_1, \alpha_2, \ldots \in A$ with $X = \bigcup_k U_{\alpha_k}$. Each $U_{\alpha_k}$ is homeomorphic to an open subset of $\mathbb{R}^n$, which has a countable basis (for instance the balls with rational centres and rational radii contained in it), so $U_{\alpha_k}$ has a countable basis $\mathcal{C}_k$, whose members are open in $U_{\alpha_k}$ and hence in $X$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). The union $\mathcal{C} = \bigcup_k \mathcal{C}_k$ is a countable union of countable sets, so countable. It is a basis of $X$ (Definition [[§1 Point-Set Topology Review#^def-1-1|§1.1]]): if $W$ is open in $X$ and $p \in W$, choose $k$ with $p \in U_{\alpha_k}$; then $W \cap U_{\alpha_k}$ is open in $U_{\alpha_k}$ and contains $p$, so some $C \in \mathcal{C}_k$ has $p \in C \subseteq W \cap U_{\alpha_k} \subseteq W$ (Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]).
>
> *The smooth atlas.* Each $(U_\alpha, \varphi_\alpha)$ is a chart of the topological manifold $X$: a homeomorphism of an open set onto an open subset of $\mathbb{R}^n$. The domains cover $X$ by (4), and any two charts are $C^\infty$-compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]), because each transition map $\varphi_\beta \circ \varphi_\alpha^{-1}$ is smooth with smooth inverse $\varphi_\alpha \circ \varphi_\beta^{-1}$ by (3), a diffeomorphism between open subsets of $\mathbb{R}^n$ (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]). So the charts form a smooth atlas (Definition [[§17 Differentiable Structures#^def-17-6|§17.6]]).

^pf-49-1

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]]

![[m591-49-5.svg]]

The chart lemma in one picture. The set $X$ has no topology yet; it is only covered by sets $U_\alpha$, $U_\beta$ with injections into $\mathbb{R}^n$. Condition (2) asks that the overlap (shaded) go to open sets on both sides, and (3) that the transition map $\varphi_\beta \circ \varphi_\alpha^{-1}$ between these two open sets be smooth. The topology is then forced: a set is open exactly when each chart sends its part to an open set.

> [!theorem] Proposition §49.2: The Transition Maps of $TM$
> Let $(U, \varphi = (x^i))$ and $(V, \psi = (y^j))$ be smooth charts of $M$. Then $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$, an open subset of $\mathbb{R}^{2m}$, and the transition map is
>
> $$
> \tilde\psi \circ \tilde\varphi^{-1}(r, v) = \Big( \psi \circ \varphi^{-1}(r), \ \ \sum_{j=1}^m \frac{\partial y^1}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j, \ \ldots, \ \sum_{j=1}^m \frac{\partial y^m}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j \Big) .
> $$
>
> In matrix form, the last $m$ components are the column $v$ multiplied by the Jacobian $\big[\partial y^i/\partial x^j\big]$ of the change of coordinates (row $i$, column $j$), evaluated at $\varphi^{-1}(r)$:
>
> $$
> \begin{pmatrix}
> \dfrac{\partial y^1}{\partial x^1} & \cdots & \dfrac{\partial y^1}{\partial x^m} \\
> \vdots & \ddots & \vdots \\
> \dfrac{\partial y^m}{\partial x^1} & \cdots & \dfrac{\partial y^m}{\partial x^m}
> \end{pmatrix}
> \begin{pmatrix} v^1 \\ \vdots \\ v^m \end{pmatrix} .
> $$
>
> It is a diffeomorphism of $\varphi(U \cap V) \times \mathbb{R}^m$ onto $\psi(U \cap V) \times \mathbb{R}^m$. No topology on $TM$ is used: the statement concerns only the bijections $\tilde\varphi$, $\tilde\psi$ of Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]].
>
> *Lee: Proposition 3.18*

^prop-49-2

> [!proof]+ Proof
> *(Lecture 13: “the only thing that I want to have a look at is … the transition functions of the atlas, because this is how people handle tangent vectors.” Completed here.)* Three things have to be shown: the domain and target of the transition map; its formula; and that it is a diffeomorphism, that is (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]), smooth with smooth inverse.
>
> *The domain of the transition map.* A point $(p, v)$ lies in $TU \cap TV$ exactly when $p \in U \cap V$; for such $p$ every list of components $(v^1, \ldots, v^m) \in \mathbb{R}^m$ occurs (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). So the domain is $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$, open in $\mathbb{R}^{2m}$ since $\varphi(U \cap V)$ is open (Proposition [[§2 Topological Manifolds#^prop-2-11|§2.11]]); likewise the target is $\psi(U \cap V) \times \mathbb{R}^m$.
>
> *The formula.* Let $(r, v) = (r, v^1, \ldots, v^m)$ be a point of the domain and $p = \varphi^{-1}(r) \in U \cap V$. By the inverse formula of Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]], $\tilde\varphi^{-1}(r, v) = (p, u)$ with $u \in T_pM$ the tangent vector whose components in the basis $\partial/\partial x^j|_p$ are the $v^j$. Write $u$ in both bases (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]):
>
> $$
> u = \sum_j v^j \frac{\partial}{\partial x^j}\Big|_p = \sum_i w^i \frac{\partial}{\partial y^i}\Big|_p .
> $$
>
> By Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]] for the chart $\psi$, $\tilde\psi(p, u) = \big(\psi(p), w^1, \ldots, w^m\big)$, and $\psi(p) = \psi \circ \varphi^{-1}(r)$; so the first component of the transition is $\psi \circ \varphi^{-1}$, smooth because the charts of $M$ are compatible. For the rest we need the $w$'s in terms of the $v$'s: “a change of basis formula from 217, which I always forget.” By the universal formula (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]) in the chart $\psi$, the $i$-th coefficient of a derivation $D$ in the basis $\partial/\partial y^i|_p$ is $D[y^i]$. Applied to $D = \partial/\partial x^j|_p$, whose value on $y^i$ is $\partial y^i/\partial x^j(p)$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]]), it gives the change of basis formula
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
> *The inverse.* The inverse of $\tilde\psi \circ \tilde\varphi^{-1}$ is $\tilde\varphi \circ \tilde\psi^{-1}$, and the computation above with the names exchanged — $(U, \varphi, x^i)$ and $(V, \psi, y^i)$ swapped — shows that it is $(s, w) \mapsto \big(\varphi \circ \psi^{-1}(s), (\varphi \circ \psi^{-1})'(s)\, w\big)$, smooth. So every transition map is a smooth bijection with smooth inverse, a diffeomorphism (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]).

^pf-49-2

*Uses:* [[§49 The Tangent Bundle#^def-49-4|Def. §49.4]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]], [[§49 The Tangent Bundle#^prop-49-3|§49.3]], [[§2 Topological Manifolds#^prop-2-11|§2.11]], [[§49 The Tangent Bundle#^def-49-5|Def. §49.5]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]]

![[m591-17-3.svg]]
*The transition map of the charts $\tilde\varphi$ and $\tilde\psi$ of $TM$, as drawn in lecture over a point $(p, v)$ of $TU \cap TV$.*

> [!remark]- Connections
> - The same expansion of coordinate derivations: [[§30 The Differential in Coordinates#^cor-30-4|Change of Coordinates, §30.4]]; the Jacobian matrix in 452: [[§16 The Inverse Function Theorem#^def-16-1|452 Def. §16.1]]; change of basis: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].

The transition map of $TM$, in one line: the base point moves by the transition map of $M$, and the vector by its Jacobian. This is Uribe's identity at work once more — the partials $\partial y^i/\partial x^j$, taken upstairs on $M$, are the Jacobian downstairs.

> [!theorem] Proposition §49.3: The Topology and Smooth Structure of $TM$
> There is a unique topology on $TM$ for which every $TU$ is open and every chart $\tilde\varphi : TU \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $TM$ is a topological manifold of dimension $2m$, and the charts $(TU, \tilde\varphi)$, as $(U, \varphi)$ ranges over the smooth charts of $M$, form a smooth atlas on it.
>
> *Lee: Lemma 1.35 and Proposition 3.18*

^prop-49-3

> [!proof]+ Proof
> *(Stated in Lecture 13 without proof — “it's all point-set topology, and of course everything is in Lee … see Lee”; filled in.)* Apply Lemma [[§49 The Tangent Bundle#^lem-49-1|§49.1]] with $X = TM$, $n = 2m$, and the sets $TU$ with the maps $\tilde\varphi$, indexed by the smooth charts $(U, \varphi)$ of $M$. Each $\tilde\varphi$ is injective, being a bijection of $TU$ onto $\varphi(U) \times \mathbb{R}^m$ (Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]]). We check the five conditions of the lemma.
>
> *(1) and (2).* By Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]], $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$ is open in $\mathbb{R}^{2m}$ for any two charts; this is (2), and with $V = U$ it is (1), $\tilde\varphi(TU) = \varphi(U) \times \mathbb{R}^m$.
>
> *(3)* Each transition map $\tilde\psi \circ \tilde\varphi^{-1}$ is smooth by Proposition [[§49 The Tangent Bundle#^prop-49-2|§49.2]].
>
> *(4)* Let $\mathcal{B}$ be a countable basis of $M$ (Definition [[§1 Point-Set Topology Review#^def-1-6|§1.6]]). For each $B \in \mathcal{B}$ contained in some chart domain, choose one such chart $(U_B, \varphi_B)$, so $B \subseteq U_B$. These countably many charts cover $M$: each $p$ lies in some chart domain $U$, and then, by Definition [[§1 Point-Set Topology Review#^def-1-1|§1.1]], in some $B \in \mathcal{B}$ with $p \in B \subseteq U$; this $B$ is contained in a chart domain, so $(U_B, \varphi_B)$ was chosen, and $p \in B \subseteq U_B$. A point $(p, v) \in TM$ lies in $TU_B$ for any $B$ with $p \in U_B$, so the countably many sets $TU_B$ cover $TM$.
>
> *(5)* Let $(p, v) \ne (q, w)$. *Case $p = q$.* Both points lie in $TU$ for any chart $(U, \varphi)$ at $p$. *Case $p \ne q$.* $M$ is Hausdorff, so there are disjoint open sets $U_0 \ni p$ and $V_0 \ni q$. Take charts $(U, \varphi)$ at $p$ and $(V, \psi)$ at $q$ and shrink their domains to $U \cap U_0$ and $V \cap V_0$; the restrictions are still smooth charts (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1), applied to the open subsets $U \cap U_0 \subseteq U$ and $V \cap V_0 \subseteq V$; their transition maps are restrictions of those of $\varphi$ and $\psi$ to open subsets). Then $T(U \cap U_0) \ni (p, v)$ and $T(V \cap V_0) \ni (q, w)$ are disjoint: a common point $(x, u)$ would have $x \in U_0 \cap V_0 = \emptyset$.
>
> So Lemma [[§49 The Tangent Bundle#^lem-49-1|§49.1]] applies: $TM$ has a unique topology in which every $TU$ is open and every $\tilde\varphi$ is a homeomorphism onto $\varphi(U) \times \mathbb{R}^m$; with it, $TM$ is a topological manifold of dimension $2m$, and the charts $(TU, \tilde\varphi)$ form a smooth atlas.

^pf-49-3

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§49 The Tangent Bundle#^def-49-5|Def. §49.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§2 Topological Manifolds#^prop-2-11|§2.11]], [[§49 The Tangent Bundle#^prop-49-2|§49.2]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§49 The Tangent Bundle#^lem-49-1|§49.1]]

Lemma [[§49 The Tangent Bundle#^lem-49-1|§49.1]] builds the topology and smooth structure of the cotangent bundle ([[§50 The Cotangent Bundle|§50]]) in the same way, with the dual bases in place of the coordinate bases (Proposition [[§50 The Cotangent Bundle#^prop-50-2|§50.2]]).

> [!theorem] Corollary §49.4: The Tangent Bundle Is a Fibration
> With the smooth structure of Proposition [[§49 The Tangent Bundle#^prop-49-3|§49.3]]:
>
> 1. $TM$ is a smooth manifold of dimension $2m$, and $\pi : TM \to M$ is smooth;
> 2. the $\Phi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Phi$ restricts on the fibre $T_pM$ to a linear isomorphism $T_pM \to \{p\} \times \mathbb{R}^m$;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $TM$ of codimension $m$.
>
> With Proposition [[§49 The Tangent Bundle#^prop-49-3|§49.3]], this proves Proposition [[§49 The Tangent Bundle#^prop-49-5|§49.5]] below in full.

^cor-49-4

> [!proof]+ Proof
> *((1) and (2) are the lecture's observations — “in these coordinates, the projection is just projection onto the first $m$ components … so we get a beautiful fibration”; the details and (3) are filled in.)*
>
> *(1)* By Proposition [[§49 The Tangent Bundle#^prop-49-3|§49.3]], $TM$ is a topological manifold of dimension $2m$ and the charts $(TU, \tilde\varphi)$ form a smooth atlas on it; so $TM$ is a smooth manifold of dimension $2m$, with the smooth structure determined by this atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). To see that $\pi$ is smooth, check Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]. *Continuity:* on each open set $TU$, by Definitions [[§49 The Tangent Bundle#^def-49-2|§49.2]] and [[§49 The Tangent Bundle#^def-49-5|§49.5]], $\pi = \varphi^{-1} \circ \mathrm{pr}_1 \circ \tilde\varphi$ with $\mathrm{pr}_1(r, v) = r$, a composite of continuous maps; the open sets $TU$ cover $TM$, so $\pi$ is continuous. *Coordinate representation:* for $(p, v) \in TM$ take a chart $(U, \varphi)$ of $M$ at $p$; then $(TU, \tilde\varphi)$ is a chart at $(p, v)$ with $\pi(TU) \subseteq U$, and for $(r, v) \in \varphi(U) \times \mathbb{R}^m$, with $\tilde\varphi^{-1}(r, v) = (\varphi^{-1}(r), u)$ for some $u$ (Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]]),
>
> $$
> \varphi \circ \pi \circ \tilde\varphi^{-1}(r, v) = \varphi\big(\pi(\varphi^{-1}(r), u)\big) = \varphi\big(\varphi^{-1}(r)\big) = r .
> $$
>
> So in the charts $\tilde\varphi$ and $\varphi$, $\pi$ is $(r, v) \mapsto r$, a linear projection, which is smooth.
>
> *(2)* By Definition [[§38 Fibrations#^def-38-1|§38.1]] we need an open cover of $M$ and, over each member $U$, a diffeomorphism $\pi^{-1}(U) = TU \to U \times \mathbb{R}^m$ commuting with the projections. Take the chart domains $U$, which cover $M$, and the maps $\Phi$ of Definition [[§49 The Tangent Bundle#^def-49-4|§49.4]]. Since $\tilde\varphi = (\varphi \times \mathrm{id}) \circ \Phi$ (Definition [[§49 The Tangent Bundle#^def-49-5|§49.5]]) and $\varphi \times \mathrm{id} : U \times \mathbb{R}^m \to \varphi(U) \times \mathbb{R}^m$ is a bijection with inverse $\varphi^{-1} \times \mathrm{id}$,
>
> $$
> \Phi = (\varphi^{-1} \times \mathrm{id}) \circ \tilde\varphi .
> $$
>
> Both factors are diffeomorphisms (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]): $\tilde\varphi$ is a chart of the smooth manifold $TU$, and $\varphi^{-1} \times \mathrm{id}$ is the inverse of the product chart $\varphi \times \mathrm{id}$ of the product manifold $U \times \mathbb{R}^m$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]], with the chart $\mathrm{id}$ of $\mathbb{R}^m$). A composite of diffeomorphisms is a diffeomorphism, since the composite and its inverse are composites of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). And for $(p, v) \in TU$, $\mathrm{pr}_1(\Phi(p, v)) = \mathrm{pr}_1(p, v^1, \ldots, v^m) = p = \pi(p, v)$, so $\mathrm{pr}_1 \circ \Phi = \pi$ on $TU$. Hence $\pi$ is a fibration with fibre $\mathbb{R}^m$.
>
> *Linearity on fibres.* Fix $p \in U$. On $T_pM$ (that is, on the fibre $\{p\} \times T_pM$), $\Phi$ is $v \mapsto (p, v^1, \ldots, v^m)$ with $v^i = v[x^i]$ (universal formula, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]). Each $v \mapsto v[x^i]$ is linear, because tangent vectors are added and scaled pointwise (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-2|§28.2]]): $(av + bw)[x^i] = a\,v[x^i] + b\,w[x^i]$. It is bijective onto $\mathbb{R}^m$ because the $\partial/\partial x^i|_p$ form a basis (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]): the components of $v$ exist and are unique, and every list $(a^1, \ldots, a^m)$ is the list of components of $\sum_i a^i\, \partial/\partial x^i|_p$. So taking components in a basis is a linear isomorphism $T_pM \to \{p\} \times \mathbb{R}^m$.
>
> *(3)* By Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] (with $2m$ coordinates and $k = m$), it suffices to find, around each point of $\zeta(M)$, a smooth chart of $TM$ in which $\zeta(M)$ is cut out by the vanishing of the last $m$ coordinates. A point of $\zeta(M)$ is $\zeta(p) = (p, 0)$; take a chart $(U, \varphi)$ of $M$ at $p$, so $(p, 0) \in TU$. A point $\zeta(q) = (q, 0)$ lies in $TU$ exactly when $q \in U$, so $\zeta(M) \cap TU = \{(q, 0) : q \in U\}$. For $(q, v) \in TU$, the last $m$ coordinates of $\tilde\varphi(q, v)$ are $v^i = v[x^i]$, and by the universal formula $v = \sum_i v^i\, \partial/\partial x^i|_q$, so $v = 0$ exactly when $v^1 = \cdots = v^m = 0$. Hence
>
> $$
> \zeta(M) \cap TU = \{\, (q, v) \in TU : v^1 = \cdots = v^m = 0 \,\},
> $$
>
> so the charts $\tilde\varphi$ are adapted to $\zeta(M)$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), and $\zeta(M)$ is a submanifold of codimension $m$.

^pf-49-4

*Uses:* [[§49 The Tangent Bundle#^def-49-4|Def. §49.4]], [[§49 The Tangent Bundle#^prop-49-3|§49.3]], [[§49 The Tangent Bundle#^prop-49-2|§49.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§49 The Tangent Bundle#^def-49-2|Def. §49.2]], [[§49 The Tangent Bundle#^def-49-5|Def. §49.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§28 Derivations and the Abstract Tangent Space#^def-28-2|Def. §28.2]]

> [!theorem] Proposition §49.5: The Tangent Bundle Is a Manifold (Claim)
> $TM$ has a natural topology and smooth structure making it a smooth manifold of dimension $2m$, for which $\pi : TM \to M$ is a fibration with fibre $\mathbb{R}^m$, and the image $\zeta(M)$ of the zero section is a submanifold of $TM$.
>
> *Lee: Proposition 3.18*

^prop-49-5

> [!proof]+ Proof
> [[§49 The Tangent Bundle#^prop-49-3|Proposition §49.3]] gives the topology, and [[§49 The Tangent Bundle#^cor-49-4|Corollary §49.4]] the smooth structure, the fibration with fibre $\mathbb{R}^m$, and the zero section as a submanifold.

^pf-49-5

*Uses:* [[§49 The Tangent Bundle#^prop-49-3|§49.3]], [[§49 The Tangent Bundle#^prop-49-2|§49.2]], [[§49 The Tangent Bundle#^cor-49-4|§49.4]]

> [!remark] Remark: Vector Bundles
> $TM$ is in fact a *vector bundle*: a fibration whose fibres are vector spaces, with trivializations that are linear isomorphisms on each fibre. Uribe postponed the general definition — “it takes another 10 minutes of axioms” — but these are the two features: “the fibres are abstract vector spaces, and you can find trivializations which restrict to linear isomorphisms fibrewise.” Vector bundles are “fun objects” in their own right; K-theory is built from them.

^rem-49-2

> [!remark] Remark: Trivializations and Frames
> [[§38 Fibrations#^prop-38-4|Proposition §38.4]] turns local trivializations into local sections. For the tangent bundle the dictionary is between trivializations and *frames*: the trivialization $\Phi$ of a chart (Definition [[§49 The Tangent Bundle#^def-49-4|§49.4]]) corresponds to the $m$ local sections ([[§38 Fibrations#^def-38-4|Def. §38.4]]) $u \mapsto \partial/\partial x^i|_u$, since $\Phi^{-1}(u, e_i) = \partial/\partial x^i|_u$; for a vector bundle ([[§49 The Tangent Bundle#^rem-49-2|Rem. in §49]]) of rank $m$ one local section is not enough, and it takes $m$ sections that are linearly independent at every point (Lee, Example 10.18 and Proposition 10.19). For the Hopf fibration one section suffices because the fibre is a single orbit ([[§13 Group Actions and Orbit Spaces#^def-13-3|Def. §13.3]]) of the free $S^1$-action. That is the general pattern of *principal bundles*, where a group acts freely and transitively on each fibre; it is stated here, not proved.

^rem-49-3
