---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8a
section: C8a.16
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square|§C8a.15]] · ↑ [[· C8a Quantum Electrodynamics]] · [[§C8a.17 Compton Scattering꞉ the Compton Formula, Klein–Nishina and High Energy|§C8a.17]] →

*Sources: PHY 513 Lecture 22 (Larsen, 23 Nov 2026, "Compton Scattering"), slides 3, 9, 12–18 (Part B), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2 "The Ward identity" (Derivation "Current conservation implies $k_\mu\mathcal M^\mu = 0$", Principle "The Ward identity and the polarization sum", paragraphs "Interpretation", "Gauge invariance", "The quantum fine print", "Compton scattering as an example", "Asked in the lecture: what about higher-order diagrams?"), Caution "Slips in the slides", PART 2 (d), (g), paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.5, pp. 159–161, eqs. (5.75)–(5.80) (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.6.1, eqs. (8.325)–(8.337) (page images of the current build checked).*

Does one sum over two photon polarizations or over four? A photon in the initial or the final state has two physical polarizations ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]]), and those are what an unpolarized cross section sums over. But the only Lorentz-invariant object that can replace a sum $\sum\epsilon^\ast_\mu\epsilon_\nu$ is the metric, which is what a complete set of four polarizations gives ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-4|Theorem §C8a.3.4]]). Lorentz invariance asks for all four, common sense for two. This section shows that both can be had: in any QED amplitude the contributions of the two unphysical polarizations cancel each other, because the photon couples to a conserved current. The statement behind the cancellation is the Ward identity ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]]); its consequence is the replacement $\sum\epsilon^\ast_\mu\epsilon_\nu \to -g_{\mu\nu}$ for external photons ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]]), used in [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]].

**The mathematical picture.** An amplitude with one external photon singled out is a linear functional of that photon's polarization vector, $\epsilon \mapsto \mathcal M^\mu\epsilon^\ast_\mu$: it is given by a four-component object $\mathcal M^\mu(k)$ ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]]). The Ward identity says that this functional vanishes on the momentum $k$ itself. It therefore depends only on the class of $\epsilon$ modulo multiples of $k$, which is exactly the freedom that a polarization vector of a massless particle has under Lorentz transformations ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]]) and under gauge transformations ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-3|Theorem §C8a.3.3]], 4).

**Setup.** [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]], in which the photon field enters the interaction only through $e\,j^\mu A_\mu$ with the conserved current $j^\mu = \bar\psi\gamma^\mu\psi$ ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|Theorem §C8a.1.3]]). The statements are about any process with at least one external photon, of momentum $k$ with $k^2 = 0$, all other external particles on shell. The derivation of the Ward identity is the one given in the lecture; what it leaves open is collected in [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^rem-c8a-16-1|§C8a.16, Remark: The quantum fine print]].

*Conventions* ([[Larsen PHY 513]]): for a photon moving along $\hat{\mathbf z}$, $k^\mu = (\kappa, 0, 0, \kappa)$ with $\kappa > 0$ its energy, and $k_\mu = (\kappa, 0, 0, -\kappa)$; the slides write $k^\mu = (k, 0, 0, k)$, with the same letter for the four-vector and for the number. $\mathcal M^0, \dots, \mathcal M^3$ are the components of $\mathcal M^\mu$ with upper index. $j^\mu$ is the number current; the electric current is $J^\mu = e\,j^\mu$ ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|Theorem §C8a.1.3]]).

## The amplitude with one polarization stripped off

