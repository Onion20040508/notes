---
type: draft
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.0
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
> [!warning] Draft for review — not yet part of the chapter
> Planned overview §C6a.0 for the C6 restructure (plan `qft-C/C6-RESTRUCTURE-PLAN.md`, §2). Every link points to the current notes. Nothing in C6a or C6b has been changed yet.

*Sources: PHY 513 Lectures 13–15 (Larsen, 14, 26 and 28 Oct 2026) · the user's PHY 513 notes, Ch. 13–15 (Ch. 15, Figure "bigpicture" and Principle "Dynamics versus kinematics") · PHY 513, Problem Set 8 (the user's solution, submitted 2026-10-30) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.1–§4.5 · Yu Zhao-Huan, 量子场论讲义, §6.1–§6.3, §6.5, §10.3–§10.6.*

C6a and C6b answer one question: **given a Lagrangian with an interaction, which number do we compute, and how?** There are two kinds of target. A **correlation function** $\langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_n)\}|\Omega\rangle$ is what the Dyson series and Wick's theorem produce directly (C6a). An **$S$-matrix element** $\langle f|\hat S|i\rangle$ is what an experiment needs, through $|\mathcal M|^2$, $d\sigma$ and $d\Gamma$ (C6b). Both come from the same machinery, the interaction-picture evolution operator. Amputation is the bridge from the first to the second ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]; LSZ in Lecture 16). This note lays out the chain in formulas, lists every object with its normalization and its use, and says which section answers which question.

*Conventions* ([[Larsen PHY 513]]): $\phi^4$ theory, $\mathcal L_{\rm int} = -\frac{\lambda}{4!}\phi^4$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]), as the running example; relativistically normalized states $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) except where a row of the table says otherwise; $T$ is half the time interval $[-T, T]$, $T\{\cdots\}$ is time ordering, and $\hat T$ is the $T$-matrix.

## The pipeline

![[ph-qft-c6a-0-1.svg]]
*The chain of C6a and C6b. The common trunk (1–3) builds the evolution operator from the Lagrangian. Branch 1 (blue, 4–7) turns it into correlation functions. Branch 2 (orange, 8–9) turns it into $S$-matrix elements and the amplitude $\mathcal M$. Green boxes are end products: correlators (7), observables (11), and the source model's particle-number probabilities (12). The red arrow (10) is amputation, which reads $i\mathcal M$ off a correlator. The numbers match the list below. Added figure.*

**Common trunk.**

1. **Lagrangian → Hamiltonian** ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]], [[§C6a.1 From Free to Interacting Fields#^def-c6a-1-1|Def. §C6a.1.1]]). Without derivatives in $\mathcal L_{\rm int}$,
$$
\mathcal H_{\rm int} = -\mathcal L_{\rm int} = \frac{\lambda}{4!}\phi^4 , \qquad \hat H = \hat H_0 + \hat H_{\rm int} , \qquad \hat H_{\rm int} = \int d^3x\,\frac{\lambda}{4!}\,\hat\phi_S(\mathbf x)^4 .
$$
2. **Interaction picture** ([[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-6|Theorem §C6a.2.6]]). The interaction, evaluated on the free field $\hat\phi_I$ ([[§C6a.2 The Interaction Picture#^thm-c6a-2-1|Theorem §C6a.2.1]]):
$$
\hat H_I(t) = e^{i\hat H_0t}\,\hat H_{\rm int}\,e^{-i\hat H_0t} = \int d^3x\,\frac{\lambda}{4!}\,\hat\phi_I(t, \mathbf x)^4 .
$$
3. **Evolution operator, Dyson series** ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-2|Def. §C6a.3.2]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-8|Theorem §C6a.3.8]], series [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]):
$$
U(t, t') = e^{i\hat H_0t}\,e^{-i\hat H(t - t')}\,e^{-i\hat H_0t'} = T\Bigl\{\exp\Bigl[-i\int_{t'}^tdt''\,\hat H_I(t'')\Bigr]\Bigr\} = \sum_{n=0}^\infty\frac{(-i)^n}{n!}\int_{t'}^tdt_1\cdots\int_{t'}^tdt_n\,T\{\hat H_I(t_1)\cdots\hat H_I(t_n)\} .
$$

