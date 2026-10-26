---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions]] · ↑ [[· CA Mathematical Methods]]

*Sources: the user's PHY 513 notes, Ch. 14 §14.2 (Principle "Vacuum expectation values: complete contractions": the count $(n-1)!!$), §14.5 (Principle "The symmetry factor", Figure "Symmetry factors": the contraction counts), §14.7 (Derivation "The factorization at second order") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.3, p. 89; §4.4, pp. 92–93 · Yu Zhao-Huan, 量子场论讲义, §6.3.1, eqs. (6.167)–(6.168); §7.3, eqs. (7.114)–(7.125); §10.5.1, eqs. (10.194)–(10.196) · the 493 notes (Group Theory) §25–§27, §29–§30, §41, §55 · proofs written here; every count checked by enumeration (`qft-C/tools/l14/enumerate_pairings.py`).*

Wick's theorem turns a vacuum expectation value of free fields into a sum over the ways of grouping the fields in pairs ([[§C6.6 Wick's Theorem|§C6.6]]). Perturbation theory then asks two counting questions: how many pairings give the same formula, and how a sum over pairings splits when some fields are joined to fixed points and others are not. Both are questions about finite sets and permutation groups, with no physics in them. This section answers them. Pairings are counted directly. Relabelling vertices and their legs is a group action, so pairings that give the same diagram form an orbit, and orbit–stabilizer ([[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]]) gives their number in terms of the diagram's automorphism group. The split of a pairing into the part attached to marked points and the rest gives a factorization of weighted sums. The group theory is taken from the 493 notes (actions, orbits, stabilizers, semidirect products, the first isomorphism theorem). Statements are made for vertices with four half-edges, the case used so far.

## Pairings

> [!definition] Definition §CA.7.1: Pairing
> A **pairing** (perfect matching) of a finite set $X$ is a partition of $X$ into blocks of exactly two elements. $\mathcal P(X)$ denotes the set of pairings of $X$; $\mathcal P(\varnothing) = \{\varnothing\}$ (one pairing, with no blocks).
>
> *Source: PS §4.3, p. 89 ("one term for each possible way of contracting the $m$ fields in pairs") · Yu §6.3.1, after eq. (6.166) · the user's PHY 513 notes, Ch. 14 §14.2*

^def-ca-7-1

> [!theorem] Theorem §CA.7.1: The Number of Pairings
> Let $X$ be a finite set.
> 1. If $|X|$ is odd, $\mathcal P(X) = \varnothing$.
> 2. If $|X| = 2k$, then
>
> $$
> |\mathcal P(X)| = (2k - 1)!! \equiv (2k - 1)(2k - 3)\cdots3\cdot1 = \frac{(2k)!}{2^kk!} .
> $$
>
> The first values are $1, 3, 15, 105, 945, 10\,395, 135\,135$ for $2k = 2, 4, \dots, 14$.
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.2 ("The number of terms is $(n-1)!!$: 3 for $n = 4$, 15 for $n = 6$, 105 for $n = 8$") · PS §4.4, p. 92 (135 135 for 14 operators) · Yu §6.3.1, eqs. (6.167)–(6.168) · proof written here*

^thm-ca-7-1

> [!derivation]- Derivation
> **Step 1** (odd sets). The blocks of a pairing are disjoint and each has two elements, so a pairing with $b$ blocks covers $2b$ elements. If $|X|$ is odd, no $b$ gives $2b = |X|$. Part 1.
>
> **Step 2** (the partner of one element). Let $|X| = 2k \ge 2$ and fix $x_0 \in X$. In a pairing $P$, $x_0$ lies in exactly one block $\{x_0, y\}$, $y \ne x_0$. The map
>
> $$
> P \mapsto \bigl(y,\; P \setminus \{\{x_0, y\}\}\bigr)
> $$
>
> sends $\mathcal P(X)$ to the disjoint union over $y \in X \setminus \{x_0\}$ of $\{y\} \times \mathcal P(X \setminus \{x_0, y\})$: removing the block leaves a partition of $X \setminus \{x_0, y\}$ into pairs. Its inverse adds the block $\{x_0, y\}$ back. So it is a bijection, and
>
> $$
> |\mathcal P(X)| = \sum_{y \ne x_0}|\mathcal P(X \setminus \{x_0, y\})| = (2k - 1)\,|\mathcal P(2k - 2\text{ elements})| ,
> $$
>
> because there are $2k - 1$ choices of $y$ and each remaining set has $2k - 2$ elements (the count depends only on the size: a bijection of sets induces one of their pairings).
>
> **Step 3** (induction). $|\mathcal P(\varnothing)| = 1$. If $|\mathcal P| = (2k - 3)!!$ for $2k - 2$ elements, Step 2 gives $(2k - 1)(2k - 3)!! = (2k - 1)!!$.
>
> **Step 4** (closed form). $(2k)! = \prod_{j=1}^{2k}j$ splits into the odd factors, $(2k - 1)!!$, and the even ones, $\prod_{i=1}^k2i = 2^kk!$. So $(2k - 1)!! = (2k)!/(2^kk!)$.
>
> **Step 5** (values). $1, 3, 3\cdot5 = 15, 15\cdot7 = 105, 105\cdot9 = 945, 945\cdot11 = 10\,395, 10\,395\cdot13 = 135\,135$. Enumerating all pairings of $4, 6, 8, 10$ elements gives the same numbers.
>
> **What the derivation shows.**
> - The recursion "choose the partner of the first element, pair the rest" is the order in which contractions are counted by hand.
> - Used in: the vacuum expectation values of Wick's theorem ([[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]]) and the first-order count $15 = 3 + 12$ ([[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-1|Theorem §C6.7.1]]).

