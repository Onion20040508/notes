---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6a
section: C6a.0
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.9 Spin and Statistics]] · ↑ [[· C6a Interactions and Correlation Functions]] · [[§C6a.1 From Free to Interacting Fields]] →

*Sources: S. Coleman, Lectures of Sidney Coleman on QFT (Harvard 253a, 1986), arXiv:1110.5013, pp. 73–74 ("low budget scattering theory"), pp. 79–80 (the three models), p. 86, pp. 89–97 (Model 1 solved, Model 2), pp. 100–102 (Model 3, mass counterterms), pp. 140–141, 144, 151–154 (the three meanings of a blob), pp. 155, 158 (the physical vacuum) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.4, pp. 32–33, eq. (2.65); §4.2, p. 82, p. 86, eq. (4.27); §4.5, p. 99, p. 102, pp. 107–108; §4.6, p. 111; §7.2, p. 229; Problem 4.1, pp. 126–127 · Yu Zhao-Huan, 量子场论讲义, §6.2, p. 216; §6.5.1, eq. (6.284); §10.1, eq. (10.4), p. 440; §10.4, eq. (10.171), p. 463; §10.5.2, p. 474 · M. D. Schwartz, Quantum Field Theory and the Standard Model, §6.1, p. 69; §6.2, p. 75; §7.1, pp. 81, 83–84, eq. (7.26) · M. Srednicki, Quantum Field Theory (2006 draft), §5, pp. 51–52, 55, eq. (5.25); §10, p. 88; §11, p. 100 · PHY 513, Problem Set 8, Problems 1–4 (statements; the user's solution, submitted 2026-10-30) · PHY 513 Lectures 13 and 15 (Larsen, 14 and 28 Oct 2026).*

**The question this note answers.** A problem asks, in words, for a probability, a rate, a cross section or a correlation function. Before any formula: *what is being observed, and from which setup do we get there?* The setup fixes three things, and every formula of C6a and C6b holds only for the right choice of all three: **the states** (free Fock states of $\hat H_0$, or in and out states of the full $\hat H$, and in which normalization), **the vacuum** (the free vacuum $|0\rangle$ or the interacting vacuum $|\Omega\rangle$), and **the applicable theory** (exact, lowest order, or only with assumptions about the spectrum). The setup is decided by one physical fact: **how the interaction behaves in time.** This note classifies the physical situations by that fact (three models, after Coleman), says which vacuum and which states each one has and why, and then turns questions as asked into the object to compute. It is not a chain of formulas; the formulas are in the sections it points to.

*Conventions* ([[Larsen PHY 513]]): $|0\rangle$ is the free vacuum, $\hat H_0|0\rangle = 0$; $|\Omega\rangle$ the interacting vacuum ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]; other books' names: [[§C6a.0 Setups and Observables#^cau-c6a-0-1|Caution: Names for the vacua]]); relativistic states $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) unless a model says otherwise; a source enters as $\mathcal L_{\rm int} = j\phi$, $\hat H_{\rm int}(t) = -\int d^3x\,j(t, \mathbf x)\,\hat\phi_S(\mathbf x)$; $\tilde j(k) = \int d^4x\,e^{ik\cdot x}j(x)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]), and for a static source $\tilde j(\mathbf k) = \int d^3x\,e^{-i\mathbf k\cdot\mathbf x}j(\mathbf x)$. Coleman's coupling $-g\rho\phi$ is $j = -g\rho$.

## Three kinds of physical situation

