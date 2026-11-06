---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.5 Second Order]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.7★ The Yukawa Potential]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 15–18 and 23, and transcript · the user's PHY 513 notes, Lecture 17 update, §17.4 (paragraph "Dashed and solid", Figure "yukprops"), §17.5 (Principle "Feynman rules for $i\mathcal M$ in Yukawa theory (momentum space)"), §17.7 (Principle "Feynman rules with fermions"), paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, p. 118 (rules 1–6) and pp. 118–120 (the comments) · Yu Zhao-Huan, 量子场论讲义, §7.1, eqs. (7.11)–(7.12), (7.23)–(7.24), (7.34), (7.40)–(7.41), (7.44), pp. 262–272, p. 275 (the $1/n!$ rule and its footnote); §7.2, rules 1–12 (pp. 287–288), eqs. (7.104)–(7.107) and the paragraphs on relative signs (pp. 287–289).*

[[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]] stated the rules for $i\mathcal M$ in scalar theories. With [[§C6d.1 Yukawa Theory|§C6d.1]]–[[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule|§C6d.3]] the same derivation runs for Yukawa theory, and this section collects the result ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]], slides 16–18, PS p. 118). The line factors come from the free Dirac field and only the vertex from $\mathcal L_{\rm int}$ ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|Theorem §C6d.6.1]]). The statements the rules rest on are proved where they first appear: the vertex carries no $\frac{1}{3!}$ ([[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]], from the user's discussion with Larsen), there are no symmetry factors ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]], slide 18), a closed fermion loop gives $-1$ and a trace ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]), the relative signs come from the contractions ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]; [[§C6d.6 Momentum-Space Feynman Rules#^cau-c6d-6-1|Caution: Relative signs still need the contractions]]), and the momentum on a fermion line runs along its arrow ([[§C6d.6 Momentum-Space Feynman Rules#^rem-c6d-6-1|Remark: The direction of momentum on fermion lines]]). The first application is the first-order decay $\phi \to f\bar f$ ([[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]), the one first-order process of Yukawa theory that kinematics allows besides its inverse (Yu p. 272). The QED rules of Lecture 18 join this chapter after this section. Yu reads the same rules off first-order $T$-matrix elements in §7.1 (here [[§C6d.4 First Order|§C6d.4]]–[[§C6d.5 Second Order|§C6d.5]]) and lists them in §7.2 (rules 1–12).

**Setup.** As in [[§C6c.6 Feynman Rules for Amplitudes|§C6c.6]], for [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]: free relativistic states over $|0\rangle$ stand for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); exact at the lowest order of a process, beyond it $\sqrt Z$ per external line and the physical masses ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). States are ordered as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]].

## The rules

