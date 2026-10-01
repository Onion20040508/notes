---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 17
tags: [differentiable-manifolds, math591]
---
← [[§16 Fibrations]] · ↑ [[· 5 Maps of Constant Rank and Bundles]] · [[§18 Immersions]] →

*Stage: bundles — All the tangent spaces of $M$, assembled into a single manifold that fibres over $M$.*

*Lecture 12. “Again, these constructions, especially the cotangent [bundle], are basic parts of the basic theory.” The tangent bundle was introduced as a set, with its projection and zero section; its topology, smooth structure and charts come next lecture.*

> [!definition] Definition §17.1: The Tangent Bundle as a Set
> Let $M$ be a smooth manifold of dimension $m$. Its **tangent bundle** is the set
>
> $$
> TM = \bigcup_{p \in M} \{p\} \times T_pM = \{\, (p, v) : p \in M,\ v \in T_pM \,\},
> $$
>
> all the tangent spaces “put together in one big set.” It comes with the **projection** $\pi : TM \to M$, $\pi(p, v) = p$, whose fibre $\pi^{-1}(p) = \{p\} \times T_pM$ is identified with $T_pM$; and with the **zero section** $\zeta : M \to TM$, $\zeta(p) = (p, 0)$, which is one-to-one because every tangent space has a distinguished element, its zero.
>
> *Lee: Ch. 3, The Tangent Bundle*

^def-17-1

> [!remark] Remark: The Picture Changes
> “There are several psychological inflection steps that one needs to make. The most important one is that we're going to think of $TM$ as fibering over $M$.” A tangent space is usually drawn touching $M$, lying along it. In the bundle picture it stands *vertically*, as the fibre over its point, and $M$ itself sits horizontally inside $TM$ as the zero section — the tangent spaces become “transversal” to it.

^rem-17-1

![[m591-17-1.svg]]
*The tangent bundle as a fibration. Each fibre $\pi^{-1}(p) = T_pM$ is a vertical line over $p$ (in general a copy of $\mathbb{R}^m$); the point $(p, v)$ lies on it, and the zero section $\zeta$ lifts each $p$ straight up to $(p, 0)$, placing a copy of $M$ horizontally inside $TM$.*

