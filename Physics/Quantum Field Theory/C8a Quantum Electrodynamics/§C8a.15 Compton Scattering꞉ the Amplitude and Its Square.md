---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
section: C8a.15
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.14 Crossing Symmetry and Mandelstam Variables|§C8a.14]] · ↑ [[· C8a Quantum Electrodynamics]] · [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations|§C8a.16]] →

*Sources: PHY 513 Lecture 22 (Larsen, 23 Nov 2026, "Compton Scattering"), slides 2–10 (Part A), and transcript · the user's PHY 513 notes, Lecture 22 update, chapter opening (Principle "Tools for this chapter (the lecture's cheat sheet)"), §22.1 "The amplitude" (Derivation "Reading off the first diagram", paragraphs "What is new", "Corrections from the class", subsections "Simplifying" with Derivation "Numerators: using the Dirac equation", "Squaring" with paragraphs "One trace of eight", "Which invariants?" and Principle "Spin-averaged Compton scattering"), Caution "Slips in the slides", paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.5, pp. 158–162: the unnumbered displays of pp. 158–159, eqs. (5.74), (5.81), (5.82), (5.87) (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.6, eqs. (8.321)–(8.324); §8.6.2, eqs. (8.348)–(8.349), (8.380)–(8.383) (page images of the current build checked).*

What does a photon do when it hits an electron? Lecture 22, the last of the four lectures on QED processes, studies Compton scattering, $\gamma e^- \to \gamma e^-$: a photon and an electron come in, and a photon and an electron go out with changed momenta. The photon scatters as a particle. Three features are new compared with [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon|§C8a.6]]–[[§C8a.14 Crossing Symmetry and Mandelstam Variables|§C8a.14]]:
1. **external photons**: no earlier process had a photon in the initial or the final state. Each brings a polarization vector ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]]);
2. **a virtual electron**: the internal line is a fermion, which does not satisfy $q^2 = m^2$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]]). Its propagator is the Dirac propagator $S_F$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]), and the spinor indices are no longer closed off vertex by vertex: the incoming electron's $\hat\psi$ and the outgoing electron's $\hat{\bar\psi}$ sit at different vertices, with the propagator between them;
3. **two diagrams**: the same initial and final states are attached in two different ways, so the square contains interference terms and more algebra.

The lecture has three parts, and the notes follow them:
- **A, the Feynman diagrams** (this section): the amplitude ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]]), its simplification with the Dirac equation ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]]), and its square, one trace of eight $\gamma$'s for each term ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]]);
- **B, the Ward identity** ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations|§C8a.16]]): why the sum over the two physical photon polarizations may be replaced by $-g_{\mu\nu}$;
- **C, the physics of Compton scattering** ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy|§C8a.17]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering|§C8b.10]]): the Compton formula, the Klein–Nishina and Thomson cross sections, the backward peak at high energy and its helicity suppression.

