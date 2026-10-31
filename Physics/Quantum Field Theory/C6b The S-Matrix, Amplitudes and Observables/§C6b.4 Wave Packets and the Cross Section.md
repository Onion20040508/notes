---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.1 The S-Matrix and the Invariant Amplitude]] · ↑ [[· C6b The S-Matrix, Amplitudes and Observables]] · [[§C6b.5 Evaluating the Cross Section]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.2 (paragraph "Event counting (filled in)", Definition "Classical differential cross section", Figure "classicalxsec", paragraph "Example: the hard sphere (filled in)"), §15.3 (Definition "Wave packets", eq. (twopacket), paragraph "Why $e^{-i\vec b\cdot\vec k_B}$ shifts $B$ by $+\vec b$ (filled in)", Figure "wavepackets", Caution "A slip on the wave-packet slide", eq. (Pb), Definition "The quantum cross section", paragraphs "Why integrate over $\vec b$ (filled in)", "Which final states (filled in)"), §15.4 (eq. (dsigmafull), paragraph "Counting", Derivations "The $\delta$-functions and the one Jacobian", "A $\delta$-function of a function (filled in)", Caution "$1/f'(0)$ on the slide", paragraphs "Integrating over $\bar k_B^z$ instead", "A second zero (filled in)", "Smoothness"), §15.5 (Principle "Cross section for $2\to n$ scattering", paragraph "Reading the formula", Derivation "Dimension check (filled in)", paragraph "Identical particles (filled in)") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part A, slide 8, Part B, slides 11–16, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 99–106 and 108, eqs. (4.59)–(4.61), (4.65)–(4.79) · Yu Zhao-Huan, 量子场论讲义, §6.5.1–§6.5.2, eqs. (6.276)–(6.313), (6.321).*

What an experiment observes is an event rate, and the cross section is that rate with the set-up divided out ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]]); classically it is an area in the plane of impact parameters ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-2|Def. §C6b.4.2]]). The goal is a quantum, relativistic formula for it in terms of the amplitude $\mathcal M$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]. Momentum eigenstates never "come in" from anywhere, and squaring amplitudes between them produces squares of delta functions; so the incoming particles are wave packets, one of them displaced by an impact parameter $\mathbf b$, and the probability of scattering is integrated over $\mathbf b$. This section sets up the definitions: the wave packets ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3|Def. §C6b.4.3]], [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-4|Def. §C6b.4.4]]), the scattering probability at fixed impact parameter ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5|Def. §C6b.4.5]]) and the quantum cross section ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6|Def. §C6b.4.6]]), what it counts ([[§C6b.4 Wave Packets and the Cross Section#^thm-c6b-4-4|Theorem §C6b.4.4]]) and which final states contribute ([[§C6b.4 Wave Packets and the Cross Section#^lem-c6b-4-5|Lemma §C6b.4.5]]). The integrals are done in [[§C6b.5 Evaluating the Cross Section|§C6b.5]], whose result is the cross-section formula [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-2|Theorem §C6b.5.2]].

*Conventions* ([[Larsen PHY 513]]): beams along the $z$-axis; $\perp$ marks the components $(x, y)$ transverse to it; $E_A \equiv E_{\mathbf k_A} = \sqrt{\mathbf k_A^2 + m_A^2}$ inside integrals and $E_A = E_{\mathbf p_A}$ in final formulas; $\mathbf v = \mathbf k/E$ is the velocity; barred momenta $\bar{\mathbf k}_A$, $\bar{\mathbf k}_B$ label the second, complex-conjugated copy of an amplitude.


## The cross section: a universal event rate

> [!definition] Definition §C6b.4.1: The Cross Section as a Universal Event Rate
> The observable of a scattering experiment is an event rate. The **cross section** $\sigma$ is a universal event rate: the rate with the factors of the experimental set-up divided out, independent of the set-up. For a beam of particles $B$ with flux $j_B$ (particles per unit area per unit time) on a target of $N_A$ particles $A$, the number of events in a time $t$ is
>
> $$
> N_{\rm events} = \sigma\,N_A\,j_B\,t ,
> $$
>
> so $\sigma$ has the dimension of an area. A separate, set-up-dependent step turns $\sigma$ back into a count of events.
>
> *Source: PHY 513 Lecture 15, slide 8 ("Observable in scattering experiment: event rate. Cross-section $= \sigma$: is a universal event rate. It is independent of experimental set-up."), and transcript ("how many clicks do you get per time … I mean divided by that … the cross section is that universal event rate") · the user's PHY 513 notes, Ch. 15 §15.2 (paragraph "Event counting (filled in)") · Yu §6.5.2, eq. (6.308) · PS §4.5, eqs. (4.59)–(4.61)*

^def-c6b-4-1

> [!definition] Definition §C6b.4.2: The Classical Differential Cross Section
> In classical, non-relativistic mechanics a particle aimed at the target with impact parameter $\mathbf b$ (its transverse offset from a head-on hit, an area element $d^2b$ in **impact-parameter space**) leaves in a definite direction. The differential cross section is the area giving scattering into $d\Omega$:
>
> $$
> \frac{d\sigma}{d\Omega} = \frac{d^2b}{d\Omega} .
> $$
>
> This is the classical-mechanics definition ([[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^def-b4-2-1|CM Def. §B4.2.1]], the number scattered into $d\Omega$ per unit time divided by the incident flux) rewritten with the deflection function ([[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^thm-b4-2-2|CM Theorem §B4.2.2]]).
>
> *Source: PHY 513 Lecture 15, slide 8 ("Definition in classical, non-relativistic mechanics: $\frac{d\sigma}{d\Omega}$ = area giving scattering into $d\Omega = \frac{d^2b}{d\Omega}$. $d^2b$ is an area in impact parameter space."), and transcript ("The cross section is literally what kind of area should you hit … if you want it out in this final angle") · the user's PHY 513 notes, Ch. 15 §15.2, eq. (classicalxsec)*

^def-c6b-4-2

The user's notes check the definition on the hard sphere, the example worked in Classical Mechanics:

![[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^thm-b4-2-4]]

![[ph-qft-c6-13-1.svg]]
*The classical cross section, here for a hard sphere of radius $R$ (the $a$ of CM Theorem §B4.2.4). Particles crossing the patch $d^2b$ of the impact-parameter plane leave into the solid angle $d\Omega$; a larger $b$ means a more glancing hit and a smaller deflection $\theta$, with $b = R\cos(\theta/2)$. Added figure, from the user's notes (Figure "classicalxsec").*

> [!remark] Remark: The goal: a quantum, relativistic version
> "What we want to do is to have a quantum and relativistic version of that, where it's not actually literally an area like that, but it's something that has the same properties." It should strip out "the kinematics of this situation and the quantum stuff with squared wave functions … that are completely universal. Nothing to do with the actual interaction", and leave a formula in terms of $\mathcal M$: "if you learn how to compute $M$ … you can compute the cross section." Quantum mechanics already did this for a fixed potential, with a transition rate divided by a probability current ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^def-c10-1-1|QM Def. §C10.1.1]]); the new features are two moving particles and relativistic kinematics.
>
> *Source: PHY 513 Lecture 15, slide 8 ("Goal: quantum, relativistic formula for $\frac{d\sigma}{d\Omega}$"), and transcript*

