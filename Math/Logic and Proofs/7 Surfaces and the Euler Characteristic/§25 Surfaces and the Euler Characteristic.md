---
type: section
subject: "[[Logic and Proofs]]"
chapter: 7
section: 25
tags: [logic-and-proofs, mat250]
---
← [[§24★ Congruence Modulo a Prime]] · ↑ [[· 7 Surfaces and the Euler Characteristic]]

*MAT 250 lecture (Euler characteristic) · MAT 250 HW6 (Questions 1–4); standard material.*

A surface built from polygons has a simple numerical fingerprint, $\chi = V - E + F$. This section computes it by cutting and gluing: removing a disk lowers $\chi$ by $1$, gluing two boundary circles does not change it, and so a sphere with $h$ handles and $b$ holes has $\chi = 2 - 2h - b$. Everything here is honest counting, and the counting is proved; two deep facts sit underneath and are only stated: that $\chi$ does not depend on how the surface is cut into polygons, and the classification of surfaces. There is no Eccles chapter; the unit is known from lecture through HW6.

## Polygonal Surfaces

> [!definition] Definition §25.1: Polygonal Surface
> A **polygon** is a closed disk whose boundary circle is divided by $n \ge 1$ points (its *corners*) into $n$ arcs (its *sides*); for $n \ge 3$ picture an ordinary $n$-gon. A **polygonal surface** $S$ is a space obtained from finitely many disjoint polygons by choosing some disjoint pairs of sides, giving each side of a pair a direction (an arrow), and gluing the two sides of each pair together so that the arrows match (start to start, end to end).
>
> After gluing, the images of the corners are the **vertices** of $S$, the images of the sides are its **edges** (two glued sides make one edge), and the polygons are its **faces**; write $V, E, F$ for their numbers. A side that is glued to nothing is a **boundary edge**. The boundary edges form the **boundary** of $S$, which is a disjoint union of circles, the **boundary circles** of $S$.
>
> Every point of $S$ has a neighbourhood that looks like an open disk (at points off the boundary) or a half-disk (on the boundary); this is what makes $S$ a *surface*. Different polygonal structures can give the same surface (up to [[§9 Continuous Functions#^def-9-2|homeomorphism]]); each is a **polygonal decomposition** of that surface.
>
> *Source: lecture (HW6); standard*

^def-25-1

> [!remark]- Connections
> - The gluing is a quotient space: [[§12 Quotient Topology#^def-12-3|590 Def. §12.3]]; a single polygon with labelled, oriented sides is [[§29 The Seifert–van Kampen Theorem#^def-29-1|590 Def. §29.1]].

> [!definition] Definition §25.2: Euler Characteristic
> The **Euler characteristic** of a polygonal surface $S$ is
>
> $$
> \chi(S) = V - E + F
> $$
>
> (in lecture: $\chi = \#_0 - \#_1 + \#_2$, the numbers of $0$-, $1$- and $2$-dimensional pieces). For a circle divided into $n$ arcs — vertices and edges only — the same count gives $\chi = n - n = 0$. Since the counts simply add, $\chi(S \sqcup S') = \chi(S) + \chi(S')$ for a disjoint union.
>
> *Source: lecture (HW6); standard*

^def-25-2

> [!example] Example §25.1: Sphere, Disk and Circle
> - **Sphere.** The surface of a tetrahedron: $4 - 6 + 4 = 2$. Of a cube: $8 - 12 + 6 = 2$. Two $1$-gons (disks with one corner and one side) glued along their sides — the northern and southern hemispheres, glued along the equator: $V = 1$, $E = 1$, $F = 2$, so $1 - 1 + 2 = 2$.
> - **Disk.** A single triangle, nothing glued: $3 - 3 + 1 = 1$; a single $n$-gon: $n - n + 1 = 1$.
> - **Circle.** $n$ vertices and $n$ edges: $0$.
>
> Three decompositions of the sphere give the same value $2$. This is no accident ([[§25 Surfaces and the Euler Characteristic#^thm-25-2|Theorem §25.2]] below), and it is why one writes $\chi(\text{sphere}) = 2$, $\chi(\text{disk}) = 1$.
>
> *Source: lecture (HW6); standard*

^ex-25-1

## Invariance

> [!theorem] Lemma §25.1: Subdivision Does Not Change $\chi$
> Each of the following changes a polygonal decomposition of a surface into another decomposition of the same surface, with the same $\chi$:
> 1. adding a new vertex in the interior of an edge, which splits it into two edges;
> 2. adding a new edge inside a face, joining two of its corners and cutting the face into two polygons.
>
> *Source: lecture (HW6); standard*

^lem-25-1

> [!proof]+ Proof
> (1) $V$ and $E$ each increase by $1$ and $F$ is unchanged: $(V + 1) - (E + 1) + F = V - E + F$. (2) $E$ and $F$ each increase by $1$ and $V$ is unchanged: $V - (E + 1) + (F + 1) = V - E + F$.

^pf-25-1

*Uses:* [[§25 Surfaces and the Euler Characteristic#^def-25-2|Def. §25.2]]

> [!theorem] Theorem §25.2: Invariance of the Euler Characteristic
> Any two polygonal decompositions of the same surface (or of homeomorphic surfaces) have the same Euler characteristic. So $\chi(S)$ is a property of the surface $S$, not of the way it is cut into polygons.
>
> (Stated without proof; see the remark below.)
>
> *Source: lecture (HW6); standard*

^thm-25-2

> [!remark] Remark: What Is Proved Here and What Is Taken on Trust
> - *Proved:* all the counting — [[§25 Surfaces and the Euler Characteristic#^lem-25-1|Lemma §25.1]], the cutting and gluing rules ([[§25 Surfaces and the Euler Characteristic#^prop-25-3|Propositions §25.3]], [[§25 Surfaces and the Euler Characteristic#^prop-25-4|§25.4]], [[§25 Surfaces and the Euler Characteristic#^cor-25-5|Corollary §25.5]]) and the formula of [[§25 Surfaces and the Euler Characteristic#^thm-25-6|Theorem §25.6]]. Each says how $V - E + F$ changes from one explicit decomposition to the next, so each computes $V - E + F$ for the particular decomposition that the construction produces.
> - *Taken on trust:* [[§25 Surfaces and the Euler Characteristic#^thm-25-2|Theorem §25.2]]. It is what turns these counts into facts about surfaces: that *every* decomposition of the torus has $V - E + F = 0$, that the different methods in the examples below had to give the same answer, and that the result does not depend on where the disks are removed or in which order the steps are made. Lemma §25.1 shows that $\chi$ survives subdividing, so the theorem would follow if any two decompositions of a surface had a common subdivision. That is true, but its proof needs real topology (every surface can be triangulated, and any two triangulations of it have subdivisions that match up — both due to Radó in the 1920s); the modern proof identifies $\chi$ with an alternating sum of ranks of homology groups. We also trust that the result of a gluing does not depend on which matching homeomorphism is used, only on the directions of the arrows, and the claim in [[§25 Surfaces and the Euler Characteristic#^def-25-1|Def. §25.1]] that the glued space is a surface.
> - *Also taken on trust:* the classification of surfaces ([[§25 Surfaces and the Euler Characteristic#^thm-25-7|Theorem §25.7]]).
>
> Granting Theorem §25.2, $\chi$ distinguishes surfaces: a sphere ($\chi = 2$) is not homeomorphic to a torus ($\chi = 0$), however the two are cut up.

^rem-25-1

> [!remark]- Connections
> - The fundamental group gives a different proof that such surfaces are distinct: [[§28 Fundamental Group of Some Surfaces#^cor-28-6|590 Cor. §28.6]] ($S^2$, $T^2$, $P^2$, $\Sigma_2$ are pairwise non-homeomorphic).

## Cutting and Gluing

> [!theorem] Proposition §25.3: Removing a Disk Lowers $\chi$ by 1
> Let $S$ be a polygonal surface and let $S'$ be obtained from $S$ by removing a small open disk inside a face ("adding a boundary circle"). Then $S'$ has one more boundary circle than $S$, and
>
> $$
> \chi(S') = \chi(S) - 1 .
> $$
>
> *Source: lecture (HW6); standard*

^prop-25-3

> [!proof]+ Proof
> Let $P$ be the face and $v$ one of its corners. Inside $P$ draw a small triangle $T$ with three new vertices $x, y, z$ and edges $xy, yz, zx$, enclosing the disk to be removed, and join it to the boundary of $P$ by two new edges $vx$ and $vy$ that meet only at $v$. The region of $P$ outside $T$ is an annulus, and the two cuts $vx$, $vy$ divide it into two polygons. So $P$ is replaced by three faces (two pieces and $T$): $V$ increases by $3$, $E$ by $3 + 2 = 5$, $F$ by $2$, and $\chi$ changes by $3 - 5 + 2 = 0$.
>
> Now remove the interior of $T$: the result $S'$ is the polygonal surface made from the same polygons except $T$, whose three sides $xy, yz, zx$ become a new boundary circle. $V$ and $E$ are unchanged and $F$ drops by $1$, so $\chi(S') = \chi(S) - 1$.

^pf-25-3

*Uses:* [[§25 Surfaces and the Euler Characteristic#^def-25-1|Def. §25.1]], [[§25 Surfaces and the Euler Characteristic#^def-25-2|Def. §25.2]]

> [!theorem] Proposition §25.4: Gluing Two Boundary Circles Leaves $\chi$ Unchanged
> Let $C$ and $C'$ be two different boundary circles of a polygonal surface $S$ ($S$ may be the disjoint union of two surfaces, one containing $C$ and the other $C'$). Let $S''$ be obtained by gluing $C$ to $C'$, in either of the two possible directions. Then
>
> $$
> \chi(S'') = \chi(S) .
> $$
>
> *Source: lecture (HW6); standard*

^prop-25-4

> [!proof]+ Proof
> Suppose $C$ consists of $m$ edges and $C'$ of $m'$ edges. Adding vertices on edges of the shorter circle ([[§25 Surfaces and the Euler Characteristic#^lem-25-1|Lemma §25.1]](1), which does not change $\chi$), we may assume both consist of $n$ vertices and $n$ edges. Glue $C$ to $C'$ matching the vertices and edges of $C$ with those of $C'$ in cyclic order, going round $C'$ in whichever direction is wanted. Then the $n$ vertices of $C$ are identified with the $n$ vertices of $C'$, and likewise the edges, while the faces are untouched:
>
> $$
> \chi(S'') = (V - n) - (E - n) + F = V - E + F = \chi(S) .
> $$
>
> Equivalently: the glued circle, which has $\chi = 0$, was counted twice and is now counted once.

^pf-25-4

*Uses:* [[§25 Surfaces and the Euler Characteristic#^lem-25-1|§25.1]], [[§25 Surfaces and the Euler Characteristic#^def-25-2|Def. §25.2]]

> [!example] Example §25.2: The Cylinder
> The cylinder (annulus) has $\chi = 0$, computed two ways.
> - *Directly:* a square with one pair of opposite sides glued, arrows in the same direction. The four corners become $2$ vertices, the four sides become $3$ edges (the glued pair is one edge; the other two sides are the two boundary circles), and there is $1$ face: $2 - 3 + 1 = 0$.
> - *By cutting:* the cylinder is a sphere with two disks removed, so by [[§25 Surfaces and the Euler Characteristic#^prop-25-3|Proposition §25.3]] twice, $\chi = 2 - 1 - 1 = 0$. In the same way the disk is a sphere minus one disk, $2 - 1 = 1$, agreeing with [[§25 Surfaces and the Euler Characteristic#^ex-25-1|Example §25.1]].
>
> *Source: lecture (HW6); standard*

^ex-25-2

![[m250-25-1.svg]]
*The cylinder as a square whose two $a$-sides (blue) are glued with matching arrows; the other two sides (red) stay free and become the two boundary circles. Stretching the cylinder's ends open shows it is a sphere with two disks removed, so the counts $2 - 3 + 1$ and $2 - 1 - 1$ must agree.*

> [!theorem] Corollary §25.5: Attaching a Handle Lowers $\chi$ by 2
> Let $S^+$ be obtained from a polygonal surface $S$ by **attaching a handle**: remove two disjoint small open disks and glue the two ends of a cylinder to the two new boundary circles. Then
>
> $$
> \chi(S^+) = \chi(S) - 2 .
> $$
>
> *Source: lecture (HW6: "adding a hole, $\chi - 2$"); standard*

^cor-25-5

> [!proof]+ Proof
> Removing the two disks gives $\chi(S) - 2$ ([[§25 Surfaces and the Euler Characteristic#^prop-25-3|Proposition §25.3]] twice). Adding the disjoint cylinder adds $0$ ([[§25 Surfaces and the Euler Characteristic#^ex-25-2|Example §25.2]], [[§25 Surfaces and the Euler Characteristic#^def-25-2|Def. §25.2]]). The two gluings change nothing ([[§25 Surfaces and the Euler Characteristic#^prop-25-4|Proposition §25.4]]). Total: $\chi(S) - 2$. (Gluing the two new boundary circles directly to each other, without a cylinder, gives the same count.)

^pf-25-5

*Uses:* [[§25 Surfaces and the Euler Characteristic#^prop-25-3|§25.3]], [[§25 Surfaces and the Euler Characteristic#^prop-25-4|§25.4]], [[§25 Surfaces and the Euler Characteristic#^ex-25-2|Ex. §25.2]], [[§25 Surfaces and the Euler Characteristic#^def-25-2|Def. §25.2]]

## The Torus, the Genus-2 Surface and the Klein Bottle

> [!example] Example §25.3: The Torus
> $\chi(\text{torus}) = 0$.
>
> *Method 1 (glue the ends of a cylinder).* Gluing the two boundary circles of a cylinder together, with matching directions, turns it into a torus. The cylinder is a sphere with two boundary circles, $\chi = 2 - 2 = 0$ ([[§25 Surfaces and the Euler Characteristic#^ex-25-2|Example §25.2]]), and the gluing does not change $\chi$ ([[§25 Surfaces and the Euler Characteristic#^prop-25-4|Proposition §25.4]]): $\chi_{\text{torus}} = \chi_{\text{cylinder}} = 0$.
>
> *Method 2 (cut along two circles).* Cutting a torus lying flat along its outer equator and its inner equator (the circle around the hole) splits it into a top half and a bottom half, each an annulus, i.e. a disk with a disk removed. So
>
> $$
> \chi_{\text{torus}} = 2\chi_{\text{disk}} - 2 = 2 - 2 = 0 ,
> $$
>
> the $-2$ for the two holes, and the two gluings of boundary circles counting $0$.
>
> *Method 3 (gluing diagram).* The torus is a square with both pairs of opposite sides glued, all arrows matching (figure below): all four corners become one vertex, the four sides become two edges $a$, $b$, and there is one face: $1 - 2 + 1 = 0$. Equivalently, the torus is a sphere with one handle: $2 - 2 = 0$ ([[§25 Surfaces and the Euler Characteristic#^cor-25-5|Corollary §25.5]]).
>
> *Source: HW6*

^ex-25-3

> [!remark]- Connections
> - The torus as a quotient of the square: [[§12 Quotient Topology#^ex-12-3|590 Ex. §12.3]], with boundary word $aba^{-1}b^{-1}$ in [[§29 The Seifert–van Kampen Theorem#^ex-29-7|590 Ex. §29.7]]; its fundamental group $\mathbb{Z} \times \mathbb{Z}$: [[§23 The Fundamental Group#^cor-23-8|590 Cor. §23.8]]. Workhorse note: [[Torus]].

> [!example] Example §25.4: The Genus-2 Surface
> The genus-$2$ surface ("pretzel", double torus) has $\chi = -2$.
>
> *Method 1 (two tori joined by a tube).* Remove a disk from each of two tori and join the two new boundary circles by a cylinder:
>
> $$
> \chi_{\text{pretzel}} = 2\chi_{\text{torus}} - 2 = 0 - 2 = -2
> $$
>
> (two removed disks; the tube and both gluings count $0$).
>
> *Method 2 (cut into top and bottom halves).* Cutting along the horizontal "equator" circles — the outer one and one around each hole — splits the pretzel into two copies of a disk with two holes, glued along three pairs of boundary circles. Each half has $\chi = 1 - 2 = -1$, the gluings count $0$, so
>
> $$
> \chi_{\text{pretzel}} = 2\chi_{\text{disk}} - 4 = 2 - 4 = -2 ,
> $$
>
> in agreement with Method 1.
>
> *Method 3 (gluing diagram).* An octagon with sides $a_1 b_1 a_1^{-1} b_1^{-1} a_2 b_2 a_2^{-1} b_2^{-1}$ glued in pairs: one vertex, four edges, one face, $1 - 4 + 1 = -2$. Or: a sphere with two handles, $2 - 2 \cdot 2 = -2$.
>
> *Source: HW6*
>
> *The HW6 solution writes $2\chi_{\text{disk}} - 4 = 2 - 4 = 0$ in Method 2; the value is $-2$, as in Method 1.*

^ex-25-4

> [!remark]- Connections
> - [[§28 Fundamental Group of Some Surfaces#^def-28-5|590 Def. §28.5]] (the double torus $\Sigma_2$, two tori glued along a removed disk, as in Method 1). Workhorse note: [[Double torus]].

> [!example] Example §25.5: The Klein Bottle
> The **Klein bottle** is obtained from a cylinder by gluing its two boundary circles to each other in the *opposite* direction from the torus; equivalently, it is the square with one pair of opposite sides arrowed in the same direction and the other pair arrowed in opposite directions, each pair glued so that the arrows match (figure below). It cannot be built inside $\mathbb{R}^3$ without the surface passing through itself, and it has only one side. Its Euler characteristic is $0$.
>
> *Method 1 (glue the ends of a cylinder).* Gluing the two boundary circles of a cylinder together, in either direction, does not change $\chi$ ([[§25 Surfaces and the Euler Characteristic#^prop-25-4|Proposition §25.4]]): $\chi_{\text{Klein bottle}} = \chi_{\text{cylinder}} = 0$.
>
> *Method 2 (two cylinders).* Cutting the cylinder of Method 1 around its middle shows the Klein bottle as two cylinders glued end to end along both pairs of boundary circles (one gluing reversed): $\chi_{\text{Klein bottle}} = 2\chi_{\text{cylinder}} = 0$.
>
> *Method 3 (gluing diagram).* All four corners of the square become one vertex, there are two edges and one face: $1 - 2 + 1 = 0$ — the same count as the torus, although the surfaces are different.
>
> *Source: HW6*

^ex-25-5

![[m250-25-2.svg]]
*Gluing diagrams: glue each pair of equally labelled sides so that the arrows match. For the torus both pairs keep their direction; for the Klein bottle the $b$-sides (red) point opposite ways, so they are glued with a flip. In both, all four corners become a single vertex and $\chi = 1 - 2 + 1 = 0$.*

> [!remark]- Connections
> - The Klein bottle as the square with boundary word $aba^{-1}b$: [[§29 The Seifert–van Kampen Theorem#^ex-29-7|590 Ex. §29.7]], and its (non-abelian) fundamental group in [[§29 The Seifert–van Kampen Theorem#^ex-29-8|590 Ex. §29.8]].

## The General Formula

> [!definition] Definition §25.3: Sphere with Handles and Holes
> For integers $h, b \ge 0$, let $\Sigma_{h,b}$ be the surface obtained from a sphere by attaching $h$ handles and removing $b$ disjoint open disks. Its **genus** is $h$ and it has $b$ boundary circles. Thus $\Sigma_{0,0}$ is the sphere, $\Sigma_{0,1}$ the disk, $\Sigma_{0,2}$ the cylinder, $\Sigma_{1,0}$ the torus and $\Sigma_{2,0}$ the genus-$2$ surface.
>
> *Source: lecture (HW6); standard*

^def-25-3

> [!theorem] Theorem §25.6: Euler Characteristic of a Sphere with Handles and Holes
> $$
> \chi(\Sigma_{h,b}) = 2 - 2h - b .
> $$
>
> *Source: HW6*

^thm-25-6

> [!proof]+ Proof
> Start from the sphere, $\chi = 2$ ([[§25 Surfaces and the Euler Characteristic#^ex-25-1|Example §25.1]]). Each of the $h$ handles lowers $\chi$ by $2$ ([[§25 Surfaces and the Euler Characteristic#^cor-25-5|Corollary §25.5]]), and each of the $b$ removed disks lowers it by $1$ ([[§25 Surfaces and the Euler Characteristic#^prop-25-3|Proposition §25.3]]). Formally, by induction on $h + b$: the case $h = b = 0$ is the sphere, and $\Sigma_{h,b}$ arises from $\Sigma_{h-1,b}$ by attaching a handle or from $\Sigma_{h,b-1}$ by removing a disk. Hence $\chi(\Sigma_{h,b}) = 2 - 2h - b$ for the decomposition built in this way, and so, by [[§25 Surfaces and the Euler Characteristic#^thm-25-2|Theorem §25.2]], for every decomposition.

^pf-25-6

*Uses:* [[§25 Surfaces and the Euler Characteristic#^ex-25-1|Ex. §25.1]], [[§25 Surfaces and the Euler Characteristic#^cor-25-5|§25.5]], [[§25 Surfaces and the Euler Characteristic#^prop-25-3|§25.3]], [[§25 Surfaces and the Euler Characteristic#^thm-25-2|§25.2]], [[§5 The Induction Principle#^thm-5-3|§5.3]] (induction from $0$)

| surface | $h$ | $b$ | $\chi = 2 - 2h - b$ |
|---|---|---|---|
| sphere | $0$ | $0$ | $2$ |
| disk | $0$ | $1$ | $1$ |
| cylinder | $0$ | $2$ | $0$ |
| torus | $1$ | $0$ | $0$ |
| torus minus a disk | $1$ | $1$ | $-1$ |
| genus-$2$ surface | $2$ | $0$ | $-2$ |

> [!theorem] Theorem §25.7: Classification of Surfaces
> Every [[§15 Compact Spaces#^def-15-2|compact]] [[§13 Connected Spaces#^def-13-new1|connected]] surface is homeomorphic to exactly one of the following:
> - $\Sigma_{h,b}$, a sphere with $h \ge 0$ handles and $b \ge 0$ holes, with $\chi = 2 - 2h - b$ (the two-sided, or *orientable*, surfaces);
> - a sphere with $k \ge 1$ *crosscaps* (a disk removed and a Möbius band glued in, each lowering $\chi$ by $1$) and $b \ge 0$ holes, with $\chi = 2 - k - b$ (the one-sided surfaces).
>
> Hence two compact connected surfaces are homeomorphic if and only if they have the same number of boundary circles, are both one-sided or both two-sided, and have the same Euler characteristic. For example, the projective plane is the case $k = 1$ ($\chi = 1$) and the Klein bottle the case $k = 2$ ($\chi = 0$).
>
> (Stated without proof.)
>
> *Source: lecture (HW6); standard*

^thm-25-7

> [!remark]- Connections
> - Developed further in: the projective plane [[§28 Fundamental Group of Some Surfaces#^def-28-1|590 Def. §28.1]], and surfaces as quotients of a single polygon with their fundamental groups, [[§29 The Seifert–van Kampen Theorem#^thm-29-3|590 Thm. §29.3]], [[§29 The Seifert–van Kampen Theorem#^ex-29-8|590 Ex. §29.8]].
