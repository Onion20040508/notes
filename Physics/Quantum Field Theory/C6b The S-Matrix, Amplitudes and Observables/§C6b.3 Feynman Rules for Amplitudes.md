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

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.6, pp. 112–115, eqs. (4.101)–(4.104) and the rules for $\phi^4$ (p. 115) · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part C, slides 21–26, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.6–§16.9 · Yu Zhao-Huan, 量子场论讲义, §7.2, rules 6–11 (pp. 287–288); §7.3, pp. 294–296; §7.4, rules 1–5 (p. 300); §10.5.3 · Schwartz, Quantum Field Theory and the Standard Model, §7.4, pp. 97–98, eqs. (7.91)–(7.96) · PHY 513, Problem Set 8, Problem 2 (the user's solution, submitted 2026-10-30) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), transcript ("strip off the external lines").*

Lecture 16, Part C, states the Feynman rules for the amplitude itself: "$i\mathcal M$ = sum over all connected, amputated diagrams". [[§C6b.2 Matrix Elements between Particle States|§C6b.2]] expanded the $S$-matrix element between free particle states and sorted its terms ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]]). The whole route in one line, as the user's notes summarize it (Principle "From the time-evolution operator to $i\mathcal M$"): expand ${}_0\langle\mathbf p_1\mathbf p_2\cdots|T\{e^{-i\int\hat H_I}\}|\mathbf p_A\mathbf p_B\rangle_0$ between free states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); Wick's theorem contracts fields with each other ($D_F$) or with particles (wave functions $e^{\mp ip\cdot z}$; [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]]); omit particles going straight through ($\delta$-lines, the $\mathbb 1$), vacuum bubbles, and corrections on external legs (of the size of $\sqrt Z - 1$); what remains is $i\mathcal M$ with vertex $-i\lambda$, propagator $\frac{i}{p^2 - m^2 + i\varepsilon}$, external lines $1$, momentum conservation at each vertex, $\int\frac{d^4q}{(2\pi)^4}$ per loop and $\frac1S$.

This section defines amputation ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]]) and the diagram of an amplitude ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]]), shows $S = 1$ for saturated vertices and trees ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-1|Theorem §C6b.3.1]]), gives the tree-level rules for any polynomial interaction ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]]) and the rules at any order ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]], PS (4.103)–(4.104)), enumerates the tree diagrams of a process with the $s$-, $t$-, $u$-channels ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-4|Theorem §C6b.3.4]]), and works the cubic–quartic diagrams of Problem Set 8 and $\phi\phi \to \phi\phi$ at order $\lambda^2$ ([[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-3|Example §C6b.3.3]]). [[§C6b.10 Amplitudes from Correlation Functions|§C6b.10]] reaches the same rules from the correlation functions of C6a by amputation, the route that generalizes through LSZ. Yu states the rules case by case in §7.2–§7.4, read off first-order $T$-matrix elements, and justifies them in §10.5.

