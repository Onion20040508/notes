---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 7
tags: [differentiable-manifolds, math591]
---
← [[§6 Group Actions and Orbit Spaces]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§8 Differentiable Structures]] →

*Thread: quotients — A transitive action identifies a space with a coset space $G/H$; the Grassmannians are the payoff. The two threads meet in the [[· 3 Smooth Manifolds|next chapter]].*

*Reference: Lee Ch. 21, the section on homogeneous spaces; Lee Example 1.36 (Grassmannians). Logistics: a substitute lectures on Friday Sep 11; smooth structures are scheduled to begin then.*

> [!remark] Remark: Why This Section
> *Homogeneous spaces* are spaces on which a group acts transitively. They are identified with coset spaces $G/H$, which are themselves orbit spaces (of $H$ acting on $G$), so everything in [[§6 Group Actions and Orbit Spaces|§6]] applies. This is how spheres, projective spaces, and Grassmannians acquire their topology in one stroke: “that's a natural way to give a topology to homogeneous spaces.”

^rem-7-1

## Transitive Actions and Isotropy

> [!definition] Definition §7.1: Transitive Action and Homogeneous Space
> An action of $G$ on $X$ is **transitive** if there is only one orbit; equivalently,
>
> $$
> \forall\, x, y \in X\ \ \exists\, g \in G \text{ such that } y = g \cdot x .
> $$
>
> A topological space $X$ is **homogeneous** for the topological group $G$ if $G$ acts continuously and transitively on $X$.
>
> *Lee: Ch. 7 and Example 21.15*

^def-7-1

