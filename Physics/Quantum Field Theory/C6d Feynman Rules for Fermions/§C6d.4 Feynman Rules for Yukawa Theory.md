---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.3 Wick's Theorem with Fermions]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.5 Fermion–Fermion Scattering]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 15–18 and 23, and transcript · the user's PHY 513 notes, Lecture 17 update, §17.4 (paragraph "Dashed and solid", Figure "yukprops"), §17.5 (Principle "Feynman rules for $i\mathcal M$ in Yukawa theory (momentum space)"), §17.7 (Principle "Feynman rules with fermions"), paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, p. 118 (rules 1–6) and pp. 118–120 (the comments) · Yu Zhao-Huan, 量子场论讲义, §7.1, eqs. (7.11)–(7.12), (7.23)–(7.24), (7.34), (7.40)–(7.41), (7.44), pp. 262–272, p. 275 (the $1/n!$ rule and its footnote); §7.2, rules 1–12 (pp. 287–288).*

[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] stated the rules for $i\mathcal M$ in scalar theories. With [[§C6d.1 Yukawa Theory|§C6d.1]]–[[§C6d.3 Wick's Theorem with Fermions|§C6d.3]] the same derivation runs for Yukawa theory, and this section collects the result ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-1|Theorem §C6d.4.1]], slides 16–18, PS p. 118). Three statements need their own proof: the vertex carries no $\frac{1}{3!}$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-2|Theorem §C6d.4.2]], from the user's discussion with Larsen), there are no symmetry factors ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]], slide 18), and the momentum on a fermion line runs along its arrow ([[§C6d.4 Feynman Rules for Yukawa Theory#^rem-c6d-4-1|Remark: The direction of momentum on fermion lines]]). The first application is the first-order decay $\phi \to f\bar f$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^ex-c6d-4-1|Example §C6d.4.1]]), the one first-order process of Yukawa theory that kinematics allows besides its inverse (Yu p. 272). "There's one more lecture with rules. Then after that, processes" (transcript): the QED rules of Lecture 18 join this chapter. Yu reads the same rules off first-order $T$-matrix elements in §7.1 and lists them in §7.2 (rules 1–12).

**Setup.** As in [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]], for [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]: free relativistic states over $|0\rangle$ stand for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); exact at the lowest order of a process, beyond it $\sqrt Z$ per external line and the physical masses ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). States are ordered as in [[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]].

## The rules

> [!theorem] Theorem §C6d.4.1: Feynman Rules for iℳ in Yukawa Theory
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], $i\mathcal M\,(2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})$ is the sum of all connected, amputated diagrams ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]) built from vertices with one dashed and two solid lines, one fermion arrow in and one out ([[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]]), each diagram the product of
>
> | element | position space | momentum space |
> |---|---|---|
> | vertex | $-ig\int d^4x$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3\|Theorem §C6d.1.3]]) | $-ig$, momentum conserved |
> | scalar propagator, $x$ to $y$ (dashed) | $D_F(x - y)$ | $\dfrac{i}{q^2 - m_\phi^2 + i\varepsilon}$ |
> | fermion propagator, arrow from $y$ to $x$ (solid) | $S_F(x - y)$ | $\dfrac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon} = \dfrac{i}{\slashed q - m + i\varepsilon}$, $q$ along the arrow |
> | external scalar, in / out | $e^{-ip\cdot x}$ / $e^{+ip\cdot x}$ | $1$ |
> | external fermion, in / out | $u^s(p)e^{-ip\cdot x}$ / $\bar u^s(p)e^{+ip\cdot x}$ | $u^s(p)$ / $\bar u^s(p)$ |
> | external antifermion, in / out | $\bar v^s(p)e^{-ip\cdot x}$ / $v^s(p)e^{+ip\cdot x}$ | $\bar v^s(p)$ / $v^s(p)$ |
> | momentum not fixed by conservation | — | $\int\frac{d^4\ell}{(2\pi)^4}$ |
>
> and:
> 1. each fermion line is written **against its arrow**, a row times matrices times a column, so that it is a number ([[§C6d.2 External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]]);
> 2. each closed fermion loop gives a factor $-1$ and a trace ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-5|Theorem §C6d.3.5]]);
> 3. the vertex carries no combinatorial factor, $-ig$ and not $-ig/3!$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-2|Theorem §C6d.4.2]]), and there are **no symmetry factors**, $S = 1$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]]);
> 4. each diagram carries the **sign** $(-1)^{\#\text{crossings}}$ of its contraction pattern with the external states ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|Theorem §C6d.3.4]]); the relative signs between diagrams are physical, the overall sign depends on the order of the external states ([[§C6d.5 Fermion–Fermion Scattering#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]).
>
> In momentum space the overall $(2\pi)^4\delta^4$ is stripped. *Equivalence:* for the scalar lines and vertices these are the rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]] with the vertex $-ig$ of a monomial with three distinct legs; what fermions add is the propagator $S_F$, the external spinors, items 1, 2 and 4, and $S = 1$ always. Conversely, deleting the fermion items leaves Theorem §C6c.6.3.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]: at the lowest order of a process exact, as [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]; loop corrections on internal lines by these rules; corrections on external legs excluded by amputation, with their $\sqrt Z$ and the physical masses deferred (second semester).
>
> *Source: PHY 513 Lecture 17, slide 16 ("Interaction at nth order: $\frac{1}{n!}T\bigl(-ig\int d^4x\,\bar\psi_I\psi_I\phi_I\bigr)^n$. Vertex $= -ig$. Propagators: … $\frac{i}{q^2 - m^2_\phi + i\epsilon}$ … $\frac{i(\slashed p + m)}{p^2 - m^2 + i\epsilon}$"), slide 12 (external lines), slide 18 ("Momentum conserved at vertices. Loop momenta … should be integrated. Symmetry factors: none … All diagrams must be connected and amputated. Sign of amplitude: determine from explicit contractions if it is needed"), slide 23 (loops) · the user's PHY 513 notes, Lecture 17 update, §17.5, Principle "Feynman rules for $i\mathcal M$ in Yukawa theory (momentum space)" (a principle there, a theorem here because it is derived), §17.7, Principle "Feynman rules with fermions" · PS §4.7, p. 118 (rules 1–6: "Figure out the overall sign of the diagram"), pp. 118–120 · Yu §7.2, rules 1–12 (pp. 287–288); position space: Yu (7.25)–(7.28), (7.31)–(7.33), (7.40)–(7.41) · proof written here from [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]]*

