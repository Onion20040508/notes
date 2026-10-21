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

*(Not from lecture.)* Which subsets of a smooth manifold $M$ inherit a smooth structure from $M$? An arbitrary subset with the subspace topology need not even be a manifold — $\mathbb{Q} \subseteq \mathbb{R}$ is not locally Euclidean (the remark *What Subspaces Do Not Inherit* in [[§3 Subspaces and Products#^rem-3-3|§3]]) — and when it is a lower-dimensional one, the charts of $M$ do not restrict to charts of it: for a chart $(U, \varphi)$, the set $\varphi(U \cap S)$ is in general not open in $\mathbb{R}^m$ (for the circle in $\mathbb{R}^2$ it is a piece of a curve). Open subsets are the easy case: the charts of $M$ simply restrict (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]]). Regular submanifolds, in the rest of this section, are the general answer, and the two meet in codimension $0$ (Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]]).

> [!definition] Definition §37.1: Open Submanifold of a Smooth Manifold
> An **open submanifold** of a smooth manifold $M$ is an open subset $S \subseteq M$ with the subspace topology and the smooth structure of Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]], whose charts are the smooth charts of $M$ with domain in $S$. It is the smooth counterpart of Definition [[§3 Subspaces and Products#^def-3-2|§3.2]]; its inclusion into $M$ is smooth, and maps into $S$ are smooth exactly when they are smooth into $M$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]]).

^def-37-1

> [!theorem] Proposition §37.1: Open Subsets of a Product
> Let $M_1$, $M_2$ be smooth manifolds and $U \subseteq M_1$ open. Then $U \times M_2$ is open in $M_1 \times M_2$, and the open submanifold $U \times M_2$ of $M_1 \times M_2$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]) is the same smooth manifold as the product manifold $U \times M_2$ of the open submanifold $U$ with $M_2$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-7|§19.7]]). In particular the projection $\mathrm{pr}_1 : U \times M_2 \to U$ is the restriction to $U \times M_2$ of the projection $\mathrm{pr}_1 : M_1 \times M_2 \to M_1$ (Definition [[§3 Subspaces and Products#^def-3-4|§3.4]]).

^prop-37-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Open.* $U \times M_2 = \mathrm{pr}_1^{-1}(U)$, open because $\mathrm{pr}_1$ is continuous (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]]).
>
> *Same topology.* The product topology of $U \times M_2$ has the basis of sets $A' \times B$ with $A'$ open in $U$ and $B$ open in $M_2$ (Definition [[§3 Subspaces and Products#^def-3-3|§3.3]]); since $U$ is open, the sets $A'$ open in $U$ are the sets $A \cap U$ with $A$ open in $M_1$. The subspace topology of $U \times M_2$ in $M_1 \times M_2$ has the basis of sets $(A \times B) \cap (U \times M_2) = (A \cap U) \times B$. The two bases are the same, so the topologies agree.
>
> *Same smooth structure.* A product chart of $U \times M_2$ is $(U_1 \times U_2, \varphi_1 \times \varphi_2)$ with $(U_1, \varphi_1)$ a smooth chart of the open submanifold $U$ and $(U_2, \varphi_2)$ one of $M_2$. By Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2), $(U_1, \varphi_1)$ is a smooth chart of $M_1$ with $U_1 \subseteq U$, so $(U_1 \times U_2, \varphi_1 \times \varphi_2)$ is a product chart of $M_1 \times M_2$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]) with domain in $U \times M_2$ — a smooth chart of the open submanifold $U \times M_2$, by Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2) again. So the product charts of $U \times M_2$, an atlas generating its product structure, all lie in the smooth structure of the open submanifold; by the uniqueness in Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]] the two smooth structures are equal.
>
> *The projection.* Both maps send $(b, y)$ to $b$.

^pf-37-1

*Uses:* [[§19 Smooth Functions and Smooth Maps#^prop-19-11|§19.11]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

## Regular Submanifolds

*Lecture 12 (Mon Sep 28). “I know we're in the middle of discussing submersions and fibrations, but we need the notion of submanifold. So let's pause to discuss that. It's not difficult.” The local model is a lower-dimensional Euclidean space inside a higher-dimensional one: $\mathbb{R}^{m-k} \subseteq \mathbb{R}^m$ as the points whose last $k$ coordinates vanish, $x \mapsto (x, \vec 0)$.*

> [!definition] Definition §37.2: Regular Submanifold
> Let $M$ be a smooth manifold of dimension $m$, $S \subseteq M$ a subset with the subspace topology, and $0 \le k \le m$. For a chart $\varphi = (x^1, \ldots, x^m)$ write $x_a = (x^1, \ldots, x^{m-k})$ for its first $m - k$ components and $x_b = (x^{m-k+1}, \ldots, x^m)$ for its last $k$. Then $S$ is a **regular submanifold of $M$ of codimension $k$** if every $p \in S$ lies in the domain of a smooth chart $(U, \varphi)$ of $M$ with
>
> $$
> U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\}.
> $$
>
> Regular submanifolds are also called **embedded** submanifolds, as opposed to the [[§42 Embeddings#^def-42-4|immersed submanifolds]] of [[§42 Embeddings#^def-42-4|Definition §42.4]]. In these notes, “submanifold” without qualification means a regular submanifold.
>
> *Lee: Theorem 5.8*

^def-37-2

> [!remark]- Connections
> - The other kind of submanifold: [[§42 Embeddings#^def-42-4|immersed submanifolds, Def. §42.4]]; when an immersed submanifold is regular: [[§42 Embeddings#^prop-42-15|§42.15]]; local images of immersions: [[§41 Immersions#^cor-41-2|§41.2]].
> - Codimension in the Euclidean setting: [[§26 Transversality#^def-26-1|Def. §26.1]].
> - The geometric stage: in $\mathbb{R}^{n+k}$ the submanifolds are exactly the manifolds of [[§20 Manifolds in Euclidean Space|§20]] — the external, internal and graph descriptions ([[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]) — and the slice of this definition is a fourth: [[§37 Regular Submanifolds#^prop-37-9|§37.9]].
> - Their tangent spaces: $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) is $\iota_{\ast p}(T_pX)$ ([[§37 Regular Submanifolds#^rem-37-2|Remark: The Tangent Spaces Match]], [[§37 Regular Submanifolds#^prop-37-14|§37.14]]).

> [!definition] Definition §37.3: Adapted Chart
> Let $M$, $S$ and $k$ be as in [[§37 Regular Submanifolds#^def-37-2|Definition §37.2]]. Such charts — smooth charts $(U, \varphi)$ of $M$ with $U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\}$ — are **adapted** to $S$; “a random chart of $M$ is not adapted.” In an adapted chart, $U \cap S$ is cut out by the $k$ equations $x^{m-k+1} = \cdots = x^m = 0$, exactly as in the local model.
>
> *Lee: Theorem 5.8*

^def-37-3

> [!remark]- Connections
> - In Euclidean space an adapted chart comes from a graph chart ([[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) by straightening the graph: [[§37 Regular Submanifolds#^prop-37-9|§37.9]] and its figure.

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
> Then $A = T \circ P$ is an affine diffeomorphism of $\mathbb{R}^m$, with inverse $A^{-1}(s) = P^{-1}\big(s + (\vec 0, \vec c)\big)$, so $(U, A \circ \varphi)$ is a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](2), applied with $h = A$: a diffeomorphism of $\mathbb{R}^m$ onto itself (the components of $A$ and of $A^{-1}$ are affine, hence smooth), defined on all of $\mathbb{R}^m \supseteq \varphi(U)$. (In that lemma the transition maps with a smooth chart $(V, \chi)$ are $(A \circ \varphi) \circ \chi^{-1} = A \circ (\varphi \circ \chi^{-1})$ and $\chi \circ (A \circ \varphi)^{-1} = (\chi \circ \varphi^{-1}) \circ A^{-1}$, composites of smooth maps.) Its last $k$ coordinates are $x^{i_1} - c_1, \ldots, x^{i_k} - c_k$, which vanish exactly on $U \cap S$: for $q \in U$,
>
> $$
> (A \circ \varphi)(q) = \big(x^{j_1}(q), \ldots, x^{j_{m-k}}(q),\ x^{i_1}(q) - c_1, \ldots, x^{i_k}(q) - c_k\big),
> $$
>
> and its last $k$ entries are all $0$ if and only if $x^{i_l}(q) = c_l$ for $l = 1, \ldots, k$, that is (by hypothesis), if and only if $q \in U \cap S$. So $(U, A \circ \varphi)$ is adapted (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]). Observation (1) is the case $(i_1, \ldots, i_k) = (m-k+1, \ldots, m)$, where $P$ is the identity; observation (2) is the case $\vec c = \vec 0$, where $T$ is the identity.

^pf-37-2

*Uses:* [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]]

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
> *(1)* Let $S$ be open and $p \in S$. For a smooth chart $(U, \varphi)$ of $M$ at $p$, its restriction $(U \cap S, \varphi|_{U \cap S})$ is a smooth chart of $M$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2)) with domain inside $S$, hence adapted with $k = 0$. So $S$ is a regular submanifold of codimension $0$. The induced chart of an adapted chart $(U, \varphi)$ with $U \subseteq S$ is $\varphi_S = x_a|_{U \cap S} = \varphi$, the chart itself; so the atlas $\mathcal{A}_S$ of Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]] consists of the smooth charts of $M$ with domain in $S$, which generate the open-submanifold structure (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2)). The two smooth structures are therefore equal (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> *(2)* Let $S$ be a regular submanifold of codimension $0$. Each $p \in S$ lies in the domain $U_p$ of an adapted chart, and $U_p \subseteq S$ by the observation above. So $S = \bigcup_{p \in S} U_p$ is a union of open sets of $M$, hence open.

^pf-37-4

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§17 Differentiable Structures#^thm-17-5|§17.5]]

![[m591-15-1.svg]]
*An adapted chart ($m = 2$, $k = 1$). The chart $\varphi$ straightens $U \cap S$ onto the part of the $x_a$-axis inside $\varphi(U)$ — exactly the set $\varphi(U) \cap \{x_b = 0\}$, running from rim to rim — and the induced chart $\varphi_S$ keeps only the coordinate $x_a$, landing on an open interval of $\mathbb{R}^{m-k}$.*

> [!remark]- Connections
> - The subspace topology: [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]].
> - The Euclidean prototype, level sets with graph charts: [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]; the two structures agree by [[§37 Regular Submanifolds#^prop-37-14|§37.14]].

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
> (2) $G$ is continuous into $S$, since $G^{-1}(O \cap S) = G^{-1}(O)$ for $O$ open in $M$ (because $G(X) \subseteq S$), and the sets $O \cap S$ are the open sets of $S$. Given $x \in X$, take an adapted chart $(U, \varphi)$ at $G(x)$ and a chart $\chi$ of $X$ at $x$ with domain inside $G^{-1}(U)$ — the restriction of any smooth chart at $x$ to its intersection with the open set $G^{-1}(U)$, again a smooth chart (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1)). Its domain is then mapped by $G$ into $U \cap S$, the domain of the induced chart $\varphi_S$. Then $\varphi_S \circ G \circ \chi^{-1} = \mathrm{pr} \circ (\varphi \circ G \circ \chi^{-1})$, a linear map composed with a coordinate representation of the smooth map $G$, hence smooth: $\varphi \circ G \circ \chi^{-1}$ is smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], and $\varphi_S = \mathrm{pr} \circ \varphi$ on $U \cap S$. So $G : X \to S$ is smooth by Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]].

^pf-37-5

*Uses:* [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§17 Differentiable Structures#^lem-17-6|§17.6]]

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
> *(Lecture 12: “immediate from the definitions”; filled in.)* Fix an adapted chart $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and its induced chart $(U \cap S, \varphi_S)$ of $S$, whose coordinate functions are $x^1, \ldots, x^{m-k}$ restricted to $U \cap S$; by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]] the $\partial/\partial x^i|^S_p$, $i \le m - k$, form a basis of $T_pS$, and the $\partial/\partial x^l|_p$, $l \le m$, a basis of $T_pM$.
>
> *The formula.* By Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) the coordinate representation of $\iota$ is $j$, whose Jacobian is the $m \times (m-k)$ matrix $\binom{I_{m-k}}{0}$: the components of $j(r) = (r, \vec 0)$ are $j^l(r) = r^l$ for $l \le m - k$ and $j^l(r) = 0$ for $l > m - k$, so $\partial j^l/\partial r^i = \delta^l_i$ for $l \le m - k$ and $0$ for $l > m - k$. Written out, at every point,
>
> $$
> j'(r) = \left(\begin{array}{ccc} 1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 1 \\ \hline 0 & \cdots & 0 \\ \vdots & & \vdots \\ 0 & \cdots & 0 \end{array}\right) = \begin{pmatrix} I_{m-k} \\ 0 \end{pmatrix} \qquad (m \text{ rows}, \ m - k \text{ columns}).
> $$
> By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] this is the matrix of $\iota_{\ast p}$ in the coordinate bases; its $i$-th column gives the formula. Explicitly, the formula of that theorem, with the upstairs partials replaced by the entries of the Jacobian of $j$, reads
>
> $$
> \iota_{\ast p}\Big(\frac{\partial}{\partial x^i}\Big|^S_p\Big) = \sum_{l=1}^m \frac{\partial j^l}{\partial r^i}\big(\varphi_S(p)\big)\, \frac{\partial}{\partial x^l}\Big|_p = \sum_{l=1}^{m-k} \delta^l_i\, \frac{\partial}{\partial x^l}\Big|_p = \frac{\partial}{\partial x^i}\Big|_p \qquad (i \le m - k).
> $$
>
> *The image.* $\iota_{\ast p}$ is linear, so it maps $T_pS$, the span of the basis $\partial/\partial x^i|^S_p$ ($i \le m - k$), onto the span of their images, which by the formula is $\operatorname{Span}\{\partial/\partial x^1|_p, \ldots, \partial/\partial x^{m-k}|_p\}$.
>
> *Injectivity.* The columns of $\binom{I_{m-k}}{0}$ are independent, so $\iota_{\ast p}$ is injective. In terms of vectors: if $\iota_{\ast p}\big(\sum_i a_i\, \partial/\partial x^i|^S_p\big) = \sum_i a_i\, \partial/\partial x^i|_p = 0$, then every $a_i = 0$, because the $\partial/\partial x^i|_p$ are part of a basis of $T_pM$.
>
> *Curves.* The statement for curves is Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], applied to the smooth map $F = \iota$ and a smooth curve $\gamma$ in $S$ with $\gamma(0) = p$: it gives $\iota_{\ast p} D_\gamma = D_{\iota \circ \gamma}$, where $\iota \circ \gamma$ is $\gamma$ regarded as a curve in $M$, smooth by Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]].

^pf-37-6

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]

So $T_pS$ is identified with the $(m-k)$-dimensional subspace $\iota_{*p}(T_pS) \subseteq T_pM$, the “intrinsic tangent space” inside the ambient one — “for some reason this class, and maybe all abstract classes, keep identifying things with each other.” The second description is the one from Assignment 3, Problem 2: think of a curve in $S$ composed with the inclusion as a curve in $M$, and take its velocity there.

> [!theorem] Proposition §37.7: Adapted Charts Give Local Defining Maps
> Let $S \subseteq M$ be a regular submanifold of codimension $k$ and $(U, \varphi = (x_a, x_b))$ a chart adapted to $S$, with $x_b = (x^{m-k+1}, \ldots, x^m) : U \to \mathbb{R}^k$, a map from the open submanifold $U$ to $\mathbb{R}^k$ with its standard coordinates $r^1, \ldots, r^k$.
>
> 1. $x_b$ is smooth, and for every $q \in U$
>
> $$
> (x_b)_{\ast q}\Big(\frac{\partial}{\partial x^i}\Big|_q\Big) = \begin{cases} 0, & i \le m - k, \\[2pt] \dfrac{\partial}{\partial r^{\,i-(m-k)}}\Big|_{x_b(q)}, & i > m - k. \end{cases}
> $$
>
> 2. $x_b$ is a submersion at every point of $U$.
> 3. $U \cap S = x_b^{-1}(\vec 0)$, and $\vec 0$ is a regular value of $x_b$.
> 4. For every $q \in U \cap S$, $\iota_{\ast q}(T_qS) = \ker (x_b)_{\ast q}$.
>
> In particular, a regular submanifold is locally a regular level set: every point of $S$ has an open neighbourhood $U$ in $M$ on which $U \cap S$ is the preimage of the regular value $\vec 0$ of a smooth map $U \to \mathbb{R}^k$.

^prop-37-7

> [!proof]+ Proof
> *(Not from lecture; filled in. The computation is Step 2 of the submitted solution of Assignment 5, Problem 2, and the last sentence is the remark of Assignment 5, Problem 4, that a regular submanifold is locally a regular level set.)* Throughout, the tangent space of the open set $U$ at $q$ is identified with $T_qM$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), and $\mathbb{R}^k$ carries the identity chart, whose coordinate functions are $r^1, \ldots, r^k$.
>
> *(1)* The coordinate representation of $x_b$ in the charts $(U, \varphi)$ and $(\mathbb{R}^k, \mathrm{id})$ is
>
> $$
> \mathrm{id} \circ x_b \circ \varphi^{-1}\big(r^1, \ldots, r^m\big) = \big(r^{m-k+1}, \ldots, r^m\big) \qquad \text{on } \varphi(U),
> $$
>
> because the $l$-th entry of $\varphi(q')$ is $x^l(q')$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]). This is a linear map, hence smooth, so $x_b$ is smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]]). Its components are $x_b^{\,j} = r^j \circ x_b = x^{m-k+j}$, $j = 1, \ldots, k$, and the Jacobian of the coordinate representation at every point is the $k \times m$ matrix $(0 \mid I_k)$: $\partial r^{m-k+j}/\partial r^i = \delta^{m-k+j}_i$. Written out,
>
> $$
> \left(\begin{array}{ccc|ccc} 0 & \cdots & 0 & 1 & \cdots & 0 \\ \vdots & & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 1 \end{array}\right) = (0 \mid I_k) \qquad (k \text{ rows}; \ m - k \text{ zero columns, then } k).
> $$
> By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], whose upstairs partials $\partial x_b^{\,j}/\partial x^i(q) = \partial x^{m-k+j}/\partial x^i(q)$ are the entries of this Jacobian, for $q \in U$
>
> $$
> (x_b)_{\ast q}\Big(\frac{\partial}{\partial x^i}\Big|_q\Big) = \sum_{j=1}^k \frac{\partial x^{m-k+j}}{\partial x^i}(q)\, \frac{\partial}{\partial r^j}\Big|_{x_b(q)} = \sum_{j=1}^k \delta^{m-k+j}_i\, \frac{\partial}{\partial r^j}\Big|_{x_b(q)} =
> \begin{cases} 0, & i \le m - k, \\[2pt] \dfrac{\partial}{\partial r^{\,i-(m-k)}}\Big|_{x_b(q)}, & i > m - k. \end{cases}
> $$
>
> *(2)* Let $q \in U$. The image of $(x_b)_{\ast q}$ is a subspace containing, by the second case of (1), every vector $\partial/\partial r^j|_{x_b(q)}$ of the coordinate basis of $T_{x_b(q)}\mathbb{R}^k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), hence their span, which is everything. So $(x_b)_{\ast q}$ is onto, and $x_b$ is a submersion at $q$ (Definition [[§36 Submersions#^def-36-1|§36.1]]).
>
> *(3)* By Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]], $U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\} = x_b^{-1}(\vec 0)$. Every point of $x_b^{-1}(\vec 0)$ is a point of $U$, at which $x_b$ is a submersion by (2); so $\vec 0$ is a regular value of $x_b$ (Definition [[§36 Submersions#^def-36-4|§36.4]]).
>
> *(4)* Let $q \in U \cap S$; then $(U, \varphi)$ is an adapted chart at $q$. By the first case of (1), $(x_b)_{\ast q}$ kills $\partial/\partial x^1|_q, \ldots, \partial/\partial x^{m-k}|_q$, hence, being linear, their span; by Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]] that span is $\iota_{\ast q}(T_qS)$, so $\iota_{\ast q}(T_qS) \subseteq \ker (x_b)_{\ast q}$. The span has dimension $m - k$, its spanning vectors being part of a basis of $T_qM$. On the other side, by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) with $\dim T_qM = m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]) and $\operatorname{rank}(x_b)_{\ast q} = k$ by (2),
>
> $$
> \dim \ker (x_b)_{\ast q} = \dim T_qM - \operatorname{rank}(x_b)_{\ast q} = m - k .
> $$
>
> A subspace of the same finite dimension is the whole space, so $\iota_{\ast q}(T_qS) = \ker (x_b)_{\ast q}$.
>
> *The last sentence.* Every $p \in S$ lies in the domain $U$ of an adapted chart (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), an open neighbourhood of $p$ in $M$, and by (1) and (3) $U \cap S = x_b^{-1}(\vec 0)$ with $x_b : U \to \mathbb{R}^k$ smooth and $\vec 0$ a regular value.