| situation | how $\hat H$ depends on time | Hamiltonian at early and late times | asymptotic vacuum | model |
|---|---|---|---|---|
| an external apparatus acts for a finite time | $\hat H(t) = \hat H_0 + \hat H_{\rm int}(t)$, $\hat H_{\rm int}(t) = 0$ for $t \notin [t_1, t_2]$ | $\hat H_0$ | $\lvert0\rangle$, exactly | [[§C6a.0 Setups and Observables#^mod-c6a-0-1\|Model §C6a.0.1]] |
| an external apparatus acts for ever, unchanged | $\hat H = \hat H_0 + \hat H_{\rm int}$, $\hat H_{\rm int}$ linear in $\hat\phi$, time independent | $\hat H$ (switching put in by hand) | $\lvert\Omega\rangle \ne \lvert0\rangle$ | ★ [[§C6a.0 Setups and Observables#^mod-c6a-0-2\|Model §C6a.0.2]] |
| the fields act on each other | $\hat H = \hat H_0 + \hat H_{\rm int}$, $\hat H_{\rm int}$ nonlinear in the fields, time independent | $\hat H$ | $\lvert\Omega\rangle \ne \lvert0\rangle$ | [[§C6a.0 Setups and Observables#^mod-c6a-0-3\|Model §C6a.0.3]] |

Coleman's sentence for the first row: "Unless the interaction is with some externally specified apparatus, interesting Hamiltonians and the real world Hamiltonian are not of this form" (p. 73). The first question to ask of every problem is therefore: **does the interaction switch off?**

## The model ladder

> [!model] Model §C6a.0.1: A Free Field and a Source Switched Off at Early and Late Times
> A free real scalar field and a prescribed real c-number source $j(x)$, smooth and of compact support in spacetime:
>
> $$
> \mathcal L = \tfrac12(\partial_\mu\phi)^2 - \tfrac12m^2\phi^2 + j\phi , \qquad \hat H(t) = \hat H_0 - \int d^3x\,j(t, \mathbf x)\,\hat\phi_S(\mathbf x) , \qquad j(t, \mathbf x) = 0 \ \text{ for } t \notin [t_1, t_2] .
> $$
>
> *Assumptions:* the source is external and classical; it acts on the field and the field does not act back on it. This is [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]] written as a Hamiltonian ($\mathcal L_{\rm int} = j\phi$ has no derivatives, so $\mathcal H_{\rm int} = -j\phi$); the setup is the same, and Problem Set 8 states it so: "$j(x)$ is nonvanishing only during a finite interval of time, so that asymptotic in and out states can be defined."
>
> *Applies:* **exactly**, to all orders in $j$: $\hat H(t) = \hat H_0$ before $t_1$ and after $t_2$; the in and out vacuum is $|0\rangle$ and the in and out states are the free Fock states $\hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}|0\rangle$; $\hat S = U(+\infty, -\infty) = U(t_2, t_1)$; probabilities are $|\langle f|\hat S|0\rangle|^2$ with no denominator ([[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]], 1). Observables: $P(n)$, $\bar N$, the radiated energy and momentum. Two exact routes: the Heisenberg field with $D_R$ ([[§C2b.8 Particle Production by a Classical Source|§C2b.8]]) and the Dyson series with source vertices ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]]). Nothing is renormalized.
>
> *Source: Coleman pp. 79 ("Model 1 … $\rho(x) \to 0$ as $x \to \infty$ in space or time … a bunch of independent forced harmonic oscillators"), 86 ("we don't have to insert a turning on and off function because the interaction goes to zero as $x \to \infty$ in any direction and in particular in the time direction"), 89–91 (solved: $P_n$ Poisson, coherent state, $\langle N\rangle$, $\langle H\rangle$, $\langle\mathbf P\rangle$) · PS §2.4, pp. 32–33 ("nonzero only for a finite time interval"); Problem 4.1 · PHY 513, Problem Set 8, Problem 3*

^mod-c6a-0-1

> [!model]- ★ Model §C6a.0.2: A Free Field and a Static Source
> The same field with a source that does not depend on time, localized in space, $j(\mathbf x) \to 0$ for $|\mathbf x| \to \infty$:
>
> $$
> \hat H = \hat H_0 - \int d^3x\,j(\mathbf x)\,\hat\phi_S(\mathbf x) , \qquad \hat H_{\rm sw}(t) = \hat H_0 + f(t)\Bigl[-\int d^3x\,j(\mathbf x)\,\hat\phi_S(\mathbf x) - a\Bigr] ,
> $$
>
> where $f(t)$ switches the interaction on and off adiabatically ($f = 1$ for a time $\tilde T$, ramps of duration $\Delta$; limits $\Delta \to \infty$, $\tilde T \to \infty$, $\Delta/\tilde T \to 0$, Coleman p. 74) and the constant $a$ is a counterterm.
>
> *Assumptions:* as in [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]], but the source never switches off: "you might think this time independent problem would be easier … but it isn't because the source does not turn off as $|t| \to \infty$" (Coleman p. 79).
>
> *Applies* (beyond the course; results quoted from Coleman, not used in C6):
> - $|0\rangle$ is not the ground state. Completing the square gives the exact ground state, a coherent state ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]] with $\eta_{\mathbf p} = \tilde j(\mathbf p)/E_{\mathbf p}$), and its energy:
>
> $$
> |\Omega\rangle = e^{-\frac12\int\frac{d^3p}{(2\pi)^3}|\alpha_{\mathbf p}|^2}\,e^{\int\frac{d^3p}{(2\pi)^3}\alpha_{\mathbf p}\hat a^\dagger_{\mathbf p}}|0\rangle , \qquad \alpha_{\mathbf p} = \frac{\tilde j(\mathbf p)}{E_{\mathbf p}\sqrt{2E_{\mathbf p}}} , \qquad E_0 = -\frac12\int\frac{d^3p}{(2\pi)^3}\,\frac{|\tilde j(\mathbf p)|^2}{\mathbf p^2 + m^2} .
> $$
>
> - Without the counterterm the free vacuum persists only up to a divergent phase, $\langle0|U(+\infty, -\infty)|0\rangle = e^{-i(\gamma_+ + \gamma_- + E_0\tilde T)}$, "This is disgusting. A divergent phase" (p. 92); $a = E_0$ makes $\langle0|\hat S|0\rangle = 1$ (pp. 92–93).
> - $\hat S = \mathbb 1$: a static source has $\tilde j(k) = 2\pi\delta(k^0)\,\tilde j(\mathbf k)$, and a particle needs $k^0 = E_{\mathbf k} \ge m > 0$; "A time independent source can impart no energy" (p. 94).
> - Two point sources $j = g[\delta^3(\mathbf x - \mathbf y_1) + \delta^3(\mathbf x - \mathbf y_2)]$: the $\mathbf y$-dependent part of $E_0$ is the **Yukawa potential** $V(r) = -\frac{g^2}{4\pi r}e^{-mr}$, $r = |\mathbf y_1 - \mathbf y_2|$ (pp. 95–96); the ground state in the free basis is $\langle\mathbf k_1\cdots\mathbf k_n|\Omega\rangle$, obtained by switching on slowly and off abruptly and reusing Model 1 (pp. 96–97).
>
> *Source: Coleman pp. 79, 91–97 ("Model 2", "mesostatics")*

^mod-c6a-0-2

> [!derivation]- ★ Derivation (the ground state and $E_0$)
> **Step 1** (the interaction in modes). With the mode expansion at $t = 0$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]) and $\int d^3x\,j(\mathbf x)\,e^{i\mathbf p\cdot\mathbf x} = \tilde j(-\mathbf p) = \tilde j(\mathbf p)^\ast$ ($j$ real):
>
> $$
> -\int d^3x\,j(\mathbf x)\,\hat\phi_S(\mathbf x) = -\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\tilde j(\mathbf p)^\ast\,\hat a_{\mathbf p} + \tilde j(\mathbf p)\,\hat a^\dagger_{\mathbf p}\Bigr) .
> $$
>
> **Step 2** (completing the square). With $\hat H_0 = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$ and $\alpha_{\mathbf p}$ as above, so that $E_{\mathbf p}\alpha_{\mathbf p} = \tilde j(\mathbf p)/\sqrt{2E_{\mathbf p}}$:
>
> $$
> E_{\mathbf p}(\hat a^\dagger_{\mathbf p} - \alpha_{\mathbf p}^\ast)(\hat a_{\mathbf p} - \alpha_{\mathbf p}) = E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \frac{\tilde j(\mathbf p)}{\sqrt{2E_{\mathbf p}}}\hat a^\dagger_{\mathbf p} - \frac{\tilde j(\mathbf p)^\ast}{\sqrt{2E_{\mathbf p}}}\hat a_{\mathbf p} + E_{\mathbf p}|\alpha_{\mathbf p}|^2 ,
> $$
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,\hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + E_0 , \qquad \hat b_{\mathbf p} = \hat a_{\mathbf p} - \alpha_{\mathbf p} , \qquad E_0 = -\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}|\alpha_{\mathbf p}|^2 = -\int\frac{d^3p}{(2\pi)^3}\frac{|\tilde j(\mathbf p)|^2}{2E_{\mathbf p}^2} ,
> $$
>
> and $E_{\mathbf p}^2 = \mathbf p^2 + m^2$. $[\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, so $\hat H - E_0 \ge 0$ with equality exactly on the state annihilated by every $\hat b_{\mathbf p}$.
>
> **Step 3** (the ground state). $\hat b_{\mathbf p}|\Omega\rangle = 0$ means $\hat a_{\mathbf p}|\Omega\rangle = \alpha_{\mathbf p}|\Omega\rangle$, solved by the coherent state above ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]), and
>
> $$
> \langle0|\Omega\rangle = e^{-\frac12\int\frac{d^3p}{(2\pi)^3}|\alpha_{\mathbf p}|^2} < 1 \qquad (j \ne 0) .
> $$
>
> **What the derivation shows.** A source that never switches off moves the ground state: $|\Omega\rangle \ne |0\rangle$ and $E_0 < 0$, even though the field is free. The same coherent-state structure as in Model 1 appears, now as the vacuum instead of the final state.

^der-c6a-0-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]

