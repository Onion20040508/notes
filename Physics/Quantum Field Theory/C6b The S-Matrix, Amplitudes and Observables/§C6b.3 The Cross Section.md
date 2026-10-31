---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.2 Transition Probabilities in a Box]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.4 Wave Packets and the Cross Section]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.5.2 "散射截面", pp. 242–246, eqs. (6.307)–(6.331), Fig. 6.4 (page images checked, PDF pp. 250–254) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part A, slide 8 ("Cross-section … is a universal event rate"), slides 16, 20, 24, and transcript · the user's PHY 513 notes, Ch. 15 §15.2 (paragraph "Event counting (filled in)"), §15.5, §15.6 (eq. (moller)), §15.10 (paragraph "Correspondence with Yu") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 99–101, 106, eqs. (4.59)–(4.61), (4.79)–(4.80).*

**What is prepared.** A beam of particles $B$, all with the same velocity, falls on a target of particles $A$ at rest ([[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]). **What is measured.** The number $N$ of scattering events, with the final particles in a given range of momenta, during a time $t$. The cross section is that count with the beam and the target divided out ([[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]]). Applied to one $A$ and one $B$ in the box of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]], it is the rate of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]] divided by the flux, and the last power of the box volume cancels ([[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]]). The Møller velocity makes the result Lorentz invariant ([[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]]); for collinear beams it is the velocity difference $|\mathbf v_A - \mathbf v_B|$ ([[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]]), and the differential cross section ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]]) is the formula of the lecture. The section ends with that formula written once, every factor labelled by the box that produced it. Yu §6.5.2 is followed step by step; the course's own derivation of the same formula, with wave packets, follows in [[§C6b.4 Wave Packets and the Cross Section|§C6b.4]]–[[§C6b.5 Evaluating the Cross Section|§C6b.5]].

*Conventions* ([[Larsen PHY 513]]): $\mathbf v = \mathbf p/E = \partial E_{\mathbf p}/\partial\mathbf p$, the group velocity of a packet peaked at $\mathbf p$; $a$ is the cross-sectional area of the beam (Yu: $A$) and $V$ the volume it sweeps (Yu: $V$), not the box volume $\tilde V$; $\mathcal R$ is a rate per unit volume, $R$ the rate of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]] ([[§C6b.2 Transition Probabilities in a Box#^cau-c6b-2-1|§C6b.2, Caution: Names in Yu's §6.5.1]]); $S_{\rm id}$ the identical-particle factor.

## The model and the definitions

> [!model] Model §C6b.3.1: Beam on a Fixed Target
> - *Target:* $N_A$ particles $A$ at rest, filling the volume $V$ with density $n_A = N_A/V$.
> - *Beam:* particles $B$ with one common velocity $\mathbf v_B = \mathbf p_B/E_B$, density $n_B$ (particles per volume), cross-sectional area $a$.
> - *Independence:* every event is one $A$ and one $B$ scattering once; the target is thin, so the beam is not depleted and no particle scatters twice; the targets do not shadow each other.
> - *Count:* $N$ = the number of events, with final momenta in a given range, in a time $t$.
> - *Each collision:* one $A$ and one $B$ in a box of volume $\tilde V$, [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], with its Hamiltonian, free states and range of validity.
>
> *Source: Yu §6.5.2, pp. 242–243, Fig. 6.4 ("束流打靶实验"), eqs. (6.307)–(6.308) · PHY 513 Lecture 15, slide 8 · PS §4.5, pp. 99–100*

^mod-c6b-3-1

> [!definition] Definition §C6b.3.1: Flux
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]].
> The **flux** (流密度) of the beam is the number of $B$ particles crossing unit area per unit time. The particles that cross the area $a$ in the time $t$ fill the cylinder of volume $a|\mathbf v_B|t$ behind it, $N_B = n_Ba|\mathbf v_B|t$, so
>
> $$
> j_B \equiv \frac{N_B}{a\,t} = \frac{n_Ba|\mathbf v_B|t}{a\,t} = n_B\,|\mathbf v_B| .
> $$
>
> *Source: Yu §6.5.2, eq. (6.307) (page image checked)*

^def-c6b-3-1

> [!definition] Definition §C6b.3.2: Cross Section (Operational)
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]].
> The **cross section** $\sigma$ is the constant of proportionality in
>
> $$
> N = N_A\,j_B\,\sigma\,t ;
> $$
>
> it is an area, the effective area that one target particle presents to the beam (散射截面, "相当于发生散射的有效面积"). Unit: the barn, $1\,\mathrm b = 10^{-28}\,\mathrm m^2$; in natural units $1\,\mathrm b = 2.568\times10^3\,\mathrm{GeV}^{-2}$ and $1\,\mathrm{GeV}^{-2} = 3.894\times10^{-4}\,\mathrm b = 0.3894\,\mathrm{mb}$. When only final momenta in a range are counted, the constant is the differential cross section $d\sigma$.
>
> This is the course's definition of the cross section as a universal event rate, [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]] (slide 8), stated for Yu's set-up: the same $N_{\rm events} = \sigma N_Aj_Bt$.
>
> *Source: Yu §6.5.2, eqs. (6.308)–(6.311) (page image checked) · PHY 513 Lecture 15, slide 8 · PS §4.5, eqs. (4.59)–(4.61)*

