---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 3
tags: [differentiable-manifolds, math591]
---
← [[§2 Topological Manifolds]] · ↑ [[1 Topological Manifolds]] · [[§4 The Regular Value Theorem]] →

*Thread: quotients — Manifolds built by gluing and identifying points; $\mathbb{CP}^n$ is the first. The thread continues with orbit spaces ([[§6 Group Actions and Orbit Spaces|§6]]) and coset spaces ([[§7 Homogeneous Spaces|§7]]), where the Hausdorff question answered here by Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|§3.26]] returns.*

*Reference: Lee Appendix A (“Subspaces, Products, Disjoint Unions, and Quotients”); MATH 590 notes [[§5 Subspace Topology|§5]] (subspaces), [[§4 Product Topology|§4]] (products), [[§12 Quotient Topology|§12]] (quotients).*

> [!remark] Remark: Why This Section
> Many of the most important manifolds are not defined by charts directly but are *constructed* out of other spaces: complex projective space, Grassmannians, moduli spaces are all quotients. Uribe: “quotients are the most important construction; a lot of really neat, important manifolds are constructed as quotients of others.” The guiding question of the lecture, for each construction, is whether the two point-set conditions in the definition of a manifold are *heritable*: if $X$ is $T_2$ and second countable, is the new space too? For subspaces and products the answer is an easy yes; for quotients *everything can go wrong*, and the substance of the lecture is a usable criterion for when it doesn't.

^rem-3-1

## Subspaces

> [!definition] Definition §3.1: Subspace Topology
> Let $X$ be a topological space and $S \subseteq X$ a subset. The **subspace topology** on $S$ is defined by: $V \subseteq S$ is open $\iff$ there exists $U \subseteq X$ open such that $V = U \cap S$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^def-3-1

> [!remark]- Connections
> - Home in MATH 590: [[§5 Subspace Topology#^def-5-1|590 Def. §5.1]].

> [!remark] Remark
> In 590 [[§5 Subspace Topology#^def-5-1|§5]] the same topology was defined by naming it as a collection, $\mathcal{T}_S = \{\, U \cap S \mid U \in \mathcal{T} \,\}$; [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-1|Definition §3.1]] just says which sets belong to it. Three facts about it from 590 are used repeatedly in these notes and are recorded here with proofs.

^rem-3-2

> [!theorem] Lemma §3.1: Basis of a Subspace
> If $\mathcal{B}$ is a basis for $X$ and $S \subseteq X$, then $\mathcal{B}_S = \{\, B \cap S \mid B \in \mathcal{B} \,\}$ is a basis for the subspace topology on $S$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^lem-3-1

> [!proof]+ Proof
> Each $B \cap S$ is open in $S$ by definition. Let $V$ be open in $S$ and $p \in V$; write $V = U \cap S$ with $U$ open in $X$. Since $p \in U$, there is $B \in \mathcal{B}$ with $p \in B \subseteq U$, and then $p \in B \cap S \subseteq U \cap S = V$. This is [[§1 Point-Set Topology Review#^def-1-1|Definition §1.1]].

^pf-3-1

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-1|Def. §3.1]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - Home in MATH 590: [[§5 Subspace Topology#^lem-5-1|590 §5.1 (Basis for Subspace Topology)]].

> [!theorem] Lemma §3.2: Open in Open is Open
> Let $S \subseteq X$ be open in $X$. If $V \subseteq S$ is open in the subspace topology of $S$, then $V$ is open in $X$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^lem-3-2

> [!proof]+ Proof
> $V = U \cap S$ for some $U$ open in $X$, and $U \cap S$ is an intersection of two open subsets of $X$.

^pf-3-2

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - Home in MATH 590: [[§5 Subspace Topology#^lem-5-2|590 §5.2]]; closed analogue [[§6 Closed Sets and Limit Points#^thm-6-3|590 §6.3]], used in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-25|§3.25]].

> [!theorem] Proposition §3.3: Universal Property of the Subspace Topology
> Let $S \subseteq X$ carry the subspace topology and let $\iota : S \hookrightarrow X$ be the inclusion.
> 1. $\iota$ is continuous, and the subspace topology is the coarsest topology on $S$ for which it is.
> 2. For any topological space $Z$ and any function $f : Z \to S$,
>
> $$
> f \text{ is continuous} \iff \iota \circ f : Z \to X \text{ is continuous.}
> $$
>
> *Lee: Proposition A.17(a)*

^prop-3-3

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (1) For $U$ open in $X$, $\iota^{-1}(U) = U \cap S$ is open in $S$, so $\iota$ is continuous. If $\mathcal{T}'$ is any topology on $S$ making $\iota$ continuous, then $\mathcal{T}'$ contains $\iota^{-1}(U) = U \cap S$ for every open $U \subseteq X$, i.e. $\mathcal{T}'$ contains every open set of the subspace topology.
>
> (2) ($\Rightarrow$) Composition of continuous maps. ($\Leftarrow$) Let $V$ be open in $S$, $V = U \cap S$ with $U$ open in $X$. Since $f$ takes values in $S$,
>
> $$
> f^{-1}(V) = f^{-1}(U \cap S) = f^{-1}(U) = \{z \mid f(z) \in U\} = \{z \mid \iota(f(z)) \in U\} = (\iota \circ f)^{-1}(U),
> $$
>
> which is open in $Z$.

^pf-3-3

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-1|Def. §3.1]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]]

> [!remark]- Connections
> - In MATH 590 these are the inclusion and range rules of [[§9 Continuous Functions#^thm-9-4|590 §9.4 (Rules for Continuous Functions)]].

> [!theorem] Corollary §3.4: The Universal Property Characterizes the Subspace Topology
> The subspace topology is the unique topology $\mathcal{T}$ on $S$ such that, for every space $Z$, a map $f : Z \to (S, \mathcal{T})$ is continuous if and only if $\iota \circ f : Z \to X$ is continuous.
>
> *Lee: Proposition A.17(b)*

^cor-3-4

> [!proof]+ Proof
> The subspace topology has the property by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-3|Proposition §3.3]](2). Suppose $\mathcal{T}$ has it. Taking $Z = (S, \mathcal{T})$ and $f = \mathrm{id}$, which is continuous, $\iota$ is continuous for $\mathcal{T}$, so $\mathcal{T}$ contains the subspace topology, the coarsest such ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-3|Proposition §3.3]](1)). Taking $Z$ to be $S$ with the subspace topology and $f = \mathrm{id}$, the composite $\iota \circ \mathrm{id} = \iota$ is continuous, so the property makes $\mathrm{id}$ continuous from the subspace topology to $\mathcal{T}$, i.e. $\mathcal{T}$ is contained in the subspace topology.

^pf-3-4

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-3|§3.3]]

This completes the pattern: each of the three constructions — subspace, product ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-11|Corollary §3.11]]) and quotient ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-20|Corollary §3.20]]) — has its topology characterized by its universal property.

> [!theorem] Theorem §3.5: Subspaces Inherit Both Conditions
> Let $S \subseteq X$ carry the subspace topology.
> 1. If $X$ is $T_2$, then so is $S$.
> 2. If $X$ is second countable, then so is $S$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^thm-3-5

> [!proof]+ Proof (only sketched in lecture)
> (1) Let $p \neq q$ in $S$. Since $X$ is $T_2$, there are disjoint open sets $U \ni p$, $V \ni q$ in $X$. Then $U \cap S$ and $V \cap S$ are disjoint neighborhoods of $p$ and $q$ in $S$.
>
> (2) If $\{U_\alpha\}_{\alpha \in A}$ is a countable basis of $X$, then $\{U_\alpha \cap S\}_{\alpha \in A}$ is a basis of $S$ by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-1|Lemma §3.1]], and it is indexed by the same countable set $A$.

^pf-3-5

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-1|Def. §3.1]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-1|§3.1]]

