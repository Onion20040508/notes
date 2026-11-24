---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
section: C8a.12
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field|§C8a.11]] · ↑ [[· C8a Quantum Electrodynamics]] · [[§C8a.13 The Cross Section for Electron–Muon Scattering|§C8a.13]] →

*Sources: PHY 513 Lecture 21 (Larsen, 18 Nov 2026, "Crossing Symmetry"; a recorded lecture in three parts), slides 2–8 (Part A), and recording, part A · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.4, pp. 153–154: the two unnumbered displays of p. 153 (the amplitude; the product of two traces), eqs. (5.60)–(5.61) (page images checked).*

What changes when the muon is in the initial state instead of the final one? Lecture 21 studies a second QED process, the scattering of an electron off a muon, $e^-\mu^- \to e^-\mu^-$: the same particles before and after, with their momenta changed. Its diagram is the annihilation diagram of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]] with two legs moved between the initial and the final state, and the result of the lecture is that nothing has to be computed again: the spin-averaged $|\mathcal M|^2$ of $e^-e^+ \to \mu^-\mu^+$ ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]]) becomes that of $e^-\mu^- \to e^-\mu^-$ by a substitution of momenta. The lecture has three parts, and the chapter follows them:
1. **the amplitude and the substitution** (this section): the diagram and $i\mathcal M$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|Theorem §C8a.12.1]]), the spin average as two traces ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2|Theorem §C8a.12.2]]), the comparison with annihilation ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]) and the result ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]]);
2. **the physics of the process** ([[§C8a.13 The Cross Section for Electron–Muon Scattering|§C8a.13]]): centre-of-mass kinematics, the cross section and its forward peak;
3. **crossing symmetry in general and the Mandelstam variables** ([[§C8a.14 Crossing Symmetry and Mandelstam Variables|§C8a.14]]).

The diagram itself is not new: it is the one-photon exchange of [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]] (Lecture 18), whose nonrelativistic limit gave the Coulomb potential ([[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-3|Theorem §C8a.5.3]]). What is new is its square, summed over spins, at any energy.

**Setup.** [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]: QED with two charged Dirac fields, the electron and the muon, in the interaction picture; free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); order $e^2$, the lowest order of the process, where the rules are exact ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). The "muon" stands for any electrically charged spin-$\frac12$ particle that is described by a Dirac field like the electron but is distinct from it. The amplitude and the two traces are written with both masses, as on the slides; the evaluated result ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]]) is at $m_e = 0$, as lectured. External states are ordered as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]].