> [!model] Model §C6a.0.3: A Self-Interacting Field
> Fields with a polynomial interaction without derivatives that never switches off:
>
> $$
> \hat H = \hat H_0 + \hat H_{\rm int} , \qquad \hat H_{\rm int} = \int d^3x\,\mathcal H_{\rm int}(\hat\phi_S(\mathbf x)) , \qquad \mathcal H_{\rm int} = -\mathcal L_{\rm int} , \qquad \hat H \text{ independent of } t .
> $$
>
> Instances in C6:
>
> | theory | $\mathcal L_{\rm int}$ | home |
> |---|---|---|
> | $\phi^4$ | $-\frac{\lambda}{4!}\phi^4$ | [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1\|Model §C6a.1.1]] |
> | cubic–quartic | $-\frac{g}{3!}\phi^3 - \frac{\lambda}{4!}\phi^4$ | [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-3\|Example §C6b.8.3]] (Problem Set 8, Problem 2) |
> | complex $(\phi^\dagger\phi)^2$ | $-\frac{\lambda}{4}(\phi^\dagger\phi)^2$ | [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-7\|Example §C6a.9.7]] (Problem Set 8, Problem 1(b)) |
> | two fields, $\Phi\phi^2$ | $-\mu\,\Phi\phi^2$ | [[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1\|Example §C6b.7.1]] (Problem Set 8, Problem 4) |
>
> *Assumptions:*
> 1. $\hat H$ has a unique ground state $|\Omega\rangle$, $\hat H|\Omega\rangle = E_0|\Omega\rangle$, separated by a gap $\Delta > 0$ from the rest of the spectrum, with $\langle\Omega|0\rangle \ne 0$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]; PS p. 86).
> 2. The one-particle states form isolated mass hyperbolas $p^2 = m^2$ below the two-particle continuum, with no bound states (Srednicki pp. 51–52), and the particles of the in and out states are stable.
> 3. The couplings are small, so that $\lambda = 0$ is a good starting point ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]); the potential is bounded below ($\lambda > 0$; a pure $\phi^3$ is not, PS p. 77).
>
> *Applies:*
> - **Correlation functions, exactly** (given 1): $\langle\Omega|T\{\hat\phi_H\cdots\hat\phi_H\}|\Omega\rangle$ is the ratio of free vacuum values with $T \to \infty(1 - i\varepsilon)$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7|Theorem §C6a.4.7]]), evaluated by Wick's theorem as a power series. The vacuum is $|\Omega\rangle$, never $|0\rangle$ ([[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]], 2).
> - **Scattering**: $\hat S$ is defined between in and out states of $\hat H$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-1|Def. §C6b.1.1]]), not between free states. Computing $\langle f|U(T, -T)|i\rangle$ with free states $\sqrt{2E}\,\hat a^\dagger\cdots|0\rangle$ and keeping the fully connected, amputated diagrams is valid **at lowest order only** ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-1|Theorem §C6b.1.1]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]); beyond it each external particle carries $\sqrt Z$ and the physical mass ([[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-2|§C6b.8, Caution: The rule is stated at lowest order]]).
> - **Decays**: an unstable particle violates assumption 2, so the decay formula is used beyond the stated scope ([[§C6b.7 Decay Rates and Widths#^cau-c6b-7-1|§C6b.7, Caution: Free states in a decay amplitude]]).
>
> *Source: Coleman p. 80 (his Model 3 is the meson–"nucleon" theory $g\psi^\ast\psi\phi$, one instance of this setup), p. 92 ("The particles interact with themselves and they can never get away from that as a particle can get away from an external potential"), pp. 100–102 (mass counterterms fixed by $\langle0|\hat S|0\rangle = 1$ and one-particle states that "shouldn't do anything") · PS §4.2, p. 82, p. 86; §7.2, p. 229 ("The $Z$ factors are irrelevant for calculations at the leading order of perturbation theory") · Yu §10.5.2, p. 474 (at leading order one may take $Z = 1$, $\delta m^2 = 0$, which justifies the leading-order methods of ch. 7–9) · Srednicki §5, pp. 51–52, 55 (eq. (5.25): "The LSZ formula is valid provided that …"); §11, p. 100 ("Strictly speaking, then, the LSZ formula is not applicable")*

^mod-c6a-0-3

## Which vacuum, and why

> [!theorem] Theorem §C6a.0.4: The Free Vacuum Is Exact Only When the Interaction Switches Off
> 1. *Model §C6a.0.1.* If $j = 0$ for $t \notin [t_1, t_2]$, then
>
> $$
> \hat H(t) = \hat H_0 \ (t < t_1,\ t > t_2), \qquad \hat S = U(+\infty, -\infty) = U(t_2, t_1), \qquad P(f) = |\langle f|\hat S|0\rangle|^2, \qquad \sum_fP(f) = \langle0|\hat S^\dagger\hat S|0\rangle = 1 ,
> $$
>
> for normalized eigenstates $|f\rangle$ of $\hat H_0$ (a complete set, with the measure of [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-6|Theorem §C6b.9.6]] for plane waves): $|0\rangle$ is the in and the out vacuum, and no vacuum normalization is divided out.
> 2. *Model §C6a.0.3, $\phi^4$.* $\hat H$ does not depend on time and $|0\rangle$ is not an eigenstate of it:
>
> $$
> \langle\mathbf p_1\mathbf p_2\mathbf p_3\mathbf p_4|\,\hat H\,|0\rangle = \lambda\,(2\pi)^3\delta^3(\mathbf p_1 + \mathbf p_2 + \mathbf p_3 + \mathbf p_4) \ne 0 ,
> $$
>
> so $|\Omega\rangle \ne |0\rangle$, $|\langle0|\Omega\rangle| < 1$, and the free vacuum does not persist: $\langle0|U(T, -T)|0\rangle \to e^{-2iE_0T}|\langle0|\Omega\rangle|^2$ as $T \to \infty(1 - i\varepsilon)$ ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]]). Every correlator needs the ratio of [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6|Theorem §C6a.4.6]].
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] (part 1), [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]] (part 2); *applies:* part 1 exactly; part 2 exactly, for every $\lambda \ne 0$ (as a statement about the regularized Hamiltonian; the delta function is a distribution in the momenta).
>
> *Source: Coleman pp. 73, 86, 92 · PS §4.2, p. 82 ("generally different from $|0\rangle$"), p. 86 · the setup paragraph of [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]] · PHY 513, Problem Set 8, Problem 3 (statement)*

^thm-c6a-0-4

