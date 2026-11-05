---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.4 Two-Body Scattering Kinematics]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.6 Decay Kinematics]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.8 (Principle "Decay rate", paragraph "Reading the formula", Caution "'Corollary of studying interacting wave function (2nd term)'", eq. (BWprop), Figure "breitwigner", paragraph "Relation to non-relativistic decay", eq. (GammaNR), Principle "The width is invariant; the decay rate is time-dilated", paragraph "Checks (filled in)") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part C, slides 22–23, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 101, 107–108, eqs. (4.62)–(4.64), (4.86) · Yu Zhao-Huan, 量子场论讲义, §6.5.4, eqs. (6.367)–(6.378); §6.5.5, eqs. (6.379)–(6.385); §10.6, eqs. (10.259)–(10.275) · the user's PHY 513 notes, Ch. 15 §15.8, paragraph "Two-body decays (filled in)" · PHY 513, Problem Set 8, Problem 4 (= PS Problem 4.2; the user's solution).*

"The other one that's really important and common is … one to $n$, which does not seem like scattering at all": the decay of one particle into $n$ decay products. The wave-packet construction of [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]] was built around two packets and an impact parameter and does not apply as it stands; the lecture stated the result, the decay rate $d\Gamma = |\mathcal M|^2d\Pi_n/2m_A$ ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]), with the same final phase space as before ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]), and derived here by Yu's box route: the chain of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]] with one initial particle, set up in [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]] and run in [[§C6b.5 Decay Widths#^thm-c6b-5-4|Theorem §C6b.5.4]]–[[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]. For two decay products everything but the direction is fixed ([[§C6b.6 Decay Kinematics#^thm-c6b-6-1|Theorem §C6b.6.1]]); the decay $\Phi \to \phi\phi$ of Problem Set 8 is worked as the user solved it ([[§C6b.6 Decay Kinematics#^ex-c6b-6-1|Example §C6b.6.1]]). A population decays exponentially ([[§C6b.5 Decay Widths#^law-c6b-5-2|Law §C6b.5.2]]); in relativistic physics one quotes the width $\Gamma$, an energy, rather than the lifetime. The width also appears in the propagator of an unstable particle, $i/(p^2 - m^2 + im\Gamma)$ in place of the $+i\varepsilon$ ([[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]]); near its pole this is the non-relativistic exponential decay with the rate time-dilated by $m/E_{\mathbf p}$ ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|Theorem §C6b.7.3]]), and its square is the Breit–Wigner resonance of full width $\Gamma$. Yu treats decay widths in §6.5.4, eqs. (6.367)–(6.378), with box normalization, and the width in the propagator in §10.6, eqs. (10.259)–(10.275), where it is derived from the imaginary part of the self-energy.

<!-- HEADER-5 -->

*Conventions* ([[Larsen PHY 513]]): $A$ is the decaying particle, mass $m_A$, at rest unless said otherwise; $\Gamma$ (width, rest frame) and $\Gamma_{\rm NR}$ (decay constant of a non-relativistic wave function, any frame) as defined below; $S_{\rm id}$ the identical-particle factor ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]]); $\tilde V$, $\tilde T$ Yu's volume and duration.

## The decay rate