> [!remark]- Connections
> - Home in MATH 590: second countability of subspaces is [[§18 Countability Axioms#^thm-18-3|590 §18.3]]; Hausdorff is [[§8 Hausdorff Spaces#^def-8-1|590 Def. §8.1]].
> - Already used ad hoc for spheres in [[§2 Topological Manifolds#^ex-2-4|Ex. §2.4]] and [[§2 Topological Manifolds#^prop-2-7|§2.7]]; reused for level sets in [[§4 The Regular Value Theorem#^thm-4-3|§4.3]].

> [!theorem] Proposition §3.6: Open Subsets of Manifolds Are Manifolds
> An open subset $S$ of a topological $n$-manifold $X$, with the subspace topology, is a topological $n$-manifold.
>
> *Lee: Example 1.26*

^prop-3-6

> [!proof]+ Proof
> $S$ is Hausdorff and second countable by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|Theorem §3.5]]. For $p \in S$ choose a chart $(U, \varphi)$ of $X$ at $p$. Then $U \cap S$ is open in $X$, hence in $S$, and $(U \cap S, \varphi|_{U \cap S})$ is a chart by [[§2 Topological Manifolds#^lem-2-11|Lemma §2.11]](1). [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] finishes. ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-2|Lemma §3.2]] is what makes “open in $S$” and “open in $X$” interchangeable here.)

^pf-3-6

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|§3.5]], [[§2 Topological Manifolds#^lem-2-11|§2.11]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-2|§3.2]]

> [!definition] Definition §3.2: Open Submanifold
> An **open submanifold** of a topological $n$-manifold $X$ is an open subset $S \subseteq X$ with the subspace topology — a topological $n$-manifold by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-6|Proposition §3.6]].
>
> *Lee: Example 1.26*

^def-3-2

> [!remark] Remark: What Subspaces Do Not Inherit
> Local Euclideanness is *not* hereditary: $\mathbb{R}$ is a $1$-manifold, but its subspace $\mathbb{Q}$ is not locally Euclidean ([[§2 Topological Manifolds#^ex-2-2|Example §2.2]]). By the proposition, openness is exactly what rescues it.

^rem-3-3

## Products

> [!definition] Definition §3.3: Product Topology
> Let $X, Y$ be topological spaces. The **product topology** on $X \times Y$ is the one having
>
> $$
> \mathcal{B} = \{\, U \times V \mid U \subseteq X \text{ open},\ V \subseteq Y \text{ open} \,\}
> $$
>
> as a basis.

^def-3-3

> [!remark]- Connections
> - Home in MATH 590: [[§4 Product Topology#^def-4-1|590 Def. §4.1]]; arbitrary products in [[§10 Product Topology on Arbitrary Products#^def-10-1|590 Def. §10.1]].
> - Smooth version: [[§8 Differentiable Structures#^prop-8-19|The Product Smooth Structure, §8.19]].

> [!theorem] Proposition §3.7: The Product Basis Generates a Topology
> The collection $\mathcal{B}$ of products $U \times V$ of open sets satisfies the axioms of [[§1 Point-Set Topology Review#^def-1-2|Definition §1.2]], so it is a basis for a topology on $X \times Y$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^prop-3-7

> [!proof]+ Proof
> *(Lecture 2 described the product topology by boxes — “for any point $(x,y)$ in $A$, I can fit a box”; that the boxes form a basis is filled in.)* Axiom 1 is clear, since $X \times Y \in \mathcal{B}$. Axiom 2 holds with room to spare, because $\mathcal{B}$ is closed under finite intersections:
>
> $$
> (U_1 \times V_1) \cap (U_2 \times V_2) = (U_1 \cap U_2) \times (V_1 \cap V_2).
> $$

^pf-3-7

*Uses:* [[§1 Point-Set Topology Review#^def-1-2|Def. §1.2]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]]

> [!remark]- Connections
> - Home in MATH 590: [[§4 Product Topology#^rem-4-2|590 §4, Check that 𝓑 is a basis]] and [[§4 Product Topology#^thm-4-1|590 §4.1]].

> [!theorem] Proposition §3.8: Box Characterization of Open Sets
> $A \subseteq X \times Y$ is open in the product topology if and only if
>
> $$
> \forall\, (x, y) \in A\ \ \exists \text{ neighborhoods } U \text{ of } x \text{ in } X \text{ and } V \text{ of } y \text{ in } Y \text{ such that } U \times V \subseteq A.
> $$
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^prop-3-8

![[m591-3-1.svg]]
*An open set $A \subseteq X \times Y$: every point $(x,y)$ of $A$ can be surrounded by a box $U \times V$ (dashed) that stays inside $A$.*

> [!proof]+ Proof
> If $A$ is open and $(x,y) \in A$, then by [[§1 Point-Set Topology Review#^def-1-1|Definition §1.1]] applied to the basis $\mathcal{B}$ there is a basis element $U \times V$ with $(x,y) \in U \times V \subseteq A$; that is the box. Conversely, if every point of $A$ admits such a box, then $A$ is a union of basis elements, hence open ([[§1 Point-Set Topology Review#^prop-1-1|Proposition §1.1]]).

^pf-3-8

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-7|§3.7]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^prop-1-1|§1.1]]

> [!remark] Remark: Cartoons
> Uribe on the figure above: diagrams of this kind are “incredibly important and useful”—an open set in a product is one in which every point can be surrounded by a *box*. The box picture is what actually gets used in proofs (it reappears in the second-countability part of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-12|Theorem §3.12]] and in the proof of the [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^pf-3-26|Hausdorff Criterion]] below), and he encourages drawing it every time.

^rem-3-4

> [!theorem] Proposition §3.9: Coarsest Topology with Continuous Projections
> Let $\pi_X : X \times Y \to X$ and $\pi_Y : X \times Y \to Y$ be the projection maps. The product topology is the *coarsest* topology on $X \times Y$ for which $\pi_X$ and $\pi_Y$ are both continuous.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^prop-3-9

> [!proof]+ Proof (not given in lecture)
> The product topology makes the projections continuous: $\pi_X^{-1}(U) = U \times Y$ and $\pi_Y^{-1}(V) = X \times V$ are basis elements. Conversely, let $\mathcal{T}$ be any topology on $X \times Y$ making both projections continuous. For $U \subseteq X$, $V \subseteq Y$ open, $\mathcal{T}$ contains $U \times Y$ and $X \times V$, hence their intersection $U \times V$. So $\mathcal{T}$ contains the basis $\mathcal{B}$, hence contains all unions of members of $\mathcal{B}$, i.e. every set open in the product topology. Thus the product topology is contained in every such $\mathcal{T}$.

^pf-3-9

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]]

> [!theorem] Theorem §3.10: Universal Property of the Product
> Let $Z$ be any topological space and $F : Z \to X \times Y$ a function. Then
>
> $$
> F \text{ is continuous} \iff \text{both } \pi_X \circ F \text{ and } \pi_Y \circ F \text{ are continuous.}
> $$
>
> *Lee: Proposition A.23(a)*

^thm-3-10

> [!proof]+ Proof (one direction in lecture; other filled in)
> ($\Rightarrow$) The projections are continuous, and compositions of continuous maps are continuous.
>
> ($\Leftarrow$) It suffices to check that preimages of *basis* elements are open (a preimage of a union is the union of the preimages). For $U \times V \in \mathcal{B}$,
>
> $$
> F^{-1}(U \times V) = \{z \mid \pi_X(F(z)) \in U \text{ and } \pi_Y(F(z)) \in V\} = (\pi_X \circ F)^{-1}(U) \cap (\pi_Y \circ F)^{-1}(V),
> $$
>
> an intersection of two open sets.

^pf-3-10

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-9|§3.9]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]]

> [!remark]- Connections
> - Home in MATH 590: [[§10 Product Topology on Arbitrary Products#^thm-10-1|590 §10.1 (Continuity into Product Spaces)]]; imported in [[§1 Point-Set Topology Review#^prop-1-5|§1.5]].
> - Smooth version: [[§8 Differentiable Structures#^prop-8-19|§8.19]], [[§8 Differentiable Structures#^prop-8-20|§8.20]].

> [!remark] Remark: Why the Universal Property Matters
> “To check that $F$ is continuous, you just check component by component.” Uribe flagged that the same pattern will reappear for *differentiability*: a map into a product of manifolds will be smooth iff its components are. In Lee's language this is the *characteristic property* of the product topology (Lee Prop. A.16), and it characterizes the product topology uniquely ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-11|Corollary §3.11]] below). Together with the previous proposition this gives two independent abstract descriptions of the same topology—“coarsest making projections continuous” and “the one that lets you check maps componentwise.”
>
> Compare [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-3|Proposition §3.3]]: the subspace topology is the coarsest making the inclusion continuous, and continuity of a map *into* $S$ is checked by composing with $\iota$. The quotient topology will complete the pattern in the opposite direction (Proposition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]): it is the *finest* making $\pi$ continuous, and continuity of a map *out of* $X/{\sim}$ is checked by precomposing with $\pi$.

^rem-3-5

> [!theorem] Corollary §3.11: The Universal Property Characterizes the Product Topology
> The product topology is the unique topology $\mathcal{T}$ on $X \times Y$ such that, for every space $Z$, a map $f : Z \to (X \times Y, \mathcal{T})$ is continuous if and only if $\pi_X \circ f$ and $\pi_Y \circ f$ are continuous.
>
> *Lee: Proposition A.23(b)*

^cor-3-11

> [!proof]+ Proof
> The product topology has the property by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|Theorem §3.10]]. Suppose $\mathcal{T}$ has it. Taking $Z = (X \times Y, \mathcal{T})$ and $f = \mathrm{id}$, which is continuous, the projections are continuous for $\mathcal{T}$, so $\mathcal{T}$ contains the product topology by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-9|Proposition §3.9]]. Taking $Z$ to be $X \times Y$ with the product topology and $f = \mathrm{id}$, whose components $\pi_X$ and $\pi_Y$ are continuous there, the property makes $\mathrm{id}$ continuous from the product topology to $\mathcal{T}$, i.e. $\mathcal{T}$ is contained in the product topology.

^pf-3-11

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-9|§3.9]]

> [!theorem] Theorem §3.12: Products Inherit Both Conditions
> 1. If $X$ and $Y$ are both $T_2$, then $X \times Y$ is $T_2$.
> 2. If $X$ and $Y$ are both second countable, then $X \times Y$ is second countable.
>
> *Lee: Example 1.8*

^thm-3-12

> [!proof]+ Proof (not given in lecture — “it's point-set topology”)
> (1) Let $(x, y) \neq (x', y')$; they differ in some coordinate, say $x \neq x'$ (the other case is symmetric). Choose disjoint open $U \ni x$, $U' \ni x'$ in $X$. Then $U \times Y$ and $U' \times Y$ are disjoint open neighborhoods of the two points.
>
> (2) If $\{U_\alpha\}_{\alpha \in A}$ and $\{V_\beta\}_{\beta \in B}$ are countable bases of $X$ and $Y$, then $\{U_\alpha \times V_\beta\}_{(\alpha,\beta) \in A \times B}$ is a countable collection ($A \times B$ countable), and it is a basis: given $(x,y) \in W$ open, the box characterization gives $U \times V \subseteq W$ around $(x,y)$, and then $U_\alpha \subseteq U$, $V_\beta \subseteq V$ around $x, y$ give $(x,y) \in U_\alpha \times V_\beta \subseteq W$.

^pf-3-12

*Uses:* [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-8|§3.8]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - Home in MATH 590: second countability of products is [[§18 Countability Axioms#^thm-18-3|590 §18.3]].
> - Gives product manifolds their point-set hygiene: [[§8 Differentiable Structures#^prop-8-19|§8.19]].

> [!remark] Remark
> Both statements extend to finite products by induction. For *infinite* products the story is subtler (product vs. box topology, 590 [[§10 Product Topology on Arbitrary Products#^def-10-2|§10]]), but finite products are all we need: they are how product manifolds like the torus $T^n = S^1 \times \cdots \times S^1$ will get their point-set hygiene for free, leaving only local Euclideanness to check.

^rem-3-6

## Quotient Spaces

> [!definition] Definition §3.4: Quotient Space and Quotient Topology
> Let $X$ be a topological space and $\sim$ an equivalence relation on $X$. Form the **quotient space**
>
> $$
> X/{\sim} \;=\; \{\, [x] \mid x \in X \,\}, \qquad [x] = \{y \in X \mid y \sim x\},
> $$
>
> the set of equivalence classes, with the natural surjection $\pi : X \to X/{\sim}$, $x \mapsto [x]$. The **quotient topology** on $X/{\sim}$ is defined by:
>
> $$
> W \subseteq X/{\sim} \text{ is open} \iff \pi^{-1}(W) \subseteq X \text{ is open in } X.
> $$
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^def-3-4

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^def-12-3|590 Def. §12.3 (Quotient Space)]], with the topology of [[§12 Quotient Topology#^prop-12-1|590 §12.1]].
> - Reused for orbit spaces [[§6 Group Actions and Orbit Spaces#^def-6-5|Def. §6.5]] and coset spaces [[§7 Homogeneous Spaces#^prop-7-6|§7.6]].

> [!theorem] Proposition §3.13: The Quotient Topology Is the Finest Making $\pi$ Continuous
> The projection $\pi : X \to X/{\sim}$ is continuous, and the quotient topology is the *finest* topology on $X/{\sim}$ with this property: every topology $\mathcal{T}'$ on $X/{\sim}$ for which $\pi$ is continuous is contained in it.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^prop-3-13

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $W$ is open in $X/{\sim}$ then $\pi^{-1}(W)$ is open in $X$ by definition, so $\pi$ is continuous. If $\pi$ is continuous for $\mathcal{T}'$, then every $W \in \mathcal{T}'$ has $\pi^{-1}(W)$ open in $X$, hence $W$ is open in the quotient topology.

^pf-3-13

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]]

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^rem-12-4|590 §12, The Quotient Topology is the Finest Making p Continuous]].

> [!remark] Remark: How to Read a Quotient
> A quotient space is easy to define and easy to lose track of. Whenever a quotient $X/{\sim}$ appears in these notes, four things are made explicit, and it is worth demanding them of every quotient you meet:
> 1. **What a point is.** A point of $X/{\sim}$ is an equivalence class $[x]$, i.e. a *subset* of $X$. Say which subset.
> 2. **What $\pi$ does.** $\pi(x) = [x]$: it sends a point of $X$ to the class containing it.
> 3. **What the open sets are.** $W \subseteq X/{\sim}$ is open iff $\pi^{-1}(W) = \bigcup_{[x] \in W} [x]$—the union in $X$ of all the classes belonging to $W$—is open in $X$. So the open sets of $X/{\sim}$ correspond exactly to the open subsets of $X$ that are *unions of classes* (the *saturated* open sets, [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#Open Maps and Open Relations|§3, Open Maps and Open Relations]]).
> 4. **What an identification does.** When $X/{\sim}$ is identified with a concrete space $Y$ via a bijection $\Phi$, say what $\Phi$ does to a class, and what its inverse does to a point of $Y$.
>
> For the line with two origins ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-1|Example §3.1]]): a point is a pair $\{(x,1), (x,2)\}$ for $x \neq 0$ or a singleton $\{(0,i)\}$; $\pi$ forgets the label except at $0$; a set is open iff its preimage, a union of such pairs and singletons, is open in the two lines; the identification with [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] sends $\{(x,1),(x,2)\} \mapsto x$ and $\{(0,i)\} \mapsto 0_i$.

^rem-3-7

> [!remark] Remark: Warning: Nothing Is Automatically Inherited
> **Neither $T_2$ nor second countability of $X$ is automatically inherited by $X/{\sim}$.** This is the reason the lecture spends most of its time here: the constructions that produce interesting manifolds are quotients, so we need theorems telling us *when* the quotient is $T_2$ (and second countable) — these properties must be earned, not assumed.

^rem-3-8

> [!example] Example §3.1: Failure of Hausdorffness — the Line with Two Origins as a Quotient
> Let
>
> $$
> X = (\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\})
> $$
>
> (two disjoint copies of the real line), and define $(x, 1) \sim (x, 2)$ for all $x \neq 0$ — these, together with the relations forced by reflexivity and symmetry, are the only identifications. In particular $(0,1) \not\sim (0,2)$: the two origins survive as distinct points. The quotient space is exactly the real line with two origins of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]], which is not $T_2$ — even though $X$ itself, a disjoint union of two lines, is a metrizable space with every good property one could ask for.
>
> *Lee: Problem 1-1*

^ex-3-1

> [!remark]- Connections
> - The same space: [[§1 Point-Set Topology Review#^ex-1-4|Ex. §1.4]], [[§1 Point-Set Topology Review#^rem-1-9|§1, The Line with Two Origins as a Quotient]], [[§2 Topological Manifolds#^ex-2-1|Ex. §2.1]]; via the Hausdorff criterion in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-7|Ex. §3.7]].
> - A quotient of the Hausdorff $\mathbb{R}$ that is not Hausdorff, in MATH 590: [[§12 Quotient Topology#^ex-12-5|590 Ex. §12.5]].

> [!theorem] Proposition §3.14: The Two Constructions Agree
> The bijection sending the class $\{(x,1),(x,2)\}$ to $x$ for $x \neq 0$ and the class $\{(0,i)\}$ to $0_i$ is a homeomorphism from $X/{\sim}$, with the quotient topology, onto the line with two origins of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]], with the topology generated by the neighborhood bases $(-\varepsilon,0) \cup \{0_i\} \cup (0,\varepsilon)$.

^prop-3-14

> [!proof]+ Exercise
> Set up the bijection as above and check that a subset downstairs is open for one topology iff it is open for the other; by [[§7 Homogeneous Spaces#^prop-7-6|Proposition §7.6]]-style reasoning it is enough to compare the two on the basic sets of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]], pulling each back along $\pi$. Assigned in lecture and left here.

^pf-3-14

> [!example] Example §3.2: Failure of Second Countability
> Let $X = \mathbb{R}/{\sim}$ with the quotient topology, where $x \sim y$ iff $x = y$ or both $x, y \in \mathbb{Z}$: all integers are collapsed to a single point $x_0$, and $X$ looks like $x_0$ with countably many loops attached. Then $\mathbb{R}$ is second countable but $X$ is not, because $X$ is not first countable at $x_0$.

^ex-3-2

![[m591-3-2.svg]]
*The diagonal construction in the proof below: each $A_j$ has some radius at every integer, and $W$ is chosen thinner than $A_j$ at the integer $j$, so the marked point $w_j \in A_j$ lies outside $W$.*

> [!proof]+ Proof (PSet 1, Problem 4)
> Write $\pi : \mathbb{R} \to X$, so $\pi^{-1}(x_0) = \mathbb{Z}$ and $\pi^{-1}(\pi(x)) = \{x\}$ for $x \notin \mathbb{Z}$. Two preliminary facts. (i) If $V \subseteq X$ is a neighborhood of $x_0$, then $\pi^{-1}(V)$ is open in $\mathbb{R}$ and contains $\mathbb{Z}$. (ii) If $U \subseteq \mathbb{R}$ is open with $\mathbb{Z} \subseteq U$, then $U$ is saturated—each class is either $\mathbb{Z} \subseteq U$ or a singleton $\{x\} \subseteq U$—so $\pi^{-1}(\pi(U)) = U$ and $\pi(U)$ is a neighborhood of $x_0$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Definition §3.7]] and [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-15|Lemma §3.15]](4)).
>
> Suppose $X$ were first countable at $x_0$, with $\{\widetilde U_j\}_{j \in \mathbb{N}}$ a countable basis of neighborhoods of $x_0$, and set $U_j = \pi^{-1}(\widetilde U_j)$, open with $\mathbb{Z} \subseteq U_j$ by (i). For each $j \in \mathbb{N}$ and $n \in \mathbb{Z}$, openness gives a radius $a_{j,n} \in (0, \tfrac14]$ with $(n - a_{j,n}, n + a_{j,n}) \subseteq U_j$; write $A_j = \bigcup_{n \in \mathbb{Z}} (n - a_{j,n}, n + a_{j,n}) \subseteq U_j$. (Radii are capped at $\tfrac14$ so that arms around distinct integers are disjoint: two of them reach out at most $\tfrac12 < 1$.)
>
> *The diagonal neighborhood.* Put
>
> $$
> b_n = \begin{cases} a_{n,n}/2, & n \in \mathbb{N}, \\ 1/8, & n \in \mathbb{Z} \setminus \mathbb{N}, \end{cases}
> \qquad W = \bigcup_{n \in \mathbb{Z}} (n - b_n,\, n + b_n).
> $$
>
> Then $W$ is open, $\mathbb{Z} \subseteq W$, and $b_n \le \tfrac18$ for all $n$.
>
> *No $U_j$ is contained in $W$.* Fix $j \in \mathbb{N}$ and set $w_j = j + \tfrac34 a_{j,j}$. Then $w_j \in A_j \subseteq U_j$, since $|w_j - j| = \tfrac34 a_{j,j} < a_{j,j}$. But $w_j \notin W$: it is not in the arm at $j$, because $j + b_j = j + \tfrac12 a_{j,j} < w_j$; and it is in no other arm, since $|w_j - j| \le \tfrac34 \cdot \tfrac14 < \tfrac14$ while a point of the arm at $m$ is within $b_m \le \tfrac18$ of $m$, so $w_j$ in that arm would force $|j - m| < \tfrac14 + \tfrac18 < 1$, impossible for distinct integers.
>
> *Conclusion.* By (ii), $\widetilde W = \pi(W)$ is a neighborhood of $x_0$. If $\widetilde U_j \subseteq \widetilde W$ for some $j$, taking preimages would give $U_j \subseteq \pi^{-1}(\widetilde W) = W$, contradicting the previous paragraph. So no member of the family sits inside $\widetilde W$, and $\{\widetilde U_j\}$ is not a basis of neighborhoods of $x_0$—a contradiction. Hence $X$ is not first countable at $x_0$, and by [[§1 Point-Set Topology Review#^prop-1-4|Proposition §1.4]] it is not second countable.

^pf-ex-3-2

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-15|§3.15]], [[§1 Point-Set Topology Review#^def-1-4|Def. §1.4]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§1 Point-Set Topology Review#^prop-1-4|§1.4]]

> [!remark]- Connections
> - First and second countability in MATH 590: [[§18 Countability Axioms#^def-18-2|590 Def. §18.2]], [[§18 Countability Axioms#^def-18-3|590 Def. §18.3]].
> - Cited in [[§1 Point-Set Topology Review#^prop-1-4|§1.4]] as the use of the contrapositive.

> [!remark] Remark: Why the Diagonal
> The mechanism is Cantor's: each candidate $U_j$ is pinned down at the single integer $j$, and $W$ is built to be strictly thinner than $U_j$ exactly there. No countable family can control all of the infinitely many arms at once, because a neighborhood of $x_0$ must specify a radius at *every* integer simultaneously—that is what collapsing infinitely many points to one costs. [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|Theorem §3.28]] is not contradicted, because its hypothesis fails: this relation is *not* open. The saturation of the open set $(-\tfrac12, \tfrac12)$, which meets $\mathbb{Z}$ at $0$, is $(-\tfrac12,\tfrac12) \cup \mathbb{Z}$, and that is not open—no neighborhood of the point $1$ is contained in it.

^rem-3-9

The single most useful fact about the quotient topology — that a map *out* of a quotient is continuous as soon as its composite with $\pi$ is, and that a map on $X$ constant on the classes descends to one on $X/{\sim}$ — is [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|Theorem §3.18]] below. It is stated in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#Quotient Maps|§3, Quotient Maps]] because its natural generality is quotient maps rather than quotient spaces.

## Open Maps and Open Relations

> [!definition] Definition §3.5: Open Map
> A continuous map $F : X \to Y$ between topological spaces is **open** if for every open $U \subseteq X$, the image $F(U)$ is open in $Y$.

^def-3-5

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^def-12-4|590 Def. §12.4]].

> [!example] Example §3.3: Projections Are Open
> $\pi_X : X \times Y \to X$ is always an open map.

^ex-3-3

> [!proof]+ Proof (not given in lecture — “go home and check yourself”)
> First, for a basis element: $\pi_X(U \times V) = U$ if $V \neq \emptyset$ (and $= \emptyset$ if $V = \emptyset$), open either way. A general open $A \subseteq X \times Y$ is a union of basis elements, $A = \bigcup_i U_i \times V_i$, and images commute with unions:
>
> $$
> \pi_X(A) = \bigcup_i \pi_X(U_i \times V_i),
> $$
>
> a union of open sets.

^pf-ex-3-3

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-5|Def. §3.5]]

> [!definition] Definition §3.6: Open Equivalence Relation
> An equivalence relation $\sim$ on $X$ is **open** if the projection $\pi : X \to X/{\sim}$ is an open map.

^def-3-6

> [!example] Example §3.4: Non-Example
> Let $X = \mathbb{R}$ and let $\sim$ be the equivalence relation generated by the single non-trivial identification $0 \sim 1$ (glue the two points; the quotient looks like a line with a small loop). Take the open set $\left(-\tfrac12, \tfrac12\right)$ and compute the preimage of its image:
>
> $$
> \pi^{-1}\!\left(\pi\!\left(-\tfrac12, \tfrac12\right)\right) = \left(-\tfrac12, \tfrac12\right) \cup \{1\},
> $$
>
> because the identified point $[0] = [1]$ has the *two* preimages $0$ and $1$. This set is not open in $\mathbb{R}$ (no neighborhood of $1$ fits inside), so $\pi\left(-\tfrac12,\tfrac12\right)$ is not open in the quotient, and $\sim$ is not an open relation. Uribe: “I love little examples like this.”

^ex-3-4

> [!definition] Definition §3.7: Saturation and Saturated Sets
> Let $\sim$ be an equivalence relation on a set $X$ with quotient map $\pi : X \to X/{\sim}$. For any subset $U \subseteq X$, the **saturation** of $U$ is
>
> $$
> \tilde U \;:=\; \pi^{-1}(\pi(U)) \;=\; \{\, y \in X \mid \exists\, x \in U \text{ such that } y \sim x \,\} \;=\; \bigcup_{x \in U} [x],
> $$
>
> the union of all equivalence classes that meet $U$. A subset $S \subseteq X$ is **saturated** if $S = \tilde S$; equivalently, $S$ is a union of equivalence classes; equivalently, $S = \pi^{-1}(W)$ for some $W \subseteq X/{\sim}$ (namely $W = \pi(S)$).

^def-3-7

![[m591-3-3.svg]]
*Saturation for the relation $x \sim y \iff x - y \in \mathbb{Z}$ on $\mathbb{R}$, whose quotient is the circle ([[§7 Homogeneous Spaces#^ex-7-4|Example §7.4]]). The saturation of the interval $U$ is the union of all its integer translates, $\pi^{-1}(\pi(U))$: everything the quotient map cannot tell apart from $U$. It is open because each translate is — the mechanism behind “orbit relations are open” ([[§6 Group Actions and Orbit Spaces#^lem-6-3|Lemma §6.3]]) — and its image $\pi(U)$ is an open arc of the circle.*

> [!remark]- Connections
> - Saturated sets for cosets: [[§7 Homogeneous Spaces#^prop-7-6|§7.6]]; for orbits: [[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]].

> [!theorem] Lemma §3.15: Basic Properties of Saturation
> For all $U, V \subseteq X$ and any family $(U_\alpha)$ of subsets:
> 1. $U \subseteq \tilde U$, and $\tilde{\tilde U} = \tilde U$ (the saturation is saturated).
> 2. $U \subseteq V \Rightarrow \tilde U \subseteq \tilde V$, and $\widetilde{\bigcup_\alpha U_\alpha} = \bigcup_\alpha \tilde U_\alpha$.
> 3. $\pi(\tilde U) = \pi(U)$.
> 4. The three descriptions of “saturated” in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Definition §3.7]] are equivalent, and for saturated $S$ one has $\pi^{-1}(\pi(S)) = S$.

^lem-3-15

> [!proof]+ Proof
> Write $\tilde U = \bigcup_{x \in U}[x]$. (1) $x \in [x]$ gives $U \subseteq \tilde U$. If $y \in \tilde{\tilde U}$ then $y \sim z$ for some $z \in \tilde U$, so $z \sim x$ for some $x \in U$, and transitivity gives $y \sim x$, i.e. $y \in \tilde U$; with $\tilde U \subseteq \tilde{\tilde U}$ from the first part, equality follows. (2) Both are immediate from $\tilde U = \bigcup_{x \in U}[x]$: enlarging $U$ enlarges the union, and the union over $\bigcup_\alpha U_\alpha$ is the union of the unions. (3) $\pi(\tilde U) \supseteq \pi(U)$ by (1); conversely $\pi(y)$ for $y \in [x]$, $x \in U$, equals $\pi(x) \in \pi(U)$. (4) If $S = \tilde S$ then $S$ is the union of the classes $[x]$, $x \in S$. If $S$ is a union of classes, $S = \bigcup_{[x] \in W}[x]$ for $W = \pi(S)$, then $\pi^{-1}(W) = \{y \mid [y] \in W\} = S$. If $S = \pi^{-1}(W)$ then $\tilde S = \pi^{-1}(\pi(\pi^{-1}(W))) = \pi^{-1}(W) = S$, using $\pi(\pi^{-1}(W)) = W$ (surjectivity of $\pi$).

^pf-3-15

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]]

> [!theorem] Proposition §3.16: The Saturation Correspondence
> Let $\pi : X \to X/{\sim}$ be the projection. Then $W \mapsto \pi^{-1}(W)$ is a bijection from the subsets of $X/{\sim}$ onto the saturated subsets of $X$, with inverse $S \mapsto \pi(S)$, and it preserves unions, intersections and complements. Under it, the open subsets of $X/{\sim}$ correspond exactly to the saturated open subsets of $X$, and the closed subsets to the saturated closed subsets.
>
> *Lee: Theorem A.27(c)*

^prop-3-16

> [!proof]+ Proof
> *(Lecture 2 defined the saturation and stated that a relation is open exactly when saturations of open sets are open; the proof is filled in.)* Every $\pi^{-1}(W)$ is saturated, and $\pi(\pi^{-1}(W)) = W$ because $\pi$ is surjective. Conversely, a saturated $S$ satisfies $\pi^{-1}(\pi(S)) = S$ by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-15|Lemma §3.15]](4). So the two maps are mutually inverse. Taking preimages commutes with unions, intersections and complements. The open sets of $X/{\sim}$ are by definition those $W$ with $\pi^{-1}(W)$ open, which gives the statement for open sets. For closed sets pass to complements, using that the complement of a saturated set is saturated (it is the union of the remaining classes).

^pf-3-16

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-15|§3.15]]

> [!theorem] Proposition §3.17: Openness via Saturations
> $\sim$ is open $\iff$ for every open $U \subseteq X$, the saturation $\tilde U = \pi^{-1}(\pi(U))$ is open in $X$.

^prop-3-17

> [!proof]+ Proof
> $\pi$ is open iff $\pi(U)$ is open in $X/{\sim}$ for every open $U \subseteq X$; and by the definition of the quotient topology, $\pi(U)$ is open in $X/{\sim}$ iff $\pi^{-1}(\pi(U)) = \tilde U$ is open in $X$.

^pf-3-17

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-6|Def. §3.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]]