**Setup and scope.** As in [[§C6b.2 Matrix Elements between Particle States|§C6b.2]]: free relativistic states over $|0\rangle$ standing for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]), a permanent interaction ([[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]); exact at the lowest order of a process, beyond it $\sqrt Z$ per external line and the physical mass ([[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]). Each box states its scope.

## Amputation and the diagrams of an amplitude

> [!definition] Definition §C6b.3.1: Amputation of an External Leg
> In a diagram with external particles, start at the tip of an external leg (the end at the particle) and go into the diagram to the **last point at which the diagram can be cut by removing one propagator** such that the cut separates the leg, with everything that hangs on it, from the rest. **Amputating** the leg removes everything between the tip and that cut: the particle is then joined, by a line without propagator, directly to the vertex beyond the cut. A diagram is **amputated** if no leg has anything to remove, i.e. no propagator separates a part holding a single particle from the rest.
>
> What is removed is "interaction corrects external state. Not an interaction between different states" (slide 26). A tree whose vertices all have $r_v \ge 3$ legs is amputated: removing an internal line leaves on each side a vertex with at least two further branches, each ending at a particle, so no line separates a single particle.
>
> *Model:* any (combinatorics); *applies:* diagrams of $S$-matrix elements and of correlation functions alike (for a correlation function the removed part includes the external propagator: [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]); the removed corrections are not zero: beyond lowest order they return as $\sqrt Z$ per external line and the physical mass ([[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]; second semester).
>
> *Source: PHY 513 Lecture 16, slide 26 ("Some diagrams encode 'interaction corrects external state' … Amputation: exclude such diagrams. General rule for where to amputate external leg: go from tip to last point where diagram can be cut by removing one propagator. Corrections to external wave functions are interesting and studied in 2nd semester") · the user's PHY 513 notes, Lecture 16 update, §16.7, Definition "Connected and amputated" and paragraph "Why amputated" · PHY 513 Lecture 16, transcript ("What amputation means is that in these kind of diagrams … nothing happens between out here and into the vertex") · PS §4.6, p. 113 ("Starting from the tip of each external leg, find the last point at which the diagram can be cut by removing a single propagator, such that this operation separates the leg from the rest of the diagram. Cut there.") and the figure on p. 114*

^def-c6b-3-1

![[ph-qft-c6b-3-1.svg]]
*Amputation ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]]). (a) Slide 26: a loop at $z_1$ on the leg of $A$; removing the propagator $z_1z$ separates the leg with its loop. (b) Two loops on the leg: two propagators separate it; the cut is made at the last one, next to the vertex $z$, and both loops go. (c) What remains in both cases is the vertex $-i\lambda$ with $A$ attached directly. Added figure.*

> [!definition] Definition §C6b.3.2: Diagram of a Scattering Amplitude
> For a process with initial momenta $p_A, p_B, \dots$ and final momenta $p_1, p_2, \dots$, a **diagram of the amplitude** $i\mathcal M$ is a diagram ([[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]]; other vertices: [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]) such that
> 1. its external points are labelled by the external momenta, one per particle, and are never relabelled;
> 2. it is fully connected ([[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-1|Caution: "Connected" here means fully connected]]);
> 3. its external legs are amputated ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]]; [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]); for a tree this means: each external point is joined by a line without propagator to a vertex, and the momentum of every internal line is fixed by conservation at the vertices. Between particle states this is the contraction of a leg with the particle, a plane wave without propagator ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]]).
>
> Its symmetry factor is that of [[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]] with the labelled external points held fixed. Diagrams that are not fully connected are excluded: their pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ or to products of smaller processes ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-2|Theorem §C6b.10.2]], [[§C6b.10 Amplitudes from Correlation Functions#^rem-c6b-10-1|Remark: Disconnected pieces beyond zeroth order]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction without derivatives, any order; used for $\mathcal M$ at lowest order ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]) and at every order ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]]).
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

## The rules

> [!theorem] Theorem §C6b.3.2: Tree-Level Feynman Rules for iℳ
> For an interaction with the vertex data of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]] and a process with incoming momenta $k_1, \dots, k_n$ and outgoing $p_1, \dots, p_m$, none equal to an incoming one, the contribution of the tree diagrams of the amplitude ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]], with no loops) to $i\mathcal M$ is the sum over these diagrams of the product of:
> - each **external line**: $1$ (a particle or antiparticle of a complex field attaches to the leg of [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 3);
> - each **vertex** of type $t$: $-ig_t\prod_km_{t,k}!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]);
> - each **internal line** of mass $m_j$: $\dfrac{i}{q^2 - m_j^2 + i\varepsilon}$, with $q$ fixed by four-momentum conservation at the vertices;
>
> with symmetry factor $S = 1$ for every tree diagram and the overall $(2\pi)^4\delta^4(\sum_ik_i - \sum_jp_j)$ stripped ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). These are the rules of [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]] for diagrams without loops ($L = 0$, $S = 1$).
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
> - Nothing about loops was used except in Step 4; loop diagrams follow the same rules with $\frac1S$ and one $\int\frac{d^4\ell}{(2\pi)^4}$ per loop, but external-leg loops then need the $\sqrt Z$ of LSZ; stated as [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]].

^der-c6b-3-2

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, steps 4–6]]