> [!model] Model §C6b.5.1: A Decaying Particle at Rest
> - *Particle:* one unstable particle $A$ of mass $m_A$, at rest, $p_A = (m_A, \mathbf 0)$ (in a frame where it moves, $E_A = \gamma m_A$); it decays into $n \ge 2$ particles with $m_A > \sum_jm_j$.
> - *Population:* $N(t)$ particles $A$ at rest, each decaying with the same constant probability $\Gamma$ per unit time, independently of its age and of the others (observed: [[§C6b.5 Decay Widths#^law-c6b-5-2|Law §C6b.5.2]]).
> - *Box:* one decay is computed as in [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] with one initial particle: a periodic box of volume $\tilde V$, a duration $\tilde T$, the free states $|i\rangle = \sqrt{2E_A}\,\hat a^\dagger_{\mathbf p_A}|0\rangle$ and $|f\rangle = \prod_j\sqrt{2E_j}\,\hat a^\dagger_{\mathbf p_j}|0\rangle$ over the free vacuum $|0\rangle$, and $\hat S = U(+\infty, -\infty)$.
> - *Applies:* at lowest order in the interaction that makes $A$ decay. An unstable particle cannot be prepared in the infinite past, and the interaction is never switched off, so free states are not its exact asymptotic states; the formula is correct with $\mathcal M$ from the Feynman rules (PS pp. 107–108; [[§C6b.5 Decay Widths#^cau-c6b-5-1|Caution: Free states in a decay amplitude]], [[§C6b.5 Decay Widths#^cau-c6b-5-2|Caution: "Corollary of studying interacting wave function (2nd term)"]], below; [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]).
>
> *Source: Yu §6.5.4, eqs. (6.367)–(6.378) (page images checked, PDF pp. 258–260) · PHY 513 Lecture 15, slide 22 · PS §4.5, pp. 101, 107–108*

^mod-c6b-5-1

> [!definition] Definition §C6b.5.1: Decay Rate, Width and Lifetime
> The **decay rate** $\Gamma$ of an unstable particle $A$ is the probability per unit time that $A$, at rest, decays (into a specified final state, or into anything for the total rate): $\Gamma = \frac{\text{number of decays per unit time}}{\text{number of }A\text{ particles present}}$. In relativistic contexts it is quoted as the **width**, an energy. The **lifetime** is $\tau = 1/\Gamma$.
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* a definition; the formula for $\Gamma$ holds at lowest order ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]).
>
> *Source: PHY 513 Lecture 15, slide 22 ("Another important process: $1 \to n$ 'scattering'. Decay of one particle (to $n$ decay products). Result for relativistic decay width: …"), and transcript ("What you do for decay, at least in relativistic context, is that you give not the decay time, you give the width. The width is an energy") · the user's PHY 513 notes, Ch. 15 §15.8, Principle "Decay rate" (last sentence) · PS §4.5, eq. (4.62) · Yu §6.5.4, eqs. (6.367)–(6.370) ($N(t) = N(0)e^{-\Gamma t}$, $\tau \equiv 1/\Gamma$, 衰变宽度)*

^def-c6b-5-1

> [!law] Law §C6b.5.2: The Exponential Decay Law
> A population of unstable particles $A$ at rest, $N(0)$ of them at $t = 0$, decays as
>
> $$
> N(t) = N(0)\,e^{-\Gamma t} , \qquad \tau = \frac1\Gamma ,
> $$
>
> with the decay rate $\Gamma$ and the lifetime $\tau$ of [[§C6b.5 Decay Widths#^def-c6b-5-1|Def. §C6b.5.1]]: each particle decays with the same probability $\Gamma$ per unit time, independently of its age and of the others. The same $\Gamma$ is the full width of the resonance peak ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-4|Theorem §C6b.7.4]]); a moving population decays at $\Gamma/\gamma$ ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|Theorem §C6b.7.3]]).
>
> *Valid when:* narrow resonances, $\Gamma \ll m_A$, where the pole of the propagator gives the exponential at first order in $\Gamma$ ([[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]], [[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|Theorem §C6b.7.3]]); not at very short or very long times: a survival probability starts as $1 - (\Delta E\,t)^2$, not linearly, and at very long times the decay of a state coupled to a continuum bounded below turns into a power law ([[§C9.6 The Interaction Picture and the Atom–Field Interaction#^rem-c9-6-8|QM Remark: Natural line width, derived]]). In between it is the law of radioactive decay ([[§A7.2 Radioactive Decay#^thm-a7-2-2|QM Theorem §A7.2.2]]).
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]] (its *Population* item); *applies:* a population at rest; $\Gamma$ itself is computed at lowest order by [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]].
>
> *Source: Yu §6.5.4, eqs. (6.367)–(6.370), pp. 250–251 · PHY 513 Lecture 15, slide 23 ($|\psi|^2 = e^{-\Gamma_{\rm NR}t}$) · the user's PHY 513 notes, Ch. 15 §15.8 (Principle "Decay rate": "the decay probability per unit time in the rest frame; the lifetime is $\tau = 1/\Gamma$")*

^law-c6b-5-2

<!-- NEW thm-c6b-5-3 -->
The definition and [[§C6b.5 Decay Widths#^law-c6b-5-2|Law §C6b.5.2]] are the non-relativistic decay constant and decay law of a population of particles at rest ([[§A7.2 Radioactive Decay#^def-a7-2-2|QM Def. §A7.2.2]], [[§A7.2 Radioactive Decay#^thm-a7-2-2|QM Theorem §A7.2.2]]; Yu eqs. (6.367)–(6.370)). Separating variables in $dN = -\Gamma N\,dt$ and integrating by parts for the mean life, with the decay-time density $\Gamma e^{-\Gamma t}$:

$$
\int_{N(0)}^{N(t)}\frac{dN}{N} = -\Gamma\int_0^tdt' \;\Rightarrow\; N(t) = N(0)\,e^{-\Gamma t} , \qquad \langle t\rangle = \int_0^\infty t\,\Gamma e^{-\Gamma t}\,dt = \bigl[-t\,e^{-\Gamma t}\bigr]_0^\infty + \int_0^\infty e^{-\Gamma t}\,dt = 0 + \frac1\Gamma = \tau .
$$

<!-- NEW rem-c6b-5-1 -->
Why a rate is quoted as an energy: with $\hbar = 1$, $[\Gamma] = (\text{time})^{-1} = \text{energy}$. Restoring $\hbar$, the width is $\hbar\Gamma$ and the lifetime $\tau = \hbar/(\hbar\Gamma)$; with $\hbar = 6.582\times10^{-25}\,\mathrm{GeV\,s}$,

$$
\hbar\Gamma = 1\,\mathrm{GeV} \quad\Longleftrightarrow\quad \tau = \frac{\hbar}{1\,\mathrm{GeV}} = 6.582\times10^{-25}\,\mathrm s ,
$$

and in the propagator of an unstable particle the same $\Gamma$ is the full width at half maximum of the resonance peak ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-4|Theorem §C6b.7.4]]).

<!-- NEW def-c6b-5-2 -->

The decay rate follows from the box chain of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]] with one initial particle (Yu §6.5.4): norm and transition probability ([[§C6b.5 Decay Widths#^thm-c6b-5-4|Theorem §C6b.5.4]]), rate per unit time ([[§C6b.5 Decay Widths#^thm-c6b-5-5|Theorem §C6b.5.5]]), counting of the final states and the rest frame ([[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]).

> [!theorem] Theorem §C6b.5.4: The Transition Probability of One Particle in a Box
> With $p_f = \sum_jp_j$ and distinct final momenta,
>
> $$
> \langle i|i\rangle = 2E_A\tilde V , \qquad P_{fi} = \frac{|\langle f|i\hat T|i\rangle|^2}{\langle i|i\rangle\langle f|f\rangle} = \frac{\tilde T\,(2\pi)^4\delta^4(p_A - p_f)\,|\mathcal M|^2}{2E_A\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)} .
> $$
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there.
>
> *Source: Yu §6.5.4, eqs. (6.373)–(6.374) (page image checked)*

^thm-c6b-5-4

> [!derivation]- Derivation
> The transition probability is [[§C6b.2 Transition Probabilities in a Box#^def-c6b-2-1|Def. §C6b.2.1]], with only $i\hat T$ for $f \ne i$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]], 1); the norms are [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]], parts 1 and 3, the squared amplitude [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]], 2, with $p_i = p_A$.
>
> **Step 1** (norms). By [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] at coincident momenta, with $(2\pi)^3\delta^3(\mathbf 0) = \tilde V$ (Yu eqs. (6.373), (6.290)),
>
> $$
> \langle i|i\rangle = \langle\mathbf p_A|\mathbf p_A\rangle = 2E_A(2\pi)^3\delta^3(\mathbf 0) = 2E_A\tilde V , \qquad \langle f|f\rangle = \prod_{j=1}^n2E_j(2\pi)^3\delta^3(\mathbf 0) = \prod_{j=1}^n2E_j\tilde V ,
> $$
>
> the second for $n$ distinct momenta, where of the $n!$ matchings in the overlap only the identity survives ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]).
>
> **Step 2** (the transition probability). For $f \ne i$ only $i\hat T$ contributes, and by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]
>
> $$
> |\langle f|i\hat T|i\rangle|^2 = \bigl[(2\pi)^4\delta^4(p_A - p_f)\bigr]^2|\mathcal M|^2 = (2\pi)^4\delta^4(0)\cdot(2\pi)^4\delta^4(p_A - p_f)\,|\mathcal M|^2 = \tilde V\tilde T\,(2\pi)^4\delta^4(p_A - p_f)\,|\mathcal M|^2 ,
> $$
>
> one delta function evaluated at the zero that the other enforces (Yu eq. (6.277), a box identity; on all of space $\delta^2$ has no value, [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]). The normalized probability is
>
> $$
> P_{fi} = \frac{|\langle f|i\hat T|i\rangle|^2}{\langle i|i\rangle\langle f|f\rangle} = \frac{\tilde V\tilde T\,(2\pi)^4\delta^4(p_A - p_f)\,|\mathcal M|^2}{2E_A\tilde V\cdot\prod_j(2E_j\tilde V)} = \frac{\tilde T\,(2\pi)^4\delta^4(p_A - p_f)\,|\mathcal M|^2}{2E_A\prod_j(2E_j\tilde V)} .
> $$
>
> **What the derivation shows.**
> - Only the initial norm differs from scattering: one factor $2E_A\tilde V$ instead of $4E_AE_B\tilde V^2$, so one power of $\tilde V$ less, and no flux will be needed to remove it.

^der-c6b-5-4

*Uses:* [[§C6b.2 Transition Probabilities in a Box#^def-c6b-2-1|Def. §C6b.2.1]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]

> [!theorem] Theorem §C6b.5.5: The Decay Rate into Fixed Final Momenta
> $P_{fi} \propto \tilde T$, and the transition probability per unit time for one set of final momenta $\{p_j\}$ is
>
> $$
> R_{\{p_j\}} = \frac{P_{fi}}{\tilde T} = \Bigl[2E_A\prod_{j=1}^n\bigl(2E_j\tilde V\bigr)\Bigr]^{-1}(2\pi)^4\delta^4\Bigl(p_A - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2 .
> $$
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there, for a duration $\tilde T$ long compared with the decay process but short compared with the lifetime.
>
> *Source: Yu §6.5.4, eq. (6.375) (page image checked)*

^thm-c6b-5-5

> [!derivation]- Derivation
> **Step 1** (per unit time). $P_{fi}$ grows linearly with $\tilde T$; the rate for a given set of final momenta is (Yu eq. (6.375))
>
> $$
> \frac{P_{fi}}{\tilde T} = \frac{(2\pi)^4\delta^4(p_A - p_f)\,|\mathcal M|^2}{2E_A\prod_j\bigl(2E_j\tilde V\bigr)} .
> $$
>
> **What the derivation shows.**
> - The linear growth in $\tilde T$ is what makes a rate meaningful, as for scattering ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]]) and for Fermi's golden rule ([[§C9.5 Fermi's Golden Rule#^thm-c9-5-1|QM Theorem §C9.5.1]]). $\tilde T \ll \tau$ keeps the probability small, so that the population of [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]] is not yet depleted.

^der-c6b-5-5

*Uses:* [[§C6b.5 Decay Widths#^thm-c6b-5-4|Theorem §C6b.5.4]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]]

> [!theorem] Theorem §C6b.5.6: The Decay Rate Formula
> For a particle $A$ of mass $m_A$ decaying at rest into $n$ particles,
>
> $$
> d\Gamma = \frac{1}{2m_A}\cdot|\mathcal M(p_A \to \{p_i\})|^2\cdot d\Pi_n , \qquad d\Pi_n = \prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\cdot(2\pi)^4\delta^4\Bigl(p_A - \sum_ip_i\Bigr) ,
> $$
>
> with $\mathcal M$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] for one particle in the initial state; the width into a final state with identical particles is $\Gamma = \frac{1}{S_{\rm id}}\int d\Gamma$.
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there (lowest order in the decaying interaction; [[§C6b.5 Decay Widths#^cau-c6b-5-1|Caution: Free states in a decay amplitude]]).
>
> *Source: PHY 513 Lecture 15, slide 22 ("Result for relativistic decay width: $d\Gamma = \frac{1}{2m_A}\cdot|\mathcal M|^2\cdot d\Pi_n$ with phase space factor for final $n$ particles: $d\Pi_n = \prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\cdot(2\pi)^4\delta^{(4)}(p_A - \sum_ip_i)$"), and transcript · the user's PHY 513 notes, Ch. 15 §15.8, Principle "Decay rate", eq. (dGamma) (stated, not derived, in the lecture: a theorem here, derived by Yu's route) · PS §4.5, eq. (4.86) · Yu §6.5.4, eqs. (6.373)–(6.377)*

^thm-c6b-5-6

> [!derivation]- Derivation (Yu's route: box normalization)
> The box of [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]: $(2\pi)^3\delta^3(\mathbf 0) = \tilde V$ and $(2\pi)^4\delta^4(0) = \int d^4x = \tilde V\tilde T$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]; Yu eq. (6.282)).
>
> **Steps 1–3** (the norms, the transition probability, the rate per unit time) are [[§C6b.5 Decay Widths#^thm-c6b-5-4|Theorem §C6b.5.4]] and [[§C6b.5 Decay Widths#^thm-c6b-5-5|Theorem §C6b.5.5]]: $R_{\{p_j\}} = (2\pi)^4\delta^4(p_A - \sum_jp_j)\,|\mathcal M|^2\big/\bigl[2E_A\prod_j(2E_j\tilde V)\bigr]$.
>
> **Step 4** (count the final states). In the box the momenta are discrete, $\mathbf p \in (2\pi/L)\mathbb Z^3$, one state per cell of volume $(2\pi/L)^3 = (2\pi)^3/\tilde V$, so a cell $d^3p_j$ contains $\tilde V\,d^3p_j/(2\pi)^3$ states (Yu eq. (6.302); [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|Theorem §C6b.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-10|Theorem §CA.3.10]]). Summing the rate over these states multiplies it by $\prod_j\tilde V\frac{d^3p_j}{(2\pi)^3}$, and the $n$ factors $\tilde V$ cancel the $n$ in the denominator:
>
> $$
> \prod_j\frac{\tilde V\,d^3p_j}{(2\pi)^3}\cdot\frac{1}{2E_A\prod_j(2E_j\tilde V)} = \frac{1}{2E_A}\prod_j\frac{d^3p_j}{(2\pi)^3\,2E_j} ,
> $$
>
> and
>
> $$
> dR = \frac{1}{2E_A}\prod_j\frac{d^3p_j}{(2\pi)^32E_j}\,(2\pi)^4\delta^4\Bigl(p_A - \sum_jp_j\Bigr)|\mathcal M|^2 = \frac{1}{2E_A}|\mathcal M|^2\,d\Pi_n .
> $$
>
> **Step 5** (rest frame; identical particles). For $A$ at rest $E_A = \sqrt{\mathbf 0^2 + m_A^2} = m_A$, and the rate is $d\Gamma$ of [[§C6b.5 Decay Widths#^def-c6b-5-1|Def. §C6b.5.1]]:
>
> $$
> d\Gamma = dR\big|_{E_A = m_A} = \frac{1}{2m_A}|\mathcal M|^2\,d\Pi_n , \qquad \Gamma = \frac{1}{S_{\rm id}}\int d\Gamma ,
> $$
>
> since integrating over all final momenta counts each state of identical particles $S_{\rm id}$ times ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]] in the box, [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]]; Yu eqs. (6.376)–(6.377)).
>
> ⚑ By-product: $[\Gamma] = 1$ for every $n$. With $N = 1 + n$, $[\mathcal M] = 4 - (1 + n) = 3 - n$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]) and $[d\Pi_n] = 2n - 4$ ([[§C6b.3 The Cross Section#^der-c6b-3-10|Derivation §C6b.3.10]], Step 2):
>
> $$
> [d\Gamma] = \Bigl[\frac{1}{2m_A}\Bigr] + 2[\mathcal M] + [d\Pi_n] = -1 + 2(3 - n) + (2n - 4) = 1 :
> $$
>
> the width is an energy, as the definition demands.
>
> ⚑ By-product: in a frame where $A$ moves, Step 4 gives, with $E_A = \gamma m_A$ and $|\mathcal M|^2d\Pi_n$ invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]], [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]]),
>
> $$
> dR = \frac{1}{2E_A}|\mathcal M|^2d\Pi_n = \frac{m_A}{E_A}\cdot\frac{1}{2m_A}|\mathcal M|^2d\Pi_n = \frac{1}{\gamma}\,d\Gamma ,
> $$
>
> smaller by $1/\gamma$: "in any other frame, this factor would give the usual time dilation" (PS p. 107) → [[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|Theorem §C6b.7.3]].
>
> **What the derivation shows.**
> - The decay formula is the cross-section formula with the initial-state factor of a single particle: $\frac{1}{2E_A}$ from its normalization, no flux; "the final phase space … just went on for the ride".
> - The box route squares a delta function, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$; the factors cancel, which is why the result is finite. A wave-packet derivation for one particle, as in [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]]–[[§C6b.9 Evaluating the Cross Section|§C6b.9]], is "similar" (slide 22) and was not done.
> - The decay is kinematically possible only if $m_A > \sum_im_i$ (Yu eq. (6.378)): in the rest frame $\delta^4(p_A - \sum p_i)$ requires $m_A = \sum_iE_i \ge \sum_im_i$, with equality only at $\mathbf p_i = 0$ for all $i$; otherwise the delta function has no support.

^der-c6b-5-6

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]], [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]], [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-5|P7, steps 5–6]]

