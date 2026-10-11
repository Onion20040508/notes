---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 37
tags: [differentiable-manifolds, math591]
---
← [[§36 Submersions]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§38 Fibrations]] →

*Stage: submanifolds — Subsets of a manifold that are locally coordinate slices — the equations thread, completed.*

*References: Lee Ch. 5. Lecture 12.*

The subsets of a manifold that look locally like $\mathbb{R}^{m-k} \subseteq \mathbb{R}^m$. The regular value theorem for manifolds, proved from the submersion normal form of [[§36 Submersions|§36]], produces them as level sets — the end of the equations thread that began in [[§7 The Regular Value Theorem|§7]].

## Open Submanifolds

*(Not from lecture.)* Which subsets of a smooth manifold $M$ inherit a smooth structure from $M$? An arbitrary subset with the subspace topology need not even be a manifold — $\mathbb{Q} \subseteq \mathbb{R}$ is not locally Euclidean (the remark *What Subspaces Do Not Inherit* in [[§3 Subspaces and Products#^rem-3-3|§3]]) — and when it is a lower-dimensional one, the charts of $M$ do not restrict to charts of it: for a chart $(U, \varphi)$, the set $\varphi(U \cap S)$ is in general not open in $\mathbb{R}^m$ (for the circle in $\mathbb{R}^2$ it is a piece of a curve). Open subsets are the easy case: the charts of $M$ simply restrict (Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]]). Regular submanifolds, in the rest of this section, are the general answer, and the two meet in codimension $0$ (Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]]).

> [!definition] Definition §37.1: Open Submanifold of a Smooth Manifold
> An **open submanifold** of a smooth manifold $M$ is an open subset $S \subseteq M$ with the subspace topology and the smooth structure of Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]], whose charts are the smooth charts of $M$ with domain in $S$. It is the smooth counterpart of Definition [[§3 Subspaces and Products#^def-3-2|§3.2]]; its inclusion into $M$ is smooth, and maps into $S$ are smooth exactly when they are smooth into $M$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-5|§19.5]]).

^def-37-1

> [!theorem] Proposition §37.1: Open Subsets of a Product
> Let $M_1$, $M_2$ be smooth manifolds and $U \subseteq M_1$ open. Then $U \times M_2$ is open in $M_1 \times M_2$, and the open submanifold $U \times M_2$ of $M_1 \times M_2$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]) is the same smooth manifold as the product manifold $U \times M_2$ of the open submanifold $U$ with $M_2$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]). In particular the projection $\mathrm{pr}_1 : U \times M_2 \to U$ is the restriction to $U \times M_2$ of the projection $\mathrm{pr}_1 : M_1 \times M_2 \to M_1$ (Definition [[§3 Subspaces and Products#^def-3-4|§3.4]]).

^prop-37-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Open.* $U \times M_2 = \mathrm{pr}_1^{-1}(U)$, open because $\mathrm{pr}_1$ is continuous (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]).
>
> *Same topology.* The product topology of $U \times M_2$ has the basis of sets $A' \times B$ with $A'$ open in $U$ and $B$ open in $M_2$ (Definition [[§3 Subspaces and Products#^def-3-3|§3.3]]); since $U$ is open, the sets $A'$ open in $U$ are the sets $A \cap U$ with $A$ open in $M_1$. The subspace topology of $U \times M_2$ in $M_1 \times M_2$ has the basis of sets $(A \times B) \cap (U \times M_2) = (A \cap U) \times B$. The two bases are the same, so the topologies agree.
>
> *Same smooth structure.* A product chart of $U \times M_2$ is $(U_1 \times U_2, \varphi_1 \times \varphi_2)$ with $(U_1, \varphi_1)$ a smooth chart of the open submanifold $U$ and $(U_2, \varphi_2)$ one of $M_2$. By Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]](2), $(U_1, \varphi_1)$ is a smooth chart of $M_1$ with $U_1 \subseteq U$, so $(U_1 \times U_2, \varphi_1 \times \varphi_2)$ is a product chart of $M_1 \times M_2$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]]) with domain in $U \times M_2$ — a smooth chart of the open submanifold $U \times M_2$, by Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]](2) again. So the product charts of $U \times M_2$, an atlas generating its product structure, all lie in the smooth structure of the open submanifold; by the uniqueness in Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] the two smooth structures are equal.
>
> *The projection.* Both maps send $(b, y)$ to $b$.

^pf-37-1

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§17 Differentiable Structures#^prop-17-6|§17.6]], [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

## Regular Submanifolds

*Lecture 12 (Mon Sep 28). “I know we're in the middle of discussing submersions and fibrations, but we need the notion of submanifold. So let's pause to discuss that. It's not difficult.” The local model is a lower-dimensional Euclidean space inside a higher-dimensional one: $\mathbb{R}^{m-k} \subseteq \mathbb{R}^m$ as the points whose last $k$ coordinates vanish, $x \mapsto (x, \vec 0)$.*

