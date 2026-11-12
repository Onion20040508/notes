---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.6, pp. 112–115, eqs. (4.101)–(4.104) and the rules for $\phi^4$ (p. 115) · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part C, slides 21–26, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.6–§16.9 · Yu Zhao-Huan, 量子场论讲义, §7.2, rules 6–11 (pp. 287–288); §7.3, pp. 294–296; §7.4, rules 1–5 (p. 300); §10.5.3 · Schwartz, Quantum Field Theory and the Standard Model, §7.4, pp. 97–98, eqs. (7.91)–(7.96) · PHY 513, Problem Set 8, Problem 2 (the user's solution, submitted 2026-10-30) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), transcript ("strip off the external lines") · PHY 513, Problem Set 9, Problem 3 (the user's solution, submitted 2026-11-05).*

Lecture 16, Part C, states the Feynman rules for the amplitude itself: "$i\mathcal M$ = sum over all connected, amputated diagrams". [[§C6c.2 Contractions with External Particles|§C6c.2]] expanded the $S$-matrix element between free particle states and sorted its terms ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]). The whole route in one line, as the user's notes summarize it (Principle "From the time-evolution operator to $i\mathcal M$"): expand ${}_0\langle\mathbf p_1\mathbf p_2\cdots|T\{e^{-i\int\hat H_I}\}|\mathbf p_A\mathbf p_B\rangle_0$ between free states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); Wick's theorem contracts fields with each other ($D_F$) or with particles (wave functions $e^{\mp ip\cdot z}$; [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]); omit particles going straight through ($\delta$-lines, the $\mathbb 1$), vacuum bubbles, and corrections on external legs (of the size of $\sqrt Z - 1$); what remains is $i\mathcal M$ with vertex $-i\lambda$, propagator $\frac{i}{p^2 - m^2 + i\varepsilon}$, external lines $1$, momentum conservation at each vertex, $\int\frac{d^4q}{(2\pi)^4}$ per loop and $\frac1S$.

Amputation ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]), $S = 1$ for saturated vertices and trees ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]) and $\phi\phi \to \phi\phi$ at order $\lambda^2$ are in [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors|§C6c.5]]. This section collects the rules: it defines the diagram of an amplitude ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]), shows that only the vertex depends on the interaction ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]]), gives the tree-level rules for any polynomial interaction ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]) and the rules at any order ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]], PS (4.103)–(4.104)), enumerates the tree diagrams of a process with the $s$-, $t$-, $u$-channels ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]), states which channels a vertex allows when several fields interact ([[§C6c.6 Feynman Rules for Amplitudes#^mod-c6c-6-5|Model §C6c.6.5]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|Theorem §C6c.6.6]]), and works the cubic–quartic diagrams of Problem Set 8 and the three-scalar process of Problem Set 9 ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-3|Example §C6c.6.3]]; the order-$\lambda^2$ loops of $\phi\phi \to \phi\phi$: [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]]). [[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]] reaches the same rules from the correlation functions of C6a by amputation, the route that generalizes through LSZ. Yu states the rules case by case in §7.2–§7.4, read off first-order $T$-matrix elements, and justifies them in §10.5.

**Setup and scope.** As in [[§C6c.2 Contractions with External Particles|§C6c.2]]: free relativistic states over $|0\rangle$ standing for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]), a permanent interaction ([[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]); exact at the lowest order of a process, beyond it $\sqrt Z$ per external line and the physical mass ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). Each box states its scope.

## The diagrams of an amplitude

> [!definition] Definition §C6c.6.1: Diagram of a Scattering Amplitude
> For a process with initial momenta $p_A, p_B, \dots$ and final momenta $p_1, p_2, \dots$, a **diagram of the amplitude** $i\mathcal M$ is a diagram ([[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]]; other vertices: [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]) such that
> 1. its external points are labelled by the external momenta, one per particle, and are never relabelled;
> 2. it is fully connected ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-1|Caution: "Connected" here means fully connected]]);
> 3. its external legs are amputated ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]]; [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]); for a tree this means: each external point is joined by a line without propagator to a vertex, and the momentum of every internal line is fixed by conservation at the vertices. Between particle states this is the contraction of a leg with the particle, a plane wave without propagator ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]).
>
> Its symmetry factor is that of [[§C6a.8 Position-Space Feynman Rules#^def-c6a-8-1|Def. §C6a.8.1]] with the labelled external points held fixed. Diagrams that are not fully connected are excluded: their pieces belong to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$ or to products of smaller processes ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]], [[§C6c.1 Amplitudes from Correlation Functions#^rem-c6c-1-1|Remark: Disconnected pieces beyond zeroth order]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction without derivatives, any order; used for $\mathcal M$ at lowest order ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]) and at every order ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]).
>
> *Source: PHY 513, Problem Set 8, Problem 2(a)–(b) (the user's solution: "The four external particles are labeled by their momenta and are never relabeled, so a diagram is determined by which external particles are attached to which vertex"; a vertex with too many external particles leaves two legs "contracted with each other, giving a disconnected diagram that does not contribute to the scattering amplitude") · PHY 513 Lecture 15, transcript ("strip off the external lines") · Yu §7.3 (external lines of $\langle f|iT|i\rangle$)*

^def-c6c-6-1

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!theorem] Theorem §C6c.6.1: The Line Factors Come from the Free Fields; the Interaction Fixes Only the Vertex
> In the Feynman rules for $\langle f|i\hat T|i\rangle$ of a polynomial interaction without derivatives ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]):
> 1. an **external line** is the contraction of a free field with a free particle, $e^{-ip\cdot x}$ incoming and $e^{+ip\cdot x}$ outgoing ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]]); in momentum space it is $1$, because the plane wave is used up in the vertex delta;
> 2. an **internal line** is the contraction of two free fields, $D_F^{(m_j)}(x - y)$, in momentum space $\frac{i}{q^2 - m_j^2 + i\varepsilon}$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]); its momentum is in general off shell ([[§C8.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8-6-2|Def. §C8.6.2]]);
> 3. momentum conservation at the vertices, the loop integrals and the $\frac1S$ do not depend on $\mathcal L_{\rm int}$ either;
> 4. only the **vertex** depends on $\mathcal L_{\rm int}$: strip the fields from a term $-g\prod_k\phi_k^{m_k}$, multiply by $i$ and by $\prod_km_k!$, giving $-ig\prod_km_k!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]).
>
> So the rules for a new interaction of the same fields need only its vertices; the line rules of other free fields (spinors, polarization vectors, $S_F$) follow from their free fields in the same way ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|§C6d.2, Theorem §C6d.2.1]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]], any polynomial interaction without derivatives; *applies:* every order, free relativistic states over $|0\rangle$ as in [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; beyond lowest order the external lines carry $\sqrt Z$ ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]), which also comes from the two-point function, not from the vertex.
>
> *Source: Yu §7.3, p. 292 ("the Feynman rules of the external and internal lines are determined by the free part of the Lagrangian, so they do not depend on the interaction theory and are general"); §7.2, p. 288 ("apart from rule 9 for the vertex, which has the form particular to the Yukawa interaction, the other rules are general"; the vertex: strip the fields from $\mathcal L_{\rm Y}$ and multiply by $i$); §7.4, p. 296 (the line rules of other free fields, "valid for every interaction") · PS §4.6, p. 114 ("the factor for an ingoing line is just the amplitude for that particle to be found at the vertex") · from the "What the derivation shows" of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-2|Derivation §C6c.6.2]]*

