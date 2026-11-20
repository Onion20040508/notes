---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
← [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C9.1 Discrete Lorentz Transformations|§C9.1]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §4.3.1, eqs. (4.103)–(4.121); §4.2.2, eqs. (4.41)–(4.43); §4.4.4, eqs. (4.267)–(4.280) · the user's pre-course notes, §4.3 ("a helicity eigenstate"; Note "Checking the helicity eigenvalue equation"), §4.4 ("Physical helicity states") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §9.4, p. 298 · PHY 513 Lecture 18 (Larsen, 9 Nov 2026), slides 9, 13 (course forms: [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator|§C8a.3]]); Lecture 20, slide 28 (the "+" polarization of the virtual photon). Moved here from §C4.3★, §C4.5★ and §C4.10 (2026-11-16, user decision: the helicity material next to Lecture 20).*

*Draft: Definition §C8b.9.1 and Theorems §C8b.9.4–§C8b.9.9 were written ahead of PHY 513 (photon quantization is Lecture 25) from Yu, the user's pre-course notes and Peskin–Schroeder, in Yu's notation, and are to be revised after Lecture 25, as the rest of [[§C4.10 The Gupta–Bleuler Condition and Physical Photons|§C4.10]]. Lecture 18 taught only their outcome: two transverse physical polarizations, written in the circular basis.*

Which helicities do the quanta of a vector field carry? A massive spin-1 particle has the three helicities $+1, 0, -1$ of its $2s + 1$ states ([[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-2|§C8b.3, Remark: Helicity of a massive particle]]); a massless one only $\pm1$, each Lorentz invariant ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]], [[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-3|§C8b.3, Remark: Parity pairs λ with −λ]]). This section finds both on the quantized fields: the helicity polarization vectors are eigenvectors of the spin matrix along $\hat{\mathbf p}$, the one-particle states inherit their eigenvalues through the covariance law, and the Noether spin confirms them, once for the Proca field (★, beyond the course) and once for the photon, whose physical states are those of the Gupta–Bleuler condition. Lecture 20 uses the result in its last step: the vertex current of $e^-_Re^+_L$ is the circular polarization vector of a $J_z = +1$ photon ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]).

The section is the vector counterpart of [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]]. The polarization vector plays the part of the two-spinor; its two bases, linear and helicity, are compared in [[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]]; and the closing remark sets the spinor and the vector field side by side ([[§C8b.9 Photon Helicity#^rem-c8b-9-1|Remark: Helicity and chirality for the spinor field and the vector field]]). Why a vector potential, whose index has no chirality, can describe helicity $\pm1$ at all is the general rule of [[§C8b.4 Chirality#^thm-c8b-4-3|★ Theorem §C8b.4.3]] with [[§C8b.4 Chirality#^thm-c8b-4-4|★ Theorem §C8b.4.4]].

**The mathematical picture.** The four components of a vector field carry $(\frac12, \frac12)$, whose rotation content is spin $0 \oplus 1$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-9|Theorem §C3.2.9]]). The matrix $\hat{\mathbf p}\cdot\boldsymbol{\mathcal J}$ of the vector representation ([[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]]) has eigenvalues $\pm1$ on the plane transverse to $\hat{\mathbf p}$ and $0$ on the span of $(1, \mathbf 0)$ and $(0, \hat{\mathbf p})$; a polarization vector is an intertwiner between this index and the particle's spin label, so its eigenvalue becomes the helicity of the state it creates. The massive field keeps the three transverse-to-$p$ vectors; the massless one keeps the two transverse ones on the physical subspace.

**Setup.** Two systems, each box names its own. *Massive:* the free Proca quantum field of [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^mod-c4-4-1|Model §C4.4.1]] ($m > 0$) on its positive-norm Fock space ([[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^pr-c4-5-1|Principle §C4.5.1]]), one-particle states $|\mathbf p, \lambda\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p,\lambda}|0\rangle$ in the helicity basis of [[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]], $\mathbf p \ne \mathbf 0$. *Massless:* the free Feynman-gauge field of [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]] ($m = 0$, $\xi = 1$) on the indefinite-metric Fock space of [[§C4.9 Energy, Momentum and the Indefinite Fock Space#^pr-c4-9-5|Principle §C4.9.5]]; operator identities hold on the whole space, statements on norms, expectation values and null states on the physical subspace of the Gupta–Bleuler condition ([[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^pr-c4-10-1|Principle §C4.10.1]]). The helicity from $\hat{\mathbf J}$ (★ Theorem §C8b.9.2, Theorem §C8b.9.5) assumes the covariance law of a vector field ([[§C4.1 The Vector Field and Its Lorentz Transformation#^rem-c4-1-1|§C4.1, Remark: The quantum vector field, recalled]]); the Noether route (★ Theorems §C8b.9.3, §C8b.9.7–§C8b.9.9) does not. Relativistic normalization, continuum normalization; all results exact for the free fields.

*Conventions* ([[Larsen PHY 513]]): Yu's notation of C4 is kept inside the boxes: polarization vectors $e^\mu(p, \sigma)$, $\varepsilon^\mu(p, \lambda)$, covariant mode operators $\hat b_{\mathbf p,\sigma}$, helicity modes $\hat a_{\mathbf p,\pm}$; the course writes $\epsilon^r_\mu(p)$, $\hat a^r_{\mathbf p}$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^cau-c4-8-2|§C4.8, Caution: Names for the photon's polarization vectors and mode operators]]). Rotations act as $U(R) = e^{-i\theta\,\hat{\mathbf u}\cdot\hat{\mathbf J}}$; $\hat{\mathbf p} = \mathbf p/|\mathbf p|$ is a c-number unit vector.

## Spin one with a mass

> [!theorem] ★ Theorem §C8b.9.1: The Helicity Vectors Are Helicity Eigenvectors
> With the helicity matrix of [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]] for $\hat{\mathbf n} = \hat{\mathbf p}$,
>
> $$
> (\hat{\mathbf p}\cdot\boldsymbol{\mathcal J})^\mu{}_\nu\,\varepsilon^\nu(p, \lambda) = \lambda\,\varepsilon^\mu(p, \lambda), \qquad \lambda = +1, 0, -1 :
> $$
>
> $\varepsilon(p, \pm)$ are the transverse polarizations of helicity $\pm1$ (right and left circular), $\varepsilon(p, 0)$ the longitudinal polarization of helicity $0$.
>
> *Source: Yu §4.3.1, eqs. (4.103)–(4.108) · the user's pre-course notes, §4.3, eq. (helicity-eigen) and Note "Checking the helicity eigenvalue equation"*

^thm-c8b-9-1

> [!derivation]- Derivation
> **1. Transverse vectors.** $(\mathbf e(p, 1), \mathbf e(p, 2), \hat{\mathbf p})$ is a right-handed orthonormal triad ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]]), so by [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]] (with $\mathbf e_1 = \mathbf e(p, 1)$, $\mathbf e_2 = \mathbf e(p, 2)$) the vectors $\varepsilon(p, \pm) = \frac1{\sqrt2}(0, \mathbf e(p, 1) \pm i\mathbf e(p, 2))$ have eigenvalues $\pm1$.
>
> **2. Longitudinal vector.** $\varepsilon(p, 0) = \frac{|\mathbf p|}{m}(1, \mathbf 0) + \frac{E_{\mathbf p}}{m}(0, \hat{\mathbf p})$, a combination of the two eigenvectors with eigenvalue $0$ of Theorem §C4.1.1: eigenvalue $0$. Yu verifies all three by multiplying out the matrix (4.103) with the column vectors (4.104), (4.105)–(4.107).
>
> **What the derivation shows**
> - Helicity is measured by the spin matrix of the index along $\hat{\mathbf p}$; the time component, although nonzero in $\varepsilon(p, 0)$, is inert under it. The matrix $\hat{\mathbf p}\cdot\boldsymbol{\mathcal J}$ does not commute with boosts along $\hat{\mathbf p}$, but $L(p)$ maps its eigenvectors at rest to eigenvectors at $p$ with the same eigenvalue because both lie in the span of $(1, \mathbf 0)$, $(0, \hat{\mathbf p})$ or in the plane $\perp\hat{\mathbf p}$, which $L(p)$ preserves.
> - Used next: the helicity of the one-particle states ([[§C8b.9 Photon Helicity#^thm-c8b-9-2|Theorem §C8b.9.2]]).

^der-c8b-9-1

*Uses:* [[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]], [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]]

> [!theorem] ★ Theorem §C8b.9.2: The One-Particle States Are Helicity Eigenstates
> In the helicity basis ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]]), for $\mathbf p \ne \mathbf 0$, with $\hat{\mathbf p} = \mathbf p/|\mathbf p|$ the unit vector (a c-number, not an operator),
>
> $$
> [\hat a_{\mathbf p,\lambda}, \hat{\mathbf p}\cdot\hat{\mathbf J}] = \lambda\,\hat a_{\mathbf p,\lambda}, \qquad (\hat{\mathbf p}\cdot\hat{\mathbf J})\,|\mathbf p, \lambda\rangle = \lambda\,|\mathbf p, \lambda\rangle, \qquad \lambda = +1, 0, -1 :
> $$
>
> $|\mathbf p, \pm\rangle$ are the transverse states of helicity $\pm1$, $|\mathbf p, 0\rangle$ the longitudinal state.
>
> *Model:* [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^mod-c4-4-1|Model §C4.4.1]]; *applies:* as [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-7|Theorem §C4.5.7]], helicity basis, $\mathbf p \ne \mathbf 0$.
>
> *Source: Yu §4.3.1, eqs. (4.110)–(4.121) · the user's pre-course notes, §4.3 ("a helicity eigenstate") · derived here by the finite rotation about $\hat{\mathbf p}$*

^thm-c8b-9-2