*Conventions* ([[Larsen PHY 513]]): incoming $e^-(p_1, s)$, $\mu^-(p_2, r)$, outgoing $e^-(p_1', s')$, $\mu^-(p_2', r')$: the index 1 is the electron, 2 the muon, a prime marks the final state; $q = p_1 - p_1'$. In this section $p, p', k, k'$ always denote the momenta of the annihilation process, $e^-(p) + e^+(p') \to \mu^-(k) + \mu^+(k')$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]]). [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]] wrote the present process with $p, k \to p', k'$: its $p, p', k, k'$ are $p_1, p_1', p_2, p_2'$ here. $m_e$, $m_\mu$ are masses, and the subscript $\mu$ of $m_\mu$ is not an index ([[§C8a.7 The Spin-Averaged Squared Amplitude#^cau-c8a-7-1|§C8a.7, Caution: The subscript of the muon mass is not an index]]); $e$ as in [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^cau-c8a-1-1|§C8a.1, Caution: What e means]]; $q^4 \equiv (q^2)^2$.

## The diagram and the amplitude

> [!theorem] Theorem §C8a.12.1: The Amplitude for Electron–Muon Scattering
> ![[ph-qft-c8-18-1.svg]]
> *The single diagram at order $e^2$, time running upward (after PHY 513 Lecture 21, slide 4). Line arrows are fermion number ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]), orange arrows momenta. All four external particles are particles, so every momentum arrow runs along its line arrow.*
>
> In [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]], for $e^-(p_1, s) + \mu^-(p_2, r) \to e^-(p_1', s') + \mu^-(p_2', r')$ at order $e^2$:
> 1. exactly one diagram contributes, the exchange diagram of the figure. There is no diagram with $p_1' \leftrightarrow p_2'$, because the electron and the muon are distinct particles;
> 2. its value is
>
> $$
> i\mathcal M = \bigl[\bar u^{s'}(p_1')(-ie\gamma^\mu)u^s(p_1)\bigr]\,\frac{-ig_{\mu\nu}}{q^2}\,\bigl[\bar u^{r'}(p_2')(-ie\gamma^\nu)u^r(p_2)\bigr] = \frac{ie^2}{q^2}\,\bigl[\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr]\bigl[\bar u^{r'}(p_2')\gamma_\mu u^r(p_2)\bigr] , \qquad q = p_1 - p_1' = p_2' - p_2 ;
> $$
>
> 3. each bracket is one fermion line read against its arrow ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]), the electron line with the electron mass in its spinors and the muon line with the muon mass. Only $u$ and $\bar u$ occur: an incoming particle gives $u$, an outgoing particle $\bar u$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]);
> 4. the photon carries the momentum that the electron hands to the muon. It is spacelike or zero, $q^2 \le 0$, with $q^2 = 0$ only for forward scattering, $p_1' = p_1$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]]): the photon is off shell ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]]), and away from the forward direction the $i\varepsilon$ of the propagator may be dropped;
> 5. the sign is that of the contractions with the states ordered as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]: $+$ for two particles ([[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-5|Theorem §C8a.5.5]]). It is physical relative to the unscattered term ([[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-6|Theorem §C8a.5.6]]) and drops out of $|\mathcal M|^2$.
>
> *Equivalently,* this is $i\mathcal M_{\rm QED}$ of [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]] in the labels of this lecture, with the index lowered by the $g_{\mu\nu}$ of the propagator.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$ (the lowest), free states over $|0\rangle$, any spins, both masses kept; $p_1' \ne p_1$ for the dropped $i\varepsilon$.
>
> *Source: PHY 513 Lecture 21, slide 4 ("$\mu^-$ refers to any electrically charged spin-$\frac12$ particle similar to but distinct from an electron. (There is no diagram with $p_1' \leftrightarrow p_2'$)"; "$i\mathcal M = \bar u^{s'}(p_1')(-ie\gamma^\mu)u^s(p_1)\cdot\frac{-ig_{\mu\nu}}{q^2}\cdot\bar u^{r'}(p_2')(-ie\gamma^\nu)u^r(p_2) = \frac{ie^2}{q^2}\bigl(\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr)\cdot\bigl(\bar u^{r'}(p_2')\gamma_\mu u^r(p_2)\bigr)$"), and recording, part A · PS §5.4, p. 153 (the display under "Electron-Muon Scattering": "The lowest-order Feynman diagram is just the previous one turned on its side") · items 4 and 5 written here from the homes linked*

^thm-c8a-12-1

