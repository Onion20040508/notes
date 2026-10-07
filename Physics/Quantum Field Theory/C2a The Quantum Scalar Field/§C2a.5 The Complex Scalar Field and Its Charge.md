---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2a.4 Particles and Relativistic Normalization]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2a.6 Coherent States and the Classical Field]] →

*Sources: the user's PHY 513 notes, Ch. 4 §§4.4–4.7 (complex-field paragraphs) and Ch. 3 §3.4 · PHY 513 Problem Set 3, Problem 2 (= Peskin & Schroeder, Problem 2.2(a)–(c)), with the course solution · Yu Zhao-Huan, 量子场论讲义, §2.4 · the user's pre-course notes, §3.4.*

What does a complex field have that a real one lacks? Two independent sets of oscillators, and a conserved charge that tells them apart. The classical field is recalled first, from its home in Chapter C1b. The construction is then [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] run again ([[P1 Canonical Quantization]]), with two changes: the momentum conjugate to $\phi$ is the velocity of $\phi^\dagger$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]), and the phase symmetry $\phi \to e^{i\alpha}\phi$ gives a charge whose Noether derivation is [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]. Quantum Mechanics previewed the result by combining two real fields in a box ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-7|QM Theorem §C13.1.7]]); here the complex field is quantized through its own canonical pairs, the charge is normalized as in Peskin–Schroeder, and its operator ordering turns out to be fixed by physics rather than convention. The result is the first appearance of antiparticles.

## The classical complex field, recalled

The classical field has its home in Chapter C1b; its boxes are shown as they stand there. The Lagrangian, defined in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]:

![[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7]]

Its momenta and Hamiltonian density, derived in [[§C1b.4 Hamiltonian Field Theory|§C1b.4]] with $\phi$ and $\phi^\ast$ as independent coordinates:

![[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3]]

The energy and the field momentum, [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]] (recalled in [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]) for the two fields, in field form:

![[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-8]]

The U(1) current is recalled where the charge is built ([[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]]). Quantization reads these as operators, written with a hat; the boxes recalled above are classical and stay unhatted, the hat marking the quantization step ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|§C2a.1, Caution: Eₚ, not ωₚ; π, not Π]]):

## The quantum model

> [!model] Model §C2a.5.1: The Free Complex Scalar Quantum Field
> A field $\hat\phi$ and its adjoint $\hat\phi^\dagger$, treated as independent canonical fields, with
>
> $$
> \mathcal L = \partial_\mu\phi^\dagger\,\partial^\mu\phi - m^2\phi^\dagger\phi, \qquad \pi = \frac{\partial\mathcal L}{\partial\dot\phi} = \dot\phi^\dagger \;\to\; \hat\pi = \dot{\hat\phi}^\dagger, \quad \hat\pi^\dagger = \dot{\hat\phi}, \qquad \hat H = \int d^3x\,\bigl(\hat\pi^\dagger\hat\pi + \nabla\hat\phi^\dagger\cdot\nabla\hat\phi + m^2\hat\phi^\dagger\hat\phi\bigr) ,
> $$
>
> quantized by [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]: $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = [\hat\phi^\dagger(\mathbf x), \hat\pi^\dagger(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, all other equal-time commutators zero, including $[\hat\phi, \hat\pi^\dagger]$ and $[\hat\phi, \hat\phi^\dagger]$.
>
> *Assumptions:* those of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]. With $\hat\phi = (\hat\phi_1 + i\hat\phi_2)/\sqrt2$, $\hat\pi = (\hat\pi_1 - i\hat\pi_2)/\sqrt2$ it is two real fields of the same mass $m$.
> *Source: the user's PHY 513 notes, Ch. 3 §3.4 ("The complex scalar, worked") and Ch. 4 §4.4, eq. (canonicalcomplex) · PHY 513 Problem Set 3, Problem 2(a1), course solution · Yu §2.4, eqs. (2.179)–(2.183), (2.192)*

^mod-c2a-5-1

## Two sets of oscillators

> [!theorem] Theorem §C2a.5.2: Mode Expansion of the Complex Field
> With $p^0 = E_{\mathbf p}$,
>
> $$
> \hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p}\,e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}\,e^{ip\cdot x}\Bigr), \qquad \hat\phi^\dagger(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat b_{\mathbf p}\,e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}\,e^{ip\cdot x}\Bigr) ,
> $$
>
> $\hat\pi = \dot{\hat\phi}^\dagger$, $\hat\pi^\dagger = \dot{\hat\phi}$, at $t = 0$ for the Schrödinger-picture operators. The two independent sets of mode operators are extracted by the Klein–Gordon product ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]]): $\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi)$, $\hat b_{\mathbf p} = (f_{\mathbf p}, \hat\phi^\dagger)$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §§4.4–4.5, eqs. (phicomplex), (picomplex), (ainverse) · PHY 513 Problem Set 3, Problem 2(b), course solution · Yu §2.4.1, eqs. (2.184)–(2.191), and §2.4.2, eqs. (2.194)–(2.203)*

^thm-c2a-5-2