^thm-c6c-6-1

> [!derivation]- Derivation
> **Step 1** (part 1). [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2, and [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]]: $\overbracket{\hat\phi_I(x)|\mathbf p\rangle} = e^{-ip\cdot x}$ and $\overbracket{\langle\mathbf p|\hat\phi_I(x)} = e^{+ip\cdot x}$, computed from the mode expansion of the free field and $[\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$ alone. In momentum space the vertex integral $\int d^4x\,e^{-ip\cdot x}(\cdots)$ turns the plane wave into the momentum $p$ entering the vertex delta ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]], 2); after the deltas are used, nothing of the external line is left: factor $1$ (Step 5 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-2|Derivation §C6c.6.2]]).
>
> **Step 2** (part 2). A leg–leg contraction is $\langle0|T\{\hat\phi_{I,j}(x)\hat\phi_{I,j}(y)\}|0\rangle = D_F^{(m_j)}(x - y)$ for fields of one kind and $0$ otherwise ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]), with $D_F = \int\frac{d^4q}{(2\pi)^4}\frac{i\,e^{-iq\cdot(x - y)}}{q^2 - m_j^2 + i\varepsilon}$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]): a property of the free field of mass $m_j$.
>
> **Step 3** (part 3). The vertex deltas come from $\int d^4x\,e^{-i\sum q\cdot x}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]), the loop count $L = I - V + 1$ from the graph ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]]), and $S$ from the relabelling group of the diagram ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]); none involves the coupling.
>
> **Step 4** (part 4). The term $-g\prod_k\hat\phi_k^{m_k}$ enters the Dyson series as $i\int d^4x\,\mathcal L_{\rm int} = -ig\int d^4x\prod_k\hat\phi_k^{m_k}$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]); the $\prod_km_k!$ attachments of its legs give equal terms ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], 3). Examples: $\phi^4$, $-i\frac{\lambda}{4!}\cdot4! = -i\lambda$; $\Phi\phi^2$, $-i\mu\cdot1!\,2! = -2i\mu$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]]); Yukawa $-g\,\phi\bar\psi\psi$, $-ig$ (Yu rule 9, with his $\kappa$ for $g$; [[§C6d.4 First Order#^thm-c6d-4-4|§C6d.4, Theorem §C6d.4.4]]).
>
> **What the derivation shows.**
> - Every rule except the vertex is a statement about free fields; this is why the vertex is the only input when a new theory is written down ([[P6 Tree Amplitude from a Lagrangian|P6]]).

^der-c6c-6-1

*Uses:* [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

## The rules

> [!theorem] Theorem §C6c.6.2: Tree-Level Feynman Rules for iℳ
> For an interaction with the vertex data of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]] and a process with incoming momenta $k_1, \dots, k_n$ and outgoing $p_1, \dots, p_m$, none equal to an incoming one, the contribution of the tree diagrams of the amplitude ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]], with no loops) to $i\mathcal M$ is the sum over these diagrams of the product of:
> - each **external line**: $1$ (a particle or antiparticle of a complex field attaches to the leg of [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3);
> - each **vertex** of type $t$: $-ig_t\prod_km_{t,k}!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]);
> - each **internal line** of mass $m_j$: $\dfrac{i}{q^2 - m_j^2 + i\varepsilon}$, with $q$ fixed by four-momentum conservation at the vertices;
>
> with symmetry factor $S = 1$ for every tree diagram ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]) and the overall $(2\pi)^4\delta^4(\sum_ik_i - \sum_jp_j)$ stripped ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). These are the rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]] for diagrams without loops ($L = 0$, $S = 1$).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* tree level, free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]); at the lowest order of a process this is the amplitude; beyond it loops on external lines need $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; LSZ, second semester).
>
> *Source: PS §4.6, p. 114 (eq. (4.103): "sum of all connected, amputated Feynman diagrams"; "the factor for an ingoing line is just the amplitude for that particle to be found at the vertex"), p. 115 (rules 1–6) · Yu §7.2, rules 6–11 (pp. 287–288); §7.4, momentum-space rules 1–5 (p. 300); §7.3, p. 294 (tree diagrams have $S = 1$; [[§C6a.9 Symmetry Factors in Practice#^rem-c6a-9-3|§C6a.9, Remark: Yu's route]]) · PHY 513 Lecture 15, transcript ("strip off the external lines") · proof written here*

^thm-c6c-6-2

> [!derivation]- Derivation
> **Step 1** (order $\mathbf n$). With [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]] and Step 1 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]],
>
> $$
> \langle f|\hat S|i\rangle^{(\mathbf n)} = \prod_t\frac{(-ig_t)^{n_t}}{n_t!}\int\prod_{t,v}d^4z_{t,v}\;\langle\mathbf p_1\cdots\mathbf p_m|\,T\Bigl\{\prod_{t,v}M_t\bigl(\hat\phi_I(z_{t,v})\bigr)\Bigr\}|\mathbf k_1\cdots\mathbf k_n\rangle .
> $$
>
> **Step 2** (full contractions). By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]] (with kinds), the matrix element is a sum over full contractions of legs and particles; outgoing–incoming pairs vanish (distinct momenta). A full contraction is a labelled diagram whose external points are the particles, never relabelled ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]], 1). If it falls into several connected pieces, each piece carries its own momentum delta (Step 3 below): such terms are not of the form $\delta^4(\sum k - \sum p)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]] and do not belong to $\mathcal M$ ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]]; vacuum pieces are the phase of [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]]). Keep the fully connected ones.
>
> **Step 3** (values). A particle on a leg at $z$ gives $e^{-ik\cdot z}$ (incoming) or $e^{+ip\cdot z}$ (outgoing) ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2–3); a leg–leg pair gives $D_F^{(m_j)}(z - z')$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]). Relabelling vertices and legs of one kind leaves the integral unchanged, and orbit–stabilizer turns the prefactor into $\frac1S\prod_v(-ig_t\prod_km_{t,k}!)$ (Steps 3–5 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]], the particles playing the external points).
>
> **Step 4** ($S = 1$ for a tree). Every tree diagram of the amplitude has $S = 1$: [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]].
>
> **Step 5** (momentum space). Insert the Fourier form of every internal line and do the vertex integrals ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], Steps 1–2): each vertex gives $(2\pi)^4\delta^4(\text{momenta in} - \text{momenta out})$, the external momenta entering through the plane waves of Step 3. A tree has $L = I - V + 1 = 0$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 2): $V$ deltas, $I = V - 1$ internal momentum integrals. Each integral uses one delta and fixes its $q$; the last delta is
>
> $$
> (2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr) ,
> $$
>
> and what multiplies it is $\prod(\text{vertex factors})\prod\frac{i}{q^2 - m_j^2 + i\varepsilon}$. External lines leave no factor: their plane wave became part of a delta.
>
> **Step 6** (read off). Comparing with [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] strips the delta. Check: $\phi^4$, one vertex, $i\mathcal M = -i\lambda$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]); $\Phi\phi^2$, one vertex, $-2i\mu$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-4|Example §C6c.4.4]]).
>
> **What the derivation shows.**
> - The external line is $1$ because the contraction of a field with a relativistically normalized particle is a pure plane wave; the amputation of [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]] removes the external propagator to reach the same factor from a correlation function → [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]].
> - Nothing about loops was used except in Step 4; loop diagrams follow the same rules with $\frac1S$ and one $\int\frac{d^4\ell}{(2\pi)^4}$ per loop, but external-leg loops then need the $\sqrt Z$ of LSZ; stated as [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]].

