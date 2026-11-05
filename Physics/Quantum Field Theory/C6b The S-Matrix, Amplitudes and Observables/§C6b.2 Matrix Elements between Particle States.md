---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.1 The S-Matrix and the Invariant Amplitude]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.3 Feynman Rules for Amplitudes]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.6, pp. 109–113, eqs. (4.89)–(4.98), (4.101)–(4.102) (contractions with external states (4.93)–(4.94); $\phi\phi \to \phi\phi$ (4.98)) · PHY 513 Lecture 16 (Larsen, 2 Nov 2026), Part B, slides 10–18, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.3–§16.4 · Yu Zhao-Huan, 量子场论讲义, §7.1, pp. 262–272, eqs. (7.13)–(7.24) (contractions of fields with initial and final particles; the first-order $T$-matrix elements of Yukawa theory, Fig. 7.1–7.2, and the kinematic filter, p. 272), p. 268 (boxed contraction rule), p. 281 (boxed $n!$ rule), eqs. (7.86)–(7.87); §7.3, eqs. (7.112)–(7.121); §7.4, eqs. (7.133)–(7.142) · PHY 513, Problem Set 8, Problems 2, 3(d)–(e) and 4 (the user's solutions, submitted 2026-10-30) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), transcript ("strip off the external lines").*

[[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]] defined the matrix elements $\langle f|i\hat T|i\rangle$ and the amplitude $\mathcal M$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]). This section computes them from the Dyson series with particles, not the vacuum, on both sides. The new step is a contraction of a field with an external particle: a field annihilates an incoming particle or creates an outgoing one, and each such contraction is a plane wave ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]]). With it Wick's theorem holds between particle states ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]]), and its terms sort into the $\mathbb 1$ (particles passing through on $\delta$-lines, [[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]]), vacuum bubbles, corrections of the external states, and the scattering ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]]; Lecture 16, Part B). At first order this gives Yu's procedure: list every matrix element the interaction allows, then keep those that energy-momentum conservation allows ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]]). At higher order it gives the Feynman rules for $i\mathcal M$, the subject of [[§C6b.3 Feynman Rules for Amplitudes|§C6b.3]] ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-2|Theorem §C6b.3.2]], [[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]]). Problem Set 8 had to build these tools by hand (Problems 3 and 4). [[§C6b.10 Amplitudes from Correlation Functions|§C6b.10]] reaches the same rules from the correlation functions of C6a by amputation, the route that generalizes beyond lowest order (LSZ). Yu computes $S$-matrix elements this way from the start (§7.1–§7.4); PS do it in §4.6 (eqs. (4.89)–(4.98)); Lecture 16, Part B, does it for $2 \to 2$ in $\phi^4$.

**Setup and scope.** The in and out states are free Fock states over the free vacuum $|0\rangle$, relativistically normalized ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), $|i\rangle = |\mathbf k_1\cdots\mathbf k_n\rangle$, $\langle f| = \langle\mathbf p_1\cdots\mathbf p_m|$. Between them the interaction-picture evolution operator acts ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]):
$$
\langle f|\hat S|i\rangle = \langle f|U(+\infty, -\infty)|i\rangle = \langle f|\,T\Bigl\{\exp\Bigl[i\int d^4x\,\mathcal L_{\rm int}\bigl(\hat\phi_I(x)\bigr)\Bigr]\Bigr\}|i\rangle \qquad (\text{no derivatives in }\mathcal L_{\rm int}) .
$$
This is **exact** in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] (the source switches off; [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.11]]). In [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] (a permanent interaction) it is valid at **lowest order**; beyond it the external particles carry $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]; the LSZ formula, Lecture 16). The lemmas and Theorem §C6b.2.3 are statements about free fields and free states, exact in any case. Each box states its scope.

*Conventions* ([[Larsen PHY 513]]): $\hat\phi_I^\pm$ the positive- and negative-frequency parts ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]); a contraction with an external particle is written with the same bracket as between fields, $\overbracket{\hat\phi_I(x)|\mathbf k\rangle}$, $\overbracket{\langle\mathbf p|\hat\phi_I(x)}$ (PS (4.94); Yu (7.15), (7.18)); for a complex field $|\mathbf p^+\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$ (particle), $|\mathbf p^-\rangle = \sqrt{2E_{\mathbf p}}\,\hat b^\dagger_{\mathbf p}|0\rangle$ (antiparticle), as Yu (7.133)–(7.134). The vertex integrals give momentum deltas, $\int d^4x\,e^{ip\cdot x} = (2\pi)^4\delta^4(p)$ as tempered distributions ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], listed at the end).

## External states