**Branch 1: correlation functions (C6a).**

4. **Master formula** ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]]). The interacting vacuum $|\Omega\rangle$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]) is projected out of $|0\rangle$ by the tilted limit:
$$
\langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_n)\}|\Omega\rangle = \lim_{T\to\infty(1 - i\varepsilon)}\frac{\langle0|\,T\bigl\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_n)\exp\bigl[-i\int_{-T}^Tdt\,\hat H_I(t)\bigr]\bigr\}\,|0\rangle}{\langle0|\,T\bigl\{\exp\bigl[-i\int_{-T}^Tdt\,\hat H_I(t)\bigr]\bigr\}\,|0\rangle} .
$$
5. **Wick's theorem** ([[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]]; contraction [[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]). Each term of the expanded numerator is a free vacuum value:
$$
\langle0|T\{\hat\phi_1\cdots\hat\phi_n\}|0\rangle = \sum_{\text{pairings }P}\;\prod_{\{i,j\}\in P}D_F(x_i - x_j) , \qquad D_F(x - y) = \langle0|T\{\hat\phi_I(x)\hat\phi_I(y)\}|0\rangle .
$$
6. **Diagrams and rules** ([[§C6a.7 Feynman Diagrams for Correlation Functions#^def-c6a-7-1|Def. §C6a.7.1]], [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1|Theorem §C6a.8.1]], [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-2|Theorem §C6a.8.2]], [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2|Theorem §C6a.10.2]]). Pairings that draw the same diagram $D$ are collected:
$$
\frac{1}{n!}\Bigl(\frac{-i\lambda}{4!}\Bigr)^n\int\prod_{v}d^4z_v\,\langle0|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_r)\,\hat\phi_I(z_1)^4\cdots\hat\phi_I(z_n)^4\}|0\rangle = \sum_D\frac{(-i\lambda)^n}{S(D)}\int\prod_vd^4z_v\prod_{\text{lines of }D}D_F .
$$
7. **Bubbles cancel** ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-2|Theorem §C6a.11.2]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6|Theorem §C6a.11.6]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5|Theorem §C6a.11.5]]):
$$
\langle0|T\Bigl\{\exp\Bigl[-i\int_{-T}^T\hat H_I\Bigr]\Bigr\}|0\rangle = \exp\Bigl(\sum_iV_i\Bigr) , \qquad \langle\Omega|T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_r)\}|\Omega\rangle = \sum\bigl(\text{diagrams attached to }x_1, \dots, x_r\bigr) .
$$

**Branch 2: $S$-matrix elements and observables (C6b).**