^der-ca-7-1

> [!theorem] Lemma §CA.7.2: Permutations Act on Pairings
> For a finite set $X$, the symmetric group $\operatorname{Sym}(X)$ acts on $\mathcal P(X)$ ([[§25 Actions#^def-25-1|493 Def. §25.1]]) by
>
> $$
> g\cdot P = \bigl\{\{g(a), g(b)\} : \{a, b\} \in P\bigr\} .
> $$
>
> So does every subgroup of $\operatorname{Sym}(X)$, and every group with a homomorphism to $\operatorname{Sym}(X)$.
>
> *Source: written here*

^lem-ca-7-2

> [!derivation]- Derivation
> **Step 1** ($g\cdot P$ is a pairing). $g$ is a bijection, so the image of a 2-element set is a 2-element set, images of disjoint sets are disjoint, and the images of the blocks cover $g(X) = X$.
>
> **Step 2** (action law). $e\cdot P = P$. For $g, h$: $g\cdot(h\cdot P) = \{\{g(h(a)), g(h(b))\}\} = (gh)\cdot P$.
>
> **Step 3** (subgroups, homomorphisms). Restricting an action to a subgroup, or composing it with a homomorphism $\rho: G \to \operatorname{Sym}(X)$ ($g\cdot P \equiv \rho(g)\cdot P$), keeps both axioms ([[§25 Actions#^thm-25-3|493 Thm. §25.3]]).

^der-ca-7-2

## Group actions and orbit counting

The counting below uses five statements of the 493 notes, proved there. An action of a group $G$ on a set:

![[§25 Actions#^def-25-1]]

The stabilizer of a point, a subgroup of $G$ ([[§26 Stabilizers and Fixed Points#^prop-26-1|493 Prop. §26.1]]):

![[§26 Stabilizers and Fixed Points#^def-26-1]]

The orbit of a point; the orbits partition the set ([[§27 Orbits#^prop-27-1|493 Prop. §27.1]]):

![[§27 Orbits#^def-27-1]]

Orbit–stabilizer:

![[§30 Orbit–Stabilizer#^thm-30-3]]

Points of one orbit have conjugate, hence equally large, stabilizers:

![[§26 Stabilizers and Fixed Points#^prop-26-2]]

Two more are linked where they are used: the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) with Lagrange's theorem ([[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]), and the external semidirect product ([[§55 Semidirect Products#^def-55-2|493 Def. §55.2]], a group by [[§55 Semidirect Products#^thm-55-5|493 Thm. §55.5]]).

## Labelled diagrams and their symmetry group

> [!definition] Definition §CA.7.2: Labelled Diagram with Vertices of Valence Four
> Let $E$ be a finite set (the **external points**) and $n \ge 0$. The set of **half-edges** is
>
> $$
> X_{E,n} = E \;\sqcup\; \bigl([n] \times \{1, 2, 3, 4\}\bigr), \qquad [n] = \{1, \dots, n\},
> $$
>
> where $(v, a)$ is the $a$-th half-edge at the **vertex** $v$. A **labelled diagram** is a pairing $P \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-1|Def. §CA.7.1]]). Its **multigraph** $\Gamma(P)$ has the nodes $E \sqcup [n]$ and one edge for each block $\{h, h'\}$ of $P$, joining the node of $h$ to the node of $h'$ (the node of $e \in E$ is $e$, that of $(v, a)$ is $v$). Loops (both half-edges at one vertex) and multiple edges are allowed; every external node has degree 1, every vertex degree 4. Write $m_P(u, w)$ for the number of edges between distinct nodes $u, w$ and $\ell_P(v)$ for the number of loops at $v$.
>
> *Source: written here (the half-edge form of PS §4.4, pp. 92–93, and of the user's PHY 513 notes, Ch. 14 §14.5)*

^def-ca-7-2

> [!definition] Definition §CA.7.3: The Relabelling Group
> For $n \ge 0$, let $S_n$ act on $(S_4)^n$ by permuting the factors, $\varphi(\sigma)(\tau)_v = \tau_{\sigma^{-1}(v)}$, and let
>
> $$
> G_n = (S_4)^n \rtimes_\varphi S_n , \qquad (\tau, \sigma)\cdot(\tau', \sigma') = \bigl(\tau\,\varphi(\sigma)(\tau'),\; \sigma\sigma'\bigr)
> $$
>
> be the external semidirect product ([[§55 Semidirect Products#^def-55-2|493 Def. §55.2]]); $|G_n| = n!\,(4!)^n$. It acts on the half-edges $X_{E,n}$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-2|Def. §CA.7.2]]) by
>
> $$
> (\tau, \sigma)\cdot e = e \quad (e \in E), \qquad (\tau, \sigma)\cdot(v, a) = \bigl(\sigma(v),\; \tau_{\sigma(v)}(a)\bigr) :
> $$
>
> permute the vertices, and the half-edges at each vertex, with the external points fixed.
>
> *Source: written here (PS §4.4, p. 92: "interchange of vertices" and "placement of contractions into the vertex")*

^def-ca-7-3

> [!theorem] Lemma §CA.7.3: The Relabelling Group Acts on Half-Edges and on Labelled Diagrams
> The formula of [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-3|Def. §CA.7.3]] is a faithful action of $G_n$ on $X_{E,n}$, and hence ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^lem-ca-7-2|Lemma §CA.7.2]]) an action on the labelled diagrams $\mathcal P(X_{E,n})$.
>
> *Source: written here*

^lem-ca-7-3

> [!derivation]- Derivation
> **Step 1** (identity). The identity of $G_n$ is $(\mathrm{id}, \mathrm{id})$, which fixes every half-edge.
>
> **Step 2** (one element after another). Apply $(\tau', \sigma')$, then $(\tau, \sigma)$, to $(v, a)$:
>
> $$
> (\tau, \sigma)\cdot\bigl(\sigma'(v), \tau'_{\sigma'(v)}(a)\bigr) = \Bigl(\sigma\sigma'(v),\; \tau_{\sigma\sigma'(v)}\,\tau'_{\sigma'(v)}(a)\Bigr) .
> $$
>
> **Step 3** (the product applied once). The product is $(\tau'', \sigma\sigma')$ with $\tau''_w = \tau_w\,\varphi(\sigma)(\tau')_w = \tau_w\,\tau'_{\sigma^{-1}(w)}$. At $w = \sigma\sigma'(v)$, $\sigma^{-1}(w) = \sigma'(v)$, so
>
> $$
> (\tau'', \sigma\sigma')\cdot(v, a) = \Bigl(\sigma\sigma'(v),\; \tau_{\sigma\sigma'(v)}\,\tau'_{\sigma'(v)}(a)\Bigr) ,
> $$
>
> the same as Step 2. External points are fixed by both sides. So the formula is an action.
>
> **Step 4** (faithful). If $(\tau, \sigma)$ fixes every half-edge, then $\sigma(v) = v$ for all $v$ (compare first entries) and $\tau_v(a) = a$ for all $a$, so $(\tau, \sigma)$ is the identity. Distinct elements therefore act differently, and $G_n$ embeds in $\operatorname{Sym}(X_{E,n})$; [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^lem-ca-7-2|Lemma §CA.7.2]] gives the action on pairings.
>
> **What the derivation shows.**
> - The convention $\varphi(\sigma)(\tau)_v = \tau_{\sigma^{-1}(v)}$ is the one that makes "act at the new place of the vertex" compose correctly.

^der-ca-7-3

> [!definition] Definition §CA.7.4: Diagram, Automorphism Group, Symmetry Factor
> For a labelled diagram $P \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-2|Def. §CA.7.2]]):
> 1. its **diagram** is the orbit $G_n\cdot P$ under the relabelling group ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-3|Def. §CA.7.3]]; [[§27 Orbits#^def-27-1|493 Def. §27.1]]);
> 2. its **automorphism group** is the stabilizer $\operatorname{Aut}(P) = \operatorname{Stab}_{G_n}(P)$ ([[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]]);
> 3. its **symmetry factor** is $S(P) = |\operatorname{Aut}(P)|$.
>
> $S$ is the same for all labelled diagrams of one diagram, since their stabilizers are conjugate ([[§26 Stabilizers and Fixed Points#^prop-26-2|493 Prop. §26.2]]); it is the symmetry factor of the diagram.
>
> *Source: PS §4.4, p. 93 ("the number of ways of interchanging components without changing the diagram") · the user's PHY 513 notes, Ch. 14 §14.5 · made precise here*

^def-ca-7-4

> [!theorem] Theorem §CA.7.4: The Number of Labelled Diagrams of One Diagram
> For every $P \in \mathcal P(X_{E,n})$,
>
> $$
> |G_n\cdot P| = \frac{n!\,(4!)^n}{S(P)} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor": $\frac1S = \frac{\text{number of complete contractions that produce the diagram}}{n!\,(4!)^n}$) · proof written here*

^thm-ca-7-4

> [!derivation]- Derivation
> **Step 1** (orbit–stabilizer). $G_n$ is finite and acts on $\mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^lem-ca-7-3|Lemma §CA.7.3]]), so $|G_n| = |G_n\cdot P|\cdot|\operatorname{Stab}_{G_n}(P)|$ ([[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]]).
>
> **Step 2** (insert). $|G_n| = |(S_4)^n|\cdot|S_n| = (4!)^n\,n!$ (the underlying set of the semidirect product is the product set), and $|\operatorname{Stab}(P)| = S(P)$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-4|Def. §CA.7.4]]). Divide.
>
> **Step 3** (example). $E = \{x, y\}$, $n = 1$: $X$ has 6 half-edges and $5!! = 15$ pairings ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-1|Theorem §CA.7.1]]). They form two orbits: the 3 pairings with $\{x, y\}$ a block (the four vertex half-edges paired among themselves) and the 12 with $x$ and $y$ paired to vertex half-edges. $|G_1| = 24$, so the stabilizers have orders $24/3 = 8$ and $24/12 = 2$, as a direct count of the stabilizers (by enumeration over $S_4$) confirms.
>
> **What the derivation shows.**
> - Dividing a sum over all pairings by $n!\,(4!)^n$ leaves $1/S$ per diagram exactly when the summand is constant on orbits.
> - Used in: the coefficient of a Feynman diagram ([[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]]).

^der-ca-7-4

> [!theorem] Theorem §CA.7.5: A Diagram Is Its Multigraph up to Relabelling the Vertices
> Two labelled diagrams $P, P' \in \mathcal P(X_{E,n})$ lie in the same orbit of $G_n$ if and only if there is a permutation $\sigma \in S_n$ of the vertices, extended by the identity on $E$, with
>
> $$
> m_{P'}\bigl(\sigma(u), \sigma(w)\bigr) = m_P(u, w)\quad\text{and}\quad \ell_{P'}\bigl(\sigma(v)\bigr) = \ell_P(v)
> $$
>
> for all nodes $u \ne w$ and all vertices $v$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-2|Def. §CA.7.2]]). So a diagram is determined by its multigraph with the external points labelled and the vertices unlabelled: by its drawing.
>
> *Source: written here (the transcript's test: a diagram is what can be described "to a friend who is not looking at the blackboard", PHY 513 Lecture 14, Part B)*

^thm-ca-7-5

> [!derivation]- Derivation
> **Step 1** (only if). Let $P' = (\tau, \sigma)\cdot P$. A block $\{h, h'\}$ of $P$ joining nodes $u, w$ goes to a block of $P'$ joining $\sigma(u), \sigma(w)$ (the action moves the half-edges of $v$ to half-edges of $\sigma(v)$ and fixes $E$). This is a bijection between the blocks of $P$ and of $P'$, so multiplicities and loop numbers correspond under $\sigma$.
>
> **Step 2** (if: the edges). Assume $\sigma$ as stated. For each unordered pair of distinct nodes $\{u, w\}$ the edges of $\Gamma(P)$ between $u, w$ and those of $\Gamma(P')$ between $\sigma(u), \sigma(w)$ are equally many; choose a bijection between them. Likewise for the loops at $v$ and at $\sigma(v)$.
>
> **Step 3** (if: the half-edges). For an edge $\{h, h'\}$ of $P$ between distinct nodes, sent to the edge $\{k, k'\}$ of $P'$, send the half-edge of $h$ at $u$ to the one of $k$ at $\sigma(u)$ and $h'$ to $k'$. For a loop $\{h, h'\}$ at $v$ sent to the loop $\{k, k'\}$, send $h \mapsto k$, $h' \mapsto k'$. Every half-edge at a vertex $v$ belongs to exactly one block, so this defines a map from the four half-edges of $v$ to half-edges of $\sigma(v)$; it is injective (different blocks go to different blocks) and hence, both sides having four elements, a bijection $\tau_{\sigma(v)}$. External half-edges are fixed, consistently, because the vertex an external point is joined to is mapped by $\sigma$ to the vertex it is joined to in $P'$ ($m$ preserved, $E$ fixed).
>
> **Step 4** (conclude). $(\tau, \sigma)$ maps every block of $P$ to a block of $P'$, so $(\tau, \sigma)\cdot P = P'$.
>
> **What the derivation shows.**
> - Equality of diagrams can be decided on the drawing: count lines between each pair of points and loops at each vertex, up to renaming the vertices.
> - The same construction with $P' = P$ produces the automorphisms above a given vertex permutation (Theorem §CA.7.6).

^der-ca-7-5

> [!theorem] Theorem §CA.7.6: The Symmetry Factor as a Product
> For $P \in \mathcal P(X_{E,n})$ let $\Gamma_P \le S_n$ be the group of vertex permutations $\sigma$ (extended by the identity on $E$) that preserve all multiplicities and loop numbers, $m_P(\sigma u, \sigma w) = m_P(u, w)$, $\ell_P(\sigma v) = \ell_P(v)$. Then
>
> $$
> S(P) = |\Gamma_P|\;\cdot\prod_{\text{vertices } v}2^{\ell_P(v)}\,\ell_P(v)!\;\cdot\prod_{\{u, w\},\,u \ne w}m_P(u, w)! .
> $$
>
> In words: a factor 2 for each loop (its two ends can be exchanged), $k!$ for each set of $k$ loops at one vertex and for each set of $k$ lines joining the same two points, and the number of permutations of the vertices that map the diagram to itself.
>
> *Source: PHY 513 Lecture 14, slides 17–18, and transcript · the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor", "In practice, multiply") · PS §4.4, p. 93 · proof written here*

^thm-ca-7-6

> [!derivation]- Derivation
> **Step 1** (the projection to vertex permutations). $\pi: \operatorname{Aut}(P) \to S_n$, $(\tau, \sigma) \mapsto \sigma$, is a homomorphism (the second component of the semidirect product multiplies as $\sigma\sigma'$, [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-3|Def. §CA.7.3]]).
>
> **Step 2** (the image is $\Gamma_P$). By Step 1 of [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^der-ca-7-5|Derivation §CA.7.5]] with $P' = P$, every $\sigma$ in the image preserves multiplicities and loops. Conversely, for $\sigma \in \Gamma_P$, Steps 2–4 there with $P' = P$ build $(\tau, \sigma) \in \operatorname{Aut}(P)$. So $\pi(\operatorname{Aut}(P)) = \Gamma_P$.
>
> **Step 3** (the kernel). $\ker\pi = \{(\tau, \mathrm{id}) : (\tau, \mathrm{id})\cdot P = P\}$: half-edge permutations at fixed vertices preserving the blocks. Such a $\tau$ maps each edge to an edge with the same end nodes. Count the choices bundle by bundle:
> - a bundle of $m$ edges between two distinct vertices $u, w$: $\tau_u$ may permute the $m$ half-edges of the bundle at $u$ in $m!$ ways, and then $\tau_w$ on the bundle's half-edges at $w$ is forced (each edge must go to an edge); $m!$;
> - an edge from an external point $e$ to $v$: $e$ is fixed, so the half-edge at $v$ is fixed; $1 = 1!$;
> - the $\ell$ loops at $v$: their $2\ell$ half-edges may be permuted in any way that maps loops to loops: choose where the loops go ($\ell!$) and, for each, which end goes to which ($2^\ell$); $2^\ell\ell!$.
>
> The choices for different bundles are independent (they act on disjoint sets of half-edges, and every half-edge lies in exactly one bundle), so $|\ker\pi| = \prod_v2^{\ell(v)}\ell(v)!\prod_{u \ne w}m(u, w)!$.
>
> **Step 4** (count). By the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) $\operatorname{Aut}(P)/\ker\pi \cong \Gamma_P$, and by Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]) $|\operatorname{Aut}(P)| = |\Gamma_P|\cdot|\ker\pi|$.
>
> ⚑ By-product: the factor $k!$ applies to $k$ loops at one vertex as well as to $k$ lines between two vertices. The figure-eight needs both: $2\cdot2$ for the two loops and $2!$ for exchanging them, $S = 8$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^ex-ca-7-1|Example §CA.7.1]]).
>
> **What the derivation shows.**
> - The rule of thumb of the slides is exact: the symmetry factor is the product of independent local symmetries (loops, bundles) times the global symmetry of the vertex arrangement.
> - Checked against a brute-force count of stabilizers in $G_1$ and $G_2$ for every diagram with $n \le 2$ and $E = \varnothing$ or $\{x, y\}$.

^der-ca-7-6

*Uses:* [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-5|Theorem §CA.7.5]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]

> [!example] Example §CA.7.1: Symmetry Factors from the Product Formula
> Each line: the diagram, $S$ by [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-6|Theorem §CA.7.6]], and the size of its orbit by [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-4|Theorem §CA.7.4]], each confirmed by enumerating the pairings.
> - $n = 1$, $E = \{x, y\}$, $|G_1| = 24$. *Tadpole* ($x$–$v$, $v$–$y$, one loop at $v$): $S = 2$, orbit 12. *Line times figure-eight* ($x$–$y$, two loops at $v$): $S = 2^2\cdot2! = 8$, orbit 3. $12 + 3 = 15 = 5!!$.
> - $n = 1$, $E = \varnothing$. *Figure-eight*: $S = 8$, orbit $3 = 3!!$.
> - $n = 2$, $E = \varnothing$, $|G_2| = 2\cdot24^2 = 1152$. *Melon* (four lines between the two vertices): $S = 2\cdot4! = 48$ (the vertex swap is in $\Gamma_P$), orbit 24. *Dumbbell* (one loop at each vertex, two lines between them): $S = 2\cdot(2\cdot1!)^2\cdot2! = 16$, orbit 72. *Two figure-eights*: $S = 2\cdot(2^2\cdot2!)^2 = 128$, orbit 9. Together $24 + 72 + 9 = 105 = 7!!$: every pairing of the eight half-edges is one of these three diagrams.
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5 (Figure "Symmetry factors": "12 of 4!", "3 of 4!", "24 of $2\cdot4!^2$", "72", "9") · PHY 513 Lecture 14, slide 18 · checked with `qft-C/tools/l14/enumerate_pairings.py`*

^ex-ca-7-1

## Splitting a pairing at the external points

> [!definition] Definition §CA.7.5: Attached Vertex; Attached Labelled Diagram
> Let $P \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-2|Def. §CA.7.2]]). A vertex $v$ is **attached** if the multigraph $\Gamma(P)$ contains a path from $v$ to some external point. $P$ is **attached** if every vertex is attached; $\mathcal P_{\rm att}(X_{E,n})$ denotes the attached labelled diagrams. (For $n = 0$ every pairing of $E$ is attached; for $E = \varnothing$ and $n \ge 1$ none is.)
>
> *Source: written here (PS §4.4, p. 98: "disconnected from all external points"; Yu §10.5.1, after eq. (10.192): diagrams with every vertex connected to the external points)*

^def-ca-7-5

> [!theorem] Theorem §CA.7.7: Splitting a Pairing at the External Points
> For $P \in \mathcal P(X_{E,n})$ let $A(P) \subseteq [n]$ be its set of vertices that are not attached ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^def-ca-7-5|Def. §CA.7.5]]), $P_{\rm att}$ the set of its blocks contained in $E \sqcup (([n]\setminus A)\times[4])$, and $P_{\rm vac}$ the set of its blocks contained in $A\times[4]$. Then
>
> $$
> P \longmapsto \bigl(A(P),\, P_{\rm att},\, P_{\rm vac}\bigr)
> $$
>
> is a bijection
>
> $$
> \mathcal P(X_{E,n}) \;\longrightarrow\; \bigsqcup_{A \subseteq [n]}\;\mathcal P_{\rm att}\bigl(E \sqcup (([n]\setminus A)\times[4])\bigr) \times \mathcal P\bigl(A\times[4]\bigr) .
> $$
>
> *Source: Yu §10.5.1, eq. (10.194) (second step: the full contractions split into a part containing the external points and a vacuum part) · stated as a bijection and proved here*

