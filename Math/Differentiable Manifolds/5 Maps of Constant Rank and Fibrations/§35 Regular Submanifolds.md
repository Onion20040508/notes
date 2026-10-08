---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 35
tags: [differentiable-manifolds, math591]
---
← [[§34 Submersions]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§36 Fibrations]] →

*Stage: submanifolds — Subsets of a manifold that are locally coordinate slices — the equations thread, completed.*

*References: Lee Ch. 5. Lecture 12.*

The subsets of a manifold that look locally like $\mathbb{R}^{m-k} \subseteq \mathbb{R}^m$. The regular value theorem for manifolds, proved from the submersion normal form of [[§34 Submersions|§34]], produces them as level sets — the end of the equations thread that began in [[§7 The Regular Value Theorem|§7]].

## Regular Submanifolds

*Lecture 12 (Mon Sep 28). “I know we're in the middle of discussing submersions and fibrations, but we need the notion of submanifold. So let's pause to discuss that. It's not difficult.” The local model is a lower-dimensional Euclidean space inside a higher-dimensional one: $\mathbb{R}^{m-k} \subseteq \mathbb{R}^m$ as the points whose last $k$ coordinates vanish, $x \mapsto (x, \vec 0)$.*

> [!definition] Definition §35.1: Regular Submanifold
> Let $M$ be a smooth manifold of dimension $m$, $S \subseteq M$ a subset with the subspace topology, and $0 \le k \le m$. For a chart $\varphi = (x^1, \ldots, x^m)$ write $x_a = (x^1, \ldots, x^{m-k})$ for its first $m - k$ components and $x_b = (x^{m-k+1}, \ldots, x^m)$ for its last $k$. Then $S$ is a **regular submanifold of $M$ of codimension $k$** if every $p \in S$ lies in the domain of a smooth chart $(U, \varphi)$ of $M$ with
>
> $$
> U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\}.
> $$
>
> Regular submanifolds are also called **embedded** submanifolds, as opposed to the [[§38 Embeddings#^def-38-4|immersed submanifolds]] of [[§38 Embeddings#^def-38-4|Definition §38.4]]. In these notes, “submanifold” without qualification means a regular submanifold.
>
> *Lee: Theorem 5.8*

^def-35-1

> [!remark]- Connections
> - The other kind of submanifold: [[§38 Embeddings#^def-38-4|immersed submanifolds, Def. §38.4]]; when an immersed submanifold is regular: [[§38 Embeddings#^prop-38-14|§38.14]]; local images of immersions: [[§37 Immersions#^cor-37-2|§37.2]].
> - Codimension in the Euclidean setting: [[§26 Transversality#^def-26-1|Def. §26.1]].
> - The geometric stage: in $\mathbb{R}^{n+k}$ the submanifolds are exactly the manifolds of [[§20 Manifolds in Euclidean Space|§20]] — the external, internal and graph descriptions ([[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]]) — and the slice of this definition is a fourth: [[§35 Regular Submanifolds#^prop-35-6|§35.6]].
> - Their tangent spaces: $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]) is $\iota_{\ast p}(T_pX)$ ([[§35 Regular Submanifolds#^rem-35-2|Remark: The Tangent Spaces Match]], [[§35 Regular Submanifolds#^prop-35-9|§35.9]]).

> [!definition] Definition §35.2: Adapted Chart
> Let $M$, $S$ and $k$ be as in [[§35 Regular Submanifolds#^def-35-1|Definition §35.1]]. Such charts — smooth charts $(U, \varphi)$ of $M$ with $U \cap S = \{\, q \in U : x_b(q) = \vec 0 \,\}$ — are **adapted** to $S$; “a random chart of $M$ is not adapted.” In an adapted chart, $U \cap S$ is cut out by the $k$ equations $x^{m-k+1} = \cdots = x^m = 0$, exactly as in the local model.
>
> *Lee: Theorem 5.8*

^def-35-2

> [!remark]- Connections
> - In Euclidean space an adapted chart comes from a graph chart ([[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) by straightening the graph: [[§35 Regular Submanifolds#^prop-35-6|§35.6]] and its figure.

> [!theorem] Proposition §35.1: Two Observations on Adapted Charts
> Let $(U, \varphi)$ be a smooth chart of $M$, and suppose that $U \cap S$ is cut out in it by setting some $k$ of the coordinates equal to constants:
>
> $$
> U \cap S = \{\, q \in U : x^{i_1}(q) = c_1, \ \ldots, \ x^{i_k}(q) = c_k \,\}.
> $$
>
> Then there is an adapted chart with the same domain $U$. That is:
> 1. the value $\vec 0$ in the definition may be replaced by any constant vector $\vec c$;
> 2. the last $k$ coordinates may be replaced by any $k$ of them.

^prop-35-1

> [!proof]+ Proof
> *(Lecture 12: “obvious observations”; filled in.)* Let $P : \mathbb{R}^m \to \mathbb{R}^m$ be the permutation of coordinates that moves positions $i_1, \ldots, i_k$ to the last $k$ places, and $T(r) = r - (\vec 0, \vec c)$. Then $A = T \circ P$ is an affine diffeomorphism of $\mathbb{R}^m$, so $(U, A \circ \varphi)$ is a smooth chart: a chart by Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]], whose transition maps with any smooth chart are those of $\varphi$ composed with $A$ or $A^{-1}$, hence smooth. Its last $k$ coordinates are $x^{i_1} - c_1, \ldots, x^{i_k} - c_k$, which vanish exactly on $U \cap S$.

^pf-35-1

*Uses:* [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§2 Topological Manifolds#^lem-2-10|§2.10]]

> [!theorem] Proposition §35.2: The Induced Smooth Structure
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

^prop-35-2

> [!proof]+ Proof
> *(Lecture 12 claimed (1) — “easy to check” — and gave the reason for (2); completed here.)* $S$ is Hausdorff and second countable as a subspace of $M$ (Theorem [[§3 Subspaces and Products#^thm-3-5|§3.5]]) — “back to week one of the class.” Let $j : \mathbb{R}^{m-k} \to \mathbb{R}^m$, $j(r) = (r, \vec 0)$, and $\mathrm{pr} : \mathbb{R}^m \to \mathbb{R}^{m-k}$, $\mathrm{pr}(r, s) = r$.
>
> (1) $U \cap S$ is open in $S$ by the definition of the subspace topology. Since $U \cap S = \{x_b = \vec 0\}$, the chart $\varphi$ maps $U \cap S$ bijectively onto $\varphi(U) \cap j(\mathbb{R}^{m-k}) = j(W)$, where $W = j^{-1}(\varphi(U))$ is open in $\mathbb{R}^{m-k}$ because $j$ is continuous. So $\varphi_S = \mathrm{pr} \circ \varphi|_{U \cap S}$ is a continuous bijection $U \cap S \to W$, with continuous inverse $r \mapsto \varphi^{-1}(j(r))$.
>
> (2) Every point of $S$ lies in an adapted chart, so the domains cover $S$. For adapted charts $(U, \varphi)$ and $(V, \psi)$, since $\varphi_S^{-1} = \varphi^{-1} \circ j$,
>
> $$
> \psi_S \circ \varphi_S^{-1} = \mathrm{pr} \circ (\psi \circ \varphi^{-1}) \circ j \qquad \text{on } \varphi_S(U \cap V \cap S) = j^{-1}\big(\varphi(U \cap V)\big) .
> $$
>
> This is the transition map of $M$, which is smooth, composed with the linear maps $j$ and $\mathrm{pr}$: the transition maps of $S$ are “restrictions to $\mathbb{R}^{m-k}$ of $C^\infty$ maps between open sets of $\mathbb{R}^m$.”

^pf-35-2

*Uses:* [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]]

![[m591-15-1.svg]]
*An adapted chart ($m = 2$, $k = 1$). The chart $\varphi$ straightens $U \cap S$ onto the part of the $x_a$-axis inside $\varphi(U)$ — exactly the set $\varphi(U) \cap \{x_b = 0\}$, running from rim to rim — and the induced chart $\varphi_S$ keeps only the coordinate $x_a$, landing on an open interval of $\mathbb{R}^{m-k}$.*

> [!remark]- Connections
> - The subspace topology: [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]].
> - The Euclidean prototype, level sets with graph charts: [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]; the two structures agree by [[§35 Regular Submanifolds#^prop-35-9|§35.9]].

**Extending charts.** A student asked whether every chart of $S$ extends to an adapted chart of $M$. Uribe: “The answer is yes” — since everything reduces to the local Euclidean picture, the $m - k$ functions of a chart of $S$ extend to a neighbourhood in $M$. This is stated, not proved, here; likewise his remark that smooth functions on $S$ extend to smooth functions near $S$.

> [!theorem] Lemma §35.3: Smooth Maps and Regular Submanifolds
> Let $S \subseteq M$ be a regular submanifold, with its induced structure, and $\iota : S \to M$ the inclusion.
> 1. $\iota$ is smooth; in an adapted chart and its induced chart, its coordinate representation is $j(r) = (r, \vec 0)$.
> 2. If $G : X \to M$ is smooth and $G(X) \subseteq S$, then $G$ is smooth as a map into $S$.
>
> *Lee: Corollary 5.30*

^lem-35-3

> [!proof]+ Proof
> *((1) is Uribe's “immediate from the definitions”; filled in, and (2) is not from lecture.)* (1) $\iota$ is continuous for the subspace topology. For an adapted chart, $\varphi \circ \iota \circ \varphi_S^{-1} = \varphi \circ \varphi^{-1} \circ j = j$ on $\varphi_S(U \cap S)$, which is smooth, so $\iota$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]). (2) $G$ is continuous into $S$, since $G^{-1}(O \cap S) = G^{-1}(O)$ for $O$ open in $M$. Given $x \in X$, take an adapted chart $(U, \varphi)$ at $G(x)$ and a chart $\chi$ of $X$ at $x$ with domain inside $G^{-1}(U)$. Then $\varphi_S \circ G \circ \chi^{-1} = \mathrm{pr} \circ (\varphi \circ G \circ \chi^{-1})$, a linear map composed with a coordinate representation of the smooth map $G$, hence smooth.

^pf-35-3

*Uses:* [[§35 Regular Submanifolds#^prop-35-2|§35.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]]

![[m591-15-2.svg]] ![[m591-15-3.svg]]
*Left, (1): in an adapted chart and its induced chart the inclusion is $j(r) = (r, \vec 0)$. Right, (2): a smooth map into $M$ whose values lie in $S$ factors through $S$, and the factor — dashed — is smooth.*

> [!theorem] Proposition §35.4: Tangent Spaces of a Regular Submanifold
> Let $S \subseteq M$ be a regular submanifold of codimension $k$ and $p \in S$. Then $\iota_{*p} : T_pS \to T_pM$ is injective. In an adapted chart $(x^1, \ldots, x^m)$ at $p$, writing $\partial/\partial x^i|^S_p$ for the coordinate derivations of the induced chart $(x^1, \ldots, x^{m-k})$ of $S$,
>
> $$
> \iota_{*p}\Big(\frac{\partial}{\partial x^i}\Big|^S_p\Big) = \frac{\partial}{\partial x^i}\Big|_p \quad (i \le m - k), \qquad \iota_{*p}(T_pS) = \operatorname{Span}\Big\{\frac{\partial}{\partial x^1}\Big|_p, \ldots, \frac{\partial}{\partial x^{m-k}}\Big|_p\Big\}.
> $$
>
> Equivalently, by curves: for a smooth curve $\gamma$ in $S$ with $\gamma(0) = p$, $\iota_{*p} D_\gamma = D_{\iota \circ \gamma}$ — a curve in $S$ is a curve in $M$, with the same velocity.
>
> *Lee: Propositions 5.35 and 5.37*

^prop-35-4

> [!proof]+ Proof
> *(Lecture 12: “immediate from the definitions”; filled in.)* By Lemma [[§35 Regular Submanifolds#^lem-35-3|§35.3]](1) the coordinate representation of $\iota$ is $j$, whose Jacobian is the $m \times (m-k)$ matrix $\binom{I_{m-k}}{0}$. By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] this is the matrix of $\iota_{\ast p}$ in the coordinate bases; its $i$-th column gives the formula, and its columns are independent, so $\iota_{\ast p}$ is injective. The statement for curves is Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]].

^pf-35-4

*Uses:* [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]

So $T_pS$ is identified with the $(m-k)$-dimensional subspace $\iota_{*p}(T_pS) \subseteq T_pM$, the “intrinsic tangent space” inside the ambient one — “for some reason this class, and maybe all abstract classes, keep identifying things with each other.” The second description is the one from Assignment 3, Problem 2: think of a curve in $S$ composed with the inclusion as a curve in $M$, and take its velocity there.

> [!definition] Definition §35.3: Conormal Space
> Let $S \subseteq M$ be a regular submanifold and $p \in S$. The **conormal space** of $S$ at $p$ is
>
> $$
> N_pS = \{\, \xi \in T_p^*M : \xi(v) = 0 \text{ for all } v \in \iota_{*p}(T_pS) \,\},
> $$
>
> the covectors at $p$ that vanish on the tangent space of $S$ — the annihilator of $T_pS$ in $T_p^*M$.

^def-35-3

> [!remark]- Connections
> - The annihilator of a subspace: [[§12 Duality#^ladr-3-121|LADR 3.121]].

> [!theorem] Proposition §35.5: A Basis of the Conormal Space
> In an adapted chart at $p$, $N_pS$ has basis $dx^{m-k+1}|_p, \ldots, dx^m|_p$. In particular $\dim N_pS = k$, the codimension of $S$.

^prop-35-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Write $\xi = \sum_j \xi_j\, dx^j|_p$ in the dual basis (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), so that $\xi(\partial/\partial x^i|_p) = \xi_i$. By Proposition [[§35 Regular Submanifolds#^prop-35-4|§35.4]], $\xi$ vanishes on $\iota_{\ast p}(T_pS)$ if and only if $\xi_i = 0$ for all $i \le m - k$. So $N_pS$ is spanned by the $dx^j|_p$ with $j > m - k$, which are linearly independent as part of a basis.

^pf-35-5

*Uses:* [[§35 Regular Submanifolds#^def-35-3|Def. §35.3]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§32 The Cotangent Space#^lem-32-2|§32.2]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]]

> [!remark]- Connections
> - The dimension count in general: [[§12 Duality#^ladr-3-125|LADR 3.125]] ($\dim U^0 = \dim V - \dim U$).

> [!remark] Remark: No Normal Vectors Without a Metric
> “We don't have normal vectors, because we don't have a metric … There is no notion of orthogonality, but there is an intrinsic” definition: the conormal space. “If we had a metric, [an] inner product on $T_pM$, we could identify $T^*_pM$ with $T_pM$, and this would be the normal space.” Uribe added that he regards the cotangent side as “actually more natural” than the tangent side — “that's where Hamiltonian mechanics takes place.”

^rem-35-1

![[m591-15-4.svg]]
*How to draw a conormal covector. Without a metric, a covector $\xi$ on $T_pM$ is drawn by its level lines $\{\xi = \text{const}\}$. For $\xi \in N_pS$ the level line $\xi = 0$ contains $T_pS$, so all of its level lines run* parallel *to $T_pS$ (left). Only once an inner product is chosen does $\xi$ become a vector, perpendicular to its level lines, and $N_pS$ becomes the normal line $(T_pS)^\perp$ (right). The board, and page 33 of the handwritten notes, draw $N_pS$ as a line perpendicular to $T_pS$: that is the right-hand, metric picture.*

> [!remark]- Connections
> - With an inner product: the orthogonal complement [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]], and the identification of covectors with vectors, [[Riesz representation theorem|LADR 6.42]].
> - The same point for gradients: [[§32 The Cotangent Space#^rem-32-2|Differential — Not Gradient]].

## Regular Submanifolds of Euclidean Space

*Not from lecture: the link back to the geometric stage.* Inside a Euclidean space, [[§20 Manifolds in Euclidean Space|§20]] described a manifold $X \subseteq \mathbb{R}^{n+k}$ near a point in three ways — externally, by equations ([[§20 Manifolds in Euclidean Space#^def-20-1|Definition §20.1]]); internally, by a parametrization ([[§20 Manifolds in Euclidean Space#^def-20-2|Definition §20.2]]); and as a graph — and [[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]] showed that they agree. [[§35 Regular Submanifolds#^def-35-1|Definition §35.1]] adds a fourth, the *slice* description: a chart of the ambient space in which $X$ is a coordinate plane. The fourth agrees with the other three, so in $\mathbb{R}^{n+k}$ the submanifolds of codimension $k$ are exactly the manifolds of [[§20 Manifolds in Euclidean Space|§20]], and Definition §35.1 is their description made intrinsic to the ambient manifold.

> [!theorem] Proposition §35.6: Regular Submanifolds of $\mathbb{R}^{n+k}$: The Fourth Description
> Let $X \subseteq \mathbb{R}^{n+k}$ and $p \in X$. The following are equivalent:
> 1. near $p$, $X$ is described [[§20 Manifolds in Euclidean Space#^def-20-1|externally]] ([[§20 Manifolds in Euclidean Space#^def-20-1|Definition §20.1]]) — equivalently, [[§20 Manifolds in Euclidean Space#^def-20-2|internally]] or as a graph ([[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]]);
> 2. *(slice)* there is a smooth chart $(U, \varphi = (x_a, x_b))$ of $\mathbb{R}^{n+k}$ with $p \in U$, $x_a$ its first $n$ and $x_b$ its last $k$ components, such that $U \cap X = \{\, q \in U : x_b(q) = \vec 0 \,\}$, that is, a chart [[§35 Regular Submanifolds#^def-35-2|adapted]] to $X$ ([[§35 Regular Submanifolds#^def-35-2|Definition §35.2]]).
>
> In particular $X$ is a [[§35 Regular Submanifolds#^def-35-1|regular submanifold]] of $\mathbb{R}^{n+k}$ of codimension $k$ ([[§35 Regular Submanifolds#^def-35-1|Definition §35.1]]) if and only if every point of $X$ has the descriptions of [[§20 Manifolds in Euclidean Space|§20]].

^prop-35-6

> [!proof]+ Proof
> *(Not from lecture.)* *Graph $\Rightarrow$ slice.* Permuting coordinates is a linear isomorphism, so we may assume $X \cap (V \times V') = \{(x, h(x)) : x \in V\}$ as in (G) of [[§20 Manifolds in Euclidean Space#^thm-20-1|Theorem §20.1]]. Let $U = V \times V'$ and $\Phi(x, y) = (x,\, y - h(x))$. Then $\Phi$ is smooth and injective, its image $\{(x, z) : x \in V,\ z + h(x) \in V'\}$ is open, and its inverse $(x, z) \mapsto (x, z + h(x))$ is smooth; so $\Phi$ is a diffeomorphism of $U$ onto an open set, hence a smooth chart of $\mathbb{R}^{n+k}$ (its transition maps with the identity chart are $\Phi$ and $\Phi^{-1}$). Its last $k$ components $y - h(x)$ vanish exactly on $X \cap U$.
>
> *Slice $\Rightarrow$ external.* Let $F = x_b : U \to \mathbb{R}^k$, the last $k$ components of $\varphi$; it is smooth. A chart is a diffeomorphism onto its image ([[§28 Derivations and the Abstract Tangent Space#^prop-28-9|Proposition §28.9]]), so the Jacobian $\varphi'(q)$ is invertible at every $q \in U$, and its last $k$ rows, which form $F'(q)$, are linearly independent. Hence $F'(q)$ has rank $k$ everywhere, $\vec 0$ is a regular value of $F$, and $X \cap U = F^{-1}(\vec 0)$: the external description with $W = U$.
>
> The final statement follows, since Definition §35.1 asks for (2) at every point of $X$.

^pf-35-6

*Uses:* [[§20 Manifolds in Euclidean Space#^def-20-1|Def. §20.1]], [[§20 Manifolds in Euclidean Space#^def-20-2|Def. §20.2]], [[§20 Manifolds in Euclidean Space#^thm-20-1|§20.1]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]

![[m591-35-3.svg]]
*Straightening a graph. The map $\Phi(x, y) = (x, y - h(x))$ keeps $x$ and measures the height above the graph; it carries the graph $X$ to the slice $z = 0$, and the parallel graphs $y = h(x) + c$ to the slices $z = c$. This is the passage from the graph charts of [[§20 Manifolds in Euclidean Space#^prop-20-2|Proposition §20.2]], which flatten $X$ alone, to an adapted chart, which straightens a whole neighbourhood of $X$ in the ambient space.*

For the unit sphere $S^2 \subseteq \mathbb{R}^3$ near the north pole, the graph is $z = \sqrt{1 - x^2 - y^2}$, and $(x, y, z) \mapsto (x, y, z - \sqrt{1 - x^2 - y^2})$ is an adapted chart; so is $(x, y, z) \mapsto (x, y, x^2 + y^2 + z^2 - 1)$ near any point with $z \neq 0$, whose last coordinate is the defining function of the external description.

> [!remark] Remark: The Tangent Spaces Match
> *(Not from lecture.)* The two tangent spaces of the geometric and the abstract stage correspond as well. Externally, $T^{\mathrm{geo}}_pX = \ker F'(p)$ ([[§25 The Geometric Tangent Space#^thm-25-3|Theorem §25.3]]). In the slice chart of [[§35 Regular Submanifolds#^prop-35-6|Proposition §35.6]], with $F = x_b$, this kernel is the set of vectors on which the differentials of the last $k$ coordinates vanish, the span of the first $n$ coordinate directions; and that span is $\iota_{\ast p}(T_pX)$ ([[§35 Regular Submanifolds#^prop-35-4|Proposition §35.4]]). [[§35 Regular Submanifolds#^prop-35-9|Proposition §35.9]] below makes the identification precise, together with the agreement of the two smooth structures.

^rem-35-2

## The Regular Value Theorem for Manifolds

*Lecture 12. “And now we go back to submersions” — to “[the] wonderful version of the regular value theorem.”*

> [!theorem] Theorem §35.7: The Regular Value Theorem for Manifolds
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$, and let $q \in N$ be a regular value of $F$ (Definition [[§34 Submersions#^def-34-4|§34.4]]). Then $S = F^{-1}(q)$ is a regular submanifold of $M$ of codimension $n$ (possibly empty), so $\dim S = m - n$, and for every $p \in S$
>
> $$
> \iota_{*p}(T_pS) = \ker F_{*p} .
> $$
>
> *Lee: Corollary 5.14 and Proposition 5.38*

^thm-35-7

> [!proof]+ Proof
> *$S$ is a submanifold (Lecture 12).* We check the definition at each $p \in S$: we need an adapted chart at $p$. By assumption $F$ is a submersion at $p$, so the normal form (Theorem [[§34 Submersions#^thm-34-4|§34.4]]) gives charts $(U, \hat\varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q = F(p)$, with $F(U) \subseteq V$ and $\tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^n)$. What are the equations of $S \cap U$ in these coordinates? For $q' \in U$,
>
> $$
> \begin{aligned}
> q' \in S &\iff F(q') = q \iff \psi\big(F(q')\big) = \psi(q) \\
> &\iff \tilde F\big(\hat\varphi(q')\big) = \psi(q) \iff \big(x^1(q'), \ldots, x^n(q')\big) = \big(y^1(q), \ldots, y^n(q)\big).
> \end{aligned}
> $$
>
> “These are not of the type $x_b = 0$, but of the type $x_a$ equals a constant”: the first $n$ coordinates equal a constant vector. By the observations after the definition (Proposition [[§35 Regular Submanifolds#^prop-35-1|§35.1]]) — any constant, and any $n$ of the coordinates — $S$ has an adapted chart at $p$, of codimension $n$. *(Completion.)* The second equivalence uses that $\psi$ is injective on $V$, which contains $F(q')$; the last is the normal form.
>
> *The tangent space.* *(Completion. In lecture: “I won't bother checking the kernel thing, because everything really reduces to the Euclidean [case].”)* The composite $F \circ \iota : S \to N$ is constant, with value $q$, and the pushforward along a constant map is zero (as in the proof of Theorem [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]]); so $F_{\ast p} \circ \iota_{\ast p} = 0$ and $\iota_{\ast p}(T_pS) \subseteq \ker F_{\ast p}$. The left side has dimension $m - n$, since $\iota_{\ast p}$ is injective (Proposition [[§35 Regular Submanifolds#^prop-35-4|§35.4]]); the right side has dimension $m - n$ by rank–nullity, since $F_{\ast p}$ is onto (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]). A subspace of the same finite dimension is everything, so the two are equal. This is the argument of Lecture 8 for $T^{\mathrm{geo}}_pM = \ker F'(p)$ (Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]), one level up.

^pf-35-7

*Uses:* [[§34 Submersions#^def-34-3|Def. §34.3]], [[§34 Submersions#^def-34-4|Def. §34.4]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§34 Submersions#^thm-34-4|§34.4]], [[§35 Regular Submanifolds#^prop-35-1|§35.1]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§31 Tangent Vectors as Velocities of Curves#^thm-31-4|§31.4]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[Fundamental theorem of linear maps|LADR 3.21]]

![[m591-15-5.svg]]
*The proof in one square, as on the board. In the normal-form charts $\tilde F$ is the projection onto the first $n$ coordinates, so the level set $S \cap U = F^{-1}(q) \cap U$ is carried by $\hat\varphi$ onto a fibre of a projection: the slice where the first $n$ coordinates equal $\psi(q)$.*

> [!remark]- Connections
> - The earlier regular value theorems it contains: [[§7 The Regular Value Theorem#^thm-7-3|§7.3]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§30 The Differential in Coordinates#^cor-30-8|§30.8]] (see the remark below); the tangent-space statement generalizes [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]].
> - Constraint sets $\{g_1 = c_1, \ldots, g_k = c_k\}$ in multivariable analysis: [[§17 Optimization and Lagrange Multipliers#^thm-17-3|452 §17.3]] (Lagrange multipliers with several constraints).
> - Fibres of submersions that are all copies of one fibre: [[§36 Fibrations#^def-36-1|fibrations, Def. §36.1]].

**Transcription note.** Page 33 of the handwritten notes states the theorem for “$q \in M$ a regular value”; the regular value lies in the target, $q \in N$.

> [!theorem] Corollary §35.8: Fibres of Submersions Are Regular Submanifolds
> If $F : M \to N$ is a submersion, then every fibre $F^{-1}(q)$, $q \in N$, is a regular submanifold of $M$ of codimension $n$ — “they could be empty, some of them.”

^cor-35-8

> [!proof]+ Proof
> Every $q \in N$ is a regular value: every point of $F^{-1}(q)$ is a regular point, and if $F^{-1}(q)$ is empty the condition holds vacuously. Apply Theorem [[§35 Regular Submanifolds#^thm-35-7|§35.7]].

^pf-35-8

*Uses:* [[§34 Submersions#^def-34-3|Def. §34.3]], [[§34 Submersions#^def-34-4|Def. §34.4]], [[§35 Regular Submanifolds#^thm-35-7|§35.7]]

> [!remark] Remark: The Regular Value Theorems — Old and New
> The notes now contain the regular value theorem in five forms. They are one idea met at increasing generality, not competing statements.
>
> | **Where** | **Setting** | **Conclusion** | **Role now** |
> |---|---|---|---|
> | Thm. [[§7 The Regular Value Theorem#^thm-7-3\|§7.3]], Cor. [[§7 The Regular Value Theorem#^cor-7-4\|§7.4]] | $F : W \to \mathbb{R}^k$, $W \subseteq \mathbb{R}^{n+k}$ open | topological manifold | the first version (Lecture 3); Chapter 2 needs it |
> | Prop. [[§20 Manifolds in Euclidean Space#^prop-20-2\|§20.2]] | the same | smooth manifold, by graph charts | the Euclidean case (Lecture 6) |
> | Prop. [[§30 The Differential in Coordinates#^prop-30-7\|§30.7]] | $F : M \to N$, level set inside one chart | regular for $F$ iff for $\tilde F$ | a computational tool |
> | Cor. [[§30 The Differential in Coordinates#^cor-30-8\|§30.8]] | $F : M \to N$ | topological manifold | subsumed; a more elementary proof |
> | Thm. [[§35 Regular Submanifolds#^thm-35-7\|§35.7]] | $F : M \to N$ | submanifold, with $\iota_{*p}(T_pS) = \ker F_{*p}$ | the general theorem (Lecture 12) |
>
> The general theorem contains the others: taking $M$ an open subset of Euclidean space recovers the first two. Its proof goes through the normal form, which rests on the inverse function theorem and not on [[§7 The Regular Value Theorem|§7]], so nothing is circular. The next proposition shows that the old and new versions give the same smooth structure and the same tangent spaces.

^rem-35-3

> [!theorem] Proposition §35.9: The Old and New Versions Agree
> Let $W \subseteq \mathbb{R}^{n+k}$ be open, $F : W \to \mathbb{R}^k$ smooth, $c$ a regular value, and $S = F^{-1}(c)$.
> 1. The smooth structure on $S$ given by the graph charts (Proposition [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]]) is the induced structure of $S$ as a regular submanifold of $W$ (Theorem [[§35 Regular Submanifolds#^thm-35-7|§35.7]]).
> 2. In the setting of Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], under the identification $T_pW = \mathbb{R}^{n+k}$ of Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], the subspace $\iota_{*p}(T_pS)$ is $T^{\mathrm{geo}}_pS = \ker F'(p)$.

^prop-35-9

> [!proof]+ Proof
> *(Not from lecture; filled in.)* First, $c$ is a regular value in both senses, since the matrix of $F_{\ast p}$ in the standard coordinates is $F'(p)$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]).
>
> (1) Let $p \in S$. As in the construction of the graph charts, after reordering the coordinates write the points of $\mathbb{R}^{n+k}$ as $(x, y) \in \mathbb{R}^n \times \mathbb{R}^k$ with $\partial F/\partial y\,(p)$ invertible, so that the graph chart near $p$ is $(x, y) \mapsto x$ on $S$. Let $\Phi(x, y) = (x, F(x, y) - c)$. Its Jacobian at $p$ is $\begin{pmatrix} I_n & 0 \\ \partial F/\partial x & \partial F/\partial y \end{pmatrix}$, which is invertible, so by the inverse function theorem $\Phi$ restricts to a diffeomorphism of an open $U \ni p$ onto an open set, and by Lemma [[§34 Submersions#^lem-34-3|§34.3]] it is a smooth chart of $W$. Its last $k$ components are $F - c$, which vanish exactly on $S \cap U$, so $\Phi$ is adapted, and its induced chart is $\Phi_S = x|_{S \cap U}$: the graph chart. So near each of its points, every graph chart is an induced chart. Induced charts are pairwise compatible, and smoothness of a transition map is local, so every graph chart is compatible with every induced chart, and the two atlases determine the same maximal atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> (2) Let $v \in T^{\mathrm{geo}}_pS$, and let $\gamma$ be the lifted line of Definition [[§25 The Geometric Tangent Space#^def-25-4|§25.4]], a curve in $S$ with $\gamma(0) = p$ and $\gamma'(0) = v$, so that $D_v = D_\gamma$. By Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], $\iota_{*p}D_v = D_{\iota \circ \gamma}$, the derivation $g \mapsto (g \circ \gamma)'(0) = \nabla g(p) \cdot v$ at $p$ — the directional derivative in the direction $v$, which is $v$ under Corollary [[§30 The Differential in Coordinates#^cor-30-6|§30.6]]. Since $v \mapsto D_v$ is onto $T_pS$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]]), $\iota_{*p}(T_pS) = T^{\mathrm{geo}}_pS$, and $T^{\mathrm{geo}}_pS = \ker F'(p)$ by Theorem [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]]. This matches $\ker F_{*p}$ in Theorem [[§35 Regular Submanifolds#^thm-35-7|§35.7]], $F_{*p}$ being $F'(p)$.

^pf-35-9

*Uses:* [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§20 Manifolds in Euclidean Space#^prop-20-2|§20.2]], [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[§34 Submersions#^lem-34-3|§34.3]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§35 Regular Submanifolds#^prop-35-2|§35.2]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§25 The Geometric Tangent Space#^def-25-4|Def. §25.4]], [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]], [[§30 The Differential in Coordinates#^cor-30-6|§30.6]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-6|§29.6]], [[§25 The Geometric Tangent Space#^thm-25-3|§25.3]], [[§35 Regular Submanifolds#^thm-35-7|§35.7]], [[Directional Derivative Formula|452 §9.1]], [[Multivariable Chain Rule|452 §12.2]]