> [!theorem] Lemma §C6b.2.1: Contraction of Fields with Outgoing Particles
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$ and $k_i^0 = E_{\mathbf k_i}$. For a normal-ordered product of $r$ free fields ([[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]]),
>
> $$
> \langle\mathbf k_1\cdots\mathbf k_n|\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|0\rangle = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} :
> $$
>
> each outgoing particle contracts with exactly one field, $\overbracket{\langle\mathbf k|\,\hat\phi_I(y)} \equiv [\hat a_{\mathbf k}, \hat\phi_I^-(y)] = e^{ik\cdot y}/\sqrt{2E_{\mathbf k}}$. Hence in $\langle\mathbf k_1\cdots\mathbf k_n|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}|0\rangle$ only the Wick terms with exactly $n$ uncontracted fields survive. For relativistically normalized states $|\mathbf k\rangle_{\rm rel} = \sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf k}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) the factors $\frac{1}{\sqrt{2E}}$ drop out: ${}_{\rm rel}\langle\mathbf k_1\cdots\mathbf k_n|{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_n){:}|0\rangle = \sum_\sigma\prod_ie^{ik_i\cdot y_{\sigma(i)}}$; for $n = 1$, $\langle\mathbf p|\hat\phi_I(x)|0\rangle = e^{ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]).
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free vacuum: any free fields between $\langle\mathbf k_1\cdots\mathbf k_n|$ and $|0\rangle$, independent of the dynamics; $\langle\mathbf p|\hat\phi_I(x)|0\rangle$ is the free-field result of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]; both normalizations ([[§C6b.2 Matrix Elements between Particle States#^cau-c6b-2-1|§C6b.2, Caution: Two normalizations]]).
>
> *Source: PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's solution: "Only one uncontracted field survives"; "Exactly $n$ uncontracted fields survive"; the sum over $\sigma \in S_n$) and Problem 4 (relativistic form) · stated in general there and moved here (2026-11-02)*

^lem-c6b-2-1

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

^der-c6b-2-1

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

^cau-c6b-2-1

> [!theorem] Lemma §C6b.2.2: Contraction of Fields with Incoming Particles
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle = \hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$, $k_i^0 = E_{\mathbf k_i}$. Then
> 1. $\hat\phi_I^+(y)\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{i=1}^n\frac{e^{-ik_i\cdot y}}{\sqrt{2E_{\mathbf k_i}}}\,|\mathbf k_1\cdots\widehat{\mathbf k_i}\cdots\mathbf k_n\rangle$ (the hat: $\mathbf k_i$ removed), and for a normal-ordered product of $r$ free fields
>
> $$
> \langle0|\,{:}\hat\phi_I(y_1)\cdots\hat\phi_I(y_r){:}\,|\mathbf k_1\cdots\mathbf k_n\rangle = \delta_{rn}\sum_{\sigma\in S_n}\prod_{i=1}^n\frac{e^{-ik_i\cdot y_{\sigma(i)}}}{\sqrt{2E_{\mathbf k_i}}} :
> $$
>
> each incoming particle contracts with exactly one field, $\overbracket{\hat\phi_I(y)|\mathbf k\rangle} \equiv [\hat\phi_I^+(y), \hat a^\dagger_{\mathbf k}] = e^{-ik\cdot y}/\sqrt{2E_{\mathbf k}}$;
> 2. with relativistic normalization the factors $\frac{1}{\sqrt{2E}}$ drop out: $\hat\phi_I^+(x)|\mathbf p\rangle = e^{-ip\cdot x}|0\rangle$ (PS (4.93)), so $\overbracket{\hat\phi_I(x)|\mathbf p\rangle} = e^{-ip\cdot x}$ and, with [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], $\overbracket{\langle\mathbf p|\hat\phi_I(x)} = e^{+ip\cdot x}$ (PS (4.94)); for $n = 1$, $\langle0|\hat\phi_I(x)|\mathbf p\rangle = e^{-ip\cdot x}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]);
> 3. for a complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]), relativistic normalization,
>
> $$
> \overbracket{\hat\phi(x)|\mathbf p^+\rangle} = \overbracket{\hat\phi^\dagger(x)|\mathbf p^-\rangle} = e^{-ip\cdot x}, \qquad \overbracket{\langle\mathbf p^+|\hat\phi^\dagger(x)} = \overbracket{\langle\mathbf p^-|\hat\phi(x)} = e^{+ip\cdot x} ,
> $$
>
> and $\hat\phi$ with $|\mathbf p^-\rangle$ or $\langle\mathbf p^+|$, $\hat\phi^\dagger$ with $|\mathbf p^+\rangle$ or $\langle\mathbf p^-|$ give $0$: $\hat\phi$ annihilates particles and creates antiparticles.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]; *applies:* free fields between $\langle0|$ and free $n$-particle states, exact, independent of the dynamics; both normalizations ([[§C6b.2 Matrix Elements between Particle States#^cau-c6b-2-1|Caution: Two normalizations of one-particle states]]).
>
> *Source: PS §4.6, p. 110, eqs. (4.93)–(4.94) · Yu §7.1, eqs. (7.15), (7.18); §7.4, eqs. (7.135)–(7.138); p. 281, eq. (7.87) and the boxed rule ("$n$ identical positive-frequency field operators acting on $n$ identical particles of the initial state equal the sum of the $n!$ contractions") · the incoming counterpart of [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], written here*

^lem-c6b-2-2

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
> Hence, with $\langle0|A|\psi\rangle = \overline{\langle\psi|A^\dagger|0\rangle}$ and [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]],
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

^der-c6b-2-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]

## Wick's theorem between particle states

> [!theorem] Theorem §C6b.2.3: Wick's Theorem between Particle States
> Let $|\mathbf k_1\cdots\mathbf k_n\rangle$ and $\langle\mathbf p_1\cdots\mathbf p_m|$ be relativistically normalized free states of one real field. Then
>
> $$
> \langle\mathbf p_1\cdots\mathbf p_m|\,T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_\ell)\}\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{\text{full contractions}}\;\prod_{\text{pairs}}(\text{value}) ,
> $$
>
> the sum over all ways of splitting the $\ell$ fields and the $n + m$ particles into pairs of the four types
>
> $$
> \overbracket{\hat\phi_I(x_a)\hat\phi_I(x_b)} = D_F(x_a - x_b), \quad \overbracket{\hat\phi_I(x)|\mathbf k\rangle} = e^{-ik\cdot x}, \quad \overbracket{\langle\mathbf p|\hat\phi_I(x)} = e^{+ip\cdot x}, \quad \overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k) ,
> $$
>
> with no pair of two incoming or two outgoing particles. Equivalently: in Wick's theorem $T\{\cdots\} = \sum_C\prod D_F\;{:}\text{rest}{:}$ ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]), a normal-ordered remainder contributes only through the terms in which **every** one of its fields is contracted with an external particle. Several fields and complex fields: the same, with the contractions of [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]] and [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 3.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free fields between free states, exact, independent of the dynamics; used with the Dyson series as in the opening.
>
> *Source: PS §4.6, p. 110 ("To evaluate an $S$-matrix element such as (4.92), we simply write down all possible full contractions of the $\phi_I$ operators *and* the external-state momenta"), p. 111 · Yu §7.1, p. 268 (boxed: "a nontrivial $T$-matrix element equals the result of contracting the field operators one by one with the initial- and final-state particles") · PHY 513, Problem Set 8, Problem 3(d)–(e) (the user's "only the Wick terms with exactly $n$ uncontracted fields survive") · proof written here*

^thm-c6b-2-3

> [!derivation]- Derivation
> **Step 1** (Wick). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], an operator identity,
>
> $$
> \langle f|T\{\hat\phi_1\cdots\hat\phi_\ell\}|i\rangle = \sum_C\;\prod_{\{a,b\}\in C}D_F(x_a - x_b)\;\langle f|{:}\textstyle\prod_{c\in R_C}\hat\phi_c{:}|i\rangle , \qquad R_C = \{1, \dots, \ell\}\setminus\cup C .
> $$
>
> **Step 2** (split the remainder). By [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], 1,
>
> $$
> {:}\prod_{c\in R}\hat\phi_c{:} = \sum_{A\subseteq R}\;\prod_{a\in A}\hat\phi_a^-\prod_{b\in R\setminus A}\hat\phi_b^+ .
> $$
>
> **Step 3** (the $\hat\phi^+$ on the incoming particles). By [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 1–2, applied once per field (relativistic states, each removal $e^{-ik\cdot x}$),
>
> $$
> \prod_{b\in R\setminus A}\hat\phi_b^+\,|\mathbf k_1\cdots\mathbf k_n\rangle = \sum_{\beta}\;\prod_{b\in R\setminus A}e^{-ik_{\beta(b)}\cdot x_b}\;\bigl|\{\mathbf k_i\}_{i\notin\beta(R\setminus A)}\bigr\rangle ,
> $$
>
> the sum over injective maps $\beta$ from $R\setminus A$ to the incoming particles; no such map if $|R\setminus A| > n$ (a $\hat\phi^+$ meets $|0\rangle$).
>
> **Step 4** (the $\hat\phi^-$ on the outgoing particles). Taking adjoints in Step 3 ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]]),
>
> $$
> \langle\mathbf p_1\cdots\mathbf p_m|\prod_{a\in A}\hat\phi_a^- = \sum_{\alpha}\;\prod_{a\in A}e^{+ip_{\alpha(a)}\cdot x_a}\;\bigl\langle\{\mathbf p_j\}_{j\notin\alpha(A)}\bigr| ,
> $$
>
> $\alpha$ injective from $A$ to the outgoing particles.
>
> **Step 5** (the particles left over). The remaining overlap is ([[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-5|Theorem §C6b.11.5]], relativistic form)
>
> $$
> \langle\mathbf p_{j_1}\cdots\mathbf p_{j_s}|\mathbf k_{i_1}\cdots\mathbf k_{i_{s'}}\rangle = \delta_{ss'}\sum_{\pi\in S_s}\prod_{u=1}^s2E_{\mathbf k_{i_u}}(2\pi)^3\delta^3(\mathbf p_{j_{\pi(u)}} - \mathbf k_{i_u}) ,
> $$
>
> a sum over bijections, each pair $\overbracket{\langle\mathbf p|\mathbf k\rangle}$.
>
> **Step 6** (assemble). A term of Steps 1–5 is a choice $(C, A, \beta, \alpha, \pi)$, and it is the product of the values of the pairs: $C$ (field–field), $\{b, \beta(b)\}$ (field–incoming), $\{\alpha(a), a\}$ (outgoing–field), $\pi$ (outgoing–incoming). Conversely a full contraction determines $C$, $A$ (the fields paired with outgoing particles), $\beta$, $\alpha$, $\pi$ uniquely. So the sum is over full contractions, each once; a remainder field not paired with a particle gives no term (Steps 3–4).
>
> **Step 7** (the case $\ell = 2$, $n = m = 1$). Steps 1–2: $T\{\hat\phi_1\hat\phi_2\} = D_F(x_1 - x_2) + \hat\phi_1^+\hat\phi_2^+ + \hat\phi_2^-\hat\phi_1^+ + \hat\phi_1^-\hat\phi_2^+ + \hat\phi_1^-\hat\phi_2^-$. Between $\langle\mathbf p|$ and $|\mathbf k\rangle$: $\hat\phi^+\hat\phi^+|\mathbf k\rangle = 0$ (one particle, two removals) and $\langle\mathbf p|\hat\phi^-\hat\phi^- = 0$, so
>
> $$
> \langle\mathbf p|T\{\hat\phi_1\hat\phi_2\}|\mathbf k\rangle = \overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\langle\mathbf p|\mathbf k\rangle} + \overbracket{\langle\mathbf p|\hat\phi_2}\,\overbracket{\hat\phi_1|\mathbf k\rangle} + \overbracket{\langle\mathbf p|\hat\phi_1}\,\overbracket{\hat\phi_2|\mathbf k\rangle} = D_F(x_1 - x_2)\,2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k) + e^{ip\cdot x_2}e^{-ik\cdot x_1} + e^{ip\cdot x_1}e^{-ik\cdot x_2} ,
> $$
>
> the three full contractions.
>
> **What the derivation shows.**
> - The vacuum version ([[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]) is the case $n = m = 0$: then only $R = \varnothing$ survives.
> - The outgoing–incoming pairs are the particles that pass through untouched; with all outgoing momenta different from the incoming ones they vanish, and every particle must attach to a field.

^der-c6b-2-3

*Uses:* [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.5 Normal Ordering and Contractions#^thm-c6a-5-1|Theorem §C6a.5.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-1|Lemma §C6b.2.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-5|Theorem §C6b.11.5]]

## Which terms are scattering

> [!definition] Definition §C6b.2.1: The δ-Line
> A particle that passes from the initial to the final state without reaching any vertex contributes the overlap of [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]],
>
> $$
> \overbracket{\langle\mathbf p'|\mathbf p\rangle} = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf p') ,
> $$
>
> drawn as a line from the incoming to the outgoing particle, the **$\delta$-line** (dashed in these notes). With $A$, $B$ written on the left and $1$, $2$ on the right, the zeroth-order $2 \to 2$ element is two pictures, $A$–$1$, $B$–$2$ and $A$–$2$, $B$–$1$:
>
> $$
> {}_0\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle_0 = 2E_A2E_B(2\pi)^6\bigl[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + \delta^3(\mathbf p_A - \mathbf p_2)\delta^3(\mathbf p_B - \mathbf p_1)\bigr] .
> $$
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free relativistic states, exact; it appears only in the diagrams of $S$-matrix elements before the terms of the $\mathbb 1$ are dropped ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]]): the rules for $i\mathcal M$ have no $\delta$-lines.
>
> *Source: PHY 513 Lecture 16 (Larsen, 2 Nov 2026), slides 10–11 ("Encode essential combinatorial data in diagrams … Caution: line = $\delta$"), and transcript ("this kind of Feynman rules, where a single line is a delta function, will appear only today") · the user's PHY 513 notes, Lecture 16 update, §16.3, Definition "The $\delta$-line (this lecture only)" and eq. (orderzero) · PS §4.6, p. 109, eq. (4.91), and the diagrams on p. 110*