> [!derivation]- Derivation
> **Step 1** (which diagrams). There are no external photons, so the photon fields of the vertices contract with each other and the number of vertices is even ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]], 1): the lowest order is $e^2$, two vertices joined by one photon line. Each vertex holds two fermion legs of one species ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]], 3), and with four external fermions no leg is left for an internal fermion line. The external particles are two of the electron species, one in and one out, and two of the muon species, one in and one out. So one vertex takes the two electron legs and the other the two muon legs. Exchanging $p_1'$ and $p_2'$ would put the outgoing muon on the electron vertex, and no vertex joins an electron to a muon. One diagram remains.
>
> **Step 2** (the electron vertex). The vertex holds $\hat{\bar\psi}_e\gamma^\mu\hat\psi_e$. The incoming electron is annihilated: the $\hat\psi_e$ of the vertex contains $\hat a\,u$ (and $\hat b^\dagger v$), its $\hat a$ contracts with the electron of the initial state and leaves the wave function $u^s(p_1)$. The outgoing electron is created: $\hat{\bar\psi}_e$ contains $\hat a^\dagger\bar u$, which contracts with the electron of the final state and leaves $\bar u^{s'}(p_1')$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). With the vertex factor ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]), read against the arrow:
>
> $$
> \bar u^{s'}(p_1')\,(-ie\gamma^\mu)\,u^s(p_1) .
> $$
>
> **Step 3** (the muon vertex). The same with the muon field: the vertex does not care that the particles are muons, only the momenta, the spins and the mass in the spinors differ. It carries its own Lorentz index $\nu$:
>
> $$
> \bar u^{r'}(p_2')\,(-ie\gamma^\nu)\,u^r(p_2) .
> $$
>
> **Step 4** (the propagator). Each vertex holds one photon field, and there is no photon in the initial or the final state, so the two fields can only contract with each other: $\frac{-ig_{\mu\nu}}{q^2 + i\varepsilon}$ ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|Theorem §C8a.3.5]]). Momentum conservation at the electron vertex, $p_1$ in and $p_1'$ out, gives $q = p_1 - p_1'$ flowing to the muon vertex, where $p_2 + q = p_2'$.
>
> **Step 5** (collect the constants). $(-ie)\cdot(-i)\cdot(-ie) = (-i)^3e^2 = +ie^2$, and $g_{\mu\nu}\gamma^\nu = \gamma_\mu$ ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]], step 1):
>
> $$
> i\mathcal M = \frac{ie^2}{q^2 + i\varepsilon}\,\bigl[\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr]\bigl[\bar u^{r'}(p_2')\gamma_\mu u^r(p_2)\bigr] .
> $$
>
> **Step 6** (the photon is spacelike). Each fermion keeps its mass, $p_1^2 = p_1'^2$ and $p_2^2 = p_2'^2$, so the argument given with the table of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]] applies: $q^2 = -|\mathbf p_1 - \mathbf p_1'|^2 \le 0$ in the centre-of-mass frame, hence in every frame, with equality only for $\mathbf p_1' = \mathbf p_1$. For $p_1' \ne p_1$ the denominator does not vanish and $\frac{1}{q^2 + i\varepsilon} \to \frac{1}{q^2}$. ⚑ By-product: the forward direction is the pole of the propagator → [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-6|Theorem §C8a.13.6]].
>
> **Step 7** (the sign). With $|i\rangle \propto \hat a^\dagger_{e\mathbf p_1}\hat a^\dagger_{\mu\mathbf p_2}|0\rangle$ and the bra its Hermitian conjugate, the contractions are those of [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]], paragraph "Sign": two crossings, sign $+$ ([[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-5|Theorem §C8a.5.5]]).
>
> **What the derivation shows.**
> - The steps are those of the annihilation amplitude ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^der-c8a-6-2|Derivation §C8a.6.2]]), vertex by vertex. The only differences are which of $u$, $\bar u$, $\bar v$, $v$ appear and what $q$ is.
> - ⚑ By-product: the two brackets are again the two fermion lines; after the spin sum each becomes one trace → [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2|Theorem §C8a.12.2]].

^der-c8a-12-1

