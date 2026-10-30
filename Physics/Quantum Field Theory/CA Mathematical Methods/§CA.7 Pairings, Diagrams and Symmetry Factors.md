---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CA
section: CA.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions]] · ↑ [[· CA Mathematical Methods]] · [[§CA.8 Splitting Pairings and the Exponential Formula]] →

*Sources: the user's PHY 513 notes, Ch. 14 §14.2 (Principle "Vacuum expectation values: complete contractions": the count $(n-1)!!$), §14.5 (Principle "The symmetry factor", Figure "Symmetry factors": the contraction counts) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.3, p. 89; §4.4, pp. 92–93 · Yu Zhao-Huan, 量子场论讲义, §6.3.1, eqs. (6.167)–(6.168); §7.3, eqs. (7.114)–(7.125) · the 493 notes (Group Theory) §25–§27, §29–§30, §41, §55 · the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §1–§5, §7 · proofs written here; every count checked by enumeration (`qft-C/tools/l14/enumerate_pairings.py`).*

Wick's theorem turns a vacuum expectation value of free fields into a sum over the ways of grouping the fields in pairs ([[§C6.6 Wick's Theorem|§C6.6]]). Perturbation theory then asks two counting questions: how many pairings give the same formula, and how a sum over pairings splits when some fields are joined to fixed points and others are not. Both are questions about finite sets and permutation groups, with no physics in them. This section answers the first; the second is answered in [[§CA.8 Splitting Pairings and the Exponential Formula|§CA.8]]. Pairings are counted directly. Relabelling vertices and their legs is a group action, so pairings that give the same diagram form an orbit, and orbit–stabilizer ([[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]]) gives their number in terms of the diagram's automorphism group. The group theory is taken from the 493 notes (actions, orbits, stabilizers, semidirect products, the first isomorphism theorem). Statements are made for vertices with four half-edges, the case used so far.

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
> **Step 1** (odd sets). The blocks of a pairing are disjoint and each has two elements, so a pairing with $b$ blocks covers $2b$ elements:
>
> $$
> |X| = \sum_{B\in P}|B| = 2b .
> $$
>
> If $|X|$ is odd, no $b$ gives $2b = |X|$. Part 1.
>
> **Step 2** (the partner of one element). Let $|X| = 2k \ge 2$ and fix $x_0 \in X$. In a pairing $P$, $x_0$ lies in exactly one block $\{x_0, y\}$, $y \ne x_0$. The map
>
> $$
> \Phi:\ P \mapsto \bigl(y,\; P \setminus \{\{x_0, y\}\}\bigr), \qquad \Phi:\ \mathcal P(X) \to \bigsqcup_{y \in X\setminus\{x_0\}}\{y\}\times\mathcal P(X \setminus \{x_0, y\}),
> $$
>
> is well defined (removing the block leaves a partition of $X \setminus \{x_0, y\}$ into pairs), and $\Psi(y, Q) = Q \cup \{\{x_0, y\}\}$ is its inverse: $\Psi\Phi(P) = P$ and $\Phi\Psi(y, Q) = (y, Q)$. So it is a bijection, and
>
> $$
> |\mathcal P(X)| = \sum_{y \ne x_0}|\mathcal P(X \setminus \{x_0, y\})| = (2k - 1)\,|\mathcal P(2k - 2\text{ elements})| ,
> $$
>
> because there are $2k - 1$ choices of $y$ and each remaining set has $2k - 2$ elements (the count depends only on the size: a bijection of sets induces one of their pairings). For $X = \{1, 2, 3, 4\}$, $x_0 = 1$:
>
> $$
> \{\{1,2\},\{3,4\}\} \mapsto \bigl(2, \{\{3,4\}\}\bigr), \qquad \{\{1,3\},\{2,4\}\} \mapsto \bigl(3, \{\{2,4\}\}\bigr), \qquad \{\{1,4\},\{2,3\}\} \mapsto \bigl(4, \{\{2,3\}\}\bigr) :
> $$
>
> $3 = 3\cdot|\mathcal P(2\text{ elements})| = 3\cdot1$.
>
> **Step 3** (induction). $|\mathcal P(\varnothing)| = 1$. If $|\mathcal P| = (2k - 3)!!$ for $2k - 2$ elements, Step 2 gives $(2k - 1)(2k - 3)!! = (2k - 1)!!$.
>
> **Step 4** (closed form). $(2k)! = \prod_{j=1}^{2k}j$ splits into the odd factors and the even ones:
>
> $$
> (2k)! = \underbrace{1\cdot3\cdots(2k - 1)}_{(2k-1)!!}\cdot\underbrace{2\cdot4\cdots2k}_{\prod_{i=1}^k2i\,=\,2^kk!}, \qquad\text{e.g. } 6! = 720 = (1\cdot3\cdot5)(2\cdot4\cdot6) = 15\cdot48,\ 48 = 2^3\cdot3! .
> $$
>
> So $(2k - 1)!! = (2k)!/(2^kk!)$.
>
> **Step 5** (values). $1, 3, 3\cdot5 = 15, 15\cdot7 = 105, 105\cdot9 = 945, 945\cdot11 = 10\,395, 10\,395\cdot13 = 135\,135$. Enumerating all pairings of $4, 6, 8, 10$ elements gives the same numbers.
>
> **What the derivation shows.**
> - The recursion "choose the partner of the first element, pair the rest" is the order in which contractions are counted by hand.
> - Used in: the vacuum expectation values of Wick's theorem ([[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]]) and the first-order count $15 = 3 + 12$ ([[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-1|Theorem §C6.7.1]]).

^der-ca-7-1