^def-c6b-3-2

## From the box rate to the cross section

> [!theorem] Theorem §C6b.3.2: Events per Unit Volume and Time
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]].
> The number of events per unit volume and unit time is
>
> $$
> \mathcal R \equiv \frac{N}{V\,t} = n_A\,n_B\,\sigma\,|\mathbf v_B| .
> $$
>
> *Source: Yu §6.5.2, eq. (6.312) (page image checked)*

^thm-c6b-3-2

> [!derivation]- Derivation
> **Step 1** (insert the definitions). [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]], then [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], then $n_A = N_A/V$ ([[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]):
>
> $$
> \frac{N}{Vt} = \frac{N_Aj_B\sigma t}{Vt} = \frac{N_Aj_B\sigma}{V} = \frac{N_An_B|\mathbf v_B|\sigma}{V} = n_An_B\sigma|\mathbf v_B| .
> $$
>
> **What the derivation shows.**
> - $\mathcal R$ is symmetric in the two densities: per unit volume, the event rate is $\sigma$ times the product of the densities times the speed at which the two populations pass through each other.

^der-c6b-3-2

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]]

> [!theorem] Theorem §C6b.3.3: The Cross Section in the Rest Frame of A
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] with one $A$ and one $B$ in the box of [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there; $A$ at rest.
> With $R$ the total rate of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]],
>
> $$
> \sigma = \frac{R\,\tilde V}{|\mathbf v_B|} = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_B|\mathbf v_B|}\;\prod_{j=1}^n\int\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2 .
> $$
>
> The box volume $\tilde V$ and the duration $\tilde T$ have cancelled.
>
> *Source: Yu §6.5.2, eq. (6.313) (page image checked; "上式对 $\mathcal A$ 粒子静止的参考系成立")*

^thm-c6b-3-3