*Uses:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]], [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|Theorem §C8a.3.5]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]], [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]], [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-5|Theorem §C8a.5.5]], [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-1|P8, step 1]], [[P8 Unpolarized Cross Section from Diagrams#^p8-2|P8, step 2]]; [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!remark] Remark: The picture of the process
> The process is a scattering in the everyday sense: an electron comes in, meets a charged particle, and goes out at a different angle. The lecture's picture is that of Rutherford scattering, an electron deflected by some hard centre, some heavy particle; that the target is negatively charged here makes no great difference to the picture. Nothing is created or destroyed in the net: the electron is there before and after, and so is the muon; what changes is their four-momenta. At the vertex the description is still one of annihilation and creation: the incoming electron is annihilated by the $\hat\psi$ of the interaction and a new electron is created by its $\hat{\bar\psi}$ (Step 2 of the derivation).
>
> *Source: PHY 513 Lecture 21, recording, part A; slide 26 ("Same particles in initial and final state, 4-momenta change")*

^rem-c8a-12-1

## The spin average

> [!theorem] Theorem §C8a.12.2: The Spin-Averaged Squared Amplitude as Two Traces
> With the spin average of [[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1|Def. §C8a.7.1]] (sum over $s'$, $r'$, average over $s$, $r$),
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2 = \frac{e^4}{4q^4}\,\operatorname{tr}\bigl[(\slashed p_1' + m_e)\gamma^\mu(\slashed p_1 + m_e)\gamma^\nu\bigr]\;\operatorname{tr}\bigl[(\slashed p_2' + m_\mu)\gamma_\mu(\slashed p_2 + m_\mu)\gamma_\nu\bigr] , \qquad q = p_1 - p_1' .
> $$
>
> 1. One trace for each fermion line, the first from the electron line, the second from the muon line, contracted in $\mu$ and $\nu$.
> 2. Squaring the electron bracket gives $\bigl[\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr]\bigl[\bar u^s(p_1)\gamma^\nu u^{s'}(p_1')\bigr]$: the bracket times its complex conjugate, which is the same expression in the opposite order, with a new index $\nu$.
> 3. Every spin sum is the completeness relation of a particle, $\sum_su^s(p)\bar u^s(p) = \slashed p + m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]): all four masses enter with a plus sign.
>
> *Equivalently,* it is [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], parts 2–4, with $w_1 = u(p_1')$, $w_2 = u(p_1)$, $\Gamma = \gamma^\mu$, $\Gamma' = \gamma^\nu$ for the electron line and $w_1 = u(p_2')$, $w_2 = u(p_2)$, $\Gamma = \gamma_\mu$, $\Gamma' = \gamma_\nu$ for the muon line (the traces agree after a cyclic shift).
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, unpolarized, on-shell external momenta, any frame; the traces are written with both masses and are not evaluated here.
>
> *Source: PHY 513 Lecture 21, slide 5 ("Square amplitude. The factor from the electron vertex gives: $\bar u^{s'}(p_1')\gamma^\mu u^s(p_1) \to \bigl(\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr)\bigl(\bar u^s(p_1)\gamma^\nu u^{s'}(p_1')\bigr)$. Average over initial spins and sum over final spins. Exploit completeness: $\sum_{s=1,2}u^s(p)\bar u^s(p) = \slashed p + m$. Result: $\frac14\sum_{\rm spin}|\mathcal M|^2 = \frac{e^4}{4q^4}\operatorname{Tr}[(\slashed p_1' + m_e)\gamma^\mu(\slashed p_1 + m_e)\gamma^\nu]\cdot\operatorname{Tr}[(\slashed p_2' + m_\mu)\gamma_\mu(\slashed p_2 + m_\mu)\gamma_\nu]$"), and recording, part A · PS §5.4, p. 153 (the display before eq. (5.60))*

^thm-c8a-12-2

> [!derivation]- Derivation
> **Step 1** (the conjugate). A bracket is a number, so its complex conjugate is its Hermitian conjugate, which reverses the order: $\bigl[\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr]^\ast = \bar u^s(p_1)\gamma^\mu u^{s'}(p_1')$ ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], part 1, with $\bar\Gamma = \Gamma$ for $\Gamma = \gamma^\mu$; the same computation as [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-1|Theorem §C8a.7.1]]). The $u(p_1)$ becomes a $\bar u(p_1)$ on the left, the $\bar u(p_1')$ a $u(p_1')$ on the right.
>
> **Step 2** (the square). $q^2$ is real, and the summed index of $\mathcal M^\ast$ is renamed $\nu$, because it is contracted between the two conjugated brackets, not with the $\mu$ of $\mathcal M$ ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-2|Theorem §C8a.7.2]]):
>
> $$
> |\mathcal M|^2 = \frac{e^4}{q^4}\,\bigl[\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr]\bigl[\bar u^s(p_1)\gamma^\nu u^{s'}(p_1')\bigr]\;\bigl[\bar u^{r'}(p_2')\gamma_\mu u^r(p_2)\bigr]\bigl[\bar u^r(p_2)\gamma_\nu u^{r'}(p_2')\bigr] .
> $$
>
> Instead of two wave functions each line now has four.
>
> **Step 3** (the sum over $s$). $u^s(p_1)$ and $\bar u^s(p_1)$ stand next to each other with the same $s$, a column times a row: $\sum_su^s(p_1)\bar u^s(p_1) = \slashed p_1 + m_e$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]).
>
> **Step 4** (the sum over $s'$). With spinor indices written, every factor is a number; the $u^{s'}(p_1')$ at the far right is moved to the far left, next to $\bar u^{s'}(p_1')$, and $\sum_{s'}u^{s'}(p_1')\bar u^{s'}(p_1') = \slashed p_1' + m_e$. All spinor indices are now contracted in a ring, which is a trace ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|Theorem §C8a.7.3]], Steps 1–4, with this completeness relation in both places):
>
> $$
> \sum_{s, s'}\bigl[\bar u^{s'}(p_1')\gamma^\mu u^s(p_1)\bigr]\bigl[\bar u^s(p_1)\gamma^\nu u^{s'}(p_1')\bigr] = \operatorname{tr}\bigl[(\slashed p_1' + m_e)\gamma^\mu(\slashed p_1 + m_e)\gamma^\nu\bigr] .
> $$
>
> No fermion wave function is left.
>
> **Step 5** (the muon line). The same three steps with $p_1 \to p_2$, $p_1' \to p_2'$, $m_e \to m_\mu$ and the indices lowered: $\operatorname{tr}\bigl[(\slashed p_2' + m_\mu)\gamma_\mu(\slashed p_2 + m_\mu)\gamma_\nu\bigr]$.
>
> **Step 6** (the average). The factor $\frac14$ of [[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1|Def. §C8a.7.1]], for the two spin states of each initial particle.
>
> **What the derivation shows.**
> - The procedure is that of the annihilation process step for step, with the same numerical factors ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4|Theorem §C8a.7.4]]). What must be watched on each leg is whether it is a particle or an antiparticle and what its momentum is called.
> - ⚑ By-product: the only difference from annihilation is the sign of two of the four mass terms, $(\slashed p' - m_e) \leftrightarrow (\slashed p_1' + m_e)$ and $(\slashed k' - m_\mu) \leftrightarrow (\slashed p_2 + m_\mu)$: the two legs that were antiparticles there → [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]].

^der-c8a-12-2

*Uses:* [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|Theorem §C8a.12.1]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1|Def. §C8a.7.1]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-2|Theorem §C8a.7.2]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|Theorem §C8a.7.3]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-3|P8, step 3]]

