---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.2 Matrix Elements between Particle States]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.4 Transition Probabilities in a Box]] →

SOURCES_PLACEHOLDER

OPENING_PLACEHOLDER

## Tree-level rules for the amplitude

> [!definition] Definition §C6b.3.2: Diagram of a Scattering Amplitude
> For a process with initial momenta $p_A, p_B, \dots$ and final momenta $p_1, p_2, \dots$, a **diagram of the amplitude** $i\mathcal M$ is a diagram ([[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]]; other vertices: [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]) such that
> 1. its external points are labelled by the external momenta, one per particle, and are never relabelled;
> 2. it is fully connected ([[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-1|Caution: "Connected" here means fully connected]]);
> 3. its external lines are amputated ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]): each external point is joined by a line without propagator to a vertex, and the momentum of every internal line is fixed by conservation at the vertices. Between particle states this is the contraction of a leg with the particle, a plane wave without propagator ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]]).
>
> Its symmetry factor is that of [[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]] with the labelled external points held fixed. Diagrams that are not fully connected are excluded: their pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ or to products of smaller processes ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-2|Theorem §C6b.10.2]], [[§C6b.10 Amplitudes from Correlation Functions#^rem-c6b-10-1|Remark: Disconnected pieces beyond zeroth order]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction without derivatives, any order; used for $\mathcal M$ at lowest order ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]).
>
> *Source: PHY 513, Problem Set 8, Problem 2(a)–(b) (the user's solution: "The four external particles are labeled by their momenta and are never relabeled, so a diagram is determined by which external particles are attached to which vertex"; a vertex with too many external particles leaves two legs "contracted with each other, giving a disconnected diagram that does not contribute to the scattering amplitude") · PHY 513 Lecture 15, transcript ("strip off the external lines") · Yu §7.3 (external lines of $\langle f|iT|i\rangle$)*

^def-c6b-3-2

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!theorem] Theorem §C6b.3.1: Vertices Saturated by External Lines Give S = 1
> If every vertex $v$ of a diagram has valence $r_v \ge 2$ and at least $r_v - 1$ of its legs joined to external points, then $S = 1$; equivalently $N_D = |G|$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]). In particular every tree diagram with one internal line has $S = 1$.
>
> *Model:* any (combinatorics); *applies:* any diagram with the stated valences, any vertex types.
>
> *Source: PHY 513, Problem Set 8, Problem 2(c) (the user's argument: "each vertex has exactly one internal leg … The external particles are never relabeled, so an element of $\mathrm{Stab}(P)$ fixes every leg joined to an external particle. The internal leg is then the only remaining leg at its vertex, so it is fixed as well") · PHY 513 Lecture 14, slide 17 ("Reordering of legs = topologically distinct diagram ⇒ S = 1")*

^thm-c6b-3-1

> [!derivation]- Derivation
> **Step 1** (vertices fixed). Let $g \in \operatorname{Stab}(P)$. Each leg joined to an external point is fixed, and so is its vertex ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3). Every vertex has $r_v - 1 \ge 1$ such legs, so $g$ permutes no vertices.
>
> **Step 2** (legs fixed). $g$ maps the legs of $v$ to legs of $v$; at least $r_v - 1$ are fixed, so the remaining one (if any) is mapped to itself. Hence $g$ fixes every half-edge: $g = e$, $S = |\operatorname{Stab}(P)| = 1$.
>
> **Step 3** (count). $N_D = |G|/S = |G|$. Example (one cubic and one quartic vertex, five external particles, two on the cubic and three on the quartic vertex): the two at the cubic vertex attach in $3\cdot2$ ways, the three at the quartic vertex in $4\cdot3\cdot2$, the remaining two legs pair in one way: $N_D = 6\cdot24 = 144 = 3!\,4! = |G|$.

^der-c6b-3-1

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-5|P5, step 5]]