**The mathematical picture.** The amplitude is linear in the polarization vector of the incoming photon and antilinear in that of the outgoing one: $\mathcal M = \epsilon^\ast_\mu(k')\,\epsilon_\nu(k)\,\mathcal M^{\mu\nu}$ with a tensor $\mathcal M^{\mu\nu}$ of two Lorentz indices. In spinor space, $\mathcal M^{\mu\nu} = -e^2\,\bar u(p')\,\Gamma^{\mu\nu}\,u(p)$, where each $\Gamma^{\mu\nu}$ is a $4\times4$ matrix, a sum of products of three and of one $\gamma$ matrices ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-8|Theorem §C5a.13.8]]), between the row $\bar u(p')$ and the column $u(p)$: one fermion line read against its arrow ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). The spin sum of the square is therefore a single trace over spinor space ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], part 2), and the polarization sums contract the Lorentz indices.

**Setup.** [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]], QED with the electron field, in the interaction picture; free relativistic states over $|0\rangle$ in place of the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]); order $e^2$, the lowest order of the process, where the rules are exact ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]). External photons are physical, that is transverse ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]], [[§C8a.4 Feynman Rules for QED#^def-c8a-4-2|Def. §C8a.4.2]]). The electron mass $m > 0$ is kept throughout.

*Conventions* ([[Larsen PHY 513]]): incoming electron $e^-(p)$ and photon $\gamma(k)$, outgoing electron $e^-(p')$ and photon $\gamma(k')$; $p^2 = p'^2 = m^2$, $k^2 = k'^2 = 0$, $p + k = p' + k'$. The index $\nu$ belongs to the incoming photon and $\mu$ to the outgoing one, in both diagrams. Spin labels on $u(p)$, $\bar u(p')$ and polarization labels on $\epsilon_\nu(k)$, $\epsilon^\ast_\mu(k')$ are suppressed. $e$ as in [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^cau-c8a-1-1|§C8a.1, Caution: What e means]]. Abbreviations used in the derivations of this section only: $a = p\cdot k$ and $b = p\cdot k'$, written there with $\equiv$. Yu labels the momenta $k_1$, $k_2$ (incoming electron, photon) and $p_1$, $p_2$ (outgoing electron, photon).

## The two diagrams and the amplitude

> [!theorem] Theorem §C8a.15.1: The Amplitude for Compton Scattering
> ![[ph-qft-c8a-15-1.svg]]
> *The two diagrams at order $e^2$, time running upward (after PHY 513 Lecture 22, slides 5–6, and PS p. 158). Line arrows are fermion number ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]), orange arrows momenta. The internal line is a virtual electron, not a photon.*
>
> In [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]], for $\gamma(k) + e^-(p) \to \gamma(k') + e^-(p')$ at order $e^2$:
> 1. exactly two diagrams contribute. In (a) the electron absorbs the incoming photon and later emits the outgoing one; in (b) it first emits the outgoing photon and only later absorbs the incoming one;
> 2. their sum is
>
> $$
> \begin{aligned}
> i\mathcal M &= \bar u(p')\,(-ie\gamma^\mu)\,\epsilon^\ast_\mu(k')\;\frac{i(\slashed p + \slashed k + m)}{(p + k)^2 - m^2}\;(-ie\gamma^\nu)\,\epsilon_\nu(k)\,u(p) \;+\; \bar u(p')\,(-ie\gamma^\nu)\,\epsilon_\nu(k)\;\frac{i(\slashed p - \slashed k' + m)}{(p - k')^2 - m^2}\;(-ie\gamma^\mu)\,\epsilon^\ast_\mu(k')\,u(p) \\
> &= -ie^2\,\epsilon^\ast_\mu(k')\,\epsilon_\nu(k)\;\bar u(p')\,\Gamma^{\mu\nu}\,u(p) , \qquad \Gamma^{\mu\nu} \equiv \frac{\gamma^\mu(\slashed p + \slashed k + m)\gamma^\nu}{(p + k)^2 - m^2} + \frac{\gamma^\nu(\slashed p - \slashed k' + m)\gamma^\mu}{(p - k')^2 - m^2} ;
> \end{aligned}
> $$
>
> 3. both terms have $\bar u(p')$ on the far left and $u(p)$ on the far right. They differ in the string vertex–propagator–vertex between them: the two photon vertices are interchanged along the fermion line, and the internal momentum is $p + k$ in (a) and $p - k'$ in (b);
> 4. the incoming photon contributes its wave function $\epsilon_\nu(k)$, the outgoing one the complex conjugate $\epsilon^\ast_\mu(k')$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]]). The polarization vectors are numbers that contract the Lorentz indices of the vertices, so they may be written outside the spinor string;
> 5. the two diagrams enter with the same sign ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-2|Theorem §C8a.15.2]]), and the $i\varepsilon$ of the propagators has been dropped ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]).
>
> In the language of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-2|Def. §C8a.14.2]], with the incoming pair $p$, $k$ and the outgoing pair $p'$, $k'$: (a) is the $s$-channel diagram, internal momentum squared $(p + k)^2 = s$, and (b) the $u$-channel diagram, $(p - k')^2 = u$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$ (the lowest), free states over $|0\rangle$, any spins and any physical polarizations, $m > 0$.
>
> *Source: PHY 513 Lecture 22, slide 5 ("Several new features: External photons. A virtual electron ⇒ fermion propagator ⇒ spinor indices not contracted at each vertex independently. Two diagrams ⇒ interference and more algebra"), slide 6 ("$= \bar u(p')(-ie\gamma^\mu)\epsilon^\ast_\mu(k')\frac{i(\slashed p + \slashed k + m)}{(p + k)^2 - m^2}(-ie\gamma^\nu)\epsilon_\nu(k)u(p) + \bar u(p')(-ie\gamma^\nu)\epsilon_\nu(k)\frac{i(\slashed p - \slashed k' + m)}{(p - k')^2 - m^2}(-ie\gamma^\mu)\epsilon^\ast_\mu(k')u(p)$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1 (Derivation "Reading off the first diagram", eq. for $i\mathcal M$; the channel names filled in by the user's notes) · PS §5.5, pp. 158–159 (the displays before eq. (5.74)) · Yu §8.6, eq. (8.321)*

^thm-c8a-15-1

> [!derivation]- Derivation
> **Step 1** (which diagrams). One photon in and one out need two photon fields, hence two vertices: order $e^2$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]], 1). Each vertex holds $\hat{\bar\psi}\gamma^\mu\hat\psi\,\hat A_\mu$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]). The two photon fields contract with the two external photons; of the four fermion fields, one $\hat\psi$ annihilates the incoming electron and one $\hat{\bar\psi}$ creates the outgoing one ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). If these two sat at the same vertex, the other vertex would be left with a $\hat\psi$ and a $\hat{\bar\psi}$ contracted with each other at one point: a closed loop attached to one photon, a disconnected piece, not part of $i\mathcal M$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]]: connected diagrams). So they sit at different vertices, and the remaining $\hat\psi$ and $\hat{\bar\psi}$ are contracted into a propagator between the vertices. What is left free is which vertex takes which photon: two diagrams.
>
> **Step 2** (diagram (a), the lower vertex). Start where the electron comes in. One of the three fields at the lower vertex must annihilate it; $\hat\psi$ can, and what is left is its wave function $u(p)$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]). The photon field at this vertex annihilates the incoming photon and leaves the photon wave function, $e^{-ik\cdot x}$ times the polarization vector $\epsilon_\nu(k)$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]]); the plane wave goes into momentum conservation. The vertex factor $-ie\gamma^\nu$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]) contracts the photon's Lorentz index. So far:
>
> $$
> (-ie\gamma^\nu)\,\epsilon_\nu(k)\,u(p) .
> $$
>
> This is a column: the spinor index of the $\hat{\bar\psi}$ of this vertex is still open.
>
> **Step 3** (diagram (a), the propagator). The open index is taken up by the propagator of the virtual electron. Momentum conservation at the lower vertex gives it the momentum $p + k$ along the arrow ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]], table):
>
> $$
> \frac{i(\slashed p + \slashed k + m)}{(p + k)^2 - m^2 + i\varepsilon} .
> $$
>
> The numerator is a matrix: the momenta are slashed.
>
> **Step 4** (diagram (a), the upper vertex). The $\hat{\bar\psi}$ of the upper vertex creates the outgoing electron and leaves $\bar u(p')$; antiparticles play no role. The vertex is $-ie\gamma^\mu$, with a new index. The photon field is real ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-2|Theorem §C8a.3.2]]): its annihilation part carries $\epsilon$ and its creation part the complex conjugate, so the outgoing photon gives $\epsilon^\ast_\mu(k')$. Written against the arrow, from the outgoing electron back to the incoming one:
>
> $$
> \bar u(p')\,(-ie\gamma^\mu)\,\epsilon^\ast_\mu(k')\;\frac{i(\slashed p + \slashed k + m)}{(p + k)^2 - m^2 + i\varepsilon}\;(-ie\gamma^\nu)\,\epsilon_\nu(k)\,u(p) .
> $$
>
> **Step 5** (diagram (b)). The same electrons: $u(p)$ on the right, $\bar u(p')$ on the left. Now the lower vertex, the one that absorbs the incoming electron, attaches to the outgoing photon: $(-ie\gamma^\mu)\epsilon^\ast_\mu(k')u(p)$. The electron has emitted a photon, so the internal momentum is $p - k'$ (equal to $p' - k$ by momentum conservation). The upper vertex absorbs the incoming photon, $(-ie\gamma^\nu)\epsilon_\nu(k)$:
>
> $$
> \bar u(p')\,(-ie\gamma^\nu)\,\epsilon_\nu(k)\;\frac{i(\slashed p - \slashed k' + m)}{(p - k')^2 - m^2 + i\varepsilon}\;(-ie\gamma^\mu)\,\epsilon^\ast_\mu(k')\,u(p) .
> $$
>
> **Step 6** (collect). In each term $(-ie)\cdot i\cdot(-ie) = i\,(-i)^2e^2 = -ie^2$. The polarization vectors are numbers and are moved to the front. The two terms are added with the same sign ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-2|Theorem §C8a.15.2]]), and $i\varepsilon$ is dropped ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]). This is the statement.
>
> **What the derivation shows.**
> - ⚑ By-product: an external photon is handled like an external fermion, with $\epsilon_\nu$ or $\epsilon^\ast_\mu$ in place of $u$ or $\bar u$; the new element is that the fermion line now runs through two vertices, with a matrix-valued propagator between them.
> - ⚑ By-product: the polarization vectors contract every Lorentz index, so the amplitude is a number. Squared and summed over polarizations, they must be eliminated: [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^def-c8a-15-1|Def. §C8a.15.1]], [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]].
> - The structure $\epsilon^\ast_\mu(k')\,\mathcal M^{\mu\nu}\epsilon_\nu(k)$ is the starting point of the Ward identity: [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]].

^der-c8a-15-1

*Uses:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]], [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-2|Theorem §C8a.3.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-1|P8, step 1]], [[P8 Unpolarized Cross Section from Diagrams#^p8-2|P8, step 2]]; [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!theorem] Theorem §C8a.15.2: The Two Compton Diagrams Have the Same Sign
> The diagrams (a) and (b) of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]] enter $i\mathcal M$ with a relative $+$. In both, the external electrons are contracted in the same way: the incoming electron with the $\hat\psi$ of one vertex, the outgoing electron with the $\hat{\bar\psi}$ of the other, and the remaining pair into the propagator. The diagrams differ only in which photon field is contracted with which external photon, and photon contractions bring no sign ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]]).
>
> *Equivalently,* this is [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]], item 3: diagrams related by exchanging two bosons enter with a relative $+$, as in the Yukawa process of [[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]]. The contrast is the exchange of two identical fermions, which gives a relative $-$ ([[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]).
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$; states ordered as in [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]. The relative sign is physical: it fixes the sign of the interference term ([[§C6d.5 Second Order#^thm-c6d-5-5|Theorem §C6d.5.5]]).
>
> *Source: the user's PHY 513 notes, Lecture 22 update, §22.1 ("The two diagrams have the same sign: the external fermions are contracted the same way in both") · PS §5.5, p. 158 ("since the fermion portions of the two diagrams are identical, there is no relative minus sign between the two terms") · Yu §8.6, the paragraph after eq. (8.321)*

^thm-c8a-15-2

> [!derivation]- Derivation
> **Step 1** (the term). At second order the Dyson series gives $\frac{1}{2!}(-ie)^2\int d^4x\,d^4y\;\langle f|\,T\bigl\{\hat{\bar\psi}\gamma^\mu\hat\psi\hat A_\mu(x)\;\hat{\bar\psi}\gamma^\nu\hat\psi\hat A_\nu(y)\bigr\}|i\rangle$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]).
>
> **Step 2** (one fermion pattern). Fix the fermion contractions: $\hat\psi(y)$ with the incoming electron, $\hat{\bar\psi}(x)$ with the outgoing electron, and $\hat\psi(x)$ with $\hat{\bar\psi}(y)$ into $S_F(x - y)$. This pattern has one sign $(-1)^{\#\text{crossings}}$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]), whatever the photon fields do.
>
> **Step 3** (two photon patterns). For this fermion pattern the photon fields can be contracted in two ways: $\hat A_\nu(y)$ with the incoming photon and $\hat A_\mu(x)$ with the outgoing one, which is diagram (a); or $\hat A_\mu(x)$ with the incoming photon and $\hat A_\nu(y)$ with the outgoing one, which is diagram (b). The photon operators commute with each other and with the Dirac operators ([[§C8a.4 Feynman Rules for QED#^def-c8a-4-2|Def. §C8a.4.2]]), so moving them brings no sign ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]]). Both diagrams carry the sign of Step 2.
>
> **Step 4** (the $\frac{1}{2!}$). The other fermion pattern, with $x$ and $y$ exchanged, gives the same two diagrams again after renaming the integration variables; the vertices are even in fermion fields and move without sign. The factor 2 cancels the $\frac{1}{2!}$ ([[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]]).
>
> **What the derivation shows.**
> - The relative sign is decided by the fermion contractions alone, and they are the same in the two diagrams.
> - The overall sign, that of Step 2, is $+$ with one fermion in and one out; it drops out of $|\mathcal M|^2$.

^der-c8a-15-2

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-2|Theorem §C8a.4.2]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]], [[§C8a.4 Feynman Rules for QED#^def-c8a-4-2|Def. §C8a.4.2]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.5 Second Order#^thm-c6d-5-2|Theorem §C6d.5.2]], [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]

> [!remark] Remark: Checks on an amplitude before computing with it
> An expression of this size has a fair amount of redundancy to check against, before any algebra:
> 1. every Lorentz index is contracted, and each index appears exactly twice: here $\mu$ joins $\epsilon^\ast_\mu(k')$ to one $\gamma^\mu$ and $\nu$ joins $\epsilon_\nu(k)$ to one $\gamma^\nu$ in each term;
> 2. each momentum sits on the right external particle: $u(p)$, $\bar u(p')$, $\epsilon_\nu(k)$, $\epsilon^\ast_\mu(k')$, and the internal momentum of each propagator is the one fixed by its vertices ($p + k$ where the incoming photon has been absorbed, $p - k'$ where the outgoing one has been emitted);
> 3. the numerators of fermion propagators are matrices, $\slashed p + \slashed k + m$ with slashes;
> 4. the polarization vectors stand outside the string of matrices, and the spinors at its two ends.
>
> *Source: PHY 513 Lecture 22, transcript (the three corrections made to the board version: slashed numerators, $k$ in place of $k'$ in the first numerator, an index used twice) · the user's PHY 513 notes, Lecture 22 update, §22.1, paragraph "Corrections from the class"*

^rem-c8a-15-1

## Simplifying the amplitude

> [!theorem] Theorem §C8a.15.3: The Denominators of the Two Propagators
> For on-shell external momenta, $p^2 = m^2$ and $k^2 = k'^2 = 0$,
>
> $$
> (p + k)^2 - m^2 = 2\,p\cdot k , \qquad (p - k')^2 - m^2 = -2\,p\cdot k' .
> $$
>
> 1. Only the cross terms survive: the whole virtuality of the internal electron is in them.
> 2. For $m > 0$, $p\cdot k > 0$ and $p\cdot k' > 0$. The first denominator is positive and the second negative: they differ by more than a sign, and neither vanishes.
> 3. The virtual electron is off shell in both diagrams ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]], [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^pr-c8a-6-4|Principle §C8a.6.4]]): $(p + k)^2 > m^2$ in (a) and $(p - k')^2 < m^2$ in (b).
> 4. Since neither denominator vanishes for physical momenta, the $i\varepsilon$ of the propagators plays no role and is dropped.
>
> *Model:* kinematics; *applies:* on-shell external momenta with $m > 0$. For $m = 0$ the second denominator vanishes when $\mathbf k'$ is parallel to $\mathbf p$; at high energy it becomes small near that configuration ([[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]]).
>
> *Source: PHY 513 Lecture 22, slide 7 ("Denominators: $p^2 = m^2$, $k^2 = 0 = k'^2$ ⇒ $(p + k)^2 - m^2 = 2p\cdot k$, $(p - k')^2 - m^2 = -2p\cdot k'$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, subsection "Simplifying" · PS §5.5, p. 159 · Yu §8.6, eq. (8.322) · items 2–4 written out here*

^thm-c8a-15-3

> [!derivation]- Derivation
> **Step 1** (expand). $(p + k)^2 - m^2 = p^2 + 2p\cdot k + k^2 - m^2$. The real electron has $p^2 = m^2$, which cancels the $-m^2$; the real photon has $k^2 = 0$. What remains is $2p\cdot k$.
>
> **Step 2** (the second). $(p - k')^2 - m^2 = p^2 - 2p\cdot k' + k'^2 - m^2 = -2p\cdot k'$, by $p^2 = m^2$ and $k'^2 = 0$.
>
> **Step 3** (the signs). $p\cdot k$ is a Lorentz scalar; in the rest frame of the incoming electron, $p = (m, \mathbf 0)$ and $k = (\omega, \mathbf k)$ with $\omega = |\mathbf k| > 0$, it equals $m\omega > 0$. The same argument gives $p\cdot k' = m\omega' > 0$.
>
> **Step 4** (off shell). $(p + k)^2 = m^2 + 2p\cdot k > m^2$ and $(p - k')^2 = m^2 - 2p\cdot k' < m^2$: neither internal momentum is on the mass shell $q^2 = m^2$.
>
> **What the derivation shows.**
> - ⚑ By-product: with $m = 0$, $p\cdot k' = |\mathbf p|\,|\mathbf k'|\,(1 - \cos\angle(\mathbf p, \mathbf k'))$ can vanish; the electron mass is what keeps the second propagator finite → [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-8|Theorem §C8a.17.8]].
> - $p\cdot k$ and $p\cdot k'$ are the two invariants in which the whole result is expressed: [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|Theorem §C8a.15.8]].

^der-c8a-15-3

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]], [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^def-c8a-6-2|Def. §C8a.6.2]]

> [!theorem] Lemma §C8a.15.4: The Dirac Equation Simplifies the Numerator
> For $p^2 = m^2$ and $u(p)$ a positive-frequency spinor ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]]):
> 1. $(\slashed p + m)\,\gamma^\nu\,u(p) = 2p^\nu\,u(p)$;
> 2. $\bar u(p)\,\gamma^\nu\,(\slashed p + m) = 2p^\nu\,\bar u(p)$;
> 3. without spinors, $(\slashed p + m)\,\gamma^\nu\,(\slashed p + m) = 2p^\nu\,(\slashed p + m)$.
>
> The numerator of a propagator contains $\slashed p + m$, whereas the Dirac equation of $u(p)$ contains $\slashed p - m$. Anticommuting $\slashed p$ through $\gamma^\nu$ flips its sign and makes the Dirac equation applicable.
>
> *Model:* the free Dirac spinors; *applies:* on-shell $p$, any spin state, $m \ge 0$.
>
> *Source: PHY 513 Lecture 22, slide 7 ("$u(p)$ satisfies the Dirac equation $(\slashed p - m)u(p) = 0$ ⇒ $(\slashed p + m)\gamma^\nu u(p) = (-\gamma^\nu\slashed p + 2p^\nu + m\gamma^\nu)u(p) = 2p^\nu u(p)$", with $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ under the first equals sign), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, Derivation "Numerators: using the Dirac equation" · PS §5.5, p. 159 · Yu §8.6, eq. (8.323) · items 2 and 3 written out here (checked numerically)*

^lem-c8a-15-4

> [!derivation]- Derivation
> **Step 1** (anticommute). $\slashed p\gamma^\nu = p_\mu\gamma^\mu\gamma^\nu = p_\mu(2g^{\mu\nu} - \gamma^\nu\gamma^\mu) = 2p^\nu - \gamma^\nu\slashed p$ ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]], read from the other side).
>
> **Step 2** (item 1). $(\slashed p + m)\gamma^\nu u(p) = \bigl(2p^\nu - \gamma^\nu\slashed p + m\gamma^\nu\bigr)u(p) = 2p^\nu u(p) - \gamma^\nu(\slashed p - m)u(p)$. The last term vanishes by the Dirac equation $(\slashed p - m)u(p) = 0$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]]).
>
> **Step 3** (item 2). From Step 1, $\gamma^\nu\slashed p = 2p^\nu - \slashed p\gamma^\nu$. Then $\bar u(p)\gamma^\nu(\slashed p + m) = \bar u(p)\bigl(2p^\nu - \slashed p\gamma^\nu + m\gamma^\nu\bigr) = 2p^\nu\bar u(p) - \bar u(p)(\slashed p - m)\gamma^\nu$, and $\bar u(p)(\slashed p - m) = 0$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]]).
>
> **Step 4** (item 3). $(\slashed p + m)\gamma^\nu(\slashed p + m) = \bigl[2p^\nu - \gamma^\nu(\slashed p - m)\bigr](\slashed p + m) = 2p^\nu(\slashed p + m) - \gamma^\nu(\slashed p\slashed p - m^2)$, and $\slashed p\slashed p = p^2 = m^2$ ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]]). Items 1 and 2 follow from item 3 as well, since $\sum_su^s(p)\bar u^s(p) = \slashed p + m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]).
>
> **What the derivation shows.**
> - Only the part $\slashed p + m$ of the numerator simplifies. The photon momentum, $\slashed k$ or $\slashed k'$, stays: the amplitude becomes simpler, not simple.