^def-c6b-2-1

> [!theorem] Theorem §C6b.2.4: Which Terms of the S-Matrix Element Belong to iT̂
> Let $|i\rangle = |\mathbf k_1\cdots\mathbf k_n\rangle$, $\langle f| = \langle\mathbf p_1\cdots\mathbf p_m|$ be relativistically normalized free states, and expand ${}_0\langle f|T\{\exp[-i\int_{-T}^{T}dt\,\hat H_I]\}|i\rangle_0$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], 2) by [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]]: each term is a diagram whose external points are the particles. Split it into its connected pieces. Then
> 1. each piece with particles carries its own momentum delta: a lone pair $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$ (a particle attached to no vertex: the $\delta$-line of [[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]]; [[§C6b.2 Matrix Elements between Particle States#^cau-c6b-2-2|Caution: A line is a δ, not a D_F]]), a piece with vertices $(2\pi)^4\delta^4(\sum k - \sum p)$ over its own particles;
> 2. **vacuum bubbles** (pieces without particles) factor out as $\langle0|U(T, -T)|0\rangle$ and are omitted;
> 3. **several pieces with particles**: each conserves momentum separately; if every piece is $1 \to 1$ (a $\delta$ line, or a line with insertions passing through), the final momenta equal the initial ones and the term belongs to the $\mathbb 1$ of $\hat S = \mathbb 1 + i\hat T$; otherwise it is a product of smaller processes; neither has the form $\delta^4(\sum k - \sum p)\times$(smooth) of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]];
> 4. **one piece with all particles** (fully connected): a part hanging on one external leg, separated from the rest by one propagator, is a correction of the external state; its propagator carries the on-shell momentum of the particle, $\frac{i}{k^2 - m^2}\big|_{k^2 = m^2}$, and it is removed by amputation ([[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]]);
> 5. the rest, the fully connected amputated diagrams, is $\langle f|i\hat T|i\rangle = (2\pi)^4\delta^4(\sum k - \sum p)\,i\mathcal M$ at the order considered ([[§C6b.3 Feynman Rules for Amplitudes#^thm-c6b-3-3|Theorem §C6b.3.3]]).
>
> $\phi^4$, $2 \to 2$, through first order (slides 10–18; PS (4.91)–(4.98)):
>
> | term | pieces | value | class |
> |---|---|---|---|
> | $\lambda^0$ | two $\delta$ lines | $2E_A2E_B(2\pi)^6[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + (1 \leftrightarrow 2)]$ | 3: the $\mathbb 1$ |
> | $\lambda$, $3$ full contractions | figure-eight $\times$ two $\delta$ lines | $-\frac{i\lambda}{8}D_F(0)^2\int d^4z\times(\lambda^0\text{ term})$ | 2 and 3 |
> | $\lambda$, $6$ single contractions | loop on a passing line $\times$ a $\delta$ line, four diagrams | each $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4(p_A - p_1)\cdot2E_B(2\pi)^3\delta^3(\mathbf p_B - \mathbf p_2)$ and permutations | 3: forward, the $\mathbb 1$ |
> | $\lambda$, no contraction | one vertex | $-i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)$ | 5: $i\mathcal M = -i\lambda$ |
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* any polynomial interaction, every order, with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]] (and its scope); the external-state corrections of part 4 return beyond lowest order as $\sqrt Z$ and the physical mass ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]]; [[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]; second semester).
>
> *Source: PHY 513 Lecture 16, slides 10–18 (slide 11: "This is part of '1' in $\mathcal S = 1 + i\mathcal T$ ⇒ omit this contribution when computing '$i\mathcal T$'"; slide 14: "Overall figure 8 = vacuum bubble ⇒ omit … same momenta in initial+final states ⇒ contribution to '1' … Either 1. or 2. justifies omitting this diagram"; slide 17: "Self-energy (bubble on line) conserves energy ⇒ same momentum in initial and final state ⇒ diagram contributes to '1' in $\mathcal S = 1 + i\mathcal T$ ⇒ omit. Remark: self-energy corrects free state → interacting state"), slides 25–26 · PS §4.6, pp. 109–113, eqs. (4.90)–(4.98), (4.101)–(4.102) ("Only *fully connected* diagrams, in which all external lines are connected to each other, contribute to the $T$-matrix", p. 111) · the user's PHY 513 notes, Lecture 16 update, §16.3–§16.4 (Table "The first-order matrix element, term by term"; Caution "The partial-contraction count on the slide") and §16.7 ("Why connected", "Why amputated") · PHY 513 Lecture 16, transcript (the figure-eight term "should absolutely not be part of my Feynman rules for two reasons, at least") · proof written here*