> [!derivation]- Derivation
> **Step 1** (one of each in the box). One $A$ and one $B$ in the volume $\tilde V$: $n_A = n_B = 1/\tilde V$. Their single event rate $R$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]]) is spread over the box, so the rate per unit volume is $\mathcal R = R/\tilde V$ (Yu, before (6.313)).
>
> **Step 2** (solve for $\sigma$). [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] solved for $\sigma$, with Step 1:
>
> $$
> \sigma = \frac{\mathcal R}{n_An_B|\mathbf v_B|} = \frac{R}{\tilde V}\cdot\frac{1}{\tilde V^{-1}\tilde V^{-1}|\mathbf v_B|} = \frac{R}{\tilde V}\cdot\frac{\tilde V^2}{|\mathbf v_B|} = \frac{R\,\tilde V}{|\mathbf v_B|} .
> $$
>
> Equivalently: the rate per target particle is $\sigma j_B$ ([[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]] with $N_A = 1$), and $j_B = n_B|\mathbf v_B| = |\mathbf v_B|/\tilde V$ ([[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]]), so $\sigma = R/j_B = R\tilde V/|\mathbf v_B|$.
>
> **Step 3** (insert the rate). [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]] has the prefactor $\frac{1}{S_{\rm id}}\frac{1}{4E_AE_B\tilde V}$; multiplied by $\tilde V/|\mathbf v_B|$ it becomes $\frac{1}{S_{\rm id}}\frac{1}{4E_AE_B|\mathbf v_B|}$, the statement (Yu (6.313)).
>
> **Step 4** (bookkeeping of the box). Every power of $\tilde V$ and $\tilde T$ along the chain of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]]:
>
> | step | factor | power of $\tilde V$ | power of $\tilde T$ |
> |---|---|---|---|
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2\|Theorem §C6b.2.2]] | $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ | $+1$ | $+1$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]], 2 | $1/\langle i\vert i\rangle = 1/(4E_AE_B\tilde V^2)$ | $-2$ | $0$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]], 3 | $1/\langle f\vert f\rangle = 1/\prod_j(2E_j\tilde V)$ | $-n$ | $0$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4\|Theorem §C6b.2.4]] | per unit time, $1/\tilde T$ | $0$ | $-1$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5\|Theorem §C6b.2.5]] | states in the range, $\prod_j\tilde V\,d^3p_j/(2\pi)^3$ | $+n$ | $0$ |
> | this theorem | per unit flux, $\tilde V/\lvert\mathbf v_B\rvert$ | $+1$ | $0$ |
> | | total | $1 - 2 - n + n + 1 = 0$ | $1 - 1 = 0$ |
>
> **What the derivation shows.**
> - The flux of one plane-wave particle in the box is $|\mathbf v_B|/\tilde V$: its density is uniform, $1/\tilde V$. The careful route makes the same average explicit as an integral over the impact parameter at unit density ([[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4|Theorem §C6b.4.4]]).
> - The result is finite and independent of the regularization: the box was only bookkeeping.
> - Only $E_B|\mathbf v_B| = |\mathbf p_B|$ and $E_A = m_A$ refer to the rest frame of $A$; the next two theorems remove that restriction.

^der-c6b-3-3

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]], [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]]

## Any frame: the Møller velocity

In [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]] everything except the factor $(4E_AE_B|\mathbf v_B|)^{-1}$ is Lorentz invariant: $|\mathcal M|^2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]) and the measure ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]). In the rest frame of $A$, $|\mathbf v_B|$ is the speed of $B$ relative to $A$; Yu replaces it by an invariant that takes this value there.

> [!definition] Definition §C6b.3.3: Møller Velocity
> For two particles with four-momenta $p_A$, $p_B$ and masses $m_A$, $m_B$, the **Møller velocity** is
>
> $$
> v_{\rm Møl} \equiv \frac{1}{E_AE_B}\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} .
> $$
>
> *Source: Yu §6.5.2, eq. (6.315) (page image checked)*

^def-c6b-3-3

> [!theorem] Theorem §C6b.3.4: The Lorentz-Invariant Cross Section
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] and [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], in any inertial frame; spinless particles (for $|\mathcal M|^2$ invariant).
> 1. The incident flux factor $E_AE_Bv_{\rm Møl} = \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ is Lorentz invariant.
> 2. In the rest frame of $A$, $v_{\rm Møl} = |\mathbf v_B|$.
> 3. Hence
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_Bv_{\rm Møl}}\;\prod_{j=1}^n\int\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2
> $$
>
> is Lorentz invariant and equals [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]] in the rest frame of $A$. Yu takes it as the definition of $\sigma$ in every frame (eq. (6.316)).
>
> *Source: Yu §6.5.2, eqs. (6.313)–(6.317) (page image checked)*

^thm-c6b-3-4