> [!definition] Definition §37.2: Regular Submanifold
> Let $M$ be a smooth manifold of dimension $m$, $S \subseteq M$ a subset with the subspace topology, and $0 \le k \le m$. For a chart $\varphi = (x^1, \ldots, x^m)$ write $x_a = (x^1, \ldots, x^{m-k})$ for its first $m - k$ components and $x_b = (x^{m-k+1}, \ldots, x^m)$ for its last $k$. Then $S$ is a **regular submanifold of $M$ of codimension $k$** if every $p \in S$ lies in the domain of a smooth chart $(U, \varphi)$ of $M$ with
>
> $$
> U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\}.
> $$
>
> Regular submanifolds are also called **embedded** submanifolds, as opposed to the [[§41 Embeddings#^def-41-4|immersed submanifolds]] of [[§41 Embeddings#^def-41-4|Definition §41.4]]. In these notes, “submanifold” without qualification means a regular submanifold.
>
> *Lee: Theorem 5.8*

^def-37-2

> [!remark]- Connections
> - The other kind of submanifold: [[§41 Embeddings#^def-41-4|immersed submanifolds, Def. §41.4]]; when an immersed submanifold is regular: [[§41 Embeddings#^prop-41-15|§41.15]]; local images of immersions: [[§40 Immersions#^cor-40-2|§40.2]].
> - Codimension in the Euclidean setting: [[§26 Transversality#^def-26-1|Def. §26.1]].
> - The geometric stage: in $\mathbb{R}^{n+k}$ the submanifolds are exactly the manifolds of [[§20 Manifolds in Euclidean Space|§20]] — the external, internal and graph descriptions ([[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]) — and the slice of this definition is a fourth: [[§37 Regular Submanifolds#^prop-37-8|§37.8]].
> - Their tangent spaces: $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) is $\iota_{\ast p}(T_pX)$ ([[§37 Regular Submanifolds#^rem-37-2|Remark: The Tangent Spaces Match]], [[§37 Regular Submanifolds#^prop-37-11|§37.11]]).

> [!definition] Definition §37.3: Adapted Chart
> Let $M$, $S$ and $k$ be as in [[§37 Regular Submanifolds#^def-37-2|Definition §37.2]]. Such charts — smooth charts $(U, \varphi)$ of $M$ with $U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\}$ — are **adapted** to $S$; “a random chart of $M$ is not adapted.” In an adapted chart, $U \cap S$ is cut out by the $k$ equations $x^{m-k+1} = \cdots = x^m = 0$, exactly as in the local model.
>
> *Lee: Theorem 5.8*

^def-37-3

> [!remark]- Connections
> - In Euclidean space an adapted chart comes from a graph chart ([[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) by straightening the graph: [[§37 Regular Submanifolds#^prop-37-8|§37.8]] and its figure.

> [!theorem] Proposition §37.2: Two Observations on Adapted Charts
> Let $(U, \varphi)$ be a smooth chart of $M$, and suppose that $U \cap S$ is cut out in it by setting some $k$ of the coordinates equal to constants:
>
> $$
> U \cap S = \{\, q \in U : x^{i_1}(q) = c_1, \ \ldots, \ x^{i_k}(q) = c_k \,\}.
> $$
>
> Then there is an adapted chart with the same domain $U$. That is:
> 1. the value $\vec 0$ in the definition may be replaced by any constant vector $\vec c$;
> 2. the last $k$ coordinates may be replaced by any $k$ of them.

^prop-37-2

> [!proof]+ Proof
> *(Lecture 12: “obvious observations”; filled in.)* Let $P : \mathbb{R}^m \to \mathbb{R}^m$ be the permutation of coordinates that moves positions $i_1, \ldots, i_k$ to the last $k$ places, and $T(r) = r - (\vec 0, \vec c)$. Explicitly, if $j_1 < \cdots < j_{m-k}$ are the remaining indices,
>
> $$
> P(r) = \big(r^{j_1}, \ldots, r^{j_{m-k}}, r^{i_1}, \ldots, r^{i_k}\big), \qquad T(s) = \big(s^1, \ldots, s^{m-k}, s^{m-k+1} - c_1, \ldots, s^m - c_k\big).
> $$
>
> Then $A = T \circ P$ is an affine diffeomorphism of $\mathbb{R}^m$, with inverse $A^{-1}(s) = P^{-1}\big(s + (\vec 0, \vec c)\big)$, so $(U, A \circ \varphi)$ is a smooth chart: a chart by Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]], whose transition maps with any smooth chart are those of $\varphi$ composed with $A$ or $A^{-1}$, hence smooth. In detail: $A$ is a homeomorphism of $W = \mathbb{R}^m \supseteq \varphi(U)$ onto $\mathbb{R}^m$, so Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](2) applies; and for a smooth chart $(V, \chi)$ of $M$ the transition maps are
>
> $$
> (A \circ \varphi) \circ \chi^{-1} = A \circ (\varphi \circ \chi^{-1}), \qquad \chi \circ (A \circ \varphi)^{-1} = (\chi \circ \varphi^{-1}) \circ A^{-1},
> $$
>
> composites of smooth maps, and inverse to each other; so $(U, A \circ \varphi)$ is compatible with every smooth chart and lies in the maximal atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). Its last $k$ coordinates are $x^{i_1} - c_1, \ldots, x^{i_k} - c_k$, which vanish exactly on $U \cap S$: for $q \in U$,
>
> $$
> (A \circ \varphi)(q) = \big(x^{j_1}(q), \ldots, x^{j_{m-k}}(q),\ x^{i_1}(q) - c_1, \ldots, x^{i_k}(q) - c_k\big),
> $$
>
> and its last $k$ entries are all $0$ if and only if $x^{i_l}(q) = c_l$ for $l = 1, \ldots, k$, that is (by hypothesis), if and only if $q \in U \cap S$. So $(U, A \circ \varphi)$ is adapted (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]). Observation (1) is the case $(i_1, \ldots, i_k) = (m-k+1, \ldots, m)$, where $P$ is the identity; observation (2) is the case $\vec c = \vec 0$, where $T$ is the identity.

^pf-37-2

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

> [!theorem] Proposition §37.3: The Induced Smooth Structure
> Let $S \subseteq M$ be a regular submanifold of codimension $k$. For each adapted chart $(U, \varphi = (x_a, x_b))$ put
>
> $$
> \varphi_S = x_a|_{U \cap S} : U \cap S \longrightarrow \mathbb{R}^{m-k}.
> $$
>
> Then:
> 1. $U \cap S$ is open in $S$, and $\varphi_S$ is a homeomorphism onto an open subset of $\mathbb{R}^{m-k}$;
> 2. the charts $(U \cap S, \varphi_S)$, over all adapted charts, form a smooth atlas $\mathcal{A}_S$ on $S$.
>
> So $S$ is a topological manifold of dimension $m - k$, and with the smooth structure generated by $\mathcal{A}_S$ it is a smooth manifold — “a manifold in its own right.”
>
> *Lee: Theorem 5.8*

^prop-37-3

> [!proof]+ Proof
> *(Lecture 12 claimed (1) — “easy to check” — and gave the reason for (2); completed here.)* $S$ is Hausdorff and second countable as a subspace of $M$ (Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]) — “back to week one of the class.” Let $j : \mathbb{R}^{m-k} \to \mathbb{R}^m$, $j(r) = (r, \vec 0)$, and $\mathrm{pr} : \mathbb{R}^m \to \mathbb{R}^{m-k}$, $\mathrm{pr}(r, s) = r$. Both are linear, hence smooth, and $\mathrm{pr} \circ j = \mathrm{id}$; also $x_a = \mathrm{pr} \circ \varphi$ on $U$, so $\varphi_S = \mathrm{pr} \circ \varphi|_{U \cap S}$.
>
> (1) $U \cap S$ is open in $S$ by the definition of the subspace topology, $U$ being open in $M$. Since $U \cap S = \{x_b = \vec 0\}$, the chart $\varphi$ maps $U \cap S$ bijectively onto $\varphi(U) \cap j(\mathbb{R}^{m-k}) = j(W)$, where $W = j^{-1}(\varphi(U))$ is open in $\mathbb{R}^{m-k}$ because $j$ is continuous. Indeed, for $q \in U$: $q \in S$ iff the last $k$ entries of $\varphi(q)$ vanish iff $\varphi(q) \in j(\mathbb{R}^{m-k})$; so $\varphi(U \cap S) = \varphi(U) \cap j(\mathbb{R}^{m-k})$, and a point $j(r)$ lies in $\varphi(U)$ exactly when $r \in W$. So $\varphi_S = \mathrm{pr} \circ \varphi|_{U \cap S}$ is a continuous bijection $U \cap S \to W$, with continuous inverse $r \mapsto \varphi^{-1}(j(r))$. In detail: $\varphi_S$ is continuous as a composite of continuous maps; $r \mapsto \varphi^{-1}(j(r))$ is continuous $W \to U$, with values in $U \cap S$ because $j(r) \in \varphi(U \cap S)$, hence continuous into the subspace $U \cap S$; and the two maps are inverse to each other,
>
> $$
> \varphi_S\big(\varphi^{-1}(j(r))\big) = \mathrm{pr}\big(j(r)\big) = r, \qquad \varphi^{-1}\big(j(\varphi_S(q))\big) = \varphi^{-1}\big(j(\mathrm{pr}(\varphi(q)))\big) = \varphi^{-1}\big(\varphi(q)\big) = q ,
> $$
>
> the last because $\varphi(q) = (x_a(q), \vec 0) = j(\mathrm{pr}(\varphi(q)))$ for $q \in U \cap S$. So $\varphi_S$ is a homeomorphism of the open set $U \cap S$ of $S$ onto the open set $W$ of $\mathbb{R}^{m-k}$; as every point of $S$ lies in an adapted chart, $S$ is locally Euclidean of dimension $m - k$, and with the first paragraph it is a topological manifold of dimension $m - k$.
>
> (2) Every point of $S$ lies in an adapted chart, so the domains cover $S$. For adapted charts $(U, \varphi)$ and $(V, \psi)$, since $\varphi_S^{-1} = \varphi^{-1} \circ j$,
>
> $$
> \psi_S \circ \varphi_S^{-1} = \mathrm{pr} \circ (\psi \circ \varphi^{-1}) \circ j \qquad \text{on } \varphi_S(U \cap V \cap S) = j^{-1}\big(\varphi(U \cap V)\big) .
> $$
>
> Here $\psi_S = \mathrm{pr} \circ \psi$ on $V \cap S$ gives the formula, and the domain is computed as in (1) with the open set $U \cap V$ in place of $U$ (the restriction of $\varphi$ to $U \cap V$ is again adapted). This is the transition map of $M$, which is smooth, composed with the linear maps $j$ and $\mathrm{pr}$: the transition maps of $S$ are “restrictions to $\mathbb{R}^{m-k}$ of $C^\infty$ maps between open sets of $\mathbb{R}^m$.” Exchanging the roles of the two charts, $\varphi_S \circ \psi_S^{-1} = \mathrm{pr} \circ (\varphi \circ \psi^{-1}) \circ j$ is smooth as well, and the two transition maps are inverse to each other; so they are diffeomorphisms, and any two charts of $\mathcal{A}_S$ are compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]). Thus $\mathcal{A}_S$ is a smooth atlas, and it generates a smooth structure (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).

^pf-37-3

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

> [!theorem] Proposition §37.4: Open Submanifolds Are the Regular Submanifolds of Codimension 0
> Let $M$ be a smooth $m$-manifold and $S \subseteq M$.
>
> 1. If $S$ is open, it is a regular submanifold of codimension $0$, and its induced smooth structure (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]) is that of the open submanifold $S$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]).
> 2. Conversely, a regular submanifold of codimension $0$ is open in $M$.

^prop-37-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* For $k = 0$ the chart has no last coordinates: $x_a = \varphi$ and $x_b$ is empty, so the condition $x_b(q) = \vec 0$ in Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] holds for every $q$. A chart $(U, \varphi)$ is therefore adapted to $S$ with $k = 0$ exactly when $U \cap S = U$, that is, when $U \subseteq S$.
>
> *(1)* Let $S$ be open and $p \in S$. For a smooth chart $(U, \varphi)$ of $M$ at $p$, its restriction $(U \cap S, \varphi|_{U \cap S})$ is a smooth chart of $M$ (Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]](2)) with domain inside $S$, hence adapted with $k = 0$. So $S$ is a regular submanifold of codimension $0$. The induced chart of an adapted chart $(U, \varphi)$ with $U \subseteq S$ is $\varphi_S = x_a|_{U \cap S} = \varphi$, the chart itself; so the atlas $\mathcal{A}_S$ of Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] consists of the smooth charts of $M$ with domain in $S$, which generate the open-submanifold structure (Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]](2)). The two smooth structures are therefore equal (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> *(2)* Let $S$ be a regular submanifold of codimension $0$. Each $p \in S$ lies in the domain $U_p$ of an adapted chart, and $U_p \subseteq S$ by the observation above. So $S = \bigcup_{p \in S} U_p$ is a union of open sets of $M$, hence open.

^pf-37-4

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§17 Differentiable Structures#^prop-17-6|§17.6]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

![[m591-15-1.svg]]
*An adapted chart ($m = 2$, $k = 1$). The chart $\varphi$ straightens $U \cap S$ onto the part of the $x_a$-axis inside $\varphi(U)$ — exactly the set $\varphi(U) \cap \{x_b = 0\}$, running from rim to rim — and the induced chart $\varphi_S$ keeps only the coordinate $x_a$, landing on an open interval of $\mathbb{R}^{m-k}$.*

> [!remark]- Connections
> - The subspace topology: [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]].
> - The Euclidean prototype, level sets with graph charts: [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]; the two structures agree by [[§37 Regular Submanifolds#^prop-37-11|§37.11]].

**Extending charts.** A student asked whether every chart of $S$ extends to an adapted chart of $M$. Uribe: “The answer is yes” — since everything reduces to the local Euclidean picture, the $m - k$ functions of a chart of $S$ extend to a neighbourhood in $M$. This is stated, not proved, here; likewise his remark that smooth functions on $S$ extend to smooth functions near $S$.

> [!theorem] Lemma §37.5: Smooth Maps and Regular Submanifolds
> Let $S \subseteq M$ be a regular submanifold, with its induced structure, and $\iota : S \to M$ the inclusion.
> 1. $\iota$ is smooth; in an adapted chart and its induced chart, its coordinate representation is $j(r) = (r, \vec 0)$.
> 2. If $G : X \to M$ is smooth and $G(X) \subseteq S$, then $G$ is smooth as a map into $S$.
>
> *Lee: Corollary 5.30*

^lem-37-5

> [!proof]+ Proof
> *((1) is Uribe's “immediate from the definitions”; filled in, and (2) is not from lecture.)* Recall from the proof of Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] that for an adapted chart $(U, \varphi)$, $\varphi_S = \mathrm{pr} \circ \varphi$ on $U \cap S$ and $\varphi_S^{-1} = \varphi^{-1} \circ j$, with $j(r) = (r, \vec 0)$ and $\mathrm{pr}(r, s) = r$.
>
> (1) $\iota$ is continuous for the subspace topology: the preimage of an open $O \subseteq M$ is $O \cap S$, open in $S$. For an adapted chart, $\varphi \circ \iota \circ \varphi_S^{-1} = \varphi \circ \varphi^{-1} \circ j = j$ on $\varphi_S(U \cap S)$, which is smooth, so $\iota$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]). In detail: every $p \in S$ lies in an adapted chart $(U, \varphi)$, whose induced chart $(U \cap S, \varphi_S)$ is a chart of $S$ at $p$ with $\iota(U \cap S) \subseteq U$; the coordinate representation in these charts is the linear map $j$; so $\iota$ is smooth by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]], and this computation shows that its coordinate representation is $j$ in every adapted chart and its induced chart.
>
> (2) $G$ is continuous into $S$, since $G^{-1}(O \cap S) = G^{-1}(O)$ for $O$ open in $M$ (because $G(X) \subseteq S$), and the sets $O \cap S$ are the open sets of $S$. Given $x \in X$, take an adapted chart $(U, \varphi)$ at $G(x)$ and a chart $\chi$ of $X$ at $x$ with domain inside $G^{-1}(U)$ — the restriction of any chart at $x$ to its intersection with the open set $G^{-1}(U)$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)). Its domain is then mapped by $G$ into $U \cap S$, the domain of the induced chart $\varphi_S$. Then $\varphi_S \circ G \circ \chi^{-1} = \mathrm{pr} \circ (\varphi \circ G \circ \chi^{-1})$, a linear map composed with a coordinate representation of the smooth map $G$, hence smooth: $\varphi \circ G \circ \chi^{-1}$ is smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], and $\varphi_S = \mathrm{pr} \circ \varphi$ on $U \cap S$. So $G : X \to S$ is smooth by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]].