> [!theorem] Theorem §C6b.3.2: Tree-Level Feynman Rules for iℳ
> For an interaction with the vertex data of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]] and a process with incoming momenta $k_1, \dots, k_n$ and outgoing $p_1, \dots, p_m$, none equal to an incoming one, the contribution of the tree diagrams of the amplitude ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]], with no loops) to $i\mathcal M$ is the sum over these diagrams of the product of:
> - each **external line**: $1$ (a particle or antiparticle of a complex field attaches to the leg of [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 3);
> - each **vertex** of type $t$: $-ig_t\prod_km_{t,k}!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]);
> - each **internal line** of mass $m_j$: $\dfrac{i}{q^2 - m_j^2 + i\varepsilon}$, with $q$ fixed by four-momentum conservation at the vertices;
>
> with symmetry factor $S = 1$ for every tree diagram and the overall $(2\pi)^4\delta^4(\sum_ik_i - \sum_jp_j)$ stripped ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* tree level, free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]); at the lowest order of a process this is the amplitude; beyond it loops on external lines need $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]; LSZ, Lecture 16).
>
> *Source: PS §4.6, p. 114 (eq. (4.103): "sum of all connected, amputated Feynman diagrams"; "the factor for an ingoing line is just the amplitude for that particle to be found at the vertex"), p. 115 (rules 1–6) · Yu §7.2, rules 6–11 (pp. 287–288); §7.4, momentum-space rules 1–5 (p. 300); §7.3, p. 294 (tree diagrams have $S = 1$; [[§C6a.9 Symmetry Factors in Practice#^rem-c6a-9-3|§C6a.9, Remark: Yu's route]]) · PHY 513 Lecture 15, transcript ("strip off the external lines") · proof written here*

^thm-c6b-3-2

> [!derivation]- Derivation
> **Step 1** (order $\mathbf n$). With [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]] and Step 1 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]],
>
> $$
> \langle f|\hat S|i\rangle^{(\mathbf n)} = \prod_t\frac{(-ig_t)^{n_t}}{n_t!}\int\prod_{t,v}d^4z_{t,v}\;\langle\mathbf p_1\cdots\mathbf p_m|\,T\Bigl\{\prod_{t,v}M_t\bigl(\hat\phi_I(z_{t,v})\bigr)\Bigr\}|\mathbf k_1\cdots\mathbf k_n\rangle .
> $$
>
> **Step 2** (full contractions). By [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]] (with kinds), the matrix element is a sum over full contractions of legs and particles; outgoing–incoming pairs vanish (distinct momenta). A full contraction is a labelled diagram whose external points are the particles, never relabelled ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]], 1). If it falls into several connected pieces, each piece carries its own momentum delta (Step 3 below): such terms are not of the form $\delta^4(\sum k - \sum p)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]] and do not belong to $\mathcal M$ ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-2|Theorem §C6b.10.2]]; vacuum pieces are the phase of [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]). Keep the fully connected ones.
>
> **Step 3** (values). A particle on a leg at $z$ gives $e^{-ik\cdot z}$ (incoming) or $e^{+ip\cdot z}$ (outgoing) ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 2–3); a leg–leg pair gives $D_F^{(m_j)}(z - z')$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]). Relabelling vertices and legs of one kind leaves the integral unchanged, and orbit–stabilizer turns the prefactor into $\frac1S\prod_v(-ig_t\prod_km_{t,k}!)$ (Steps 3–5 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]], the particles playing the external points).
>
> **Step 4** ($S = 1$ for a tree). Let $D$ be a fully connected diagram without loops (a tree) and $g \in \operatorname{Stab}(P)$. Every leaf of the tree is an external particle (a vertex with a single line would have valence one). Removing an internal line $e$ splits the particles into two nonempty sets $E_1(e) \sqcup E_2(e)$, and different lines give different splits (two lines of a tree are separated by a vertex with a third branch, which holds a particle). $g$ fixes every particle ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3), so it maps each line to the line with the same split, i.e. to itself, with its ends on their own sides: every line and every vertex is fixed. A tree has no two lines between the same vertices, so the legs of a fixed vertex are fixed too: $g = e$, $S = |\operatorname{Stab}(P)| = 1$ (for one internal line this is [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-1|Theorem §C6b.3.1]]).
>
> **Step 5** (momentum space). Insert the Fourier form of every internal line and do the vertex integrals ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], Steps 1–2): each vertex gives $(2\pi)^4\delta^4(\text{momenta in} - \text{momenta out})$, the external momenta entering through the plane waves of Step 3. A tree has $L = I - V + 1 = 0$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 2): $V$ deltas, $I = V - 1$ internal momentum integrals. Each integral uses one delta and fixes its $q$; the last delta is
>
> $$
> (2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr) ,
> $$
>
> and what multiplies it is $\prod(\text{vertex factors})\prod\frac{i}{q^2 - m_j^2 + i\varepsilon}$. External lines leave no factor: their plane wave became part of a delta.
>
> **Step 6** (read off). Comparing with [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] strips the delta. Check: $\phi^4$, one vertex, $i\mathcal M = -i\lambda$ ([[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1|Example §C6b.2.1]]); $\Phi\phi^2$, one vertex, $-2i\mu$ ([[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-2|Example §C6b.2.2]]).
>
> **What the derivation shows.**
> - The external line is $1$ because the contraction of a field with a relativistically normalized particle is a pure plane wave; the amputation of [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]] removes the external propagator to reach the same factor from a correlation function.
> - Nothing about loops was used except in Step 4; loop diagrams follow the same rules with $\frac1S$ and one $\int\frac{d^4\ell}{(2\pi)^4}$ per loop, but external-leg loops then need the $\sqrt Z$ of LSZ.

^der-c6b-3-2

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, steps 4–6]]