> [!remark]- Connections
> - Applied to orbit relations: [[§6 Group Actions and Orbit Spaces#^lem-6-3|Orbit Relations Are Open, §6.3]]; to cosets: [[§7 Homogeneous Spaces#^prop-7-6|§7.6]].

In lecture, saturation was named after the proposition, as the set $\pi^{-1}(\pi(U))$ appearing in it; the notion is worth having on its own (it recurs for orbit spaces in [[§6 Group Actions and Orbit Spaces|§6]]), which is why it is defined first here, with its elementary properties.

> [!remark] Remark: In Words
> The saturation of $U$ is $U$ together with everything equivalent to something in $U$ — “you push forward and then take the preimage.” [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-17|Proposition §3.17]] then reads as a slogan: *$\sim$ is open iff the saturation of every open set is open.* In the [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-4|non-example above]], saturating $\left(-\tfrac12,\tfrac12\right)$ adjoined the isolated point $1$ and destroyed openness. In the [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|ℂPⁿ example below]], saturating an open set means rotating it in every possible way, which *preserves* openness — that contrast is the whole point of the definition.

^rem-3-10

## Quotient Maps

So far “quotient” has named a topology on a set of equivalence classes. The same notion can be phrased as a property of a map, which is often how it is recognized in practice.

> [!definition] Definition §3.8: Quotient Map
> A map $F : X \to Y$ between topological spaces is a **quotient map** if it is surjective and
>
> $$
> U \subseteq Y \text{ is open} \iff F^{-1}(U) \subseteq X \text{ is open}.
> $$
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^def-3-8

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^def-12-1|590 Def. §12.1]].