^thm-ca-7-7

> [!derivation]- Derivation
> **Step 1** (no block joins the two parts). If a block joined a half-edge at an attached vertex (or an external point) to a half-edge at $v \in A$, its edge would extend a path to $E$ to $v$, and $v$ would be attached. So every block lies inside $E \sqcup (([n]\setminus A)\times[4])$ or inside $A\times[4]$: $P = P_{\rm att}\sqcup P_{\rm vac}$, and the two are pairings of these two sets.
>
> **Step 2** ($P_{\rm att}$ is attached). Every vertex outside $A$ has a path to $E$ in $\Gamma(P)$; the path never enters $A$ (a vertex of $A$ on it would be attached), so it uses only blocks of $P_{\rm att}$. The image lies in the stated set.
>
> **Step 3** (inverse). Given $A$, an attached pairing $Q$ of $E \sqcup (([n]\setminus A)\times[4])$ and any pairing $R$ of $A\times[4]$, let $P = Q \sqcup R$, a pairing of $X_{E,n}$. In $\Gamma(P)$ the vertices of $A$ are joined only among themselves (blocks of $R$), so they have no path to $E$; every other vertex has one through $Q$. Hence $A(P) = A$, $P_{\rm att} = Q$, $P_{\rm vac} = R$. Conversely $P = P_{\rm att}\sqcup P_{\rm vac}$ (Step 1). The two maps are inverse.
>
> **What the derivation shows.**
> - A pairing is uniquely "the part that touches the external points" together with "a vacuum part", and the vacuum part may sit on any subset of the vertices.