> [!derivation]- Derivation
> **Part 1.**
>
> **Step 1** (the Hamiltonian at early and late times). For $t \notin [t_1, t_2]$, $\hat H_{\rm int}(t) = -\int d^3x\,j(t, \mathbf x)\hat\phi_S(\mathbf x) = 0$, so $\hat H(t) = \hat H_0$, and in the interaction picture ([[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]])
>
> $$
> \hat H_I(t) = e^{i\hat H_0t}\,\hat H_{\rm int}(t)\,e^{-i\hat H_0t} = 0 \qquad (t \notin [t_1, t_2]) .
> $$
>
> **Step 2** (the evolution operator). $U(t, t') = T\{\exp[-i\int_{t'}^tdt''\,\hat H_I(t'')]\}$ ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]); the integrand vanishes outside $[t_1, t_2]$, so $U(t, t') = \mathbb 1$ for $t' < t \le t_1$ and for $t_2 \le t' < t$. For $t' < t_1$, $t > t_2$, by the composition law ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]),
>
> $$
> U(t, t') = U(t, t_2)\,U(t_2, t_1)\,U(t_1, t') = U(t_2, t_1) \equiv \hat S ,
> $$
>
> independent of $t$ and $t'$: the limits $t \to +\infty$, $t' \to -\infty$ are reached at finite times.
>
> **Step 3** (the Schrödinger state). The Schrödinger-picture state is $|\psi(t)\rangle_S = e^{-i\hat H_0t}U(t, t')e^{i\hat H_0t'}|\psi(t')\rangle_S$. Start in the free vacuum, $|\psi(t')\rangle_S = |0\rangle$, $\hat H_0|0\rangle = 0$, the ground state of $\hat H(t') = \hat H_0$:
>
> $$
> |\psi(t)\rangle_S = e^{-i\hat H_0t}\,\hat S\,|0\rangle \qquad (t > t_2) .
> $$
>
> **Step 4** (the probabilities). For $\hat H_0|f\rangle = E_f|f\rangle$, $\langle f|f\rangle = 1$: $\langle f|\psi(t)\rangle_S = e^{-iE_ft}\langle f|\hat S|0\rangle$, so
>
> $$
> P(f) = |\langle f|\psi(t)\rangle_S|^2 = |\langle f|\hat S|0\rangle|^2 ,
> $$
>
> the same at every $t > t_2$: $|f\rangle$ is an eigenstate of the Hamiltonian $\hat H_0$ that acts after $t_2$, so the probability is final.
>
> **Step 5** (no denominator). $\hat S$ is unitary ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]]) and the eigenstates of $\hat H_0$ are complete, $\mathbb 1 = \sum_f|f\rangle\langle f|$:
>
> $$
> \sum_fP(f) = \sum_f\langle0|\hat S^\dagger|f\rangle\langle f|\hat S|0\rangle = \langle0|\hat S^\dagger\hat S|0\rangle = \langle0|0\rangle = 1 .
> $$
>
> In particular $\langle0|\hat S|0\rangle$ is itself the physical amplitude $\mathcal A(0)$ of [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-1|Theorem §C6b.9.1]], with $|\mathcal A(0)| \le 1$, and nothing is divided by it.
>
> **Part 2.**
>
> **Step 6** ($\hat H$ on the free vacuum). $\hat H_0|0\rangle = 0$ and $\hat H_{\rm int} = \frac{\lambda}{4!}\int d^3x\,\hat\phi_S(\mathbf x)^4$ ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]]), so $\hat H|0\rangle = \hat H_{\rm int}|0\rangle$.
>
> **Step 7** (the four-particle component). $\hat\phi_S(\mathbf x) = \hat\phi_I(0, \mathbf x) = \hat\phi^+ + \hat\phi^-$ ([[§C6a.2 The Interaction Picture#^def-c6a-2-1|Def. §C6a.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]). Each $\hat\phi^-$ adds one particle and each $\hat\phi^+$ removes one, so of the $2^4$ terms of $(\hat\phi^+ + \hat\phi^-)^4$ only $(\hat\phi^-)^4$ takes $|0\rangle$ to four particles; by [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]] (relativistic form, its derivation Step 1) at $x = (0, \mathbf x)$,
>
> $$
> \langle\mathbf p_1\mathbf p_2\mathbf p_3\mathbf p_4|\,\hat\phi_S(\mathbf x)^4\,|0\rangle = \langle\mathbf p_1\cdots\mathbf p_4|\,\bigl(\hat\phi^-(0, \mathbf x)\bigr)^4|0\rangle = \sum_{\sigma\in S_4}\prod_{i=1}^4e^{-i\mathbf p_i\cdot\mathbf x} = 4!\,e^{-i(\mathbf p_1 + \mathbf p_2 + \mathbf p_3 + \mathbf p_4)\cdot\mathbf x} .
> $$
>
> **Step 8** (the space integral). $\int d^3x\,e^{-i\mathbf q\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf q)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]):
>
> $$
> \langle\mathbf p_1\cdots\mathbf p_4|\,\hat H\,|0\rangle = \frac{\lambda}{4!}\cdot4!\cdot(2\pi)^3\delta^3(\mathbf p_1 + \cdots + \mathbf p_4) = \lambda\,(2\pi)^3\delta^3(\mathbf p_1 + \cdots + \mathbf p_4) .
> $$
>
> **Step 9** (not an eigenstate). If $\hat H|0\rangle = E|0\rangle$, then $\langle\mathbf p_1\cdots\mathbf p_4|\hat H|0\rangle = E\langle\mathbf p_1\cdots\mathbf p_4|0\rangle = 0$; smeared with a test function $f(\mathbf p_1, \dots, \mathbf p_4)$ that is nonzero somewhere on $\sum\mathbf p_i = 0$, Step 8 gives $\lambda\int\prod_i\frac{d^3p_i}{(2\pi)^32E_i}f\,(2\pi)^3\delta^3(\sum\mathbf p_i) \ne 0$ for suitable $f$. So $|0\rangle$ is not an eigenstate of $\hat H$, in particular not its ground state $|\Omega\rangle$.
>
> **Step 10** (the overlap). $|0\rangle$ and $|\Omega\rangle$ are unit vectors that are not proportional, so the Cauchy–Schwarz inequality is strict, $|\langle0|\Omega\rangle| < 1$; with Assumption 1 of [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] it is also nonzero, and [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]] gives the persistence amplitude $e^{-2iE_0T}|\langle0|\Omega\rangle|^2$, not $1$.
>
> ⚑ By-product: $\hat H|0\rangle$ also has two-particle and zero-particle components, from the terms of $(\hat\phi^+ + \hat\phi^-)^4$ with three or two $\hat\phi^-$'s; they carry the coincident-point constant $\langle0|\hat\phi_S(\mathbf x)^2|0\rangle$, which diverges ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]] for the same constant in $\hat H_0$). They are not needed for Step 9.
>
> **What the derivation shows.** The vacuum of a setup is the ground state of the Hamiltonian that acts at early and late times. In Model 1 that Hamiltonian is $\hat H_0$, so $|0\rangle$ is exact and $\hat S$ is reached at finite times; in Model 3 it is the full $\hat H$, which takes $|0\rangle$ into multi-particle states, so the vacuum is $|\Omega\rangle$ and must be projected out ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]]).

^der-c6a-0-4