^rem-c6b-4-1

## Wave packets and the scattering probability

"You're telling me these initial particles have [definite] momentum … What is their position then? There was this Heisenberg business." A momentum eigenstate is spread over all space and is not normalizable ([[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]); by "momentum $\mathbf p$" we mean "as close as I can get to momentum $\mathbf p$".

> [!definition] Definition §C6b.4.3: Wave Packet
> A smeared initial state: the **wave packet** peaked at $\mathbf k = \mathbf p$ is
>
> $$
> |\phi_{\mathbf p}\rangle = \int\frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\mathbf k}}}\,\phi(\mathbf k)\,|\mathbf k\rangle , \qquad \int\frac{d^3k}{(2\pi)^3}\,|\phi(\mathbf k)|^2 = 1 ,
> $$
>
> with a smooth profile $\phi(\mathbf k)$ sharply peaked at $\mathbf k = \mathbf p$. It is the wave packet $|g\rangle$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]] with the profile $g(\mathbf k) = \sqrt{2E_{\mathbf k}}\,\phi(\mathbf k)$.
>
> *Source: PHY 513 Lecture 15, slide 11 ("Smeared initial state: wave packet peaked at $\vec k = \vec p$ … Normalization $\int\frac{d^3k}{(2\pi)^3}|\phi(\vec k)|^2 = 1$"), and transcript ("I'm going to take my energy normalizations and make them part of this") · the user's PHY 513 notes, Ch. 15 §15.3, eq. (wavepacket) · PS §4.5, eqs. (4.65)–(4.66)*