^thm-c6d-4-1

> [!derivation]- Derivation
> **Step 1** (the matrix element at order $n$). By Dyson's formula, valid with fermions ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]), and [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]],
>
> $$
> \langle f|\hat S|i\rangle^{(n)} = \frac{(-ig)^n}{n!}\int d^4x_1\cdots d^4x_n\;{}_0\langle f|\,T\bigl\{\hat{\bar\psi}\hat\psi\hat\phi(x_1)\cdots\hat{\bar\psi}\hat\psi\hat\phi(x_n)\bigr\}\,|i\rangle_0 .
> $$
>
> **Step 2** (full contractions). Wick's theorem with fermions ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-2|Theorem §C6d.3.2]]) turns $T$ into normal-ordered products and contractions; between the states only the terms in which every remaining field is contracted with an external particle survive (the argument of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]: a $\hat\Phi^+$ moved to the right must meet a creation operator of $|i\rangle$, a $\hat\Phi^-$ an annihilation operator of $\langle f|$). The terms that belong to $i\hat T$ are the fully connected, amputated ones ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]; their proofs move only whole packages and is unchanged by [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]).
>
> **Step 3** (values and signs). Each term is $(-1)^{\#\text{crossings}}$ times the product of the pair values ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|Theorem §C6d.3.4]]): $D_F$ and $S_F$ for internal lines, $e^{\mp ip\cdot x}$ for external scalars, the spinors times plane waves of [[§C6d.2 External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]] for external fermions; the spinor indices are summed along each line (item 1, [[§C6d.2 External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]]), closed lines give $-\operatorname{tr}$ (item 2).
>
> **Step 4** ($\frac{1}{n!}$). The $n!$ relabellings of the vertices give terms with equal values and equal signs, and a diagram whose pieces all touch an external particle arises from exactly $n!$ of them ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]]): the prefactor becomes $(-ig)^n$, one $-ig\int d^4x$ per vertex, $S = 1$.
>
> **Step 5** (momentum space). Insert $D_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2 - m_\phi^2 + i\varepsilon}e^{-iq\cdot(x - y)}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]) and $S_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}e^{-iq\cdot(x - y)}$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], stated there; its compact form $i/(\slashed q - m + i\varepsilon)$ is [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]]). Each vertex now carries three plane waves, and $\int d^4x\,e^{-i(\sum q_{\rm in})\cdot x} = (2\pi)^4\delta^4(\sum q_{\rm in})$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]), with $e^{-iq\cdot x}$ counted as $q$ flowing into $x$. For $S_F(x - y)$ the factor $e^{-iq\cdot x}$ sits at $x$ (the $\hat\psi$ end) and $e^{+iq\cdot y}$ at $y$ (the $\hat{\bar\psi}$ end): $q$ flows from $y$ to $x$, along the arrow. The internal momenta are fixed by the deltas up to $L$ loop integrals; the last delta is the overall one, stripped by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] (Steps 5–6 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]]).
>
> **Step 6** (checks). First order, $\phi \to f\bar f$: $i\mathcal M = -ig\,\bar u^s(p)v^{s'}(q)$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^ex-c6d-4-1|Example §C6d.4.1]]). Second order, $ff \to ff$: two diagrams with a relative minus sign ([[§C6d.5 Fermion–Fermion Scattering#^ex-c6d-5-1|Example §C6d.5.1]], PS (4.119)).
>
> **What the derivation shows.**
> - Nothing about the origin of the rules is new for fermions; the new items are bookkeeping of spinor indices and signs.
> - The amplitude is a number because each fermion line is a closed chain of spinor indices, and its sign is fixed only relative to the order of the external states.

^der-c6d-4-1

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.2 External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]], [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-5|Theorem §C6d.3.5]], [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!theorem] Theorem §C6d.4.2: The Yukawa Vertex Carries No Combinatorial Factor
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], let $|\mathbf P\rangle = \sqrt{2E_{\mathbf P}}\,\hat a^\dagger_{\phi,\mathbf P}|0\rangle$ be one scalar and $|\mathbf p, s; \mathbf k, r\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\hat a^{s\dagger}_{\mathbf p}\hat b^{r\dagger}_{\mathbf k}|0\rangle$ a fermion–antifermion pair, fermion first, with bra $\sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\langle0|\hat b^r_{\mathbf k}\hat a^s_{\mathbf p}$ ([[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). Then
>
> $$
> \langle\mathbf p, s; \mathbf k, r|\,\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)\,|\mathbf P\rangle = \bar u^s(p)\,v^r(k)\,e^{i(p + k - P)\cdot x} ,
> $$
>
> a single term with coefficient $1$: each of the three fields is used by exactly one external particle, $\hat\phi^+$ by the scalar, $\hat{\bar\psi}^-$ by the fermion ($\bar u$), $\hat\psi^-$ by the antifermion ($v$), and no field is left for an internal contraction; the number of assignments of fields to particles is $1\cdot1\cdot1 = 1$. Hence
>
> $$
> \langle\mathbf p, s; \mathbf k, r|i\hat T^{(1)}|\mathbf P\rangle = -ig\,\bar u^s(p)v^r(k)\,(2\pi)^4\delta^4(p + k - P) , \qquad i\mathcal M = -ig\,\bar u^s(p)v^r(k) :
> $$
>
> the vertex is $-ig$, not $-ig/3!$. With the opposite order of the pair, $\hat b^\dagger\hat a^\dagger|0\rangle$, the matrix element and $i\mathcal M$ change sign. *Contrast:* for $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3$ the three identical fields can be assigned to three scalars in $3!$ ways, and $-i\frac{g}{3!}\cdot3! = -ig$; in general $\mathcal L_{\rm int} = -g\prod_k\phi_k^{m_k}$ gives $-ig\prod_km_k!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]), and Yukawa theory has $m_{\bar\psi} = m_\psi = m_\phi = 1$. $\hat\psi$ and $\hat{\bar\psi}$ count as different fields, as $\hat\phi$ and $\hat\phi^\dagger$ of a complex scalar do ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 3). This is the vertex-level statement; the diagram-level one, the $\frac{1}{n!}$ against the $n!$ relabellings of vertices, is [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* first order, free states over $|0\rangle$ (the lowest order, as [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]); the matrix element is a statement about the factor and holds for any momenta; whether the decay is allowed is kinematics, $m_\phi > 2m$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^ex-c6d-4-1|Example §C6d.4.1]]).
>
> *Source: the user's discussion with Larsen after Lecture 17 (2026-11-04) ("if we were to write out the vertex explicitly such as $\langle p, k, s, r|\bar\psi\psi\phi|P\rangle$, there's no room for contraction") · written here · PHY 513 Lecture 17, slide 18 ("Fields in $\bar\psi\psi\phi$ cannot substitute for one another in contractions") · PS §4.7, p. 118 (first comment after the rules) · the general count: [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]]*

