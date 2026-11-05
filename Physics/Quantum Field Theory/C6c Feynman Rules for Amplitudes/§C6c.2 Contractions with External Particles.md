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

**Setup and scope.** The in and out states are free Fock states over the free vacuum $|0\rangle$, relativistically normalized ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), $|i\rangle = |\mathbf k_1\cdots\mathbf k_n\rangle$, $\langle f| = \langle\mathbf p_1\cdots\mathbf p_m|$. Between them the interaction-picture evolution operator acts ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]):
$$
\langle f|\hat S|i\rangle = \langle f|U(+\infty, -\infty)|i\rangle = \langle f|\,T\Bigl\{\exp\Bigl[i\int d^4x\,\mathcal L_{\rm int}\bigl(\hat\phi_I(x)\bigr)\Bigr]\Bigr\}|i\rangle \qquad (\text{no derivatives in }\mathcal L_{\rm int}) .
$$
This is **exact** in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] (the source switches off; [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6c.7]]). In [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (a permanent interaction) it is valid at **lowest order**; beyond it the external particles carry $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; the LSZ formula, Lecture 16). The lemmas and Theorem §C6c.3.1 are statements about free fields and free states, exact in any case. Each box states its scope.

*Conventions* ([[Larsen PHY 513]]): $\hat\phi_I^\pm$ the positive- and negative-frequency parts ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]); a contraction with an external particle is written with the same bracket as between fields, $\overbracket{\hat\phi_I(x)|\mathbf k\rangle}$, $\overbracket{\langle\mathbf p|\hat\phi_I(x)}$ (PS (4.94); Yu (7.15), (7.18)); for a complex field $|\mathbf p^+\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$ (particle), $|\mathbf p^-\rangle = \sqrt{2E_{\mathbf p}}\,\hat b^\dagger_{\mathbf p}|0\rangle$ (antiparticle), as Yu (7.133)–(7.134). The vertex integrals give momentum deltas, $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p)$ as tempered distributions ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], listed at the end).

## External states

> [!theorem] Lemma §C6c.2.1: Contraction of Fields with Outgoing Particles
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$ and $k_i^0 = E_{\mathbf k_i}$. For a normal-ordered product of $r$ free fields ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]]),
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|0\rangle = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} :
> $$
>
> each outgoing particle contracts with exactly one field, $\overbracket{\langle\mathbf k|\,\hat\phi_I(y)} \equiv [\hat a_{\mathbf k}, \hat\phi_I^-(y)] = e^{ik\cdot y}/\sqrt{2E_{\mathbf k}}$. Hence in $\langle\mathbf k_1\cdots\mathbf k_n|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}|0\rangle$ only the Wick terms with exactly $n$ uncontracted fields survive. For relativistically normalized states $|\mathbf k\rangle_{\rm rel} = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) the factors $\frac{1}{\sqrt{2E}}$ drop out: ${}_{\rm rel}\langle\mathbf k_1\cdots\mathbf k_n|{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_n){:}|0\rangle = \sum_\sigma\prod_ie^{ik_i\cdot y_{\sigma(i)}}$; for $n = 1$, $\langle\mathbf p|\hat\phi_I(x)|0\rangle = e^{ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]).
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free vacuum: any free fields between $\langle\mathbf k_1\cdots\mathbf k_n|$ and $|0\rangle$, independent of the dynamics; $\langle\mathbf p|\hat\phi_I(x)|0\rangle$ is the free-field result of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]; both normalizations ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations]]).
>
> *Source: PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's solution: "Only one uncontracted field survives"; "Exactly $n$ uncontracted fields survive"; the sum over $\sigma \in S_n$) and Problem 4 (relativistic form) · stated in general there and moved here (2026-11-02)*

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
> **Step 5** (in Wick's theorem). $T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\} = \sum(\text{products of }D_F)\cdot{:}\text{remaining }r\text{ fields}{:}$ ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]), $r = \ell, \ell - 2, \dots$; by Step 4 only $r = n$ survives between $\langle\mathbf k_1\cdots\mathbf k_n|$ and $|0\rangle$. Relativistic normalization multiplies by $\prod_i\sqrt{2E_{\mathbf k_i}}$.

^der-c6c-2-1

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]