^def-c6b-4-3

> [!theorem] Theorem §C6b.4.2: The Normalization Condition Is the Unit Norm
> For the wave packet of [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3|Def. §C6b.4.3]],
>
> $$
> \langle\phi_{\mathbf p}|\phi_{\mathbf p}\rangle = \int\frac{d^3k}{(2\pi)^3}\,|\phi(\mathbf k)|^2 ,
> $$
>
> so the normalization of the profile is $\langle\phi_{\mathbf p}|\phi_{\mathbf p}\rangle = 1$: the factor $1/\sqrt{2E_{\mathbf k}}$ absorbs the relativistic normalization of $|\mathbf k\rangle$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.3 (the check after Definition "Wave packets") · PS §4.5, eq. (4.66)*

^thm-c6b-4-2

> [!derivation]- Derivation
> **Step 1** (two copies). With a second integration variable $\mathbf k'$ for the bra,
>
> $$
> \langle\phi_{\mathbf p}|\phi_{\mathbf p}\rangle = \int\frac{d^3k\,d^3k'}{(2\pi)^6}\,\frac{\phi^\ast(\mathbf k)\,\phi(\mathbf k')}{\sqrt{2E_{\mathbf k}\,2E_{\mathbf k'}}}\,\langle\mathbf k|\mathbf k'\rangle .
> $$
>
> **Step 2** (the overlap). Insert $\langle\mathbf k|\mathbf k'\rangle = 2E_{\mathbf k}(2\pi)^3\delta^3(\mathbf k - \mathbf k')$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) and do the $\mathbf k'$ integral with the delta function, $\mathbf k' = \mathbf k$, $E_{\mathbf k'} = E_{\mathbf k}$:
>
> $$
> \langle\phi_{\mathbf p}|\phi_{\mathbf p}\rangle = \int\frac{d^3k}{(2\pi)^3}\,\frac{\phi^\ast(\mathbf k)}{\sqrt{2E_{\mathbf k}}}\,2E_{\mathbf k}\int\frac{d^3k'}{(2\pi)^3}\,(2\pi)^3\delta^3(\mathbf k - \mathbf k')\,\frac{\phi(\mathbf k')}{\sqrt{2E_{\mathbf k'}}} = \int\frac{d^3k}{(2\pi)^3}\,\frac{\phi^\ast(\mathbf k)}{\sqrt{2E_{\mathbf k}}}\,2E_{\mathbf k}\,\frac{\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}} .
> $$
>
> **Step 3** (collect). $\frac{2E_{\mathbf k}}{\sqrt{2E_{\mathbf k}}\sqrt{2E_{\mathbf k}}} = 1$ and $\phi^\ast\phi = |\phi|^2$:
>
> $$
> \langle\phi_{\mathbf p}|\phi_{\mathbf p}\rangle = \int\frac{d^3k}{(2\pi)^3}\,|\phi(\mathbf k)|^2 .
> $$
>
> The pairing of δ with the smooth, rapidly decreasing profiles is a pairing of a tempered distribution with a test function ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], 1).
>
> **What the derivation shows.**
> - With the course's profile $\phi$, probabilities are computed with the plain measure $\frac{d^3k}{(2\pi)^3}$; with the profile $g = \sqrt{2E}\phi$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]] the same norm reads $\int\frac{d^3k}{(2\pi)^32E_{\mathbf k}}|g|^2$.