^der-c8a-15-4

*Uses:* [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-2|Theorem §C5a.11.2]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]]

> [!theorem] Theorem §C8a.15.5: The Simplified Compton Amplitude
> $$
> i\mathcal M = -ie^2\,\epsilon^\ast_\mu(k')\,\epsilon_\nu(k)\;\bar u(p')\left[\frac{\gamma^\mu\slashed k\gamma^\nu + 2\gamma^\mu p^\nu}{2\,p\cdot k} + \frac{\gamma^\nu\slashed k'\gamma^\mu - 2\gamma^\nu p^\mu}{2\,p\cdot k'}\right]u(p) .
> $$
>
> 1. It equals the amplitude of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]] for every spin state and every pair of polarization vectors; the two brackets differ as matrices and agree when they act on $u(p)$.
> 2. The plus sign between the terms and the minus sign inside the second numerator come from the negative denominator $-2p\cdot k'$ ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]).
> 3. The second term is the first with $k \to -k'$ and $\mu \leftrightarrow \nu$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, on-shell external momenta, $m > 0$; the bracket may be used only next to $u(p)$ on its right.
>
> *Source: PHY 513 Lecture 22, slide 7 ("Simplified amplitude"; its typography: next caution), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, subsection "Simplifying" (the displayed result, "Checked numerically") · PS §5.5, eq. (5.74) · Yu §8.6, eq. (8.324) · item 3: the user's notes, subsection "Squaring" (filled in by the user's notes)*