> [!derivation]- Derivation
> **1. General solution without reality.** Steps 1–3 of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-2|Derivation §C2a.2.2]] did not use reality:
>
> $$
> \hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p}\,e^{-ip\cdot x} + \hat{\tilde a}_{-\mathbf p}\,e^{+ip\cdot x}\Bigr) ,
> $$
>
> after the change of variables $\mathbf k = -\mathbf p$ in the negative-frequency term ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$, label $\hat{\tilde a}_{\mathbf k} \to \hat{\tilde a}_{-\mathbf p}$).
>
> **2. Name the second coefficient.** Define $\hat b^\dagger_{\mathbf p} \equiv \hat{\tilde a}_{-\mathbf p}$. This is a definition, not a constraint: $\hat\phi^\dagger \ne \hat\phi$, so step 4 of Derivation §C2a.2.2 does not apply and $\hat b_{\mathbf p}$ is independent of $\hat a_{\mathbf p}$. ⚑ By-product: a complex field has two independent sets of oscillators, the real field one → [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-1|Remark: The real field is a constrained complex field]].
>
> **3. The adjoint field.** Taking the adjoint term by term ($\hat a_{\mathbf p} \to \hat a^\dagger_{\mathbf p}$, $\hat b^\dagger_{\mathbf p} \to \hat b_{\mathbf p}$, $e^{\mp ip\cdot x} \to e^{\pm ip\cdot x}$) gives $\hat\phi^\dagger$ as stated: it brings no new coefficients.
>
> **4. Momenta.** $\hat\pi = \dot{\hat\phi}^\dagger$ and $\hat\pi^\dagger = \dot{\hat\phi}$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]). Differentiate under the integral as in [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-2|Derivation §C2a.2.2]], step 5 (for the operator field, the derivative of a distribution), $\partial_te^{\mp ip\cdot x} = \mp iE_{\mathbf p}e^{\mp ip\cdot x}$, $E_{\mathbf p}/\sqrt{2E_{\mathbf p}} = \sqrt{E_{\mathbf p}/2}$:
>
> $$
> \hat\pi = \int\frac{d^3p}{(2\pi)^3}\,i\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(-\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\Bigr), \qquad \hat\pi^\dagger = \int\frac{d^3p}{(2\pi)^3}\,i\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(-\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x}\Bigr) .
> $$
>
> ⚑ By-product: the momentum conjugate to $\hat\phi$ contains the operators of $\hat\phi^\dagger$ (the crossover) → [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]; [[P1 Canonical Quantization#^p1-1|P1, step 1]].
>
> **5. Fixed time.** At $t = 0$, relabelling $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1) in the negative-frequency terms as in step 6 of Derivation §C2a.2.2:
>
> $$
> \hat\phi = \int\frac{d^3p}{(2\pi)^3}\frac{\hat a_{\mathbf p} + \hat b^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}e^{i\mathbf p\cdot\mathbf x}, \quad \hat\phi^\dagger = \int\frac{d^3p}{(2\pi)^3}\frac{\hat b_{\mathbf p} + \hat a^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}e^{i\mathbf p\cdot\mathbf x}, \quad \hat\pi = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(\hat b_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x}, \quad \hat\pi^\dagger = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(\hat a_{\mathbf p} - \hat b^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x} .
> $$
>
> **6. Extraction.** $\hat\phi = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}f_{\mathbf q} + \hat b^\dagger_{\mathbf q}f^{\ast}_{\mathbf q}\bigr)$. Steps 1–3 of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-5|Derivation §C2a.2.5]] with $\hat a^\dagger_{\mathbf q}$ replaced by $\hat b^\dagger_{\mathbf q}$ give $(f_{\mathbf p}, \hat\phi) = \hat a_{\mathbf p}$ and $-(f^{\ast}_{\mathbf p}, \hat\phi) = \hat b^\dagger_{\mathbf p}$; the same on $\hat\phi^\dagger = \int(\hat b_{\mathbf q}f_{\mathbf q} + \hat a^\dagger_{\mathbf q}f^{\ast}_{\mathbf q})$ gives $(f_{\mathbf p}, \hat\phi^\dagger) = \hat b_{\mathbf p}$; as there, these are identities of operator-valued distributions in $\mathbf p$, and smeared they read $\hat a(g) = (f_g, \hat\phi)$, $\hat b(g) = (f_g, \hat\phi^\dagger)$, combinations of smeared fields ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]). Explicitly, with $\partial_t\hat\phi = \hat\pi^\dagger$ and $\partial_t\hat\phi^\dagger = \hat\pi$,
>
> $$
> \hat a_{\mathbf p} = i\int d^3x\,\bigl(f^*_{\mathbf p}\,\hat\pi^\dagger - \dot f^*_{\mathbf p}\,\hat\phi\bigr), \qquad \hat b_{\mathbf p} = i\int d^3x\,\bigl(f^*_{\mathbf p}\,\hat\pi - \dot f^*_{\mathbf p}\,\hat\phi^\dagger\bigr) .
> $$
>
> ⚑ By-product: $\hat a$ is built from $(\hat\phi, \hat\pi^\dagger)$ and $\hat b$ from $(\hat\phi^\dagger, \pi)$, never from a canonical pair; this decides which commutators survive → [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]].
>
> **What the derivation shows**
> - Dropping reality frees the negative-frequency coefficient: two species, $\hat a$ and $\hat b$.
> - The extraction formula of the real field carries over unchanged; only which field and momentum enter changes.
> - Used next: the algebra ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]), $\hat H$, $\hat{\mathbf P}$ and $\hat Q$.

^der-c2a-5-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!theorem] Theorem §C2a.5.3: Mode Algebra of the Complex Field
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = [\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q) ,
> $$
>
> and all other commutators vanish, including the mixed ones $[\hat a, \hat b]$, $[\hat a, \hat b^\dagger]$: two independent copies of the real field's algebra ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5, eq. (aadagger) and Derivation "From [φ, π] to [a, a†]" · PHY 513 Problem Set 3, Problem 2(b), course solution · Yu §2.4.2, eqs. (2.204)–(2.207) · the user's pre-course notes, §3.4*

^thm-c2a-5-3