^der-c6b-4-2

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]

"Standard scattering: two particle initial state." Not a stationary situation: particle $A$ comes in along the $z$-axis, particle $B$ along a parallel line displaced transversely.

> [!definition] Definition §C6b.4.4: The Two-Packet Initial State
> With $A$ at impact parameter $\mathbf 0$ and $B$ shifted transversely by the **impact parameter** $\mathbf b \perp \hat{\mathbf z}$ relative to $A$, the initial state is
>
> $$
> |\phi_A\phi_B\rangle_{\rm in} = \int\frac{d^3k_A}{(2\pi)^3}\frac{d^3k_B}{(2\pi)^3}\;e^{-i\mathbf b\cdot\mathbf k_B}\;\frac{\phi_A(\mathbf k_A)}{\sqrt{2E_A}}\,\frac{\phi_B(\mathbf k_B)}{\sqrt{2E_B}}\;|\mathbf k_A\mathbf k_B\rangle_{\rm in} ,
> $$
>
> with profiles $\phi_A$ peaked at $\mathbf p_A$ and $\phi_B$ peaked at $\mathbf p_B$, each normalized as in [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-3|Def. §C6b.4.3]].
>
> *Source: PHY 513 Lecture 15, slide 11 ("Standard scattering: two particle initial state. B shifted transverse by $\vec b$ relative to A (which is at $\vec 0$)"; formula corrected, Caution below), and transcript ("A has impact parameter zero, and B is impact parameter $b$") · the user's PHY 513 notes, Ch. 15 §15.3, eq. (twopacket) · PS §4.5, eq. (4.68)*

^def-c6b-4-4

> [!caution] Caution: A slip on slide 11
> Slide 11 writes the $B$ factor as $\phi(\vec k_B)/\sqrt{2E_A}$. It is $\phi_B(\mathbf k_B)/\sqrt{2E_B}$: each packet carries its own energy, and the final formula has $2E_A\,2E_B$, not $(2E_A)^2$ (slides 13 and 16 have it right). The slide also uses one profile $\phi$ for both particles; $A$ and $B$ may have different profiles.
>
> *Source: PHY 513 Lecture 15, slide 11 (page image) · the user's PHY 513 notes, Ch. 15 §15.3, Caution "A slip on the wave-packet slide" · PS §4.5, eq. (4.68)*

^cau-c6b-4-1

> [!theorem] Theorem §C6b.4.3: The Phase Displaces the Packet by b
> Multiplying a momentum profile by $e^{-i\mathbf b\cdot\mathbf k}$ translates the packet by $+\mathbf b$ in space: if $\psi(\mathbf x) = \int\frac{d^3k}{(2\pi)^3}\,\phi(\mathbf k)\,e^{i\mathbf k\cdot\mathbf x}$, then the profile $e^{-i\mathbf b\cdot\mathbf k}\phi(\mathbf k)$ has position-space form $\psi(\mathbf x - \mathbf b)$. Equivalently, $e^{-i\mathbf b\cdot\hat{\mathbf P}}$ is the translation by $\mathbf b$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.3 (paragraph "Why $e^{-i\vec b\cdot\vec k_B}$ shifts $B$ by $+\vec b$ (filled in)") · PS §4.5, p. 103*

^thm-c6b-4-3

