---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.1 Amplitudes from Correlation Functions]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.3 Wick's Theorem between Particle States]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.6, pp. 109–113, eqs. (4.89)–(4.98), (4.101)–(4.102) (contractions with external states (4.93)–(4.94); $\phi\phi \to \phi\phi$ (4.98)) · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part B, slides 10–18, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.3–§16.4 · Yu Zhao-Huan, 量子场论讲义, §7.1, pp. 262–272, eqs. (7.13)–(7.24) (contractions of fields with initial and final particles; the first-order $T$-matrix elements of Yukawa theory, Fig. 7.1–7.2, and the kinematic filter, p. 272), p. 268 (boxed contraction rule), p. 281 (boxed $n!$ rule), eqs. (7.86)–(7.87); §7.3, eqs. (7.112)–(7.121); §7.4, eqs. (7.133)–(7.142) · PHY 513, Problem Set 8, Problems 2, 3(d)–(e) and 4 (the user's solutions, submitted 2026-10-30) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), transcript ("strip off the external lines").*

[[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]] defined the matrix elements $\langle f|i\hat T|i\rangle$ and the amplitude $\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). This section computes them from the Dyson series with particles, not the vacuum, on both sides. The new step is a contraction of a field with an external particle: a field annihilates an incoming particle or creates an outgoing one, and each such contraction is a plane wave ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]). With it Wick's theorem holds between particle states ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]), and its terms sort into the $\mathbb 1$ (particles passing through on $\delta$-lines, [[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]), vacuum bubbles, corrections of the external states, and the scattering ([[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-3|Theorem §C6c.3.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]; Lecture 16, Part B). At first order this gives Yu's procedure: list every matrix element the interaction allows, then keep those that energy-momentum conservation allows ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]]). At higher order it gives the Feynman rules for $i\mathcal M$, the subject of [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] ([[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]]). Problem Set 8 had to build these tools by hand (Problems 3 and 4). [[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]] reaches the same rules from the correlation functions of C6a by amputation, the route that generalizes beyond lowest order (LSZ). Yu computes $S$-matrix elements this way from the start (§7.1–§7.4); PS do it in §4.6 (eqs. (4.89)–(4.98)); Lecture 16, Part B, does it for $2 \to 2$ in $\phi^4$.

The chapter follows Yu's order (§7.1–§7.3) with $\phi^4$ as the running theory: this section holds the contractions themselves, with one particle ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]), the overlap of two $n$-particle states, the pair in which no field takes part ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-3|Lemma §C6c.2.3]]), with $n$ identical particles ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]]) and read in both directions ([[§C6c.2 Contractions with External Particles#^thm-c6c-2-5|Theorem §C6c.2.5]]); Wick's theorem between particle states is [[§C6c.3 Wick's Theorem between Particle States|§C6c.3]], first order [[§C6c.4 First Order꞉ Enumerate, then Filter|§C6c.4]], second order [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors|§C6c.5]], the collected rules [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]. The fermion counterpart of each section is in [[· C6d Feynman Rules for Fermions|C6d]].

**Setup and scope.** The in and out states are free Fock states over the free vacuum $|0\rangle$, relativistically normalized ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), $|i\rangle = |\mathbf k_1\cdots\mathbf k_n\rangle$, $\langle f| = \langle\mathbf p_1\cdots\mathbf p_m|$. Between them the interaction-picture evolution operator acts ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]):
$$
\langle f|\hat S|i\rangle = \langle f|U(+\infty, -\infty)|i\rangle = \langle f|\,T\Bigl\{\exp\Bigl[i\int d^4x\,\mathcal L_{\rm int}\bigl(\hat\phi_I(x)\bigr)\Bigr]\Bigr\}|i\rangle \qquad (\text{no derivatives in }\mathcal L_{\rm int}) .
$$
This is **exact** in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] (the source switches off; [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6c.7]]). In [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (a permanent interaction) it is valid at **lowest order**; beyond it the external particles carry $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; the LSZ formula, named in Lecture 16 and left to the second semester; QFT C10, planned). The lemmas and Theorem §C6c.3.1 are statements about free fields and free states, exact in any case. Each box states its scope.