*Uses:* [[§C6a.2 The Interaction Picture#^def-c6a-2-1|Def. §C6a.2.1]], [[§C6a.2 The Interaction Picture#^def-c6a-2-3|Def. §C6a.2.3]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]], [[§C6a.3 The Time-Evolution Operator and Time Ordering#^thm-c6a-3-7|Theorem §C6a.3.7]], [[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-5|Theorem §C6a.1.5]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-6|Theorem §C6b.9.6]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-4|Theorem §C6a.4.4]]

## Which diagrams carry which physics

> [!theorem] Theorem §C6a.0.5: The Connected Diagrams of a Switched Source Are Two Trees
> In [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]], with the source vertex of [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^def-c6b-9-1|Def. §C6b.9.1]] and outgoing particles $\langle\mathbf k_1\cdots\mathbf k_n|$ (in state $|0\rangle$), the connected diagrams are exactly
>
> $$
> \times\!\!-\!\!\times\ : \ L = \int d^4x\,d^4y\,\bigl(ij(x)\bigr)\bigl(ij(y)\bigr)D_F(x - y) , \qquad \times\!\!-\!\!\mathbf k\ : \ \frac{i\tilde j(k)}{\sqrt{2E_{\mathbf k}}}\Big|_{k^0 = E_{\mathbf k}} ,
> $$
>
> neither has a closed loop, and the exact amplitudes are $\mathcal A(\mathbf k_1, \dots, \mathbf k_n) = \prod_i\frac{i\tilde j(k_i)}{\sqrt{2E_{\mathbf k_i}}}\,e^{L/2}$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7|Theorem §C6b.9.7]]).
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]], states $\hat a^\dagger\cdots|0\rangle$ (not relativistically normalized); *applies:* exactly, all orders in $j$.
>
> *Source: Coleman p. 89 ("Model 1 Solved": the two connected diagrams $D_1$, $D_2$, $S(D_2) = 2$) · PHY 513, Problem Set 8, Problem 3(c)–(e) (the user's solution)*

^thm-c6a-0-5

> [!derivation]- Derivation
> **Step 1** (what can end a line). A line is a contraction ([[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]]) of two fields, each at a source vertex, or of a field with an outgoing particle ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]]). Two outgoing particles are never joined: with in state $|0\rangle$ there is no incoming particle to pair with, and $\langle\mathbf k|$ contracts only with a field.
>
> **Step 2** (counting ends). In a connected diagram let $V$ be the number of source vertices, $E$ the number of outgoing particles, $I$ the number of lines. Every source vertex has one leg and every outgoing particle one line, and every line has two ends:
>
> $$
> 2I = V + E .
> $$
>
> **Step 3** (connectedness). A connected graph on $N = V + E$ nodes has at least $N - 1$ edges:
>
> $$
> \frac{V + E}{2} = I \ge V + E - 1 \quad\Longrightarrow\quad V + E \le 2 .
> $$
>
> With at least one line, $V + E = 2$: $(V, E) = (2, 0)$, the line $L$ between two sources, or $(1, 1)$, a source joined to $\langle\mathbf k|$, whose factor $\int d^4x\,ij(x)\,e^{ik\cdot x}/\sqrt{2E_{\mathbf k}} = i\tilde j(k)/\sqrt{2E_{\mathbf k}}$ is Lemma §C6b.9.4 with [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]; $(0, 2)$ is excluded by Step 1.
>
> **Step 4** (no loops). The number of independent closed loops of a connected graph is $I - N + 1 = 1 - 2 + 1 = 0$ for both.
>
> **Step 5** (the amplitudes). Every diagram is a product of connected ones; the vacuum part exponentiates, $\sum_m\frac{L^m}{2^mm!} = e^{L/2}$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3|Theorem §C6b.9.3]], by [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]]), and each outgoing particle carries one source line, which is [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7|Theorem §C6b.9.7]].
>
> **What the derivation shows.** A source with one leg cannot build a loop, nor scatter a particle ("Mesons don't scatter off nailed down nucleons", Coleman p. 93): Model 1 is classical field theory plus the Poisson counting of its coherent state ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|Theorem §C2b.8.2]]).

^der-c6a-0-5