^pf-37-5

*Uses:* [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§2 Topological Manifolds#^lem-2-10|§2.10]]

![[m591-15-2.svg]] ![[m591-15-3.svg]]
*Left, (1): in an adapted chart and its induced chart the inclusion is $j(r) = (r, \vec 0)$. Right, (2): a smooth map into $M$ whose values lie in $S$ factors through $S$, and the factor — dashed — is smooth.*

> [!theorem] Proposition §37.6: Tangent Spaces of a Regular Submanifold
> Let $S \subseteq M$ be a regular submanifold of codimension $k$ and $p \in S$. Then $\iota_{*p} : T_pS \to T_pM$ is injective. In an adapted chart $(x^1, \ldots, x^m)$ at $p$, writing $\partial/\partial x^i|^S_p$ for the coordinate derivations of the induced chart $(x^1, \ldots, x^{m-k})$ of $S$,
>
> $$
> \iota_{*p}\Big(\frac{\partial}{\partial x^i}\Big|^S_p\Big) = \frac{\partial}{\partial x^i}\Big|_p \quad (i \le m - k), \qquad \iota_{*p}(T_pS) = \operatorname{Span}\Big\{\frac{\partial}{\partial x^1}\Big|_p, \ldots, \frac{\partial}{\partial x^{m-k}}\Big|_p\Big\}.
> $$
>
> Equivalently, by curves: for a smooth curve $\gamma$ in $S$ with $\gamma(0) = p$, $\iota_{*p} D_\gamma = D_{\iota \circ \gamma}$ — a curve in $S$ is a curve in $M$, with the same velocity.
>
> *Lee: Propositions 5.35 and 5.37*

^prop-37-6

> [!proof]+ Proof
> *(Lecture 12: “immediate from the definitions”; filled in.)* Fix an adapted chart $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and its induced chart $(U \cap S, \varphi_S)$ of $S$, whose coordinate functions are $x^1, \ldots, x^{m-k}$ restricted to $U \cap S$; by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]] the $\partial/\partial x^i|^S_p$, $i \le m - k$, form a basis of $T_pS$, and the $\partial/\partial x^l|_p$, $l \le m$, a basis of $T_pM$.
>
> *The formula.* By Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) the coordinate representation of $\iota$ is $j$, whose Jacobian is the $m \times (m-k)$ matrix $\binom{I_{m-k}}{0}$: the components of $j(r) = (r, \vec 0)$ are $j^l(r) = r^l$ for $l \le m - k$ and $j^l(r) = 0$ for $l > m - k$, so $\partial j^l/\partial r^i = \delta^l_i$ for $l \le m - k$ and $0$ for $l > m - k$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] this is the matrix of $\iota_{\ast p}$ in the coordinate bases; its $i$-th column gives the formula. Explicitly, the formula of that theorem, with the upstairs partials replaced by the entries of the Jacobian of $j$, reads
>
> $$
> \iota_{\ast p}\Big(\frac{\partial}{\partial x^i}\Big|^S_p\Big) = \sum_{l=1}^m \frac{\partial j^l}{\partial r^i}\big(\varphi_S(p)\big)\, \frac{\partial}{\partial x^l}\Big|_p = \sum_{l=1}^{m-k} \delta^l_i\, \frac{\partial}{\partial x^l}\Big|_p = \frac{\partial}{\partial x^i}\Big|_p \qquad (i \le m - k).
> $$
>
> *The image.* $\iota_{\ast p}$ is linear, so it maps $T_pS$, the span of the basis $\partial/\partial x^i|^S_p$ ($i \le m - k$), onto the span of their images, which by the formula is $\operatorname{Span}\{\partial/\partial x^1|_p, \ldots, \partial/\partial x^{m-k}|_p\}$.
>
> *Injectivity.* The columns of $\binom{I_{m-k}}{0}$ are independent, so $\iota_{\ast p}$ is injective. In terms of vectors: if $\iota_{\ast p}\big(\sum_i a_i\, \partial/\partial x^i|^S_p\big) = \sum_i a_i\, \partial/\partial x^i|_p = 0$, then every $a_i = 0$, because the $\partial/\partial x^i|_p$ are part of a basis of $T_pM$.
>
> *Curves.* The statement for curves is Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], applied to the smooth map $F = \iota$ and a smooth curve $\gamma$ in $S$ with $\gamma(0) = p$: it gives $\iota_{\ast p} D_\gamma = D_{\iota \circ \gamma}$, where $\iota \circ \gamma$ is $\gamma$ regarded as a curve in $M$, smooth by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]].

^pf-37-6

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]

So $T_pS$ is identified with the $(m-k)$-dimensional subspace $\iota_{*p}(T_pS) \subseteq T_pM$, the “intrinsic tangent space” inside the ambient one — “for some reason this class, and maybe all abstract classes, keep identifying things with each other.” The second description is the one from Assignment 3, Problem 2: think of a curve in $S$ composed with the inclusion as a curve in $M$, and take its velocity there.

> [!definition] Definition §37.4: Conormal Space
> Let $S \subseteq M$ be a regular submanifold and $p \in S$. The **conormal space** of $S$ at $p$ is
>
> $$
> N_pS = \{\, \xi \in T_p^*M : \xi(v) = 0 \text{ for all } v \in \iota_{*p}(T_pS) \,\},
> $$
>
> the covectors at $p$ that vanish on the tangent space of $S$ — the annihilator of $T_pS$ in $T_p^*M$.

^def-37-4

> [!remark]- Connections
> - The annihilator of a subspace: [[§12 Duality#^ladr-3-121|LADR 3.121]].

> [!theorem] Proposition §37.7: A Basis of the Conormal Space
> In an adapted chart at $p$, $N_pS$ has basis $dx^{m-k+1}|_p, \ldots, dx^m|_p$. In particular $\dim N_pS = k$, the codimension of $S$.

^prop-37-7

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Fix an adapted chart $(x^1, \ldots, x^m)$ at $p$. Write $\xi = \sum_j \xi_j\, dx^j|_p$ in the dual basis (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), so that $\xi(\partial/\partial x^i|_p) = \xi_i$. (By Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] the $dx^j|_p$ are the basis dual to the $\partial/\partial x^j|_p$, and the coefficients are the components $\xi_i = \xi(\partial/\partial x^i|_p)$ of Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]].) By Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], $\xi$ vanishes on $\iota_{\ast p}(T_pS)$ if and only if $\xi_i = 0$ for all $i \le m - k$. Indeed, $\iota_{\ast p}(T_pS)$ is the span of $\partial/\partial x^1|_p, \ldots, \partial/\partial x^{m-k}|_p$, and a linear functional vanishes on a span if and only if it vanishes on each spanning vector; so
>
> $$
> \xi \in N_pS \iff \xi\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = 0 \ \ (i \le m - k) \iff \xi_i = 0 \ \ (i \le m - k) \iff \xi = \sum_{j = m-k+1}^m \xi_j\, dx^j\big|_p .
> $$
>
> So $N_pS$ is spanned by the $dx^j|_p$ with $j > m - k$, which are linearly independent as part of a basis. (Each of them does lie in $N_pS$, by the same equivalence: for $j > m - k$ and $i \le m - k$, $dx^j|_p(\partial/\partial x^i|_p) = \delta^j_i = 0$.) So they form a basis of $N_pS$, and $\dim N_pS = m - (m - k) = k$, the codimension of $S$.

^pf-37-7

