---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 27
tags: [group-theory, math493]
---
← [[§26 Stabilizers and Fixed Points]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§28 Left and Right Cosets]] →

*Reference: Pinter Ch. 13, Ex. J.*

> [!definition] Definition §27.1: Orbit; Orbit Space
> Let $G$ [[§25 Actions#^def-25-1|act]] on $X$. For $x \in X$, the **orbit** of $x$ is
>
> $$
> Gx := \{ g \star x : g \in G \} \subseteq X,
> $$
>
> the set of points reachable from $x$. The set of all orbits is written $G \backslash X$ (for a right action, $X/G$). The action is **transitive** if there is only one orbit, i.e. $Gx = X$ for some (equivalently every) $x$.
>
> *Source: WS 4*

^def-27-1

> [!remark]- Connections
> - Orbit size is the index of the stabilizer: [[§30 Orbit–Stabilizer#^thm-30-3|Orbit–Stabilizer]]; cosets are orbits: [[§28 Left and Right Cosets#^prop-28-1|Cosets Are Orbits]].
> - The orbit-space notation is restated from lecture in [[§27 Orbits#^def-27-2|Orbit Space Notation, Def. §27.2]].
> - With topologies: the orbit space X/G with the quotient topology, [[§12 Group Actions and Orbit Spaces#^def-12-5|591 Def. §12.5]] (orbits as in [[§12 Group Actions and Orbit Spaces#^def-12-3|591 Def. §12.3]]; e.g. complex projective space as an orbit space, [[§12 Group Actions and Orbit Spaces#^ex-12-3|591 Ex. §12.3]]); a continuous transitive action makes X a homogeneous space, [[§13 Homogeneous Spaces#^def-13-1|591 Def. §13.1]].

> [!theorem] Proposition §27.1: Orbits Partition $X$
> Let $G$ act on $X$ and $x, y \in X$. Then either $Gx = Gy$ or $Gx \cap Gy = \varnothing$. Hence $X$ is the disjoint union of the distinct orbits.
>
> *Source: WS 4.6*

^prop-27-1

> [!proof]+ Proof
> Suppose $z \in Gx \cap Gy$, say $z = g \star x = h \star y$ with $g, h \in G$. Then $x = g^{-1} \star (h \star y) = (g^{-1}h) \star y \in Gy$, so for any $a \in G$, $a \star x = (ag^{-1}h) \star y \in Gy$; thus $Gx \subseteq Gy$. Symmetrically $Gy \subseteq Gx$. So a nonempty intersection forces equality. Every $x$ lies in its own orbit ($x = e \star x$), so the orbits cover $X$.

^pf-27-1

*Uses:* [[§27 Orbits#^def-27-1|Def. §27.1]], [[§25 Actions#^def-25-1|Def. §25.1]], [[§24 Equivalence Relations and Partitions#^def-24-3|Def. §24.3]]

![[m493-25-1.svg]]
*The proof: if the orbits of $x$ and $y$ share a point $z$, then $x$ is reached from $y$ by going to $z$ with $h$ and back with $g^{-1}$ (red), so $x = (g^{-1}h) \star y \in Gy$, and then all of $Gx$ lies in $Gy$.*

> [!theorem] Proposition §27.2: The Orbit Relation
> The relation “$x \sim y$ iff $y = g \star x$ for some $g \in G$” is an [[§24 Equivalence Relations and Partitions#^def-24-1|equivalence relation]] on $X$, and its equivalence classes are the orbits.

^prop-27-2

> [!proof]+ Proof
> Reflexive: $x = e \star x$. Symmetric: $y = g \star x$ gives $x = g^{-1} \star y$. Transitive: $y = g \star x$ and $z = h \star y$ give $z = (hg) \star x$. The class of $x$ is $\{g \star x : g \in G\} = Gx$. (This is a second proof that the orbits partition $X$, via [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]].)

^pf-27-2

*Uses:* [[§24 Equivalence Relations and Partitions#^def-24-1|Def. §24.1]], [[§24 Equivalence Relations and Partitions#^def-24-2|Def. §24.2]], [[§24 Equivalence Relations and Partitions#^prop-24-1|§24.1]], [[§25 Actions#^def-25-1|Def. §25.1]], [[§27 Orbits#^def-27-1|Def. §27.1]]

> [!remark]- Connections
> - The orbit space is the [[§22 Partitions and Equivalence Relations#^def-22-6|quotient set]] (250 Def. §22.6) of this relation; with a topology it is a quotient space in MATH 590: [[§13 Quotient Topology#^def-13-3|Quotient Space]] (590 Def. §13.3).
> - Same relation in 591, [[§12 Group Actions and Orbit Spaces#^def-12-4|591 Def. §12.4]] and [[§12 Group Actions and Orbit Spaces#^prop-12-1|591 Prop. §12.1]]; for a continuous action it is an open equivalence relation, [[§12 Group Actions and Orbit Spaces#^lem-12-3|591 Lemma §12.3]].

The left cosets of $H \leq G$ are the special case of $H$ acting on $G$ by right multiplication, discussed [[§28 Left and Right Cosets#^prop-28-1|below]].

> [!definition] Definition §27.2: Orbit Space Notation
> For a left action of $G$ on $X$, the set of orbits is written
>
> $$
> G \backslash X := \{ Gx : x \in X \};
> $$
>
> for a right action, $X / G := \{ xG : x \in X \}$, “like a quotient.” The group is written on the side from which it acts. Example: the orbits of $O_3(\mathbb{R})$ on $\mathbb{R}^3$ are the spheres about the origin ([[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-2|WS 4.8]] below), so $O_3 \backslash \mathbb{R}^3 \leftrightarrow \mathbb{R}_{\geq 0}$ via the radius.
>
> *Source: lecture*

^def-27-2

![[m493-25-2.svg]]
*The orbits of $O_3(\mathbb{R})$ on $\mathbb{R}^3$ are the spheres about the origin, the origin itself being a one-point orbit; the orbit of $x$ (red) is the sphere of radius $|x|$. The ray $\mathbb{R}_{\geq 0}$ (blue) meets each orbit exactly once, which is the bijection $O_3 \backslash \mathbb{R}^3 \leftrightarrow \mathbb{R}_{\geq 0}$.*

> [!remark]- Connections
> - Same notion as the orbit space of [[§27 Orbits#^def-27-1|Def. §27.1]] (worksheet form).
> - “Like a quotient”: the quotient-set notation $X/{\sim}$ of MATH 590, [[§13 Quotient Topology#^def-13-3|Quotient Space]] (590 Def. §13.3); the coset spaces $G/H$ of [[§28 Left and Right Cosets#^def-28-2|Def. §28.2]] and quotient groups [[§40 Quotient Groups#^def-40-1|Def. §40.1]].