*Conventions* ([[Larsen PHY 513]]): $\hat\phi_I^\pm$ the positive- and negative-frequency parts ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]); a contraction with an external particle is written, like a contraction between fields ([[§C6a.6 Normal Ordering and Contractions#^def-c6a-6-1|Def. §C6a.6.1]]), as the value it equals: the plane wave $e^{-ik\cdot x}$ for $\hat\phi_I(x)$ with an incoming particle $|\mathbf k\rangle$, $e^{+ip\cdot x}$ for an outgoing particle $\langle\mathbf p|$ with $\hat\phi_I(x)$, with the pair named in words or as "pair $\longmapsto$ value" (PS (4.94) and Yu (7.15), (7.18) draw the bracket of the slides over the field and the state; in these notes the bracket appears in figures only); for a complex field $|\mathbf p^+\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$ (particle), $|\mathbf p^-\rangle = \sqrt{2E_{\mathbf p}}\,\hat b^\dagger_{\mathbf p}|0\rangle$ (antiparticle), as Yu (7.133)–(7.134). The vertex integrals give momentum deltas, $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p)$ as tempered distributions ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], listed at the end).

## External states

> [!theorem] Lemma §C6c.2.1: Contraction of Fields with Outgoing Particles
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$ and $k_i^0 = E_{\mathbf k_i}$. For a normal-ordered product of $r$ free fields ([[§C6a.6 Normal Ordering and Contractions#^thm-c6a-6-1|Theorem §C6a.6.1]]),
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|0\rangle = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} :
> $$
>
> each outgoing particle contracts with exactly one field, and the contraction of $\langle\mathbf k|$ with $\hat\phi_I(y)$ is the number $[\hat a_{\mathbf k}, \hat\phi_I^-(y)] = e^{ik\cdot y}/\sqrt{2E_{\mathbf k}}$ (for $\hat a^\dagger|0\rangle$ states; $e^{ik\cdot y}$ for relativistic states, the convention from here on). Hence in $\langle\mathbf k_1\cdots\mathbf k_n|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}|0\rangle$ only the Wick terms with exactly $n$ uncontracted fields survive. For relativistically normalized states $|\mathbf k\rangle_{\rm rel} = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) the factors $\frac{1}{\sqrt{2E}}$ drop out: ${}_{\rm rel}\langle\mathbf k_1\cdots\mathbf k_n|{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_n){:}|0\rangle = \sum_\sigma\prod_ie^{ik_i\cdot y_{\sigma(i)}}$; for $n = 1$, $\langle\mathbf p|\hat\phi_I(x)|0\rangle = e^{ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]).
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free vacuum: any free fields between $\langle\mathbf k_1\cdots\mathbf k_n|$ and $|0\rangle$, independent of the dynamics; $\langle\mathbf p|\hat\phi_I(x)|0\rangle$ is the free-field result of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]; both normalizations ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations]]).
>
> *Source: PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's solution: "Only one uncontracted field survives"; "Exactly $n$ uncontracted fields survive"; the sum over $\sigma \in S_n$) and Problem 4 (relativistic form)*

^lem-c6c-2-1