![[ph-qft-ca-7-2.svg]]
*Pairings ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]) drawn as arcs. (a) The three pairings of four points. (b) The step of the proof of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]: the partner of the first point has $2k-1$ choices, and the remaining $2k-2$ points are paired in $(2k-3)!!$ ways, here $5\cdot3 = 15$. (c) An odd set has no pairing.*

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
> **Step 1** ($g\cdot P$ is a pairing). $g$ is a bijection, so for blocks $\{a, b\} \ne \{c, d\}$ of $P$:
>
> $$
> a \ne b \Rightarrow g(a) \ne g(b), \qquad \{a, b\}\cap\{c, d\} = \varnothing \Rightarrow \{g(a), g(b)\}\cap\{g(c), g(d)\} = \varnothing, \qquad \bigcup_{\{a,b\}\in P}\{g(a), g(b)\} = g(X) = X .
> $$
>
> For example, $g = (1\,2\,3)$ on $X = \{1, 2, 3, 4\}$: $g\cdot\{\{1,2\},\{3,4\}\} = \{\{2,3\},\{1,4\}\}$.
>
> **Step 2** (action law). $e\cdot P = P$. For $g, h$:
>
> $$
> g\cdot(h\cdot P) = \bigl\{\{g(h(a)), g(h(b))\} : \{a, b\}\in P\bigr\} = (gh)\cdot P .
> $$
>
> **Step 3** (subgroups, homomorphisms). Restricting an action to a subgroup, or composing it with a homomorphism $\rho: G \to \operatorname{Sym}(X)$ ($g\cdot P \equiv \rho(g)\cdot P$, so $g\cdot(h\cdot P) = \rho(g)\rho(h)\cdot P = \rho(gh)\cdot P$), keeps both axioms ([[§25 Actions#^thm-25-3|493 Thm. §25.3]]).

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

Two more are linked where they are used: the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) with Lagrange's theorem ([[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]), and the external semidirect product ([[§56 Semidirect Products#^def-56-2|493 Def. §56.2]], a group by [[§56 Semidirect Products#^thm-56-5|493 Thm. §56.5]]).

## Labelled diagrams and their symmetry group

> [!definition] Definition §CA.7.2: Labelled Diagram with Vertices of Valence Four
> Let $E$ be a finite set (the **external points**) and $n \ge 0$. The set of **half-edges** is
>
> $$
> X_{E,n} = E \;\sqcup\; \bigl([n] \times \{1, 2, 3, 4\}\bigr), \qquad [n] = \{1, \dots, n\},
> $$
>
> where $(v, a)$ is the $a$-th half-edge at the **vertex** $v$. A **labelled diagram** is a pairing $P \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-1|Def. §CA.7.1]]). Its **multigraph** $\Gamma(P)$ has the nodes $E \sqcup [n]$ and one edge for each block $\{h, h'\}$ of $P$, joining the node of $h$ to the node of $h'$ (the node of $e \in E$ is $e$, that of $(v, a)$ is $v$). Loops (both half-edges at one vertex) and multiple edges are allowed; every external node has degree 1, every vertex degree 4. Write $m_P(u, w)$ for the number of edges between distinct nodes $u, w$ and $\ell_P(v)$ for the number of loops at $v$.
>
> *Source: written here (the half-edge form of PS §4.4, pp. 92–93, and of the user's PHY 513 notes, Ch. 14 §14.5)*

^def-ca-7-2

![[ph-qft-ca-7-3.svg]]
*Half-edges and a labelled diagram ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]) for $E = \{x_1, x_2\}$, $n = 2$. (a) The ten half-edges: two external points and four legs at each vertex. (b) One labelled diagram $P$, a pairing of them. (c) Its multigraph $\Gamma(P)$, which forgets which leg is used.*

> [!definition] Definition §CA.7.3: The Relabelling Group
> For $n \ge 0$, let $S_n$ act on $(S_4)^n$ by permuting the factors, $\varphi(\sigma)(\tau)_v = \tau_{\sigma^{-1}(v)}$, and let
>
> $$
> G_n = (S_4)^n \rtimes_\varphi S_n , \qquad (\tau, \sigma)\cdot(\tau', \sigma') = \bigl(\tau\,\varphi(\sigma)(\tau'),\; \sigma\sigma'\bigr)
> $$
>
> be the external semidirect product ([[§56 Semidirect Products#^def-56-2|493 Def. §56.2]]); $|G_n| = n!\,(4!)^n$. It acts on the half-edges $X_{E,n}$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]) by
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
> The formula of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]] is a faithful action of $G_n$ on $X_{E,n}$, and hence ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-2|Lemma §CA.7.2]]) an action on the labelled diagrams $\mathcal P(X_{E,n})$.
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
> **Step 4** (faithful). If $(\tau, \sigma)$ fixes every half-edge, then $\sigma(v) = v$ for all $v$ (compare first entries) and $\tau_v(a) = a$ for all $a$, so $(\tau, \sigma)$ is the identity. Distinct elements therefore act differently, and $G_n$ embeds in $\operatorname{Sym}(X_{E,n})$; [[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-2|Lemma §CA.7.2]] gives the action on pairings.
>
> **What the derivation shows.**
> - The convention $\varphi(\sigma)(\tau)_v = \tau_{\sigma^{-1}(v)}$ is the one that makes "act at the new place of the vertex" compose correctly.

^der-ca-7-3

> [!definition] Definition §CA.7.4: Diagram, Automorphism Group, Symmetry Factor
> For a labelled diagram $P \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]):
> 1. its **diagram** is the orbit $G_n\cdot P$ under the relabelling group ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]; [[§27 Orbits#^def-27-1|493 Def. §27.1]]);
> 2. its **automorphism group** is the stabilizer $\operatorname{Aut}(P) = \operatorname{Stab}_{G_n}(P)$ ([[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]]);
> 3. its **symmetry factor** is $S(P) = |\operatorname{Aut}(P)|$.
>
> $S$ is the same for all labelled diagrams of one diagram, since their stabilizers are conjugate ([[§26 Stabilizers and Fixed Points#^prop-26-2|493 Prop. §26.2]]); it is the symmetry factor of the diagram. That the orbit and the stabilizer are the isomorphism class and the automorphism group of the graph is shown next ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-5|Def. §CA.7.5]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-4|Theorem §CA.7.4]]).
>
> *Source: PS §4.4, p. 93 ("the number of ways of interchanging components without changing the diagram") · the user's PHY 513 notes, Ch. 14 §14.5 · made precise here*

^def-ca-7-4

![[ph-qft-ca-7-4.svg]]
*The relabelling group ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]) acting on one labelled diagram $P$. (a) A leg permutation that maps $P$ to itself: an automorphism ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]]). (b), (c) A leg permutation and a vertex permutation that change $P$ but not its drawing: they move $P$ inside its orbit, the diagram. Orbit–stabilizer gives the count at the bottom ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]]).*