> [!example] Example §C6b.3.1: Cubic–Quartic Theory, 2 → 2 at Order g² and λ
> ![[ph-qft-c6b-11-5.svg]]
>
> $\mathcal L = \frac12(\partial_\mu\phi)^2 - \frac{m^2}{2}\phi^2 - \frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]), vertices $-ig$, $-i\lambda$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]); $p_A + p_B \to p_1 + p_2$. A diagram with $n_3$ cubic and $n_4$ quartic vertices is of order $g^{n_3}\lambda^{n_4}$ (Problem Set 8: treat $\lambda \sim g^2/m^2$ as the same order).
> - *$O(g^2)$, two cubic vertices*: $6$ legs, $4$ joined to external lines, so one internal line ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1: $6 = 4 + 2I$; $L = 1 - 2 + 1 = 0$, a tree). If one vertex carried three external particles, the other would carry one, and its two remaining legs would be contracted with each other: not fully connected ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3), excluded ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]]). So each vertex carries two, and $p_A$ shares its vertex with exactly one of $p_B$, $p_1$, $p_2$ (putting $p_A$ on the other vertex only exchanges the vertices): three diagrams.
> - *$O(\lambda)$, one quartic vertex*: all four on it, one diagram.
>
> | diagram | at one vertex | at the other | internal momentum |
> |---|---|---|---|
> | $s$-channel | $p_A, p_B$ | $p_1, p_2$ | $p_A + p_B$ |
> | $t$-channel | $p_A, p_1$ | $p_B, p_2$ | $p_A - p_1$ |
> | $u$-channel | $p_A, p_2$ | $p_B, p_1$ | $p_A - p_2$ |
> | contact | $p_A, p_B, p_1, p_2$ | — | — |
>
> Each has $S = 1$ ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-1|Theorem §C6b.3.1]]): the cubic vertices carry $2 = 3 - 1$ external lines, the quartic one $4$. Enumeration: the $9!! = 945$ pairings at order $g^2$ form $31$ diagrams, of which exactly these $3$ are fully connected, each an orbit of $72 = 2!\,(3!)^2 = |G|$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(a) (the user's solution: diagrams drawn and with vertices opened into their legs) · checked with `qft-C/tools/hw8/check_hw8.py`*

^ex-c6b-3-1

> [!example] Example §C6b.3.2: Cubic–Quartic Theory, 2 → 3 at Order gλ
> ![[ph-qft-c6b-2-4.svg]]
>
> Same theory, $p_A + p_B \to p_1 + p_2 + p_3$, one cubic and one quartic vertex: $3 + 4 = 7$ legs, $5$ joined to external lines, one internal line ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1: $7 = 5 + 2I$, a tree). Three external particles on the cubic vertex would leave two legs of the quartic vertex contracted with each other, four on the quartic vertex two legs of the cubic one: not fully connected ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3). So two external particles sit on the cubic vertex and three on the quartic, and a diagram is the choice of the two at the cubic vertex: $\binom52 = 10$. With $u \in \{A, B\}$, $v \ne u$, $i \in \{1, 2, 3\}$, $\{j, k\} = \{1, 2, 3\}\setminus\{i\}$:
>
> | class | at the cubic vertex | number | internal momentum |
> |---|---|---|---|
> | (I) both incoming | $p_A, p_B$ | $1$ | $p_A + p_B$ |
> | (II) one in, one out | $p_u, p_i$ | $2\cdot3 = 6$ | $p_u - p_i$ |
> | (III) both outgoing | $p_j, p_k$ | $3$ | $p_A + p_B - p_i = p_j + p_k$ |
>
> $1 + 6 + 3 = 10$. All have $S = 1$ ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-1|Theorem §C6b.3.1]], Step 3: $N_D = 144 = 3!\,4! = |G|$; there is one vertex of each type, so $G$ contains no vertex permutations). Enumeration: the $11!! = 10\,395$ pairings of the $12$ half-edges form $195$ diagrams, exactly $10$ of them fully connected, each an orbit of $144$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(b)–(c) (the user's solution) · checked with `qft-C/tools/hw8/check_hw8.py`*

^ex-c6b-3-2

![[ph-qft-c6-17-1.svg]]
*The diagrams of [[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-1|Example §C6b.3.1]] and [[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-2|Example §C6b.3.2]] (cubic vertices orange, quartic blue; incoming momenta left, outgoing right). Top: $2 \to 2$, the $s$-, $t$-, $u$-channel diagrams at order $g^2$ and the contact diagram at order $\lambda$. Bottom: $2 \to 3$ at order $g\lambda$, one representative of each class (I), (II), (III). Added figure, adapted from the user's solution of PHY 513, Problem Set 8, Problem 2.*

BACKGROUND_PLACEHOLDER

> [!remark]- Connections
> - The vertex factors and lines are those of the correlation functions — [[§C6a.12 Feynman Rules for Polynomial Interactions|§C6a.12]]; the amputation route to the same $i\mathcal M$ and its LSZ form — [[§C6b.10 Amplitudes from Correlation Functions|§C6b.10]].