> [!derivation]- Derivation
> **Step 1** (only $\hat\phi^-$ acts). Normal ordering puts every $\hat\phi_I^-$ ($\propto \hat a^\dagger$) left of every $\hat\phi_I^+$ ($\propto \hat a$), and $\hat\phi_I^+|0\rangle = 0$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]): of the $2^r$ terms of ${:}\prod(\hat\phi^+ + \hat\phi^-){:}$ only one survives on $|0\rangle$,
>
> $$
> \langle0|\hat a_{\mathbf k_n}\cdots\hat a_{\mathbf k_1}\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|0\rangle = \langle0|\hat a_{\mathbf k_n}\cdots\hat a_{\mathbf k_1}\,\hat\phi_I^-(y_1)\cdots\hat\phi_I^-(y_r)|0\rangle
> $$
>
> (the order of the $\hat a$'s is irrelevant, they commute).
>
> **Step 2** (the elementary contraction). With $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf k - \mathbf p)$,
>
> $$
> [\hat a_{\mathbf k}, \hat\phi_I^-(y)] = \int\frac{d^3p}{(2\pi)^3}\frac{e^{ip\cdot y}}{\sqrt{2E_{\mathbf p}}}(2\pi)^3\delta^3(\mathbf k - \mathbf p) = \frac{e^{ik\cdot y}}{\sqrt{2E_{\mathbf k}}}, \qquad k^0 = E_{\mathbf k},
> $$
>
> a number.
>
> **Step 3** (move one $\hat a$ through). With $X = \hat\phi_I^-(y_2)\cdots\hat\phi_I^-(y_r)$ and $\hat aB = B\hat a + [\hat a, B]$,
>
> $$
> \hat a_{\mathbf k}\,\hat\phi_I^-(y_1)X|0\rangle = \hat\phi_I^-(y_1)\,\hat a_{\mathbf k}X|0\rangle + \frac{e^{ik\cdot y_1}}{\sqrt{2E_{\mathbf k}}}\,X|0\rangle ,
> $$
>
> and repeating through $X$, $\hat a_{\mathbf k}\hat\phi_I^-(y_1)\cdots\hat\phi_I^-(y_r)|0\rangle = \sum_{l=1}^r\frac{e^{ik\cdot y_l}}{\sqrt{2E_{\mathbf k}}}\prod_{l'\ne l}\hat\phi_I^-(y_{l'})|0\rangle$ (the term with $\hat a_{\mathbf k}$ at the right end vanishes): each $\hat a$ removes one $\hat\phi^-$ in all possible ways.
>
> **Step 4** (count). Apply $\hat a_{\mathbf k_1}, \dots, \hat a_{\mathbf k_n}$ in turn. If $r < n$, an $\hat a$ meets $|0\rangle$ with no $\hat\phi^-$ left: $0$. If $r > n$, after all $\hat a$'s a $\hat\phi^- \propto \hat a^\dagger$ stands next to $\langle0|$: $0$. If $r = n$, $\hat a_{\mathbf k_1}$ picks $y_{\sigma(1)}$ ($n$ choices), $\hat a_{\mathbf k_2}$ one of the remaining ($n - 1$), …: one term per bijection $\sigma$, $n!$ terms, the stated sum. For $n = 1$: $\langle\mathbf k|\hat\phi_I^-(y)|0\rangle = e^{ik\cdot y}/\sqrt{2E_{\mathbf k}}$.
>
> **Step 5** (in Wick's theorem). $T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\} = \sum(\text{products of }D_F)\cdot{:}\text{remaining }r\text{ fields}{:}$ ([[§C6a.7 Wick's Theorem#^thm-c6a-7-2|Theorem §C6a.7.2]]), $r = \ell, \ell - 2, \dots$; by Step 4 only $r = n$ survives between $\langle\mathbf k_1\cdots\mathbf k_n|$ and $|0\rangle$. Relativistic normalization multiplies by $\prod_i\sqrt{2E_{\mathbf k_i}}$.

^der-c6c-2-1

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6a.6 Normal Ordering and Contractions#^thm-c6a-6-1|Theorem §C6a.6.1]], [[§C6a.7 Wick's Theorem#^thm-c6a-7-2|Theorem §C6a.7.2]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]

> [!caution] Caution: Two normalizations of one-particle states
> Problem Set 8 uses both. Problem 3 (PS 4.1) takes $|\mathbf k\rangle = \hat a^\dagger_{\mathbf k}|0\rangle$, with
>
> $$
> \langle\mathbf p|\mathbf k\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf k), \qquad \mathbb 1_1 = \int\frac{d^3k}{(2\pi)^3}|\mathbf k\rangle\langle\mathbf k|, \qquad \langle\mathbf k|\hat\phi_I(x)|0\rangle = \frac{e^{ik\cdot x}}{\sqrt{2E_{\mathbf k}}} ;
> $$
>
> Problem 4 and the decay and cross-section formulas take $|\mathbf k\rangle = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), with $\langle\mathbf p|\mathbf k\rangle = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$, $\mathbb 1_1 = \int\frac{d^3k}{(2\pi)^32E_{\mathbf k}}|\mathbf k\rangle\langle\mathbf k|$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], 3) and $\langle\mathbf k|\hat\phi_I(x)|0\rangle = e^{ik\cdot x}$. The amplitudes differ by $\sqrt{2E}$ per particle and the measures by $\frac{1}{2E}$ per particle; probabilities, integrated with the matching measure, agree. Mixing the two (a relativistic amplitude with $\frac{d^3k}{(2\pi)^3}$) gives a wrong factor $2E$ per particle.
>
> *Source: PHY 513, Problem Set 8, Problems 3(d) and 4 (the user's solution: "To use the decay rate of Lecture 15, the states are taken relativistically normalized") · [[Larsen PHY 513]] (register row)*

^cau-c6c-2-1

> [!theorem] Lemma §C6c.2.2: Contraction of Fields with Incoming Particles
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$, $k_i^0 = E_{\mathbf k_i}$. Then
> 1. $\hat\phi_I^+(y)\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{i=1}^n\frac{e^{-ik_i\cdot y}}{\sqrt{2E_{\mathbf k_i}}}\,|\mathbf k_1\cdots\widehat{\mathbf k_i}\cdots\mathbf k_n\rangle$ (the hat: $\mathbf k_i$ removed), and for a normal-ordered product of $r$ free fields
>
> $$
> \langle0|\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|\mathbf k_1\cdots\mathbf k_n\rangle = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{-ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} :
> $$
>
> each incoming particle contracts with exactly one field, and the contraction of $\hat\phi_I(y)$ with $|\mathbf k\rangle$ is the number $[\hat\phi_I^+(y), \hat a^\dagger_{\mathbf k}] = e^{-ik\cdot y}/\sqrt{2E_{\mathbf k}}$ (for $\hat a^\dagger|0\rangle$ states; $e^{-ik\cdot y}$ for relativistic states, part 2, the convention from here on);
> 2. with relativistic normalization the factors $\frac{1}{\sqrt{2E}}$ drop out: $\hat\phi_I^+(x)|\mathbf p\rangle = e^{-ip\cdot x}|0\rangle$ (PS (4.93)), so the contraction of $\hat\phi_I(x)$ with an incoming $|\mathbf p\rangle$ is $e^{-ip\cdot x}$ and, with [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], the contraction of an outgoing $\langle\mathbf p|$ with $\hat\phi_I(x)$ is $e^{+ip\cdot x}$ (PS (4.94)); for $n = 1$, $\langle0|\hat\phi_I(x)|\mathbf p\rangle = e^{-ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]);
> 3. for a complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]), relativistic normalization, the contractions are (the pair $\longmapsto$ the number that replaces it)
>
> $$
> \hat\phi(x),\ |\mathbf p^+\rangle \;\longmapsto\; e^{-ip\cdot x}, \qquad \hat\phi^\dagger(x),\ |\mathbf p^-\rangle \;\longmapsto\; e^{-ip\cdot x}, \qquad \langle\mathbf p^+|,\ \hat\phi^\dagger(x) \;\longmapsto\; e^{+ip\cdot x}, \qquad \langle\mathbf p^-|,\ \hat\phi(x) \;\longmapsto\; e^{+ip\cdot x} ,
> $$
>
> and $\hat\phi$ with $|\mathbf p^-\rangle$ or $\langle\mathbf p^+|$, $\hat\phi^\dagger$ with $|\mathbf p^+\rangle$ or $\langle\mathbf p^-|$ give $0$: $\hat\phi$ annihilates particles and creates antiparticles.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]; *applies:* free fields between $\langle0|$ and free $n$-particle states, exact, independent of the dynamics; both normalizations ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|Caution: Two normalizations of one-particle states]]).
>
> *Source: PS §4.6, p. 110, eqs. (4.93)–(4.94) · Yu §7.1, eqs. (7.15), (7.18); §7.4, eqs. (7.135)–(7.138); p. 281, eq. (7.87) and the boxed rule ("$n$ identical positive-frequency field operators acting on $n$ identical particles of the initial state equal the sum of the $n!$ contractions") · the incoming counterpart of [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], written here*