> [!definition] Definition §C8a.16.1: The Amplitude with One Photon's Polarization Stripped Off
> Any amplitude with an outgoing photon of momentum $k$ and polarization $\epsilon$ has the form
>
> $$
> i\mathcal M(k) = i\mathcal M^\mu(k)\,\epsilon^\ast_\mu(k) .
> $$
>
> $\mathcal M^\mu(k)$ is **the amplitude with the polarization vector of that photon stripped off**: whatever the rest of the diagrams gives, with one loose Lorentz index. For an incoming photon the same is written with $\epsilon_\mu(k)$ in place of $\epsilon^\ast_\mu(k)$.
> 1. Only the momentum of the one photon is displayed. Everything else is suppressed: the momenta and spins of the other particles, and other external photons, with their polarization vectors or with their indices left open.
> 2. The form holds because the external photon enters a diagram only through its wave function at one vertex ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]]), which contracts the index of that vertex ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]], 2).
> 3. It is not special to one process. For Compton scattering, stripping both photons gives $\mathcal M = \epsilon^\ast_\mu(k')\,\epsilon_\nu(k)\,\mathcal M^{\mu\nu}$ with $\mathcal M^{\mu\nu} = -e^2\,\bar u(p')\Gamma^{\mu\nu}u(p)$ ([[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]]).
>
> *Equivalently,* this is the $\mathcal M^\mu(k)$ of [[§C4.11 Vector-Field Propagators#^thm-c4-11-10|Theorem §C4.11.10]], PS (5.76) and Yu (8.326) (who writes $M^\mu(p)$).
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* any process with an external photon, at any order; the sum of all diagrams of that order.
>
> *Source: PHY 513 Lecture 22, slide 13 ("Any amplitude including a final photon with momentum $k$: $i\mathcal M(k) = i\mathcal M^\mu(k)\epsilon^\ast_\mu(k)$. Only photon momentum $k$ highlighted (others suppressed). $\epsilon^\ast_\mu(k)$ = polarization of 'the' final photon. $i\mathcal M^\mu(k)$ = whatever rest of diagram gives"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2; PART 2 (g) · PS §5.5, eq. (5.76) · Yu §8.6.1, eq. (8.326)*

^def-c8a-16-1

## Two polarizations or four

> [!theorem] Theorem §C8a.16.1: The Physical Sum and the Invariant Sum
> For a photon along $\hat{\mathbf z}$, $k^\mu = (\kappa, 0, 0, \kappa)$, with the physical polarization vectors $\epsilon_1^\mu = (0, 1, 0, 0)$ and $\epsilon_2^\mu = (0, 0, 1, 0)$, spatial and transverse to $\hat{\mathbf z}$ ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]]):
> 1. the sum over the physical polarizations is
>
> $$
> \sum_{\rm phys}|\mathcal M|^2 = \sum_{r = 1, 2}\epsilon^{r\ast}_\mu\,\epsilon^r_\nu\,\mathcal M^\mu\mathcal M^{\nu\ast} = |\mathcal M^1|^2 + |\mathcal M^2|^2 ;
> $$
>
> 2. the Lorentz-invariant combination is
>
> $$
> -g_{\mu\nu}\,\mathcal M^\mu\mathcal M^{\nu\ast} = -|\mathcal M^0|^2 + |\mathcal M^1|^2 + |\mathcal M^2|^2 + |\mathcal M^3|^2 ;
> $$
>
> 3. the two agree if and only if $|\mathcal M^0| = |\mathcal M^3|$: the term of the polarization along the time direction and the term of the polarization along $\hat{\mathbf z}$ must cancel.
>
> The first is what is physically right; the second is what Lorentz invariance wants.
>
> *Model:* c-number algebra for one four-component $\mathcal M^\mu$; *applies:* any $\mathcal M^\mu(k)$ of [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]], $k$ along $\hat{\mathbf z}$; the physical sum is the same for the circular pair ([[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]], 4).
>
> *Source: PHY 513 Lecture 22, slide 14 ("For motion in the $\hat z$-direction: $k^\mu = (k, 0, 0, k)$. Physical polarizations are spatial and transverse to $\hat z$: $\epsilon_1^\mu = (0, 1, 0, 0)$, $\epsilon_2^\mu = (0, 0, 1, 0)$. Squaring amplitude (sum over physical polarizations only): $\sum_{\rm phys}|\mathcal M|^2 = \sum_{\rm phys}\epsilon^\ast_\mu\epsilon_\nu\mathcal M^\mu\mathcal M^{\nu\ast} = |\mathcal M^1|^2 + |\mathcal M^2|^2$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2 (the two displayed sums) · PS §5.5, eq. (5.77)*

^thm-c8a-16-1

> [!derivation]- Derivation
> **Step 1** (one polarization). $\epsilon_1$ has the lower components $\epsilon_{1\mu} = (0, -1, 0, 0)$ and is real, so $\mathcal M = \mathcal M^\mu\epsilon^\ast_{1\mu} = -\mathcal M^1$ and $|\mathcal M|^2 = |\mathcal M^1|^2$. In the same way $\epsilon_2$ gives $|\mathcal M^2|^2$. Item 1 is their sum.
>
> **Step 2** (the metric). $g_{\mu\nu} = \operatorname{diag}(1, -1, -1, -1)$, so $-g_{\mu\nu}\mathcal M^\mu\mathcal M^{\nu\ast} = -\mathcal M^0\mathcal M^{0\ast} + \sum_{i=1}^3\mathcal M^i\mathcal M^{i\ast}$: item 2.
>
> **Step 3** (compare). The difference of item 2 and item 1 is $|\mathcal M^3|^2 - |\mathcal M^0|^2$.
>
> **What the derivation shows.**
> - The polarizations along $\hat{\mathbf z}$ and along the time direction are not possible for a physical photon; the invariant sum nevertheless contains their terms, with opposite signs.
> - ⚑ By-product: the two sums agree exactly when the amplitudes for the two unphysical polarizations are equal in size → [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]], 2.