> [!derivation]- Derivation
> **1. The operators involved.** From [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-2|Derivation §C2a.5.2]], step 6, and their adjoints:
>
> $$
> \hat a_{\mathbf p} = i\!\int\!(f^*_{\mathbf p}\hat\pi^\dagger - \dot f^*_{\mathbf p}\hat\phi), \quad \hat a^\dagger_{\mathbf q} = -i\!\int\!(f_{\mathbf q}\hat\pi - \dot f_{\mathbf q}\hat\phi^\dagger), \quad \hat b_{\mathbf q} = i\!\int\!(f^*_{\mathbf q}\hat\pi - \dot f^*_{\mathbf q}\hat\phi^\dagger), \quad \hat b^\dagger_{\mathbf q} = -i\!\int\!(f_{\mathbf q}\hat\pi^\dagger - \dot f_{\mathbf q}\hat\phi) .
> $$
>
> **2. The nonzero equal-time relations.** By [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]] only $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3$, $[\hat\phi^\dagger(\mathbf x), \hat\pi^\dagger(\mathbf y)] = i\delta^3$ and their reverses $[\hat\pi, \hat\phi] = [\hat\pi^\dagger, \hat\phi^\dagger] = -i\delta^3$ are nonzero.
>
> **3. $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}]$: expand into four terms.** With $(i)(-i) = 1$,
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = \int d^3x\,d^3y\,\Bigl(f^*_{\mathbf p}f_{\mathbf q}[\hat\pi^\dagger, \hat\pi] - f^*_{\mathbf p}\dot f_{\mathbf q}[\hat\pi^\dagger, \hat\phi^\dagger] - \dot f^*_{\mathbf p}f_{\mathbf q}[\hat\phi, \hat\pi] + \dot f^*_{\mathbf p}\dot f_{\mathbf q}[\hat\phi, \hat\phi^\dagger]\Bigr) .
> $$
>
> The first and last commutators vanish; the middle two are $-i\delta^3$ and $i\delta^3$, giving $i\int d^3x\,(f^*_{\mathbf p}\dot f_{\mathbf q} - \dot f^*_{\mathbf p}f_{\mathbf q}) = (f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ (an identity of distributions in $(\mathbf p, \mathbf q)$; smeared, $[\hat a(g), \hat a^\dagger(h)] = \int\frac{d^3p}{(2\pi)^3}\overline gh$ as in [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], and likewise for $\hat b$), exactly as in steps 2–5 of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-6|Derivation §C2a.2.6]].
>
> **4. $[\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}]$.** Step 3 with $\hat\phi \leftrightarrow \hat\phi^\dagger$, $\hat\pi \leftrightarrow \hat\pi^\dagger$: the surviving commutators are $[\hat\pi, \hat\phi] = -i\delta^3$ and $[\hat\phi^\dagger, \hat\pi^\dagger] = i\delta^3$, and the result is again $(f_{\mathbf p}, f_{\mathbf q})$.
>
> **5. $[\hat a_{\mathbf p}, \hat b^\dagger_{\mathbf q}]$.** Both operators are built from $\hat\pi^\dagger$ and $\hat\phi$ only, and $[\hat\pi^\dagger, \hat\pi^\dagger] = [\hat\pi^\dagger, \hat\phi] = [\hat\phi, \hat\phi] = 0$: every term vanishes. Likewise $[\hat a, \hat a] = 0$ (only $\hat\pi^\dagger$, $\hat\phi$) and $[\hat b, \hat b] = 0$ (only $\hat\pi$, $\hat\phi^\dagger$). ⚑ By-product: $\hat\phi$ is conjugate to $\hat\pi$, not to $\hat\pi^\dagger$; the canonical pairing never crosses the dagger, and this is why the species are independent → [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]] (the vanishing $[\hat\phi, \hat\pi^\dagger]$).
>
> **6. $[\hat a_{\mathbf p}, \hat b_{\mathbf q}]$, the one non-automatic case.** Prefactor $(i)(i) = -1$; the four terms are
>
> $$
> -\int d^3x\,d^3y\,\Bigl(f^*_{\mathbf p}f^*_{\mathbf q}[\hat\pi^\dagger, \hat\pi] - f^*_{\mathbf p}\dot f^*_{\mathbf q}[\hat\pi^\dagger, \hat\phi^\dagger] - \dot f^*_{\mathbf p}f^*_{\mathbf q}[\hat\phi, \hat\pi] + \dot f^*_{\mathbf p}\dot f^*_{\mathbf q}[\hat\phi, \hat\phi^\dagger]\Bigr) = -i\int d^3x\,\bigl(f^*_{\mathbf p}\dot f^*_{\mathbf q} - \dot f^*_{\mathbf p}f^*_{\mathbf q}\bigr) = -(f_{\mathbf p}, f^*_{\mathbf q}) .
> $$
>
> By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], step 9 of its derivation, this is $\propto (E_{\mathbf q} - E_{\mathbf p})\,\delta^3(\mathbf p + \mathbf q) = 0$, because $E_{-\mathbf p} = E_{\mathbf p}$: a smooth function vanishing on the support of δ, times δ, is the zero distribution ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1); smeared, $(f_g, f^*_h) = 0$ exactly ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]]).
>
> **7. The rest by adjoints.** $[\hat a^\dagger, \hat a^\dagger]$, $[\hat b^\dagger, \hat b^\dagger]$, $[\hat a^\dagger, \hat b^\dagger]$ and $[\hat b, \hat a^\dagger]$ are adjoints (up to sign) of the vanishing ones.
>
> **What the derivation shows**
> - Two independent oscillator algebras come out of one complex field; independence is derived, not assumed.
> - $[\hat a, \hat b] = 0$ rests on $E_{-\mathbf p} = E_{\mathbf p}$; it is what will kill the number-changing terms of $\hat H$ and $\hat{\mathbf P}$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]]).

^der-c2a-5-3

*Uses:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark] Remark: The real field is a constrained complex field, with one trap
> Imposing $\hat\phi^\dagger = \hat\phi$ in Theorems §C2a.5.2 and §C2a.5.3 and comparing coefficients gives $\hat b_{\mathbf p} = \hat a_{\mathbf p}$: one set of oscillators is removed and [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] results, which is why the user's notes derive everything for the complex field first. But setting $\hat b = \hat a$ in the *Hamiltonian* below overcounts by a factor 2: a complex field constrained to be real has $\mathcal L = (\partial\phi)^2 - m^2\phi^2$, twice the canonical real Lagrangian. The real field is one of the two real components, $\hat\phi_1$, not the complex field made real.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.4 ("Real field") and §4.6 ("Real field")*

^rem-c2a-5-1