^lem-c6c-2-2

> [!derivation]- Derivation
> **Step 1** (the elementary contraction). With $\hat\phi_I^+(y) = \int\frac{d^3q}{(2\pi)^3}\frac{\hat a_{\mathbf q}e^{-iq\cdot y}}{\sqrt{2E_{\mathbf q}}}$ and $[\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf k}] = (2\pi)^3\delta^3(\mathbf q - \mathbf k)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]),
>
> $$
> [\hat\phi_I^+(y), \hat a^\dagger_{\mathbf k}] = \int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot y}}{\sqrt{2E_{\mathbf q}}}(2\pi)^3\delta^3(\mathbf q - \mathbf k) = \frac{e^{-ik\cdot y}}{\sqrt{2E_{\mathbf k}}}, \qquad k^0 = E_{\mathbf k} .
> $$
>
> **Step 2** (part 1, one field). Move $\hat\phi_I^+(y)$ to the right through the creators with $AB = BA + [A, B]$; $\hat\phi_I^+|0\rangle = 0$:
>
> $$
> \hat\phi_I^+(y)\,\hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle = \sum_{i=1}^n\hat a^\dagger_{\mathbf k_1}\cdots[\hat\phi_I^+(y), \hat a^\dagger_{\mathbf k_i}]\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle + \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}\hat\phi_I^+(y)|0\rangle = \sum_{i=1}^n\frac{e^{-ik_i\cdot y}}{\sqrt{2E_{\mathbf k_i}}}\prod_{j\ne i}\hat a^\dagger_{\mathbf k_j}|0\rangle .
> $$
>
> For $n = 2$: $\hat\phi_I^+(y)|\mathbf k_1\mathbf k_2\rangle = \frac{e^{-ik_1\cdot y}}{\sqrt{2E_{\mathbf k_1}}}|\mathbf k_2\rangle + \frac{e^{-ik_2\cdot y}}{\sqrt{2E_{\mathbf k_2}}}|\mathbf k_1\rangle$ (Yu (7.87)).
>
> **Step 3** (part 1, the normal-ordered product). $\hat\phi_I$ is self-adjoint and $(\hat\phi_I^\pm)^\dagger = \hat\phi_I^\mp$, so the adjoint of a normal-ordered product is the normal-ordered product of the same fields in reverse order, which is the same operator ([[§C6a.6 Normal Ordering and Contractions#^thm-c6a-6-1|Theorem §C6a.6.1]], 3):
>
> $$
> \bigl({:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\bigr)^\dagger = {:}\hat\phi_I(y_r)\cdots\hat\phi_I(y_1){:} = {:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:} .
> $$
>
> Hence, with $\langle0|A|\psi\rangle = \overline{\langle\psi|A^\dagger|0\rangle}$ and [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]],
>
> $$
> \langle0|{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}|\mathbf k_1\cdots\mathbf k_n\rangle = \overline{\langle\mathbf k_1\cdots\mathbf k_n|{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}|0\rangle} = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\overline{\Bigl(\frac{e^{ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}}\Bigr)} = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{-ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} .
> $$
>
> **Step 4** (part 2). $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$: Step 2 with $n = 1$ times $\sqrt{2E_{\mathbf p}}$ gives $\hat\phi_I^+(x)|\mathbf p\rangle = e^{-ip\cdot x}|0\rangle$; with $\langle0|\hat\phi_I^- = 0$, $\langle0|\hat\phi_I(x)|\mathbf p\rangle = \langle0|\hat\phi_I^+(x)|\mathbf p\rangle = e^{-ip\cdot x}\langle0|0\rangle = e^{-ip\cdot x}$.
>
> **Step 5** (part 3). By [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]] the positive-frequency part of $\hat\phi$ holds $\hat a$, its negative-frequency part $\hat b^\dagger$; for $\hat\phi^\dagger$, $\hat b$ and $\hat a^\dagger$. With [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], $[\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = [\hat b_{\mathbf q}, \hat b^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$ and $[\hat a_{\mathbf q}, \hat b^\dagger_{\mathbf p}] = 0$:
>
> $$
> \hat\phi^+(x)|\mathbf p^+\rangle = \sqrt{2E_{\mathbf p}}\int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E_{\mathbf q}}}[\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}]|0\rangle = e^{-ip\cdot x}|0\rangle, \qquad \hat\phi^+(x)|\mathbf p^-\rangle = \sqrt{2E_{\mathbf p}}\int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E_{\mathbf q}}}[\hat a_{\mathbf q}, \hat b^\dagger_{\mathbf p}]|0\rangle = 0 ,
> $$
>
> and with $\hat a \leftrightarrow \hat b$ the same for $\hat\phi^{\dagger+}$ on $|\mathbf p^-\rangle$ ($e^{-ip\cdot x}$) and on $|\mathbf p^+\rangle$ ($0$). The outgoing ones are the adjoints: $\langle\mathbf p^+|\hat\phi^{\dagger-}(x) = \bigl(\hat\phi^+(x)|\mathbf p^+\rangle\bigr)^\dagger = e^{+ip\cdot x}\langle0|$, $\langle\mathbf p^-|\hat\phi^-(x) = \bigl(\hat\phi^{\dagger+}(x)|\mathbf p^-\rangle\bigr)^\dagger = e^{+ip\cdot x}\langle0|$ (Yu (7.137)–(7.138)).
>
> **What the derivation shows.**
> - An incoming particle and an outgoing particle are the same contraction read in opposite directions; the plane wave carries $e^{-ip\cdot x}$ in and $e^{+ip\cdot x}$ out, so a vertex integral collects $e^{i(\sum p_{\rm out} - \sum p_{\rm in})\cdot x}$ → [[§C6c.2 Contractions with External Particles#^thm-c6c-2-5|Theorem §C6c.2.5]].
> - The $\sum_\sigma$ is the $n!$ of Yu's boxed rule: identical particles attach to identical fields in all $n!$ ways → [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]].

^der-c6c-2-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C6a.6 Normal Ordering and Contractions#^thm-c6a-6-1|Theorem §C6a.6.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]

> [!theorem] Lemma §C6c.2.3: The Overlap of Two n-Particle States
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$ and $|\mathbf p_1\cdots\mathbf p_{n'}\rangle = \hat a^\dagger_{\mathbf p_1}\cdots\hat a^\dagger_{\mathbf p_{n'}}|0\rangle$. Then
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\mathbf p_1\cdots\mathbf p_{n'}\rangle = \delta_{nn'}\sum_{\sigma\in S_n}\prod_{i=1}^n(2\pi)^3\delta^3(\mathbf k_i - \mathbf p_{\sigma(i)}) :
> $$
>
> each particle of the bra pairs with one particle of the ket, in all $n!$ ways, and states with different numbers of particles are orthogonal. For relativistically normalized states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) every pair carries $2E$:
>
> $$
> {}_{\rm rel}\langle\mathbf k_1\cdots\mathbf k_n|\mathbf p_1\cdots\mathbf p_{n'}\rangle_{\rm rel} = \delta_{nn'}\sum_{\sigma\in S_n}\prod_{i=1}^n2E_{\mathbf k_i}(2\pi)^3\delta^3(\mathbf k_i - \mathbf p_{\sigma(i)}) ;
> $$
>
> for $n = 1$ these are the two overlaps $\langle\mathbf p|\mathbf k\rangle$ of [[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|Caution: Two normalizations of one-particle states]].
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* the free Fock space, any $n$-particle states, independent of the dynamics; both normalizations.
>
> *Source: PHY 513, Problem Set 8, Problem 3(e) (the user's solution, paragraph "Measure": "By the same commuting argument as above, with $\hat a^\dagger_{\mathbf p}$ in place of $\hat\phi_I^-$"; the statement and Step 1 below stood in [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]] until 2026-11-12) · PS §4.6, p. 109, eq. (4.91) ($n = 2$, relativistic states) · the case $n \ne n'$ and the relativistic form: from Step 5 of [[§C6c.3 Wick's Theorem between Particle States#^der-c6c-3-1|Derivation §C6c.3.1]], moved here*

^lem-c6c-2-3

> [!derivation]- Derivation
> **Step 1** (overlap). $\langle\mathbf k_1\cdots\mathbf k_n|\mathbf p_1\cdots\mathbf p_n\rangle = \langle0|\hat a_{\mathbf k_1}\cdots\hat a_{\mathbf k_n}\hat a^\dagger_{\mathbf p_1}\cdots\hat a^\dagger_{\mathbf p_n}|0\rangle$ is Step 4 of [[§C6c.2 Contractions with External Particles#^der-c6c-2-1|Derivation §C6c.2.1]] with $\hat a^\dagger_{\mathbf p}$ for $\hat\phi^-$ and $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf k - \mathbf p)$: the stated sum.
>
> **Step 2** (different numbers of particles). Move each $\hat a_{\mathbf k}$ to the right with $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf k - \mathbf p)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]): each commutator removes one $\hat a^\dagger_{\mathbf p}$ in all possible ways, and an $\hat a$ that reaches $|0\rangle$ (or an $\hat a^\dagger$ left next to $\langle0|$) gives $0$, exactly as in Steps 3–4 of [[§C6c.2 Contractions with External Particles#^der-c6c-2-1|Derivation §C6c.2.1]] with $\hat a^\dagger_{\mathbf p}$ in place of $\hat\phi^-$. So the overlap vanishes unless $n = n'$.
>
> **Step 3** (relativistic normalization). The two states carry the factors $\prod_i\sqrt{2E_{\mathbf k_i}}\prod_j\sqrt{2E_{\mathbf p_j}}$. On the support of the delta the two square roots combine to $2E_{\mathbf k}$: in the term of $\sigma$, $\mathbf p_{\sigma(i)} = \mathbf k_i$ for every $i$, so $\prod_j\sqrt{2E_{\mathbf p_j}} = \prod_i\sqrt{2E_{\mathbf k_i}}$ and the factor is $\prod_i2E_{\mathbf k_i}$.
>
> **What the derivation shows.**
> - The overlap is the fourth kind of pair in Wick's theorem between particle states, a particle of the bra with a particle of the ket and no field → [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]; drawn, it is the $\delta$-line ([[§C6c.3 Wick's Theorem between Particle States#^def-c6c-3-1|Def. §C6c.3.1]]).
> - The sum over $\sigma$ expresses the symmetry of the states; because of it, integrating each momentum independently counts each state $n!$ times → [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]].

^der-c6c-2-3

*Uses:* [[§C6c.2 Contractions with External Particles#^der-c6c-2-1|Derivation §C6c.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]

## Identical particles and the direction of a contraction

> [!theorem] Theorem §C6c.2.4: n Identical Fields on n Identical Particles Give the n! Contractions
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle$ be a relativistically normalized state of $n$ particles of one real free field ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), $k_i^0 = E_{\mathbf k_i}$, and $\hat\phi_I^\pm$ the positive- and negative-frequency parts ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]). Then
>
> $$
> \hat\phi_I^+(y_1)\cdots\hat\phi_I^+(y_n)\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{\sigma\in S_n}\prod_{i=1}^ne^{-ik_i\cdot y_{\sigma(i)}}\;|0\rangle , \qquad \langle\mathbf k_1\cdots\mathbf k_n|\,\hat\phi_I^-(y_1)\cdots\hat\phi_I^-(y_n) = \sum_{\sigma\in S_n}\prod_{i=1}^ne^{+ik_i\cdot y_{\sigma(i)}}\;\langle0| :
> $$
>
> $n$ identical positive- (negative-) frequency fields acting on $n$ identical incoming (outgoing) particles give the sum of the $n!$ contractions, one for each way of attaching the particles to the fields (the single contractions of [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]] and [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2). If the $n$ fields sit at one point, $y_1 = \cdots = y_n = x$, the $n!$ terms are equal and the sum is $n!\prod_ie^{\mp ik_i\cdot x}$.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free states, exact, independent of the dynamics; with $|\mathbf k\rangle = \hat a^\dagger_{\mathbf k}|0\rangle$ each term carries $\prod_i(2E_{\mathbf k_i})^{-1/2}$ ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]).
>
> *Source: Yu §7.1.2, p. 281, eqs. (7.86)–(7.87) and the boxed rule ("$n$ identical positive- (negative-) energy field operators acting on $n$ corresponding identical particles of the initial (final) state equal the sum of the $n!$ contractions of these field operators with the initial- (final-) state particles") · PS §4.6, eq. (4.98) · PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's solution: the sum over $\sigma \in S_n$) · stated here from Step 4 of [[§C6c.2 Contractions with External Particles#^der-c6c-2-1|Derivation §C6c.2.1]] and the "What the derivation shows" of [[§C6c.2 Contractions with External Particles#^der-c6c-2-2|Derivation §C6c.2.2]]*

