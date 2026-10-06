---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 3
tags: [differentiable-manifolds, math591]
---
← [[§2 Topological Manifolds]] · ↑ [[· 1 Topological Manifolds]] · [[§4 Quotient Spaces and Open Maps]] →

*Thread: quotients — New spaces from old, first the easy constructions: subspaces and products, with the universal properties that make maps into them easy to check.*

*Reference: Lee Appendix A (“Subspaces, Products, Disjoint Unions, and Quotients”); MATH 590 notes [[§5 Subspace Topology|§5]] (subspaces), [[§4 Product Topology|§4]] (products), [[§13 Quotient Topology|§13]] (quotients).*

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
> In 590 [[§5 Subspace Topology#^def-5-1|§5]] the same topology was defined by naming it as a collection, $\mathcal{T}_S = \{\, U \cap S \mid U \in \mathcal{T} \,\}$; [[§3 Subspaces and Products#^def-3-1|Definition §3.1]] just says which sets belong to it. Three facts about it from 590 are used repeatedly in these notes and are recorded here with proofs.

^rem-3-2

> [!theorem] Lemma §3.1: Basis of a Subspace
> If $\mathcal{B}$ is a basis for $X$ and $S \subseteq X$, then $\mathcal{B}_S = \{\, B \cap S \mid B \in \mathcal{B} \,\}$ is a basis for the subspace topology on $S$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^lem-3-1

> [!proof]+ Proof
> Each $B \cap S$ is open in $S$ by definition. Let $V$ be open in $S$ and $p \in V$; write $V = U \cap S$ with $U$ open in $X$. Since $p \in U$, there is $B \in \mathcal{B}$ with $p \in B \subseteq U$, and then $p \in B \cap S \subseteq U \cap S = V$. This is [[§1 Point-Set Topology Review#^def-1-1|Definition §1.1]].

^pf-3-1

*Uses:* [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]]

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

*Uses:* [[§3 Subspaces and Products#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - Home in MATH 590: [[§5 Subspace Topology#^lem-5-2|590 §5.2]]; closed analogue [[§7 Closed Sets and Limit Points#^thm-7-3|590 §7.3]], used in [[§5 Quotient Maps#^lem-5-8|§5.8]].

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

*Uses:* [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§10 Continuous Functions#^thm-10-4|590 §10.4]]

> [!remark]- Connections
> - In MATH 590 these are the inclusion and range rules of [[§10 Continuous Functions#^thm-10-4|590 §10.4 (Rules for Continuous Functions)]].

> [!theorem] Corollary §3.4: The Universal Property Characterizes the Subspace Topology
> The subspace topology is the unique topology $\mathcal{T}$ on $S$ such that, for every space $Z$, a map $f : Z \to (S, \mathcal{T})$ is continuous if and only if $\iota \circ f : Z \to X$ is continuous.
>
> *Lee: Proposition A.17(b)*

^cor-3-4

> [!proof]+ Proof
> The subspace topology has the property by [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]](2). Suppose $\mathcal{T}$ has it. Taking $Z = (S, \mathcal{T})$ and $f = \mathrm{id}$, which is continuous, $\iota$ is continuous for $\mathcal{T}$, so $\mathcal{T}$ contains the subspace topology, the coarsest such ([[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]](1)). Taking $Z$ to be $S$ with the subspace topology and $f = \mathrm{id}$, the composite $\iota \circ \mathrm{id} = \iota$ is continuous, so the property makes $\mathrm{id}$ continuous from the subspace topology to $\mathcal{T}$, i.e. $\mathcal{T}$ is contained in the subspace topology.

^pf-3-4

*Uses:* [[§3 Subspaces and Products#^prop-3-3|§3.3]]

This completes the pattern: each of the three constructions — subspace, product ([[§3 Subspaces and Products#^cor-3-11|Corollary §3.11]]) and quotient ([[§5 Quotient Maps#^cor-5-3|Corollary §5.3]]) — has its topology characterized by its universal property.

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
> (2) If $\{U_\alpha\}_{\alpha \in A}$ is a countable basis of $X$, then $\{U_\alpha \cap S\}_{\alpha \in A}$ is a basis of $S$ by [[§3 Subspaces and Products#^lem-3-1|Lemma §3.1]], and it is indexed by the same countable set $A$.

^pf-3-5

*Uses:* [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§3 Subspaces and Products#^lem-3-1|§3.1]]

> [!remark]- Connections
> - Home in MATH 590: second countability of subspaces is [[§22 Countability Axioms#^thm-22-3|590 §22.3]]; Hausdorff is [[§9 Hausdorff Spaces#^def-9-1|590 Def. §9.1]].
> - Used ad hoc for spheres in [[§8 Spheres#^ex-8-1|Ex. §8.1]] and [[§8 Spheres#^prop-8-1|§8.1]]; reused for level sets in [[§7 The Regular Value Theorem#^thm-7-3|§7.3]].

> [!theorem] Proposition §3.6: Open Subsets of Manifolds Are Manifolds
> An open subset $S$ of a topological $n$-manifold $X$, with the subspace topology, is a topological $n$-manifold.
>
> *Lee: Example 1.26*

^prop-3-6

> [!proof]+ Proof
> $S$ is Hausdorff and second countable by [[§3 Subspaces and Products#^thm-3-5|Theorem §3.5]]. For $p \in S$ choose a chart $(U, \varphi)$ of $X$ at $p$. Then $U \cap S$ is open in $X$, hence in $S$, and $(U \cap S, \varphi|_{U \cap S})$ is a chart by [[§2 Topological Manifolds#^lem-2-10|Lemma §2.10]](1). [[§2 Topological Manifolds#^prop-2-3|Proposition §2.3]] finishes. ([[§3 Subspaces and Products#^lem-3-2|Lemma §3.2]] is what makes “open in $S$” and “open in $X$” interchangeable here.)

^pf-3-6

*Uses:* [[§2 Topological Manifolds#^def-2-2|Def. §2.2]], [[§3 Subspaces and Products#^thm-3-5|§3.5]], [[§2 Topological Manifolds#^lem-2-10|§2.10]], [[§2 Topological Manifolds#^prop-2-3|§2.3]], [[§3 Subspaces and Products#^lem-3-2|§3.2]]

> [!definition] Definition §3.2: Open Submanifold
> An **open submanifold** of a topological $n$-manifold $X$ is an open subset $S \subseteq X$ with the subspace topology — a topological $n$-manifold by [[§3 Subspaces and Products#^prop-3-6|Proposition §3.6]].
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
> - Home in MATH 590: [[§4 Product Topology#^def-4-1|590 Def. §4.1]]; arbitrary products in [[§11 Product Topology on Arbitrary Products#^def-11-1|590 Def. §11.1]].
> - Smooth version: [[§19 Smooth Functions and Smooth Maps#^prop-19-8|The Product Smooth Structure, §19.8]].

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

*Uses:* [[§1 Point-Set Topology Review#^def-1-2|Def. §1.2]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]]

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

*Uses:* [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§3 Subspaces and Products#^prop-3-7|§3.7]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^prop-1-1|§1.1]]

> [!remark] Remark: Cartoons
> Uribe on the figure above: diagrams of this kind are “incredibly important and useful”—an open set in a product is one in which every point can be surrounded by a *box*. The box picture is what actually gets used in proofs (it reappears in the second-countability part of [[§3 Subspaces and Products#^thm-3-12|Theorem §3.12]] and in the proof of the [[§6 Open Quotients#^pf-6-1|Hausdorff Criterion]] below), and he encourages drawing it every time.

^rem-3-4

> [!theorem] Proposition §3.9: Coarsest Topology with Continuous Projections
> Let $\pi_X : X \times Y \to X$ and $\pi_Y : X \times Y \to Y$ be the projection maps. The product topology is the *coarsest* topology on $X \times Y$ for which $\pi_X$ and $\pi_Y$ are both continuous.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^prop-3-9

> [!proof]+ Proof (not given in lecture)
> The product topology makes the projections continuous: $\pi_X^{-1}(U) = U \times Y$ and $\pi_Y^{-1}(V) = X \times V$ are basis elements. Conversely, let $\mathcal{T}$ be any topology on $X \times Y$ making both projections continuous. For $U \subseteq X$, $V \subseteq Y$ open, $\mathcal{T}$ contains $U \times Y$ and $X \times V$, hence their intersection $U \times V$. So $\mathcal{T}$ contains the basis $\mathcal{B}$, hence contains all unions of members of $\mathcal{B}$, i.e. every set open in the product topology. Thus the product topology is contained in every such $\mathcal{T}$.

^pf-3-9

*Uses:* [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§1 Point-Set Topology Review#^prop-1-1|§1.1]]

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

*Uses:* [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§3 Subspaces and Products#^prop-3-9|§3.9]], [[§1 Point-Set Topology Review#^prop-1-5|§1.5]] (1), [[§10 Continuous Functions#^thm-10-4|590 §10.4]]

> [!remark]- Connections
> - Home in MATH 590: [[§11 Product Topology on Arbitrary Products#^thm-11-1|590 §11.1 (Continuity into Product Spaces)]]; imported in [[§1 Point-Set Topology Review#^prop-1-5|§1.5]].
> - Smooth version: [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]], [[§19 Smooth Functions and Smooth Maps#^prop-19-9|§19.9]].

> [!remark] Remark: Why the Universal Property Matters
> “To check that $F$ is continuous, you just check component by component.” Uribe flagged that the same pattern will reappear for *differentiability*: a map into a product of manifolds will be smooth iff its components are. In Lee's language this is the *characteristic property* of the product topology (Lee Prop. A.16), and it characterizes the product topology uniquely ([[§3 Subspaces and Products#^cor-3-11|Corollary §3.11]] below). Together with the previous proposition this gives two independent abstract descriptions of the same topology—“coarsest making projections continuous” and “the one that lets you check maps componentwise.”
>
> Compare [[§3 Subspaces and Products#^prop-3-3|Proposition §3.3]]: the subspace topology is the coarsest making the inclusion continuous, and continuity of a map *into* $S$ is checked by composing with $\iota$. The quotient topology will complete the pattern in the opposite direction (Proposition [[§5 Quotient Maps#^cor-5-2|§5.2]]): it is the *finest* making $\pi$ continuous, and continuity of a map *out of* $X/{\sim}$ is checked by precomposing with $\pi$.

^rem-3-5

> [!theorem] Corollary §3.11: The Universal Property Characterizes the Product Topology
> The product topology is the unique topology $\mathcal{T}$ on $X \times Y$ such that, for every space $Z$, a map $f : Z \to (X \times Y, \mathcal{T})$ is continuous if and only if $\pi_X \circ f$ and $\pi_Y \circ f$ are continuous.
>
> *Lee: Proposition A.23(b)*

^cor-3-11

> [!proof]+ Proof
> The product topology has the property by [[§3 Subspaces and Products#^thm-3-10|Theorem §3.10]]. Suppose $\mathcal{T}$ has it. Taking $Z = (X \times Y, \mathcal{T})$ and $f = \mathrm{id}$, which is continuous, the projections are continuous for $\mathcal{T}$, so $\mathcal{T}$ contains the product topology by [[§3 Subspaces and Products#^prop-3-9|Proposition §3.9]]. Taking $Z$ to be $X \times Y$ with the product topology and $f = \mathrm{id}$, whose components $\pi_X$ and $\pi_Y$ are continuous there, the property makes $\mathrm{id}$ continuous from the product topology to $\mathcal{T}$, i.e. $\mathcal{T}$ is contained in the product topology.

^pf-3-11

*Uses:* [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§3 Subspaces and Products#^prop-3-9|§3.9]]

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

*Uses:* [[§1 Point-Set Topology Review#^def-1-8|Def. §1.8]], [[§1 Point-Set Topology Review#^def-1-6|Def. §1.6]], [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§3 Subspaces and Products#^prop-3-8|§3.8]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - Home in MATH 590: second countability of products is [[§22 Countability Axioms#^thm-22-3|590 §22.3]].
> - Gives product manifolds their point-set hygiene: [[§19 Smooth Functions and Smooth Maps#^prop-19-8|§19.8]].

> [!remark] Remark
> Both statements extend to finite products by induction. For *infinite* products the story is subtler (product vs. box topology, 590 [[§11 Product Topology on Arbitrary Products#^def-11-2|§11]]), but finite products are all we need: they are how product manifolds like the torus $T^n = S^1 \times \cdots \times S^1$ will get their point-set hygiene for free, leaving only local Euclideanness to check.

^rem-3-6