^thm-c8a-15-5

> [!derivation]- Derivation
> **Step 1** (first numerator). Split $\slashed p + \slashed k + m = \slashed k + (\slashed p + m)$ and apply [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^lem-c8a-15-4|Lemma §C8a.15.4]], item 1:
>
> $$
> (\slashed p + \slashed k + m)\,\gamma^\nu u(p) = \slashed k\gamma^\nu u(p) + (\slashed p + m)\gamma^\nu u(p) = \bigl(\slashed k\gamma^\nu + 2p^\nu\bigr)u(p) .
> $$
>
> Multiplied by $\gamma^\mu$ from the left: $\bigl(\gamma^\mu\slashed k\gamma^\nu + 2\gamma^\mu p^\nu\bigr)u(p)$. The number $p^\nu$ commutes with everything; the matrix $\gamma^\mu$ stays.
>
> **Step 2** (second numerator). The same with the index $\mu$: $(\slashed p - \slashed k' + m)\gamma^\mu u(p) = \bigl(-\slashed k'\gamma^\mu + 2p^\mu\bigr)u(p)$, and with $\gamma^\nu$ from the left $\bigl(-\gamma^\nu\slashed k'\gamma^\mu + 2\gamma^\nu p^\mu\bigr)u(p)$.
>
> **Step 3** (denominators). By [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]] the first term is divided by $2p\cdot k$ and the second by $-2p\cdot k'$. The minus sign of the second denominator is moved into its numerator:
>
> $$
> \frac{-\gamma^\nu\slashed k'\gamma^\mu + 2\gamma^\nu p^\mu}{-2\,p\cdot k'} = \frac{\gamma^\nu\slashed k'\gamma^\mu - 2\gamma^\nu p^\mu}{2\,p\cdot k'} .
> $$
>
> **Step 4** (item 3). In the first term replace $k \to -k'$ and exchange $\mu \leftrightarrow \nu$: the numerator becomes $-\gamma^\nu\slashed k'\gamma^\mu + 2\gamma^\nu p^\mu$ and the denominator $-2p\cdot k'$, which is the second term. The polarization vectors go along: $\epsilon_\nu(k) \leftrightarrow \epsilon^\ast_\mu(k')$.
>
> **What the derivation shows.**
> - ⚑ By-product: the two diagrams are exchanged by $k \leftrightarrow -k'$ (with the photon indices), so the square must be symmetric under this exchange → [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|Theorem §C8a.15.8]], 3. Only two of the four terms of the square need to be computed.
> - The $\slashed k$ and $\slashed k'$ remain: each term of the square still contains eight $\gamma$'s → [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]].

^der-c8a-15-5

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^lem-c8a-15-4|Lemma §C8a.15.4]]

> [!caution] Caution: Reading the fraction on slide 7
> Slides 7 and 18 typeset the bracket as $\gamma^\mu\,\frac{\slashed k\gamma^\nu + 2p^\nu}{2p\cdot k} + \gamma^\nu\,\frac{\slashed k'\gamma^\mu - 2p^\mu}{2p\cdot k'}$, with the first $\gamma$ of each term standing in front of the fraction. It multiplies the whole numerator, so the slide agrees with [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]]: the terms with $2p$ keep their matrix, $2\gamma^\mu p^\nu$ and $2\gamma^\nu p^\mu$. Read as $\gamma^\mu\slashed k\gamma^\nu + 2p^\nu$, with a bare $2p^\nu$, the second piece would have lost its matrix and its index $\mu$, and the expression would not equal the amplitude.
>
> *Source: PHY 513 Lecture 22, slides 7 and 18 (page images) · the user's PHY 513 notes, Lecture 22 update, Caution "Slips in the slides", first item, which reads the slide in the second way; the comparison with the slide image was made here (the form with bare $2p$ terms was checked numerically to differ from the amplitude)*

^cau-c8a-15-1

## The square