> [!theorem] Theorem §C2a.5.4: Hamiltonian of the Complex Field
> The Hamiltonian of [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]], the field form of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]] (recalled above) read as an operator in the order written, is in modes
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) + 2E_0 ,
> $$
>
> with $E_0$ the real field's zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]): one $\frac12E_{\mathbf p}$ per mode per species. Normal ordered, $:\!\hat H\!: = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^\dagger\hat a + \hat b^\dagger\hat b)$. It is time independent.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.6, eqs. (Hcomplexzp), (Hcomplex) · PHY 513 Problem Set 3, Problem 2(b), course solution · Yu §2.4.4, eqs. (2.215), (2.217)*

^thm-c2a-5-4

> [!derivation]- Derivation
> Work at a fixed but arbitrary time $t$ with the time-dependent expansion; time independence will come out.
>
> **1. Integrate the gradient term by parts.** $\int d^3x\,\nabla\hat\phi^\dagger\cdot\nabla\hat\phi = \lim_{R\to\infty}\oint_{|\mathbf x| = R}\hat\phi^\dagger\nabla\hat\phi\cdot d\mathbf S - \int d^3x\,\hat\phi^\dagger\nabla^2\hat\phi$. ⚑ By-product: the surface term is dropped by assuming fall-off at spatial infinity (for the plane-wave expansion, in the distributional sense) → [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]. *Sense:* in matrix elements between wave-packet states the integrands are Schwartz functions of $\mathbf x$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-4|Derivation §C2a.2.4]], step 1), and the surface integral over $|\mathbf x| = R$ tends to $0$ as $R \to \infty$.
>
> **2. Use the field equation.** Each mode $e^{\mp ip\cdot x}$ is on shell, so the expansion satisfies $\ddot{\hat\phi} = (\nabla^2 - m^2)\hat\phi$. Hence
>
> $$
> \int d^3x\,\bigl(\nabla\hat\phi^\dagger\cdot\nabla\hat\phi + m^2\hat\phi^\dagger\hat\phi\bigr) = -\int d^3x\,\hat\phi^\dagger(\nabla^2 - m^2)\hat\phi = -\int d^3x\,\hat\phi^\dagger\ddot{\hat\phi}, \qquad \hat H = \int d^3x\,\bigl(\hat\pi^\dagger\hat\pi - \hat\phi^\dagger\ddot{\hat\phi}\bigr) .
> $$
>
> The mass shell is spent here.
>
> **3. Substitute, with all four terms of each product.** Variable $\mathbf p$ in the first factor, $\mathbf q$ in the second; $\ddot{\hat\phi}$ multiplies each mode by $-E_{\mathbf q}^2$, and $\hat\pi^\dagger\hat\pi$ carries $i\cdot i = -1$:
>
> $$
> \hat\pi^\dagger\hat\pi = \int\frac{d^3p\,d^3q}{(2\pi)^6}\frac{\sqrt{E_{\mathbf p}E_{\mathbf q}}}{2}\Bigl(-\hat a_{\mathbf p}\hat b_{\mathbf q}e^{-i(p+q)\cdot x} + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf q}e^{i(p-q)\cdot x} - \hat b^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf q}e^{i(p+q)\cdot x}\Bigr),
> $$
>
> $$
> -\hat\phi^\dagger\ddot{\hat\phi} = \int\frac{d^3p\,d^3q}{(2\pi)^6}\frac{E_{\mathbf q}^2}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\Bigl(\hat b_{\mathbf p}\hat a_{\mathbf q}e^{-i(p+q)\cdot x} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{i(p+q)\cdot x}\Bigr) .
> $$
>
> **4. The $d^3x$ integrals.** By the split rule ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]]; identities in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], with the phase moved out by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]):
>
> $$
> \int d^3x\,e^{\mp i(p+q)\cdot x} = e^{\mp i(E_{\mathbf p} + E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p + \mathbf q), \qquad \int d^3x\,e^{\mp i(p-q)\cdot x} = e^{\mp i(E_{\mathbf p} - E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p - \mathbf q) .
> $$
>
> **5. Integrate the deltas over $\mathbf q$.** In the $p + q$ terms $\mathbf q = -\mathbf p$; in the $p - q$ terms $\mathbf q = \mathbf p$ (δ acting in $\mathbf q$; the smooth prefactors are evaluated on the support, [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1). In both $E_{\mathbf q} = E_{\mathbf p}$, so both prefactors become $E_{\mathbf p}/2$; the $p - q$ phases become $1$, the $p + q$ phases $e^{\mp2iE_{\mathbf p}t}$:
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}\Bigl[e^{-2iE_{\mathbf p}t}\bigl(-\hat a_{\mathbf p}\hat b_{-\mathbf p} + \hat b_{\mathbf p}\hat a_{-\mathbf p}\bigr) + e^{2iE_{\mathbf p}t}\bigl(-\hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}\bigr) + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\Bigr] .
> $$
>
> **6. The $e^{-2iE_{\mathbf p}t}$ group vanishes.** Substitute $\mathbf p \to -\mathbf p$ in its first term ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian 1; $E$ and the phase unchanged; $\hat a_{\mathbf p}\hat b_{-\mathbf p} \to \hat a_{-\mathbf p}\hat b_{\mathbf p}$): the group becomes $\hat b_{\mathbf p}\hat a_{-\mathbf p} - \hat a_{-\mathbf p}\hat b_{\mathbf p} = [\hat b_{\mathbf p}, \hat a_{-\mathbf p}] = 0$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]). Dropped: the species commute.
>
> **7. The $e^{2iE_{\mathbf p}t}$ group vanishes.** Substitute $\mathbf p \to -\mathbf p$ in its second term ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1; $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p} \to \hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p}$): the group becomes $\hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p} = [\hat a^\dagger_{-\mathbf p}, \hat b^\dagger_{\mathbf p}] = 0$. With the two groups go the only time-dependent terms: $\hat H$ is the same on every slice.
>
> **8. Reorder.** $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$ and $\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} = \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$:
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) + 2\cdot\int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\,(2\pi)^3\delta^3(\mathbf 0) .
> $$
>
> ⚑ By-product: the constant is $2E_0$, twice the real field's zero-point energy, one tower per species → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]; as written it has no value, and in the box it is $2E_0(V, \Lambda) = \sum_{|\mathbf k|<\Lambda}E_{\mathbf k}$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]); normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]) removes it.
>
> **What the derivation shows**
> - Two independent oscillators per momentum, both of frequency $E_{\mathbf p}$: particle and antiparticle have the same mass.
> - Here the number-changing terms die because the species commute (steps 6–7), the mass shell having been spent in step 2; in the real-field route ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], steps 4–6) the mass shell kills them directly. The course solution uses the latter route for this field too.
> - Assumptions used: fall-off at infinity (step 1), the algebra of Theorem §C2a.5.3.