> [!derivation]- Derivation
> **Step 1** (part 1). $p_A\cdot p_B$ and $m_A^2$, $m_B^2$ are Lorentz scalars, so $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ is, and by [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]] it equals $E_AE_Bv_{\rm Møl}$.
>
> **Step 2** (part 2). At rest $p_A = (m_A, \mathbf 0)$, so $p_A\cdot p_B = m_AE_B$, $E_A = m_A$, and with $E_B^2 - m_B^2 = |\mathbf p_B|^2$ (Yu (6.317)):
>
> $$
> v_{\rm Møl} = \frac{1}{m_AE_B}\sqrt{m_A^2E_B^2 - m_A^2m_B^2} = \frac{m_A\sqrt{E_B^2 - m_B^2}}{m_AE_B} = \frac{|\mathbf p_B|}{E_B} = |\mathbf v_B| .
> $$
>
> **Step 3** (the rest of the integrand). $|\mathcal M|^2$ is invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]]); each $\frac{d^3p_j}{(2\pi)^32E_j}$ is invariant ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]); and $\delta^4(\Lambda P - \sum_j\Lambda p_j) = |\det\Lambda|^{-1}\delta^4(P - \sum_jp_j) = \delta^4(P - \sum_jp_j)$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1). The same argument written out for the phase-space integral is [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-4|Theorem §C6b.6.4]].
>
> **Step 4** (part 3). By Steps 1 and 3 every factor of the expression is invariant. By Step 2 it equals [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]] in the rest frame of $A$ (with $4E_AE_B|\mathbf v_B| = 4E_AE_Bv_{\rm Møl}$ there), hence in every frame it takes the rest-frame value.
>
> **What the derivation shows.**
> - Yu's choice builds the invariance in; the course instead shows that $E_AE_B|\mathbf v_A - \mathbf v_B|$ is a component of an antisymmetric tensor, invariant under boosts along the beam ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-3|Theorem §C6b.6.3]]). For collinear beams the two agree ([[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]]).
> - $E_AE_B|\mathbf v_A - \mathbf v_B|$ alone is not invariant for general directions (Yu, after (6.314): "$E_{\mathcal A}E_{\mathcal B}v_{\rm rel}$ 并不是 Lorentz 不变量").

^der-c6b-3-4

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]], [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-4|Theorem §C6b.1.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!theorem] Theorem §C6b.3.5: The Møller Velocity and the Velocity Difference
> With $\mathbf v_A = \mathbf p_A/E_A$, $\mathbf v_B = \mathbf p_B/E_B$,
>
> $$
> v_{\rm Møl} = \sqrt{|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2} .
> $$
>
> 1. For collinear motion, $\mathbf v_A\times\mathbf v_B = \mathbf 0$ (one particle at rest, or the two moving along one line in the same or opposite directions, as in a collider), $v_{\rm Møl} = |\mathbf v_A - \mathbf v_B|$ exactly, and the flux factor is $E_AE_B|\mathbf v_A - \mathbf v_B|$.
> 2. For $|\mathbf v_A|, |\mathbf v_B| \ll 1$, $v_{\rm Møl} \simeq |\mathbf v_A - \mathbf v_B|$, the Newtonian relative velocity.
>
> *Source: Yu §6.5.2, eqs. (6.322)–(6.331) and the paragraphs after (6.329) (page images checked) · the user's PHY 513 notes, Ch. 15 §15.6, eq. (moller)*

^thm-c6b-3-5

