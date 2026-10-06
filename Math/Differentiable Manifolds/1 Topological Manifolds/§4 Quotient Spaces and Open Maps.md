---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 1
section: 4
tags: [differentiable-manifolds, math591]
---
← [[§3 Subspaces and Products]] · ↑ [[· 1 Topological Manifolds]] · [[§5 Quotient Maps]] →

*Thread: quotients — Manifolds built by gluing and identifying points. The quotient topology, and open maps and open relations — the tool that keeps quotients second countable.*

> [!definition] Definition §4.1: Quotient Space
> Let $X$ be a topological space and $\sim$ an equivalence relation on $X$. Form the **quotient space**
>
> $$
> X/{\sim} \;=\; \{\, [x] \mid x \in X \,\}, \qquad [x] = \{y \in X \mid y \sim x\},
> $$
>
> the set of equivalence classes, with the natural surjection $\pi : X \to X/{\sim}$, $x \mapsto [x]$.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^def-4-1

> [!remark]- Connections
> - Home in MATH 590: [[§13 Quotient Topology#^def-13-3|590 Def. §13.3 (Quotient Space)]].
> - The quotient set $X/{\sim}$ of equivalence classes in 250: [[§22 Partitions and Equivalence Relations#^def-22-6|250 Def. §22.6]]; the classes partition $X$: [[Equivalence Relations Are Partitions|250 Cor. §22.4]].

> [!definition] Definition §4.2: Quotient Topology
> With $X$, $\sim$ and $\pi$ as in [[§4 Quotient Spaces and Open Maps#^def-4-1|Definition §4.1]], the **quotient topology** on $X/{\sim}$ is defined by:
>
> $$
> W \subseteq X/{\sim} \text{ is open} \iff \pi^{-1}(W) \subseteq X \text{ is open in } X.
> $$
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^def-4-2

> [!remark]- Connections
> - Home in MATH 590: the topology of [[§13 Quotient Topology#^prop-13-1|590 §13.1]], [[§13 Quotient Topology#^def-13-2|590 Def. §13.2]].
> - Reused for orbit spaces [[§13 Group Actions and Orbit Spaces#^def-13-5|Def. §13.5]] and coset spaces [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|§15.1]].

> [!theorem] Proposition §4.1: The Quotient Topology Is the Finest Making $\pi$ Continuous
> The projection $\pi : X \to X/{\sim}$ is continuous, and the quotient topology is the *finest* topology on $X/{\sim}$ with this property: every topology $\mathcal{T}'$ on $X/{\sim}$ for which $\pi$ is continuous is contained in it.
>
> *Lee: App. A, Subspaces, Products, Disjoint Unions, and Quotients*

^prop-4-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* If $W$ is open in $X/{\sim}$ then $\pi^{-1}(W)$ is open in $X$ by definition, so $\pi$ is continuous. If $\pi$ is continuous for $\mathcal{T}'$, then every $W \in \mathcal{T}'$ has $\pi^{-1}(W)$ open in $X$, hence $W$ is open in the quotient topology.

^pf-4-1

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]]

> [!remark]- Connections
> - Home in MATH 590: [[§13 Quotient Topology#^rem-13-4|590 §13, The Quotient Topology is the Finest Making p Continuous]].

> [!remark] Remark: How to Read a Quotient
> A quotient space is easy to define and easy to lose track of. Whenever a quotient $X/{\sim}$ appears in these notes, four things are made explicit, and it is worth demanding them of every quotient you meet:
> 1. **What a point is.** A point of $X/{\sim}$ is an equivalence class $[x]$, i.e. a *subset* of $X$. Say which subset.
> 2. **What $\pi$ does.** $\pi(x) = [x]$: it sends a point of $X$ to the class containing it.
> 3. **What the open sets are.** $W \subseteq X/{\sim}$ is open iff $\pi^{-1}(W) = \bigcup_{[x] \in W} [x]$—the union in $X$ of all the classes belonging to $W$—is open in $X$. So the open sets of $X/{\sim}$ correspond exactly to the open subsets of $X$ that are *unions of classes* (the *saturated* open sets, [[§4 Quotient Spaces and Open Maps#Open Maps and Open Relations|§4, Open Maps and Open Relations]]).
> 4. **What an identification does.** When $X/{\sim}$ is identified with a concrete space $Y$ via a bijection $\Phi$, say what $\Phi$ does to a class, and what its inverse does to a point of $Y$.
>
> For the line with two origins ([[§4 Quotient Spaces and Open Maps#^ex-4-1|Example §4.1]]): a point is a pair $\{(x,1), (x,2)\}$ for $x \neq 0$ or a singleton $\{(0,i)\}$; $\pi$ forgets the label except at $0$; a set is open iff its preimage, a union of such pairs and singletons, is open in the two lines; the identification with [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]] sends $\{(x,1),(x,2)\} \mapsto x$ and $\{(0,i)\} \mapsto 0_i$.

^rem-4-1

> [!remark] Remark: Warning: Nothing Is Automatically Inherited
> **Neither $T_2$ nor second countability of $X$ is automatically inherited by $X/{\sim}$.** This is the reason the lecture spends most of its time here: the constructions that produce interesting manifolds are quotients, so we need theorems telling us *when* the quotient is $T_2$ (and second countable) — these properties must be earned, not assumed.

^rem-4-2

> [!example] Example §4.1: Failure of Hausdorffness — the Line with Two Origins as a Quotient
> Let
>
> $$
> X = (\mathbb{R} \times \{1\}) \cup (\mathbb{R} \times \{2\})
> $$
>
> (two disjoint copies of the real line), and define $(x, 1) \sim (x, 2)$ for all $x \neq 0$ — these, together with the relations forced by reflexivity and symmetry, are the only identifications. In particular $(0,1) \not\sim (0,2)$: the two origins survive as distinct points. The quotient space is exactly the real line with two origins of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]], which is not $T_2$ — even though $X$ itself, a disjoint union of two lines, is a metrizable space with every good property one could ask for.
>
> *Lee: Problem 1-1*

^ex-4-1

*Uses:* [[§1 Point-Set Topology Review#^ex-1-4|Ex. §1.4]], [[§4 Quotient Spaces and Open Maps#^prop-4-2|§4.2]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]]

![[m591-3-8.svg]]
*Two copies of $\mathbb{R}$ (blue) glued along every vertical pair $(x,1) \sim (x,2)$ with $x \neq 0$ — except the two origins (red). The glued pairs at $x = \tfrac1n$ crowd in on the unglued pair $\big((0,1),(0,2)\big)$: that is the sequence in $\Gamma$ whose limit escapes $\Gamma$ in [[§10 The Line with Two Origins#^ex-10-1|Example §10.1]], and downstairs it is why every neighbourhood of $0_1$ meets every neighbourhood of $0_2$.*

> [!remark]- Connections
> - The same space: [[§1 Point-Set Topology Review#^ex-1-4|Ex. §1.4]], [[§10 The Line with Two Origins#^rem-10-1|§10, The Line with Two Origins as a Quotient]], [[§2 Topological Manifolds#^ex-2-1|Ex. §2.1]]; via the Hausdorff criterion in [[§10 The Line with Two Origins#^ex-10-1|Ex. §10.1]].
> - A quotient of the Hausdorff $\mathbb{R}$ that is not Hausdorff, in MATH 590: [[§13 Quotient Topology#^ex-13-5|590 Ex. §13.5]].

> [!theorem] Proposition §4.2: The Two Constructions Agree
> The bijection sending the class $\{(x,1),(x,2)\}$ to $x$ for $x \neq 0$ and the class $\{(0,i)\}$ to $0_i$ is a homeomorphism from $X/{\sim}$, with the quotient topology, onto the line with two origins of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]], with the topology generated by the neighborhood bases $(-\varepsilon,0) \cup \{0_i\} \cup (0,\varepsilon)$.

^prop-4-2

> [!proof]+ Exercise
> Set up the bijection as above and check that a subset downstairs is open for one topology iff it is open for the other; by [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|Proposition §15.1]]-style reasoning it is enough to compare the two on the basic sets of [[§1 Point-Set Topology Review#^ex-1-4|Example §1.4]], pulling each back along $\pi$. Assigned in lecture and left here.

^pf-4-2

The line with two origins through the course: defined by its neighbourhood bases, and not Hausdorff, in [[§1 Point-Set Topology Review#^ex-1-4|the real line with two origins]]; second countable and locally Euclidean but not Hausdorff, so not a manifold, in [[§2 Topological Manifolds#^ex-2-1|the line with two origins fails Hausdorff]]; the quotient of two lines in [[§4 Quotient Spaces and Open Maps#^ex-4-1|the line with two origins as a quotient]], the two constructions agreeing by [[§4 Quotient Spaces and Open Maps#^prop-4-2|the two constructions agree]]; and, with its description as a quotient and the Hausdorff criterion for open quotients applied to it, in [[§10 The Line with Two Origins|The Line with Two Origins]].

The single most useful fact about the quotient topology — that a map *out* of a quotient is continuous as soon as its composite with $\pi$ is, and that a map on $X$ constant on the classes descends to one on $X/{\sim}$ — is [[§5 Quotient Maps#^thm-5-1|Theorem §5.1]] below. It is stated in [[§5 Quotient Maps|§5, Quotient Maps]] because its natural generality is quotient maps rather than quotient spaces.

## Open Maps and Open Relations

> [!definition] Definition §4.3: Open Map
> A continuous map $F : X \to Y$ between topological spaces is **open** if for every open $U \subseteq X$, the image $F(U)$ is open in $Y$.

^def-4-3

> [!remark]- Connections
> - Home in MATH 590: [[§13 Quotient Topology#^def-13-4|590 Def. §13.4]].

> [!example] Example §4.2: Projections Are Open
> $\pi_X : X \times Y \to X$ is always an open map.

^ex-4-2

> [!proof]+ Proof (not given in lecture — “go home and check yourself”)
> First, for a basis element: $\pi_X(U \times V) = U$ if $V \neq \emptyset$ (and $= \emptyset$ if $V = \emptyset$), open either way. A general open $A \subseteq X \times Y$ is a union of basis elements, $A = \bigcup_i U_i \times V_i$, and images commute with unions:
>
> $$
> \pi_X(A) = \bigcup_i \pi_X(U_i \times V_i),
> $$
>
> a union of open sets.

^pf-ex-4-2

*Uses:* [[§3 Subspaces and Products#^def-3-3|Def. §3.3]], [[§4 Quotient Spaces and Open Maps#^def-4-3|Def. §4.3]], [[§1 Point-Set Topology Review#^prop-1-1|§1.1]]

> [!definition] Definition §4.4: Open Equivalence Relation
> An equivalence relation $\sim$ on $X$ is **open** if the projection $\pi : X \to X/{\sim}$ is an open map.

^def-4-4

> [!example] Example §4.3: Non-Example
> Let $X = \mathbb{R}$ and let $\sim$ be the equivalence relation generated by the single non-trivial identification $0 \sim 1$ (glue the two points; the quotient looks like a line with a small loop). Take the open set $\left(-\tfrac12, \tfrac12\right)$ and compute the preimage of its image:
>
> $$
> \pi^{-1}\!\left(\pi\!\left(-\tfrac12, \tfrac12\right)\right) = \left(-\tfrac12, \tfrac12\right) \cup \{1\},
> $$
>
> because the identified point $[0] = [1]$ has the *two* preimages $0$ and $1$. This set is not open in $\mathbb{R}$ (no neighborhood of $1$ fits inside), so $\pi\left(-\tfrac12,\tfrac12\right)$ is not open in the quotient, and $\sim$ is not an open relation. Uribe: “I love little examples like this.”

^ex-4-3

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]]

> [!definition] Definition §4.5: Saturation
> Let $\sim$ be an equivalence relation on a set $X$ with quotient map $\pi : X \to X/{\sim}$. For any subset $U \subseteq X$, the **saturation** of $U$ is
>
> $$
> \tilde U \;:=\; \pi^{-1}(\pi(U)) \;=\; \{\, y \in X \mid \exists\, x \in U \text{ such that } y \sim x \,\} \;=\; \bigcup_{x \in U} [x],
> $$
>
> the union of all equivalence classes that meet $U$.

^def-4-5

![[m591-3-3.svg]]
*Saturation for the relation $x \sim y \iff x - y \in \mathbb{Z}$ on $\mathbb{R}$, whose quotient is the circle ([[§15 The Topology of G∕H and Real Grassmannians#^ex-15-1|Example §15.1]]). The saturation of the interval $U$ is the union of all its integer translates, $\pi^{-1}(\pi(U))$: everything the quotient map cannot tell apart from $U$. It is open because each translate is — the mechanism behind “orbit relations are open” ([[§13 Group Actions and Orbit Spaces#^lem-13-3|Lemma §13.3]]) — and its image $\pi(U)$ is an open arc of the circle.*

> [!definition] Definition §4.6: Saturated Set
> Let $\sim$ be an equivalence relation on a set $X$ with quotient map $\pi : X \to X/{\sim}$. A subset $S \subseteq X$ is **saturated** if $S = \tilde S$, its saturation ([[§4 Quotient Spaces and Open Maps#^def-4-5|Definition §4.5]]); equivalently, $S$ is a union of equivalence classes; equivalently, $S = \pi^{-1}(W)$ for some $W \subseteq X/{\sim}$ (namely $W = \pi(S)$).

^def-4-6

> [!remark]- Connections
> - Saturated sets for cosets: [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|§15.1]]; for orbits: [[§13 Group Actions and Orbit Spaces#^lem-13-3|§13.3]].

> [!theorem] Lemma §4.3: Basic Properties of Saturation
> For all $U, V \subseteq X$ and any family $(U_\alpha)$ of subsets:
> 1. $U \subseteq \tilde U$, and $\tilde{\tilde U} = \tilde U$ (the saturation is saturated).
> 2. $U \subseteq V \Rightarrow \tilde U \subseteq \tilde V$, and $\widetilde{\bigcup_\alpha U_\alpha} = \bigcup_\alpha \tilde U_\alpha$.
> 3. $\pi(\tilde U) = \pi(U)$.
> 4. The three descriptions of “saturated” in [[§4 Quotient Spaces and Open Maps#^def-4-6|Definition §4.6]] are equivalent, and for saturated $S$ one has $\pi^{-1}(\pi(S)) = S$.

^lem-4-3

> [!proof]+ Proof
> Write $\tilde U = \bigcup_{x \in U}[x]$. (1) $x \in [x]$ gives $U \subseteq \tilde U$. If $y \in \tilde{\tilde U}$ then $y \sim z$ for some $z \in \tilde U$, so $z \sim x$ for some $x \in U$, and transitivity gives $y \sim x$, i.e. $y \in \tilde U$; with $\tilde U \subseteq \tilde{\tilde U}$ from the first part, equality follows. (2) Both are immediate from $\tilde U = \bigcup_{x \in U}[x]$: enlarging $U$ enlarges the union, and the union over $\bigcup_\alpha U_\alpha$ is the union of the unions. (3) $\pi(\tilde U) \supseteq \pi(U)$ by (1); conversely $\pi(y)$ for $y \in [x]$, $x \in U$, equals $\pi(x) \in \pi(U)$. (4) If $S = \tilde S$ then $S$ is the union of the classes $[x]$, $x \in S$. If $S$ is a union of classes, $S = \bigcup_{[x] \in W}[x]$ for $W = \pi(S)$, then $\pi^{-1}(W) = \{y \mid [y] \in W\} = S$. If $S = \pi^{-1}(W)$ then $\tilde S = \pi^{-1}(\pi(\pi^{-1}(W))) = \pi^{-1}(W) = S$, using $\pi(\pi^{-1}(W)) = W$ (surjectivity of $\pi$).

^pf-4-3

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^def-4-6|Def. §4.6]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]]

> [!theorem] Proposition §4.4: The Saturation Correspondence
> Let $\pi : X \to X/{\sim}$ be the projection. Then $W \mapsto \pi^{-1}(W)$ is a bijection from the subsets of $X/{\sim}$ onto the saturated subsets of $X$, with inverse $S \mapsto \pi(S)$, and it preserves unions, intersections and complements. Under it, the open subsets of $X/{\sim}$ correspond exactly to the saturated open subsets of $X$, and the closed subsets to the saturated closed subsets.
>
> *Lee: Theorem A.27(c)*

^prop-4-4

> [!proof]+ Proof
> *(Lecture 2 defined the saturation and stated that a relation is open exactly when saturations of open sets are open; the proof is filled in.)* Every $\pi^{-1}(W)$ is saturated, and $\pi(\pi^{-1}(W)) = W$ because $\pi$ is surjective. Conversely, a saturated $S$ satisfies $\pi^{-1}(\pi(S)) = S$ by [[§4 Quotient Spaces and Open Maps#^lem-4-3|Lemma §4.3]](4). So the two maps are mutually inverse. Taking preimages commutes with unions, intersections and complements. The open sets of $X/{\sim}$ are by definition those $W$ with $\pi^{-1}(W)$ open, which gives the statement for open sets. For closed sets pass to complements, using that the complement of a saturated set is saturated (it is the union of the remaining classes).

^pf-4-4

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^def-4-6|Def. §4.6]], [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]]

> [!theorem] Proposition §4.5: Openness via Saturations
> $\sim$ is open $\iff$ for every open $U \subseteq X$, the saturation $\tilde U = \pi^{-1}(\pi(U))$ is open in $X$.

^prop-4-5

> [!proof]+ Proof
> $\pi$ is open iff $\pi(U)$ is open in $X/{\sim}$ for every open $U \subseteq X$; and by the definition of the quotient topology, $\pi(U)$ is open in $X/{\sim}$ iff $\pi^{-1}(\pi(U)) = \tilde U$ is open in $X$.

^pf-4-5

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-4|Def. §4.4]], [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]]

> [!remark]- Connections
> - Applied to orbit relations: [[§13 Group Actions and Orbit Spaces#^lem-13-3|Orbit Relations Are Open, §13.3]]; to cosets: [[§15 The Topology of G∕H and Real Grassmannians#^prop-15-1|§15.1]].

In lecture, saturation was named after the proposition, as the set $\pi^{-1}(\pi(U))$ appearing in it; the notion is worth having on its own (it recurs for orbit spaces in [[§13 Group Actions and Orbit Spaces|§13]]), which is why it is defined first here, with its elementary properties.

> [!remark] Remark: In Words
> The saturation of $U$ is $U$ together with everything equivalent to something in $U$ — “you push forward and then take the preimage.” [[§4 Quotient Spaces and Open Maps#^prop-4-5|Proposition §4.5]] then reads as a slogan: *$\sim$ is open iff the saturation of every open set is open.* In the [[§4 Quotient Spaces and Open Maps#^ex-4-3|non-example above]], saturating $\left(-\tfrac12,\tfrac12\right)$ adjoined the isolated point $1$ and destroyed openness. In the [[§9 Complex Projective Space#^prop-9-1|ℂPⁿ example below]], saturating an open set means rotating it in every possible way, which *preserves* openness — that contrast is the whole point of the definition.

^rem-4-3

> [!example] Example §4.4: Failure of Second Countability
> Let $X = \mathbb{R}/{\sim}$ with the quotient topology, where $x \sim y$ iff $x = y$ or both $x, y \in \mathbb{Z}$: all integers are collapsed to a single point $x_0$, and $X$ looks like $x_0$ with countably many loops attached. Then $\mathbb{R}$ is second countable but $X$ is not, because $X$ is not first countable at $x_0$.

^ex-4-4

![[m591-3-2.svg]]
*The diagonal construction in the proof below: each $A_j$ has some radius at every integer, and $W$ is chosen thinner than $A_j$ at the integer $j$, so the marked point $w_j \in A_j$ lies outside $W$.*

> [!proof]+ Proof (PSet 1, Problem 4)
> Write $\pi : \mathbb{R} \to X$, so $\pi^{-1}(x_0) = \mathbb{Z}$ and $\pi^{-1}(\pi(x)) = \{x\}$ for $x \notin \mathbb{Z}$. Two preliminary facts. (i) If $V \subseteq X$ is a neighborhood of $x_0$, then $\pi^{-1}(V)$ is open in $\mathbb{R}$ and contains $\mathbb{Z}$. (ii) If $U \subseteq \mathbb{R}$ is open with $\mathbb{Z} \subseteq U$, then $U$ is saturated—each class is either $\mathbb{Z} \subseteq U$ or a singleton $\{x\} \subseteq U$—so $\pi^{-1}(\pi(U)) = U$ and $\pi(U)$ is a neighborhood of $x_0$ ([[§4 Quotient Spaces and Open Maps#^def-4-6|Definition §4.6]] and [[§4 Quotient Spaces and Open Maps#^lem-4-3|Lemma §4.3]](4)).
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

^pf-ex-4-4

*Uses:* [[§4 Quotient Spaces and Open Maps#^def-4-1|Def. §4.1]], [[§4 Quotient Spaces and Open Maps#^def-4-2|Def. §4.2]], [[§4 Quotient Spaces and Open Maps#^def-4-5|Def. §4.5]], [[§4 Quotient Spaces and Open Maps#^def-4-6|Def. §4.6]], [[§4 Quotient Spaces and Open Maps#^lem-4-3|§4.3]], [[§1 Point-Set Topology Review#^def-1-5|Def. §1.5]], [[§1 Point-Set Topology Review#^def-1-7|Def. §1.7]], [[§1 Point-Set Topology Review#^prop-1-4|§1.4]]

> [!remark]- Connections
> - First and second countability in MATH 590: [[§22 Countability Axioms#^def-22-2|590 Def. §22.2]], [[§22 Countability Axioms#^def-22-3|590 Def. §22.3]].
> - Cited as the use of the contrapositive of [[§1 Point-Set Topology Review#^prop-1-4|§1.4]] in [[§1 Point-Set Topology Review#^rem-1-7|the remark after it]].

> [!remark] Remark: Why the Diagonal
> The mechanism is Cantor's: each candidate $U_j$ is pinned down at the single integer $j$, and $W$ is built to be strictly thinner than $U_j$ exactly there. No countable family can control all of the infinitely many arms at once, because a neighborhood of $x_0$ must specify a radius at *every* integer simultaneously—that is what collapsing infinitely many points to one costs. [[§6 Open Quotients#^thm-6-3|Theorem §6.3]] is not contradicted, because its hypothesis fails: this relation is *not* open. The saturation of the open set $(-\tfrac12, \tfrac12)$, which meets $\mathbb{Z}$ at $0$, is $(-\tfrac12,\tfrac12) \cup \mathbb{Z}$, and that is not open—no neighborhood of the point $1$ is contained in it.

^rem-4-4