> [!theorem] Theorem §C6b.3.3: Feynman Rules for iℳ, All Orders
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), for $p_A + p_B \to \{p_f\}$,
>
> $$
> i\mathcal M\,(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_fp_f\Bigr) = \Bigl(\text{sum of all connected, amputated diagrams with } p_A, p_B \text{ incoming, } p_f \text{ outgoing}\Bigr) ,
> $$
>
> connected meaning fully connected and amputated as in [[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]] (the terms that remain by [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]]), each diagram the product of
>
> | element | position space | momentum space |
> |---|---|---|
> | vertex (four line-ends meet) | $-i\lambda\int d^4x$ | $-i\lambda$, momentum conserved at the vertex |
> | propagator between vertices at $x$, $y$ | $D_F(x - y)$ | $\dfrac{i}{p^2 - m^2 + i\varepsilon}$ |
> | external line, incoming $p$, at $x$ | $e^{-ip\cdot x}$ | $1$ |
> | external line, outgoing $p$, at $x$ | $e^{+ip\cdot x}$ | $1$ |
> | momentum not fixed by conservation | — | $\int\frac{d^4\ell}{(2\pi)^4}$, $L = I - V + 1$ of them ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]]) |
> | the diagram | $\frac1S$ | $\frac1S$ |
>
> and in momentum space the overall delta is stripped: $i\mathcal M$ = sum of all connected, amputated diagrams. $S$ is the symmetry factor with the external particles held fixed ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]], 1): "$\mathcal M$ has less symmetry than the Green's function ⇒ $S$ simpler". For a polynomial interaction ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]) the vertex is $-ig_t\prod_km_{t,k}!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]) and each line carries the propagator of its field ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]). For diagrams without loops ($L = 0$, $S = 1$) these are the tree rules of [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]: at the lowest order of a process exact as [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]]; loop corrections on internal lines by these rules; corrections on external legs are excluded by amputation, and their $\sqrt Z$ and the physical mass are deferred ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]; PS p. 115: "(4.103) still isn't quite correct … the modification affects only diagrams containing loops").
>
> *Source: PHY 513 Lecture 16, slides 22–24 (slide 22: "Vertex = 4 endpoints of lines meet = $-i\lambda\int d^4x$ … Propagator: line btw. vertices at $x$, $y$ = $D_F(x - y)$. External line: vertex to incoming/outgoing particle = $e^{-ipx}$. Symmetry factor: divide by $S$. $\mathcal M$ has less symmetry than Green's function ⇒ $S$ simpler"; slide 24: "'Loop' integration over momenta undetermined by conservation at each vertex") · PS §4.6, p. 114, eqs. (4.103)–(4.104), p. 115 (rules 1–6) · Yu §7.3, p. 296 · the outgoing plane wave $e^{+ip\cdot x}$: slide 15, PS (4.94) ([[§C6b.3 Feynman Rules for Amplitudes#^cau-c6b-3-1|Caution: The sign of the external wave function]]) · the user's PHY 513 notes, Lecture 16 update, §16.6, Principles "Feynman rules for $iT$, position space" and "Feynman rules for $i\mathcal M$, momentum space", Derivation "From position space to momentum space" · PHY 513 Lecture 16, transcript ("We do not get a propagator coming from the external particle to the vertex. You only get it from one vertex to another … Did not involve an integral"; "That overall delta function you're not supposed to write down anyway") · proof written here*

^thm-c6b-3-3

> [!derivation]- Derivation
> **Step 1** (the matrix element at order $n$). By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], 2, and the Dyson series ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]]),
>
> $$
> \langle f|\hat S|i\rangle^{(n)} = \frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\int d^4z_1\cdots d^4z_n\;{}_0\langle\mathbf p_1\cdots|\,T\{\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}\,|\mathbf p_A\mathbf p_B\rangle_0 .
> $$
>
> **Step 2** (diagrams). By [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]] the matrix element is the sum over full contractions of the $4n$ legs and the particles, each a labelled diagram with the particles as external points; by [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]] the terms of $\langle f|i\hat T|i\rangle$ are the fully connected, amputated ones.
>
> **Step 3** (values in position space). A particle on a leg at $x$ gives $e^{-ip\cdot x}$ (incoming) or $e^{+ip\cdot x}$ (outgoing) ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 2; slide 15), a leg–leg pair $D_F(x - y)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]).
>
> **Step 4** ($\frac1S$). Relabelling the $n$ vertices and the four legs at each vertex, a group of order $n!\,(4!)^n$, maps contractions to contractions with the same integral (Step 5 of [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]]); the particles are not relabelled. By orbit–stabilizer a diagram $D$ arises from $n!\,(4!)^n/S(D)$ contractions ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]), and the prefactor of Step 1 becomes $\frac{1}{S(D)}(-i\lambda)^n$: each vertex $-i\lambda\int d^4x$, the whole $\frac1S$ (slide 22). A symmetry must fix every leg joined to a particle, so only loops and parallel internal lines can contribute to $S$: "$S$ simpler".
>
> **Step 5** (momentum space; slide 23, steps 1–3). Insert $D_F(x - y) = \int\frac{d^4p}{(2\pi)^4}\frac{i}{p^2 - m^2 + i\varepsilon}e^{-ip\cdot(x - y)}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]). Each vertex then carries four plane waves, from external lines or ends of propagators, and its integral is ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]])
>
> $$
> \int d^4x\,e^{-i(q_1 + q_2 + q_3 + q_4)\cdot x} = (2\pi)^4\delta^4(q_1 + q_2 + q_3 + q_4) ,
> $$
>
> $q_a$ the momenta flowing in (an outgoing particle's $e^{+ip\cdot x}$ is $q = -p$). The $I$ internal momenta and $V$ deltas leave, in a connected diagram, $L = I - V + 1$ integrals $\int\frac{d^4\ell}{(2\pi)^4}$ and one overall delta (Step 3 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]]).
>
> **Step 6** (strip the delta; slide 23, step 4). The overall delta is $(2\pi)^4\delta^4(p_A + p_B - \sum_fp_f)$, built from the external plane waves; what multiplies it is $i\mathcal M$ by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], with external line $1$.
>
> **Step 7** (checks). First order: one vertex, $L = 0$, $S = 1$, $i\mathcal M = -i\lambda$ ([[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1|Example §C6b.2.1]]). Second order: the three loop diagrams of [[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-3|Example §C6b.3.3]], $L = 1$, $S = 2$ each.
>
> **What the derivation shows.**
> - The rules for $i\mathcal M$ are the rules for correlation functions with external lines replaced by plane waves (position space) or by $1$ (momentum space); amputation is what makes the external propagators disappear.
> - The prescription of Principle §C6b.1.3 is the only heuristic input; at loop level its missing factors are the $\sqrt Z$ of LSZ.