8. **$S$-matrix** ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]]). The same evolution operator is taken between particle states:
$$
\langle f|\hat S|i\rangle = \lim_{T\to\infty}\langle f|e^{-i\hat H\,2T}|i\rangle , \qquad \langle f|U(T, -T)|i\rangle = e^{i(E_f + E_i)T}\,\langle f|e^{-i\hat H\,2T}|i\rangle \quad (|i\rangle, |f\rangle \text{ eigenstates of } \hat H_0) .
$$
9. **Remove "nothing happened" and $\delta^4$** ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-2|Theorem §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]):
$$
\hat S = \mathbb 1 + i\hat T , \qquad \langle f|i\hat T|i\rangle = (2\pi)^4\delta^4\Bigl(\sum_{\rm in}p - \sum_{\rm out}p\Bigr)\,i\mathcal M .
$$
10. **Bridge: amputation** ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]], [[§C6b.8 Amplitudes from Correlation Functions#^def-c6b-8-1|Def. §C6b.8.1]], vertex factors [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-3|Theorem §C6b.8.3]]). At lowest order,
$$
i\mathcal M = \frac{\text{fully connected diagrams of the momentum-space correlator}}{\prod_{\text{external}}\tilde D_F(p)\cdot(2\pi)^4\delta^4(\cdots)} , \qquad \phi^4:\ i\mathcal M = -i\lambda + O(\lambda^2) .
$$
The second route to $i\mathcal M$ skips the correlator. It contracts the fields of the Dyson series directly with the external states: $\langle\mathbf p|\hat\phi_I(x)|0\rangle = e^{ip\cdot x}$, [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]]. Problem Set 8, Problem 4 takes this route ([[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1|Example §C6b.7.1]]).
11. **Observables** ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]], [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^def-c6b-6-1|Def. §C6b.6.1]], [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4|Theorem §C6b.7.4]]; where each factor comes from: [[§C6b.2 Cross Section — opening rewrite (draft)|draft opening of §C6b.2]]):
$$
d\sigma = \frac{|\mathcal M|^2\,d\Pi_n}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|} , \qquad d\Gamma = \frac{|\mathcal M|^2\,d\Pi_n}{2m_A} , \qquad d\Pi_n = \prod_{j=1}^n\frac{d^3p_j}{(2\pi)^32E_j}\,(2\pi)^4\delta^4\Bigl(P - \sum_jp_j\Bigr) .
$$
12. **Source model** ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-1|Theorem §C6b.9.1]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7|Theorem §C6b.9.7]]). The interaction is a c-number source, $\hat H_I(t) = -\int d^3x\,j(t, \mathbf x)\,\hat\phi_I(t, \mathbf x)$, and the in- and out-vacuum is $|0\rangle$:
$$
\mathcal A(\mathbf k_1, \dots, \mathbf k_n) = \langle\mathbf k_1\cdots\mathbf k_n|\,T\Bigl\{\exp\Bigl[i\int d^4x\,j(x)\,\hat\phi_I(x)\Bigr]\Bigr\}|0\rangle , \qquad P(n) = \frac{1}{n!}\int\prod_i\frac{d^3k_i}{(2\pi)^3}\,|\mathcal A|^2 = \frac{\lambda^n}{n!}\,e^{-\lambda} .
$$

## The objects

One row per object. "States" gives the normalization the formula assumes; mixing two normalizations costs a factor $2E$ per particle ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^cau-c6b-9-1|§C6b.9, Caution: Two normalizations of one-particle states]]).