> [!definition] Definition §CA.7.5: Isomorphism of Labelled Diagrams
> Let $P, Q \in \mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]). Regard $P$ as a graph with half-edges: nodes $E \sqcup [n]$, half-edges $X_{E,n}$, each half-edge $h$ attached to its node $\nu(h)$,
>
> $$
> \nu(e) = e \quad (e \in E), \qquad \nu\bigl((v, a)\bigr) = v ,
> $$
>
> and one edge for each block $\{h, h'\}$ of $P$, formed by joining $h$ and $h'$. An **isomorphism** $P \to Q$ is a pair $(g, \bar g)$ of a bijection $g$ of $X_{E,n}$ and a bijection $\bar g$ of $E \sqcup [n]$ such that
> 1. $\bar g(e) = e$ for every $e \in E$;
> 2. $\nu(g(h)) = \bar g(\nu(h))$ for every half-edge $h$: the half-edges at a node go to the half-edges at its image;
> 3. $\bigl\{\{g(h), g(h')\} : \{h, h'\} \in P\bigr\} = Q$: edges go to edges.
>
> An isomorphism $P \to P$ is an **automorphism of the graph** $\Gamma(P)$; under composition they form a group $\operatorname{Aut}(\Gamma(P))$. $P$ and $Q$ **give the same Feynman diagram** if there is an isomorphism $P \to Q$.
>
> *Source: the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §4, Definition "Feynman graph of a pairing" (there written $\Gamma_P$; here $\Gamma(P)$, since $\Gamma_P$ is the vertex group of Theorem §CA.7.9; the note's slots $\mathcal M$ are $X_{E,n}$, its $k$ vertices are $n$, its relabelling group $G$ is the image of $G_n$)*

^def-ca-7-5

> [!theorem] Theorem §CA.7.4: Diagrams Are Orbits, Graph Automorphisms Are Stabilizers
> For $P, Q \in \mathcal P(X_{E,n})$, an isomorphism $(g, \bar g): P \to Q$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-5|Def. §CA.7.5]]) is determined by $g$, and the maps $g$ that occur are exactly the actions of the elements $(\tau, \sigma) \in G_n$ with $(\tau, \sigma)\cdot P = Q$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]). Hence:
> 1. $P$ and $Q$ give the same Feynman diagram if and only if $Q \in G_n\cdot P$; the Feynman diagrams are the orbits, the diagrams of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]];
> 2. $\operatorname{Aut}(\Gamma(P)) \cong \operatorname{Stab}_{G_n}(P) = \operatorname{Aut}(P)$, so $S(P) = |\operatorname{Aut}(\Gamma(P))|$.
>
> Theorem §CA.7.8 (below) decides part 1 on the multigraph alone, by the multiplicities $m_P$ and loop numbers $\ell_P$ up to a permutation of the vertices.
>
> *Source: the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §4, Proposition "Diagrams are orbits" · proof written out here*

^thm-ca-7-4

> [!derivation]- Derivation
> **Step 1** ($\bar g$ is determined by $g$). Every node carries a half-edge: $e$ carries $e$, and $v$ carries $(v, 1), \dots, (v, 4)$. Condition 2 at these half-edges gives
>
> $$
> \bar g(e) = \bar g(\nu(e)) = \nu(g(e)), \qquad \bar g(v) = \bar g\bigl(\nu(v, 1)\bigr) = \nu\bigl(g(v, 1)\bigr) .
> $$
>
> **Step 2** (conditions 1–2 say $g \in G_n$). *External points.* By 1 and 2, $\nu(g(e)) = \bar g(e) = e$; the only half-edge at the node $e$ is $e$, so $g(e) = e$. *Vertices.* $\bar g$ is a bijection fixing $E$ pointwise, so it permutes $[n]$: $\bar g|_{[n]} = \sigma \in S_n$. By 2, $g$ maps the four half-edges at $v$ to half-edges at $\sigma(v)$, injectively, hence onto the four half-edges at $\sigma(v)$:
>
> $$
> g(v, a) = \bigl(\sigma(v),\ \tau_{\sigma(v)}(a)\bigr), \qquad \tau_{\sigma(v)} \in S_4 \text{ unique},
> $$
>
> which is the action of $(\tau, \sigma) \in G_n$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]). Conversely, for $(\tau, \sigma) \in G_n$ put $g = (\tau, \sigma)\cdot(-)$ and $\bar g = \mathrm{id}_E \sqcup \sigma$:
>
> $$
> \nu\bigl(g(e)\bigr) = e = \bar g(e), \qquad \nu\bigl(g(v, a)\bigr) = \sigma(v) = \bar g\bigl(\nu(v, a)\bigr) ,
> $$
>
> so 1 and 2 hold.
>
> **Step 3** (condition 3 says $g\cdot P = Q$). By the formula of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-2|Lemma §CA.7.2]],
>
> $$
> \bigl\{\{g(h), g(h')\} : \{h, h'\} \in P\bigr\} = (\tau, \sigma)\cdot P ,
> $$
>
> so 3 is $(\tau, \sigma)\cdot P = Q$. The action on half-edges is faithful ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-3|Lemma §CA.7.3]]), so different $(\tau, \sigma)$ give different $g$, and with Step 1
>
> $$
> \{\text{isomorphisms } P \to Q\} \;\longleftrightarrow\; \{(\tau, \sigma) \in G_n : (\tau, \sigma)\cdot P = Q\}
> $$
>
> is a bijection.
>
> **Step 4** (the two parts). Part 1: an isomorphism exists iff some $(\tau, \sigma)$ maps $P$ to $Q$, iff $Q \in G_n\cdot P$ ([[§27 Orbits#^def-27-1|493 Def. §27.1]]). Part 2: for $Q = P$ the right side of Step 3 is $\operatorname{Stab}_{G_n}(P)$ ([[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]]). Composing isomorphisms composes their half-edge maps, and $G_n \to \operatorname{Sym}(X_{E,n})$ is a homomorphism ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-3|Lemma §CA.7.3]]), so the bijection is a group isomorphism:
>
> $$
> \operatorname{Aut}(\Gamma(P)) \cong \operatorname{Stab}_{G_n}(P), \qquad S(P) = |\operatorname{Stab}_{G_n}(P)| = |\operatorname{Aut}(\Gamma(P))| .
> $$
>
> **Step 5** (example). $E = \{x, y\}$, $n = 1$, $a$ for $(1, a)$; $P_t = \{\{x,1\},\{y,2\},\{3,4\}\}$ and $Q = \{\{x,3\},\{y,1\},\{2,4\}\}$. Here $\bar g = \mathrm{id}$, and 3 forces $g(1) = 3$, $g(2) = 1$, $g(\{3, 4\}) = \{2, 4\}$:
>
> $$
> g = \begin{pmatrix}1 & 2 & 3 & 4\\ 3 & 1 & 2 & 4\end{pmatrix} = (1\,3\,2) \qquad\text{or}\qquad g = \begin{pmatrix}1 & 2 & 3 & 4\\ 3 & 1 & 4 & 2\end{pmatrix} = (1\,3\,4\,2) = (1\,3\,2)(3\,4) :
> $$
>
> two isomorphisms, the coset $(1\,3\,2)\operatorname{Stab}(P_t)$ with $\operatorname{Stab}(P_t) = \{\mathrm{id}, (3\,4)\}$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-5|Derivation §CA.7.5]], Step 3).
>
> **What the derivation shows.**
> - [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]] (diagram = orbit, $\operatorname{Aut}$ = stabilizer) agrees with the graph notions: isomorphism classes of graphs with half-edges and their automorphism groups.
> - The image of $G_n$ in $\operatorname{Sym}(X_{E,n})$ is the set of bijections that fix $E$ and carry each leg set $\{v\}\times[4]$ onto a leg set (Step 2): the user's note's relabelling group $G$, of order $k!\,(4!)^k$, which it describes as the wreath product $S_4 \wr S_k$; here $k = n$ and $S_4 \wr S_n = (S_4)^n \rtimes S_n = G_n$.