^der-c2a-5-4

*Uses:* [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]

*Procedure:* [[P1 Canonical Quantization#^p1-7|P1, step 7]]

> [!theorem] Theorem §C2a.5.5: Momentum of the Complex Field
> The field momentum of the complex field in field form ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-8|Theorem §C1b.6.8]], recalled above) is in modes
>
> $$
> \hat{\mathbf P} = -\int d^3x\,\bigl(\hat\pi\,\nabla\hat\phi + \hat\pi^\dagger\,\nabla\hat\phi^\dagger\bigr) = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) ,
> $$
>
> with no constant and no ordering choice: particles and antiparticles of label $\mathbf p$ both carry momentum $\mathbf p$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.7, eq. (Pfinal) · Yu §2.4.4, eq. (2.216) · the user's pre-course notes, §3.4 (Note "Reducing H and P to mode form")*

^thm-c2a-5-5

> [!derivation]- Derivation
> **1. Substitute the $t = 0$ forms** of [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-2|Derivation §C2a.5.2]], step 5: variable $\mathbf p$ in the momentum density, $\mathbf p'$ in the gradient, which brings down $i\mathbf p'$; the factor $(-i)(i) = 1$:
>
> $$
> -\int d^3x\,\hat\pi\nabla\hat\phi = -\int d^3x\int\frac{d^3p\,d^3p'}{(2\pi)^6}\,\frac{\mathbf p'\sqrt{E_{\mathbf p}}}{2\sqrt{E_{\mathbf p'}}}\bigl(\hat b_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\bigr)\bigl(\hat a_{\mathbf p'} + \hat b^\dagger_{-\mathbf p'}\bigr)e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} ,
> $$
>
> and the same for $-\int\hat\pi^\dagger\nabla\hat\phi^\dagger$ with $(\hat a_{\mathbf p} - \hat b^\dagger_{-\mathbf p})(\hat b_{\mathbf p'} + \hat a^\dagger_{-\mathbf p'})$.
>
> **2. $d^3x$, then the delta.** $\int d^3x\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p + \mathbf p')$ (an identity in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; the exchange as in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], step 2); integrating $\mathbf p'$ sets $\mathbf p' = -\mathbf p$, $E_{\mathbf p'} = E_{\mathbf p}$, and the factor becomes $-\mathbf p/2$, i.e. $+\mathbf p/2$ with the overall minus sign:
>
> $$
> \hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\,\frac{\mathbf p}{2}\Bigl[\bigl(\hat b_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\bigr)\bigl(\hat a_{-\mathbf p} + \hat b^\dagger_{\mathbf p}\bigr) + \bigl(\hat a_{\mathbf p} - \hat b^\dagger_{-\mathbf p}\bigr)\bigl(\hat b_{-\mathbf p} + \hat a^\dagger_{\mathbf p}\bigr)\Bigr] .
> $$
>
> **3. Expand into all eight terms.**
>
> $$
> \hat b_{\mathbf p}\hat a_{-\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p} - \hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a_{\mathbf p}\hat b_{-\mathbf p} + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} - \hat b^\dagger_{-\mathbf p}\hat b_{-\mathbf p} - \hat b^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p} .
> $$
>
> **4. Annihilator pairs.** In $\mathbf p\,\hat a_{\mathbf p}\hat b_{-\mathbf p}$ substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian 1): it becomes $-\mathbf p\,\hat a_{-\mathbf p}\hat b_{\mathbf p}$. Together with $\mathbf p\,\hat b_{\mathbf p}\hat a_{-\mathbf p}$: $\mathbf p\,[\hat b_{\mathbf p}, \hat a_{-\mathbf p}] = 0$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]). Dropped: the species commute.
>
> **5. Creator pairs.** In $-\mathbf p\,\hat b^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p}$ substitute $\mathbf p \to -\mathbf p$: it becomes $+\mathbf p\,\hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p}$. Together with $-\mathbf p\,\hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p}$: $-\mathbf p\,[\hat a^\dagger_{-\mathbf p}, \hat b^\dagger_{\mathbf p}] = 0$.
>
> **6. Number-conserving terms.** In $-\mathbf p\,\hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p}$ and $-\mathbf p\,\hat b^\dagger_{-\mathbf p}\hat b_{-\mathbf p}$ substitute $\mathbf p \to -\mathbf p$: they become $+\mathbf p\,\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$ and $+\mathbf p\,\hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}$. So
>
> $$
> \hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\,\frac{\mathbf p}{2}\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) .
> $$
>
> **7. Reorder.** The commutators leave $V\int\frac{d^3p}{(2\pi)^3}\,\mathbf p$, an odd integrand: zero for a rotation-invariant regularization, as in step 7 of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-5|Derivation §C2a.3.5]].
>
> **What the derivation shows**
> - Both species carry momentum $\mathbf p$ for label $\mathbf p$: the negative-frequency term creates an antiparticle of momentum $+\mathbf p$, not $-\mathbf p$, because of the relabelling in [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-2|Derivation §C2a.5.2]], step 1.
> - The number-changing terms die by the mixed commutator; for the real field they died by oddness ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).

^der-c2a-5-5

*Uses:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-7|P1, step 7]]

## The charge