^thm-c6b-2-4

> [!derivation]- Derivation
> **Step 1** (pieces factor). A term of [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]] is a product of pair values times the vertex integrals $\int\prod_vd^4z_v$. A pair joins two nodes of the same piece, so the integrand is a product over pieces, each depending only on the $z_v$ of its own vertices, and the integral factorizes (each $z_v$ belongs to one piece):
>
> $$
> \text{term} = \prod_{\text{pieces }P}\Bigl(\int\prod_{v\in P}d^4z_v\;\prod_{\text{pairs in }P}(\text{value})\Bigr) .
> $$
>
> **Step 2** (part 1, one delta per piece). A lone pair is $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$ (Theorem §C6b.2.3). For a piece with vertices, insert the Fourier form of each internal line; the particles enter through $e^{-ik\cdot z}$, $e^{+ip\cdot z}$ ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 2); each vertex integral gives $(2\pi)^4\delta^4$ of the momenta at that vertex ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], 1). Doing the internal momentum integrals along a spanning tree of the piece (Step 3 of [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]]) uses all deltas but one, which is $(2\pi)^4\delta^4(\sum_{\rm in}k - \sum_{\rm out}p)$ over the particles of the piece.
>
> **Step 3** (part 2, bubbles). The pieces without particles share no line with the others; summed over all terms they factor out exactly as in [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], and their sum is $\langle0|U(T, -T)|0\rangle$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]]), the normalization that [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], 2, omits (Step 4 of its derivation).
>
> **Step 4** (part 3). A $1 \to 1$ piece carries $\delta^4(k - p)$ (or $\delta^3(\mathbf p - \mathbf k)$) with $k$, $p$ on the mass shell, so $p = k$ ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]], 4): if every piece is $1 \to 1$, every final momentum equals an initial one, the "nothing happened" part of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]. Otherwise there are at least two deltas in independent combinations of the momenta, and the term is a product of processes on subsets of the particles; it is not $\delta^4(\sum k - \sum p)$ times a smooth function, the form of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]] that defines $\mathcal M$ ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-2|Theorem §C6b.10.2]] for the free four-point function).
>
> **Step 5** (part 4). Let a propagator $\ell$ separate a part $X$ holding a single particle, of momentum $k$, from the rest. Step 2 applied to $X$, with $\ell$ as its second external line, fixes the momentum of $\ell$ to $k$, so $\ell$ contributes
>
> $$
> \frac{i}{k^2 - m^2 + i\varepsilon}\Big|_{k^2 = m^2} = \frac{i}{i\varepsilon} \xrightarrow{\varepsilon\to0^+} \infty
> $$
>
> (PS (4.102): "$\frac{1}{p'^2 - m^2}\big|_{p' = p_B} = \frac{1}{0}$"). $X$ turns the free particle into the dressed one ("self-energy: wave function of external state corrected from free to interacting", slide 25), not a scattering between different particles; the amputation of [[§C6b.3 Feynman Rules for Amplitudes#^def-c6b-3-1|Def. §C6b.3.1]] removes it.
>
> **Step 6** (part 5). What is left has one piece, so one overall delta (Step 2), and no external-state part: by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] its sum is $(2\pi)^4\delta^4(\sum k - \sum p)\,i\mathcal M$.
>
> **Step 7** (the table). Zeroth order: $T\{\cdots\} \to 1$ and
>
> $$
> {}_0\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle_0 = \sqrt{2E_12E_22E_A2E_B}\,\langle0|\hat a_1\hat a_2\hat a^\dagger_A\hat a^\dagger_B|0\rangle = 2E_A2E_B(2\pi)^6\bigl[\delta^3(\mathbf p_A - \mathbf p_1)\delta^3(\mathbf p_B - \mathbf p_2) + \delta^3(\mathbf p_A - \mathbf p_2)\delta^3(\mathbf p_B - \mathbf p_1)\bigr]
> $$
>
> (slide 10, PS (4.91)), two $1 \to 1$ pieces per term. First order, with the Wick expansion of [[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1|Example §C6b.2.1]], Step 2:
> - full contractions: $-\frac{i\lambda}{4!}\cdot3D_F(0)^2\int d^4z\;{}_0\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle_0 = -\frac{i\lambda}{8}D_F(0)^2\int d^4z\times(\text{zeroth order})$ (slide 14: "$-\frac18i\lambda$");
> - one contraction, $\overbracket{\hat\phi_a\hat\phi_b}\,{:}\hat\phi_c\hat\phi_d{:}$, $6$ terms: the two remaining fields take one incoming and one outgoing particle ($2$ ways for each of the $4$ choices $(A, 1)$, $(A, 2)$, $(B, 1)$, $(B, 2)$), the other two particles overlap; for $(A, 1)$
>
> $$
> -\frac{i\lambda}{4!}\cdot6\cdot2\,D_F(0)\int d^4z\,e^{-ip_A\cdot z}e^{ip_1\cdot z}\;\overbracket{\langle\mathbf p_2|\mathbf p_B\rangle} = -\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4(p_A - p_1)\,2E_B(2\pi)^3\delta^3(\mathbf p_B - \mathbf p_2)
> $$
>
> (slide 16: "5 permutations ⇒ factor 6"; the $6$ counts the contracted pair, each picture gets $6\cdot2 = 12$ pairings, $\frac{12}{4!} = \frac12 = \frac1S$ of the tadpole: the user's notes, Caution "The partial-contraction count on the slide"), forward;
> - no contraction: $4!$ attachments, $-i\lambda(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2)$ (Example §C6b.2.1, Steps 3–4; slide 18).
>
> **What the derivation shows.**
> - "Connected" and "amputated" are not extra assumptions: disconnected terms are the $\mathbb 1$, bubbles or smaller processes (each piece its own delta), and external-leg parts are state corrections with an on-shell propagator.
> - Two reasons can exclude the same term (slide 14: the bubble and the $\mathbb 1$); either suffices.

^der-c6b-2-4

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-5|Theorem §C6a.12.5]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^der-c6a-12-3|Derivation §C6a.12.3]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-4|Theorem §C6a.11.4]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-2|Theorem §C6b.10.2]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