*Uses:* [[§37 Regular Submanifolds#^def-37-4|Def. §37.4]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]

> [!remark]- Connections
> - The dimension count in general: [[§12 Duality#^ladr-3-125|LADR 3.125]] ($\dim U^0 = \dim V - \dim U$).

> [!remark] Remark: No Normal Vectors Without a Metric
> “We don't have normal vectors, because we don't have a metric … There is no notion of orthogonality, but there is an intrinsic” definition: the conormal space. “If we had a metric, [an] inner product on $T_pM$, we could identify $T^*_pM$ with $T_pM$, and this would be the normal space.” Uribe added that he regards the cotangent side as “actually more natural” than the tangent side — “that's where Hamiltonian mechanics takes place.”

^rem-37-1

![[m591-15-4.svg]]
*How to draw a conormal covector. Without a metric, a covector $\xi$ on $T_pM$ is drawn by its level lines $\{\xi = \text{const}\}$. For $\xi \in N_pS$ the level line $\xi = 0$ contains $T_pS$, so all of its level lines run* parallel *to $T_pS$ (left). Only once an inner product is chosen does $\xi$ become a vector, perpendicular to its level lines, and $N_pS$ becomes the normal line $(T_pS)^\perp$ (right). The board, and page 33 of the handwritten notes, draw $N_pS$ as a line perpendicular to $T_pS$: that is the right-hand, metric picture.*

> [!remark]- Connections
> - With an inner product: the orthogonal complement [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]], and the identification of covectors with vectors, [[Riesz representation theorem|LADR 6.42]].
> - The same point for gradients: [[§33 Covectors in Coordinates#^rem-33-2|Differential — Not Gradient]].

## Regular Submanifolds of Euclidean Space

*Not from lecture: the link back to the geometric stage.* Inside a Euclidean space, [[§20 Manifolds in Euclidean Space|§20]] described a manifold $X \subseteq \mathbb{R}^{n+k}$ near a point in three ways — externally, by equations ([[§20 Manifolds in Euclidean Space#^def-20-1|Definition §20.1]]); internally, by a parametrization ([[§20 Manifolds in Euclidean Space#^def-20-2|Definition §20.2]]); and as a graph — and [[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]] showed that they agree. [[§37 Regular Submanifolds#^def-37-2|Definition §37.2]] adds a fourth, the *slice* description: a chart of the ambient space in which $X$ is a coordinate plane. The fourth agrees with the other three, so in $\mathbb{R}^{n+k}$ the submanifolds of codimension $k$ are exactly the manifolds of [[§20 Manifolds in Euclidean Space|§20]], and Definition §35.1 is their description made intrinsic to the ambient manifold.

> [!theorem] Proposition §37.8: Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description
> Let $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$. The following are equivalent:
> 1. near $p$, $X$ is described [[§20 Manifolds in Euclidean Space#^def-20-1|externally]] ([[§20 Manifolds in Euclidean Space#^def-20-1|Definition §20.1]]) — equivalently, [[§20 Manifolds in Euclidean Space#^def-20-2|internally]] or as a graph ([[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]]);
> 2. *(slice)* there is a smooth chart $(U, \varphi = (x_a, x_b))$ of $\mathbb{R}^{n+k}$ with $p \in U$, $x_a$ its first $n$ and $x_b$ its last $k$ components, such that $U \cap X = \{\, q \in U : x_b(q) = \vec 0 \,\}$, that is, a chart [[§37 Regular Submanifolds#^def-37-3|adapted]] to $X$ ([[§37 Regular Submanifolds#^def-37-3|Definition §37.3]]).
>
> In particular $X$ is a [[§37 Regular Submanifolds#^def-37-2|regular submanifold]] of $\mathbb{R}^{n+k}$ of codimension $k$ ([[§37 Regular Submanifolds#^def-37-2|Definition §37.2]]) if and only if every point of $X$ has the descriptions of [[§20 Manifolds in Euclidean Space|§20]].

^prop-37-8

> [!proof]+ Proof
> *(Not from lecture.)* By Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] the external, internal and graph descriptions near $p$ are equivalent, so for (1)$\iff$(2) it suffices to prove graph $\Rightarrow$ slice and slice $\Rightarrow$ external; together with external $\Rightarrow$ graph (Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]) these close the cycle.
>
> *Graph $\Rightarrow$ slice.* Permuting coordinates is a linear isomorphism, so we may assume $X \cap (V \times V') = \{(x, h(x)) : x \in V\}$ as in (G) of Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]. (If a permutation $P$ is needed, the construction below gives a chart $\Phi$ adapted to $P(X)$, and $\Phi \circ P$ is a chart adapted to $X$ for the same reason as in the proof of Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]: its transition maps with any smooth chart are those of $\Phi$ composed with the linear maps $P$ or $P^{-1}$.) Let $U = V \times V'$, an open set containing $p$, and $\Phi(x, y) = (x,\, y - h(x))$ on $U$. Then:
> - $\Phi$ is smooth, its components $x$ and $y - h(x)$ being smooth;
> - $\Phi$ is injective: $\Phi(x, y) = \Phi(x', y')$ gives $x = x'$ and then $y - h(x) = y' - h(x)$, so $y = y'$;
> - its image $\{(x, z) : x \in V,\ z + h(x) \in V'\}$ is open: it is the preimage of the open set $V \times V'$ under the continuous map $\Psi(x, z) = (x, z + h(x))$ on the open set $V \times \mathbb{R}^k$;
> - its inverse is $\Psi$ restricted to the image, $(x, z) \mapsto (x, z + h(x))$, which is smooth.
>
> So $\Phi$ is a diffeomorphism of $U$ onto an open set (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]), hence a smooth chart of $\mathbb{R}^{n+k}$: it is a homeomorphism onto an open set, and its transition maps with the identity chart are $\Phi$ and $\Phi^{-1}$, so it is compatible with the atlas $\{(\mathbb{R}^{n+k}, \mathrm{id})\}$ and lies in the maximal atlas it generates (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). Its last $k$ components $y - h(x)$ vanish exactly on $X \cap U$: for $(x, y) \in U$, $y - h(x) = 0$ iff $y = h(x)$ iff $(x, y) \in X \cap (V \times V')$. So $\Phi$ is a chart adapted to $X$ at $p$.
>
> *Slice $\Rightarrow$ external.* Let $F = x_b : U \to \mathbb{R}^k$, the last $k$ components of $\varphi$; it is smooth, its components being components of the smooth map $\varphi$. A chart is a diffeomorphism onto its image (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]; it is a diffeomorphism of open subsets of $\mathbb{R}^{n+k}$ by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]]), so the Jacobian $\varphi'(q)$ is invertible at every $q \in U$: the ordinary chain rule applied to $\varphi^{-1} \circ \varphi = \mathrm{id}_U$ gives $(\varphi^{-1})'(\varphi(q))\, \varphi'(q) = I$. Its last $k$ rows, which form $F'(q)$, are linearly independent, since the rows of an invertible matrix are; and row $l$ of $\varphi'(q)$ is the gradient of the $l$-th component of $\varphi$ (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]), so these rows are exactly the rows of $F'(q)$. Hence $F'(q)$ has rank $k$ everywhere, $\vec 0$ is a regular value of $F$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]: every point of $F^{-1}(\vec 0)$, indeed every point of $U$, is a regular point), and
>
> $$
> X \cap U = \{\, q \in U : x_b(q) = \vec 0 \,\} = F^{-1}(\vec 0) ,
> $$
>
> by (2): the external description with $W = U$ (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]]).
>
> The final statement follows, since Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] asks for (2) at every point of $X$: $X$ is a regular submanifold of codimension $k$ iff every $p \in X$ has an adapted chart, i.e. satisfies (2), iff every $p \in X$ satisfies (1), by the equivalence just proved.

^pf-37-8

*Uses:* [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§20 Manifolds in Euclidean Space#^def-20-2|Def. §20.2]], [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]]

![[m591-35-3.svg]]
*Straightening a graph. The map $\Phi(x, y) = (x, y - h(x))$ keeps $x$ and measures the height above the graph; it carries the graph $X$ to the slice $z = 0$, and the parallel graphs $y = h(x) + c$ to the slices $z = c$. This is the passage from the graph charts of [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2]], which flatten $X$ alone, to an adapted chart, which straightens a whole neighbourhood of $X$ in the ambient space.*

For the unit sphere $S^2 \subseteq \mathbb{R}^3$ near the north pole, the graph is $z = \sqrt{1 - x^2 - y^2}$, and $(x, y, z) \mapsto (x, y, z - \sqrt{1 - x^2 - y^2})$ is an adapted chart; so is $(x, y, z) \mapsto (x, y, x^2 + y^2 + z^2 - 1)$ near any point with $z \neq 0$, whose last coordinate is the defining function of the external description.

> [!remark] Remark: The Tangent Spaces Match
> *(Not from lecture.)* The two tangent spaces of the geometric and the abstract stage correspond as well. Externally, $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]]). In the slice chart of [[§37 Regular Submanifolds#^prop-37-8|Proposition §37.8]], with $F = x_b$, this kernel is the set of vectors on which the differentials of the last $k$ coordinates vanish, the span of the first $n$ coordinate directions; and that span is $\iota_{\ast p}(T_pX)$ ([[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6]]). [[§37 Regular Submanifolds#^prop-37-11|Proposition §37.11]] below makes the identification precise, together with the agreement of the two smooth structures.

^rem-37-2

## The Regular Value Theorem for Manifolds

*Lecture 12. “And now we go back to submersions” — to “[the] wonderful version of the regular value theorem.”*

> [!theorem] Theorem §37.9: The Regular Value Theorem for Manifolds
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$, and let $q \in N$ be a regular value of $F$ (Definition [[§36 Submersions#^def-36-4|§36.4]]). Then $S = F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$ (possibly empty), so $\dim S = m - n$, and for every $p \in S$
>
> $$
> \iota_{*p}(T_pS) = \ker F_{*p} .
> $$
>
> *Lee: Corollary 5.14 and Proposition 5.38*

^thm-37-9

> [!proof]+ Proof
> *$S$ is a submanifold (Lecture 12).* We check the definition at each $p \in S$: we need an adapted chart at $p$. (If $S = \emptyset$ there is nothing to check.) By assumption $F$ is a submersion at $p$, so the normal form (Theorem [[§36 Submersions#^thm-36-4|§36.4]]) gives charts $(U, \hat\varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q = F(p)$, with $F(U) \subseteq V$ and $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$. What are the equations of $S \cap U$ in these coordinates? For $q' \in U$,
>
> $$
> \begin{aligned}q' \in S &\iff F(q') = q \iff \psi\big(F(q')\big) = \psi(q) \\
> &\iff \tilde F\big(\hat\varphi(q')\big) = \psi(q) \iff \big(x^1(q'), \ldots, x^n(q')\big) = \big(y^1(q), \ldots, y^n(q)\big).\end{aligned}
> $$
>
> “These are not of the type $x_b = 0$, but of the type $x_a$ equals a constant”: the first $n$ coordinates equal a constant vector. By the observations after the definition (Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]) — any constant, and any $n$ of the coordinates — $S$ has an adapted chart at $p$, of codimension $n$. *(Completion.)* The second equivalence uses that $\psi$ is injective on $V$, which contains $F(q')$; the last is the normal form. In detail: the first equivalence is $S = F^{-1}(q)$; the second holds because $F(q')$ and $q$ both lie in $V$, on which $\psi$ is injective; the third because $\psi \circ F = \tilde F \circ \hat\varphi$ on $U$, by the definition $\tilde F = \psi \circ F \circ \hat\varphi^{-1}$; and the last because $\tilde F(\hat\varphi(q'))$ consists of the first $n$ entries $x^1(q'), \ldots, x^n(q')$ of $\hat\varphi(q')$, while $\psi(q) = (y^1(q), \ldots, y^n(q))$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]). So Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] applies with $k = n$, the coordinates $x^1, \ldots, x^n$ and the constant vector $\vec c = \psi(q)$, and here $n \le m$ by the normal form. As $p \in S$ was arbitrary, $S$ is a regular submanifold of codimension $n$, and $\dim S = m - n$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]].
>
> *The tangent space.* *(Completion. In lecture: “I won't bother checking the kernel thing, because everything really reduces to the Euclidean [case].”)* The composite $F \circ \iota : S \to N$ is constant, with value $q$, and the pushforward along a constant map is zero (as in the proof of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]); so $F_{\ast p} \circ \iota_{\ast p} = 0$ and $\iota_{\ast p}(T_pS) \subseteq \ker F_{\ast p}$. Explicitly, by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $F_{\ast p} \circ \iota_{\ast p} = (F \circ \iota)_{\ast p} = 0$, so $F_{\ast p}(\iota_{\ast p}v) = 0$ for every $v \in T_pS$. The left side has dimension $m - n$, since $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]); the right side has dimension $m - n$ by rank–nullity, since $F_{\ast p}$ is onto (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]). In detail: $\dim \iota_{\ast p}(T_pS) = \dim T_pS = \dim S = m - n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]), an injective linear map preserving dimension; and $m = \dim T_pM = \dim\ker F_{\ast p} + \operatorname{rank} F_{\ast p} = \dim\ker F_{\ast p} + n$. A subspace of the same finite dimension is everything, so the two are equal. This is the argument of Lecture 8 for $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]), one level up.

^pf-37-9

*Uses:* [[§36 Submersions#^def-36-3|Def. §36.3]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§36 Submersions#^thm-36-4|§36.4]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[Fundamental theorem of linear maps|LADR 3.21]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]

![[m591-15-5.svg]]
*The proof in one square, as on the board. In the normal-form charts $\tilde F$ is the projection onto the first $n$ coordinates, so the level set $S \cap U = F^{-1}(q) \cap U$ is carried by $\hat\varphi$ onto a fibre of a projection: the slice where the first $n$ coordinates equal $\psi(q)$.*

> [!remark]- Connections
> - The earlier regular value theorems it contains: [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§30 The Differential in Coordinates#^cor-30-9|§30.9]] (see the remark below); the tangent-space statement generalizes [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]].
> - Constraint sets $\{g_1 = c_1, \ldots, g_k = c_k\}$ in multivariable analysis: [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 §17.3]] (Lagrange multipliers with several constraints).
> - Fibres of submersions that are all copies of one fibre: [[§38 Fibrations#^def-38-1|fibrations, Def. §38.1]].

**Transcription note.** Page 33 of the handwritten notes states the theorem for “$q \in M$ a regular value”; the regular value lies in the target, $q \in N$.

> [!theorem] Corollary §37.10: Fibres of Submersions Are Regular Submanifolds
> If $F : M \to N$ is a submersion, then every fibre $F^{-1}(q)$, $q \in N$, is a regular submanifold of $M$ of codimension $n$ — “they could be empty, some of them.”

^cor-37-10

> [!proof]+ Proof
> Every $q \in N$ is a regular value: every point of $F^{-1}(q)$ is a regular point, and if $F^{-1}(q)$ is empty the condition holds vacuously. Indeed, $F$ is a submersion at every point of $M$ (Definition [[§36 Submersions#^def-36-1|§36.1]]), in particular at every $p \in F^{-1}(q)$, which is what Definition [[§36 Submersions#^def-36-4|§36.4]](2) asks of a regular value; and if $q \notin F(M)$, it is a regular value by Definition [[§36 Submersions#^def-36-4|§36.4]](3). Apply Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]]: $F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$.

^pf-37-10

*Uses:* [[§36 Submersions#^def-36-3|Def. §36.3]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§37 Regular Submanifolds#^thm-37-9|§37.9]], [[§36 Submersions#^def-36-1|Def. §36.1]]

> [!remark] Remark: The Regular Value Theorems — Old and New
> The notes now contain the regular value theorem in five forms. They are one idea met at increasing generality, not competing statements.
>
> | **Where** | **Setting** | **Conclusion** | **Role now** |
> |---|---|---|---|
> | Thm. [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]], Cor. [[§7 The Regular Value Theorem#^cor-7-4\|§7.4]] | $F : W \to \mathbb{R}^k$, $W \subseteq \mathbb{R}^{n+k}$ open | topological manifold | the first version (Lecture 3); Chapter 2 needs it |
> | Prop. [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] | the same | smooth manifold, by graph charts | the Euclidean case (Lecture 6) |
> | Prop. [[§30 The Differential in Coordinates#^prop-30-8\|§30.8]] | $F : M \to N$, level set inside one chart | regular for $F$ iff for $\tilde F$ | a computational tool |
> | Cor. [[§30 The Differential in Coordinates#^cor-30-9\|§30.9]] | $F : M \to N$ | topological manifold | subsumed; a more elementary proof |
> | Thm. [[§37 Regular Submanifolds#^thm-37-9\|§37.9]] | $F : M \to N$ | submanifold, with $\iota_{*p}(T_pS) = \ker F_{*p}$ | the general theorem (Lecture 12) |
>
> The general theorem contains the others: taking $M$ an open subset of Euclidean space recovers the first two. Its proof goes through the normal form, which rests on the inverse function theorem and not on [[§7 The Regular Value Theorem|§7]], so nothing is circular. The next proposition shows that the old and new versions give the same smooth structure and the same tangent spaces.

^rem-37-3

> [!theorem] Proposition §37.11: The Old and New Versions Agree
> Let $W \subseteq \mathbb{R}^{n+k}$ be open, $F : W \to \mathbb{R}^k$ smooth, $c$ a regular value, and $S = F^{-1}(c)$.
> 1. The smooth structure on $S$ given by the graph charts (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) is the induced structure of $S$ as a regular submanifold of $W$ (Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]]).
> 2. In the setting of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], under the identification $T_pW = \mathbb{R}^{n+k}$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the subspace $\iota_{*p}(T_pS)$ is $T^{\mathrm{geo}}_pS = \ker F'(p)$.

^prop-37-11

> [!proof]+ Proof
> *(Not from lecture; filled in.)* First, $c$ is a regular value in both senses, since the matrix of $F_{\ast p}$ in the standard coordinates is $F'(p)$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]). In detail: with the identity charts on $W$ and on $\mathbb{R}^k$, the coordinate representation of $F$ is $F$ itself, so Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] says the matrix of $F_{\ast p}$ in the coordinate bases is $F'(p)$. A linear map is onto $T_{F(p)}\mathbb{R}^k$ iff its rank is $k$, and its rank is that of its matrix (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)); so $F_{\ast p}$ is onto (Definition [[§36 Submersions#^def-36-4|§36.4]]) iff $F'(p)$ has rank $k$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]). Hence Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]] applies to $F : W \to \mathbb{R}^k$, and $S$ is a regular submanifold of $W$ of codimension $k$.
>
> (1) Let $p \in S$. As in the construction of the graph charts, after reordering the coordinates write the points of $\mathbb{R}^{n+k}$ as $(x, y) \in \mathbb{R}^n \times \mathbb{R}^k$ with $\partial F/\partial y\,(p)$ invertible, so that the graph chart near $p$ is $(x, y) \mapsto x$ on $S$. (Here $x = x_I$, $y = x_J$ in the notation of the construction before Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], and the graph chart is $\varphi_J = \pi_I|_{U_J}$. The reordering is a permutation $P$ of coordinates; the chart produced below is then $\Phi \circ P$, a smooth chart for the reason given in the proof of Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]], with the same last $k$ components. We suppress $P$.) Let $\Phi(x, y) = (x, F(x, y) - c)$. Its Jacobian at $p$ is $\begin{pmatrix} I_n & 0 \\ \partial F/\partial x & \partial F/\partial y \end{pmatrix}$, which is invertible: it is block lower triangular, so its determinant is $\det I_n \cdot \det\big(\partial F/\partial y\,(p)\big) \ne 0$. So by the inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], with $\Phi$ on $W$ and $a = p$) $\Phi$ restricts to a diffeomorphism of an open $U \ni p$ onto an open set, and by Lemma [[§36 Submersions#^lem-36-3|§36.3]] (with $M = W$, the diffeomorphism being one of manifolds by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]]) it is a smooth chart of $W$. Its last $k$ components are $F - c$, which vanish exactly on $S \cap U$, so $\Phi$ is adapted, and its induced chart is $\Phi_S = x|_{S \cap U}$: the graph chart. More precisely, $\Phi_S$ and the graph chart $\varphi_J$ are both restrictions of the projection $(x, y) \mapsto x$, so they agree on $S \cap U \cap U_J$, an open neighbourhood of $p$ in $S$. The same construction works at every point $p'$ of the graph chart's domain $U_J$, with the same splitting $(x, y)$: there $S$ is the graph $y = h_J(x)$, and differentiating $F(x, h_J(x)) = c$ gives $\partial F/\partial x = -\,\partial F/\partial y \cdot h_J'$, so $F'(p') = \partial F/\partial y\,(p') \cdot \big({-h_J'} \mid I_k\big)$; as $F'(p')$ has rank $k$, the $k \times k$ matrix $\partial F/\partial y\,(p')$ has rank $k$, i.e. is invertible. So near each of its points, every graph chart is an induced chart. Induced charts are pairwise compatible, and smoothness of a transition map is local, so every graph chart is compatible with every induced chart, and the two atlases determine the same maximal atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). In detail: let $(U_J, \varphi_J)$ be a graph chart and $(V \cap S, \psi_S)$ an induced chart. Near each point $\varphi_J(p')$ of the domain of $\psi_S \circ \varphi_J^{-1}$, by what was just shown, $\varphi_J$ agrees with an induced chart $\Phi_S$ on an open neighbourhood $O$ of $p'$ in $S$; on $\varphi_J(O \cap V)$ the map $\psi_S \circ \varphi_J^{-1}$ equals $\psi_S \circ \Phi_S^{-1}$, a transition map between induced charts, smooth by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]](2). The same holds for $\varphi_J \circ \psi_S^{-1}$ near each point. So the two charts are compatible, the union of the two atlases is an atlas, and both generate the maximal atlas containing it.
>
> (2) Let $v \in T^{\mathrm{geo}}_pS$, and let $\gamma$ be the lifted line of Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], a curve in $S$ with $\gamma(0) = p$ and $\gamma'(0) = v$, so that $D_v = D_\gamma$. (It is smooth into $\mathbb{R}^{n+k}$ with values in $S$, hence smooth into $S$ by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2); by (1) the structure there is the induced one, so $T_pS$ and $\iota_{\ast p}$ are unambiguous. And $D_v = D_\gamma$ because both send $f$ to $\frac{d}{dt}|_{t=0} f(\gamma(t))$, by Definitions [[§25 The Geometric Tangent Space#^def-25-4|§25.4]] and [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]].) By Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], $\iota_{\ast p}D_v = D_{\iota \circ \gamma}$, the derivation $g \mapsto (g \circ \gamma)'(0) = \nabla g(p) \cdot v$ at $p$ — the directional derivative in the direction $v$, which is $v$ under Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]. In detail, for a germ $[g]$ at $p$ on $W$, by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]] and the chain rule (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]),
>
> $$
> (\iota_{\ast p}D_v)[g] = D_{\iota \circ \gamma}[g] = \frac{d}{dt}\Big|_{t=0} g\big(\gamma(t)\big) = \nabla g(p) \cdot \gamma'(0) = \nabla g(p) \cdot v = \frac{d}{dt}\Big|_{t=0} g(p + tv) = D_v|_p[g] ,
> $$
>
> where $D_v|_p \in T_pW$ is the derivation of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the vector $v$ under the identification $T_pW = \mathbb{R}^{n+k}$; the fifth equality is the chain rule for the line $t \mapsto p + tv$. Since $v \mapsto D_v$ is onto $T_pS$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), $\iota_{\ast p}(T_pS) = T^{\mathrm{geo}}_pS$: every element of $T_pS$ is $D_v$ for some $v \in T^{\mathrm{geo}}_pS$, and its image is the vector $v$. And $T^{\mathrm{geo}}_pS = \ker F'(p)$ by Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]. This matches $\ker F_{\ast p}$ in Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]], $F_{\ast p}$ being $F'(p)$: by Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], $F_{\ast p}$ corresponds to $F'(p)$ under the identification $\partial/\partial r^i|_p \mapsto e_i$, which is the identification of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], since $D_{e_i}|_p[g] = \frac{d}{dt}|_{t=0}\, g(p + te_i) = \partial g/\partial r^i(p)$; so $\ker F_{\ast p}$ corresponds to $\ker F'(p)$.

^pf-37-11

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§36 Submersions#^lem-36-3|§36.3]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§37 Regular Submanifolds#^thm-37-9|§37.9]], [[Directional Derivative Formula|452 §9.1]], [[Multivariable Chain Rule|452 §12.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]

*Assignment 5, Problem 2.* [[§26 Transversality|§26]] treated transversality in Euclidean space: a smooth map $F : \mathbb{R}^N \to \mathbb{R}^k$ transverse to a regular level set $S = G^{-1}(0)$ (Definition [[§26 Transversality#^def-26-2|§26.2]]) pulls $S$ back to a manifold of the same codimension, with $T^{\mathrm{geo}}_pF^{-1}(S) = F'(p)^{-1}(T^{\mathrm{geo}}_{F(p)}S)$ (Theorem [[§26 Transversality#^thm-26-1|§26.1]]). That proof needed a global defining map $G$. With regular submanifolds and their adapted charts, the same statement holds for any smooth map between manifolds and any regular submanifold of the target — an adapted chart supplies a defining map $x_b$ near each point, which is the localization announced in Remark [[§26 Transversality#^rem-26-2|remark]].

> [!definition] Definition §37.5: Transversality to a Submanifold
> Let $F : M \to N$ be smooth, $S \subseteq N$ a regular submanifold, and $\iota : S \to N$ the inclusion. For $p \in F^{-1}(S)$, $F$ is **transverse to $S$ at $p$** if
>
> $$
> F_{\ast p}\big(T_pM\big) + \iota_{\ast F(p)}\big(T_{F(p)}S\big) = T_{F(p)}N ,
> $$
>
> the sum of two subspaces of $T_{F(p)}N$; and $F$ is **transverse to $S$**, written $F \pitchfork S$, if it is transverse to $S$ at every $p \in F^{-1}(S)$. Here $T_qS$ is regarded as a subspace of $T_qN$ through the injective map $\iota_{\ast q}$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]). The condition is imposed only at points of the preimage, and holds vacuously if $F^{-1}(S) = \emptyset$.
>
> *Lee: Ch. 6, Transversality*

^def-37-5

> [!theorem] Theorem §37.12: Preimages of Transverse Submanifolds
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$, let $S \subseteq N$ be a regular submanifold of codimension $k$, and suppose $F \pitchfork S$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]). Let $\iota : S \to N$ and $j : F^{-1}(S) \to M$ be the inclusions.
>
> 1. $F^{-1}(S)$ is a regular submanifold of $M$ of codimension $k$, the codimension of $S$ in $N$ (possibly empty). If it is nonempty, then $k \le m$ and $\dim F^{-1}(S) = m - k$.
> 2. For every $p \in F^{-1}(S)$,
>
> $$
> j_{\ast p}\big(T_pF^{-1}(S)\big) = (F_{\ast p})^{-1}\big(\iota_{\ast F(p)}(T_{F(p)}S)\big) = \big\{\, v \in T_pM : F_{\ast p}v \in \iota_{\ast F(p)}(T_{F(p)}S) \,\big\} .
> $$
>
> Identifying the tangent spaces of the two submanifolds with their images (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), (2) reads $T_pF^{-1}(S) = F_{\ast p}^{-1}\big(T_{F(p)}S\big)$, the formula of Theorem [[§26 Transversality#^thm-26-1|§26.1]].
>
> *Lee: Theorem 6.30(a)*

^thm-37-12

> [!proof]+ Proof
> *(Assignment 5, Problem 2; the student's route, with two steps completed — the normal form is applied at a single point, and the kernel of $(x_b)_{\ast q}$ is computed directly, without the regular value theorem.)* For (1) we must produce, at every $p \in F^{-1}(S)$, a smooth chart of $M$ adapted to $F^{-1}(S)$ with $k$ equations (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]). If $F^{-1}(S) = \emptyset$ there is nothing to check, since the condition of Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] is one condition at each point of the subset (the convention of Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]], whose fibres may be empty); and (2) is then vacuous. So fix $p \in F^{-1}(S)$ and put $q = F(p)$, a point of $S$. The plan: an adapted chart of $S$ at $q$ supplies a local defining map $x_b$ for $S$; transversality makes $G = x_b \circ F$ a submersion at $p$; the normal form of $G$ then straightens $F^{-1}(S)$ near $p$. Throughout, the tangent space of an open subset at a point is identified with that of the ambient manifold (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), as everywhere in the notes; by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), applied to a restriction $F|_V = F \circ \iota_V$ with $\iota_V$ the inclusion of the open set $V$, this identification turns the differential of a restriction of $F$ into $F_{\ast p}$.
>
> *Step 1: an adapted chart at $q$.* Since $q \in S$ and $S$ is a regular submanifold of codimension $k$, there is a smooth chart $(U, \varphi = (x^1, \ldots, x^n))$ of $N$ with $q \in U$ and
>
> $$
> U \cap S = \{\, q' \in U : x_b(q') = \vec 0 \,\}, \qquad x_a = (x^1, \ldots, x^{n-k}), \quad x_b = (x^{n-k+1}, \ldots, x^n)
> $$
>
> (Definitions [[§37 Regular Submanifolds#^def-37-2|§37.2]] and [[§37 Regular Submanifolds#^def-37-3|§37.3]]). By Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], applied to $S \subseteq N$,
>
> $$
> \iota_{\ast q}\big(T_qS\big) = \operatorname{Span}\Big\{\frac{\partial}{\partial x^1}\Big|_q, \ldots, \frac{\partial}{\partial x^{n-k}}\Big|_q\Big\} .
> $$
>
> *Step 2: the map $x_b$ and its differential.* Regard $x_b : U \to \mathbb{R}^k$ as a map from the open submanifold $U$ to $\mathbb{R}^k$, the latter with the identity chart, whose coordinate functions are $r^1, \ldots, r^k$. Its coordinate representation in the charts $(U, \varphi)$ and $(\mathbb{R}^k, \mathrm{id})$ is
>
> $$
> \mathrm{id} \circ x_b \circ \varphi^{-1}\big(r^1, \ldots, r^n\big) = \big(r^{n-k+1}, \ldots, r^n\big) \qquad \text{on } \varphi(U),
> $$
>
> because the $l$-th entry of $\varphi(q')$ is $x^l(q')$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]). This is a linear map, hence smooth, so $x_b$ is smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]). Its components are $x_b^{\,j} = r^j \circ x_b = x^{n-k+j}$, $j = 1, \ldots, k$, and the Jacobian of the coordinate representation at every point is the $k \times n$ matrix $(0 \mid I_k)$: $\partial r^{n-k+j}/\partial r^i = \delta^{n-k+j}_i$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], whose upstairs partials $\partial x_b^{\,j}/\partial x^i(q) = \partial x^{n-k+j}/\partial x^i(q)$ are the entries of this Jacobian, at $q$ (where $x_b(q) = \vec 0$, as $q \in U \cap S$),
>
> $$
> (x_b)_{\ast q}\Big(\frac{\partial}{\partial x^i}\Big|_q\Big) = \sum_{j=1}^k \frac{\partial x^{n-k+j}}{\partial x^i}(q)\, \frac{\partial}{\partial r^j}\Big|_{\vec 0} = \sum_{j=1}^k \delta^{n-k+j}_i\, \frac{\partial}{\partial r^j}\Big|_{\vec 0} =
> \begin{cases} 0, & i \le n - k, \\[2pt] \dfrac{\partial}{\partial r^{\,i-(n-k)}}\Big|_{\vec 0}, & i > n - k. \end{cases}
> $$
>
> Two consequences.
>
> 1. [(a)] *$(x_b)_{\ast q}$ is onto $T_{\vec 0}\mathbb{R}^k$.* Its image is a subspace containing, by the second case, every vector $\partial/\partial r^j|_{\vec 0}$ of the coordinate basis of $T_{\vec 0}\mathbb{R}^k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]), hence their span, which is everything.
> 2. [(b)] *$\ker (x_b)_{\ast q} = \iota_{\ast q}(T_qS)$.* By the first case, $(x_b)_{\ast q}$ kills $\partial/\partial x^1|_q, \ldots, \partial/\partial x^{n-k}|_q$, hence, being linear, their span; by Step 1 that span is $\iota_{\ast q}(T_qS)$, so $\iota_{\ast q}(T_qS) \subseteq \ker (x_b)_{\ast q}$. The span has dimension $n - k$, its spanning vectors being part of a basis of $T_qN$. On the other side, by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) with $\dim T_qN = n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]) and $\operatorname{rank}(x_b)_{\ast q} = k$ by (a),
>
> $$
> \dim \ker (x_b)_{\ast q} = \dim T_qN - \operatorname{rank}(x_b)_{\ast q} = n - k .
> $$
>
> A subspace of the same finite dimension is the whole space, so $\iota_{\ast q}(T_qS) = \ker (x_b)_{\ast q}$.
>
> *Step 3: a chart at $p$ mapped into $U$, and the map $G$.* $F$ is continuous, so $F^{-1}(U)$ is an open set containing $p$. Take any smooth chart $(\tilde V, \tilde\psi)$ of $M$ at $p$ and put $V = \tilde V \cap F^{-1}(U)$, an open set containing $p$ with $F(V) \subseteq U$; the restriction of $\tilde\psi$ to $V$ is again a smooth chart (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)). Define
>
> $$
> G = x_b \circ F|_V : V \longrightarrow \mathbb{R}^k .
> $$
>
> It is smooth: $F|_V$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-5|§19.5]](2)), and smooth as a map into the open submanifold $U$, since it takes values in $U$ and its composite with the inclusion $U \hookrightarrow N$ is the smooth map $F|_V$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-5|§19.5]](3)); then $G$ is a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]). By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and the identifications $T_pV = T_pM$, $T_qU = T_qN$,
>
> $$
> G_{\ast p} = (x_b)_{\ast q} \circ F_{\ast p} : T_pM \longrightarrow T_{\vec 0}\mathbb{R}^k .
> $$
>
> *Step 4: $G$ cuts out $F^{-1}(S)$ in $V$.* For $p' \in V$ we have $F(p') \in U$, so
>
> $$
> G(p') = \vec 0 \iff x_b\big(F(p')\big) = \vec 0 \iff F(p') \in U \cap S \iff F(p') \in S \iff p' \in F^{-1}(S) :
> $$
>
> the first equivalence is the definition of $G$; the second is Step 1, $F(p')$ being a point of $U$; the third holds because $F(p') \in U$ anyway. Hence $G^{-1}(\vec 0) = V \cap F^{-1}(S)$.
>
> *Step 5: $G$ is a submersion at $p$.* We show $G_{\ast p}$ is onto. Let $w \in T_{\vec 0}\mathbb{R}^k$. By Step 2(a) there is $u \in T_qN$ with $(x_b)_{\ast q}u = w$. By transversality at $p$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]), $u = F_{\ast p}v + t$ with $v \in T_pM$ and $t \in \iota_{\ast q}(T_qS)$, and $(x_b)_{\ast q}t = 0$ by Step 2(b). By linearity of $(x_b)_{\ast q}$ and Step 3,
>
> $$
> w = (x_b)_{\ast q}u = (x_b)_{\ast q}F_{\ast p}v + (x_b)_{\ast q}t = (x_b)_{\ast q}F_{\ast p}v + 0 = G_{\ast p}v .
> $$
>
> So $G_{\ast p}$ is onto, i.e. $G$ is a submersion at $p$ (Definition [[§36 Submersions#^def-36-1|§36.1]]). In particular $k \le m$: a surjective linear map $T_pM \to T_{\vec 0}\mathbb{R}^k$ has $\dim T_pM \ge \dim T_{\vec 0}\mathbb{R}^k$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), and these dimensions are $m$ and $k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]).
>
> *Step 6: the normal form of $G$ at $p$.* The normal form (Theorem [[§36 Submersions#^thm-36-4|§36.4]]) requires $G$ to be a submersion only at the one point $p$, which is Step 5. (That $G$ is then a submersion on a whole neighbourhood of $p$, Corollary [[§36 Submersions#^cor-36-5|§36.5]], is a consequence of the normal form, not a hypothesis of it; no shrinking of $V$ is needed.) Applied to $G : V \to \mathbb{R}^k$ at $p$, it gives smooth charts $(W, \theta = (z^1, \ldots, z^m))$ of $V$ at $p$ and $(Y, \chi)$ of $\mathbb{R}^k$ at $G(p) = \vec 0$, with $G(W) \subseteq Y$ and
>
> $$
> \chi \circ G \circ \theta^{-1}\big(r^1, \ldots, r^m\big) = \big(r^1, \ldots, r^k\big) \quad \text{on } \theta(W),
> $$
>
> that is, $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^k(p')\big)$ for $p' \in W$ (apply the first identity at $\theta(p')$).
> Since $W \subseteq V$ is open in $V$, hence in $M$, $(W, \theta)$ is also a smooth chart of $M$ (Proposition [[§17 Differentiable Structures#^prop-17-6|§17.6]](2)). Put $\vec c = \chi(\vec 0) = (c_1, \ldots, c_k)$.
>
> *Step 7: an adapted chart at $p$.* For $p' \in W$,
>
> $$
> p' \in F^{-1}(S) \iff G(p') = \vec 0 \iff \chi\big(G(p')\big) = \chi(\vec 0) \iff \big(z^1(p'), \ldots, z^k(p')\big) = (c_1, \ldots, c_k) .
> $$
>
> The first equivalence is Step 4, as $W \subseteq V$; the second holds because $G(p')$ and $\vec 0$ both lie in $Y$ (as $G(W) \subseteq Y$), on which $\chi$ is injective; the third is the normal form of Step 6. So
>
> $$
> W \cap F^{-1}(S) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^k(p') = c_k \,\} ,
> $$
>
> the intersection cut out in the smooth chart $(W, \theta)$ of $M$ by setting $k$ of its coordinates equal to constants. By Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] — with the coordinates $z^1, \ldots, z^k$ and the constant vector $\vec c$ — there is a chart of $M$ with domain $W$ adapted to $F^{-1}(S)$, of codimension $k$: explicitly, $\big(z^{k+1}, \ldots, z^m, \ z^1 - c_1, \ldots, z^k - c_k\big)$, the translation and permutation of the student's solution. Here $k \le m$ by Step 5.
>
> *Conclusion of (1).* As $p \in F^{-1}(S)$ was arbitrary, every point of $F^{-1}(S)$ lies in a chart of $M$ adapted to $F^{-1}(S)$ with $k$ equations, so $F^{-1}(S)$ is a regular submanifold of $M$ of codimension $k$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), and $\dim F^{-1}(S) = m - k$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]. The codimension of $S$ in $N$ is also $k$, by hypothesis.
>
> *(2): $j_{\ast p}(T_pF^{-1}(S)) \subseteq \ker G_{\ast p}$.* The set $V \cap F^{-1}(S)$ is open in $F^{-1}(S)$ (subspace topology) and contains $p$, so its tangent space at $p$ is $T_pF^{-1}(S)$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]). On it the composite $G \circ j$ is defined (as $j$ maps it into $V$; its restriction is smooth into the open set $V$ by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) and Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-5|§19.5]](3)) and constant with value $\vec 0$, by Step 4. The differential of a constant map is zero: for a derivation $D$ at $p$ and a germ $[g]$ at $\vec 0$, $(G \circ j)_{\ast p}D\,[g] = D[g \circ G \circ j]$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]), and $g \circ G \circ j$ is the constant $g(\vec 0)$ near $p$, whose germ $D$ kills (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]](1)). So, by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]),
>
> $$
> G_{\ast p} \circ j_{\ast p} = (G \circ j)_{\ast p} = 0 ,
> $$
>
> that is, $G_{\ast p}(j_{\ast p}v) = 0$ for every $v \in T_pF^{-1}(S)$.
>
> *(2): dimensions.* $j_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], for the submanifold $F^{-1}(S) \subseteq M$), so, by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]] and (1),
>
> $$
> \dim j_{\ast p}\big(T_pF^{-1}(S)\big) = \dim T_pF^{-1}(S) = \dim F^{-1}(S) = m - k .
> $$
> On the other side, $G_{\ast p}$ is onto the $k$-dimensional space $T_{\vec 0}\mathbb{R}^k$ (Step 5), so by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1))
>
> $$
> \dim \ker G_{\ast p} = \dim T_pM - \operatorname{rank} G_{\ast p} = m - k .
> $$
>
> A subspace of the same finite dimension is the whole space, so $j_{\ast p}(T_pF^{-1}(S)) = \ker G_{\ast p}$.
>
> *(2): the kernel of $G_{\ast p}$.* By Step 3, the definition of the kernel, and Step 2(b),
>
> $$
> \begin{aligned}\ker G_{\ast p} &= \big\{\, v \in T_pM : (x_b)_{\ast q}\big(F_{\ast p}v\big) = 0 \,\big\} \\
> &= \big\{\, v \in T_pM : F_{\ast p}v \in \ker (x_b)_{\ast q} \,\big\} = \big\{\, v \in T_pM : F_{\ast p}v \in \iota_{\ast q}(T_qS) \,\big\} ,\end{aligned}
> $$
>
> which is $(F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big)$. With the previous paragraph, $j_{\ast p}(T_pF^{-1}(S)) = (F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big)$. This is the argument of the tangent-space half of Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]], run for $G$, followed by the computation of $\ker G_{\ast p}$ that ends the proof of Theorem [[§26 Transversality#^thm-26-1|§26.1]].

^pf-37-12

*Uses:* [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^thm-37-9|§37.9]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§19 Smooth Functions and Smooth Maps#^prop-19-5|§19.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§36 Submersions#^thm-36-4|§36.4]], [[§36 Submersions#^cor-36-5|§36.5]], [[§17 Differentiable Structures#^prop-17-6|§17.6]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-2|§28.2]], [[§26 Transversality#^thm-26-1|§26.1]]

> [!theorem] Proposition §37.13: Normal Spaces Under a Transverse Map
> Let $F : M \to N$ be smooth, $S \subseteq N$ a regular submanifold of codimension $k$ with inclusion $\iota$, $p \in F^{-1}(S)$ and $q = F(p)$. Put
>
> $$
> K_p = (F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big) \subseteq T_pM .
> $$
>
> 1. $F_{\ast p}$ induces a well-defined linear map of quotient spaces (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]])
>
> $$
> \bar F_{\ast p} : T_pM / K_p \longrightarrow T_qN / \iota_{\ast q}(T_qS), \qquad v + K_p \longmapsto F_{\ast p}v + \iota_{\ast q}(T_qS) .
> $$
>
> 2. $\bar F_{\ast p}$ is injective.
> 3. $\bar F_{\ast p}$ is surjective if and only if $F$ is transverse to $S$ at $p$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]).
>
> So if $F \pitchfork S$, then $K_p = j_{\ast p}(T_pF^{-1}(S))$, with $j$ the inclusion of $F^{-1}(S)$ (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]) and $\bar F_{\ast p}$ is an isomorphism $T_pM/T_pF^{-1}(S) \cong T_qN/T_qS$ of the normal spaces: both have dimension $k$, which is the reason the codimension is preserved.

