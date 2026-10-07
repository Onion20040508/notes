---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 44
tags: [differentiable-manifolds, math591]
---
← [[§43 Recap꞉ Covectors and the Four Differentials]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§45 The Cotangent Bundle]] →

*Stage: bundles — All the tangent spaces of $M$, assembled into a single manifold that fibres over $M$.*

*Lecture 12. “Again, these constructions, especially the cotangent [bundle], are basic parts of the basic theory.” The tangent bundle was introduced as a set, with its projection and zero section; its topology, smooth structure and charts come next lecture.*

> [!definition] Definition §44.1: The Tangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **tangent bundle** is the set
>
> $$
> TM = \bigcup_{p \in M} \{p\} \times T_pM = \{\, (p, v) : p \in M,\ v \in T_pM \,\},
> $$
>
> all the tangent spaces “put together in one big set.”
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-44-1

> [!definition] Definition §44.2: The Projection of $TM$
> The **projection** of the tangent bundle is
>
> $$
> \pi : TM \longrightarrow M, \qquad \pi(p, v) = p .
> $$
>
> Its fibre over $p$, $\pi^{-1}(p) = \{p\} \times T_pM$, is identified with $T_pM$.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-44-2

> [!definition] Definition §44.3: The Zero Section of $TM$
> The **zero section** of the tangent bundle is
>
> $$
> \zeta : M \longrightarrow TM, \qquad \zeta(p) = (p, 0) .
> $$
>
> It is one-to-one because every tangent space has a distinguished element, its zero.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-44-3

> [!remark] Remark: The Picture Changes
> “There are several psychological inflection steps that one needs to make. The most important one is that we're going to think of $TM$ as fibering over $M$.” A tangent space is usually drawn touching $M$, lying along it. In the bundle picture it stands *vertically*, as the fibre over its point, and $M$ itself sits horizontally inside $TM$ as the zero section — the tangent spaces become “transversal” to it.

^rem-44-1

![[m591-17-1.svg]]
*The tangent bundle as a fibration. Each fibre $\pi^{-1}(p) = T_pM$ is a vertical line over $p$ (in general a copy of $\mathbb{R}^m$); the point $(p, v)$ lies on it, and the zero section $\zeta$ lifts each $p$ straight up to $(p, 0)$, placing a copy of $M$ horizontally inside $TM$.*