> [!remark]- Connections
> - Transitivity is defined in [[§25 Orbits#^def-25-1|493 Def. §25.1]]; the model transitive action is $G$ on $G/H$, [[§29 G Acting on Coset Spaces#^prop-29-1|493 §29.1]].

> [!remark] Remark
> For a transitive action the orbit space $X/G$ is a single point, “which is not that interesting.” The interesting quotient is a different one: $X$ itself will be exhibited as a quotient $G/H$ of the *group*, by the action of a subgroup $H$ on $G$.

^rem-7-2

> [!definition] Definition §7.2: Isotropy Subgroup
> For any action of $G$ on $X$ and any $x_0 \in X$, the **isotropy subgroup** (or **stabilizer**) of $x_0$ is
>
> $$
> H_{x_0} = \{\, g \in G \mid g \cdot x_0 = x_0 \,\},
> $$
>
> the set of group elements that do not move $x_0$.
>
> *Lee: Ch. 7, p. 162*

^def-7-2

> [!remark]- Connections
> - Home: [[§24 Stabilizers and Fixed Points#^def-24-1|493 Def. §24.1 (Stabilizer)]], written $\operatorname{Stab}(x_0)$ there.

> [!theorem] Proposition §7.1: The Isotropy Is a Subgroup
> $H_{x_0}$ is a subgroup of $G$.

^prop-7-1

> [!proof]+ Proof
> $e \in H_{x_0}$ since $e \cdot x_0 = x_0$. If $g, g' \in H_{x_0}$ then $(gg') \cdot x_0 = g \cdot (g' \cdot x_0) = g \cdot x_0 = x_0$. If $g \in H_{x_0}$ then $g^{-1} \cdot x_0 = g^{-1} \cdot (g \cdot x_0) = (g^{-1}g) \cdot x_0 = x_0$.

^pf-7-1

*Uses:* [[§7 Homogeneous Spaces#^def-7-2|Def. §7.2]], [[§6 Group Actions and Orbit Spaces#^def-6-1|Def. §6.1]], [[§4 Subgroups#^def-4-1|493 Def. §4.1]]

> [!remark]- Connections
> - Home of this result: [[§24 Stabilizers and Fixed Points#^prop-24-1|493 §24.1 (The Stabilizer Is a Subgroup)]].

> [!definition] Definition §7.3: Orbit Map
> Let a topological group $G$ act continuously on $X$, and let $x_0 \in X$. The **orbit map** of $x_0$ is
>
> $$
> \theta_{x_0} : G \to X, \qquad \theta_{x_0}(g) = g \cdot x_0 .
> $$
>
> It is continuous, being the action composed with $g \mapsto (g, x_0)$, and its image is the orbit of $x_0$.
>
> *Lee: Proposition 7.26*

^def-7-3

> [!theorem] Theorem §7.2: Isotropy Subgroups Are Closed
> Let $G$ be a topological group acting continuously on a topological space $X$ in which points are closed (for instance, $X$ Hausdorff). Then for every $x_0 \in X$ the isotropy subgroup $H_{x_0}$ is a *closed* subgroup of $G$.
>
> *Lee: proof of Theorem 21.18 (“closed by continuity)*

^thm-7-2

> [!proof]+ Exercise
> *(Claimed in Lecture 4 — “this is a closed subgroup”; filled in.)* Consider the orbit map $\theta_{x_0} : G \to X$, $\theta_{x_0}(g) = g \cdot x_0$, of Definition [[§7 Homogeneous Spaces#^def-7-3|§7.3]], and identify $H_{x_0}$ as a preimage under it. Two things are to be checked: that $\theta_{x_0}$ is continuous, and that the relevant subset of $X$ is closed. Uribe stated the result and said the closedness “may be the next assignment”; it was not proved in lecture, and the argument is left here.

^pf-7-2

*Uses:* [[§7 Homogeneous Spaces#^def-7-3|Def. §7.3]]

> [!remark]- Connections
> - “Points are closed” is the $T_1$ axiom, [[§19 Separation Axioms#^def-19-1|590 Def. §19.1]]; Hausdorff implies it by [[§8 Hausdorff Spaces#^thm-8-1|590 §8.1]].

**On the hypothesis.** The board stated the theorem with no condition on $X$, and in that form it is false, as the next example shows. What fails there is precisely that points of $X$ are not closed. Requiring $X$ to be $T_1$ — in particular Hausdorff, which is the case for every manifold — repairs the statement, and costs nothing in the applications: $\mathrm{O}(n)$ acting on $\mathrm{Gr}_k(\mathbb{R}^n)$, $\mathrm{SO}(3)$ on $S^2$, and every other action met here has Hausdorff target.

> [!example] Example §7.1: An Isotropy Group That Is Not Closed
> Let $G = \mathbb{R}$ act on $X = \mathbb{R}/\mathbb{Q}$, with the quotient topology, by $t \cdot [x] = [x+t]$. The action is continuous, but the isotropy group $H_{[0]} = \mathbb{Q}$ is not closed in $\mathbb{R}$. So Theorem [[§7 Homogeneous Spaces#^thm-7-2|§7.2]] fails without its hypothesis on $X$.

^ex-7-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* The action is well defined, since $x - x' \in \mathbb{Q}$ implies $(x+t) - (x'+t) \in \mathbb{Q}$. Every nonempty open saturated subset of $\mathbb{R}$ contains an interval and is invariant under adding rationals; since $\mathbb{Q}$ is dense, the translates of an interval by rationals cover $\mathbb{R}$, so the set is all of $\mathbb{R}$. Hence $X$ carries the indiscrete topology, every map into $X$ is continuous, and in particular so is the action. Finally
>
> $$
> H_{[0]} = \{\, t \in \mathbb{R} \mid [t] = [0] \,\} = \mathbb{Q},
> $$
>
> which is dense in $\mathbb{R}$ and not closed.

^pf-ex-7-1

*Uses:* [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|Def. §3.4]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-16|§3.16]], [[§6 Group Actions and Orbit Spaces#^def-6-2|Def. §6.2]], [[§7 Homogeneous Spaces#^def-7-2|Def. §7.2]]

> [!remark]- Connections
> - $X$ is indiscrete, the standard non-$T_1$ space: [[Discrete and indiscrete topologies]].

> [!example] Example §7.2: Isotropy of the North Pole under $\mathrm{SO}(3)$
> Let $\mathrm{SO}(3)$ act on $S^2 = \{x \in \mathbb{R}^3 \mid |x| = 1\}$ by rotations (matrix multiplication; it preserves the sphere since orthogonal matrices preserve norms). For $x_0 = (0,0,1)$, the answer from the floor: the isotropy consists of the rotations about the $z$-axis. In matrices, $g \cdot e_3 = e_3$ says the third column of $g$ is $e_3$; orthogonality then forces the third row to be $e_3^T$ as well (the columns are orthonormal, so the first two columns are orthogonal to $e_3$, i.e. have zero third entry), and the remaining $2 \times 2$ block is orthogonal with determinant $1$:
>
> $$
> H_{x_0} = \left\{ \begin{pmatrix} A & 0 \\ 0 & 1 \end{pmatrix} \;\middle|\; A \in \mathrm{SO}(2) \right\} \;\cong\; \mathrm{SO}(2) \;\cong\; S^1 .
> $$

^ex-7-2

> [!remark]- Connections
> - The same column-then-row argument for $\operatorname{Stab}(e_1)$ in $\mathrm{O}_3$: [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|493 §30.2]](2), [[§30 Examples꞉ Linear Groups and the Cube#^rem-30-1|493, GL₃ versus O₃]].

## The Coset Space $G/H$

> [!remark] Remark: The Organizing Fact
> Everything in this subsection and the next is a special case of [[§6 Group Actions and Orbit Spaces|§6]]. The coset space $G/H$ is not merely *like* an orbit space: it *is* one, for a suitable action of $H$ on $G$ (Proposition [[§7 Homogeneous Spaces#^prop-7-4|§7.4]]), with the same underlying set and the same projection map — so the quotient topology of [[§7 Homogeneous Spaces#^def-7-6|Def. §7.6]] and the orbit-space topology of Definition [[§6 Group Actions and Orbit Spaces#^def-6-5|§6.5]] are equal by construction, not merely homeomorphic. Consequently every result of [[§6 Group Actions and Orbit Spaces|§6]] applies to $G/H$ with no further work, and three facts below are obtained that way: $\pi$ is an open map (Lemma [[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]]), $G/H$ is Hausdorff under a compactness hypothesis (Corollary [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]]), and it is second countable (Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|§3.28]]).

^rem-7-3

> [!definition] Definition §7.4: Left Cosets and the Coset Space
> Let $H \le G$ be a subgroup of a group $G$. The **left coset** of $g \in G$ is
>
> $$
> gH \;=\; \{\, gh \mid h \in H \,\} \;\subseteq\; G,
> $$
>
> the translate of $H$ by $g$. The **coset space** $G/H$ is the set whose elements are the left cosets,
>
> $$
> G/H \;=\; \{\, gH \mid g \in G \,\}.
> $$
>
> (This is the algebraic quotient from [[§26 Left and Right Cosets#^def-26-2|MATH 493]]. Note that $G/H$ is a *group* only when $H$ is normal, which is not assumed here; for us it is only a set, and shortly a space.)
>
> *Lee: proof of Theorem 21.17*

^def-7-4

> [!remark]- Connections
> - Home: [[§26 Left and Right Cosets#^def-26-2|493 Def. §26.2 (Left and Right Cosets)]]; the group case (normal $H$) is [[§37 Quotient Groups|493 §37]], and in 590 [[§21 Algebra Prerequisites꞉ Groups#^def-21-13|590 Def. §21.13]].

> [!theorem] Lemma §7.3: When Two Cosets Coincide
> $gH = g'H \iff g^{-1}g' \in H$. Consequently the left cosets partition $G$.
>
> *Lee: proof of Theorem 21.17*

^lem-7-3

> [!proof]+ Proof
> *(Used in Lecture 4 as “$gH = g'H \iff g^{-1}g' \in H$”; filled in.)* ($\Rightarrow$) $g' = g'e \in g'H = gH$, so $g' = gh$ for some $h \in H$, i.e. $g^{-1}g' = h \in H$. ($\Leftarrow$) If $g^{-1}g' = h \in H$, then $g' = gh$, so $g'H = ghH = gH$ (as $hH = H$ for $h \in H$, $H$ being a subgroup). For the partition: $g \in gH$, and if $gH \cap g'H \ni a$, then $aH = gH$ and $aH = g'H$ by the first part, so $gH = g'H$.

^pf-7-3

*Uses:* [[§7 Homogeneous Spaces#^def-7-4|Def. §7.4]], [[§4 Subgroups#^def-4-1|493 Def. §4.1]]

> [!remark]- Connections
> - Home of this result: [[§26 Left and Right Cosets#^prop-26-2|493 §26.2 (Cosets Are the Equivalence Classes)]]; hub [[Cosets Partition a Group]].

> [!definition] Definition §7.5: The Canonical Projection
> The **canonical projection** associated with $H \le G$ is the map
>
> $$
> \pi : G \longrightarrow G/H, \qquad \pi(g) = gH,
> $$
>
> sending a group element to the coset containing it. It is surjective by construction, and by Lemma [[§7 Homogeneous Spaces#^lem-7-3|§7.3]] its fibres are exactly the cosets: $\pi^{-1}(gH) = gH$.
>
> *Lee: Theorem 21.17*

^def-7-5

> [!remark] Remark
> A point of $G/H$ is a *subset* of $G$, and $\pi$ is the map that forgets which element of that subset one started from. The two roles of the symbol $gH$ — a subset of $G$, and a single point of $G/H$ — are the usual source of confusion with quotients ([[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients|§3]]); the identity $\pi^{-1}(gH) = gH$ is that ambiguity made harmless, the left side reading $gH$ as a point and the right side as a set.

^rem-7-4

> [!theorem] Proposition §7.4: $G/H$ Is an Orbit Space
> Let $H \le G$. The formula
>
> $$
> H \times G \longrightarrow G, \qquad (h, g) \longmapsto g h^{-1}
> $$
>
> is an action of $H$ on $G$, and its orbits are exactly the left cosets: $\mathcal{O}_g = gH$. Hence $G/H$ (the set of left cosets) is the orbit space of this action.
>
> *Lee: proof of Theorem 21.17 ($H$ acting on $G$ by right translation)*

^prop-7-4

> [!proof]+ Proof
> *(Lecture 4 checked the action axiom, $(hh')\cdot g = h \cdot (h' \cdot g)$, on the board; the rest is filled in.)* *Action.* $e \cdot g = g e^{-1} = g$. For $h, h' \in H$: $(hh') \cdot g = g (hh')^{-1} = g\, h'^{-1} h^{-1} = (g h'^{-1}) h^{-1} = h \cdot (h' \cdot g)$. (The inverse is what makes the order of the factors come out right: multiplying on the right by $h$ itself would give $g h' h$, which is $(h'h) \cdot g$, the wrong order.) *Orbits.* $\mathcal{O}_g = \{\, g h^{-1} \mid h \in H \,\} = \{\, g h \mid h \in H \,\} = gH$, since $h \mapsto h^{-1}$ is a bijection of $H$.

^pf-7-4

*Uses:* [[§6 Group Actions and Orbit Spaces#^def-6-1|Def. §6.1]], [[§6 Group Actions and Orbit Spaces#^def-6-3|Def. §6.3]], [[§6 Group Actions and Orbit Spaces#^def-6-5|Def. §6.5]], [[§7 Homogeneous Spaces#^def-7-4|Def. §7.4]]

> [!remark]- Connections
> - In 493 the same orbits come from the *right* action $g \star h = gh$: [[§26 Left and Right Cosets#^prop-26-1|493 §26.1 (Cosets Are Orbits)]]; converting it to a left action by inverting is [[§23 Actions#^prop-23-1|493 §23.1 (A Left Action Gives a Right Action)]].

> [!remark] Remark
> The inverse in the formula is not cosmetic. The first thing one writes, $(h,g) \mapsto hg$, is also an action, but its orbits are the *right* cosets $Hg$, giving the other quotient $H \backslash G$. To produce *left* cosets from a *left* action of $H$ one must multiply on the right and invert, and that is exactly what makes the second axiom come out in the correct order, as the proof shows. For non-abelian $H$ the naive formula $(h,g) \mapsto gh$ fails the axiom outright.
>
> Proposition [[§7 Homogeneous Spaces#^prop-7-4|§7.4]] is a statement about sets; the topological half is Definition [[§7 Homogeneous Spaces#^def-7-6|§7.6]] together with the observation that the two projections $G \to G/H$ — the canonical one of Definition [[§7 Homogeneous Spaces#^def-7-5|§7.5]] and the orbit projection of Definition [[§6 Group Actions and Orbit Spaces#^def-6-5|§6.5]] — are the same function, so the two quotient topologies they induce are the same topology.

^rem-7-5

> [!theorem] Lemma §7.5: Homogeneous Spaces Are Coset Spaces
> Suppose $G$ acts transitively on $X$, fix a *base point* $x_0 \in X$, and let $H = H_{x_0}$. Then
>
> $$
> \Phi : G/H \longrightarrow X, \qquad \Phi(gH) = g \cdot x_0
> $$
>
> is a well-defined bijection.
>
> *Lee: proof of Theorem 21.18*

^lem-7-5

> [!proof]+ Proof
> *(Lecture 4 checked well-definedness — translate “the so-called base point” — on the board; injectivity and surjectivity are filled in.)* *Well defined.* If $gH = g'H$ then $g' = gh$ with $h \in H$ (Lemma [[§7 Homogeneous Spaces#^lem-7-3|§7.3]]), and
>
> $$
> g' \cdot x_0 = (gh) \cdot x_0 = g \cdot (h \cdot x_0) = g \cdot x_0,
> $$
>
> since $h$ fixes $x_0$. *Injective.* If $g \cdot x_0 = g' \cdot x_0$, apply $L_{g^{-1}}$: $x_0 = g^{-1} \cdot (g' \cdot x_0) = (g^{-1}g') \cdot x_0$, so $g^{-1}g' \in H$ and $gH = g'H$ by Lemma [[§7 Homogeneous Spaces#^lem-7-3|§7.3]]. *Surjective.* Given $y \in X$, transitivity gives $g$ with $y = g \cdot x_0 = \Phi(gH)$.

^pf-7-5

*Uses:* [[§7 Homogeneous Spaces#^lem-7-3|§7.3]], [[§7 Homogeneous Spaces#^def-7-1|Def. §7.1]], [[§7 Homogeneous Spaces#^def-7-2|Def. §7.2]], [[§6 Group Actions and Orbit Spaces#^def-6-1|Def. §6.1]], [[§6 Group Actions and Orbit Spaces#^lem-6-2|§6.2]]

> [!remark]- Connections
> - Home of this bijection: [[§28 Orbit–Stabilizer#^prop-28-2|493 §28.2 (The Orbit Bijection)]], same proof, for any orbit; hub [[Orbit–Stabilizer Theorem]].
> - Conversely every $G/H$ carries a transitive action with isotropy $H$ at $eH$: [[§29 G Acting on Coset Spaces#^prop-29-1|493 §29.1]].

> [!example] Example §7.3: The Sphere as a Homogeneous Space
> $\mathrm{SO}(3)$ acts transitively on $S^2$: the orbit of $e_3$ is the whole sphere (the argument of Example [[§6 Group Actions and Orbit Spaces#^ex-6-5|§6.5]] with $r = 1$). By Example [[§7 Homogeneous Spaces#^ex-7-2|§7.2]] the isotropy of $e_3$ is the copy $H$ of $\mathrm{SO}(2)$ in the upper-left block. Hence, as sets (and, by the [[§7 Homogeneous Spaces#^thm-7-8|theorem below]], as spaces),
>
> $$
> S^2 \;\cong\; \mathrm{SO}(3)/\mathrm{SO}(2).
> $$
>
> *Explicitly.* A point of $\mathrm{SO}(3)/H$ is a coset $gH = \{\, gh \mid h \in H \,\}$. Since $h e_3 = e_3$ for $h \in H$, every element of $gH$ has the same third column $g e_3$; conversely, if $g' e_3 = g e_3$ then $g^{-1} g' \in H$, so $g' \in gH$ (Lemma [[§7 Homogeneous Spaces#^lem-7-3|§7.3]]). Thus
>
> $$
> gH = \{\, \text{rotations whose third column is } g e_3 \,\},
> $$
>
> and the cosets are indexed by unit vectors. The identification $\Phi(gH) = g \cdot e_3 = g e_3$ reads off that third column; its inverse sends a unit vector $v \in S^2$ to the set of all rotations having $v$ as third column (nonempty, since some rotation carries $e_3$ to $v$). A set of unit vectors $W \subseteq S^2$ is open in the quotient topology iff the set of all rotations whose third column lies in $W$ is open in $\mathrm{SO}(3)$; Theorem [[§7 Homogeneous Spaces#^thm-7-8|§7.8]] says this agrees with the usual topology of $S^2 \subseteq \mathbb{R}^3$.
>
> *Lee: Examples 21.15(a) and 21.19(a)*

^ex-7-3

> [!remark]- Connections
> - The $\mathrm{O}_3$ version of orbit and stabilizer: [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|493 §30.2]].
> - Used for dimension counts in [[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9|Dimension Checks through Homogeneous Spaces]].

**Transcription note.** Page 12 of the handwritten notes writes “$X = \mathrm{SO}(3)$ acting on $S^2$”; the group is $G = \mathrm{SO}(3)$ and the space is $X = S^2$.

![[m591-7-1.svg]]
*The north pole $N$, its isotropy group $H \cong \mathrm{SO}(2)$ of rotations about the vertical axis, and a rotation $g$ carrying $N$ to $g \cdot N$.*

The picture behind Example [[§7 Homogeneous Spaces#^ex-7-3|§7.3]]. The rotations about the vertical axis fix the north pole $N$; they form the isotropy group $H \cong \mathrm{SO}(2)$. A rotation $g$ carries $N$ to $g \cdot N$, and the rotations carrying $N$ to that same point are exactly the products $gh$ with $h \in H$: the fibre of the orbit map $\theta_N$ over $g \cdot N$ is the coset $gH$. Collapsing each fibre to a point is the passage from $\mathrm{SO}(3)$ to $\mathrm{SO}(3)/\mathrm{SO}(2)$, which is why the coset space is the sphere (Theorem [[§7 Homogeneous Spaces#^thm-7-8|§7.8]]).

## The Topology of $G/H$

Definitions [[§7 Homogeneous Spaces#^def-7-4|§7.4]] and [[§7 Homogeneous Spaces#^def-7-5|§7.5]] are purely algebraic. If $G$ carries a topology, $G/H$ inherits one in the only reasonable way.

> [!definition] Definition §7.6: The Quotient Topology on a Coset Space
> Let $G$ be a topological group and $H \le G$ a subgroup. The **quotient topology** on $G/H$ is the quotient topology induced by the canonical projection $\pi$ of Definition [[§7 Homogeneous Spaces#^def-7-5|§7.5]], in the sense of Definition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|§3.4]]:
>
> $$
> W \subseteq G/H \text{ is open} \iff \pi^{-1}(W) \subseteq G \text{ is open in } G.
> $$
>
> Unless stated otherwise, $G/H$ always carries this topology.
>
> *Lee: Theorem 21.17*

^def-7-6

> [!remark]- Connections
> - The quotient topology in 590: [[§12 Quotient Topology#^def-12-2|590 Def. §12.2]].

> [!theorem] Proposition §7.6: Three Descriptions of the Open Sets
> Let $G$ be a topological group, $H \le G$, and $W \subseteq G/H$. The following are equivalent:
> 1. $W$ is open in $G/H$;
> 2. $\displaystyle\bigcup_{gH \in W} gH$, the union in $G$ of the cosets belonging to $W$, is open in $G$;
> 3. $W = \pi(U)$ for some open $U \subseteq G$ satisfying $UH = U$.
>
> Moreover $\pi$ is a continuous, surjective, *open* map, and the quotient topology is the finest topology on $G/H$ making $\pi$ continuous.
>
> *Lee: Theorem 21.17 and Lemma 21.1*

^prop-7-6

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $(1 \Leftrightarrow 2)$ By Definition [[§7 Homogeneous Spaces#^def-7-5|§7.5]] the fibre over a point $gH \in W$ is the coset $gH$, so $\pi^{-1}(W) = \bigcup_{gH \in W} gH$; now apply Definition [[§7 Homogeneous Spaces#^def-7-6|§7.6]].
>
> $(1 \Leftrightarrow 3)$ A subset $U \subseteq G$ satisfies $UH = U$ iff it is a union of cosets, i.e. iff it is saturated for the coset relation (Definition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|§3.7]]): $UH = \bigcup_{u \in U} uH$ always contains $U$, and equals $U$ exactly when each $uH \subseteq U$. If $W$ is open, take $U = \pi^{-1}(W)$, which is open, saturated, and has $\pi(U) = W$ by surjectivity of $\pi$. Conversely if $U$ is open with $UH = U$, then $\pi^{-1}(\pi(U)) = U$ by saturation (Lemma [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-15|§3.15]](4)), which is open, so $\pi(U)$ is open.
>
> *Openness of $\pi$.* For $U \subseteq G$ open, $\pi^{-1}(\pi(U)) = UH = \bigcup_{h \in H} Uh$, a union of translates of $U$. Right translation by $h$ is a homeomorphism of $G$ (it is continuous with continuous inverse, both restrictions of the multiplication of the topological group), so each $Uh$ is open and the union is open; hence $\pi(U)$ is open. Continuity and finest-topology are the general facts recorded after Definition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-4|§3.4]].

^pf-7-6

*Uses:* [[§7 Homogeneous Spaces#^def-7-5|Def. §7.5]], [[§7 Homogeneous Spaces#^def-7-6|Def. §7.6]], [[§7 Homogeneous Spaces#^lem-7-3|§7.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-7|Def. §3.7]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^lem-3-15|§3.15]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-13|§3.13]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-1|Def. §5.1]]

> [!theorem] Corollary §7.7: $\pi$ Is a Quotient Map
> $\pi : G \to G/H$ is a quotient map in the sense of Definition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^def-3-8|§3.8]], and consequently a map $g : G/H \to Z$ into a topological space is continuous if and only if $g \circ \pi : G \to Z$ is continuous.
>
> *Lee: Theorem 21.17*

^cor-7-7

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $\pi$ is a continuous open surjection by Proposition [[§7 Homogeneous Spaces#^prop-7-6|§7.6]], hence a quotient map by Proposition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-22|§3.22]]. (It is also one directly from Definition [[§7 Homogeneous Spaces#^def-7-6|§7.6]], which is the defining property.) The second statement is the universal property, Proposition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]].

^pf-7-7

*Uses:* [[§7 Homogeneous Spaces#^prop-7-6|§7.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^prop-3-22|§3.22]], [[§7 Homogeneous Spaces#^def-7-6|Def. §7.6]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]

> [!remark]- Connections
> - In 590: open surjections are quotient maps, [[§12 Quotient Topology#^prop-12-2|590 §12.2]]; the universal property, [[Universal Property of Quotient Maps]].

> [!remark] Remark
> **Openness of $\pi$, for free.** The action of $H$ on $G$ in Proposition [[§7 Homogeneous Spaces#^prop-7-4|§7.4]] is continuous, being the restriction to $H \times G$ of the map $(h,g) \mapsto gh^{-1}$ on $G \times G$, a composite of inversion and multiplication. So by the [[§7 Homogeneous Spaces#^rem-7-3|organizing fact]], Definition [[§7 Homogeneous Spaces#^def-7-6|§7.6]] *is* the orbit-space topology, and Lemma [[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]] — every orbit relation of a continuous action is open — already gives that $\pi$ is an open map. The proof above is that argument written out in the group case, with the translations $L_h$ of Lemma [[§6 Group Actions and Orbit Spaces#^lem-6-2|§6.2]] appearing as right translations $g \mapsto gh$; it is included because the formula $\pi^{-1}(\pi(U)) = UH$ is worth seeing explicitly.

^rem-7-6

> [!theorem] Theorem §7.8: Homogeneous Spaces Are Homeomorphic to Coset Spaces
> Let $G$ act continuously and transitively on a topological space $X$, let $x_0 \in X$, $H = H_{x_0}$, and let $\Phi : G/H \to X$, $\Phi(gH) = g \cdot x_0$.
> 1. $\Phi$ is a continuous bijection.
> 2. If $G/H$ is compact and $X$ is Hausdorff, then $\Phi$ is a homeomorphism.
>
> In particular (2) applies whenever $G$ itself is compact.
>
> *Lee: Theorem 21.18, a smooth version without compactness (see the comparison below)*

^thm-7-8

![[m591-7-2.svg]]
*The triangle $G \to G/H \to X$: the orbit map $g \mapsto g \cdot x_0$ factors as $\Phi \circ \pi$.*

Upstairs is the group, downstairs its coset space, and the triangle commutes: $\Phi \circ \pi$ is the orbit map. The orbit map is continuous for free; part (1) is the universal property pushing that continuity down along $\pi$, and part (2) is the compactness argument upgrading the bottom arrow to a homeomorphism.

> [!proof]+ Proof
> *(Stated in Lecture 4, with a hypothesis missing — the board said “$G$ compact $\Rightarrow$ $G/H \cong X$”, and $X$ must also be Hausdorff; filled in.)*
> (1) Bijectivity is Lemma [[§7 Homogeneous Spaces#^lem-7-5|§7.5]]. The composite $\Phi \circ \pi : G \to X$ is the orbit map $g \mapsto g \cdot x_0$, which is continuous: it is $G \to G \times X \to X$, $g \mapsto (g, x_0) \mapsto g \cdot x_0$, a composite of a map continuous by Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]] with the action. By the universal property of the quotient (Proposition [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]), $\Phi$ is continuous.
>
> (2) By (1), $\Phi$ is a continuous bijection from the compact space $G/H$ onto the Hausdorff space $X$, hence a homeomorphism (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](6)). Spelled out: if $C \subseteq G/H$ is closed, then $C$ is compact by Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](5), so $\Phi(C)$ is compact by (2) of that proposition, hence closed in $X$ by (4); so $\Phi$ is a closed map, and the inverse of a closed continuous bijection is continuous, since $(\Phi^{-1})^{-1}(C) = \Phi(C)$ for every $C$.
>
> For the final sentence of the theorem: if $G$ is compact, then $G/H = \pi(G)$ is compact as the continuous image of a compact space.

^pf-7-8

*Uses:* [[§7 Homogeneous Spaces#^lem-7-5|§7.5]], [[§7 Homogeneous Spaces#^def-7-3|Def. §7.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-10|§3.10]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]], [[§7 Homogeneous Spaces#^cor-7-7|§7.7]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Bijection from Compact to Hausdorff is a Homeomorphism]], [[Continuous Image of a Compact Space is Compact]]

> [!remark]- Connections
> - The same pattern in 590 — a map constant on fibres induces a continuous bijection from the quotient: [[§12 Quotient Topology#^cor-12-4|590 §12.4 (Induced Bijection from Quotient)]].
> - The underlying bijection is the orbit bijection [[§28 Orbit–Stabilizer#^prop-28-2|493 §28.2]].

> [!example] Example §7.4: The Circle as $\mathbb{R}/\mathbb{Z}$
> Let the additive group $\mathbb{R}$ act on $S^1 = \{z \in \mathbb{C} \mid |z| = 1\}$ by
>
> $$
> t \cdot z = e^{2\pi i t} z .
> $$
>
> This is an action ($0 \cdot z = z$ and $s \cdot (t \cdot z) = e^{2\pi i s}e^{2\pi i t}z = (s+t) \cdot z$), it is continuous (the map $(t,z) \mapsto e^{2\pi i t}z$ is continuous on $\mathbb{R} \times S^1$), and it is transitive (every $w \in S^1$ is $e^{2\pi i \theta} = \theta \cdot 1$ for some $\theta$). The isotropy of the base point $1$ is
>
> $$
> H_1 = \{\, t \in \mathbb{R} \mid e^{2\pi i t} = 1 \,\} = \mathbb{Z} .
> $$
>
> The coset space $\mathbb{R}/\mathbb{Z}$ is compact, being the image under $\pi$ of the compact interval $[0,1]$ (every coset $t + \mathbb{Z}$ meets $[0,1]$), and $S^1$ is Hausdorff. So Theorem [[§7 Homogeneous Spaces#^thm-7-8|§7.8]](2) gives a homeomorphism
>
> $$
> \Phi : \mathbb{R}/\mathbb{Z} \xrightarrow{\ \cong\ } S^1, \qquad t + \mathbb{Z} \longmapsto e^{2\pi i t} .
> $$
>
> Here $G = \mathbb{R}$ is *not* compact, so the version of the theorem with “$G$ compact” would not apply. The hypothesis on the quotient is genuinely weaker than the hypothesis on the group, and it is the one that matters: the proof uses compactness of $G/H$ and nothing about $G$.
>
> *Lee: Example 21.14(a)*

^ex-7-4

![[m591-7-3.svg]]
*The triangle for $\mathbb{R}$ acting on $S^1$: $t \mapsto e^{2\pi i t}$ factors through $\mathbb{R}/\mathbb{Z}$ as $\Phi \circ \pi$.*

The same triangle with $G = \mathbb{R}$. The exponential wraps the line around the circle; it is constant exactly on the cosets $t + \mathbb{Z}$, which is why it descends to the quotient, and the induced bottom arrow is the homeomorphism.

> [!remark]- Connections
> - In 590 the circle is the quotient $[0,1]/(0 \sim 1)$ via the same map $e^{2\pi i t}$: [[§12 Quotient Topology#^ex-12-2|590 Ex. §12.2]].

> [!example] Example §7.5: A Continuous Bijection That Is Not a Homeomorphism
> Let $G = \mathbb{R}_{\mathrm{disc}}$, the additive group of real numbers with the discrete topology — a topological group, since every map out of a discrete space is continuous. It acts on $X = \mathbb{R}$, with its usual topology, by translation, $t \cdot x = x + t$. The action is continuous, because $G \times X$ is the disjoint union of the open sets $\{t\} \times X$, on each of which it is a translation. It is transitive, the isotropy group of $0$ is $\{0\}$, and so $G/H = \mathbb{R}_{\mathrm{disc}}$. The map $\Phi : \mathbb{R}_{\mathrm{disc}} \to \mathbb{R}$, $t \mapsto t$, is a continuous bijection but not a homeomorphism: $\{0\}$ is open in $\mathbb{R}_{\mathrm{disc}}$ and not in $\mathbb{R}$. Here $X$ is Hausdorff and $G/H$ is not compact, so Theorem [[§7 Homogeneous Spaces#^thm-7-8|§7.8]](2) does not apply — and its conclusion genuinely fails.
>
> *Lee: no counterpart; a course example*

^ex-7-5

> [!remark]- Connections
> - [[Discrete and indiscrete topologies]]; the same group appears in [[§2 Topological Manifolds#^ex-2-3|§2.3]] and [[§5 Topological Groups and Classical Matrix Groups#^ex-5-1|Discrete Groups, §5.1]].

**Comparison with Lee.** Lee's Theorem 21.18 has no compactness hypothesis: for a Lie group acting smoothly and transitively on a manifold, $\Phi$ is an equivariant *diffeomorphism*. Smoothness does the work that compactness does here — $\Phi$ has constant rank by his equivariant rank theorem (Theorem 7.25), and a bijection of constant rank is a diffeomorphism. His standing assumption that $G$ is a Lie group, in particular second countable, also rules out Example [[§7 Homogeneous Spaces#^ex-7-5|§7.5]], where $G$ is an uncountable discrete group. In the purely topological setting of the course some hypothesis is needed, and “$G/H$ compact, $X$ Hausdorff” is the one used.

**Classroom exchange and its resolution.** On the board the statement read “if $G$ is compact, then $G/H \cong X$ is a homeomorphism,” with no hypothesis on $X$ beyond the continuous transitive action. A student objected that the conclusion cannot hold with no condition on the topology of $X$; Uribe agreed on the spot (“good catch … I think I made a mistake, and I will correct that by email”). The correction arrived as Problem 1 of Assignment 2, which states exactly the theorem above: (1) with no hypotheses, and (2) under “$G/H$ compact and $X$ Hausdorff.” So the board version was off in two ways at once — it was missing Hausdorffness of $X$, and it asked for compactness of the wrong space. Example [[§7 Homogeneous Spaces#^ex-7-4|§7.4]] shows the second repair matters.

> [!definition] Definition §7.7: The Topology of a Homogeneous Space
> Let a topological group $G$ act transitively on a *set* $X$, let $x_0 \in X$, and let $H = H_{x_0}$. The **homogeneous-space topology** on $X$ is the one that makes the bijection $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$, of Lemma [[§7 Homogeneous Spaces#^lem-7-5|§7.5]] a homeomorphism: $V \subseteq X$ is open iff $\Phi^{-1}(V)$ is open in $G/H$.
>
> *Lee: Theorem 21.20*

^def-7-7

> [!remark]- Connections
> - For $\mathrm{Gr}_1(\mathbb{R}^{n+1}) = \mathbb{RP}^n$ this topology agrees with the quotient topology of $S^n/\{\pm 1\}$: [[§8 Differentiable Structures#^prop-8-11|§8.11]].

> [!theorem] Proposition §7.9: Independence of the Base Point
> The homogeneous-space topology does not depend on the choice of $x_0$.
>
> *Lee: Theorem 21.20*

^prop-7-9

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $x_1 = a \cdot x_0$. Then $H_{x_1} = aH_{x_0}a^{-1}$, since $g\,a\cdot x_0 = a\cdot x_0 \iff a^{-1}ga \in H_{x_0}$. Right translation $g \mapsto ga^{-1}$ is a homeomorphism of $G$ carrying each coset $gH_{x_0}$ onto $ga^{-1}(aH_{x_0}a^{-1}) = ga^{-1}H_{x_1}$. So, by the universal property (Corollary [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]), it induces a continuous map $\bar R : G/H_{x_0} \to G/H_{x_1}$, $gH_{x_0} \mapsto ga^{-1}H_{x_1}$, whose inverse is induced in the same way by $g \mapsto ga$. Hence $\bar R$ is a homeomorphism. It intertwines the two bijections, since $\Phi_1(\bar R(gH_{x_0})) = ga^{-1}\cdot x_1 = g \cdot x_0 = \Phi_0(gH_{x_0})$. So $\Phi_1 = \Phi_0 \circ \bar R^{-1}$, and the two transported topologies coincide.

^pf-7-9

*Uses:* [[§7 Homogeneous Spaces#^def-7-2|Def. §7.2]], [[§7 Homogeneous Spaces#^def-7-6|Def. §7.6]], [[§7 Homogeneous Spaces#^def-7-7|Def. §7.7]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-1|Def. §5.1]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^cor-3-19|§3.19]]

> [!remark]- Connections
> - $H_{a \cdot x_0} = aH_{x_0}a^{-1}$ is [[§24 Stabilizers and Fixed Points#^prop-24-2|493 §24.2 (Stabilizers of Points in the Same Orbit Are Conjugate)]].

> [!remark] Remark: Giving a Set a Topology
> Theorem [[§7 Homogeneous Spaces#^thm-7-8|§7.8]] is also used in reverse: when $X$ is merely a *set* on which $G$ acts transitively, the [[§7 Homogeneous Spaces#^def-7-7|definition above]] gives it a topology — “that's a natural way to give a topology to homogeneous spaces.” This is how the Grassmannians below get their topology, and the [[§7 Homogeneous Spaces#^prop-7-9|proposition]] says the result is canonical.

^rem-7-7

> [!theorem] Corollary §7.10: When $G/H$ Is Hausdorff and Second Countable
> Let $G$ be a compact Hausdorff topological group and $H \le G$ a compact subgroup. Then $G/H$ is compact Hausdorff; if moreover $G$ is second countable, so is $G/H$.
>
> *Lee: Theorem 21.17*

^cor-7-10

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Everything is an application of [[§6 Group Actions and Orbit Spaces|§6]] to the continuous action of $H$ on $G$ of Proposition [[§7 Homogeneous Spaces#^prop-7-4|§7.4]], whose orbit space is $G/H$ with its quotient topology. Apply Corollary [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]]: $H$ and $G$ compact, $G$ Hausdorff, so the orbit space $G/H$ is Hausdorff; it is compact as $\pi(G)$. Second countability is Theorem [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|§3.28]], the orbit relation being open by Lemma [[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]].

^pf-7-10

*Uses:* [[§7 Homogeneous Spaces#^prop-7-4|§7.4]], [[§7 Homogeneous Spaces#^rem-7-6|Remark after §7.7]], [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]], [[§6 Group Actions and Orbit Spaces#^lem-6-3|§6.3]], [[§3 New Spaces from Old꞉ Subspaces, Products, and Quotients#^thm-3-28|§3.28]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]

## Real Grassmannians

> [!definition] Definition §7.8: Grassmannian
> For $0 \le k \le n$, the **real Grassmannian** is the set
>
> $$
> \mathrm{Gr}_k(\mathbb{R}^n) = \{\, V \subseteq \mathbb{R}^n \mid V \text{ is a } k\text{-dimensional linear subspace} \,\}.
> $$
>
> For $k = 1$ it is the set of lines through the origin in $\mathbb{R}^n$, the **real projective space**
>
> $$
> \mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^{n-1}.
> $$
>
> *Lee: Example 1.36*

^def-7-8

> [!remark]- Connections
> - The smooth atlas on $\mathbb{RP}^n$: [[§8 Differentiable Structures#^cor-8-10|§8.10 (Real Projective Space)]].

> [!remark] Remark: On the Index
> The board first said $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^n$; a student asked whether it should be $n-1$, and after some back-and-forth (“this drives me absolutely crazy”) the answer settled on $\mathbb{RP}^{n-1}$: each line through $0$ in $\mathbb{R}^n$ meets the unit sphere $S^{n-1}$ in exactly two antipodal points $\pm v$, so $\mathbb{RP}^{n-1} \cong S^{n-1}/\{\pm I\}$, an $(n-1)$-dimensional object. Explicitly, the quotient on the right is the orbit space of the group $\{\pm I\} \cong \mathbb{Z}/2$ acting on $S^{n-1}$ by $v \mapsto \pm v$: a point is an antipodal pair $\{v, -v\}$, $\pi(v) = \{v,-v\}$, a set of pairs is open iff the union of the pairs is open in $S^{n-1}$, and the identification with $\mathrm{Gr}_1(\mathbb{R}^n)$ is $\{v, -v\} \mapsto \mathbb{R} v$, with inverse $\ell \mapsto \ell \cap S^{n-1}$. This orbit space is Hausdorff by Corollary [[§6 Group Actions and Orbit Spaces#^cor-6-4|§6.4]] ($\{\pm I\}$ finite, hence compact), and its topology agrees with the homogeneous-space topology of $\mathrm{Gr}_1(\mathbb{R}^n)$ (see [[§8 Differentiable Structures#^prop-8-11|the note]] after Corollary [[§8 Differentiable Structures#^cor-8-10|§8.10]]). The superscript on $\mathbb{RP}$ records the dimension of the manifold; the superscript on the $\mathbb{R}^n$ it is built from is one larger. (The alternative notation $\mathbb{P}(\mathbb{R}^n)$, treating $\mathbb{P}$ as an operation on the vector space, avoids the off-by-one.)

^rem-7-8

> [!remark]- Connections
> - For $n = 3$ this is the projective plane $S^2/(x \sim -x)$ of 590: [[§28 Fundamental Group of Some Surfaces#^def-28-1|590 Def. §28.1]], [[Projective plane]].

> [!theorem] Proposition §7.11: $\mathrm{O}(n)$ Acts Transitively on $\mathrm{Gr}_k({\mathbb{R}^n})$
> For $g \in \mathrm{O}(n)$ and $V \in \mathrm{Gr}_k(\mathbb{R}^n)$ set $g \cdot V = gV = \{\, gv \mid v \in V \,\}$. This defines an action of $\mathrm{O}(n)$ on $\mathrm{Gr}_k(\mathbb{R}^n)$, and the action is transitive.
>
> *Lee: Example 21.21*

^prop-7-11

> [!proof]+ Proof
> *(Set in Lecture 4 as a “linear algebra exercise”; filled in.)* *Action.* $gV$ is a linear subspace (image of a subspace under a linear map) of dimension $k$ ($g$ is injective), so $gV \in \mathrm{Gr}_k(\mathbb{R}^n)$; $IV = V$; and $g(g'V) = (gg')V$ by associativity.
>
> *Transitive* (“a linear algebra exercise”). Let $V, W \in \mathrm{Gr}_k(\mathbb{R}^n)$. Choose an orthonormal basis $v_1, \ldots, v_k$ of $V$ (Gram–Schmidt applied to any basis of $V$) and extend it to an orthonormal basis $v_1, \ldots, v_n$ of $\mathbb{R}^n$ (apply Gram–Schmidt to a basis of the orthogonal complement $V^\perp$, which has dimension $n - k$). Do the same for $W$: an orthonormal basis $w_1, \ldots, w_n$ of $\mathbb{R}^n$ with $w_1, \ldots, w_k$ spanning $W$. Let $g$ be the linear map with $g v_i = w_i$ for all $i$. Since $g$ carries an orthonormal basis to an orthonormal basis, $(gx) \cdot (gy) = x \cdot y$ for all $x, y$ (expand $x, y$ in the $v_i$), so $g \in \mathrm{O}(n)$; and $gV = g\,\operatorname{span}(v_1, \ldots, v_k) = \operatorname{span}(w_1, \ldots, w_k) = W$.

^pf-7-11

*Uses:* [[§7 Homogeneous Spaces#^def-7-8|Def. §7.8]], [[§6 Group Actions and Orbit Spaces#^def-6-1|Def. §6.1]], [[§7 Homogeneous Spaces#^def-7-1|Def. §7.1]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-6|Def. §5.6]], [[Gram–Schmidt procedure]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|LADR 6.51]], [[Linear map lemma]]

> [!remark]- Connections
> - The case $k = 1$ of the orthonormal-basis argument is [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|493 §30.2]] and [[§6 Group Actions and Orbit Spaces#^ex-6-5|Ex. §6.5]]; orthonormal bases in LADR: [[§20 Orthonormal Bases#^ladr-6-36|LADR 6.36]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]].

> [!theorem] Proposition §7.12: Isotropy of the Standard $k$-Plane
> Let $V_0 = \operatorname{span}(e_1, \ldots, e_k) \in \mathrm{Gr}_k(\mathbb{R}^n)$ be the base point. Then
>
> $$
> H_{V_0} = \left\{ \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \;\middle|\; A \in \mathrm{O}(k),\ B \in \mathrm{O}(n-k) \right\} \;\cong\; \mathrm{O}(k) \times \mathrm{O}(n-k),
> $$
>
> block matrices with respect to the decomposition $\mathbb{R}^n = V_0 \oplus V_0^\perp$, $V_0^\perp = \operatorname{span}(e_{k+1}, \ldots, e_n)$.
>
> *Lee: Example 21.21*

^prop-7-12

> [!proof]+ Proof
> *(Stated in Lecture 4, with the block picture of $\mathrm{O}(k) \times \mathrm{O}(n-k)$; filled in.)* Write $g \in \mathrm{O}(n)$ in blocks $g = \begin{pmatrix} A & C \\ D & B \end{pmatrix}$ with $A$ of size $k \times k$. Then $gV_0 = V_0$ iff $g e_j \in V_0$ for $j \le k$ iff the first $k$ columns have zero lower part, i.e. $D = 0$ (then $g$ maps $V_0$ into $V_0$, and injectivity plus $\dim$ gives $gV_0 = V_0$). Now orthogonal maps preserve orthogonal complements: if $gV_0 = V_0$ and $u \in V_0^\perp$, then for all $v \in V_0$, $(gu) \cdot v = (gu) \cdot (g g^{-1} v) = u \cdot g^{-1}v = 0$ since $g^{-1}v \in V_0$; so $g V_0^\perp \subseteq V_0^\perp$, i.e. $C = 0$. With $C = D = 0$, the condition $g^T g = I$ reads $A^T A = I_k$ and $B^T B = I_{n-k}$, i.e. $A \in \mathrm{O}(k)$, $B \in \mathrm{O}(n-k)$. Conversely every such block-diagonal matrix is orthogonal and fixes $V_0$. The map $(A, B) \mapsto \mathrm{diag}(A, B)$ is a group isomorphism from the product group and a homeomorphism (it is a linear embedding of coordinates).

^pf-7-12

*Uses:* [[§7 Homogeneous Spaces#^def-7-2|Def. §7.2]], [[§7 Homogeneous Spaces#^prop-7-11|§7.11]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-6|Def. §5.6]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-7|§5.7]]

> [!remark]- Connections
> - The case $k = 1$ (up to reordering) is $\operatorname{Stab}(e_1) \cong \mathrm{O}_2$ in [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|493 §30.2]](2).

**Transcription note.** Page 13 of the handwritten notes writes the base point as the span of $e_1$ through $e_n$. A $k$-plane is spanned by $k$ vectors, so the base point is the span of $e_1$ through $e_k$, as above.

> [!theorem] Corollary §7.13: Grassmannians as Homogeneous Spaces
> As sets, $\mathrm{Gr}_k(\mathbb{R}^n) \cong \mathrm{O}(n)/\big(\mathrm{O}(k) \times \mathrm{O}(n-k)\big)$ via $g H_{V_0} \mapsto g V_0$. Transporting the quotient topology across this bijection makes $\mathrm{Gr}_k(\mathbb{R}^n)$ a compact, Hausdorff, second countable space.
>
> *Lee: Examples 1.36 and 21.21*

^cor-7-13

> [!proof]+ Proof
> The bijection is Lemma [[§7 Homogeneous Spaces#^lem-7-5|§7.5]] with Propositions [[§7 Homogeneous Spaces#^prop-7-11|§7.11]] and [[§7 Homogeneous Spaces#^prop-7-12|§7.12]]. Explicitly, with $H = H_{V_0}$: a point of $\mathrm{O}(n)/H$ is a coset $gH$, and since every $h \in H$ preserves $V_0 = \operatorname{span}(e_1, \ldots, e_k)$, all elements of $gH$ have first $k$ columns spanning the same $k$-plane $gV_0$; conversely $g' V_0 = g V_0$ implies $g^{-1}g' \in H$, so
>
> $$
> gH = \{\, g' \in \mathrm{O}(n) \mid \operatorname{span}(\text{first } k \text{ columns of } g') = g V_0 \,\}.
> $$
>
> The identification $\Phi(gH) = gV_0$ sends a coset to the span of the first $k$ columns of any of its members; its inverse sends a $k$-plane $V$ to the set of orthogonal matrices whose first $k$ columns span $V$ (nonempty by transitivity). A set $W$ of $k$-planes is declared open iff the set of orthogonal matrices whose first $k$ columns span some member of $W$ is open in $\mathrm{O}(n)$. For the topology, apply Corollary [[§7 Homogeneous Spaces#^cor-7-10|§7.10]]: $\mathrm{O}(n)$ is compact, being closed (the preimage of $\{I\}$ under the continuous map $g \mapsto g^T g$) and bounded (each column is a unit vector, so every entry satisfies $|g_{ij}| \le 1$) in $\mathbb{R}^{n^2}$; it is Hausdorff and second countable as a subspace of $\mathbb{R}^{n^2}$; and the subgroup $\mathrm{O}(k) \times \mathrm{O}(n-k)$ is compact by the same argument.

^pf-7-13

*Uses:* [[§7 Homogeneous Spaces#^lem-7-5|§7.5]], [[§7 Homogeneous Spaces#^prop-7-11|§7.11]], [[§7 Homogeneous Spaces#^prop-7-12|§7.12]], [[§7 Homogeneous Spaces#^lem-7-3|§7.3]], [[§7 Homogeneous Spaces#^def-7-7|Def. §7.7]], [[§7 Homogeneous Spaces#^cor-7-10|§7.10]], [[§5 Topological Groups and Classical Matrix Groups#^def-5-2|Def. §5.2]], [[§5 Topological Groups and Classical Matrix Groups#^prop-5-7|§5.7]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[Heine–Borel Theorem]]

> [!remark]- Connections
> - For $k = 1$ the transported topology agrees with the quotient topology of $\mathbb{RP}^{n-1}$: [[§8 Differentiable Structures#^prop-8-11|§8.11]]; $\mathrm{O}(n)$ becomes a smooth manifold in [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Ex. §10.1]].

> [!remark] Remark: Dimension Count and What Is Still Missing
> Heuristically, $\dim G/H = \dim G - \dim H$, which with $\dim \mathrm{O}(m) = \tfrac{m(m-1)}{2}$ ([[§5 Topological Groups and Classical Matrix Groups#The Classical Groups Are Topological Manifolds|§5, The Classical Groups Are Topological Manifolds]]) gives
>
> $$
> \dim \mathrm{Gr}_k(\mathbb{R}^n) = \frac{n(n-1)}{2} - \frac{k(k-1)}{2} - \frac{(n-k)(n-k-1)}{2} = k(n-k).
> $$
>
> This is correct, but nothing proved so far shows $\mathrm{Gr}_k(\mathbb{R}^n)$ is locally Euclidean at all: the corollary only supplies the two point-set conditions. Charts on Grassmannians (graphs of linear maps $V_0 \to V_0^\perp$) are Lee Example 1.36, and will make $\mathrm{Gr}_k(\mathbb{R}^n)$ a $k(n-k)$-manifold. For $k = 1$ this is $\mathbb{RP}^{n-1}$, of dimension $n - 1$, consistent with the [[§7 Homogeneous Spaces#^rem-7-8|index remark]] above. The picture Uribe drew is $n = 3$, $k = 2$: $V_0$ is the $xy$-plane, $\mathrm{Gr}_2(\mathbb{R}^3)$ is the space of planes through the origin in $\mathbb{R}^3$, and $k(n-k) = 2$.

^rem-7-9

![[m591-7-4.svg]]
*Uribe's picture for $n = 3$, $k = 2$: a point of $\mathrm{Gr}_2(\mathbb{R}^3)$ is a whole plane through the origin. The base point $V_0 = \operatorname{span}(e_1, e_2)$ (blue) is carried by an orthogonal $g$ to another plane $V = gV_0$ (red); two distinct planes through $0$ always share a line (dashed). The isotropy group $\mathrm{O}(2) \times \mathrm{O}(1)$ of [[§7 Homogeneous Spaces#^prop-7-12|Proposition §7.12]] consists of the $g$ that move $V_0$ onto itself: an orthogonal map of the plane, together with $e_3 \mapsto \pm e_3$ on the normal line. A plane is pinned down by its unit normal up to sign ($\pm e_3$ for $V_0$, $\pm g e_3$ for $V$), so it takes two parameters to choose one — the count $k(n-k) = 2$.*

> [!remark]- Connections
> - $\dim \mathrm{O}(n) = \tfrac{n(n-1)}{2}$ is proved in [[§10 Vector Spaces and Matrix Groups#^ex-10-1|Ex. §10.1]]; the same subtraction of dimensions for $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ is [[§11 Tangent Spaces I꞉ The Geometric Picture#^rem-11-9|Dimension Checks through Homogeneous Spaces]].