*Uses:* [[§C6a.5 Normal Ordering and Contractions#^def-c6a-5-1|Def. §C6a.5.1]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^def-c6b-9-1|Def. §C6b.9.1]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4|Lemma §C6b.9.4]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3|Theorem §C6b.9.3]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7|Theorem §C6b.9.7]], [[§CA.8 Splitting Pairings and the Exponential Formula#^thm-ca-8-3|Theorem §CA.8.3]]

> [!remark] Remark: Classical, semi-classical, quantum (Schwartz's triad)
> Schwartz sorts diagrams by the physics they need (§7.1, pp. 83–84, eq. (7.26)). For a connected diagram with $I$ internal lines and $V$ vertices, the number of closed loops is $I - V + 1$.
>
> | diagrams | physics | in C6 |
> |---|---|---|
> | trees whose external points are all sources | classical field theory: the iterated classical solution with sources ("calculated entirely with classical field theory") | Model 1, all of it ([[§C6a.0 Setups and Observables#^thm-c6a-0-5\|Theorem §C6a.0.5]]; the classical retarded field, [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1\|Theorem §C2b.8.1]]) |
> | one quantized line through an external field, no closed loop | semi-classical: "a single field is quantized … and does not get classical-source blobs on the end of its lines" | needs a two-legged external vertex, e.g. $\bar\psi\gamma^\mu\psi A^{\rm ext}_\mu$; none in C6 (Model 1 has one-legged vertices) |
> | at least one closed loop | quantum field theory proper: virtual particles created and destroyed, from the contact terms of the Schwinger–Dyson equation (p. 81) | the tadpole $D_F(0)$ ([[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-3\|Theorem §C6a.10.3]]); vacuum bubbles and $E_0$ ([[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-7\|Theorem §C6a.11.7]]); external-leg loops, the origin of $\sqrt Z$ |
>
> The lowest-order amplitudes of Model 3 asked for in Problem Set 8 (Problems 2 and 4; $i\mathcal M = -i\lambda$, [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-1|Example §C6b.8.1]]) are trees; the loops are where the free states stop being enough.
>
> *Source: Schwartz §7.1, pp. 81, 83–84 · Coleman p. 93*

^rem-c6a-0-1

## One object, three meanings

> [!remark] Remark: The three meanings of a blob (Coleman)
> Let a blob $\tilde G^{(n)}(k_1, \dots, k_n)$ be the sum of Feynman diagrams with $n$ external lines, momenta off the mass shell. Coleman gives it three meanings, "Something neat is that they all agree" (p. 140; summary p. 154):
>
> | meaning | the object | formula | in the vault |
> |---|---|---|---|
> | 1. internal subdiagram | a part of a larger diagram, plugged in with its off-shell momenta and integrated | lines $\tilde D_F$, $\int\frac{d^4k}{(2\pi)^4}$ per loop | [[§C6a.10 Feynman Rules in Momentum Space#^thm-c6a-10-2\|Theorem §C6a.10.2]] |
> | 2. coefficient in $\langle0\lvert\hat S\rvert0\rangle_j$ | the vacuum-persistence amplitude in a source, $Z[j]$ | $Z[j] = \sum_n\frac{i^n}{n!}\int d^4x_1\cdots d^4x_n\,j(x_1)\cdots j(x_n)\,G^{(n)}(x_1, \dots, x_n)$ | Model 1: [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3\|Theorem §C6b.9.3]], [[§C6a.0 Setups and Observables#^ex-c6a-0-1\|Example §C6a.0.1]] |
> | 3. Fourier transform of a Heisenberg correlator | the time-ordered vacuum value of Heisenberg fields | $G^{(n)}(x_1, \dots, x_n) = \langle\Omega\rvert T\{\hat\phi_H(x_1)\cdots\hat\phi_H(x_n)\}\lvert\Omega\rangle$ | [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-2\|Def. §C6a.4.2]], [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-7\|Theorem §C6a.4.7]] |
>
> Meanings 2 and 3 agree because the source can be treated as the interaction and $\hat H_0 + \hat H_{\rm int}$ as the "free" part, so that the Dyson series in $j$ has Heisenberg fields in it (p. 153–154; with interactions, Coleman's $|0\rangle$ there is the physical vacuum, pp. 155, 158): $Z[j] = \langle\Omega|T\{\exp[i\int d^4x\,j\hat\phi_H]\}|\Omega\rangle$. "Ex nihil omnes: All physical information (all Green's functions, and hence all S matrix elements) about the system is coded in the vacuum persistence amplitude in the presence of an external source" (p. 152). The bridge from meaning 3 to the $S$-matrix is amputation on the mass shell ([[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1|Theorem §C6b.8.1]]). In Model 1 all three are elementary, because $\hat\phi_H = \hat\phi_I$ apart from the source; in Model 3 meaning 2 is the generating functional of the path integral (later).
>
> *Source: Coleman pp. 140–141 (Answer 1), 144, 151–152 (Answer 2, eq. (14.4), $Z[\rho] \equiv \langle0|S|0\rangle_\rho$), 153–154 (Answer 3, eq. (14.5), the summary)*

^rem-c6a-0-2

> [!example] Example §C6a.0.1: Meanings 2 and 3 for a Switched Source
> In [[§C6a.0 Setups and Observables#^mod-c6a-0-1|Model §C6a.0.1]] the correlators of meaning 3 are free, and meaning 2 reproduces the vacuum-persistence amplitude of [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3|Theorem §C6b.9.3]]:
>
> $$
> Z[j] = \sum_{n\ge0}\frac{i^n}{n!}\int\prod_{l=1}^nd^4x_l\,j(x_l)\;\langle0|T\{\hat\phi_I(x_1)\cdots\hat\phi_I(x_n)\}|0\rangle = \exp\Bigl[-\frac12\int d^4x\,d^4y\,j(x)\,D_F(x - y)\,j(y)\Bigr] = e^{\mathcal A_2} .
> $$
>
> **Step 1** (meaning 2 = meaning 3 here). With no other interaction, $\hat\phi_H = \hat\phi_I$ and $|\Omega\rangle = |0\rangle$; the series is the Taylor series of $\langle0|T\{\exp[i\int j\hat\phi_I]\}|0\rangle = \mathcal A(0)$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-1|Theorem §C6b.9.1]]) term by term ([[§C6a.3 The Time-Evolution Operator and Time Ordering#^def-c6a-3-1|Def. §C6a.3.1]]).
>
> **Step 2** (the free correlators). By [[§C6a.6 Wick's Theorem#^thm-c6a-6-3|Theorem §C6a.6.3]], $G^{(n)} = 0$ for $n$ odd and, for $n = 2m$, $G^{(2m)} = \sum_P\prod_{\{a,b\}\in P}D_F(x_a - x_b)$, a sum over the $\frac{(2m)!}{2^mm!}$ pairings ([[§CA.7 Pairings, Diagrams and Symmetry Factors#^thm-ca-7-1|Theorem §CA.7.1]]). For $m = 1, 2$:
>
> $$
> G^{(2)} = D_F(x_1 - x_2) , \qquad G^{(4)} = D_F(x_1 - x_2)D_F(x_3 - x_4) + D_F(x_1 - x_3)D_F(x_2 - x_4) + D_F(x_1 - x_4)D_F(x_2 - x_3) .
> $$
>
> **Step 3** (each pairing gives the same integral). The $j$'s are integrated symmetrically, so renaming the variables turns every pairing into the first one:
>
> $$
> \int\prod_{l=1}^{2m}d^4x_l\,j(x_l)\prod_{\{a,b\}\in P}D_F(x_a - x_b) = \Bigl(\int d^4x\,d^4y\,j(x)D_F(x - y)j(y)\Bigr)^m \equiv J^m .
> $$
>
> **Step 4** (the sum). With $i^{2m} = (-1)^m$:
>
> $$
> Z[j] = \sum_{m\ge0}\frac{(-1)^m}{(2m)!}\cdot\frac{(2m)!}{2^mm!}\,J^m = \sum_{m\ge0}\frac1{m!}\Bigl(-\frac J2\Bigr)^m = e^{-J/2} ,
> $$
>
> and $\mathcal A_2 = \frac{1}{2!}\int d^4x\,d^4y\,(ij(x))(ij(y))D_F(x - y) = -\frac J2 = \frac L2$ ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^def-c6b-9-1|Def. §C6b.9.1]]).
>
> *Source: Coleman pp. 151–154 · PHY 513, Problem Set 8, Problem 3(c)*

^ex-c6a-0-1

## From the question to the object

Read a row left to right: the words of the problem, the setup they imply, the states and vacuum, the matrix element or function to compute, the boxes that compute it, and what goes wrong most often. "PS8 P$k$" is PHY 513, Problem Set 8, Problem $k$.

| question as asked | model | in/out states and vacuum | object to compute | theorems | pitfalls |
|---|---|---|---|---|---|
| "the probability that the source creates no particles at all" (PS8 P3(a)–(c)) | [[§C6a.0 Setups and Observables#^mod-c6a-0-1\|Model §C6a.0.1]] | in $\lvert0\rangle$, out $\lvert0\rangle$, exactly | $P(0) = \lvert\langle0\vert\hat S\vert0\rangle\rvert^2$, $\hat S = T\{e^{i\int j\hat\phi_I}\}$ | [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-1\|Theorem §C6b.9.1]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-2\|Theorem §C6b.9.2]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-3\|Theorem §C6b.9.3]] | $\lvert0\rangle$, not $\lvert\Omega\rangle$, and no denominator ([[§C6a.0 Setups and Observables#^thm-c6a-0-4\|Theorem §C6a.0.4]]); only $\operatorname{Re}\mathcal A_2$ enters $P(0)$, and it comes from the $i\varepsilon$ of $D_F$: $2\operatorname{Re}\mathcal A_2 = -\lambda$ |
| "the probability that the source creates exactly one particle, with momentum $\mathbf k$" (PS8 P3(d)) | Model §C6a.0.1 | in $\lvert0\rangle$; out $\langle\mathbf k\vert = \langle0\vert\hat a_{\mathbf k}$ | $dP(1) = \frac{d^3k}{(2\pi)^3}\lvert\langle\mathbf k\vert\hat S\vert0\rangle\rvert^2$, a density in $\mathbf k$ | [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^lem-c6b-9-4\|Lemma §C6b.9.4]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-5\|Theorem §C6b.9.5]] | normalization: with $\hat a^\dagger\vert0\rangle$ the measure is $\frac{d^3k}{(2\pi)^3}$ and $\langle\mathbf k\vert\hat\phi_I\vert0\rangle = \frac{e^{ik\cdot x}}{\sqrt{2E}}$; with $\sqrt{2E}\,\hat a^\dagger\vert0\rangle$ it is $\frac{d^3k}{(2\pi)^32E}$; never mix ([[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^cau-c6b-9-1\|§C6b.9, Caution: Two normalizations]]) |
| "the probability of producing $n$ particles" (PS8 P3(e)) | Model §C6a.0.1 | in $\lvert0\rangle$; out $\hat a^\dagger_{\mathbf k_1}\cdots\hat a^\dagger_{\mathbf k_n}\vert0\rangle$ | $P(n) = \frac{1}{n!}\int\prod_i\frac{d^3k_i}{(2\pi)^3}\lvert\mathcal A(\mathbf k_1, \dots, \mathbf k_n)\rvert^2$ | [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-6\|Theorem §C6b.9.6]], [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-7\|Theorem §C6b.9.7]], [[§C6a.0 Setups and Observables#^thm-c6a-0-5\|Theorem §C6a.0.5]] | the $\frac{1}{n!}$ of the measure: integrating each momentum freely counts each state $n!$ times |
| "verify $\sum P(n) = 1$, $\bar N = \lambda$; the fluctuation $\langle(N - \bar N)^2\rangle$" (PS8 P3(f)); the radiated energy | Model §C6a.0.1 | in $\lvert0\rangle$; the late-time state $\hat S\lvert0\rangle$, a coherent state | $\sum_n n^kP(n)$; $\Delta E = \langle0\vert\hat S^\dagger\hat H_0\hat S\vert0\rangle$ | [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route#^thm-c6b-9-8\|Theorem §C6b.9.8]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2\|Theorem §C2b.8.2]], [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3\|Theorem §C2b.8.3]] | $\sum_nP(n) = 1$ is unitarity, a check, not an input; in the Heisenberg route the state stays $\lvert0\rangle$ and the operators $\hat b_{\mathbf p}$ change |
| "the ground-state energy of two static sources; the force between them" | ★ [[§C6a.0 Setups and Observables#^mod-c6a-0-2\|Model §C6a.0.2]] | $\lvert0\rangle$ in and out only through adiabatic switching; the ground state is $\lvert\Omega\rangle \ne \lvert0\rangle$ | $E_0$, from $\langle0\vert\hat S\vert0\rangle = e^{-iE_0\tilde T}$ or by completing the square | Model §C6a.0.2 (Coleman pp. 92–97) | the phase diverges with $\tilde T$; $\hat S = \mathbb 1$, so the physics is in $E_0$, not in scattering |
| "the two-point correlator at order $\lambda$" ($\phi^4$) | [[§C6a.0 Setups and Observables#^mod-c6a-0-3\|Model §C6a.0.3]] | vacuum $\lvert\Omega\rangle$; no particle states | $\langle\Omega\vert T\{\hat\phi_H(x)\hat\phi_H(y)\}\vert\Omega\rangle$ = ratio of free vacuum values | [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-6\|Theorem §C6a.4.6]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-5\|Theorem §C6a.11.5]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^ex-c6a-11-4\|Example §C6a.11.4]] | not an observable ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^rem-c6b-1-2\|§C6b.1, Remark: The fundamental observable?]]); the denominator (bubbles) must be kept or cancelled; $T \to \infty(1 - i\varepsilon)$, not real $T$ |
| "the symmetry factor of each diagram" in $\phi^4$, or in $(\phi^\dagger\phi)^2$ with oriented lines (PS8 P1) | Model §C6a.0.3 | vacuum $\lvert0\rangle$ inside the numerator of the master formula | the coefficient $\frac1S$ of a diagram in $\langle0\vert T\{\hat\phi_I\cdots e^{-i\int\hat H_I}\}\vert0\rangle$ (meaning 1 or 3 of a blob) | [[§C6a.8 Position-Space Feynman Rules#^thm-c6a-8-1\|Theorem §C6a.8.1]], [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-5\|Example §C6a.9.5]], [[§C6a.9 Symmetry Factors in Practice#^thm-c6a-9-1\|Theorem §C6a.9.1]], [[§C6a.9 Symmetry Factors in Practice#^ex-c6a-9-7\|Example §C6a.9.7]] | a vacuum bubble is not attached to an external point; the vertex normalization $\frac{\lambda}{4}$ of $(\phi^\dagger\phi)^2$ is not $\frac{\lambda}{4!}$; arrows forbid exchanging $\hat\phi$ and $\hat\phi^\dagger$ legs |
| "which diagrams contribute to $p_A + p_B \to p_1 + p_2$ at order $g^2$ or $\lambda$"; "to $2 \to 3$ at order $g\lambda$"; "show $S = 1$" (PS8 P2) | Model §C6a.0.3, cubic–quartic | free relativistic states $\sqrt{2E}\,\hat a^\dagger\cdots\vert0\rangle$, valid at lowest order | the fully connected, amputated diagrams of $\langle f\vert i\hat T\vert i\rangle$ | [[§C6b.8 Amplitudes from Correlation Functions#^def-c6b-8-1\|Def. §C6b.8.1]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-2\|Theorem §C6b.8.2]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-4\|Theorem §C6b.8.4]], [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-3\|Example §C6b.8.3]], [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-4\|Example §C6b.8.4]] | disconnected pieces belong to the $\mathbb 1$ of $\hat S$ ("not the event whose probability we wish to compute", Srednicki p. 88); bubbles are a phase; loops on external legs are not in $\mathcal M$ (amputation, $\sqrt Z$); order counting $g^{n_3}\lambda^{n_4}$ with $\lambda \sim g^2/m^2$ |
| any process: "which diagrams contribute at order $n$?" | Model §C6a.0.3 | in and out states of $\hat H$; free ones at lowest order | $i\mathcal M$ = fully connected amputated diagrams, external lines $1$ | [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-1\|Theorem §C6b.8.1]], [[§C6b.8 Amplitudes from Correlation Functions#^thm-c6b-8-3\|Theorem §C6b.8.3]] | "connected" means fully connected here ([[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-1\|§C6b.8, Caution: "Connected" here means fully connected]]), unlike the correlators' "attached" |
| "$d\sigma/d\Omega$ and $\sigma$ for $\phi\phi \to \phi\phi$ at lowest order" ($\phi^4$) | Model §C6a.0.3, $\phi^4$; experiment: [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1\|Model §C6b.2.1]] or [[§C6b.4 Wave Packets and the Cross Section#^mod-c6b-4-1\|Model §C6b.4.1]] | $\lvert\mathbf p_A\mathbf p_B\rangle$, $\lvert\mathbf p_1\mathbf p_2\rangle$ free, relativistic, over $\lvert0\rangle$ (lowest order) | $i\mathcal M = -i\lambda$; $\frac{d\sigma}{d\Omega}\big\vert_{\rm cm} = \frac{\lvert\mathcal M\rvert^2}{64\pi^2E_{\rm cm}^2}$; $\sigma = \frac12\int d\sigma$ | [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-1\|Example §C6b.8.1]], [[§C6b.8 Amplitudes from Correlation Functions#^ex-c6b-8-2\|Example §C6b.8.2]], [[§C6b.6 Lorentz Invariance and Two-Body Phase Space#^thm-c6b-6-8\|Theorem §C6b.6.8]], [[§C6b.3 The Cross Section#^thm-c6b-3-6\|Theorem §C6b.3.6]] | $\lvert\langle f\vert i\hat T\vert i\rangle\rvert^2$ contains $[(2\pi)^4\delta^4]^2$, one $\delta^4(0) = \tilde V\tilde T/(2\pi)^4$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-2\|Theorem §C6b.2.2]]); the $\frac1{S_{\rm id}}$ belongs to $\sigma$, not to $d\sigma$ ([[§C6b.5 Evaluating the Cross Section#^thm-c6b-5-4\|Theorem §C6b.5.4]]); relativistic normalization is what the formula assumes |
| "the lifetime of $\Phi$ to the lowest order in $\mu$" (PS8 P4) | Model §C6a.0.3, $\Phi\phi^2$; [[§C6b.7 Decay Rates and Widths#^mod-c6b-7-1\|Model §C6b.7.1]] | $\lvert\mathbf K\rangle_\Phi = \sqrt{2E}\,\hat b^\dagger_{\mathbf K}\vert0\rangle$ at rest, out $\lvert\mathbf p_1\mathbf p_2\rangle$, free, lowest order | $i\mathcal M = -2i\mu$; $\Gamma = \frac{1}{2!}\int d\Gamma$, $\tau = \frac1\Gamma$ | [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-4\|Theorem §C6b.7.4]], [[§C6b.7 Decay Rates and Widths#^thm-c6b-7-5\|Theorem §C6b.7.5]], [[§C6b.7 Decay Rates and Widths#^ex-c6b-7-1\|Example §C6b.7.1]] | the $2$ in $\mathcal M = -2\mu$ (two ways to contract $\hat\phi^2$) and the $\frac1{2!}$ of identical final $\phi$'s are separate factors; an unstable $\Phi$ is not an asymptotic state ([[§C6b.7 Decay Rates and Widths#^cau-c6b-7-1\|§C6b.7, Caution: Free states in a decay amplitude]]); kinematics first: $M > 2m$ |
| "the vacuum energy density of $\phi^4$" | Model §C6a.0.3 | $\lvert\Omega\rangle$ against $\lvert0\rangle$ | $E_0/V$ from the connected vacuum bubbles, $\langle0\vert U(T, -T)\vert0\rangle = e^{\sum_iV_i}$ | [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-6\|Theorem §C6a.11.6]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-7\|Theorem §C6a.11.7]] | each bubble carries $(2\pi)^4\delta^4(0) = 2T\cdot V$; this $E_0$ is not the zero-point energy ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^cau-c6a-4-1\|§C6a.4, Caution: Two E₀'s]]) |

> [!caution] Caution: Names for the vacua
> The vault keeps PS's names: $|0\rangle$ is the free vacuum ($\hat H_0|0\rangle = 0$), $|\Omega\rangle$ the interacting one ([[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]]). Several sources write $|0\rangle$ for the **interacting** vacuum:
>
> | source | free vacuum | interacting vacuum |
> |---|---|---|
> | PS; Schwartz | $\lvert0\rangle$ | $\lvert\Omega\rangle$ (PS p. 82; Schwartz pp. 69, 75) |
> | Yu, ch. 6–7 | $\lvert0\rangle$ (eq. (6.284)) | not discussed |
> | Yu, ch. 10 | — (the in-field vacuum equals the true vacuum up to a phase, eq. (10.171), p. 463) | $\lvert0\rangle$ (eq. (10.4), p. 440) |
> | Coleman, Models 1–3 | $\lvert0\rangle$ (the bare vacuum) | $\lvert0\rangle_P$ (p. 92) |
> | Coleman, LSZ lectures | — | $\lvert0\rangle \equiv \lvert0\rangle_p$ (p. 158) |
> | Srednicki | $\lvert\varnothing\rangle$ (Problem 9.5 only) | $\lvert0\rangle$, "a unique ground state" (p. 51) |
>
> A formula copied from Yu ch. 10, Coleman's LSZ lectures or Srednicki with $|0\rangle$ is a formula in $|\Omega\rangle$. In Model §C6a.0.1 the two names agree at early and late times, which is why $|0\rangle$ and no denominator are correct there ([[§C6a.0 Setups and Observables#^thm-c6a-0-4|Theorem §C6a.0.4]]).
>
> *Source: survey of the books, 2026-10-31 (pages as listed) · [[Larsen PHY 513]] (register row)*

^cau-c6a-0-1

> [!remark]- Connections
> - The models are the setups behind every *Model:* and *applies:* line of C6a and C6b: Model §C6a.0.1 behind [[§C6b.9 Particle Production by a Classical Source꞉ the Diagrammatic Route|§C6b.9]] and [[§C2b.8 Particle Production by a Classical Source|§C2b.8]]; Model §C6a.0.3 behind §C6a.1–§C6a.11 and the experiment models [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]], [[§C6b.4 Wave Packets and the Cross Section#^mod-c6b-4-1|Model §C6b.4.1]], [[§C6b.7 Decay Rates and Widths#^mod-c6b-7-1|Model §C6b.7.1]].
> - The projection that replaces "the interaction switches off" in Model §C6a.0.3 is the tilted limit — [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^thm-c6a-4-1|Theorem §C6a.4.1]], [[§C6a.11 The iε Limit and Vacuum Bubbles#^thm-c6a-11-1|Theorem §C6a.11.1]].
> - The same table, as worked translations (question as asked → model → in/out states and vacuum → matrix element → normalization and measure → theorem → result), is the planned closing section of C6b, "From the Question to the Formula" (planned).
> - The precise statement of "free states at lowest order, $\sqrt Z$ beyond" is the LSZ formula (Lecture 16; QFT C10, planned) — [[§C6b.8 Amplitudes from Correlation Functions#^cau-c6b-8-2|§C6b.8, Caution: The rule is stated at lowest order]].
> - Model §C6a.0.2 and meaning 2 of a blob return with the generating functional $Z[J]$ of the path integral (QFT C11, planned).