> [!definition] Definition §C8a.15.1: Average over Spins and Polarizations
> For $\gamma e^- \to \gamma e^-$ the **spin- and polarization-averaged** squared amplitude is the sum over the final electron spin and the final photon polarization and the average over the initial ones:
>
> $$
> \frac14\sum_{\rm spins,\,pols}|\mathcal M|^2 \equiv \frac12\sum_{e\ \rm spins}\;\frac12\sum_{\gamma\ \rm pols}|\mathcal M|^2 .
> $$
>
> 1. Each of the two initial particles has two states: the electron two spin states, the photon two physical polarizations ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]]). Hence the same factor $\frac14$ as for two electrons, although the two initial particles are of different kinds.
> 2. The sums over the photon polarizations run over the two physical polarizations only. In the computation they are carried out with the replacement $\sum_{\rm pol}\epsilon^\ast_\mu(k)\,\epsilon_\nu(k) \to -g_{\mu\nu}$, written with an arrow: the two sides are not equal as tensors, and they give the same result once contracted with the amplitude. The reason is the Ward identity ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]]).
>
> *Equivalently,* this is $\overline{|\mathcal M|^2}$ of [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]] with one spin-$\frac12$ particle and one photon in the initial state, the twin of [[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1|Def. §C8a.7.1]].
>
> *Model:* as in [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]; *applies:* unpolarized beams, detectors blind to spin and polarization.
>
> *Source: PHY 513 Lecture 22, slide 8 ("Average over initial and sum over final e-spin/γ-polarization. Eliminates wavefunctions $u(p)$ (electron) and $\epsilon^\mu$ (photon)"), slide 9 ("$\sum_{\rm pol.}\epsilon^\ast_\mu(k)\epsilon_\nu(k) \to -g_{\mu\nu}$. Note: '→' rather than '='. '=' would be true for a complete set of four polarization vectors. The $\sum_{\rm pol.}$ is over two physical polarizations only. '→' means 2 and 4 polarizations are equivalent because the two 'unphysical' polarizations cancel in physical amplitudes"), slide 10 ("$\frac12\sum_{e\ \rm spin}\frac12\sum_{\gamma\ \rm pol}|\mathcal M|^2 = \frac14\sum_{\rm spin, pol}|\mathcal M|^2$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, subsection "Squaring" · PS §5.5, eq. (5.75)*

^def-c8a-15-1

> [!remark] Remark: Why the arrow needs an explanation for external photons
> With an equals sign the relation would hold for a complete set of four polarization vectors with their weights ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-4|Theorem §C8a.3.4]]). For the virtual photon of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon|§C8a.6]] all four belong in the propagator ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|Theorem §C8a.3.5]]). A photon in the initial or the final state is a real photon with two polarizations, and those are what one must sum over; pretending that there are four is the step that has to be justified. [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations|§C8a.16]] does it.
>
> *Source: PHY 513 Lecture 22, slide 9, and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, subsection "Squaring"*

^rem-c8a-15-2

> [!theorem] Theorem §C8a.15.6: The Square Is One Trace of Eight γ's for Each Term
> With $\Gamma^{\mu\nu}$ of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]] and $\bar\Gamma^{\mu\nu} \equiv \gamma^0(\Gamma^{\mu\nu})^\dagger\gamma^0$:
> 1. for fixed polarization vectors, the sum over the two electron spins is one trace,
>
> $$
> \sum_{e\ \rm spins}|\mathcal M|^2 = e^4\,\epsilon^\ast_\mu(k')\epsilon_\nu(k)\,\epsilon_\rho(k')\epsilon^\ast_\sigma(k)\;\operatorname{tr}\bigl[(\slashed p' + m)\,\Gamma^{\mu\nu}\,(\slashed p + m)\,\bar\Gamma^{\rho\sigma}\bigr] ;
> $$
>
> 2. with the replacement of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^def-c8a-15-1|Def. §C8a.15.1]], item 2, for each photon,
>
> $$
> \frac14\sum_{\rm spins,\,pols}|\mathcal M|^2 = \frac{e^4}{4}\,\operatorname{tr}\bigl[(\slashed p' + m)\,\Gamma^{\mu\nu}\,(\slashed p + m)\,\bar\Gamma_{\mu\nu}\bigr] ;
> $$
>
> 3. the conjugate matrix has its factors in reversed order, $\bar\Gamma^{\mu\nu} = \dfrac{\gamma^\nu(\slashed p + \slashed k + m)\gamma^\mu}{2\,p\cdot k} + \dfrac{\gamma^\mu(\slashed p - \slashed k' + m)\gamma^\nu}{-2\,p\cdot k'}$;
> 4. two diagrams give four terms, and each term is a single trace of eight $\gamma$'s (counting slashed momenta). In $e^-e^+ \to \mu^-\mu^+$ each fermion line closed on itself at one vertex and the square was a product of two traces of four $\gamma$'s ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-4|Theorem §C8a.7.4]]). Here the internal line is a fermion, the one fermion line runs through both vertices, and nothing factorizes.
>
> *Equivalently,* with the simplified numerators of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]] in both $\Gamma$ and $\bar\Gamma$ the trace is that of PS (5.81); the method is unchanged, only longer.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, unpolarized, on-shell external momenta, any frame; item 2 uses [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]] for both photons.
>
> *Source: PHY 513 Lecture 22, slide 8 ("Square amplitude: two diagrams ⇒ four terms. … Evaluate traces over gamma-matrices. Completeness for spinors: $\sum_su^s(p)\bar u^s(p) = \slashed p + m$"), slide 10 ("= 4 terms (from squaring 2 terms), each with traces of 8 γ's. Contrast: $e^-e^+ \to \mu^-\mu^+$ factorizes to two traces over 4 γ's. Upshot: hard work to compute traces"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, paragraph "One trace of eight" · PS §5.5, eq. (5.81) · Yu §8.6.2, eqs. (8.348)–(8.349) and the display after them*

^thm-c8a-15-6

> [!derivation]- Derivation
> **Step 1** (the conjugate). For fixed polarizations $\mathcal M = -e^2\,\bar u(p')\,\Gamma\,u(p)$ with the matrix $\Gamma \equiv \epsilon^\ast_\mu(k')\epsilon_\nu(k)\Gamma^{\mu\nu}$. By [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], part 1, $\bigl(\bar u(p')\Gamma u(p)\bigr)^\ast = \bar u(p)\,\bar\Gamma\,u(p')$ with $\bar\Gamma = \gamma^0\Gamma^\dagger\gamma^0 = \epsilon_\rho(k')\epsilon^\ast_\sigma(k)\,\bar\Gamma^{\rho\sigma}$: the polarization vectors are complex conjugated, and the summed indices are renamed $\rho$, $\sigma$ because they are contracted inside $\mathcal M^\ast$.
>
> **Step 2** (item 3). The bar reverses a product of $\gamma$ matrices and leaves each $\gamma^\mu$ unchanged ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], part 1); the momenta and denominators are real. So $\overline{\gamma^\mu(\slashed p + \slashed k + m)\gamma^\nu} = \gamma^\nu(\slashed p + \slashed k + m)\gamma^\mu$, and the same for the second term.
>
> **Step 3** (the spin sum). [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], part 2, with $w_1 = u(p')$, $w_2 = u(p)$, $\Pi_1 = \slashed p' + m$, $\Pi_2 = \slashed p + m$: $\sum_{s, s'}|\bar u(p')\Gamma u(p)|^2 = \operatorname{tr}\bigl[\Gamma(\slashed p + m)\bar\Gamma(\slashed p' + m)\bigr] = \operatorname{tr}\bigl[(\slashed p' + m)\Gamma(\slashed p + m)\bar\Gamma\bigr]$ by cyclicity. With $|-e^2|^2 = e^4$ this is item 1. No electron wave function is left.
>
> **Step 4** (the polarization sums). The outgoing photon appears as $\epsilon^\ast_\mu(k')\epsilon_\rho(k')$ and the incoming one as $\epsilon_\nu(k)\epsilon^\ast_\sigma(k)$. Summed over the physical polarizations, each pair is replaced by minus the metric, $-g_{\mu\rho}$ and $-g_{\nu\sigma}$ ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]], one photon at a time). The two minus signs cancel, and $g_{\mu\rho}g_{\nu\sigma}\bar\Gamma^{\rho\sigma} = \bar\Gamma_{\mu\nu}$. No photon wave function is left.
>
> **Step 5** (the average). The factor $\frac14$ of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^def-c8a-15-1|Def. §C8a.15.1]].
>
> **Step 6** (counting). Each of $\Gamma$ and $\bar\Gamma$ is a sum of two terms: four products. In the leading part of each, $\slashed p'\cdot\gamma^\mu(\slashed p + \slashed k)\gamma^\nu\cdot\slashed p\cdot\gamma_\nu(\slashed p + \slashed k)\gamma_\mu$, there are $1 + 3 + 1 + 3 = 8$ matrices.
>
> **What the derivation shows.**
> - The procedure is that of [[§C8a.7 The Spin-Averaged Squared Amplitude|§C8a.7]] step for step ([[P8 Unpolarized Cross Section from Diagrams#^p8-3|P8, step 3]]): square, replace the wave functions by completeness relations, take traces.
> - ⚑ By-product: for external photons the completeness relation is replaced by a statement that holds only inside amplitudes → [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]].

^der-c8a-15-6

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^def-c8a-15-1|Def. §C8a.15.1]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-3|P8, step 3]]