![[m591-17-6.svg]]
*$TS^1$ as a cylinder. Left: the usual picture, each tangent line touching the circle at its point. Right: the bundle picture of the remark — each tangent line $T_pS^1$ (red) stands upright over $p$, and the zero section $\zeta(S^1)$ (blue) runs around the waist. Here the bundle is a genuine product $S^1 \times \mathbb{R}$: two angle charts ([[§24 The Circle#^prop-24-1|§24.1]]) differ by a constant on each piece of their overlap, so their coordinate vectors $\partial/\partial\theta$ agree, and $c\,\partial/\partial\theta|_p \mapsto (p, c)$ is a global trivialization. The green circle is the vector field $\partial/\partial\theta$ ([[§47 Vector Fields#^def-47-1|Definition §47.1]]), a section that never meets the zero section.*

*Status.* [[§44 The Tangent Bundle#^prop-44-4|Proposition §44.4]], below, was stated in Lecture 12 — “the claim, which takes a lot of detail to prove” — and made precise in Lecture 13 ([[§44 The Tangent Bundle#Trivializations and Charts|Trivializations and Charts]]), which wrote down the charts. Their idea was given: a chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ gives the basis $\partial/\partial x^i|_p$ of every $T_pM$, $p \in U$, hence an identification of each of these tangent spaces with $\mathbb{R}^m$; “putting all that together gives us a map” $\pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}$, the chart of $TM$. The dimension $2m$ is $m$ coordinates for the point and $m$ for the vector.

## Trivializations and Charts

*Lecture 13. “Back to the tangent bundle.” $TM$ has been defined as a set; its charts come from charts of $M$ and the coordinate bases.*

> [!definition] Definition §44.4: Local Trivializations of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $TU = \pi^{-1}(U) = \{(p, v) \in TM : p \in U\}$, the tangent vectors at points of $U$. The **local trivialization** over $U$ is
>
> $$
> \Phi : TU \longrightarrow U \times \mathbb{R}^m, \qquad \Phi(p, v) = (p, v^1, \ldots, v^m), \qquad \text{where } v = \sum_{i=1}^m v^i \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> the components of $v$ in the coordinate basis ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]). It is a bijection, and $\mathrm{pr}_1 \circ \Phi = \pi$ — “that's why I call it a trivialization.”
>
> *Lee: Proposition 3.18*

^def-44-4

> [!definition] Definition §44.5: Charts of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$ and $\Phi$ the local trivialization over $U$ ([[§44 The Tangent Bundle#^def-44-4|Definition §44.4]]). The **chart** of $TM$ over $U$ is
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

^def-44-5

![[m591-17-2.svg]]
*The trivialization and the chart, as on the board. The triangle commutes, $\mathrm{pr}_1 \circ \Phi = \pi$ — the fibration diagram of [[§36 Fibrations#^def-36-1|Definition §36.1]] — and the chart $\tilde\varphi$ is $\Phi$ followed by $\varphi$ on the first factor.*

> [!theorem] Proposition §44.1: The Topology of $TM$
> There is a unique topology on $TM$ for which every $TU$ is open and every chart $\tilde\varphi : TU \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $TM$ is a topological manifold of dimension $2m$.
>
> *Lee: Lemma 1.35 and Proposition 3.18*

^prop-44-1

> [!proof]+ Proof
> *(Stated in Lecture 13 without proof — “it's all point-set topology, and of course everything is in Lee … see Lee”; filled in, following Lee's smooth manifold chart lemma.)* Throughout, $(U, \varphi)$ and $(V, \psi)$ denote smooth charts of $M$.
>
> *The transition maps.* The computation in the proof of [[§44 The Tangent Bundle#^prop-44-2|Proposition §44.2]] below uses only the definitions of the charts, not any topology on $TM$. It shows that $\tilde\psi \circ \tilde\varphi^{-1}$ maps the open set $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$ bijectively onto the open set $\psi(U \cap V) \times \mathbb{R}^m$, by a smooth map whose inverse, $\tilde\varphi \circ \tilde\psi^{-1}$, is given by the same formula with the two charts exchanged. So each transition map is a homeomorphism between open subsets of $\mathbb{R}^{2m}$.
>
> *The topology.* Declare $W \subseteq TM$ open if $\tilde\varphi(W \cap TU)$ is open in $\mathbb{R}^{2m}$ for every chart $(U, \varphi)$. This is a topology: $\emptyset$ and $TM$ are open, the latter because $\tilde\varphi(TU) = \varphi(U) \times \mathbb{R}^m$ is open; and since each $\tilde\varphi$ is a bijection, it carries unions and finite intersections of subsets of $TU$ to unions and finite intersections of their images.
>
> *Each $TU$ is open, and each $\tilde\varphi$ is a homeomorphism onto an open set.* For any chart $(V, \psi)$, $\tilde\psi(TU \cap TV) = \psi(U \cap V) \times \mathbb{R}^m$ is open, so $TU$ is open. If $W \subseteq TU$ is open, then $\tilde\varphi(W) = \tilde\varphi(W \cap TU)$ is open by definition, so $\tilde\varphi$ is an open map. For continuity, let $O \subseteq \varphi(U) \times \mathbb{R}^m$ be open and $W = \tilde\varphi^{-1}(O)$. For any chart $(V, \psi)$,
>
> $$
> \tilde\psi(W \cap TV) = \big(\tilde\psi \circ \tilde\varphi^{-1}\big)\Big(O \cap \big(\varphi(U \cap V) \times \mathbb{R}^m\big)\Big),
> $$
>
> the image of an open set under a homeomorphism between open sets, hence open. So $W$ is open.
>
> *Uniqueness.* Let $\tau'$ be any topology in which every $TU$ is open and every $\tilde\varphi$ is a homeomorphism. If $W \in \tau'$, then $W \cap TU$ is open in $TU$, so $\tilde\varphi(W \cap TU)$ is open, and $W$ is open in the topology above. Conversely, if $W$ is open above, then each $W \cap TU = \tilde\varphi^{-1}\big(\tilde\varphi(W \cap TU)\big)$ is open in $TU$, hence in $\tau'$ since $TU \in \tau'$, and $W = \bigcup_U (W \cap TU) \in \tau'$.
>
> *Locally Euclidean.* Every point of $TM$ lies in some $TU$, which is open and homeomorphic, by $\tilde\varphi$, to an open subset of $\mathbb{R}^{2m}$.
>
> *Hausdorff.* Let $(p, v) \ne (q, w)$. If $p = q$, both points lie in one $TU$, homeomorphic to a subset of the Hausdorff space $\mathbb{R}^{2m}$; disjoint open sets of $TU$ separating them are open in $TM$, because $TU$ is. If $p \ne q$, choose charts with disjoint domains $U \ni p$ and $V \ni q$, possible because $M$ is Hausdorff (shrink the domains, [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10]]); then $TU$ and $TV$ are disjoint open sets containing the two points.
>
> *Second countable.* Let $\mathcal{B}$ be a countable basis of $M$. For each $B \in \mathcal{B}$ contained in some chart domain, choose one such chart $(U_B, \varphi_B)$. These countably many charts cover $M$: each $p$ lies in some chart domain $U$, and then in some $B \in \mathcal{B}$ with $p \in B \subseteq U$. So the countably many open sets $TU_B$ cover $TM$. Each is homeomorphic to an open subset of $\mathbb{R}^{2m}$, so has a countable basis, whose members are open in $TM$; the union of these countably many bases is countable and is a basis of $TM$, since any open $W \ni (p, v)$ meets some $TU_B$ containing $(p, v)$ in a set open in $TU_B$.

^pf-44-1

*Uses:* [[§44 The Tangent Bundle#^def-44-4|Def. §44.4]], [[§44 The Tangent Bundle#^prop-44-2|§44.2]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§2 Basis for a Topology#^def-2-1|590 Def. §2.1]], [[§9 Hausdorff Spaces#^def-9-1|590 Def. §9.1]], [[§22 Countability Axioms#^def-22-3|590 Def. §22.3]]

The same argument, word for word, builds the topology of the cotangent bundle ([[§45 The Cotangent Bundle|§45]]), with the dual bases in place of the coordinate bases.

> [!theorem] Proposition §44.2: The Smooth Atlas of $TM$
> The charts $(TU, \tilde\varphi)$, as $(U, \varphi)$ ranges over the smooth charts of $M$, form a smooth atlas on $TM$. For charts $\varphi = (x^i)$ and $\psi = (y^j)$ of $M$, the transition map is
>
> $$
> \tilde\psi \circ \tilde\varphi^{-1}(r, v) = \Big( \psi \circ \varphi^{-1}(r), \ \ \sum_{j=1}^m \frac{\partial y^1}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j, \ \ldots, \ \sum_{j=1}^m \frac{\partial y^m}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j \Big) .
> $$
>
> *Lee: Proposition 3.18*

^prop-44-2

> [!proof]+ Proof
> *(Lecture 13: “the only thing that I want to have a look at is … the transition functions of the atlas, because this is how people handle tangent vectors.” Completed here.)* The domain is $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$, open in $\mathbb{R}^{2m}$. Let $p \in U \cap V$ and $v \in T_pM$, written in both bases:
>
> $$
> v = \sum_j v^j \frac{\partial}{\partial x^j}\Big|_p = \sum_i w^i \frac{\partial}{\partial y^i}\Big|_p .
> $$
>
> The first component of the transition is $\psi \circ \varphi^{-1}$, smooth because the charts of $M$ are compatible. For the rest we need the $w$'s in terms of the $v$'s: “a change of basis formula from 217, which I always forget.” By the universal formula ([[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|Theorem §29.5]]), the $i$-th coefficient of a derivation $D$ in the basis $\partial/\partial y^i|_p$ is $D[y^i]$; applied to $D = \partial/\partial x^j|_p$ it gives
>
> $$
> \frac{\partial}{\partial x^j}\Big|_p = \sum_i \frac{\partial y^i}{\partial x^j}(p) \frac{\partial}{\partial y^i}\Big|_p, \qquad\text{so}\qquad w^i = \sum_j \frac{\partial y^i}{\partial x^j}(p)\, v^j ,
> $$
>
> comparing coefficients in the basis $\partial/\partial y^i|_p$. (In lecture Uribe expanded $\partial/\partial y^j$ in the other basis and first solved for the $v$'s — “I did it backwards” — then took the other direction “by the same argument”.) With $p = \varphi^{-1}(r)$ this is the displayed formula. The coefficients are smooth functions of $r$: by [[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1]], $\partial y^i/\partial x^j(\varphi^{-1}(r)) = \partial(\psi \circ \varphi^{-1})^i/\partial r^j(r)$, the entries of the Jacobian of the transition map of $M$. So the transition map of $TM$ is $(r, v) \mapsto \big(\psi \circ \varphi^{-1}(r), (\psi \circ \varphi^{-1})'(r)\, v\big)$, smooth.

^pf-44-2

*Uses:* [[§44 The Tangent Bundle#^def-44-4|Def. §44.4]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^def-17-6|Def. §17.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]

![[m591-17-3.svg]]
*The transition map of the charts $\tilde\varphi$ and $\tilde\psi$ of $TM$, as drawn in lecture over a point $(p, v)$ of $TU \cap TV$.*

> [!remark]- Connections
> - The same expansion of coordinate derivations: [[§30 The Differential in Coordinates#^cor-30-4|Change of Coordinates, §30.4]]; the Jacobian matrix in 452: [[§16 The Inverse Function Theorem#^def-16-1|452 Def. §16.1]]; change of basis: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].

The transition map of $TM$, in one line: the base point moves by the transition map of $M$, and the vector by its Jacobian. This is Uribe's identity at work once more — the partials $\partial y^i/\partial x^j$, taken upstairs on $M$, are the Jacobian downstairs.

> [!theorem] Corollary §44.3: The Tangent Bundle Is a Fibration
> With the smooth structure of [[§44 The Tangent Bundle#^prop-44-2|Proposition §44.2]]:
> 1. $TM$ is a smooth manifold of dimension $2m$, and $\pi : TM \to M$ is smooth;
> 2. the $\Phi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Phi$ restricts on the fibre $T_pM$ to a linear isomorphism $T_pM \to \{p\} \times \mathbb{R}^m$;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $TM$ of codimension $m$.
>
> With [[§44 The Tangent Bundle#^prop-44-1|Proposition §44.1]], this proves [[§44 The Tangent Bundle#^prop-44-4|Proposition §44.4]] below in full.

^cor-44-3

> [!proof]+ Proof
> *((1) and (2) are the lecture's observations — “in these coordinates, the projection is just projection onto the first $m$ components … so we get a beautiful fibration”; the details and (3) are filled in.)* (1) In the charts $\tilde\varphi$ and $\varphi$, $\pi$ is $(r, v) \mapsto r$, which is smooth. (2) $\Phi = (\varphi^{-1} \times \mathrm{id}) \circ \tilde\varphi$ is a composite of diffeomorphisms ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9]]), and $\mathrm{pr}_1 \circ \Phi = \pi$; the $TU$ cover $TM$, the $U$ cover $M$. On $T_pM$, $\Phi$ is $v \mapsto (p, v^1, \ldots, v^m)$, taking components in a basis, which is a linear isomorphism. (3) In the chart $\tilde\varphi$, $\zeta(M) \cap TU = \{v^1 = \cdots = v^m = 0\}$, so the charts $\tilde\varphi$ are adapted to $\zeta(M)$ ([[§35 Submanifolds#^def-35-2|Definition §35.2]]).

^pf-44-3

*Uses:* [[§44 The Tangent Bundle#^def-44-4|Def. §44.4]], [[§44 The Tangent Bundle#^prop-44-1|§44.1]], [[§44 The Tangent Bundle#^prop-44-2|§44.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-7|Def. §19.7]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§36 Fibrations#^def-36-1|Def. §36.1]], [[§35 Submanifolds#^def-35-1|Def. §35.1]], [[§35 Submanifolds#^def-35-2|Def. §35.2]], [[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]]

> [!theorem] Proposition §44.4: The Tangent Bundle Is a Manifold (Claim)
> $TM$ has a natural topology and smooth structure making it a smooth manifold of dimension $2m$, for which $\pi : TM \to M$ is a fibration with fibre $\mathbb{R}^m$, and the image $\zeta(M)$ of the zero section is a submanifold of $TM$.
>
> *Lee: Proposition 3.18*

^prop-44-4

> [!proof]+ Proof
> [[§44 The Tangent Bundle#^prop-44-1|Proposition §44.1]] gives the topology, and [[§44 The Tangent Bundle#^cor-44-3|Corollary §44.3]] the smooth structure, the fibration with fibre $\mathbb{R}^m$, and the zero section as a submanifold.

^pf-44-4

*Uses:* [[§44 The Tangent Bundle#^prop-44-1|§44.1]], [[§44 The Tangent Bundle#^prop-44-2|§44.2]], [[§44 The Tangent Bundle#^cor-44-3|§44.3]]

> [!remark] Remark: Vector Bundles
> $TM$ is in fact a *vector bundle*: a fibration whose fibres are vector spaces, with trivializations that are linear isomorphisms on each fibre. Uribe postponed the general definition — “it takes another 10 minutes of axioms” — but these are the two features: “the fibres are abstract vector spaces, and you can find trivializations which restrict to linear isomorphisms fibrewise.” Vector bundles are “fun objects” in their own right; K-theory is built from them.

^rem-44-2

> [!remark] Remark: Trivializations and Frames
> [[§36 Fibrations#^prop-36-4|Proposition §36.4]] turns local trivializations into local sections. For the tangent bundle the dictionary is between trivializations and *frames*: the trivialization $\Phi$ of a chart (Definition [[§44 The Tangent Bundle#^def-44-4|§44.4]]) corresponds to the $m$ local sections ([[§36 Fibrations#^def-36-3|Def. §36.3]]) $u \mapsto \partial/\partial x^i|_u$, since $\Phi^{-1}(u, e_i) = \partial/\partial x^i|_u$; for a vector bundle ([[§44 The Tangent Bundle#^rem-44-2|Rem. in §44]]) of rank $m$ one local section is not enough, and it takes $m$ sections that are linearly independent at every point (Lee, Example 10.18 and Proposition 10.19). For the Hopf fibration one section suffices because the fibre is a single orbit ([[§13 Group Actions and Orbit Spaces#^def-13-3|Def. §13.3]]) of the free $S^1$-action. That is the general pattern of *principal bundles*, where a group acts freely and transitively on each fibre; it is stated here, not proved.

^rem-44-3