## What the decay formula implies

<!-- NEW thm-c6b-5-7 -->

<!-- NEW thm-c6b-5-8 -->

<!-- NEW thm-c6b-5-9 -->

<!-- NEW thm-c6b-5-10 -->

> [!caution] Caution: Free states in a decay amplitude
> The user's solution: "The interaction does not switch off, so the free states are not exactly the asymptotic states; to lowest order in $\mu$ this does not matter, the corrections from external legs and the vacuum entering at higher order." For an unstable particle this is the subtlety PS raise (pp. 107–108; [[§C6b.5 Decay Widths#^cau-c6b-5-2|Caution: "Corollary of studying interacting wave function (2nd term)"]]); beyond lowest order the external legs carry $\sqrt Z$ and the physical mass ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]); "free" in the $S$-matrix means widely separated ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-1|§C6b.1, Caution: "Free" means widely separated]]).
>
> *Source: PHY 513, Problem Set 8, Problem 4 (the user's solution, paragraph "Amplitude")*

^cau-c6b-5-1

> [!remark] Remark: Reading the decay formula
> The final phase space is the same as for scattering: "this was kind of what you integrated over [in the] final state, and … just went on for the ride." Of the two $\delta^4$'s of the squared amplitude, "one of which is the overall delta that sits there, and you make it part of [the] final phase space". The initial-state factor is simpler: for scattering it was an inverse area because $\sigma$ is an area; for a decay it must turn $|\mathcal M|^2d\Pi_n$ into a rate, and in the rest frame the only quantity available is the mass: "It had to be relativistic[ally] in[variant]. It's the mass." $\frac{1}{2m_A}$ is the $\frac{1}{2E_A}$ of the normalization of $A$ with $E_A = m_A$.
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Reading the formula")*

^rem-c6b-5-2

> [!caution] Caution: "Corollary of studying interacting wave function (2nd term)"
> Slide 22 gives two routes to [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]]: "Derivation similar (wave packets, square amplitude, …)", or "Corollary of studying interacting wave function (2nd term)". The lecture explained the second: in an interacting theory a one-particle state is not just $\hat a^\dagger|0\rangle$ but "a dagger with all the rest stuff", and studying such states in detail, for other reasons, in the second term, produces the formula "kind of like for free". Concretely, an unstable particle's two-point function develops an imaginary part, and $\Gamma$ is read off from it (Yu eq. (10.265); ★ Remark: Yu's route to the width, below). Neither derivation is done in the course this term. A further subtlety (PS pp. 107–108): an unstable particle cannot be prepared in the infinitely distant past, so the definition of $\mathcal M$ through in and out states "makes no sense in this context"; the formula is nevertheless correct when $\mathcal M$ is computed with the Feynman rules ([[§C6c.1 Amplitudes from Correlation Functions|§C6c.1]]).
>
> *Source: PHY 513 Lecture 15, slide 22 (page image), and transcript · the user's PHY 513 notes, Ch. 15 §15.8, Caution "'Corollary of studying interacting wave function (2nd term)'" · PS §4.5, pp. 107–108*