^der-c8a-16-1

*Uses:* [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]], [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]]

![[ph-qft-c8a-16-1.svg]]
*ADDED figure (not in the sources): the four polarization directions for a photon along $\hat{\mathbf z}$. Blue: the two transverse, physical ones. Red, dashed: the longitudinal and the timelike one, drawn apart because it points along the time axis. Below: the invariant sum split into the physical sum and the two terms that cancel by the Ward identity ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]]).*

> [!caution] Caution: The sum over all polarizations on slide 14
> Slide 14 writes "$\sum_{\rm all}|\mathcal M|^2 = \sum_{\rm all}\epsilon^\ast_\mu\epsilon_\nu\mathcal M^\mu\mathcal M^{\nu\ast} \to -|\mathcal M^0|^2 + |\mathcal M^1|^2 + |\mathcal M^2|^2 + |\mathcal M^3|^2$". A plain sum over the four basis vectors would give $+|\mathcal M^0|^2$. The minus sign belongs to the weight $-g^{rr}$ of the temporal mode in the completeness relation ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-4|Theorem §C8a.3.4]]); with it the sum is $-g_{\mu\nu}\mathcal M^\mu\mathcal M^{\nu\ast}$. The arrow on the slide stands for this weighted sum ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^cau-c8a-3-2|§C8a.3, Caution: The slide's polarization sum is not literally a completeness sum]]).
>
> *Source: PHY 513 Lecture 22, slide 14 · the user's PHY 513 notes, Lecture 22 update, Caution "Slips in the slides", third item (checked numerically)*

^cau-c8a-16-1

## The Ward identity