^der-ca-7-4

*Uses:* [[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-2|Lemma §CA.7.2]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-3|Lemma §CA.7.3]], [[§27 Orbits#^def-27-1|493 Def. §27.1]], [[§26 Stabilizers and Fixed Points#^def-26-1|493 Def. §26.1]]

> [!theorem] Theorem §CA.7.5: The Number of Labelled Diagrams of One Diagram
> For every $P \in \mathcal P(X_{E,n})$,
>
> $$
> |G_n\cdot P| = \frac{n!\,(4!)^n}{S(P)} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor": $\frac1S = \frac{\text{number of complete contractions that produce the diagram}}{n!\,(4!)^n}$) · proof written here*

^thm-ca-7-5

> [!derivation]- Derivation
> **Step 1** (orbit–stabilizer). $G_n$ is finite and acts on $\mathcal P(X_{E,n})$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^lem-ca-7-3|Lemma §CA.7.3]]), so ([[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]])
>
> $$
> |G_n| = |G_n\cdot P|\cdot|\operatorname{Stab}_{G_n}(P)| .
> $$
>
> **Step 2** (insert). The underlying set of the semidirect product is the product set, so $|G_n| = |(S_4)^n|\cdot|S_n| = (4!)^n\,n!$, and $|\operatorname{Stab}(P)| = S(P)$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]]). Divide:
>
> $$
> |G_n\cdot P| = \frac{n!\,(4!)^n}{S(P)} .
> $$
>
> **Step 3** (example). $E = \{x, y\}$, $n = 1$; write $a$ for the half-edge $(1, a)$. $X$ has 6 half-edges and $5!! = 15$ pairings ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]); $G_1 = S_4$ acts by $\tau\cdot\{h, h'\} = \{\tau h, \tau h'\}$, $\tau x = x$, $\tau y = y$. The 15 pairings form two orbits:
>
> $$
> G_1\cdot P_8 = \bigl\{\{\{x,y\},\{1,2\},\{3,4\}\},\ \{\{x,y\},\{1,3\},\{2,4\}\},\ \{\{x,y\},\{1,4\},\{2,3\}\}\bigr\}, \qquad P_8 = \{\{x,y\},\{1,2\},\{3,4\}\},
> $$
>
> $$
> G_1\cdot P_t = \bigl\{\{\{x,a\},\{y,b\},\{c,d\}\} : a \ne b,\ \{c,d\} = \{1,2,3,4\}\setminus\{a,b\}\bigr\}, \qquad P_t = \{\{x,1\},\{y,2\},\{3,4\}\},
> $$
>
> the second because $\tau\cdot P_t = \{\{x,\tau(1)\},\{y,\tau(2)\},\{\tau(3),\tau(4)\}\}$ and $(\tau(1), \tau(2))$ runs through all 12 ordered pairs. The stabilizers:
>
> $$
> \operatorname{Stab}(P_8) = \{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3), (1\,3\,2\,4), (1\,4\,2\,3)\}, \qquad \operatorname{Stab}(P_t) = \{\mathrm{id}, (3\,4)\},
> $$
>
> and $3\cdot8 = 24 = 12\cdot2 = |G_1|$ (stabilizers checked by enumeration over $S_4$).
>
> **What the derivation shows.**
> - Dividing a sum over all pairings by $n!\,(4!)^n$ leaves $1/S$ per diagram exactly when the summand is constant on orbits.
> - Used in: the coefficient of a Feynman diagram ([[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]]).

^der-ca-7-5

![[ph-qft-ca-7-1.svg]]
*The orbit picture of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]]. Left: one labelled diagram, a pairing of all half-edges (orange: leg $a$ of vertex $z_j$). Right: its diagram $D$; the map $\pi$ forgets the labels $j$ and $a$. The fiber $\pi^{-1}(D)$ is the orbit of the pairing under the relabelling group $G_n$, so $|\pi^{-1}(D)| = |G_n|/S$ by orbit–stabilizer, and dividing by $|G_n| = n!\,(4!)^n$ leaves $1/S$. (a) the tadpole, (b) the figure-eight, (c) the melon; each stabilizer is listed on the right, and $S$ agrees with the product formula of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]].*