![[ph-qft-c6b-2-5.svg]]
*The classes of [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]] for $\phi\phi \to \phi\phi$ (dashed red: $\delta$-lines, [[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]]; blue: vertices). (1) Zeroth order, the particles pass through. (2) The figure-eight bubble times the same (slide 14). (3) A loop on a passing line next to a $\delta$ line, one of four (slide 16): energy conservation forces $p_1 = p_A$. (4) A loop on the leg of $A$ at order $\lambda^2$ (slide 26): a correction of the external state, removed by amputation. (5) The vertex, the only term of $i\hat T$ at first order. Added figure.*

> [!caution] Caution: A line is a δ, not a D_F
> The same drawn line means two things in Lecture 16. In the diagrams of ${}_0\langle f|T\{\cdots\}|i\rangle_0$ two kinds of line look alike. A line from an incoming particle straight to an outgoing one, touching no vertex, is the overlap $\overbracket{\langle\mathbf p|\mathbf k\rangle} = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf p - \mathbf k)$; a line between two vertices, or a loop, is $D_F$. The slides: "Caution: line = $\delta$ (not standard rule where line = $D_F$)" (slide 10); "line = $D_F$ in figure 8 but line = $\delta$ inside round brackets" (slide 14); "direct line is a $\delta$-function" (slide 16). In the diagrams of correlation functions every line is a $D_F$ ([[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-4|Theorem §C6a.8.4]]); an external line of an amplitude diagram is neither: a plane wave $e^{\mp ip\cdot x}$ in position space ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 2) and $1$ in momentum space. Figure ph-qft-c6b-2-5 and the user's notes draw the $\delta$-lines ([[§C6b.2 Matrix Elements between Particle States#^def-c6b-2-1|Def. §C6b.2.1]]) dashed and keep solid lines for propagators and wave functions; "this kind of Feynman rules, where a single line is a delta function, will appear only today".
>
> *Source: PHY 513 Lecture 16, slides 10, 14, 16, and transcript · the user's PHY 513 notes, Lecture 16 update, §16.3, Caution "The same line means two different things in the lecture" · PS §4.6, eqs. (4.91), (4.96)*

^cau-c6b-2-2

## First order: enumerate, then filter