> [!derivation]- Derivation
> **1. Rotations about $\hat{\mathbf p}$.** For $R = R(\hat{\mathbf p}, \theta)$, $R\mathbf p = \mathbf p$, and $R\varepsilon(p, \lambda) = e^{-i\lambda\theta}\varepsilon(p, \lambda)$ ([[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]] with [[§C8b.9 Photon Helicity#^thm-c8b-9-1|Theorem §C8b.9.1]]; $\varepsilon(p, 0)$ lies in the span of the two eigenvalue-$0$ vectors). So $\mathcal D_{\lambda'\lambda}(R, \mathbf p) = -\varepsilon^{\ast}(p, \lambda')\cdot e^{-i\lambda\theta}\varepsilon(p, \lambda) = e^{-i\lambda\theta}\delta_{\lambda'\lambda}$.
>
> **2. Insert in Theorem §C4.5.7.** $U(R)|\mathbf p, \lambda\rangle = e^{-i\lambda\theta}|\mathbf p, \lambda\rangle$, and step 4 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-7|Derivation §C4.5.7]] gives $U^{-1}\hat a_{\mathbf p,\lambda}U = e^{-i\lambda\theta}\hat a_{\mathbf p,\lambda}$.
>
> **3. Differentiate.** With $U(R) = e^{-i\theta\,\hat{\mathbf p}\cdot\hat{\mathbf J}}$ ($\hat{\mathbf p}$ a fixed unit vector, not an operator), $\frac{d}{d\theta}\big|_0$ of $U|\mathbf p, \lambda\rangle$ gives $-i\,\hat{\mathbf p}\cdot\hat{\mathbf J}|\mathbf p, \lambda\rangle = -i\lambda|\mathbf p, \lambda\rangle$; of $U^{-1}\hat aU = \hat a + i\theta[\hat{\mathbf p}\cdot\hat{\mathbf J}, \hat a] + O(\theta^2)$ it gives $i[\hat{\mathbf p}\cdot\hat{\mathbf J}, \hat a] = -i\lambda \hat a$, i.e. $[\hat a, \hat{\mathbf p}\cdot\hat{\mathbf J}] = \lambda \hat a$ (Yu (4.114)).
>
> **What the derivation shows**
> - For a free particle $\hat{\mathbf p}\cdot\hat{\mathbf J}$ is the helicity operator: the orbital part has no component along $\hat{\mathbf p}$ (Yu after (4.121)).
> - Yu reaches (4.112) by equating coefficients of $e^{\mp ip\cdot x}$ in $[\hat A^\mu, \hat{\mathbf J}] = -i\,\mathbf x\times\nabla\hat A^\mu + \boldsymbol{\mathcal J}^\mu{}_\nu \hat A^\nu$, but the orbital term $\mathbf x\times\mathbf p$ depends on $\mathbf x$, so these are not Fourier coefficients; the orbital part of $[\hat a_{\mathbf p,\lambda}, \hat{\mathbf J}]$ is really a momentum-space derivative ($-i\,\mathbf p\times\nabla_{\mathbf p}$, plus a term from the $\mathbf p$-dependence of $\varepsilon$). Its component along $\hat{\mathbf p}$ vanishes, so (4.114) and (4.121) are correct; the finite rotation about the fixed axis $\hat{\mathbf p}$ avoids the issue.

^der-c8b-9-2

*Uses:* [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-7|Theorem §C4.5.7]], [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-1|Theorem §C4.1.1]], [[§C8b.9 Photon Helicity#^thm-c8b-9-1|Theorem §C8b.9.1]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-6|Theorem §C3.4.6]]

> [!theorem] ★ Theorem §C8b.9.3: Helicity and Transverse Spin from the Noether Spin
> On a one-particle state $|\mathbf p, \lambda\rangle$ of the Proca field, $\hat{\mathbf S}|\mathbf p, \lambda\rangle = \sum_{\lambda'}\boldsymbol{\mathcal S}_{\lambda'\lambda}(\mathbf p)|\mathbf p, \lambda'\rangle + |\text{three particles}\rangle$ ([[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-11|Theorem §C4.5.11]], with $\boldsymbol{\mathcal S}$ of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-9|Theorem §C4.5.9]]). In the helicity basis ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]]), for $\mathbf p \ne \mathbf 0$:
> 1. **along the momentum**, $\hat{\mathbf p}\cdot\boldsymbol{\mathcal S}_{\lambda'\lambda}(\mathbf p) = \lambda\,\delta_{\lambda'\lambda}$, so $\langle\mathbf p', \lambda'|\,\hat{\mathbf p}\cdot\hat{\mathbf S}\,|\mathbf p, \lambda\rangle = \lambda\,\langle\mathbf p', \lambda'|\mathbf p, \lambda\rangle$ for the fixed unit vector $\hat{\mathbf p}$, $\lambda = +1, 0, -1$: the helicities of [[§C8b.9 Photon Helicity#^thm-c8b-9-2|Theorem §C8b.9.2]];
> 2. **across the momentum**, $\boldsymbol{\mathcal S}_{\pm\pm} = \pm\hat{\mathbf p}$, $\boldsymbol{\mathcal S}_{00} = \boldsymbol{\mathcal S}_{\pm\mp} = 0$ and $\boldsymbol{\mathcal S}_{\pm0} = \mp\frac{E_{\mathbf p}^2 + m^2}{2mE_{\mathbf p}}\,\boldsymbol\varepsilon^{\ast}(p, \pm)$, $\boldsymbol{\mathcal S}_{0\pm} = \overline{\boldsymbol{\mathcal S}_{\pm0}}$: the transverse spin of a moving quantum is not the rest-frame spin matrix.
>
> *Model:* [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^mod-c4-4-1|Model §C4.4.1]]; *applies:* free field, one-particle states on $|0\rangle$; exact; helicity basis, $\mathbf p \ne \mathbf 0$.
>
> *Source: derived here; item 1 agrees with Yu §4.3.1, eqs. (4.110)–(4.121), and with the user's pre-course notes, §4.3 ("a helicity eigenstate"), which reach it through the covariance law*

^thm-c8b-9-3

> [!derivation]- Derivation
> **1–3.** Steps 1–3 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-11|Derivation §C4.5.11]]: the number-conserving part of $\hat{\mathbf S}$ acts on $|\mathbf p, \lambda\rangle$ by the matrix $\boldsymbol{\mathcal S}_{\lambda'\lambda}(\mathbf p)$, and the rest is a three-particle vector orthogonal to every one-particle state.
>
> **4. Along $\hat{\mathbf p}$.** $\hat{\mathbf p}\cdot\bigl(\mathbf p\times\mathbf v\bigr) = 0$ for every $\mathbf v$, so the second term of $\boldsymbol{\mathcal S}$ drops out of $\hat{\mathbf p}\cdot\boldsymbol{\mathcal S}$. The first gives $-\varepsilon^{\ast}(p, \lambda')\cdot(\hat{\mathbf p}\cdot\boldsymbol{\mathcal J})\varepsilon(p, \lambda) = -\lambda\,\varepsilon^{\ast}(p, \lambda')\cdot\varepsilon(p, \lambda) = \lambda\,\delta_{\lambda'\lambda}$, by the eigenvalue equation $(\hat{\mathbf p}\cdot\boldsymbol{\mathcal J})\varepsilon(p, \lambda) = \lambda\varepsilon(p, \lambda)$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-1|Theorem §C8b.9.1]]) and orthonormality ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]]). Then $\langle\mathbf p', \lambda'|\hat{\mathbf p}\cdot\hat{\mathbf S}|\mathbf p, \lambda\rangle = \sum_\mu\hat{\mathbf p}\cdot\boldsymbol{\mathcal S}_{\mu\lambda}\langle\mathbf p', \lambda'|\mathbf p, \mu\rangle + 0 = \lambda\langle\mathbf p', \lambda'|\mathbf p, \lambda\rangle$, the three-particle part dropping by step 2.
>
> **5. Across $\hat{\mathbf p}$.** Use step 6 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-9|Derivation §C4.5.9]], $\boldsymbol{\mathcal S}_{\lambda\lambda'} = i\boldsymbol\varepsilon(\lambda')\times\boldsymbol\varepsilon^{\ast}(\lambda) + \frac{i}{2E}\mathbf p\times[\varepsilon^{0\ast}(\lambda)\boldsymbol\varepsilon(\lambda') - \varepsilon^0(\lambda')\boldsymbol\varepsilon^{\ast}(\lambda)]$, with $\boldsymbol\varepsilon(\pm) = (\mathbf e_1 \pm i\mathbf e_2)/\sqrt2$, $\boldsymbol\varepsilon(0) = \frac Em\hat{\mathbf p}$, $\varepsilon^0(\pm) = 0$, $\varepsilon^0(0) = |\mathbf p|/m$, and $\hat{\mathbf p}\times\boldsymbol\varepsilon^{\ast}(\pm) = \pm i\boldsymbol\varepsilon^{\ast}(\pm)$ (conjugate of step 5 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-10|Derivation §C4.5.10]]).
> - $(\pm, \pm)$: $\boldsymbol\varepsilon(\pm)\times\boldsymbol\varepsilon^*(\pm) = \frac12(\mathbf e_1 \pm i\mathbf e_2)\times(\mathbf e_1 \mp i\mathbf e_2) = \frac12(\mp i - (\pm i))\,\mathbf e_1\times\mathbf e_2 = \mp i\,\hat{\mathbf p}$, times $i$: $\pm\hat{\mathbf p}$; no $\varepsilon^0$ term.
> - $(\pm, \mp)$: $\boldsymbol\varepsilon^*(\pm) = \boldsymbol\varepsilon(\mp)$, so $\boldsymbol\varepsilon(\mp)\times\boldsymbol\varepsilon^*(\pm) = \boldsymbol\varepsilon(\mp)\times\boldsymbol\varepsilon(\mp) = 0$. $(0, 0)$: $\boldsymbol\varepsilon(0)$ is real, $\boldsymbol\varepsilon(0)\times\boldsymbol\varepsilon(0) = 0$, and the bracket is $\frac{|\mathbf p|}{m}(\boldsymbol\varepsilon(0) - \boldsymbol\varepsilon(0)) = 0$.
> - $(\pm, 0)$: first term $i\frac Em\hat{\mathbf p}\times\boldsymbol\varepsilon^*(\pm) = i\frac Em(\pm i)\boldsymbol\varepsilon^*(\pm) = \mp\frac Em\boldsymbol\varepsilon^*(\pm)$; second term $\frac{i}{2E}\mathbf p\times\bigl[0 - \frac{|\mathbf p|}{m}\boldsymbol\varepsilon^*(\pm)\bigr] = -\frac{i|\mathbf p|^2}{2mE}(\pm i)\boldsymbol\varepsilon^*(\pm) = \pm\frac{|\mathbf p|^2}{2mE}\boldsymbol\varepsilon^*(\pm)$. Sum: $\mp\frac{2E^2 - |\mathbf p|^2}{2mE}\boldsymbol\varepsilon^*(\pm) = \mp\frac{E^2 + m^2}{2mE}\boldsymbol\varepsilon^*(\pm)$, by the mass shell $|\mathbf p|^2 = E^2 - m^2$.
> - $(0, \pm)$: Hermiticity (step 8 of Derivation §C4.5.9).
>
> **What the derivation shows**
> - ⚑ By-product: the components of $\hat{\mathbf S}$ across the momentum are boost dependent: $\frac{E^2 + m^2}{2mE} = 1$ at rest and grows like $E/2m$. Only the helicity, the component along $\hat{\mathbf p}$, is the same in every frame reached by a boost along $\hat{\mathbf p}$; this is why the little group, not the canonical spin, classifies moving particles ([[§C8b.2 Particle States and the Little Group#^thm-c8b-2-9|Theorem §C8b.2.9]]).

^der-c8b-9-3

*Uses:* [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-11|Theorem §C4.5.11]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-11|Derivation §C4.5.11]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-9|Theorem §C4.5.9]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-9|Derivation §C4.5.9]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-10|Derivation §C4.5.10]], [[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]], [[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]], [[§C8b.9 Photon Helicity#^thm-c8b-9-1|Theorem §C8b.9.1]]

## Photons of definite helicity

> [!definition] Definition §C8b.9.1: Helicity Mode Operators
> $$
> \hat a_{\mathbf p,\pm} \equiv \frac{1}{\sqrt2}\bigl(\hat b_{\mathbf p,1} \mp i\hat b_{\mathbf p,2}\bigr), \qquad \hat a^\dagger_{\mathbf p,\pm} = \frac{1}{\sqrt2}\bigl(\hat b^\dagger_{\mathbf p,1} \pm i\hat b^\dagger_{\mathbf p,2}\bigr); \qquad \hat b_{\mathbf p,1} = \frac{\hat a_{\mathbf p,+} + \hat a_{\mathbf p,-}}{\sqrt2}, \quad \hat b_{\mathbf p,2} = \frac{i\bigl(\hat a_{\mathbf p,+} - \hat a_{\mathbf p,-}\bigr)}{\sqrt2} ,
> $$
>
> with the one-photon states $|\mathbf p, \pm\rangle \equiv \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p,\pm}|0\rangle$ (the analogues of the massive helicity states, [[§C8b.9 Photon Helicity#^thm-c8b-9-2|Theorem §C8b.9.2]]).
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field, operators on the full indefinite-metric space; relativistic normalization of $|\mathbf p, \pm\rangle$.
>
> *Source: Yu §4.4.4, eqs. (4.267)–(4.268), (4.276) · the user's pre-course notes, §4.4 ("Physical helicity states")*

^def-c8b-9-1

> [!theorem] Theorem §C8b.9.4: Helicity Mode Algebra and Expansion
> 1. $[\hat a_{\mathbf p,\lambda}, \hat a^\dagger_{\mathbf q,\lambda'}] = \delta_{\lambda\lambda'}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $[\hat a, \hat a] = [\hat a^\dagger, \hat a^\dagger] = 0$, and $\hat a_{\mathbf p,\lambda}$, $\hat a^\dagger_{\mathbf p,\lambda}$ commute with $\hat b_{\mathbf q,\sigma}$, $\hat b^\dagger_{\mathbf q,\sigma}$ for $\sigma = 0, 3$: positive-norm, physical creators.
> 2. $\sum_{\sigma = 1}^2e^\mu(p, \sigma)\hat b_{\mathbf p,\sigma} = \sum_{\lambda = \pm}\varepsilon^\mu(p, \lambda)\hat a_{\mathbf p,\lambda}$, so
>
> $$
> \hat A^\mu(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl[\sum_{\sigma = 0, 3}e^\mu(p, \sigma)\bigl(\hat b_{\mathbf p,\sigma}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p,\sigma}e^{ip\cdot x}\bigr) + \sum_{\lambda = \pm}\bigl(\varepsilon^\mu(p, \lambda)\hat a_{\mathbf p,\lambda}e^{-ip\cdot x} + \varepsilon^{\mu*}(p, \lambda)\hat a^\dagger_{\mathbf p,\lambda}e^{ip\cdot x}\bigr)\Bigr] ,
> $$
>
> the first line unphysical, the second the two physical circular polarizations.
> 3. $\sum_{\sigma = 1}^2\hat b^\dagger_{\mathbf p,\sigma}\hat b_{\mathbf p,\sigma} = \sum_{\lambda = \pm}\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda}$.
>
> *Course form (Lecture 18):* [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-1|Theorem §C8a.3.1]] written with a circular transverse pair, $\epsilon$ in the annihilation term and $\epsilon^\ast$ in the creation term; external photons then carry $\epsilon_\mu$ (incoming) and $\epsilon^\ast_\mu$ (outgoing), [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-1|Theorem §C8a.4.1]].
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field; operator identities on the full indefinite-metric space, exact.
>
> *Source: Yu §4.4.4, eqs. (4.269)–(4.275), (4.278) · the user's pre-course notes, §4.4*

^thm-c8b-9-4

> [!derivation]- Derivation
> **1. Same helicity.** $[\hat a_{\mathbf p,\pm}, \hat a^\dagger_{\mathbf q,\pm}] = \frac12[\hat b_1 \mp ib_2, \hat b^\dagger_1 \pm i\hat b^\dagger_2] = \frac12\bigl([\hat b_1, \hat b^\dagger_1] + (\mp i)(\pm i)[\hat b_2, \hat b^\dagger_2] \pm i[\hat b_1, \hat b^\dagger_2] \mp i[\hat b_2, \hat b^\dagger_1]\bigr) = \frac12(1 + 1 + 0 + 0)(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, with $[\hat b_i, \hat b^\dagger_i] = -g_{ii}(2\pi)^3\delta^3 = +(2\pi)^3\delta^3$ for $i = 1, 2$ and the mixed ones zero ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-11|Theorem §C4.8.11]]).
>
> **2. Opposite helicity.** $\hat a^\dagger_{\mathbf q,\mp} = \frac{1}{\sqrt2}(\hat b^\dagger_1 \mp i\hat b^\dagger_2)$, so $[\hat a_{\mathbf p,\pm}, \hat a^\dagger_{\mathbf q,\mp}] = \frac12\bigl([\hat b_1, \hat b^\dagger_1] + (\mp i)(\mp i)[\hat b_2, \hat b^\dagger_2]\bigr) = \frac12(1 - 1)(2\pi)^3\delta^3 = 0$. $[\hat a, \hat a] = 0$ and $[\hat a^\dagger, \hat a^\dagger] = 0$ follow from $[\hat b, \hat b] = 0$. Commutation with $\hat b_{0, 3}$, $\hat b^\dagger_{0, 3}$: $g_{\sigma\sigma'}$ is diagonal, so $[\hat b_{1, 2}, \hat b^\dagger_{0, 3}] = 0$. Hence $(\hat b_{\mathbf q,0} - \hat b_{\mathbf q,3})\hat a^\dagger_{\mathbf p,\lambda}|\Psi\rangle = \hat a^\dagger_{\mathbf p,\lambda}(\hat b_{\mathbf q,0} - \hat b_{\mathbf q,3})|\Psi\rangle$: $\hat a^\dagger$ maps physical states to physical states.
>
> **3. Item 2.** Insert the inverse relations of [[§C8b.9 Photon Helicity#^def-c8b-9-1|Def. §C8b.9.1]]: $e(1)\hat b_1 + e(2)\hat b_2 = e(1)\frac{\hat a_+ + \hat a_-}{\sqrt2} + e(2)\frac{i(\hat a_+ - \hat a_-)}{\sqrt2} = \frac{e(1) + ie(2)}{\sqrt2}\hat a_+ + \frac{e(1) - ie(2)}{\sqrt2}\hat a_- = \varepsilon(+)\hat a_+ + \varepsilon(-)\hat a_-$ by [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]]. The adjoint gives $\sum_\sigma e(\sigma)\hat b^\dagger_\sigma = \sum_\lambda\varepsilon^{\ast}(\lambda)\hat a^\dagger_\lambda$ (Yu (4.273)–(4.274)); substitute into [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-9|Theorem §C4.8.9]].
>
> **4. Item 3.** $\hat b^\dagger_1\hat b_1 = \frac12(\hat a^\dagger_+ + \hat a^\dagger_-)(\hat a_+ + \hat a_-)$ and $\hat b^\dagger_2\hat b_2 = \frac12(-i)(i)(\hat a^\dagger_+ - \hat a^\dagger_-)(\hat a_+ - \hat a_-) = \frac12(\hat a^\dagger_+ - \hat a^\dagger_-)(\hat a_+ - \hat a_-)$. Expanding both into four terms, the cross terms $\pm\frac12(\hat a^\dagger_+\hat a_- + \hat a^\dagger_-\hat a_+)$ cancel and the diagonal ones add: $\hat a^\dagger_+\hat a_+ + \hat a^\dagger_-\hat a_-$.
>
> **What the derivation shows**
> - The physical photon is two ordinary bosonic oscillators per momentum, exactly the scalar algebra twice, with positive norms.

^der-c8b-9-4

*Uses:* [[§C8b.9 Photon Helicity#^def-c8b-9-1|Def. §C8b.9.1]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-11|Theorem §C4.8.11]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-9|Theorem §C4.8.9]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]]

> [!theorem] Theorem §C8b.9.5: Photons Have Helicity ±1
> Suppose rotations act on the state space by operators $U(R) = e^{-i\theta\,\hat{\mathbf u}\cdot\hat{\mathbf J}}$ (rotation by $\theta$ about $\hat{\mathbf u}$, the convention of [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-2|Theorem §C8b.3.2]]) with $U(R)|0\rangle = |0\rangle$, under which $\hat A^\mu$ transforms as a four-vector field ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]] with $D = \Lambda$, [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]]). Then
>
> $$
> [(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat a^\dagger_{\mathbf p,\pm}] = \pm \hat a^\dagger_{\mathbf p,\pm}, \qquad \hat h\,|\mathbf p, \pm\rangle = \pm|\mathbf p, \pm\rangle ,
> $$
>
> with $\hat h = \hat{\mathbf J}\cdot\hat{\mathbf P}/|\hat{\mathbf P}|$ the helicity ([[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]): the physical photons have helicity $\pm1$, the values allowed by [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-6|Theorem §C8b.3.6]] for a particle without continuous spin ([[§C8b.3 Massless Particles and Helicity#^law-c8b-3-4|Law §C8b.3.4]]). The unphysical $|\mathbf p, 0\rangle$, $|\mathbf p, 3\rangle$ have $(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J} = 0$.
>
> *Course form (Lecture 18):* the two physical polarizations of [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]], in the circular basis $\epsilon^\mu = (0, 1, \pm i, 0)/\sqrt2$ for $\mathbf p \parallel \hat{\mathbf z}$.
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field, states on $|0\rangle$; assumes the covariance law under rotations with $U(R)|0\rangle = |0\rangle$, as stated; the transverse states $|\mathbf p, \pm\rangle$ are physical ([[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-4|Theorem §C4.10.4]]).
>
> *Source: Yu §4.4.4, eq. (4.277) (stated "类似于 (4.121) 式"); Exercise 4.4 for the massive analogue · the derivation from the transformation law written out here, parallel to [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-7|Theorem §C4.5.7]]*

^thm-c8b-9-5

> [!derivation]- Derivation
> **1. The law for the positive-frequency part.** $U^{-1}(R)\hat A^\mu(x)U(R) = R^\mu{}_\nu \hat A^\nu(R^{-1}x)$. Rotations commute with $\hat H$ ([[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-8|Theorem §C3.4.8]]: $[\hat J^i, \hat H] = 0$) and $R^{-1}x$ has the same time as $x$, so both sides have the same split into $e^{-iE t}$ and $e^{+iEt}$ parts: $U^{-1}\hat A^{\mu(+)}(x)U = R^\mu{}_\nu \hat A^{\nu(+)}(R^{-1}x)$.
>
> **2. Compare the modes.** Steps 1–3 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-7|Derivation §C4.5.7]] go through unchanged, with the four Feynman-gauge modes $\hat b_{\mathbf q,\sigma}$ and the basis $e(q, \sigma)$ of [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-9|Theorem §C4.8.9]] in place of the three $\hat a_{\mathbf q,\lambda}$, $\varepsilon(q, \lambda)$ (the substitution $\mathbf q' = R\mathbf q$ has Jacobian $1$ and keeps $E_{\mathbf q} = |\mathbf q|$; the comparison of coefficients uses [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-2|Theorem §CA.4.2]]). For every $\mathbf q$:
>
> $$
> \sum_\sigma e^\mu(q, \sigma)\,U^{-1}\hat b_{\mathbf q,\sigma}U = \sum_\sigma R^\mu{}_\nu\,e^\nu(R^{-1}q, \sigma)\,\hat b_{R^{-1}\mathbf q,\sigma} .
> $$
>
> The difference from the massive case appears in the projection (step 4): the basis now contains $n$ and $e(q, 3)$, which are not transverse.
>
> **3. A rotation about the momentum.** Take $\mathbf q = \mathbf p$ and $R$ the rotation by $\theta$ about $\hat{\mathbf p}$: $R^{-1}\mathbf p = \mathbf p$, $Rn = n$, $R(0, \hat{\mathbf p}) = (0, \hat{\mathbf p})$, and, because $(\mathbf e(p, 1), \mathbf e(p, 2), \hat{\mathbf p})$ is right handed ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-2|Theorem §C4.8.2]]), $\mathbf e_1 \mapsto \cos\theta\,\mathbf e_1 + \sin\theta\,\mathbf e_2$, $\mathbf e_2 \mapsto -\sin\theta\,\mathbf e_1 + \cos\theta\,\mathbf e_2$, so $\mathbf e_1 \pm i\mathbf e_2 \mapsto (\cos\theta \mp i\sin\theta)\mathbf e_1 + (\sin\theta \pm i\cos\theta)\mathbf e_2 = e^{\mp i\theta}(\mathbf e_1 \pm i\mathbf e_2)$: $R\varepsilon(p, \pm) = e^{\mp i\theta}\varepsilon(p, \pm)$ (as [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8|Theorem §C8b.3.8]], 1). With [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 2, the displayed identity of step 2 reads
>
> $$
> n\,U^{-1}\hat b_{\mathbf p,0}U + e(p, 3)\,U^{-1}\hat b_{\mathbf p,3}U + \sum_\pm\varepsilon(p, \pm)\,U^{-1}\hat a_{\mathbf p,\pm}U = n\,\hat b_{\mathbf p,0} + e(p, 3)\,\hat b_{\mathbf p,3} + \sum_\pm e^{\mp i\theta}\varepsilon(p, \pm)\,\hat a_{\mathbf p,\pm} .
> $$
>
> **4. Project.** Contract with $-\varepsilon^{\ast}_\mu(p, \pm)$: $\varepsilon^{\ast}(\lambda)\cdot\varepsilon(\lambda') = -\delta_{\lambda\lambda'}$ ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]]; the massless transverse vectors are the same), $\varepsilon^{\ast}(\pm)\cdot n = \varepsilon^{\ast}(\pm)\cdot e(p, 3) = 0$ (transversality). So $U^{-1}\hat a_{\mathbf p,\pm}U = e^{\mp i\theta}\hat a_{\mathbf p,\pm}$; contracting with $n$ and with $-e(p, 3)$ gives $U^{-1}\hat b_{\mathbf p,0}U = \hat b_{\mathbf p,0}$, $U^{-1}\hat b_{\mathbf p,3}U = \hat b_{\mathbf p,3}$.
>
> **5. The generator.** $U^{-1}\hat a\,U = e^{i\theta(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}}\hat a\,e^{-i\theta(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}}$; differentiate at $\theta = 0$: $i[(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat a_{\mathbf p,\pm}] = \mp i\,\hat a_{\mathbf p,\pm}$, i.e. $[(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat a_{\mathbf p,\pm}] = \mp \hat a_{\mathbf p,\pm}$; the adjoint ($\hat{\mathbf J}$ Hermitian) gives $[(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat a^\dagger_{\mathbf p,\pm}] = \pm \hat a^\dagger_{\mathbf p,\pm}$, and likewise $[(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat b^\dagger_{\mathbf p,0}] = [(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat b^\dagger_{\mathbf p,3}] = 0$.
>
> **6. On states.** $U(R)|0\rangle = |0\rangle$ for all $\theta$ gives $\hat{\mathbf J}|0\rangle = 0$, so $(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}|\mathbf p, \pm\rangle = \sqrt{2E_{\mathbf p}}\bigl([(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}, \hat a^\dagger_{\mathbf p,\pm}] + \hat a^\dagger_{\mathbf p,\pm}(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}\bigr)|0\rangle = \pm|\mathbf p, \pm\rangle$. Finally $\hat{\mathbf P}|\mathbf p, \pm\rangle = \mathbf p|\mathbf p, \pm\rangle$ ([[§C4.9 Energy, Momentum and the Indefinite Fock Space#^thm-c4-9-4|Theorem §C4.9.4]]), so $\hat{\mathbf J}\cdot\hat{\mathbf P}|\mathbf p, \pm\rangle = \sum_i\hat J^ip^i|\mathbf p, \pm\rangle = |\mathbf p|\,(\mathbf p/|\mathbf p|)\cdot\hat{\mathbf J}|\mathbf p, \pm\rangle$, and $\hat h|\mathbf p, \pm\rangle = \pm|\mathbf p, \pm\rangle$.
>
> ⚑ By-product: the helicity-zero states $|\mathbf p, 0\rangle$, $|\mathbf p, 3\rangle$ exist in the covariant space but are removed by the Gupta–Bleuler condition; the massive field's helicity-zero state ([[§C8b.9 Photon Helicity#^thm-c8b-9-2|Theorem §C8b.9.2]]) has no physical massless counterpart, as [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-6|Theorem §C8b.3.6]] and [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^rem-c4-6-2|§C4.6, Remark: Three polarizations become two]] require.
>
> **What the derivation shows**
> - The helicity of a photon is the eigenvalue of its polarization vector under rotations about the momentum; covariance of the field (which the Coulomb gauge would lose) is what transfers it to the states.
> - Assumed: a unitary (with respect to the indefinite product) implementation of rotations that leaves $|0\rangle$ invariant, as for the scalar ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-4|Theorem §C3.5.4]]).

^der-c8b-9-5

*Uses:* [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^pr-c3-5-1|Principle §C3.5.1]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^thm-c3-4-8|Theorem §C3.4.8]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-7|Derivation §C4.5.7]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-2|Theorem §CA.4.2]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-2|Theorem §C4.8.2]], [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], [[§C4.9 Energy, Momentum and the Indefinite Fock Space#^thm-c4-9-4|Theorem §C4.9.4]], [[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]

> [!theorem] Theorem §C8b.9.6: Energy and Momentum of Physical States in Helicity Form
> For every physical $|\Psi\rangle$,
>
> $$
> \langle\Psi|\hat H|\Psi\rangle = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\sum_{\lambda = \pm}\langle\Psi|\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda}|\Psi\rangle + E_0^{(\gamma)}\langle\Psi|\Psi\rangle, \qquad \langle\Psi|\hat{\mathbf P}|\Psi\rangle = \int\frac{d^3p}{(2\pi)^3}\mathbf p\sum_{\lambda = \pm}\langle\Psi|\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda}|\Psi\rangle .
> $$
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field, physical subspace only; $\hat H$ unordered, as in [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-5|Theorem §C4.10.5]].
>
> *Source: Yu §4.4.4, eqs. (4.279)–(4.280) · the user's pre-course notes, §4.4*