^der-ca-7-7

> [!theorem] Theorem §CA.7.8: Factorization of Sums over Pairings
> Let $R$ be a commutative ring and, for each $k \ge 0$, $f_k$ a function on $\mathcal P(X_{E,k})$ with values in $R$. Suppose there are functions $a_i$ on $\mathcal P_{\rm att}(X_{E,i})$ and $b_j$ on $\mathcal P(X_{\varnothing,j})$ such that for every $P$, with $A = A(P)$, $|A| = j$ ([[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-7|Theorem §CA.7.7]]),
>
> $$
> f_k(P) = a_{k-j}\bigl(\rho_A P_{\rm att}\bigr)\;b_j\bigl(\rho'_AP_{\rm vac}\bigr) ,
> $$
>
> where $\rho_A$, $\rho'_A$ rename the vertices of $[k]\setminus A$ and of $A$ by the order-preserving bijections onto $[k - j]$ and $[j]$. Then, in the ring of formal power series $R[\![t]\!]$,
>
> $$
> \sum_{k\ge0}\frac{t^k}{k!}\sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \Bigl(\sum_{i\ge0}\frac{t^i}{i!}\sum_{Q\in\mathcal P_{\rm att}(X_{E,i})}a_i(Q)\Bigr)\Bigl(\sum_{j\ge0}\frac{t^j}{j!}\sum_{R'\in\mathcal P(X_{\varnothing,j})}b_j(R')\Bigr) .
> $$
>
> *Source: Yu §10.5.1, eqs. (10.194)–(10.196) (the same argument for the vacuum expectation values of $\phi^4$ theory) · stated for pairings and proved here*

^thm-ca-7-8

> [!derivation]- Derivation
> **Step 1** (split). By [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-7|Theorem §CA.7.7]],
>
> $$
> \sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \sum_{A\subseteq[k]}\;\sum_{Q}\;\sum_{R}a_{k-|A|}(\rho_AQ)\,b_{|A|}(\rho'_AR) ,
> $$
>
> with $Q$ over the attached pairings of $E \sqcup (([k]\setminus A)\times[4])$ and $R$ over the pairings of $A\times[4]$.
>
> **Step 2** (rename). Renaming vertices by $\rho_A$ is a bijection from the attached pairings of $E \sqcup (([k]\setminus A)\times[4])$ onto $\mathcal P_{\rm att}(X_{E,k-j})$ (attachment is a property of the multigraph and survives renaming), and $\rho'_A$ is a bijection from $\mathcal P(A\times[4])$ onto $\mathcal P(X_{\varnothing,j})$. So for $|A| = j$ the double sum equals $\alpha_{k-j}\beta_j$, with $\alpha_i = \sum_{\mathcal P_{\rm att}(X_{E,i})}a_i$ and $\beta_j = \sum_{\mathcal P(X_{\varnothing,j})}b_j$, independently of which $A$.
>
> **Step 3** (count the subsets). There are $\binom kj$ subsets with $|A| = j$:
>
> $$
> \sum_{P\in\mathcal P(X_{E,k})}f_k(P) = \sum_{j=0}^k\binom kj\alpha_{k-j}\beta_j .
> $$
>
> **Step 4** (the factorials). $\frac{1}{k!}\binom kj = \frac{1}{(k-j)!\,j!}$. So the coefficient of $t^k$ on the left is $\sum_{i+j=k}\frac{\alpha_i}{i!}\frac{\beta_j}{j!}$, which is the coefficient of $t^k$ of the product on the right (the product of formal power series, the Cauchy product; no convergence is involved).
>
> ⚑ Check: with all functions equal to 1 and $E = \{x, y\}$, the identity says $(4k+1)!! = \sum_j\binom kj\,|\mathcal P_{\rm att}(X_{E,k-j})|\,(4j-1)!!$; for $k = 1$: $15 = 12 + 1\cdot3$, the 12 tadpole pairings and the 3 with a figure-eight. Enumeration confirms it for $k = 1, 2, 3$.
>
> **What the derivation shows.**
> - The $\frac{1}{k!}$ of an exponential series is exactly what turns the choice of which vertices are "vacuum" into a product.
> - Only renaming and the split were used; nothing about the values of $a$ and $b$.
> - Used in: the cancellation of vacuum bubbles to all orders ([[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-4|Theorem §C6.11.4]]).

^der-ca-7-8

*Uses:* [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-7|Theorem §CA.7.7]]