^thm-c6d-4-2

> [!derivation]- Derivation
> **Step 1** (eight terms). Split each field into its frequency parts ([[§C6d.2 External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]; [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]] for $\hat\phi$):
>
> $$
> \hat{\bar\psi}_a\hat\psi_a\hat\phi = \sum_{\sigma_1, \sigma_2, \sigma_3 = \pm}\hat{\bar\psi}^{\sigma_1}_a\hat\psi^{\sigma_2}_a\hat\phi^{\sigma_3} , \qquad 2\cdot2\cdot2 = 8 \text{ terms.}
> $$
>
> **Step 2** (the scalar factor). The state space is $\mathcal F_\psi \otimes \mathcal F_\phi$ ([[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], 1), the fermion operators act on the first factor and $\hat\phi$ on the second, and $|\mathbf P\rangle$ has no fermions, the bra no scalar. So the matrix element factorizes:
>
> $$
> \langle\mathbf p, s; \mathbf k, r|\,\hat{\bar\psi}_a\hat\psi_a\hat\phi\,|\mathbf P\rangle = \langle\mathbf p, s; \mathbf k, r|\hat{\bar\psi}_a\hat\psi_a|0\rangle_\psi\;\cdot\;\langle0|\hat\phi(x)|\mathbf P\rangle_\phi .
> $$
>
> In the scalar factor $\hat\phi^-|\mathbf P\rangle$ is a two-scalar state, orthogonal to $\langle0|$: $\sigma_3 = -$ gives $0$. $\sigma_3 = +$: $\langle0|\hat\phi^+(x)|\mathbf P\rangle = e^{-iP\cdot x}$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2). Four terms remain.
>
> **Step 3** (the fermion factor; no room for contraction). $\hat\psi^+|0\rangle = 0$ ($\hat\psi^+$ holds only $\hat a$'s), so $\sigma_2 = +$ gives $0$: two terms remain, $\hat{\bar\psi}^+\hat\psi^-|0\rangle$ and $\hat{\bar\psi}^-\hat\psi^-|0\rangle$. The first is the would-be internal contraction: $\hat{\bar\psi}^+_a\hat\psi^-_a|0\rangle = \bigl(\{\hat{\bar\psi}^+_a, \hat\psi^-_a\} - \hat\psi^-_a\hat{\bar\psi}^+_a\bigr)|0\rangle = \{\hat{\bar\psi}^+_a, \hat\psi^-_a\}|0\rangle$, a number times $|0\rangle$ (the $\hat b$, $\hat b^\dagger$ anticommutator, [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]; the tadpole $\overbracket{\hat{\bar\psi}_a\hat\psi_a}$ of [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-2|Theorem §C6d.3.2]]). Its matrix element is that number times $\langle\mathbf p, s; \mathbf k, r|0\rangle = 0$: after the fermions have contracted with each other, $\hat\phi$ is left alone between $\langle\mathbf p, s; \mathbf k, r|$ and $|\mathbf P\rangle$, and $\langle\mathbf p, \mathbf k|\hat\phi|\mathbf P\rangle = 0$ ($\hat\phi$ changes the scalar number by one and the fermion numbers by zero). Exactly one of the eight terms survives, $\sigma = (-, -, +)$. Counting: three fields, three external particles of three kinds; $\hat\phi$ can meet only the scalar, $\hat{\bar\psi}^-$ (with $\hat a^\dagger$) only the fermion, $\hat\psi^-$ (with $\hat b^\dagger$) only the antifermion: $1\cdot1\cdot1 = 1$ assignment.
>
> **Step 4** (evaluate). With the mode expansions (variables $\mathbf q$, $\mathbf l$, spins $s'$, $r'$):
>
> $$
> \langle\mathbf p, s; \mathbf k, r|\hat{\bar\psi}^-_a\hat\psi^-_a|0\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\int\frac{d^3q}{(2\pi)^3}\frac{d^3l}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}2E_{\mathbf l}}}\sum_{s', r'}\bar u^{s'}_a(q)e^{iq\cdot x}\,v^{r'}_a(l)e^{il\cdot x}\;\langle0|\hat b^r_{\mathbf k}\hat a^s_{\mathbf p}\,\hat a^{s'\dagger}_{\mathbf q}\hat b^{r'\dagger}_{\mathbf l}|0\rangle .
> $$
>
> The operator string: $\hat a^s_{\mathbf p}\hat a^{s'\dagger}_{\mathbf q} = \{\hat a^s_{\mathbf p}, \hat a^{s'\dagger}_{\mathbf q}\} - \hat a^{s'\dagger}_{\mathbf q}\hat a^s_{\mathbf p}$; in the second term $\hat a^s_{\mathbf p}\hat b^{r'\dagger}_{\mathbf l}|0\rangle = -\hat b^{r'\dagger}_{\mathbf l}\hat a^s_{\mathbf p}|0\rangle = 0$. So
>
> $$
> \langle0|\hat b^r_{\mathbf k}\hat a^s_{\mathbf p}\hat a^{s'\dagger}_{\mathbf q}\hat b^{r'\dagger}_{\mathbf l}|0\rangle = (2\pi)^3\delta^{ss'}\delta^3(\mathbf p - \mathbf q)\,\langle0|\hat b^r_{\mathbf k}\hat b^{r'\dagger}_{\mathbf l}|0\rangle = (2\pi)^6\delta^{ss'}\delta^{rr'}\delta^3(\mathbf p - \mathbf q)\delta^3(\mathbf k - \mathbf l) ,
> $$
>
> with sign $+$: the arcs $\hat a_{\mathbf p}$–$\hat a^\dagger_{\mathbf q}$ (positions 2–3) and $\hat b_{\mathbf k}$–$\hat b^\dagger_{\mathbf l}$ (1–4) are nested ([[§C6d.3 Wick's Theorem with Fermions#^lem-c6d-3-3|Lemma §C6d.3.3]]). For the ket $\hat b^\dagger_{\mathbf k}\hat a^\dagger_{\mathbf p}|0\rangle$ (bra $\langle0|\hat a\hat b$) the arcs would cross once: sign $-$. The $\delta^3$'s do the integrals ($\mathbf q = \mathbf p$, $\mathbf l = \mathbf k$), the $(2\pi)^6$ cancel, $\sqrt{2E_{\mathbf p}2E_{\mathbf k}}/\sqrt{2E_{\mathbf q}2E_{\mathbf l}} = 1$ on the support ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1), the Kronecker deltas do the spin sums, and the index $a$ is summed: $\bar u^s(p)v^r(k)\,e^{ip\cdot x}e^{ik\cdot x}$. With Step 2: $\bar u^s(p)v^r(k)\,e^{i(p + k - P)\cdot x}$, the statement.
>
> **Step 5** (the amplitude). By [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]] the first-order term is $-ig\int d^4x$ times this; $\int d^4x\,e^{i(p + k - P)\cdot x} = (2\pi)^4\delta^4(p + k - P)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); stripping the delta ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) gives $i\mathcal M = -ig\,\bar u^s(p)v^r(k)$, as [[§C6d.4 Feynman Rules for Yukawa Theory#^ex-c6d-4-1|Example §C6d.4.1]] found with the contraction rules.
>
> **Step 6** (contrast: $\phi^3$). For $\mathcal L_{\rm int} = -\frac{g}{3!}\phi^3$ ([[§C6a.8 Position-Space Feynman Rules#^mod-c6a-8-2|Model §C6a.8.2]] at $\lambda = 0$) and $\langle\mathbf p_1\mathbf p_2|\hat\phi^3(x)|\mathbf P\rangle$: write $\hat\phi^3 = \hat\phi\hat\phi\hat\phi$ (factors 1, 2, 3). The incoming scalar can be absorbed by the $\hat\phi^+$ of any of the three factors, $\mathbf p_1$ created by the $\hat\phi^-$ of either remaining one, $\mathbf p_2$ by the last: $3\cdot2\cdot1 = 3!$ terms, each $e^{i(p_1 + p_2 - P)\cdot x}$ (the self-contraction of two factors leaves $\langle\mathbf p_1\mathbf p_2|\hat\phi|\mathbf P\rangle = 0$, as in Step 3). So $\langle\mathbf p_1\mathbf p_2|i\hat T^{(1)}|\mathbf P\rangle = -i\frac{g}{3!}\cdot3!\,(2\pi)^4\delta^4 = -ig(2\pi)^4\delta^4$ ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|Example §C6c.4.5]]). The $\frac{1}{3!}$ (and $\frac{1}{4!}$ for $\phi^4$) is a convention chosen to cancel the permutations of identical fields; with $\hat{\bar\psi}$, $\hat\psi$, $\hat\phi$ all different there is nothing to cancel, and writing $\frac{g}{3!}\bar\psi\psi\phi$ would only rescale the coupling (vertex $-ig/6$). General count: $-ig\prod_km_k!$ ([[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]); Yukawa: $\prod_km_k! = 1!\,1!\,1! = 1$.
>
> **What the derivation shows.**
> - The absence of $\frac{1}{3!}$ is a property of the vertex, distinct fields, independent of the diagram it sits in; the absence of symmetry factors in whole diagrams ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]]) follows from the same distinctness.
> - The single fermion sign of the vertex is fixed by the order of the external pair; it is the first instance of [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|Theorem §C6d.3.4]].

^der-c6d-4-2

*Uses:* [[§C6d.2 External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6d.3 Wick's Theorem with Fermions#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-1|Theorem §C6c.4.1]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-2|P6, step 2]]

> [!theorem] Theorem §C6d.4.3: Yukawa Diagrams Have No Symmetry Factors
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] the relabelling group of $n$ vertices is $S_n$ alone, of order $n!$: the three legs $\hat{\bar\psi}$, $\hat\psi$, $\hat\phi$ of a vertex are of three different kinds and "cannot substitute for one another in contractions". The $\frac{1}{n!}$ of the Dyson series is cancelled by the $n!$ ways of relabelling the vertices, with equal values and equal fermion signs, and
>
> $$
> S(D) = 1 \qquad \text{for every diagram } D \text{ each of whose connected pieces contains an external particle or an external field.}
> $$
>
> The vertex-level statement, no $\frac{1}{3!}$ at a single vertex, is [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-2|Theorem §C6d.4.2]]. Vacuum bubbles may have $S > 1$: the second-order bubble with one fermion loop through both vertices and a scalar line between them, and the one with a tadpole loop at each vertex joined by the scalar line, both have $S = 2$ (Yu (7.72)–(7.73): "the $1/2!$ is not cancelled").
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* combinatorics of the Dyson series, every order; the amplitudes of [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-1|Theorem §C6d.4.1]] (connected) always have $S = 1$.
>
> *Source: PHY 513 Lecture 17, slide 18 ("Symmetry factors: none. Fields in $\bar\psi\psi\phi$ cannot substitute for one another in contractions") · PS §4.7, p. 118 ("the $1/n!$ from the Taylor series of the time-ordered exponential is always canceled by the $n!$ ways of interchanging vertices to obtain the same contraction. The diagrams of Yukawa theory never have symmetry factors, since the three fields $(\bar\psi\psi\phi)$ in $H_I$ cannot substitute for one another in contractions") · Yu §7.1, p. 275 (boxed: "$iT^{(n)}$ 中的 $1/n!$ 因子恰好与时空坐标的交换对称性引起的 $n!$ 因子抵消", footnote: "不过，此规律不适用于下文中具有非平庸对称性因子的气泡图"), eqs. (7.72)–(7.73), p. 286 · proof written here with [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]]*