^thm-c8b-9-6

> [!derivation]- Derivation
> **1.** Insert [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 3, into [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-5|Theorem §C4.10.5]].
>
> **What the derivation shows**
> - On physical states the photon field is two massless bosons per momentum, counted by $\hat a^\dagger_\lambda \hat a_\lambda$; with normal ordering the constant disappears.

^der-c8b-9-6

*Uses:* [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-5|Theorem §C4.10.5]], [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]]

*Procedure:* [[P1 Canonical Quantization#^p1-8|P1, steps 8–9]]

## The Noether spin of photons

[[§C8b.9 Photon Helicity#^thm-c8b-9-5|Theorem §C8b.9.5]] obtained the photon's helicity from the covariance law. The Noether spin of the quantized Lagrangian $\mathcal L_2$ is $\mathbf S_2 = -\int d^3x\,\partial_t\mathbf A\times\mathbf A$ ([[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-7|Theorem §C4.7.7]]); on transverse fields it is the Maxwell spin $\int\mathbf E\times\mathbf A$ of [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-5|Theorem §C4.1.5]]. Its mode form gives the helicity directly, and shows where the gauge dependence of the classical spin ([[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-6|Theorem §C4.7.6]]) goes.

> [!theorem] ★ Theorem §C8b.9.7: The Spin of Transverse Photons
> Let $\hat{\mathbf A}_\perp$ be the physical part of the field, the $\lambda = \pm$ terms of [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 2 (so $\hat A^0_\perp = 0$), and $\hat{\mathbf E}_\perp = -\partial_t\hat{\mathbf A}_\perp$; $\hat{\mathbf p} = \mathbf p/|\mathbf p|$ is the unit vector, a c-number. Then, in the order written,
>
> $$
> \hat{\mathbf S}_\perp \equiv \int d^3x\;\hat{\mathbf E}_\perp\times\hat{\mathbf A}_\perp = \sum_{\lambda = \pm}\int\frac{d^3p}{(2\pi)^3}\;\lambda\,\hat{\mathbf p}\;\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda} :
> $$
>
> no number-changing terms (so $[\hat H, \hat{\mathbf S}_\perp] = 0$: the spin of transverse photons is conserved by itself) and no constant (the zero-point spins of the two helicities cancel mode by mode). In the Coulomb gauge, where $\hat{\mathbf A} = \hat{\mathbf A}_\perp$ and $\hat A^0 = 0$ for the free field ([[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^rem-c4-10-2|Remark: Covariant or Coulomb quantization]]), $\hat{\mathbf S}_\perp$ is the whole Noether spin.
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field; an operator identity for the transverse part $\hat{\mathbf A}_\perp$ (any state of the full space), in the order written; no covariance law used.
>
> *Source: derived here (Yu §4.4.4 and the user's pre-course notes, §4.4 ("Physical helicity states"), state the helicity eigenvalues without the Noether charge)*

^thm-c8b-9-7

> [!derivation]- Derivation
> **1. The coefficients.** By [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 2, $\hat{\mathbf A}_\perp = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E}}\sum_{\lambda = \pm}\bigl(\boldsymbol\varepsilon(p, \lambda)\hat a_{\mathbf p,\lambda}e^{-ip\cdot x} + \boldsymbol\varepsilon^{\ast}(p, \lambda)\hat a^\dagger_{\mathbf p,\lambda}e^{ip\cdot x}\bigr)$, $E = |\mathbf p|$; the helicity vectors have $\varepsilon^0(p, \pm) = 0$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]]). $\partial_t$ brings down $-iE$ on $e^{-ip\cdot x}$ and $+iE$ on $e^{ip\cdot x}$, so $\hat{\mathbf E}_\perp = -\partial_t\hat{\mathbf A}_\perp$ has coefficients $iE\boldsymbol\varepsilon$ on $\hat a$ and $-iE\boldsymbol\varepsilon^{\ast}$ on $\hat a^\dagger$ (the Proca $\hat{\mathbf W}$ with $\varepsilon^0 = 0$).
>
> **2. Substitute and integrate.** As in steps 1–2 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-9|Derivation §C4.5.9]] with $\hat{\mathbf W} \to E\boldsymbol\varepsilon$ (same deltas, same factor $\frac{1}{2E}$; [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]]):
>
> $$
> \hat{\mathbf S}_\perp = \int\frac{d^3p}{(2\pi)^3}\frac12\sum_{\lambda\lambda'}\Bigl(i\boldsymbol\varepsilon(p, \lambda)\times\boldsymbol\varepsilon^*(p, \lambda')\,\hat a_{\mathbf p,\lambda}\hat a^\dagger_{\mathbf p,\lambda'} - i\boldsymbol\varepsilon^*(p, \lambda)\times\boldsymbol\varepsilon(p, \lambda')\,\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda'} + i\boldsymbol\varepsilon(p, \lambda)\times\boldsymbol\varepsilon(-p, \lambda')\,\hat a_{\mathbf p,\lambda}\hat a_{-\mathbf p,\lambda'}e^{-2iEt} + \text{h.c.}\Bigr) .
> $$
>
> **3. The cross products of helicity vectors.** With the right-handed triad $(\mathbf e_1, \mathbf e_2, \hat{\mathbf p})$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-2|Theorem §C4.8.2]]) and $\boldsymbol\varepsilon(\pm) = (\mathbf e_1 \pm i\mathbf e_2)/\sqrt2$: $\boldsymbol\varepsilon(\pm)\times\boldsymbol\varepsilon^{\ast}(\pm) = \frac12(\mathbf e_1 \pm i\mathbf e_2)\times(\mathbf e_1 \mp i\mathbf e_2) = \frac12(\mp i\,\mathbf e_1\times\mathbf e_2 \pm i\,\mathbf e_2\times\mathbf e_1) = \mp i\,\hat{\mathbf p}$; and $\boldsymbol\varepsilon(\pm)\times\boldsymbol\varepsilon^{\ast}(\mp) = \boldsymbol\varepsilon(\pm)\times\boldsymbol\varepsilon(\pm) = 0$. So $i\boldsymbol\varepsilon(\lambda)\times\boldsymbol\varepsilon^{\ast}(\lambda') = \lambda\,\delta_{\lambda\lambda'}\,\hat{\mathbf p}$, real; its complex conjugate is $-i\boldsymbol\varepsilon^{\ast}(\lambda)\times\boldsymbol\varepsilon(\lambda') = \lambda\,\delta_{\lambda\lambda'}\,\hat{\mathbf p}$. (Phases of $\boldsymbol\varepsilon$ cancel in $\boldsymbol\varepsilon\times\boldsymbol\varepsilon^{\ast}$.)
>
> **4. The pair terms vanish.** Call the $\hat a\hat a$ term $\hat{\mathbf T}$. Substitute $\mathbf p \to -\mathbf p$ (Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$; [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], 1), rename $\lambda \leftrightarrow \lambda'$ and commute the annihilators ([[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 1): the coefficient becomes $i\boldsymbol\varepsilon(-p, \lambda')\times\boldsymbol\varepsilon(p, \lambda) = -i\boldsymbol\varepsilon(p, \lambda)\times\boldsymbol\varepsilon(-p, \lambda')$, so $\hat{\mathbf T} = -\hat{\mathbf T} = 0$, and its adjoint with it. Here, unlike the Proca case ([[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-10|Derivation §C4.5.10]], step 3), there is no $\varepsilon^0$ term to survive.
>
> **5. Reorder.** By step 3 the middle terms are $\sum_\lambda\frac{\lambda\hat{\mathbf p}}{2}\bigl(\hat a_{\mathbf p,\lambda}\hat a^\dagger_{\mathbf p,\lambda} + \hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda}\bigr)$, and $\hat a_{\mathbf p,\lambda}\hat a^\dagger_{\mathbf p,\lambda} = \hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda} + (2\pi)^3\delta^3(\mathbf 0)$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 1). The constant is $(2\pi)^3\delta^3(\mathbf 0)\int\frac{d^3p}{(2\pi)^3}\frac{\hat{\mathbf p}}{2}\sum_{\lambda = \pm}\lambda$, and $\sum_{\lambda = \pm}\lambda = 1 - 1 = 0$ for each $\mathbf p$. ⚑ By-product: no zero-point spin, by helicity balance, before any integral (the integrand $\hat{\mathbf p}$ is also odd, a second reason).
>
> **6. Conservation.** Each term is $\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda}$ at one momentum; with $[\hat H, \hat a^\dagger_{\mathbf p,\lambda}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p,\lambda}$ (from [[§C4.9 Energy, Momentum and the Indefinite Fock Space#^thm-c4-9-4|Theorem §C4.9.4]] for $\hat b_1$, $\hat b_2$ and [[§C8b.9 Photon Helicity#^def-c8b-9-1|Def. §C8b.9.1]]) and its adjoint, $[\hat H, \hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda}] = (E_{\mathbf p} - E_{\mathbf p})\hat a^\dagger \hat a = 0$.
>
> **7. Coulomb gauge.** There the free field is $\hat{\mathbf A}_\perp$ alone with $\hat A^0 = 0$ ([[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-4|EM Theorem §C1.4.4]]), $\hat{\mathbf E} = -\partial_t\hat{\mathbf A}_\perp$, and $\int\hat{\mathbf E}\times\hat{\mathbf A}$ is the integral just computed.
>
> **What the derivation shows**
> - Each transverse photon carries spin $\lambda\hat{\mathbf p}$, exactly, as an operator identity: the circular polarization vectors diagonalize the spin, and the two helicities enter with opposite signs.
> - Contrast with the Proca field: there the pair terms survive through $\varepsilon^0$, i.e. through $\hat A^0$ ([[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-10|Theorem §C4.5.10]]); transverse photons have no $\hat A^0$, and their spin is conserved by itself, as $dS^{jk}/dt = \int(T^{kj} - T^{jk})$ ([[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-6|Theorem §C4.1.6]]) then vanishes.
> - Used next: the Noether spin of the covariant field ([[§C8b.9 Photon Helicity#^thm-c8b-9-8|Theorem §C8b.9.8]]).

^der-c8b-9-7

*Uses:* [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-2|Theorem §C4.8.2]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-9|Derivation §C4.5.9]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], [[§C4.9 Energy, Momentum and the Indefinite Fock Space#^thm-c4-9-4|Theorem §C4.9.4]], [[§C8b.9 Photon Helicity#^def-c8b-9-1|Def. §C8b.9.1]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-4|EM Theorem §C1.4.4]]

> [!theorem] ★ Theorem §C8b.9.8: Photon Helicity from the Noether Spin
> The Noether spin of the quantized Feynman-gauge field ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; $\hat{\mathbf S}_2$ of [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-7|Theorem §C4.7.7]]) is, in the order written,
>
> $$
> \hat{\mathbf S}_2 = -\int d^3x\;\partial_t\hat{\mathbf A}\times\hat{\mathbf A} = \sum_{\lambda = \pm}\int\frac{d^3p}{(2\pi)^3}\;\lambda\Bigl[\hat{\mathbf p}\;\hat a^\dagger_{\mathbf p,\lambda}\hat a_{\mathbf p,\lambda} - \boldsymbol\varepsilon^*(p, \lambda)\,\hat a^\dagger_{\mathbf p,\lambda}\hat b_{\mathbf p,3} - \boldsymbol\varepsilon(p, \lambda)\,\hat b^\dagger_{\mathbf p,3}\hat a_{\mathbf p,\lambda}\Bigr] ,
> $$
>
> with the helicity operators of [[§C8b.9 Photon Helicity#^def-c8b-9-1|Def. §C8b.9.1]] and the longitudinal $\hat b_{\mathbf p,3}$ of [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-9|Theorem §C4.8.9]]. The timelike modes do not enter, and there are no pair terms and no constant. Hence
> 1. $\hat{\mathbf p}\cdot\hat{\mathbf S}_2\,|\mathbf p, \pm\rangle = \pm|\mathbf p, \pm\rangle$ exactly, for the fixed unit vector $\hat{\mathbf p}$: the helicities $\pm1$ of [[§C8b.9 Photon Helicity#^thm-c8b-9-5|Theorem §C8b.9.5]], now from the Noether charge;
> 2. between transverse states (annihilated by $\hat b_{\mathbf q,0}$ and $\hat b_{\mathbf q,3}$) $\hat{\mathbf S}_2$ has the matrix elements of $\hat{\mathbf S}_\perp$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-7|Theorem §C8b.9.7]]).
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field; the mode form an operator identity on the full indefinite-metric space; item 1 on the one-photon states $|\mathbf p, \pm\rangle$, item 2 between transverse states.
>
> *Source: derived here*

^thm-c8b-9-8

> [!derivation]- Derivation
> **1. Only spatial components enter.** $\hat{\mathbf S}_2$ contains $\hat{\mathbf A}$ only. The spatial parts of the basis are $\mathbf e(p, 0) = 0$, $\mathbf e(p, 3) = \hat{\mathbf p}$ and the transverse $\mathbf e(p, 1)$, $\mathbf e(p, 2)$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]]). With [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 2, $\hat{\mathbf A} = \hat{\mathbf A}_\perp + \hat{\mathbf A}_\parallel$, $\hat{\mathbf A}_\parallel = \int\frac{d^3p}{(2\pi)^3}\frac{\hat{\mathbf p}}{\sqrt{2E}}\bigl(\hat b_{\mathbf p,3}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p,3}e^{ip\cdot x}\bigr)$: $\hat b_{\mathbf p,0}$ drops out because the timelike vector has no spatial part.
>
> **2. Four pieces.** $\hat{\mathbf S}_2 = -\int(\partial_t\hat{\mathbf A}_\perp + \partial_t\hat{\mathbf A}_\parallel)\times(\hat{\mathbf A}_\perp + \hat{\mathbf A}_\parallel)$. The piece $-\int\partial_t\hat{\mathbf A}_\perp\times\hat{\mathbf A}_\perp$ is $\hat{\mathbf S}_\perp$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-7|Theorem §C8b.9.7]]; $\hat{\mathbf E}_\perp = -\partial_t\hat{\mathbf A}_\perp$).
>
> **3. Longitudinal with longitudinal.** In $-\int\partial_t\hat{\mathbf A}_\parallel\times\hat{\mathbf A}_\parallel$ every term, after the $d^3x$ integral, has the coefficient vectors at $\mathbf q = \pm\mathbf p$: $\hat{\mathbf p}\times(\pm\hat{\mathbf p}) = 0$. The piece vanishes identically, and with it every $\hat b^\dagger_3\hat b_3$ term and its reordering constant.
>
> **4. Mixed pieces, number-conserving terms.** $\partial_t\hat{\mathbf A}_\perp$ has coefficients $-iE\boldsymbol\varepsilon$ on $\hat a$, $+iE\boldsymbol\varepsilon^{\ast}$ on $\hat a^\dagger$; $\partial_t\hat{\mathbf A}_\parallel$ has $-iE\hat{\mathbf p}$ on $\hat b_3$, $+iE\hat{\mathbf p}$ on $\hat b^\dagger_3$. After $d^3x$ and the delta ($\mathbf q = \mathbf p$, factor $\frac{1}{2E}$, as in step 2 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-9|Derivation §C4.5.9]]):
> - $-\partial_t\hat{\mathbf A}_\perp(\hat a^\dagger)\times\hat{\mathbf A}_\parallel(\hat b_3)$: $-\frac{1}{2E}(iE\boldsymbol\varepsilon^*)\times\hat{\mathbf p} = -\frac i2\boldsymbol\varepsilon^*\times\hat{\mathbf p}$ on $\hat a^\dagger_{\mathbf p,\lambda}\hat b_{\mathbf p,3}$;
> - $-\partial_t\hat{\mathbf A}_\parallel(\hat b_3)\times\hat{\mathbf A}_\perp(\hat a^\dagger)$: $-\frac{1}{2E}(-iE\hat{\mathbf p})\times\boldsymbol\varepsilon^* = \frac i2\hat{\mathbf p}\times\boldsymbol\varepsilon^* = -\frac i2\boldsymbol\varepsilon^*\times\hat{\mathbf p}$ on $\hat b_{\mathbf p,3}\hat a^\dagger_{\mathbf p,\lambda} = \hat a^\dagger_{\mathbf p,\lambda}\hat b_{\mathbf p,3}$ ($\hat a$ and $\hat b_3$ commute, [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], 1).
>
> Total $-i\,\boldsymbol\varepsilon^*(p, \lambda)\times\hat{\mathbf p}$. Since $\hat{\mathbf p}\times\boldsymbol\varepsilon^*(\pm) = \pm i\boldsymbol\varepsilon^*(\pm)$ (conjugate of $\hat{\mathbf p}\times\boldsymbol\varepsilon(\pm) = \mp i\boldsymbol\varepsilon(\pm)$, [[§C4.1 The Vector Field and Its Lorentz Transformation#^der-c4-1-1|Derivation §C4.1.1]], step 5), $\boldsymbol\varepsilon^*(\pm)\times\hat{\mathbf p} = \mp i\boldsymbol\varepsilon^*(\pm)$ and $-i(\mp i) = \mp1$: the coefficient is $-\lambda\boldsymbol\varepsilon^*(p, \lambda)$. The $\hat b^\dagger_3\hat a$ terms are the adjoint ones, coefficient $-\lambda\boldsymbol\varepsilon(p, \lambda)$. No reordering is needed, so no constant arises.
>
> **5. Mixed pieces, pair terms.** For $\hat a^\dagger_{\mathbf p,\lambda}\hat b^\dagger_{-\mathbf p,3}$ (delta $\mathbf q = -\mathbf p$; $\mathbf e(-p, 3) = -\hat{\mathbf p}$):
> - $-\partial_t\hat{\mathbf A}_\perp(\hat a^\dagger_{\mathbf p})\times\hat{\mathbf A}_\parallel(\hat b^\dagger_{-\mathbf p})$: $-\frac{1}{2E}(iE\boldsymbol\varepsilon^*)\times(-\hat{\mathbf p}) = \frac i2\boldsymbol\varepsilon^*\times\hat{\mathbf p}$;
> - $-\partial_t\hat{\mathbf A}_\parallel(\hat b^\dagger_{-\mathbf p})\times\hat{\mathbf A}_\perp(\hat a^\dagger_{\mathbf p})$: $-\frac{1}{2E}\bigl(iE(-\hat{\mathbf p})\bigr)\times\boldsymbol\varepsilon^* = \frac i2\hat{\mathbf p}\times\boldsymbol\varepsilon^* = -\frac i2\boldsymbol\varepsilon^*\times\hat{\mathbf p}$.
>
> They cancel; the $\hat a\hat b_3$ terms are their adjoints and cancel too. With step 3 and Theorem §C8b.9.7 (no pair terms in $\hat{\mathbf S}_\perp$), $\hat{\mathbf S}_2$ is number-conserving: the stated form.
>
> **6. Item 1.** $\hat{\mathbf S}_\perp|\mathbf p, \lambda\rangle = \lambda\hat{\mathbf p}|\mathbf p, \lambda\rangle$ (as in step 1 of [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-11|Derivation §C4.5.11]]); $\hat b_{\mathbf q,3}\hat a^\dagger_{\mathbf p,\lambda}|0\rangle = \hat a^\dagger_{\mathbf p,\lambda}\hat b_{\mathbf q,3}|0\rangle = 0$; and $\hat b^\dagger_{\mathbf q,3}\hat a_{\mathbf q,\lambda'}$ gives $-\lambda\boldsymbol\varepsilon(p, \lambda)\sqrt{2E}\,\hat b^\dagger_{\mathbf p,3}|0\rangle = -\lambda\boldsymbol\varepsilon(p, \lambda)|\mathbf p, 3\rangle$. So $\hat{\mathbf S}_2|\mathbf p, \lambda\rangle = \lambda\hat{\mathbf p}|\mathbf p, \lambda\rangle - \lambda\boldsymbol\varepsilon(p, \lambda)|\mathbf p, 3\rangle$, and $\hat{\mathbf p}\cdot\boldsymbol\varepsilon(p, \lambda) = 0$ removes the second term from $\hat{\mathbf p}\cdot\hat{\mathbf S}_2$.
>
> **7. Item 2.** In every term of $\hat{\mathbf S}_2 - \hat{\mathbf S}_\perp$ the longitudinal operator can be put on the outside ($\hat a$, $\hat b_3$ commute): $\hat b_{\mathbf p,3}$ on the right, where it annihilates a transverse ket, or $\hat b^\dagger_{\mathbf p,3}$ on the left, where $\langle\Psi'|\hat b^\dagger_{\mathbf p,3} = (\hat b_{\mathbf p,3}|\Psi'\rangle)^\dagger = 0$.
>
> **What the derivation shows**
> - $\hat{\mathbf S}_2$ is a gauge-fixed quantity, and it shows: it mixes transverse photons with longitudinal ones, $\hat{\mathbf S}_2|\mathbf p, \pm\rangle$ has a component $\mp\boldsymbol\varepsilon(p, \pm)|\mathbf p, 3\rangle$ outside the physical subspace, perpendicular to $\mathbf p$. Only the component along the momentum, the helicity, and matrix elements between transverse states are physical → [[§C8b.9 Photon Helicity#^thm-c8b-9-9|Theorem §C8b.9.9]].
> - The longitudinal–transverse terms are the quantum form of the term $-\int A^0\mathbf B$ and of the gauge dependence of [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-6|Theorem §C4.7.6]]; that the timelike $\hat b_0$ is absent is particular to $\mathcal L_2$ ([[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-7|Theorem §C4.7.7]]: the spin of $\mathcal L_1$ adds $\int \hat A^0\hat{\mathbf B}$, which contains $\hat b_0$).
> - ⚑ By-product: no zero-point spin and no pair creation, for all four polarizations together; the photon's Noether spin, unlike the Proca spin ([[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-10|Theorem §C4.5.10]]), annihilates the vacuum.

^der-c8b-9-8

*Uses:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]], [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-7|Theorem §C4.7.7]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]], [[§C8b.9 Photon Helicity#^thm-c8b-9-4|Theorem §C8b.9.4]], [[§C8b.9 Photon Helicity#^thm-c8b-9-7|Theorem §C8b.9.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-9|Derivation §C4.5.9]], [[§C4.1 The Vector Field and Its Lorentz Transformation#^der-c4-1-1|Derivation §C4.1.1]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^der-c4-5-11|Derivation §C4.5.11]]

> [!theorem] ★ Theorem §C8b.9.9: Null States Change the Transverse Spin, Not the Helicity
> Let $|\chi_{\mathbf p}\rangle \equiv \sqrt{2E_{\mathbf p}}\bigl(\hat b^\dagger_{\mathbf p,0} - \hat b^\dagger_{\mathbf p,3}\bigr)|0\rangle$, the one-photon null state of [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]]. Then
>
> $$
> \hat{\mathbf S}_2\,|\chi_{\mathbf p}\rangle = \sum_{\lambda = \pm}\lambda\,\boldsymbol\varepsilon^*(p, \lambda)\,|\mathbf p, \lambda\rangle, \qquad \hat{\mathbf p}\cdot\hat{\mathbf S}_2\,|\chi_{\mathbf p}\rangle = 0 .
> $$
>
> For the representatives $|\Psi_c\rangle = |\mathbf p, \lambda\rangle + c\,|\chi_{\mathbf p}\rangle$, $c \in \mathbb C$, of one physical one-photon state: $\langle\Psi_c|\Psi_c\rangle = \langle\mathbf p, \lambda|\mathbf p, \lambda\rangle$ and $\langle\Psi_c|\hat{\mathbf S}_2|\Psi_c\rangle = \bigl[\lambda\hat{\mathbf p} + 2\lambda\operatorname{Re}\bigl(c\,\boldsymbol\varepsilon^*(p, \lambda)\bigr)\bigr]\langle\mathbf p, \lambda|\mathbf p, \lambda\rangle$: the component along $\hat{\mathbf p}$ is the helicity for every $c$, the transverse components depend on the representative.
>
> *Model:* [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^mod-c4-8-4|Model §C4.8.4]]; *applies:* free field, one-photon states on $|0\rangle$ in the physical subspace (representatives modulo null states); exact.
>
> *Source: derived here, from Yu's algebra (4.232) and the null states of PS §9.4, p. 298*