## Comparison with annihilation

![[ph-qft-c8-18-2.svg]]
*ADDED figure (after PHY 513 Lecture 21, slide 6, and PS p. 153): the two diagrams, each with its own direction of time. Black legs are the same particle with a new name; red legs are crossed: the incoming positron of (a) corresponds to the outgoing electron of (b), the outgoing antimuon of (a) to the incoming muon of (b).*

> [!theorem] Theorem §C8a.12.3: The Crossing Substitution Maps Annihilation onto Scattering
> The two processes, side by side:
>
> | | $e^-e^+ \to \mu^-\mu^+$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2\|Theorem §C8a.6.2]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4\|Theorem §C8a.7.4]]) | $e^-\mu^- \to e^-\mu^-$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1\|Theorem §C8a.12.1]], [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2\|Theorem §C8a.12.2]]) |
> |---|---|---|
> | particles | in: $e^-(p)$, $e^+(p')$; out: $\mu^-(k)$, $\mu^+(k')$ | in: $e^-(p_1)$, $\mu^-(p_2)$; out: $e^-(p_1')$, $\mu^-(p_2')$ |
> | $i\mathcal M$ | $\frac{ie^2}{q^2}\bigl[\bar v(p')\gamma^\mu u(p)\bigr]\bigl[\bar u(k)\gamma_\mu v(k')\bigr]$ | $\frac{ie^2}{q^2}\bigl[\bar u(p_1')\gamma^\mu u(p_1)\bigr]\bigl[\bar u(p_2')\gamma_\mu u(p_2)\bigr]$ |
> | photon | $q = p + p'$, $q^2 = E_{\rm cm}^2 > 0$ | $q = p_1 - p_1'$, $q^2 \le 0$ |
> | completeness used | $\sum u\bar u = \slashed p + m$ and $\sum v\bar v = \slashed k - m$ | $\sum u\bar u = \slashed p + m$ only |
> | electron trace | $\operatorname{tr}\bigl[(\slashed p' - m_e)\gamma^\mu(\slashed p + m_e)\gamma^\nu\bigr]$ | $\operatorname{tr}\bigl[(\slashed p_1' + m_e)\gamma^\mu(\slashed p_1 + m_e)\gamma^\nu\bigr]$ |
> | muon trace | $\operatorname{tr}\bigl[(\slashed k + m_\mu)\gamma_\mu(\slashed k' - m_\mu)\gamma_\nu\bigr]$ | $\operatorname{tr}\bigl[(\slashed p_2' + m_\mu)\gamma_\mu(\slashed p_2 + m_\mu)\gamma_\nu\bigr]$ |
>
> In both columns $\frac14\sum_{\rm spins}|\mathcal M|^2 = \frac{e^4}{4q^4}\,(\text{electron trace})\,(\text{muon trace})$. The substitution
>
> $$
> p \to p_1 , \qquad p' \to -p_1' , \qquad k \to p_2' , \qquad k' \to -p_2
> $$
>
> turns the left column into the right one:
> 1. $q = p + p' \to p_1 - p_1'$, the photon momentum of the scattering diagram;
> 2. the electron trace goes to minus the scattering electron trace, and the muon trace to minus the scattering muon trace: one sign for each crossed fermion line. There are two, so the product of the traces, and with it $\frac14\sum|\mathcal M|^2$, is reproduced with no sign;
> 3. two of the four replacements are new names for the same particle: $p \to p_1$ for the incoming electron, $k \to p_2'$ for the outgoing muon. The other two cross a leg: the incoming positron of momentum $p'$ becomes the outgoing electron of momentum $p_1' = -p'$, and the outgoing antimuon of momentum $k'$ becomes the incoming muon of momentum $p_2 = -k'$. What counts on each leg is whether it is a particle or an antiparticle, whether it comes in or goes out, and the sign of its momentum;
> 4. the equality is one between functions of four four-vectors. The arguments $-p_1'$ and $-p_2$ have negative energy, so they are not momenta of a physical positron or antimuon: no physical annihilation event is mapped to a physical scattering event ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-2|Principle §C8a.14.2]]).
>
> This is the first instance of crossing symmetry ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]]), used twice; the sign of item 2 is the general fermion sign ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]]).
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, the spin-averaged squares, both masses as written on the slides, the traces not evaluated.
>
> *Source: PHY 513 Lecture 21, slides 6–7 (the two diagrams, amplitudes and trace forms side by side, with "Completeness: $\sum_su^s(p)\bar u^s(p) = \slashed p + m$" and "Completeness: $\sum_rv^r(k)\bar v^r(k) = \slashed k - m$"), slide 8 ("Substitutions: $p \to p_1$, $k \to p_2'$, $p' \to -p_1'$, $k' \to -p_2$"), and recording, part A · PS §5.4, p. 153, eq. (5.60) ("This is exactly the same as our result (5.4) for $e^+e^- \to \mu^+\mu^-$, with the replacements") · items 2 and 4 derived here; checked numerically (`qft-C/tools/l21/verify.py`)*

