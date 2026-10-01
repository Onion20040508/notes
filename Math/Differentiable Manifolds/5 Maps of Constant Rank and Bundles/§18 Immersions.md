---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 18
tags: [differentiable-manifolds, math591]
---
← [[§17 The Tangent Bundle]] · ↑ [[· 5 Maps of Constant Rank and Bundles]]

*Stage: maps — The maps with injective differentials: locally inclusions, globally more subtle.*

*References: Lee Ch. 4. Lecture 13.*

The third special type of map, dual to the submersions of [[§14 Local Diffeomorphisms and Submersions|§14]]: the differential is injective instead of surjective, and the local model is an inclusion instead of a projection.

## Immersions

*Lecture 13. “Next class of special maps”: Lecture 10 listed immersions among the special types of map, and the definition has been on record since ([[§14 Local Diffeomorphisms and Submersions#^def-14-2|Definition §14.2]]); Lecture 13 is where they were first treated seriously, after the tangent bundle ([[§17 The Tangent Bundle|§17]]).*

> [!definition] Definition §18.1: Immersions
> Let $F : M \to N$ be smooth, with $\dim M = m$ and $\dim N = n$. $F$ is an **immersion at $p$** if $F_{*p} : T_pM \to T_{F(p)}N$ is injective — which forces $m \le n$, since an injective linear map cannot lower dimension — and an **immersion** if it is an immersion at every point. “Go from a lower-dimensional manifold to a bigger one.”
>
> *Lee: Ch. 4, Immersions*

^def-18-1

> [!remark]- Connections
> - The earlier definition, stated with submersions: [[§14 Local Diffeomorphisms and Submersions#^def-14-2|Def. §14.2]]; the dimension constraint there: [[§14 Local Diffeomorphisms and Submersions#^prop-14-4|§14.4]].
> - An injective linear map cannot lower dimension: [[§8 Null Spaces and Ranges#^ladr-3-22|LADR 3.22]].

> [!theorem] Theorem §18.1: Local Normal Form for Immersions
> Let $F : M \to N$ be an immersion at $p$, with $\dim M = m \le n = \dim N$. Then there are charts $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$ with $F(U) \subseteq V$ in which the coordinate representation $\tilde F = \psi \circ F \circ \varphi^{-1}$ is the standard inclusion:
>
> $$
> \tilde F(r^1, \ldots, r^m) = (r^1, \ldots, r^m, \underbrace{0, \ldots, 0}_{n - m}) .
> $$
>
> *Lee: Theorem 4.12, the rank theorem*

^thm-18-1

![[m591-18-1.svg]]
*The immersion normal form, as on the board: the mirror image of the submersion normal form ([[§14 Local Diffeomorphisms and Submersions#^thm-14-5|Theorem §14.5]]). There $\tilde F$ forgot the last $m - n$ coordinates; here it appends $n - m$ zeros.*

*Status.* Stated in Lecture 13; the proof — “a little bit technical … better do it fresh at the beginning of the class” — is due in the next lecture. It is the counterpart of [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|Theorem §14.5]]: there $F$ was locally a projection, here it is locally an inclusion.

> [!remark]- Connections
> - The mirror-image result for submersions: [[§14 Local Diffeomorphisms and Submersions#^thm-14-5|Local Normal Form for Submersions, §14.5]]; the case $m = n$: [[§14 Local Diffeomorphisms and Submersions#^thm-14-2|§14.2]], via the [[§14 Local Diffeomorphisms and Submersions#^thm-14-1|Inverse Function Theorem, §14.1]] ([[Inverse Function Theorem (several variables)|452 §13.2]]).

What the image of an immersion looks like — locally a submanifold, globally not necessarily — is taken up next, in [[§18 Immersions#Images of Immersions|Images of Immersions]].

## Images of Immersions

*Lecture 13, continuing [[§18 Immersions#Immersions|Immersions]]. What the image of an immersion looks like. These results use submanifolds ([[§15 Submanifolds|§15]]).*

> [!theorem] Corollary §18.2: The Local Image of an Immersion
> In the charts of [[§18 Immersions#^thm-18-1|Theorem §18.1]], $F|_U$ is injective and $F(U)$ is a submanifold of $N$ of codimension $n - m$.

^cor-18-2

> [!proof]+ Proof
> *(Lecture 13 gave the idea — the image of $\tilde F$ is an open set times zeros, “and so since what happens below happens upstairs too”, $F(U)$ is a submanifold — adding “I'm feeling a little bit uneasy, because I want to say after restriction, possibly after restricting $U$.” Completed here: shrinking $V$ instead of $U$ settles it.)* $\tilde F$ is injective, so $F|_U$ is. Let
>
> $$
> V' = \big\{\, q \in V : \big(y^1(q), \ldots, y^m(q)\big) \in \varphi(U) \,\big\},
> $$
>
> open in $N$ because $\varphi(U)$ is open, and containing $F(U)$ because $\psi(F(u)) = (\varphi(u), \vec 0)$. We claim $F(U) = \{ q \in V' : y^{m+1}(q) = \cdots = y^n(q) = 0 \}$. The inclusion $\subseteq$ is clear. Conversely, if $q \in V'$ has $\psi(q) = (r, \vec 0)$ with $r \in \varphi(U)$, then $\psi(q) = \tilde F(r) = \psi\big(F(\varphi^{-1}(r))\big)$, so $q = F(\varphi^{-1}(r))$ because $\psi$ is injective. So $(V', \psi|_{V'})$ is an adapted chart ([[§15 Submanifolds#^def-15-1|Definition §15.1]]) at every point of $F(U)$, and $F(U)$ is a submanifold of codimension $n - m$. No restriction of $U$ was needed: the worry was that $\psi(V) \cap (\mathbb{R}^m \times \{\vec 0\})$ might contain points not of the form $\tilde F(r)$ with $r \in \varphi(U)$, and passing to $V'$ removes exactly those.

^pf-18-2

*Uses:* [[§18 Immersions#^thm-18-1|§18.1]], [[§15 Submanifolds#^def-15-1|Def. §15.1]], [[§2 Topological Manifolds#^lem-2-11|§2.11]]

> [!remark]- Connections
> - The global version needs a topological condition: [[§18 Immersions#^rem-18-1|Remark: Embeddings — Next Time]].

“But the really interesting thing about these immersions is that globally it doesn't have to be the case”: the whole image of an immersion need not be a submanifold. There are two ways for this to fail.

> [!example] Example §18.1: An Immersion That Crosses Itself
> $\gamma : \mathbb{R} \to \mathbb{R}^2$, $\gamma(t) = (t^2 - 1, \ t^3 - t)$, is an immersion, but it is not injective, and its image is not a submanifold of $\mathbb{R}^2$: near the origin the image looks like an X.

^ex-18-1

> [!proof]+ Proof
> *(Lecture 13 drew a curve crossing itself and gave the argument below; the specific curve is filled in.)* $\gamma'(t) = (2t, 3t^2 - 1)$ never vanishes — the first component vanishes only at $t = 0$, where the second is $-1$ — so $\gamma$ is an immersion. And $\gamma(1) = \gamma(-1) = (0, 0)$, so $\gamma$ is not injective. Near the origin the image consists of two arcs crossing transversally, one through $\gamma(-1)$ and one through $\gamma(1)$, with tangent directions $\gamma'(\mp 1) = (\mp 2, 2)$. “What is the proof? If you remove the point of intersection from an X, you get four connected components. If you remove a point from an interval, you get two.” This is the lecture's level of rigour: made precise, it compares small connected neighbourhoods of the crossing point in the image with those of a point of a $1$-manifold.

^pf-ex-18-1

*Uses:* [[§18 Immersions#^def-18-1|Def. §18.1]], [[§12 Tangent Spaces II꞉ The Abstract Tangent Space#^prop-12-25|§12.25]], [[§15 Submanifolds#^def-15-1|Def. §15.1]], [[§13 Connected Spaces#^thm-13-3|590 §13.3]]

![[m591-18-2.svg]]
*The nodal cubic. The parameter values $t = -1$ and $t = 1$ both land on the origin, where the two branches cross; the arrows show the curve continuing, its domain being all of $\mathbb{R}$. A small disc around the crossing meets the image in an X, which is not a piece of a line.*

> [!example] Example §18.2: An Injective Immersion That Is Not a Homeomorphism onto Its Image
> Let $\gamma : (a, b) \to \mathbb{R}^2$ be an injective immersion that passes through a point $P = \gamma(t_0)$ and whose other end returns to $P$: $\gamma(t) \to P$ as $t \to b$. Then $\gamma$ is not a homeomorphism onto its image, and near $P$ the image looks like a T.

^ex-18-2

> [!proof]+ Proof
> *(Lecture 13: “it's like you're making a hook with a piece of wire … but the wire is open, it doesn't have an end”; the discontinuity argument is filled in.)* Choose $t_k \to b$. Then $\gamma(t_k) \to P = \gamma(t_0)$ in the image, but $t_k \to b \ne t_0$, so $\gamma^{-1}(\gamma(t_k)) = t_k$ does not converge to $\gamma^{-1}(P) = t_0$. So $\gamma^{-1} : \gamma\big((a,b)\big) \to (a, b)$ is not continuous at $P$. The image near $P$ consists of the strand through $P$ together with the end arriving at it: “this point now doesn't look like an X, but it looks like a T”; removing it leaves three pieces, not two.

^pf-ex-18-2

*Uses:* [[§18 Immersions#^def-18-1|Def. §18.1]], [[§11 Metric Topology#^thm-11-9|590 §11.9]]

![[m591-18-3.svg]]
*The hook. The domain is an open interval, so neither end is attained: the left end of the image is missing (hollow), and the right end only approaches $P$. But $P$ is in the image, reached at $t_0$ by the strand passing through it — so points of the image near $P$ come from parameters near $t_0$* and *from parameters near $b$, which is exactly the failure of continuity of $\gamma^{-1}$. Lee's figure-eight (Example 4.19) is an explicit instance with both ends returning, $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi)$, where the image near the origin is an X although $\beta$ is injective.*

> [!remark]- Connections
> - The image of Lee's figure-eight, as a topological space, is the wedge of two circles: [[Figure eight|590 Figure eight]].

> [!remark] Remark: Embeddings — Next Time
> To make the image of an immersion a submanifold, “you have to add a topological condition”: an *embedding* is, roughly, an injective immersion that is a homeomorphism onto its image, and its image will be a submanifold. The definition and the proof of the normal form for immersions are due in the next lecture.

^rem-18-1
