---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 13
tags: [differentiable-manifolds, math591]
---
← [[§12 Group Actions and Orbit Spaces]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§14 The Topology of G∕H and Real Grassmannians]] →

*Thread: quotients — A transitive action identifies a space with a coset space $G/H$, here as a set; its topology and the Grassmannians follow in [[§14 The Topology of G∕H and Real Grassmannians|§14]].*

*Reference: Lee Ch. 21, the section on homogeneous spaces; Lee Example 1.36 (Grassmannians). Logistics: a substitute lectures on Friday Sep 11; smooth structures are scheduled to begin then.*

> [!remark] Remark: Why This Section
> *Homogeneous spaces* are spaces on which a group acts transitively. They are identified with coset spaces $G/H$, which are themselves orbit spaces (of $H$ acting on $G$), so everything in [[§12 Group Actions and Orbit Spaces|§12]] applies. This is how spheres, projective spaces, and Grassmannians acquire their topology in one stroke: “that's a natural way to give a topology to homogeneous spaces.”

^rem-13-1

## Transitive Actions and Isotropy

> [!definition] Definition §13.1: Transitive Action and Homogeneous Space
> An action of $G$ on $X$ is **transitive** if there is only one orbit; equivalently,
>
> $$
> \forall\, x, y \in X\ \ \exists\, g \in G \text{ such that } y = g \cdot x .
> $$
>
> A topological space $X$ is **homogeneous** for the topological group $G$ if $G$ acts continuously and transitively on $X$.
>
> *Lee: Ch. 7 and Example 21.15*

^def-13-1