| object | definition | states and normalization | measurable? | home | worked in |
|---|---|---|---|---|---|
| free vacuum value | $\langle0\vert T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_n)\}\vert0\rangle = \sum_P\prod D_F(x_i - x_j)$ | free vacuum, $\hat H_0\vert0\rangle = 0$, $\langle0\vert0\rangle = 1$; free fields $\hat\phi_I$ | no: the building block of every Dyson term | [[§C6a.2 The Interaction Picture#^thm-c6a-2-3\|Theorem §C6a.2.3]], [[§C6a.6 Wick's Theorem#^thm-c6a-6-3\|Theorem §C6a.6.3]] | Lecture 14, slides 9–10, 13 ([[§C6a.6 Wick's Theorem#^ex-c6a-6-2\|Example §C6a.6.2]], [[§C6a.7 Feynman Diagrams for Correlation Functions#^ex-c6a-7-1\|Example §C6a.7.1]]); PS8 P3(b), $D_F$ in $\mathcal A_2$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-2\|Theorem §C6b.9.2]]) |
| interacting correlator | $\langle\Omega\vert T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_n)\}\vert\Omega\rangle$ = master-formula ratio = sum of diagrams attached to $x_1, \dots, x_n$ | interacting vacuum, $\langle\Omega\vert\Omega\rangle = 1$; Heisenberg fields | not in a scattering experiment: a Green's (response) function ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^rem-c6b-1-2\|§C6b.1, Remark: The fundamental observable?]]); its external poles carry $i\mathcal M$ | [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-2\|Def. §C6a.4.2]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7\|Theorem §C6a.4.7]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5\|Theorem §C6a.11.5]] | Lecture 13, slides 17–22; Lecture 14, slides 16–18, 25; PS8 P1(a), P1(b) ([[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5\|Example §C6a.9.5]], [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-7\|Example §C6a.9.7]]) |
| vacuum-to-vacuum amplitude, vacuum bubbles | $\langle0\vert T\{e^{-i\int_{-T}^T\hat H_I}\}\vert0\rangle = \langle0\vert U(T, -T)\vert0\rangle = 1 + \sum$ vacuum diagrams $= e^{\sum_iV_i}$ | free vacuum $\vert0\rangle$ | in $\phi^4$: no, it cancels from every correlator; $\sum_iV_i$ gives $E_0/V$. For a source: $P(0) = \lvert\cdot\rvert^2$, yes | [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4\|Theorem §C6a.4.4]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^def-c6a-11-1\|Def. §C6a.11.1]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6\|Theorem §C6a.11.6]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-7\|Theorem §C6a.11.7]] | Lecture 13, slide 20; Lecture 14, slides 24–26; PS8 P3(a), (c), $\langle0\vert\hat S\vert0\rangle = e^{\mathcal A_2}$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3\|Theorem §C6b.9.3]]) |
| $S$-matrix element and its $\mathbb 1$ part | $\langle f\vert\hat S\vert i\rangle = \lim_{T\to\infty}\langle f\vert e^{-i\hat H\,2T}\vert i\rangle = \langle f\vert i\rangle + \langle f\vert i\hat T\vert i\rangle$ | in and out states (widely separated), relativistic $\langle\mathbf p\vert\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ | an amplitude, not itself; $\lvert\cdot\rvert^2$ between normalized states is a probability. The $\mathbb 1$ part $\langle f\vert i\rangle$ is "nothing happened": forward only, dropped from $d\sigma$; disconnected correlator pieces belong to it | [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1\|Def. §C6b.1.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2\|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1\|Theorem §C6b.1.1]], [[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5\|Lemma §C6b.4.5]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-2\|Theorem §C6b.8.2]] | Lecture 15, slides 4–6; PS8 P3(a), (d): $\langle0\vert\hat S\vert0\rangle$ and $\langle\mathbf k\vert\hat S\vert0\rangle$ in a source ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-5\|Theorem §C6b.9.5]]) |
| $T$-matrix element and amplitude | $\langle f\vert i\hat T\vert i\rangle = (2\pi)^4\delta^4(p_i - p_f)\,i\mathcal M$; at lowest order $i\mathcal M$ = amputated fully connected diagrams | relativistic (only then is $\mathcal M$ Lorentz invariant); $[\mathcal M] = 4 - N$ | no: complex, dynamics only | [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3\|Def. §C6b.1.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4\|Theorem §C6b.1.4]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1\|Theorem §C6b.8.1]], [[§C6b.8 Amplitudes from Correlation Functions#^def-c6b-8-1\|Def. §C6b.8.1]] | Lecture 15, slide 6 and end of lecture; $i\mathcal M = -i\lambda$ ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-1\|Example §C6b.8.1]]); PS8 P2, diagrams ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-3\|Example §C6b.8.3]], [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-4\|Example §C6b.8.4]]); PS8 P4, $\mathcal M = -2\mu$ ([[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1\|Example §C6b.7.1]]) |
| squared amplitude | $\lvert\mathcal M(p_A, p_B \to \{p_j\})\rvert^2$ | as for $\mathcal M$ | not alone: the dynamical factor of $d\sigma$ and $d\Gamma$ | [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2\|Theorem §C6b.5.2]], [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4\|Theorem §C6b.7.4]] | Lecture 15, slide 16; $\lambda^2$ ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-2\|Example §C6b.8.2]]); PS8 P4, $4\mu^2$ |
| cross section | $d\sigma = \frac{1}{2E_A2E_B\lvert\mathbf v_A - \mathbf v_B\rvert}\lvert\mathcal M\rvert^2d\Pi_n$, $\sigma = \frac{1}{S_{\rm id}}\int d\sigma$ | packets with $\int\frac{d^3k}{(2\pi)^3}\lvert\phi\rvert^2 = 1$, or a box with $\langle\mathbf p\vert\mathbf p\rangle = 2E\tilde V$; final measure $\frac{d^3p}{(2\pi)^32E}$ | yes: events per target particle per unit flux, $N = \sigma N_Aj_Bt$ | [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1\|Def. §C6b.4.1]], [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6\|Def. §C6b.4.6]], [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2\|Theorem §C6b.5.2]], [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4\|Theorem §C6b.5.4]], [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-7\|Theorem §C6b.6.7]] | Lecture 15, slides 8, 11–16, 19–21; $\sigma = \lambda^2/(32\pi E_{\rm cm}^2)$ ([[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-2\|Example §C6b.8.2]]); PS8: none (P2 stops at the diagrams) |
| decay rate | $d\Gamma = \frac{1}{2m_A}\lvert\mathcal M\rvert^2d\Pi_n$, $\Gamma = \frac{1}{S_{\rm id}}\int d\Gamma$ | relativistic, $A$ at rest; box route | yes: $\Gamma = 1/\tau$, decays per unit time per particle; also the resonance width | [[§C6b.7 Decay Rates and Widths#^def-c6b-7-1\|Def. §C6b.7.1]], [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4\|Theorem §C6b.7.4]], [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-5\|Theorem §C6b.7.5]], [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-10\|Theorem §C6b.7.10]] | Lecture 15, slides 22–23; PS8 P4, $\Phi \to \phi\phi$ ([[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1\|Example §C6b.7.1]]) |
| particle number in an external source | $P(n) = \frac{1}{n!}\int\prod_i\frac{d^3k_i}{(2\pi)^3}\lvert\langle\mathbf k_1\cdots\mathbf k_n\vert T\{e^{i\int j\hat\phi_I}\}\vert0\rangle\rvert^2 = \frac{\lambda^n}{n!}e^{-\lambda}$ | $\vert\mathbf k\rangle = \hat a^\dagger_{\mathbf k}\vert0\rangle$, $\langle\mathbf p\vert\mathbf k\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf k)$; measure $\frac{1}{n!}\prod\frac{d^3k}{(2\pi)^3}$ | yes: a probability (Poisson, mean $\lambda$) | [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-1\|Theorem §C6b.9.1]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4\|Lemma §C6b.9.4]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-6\|Theorem §C6b.9.6]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7\|Theorem §C6b.9.7]] | PS8 P3(a)–(f); lecture: none (the coherent-state route is [[§C2b.8 Particle Production by a Classical Source\|§C2b.8]]) |