^thm-c6d-4-3

> [!derivation]- Derivation
> **Step 1** (vertex data). In the language of [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]]: kinds $\bar\psi$, $\psi$, $\phi$ with $\psi \smile \bar\psi$, $\phi \smile \phi$ ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-1|Theorem §C6d.3.1]]: $\overbracket{\hat\psi\hat\psi} = \overbracket{\hat{\bar\psi}\hat{\bar\psi}} = \overbracket{\hat\psi\hat\phi} = 0$); one vertex type with three legs of three kinds, $m_{\bar\psi} = m_\psi = m_\phi = 1$. The leg group is trivial, $|H| = 1!\,1!\,1! = 1$, and $|G_n| = n!$ ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 1).
>
> **Step 2** (equal values on an orbit). Relabelling the vertices permutes the packages $\hat{\bar\psi}\hat\psi\hat\phi(x_k)$ inside $T$ and renames the integration variables. The first is free of sign ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], 1: each package holds two fermion fields), the second leaves the integral unchanged. So the value of a contraction pattern, sign included, is constant on its orbit, and by [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 2,
>
> $$
> \frac{1}{n!}\sum_{\text{patterns}}(\text{value}) = \frac{1}{|G_n|}\sum_P f(P) = \sum_D\frac{f(D)}{S(D)} .
> $$
>
> **Step 3** ($S = 1$ with external points). Let $g \in \operatorname{Stab}(P)$. A vertex with a leg joined to an external point is fixed ([[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], 3). If a vertex $v$ is fixed, so are its three legs ($H$ trivial), and for each leg $h$ with partner $h'$ ($\{h, h'\} \in P$): $\{gh, gh'\} = \{h, gh'\} \in P$ forces $gh' = h'$, so the vertex of $h'$ is fixed. Moving along lines, every vertex connected to $v$ is fixed. If every connected piece contains an external point, every vertex is fixed, hence every half-edge: $g = e$, $S = 1$.
>
> **Step 4** (bubbles). At $n = 2$, no external points: (a) one fermion loop through $x_1$, $x_2$ and a scalar line, $P = \{\{\psi_1, \bar\psi_2\}, \{\psi_2, \bar\psi_1\}, \{\phi_1, \phi_2\}\}$; the exchange $1 \leftrightarrow 2$ maps each block to a block of $P$ ($\{\psi_2, \bar\psi_1\}$, $\{\psi_1, \bar\psi_2\}$, $\{\phi_2, \phi_1\}$), so $S = 2$ and the orbit has $2!/2 = 1$ element. (b) Tadpoles $\{\psi_1, \bar\psi_1\}$, $\{\psi_2, \bar\psi_2\}$ and $\{\phi_1, \phi_2\}$: likewise $S = 2$. These are Yu's $iT^{(2)}_{13}$, $iT^{(2)}_{14}$ (Fig. 7.11), whose $\frac{1}{2!}$ survives; as for QED ([[§C6a.9 Symmetry Factors in Practice#^cau-c6a-9-2|§C6a.9, Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points]]).
>
> **What the derivation shows.**
> - Symmetry factors come from leg permutations at a vertex and from automorphisms not pinned by external points; Yukawa theory has no leg permutations, and external particles pin every connected diagram.
> - The fermion sign does not spoil orbit counting because vertices move as even packages.