> [!theorem] Theorem §C8a.16.2: The Ward Identity
> In [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]], for any amplitude with an external photon of momentum $k$, with $\mathcal M^\mu(k)$ of [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]],
>
> $$
> k_\mu\,\mathcal M^\mu(k) = 0 .
> $$
>
> 1. **In words.** The amplitude vanishes when the polarization vector of one external photon is replaced by the momentum of that photon: $\epsilon^\ast_\mu(k) \to k_\mu$ for an outgoing photon, $\epsilon_\mu(k) \to k_\mu$ for an incoming one.
> 2. **Along $\hat{\mathbf z}$.** For $k^\mu = (\kappa, 0, 0, \kappa)$ it reads $\kappa\,(\mathcal M^0 - \mathcal M^3) = 0$: $\mathcal M^0 = \mathcal M^3$.
> 3. **Reason.** The photon is created or absorbed by the interaction $\int dt\,\hat H_I = \int d^4x\;e\,j^\mu A_\mu$ ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-2|Theorem §C8a.1.2]]), so $\mathcal M^\mu(k) \propto \int d^4x\,e^{ik\cdot x}\,\langle f|j^\mu(x)|i\rangle$, and the current is conserved, $\partial_\mu j^\mu = 0$ ([[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-3|Theorem §C5a.9.3]]).
> 4. **Scope.** It is exact, for any process and at any order of perturbation theory; it holds for the sum of the diagrams of a given order, not for single diagrams ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^rem-c8a-16-4|§C8a.16, Remark: Order by order, not diagram by diagram]]).
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* $k^2 = 0$, all other external particles on shell; the derivation below treats $\partial_\mu j^\mu = 0$ inside the matrix element as for a classical field ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^rem-c8a-16-1|§C8a.16, Remark: The quantum fine print]]).
>
> *Source: PHY 513 Lecture 22, slide 3 ("Photon wavefunction has 4 polarizations but only 2 are physical due to current conservation"), slide 15 ("Photons are created by the interaction $\int dt\,H_I = \int d^4x\,e\,j^\mu A_\mu$ with current $j^\mu = \bar\psi\gamma^\mu\psi$. … Generally, the matrix element is complicated: $|i\rangle$, $\langle f|$: all initial/final particles other than 'the' photon. Expansion of $Te^{-ie\bar\psi\gamma^\mu\psi A_\mu}$ gives more interactions"), slide 16 ("Integration by parts, then current conservation … With $k^\mu = (k, 0, 0, k)$: $0 = k_\mu\mathcal M^\mu(k) = k(\mathcal M^0 - \mathcal M^3)$ ⇒ $\mathcal M^0 = \mathcal M^3$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2, Derivation "Current conservation implies $k_\mu\mathcal M^\mu = 0$" · PS §5.5, eqs. (5.78)–(5.80) ("This famous relation is known as the Ward identity. It is essentially a statement of current conservation, which is a consequence of the gauge symmetry (4.6) of QED") · Yu §8.6.1, eqs. (8.328)–(8.331) and the boxed statement after (8.331)*

^thm-c8a-16-2

> [!derivation]- Derivation (as in the lecture)
> **Step 1** (the package). The photon field enters the interaction only in the combination $e\,j^\mu A_\mu$ with $j^\mu = \bar\psi\gamma^\mu\psi$ ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-2|Theorem §C8a.1.2]], [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|Theorem §C8a.1.3]]). In the free theory $j^0$ is the number density of electrons minus that of positrons ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]]); here the current is not expanded in oscillators, and only the fact that a photon, real or virtual, is always created or absorbed together with this package is used.
>
> **Step 2** (single out the photon). In the Dyson series $T\exp\bigl(-ie\int d^4x\,\hat{\bar\psi}\gamma^\mu\hat\psi\hat A_\mu\bigr)$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]) the outgoing photon is created by the $\hat A_\mu(x)$ of one vertex. The contraction with the photon of the final state leaves the wave function $\epsilon^\ast_\mu(k)\,e^{ik\cdot x}$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]]). What remains at that vertex is $-ie\,j^\mu(x)$, and everything else is collected in a matrix element:
>
> $$
> i\mathcal M^\mu(k)\,\epsilon^\ast_\mu \;\propto\; -ie\int d^4x\;e^{ik\cdot x}\,\langle f|\,j^\mu(x)\,|i\rangle\;\epsilon^\ast_\mu .
> $$
>
> Here $|i\rangle$ and $\langle f|$ contain all initial and final particles other than "the" photon. The matrix element is in general complicated: it contains the rest of the diagrams, with all the other interactions from the expansion of the exponential, so that $j^\mu(x)$ stands for the full interacting current. The sign $\propto$ hides the overall factors that are common to all components (the momentum-conservation delta function of the other particles).
>
> **Step 3** (replace the polarization by the momentum). Put $k_\mu$ in place of $\epsilon^\ast_\mu$ and use $k_\mu\,e^{ik\cdot x} = -i\,\partial_\mu e^{ik\cdot x}$:
>
> $$
> k_\mu\mathcal M^\mu(k) \;\propto\; -e\int d^4x\;\bigl(-i\,\partial_\mu e^{ik\cdot x}\bigr)\,\langle f|\,j^\mu(x)\,|i\rangle .
> $$
>
> **Step 4** (integrate by parts). The integral runs over all of spacetime and the integrand is the plane wave times the matrix element. Moving the derivative costs a sign, $-i \to +i$, and a surface term $\int d^4x\,\partial_\mu\bigl(e^{ik\cdot x}\langle f|j^\mu(x)|i\rangle\bigr)$, which is dropped: the plane-wave states stand for wave packets ([[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]), for which the matrix element of the current falls off at large distances and times.
>
> $$
> k_\mu\mathcal M^\mu(k) \;\propto\; -ie\int d^4x\;e^{ik\cdot x}\,\langle f|\,\partial_\mu j^\mu(x)\,|i\rangle .
> $$
>
> **Step 5** (current conservation). $\partial_\mu j^\mu = 0$: the right side vanishes. The current is the Noether current of the global phase symmetry ([[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-3|Theorem §C5a.9.3]]), and the interaction does not break that symmetry: the QED Lagrangian is invariant under a constant phase, a special gauge transformation ([[§C8a.2 Gauge Invariance#^thm-c8a-2-3|Theorem §C8a.2.3]]). Maxwell's equation with this source requires the same, $0 = \partial_\nu\partial_\mu F^{\mu\nu} = e\,\partial_\nu j^\nu$ ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|Theorem §C8a.1.3]], 2).
>
> **Step 6** (an incoming photon). Its wave function is $\epsilon_\mu(k)\,e^{-ik\cdot x}$, and $k_\mu e^{-ik\cdot x} = +i\,\partial_\mu e^{-ik\cdot x}$: the same steps with the opposite sign of $i$.
>
> **Step 7** (along $\hat{\mathbf z}$). $k_\mu = (\kappa, 0, 0, -\kappa)$ gives $k_\mu\mathcal M^\mu = \kappa\mathcal M^0 - \kappa\mathcal M^3$ (PS (5.80)).
>
> **What the derivation shows.**
> - Nothing about the process was used: only that the one photon couples to a conserved current. Whatever the matrix element is, it is the diagrammatic expansion of something conserved.
> - ⚑ By-product: $\mathcal M^0 = \mathcal M^3$ is the equality that [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-1|Theorem §C8a.16.1]], 3, needs → [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-3|Theorem §C8a.16.3]].
> - ⚑ Assumptions: the surface term of Step 4, and the use of $\partial_\mu j^\mu = 0$ inside the matrix element → [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^rem-c8a-16-1|§C8a.16, Remark: The quantum fine print]].
> - Had the vector particle been coupled to a current that is not conserved, Step 5 would fail and the unphysical polarizations would not drop out.

^der-c8a-16-2

*Uses:* [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]], [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-2|Theorem §C8a.1.2]], [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^thm-c8a-1-3|Theorem §C8a.1.3]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]], [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-3|Theorem §C5a.9.3]], [[§C8a.2 Gauge Invariance#^thm-c8a-2-3|Theorem §C8a.2.3]]

> [!remark] Remark: The quantum fine print
> The derivation uses $\partial_\mu j^\mu = 0$ as if $j^\mu$ were a classical field. For the operator, what is needed is $\langle f|\partial_\mu j^\mu(x)|i\rangle = 0$ for all $\langle f|$ and $|i\rangle$, and there is a subtlety when the derivative acts inside the perturbation series: the current stands inside a time-ordered product, and a time derivative does not commute with the time ordering. It produces additional terms with equal-time commutators (the mechanism of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-6|Theorem §C5b.8.6]] for one derivative of a time-ordered product). Filled in by the user's notes: these extra terms drop out when all the other external particles are on shell. The precise statement, which keeps track of them, is the Ward–Takahashi identity (PS §7.4), a topic of the second semester; the extra terms do not change anything stated in this section. PS announces the formal proof for its Section 7.4, and Yu remarks that the argument has a gap, closed in his Chapter 11.
>
> *Source: PHY 513 Lecture 22, slide 16 ("Warning: here we used $\partial_\mu j^\mu(x) = 0$ classically. For a quantum operator: $\langle f|\partial_\mu j^\mu(x)|i\rangle = 0$, $\forall\langle f|, |i\rangle$. A more precise Ward identity: 2nd term"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2, paragraph "The quantum fine print" (the sentence on equal-time commutators filled in by the user's notes; PS §7.4 was not read for this section) · PS §5.5, p. 160 ("Provided that this property still holds in the quantum theory … We will give a formal proof of the Ward identity in Section 7.4") · Yu §8.6.1, the sentence after the boxed statement following eq. (8.331)*

^rem-c8a-16-1

## The polarization sum

> [!theorem] Theorem §C8a.16.3: The Polarization Sum for External Photons
> For any amplitude with an external photon of momentum $k$, by the Ward identity ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]]),
>
> $$
> \sum_{\rm phys}\epsilon^\ast_\mu(k)\,\epsilon_\nu(k)\,\mathcal M^\mu\mathcal M^{\nu\ast} = |\mathcal M^1|^2 + |\mathcal M^2|^2 = |\mathcal M^1|^2 + |\mathcal M^2|^2 + |\mathcal M^3|^2 - |\mathcal M^0|^2 = -g_{\mu\nu}\,\mathcal M^\mu\mathcal M^{\nu\ast}
> $$
>
> (components for $k$ along $\hat{\mathbf z}$). Hence, in a sum over the physical polarizations of an external photon,
>
> $$
> \sum_{\rm pol}\epsilon^\ast_\mu(k)\,\epsilon_\nu(k) \;\to\; -g_{\mu\nu} .
> $$
>
> 1. The arrow is not an equality of tensors. The two sides give the same number after contraction with $\mathcal M^\mu\mathcal M^{\nu\ast}$; the true transverse sum differs from $-g_{\mu\nu}$ by terms proportional to $k_\mu$ or $k_\nu$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-3|Theorem §C4.8.3]]).
> 2. The replacement is made for one photon at a time. The Ward identity for one photon does not involve the polarization vectors of the other photons, which are among the suppressed labels of [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]], 1; it holds with their indices left open. So each polarization sum of a process with several external photons may be replaced in turn.
> 3. The right side is Lorentz invariant, although the physical polarization vectors were chosen in one frame.
>
> *Equivalently,* this is [[§C4.11 Vector-Field Propagators#^thm-c4-11-10|Theorem §C4.11.10]], which derives the replacement for a general direction of $k$, with the frame vector $n$, assuming the Ward identity. The assumption is now [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]].
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* sums over the two physical polarizations of external photons in any process, at any order; not needed for the photon propagator, where the four polarizations enter with their weights ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|Theorem §C8a.3.5]]).
>
> *Source: PHY 513 Lecture 22, slide 9, slide 17 ("Sum over physical $\epsilon$'s only, then use Ward identity: $\sum_{\rm phys.}\epsilon^\ast_\mu(k)\epsilon_\nu(k)\mathcal M^\mu(k)\mathcal M^{\nu\ast}(k) = |\mathcal M_1(k)|^2 + |\mathcal M_2(k)|^2 \to |\mathcal M_1|^2 + |\mathcal M_2|^2 + |\mathcal M_3|^2 - |\mathcal M_0|^2 = -g_{\mu\nu}\mathcal M^\mu\mathcal M^{\nu\ast}$"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2, Principle "The Ward identity and the polarization sum" ("one photon at a time") · PS §5.5, eq. (5.75) and the display after eq. (5.80) · Yu §8.6.1, eqs. (8.325), (8.327), (8.336)–(8.337) · item 2 written out here; PS (5.81) uses it for both photons of Compton scattering*

^thm-c8a-16-3

> [!derivation]- Derivation
> **Step 1** (the physical sum). [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-1|Theorem §C8a.16.1]], 1: $|\mathcal M^1|^2 + |\mathcal M^2|^2$.
>
> **Step 2** (add zero). By [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]], 2, $\mathcal M^0 = \mathcal M^3$, so $|\mathcal M^3|^2 - |\mathcal M^0|^2 = 0$ may be added.
>
> **Step 3** (recognize the metric). The four terms are $-g_{\mu\nu}\mathcal M^\mu\mathcal M^{\nu\ast}$ ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-1|Theorem §C8a.16.1]], 2).
>
> **Step 4** (a general direction). For $k$ not along $\hat{\mathbf z}$, rotate the axes; or use the transverse sum for any $k$, $\sum_{\rm pol}\epsilon^\ast_\mu\epsilon_\nu = -g_{\mu\nu} - \frac{k_\mu k_\nu}{(k\cdot n)^2} + \frac{k_\mu n_\nu + k_\nu n_\mu}{k\cdot n}$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-3|Theorem §C4.8.3]]), in which every term beyond $-g_{\mu\nu}$ contains $k_\mu$ or $k_\nu$ and vanishes on $\mathcal M^\mu\mathcal M^{\nu\ast}$ by the Ward identity ([[§C4.11 Vector-Field Propagators#^der-c4-11-10|Derivation §C4.11.10]], Step 2; Yu (8.327), (8.336)).
>
> **Step 5** (several photons). For two external photons write $\mathcal M = \epsilon^\ast_\mu(k')\epsilon_\nu(k)\mathcal M^{\mu\nu}$. The derivation of the Ward identity for one photon makes no use of the wave functions of the other particles, so it holds whatever vector stands on the index of the other photon. For each fixed $\nu$, $\mathcal M^{\mu\nu}$ is an $\mathcal M^\mu(k')$ in the sense of [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^def-c8a-16-1|Def. §C8a.16.1]], so $k'_\mu\mathcal M^{\mu\nu} = 0$ and the sum over the polarizations of the photon $k'$ becomes $-g_{\mu\rho}\mathcal M^{\mu\nu}\mathcal M^{\rho\sigma\ast}$. This is again of the form $\mathcal M^\nu\mathcal M^{\sigma\ast}$ in the indices of the photon $k$, summed over $\mu$, with $k_\nu\mathcal M^{\mu\nu} = 0$ for each $\mu$: the second replacement follows.
>
> **What the derivation shows.**
> - ⚑ By-product: the sum over two physical polarizations and the invariant sum over four are the same number. Either may be used: the invariant one for unpolarized cross sections, a projection onto definite polarizations when the polarization is of interest ([[§C8b.10 Helicity Suppression in Backward Compton Scattering|§C8b.10]]).
> - The frame vector $n$ and the choice of the transverse pair are invisible in the result: [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^rem-c4-8-1|§C4.8, Remark: The frame vector n is a choice that physics does not see]].

^der-c8a-16-3

*Uses:* [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-1|Theorem §C8a.16.1]], [[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-10|Theorem §C4.11.10]]