^der-c6c-6-2

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-4|Derivation §C6a.12.4]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-2|Theorem §C6c.1.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3|Theorem §C6a.11.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, steps 4–6]]

> [!theorem] Theorem §C6c.6.3: Feynman Rules for iℳ, All Orders
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), for $p_A + p_B \to \{p_f\}$,
>
> $$
> i\mathcal M\,(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_fp_f\Bigr) = \Bigl(\text{sum of all connected, amputated diagrams with } p_A, p_B \text{ incoming, } p_f \text{ outgoing}\Bigr) ,
> $$
>
> connected meaning fully connected and amputated as in [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^def-c6c-5-1|Def. §C6c.5.1]] (the terms that remain by [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]), each diagram the product of
>
> | element | position space | momentum space |
> |---|---|---|
> | vertex (four line-ends meet) | $-i\lambda\int d^4x$ | $-i\lambda$, momentum conserved at the vertex (strip the four $\phi$ from $\mathcal L_{\rm int} = -\frac{\lambda}{4!}\phi^4$, $\times i$, $\times4!$: [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4\|Theorem §C6c.4.4]]) |
> | propagator between vertices at $x$, $y$ | $D_F(x - y)$ | $\dfrac{i}{p^2 - m^2 + i\varepsilon}$ |
> | external line, incoming $p$, at $x$ | $e^{-ip\cdot x}$ | $1$ |
> | external line, outgoing $p$, at $x$ | $e^{+ip\cdot x}$ | $1$ |
> | momentum not fixed by conservation | — | $\int\frac{d^4\ell}{(2\pi)^4}$, $L = I - V + 1$ of them ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]]) |
> | the diagram | $\frac1S$ | $\frac1S$ |
>
> and in momentum space the overall delta is stripped: $i\mathcal M$ = sum of all connected, amputated diagrams. *Equivalently,* these are the rules for correlation functions with the external propagators removed ([[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]): external lines become plane waves in position space and $1$ in momentum space. $S$ is the symmetry factor with the external particles held fixed ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]], 1): "$\mathcal M$ has less symmetry than the Green's function ⇒ $S$ simpler". For a polynomial interaction ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]) the vertex is $-ig_t\prod_km_{t,k}!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]) and each line carries the propagator of its field ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]). For diagrams without loops ($L = 0$, $S = 1$) these are the tree rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]: at the lowest order of a process exact as [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]; loop corrections on internal lines by these rules; corrections on external legs are excluded by amputation, and their $\sqrt Z$ and the physical mass are deferred ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; PS p. 115: "(4.103) still isn't quite correct … the modification affects only diagrams containing loops").
>
> *Source: PHY 513 Lecture 16, slides 22–24 (slide 22: "Vertex = 4 endpoints of lines meet = $-i\lambda\int d^4x$ … Propagator: line btw. vertices at $x$, $y$ = $D_F(x - y)$. External line: vertex to incoming/outgoing particle = $e^{-ipx}$. Symmetry factor: divide by $S$. $\mathcal M$ has less symmetry than Green's function ⇒ $S$ simpler"; slide 24: "'Loop' integration over momenta undetermined by conservation at each vertex") · PS §4.6, p. 114, eqs. (4.103)–(4.104), p. 115 (rules 1–6) · Yu §7.3, p. 296 · the outgoing plane wave $e^{+ip\cdot x}$: slide 15, PS (4.94) ([[§C6c.6 Feynman Rules for Amplitudes#^cau-c6c-6-1|Caution: The sign of the external wave function]]) · the user's PHY 513 notes, Lecture 16 update, §16.6, Principles "Feynman rules for $iT$, position space" and "Feynman rules for $i\mathcal M$, momentum space", Derivation "From position space to momentum space" · PHY 513 Lecture 16, transcript ("We do not get a propagator coming from the external particle to the vertex. You only get it from one vertex to another … Did not involve an integral"; "That overall delta function you're not supposed to write down anyway") · proof written here*

^thm-c6c-6-3

> [!derivation]- Derivation
> **Step 1** (the matrix element at order $n$). By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], 2, and the Dyson series ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-9|Theorem §C6a.3.9]]),
>
> $$
> \langle f|\hat S|i\rangle^{(n)} = \frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\int d^4z_1\cdots d^4z_n\;{}_0\langle\mathbf p_1\cdots|\,T\{\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}\,|\mathbf p_A\mathbf p_B\rangle_0 .
> $$
>
> **Step 2** (diagrams). By [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]] the matrix element is the sum over full contractions of the $4n$ legs and the particles, each a labelled diagram with the particles as external points; by [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]] the terms of $\langle f|i\hat T|i\rangle$ are the fully connected, amputated ones.
>
> **Step 3** (values in position space). A particle on a leg at $x$ gives $e^{-ip\cdot x}$ (incoming) or $e^{+ip\cdot x}$ (outgoing) ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2; slide 15), a leg–leg pair $D_F(x - y)$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]]).
>
> **Step 4** ($\frac1S$). The $n!\,(4!)^n$ relabellings of vertices and legs leave the integral unchanged, and a diagram $D$ arises from $n!\,(4!)^n/S(D)$ contractions: [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]. The prefactor of Step 1 becomes $\frac{1}{S(D)}(-i\lambda)^n$: each vertex $-i\lambda\int d^4x$ (the $\frac{1}{4!}$ cancelled, [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]; the $\frac{1}{n!}$ cancelled, [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]), the whole $\frac1S$ (slide 22); with the particles fixed only loops and parallel lines give $S > 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|Theorem §C6c.5.4]]): "$S$ simpler".
>
> **Step 5** (momentum space; slide 23, steps 1–3). Insert $D_F(x - y) = \int\frac{d^4p}{(2\pi)^4}\frac{i}{p^2 - m^2 + i\varepsilon}e^{-ip\cdot(x - y)}$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]). Each vertex then carries four plane waves, from external lines or ends of propagators, and its integral is ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]])
>
> $$
> \int d^4x\,e^{-i(q_1 + q_2 + q_3 + q_4)\cdot x} = (2\pi)^4\delta^4(q_1 + q_2 + q_3 + q_4) ,
> $$
>
> $q_a$ the momenta flowing in (an outgoing particle's $e^{+ip\cdot x}$ is $q = -p$). The $I$ internal momenta and $V$ deltas leave, in a connected diagram, $L = I - V + 1$ integrals $\int\frac{d^4\ell}{(2\pi)^4}$ and one overall delta (Step 3 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]]).
>
> **Step 6** (strip the delta; slide 23, step 4). The overall delta is $(2\pi)^4\delta^4(p_A + p_B - \sum_fp_f)$, built from the external plane waves; what multiplies it is $i\mathcal M$ by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], with external line $1$.
>
> **Step 7** (checks). First order: one vertex, $L = 0$, $S = 1$, $i\mathcal M = -i\lambda$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]). Second order: the three loop diagrams of [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^ex-c6c-5-1|Example §C6c.5.1]], $L = 1$, $S = 2$ each.
>
> **What the derivation shows.**
> - The rules for $i\mathcal M$ are the rules for correlation functions with external lines replaced by plane waves (position space) or by $1$ (momentum space); amputation is what makes the external propagators disappear (the equivalence sentence of the theorem; [[§C6c.1 Amplitudes from Correlation Functions#^thm-c6c-1-1|Theorem §C6c.1.1]]).
> - The prescription of Principle §C6b.1.3 is the only heuristic input; at loop level its missing factors are the $\sqrt Z$ of LSZ ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]).

^der-c6c-6-3

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-9|Theorem §C6a.3.9]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-2|Theorem §C2b.7.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-4|Theorem §C6c.5.4]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!caution] Caution: The sign of the external wave function
> Slide 22 ("External line: vertex to incoming/outgoing particle $= e^{-ipx}$") and PS p. 114 (rule 3) write $e^{-ip\cdot x}$ for every external line. That is the wave function of an incoming particle; an outgoing particle gives $\langle\mathbf p|\hat\phi_I(x) = \langle0|\,e^{+ip\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2; slide 15). The two agree if every momentum is counted as flowing into the vertex, an outgoing $p$ being an incoming $-p$, as in slide 23, step 2 ("each vertex has four Fourier factors $e^{-ipx}$").
>
> *Source: PHY 513 Lecture 16, slides 15, 22, 23 · PS §4.6, p. 110, eq. (4.94), p. 114 · the user's PHY 513 notes, Lecture 16 update, §16.6, Caution "The sign of the external wave function"*

