---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 2
section: 14
tags: [differentiable-manifolds, math591]
---
← [[§13 Homogeneous Spaces]] · ↑ [[· 2 Topological Groups and Homogeneous Spaces]] · [[§15 Example꞉ The Classical Groups]] →

*Thread: quotients — The coset space $G/H$ as a topological space: open quotient, Hausdorff when $H$ is closed, and homeomorphic to a homogeneous space. The Grassmannians are the payoff. The two threads meet in the next chapter.*

Definitions [[§13 Homogeneous Spaces#^def-13-4|§13.4]] and [[§13 Homogeneous Spaces#^def-13-5|Def. §13.5]] are purely algebraic. If $G$ carries a topology, $G/H$ inherits one in the only reasonable way.

> [!definition] Definition §14.1: The Quotient Topology on a Coset Space
> Let $G$ be a topological group and $H \le G$ a subgroup. The **quotient topology** on $G/H$ is the quotient topology induced by the canonical projection $\pi$ of Definition [[§13 Homogeneous Spaces#^def-13-5|§13.5]], in the sense of Definition [[§4 Quotient Spaces and Open Maps#^def-4-1|§4.1]]:
>
> $$
> W \subseteq G/H \text{ is open} \iff \pi^{-1}(W) \subseteq G \text{ is open in } G.
> $$
>
> Unless stated otherwise, $G/H$ always carries this topology.
>
> *Lee: Theorem 21.17*

^def-14-1

> [!remark]- Connections
> - The quotient topology in 590: [[§12 Quotient Topology#^def-12-2|590 Def. §12.2]].

> [!theorem] Proposition §14.1: Three Descriptions of the Open Sets
> Let $G$ be a topological group, $H \le G$, and $W \subseteq G/H$. The following are equivalent:
> 1. $W$ is open in $G/H$;
> 2. $\displaystyle\bigcup_{gH \in W} gH$, the union in $G$ of the cosets belonging to $W$, is open in $G$;
> 3. $W = \pi(U)$ for some open $U \subseteq G$ satisfying $UH = U$.
>
> Moreover $\pi$ is a continuous, surjective, *open* map, and the quotient topology is the finest topology on $G/H$ making $\pi$ continuous.
>
> *Lee: Theorem 21.17 and Lemma 21.1*

^prop-14-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $(1 \Leftrightarrow 2)$ By Definition [[§13 Homogeneous Spaces#^def-13-5|§13.5]] the fibre over a point $gH \in W$ is the coset $gH$, so $\pi^{-1}(W) = \bigcup_{gH \in W} gH$; now apply Definition [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|§14.1]].
>
> $(1 \Leftrightarrow 3)$ A subset $U \subseteq G$ satisfies $UH = U$ iff it is a union of cosets, i.e. iff it is saturated for the coset relation (Definition [[§4 Quotient Spaces and Open Maps#^def-4-4|§4.4]]): $UH = \bigcup_{u \in U} uH$ always contains $U$, and equals $U$ exactly when each $uH \subseteq U$. If $W$ is open, take $U = \pi^{-1}(W)$, which is open, saturated, and has $\pi(U) = W$ by surjectivity of $\pi$. Conversely if $U$ is open with $UH = U$, then $\pi^{-1}(\pi(U)) = U$ by saturation (Lemma [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]](4)), which is open, so $\pi(U)$ is open.
>
> *Openness of $\pi$.* For $U \subseteq G$ open, $\pi^{-1}(\pi(U)) = UH = \bigcup_{h \in H} Uh$, a union of translates of $U$. Right translation by $h$ is a homeomorphism of $G$ (it is continuous with continuous inverse, both restrictions of the multiplication of the topological group), so each $Uh$ is open and the union is open; hence $\pi(U)$ is open. Continuity and finest-topology are the general facts recorded after Definition [[§4 Quotient Spaces and Open Maps#^def-4-1|§4.1]].

^pf-14-1

*Uses:* [[§13 Homogeneous Spaces#^def-13-5|Def. §13.5]], [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|Def. §14.1]], [[§13 Homogeneous Spaces#^lem-13-3|§13.3]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]], [[§4 Quotient Spaces and Open Maps#^prop-4-1|§4.1]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-1|Def. §10.1]]

> [!theorem] Corollary §14.2: $\pi$ Is a Quotient Map
> $\pi : G \to G/H$ is a quotient map in the sense of Definition [[§5 Quotient Maps#^def-5-1|§5.1]], and consequently a map $g : G/H \to Z$ into a topological space is continuous if and only if $g \circ \pi : G \to Z$ is continuous.
>
> *Lee: Theorem 21.17*

^cor-14-2

> [!proof]+ Proof
> *(Not from lecture; filled in.)* $\pi$ is a continuous open surjection by Proposition [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-1|§14.1]], hence a quotient map by Proposition [[§5 Quotient Maps#^prop-5-5|§5.5]]. (It is also one directly from Definition [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|§14.1]], which is the defining property.) The second statement is the universal property, Proposition [[§5 Quotient Maps#^cor-5-2|§5.2]].

^pf-14-2

*Uses:* [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-1|§14.1]], [[§5 Quotient Maps#^prop-5-5|§5.5]], [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|Def. §14.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]]

> [!remark]- Connections
> - In 590: open surjections are quotient maps, [[§12 Quotient Topology#^prop-12-2|590 §12.2]]; the universal property, [[Universal Property of Quotient Maps]].

> [!remark] Remark
> **Openness of $\pi$, for free.** The action of $H$ on $G$ in Proposition [[§13 Homogeneous Spaces#^prop-13-4|§13.4]] is continuous, being the restriction to $H \times G$ of the map $(h,g) \mapsto gh^{-1}$ on $G \times G$, a composite of inversion and multiplication. So by the [[§13 Homogeneous Spaces#^rem-13-3|organizing fact]], Definition [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|§14.1]] *is* the orbit-space topology, and Lemma [[§12 Group Actions and Orbit Spaces#^lem-12-3|§12.3]] — every orbit relation of a continuous action is open — already gives that $\pi$ is an open map. The proof above is that argument written out in the group case, with the translations $L_h$ of Lemma [[§12 Group Actions and Orbit Spaces#^lem-12-2|§12.2]] appearing as right translations $g \mapsto gh$; it is included because the formula $\pi^{-1}(\pi(U)) = UH$ is worth seeing explicitly.

^rem-14-1

> [!theorem] Theorem §14.3: Homogeneous Spaces Are Homeomorphic to Coset Spaces
> Let $G$ act continuously and transitively on a topological space $X$, let $x_0 \in X$, $H = H_{x_0}$, and let $\Phi : G/H \to X$, $\Phi(gH) = g \cdot x_0$.
> 1. $\Phi$ is a continuous bijection.
> 2. If $G/H$ is compact and $X$ is Hausdorff, then $\Phi$ is a homeomorphism.
>
> In particular (2) applies whenever $G$ itself is compact.
>
> *Lee: Theorem 21.18, a smooth version without compactness (see the comparison below)*

^thm-14-3

![[m591-7-2.svg]]
*The triangle $G \to G/H \to X$: the orbit map $g \mapsto g \cdot x_0$ factors as $\Phi \circ \pi$.*

Upstairs is the group, downstairs its coset space, and the triangle commutes: $\Phi \circ \pi$ is the orbit map. The orbit map is continuous for free; part (1) is the universal property pushing that continuity down along $\pi$, and part (2) is the compactness argument upgrading the bottom arrow to a homeomorphism.

> [!proof]+ Proof
> *(Stated in Lecture 4, with a hypothesis missing — the board said “$G$ compact $\Rightarrow$ $G/H \cong X$”, and $X$ must also be Hausdorff; filled in.)*
> (1) Bijectivity is Lemma [[§13 Homogeneous Spaces#^lem-13-5|§13.5]]. The composite $\Phi \circ \pi : G \to X$ is the orbit map $g \mapsto g \cdot x_0$, which is continuous: it is $G \to G \times X \to X$, $g \mapsto (g, x_0) \mapsto g \cdot x_0$, a composite of a map continuous by Theorem [[§3 Subspaces and Products#^thm-3-10|§3.10]] with the action. By the universal property of the quotient (Proposition [[§5 Quotient Maps#^cor-5-2|§5.2]]), $\Phi$ is continuous.
>
> (2) By (1), $\Phi$ is a continuous bijection from the compact space $G/H$ onto the Hausdorff space $X$, hence a homeomorphism (Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](6)). Spelled out: if $C \subseteq G/H$ is closed, then $C$ is compact by Proposition [[§1 Point-Set Topology Review#^prop-1-8|§1.8]](5), so $\Phi(C)$ is compact by (2) of that proposition, hence closed in $X$ by (4); so $\Phi$ is a closed map, and the inverse of a closed continuous bijection is continuous, since $(\Phi^{-1})^{-1}(C) = \Phi(C)$ for every $C$.
>
> For the final sentence of the theorem: if $G$ is compact, then $G/H = \pi(G)$ is compact as the continuous image of a compact space.

^pf-14-3

*Uses:* [[§13 Homogeneous Spaces#^lem-13-5|§13.5]], [[§13 Homogeneous Spaces#^def-13-3|Def. §13.3]], [[§3 Subspaces and Products#^thm-3-10|§3.10]], [[§5 Quotient Maps#^cor-5-2|§5.2]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-2|§14.2]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[Bijection from Compact to Hausdorff is a Homeomorphism]], [[Continuous Image of a Compact Space is Compact]]

> [!remark]- Connections
> - The same pattern in 590 — a map constant on fibres induces a continuous bijection from the quotient: [[§12 Quotient Topology#^cor-12-4|590 §12.4 (Induced Bijection from Quotient)]].
> - The underlying bijection is the orbit bijection [[§28 Orbit–Stabilizer#^prop-28-2|493 §28.2]].

> [!example] Example §14.1: The Circle as $\mathbb{R}/\mathbb{Z}$
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
> The coset space $\mathbb{R}/\mathbb{Z}$ is compact, being the image under $\pi$ of the compact interval $[0,1]$ (every coset $t + \mathbb{Z}$ meets $[0,1]$), and $S^1$ is Hausdorff. So Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|§14.3]](2) gives a homeomorphism
>
> $$
> \Phi : \mathbb{R}/\mathbb{Z} \xrightarrow{\ \cong\ } S^1, \qquad t + \mathbb{Z} \longmapsto e^{2\pi i t} .
> $$
>
> Here $G = \mathbb{R}$ is *not* compact, so the version of the theorem with “$G$ compact” would not apply. The hypothesis on the quotient is genuinely weaker than the hypothesis on the group, and it is the one that matters: the proof uses compactness of $G/H$ and nothing about $G$.
>
> *Lee: Example 21.14(a)*

^ex-14-1

![[m591-7-3.svg]]
*The triangle for $\mathbb{R}$ acting on $S^1$: $t \mapsto e^{2\pi i t}$ factors through $\mathbb{R}/\mathbb{Z}$ as $\Phi \circ \pi$.*

The same triangle with $G = \mathbb{R}$. The exponential wraps the line around the circle; it is constant exactly on the cosets $t + \mathbb{Z}$, which is why it descends to the quotient, and the induced bottom arrow is the homeomorphism.

> [!remark]- Connections
> - In 590 the circle is the quotient $[0,1]/(0 \sim 1)$ via the same map $e^{2\pi i t}$: [[§12 Quotient Topology#^ex-12-2|590 Ex. §12.2]].

> [!example] Example §14.2: A Continuous Bijection That Is Not a Homeomorphism
> Let $G = \mathbb{R}_{\mathrm{disc}}$, the additive group of real numbers with the discrete topology — a topological group, since every map out of a discrete space is continuous. It acts on $X = \mathbb{R}$, with its usual topology, by translation, $t \cdot x = x + t$. The action is continuous, because $G \times X$ is the disjoint union of the open sets $\{t\} \times X$, on each of which it is a translation. It is transitive, the isotropy group of $0$ is $\{0\}$, and so $G/H = \mathbb{R}_{\mathrm{disc}}$. The map $\Phi : \mathbb{R}_{\mathrm{disc}} \to \mathbb{R}$, $t \mapsto t$, is a continuous bijection but not a homeomorphism: $\{0\}$ is open in $\mathbb{R}_{\mathrm{disc}}$ and not in $\mathbb{R}$. Here $X$ is Hausdorff and $G/H$ is not compact, so Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|§14.3]](2) does not apply — and its conclusion genuinely fails.
>
> *Lee: no counterpart; a course example*

^ex-14-2

> [!remark]- Connections
> - [[Discrete and indiscrete topologies]]; the same group appears in [[§2 Topological Manifolds#^ex-2-3|Ex. §2.3]] and [[§10 Topological Groups and Classical Matrix Groups#^ex-10-1|Discrete Groups, §10.1]].

**Comparison with Lee.** Lee's Theorem 21.18 has no compactness hypothesis: for a Lie group acting smoothly and transitively on a manifold, $\Phi$ is an equivariant *diffeomorphism*. Smoothness does the work that compactness does here — $\Phi$ has constant rank by his equivariant rank theorem (Theorem 7.25), and a bijection of constant rank is a diffeomorphism. His standing assumption that $G$ is a Lie group, in particular second countable, also rules out Example [[§14 The Topology of G∕H and Real Grassmannians#^ex-14-2|§14.2]], where $G$ is an uncountable discrete group. In the purely topological setting of the course some hypothesis is needed, and “$G/H$ compact, $X$ Hausdorff” is the one used.

**Classroom exchange and its resolution.** On the board the statement read “if $G$ is compact, then $G/H \cong X$ is a homeomorphism,” with no hypothesis on $X$ beyond the continuous transitive action. A student objected that the conclusion cannot hold with no condition on the topology of $X$; Uribe agreed on the spot (“good catch … I think I made a mistake, and I will correct that by email”). The correction arrived as Problem 1 of Assignment 2, which states exactly the theorem above: (1) with no hypotheses, and (2) under “$G/H$ compact and $X$ Hausdorff.” So the board version was off in two ways at once — it was missing Hausdorffness of $X$, and it asked for compactness of the wrong space. Example [[§14 The Topology of G∕H and Real Grassmannians#^ex-14-1|§14.1]] shows the second repair matters.

> [!definition] Definition §14.2: The Topology of a Homogeneous Space
> Let a topological group $G$ act transitively on a *set* $X$, let $x_0 \in X$, and let $H = H_{x_0}$. The **homogeneous-space topology** on $X$ is the one that makes the bijection $\Phi : G/H \to X$, $gH \mapsto g \cdot x_0$, of Lemma [[§13 Homogeneous Spaces#^lem-13-5|§13.5]] a homeomorphism: $V \subseteq X$ is open iff $\Phi^{-1}(V)$ is open in $G/H$.
>
> *Lee: Theorem 21.20*

^def-14-2

> [!remark]- Connections
> - For $\mathrm{Gr}_1(\mathbb{R}^{n+1}) = \mathbb{RP}^n$ this topology agrees with the quotient topology of $S^n/\{\pm 1\}$: [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|§17.6]].

> [!theorem] Proposition §14.4: Independence of the Base Point
> The homogeneous-space topology does not depend on the choice of $x_0$.
>
> *Lee: Theorem 21.20*

^prop-14-4

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $x_1 = a \cdot x_0$. Then $H_{x_1} = aH_{x_0}a^{-1}$, since $g\,a\cdot x_0 = a\cdot x_0 \iff a^{-1}ga \in H_{x_0}$. Right translation $g \mapsto ga^{-1}$ is a homeomorphism of $G$ carrying each coset $gH_{x_0}$ onto $ga^{-1}(aH_{x_0}a^{-1}) = ga^{-1}H_{x_1}$. So, by the universal property (Corollary [[§5 Quotient Maps#^cor-5-2|§5.2]]), it induces a continuous map $\bar R : G/H_{x_0} \to G/H_{x_1}$, $gH_{x_0} \mapsto ga^{-1}H_{x_1}$, whose inverse is induced in the same way by $g \mapsto ga$. Hence $\bar R$ is a homeomorphism. It intertwines the two bijections, since $\Phi_1(\bar R(gH_{x_0})) = ga^{-1}\cdot x_1 = g \cdot x_0 = \Phi_0(gH_{x_0})$. So $\Phi_1 = \Phi_0 \circ \bar R^{-1}$, and the two transported topologies coincide.

^pf-14-4

*Uses:* [[§13 Homogeneous Spaces#^def-13-2|Def. §13.2]], [[§14 The Topology of G∕H and Real Grassmannians#^def-14-1|Def. §14.1]], [[§14 The Topology of G∕H and Real Grassmannians#^def-14-2|Def. §14.2]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-1|Def. §10.1]], [[§5 Quotient Maps#^cor-5-2|§5.2]]

> [!remark]- Connections
> - $H_{a \cdot x_0} = aH_{x_0}a^{-1}$ is [[§24 Stabilizers and Fixed Points#^prop-24-2|493 §24.2 (Stabilizers of Points in the Same Orbit Are Conjugate)]].

> [!remark] Remark: Giving a Set a Topology
> Theorem [[§14 The Topology of G∕H and Real Grassmannians#^thm-14-3|§14.3]] is also used in reverse: when $X$ is merely a *set* on which $G$ acts transitively, the [[§14 The Topology of G∕H and Real Grassmannians#^def-14-2|definition above]] gives it a topology — “that's a natural way to give a topology to homogeneous spaces.” This is how the Grassmannians below get their topology, and the [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-4|proposition]] says the result is canonical.

^rem-14-2

> [!theorem] Corollary §14.5: When $G/H$ Is Hausdorff and Second Countable
> Let $G$ be a compact Hausdorff topological group and $H \le G$ a compact subgroup. Then $G/H$ is compact Hausdorff; if moreover $G$ is second countable, so is $G/H$.
>
> *Lee: Theorem 21.17*

^cor-14-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Everything is an application of [[§12 Group Actions and Orbit Spaces|§12]] to the continuous action of $H$ on $G$ of Proposition [[§13 Homogeneous Spaces#^prop-13-4|§13.4]], whose orbit space is $G/H$ with its quotient topology. Apply Corollary [[§12 Group Actions and Orbit Spaces#^cor-12-4|§12.4]]: $H$ and $G$ compact, $G$ Hausdorff, so the orbit space $G/H$ is Hausdorff; it is compact as $\pi(G)$. Second countability is Theorem [[§6 Open Quotients#^thm-6-3|§6.3]], the orbit relation being open by Lemma [[§12 Group Actions and Orbit Spaces#^lem-12-3|§12.3]].

^pf-14-5

*Uses:* [[§13 Homogeneous Spaces#^prop-13-4|§13.4]], [[§14 The Topology of G∕H and Real Grassmannians#^rem-14-1|Remark after §12.2]], [[§12 Group Actions and Orbit Spaces#^cor-12-4|§12.4]], [[§12 Group Actions and Orbit Spaces#^lem-12-3|§12.3]], [[§6 Open Quotients#^thm-6-3|§6.3]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]]

The classical groups through the course: defined in [[§10 Topological Groups and Classical Matrix Groups|Topological Groups and Classical Matrix Groups]], with the examples of [[§15 Example꞉ The Classical Groups|Example: The Classical Groups]]; topological manifolds as level sets in [[§11 The Classical Groups Are Topological Manifolds#^thm-11-6|Classical Groups Are Manifolds]]; $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$ acting on $\mathbb{R}^2$ and $\mathbb{R}^3$ in [[§12 Group Actions and Orbit Spaces#^ex-12-4|the rotations of the plane]] and [[§12 Group Actions and Orbit Spaces#^ex-12-5|the rotations of space]], and $\mathrm{SO}(3)$ on $S^2$ in [[§13 Homogeneous Spaces#^ex-13-2|the isotropy of the north pole]] and [[§13 Homogeneous Spaces#^ex-13-3|the sphere as a homogeneous space]]; $\mathrm{O}(n)$ acting on the Grassmannians in [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-8|Grassmannians as Homogeneous Spaces]]; smooth manifolds in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|the orthogonal group]] and [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-2|the unitary group]]; their tangent spaces at the identity in [[§23 Tangent Spaces I꞉ The Geometric Picture#^thm-23-5|The Classical Groups]], with [[§23 Tangent Spaces I꞉ The Geometric Picture#^ex-23-4|the infinitesimal rotations]]; and the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ in [[§39 Worked Example꞉ The Double Cover SU(2) → SO(3)#^thm-39-8|The Double Cover]].

## Real Grassmannians

> [!definition] Definition §14.3: Grassmannian
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

^def-14-3

> [!remark]- Connections
> - The smooth atlas on $\mathbb{RP}^n$: [[§17 Projective Spaces as Smooth Manifolds#^cor-17-5|§17.5 (Real Projective Space)]].

> [!remark] Remark: On the Index
> The board first said $\mathrm{Gr}_1(\mathbb{R}^n) = \mathbb{RP}^n$; a student asked whether it should be $n-1$, and after some back-and-forth (“this drives me absolutely crazy”) the answer settled on $\mathbb{RP}^{n-1}$: each line through $0$ in $\mathbb{R}^n$ meets the unit sphere $S^{n-1}$ in exactly two antipodal points $\pm v$, so $\mathbb{RP}^{n-1} \cong S^{n-1}/\{\pm I\}$, an $(n-1)$-dimensional object. Explicitly, the quotient on the right is the orbit space of the group $\{\pm I\} \cong \mathbb{Z}/2$ acting on $S^{n-1}$ by $v \mapsto \pm v$: a point is an antipodal pair $\{v, -v\}$, $\pi(v) = \{v,-v\}$, a set of pairs is open iff the union of the pairs is open in $S^{n-1}$, and the identification with $\mathrm{Gr}_1(\mathbb{R}^n)$ is $\{v, -v\} \mapsto \mathbb{R} v$, with inverse $\ell \mapsto \ell \cap S^{n-1}$. This orbit space is Hausdorff by Corollary [[§12 Group Actions and Orbit Spaces#^cor-12-4|§12.4]] ($\{\pm I\}$ finite, hence compact), and its topology agrees with the homogeneous-space topology of $\mathrm{Gr}_1(\mathbb{R}^n)$ (see [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|the note]] after Corollary [[§17 Projective Spaces as Smooth Manifolds#^cor-17-5|§17.5]]). The superscript on $\mathbb{RP}$ records the dimension of the manifold; the superscript on the $\mathbb{R}^n$ it is built from is one larger. (The alternative notation $\mathbb{P}(\mathbb{R}^n)$, treating $\mathbb{P}$ as an operation on the vector space, avoids the off-by-one.)

^rem-14-3

> [!remark]- Connections
> - For $n = 3$ this is the projective plane $S^2/(x \sim -x)$ of 590: [[§28 Fundamental Group of Some Surfaces#^def-28-1|590 Def. §28.1]], [[Projective plane]].

> [!theorem] Proposition §14.6: $\mathrm{O}(n)$ Acts Transitively on $\mathrm{Gr}_k({\mathbb{R}^n})$
> For $g \in \mathrm{O}(n)$ and $V \in \mathrm{Gr}_k(\mathbb{R}^n)$ set $g \cdot V = gV = \{\, gv \mid v \in V \,\}$. This defines an action of $\mathrm{O}(n)$ on $\mathrm{Gr}_k(\mathbb{R}^n)$, and the action is transitive.
>
> *Lee: Example 21.21*

^prop-14-6

> [!proof]+ Proof
> *(Set in Lecture 4 as a “linear algebra exercise”; filled in.)* *Action.* $gV$ is a linear subspace (image of a subspace under a linear map) of dimension $k$ ($g$ is injective), so $gV \in \mathrm{Gr}_k(\mathbb{R}^n)$; $IV = V$; and $g(g'V) = (gg')V$ by associativity.
>
> *Transitive* (“a linear algebra exercise”). Let $V, W \in \mathrm{Gr}_k(\mathbb{R}^n)$. Choose an orthonormal basis $v_1, \ldots, v_k$ of $V$ (Gram–Schmidt applied to any basis of $V$) and extend it to an orthonormal basis $v_1, \ldots, v_n$ of $\mathbb{R}^n$ (apply Gram–Schmidt to a basis of the orthogonal complement $V^\perp$, which has dimension $n - k$). Do the same for $W$: an orthonormal basis $w_1, \ldots, w_n$ of $\mathbb{R}^n$ with $w_1, \ldots, w_k$ spanning $W$. Let $g$ be the linear map with $g v_i = w_i$ for all $i$. Since $g$ carries an orthonormal basis to an orthonormal basis, $(gx) \cdot (gy) = x \cdot y$ for all $x, y$ (expand $x, y$ in the $v_i$), so $g \in \mathrm{O}(n)$; and $gV = g\,\operatorname{span}(v_1, \ldots, v_k) = \operatorname{span}(w_1, \ldots, w_k) = W$.

^pf-14-6

*Uses:* [[§14 The Topology of G∕H and Real Grassmannians#^def-14-3|Def. §14.3]], [[§12 Group Actions and Orbit Spaces#^def-12-1|Def. §12.1]], [[§13 Homogeneous Spaces#^def-13-1|Def. §13.1]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-6|Def. §10.6]], [[Gram–Schmidt procedure]], [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-51|LADR 6.51]], [[Linear map lemma]]

> [!remark]- Connections
> - The case $k = 1$ of the orthonormal-basis argument is [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|493 §30.2]] and [[§12 Group Actions and Orbit Spaces#^ex-12-5|Ex. §12.5]]; orthonormal bases in LADR: [[§20 Orthonormal Bases#^ladr-6-36|LADR 6.36]], [[§25 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-49|LADR 7.49]].

> [!theorem] Proposition §14.7: Isotropy of the Standard $k$-Plane
> Let $V_0 = \operatorname{span}(e_1, \ldots, e_k) \in \mathrm{Gr}_k(\mathbb{R}^n)$ be the base point. Then
>
> $$
> H_{V_0} = \left\{ \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \;\middle|\; A \in \mathrm{O}(k),\ B \in \mathrm{O}(n-k) \right\} \;\cong\; \mathrm{O}(k) \times \mathrm{O}(n-k),
> $$
>
> block matrices with respect to the decomposition $\mathbb{R}^n = V_0 \oplus V_0^\perp$, $V_0^\perp = \operatorname{span}(e_{k+1}, \ldots, e_n)$.
>
> *Lee: Example 21.21*

^prop-14-7

> [!proof]+ Proof
> *(Stated in Lecture 4, with the block picture of $\mathrm{O}(k) \times \mathrm{O}(n-k)$; filled in.)* Write $g \in \mathrm{O}(n)$ in blocks $g = \begin{pmatrix} A & C \\ D & B \end{pmatrix}$ with $A$ of size $k \times k$. Then $gV_0 = V_0$ iff $g e_j \in V_0$ for $j \le k$ iff the first $k$ columns have zero lower part, i.e. $D = 0$ (then $g$ maps $V_0$ into $V_0$, and injectivity plus $\dim$ gives $gV_0 = V_0$). Now orthogonal maps preserve orthogonal complements: if $gV_0 = V_0$ and $u \in V_0^\perp$, then for all $v \in V_0$, $(gu) \cdot v = (gu) \cdot (g g^{-1} v) = u \cdot g^{-1}v = 0$ since $g^{-1}v \in V_0$; so $g V_0^\perp \subseteq V_0^\perp$, i.e. $C = 0$. With $C = D = 0$, the condition $g^T g = I$ reads $A^T A = I_k$ and $B^T B = I_{n-k}$, i.e. $A \in \mathrm{O}(k)$, $B \in \mathrm{O}(n-k)$. Conversely every such block-diagonal matrix is orthogonal and fixes $V_0$. The map $(A, B) \mapsto \mathrm{diag}(A, B)$ is a group isomorphism from the product group and a homeomorphism (it is a linear embedding of coordinates).

^pf-14-7

*Uses:* [[§13 Homogeneous Spaces#^def-13-2|Def. §13.2]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-6|§14.6]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-6|Def. §10.6]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10.5]]

> [!remark]- Connections
> - The case $k = 1$ (up to reordering) is $\operatorname{Stab}(e_1) \cong \mathrm{O}_2$ in [[§30 Examples꞉ Linear Groups and the Cube#^prop-30-2|493 §30.2]](2).

**Transcription note.** Page 13 of the handwritten notes writes the base point as the span of $e_1$ through $e_n$. A $k$-plane is spanned by $k$ vectors, so the base point is the span of $e_1$ through $e_k$, as above.

> [!theorem] Corollary §14.8: Grassmannians as Homogeneous Spaces
> As sets, $\mathrm{Gr}_k(\mathbb{R}^n) \cong \mathrm{O}(n)/\big(\mathrm{O}(k) \times \mathrm{O}(n-k)\big)$ via $g H_{V_0} \mapsto g V_0$. Transporting the quotient topology across this bijection makes $\mathrm{Gr}_k(\mathbb{R}^n)$ a compact, Hausdorff, second countable space.
>
> *Lee: Examples 1.36 and 21.21*

^cor-14-8

> [!proof]+ Proof
> The bijection is Lemma [[§13 Homogeneous Spaces#^lem-13-5|§13.5]] with Propositions [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-6|§14.6]] and [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-7|§14.7]]. Explicitly, with $H = H_{V_0}$: a point of $\mathrm{O}(n)/H$ is a coset $gH$, and since every $h \in H$ preserves $V_0 = \operatorname{span}(e_1, \ldots, e_k)$, all elements of $gH$ have first $k$ columns spanning the same $k$-plane $gV_0$; conversely $g' V_0 = g V_0$ implies $g^{-1}g' \in H$, so
>
> $$
> gH = \{\, g' \in \mathrm{O}(n) \mid \operatorname{span}(\text{first } k \text{ columns of } g') = g V_0 \,\}.
> $$
>
> The identification $\Phi(gH) = gV_0$ sends a coset to the span of the first $k$ columns of any of its members; its inverse sends a $k$-plane $V$ to the set of orthogonal matrices whose first $k$ columns span $V$ (nonempty by transitivity). A set $W$ of $k$-planes is declared open iff the set of orthogonal matrices whose first $k$ columns span some member of $W$ is open in $\mathrm{O}(n)$. For the topology, apply Corollary [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-5|§14.5]]: $\mathrm{O}(n)$ is compact, being closed (the preimage of $\{I\}$ under the continuous map $g \mapsto g^T g$) and bounded (each column is a unit vector, so every entry satisfies $|g_{ij}| \le 1$) in $\mathbb{R}^{n^2}$; it is Hausdorff and second countable as a subspace of $\mathbb{R}^{n^2}$; and the subgroup $\mathrm{O}(k) \times \mathrm{O}(n-k)$ is compact by the same argument.

^pf-14-8

*Uses:* [[§13 Homogeneous Spaces#^lem-13-5|§13.5]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-6|§14.6]], [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-7|§14.7]], [[§13 Homogeneous Spaces#^lem-13-3|§13.3]], [[§14 The Topology of G∕H and Real Grassmannians#^def-14-2|Def. §14.2]], [[§14 The Topology of G∕H and Real Grassmannians#^cor-14-5|§14.5]], [[§10 Topological Groups and Classical Matrix Groups#^def-10-2|Def. §10.2]], [[§10 Topological Groups and Classical Matrix Groups#^prop-10-5|§10.5]], [[§1 Point-Set Topology Review#^prop-1-8|§1.8]], [[§1 Point-Set Topology Review#^prop-1-6|§1.6]], [[Heine–Borel Theorem]]

> [!remark]- Connections
> - For $k = 1$ the transported topology agrees with the quotient topology of $\mathbb{RP}^{n-1}$: [[§17 Projective Spaces as Smooth Manifolds#^prop-17-6|§17.6]]; $\mathrm{O}(n)$ becomes a smooth manifold in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Ex. §22.1]].

> [!remark] Remark: Dimension Count and What Is Still Missing
> Heuristically, $\dim G/H = \dim G - \dim H$, which with $\dim \mathrm{O}(m) = \tfrac{m(m-1)}{2}$ ([[§11 The Classical Groups Are Topological Manifolds|§11, The Classical Groups Are Topological Manifolds]]) gives
>
> $$
> \dim \mathrm{Gr}_k(\mathbb{R}^n) = \frac{n(n-1)}{2} - \frac{k(k-1)}{2} - \frac{(n-k)(n-k-1)}{2} = k(n-k).
> $$
>
> This is correct, but nothing proved so far shows $\mathrm{Gr}_k(\mathbb{R}^n)$ is locally Euclidean at all: the corollary only supplies the two point-set conditions. Charts on Grassmannians (graphs of linear maps $V_0 \to V_0^\perp$) are Lee Example 1.36, and will make $\mathrm{Gr}_k(\mathbb{R}^n)$ a $k(n-k)$-manifold. For $k = 1$ this is $\mathbb{RP}^{n-1}$, of dimension $n - 1$, consistent with the [[§14 The Topology of G∕H and Real Grassmannians#^rem-14-3|index remark]] above. The picture Uribe drew is $n = 3$, $k = 2$: $V_0$ is the $xy$-plane, $\mathrm{Gr}_2(\mathbb{R}^3)$ is the space of planes through the origin in $\mathbb{R}^3$, and $k(n-k) = 2$.

^rem-14-4

![[m591-7-4.svg]]
*Uribe's picture for $n = 3$, $k = 2$: a point of $\mathrm{Gr}_2(\mathbb{R}^3)$ is a whole plane through the origin. The base point $V_0 = \operatorname{span}(e_1, e_2)$ (blue) is carried by an orthogonal $g$ to another plane $V = gV_0$ (red); two distinct planes through $0$ always share a line (dashed). The isotropy group $\mathrm{O}(2) \times \mathrm{O}(1)$ of [[§14 The Topology of G∕H and Real Grassmannians#^prop-14-7|Proposition §14.7]] consists of the $g$ that move $V_0$ onto itself: an orthogonal map of the plane, together with $e_3 \mapsto \pm e_3$ on the normal line. A plane is pinned down by its unit normal up to sign ($\pm e_3$ for $V_0$, $\pm g e_3$ for $V$), so it takes two parameters to choose one — the count $k(n-k) = 2$.*

> [!remark]- Connections
> - $\dim \mathrm{O}(n) = \tfrac{n(n-1)}{2}$ is proved in [[§22 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-22-1|Ex. §22.1]]; the same subtraction of dimensions for $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ is [[§23 Tangent Spaces I꞉ The Geometric Picture#^rem-23-9|Dimension Checks through Homogeneous Spaces]].