> [!theorem] Theorem §C6b.2.5: The First-Order Matrix Elements of a Monomial
> Let $\mathcal L_{\rm int} = -g\,M$, $M = \prod_k\phi_k^{m_k}$ a monomial in real fields without derivatives ([[§C6a.12 Feynman Rules for Polynomial Interactions#^def-c6a-12-1|Def. §C6a.12.1]]). Let $|i\rangle$ and $\langle f|$ hold $n_k$ particles of kind $k$ in total, with no outgoing momentum equal to an incoming one. Then
>
> $$
> \langle f|i\hat T^{(1)}|i\rangle = -ig\int d^4x\,\langle f|M\bigl(\hat\phi_I(x)\bigr)|i\rangle = -ig\prod_k\frac{m_k!}{2^{\ell_k}\,\ell_k!}\,D_F^{(m_k)}(0)^{\ell_k}\;(2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr), \qquad \ell_k = \frac{m_k - n_k}{2} ,
> $$
>
> nonzero only if every $m_k - n_k$ is even and $\ge 0$: each leg takes one external particle or is closed with another leg of its kind into a loop. In particular, for a tree ($\ell_k = 0$, every leg on a particle), $i\mathcal M = -ig\prod_km_k!$, the vertex factor ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]).
>
> **Procedure** (Yu's enumerate-then-filter): (1) list every split of the legs of $M$ into incoming particles, outgoing particles and pairs closed into loops, each giving a matrix element above; (2) keep those that four-momentum conservation allows on the mass shell ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]; *applies:* first order, free relativistic states over $|0\rangle$ in place of the in and out states (as in the opening: lowest order; a loop $D_F(0)$ on a single particle is a mass shift, [[§C6b.10 Amplitudes from Correlation Functions#^cau-c6b-10-2|§C6b.10, Caution: The rule is stated at lowest order]]); complex fields: the legs $\phi$, $\phi^\dagger$ take particles and antiparticles by [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 3.
>
> *Source: Yu §7.1.1, pp. 264–272 (all first-order $T$-matrix elements of Yukawa theory, eqs. (7.21)–(7.43), Fig. 7.1–7.2; "the 10 Feynman diagrams correspond to 10 dynamically allowed processes; most are kinematically forbidden", p. 272); §7.3, eqs. (7.115)–(7.121) · PS §4.6, eqs. (4.92)–(4.98) · proof written here*

^thm-c6b-2-5

> [!derivation]- Derivation
> **Step 1** (first order). $\hat S = \mathbb 1 + i\hat T$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]]) and the $n = 1$ term of the Dyson series ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]]) with $\hat{\mathcal H}_I = gM(\hat\phi_I)$: $i\hat T^{(1)} = -i\int dt\,\hat H_I(t) = -ig\int d^4x\,M(\hat\phi_I(x))$; one time, so $T\{\cdot\}$ acts trivially.
>
> **Step 2** (Wick between the states). Label the $m_k$ factors of kind $k$ as legs. By [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]] (all fields at $x$; [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]] for several kinds), $\langle f|M|i\rangle$ is the sum over full contractions of legs and particles. Outgoing–incoming pairs give $\delta^3(\mathbf p - \mathbf k) = 0$ (distinct momenta); leg–leg pairs give $D_F^{(m_k)}(x - x) = D_F^{(m_k)}(0)$ (formal, [[§C6a.5 Normal Ordering and Contractions#^cau-c6a-5-3|§C6a.5, Caution: In what sense these identities hold]]); a particle pairs only with a leg of its kind.
>
> **Step 3** (count, per kind). The $n_k$ distinct particles of kind $k$ go injectively to the $m_k$ legs, $m_k(m_k - 1)\cdots(m_k - n_k + 1) = \frac{m_k!}{(2\ell_k)!}$ ways; the remaining $2\ell_k$ legs pair in $(2\ell_k - 1)!! = \frac{(2\ell_k)!}{2^{\ell_k}\ell_k!}$ ways ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]); the product is $\frac{m_k!}{2^{\ell_k}\ell_k!}$. If $m_k - n_k$ is odd or negative, no full contraction exists. Kinds are independent.
>
> **Step 4** (the vertex integral). Every term carries $\prod_ie^{-ik_i\cdot x}\prod_je^{+ip_j\cdot x}$ ([[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], 2), and with [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]
>
> $$
> \int d^4x\,e^{i(\sum_jp_j - \sum_ik_i)\cdot x} = (2\pi)^4\delta^4\Bigl(\sum_ik_i - \sum_jp_j\Bigr) .
> $$
>
> **Step 5** (tree). $\ell_k = 0$ for all $k$: $\langle f|i\hat T^{(1)}|i\rangle = -ig\prod_km_k!\,(2\pi)^4\delta^4(\cdots)$, and [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] gives $i\mathcal M = -ig\prod_km_k!$. Checks ([[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1|Example §C6b.2.1]]): $\phi^4$, $m = 4$, $n = 4$: $\frac{\lambda}{4!}\cdot24$; $n = 2$: $\frac{4!}{2} = 12$ (the tadpole, $\frac{12}{24} = \frac12$); $n = 0$: $\frac{4!}{4\cdot2} = 3$ (the figure-eight, $\frac{3}{24} = \frac18$), the counts of [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-1|Example §C6a.9.1]].
>
> **What the derivation shows.**
> - At first order the operator content of $\mathcal L_{\rm int}$ alone decides which processes have a matrix element; kinematics decides which of them happen.

^der-c6b-2-5

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-6|Theorem §C6a.3.6]], [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]], [[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]], [[§C6b.2 Matrix Elements between Particle States#^lem-c6b-2-2|Lemma §C6b.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!theorem] Theorem §C6b.2.6: The Kinematic Filter
> Let all external particles be on shell, $p^0 = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2} > 0$. Then $\delta^4\bigl(\sum_{\rm in}p - \sum_{\rm out}p\bigr)$ restricted to the mass shells
> 1. vanishes if one side has no particles and the other has at least one ($0 \to n$, $n \to 0$);
> 2. vanishes for one incoming particle of mass $M > 0$ and outgoing masses $m_1, \dots, m_n$, $n \ge 2$, if $M < \sum_im_i$; for $M = \sum_im_i$ it is supported on the set where every product is at rest in the frame of the decaying particle, of measure zero in the final momenta;
> 3. vanishes for $n \ge 2$ incoming particles of masses $m_i$ and one outgoing of mass $M > 0$ if $M < \sum_im_i$ (part 2 reversed);
> 4. for one incoming and one outgoing particle, requires $p_{\rm out} = p_{\rm in}$: forward, with equal masses.
>
> For equal masses $m > 0$ every $1 \to n$ and $n \to 1$ with $n \ge 2$ is forbidden.
>
> *Model:* any (kinematics); *applies:* on-shell external momenta, any theory; it filters the matrix elements of [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]] at every order.
>
> *Source: Yu §7.1.1, p. 272 ("most of these processes are kinematically not allowed, because the initial and final states cannot satisfy energy-momentum conservation at the same time … when $m_\phi > 2m_\psi$, two processes are exceptions"); §6.5.4, threshold (6.378) · PHY 513, Problem Set 8, Problem 4 ("provided that $M > 2m$") · proof written here*

^thm-c6b-2-6

> [!derivation]- Derivation
> **Step 1** (part 1). Each $p^0 = E_{\mathbf p} > 0$, so a nonempty side has $\sum p^0 > 0$ and the empty side $0$: $\sum_{\rm in}p^0 - \sum_{\rm out}p^0 \ne 0$ on the whole mass shell, and the delta vanishes there ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]).
>
> **Step 2** (frame). The support condition $\Delta \equiv \sum_{\rm in}p - \sum_{\rm out}p = 0$ is Lorentz covariant, $\Lambda\Delta = 0 \Leftrightarrow \Delta = 0$, and $\delta^4(\Lambda\Delta) = \delta^4(\Delta)$ (Step 3 of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-6|Derivation §C6b.1.6]]): it may be checked in any frame.
>
> **Step 3** (part 2). In the rest frame of the incoming particle, $p_{\rm in} = (M, \mathbf 0)$. Conservation requires
>
> $$
> M = \sum_{i=1}^nE_{\mathbf p_i} = \sum_{i=1}^n\sqrt{\mathbf p_i^2 + m_i^2} \ \ge\ \sum_{i=1}^nm_i , \qquad \sum_i\mathbf p_i = \mathbf 0 ,
> $$
>
> with equality iff every $\mathbf p_i = \mathbf 0$. So for $M < \sum m_i$ no momenta satisfy it, and for $M = \sum m_i$ only $\mathbf p_1 = \cdots = \mathbf p_n = \mathbf 0$, one point.
>
> **Step 4** (part 3). The same in the rest frame of the outgoing particle, $p_{\rm out} = (M, \mathbf 0)$, with the roles of in and out exchanged.
>
> **Step 5** (part 4). $p_{\rm in} = p_{\rm out}$ as four-vectors; then $m_{\rm in}^2 = p_{\rm in}^2 = p_{\rm out}^2 = m_{\rm out}^2$ and $\mathbf p_{\rm out} = \mathbf p_{\rm in}$.
>
> **Step 6** (equal masses). $M = m < nm$ for $n \ge 2$: parts 2–3.
>
> **What the derivation shows.**
> - A decay needs $M > \sum m_i$ (for two bodies, $M > 2m$); a one-vertex fusion $n \to 1$ is the reverse, possible only at the special incoming momenta with $(\sum p_i)^2 = M^2$.

^der-c6b-2-6

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^der-c6b-1-6|Derivation §C6b.1.6]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-3|P6, step 3]]

