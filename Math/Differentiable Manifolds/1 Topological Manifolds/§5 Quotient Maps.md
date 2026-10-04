---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 5
tags: [differentiable-manifolds, math591]
---
← [[§4 Quotient Spaces and Open Maps]] · ↑ [[· 1 Topological Manifolds]] · [[§6 Open Quotients]] →

*Thread: quotients — The quotient topology as a property of a map: how quotients are recognized in practice, and how maps out of them are built.*

So far “quotient” has named a topology on a set of equivalence classes. The same notion can be phrased as a property of a map, which is often how it is recognized in practice.

> [!definition] Definition §5.1: Quotient Map
> A map $F : X \to Y$ between topological spaces is a **quotient map** if it is surjective and
>
> $$
> U \subseteq Y \text{ is open} \iff F^{-1}(U) \subseteq X \text{ is open}.
> $$
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^def-5-1

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^def-12-1|590 Def. §12.1]].

> [!example] Example §5.1: Projections onto Quotient Spaces Are Quotient Maps
> The projection $\pi : X \to X/{\sim}$ of [[§4 Quotient Spaces and Open Maps#^def-4-1|Definition §4.1]] is a quotient map in the sense of [[§5 Quotient Maps#^def-5-1|Definition §5.1]]: it is surjective, and $W$ is open in $X/{\sim}$ if and only if $\pi^{-1}(W)$ is open in $X$, which is the definition of the quotient topology. The [[§5 Quotient Maps#^prop-5-4|next proposition]] says that these are the only examples.

^ex-5-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§5 Quotient Maps#^def-5-1|Def. §5.1]]

> [!definition] Definition §5.2: Maps Constant on Fibres
> Let $p : X \to Y$ be a map. A map $g : X \to Z$ is **constant on the fibres of $p$** if it is constant on $p^{-1}(\{y\})$ for every $y \in Y$; equivalently, $p(x) = p(x')$ implies $g(x) = g(x')$.

^def-5-2

> [!theorem] Theorem §5.1: Universal Property of a Quotient Map
> Let $p : X \to Y$ be a quotient map ([[§5 Quotient Maps#^def-5-1|Definition §5.1]]), let $Z$ be a topological space, and let $g : X \to Z$ be a map that is constant on the fibres of $p$ ([[§5 Quotient Maps#^def-5-2|Definition §5.2]]). Then there is a *unique* map $f : Y \to Z$ with
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

^thm-5-1

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

^pf-5-1

*Uses:* [[§5 Quotient Maps#^def-5-1|Def. §5.1]], [[§5 Quotient Maps#^def-5-2|Def. §5.2]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]]

> [!remark]- Connections
> - Home in MATH 590: [[Universal Property of Quotient Maps|590 §12.3 (Universal Property of Quotient Maps)]]; composites of quotient maps are [[§12 Quotient Topology#^ex-12-4|590 Ex. §12.4]].
> - Linear counterpart: [[§20 Linear Algebra Toolkit#^prop-20-6|Quotient Spaces and Their Universal Property, §20.6]].

> [!theorem] Corollary §5.2: The Form Used in Practice
> Let $\sim$ be an equivalence relation on $X$ with projection $\pi : X \to X/{\sim}$.
> 1. If $g : X \to Z$ is constant on equivalence classes, there is a unique $\overline{g} : X/{\sim} \to Z$ with $\overline{g} \circ \pi = g$, and $\overline{g}$ is continuous if and only if $g$ is.
> 2. For any function $h : X/{\sim} \to Z$: $h$ is continuous $\iff$ $h \circ \pi$ is continuous.
>
> *Lee: Theorem A.30*

^cor-5-2

> [!proof]+ Proof
> $\pi$ is a quotient map by the definition of the quotient topology, and its fibres are the equivalence classes, so (1) is [[§5 Quotient Maps#^thm-5-1|Theorem §5.1]] verbatim. For (2), apply the theorem to $g = h \circ \pi$, which is constant on each class because $\pi$ is; the unique $f$ with $f \circ \pi = g$ is $h$ itself, and (1) of the theorem gives the equivalence.

^pf-5-2

*Uses:* [[§5 Quotient Maps#^ex-5-1|Ex. §5.1]], [[§5 Quotient Maps#^thm-5-1|§5.1]]

> [!theorem] Corollary §5.3: The Universal Property Characterizes the Quotient Topology
> Let $X$ be a topological space, $Y$ a set, and $p : X \to Y$ a surjection. The quotient topology is the *unique* topology $\mathcal{T}$ on $Y$ with the property that for every topological space $Z$ and every function $f : Y \to Z$,
>
> $$
> f \text{ is continuous} \iff f \circ p \text{ is continuous.}
> $$
>
> *Lee: Theorem A.27(b)*

^cor-5-3

> [!proof]+ Proof
> The quotient topology has the property: with the quotient topology, $p$ is a quotient map by [[§5 Quotient Maps#^def-5-1|Definition §5.1]], so [[§5 Quotient Maps#^thm-5-1|Theorem §5.1]](1) applies to $g = f \circ p$, which is constant on the fibres of $p$. Suppose $\mathcal{T}$ and $\mathcal{T}'$ both have it. Taking $Z = (Y,\mathcal{T})$ and $f = \mathrm{id}$, which is continuous, the property of $\mathcal{T}$ gives that $p : X \to (Y,\mathcal{T})$ is continuous; likewise $p : X \to (Y,\mathcal{T}')$ is continuous. Now take $Z = (Y,\mathcal{T}')$ and $f = \mathrm{id} : (Y,\mathcal{T}) \to (Y,\mathcal{T}')$. Then $f \circ p = p : X \to (Y,\mathcal{T}')$ is continuous, so by the property of $\mathcal{T}$ the map $f$ is continuous, i.e. $\mathcal{T}' \subseteq \mathcal{T}$. Exchanging the roles gives $\mathcal{T} \subseteq \mathcal{T}'$.

^pf-5-3

*Uses:* [[§5 Quotient Maps#^def-5-1|Def. §5.1]], [[§5 Quotient Maps#^thm-5-1|§5.1]]

> [!remark]- Connections
> - Uniqueness of the quotient topology in MATH 590: [[§12 Quotient Topology#^prop-12-1|590 §12.1]].

> [!remark] Remark: How This Gets Used
> This is 590 [[§12 Quotient Topology#^thm-12-3|§12]] material (Munkres Theorem 22.2, Lee Theorem A.27), stated there in the full form above; it was not repeated in lecture but is used constantly here. The recipe it encodes is: *to define a continuous map out of a quotient, never define it on the quotient.* Define it upstairs on $X$, check it is constant on the classes, check continuity upstairs — and the theorem delivers a unique continuous map downstairs. Every identification in these notes is made this way:
> - $\rho : \mathbb{R}^3/\mathrm{SO}(3) \to [0,\infty)$, $[x] \mapsto |x|$, from the norm on $\mathbb{R}^3$ ([[§12 Group Actions and Orbit Spaces#^ex-12-5|Example §12.5]]);
> - $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$, from the orbit map on $G$ ([[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|Theorem §14.3]]);
> - $\overline{F} : X/{\sim} \to Y$ recognizing a quotient map ([[§5 Quotient Maps#^prop-5-4|Proposition §5.4]]);
> - continuity of the charts on $\mathbb{CP}^n$ and $\mathbb{RP}^n$ ([[§17 Projective Spaces as Smooth Manifolds|§17, Projective Spaces as Smooth Manifolds]]), applied locally via [[§5 Quotient Maps#^lem-5-7|Lemma §5.7]].
>
> Part (2) of [[§5 Quotient Maps#^thm-5-1|Theorem §5.1]] is what makes the recipe self-improving: if the map upstairs is itself a quotient map, the induced map downstairs is not merely continuous but a homeomorphism when injective, since a bijective quotient map is a homeomorphism.

^rem-5-1

> [!theorem] Proposition §5.4: A Quotient Map Presents Its Target as a Quotient
> Let $F : X \to Y$ be a quotient map and let $\sim$ be the relation on $X$ defined by $a \sim b \iff F(a) = F(b)$ (an equivalence relation, the fibres of $F$ being its classes). Then
>
> $$
> \overline{F} : X/{\sim} \longrightarrow Y, \qquad \overline{F}([a]) = F(a)
> $$
>
> is a homeomorphism, and $F = \overline{F} \circ \pi$.
>
> *Lee: Theorem A.31*

^prop-5-4

> [!proof]+ Proof
> *Well defined and bijective.* $\overline{F}$ is well defined because $a \sim b$ means $F(a) = F(b)$, and injective because $F(a) = F(b)$ means $a \sim b$, i.e. $[a] = [b]$; it is surjective because $F$ is. The factorization $F = \overline{F} \circ \pi$ holds by construction.
>
> *Continuity of $\overline{F}$.* $\overline{F} \circ \pi = F$ is continuous, so $\overline{F}$ is continuous by the universal property of the quotient (Corollary [[§5 Quotient Maps#^cor-5-2|§5.2]]).
>
> *Continuity of $\overline{F}^{-1}$.* Let $W \subseteq X/{\sim}$ be open; we show $\overline{F}(W)$ is open in $Y$, which is exactly continuity of $\overline{F}^{-1}$. Since $F$ is a quotient map it suffices to show $F^{-1}(\overline{F}(W))$ is open in $X$. But
>
> $$
> F^{-1}\big(\overline{F}(W)\big) = \pi^{-1}\big(\overline{F}^{-1}(\overline{F}(W))\big) = \pi^{-1}(W),
> $$
>
> using $F = \overline{F} \circ \pi$ for the first equality and injectivity of $\overline{F}$ for the second; and $\pi^{-1}(W)$ is open because $W$ is.

^pf-5-4

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§5 Quotient Maps#^def-5-1|Def. §5.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]]

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^cor-12-4|590 §12.4 (Induced Bijection from Quotient)]].

> [!remark] Remark
> So “quotient map” and “presentation of the target as a quotient space” are the same notion, and one may use whichever is convenient: to recognize a quotient topology, exhibit a quotient map onto it. Stated without proof in PSet 1, Problem 5.

^rem-5-2

> [!theorem] Proposition §5.5: Open Surjections Are Quotient Maps
> A continuous open surjection $F : X \to Y$ is a quotient map.

^prop-5-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* ($\Rightarrow$) Continuity. ($\Leftarrow$) Suppose $F^{-1}(U)$ is open. Then $F(F^{-1}(U))$ is open, $F$ being an open map; and $F(F^{-1}(U)) = U$ because $F$ is surjective.

^pf-5-5

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§5 Quotient Maps#^def-5-1|Def. §5.1]]

> [!remark]- Connections
> - Home in MATH 590: [[§12 Quotient Topology#^prop-12-2|590 §12.2]] (open or closed continuous surjections).
> - Applied to $G \to G/H$: [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-2|§14.2]].

> [!example] Example §5.2: Projections Are Quotient Maps
> If $X_1, \ldots, X_n$ are nonempty topological spaces, every projection $\pi_i : X_1 \times \cdots \times X_n \to X_i$ is a quotient map: it is surjective (choose any point in each other factor), continuous, and open ([[§4 Quotient Spaces and Open Maps#^ex-4-2|Example §4.2]] and induction), so [[§5 Quotient Maps#^prop-5-5|Proposition §5.5]] applies. Nonemptiness is needed: if some $X_k = \emptyset$ the product is empty and $\pi_i$ is not surjective onto a nonempty $X_i$.

^ex-5-2

*Uses:* [[§4 Quotient Spaces and Open Maps#^ex-4-2|Ex. §4.2]], [[§5 Quotient Maps#^prop-5-5|§5.5]]

> [!remark] Remark
> This is PSet 1, Problem 5, where it is proved directly from the definition. The direct argument is worth seeing once: writing an open $\pi_i^{-1}(U)$ as a union of boxes $\bigcup_x U_{x,1} \times \cdots \times U_{x,n}$ and projecting gives $U = \bigcup_x U_{x,i}$, a union of open sets—and the step $\pi_i(U_{x,1} \times \cdots \times U_{x,n}) = U_{x,i}$ is exactly where nonemptiness of the other factors enters.

^rem-5-3

> [!theorem] Lemma §5.6: Open Surjections Push Bases Forward
> Let $\pi : Y \to Q$ be a continuous open surjection and $\mathcal{B}$ a basis for the topology of $Y$. Then $\pi(\mathcal{B}) = \{\pi(B) \mid B \in \mathcal{B}\}$ is a basis for the topology of $Q$. In particular, if $Y$ is second countable, so is $Q$.

^lem-5-6

> [!proof]+ Proof
> Each $\pi(B)$ is open, $\pi$ being an open map. Let $W \subseteq Q$ be open and $q \in W$. By surjectivity choose $y \in Y$ with $\pi(y) = q$. By continuity $\pi^{-1}(W)$ is open, and it contains $y$, so there is $B \in \mathcal{B}$ with $y \in B \subseteq \pi^{-1}(W)$. Applying $\pi$ and using $\pi(\pi^{-1}(W)) \subseteq W$,
>
> $$
> q = \pi(y) \in \pi(B) \subseteq W .
> $$
>
> By [[§1 Point-Set Topology Review#^def-1-1|Definition §1.1]], $\pi(\mathcal{B})$ is a basis. It is the image of $\mathcal{B}$ under $B \mapsto \pi(B)$, hence countable when $\mathcal{B}$ is.

^pf-5-6

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§1 Point-Set Topology Review#^def-1-1|Def. §1.1]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]]

> [!theorem] Lemma §5.7: Restricting a Quotient Map over an Open Set
> Let $p : X \to Y$ be a quotient map and $V \subseteq Y$ an open set, and put $W = p^{-1}(V)$. Then the restriction
>
> $$
> q := p|_W : W \longrightarrow V
> $$
>
> is a quotient map, where $W$ and $V$ carry the subspace topologies.
>
> *Lee: Theorem A.27(e)*

^lem-5-7

![[m591-3-5.svg]]
*The square commutes, and the horizontal arrows are inclusions of open sets. The lemma says the left arrow inherits the quotient property of the right one. Restricting a quotient map to an arbitrary subspace can destroy that property; restricting it over an open set cannot.*

> [!proof]+ Proof
> $q$ is surjective because $p$ is, and continuous as a restriction of a continuous map. Let $A \subseteq V$ be such that $q^{-1}(A)$ is open in $W$; we show $A$ is open in $V$. Since $A \subseteq V$,
>
> $$
> q^{-1}(A) = p^{-1}(A) \cap W = p^{-1}(A),
> $$
>
> as $p^{-1}(A) \subseteq p^{-1}(V) = W$. The set $W = p^{-1}(V)$ is open in $X$, $V$ being open and $p$ continuous; so a subset open in $W$ is open in $X$ ([[§3 Subspaces and Products#^lem-3-2|Lemma §3.2]]), and $p^{-1}(A)$ is open in $X$. As $p$ is a quotient map, $A$ is open in $Y$, hence in $V$. The reverse implication is continuity of $q$.

^pf-5-7

*Uses:* [[§5 Quotient Maps#^def-5-1|Def. §5.1]], [[§3 Subspaces and Products#^def-3-1|Def. §3.1]], [[§3 Subspaces and Products#^lem-3-2|§3.2]], [[§9 Continuous Functions#^thm-9-4|590 §9.4]]

> [!remark]- Connections
> - Used for the charts on $\mathbb{CP}^n$: [[§17 Projective Spaces as Smooth Manifolds#^prop-17-1|Each φᵢ Is a Chart, §17.1]].

> [!theorem] Lemma §5.8: Restricting a Quotient Map over a Closed Set
> [[§5 Quotient Maps#^lem-5-7|Lemma §5.7]] holds with “open” replaced by “closed”: if $p : X \to Y$ is a quotient map, $V \subseteq Y$ is closed and $W = p^{-1}(V)$, then $p|_W : W \to V$ is a quotient map.
>
> *Lee: Theorem A.27(e)*

^lem-5-8

> [!proof]+ Proof
> By taking complements, a continuous surjection is a quotient map exactly when a set is closed iff its preimage is closed. Let $C \subseteq V$ with $q^{-1}(C) = p^{-1}(C)$ closed in $W$. Now $W$ is closed in $X$, as $V$ is closed and $p$ continuous, and a set closed in a closed subspace is closed in the whole space: it is the intersection of $W$ with a closed subset of $X$. So $p^{-1}(C)$ is closed in $X$, hence $C$ is closed in $Y$ because $p$ is a quotient map, and therefore closed in $V$.

^pf-5-8

*Uses:* [[§5 Quotient Maps#^def-5-1|Def. §5.1]], [[§5 Quotient Maps#^lem-5-7|§5.7]], [[§6 Closed Sets and Limit Points#^thm-6-2|590 §6.2]], [[§6 Closed Sets and Limit Points#^thm-6-3|590 §6.3]]

> [!remark] Remark
> Both hypotheses are used, at different steps: that $W$ is a full preimage gives $q^{-1}(A) = p^{-1}(A)$, and that $V$ is open makes a set open in $W$ open in $X$. Without them the restriction of a quotient map need not be a quotient map. The lemma is what allows the universal property ([[§5 Quotient Maps#^thm-5-1|Theorem §5.1]]) to be applied *locally*, on an open piece of a quotient — which is exactly the situation of a chart on a quotient space ([[§17 Projective Spaces as Smooth Manifolds|§17, Projective Spaces as Smooth Manifolds]]). Both lemmas are from Assignment 2, Problem 2.

^rem-5-4