> [!theorem] Theorem §C6d.6.1: The Fermion Line Factors Come from the Free Dirac Field; Only the Vertex Is Theory-Specific
> In the Feynman rules of a theory with Dirac fermions and an interaction without derivatives:
> 1. the **external fermion lines** $u$, $\bar u$, $\bar v$, $v$ are the contractions of the free Dirac field with free one-particle states ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]; the frequency parts of [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]);
> 2. the **internal fermion line** is the contraction of two free fields, $S_F$, in momentum space $\frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}$ with $q$ along the arrow ([[§C6d.4 First Order#^def-c6d-4-1|Def. §C6d.4.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]);
> 3. the reading against the arrow ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]), the sign from the contractions ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]), the $-1$ and trace of a closed loop ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]), momentum conservation and the loop integrals ([[§C6d.4 First Order#^def-c6d-4-3|Def. §C6d.4.3]]) follow from Wick's theorem with fermions and from the free fields, not from $\mathcal L_{\rm int}$;
> 4. only the **vertex** depends on the interaction: $i\mathcal L_{\rm int}$ with the fields stripped ([[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]]), $-ig$ for Yukawa theory, $-ie\gamma^\mu$ for QED.
>
> So the rules of a new theory with the same fields need only its vertices; Yu's rules 1–8 and 10–12 hold for every such theory, rule 9 is the Yukawa vertex.
>
> *Equivalently,* the scalar case is [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]]: external line $1$, internal line $\frac{i}{q^2 - m^2 + i\varepsilon}$, only the vertex from $\mathcal L_{\rm int}$; fermions add items 1–2 and the signs of item 3.
>
> *Proof:* items 1–2 are the contractions of [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]] and [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|Theorem §C6d.3.1]], which involve only the free fields of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; item 3 is [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]] and Step 5 of [[§C6d.6 Momentum-Space Feynman Rules#^der-c6d-6-2|Derivation §C6d.6.2]], none of which uses the form of $\hat H_I$ beyond its being built of packages ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]); item 4 is [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] and any interaction of Dirac fermions without derivatives; *applies:* every order, free relativistic states over $|0\rangle$ as in [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]; beyond lowest order the external lines carry $\sqrt Z$ ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]).
>
> *Source: Yu §7.2, p. 288 ("除了关于顶点的第 9 条规则具有 Yukawa 相互作用特有的形式之外，其它规则具有一般性"); §7.3, p. 292 ("外线和内线的 Feynman 规则由拉氏量的自由部分决定，因而不依赖于相互作用理论，具有普遍性") · PHY 513 Lecture 17, transcript ("Fermions give nothing new. Do it for the scalars") · PS §4.7, p. 118 · stated here from [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-4|Theorem §C6d.1.4]] and the derivation of [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]*

^thm-c6d-6-1

> [!theorem] Theorem §C6d.6.2: Feynman Rules for iℳ in Yukawa Theory
> In [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]], $i\mathcal M\,(2\pi)^4\delta^4(\sum p_{\rm in} - \sum p_{\rm out})$ is the sum of all connected, amputated diagrams ([[§C6c.6 Feynman Rules for Amplitudes#^def-c6c-6-1|Def. §C6c.6.1]]) built from vertices with one dashed and two solid lines, one fermion arrow in and one out ([[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]]), each diagram the product of
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
> 1. each fermion line is written **against its arrow**, a row times matrices times a column, so that it is a number ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]);
> 2. each closed fermion loop gives a factor $-1$ and a trace ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]);
> 3. the vertex carries no combinatorial factor, $-ig$ and not $-ig/3!$ ([[§C6d.4 First Order#^thm-c6d-4-4|Theorem §C6d.4.4]]), and there are **no symmetry factors**, $S = 1$ ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]);
> 4. each diagram carries the **sign** $(-1)^{\#\text{crossings}}$ of its contraction pattern with the external states ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]); the relative signs between diagrams are physical, the overall sign depends on the order of the external states ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]).
>
> In momentum space the overall $(2\pi)^4\delta^4$ is stripped. *Equivalence:* for the scalar lines and vertices these are the rules of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]] with the vertex $-ig$ of a monomial with three distinct legs; what fermions add is the propagator $S_F$, the external spinors, items 1, 2 and 4, and $S = 1$ always. Conversely, deleting the fermion items leaves Theorem §C6c.6.3.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* with the prescription of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]: at the lowest order of a process exact, as [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-2|Theorem §C6c.6.2]]; loop corrections on internal lines by these rules; corrections on external legs excluded by amputation, with their $\sqrt Z$ and the physical masses deferred (second semester).
>
> *Source: PHY 513 Lecture 17, slide 16 ("Interaction at nth order: $\frac{1}{n!}T\bigl(-ig\int d^4x\,\bar\psi_I\psi_I\phi_I\bigr)^n$. Vertex $= -ig$. Propagators: … $\frac{i}{q^2 - m^2_\phi + i\epsilon}$ … $\frac{i(\slashed p + m)}{p^2 - m^2 + i\epsilon}$"), slide 12 (external lines), slide 18 ("Momentum conserved at vertices. Loop momenta … should be integrated. Symmetry factors: none … All diagrams must be connected and amputated. Sign of amplitude: determine from explicit contractions if it is needed"), slide 23 (loops) · the user's PHY 513 notes, Lecture 17 update, §17.5, Principle "Feynman rules for $i\mathcal M$ in Yukawa theory (momentum space)" (a principle there, a theorem here because it is derived), §17.7, Principle "Feynman rules with fermions" · PS §4.7, p. 118 (rules 1–6: "Figure out the overall sign of the diagram"), pp. 118–120 · Yu §7.2, rules 1–12 (pp. 287–288); position space: Yu (7.25)–(7.28), (7.31)–(7.33), (7.40)–(7.41) · proof written here from [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]]*

^thm-c6d-6-2