> [!theorem] Corollary §CA.7.6: The Wick Sum Splits into Diagrams
> For $|E|$ even,
>
> $$
> (|E| + 4n - 1)!! = |\mathcal P(X_{E,n})| = \sum_{\text{diagrams }D}|D| = \sum_{\text{diagrams }D}\frac{n!\,(4!)^n}{S(D)} .
> $$
>
> *Source: the user's note "Symmetry Factors and the Orbit–Stabilizer Theorem" (Oct 2026), §5, after Theorem "Symmetry factor: counting pairings = counting symmetries" · the user's PHY 513 notes, Ch. 14 §14.5 (Figure "Symmetry factors": the counts 12, 3; 24, 72, 9)*

^thm-ca-7-6

> [!derivation]- Derivation
> **Step 1** (count). $X_{E,n}$ has $|E| + 4n$ elements, an even number, so $|\mathcal P(X_{E,n})| = (|E| + 4n - 1)!!$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]).
>
> **Step 2** (orbits). The orbits of $G_n$ partition $\mathcal P(X_{E,n})$ ([[§27 Orbits#^prop-27-1|493 Prop. §27.1]]), and the orbits are the diagrams ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-4|Def. §CA.7.4]]; [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-4|Theorem §CA.7.4]]):
>
> $$
> |\mathcal P(X_{E,n})| = \sum_D|D| .
> $$
>
> **Step 3** (orbit sizes). $|D| = n!\,(4!)^n/S(D)$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]]).
>
> **Step 4** (check: $E = \{x, y\}$, $n = 1$). $|G_1| = 24$; the two diagrams are the tadpole ($S = 2$) and the line times the figure-eight ($S = 8$), their orbits listed in Step 3 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-5|Derivation §CA.7.5]]:
>
> $$
> 5!! = 15 = \frac{24}{2} + \frac{24}{8} = 12 + 3 .
> $$
>
> **Step 5** (check: $E = \varnothing$, $n = 2$). $|G_2| = 2\cdot24^2 = 1152$; the three diagrams are the melon ($S = 48$), the dumbbell ($S = 16$) and two figure-eights ($S = 128$) ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^ex-ca-7-1|Example §CA.7.1]]):
>
> $$
> 7!! = 105 = \frac{1152}{48} + \frac{1152}{16} + \frac{1152}{128} = 24 + 72 + 9 .
> $$
>
> Both checked by enumerating the pairings (`qft-C/tools/l14/enumerate_pairings.py`).
>
> **What the derivation shows.**
> - The decomposition of the set of pairings into orbits is the decomposition of the Wick sum into diagrams: each diagram stands for $n!\,(4!)^n/S$ terms.

^der-ca-7-6

*Uses:* [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]], [[§27 Orbits#^prop-27-1|493 Prop. §27.1]]

> [!theorem] Theorem §CA.7.7: Sums over Pairings as Sums over Diagrams
> If $f: \mathcal P(X_{E,n}) \to R$ (a commutative ring containing $\mathbb Q$) is constant on the orbits of $G_n$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]), with value $f(D)$ on the orbit $D$, then
>
> $$
> \frac{1}{n!\,(4!)^n}\sum_{P\in\mathcal P(X_{E,n})}f(P) = \sum_{\text{diagrams }D}\frac{f(D)}{S(D)} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor") · written here*

^thm-ca-7-7

> [!derivation]- Derivation
> **Step 1** (partition into orbits). The orbits partition $\mathcal P(X_{E,n})$ ([[§27 Orbits#^prop-27-1|493 Prop. §27.1]]), and $f$ is constant on each:
>
> $$
> \sum_{P\in\mathcal P(X_{E,n})}f(P) = \sum_D\;\sum_{P\in D}f(P) = \sum_D|D|\,f(D) .
> $$
>
> **Step 2** (orbit size). $|D| = n!\,(4!)^n/S(D)$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]]); divide by $n!\,(4!)^n$:
>
> $$
> \frac{1}{n!\,(4!)^n}\sum_D|D|\,f(D) = \frac{1}{n!\,(4!)^n}\sum_D\frac{n!\,(4!)^n}{S(D)}\,f(D) = \sum_D\frac{f(D)}{S(D)} .
> $$
>
> With $f \equiv 1$ this is [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-6|Corollary §CA.7.6]] divided by $n!\,(4!)^n$.
>
> **Step 3** (example). $E = \{x, y\}$, $n = 1$, $f(P)$ the number of blocks of $P$ joining $x$ to a vertex half-edge (0 on the 3 pairings of the first orbit, 1 on the 12 of the second, [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-5|Derivation §CA.7.5]], Step 3):
>
> $$
> \frac{1}{24}\bigl(3\cdot0 + 12\cdot1\bigr) = \frac12 = \frac{0}{8} + \frac{1}{2} .
> $$
>
> **What the derivation shows.**
> - "Divide by the symmetry factor" is this identity: the prefactor $\frac{1}{n!}\bigl(\frac{1}{4!}\bigr)^n$ of perturbation theory cancels the size of the group, and each diagram keeps $1/|\operatorname{Aut}|$.
> - Used in: the coefficient of a Feynman diagram ([[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]]).

^der-ca-7-7