^cau-c6c-6-1

> [!theorem] Theorem §C6c.6.4: Tree Diagrams of a Process; the s-, t-, u-Channels
> 1. A fully connected tree diagram of a process ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]; the particles labelled and never relabelled) is fixed by its **shape**, the tree of vertices (with their types) and internal lines, and by **which particles sit at which vertex**, up to the symmetries of the shape that exchange vertices of one type together with their particles; the momentum of every internal line is then fixed by conservation ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], $L = 0$), and $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]).
> 2. In the cubic–quartic theory ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]), for $p_A + p_B \to p_1 + p_2$ at order $g^2$ and $\lambda$, the diagrams are exactly the $s$-, $t$- and $u$-channel exchanges, internal momentum $p_A + p_B$, $p_A - p_1$, $p_A - p_2$, and the contact diagram, and
>
> $$
> i\mathcal M = -ig^2\Bigl[\frac{1}{s - m^2 + i\varepsilon} + \frac{1}{t - m^2 + i\varepsilon} + \frac{1}{u - m^2 + i\varepsilon}\Bigr] - i\lambda ,
> $$
>
> $s$, $t$, $u$ as in [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]], $s + t + u = 4m^2$. In the physical region $s \ge 4m^2$ and $t, u \le 0$, so no denominator vanishes and the $i\varepsilon$ may be dropped. The amplitude is symmetric under $p_1 \leftrightarrow p_2$ ($t \leftrightarrow u$).
>
> *Model:* [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]; *applies:* tree level, the lowest order in each coupling, as [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]].
>
> *Source: PHY 513, Problem Set 8, Problem 2(a) (the diagrams; the user's solution: "The four external particles are labeled by their momenta and are never relabeled, so a diagram is determined by which external particles are attached to which vertex … putting $p_A$ on the other vertex only exchanges the two vertices") · the amplitude goes beyond what Problem Set 8 asked: derived here from [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]], checked against Schwartz §7.4, pp. 97–98, eqs. (7.91)–(7.96) (his $\mathcal L \ni +\frac{g}{3!}\phi^3$, vertex $ig$; each channel $\frac{-ig^2}{s - m^2 + i\varepsilon}$ etc.; Box 7.2) · PHY 513 Lecture 16 (the rules, slides 22–24)*

^thm-c6c-6-4

> [!derivation]- Derivation
> **Step 1** (part 1). By [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]], a tree diagram has $S = 1$, so it is one orbit of contractions of size $|G|$, and its graph with the particles at the vertices is the whole datum. Given the shape and the assignment of particles to vertices, the legs at each vertex are filled in all $|G|$ ways by the same orbit; two assignments give the same diagram exactly when a symmetry of the shape (vertices of one type exchanged with their particles) maps one to the other. Momentum conservation at each vertex fixes the internal momenta, one for each of the $I = V - 1$ lines ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 2).
>
> **Step 2** (the diagrams at order $g^2$, $\lambda$). Order $g^2$: two cubic vertices, $\sum r = 6$, $E = 4$, $I = 1$, $L = 0$; by [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3, each vertex carries $3 - 1 = 2$ particles. The shape is one line between the vertices, its symmetry exchanges them; so a diagram is the partner of $p_A$: $p_B$ ($s$), $p_1$ ($t$), $p_2$ ($u$). Order $\lambda$: one quartic vertex with all four particles (contact). These are all diagrams with $(n_3, n_4) = (2, 0)$ or $(0, 1)$ ([[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]], with the enumeration $9!! = 945$ pairings → $3$ connected diagrams).
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
> - At tree level a $2 \to 2$ amplitude with one exchanged particle is a sum of poles in $s$, $t$, $u$; the contact term is a constant. With $\lambda \sim g^2/m^2$ (Problem Set 8) all four terms are of one order (part 2 of the statement).

^der-c6c-6-4

*Uses:* [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]], [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-5|P6, step 5]]