^der-c6b-3-3

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C6a.8 Position-Space Feynman Rules#^der-c6a-8-1|Derivation §C6a.8.1]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!caution] Caution: The sign of the external wave function
> Slide 22 ("External line: vertex to incoming/outgoing particle $= e^{-ipx}$") and PS p. 114 (rule 3) write $e^{-ip\cdot x}$ for every external line. That is the wave function of an incoming particle; an outgoing particle gives $\langle\mathbf p|\hat\phi_I(x) = \langle0|\,e^{+ip\cdot x}$ ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 2; slide 15). The two agree if every momentum is counted as flowing into the vertex, an outgoing $p$ being an incoming $-p$, as in slide 23, step 2 ("each vertex has four Fourier factors $e^{-ipx}$").
>
> *Source: PHY 513 Lecture 16, slides 15, 22, 23 · PS §4.6, p. 110, eq. (4.94), p. 114 · the user's PHY 513 notes, Lecture 16 update, §16.6, Caution "The sign of the external wave function"*

^cau-c6b-3-1

> [!theorem] Theorem §C6b.3.4: Tree Diagrams of a Process; the s-, t-, u-Channels
> 1. A fully connected tree diagram of a process ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-2|Def. §C6b.3.2]]; the particles labelled and never relabelled) is fixed by its **shape**, the tree of vertices (with their types) and internal lines, and by **which particles sit at which vertex**, up to the symmetries of the shape that exchange vertices of one type together with their particles; the momentum of every internal line is then fixed by conservation ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], $L = 0$), and $S = 1$ ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]]).
> 2. In the cubic–quartic theory ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]), for $p_A + p_B \to p_1 + p_2$ at order $g^2$ and $\lambda$, the diagrams are exactly the $s$-, $t$- and $u$-channel exchanges, internal momentum $p_A + p_B$, $p_A - p_1$, $p_A - p_2$, and the contact diagram, and
>
> $$
> i\mathcal M = -ig^2\Bigl[\frac{1}{s - m^2 + i\varepsilon} + \frac{1}{t - m^2 + i\varepsilon} + \frac{1}{u - m^2 + i\varepsilon}\Bigr] - i\lambda ,
> $$
>
> $s$, $t$, $u$ as in [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]], $s + t + u = 4m^2$. In the physical region $s \ge 4m^2$ and $t, u \le 0$, so no denominator vanishes and the $i\varepsilon$ may be dropped. The amplitude is symmetric under $p_1 \leftrightarrow p_2$ ($t \leftrightarrow u$).
>
> *Model:* [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]; *applies:* tree level, the lowest order in each coupling, as [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]].
>
> *Source: PHY 513, Problem Set 8, Problem 2(a) (the diagrams; the user's solution: "The four external particles are labeled by their momenta and are never relabeled, so a diagram is determined by which external particles are attached to which vertex … putting $p_A$ on the other vertex only exchanges the two vertices") · the amplitude goes beyond what Problem Set 8 asked: derived here from [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]], checked against Schwartz §7.4, pp. 97–98, eqs. (7.91)–(7.96) (his $\mathcal L \ni +\frac{g}{3!}\phi^3$, vertex $ig$; each channel $\frac{-ig^2}{s - m^2 + i\varepsilon}$ etc.; Box 7.2) · PHY 513 Lecture 16 (the rules, slides 22–24)*

^thm-c6b-3-4

> [!derivation]- Derivation
> **Step 1** (part 1). By [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]], Step 4, a tree diagram has $S = 1$, so it is one orbit of contractions of size $|G|$, and its graph with the particles at the vertices is the whole datum. Given the shape and the assignment of particles to vertices, the legs at each vertex are filled in all $|G|$ ways by the same orbit; two assignments give the same diagram exactly when a symmetry of the shape (vertices of one type exchanged with their particles) maps one to the other. Momentum conservation at each vertex fixes the internal momenta, one for each of the $I = V - 1$ lines ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 2).
>
> **Step 2** (the diagrams at order $g^2$, $\lambda$). Order $g^2$: two cubic vertices, $\sum r = 6$, $E = 4$, $I = 1$, $L = 0$; by [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3, each vertex carries $3 - 1 = 2$ particles. The shape is one line between the vertices, its symmetry exchanges them; so a diagram is the partner of $p_A$: $p_B$ ($s$), $p_1$ ($t$), $p_2$ ($u$). Order $\lambda$: one quartic vertex with all four particles (contact). These are all diagrams with $(n_3, n_4) = (2, 0)$ or $(0, 1)$ ([[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-1|Example §C6b.3.1]], with the enumeration $9!! = 945$ pairings → $3$ connected diagrams).
>
> **Step 3** (internal momenta). Conservation at the vertex holding $p_A$: $s$: $q = p_A + p_B$; $t$: $p_A$ in, $p_1$ out, $q = p_A - p_1$; $u$: $q = p_A - p_2$. So $q^2 = s$, $t$, $u$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]).
>
> **Step 4** (values). Vertex $-ig$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]), internal line $\frac{i}{q^2 - m^2 + i\varepsilon}$, external lines $1$, $S = 1$:
>
> $$
> (-ig)\,\frac{i}{s - m^2 + i\varepsilon}\,(-ig) = \frac{(-i)^2\,i\,g^2}{s - m^2 + i\varepsilon} = \frac{-ig^2}{s - m^2 + i\varepsilon} ,
> $$
>
> since $(-i)^2i = -i$; the same with $t$, $u$. Contact: $-i\lambda$. Sum: the statement.
>
> **Step 5** (no pole in the physical region). In the centre-of-mass frame, equal masses: $p_A = (E, \mathbf p)$, $p_B = (E, -\mathbf p)$, $p_1 = (E, \mathbf p')$, $|\mathbf p'| = |\mathbf p|$, angle $\theta$:
>
> $$
> s = (2E)^2 = 4(\mathbf p^2 + m^2) \ge 4m^2 , \qquad t = (E - E)^2 - (\mathbf p - \mathbf p')^2 = -2\mathbf p^2(1 - \cos\theta) \le 0 ,
> $$
>
> and $u = -2\mathbf p^2(1 + \cos\theta) \le 0$; $s + t + u = 4\mathbf p^2 + 4m^2 - 4\mathbf p^2 = 4m^2$. None equals $m^2$ (for $m > 0$), so $\varepsilon \to 0$ may be taken (Schwartz p. 98).
>
> **Step 6** (check). Schwartz's $+\frac{g}{3!}\phi^3$ gives vertex $+ig$ and $(ig)^2 = (-ig)^2 = -g^2$: the same $-ig^2/(s - m^2 + i\varepsilon)$ per channel (his (7.93)–(7.95)); the sign of $g$ does not enter.
>
> **What the derivation shows.**
> - At tree level a $2 \to 2$ amplitude with one exchanged particle is a sum of poles in $s$, $t$, $u$; the contact term is a constant. With $\lambda \sim g^2/m^2$ (Problem Set 8) all four terms are of one order.

^der-c6b-3-4

*Uses:* [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]], [[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-1|Example §C6b.3.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-5|P6, step 5]]

![[ph-qft-c6b-3-2.svg]]
*[[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-4|Theorem §C6b.3.4]]: the four tree diagrams of $\phi\phi \to \phi\phi$ in the cubic–quartic theory with the momentum of the internal line (orange arrows) and the value of each diagram; cubic vertices orange, the quartic vertex blue. The diagrams themselves, with $S$, are [[§C6b.12 From the Question to the Formula#^ex-c6b-12-5|Example §C6b.12.5]]'s figure. Added figure.*

## Examples

> [!example] Example §C6b.3.1: Cubic–Quartic Theory, 2 → 2 at Order g² and λ
> ![[ph-qft-c6b-11-5.svg]]
>
> [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-4|Theorem §C6b.3.4]] states the result with its amplitude; the enumeration below is its proof for this case. $\mathcal L = \frac12(\partial_\mu\phi)^2 - \frac{m^2}{2}\phi^2 - \frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]), vertices $-ig$, $-i\lambda$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]); $p_A + p_B \to p_1 + p_2$. A diagram with $n_3$ cubic and $n_4$ quartic vertices is of order $g^{n_3}\lambda^{n_4}$ (Problem Set 8: treat $\lambda \sim g^2/m^2$ as the same order).
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