^prop-37-13

> [!proof]+ Proof
> *(Not from lecture.)* Write $E = \iota_{\ast q}(T_qS)$, a subspace of $T_qN$ (the image of a linear map), and $\pi_N : T_qN \to T_qN/E$, $\pi_M : T_pM \to T_pM/K_p$ for the projections. $K_p$ is a subspace of $T_pM$, as the preimage of the subspace $E$ under the linear map $F_{\ast p}$: if $F_{\ast p}v, F_{\ast p}v' \in E$, then $F_{\ast p}(v + cv') = F_{\ast p}v + c\,F_{\ast p}v' \in E$. Throughout, two vectors have the same coset iff their difference lies in the subspace (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]]).
>
> *(1)* Let $A = \pi_N \circ F_{\ast p} : T_pM \to T_qN/E$, $A(v) = F_{\ast p}v + E$, linear as a composite of linear maps (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)). Its kernel is $K_p$: by $\ker \pi_N = E$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)),
>
> $$
> A(v) = 0 \iff \pi_N\big(F_{\ast p}v\big) = 0 \iff F_{\ast p}v \in E \iff v \in K_p .
> $$
>
> In particular $K_p \subseteq \ker A$, so by the universal property (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](2)) there is a unique linear $\bar F_{\ast p} : T_pM/K_p \to T_qN/E$ with $\bar F_{\ast p} \circ \pi_M = A$, namely $\bar F_{\ast p}(v + K_p) = A(v) = F_{\ast p}v + E$ — the map of (1), well defined and linear.
>
> *(2)* Suppose $\bar F_{\ast p}(v + K_p) = 0$. Then $A(v) = 0$, so $v \in \ker A = K_p$ by (1), i.e. $v + K_p = 0 + K_p$, the zero of $T_pM/K_p$. A linear map with zero kernel is injective.
>
> *(3)* Since $\pi_M$ is surjective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](1)), every element of $T_pM/K_p$ is some $v + K_p$, and the image of $\bar F_{\ast p}$ is $\{F_{\ast p}v + E : v \in T_pM\}$. So, by the criterion for equal cosets,
>
> $$
> \begin{aligned}\bar F_{\ast p} \text{ is surjective} &\iff \text{for every } u \in T_qN \text{ there is } v \in T_pM \text{ with } u + E = F_{\ast p}v + E \\
> &\iff \text{for every } u \in T_qN \text{ there is } v \in T_pM \text{ with } u - F_{\ast p}v \in E \\
> &\iff \text{every } u \in T_qN \text{ lies in } F_{\ast p}(T_pM) + E .\end{aligned}
> $$
>
> For the last equivalence: if $u - F_{\ast p}v = t \in E$, then $u = F_{\ast p}v + t$ lies in the sum; conversely if $u = F_{\ast p}v + t$ with $t \in E$, then $u - F_{\ast p}v = t \in E$. The last condition says $F_{\ast p}(T_pM) + \iota_{\ast q}(T_qS) = T_qN$, since the sum is a subspace of $T_qN$ in any case; this is transversality at $p$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]).
>
> *The transverse case.* If $F \pitchfork S$, then $\bar F_{\ast p}$ is injective by (2) and surjective by (3), hence an isomorphism, and $K_p = j_{\ast p}(T_pF^{-1}(S))$ by Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]](2). The dimensions are $\dim T_pM = m$ and $\dim T_qN = n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]); $\dim E = \dim T_qS = n - k$, as $\iota_{\ast q}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]); and $\dim K_p = m - k$ (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]](1)). So by Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](3)
>
> $$
> \dim T_pM/K_p = m - (m - k) = k = n - (n - k) = \dim T_qN/E ,
> $$
>
> as an isomorphism requires. Read backwards, the isomorphism alone gives $\dim K_p = m - \dim T_qN/E = m - k$: the codimension of $F^{-1}(S)$ in $M$ is the dimension of its normal space $T_pM/K_p$, and transversality makes $F_{\ast p}$ carry that normal space isomorphically onto the normal space of $S$, of dimension $k$.