> [!example] Example §C6b.2.1: φφ → φφ at First Order, by Contractions with the External States
> ![[ph-qft-c6b-2-1.svg]]
>
> In $\phi^4$ theory ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), for $\mathbf p_1, \mathbf p_2 \notin \{\mathbf p_A, \mathbf p_B\}$,
>
> $$
> \langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf p_A\mathbf p_B\rangle = -i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2), \qquad i\mathcal M = -i\lambda ;
> $$
>
> the $4!$ ways of attaching the four particles to the four fields cancel the $\frac{1}{4!}$. The other first-order processes are $1 \leftrightarrow 3$, $0 \leftrightarrow 4$ (forbidden), $0 \leftrightarrow 2$ with a loop (forbidden), $1 \to 1$ with a loop (forward only: a mass shift), and the vacuum bubble.
>
> **Step 1** (first order). [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]], Step 1, with the four factors of $\hat\phi_I(x)^4$ labelled $\hat\phi_1, \dots, \hat\phi_4$ (all at $x$):
>
> $$
> \langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf p_A\mathbf p_B\rangle = -\frac{i\lambda}{4!}\int d^4x\,\langle\mathbf p_1\mathbf p_2|T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\}|\mathbf p_A\mathbf p_B\rangle .
> $$
>
> **Step 2** (Wick: time order → normal order plus contractions). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], with $\overbracket{\hat\phi_a\hat\phi_b} = D_F(0)$,
>
> $$
> T\{\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4\} = {:}\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4{:} + \bigl(\overbracket{\hat\phi_1\hat\phi_2}\,{:}\hat\phi_3\hat\phi_4{:} + \cdots\bigr)_{6\text{ terms}} + \bigl(\overbracket{\hat\phi_1\hat\phi_2}\,\overbracket{\hat\phi_3\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_3}\,\overbracket{\hat\phi_2\hat\phi_4} + \overbracket{\hat\phi_1\hat\phi_4}\,\overbracket{\hat\phi_2\hat\phi_3}\bigr)
> $$
>
> (PS (4.95)).
>
> **Step 3** (between the states). By [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]], all four particles must be paired, and outgoing–incoming pairs vanish ($\mathbf p_1, \mathbf p_2 \notin \{\mathbf p_A, \mathbf p_B\}$):
> - the last three terms: $3D_F(0)^2\langle\mathbf p_1\mathbf p_2|\mathbf p_A\mathbf p_B\rangle = 0$ (a bubble times the "1", PS (4.96));
> - $D_F(0)\langle\mathbf p_1\mathbf p_2|{:}\hat\phi_a\hat\phi_b{:}|\mathbf p_A\mathbf p_B\rangle$: two fields take two particles, the other two would pair with each other: $0$ (PS's four diagrams on p. 111, particles passing by) — the classes of [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-4|Theorem §C6b.2.4]]: the bubble with $\delta$-lines (parts 2–3), the forward pieces (part 3), the vertex (part 5);
> - ${:}\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4{:}$: every field takes one particle. With $\sigma \in S_4$ giving the fields of $\mathbf p_1, \mathbf p_2, \mathbf p_A, \mathbf p_B$,
>
> $$
> \langle\mathbf p_1\mathbf p_2|{:}\hat\phi_1\hat\phi_2\hat\phi_3\hat\phi_4{:}|\mathbf p_A\mathbf p_B\rangle = \sum_{\sigma\in S_4}\overbracket{\langle\mathbf p_1|\hat\phi_{\sigma(1)}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{\sigma(2)}}\,\overbracket{\hat\phi_{\sigma(3)}|\mathbf p_A\rangle}\,\overbracket{\hat\phi_{\sigma(4)}|\mathbf p_B\rangle} = \sum_{\sigma\in S_4}e^{ip_1\cdot x}e^{ip_2\cdot x}e^{-ip_A\cdot x}e^{-ip_B\cdot x} ,
> $$
>
> the $24$ assignments $(\sigma(1)\sigma(2)\sigma(3)\sigma(4))$:
>
> $$
> \begin{aligned}
> &1234,\ 1243,\ 1324,\ 1342,\ 1423,\ 1432, && 2134,\ 2143,\ 2314,\ 2341,\ 2413,\ 2431,\\
> &3124,\ 3142,\ 3214,\ 3241,\ 3412,\ 3421, && 4123,\ 4132,\ 4213,\ 4231,\ 4312,\ 4321 ,
> \end{aligned}
> $$
>
> each the same plane wave, since all four fields sit at $x$.
>
> **Step 4** (vertex integral). [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]:
>
> $$
> -\frac{i\lambda}{4!}\cdot24\int d^4x\,e^{i(p_1 + p_2 - p_A - p_B)\cdot x} = -i\lambda\,(2\pi)^4\delta^4(p_A + p_B - p_1 - p_2) ,
> $$
>
> and [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] gives $i\mathcal M = -i\lambda$ (PS (4.98); Yu (7.119), (7.121)).
>
> **Step 5** (enumerate, then filter). The splits of the four legs ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]]), with [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]] for equal masses $m$:
>
> | in → out | loops | matrix element | kinematics |
> |---|---|---|---|
> | $2 \to 2$ | $0$ | $-i\lambda\,(2\pi)^4\delta^4$ | allowed |
> | $1 \to 3$, $3 \to 1$ | $0$ | $-i\lambda\,(2\pi)^4\delta^4$ | forbidden, $m < 3m$ (parts 2, 3) |
> | $0 \to 4$, $4 \to 0$ | $0$ | $-i\lambda\,(2\pi)^4\delta^4$ | forbidden (part 1) |
> | $1 \to 1$ | $1$ | $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4$ | forward only (part 4): no scattering, a mass shift |
> | $0 \to 2$, $2 \to 0$ | $1$ | $-\frac{i\lambda}{2}D_F(0)\,(2\pi)^4\delta^4$ | forbidden (part 1) |
> | $0 \to 0$ | $2$ | $-\frac{i\lambda}{8}D_F(0)^2\,(2\pi)^4\delta^4(0)$ | the vacuum bubble, a phase ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-3\|Theorem §C6a.11.3]]) |
>
> *Two routes, one answer.* [[§C6b.10 Amplitudes from Correlation Functions#^ex-c6b-10-1|Example §C6b.10.1]] gets $i\mathcal M = -i\lambda$ from the four-point correlation function by amputation ([[§C6b.10 Amplitudes from Correlation Functions#^thm-c6b-10-1|Theorem §C6b.10.1]]); there the $24$ are the bijections of four external points to four legs, here of four particles to four legs.
>
> *Source: PS §4.6, eqs. (4.92)–(4.98), pp. 110–112 · Yu §7.3, eqs. (7.115)–(7.121) · the table written here from [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]] and [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]]*

^ex-c6b-2-1