^thm-c8b-9-9

> [!derivation]- Derivation
> **1. Which terms act.** In [[§C8b.9 Photon Helicity#^thm-c8b-9-8|Theorem §C8b.9.8]], $\hat a_{\mathbf q,\lambda}|\chi_{\mathbf p}\rangle = 0$ ($\hat a_\lambda$ commutes with $\hat b^\dagger_0$, $\hat b^\dagger_3$ and annihilates $|0\rangle$), which removes the $\hat a^\dagger \hat a$ and $\hat b^\dagger_3\hat a$ terms. The remaining term is $-\sum_\lambda\int\frac{d^3q}{(2\pi)^3}\lambda\boldsymbol\varepsilon^{\ast}(q, \lambda)\hat a^\dagger_{\mathbf q,\lambda}\hat b_{\mathbf q,3}$.
>
> **2. The longitudinal commutators.** $\hat b_{\mathbf q,3}(\hat b^\dagger_{\mathbf p,0} - \hat b^\dagger_{\mathbf p,3})|0\rangle = \bigl([\hat b_{\mathbf q,3}, \hat b^\dagger_{\mathbf p,0}] - [\hat b_{\mathbf q,3}, \hat b^\dagger_{\mathbf p,3}]\bigr)|0\rangle = \bigl(0 - (-g_{33})(2\pi)^3\delta^3(\mathbf q - \mathbf p)\bigr)|0\rangle = -(2\pi)^3\delta^3(\mathbf q - \mathbf p)|0\rangle$ ([[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-11|Theorem §C4.8.11]], $g_{30} = 0$, $g_{33} = -1$).
>
> **3. Assemble.** $\hat{\mathbf S}_2|\chi_{\mathbf p}\rangle = -\sum_\lambda\lambda\boldsymbol\varepsilon^{\ast}(p, \lambda)\sqrt{2E_{\mathbf p}}\hat a^\dagger_{\mathbf p,\lambda}\cdot(-1)|0\rangle = \sum_\lambda\lambda\boldsymbol\varepsilon^{\ast}(p, \lambda)|\mathbf p, \lambda\rangle$ (the delta removes the $\mathbf q$ integral). $\hat{\mathbf p}\cdot\boldsymbol\varepsilon^{\ast}(p, \lambda) = 0$ gives the second formula.
>
> **4. Norm.** $\langle\Psi_c|\Psi_c\rangle = \langle\mathbf p, \lambda|\mathbf p, \lambda\rangle + 2\operatorname{Re}\bigl(c\langle\mathbf p, \lambda|\chi_{\mathbf p}\rangle\bigr) + |c|^2\langle\chi_{\mathbf p}|\chi_{\mathbf p}\rangle$; the last two vanish ($\hat a$ commutes with $\hat b^\dagger_{0,3}$; $|\chi_{\mathbf p}\rangle$ has zero norm, [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]], step 1 of its derivation).
>
> **5. Expectation value.** Expand into four terms. $\langle\mathbf p, \lambda|\hat{\mathbf S}_2|\mathbf p, \lambda\rangle = \lambda\hat{\mathbf p}\langle\mathbf p, \lambda|\mathbf p, \lambda\rangle$ by step 6 of [[§C8b.9 Photon Helicity#^der-c8b-9-8|Derivation §C8b.9.8]] (the $|\mathbf p, 3\rangle$ component is orthogonal to $|\mathbf p, \lambda\rangle$). $\langle\mathbf p, \lambda|\hat{\mathbf S}_2|\chi_{\mathbf p}\rangle = \lambda\boldsymbol\varepsilon^{\ast}(p, \lambda)\langle\mathbf p, \lambda|\mathbf p, \lambda\rangle$ by step 3 (the other helicity is orthogonal). $\langle\chi_{\mathbf p}|\hat{\mathbf S}_2|\mathbf p, \lambda\rangle$ is its complex conjugate, since $\hat{\mathbf S}_2$ is self-adjoint for the indefinite product (each term of Theorem §C8b.9.8 appears with its adjoint); directly: $\langle\chi_{\mathbf p}|\bigl(\lambda\hat{\mathbf p}|\mathbf p, \lambda\rangle - \lambda\boldsymbol\varepsilon|\mathbf p, 3\rangle\bigr) = -\lambda\boldsymbol\varepsilon\,\langle\chi_{\mathbf p}|\mathbf p, 3\rangle = \lambda\boldsymbol\varepsilon(p, \lambda)\langle\mathbf p, \lambda|\mathbf p, \lambda\rangle$, with $\langle\chi_{\mathbf p}|\mathbf p, 3\rangle = 2E\,\langle0|(\hat b_{\mathbf p,0} - \hat b_{\mathbf p,3})\hat b^\dagger_{\mathbf p,3}|0\rangle = -2E(2\pi)^3\delta^3(\mathbf 0)$. $\langle\chi_{\mathbf p}|\hat{\mathbf S}_2|\chi_{\mathbf p}\rangle = \sum_{\lambda'}\lambda'\boldsymbol\varepsilon^{\ast}\langle\chi_{\mathbf p}|\mathbf p, \lambda'\rangle = 0$. Sum: $\bigl[\lambda\hat{\mathbf p} + \lambda(c\boldsymbol\varepsilon^{\ast} + \bar c\boldsymbol\varepsilon)\bigr]\langle\mathbf p, \lambda|\mathbf p, \lambda\rangle$, and $c\boldsymbol\varepsilon^{\ast} + \bar c\boldsymbol\varepsilon = 2\operatorname{Re}(c\boldsymbol\varepsilon^{\ast})$.
>
> **6. Sense.** All brackets carry the same $\langle\mathbf p, \lambda|\mathbf p, \lambda\rangle = 2E(2\pi)^3\delta^3(\mathbf 0)$; read as the ratio, or for wave packets $\int g(\mathbf p)\dots$ narrow in momentum, where the same computation holds with $\int|g|^2$ in place of the delta ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]).
>
> **What the derivation shows**
> - ⚑ By-product: the classical gauge dependence of the spin ([[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-6|Theorem §C4.7.6]]) survives quantization as a dependence on the null-state representative ([[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^rem-c4-10-1|Remark: Physical states up to null states, and gauge invariance]]): a residual gauge transformation of the mean field ([[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]], 4) shifts the spin across the momentum. The helicity is unaffected, as the physical quantum number must be.
> - Physical spin observables of photons are therefore the helicity and the total $\hat{\mathbf J}$; the transverse spin of a single photon is not one of them.

^der-c8b-9-9

*Uses:* [[§C8b.9 Photon Helicity#^thm-c8b-9-8|Theorem §C8b.9.8]], [[§C8b.9 Photon Helicity#^der-c8b-9-8|Derivation §C8b.9.8]], [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^thm-c4-8-11|Theorem §C4.8.11]], [[§C4.10 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-10-6|Theorem §C4.10.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]]

## The linear basis and the helicity basis compared

A polarization vector does for the vector field what the two-spinor does for the Dirac field: it carries the spin label of the plane wave. It also comes in two bases, a real one fixed by two directions in space and the helicity basis. This part is the vector counterpart of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-5|Theorem §C8b.5.5]].

> [!theorem] Theorem §C8b.9.10: The Helicity Vectors Are the Linear Vectors in Circular Combination
> Let $\mathbf e_1 \equiv \mathbf e(p, 1)$ and $\mathbf e_2 \equiv \mathbf e(p, 2)$ be the real transverse unit vectors of [[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]], the two **linear polarizations**, with $(\mathbf e_1, \mathbf e_2, \hat{\mathbf p})$ a right-handed orthonormal triad ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]]), and $\boldsymbol\varepsilon(p, \pm) = (\mathbf e_1 \pm i\mathbf e_2)/\sqrt2$ the helicity vectors (all with time component zero).
> 1. **Change of basis.** $\boldsymbol\varepsilon(p, \lambda) = \sum_{r=1,2}V_{r\lambda}\,\mathbf e_r$ with the unitary matrix $V = \frac1{\sqrt2}\begin{pmatrix}1 & 1\\ i & -i\end{pmatrix}$, the same for every momentum. Inverted: $\mathbf e_1 = \bigl(\boldsymbol\varepsilon(p, +) + \boldsymbol\varepsilon(p, -)\bigr)/\sqrt2$ and $\mathbf e_2 = -i\bigl(\boldsymbol\varepsilon(p, +) - \boldsymbol\varepsilon(p, -)\bigr)/\sqrt2$.
> 2. **Rotation about the momentum.** A rotation by $\alpha$ about $\hat{\mathbf p}$ turns the linear vectors into each other, $\mathbf e_1 \to \cos\alpha\,\mathbf e_1 + \sin\alpha\,\mathbf e_2$ and $\mathbf e_2 \to -\sin\alpha\,\mathbf e_1 + \cos\alpha\,\mathbf e_2$, and multiplies each helicity vector by a phase, $\boldsymbol\varepsilon(p, \pm) \to e^{\mp i\alpha}\boldsymbol\varepsilon(p, \pm)$. So $\boldsymbol\varepsilon(p, \pm)$ are the eigenvectors of $\hat{\mathbf p}\cdot\boldsymbol{\mathcal J}$ with eigenvalues $\pm1$, and a linear vector is an eigenvector of no helicity: it is an equal mixture, $|\boldsymbol\varepsilon(p, \pm)^{\ast}\cdot\mathbf e_r|^2 = \frac12$.
> 3. **Complex conjugates.** $\boldsymbol\varepsilon(p, -) = \boldsymbol\varepsilon(p, +)^{\ast}$: the helicity vectors are complex and conjugate to each other, the linear ones are real.
> 4. **Amplitudes.** An amplitude with one incoming photon is linear in its polarization vector ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]]), so $\mathcal M_\lambda = \sum_rV_{r\lambda}\mathcal M_r$ and $\sum_{\lambda=\pm}|\mathcal M_\lambda|^2 = \sum_{r=1,2}|\mathcal M_r|^2$; for an outgoing photon, which enters through $\varepsilon^{\ast}$, the same holds with $V^{\ast}$. A sum over the two physical polarizations does not depend on the basis; an amplitude for one chosen polarization does.
> 5. **No direction makes the bases agree.** For a spinor the two bases coincide when the momentum is along $+\hat{\mathbf z}$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-5|Theorem §C8b.5.5]], part 5). Here they never do: $V$ does not depend on $\mathbf p$ and is not the identity.
>
> *Course form (Lecture 18):* for $\mathbf p \parallel \hat{\mathbf z}$, $\mathbf e_1 = \hat{\mathbf x}$, $\mathbf e_2 = \hat{\mathbf y}$ and $\epsilon^\mu = (0, 1, \pm i, 0)/\sqrt2$, the right- and left-handed polarization vectors of [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]]; the linear ones are the course's $r = 1, 2$ ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-1|Def. §C8a.3.1]]).
>
> *Model:* the transverse polarization vectors of a vector field at momentum $\mathbf p \ne 0$: the photon's physical polarizations (Def. §C8a.3.2) and the transverse two of the massive field (★, [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^mod-c4-4-1|Model §C4.4.1]]); *applies:* every $m \ge 0$; with Yu's explicit $\mathbf e(p, 1)$, $\mathbf e(p, 2)$ for $\mathbf p$ not along $\pm\hat{\mathbf z}$, and with any right-handed transverse pair otherwise.
>
> *Source: PS §4.8, p. 124 (transverse polarization vectors; for $\mathbf p$ along $z$ the right- and left-handed vectors $(0, 1, \pm i, 0)/\sqrt2$) · Yu §4.3.1 (the vectors $e(p, 1)$, $e(p, 2)$ and their circular combinations) · PHY 513 Lecture 18, slide 9 · the comparison written for the user's question of 2026-11-20 and checked numerically (`qft-C/tools/c8b-general/verify_general.py`)*