The Lagrangian ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]]) is invariant under the global phase rotation $\phi \to e^{i\alpha}\phi$, $\phi^\dagger \to e^{-i\alpha}\phi^\dagger$; Noether's theorem ([[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]; this current: [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]) gives, for $\Delta\phi = i\phi$, the conserved current $j^\mu = i(\phi\,\partial^\mu\phi^* - \phi^*\partial^\mu\phi)$ (PS eq. (2.16)), conserved even though $m \ne 0$. Its quantum version is normalized as follows. The current, derived in [[§C1b.5 Noether's Theorem|§C1b.5]]:

![[§C1b.5 Noether's Theorem#^thm-c1b-5-5]]

> [!definition] Definition §C2a.5.1: The U(1) Charge Operator
> The **charge** of the complex scalar field is
>
> $$
> \hat Q = \frac i2\int d^3x\;:\!\bigl(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi\bigr)\!: \; = \frac i2\int d^3x\;:\!\hat\phi^\dagger\overleftrightarrow{\partial_t}\hat\phi\!: ,
> $$
>
> normal ordered ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]). It is $-\frac12$ times the Noether charge $\int d^3x\,j^0$ of the current above, and $\frac12(\hat\phi, \hat\phi)$ in the notation of the Klein–Gordon inner product ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.7, eq. (Qdef) · PHY 513 Problem Set 3, Problem 2(c) (= PS Problem 2.2(c)), course solution*

^def-c2a-5-1

> [!theorem] Theorem §C2a.5.6: The Charge Counts Particles Minus Antiparticles
>
> $$
> \hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) = \tfrac12\bigl(\hat N_a - \hat N_b\bigr), \qquad [\hat Q, \hat a^\dagger_{\mathbf p}] = +\tfrac12\hat a^\dagger_{\mathbf p}, \quad [\hat Q, \hat b^\dagger_{\mathbf p}] = -\tfrac12\hat b^\dagger_{\mathbf p} ,
> $$
>
> and $[\hat Q, \hat H] = [\hat Q, \hat{\mathbf P}] = 0$: the charge is conserved. Without normal ordering, $\hat Q$ would be $\frac12(\hat N_a - \hat N_b) - \frac12V\int\frac{d^3p}{(2\pi)^3}$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.7 (Derivation "The charge in mode form") · PHY 513 Problem Set 3, Problem 2(c), course solution · Yu §2.4.3, eqs. (2.211)–(2.212)*

^thm-c2a-5-6

> [!derivation]- Derivation
> **1. Substitute.** In $\hat Q = \frac i2\int d^3x\,(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)$ (before ordering) insert the expansions of [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]] at time $t$, variable $\mathbf p$ in the first factor and $\mathbf q$ in the second. The prefactors are
>
> $$
> \hat\phi^\dagger\hat\pi^\dagger:\ \frac{1}{\sqrt{2E_{\mathbf p}}}\cdot i\sqrt{\frac{E_{\mathbf q}}{2}} = \frac i2\sqrt{\frac{E_{\mathbf q}}{E_{\mathbf p}}}, \qquad \hat\pi\hat\phi:\ i\sqrt{\frac{E_{\mathbf p}}{2}}\cdot\frac{1}{\sqrt{2E_{\mathbf q}}} = \frac i2\sqrt{\frac{E_{\mathbf p}}{E_{\mathbf q}}} .
> $$
>
> **2. Expand both products into all four terms.**
>
> $$
> \bigl(\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)\bigl(-\hat a_{\mathbf q}e^{-iq\cdot x} + \hat b^\dagger_{\mathbf q}e^{iq\cdot x}\bigr) = -\hat b_{\mathbf p}\hat a_{\mathbf q}e^{-i(p+q)\cdot x} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} - \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{i(p+q)\cdot x} ,
> $$
>
> $$
> \bigl(-\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)\bigl(\hat a_{\mathbf q}e^{-iq\cdot x} + \hat b^\dagger_{\mathbf q}e^{iq\cdot x}\bigr) = -\hat b_{\mathbf p}\hat a_{\mathbf q}e^{-i(p+q)\cdot x} - \hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{i(p+q)\cdot x} .
> $$
>
> **3. $d^3x$ and the deltas.** As in steps 4–5 of [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-4|Derivation §C2a.5.4]]: $\mathbf q = -\mathbf p$ in the $p + q$ terms, $\mathbf q = \mathbf p$ in the $p - q$ terms; in both $E_{\mathbf q} = E_{\mathbf p}$, so both prefactors become $\frac i2$.
>
> **4. Number-changing terms cancel.** The first product minus the second: $(-\hat b_{\mathbf p}\hat a_{-\mathbf p}) - (-\hat b_{\mathbf p}\hat a_{-\mathbf p}) = 0$ and $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p} - \hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p} = 0$, term by term, with no relabelling. Dropped: identical terms with opposite sign, once the energies are equal.
>
> **5. Number-conserving terms double.** $(\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}) - (-\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}) = 2\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - 2\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, with phase $1$. With the outer $\frac i2$ and the prefactor $\frac i2$, $\frac i2\cdot\frac i2 = -\frac14$:
>
> $$
> \hat Q = -\frac14\int\frac{d^3p}{(2\pi)^3}\bigl(2\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - 2\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\bigr) = \frac12\int\frac{d^3p}{(2\pi)^3}\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p}\bigr) .
> $$
>
> **6. Reorder.** $\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} = \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$ gives $\hat Q = \frac12(\hat N_a - \hat N_b) - \frac12V\int\frac{d^3p}{(2\pi)^3}$. *Sense:* $(2\pi)^3\delta^3(\mathbf 0)$ has no value; in the box of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]] the constant is $-\frac12\sum_{|\mathbf k|<\Lambda}1 = -\frac12\mathcal N(V, \Lambda)$, minus half the number of modes, with $\mathcal N \approx V\Lambda^3/6\pi^2$ (lattice points in the ball, one per momentum cell of volume $(2\pi)^3/V$): its density $-\Lambda^3/12\pi^2$ diverges with the cutoff. ⚑ By-product: an infinite negative vacuum charge, which normal ordering removes and which, unlike $E_0$, would be observable → [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|Remark: Why the vacuum must be neutral]]. The normal-ordered $\hat Q$ of [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]] is the first term.
>
> **7. Ladder relations.** As in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-7|Derivation §C2a.3.7]], steps 2–3, with weight $\frac12$: $[\frac12\int \hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = \frac12\hat a^\dagger_{\mathbf p}$; and $[-\frac12\int \hat b^\dagger_{\mathbf q}\hat b_{\mathbf q}, \hat b^\dagger_{\mathbf p}] = -\frac12\hat b^\dagger_{\mathbf p}$. The cross commutators vanish by [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]].
>
> **8. Conservation.** $\hat Q$, $:\!\hat H\!:$ and $\hat{\mathbf P}$ are integrals of the number densities $\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, $\hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}$, which commute with each other (step 5 of [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-1|Derivation §C2a.4.1]], for each species, and Theorem §C2a.5.3 across species). So $[\hat Q, \hat H] = [\hat Q, \hat{\mathbf P}] = 0$.
>
> **What the derivation shows**
> - $a$-quanta carry $+\frac12$ and $b$-quanta $-\frac12$ in this normalization; only the ratio $-1$ is physical ([[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|Caution: Normalization and sign of the charge]]).
> - The number-changing terms cancel identically (step 4), by a third mechanism after the mass shell ($\hat H$) and the mixed commutator ($\hat{\mathbf P}$).
> - The ordering constant is a vacuum charge, and its removal is forced by physics (step 6).