^der-c6d-4-3

*Uses:* [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]], [[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-1|Theorem §C6d.3.1]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]

*Procedure:* [[P5 Symmetry Factor of a Diagram#^p5-5|P5, step 5]]

> [!remark] Remark: The direction of momentum on fermion lines
> On external lines, as for bosons, the momentum is ingoing for initial and outgoing for final particles: the annihilation operators $\hat a_{\mathbf p}$, $\hat b_{\mathbf p}$ come with $e^{-ip\cdot x}$, the creation operators with $e^{+ip\cdot x}$. On an internal fermion line the momentum must be assigned along the arrow (particle-number flow): the vertex integrals "force $q$ to flow from $y$ to $x$" in $S_F(x - y)$ (Step 5 of [[§C6d.4 Feynman Rules for Yukawa Theory#^der-c6d-4-1|Derivation §C6d.4.1]]). Reversing it changes the numerator, $\slashed q + m \to -\slashed q + m$, since $S_F$ is not even. On boson lines the direction is irrelevant, $D_F(x - y) = D_F(y - x)$. For external antiparticles the momentum runs against the arrow (PS: "it helps to show this explicitly by drawing a second arrow next to the line").
>
> *Source: PS §4.7, pp. 118–119 (the second comment and the example $\langle\mathbf k, \mathbf k'|\int\phi\bar\psi\psi\int\phi\bar\psi\psi|\mathbf p, \mathbf p'\rangle$) · PHY 513 Lecture 17, slide 12 · Yu §7.1, p. 270 (after (7.41): the momentum of a Dirac propagator along the arrow)*

^rem-c6d-4-1

> [!remark] Remark: Dashed and solid
> PS, the lecture and the user's notes draw the scalar dashed and the fermion solid with an arrow. In QED there are no scalars: the fermions are "the heroes of QED", and the scalar is "a little bit exotic … a toy", so it gets the dashed line. "That's just a historic sort of remark": a convention, not a rule (Yu also uses dashed lines for real scalars, Fig. 7.1).
>
> *Source: PHY 513 Lecture 17, transcript (about 50 min) · the user's PHY 513 notes, Lecture 17 update, §17.4, paragraph "Dashed and solid" · PS §4.7, p. 118 ("We denote scalar particles by dashed lines, and fermions by solid lines")*

^rem-c6d-4-2

## Example

> [!example] Example §C6d.4.1: φ → f f̄ at First Order
> ![[ph-qft-c6d-4-1.svg]]
>
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with $m_\phi > 2m$, a scalar of momentum $k$ decays into a fermion $(p, s)$ and an antifermion $(q, s')$, final state $|\mathbf p, s; \mathbf q, s'\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf q}}\,\hat a^{s\dagger}_{\mathbf p}\hat b^{s'\dagger}_{\mathbf q}|0\rangle$ ([[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). At first order
>
> $$
> i\mathcal M(\phi \to f\bar f) = -ig\;\bar u^s(p)\,v^{s'}(q) ,
> $$
>
> one diagram, the chain $\bar uv$ read against the arrow. Kinematically allowed iff $m_\phi > 2m$.
>
> **Step 1** (the matrix element). By [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], $\langle\mathbf p, s; \mathbf q, s'|i\hat T^{(1)}|\mathbf k\rangle = -ig\int d^4x\,\langle\mathbf p, s; \mathbf q, s'|\hat{\bar\psi}_a\hat\psi_a\hat\phi(x)|\mathbf k\rangle$, the bra $\sqrt{2E_{\mathbf p}2E_{\mathbf q}}\langle0|\hat b^{s'}_{\mathbf q}\hat a^s_{\mathbf p}$.
>
> **Step 2** (who contracts with whom). The scalar is absorbed by $\hat\phi^+$: $\hat\phi^+(x)|\mathbf k\rangle = e^{-ik\cdot x}|0\rangle$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]). The outgoing fermion needs an $\hat a^\dagger$: $\hat{\bar\psi}^-$; the outgoing antifermion needs a $\hat b^\dagger$: $\hat\psi^-$ ([[§C6d.2 External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). The fermion string is $\langle0|\hat b_{\mathbf q}\hat a_{\mathbf p}\,\hat{\bar\psi}_a\hat\psi_a|0\rangle$ with arcs $\hat a_{\mathbf p}$–$\hat{\bar\psi}$ (positions 2–3) inside $\hat b_{\mathbf q}$–$\hat\psi$ (1–4): no crossing, sign $+$ ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|Theorem §C6d.3.4]]).
>
> **Step 3** (values). $\sqrt{2E_{\mathbf p}}\langle0|\hat a^s_{\mathbf p}\hat{\bar\psi}_a(x)|0\rangle = \bar u^s_a(p)e^{ip\cdot x}$ and $\sqrt{2E_{\mathbf q}}\langle0|\hat b^{s'}_{\mathbf q}\hat\psi_a(x)|0\rangle = v^{s'}_a(q)e^{iq\cdot x}$ (Theorem §C6d.2.1); summing over $a$,
>
> $$
> \langle\mathbf p, s; \mathbf q, s'|i\hat T^{(1)}|\mathbf k\rangle = -ig\,\bar u^s(p)v^{s'}(q)\int d^4x\,e^{i(p + q - k)\cdot x} = -ig\,\bar u^s(p)v^{s'}(q)\,(2\pi)^4\delta^4(k - p - q)
> $$
>
> ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); stripping the delta ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]) gives the statement (every one of the eight frequency terms written out: [[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-2|Theorem §C6d.4.2]]). By the rules ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-1|Theorem §C6d.4.1]]) directly: vertex $-ig$, external $\bar u^s(p)$ (outgoing fermion, the arrow's head) and $v^{s'}(q)$ (outgoing antifermion, the arrow's tail), scalar $1$.
>
> **Step 4** (kinematics). In the rest frame of the scalar, $k = (m_\phi, \mathbf 0)$, conservation gives $\mathbf q = -\mathbf p$ and $m_\phi = 2\sqrt{\mathbf p^2 + m^2} \ge 2m$: allowed iff $m_\phi > 2m$ (at $m_\phi = 2m$ only $\mathbf p = 0$, of measure zero), [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-2|Theorem §C6c.4.2]], 2. Of the ten first-order processes of Yukawa theory (Yu Fig. 7.1–7.2) only this one and its inverse $f\bar f \to \phi$ survive ([[§C6c.4 First Order꞉ Enumerate, then Filter#^ex-c6c-4-5|§C6c.4, Example §C6c.4.5]], Yu p. 272).
>
> **Step 5** (Yu's sign). Yu (7.34), (7.44) find $i\mathcal M = +i\kappa\,\bar u(p, \lambda)v(q, \lambda')$ with his bra $\langle\mathbf p^+, \lambda; \mathbf q^-, \lambda'| \propto \langle0|\hat a_{\mathbf p}\hat b_{\mathbf q}$ (7.12), which is $-1$ times ours ($\hat a\hat b = -\hat b\hat a$): the same amplitude up to the overall sign of the state, $|\mathcal M|^2$ equal ([[§C6d.4 Feynman Rules for Yukawa Theory#^cau-c6d-4-1|Caution: Yu's (7.23)–(7.24) and his order of the bra]]).
>
> *Source: Yu §7.1, p. 272 ($\phi \to \psi\bar\psi$ allowed for $m_\phi > 2m_\psi$), eqs. (7.34), (7.44), Fig. 7.1(b) · the user's PHY 513 notes, Lecture 17 update, §17.2, Figure "yukvertex" (c), paragraph "Correspondence with Yu" · PHY 513 Lecture 17, transcript ("what really happened was scalar coming in, particle, antiparticle being created") · computed here in the vault's conventions*