^pf-37-7

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]

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

> [!theorem] Proposition §37.8: A Basis of the Conormal Space
> Let $(x^1, \ldots, x^m)$ be an adapted chart at $p$, and write a covector $\xi \in T_p^{\ast}M$ as $\xi = \sum_i \xi_i\, dx^i|_p$, with components $\xi_i = \xi(\partial/\partial x^i|_p)$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]).
>
> 1. $\xi \in N_pS$ if and only if $\xi_i = 0$ for every $i \le m - k$.
> 2. $N_pS$ has basis $dx^{m-k+1}|_p, \ldots, dx^m|_p$. In particular $\dim N_pS = k$, the codimension of $S$.

^prop-37-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Fix an adapted chart $(x^1, \ldots, x^m)$ at $p$. Write $\xi = \sum_j \xi_j\, dx^j|_p$ in the dual basis (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), so that $\xi(\partial/\partial x^i|_p) = \xi_i$. (By Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] the $dx^j|_p$ are the basis dual to the $\partial/\partial x^j|_p$, and the coefficients are the components $\xi_i = \xi(\partial/\partial x^i|_p)$ of Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]].)
>
> *(1)* By Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]], $\iota_{\ast p}(T_pS)$ is the span of $\partial/\partial x^1|_p, \ldots, \partial/\partial x^{m-k}|_p$, and a linear functional vanishes on a span if and only if it vanishes on each spanning vector; so, by Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]],
>
> $$
> \xi \in N_pS \iff \xi\Big(\frac{\partial}{\partial x^i}\Big|_p\Big) = 0 \ \ (i \le m - k) \iff \xi_i = 0 \ \ (i \le m - k) .
> $$
>
> *(2)* By (1), and since a covector is the sum of its components times the dual basis,
>
> $$
> \xi \in N_pS \iff \xi = \sum_{j = m-k+1}^m \xi_j\, dx^j\big|_p .
> $$
>
> So $N_pS$ is spanned by the $dx^j|_p$ with $j > m - k$, which are linearly independent as part of a basis. (Each of them does lie in $N_pS$, by (1): for $j > m - k$ and $i \le m - k$, the $i$-th component of $dx^j|_p$ is $dx^j|_p(\partial/\partial x^i|_p) = \delta^j_i = 0$.) So they form a basis of $N_pS$, and $\dim N_pS = m - (m - k) = k$, the codimension of $S$.

^pf-37-8