> [!example] Example §3.5: Projections onto Quotient Spaces Are Quotient Maps
> The projection $\pi : X \to X/{\sim}$ of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Definition §3.4]] is a quotient map in the sense of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Definition §3.8]]: it is surjective, and $W$ is open in $X/{\sim}$ if and only if $\pi^{-1}(W)$ is open in $X$, which is the definition of the quotient topology. The [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-21|next proposition]] says that these are the only examples.

^ex-3-5

> [!definition] Definition §3.9: Maps Constant on Fibres
> Let $p : X \to Y$ be a map. A map $g : X \to Z$ is **constant on the fibres of $p$** if it is constant on $p^{-1}(\{y\})$ for every $y \in Y$; equivalently, $p(x) = p(x')$ implies $g(x) = g(x')$.

^def-3-9

> [!theorem] Theorem §3.18: Universal Property of a Quotient Map
> Let $p : X \to Y$ be a quotient map ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Definition §3.8]]), let $Z$ be a topological space, and let $g : X \to Z$ be a map that is constant on the fibres of $p$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-9|Definition §3.9]]). Then there is a *unique* map $f : Y \to Z$ with
>
> $$
> f \circ p = g .
> $$
>
> Moreover:
> 1. $f$ is continuous $\iff$ $g$ is continuous;
> 2. $f$ is a quotient map $\iff$ $g$ is a quotient map.
>
> *Lee: Theorems A.27(a) and A.30*

^thm-3-18

![[m591-3-4.svg]]
*The universal property: $g$ is constant on the fibres of the quotient map $p$, so it factors as $g = f \circ p$ through the dashed induced map $f$.*

> [!proof]+ Proof
> *Existence and uniqueness of $f$.* Let $y \in Y$. Since $p$ is surjective the fibre $p^{-1}(\{y\})$ is nonempty; choose $x$ in it and set $f(y) := g(x)$. This does not depend on the choice, because $g$ is constant on that fibre. By construction $f(p(x)) = g(x)$ for every $x \in X$, i.e. $f \circ p = g$. If $f'$ also satisfies $f' \circ p = g$, then $f'(y) = f'(p(x)) = g(x) = f(y)$ for any $x$ in the fibre over $y$, so $f' = f$: surjectivity of $p$ makes $f$ unique.
>
> *(1).* ($\Rightarrow$) $g = f \circ p$ is a composite of continuous maps. ($\Leftarrow$) Let $V \subseteq Z$ be open. Then
>
> $$
> p^{-1}\big(f^{-1}(V)\big) = (f \circ p)^{-1}(V) = g^{-1}(V),
> $$
>
> which is open in $X$; since $p$ is a quotient map, $f^{-1}(V)$ is open in $Y$. Hence $f$ is continuous.
>
> *(2), $\Leftarrow$.* Suppose $g$ is a quotient map. Then $f$ is surjective, since $f(Y) = f(p(X)) = g(X) = Z$, and continuous by (1). Let $V \subseteq Z$ with $f^{-1}(V)$ open; then $g^{-1}(V) = p^{-1}(f^{-1}(V))$ is open by continuity of $p$, so $V$ is open because $g$ is a quotient map. Together with continuity this says: $V$ open $\iff$ $f^{-1}(V)$ open. So $f$ is a quotient map.
>
> *(2), $\Rightarrow$.* Suppose $f$ is a quotient map. Then $g = f \circ p$ is surjective, and for $V \subseteq Z$,
>
> $$
> V \text{ open} \iff f^{-1}(V) \text{ open in } Y \iff p^{-1}\big(f^{-1}(V)\big) \text{ open in } X \iff g^{-1}(V) \text{ open in } X,
> $$
>
> the first equivalence because $f$ is a quotient map and the second because $p$ is. So $g$ is a quotient map. (In particular: *a composite of quotient maps is a quotient map*.)

