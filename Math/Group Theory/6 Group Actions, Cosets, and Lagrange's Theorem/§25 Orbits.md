---
type: section
subject: "[[Group Theory]]"
chapter: 6
section: 25
tags: [group-theory, math493]
---
← [[§24 Stabilizers and Fixed Points]] · ↑ [[· 6 Group Actions, Cosets, and Lagrange's Theorem]] · [[§26 Left and Right Cosets]] →

*Reference: Pinter Ch. 13, Ex. J.*

> [!definition] Definition §25.1: Orbit; Orbit Space
> Let $G$ [[§23 Actions#^def-23-1|act]] on $X$. For $x \in X$, the **orbit** of $x$ is
>
> $$
> Gx := \{ g \star x : g \in G \} \subseteq X,
> $$
>
> the set of points reachable from $x$. The set of all orbits is written $G \backslash X$ (for a right action, $X/G$). The action is **transitive** if there is only one orbit, i.e. $Gx = X$ for some (equivalently every) $x$.
>
> *Source: WS 4*

^def-25-1

> [!remark]- Connections
> - Orbit size is the index of the stabilizer: [[§28 Orbit–Stabilizer#^thm-28-3|Orbit–Stabilizer]]; cosets are orbits: [[§26 Left and Right Cosets#^prop-26-1|Cosets Are Orbits]].
> - The orbit-space notation is restated from lecture in [[§25 Orbits#^def-25-2|Orbit Space Notation, Def. §25.2]].
> - With topologies: the orbit space X/G with the quotient topology, [[§12 Group Actions and Orbit Spaces#^def-12-5|591 Def. §12.5]] (orbits as in [[§12 Group Actions and Orbit Spaces#^def-12-3|591 Def. §12.3]]; e.g. complex projective space as an orbit space, [[§12 Group Actions and Orbit Spaces#^ex-12-3|591 Ex. §12.3]]); a continuous transitive action makes X a homogeneous space, [[§13 Homogeneous Spaces#^def-13-1|591 Def. §13.1]].

> [!theorem] Proposition §25.1: Orbits Partition $X$
> Let $G$ act on $X$ and $x, y \in X$. Then either $Gx = Gy$ or $Gx \cap Gy = \varnothing$. Hence $X$ is the disjoint union of the distinct orbits.
>
> *Source: WS 4.6*

^prop-25-1

> [!proof]+ Proof
> Suppose $z \in Gx \cap Gy$, say $z = g \star x = h \star y$ with $g, h \in G$. Then $x = g^{-1} \star (h \star y) = (g^{-1}h) \star y \in Gy$, so for any $a \in G$, $a \star x = (ag^{-1}h) \star y \in Gy$; thus $Gx \subseteq Gy$. Symmetrically $Gy \subseteq Gx$. So a nonempty intersection forces equality. Every $x$ lies in its own orbit ($x = e \star x$), so the orbits cover $X$.

^pf-25-1

*Uses:* [[§25 Orbits#^def-25-1|Def. §25.1]], [[§23 Actions#^def-23-1|Def. §23.1]], [[§22 Equivalence Relations and Partitions#^def-22-3|Def. §22.3]]

![[m493-25-1.svg]]
*The proof: if the orbits of $x$ and $y$ share a point $z$, then $x$ is reached from $y$ by going to $z$ with $h$ and back with $g^{-1}$ (red), so $x = (g^{-1}h) \star y \in Gy$, and then all of $Gx$ lies in $Gy$.*

> [!theorem] Proposition §25.2: The Orbit Relation
> The relation “$x \sim y$ iff $y = g \star x$ for some $g \in G$” is an [[§22 Equivalence Relations and Partitions#^def-22-1|equivalence relation]] on $X$, and its equivalence classes are the orbits.

^prop-25-2

> [!proof]+ Proof
> Reflexive: $x = e \star x$. Symmetric: $y = g \star x$ gives $x = g^{-1} \star y$. Transitive: $y = g \star x$ and $z = h \star y$ give $z = (hg) \star x$. The class of $x$ is $\{g \star x : g \in G\} = Gx$. (This is a second proof that the orbits partition $X$, via [[§22 Equivalence Relations and Partitions#^prop-22-1|§22.1]].)

^pf-25-2

*Uses:* [[§22 Equivalence Relations and Partitions#^def-22-1|Def. §22.1]], [[§22 Equivalence Relations and Partitions#^def-22-2|Def. §22.2]], [[§22 Equivalence Relations and Partitions#^prop-22-1|§22.1]], [[§23 Actions#^def-23-1|Def. §23.1]], [[§25 Orbits#^def-25-1|Def. §25.1]]

> [!remark]- Connections
> - The orbit space is the quotient set of this relation; with a topology it is a quotient space in MATH 590: [[§12 Quotient Topology#^def-12-3|Quotient Space]] (590 §12.3).
> - Same relation in 591, [[§12 Group Actions and Orbit Spaces#^def-12-4|591 Def. §12.4]] and [[§12 Group Actions and Orbit Spaces#^prop-12-1|591 Prop. §12.1]]; for a continuous action it is an open equivalence relation, [[§12 Group Actions and Orbit Spaces#^lem-12-3|591 Lemma §12.3]].

The left cosets of $H \leq G$ are the special case of $H$ acting on $G$ by right multiplication, discussed [[§26 Left and Right Cosets#^prop-26-1|below]].

> [!definition] Definition §25.2: Orbit Space Notation
> For a left action of $G$ on $X$, the set of orbits is written
>
> $$
> G \backslash X := \{ Gx : x \in X \};
> $$
>
> for a right action, $X / G := \{ xG : x \in X \}$, “like a quotient.” The group is written on the side from which it acts. Example: the orbits of $O_3(\mathbb{R})$ on $\mathbb{R}^3$ are the spheres about the origin ([[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|WS 4.8]] below), so $O_3 \backslash \mathbb{R}^3 \leftrightarrow \mathbb{R}_{\geq 0}$ via the radius.
>
> *Source: lecture*

^def-25-2

![[m493-25-2.svg]]
*The orbits of $O_3(\mathbb{R})$ on $\mathbb{R}^3$ are the spheres about the origin, the origin itself being a one-point orbit; the orbit of $x$ (red) is the sphere of radius $|x|$. The ray $\mathbb{R}_{\geq 0}$ (blue) meets each orbit exactly once, which is the bijection $O_3 \backslash \mathbb{R}^3 \leftrightarrow \mathbb{R}_{\geq 0}$.*

> [!remark]- Connections
> - Same notion as the orbit space of [[§25 Orbits#^def-25-1|Def. §25.1]] (worksheet form).
> - “Like a quotient”: the quotient-set notation $X/{\sim}$ of MATH 590, [[§12 Quotient Topology#^def-12-3|Quotient Space]] (590 §12.3); the coset spaces $G/H$ of [[§26 Left and Right Cosets#^def-26-2|Def. §26.2]] and quotient groups [[§37 Quotient Groups#^def-37-1|Def. §37.1]].