^der-c2a-5-6

*Uses:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]

*Procedure:* [[P1 Canonical Quantization#^p1-8|P1, step 8]]

> [!caution] Caution: Normalization and sign of the charge
> Only the ratio $-1$ of the two species' charges is physical; the overall factor and sign are conventions, and the sources differ:
> - **These notes, Peskin–Schroeder and Problem Set 3:** $\hat Q = \frac i2\int(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi) = \frac12(\hat N_a - \hat N_b)$; $a$-quanta carry $+\frac12$.
> - **The Noether current with $\Delta\phi = +i\phi$** (the user's notes, Ch. 3; PS eq. (2.16)): $\int \hat j^0 = \hat N_b - \hat N_a$, twice as large and of opposite sign, because a positive-frequency mode $\phi = Ae^{-iEt}$ has $j^0 = -2E|A|^2 < 0$. The lecture slides and board write the current with the opposite overall sign, which gives $\hat N_a - \hat N_b$ ([[§C1b.5 Noether's Theorem#^cau-c1b-5-3|§C1b.5, Caution: Sign and normalization of the U(1) current]]).
> - **Yu:** $\hat Q = iq\int\hat\phi^\dagger\overleftrightarrow{\partial^0}\hat\phi = q(\hat N_a - \hat N_b)$ (eq. (2.212)), $2q$ times the definition above.
> - **Quantum Mechanics ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-7|QM Theorem §C13.1.7]]):** $\hat Q = e(\hat N_b - \hat N_c)$, with $\hat b$ the particles, in Sakurai's notation.
>
> The sign of the Noether current is the sign of $\alpha$; [[Larsen PHY 513]] records the choice.

^cau-c2a-5-1

> [!remark] Remark: Why the vacuum must be neutral
> For the energy, the ordering constant was an unobservable shift ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|Remark: Why the zero-point energy is dropped]]). For the charge it is not: the unordered $\hat Q$ gives the vacuum an infinite negative charge, $-\frac12V\int d^3p/(2\pi)^3$ (Yu's "zero-point charge"). A charged vacuum would distinguish particles from antiparticles and break the symmetry between $\hat a$ and $\hat b$ (charge conjugation; QFT C9, planned). So here the ordering is fixed by physics: the vacuum must be neutral. Normal ordering achieves it; so does symmetrizing, $\frac12(\hat a^\dagger\hat a + \hat a\hat a^\dagger) - \frac12(\hat b^\dagger\hat b + \hat b\hat b^\dagger)$, whose constants $\pm\frac12(2\pi)^3\delta^3(\mathbf 0)$ cancel between the species.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.7 ("Here the ordering is not harmless") · Yu §2.4.3, eq. (2.212)*

^rem-c2a-5-2

> [!theorem] Theorem §C2a.5.7: Particles and Antiparticles
> $\hat a^\dagger_{\mathbf p}|0\rangle$ and $\hat b^\dagger_{\mathbf p}|0\rangle$ both have energy $E_{\mathbf p}$ and momentum $\mathbf p$: two species of the same mass $m$, with opposite charges $+\frac12$ and $-\frac12$. A state with $n_a$ $a$-quanta and $n_b$ $b$-quanta has $Q = \frac12(n_a - n_b)$. A real scalar field admits no such phase symmetry, $\hat Q \equiv 0$: its quanta are truly neutral, each its own antiparticle.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.7–4.8 · Yu §2.4.3, eqs. (2.212)–(2.216) · the user's pre-course notes, §3.4 (Keypoint "Particle and antiparticle")*

^thm-c2a-5-7

> [!derivation]- Derivation
> **1. Ladder relations for both species.** $:\!\hat H\!:$ and $\hat{\mathbf P}$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]]) are sums of one real-field form per species, and the species commute ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]). So [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-7|Derivation §C2a.3.7]], steps 2–5, applies to each: $[\hat H, \hat a^\dagger_{\mathbf p}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p}$, $[\hat H, \hat b^\dagger_{\mathbf p}] = E_{\mathbf p}\hat b^\dagger_{\mathbf p}$, $[\hat{\mathbf P}, \hat a^\dagger_{\mathbf p}] = \mathbf p\,\hat a^\dagger_{\mathbf p}$, $[\hat{\mathbf P}, \hat b^\dagger_{\mathbf p}] = \mathbf p\,\hat b^\dagger_{\mathbf p}$.
>
> **2. Charges.** $[\hat Q, \hat a^\dagger_{\mathbf p}] = \frac12\hat a^\dagger_{\mathbf p}$, $[\hat Q, \hat b^\dagger_{\mathbf p}] = -\frac12\hat b^\dagger_{\mathbf p}$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]]), and $\hat Q|0\rangle = 0$ because every term of the normal-ordered $\hat Q$ ends in an annihilator.
>
> **3. Many quanta.** Push $\hat H$, $\hat{\mathbf P}$, $\hat Q$ through the creation operators one at a time, as in step 4 of [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-1|Derivation §C2a.4.1]]: each $\hat a^\dagger$ adds $+\frac12$ to $\hat Q$, each $\hat b^\dagger$ adds $-\frac12$.
>
> **4. The real field.** A phase rotation $\hat\phi \to e^{iq\theta}\hat\phi$ must respect $\hat\phi^\dagger = \hat\phi$: $e^{iq\theta}\hat\phi = (e^{iq\theta}\hat\phi)^\dagger = e^{-iq\theta}\hat\phi$ for all $\theta$ forces $q = 0$ (Yu eq. (2.214)). In modes, $\hat b = \hat a$ makes $\frac12(\hat N_a - \hat N_b) = 0$.
>
> **What the derivation shows**
> - Same mass because both species are created by one field on one mass shell; opposite charge because they sit in the two frequency parts of that field.
> - Truly neutral particles are exactly the quanta of Hermitian fields.