^thm-c6c-2-4

> [!derivation]- Derivation
> **Step 1** (one field). [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 1, with $|\mathbf k_1\cdots\mathbf k_n\rangle_{\rm rel} = \prod_i\sqrt{2E_{\mathbf k_i}}\;\hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$: the factor $\frac{1}{\sqrt{2E_{\mathbf k_i}}}$ of the removed particle cancels its $\sqrt{2E_{\mathbf k_i}}$, and the other factors stay with the remaining state,
>
> $$
> \hat\phi_I^+(y)\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{i=1}^ne^{-ik_i\cdot y}\,|\mathbf k_1\cdots\widehat{\mathbf k_i}\cdots\mathbf k_n\rangle ,
> $$
>
> the hat marking the removed momentum; the state on the right is the relativistically normalized $(n - 1)$-particle state.
>
> **Step 2** ($n$ fields). The $\hat\phi_I^+$ contain only annihilators and commute, $[\hat\phi_I^+(y), \hat\phi_I^+(y')] = 0$, so they may act in any order; let $\hat\phi_I^+(y_n)$ act first. By Step 1 it removes a particle $i_n$ ($n$ choices), then $\hat\phi_I^+(y_{n-1})$ removes $i_{n-1}$ from the remaining $n - 1$, …, and $\hat\phi_I^+(y_1)$ removes the last one, leaving $|0\rangle$. A sequence of choices $(i_n, \dots, i_1)$ is a bijection $\sigma$ with $\sigma(i_l) = l$, there are $n(n - 1)\cdots1 = n!$ of them, and the term of $\sigma$ is the product of the removal factors, $\prod_ie^{-ik_i\cdot y_{\sigma(i)}}|0\rangle$.
>
> **Step 3** ($n = 2$, Yu (7.87)). Step 1 twice:
>
> $$
> \hat\phi_I^+(x)\hat\phi_I^+(y)|\mathbf k_1\mathbf k_2\rangle = \hat\phi_I^+(x)\bigl(e^{-ik_1\cdot y}|\mathbf k_2\rangle + e^{-ik_2\cdot y}|\mathbf k_1\rangle\bigr) = \bigl(e^{-ik_2\cdot x - ik_1\cdot y} + e^{-ik_1\cdot x - ik_2\cdot y}\bigr)|0\rangle ,
> $$
>
> the two contractions, symmetric under $\mathbf k_1 \leftrightarrow \mathbf k_2$.
>
> **Step 4** (outgoing particles). Take the adjoint of Step 2: $(\hat\phi_I^+(y))^\dagger = \hat\phi_I^-(y)$ ($\hat\phi_I$ is self-adjoint), the adjoint reverses the order of the $\hat\phi^-$, which commute, and $\overline{e^{-ik\cdot y}} = e^{+ik\cdot y}$ for real $k$, $y$:
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\hat\phi_I^-(y_n)\cdots\hat\phi_I^-(y_1) = \Bigl(\hat\phi_I^+(y_1)\cdots\hat\phi_I^+(y_n)|\mathbf k_1\cdots\mathbf k_n\rangle\Bigr)^\dagger = \sum_{\sigma\in S_n}\prod_{i=1}^ne^{+ik_i\cdot y_{\sigma(i)}}\,\langle0| .
> $$
>
> **Step 5** (one point). For $y_1 = \cdots = y_n = x$ every term of Step 2 equals $\prod_ie^{-ik_i\cdot x}$, so the sum is $n!\prod_ie^{-ik_i\cdot x}$; Step 4 likewise with $e^{+ik_i\cdot x}$.
>
> **What the derivation shows.**
> - The $n!$ belongs to the identical fields; at a vertex it cancels the $\frac{1}{4!}$ of $\phi^4$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-4|Theorem §C6c.4.4]]); when legs close on each other fewer assignments are distinct and the symmetry factor is left over ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-5|Theorem §C6c.4.5]]).
> - Several kinds of particles: one such sum per kind, since a particle attaches only to a field of its kind ([[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]; the count per kind is Step 3 of [[§C6c.4 First Order꞉ Enumerate, then Filter#^der-c6c-4-1|Derivation §C6c.4.1]]).

^der-c6c-2-4

*Uses:* [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]

> [!theorem] Theorem §C6c.2.5: In and Out Are One Contraction Read Both Ways; a Vertex Collects the Momenta
> Let all states be relativistically normalized free states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]).
> 1. The contraction with an outgoing particle is the complex conjugate of the contraction with the incoming particle of the same momentum ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2):
>
> $$
> \hat\phi_I(x),\ |\mathbf p\rangle \;\longmapsto\; e^{-ip\cdot x}, \qquad \langle\mathbf p|,\ \hat\phi_I(x) \;\longmapsto\; e^{+ip\cdot x} = \overline{e^{-ip\cdot x}} = e^{-i(-p)\cdot x} :
> $$
>
> an outgoing particle of momentum $p$ enters a vertex as an incoming one of momentum $-p$.
> 2. If incoming particles $k_1, \dots, k_a$ and outgoing particles $p_1, \dots, p_b$ are contracted with fields at one vertex $x$, their wave functions multiply to $e^{i(\sum_jp_j - \sum_ik_i)\cdot x}$; for a vertex holding only particles the vertex integral is
>
> $$
> \int d^4x\;e^{i(\sum_jp_j - \sum_ik_i)\cdot x} = (2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr) ,
> $$
>
> and an internal line ending at $x$ adds its momentum to the balance ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-5|Theorem §C6a.14.5]], 1): four-momentum is conserved at every vertex.
> 3. For a complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]) particle and antiparticle carry the same phases, $e^{-ip\cdot x}$ in and $e^{+ip\cdot x}$ out; they differ only in which of $\hat\phi$, $\hat\phi^\dagger$ they contract with ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3).
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]; *applies:* free fields and free relativistic states, exact, independent of the dynamics; the vertex integral as an identity of tempered distributions ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]).
>
> *Source: Yu §7.1, eqs. (7.15), (7.18) (the contractions of $\phi$ with initial and final particles); §7.4, eqs. (7.135)–(7.138) · PS §4.6, p. 110, eqs. (4.93)–(4.94) · PHY 513 Lecture 16, slide 15 · stated here from the "What the derivation shows" of [[§C6c.2 Contractions with External Particles#^der-c6c-2-2|Derivation §C6c.2.2]]*

^thm-c6c-2-5

> [!derivation]- Derivation
> **Step 1** (part 1). [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2: $\hat\phi_I^+(x)|\mathbf p\rangle = e^{-ip\cdot x}|0\rangle$; its adjoint, with $(\hat\phi_I^+)^\dagger = \hat\phi_I^-$, is $\langle\mathbf p|\hat\phi_I^-(x) = \overline{e^{-ip\cdot x}}\,\langle0| = e^{+ip\cdot x}\langle0|$, since $p\cdot x$ is real. Writing $e^{+ip\cdot x} = e^{-i(-p)\cdot x}$ shows it as the incoming wave function of momentum $-p$.
>
> **Step 2** (part 2, the product). The exponents add:
>
> $$
> \prod_{i=1}^ae^{-ik_i\cdot x}\prod_{j=1}^be^{+ip_j\cdot x} = \exp\Bigl[i\Bigl(\sum_jp_j - \sum_ik_i\Bigr)\cdot x\Bigr] .
> $$
>
> **Step 3** (part 2, the vertex integral). With $q = \sum_jp_j - \sum_ik_i$, [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] gives $\int d^4x\,e^{iq\cdot x} = (2\pi)^4\delta^4(q)$, and $\delta^4(q) = \delta^4(-q)$ (the delta is even) gives the stated form.
>
> **Step 4** (part 2, internal lines). An internal line from $x$ to $y$ is $D_F(x - y) = \int\frac{d^4\ell}{(2\pi)^4}\tilde D_F(\ell)\,e^{-i\ell\cdot(x - y)}$ ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]]): at $x$ it contributes $e^{-i\ell\cdot x}$, the same form as an incoming particle of momentum $\ell$ (and $e^{+i\ell\cdot y}$ at $y$, outgoing). The integral over $x$ becomes $(2\pi)^4\delta^4(\sum_ik_i + \sum_{\rm lines\ in}\ell - \sum_jp_j - \sum_{\rm lines\ out}\ell)$ ([[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-5|Theorem §C6a.14.5]], 1).
>
> **Step 5** (part 3). [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3: $\hat\phi(x)$ with $|\mathbf p^+\rangle$ and $\hat\phi^\dagger(x)$ with $|\mathbf p^-\rangle$ contract to $e^{-ip\cdot x}$, $\langle\mathbf p^+|$ with $\hat\phi^\dagger(x)$ and $\langle\mathbf p^-|$ with $\hat\phi(x)$ to $e^{+ip\cdot x}$; the other four combinations vanish.
>
> **What the derivation shows.**
> - The sign of the exponent distinguishes in from out; counting every momentum as flowing into the vertex is what reconciles the slide's "$e^{-ipx}$ for every external line" with the outgoing $e^{+ip\cdot x}$ ([[§C6c.6 Feynman Rules for Amplitudes#^cau-c6c-6-1|§C6c.6, Caution: The sign of the external wave function]]).

^der-c6c-2-5

*Uses:* [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-10|Theorem §C2b.7.10]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^thm-c6a-14-5|Theorem §C6a.14.5]]