<!-- HELD until Problem Set 8 is submitted (Nov 1; qft-C/HOLD-PS8.md, user decision D3): Theorem §CA.7.9 The exponential formula (sum over diagrams whose components are all vacuum diagrams, weighted 1/S, = exp of the sum over connected vacuum diagrams; S of n_i identical copies = n_i! S_i^{n_i}) and its corollary PS (4.52). Insert here, before the remarks. -->

> [!remark] Remark: Sums over pairings as sums over diagrams
> If a function $f$ on $\mathcal P(X_{E,n})$ is constant on the orbits of $G_n$, then by [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-4|Theorem §CA.7.4]]
>
> $$
> \frac{1}{n!\,(4!)^n}\sum_{P\in\mathcal P(X_{E,n})}f(P) = \sum_{\text{diagrams }D}\frac{f(D)}{S(D)} ,
> $$
>
> the sum on the right over the orbits, $f(D)$ the common value. This is the whole content of "divide by the symmetry factor": the prefactor $\frac{1}{n!}\bigl(\frac{1}{4!}\bigr)^n$ of perturbation theory cancels the size of the group, and each diagram keeps $1/|\operatorname{Aut}|$.
>
> *Source: written here*

^rem-ca-7-1

> [!remark]- ★ Remark: The same sum is the moment formula of a Gaussian
> For a centred Gaussian random vector $\xi = (\xi_1, \dots, \xi_{2k})$ with covariance $C_{ij} = \mathbb E[\xi_i\xi_j]$, $\mathbb E[\xi_1\cdots\xi_{2k}] = \sum_{P\in\mathcal P([2k])}\prod_{\{i,j\}\in P}C_{ij}$ and odd moments vanish (Isserlis' theorem). The vacuum values of Wick's theorem have the same form with $C = D_F$ ([[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]]); in the path integral they *are* Gaussian moments ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|§C2b.6, Remark: Preview: the propagator as a Gaussian covariance]]; QFT C11, planned). Not used in the course at this stage.
>
> *Source: L. Isserlis, Biometrika 12 (1918) 134 (stated, not proved here) · Gaussian integrals: [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]]*