^thm-c8b-9-10

> [!derivation]- Derivation
> **Step 1** (change of basis). Reading off the definition, $\boldsymbol\varepsilon(p, +) = \frac1{\sqrt2}\mathbf e_1 + \frac i{\sqrt2}\mathbf e_2$ and $\boldsymbol\varepsilon(p, -) = \frac1{\sqrt2}\mathbf e_1 - \frac i{\sqrt2}\mathbf e_2$: the columns of $V$. The columns are orthonormal, $\frac12(1\cdot1 + (-i)(i)) = 1$ for each and $\frac12(1\cdot1 + (-i)(-i)) = 0$ between them (the first factor conjugated), so $V$ is unitary. Adding and subtracting the two lines gives $\mathbf e_1$ and $\mathbf e_2$. Part 1.
>
> **Step 2** (rotation about $\hat{\mathbf p}$). Since $(\mathbf e_1, \mathbf e_2, \hat{\mathbf p})$ is right-handed, a rotation by $\alpha$ about $\hat{\mathbf p}$ acts on the pair $(\mathbf e_1, \mathbf e_2)$ as a rotation about $\hat{\mathbf z}$ acts on $(\hat{\mathbf x}, \hat{\mathbf y})$: the two rules of part 2. Then
>
> $$
> \boldsymbol\varepsilon(p, +) \to \frac{(\cos\alpha\,\mathbf e_1 + \sin\alpha\,\mathbf e_2) + i(-\sin\alpha\,\mathbf e_1 + \cos\alpha\,\mathbf e_2)}{\sqrt2} = \frac{(\cos\alpha - i\sin\alpha)\,\mathbf e_1 + (\sin\alpha + i\cos\alpha)\,\mathbf e_2}{\sqrt2} = e^{-i\alpha}\,\frac{\mathbf e_1 + i\mathbf e_2}{\sqrt2},
> $$
>
> using $\sin\alpha + i\cos\alpha = i(\cos\alpha - i\sin\alpha) = i\,e^{-i\alpha}$. The complex conjugate of this line is the rule for $\boldsymbol\varepsilon(p, -)$, with $e^{+i\alpha}$. The rotation is $e^{-i\alpha\,\hat{\mathbf p}\cdot\boldsymbol{\mathcal J}}$, so the phases $e^{\mp i\alpha}$ mean $\hat{\mathbf p}\cdot\boldsymbol{\mathcal J} = \pm1$ on $\boldsymbol\varepsilon(p, \pm)$ (for the massive field this is [[§C8b.9 Photon Helicity#^thm-c8b-9-1|★ Theorem §C8b.9.1]]). The overlaps: $\boldsymbol\varepsilon(p, \pm)^{\ast}\cdot\mathbf e_1 = \frac1{\sqrt2}$ and $\boldsymbol\varepsilon(p, \pm)^{\ast}\cdot\mathbf e_2 = \mp\frac i{\sqrt2}$, each of squared modulus $\frac12$. Part 2.
>
> **Step 3** (conjugates). $\mathbf e_1$, $\mathbf e_2$ are real, so $\bigl((\mathbf e_1 + i\mathbf e_2)/\sqrt2\bigr)^{\ast} = (\mathbf e_1 - i\mathbf e_2)/\sqrt2$. Part 3.
>
> **Step 4** (amplitudes). Linearity gives $\mathcal M_\lambda = \sum_rV_{r\lambda}\mathcal M_r$, and unitarity gives $\sum_\lambda|\mathcal M_\lambda|^2 = \sum_{r, r'}\bigl(\sum_\lambda V_{r\lambda}V^{\ast}_{r'\lambda}\bigr)\mathcal M_r\mathcal M_{r'}^{\ast} = \sum_r|\mathcal M_r|^2$, the same step as in [[§C8b.5 Helicity Spinors and the Massless Limit#^der-c8b-5-5|Derivation §C8b.5.5]], Step 7. Part 4. Part 5 is read off $V$.
>
> **What the derivation shows**
> - The spinor matrix $U(\hat{\mathbf p})$ of Theorem §C8b.5.5 depends on the direction, because the fixed-axis basis ignores the momentum. The linear vectors already follow the momentum (they are transverse to it), so what is left is a fixed change from real to circular combinations.
> - The phase under a rotation by $\alpha$ about the momentum is $e^{\mp i\alpha}$ here and $e^{\mp i\alpha/2}$ for $u_\pm$: helicity $\pm1$ against $\pm\frac12$.

^der-c8b-9-10

*Uses:* [[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]], [[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-6|Theorem §C4.3.6]], [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-2|Def. §C8a.3.2]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]], [[§C8b.5 Helicity Spinors and the Massless Limit#^der-c8b-5-5|Derivation §C8b.5.5]]

> [!example] Example §C8b.9.1: A Photon along the Beam in Both Bases
> For $\mathbf p$ along $+\hat{\mathbf z}$ the linear polarizations are $\hat{\mathbf x}$ and $\hat{\mathbf y}$, and the helicity vectors are $\boldsymbol\varepsilon(\pm) = (\hat{\mathbf x} \pm i\hat{\mathbf y})/\sqrt2$, in four-vector form $(0, 1, \pm i, 0)/\sqrt2$.
> 1. The physical field of the wave is the real part: $\operatorname{Re}\bigl[(\hat{\mathbf x} + i\hat{\mathbf y})\,e^{-i\omega t}\bigr] = \hat{\mathbf x}\cos\omega t + \hat{\mathbf y}\sin\omega t$. For helicity $+1$ the field vector turns from $\hat{\mathbf x}$ towards $\hat{\mathbf y}$, counterclockwise about the direction of motion: the right-hand rule with the thumb along $\mathbf p$. For helicity $-1$ it turns the other way.
> 2. A linear polarization keeps its direction and only changes size: $\operatorname{Re}\bigl[\hat{\mathbf x}\,e^{-i\omega t}\bigr] = \hat{\mathbf x}\cos\omega t$. It is the sum of the two circular motions, $\hat{\mathbf x} = \bigl(\boldsymbol\varepsilon(+) + \boldsymbol\varepsilon(-)\bigr)/\sqrt2$.
> 3. In Lecture 20 the current of $e^-_Re^+_L$ along the beam is proportional to $(0, 1, i, 0)$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]): the helicity $+1$ vector, an equal mixture of the two linear polarizations.
>
> *Source: Theorem §C8b.9.10 applied to PS §4.8, p. 124 · PHY 513 Lecture 20, slide 28 · the time dependence written for the user's question of 2026-11-20*

^ex-c8b-9-1

![[ph-qft-c8b-9-a1.gif|640]]
*The field vector of a wave moving towards the viewer ($\mathbf p$ out of the page), for the three polarizations of [[§C8b.9 Photon Helicity#^ex-c8b-9-1|Example §C8b.9.1]]. Left: helicity $+1$, $(\hat{\mathbf x}\cos\omega t + \hat{\mathbf y}\sin\omega t)/\sqrt2$, turning counterclockwise, the right-hand rule about the motion. Middle: helicity $-1$, turning clockwise. Right: the two circular motions added tip to tail and divided by $\sqrt2$ (each arrow of length $\frac12$): the sum stays on the $x$ axis and is the linear polarization $\hat{\mathbf x}\cos\omega t$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-10|Theorem §C8b.9.10]], part 1). (Not from the sources; animation added, vault only.)*

## Spinor and vector side by side

> [!remark] Remark: Helicity and chirality for the spinor field and the vector field
> The same questions, asked of both fields:
>
> | | spinor field $\psi$ | vector field $A^\mu$ |
> |---|---|---|
> | the index carries | $(\frac12, 0)\oplus(0, \frac12)$ | $(\frac12, \frac12)$; its field strength $F^{\mu\nu}$ carries $(1, 0)\oplus(0, 1)$ |
> | chirality | the eigenvalue $\mp1$ of $\gamma^5$: $\psi_L$, $\psi_R$ ([[§C8b.4 Chirality#^thm-c8b-4-1\|Theorem §C8b.4.1]]) | none for $A^\mu$; for $F^{\mu\nu}$ the pair $\mathbf E - i\mathbf B$, $\mathbf E + i\mathbf B$ ([[§C8b.4 Chirality#^thm-c8b-4-4\|★ Theorem §C8b.4.4]]) |
> | what carries the spin label of a plane wave | the two-spinor $\xi$ inside $u(p)$, $v(p)$ | the polarization vector $\varepsilon^\mu(p)$ |
> | basis fixed in space | $\xi^1, \xi^2$: spin along $\pm\hat{\mathbf z}$ ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-3\|Def. §C5a.10.3]]) | $\mathbf e_1, \mathbf e_2$: linear polarizations ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5\|Def. §C4.3.5]]; course form [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^def-c8a-3-1\|Def. §C8a.3.1]]) |
> | helicity basis | $\xi_\pm(\hat{\mathbf p})$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1\|Theorem §C8b.5.1]]) | $\boldsymbol\varepsilon(p, \pm) = (\mathbf e_1 \pm i\mathbf e_2)/\sqrt2$ |
> | change of basis | the rotation $U(\hat{\mathbf p})$, different for each direction, the identity for $\mathbf p$ along $+\hat{\mathbf z}$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-5\|Theorem §C8b.5.5]]) | one fixed matrix $V$ for every momentum ([[§C8b.9 Photon Helicity#^thm-c8b-9-10\|Theorem §C8b.9.10]]) |
> | rotation by $\alpha$ about $\hat{\mathbf p}$ | $u_\pm \to e^{\mp i\alpha/2}u_\pm$ | $\boldsymbol\varepsilon(p, \pm) \to e^{\mp i\alpha}\boldsymbol\varepsilon(p, \pm)$ |
> | helicities for $m > 0$ | $\pm\frac12$, two states | $+1, 0, -1$, three states ([[§C8b.9 Photon Helicity#^thm-c8b-9-2\|★ Theorem §C8b.9.2]]) |
> | helicities for $m = 0$ | $\pm\frac12$, each the same in every frame | $\pm1$ only, no helicity $0$ ([[§C8b.9 Photon Helicity#^thm-c8b-9-5\|Theorem §C8b.9.5]]; [[§C8b.3 Massless Particles and Helicity#^law-c8b-3-4\|Law §C8b.3.4]]) |
> | what $m \to 0$ does to the rest | the other Weyl half of $u_\pm$ shrinks like $m/E$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4\|Theorem §C8b.5.4]]) | the longitudinal vector grows like $E/m$ and has no limit ([[§C4.3★ Massive Polarization Vectors and Plane Waves#^thm-c4-3-9\|Theorem §C4.3.9]]) |
> | helicity and chirality at $m = 0$ | helicity $\pm\frac12$ is chirality $\pm1$ of the spinor ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4\|Theorem §C8b.5.4]]) | helicity $\pm1$ goes with $\mathbf E \pm i\mathbf B$; the potential carries no such label ([[§C8b.4 Chirality#^thm-c8b-4-3\|★ Theorem §C8b.4.3]]) |
> | antiparticle | the spinor $v$ shows the opposite helicity ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2\|Theorem §C8b.6.2]]) | the photon is its own antiparticle; an outgoing photon enters through $\varepsilon^{\ast}$ |
> | is the field a true tensor or spinor? | yes | only up to a gauge shift $\varepsilon \to \varepsilon + c\,p$ ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-8\|Theorem §C8b.3.8]]; [[§C8b.4 Chirality#^rem-c8b-4-4\|§C8b.4, ★ Remark: Why photons of helicity ±1 do not contradict the rule]]) |
> | sum over the spin states | the same in every basis: $\sum_su^s\bar u^s = \slashed{p} + m$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7\|Theorem §C5a.12.7]]) | the same in every basis ([[§C8b.9 Photon Helicity#^thm-c8b-9-10\|Theorem §C8b.9.10]], part 4) |
> | at the QED vertex | chirality is kept along the fermion line ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4\|Theorem §C8b.6.4]]) | the current of $e^-_Re^+_L$ is the helicity $+1$ vector along the beam ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10\|Theorem §C8b.7.10]]) |
>
> Helicity means the same thing for both fields, the spin along the motion, and both have a helicity basis. Chirality does not carry over to the potential: a vector index has one type only. What replaces it is the split of the field strength, and the reason the potential can still describe helicity $\pm1$ is gauge invariance.
>
> *Source: the homes linked in each row · the table written for the user's question of 2026-11-20*