^pf-3-18

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Def. §3.8]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-9|Def. §3.9]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]]

> [!remark]- Connections
> - Home in MATH 590: [[Universal Property of Quotient Maps|590 §12.3 (Universal Property of Quotient Maps)]]; composites of quotient maps are [[§12 Quotient Topology#^ex-12-4|590 Ex. §12.4]].
> - Linear counterpart: [[§10 Vector Spaces and Matrix Groups#^prop-10-6|Quotient Spaces and Their Universal Property, §10.6]].

> [!theorem] Corollary §3.19: The Form Used in Practice
> Let $\sim$ be an equivalence relation on $X$ with projection $\pi : X \to X/{\sim}$.
> 1. If $g : X \to Z$ is constant on equivalence classes, there is a unique $\overline{g} : X/{\sim} \to Z$ with $\overline{g} \circ \pi = g$, and $\overline{g}$ is continuous if and only if $g$ is.
> 2. For any function $h : X/{\sim} \to Z$: $h$ is continuous $\iff$ $h \circ \pi$ is continuous.
>
> *Lee: Theorem A.30*

^cor-3-19

> [!proof]+ Proof
> $\pi$ is a quotient map by the definition of the quotient topology, and its fibres are the equivalence classes, so (1) is [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|Theorem §3.18]] verbatim. For (2), apply the theorem to $g = h \circ \pi$, which is constant on each class because $\pi$ is; the unique $f$ with $f \circ \pi = g$ is $h$ itself, and (1) of the theorem gives the equivalence.

^pf-3-19

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-5|Ex. §3.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]]

> [!theorem] Corollary §3.20: The Universal Property Characterizes the Quotient Topology
> Let $X$ be a topological space, $Y$ a set, and $p : X \to Y$ a surjection. The quotient topology is the *unique* topology $\mathcal{T}$ on $Y$ with the property that for every topological space $Z$ and every function $f : Y \to Z$,
>
> $$
> f \text{ is continuous} \iff f \circ p \text{ is continuous.}
> $$
>
> *Lee: Theorem A.27(b)*

^cor-3-20

> [!proof]+ Proof
> The quotient topology has the property: with the quotient topology, $p$ is a quotient map by [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Definition §3.8]], so [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|Theorem §3.18]](1) applies to $g = f \circ p$, which is constant on the fibres of $p$. Suppose $\mathcal{T}$ and $\mathcal{T}'$ both have it. Taking $Z = (Y,\mathcal{T})$ and $f = \mathrm{id}$, which is continuous, the property of $\mathcal{T}$ gives that $p : X \to (Y,\mathcal{T})$ is continuous; likewise $p : X \to (Y,\mathcal{T}')$ is continuous. Now take $Z = (Y,\mathcal{T}')$ and $f = \mathrm{id} : (Y,\mathcal{T}) \to (Y,\mathcal{T}')$. Then $f \circ p = p : X \to (Y,\mathcal{T}')$ is continuous, so by the property of $\mathcal{T}$ the map $f$ is continuous, i.e. $\mathcal{T}' \subseteq \mathcal{T}$. Exchanging the roles gives $\mathcal{T} \subseteq \mathcal{T}'$.

^pf-3-20

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Def. §3.8]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]]

> [!remark]- Connections
> - Uniqueness of the quotient topology in MATH 590: [[§12 Quotient Topology#^prop-12-1|590 §12.1]].

> [!remark] Remark: How This Gets Used
> This is 590 [[§12 Quotient Topology#^thm-12-3|§12]] material (Munkres Theorem 22.2, Lee Theorem A.27), stated there in the full form above; it was not repeated in lecture but is used constantly here. The recipe it encodes is: *to define a continuous map out of a quotient, never define it on the quotient.* Define it upstairs on $X$, check it is constant on the classes, check continuity upstairs — and the theorem delivers a unique continuous map downstairs. Every identification in these notes is made this way:
> - $\rho : \mathbb{R}^3/\mathrm{SO}(3) \to [0,\infty)$, $[x] \mapsto |x|$, from the norm on $\mathbb{R}^3$ ([[§6 Group Actions and Orbit Spaces#^ex-6-5|Example §6.5]]);
> - $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$, from the orbit map on $G$ ([[§7 Homogeneous Spaces#^thm-7-8|Theorem §7.8]]);
> - $\overline{F} : X/{\sim} \to Y$ recognizing a quotient map ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-21|Proposition §3.21]]);
> - continuity of the charts on $\mathbb{CP}^n$ and $\mathbb{RP}^n$ ([[§8 Differentiable Structures#Projective Spaces as Smooth Manifolds|§8, Projective Spaces as Smooth Manifolds]]), applied locally via [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|Lemma §3.24]].
>
> Part (2) of [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|Theorem §3.18]] is what makes the recipe self-improving: if the map upstairs is itself a quotient map, the induced map downstairs is not merely continuous but a homeomorphism when injective, since a bijective quotient map is a homeomorphism.

^rem-3-11

> [!theorem] Proposition §3.21: A Quotient Map Presents Its Target as a Quotient
> Let $F : X \to Y$ be a quotient map and let $\sim$ be the relation on $X$ defined by $a \sim b \iff F(a) = F(b)$ (an equivalence relation, the fibres of $F$ being its classes). Then
>
> $$
> \overline{F} : X/{\sim} \longrightarrow Y, \qquad \overline{F}([a]) = F(a)
> $$
>
> is a homeomorphism, and $F = \overline{F} \circ \pi$.
>
> *Lee: Theorem A.31*

^prop-3-21

> [!proof]+ Proof
> *Well defined and bijective.* $\overline{F}$ is well defined because $a \sim b$ means $F(a) = F(b)$, and injective because $F(a) = F(b)$ means $a \sim b$, i.e. $[a] = [b]$; it is surjective because $F$ is. The factorization $F = \overline{F} \circ \pi$ holds by construction.
>
> *Continuity of $\overline{F}$.* $\overline{F} \circ \pi = F$ is continuous, so $\overline{F}$ is continuous by the universal property of the quotient (Proposition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]).
>
> *Continuity of $\overline{F}^{-1}$.* Let $W \subseteq X/{\sim}$ be open; we show $\overline{F}(W)$ is open in $Y$, which is exactly continuity of $\overline{F}^{-1}$. Since $F$ is a quotient map it suffices to show $F^{-1}(\overline{F}(W))$ is open in $X$. But
>
> $$
> F^{-1}\big(\overline{F}(W)\big) = \pi^{-1}\big(\overline{F}^{-1}(\overline{F}(W))\big) = \pi^{-1}(W),
> $$
>
> using $F = \overline{F} \circ \pi$ for the first equality and injectivity of $\overline{F}$ for the second; and $\pi^{-1}(W)$ is open because $W$ is.

^pf-3-21

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Def. §3.8]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^cor-12-4|590 §12.4 (Induced Bijection from Quotient)]].

> [!remark] Remark
> So “quotient map” and “presentation of the target as a quotient space” are the same notion, and one may use whichever is convenient: to recognize a quotient topology, exhibit a quotient map onto it. Stated without proof in PSet 1, Problem 5.

^rem-3-12

> [!theorem] Proposition §3.22: Open Surjections Are Quotient Maps
> A continuous open surjection $F : X \to Y$ is a quotient map.

^prop-3-22

> [!proof]+ Proof
> *(Not from lecture; filled in.)* ($\Rightarrow$) Continuity. ($\Leftarrow$) Suppose $F^{-1}(U)$ is open. Then $F(F^{-1}(U))$ is open, $F$ being an open map; and $F(F^{-1}(U)) = U$ because $F$ is surjective.

^pf-3-22

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-5|Def. §3.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Def. §3.8]]

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^prop-12-2|590 §12.2]] (open or closed continuous surjections).
> - Applied to $G \to G/H$: [[§7 Homogeneous Spaces#^cor-7-7|§7.7]].

> [!example] Example §3.6: Projections Are Quotient Maps
> If $X_1, \ldots, X_n$ are nonempty topological spaces, every projection $\pi_i : X_1 \times \cdots \times X_n \to X_i$ is a quotient map: it is surjective (choose any point in each other factor), continuous, and open ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-3|Example §3.3]] and induction), so [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-22|Proposition §3.22]] applies. Nonemptiness is needed: if some $X_k = \emptyset$ the product is empty and $\pi_i$ is not surjective onto a nonempty $X_i$.

^ex-3-6

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-3|Ex. §3.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-22|§3.22]]

> [!remark] Remark
> This is PSet 1, Problem 5, where it is proved directly from the definition. The direct argument is worth seeing once: writing an open $\pi_i^{-1}(U)$ as a union of boxes $\bigcup_x U_{x,1} \times \cdots \times U_{x,n}$ and projecting gives $U = \bigcup_x U_{x,i}$, a union of open sets—and the step $\pi_i(U_{x,1} \times \cdots \times U_{x,n}) = U_{x,i}$ is exactly where nonemptiness of the other factors enters.

^rem-3-13

> [!theorem] Lemma §3.23: Open Surjections Push Bases Forward
> Let $\pi : Y \to Q$ be a continuous open surjection and $\mathcal{B}$ a basis for the topology of $Y$. Then $\pi(\mathcal{B}) = \{\pi(B) \mid B \in \mathcal{B}\}$ is a basis for the topology of $Q$. In particular, if $Y$ is second countable, so is $Q$.

^lem-3-23

> [!proof]+ Proof
> Each $\pi(B)$ is open, $\pi$ being an open map. Let $W \subseteq Q$ be open and $q \in W$. By surjectivity choose $y \in Y$ with $\pi(y) = q$. By continuity $\pi^{-1}(W)$ is open, and it contains $y$, so there is $B \in \mathcal{B}$ with $y \in B \subseteq \pi^{-1}(W)$. Applying $\pi$ and using $\pi(\pi^{-1}(W)) \subseteq W$,
>
> $$
> q = \pi(y) \in \pi(B) \subseteq W .
> $$
>
> By [[§1 Point-Set Topology Review#^def-1-1|Definition §1.1]], $\pi(\mathcal{B})$ is a basis. It is the image of $\mathcal{B}$ under $B \mapsto \pi(B)$, hence countable when $\mathcal{B}$ is.

^pf-3-23

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-5|Def. §3.5]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]]