> [!example] Example §C6b.3.3: φφ → φφ at Order λ²
> ![[ph-qft-c6b-3-3.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the connected, amputated diagrams of $p_A + p_B \to p_1 + p_2$ at order $\lambda^2$ are exactly the three loops (a)–(c), each with $S = 2$, and with $P_s = p_A + p_B$, $P_t = p_A - p_1$, $P_u = p_A - p_2$ the momentum through the loop,
>
> $$
> i\mathcal M^{(2)} = \frac{(-i\lambda)^2}{2}\sum_{P = P_s, P_t, P_u}\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m^2 + i\varepsilon}\,\frac{i}{(P - q)^2 - m^2 + i\varepsilon} ;
> $$
>
> (d)–(f) are not diagrams of $i\mathcal M$. "A total of three diagrams at that order. It's not a humongous number."
>
> **Step 1** (legs and lines). Two quartic vertices, four particles: $\sum r_v = 8 = 4 + 2I$, $I = 2$; connected, $L = I - V + 1 = 1$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1–2). With $e_v$ particles at vertex $v$, the free legs number $(4 - e_1) + (4 - e_2) = 2I = 4$, so $e_1 + e_2 = 4$:
> - $(e_1, e_2) = (4, 0)$: $v_2$ closes on itself, the figure-eight beside the vertex, (d): not connected ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3), a vacuum bubble ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]], 2);
> - $(3, 1)$: the free leg of $v_1$ goes to $v_2$, the two other free legs of $v_2$ close a loop: a loop on the leg of the single particle at $v_2$, (f), four such diagrams; removing the line $v_2v_1$ separates that particle with its loop: not amputated ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]]);
> - $(2, 2)$ with a loop at each vertex: two pieces; one incoming and one outgoing particle at each vertex gives (e), two forward pieces, the $\mathbb 1$ ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]], 3); $p_A$, $p_B$ at one vertex gives $\delta^4(p_A + p_B)$, zero on shell ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]], 1);
> - $(2, 2)$ with both lines between $v_1$ and $v_2$: connected and amputated; a diagram is the partner of $p_A$ at its vertex, $p_B$ (a), $p_1$ (b), $p_2$ (c).
>
> **Step 2** ($S$). The particles are fixed; the only symmetry is the exchange of the two parallel lines: $S = 2$. Count: $|G| = 2!\,(4!)^2 = 1152$ relabellings, $576$ pairings per channel (the fish of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5|Example §C6a.9.5]] (c), with particles for external points), $1152/576 = 2$.
>
> **Step 3** (momenta). By [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]], in (a) $P_s$ enters the vertex of $p_A$, $p_B$ and leaves as $q$ and $P_s - q$ on the two lines; the vertex delta fixes the second line, the other vertex gives the overall $\delta^4(p_A + p_B - p_1 - p_2)$, and one integral $\int\frac{d^4q}{(2\pi)^4}$ is left ($L = 1$). In (b) the vertex of $p_A$ and $p_1$ passes $P_t = p_A - p_1$ into the loop, in (c) $P_u = p_A - p_2$. Each diagram: $\frac12(-i\lambda)^2\int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2 - m^2 + i\varepsilon}\frac{i}{(P - q)^2 - m^2 + i\varepsilon}$; the sum is the statement.
>
> **Step 4** (what the integral does at large $q$). The integrand falls like $\frac{1}{q^4}$, and $\int\frac{d^4q}{q^4}$ diverges logarithmically: making sense of it is renormalization (second semester). The dependence on $P_s^2 = s$, $P_t^2 = t$, $P_u^2 = u$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]) is the energy dependence the first order lacks.
>
> *Source: PHY 513 Lecture 16, slide 25 (the $s$-channel loop as the connected example; "2nd and 3rd diagram are not connected"), slide 26, and transcript ("total of three diagrams at that order. It's not a humongous number") · the user's PHY 513 notes, Lecture 16 update, §16.8 "Example: $2 \to 2$ at order $\lambda^2$" (eq. (oneloop), "The symmetry factor $2$ (filled in)", "Looking ahead") and Figure "connamp" · PS §4.6, eq. (4.101), p. 112*

^ex-c6b-3-3

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give the momentum deltas of the rules in momentum space.
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group and orbit–stabilizer behind $\frac1S$ and behind $S = 1$ for trees.

> [!remark]- Connections
> - What the rules drop is what §C6b.2 sorted out: $\delta$-lines and forward pieces are the $\mathbb 1$, bubbles the vacuum's normalization — [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]], [[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]].
> - Amputated leg corrections are not zero: they return as $\sqrt Z$ per external line and the physical mass, the LSZ formula — [[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]].
> - A tree amplitude with one exchanged particle is a sum of poles in the invariants of $2 \to 2$ kinematics — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]; the loop of Example §C6b.3.3 diverges logarithmically, the starting point of renormalization (second semester).
> - The vertex factors and lines are those of the correlation functions — [[§C6a.12 Feynman Rules for Polynomial Interactions|§C6a.12]]; the amputation route to the same $i\mathcal M$ and its LSZ form — [[§C6b.10 Amplitudes from Correlation Functions|§C6b.10]].