*Uses:* [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§33 Covectors in Coordinates#^cor-33-2|§33.2]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§37 Regular Submanifolds#^def-37-4|Def. §37.4]]

> [!proof]+ Second proof that $\dim N_pS = k$ (without a chart)
> *(Not from lecture; the chart-free count of the official solution of Assignment 5, Problem 4.)* Let $\iota_p^{\ast} : T_p^{\ast}M \to T_p^{\ast}S$ be the pullback of covectors by the inclusion (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]), $\iota_p^{\ast}\xi = \xi \circ \iota_{\ast p}$. By Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]], $\xi \in N_pS$ if and only if $\xi(\iota_{\ast p}v) = 0$ for all $v \in T_pS$, that is, $\iota_p^{\ast}\xi = 0$; so $N_pS = \ker\iota_p^{\ast}$. The map $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), so its dual map $\iota_p^{\ast}$ is surjective (Proposition [[§21 Linear Algebra Toolkit#^prop-21-4|§21.4]](3)). Concretely, a functional on the subspace $\iota_{\ast p}(T_pS)$ extends to $T_pM$: extend a basis of the subspace to a basis of $T_pM$ and send the new vectors to $0$. The dimensions are $\dim T_p^{\ast}M = m$ and $\dim T_p^{\ast}S = \dim T_pS = m - k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], and $\dim S = m - k$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]). Rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) gives
>
> $$
> \dim N_pS = \dim\ker\iota_p^{\ast} = \dim T_p^{\ast}M - \operatorname{rank}\iota_p^{\ast} = m - (m - k) = k .
> $$
>
> This is the linear-algebra fact that the annihilator of a $d$-dimensional subspace of an $m$-dimensional space has dimension $m - d$.

^pf-37-8-2

*Uses:* [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]], [[§37 Regular Submanifolds#^def-37-4|Def. §37.4]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-4|§21.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

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

> [!theorem] Proposition §37.9: Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description
> Let $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$. The following are equivalent:
> 1. near $p$, $X$ is described [[§20 Manifolds in Euclidean Space#^def-20-1|externally]] ([[§20 Manifolds in Euclidean Space#^def-20-1|Definition §20.1]]) — equivalently, [[§20 Manifolds in Euclidean Space#^def-20-2|internally]] or as a graph ([[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]]);
> 2. *(slice)* there is a smooth chart $(U, \varphi = (x_a, x_b))$ of $\mathbb{R}^{n+k}$ with $p \in U$, $x_a$ its first $n$ and $x_b$ its last $k$ components, such that $U \cap X = \{\, q \in U : x_b(q) = \vec 0 \,\}$, that is, a chart [[§37 Regular Submanifolds#^def-37-3|adapted]] to $X$ ([[§37 Regular Submanifolds#^def-37-3|Definition §37.3]]).
>
> In particular $X$ is a [[§37 Regular Submanifolds#^def-37-2|regular submanifold]] of $\mathbb{R}^{n+k}$ of codimension $k$ ([[§37 Regular Submanifolds#^def-37-2|Definition §37.2]]) if and only if every point of $X$ has the descriptions of [[§20 Manifolds in Euclidean Space|§20]].

^prop-37-9

> [!proof]+ Proof
> *(Not from lecture.)* By Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]] the external, internal and graph descriptions near $p$ are equivalent, so for (1)$\iff$(2) it suffices to prove graph $\Rightarrow$ slice and slice $\Rightarrow$ external; together with external $\Rightarrow$ graph (Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]) these close the cycle.
>
> *Graph $\Rightarrow$ slice.* Permuting coordinates is a linear isomorphism, so we may assume $X \cap (V \times V') = \{(x, h(x)) : x \in V\}$ as in (G) of Theorem [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]. (If a permutation $P$ is needed, the construction below gives a chart $\Phi$ adapted to $P(X)$, with domain $U$, and $\Phi \circ P$, on the open set $P^{-1}(U)$, is a chart adapted to $X$. It is a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]: (2), applied to the identity chart of $\mathbb{R}^{n+k}$ with the linear isomorphism $h = P$, and (1), restricting to $P^{-1}(U)$, make $P$ a smooth chart on $P^{-1}(U)$, and (2) again, with the diffeomorphism $h = \Phi$ of $U = P(P^{-1}(U))$ onto an open set, gives $\Phi \circ P$. Its last $k$ components vanish at $q \in P^{-1}(U)$ iff $P(q) \in P(X)$, i.e. iff $q \in X$.) Let $U = V \times V'$, an open set containing $p$, and $\Phi(x, y) = (x,\, y - h(x))$ on $U$. Then:
> - $\Phi$ is smooth, its components $x$ and $y - h(x)$ being smooth;
> - $\Phi$ is injective: $\Phi(x, y) = \Phi(x', y')$ gives $x = x'$ and then $y - h(x) = y' - h(x)$, so $y = y'$;
> - its image $\{(x, z) : x \in V,\ z + h(x) \in V'\}$ is open: it is the preimage of the open set $V \times V'$ under the continuous map $\Psi(x, z) = (x, z + h(x))$ on the open set $V \times \mathbb{R}^k$;
> - its inverse is $\Psi$ restricted to the image, $(x, z) \mapsto (x, z + h(x))$, which is smooth.
>
> *(Computed; not from lecture.)* In matrix form, with $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^k$, the Jacobians of $\Phi$ and of its inverse $\Psi$ are block lower triangular with identity diagonal blocks,
>
> $$
> \Phi'(x, y) = \begin{pmatrix} I_n & 0 \\ -Dh(x) & I_k \end{pmatrix},
> \qquad
> \Psi'(x, z) = \begin{pmatrix} I_n & 0 \\ Dh(x) & I_k \end{pmatrix},
> \qquad
> \Phi'(x, y)\, \Psi'\big(\Phi(x, y)\big) = I_{n+k},
> $$
>
> where $Dh(x)$ is the $k \times n$ Jacobian of $h$; in particular $\det \Phi' = 1$ everywhere.
>
> So $\Phi$ is a diffeomorphism of $U$ onto an open set (Definition [[§17 Differentiable Structures#^def-17-3|§17.3]]), hence a smooth chart of $\mathbb{R}^{n+k}$: it is a homeomorphism onto an open set, and its transition maps with the identity chart are $\Phi$ and $\Phi^{-1}$, so it is compatible with the atlas $\{(\mathbb{R}^{n+k}, \mathrm{id})\}$ and lies in the maximal atlas it generates (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). Its last $k$ components $y - h(x)$ vanish exactly on $X \cap U$: for $(x, y) \in U$, $y - h(x) = 0$ iff $y = h(x)$ iff $(x, y) \in X \cap (V \times V')$. So $\Phi$ is a chart adapted to $X$ at $p$.
>
> *Slice $\Rightarrow$ external.* Let $F = x_b : U \to \mathbb{R}^k$, the last $k$ components of $\varphi$; it is smooth, its components being components of the smooth map $\varphi$. A chart is a diffeomorphism onto its image (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]; it is a diffeomorphism of open subsets of $\mathbb{R}^{n+k}$ by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]), so the Jacobian $\varphi'(q)$ is invertible at every $q \in U$: the ordinary chain rule applied to $\varphi^{-1} \circ \varphi = \mathrm{id}_U$ gives $(\varphi^{-1})'(\varphi(q))\, \varphi'(q) = I$. Its last $k$ rows, which form $F'(q)$, are linearly independent, since the rows of an invertible matrix are; and row $l$ of $\varphi'(q)$ is the gradient of the $l$-th component of $\varphi$ (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]), so these rows are exactly the rows of $F'(q)$. In block form, with $\varphi = (\varphi^1, \ldots, \varphi^{n+k})$,
>
> $$
> \varphi'(q) = \left(\begin{array}{c} \nabla \varphi^1(q) \\ \vdots \\ \nabla \varphi^n(q) \\ \hline \nabla \varphi^{n+1}(q) \\ \vdots \\ \nabla \varphi^{n+k}(q) \end{array}\right) = \begin{pmatrix} x_a'(q) \\ F'(q) \end{pmatrix} \qquad (F = x_b).
> $$
> Hence $F'(q)$ has rank $k$ everywhere, $\vec 0$ is a regular value of $F$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]: every point of $F^{-1}(\vec 0)$, indeed every point of $U$, is a regular point), and
>
> $$
> X \cap U = \{\, q \in U : x_b(q) = \vec 0 \,\} = F^{-1}(\vec 0) ,
> $$
>
> by (2): the external description with $W = U$ (Definition [[§20 Manifolds in Euclidean Space#^def-20-1|§20.1]]).
>
> The final statement follows, since Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] asks for (2) at every point of $X$: $X$ is a regular submanifold of codimension $k$ iff every $p \in X$ has an adapted chart, i.e. satisfies (2), iff every $p \in X$ satisfies (1), by the equivalence just proved.

^pf-37-9

*Uses:* [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§17 Differentiable Structures#^def-17-3|Def. §17.3]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]

![[m591-35-3.svg]]
*Straightening a graph. The map $\Phi(x, y) = (x, y - h(x))$ keeps $x$ and measures the height above the graph; it carries the graph $X$ to the slice $z = 0$, and the parallel graphs $y = h(x) + c$ to the slices $z = c$. This is the passage from the graph charts of [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2]], which flatten $X$ alone, to an adapted chart, which straightens a whole neighbourhood of $X$ in the ambient space.*

For the unit sphere $S^2 \subseteq \mathbb{R}^3$ near the north pole, the graph is $z = \sqrt{1 - x^2 - y^2}$, and $(x, y, z) \mapsto (x, y, z - \sqrt{1 - x^2 - y^2})$ is an adapted chart; so is $(x, y, z) \mapsto (x, y, x^2 + y^2 + z^2 - 1)$ near any point with $z \neq 0$, whose last coordinate is the defining function of the external description.

> [!theorem] Lemma §37.10: An Adapted Chart of a Submanifold of $\mathbb{R}^n$
> Let $M \subseteq \mathbb{R}^n$ be a regular submanifold of dimension $m$, that is, of codimension $n - m$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), and let $(U, \varphi = (x^1, \ldots, x^n))$ be a smooth chart of $\mathbb{R}^n$ adapted to $M$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]), so that
>
> $$
> U \cap M = \{\, q \in U : x^{m+1}(q) = \cdots = x^n(q) = 0 \,\}.
> $$
>
> Put
>
> $$
> G = (G^1, \ldots, G^{n-m}) = (x^{m+1}, \ldots, x^n) : U \to \mathbb{R}^{n-m}, \qquad J(q) = G'(q) \quad (q \in U),
> $$
>
> the $(n-m) \times n$ Jacobian of $G$ in the standard coordinates, whose $s$-th row is the gradient $\nabla G^s(q)$ (Definitions [[§7 The Regular Value Theorem#^def-7-1|§7.1]] and [[§33 Covectors in Coordinates#^def-33-2|§33.2]]):
>
> $$
> J(q) = \begin{pmatrix} \nabla G^1(q) \\ \vdots \\ \nabla G^{n-m}(q) \end{pmatrix} = \begin{pmatrix} \dfrac{\partial G^1}{\partial r^1}(q) & \cdots & \dfrac{\partial G^1}{\partial r^n}(q) \\ \vdots & \ddots & \vdots \\ \dfrac{\partial G^{n-m}}{\partial r^1}(q) & \cdots & \dfrac{\partial G^{n-m}}{\partial r^n}(q) \end{pmatrix} .
> $$
> Tangent spaces are the geometric ones (Definition [[§25 The Geometric Tangent Space#^def-25-1|§25.1]], whose formula makes sense verbatim for any subset of $\mathbb{R}^n$), and $v \cdot w = \sum_l v^l w^l$ is the dot product.
>
> 1. For every $q \in U$, $\varphi'(q)$ is invertible, with inverse $(\varphi^{-1})'(\varphi(q))$, and $J(q)$ has rank $n - m$.
> 2. For every $q \in U \cap M$,
>
> $$
> T^{\mathrm{geo}}_qM = T^{\mathrm{geo}}_q(U \cap M) = \ker J(q), \qquad \dim T^{\mathrm{geo}}_qM = m.
> $$
>
> 3. For $q \in U$ and $j = 1, \ldots, n$ let $X_j(q) = \dfrac{\partial \varphi^{-1}}{\partial r^j}\big(\varphi(q)\big) \in \mathbb{R}^n$, the $j$-th column of $(\varphi^{-1})'(\varphi(q))$, with components $X_j^l(q)$:
>
> $$
> (\varphi^{-1})'\big(\varphi(q)\big) = \big(\, X_1(q) \ \big|\ X_2(q) \ \big|\ \cdots \ \big|\ X_n(q) \,\big) = \begin{pmatrix} X_1^1(q) & \cdots & X_n^1(q) \\ \vdots & \ddots & \vdots \\ X_1^n(q) & \cdots & X_n^n(q) \end{pmatrix} .
> $$
> Each $X_j^l$ is smooth on $U$; $X_1(q), \ldots, X_n(q)$ form a basis of $\mathbb{R}^n$, with $\varphi'(q)\, X_j(q) = e_j$ (in particular $X_1(q), \ldots, X_m(q)$ are linearly independent for every $q \in U$); and for $q \in U \cap M$, $X_1(q), \ldots, X_m(q)$ form a basis of $T^{\mathrm{geo}}_qM$.
> 4. For $q \in U \cap M$, the gradients $\nabla G^1(q), \ldots, \nabla G^{n-m}(q)$ form a basis of the orthogonal complement
>
> $$
> (T^{\mathrm{geo}}_qM)^\perp = \{\, v \in \mathbb{R}^n : v \cdot w = 0 \text{ for all } w \in T^{\mathrm{geo}}_qM \,\} ;
> $$
>
> equivalently, $(T^{\mathrm{geo}}_qM)^\perp = \{\, J(q)^{\mathsf T} c : c \in \mathbb{R}^{n-m} \,\}$, and $c \mapsto J(q)^{\mathsf T} c$ is injective.

^lem-37-10

> [!proof]+ Proof
> *(Not from lecture; filled in. These are the facts about an adapted chart used for the normal bundle of Assignment 5, Problem 5.)* Every point of $M$ lies in such a chart (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]).
>
> *(1)* The chart $\varphi : U \to \varphi(U)$ is a diffeomorphism of open subsets of $\mathbb{R}^n$ (Propositions [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]] and [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]), and the chain rule applied to $\varphi \circ \varphi^{-1} = \mathrm{id}_{\varphi(U)}$ at $\varphi(q)$ gives
>
> $$
> \varphi'(q)\, (\varphi^{-1})'\big(\varphi(q)\big) = I_n ,
> $$
>
> so the square matrix $\varphi'(q)$ is invertible, with inverse $(\varphi^{-1})'(\varphi(q))$. The rows of an invertible matrix are linearly independent, and row $l$ of $\varphi'(q)$ is $\nabla x^l(q)$ (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]); the rows of $J(q)$ are the last $n - m$ of these, $\nabla x^{m+1}(q), \ldots, \nabla x^n(q)$, so they are independent and $J(q)$ has rank $n - m$ (Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]]). This is the computation in the proof of Proposition [[§37 Regular Submanifolds#^prop-37-9|§37.9]] (slice $\Rightarrow$ external, with $m$ and $n - m$ in place of $n$ and $k$).
>
> *(2)* By (1), $\vec 0$ is a regular value of $G$ on the open set $U$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]), and $U \cap M = G^{-1}(\vec 0)$ by the displayed description of $U \cap M$. The first equality is Lemma [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]], since $U \cap M$ is open in $M$ (its proof uses only that $U \cap M$ is open in the subset $M$ of the Euclidean space). The second, and the dimension, are Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]] for the regular level set $U \cap M = G^{-1}(\vec 0)$, with $W = U$, $F = G$, $c = \vec 0$ and $m$, $n - m$ in place of $n$, $k$: the kernel of the surjective $J(q) : \mathbb{R}^n \to \mathbb{R}^{n-m}$ has dimension $n - (n - m) = m$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)).
>
> *(3)* $X_j(q)$ is the velocity of the $j$-th coordinate line $t \mapsto \varphi^{-1}(\varphi(q) + t e_j)$ at $t = 0$, by the chain rule: the coordinate field $\partial/\partial x^j$ regarded as a vector field on $U$ in the sense of multivariable calculus. Each $X_j^l$ is smooth on $U$, as the composite of the smooth $\varphi$ with the partial derivative $\partial(\varphi^{-1})^l/\partial r^j$ of the smooth map $\varphi^{-1}$.
> - *$X_1(q), \ldots, X_n(q)$ form a basis of $\mathbb{R}^n$, and $\varphi'(q)\, X_j(q) = e_j$.* By (1), $(\varphi^{-1})'(\varphi(q))$ is the inverse of $\varphi'(q)$; so it is invertible, its columns $X_1(q), \ldots, X_n(q)$ form a basis, and $\varphi'(q)\, X_j(q)$, the $j$-th column of $\varphi'(q)\,(\varphi^{-1})'(\varphi(q)) = I_n$, is $e_j$. Any $m$ of the $n$ basis vectors, in particular $X_1(q), \ldots, X_m(q)$, are linearly independent, for every $q \in U$.
> - *For $q \in U \cap M$, $X_1(q), \ldots, X_m(q)$ form a basis of $T^{\mathrm{geo}}_qM$.* The rows of $J(q)$ are the last $n - m$ rows of $\varphi'(q)$ (proof of (1)), so $J(q)\, X_j(q)$ consists of the last $n - m$ entries of $\varphi'(q)\, X_j(q) = e_j$. For $j \le m$ these entries are all $0$, so $X_j(q) \in \ker J(q) = T^{\mathrm{geo}}_qM$ by (2). The $m$ vectors $X_1(q), \ldots, X_m(q)$ are linearly independent, as part of the basis just found, and lie in the $m$-dimensional space $T^{\mathrm{geo}}_qM$ (2); $m$ independent vectors in an $m$-dimensional space form a basis. So
>
> $$
> T^{\mathrm{geo}}_qM = \operatorname{Span}\{X_1(q), \ldots, X_m(q)\}.
> $$
>
> *(4)* Fix $q \in U \cap M$. *The gradients are normal:* for $w \in T^{\mathrm{geo}}_qM = \ker J(q)$ (2), the $s$-th entry of $J(q)\, w$ is $\nabla G^s(q) \cdot w$ (the $s$-th row of $J(q)$ is $\nabla G^s(q)$, Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]), and $J(q)\, w = 0$; so $\nabla G^s(q) \cdot w = 0$, and $\nabla G^s(q) \in (T^{\mathrm{geo}}_qM)^\perp$. *They are independent:* $J(q)$ has rank $n - m$ by (1), so its $n - m$ rows are linearly independent (Definition [[§7 The Regular Value Theorem#^def-7-2|§7.2]]). *The orthogonal complement has dimension $n - m$:* choose a basis $w_1, \ldots, w_m$ of $T^{\mathrm{geo}}_qM$ ($\dim = m$ by (2)), and let $B$ be the $m \times n$ matrix with rows $w_1^{\mathsf T}, \ldots, w_m^{\mathsf T}$. A vector $v$ is orthogonal to every element $\sum_i a_i w_i$ of $T^{\mathrm{geo}}_qM$ if and only if it is orthogonal to each $w_i$, because $v \cdot \sum_i a_i w_i = \sum_i a_i\, (v \cdot w_i)$ by linearity of the dot product (“if” by this formula, “only if” by taking $a = e_i$); that is, iff $Bv = 0$. So $(T^{\mathrm{geo}}_qM)^\perp = \ker B$. The rows of $B$ are independent, so $B$ has rank $m$, and rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) gives $\dim \ker B = n - m$. So the $n - m$ independent vectors $\nabla G^s(q)$ lie in the $(n-m)$-dimensional space $(T^{\mathrm{geo}}_qM)^\perp$, and form a basis of it. *Matrix form:* for $c = (c^1, \ldots, c^{n-m}) \in \mathbb{R}^{n-m}$, $J(q)^{\mathsf T} c = \sum_s c^s\, \nabla G^s(q)$, since the columns of $J(q)^{\mathsf T}$ are the rows of $J(q)$,
>
> $$
> J(q)^{\mathsf T} = \begin{pmatrix} \dfrac{\partial G^1}{\partial r^1}(q) & \cdots & \dfrac{\partial G^{n-m}}{\partial r^1}(q) \\ \vdots & & \vdots \\ \dfrac{\partial G^1}{\partial r^n}(q) & \cdots & \dfrac{\partial G^{n-m}}{\partial r^n}(q) \end{pmatrix} \qquad (\text{column } s \text{ holds the entries of } \nabla G^s(q));
> $$
> so the set of all $J(q)^{\mathsf T} c$ is the span of the gradients, which is $(T^{\mathrm{geo}}_qM)^\perp$, and $c \mapsto J(q)^{\mathsf T} c$ is injective because the gradients are independent.

^pf-37-10

*Uses:* [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§7 The Regular Value Theorem#^def-7-2|Def. §7.2]], [[§37 Regular Submanifolds#^prop-37-9|§37.9]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§25 The Geometric Tangent Space#^lem-25-1|§25.1]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!remark] Remark: The Tangent Spaces Match
> *(Not from lecture.)* The two tangent spaces of the geometric and the abstract stage correspond as well. Externally, $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]]). In the slice chart of [[§37 Regular Submanifolds#^prop-37-9|Proposition §37.9]], with $F = x_b$, this kernel is the set of vectors on which the differentials of the last $k$ coordinates vanish, the span of the first $n$ coordinate directions; and that span is $\iota_{\ast p}(T_pX)$ ([[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6]]). [[§37 Regular Submanifolds#^prop-37-14|Proposition §37.14]] below makes the identification precise, together with the agreement of the two smooth structures.

^rem-37-2

## The Regular Value Theorem for Manifolds

*Lecture 12. “And now we go back to submersions” — to “[the] wonderful version of the regular value theorem.”*

The local half of the theorem below holds at a single point where a map is a submersion. It is isolated as a lemma because it is used twice: for level sets here, and for preimages of transverse submanifolds later in this section.

> [!theorem] Lemma §37.11: Level Sets Near a Regular Point
> Let $V \subseteq M$ be open, $\dim M = m$, $G : V \to N$ smooth with $\dim N = n$, $p \in V$ a point at which $G$ is a submersion (Definition [[§36 Submersions#^def-36-1|§36.1]]), and $c = G(p)$.
>
> 1. There are a smooth chart $(W, \theta = (z^1, \ldots, z^m))$ of $M$ at $p$ with $W \subseteq V$ and a smooth chart $(Y, \chi)$ of $N$ at $c$ with $G(W) \subseteq Y$, such that $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^n(p')\big)$ for $p' \in W$; consequently, with $\vec c = \chi(c) = (c_1, \ldots, c_n)$,
>
> $$
> W \cap G^{-1}(c) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^n(p') = c_n \,\} .
> $$
>
> In particular $n \le m$.
> 2. $\hat\theta = \big(z^{n+1}, \ldots, z^m,\ z^1 - c_1, \ldots, z^n - c_n\big)$ is a smooth chart of $M$ with domain $W$, whose last $n$ components vanish exactly on $W \cap G^{-1}(c)$. Hence, if $S \subseteq M$ is a subset with $S \cap W = G^{-1}(c) \cap W$, then $(W, \hat\theta)$ is a chart adapted to $S$ of codimension $n$ (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]).
> 3. Let $S \subseteq M$ be a regular submanifold of codimension $n$ with inclusion $\iota$ and $p \in S$, and suppose $S \cap W' = G^{-1}(c) \cap W'$ for some open $W' \subseteq V$ containing $p$. Then $\iota_{\ast p}(T_pS) = \ker G_{\ast p}$.

^lem-37-11

> [!proof]+ Proof
> *(Lecture 12's argument for the regular value theorem below, and Steps 6–7 and part (2) of the submitted solution of Assignment 5, Problem 2; isolated here, with the details filled in.)* Throughout, the tangent spaces of the open sets $V$ and $W'$ at their points are identified with those of $M$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]).
>
> *(1)* $V$ is an open submanifold of $M$, of dimension $m$. The normal form (Theorem [[§36 Submersions#^thm-36-6|§36.6]]) requires $G$ to be a submersion only at the one point $p$. (That $G$ is then a submersion on a whole neighbourhood of $p$, Corollary [[§36 Submersions#^cor-36-7|§36.7]], is a consequence of the normal form, not a hypothesis of it; no shrinking of $V$ is needed.) Applied to $G : V \to N$ at $p$, it gives smooth charts $(W, \theta = (z^1, \ldots, z^m))$ of $V$ at $p$ and $(Y, \chi)$ of $N$ at $G(p) = c$, with $G(W) \subseteq Y$, $n \le m$, and
>
> $$
> \chi \circ G \circ \theta^{-1}\big(r^1, \ldots, r^m\big) = \big(r^1, \ldots, r^n\big) \quad \text{on } \theta(W) ;
> $$
>
> applying this identity at $\theta(p')$, and using $z^i = r^i \circ \theta$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|§29.1]]), gives $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^n(p')\big)$ for $p' \in W$. Since $W \subseteq V$ is open in $V$, hence in $M$, $(W, \theta)$ is also a smooth chart of $M$ (Proposition [[§17 Differentiable Structures#^prop-17-7|§17.7]](2)). For $p' \in W$,
>
> $$
> p' \in G^{-1}(c) \iff G(p') = c \iff \chi\big(G(p')\big) = \chi(c) \iff \big(z^1(p'), \ldots, z^n(p')\big) = (c_1, \ldots, c_n) .
> $$
>
> The first equivalence is the definition of the preimage; the second holds because $G(p')$ and $c = G(p)$ both lie in $Y$ (as $G(W) \subseteq Y$ and $p, p' \in W$), on which $\chi$ is injective; the third is the identity just derived from the normal form.
>
> *(2)* By (1), $W \cap G^{-1}(c)$ is cut out in the smooth chart $(W, \theta)$ of $M$ by setting $n$ of its coordinates, $z^1, \ldots, z^n$, equal to the constants $c_1, \ldots, c_n$; and so is $W \cap S$ for any subset $S$ with $S \cap W = G^{-1}(c) \cap W$. Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]], with $k = n$, the coordinates $z^1, \ldots, z^n$ and the constant vector $\vec c$, therefore gives the chart $(W, A \circ \theta)$ of $M$ adapted to $S$, where, in the notation of its proof, $A(r) = \big(r^{n+1}, \ldots, r^m,\ r^1 - c_1, \ldots, r^n - c_n\big)$; explicitly $A \circ \theta = \hat\theta$. Its last $n$ components $z^1 - c_1, \ldots, z^n - c_n$ vanish at $p' \in W$ if and only if $z^i(p') = c_i$ for $i = 1, \ldots, n$, that is, by (1), if and only if $p' \in G^{-1}(c)$; this is the case $S = G^{-1}(c)$.
>
> *(3): $\iota_{\ast p}(T_pS) \subseteq \ker G_{\ast p}$.* The set $S \cap W'$ is open in $S$ (subspace topology) and contains $p$, so its tangent space at $p$ is $T_pS$ (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]). On it the composite $G \circ \iota$ is defined — $\iota$ maps it into $W' \subseteq V$, and its restriction is smooth into the open set $V$ by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) and Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3) — and constant with value $c$, since $S \cap W' \subseteq G^{-1}(c)$. The pushforward along a constant map is zero (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]), so by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]])
>
> $$
> G_{\ast p} \circ \iota_{\ast p} = (G \circ \iota)_{\ast p} = 0 ,
> $$
>
> that is, $G_{\ast p}(\iota_{\ast p}v) = 0$ for every $v \in T_pS$.
>
> *(3): dimensions.* $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), so, by Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]] and Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]],
>
> $$
> \dim \iota_{\ast p}\big(T_pS\big) = \dim T_pS = \dim S = m - n .
> $$
>
> On the other side, $G_{\ast p}$ is onto the $n$-dimensional space $T_cN$, so by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1))
>
> $$
> \dim \ker G_{\ast p} = \dim T_pM - \operatorname{rank} G_{\ast p} = m - n .
> $$
>
> A subspace of the same finite dimension is the whole space, so $\iota_{\ast p}(T_pS) = \ker G_{\ast p}$.

^pf-37-11

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§36 Submersions#^thm-36-6|§36.6]], [[§36 Submersions#^cor-36-7|§36.7]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-1|Def. §29.1]], [[§17 Differentiable Structures#^prop-17-7|§17.7]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

> [!theorem] Theorem §37.12: The Regular Value Theorem for Manifolds
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$, and let $q \in N$ be a regular value of $F$ (Definition [[§36 Submersions#^def-36-4|§36.4]]). Then $S = F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$ (possibly empty), so $\dim S = m - n$, and for every $p \in S$
>
> $$
> \iota_{*p}(T_pS) = \ker F_{*p} .
> $$
>
> *Lee: Corollary 5.14 and Proposition 5.38*

^thm-37-12

> [!proof]+ Proof
> *$S$ is a submanifold (Lecture 12).* We check the definition at each $p \in S$: we need an adapted chart at $p$. (If $S = \emptyset$ there is nothing to check.) By assumption $F$ is a submersion at $p$, so the normal form (Theorem [[§36 Submersions#^thm-36-6|§36.6]]) gives charts $(U, \hat\varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q = F(p)$, with $F(U) \subseteq V$ and $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$. What are the equations of $S \cap U$ in these coordinates? For $q' \in U$,
>
> $$
> \begin{aligned}q' \in S &\iff F(q') = q \iff \psi\big(F(q')\big) = \psi(q) \\
> &\iff \tilde F\big(\hat\varphi(q')\big) = \psi(q) \iff \big(x^1(q'), \ldots, x^n(q')\big) = \big(y^1(q), \ldots, y^n(q)\big).\end{aligned}
> $$
>
> “These are not of the type $x_b = 0$, but of the type $x_a$ equals a constant”: the first $n$ coordinates equal a constant vector. By the observations after the definition (Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]) — any constant, and any $n$ of the coordinates — $S$ has an adapted chart at $p$, of codimension $n$. *(Completion.)* This is Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]], applied with $V = M$, $G = F$ and $c = q$, so that $G^{-1}(c) = S$; its proof gives the details. Part (1) of the lemma is the computation above, with the normal-form charts $(U, \hat\varphi)$ and $(V, \psi)$ and the constant vector $\vec c = \psi(q) = (y^1(q), \ldots, y^n(q))$: the first equivalence is $S = F^{-1}(q)$; the second holds because $F(q')$ and $q$ both lie in $V$, on which $\psi$ is injective; the third because $\psi \circ F = \tilde F \circ \hat\varphi$ on $U$; the last because $\tilde F(\hat\varphi(q'))$ consists of the first $n$ entries of $\hat\varphi(q')$. Part (2), with $S \cap U = F^{-1}(q) \cap U$, is Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] with $k = n$, the coordinates $x^1, \ldots, x^n$ and $\vec c = \psi(q)$: it gives the adapted chart $\big(x^{n+1}, \ldots, x^m,\ x^1 - y^1(q), \ldots, x^n - y^n(q)\big)$ at $p$, of codimension $n$, and $n \le m$ by the normal form. As $p \in S$ was arbitrary, $S$ is a regular submanifold of codimension $n$, and $\dim S = m - n$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]].
>
> *The tangent space.* *(Completion. In lecture: “I won't bother checking the kernel thing, because everything really reduces to the Euclidean [case].”)* By Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](3), applied with $V = W' = M$, $G = F$, $c = q$ and the regular submanifold $S$ of codimension $n$ itself (so that $S \cap M = F^{-1}(q) \cap M$), $\iota_{\ast p}(T_pS) = \ker F_{\ast p}$. In that lemma's proof: the composite $F \circ \iota : S \to N$ is constant, with value $q$, so $F_{\ast p} \circ \iota_{\ast p} = (F \circ \iota)_{\ast p} = 0$ by the Chain Rule and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], and $\iota_{\ast p}(T_pS) \subseteq \ker F_{\ast p}$; the left side has dimension $m - n$, since $\iota_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), and the right side has dimension $m - n$ by rank–nullity, since $F_{\ast p}$ is onto (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)); and a subspace of the same finite dimension is everything. This is the argument of Lecture 8 for $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]), one level up.

^pf-37-12

*Uses:* [[§36 Submersions#^thm-36-6|§36.6]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^lem-37-11|§37.11]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]

![[m591-15-5.svg]]
*The proof in one square, as on the board. In the normal-form charts $\tilde F$ is the projection onto the first $n$ coordinates, so the level set $S \cap U = F^{-1}(q) \cap U$ is carried by $\hat\varphi$ onto a fibre of a projection: the slice where the first $n$ coordinates equal $\psi(q)$.*

> [!remark]- Connections
> - The earlier regular value theorems it contains: [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§30 The Differential in Coordinates#^cor-30-9|§30.9]] (see the remark below); the tangent-space statement generalizes [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]].
> - Constraint sets $\{g_1 = c_1, \ldots, g_k = c_k\}$ in multivariable analysis: [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 §17.3]] (Lagrange multipliers with several constraints).
> - Fibres of submersions that are all copies of one fibre: [[§38 Fibrations#^def-38-1|fibrations, Def. §38.1]].

**Transcription note.** Page 33 of the handwritten notes states the theorem for “$q \in M$ a regular value”; the regular value lies in the target, $q \in N$.

> [!theorem] Corollary §37.13: Fibres of Submersions Are Regular Submanifolds
> If $F : M \to N$ is a submersion, then every fibre $F^{-1}(q)$, $q \in N$, is a regular submanifold of $M$ of codimension $n$ — “they could be empty, some of them.”

^cor-37-13

> [!proof]+ Proof
> Every $q \in N$ is a regular value: every point of $F^{-1}(q)$ is a regular point, and if $F^{-1}(q)$ is empty the condition holds vacuously. Indeed, $F$ is a submersion at every point of $M$ (Definition [[§36 Submersions#^def-36-1|§36.1]]), in particular at every $p \in F^{-1}(q)$, which is what Definition [[§36 Submersions#^def-36-4|§36.4]](2) asks of a regular value; and if $q \notin F(M)$, it is a regular value by Definition [[§36 Submersions#^def-36-4|§36.4]](3). Apply Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]: $F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$.

^pf-37-13

*Uses:* [[§36 Submersions#^def-36-3|Def. §36.3]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§36 Submersions#^def-36-1|Def. §36.1]]

> [!remark] Remark: The Regular Value Theorems — Old and New
> The notes now contain the regular value theorem in five forms. They are one idea met at increasing generality, not competing statements.
>
> | **Where** | **Setting** | **Conclusion** | **Role now** |
> |---|---|---|---|
> | Thm. [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]], Cor. [[§7 The Regular Value Theorem#^cor-7-4\|§7.4]] | $F : W \to \mathbb{R}^k$, $W \subseteq \mathbb{R}^{n+k}$ open | topological manifold | the first version (Lecture 3); Chapter 2 needs it |
> | Prop. [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] | the same | smooth manifold, by graph charts | the Euclidean case (Lecture 6) |
> | Prop. [[§30 The Differential in Coordinates#^prop-30-8\|§30.8]] | $F : M \to N$, level set inside one chart | regular for $F$ iff for $\tilde F$ | a computational tool |
> | Cor. [[§30 The Differential in Coordinates#^cor-30-9\|§30.9]] | $F : M \to N$ | topological manifold | subsumed; a more elementary proof |
> | Thm. [[§37 Regular Submanifolds#^thm-37-12\|§37.12]] | $F : M \to N$ | submanifold, with $\iota_{*p}(T_pS) = \ker F_{*p}$ | the general theorem (Lecture 12) |
>
> The general theorem contains the others: taking $M$ an open subset of Euclidean space recovers the first two. Its proof goes through the normal form, which rests on the inverse function theorem and not on [[§7 The Regular Value Theorem|§7]], so nothing is circular. The next proposition shows that the old and new versions give the same smooth structure and the same tangent spaces.

^rem-37-3

> [!theorem] Proposition §37.14: The Old and New Versions Agree
> Let $W \subseteq \mathbb{R}^{n+k}$ be open, $F : W \to \mathbb{R}^k$ smooth, $c$ a regular value, and $S = F^{-1}(c)$.
> 1. The smooth structure on $S$ given by the graph charts (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) is the induced structure of $S$ as a regular submanifold of $W$ (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]).
> 2. In the setting of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], under the identification $T_pW = \mathbb{R}^{n+k}$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the subspace $\iota_{*p}(T_pS)$ is $T^{\mathrm{geo}}_pS = \ker F'(p)$.

^prop-37-14

> [!proof]+ Proof
> *(Not from lecture; filled in.)* First, $c$ is a regular value in both senses, since the matrix of $F_{\ast p}$ in the standard coordinates is $F'(p)$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]). In detail: with the identity charts on $W$ and on $\mathbb{R}^k$, the coordinate representation of $F$ is $F$ itself, so Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] says the matrix of $F_{\ast p}$ in the coordinate bases is $F'(p)$. A linear map is onto $T_{F(p)}\mathbb{R}^k$ iff its rank is $k$, and its rank is that of its matrix (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)); so $F_{\ast p}$ is onto (Definition [[§36 Submersions#^def-36-4|§36.4]]) iff $F'(p)$ has rank $k$ (Definition [[§7 The Regular Value Theorem#^def-7-4|§7.4]]). Hence Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] applies to $F : W \to \mathbb{R}^k$, and $S$ is a regular submanifold of $W$ of codimension $k$.
>
> (1) Let $p \in S$. As in the construction of the graph charts, after reordering the coordinates write the points of $\mathbb{R}^{n+k}$ as $(x, y) \in \mathbb{R}^n \times \mathbb{R}^k$ with $\partial F/\partial y\,(p)$ invertible, so that the graph chart near $p$ is $(x, y) \mapsto x$ on $S$. (Here $x = x_I$, $y = x_J$ in the notation of the construction before Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], and the graph chart is $\varphi_J = \pi_I|_{U_J}$. The reordering is a permutation $P$ of coordinates; the chart produced below is then $\Phi \circ P$, with the same last $k$ components, a smooth chart by Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]]: (2), applied to the identity chart with the linear isomorphism $h = P$, and (1), restricting to an open set, make $P$ a smooth chart on $P^{-1}(U)$, and (2) again, with the diffeomorphism $h = \Phi|_U$, gives $\Phi \circ P$. We suppress $P$.) Let $\Phi(x, y) = (x, F(x, y) - c)$. Its Jacobian at $p$ is $\begin{pmatrix} I_n & 0 \\ \partial F/\partial x & \partial F/\partial y \end{pmatrix}$, which is invertible: it is block lower triangular, so its determinant is $\det I_n \cdot \det\big(\partial F/\partial y\,(p)\big) \ne 0$. Written out, with $x = (x^1, \ldots, x^n)$, $y = (y^1, \ldots, y^k)$, $F = (F^1, \ldots, F^k)$ and all partials at $p$,
>
> $$
> \Phi'(p) = \left(\begin{array}{ccc|ccc} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ \hline \dfrac{\partial F^1}{\partial x^1} & \cdots & \dfrac{\partial F^1}{\partial x^n} & \dfrac{\partial F^1}{\partial y^1} & \cdots & \dfrac{\partial F^1}{\partial y^k} \\ \vdots & & \vdots & \vdots & & \vdots \\ \dfrac{\partial F^k}{\partial x^1} & \cdots & \dfrac{\partial F^k}{\partial x^n} & \dfrac{\partial F^k}{\partial y^1} & \cdots & \dfrac{\partial F^k}{\partial y^k} \end{array}\right) = \begin{pmatrix} I_n & 0 \\ \dfrac{\partial F}{\partial x} & \dfrac{\partial F}{\partial y} \end{pmatrix} .
> $$
> So by the inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], with $\Phi$ on $W$ and $a = p$) $\Phi$ restricts to a diffeomorphism of an open $U \ni p$ onto an open set, and by Lemma [[§36 Submersions#^lem-36-5|§36.5]] (with $M = W$, the diffeomorphism being one of manifolds by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]]) it is a smooth chart of $W$. Its last $k$ components are $F - c$, which vanish exactly on $S \cap U$, so $\Phi$ is adapted, and its induced chart is $\Phi_S = x|_{S \cap U}$: the graph chart. More precisely, $\Phi_S$ and the graph chart $\varphi_J$ are both restrictions of the projection $(x, y) \mapsto x$, so they agree on $S \cap U \cap U_J$, an open neighbourhood of $p$ in $S$. The same construction works at every point $p'$ of the graph chart's domain $U_J$, with the same splitting $(x, y)$: there $S$ is the graph $y = h_J(x)$, and differentiating $F(x, h_J(x)) = c$ gives $\partial F/\partial x = -\,\partial F/\partial y \cdot h_J'$, so $F'(p') = \partial F/\partial y\,(p') \cdot \big({-h_J'} \mid I_k\big)$; as $F'(p')$ has rank $k$, the $k \times k$ matrix $\partial F/\partial y\,(p')$ has rank $k$, i.e. is invertible. So near each of its points, every graph chart is an induced chart. Induced charts are pairwise compatible, and smoothness of a transition map is local, so every graph chart is compatible with every induced chart, and the two atlases determine the same maximal atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]). In detail: let $(U_J, \varphi_J)$ be a graph chart and $(V \cap S, \psi_S)$ an induced chart. Near each point $\varphi_J(p')$ of the domain of $\psi_S \circ \varphi_J^{-1}$, by what was just shown, $\varphi_J$ agrees with an induced chart $\Phi_S$ on an open neighbourhood $O$ of $p'$ in $S$; on $\varphi_J(O \cap V)$ the map $\psi_S \circ \varphi_J^{-1}$ equals $\psi_S \circ \Phi_S^{-1}$, a transition map between induced charts, smooth by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]](2). The same holds for $\varphi_J \circ \psi_S^{-1}$ near each point. So the two charts are compatible, the union of the two atlases is an atlas, and both generate the maximal atlas containing it.
>
> (2) Let $v \in T^{\mathrm{geo}}_pS$, and let $\gamma$ be the lifted line of Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], a curve in $S$ with $\gamma(0) = p$ and $\gamma'(0) = v$, so that $D_v = D_\gamma$. (It is smooth into $\mathbb{R}^{n+k}$ with values in $S$, hence smooth into $S$ by Lemma [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]](2); by (1) the structure there is the induced one, so $T_pS$ and $\iota_{\ast p}$ are unambiguous. And $D_v = D_\gamma$ because both send $f$ to $\frac{d}{dt}|_{t=0} f(\gamma(t))$, by Definitions [[§25 The Geometric Tangent Space#^def-25-4|§25.4]] and [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]].) By Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], $\iota_{\ast p}D_v = D_{\iota \circ \gamma}$, the derivation $g \mapsto (g \circ \gamma)'(0) = \nabla g(p) \cdot v$ at $p$ — the directional derivative in the direction $v$, which is $v$ under Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]. In detail, for a germ $[g]$ at $p$ on $W$, by Definition [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|§31.2]] and the chain rule (Definition [[§7 The Regular Value Theorem#^def-7-1|§7.1]]),
>
> $$
> (\iota_{\ast p}D_v)[g] = D_{\iota \circ \gamma}[g] = \frac{d}{dt}\Big|_{t=0} g\big(\gamma(t)\big) = \nabla g(p) \cdot \gamma'(0) = \nabla g(p) \cdot v = \frac{d}{dt}\Big|_{t=0} g(p + tv) = D_v|_p[g] ,
> $$
>
> where $D_v|_p \in T_pW$ is the derivation of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the vector $v$ under the identification $T_pW = \mathbb{R}^{n+k}$; the fifth equality is the chain rule for the line $t \mapsto p + tv$. Since $v \mapsto D_v$ is onto $T_pS$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]]), $\iota_{\ast p}(T_pS) = T^{\mathrm{geo}}_pS$: every element of $T_pS$ is $D_v$ for some $v \in T^{\mathrm{geo}}_pS$, and its image is the vector $v$. And $T^{\mathrm{geo}}_pS = \ker F'(p)$ by Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]. This matches $\ker F_{\ast p}$ in Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], $F_{\ast p}$ being $F'(p)$: by Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], $F_{\ast p}$ corresponds to $F'(p)$ under the identification $\partial/\partial r^i|_p \mapsto e_i$, which is the identification of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], since $D_{e_i}|_p[g] = \frac{d}{dt}|_{t=0}\, g(p + te_i) = \partial g/\partial r^i(p)$; so $\ker F_{\ast p}$ corresponds to $\ker F'(p)$.

^pf-37-14

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§7 The Regular Value Theorem#^def-7-4|Def. §7.4]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§36 Submersions#^lem-36-5|§36.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-4|§19.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§20 Manifolds in Euclidean Space#^lem-20-3|§20.3]], [[§31 Tangent Vectors as Velocities of Curves#^def-31-2|Def. §31.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§7 The Regular Value Theorem#^def-7-1|Def. §7.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-7|§29.7]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]

*Assignment 5, Problem 2.* [[§26 Transversality|§26]] treated transversality in Euclidean space: a smooth map $F : \mathbb{R}^N \to \mathbb{R}^k$ transverse to a regular level set $S = G^{-1}(0)$ (Definition [[§26 Transversality#^def-26-2|§26.2]]) pulls $S$ back to a manifold of the same codimension, with $T^{\mathrm{geo}}_pF^{-1}(S) = F'(p)^{-1}(T^{\mathrm{geo}}_{F(p)}S)$ (Theorem [[§26 Transversality#^thm-26-1|§26.1]]). That proof needed a global defining map $G$. With regular submanifolds and their adapted charts, the same statement holds for any smooth map between manifolds and any regular submanifold of the target — an adapted chart supplies a defining map $x_b$ near each point, which is the localization announced in the remark *An Intrinsic Statement with a Chosen Proof* in [[§26 Transversality|§26]].

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

> [!theorem] Theorem §37.15: Preimages of Transverse Submanifolds
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

^thm-37-15

> [!proof]+ Proof
> *(Assignment 5, Problem 2; the student's route, with two steps completed — the normal form is applied at a single point, and the kernel of $(x_b)_{\ast q}$ is computed directly, without the regular value theorem.)* *(The two completions are now separate statements, Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]] and Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]], which Steps 2, 6 and 7 and part (2) below cite; the details are written out in their proofs.)* For (1) we must produce, at every $p \in F^{-1}(S)$, a smooth chart of $M$ adapted to $F^{-1}(S)$ with $k$ equations (Definition [[§37 Regular Submanifolds#^def-37-3|§37.3]]). If $F^{-1}(S) = \emptyset$ there is nothing to check, since the condition of Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] is one condition at each point of the subset (the convention of Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], whose fibres may be empty); and (2) is then vacuous. So fix $p \in F^{-1}(S)$ and put $q = F(p)$, a point of $S$. The plan: an adapted chart of $S$ at $q$ supplies a local defining map $x_b$ for $S$; transversality makes $G = x_b \circ F$ a submersion at $p$; the normal form of $G$ then straightens $F^{-1}(S)$ near $p$. Throughout, the tangent space of an open subset at a point is identified with that of the ambient manifold (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]), as everywhere in the notes; by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), applied to a restriction $F|_V = F \circ \iota_V$ with $\iota_V$ the inclusion of the open set $V$, this identification turns the differential of a restriction of $F$ into $F_{\ast p}$.
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
> *Step 2: the map $x_b$ and its differential.* Regard $x_b : U \to \mathbb{R}^k$ as a map from the open submanifold $U$ to $\mathbb{R}^k$, the latter with the identity chart, whose coordinate functions are $r^1, \ldots, r^k$. Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]], applied to the regular submanifold $S \subseteq N$ of codimension $k$ and the adapted chart $(U, \varphi)$ of Step 1 (so with $n$ in place of $m$), gives: $x_b$ is smooth, and at $q$ (where $x_b(q) = \vec 0$, as $q \in U \cap S$) $(x_b)_{\ast q}(\partial/\partial x^i|_q)$ is $0$ for $i \le n - k$ and $\partial/\partial r^{\,i-(n-k)}|_{\vec 0}$ for $i > n - k$. Two consequences.
>
> 1. [(a)] *$(x_b)_{\ast q}$ is onto $T_{\vec 0}\mathbb{R}^k$*: by part (2) of the proposition, $x_b$ is a submersion at every point of $U$, in particular at $q$.
> 2. [(b)] *$\ker (x_b)_{\ast q} = \iota_{\ast q}(T_qS)$*: part (4) of the proposition, at the point $q \in U \cap S$.
>
> *Step 3: a chart at $p$ mapped into $U$, and the map $G$.* $F$ is continuous, so $F^{-1}(U)$ is an open set containing $p$. Take any smooth chart $(\tilde V, \tilde\psi)$ of $M$ at $p$ and put $V = \tilde V \cap F^{-1}(U)$, an open set containing $p$ with $F(V) \subseteq U$; the restriction of $\tilde\psi$ to $V$ is again a smooth chart (Lemma [[§17 Differentiable Structures#^lem-17-6|§17.6]](1), with $U' = V$). Define
>
> $$
> G = x_b \circ F|_V : V \longrightarrow \mathbb{R}^k .
> $$
>
> It is smooth: $F|_V$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](2)), and smooth as a map into the open submanifold $U$, since it takes values in $U$ and its composite with the inclusion $U \hookrightarrow N$ is the smooth map $F|_V$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3)); then $G$ is a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and the identifications $T_pV = T_pM$, $T_qU = T_qN$,
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
> So $G_{\ast p}$ is onto, i.e. $G$ is a submersion at $p$ (Definition [[§36 Submersions#^def-36-1|§36.1]]). In particular $k \le m$: a surjective linear map $T_pM \to T_{\vec 0}\mathbb{R}^k$ has $\dim T_pM \ge \dim T_{\vec 0}\mathbb{R}^k$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), and these dimensions are $m$ and $k$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]).
>
> *Step 6: the normal form of $G$ at $p$.* Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]] requires $G$ to be a submersion only at the one point $p$, which is Step 5; no shrinking of $V$ is needed. Its part (1), applied to $G : V \to \mathbb{R}^k$ at $p$ with $c = G(p) = \vec 0$ (and $k$ in place of $n$), gives — by the normal form of $G$ — a smooth chart $(W, \theta = (z^1, \ldots, z^m))$ of $M$ at $p$ with $W \subseteq V$ and a smooth chart $(Y, \chi)$ of $\mathbb{R}^k$ at $\vec 0$ with $G(W) \subseteq Y$ and $\chi\big(G(p')\big) = \big(z^1(p'), \ldots, z^k(p')\big)$ for $p' \in W$; and, with $\vec c = \chi(\vec 0) = (c_1, \ldots, c_k)$,
>
> $$
> W \cap G^{-1}(\vec 0) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^k(p') = c_k \,\} .
> $$
>
> *Step 7: an adapted chart at $p$.* Since $W \subseteq V$, Step 4 gives $W \cap F^{-1}(S) = W \cap V \cap F^{-1}(S) = W \cap G^{-1}(\vec 0)$, so
>
> $$
> W \cap F^{-1}(S) = \{\, p' \in W : z^1(p') = c_1, \ \ldots, \ z^k(p') = c_k \,\} ,
> $$
>
> the intersection cut out in the smooth chart $(W, \theta)$ of $M$ by setting $k$ of its coordinates equal to constants. By Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](2), with the subset $F^{-1}(S)$ — that is, Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]] with the coordinates $z^1, \ldots, z^k$ and the constant vector $\vec c$ — there is a chart of $M$ with domain $W$ adapted to $F^{-1}(S)$, of codimension $k$: explicitly, $\big(z^{k+1}, \ldots, z^m, \ z^1 - c_1, \ldots, z^k - c_k\big)$, the translation and permutation of the student's solution. Here $k \le m$ by Step 5.
>
> *Conclusion of (1).* As $p \in F^{-1}(S)$ was arbitrary, every point of $F^{-1}(S)$ lies in a chart of $M$ adapted to $F^{-1}(S)$ with $k$ equations, so $F^{-1}(S)$ is a regular submanifold of $M$ of codimension $k$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), and $\dim F^{-1}(S) = m - k$ by Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]. The codimension of $S$ in $N$ is also $k$, by hypothesis.
>
> *(2): $j_{\ast p}(T_pF^{-1}(S)) \subseteq \ker G_{\ast p}$.* Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](3) applies to $G : V \to \mathbb{R}^k$, a submersion at $p$ (Step 5) with $c = G(p) = \vec 0$, to the regular submanifold $F^{-1}(S)$ of $M$ of codimension $k$ (part (1)) with inclusion $j$, and to $W' = V$: by Step 4, $F^{-1}(S) \cap V = G^{-1}(\vec 0) = G^{-1}(\vec 0) \cap V$. The inclusion is the first half of its proof: on the open neighbourhood $V \cap F^{-1}(S)$ of $p$ in $F^{-1}(S)$ the composite $G \circ j$ is constant with value $\vec 0$, by Step 4, so $G_{\ast p} \circ j_{\ast p} = (G \circ j)_{\ast p} = 0$ by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) and Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]; that is, $G_{\ast p}(j_{\ast p}v) = 0$ for every $v \in T_pF^{-1}(S)$.
>
> *(2): dimensions.* The second half of the lemma's proof: $\dim j_{\ast p}(T_pF^{-1}(S)) = \dim F^{-1}(S) = m - k$, since $j_{\ast p}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]) and by (1); and $\dim \ker G_{\ast p} = m - k$ by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)), $G_{\ast p}$ being onto the $k$-dimensional $T_{\vec 0}\mathbb{R}^k$ (Step 5). A subspace of the same finite dimension is the whole space, so $j_{\ast p}(T_pF^{-1}(S)) = \ker G_{\ast p}$.
>
> *(2): the kernel of $G_{\ast p}$.* By Step 3, the definition of the kernel, and Step 2(b),
>
> $$
> \begin{aligned}\ker G_{\ast p} &= \big\{\, v \in T_pM : (x_b)_{\ast q}\big(F_{\ast p}v\big) = 0 \,\big\} \\
> &= \big\{\, v \in T_pM : F_{\ast p}v \in \ker (x_b)_{\ast q} \,\big\} = \big\{\, v \in T_pM : F_{\ast p}v \in \iota_{\ast q}(T_qS) \,\big\} ,\end{aligned}
> $$
>
> which is $(F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big)$. With the previous paragraph, $j_{\ast p}(T_pF^{-1}(S)) = (F_{\ast p})^{-1}\big(\iota_{\ast q}(T_qS)\big)$. This is Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](3) — the argument of the tangent-space half of Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]] — run for $G$, followed by the computation of $\ker G_{\ast p}$ that ends the proof of Theorem [[§26 Transversality#^thm-26-1|§26.1]].

^pf-37-15

*Uses:* [[§37 Regular Submanifolds#^prop-37-7|§37.7]], [[§37 Regular Submanifolds#^lem-37-11|§37.11]], [[§37 Regular Submanifolds#^def-37-3|Def. §37.3]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§17 Differentiable Structures#^lem-17-6|§17.6]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§26 Transversality#^thm-26-1|§26.1]]

> [!proof]+ Second proof (reduction to Theorem [[§26 Transversality#^thm-26-1|§26.1]] in charts)
> *(Not from lecture; the route of the official solution of Assignment 5, Problem 2, and the one its hint intends. The three facts that transport the Euclidean theorem are checked explicitly.)* Fix $p \in F^{-1}(S)$ and $q = F(p)$. As in Steps 1 and 3 of the first proof, take a chart $(U, \varphi = (x^1, \ldots, x^n))$ of $N$ adapted to $S$ at $q$, so $U \cap S = x_b^{-1}(\vec 0)$, and a chart $(V, \psi)$ of $M$ at $p$ with $F(V) \subseteq U$. Downstairs, set
>
> $$
> \tilde F = \varphi \circ F \circ \psi^{-1} : \psi(V) \to \mathbb{R}^n, \qquad \tilde G : \mathbb{R}^n \to \mathbb{R}^k, \quad \tilde G(y) = (y^{n-k+1}, \ldots, y^n) .
> $$
>
> $\tilde G$ is linear with $\tilde G' = (0 \mid I_k)$ surjective everywhere, so $\tilde S = \tilde G^{-1}(\vec 0) = \mathbb{R}^{n-k} \times \{\vec 0\}$ is a regular level set with $T^{\mathrm{geo}}_y\tilde S = \ker\tilde G' = \mathbb{R}^{n-k} \times \{\vec 0\}$, and $\varphi(U \cap S) = \tilde S \cap \varphi(U)$. As $\tilde F$ takes values in $\varphi(U)$,
>
> $$
> \tilde F^{-1}(\tilde S) = \psi\big(V \cap F^{-1}(S)\big) .
> $$
>
> *Fact 1: transversality survives the charts.* Let $p' \in V \cap F^{-1}(S)$, $q' = F(p')$, $x' = \psi(p')$. By the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $\tilde F_{\ast x'} = \varphi_{\ast q'} \circ F_{\ast p'} \circ (\psi^{-1})_{\ast x'}$, and $(\psi^{-1})_{\ast x'}$ is onto (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), so $\operatorname{im}\tilde F_{\ast x'} = \varphi_{\ast q'}(\operatorname{im}F_{\ast p'})$. The chart is adapted at $q'$ too, so $\iota_{\ast q'}(T_{q'}S)$ is spanned by the $\partial/\partial x^i|_{q'}$ with $i \le n - k$ (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]), which $\varphi_{\ast q'}$ sends to the $\partial/\partial r^i|_{\varphi(q')}$, that is, to $e_1, \ldots, e_{n-k}$ under the identification of Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]. Applying the isomorphism $\varphi_{\ast q'}$ to $\operatorname{im}F_{\ast p'} + \iota_{\ast q'}(T_{q'}S) = T_{q'}N$ gives
>
> $$
> \operatorname{im}\tilde F'(x') + T^{\mathrm{geo}}_{\tilde F(x')}\tilde S = \mathbb{R}^n .
> $$
>
> *Fact 2: Theorem [[§26 Transversality#^thm-26-1|§26.1]] on an open set.* Its proof is pointwise until the regular value theorem is invoked: the surjectivity step (or the remark *The Surjectivity Step as an Image Computation*) uses only Fact 1 at each point. So $0$ is a regular value of $\tilde H = \tilde G \circ \tilde F : \psi(V) \to \mathbb{R}^k$, and $\tilde H^{-1}(\vec 0) = \tilde F^{-1}(\tilde S) = \psi(V \cap F^{-1}(S))$. Note $\tilde H = x_b \circ F \circ \psi^{-1}$.
>
> *Fact 3: slice charts pull back.* By the Regular Value Theorem for manifolds (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]), applied to $\tilde H$ on the open submanifold $\psi(V)$ of $\mathbb{R}^m$, there is a chart $(W', \theta)$ of $\psi(V)$ at $x' = \psi(p)$ adapted to $\tilde H^{-1}(\vec 0)$, with $k$ equations. Then $\theta \circ \psi : \psi^{-1}(W') \to \theta(W')$ is a diffeomorphism onto an open set, so a smooth chart of $M$ (Lemma [[§36 Submersions#^lem-36-5|§36.5]]), and for $p'' \in \psi^{-1}(W') \subseteq V$, the last $k$ coordinates of $\theta(\psi(p''))$ vanish if and only if $\psi(p'') \in \tilde H^{-1}(\vec 0)$, if and only if $p'' \in F^{-1}(S)$. So $(\psi^{-1}(W'), \theta \circ \psi)$ is a chart of $M$ adapted to $F^{-1}(S)$ at $p$, with $k$ equations.
>
> As $p$ was arbitrary, $F^{-1}(S)$ is a regular submanifold of codimension $k$, which is (1). For (2), $G = x_b \circ F|_V = \tilde H \circ \psi$ is the map of the first proof; it is a submersion at $p$, since $\tilde H$ is one at $\psi(p)$ and $\psi_{\ast p}$ is an isomorphism; and (2) follows as there.

^pf-37-15-2

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§26 Transversality#^thm-26-1|§26.1]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§36 Submersions#^lem-36-5|§36.5]]

> [!definition] Definition §37.6: Normal Space
> Let $S \subseteq M$ be a regular submanifold with inclusion $\iota$, and $p \in S$. The **normal space** of $S$ at $p$ is the quotient vector space (Definition [[§21 Linear Algebra Toolkit#^def-21-6|§21.6]])
>
> $$
> T_pM / \iota_{\ast p}(T_pS) ,
> $$
>
> written $T_pM / T_pS$ when $T_pS$ is identified with its image (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]).

^def-37-6

*(Not from lecture.)* If $S$ has codimension $k$, the normal space has dimension $k$: $\dim T_pM = m$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]), $\dim \iota_{\ast p}(T_pS) = \dim T_pS = m - k$ because $\iota_{\ast p}$ is injective (Propositions [[§37 Regular Submanifolds#^prop-37-6|§37.6]] and [[§37 Regular Submanifolds#^prop-37-3|§37.3]]), and $\dim T_pM/\iota_{\ast p}(T_pS) = m - (m - k) = k$ by Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](3). It needs no metric, unlike the normal vectors of the remark *No Normal Vectors Without a Metric*; its dimension is that of the conormal space $N_pS$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]]).

> [!theorem] Proposition §37.16: Normal Spaces Under a Transverse Map
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
> So if $F \pitchfork S$, then $K_p = j_{\ast p}(T_pF^{-1}(S))$, with $j$ the inclusion of $F^{-1}(S)$ (Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]]) and $\bar F_{\ast p}$ is an isomorphism $T_pM/T_pF^{-1}(S) \cong T_qN/T_qS$ of the normal spaces (Definition [[§37 Regular Submanifolds#^def-37-6|§37.6]]): both have dimension $k$, which is the reason the codimension is preserved.

^prop-37-16

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
> *The transverse case.* If $F \pitchfork S$, then $\bar F_{\ast p}$ is injective by (2) and surjective by (3), hence an isomorphism, and $K_p = j_{\ast p}(T_pF^{-1}(S))$ by Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]](2). The dimensions are $\dim T_pM = m$ and $\dim T_qN = n$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]]); $\dim E = \dim T_qS = n - k$, as $\iota_{\ast q}$ is injective (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]); and $\dim K_p = m - k$ (Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]](1)). So by Proposition [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]](3)
>
> $$
> \dim T_pM/K_p = m - (m - k) = k = n - (n - k) = \dim T_qN/E ,
> $$
>
> as an isomorphism requires. Read backwards, the isomorphism alone gives $\dim K_p = m - \dim T_qN/E = m - k$: the codimension of $F^{-1}(S)$ in $M$ is the dimension of its normal space $T_pM/K_p$, and transversality makes $F_{\ast p}$ carry that normal space isomorphically onto the normal space of $S$, of dimension $k$.

^pf-37-16

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-6|Def. §21.6]], [[§21 Linear Algebra Toolkit#^prop-21-6|§21.6]], [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]], [[§37 Regular Submanifolds#^thm-37-15|§37.15]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]]

> [!theorem] Corollary §37.17: Special Cases of Transversality
> Let $F : M \to N$ be smooth, $\dim M = m$, $\dim N = n$.
>
> 1. *A point.* For $c \in N$, $\{c\}$ is a regular submanifold of $N$ of codimension $n$, and $F \pitchfork \{c\}$ if and only if $c$ is a regular value of $F$. In that case Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] returns the regular value theorem, Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]: $F^{-1}(c)$ is a regular submanifold of $M$ of codimension $n$, and $j_{\ast p}(T_pF^{-1}(c)) = \ker F_{\ast p}$ for $p \in F^{-1}(c)$.
> 2. *Two submanifolds.* Let $S, S' \subseteq N$ be regular submanifolds of codimensions $k$ and $k'$, with inclusions $\iota$ and $\iota'$, that *intersect transversally*:
>
> $$
> \iota'_{\ast p}\big(T_pS'\big) + \iota_{\ast p}\big(T_pS\big) = T_pN \qquad \text{for every } p \in S' \cap S ,
> $$
>
> that is, $\iota' \pitchfork S$ (a condition symmetric in $S$ and $S'$). Then $S' \cap S$ is a regular submanifold of $S'$ of codimension $k$, and a regular submanifold of $N$ of codimension $k + k'$; and, with all tangent spaces regarded as subspaces of $T_pN$, $T_p(S' \cap S) = T_pS' \cap T_pS$.
> 3. *Submersions.* If $F$ is a submersion, then $F \pitchfork S$ for every regular submanifold $S \subseteq N$, and $F^{-1}(S)$ is a regular submanifold of $M$ of the same codimension as $S$.
>
> *Lee: Theorem 6.30(b), for (2)*

^cor-37-17

> [!proof]+ Proof
> *(Not from lecture; filled in.)*
>
> *(1)* $\{c\}$ is a regular submanifold of $N$ of codimension $n$: it is the fibre $\mathrm{id}_N^{-1}(c)$ of the identity, a submersion since $(\mathrm{id}_N)_{\ast} = \mathrm{id}$ (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), so Corollary [[§37 Regular Submanifolds#^cor-37-13|§37.13]] applies. Its tangent space is $0$ (dimension $n - n = 0$, Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]] and Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]), so transversality at $p \in F^{-1}(c)$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]) reads $F_{\ast p}(T_pM) + 0 = T_cN$: $F_{\ast p}$ is onto. Thus $F \pitchfork \{c\}$ iff $F$ is a submersion at every point of $F^{-1}(c)$, iff $c$ is a regular value (Definition [[§36 Submersions#^def-36-4|§36.4]], the empty case included). Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]], with $S = \{c\}$ and $k = n$, then gives that $F^{-1}(c)$ is a regular submanifold of codimension $n$, and $j_{\ast p}(T_pF^{-1}(c)) = (F_{\ast p})^{-1}(0) = \ker F_{\ast p}$.
>
> *(2), in $S'$.* The inclusion $\iota' : S' \to N$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), $(\iota')^{-1}(S) = S' \cap S$, and $\iota'_{\ast p}(T_pS')$ is the image of the differential of $\iota'$ at $p$; so $\iota' \pitchfork S$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]) is the displayed condition, which is symmetric in $S$ and $S'$ because a sum of subspaces is. Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]], applied to $\iota'$ in place of $F$, makes $S' \cap S$ a regular submanifold of $S'$ of codimension $k = \operatorname{codim} S$, so of dimension $(n - k') - k = n - (k' + k)$, $S'$ having dimension $n - k'$ (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]); and, with $j : S' \cap S \to S'$ the inclusion, $j_{\ast p}(T_p(S' \cap S)) = (\iota'_{\ast p})^{-1}\big(\iota_{\ast p}(T_pS)\big)$: the vectors of $T_pS'$ whose image in $T_pN$ lies in $\iota_{\ast p}(T_pS)$. Applying $\iota'_{\ast p}$, and using that $\iota' \circ j$ is the inclusion of $S' \cap S$ into $N$ (Chain Rule), the tangent space of $S' \cap S$ inside $T_pN$ is
>
> $$
> \iota'_{\ast p}\Big((\iota'_{\ast p})^{-1}\big(\iota_{\ast p}(T_pS)\big)\Big) = \iota'_{\ast p}\big(T_pS'\big) \cap \iota_{\ast p}\big(T_pS\big) ,
> $$
>
> since for a linear map $A$ and a subspace $E$ of its target, $A\big(A^{-1}(E)\big) = \operatorname{im} A \cap E$: an element $Av$ with $Av \in E$ lies in both; conversely $w = Av \in E$ gives $v \in A^{-1}(E)$. With all tangent spaces regarded as subspaces of $T_pN$: $T_p(S' \cap S) = T_pS' \cap T_pS$.
>
> *(2), in $N$.* Fix $p \in S' \cap S$ (if $S' \cap S = \emptyset$ there is nothing to check). Take charts $(U, \varphi)$ adapted to $S$ and $(U', \varphi')$ adapted to $S'$ at $p$, with local defining maps $x_b : U \to \mathbb{R}^k$ and $x'_b : U' \to \mathbb{R}^{k'}$ (Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]]), and on the open set $V = U \cap U' \ni p$ put
>
> $$
> H = (x_b, x'_b) : V \longrightarrow \mathbb{R}^{k + k'} ,
> $$
>
> smooth because its components are. Its first $k$ components are those of $x_b$ and its last $k'$ those of $x'_b$.
> - *$H^{-1}(\vec 0) = V \cap S \cap S'$*: $H(q) = \vec 0$ iff $x_b(q) = \vec 0$ and $x'_b(q) = \vec 0$, iff $q \in U \cap S$ and $q \in U' \cap S'$ (Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]](3)).
> - *$\ker H_{\ast p} = \iota_{\ast p}(T_pS) \cap \iota'_{\ast p}(T_pS')$*: by Proposition [[§36 Submersions#^prop-36-4|§36.4]](1), $H_{\ast p}v = \sum_j dH^j|_p(v)\, \partial/\partial r^j|_{\vec 0}$, which is $0$ iff every coefficient $dH^j|_p(v)$ is $0$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]); by the same formula for $x_b$ and $x'_b$, $(x_b)_{\ast p}v = 0$ iff $dH^j|_p(v) = 0$ for $j \le k$, and $(x'_b)_{\ast p}v = 0$ iff $dH^j|_p(v) = 0$ for $j > k$. So $\ker H_{\ast p} = \ker (x_b)_{\ast p} \cap \ker (x'_b)_{\ast p}$, which is $\iota_{\ast p}(T_pS) \cap \iota'_{\ast p}(T_pS')$ by Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]](4).
> - *$H$ is a submersion at $p$*: by the dimension formula for a sum of two subspaces, with $\dim \iota_{\ast p}(T_pS) = n - k$ and $\dim \iota'_{\ast p}(T_pS') = n - k'$ ($\iota_{\ast p}$, $\iota'_{\ast p}$ injective, Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]) and their sum $T_pN$ by transversality,
>
> $$
> \dim \ker H_{\ast p} = (n - k) + (n - k') - n = n - k - k' ,
> $$
>
> so by rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) $\operatorname{rank} H_{\ast p} = n - (n - k - k') = k + k'$, and $H_{\ast p}$ is onto the $(k + k')$-dimensional $T_{\vec 0}\mathbb{R}^{k+k'}$.
>
> By Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](2), applied to $H : V \to \mathbb{R}^{k+k'}$ at $p$ with $c = \vec 0$, there is a chart $(W, \hat\theta)$ of $N$ at $p$, $W \subseteq V$, whose last $k + k'$ components vanish exactly on $W \cap H^{-1}(\vec 0) = W \cap S \cap S'$; it is adapted to $S' \cap S$, of codimension $k + k'$. As $p$ was arbitrary, $S' \cap S$ is a regular submanifold of $N$ of codimension $k + k'$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), of dimension $n - k - k'$, in agreement with the first part. And Lemma [[§37 Regular Submanifolds#^lem-37-11|§37.11]](3), with $W' = V$, gives again that its tangent space at $p$ is $\ker H_{\ast p} = \iota_{\ast p}(T_pS) \cap \iota'_{\ast p}(T_pS')$.
>
> *(3)* If $F$ is a submersion, then $F_{\ast p}(T_pM) = T_{F(p)}N$ already, so the sum in Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]] is all of $T_{F(p)}N$ at every $p \in F^{-1}(S)$: $F \pitchfork S$. Theorem [[§37 Regular Submanifolds#^thm-37-15|§37.15]] then makes $F^{-1}(S)$ a regular submanifold of $M$ of the same codimension as $S$.

^pf-37-17

*Uses:* [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^cor-37-13|§37.13]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-9|§29.9]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]], [[§36 Submersions#^def-36-4|Def. §36.4]], [[§37 Regular Submanifolds#^thm-37-15|§37.15]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§37 Regular Submanifolds#^prop-37-7|§37.7]], [[§36 Submersions#^prop-36-4|§36.4]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§37 Regular Submanifolds#^prop-37-6|§37.6]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§37 Regular Submanifolds#^lem-37-11|§37.11]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]

> [!remark] Remark: Special Cases and the Euclidean Versions
> *(Not from lecture.)* Corollary [[§37 Regular Submanifolds#^cor-37-17|§37.17]](1) is the manifold version of Corollary [[§26 Transversality#^cor-26-3|§26.3]], and (2) that of Proposition [[§26 Transversality#^prop-26-4|§26.4]]: the codimensions add, as for level sets. For $S = \{c\}$ a point, (3) is Corollary [[§37 Regular Submanifolds#^cor-37-13|§37.13]]: a submersion is transverse to every point, and its fibres are regular submanifolds of codimension $n$.

^rem-37-4

*Assignment 5, Problem 4 (“Revisiting Lagrange multipliers”), in the notation of these notes: the assignment's submanifold $M \subset N$ is here $S \subseteq M$, with $M$ the ambient manifold of dimension $m$; its conormal space $\mathcal{N}_pM$ is $N_pS$ (Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]); and $d(G^j)_p$ is written $dG^j|_p$. The problem: (a) a point is a critical point of the restriction $f = \Phi|_S$ of a smooth function $\Phi$ on $M$ exactly when $d\Phi_p$ is conormal to $S$; (b) for a regular level set $S = G^{-1}(0)$ the differentials $dG^1|_p, \ldots, dG^k|_p$ form a basis of $N_pS$, and the method of Lagrange multipliers follows. The proofs are the submitted solution's, written out.*

> [!theorem] Proposition §37.18: Critical Points of a Restriction
> Let $S \subseteq M$ be a regular submanifold, $\iota : S \to M$ the inclusion, $p \in S$, and $\iota_p^{\ast} : T_p^{\ast}M \to T_p^{\ast}S$ the pullback of covectors (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]). Let $\Phi : M \to \mathbb{R}$ be smooth and $f = \Phi \circ \iota = \Phi|_S : S \to \mathbb{R}$ its restriction.
>
> 1. $N_pS = \ker \iota_p^{\ast}$.
> 2. $df_p = \iota_p^{\ast}\big(d\Phi_p\big)$.
> 3. $p$ is a critical point of $f$ if and only if $d\Phi_p \in N_pS$.

^prop-37-18

> [!proof]+ Proof
> *(Assignment 5, Problem 4(a).)* The restriction $f = \Phi \circ \iota$ is smooth, as a composite of smooth maps (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1) and Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]), so $df_p \in T_p^{\ast}S$ is defined. By Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]] with $F = \iota$ and $F(p) = \iota(p) = p$, the pullback of a covector $\xi \in T_p^{\ast}M$ is the covector on $T_pS$
>
> $$
> \big(\iota_p^{\ast}\xi\big)(v) = \xi\big(\iota_{\ast p}v\big), \qquad v \in T_pS .
> $$
>
> *(1)* Let $\xi \in T_p^{\ast}M$. A covector is zero when it vanishes at every vector, and every element of $\iota_{\ast p}(T_pS)$ is $\iota_{\ast p}v$ for some $v \in T_pS$; so
>
> $$
> \iota_p^{\ast}\xi = 0 \iff \xi\big(\iota_{\ast p}v\big) = 0 \ \text{ for all } v \in T_pS \iff \xi(w) = 0 \ \text{ for all } w \in \iota_{\ast p}(T_pS) \iff \xi \in N_pS ,
> $$
>
> the last step by Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]]. So the annihilator of the tangent space, which is how Definition [[§37 Regular Submanifolds#^def-37-4|§37.4]] describes $N_pS$, is the kernel of the pullback, which is how the assignment describes it.
>
> *(2)* This is Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]] with $F = \iota$ and the function $\Phi$, smooth near $\iota(p) = p$: it gives $\iota_p^{\ast}(d\Phi_p) = d(\Phi \circ \iota)_p = df_p$. Written out for $v \in T_pS$, by Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]], the definition of the pushforward (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]), Proposition [[§32 The Cotangent Space#^prop-32-2|§32.2]] again, and the formula for $\iota_p^{\ast}$ above,
>
> $$
> df_p(v) = v\big[\Phi \circ \iota\big] = \big(\iota_{\ast p}v\big)[\Phi] = d\Phi_p\big(\iota_{\ast p}v\big) = \big(\iota_p^{\ast}(d\Phi_p)\big)(v) .
> $$
>
> Two covectors on $T_pS$ that agree at every $v$ are equal.
>
> *(3)* By Proposition [[§36 Submersions#^prop-36-2|§36.2]], applied to the smooth function $f$ on the manifold $S$, then (2), then (1),
>
> $$
> p \text{ is a critical point of } f \iff df_p = 0 \iff \iota_p^{\ast}\big(d\Phi_p\big) = 0 \iff d\Phi_p \in \ker \iota_p^{\ast} = N_pS .
> $$
>
> In words: $p$ is critical for the restriction exactly when $d\Phi_p$ vanishes on every vector tangent to $S$ at $p$.

^pf-37-18

*Uses:* [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]], [[§37 Regular Submanifolds#^def-37-4|Def. §37.4]], [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§32 The Cotangent Space#^prop-32-2|§32.2]], [[§28 Derivations and the Abstract Tangent Space#^def-28-6|Def. §28.6]], [[§36 Submersions#^prop-36-2|§36.2]]

> [!theorem] Proposition §37.19: The Conormal Space of a Regular Level Set
> Let $G = (G^1, \ldots, G^k) : M \to \mathbb{R}^k$ be smooth, with $0$ a regular value of $G$ (Definition [[§36 Submersions#^def-36-4|§36.4]]), and let $S = G^{-1}(0)$. Then for every $p \in S$ the covectors $dG^1|_p, \ldots, dG^k|_p$ form a basis of the conormal space $N_pS$.

^prop-37-19

> [!proof]+ Proof
> *(Assignment 5, Problem 4(b), first part. The dimension count cites Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]], which the submitted solution re-derives in an adapted chart; the submitted solution's independence argument, and its second, Jacobian form, are now the two proofs of Proposition [[§36 Submersions#^prop-36-4|§36.4]].)* Let $r^1, \ldots, r^k$ be the standard coordinates of $\mathbb{R}^k$, so that $G^j = r^j \circ G$; each $G^j$ is smooth, as a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]]). Fix $p \in S$. We show three things: $\dim N_pS = k$; each $dG^j|_p$ lies in $N_pS$; and the $k$ covectors $dG^j|_p$ are linearly independent. Then they span a $k$-dimensional subspace of the $k$-dimensional space $N_pS$, and a subspace of the same finite dimension is the whole space; so they are a basis.
>
> *$S$ is a regular submanifold, and $\dim N_pS = k$.* By Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], applied to $G : M \to \mathbb{R}^k$ and the regular value $0$ (so $n = k$ there), $S$ is a regular submanifold of $M$ of codimension $k$; so $N_pS$ is defined, and $\dim N_pS = k$ by Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](2). In an adapted chart $(x^1, \ldots, x^m)$ at $p$, a covector $\xi = \sum_i \xi_i\, dx^i|_p$ lies in $N_pS$ exactly when $\xi_i = 0$ for $i \le m - k$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](1)), so $N_pS$ has basis $dx^{m-k+1}|_p, \ldots, dx^m|_p$ (Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](2)).
>
> *Each $dG^j|_p$ lies in $N_pS$.* Let $1 \le j \le k$. Every $q \in S = G^{-1}(0)$ has $G(q) = 0$, so $(G^j \circ \iota)(q) = G^j(q) = 0$: the function $G^j \circ \iota$ is the constant $0$ on $S$, and its germ at $p$ is the constant germ $[\underline 0]$. So $(G^j \circ \iota)_{\ast p} = 0$, the pushforward along a constant map being zero (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]]), and hence $d(G^j \circ \iota)_p = 0$, the differential being this pushforward followed by the identification $T_0\mathbb{R} \cong \mathbb{R}$ (Definition [[§32 The Cotangent Space#^def-32-5|§32.5]]). By Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]](2) with $\Phi = G^j$,
>
> $$
> \iota_p^{\ast}\big(dG^j|_p\big) = d\big(G^j \circ \iota\big)_p = 0 ,
> $$
>
> so $dG^j|_p \in \ker \iota_p^{\ast} = N_pS$ by Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]](1).
>
> *Linear independence.* Since $0$ is a regular value and $p \in G^{-1}(0)$, $G$ is a submersion at $p$ (Definition [[§36 Submersions#^def-36-4|§36.4]](2)). By Proposition [[§36 Submersions#^prop-36-4|§36.4]](2), direction ($\Rightarrow$), the covectors $dG^1|_p, \ldots, dG^k|_p$ are therefore linearly independent. Its proof is the submitted solution's argument: by its formula (1), $G_{\ast p}v = \sum_j dG^j|_p(v)\, \partial/\partial r^j|_0$, a relation $\sum_j c_j\, dG^j|_p = 0$ says $c \cdot G_{\ast p}(v) = 0$ for every $v$, and since $G_{\ast p}$ is onto we may take $G_{\ast p}(v) = c$, which gives $|c|^2 = 0$. Its second proof is the Jacobian form: the relation says $J^{\mathsf T} c = 0$ for the $k \times m$ matrix $J = [\partial G^j/\partial x^i(p)]$ of $G_{\ast p}$ in any chart, and $J^{\mathsf T}$ has rank $k$.
>
> *Conclusion.* $dG^1|_p, \ldots, dG^k|_p$ are $k$ linearly independent elements of $N_pS$, which has dimension $k$, so they form a basis of $N_pS$. As $p \in S$ was arbitrary, this holds at every point of $S$.

^pf-37-19

*Uses:* [[§37 Regular Submanifolds#^prop-37-8|§37.8]], [[§36 Submersions#^prop-36-4|§36.4]], [[§19 Smooth Functions and Smooth Maps#^lem-19-5|§19.5]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-10|§28.10]], [[§32 The Cotangent Space#^def-32-5|Def. §32.5]], [[§37 Regular Submanifolds#^prop-37-18|§37.18]], [[§36 Submersions#^def-36-4|Def. §36.4]]

The assignment adds that a regular submanifold is *locally* always a regular level set: this is Proposition [[§37 Regular Submanifolds#^prop-37-7|§37.7]]. Given an adapted chart $(U, \varphi = (x_a, x_b))$, put $G = x_b : U \to \mathbb{R}^k$. By that proposition, $U \cap S = G^{-1}(0)$ and $0$ is a regular value of $G$ (part (3)), $G$ being a submersion at every point of $U$ (part (2)). So Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]] and the theorem below apply to $U \cap S \subseteq U$. For this $G$ the basis $dG^j|_p = dx^{m-k+j}|_p$ is the basis of Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](2).

> [!theorem] Theorem §37.20: Lagrange Multipliers
> Let $G = (G^1, \ldots, G^k) : M \to \mathbb{R}^k$ be smooth with $0$ a regular value, $S = G^{-1}(0)$, $\Phi : M \to \mathbb{R}$ smooth, and $f = \Phi|_S$.
>
> 1. If $f$ has a local extremum at $p \in S$ — $f(q) \le f(p)$ for all $q$ in some neighbourhood of $p$ in $S$, or $f(q) \ge f(p)$ for all such $q$ — then $p$ is a critical point of $f$.
> 2. A point $p \in S$ is a critical point of $f$ if and only if there are $\lambda_1, \ldots, \lambda_k \in \mathbb{R}$ with
>
> $$
> d\Phi_p = \sum_{j=1}^k \lambda_j\, dG^j|_p ,
> $$
>
> and the **Lagrange multipliers** $\lambda_j$ are then unique. Equivalently, the critical points of $f$ are the points $p \in M$ for which there is $\lambda \in \mathbb{R}^k$ with
>
> $$
> d\Big(\Phi - \sum_{j=1}^k \lambda_j G^j\Big)_p = 0, \qquad G(p) = 0 .
> $$
>
> 3. If $M = \mathbb{R}^m$, with the gradient $\nabla h(p) = \big(\partial h/\partial r^1(p), \ldots, \partial h/\partial r^m(p)\big)$ (Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]), the vector with $\nabla h(p) \cdot v = dh_p(v)$ (Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]), the conditions of (2) read
>
> $$
> \nabla\Phi(p) = \sum_{j=1}^k \lambda_j\, \nabla G^j(p), \qquad G^1(p) = \cdots = G^k(p) = 0 ,
> $$
>
> $m + k$ equations in the $m + k$ unknowns $(p, \lambda) \in \mathbb{R}^m \times \mathbb{R}^k$.

^thm-37-20

> [!proof]+ Proof
> *(Assignment 5, Problem 4(b), second part: “explain how the method of Lagrange multipliers follows.”)* By Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], $S$ is a regular submanifold of $M$, and $f = \Phi \circ \iota$ is smooth on it (Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]]).
>
> *(1)* This is Proposition [[§36 Submersions#^prop-36-3|§36.3]], applied to the smooth function $f$ on the manifold $S$ (with its induced structure) and the neighbourhood of $p$ in $S$ on which $f \le f(p)$ (or $f \ge f(p)$): it gives $df_p = 0$, which by Proposition [[§36 Submersions#^prop-36-2|§36.2]] says that $p$ is a critical point of $f$. Its proof is the argument along curves: every $v \in T_pS$ is the velocity $D_\gamma$ of a smooth curve $\gamma$ in $S$ with $\gamma(0) = p$ (Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]]), $f \circ \gamma$ has a local extremum at the interior point $0$, and $df_p(v) = (f \circ \gamma)'(0) = 0$. So the method, which looks for the critical points of $f$, finds in particular all local extrema of $\Phi$ subject to the constraint $G = 0$.
>
> *(2)* By Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]](3), $p$ is a critical point of $f$ iff $d\Phi_p \in N_pS$. By Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]], $N_pS$ is the span of $dG^1|_p, \ldots, dG^k|_p$. So if $p$ is critical, $d\Phi_p$ is a linear combination $\sum_j \lambda_j\, dG^j|_p$; conversely, such a combination lies in $N_pS$, which is a subspace (the kernel of the linear map $\iota_p^{\ast}$, Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]](1)) containing every $dG^j|_p$, so $p$ is critical. *Uniqueness:* if $\sum_j \lambda_j\, dG^j|_p = \sum_j \mu_j\, dG^j|_p$, then $\sum_j (\lambda_j - \mu_j)\, dG^j|_p = 0$, and linear independence of the $dG^j|_p$ (Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]], or directly Proposition [[§36 Submersions#^prop-36-4|§36.4]](2), $G$ being a submersion at $p \in G^{-1}(0)$) gives $\lambda_j = \mu_j$ for every $j$. *The equivalent form:* the function $\Phi - \sum_j \lambda_j G^j$ is smooth on $M$, and linearity of $d$ (Corollary [[§32 The Cotangent Space#^cor-32-3|§32.3]](1), applied once for each of the $k$ terms) gives
>
> $$
> d\Big(\Phi - \sum_{j=1}^k \lambda_j G^j\Big)_p = d\Phi_p - \sum_{j=1}^k \lambda_j\, dG^j|_p ,
> $$
>
> which is $0$ iff $d\Phi_p = \sum_j \lambda_j\, dG^j|_p$; and a point $p \in M$ lies in $S = G^{-1}(0)$ iff $G(p) = 0$.
>
> *(3)* Use the identity chart of $\mathbb{R}^m$, with coordinate functions $r^1, \ldots, r^m$; its coordinate derivations are the ordinary partial derivatives, $\partial/\partial r^i|_p[h] = \partial h/\partial r^i(p)$ (Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], the chart being the identity). For a smooth $h$ on $\mathbb{R}^m$, Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]] gives $dh_p = \sum_i \partial h/\partial r^i(p)\, dr^i|_p$: the components of $dh_p$ are the entries of the gradient $\nabla h(p)$ (Definition [[§33 Covectors in Coordinates#^def-33-2|§33.2]]). This is the identification of Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]: under the linear isomorphism $v \mapsto \xi_v$ of $\mathbb{R}^m$ onto $T_p^{\ast}\mathbb{R}^m$, $\xi_v(D_w|_p) = v \cdot w$, the vector $\nabla h(p)$ goes to $dh_p$. (So for $w = \sum_i w^i\, \partial/\partial r^i|_p$, identified with $(w^1, \ldots, w^m) \in \mathbb{R}^m$ as in Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], $dh_p(w) = \sum_i \partial h/\partial r^i(p)\, w^i = \nabla h(p) \cdot w$.) Two covectors are equal iff their components in the basis $dr^i|_p$ are equal, so, applying this to $h = \Phi$ and $h = G^j$,
>
> $$
> d\Phi_p = \sum_{j=1}^k \lambda_j\, dG^j|_p \iff \frac{\partial \Phi}{\partial r^i}(p) = \sum_{j=1}^k \lambda_j\, \frac{\partial G^j}{\partial r^i}(p) \ \ (i = 1, \ldots, m) \iff \nabla\Phi(p) = \sum_{j=1}^k \lambda_j\, \nabla G^j(p) .
> $$
>
> Equivalently, by Proposition [[§33 Covectors in Coordinates#^prop-33-3|§33.3]]: $v \mapsto \xi_v$ is linear and injective, with $\xi_{\nabla\Phi(p)} = d\Phi_p$ and $\xi_{\nabla G^j(p)} = dG^j|_p$, so $d\Phi_p = \sum_j \lambda_j\, dG^j|_p$ says $\xi_{\nabla\Phi(p)} = \xi_{\sum_j \lambda_j \nabla G^j(p)}$, that is, $\nabla\Phi(p) = \sum_j \lambda_j\, \nabla G^j(p)$.
> With $G(p) = 0$ from (2) this is the system stated: $m$ scalar equations from the gradients and $k$ from the constraints, in the $m$ coordinates of $p$ and the $k$ multipliers. (The count makes a finite set of solutions plausible; it is not a theorem that there are any, or finitely many.)

^pf-37-20

*Uses:* [[§37 Regular Submanifolds#^thm-37-12|§37.12]], [[§37 Regular Submanifolds#^prop-37-18|§37.18]], [[§36 Submersions#^prop-36-3|§36.3]], [[§36 Submersions#^prop-36-2|§36.2]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-2|§31.2]], [[§37 Regular Submanifolds#^prop-37-19|§37.19]], [[§36 Submersions#^prop-36-4|§36.4]], [[§32 The Cotangent Space#^cor-32-3|§32.3]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§33 Covectors in Coordinates#^def-33-2|Def. §33.2]], [[§33 Covectors in Coordinates#^prop-33-3|§33.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]

> [!remark]- Connections
> - In $\mathbb{R}^n$, with proofs by the implicit function theorem: [[Method of Lagrange Multipliers|452 hub]], [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 Thm. §17.3]] (several constraints); computational treatment: [[§114 Lagrange Multipliers#^thm-114-1|Calc Thm. §114.1]].
> - In mechanics, constraint forces as multipliers: [[§B6.3 Constraints and Lagrange Multipliers#^thm-b6-3-1|CM Thm. §B6.3.1]].

*(Not from the assignment.)* In (3) the system is the vanishing of the gradient of the single function $L(x, \lambda) = \Phi(x) - \sum_j \lambda_j G^j(x)$ on $\mathbb{R}^{m+k}$: its partial derivatives at $(p, \lambda)$ are $\partial\Phi/\partial r^i(p) - \sum_j \lambda_j\, \partial G^j/\partial r^i(p)$ in the direction of $x^i$ and $-G^j(p)$ in the direction of $\lambda_j$, so $\nabla L(p, \lambda) = 0$ is exactly the $m + k$ equations above.

> [!remark] Remark: The Conormal Bundle
> *(Not from the assignment.)* The conormal spaces $N_pS$, $p \in S$, can be put together, as the cotangent spaces are put together in the cotangent bundle $T^{\ast}M$, into the *conormal bundle* $N^{\ast}S \subseteq T^{\ast}M$. This is done later, in [[§52 Critical Points and the Hessian|§52]], once $T^{\ast}M$ and its standard coordinates are available (Definition [[§52 Critical Points and the Hessian#^def-52-6|§52.6]]). There $N^{\ast}S$ is shown to be a regular submanifold of $T^{\ast}M$ of dimension $m$, whatever the codimension of $S$, cut out in the standard coordinates over an adapted chart by the description of $N_pS$ in Proposition [[§37 Regular Submanifolds#^prop-37-8|§37.8]](1) (Proposition [[§52 Critical Points and the Hessian#^prop-52-6|§52.6]]); the critical points of a restriction $\Phi|_S$ are where the graph of $d\Phi$ meets it, by Proposition [[§37 Regular Submanifolds#^prop-37-18|§37.18]](3) (Corollary [[§52 Critical Points and the Hessian#^cor-52-7|§52.7]]); and for $S = G^{-1}(0)$ the Lagrange multipliers of Theorem [[§37 Regular Submanifolds#^thm-37-20|§37.20]] are the coordinates of $(p, d\Phi_p) \in N^{\ast}S$ in its fibre, in the basis $dG^1|_p, \ldots, dG^k|_p$ of Proposition [[§37 Regular Submanifolds#^prop-37-19|§37.19]].

^rem-37-5

## Transverse Submanifolds

*Review session, Oct 16 (and Uribe's email before it). The homework defined a map transverse to a submanifold (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]). “We can also talk about two submanifolds being transverse to each other, which was the original definition historically, and then it was generalized.” The Euclidean version is Definition [[§26 Transversality#^def-26-3|§26.3]].*

> [!definition] Definition §37.7: Transverse Submanifolds
> Let $S_1, S_2 \subseteq N$ be regular submanifolds. $S_1$ **intersects $S_2$ transversally**, written $S_1 \pitchfork S_2$, if
>
> $$
> T_qS_1 + T_qS_2 = T_qN \qquad \text{for every } q \in S_1 \cap S_2 ,
> $$
>
> with $T_qS_i \subseteq T_qN$ through the inclusions (Proposition [[§37 Regular Submanifolds#^prop-37-6|§37.6]]). The condition holds vacuously if $S_1 \cap S_2 = \varnothing$.
>
> *Lee: Ch. 6, Transversality*

^def-37-7

On the notation: “I don't like it … to me it's very confusing, because intersection to me is an operation … This is a statement, not a set.”

> [!theorem] Proposition §37.21: Transverse Submanifolds and Transverse Maps
> $S_1 \pitchfork S_2$ if and only if the inclusion $\iota_1 : S_1 \hookrightarrow N$ is transverse to $S_2$ (Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]]).

^prop-37-21

> [!proof]+ Proof
> *(Stated in the review session: “if you look at the definitions, it's the same”; written out.)* $\iota_1^{-1}(S_2) = S_1 \cap S_2$, and for $q$ in it, $(\iota_1)_{\ast q}(T_qS_1)$ is $T_qS_1$ regarded as a subspace of $T_qN$. So the condition of Definition [[§37 Regular Submanifolds#^def-37-5|§37.5]] for $F = \iota_1$ at $q$ is $T_qS_1 + T_qS_2 = T_qN$.

^pf-37-21

*Uses:* [[§37 Regular Submanifolds#^def-37-5|Def. §37.5]]

> [!theorem] Theorem §37.22: Transverse Intersections in a Manifold
> If $S_1 \pitchfork S_2$ in $N$, then $S_1 \cap S_2$ is a regular submanifold of $N$, with
>
> $$
> \operatorname{codim}(S_1 \cap S_2) = \operatorname{codim} S_1 + \operatorname{codim} S_2, \qquad T_q(S_1 \cap S_2) = T_qS_1 \cap T_qS_2 .
> $$
>
> *Lee: Theorem 6.30(b)*

^thm-37-22

> [!proof]+ Proof
> *(The theorem “that you proved in homework”, first in the Euclidean case, Proposition [[§26 Transversality#^prop-26-4|§26.4]]; “again, that's just a linear algebra thing.” The manifold version is filled in, along the Euclidean proof.)* Let $n = \dim N$, $k_i = \operatorname{codim} S_i$, and $q \in S_1 \cap S_2$.
>
> *Local defining functions.* Take a slice chart $(U_i, \varphi_i)$ for $S_i$ at $q$ (Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]]), so that $U_i \cap S_i = G_i^{-1}(0)$, where $G_i : U_i \to \mathbb{R}^{k_i}$ is the last $k_i$ coordinates of $\varphi_i$. $G_i$ is a submersion (a coordinate projection composed with a chart), so by the regular value theorem (Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]]) $T_qS_i = \ker (dG_i)_q$, a subspace of $T_qN$ of dimension $n - k_i$.
>
> *Transversality is a regular value condition.* On $W = U_1 \cap U_2$ put $G = (G_1, G_2) : W \to \mathbb{R}^{k_1 + k_2}$, so that $W \cap S_1 \cap S_2 = G^{-1}(0)$ and $\ker dG_q = K_1 \cap K_2$, with $K_i = \ker (dG_i)_q = T_qS_i$. By the dimension formula for subspaces,
>
> $$
> \dim(K_1 \cap K_2) = \dim K_1 + \dim K_2 - \dim(K_1 + K_2) = 2n - k_1 - k_2 - \dim(K_1 + K_2).
> $$
>
> So $K_1 + K_2 = T_qN$ if and only if $\dim \ker dG_q = n - k_1 - k_2$, if and only if $dG_q$ has rank $k_1 + k_2$, that is, is onto. In a chart $(x^1, \ldots, x^n)$ at $q$, with $G_i = (G_i^1, \ldots, G_i^{k_i})$, the matrix of $dG_q$ is the $(k_1 + k_2) \times n$ matrix that stacks those of $(dG_1)_q$ and $(dG_2)_q$:
>
> $$
> \left(\begin{array}{ccc} \dfrac{\partial G_1^1}{\partial x^1}(q) & \cdots & \dfrac{\partial G_1^1}{\partial x^n}(q) \\ \vdots & & \vdots \\ \dfrac{\partial G_1^{k_1}}{\partial x^1}(q) & \cdots & \dfrac{\partial G_1^{k_1}}{\partial x^n}(q) \\ \hline \dfrac{\partial G_2^1}{\partial x^1}(q) & \cdots & \dfrac{\partial G_2^1}{\partial x^n}(q) \\ \vdots & & \vdots \\ \dfrac{\partial G_2^{k_2}}{\partial x^1}(q) & \cdots & \dfrac{\partial G_2^{k_2}}{\partial x^n}(q) \end{array}\right) ,
> $$
>
> so a vector is in its kernel exactly when it is killed by both blocks. Since $S_1 \pitchfork S_2$, this holds at every point of $G^{-1}(0)$: $0$ is a regular value of $G$.
>
> *Conclusion.* By Theorem [[§37 Regular Submanifolds#^thm-37-12|§37.12]], $G^{-1}(0) = W \cap S_1 \cap S_2$ is a regular submanifold of $W$ of codimension $k_1 + k_2$, with $T_q(S_1 \cap S_2) = \ker dG_q = T_qS_1 \cap T_qS_2$. Being a regular submanifold is a local condition (slice charts at each point), and $W$ is open in $N$; $q$ was arbitrary, so $S_1 \cap S_2$ is a regular submanifold of $N$ of codimension $k_1 + k_2$.

^pf-37-22

*Uses:* [[§26 Transversality#^prop-26-4|§26.4]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§37 Regular Submanifolds#^thm-37-12|§37.12]]

*The picture*, asked for by a student (“wonderful picture … great question, I haven't drawn enough pictures”). In $\mathbb{R}^3$, if $S_1$ is a surface and $S_2$ a curve, at a point of intersection the tangent plane and the tangent line must add up to all of $\mathbb{R}^3$, so the curve “has to come across like that … it has to pierce” the surface. If both are surfaces, two planes add up to $\mathbb{R}^3$ exactly when they are different, and then they meet in a line: the surfaces cut through each other along a curve. “It's really a local picture … just the vector space picture.”

![[m591-37-1.svg]]

Codimensions add: $1 + 2 = 3$ for a surface and a curve, a point; $1 + 1 = 2$ for two surfaces, a curve. In the Morse problem of the homework the same thing happened in $T^{\ast}M$: the section $s_f = df$ “was actually an embedding because it was a section, so it's the same as intersecting the image of the embedding with the zero section” (Theorem [[§52 Critical Points and the Hessian#^thm-52-10|§52.10]]), and there $m + m = 2m$, the full dimension: the intersection is a set of isolated points.
