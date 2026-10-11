---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 38
tags: [differentiable-manifolds, math591]
---
← [[§37 Regular Submanifolds]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§39 Immersions]] →

*Stage: bundles — Submersions that are locally products.*

*References: Lee Ch. 10. Lectures 11–13.*

The submersions that look locally like the projection $U \times F \to U$. Their fibres are submanifolds ([[§37 Regular Submanifolds|§37]]), all copies of one fibre; the tangent bundle of the next section is the first major example.

## Fibrations

*Lecture 11. “An important class within the submersions.” Uribe introduced fibrations now because the tangent bundle, the cotangent bundle and vector bundles, coming soon, are all fibrations. The idea: surjective maps $\pi : M \to B$ that are locally like the projection $U \times F \to U$, with $U$ open in the **base** $B$ and $F$ a third, fixed manifold. There is a notation clash he apologized for — $F$ now names the fibre, not the map, which is called $\pi$.*

> [!definition] Definition §38.1: Fibration
> Let $M$, $B$ and $F$ be smooth manifolds and $\pi : M \to B$ smooth. Then $\pi$ is a **fibration with fibre $F$** if there are an open cover $\{U_\alpha\}_{\alpha \in A}$ of $B$ and, for each $\alpha$, a diffeomorphism
>
> $$
> \phi_\alpha : \pi^{-1}(U_\alpha) \longrightarrow U_\alpha \times F \qquad \text{with} \qquad \mathrm{pr}_1 \circ \phi_\alpha = \pi|_{\pi^{-1}(U_\alpha)},
> $$
>
> where $\pi^{-1}(U_\alpha)$ is an [[§37 Regular Submanifolds#^def-37-1|open submanifold]] of $M$ (Definition §37.1), $U_\alpha \times F$ a product manifold ([[§19 Smooth Functions and Smooth Maps#^def-19-7|Definition §19.7]]) — equivalently, an open submanifold of $B \times F$ ([[§37 Regular Submanifolds#^prop-37-1|Proposition §37.1]]) — and
>
> $$
> \mathrm{pr}_1 : U_\alpha \times F \to U_\alpha, \qquad \mathrm{pr}_1(b, y) = b ,
> $$
>
> the [[§3 Subspaces and Products#^def-3-4|projection]] onto the first factor (Definition §3.4; written $\mathrm{pr}_1$ rather than $\pi_1$ because $\pi$ already names the fibration), which is smooth ([[§19 Smooth Functions and Smooth Maps#^prop-19-10|Proposition §19.10]]). The condition $\mathrm{pr}_1 \circ \phi_\alpha = \pi|_{\pi^{-1}(U_\alpha)}$ says that $\phi_\alpha$ keeps the base point: for $x \in \pi^{-1}(U_\alpha)$ the first component of $\phi_\alpha(x)$ is $\pi(x)$, that is, $\phi_\alpha(x) = \big(\pi(x), y\big)$ for some $y \in F$. The $\phi_\alpha$ are called **local trivializations**. $M$ is the **total space** and $B$ the **base**.
>
> *Lee: Ch. 10, smooth fiber bundles*

^def-38-1

> [!remark]- Connections
> - The first major example: [[§47 The Tangent Bundle#^cor-47-3|the tangent bundle, §47.3]]; sections of a fibration: [[§38 Fibrations#^def-38-3|Def. §38.3]].
> - The topological analogue with discrete fibre: [[§31 Covering Spaces#^def-31-2|covering maps, 590 Def. §31.2]]; in 591, [[§35 Local Diffeomorphisms#^rem-35-2|Remark: Covering Maps (§35)]].

![[m591-16-1.svg]]
*The local trivialization $\phi_\alpha$ over $U_\alpha$: the triangle commutes, $\mathrm{pr}_1 \circ \phi_\alpha = \pi|$.*

The diagram *commutes*. A student asked what that means; Uribe: “whenever you have a diagram … all the compositions that you can construct from one place to another give you the same answer.” Here there are two routes from $\pi^{-1}(U_\alpha)$ to $U_\alpha$, and they agree: $\mathrm{pr}_1 \circ \phi_\alpha = \pi|$. Concretely, $\phi_\alpha(p) = (\pi(p), \ast)$ — its first component *is* $\pi(p)$, and only the second, a point of $F$, is new information.

![[m591-16-2.svg]]
*Uribe's cartoon, and why it matters: “these cartoons are incredibly important.” On the left, the global product $B \times F$, with each fibre $\{b\} \times F$ standing over its point. On the right, a total space that need not be a product: its fibres may twist as they travel over $B$. But over each $U_\alpha$ the part $\pi^{-1}(U_\alpha)$ is identified by $\phi_\alpha$ with the straight product $U_\alpha \times F$, and the identification respects the base points, which is the commuting diagram.*

> [!definition] Definition §38.2: Trivial Fibration
> A fibration $\pi : M \to B$ with fibre $F$ (Definition [[§38 Fibrations#^def-38-1|§38.1]]) is **trivial** if it has a local trivialization over all of $B$: a diffeomorphism $\phi : M \to B \times F$ with $\mathrm{pr}_1 \circ \phi = \pi$.

^def-38-2

> [!example] Example §38.1: Product Fibrations
> *(Not from lecture.)* For smooth manifolds $B$ and $F$, the projection $\mathrm{pr}_1 : B \times F \to B$, $\mathrm{pr}_1(b, y) = b$, is a trivial fibration with fibre $F$, with one open set $U = B$ and one local trivialization $\phi = \mathrm{id}_{B \times F}$. Every trivial fibration is this one up to the diffeomorphism $\phi$: if $\phi : M \to B \times F$ is a global trivialization of $\pi$, then $\pi = \mathrm{pr}_1 \circ \phi$.

^ex-38-1

> [!proof]+ Proof
> Check Definition [[§38 Fibrations#^def-38-1|§38.1]] with $M = B \times F$ and $\pi = \mathrm{pr}_1$. The map $\mathrm{pr}_1$ is smooth (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]). The single set $U = B$ covers $B$, and $\mathrm{pr}_1^{-1}(B) = B \times F$. The identity $\mathrm{id}_{B \times F}$ is a diffeomorphism $\mathrm{pr}_1^{-1}(B) \to B \times F$, and $\mathrm{pr}_1 \circ \mathrm{id}_{B \times F} = \mathrm{pr}_1 = \pi|_{\pi^{-1}(B)}$. So $\mathrm{pr}_1$ is a fibration with fibre $F$, trivial by Definition [[§38 Fibrations#^def-38-2|§38.2]]. The last sentence is the condition $\mathrm{pr}_1 \circ \phi = \pi$ of that definition.

^pf-ex-38-1

*Uses:* [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§38 Fibrations#^def-38-2|Def. §38.2]]

> [!remark] Remark: Where Explicit Trivializations Come From
> *(Not from lecture.)* In Definition [[§38 Fibrations#^def-38-1|§38.1]] the local trivializations $\phi_\alpha$ are part of the data: a fibration has some, and nothing in the definition says how to find them — the charts of the base $B$ carry no information about the total space or the fibre. So a fibration is a map that is, over each $U_\alpha$, a product fibration (Example [[§38 Fibrations#^ex-38-1|§38.1]]), but there is no general formula for $\phi_\alpha$. Explicit trivializations come from extra structure:
> - for the tangent and cotangent bundles ([[§47 The Tangent Bundle|§47]], [[§48 The Cotangent Bundle|§48]]), a chart $(U, \varphi = (x^1, \ldots, x^m))$ of $M$ also gives every fibre a basis, $\partial/\partial x^i|_p$ of $T_pM$ and $dx^i|_p$ of $T_p^{\ast}M$ (Theorem [[§29 Coordinate Derivations and the Basis Theorem#^thm-29-5|§29.5]], Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]), and writing a vector or covector in that basis is the trivialization, $v \mapsto (p, v^1, \ldots, v^m)$ (Definition [[§47 The Tangent Bundle#^def-47-4|§47.4]]) and $\xi \mapsto (p, \xi_1, \ldots, \xi_m)$ (Definition [[§48 The Cotangent Bundle#^def-48-4|§48.4]]);
> - for a quotient by a group action, a description of the total space as a quotient gives them, as for the Möbius band (Proposition [[§38 Fibrations#^prop-38-3|§38.3]] below);
> - for the Hopf fibration, local sections give them (Proposition [[§42 Projective Spaces and the Hopf Fibration#^prop-42-1|§42.1]]).
>
> Ehresmann's theorem (Theorem [[§38 Fibrations#^thm-38-4|§38.4]]) produces trivializations for proper submersions, but not by a formula.

^rem-38-1

> [!theorem] Proposition §38.1: Fibres and Fibrations
> Let $\pi : M \to B$ be a fibration with fibre $F$.
> 1. For every $b \in B$, the fibre $\pi^{-1}(b)$ is homeomorphic to $F$: every fibre is a copy of the model fibre.
> 2. $\pi$ is a submersion, and it is surjective if $F \ne \emptyset$.
> 3. $\pi$ is an open map.

^prop-38-1

> [!proof]+ Proof
> *(Stated in lecture; (2) as “chain rule and stuff”.)* Throughout, recall from Definition [[§38 Fibrations#^def-38-1|§38.1]] that the sets $U_\alpha$ cover $B$, that each $\pi^{-1}(U_\alpha)$ is open in $M$ (the preimage of an open set under the continuous map $\pi$), and that on it $\pi = \mathrm{pr}_1 \circ \phi_\alpha$ — the commuting diagram.
>
> *(1)* Fix $b \in B$ and choose $\alpha$ with $b \in U_\alpha$; then $\pi^{-1}(b) \subseteq \pi^{-1}(U_\alpha)$, the domain of $\phi_\alpha$.
>
> *$\phi_\alpha$ maps $\pi^{-1}(b)$ onto $\mathrm{pr}_1^{-1}(b) = \{b\} \times F$.* This is where the commuting diagram and the bijectivity of $\phi_\alpha$ are used. If $x \in \pi^{-1}(b)$, then $\mathrm{pr}_1(\phi_\alpha(x)) = \pi(x) = b$, so $\phi_\alpha(x) \in \{b\} \times F$. Conversely, if $(b, f) \in \{b\} \times F \subseteq U_\alpha \times F$, then $x = \phi_\alpha^{-1}(b, f)$ is defined, $\phi_\alpha$ being a bijection onto $U_\alpha \times F$, and
>
> $$
> \pi(x) = \mathrm{pr}_1\big(\phi_\alpha(x)\big) = \mathrm{pr}_1(b, f) = b ,
> $$
>
> so $x \in \pi^{-1}(b)$ with $\phi_\alpha(x) = (b, f)$. Thus $\phi_\alpha$ restricts to a bijection $\pi^{-1}(b) \to \{b\} \times F$.
>
> *The restriction is a homeomorphism with the subspace topologies.* $\phi_\alpha$ is a diffeomorphism, in particular a homeomorphism, so its restriction to the subset $\pi^{-1}(b)$ is a homeomorphism onto its image $\{b\} \times F$ (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](3)). The subspace topology of $\pi^{-1}(b)$ is the same whether it is taken from $\pi^{-1}(U_\alpha)$ or from $M$, since $\big(O \cap \pi^{-1}(U_\alpha)\big) \cap \pi^{-1}(b) = O \cap \pi^{-1}(b)$ for every $O$ open in $M$.
>
> *$\{b\} \times F$ is a copy of $F$.* The map $\{b\} \times F \to F$, $(b, f) \mapsto f$, is a homeomorphism, with inverse $f \mapsto (b, f)$. The first is the restriction of the projection $\mathrm{pr}_2$, which is continuous; the second is continuous into $U_\alpha \times F$ because its two components, the constant map $b$ and $\mathrm{id}_F$, are continuous (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](4)), hence continuous into the subspace $\{b\} \times F$ (Proposition [[§3 Subspaces and Products#^prop-3-3|§3.3]](2)); and the two maps are inverse to each other. Composing, $\pi^{-1}(b) \to \{b\} \times F \to F$ is a homeomorphism.
>
> *(2)* *$\pi$ is a submersion.* Fix $p \in M$; we show that $\pi_{\ast p}$ is onto $T_{\pi(p)}B$. Choose $\alpha$ with $\pi(p) \in U_\alpha$, let $W = \pi^{-1}(U_\alpha)$, an open submanifold of $M$ containing $p$, and write $\pi|_W : W \to U_\alpha$ for the restriction. On the open set $W$, $\pi|_W = \mathrm{pr}_1 \circ \phi_\alpha$; by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]),
>
> $$
> (\pi|_W)_{\ast p} = (\mathrm{pr}_1)_{\ast\phi_\alpha(p)} \circ (\phi_\alpha)_{\ast p} ,
> $$
>
> a composite of an isomorphism and a surjection. Indeed $(\phi_\alpha)_{\ast p}$ is an isomorphism because $\phi_\alpha$ is a diffeomorphism (Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]), and $(\mathrm{pr}_1)_{\ast\phi_\alpha(p)}$ is onto because the projection of the product manifold $U_\alpha \times F$ onto its first factor is a submersion (Example [[§36 Submersions#^ex-36-2|§36.2]], with $M_1 = U_\alpha$ and $M_2 = F$). So, given $w \in T_{\pi(p)}U_\alpha$, choose $u$ with $(\mathrm{pr}_1)_{\ast\phi_\alpha(p)}u = w$ and put $v = (\phi_\alpha)_{\ast p}^{-1}u$; then $(\pi|_W)_{\ast p}v = w$, and $(\pi|_W)_{\ast p}$ is onto.
>
> It remains to pass from $\pi|_W$ to $\pi$. With the inclusions $\iota_W : W \hookrightarrow M$ and $\iota_{U_\alpha} : U_\alpha \hookrightarrow B$ we have $\pi \circ \iota_W = \iota_{U_\alpha} \circ \pi|_W$, so by the Chain Rule
>
> $$
> \pi_{\ast p} \circ (\iota_W)_{\ast p} = (\iota_{U_\alpha})_{\ast\pi(p)} \circ (\pi|_W)_{\ast p} .
> $$
>
> The right side is onto $T_{\pi(p)}B$, because $(\iota_{U_\alpha})_{\ast\pi(p)}$ is an isomorphism (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]) and $(\pi|_W)_{\ast p}$ is onto. Hence the left side is onto, and therefore so is $\pi_{\ast p}$. As $p$ was arbitrary, $\pi$ is a submersion (Definition [[§36 Submersions#^def-36-1|§36.1]]).
>
> *$\pi$ is surjective if $F \neq \emptyset$.* Every $b$ lies in some $U_\alpha$, and its fibre is a copy of $F$ by (1), nonempty if $F$ is; any $x \in \pi^{-1}(b)$ has $\pi(x) = b$.
>
> *(3)* By (2), $\pi$ is a submersion, so by Corollary [[§36 Submersions#^cor-36-6|§36.6]] $\pi(O)$ is open in $B$ for every open $O \subseteq M$: $\pi$ is an open map.

^pf-38-1

*Uses:* [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§36 Submersions#^def-36-1|Def. §36.1]], [[§36 Submersions#^ex-36-2|Ex. §36.2]], [[§36 Submersions#^cor-36-6|§36.6]], [[§10 Continuous Functions#^prop-10-3|590 §10.3]], [[§3 Subspaces and Products#^prop-3-3|§3.3]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]

The Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$, the first example of a fibration, and its local but not global sections are collected in [[§42 Projective Spaces and the Hopf Fibration|§42]].

> [!remark] Remark: What Comes Next
> Tangent bundles, cotangent bundles and vector bundles are fibrations “with additional structure, where the fibres are vector spaces.” The basic notion of fibration is more general: its fibre $F$ is any manifold.

^rem-38-2

> [!remark]- Connections
> - [[§47 The Tangent Bundle#^cor-47-3|The tangent bundle is a fibration, §47.3]]; [[§48 The Cotangent Bundle#^def-48-1|the cotangent bundle, Def. §48.1]]; [[§47 The Tangent Bundle#^rem-47-2|Remark: Vector Bundles (§47)]].

**Transcription note.** Stating the idea of a fibration, Uribe first said “$U$ open in $M$”; a student corrected it to open in $B$, as in the definition.

## Fibres and Examples

*Lecture 12. Uribe changed the notation once more “to conform to more general usage”: the fibration is $\pi : E \to B$, with total space $E$, base $B$, and fibre $F$ — the definition as before ([[§38 Fibrations#^def-38-1|Definition §38.1]]), with $E$ in place of $M$.*

> [!theorem] Proposition §38.2: Fibres Are Copies of the Model Fibre
> Let $\pi : E \to B$ be a fibration with fibre $F$ and $b \in B$. Then $\pi^{-1}(b)$ is a regular submanifold of $E$, and for every $\alpha$ with $b \in U_\alpha$ the local trivialization $\phi_\alpha$ restricts to a diffeomorphism
>
> $$
> \pi^{-1}(b) \longrightarrow \{b\} \times F \cong F .
> $$

^prop-38-2

> [!proof]+ Proof
> *(Claimed in Lecture 12 — “I claim that they are diffeomorphic to this fibre, to the third manifold that is sitting outside, looking over [the] landscape”; filled in.)* Three things are claimed: $\pi^{-1}(b)$ is a regular submanifold of $E$; $\phi_\alpha$ restricts to a diffeomorphism $\pi^{-1}(b) \to \{b\} \times F$; and $\{b\} \times F$ is diffeomorphic to $F$.
>
> *The two submanifolds.* $\pi$ is a submersion (Proposition [[§38 Fibrations#^prop-38-1|§38.1]](2)), so its fibre $\pi^{-1}(b)$ is a regular submanifold of $E$ (Corollary [[§37 Regular Submanifolds#^cor-37-10|§37.10]]). Likewise the projection $\mathrm{pr}_1 : U_\alpha \times F \to U_\alpha$ is a submersion (Example [[§36 Submersions#^ex-36-2|§36.2]]), so its fibre $\{b\} \times F = \mathrm{pr}_1^{-1}(b)$ is a regular submanifold of $U_\alpha \times F$ (Corollary [[§37 Regular Submanifolds#^cor-37-10|§37.10]] again). Both carry their induced smooth structures (Proposition [[§37 Regular Submanifolds#^prop-37-3|§37.3]]).
>
> *A bijection.* Because the diagram commutes, $\phi_\alpha$ maps $\pi^{-1}(b)$ bijectively onto $\{b\} \times F$: this is the first step of the proof of Proposition [[§38 Fibrations#^prop-38-1|§38.1]](1), namely $\mathrm{pr}_1(\phi_\alpha(x)) = \pi(x) = b$ for $x \in \pi^{-1}(b)$, and $\pi\big(\phi_\alpha^{-1}(b, f)\big) = \mathrm{pr}_1(b, f) = b$ for $(b, f) \in \{b\} \times F$. Write $\Phi : \pi^{-1}(b) \to \{b\} \times F$ for the restriction of $\phi_\alpha$; its inverse is the restriction of $\phi_\alpha^{-1}$ to $\{b\} \times F$.
>
> *$\Phi$ is smooth.* The inclusion $\iota : \pi^{-1}(b) \hookrightarrow E$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)). It takes values in the open subset $\pi^{-1}(U_\alpha)$, so it is also smooth as a map into the open submanifold $\pi^{-1}(U_\alpha)$, whose smooth charts are the charts of $E$ with domain inside $\pi^{-1}(U_\alpha)$. Hence $\phi_\alpha \circ \iota : \pi^{-1}(b) \to U_\alpha \times F$ is smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]). It takes values in the submanifold $\{b\} \times F$, so it is smooth as a map into $\{b\} \times F$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)); that map is $\Phi$.
>
> *$\Phi^{-1}$ is smooth.* The inclusion $\iota' : \{b\} \times F \hookrightarrow U_\alpha \times F$ is smooth (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)), and $\phi_\alpha^{-1} \circ \iota'$ is smooth into $\pi^{-1}(U_\alpha)$, hence into $E$, the inclusion of an open submanifold being smooth (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]). It takes values in the submanifold $\pi^{-1}(b)$, so it is smooth as a map into $\pi^{-1}(b)$ (Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2)); that map is $\Phi^{-1}$. So $\Phi$ is a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]): the restriction and its inverse are smooth as maps into $U_\alpha \times F$ and into $E$, hence smooth into the submanifolds $\{b\} \times F$ and $\pi^{-1}(b)$.
>
> *$\{b\} \times F \cong F$.* Finally $\{b\} \times F \to F$, $(b, f) \mapsto f$, is a diffeomorphism by the same lemma, with inverse $f \mapsto (b, f)$. Explicitly: the first map is $\mathrm{pr}_2 \circ \iota'$, smooth because $\mathrm{pr}_2$ and $\iota'$ are (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](1)). The second is the slice inclusion $\iota^{b} : F \to U_\alpha \times F$, $f \mapsto (b, f)$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]]), smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]; it takes values in $\{b\} \times F$, so it is smooth into $\{b\} \times F$ by Lemma [[§37 Regular Submanifolds#^lem-37-5|§37.5]](2). The two maps are inverse to each other. Composing with $\Phi$ gives the diffeomorphism $\pi^{-1}(b) \to \{b\} \times F \cong F$.

^pf-38-2

*Uses:* [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§38 Fibrations#^prop-38-1|§38.1]], [[§37 Regular Submanifolds#^cor-37-10|§37.10]], [[§36 Submersions#^ex-36-2|Ex. §36.2]], [[§37 Regular Submanifolds#^lem-37-5|§37.5]], [[§37 Regular Submanifolds#^prop-37-3|§37.3]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]]

![[m591-16-3.svg]]
*The fibre over $b$ and the model fibre. The trivialization $\phi_\alpha$ carries the submanifold $\pi^{-1}(b)$ onto the submanifold $\{b\} \times F$ — this is where the commuting triangle of [[§38 Fibrations#^def-38-1|Definition §38.1]] is used — and $\mathrm{pr}_2$ identifies that with $F$.*

This upgrades [[§38 Fibrations#^prop-38-1|Proposition §38.1]](1) from homeomorphic to diffeomorphic. Not every submersion has this property: its fibres are submanifolds, but they can change type from one point to another.

> [!example] Example §38.2: A Submersion That Is Not a Fibration
> Let $E = \mathbb{R}^2 \setminus \{(0, 1)\}$ and $\pi : E \to \mathbb{R}$, $\pi(x, y) = x$. Then $\pi$ is a surjective submersion, but not a fibration.

^ex-38-2

> [!proof]+ Proof
> *(Lecture 12.)* Three things are claimed: $\pi$ is a submersion, it is onto, and it is not a fibration.
>
> *Submersion.* $E$ is open in $\mathbb{R}^2$, the complement of the closed set $\{(0, 1)\}$. $\pi$ is the restriction of the projection $\mathrm{pr} : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ to an open subset, so it is a submersion (Example [[§36 Submersions#^ex-36-1|§36.1]], with $k = l = 1$). In detail: with $\iota_E : E \hookrightarrow \mathbb{R}^2$ the inclusion, $\pi = \mathrm{pr} \circ \iota_E$, so by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) $\pi_{\ast q} = \mathrm{pr}_{\ast q} \circ (\iota_E)_{\ast q}$ for $q \in E$; here $(\iota_E)_{\ast q}$ is an isomorphism (Lemma [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]]) and $\mathrm{pr}_{\ast q}$ is onto, so $\pi_{\ast q}$ is onto.
>
> *Onto.* For $x \in \mathbb{R}$, the point $(x, 0)$ is not $(0, 1)$, so it lies in $E$, and $\pi(x, 0) = x$.
>
> *The fibres.* Its fibres are the vertical lines $\{x\} \times \mathbb{R}$ for $x \ne 0$, “except for one”: over $0$ the fibre is $\{0\} \times (\mathbb{R} \setminus \{1\})$, two half-lines — “it wants to be a vertical line, but there's a point missing.” Indeed $\pi^{-1}(x) = \{(x, y) : (x, y) \neq (0, 1)\}$, and the excluded point has $x = 0$.
>
> *Not a fibration.* If $\pi$ were a fibration with fibre $F$, all fibres would be diffeomorphic to $F$ (Proposition [[§38 Fibrations#^prop-38-2|§38.2]]), hence to each other (compose one diffeomorphism with the inverse of the other), and in particular homeomorphic. But $\{1\} \times \mathbb{R}$ is connected and $\{0\} \times (\mathbb{R} \setminus \{1\})$ is not, and connectedness is preserved by homeomorphisms. In detail: $\{1\} \times \mathbb{R}$ is homeomorphic to $\mathbb{R}$ by $(1, y) \mapsto y$, hence connected (Proposition [[§1 Point-Set Topology Review#^prop-1-7|§1.7]](4)). $\{0\} \times (\mathbb{R} \setminus \{1\})$ is the union of the two disjoint nonempty sets $\{0\} \times (-\infty, 1)$ and $\{0\} \times (1, \infty)$, each open in it, being its intersection with the open half-plane $\{y < 1\}$, resp. $\{y > 1\}$; so it is not connected. And the image of a connected space under a homeomorphism, a continuous map, is connected (Proposition [[§1 Point-Set Topology Review#^prop-1-7|§1.7]](1)).

^pf-ex-38-2

*Uses:* [[§36 Submersions#^ex-36-1|Ex. §36.1]], [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§38 Fibrations#^prop-38-2|§38.2]], [[§15 Connected Spaces#^thm-15-3|590 §15.3]], [[§16 Connected Subspaces of ℝ#^cor-16-2|590 §16.2]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^lem-28-8|§28.8]], [[§1 Point-Set Topology Review#^prop-1-7|§1.7]]

![[m591-16-4.svg]]
*The punctured plane over the $x$-axis. Every fibre is a whole vertical line except the one over $0$, which is broken at the missing point into two half-lines. The fibres are all submanifolds ([[§37 Regular Submanifolds#^cor-37-10|Corollary §37.10]]), but not all of the same type.*

A student asked the converse: if all the fibres of a surjective submersion are diffeomorphic to one manifold, must it be a fibration? Uribe: “I don't think that's true, but I don't have a quick example.” He answered it at the start of Lecture 13: yes when $\pi$ is proper, no in general ([[§38 Fibrations#^thm-38-4|Theorem §38.4]] and [[§38 Fibrations#^ex-38-4|Example §38.4]] below).

> [!example] Example §38.3: The Möbius Band
> The Möbius band fibres over its core circle, with an interval as fibre: “no matter where you cut it, it just looks like a [strip]. But globally, it's not a product.” Concretely, let $E = \big(\mathbb{R} \times (-1, 1)\big)/{\sim}$ with $(s, t) \sim (s + n, (-1)^n t)$ for $n \in \mathbb{Z}$, and $\pi[s, t] = [s] \in \mathbb{R}/\mathbb{Z} \cong S^1$.
>
> *Lee: Example 10.3*

^ex-38-3

*Status.* In lecture this was a picture, not a proof: the claim that $\pi$ is a fibration with fibre $(-1, 1)$ is proved, with explicit local trivializations, in [[§38 Fibrations#^prop-38-3|Proposition §38.3]] below; the claim that $E$ is not globally the product $S^1 \times (-1, 1)$ is stated, not proved, here. Over any arc of the circle shorter than the whole, the twist can be undone, which is the local product structure; the obstruction is global, and it is visible in the picture: the band has a single boundary curve, while the product $S^1 \times (-1, 1)$ closed up would have two. Lee's Möbius bundle takes the fibre $\mathbb{R}$ in place of $(-1, 1)$.

![[m591-16-5.svg]]
*Left: the strip $[0, 1] \times (-1, 1)$, ruled by its fibres, with the core circle in orange; glue the two ends with a half-twist, matching the arrows. Right: the band itself. Each grey segment is a fibre, lying over one point of the orange core circle, and the boundary is a single curve.*

> [!remark]- Connections
> - $E$ is the orbit space of $\mathbb{Z}$ acting on $\mathbb{R} \times (-1,1)$: [[§13 Group Actions and Orbit Spaces#^def-13-5|Def. §13.5]]; quotient spaces in 590: [[§13 Quotient Topology#^def-13-3|590 Def. §13.3]].

> [!theorem] Proposition §38.3: The Möbius Band Is a Fibration
> Let $E = \big(\mathbb{R} \times (-1, 1)\big)/{\sim}$ and $\pi[s, t] = [s]$ be as in Example [[§38 Fibrations#^ex-38-3|§38.3]], let $q : \mathbb{R} \times (-1, 1) \to E$ be the quotient map, and identify $\mathbb{R}/\mathbb{Z}$ with $S^1$ by $h[s] = (\cos 2\pi s, \sin 2\pi s)$. For $a \in \{0, \tfrac12\}$ put $I_a = (a, a + 1)$, $U_a = \{[s] : s \in I_a\} \subseteq \mathbb{R}/\mathbb{Z}$ and $W_a = q\big(I_a \times (-1, 1)\big) \subseteq E$.
>
> 1. $E$ is a topological $2$-manifold, and the two maps $\psi_a = \big(q|_{I_a \times (-1,1)}\big)^{-1} : W_a \to I_a \times (-1, 1)$ form a smooth atlas, with transition
>
> $$
> \psi_{1/2} \circ \psi_0^{-1}(s, t) = \begin{cases} (s, t), & \tfrac12 < s < 1, \\ (s + 1, -t), & 0 < s < \tfrac12. \end{cases}
> $$
>
> 2. With this smooth structure $\pi$ is smooth, $\pi^{-1}(U_a) = W_a$, and
>
> $$
> \phi_a : \pi^{-1}(U_a) \to U_a \times (-1, 1), \qquad \phi_a[s, t] = \big([s], t\big) \quad (s \in I_a),
> $$
>
> are local trivializations. So $\pi$ is a fibration with fibre $(-1, 1)$.
> 3. On $U_0 \cap U_{1/2}$ the two trivializations differ by a sign on one arc:
>
> $$
> \phi_{1/2} \circ \phi_0^{-1}\big([s], t\big) = \begin{cases} \big([s], t\big), & \tfrac12 < s < 1, \\ \big([s], -t\big), & 0 < s < \tfrac12. \end{cases}
> $$

^prop-38-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Write $g_n(s, t) = \big(s + n, (-1)^n t\big)$ for $n \in \mathbb{Z}$, so that $(s, t) \sim (s', t')$ exactly when $(s', t') = g_n(s, t)$ for some $n$. Each $g_n$ is a homeomorphism of $\mathbb{R} \times (-1, 1)$, with inverse $g_{-n}$, since $g_n \circ g_m = g_{n+m}$ and $g_0 = \mathrm{id}$.
>
> *$q$ is open.* For $O$ open in $\mathbb{R} \times (-1, 1)$, the saturation $q^{-1}(q(O)) = \bigcup_{n \in \mathbb{Z}} g_n(O)$ is a union of open sets, so $q(O)$ is open in the quotient topology (Definition [[§4 Quotient Spaces and Open Maps#^def-4-2|§4.2]]).
>
> *$q$ restricted to $I_a \times (-1, 1)$.* It is injective: if $q(s, t) = q(s', t')$ with $s, s' \in I_a$, then $(s', t') = g_n(s, t)$, so $s' - s = n$ is an integer with $|s' - s| < 1$, hence $n = 0$ and $(s', t') = (s, t)$. It is continuous, as a restriction of $q$, and open, since an open subset of $I_a \times (-1, 1)$ is open in $\mathbb{R} \times (-1, 1)$ and $q$ is open. So it is a homeomorphism onto the open set $W_a$, and $\psi_a$ is a homeomorphism of $W_a$ onto the open subset $I_a \times (-1, 1)$ of $\mathbb{R}^2$.
>
> *(1) $E$ is a topological $2$-manifold.* The sets $W_0, W_{1/2}$ cover $E$: every $s \in \mathbb{R}$ has $s - n \in (0, 1)$ for some $n \in \mathbb{Z}$ unless $s$ is an integer, and then $s - n = 1 \in I_{1/2}$ for $n = s - 1$; and $q(s, t) = q\big(g_{-n}(s, t)\big)$. *Hausdorff:* let $x \ne y$ in $E$. If both lie in one $W_a$, separate them there, $W_a$ being homeomorphic to a subset of $\mathbb{R}^2$ and open in $E$. Otherwise one lies in $W_0 \setminus W_{1/2} = q\big(\{\tfrac12\} \times (-1, 1)\big)$ and the other in $W_{1/2} \setminus W_0 = q\big(\{1\} \times (-1, 1)\big)$; then $q\big((\tfrac14, \tfrac34) \times (-1, 1)\big)$ and $q\big((\tfrac34, \tfrac54) \times (-1, 1)\big)$ are open neighbourhoods of them, disjoint because two of their points with first coordinates $s \in (\tfrac14, \tfrac34)$, $s' \in (\tfrac34, \tfrac54)$ have $0 < s' - s < 1$, not an integer. *Second countable:* each $W_a$ has a countable basis of sets open in $W_a$, hence in $E$, and the union of the two bases is a countable basis of $E$. With the charts $\psi_a$, $E$ is a topological $2$-manifold (Definition [[§2 Topological Manifolds#^def-2-2|§2.2]]).
>
> *(1) The transition.* $W_0 \cap W_{1/2} = q\big(((0, \tfrac12) \cup (\tfrac12, 1)) \times (-1, 1)\big)$. Let $(s, t) \in \psi_0(W_0 \cap W_{1/2})$. If $\tfrac12 < s < 1$, then $s \in I_{1/2}$ and $\psi_{1/2}(q(s, t)) = (s, t)$. If $0 < s < \tfrac12$, then $q(s, t) = q\big(g_1(s, t)\big) = q(s + 1, -t)$ with $s + 1 \in I_{1/2}$, so $\psi_{1/2}(q(s, t)) = (s + 1, -t)$. Both branches are smooth, and so is the inverse, $(s, t) \mapsto (s, t)$ or $(s - 1, -t)$. So the two charts are compatible (Definition [[§17 Differentiable Structures#^def-17-4|§17.4]]) and form a smooth atlas (Theorem [[§17 Differentiable Structures#^thm-17-5|§17.5]]).
>
> *The base.* $h$ is well defined and bijective because $(\cos 2\pi s, \sin 2\pi s)$ depends exactly on $s$ modulo $1$; $\mathbb{R}/\mathbb{Z}$ carries the topology and smooth structure of $S^1$ transported along $h$ (Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-7|§19.7]]). For $s \in I_0 = (0, 1)$ the angle $2\pi s$ lies in $(0, 2\pi)$, and for $s \in I_{1/2}$ in $(\pi, 3\pi)$; so the maps $\chi_a : U_a \to I_a$, $\chi_a[s] = s$ ($s \in I_a$), are $\chi_0 = \tfrac{1}{2\pi}\,\varphi_a \circ h$ and $\chi_{1/2} = \tfrac{1}{2\pi}\,\varphi_b \circ h$, with $\varphi_a, \varphi_b$ the angle charts of Example [[§17 Differentiable Structures#^ex-17-4|§17.4]]. Rescaling by the diffeomorphism $\theta \mapsto \theta/2\pi$ of $\mathbb{R}$ keeps a chart in the smooth structure (as in the proof of Proposition [[§37 Regular Submanifolds#^prop-37-2|§37.2]]), so $\chi_0, \chi_{1/2}$ are smooth charts of $\mathbb{R}/\mathbb{Z}$ with domains $U_0, U_{1/2}$.
>
> *(2) $\pi$ is smooth and $\pi^{-1}(U_a) = W_a$.* $\pi$ is well defined, since $\pi[g_n(s, t)] = [s + n] = [s]$. If $[s] \in U_a$ then $s - n \in I_a$ for some $n$ and $q(s, t) = q(g_{-n}(s, t)) \in W_a$; conversely $\pi(W_a) \subseteq U_a$. So $\pi^{-1}(U_a) = W_a$, and in the charts $\psi_a$ and $\chi_a$,
>
> $$
> \chi_a \circ \pi \circ \psi_a^{-1}(s, t) = \chi_a[s] = s \qquad \big((s, t) \in I_a \times (-1, 1)\big),
> $$
>
> a smooth map. The $W_a$ cover $E$, so $\pi$ is smooth (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-3|§19.3]], Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]]).
>
> *(2) The trivializations.* $\phi_a = (\chi_a^{-1} \times \mathrm{id}) \circ \psi_a$, since $\psi_a[s, t] = (s, t)$ and $\chi_a^{-1}(s) = [s]$ for $s \in I_a$. Here $\psi_a : W_a \to I_a \times (-1, 1)$ is a diffeomorphism, a chart of the open submanifold $W_a$ (Proposition [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]]), and $\chi_a^{-1} \times \mathrm{id} : I_a \times (-1, 1) \to U_a \times (-1, 1)$ is a diffeomorphism, with inverse $\chi_a \times \mathrm{id}$, both having the identity as coordinate representation in the product chart $(U_a \times (-1, 1), \chi_a \times \mathrm{id})$. So $\phi_a$ is a diffeomorphism, and $\mathrm{pr}_1 \circ \phi_a[s, t] = [s] = \pi[s, t]$. With the open cover $\{U_0, U_{1/2}\}$ of $\mathbb{R}/\mathbb{Z}$, Definition [[§38 Fibrations#^def-38-1|§38.1]] holds with fibre $(-1, 1)$.
>
> *(3)* Let $[s] \in U_0 \cap U_{1/2}$ with $s \in I_0$. Then $\phi_0^{-1}([s], t) = q(s, t)$, and by the transition in (1), $q(s, t) = q(s, t)$ with $s \in I_{1/2}$ if $\tfrac12 < s < 1$, and $q(s, t) = q(s + 1, -t)$ with $s + 1 \in I_{1/2}$ if $0 < s < \tfrac12$. Applying $\phi_{1/2}$ gives $([s], t)$ in the first case and $([s + 1], -t) = ([s], -t)$ in the second.

^pf-38-3

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§17 Differentiable Structures#^def-17-4|Def. §17.4]], [[§17 Differentiable Structures#^thm-17-5|§17.5]], [[§19 Smooth Functions and Smooth Maps#^prop-19-7|§19.7]], [[§17 Differentiable Structures#^ex-17-4|Ex. §17.4]], [[§37 Regular Submanifolds#^prop-37-2|§37.2]], [[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]], [[§19 Smooth Functions and Smooth Maps#^prop-19-2|§19.2]], [[§28 Derivations and the Abstract Tangent Space#^prop-28-9|§28.9]], [[§38 Fibrations#^def-38-1|Def. §38.1]]

The sign in (3) is the half-twist: going once around the circle, the two trivializations agree on one arc and differ by $t \mapsto -t$ on the other. Over either arc alone the band is a product; the sign is what a global product would have to remove.

## When Is a Submersion a Fibration?

*Lecture 13 (Wed Sep 30). Uribe opened with the answer to the question left open in Lecture 12 — “I didn't know the answer right away. I thought the answer was no, and in fact the answer is no. But there's a partial yes.”*

> [!theorem] Theorem §38.4: Ehresmann's Theorem
> Let $\pi : E \to B$ be a surjective submersion which is *proper*: the preimage of every compact set is compact. If $B$ is connected, then $\pi$ is a fibration.

^thm-38-4

> [!proof]+ Proof (to be filled)
> Stated in Lecture 13, not proved: the proof uses connections, which the course does not cover. To be filled.

^pf-38-4

*Status.* Stated in Lecture 13, not proved: “we don't have time to do the proof, and it uses material that we're not going to cover called connections.” Uribe first recalled the case of a compact fibre, then the general statement for proper maps, which is the form given here. The intuition: a connection lets one lift a path from $b$ to $b'$ in the base to paths in $E$, and flow the fibre over $b$ onto the fibre over $b'$; properness is what lets the flow run for as long as needed, so that it identifies the fibres not just one at a time but over a whole neighbourhood — a local trivialization. The transcript renders the name as “Aristotle”; it is Ehresmann.

> [!remark]- Connections
> - Proper maps were defined earlier, for group actions: [[§13 Group Actions and Orbit Spaces#^def-13-6|Def. §13.6]]; compactness: [[§18 Compact Spaces|590 §18]].

> [!example] Example §38.4: All Fibres Diffeomorphic but Not a Fibration
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

^ex-38-4

*Uses:* [[§36 Submersions#^ex-36-1|Ex. §36.1]]

*Status.* Found for Uribe by ChatGPT, which reported that a human had posted it on a mathematics forum; given in lecture as a picture, without proof. *(Completion.)* $E$ is open in $\mathbb{R}^3$: its complement is the $t$-axis $\{(0,0,t)\}$, together with the line $\{(t, 0, t)\}$ and the single point $(1, 0, 0)$, a closed set. So $\pi$ is the restriction of a projection to an open set, hence a submersion ([[§36 Submersions#^ex-36-1|Example §36.1]]), and it is onto. Any two copies of the plane with two points removed are diffeomorphic by an affine map. That $\pi$ is not a fibration is stated, not proved, here. Uribe's intuition: as $t \to 0$ the missing point $(t, 0)$ “is colliding with $(0,0)$”, while over $t = 0$ the second missing point sits away at $(1, 0)$. He added that the example is subtler than it looks: with lines in place of planes the corresponding map would be locally trivial, and “it's the fact that you have [a] fundamental group that messes things up.”

![[m591-16-6.svg]]
*The fibres over a few values of $t$. The origin, grey, is missing from every fibre, and the missing points $(t, 0)$, red, lie on a line — dashed — which meets the line of origins exactly at $t = 0$: the collision. Over $t = 0$ (orange) the second missing point is $(1, 0)$, off that line. Each fibre on its own is a plane minus two points; what fails is the way they fit together near $t = 0$.*

**Transcription note.** Page 35 of the handwritten notes labels the second missing point over $t = 0$ as $(1, 1)$; it is $(1, 0)$.

## Sections and Local Sections

*From Assignment 4, Problem 4, whose hint — “declare that $\Phi_i \circ s_i$ includes $U_i \to U_i \times \{1\}$, and extend the definition of $\Phi_i$ by equivariance” — contains a general principle: local trivializations and local sections are two descriptions of the same thing.*

> [!definition] Definition §38.3: Section
> Let $\pi : E \to B$ be a fibration. A **section** of $\pi$ is a smooth map $s : B \to E$ with $\pi \circ s = \mathrm{id}_B$: “if you first go up and then down, you get the identity on the base.” It picks, smoothly in $b$, one point $s(b)$ of each fibre $\pi^{-1}(b)$.
>
> *Lee: Ch. 10, Sections of Vector Bundles*

^def-38-3

![[m591-17-4.svg]]
*$\pi \circ s = \mathrm{id}_B$. A section goes up, the projection comes down, and the round trip is the identity on the base.*

![[m591-17-5.svg]]
*The cartoon of a section. The fibration is drawn as a box over its base, with fibres vertical; a section is a graph over the base, meeting every fibre exactly once — at $s(b)$ in the fibre over $b$ — so its image $s(B)$ is “a copy of $B$” inside $E$.*

> [!definition] Definition §38.4: Local Section
> Let $\pi : E \to B$ be smooth ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]) and $U \subseteq B$ open. A **local section** of $\pi$ over $U$ is a smooth map $s : U \to E$ with $\pi \circ s = \mathrm{id}_U$.
>
> *Lee: Ch. 10, Local and Global Sections of Vector Bundles*

^def-38-4

A section in the sense of [[§38 Fibrations#^def-38-3|Definition §38.3]] is a local section over $U = B$; to stress the difference, it is also called a *global* section.

> [!theorem] Proposition §38.5: Local Trivializations Give Local Sections
> Let $\pi : E \to B$ be a fibration with fibre $F$, and $\phi : \pi^{-1}(U) \to U \times F$ a local trivialization ([[§38 Fibrations#^def-38-1|Def. §38.1]]). For every $f_0 \in F$, the map $s(u) = \phi^{-1}(u, f_0)$ is a local section ([[§38 Fibrations#^def-38-4|Def. §38.4]]) over $U$.

^prop-38-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Two things are to be shown (Definition [[§38 Fibrations#^def-38-4|§38.4]]): $s : U \to E$ is smooth, and $\pi \circ s = \mathrm{id}_U$.
>
> *Smooth.* $s$ is a composite of $u \mapsto (u, f_0)$ and the diffeomorphism $\phi^{-1}$. The first map is the slice inclusion $\iota^{f_0} : U \to U \times F$ (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-8|§19.8]], with $M_1 = U$ and $M_2 = F$), smooth by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]]. Then $\phi^{-1} : U \times F \to \pi^{-1}(U)$ is smooth, and so is the inclusion of the open submanifold $\pi^{-1}(U)$ into $E$. So $s$ is smooth as a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]).
>
> *Section.* For $u \in U$, using $\pi = \mathrm{pr}_1 \circ \phi$ on $\pi^{-1}(U)$ (the commuting triangle of Definition [[§38 Fibrations#^def-38-1|§38.1]]) and $\phi \circ \phi^{-1} = \mathrm{id}$,
>
> $$
> \pi\big(s(u)\big) = \mathrm{pr}_1\big(\phi(s(u))\big) = \mathrm{pr}_1\big(\phi(\phi^{-1}(u, f_0))\big) = \mathrm{pr}_1(u, f_0) = u .
> $$

^pf-38-5

*Uses:* [[§38 Fibrations#^def-38-1|Def. §38.1]], [[§38 Fibrations#^def-38-4|Def. §38.4]], [[§19 Smooth Functions and Smooth Maps#^prop-19-10|§19.10]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§19 Smooth Functions and Smooth Maps#^def-19-8|Def. §19.8]]