> [!example] Example §C6b.2.2: Φφ² at First Order: the Factor 2 of Φ → φφ
> ![[ph-qft-c6b-2-2.svg]]
>
> In [[§C6b.9 Decay Rates and Widths#^mod-c6b-9-7|Model §C6b.9.7]] ($\mathcal L_{\rm int} = -\mu\Phi\phi^2$, masses $M$, $m$), the first-order processes are:
>
> | in → out | loops | $i\mathcal M$ | kinematics ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6\|Theorem §C6b.2.6]]) |
> |---|---|---|---|
> | $\Phi \to \phi\phi$ | $0$ | $-2i\mu$ | allowed iff $M > 2m$ (part 2) |
> | $\phi\phi \to \Phi$ | $0$ | $-2i\mu$ | allowed for $(p_1 + p_2)^2 = M^2$ (part 3) |
> | $\phi \to \Phi\phi$, $\Phi\phi \to \phi$ | $0$ | $-2i\mu$ | forbidden, $m < M + m$ (parts 2, 3) |
> | $0 \to \Phi\phi\phi$, $\Phi\phi\phi \to 0$ | $0$ | $-2i\mu$ | forbidden (part 1) |
> | $0 \to \Phi$, $\Phi \to 0$ | $1$ ($\phi$ loop) | $-i\mu D_F^{(m)}(0)$ | forbidden (part 1) |
>
> A $\phi$ leg cannot be left without partner, and the $\Phi$ leg cannot close on a $\phi$ leg ([[§C6a.12 Feynman Rules for Polynomial Interactions#^lem-c6a-12-1|Lemma §C6a.12.1]]); the counts are $\frac{1!\,2!}{2^{\ell}\ell!}$ of [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]].
>
> **The decay.** With the $\Phi$ field $\hat\Phi_x$ and the two $\phi$ fields $\hat\phi_{x1}$, $\hat\phi_{x2}$ of $\hat\Phi\hat\phi^2(x)$, and [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-3|Theorem §C6b.2.3]],
>
> $$
> \langle\mathbf p_1\mathbf p_2|{:}\hat\Phi_x\hat\phi_{x1}\hat\phi_{x2}{:}|\mathbf K\rangle_\Phi = \overbracket{\hat\Phi_x|\mathbf K\rangle}\Bigl(\overbracket{\langle\mathbf p_1|\hat\phi_{x1}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{x2}} + \overbracket{\langle\mathbf p_1|\hat\phi_{x2}}\,\overbracket{\langle\mathbf p_2|\hat\phi_{x1}}\Bigr) = 2\,e^{i(p_1 + p_2 - K)\cdot x} ,
> $$
>
> so $\langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf K\rangle_\Phi = -2i\mu(2\pi)^4\delta^4(K - p_1 - p_2)$, $i\mathcal M = -2i\mu$. The same computation with the operators written out, and the width and lifetime, are [[§C6b.9 Decay Rates and Widths#^ex-c6b-9-1|Example §C6b.9.1]] (Steps 3–5 for $\mathcal M$).
>
> *Source: PHY 513, Problem Set 8, Problem 4 (the user's solution: "each of $\hat a_{\mathbf p_1}, \hat a_{\mathbf p_2}$ … pairs with one of the two fields, in 2 ways") · PS Problem 4.2 · the table written here*

^ex-c6b-2-2

> [!example] Example §C6b.2.3: The Cubic Interaction at First Order: Everything Is Forbidden
> ![[ph-qft-c6b-2-3.svg]]
>
> For $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3$ (the cubic vertex of [[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]]) and on-shell particles of mass $m > 0$, every first-order matrix element with no forward pair vanishes:
>
> | in → out | loops | count $\frac{3!}{2^\ell\ell!}$ | matrix element | kinematics ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6\|Theorem §C6b.2.6]]) |
> |---|---|---|---|---|
> | $1 \to 2$, $2 \to 1$ | $0$ | $6$ | $-ig\,(2\pi)^4\delta^4$ | forbidden, $m < 2m$ (parts 2, 3) |
> | $0 \to 3$, $3 \to 0$ | $0$ | $6$ | $-ig\,(2\pi)^4\delta^4$ | forbidden (part 1) |
> | $0 \to 1$, $1 \to 0$ | $1$ | $3$ | $-\frac{ig}{2}D_F(0)\,(2\pi)^4\delta^4$ | forbidden (part 1) |
>
> **Step 1** (enumerate). Three legs: $n$ particles and $\ell$ loops with $n + 2\ell = 3$, so $(n, \ell) = (3, 0)$ or $(1, 1)$; the $n$ particles split into in and out in all ways ([[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]]). Coefficients: $-i\frac{g}{3!}\cdot6 = -ig$ and $-i\frac{g}{3!}\cdot3 = -\frac{ig}{2}$.
>
> **Step 2** (filter). $1 \to 2$ in the rest frame of the incoming particle: $m = E_{\mathbf p_1} + E_{\mathbf p_2} \ge 2m$, impossible for $m > 0$ (Theorem §C6b.2.6, Step 3); $2 \to 1$ likewise in the rest frame of the outgoing one; $0 \leftrightarrow 3$ and $0 \leftrightarrow 1$: positive energy on one side only.
>
> So the first process of the cubic theory between on-shell particles is at order $g^2$: $2 \to 2$ through two vertices ([[§C6b.3 Feynman Rules for Amplitudes#^ex-c6b-3-1|Example §C6b.3.1]]). Yu's Yukawa analogue ([[§C6c.4 Feynman Rules for Yukawa Theory#^ex-c6c-4-1|§C6c.4, Example §C6c.4.1]]): of the ten first-order processes only $\phi \to \psi\bar\psi$ and $\psi\bar\psi \to \phi$ survive, and only for $m_\phi > 2m_\psi$ (p. 272).
>
> *Source: Yu §7.1.1, p. 272 (the Yukawa analogue) · written here from [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-5|Theorem §C6b.2.5]] and [[§C6b.2 Matrix Elements between Particle States#^thm-c6b-2-6|Theorem §C6b.2.6]]*

^ex-c6b-2-3

> [!remark] Remark: Yu's route
> Yu computes $S$-matrix elements this way before any correlation function: he defines the contractions of each field with initial and final particles (eqs. (7.13)–(7.18)), lists all first-order $T$-matrix elements of Yukawa theory and filters them kinematically (p. 272), reads the position- and then momentum-space rules off the results (eqs. (7.25)–(7.28), §7.2), and justifies them only in ch. 10 through LSZ ("our method for leading-order processes in chapters 7, 8, 9 is justified", p. 474). He keeps the field operators in the order of $\mathcal L_{\rm int}$ to fix fermion signs (boxed rule, p. 268; in the vault's form, crossing contractions: [[§C6c.3 Wick's Theorem with Fermions#^thm-c6c-3-4|§C6c.3, Theorem §C6c.3.4]]); for scalars there are no signs. Yukawa theory with these rules: [[· C6c Feynman Rules for Fermions|C6c]]. The course reaches amplitudes from correlation functions ([[§C6b.10 Amplitudes from Correlation Functions|§C6b.10]]); the two routes agree at lowest order ([[§C6b.2 Matrix Elements between Particle States#^ex-c6b-2-1|Example §C6b.2.1]]).
>
> *Source: Yu §7.1, pp. 262–272; §7.2, pp. 287–288; §10.5.2, p. 474*

^rem-c6b-2-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give momentum deltas.

> [!remark]- Connections
> - The contraction of a field with an external particle is the one-particle wave function $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$; with interactions it carries $\sqrt Z$, the origin of the LSZ factor — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|§C2b.1, Caution: With interactions, the one-particle matrix element carries √Z]].
> - The $n!$ of identical particles appears twice: as the sum over $\sigma$ when particles attach to fields, and as the $\frac{1}{n!}$ of the $n$-particle measure ($S_{\rm id}$) — [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-11-5|Theorem §C6b.11.5]], [[§C6b.7 Evaluating the Cross Section#^thm-c6b-7-4|Theorem §C6b.7.4]].
> - The same expansion with a source vertex is exact and solves the classical-source problem — [[§C6b.11 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.11]].
> - The kinematic filter is the threshold of a decay, $M > \sum m_i$, the condition of the two-body decay formula — [[§C6b.9 Decay Rates and Widths#^thm-c6b-9-6|Theorem §C6b.9.6]].