> [!remark] Remark: Yu's route
> Yu computes $S$-matrix elements this way before any correlation function: he defines the contractions of each field with initial and final particles (eqs. (7.13)–(7.18)), lists all first-order $T$-matrix elements of Yukawa theory and filters them kinematically (p. 272), reads the position- and then momentum-space rules off the results (eqs. (7.25)–(7.28), §7.2; this chapter follows the same order, [[§C6c.2 Contractions with External Particles|§C6c.2]]–[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]]), and justifies them only in ch. 10 through LSZ ("our method for leading-order processes in chapters 7, 8, 9 is justified", p. 474). He keeps the field operators in the order of $\mathcal L_{\rm int}$ to fix fermion signs (boxed rule, p. 268; in the vault's form, crossing contractions: [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|§C6d.3, Theorem §C6d.3.4]]); for scalars there are no signs. Yukawa theory with these rules: [[· C6d Feynman Rules for Fermions|C6d]]. The course stated the amputation rule from correlation functions at the end of Lecture 15 ([[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]]) and then took Yu's direct route in Lecture 16, for $2 \to 2$ in $\phi^4$; the two routes agree at lowest order ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]).
>
> *Source: Yu §7.1, pp. 262–272; §7.2, pp. 287–288; §10.5.2, p. 474*

^rem-c6c-2-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the vertex integrals give momentum deltas.

> [!remark]- Connections
> - The contraction of a field with an external particle is the one-particle wave function $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$; with interactions it carries $\sqrt Z$, the origin of the LSZ factor — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]].
> - The fermion counterparts: four external wave functions $u$, $\bar u$, $v$, $\bar v$ instead of one plane wave — [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|§C6d.2, Theorem §C6d.2.1]].
> - The $n!$ of identical particles appears twice: as the sum over $\sigma$ when particles attach to fields or to each other ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-3|Lemma §C6c.2.3]]), and as the $\frac{1}{n!}$ of the $n$-particle measure ($S_{\rm id}$) — [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]].
> - The fermion counterparts of the lemmas and theorems here: several fields on one state contract from the inside out, $n$ identical fermions give the $n!$ contractions with the signs of the permutations, and a vertex also joins spinor indices — [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-3|Theorem §C6d.2.3]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]].