> [!theorem] Lemma §3.24: Restricting a Quotient Map over an Open Set
> Let $p : X \to Y$ be a quotient map and $V \subseteq Y$ an open set, and put $W = p^{-1}(V)$. Then the restriction
>
> $$
> q := p|_W : W \longrightarrow V
> $$
>
> is a quotient map, where $W$ and $V$ carry the subspace topologies.
>
> *Lee: Theorem A.27(e)*

^lem-3-24

![[m591-3-5.svg]]
*The square commutes, and the horizontal arrows are inclusions of open sets. The lemma says the left arrow inherits the quotient property of the right one. Restricting a quotient map to an arbitrary subspace can destroy that property; restricting it over an open set cannot.*

> [!proof]+ Proof
> $q$ is surjective because $p$ is, and continuous as a restriction of a continuous map. Let $A \subseteq V$ be such that $q^{-1}(A)$ is open in $W$; we show $A$ is open in $V$. Since $A \subseteq V$,
>
> $$
> q^{-1}(A) = p^{-1}(A) \cap W = p^{-1}(A),
> $$
>
> as $p^{-1}(A) \subseteq p^{-1}(V) = W$. The set $W = p^{-1}(V)$ is open in $X$, $V$ being open and $p$ continuous; so a subset open in $W$ is open in $X$ ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-2|Lemma §3.2]]), and $p^{-1}(A)$ is open in $X$. As $p$ is a quotient map, $A$ is open in $Y$, hence in $V$. The reverse implication is continuity of $q$.

^pf-3-24

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Def. §3.8]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-1|Def. §3.1]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-2|§3.2]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]]

> [!remark]- Connections
> - Used for the charts on $\mathbb{CP}^n$: [[§8 Differentiable Structures#^prop-8-6|Each φᵢ Is a Chart, §8.6]].

> [!theorem] Lemma §3.25: Restricting a Quotient Map over a Closed Set
> [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|Lemma §3.24]] holds with “open” replaced by “closed”: if $p : X \to Y$ is a quotient map, $V \subseteq Y$ is closed and $W = p^{-1}(V)$, then $p|_W : W \to V$ is a quotient map.
>
> *Lee: Theorem A.27(e)*

^lem-3-25

> [!proof]+ Proof
> By taking complements, a continuous surjection is a quotient map exactly when a set is closed iff its preimage is closed. Let $C \subseteq V$ with $q^{-1}(C) = p^{-1}(C)$ closed in $W$. Now $W$ is closed in $X$, as $V$ is closed and $p$ continuous, and a set closed in a closed subspace is closed in the whole space: it is the intersection of $W$ with a closed subset of $X$. So $p^{-1}(C)$ is closed in $X$, hence $C$ is closed in $Y$ because $p$ is a quotient map, and therefore closed in $V$.

^pf-3-25

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|Def. §3.8]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-24|§3.24]], [[§6 Closed Sets and Limit Points#^thm-6-2|590 §6.2]], [[§6 Closed Sets and Limit Points#^thm-6-3|590 §6.3]]

> [!remark] Remark
> Both hypotheses are used, at different steps: that $W$ is a full preimage gives $q^{-1}(A) = p^{-1}(A)$, and that $V$ is open makes a set open in $W$ open in $X$. Without them the restriction of a quotient map need not be a quotient map. The lemma is what allows the universal property ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|Theorem §3.18]]) to be applied *locally*, on an open piece of a quotient — which is exactly the situation of a chart on a quotient space ([[§8 Differentiable Structures#Projective Spaces as Smooth Manifolds|§8, Projective Spaces as Smooth Manifolds]]). Both lemmas are from Assignment 2, Problem 2.

^rem-3-14

## The Hausdorff Criterion for Open Quotients

> [!definition] Definition §3.10: Graph of a Relation
> The **graph** of a relation $\sim$ on a set $X$ is
>
> $$
> \Gamma = \{\, (x, y) \in X \times X \mid x \sim y \,\} \subseteq X \times X .
> $$

^def-3-10

> [!theorem] Theorem §3.26: Hausdorff Criterion
> Assume $\sim$ is an *open* equivalence relation on a topological space $X$, and let $\Gamma \subseteq X \times X$ be its graph ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Definition §3.10]]). Then:
>
> $$
> X/{\sim} \text{ is } T_2 \iff \Gamma \text{ is closed in } X \times X.
> $$
>
> *Lee: no counterpart; a course result (see the comparison below Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|§3.28]])*

^thm-3-26

> [!remark] Remark: No Hausdorff Hypothesis on $X$
> Mid-statement, Uribe began to add the hypothesis “assume $X$ is Hausdorff”—then stopped: “actually, I don't need that.” The final statement is correct as it stands: no separation assumption on $X$ is required, only openness of the relation. (Openness, moreover, is used only in the direction $\Leftarrow$; the direction $\Rightarrow$ holds for arbitrary equivalence relations, as the [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^pf-3-26|proof]] shows.)

^rem-3-15

> [!theorem] Corollary §3.27: The Diagonal Criterion
> A topological space $X$ is Hausdorff if and only if the diagonal $\Delta = \{(x,x) \mid x \in X\}$ is closed in $X \times X$.

^cor-3-27

> [!proof]+ Proof
> Apply [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|Theorem §3.26]] to the trivial relation, $x \sim y \iff x = y$. It is open, since every set is its own saturation. Its graph is $\Gamma = \Delta$. And $\pi : X \to X/{\sim}$ is a continuous open bijection, hence a homeomorphism, so $X/{\sim}$ is Hausdorff iff $X$ is. This classical characterization is the special case of the theorem with nothing identified; the theorem is its generalization to quotients.

^pf-3-27

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|§3.26]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-17|§3.17]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Def. §3.10]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

> [!proof]+ Proof (given in full in lecture)
> ($\Leftarrow$) Assume $\Gamma$ is closed. Let $[x] \neq [y]$ in $X/{\sim}$, i.e. $x \not\sim y$, i.e. $(x, y) \notin \Gamma$. Since $\Gamma$ is closed, its complement is an open set containing $(x,y)$, so by the box characterization ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-8|Proposition §3.8]]) there exist neighborhoods $U$ of $x$ and $V$ of $y$ such that
>
> $$
> (U \times V) \cap \Gamma = \emptyset.
> $$
>
> Now push forward: $\pi(U)$ and $\pi(V)$ are open in $X/{\sim}$ *because the relation is open*, and $[x] \in \pi(U)$, $[y] \in \pi(V)$.
>
> **Claim:** $\pi(U) \cap \pi(V) = \emptyset$. If not, there exist $a \in U$, $b \in V$ with $\pi(a) = \pi(b)$. But $\pi(a) = \pi(b)$ means exactly $a \sim b$, i.e. $(a, b) \in \Gamma$; and $(a,b) \in U \times V$, so $(U \times V) \cap \Gamma \neq \emptyset$ — contradiction.
>
> Thus $\pi(U), \pi(V)$ separate $[x]$ and $[y]$, and $X/{\sim}$ is $T_2$.
>
> ($\Rightarrow$) Assume $X/{\sim}$ is $T_2$; we show the complement of $\Gamma$ is open. Take $(x, y) \in (X \times X) \setminus \Gamma$, i.e. $x \not\sim y$, i.e. $\pi(x) \neq \pi(y)$. By assumption there exist neighborhoods $A$ of $\pi(x)$ and $B$ of $\pi(y)$ in $X/{\sim}$ with $A \cap B = \emptyset$. Careful: $A$ and $B$ live in the *quotient*, not in $X$ — so pull back. Since $\pi$ is continuous, $\pi^{-1}(A) \times \pi^{-1}(B)$ is an open neighborhood of $(x, y)$ in $X \times X$.
>
> **Claim:** $\left(\pi^{-1}(A) \times \pi^{-1}(B)\right) \cap \Gamma = \emptyset$. Suppose by contradiction there is $(a, b) \in \Gamma$ with $a \in \pi^{-1}(A)$ and $b \in \pi^{-1}(B)$. Then $\pi(a) \in A$ and $\pi(b) \in B$; but $(a,b) \in \Gamma$ means $a \sim b$, so $\pi(a) = \pi(b)$. This common point lies in $A \cap B$, so $A \cap B \neq \emptyset$ — contradiction.
>
> Hence every point of the complement of $\Gamma$ has a neighborhood inside the complement, so $\Gamma$ is closed. (Note openness of $\sim$ was not used in this direction.)

^pf-3-26

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Def. §3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-6|Def. §3.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-8|§3.8]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-3|Def. §3.3]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]]

![[m591-3-6.svg]]
*The direction ($\Leftarrow$): a point $(x,y)$ off the closed graph $\Gamma$ has a box $U \times V$ missing $\Gamma$, and then $\pi(U)$ and $\pi(V)$ separate $[x]$ from $[y]$.*

> [!remark]- Connections
> - Applied to orbit spaces: [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]], [[§6 Group Actions and Orbit Spaces#^thm-6-5|§6.5]]; the failure mode is [[§6 Group Actions and Orbit Spaces#^ex-6-6|Ex. §6.6]].
> - Hausdorff spaces in MATH 590: [[§8 Hausdorff Spaces#^def-8-1|590 Def. §8.1]]; for the special case of a quotient onto a Hausdorff space, compare [[§12 Quotient Topology#^cor-12-4|590 §12.4]](2).

> [!remark] Remark: This Is the Tool
> Uribe (emphasized): “this is going to be our tool for figuring out whether a quotient space is $T_2$.” The workflow it suggests, and which the [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-29|ℂPⁿ example below]] executes: (i) show the relation is open — usually via the saturation slogan; (ii) show the graph is closed — often by exhibiting $\Gamma$ as a preimage of a closed set, or as a compact set inside a Hausdorff space.

^rem-3-16

> [!theorem] Theorem §3.28: Second Countability of Open Quotients
> If $\sim$ is an open equivalence relation and $X$ is second countable, then $X/{\sim}$ is second countable.
>
> *Lee: no counterpart; a course result*

^thm-3-28

> [!proof]+ Proof (one line in lecture — “project the countable basis”)
> $\pi : X \to X/{\sim}$ is a continuous surjection, and open because $\sim$ is; so [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-23|Lemma §3.23]] applies and the image of a countable basis of $X$ is a countable basis of $X/{\sim}$.

^pf-3-28

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-6|Def. §3.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-23|§3.23]]

> [!remark]- Connections
> - Reused for coset spaces: [[§7 Homogeneous Spaces|§7]].

**Comparison with Lee.** Lee's Appendix A has no counterpart to Theorems [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|§3.26]] and [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|§3.28]]: in his book the Hausdorff property and second countability of $\mathbb{RP}^n$ and $\mathbb{CP}^n$ are checked example by example (Example 1.5, Problem 1-9). The course proves one criterion for all open quotients at once and then reuses it for orbit spaces ([[§6 Group Actions and Orbit Spaces|§6]]) and coset spaces ([[§7 Homogeneous Spaces|§7]]) — which is what makes the quotient thread a thread.