> [!derivation]- Derivation
> **Step 1** (the angle). With $\alpha$ the angle between $\mathbf v_A$ and $\mathbf v_B$ (Yu (6.322)–(6.323)),
>
> $$
> \mathbf v_A\cdot\mathbf v_B = |\mathbf v_A||\mathbf v_B|\cos\alpha , \qquad |\mathbf v_A\times\mathbf v_B| = |\mathbf v_A||\mathbf v_B|\sin\alpha , \qquad (\mathbf v_A\cdot\mathbf v_B)^2 = |\mathbf v_A|^2|\mathbf v_B|^2(1 - \sin^2\alpha) = |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 .
> $$
>
> **Step 2** (square $1 - \mathbf v_A\cdot\mathbf v_B$). Expand, insert Step 1, and write $-2\mathbf v_A\cdot\mathbf v_B = |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A|^2 - |\mathbf v_B|^2$ (Yu (6.324)):
>
> $$
> \begin{aligned}
> (1 - \mathbf v_A\cdot\mathbf v_B)^2 &= 1 - 2\mathbf v_A\cdot\mathbf v_B + |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\\
> &= 1 + |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A|^2 - |\mathbf v_B|^2 + |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\\
> &= |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 + (1 - |\mathbf v_A|^2)(1 - |\mathbf v_B|^2) .
> \end{aligned}
> $$
>
> **Step 3** (the four-vector product). $p^\mu = (E, \mathbf p) = E(1, \mathbf v)$ (Yu (6.325)), so (Yu (6.326))
>
> $$
> p_A\cdot p_B = E_AE_B - \mathbf p_A\cdot\mathbf p_B = E_AE_B(1 - \mathbf v_A\cdot\mathbf v_B) .
> $$
>
> **Step 4** (the masses cancel). Square Step 3, insert Step 2, and use $E^2(1 - |\mathbf v|^2) = E^2 - |\mathbf p|^2 = m^2$ for each particle (Yu (6.327)–(6.328)):
>
> $$
> \begin{aligned}
> (p_A\cdot p_B)^2 - m_A^2m_B^2 &= E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) + E_A^2(1 - |\mathbf v_A|^2)\,E_B^2(1 - |\mathbf v_B|^2) - m_A^2m_B^2\\
> &= E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) + m_A^2m_B^2 - m_A^2m_B^2 = E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) .
> \end{aligned}
> $$
>
> **Step 5** (the statement). Divide by $E_A^2E_B^2$ and take the positive root ([[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]]; Yu (6.329)):
>
> $$
> v_{\rm Møl} = \frac{1}{E_AE_B}\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = \sqrt{|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2} .
> $$
>
> **Step 6** (parts 1–2). If $\mathbf v_A\times\mathbf v_B = \mathbf 0$, Step 5 is $\sqrt{|\mathbf v_A - \mathbf v_B|^2} = |\mathbf v_A - \mathbf v_B|$, and the flux factor is $E_AE_Bv_{\rm Møl} = E_AE_B|\mathbf v_A - \mathbf v_B|$ (Yu (6.330)–(6.331)). For small velocities $|\mathbf v_A\times\mathbf v_B|^2 = |\mathbf v_A|^2|\mathbf v_B|^2\sin^2\alpha$ is of fourth order in the velocities and $|\mathbf v_A - \mathbf v_B|^2$ of second order, so the cross product is negligible.
>
> **What the derivation shows.**
> - The Møller velocity is the relativistic generalization of the relative velocity; for collinear beams it is the velocity difference measured in one frame, which can exceed 1: head-on at the speed of light $|\mathbf v_A - \mathbf v_B| = 2$ (Yu after (6.331); [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^cau-c6b-6-1|§C6b.6, Caution: The velocity difference is not a relative velocity]]).
> - Multiplied by $E_AE_B$, Step 5 is the course's invariant form of the flux factor, [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-3|Theorem §C6b.6.3]].

^der-c6b-3-5

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]]

## The differential cross section

> [!definition] Definition §C6b.3.4: n-Body Invariant Phase Space
> For $2 \to n$ scattering with initial momenta $p_A$, $p_B$, the **$n$-body invariant phase space** is
>
> $$
> d\Pi_n = \Bigl(\prod_{j=1}^n\frac{d^3p_j}{(2\pi)^3\,2E_j}\Bigr)\,(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr) .
> $$
>
> This is the course's $n$-particle phase space, [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^def-c6b-6-1|Def. §C6b.6.1]] (slide 20), with total momentum $P = p_A + p_B$; it is Lorentz invariant ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-4|Theorem §C6b.6.4]]).
>
> *Source: Yu §6.5.2, eq. (6.318) ("$n$ 体不变相空间") · PHY 513 Lecture 15, slide 20 · PS §4.5, eq. (4.80)*