^rem-ca-7-2

> [!remark]- Connections
> - Counting pairings is counting the terms of a vacuum expectation value of free fields; $(2k-1)!!$ grows like $\sqrt2\,(2k/e)^k$, which is why perturbation theory is organized by diagrams rather than by terms — [[§CA.7 Pairings, Graph Symmetries and the Exponential Formula#^thm-ca-7-1|Theorem §CA.7.1]], [[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]].
> - The symmetry factor is a stabilizer order, and "divide by $S$" is orbit–stabilizer in disguise; the same counting gives the class equation and Burnside's lemma in group theory — [[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]], [[§30 Orbit–Stabilizer#^thm-30-6|493 Thm. §30.6]].
> - The relabelling group $(S_4)^n \rtimes S_n$ is a wreath product; the 493 notes construct the semidirect product it is built from — [[§55 Semidirect Products#^def-55-2|493 Def. §55.2]].
> - The ordered simplex of [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]] produced the $\frac{1}{n!}$ of the Dyson series; here the same $\frac{1}{n!}$ meets the $n!$ relabellings of the vertices — [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]].
> - **Used in** (C6 places): Theorem §CA.7.1 — the vacuum values of Wick's theorem and the first-order count ([[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]], [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-1|Theorem §C6.7.1]]); Definitions §CA.7.2–§CA.7.4, Lemma §CA.7.3, Theorems §CA.7.4–§CA.7.5 — the coefficient $1/S$ and the position-space rules ([[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]], [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-2|Theorem §C6.8.2]]); Theorem §CA.7.6 and Example §CA.7.1 — the symmetry factors in practice ([[§C6.9 Symmetry Factors in Practice|§C6.9]]); Theorems §CA.7.7–§CA.7.8 — the factorization of the numerator and the cancellation of vacuum bubbles ([[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-4|Theorem §C6.11.4]], [[§C6.11 The iε Limit and Vacuum Bubbles#^thm-c6-11-5|Theorem §C6.11.5]]).