![[m591-17-6.svg]]
*$TS^1$ as a cylinder. Left: the usual picture, each tangent line touching the circle at its point. Right: the bundle picture of the remark — each tangent line $T_pS^1$ (red) stands upright over $p$, and the zero section $\zeta(S^1)$ (blue) runs around the waist. Here the bundle is a genuine product $S^1 \times \mathbb{R}$: two angle charts ([[§9 Manifolds in Euclidean Space#^prop-9-4|§9.4]]) differ by a constant on each piece of their overlap, so their coordinate vectors $\partial/\partial\theta$ agree, and $c\,\partial/\partial\theta|_p \mapsto (p, c)$ is a global trivialization. The green circle is the vector field $\partial/\partial\theta$ ([[§17 The Tangent Bundle#^def-17-4|Definition §17.4]]), a section that never meets the zero section.*

> [!theorem] Proposition §17.1: The Tangent Bundle Is a Manifold (Claim)
> $TM$ has a natural topology and smooth structure making it a smooth manifold of dimension $2m$, for which $\pi : TM \to M$ is a fibration with fibre $\mathbb{R}^m$, and the image $\zeta(M)$ of the zero section is a submanifold of $TM$.
>
> *Lee: Proposition 3.18*

^prop-17-1

*Uses:* [[§17 The Tangent Bundle#^prop-17-2|§17.2]], [[§17 The Tangent Bundle#^prop-17-3|§17.3]], [[§17 The Tangent Bundle#^cor-17-4|§17.4]]

*Status.* Stated in Lecture 12 — “the claim, which takes a lot of detail to prove” — and made precise in Lecture 13 ([[§17 The Tangent Bundle#Trivializations and Charts|Trivializations and Charts]]), which wrote down the charts. Their idea was given: a chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ gives the basis $\partial/\partial x^i|_p$ of every $T_pM$, $p \in U$, hence an identification of each of these tangent spaces with $\mathbb{R}^m$; “putting all that together gives us a map” $\pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}$, the chart of $TM$. The dimension $2m$ is $m$ coordinates for the point and $m$ for the vector.

## Trivializations and Charts

*Lecture 13. “Back to the tangent bundle.” $TM$ has been defined as a set; its charts come from charts of $M$ and the coordinate bases.*

> [!definition] Definition §17.2: Trivializations and Charts of $TM$
> Let $(U, \varphi = (x^1, \ldots, x^m))$ be a smooth chart of $M$, and $TU = \pi^{-1}(U) = \{(p, v) \in TM : p \in U\}$, the tangent vectors at points of $U$. The **local trivialization** over $U$ is
>
> $$
> \Phi : TU \longrightarrow U \times \mathbb{R}^m, \qquad \Phi(p, v) = (p, v^1, \ldots, v^m), \qquad \text{where } v = \sum_{i=1}^m v^i \frac{\partial}{\partial x^i}\Big|_p ,
> $$
>
> the components of $v$ in the coordinate basis ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|Theorem §12.16]]); and the **chart** of $TM$ is
>
> $$
> \tilde\varphi = (\varphi \times \mathrm{id}) \circ \Phi : TU \longrightarrow \varphi(U) \times \mathbb{R}^m \subseteq \mathbb{R}^{2m}, \qquad (p, v) \longmapsto \big(x^1(p), \ldots, x^m(p), v^1, \ldots, v^m\big).
> $$
>
> Both are bijections, with inverse $(r, v) \mapsto \big(\varphi^{-1}(r), \sum_i v^i\, \partial/\partial x^i|_{\varphi^{-1}(r)}\big)$ for $\tilde\varphi$; and $\mathrm{pr}_1 \circ \Phi = \pi$ — “that's why I call it a trivialization.”
>
> *Lee: Proposition 3.18*

^def-17-2

![[m591-17-2.svg]]
*The trivialization and the chart, as on the board. The triangle commutes, $\mathrm{pr}_1 \circ \Phi = \pi$ — the fibration diagram of [[§16 Fibrations#^def-16-1|Definition §16.1]] — and the chart $\tilde\varphi$ is $\Phi$ followed by $\varphi$ on the first factor.*

> [!theorem] Proposition §17.2: The Topology of $TM$
> There is a unique topology on $TM$ for which every $TU$ is open and every chart $\tilde\varphi : TU \to \varphi(U) \times \mathbb{R}^m$ is a homeomorphism. With it, $TM$ is a topological manifold of dimension $2m$.
>
> *Lee: Lemma 1.35 and Proposition 3.18*

^prop-17-2

> [!proof]+ Proof
> *(Stated in Lecture 13 without proof — “it's all point-set topology, and of course everything is in Lee … see Lee”; filled in, following Lee's smooth manifold chart lemma.)* Throughout, $(U, \varphi)$ and $(V, \psi)$ denote smooth charts of $M$.
>
> *The transition maps.* The computation in the proof of [[§17 The Tangent Bundle#^prop-17-3|Proposition §17.3]] below uses only the definitions of the charts, not any topology on $TM$. It shows that $\tilde\psi \circ \tilde\varphi^{-1}$ maps the open set $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$ bijectively onto the open set $\psi(U \cap V) \times \mathbb{R}^m$, by a smooth map whose inverse, $\tilde\varphi \circ \tilde\psi^{-1}$, is given by the same formula with the two charts exchanged. So each transition map is a homeomorphism between open subsets of $\mathbb{R}^{2m}$.
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
> *Hausdorff.* Let $(p, v) \ne (q, w)$. If $p = q$, both points lie in one $TU$, homeomorphic to a subset of the Hausdorff space $\mathbb{R}^{2m}$; disjoint open sets of $TU$ separating them are open in $TM$, because $TU$ is. If $p \ne q$, choose charts with disjoint domains $U \ni p$ and $V \ni q$, possible because $M$ is Hausdorff (shrink the domains, [[§2 Topological Manifolds#^lem-2-11|Lemma §2.11]]); then $TU$ and $TV$ are disjoint open sets containing the two points.
>
> *Second countable.* Let $\mathcal{B}$ be a countable basis of $M$. For each $B \in \mathcal{B}$ contained in some chart domain, choose one such chart $(U_B, \varphi_B)$. These countably many charts cover $M$: each $p$ lies in some chart domain $U$, and then in some $B \in \mathcal{B}$ with $p \in B \subseteq U$. So the countably many open sets $TU_B$ cover $TM$. Each is homeomorphic to an open subset of $\mathbb{R}^{2m}$, so has a countable basis, whose members are open in $TM$; the union of these countably many bases is countable and is a basis of $TM$, since any open $W \ni (p, v)$ meets some $TU_B$ containing $(p, v)$ in a set open in $TU_B$.

^pf-17-2

*Uses:* [[§17 The Tangent Bundle#^def-17-2|Def. §17.2]], [[§17 The Tangent Bundle#^prop-17-3|§17.3]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§2 Topological Manifolds#^def-2-1|Def. §2.1]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^lem-2-11|§2.11]], [[§2 Basis for a Topology#^def-2-1|590 §2.1]], [[§8 Hausdorff Spaces#^def-8-1|590 §8.1]], [[§18 Countability Axioms#^def-18-3|590 §18.3]]

The same argument, word for word, builds the topology of the cotangent bundle ([[§17 The Tangent Bundle#The Cotangent Bundle|The Cotangent Bundle]]), with the dual bases in place of the coordinate bases.

> [!theorem] Proposition §17.3: The Smooth Atlas of $TM$
> The charts $(TU, \tilde\varphi)$, as $(U, \varphi)$ ranges over the smooth charts of $M$, form a smooth atlas on $TM$. For charts $\varphi = (x^i)$ and $\psi = (y^j)$ of $M$, the transition map is
>
> $$
> \tilde\psi \circ \tilde\varphi^{-1}(r, v) = \Big( \psi \circ \varphi^{-1}(r), \ \ \sum_{j=1}^m \frac{\partial y^1}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j, \ \ldots, \ \sum_{j=1}^m \frac{\partial y^m}{\partial x^j}\big(\varphi^{-1}(r)\big)\, v^j \Big) .
> $$
>
> *Lee: Proposition 3.18*

^prop-17-3

> [!proof]+ Proof
> *(Lecture 13: “the only thing that I want to have a look at is … the transition functions of the atlas, because this is how people handle tangent vectors.” Completed here.)* The domain is $\tilde\varphi(TU \cap TV) = \varphi(U \cap V) \times \mathbb{R}^m$, open in $\mathbb{R}^{2m}$. Let $p \in U \cap V$ and $v \in T_pM$, written in both bases:
>
> $$
> v = \sum_j v^j \frac{\partial}{\partial x^j}\Big|_p = \sum_i w^i \frac{\partial}{\partial y^i}\Big|_p .
> $$
>
> The first component of the transition is $\psi \circ \varphi^{-1}$, smooth because the charts of $M$ are compatible. For the rest we need the $w$'s in terms of the $v$'s: “a change of basis formula from 217, which I always forget.” By the universal formula ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|Theorem §12.16]]), the $i$-th coefficient of a derivation $D$ in the basis $\partial/\partial y^i|_p$ is $D[y^i]$; applied to $D = \partial/\partial x^j|_p$ it gives
>
> $$
> \frac{\partial}{\partial x^j}\Big|_p = \sum_i \frac{\partial y^i}{\partial x^j}(p) \frac{\partial}{\partial y^i}\Big|_p, \qquad\text{so}\qquad w^i = \sum_j \frac{\partial y^i}{\partial x^j}(p)\, v^j ,
> $$
>
> comparing coefficients in the basis $\partial/\partial y^i|_p$. (In lecture Uribe expanded $\partial/\partial y^j$ in the other basis and first solved for the $v$'s — “I did it backwards” — then took the other direction “by the same argument”.) With $p = \varphi^{-1}(r)$ this is the displayed formula. The coefficients are smooth functions of $r$: by [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|Proposition §12.21]], $\partial y^i/\partial x^j(\varphi^{-1}(r)) = \partial(\psi \circ \varphi^{-1})^i/\partial r^j(r)$, the entries of the Jacobian of the transition map of $M$. So the transition map of $TM$ is $(r, v) \mapsto \big(\psi \circ \varphi^{-1}(r), (\psi \circ \varphi^{-1})'(r)\, v\big)$, smooth.

^pf-17-3

*Uses:* [[§17 The Tangent Bundle#^def-17-2|Def. §17.2]], [[§8 Differentiable Structures#^def-8-4|Def. §8.4]], [[§8 Differentiable Structures#^def-8-6|Def. §8.6]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^thm-12-16|§12.16]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-21|§12.21]], [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]]

![[m591-17-3.svg]]
*The transition map of the charts $\tilde\varphi$ and $\tilde\psi$ of $TM$, as drawn in lecture over a point $(p, v)$ of $TU \cap TV$.*

> [!remark]- Connections
> - The same expansion of coordinate derivations: [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-24|Change of Coordinates, §12.24]]; the Jacobian matrix in 452: [[§13 The Inverse Function Theorem#^def-13-1|452 §13.1]]; change of basis: [[§10 Invertibility and Isomorphisms#^ladr-3-84|LADR 3.84]].

The transition map of $TM$, in one line: the base point moves by the transition map of $M$, and the vector by its Jacobian. This is Uribe's identity at work once more — the partials $\partial y^i/\partial x^j$, taken upstairs on $M$, are the Jacobian downstairs.

> [!theorem] Corollary §17.4: The Tangent Bundle Is a Fibration
> With the smooth structure of [[§17 The Tangent Bundle#^prop-17-3|Proposition §17.3]]:
> 1. $TM$ is a smooth manifold of dimension $2m$, and $\pi : TM \to M$ is smooth;
> 2. the $\Phi$ are local trivializations, so $\pi$ is a fibration with fibre $\mathbb{R}^m$, and each $\Phi$ restricts on the fibre $T_pM$ to a linear isomorphism $T_pM \to \{p\} \times \mathbb{R}^m$;
> 3. the image $\zeta(M)$ of the zero section is a submanifold of $TM$ of codimension $m$.
>
> With [[§17 The Tangent Bundle#^prop-17-2|Proposition §17.2]], this proves [[§17 The Tangent Bundle#^prop-17-1|Proposition §17.1]] in full.

^cor-17-4

> [!proof]+ Proof
> *((1) and (2) are the lecture's observations — “in these coordinates, the projection is just projection onto the first $m$ components … so we get a beautiful fibration”; the details and (3) are filled in.)* (1) In the charts $\tilde\varphi$ and $\varphi$, $\pi$ is $(r, v) \mapsto r$, which is smooth. (2) $\Phi = (\varphi^{-1} \times \mathrm{id}) \circ \tilde\varphi$ is a composite of diffeomorphisms ([[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|Proposition §12.14]]), and $\mathrm{pr}_1 \circ \Phi = \pi$; the $TU$ cover $TM$, the $U$ cover $M$. On $T_pM$, $\Phi$ is $v \mapsto (p, v^1, \ldots, v^m)$, taking components in a basis, which is a linear isomorphism. (3) In the chart $\tilde\varphi$, $\zeta(M) \cap TU = \{v^1 = \cdots = v^m = 0\}$, so the charts $\tilde\varphi$ are adapted to $\zeta(M)$ ([[§15 Submanifolds#^def-15-1|Definition §15.1]]).

^pf-17-4

*Uses:* [[§17 The Tangent Bundle#^def-17-2|Def. §17.2]], [[§17 The Tangent Bundle#^prop-17-2|§17.2]], [[§17 The Tangent Bundle#^prop-17-3|§17.3]], [[§8 Differentiable Structures#^def-8-14|Def. §8.14]], [[§8 Differentiable Structures#^def-8-17|Def. §8.17]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-14|§12.14]], [[§16 Fibrations#^def-16-1|Def. §16.1]], [[§15 Submanifolds#^def-15-1|Def. §15.1]], [[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]]

> [!remark] Remark: Vector Bundles
> $TM$ is in fact a *vector bundle*: a fibration whose fibres are vector spaces, with trivializations that are linear isomorphisms on each fibre. Uribe postponed the general definition — “it takes another 10 minutes of axioms” — but these are the two features: “the fibres are abstract vector spaces, and you can find trivializations which restrict to linear isomorphisms fibrewise.” Vector bundles are “fun objects” in their own right; K-theory is built from them.

^rem-17-2

## Sections and Vector Fields

> [!definition] Definition §17.3: Section
> Let $\pi : E \to B$ be a fibration. A **section** of $\pi$ is a smooth map $s : B \to E$ with $\pi \circ s = \mathrm{id}_B$: “if you first go up and then down, you get the identity on the base.” It picks, smoothly in $b$, one point $s(b)$ of each fibre $\pi^{-1}(b)$.
>
> *Lee: Ch. 10, Sections of Vector Bundles*

^def-17-3

![[m591-17-4.svg]]
*$\pi \circ s = \mathrm{id}_B$. A section goes up, the projection comes down, and the round trip is the identity on the base.*

![[m591-17-5.svg]]
*The cartoon of a section. The fibration is drawn as a box over its base, with fibres vertical; a section is a graph over the base, meeting every fibre exactly once — at $s(b)$ in the fibre over $b$ — so its image $s(B)$ is “a copy of $B$” inside $E$.*

> [!remark] Remark: Sections Need Not Exist
> “A fact”: the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ of [[§16 Fibrations#^ex-16-1|Example §16.1]] — “the fibration that you're working with in homework” — has no continuous section, for $n \ge 1$. (For $n = 0$ the base is a single point.) This is stated, not proved, here; a proof uses the fundamental group. A vector bundle, by contrast, always has sections — the zero section at least — and in fact “a very infinite-dimensional space” of them.

^rem-17-3

> [!definition] Definition §17.4: Vector Field
> A **vector field** on $M$ is a section of the tangent bundle $\pi : TM \to M$: a smooth map $X : M \to TM$ with $X(p) \in T_pM$ for every $p$ — “for every point, [it] selects a tangent vector at that point.”
>
> *Lee: Ch. 8, Vector Fields*

^def-17-4

> [!remark]- Connections
> - Vector fields on open subsets of $\mathbb{R}^3$ in 452: [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §11]].

**Transcription note.** Page 36 of the handwritten notes writes “Section of $TM \xrightarrow{F} M$”; the map is the projection $\pi$.

## The Cotangent Bundle

> [!definition] Definition §17.5: The Cotangent Bundle
> The **cotangent bundle** of $M$ is
>
> $$
> T^*M = \bigcup_{p \in M} \{p\} \times T_p^*M,
> $$
>
> with projection $\pi(p, \xi) = p$. For a chart $(U, \varphi = (x^i))$ of $M$, its chart is $(p, \xi) \mapsto (x^1(p), \ldots, x^m(p), \xi_1, \ldots, \xi_m)$, where $\xi = \sum_i \xi_i\, dx^i|_p$ in the dual basis ([[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1|Definition §13.1]]).
>
> *Lee: Proposition 11.9*

^def-17-5

> [!remark]- Connections
> - The fibre $T_p^*M$ is a dual space, [[§12 Duality#^ladr-3-110|LADR 3.110]], and the chart uses the dual basis, [[§12 Duality#^ladr-3-112|LADR 3.112]]. Counterpart in 452: differential forms on $\mathbb{R}^n$, [[§21 Introduction to Differential Forms#^def-21-1|452 §21.1]].

> [!theorem] Proposition §17.5: The Cotangent Transition Maps
> For charts $\varphi = (x^i)$ and $\psi = (y^j)$, if $\xi = \sum_i \xi_i\, dx^i|_p = \sum_j \eta_j\, dy^j|_p$, then
>
> $$
> dx^i|_p = \sum_j \frac{\partial x^i}{\partial y^j}(p)\, dy^j|_p, \qquad \eta_j = \sum_i \frac{\partial x^i}{\partial y^j}(p)\, \xi_i .
> $$
>
> So the covector components transform by the transpose of the inverse of the matrix that transforms tangent components, and the charts of $T^*M$ form a smooth atlas making $\pi : T^*M \to M$ a vector bundle with fibre $\mathbb{R}^m$.
>
> *Lee: Proposition 11.9*

^prop-17-5

> [!proof]+ Proof
> *(Lecture 13: “completely analogous”, with the change “we use the dual basis”, and the formula for $dx^i$ given; the rest is filled in.)* The formula for $dx^i|_p$ is [[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2|Lemma §13.2]] applied to the function $x^i$ in the chart $\psi$. Substituting it into $\sum_i \xi_i\, dx^i|_p$ and comparing coefficients of $dy^j|_p$ gives $\eta_j$. The matrix $\big[\partial x^i/\partial y^j\big]$ is the inverse of $\big[\partial y^i/\partial x^j\big]$ (chain rule), so the tangent components transform by $A = \big[\partial y^i/\partial x^j\big]$ and the covector components by $(A^{-1})^{\mathsf T}$. Its entries are smooth functions of the base point, so the transition maps are smooth, as in [[§17 The Tangent Bundle#^prop-17-3|Proposition §17.3]]; the fibration and linearity statements follow as in [[§17 The Tangent Bundle#^cor-17-4|Corollary §17.4]].

^pf-17-5

*Uses:* [[§17 The Tangent Bundle#^def-17-5|Def. §17.5]], [[§13 Tangent Spaces III꞉ The Cotangent Space#^def-13-1|Def. §13.1]], [[§13 Tangent Spaces III꞉ The Cotangent Space#^lem-13-2|§13.2]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^cor-12-23|§12.23]], [[§17 The Tangent Bundle#^prop-17-3|§17.3]], [[§17 The Tangent Bundle#^cor-17-4|§17.4]], [[Multivariable Chain Rule|452 §10.2]], [[§12 Duality#^ladr-3-132|LADR 3.132]]

> [!remark]- Connections
> - The matrix of a dual map in dual bases is the transpose: [[§12 Duality#^ladr-3-132|LADR 3.132]].

“We'll see that the cotangent bundle has a natural structure that the tangent bundle doesn't have.” $TM$ and $T^*M$ are isomorphic as vector bundles, “but not naturally isomorphic — we have to make choices to construct an isomorphism” (a metric, for instance, as in the [[§15 Submanifolds#^rem-15-1|remark on conormal spaces]]). This is stated, not proved, here.
