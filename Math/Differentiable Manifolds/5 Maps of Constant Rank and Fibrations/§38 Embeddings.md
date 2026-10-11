---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 38
tags: [differentiable-manifolds, math591]
---
← [[§37 Immersions]] · ↑ [[· 5 Maps of Constant Rank and Fibrations]] · [[§39 Geometric and Abstract Manifolds]] →

*Stage: maps — Immersions that are homeomorphisms onto their images — their images are submanifolds.*

*References: Lee Ch. 4 and Ch. 5. Lecture 14.*

The normal form makes every immersion locally an inclusion, but an immersion's image can still fail to be a submanifold ([[§37 Immersions|§37]]). Embeddings are the immersions for which it cannot: the normal form is local in the domain, and the topological condition makes it local in the image too.

## Embeddings and Their Images

> [!definition] Definition §38.1: Embedding
> A smooth map ([[§19 Smooth Functions and Smooth Maps#^def-19-3|Def. §19.3]]) $F : M \to N$ is an **embedding** if it is an immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) and, as a map onto its image, $F : M \to F(M)$ is a homeomorphism ([[§10 Continuous Functions#^def-10-2|590 Def. §10.2]]), $F(M)$ carrying the subspace topology ([[§3 Subspaces and Products#^def-3-1|Def. §3.1]]) of $N$. Injectivity is part of being a homeomorphism; Uribe wrote “(injective) immersion” and called the word redundant.
>
> *Lee: Ch. 4, Embeddings*

^def-38-1

> [!remark]- Connections
> - Announced at the end of Lecture 13: [[§37 Immersions#^rem-37-1|Remark: Embeddings — Next Time (§37)]]; the two ways an immersion's image can fail to be a submanifold: [[§37 Immersions#^ex-37-1|Ex. §37.1]], [[§37 Immersions#^ex-37-2|Ex. §37.2]].
> - Homeomorphisms in 590: [[§10 Continuous Functions#^def-10-2|590 Def. §10.2]].

![[m591-33-1.svg]]
*An embedding factors through its image as a homeomorphism followed by the inclusion — “you're taking the manifold $M$ and you're putting it inside $N$.” The figure-eight of Lee's Example 4.19 ([[§37 Immersions#Images of Immersions|§37]]) is an injective immersion for which the top arrow is not a homeomorphism.*

The standard non-example is the *irrational line on the torus*: for $\alpha$ irrational, $F : \mathbb{R} \to T^2 = \mathbb{R}^2/\mathbb{Z}^2$ (the [[Torus|torus]]), $F(t) = [t, \alpha t]$. It is an injective immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) whose image is dense in $T^2$, and it is not an embedding ([[§38 Embeddings#^prop-38-11|Proposition §38.11]] below, from Assignment 4, Problem 5; Lee, Example 4.20). In lecture its image was also said not to be a regular submanifold of $T^2$ ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]).

*In lecture.* Given as “a very important category: non-examples.” “You're wrapping a line, but the slope of the line is irrational, so it never closes … like one of those spirographs.” The normal form still applies: around any $p$ there are neighbourhoods $U$ and $V$ for which $F(U)$ is “a very nice submanifold.” But “it's local in the domain”, while being a submanifold is a statement about the whole image. Points outside $U$ “contribute segments like this, and they're going to be dense. No matter how you shrink this $V$, you won't be able to isolate only the yellow guy.”

![[m591-33-2.svg]]
*The irrational line, drawn here with $\alpha = (\sqrt5 - 1)/2$. Left: nine turns of $F(\mathbb{R})$ in the square, whose opposite sides are identified; the orange piece is $F(U)$, and two other strands already cross the neighbourhood $V$. Right: a disc around $F(p)$ about $4.6$ times smaller, and the first 400 turns of the curve, which cross it in 34 strands. Shrinking further only takes more turns: every neighbourhood of $F(p)$ meets infinitely many strands.*

> [!theorem] Theorem §38.1: The Image of an Embedding Is a Regular Submanifold
> If $F : M \to N$ is an embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]), with $\dim M = m$ and $\dim N = n$, then $F(M)$ is a regular submanifold ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]) of $N$ of codimension $n - m$.
>
> *Lee: Proposition 5.2*

^thm-38-1

> [!proof]+ Proof
> *(Lecture 14. The final equality is completed with Corollary [[§37 Immersions#^cor-37-2|§37.2]]; see the remark after the proof.)* Let $q = F(p) \in F(M)$. We need a chart of $N$ at $q$ in which $F(M)$ is cut out by the vanishing of the last $n - m$ coordinates: an adapted chart at $q$ (Definition [[§35 Regular Submanifolds#^def-35-2|§35.2]], with $k = n - m$). Since $q$ is arbitrary, this shows that $F(M)$ is a regular submanifold of codimension $n - m$ (Definition [[§35 Regular Submanifolds#^def-35-1|§35.1]]).
>
> *Start with the normal form.* $F$ is an immersion (Definition [[§38 Embeddings#^def-38-1|§38.1]]). Take the charts $(U, \varphi)$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q$ of Theorem [[§37 Immersions#^thm-37-1|§37.1]]. By Corollary [[§37 Immersions#^cor-37-2|§37.2]], after replacing $V$ by the smaller open set
>
> $$
> V' = \big\{\, x \in V : \big(y^1(x), \ldots, y^m(x)\big) \in \varphi(U) \,\big\},
> $$
>
> which contains $F(U)$, we have
>
> $$
> F(U) = \{\, x \in V' : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\}. \tag{$\ast$}
> $$
>
> This describes $F(U)$, not $F(M) \cap V'$: “other pieces of the image” may still pass through $V'$, as in the irrational line.
>
> *The key step: the topological hypothesis.* “Here's where we use the very strong condition that $F$ is a topological homeomorphism to its image.” $U$ is open in $M$ and $F : M \to F(M)$ is a homeomorphism, so $F(U)$ is open in $F(M)$ (homeomorphisms are open maps, Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](2)). Since $F(M)$ carries the subspace topology, this means (Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]) that there is an open $W \subseteq N$ with
>
> $$
> F(U) = W \cap F(M) .
> $$
>
> *Shrink $V'$ to $V' \cap W$, and keep the same coordinates.* Since $F(U) \subseteq V' \cap W$ — $F(U) \subseteq V'$ by Corollary [[§37 Immersions#^cor-37-2|§37.2]], and $F(U) = W \cap F(M) \subseteq W$ —
>
> $$
> F(M) \cap (V' \cap W) = F(U) = \{\, x \in V' \cap W : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\},
> $$
>
> the first equality because $F(M) \cap W = F(U) \subseteq V'$, the second by $(\ast)$ intersected with $W$. In full, using in turn the regrouping of intersections, $F(M) \cap W = F(U)$, $F(U) \subseteq V'$, $F(U) \subseteq W$, and $(\ast)$:
>
> $$
> F(M) \cap (V' \cap W) = \big(F(M) \cap W\big) \cap V' = F(U) \cap V' = F(U) = F(U) \cap W = \{\, x \in V' : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\} \cap W .
> $$
>
> The set $V' \cap W$ is open and contains $q \in F(U)$, and $(V' \cap W, \psi|_{V' \cap W})$ is a smooth chart (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)). So $(V' \cap W, \psi)$ is an adapted chart at $q$ (Definition [[§35 Regular Submanifolds#^def-35-2|§35.2]]), and $F(M)$ is a submanifold of codimension $n - m$.
^pf-38-1

*Uses:* [[§38 Embeddings#^def-38-1|Def. §38.1]], [[§37 Immersions#^thm-37-1|§37.1]], [[§37 Immersions#^cor-37-2|§37.2]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§10 Continuous Functions#^prop-10-2|590 §10.2]], [[§2 Topological Manifolds#^lem-2-10|§2.10]]

![[m591-33-3.svg]]
*The key step. $V$ may contain other parts of $F(M)$ (black) besides $F(U)$ (orange). Because $F(U)$ is open in $F(M)$, it is $W \cap F(M)$ for an open $W$ (shaded), and $W$ cuts the other parts away; $F(M)$ continues beyond $F(U)$ only by leaving $W$. For the irrational line no such $W$ exists, which is exactly the failure of openness.*

> [!remark]- Connections
> - Submanifolds and adapted charts: [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]]; the other main source of submanifolds, level sets: [[§35 Regular Submanifolds#^thm-35-7|§35.7]].
> - The local statement this globalizes: [[§37 Immersions#^cor-37-2|§37.2]], from the [[Immersion Normal Form]].

**Transcription note.** Page 39 of the handwritten notes writes the target as $F(M) \cap V = \{0 = y^{n-m+1} = \cdots = y^m\}$; the vanishing coordinates are the last $n - m$ of them, $y^{m+1}, \ldots, y^n$, as the lecture said.

> [!remark] Remark: Where Is Injectivity Used?
> In lecture the last equality caused trouble, and a discussion. Uribe first located the use of injectivity there; a student pointed out that $(*)$ concerns only $F(U)$, and that the proof seems to need only that $F$ be an immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) which is open ([[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]]) onto its image. Another student added covering-type examples: maps that are not injective but whose images are manifolds, such as $\mathbb{R} \to S^1$, $t \mapsto (\cos t, \sin t)$ ([[§33 Local Diffeomorphisms#^ex-33-1|Ex. §33.1]]), or the two-to-one map $S^2 \to \mathbb{RP}^2$ ([[§40 Projective Spaces and the Hopf Fibration#^ex-40-1|Ex. §40.1]]). Uribe agreed — “I don't think we're using injectivity” — and promised “a definite conclusion by email.”
>
> *The conclusion, from Uribe's follow-up email.* The students were right: “a proof that we did today does show that for an immersion that is open as a map onto its image (so for all $U$ open in $M$, $F(U)$ is open in $F(M)$), $F(M)$ is a submanifold. The map $F$ does not have to be injective.” The proof uses exactly two things: the normal form (the immersion hypothesis), and that $F(U)$ is open in $F(M)$ for the $U$ of the normal form; with the completion via [[§37 Immersions#^cor-37-2|Corollary §37.2]] nothing else enters. Injectivity belongs to the *idea* of an embedding — “the idea of an embedding is that it is an isomorphism between $M$ and its image” ([[§38 Embeddings#^cor-38-3|Corollary §38.3]]) — not to this proof. He added that “being an immersion and an open map onto its image” is “an unusual class of maps.”

^rem-38-1

> [!theorem] Proposition §38.2: Immersions That Are Open onto Their Images
> Let $F : M \to N$ be an immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) such that $F : M \to F(M)$ is an open map ([[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]]), $F(M)$ carrying the subspace topology ([[§3 Subspaces and Products#^def-3-1|Def. §3.1]]). Then $F(M)$ is a regular submanifold ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]) of $N$ of codimension $n - m$.

^prop-38-2

> [!proof]+ Proof
> *(The conclusion of the class discussion, confirmed in Uribe's follow-up email.)* The proof of Theorem [[§38 Embeddings#^thm-38-1|§38.1]], word for word: openness of $F$ onto its image is all it used to produce $W$. Written out, with the one changed justification marked:
>
> Let $q = F(p) \in F(M)$; we need an adapted chart at $q$. *Normal form.* $F$ is an immersion, so Theorem [[§37 Immersions#^thm-37-1|§37.1]] gives charts $(U, \varphi)$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q$, and Corollary [[§37 Immersions#^cor-37-2|§37.2]] gives an open $V' \subseteq V$ containing $F(U)$ with
>
> $$
> F(U) = \{\, x \in V' : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\}. \tag{$\ast$}
> $$
>
> Neither result uses injectivity of $F$: the injectivity used in the corollary is that of the chart $\psi$. *Openness* (the changed step). $U$ is open in $M$ and, by hypothesis, $F : M \to F(M)$ is an open map, so $F(U)$ is open in $F(M)$; since $F(M)$ carries the subspace topology, $F(U) = W \cap F(M)$ for some open $W \subseteq N$ (Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]). In Theorem [[§38 Embeddings#^thm-38-1|§38.1]] this step used that $F$ is a homeomorphism onto its image, but only through its consequence that $F$ is open onto its image. *Shrinking.* Since $F(U) \subseteq V'$ and $F(U) = W \cap F(M) \subseteq W$,
>
> $$
> F(M) \cap (V' \cap W) = \big(F(M) \cap W\big) \cap V' = F(U) \cap V' = F(U) = F(U) \cap W = \{\, x \in V' \cap W : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\},
> $$
>
> the last equality by $(\ast)$ intersected with $W$. So the smooth chart $(V' \cap W, \psi|_{V' \cap W})$ (Lemma [[§2 Topological Manifolds#^lem-2-10|§2.10]](1)), whose domain contains $q$, is adapted at $q$ (Definition [[§35 Regular Submanifolds#^def-35-2|§35.2]], with $k = n - m$), and $F(M)$ is a regular submanifold of codimension $n - m$.
>
> For example, $t \mapsto (\cos t, \sin t)$ is an immersion of $\mathbb{R}$, open onto $S^1$ and far from injective — every point of $S^1$ has infinitely many preimages — and its image $S^1$ is a submanifold of $\mathbb{R}^2$. (It is an immersion into $\mathbb{R}^2$ because its velocity $(-\sin t, \cos t)$ never vanishes, as in Example [[§37 Immersions#^ex-37-1|§37.1]]. It is open onto $S^1$ because it is a local diffeomorphism onto $S^1$ (Example [[§33 Local Diffeomorphisms#^ex-33-1|§33.1]]): each $t$ has an open neighbourhood $U_t$ mapped homeomorphically onto an open subset of $S^1$, so for $O \subseteq \mathbb{R}$ open the image of $O \cap U_t$ is open in that subset, hence in $S^1$, and the image of $O$ is the union of these open sets.) The figure-eight is not open onto its image, consistent with its image not being a submanifold. (For $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi)$, the set $\beta\big((-\pi/2, \pi/2)\big)$ is not open in the image: every open set of $\mathbb{R}^2$ around $\beta(0) = (0, 0)$ contains $\beta(t)$ for $t$ near $\pm\pi$, because $\beta(t) \to (\sin(\pm 2\pi), \sin(\pm\pi)) = (0, 0)$ as $t \to \pm\pi$, and these points are not in $\beta\big((-\pi/2, \pi/2)\big)$ since $\beta$ is injective.)
^pf-38-2

*Uses:* [[§38 Embeddings#^pf-38-1|proof of §38.1]], [[§37 Immersions#^thm-37-1|§37.1]], [[§37 Immersions#^cor-37-2|§37.2]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§33 Local Diffeomorphisms#^ex-33-1|Ex. §33.1]], [[§34 Submersions#^cor-34-6|§34.6]], [[§37 Immersions#^ex-37-2|Ex. §37.2]], [[§38 Embeddings#^thm-38-1|§38.1]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§37 Immersions#^ex-37-1|Ex. §37.1]]

> [!theorem] Corollary §38.3: An Embedding Is a Diffeomorphism onto Its Image
> If $F : M \to N$ is an embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]), then $F : M \to F(M)$ is a diffeomorphism ([[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]]), $F(M)$ carrying its induced smooth structure as a regular submanifold ([[§35 Regular Submanifolds#^prop-35-2|§35.2]]).

^cor-38-3

> [!proof]+ Proof
> *(Stated in Lecture 14 — “an embedding restricts to a diffeomorphism between $M$ and the image”; filled in.)* Write $\bar F : M \to F(M)$ for $F$ regarded as a map onto its image and $\iota : F(M) \hookrightarrow N$ for the inclusion, so that $F = \iota \circ \bar F$. By Theorem [[§38 Embeddings#^thm-38-1|§38.1]], $F(M)$ is a regular submanifold of $N$ of codimension $n - m$, so with its induced structure it is a smooth manifold of dimension $n - (n - m) = m$ (Proposition [[§35 Regular Submanifolds#^prop-35-2|§35.2]]).
>
> *Smooth.* $F$ is smooth into $N$ with values in $F(M)$, so $\bar F : M \to F(M)$ is smooth by Lemma [[§35 Regular Submanifolds#^lem-35-3|§35.3]](2).
>
> *Immersion.* Its differential followed by the injective $\iota_\ast$ (Proposition [[§35 Regular Submanifolds#^prop-35-4|§35.4]]) is the injective $F_\ast$: by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]), $F_{\ast p} = \iota_{\ast F(p)} \circ \bar F_{\ast p}$ for $p \in M$. If $\bar F_{\ast p} v = 0$, then $F_{\ast p} v = \iota_{\ast F(p)}(0) = 0$, so $v = 0$ because $F$ is an immersion. So $\bar F_{\ast p}$ is injective for every $p$.
>
> *Local diffeomorphism.* Both manifolds have dimension $m$ and $\bar F$ is an immersion at every point, so it is a local diffeomorphism (Proposition [[§34 Submersions#^prop-34-1|§34.1]](3)).
>
> *Diffeomorphism.* $\bar F$ is bijective: injective because $F : M \to F(M)$ is a homeomorphism (Definition [[§38 Embeddings#^def-38-1|§38.1]]), and onto $F(M)$ by the definition of $F(M)$. Being a bijective local diffeomorphism, it is a diffeomorphism, its inverse being smooth near every point (Corollary [[§33 Local Diffeomorphisms#^cor-33-3|§33.3]]).
^pf-38-3

*Uses:* [[§38 Embeddings#^thm-38-1|§38.1]], [[§35 Regular Submanifolds#^prop-35-2|§35.2]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§34 Submersions#^prop-34-1|§34.1]], [[§33 Local Diffeomorphisms#^cor-33-3|§33.3]], [[§38 Embeddings#^def-38-1|Def. §38.1]]

## Proper Maps

*Lecture 14. When is an injective immersion an embedding? The homeomorphism condition is point-set topology, and a convenient sufficient condition is properness — the same hypothesis as in Ehresmann's theorem ([[§36 Fibrations#^thm-36-3|Theorem §36.3]]).*

> [!definition] Definition §38.2: Proper Map
> A continuous map $F : X \to Y$ is **proper** if $F^{-1}(K)$ is compact ([[§18 Compact Spaces#^def-18-2|590 Def. §18.2]]) for every compact $K \subseteq Y$.
>
> *Lee: App. A, Proper Maps*

^def-38-2

> [!remark]- Connections
> - The same definition, given earlier for proper actions: [[§13 Group Actions and Orbit Spaces#^def-13-6|Def. §13.6]].
> - The properness hypothesis of [[§36 Fibrations#^thm-36-3|Ehresmann's theorem, §36.3]].

> [!theorem] Proposition §38.4: Proper Maps into Manifolds Are Closed
> Let $F : M \to N$ be a continuous proper map ([[§38 Embeddings#^def-38-2|Def. §38.2]]), $N$ a topological manifold ([[§2 Topological Manifolds#^def-2-2|Def. §2.2]]). Then $F$ is closed ([[§13 Quotient Topology#^def-13-4|590 Def. §13.4]]): $F(C)$ is closed in $N$ for every closed $C \subseteq M$.
>
> *Lee: Theorem A.57*

^prop-38-4

> [!proof]+ Proof
> *(Lecture 14 — “it's a very funny proof. You go back and forth literally.” Uribe did not finish Claim 2 in lecture and sent the complete proof in his follow-up email; the completion of Claim 2 below is the notes' own.)* Let $C \subseteq M$ be closed. We show $\overline{F(C)} \subseteq F(C)$, so that $F(C)$ is closed. Recall that $N$, a topological manifold, is Hausdorff, and that a point lies in the closure of a set $A$ exactly when every open set containing the point meets $A$.
>
> *Claim 1: $F(C) \cap K$ is closed for every compact $K \subseteq N$.* $F^{-1}(K)$ is compact, because $F$ is proper (Definition [[§38 Embeddings#^def-38-2|§38.2]]). So $C \cap F^{-1}(K)$, a closed subset of it, is compact: it is closed in the subspace $F^{-1}(K)$, its complement there being $(M \setminus C) \cap F^{-1}(K)$, and a closed subset of a compact space is compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](5)). Its image $F\big(C \cap F^{-1}(K)\big)$ is compact, as the continuous image of a compact space (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)), hence closed in the Hausdorff space $N$ (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](4)). And $F\big(C \cap F^{-1}(K)\big) = F(C) \cap K$: a point of the left side is $F(c)$ with $c \in C$ and $F(c) \in K$, hence lies in $F(C) \cap K$; and conversely, a point $y \in F(C) \cap K$ is $y = F(c)$ with $c \in C$, and $F(c) = y \in K$ gives $c \in F^{-1}(K)$.
>
> *Claim 2.* Let $q \in \overline{F(C)}$, and let $V$ be a neighbourhood of $q$ with compact closure (Proposition [[§2 Topological Manifolds#^prop-2-12|§2.12]]). Then $q \in \overline{F(C) \cap \overline V}$. *(Completion.)* If $O$ is any open set containing $q$, then $O \cap V$ is an open set containing $q$, so it meets $F(C)$; hence $O$ meets $F(C) \cap V \subseteq F(C) \cap \overline V$.
>
> *Conclusion.* By Claim 1 with $K = \overline V$, the set $F(C) \cap \overline V$ is closed, so it equals its closure, and $q \in F(C) \cap \overline V \subseteq F(C)$. As $q \in \overline{F(C)}$ was arbitrary, $\overline{F(C)} \subseteq F(C)$; the reverse inclusion always holds. Thus $\overline{F(C)} = F(C)$.
^pf-38-4

*Uses:* [[§38 Embeddings#^def-38-2|Def. §38.2]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^prop-2-12|§2.12]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§18 Compact Spaces#^thm-18-2|590 §18.2]], [[§18 Compact Spaces#^thm-18-3|590 §18.3]], [[§18 Compact Spaces#^thm-18-4|590 §18.4]], [[§8 Interior and Closure#^thm-8-3|590 §8.3]]

> [!remark]- Connections
> - The closed-map argument for compact domains in 590, which Claim 1 localizes: [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]]; closed maps: [[§13 Quotient Topology#^def-13-4|590 Def. §13.4]].
> - Local compactness in 590: [[§20 Local Compactness#^def-20-1|590 Def. §20.1]], [[§20 Local Compactness#^thm-20-6|590 §20.6]].

> [!theorem] Theorem §38.5: Injective Proper Immersions Are Embeddings
> An injective proper ([[§38 Embeddings#^def-38-2|Def. §38.2]]) immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) $F : M \to N$ is an embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]).
>
> *Lee: Proposition 4.22*

^thm-38-5

> [!proof]+ Proof
> *(Lecture 14 reduced this to Proposition [[§38 Embeddings#^prop-38-4|§38.4]]; the last step is filled in.)* $F$ is an immersion by hypothesis, so by Definition [[§38 Embeddings#^def-38-1|§38.1]] it remains to see that $F : M \to F(M)$ is a homeomorphism, $F(M)$ carrying the subspace topology.
>
> It is a continuous bijection: continuous into $F(M)$ because it is continuous into $N$ (Proposition [[§3 Subspaces and Products#^prop-3-3|§3.3]](2)), injective by hypothesis, and onto $F(M)$ by the definition of $F(M)$. Let $G : F(M) \to M$ be its inverse. A map is continuous when the preimage of every closed set is closed (take complements in the definition of continuity), and for $C \subseteq M$ the preimage $G^{-1}(C)$ is $F(C)$. If $C \subseteq M$ is closed, then $F(C)$ is closed in $N$ by Proposition [[§38 Embeddings#^prop-38-4|§38.4]] ($F$ is continuous and proper, and $N$ is a manifold), hence $F(C) = F(C) \cap F(M)$ is closed in $F(M)$: its complement in $F(M)$ is $(N \setminus F(C)) \cap F(M)$, open in the subspace topology (Definition [[§3 Subspaces and Products#^def-3-1|§3.1]]). So the inverse $F(M) \to M$ is continuous, and $F : M \to F(M)$ is a homeomorphism.
^pf-38-5

*Uses:* [[§38 Embeddings#^def-38-1|Def. §38.1]], [[§38 Embeddings#^prop-38-4|§38.4]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§7 Closed Sets and Limit Points#^thm-7-2|590 §7.2]], [[§10 Continuous Functions#^thm-10-1|590 §10.1]], [[§3 Subspaces and Products#^prop-3-3|§3.3]]

> [!theorem] Corollary §38.6: Injective Immersions of Compact Manifolds
> If $M$ is compact ([[§18 Compact Spaces#^def-18-2|590 Def. §18.2]]), every injective immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) $F : M \to N$ is an embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]).
>
> *Lee: Proposition 4.22*

^cor-38-6

> [!proof]+ Proof
> *(Uribe's follow-up email: “Note that $F$ is proper if $M$ is compact, a fact that can be very useful!”; the proof is filled in.)* $F$ is proper (Definition [[§38 Embeddings#^def-38-2|§38.2]]): if $K \subseteq N$ is compact, it is closed, as a compact subset of the Hausdorff space $N$ (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](4)); so $F^{-1}(K)$ is closed in $M$, $F$ being continuous; and a closed subset of the compact $M$ is compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](5)). So $F$ is an injective proper immersion. Apply Theorem [[§38 Embeddings#^thm-38-5|§38.5]]: $F$ is an embedding.
^pf-38-6

*Uses:* [[§38 Embeddings#^def-38-2|Def. §38.2]], [[§38 Embeddings#^thm-38-5|§38.5]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§18 Compact Spaces#^thm-18-4|590 §18.4]], [[§18 Compact Spaces#^thm-18-2|590 §18.2]]

> [!remark]- Connections
> - The topological prototype: a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism, [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §18.7]] (in 591: [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](6)).

*An aside from the end of the lecture.* Uribe mentioned that he is developing his own notes for the course, “based on notes that somebody took a few years ago”, edited “the night before”, and asked whether they would help, perhaps shared through Overleaf.

## Closedness and Density

*Why does density of the irrational line rule out an embedding? Because the image of an embedding is always closed* locally, *and a dense set that is locally closed is open. Prompted by Assignment 4, Problem 5.*

> [!definition] Definition §38.3: Locally Closed Subset
> A subset $S$ of a topological space $N$ is **locally closed** if every point of $S$ has an open neighbourhood $V$ in $N$ such that $S \cap V$ is closed in $V$ ([[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§7 Closed Sets and Limit Points#^def-7-1|590 Def. §7.1]]). Equivalently, $S$ is closed in some open subset of $N$ containing it, namely the union $U$ of these $V$'s.

^def-38-3

> [!remark]- Connections
> - Closed sets and closed sets of a subspace in 590: [[§7 Closed Sets and Limit Points#^def-7-1|590 Def. §7.1]], [[§7 Closed Sets and Limit Points#^thm-7-2|590 §7.2]]; the subspace topology: [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]].

> [!theorem] Proposition §38.7: Images of Embeddings Are Locally Closed
> Every regular submanifold ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]) of $N$ — in particular the image of an embedding ([[§38 Embeddings#^thm-38-1|Theorem §38.1]]) — is locally closed ([[§38 Embeddings#^def-38-3|Def. §38.3]]) in $N$.

^prop-38-7

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $S$ be a regular submanifold of $N$, of codimension $k$, and put $n = \dim N$ and $m = n - k$. (By Theorem [[§38 Embeddings#^thm-38-1|§38.1]], the image of an embedding is such an $S$, so the “in particular” follows.)
>
> *Locally closed.* At each point of the submanifold $S$ there is an adapted chart $(V, \psi = (y^1, \ldots, y^n))$ (Definitions [[§35 Regular Submanifolds#^def-35-1|§35.1]] and [[§35 Regular Submanifolds#^def-35-2|§35.2]]), in which $S \cap V = \{x \in V : y^{m+1}(x) = \cdots = y^n(x) = 0\}$, a closed subset of $V$ as the zero set of continuous functions: it is the preimage of the closed set $\{\vec 0\} \subseteq \mathbb{R}^{k}$ under the continuous map $(y^{m+1}, \ldots, y^n) : V \to \mathbb{R}^k$. This is the condition of Definition [[§38 Embeddings#^def-38-3|§38.3]], with this $V$.
>
> *The equivalence in the definition.* If $U$ is the union of these $V$ — one for each point of $S$ — then $U$ is open and contains $S$. A point of $U \setminus S$ lies in some $V \setminus S$, which is open: it is open in $V$, as the complement of the closed set $S \cap V$, hence open in $N$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]); and $V \setminus S \subseteq U \setminus S$. So $U \setminus S$ is open, and $S = U \setminus (U \setminus S)$ is closed in $U$. Conversely, if $S$ is closed in an open $U \supseteq S$, then every point of $S$ has the open neighbourhood $V = U$, with $S \cap V = S$ closed in $V$.
^pf-38-7

*Uses:* [[§38 Embeddings#^def-38-3|Def. §38.3]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§38 Embeddings#^thm-38-1|§38.1]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§10 Continuous Functions#^thm-10-1|590 §10.1]], [[§7 Closed Sets and Limit Points#^def-7-1|590 Def. §7.1]]

> [!theorem] Corollary §38.8: Dense Regular Submanifolds Are Open
> A dense ([[§22 Countability Axioms#^def-22-4|590 Def. §22.4]]) regular submanifold ([[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]) $S$ of $N$ is an open subset of $N$, and has codimension $0$. In particular, the image of an embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]) $F : M \to N$ with $\dim M < \dim N$ is never dense.

^cor-38-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *$S$ is open.* By Proposition [[§38 Embeddings#^prop-38-7|§38.7]], $S$ is closed in an open $U \supseteq S$. $S$ is dense in $N$, hence in $U$: a point $u \in U$ lies in the closure of $S$ in $U$ when every open set of $U$ containing $u$ meets $S$, and such a set is open in $N$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]), so it meets $S$ by density. A closed dense subset of $U$ is all of $U$, since it equals its closure in $U$, which is $U$; so $S = U$ is open.
>
> *Codimension $0$.* If $S = \emptyset$, density forces $N = \overline{S} = \emptyset$, and there is nothing to prove; so let $x \in S$. If $S$ had codimension $k \ge 1$, take an adapted chart $(V, \psi)$ at $x$ (Definition [[§35 Regular Submanifolds#^def-35-2|§35.2]]): then $\psi(S \cap V)$ would be a nonempty subset of $\mathbb{R}^{n-k} \times \{0\}$, open in $\mathbb{R}^n$ because $S \cap V$ is open in $V$ — impossible, since no nonempty open subset of $\mathbb{R}^n$ lies in a hyperplane. In detail: $S \cap V$ is open in $V$ because $S$ is open in $N$; $\psi$ is a homeomorphism of $V$ onto the open set $\psi(V)$, so $\psi(S \cap V)$ is open in $\psi(V)$ (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](3)), hence in $\mathbb{R}^n$ (Lemma [[§3 Subspaces and Products#^lem-3-2|§3.2]]). It contains $\psi(x) = (a, \vec 0)$, hence an open ball of some radius $\varepsilon > 0$ around it, which contains the point obtained from $(a, \vec 0)$ by changing its last coordinate from $0$ to $\varepsilon/2$; since $k \ge 1$, that coordinate is one of the last $k$, so this point is not in $\mathbb{R}^{n-k} \times \{0\}$, a contradiction. So $k = 0$.
>
> *In particular.* Let $F : M \to N$ be an embedding with $m = \dim M < \dim N = n$, and $M \neq \emptyset$. By Theorem [[§38 Embeddings#^thm-38-1|§38.1]], $F(M)$ is a nonempty regular submanifold with adapted charts of codimension $n - m \ge 1$ at each of its points. If $F(M)$ were dense, it would be open by the first part, and the argument just given, applied to one of these adapted charts, would give a contradiction. So $F(M)$ is not dense.
^pf-38-8

*Uses:* [[§38 Embeddings#^prop-38-7|§38.7]], [[§38 Embeddings#^def-38-3|Def. §38.3]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^def-35-2|Def. §35.2]], [[§38 Embeddings#^thm-38-1|§38.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§22 Countability Axioms#^def-22-4|590 Def. §22.4]], [[§8 Interior and Closure#^thm-8-2|590 §8.2]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

> [!remark]- Connections
> - Dense subsets in 590: [[§22 Countability Axioms#^def-22-4|590 Def. §22.4]], with the [[Closure Characterization|590 closure characterization]].

This is the precise form of Uribe's “no matter how you shrink $V$, you won't be able to isolate only the yellow guy”: at every point of [[§38 Embeddings#^prop-38-11|the irrational line]], local closedness fails.

> [!theorem] Proposition §38.9: Closed Embeddings Are the Proper Ones
> An embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]) $F : M \to N$ is proper ([[§38 Embeddings#^def-38-2|Def. §38.2]]) if and only if its image $F(M)$ is closed in $N$. In particular, an injective proper immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]) is exactly an embedding with closed image.
>
> *Lee: Proposition 5.5*

^prop-38-9

> [!proof]+ Proof
> *(Not from lecture; filled in.)* *Proper $\Rightarrow$ closed image.* If $F$ is proper, it is closed (Proposition [[§38 Embeddings#^prop-38-4|§38.4]], $N$ being a manifold), so $F(M)$, the image of the closed set $M$, is closed.
>
> *Closed image $\Rightarrow$ proper.* Conversely, let $F(M)$ be closed and $K \subseteq N$ compact. Then $K \cap F(M)$ is a closed subset of $K$ (in the subspace topology of $K$, as the intersection of $K$ with a closed subset of $N$), hence compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](5)). Since $F$ takes all its values in $F(M)$, $F^{-1}(K) = F^{-1}\big(K \cap F(M)\big)$. And $F^{-1}\big(K \cap F(M)\big)$ is its image under the inverse of the homeomorphism $F : M \to F(M)$ (Definition [[§38 Embeddings#^def-38-1|§38.1]]), a continuous map, hence compact (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](2)). So $F$ is proper (Definition [[§38 Embeddings#^def-38-2|§38.2]]).
>
> *The last sentence.* The last sentence combines this with Theorem [[§38 Embeddings#^thm-38-5|§38.5]]. An injective proper immersion is an embedding by that theorem, and its image is closed by the first part. Conversely, an embedding with closed image is proper by the second part, and it is an injective immersion by Definition [[§38 Embeddings#^def-38-1|§38.1]].
^pf-38-9

*Uses:* [[§38 Embeddings#^def-38-1|Def. §38.1]], [[§38 Embeddings#^def-38-2|Def. §38.2]], [[§38 Embeddings#^prop-38-4|§38.4]], [[§38 Embeddings#^thm-38-5|§38.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§7 Closed Sets and Limit Points#^thm-7-2|590 §7.2]], [[§18 Compact Spaces#^thm-18-2|590 §18.2]], [[§18 Compact Spaces#^thm-18-3|590 §18.3]]

| Map | Image | Example separating it from the row above |
|---|---|---|
| injective proper immersion | closed regular submanifold | — |
| embedding | locally closed regular submanifold | an open interval embedded in $\mathbb{R}^2$ |
| injective immersion | possibly not locally closed, even dense | [[§38 Embeddings#^prop-38-11\|the irrational line]] |

Closedness of the image alone is not enough: the image of the [[§37 Immersions#^ex-37-2|figure-eight]] (Lee's Example 4.19) is compact, hence closed, but the figure-eight is not an embedding. Local closedness is necessary for an embedding, not sufficient.

![[m591-34-4.svg]]
*Local closedness ([[§38 Embeddings#^def-38-3|Definition §38.3]]) at a point $p$ of a subset $S$ (blue): is $S \cap V$ (red) closed in a small open disc $V$ (green) around $p$? (a) An open arc in $\mathbb{R}^2$, the embedded open interval of the table's middle row. Its endpoints (hollow) are missing, so $S$ is not closed in $\mathbb{R}^2$; but near each of its points $S \cap V$ is an arc running from boundary to boundary of $V$, closed in $V$, so $S$ is locally closed, as every submanifold is ([[§38 Embeddings#^prop-38-7|Proposition §38.7]]). (b) The image of the [[§37 Immersions#^ex-37-2|figure-eight]] (Lee's Example 4.19). It is compact, hence closed, and at the crossing point $p$ the set $S \cap V$ is an X, closed in $V$: locally closed. But an X is not a piece of a curve, so $S$ is not a submanifold; local closedness is necessary, not sufficient. (c) The [[§38 Embeddings#^prop-38-11|irrational line]] in the square with opposite sides identified, with slope $(\sqrt5 - 1)/2$: seven turns in blue, of which two strands cross $V$ (thick red); the thin red strands are where the turns up to $t = 90$ cross $V$, and further turns keep adding strands between them. So $S \cap V$ is dense in $V$ without being all of $V$, hence not closed in $V$, for every disc around every point: $S$ is not locally closed, and by Proposition §37.7 not a submanifold, which is [[§38 Embeddings#^cor-38-8|Corollary §38.8]] seen locally. (Drawn for these notes in the vault; not in the course tex.)*

> [!theorem] Lemma §38.10: Dirichlet's Approximation Theorem
> For every $\alpha \in \mathbb{R}$ and every integer $N \ge 1$ there are integers $n, m$ with $1 \le n \le N$ and $|n\alpha - m| < 1/N$.
>
> *Lee: Lemma 4.21*

^lem-38-10

> [!remark]- Connections
> - No home elsewhere in the vault; Lee's proof rests on the [[Pigeonhole Principle|250 Pigeonhole Principle]].

*Status.* Used in Assignment 4, Problem 5, citing Lee; not proved here. (Lee's proof is a [[Pigeonhole Principle|pigeonhole]] argument on the fractional parts of $0, \alpha, \ldots, N\alpha$.)

> [!theorem] Proposition §38.11: The Irrational Line on the Torus
> Let $\alpha$ be irrational and $\gamma : \mathbb{R} \to T^2 = S^1 \times S^1$, $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$ — the curve $F(t) = [t, \alpha t]$ introduced before [[§38 Embeddings#^thm-38-1|Theorem §38.1]], under the identification $[x, y] \mapsto (e^{2\pi i x}, e^{2\pi i y})$. Then $\gamma$ is an injective immersion ([[§37 Immersions#^def-37-1|Def. §37.1]]), its image is dense ([[§22 Countability Axioms#^def-22-4|590 Def. §22.4]]) in $T^2$, and $\gamma$ is not an embedding ([[§38 Embeddings#^def-38-1|Def. §38.1]]).
>
> *Lee: Example 4.20*

^prop-38-11

> [!proof]+ Proof
> *(Assignment 4, Problem 5: the submitted solution, condensed; the second proof of the last claim is new.)* Distances below are taken in $\mathbb{C}^2$, whose subspace topology $T^2$ carries; write $\gamma_{\mathbb{C}} = \iota \circ \gamma : \mathbb{R} \to \mathbb{C}^2$ for $\gamma$ followed by the inclusion $\iota : T^2 \hookrightarrow \mathbb{C}^2$. Two elementary facts are used: $e^{2\pi i s} = 1$ if and only if $s \in \mathbb{Z}$; and $|e^{is} - e^{it}| \le |s - t|$ for real $s, t$ (a chord of the unit circle is no longer than the arc it subtends).
>
> *Immersion.* $\gamma$ is smooth into $\mathbb{C}^2$ with values in the submanifold $T^2$, hence smooth into $T^2$ (Lemma [[§35 Regular Submanifolds#^lem-35-3|§35.3]](2)). Its velocity in $\mathbb{C}^2$, $\big(2\pi i e^{2\pi i t}, 2\pi i\alpha e^{2\pi i \alpha t}\big)$, has first entry of modulus $2\pi \ne 0$, so by the chain rule $\gamma_{\ast t}$ is nonzero, hence injective. In detail: by Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]] in the identity charts, $(\gamma_{\mathbb{C}})_{\ast t}(\partial/\partial r|_t)$ is the velocity above, which is nonzero; by the Chain Rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) $(\gamma_{\mathbb{C}})_{\ast t} = \iota_{\ast\gamma(t)} \circ \gamma_{\ast t}$, so $\gamma_{\ast t}(\partial/\partial r|_t) \neq 0$, for otherwise its image under $\iota_{\ast\gamma(t)}$ would be $0$. As $T_t\mathbb{R}$ is spanned by $\partial/\partial r|_t$, the linear map $\gamma_{\ast t}$ has kernel $0$.
>
> *Injective.* If $\gamma(t_1) = \gamma(t_2)$, then $e^{2\pi i (t_1 - t_2)} = 1$ and $e^{2\pi i \alpha(t_1 - t_2)} = 1$, so $t_1 - t_2 \in \mathbb{Z}$ and $\alpha(t_1 - t_2) \in \mathbb{Z}$; if $t_1 \ne t_2$ this makes $\alpha = \alpha(t_1 - t_2)/(t_1 - t_2)$ a quotient of integers with nonzero denominator, that is, rational. So $t_1 = t_2$.
>
> *Dense.* Using $|e^{is} - e^{it}| \le |s - t|$: by Lemma [[§38 Embeddings#^lem-38-10|§38.10]] there are $n_N \ge 1$ and $m_N$ with $|n_N\alpha - m_N| < 1/N$, so $w_N = e^{2\pi i \alpha n_N} = e^{i\theta_N}$ with $\theta_N = 2\pi(n_N\alpha - m_N)$, $0 < |\theta_N| < 2\pi/N$ (nonzero by injectivity). Here $e^{2\pi i \alpha n_N} = e^{2\pi i (\alpha n_N - m_N)}$ because $e^{-2\pi i m_N} = 1$; and $\theta_N = 0$ would give $\gamma(n_N) = (1, 1) = \gamma(0)$ with $n_N \neq 0$, contradicting injectivity. The powers $w_N^k = e^{2\pi i \alpha (k n_N)}$ are $2\pi/N$-dense in $S^1$, since consecutive ones differ in angle by $|\theta_N|$. In detail: let $\delta = |\theta_N|$, and note $e^{ik\delta} = w_N^{\pm k} = e^{2\pi i \alpha (\pm k n_N)}$, with the sign of $\theta_N$. Given $e^{i\phi} \in S^1$ with $\phi \in [0, 2\pi)$, let $k \ge 0$ be the integer with $k\delta \le \phi < (k+1)\delta$; then $0 \le \phi - k\delta < \delta$, so $|e^{i\phi} - e^{ik\delta}| \le |\phi - k\delta| < \delta < 2\pi/N$, and $e^{ik\delta}$ is a power of $w_N$. So $D = \{e^{2\pi i\alpha k} : k \in \mathbb{Z}\}$ is dense in $S^1$: every point of $S^1$ lies within $2\pi/N$ of $D$, for every $N$. Given $(e^{2\pi i a}, e^{2\pi i b}) \in T^2$, the points $\gamma(a + k) = (e^{2\pi i a}, e^{2\pi i \alpha a} e^{2\pi i \alpha k})$ have the right first coordinate, and their second coordinates come arbitrarily close to $e^{2\pi i b}$ because $D$ is dense. In detail: given $\varepsilon > 0$, choose $k \in \mathbb{Z}$ with $|e^{2\pi i \alpha k} - e^{2\pi i (b - \alpha a)}| < \varepsilon$; multiplying by $e^{2\pi i \alpha a}$, of modulus $1$,
>
> $$
> \big|\gamma(a + k) - (e^{2\pi i a}, e^{2\pi i b})\big| = \big|e^{2\pi i \alpha a} e^{2\pi i \alpha k} - e^{2\pi i \alpha a} e^{2\pi i (b - \alpha a)}\big| = \big|e^{2\pi i \alpha k} - e^{2\pi i (b - \alpha a)}\big| < \varepsilon .
> $$
>
> So every open set of $T^2$ meets $\gamma(\mathbb{R})$: the image is dense.
>
> *Not an embedding: the submitted proof.* $\gamma(n_N) \to \gamma(0)$, since
>
> $$
> |\gamma(n_N) - \gamma(0)| = \big|(e^{2\pi i n_N}, e^{2\pi i \alpha n_N}) - (1, 1)\big| = \big|e^{2\pi i \alpha n_N} - e^{2\pi i m_N}\big| \le 2\pi|n_N\alpha - m_N| < 2\pi/N ,
> $$
>
> using $e^{2\pi i n_N} = 1 = e^{2\pi i m_N}$. So $\gamma(n_N) \to \gamma(0)$ in the image $\gamma(\mathbb{R})$ with its subspace topology. If $\gamma^{-1} : \gamma(\mathbb{R}) \to \mathbb{R}$ were continuous, as it is for an embedding (Definition [[§38 Embeddings#^def-38-1|§38.1]]), then $n_N = \gamma^{-1}(\gamma(n_N)) \to \gamma^{-1}(\gamma(0)) = 0$, which is false because $n_N \ge 1$ for every $N$.
>
> *Not an embedding: via density.* The image is dense and $\dim \mathbb{R} = 1 < 2 = \dim T^2$, so by Corollary [[§38 Embeddings#^cor-38-8|§38.8]] it is not the image of an embedding.
^pf-38-11

*Uses:* [[§37 Immersions#^def-37-1|Def. §37.1]], [[§38 Embeddings#^def-38-1|Def. §38.1]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§38 Embeddings#^lem-38-10|§38.10]], [[§38 Embeddings#^cor-38-8|§38.8]], [[§22 Countability Axioms#^def-22-4|590 Def. §22.4]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]

> [!remark]- Connections
> - The torus as a quotient of the square in 590: [[§13 Quotient Topology#^ex-13-3|590 Ex. §13.3]]; the covering $\mathbb{R}^2 \to T^2$, through which $F$ factors: [[§31 Covering Spaces#^ex-31-3|590 Ex. §31.3]]; all the torus's uses: [[Torus|590 Torus]].
> - Locally the image is still a submanifold: [[§37 Immersions#^cor-37-2|§37.2]].

![[m591-34-3.svg]]
*The irrational line on a torus in $\mathbb{R}^3$, drawn with the slope $\alpha = (5 - \sqrt5)/10 \approx 0.28$ so that the stripes run steeply: the horizontal direction of the square goes around the tube, the vertical one around the hole, and strands on the far side are drawn faintly. Left: $t \in [0, 9]$, starting at $F(0)$. Middle: $t \in [0, 40]$. Right: $t \in [0, 150]$ — the curve never closes up, and its strands fill in the torus, as [[§38 Embeddings#^prop-38-11|Proposition §38.11]] proves for every irrational $\alpha$. (Drawn for these notes in the vault; not in the course tex.)*

## Regular and Immersed Submanifolds

*Not from lecture: the notion announced with [[§35 Regular Submanifolds#^def-35-1|Definition §35.1]].* A regular submanifold carries the subspace topology, and its smooth structure is forced on it by the ambient manifold. The images of the injective immersions of [[§37 Immersions|§37]] — the figure-eight, the irrational line on the torus — do not fit that definition, but each is a perfectly good manifold in the topology it inherits from its *domain*. Allowing that topology gives the second kind of submanifold.

> [!definition] Definition §38.4: Immersed Submanifold
> Let $N$ be a smooth manifold. An **immersed submanifold** of $N$ is a subset $S \subseteq N$ together with a topology on $S$, in which it is a topological manifold, and a smooth structure on $S$, such that the inclusion $\iota : S \hookrightarrow N$ is a smooth [[§37 Immersions#^def-37-1|immersion]] ([[§37 Immersions#^def-37-1|Definition §37.1]]). The topology need not be the [[§3 Subspaces and Products#^def-3-1|subspace topology]].

^def-38-4

> [!remark]- Connections
> - The other kind: [[§35 Regular Submanifolds#^def-35-1|regular submanifolds, Def. §35.1]], which are immersed submanifolds by [[§38 Embeddings#^prop-38-13|§38.13]].
> - Lee calls these immersed submanifolds as well (Ch. 5, *Immersed Submanifolds*).

> [!theorem] Proposition §38.12: Images of Injective Immersions
> Let $F : M \to N$ be an injective [[§37 Immersions#^def-37-1|immersion]] and $S = F(M)$. There is exactly one topology and smooth structure on $S$ for which $F : M \to S$ is a [[§19 Smooth Functions and Smooth Maps#^def-19-4|diffeomorphism]], and with them $S$ is an [[§38 Embeddings#^def-38-4|immersed submanifold]] of $N$.

^prop-38-12

> [!proof]+ Proof
> *(Not from lecture.)* *The topology.* Declare $U \subseteq S$ open if $F^{-1}(U)$ is open in $M$. This is a topology on $S$, because $F^{-1}(\emptyset) = \emptyset$, $F^{-1}(S) = M$, and preimages commute with unions and intersections. Let $h = F^{-1} : S \to M$ be the inverse of the bijection $F : M \to S$ ($F$ is injective). For $U \subseteq S$, $h(U) = F^{-1}(U)$, so $U$ is open in $S$ exactly when $h(U)$ is open in $M$: $h$ is a bijection that matches open sets with open sets, a homeomorphism (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](2)).
>
> *The smooth structure.* By Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], applied to the homeomorphism $h : S \to M$, $S$ is a topological manifold and carries exactly one smooth structure for which $h$, and hence $F = h^{-1}$, is a diffeomorphism (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-6|§19.6]]); a map is a diffeomorphism exactly when its inverse is (Definition [[§19 Smooth Functions and Smooth Maps#^def-19-4|§19.4]]).
>
> *Uniqueness.* The topology is forced as well, since a diffeomorphism is a homeomorphism: if some topology on $S$ makes $F : M \to S$ a homeomorphism, then a set $U \subseteq S$ is open in it exactly when $F^{-1}(U)$ is open in $M$ (Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](2)), which is the topology declared above. And for that topology the smooth structure is unique by Proposition [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]](3).
>
> *Immersed submanifold.* The inclusion is $\iota = F \circ h$, with $F : M \to N$: indeed $F(h(q)) = q$ for $q \in S$. It is a composite of smooth maps (Lemma [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]]); by the chain rule (Theorem [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]]) $\iota_{\ast q} = F_{\ast h(q)} \circ h_{\ast q}$, which is injective because $h_{\ast q}$ is an isomorphism (Corollary [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]]) and $F_{\ast h(q)}$ is injective: if $\iota_{\ast q}v = 0$, then $h_{\ast q}v \in \ker F_{\ast h(q)} = 0$, so $v = 0$. So $\iota$ is an immersion, and $S$, with this topology and smooth structure, is an immersed submanifold of $N$ (Definition [[§38 Embeddings#^def-38-4|§38.4]]).
^pf-38-12

*Uses:* [[§38 Embeddings#^def-38-4|Def. §38.4]], [[§37 Immersions#^def-37-1|Def. §37.1]], [[§19 Smooth Functions and Smooth Maps#^prop-19-6|§19.6]], [[§19 Smooth Functions and Smooth Maps#^def-19-6|Def. §19.6]], [[§19 Smooth Functions and Smooth Maps#^lem-19-4|§19.4]], [[§28 Derivations and the Abstract Tangent Space#^thm-28-6|§28.6]], [[§28 Derivations and the Abstract Tangent Space#^cor-28-7|§28.7]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§19 Smooth Functions and Smooth Maps#^def-19-4|Def. §19.4]]

> [!theorem] Proposition §38.13: Every Regular Submanifold Is an Immersed Submanifold
> A [[§35 Regular Submanifolds#^def-35-1|regular submanifold]] $S \subseteq N$, with the subspace topology and its induced smooth structure ([[§35 Regular Submanifolds#^prop-35-2|Proposition §35.2]]), is an [[§38 Embeddings#^def-38-4|immersed submanifold]] of $N$.

^prop-38-13

> [!proof]+ Proof
> *(Not from lecture.)* Check Definition [[§38 Embeddings#^def-38-4|§38.4]]. With the subspace topology and the induced smooth structure, $S$ is a topological manifold and a smooth manifold (Proposition [[§35 Regular Submanifolds#^prop-35-2|§35.2]]). The inclusion $\iota : S \hookrightarrow N$ is smooth (Lemma [[§35 Regular Submanifolds#^lem-35-3|§35.3]]) and $\iota_{\ast p}$ is injective at every $p \in S$ (Proposition [[§35 Regular Submanifolds#^prop-35-4|§35.4]]), so $\iota$ is a smooth immersion (Definition [[§37 Immersions#^def-37-1|§37.1]]).
^pf-38-13

*Uses:* [[§38 Embeddings#^def-38-4|Def. §38.4]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]], [[§35 Regular Submanifolds#^prop-35-2|§35.2]], [[§35 Regular Submanifolds#^lem-35-3|§35.3]], [[§35 Regular Submanifolds#^prop-35-4|§35.4]], [[§37 Immersions#^def-37-1|Def. §37.1]]

> [!theorem] Proposition §38.14: When an Immersed Submanifold Is Regular
> Let $F : M \to N$ be an injective immersion, and give $S = F(M)$ the structure of [[§38 Embeddings#^prop-38-12|Proposition §38.12]]. The following are equivalent:
> 1. $F$ is an [[§38 Embeddings#^def-38-1|embedding]] ([[§38 Embeddings#^def-38-1|Definition §38.1]]);
> 2. the topology of $S$ is the subspace topology;
> 3. $S$ is a [[§35 Regular Submanifolds#^def-35-1|regular submanifold]] of $N$ whose induced smooth structure is the structure of [[§38 Embeddings#^prop-38-12|Proposition §38.12]].

^prop-38-14

> [!proof]+ Proof
> *(Not from lecture.)* Write $\mathcal{T}_S$ for the topology of Proposition [[§38 Embeddings#^prop-38-12|§38.12]] and $\mathcal{T}_{\mathrm{sub}}$ for the subspace topology on $S$. We show (1) $\Leftrightarrow$ (2), (1) $\Rightarrow$ (3) and (3) $\Rightarrow$ (2), which together give all the equivalences.
>
> *(1) $\Leftrightarrow$ (2).* The topology of $S$ is the one for which $F : M \to S$ is a homeomorphism; it equals the subspace topology exactly when $F$ is a homeomorphism onto its image with the subspace topology, which, for an immersion, is the definition of an embedding. In detail: $F$ is an immersion by hypothesis, so by Definition [[§38 Embeddings#^def-38-1|§38.1]], (1) says that $F : M \to (S, \mathcal{T}_{\mathrm{sub}})$ is a homeomorphism. If $\mathcal{T}_S = \mathcal{T}_{\mathrm{sub}}$, this holds, because $F : M \to (S, \mathcal{T}_S)$ is a homeomorphism (Proposition [[§38 Embeddings#^prop-38-12|§38.12]]). Conversely, if $F : M \to (S, \mathcal{T}_{\mathrm{sub}})$ is a homeomorphism, then for $U \subseteq S$, by Proposition [[§1 Point-Set Topology Review#^prop-1-5|§1.5]](2) applied to both homeomorphisms,
>
> $$
> U \in \mathcal{T}_{\mathrm{sub}} \iff F^{-1}(U) \text{ is open in } M \iff U \in \mathcal{T}_S ,
> $$
>
> so $\mathcal{T}_S = \mathcal{T}_{\mathrm{sub}}$.
>
> *(1) $\Rightarrow$ (3).* $S$ is a regular submanifold by Theorem [[§38 Embeddings#^thm-38-1|§38.1]], and $F : M \to S$ is a diffeomorphism for its induced structure by Corollary [[§38 Embeddings#^cor-38-3|§38.3]]. By the uniqueness in Proposition [[§38 Embeddings#^prop-38-12|§38.12]] — exactly one topology and smooth structure on $S$ make $F : M \to S$ a diffeomorphism — the two structures coincide.
>
> *(3) $\Rightarrow$ (2).* The induced structure of a regular submanifold has the subspace topology (Proposition [[§35 Regular Submanifolds#^prop-35-2|§35.2]], and Definition [[§35 Regular Submanifolds#^def-35-1|§35.1]], where $S$ carries the subspace topology). By (3) the induced structure is the structure of Proposition [[§38 Embeddings#^prop-38-12|§38.12]], so its topology $\mathcal{T}_S$ is $\mathcal{T}_{\mathrm{sub}}$.
^pf-38-14

*Uses:* [[§38 Embeddings#^def-38-1|Def. §38.1]], [[§38 Embeddings#^prop-38-12|§38.12]], [[§38 Embeddings#^thm-38-1|§38.1]], [[§38 Embeddings#^cor-38-3|§38.3]], [[§35 Regular Submanifolds#^prop-35-2|§35.2]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§35 Regular Submanifolds#^def-35-1|Def. §35.1]]

> [!example] Example §38.1: Immersed but Not Regular
> 1. *The figure-eight.* $\beta(t) = (\sin 2t, \sin t)$, $t \in (-\pi, \pi)$ (Lee, Example 4.19), is an injective immersion, so its image is an [[§38 Embeddings#^def-38-4|immersed submanifold]] of $\mathbb{R}^2$ ([[§38 Embeddings#^prop-38-12|Proposition §38.12]]). It is not a regular submanifold: in the subspace topology every small neighbourhood of the origin in the image is an X — the strand through $\beta(0)$ and the two ends returning as $t \to \pm\pi$ — and removing the origin leaves four components, which cannot happen in a $1$-manifold (as in [[§37 Immersions#^ex-37-1|Example §37.1]]).
> 2. *The irrational line.* The curve $\gamma$ of [[§38 Embeddings#^prop-38-11|Proposition §38.11]] is an injective immersion, so its image is an immersed submanifold of $T^2$, a copy of $\mathbb{R}$ in its own topology. It is not a regular submanifold. The image is dense, so if it were regular it would be open in $T^2$ ([[§38 Embeddings#^cor-38-8|Corollary §38.8]]). But a nonempty open subset of $T^2$ containing $(e^{2\pi i a}, w)$ meets the circle $\{e^{2\pi i a}\} \times S^1$ in an open arc, which is uncountable, while the image meets that circle only in the countable set $\{\gamma(a + k) : k \in \mathbb{Z}\}$.

^ex-38-1

In the immersed topology, a short interval of the irrational line is an open subset of the image; in the subspace topology, every neighbourhood of a point of the image also contains points from arbitrarily far along the line, because the line comes back densely. That is the whole difference between the two kinds of submanifold.