*Uses:* [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]], [[§27 Orbits#^prop-27-1|493 Prop. §27.1]]

> [!theorem] Theorem §CA.7.8: A Diagram Is Its Multigraph up to Relabelling the Vertices
> Two labelled diagrams $P, P' \in \mathcal P(X_{E,n})$ lie in the same orbit of $G_n$ if and only if there is a permutation $\sigma \in S_n$ of the vertices, extended by the identity on $E$, with
>
> $$
> m_{P'}\bigl(\sigma(u), \sigma(w)\bigr) = m_P(u, w)\quad\text{and}\quad \ell_{P'}\bigl(\sigma(v)\bigr) = \ell_P(v)
> $$
>
> for all nodes $u \ne w$ and all vertices $v$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-2|Def. §CA.7.2]]). So a diagram is determined by its multigraph with the external points labelled and the vertices unlabelled: by its drawing. This is part 1 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-4|Theorem §CA.7.4]] read on the multigraph: an isomorphism moves the vertices by a $\sigma$ that preserves $m$ and $\ell$, and conversely Steps 2–4 below build one.
>
> *Source: written here (the transcript's test: a diagram is what can be described "to a friend who is not looking at the blackboard", PHY 513 Lecture 14, Part B)*

^thm-ca-7-8

> [!derivation]- Derivation
> **Step 1** (only if). Let $P' = (\tau, \sigma)\cdot P$. The action sends the half-edges of $v$ to half-edges of $\sigma(v)$ and fixes $E$, so a block $\{h, h'\}$ of $P$ joining nodes $u, w$ goes to a block of $P'$ joining $\sigma(u), \sigma(w)$:
>
> $$
> \{h, h'\}\ \text{joins}\ u, w \quad\Longrightarrow\quad \{(\tau,\sigma)h, (\tau,\sigma)h'\}\ \text{joins}\ \sigma(u), \sigma(w) .
> $$
>
> This is a bijection between the blocks of $P$ and of $P'$, so $m_{P'}(\sigma u, \sigma w) = m_P(u, w)$ and $\ell_{P'}(\sigma v) = \ell_P(v)$.
>
> **Step 2** (if: the edges). Assume $\sigma$ as stated. For each unordered pair of distinct nodes $\{u, w\}$ the edges of $\Gamma(P)$ between $u, w$ and those of $\Gamma(P')$ between $\sigma(u), \sigma(w)$ are equally many; choose a bijection between them. Likewise for the loops at $v$ and at $\sigma(v)$.
>
> **Step 3** (if: the half-edges). For an edge $\{h, h'\}$ of $P$ between distinct nodes $u, w$, sent to the edge $\{k, k'\}$ of $P'$ between $\sigma(u), \sigma(w)$ ($h$ at $u$, $k$ at $\sigma(u)$), put $h \mapsto k$, $h' \mapsto k'$. For a loop $\{h, h'\}$ at $v$ sent to the loop $\{k, k'\}$, put $h \mapsto k$, $h' \mapsto k'$. Every half-edge at a vertex $v$ belongs to exactly one block, so this defines a map from the four half-edges of $v$ to half-edges of $\sigma(v)$, $(v, a) \mapsto (\sigma(v), \tau_{\sigma(v)}(a))$; it is injective (different blocks go to different blocks) and hence, both sides having four elements, a bijection $\tau_{\sigma(v)} \in S_4$. External half-edges are fixed, consistently, because the vertex an external point is joined to is mapped by $\sigma$ to the vertex it is joined to in $P'$ ($m$ preserved, $E$ fixed).
>
> **Step 4** (conclude). $(\tau, \sigma)$ maps every block of $P$ to a block of $P'$, so $(\tau, \sigma)\cdot P = P'$.
>
> **Step 5** (two examples).
> - $E = \{x, y\}$, $n = 1$: $P = \{\{x,(1,1)\},\{y,(1,2)\},\{(1,3),(1,4)\}\}$ and $P' = \{\{x,(1,3)\},\{y,(1,1)\},\{(1,2),(1,4)\}\}$ have the same $m(x,1) = m(y,1) = 1$, $\ell(1) = 1$; $\sigma = \mathrm{id}$. Step 3 reads off
>
> $$
> \{x,(1,1)\}\mapsto\{x,(1,3)\}:\ \tau_1(1) = 3; \quad \{y,(1,2)\}\mapsto\{y,(1,1)\}:\ \tau_1(2) = 1; \quad \{(1,3),(1,4)\}\mapsto\{(1,2),(1,4)\}:\ \tau_1(3) = 2,\ \tau_1(4) = 4,
> $$
>
> so $\tau_1 = (1\,3\,2)$, and indeed $(\tau_1, \mathrm{id})\cdot P = P'$.
> - $E = \{x, y\}$, $n = 2$, the snowman with $x, y$ at vertex 1 or at vertex 2:
>
> $$
> P = \{\{x,(1,1)\},\{y,(1,2)\},\{(1,3),(2,1)\},\{(1,4),(2,2)\},\{(2,3),(2,4)\}\},\quad P' = \{\{x,(2,1)\},\{y,(2,2)\},\{(2,3),(1,1)\},\{(2,4),(1,2)\},\{(1,3),(1,4)\}\} .
> $$
>
> $\sigma = (1\,2)$ preserves $m$ and $\ell$: $m_{P'}(x, 2) = m_P(x, 1) = 1$, $m_{P'}(2, 1) = m_P(1, 2) = 2$, $\ell_{P'}(1) = \ell_P(2) = 1$. Step 3 gives $\tau_1 = \tau_2 = \mathrm{id}$; e.g. $(\mathrm{id}, \sigma)\cdot\{(1,3),(2,1)\} = \{(2,3),(1,1)\}$.
>
> **What the derivation shows.**
> - Equality of diagrams can be decided on the drawing: count lines between each pair of points and loops at each vertex, up to renaming the vertices.
> - The same construction with $P' = P$ produces the automorphisms above a given vertex permutation (Theorem §CA.7.9).

^der-ca-7-8

> [!theorem] Theorem §CA.7.9: The Symmetry Factor as a Product
> For $P \in \mathcal P(X_{E,n})$ let $\Gamma_P \le S_n$ be the group of vertex permutations $\sigma$ (extended by the identity on $E$) that preserve all multiplicities and loop numbers, $m_P(\sigma u, \sigma w) = m_P(u, w)$, $\ell_P(\sigma v) = \ell_P(v)$. Then
>
> $$
> S(P) = |\Gamma_P|\;\cdot\prod_{\text{vertices } v}2^{\ell_P(v)}\,\ell_P(v)!\;\cdot\prod_{\{u, w\},\,u \ne w}m_P(u, w)! .
> $$
>
> In words: a factor 2 for each loop (its two ends can be exchanged), $k!$ for each set of $k$ loops at one vertex and for each set of $k$ lines joining the same two points, and the number of permutations of the vertices that map the diagram to itself.
>
> *Source: PHY 513 Lecture 14, slides 17–18, and transcript · the user's PHY 513 notes, Ch. 14 §14.5 (Principle "The symmetry factor", "In practice, multiply") · PS §4.4, p. 93 · proof written here*

^thm-ca-7-9

> [!derivation]- Derivation
> **Step 1** (the projection to vertex permutations). The map
>
> $$
> \pi: \operatorname{Aut}(P) \to S_n, \qquad (\tau, \sigma) \mapsto \sigma ,
> $$
>
> is a homomorphism: the second component of $(\tau, \sigma)\cdot(\tau', \sigma') = (\tau\,\varphi(\sigma)(\tau'), \sigma\sigma')$ is $\sigma\sigma'$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^def-ca-7-3|Def. §CA.7.3]]).
>
> **Step 2** (the image is $\Gamma_P$). By Step 1 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-8|Derivation §CA.7.8]] with $P' = P$, every $\sigma$ in the image preserves multiplicities and loops: $\pi(\operatorname{Aut}(P)) \subseteq \Gamma_P$. Conversely, for $\sigma \in \Gamma_P$, Steps 2–4 there with $P' = P$ build $(\tau, \sigma) \in \operatorname{Aut}(P)$. So $\pi(\operatorname{Aut}(P)) = \Gamma_P$.
>
> **Step 3** (the kernel). $\ker\pi = \{(\tau, \mathrm{id}) : (\tau, \mathrm{id})\cdot P = P\}$: half-edge permutations at fixed vertices preserving the blocks. Such a $\tau$ maps each edge to an edge with the same end nodes. Count the choices bundle by bundle:
> - a bundle of $m$ edges $\{(u, a_i), (w, b_i)\}$, $i = 1, \dots, m$, between distinct vertices $u, w$: $\tau_u$ permutes $\{a_1, \dots, a_m\}$, $\tau_u(a_i) = a_{\rho(i)}$ for some $\rho \in S_m$, and then $\tau_w(b_i) = b_{\rho(i)}$ is forced (the edge $i$ must go to the edge $\rho(i)$): $m!$ choices;
> - an edge $\{e, (v, a)\}$ from an external point $e$: $e$ is fixed, so $\tau_v(a) = a$: $1 = 1!$;
> - the $\ell$ loops $\{(v, c_i), (v, d_i)\}$, $i = 1, \dots, \ell$, at $v$: $\tau_v$ sends loop $i$ to loop $\rho(i)$, $\rho \in S_\ell$, as $\{c_i, d_i\} \mapsto \{c_{\rho(i)}, d_{\rho(i)}\}$ in one of two ways each: $2^\ell\,\ell!$ choices.
>
> The choices for different bundles are independent (they act on disjoint sets of half-edges, and every half-edge lies in exactly one bundle), so
>
> $$
> |\ker\pi| = \prod_v2^{\ell(v)}\,\ell(v)!\;\prod_{u \ne w}m(u, w)! .
> $$
>
> **Step 4** (count). By the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]) $\operatorname{Aut}(P)/\ker\pi \cong \Gamma_P$, and by Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]])
>
> $$
> S(P) = |\operatorname{Aut}(P)| = |\Gamma_P|\cdot|\ker\pi| .
> $$
>
> **Step 5** (two examples).
> - The figure-eight, $E = \varnothing$, $n = 1$, $P = \{\{(1,1),(1,2)\},\{(1,3),(1,4)\}\}$: $\Gamma_P = S_1$, and the kernel consists of $\rho \in S_2$ (keep or exchange the loops) times a reversal of each loop:
>
> $$
> \ker\pi = \{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4)\}\;\cup\;(1\,3)(2\,4)\cdot\{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4)\} = \{\mathrm{id}, (1\,2), (3\,4), (1\,2)(3\,4), (1\,3)(2\,4), (1\,4\,2\,3), (1\,3\,2\,4), (1\,4)(2\,3)\},
> $$
>
> $|\ker\pi| = 2^2\cdot2! = 8 = S$.
> - The melon, $E = \varnothing$, $n = 2$, $P_\kappa = \{\{(1,a),(2,\kappa(a))\} : a = 1, \dots, 4\}$ for a fixed $\kappa \in S_4$: one bundle with $m(1, 2) = 4$, so
>
> $$
> \ker\pi = \{(\tau_1, \kappa\tau_1\kappa^{-1}) : \tau_1 \in S_4\}, \qquad |\ker\pi| = 4! = 24 ;
> $$
>
> $(1\,2) \in \Gamma_P$, with preimages $(\tau_1, \kappa\tau_1\kappa; (1\,2))$, so $|\Gamma_P| = 2$ and $S = 2\cdot24 = 48$; a brute-force count of the stabilizer in $G_2$ gives the same 48.
>
> ⚑ By-product: the factor $k!$ applies to $k$ loops at one vertex as well as to $k$ lines between two vertices. The figure-eight needs both: $2\cdot2$ for the two loops and $2!$ for exchanging them, $S = 8$ ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^ex-ca-7-1|Example §CA.7.1]]).
>
> **What the derivation shows.**
> - The rule of thumb of the slides is exact: the symmetry factor is the product of independent local symmetries (loops, bundles) times the global symmetry of the vertex arrangement.
> - Checked against a brute-force count of stabilizers in $G_1$ and $G_2$ for every diagram with $n \le 2$ and $E = \varnothing$ or $\{x, y\}$.

