---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 39
tags: [differentiable-manifolds, math591]
---
← [[§38 Fibrations]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§40 Embeddings]] →

*Stage: maps — The maps with injective differentials: locally inclusions, globally more subtle.*

*References: Lee Ch. 4. Lecture 13.*

The third special type of map, dual to the submersions of [[§36 Submersions|§36]]: the differential is injective instead of surjective, and the local model is an inclusion instead of a projection.

## Immersions

*Lecture 13. “Next class of special maps”: Lecture 10 listed immersions among the special types of map, and the definition has been on record since ([[§36 Submersions#^def-36-2|Definition §36.2]]); Lecture 13 is where they were first treated seriously, after the tangent bundle ([[§47 The Tangent Bundle|§47]]).*

> [!definition] Definition §39.1: Immersions
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$. $F$ is an **immersion at $p$** if $F_{\ast p} : T_pM \to T_{F(p)}N$ is injective — which forces $m \le n$, since an injective linear map cannot lower dimension — and an **immersion** if it is an immersion at every point. “Go from a lower-dimensional manifold to a bigger one.”
>
> *Lee: Ch. 4, Immersions*

^def-39-1

> [!remark]- Connections
> - The earlier definition, stated with submersions: [[§36 Submersions#^def-36-2|Def. §36.2]]; the dimension constraint there: [[§36 Submersions#^prop-36-1|§36.1]].
> - An injective linear map cannot lower dimension: [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]].
> - The first examples are the regular parametrized surfaces of 452, whose $3 \times 2$ Jacobian has rank 2: [[§31 Surface Integrals#^def-31-3|452 Def. §31.3]].

> [!theorem] Theorem §39.1: Local Normal Form for Immersions
> Let $F : M \to N$ be an immersion at $p$, with $\dim M = m \le n = \dim N$. Then there are charts $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U) \subseteq V$ in which the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$ is the standard inclusion:
>
> $$
> \tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^m, \underbrace{0, \ldots, 0}_{n - m}) .
> $$
>
> *Lee: Theorem 4.12, the rank theorem*

^thm-39-1

> [!proof]+ Proof (Lecture 14)
> The steps are the lecture's, in the lecture's order; sentences marked *(Completion.)* fill in details. The first half runs as for submersions (Theorem [[§36 Submersions#^thm-36-4|§36.4]]); the new step is that here the chart on $N$ changes too.
>
> *1. Start with any coordinates.* Take charts $(U_0, \varphi_0 = (x^1, \ldots, x^m))$ at $p$ and $(V_0, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U_0) \subseteq V_0$, shrinking $U_0$ if necessary, and write $F^j = y^j \circ F$. *(Completion.)* Shrinking means: replace $U_0$ by $U_0 \cap F^{-1}(V_0)$, which is open because $F$ is continuous and contains $p$; the restriction of a smooth chart to an open subset is again a smooth chart (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1); its transition maps are restrictions of the old ones). The components $F^j : U_0 \to \mathbb{R}$ are smooth, since $F^j \circ \varphi_0^{-1}$ is the $j$-th component of the smooth coordinate representation $\psi \circ F \circ \varphi_0^{-1}$ (Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]).
>
> *2. The Jacobian is taller than wide.* $J = \big[\partial F^j/\partial x^i(p)\big]$ is the matrix of $F_{\ast p}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]): $n$ rows and $m$ columns, “fewer columns than rows.” $F_{\ast p}$ is injective, so $J$ has rank $m$: it has $m$ linearly independent row vectors. *(Completion.)* By Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], $F_{\ast p}(\partial/\partial x^i|_p) = \sum_j \partial F^j/\partial x^i(p)\, \partial/\partial y^j|_{F(p)}$, so the $i$-th column of $J$ holds the coordinates of $F_{\ast p}(\partial/\partial x^i|_p)$, and $J$ is the matrix of $F_{\ast p}$ in the coordinate bases (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)). Since $F_{\ast p}$ is injective, $\ker F_{\ast p} = 0$, and rank–nullity (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](1)) gives $\operatorname{rank} F_{\ast p} = \dim T_pM = m$. So $J$ has rank $m$, and so does its transpose (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](3)), whose columns are the rows of $J$: among the $n$ rows of $J$ there are $m$ linearly independent ones.
>
> *3. Relabel the $y$'s.* Reordering the coordinates of $\psi$ — again a smooth chart, as in step 4 of the proof of Theorem [[§36 Submersions#^thm-36-4|§36.4]] — we may assume the top $m \times m$ block $A$ of $J$ is invertible. *(Completion.)* Let rows $j_1, \ldots, j_m$ of $J$ be linearly independent, and let $P : \mathbb{R}^n \to \mathbb{R}^n$ be a permutation of coordinates moving positions $j_1, \ldots, j_m$ to positions $1, \ldots, m$. Replacing $\psi$ by $P \circ \psi$ lists the same coordinate functions $y^j$ in a new order; so it lists the components $F^j = y^j \circ F$, and hence the rows of $J$, in the same new order. Afterwards rows $1, \ldots, m$ of $J$ are linearly independent, so the top block $A$, which consists of them, is an $m \times m$ matrix of rank $m$, that is, invertible. We keep the names $\psi = (y^1, \ldots, y^n)$, $F^j$ and $J$ for the reordered chart, components and matrix.
>
> *4. The first $m$ components of $F$ are coordinates on $M$.* $A$ is the Jacobian at $p$, in the $x$-coordinates, of the map $U_0 \to \mathbb{R}^m$ that sends $q$ to the first $m$ components $\big(F^1(q), \ldots, F^m(q)\big)$ (Proposition [[§30 The Differential in Coordinates#^prop-30-1|§30.1]]). *(Completion.)* Read in the $x$-coordinates, this map is $\Phi = (F^1, \ldots, F^m) \circ \varphi_0^{-1} : \varphi_0(U_0) \to \mathbb{R}^m$, with components $F^j \circ \varphi_0^{-1}$. By Definition [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|§29.2]], $\partial F^j/\partial x^i(p) = \partial (F^j \circ \varphi_0^{-1})/\partial r^i\big(\varphi_0(p)\big)$, so
>
> $$
> \Phi'\big(\varphi_0(p)\big) = \Big[\frac{\partial (F^j \circ \varphi_0^{-1})}{\partial r^i}\big(\varphi_0(p)\big)\Big]_{1 \le j, i \le m} = \Big[\frac{\partial F^j}{\partial x^i}(p)\Big]_{1 \le j, i \le m} = A .
> $$
>
> It is invertible, so by the inverse function theorem (Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]]) — “I always say implicit, but in this case I want the inverse function theorem” — this map is a local diffeomorphism near $p$, and, possibly after shrinking $U_0$ to some $U \ni p$, it is a chart:
>
> $$
> \tilde\varphi = \big(F^1, \ldots, F^m\big)\big|_U : U \longrightarrow \tilde\varphi(U) \subseteq \mathbb{R}^m .
> $$
>
> *(Completion.)* As in step 8 of the proof of Theorem [[§36 Submersions#^thm-36-4|§36.4]]: the inverse function theorem gives an open $W \ni \varphi_0(p)$ on which $\tilde\varphi \circ \varphi_0^{-1}$ is a diffeomorphism onto an open set; put $U = \varphi_0^{-1}(W)$; then $\tilde\varphi$ maps $U$ diffeomorphically onto an open set, and is a chart by Lemma [[§36 Submersions#^lem-36-3|§36.3]]. In detail: $\tilde\varphi \circ \varphi_0^{-1} = \Phi$, and Theorem [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], applied to $\Phi$ at $a = \varphi_0(p)$, gives open sets $W \ni \varphi_0(p)$ in $\varphi_0(U_0)$ and $W' \ni \Phi(\varphi_0(p))$ in $\mathbb{R}^m$ with $\Phi(W) = W'$ and $\Phi|_W : W \to W'$ bijective with smooth inverse. The set $U = \varphi_0^{-1}(W)$ is open in $M$ and contains $p$, and on it
>
> $$
> \tilde\varphi = \Phi|_W \circ \varphi_0|_U ,
> $$
>
> a composite of the diffeomorphism $\varphi_0|_U : U \to W$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]) and the diffeomorphism $\Phi|_W : W \to W'$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]]). So $\tilde\varphi$ is a diffeomorphism of $U$ onto the open set $\tilde\varphi(U) = W'$ (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]), and $(U, \tilde\varphi)$ is a smooth chart at $p$ by Lemma [[§36 Submersions#^lem-36-3|§36.3]]. Also $F(U) \subseteq F(U_0) \subseteq V_0$.
>
> *5. In the new chart, $F$ is a graph.* Let $\hat F = \psi \circ F \circ \tilde\varphi^{-1} : \tilde\varphi(U) \to \psi(V_0)$, defined because $F(U) \subseteq V_0$. By the definition of $\tilde\varphi$, the first $m$ components of $\hat F(r)$ are $F^i(\tilde\varphi^{-1}(r)) = r^i$. *(Completion.)* Fix $r \in \tilde\varphi(U)$ and put $u = \tilde\varphi^{-1}(r) \in U$, so that $\big(F^1(u), \ldots, F^m(u)\big) = \tilde\varphi(u) = r$. The $j$-th component of $\hat F(r) = \psi(F(u))$ is $y^j(F(u)) = F^j(u)$: for $j = i \le m$ it is $r^i$, and for $j = m + k$ it is $F^{m+k}(\tilde\varphi^{-1}(r))$. So
>
> $$
> \hat F(r) = \big(r, \ G^1(r), \ldots, G^{n-m}(r)\big), \qquad G^k = F^{m+k} \circ \tilde\varphi^{-1} ,
> $$
>
> with $G = (G^1, \ldots, G^{n-m})$ smooth on $\tilde\varphi(U)$: $G^k = r^{m+k} \circ \hat F$ is a component of $\hat F$, the coordinate representation of the smooth map $F$ in smooth charts (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]). “I don't get zeros yet. I get something”: $\hat F$ is the graph of $G$ over $\tilde\varphi(U)$.
>
> *6. Straighten the graph.* “You can always straighten out a graph to make it zero.” Define new coordinates on $N$ by keeping the first $m$ and shifting the rest: “I always mess up my indices \ldots so I'm going to cheat”
>
> $$
> \tilde y^i = y^i \quad (1 \le i \le m), \qquad \tilde y^i = y^i - G^{i-m}\big(y^1, \ldots, y^m\big) \quad (m+1 \le i \le n),
> $$
>
> and $\tilde\psi = (\tilde y^1, \ldots, \tilde y^n)$. *(Completion.)* This is $\tilde\psi = \Sigma \circ \psi$, where $\Sigma(y_a, y_b) = \big(y_a, \, y_b - G(y_a)\big)$ for $y_a = (y^1, \ldots, y^m)$ and $y_b = (y^{m+1}, \ldots, y^n)$: the components of $\Sigma \circ \psi$ are exactly the $\tilde y^i$ above. $\Sigma$ is defined on $\tilde\varphi(U) \times \mathbb{R}^{n-m}$, and is a diffeomorphism of that open set onto itself, with inverse $(y_a, z) \mapsto (y_a, z + G(y_a))$. In detail: $\tilde\varphi(U) \times \mathbb{R}^{n-m}$ is open in $\mathbb{R}^n$, a product of open sets; $\Sigma$ and the proposed inverse both leave the first block $y_a$ unchanged, so both map this set into itself; the two composites are the identity, since $\big(y_a, (y_b - G(y_a)) + G(y_a)\big) = (y_a, y_b)$ and $\big(y_a, (z + G(y_a)) - G(y_a)\big) = (y_a, z)$; and both are smooth, their components being $y_a$ and $y_b \mp G(y_a)$ with $G$ smooth (step 5). So on the open set $V = \psi^{-1}\big(\tilde\varphi(U) \times \mathbb{R}^{n-m}\big) \cap V_0$ the map $\tilde\psi$ is a diffeomorphism onto an open subset of $\mathbb{R}^n$, hence a chart (Lemma [[§36 Submersions#^lem-36-3|§36.3]]). In detail: $V$ is open, the preimage of an open set under the continuous $\psi$. On $V$, $\tilde\psi = \Sigma \circ \psi|_V$, where $\psi|_V$ is a diffeomorphism of $V$ onto the open set $\psi(V) = \psi(V_0) \cap \big(\tilde\varphi(U) \times \mathbb{R}^{n-m}\big)$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], for the restricted chart), and $\Sigma$ restricts to a diffeomorphism of $\psi(V)$ onto $\Sigma(\psi(V))$, which is open because $\Sigma$ is a homeomorphism of the open set $\tilde\varphi(U) \times \mathbb{R}^{n-m}$ onto itself (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](3)). And $F(U) \subseteq V$, because the first $m$ coordinates of $\psi(F(u))$ are $\tilde\varphi(u) \in \tilde\varphi(U)$: by step 5, $\psi(F(u)) = \hat F(\tilde\varphi(u)) = \big(\tilde\varphi(u), G(\tilde\varphi(u))\big)$, and $F(u) \in V_0$. In particular $F(p) \in V$.
>
> *7. These do the job.* “We're not changing the first $m$ — we already have the inclusion here — but we're fixing the other ones.” *(Completion.)* For $r \in \tilde\varphi(U)$,
>
> $$
> \tilde\psi \circ F \circ \tilde\varphi^{-1}(r) = \Sigma\big(\hat F(r)\big) = \Sigma\big(r, G(r)\big) = \big(r, \, G(r) - G(r)\big) = (r, \vec 0) .
> $$
>
> The first equality is $\tilde\psi = \Sigma \circ \psi$ on $V \supseteq F(U)$ (step 6) together with $\hat F = \psi \circ F \circ \tilde\varphi^{-1}$ (step 5); the second is the graph form of $\hat F$ (step 5); the third is the definition of $\Sigma$. So in the charts $(U, \tilde\varphi)$ and $(V, \tilde\psi)$, $F$ is the standard inclusion: these are the charts $(U, \varphi)$ and $(V, \psi)$ of the statement.

^pf-39-1

*Uses:* [[§39 Immersions#^def-39-1|Def. §39.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-1|Def. §19.1]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§36 Submersions#^thm-36-4|§36.4]] (steps 4 and 8 of its proof), [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§35 Local Diffeomorphisms#^thm-35-1|§35.1]], [[§35 Local Diffeomorphisms#^def-35-1|Def. §35.1]], [[§36 Submersions#^lem-36-3|§36.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§9 Matrices#^ladr-3-57|LADR 3.57]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]], [[§29 Coordinate Derivations and the Basis Theorem#^def-29-2|Def. §29.2]], [[§19 Smooth Functions and Smooth Maps#^prop-19-3|§19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]]

![[m591-32-1.svg]]
*The two changes of chart in one diagram, as on the board. On $M$, the chart $\tilde\varphi$ is made from the first $m$ components of $F$, which turns $F$ into the graph $\hat F$; on $N$, the straightening $\Sigma$ removes the graph, so that $\tilde F = \Sigma \circ \hat F$ is the inclusion.*

![[m591-32-2.svg]]
*Step 6 in a picture ($m = n - m = 1$). Before: the image of $\hat F$ is the graph $y_b = G(y_a)$ over $\tilde\varphi(U)$. After: each point is moved straight down by $G(y_a)$, and the graph becomes a piece of the $y_a$-axis — an open interval, over the same $\tilde\varphi(U)$.*

**Transcription note.** Page 38 of the handwritten notes begins the proof with “start with any coordinates with $\varphi(U) \subset V$”; the condition is $F(U) \subseteq V$. In the lecture the shifted coordinates were first spoken as $G^{i-m}(y^1, \ldots, y^n)$; the arguments are the first $m$ coordinates, $y^1, \ldots, y^m$, as on page 38.

![[m591-18-1.svg]]
*The immersion normal form, as on the board: the mirror image of the submersion normal form ([[§36 Submersions#^thm-36-4|Theorem §36.4]]). There $\tilde F$ forgot the last $m - n$ coordinates; here it appends $n - m$ zeros.*

*Status.* Stated in Lecture 13 — “a little bit technical … better do it fresh at the beginning of the class” — and proved at the start of Lecture 14, above. It is the counterpart of [[§36 Submersions#^thm-36-4|Theorem §36.4]]: there $F$ was locally a projection, here it is locally an inclusion.

> [!remark]- Connections
> - The mirror-image result for submersions: [[§36 Submersions#^thm-36-4|Local Normal Form for Submersions, §36.4]]; the case $m = n$: [[§35 Local Diffeomorphisms#^thm-35-2|§35.2]], via the [[§35 Local Diffeomorphisms#^thm-35-1|Inverse Function Theorem, §35.1]] ([[Inverse Function Theorem (several variables)|452 §16.2]]).

What the image of an immersion looks like — locally a submanifold, globally not necessarily — is taken up next, in [[§39 Immersions#Images of Immersions|Images of Immersions]].

## Images of Immersions

*Lecture 13, continuing [[§39 Immersions#Immersions|Immersions]]. What the image of an immersion looks like. These results use submanifolds ([[§37 Regular Submanifolds|§37]]).*

> [!theorem] Corollary §39.2: The Local Image of an Immersion
> In the charts of [[§39 Immersions#^thm-39-1|Theorem §39.1]], $F|_U$ is injective and $F(U)$ is a regular submanifold of $N$ of codimension $n - m$.

^cor-39-2

> [!proof]+ Proof
> *(Lecture 13 gave the idea — the image of $\tilde F$ is an open set times zeros, “and so since what happens below happens upstairs too”, $F(U)$ is a submanifold — adding “I'm feeling a little bit uneasy, because I want to say after restriction, possibly after restricting $U$.” Completed here: shrinking $V$ instead of $U$ settles it.)* Let $(U, \varphi)$ and $(V, \psi = (y^1, \ldots, y^n))$ be the charts of Theorem [[§39 Immersions#^thm-39-1|§39.1]]: $F(U) \subseteq V$ and $\psi\big(F(\varphi^{-1}(r))\big) = \tilde F(r) = (r, \vec 0)$ for $r \in \varphi(U)$. Putting $r = \varphi(u)$, this reads
>
> $$
> \psi\big(F(u)\big) = \big(\varphi(u), \vec 0\big) \qquad (u \in U).
> $$
>
> *$F|_U$ is injective.* $\tilde F$ is injective, so $F|_U$ is: if $F(u_1) = F(u_2)$ with $u_1, u_2 \in U$, then
>
> $$
> \big(\varphi(u_1), \vec 0\big) = \psi\big(F(u_1)\big) = \psi\big(F(u_2)\big) = \big(\varphi(u_2), \vec 0\big),
> $$
>
> so $\varphi(u_1) = \varphi(u_2)$, and $u_1 = u_2$ because $\varphi$ is injective.
>
> *The set $V'$.* Let
>
> $$
> V' = \big\{\, q \in V : \big(y^1(q), \ldots, y^m(q)\big) \in \varphi(U) \,\big\},
> $$
>
> open in $N$ because $\varphi(U)$ is open: with $\mathrm{pr} : \mathbb{R}^n \to \mathbb{R}^m$ the projection onto the first $m$ coordinates, $V' = (\mathrm{pr} \circ \psi)^{-1}\big(\varphi(U)\big)$, the preimage of an open set under the continuous map $\mathrm{pr} \circ \psi : V \to \mathbb{R}^m$, so $V'$ is open in $V$, hence in $N$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). And $V'$ contains $F(U)$ because $\psi(F(u)) = (\varphi(u), \vec 0)$: the first $m$ coordinates of $\psi(F(u))$ are $\varphi(u) \in \varphi(U)$.
>
> *The equations of $F(U)$.* We claim $F(U) = \{ q \in V' : y^{m+1}(q) = \cdots = y^n(q) = 0 \}$. The inclusion $\subseteq$ is clear: if $q = F(u)$, then $q \in V'$ as just shown, and $y^{m+1}(q), \ldots, y^n(q)$ are the last $n - m$ coordinates of $\psi(q) = (\varphi(u), \vec 0)$, all zero. Conversely, if $q \in V'$ has $\psi(q) = (r, \vec 0)$ with $r \in \varphi(U)$, then $\psi(q) = \tilde F(r) = \psi\big(F(\varphi^{-1}(r))\big)$, so $q = F(\varphi^{-1}(r))$ because $\psi$ is injective.
>
> *An adapted chart.* The restriction $(V', \psi|_{V'})$ is a smooth chart of $N$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)). Apply Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] with ambient manifold $N$ of dimension $n$, $S = F(U)$ and $k = n - m$, so that $x_b = (y^{m+1}, \ldots, y^n)$ are the last $k$ coordinates. Since $F(U) \subseteq V'$, the claim says $V' \cap F(U) = F(U) = \{ q \in V' : x_b(q) = \vec 0 \}$. So $(V', \psi|_{V'})$ is an adapted chart at every point of $F(U)$, and $F(U)$ is a submanifold of codimension $n - m$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]). No restriction of $U$ was needed: the worry was that $\psi(V) \cap (\mathbb{R}^m \times \{\vec 0\})$ might contain points not of the form $\tilde F(r)$ with $r \in \varphi(U)$, and passing to $V'$ removes exactly those.

^pf-39-2

*Uses:* [[§39 Immersions#^thm-39-1|§39.1]], [[§37 Regular Submanifolds#^def-37-1|Def. §37.1]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

> [!remark]- Connections
> - The global version needs a topological condition: [[§39 Immersions#^rem-39-1|Remark: Embeddings — Next Time]].
> - The global statement, for embeddings: [[§40 Embeddings#^thm-40-1|§40.1]].

“But the really interesting thing about these immersions is that globally it doesn't have to be the case”: the whole image of an immersion need not be a submanifold. There are two ways for this to fail.

> [!example] Example §39.1: An Immersion That Crosses Itself
> $\gamma : \mathbb{R} \to \mathbb{R}^2$, $\gamma(t) = (t^2 - 1, \ t^3 - t)$, is an immersion, but it is not injective, and its image is not a submanifold of $\mathbb{R}^2$: near the origin the image looks like an X.

^ex-39-1

> [!proof]+ Proof
> *(Lecture 13 drew a curve crossing itself and gave the argument below; the specific curve is filled in.)* Three things are claimed: $\gamma$ is an immersion, it is not injective, and its image is not a submanifold.
>
> *Immersion.* $\gamma'(t) = (2t, 3t^2 - 1)$ never vanishes — the first component vanishes only at $t = 0$, where the second is $-1$ — so $\gamma$ is an immersion. In detail: in the identity charts of $\mathbb{R}$ (coordinate $r$) and of $\mathbb{R}^2$ (coordinates $r^1, r^2$), Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] gives
>
> $$
> \gamma_{\ast t}\Big(\frac{\partial}{\partial r}\Big|_t\Big) = 2t\, \frac{\partial}{\partial r^1}\Big|_{\gamma(t)} + (3t^2 - 1)\, \frac{\partial}{\partial r^2}\Big|_{\gamma(t)} ,
> $$
>
> which is nonzero, because the coordinate derivations are linearly independent (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]) and the two coefficients do not both vanish. $T_t\mathbb{R}$ is spanned by $\partial/\partial r|_t$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]]), so a linear map on it that is nonzero on this vector has kernel $0$. Hence $\gamma_{\ast t}$ is injective for every $t$ (Definition [[§39 Immersions#^def-39-1|§39.1]]).
>
> *Not injective.* $\gamma(1) = (1 - 1, \ 1 - 1) = (0, 0)$ and $\gamma(-1) = (1 - 1, \ -1 + 1) = (0, 0)$, so $\gamma(1) = \gamma(-1) = (0, 0)$, and $\gamma$ is not injective.
>
> *Not a submanifold: the lecture's argument.* Near the origin the image consists of two arcs crossing transversally, one through $\gamma(-1)$ and one through $\gamma(1)$, with tangent directions $\gamma'(\mp 1) = (\mp 2, 2)$. “What is the proof? If you remove the point of intersection from an X, you get four connected components. If you remove a point from an interval, you get two.” This is the lecture's level of rigour: made precise, it compares small connected neighbourhoods of the crossing point in the image with those of a point of a $1$-manifold.
>
> *Not a submanifold: a complete argument.* *(Completion, by tangent spaces instead of connected components.)* Let $C = \gamma(\mathbb{R})$, and suppose that $C$ were a regular submanifold of $\mathbb{R}^2$ of some codimension $k$ (Definition [[§37 Regular Submanifolds#^def-37-1|§37.1]]), with its induced structure (Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]). By the display above at $t = \pm 1$,
>
> $$
> \gamma_{\ast1}\Big(\frac{\partial}{\partial r}\Big|_1\Big) = 2\, \frac{\partial}{\partial r^1}\Big|_0 + 2\, \frac{\partial}{\partial r^2}\Big|_0, \qquad \gamma_{\ast(-1)}\Big(\frac{\partial}{\partial r}\Big|_{-1}\Big) = -2\, \frac{\partial}{\partial r^1}\Big|_0 + 2\, \frac{\partial}{\partial r^2}\Big|_0 ,
> $$
>
> two linearly independent vectors of $T_0\mathbb{R}^2$: the determinant of their coefficients is $2 \cdot 2 - (-2) \cdot 2 = 8 \neq 0$. Both lie in $\iota_{\ast0}(T_0C)$. Indeed $\gamma$ is smooth into $\mathbb{R}^2$ with values in $C$, so $\gamma = \iota \circ c$ with $c : \mathbb{R} \to C$ smooth (Lemma [[§37 Regular Submanifolds#^lem-37-3|§37.3]](2)), and by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) $\gamma_{\ast t} = \iota_{\ast0} \circ c_{\ast t}$ for $t = \pm 1$, where $\gamma(\pm 1) = 0$. By Proposition [[§37 Regular Submanifolds#^prop-37-4|§37.4]], $\iota_{\ast0}(T_0C)$ is spanned by the first $2 - k$ coordinate derivations of an adapted chart, so it has dimension $2 - k$. Containing two independent vectors, it has dimension $2$, so $k = 0$. But for $k = 0$ the condition of Definition [[§37 Regular Submanifolds#^def-37-2|§37.2]] on an adapted chart $(U, \varphi)$ at $(0, 0)$ has no equations, and reads $U \cap C = U$: the open set $U \ni (0, 0)$ would lie in $C$. That is false. $U$ contains a point $(0, s)$ with $s \neq 0$, and $(0, s) \notin C$, since $\gamma(t) = (0, s)$ forces $t^2 - 1 = 0$ and then $s = t^3 - t = t(t^2 - 1) = 0$. So $C$ is not a regular submanifold.

^pf-ex-39-1

*Uses:* [[§39 Immersions#^def-39-1|Def. §39.1]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§37 Regular Submanifolds#^def-37-1|Def. §37.1]], [[§15 Connected Spaces#^thm-15-3|590 §15.3]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§37 Regular Submanifolds#^lem-37-3|§37.3]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§37 Regular Submanifolds#^prop-37-4|§37.4]], [[§37 Regular Submanifolds#^def-37-2|Def. §37.2]]

![[m591-18-2.svg]]
*The nodal cubic. The parameter values $t = -1$ and $t = 1$ both land on the origin, where the two branches cross; the arrows show the curve continuing, its domain being all of $\mathbb{R}$. A small disc around the crossing meets the image in an X, which is not a piece of a line.*

> [!example] Example §39.2: An Injective Immersion That Is Not a Homeomorphism onto Its Image
> Let $\gamma : (a, b) \to \mathbb{R}^2$ be an injective immersion that passes through a point $P = \gamma(t_0)$ and whose other end returns to $P$: $\gamma(t) \to P$ as $t \to b$. Then $\gamma$ is not a homeomorphism onto its image, and near $P$ the image looks like a T.

^ex-39-2

> [!proof]+ Proof
> *(Lecture 13: “it's like you're making a hook with a piece of wire \ldots but the wire is open, it doesn't have an end”; the discontinuity argument is filled in.)* Since $\gamma$ is injective, it is a bijection of $(a, b)$ onto its image $\gamma\big((a,b)\big)$, which carries the subspace topology of $\mathbb{R}^2$ (Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]); we show that the inverse $\gamma^{-1} : \gamma\big((a,b)\big) \to (a, b)$ is not continuous at $P$, so that $\gamma$ is not a homeomorphism onto its image.
>
> Choose $t_k \to b$, with $t_k \in (a, b)$. Then $\gamma(t_k) \to P = \gamma(t_0)$ in the image: by hypothesis $\gamma(t_k) \to P$ in $\mathbb{R}^2$, and every open set of the image containing $P$ has the form $O \cap \gamma\big((a,b)\big)$ with $O$ open in $\mathbb{R}^2$ and $P \in O$, so it contains $\gamma(t_k)$ for all large $k$. But $t_k \to b \ne t_0$, so $\gamma^{-1}(\gamma(t_k)) = t_k$ does not converge to $\gamma^{-1}(P) = t_0$: choose $\varepsilon > 0$ with $t_0 + \varepsilon < b$; since $t_k \to b$, eventually $t_k > t_0 + \varepsilon$, so $t_k \notin (t_0 - \varepsilon, t_0 + \varepsilon)$. If $\gamma^{-1}$ were continuous at $P$, the preimage under $\gamma^{-1}$ of the open interval $(t_0 - \varepsilon, t_0 + \varepsilon) \ni t_0$ would contain an open set of the image containing $P$, hence $\gamma(t_k)$ for all large $k$, and then $t_k = \gamma^{-1}(\gamma(t_k)) \in (t_0 - \varepsilon, t_0 + \varepsilon)$ for those $k$ — a contradiction. So $\gamma^{-1} : \gamma\big((a,b)\big) \to (a, b)$ is not continuous at $P$.
>
> The image near $P$ consists of the strand through $P$ together with the end arriving at it: “this point now doesn't look like an X, but it looks like a T”; removing it leaves three pieces, not two.

^pf-ex-39-2

*Uses:* [[§39 Immersions#^def-39-1|Def. §39.1]], [[§12 Metric Topology#^thm-12-9|590 §12.9]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]]

![[m591-18-3.svg]]
*The hook. The domain is an open interval, so neither end is attained: the left end of the image is missing (hollow), and the right end only approaches $P$. But $P$ is in the image, reached at $t_0$ by the strand passing through it — so points of the image near $P$ come from parameters near $t_0$* and *from parameters near $b$, which is exactly the failure of continuity of $\gamma^{-1}$. Lee's figure-eight (Example 4.19) is an explicit instance with both ends returning, $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi)$, where the image near the origin is an X although $\beta$ is injective.*

> [!remark]- Connections
> - The image of Lee's figure-eight, as a topological space, is the wedge of two circles: [[Figure eight|590 Figure eight]].

> [!remark] Remark: Embeddings — Next Time
> To make the image of an [[§39 Immersions#^def-39-1|immersion]] a [[§37 Regular Submanifolds#^def-37-1|submanifold]], “you have to add a topological condition”: an *[[§40 Embeddings#^def-40-1|embedding]]* is an immersion that is a homeomorphism onto its image, and its image is a submanifold ([[§40 Embeddings#^thm-40-1|Theorem §40.1]]). Both were done in Lecture 14, together with the proof of the normal form above: see [[§40 Embeddings|§40]].

^rem-39-1