> [!derivation]- Derivation
> **Step 1** (substitute and combine the exponents). With $e^{-i\mathbf b\cdot\mathbf k}e^{i\mathbf k\cdot\mathbf x} = e^{i\mathbf k\cdot(\mathbf x - \mathbf b)}$,
>
> $$
> \int\frac{d^3k}{(2\pi)^3}\,\bigl[e^{-i\mathbf b\cdot\mathbf k}\phi(\mathbf k)\bigr]\,e^{i\mathbf k\cdot\mathbf x} = \int\frac{d^3k}{(2\pi)^3}\,\phi(\mathbf k)\,e^{i\mathbf k\cdot(\mathbf x - \mathbf b)} = \psi(\mathbf x - \mathbf b) ,
> $$
>
> the definition of $\psi$ at the point $\mathbf x - \mathbf b$.
>
> **Step 2** (the peak moves by $+\mathbf b$). If $|\psi|$ is largest at $\mathbf x_0$, then $|\psi(\mathbf x - \mathbf b)|$ is largest where $\mathbf x - \mathbf b = \mathbf x_0$, i.e. at $\mathbf x = \mathbf x_0 + \mathbf b$.
>
> **Step 3** (operator form). With $\hat{\mathbf P}|\mathbf k\rangle = \mathbf k|\mathbf k\rangle$, the exponential series gives $e^{-i\mathbf b\cdot\hat{\mathbf P}}|\mathbf k\rangle = e^{-i\mathbf b\cdot\mathbf k}|\mathbf k\rangle$, so on a packet
>
> $$
> e^{-i\mathbf b\cdot\hat{\mathbf P}}\int\frac{d^3k}{(2\pi)^3}\frac{\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}}|\mathbf k\rangle = \int\frac{d^3k}{(2\pi)^3}\frac{e^{-i\mathbf b\cdot\mathbf k}\phi(\mathbf k)}{\sqrt{2E_{\mathbf k}}}|\mathbf k\rangle :
> $$
>
> multiplying the profile by the phase is acting with $e^{-i\mathbf b\cdot\hat{\mathbf P}}$, the translation operator with the sign of [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]].
>
> **What the derivation shows.**
> - Since $\mathbf b \perp \hat{\mathbf z}$, $b^z = 0$, only $\mathbf k_B^\perp$ enters the phase: $\mathbf b\cdot\mathbf k_B = b^xk_B^x + b^yk_B^y + 0\cdot k_B^z = \mathbf b\cdot\mathbf k_B^\perp$. This is why the $\mathbf b$-integral of [[§C6b.5 Evaluating the Cross Section#^der-c6b-5-2|Derivation §C6b.5.2]], Step 1, constrains only the transverse momenta.

^der-c6b-4-3

*Uses:* [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]]

![[ph-qft-c6-13-2.svg]]
*The initial state of Def. §C6b.4.4: packet $A$ moves along the $z$-axis, packet $B$ along a parallel line displaced by the impact parameter $\mathbf b$. Each packet is localized in space and therefore smeared in momentum around $\mathbf p_A$ or $\mathbf p_B$. Drawn in the centre-of-mass frame; nothing in the derivation requires it. Added figure, from the user's notes (Figure "wavepackets"); PS Fig. 4.2 draws many $B$ packets at different $\mathbf b$.*

> [!definition] Definition §C6b.4.5: The Scattering Probability at Fixed Impact Parameter
> The probability of scattering into the final phase-space element $\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}$, for a particular impact parameter $\mathbf b$, is
>
> $$
> \mathcal P(\mathbf b) = \prod_{\text{final }i}\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\;\bigl|{}_{\rm out}\langle\mathbf p_1\mathbf p_2\cdots|\phi_A\phi_B\rangle_{\rm in}\bigr|^2 .
> $$
>
> *Source: PHY 513 Lecture 15, slide 12 ("Probability of scattering into final phase space $\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}$ … This is for a particular impact parameter $\vec b$"), and transcript ("we take these guys and we kind of expand into linear superposition of possible out states. Coefficient … is some amplitude, and that one we square") · the user's PHY 513 notes, Ch. 15 §15.3, eq. (Pb) · PS §4.5, eq. (4.74)*

^def-c6b-4-5

The measure in $\mathcal P(\mathbf b)$ is the one-particle completeness measure of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]; [[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-5|Theorem §C6b.5.5]] shows that the probabilities add up to one.