^ex-c6d-4-1

> [!caution] Caution: Yu's (7.23)–(7.24) and his order of the bra
> The user's notes (paragraph "Correspondence with Yu") cite Yu (7.23)–(7.24), $i\mathcal M = -i\kappa\,\bar vu$, as "the first-order amplitude for a scalar decaying into a fermion pair". On Yu's pages (PDF pp. 272–273) (7.23)–(7.24) are the first case of Fig. 7.1(a): a fermion, an antifermion and a scalar all **incoming**, final state the vacuum, $\langle0|iT_1^{(1)}|\mathbf p^+, \lambda; \mathbf q^-, \lambda'; \mathbf k\rangle$, kinematically forbidden; $\bar v(q)u(p)$ is the chain of an incoming pair. The decay $\phi \to \psi\bar\psi$ is Fig. 7.1(b), eq. (7.34), with $i\mathcal M = +i\kappa\,\bar u(p, \lambda)v(q, \lambda')$ (7.44): an outgoing pair gives $\bar u\cdots v$. Yu's $+$ against the vault's $-ig\,\bar uv$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^ex-c6d-4-1|Example §C6d.4.1]]) comes from his special convention (7.12): his bras keep the order of the labels, $\langle\mathbf p^+; \mathbf q^-| \propto \langle0|\hat a_{\mathbf p}\hat b_{\mathbf q}$, which "differs from the usual definition by a minus sign" (Yu p. 262), while PS (4.118) and [[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] take the Hermitian conjugate. For two identical fermions the same convention flips the overall sign of $ff \to ff$ (Yu (7.82) against PS (4.119)).
>
> *Source: Yu §7.1, pp. 262, 264–265, 268, 272, eqs. (7.11)–(7.12), (7.23)–(7.24), (7.34), (7.44), (7.82) (page images checked) · the user's PHY 513 notes, Lecture 17 update, "Correspondence with Yu" · recorded in `qft-C/ERRATA.md`*

^cau-c6d-4-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give the momentum deltas; for $S_F$ they fix the direction of $q$.
> - [[§CA.8 Splitting Pairings and the Exponential Formula#^def-ca-8-2|Def. §CA.8.2]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-4|Theorem §CA.8.4]] — the relabelling group with leg kinds and orbit–stabilizer, behind $S = 1$.

> [!remark]- Connections
> - The scalar rules are the special case without fermion lines; the vertex rule is the polynomial one with $\prod m! = 1$ — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]].
> - The absence of symmetry factors is the QED statement of slide 18 of Lecture 14, for the same reason: a vertex with three legs of three kinds; and with the same exception, vacuum bubbles — [[§C6a.9 Symmetry Factors in Practice#^cau-c6a-9-2|§C6a.9, Caution: "In QED the symmetry factor is always S = 1" holds for diagrams with external points]].
> - The decay rate of $\phi \to f\bar f$ needs $\sum_{s, s'}|\bar u^sv^{s'}|^2 = \operatorname{tr}[(\slashed p + m)(\slashed q - m)] = 4(p\cdot q - m^2)$ (spin sums and traces; Yu (7.46)–(7.58) obtains $\Gamma = \frac{g^2m_\phi}{8\pi}(1 - 4m^2/m_\phi^2)^{3/2}$) — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]], [[§C5a.14 Gamma-Matrix Technology|§C5a.14]], [[§C6b.9 Decay Rates and Widths|§C6b.9]]; processes follow the rules (C8 Quantum electrodynamics, planned).
> - The QED rules replace the scalar by the photon: vertex $-ie\gamma^\mu$, propagator $-ig_{\mu\nu}/(q^2 + i\varepsilon)$, external polarization vectors (PS §4.8, p. 123) — C6d, QED rules (planned); the vector propagator — [[§C4.11 Vector-Field Propagators|§C4.11]].