^thm-c8a-12-3

> [!derivation]- Derivation
> **Step 1** (the photon momentum). $q = p + p' \to p_1 + (-p_1') = p_1 - p_1'$. At the other vertex, $q = k + k' \to p_2' - p_2$, the same four-vector by momentum conservation.
>
> **Step 2** (the electron trace). $\slashed p'$ is linear in $p'$, so $p' \to -p_1'$ gives $\slashed p' - m_e \to -\slashed p_1' - m_e = -(\slashed p_1' + m_e)$, and $\slashed p + m_e \to \slashed p_1 + m_e$:
>
> $$
> \operatorname{tr}\bigl[(\slashed p' - m_e)\gamma^\mu(\slashed p + m_e)\gamma^\nu\bigr] \;\to\; -\operatorname{tr}\bigl[(\slashed p_1' + m_e)\gamma^\mu(\slashed p_1 + m_e)\gamma^\nu\bigr] .
> $$
>
> **Step 3** (the muon trace). $\slashed k + m_\mu \to \slashed p_2' + m_\mu$ and $\slashed k' - m_\mu \to -\slashed p_2 - m_\mu = -(\slashed p_2 + m_\mu)$:
>
> $$
> \operatorname{tr}\bigl[(\slashed k + m_\mu)\gamma_\mu(\slashed k' - m_\mu)\gamma_\nu\bigr] \;\to\; -\operatorname{tr}\bigl[(\slashed p_2' + m_\mu)\gamma_\mu(\slashed p_2 + m_\mu)\gamma_\nu\bigr] .
> $$
>
> **Step 4** (the product). $(-1)(-1) = +1$, and the prefactor $\frac{e^4}{4q^4}$ goes to itself by Step 1: the annihilation expression of [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4|Theorem §C8a.7.4]] becomes the scattering expression of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2|Theorem §C8a.12.2]].
>
> **Step 5** (what the substitution preserves). The mass-shell conditions go to mass-shell conditions, $p'^2 = m_e^2 \to p_1'^2 = m_e^2$ and $k'^2 = m_\mu^2 \to p_2^2 = m_\mu^2$, and momentum conservation to momentum conservation, $p + p' = k + k' \to p_1 - p_1' = p_2' - p_2$. The substituted momenta therefore satisfy the relations of the scattering process.
>
> **Step 6** (the amplitudes). The two amplitudes of the table have the same structure, but the substitution does not turn one into the other literally: $\bar v(p')$ is a wave function of a positron of positive energy, and no such spinor is assigned to $-p_1'$. What is compared here is the spin sum of each line, where the wave functions have been traded for $\slashed p \pm m$. ⚑ By-product: in the completeness relations the replacement of a particle by an antiparticle of the opposite momentum is off by an overall sign → [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-3|Theorem §C8a.14.3]].
>
> **What the derivation shows.**
> - The work of contracting the two traces need not be repeated: the result of [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] can be used again → [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-4|Theorem §C8a.12.4]].
> - ⚑ By-product: the sign that distinguishes $\slashed p + m$ from $\slashed k - m$ is what remains, in the trace, of a leg having been an antiparticle.