> [!definition] Definition §C6b.4.6: The Cross Section from the Scattering Probability
> The (differential) cross section is the scattering probability integrated over all impact parameters:
>
> $$
> d\sigma = \int d^2b\;\mathcal P(\mathbf b) .
> $$
>
> *Source: PHY 513 Lecture 15, slide 12 ("Total probability: $\int\mathcal P(\vec b)\,d^2\vec b$. Very quantum: all $d^2b$ contribute to scatter into given $d\Omega$."), slide 13 (the expression is called $d\sigma$), and transcript ("the total probability is the integral over that") · the user's PHY 513 notes, Ch. 15 §15.3, Definition "The quantum cross section", eq. (sigmab) · PS §4.5, eq. (4.75)*

^def-c6b-4-6

> [!theorem] Theorem §C6b.4.4: The Quantum Cross Section Is the Event Rate per Unit Flux
> Let the $B$ particles arrive at random transverse positions with density $n_B = j_Bt$ per unit area, constant over the range of $\mathbf b$ where $\mathcal P(\mathbf b) \ne 0$. Then the expected number of events per target particle in the final-state element of [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5|Def. §C6b.4.5]] is
>
> $$
> N_{\rm events} = n_B\int d^2b\;\mathcal P(\mathbf b) = d\sigma\;j_B\,t ,
> $$
>
> [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]] with $N_A = 1$ and $d\sigma$ of [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6|Def. §C6b.4.6]]. If $\mathcal P(\mathbf b) \in \{0, 1\}$ (classical trajectories), $d\sigma$ is the area of the set of impact parameters that end in $d\Omega$, [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-2|Def. §C6b.4.2]].
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.3 (paragraph "Why integrate over $\vec b$ (filled in)") · PS §4.5, p. 105 · PHY 513 Lecture 15, slide 12, and transcript*

^thm-c6b-4-4

> [!derivation]- Derivation
> **Step 1** (sum over the incident particles). Each $B$ particle $i$, at impact parameter $\mathbf b_i$, scatters into the element with probability $\mathcal P(\mathbf b_i)$; the expected number of events is the sum, and the expected number of $B$ particles in $d^2b$ is $n_B\,d^2b$:
>
> $$
> N_{\rm events} = \Bigl\langle\sum_{\text{incident }i}\mathcal P(\mathbf b_i)\Bigr\rangle = \int d^2b\;n_B\,\mathcal P(\mathbf b) = n_B\int d^2b\;\mathcal P(\mathbf b) ,
> $$
>
> $n_B$ taken out of the integral because it is constant where $\mathcal P \ne 0$.
>
> **Step 2** (insert the definitions). $\int d^2b\,\mathcal P(\mathbf b) = d\sigma$ ([[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6|Def. §C6b.4.6]]) and $n_B = j_Bt$ (particles per area = flux × time):
>
> $$
> N_{\rm events} = d\sigma\cdot j_B\,t = d\sigma\cdot N_A\cdot j_B\,t\big|_{N_A = 1} .
> $$
>
> **Step 3** (classical limit). If $\mathcal P(\mathbf b) = 1$ for $\mathbf b \in R$ (the impact parameters whose trajectories end in $d\Omega$) and $0$ otherwise,
>
> $$
> d\sigma = \int d^2b\;\mathcal P(\mathbf b) = \int_Rd^2b = \operatorname{area}(R) ,
> $$
>
> the $d^2b$ of $\frac{d\sigma}{d\Omega} = \frac{d^2b}{d\Omega}$.
>
> **What the derivation shows.**
> - Integrating over $\mathbf b$ is what turns a probability into an area. Quantum mechanically every $\mathbf b$ contributes with its weight $\mathcal P(\mathbf b) \in [0, 1]$; the lecture calls it "very quantum": "it's not a specific $d^2b$ that gives me into my particular final … angle. It's all of them. All of them with a certain probability."

^der-c6b-4-4