^pf-37-13

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-6|Def. §21.6]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]], [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]]

> [!remark] Remark: Special Cases of Transversality
> *(Not from lecture.)* Let $F : M \to N$ be smooth, $\dim M = m$, $\dim N = n$.
>
> 1. *A point.* For $c \in N$, $\{c\}$ is a regular submanifold of $N$ of codimension $n$: it is the fibre $\mathrm{id}_N^{-1}(c)$ of the identity, a submersion since $(\mathrm{id}_N)_{\ast} = \mathrm{id}$ (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), so Corollary [[§37 Regular Submanifolds#^cor-37-10|§37.10]] applies. Its tangent space is $0$ (dimension $n - n = 0$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-8|§29.8]]), so transversality at $p \in F^{-1}(c)$ reads $F_{\ast p}(T_pM) + 0 = T_cN$: $F_{\ast p}$ is onto. Thus $F \pitchfork \{c\}$ iff $F$ is a submersion at every point of $F^{-1}(c)$, iff $c$ is a regular value (Definition [[§36 Submersions#^def-36-4|§36.4]], the empty case included). Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] then returns the regular value theorem, Theorem [[§37 Regular Submanifolds#^thm-37-9|§37.9]]: $F^{-1}(c)$ is a regular submanifold of codimension $n$, and $j_{\ast p}(T_pF^{-1}(c)) = (F_{\ast p})^{-1}(0) = \ker F_{\ast p}$. This is the manifold version of Corollary [[§26 Transversality#^cor-26-3|§26.3]].
> 2. *Two submanifolds.* Let $S' \subseteq N$ be another regular submanifold, of codimension $k'$, and $F = \iota' : S' \to N$ its inclusion. Then $F^{-1}(S) = S' \cap S$ and $F_{\ast p}(T_pS') = \iota'_{\ast p}(T_pS')$, so $\iota' \pitchfork S$ says
>
> $$
> \iota'_{\ast p}\big(T_pS'\big) + \iota_{\ast p}\big(T_pS\big) = T_pN \qquad \text{for every } p \in S' \cap S ,
> $$
>
> a condition symmetric in $S$ and $S'$: the two submanifolds *intersect transversally*. In that case the theorem makes $S' \cap S$ a regular submanifold of $S'$ of codimension $k = \operatorname{codim} S$, so of dimension $(n - k') - k = n - (k' + k)$ — the codimensions add, as for level sets in Proposition [[§26 Transversality#^prop-26-4|§26.4]] — and its tangent space, inside $T_pS'$, consists of the vectors whose image in $T_pN$ lies in $\iota_{\ast p}(T_pS)$: with all tangent spaces regarded as subspaces of $T_pN$, $T_p(S' \cap S) = T_pS' \cap T_pS$.
> 3. *Submersions.* If $F$ is a submersion, then $F_{\ast p}(T_pM) = T_{F(p)}N$ already, so $F$ is transverse to *every* regular submanifold $S \subseteq N$, and $F^{-1}(S)$ is a regular submanifold of the same codimension. For $S = \{c\}$ a point this is Corollary [[§37 Regular Submanifolds#^cor-37-10|§37.10]]: a submersion is transverse to every point, and its fibres are regular submanifolds of codimension $n$.
>
> *Lee: Theorem 6.30(b), for (2)*

^rem-37-4