^der-c8a-12-3

*Uses:* [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4|Theorem §C8a.7.4]], [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-2|Theorem §C8a.12.2]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams|P8, Shortcut: crossing]]

> [!remark] Remark: The same symbol q for two different photons
> In both diagrams $q$ is whatever four-momentum conservation requires at a vertex, but the two photons are far apart. In annihilation $q = p + p'$ is the total momentum: in the centre-of-mass frame it has no three-momentum and the full energy $E_{\rm cm}$, at least the rest energy of the pair, so $q^2$ is positive and never small ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-3|Theorem §C8a.6.3]]). In scattering $q = p_1 - p_1'$ is what the electron hands over: its energy component is the energy the electron loses, which may have either sign, since the electron may as well gain energy from the muon; in the centre-of-mass frame it vanishes ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]]). $q^2$ is negative and can be as small as one likes, down to zero in the forward direction. The formulas are related by a substitution; the regions in which they are used are not.
>
> *Source: PHY 513 Lecture 21, recording, part A · the centre-of-mass values from the theorems linked*

^rem-c8a-12-2

## The result

> [!theorem] Theorem §C8a.12.4: The Spin-Averaged Squared Amplitude for Electron–Muon Scattering
> For $e^-(p_1) + \mu^-(p_2) \to e^-(p_1') + \mu^-(p_2')$ at order $e^2$ with $m_e = 0$ and $q = p_1 - p_1'$,
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2 = \frac{8e^4}{q^4}\Bigl[(p_1\cdot p_2')(p_1'\cdot p_2) + (p_1\cdot p_2)(p_1'\cdot p_2') - m_\mu^2\,p_1\cdot p_1'\Bigr] .
> $$
>
> 1. It is the annihilation result at $m_e = 0$, $\frac{8e^4}{q^4}\bigl[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k) + m_\mu^2\,p\cdot p'\bigr]$ ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]]), with the substitution of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]: no trace is evaluated anew.
> 2. Each product of two dot products picks up two minus signs, which cancel; the mass term picks up one, $p\cdot p' \to -p_1\cdot p_1'$.
> 3. The prefactor $\frac{1}{q^4}$ is no longer $\frac{1}{E_{\rm cm}^4}$: $q^2 = -2p_1\cdot p_1'$ depends on the scattering angle and vanishes in the forward direction ([[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-2|Theorem §C8a.13.2]]).
> 4. Checked numerically against the explicit sum over the sixteen spin combinations of $u$ spinors, with $m_e = 0$ and $m_\mu \ne 0$.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, unpolarized, on-shell external momenta, $m_e = 0$ as lectured, the muon mass kept, any frame, $p_1' \ne p_1$.
>
> *Source: PHY 513 Lecture 21, slide 8 ("Result for annihilation amplitude (with $m_e^2 = 0$) … Substitutions give corresponding scattering amplitude"; the two formulas as printed there: Caution below), slide 12 ("$\frac14\sum_{\rm spin}|\mathcal M|^2 = \frac{8e^4}{q^4}\bigl[(p_1p_2')(p_1'p_2) + (p_1p_2)(p_1'p_2') - m_\mu^2(p_1p_1')\bigr]$"), and recording, part A · PS §5.4, p. 154, eq. (5.61) ("So instead of evaluating the traces from scratch, we can just make the same replacements in our previous result, Eq. (5.10). Setting $m_e = 0$, we find") · numerical check: `qft-C/tools/l21/verify.py`*

^thm-c8a-12-4

> [!derivation]- Derivation
> **Step 1** (the starting point). [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] with $m_e = 0$, where the terms $m_e^2\,k\cdot k'$ and $2m_e^2m_\mu^2$ are absent ([[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]], Step 1):
>
> $$
> \frac14\sum_{\rm spins}|\mathcal M|^2\Big|_{e^-e^+ \to \mu^-\mu^+} = \frac{8e^4}{q^4}\Bigl[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k) + m_\mu^2\,p\cdot p'\Bigr] , \qquad q = p + p' .
> $$
>
> **Step 2** (the first product). $p\cdot k \to p_1\cdot p_2'$ and $p'\cdot k' \to (-p_1')\cdot(-p_2) = p_1'\cdot p_2$: two signs, which cancel. So $(p\cdot k)(p'\cdot k') \to (p_1\cdot p_2')(p_1'\cdot p_2)$.
>
> **Step 3** (the second product). $p\cdot k' \to p_1\cdot(-p_2) = -p_1\cdot p_2$ and $p'\cdot k \to (-p_1')\cdot p_2' = -p_1'\cdot p_2'$: again two signs. So $(p\cdot k')(p'\cdot k) \to (p_1\cdot p_2)(p_1'\cdot p_2')$.
>
> **Step 4** (the mass term). $p\cdot p' \to p_1\cdot(-p_1') = -p_1\cdot p_1'$: one sign, and $m_\mu^2\,p\cdot p' \to -m_\mu^2\,p_1\cdot p_1'$.
>
> **Step 5** (the prefactor). $q^4 = \bigl((p + p')^2\bigr)^2 \to \bigl((p_1 - p_1')^2\bigr)^2$ ([[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]], 1). With $m_e = 0$, $q^2 = p_1^2 + p_1'^2 - 2p_1\cdot p_1' = -2p_1\cdot p_1'$.
>
> **Step 6** (collect). The three terms of Steps 2–4 with the prefactor of Step 5 are the statement.
>
> **What the derivation shows.**
> - The overall sign of [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]], item 2, has already cancelled between the two lines; the signs seen here are those of the individual dot products.
> - ⚑ By-product: the expression is positive, as a sum of squared moduli must be, although the mass term is negative: in the centre-of-mass frame it is [[§C8a.13 The Cross Section for Electron–Muon Scattering#^thm-c8a-13-3|Theorem §C8a.13.3]].
> - The invariant form is the starting point for any frame; the centre-of-mass frame is [[§C8a.13 The Cross Section for Electron–Muon Scattering|§C8a.13]].

^der-c8a-12-4

*Uses:* [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]], [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-3|Theorem §C8a.12.3]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-4|P8, step 4]]