^der-ca-7-9

*Uses:* [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-8|Theorem §CA.7.8]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|493 Thm. §29.2]]

![[ph-qft-ca-7-5.svg]]
*The product formula of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]]. (a) The three kinds of factor: $2^{\ell}\ell!$ for $\ell$ loops at one vertex, $m!$ for $m$ lines between two points, and $|\Gamma_P|$ for the vertex permutations that keep the drawing. (b) Four diagrams with their $S$; with external points fixed, $\Gamma_P$ can be trivial.*

> [!example] Example §CA.7.1: Symmetry Factors from the Product Formula
> Each item: the data $|\Gamma_P|$, $\ell_P(v)$, $m_P(u, w)$ of the diagram, $S$ by [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-9|Theorem §CA.7.9]], and the size of its orbit $|G_n|/S$ by [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-5|Theorem §CA.7.5]], each confirmed by enumerating the pairings.
>
> *$n = 1$, $E = \{x, y\}$, $|G_1| = 24$.*
> - *Tadpole* ($x$–$v$, $v$–$y$, one loop at $v$): $|\Gamma| = 1$, $\ell(v) = 1$, $m(x, v) = m(y, v) = 1$:
>
> $$
> S = 1\cdot2^1\,1!\cdot1!\,1! = 2, \qquad |G_1\cdot P| = \frac{24}{2} = 12 .
> $$
>
> - *Line times figure-eight* ($x$–$y$, two loops at $v$): $|\Gamma| = 1$, $\ell(v) = 2$, $m(x, y) = 1$:
>
> $$
> S = 1\cdot2^2\,2!\cdot1! = 8, \qquad |G_1\cdot P| = \frac{24}{8} = 3 .
> $$
>
> $12 + 3 = 15 = 5!!$: every pairing of the six half-edges is one of the two.
>
> *$n = 1$, $E = \varnothing$.* *Figure-eight*: $S = 2^2\,2! = 8$, orbit $\frac{24}{8} = 3 = 3!!$.
>
> *$n = 2$, $E = \varnothing$, $|G_2| = 2\cdot24^2 = 1152$.*
> - *Melon* (four lines between the two vertices): $\Gamma = S_2$ (the swap keeps $m(1, 2) = 4$), $\ell = 0$:
>
> $$
> S = 2\cdot4! = 48, \qquad \frac{1152}{48} = 24 .
> $$
>
> - *Dumbbell* (one loop at each vertex, two lines between them): $\Gamma = S_2$, $\ell(1) = \ell(2) = 1$, $m(1, 2) = 2$:
>
> $$
> S = 2\cdot(2^1\,1!)(2^1\,1!)\cdot2! = 16, \qquad \frac{1152}{16} = 72 .
> $$
>
> - *Two figure-eights*: $\Gamma = S_2$, $\ell(1) = \ell(2) = 2$, no line between them:
>
> $$
> S = 2\cdot(2^2\,2!)(2^2\,2!) = 128, \qquad \frac{1152}{128} = 9 .
> $$
>
> Together $24 + 72 + 9 = 105 = 7!!$: every pairing of the eight half-edges is one of these three diagrams.
>
> *Source: the user's PHY 513 notes, Ch. 14 §14.5 (Figure "Symmetry factors": "12 of 4!", "3 of 4!", "24 of $2\cdot4!^2$", "72", "9") · PHY 513 Lecture 14, slide 18 · checked with `qft-C/tools/l14/enumerate_pairings.py`*