> [!theorem] Theorem §C8a.15.7: The Spin- and Polarization-Averaged Squared Amplitude of Compton Scattering
> $$
> \frac14\sum_{\rm spins,\,pols}|\mathcal M|^2 = 2e^4\left[\frac{p\cdot k'}{p\cdot k} + \frac{p\cdot k}{p\cdot k'} + 2m^2\Bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\Bigr) + m^4\Bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\Bigr)^2\right] .
> $$
>
> It is the sum of four traces, $\frac14\sum|\mathcal M|^2 = \dfrac{e^4}{4}\left[\dfrac{\mathbf I}{(2p\cdot k)^2} + \dfrac{\mathbf{II} + \mathbf{III}}{(2p\cdot k)(2p\cdot k')} + \dfrac{\mathbf{IV}}{(2p\cdot k')^2}\right]$, with
> 1. $\mathbf I = 32\bigl[(p\cdot k)(p\cdot k') + m^2\,p\cdot k + m^4\bigr]$, the square of diagram (a);
> 2. $\mathbf{IV} = 32\bigl[(p\cdot k)(p\cdot k') - m^2\,p\cdot k' + m^4\bigr]$, the square of diagram (b): $\mathbf I$ with $k \to -k'$;
> 3. $\mathbf{II} = \mathbf{III} = -16\bigl[2m^4 + m^2(p\cdot k - p\cdot k')\bigr]$, the interference of the two diagrams. It vanishes for $m = 0$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, unpolarized electrons and photons, on-shell external momenta, $m > 0$, any frame.
>
> *Source: PHY 513 Lecture 22, slide 10 ("Result: $2e^4\bigl[\frac{p\cdot k'}{p\cdot k} + \frac{p\cdot k}{p\cdot k'} + 2m^2\bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\bigr) + m^4\bigl(\frac{1}{p\cdot k} - \frac{1}{p\cdot k'}\bigr)^2\bigr]$"; the lecture quotes the result and refers to the textbook for the four traces), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.1, Principle "Spin-averaged Compton scattering" ("Checked numerically by summing explicit spinors and the two physical polarizations of each photon") · PS §5.5, eqs. (5.81), (5.82) and (5.87) · Yu §8.6.2, eqs. (8.380)–(8.383) · the evaluation below is written out here along PS pp. 161–162, with the traces expressed in $p\cdot k$ and $p\cdot k'$ (each step checked numerically)*

^thm-c8a-15-7

> [!derivation]- Derivation (the four traces)
> Abbreviations: $a \equiv p\cdot k$, $b \equiv p\cdot k'$.
>
> **Step 1** (what is squared). By [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]], $\mathcal M = -e^2\epsilon^\ast_\mu(k')\epsilon_\nu(k)\,\bar u(p')\bigl[\frac{A^{\mu\nu}}{2a} + \frac{B^{\mu\nu}}{2b}\bigr]u(p)$ with the numerators
>
> $$
> A^{\mu\nu} \equiv \gamma^\mu\slashed k\gamma^\nu + 2\gamma^\mu p^\nu , \qquad B^{\mu\nu} \equiv \gamma^\nu\slashed k'\gamma^\mu - 2\gamma^\nu p^\mu .
> $$
>
> In $\mathcal M^\ast = -e^2\epsilon_\mu(k')\epsilon^\ast_\nu(k)\,\bar u(p)\bigl[\cdots\bigr]u(p')$ the row $\bar u(p)$ stands on the left of the reversed numerators, and [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^lem-c8a-15-4|Lemma §C8a.15.4]], item 2, simplifies them in the same way. The barred numerators, with lower indices, are
>
> $$
> \bar A_{\mu\nu} = \gamma_\nu\slashed k\gamma_\mu + 2\gamma_\mu p_\nu , \qquad \bar B_{\mu\nu} = \gamma_\mu\slashed k'\gamma_\nu - 2\gamma_\nu p_\mu .
> $$
>
> **Step 2** (four traces). The spin and polarization sums of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]], with these numerators, give
>
> $$
> \frac14\sum|\mathcal M|^2 = \frac{e^4}{4}\left[\frac{\mathbf I}{(2a)^2} + \frac{\mathbf{II}}{(2a)(2b)} + \frac{\mathbf{III}}{(2b)(2a)} + \frac{\mathbf{IV}}{(2b)^2}\right] ,
> $$
>
> $$
> \mathbf I = \operatorname{tr}\bigl[(\slashed p' + m)A^{\mu\nu}(\slashed p + m)\bar A_{\mu\nu}\bigr] , \quad \mathbf{II} = \operatorname{tr}\bigl[(\slashed p' + m)A^{\mu\nu}(\slashed p + m)\bar B_{\mu\nu}\bigr] , \quad \mathbf{III} = \operatorname{tr}\bigl[(\slashed p' + m)B^{\mu\nu}(\slashed p + m)\bar A_{\mu\nu}\bigr] , \quad \mathbf{IV} = \operatorname{tr}\bigl[(\slashed p' + m)B^{\mu\nu}(\slashed p + m)\bar B_{\mu\nu}\bigr]
> $$
>
> (PS (5.81)).
>
> **Step 3** (scalar products). From $p' = p + k - k'$ with $p^2 = p'^2 = m^2$, $k^2 = k'^2 = 0$: squaring gives $m^2 = m^2 + 2a - 2b - 2k\cdot k'$, so $k\cdot k' = a - b$. Then
>
> $$
> p'\cdot k = p\cdot k - k'\cdot k = b , \qquad p'\cdot k' = p\cdot k' + k\cdot k' = a , \qquad p\cdot p' = m^2 + a - b .
> $$
>
> **Step 4** (tools). The contraction identities $\gamma^\nu\gamma_\nu = 4$, $\gamma^\nu\slashed q\gamma_\nu = -2\slashed q$, $\gamma^\nu\slashed q\slashed r\gamma_\nu = 4\,q\cdot r$, $\gamma^\nu\slashed q\slashed r\slashed s\gamma_\nu = -2\slashed s\slashed r\slashed q$ ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-2|Theorem §C5a.13.2]]), in particular $\gamma^\nu(\slashed p + m)\gamma_\nu = -2\slashed p + 4m$. From the slash algebra ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]]): $\slashed k\slashed k = 0$, $\slashed p\slashed p = m^2$, hence
>
> $$
> \slashed k\slashed p\slashed k = \slashed k(2a - \slashed k\slashed p) = 2a\,\slashed k , \qquad \slashed p\slashed k\slashed p = \slashed p(2a - \slashed p\slashed k) = 2a\,\slashed p - m^2\slashed k , \qquad \slashed p(\slashed p + m) = (\slashed p + m)\slashed p = m(\slashed p + m) ,
> $$
>
> and the same with $k'$, $b$. The traces: $\operatorname{tr}\mathbb 1 = 4$, $\operatorname{tr}(\slashed q\slashed r) = 4\,q\cdot r$, and a trace of an odd number of $\gamma$'s vanishes ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-3|Theorem §C5a.13.3]]).
>
> **Step 5** ($\mathbf I$: contract the inner indices first). The product $A^{\mu\nu}(\slashed p + m)\bar A_{\mu\nu}$ has four terms. In each, the index $\nu$ is contracted across $(\slashed p + m)$ and the index $\mu$ across everything:
>
> $$
> \begin{aligned}
> T_1 &= \gamma^\mu\slashed k\,\gamma^\nu(\slashed p + m)\gamma_\nu\,\slashed k\gamma_\mu = \gamma^\mu\slashed k(-2\slashed p + 4m)\slashed k\gamma_\mu = \gamma^\mu(-4a\,\slashed k)\gamma_\mu = 8a\,\slashed k , \\
> T_2 &= \gamma^\mu\slashed k\gamma^\nu(\slashed p + m)\,2\gamma_\mu p_\nu = 2\gamma^\mu\slashed k\,\slashed p(\slashed p + m)\gamma_\mu = 2m\,\gamma^\mu\slashed k(\slashed p + m)\gamma_\mu = 2m\,(4a - 2m\slashed k) = 8ma - 4m^2\slashed k , \\
> T_3 &= 2\gamma^\mu p^\nu(\slashed p + m)\gamma_\nu\slashed k\gamma_\mu = 2\gamma^\mu(\slashed p + m)\slashed p\,\slashed k\gamma_\mu = 2m\,\gamma^\mu(\slashed p + m)\slashed k\gamma_\mu = 8ma - 4m^2\slashed k , \\
> T_4 &= 2\gamma^\mu p^\nu(\slashed p + m)\,2\gamma_\mu p_\nu = 4m^2\,\gamma^\mu(\slashed p + m)\gamma_\mu = -8m^2\slashed p + 16m^3 .
> \end{aligned}
> $$
>
> In $T_1$: $\slashed k\slashed p\slashed k = 2a\slashed k$ and $\slashed k\slashed k = 0$ kill the $4m$ term; then $\gamma^\mu\slashed k\gamma_\mu = -2\slashed k$. In $T_2$, $T_3$: $\gamma^\nu p_\nu = \slashed p$, then $\slashed p(\slashed p + m) = m(\slashed p + m)$, then the two- and one-$\gamma$ contractions. In $T_4$: $p^\nu p_\nu = m^2$. The sum:
>
> $$
> T_1 + T_2 + T_3 + T_4 = 8(a - m^2)\,\slashed k - 8m^2\slashed p + 16m\,(a + m^2) .
> $$
>
> **Step 6** ($\mathbf I$: the trace). Multiply by $(\slashed p' + m)$ and take the trace; odd products drop out, so $\slashed p'$ pairs with the slashed terms and $m$ with the term without a slash:
>
> $$
> \mathbf I = 4\bigl[8(a - m^2)\,p'\cdot k - 8m^2\,p\cdot p'\bigr] + 4m\cdot16m\,(a + m^2) = 32(a - m^2)\,p'\cdot k - 32m^2\,p\cdot p' + 64m^2(a + m^2) .
> $$
>
> This is PS (5.82), $\mathbf I = 16\bigl(4m^4 - 2m^2p\cdot p' + 4m^2p\cdot k - 2m^2p'\cdot k + 2(p\cdot k)(p'\cdot k)\bigr)$. With Step 3:
>
> $$
> \mathbf I = 32(a - m^2)b - 32m^2(m^2 + a - b) + 64m^2a + 64m^4 = 32\bigl(ab + m^2a + m^4\bigr) .
> $$
>
> **Step 7** ($\mathbf{IV}$ from $\mathbf I$). $B^{\mu\nu}$ is $-A^{\nu\mu}$ with $k \to -k'$ ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]], 3), and so is $\bar B$ relative to $\bar A$. $\mathbf{IV}$ contains two such factors, the signs cancel, the summed indices may be renamed, and $p' = p + k - k'$ is unchanged by $k \leftrightarrow -k'$. So $\mathbf{IV}$ is $\mathbf I$ with $a = p\cdot k \to -p\cdot k' = -b$ and $b \to -a$:
>
> $$
> \mathbf{IV} = 32\bigl(ab - m^2b + m^4\bigr) .
> $$
>
> **Step 8** ($\mathbf{II}$: the four products). In $A^{\mu\nu}(\slashed p + m)\bar B_{\mu\nu}$ the indices are not nested:
>
> $$
> \begin{aligned}
> U_1 &= \gamma^\mu\slashed k\,\gamma^\nu(\slashed p + m)\gamma_\mu\slashed k'\gamma_\nu = \gamma^\mu\slashed k\bigl(-2\slashed k'\gamma_\mu\slashed p + 4m\,k'_\mu\bigr) = -2\,(4\,k\cdot k')\,\slashed p + 4m\,\slashed k'\slashed k = -8(k\cdot k')\,\slashed p + 4m\,\slashed k'\slashed k , \\
> U_2 &= \gamma^\mu\slashed k\gamma^\nu(\slashed p + m)(-2\gamma_\nu p_\mu) = -2\slashed p\slashed k(-2\slashed p + 4m) = 4\slashed p\slashed k\slashed p - 8m\,\slashed p\slashed k = 8a\,\slashed p - 4m^2\slashed k - 8m\,\slashed p\slashed k , \\
> U_3 &= 2\gamma^\mu p^\nu(\slashed p + m)\gamma_\mu\slashed k'\gamma_\nu = 2(-2\slashed p + 4m)\slashed k'\slashed p = -4\slashed p\slashed k'\slashed p + 8m\,\slashed k'\slashed p = -8b\,\slashed p + 4m^2\slashed k' + 8m\,\slashed k'\slashed p , \\
> U_4 &= 2\gamma^\mu p^\nu(\slashed p + m)(-2\gamma_\nu p_\mu) = -4\slashed p(\slashed p + m)\slashed p = -4m\,(\slashed p + m)\slashed p = -4m^2(\slashed p + m) .
> \end{aligned}
> $$
>
> In $U_1$ the contraction over $\nu$ runs across three matrices for the $\slashed p$ part, $\gamma^\nu\slashed p\gamma_\mu\slashed k'\gamma_\nu = -2\slashed k'\gamma_\mu\slashed p$, and across two for the $m$ part, $\gamma^\nu\gamma_\mu\slashed k'\gamma_\nu = 4k'_\mu$; then $\gamma^\mu\slashed k\slashed k'\gamma_\mu = 4k\cdot k'$ and $\gamma^\mu k'_\mu = \slashed k'$, which stands to the left of $\slashed k$. In $U_2$: $\gamma^\mu p_\mu = \slashed p$ in front, and $\gamma^\nu(\slashed p + m)\gamma_\nu = -2\slashed p + 4m$. In $U_3$: $\gamma^\mu(\slashed p + m)\gamma_\mu = -2\slashed p + 4m$ and $\gamma_\nu p^\nu = \slashed p$ at the end.
>
> **Step 9** ($\mathbf{II}$: the traces). With $(\slashed p' + m)$ in front:
>
> $$
> \begin{aligned}
> \operatorname{tr}\bigl[(\slashed p' + m)U_1\bigr] &= -32(k\cdot k')(p\cdot p') + 16m^2\,k\cdot k' , \\
> \operatorname{tr}\bigl[(\slashed p' + m)U_2\bigr] &= 32a\,(p\cdot p') - 16m^2\,p'\cdot k - 32m^2a , \\
> \operatorname{tr}\bigl[(\slashed p' + m)U_3\bigr] &= -32b\,(p\cdot p') + 16m^2\,p'\cdot k' + 32m^2b , \\
> \operatorname{tr}\bigl[(\slashed p' + m)U_4\bigr] &= -16m^2\,p\cdot p' - 16m^4 .
> \end{aligned}
> $$
>
> Insert Step 3. The terms with $(p\cdot p')$ times $a - b$ cancel: $-32(a - b)(p\cdot p') + 32a(p\cdot p') - 32b(p\cdot p') = 0$. The rest:
>
> $$
> \mathbf{II} = 16m^2(a - b) - 16m^2b - 32m^2a + 16m^2a + 32m^2b - 16m^2(m^2 + a - b) - 16m^4 = -16\bigl[2m^4 + m^2(a - b)\bigr] .
> $$
>
> **Step 10** ($\mathbf{III} = \mathbf{II}$). $\mathbf{II}$ and $\mathbf{III}$ are the two cross terms of the square, $\mathcal M_{(a)}\mathcal M_{(b)}^\ast$ and $\mathcal M_{(b)}\mathcal M_{(a)}^\ast$ summed over spins and polarizations: they are complex conjugates of each other. $\mathbf{II}$ is real, so $\mathbf{III} = \mathbf{II}$.
>
> **Step 11** (assemble).
>
> $$
> \begin{aligned}
> \frac{\mathbf I}{4a^2} + \frac{2\,\mathbf{II}}{4ab} + \frac{\mathbf{IV}}{4b^2} &= 8\Bigl[\frac ba + \frac{m^2}{a} + \frac{m^4}{a^2}\Bigr] - 8\Bigl[\frac{2m^4}{ab} + \frac{m^2}{b} - \frac{m^2}{a}\Bigr] + 8\Bigl[\frac ab - \frac{m^2}{b} + \frac{m^4}{b^2}\Bigr] \\
> &= 8\Bigl[\frac ba + \frac ab + 2m^2\Bigl(\frac1a - \frac1b\Bigr) + m^4\Bigl(\frac1a - \frac1b\Bigr)^2\Bigr] ,
> \end{aligned}
> $$
>
> using $\frac{1}{a^2} - \frac{2}{ab} + \frac{1}{b^2} = \bigl(\frac1a - \frac1b\bigr)^2$. Multiplied by $\frac{e^4}{4}$: the statement.
>
> **What the derivation shows.**
> - ⚑ By-product: the interference term $\mathbf{II} + \mathbf{III}$ is proportional to $m^2$. For $m = 0$ the two diagrams do not interfere in the unpolarized sum, and $\frac14\sum|\mathcal M|^2 = 2e^4\bigl[\frac ba + \frac ab\bigr]$ is the sum of the squares of (a) and (b): the term $\frac ba$ comes from diagram (a) and $\frac ab$ from diagram (b) → [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]].
> - ⚑ By-product: $p'$ never needed its own scalar products; momentum conservation reduced everything to $a$ and $b$ (Step 3) → [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-8|Theorem §C8a.15.8]].
> - Contracting the index pair that lies innermost first keeps every intermediate expression at three matrices or fewer; PS expands the sixteen terms of each trace instead.

^der-c8a-15-7

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^lem-c8a-15-4|Lemma §C8a.15.4]], [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-1|Theorem §C5a.13.1]], [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-2|Theorem §C5a.13.2]], [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-3|Theorem §C5a.13.3]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-4|P8, step 4]]

> [!theorem] Theorem §C8a.15.8: The Result Depends on Two Invariants
> 1. **Which invariants.** Of the four momenta, $p'$ is eliminated by momentum conservation. From $p$, $k$, $k'$ one can form $p\cdot k$, $p\cdot k'$ and $k\cdot k'$ (the squares are $m^2$, $0$, $0$), and
>
> $$
> k\cdot k' = p\cdot k - p\cdot k' ,
> $$
>
> so only $p\cdot k$ and $p\cdot k'$ are independent: the two that sit in the denominators of the propagators ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]).
> 2. **Dimensions.** $|\mathcal M|^2$ is dimensionless for a $2 \to 2$ process. So it can contain only ratios of the invariants, or $m^2$ and $m^4$ divided by one and two powers of them: the three kinds of terms of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]].
> 3. **Symmetry.** The result is unchanged under $p\cdot k \leftrightarrow -p\cdot k'$, the exchange $k \leftrightarrow -k'$ of the two diagrams ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]], 3).
>
> *Model:* kinematics; *applies:* $2 \to 2$ with $p^2 = p'^2 = m^2$, $k^2 = k'^2 = 0$.
>
> *Source: PHY 513 Lecture 22, transcript (the question why $k\cdot k'$ does not appear, answered in Part C by squaring momentum conservation; the dimensional argument) · the user's PHY 513 notes, Lecture 22 update, §22.1, paragraph "Which invariants?" (the relation and the symmetry filled in by the user's notes) · PS §5.5, p. 162 ($p^2 + 2p\cdot(k - k') - 2k\cdot k'$)*

^thm-c8a-15-8

> [!derivation]- Derivation
> **Step 1** (item 1). Square $p' = p + k - k'$: $p'^2 = p^2 + k^2 + k'^2 + 2p\cdot k - 2p\cdot k' - 2k\cdot k'$. With $p'^2 = p^2 = m^2$ and $k^2 = k'^2 = 0$ only the three cross terms remain: $0 = p\cdot k - p\cdot k' - k\cdot k'$.
>
> **Step 2** (item 2). $\mathcal M$ is dimensionless for a $2 \to 2$ process ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]; [[§C6b.4 Two-Body Scattering Kinematics#^rem-c6b-4-3|§C6b.4, Remark: Why 1/E²: dimensional analysis]]), and $e$ is dimensionless ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|Theorem §C8a.1.3]], 3). $p\cdot k$, $p\cdot k'$ and $m^2$ have mass dimension 2.
>
> **Step 3** (item 3). Under $p\cdot k \to -p\cdot k'$, $p\cdot k' \to -p\cdot k$: the two ratios are exchanged; $\frac{1}{p\cdot k} - \frac{1}{p\cdot k'} \to -\frac{1}{p\cdot k'} + \frac{1}{p\cdot k}$, unchanged.
>
> **What the derivation shows.**
> - The relation of Step 1 is, in the rest frame of the electron, the Compton formula → [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-1|Theorem §C8a.17.1]].

^der-c8a-15-8

*Uses:* [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-3|Theorem §C8a.15.3]]