^cau-c6b-5-2

## ★ Several decay channels

> [!theorem]- ★ Theorem §C6b.5.11: Partial Widths Add
> Let $A$ decay into final-state channels $f$ (distinct particle contents). The **partial width** of channel $f$ is $\Gamma_f = \frac{1}{S_{{\rm id},f}}\int d\Gamma_f$ with $d\Gamma_f$ of [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] for that channel, and the **branching ratio** is $B_f = \Gamma_f/\Gamma$. Then
>
> $$
> \Gamma = \sum_f\Gamma_f , \qquad \sum_fB_f = 1 , \qquad \tau = \frac1\Gamma = \frac{1}{\sum_f\Gamma_f} .
> $$
>
> *Model:* [[§C6b.5 Decay Widths#^mod-c6b-5-1|Model §C6b.5.1]]; *applies:* as there; each $\Gamma_f$ at the same order.
>
> *Source: Yu §6.5.4, eqs. (6.371)–(6.372) · PS §4.5, p. 101 ("the reciprocal of the sum of its decay rates into all possible final states") · not in the lecture*

^thm-c6b-5-11

> [!derivation]- Derivation
> **Step 1** (channels are orthogonal sectors). States of different particle content are orthogonal, and the identity on the states $A$ can decay into is $\mathbb 1 = \sum_f\mathbb 1_f$ with $\mathbb 1_f = \frac{1}{S_{{\rm id},f}}\int\prod_i\frac{d^3p_i}{(2\pi)^32E_i}|\mathbf p_1\cdots\rangle\langle\mathbf p_1\cdots|$ ([[§C6b.9 Evaluating the Cross Section#^der-c6b-9-4|Derivation §C6b.9.4]], Step 2).
>
> **Step 2** (rates add). The decay probability per unit time of [[§C6b.5 Decay Widths#^def-c6b-5-1|Def. §C6b.5.1]] is the sum over the sectors of Step 1 of the rate into each, which [[§C6b.5 Decay Widths#^der-c6b-5-6|Derivation §C6b.5.6]], Steps 3–5, computes sector by sector:
>
> $$
> \Gamma = \sum_f\frac{1}{S_{{\rm id},f}}\int\frac{1}{2m_A}|\mathcal M(A \to f)|^2\,d\Pi_{n_f} = \sum_f\Gamma_f .
> $$
>
> **Step 3** (branching ratios and lifetime). Divide by $\Gamma$: $\sum_fB_f = \sum_f\frac{\Gamma_f}{\Gamma} = \frac{\Gamma}{\Gamma} = 1$; and $\tau = 1/\Gamma$ ([[§C6b.5 Decay Widths#^def-c6b-5-1|Def. §C6b.5.1]]) $= 1/\sum_f\Gamma_f$.
>
> **What the derivation shows.**
> - The total width is a sum of independent channel widths because the final states of different channels are orthogonal; the lifetime is set by the sum, not by any one channel.

^der-c6b-5-11

*Uses:* [[§C6b.5 Decay Widths#^def-c6b-5-1|Def. §C6b.5.1]], [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]]

> [!remark]- Connections
> - The exponential decay law ([[§C6b.5 Decay Widths#^law-c6b-5-2|Law §C6b.5.2]]) and the lifetime are the decay constant of radioactive decay, and the width–lifetime relation is the natural line width of quantum mechanics — [[§A7.2 Radioactive Decay#^thm-a7-2-2|QM Theorem §A7.2.2]], [[§A3.5 The Heisenberg Uncertainty Principle#^def-a3-5-1|QM Def. §A3.5.1]].
<!-- CONN-5 -->