> [!derivation]- Derivation
> **Step 1** (the matrix element at order $n$). By Dyson's formula, valid with fermions ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]), and [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]],
>
> $$
> \langle f|\hat S|i\rangle^{(n)} = \frac{(-ig)^n}{n!}\int d^4x_1\cdots d^4x_n\;{}_0\langle f|\,T\bigl\{\hat{\bar\psi}\hat\psi\hat\phi(x_1)\cdots\hat{\bar\psi}\hat\psi\hat\phi(x_n)\bigr\}\,|i\rangle_0 .
> $$
>
> **Step 2** (full contractions). Wick's theorem with fermions ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]]) turns $T$ into normal-ordered products and contractions; between the states only the terms in which every remaining field is contracted with an external particle survive (the argument of [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]]: a $\hat\Phi^+$ moved to the right must meet a creation operator of $|i\rangle$, a $\hat\Phi^-$ an annihilation operator of $\langle f|$). The terms that belong to $i\hat T$ are the fully connected, amputated ones ([[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]]; their proofs move only whole packages and is unchanged by [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]).
>
> **Step 3** (values and signs). Each term is $(-1)^{\#\text{crossings}}$ times the product of the pair values ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]): $D_F$ and $S_F$ for internal lines, $e^{\mp ip\cdot x}$ for external scalars, the spinors times plane waves of [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]] for external fermions; the spinor indices are summed along each line (item 1, [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]), closed lines give $-\operatorname{tr}$ (item 2).
>
> **Step 4** ($\frac{1}{n!}$). The $n!$ relabellings of the vertices give terms with equal values and equal signs, and a diagram whose pieces all touch an external particle arises from exactly $n!$ of them ([[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]]): the prefactor becomes $(-ig)^n$, one $-ig\int d^4x$ per vertex, $S = 1$.
>
> **Step 5** (momentum space). Insert $D_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2 - m_\phi^2 + i\varepsilon}e^{-iq\cdot(x - y)}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]) and $S_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}e^{-iq\cdot(x - y)}$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], stated there; its compact form $i/(\slashed q - m + i\varepsilon)$ is [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-8|Theorem §C5b.8.8]]). Each vertex now carries three plane waves, and $\int d^4x\,e^{-i(\sum q_{\rm in})\cdot x} = (2\pi)^4\delta^4(\sum q_{\rm in})$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]), with $e^{-iq\cdot x}$ counted as $q$ flowing into $x$. For $S_F(x - y)$ the factor $e^{-iq\cdot x}$ sits at $x$ (the $\hat\psi$ end) and $e^{+iq\cdot y}$ at $y$ (the $\hat{\bar\psi}$ end): $q$ flows from $y$ to $x$, along the arrow. The internal momenta are fixed by the deltas up to $L$ loop integrals; the last delta is the overall one, stripped by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] (Steps 5–6 of [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]]).
>
> **Step 6** (checks). First order, $\phi \to f\bar f$: $i\mathcal M = -ig\,\bar u^s(p)v^{s'}(q)$ ([[§C6d.4 First Order#^ex-c6d-4-1|Example §C6d.4.1]]). Second order, $ff \to ff$: two diagrams with a relative minus sign ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], PS (4.119)).
>
> **What the derivation shows.**
> - Nothing about the origin of the rules is new for fermions; the new items are bookkeeping of spinor indices and signs.
> - The amplitude is a number because each fermion line is a closed chain of spinor indices, and its sign is fixed only relative to the order of the external states.

^der-c6d-6-2

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]], [[§C6c.3 Wick's Theorem between Particle States#^thm-c6c-3-1|Theorem §C6c.3.1]], [[§C6c.4 First Order꞉ Enumerate, then Filter#^thm-c6c-4-6|Theorem §C6c.4.6]], [[§C6c.5 Second Order꞉ Loops, Amputation and Symmetry Factors#^thm-c6c-5-3|Theorem §C6c.5.3]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]], [[§C6d.4 First Order#^thm-c6d-4-7|Theorem §C6d.4.7]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-8|Theorem §C5b.8.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6c.6 Feynman Rules for Amplitudes#^der-c6c-6-3|Derivation §C6c.6.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!caution] Caution: Relative signs still need the contractions
> The momentum-space rules ([[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]) give each diagram's value up to a sign, and the diagram itself does not show that sign: for $f\bar f \to f\bar f$ the $s$- and $t$-channel diagrams look alike, yet enter with $-$ ([[§C6d.5 Second Order#^ex-c6d-5-1|Example §C6d.5.1]]); for $f\bar f \to \phi\phi$ with $+$ ([[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]). When a process has several diagrams with fermion lines, write the contractions of each, with the fields in the order of $\mathcal L_{\rm int}$, untangle the lines and count the crossings ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]]), or apply [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]. Each fermion line is translated whole, against its arrow, before the next; the order in which the lines are translated does not matter (Yu p. 288). A single diagram needs no care: its overall sign does not enter $|\mathcal M|^2$ ([[§C6d.5 Second Order#^thm-c6d-5-5|Theorem §C6d.5.5]]); Yu's (7.104) by the rules and his (7.44) by contractions differ by exactly such an overall sign.
>
> *Source: Yu §7.2, p. 287 ("不过，当同一过程存在多个子图且涉及费米子算符时，需要回到带着缩并的表达式，通过调换场算符将纠缠的缩并线解开，以确定各个子图之间的相对符号"), p. 288 ("应将一条连续费米子线完整地翻译成代数表达式之后，再处理下一条，而各条连续费米子线的翻译次序则是无所谓的"; (7.104) "与 (7.44) 式整体相差一个负号"), p. 289, eqs. (7.105)–(7.106) ("从 Feynman 图本身看不出它们之间的相对符号") · PHY 513 Lecture 17, slide 18 ("Sign of amplitude: determine from explicit contractions if it is needed") · PS §4.7, p. 118 (rule 6: "Figure out the overall sign of the diagram")*

^cau-c6d-6-1

> [!remark] Remark: The direction of momentum on fermion lines
> On external lines, as for bosons, the momentum is ingoing for initial and outgoing for final particles: the annihilation operators $\hat a_{\mathbf p}$, $\hat b_{\mathbf p}$ come with $e^{-ip\cdot x}$, the creation operators with $e^{+ip\cdot x}$. On an internal fermion line the momentum must be assigned along the arrow (particle-number flow): the vertex integrals "force $q$ to flow from $y$ to $x$" in $S_F(x - y)$ (Step 5 of [[§C6d.6 Momentum-Space Feynman Rules#^der-c6d-6-2|Derivation §C6d.6.2]]). Reversing it changes the numerator, $\slashed q + m \to -\slashed q + m$, since $S_F$ is not even. On boson lines the direction is irrelevant, $D_F(x - y) = D_F(y - x)$. For external antiparticles the momentum runs against the arrow (PS: "it helps to show this explicitly by drawing a second arrow next to the line").
>
> *Source: PS §4.7, pp. 118–119 (the second comment and the example $\langle\mathbf k, \mathbf k'|\int\phi\bar\psi\psi\int\phi\bar\psi\psi|\mathbf p, \mathbf p'\rangle$) · PHY 513 Lecture 17, slide 12 · Yu §7.1, p. 270 (after (7.41): the momentum of a Dirac propagator along the arrow)*

^rem-c6d-6-1

> [!remark] Remark: Dashed and solid
> PS, the lecture and the user's notes draw the scalar dashed and the fermion solid with an arrow. In QED there are no scalars: the fermions are the central fields, and the scalar is an exotic toy field, so it gets the dashed line. This is a historical convention, not a rule (Yu also uses dashed lines for real scalars, Fig. 7.1).
>
> *Source: PHY 513 Lecture 17, transcript (about 50 min) · the user's PHY 513 notes, Lecture 17 update, §17.4, paragraph "Dashed and solid" · PS §4.7, p. 118 ("We denote scalar particles by dashed lines, and fermions by solid lines")*

^rem-c6d-6-2

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the vertex integrals give the momentum deltas; for $S_F$ they fix the direction of $q$.

> [!remark]- Connections
> - The scalar rules are the special case without fermion lines; the vertex rule is the polynomial one with $\prod m! = 1$ — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-3|Theorem §C6c.6.3]], [[§C6a.12 Feynman Rules for Polynomial Interactions#^thm-c6a-12-2|Theorem §C6a.12.2]].
> - The QED rules replace the scalar by the photon: vertex $-ie\gamma^\mu$, propagator $-ig_{\mu\nu}/(q^2 + i\varepsilon)$, external polarization vectors (PS §4.8, p. 123) — C6d, QED rules (planned); the vector propagator — [[§C4.11 Vector-Field Propagators|§C4.11]].
> - Every rule except the vertex comes from the free fields, for scalars and fermions alike — [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-1|Theorem §C6d.6.1]], [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-1|Theorem §C6c.6.1]].