^der-c2a-5-7

*Uses:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-8|P1, step 8]]

> [!remark] Remark: Charge, not probability
> - **What the negative frequencies became.** Classically the Klein–Gordon charge already splits as $|a_{\mathbf p}|^2 - |b_{\mathbf p}|^2$, positive frequencies against negative ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-2|QM Theorem §C13.1.2]]); after quantization each term counts quanta, and the negative-frequency solutions multiply $\hat b^\dagger$, the creation of antiparticles of *positive* energy. The density whose indefinite sign wrecked the probability interpretation ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]]) is the charge density: negative values are antimatter, not a pathology. Its eigenvalues are integers (in units of the species' charge), unlike a probability.
> - **What changes from Quantum Mechanics.** [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-7|QM Theorem §C13.1.7]] built the charged field from two independent real fields in a box and normal ordered the charge by fiat. Here the complex field is quantized through its own canonical pairs, with the crossover $\hat\pi = \dot{\hat\phi}^\dagger$, the independence of the two species is derived ($[\hat a, \hat b] = 0$ comes out rather than being assumed), and the ordering is forced by the neutrality of the vacuum. The same result for a new reason: this section is the home.
> - **Coupling.** If the field is electrically charged, $\hat Q$ times the unit of charge is the electric charge, and charge conservation is Noether's theorem for this phase symmetry; making $\alpha$ depend on $x$ requires a gauge field (QFT C8, planned; [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^pr-c13-1-3|QM Principle §C13.1.3]] for minimal coupling of the wave function).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (Example 2) and Ch. 4 §4.7 · the user's pre-course notes, §3.4 (Remark "The charge interpretation of ρ") · Yu §2.4.3, eq. (2.213)*

^rem-c2a-5-3

> [!remark]- Connections
> - A complex field is two real fields of the same mass, and $\phi \to e^{i\alpha}\phi$ is a rotation of the pair $(\phi_1, \phi_2)$: U(1) $\cong$ SO(2), and the current in real components is $\phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$, the field-space analogue of angular momentum $xp_y - yp_x$ — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|Theorem §C1b.2.8]], [[§C1b.5 Noether's Theorem#^ex-c1b-5-2|Example §C1b.5.2]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-8|§C1b.5, Remark: Global, internal, and what a local phase would need]]; [[§B8.1 Poisson Brackets#^thm-b8-1-5|CM Theorem §B8.1.5]] for conserved quantities as generators.
> - The charge is half the Klein–Gordon inner product of the field with itself, which is why it is positive on positive-frequency ($a$) quanta and why its conservation is the slice independence of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 1 — [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]].
> - The ordering problem is the field-theory version of the oscillator's zero-point energy, but with an observable consequence; the ordering prescription chosen here is the same normal ordering that Wick's theorem builds on — [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|Remark: Normal ordering is a choice of quantization]], QFT C7 (planned).
> - Particle and antiparticle having the same mass is guaranteed here because both are created by one field on one mass shell; in general it is the CPT theorem — QFT C9 (planned).
> - The Heisenberg equations of the complex field, $\dot{\hat\phi} = \hat\pi^\dagger$ and $\dot{\hat\pi}^\dagger = (\nabla^2 - m^2)\hat\phi$, reproduce the Klein–Gordon equation (Problem Set 3, Problem 2(a2)) — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]; the complex field's propagator $\langle0|T\{\hat\phi(x)\hat\phi^\dagger(y)\}|0\rangle$ propagates a particle one way and an antiparticle the other — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]].
> - The complex field is an operator-valued distribution exactly as the real one: smeared with a real test function, $\hat\phi(f) = \hat a(g_f) + \hat b^\dagger(g_f)$ with $g_f = \tilde f/\sqrt{2E_{\mathbf p}}$ (the computation of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 3, with $\hat a^\dagger \to \hat b^\dagger$), no longer Hermitian; its relations and its two mode algebras hold after smearing — [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]].
> - The ordering constants of $\hat H$ and $\hat Q$ are δ at its singular point; the box makes them $\sum_{\mathbf k}E_{\mathbf k}$ and $-\frac12\sum_{\mathbf k}1$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]) — [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.2 Generalized Functions#^thm-ca-2-10|Theorem §CA.2.10]].
> - The mode computations use the plane-wave delta (an identity in $\mathcal S'$), Fubini for wave packets with the split-exponential rule, relabelling with Jacobian 1, evaluation of smooth prefactors on the support of δ, and integration by parts with fall-off — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]].
> - The Dirac field repeats the structure with two species of operators, but the roles are reversed: its classical charge $\int\psi^\dagger\psi$ is positive definite and its energy is not, and anticommutators are what turn them into particles minus antiparticles and a positive Hamiltonian — [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]].