## How to read C6a and C6b

- *What is the interaction, and how does it act on free fields?* [[§C6a.1 From Free to Interacting Fields|§C6a.1]], [[§C6a.2 The Interaction Picture|§C6a.2]] (steps 1–2).
- *Why a time-ordered exponential instead of $e^{-i\int\hat H_I}$?* [[§C6a.3 The Time-Evolution Operator and Time Ordering|§C6a.3]] (step 3).
- *How does the unknown interacting vacuum $|\Omega\rangle$ drop out?* [[§C6a.4 The Interacting Vacuum and the Two-Point Function|§C6a.4]] (step 4).
- *How is a free vacuum value of many fields evaluated?* [[§C6a.5 Normal Ordering and Contractions|§C6a.5]], [[§C6a.6 Wick's Theorem|§C6a.6]] (step 5).
- *How are terms grouped into diagrams, and with what coefficient?* [[§C6a.7 Feynman Diagrams for Correlation Functions|§C6a.7]], [[§C6a.8 Position-Space Feynman Rules|§C6a.8]]; symmetry factors in practice [[§C6a.9 Symmetry Factors in Practice|§C6a.9]]; momentum space [[§C6a.10 Feynman Rules in Momentum Space|§C6a.10]] (step 6).
- *Where did the denominator go?* [[§C6a.11 The iε Limit and Vacuum Bubbles|§C6a.11]] (step 7).
- *What does an experiment measure, and what is $\mathcal M$?* [[§C6b.1 The S-Matrix and the Invariant Amplitude|§C6b.1]] (steps 8–9).
- *How does $\mathcal M$ become a cross section, and where does each factor come from?* [[§C6b.2 Cross Section — opening rewrite (draft)|draft opening]], then [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]], [[§C6b.5 Evaluating the Cross Section|§C6b.5]]; frames and two-body phase space [[§C6b.6 Lorentz Invariance and Two-Body Phase Space|§C6b.6]] (step 11).
- *How does $\mathcal M$ become a decay rate or a width?* [[§C6b.7 Decay Rates and Widths|§C6b.7]] (step 11).
- *How is $\mathcal M$ read off from diagrams, and which diagrams count?* [[§C6b.8 Amplitudes from Correlation Functions|§C6b.8]] (step 10).
- *What if $\hat H_I(t)$ depends explicitly on time (an external source), and how do outgoing particles contract with fields?* [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]] (step 12).
