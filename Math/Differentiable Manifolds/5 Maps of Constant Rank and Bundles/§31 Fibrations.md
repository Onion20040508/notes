---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 31
tags: [differentiable-manifolds, math591]
---
← [[§30 Submanifolds]] · ↑ [[· 5 Maps of Constant Rank and Bundles]] · [[§32 The Tangent Bundle]] →

*Stage: bundles — Submersions that are locally products.*

*References: Lee Ch. 10. Lectures 11–13.*

The submersions that look locally like the projection $U \times F \to U$. Their fibres are submanifolds ([[§30 Submanifolds|§30]]), all copies of one fibre; the tangent bundle of the next section is the first major example.

## Fibrations

*Lecture 11. “An important class within the submersions.” Uribe introduced fibrations now because the tangent bundle, the cotangent bundle and vector bundles, coming soon, are all fibrations. The idea: surjective maps $\pi : M \to B$ that are locally like the projection $U \times F \to U$, with $U$ open in the **base** $B$ and $F$ a third, fixed manifold. There is a notation clash he apologized for — $F$ now names the fibre, not the map, which is called $\pi$.*

> [!definition] Definition §31.1: Fibration
> Let $M$, $B$ and $F$ be smooth manifolds and $\pi : M \to B$ smooth. Then $\pi$ is a **fibration with fibre $F$** if there are an open cover $\{U_\alpha\}_{\alpha \in A}$ of $B$ and, for each $\alpha$, a diffeomorphism
>
> $$
> \phi_\alpha : \pi^{-1}(U_\alpha) \longrightarrow U_\alpha \times F \qquad \text{with} \qquad \mathrm{pr}_1 \circ \phi_\alpha = \pi|_{\pi^{-1}(U_\alpha)},
> $$
>
> where $\pi^{-1}(U_\alpha)$ is an open submanifold of $M$, $U_\alpha \times F$ a product manifold ([[§15 Smooth Functions and Smooth Maps#^def-15-6|Definition §15.6]]), and $\mathrm{pr}_1 : U_\alpha \times F \to U_\alpha$ the projection. The $\phi_\alpha$ are called **local trivializations**. $M$ is the **total space** and $B$ the **base**.
>
> *Lee: Ch. 10, smooth fiber bundles*

^def-31-1

> [!remark]- Connections
> - The first major example: [[§32 The Tangent Bundle#^cor-32-3|the tangent bundle, §32.3]]; sections of a fibration: [[§32 The Tangent Bundle#^def-32-3|Def. §32.3]].
> - The topological analogue with discrete fibre: [[§24 Covering Spaces#^def-24-2|covering maps, 590 Def. §24.2]]; in 591, [[§28 Local Diffeomorphisms#^rem-28-2|Remark: Covering Maps (§28)]].

![[m591-16-1.svg]]
*The local trivialization $\phi_\alpha$ over $U_\alpha$: the triangle commutes, $\mathrm{pr}_1 \circ \phi_\alpha = \pi|$.*

The diagram *commutes*. A student asked what that means; Uribe: “whenever you have a diagram … all the compositions that you can construct from one place to another give you the same answer.” Here there are two routes from $\pi^{-1}(U_\alpha)$ to $U_\alpha$, and they agree: $\mathrm{pr}_1 \circ \phi_\alpha = \pi|$. Concretely, $\phi_\alpha(p) = (\pi(p), \ast)$ — its first component *is* $\pi(p)$, and only the second, a point of $F$, is new information.

![[m591-16-2.svg]]
*Uribe's cartoon, and why it matters: “these cartoons are incredibly important.” On the left, the global product $B \times F$, with each fibre $\{b\} \times F$ standing over its point. On the right, a total space that need not be a product: its fibres may twist as they travel over $B$. But over each $U_\alpha$ the part $\pi^{-1}(U_\alpha)$ is identified by $\phi_\alpha$ with the straight product $U_\alpha \times F$, and the identification respects the base points, which is the commuting diagram.*

> [!theorem] Proposition §31.1: Fibres and Fibrations
> Let $\pi : M \to B$ be a fibration with fibre $F$.
> 1. For every $b \in B$, the fibre $\pi^{-1}(b)$ is homeomorphic to $F$: every fibre is a copy of the model fibre.
> 2. $\pi$ is a submersion, and it is surjective if $F \ne \emptyset$.
> 3. $\pi$ is an open map.

^prop-31-1

> [!proof]+ Proof
> *(Stated in lecture; (2) as “chain rule and stuff”.)* (1) Choose $\alpha$ with $b \in U_\alpha$. Because the diagram commutes and $\phi_\alpha$ is a bijection, $\phi_\alpha$ maps $\pi^{-1}(b)$ onto $\mathrm{pr}_1^{-1}(b) = \{b\} \times F$; it restricts to a homeomorphism with the subspace topologies. And $\{b\} \times F \to F$, $(b, f) \mapsto f$, is a homeomorphism, with inverse $f \mapsto (b, f)$. (2) On the open set $\pi^{-1}(U_\alpha)$, $\pi = \mathrm{pr}_1 \circ \phi_\alpha$; by the [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|Chain Rule]] $\pi_{\ast p} = (\mathrm{pr}_1)_{\ast} \circ (\phi_\alpha)_{\ast p}$, a composite of an isomorphism and a surjection ([[§29 Submersions#^ex-29-2|Example §29.2]]), hence onto. Every $b$ lies in some $U_\alpha$, and its fibre is a copy of $F$, nonempty if $F$ is. (3) [[§29 Submersions#^cor-29-6|Corollary §29.6]].

^pf-31-1

*Uses:* [[§31 Fibrations#^def-31-1|Def. §31.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§23 Derivations and the Abstract Tangent Space#^cor-23-7|§23.7]], [[§29 Submersions#^def-29-1|Def. §29.1]], [[§29 Submersions#^ex-29-2|Ex. §29.2]], [[§29 Submersions#^cor-29-6|§29.6]], [[§9 Continuous Functions#^prop-9-3|590 §9.3]]

> [!example] Example §31.1: The Hopf Fibration $S^{2n+1} \to \mathbb{CP}^n$
> The projection $\pi : S^{2n+1} \to \mathbb{CP}^n$, $\pi(z) = [z]$, is a fibration with fibre $S^1$. Over the chart domain $U_j = \{z_j \ne 0\}$ a local trivialization is
>
> $$
> \phi_j : \pi^{-1}(U_j) \to U_j \times S^1, \qquad \phi_j(z) = \Big(\, [z],\ \frac{z_j}{|z_j|} \,\Big),
> $$
>
> with inverse $([w], \lambda) \mapsto \lambda\, \hat w / |\hat w|$, where $\hat w$ is the representative of $[w]$ with $\hat w_j = 1$.
>
> *Lee: Problem 4-5(a) and the Hopf map of Ch. 21*

^ex-31-1

> [!proof]+ Proof
> *(Claimed in lecture — a student supplied the fibre, $S^1$; the trivialization is filled in.)* The sets $U_j$ cover $\mathbb{CP}^n$, and $\pi^{-1}(U_j) = S^{2n+1} \cap \{z_j \ne 0\}$ is open. $\phi_j$ is smooth: in the chart $\varphi_j$ of [[§14 Projective Spaces as Smooth Manifolds#^def-14-2|Definition §14.2]] its first component is $z \mapsto (z_k/z_j)_{k \ne j}$, and its second is $z \mapsto z_j/|z_j|$, both smooth on $\{z_j \ne 0\}$, with the second taking values in $S^1$ ([[§16 Manifolds in Euclidean Space#^lem-16-3|Lemma §16.3]]). The proposed inverse is smooth, since in the chart it is $(u, \lambda) \mapsto \lambda \hat w(u)/|\hat w(u)|$ with $\hat w(u)$ the vector $u$ with the entry $1$ inserted in slot $j$, a smooth map into $\mathbb{C}^{n+1} \setminus \{0\}$ landing in $S^{2n+1}$ ([[§16 Manifolds in Euclidean Space#^lem-16-3|Lemma §16.3]]). They are mutually inverse: for $z \in S^{2n+1}$ with $z_j \ne 0$, $\hat w = z/z_j$ and $\lambda = z_j/|z_j|$ give $\lambda \hat w/|\hat w| = z/|z| = z$; conversely $z = \lambda \hat w/|\hat w|$ has $[z] = [\hat w]$ and $z_j/|z_j| = \lambda$. Finally $\mathrm{pr}_1 \circ \phi_j = \pi$ by definition. So each $\phi_j$ is a local trivialization.

^pf-ex-31-1

*Uses:* [[§31 Fibrations#^def-31-1|Def. §31.1]], [[§14 Projective Spaces as Smooth Manifolds#^def-14-2|Def. §14.2]], [[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]], [[§16 Manifolds in Euclidean Space#^lem-16-3|§16.3]]

![[m591-16-7.svg]]
*The fibres of the Hopf fibration for $n = 1$, $S^3 \to \mathbb{CP}^1$, made visible in $\mathbb{R}^3$ by stereographic projection of $S^3$ from the point $(0, 1)$. Blue: the fibre through $(1, 0)$, which projects to the unit circle, and the fibre through $(0, 1)$ itself, which projects to the vertical axis closed up at infinity. Red: two more fibres, through points with $|z_1| = |z_2|$. Each fibre is a circle $\{\lambda z : |\lambda| = 1\}$, no two meet, and any two are linked: over each $U_j$ the circles sit side by side as in $U_j \times S^1$, but globally they are woven together.*

> [!remark]- Connections
> - $\mathbb{CP}^n$ as the orbit space $S^{2n+1}/\mathrm{U}(1)$: [[§10 Group Actions and Orbit Spaces#^ex-10-3|Ex. §10.3]]. The Hopf fibration has no section: [[§32 The Tangent Bundle#^rem-32-3|Remark: Sections Need Not Exist (§31)]].

With [[§31 Fibrations#^prop-31-1|Proposition §31.1]](2), this also proves [[§29 Submersions#^ex-29-3|Example §29.3]], which Lecture 10 stated without proof: the projection $S^{2n+1} \to \mathbb{CP}^n$ is a submersion. Its fibres are the circles $\{\lambda z : |\lambda| = 1\}$.

> [!remark] Remark: What Comes Next
> Tangent bundles, cotangent bundles and vector bundles are fibrations “with additional structure, where the fibres are vector spaces.” The basic notion of fibration is more general: its fibre $F$ is any manifold.

^rem-31-1

> [!remark]- Connections
> - [[§32 The Tangent Bundle#^cor-32-3|The tangent bundle is a fibration, §32.3]]; [[§32 The Tangent Bundle#^def-32-5|the cotangent bundle, Def. §32.5]]; [[§32 The Tangent Bundle#^rem-32-2|Remark: Vector Bundles (§31)]].

**Transcription note.** Stating the idea of a fibration, Uribe first said “$U$ open in $M$”; a student corrected it to open in $B$, as in the definition.

## Fibres and Examples

*Lecture 12. Uribe changed the notation once more “to conform to more general usage”: the fibration is $\pi : E \to B$, with total space $E$, base $B$, and fibre $F$ — the definition as before ([[§31 Fibrations#^def-31-1|Definition §31.1]]), with $E$ in place of $M$.*

> [!theorem] Proposition §31.2: Fibres Are Copies of the Model Fibre
> Let $\pi : E \to B$ be a fibration with fibre $F$ and $b \in B$. Then $\pi^{-1}(b)$ is a submanifold of $E$, and for every $\alpha$ with $b \in U_\alpha$ the local trivialization $\phi_\alpha$ restricts to a diffeomorphism
>
> $$
> \pi^{-1}(b) \longrightarrow \{b\} \times F \cong F .
> $$

^prop-31-2

> [!proof]+ Proof
> *(Claimed in Lecture 12 — “I claim that they are diffeomorphic to this fibre, to the third manifold that is sitting outside, looking over [the] landscape”; filled in.)* $\pi$ is a submersion ([[§31 Fibrations#^prop-31-1|Proposition §31.1]]), so $\pi^{-1}(b)$ is a submanifold ([[§30 Submanifolds#^cor-30-7|Corollary §30.7]]); likewise $\{b\} \times F = \mathrm{pr}_1^{-1}(b)$ is a submanifold of $U_\alpha \times F$ ([[§29 Submersions#^ex-29-2|Example §29.2]]). Because the diagram commutes, $\phi_\alpha$ maps $\pi^{-1}(b)$ bijectively onto $\{b\} \times F$. The restriction and its inverse are smooth as maps into $U_\alpha \times F$ and into $E$ (restrictions of $\phi_\alpha$, $\phi_\alpha^{-1}$ to submanifolds, [[§30 Submanifolds#^lem-30-3|Lemma §30.3]](1)), hence smooth into the submanifolds $\{b\} \times F$ and $\pi^{-1}(b)$ ([[§30 Submanifolds#^lem-30-3|Lemma §30.3]](2)). Finally $\{b\} \times F \to F$, $(b, f) \mapsto f$, is a diffeomorphism by the same lemma, with inverse $f \mapsto (b, f)$.

^pf-31-2

*Uses:* [[§31 Fibrations#^def-31-1|Def. §31.1]], [[§31 Fibrations#^prop-31-1|§31.1]], [[§30 Submanifolds#^cor-30-7|§30.7]], [[§29 Submersions#^ex-29-2|Ex. §29.2]], [[§30 Submanifolds#^lem-30-3|§30.3]]

![[m591-16-3.svg]]
*The fibre over $b$ and the model fibre. The trivialization $\phi_\alpha$ carries the submanifold $\pi^{-1}(b)$ onto the submanifold $\{b\} \times F$ — this is where the commuting triangle of [[§31 Fibrations#^def-31-1|Definition §31.1]] is used — and $\mathrm{pr}_2$ identifies that with $F$.*

This upgrades [[§31 Fibrations#^prop-31-1|Proposition §31.1]](1) from homeomorphic to diffeomorphic. Not every submersion has this property: its fibres are submanifolds, but they can change type from one point to another.

> [!example] Example §31.2: A Submersion That Is Not a Fibration
> Let $E = \mathbb{R}^2 \setminus \{(0, 1)\}$ and $\pi : E \to \mathbb{R}$, $\pi(x, y) = x$. Then $\pi$ is a surjective submersion, but not a fibration.

^ex-31-2

> [!proof]+ Proof
> *(Lecture 12.)* $\pi$ is the restriction of the projection $\mathbb{R}^2 \to \mathbb{R}$ to an open subset, so it is a submersion ([[§29 Submersions#^ex-29-1|Example §29.1]]), and it is onto. Its fibres are the vertical lines $\{x\} \times \mathbb{R}$ for $x \ne 0$, “except for one”: over $0$ the fibre is $\{0\} \times (\mathbb{R} \setminus \{1\})$, two half-lines — “it wants to be a vertical line, but there's a point missing.” If $\pi$ were a fibration with fibre $F$, all fibres would be diffeomorphic to $F$ ([[§31 Fibrations#^prop-31-2|Proposition §31.2]]), hence to each other; but $\{1\} \times \mathbb{R}$ is connected and $\{0\} \times (\mathbb{R} \setminus \{1\})$ is not, and connectedness is preserved by homeomorphisms.

^pf-ex-31-2

*Uses:* [[§29 Submersions#^ex-29-1|Ex. §29.1]], [[§31 Fibrations#^def-31-1|Def. §31.1]], [[§31 Fibrations#^prop-31-2|§31.2]], [[§13 Connected Spaces#^thm-13-3|590 §13.3]], [[§14 Connected Subspaces of ℝ#^cor-14-2|590 §14.2]]

![[m591-16-4.svg]]
*The punctured plane over the $x$-axis. Every fibre is a whole vertical line except the one over $0$, which is broken at the missing point into two half-lines. The fibres are all submanifolds ([[§30 Submanifolds#^cor-30-7|Corollary §30.7]]), but not all of the same type.*

A student asked the converse: if all the fibres of a surjective submersion are diffeomorphic to one manifold, must it be a fibration? Uribe: “I don't think that's true, but I don't have a quick example.” He answered it at the start of Lecture 13: yes when $\pi$ is proper, no in general ([[§31 Fibrations#^thm-31-3|Theorem §31.3]] and [[§31 Fibrations#^ex-31-4|Example §31.4]] below).

> [!example] Example §31.3: The Möbius Band
> The Möbius band fibres over its core circle, with an interval as fibre: “no matter where you cut it, it just looks like a [strip]. But globally, it's not a product.” Concretely, let $E = \big(\mathbb{R} \times (-1, 1)\big)/{\sim}$ with $(s, t) \sim (s + n, (-1)^n t)$ for $n \in \mathbb{Z}$, and $\pi[s, t] = [s] \in \mathbb{R}/\mathbb{Z} \cong S^1$.
>
> *Lee: Example 10.3*

^ex-31-3

*Status.* In lecture this was a picture, not a proof: the claims that $\pi$ is a fibration with fibre $(-1, 1)$, and that $E$ is not globally the product $S^1 \times (-1, 1)$, are stated, not proved, here. Over any arc of the circle shorter than the whole, the twist can be undone, which is the local product structure; the obstruction is global, and it is visible in the picture: the band has a single boundary curve, while the product $S^1 \times (-1, 1)$ closed up would have two. Lee's Möbius bundle takes the fibre $\mathbb{R}$ in place of $(-1, 1)$.

![[m591-16-5.svg]]
*Left: the strip $[0, 1] \times (-1, 1)$, ruled by its fibres, with the core circle in orange; glue the two ends with a half-twist, matching the arrows. Right: the band itself. Each grey segment is a fibre, lying over one point of the orange core circle, and the boundary is a single curve.*

> [!remark]- Connections
> - $E$ is the orbit space of $\mathbb{Z}$ acting on $\mathbb{R} \times (-1,1)$: [[§10 Group Actions and Orbit Spaces#^def-10-5|Def. §10.5]]; quotient spaces in 590: [[§12 Quotient Topology#^def-12-3|590 Def. §12.3]].

## When Is a Submersion a Fibration?

*Lecture 13 (Wed Sep 30). Uribe opened with the answer to the question left open in Lecture 12 — “I didn't know the answer right away. I thought the answer was no, and in fact the answer is no. But there's a partial yes.”*

> [!theorem] Theorem §31.3: Ehresmann's Theorem
> Let $\pi : E \to B$ be a surjective submersion which is *proper*: the preimage of every compact set is compact. If $B$ is connected, then $\pi$ is a fibration.

^thm-31-3

> [!proof]+ Proof (to be filled)
> Stated in Lecture 13, not proved: the proof uses connections, which the course does not cover. To be filled.

^pf-31-3

*Status.* Stated in Lecture 13, not proved: “we don't have time to do the proof, and it uses material that we're not going to cover called connections.” Uribe first recalled the case of a compact fibre, then the general statement for proper maps, which is the form given here. The intuition: a connection lets one lift a path from $b$ to $b'$ in the base to paths in $E$, and flow the fibre over $b$ onto the fibre over $b'$; properness is what lets the flow run for as long as needed, so that it identifies the fibres not just one at a time but over a whole neighbourhood — a local trivialization. The transcript renders the name as “Aristotle”; it is Ehresmann.

> [!remark]- Connections
> - Proper maps were defined earlier, for group actions: [[§10 Group Actions and Orbit Spaces#^def-10-6|Def. §10.6]]; compactness: [[§15 Compact Spaces|590 §15]].

> [!example] Example §31.4: All Fibres Diffeomorphic but Not a Fibration
> Let
>
> $$
> E = \big\{ (x, y, t) \in \mathbb{R}^3 : (x, y) \ne (0, 0), \ \text{and } (x, y) \ne (t, 0) \text{ if } t \ne 0, \ (x, y) \ne (1, 0) \text{ if } t = 0 \big\},
> $$
>
> and $\pi(x, y, t) = t$. Then $\pi : E \to \mathbb{R}$ is a surjective submersion, and every fibre is the plane minus two points:
>
> $$
> \pi^{-1}(t) \cong \begin{cases} \mathbb{R}^2 \setminus \{(0,0), (t,0)\}, & t \ne 0, \\ \mathbb{R}^2 \setminus \{(0,0), (1,0)\}, & t = 0, \end{cases}
> $$
>
> all diffeomorphic to one another. But $\pi$ is not a fibration.

^ex-31-4

*Uses:* [[§29 Submersions#^ex-29-1|Ex. §29.1]]

*Status.* Found for Uribe by ChatGPT, which reported that a human had posted it on a mathematics forum; given in lecture as a picture, without proof. *(Completion.)* $E$ is open in $\mathbb{R}^3$: its complement is the $t$-axis $\{(0,0,t)\}$, together with the line $\{(t, 0, t)\}$ and the single point $(1, 0, 0)$, a closed set. So $\pi$ is the restriction of a projection to an open set, hence a submersion ([[§29 Submersions#^ex-29-1|Example §29.1]]), and it is onto. Any two copies of the plane with two points removed are diffeomorphic by an affine map. That $\pi$ is not a fibration is stated, not proved, here. Uribe's intuition: as $t \to 0$ the missing point $(t, 0)$ “is colliding with $(0,0)$”, while over $t = 0$ the second missing point sits away at $(1, 0)$. He added that the example is subtler than it looks: with lines in place of planes the corresponding map would be locally trivial, and “it's the fact that you have [a] fundamental group that messes things up.”

![[m591-16-6.svg]]
*The fibres over a few values of $t$. The origin, grey, is missing from every fibre, and the missing points $(t, 0)$, red, lie on a line — dashed — which meets the line of origins exactly at $t = 0$: the collision. Over $t = 0$ (orange) the second missing point is $(1, 0)$, off that line. Each fibre on its own is a plane minus two points; what fails is the way they fit together near $t = 0$.*

**Transcription note.** Page 35 of the handwritten notes labels the second missing point over $t = 0$ as $(1, 1)$; it is $(1, 0)$.