> [!remark]- Connections
> - The external-photon rule used here for the first time, $\epsilon_\mu$ in and $\epsilon^\ast_\mu$ out, was derived with the photon field of Lecture 18 — [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]]; the proof of the photon rules from the quantized field is deferred to Lecture 25 ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]]).
> - The internal fermion line is the Dirac propagator between two vertices, first met in Yukawa theory — [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]; there the two-boson process with the same two diagrams is [[§C6d.5 Second Order#^ex-c6d-5-3|Example §C6d.5.3]].
> - The trick $(\slashed p + m)\gamma^\nu u(p) = 2p^\nu u(p)$ is the Dirac equation used across one $\gamma$ matrix; the Gordon identity uses it on both sides of a vertex — [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-9|Theorem §C5a.13.9]].
> - The replacement of the photon polarization sum by $-g_{\mu\nu}$, and the Ward identity behind it — [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]], [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]].
> - From $\frac14\sum|\mathcal M|^2$ to the cross sections: the lab frame (Klein–Nishina, Thomson) and the centre-of-mass frame at high energy — [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-4|Theorem §C8a.17.4]], [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy#^thm-c8a-17-7|Theorem §C8a.17.7]].
> - Why the term $p\cdot k/p\cdot k'$ is less singular than the square of the propagator suggests — [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]].
> - The general recipe that this section follows, and its helicity counterpart — [[P8 Unpolarized Cross Section from Diagrams|P8]], [[P9 Helicity Amplitudes|P9]].