^rem-c8b-9-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — the plane-wave deltas of the $d^3x$ integrals when the spin is written in modes ([[§C8b.9 Photon Helicity#^thm-c8b-9-7|Theorem §C8b.9.7]]).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]] — the substitution $\mathbf p \to -\mathbf p$ (Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$) under which the pair terms of the transverse spin vanish.

> [!remark]- Connections
> - The photon's helicity $\pm1$ is the representation theory of the little group $ISO(2)$ realized on a field, given the experimental input [[§C8b.3 Massless Particles and Helicity#^law-c8b-3-4|Law §C8b.3.4]]; the photon spin promised in the Noether chapter is this helicity, obtained once from the covariance law and once from the Noether charge $\int\mathbf E\times\mathbf A$ — [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-6|Theorem §C8b.3.6]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]], [[§C8b.9 Photon Helicity#^thm-c8b-9-5|Theorem §C8b.9.5]], [[§C8b.9 Photon Helicity#^thm-c8b-9-8|Theorem §C8b.9.8]].
> - Only the helicity and the total $\mathbf J$ of light are gauge invariant: classically the spin–orbit split moves under gauge transformations, quantum mechanically the transverse spin moves with the null-state representative, while the helicity does not — [[§C4.7 The Feynman-Gauge Field꞉ Canonical Structure and Angular Momentum#^thm-c4-7-6|Theorem §C4.7.6]], [[§C8b.9 Photon Helicity#^thm-c8b-9-9|Theorem §C8b.9.9]], [[§C4.1 The Vector Field and Its Lorentz Transformation#^rem-c4-1-3|§C4.1, Remark: Spin hidden in the Poynting vector]].
> - Transverse photons have a conserved spin and no zero-point spin; the massive vector field's spin is not conserved alone, through its longitudinal mode — [[§C8b.9 Photon Helicity#^thm-c8b-9-7|Theorem §C8b.9.7]], [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-10|Theorem §C4.5.10]].
> - The vectors whose helicities are found here are defined with the massive polarization basis and its phase conventions, which stay in C4 — [[§C4.3★ Massive Polarization Vectors and Plane Waves#^def-c4-3-5|Def. §C4.3.5]], [[§C4.3★ Massive Polarization Vectors and Plane Waves#^cau-c4-3-1|§C4.3★, Caution: Phase conventions and the z-axis]], and the massless basis [[§C4.8 Covariant Quantization꞉ Modes and the Indefinite Mode Algebra#^def-c4-8-1|Def. §C4.8.1]]; the course writes the same field with a circular transverse pair — [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-1|Theorem §C8a.3.1]].
> - In Lecture 20 the current of $e^-_Re^+_L$ is $\propto(0, 1, i, 0)$, the polarization vector of a helicity $+1$ photon along the beam — [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^rem-c8b-7-4|§C8b.7, Remark: The spin-one part is rotated, the spin-zero part does nothing]].