^def-c6b-3-4

> [!theorem] Theorem §C6b.3.6: The Differential Cross Section
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] and [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there.
> 1. Without the integral over the final momenta,
>
> $$
> d\sigma = \frac{1}{4E_AE_Bv_{\rm Møl}}\,|\mathcal M|^2\,d\Pi_n , \qquad \sigma = \frac{1}{S_{\rm id}}\int d\sigma .
> $$
>
> 2. For collinear beams,
>
> $$
> d\sigma = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\;|\mathcal M(p_A, p_B \to \{p_j\})|^2\;d\Pi_n .
> $$
>
> This is the formula of the lecture, derived there with wave packets ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]]; PS (4.79)).
>
> *Source: Yu §6.5.2, eqs. (6.319)–(6.321), (6.330)–(6.331) (page images checked: "计算微分截面 $d\sigma$ 时不会对全同量子态重复计数，因而不需要考虑末态对称性因子") · PHY 513 Lecture 15, slides 16, 24*

^thm-c6b-3-6

> [!derivation]- Derivation
> **Step 1** (drop the integral). Write [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]] with [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]] (Yu (6.319)):
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_Bv_{\rm Møl}}\int d\Pi_n\,|\mathcal M|^2 = \frac{1}{S_{\rm id}}\int\Bigl[\frac{1}{4E_AE_Bv_{\rm Møl}}\,|\mathcal M|^2\,d\Pi_n\Bigr] ,
> $$
>
> and the bracket is the cross section into the range $d\Pi_n$ of final momenta (Yu (6.320)).
>
> **Step 2** (no $S_{\rm id}$ in $d\sigma$). The factor of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]] corrects a sum over all orderings of the final momenta. A small range around pairwise different momenta and its permuted copies are disjoint, so each state in it is counted once: $d\sigma$ carries no factor, and $\sigma = \frac{1}{S_{\rm id}}\int d\sigma$ (Yu (6.321)).
>
> **Step 3** (collinear beams). By [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], 1, $v_{\rm Møl} = |\mathbf v_A - \mathbf v_B|$, and $4E_AE_B = 2E_A\cdot2E_B$:
>
> $$
> \frac{1}{4E_AE_Bv_{\rm Møl}} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|} .
> $$
>
> **What the derivation shows.**
> - Box route and wave-packet route give the same $d\sigma$; the course's form holds in every frame reached from the rest frame of $A$ along the beam axis, the centre-of-mass frame included ([[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-3|Theorem §C6b.6.3]]).
> - Dimension: $[d\sigma] = -2$ for every $n$ ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-3|Theorem §C6b.5.3]]).

^der-c6b-3-6

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]], [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]]

## The annotated formula

$$
d\sigma = \underbrace{\underbrace{\frac{1}{2E_A\,2E_B}}_{\text{(a)}}\;\underbrace{\frac{1}{|\mathbf v_A - \mathbf v_B|}}_{\text{(b)}}}_{\text{flux factor}}\;\;\underbrace{|\mathcal M|^2}_{\text{(c) dynamics}}\;\;\underbrace{\prod_{j=1}^n\underbrace{\frac{d^3p_j}{(2\pi)^3}}_{\text{(d)}}\,\underbrace{\frac{1}{2E_j}}_{\text{(e)}}\;\underbrace{(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)}_{\text{(f)}}}_{\text{phase space }d\Pi_n}
$$

