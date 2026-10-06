---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 37
tags: [differentiable-manifolds, math591]
---
← [[§36 Fibrations]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§38 Embeddings]] →

*Stage: maps — The maps with injective differentials: locally inclusions, globally more subtle.*

*References: Lee Ch. 4. Lecture 13.*

The third special type of map, dual to the submersions of [[§34 Submersions|§34]]: the differential is injective instead of surjective, and the local model is an inclusion instead of a projection.

## Immersions

*Lecture 13. “Next class of special maps”: Lecture 10 listed immersions among the special types of map, and the definition has been on record since ([[§34 Submersions#^def-34-2|Definition §34.2]]); Lecture 13 is where they were first treated seriously, after the tangent bundle ([[§44 The Tangent Bundle|§44]]).*

> [!definition] Definition §37.1: Immersions
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$. $F$ is an **immersion at $p$** if $F_{\ast p} : T_pM \to T_{F(p)}N$ is injective — which forces $m \le n$, since an injective linear map cannot lower dimension — and an **immersion** if it is an immersion at every point. “Go from a lower-dimensional manifold to a bigger one.”
>
> *Lee: Ch. 4, Immersions*

^def-37-1

> [!remark]- Connections
> - The earlier definition, stated with submersions: [[§34 Submersions#^def-34-2|Def. §34.2]]; the dimension constraint there: [[§34 Submersions#^prop-34-1|§34.1]].
> - An injective linear map cannot lower dimension: [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]].
> - The first examples are the regular parametrized surfaces of 452, whose $3 \times 2$ Jacobian has rank 2: [[§31 Surface Integrals#^def-31-3|452 Def. §31.3]].

> [!theorem] Theorem §37.1: Local Normal Form for Immersions
> Let $F : M \to N$ be an immersion at $p$, with $\dim M = m \le n = \dim N$. Then there are charts $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U) \subseteq V$ in which the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$ is the standard inclusion:
>
> $$
> \tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^m, \underbrace{0, \ldots, 0}_{n - m}) .
> $$
>
> *Lee: Theorem 4.12, the rank theorem*

^thm-37-1

> [!proof]+ Proof (Lecture 14)
> The steps are the lecture's, in the lecture's order; sentences marked *(Completion.)* fill in details. The first half runs as for submersions ([[§34 Submersions#^thm-34-4|Theorem §34.4]]); the new step is that here the chart on $N$ changes too.
>
> *1. Start with any coordinates.* Take [[§19 Smooth Functions and Smooth Maps#^def-19-1|charts]] $(U_0, \varphi_0 = (x^1, \ldots, x^m))$ at $p$ and $(V_0, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U_0) \subseteq V_0$, shrinking $U_0$ if necessary, and write $F^j = y^j \circ F$.
>
> *2. The Jacobian is taller than wide.* $J = \big[\partial F^j/\partial x^i(p)\big]$ is the matrix of $F_{\ast p}$ ([[§30 The Differential in Coordinates#^thm-30-2|Theorem §30.2]]): $n$ rows and $m$ columns, “fewer columns than rows.” $F_{\ast p}$ is injective, so $J$ has rank $m$: it has $m$ linearly independent row vectors.
>
> *3. Relabel the $y$'s.* Reordering the coordinates of $\psi$ — again a smooth chart, as in step 4 of the [[§34 Submersions#^pf-34-4|proof of Theorem §34.4]] — we may assume the top $m \times m$ block $A$ of $J$ is invertible.
>
> *4. The first $m$ components of $F$ are coordinates on $M$.* $A$ is the Jacobian at $p$, in the $x$-coordinates, of the map $U_0 \to \mathbb{R}^m$ that sends $q$ to the first $m$ components $\big(F^1(q), \ldots, F^m(q)\big)$ ([[§30 The Differential in Coordinates#^prop-30-1|Proposition §30.1]]). It is invertible, so by the inverse function theorem ([[§33 Local Diffeomorphisms#^thm-33-1|Theorem §33.1]]) — “I always say implicit, but in this case I want the inverse function theorem” — this map is a [[§33 Local Diffeomorphisms#^def-33-1|local diffeomorphism]] near $p$, and, possibly after shrinking $U_0$ to some $U \ni p$, it is a chart:
>
> $$
> \tilde\varphi = \big(F^1, \ldots, F^m\big)\big|_U : U \longrightarrow \tilde\varphi(U) \subseteq \mathbb{R}^m .
> $$
>
> *(Completion.)* As in step 8 of the [[§34 Submersions#^pf-34-4|proof of Theorem §34.4]]: the inverse function theorem gives an open $W \ni \varphi_0(p)$ on which $\tilde\varphi \circ \varphi_0^{-1}$ is a [[§17 Differentiable Structures#^def-17-3|diffeomorphism]] onto an open set; put $U = \varphi_0^{-1}(W)$; then $\tilde\varphi$ maps $U$ [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphically]] onto an open set, and is a chart by [[§34 Submersions#^lem-34-3|Lemma §34.3]].
>
> *5. In the new chart, $F$ is a graph.* Let $\hat F = \psi \circ F \circ \tilde\varphi^{-1} : \tilde\varphi(U) \to \psi(V_0)$. By the definition of $\tilde\varphi$, the first $m$ components of $\hat F(r)$ are $F^i(\tilde\varphi^{-1}(r)) = r^i$, so
>
> $$
> \hat F(r) = \big(r, \ G^1(r), \ldots, G^{n-m}(r)\big), \qquad G^k = F^{m+k} \circ \tilde\varphi^{-1} ,
> $$
>
> with $G = (G^1, \ldots, G^{n-m})$ smooth on $\tilde\varphi(U)$. “I don't get zeros yet. I get something”: $\hat F$ is the graph of $G$ over $\tilde\varphi(U)$.
>
> *6. Straighten the graph.* “You can always straighten out a graph to make it zero.” Define new coordinates on $N$ by keeping the first $m$ and shifting the rest: “I always mess up my indices … so I'm going to cheat”
>
> $$
> \tilde y^i = y^i \quad (1 \le i \le m), \qquad \tilde y^i = y^i - G^{i-m}\big(y^1, \ldots, y^m\big) \quad (m+1 \le i \le n),
> $$
>
> and $\tilde\psi = (\tilde y^1, \ldots, \tilde y^n)$. *(Completion.)* This is $\tilde\psi = \Sigma \circ \psi$, where $\Sigma(y_a, y_b) = \big(y_a, \, y_b - G(y_a)\big)$ for $y_a = (y^1, \ldots, y^m)$ and $y_b = (y^{m+1}, \ldots, y^n)$. $\Sigma$ is defined on $\tilde\varphi(U) \times \mathbb{R}^{n-m}$, and is a diffeomorphism of that open set onto itself, with inverse $(y_a, z) \mapsto (y_a, z + G(y_a))$. So on the open set $V = \psi^{-1}\big(\tilde\varphi(U) \times \mathbb{R}^{n-m}\big) \cap V_0$ the map $\tilde\psi$ is a diffeomorphism onto an open subset of $\mathbb{R}^n$, hence a chart ([[§34 Submersions#^lem-34-3|Lemma §34.3]]). And $F(U) \subseteq V$, because the first $m$ coordinates of $\psi(F(u))$ are $\tilde\varphi(u) \in \tilde\varphi(U)$.
>
> *7. These do the job.* “We're not changing the first $m$ — we already have the inclusion here — but we're fixing the other ones.” *(Completion.)* For $r \in \tilde\varphi(U)$,
>
> $$
> \tilde\psi \circ F \circ \tilde\varphi^{-1}(r) = \Sigma\big(\hat F(r)\big) = \Sigma\big(r, G(r)\big) = \big(r, \, G(r) - G(r)\big) = (r, \vec 0) .
> $$
>
> So in the charts $(U, \tilde\varphi)$ and $(V, \tilde\psi)$, $F$ is the standard inclusion.

^pf-37-1

*Uses:* [[§37 Immersions#^def-37-1|Def. §37.1]], [[§19 Smooth Functions and Smooth Maps#^def-19-1|Def. §19.1]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]], [[§30 The Differential in Coordinates#^prop-30-1|§30.1]], [[§34 Submersions#^thm-34-4|§34.4]] (steps 4 and 8 of its proof), [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§33 Local Diffeomorphisms#^thm-33-1|§33.1]], [[§33 Local Diffeomorphisms#^def-33-1|Def. §33.1]], [[§34 Submersions#^lem-34-3|§34.3]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§9 Matrices#^ladr-3-57|LADR 3.57]]

![[m591-32-1.svg]]
*The two changes of chart in one diagram, as on the board. On $M$, the chart $\tilde\varphi$ is made from the first $m$ components of $F$, which turns $F$ into the graph $\hat F$; on $N$, the straightening $\Sigma$ removes the graph, so that $\tilde F = \Sigma \circ \hat F$ is the inclusion.*

![[m591-32-2.svg]]
*Step 6 in a picture ($m = n - m = 1$). Before: the image of $\hat F$ is the graph $y_b = G(y_a)$ over $\tilde\varphi(U)$. After: each point is moved straight down by $G(y_a)$, and the graph becomes a piece of the $y_a$-axis — an open interval, over the same $\tilde\varphi(U)$.*

**Transcription note.** Page 38 of the handwritten notes begins the proof with “start with any coordinates with $\varphi(U) \subset V$”; the condition is $F(U) \subseteq V$. In the lecture the shifted coordinates were first spoken as $G^{i-m}(y^1, \ldots, y^n)$; the arguments are the first $m$ coordinates, $y^1, \ldots, y^m$, as on page 38.

![[m591-18-1.svg]]
*The immersion normal form, as on the board: the mirror image of the submersion normal form ([[§34 Submersions#^thm-34-4|Theorem §34.4]]). There $\tilde F$ forgot the last $m - n$ coordinates; here it appends $n - m$ zeros.*

*Status.* Stated in Lecture 13 — “a little bit technical … better do it fresh at the beginning of the class” — and proved at the start of Lecture 14, above. It is the counterpart of [[§34 Submersions#^thm-34-4|Theorem §34.4]]: there $F$ was locally a projection, here it is locally an inclusion.

> [!remark]- Connections
> - The mirror-image result for submersions: [[§34 Submersions#^thm-34-4|Local Normal Form for Submersions, §34.4]]; the case $m = n$: [[§33 Local Diffeomorphisms#^thm-33-2|§33.2]], via the [[§33 Local Diffeomorphisms#^thm-33-1|Inverse Function Theorem, §33.1]] ([[Inverse Function Theorem (several variables)|452 §16.2]]).

What the image of an immersion looks like — locally a submanifold, globally not necessarily — is taken up next, in [[§37 Immersions#Images of Immersions|Images of Immersions]].

## Images of Immersions

*Lecture 13, continuing [[§37 Immersions#Immersions|Immersions]]. What the image of an immersion looks like. These results use submanifolds ([[§35 Submanifolds|§35]]).*

> [!theorem] Corollary §37.2: The Local Image of an Immersion
> In the charts of [[§37 Immersions#^thm-37-1|Theorem §37.1]], $F|_U$ is injective and $F(U)$ is a submanifold of $N$ of codimension $n - m$.

^cor-37-2

> [!proof]+ Proof
> *(Lecture 13 gave the idea — the image of $\tilde F$ is an open set times zeros, “and so since what happens below happens upstairs too”, $F(U)$ is a submanifold — adding “I'm feeling a little bit uneasy, because I want to say after restriction, possibly after restricting $U$.” Completed here: shrinking $V$ instead of $U$ settles it.)* $\tilde F$ is injective, so $F|_U$ is. Let
>
> $$
> V' = \big\{\, q \in V : \big(y^1(q), \ldots, y^m(q)\big) \in \varphi(U) \,\big\},
> $$
>
> open in $N$ because $\varphi(U)$ is open, and containing $F(U)$ because $\psi(F(u)) = (\varphi(u), \vec 0)$. We claim $F(U) = \{ q \in V' : y^{m+1}(q) = \cdots = y^n(q) = 0 \}$. The inclusion $\subseteq$ is clear. Conversely, if $q \in V'$ has $\psi(q) = (r, \vec 0)$ with $r \in \varphi(U)$, then $\psi(q) = \tilde F(r) = \psi\big(F(\varphi^{-1}(r))\big)$, so $q = F(\varphi^{-1}(r))$ because $\psi$ is injective. So $(V', \psi|_{V'})$ is an adapted chart ([[§35 Submanifolds#^def-35-2|Definition §35.2]]) at every point of $F(U)$, and $F(U)$ is a submanifold of codimension $n - m$. No restriction of $U$ was needed: the worry was that $\psi(V) \cap (\mathbb{R}^m \times \{\vec 0\})$ might contain points not of the form $\tilde F(r)$ with $r \in \varphi(U)$, and passing to $V'$ removes exactly those.

^pf-37-2

*Uses:* [[§37 Immersions#^thm-37-1|§37.1]], [[§35 Submanifolds#^def-35-1|Def. §35.1]], [[§35 Submanifolds#^def-35-2|Def. §35.2]], [[§2 Topological Manifolds#^lem-2-10|§2.10]]

> [!remark]- Connections
> - The global version needs a topological condition: [[§37 Immersions#^rem-37-1|Remark: Embeddings — Next Time]].
> - The global statement, for embeddings: [[§38 Embeddings#^thm-38-1|§38.1]].

“But the really interesting thing about these immersions is that globally it doesn't have to be the case”: the whole image of an immersion need not be a submanifold. There are two ways for this to fail.

> [!example] Example §37.1: An Immersion That Crosses Itself
> $\gamma : \mathbb{R} \to \mathbb{R}^2$, $\gamma(t) = (t^2 - 1, \ t^3 - t)$, is an immersion, but it is not injective, and its image is not a submanifold of $\mathbb{R}^2$: near the origin the image looks like an X.

^ex-37-1

> [!proof]+ Proof
> *(Lecture 13 drew a curve crossing itself and gave the argument below; the specific curve is filled in.)* $\gamma'(t) = (2t, 3t^2 - 1)$ never vanishes — the first component vanishes only at $t = 0$, where the second is $-1$ — so $\gamma$ is an immersion. And $\gamma(1) = \gamma(-1) = (0, 0)$, so $\gamma$ is not injective. Near the origin the image consists of two arcs crossing transversally, one through $\gamma(-1)$ and one through $\gamma(1)$, with tangent directions $\gamma'(\mp 1) = (\mp 2, 2)$. “What is the proof? If you remove the point of intersection from an X, you get four connected components. If you remove a point from an interval, you get two.” This is the lecture's level of rigour: made precise, it compares small connected neighbourhoods of the crossing point in the image with those of a point of a $1$-manifold.

^pf-ex-37-1

*Uses:* [[§37 Immersions#^def-37-1|Def. §37.1]], [[§30 The Differential in Coordinates#^prop-30-5|§30.5]], [[§35 Submanifolds#^def-35-1|Def. §35.1]], [[§15 Connected Spaces#^thm-15-3|590 §15.3]]

![[m591-18-2.svg]]
*The nodal cubic. The parameter values $t = -1$ and $t = 1$ both land on the origin, where the two branches cross; the arrows show the curve continuing, its domain being all of $\mathbb{R}$. A small disc around the crossing meets the image in an X, which is not a piece of a line.*

> [!example] Example §37.2: An Injective Immersion That Is Not a Homeomorphism onto Its Image
> Let $\gamma : (a, b) \to \mathbb{R}^2$ be an injective immersion that passes through a point $P = \gamma(t_0)$ and whose other end returns to $P$: $\gamma(t) \to P$ as $t \to b$. Then $\gamma$ is not a homeomorphism onto its image, and near $P$ the image looks like a T.

^ex-37-2

> [!proof]+ Proof
> *(Lecture 13: “it's like you're making a hook with a piece of wire … but the wire is open, it doesn't have an end”; the discontinuity argument is filled in.)* Choose $t_k \to b$. Then $\gamma(t_k) \to P = \gamma(t_0)$ in the image, but $t_k \to b \ne t_0$, so $\gamma^{-1}(\gamma(t_k)) = t_k$ does not converge to $\gamma^{-1}(P) = t_0$. So $\gamma^{-1} : \gamma\big((a,b)\big) \to (a, b)$ is not continuous at $P$. The image near $P$ consists of the strand through $P$ together with the end arriving at it: “this point now doesn't look like an X, but it looks like a T”; removing it leaves three pieces, not two.

^pf-ex-37-2

*Uses:* [[§37 Immersions#^def-37-1|Def. §37.1]], [[§12 Metric Topology#^thm-12-9|590 §12.9]]

![[m591-18-3.svg]]
*The hook. The domain is an open interval, so neither end is attained: the left end of the image is missing (hollow), and the right end only approaches $P$. But $P$ is in the image, reached at $t_0$ by the strand passing through it — so points of the image near $P$ come from parameters near $t_0$* and *from parameters near $b$, which is exactly the failure of continuity of $\gamma^{-1}$. Lee's figure-eight (Example 4.19) is an explicit instance with both ends returning, $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi)$, where the image near the origin is an X although $\beta$ is injective.*

> [!remark]- Connections
> - The image of Lee's figure-eight, as a topological space, is the wedge of two circles: [[Figure eight|590 Figure eight]].

> [!remark] Remark: Embeddings — Next Time
> To make the image of an [[§37 Immersions#^def-37-1|immersion]] a [[§35 Submanifolds#^def-35-1|submanifold]], “you have to add a topological condition”: an *[[§38 Embeddings#^def-38-1|embedding]]* is an immersion that is a homeomorphism onto its image, and its image is a submanifold ([[§38 Embeddings#^thm-38-1|Theorem §38.1]]). Both were done in Lecture 14, together with the proof of the normal form above: see [[§38 Embeddings|§38]].

^rem-37-1