> [!example] Example §3.7: The Line with Two Origins — via the Criterion
> Let $X = (\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\}) \subseteq \mathbb{R}^2$ with the subspace topology (two disjoint copies of $\mathbb{R}$), and $(x,1) \sim (x,2)$ for $x \neq 0$, as in [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-1|Example §3.1]]. The graph
>
> $$
> \Gamma = \{(a,b) \in X \times X \mid a = b\} \cup \{\, ((x,i),(x,j)) \mid x \neq 0,\ i \neq j \,\}
> $$
>
> is *not* closed in $X \times X$: the points $\big((\tfrac1n, 1), (\tfrac1n, 2)\big)$ lie in $\Gamma$ for every $n$, and converge in $X \times X$ to $\big((0,1),(0,2)\big)$, which is not in $\Gamma$ (the two origins are distinct and are not identified, the identification being imposed only for $x \neq 0$). A closed set contains the limits of its convergent sequences, so $\Gamma$ is not closed.
>
> The relation is open: the saturation of an open $U \subseteq X$ is $U \cup \sigma(U \setminus (\{0\} \times \{1,2\}))$, where $\sigma(x,i) = (x, 3-i)$ swaps the two copies—a homeomorphism of $X$—so the saturation is a union of two open sets. [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|Theorem §3.26]] therefore applies and gives: $X/{\sim}$ is *not* Hausdorff. This recovers [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] from the criterion rather than by separating the origins by hand.

