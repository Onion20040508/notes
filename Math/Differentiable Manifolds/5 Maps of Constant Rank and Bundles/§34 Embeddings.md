---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 5
section: 34
tags: [differentiable-manifolds, math591]
---
← [[§33 Immersions]] · ↑ [[· 5 Maps of Constant Rank and Bundles]] · [[§35 Worked Example꞉ The Double Cover SU(2) → SO(3)]] →

*Stage: maps — Immersions that are homeomorphisms onto their images — their images are submanifolds.*

*References: Lee Ch. 4 and Ch. 5. Lecture 14.*

The normal form makes every immersion locally an inclusion, but an immersion's image can still fail to be a submanifold ([[§33 Immersions|§33]]). Embeddings are the immersions for which it cannot: the normal form is local in the domain, and the topological condition makes it local in the image too.

## Embeddings and Their Images

> [!definition] Definition §34.1: Embedding
> A smooth map ([[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]) $F : M \to N$ is an **embedding** if it is an immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) and, as a map onto its image, $F : M \to F(M)$ is a homeomorphism ([[§9 Continuous Functions#^def-9-2|590 Def. §9.2]]), $F(M)$ carrying the subspace topology ([[§3 Subspaces and Products#^def-3-1|Def. §3.1]]) of $N$. Injectivity is part of being a homeomorphism; Uribe wrote “(injective) immersion” and called the word redundant.
>
> *Lee: Ch. 4, Embeddings*

^def-34-1

> [!remark]- Connections
> - Announced at the end of Lecture 13: [[§33 Immersions#^rem-33-1|Remark: Embeddings — Next Time (§33)]]; the two ways an immersion's image can fail to be a submanifold: [[§33 Immersions#^ex-33-1|Ex. §33.1]], [[§33 Immersions#^ex-33-2|Ex. §33.2]].
> - Homeomorphisms in 590: [[§9 Continuous Functions#^def-9-2|590 Def. §9.2]].

![[m591-33-1.svg]]
*An embedding factors through its image as a homeomorphism followed by the inclusion — “you're taking the manifold $M$ and you're putting it inside $N$.” The figure-eight of Lee's Example 4.19 ([[§33 Immersions#Images of Immersions|§33]]) is an injective immersion for which the top arrow is not a homeomorphism.*

> [!example] Example §34.1: The Irrational Line on the Torus
> For $\alpha$ irrational, $F : \mathbb{R} \to T^2 = \mathbb{R}^2/\mathbb{Z}^2$ (the [[Torus|torus]]), $F(t) = [t, \alpha t]$, is an injective immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) whose image is dense in $T^2$. Its image is not a regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) of $T^2$, so $F$ is not an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]).
>
> *Lee: Example 4.20*

^ex-34-1

> [!remark]- Connections
> - The torus as a quotient of the square in 590: [[§12 Quotient Topology#^ex-12-3|590 Ex. §12.3]]; the covering $\mathbb{R}^2 \to T^2$, through which $F$ factors: [[§24 Covering Spaces#^ex-24-3|590 Ex. §24.3]]; all the torus's uses: [[Torus|590 Torus]].
> - Locally the image is still a submanifold: [[§33 Immersions#^cor-33-2|§33.2]].
> - The properties proved: [[§34 Embeddings#^prop-34-11|§34.11]].

*Status.* Given in lecture as “a very important category: non-examples”; the properties are proved in [[§34 Embeddings#^prop-34-11|Proposition §34.11]] below, from Assignment 4, Problem 5. “You're wrapping a line, but the slope of the line is irrational, so it never closes … like one of those spirographs.” The normal form still applies: around any $p$ there are neighbourhoods $U$ and $V$ for which $F(U)$ is “a very nice submanifold.” But “it's local in the domain”, while being a submanifold is a statement about the whole image. Points outside $U$ “contribute segments like this, and they're going to be dense. No matter how you shrink this $V$, you won't be able to isolate only the yellow guy.”

![[m591-33-2.svg]]
*The irrational line, drawn here with $\alpha = (\sqrt5 - 1)/2$. Left: nine turns of $F(\mathbb{R})$ in the square, whose opposite sides are identified; the orange piece is $F(U)$, and two other strands already cross the neighbourhood $V$. Right: a disc around $F(p)$ about $4.6$ times smaller, and the first 400 turns of the curve, which cross it in 34 strands. Shrinking further only takes more turns: every neighbourhood of $F(p)$ meets infinitely many strands.*

> [!theorem] Theorem §34.1: The Image of an Embedding Is a Submanifold
> If $F : M \to N$ is an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]), with $\dim M = m$ and $\dim N = n$, then $F(M)$ is a regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) of $N$ of codimension $n - m$.
>
> *Lee: Proposition 5.2*

^thm-34-1

> [!proof]+ Proof
> *(Lecture 14. The final equality is completed with [[§33 Immersions#^cor-33-2|Corollary §33.2]]; see [[§34 Embeddings#^rem-34-1|the remark after the proof]].)* Let $q = F(p) \in F(M)$. We need a chart of $N$ at $q$ in which $F(M)$ is cut out by the vanishing of the last $n - m$ coordinates.
>
> *Start with the normal form.* Take the charts $(U, \varphi)$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $q$ of [[§33 Immersions#^thm-33-1|Theorem §33.1]]. By [[§33 Immersions#^cor-33-2|Corollary §33.2]], after replacing $V$ by the smaller open set
>
> $$
> V' = \big\{\, x \in V : \big(y^1(x), \ldots, y^m(x)\big) \in \varphi(U) \,\big\},
> $$
>
> we have
>
> $$
> F(U) = \{\, x \in V' : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\}. \tag{$*$}
> $$
>
> This describes $F(U)$, not $F(M) \cap V'$: “other pieces of the image” may still pass through $V'$, as in the irrational line.
>
> *The key step: the topological hypothesis.* “Here's where we use the very strong condition that $F$ is a topological homeomorphism to its image.” $U$ is open in $M$ and $F : M \to F(M)$ is a homeomorphism, so $F(U)$ is open in $F(M)$: there is an open $W \subseteq N$ with
>
> $$
> F(U) = W \cap F(M) .
> $$
>
> *Shrink $V'$ to $V' \cap W$, and keep the same coordinates.* Since $F(U) \subseteq V' \cap W$,
>
> $$
> F(M) \cap (V' \cap W) = F(U) = \{\, x \in V' \cap W : y^{m+1}(x) = \cdots = y^n(x) = 0 \,\},
> $$
>
> the first equality because $F(M) \cap W = F(U) \subseteq V'$, the second by $(*)$ intersected with $W$. So $(V' \cap W, \psi)$ is an adapted chart at $q$ ([[§30 Submanifolds#^def-30-1|Definition §30.1]]), and $F(M)$ is a submanifold of codimension $n - m$.

^pf-34-1

*Uses:* [[§34 Embeddings#^def-34-1|Def. §34.1]], [[§33 Immersions#^thm-33-1|§33.1]], [[§33 Immersions#^cor-33-2|§33.2]], [[§30 Submanifolds#^def-30-1|Def. §30.1]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§9 Continuous Functions#^prop-9-2|590 §9.2]]

![[m591-33-3.svg]]
*The key step. $V$ may contain other parts of $F(M)$ (black) besides $F(U)$ (orange). Because $F(U)$ is open in $F(M)$, it is $W \cap F(M)$ for an open $W$ (shaded), and $W$ cuts the other parts away; $F(M)$ continues beyond $F(U)$ only by leaving $W$. For the irrational line no such $W$ exists, which is exactly the failure of openness.*

> [!remark]- Connections
> - Submanifolds and adapted charts: [[§30 Submanifolds#^def-30-1|Def. §30.1]]; the other main source of submanifolds, level sets: [[§30 Submanifolds#^thm-30-6|§30.6]].
> - The local statement this globalizes: [[§33 Immersions#^cor-33-2|§33.2]], from the [[Immersion Normal Form]].

**Transcription note.** Page 39 of the handwritten notes writes the target as $F(M) \cap V = \{0 = y^{n-m+1} = \cdots = y^m\}$; the vanishing coordinates are the last $n - m$ of them, $y^{m+1}, \ldots, y^n$, as the lecture said.

> [!remark] Remark: Where Is Injectivity Used?
> In lecture the last equality caused trouble, and a discussion. Uribe first located the use of injectivity there; a student pointed out that $(*)$ concerns only $F(U)$, and that the proof seems to need only that $F$ be an immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) which is open ([[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]]) onto its image. Another student added covering-type examples: maps that are not injective but whose images are manifolds, such as $\mathbb{R} \to S^1$, $t \mapsto (\cos t, \sin t)$ ([[§28 Local Diffeomorphisms#^ex-28-1|Ex. §28.1]]), or the two-to-one map $S^2 \to \mathbb{RP}^2$ ([[§28 Local Diffeomorphisms#^ex-28-2|Ex. §28.2]]). Uribe agreed — “I don't think we're using injectivity” — and promised “a definite conclusion by email.”
>
> *The conclusion, from Uribe's follow-up email.* The students were right: “a proof that we did today does show that for an immersion that is open as a map onto its image (so for all $U$ open in $M$, $F(U)$ is open in $F(M)$), $F(M)$ is a submanifold. The map $F$ does not have to be injective.” The proof uses exactly two things: the normal form (the immersion hypothesis), and that $F(U)$ is open in $F(M)$ for the $U$ of the normal form; with the completion via [[§33 Immersions#^cor-33-2|Corollary §33.2]] nothing else enters. Injectivity belongs to the *idea* of an embedding — “the idea of an embedding is that it is an isomorphism between $M$ and its image” ([[§34 Embeddings#^cor-34-3|Corollary §34.3]]) — not to this proof. He added that “being an immersion and an open map onto its image” is “an unusual class of maps.”

^rem-34-1

> [!theorem] Proposition §34.2: Immersions That Are Open onto Their Images
> Let $F : M \to N$ be an immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) such that $F : M \to F(M)$ is an open map ([[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]]), $F(M)$ carrying the subspace topology ([[§3 Subspaces and Products#^def-3-1|Def. §3.1]]). Then $F(M)$ is a regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) of $N$ of codimension $n - m$.

^prop-34-2

> [!proof]+ Proof
> *(The conclusion of the class discussion, confirmed in Uribe's follow-up email.)* The proof of [[§34 Embeddings#^thm-34-1|Theorem §34.1]], word for word: openness of $F$ onto its image is all it used to produce $W$. For example, $t \mapsto (\cos t, \sin t)$ is an immersion of $\mathbb{R}$, open onto $S^1$ and far from injective — every point of $S^1$ has infinitely many preimages — and its image $S^1$ is a submanifold of $\mathbb{R}^2$. The figure-eight is not open onto its image, consistent with its image not being a submanifold.

^pf-34-2

*Uses:* [[§34 Embeddings#^pf-34-1|proof of §34.1]], [[§33 Immersions#^thm-33-1|§33.1]], [[§33 Immersions#^cor-33-2|§33.2]], [[§30 Submanifolds#^def-30-1|Def. §30.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§28 Local Diffeomorphisms#^ex-28-1|Ex. §28.1]], [[§29 Submersions#^cor-29-6|§29.6]], [[§33 Immersions#^ex-33-2|Ex. §33.2]]

> [!theorem] Corollary §34.3: An Embedding Is a Diffeomorphism onto Its Image
> If $F : M \to N$ is an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]), then $F : M \to F(M)$ is a diffeomorphism ([[§15 Smooth Functions and Smooth Maps#^def-15-3|Def. §15.3]]), $F(M)$ carrying its induced smooth structure as a submanifold ([[§30 Submanifolds#^prop-30-2|§30.2]]).

^cor-34-3

> [!proof]+ Proof
> *(Stated in Lecture 14 — “an embedding restricts to a diffeomorphism between $M$ and the image”; filled in.)* $F : M \to F(M)$ is smooth by [[§30 Submanifolds#^lem-30-3|Lemma §30.3]](2), and it is an immersion: its differential followed by the injective $\iota_{\ast}$ is the injective $F_{\ast}$. Both manifolds have dimension $m$, so it is a local diffeomorphism ([[§29 Submersions#^prop-29-1|Proposition §29.1]](3)); being bijective, it is a diffeomorphism, its inverse being smooth near every point.

^pf-34-3

*Uses:* [[§34 Embeddings#^thm-34-1|§34.1]], [[§30 Submanifolds#^prop-30-2|§30.2]], [[§30 Submanifolds#^lem-30-3|§30.3]], [[§30 Submanifolds#^prop-30-4|§30.4]], [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§29 Submersions#^prop-29-1|§29.1]], [[§28 Local Diffeomorphisms#^cor-28-3|§28.3]]

## Proper Maps

*Lecture 14. When is an injective immersion an embedding? The homeomorphism condition is point-set topology, and a convenient sufficient condition is properness — the same hypothesis as in Ehresmann's theorem ([[§31 Fibrations#^thm-31-3|Theorem §31.3]]).*

> [!definition] Definition §34.2: Proper Map
> A continuous map $F : X \to Y$ is **proper** if $F^{-1}(K)$ is compact ([[§15 Compact Spaces#^def-15-2|590 Def. §15.2]]) for every compact $K \subseteq Y$.
>
> *Lee: App. A, Proper Maps*

^def-34-2

> [!remark]- Connections
> - The same definition, given earlier for proper actions: [[§10 Group Actions and Orbit Spaces#^def-10-6|Def. §10.6]].
> - The properness hypothesis of [[§31 Fibrations#^thm-31-3|Ehresmann's theorem, §31.3]].

> [!theorem] Proposition §34.4: Proper Maps into Manifolds Are Closed
> Let $F : M \to N$ be a continuous proper map ([[§34 Embeddings#^def-34-2|Def. §34.2]]), $N$ a topological manifold ([[§2 Topological Manifolds#^def-2-2|Def. §2.2]]). Then $F$ is closed ([[§12 Quotient Topology#^def-12-4|590 Def. §12.4]]): $F(C)$ is closed in $N$ for every closed $C \subseteq M$.
>
> *Lee: Theorem A.57*

^prop-34-4

> [!proof]+ Proof
> *(Lecture 14 — “it's a very funny proof. You go back and forth literally.” Uribe did not finish Claim 2 in lecture and sent the complete proof in his follow-up email; the completion of Claim 2 below is the notes' own.)* Let $C \subseteq M$ be closed.
>
> *Claim 1: $F(C) \cap K$ is closed for every compact $K \subseteq N$.* $F^{-1}(K)$ is compact, so $C \cap F^{-1}(K)$, a closed subset of it, is compact; its image $F\big(C \cap F^{-1}(K)\big)$ is compact, hence closed in the Hausdorff space $N$. And $F\big(C \cap F^{-1}(K)\big) = F(C) \cap K$: a point of the left side is $F(c)$ with $c \in C$ and $F(c) \in K$, and conversely.
>
> *Claim 2.* Let $q \in \overline{F(C)}$, and let $V$ be a neighbourhood of $q$ with compact closure ([[§2 Topological Manifolds#^prop-2-13|Proposition §2.13]]). Then $q \in \overline{F(C) \cap \overline V}$. *(Completion.)* If $O$ is any open set containing $q$, then $O \cap V$ is an open set containing $q$, so it meets $F(C)$; hence $O$ meets $F(C) \cap V \subseteq F(C) \cap \overline V$.
>
> *Conclusion.* By Claim 1 with $K = \overline V$, the set $F(C) \cap \overline V$ is closed, so it equals its closure, and $q \in F(C) \cap \overline V \subseteq F(C)$. Thus $\overline{F(C)} = F(C)$.

^pf-34-4

*Uses:* [[§34 Embeddings#^def-34-2|Def. §34.2]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§2 Topological Manifolds#^prop-2-13|§2.13]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§15 Compact Spaces#^thm-15-2|590 §15.2]], [[§15 Compact Spaces#^thm-15-3|590 §15.3]], [[§15 Compact Spaces#^thm-15-4|590 §15.4]], [[§7 Interior and Closure#^thm-7-3|590 §7.3]]

> [!remark]- Connections
> - The closed-map argument for compact domains in 590, which Claim 1 localizes: [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]]; closed maps: [[§12 Quotient Topology#^def-12-4|590 Def. §12.4]].
> - Local compactness in 590: [[§17 Local Compactness#^def-17-1|590 Def. §17.1]], [[§17 Local Compactness#^thm-17-6|590 §17.6]].

> [!theorem] Theorem §34.5: Injective Proper Immersions Are Embeddings
> An injective proper ([[§34 Embeddings#^def-34-2|Def. §34.2]]) immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) $F : M \to N$ is an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]).
>
> *Lee: Proposition 4.22*

^thm-34-5

> [!proof]+ Proof
> *(Lecture 14 reduced this to [[§34 Embeddings#^prop-34-4|Proposition §34.4]]; the last step is filled in.)* It remains to see that $F : M \to F(M)$ is a homeomorphism. It is a continuous bijection. If $C \subseteq M$ is closed, then $F(C)$ is closed in $N$ by [[§34 Embeddings#^prop-34-4|Proposition §34.4]], hence $F(C) = F(C) \cap F(M)$ is closed in $F(M)$. So the inverse $F(M) \to M$ is continuous.

^pf-34-5

*Uses:* [[§34 Embeddings#^def-34-1|Def. §34.1]], [[§34 Embeddings#^prop-34-4|§34.4]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§6 Closed Sets and Limit Points#^thm-6-2|590 §6.2]], [[§9 Continuous Functions#^thm-9-1|590 §9.1]]

> [!theorem] Corollary §34.6: Injective Immersions of Compact Manifolds
> If $M$ is compact ([[§15 Compact Spaces#^def-15-2|590 Def. §15.2]]), every injective immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) $F : M \to N$ is an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]).
>
> *Lee: Proposition 4.22*

^cor-34-6

> [!proof]+ Proof
> *(Uribe's follow-up email: “Note that $F$ is proper if $M$ is compact, a fact that can be very useful!”; the proof is filled in.)* $F$ is proper: if $K \subseteq N$ is compact, it is closed, so $F^{-1}(K)$ is closed in the compact $M$, hence compact. Apply [[§34 Embeddings#^thm-34-5|Theorem §34.5]].

^pf-34-6

*Uses:* [[§34 Embeddings#^def-34-2|Def. §34.2]], [[§34 Embeddings#^thm-34-5|§34.5]], [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§15 Compact Spaces#^thm-15-4|590 §15.4]], [[§15 Compact Spaces#^thm-15-2|590 §15.2]]

> [!remark]- Connections
> - The topological prototype: a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism, [[Bijection from Compact to Hausdorff is a Homeomorphism|590 §15.7]] (in 591: [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](6)).

*An aside from the end of the lecture.* Uribe mentioned that he is developing his own notes for the course, “based on notes that somebody took a few years ago”, edited “the night before”, and asked whether they would help, perhaps shared through Overleaf.

## Closedness and Density

*Why does density of the irrational line rule out an embedding? Because the image of an embedding is always closed* locally, *and a dense set that is locally closed is open. Prompted by Assignment 4, Problem 5.*

> [!definition] Definition §34.3: Locally Closed Subset
> A subset $S$ of a topological space $N$ is **locally closed** if every point of $S$ has an open neighbourhood $V$ in $N$ such that $S \cap V$ is closed in $V$ ([[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§6 Closed Sets and Limit Points#^def-6-1|590 Def. §6.1]]). Equivalently, $S$ is closed in some open subset of $N$ containing it, namely the union $U$ of these $V$'s.

^def-34-3

> [!remark]- Connections
> - Closed sets and closed sets of a subspace in 590: [[§6 Closed Sets and Limit Points#^def-6-1|590 Def. §6.1]], [[§6 Closed Sets and Limit Points#^thm-6-2|590 §6.2]]; the subspace topology: [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]].

> [!theorem] Proposition §34.7: Images of Embeddings Are Locally Closed
> Every regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) of $N$ — in particular the image of an embedding ([[§34 Embeddings#^thm-34-1|Theorem §34.1]]) — is locally closed ([[§34 Embeddings#^def-34-3|Def. §34.3]]) in $N$.

^prop-34-7

> [!proof]+ Proof
> *(Not from lecture; filled in.)* At each point of the submanifold $S$ there is an adapted chart $(V, \psi)$ ([[§30 Submanifolds#^def-30-1|Definition §30.1]]), in which $S \cap V = \{x \in V : y^{m+1}(x) = \cdots = y^n(x) = 0\}$, a closed subset of $V$ as the zero set of continuous functions. For the equivalence in the definition: if $U$ is the union of these $V$, a point of $U \setminus S$ lies in some $V \setminus S$, which is open, so $U \setminus S$ is open and $S$ is closed in $U$.

^pf-34-7

*Uses:* [[§34 Embeddings#^def-34-3|Def. §34.3]], [[§30 Submanifolds#^def-30-1|Def. §30.1]], [[§34 Embeddings#^thm-34-1|§34.1]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§9 Continuous Functions#^thm-9-1|590 §9.1]], [[§6 Closed Sets and Limit Points#^def-6-1|590 Def. §6.1]]

> [!theorem] Corollary §34.8: Dense Submanifolds Are Open
> A dense ([[§18 Countability Axioms#^def-18-4|590 Def. §18.4]]) regular submanifold ([[§30 Submanifolds#^def-30-1|Def. §30.1]]) $S$ of $N$ is an open subset of $N$, and has codimension $0$. In particular, the image of an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]) $F : M \to N$ with $\dim M < \dim N$ is never dense.

^cor-34-8

> [!proof]+ Proof
> *(Not from lecture; filled in.)* By [[§34 Embeddings#^prop-34-7|Proposition §34.7]], $S$ is closed in an open $U \supseteq S$. $S$ is dense in $N$, hence in $U$, and a closed dense subset of $U$ is all of $U$; so $S = U$ is open. If $S$ had codimension $k \ge 1$, take an adapted chart $(V, \psi)$ at a point of $S$: then $\psi(S \cap V)$ would be a nonempty subset of $\mathbb{R}^{n-k} \times \{0\}$, open in $\mathbb{R}^n$ because $S \cap V$ is open in $V$ — impossible, since no nonempty open subset of $\mathbb{R}^n$ lies in a hyperplane.

^pf-34-8

*Uses:* [[§34 Embeddings#^prop-34-7|§34.7]], [[§34 Embeddings#^def-34-3|Def. §34.3]], [[§30 Submanifolds#^def-30-1|Def. §30.1]], [[§34 Embeddings#^thm-34-1|§34.1]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]], [[§18 Countability Axioms#^def-18-4|590 Def. §18.4]], [[§7 Interior and Closure#^thm-7-2|590 §7.2]]

> [!remark]- Connections
> - Dense subsets in 590: [[§18 Countability Axioms#^def-18-4|590 Def. §18.4]], with the [[Closure Characterization|590 closure characterization]].

This is the precise form of Uribe's “no matter how you shrink $V$, you won't be able to isolate only the yellow guy”: at every point of [[§34 Embeddings#^ex-34-1|the irrational line]], local closedness fails.

> [!theorem] Proposition §34.9: Closed Embeddings Are the Proper Ones
> An embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]) $F : M \to N$ is proper ([[§34 Embeddings#^def-34-2|Def. §34.2]]) if and only if its image $F(M)$ is closed in $N$. In particular, an injective proper immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]) is exactly an embedding with closed image.
>
> *Lee: Proposition 5.5*

^prop-34-9

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $F$ is proper, it is closed ([[§34 Embeddings#^prop-34-4|Proposition §34.4]]), so $F(M)$ is closed. Conversely, let $F(M)$ be closed and $K \subseteq N$ compact. Then $K \cap F(M)$ is a closed subset of $K$, hence compact, and $F^{-1}(K) = F^{-1}\big(K \cap F(M)\big)$ is its image under the inverse of the homeomorphism $F : M \to F(M)$, hence compact. The last sentence combines this with [[§34 Embeddings#^thm-34-5|Theorem §34.5]].

^pf-34-9

*Uses:* [[§34 Embeddings#^def-34-1|Def. §34.1]], [[§34 Embeddings#^def-34-2|Def. §34.2]], [[§34 Embeddings#^prop-34-4|§34.4]], [[§34 Embeddings#^thm-34-5|§34.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§6 Closed Sets and Limit Points#^thm-6-2|590 §6.2]], [[§15 Compact Spaces#^thm-15-2|590 §15.2]], [[§15 Compact Spaces#^thm-15-3|590 §15.3]]

| Map | Image | Example separating it from the row above |
|---|---|---|
| injective proper immersion | closed regular submanifold | — |
| embedding | locally closed regular submanifold | an open interval embedded in $\mathbb{R}^2$ |
| injective immersion | possibly not locally closed, even dense | [[§34 Embeddings#^prop-34-11\|the irrational line]] |

Closedness of the image alone is not enough: the image of the [[§33 Immersions#^ex-33-2|figure-eight]] (Lee's Example 4.19) is compact, hence closed, but the figure-eight is not an embedding. Local closedness is necessary for an embedding, not sufficient.

> [!theorem] Lemma §34.10: Dirichlet's Approximation Theorem
> For every $\alpha \in \mathbb{R}$ and every integer $N \ge 1$ there are integers $n, m$ with $1 \le n \le N$ and $|n\alpha - m| < 1/N$.
>
> *Lee: Lemma 4.21*

^lem-34-10

> [!remark]- Connections
> - No home elsewhere in the vault; Lee's proof rests on the [[Pigeonhole Principle|250 Pigeonhole Principle]].

*Status.* Used in Assignment 4, Problem 5, citing Lee; not proved here. (Lee's proof is a [[Pigeonhole Principle|pigeonhole]] argument on the fractional parts of $0, \alpha, \ldots, N\alpha$.)

> [!theorem] Proposition §34.11: The Irrational Line Revisited
> Let $\alpha$ be irrational and $\gamma : \mathbb{R} \to T^2 = S^1 \times S^1$, $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$ — the curve of [[§34 Embeddings#^ex-34-1|Example §34.1]] under the identification $[x, y] \mapsto (e^{2\pi i x}, e^{2\pi i y})$. Then $\gamma$ is an injective immersion ([[§33 Immersions#^def-33-1|Def. §33.1]]), its image is dense ([[§18 Countability Axioms#^def-18-4|590 Def. §18.4]]) in $T^2$, and $\gamma$ is not an embedding ([[§34 Embeddings#^def-34-1|Def. §34.1]]).
>
> *Lee: Example 4.20*

^prop-34-11

> [!proof]+ Proof
> *(Assignment 4, Problem 5: the submitted solution, condensed; the second proof of the last claim is new.)* *Immersion.* $\gamma$ is smooth into $\mathbb{C}^2$ with values in the submanifold $T^2$, hence smooth into $T^2$ ([[§30 Submanifolds#^lem-30-3|Lemma §30.3]]). Its velocity in $\mathbb{C}^2$, $\big(2\pi i e^{2\pi i t}, 2\pi i\alpha e^{2\pi i \alpha t}\big)$, has first entry of modulus $2\pi \ne 0$, so by the chain rule $\gamma_{\ast t}$ is nonzero, hence injective.
>
> *Injective.* If $\gamma(t_1) = \gamma(t_2)$, then $t_1 - t_2 \in \mathbb{Z}$ and $\alpha(t_1 - t_2) \in \mathbb{Z}$; if $t_1 \ne t_2$ this makes $\alpha$ rational.
>
> *Dense.* Using $|e^{is} - e^{it}| \le |s - t|$: by [[§34 Embeddings#^lem-34-10|Lemma §34.10]] there are $n_N \ge 1$ and $m_N$ with $|n_N\alpha - m_N| < 1/N$, so $w_N = e^{2\pi i \alpha n_N} = e^{i\theta_N}$ with $\theta_N = 2\pi(n_N\alpha - m_N)$, $0 < |\theta_N| < 2\pi/N$ (nonzero by injectivity). The powers $w_N^k = e^{2\pi i \alpha (k n_N)}$ are $2\pi/N$-dense in $S^1$, since consecutive ones differ in angle by $|\theta_N|$. So $D = \{e^{2\pi i\alpha k} : k \in \mathbb{Z}\}$ is dense in $S^1$. Given $(e^{2\pi i a}, e^{2\pi i b}) \in T^2$, the points $\gamma(a + k) = (e^{2\pi i a}, e^{2\pi i \alpha a} e^{2\pi i \alpha k})$ have the right first coordinate, and their second coordinates come arbitrarily close to $e^{2\pi i b}$ because $D$ is dense.
>
> *Not an embedding: the submitted proof.* $\gamma(n_N) \to \gamma(0)$, since $|\gamma(n_N) - \gamma(0)| \le 2\pi|n_N\alpha - m_N| < 2\pi/N$. If $\gamma^{-1} : \gamma(\mathbb{R}) \to \mathbb{R}$ were continuous, then $n_N \to 0$, which is false because $n_N \ge 1$.
>
> *Not an embedding: via density.* The image is dense and $\dim \mathbb{R} = 1 < 2 = \dim T^2$, so by [[§34 Embeddings#^cor-34-8|Corollary §34.8]] it is not the image of an embedding.

^pf-34-11

*Uses:* [[§33 Immersions#^def-33-1|Def. §33.1]], [[§34 Embeddings#^def-34-1|Def. §34.1]], [[§34 Embeddings#^ex-34-1|Ex. §34.1]], [[§30 Submanifolds#^lem-30-3|§30.3]], [[§23 Derivations and the Abstract Tangent Space#^thm-23-6|§23.6]], [[§34 Embeddings#^lem-34-10|§34.10]], [[§34 Embeddings#^cor-34-8|§34.8]], [[§18 Countability Axioms#^def-18-4|590 Def. §18.4]]

> [!remark]- Connections
> - The same curve, stated in lecture: [[§34 Embeddings#^ex-34-1|Ex. §34.1]]; the torus in 590: [[Torus|590 Torus]], its covering by the plane: [[§24 Covering Spaces#^ex-24-3|590 Ex. §24.3]].