> [!remark]- Connections
> - Transitivity is defined in [[§27 Orbits#^def-27-1|493 Def. §27.1]]; the model transitive action is $G$ on $G/H$, [[§31 G Acting on Coset Spaces#^prop-31-1|493 §31.1]].

> [!remark] Remark
> For a transitive action the orbit space $X/G$ is a single point, “which is not that interesting.” The interesting quotient is a different one: $X$ itself will be exhibited as a quotient $G/H$ of the *group*, by the action of a subgroup $H$ on $G$.

^rem-13-2

> [!definition] Definition §13.2: Isotropy Subgroup
> For any action of $G$ on $X$ and any $x_0 \in X$, the **isotropy subgroup** (or **stabilizer**) of $x_0$ is
>
> $$
> H_{x_0} = \{\, g \in G \mid g \cdot x_0 = x_0 \,\},
> $$
>
> the set of group elements that do not move $x_0$.
>
> *Lee: Ch. 7, p. 162*

^def-13-2

> [!remark]- Connections
> - Home: [[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1 (Stabilizer)]], written $\operatorname{Stab}(x_0)$ there.
> - Used in Quantum Field Theory: the little group of a particle, the isotropy subgroup of its standard momentum in the Lorentz group — [[§C3.5★ Particle States and the Little Group#^def-c3-5-1|QFT Def. §C3.5.1]].

> [!theorem] Proposition §13.1: The Isotropy Is a Subgroup
> $H_{x_0}$ is a subgroup of $G$.

^prop-13-1

> [!proof]+ Proof
> $e \in H_{x_0}$ since $e \cdot x_0 = x_0$. If $g, g' \in H_{x_0}$ then $(gg') \cdot x_0 = g \cdot (g' \cdot x_0) = g \cdot x_0 = x_0$. If $g \in H_{x_0}$ then $g^{-1} \cdot x_0 = g^{-1} \cdot (g \cdot x_0) = (g^{-1}g) \cdot x_0 = x_0$.

^pf-13-1

*Uses:* [[§13 Homogeneous Spaces#^def-13-2|Def. §13.2]], [[§12 Group Actions and Orbit Spaces#^def-12-1|Def. §12.1]], [[§4 Subgroups#^def-4-1|493 Def. §4.1]]

> [!remark]- Connections
> - Home of this result: [[§26 Stabilizers and Fixed Points#^prop-26-1|493 §26.1 (The Stabilizer Is a Subgroup)]].

> [!definition] Definition §13.3: Orbit Map
> Let a topological group $G$ act continuously on $X$, and let $x_0 \in X$. The **orbit map** of $x_0$ is
>
> $$
> \theta_{x_0} : G \to X, \qquad \theta_{x_0}(g) = g \cdot x_0 .
> $$
>
> It is continuous, being the action composed with $g \mapsto (g, x_0)$, and its image is the orbit of $x_0$.
>
> *Lee: Proposition 7.26*

^def-13-3

> [!theorem] Theorem §13.2: Isotropy Subgroups Are Closed
> Let $G$ be a topological group acting continuously on a topological space $X$ in which points are closed (for instance, $X$ Hausdorff). Then for every $x_0 \in X$ the isotropy subgroup $H_{x_0}$ is a *closed* subgroup of $G$.
>
> *Lee: proof of Theorem 21.18 (“closed by continuity)*

^thm-13-2

> [!proof]+ Exercise
> *(Claimed in Lecture 4 — “this is a closed subgroup”; filled in.)* Consider the orbit map $\theta_{x_0} : G \to X$, $\theta_{x_0}(g) = g \cdot x_0$, of Definition [[§13 Homogeneous Spaces#^def-13-3|§13.3]], and identify $H_{x_0}$ as a preimage under it. Two things are to be checked: that $\theta_{x_0}$ is continuous, and that the relevant subset of $X$ is closed. Uribe stated the result and said the closedness “may be the next assignment”; it was not proved in lecture, and the argument is left here.

^pf-13-2

*Uses:* [[§13 Homogeneous Spaces#^def-13-3|Def. §13.3]]

> [!remark]- Connections
> - “Points are closed” is the $T_1$ axiom, [[§19 Separation Axioms#^def-19-1|590 Def. §19.1]]; Hausdorff implies it by [[§8 Hausdorff Spaces#^thm-8-1|590 §8.1]].

**On the hypothesis.** The board stated the theorem with no condition on $X$, and in that form it is false, as the next example shows. What fails there is precisely that points of $X$ are not closed. Requiring $X$ to be $T_1$ — in particular Hausdorff, which is the case for every manifold — repairs the statement, and costs nothing in the applications: $\mathrm{O}(n)$ acting on $\mathrm{Gr}_k(\mathbb{R}^n)$, $\mathrm{SO}(3)$ on $S^2$, and every other action met here has Hausdorff target.

> [!example] Example §13.1: An Isotropy Group That Is Not Closed
> Let $G = \mathbb{R}$ act on $X = \mathbb{R}/\mathbb{Q}$, with the quotient topology, by $t \cdot [x] = [x+t]$. The action is continuous, but the isotropy group $H_{[0]} = \mathbb{Q}$ is not closed in $\mathbb{R}$. So Theorem [[§13 Homogeneous Spaces#^thm-13-2|§13.2]] fails without its hypothesis on $X$.

^ex-13-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* The action is well defined, since $x - x' \in \mathbb{Q}$ implies $(x+t) - (x'+t) \in \mathbb{Q}$. Every nonempty open saturated subset of $\mathbb{R}$ contains an interval and is invariant under adding rationals; since $\mathbb{Q}$ is dense, the translates of an interval by rationals cover $\mathbb{R}$, so the set is all of $\mathbb{R}$. Hence $X$ carries the indiscrete topology, every map into $X$ is continuous, and in particular so is the action. Finally
>
> $$
> H_{[0]} = \{\, t \in \mathbb{R} \mid [t] = [0] \,\} = \mathbb{Q},
> $$
>
> which is dense in $\mathbb{R}$ and not closed.

^pf-ex-13-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§4 Quotient Spaces and Open Maps#^prop-4-4|§4.4]], [[§12 Group Actions and Orbit Spaces#^def-12-2|Def. §12.2]], [[§13 Homogeneous Spaces#^def-13-2|Def. §13.2]]

> [!remark]- Connections
> - $X$ is indiscrete, the standard non-$T_1$ space: [[Discrete and indiscrete topologies]].

The classical groups through the course: defined in [[§10 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§15 The Classical Groups|The Classical Groups]]; topological manifolds as level sets in [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§12 Group Actions and Orbit Spaces#^ex-12-4|the rotations of the plane]] and [[§12 Group Actions and Orbit Spaces#^ex-12-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§13 Homogeneous Spaces#^ex-13-2|the isotropy of the north pole]] and [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|the orthogonal group]] and [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|the unitary group]]; their tangent spaces at the identity in [[§23 The Geometric Tangent Space#^thm-23-5|The Classical Groups]], with [[§23 The Geometric Tangent Space#^ex-23-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§38 SU(2) → SO(3)꞉ The Double Cover#^thm-38-10|The Double Cover]].

> [!example] Example §13.2: Isotropy of the North Pole under $\mathrm{SO}(3)$
> Let $\mathrm{SO}(3)$ act on $S^2 = \{x \in \mathbb{R}^3 \mid |x| = 1\}$ by rotations (matrix multiplication; it preserves the sphere since orthogonal matrices preserve norms). For $x_0 = (0,0,1)$, the answer from the floor: the isotropy consists of the rotations about the $z$-axis. In matrices, $g \cdot e_3 = e_3$ says the third column of $g$ is $e_3$; orthogonality then forces the third row to be $e_3^T$ as well (the columns are orthonormal, so the first two columns are orthogonal to $e_3$, i.e. have zero third entry), and the remaining $2 \times 2$ block is orthogonal with determinant $1$:
>
> $$
> H_{x_0} = \left\{ \begin{pmatrix} A & 0 \\ 0 & 1 \end{pmatrix} \;\middle|\; A \in \mathrm{SO}(2) \right\} \;\cong\; \mathrm{SO}(2) \;\cong\; S^1 .
> $$

^ex-13-2

> [!remark]- Connections
> - The same column-then-row argument for $\operatorname{Stab}(e_1)$ in $\mathrm{O}_3$: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|493 §32.2]](2), [[§32 Linear Groups, the Cube, S₃ and A₄#^rem-32-1|493, GL₃ versus O₃]].

## The Coset Space $G/H$

> [!remark] Remark: The Organizing Fact
> Everything in this section and the next is a special case of [[§12 Group Actions and Orbit Spaces|§12]]. The coset space $G/H$ is not merely *like* an orbit space: it *is* one, for a suitable action of $H$ on $G$ (Proposition [[§13 Homogeneous Spaces#^prop-13-4|§13.4]]), with the same underlying set and the same projection map — so the quotient topology of [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|Def. §14.1]] and the orbit-space topology of Definition [[§12 Group Actions and Orbit Spaces#^def-12-5|§12.5]] are equal by construction, not merely homeomorphic. Consequently every result of [[§12 Group Actions and Orbit Spaces|§12]] applies to $G/H$ with no further work, and three facts below are obtained that way: $\pi$ is an open map (Lemma [[§12 Group Actions and Orbit Spaces#^lem-12-3|§12.3]]), $G/H$ is Hausdorff under a compactness hypothesis (Corollary [[§12 Group Actions and Orbit Spaces#^cor-12-4|§12.4]]), and it is second countable (Theorem [[§6 Open Quotients#^thm-6-3|§6.3]]).

^rem-13-3

> [!definition] Definition §13.4: Left Cosets and the Coset Space
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
> (This is the algebraic quotient from [[§28 Left and Right Cosets#^def-28-2|MATH 493]]. Note that $G/H$ is a *group* only when $H$ is normal, which is not assumed here; for us it is only a set, and shortly a space.)
>
> *Lee: proof of Theorem 21.17*

^def-13-4

> [!remark]- Connections
> - Home: [[§28 Left and Right Cosets#^def-28-2|493 Def. §28.2 (Left and Right Cosets)]]; the group case (normal $H$) is [[§40 Quotient Groups|493 §40]], and in 590 [[§21 Algebra Prerequisites꞉ Groups#^def-21-new3|590 Def. §21.13]].

> [!theorem] Lemma §13.3: When Two Cosets Coincide
> $gH = g'H \iff g^{-1}g' \in H$. Consequently the left cosets partition $G$.
>
> *Lee: proof of Theorem 21.17*

^lem-13-3

> [!proof]+ Proof
> *(Used in Lecture 4 as “$gH = g'H \iff g^{-1}g' \in H$”; filled in.)* ($\Rightarrow$) $g' = g'e \in g'H = gH$, so $g' = gh$ for some $h \in H$, i.e. $g^{-1}g' = h \in H$. ($\Leftarrow$) If $g^{-1}g' = h \in H$, then $g' = gh$, so $g'H = ghH = gH$ (as $hH = H$ for $h \in H$, $H$ being a subgroup). For the partition: $g \in gH$, and if $gH \cap g'H \ni a$, then $aH = gH$ and $aH = g'H$ by the first part, so $gH = g'H$.

^pf-13-3

*Uses:* [[§13 Homogeneous Spaces#^def-13-4|Def. §13.4]], [[§4 Subgroups#^def-4-1|493 Def. §4.1]]

> [!remark]- Connections
> - Home of this result: [[§28 Left and Right Cosets#^prop-28-2|493 §28.2 (Cosets Are the Equivalence Classes)]]; hub [[Cosets Partition a Group]].

> [!definition] Definition §13.5: The Canonical Projection
> The **canonical projection** associated with $H \le G$ is the map
>
> $$
> \pi : G \longrightarrow G/H, \qquad \pi(g) = gH,
> $$
>
> sending a group element to the coset containing it. It is surjective by construction, and by Lemma [[§13 Homogeneous Spaces#^lem-13-3|§13.3]] its fibres are exactly the cosets: $\pi^{-1}(gH) = gH$.
>
> *Lee: Theorem 21.17*

^def-13-5

> [!remark] Remark
> A point of $G/H$ is a *subset* of $G$, and $\pi$ is the map that forgets which element of that subset one started from. The two roles of the symbol $gH$ — a subset of $G$, and a single point of $G/H$ — are the usual source of confusion with quotients ([[§4 Quotient Spaces and Open Maps|§4]]); the identity $\pi^{-1}(gH) = gH$ is that ambiguity made harmless, the left side reading $gH$ as a point and the right side as a set.

^rem-13-4

> [!theorem] Proposition §13.4: $G/H$ Is an Orbit Space
> Let $H \le G$. The formula
>
> $$
> H \times G \longrightarrow G, \qquad (h, g) \longmapsto g h^{-1}
> $$
>
> is an action of $H$ on $G$, and its orbits are exactly the left cosets: $\mathcal{O}_g = gH$. Hence $G/H$ (the set of left cosets) is the orbit space of this action.
>
> *Lee: proof of Theorem 21.17 ($H$ acting on $G$ by right translation)*

^prop-13-4

> [!proof]+ Proof
> *(Lecture 4 checked the action axiom, $(hh')\cdot g = h \cdot (h' \cdot g)$, on the board; the rest is filled in.)* *Action.* $e \cdot g = g e^{-1} = g$. For $h, h' \in H$: $(hh') \cdot g = g (hh')^{-1} = g\, h'^{-1} h^{-1} = (g h'^{-1}) h^{-1} = h \cdot (h' \cdot g)$. (The inverse is what makes the order of the factors come out right: multiplying on the right by $h$ itself would give $g h' h$, which is $(h'h) \cdot g$, the wrong order.) *Orbits.* $\mathcal{O}_g = \{\, g h^{-1} \mid h \in H \,\} = \{\, g h \mid h \in H \,\} = gH$, since $h \mapsto h^{-1}$ is a bijection of $H$.

^pf-13-4

*Uses:* [[§12 Group Actions and Orbit Spaces#^def-12-1|Def. §12.1]], [[§12 Group Actions and Orbit Spaces#^def-12-3|Def. §12.3]], [[§12 Group Actions and Orbit Spaces#^def-12-5|Def. §12.5]], [[§13 Homogeneous Spaces#^def-13-4|Def. §13.4]]

> [!remark]- Connections
> - In 493 the same orbits come from the *right* action $g \star h = gh$: [[§28 Left and Right Cosets#^prop-28-1|493 §28.1 (Cosets Are Orbits)]]; converting it to a left action by inverting is [[§25 Actions#^prop-25-1|493 §25.1 (A Left Action Gives a Right Action)]].

> [!remark] Remark
> The inverse in the formula is not cosmetic. The first thing one writes, $(h,g) \mapsto hg$, is also an action, but its orbits are the *right* cosets $Hg$, giving the other quotient $H \backslash G$. To produce *left* cosets from a *left* action of $H$ one must multiply on the right and invert, and that is exactly what makes the second axiom come out in the correct order, as the proof shows. For non-abelian $H$ the naive formula $(h,g) \mapsto gh$ fails the axiom outright.
>
> Proposition [[§13 Homogeneous Spaces#^prop-13-4|§13.4]] is a statement about sets; the topological half is Definition [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|§14.1]] together with the observation that the two projections $G \to G/H$ — the canonical one of Definition [[§13 Homogeneous Spaces#^def-13-5|§13.5]] and the orbit projection of Definition [[§12 Group Actions and Orbit Spaces#^def-12-5|§12.5]] — are the same function, so the two quotient topologies they induce are the same topology.

^rem-13-5

> [!theorem] Lemma §13.5: Homogeneous Spaces Are Coset Spaces
> Suppose $G$ acts transitively on $X$, fix a *base point* $x_0 \in X$, and let $H = H_{x_0}$. Then
>
> $$
> \Phi : G/H \longrightarrow X, \qquad \Phi(gH) = g \cdot x_0
> $$
>
> is a well-defined bijection.
>
> *Lee: proof of Theorem 21.18*

^lem-13-5

> [!proof]+ Proof
> *(Lecture 4 checked well-definedness — translate “the so-called base point” — on the board; injectivity and surjectivity are filled in.)* *Well defined.* If $gH = g'H$ then $g' = gh$ with $h \in H$ (Lemma [[§13 Homogeneous Spaces#^lem-13-3|§13.3]]), and
>
> $$
> g' \cdot x_0 = (gh) \cdot x_0 = g \cdot (h \cdot x_0) = g \cdot x_0,
> $$
>
> since $h$ fixes $x_0$. *Injective.* If $g \cdot x_0 = g' \cdot x_0$, apply $L_{g^{-1}}$: $x_0 = g^{-1} \cdot (g' \cdot x_0) = (g^{-1}g') \cdot x_0$, so $g^{-1}g' \in H$ and $gH = g'H$ by Lemma [[§13 Homogeneous Spaces#^lem-13-3|§13.3]]. *Surjective.* Given $y \in X$, transitivity gives $g$ with $y = g \cdot x_0 = \Phi(gH)$.

^pf-13-5

*Uses:* [[§13 Homogeneous Spaces#^lem-13-3|§13.3]], [[§13 Homogeneous Spaces#^def-13-1|Def. §13.1]], [[§13 Homogeneous Spaces#^def-13-2|Def. §13.2]], [[§12 Group Actions and Orbit Spaces#^def-12-1|Def. §12.1]], [[§12 Group Actions and Orbit Spaces#^lem-12-2|§12.2]]

> [!remark]- Connections
> - Home of this bijection: [[§30 Orbit–Stabilizer#^prop-30-2|493 §30.2 (The Orbit Bijection)]], same proof, for any orbit; hub [[Orbit–Stabilizer Theorem]].
> - Conversely every $G/H$ carries a transitive action with isotropy $H$ at $eH$: [[§31 G Acting on Coset Spaces#^prop-31-1|493 §31.1]].
> - Used in Quantum Field Theory: the orbit of a particle's momentum as a coset space of the Lorentz group, the mass hyperboloid $SO^+(1,3)/SO(3)$ as the sphere is $SO(3)/SO(2)$ — [[§C3.5★ Particle States and the Little Group#^rem-c3-5-1|QFT Remark: What the definition fixes, and what it leaves free]].

> [!example] Example §13.3: The Sphere as a Homogeneous Space
> $\mathrm{SO}(3)$ acts transitively on $S^2$: the orbit of $e_3$ is the whole sphere (the argument of Example [[§12 Group Actions and Orbit Spaces#^ex-12-5|§12.5]] with $r = 1$). By Example [[§13 Homogeneous Spaces#^ex-13-2|§13.2]] the isotropy of $e_3$ is the copy $H$ of $\mathrm{SO}(2)$ in the upper-left block. Hence, as sets (and, by the [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|theorem below]], as spaces),
>
> $$
> S^2 \;\cong\; \mathrm{SO}(3)/\mathrm{SO}(2).
> $$
>
> *Explicitly.* A point of $\mathrm{SO}(3)/H$ is a coset $gH = \{\, gh \mid h \in H \,\}$. Since $h e_3 = e_3$ for $h \in H$, every element of $gH$ has the same third column $g e_3$; conversely, if $g' e_3 = g e_3$ then $g^{-1} g' \in H$, so $g' \in gH$ (Lemma [[§13 Homogeneous Spaces#^lem-13-3|§13.3]]). Thus
>
> $$
> gH = \{\, \text{rotations whose third column is } g e_3 \,\},
> $$
>
> and the cosets are indexed by unit vectors. The identification $\Phi(gH) = g \cdot e_3 = g e_3$ reads off that third column; its inverse sends a unit vector $v \in S^2$ to the set of all rotations having $v$ as third column (nonempty, since some rotation carries $e_3$ to $v$). A set of unit vectors $W \subseteq S^2$ is open in the quotient topology iff the set of all rotations whose third column lies in $W$ is open in $\mathrm{SO}(3)$; Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|§14.3]] says this agrees with the usual topology of $S^2 \subseteq \mathbb{R}^3$.
>
> *Lee: Examples 21.15(a) and 21.19(a)*

^ex-13-3

> [!remark]- Connections
> - The $\mathrm{O}_3$ version of orbit and stabilizer: [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|493 §32.2]].
> - Used for dimension counts in [[§23 The Geometric Tangent Space#^rem-23-9|Dimension Checks through Homogeneous Spaces]].

**Transcription note.** Page 12 of the handwritten notes writes “$X = \mathrm{SO}(3)$ acting on $S^2$”; the group is $G = \mathrm{SO}(3)$ and the space is $X = S^2$.

![[m591-7-1.svg]]
*The north pole $N$, its isotropy group $H \cong \mathrm{SO}(2)$ of rotations about the vertical axis, and a rotation $g$ carrying $N$ to $g \cdot N$.*

The picture behind Example [[§13 Homogeneous Spaces#^ex-13-3|§13.3]]. The rotations about the vertical axis fix the north pole $N$; they form the isotropy group $H \cong \mathrm{SO}(2)$. A rotation $g$ carries $N$ to $g \cdot N$, and the rotations carrying $N$ to that same point are exactly the products $gh$ with $h \in H$: the fibre of the orbit map $\theta_N$ over $g \cdot N$ is the coset $gH$. Collapsing each fibre to a point is the passage from $\mathrm{SO}(3)$ to $\mathrm{SO}(3)/\mathrm{SO}(2)$, which is why the coset space is the sphere (Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|§14.3]]).