^ex-3-7

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-1|Ex. §3.1]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Def. §3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-17|§3.17]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|§3.26]], [[§11 Metric Topology#^lem-11-8|590 §11.8]]

> [!remark]- Connections
> - “A closed set contains the limits of its convergent sequences” is the [[§11 Metric Topology#^lem-11-8|Sequence Lemma, 590 §11.8]].

PSet 1, Problem 2 asks for the non-closedness of $\Gamma$ directly. The sequence argument above needs no metrizability: in any topological space, if $z_n \to z$ with all $z_n$ in a closed set $C$, then $z \in C$ (otherwise the open set $X \setminus C$ would eventually contain the $z_n$).

## Application: Complex Projective Space

The following was set up in the last four minutes of lecture; the proof of the claim was given verbally, chalk down. **Uribe: “I'll write this again next time”** — so expect a [[§6 Group Actions and Orbit Spaces#^cor-6-4|careful reprise]]; the details below reconstruct the verbal argument.

> [!definition] Definition §3.11: Complex Projective Space $\mathbb{CP}^n$
> Consider the sphere $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$, and identify $\mathbb{R}^{2n+2} \cong \mathbb{C}^{n+1}$ by
>
> $$
> (x, y) \longmapsto x + iy, \qquad x, y \in \mathbb{R}^{n+1}
> $$
>
> (any such identification works). So points of $S^{2n+1}$ are complex vectors $z = (z_1, \dots, z_{n+1}) \in \mathbb{C}^{n+1}$ with $|z| = 1$. Let $S^1 = \{\xi \in \mathbb{C} \mid |\xi| = 1\}$ be the unit circle, and define a relation $\sim$ on $S^{2n+1}$ by
>
> $$
> z \sim w \iff \exists\, \xi \in S^1 \text{ such that } w = \xi z
> $$
>
> (componentwise complex multiplication: all entries of $w$ are obtained by rotating the entries of $z$ through the *same* angle). This is an equivalence relation ($\xi = 1$ gives reflexivity; $\xi^{-1} \in S^1$ gives symmetry; products give transitivity). The quotient
>
> $$
> \mathbb{CP}^n \;:=\; S^{2n+1}/{\sim}
> $$
>
> is the **complex projective space** of complex dimension $n$. Explicitly: a point of $\mathbb{CP}^n$ is a class $[z] = \{\, \xi z \mid \xi \in S^1 \,\}$, a circle inside $S^{2n+1}$; $\pi(z) = [z]$; and $W \subseteq \mathbb{CP}^n$ is open iff the union of the circles belonging to $W$ is open in $S^{2n+1}$. The class $[z]$ is the same as the complex line $\mathbb{C} z \subseteq \mathbb{C}^{n+1}$ through $z$ (a line meets the unit sphere in exactly the circle $\{\xi z\}$), so $\mathbb{CP}^n$ is the space of complex lines through the origin in $\mathbb{C}^{n+1}$; the identification is $[z] \mapsto \mathbb{C} z$, with inverse $\ell \mapsto \ell \cap S^{2n+1}$.
>
> *Lee: Problem 1-9*

^def-3-11

> [!remark]- Connections
> - As an orbit space of $\mathrm{U}(1) = S^1$: [[§6 Group Actions and Orbit Spaces#^ex-6-3|Ex. §6.3]] (cf. group actions and orbits, [[§23 Actions#^def-23-1|493 Def. §23.1]], [[§25 Orbits#^def-25-1|493 Def. §25.1]]); charts and smooth structure in [[§8 Differentiable Structures#^def-8-11|§8.11]], [[§8 Differentiable Structures#^thm-8-7|§8.7]]; the projection is a submersion, [[§14 Local Diffeomorphisms and Submersions#^ex-14-5|Ex. §14.5]].
> - Real analogue in MATH 590: [[§28 Fundamental Group of Some Surfaces#^def-28-2|590 Def. §28.2 (Projective n-Space)]], [[Projective plane]].

> [!theorem] Proposition §3.29: $\mathbb{CP}^n$ is Hausdorff and Second Countable
> The quotient topology on $\mathbb{CP}^n$ is $T_2$ and second countable.
>
> *Lee: Problem 1-9*

^prop-3-29

> [!proof]+ Proof (verbal sketch in Lecture 2; the general form is Corollary [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]])
> *(Lecture 4: the graph of the orbit relation is the continuous image of the compact $G \times X$, hence compact, hence closed in the Hausdorff $X \times X$.)* We verify the two hypotheses of the [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|Hausdorff Criterion]].
>
> *The relation is open.* For $\xi \in S^1$ define $R_\xi : S^{2n+1} \to S^{2n+1}$, $R_\xi(z) = \xi z$. This is well defined: $|\xi z| = |\xi|\,|z| = |z| = 1$. It is continuous, being the restriction to $S^{2n+1}$ of the $\mathbb{C}$-linear (hence $\mathbb{R}$-linear, hence continuous) map $z \mapsto \xi z$ on $\mathbb{C}^{n+1} \cong \mathbb{R}^{2n+2}$. Since $\xi^{-1} \in S^1$ and $R_{\xi^{-1}} \circ R_\xi = R_\xi \circ R_{\xi^{-1}} = \mathrm{id}$, $R_\xi$ is a homeomorphism; in particular $R_\xi(U)$ is open for every open $U \subseteq S^{2n+1}$. Now let $U \subseteq S^{2n+1}$ be open. For $w \in S^{2n+1}$,
>
> $$\begin{aligned}
> w \in \pi^{-1}(\pi(U)) &\iff \exists\, z \in U \text{ with } w \sim z \\
> &\iff \exists\, z \in U,\ \xi \in S^1 \text{ with } w = \xi z \iff w \in \bigcup_{\xi \in S^1} R_\xi(U),
> \end{aligned}$$
>
> so the saturation $\pi^{-1}(\pi(U)) = \bigcup_{\xi \in S^1} R_\xi(U)$ is a union of open sets, hence open. By [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-17|Proposition §3.17]], $\sim$ is open.
>
> *The graph is closed.* Define
>
> $$
> \Phi : S^1 \times S^{2n+1} \longrightarrow S^{2n+1} \times S^{2n+1}, \qquad \Phi(\xi, z) = (z, \xi z).
> $$
>
> By [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|Theorem §3.10]], $\Phi$ is continuous because its two components are: $(\xi, z) \mapsto z$ is the projection, and $(\xi, z) \mapsto \xi z$ is the restriction of the map $\mathbb{C} \times \mathbb{C}^{n+1} \to \mathbb{C}^{n+1}$, $(\xi, z) \mapsto \xi z$, whose real and imaginary parts are polynomial in the real coordinates. Its image is $\Gamma$: for $(z, w) \in S^{2n+1} \times S^{2n+1}$,
>
> $$\begin{aligned}
> (z, w) \in \Phi\big(S^1 \times S^{2n+1}\big) &\iff \exists\, \xi \in S^1 \text{ with } (z, w) = (z, \xi z) \\
> &\iff \exists\, \xi \in S^1 \text{ with } w = \xi z \iff z \sim w \iff (z,w) \in \Gamma.
> \end{aligned}$$
>
> $S^1 \subseteq \mathbb{R}^2$ and $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$ are closed and bounded, hence compact, and a finite product of compact spaces is compact ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]); so $S^1 \times S^{2n+1}$ is compact and its continuous image $\Gamma$ is compact. The space $S^{2n+1} \times S^{2n+1}$ is a subspace of $\mathbb{R}^{4n+4}$, hence metrizable, hence Hausdorff ([[§1 Point-Set Topology Review#^prop-1-6|Proposition §1.6]]), and a compact subset of a Hausdorff space is closed ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]]). Therefore $\Gamma$ is closed in $S^{2n+1} \times S^{2n+1}$.
>
> By the Hausdorff Criterion, $\mathbb{CP}^n$ is $T_2$; and since $S^{2n+1}$ is second countable (subspace of $\mathbb{R}^{2n+2}$) and $\sim$ is open, [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|Theorem §3.28]] gives second countability.

^pf-3-29

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11|Def. §3.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-17|§3.17]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-10|Def. §3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-26|§3.26]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-5|§3.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|§3.28]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§1 Point-Set Topology Review#^ex-1-1|Ex. §1.1]], [[Heine–Borel Theorem]], [[§15 Compact Spaces#^thm-15-8|590 §15.8]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§11 Metric Topology#^thm-11-4|590 §11.4]]

> [!remark]- Connections
> - The general form for compact groups acting on compact Hausdorff spaces: [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]], of which this is a special case ([[§6 Group Actions and Orbit Spaces#^rem-6-9|§6, Remark]]).

**Transcription note.** Page 7 of the handwritten notes writes the map in this argument as $S^1 \times S^{2n+1} \to S^{2n+2} \times S^{2n+2}$; the target is $S^{2n+1} \times S^{2n+1}$, where the graph of the relation lives.

**Transcription note.** On the board (and in the handwritten notes) the target of $\Phi$ was written with superscripts $2n+2$; the target must be $S^{2n+1} \times S^{2n+1}$ — pairs of points of the sphere being quotiented — as recorded here.

> [!proof]+ A direct proof that $\mathbb{CP}^n$ is Hausdorff (Assignment 2)
> This bypasses the Hausdorff criterion and exhibits the separating sets. Let $u \neq v$ in $S^{2n+1}/S^1$, with representatives $\vec u, \vec v \in S^{2n+1}$. Their orbits $S^1 \vec u$ and $S^1 \vec v$ are disjoint (distinct orbits), and compact, being images of the compact $S^1$ under $\mu \mapsto \mu\vec u$, $\mu \mapsto \mu \vec v$.
>
> *The orbits are at positive distance.* Let $d = \inf\{|\vec a - \vec b| : \vec a \in S^1\vec u,\ \vec b \in S^1 \vec v\}$. If $d = 0$, choose $\vec a_k \in S^1\vec u$, $\vec b_k \in S^1\vec v$ with $|\vec a_k - \vec b_k| \to 0$; by compactness a subsequence $\vec a_{k_j} \to \vec a \in S^1\vec u$, whence $\vec b_{k_j} \to \vec a$ too, and $\vec a \in S^1 \vec v$ since that orbit is closed. This contradicts disjointness, so $d > 0$.
>
> *Thickened orbits.* Put $r = d/3$ and $A = \bigcup_{\lambda \in S^1} \lambda\, B(\vec u, r)$, $B = \bigcup_{\lambda \in S^1} \lambda\, B(\vec v, r)$, with balls taken in $S^{2n+1}$. Each is open (a union of images of an open set under the homeomorphisms $\vec z \mapsto \lambda\vec z$) and saturated (a union of orbits). If $\lambda\vec z_1 = \lambda'\vec z_2$ with $\vec z_1 \in B(\vec u, r)$, $\vec z_2 \in B(\vec v, r)$, then
>
> $$
> d \le |\lambda\vec u - \lambda'\vec v| \le |\lambda\vec u - \lambda \vec z_1| + |\lambda\vec z_1 - \lambda'\vec z_2| + |\lambda'\vec z_2 - \lambda'\vec v| < r + 0 + r = \tfrac23 d,
> $$
>
> using $|\lambda| = |\lambda'| = 1$; a contradiction, so $A \cap B = \emptyset$. Since $\pi$ is open and $A$, $B$ are disjoint and saturated, $\pi(A)$ and $\pi(B)$ are disjoint open neighbourhoods of $u$ and $v$.

^pf-3-29-2

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11|Def. §3.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-6|Def. §3.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^pf-3-29|§3.29 (openness of the relation)]], [[Continuous Image of a Compact Space is Compact]], [[Compact Subspace of a Hausdorff Space is Closed]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]

> [!remark] Remark
> The one place the group enters the direct proof is $|\lambda \vec u - \lambda \vec z_1| = |\vec u - \vec z_1|$: every $\lambda \in S^1$ is an *isometry*, so the thickening by $r$ is uniform over the whole group. That uniformity — a compact group acting by isometries — is the concrete mechanism behind [[§6 Group Actions and Orbit Spaces#^cor-6-4|Corollary §6.4]], and it is exactly what fails for $\mathbb{R}^+$ in [[§6 Group Actions and Orbit Spaces#^ex-6-6|Example §6.6]], where $t \cdot (x,y) = (tx, y/t)$ distorts distances without bound.

^rem-3-17

> [!theorem] Proposition §3.30: $\mathbb{CP}^n$ Is Compact
> $\mathbb{CP}^n$ is compact.
>
> *Lee: Problem 1-9*

^prop-3-30

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $S^{2n+1} \subseteq \mathbb{R}^{2n+2}$ is closed and bounded, hence compact ([[§1 Point-Set Topology Review#^prop-1-8|Proposition §1.8]](1)), and $\mathbb{CP}^n = \pi(S^{2n+1})$ is its image under the continuous surjection $\pi$.

^pf-3-30

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11|Def. §3.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-13|§3.13]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Heine–Borel Theorem]], [[Continuous Image of a Compact Space is Compact]]

> [!theorem] Proposition §3.31: $\mathbb{CP}^n$ as the Space of Complex Lines
> Let the multiplicative group $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ act on $\mathbb{C}^{n+1} \setminus \{0\}$ by scalar multiplication, $\lambda \cdot \vec z = \lambda \vec z$. Then:
> 1. this is a continuous action, and the orbit of $\vec z$ is the punctured complex line $\operatorname{span}_{\mathbb{C}}(\vec z) \setminus \{0\}$; so the orbit space $(\mathbb{C}^{n+1} \setminus \{0\})/\mathbb{C}^\times$ is in natural bijection with the set of complex lines through the origin in $\mathbb{C}^{n+1}$;
> 2. the map
>
> $$
> \Theta : \big(\mathbb{C}^{n+1} \setminus \{0\}\big)/\mathbb{C}^\times \longrightarrow S^{2n+1}/S^1, \qquad \mathbb{C}^\times\vec z \longmapsto S^1 \cdot \frac{\vec z}{|\vec z|},
> $$
>
> is a homeomorphism.
>
> Consequently the two natural quotient topologies on the set of lines agree, and either may be taken as the topology of $\mathbb{CP}^n$.
>
> *Lee: Problem 1-9*

^prop-3-31

![[m591-3-7.svg]]
*Here $g(\vec z) = \vec z/|\vec z|$ and $\iota$ is the inclusion. Both squares commute: $\Theta \circ \pi_1 = \pi_2 \circ g$ and $\Psi \circ \pi_2 = \pi_1 \circ \iota$. Upstairs, $g$ and $\iota$ are **not** mutually inverse — $g \circ \iota = \mathrm{id}$, but $\iota \circ g$ replaces $\vec z$ by $\vec z/|\vec z|$. Downstairs they become inverse, because passing to the quotient forgets exactly the scale that $\iota \circ g$ changes. The proof below is the chase around these two squares.*

> [!proof]+ Proof
> Write $\pi_1 : \mathbb{C}^{n+1}\setminus\{0\} \to (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^\times$ and $\pi_2 : S^{2n+1} \to S^{2n+1}/S^1$ for the two projections, both quotient maps.
>
> (1) If $\lambda \neq 0$ and $\vec z \neq 0$ then $\lambda\vec z \neq 0$, so the action preserves $\mathbb{C}^{n+1}\setminus\{0\}$. The axioms are $1 \cdot \vec z = \vec z$ and associativity of multiplication in $\mathbb{C}$, coordinatewise. Continuity: each component $(\lambda, \vec z) \mapsto \lambda z_k$ is polynomial in the real and imaginary parts ([[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Definition §5.8]]), and the action is the restriction of this map to a subspace. The orbit $\{\lambda\vec z : \lambda \neq 0\}$ is $\operatorname{span}_{\mathbb{C}}(\vec z) \setminus \{0\}$, and a line $\ell$ is recovered from $\ell \setminus \{0\}$ by adjoining $0$.
>
> (2) *$\Theta$ is well defined and continuous.* Let $g(\vec z) = \vec z/|\vec z|$, continuous on $\mathbb{C}^{n+1} \setminus \{0\}$ with values in $S^{2n+1}$. For $\lambda \in \mathbb{C}^\times$,
>
> $$
> g(\lambda\vec z) = \frac{\lambda}{|\lambda|}\, g(\vec z), \qquad \Big|\frac{\lambda}{|\lambda|}\Big| = 1,
> $$
>
> so $g(\lambda\vec z)$ and $g(\vec z)$ lie in the same $S^1$-orbit: $\pi_2 \circ g$ is constant on the fibres of $\pi_1$, although $g$ itself is not. By the universal property ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|Theorem §3.18]]), $\pi_2 \circ g$ descends to a unique continuous map on the $\mathbb{C}^\times$-quotient, which is $\Theta$.
>
> *The inverse is continuous.* Let $\iota : S^{2n+1} \hookrightarrow \mathbb{C}^{n+1}\setminus\{0\}$ be the inclusion. Then $\pi_1 \circ \iota$ is continuous and constant on $S^1$-orbits, since $S^1 \subseteq \mathbb{C}^\times$; so it descends to a continuous $\Psi : S^{2n+1}/S^1 \to (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^\times$, $S^1\vec z \mapsto \mathbb{C}^\times \vec z$.
>
> *They are mutually inverse.* For $|\vec z| = 1$, $\Theta(\Psi(S^1\vec z)) = S^1 \vec z$; for $\vec z \neq 0$, $\Psi(\Theta(\mathbb{C}^\times\vec z)) = \mathbb{C}^\times(\vec z/|\vec z|) = \mathbb{C}^\times\vec z$, the vector $\vec z/|\vec z|$ lying in the $\mathbb{C}^\times$-orbit of $\vec z$.

^pf-3-31

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-11|Def. §3.11]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^ex-3-5|Ex. §3.5]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-18|§3.18]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-8|Def. §5.8]], [[§6 Group Actions and Orbit Spaces#^def-6-1|Def. §6.1]], [[§6 Group Actions and Orbit Spaces#^def-6-2|Def. §6.2]], [[§6 Group Actions and Orbit Spaces#^def-6-5|Def. §6.5]]

> [!remark]- Connections
> - The $\mathbb{C}^\times$-description gives homogeneous coordinates: [[§8 Differentiable Structures#^def-8-10|Def. §8.10]]; the real analogue is [[§8 Differentiable Structures#^prop-8-11|§8.11]].

> [!remark] Remark
> The key identity behind (2) is that for a unit vector $\vec z$ the part of its $\mathbb{C}^\times$-orbit lying on the sphere is exactly its $S^1$-orbit: $|\lambda\vec z| = |\lambda|$, which equals $1$ iff $\lambda \in S^1$. So each punctured line meets the unit sphere in precisely one circle, and normalizing $\vec z \mapsto \vec z/|\vec z|$ is the bridge between the two descriptions — a point downstairs, a whole line upstairs in one, a circle upstairs in the other.

^rem-3-18

> [!example] Example §3.8: Why the Origin Must Be Removed
> Let $\mathbb{C}^\times$ act instead on all of $\mathbb{C}^{n+1}$ by scalar multiplication. The action is still continuous, but the orbit space acquires one extra point, the orbit $\{\lambda \cdot 0\} = \{0\}$, which is not a line; and that point cannot be separated from any other. Indeed, let $U$ be an open set of the quotient containing $\{0\}$. Its preimage is open, saturated, and contains $0$, hence contains a ball $B(0,\varepsilon)$. For every $\vec z \neq 0$ the vector $\frac{\varepsilon}{2|\vec z|}\vec z$ lies in that ball and in the orbit of $\vec z$, so by saturation the preimage contains every orbit. Thus $U$ is the whole quotient: every neighbourhood of $\{0\}$ contains every point, and the quotient is not Hausdorff. Deleting the origin removes exactly this one orbit. Every orbit accumulates at $0$ — the same pathology as [[§6 Group Actions and Orbit Spaces#^ex-6-6|Example §6.6]], where orbits accumulate on other orbits, here concentrated at a single point.

^ex-3-8

> [!remark] Remark: Where This Is Going
> $\mathbb{CP}^n$ is “one of the main examples of manifolds” and will recur throughout the course. With $T_2$ and second countability now secured, what is missing from manifold status is the locally Euclidean condition — charts on $\mathbb{CP}^n$ — which is supplied in [[§8 Differentiable Structures#Projective Spaces as Smooth Manifolds|§8, Projective Spaces as Smooth Manifolds]], together with the smooth structure. The same two-step pattern ($\sim$ open via a group acting by homeomorphisms + graph closed via compactness) is the template for many quotient constructions to come: real projective space $\mathbb{RP}^n$ (Lee Example 1.5), Grassmannians, tori, and lens spaces all fit it.

^rem-3-19