> [!caution] Caution: Two misprints on slide 8
> Slide 8 prints the annihilation result as $\frac{8e^4}{q^4}\bigl[(pk')(p'k) + (p'k)(pk') + m_\mu^2\,pp'\bigr]$, the same product twice. The two products are different: $(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)$, as in [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] and on slide 15 of Lecture 19. It prints the first term of the scattering result as $(p_1p_2')(p_1p_2)$; the term is $(p_1\cdot p_2')(p_1'\cdot p_2)$, as on slide 12 and in PS (5.61), and the recording says so at this slide. With the printed forms the two sides do not agree numerically.
>
> *Source: PHY 513 Lecture 21, slides 8, 12, and recording, part A · PS §5.4, eq. (5.61) · numerical comparison: `qft-C/tools/l21/verify.py`; recorded in `qft-C/ERRATA.md`*

^cau-c8a-12-1

> [!remark]- Connections
> - The diagram is the one-photon exchange of Lecture 18, there taken to the nonrelativistic limit, where it gives the Coulomb potential and the repulsion of like charges — [[§C8a.4 Feynman Rules for QED#^ex-c8a-4-1|Example §C8a.4.1]], [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-3|Theorem §C8a.5.3]], [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-7|Theorem §C8a.5.7]].
> - The amplitude, the square and the traces repeat the annihilation computation step for step — [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4|Theorem §C8a.7.4]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]]; the general rule for any fermion line, of which both processes are cases — [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]].
> - The two completeness relations whose difference is the crossing sign — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]].
> - The annihilation photon is timelike, the scattering photon spacelike; a real photon lies between the two — [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]].
> - The steps as a procedure, with crossing as a shortcut for steps 3–4 — [[P8 Unpolarized Cross Section from Diagrams|P8]].
> - Forward: the centre-of-mass frame, the cross section and the forward peak — [[§C8a.13 The Cross Section for Electron–Muon Scattering|§C8a.13]]; the substitution as a general symmetry, and the two results as one function of the Mandelstam variables — [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^pr-c8a-14-1|Principle §C8a.14.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-6|Theorem §C8a.14.6]].
> - With two identical fermions in place of $e^-$ and $\mu^-$ the diagram with the outgoing momenta exchanged is present as well, with a relative minus sign: the amplitude of $e^-e^- \to e^-e^-$ in the helicity basis (Problem Set 11, Problem 2) — [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]].