*Uses:* [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-1|Def. §C6b.4.1]], [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-2|Def. §C6b.4.2]], [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-5|Def. §C6b.4.5]], [[§C6b.4 Wave Packets and the Cross Section#^def-c6b-4-6|Def. §C6b.4.6]]

> [!theorem] Lemma §C6b.4.5: Away from the Forward Direction Only iT̂ Contributes
> If the final particles differ from the initial ones in number or species, or have momenta $\{\mathbf p_1, \mathbf p_2\} \ne \{\mathbf k_A, \mathbf k_B\}$, then
>
> $$
> {}_{\rm out}\langle\mathbf p_1\mathbf p_2\cdots|\mathbf k_A\mathbf k_B\rangle_{\rm in} = \langle\mathbf p_1\mathbf p_2\cdots|i\hat T|\mathbf k_A\mathbf k_B\rangle = (2\pi)^4\delta^4\Bigl(k_A + k_B - \sum_ip_i\Bigr)\,i\mathcal M .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.3 (paragraph "Which final states (filled in)") · PS §4.5, p. 105 ("we can drop the $\mathbf 1$")*

^lem-c6b-4-5

> [!derivation]- Derivation
> **Step 1** (split $\hat S$). By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]] and [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]],
>
> $$
> {}_{\rm out}\langle\mathbf p_1\mathbf p_2\cdots|\mathbf k_A\mathbf k_B\rangle_{\rm in} = \langle\mathbf p_1\mathbf p_2\cdots|\hat S|\mathbf k_A\mathbf k_B\rangle = \langle\mathbf p_1\mathbf p_2\cdots|\mathbf k_A\mathbf k_B\rangle + \langle\mathbf p_1\mathbf p_2\cdots|i\hat T|\mathbf k_A\mathbf k_B\rangle .
> $$
>
> **Step 2** (the "1" term). States with different particle numbers or species are orthogonal, so the first term is 0 unless the final state has two particles of the species of $A$, $B$. Then, for $A$, $B$ of one species ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], factors $\sqrt{2E}$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]),
>
> $$
> \langle\mathbf p_1\mathbf p_2|\mathbf k_A\mathbf k_B\rangle = 2E_{\mathbf k_A}2E_{\mathbf k_B}(2\pi)^6\bigl[\delta^3(\mathbf p_1 - \mathbf k_A)\delta^3(\mathbf p_2 - \mathbf k_B) + \delta^3(\mathbf p_1 - \mathbf k_B)\delta^3(\mathbf p_2 - \mathbf k_A)\bigr] ,
> $$
>
> (one term only if $A \ne B$), which vanishes unless $\{\mathbf p_1, \mathbf p_2\} = \{\mathbf k_A, \mathbf k_B\}$.
>
> **Step 3** (the amplitude). The remaining term is [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]].
>
> **What the derivation shows.**
> - "Assuming that we are not interested in the trivial case of forward scattering where no interaction takes place, we can drop the $\mathbf 1$" (PS p. 105): measured final states are always of this kind (away from the forward direction, or different particles).

^der-c6b-4-5

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-2|Def. §C6b.1.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]

> [!caution] Caution: "Total probability" is an area
> Slide 12 calls $\int\mathcal P(\mathbf b)\,d^2b$ the "total probability"; slide 13 starts the computation of the same expression under the name $d\sigma$. $\mathcal P(\mathbf b)$ is a probability, but its integral over the plane of impact parameters has the dimension of an area: it is the probability summed over impact parameters at unit density, the cross section, not a probability ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-3|Theorem §C6b.5.3]]). The user's notes and PS (4.75) call it the cross section.
>
> *Source: PHY 513 Lecture 15, slides 12–13 (page images) · PS §4.5, p. 105, eq. (4.75)*

^cau-c6b-4-2

> [!remark]- Connections
> - The quantum cross section keeps the classical number, an area, and changes its meaning from a count of trajectories to an integral of probabilities over impact parameters; quantum mechanics made the same step with a probability current — [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^def-b4-2-1|CM Def. §B4.2.1]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^def-c10-1-1|QM Def. §C10.1.1]].
> - The wave packets are the honest states of [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]]: there, $|\mathbf p\rangle$ is a distribution and only packets are states; here that is exactly what removes the $\delta^4(0)$ — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]].