![[ph-qft-c6b-3-2.svg]]
*[[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]: the four tree diagrams of $\phi\phi \to \phi\phi$ in the cubic–quartic theory with the momentum of the internal line (orange arrows) and the value of each diagram; cubic vertices orange, the quartic vertex blue. The diagrams themselves, with $S$: the figure of [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]] (the same figure heads [[§C6c.8 From the Question to the Formula#^ex-c6c-8-5|Example §C6c.8.5]]). Added figure.*

## Several fields: which channels exist

> [!model] Model §C6c.6.5: The Three-Scalar Theory
> Three real scalar fields $\phi_1$, $\phi_2$, $\phi_3$ of masses $m_1$, $m_2$, $m_3 > 0$ with
>
> $$
> \mathcal L = \frac12\sum_{i=1}^3\bigl(\partial_\mu\phi_i\,\partial^\mu\phi_i - m_i^2\phi_i^2\bigr) - g\,\phi_1\phi_2\phi_3 ,
> $$
>
> $g$ a real coupling of mass dimension $1$, as the cubic coupling of [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]].
> 1. *Structure.* The state space is the product of three free scalar Fock spaces ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] for each mass), free vacuum $|0\rangle$; the three fields have independent mode operators, and two fields contract only with their own kind, $\overbracket{\hat\phi_i(z_1)\hat\phi_j(z_2)} = \delta_{ij}D_F^{(m_i)}(z_1 - z_2)$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]).
> 2. *Interaction.* $\mathcal L_{\rm int} = -g\phi_1\phi_2\phi_3$ has no derivatives, so the conjugate momenta are those of the free theory and $\mathcal H_{\rm int} = -\mathcal L_{\rm int} = g\,\phi_1\phi_2\phi_3$, as for $\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-4|Theorem §C6a.1.4]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]]).
> 3. *Vertex.* One vertex type, with one leg of each of $\phi_1$, $\phi_2$, $\phi_3$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]); its factor is $-ig\cdot1!\,1!\,1! = -ig$: a vertex of distinct fields has a trivial within-vertex group ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> *Assumptions:* those of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (stable particles of masses $m_i$, $g$ small); if one mass exceeds the sum of the other two, that particle decays into them ([[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* the theory itself; its $S$-matrix by the rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]], at lowest order exactly.
>
> *Source: PHY 513, Problem Set 9, Problem 3 (statement, Larsen) · items 1–3 written here*

^mod-c6c-6-5

> [!theorem] Theorem §C6c.6.6: The Vertex Content Decides Which Channels Exist
> 1. In a $2 \to 2$ tree diagram with two vertices and one internal line ($I = 1$, $L = 0$), each vertex carries two external particles ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3), and a particle of field $k$ attaches only to a leg of kind $k$. A channel, the choice of the partner of $p_A$ at its vertex, exists only if some vertex type has legs of the kinds of that pair, and the two leftover legs can be contracted with each other ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]], 1): the vertex content decides which of $s$, $t$, $u$ occur, before any calculation.
> 2. In the three-scalar theory ([[§C6c.6 Feynman Rules for Amplitudes#^mod-c6c-6-5|Model §C6c.6.5]]), for $\phi_1(p_A) + \phi_1(p_B) \to \phi_2(p_1) + \phi_2(p_2)$ at order $g^2$, a vertex has one $\phi_1$ leg, so the two incoming $\phi_1$ cannot meet: **no $s$-channel**. The $t$-channel ($p_A$, $p_1$ at one vertex) and the $u$-channel ($p_A$, $p_2$) exist, and the internal line is a $\phi_3$ with momentum $p_A - p_1$, respectively $p_A - p_2$.
> 3. *Instances:* one kind of field (cubic–quartic theory) gives all three channels ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], 2); the Yukawa vertex $\bar\psi\psi\phi$ has one $\psi$ leg, so two incoming fermions cannot meet: $ff \to ff$ has $t$ and $u$ only ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]), $f\bar f \to f\bar f$ has $s$ and $t$ ([[§C6d.5 Second Order#^ex-c6d-5-1|★ Example §C6d.5.1]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with any interaction of the form of [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]] (Yukawa alike); *applies:* tree level, two vertices, every channel counted with the particles labelled.
>
> *Source: PHY 513, Problem Set 9, Problem 3(a) (the user's solution: "Each vertex has exactly one leg of each of $\phi_1$, $\phi_2$, $\phi_3$ … one $\phi_1$ and one $\phi_2$ on each vertex. The remaining $\phi_3$ legs … form the internal line") · stated in general here*

^thm-c6c-6-6

> [!derivation]- Derivation
> **Step 1** (two particles per vertex). Two vertices, four external particles, one internal line: by [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3, a connected diagram with $V = 2$, $I = 1$ has $r_v - 1$ external particles at each vertex; for cubic vertices two each.
>
> **Step 2** (kinds). An incoming particle of field $k$ is absorbed by $\hat\phi_k^+$, an outgoing one emitted by $\hat\phi_k^-$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]); the fields of other kinds have independent mode operators and give zero on it ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]). So the two particles at a vertex occupy two legs of their own kinds, and the third legs of the two vertices form the internal line, which needs a nonzero contraction ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], 1–2).
>
> **Step 3** (part 2). The vertex legs are $\phi_1\phi_2\phi_3$. $\{p_A, p_B\}$ = two $\phi_1$: one vertex has one $\phi_1$ leg, impossible. $\{p_A, p_1\}$ = $\phi_1\phi_2$: the other vertex takes $\{p_B, p_2\}$ = $\phi_1\phi_2$, and both leftover legs are $\phi_3$, contracted by $D_F^{(m_3)}$. Likewise $\{p_A, p_2\}$. Momentum conservation at the vertex of $p_A$ gives the internal momentum ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], 1).
>
> **Step 4** (part 3). The cubic–quartic vertex $\phi\phi\phi$ takes any pair, and its leftover $\phi$ contracts with the other: $s$, $t$, $u$. The Yukawa vertex has one leg each of $\psi$ (absorbs an incoming fermion or emits an outgoing antifermion) and $\bar\psi$ (emits an outgoing fermion or absorbs an incoming antifermion) ([[§C6d.2 Contractions with External Fermions|§C6d.2]]); two incoming fermions would need two $\psi$ legs.
>
> **What the derivation shows**
> - An $s$-channel line is a particle that $a + b$ can produce at one vertex; the vertex content decides whether it exists.