^ex-ca-7-1

> [!remark]- ★ Remark: The same sum is the moment formula of a Gaussian
> For a centred Gaussian random vector $\xi = (\xi_1, \dots, \xi_{2k})$ with covariance $C_{ij} = \mathbb E[\xi_i\xi_j]$, $\mathbb E[\xi_1\cdots\xi_{2k}] = \sum_{P\in\mathcal P([2k])}\prod_{\{i,j\}\in P}C_{ij}$ and odd moments vanish (Isserlis' theorem). The vacuum values of Wick's theorem have the same form with $C = D_F$ ([[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]]); in the path integral they *are* Gaussian moments ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|§C2b.6, Remark: Preview: the propagator as a Gaussian covariance]]; QFT C11, planned). Not used in the course at this stage.
>
> *Source: L. Isserlis, Biometrika 12 (1918) 134 (stated, not proved here) · Gaussian integrals: [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-1|Theorem §CA.5.1]]*

^rem-ca-7-1

> [!remark]- Connections
> - Counting pairings is counting the terms of a vacuum expectation value of free fields; $(2k-1)!!$ grows like $\sqrt2\,(2k/e)^k$, which is why perturbation theory is organized by diagrams rather than by terms — [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]], [[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]].
> - The symmetry factor is a stabilizer order, and "divide by $S$" is orbit–stabilizer in disguise; the same counting gives the class equation and Burnside's lemma in group theory — [[§30 Orbit–Stabilizer#^thm-30-3|493 Thm. §30.3]], [[§30 Orbit–Stabilizer#^thm-30-6|493 Thm. §30.6]].
> - The relabelling group $(S_4)^n \rtimes S_n$ is a wreath product, $S_4 \wr S_n$ (the user's note's $S_4 \wr S_k$, $k$ the number of vertices; the identification is Step 2 of [[§CA.7 Pairings, Diagrams and Symmetry Factors#^der-ca-7-4|Derivation §CA.7.4]]); the 493 notes construct the semidirect product it is built from — [[§56 Semidirect Products#^def-56-2|493 Def. §56.2]].
> - The ordered simplex of [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-4|Theorem §CA.1.4]] produced the $\frac{1}{n!}$ of the Dyson series; here the same $\frac{1}{n!}$ meets the $n!$ relabellings of the vertices — [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]].
> - **Used in** (C6 places): Definition §CA.7.1 — Wick's theorem for ordinary products ([[§C6.6 Wick's Theorem#^thm-c6-6-4|★ Theorem §C6.6.4]]); Theorem §CA.7.1 — the vacuum values of Wick's theorem, the first-order count and the count at every order ([[§C6.6 Wick's Theorem#^thm-c6-6-3|Theorem §C6.6.3]], [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-1|Theorem §C6.7.1]], [[§C6.7 Feynman Diagrams for Correlation Functions#^thm-c6-7-3|Theorem §C6.7.3]]); Definitions §CA.7.2–§CA.7.5, Lemma §CA.7.3, Theorems §CA.7.4, §CA.7.5 and §CA.7.8 — the coefficient $1/S$ and the position-space rules ([[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]], [[§C6.8 Position-Space Feynman Rules#^thm-c6-8-2|Theorem §C6.8.2]]); Corollary §CA.7.6 — the first-order count 15 = 12 + 3 as two orbits ([[§C6.9 Symmetry Factors in Practice#^ex-c6-9-1|Example §C6.9.1]]); Theorem §CA.7.9 and Example §CA.7.1 — the symmetry factors in practice ([[§C6.9 Symmetry Factors in Practice|§C6.9]], [[§C6.9 Symmetry Factors in Practice#^cau-c6-9-1|§C6.9, Caution: Loops at one vertex are permuted too]]); Theorem §CA.7.7 — "divide by the symmetry factor" ([[§C6.8 Position-Space Feynman Rules#^thm-c6-8-1|Theorem §C6.8.1]]).