| label | factor | where it comes from | box | careful route |
|---|---|---|---|---|
| (a) | $\frac{1}{2E_A\,2E_B}$ | the norm of the initial state, $\langle i\vert i\rangle = 2E_A\tilde V\cdot2E_B\tilde V$: relativistic normalization of the two incoming particles | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]], 2 | the packet factor $1/\sqrt{2E}$, [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3\|Def. §C6b.4.3]]; [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 6 |
| (b) | $\frac{1}{\lvert\mathbf v_A - \mathbf v_B\rvert}$ | the flux $j_B = n_B\lvert\mathbf v_B\rvert = \lvert\mathbf v_B\rvert/\tilde V$: cross section = rate / flux; in any collinear frame the Møller velocity | [[§C6b.3 The Cross Section#^def-c6b-3-1\|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^thm-c6b-3-3\|Theorem §C6b.3.3]], [[§C6b.3 The Cross Section#^thm-c6b-3-5\|Theorem §C6b.3.5]] | the Jacobian of the longitudinal delta functions, [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-1\|Theorem §C6b.5.1]] |
| (c) | $\lvert\mathcal M\rvert^2$ | the squared amplitude with the $\delta^4$ taken out: the only dynamical factor | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2\|Theorem §C6b.2.2]] | $\mathcal M\bar{\mathcal M}^\ast$ at $\bar k = k$, [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Steps 2, 5–6 |
| (d) | $\frac{d^3p_j}{(2\pi)^3}$ | the number of box states in $d^3p_j$, $\tilde V\,d^3p_j/(2\pi)^3$, with $\tilde V$ cancelled | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5\|Theorem §C6b.2.5]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6\|Theorem §C6b.2.6]] | the completeness measure in $\mathcal P(\mathbf b)$, [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5\|Def. §C6b.4.5]] |
| (e) | $\frac{1}{2E_j}$ | the norm of the final state, $\langle f\vert f\rangle = \prod_j2E_j\tilde V$ | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]], 3; [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6\|Theorem §C6b.2.6]] | the same measure ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2\|Def. §C2a.4.2]]) |
| (f) | $(2\pi)^4\delta^4(\cdots)$ | the second copy of $\delta^4$ in the squared amplitude; the first became $\tilde V\tilde T$ | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2\|Theorem §C6b.2.2]] | the $\delta^4$ of the unbarred amplitude, never used up ([[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2\|Derivation §C6b.5.2]], Step 9) |

Two more factors do not appear in $d\sigma$. $\frac{1}{S_{\rm id}}$ enters only when $d\sigma$ is integrated over all final momenta ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]], [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]]). The box volume $\tilde V$ and the duration $\tilde T$ cancel (table in [[§C6b.3 The Cross Section#^der-c6b-3-3|Derivation §C6b.3.3]], Step 4).

> [!remark] Remark: Dynamics and kinematics
> Yu, after (6.318): in the cross section "不变振幅模方 $|\mathcal M|^2$ 是动力学因素，而其它部分都属于运动学因素" (the squared invariant amplitude is the dynamical factor, everything else is kinematics). Factors (a), (b) belong to the initial state, (d)–(f) to the final state, and only (c) knows the theory; this is the course's "dynamical data" ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^rem-c6b-1-3|§C6b.1, Remark: What "dynamical" means]]) and the lecture's reading of the formula ([[§C6b.5 Evaluating the Cross Section#^rem-c6b-5-1|§C6b.5, Remark: Reading the formula]]).
>
> *Source: Yu §6.5.2, p. 244 · PHY 513 Lecture 15, slide 16*

^rem-c6b-3-1

> [!remark]- Connections
> - The operational cross section and its classical meaning as an area in the plane of impact parameters — [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]], [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-2|Def. §C6b.4.2]], [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^def-b4-2-1|CM Def. §B4.2.1]].
> - Quantum mechanics divides a transition rate by a probability current in the same way — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^def-c10-1-1|QM Def. §C10.1.1]].
> - The flux factor as a component of an antisymmetric tensor (the course's route to frame independence), two-body phase space and $2 \to 2$ in the centre-of-mass frame — [[§C6b.6 Lorentz Invariance and Two-Body Phase Space|§C6b.6]].
> - The same chain with one initial particle and no flux gives the decay rate, $\frac{1}{2E_A}$ in place of $\frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}$ — [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4|Theorem §C6b.7.4]].