^der-c6c-6-6

*Uses:* [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]]

## Examples

> [!example] Example §C6c.6.1: Cubic–Quartic Theory, 2 → 2 at Order g² and λ
> ![[ph-qft-c6b-11-5.svg]]
>
> [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]] states the result with its amplitude; the enumeration below is its proof for this case. $\mathcal L = \frac12(\partial_\mu\phi)^2 - \frac{m^2}{2}\phi^2 - \frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]), vertices $-ig$, $-i\lambda$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]); $p_A + p_B \to p_1 + p_2$. A diagram with $n_3$ cubic and $n_4$ quartic vertices is of order $g^{n_3}\lambda^{n_4}$ (Problem Set 8: treat $\lambda \sim g^2/m^2$ as the same order).
> - *$O(g^2)$, two cubic vertices*: $6$ legs, $4$ joined to external lines, so one internal line ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 1: $6 = 4 + 2I$; $L = 1 - 2 + 1 = 0$, a tree). If one vertex carried three external particles, the other would carry one, and its two remaining legs would be contracted with each other: not fully connected ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-3|Theorem §C6a.12.3]], 3), excluded ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]). So each vertex carries two, and $p_A$ shares its vertex with exactly one of $p_B$, $p_1$, $p_2$ (putting $p_A$ on the other vertex only exchanges the vertices): three diagrams.
> - *$O(\lambda)$, one quartic vertex*: all four on it, one diagram.
>
> | diagram | at one vertex | at the other | internal momentum |
> |---|---|---|---|
> | $s$-channel | $p_A, p_B$ | $p_1, p_2$ | $p_A + p_B$ |
> | $t$-channel | $p_A, p_1$ | $p_B, p_2$ | $p_A - p_1$ |
> | $u$-channel | $p_A, p_2$ | $p_B, p_1$ | $p_A - p_2$ |
> | contact | $p_A, p_B, p_1, p_2$ | — | — |
>
> Each has $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]]): the cubic vertices carry $2 = 3 - 1$ external lines, the quartic one $4$. Enumeration: the $9!! = 945$ pairings at order $g^2$ form $31$ diagrams, of which exactly these $3$ are fully connected, each an orbit of $72 = 2!\,(3!)^2 = |G|$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(a) (the user's solution: diagrams drawn and with vertices opened into their legs) · checked with `qft-C/tools/hw8/check_hw8.py`*

^ex-c6c-6-1

> [!example] Example §C6c.6.2: Cubic–Quartic Theory, 2 → 3 at Order gλ
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
> $1 + 6 + 3 = 10$. All have $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-5|Theorem §C6c.5.5]], Step 3: $N_D = 144 = 3!\,4! = |G|$; there is one vertex of each type, so $G$ contains no vertex permutations). Enumeration: the $11!! = 10\,395$ pairings of the $12$ half-edges form $195$ diagrams, exactly $10$ of them fully connected, each an orbit of $144$.
>
> *Source: PHY 513, Problem Set 8, Problem 2(b)–(c) (the user's solution) · checked with `qft-C/tools/hw8/check_hw8.py`*

^ex-c6c-6-2

![[ph-qft-c6-17-1.svg]]
*The diagrams of [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-1|Example §C6c.6.1]] and [[§C6c.6 Feynman Rules for Amplitudes#^ex-c6c-6-2|Example §C6c.6.2]] (cubic vertices orange, quartic blue; incoming momenta left, outgoing right). Top: $2 \to 2$, the $s$-, $t$-, $u$-channel diagrams at order $g^2$ and the contact diagram at order $\lambda$. Bottom: $2 \to 3$ at order $g\lambda$, one representative of each class (I), (II), (III). Added figure, adapted from the user's solution of PHY 513, Problem Set 8, Problem 2.*

> [!example] Example §C6c.6.3: φ₁φ₁ → φ₂φ₂ at Order g² in the Three-Scalar Theory
> ![[ph-qft-c6c-6-1.svg]]
>
> In the three-scalar theory ([[§C6c.6 Feynman Rules for Amplitudes#^mod-c6c-6-5|Model §C6c.6.5]]), for $\phi_1(p_A) + \phi_1(p_B) \to \phi_2(p_1) + \phi_2(p_2)$ at order $g^2$,
>
> $$
> \mathcal M = -g^2\Bigl[\frac{1}{(p_A - p_1)^2 - m_3^2} + \frac{1}{(p_A - p_2)^2 - m_3^2}\Bigr] , \qquad \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{|\mathbf p_1|}{64\pi^2E_{\rm cm}^2\,|\mathbf p_A|}\,|\mathcal M|^2 :
> $$
>
> the $t$- and $u$-channel exchange of a $\phi_3$, no $s$-channel ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|Theorem §C6c.6.6]], 2), and the $i\varepsilon$ dropped because $t, u \le 0$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]], 5).
>
> **Step 1** (the diagrams). $O(g^2)$ means two vertices. Each vertex has exactly one leg of each of $\phi_1$, $\phi_2$, $\phi_3$, so two vertices have two legs of each field. The two incoming $\phi_1$ and the two outgoing $\phi_2$ use up all the $\phi_1$ and $\phi_2$ legs, one $\phi_1$ and one $\phi_2$ on each vertex; the remaining $\phi_3$ legs, one on each vertex, form the internal line. The particles are labelled, so a diagram is fixed by which of $p_1$, $p_2$ shares a vertex with $p_A$ (putting $p_A$ on the other vertex only exchanges the vertices): two diagrams, (t) and (u) in the figure.
>
> **Step 2** (the expansion term). $\langle p_1p_2|i\hat T|p_Ap_B\rangle = (2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)\,i\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]), with $\hat S = \mathbb 1 + i\hat T = T\exp\bigl(-i\int d^4z\,\mathcal H_I\bigr)$ and $\mathcal H_I = g\,\hat\phi_1\hat\phi_2\hat\phi_3$. The initial state holds $\phi_1$ particles and the final state $\phi_2$ particles, so the $\mathbb 1$ does not contribute, and at $O(g^2)$
>
> $$
> \langle p_1p_2|i\hat T|p_Ap_B\rangle = \langle p_1p_2|\,\frac{(-ig)^2}{2!}\int d^4z_1\,d^4z_2\;T\bigl\{(\hat\phi_1\hat\phi_2\hat\phi_3)(z_1)\,(\hat\phi_1\hat\phi_2\hat\phi_3)(z_2)\bigr\}\,|p_Ap_B\rangle .
> $$
>
> **Step 3** (the contractions). With $|p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$, only the annihilation part of a field acts on an incoming particle of its own type, and only the creation part on an outgoing one ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]):
>
> $$
> \hat\phi_i(z)\,|p\rangle \to e^{-ip\cdot z} , \qquad \langle p|\,\hat\phi_i(z) \to e^{ip\cdot z} .
> $$
>
> Two fields contract only with their own type ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]), with the propagator of mass $m_i$:
>
> $$
> \overbracket{\hat\phi_i(z_1)\hat\phi_i(z_2)} = D_F^{(i)}(z_1 - z_2) = \int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m_i^2 + i\varepsilon}\,e^{-iq\cdot(z_1 - z_2)} .
> $$
>
> **Step 4** (the coefficient). The group $G$ relabels the two vertices and permutes legs of the same field within a vertex. Each vertex has one leg of each field, so the within-vertex group is trivial and $|G| = 2!\cdot1\cdot1 = 2$, matching the prefactor $\frac{1}{2!}$ (vertex factor $-ig$, [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]). The particles are labelled, so the diagram has no nontrivial symmetry, $S = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]), and the number of contractions giving it is $N = |G|/S = 2$ (the pair $\{p_A, p_1\}$ on $z_1$ or on $z_2$). The coefficient is $N/|G| = 1$ ([[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-2|Theorem §C6c.5.2]]).
>
> **Step 5** (diagram (t)). With $z_1$ the vertex carrying $p_A$, $p_1$, replacing each contraction by its value and doing the vertex integrals ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]),
>
> $$
> \begin{aligned}
> &(-ig)^2\int d^4z_1\,d^4z_2\;e^{-ip_A\cdot z_1}\,e^{ip_1\cdot z_1}\,D_F^{(3)}(z_1 - z_2)\,e^{-ip_B\cdot z_2}\,e^{ip_2\cdot z_2} \\
> &= (-ig)^2\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m_3^2 + i\varepsilon}\int d^4z_1\,e^{-i(p_A - p_1 + q)\cdot z_1}\int d^4z_2\,e^{-i(p_B - p_2 - q)\cdot z_2} \\
> &= (-ig)^2\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m_3^2 + i\varepsilon}\;(2\pi)^4\delta^4(p_A - p_1 + q)\,(2\pi)^4\delta^4(p_B - p_2 - q) .
> \end{aligned}
> $$
>
> In $D_F^{(3)}(z_1 - z_2)$ the phase $e^{-iq\cdot(z_1 - z_2)}$ means that $q$ flows from $z_2$ into $z_1$. The first delta fixes $q = p_1 - p_A$ and does the $q$ integral; the second becomes $\delta^4(p_A + p_B - p_1 - p_2)$:
>
> $$
> (-ig)^2\,\frac{i}{(p_A - p_1)^2 - m_3^2 + i\varepsilon}\;(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) .
> $$
>
> **Step 6** (diagram (u)). The same with $p_1 \leftrightarrow p_2$: the deltas are $\delta^4(p_A - p_2 + q)\,\delta^4(p_B - p_1 - q)$, the first fixes $q = p_2 - p_A$, and the diagram is $(-ig)^2\,\frac{i}{(p_A - p_2)^2 - m_3^2 + i\varepsilon}\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)$.
>
> **Step 7** (the amplitude). The sum of the two diagrams, compared with Step 2:
>
> $$
> \langle p_1p_2|i\hat T|p_Ap_B\rangle = (-ig)^2\Bigl[\frac{i}{(p_A - p_1)^2 - m_3^2 + i\varepsilon} + \frac{i}{(p_A - p_2)^2 - m_3^2 + i\varepsilon}\Bigr](2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) ,
> $$
>
> and $(-ig)^2\,i = -ig^2$ gives the $\mathcal M$ of the statement, where the $i\varepsilon$ is dropped: in the centre-of-mass frame both $\phi_1$'s and both $\phi_2$'s have energy $E_{\rm cm}/2$, so $E_A = E_1 = E_2$ and $(p_A - p_{1,2})^2 = (E_A - E_{1,2})^2 - |\mathbf p_A - \mathbf p_{1,2}|^2 = -|\mathbf p_A - \mathbf p_{1,2}|^2 \le 0$, a Lorentz-invariant statement, so $(p_A - p_{1,2})^2 - m_3^2 \le -m_3^2 < 0$ and the denominators do not vanish ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]], 5).
>
> **Step 8** (the cross section). For $2 \to 2$ in the centre-of-mass frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]])
>
> $$
> \Bigl(\frac{d\sigma}{d\Omega}\Bigr)_{\rm cm} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\,\frac{|\mathbf p_1|}{16\pi^2E_{\rm cm}}\,|\mathcal M|^2 .
> $$
>
> In this frame $\mathbf p_B = -\mathbf p_A$, and both incoming particles have mass $m_1$, so $E_A = E_B = \sqrt{|\mathbf p_A|^2 + m_1^2} = E_{\rm cm}/2$. With $\mathbf v = \mathbf p/E$, $|\mathbf v_A - \mathbf v_B| = \bigl|\frac{\mathbf p_A}{E_A} + \frac{\mathbf p_A}{E_B}\bigr| = \frac{2|\mathbf p_A|}{E_A} = \frac{4|\mathbf p_A|}{E_{\rm cm}}$, so $2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B| = E_{\rm cm}^2\cdot\frac{4|\mathbf p_A|}{E_{\rm cm}} = 4|\mathbf p_A|\,E_{\rm cm}$, and the statement follows. It is part 3 of [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]] with $\beta_f/\beta_i = |\mathbf p_1|/|\mathbf p_A|$. (Integrated over all directions, the two identical $\phi_2$ would add $\frac{1}{S_{\rm id}} = \frac12$, [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]]; Problem 3 asks only for $d\sigma/d\Omega$.)
>
> *Source: PHY 513, Problem Set 9, Problem 3(a)–(c) (the user's solution; the figure follows the user's drawings, with the vertices opened into their legs)*