> [!caution] Caution: Two normalizations of one-particle states
> Problem Set 8 uses both. Problem 3 (PS 4.1) takes $|\mathbf k\rangle = \hat a^\dagger_{\mathbf k}|0\rangle$, with
>
> $$
> \langle\mathbf p|\mathbf k\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf k), \qquad \mathbb 1_1 = \int\frac{d^3k}{(2\pi)^3}|\mathbf k\rangle\langle\mathbf k|, \qquad \langle\mathbf k|\hat\phi_I(x)|0\rangle = \frac{e^{ik\cdot x}}{\sqrt{2E_{\mathbf k}}} ;
> $$
>
> Problem 4 and the decay and cross-section formulas take $|\mathbf k\rangle = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), with $\langle\mathbf p|\mathbf k\rangle = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$, $\mathbb 1_1 = \int\frac{d^3k}{(2\pi)^32E_{\mathbf k}}|\mathbf k\rangle\langle\mathbf k|$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) and $\langle\mathbf k|\hat\phi_I(x)|0\rangle = e^{ik\cdot x}$. The amplitudes differ by $\sqrt{2E}$ per particle and the measures by $\frac{1}{2E}$ per particle; probabilities, integrated with the matching measure, agree. Mixing the two (a relativistic amplitude with $\frac{d^3k}{(2\pi)^3}$) gives a wrong factor $2E$ per particle.
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
> each incoming particle contracts with exactly one field, $\overbracket{\hat\phi_I(y)|\mathbf k\rangle} \equiv [\hat\phi_I^+(y), \hat a^\dagger_{\mathbf k}] = e^{-ik\cdot y}/\sqrt{2E_{\mathbf k}}$;
> 2. with relativistic normalization the factors $\frac{1}{\sqrt{2E}}$ drop out: $\hat\phi_I^+(x)|\mathbf p\rangle = e^{-ip\cdot x}|0\rangle$ (PS (4.93)), so $\overbracket{\hat\phi_I(x)|\mathbf p\rangle} = e^{-ip\cdot x}$ and, with [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], $\overbracket{\langle\mathbf p|\hat\phi_I(x)} = e^{+ip\cdot x}$ (PS (4.94)); for $n = 1$, $\langle0|\hat\phi_I(x)|\mathbf p\rangle = e^{-ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]);
> 3. for a complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]), relativistic normalization,
>
> $$
> \overbracket{\hat\phi(x)|\mathbf p^+\rangle} = \overbracket{\hat\phi^\dagger(x)|\mathbf p^-\rangle} = e^{-ip\cdot x}, \qquad \overbracket{\langle\mathbf p^+|\hat\phi^\dagger(x)} = \overbracket{\langle\mathbf p^-|\hat\phi(x)} = e^{+ip\cdot x} ,
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
> **Step 3** (part 1, the normal-ordered product). $\hat\phi_I$ is self-adjoint and $(\hat\phi_I^\pm)^\dagger = \hat\phi_I^\mp$, so the adjoint of a normal-ordered product is the normal-ordered product of the same fields in reverse order, which is the same operator ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 3):
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
> - An incoming particle and an outgoing particle are the same contraction read in opposite directions; the plane wave carries $e^{-ip\cdot x}$ in and $e^{+ip\cdot x}$ out, so a vertex integral collects $e^{i(\sum p_{\rm out} - \sum p_{\rm in})\cdot x}$.
> - The $\sum_\sigma$ is the $n!$ of Yu's boxed rule: identical particles attach to identical fields in all $n!$ ways.

^der-c6c-2-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]

## Identical particles and the direction of a contraction

<!-- NEW thm-c6c-2-3 -->

<!-- NEW thm-c6c-2-4 -->

> [!remark] Remark: Yu's route
> Yu computes $S$-matrix elements this way before any correlation function: he defines the contractions of each field with initial and final particles (eqs. (7.13)–(7.18)), lists all first-order $T$-matrix elements of Yukawa theory and filters them kinematically (p. 272), reads the position- and then momentum-space rules off the results (eqs. (7.25)–(7.28), §7.2), and justifies them only in ch. 10 through LSZ ("our method for leading-order processes in chapters 7, 8, 9 is justified", p. 474). He keeps the field operators in the order of $\mathcal L_{\rm int}$ to fix fermion signs (boxed rule, p. 268; in the vault's form, crossing contractions: [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|§C6d.3, Theorem §C6d.3.4]]); for scalars there are no signs. Yukawa theory with these rules: [[· C6d Feynman Rules for Fermions|C6d]]. The course reaches amplitudes from correlation functions ([[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]]); the two routes agree at lowest order ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-1|Example §C6c.4.1]]).
>
> *Source: Yu §7.1, pp. 262–272; §7.2, pp. 287–288; §10.5.2, p. 474*

^rem-c6c-2-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give momentum deltas.

> [!remark]- Connections
> - The contraction of a field with an external particle is the one-particle wave function $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$; with interactions it carries $\sqrt Z$, the origin of the LSZ factor — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]].
> - The $n!$ of identical particles appears twice: as the sum over $\sigma$ when particles attach to fields, and as the $\frac{1}{n!}$ of the $n$-particle measure ($S_{\rm id}$) — [[§C6c.7 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6c-7-5|Theorem §C6c.7.5]], [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]].