*Procedure:* [[P8 Unpolarized Cross Section from Diagrams#^p8-3|P8, step 3]]

> [!remark] Remark: The timelike polarization cancels the longitudinal one
> In $-g_{\mu\nu}\mathcal M^\mu\mathcal M^{\nu\ast}$ the term of the polarization along the time direction enters with a minus sign and cancels the term of the longitudinal polarization, along $\mathbf k$. This is sometimes phrased as "the longitudinal photon is cancelled by a negative-norm photon", the one along the time direction ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-6|Theorem §C8a.3.6]], [[§C4.9 Energy, Momentum and the Indefinite Fock Space#^thm-c4-9-6|Theorem §C4.9.6]]). Both are needed for Lorentz invariance, and neither is physical. What does the work is current conservation: the vector particle couples to a conserved current. Lorentz invariance and the restriction to physical polarizations are in tension, and current conservation resolves the tension. A vector particle coupled to a current that is not conserved would not have this property. The statement for the free field, without amplitudes, is that the temporal and longitudinal modes together form null states ([[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]]).
>
> *Source: PHY 513 Lecture 22, slide 17 ("Interpretation: 'longitudinal' photon (polarization along $\vec k$) cancels 'negative norm' photon (polarization along $k^0$). Both needed for Lorentz invariance but neither is physical"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2, paragraph "Interpretation" · PS §5.5, p. 161 ("the unphysical timelike and longitudinal photons can be consistently omitted from QED calculations … The negative norm of the timelike photon state … plays an essential role in this cancellation")*

^rem-c8a-16-2

> [!remark] Remark: The Ward identity is gauge invariance seen in amplitudes
> A polarization vector proportional to the momentum, $\epsilon_\mu \propto k_\mu$, is pure gauge: $A_\mu \propto k_\mu e^{-ik\cdot x}$ is the derivative $\partial_\mu$ of a function ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-3|Theorem §C8a.3.3]], 4). It looks like a field configuration of the photon, but it has no field strength: there is an $A_\mu$ and no electromagnetic field underneath ([[§C8b.4 Chirality#^thm-c8b-4-4|★ Theorem §C8b.4.4]], last point of its derivation). By the Ward identity such a configuration does not couple to the electron current. Consequently a shift
>
> $$
> \epsilon_\mu(k) \to \epsilon_\mu(k) + c\,k_\mu
> $$
>
> does not change any amplitude. This is the shift that a gauge transformation makes in the wave function of an external photon (Yu (8.332)–(8.335)) and that a Lorentz transformation makes in the polarization vector of a massless particle ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]]; [[§C8b.4 Chirality#^rem-c8b-4-4|§C8b.4, ★ Remark: Why photons of helicity ±1 do not contradict the rule]]; [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^rem-c4-6-3|§C4.6, Remark: Why a massless vector field must be a gauge field]]). What makes a photon genuine is two things: it has a transverse polarization, and it couples to electrons.
>
> *Source: PHY 513 Lecture 22, slide 17 ("What makes this work: gauge invariance"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2, paragraph "Gauge invariance" · Yu §8.6.1, eqs. (8.332)–(8.335) and the paragraph before eq. (8.336)*

^rem-c8a-16-3

> [!remark] Remark: Order by order, not diagram by diagram
> The Ward identity holds for the sum of all diagrams of a given order in $e$, and in general not for a single diagram. The diagrams of order $e^2$ cancel among themselves when a polarization vector is replaced by the momentum, those of order $e^4$ among themselves, and so on; a diagram of higher order cannot repair a diagram that was forgotten at a lower one. If one diagram of a given order is left out, the identity fails.
>
> *Source: PHY 513 Lecture 22, transcript (the answer to the question about higher-order diagrams) · the user's PHY 513 notes, Lecture 22 update, §22.2, paragraph "Asked in the lecture: what about higher-order diagrams?"*

^rem-c8a-16-4

## The example of Compton scattering

> [!theorem] Theorem §C8a.16.4: The Ward Identity for the Compton Amplitude
> For the amplitude of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-5|Theorem §C8a.15.5]], the Ward identity ([[§C8a.16 The Ward Identity and the Sum over Photon Polarizations#^thm-c8a-16-2|Theorem §C8a.16.2]]) says:
> 1. $\mathcal M = 0$ if $\epsilon^\ast_\mu(k')$ is replaced by $k'_\mu$;
> 2. $\mathcal M = 0$ if $\epsilon_\nu(k)$ is replaced by $k_\nu$;
> 3. this holds for the sum of the two diagrams and not for each diagram separately: the two diagrams cancel against each other;
> 4. it is therefore a check on the algebra that led to the amplitude: with a wrong sign, index or momentum somewhere, the two terms would not cancel.
>
> (Verification by explicit computation: PHY 513 Problem Set 12, Problem 1; to be added after submission.)
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, on-shell external momenta.
>
> *Source: PHY 513 Lecture 22, slide 18 ("Ward identity: $\mathcal M = 0$ for $\epsilon^\ast_\mu = k'_\mu$ or $\epsilon_\nu = k_\nu$. HW exercise: verify Ward Identity by explicit computation. … Invalid diagram by diagram, a cancellation of two diagrams"), and transcript · the user's PHY 513 notes, Lecture 22 update, §22.2, paragraph "Compton scattering as an example" · PS §5.5, p. 160 ("the terms from the two diagrams cancel each other to give zero")*

^thm-c8a-16-4

> [!remark]- Connections
> - The replacement $\sum\epsilon^\ast_\mu\epsilon_\nu \to -g_{\mu\nu}$ is what turns the square of the Compton amplitude into a trace with contracted indices — [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-6|Theorem §C8a.15.6]], [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-7|Theorem §C8a.15.7]].
> - The same statement in Yu's notation, with the transverse sum for a general momentum and the frame vector $n$ — [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-3|Theorem §C4.8.3]], [[§C4.11 Vector-Field Propagators#^thm-c4-11-10|Theorem §C4.11.10]].
> - The four-polarization sum inside the photon propagator is a different statement and needs no Ward identity — [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-4|Theorem §C8a.3.4]], [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^cau-c8a-3-2|§C8a.3, Caution: The slide's polarization sum is not literally a completeness sum]].
> - Gauge symmetry of the Lagrangian, of which the Ward identity is the form in amplitudes; the conserved current as the Noether current of its global part — [[§C8a.2 Gauge Invariance#^pr-c8a-2-1|Principle §C8a.2.1]], [[§C8a.2 Gauge Invariance#^rem-c8a-2-2|§C8a.2, Remark: What the gauge symmetry is for]], [[§C5a.9 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-9-3|Theorem §C5a.9.3]].
> - Free-field version of the cancellation: physical states are the transverse ones up to null states — [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-4|Theorem §C4.10.4]], [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]]; the count "three minus one" of [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-6|Theorem §C8a.3.6]].
> - Polarization vectors of a massless particle are defined up to multiples of the momentum; the amplitude is blind to them — [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]], [[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-4|§C8b.3, Remark: Two polarizations, and why a massless vector field needs gauge invariance]].
> - When the polarization is not summed but selected, the helicity vectors are used instead of the replacement — [[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]], [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-3|Theorem §C8b.10.3]].