^ex-c6c-6-3

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give the momentum deltas of the rules in momentum space.
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group and orbit–stabilizer behind $\frac1S$ and behind $S = 1$ for trees (used through [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]] and [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-6|Theorem §C6c.5.6]]).
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]] — labelled diagrams with vertices of any type, which a diagram of an amplitude is built from.

> [!remark]- Connections
> - What the rules drop is what §C6c.3–§C6c.5 sorted out: $\delta$-lines and forward pieces are the $\mathbb 1$, bubbles the vacuum's normalization — [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]].
> - A tree amplitude with one exchanged particle is a sum of poles in the invariants of $2 \to 2$ kinematics — [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]]; the loop of Example §C6c.5.1 diverges logarithmically, the starting point of renormalization (second semester).
> - Several fields: the vertex content selects the channels, and with masses equal in pairs the exchange denominators of the $t$- and $u$-channels never vanish — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-6|Theorem §C6c.6.6]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-7|Theorem §C6b.4.7]], 5.
> - With fermions the same rules hold with spinors on external lines, $S_F$ on internal ones, a sign per contraction pattern and no symmetry factors — [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|§C6d.6, Theorem §C6d.6.2]].
> - The vertex factors and lines are those of the correlation functions — [[§C6a.12 Feynman Rules for Polynomial Interactions|§C6a.12]]; the amputation route to the same $i\mathcal M$ and its LSZ form — [[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]].
> - With fermions too only the vertex is theory-specific, but the relative signs of several diagrams must be taken from the contractions — [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|Theorem §C6d.6.1]], [[§C6d.6 Momentum-Space Feynman Rules#^cau-c6d-6-1|§C6d.6, Caution: Relative signs still need the contractions]].
