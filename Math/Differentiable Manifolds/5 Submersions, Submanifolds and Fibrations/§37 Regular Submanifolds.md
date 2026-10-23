---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 37
tags: [differentiable-manifolds, math591]
---
← [[§36 Submersions]] · ↑ [[· 5 Submersions, Submanifolds and Fibrations]] · [[§38 The Regular Value Theorem for Manifolds]] →

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
> Regular submanifolds are also called **embedded** submanifolds, as opposed to the [[§44 Embeddings#^def-44-4|immersed submanifolds]] of [[§44 Embeddings#^def-44-4|Definition §44.4]]. In these notes, “submanifold” without qualification means a regular submanifold.
>
> *Lee: Theorem 5.8*

^def-37-2

> [!remark]- Connections
> - The other kind of submanifold: [[§44 Embeddings#^def-44-4|immersed submanifolds, Def. §44.4]]; when an immersed submanifold is regular: [[§44 Embeddings#^prop-44-15|§44.15]]; local images of immersions: [[§43 Immersions#^cor-43-2|§43.2]].
> - Codimension in the Euclidean setting: [[§26 Transversality#^def-26-1|Def. §26.1]].
> - The geometric stage: in $\mathbb{R}^{n+k}$ the submanifolds are exactly the manifolds of [[§20 Manifolds in Euclidean Space|§20]] — the external, internal and graph descriptions ([[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]) — and the slice of this definition is a fourth: [[§37 Regular Submanifolds#^prop-37-9|§37.9]].
> - Their tangent spaces: $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) is $\iota_{\ast p}(T_pX)$ ([[§37 Regular Submanifolds#^rem-37-2|Remark: The Tangent Spaces Match]], [[§38 The Regular Value Theorem for Manifolds#^prop-38-4|§38.4]]).

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
> - The Euclidean prototype, level sets with graph charts: [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]; the two structures agree by [[§38 The Regular Value Theorem for Manifolds#^prop-38-4|§38.4]].

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
> *(Not from lecture.)* The two tangent spaces of the geometric and the abstract stage correspond as well. Externally, $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]]). In the slice chart of [[§37 Regular Submanifolds#^prop-37-9|Proposition §37.9]], with $F = x_b$, this kernel is the set of vectors on which the differentials of the last $k$ coordinates vanish, the span of the first $n$ coordinate directions; and that span is $\iota_{\ast p}(T_pX)$ ([[§37 Regular Submanifolds#^prop-37-6|Proposition §37.6]]). [[§38 The Regular Value Theorem for Manifolds#^prop-38-4|Proposition §38.4]] below makes the identification precise, together with the agreement of the two smooth structures.

^rem-37-2
