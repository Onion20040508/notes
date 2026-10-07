---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2a.1 Canonical Quantization of Fields]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2a.3 Energy, Momentum and the Zero-Point Energy]] →

*Sources: the user's PHY 513 notes, Ch. 4 §§4.2–4.5 (§4.2 for the decoupling into oscillators) · PHY 513 Lecture 4 (Larsen), Part B; Problem Set 3, Problem 3, with the course solutions · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.3, eqs. (2.21)–(2.22) and the rest of §2.3 · Yu Zhao-Huan, 量子场论讲义, §§2.3.1–2.3.2 · the user's pre-course notes, §3.3.*

How is the free real scalar field written in terms of oscillators, and what algebra do they obey? [[§C2a.1 Canonical Quantization of Fields|§C2a.1]] supplied the quantum model ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]) and the postulate ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]); this section first shows that the classical field is a set of oscillators ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]]); Quantum Mechanics supplies the oscillator algebra ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]]). This section derives the mode expansion and its algebra; the tool that extracts the oscillators from the field is the Klein–Gordon inner product. The energy and momentum follow in [[§C2a.3 Energy, Momentum and the Zero-Point Energy|§C2a.3]] and the particles in [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]]; the steps here are [[P1 Canonical Quantization#^p1-5|P1, steps 5–6]].

## The free field as oscillators

> [!theorem] Theorem §C2a.2.1: The Free Field Is a Set of Independent Oscillators
> Expand the classical free real field and its momentum density at a fixed time, $\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\tilde\phi(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$ and likewise $\pi$, with $\tilde\phi(-\mathbf p) = \tilde\phi^*(\mathbf p)$, $\tilde\pi(-\mathbf p) = \tilde\pi^*(\mathbf p)$. Then
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\;\frac12\Bigl[\,|\tilde\pi(\mathbf p)|^2 + E_{\mathbf p}^2\,|\tilde\phi(\mathbf p)|^2\Bigr], \qquad \ddot{\tilde\phi}(\mathbf p, t) + E_{\mathbf p}^2\,\tilde\phi(\mathbf p, t) = 0 ,
> $$
>
> a sum of independent oscillators of unit mass and frequency $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, one for each $\mathbf p$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 (Derivation "The decoupling is classical") · PS §2.3, eqs. (2.21)–(2.22) · PHY 513 Lecture 4, Part B ("modes decouple")*

^thm-c2a-2-1

> [!derivation]- Derivation
> **1. Substitute the kinetic term.** With variable $\mathbf p$ in the first factor and $\mathbf p'$ in the second,
>
> $$
> \int d^3x\,\tfrac12\pi^2 = \frac12\int\frac{d^3p}{(2\pi)^3}\frac{d^3p'}{(2\pi)^3}\,\tilde\pi(\mathbf p)\,\tilde\pi(\mathbf p')\int d^3x\;e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} .
> $$
>
> **2. The $d^3x$ integral.** $\int d^3x\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p + \mathbf p')$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]), after exchanging the order of integration. *Sense:* the delta is an identity in $\mathcal S'$ in the variable $\mathbf p + \mathbf p'$, not a convergent integral ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the exchange is legitimate for a field whose transforms $\tilde\phi(\mathbf p)$, $\tilde\pi(\mathbf p)$ are wave packets (Schwartz functions), and steps 2–3 together are the identity $\int d^3x\,a(\mathbf x)b(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}A(\mathbf p)B(-\mathbf p)$, proved by Fubini for wave packets ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]).
>
> **3. Integrate the delta.** The $\mathbf p'$ integral sets $\mathbf p' = -\mathbf p$ (eliminating $\mathbf p'$) and cancels one $(2\pi)^3$; this is $\delta^3$ acting on the test function $\mathbf p' \mapsto \tilde\pi(\mathbf p')$ ([[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]):
>
> $$
> \int d^3x\,\tfrac12\pi^2 = \frac12\int\frac{d^3p}{(2\pi)^3}\,\tilde\pi(\mathbf p)\,\tilde\pi(-\mathbf p) .
> $$
>
> **4. Reality.** $\pi$ is real, so $\tilde\pi(-\mathbf p) = \tilde\pi^{\ast}(\mathbf p)$ and the integrand is $|\tilde\pi(\mathbf p)|^2$. ⚑ By-product: the $\mathbf x$ integral pairs each mode $\mathbf p$ with $-\mathbf p$ only (translation invariance), and reality makes the pair one oscillator's worth of variables → [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|Remark: Why the modes decouple]].
>
> **5. The gradient term.** $\nabla\phi = \int\frac{d^3p}{(2\pi)^3}\,(i\mathbf p)\,\tilde\phi(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$ (derivative under the integral, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], with the dominating function $|\mathbf p\,\tilde\phi(\mathbf p)|$, integrable for a wave packet; for a transform that is only a distribution it is the derivative rule of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3). With $\mathbf p$ in the first factor and $\mathbf p'$ in the second,
>
> $$
> \int d^3x\,\tfrac12(\nabla\phi)^2 = \frac12\int\frac{d^3p}{(2\pi)^3}\frac{d^3p'}{(2\pi)^3}\,(i\mathbf p)\cdot(i\mathbf p')\,\tilde\phi(\mathbf p)\,\tilde\phi(\mathbf p')\,(2\pi)^3\delta^3(\mathbf p + \mathbf p') ,
> $$
>
> the $d^3x$ integral done as in step 2. The $\mathbf p'$ integral sets $\mathbf p' = -\mathbf p$, so $(i\mathbf p)\cdot(i\mathbf p') \to (i\mathbf p)\cdot(-i\mathbf p) = \mathbf p^2$ and $\tilde\phi(\mathbf p') \to \tilde\phi(-\mathbf p) = \tilde\phi^*(\mathbf p)$ (step 4 for $\tilde\phi$):
>
> $$
> \int d^3x\,\tfrac12(\nabla\phi)^2 = \frac12\int\frac{d^3p}{(2\pi)^3}\,\mathbf p^2\,|\tilde\phi(\mathbf p)|^2 .
> $$
>
> **6. The mass term.** The same with $m^2$ in place of $(i\mathbf p)\cdot(i\mathbf p')$: $\int d^3x\,\frac12m^2\phi^2 = \frac12\int\frac{d^3p\,d^3p'}{(2\pi)^6}\,m^2\,\tilde\phi(\mathbf p)\tilde\phi(\mathbf p')(2\pi)^3\delta^3(\mathbf p + \mathbf p') = \frac12\int\frac{d^3p}{(2\pi)^3}\,m^2|\tilde\phi(\mathbf p)|^2$.
>
> **7. Add.** $\mathbf p^2 + m^2 = E_{\mathbf p}^2$ gives the Hamiltonian of the statement. ⚑ By-product: the frequency is fixed by the gradient term ($\mathbf p^2$) and the mass term ($m^2$) together; it is the mass-shell energy → [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|Remark: Why the frequency is the energy]].
>
> **8. The equation of motion.** Insert the expansion into $\ddot\phi - \nabla^2\phi + m^2\phi = 0$ ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-4|REL Theorem §B4.1.4]]): $\nabla^2e^{i\mathbf p\cdot\mathbf x} = -\mathbf p^2e^{i\mathbf p\cdot\mathbf x}$, so $\int\frac{d^3p}{(2\pi)^3}\bigl(\ddot{\tilde\phi} + (\mathbf p^2 + m^2)\tilde\phi\bigr)e^{i\mathbf p\cdot\mathbf x} = 0$, and uniqueness of the Fourier transform ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]]; in $\mathcal S'$, where the transform is a bijection, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2) gives $\ddot{\tilde\phi} + E_{\mathbf p}^2\tilde\phi = 0$ for each $\mathbf p$. Equivalently, Hamilton's equations for the mode Hamiltonian are $\dot{\tilde\phi} = \tilde\pi$, $\dot{\tilde\pi} = -E_{\mathbf p}^2\tilde\phi$. ⚑ By-product: the field must have a Fourier transform at each time (decay at infinity); plane-wave modes are idealizations → [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]].
>
> **What the derivation shows**
> - The free field decouples into independent oscillators already classically; quantization will only add the ordering of operators, i.e. the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]).
> - The frequency of mode $\mathbf p$ is $E_{\mathbf p}$: the mass shell enters through the gradient and mass terms.
> - Used next: the mode expansion ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]) and the Hamiltonian in mode form ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]]).

^der-c2a-2-1

*Uses:* [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-4|REL Theorem §B4.1.4]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]] (classical preparation)

> [!remark] Remark: Why the modes decouple, and why the frequency is the energy
> - **Decoupling is translation invariance.** The $d^3x$ integral of a product of two fields forces opposite momenta, so $\mathbf p$ meets only $-\mathbf p$, which is the same mode after $\mathbf p \to -\mathbf p$. In position space the gradient term couples each point to its neighbours, which is what stopped $H$ from reading as an oscillator; in momentum space it is just part of the frequency. This is the normal-coordinate decoupling of coupled oscillators ([[§B2.2 Normal-Mode Solutions and Energy Exchange#^thm-b2-2-1|WO Theorem §B2.2.1]]), with plane waves as normal modes because the system is translation invariant.
> - **The frequency is not bookkeeping.** $E_{\mathbf p}^2 = \mathbf p^2 + m^2$ comes from the gradient term ($\mathbf p^2$) and the mass term ($m^2$): a wave equation with a restoring term, $\omega^2 = \omega_p^2 + c^2k^2$ ([[§B6.2 Dispersion, Phase Velocity and Group Velocity#^thm-b6-2-1|WO Theorem §B6.2.1]], 2), with the plasma frequency replaced by $m$ ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]]). It is the mass-shell relation, and it is why the quanta will be relativistic particles.
> - **Counting.** $\tilde\phi(\mathbf p)$ is complex but $\tilde\phi(-\mathbf p) = \tilde\phi^{\ast}(\mathbf p)$, so each pair $\{\mathbf p, -\mathbf p\}$ carries two real oscillators: one per $\mathbf p$. Quantum Mechanics' box version quantizes each pair as a two-dimensional isotropic oscillator ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^def-c13-1-1|QM Def. §C13.1.1]]); the mode expansion of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] does the same bookkeeping with $\hat a_{\mathbf p}$ and $\hat a^\dagger_{-\mathbf p}$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 and §4.6 (Caution "Why the decoupling had to happen")*

^rem-c2a-2-1

Quantization is now "a formality" (the user's notes): quantize each oscillator, $\hat{\tilde\phi}(\mathbf p) \sim (\hat a + \hat a^\dagger)/\sqrt{2E_{\mathbf p}}$, $\hat{\tilde\pi}(\mathbf p) \sim -i\sqrt{E_{\mathbf p}/2}\,(\hat a - \hat a^\dagger)$ (Lecture 4's sketch). The rest of this section, [[§C2a.3 Energy, Momentum and the Zero-Point Energy|§C2a.3]] and [[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] make this precise, and the one thing the quantum computation adds is the operator ordering, hence the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|Remark: Why the zero-point energy is dropped]]). The steps are [[P1 Canonical Quantization#^p1-1|P1, steps 1–4]].

The integration rules used from here on (plane-wave delta function, derivatives under the integral, integration by parts, angular integrals) are in [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorems §CA.3.3]]–[[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|§CA.3.8]], and the interchanges of limits and integrals are licensed by [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]; two rules are specific to mode expansions:

> [!remark] Remark: Two bookkeeping rules for mode integrals
> $$
> \int d^3x\;e^{\mp i(p \pm q)\cdot x} = e^{\mp i(E_{\mathbf p} \pm E_{\mathbf q})t}\,(2\pi)^3\delta^3(\mathbf p \pm \mathbf q) \qquad (p^0 = E_{\mathbf p},\ q^0 = E_{\mathbf q}).
> $$
>
> - **Split exponentials.** A fixed-time $d^3x$ integral touches only the spatial factor, as displayed; the delta then equates the energies, so the phase is $e^{\mp2iE_{\mathbf p}t}$ (for $p + q$) or $1$ (for $p - q$). This is the only place time and space are separated. The delta is an identity in $\mathcal S'$ in $\mathbf p \pm \mathbf q$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]), and moving the phase out of the $\mathbf x$-integral is the exchange of integrals of [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]: exact for wave packets, and for the operator coefficients after smearing them with test functions.
> - **Relabel.** In an integral over all $\mathbf p$ one may substitute $\mathbf p \to -\mathbf p$ in a single term: the Jacobian is $1$ and $E_{-\mathbf p} = E_{\mathbf p}$; only the exponent and the operator index change ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1). Keep the index $-\mathbf p$ on creation operators until the delta has been used, and give the two integration variables of a product different names ($\mathbf p$, $\mathbf q$); a dropped sign turns $[\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p}]$ into $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf p}]$ and produces a $\delta^3(0)$ where none belongs.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.3 (rules 2 and 3 of "The six rules"; Caution "Where the errors live")*

^rem-c2a-2-2

## The mode expansion

> [!theorem] Theorem §C2a.2.2: Mode Expansion of the Real Field
> Every real solution of $(\partial^2 + m^2)\phi = 0$ is
>
> $$
> \phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(a_{\mathbf p}\,e^{-ip\cdot x} + a_{\mathbf p}^*\,e^{ip\cdot x}\Bigr)\Big|_{p^0 = E_{\mathbf p}}, \qquad \pi = \dot\phi = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(a_{\mathbf p}\,e^{-ip\cdot x} - a_{\mathbf p}^*\,e^{ip\cdot x}\Bigr) .
> $$
>
> Accordingly the operators of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] are written at $t = 0$ with operators $\hat a_{\mathbf p}$, $\hat a_{\mathbf p}^\dagger$:
>
> $$
> \hat\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x}, \qquad \hat\pi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.4 · PHY 513 Lecture 4, Part B · PS §2.3, eqs. (2.25)–(2.28) · Yu §2.3.1, eqs. (2.97)–(2.105)*

^thm-c2a-2-2

> [!derivation]- Derivation
> **1. Plane waves.** For $e^{-ik\cdot x}$ with $k\cdot x = k^0t - \mathbf k\cdot\mathbf x$, $\partial_\mu e^{-ik\cdot x} = -ik_\mu e^{-ik\cdot x}$, so
>
> $$
> (\partial^2 + m^2)\,e^{-ik\cdot x} = (-k^2 + m^2)\,e^{-ik\cdot x} ,
> $$
>
> which vanishes iff $k^2 = m^2$, i.e. $k^0 = \pm E_{\mathbf k}$, $E_{\mathbf k} = +\sqrt{\mathbf k^2 + m^2}$ ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]]).
>
> **2. General solution.** Each spatial Fourier mode $e^{i\mathbf k\cdot\mathbf x}$ obeys $\ddot{\tilde\phi} + E_{\mathbf k}^2\tilde\phi = 0$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]]), whose solutions are spanned by $e^{-iE_{\mathbf k}t}$ and $e^{+iE_{\mathbf k}t}$; their two coefficients are fixed by $\tilde\phi(\mathbf k, 0)$ and $\dot{\tilde\phi}(\mathbf k, 0)$. Superposing all $\mathbf k$ (an absolutely convergent integral for Cauchy data whose transforms are wave packets; for operator coefficients see step 7),
>
> $$
> \phi(x) = \int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf k}}}\Bigl(a_{\mathbf k}\,e^{-iE_{\mathbf k}t + i\mathbf k\cdot\mathbf x} + \tilde a_{\mathbf k}\,e^{+iE_{\mathbf k}t + i\mathbf k\cdot\mathbf x}\Bigr) .
> $$
>
> ⚑ By-product: the factor $1/\sqrt{2E_{\mathbf k}}$ is a choice of normalization, not forced here; it is what makes the one-particle states relativistically normalized → [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]. ⚑ By-product: two independent coefficient functions per $\mathbf k$, one per sign of the frequency, matched to the two pieces of Cauchy data $\phi$, $\dot\phi$ → [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], where both survive.
>
> **3. Change of variables in the second term.** Substitute $\mathbf k = -\mathbf p$ in the $\tilde a$ term only: Jacobian $|\det(-\mathbb 1)| = 1$; the domain $\mathbb R^3$ is unchanged; $E_{-\mathbf p} = E_{\mathbf p}$; the exponent becomes $+iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x = +ip\cdot x$ with the same on-shell $p^\mu = (E_{\mathbf p}, \mathbf p)$; the coefficient becomes $\tilde a_{-\mathbf p}$. In the first term rename $\mathbf k \to \mathbf p$ (no change of variables):
>
> $$
> \phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(a_{\mathbf p}\,e^{-ip\cdot x} + \tilde a_{-\mathbf p}\,e^{+ip\cdot x}\Bigr) .
> $$
>
> **4. Reality.** Conjugating, $\phi^{\ast} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(a^{\ast}_{\mathbf p}e^{+ip\cdot x} + \tilde a^{\ast}_{-\mathbf p}e^{-ip\cdot x}\bigr)$. The functions $e^{-ip\cdot x}$ and $e^{+ip\cdot x}$ ($\mathbf p \in \mathbb R^3$) are linearly independent functions of $(t, \mathbf x)$ (at each $t$ the spatial transform is unique in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2, and the time dependences $e^{\mp iE_{\mathbf p}t}$ then separate), so $\phi^{\ast} = \phi$ holds iff the coefficients of $e^{-ip\cdot x}$ agree: $a_{\mathbf p} = \tilde a^{\ast}_{-\mathbf p}$, i.e. $\tilde a_{-\mathbf p} = a^{\ast}_{\mathbf p}$. This gives the first formula of the statement.
>
> **5. The momentum density.** $\pi = \dot\phi$ for this Lagrangian ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]). Differentiate under the integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], the dominating function $E_{\mathbf p}|a_{\mathbf p}|/\sqrt{2E_{\mathbf p}}$ being integrable for wave-packet coefficients; for the quantum field, the derivative of a distribution, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]): $\partial_te^{\mp ip\cdot x} = \mp iE_{\mathbf p}e^{\mp ip\cdot x}$ and $E_{\mathbf p}/\sqrt{2E_{\mathbf p}} = \sqrt{E_{\mathbf p}/2}$:
>
> $$
> \pi = \int\frac{d^3p}{(2\pi)^3}\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(-i\,a_{\mathbf p}e^{-ip\cdot x} + i\,a^*_{\mathbf p}e^{ip\cdot x}\Bigr) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(a_{\mathbf p}e^{-ip\cdot x} - a^*_{\mathbf p}e^{ip\cdot x}\Bigr) .
> $$
>
> **6. Fixed time.** At $t = 0$, $e^{-ip\cdot x} = e^{+i\mathbf p\cdot\mathbf x}$ and $e^{+ip\cdot x} = e^{-i\mathbf p\cdot\mathbf x}$. Substitute $\mathbf p \to -\mathbf p$ in the $a^{\ast}$ terms only ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$, label $a^{\ast}_{\mathbf p} \to a^{\ast}_{-\mathbf p}$, exponent $e^{-i\mathbf p\cdot\mathbf x} \to e^{+i\mathbf p\cdot\mathbf x}$): both terms now carry $e^{i\mathbf p\cdot\mathbf x}$,
>
> $$
> \phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{a_{\mathbf p} + a^*_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}\,e^{i\mathbf p\cdot\mathbf x}, \qquad \pi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(a_{\mathbf p} - a^*_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x} .
> $$
>
> **7. Quantize.** Replace each number $a_{\mathbf p}$ by an operator $\hat a_{\mathbf p}$ and complex conjugation by Hermitian conjugation, $a^{\ast}_{\mathbf p} \to \hat a^\dagger_{\mathbf p}$. In the step-4 form each term of $\hat\phi$ is the adjoint of the other, so $\hat\phi^\dagger = \hat\phi$; likewise $\hat\pi^\dagger = \hat\pi$. ⚑ By-product: Hermiticity is what ties the coefficient of $e^{+ip\cdot x}$ to that of $e^{-ip\cdot x}$; without it the negative-frequency coefficient is a second, independent operator → [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]. ⚑ By-product: with operators in place of numbers the $\mathbf p$-integral converges only after the field is smeared with a test function; $\hat\phi$ and $\hat\pi$ are operator-valued distributions, and the smeared field is $\hat\phi(f) = \hat a(g_f) + \hat a^\dagger(g_f)$ → [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]].
>
> **What the derivation shows**
> - The mass shell $k^0 = \pm E_{\mathbf k}$ is the only input from the field equation; both signs are needed for arbitrary Cauchy data.
> - $1/\sqrt{2E_{\mathbf p}}$ is a normalization choice, cashed in by [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]] and [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]].
> - The relabelling $\mathbf p \to -\mathbf p$ is why $\hat a^\dagger_{-\mathbf p}$, not $\hat a^\dagger_{\mathbf p}$, accompanies $\hat a_{\mathbf p}$ at fixed time: the pairing of $\mathbf p$ with $-\mathbf p$ of [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-1|Remark: Why the modes decouple]].
> - The operators $\hat a_{\mathbf p}$ are so far only names; their algebra is [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], and their extraction from $\hat\phi$, $\hat\pi$ is [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]].

^der-c2a-2-2

*Uses:* [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]], [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!remark] Remark: Posited or derived
> Lecture 4 *posited* the $t = 0$ expansions by copying the oscillator's $\hat x \sim (\hat a + \hat a^\dagger)/\sqrt{2\omega}$, $\hat p \sim -i\sqrt{\omega/2}\,(\hat a - \hat a^\dagger)$ ([[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|Remark: The oscillator, recalled]]) and adding Fourier factors, guided by Hermiticity, then verified them by the commutator ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], second route); $\hat\pi = \dot{\hat\phi}$ was not used. Here $\pi = \dot\phi$ of the classical solution is the input, and the $-i\sqrt{E/2}$ and the relative sign are consequences of $e^{-iEt}$. The two agree because the Heisenberg equation, from the same commutators and $\hat H$, gives back $\hat a_{\mathbf p}(t) = \hat a_{\mathbf p}e^{-iE_{\mathbf p}t}$ and $\partial_t\hat\phi = \hat\pi$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|Remark: Two routes that meet]]): in the lecture's route $\hat\pi = \dot{\hat\phi}$ is a theorem. The user's notes derive the expansion for a complex field first and impose reality at the end ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.4 (Caution "The lecture's route, and why it is sound")*

^rem-c2a-2-3

## The Klein–Gordon inner product

> [!definition] Definition §C2a.2.1: Klein–Gordon Inner Product
> For complex solutions $f$, $g$ of the Klein–Gordon equation,
>
> $$
> (f, g) = i\int d^3x\,\bigl(f^*\,\partial_tg - (\partial_tf^*)\,g\bigr) \equiv i\int d^3x\;f^*\overleftrightarrow{\partial_t}g ,
> $$
>
> evaluated on any time slice; it is antilinear in $f$ and linear in $g$. The **positive-frequency modes** are $f_{\mathbf p}(x) = e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $p^0 = E_{\mathbf p}$; their conjugates $f^{\ast}_{\mathbf p}$ are the negative-frequency modes.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5 · PHY 513 Problem Set 3, Problem 3*

^def-c2a-2-1

> [!theorem] Theorem §C2a.2.3: Conservation and Orthonormality of the Modes
> 1. For solutions $f$, $g$ that fall off at spatial infinity, $(f, g)$ does not depend on $t$, and $(f^*, g^*) = -(f, g)^*$.
> 2. The modes $f_{\mathbf p}$ satisfy
>
> $$
> (f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q), \qquad (f^*_{\mathbf p}, f^*_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q), \qquad (f_{\mathbf p}, f^*_{\mathbf q}) = 0 :
> $$
>
> the product is indefinite, positive on positive frequencies and negative on negative ones.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5, eqs. (KG inner product), (KGortho) · PHY 513 Problem Set 3, Problem 3(a), course solution*

^thm-c2a-2-3

> [!derivation]- Derivation
> **1. The current.** Define $j^\mu(f, g) = i\bigl(f^{\ast}\partial^\mu g - (\partial^\mu f^{\ast})\,g\bigr)$, so that $(f, g) = \int d^3x\,j^0$.
>
> **2. Its divergence.** By the product rule,
>
> $$
> \partial_\mu j^\mu = i\bigl(\partial_\mu f^*\,\partial^\mu g + f^*\,\partial^2g - \partial^2f^*\,g - \partial^\mu f^*\,\partial_\mu g\bigr) = i\bigl(f^*\,\partial^2g - (\partial^2f^*)\,g\bigr) ,
> $$
>
> the first and fourth terms cancelling because $\partial_\mu f^*\partial^\mu g = \partial^\mu f^*\partial_\mu g$ (the metric is symmetric).
>
> **3. Field equation.** $\partial^2g = -m^2g$, and $\partial^2f^{\ast} = -m^2f^{\ast}$ because the Klein–Gordon equation is real. So $\partial_\mu j^\mu = i(-m^2f^{\ast}g + m^2f^{\ast}g) = 0$: the mass terms cancel.
>
> **4. Slice independence.** $\partial_tj^0 = -\nabla\cdot\mathbf j$, so $\frac{d}{dt}(f, g) = -\int d^3x\,\nabla\cdot\mathbf j = -\lim_{R\to\infty}\oint_{|\mathbf x| = R}\mathbf j\cdot d\mathbf S$. ⚑ By-product: the surface term is dropped by assuming $f$, $g$ fall off at spatial infinity (wave packets); for plane waves the statement holds in the distributional sense of step 7 → [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]]; for wave packets it holds with no caveat → [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]].
>
> **5. Conjugation.** $(f, g)^{\ast} = -i\int d^3x\,\bigl(f\,\partial_tg^{\ast} - (\partial_tf)\,g^{\ast}\bigr)$, while $(f^{\ast}, g^{\ast}) = i\int d^3x\,\bigl(f\,\partial_tg^{\ast} - (\partial_tf)\,g^{\ast}\bigr)$ (the conjugate of $f^{\ast}$ is $f$). Hence $(f^{\ast}, g^{\ast}) = -(f, g)^{\ast}$.
>
> **6. The positive-frequency product, before integrating.** With $f^{\ast}_{\mathbf p} = e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $\partial_tf^{\ast}_{\mathbf p} = iE_{\mathbf p}f^{\ast}_{\mathbf p}$ and $\partial_tf_{\mathbf q} = -iE_{\mathbf q}f_{\mathbf q}$:
>
> $$
> (f_{\mathbf p}, f_{\mathbf q}) = i\int d^3x\,\bigl(f^*_{\mathbf p}(-iE_{\mathbf q})f_{\mathbf q} - (iE_{\mathbf p})f^*_{\mathbf p}f_{\mathbf q}\bigr) = \frac{E_{\mathbf p} + E_{\mathbf q}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\int d^3x\;e^{i(p - q)\cdot x} .
> $$
>
> **7. The $d^3x$ integral.** $e^{i(p - q)\cdot x} = e^{i(E_{\mathbf p} - E_{\mathbf q})t}\,e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x}$, and only the spatial factor is integrated ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]). *Sense:* an identity in $\mathcal S'$ in $\mathbf p - \mathbf q$, not a convergent integral ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]), with the time phase moved out by the split-exponential rule ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]); paired with test functions $\overline{g(\mathbf p)}h(\mathbf q)$ it is the convergent computation of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]]:
>
> $$
> \int d^3x\;e^{i(p - q)\cdot x} = e^{i(E_{\mathbf p} - E_{\mathbf q})t}\,(2\pi)^3\delta^3(\mathbf p - \mathbf q) .
> $$
>
> **8. Use the support of the delta.** $F(\mathbf q)\,\delta^3(\mathbf p - \mathbf q) = F(\mathbf p)\,\delta^3(\mathbf p - \mathbf q)$ with $F = \frac{E_{\mathbf p} + E_{\mathbf q}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}e^{i(E_{\mathbf p} - E_{\mathbf q})t}$ (multiplication of a distribution by a smooth function, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1; $F$ is smooth because $E_{\mathbf q}$ is, for $m > 0$), and $F(\mathbf p) = \frac{2E_{\mathbf p}}{2E_{\mathbf p}}\cdot1 = 1$. So $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, at every $t$.
>
> **9. The mixed product.** With $f^{\ast}_{\mathbf q} = e^{iq\cdot x}/\sqrt{2E_{\mathbf q}}$ and $\partial_tf^{\ast}_{\mathbf q} = iE_{\mathbf q}f^{\ast}_{\mathbf q}$,
>
> $$
> (f_{\mathbf p}, f^*_{\mathbf q}) = i\int d^3x\,\bigl(f^*_{\mathbf p}(iE_{\mathbf q})f^*_{\mathbf q} - (iE_{\mathbf p})f^*_{\mathbf p}f^*_{\mathbf q}\bigr) = -\frac{E_{\mathbf q} - E_{\mathbf p}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\,e^{i(E_{\mathbf p} + E_{\mathbf q})t}\,(2\pi)^3\delta^3(\mathbf p + \mathbf q) ,
> $$
>
> using $\int d^3x\,e^{i(p + q)\cdot x} = e^{i(E_{\mathbf p} + E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p + \mathbf q)$. On the support $\mathbf q = -\mathbf p$, $E_{\mathbf q} = E_{-\mathbf p} = E_{\mathbf p}$: the prefactor vanishes, and a smooth function vanishing on the support of $\delta^3$ times $\delta^3$ is the zero distribution ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1; the same identity in $\mathcal S'$, now in $\mathbf p + \mathbf q$). ⚑ By-product: the oscillating phase $e^{2iE_{\mathbf p}t}$ is harmless only because its coefficient vanishes; this is the same cancellation that removes number-changing terms from $\hat H$ → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], steps 10–11.
>
> **10. The negative-frequency product.** By step 5, $(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q}) = -(f_{\mathbf p}, f_{\mathbf q})^{\ast} = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ (the delta is real). ⚑ By-product: the product is not positive definite → [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|Remark: Why this inner product, and why it is indefinite]].
>
> **What the derivation shows**
> - Conservation uses exactly the field equation (step 3) and fall-off at infinity (step 4).
> - The positive- and negative-frequency modes are orthogonal, with norms of opposite sign: the frequency split is basis-free.
> - Used next: extraction of the mode operators ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]]) and the commutator $[\hat a, \hat a^\dagger] = (f, f)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).

^der-c2a-2-3

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]]

> [!theorem] Theorem §C2a.2.4: Orthonormality for Wave Packets
> For $g, h \in \mathcal S(\mathbb R^3)$ let $f_g = \int\frac{d^3p}{(2\pi)^3}\,g(\mathbf p)\,f_{\mathbf p}$ and $f_h$ likewise: positive-frequency solutions that fall off at spatial infinity. Then, every integral converging absolutely, at every $t$,
>
> $$
> (f_g, f_h) = \int\frac{d^3p}{(2\pi)^3}\,\overline{g(\mathbf p)}\,h(\mathbf p), \qquad (f^*_g, f^*_h) = -\int\frac{d^3p}{(2\pi)^3}\,g(\mathbf p)\,\overline{h(\mathbf p)}, \qquad (f_g, f^*_h) = 0 .
> $$
>
> [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 2 is the kernel of these identities: $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ holds in $\mathcal S'(\mathbb R^6)$, as a statement about its pairings with $\overline{g(\mathbf p)}h(\mathbf q)$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5 (Klein–Gordon product) and §4.8 (Caution "Two honesty points": genuine states are wave packets) · stated and proved here for wave packets (standard: Plancherel)*

^thm-c2a-2-4

> [!derivation]- Derivation
> **1. Wave packets are honest solutions.** At time $t$, $f_g(t, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}A(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$ with $A(\mathbf p) = g(\mathbf p)e^{-iE_{\mathbf p}t}/\sqrt{2E_{\mathbf p}}$. For $m > 0$ the functions $E_{\mathbf p}^{\pm1/2}$ and $e^{-iE_{\mathbf p}t}$ are smooth with polynomially bounded derivatives, so $A \in \mathcal S$, and $f_g(t, \cdot)$, its inverse transform, is a Schwartz function of $\mathbf x$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1). The same holds for $\partial_tf_g$, the inverse transform of $-iE_{\mathbf p}A$. So $f_g$ falls off, the surface term of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-3|Derivation §C2a.2.3]], step 4, vanishes, and $(f_g, f_h)$ is the same on every slice. ⚑ By-product: $m > 0$ is used; for $m = 0$, $1/\sqrt{2|\mathbf p|}$ is not smooth at $\mathbf p = \mathbf 0$ → [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] (assumptions).
>
> **2. The positive-frequency product.** Let $B(\mathbf p) = h(\mathbf p)e^{-iE_{\mathbf p}t}/\sqrt{2E_{\mathbf p}}$, so $f_h \leftrightarrow B$ and $\partial_tf_h \leftrightarrow -iE_{\mathbf p}B$. Plancherel, $\int d^3x\,\overline uv = \int\frac{d^3p}{(2\pi)^3}\overline{\tilde u}\,\tilde v$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 3), applied to the two terms of [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]]:
>
> $$
> \int d^3x\,f^*_g\,\partial_tf_h = \int\frac{d^3p}{(2\pi)^3}\,\overline{A}\,(-iE_{\mathbf p})B, \qquad \int d^3x\,(\partial_tf_g)^*\,f_h = \int\frac{d^3p}{(2\pi)^3}\,\overline{(-iE_{\mathbf p}A)}\,B = \int\frac{d^3p}{(2\pi)^3}\,(iE_{\mathbf p})\,\overline AB .
> $$
>
> **3. Combine.** $(f_g, f_h) = i\int\frac{d^3p}{(2\pi)^3}\bigl(-iE_{\mathbf p} - iE_{\mathbf p}\bigr)\overline AB = 2\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\,\overline AB$, and $\overline{A}B = \overline gh\,e^{+iE_{\mathbf p}t}e^{-iE_{\mathbf p}t}/2E_{\mathbf p} = \overline gh/2E_{\mathbf p}$: the phases cancel and $(f_g, f_h) = \int\frac{d^3p}{(2\pi)^3}\overline gh$.
>
> **4. The mixed product.** $f^{\ast}_h = \int\frac{d^3p}{(2\pi)^3}\overline{h(\mathbf p)}e^{iE_{\mathbf p}t}e^{-i\mathbf p\cdot\mathbf x}/\sqrt{2E_{\mathbf p}}$; substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$) to read off its transform $C(\mathbf p) = \overline{h(-\mathbf p)}e^{iE_{\mathbf p}t}/\sqrt{2E_{\mathbf p}}$, with $\partial_tf^{\ast}_h \leftrightarrow iE_{\mathbf p}C$. Then, as in step 2,
>
> $$
> (f_g, f^*_h) = i\int\frac{d^3p}{(2\pi)^3}\Bigl(\overline A\,(iE_{\mathbf p})C - (iE_{\mathbf p})\overline A\,C\Bigr) = 0 ,
> $$
>
> the two terms cancelling identically (the vanishing prefactor $E_{\mathbf q} - E_{\mathbf p}$ of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-3|Derivation §C2a.2.3]], step 9, seen after smearing).
>
> **5. Negative frequencies.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 1, $(f^{\ast}_g, f^{\ast}_h) = -(f_g, f_h)^{\ast} = -\int\frac{d^3p}{(2\pi)^3}g\,\overline h$.
>
> **6. The kernel.** $(f_g, f_h)$ is antilinear in $g$ and linear in $h$, so it equals $\int\frac{d^3p\,d^3q}{(2\pi)^6}\overline{g(\mathbf p)}h(\mathbf q)\,(f_{\mathbf p}, f_{\mathbf q})$ with $(f_{\mathbf p}, f_{\mathbf q})$ the distributional kernel ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]). Inserting $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and pairing it with $\overline g\otimes h$ as in [[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-3|Derivation §C2a.1.3]], step 2, gives $\int\frac{d^3p}{(2\pi)^3}\overline gh$, the result of step 3. So the physicists' computation (exchange the integrals, produce the delta, integrate it) computes the same number as the convergent one ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]).
>
> **What the derivation shows**
> - Wave packets have finite Klein–Gordon norms, $\int\frac{d^3p}{(2\pi)^3}|g|^2 \ge 0$, and conservation holds without caveat; a plane wave is the limit of ever narrower $g$, whose norm diverges like $\delta^3(\mathbf 0)$.
> - "$(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$" is shorthand for these identities; every later use is read this way.
> - Used next: the extraction formula smeared, $\hat a(g) = (f_g, \hat\phi)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-5|Derivation §C2a.2.5]], step 1), and the mode algebra as an identity of distributions ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]).

^der-c2a-2-4

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]

> [!theorem] Theorem §C2a.2.5: Mode Extraction
> For the field of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], written $\hat\phi = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}f_{\mathbf q} + \hat a^\dagger_{\mathbf q}f^*_{\mathbf q}\bigr)$, and with $\partial_t\hat\phi = \hat\pi$,
>
> $$
> \hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\;e^{ip\cdot x}\bigl(\hat\pi(x) - iE_{\mathbf p}\,\hat\phi(x)\bigr), \qquad \hat a^\dagger_{\mathbf p} = -(f^*_{\mathbf p}, \hat\phi) ,
> $$
>
> independent of the time slice on which the integral is taken.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5, eqs. (ainverse), (selection) · PHY 513 Problem Set 3, Problem 3(b), course solution · PS §2.3, p. 21 · Yu §2.3.2, eqs. (2.106)–(2.113)*

^thm-c2a-2-5

> [!derivation]- Derivation
> **1. Pull the inner product through the integral.** $(f_{\mathbf p}, \cdot)$ is linear in its second argument and involves only $\int d^3x$ and $\partial_t$; the operators $\hat a_{\mathbf q}$ do not depend on $x$. *Sense:* the $\mathbf q$-integral has operator coefficients, so the exchange of $\int d^3x$ with $\int d^3q$ is made after smearing in $\mathbf p$ with $\overline{g(\mathbf p)}$, $g \in \mathcal S$: the left side becomes $(f_g, \hat\phi) = i\bigl[\hat\pi(f^{\ast}_g) - \hat\phi(\partial_tf^{\ast}_g)\bigr]$, smeared fields with the Schwartz functions of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-4|Derivation §C2a.2.4]], step 1 ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], extended to complex test functions by linearity), and the exchange is Fubini for wave packets ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]). So, as an identity of operator-valued distributions in $\mathbf p$,
>
> $$
> (f_{\mathbf p}, \hat\phi) = \int\frac{d^3q}{(2\pi)^3}\Bigl(\hat a_{\mathbf q}\,(f_{\mathbf p}, f_{\mathbf q}) + \hat a^\dagger_{\mathbf q}\,(f_{\mathbf p}, f^*_{\mathbf q})\Bigr) .
> $$
>
> **2. Orthonormality.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 2, the second product is $0$ and the first is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; integrating over $\mathbf q$ sets $\mathbf q = \mathbf p$ and cancels the $(2\pi)^3$: $(f_{\mathbf p}, \hat\phi) = \hat a_{\mathbf p}$. Smeared, this reads $(f_g, \hat\phi) = \hat a(g)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]): the extracted mode operator is a combination of smeared fields.
>
> **3. The creation operator.** $-(f^{\ast}_{\mathbf p}, \hat\phi) = -\int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}(f^{\ast}_{\mathbf p}, f_{\mathbf q}) + \hat a^\dagger_{\mathbf q}(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q})\bigr)$. Here $(f^{\ast}_{\mathbf p}, f_{\mathbf q}) = -(f_{\mathbf p}, f^{\ast}_{\mathbf q})^{\ast} = 0$ and $(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, so $-(f^{\ast}_{\mathbf p}, \hat\phi) = \hat a^\dagger_{\mathbf p}$.
>
> **4. Explicit form.** Write out Def. §C2a.2.1 with $f^{\ast}_{\mathbf p} = e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $\partial_tf^{\ast}_{\mathbf p} = iE_{\mathbf p}f^{\ast}_{\mathbf p}$ and $\partial_t\hat\phi = \hat\pi$:
>
> $$
> (f_{\mathbf p}, \hat\phi) = i\int d^3x\,\bigl(f^*_{\mathbf p}\,\hat\pi - iE_{\mathbf p}f^*_{\mathbf p}\,\hat\phi\bigr) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\;e^{ip\cdot x}\bigl(\hat\pi - iE_{\mathbf p}\hat\phi\bigr) .
> $$
>
> **5. Check by direct Fourier inversion (PS, Yu).** At time $t$, with $\hat\phi$ written over $\mathbf q$ and the split rule ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]]; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], an identity in $\mathcal S'$ in $\mathbf p \mp \mathbf q$, the $\mathbf q$-integrals then pairing each delta with the operator-valued distribution $\mathbf q \mapsto \hat a_{\mathbf q}$, valid after smearing in $\mathbf p$; $E_{-\mathbf p} = E_{\mathbf p}$ by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1),
>
> $$
> \int d^3x\,e^{ip\cdot x}\hat\phi(x) = \int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\Bigl(\hat a_{\mathbf q}e^{i(E_{\mathbf p} - E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p - \mathbf q) + \hat a^\dagger_{\mathbf q}e^{i(E_{\mathbf p} + E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p + \mathbf q)\Bigr) = \frac{\hat a_{\mathbf p} + e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}} ,
> $$
>
> the first delta eliminating $\mathbf q = \mathbf p$, the second $\mathbf q = -\mathbf p$ (with $E_{-\mathbf p} = E_{\mathbf p}$). The same computation on $\hat\pi$, whose terms carry $\mp iE_{\mathbf q}$, gives $\int d^3x\,e^{ip\cdot x}\hat\pi = -iE_{\mathbf p}\bigl(\hat a_{\mathbf p} - e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}\bigr)/\sqrt{2E_{\mathbf p}}$. ⚑ By-product: a Fourier transform of $\hat\phi$ alone (or of $\hat\pi$ alone) mixes $\hat a_{\mathbf p}$ with $\hat a^\dagger_{-\mathbf p}$; both pieces of Cauchy data are needed to separate them → [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|Remark: Why this inner product]].
>
> **6. Combine.** $\int d^3x\,e^{ip\cdot x}(\hat\pi - iE_{\mathbf p}\hat\phi) = \frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(-iE_{\mathbf p}\hat a_{\mathbf p} + iE_{\mathbf p}e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p} - iE_{\mathbf p}\hat a_{\mathbf p} - iE_{\mathbf p}e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}\bigr) = -i\sqrt{2E_{\mathbf p}}\,\hat a_{\mathbf p}$: the $\hat a^\dagger_{-\mathbf p}$ terms and with them all $t$-dependence cancel. Multiplying by $i/\sqrt{2E_{\mathbf p}}$ gives $\hat a_{\mathbf p}$, in agreement with step 4.
>
> **What the derivation shows**
> - Extraction is a projection with the Klein–Gordon product; its slice independence ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 1) is why $\hat a_{\mathbf p}$ carries no $t$.
> - The same formula extracts mode operators from any field expanded in any orthonormal set of modes ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-5|★ Remark: Other mode functions]]).
> - Used next: the commutator of two extracted operators ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]); the complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]).

^der-c2a-2-5

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark] Remark: Why this inner product, and why it is indefinite
> - **A projection.** Extracting one coefficient from a superposition is what an inner product does, $c_n = \langle e_n|f\rangle$; the field is a superposition of plane waves with operator coefficients, and $(f_{\mathbf p}, \cdot)$ is the inner product that does it. [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]] is the inversion formula of Peskin–Schroeder and Yu in three symbols.
> - **A Noether charge.** $(f, g)$ is the charge ([[§C1b.5 Noether's Theorem#^def-c1b-5-7|Def. §C1b.5.7]]) of a conserved current, so it is the same on every slice ([[§C1b.5 Noether's Theorem#^thm-c1b-5-6|Theorem §C1b.5.6]]); that is why the extracted $\hat a_{\mathbf p}$ carries no $t$, and why it is the same operator in the Schrödinger and Heisenberg pictures. For $f = g = \phi$ the current is minus the U(1) Noether current of the complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|Caution: Normalization and sign of the charge]]).
> - **Indefinite, and that is the point.** Unlike a Hilbert-space inner product, $(f, f)$ can be negative. Quantum Mechanics met the same density as the would-be probability of a Klein–Gordon wave function and had to give it up for that reason ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]]). In the field theory the sign is the basis-free statement of the positive/negative-frequency split: positive-norm modes carry annihilators, negative-norm modes creators.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5*

^rem-c2a-2-4

> [!remark]- ★ Remark: Other mode functions, Bogoliubov transformations and the vacuum
> Nothing in Theorems §C2a.2.3 and §C2a.2.5 used plane waves except to check the orthonormality relations. Any complete set of solutions $\{u_i\}$ with $(u_i, u_j) = \delta_{ij}$, $(u^{\ast}_i, u^{\ast}_j) = -\delta_{ij}$, $(u_i, u^{\ast}_j) = 0$ gives $\hat\phi = \sum_i(\hat a_iu_i + \hat a_i^\dagger u^{\ast}_i)$ with $\hat a_i = (u_i, \hat\phi)$ and, by the computation of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], $[\hat a_i, \hat a_j^\dagger] = \delta_{ij}$. So a complete set of positive-norm modes *is* a choice of annihilation operators, hence of a vacuum and a Fock space. Two such choices are related by a Bogoliubov transformation, whose mixing is measured by the overlaps $(u_i, \bar u^{\ast}_j) \ne 0$; the two vacua then differ, and for infinitely many modes they can be unitarily inequivalent. In flat space with an inertial time the split by the sign of the frequency is canonical, which is why it can be taken for granted here; for a field in a box or a background it is replaced by the appropriate modes, and in curved spacetime, for accelerated observers (the Unruh effect) or in interacting theories (Haag's theorem) the choice genuinely matters (Wald, *Quantum Field Theory in Curved Spacetime*, Ch. 4; Streater and Wightman).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5 ("The general statement") and §4.8 (Principle "Why |0⟩ is the vacuum")*

^rem-c2a-2-5

## The mode algebra

> [!theorem] Theorem §C2a.2.6: The Mode Algebra
> For the field and momentum of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], the equal-time relations of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] hold if and only if
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q), \qquad [\hat a_{\mathbf p}, \hat a_{\mathbf q}] = [\hat a^\dagger_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = 0 :
> $$
>
> one oscillator algebra per momentum, the $(2\pi)^3$ accompanying the measure $d^3p/(2\pi)^3$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5 · PHY 513 Lecture 4, Part B (⇐ in the lecture, ⇒ in Problem Set 3, Problem 3(c), with the course solutions) · PS §2.3, eqs. (2.29)–(2.30) · Yu §2.3.2, eqs. (2.115)–(2.122)*

^thm-c2a-2-6

> [!derivation]- Derivation (⇒: from the field commutators to the mode algebra)
> **1. The extracted operators.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], on one time slice $t$,
>
> $$
> \hat a_{\mathbf p} = i\int d^3x\,\bigl(f^*_{\mathbf p}(x)\,\hat\pi(\mathbf x) - \dot f^*_{\mathbf p}(x)\,\hat\phi(\mathbf x)\bigr), \qquad \hat a^\dagger_{\mathbf q} = -i\int d^3y\,\bigl(f_{\mathbf q}(y)\,\hat\pi(\mathbf y) - \dot f_{\mathbf q}(y)\,\hat\phi(\mathbf y)\bigr) ,
> $$
>
> the second the adjoint of the first for $\mathbf q$ ($i \to -i$, $f^* \to f$, $\hat\phi$ and $\hat\pi$ Hermitian; the $f$'s are numbers, so the reversed order of factors does not matter).
>
> **2. Expand the commutator into all four terms.** The commutator is bilinear and the $f$'s are numbers; $(i)(-i) = 1$. *Sense:* the four commutators are distributions in $(\mathbf x, \mathbf y)$ ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]), paired here with products of mode functions; plane waves are not test functions, but smeared in $\mathbf p$ and $\mathbf q$ with $\overline{g(\mathbf p)}h(\mathbf q)$ they become the Schwartz functions $f^{\ast}_g(\mathbf x)$, $\partial_tf_h(\mathbf y)$, … of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-4|Derivation §C2a.2.4]], step 1, and every step below is exact:
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = \int d^3x\,d^3y\,\Bigl(f^*_{\mathbf p}f_{\mathbf q}[\hat\pi(\mathbf x), \hat\pi(\mathbf y)] - f^*_{\mathbf p}\dot f_{\mathbf q}[\hat\pi(\mathbf x), \hat\phi(\mathbf y)] - \dot f^*_{\mathbf p}f_{\mathbf q}[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] + \dot f^*_{\mathbf p}\dot f_{\mathbf q}[\hat\phi(\mathbf x), \hat\phi(\mathbf y)]\Bigr) .
> $$
>
> **3. Equal-time relations.** Both operators are taken on the same slice, so [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] applies: $[\hat\pi, \hat\pi] = [\hat\phi, \hat\phi] = 0$ remove the first and last terms; $[\hat\pi(\mathbf x), \hat\phi(\mathbf y)] = -i\delta^3(\mathbf x - \mathbf y)$ and $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$:
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = \int d^3x\,d^3y\,\Bigl(i\,f^*_{\mathbf p}(x)\dot f_{\mathbf q}(y) - i\,\dot f^*_{\mathbf p}(x)f_{\mathbf q}(y)\Bigr)\delta^3(\mathbf x - \mathbf y) .
> $$
>
> **4. Integrate the delta.** The $\mathbf y$ integral sets $\mathbf y = \mathbf x$: the pairing of $\delta^3(\mathbf x - \mathbf y)$ with a product of test functions, [[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-3|Derivation §C2a.1.3]], step 2 (after the smearing of step 2):
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = i\int d^3x\,\bigl(f^*_{\mathbf p}\,\dot f_{\mathbf q} - \dot f^*_{\mathbf p}\,f_{\mathbf q}\bigr) = (f_{\mathbf p}, f_{\mathbf q}) .
> $$
>
> **5. Orthonormality.** $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 2). ⚑ By-product: at $\mathbf q = \mathbf p$ this is $(2\pi)^3\delta^3(\mathbf 0)$, which will appear as the volume in the zero-point energy → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]; as a value it has none (δ at its singular point), and only the box gives it the meaning $V$ → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]. Smeared, the step reads $[\hat a(g), \hat a^\dagger(h)] = (f_g, f_h)$, finite → [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]].
>
> **6. Two annihilators.** With $\hat a_{\mathbf q} = i\int d^3y\,(f^{\ast}_{\mathbf q}\hat\pi - \dot f^{\ast}_{\mathbf q}\hat\phi)$ the prefactor is $(i)(i) = -1$, and the four-term expansion is
>
> $$
> [\hat a_{\mathbf p}, \hat a_{\mathbf q}] = -\int d^3x\,d^3y\,\Bigl(f^*_{\mathbf p}f^*_{\mathbf q}[\hat\pi(\mathbf x), \hat\pi(\mathbf y)] - f^*_{\mathbf p}\dot f^*_{\mathbf q}[\hat\pi(\mathbf x), \hat\phi(\mathbf y)] - \dot f^*_{\mathbf p}f^*_{\mathbf q}[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] + \dot f^*_{\mathbf p}\dot f^*_{\mathbf q}[\hat\phi(\mathbf x), \hat\phi(\mathbf y)]\Bigr) .
> $$
>
> The first and last commutators vanish; the middle two are $-i\delta^3$ and $+i\delta^3$, and the $\mathbf y$ integral sets $\mathbf y = \mathbf x$ (the same pairing as in step 4):
>
> $$
> [\hat a_{\mathbf p}, \hat a_{\mathbf q}] = -\int d^3x\,\bigl(i\,f^*_{\mathbf p}\dot f^*_{\mathbf q} - i\,\dot f^*_{\mathbf p}f^*_{\mathbf q}\bigr) = -(f_{\mathbf p}, f^*_{\mathbf q}) = 0 ,
> $$
>
> the last by [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 2.
>
> **7. Two creators.** $[\hat a_{\mathbf p}, \hat a_{\mathbf q}]^\dagger = (\hat a_{\mathbf p}\hat a_{\mathbf q} - \hat a_{\mathbf q}\hat a_{\mathbf p})^\dagger = \hat a^\dagger_{\mathbf q}\hat a^\dagger_{\mathbf p} - \hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf q} = [\hat a^\dagger_{\mathbf q}, \hat a^\dagger_{\mathbf p}]$, so it vanishes too.
>
> **8. The same in explicit variables.** With the explicit form of Theorem §C2a.2.5, $\hat a_{\mathbf p} = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}(\hat\pi - iE_{\mathbf p}\hat\phi)$ and its adjoint $\hat a^\dagger_{\mathbf q} = \frac{-i}{\sqrt{2E_{\mathbf q}}}\int d^3y\,e^{-iq\cdot y}(\hat\pi + iE_{\mathbf q}\hat\phi)$,
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = \frac{1}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\;e^{ip\cdot x - iq\cdot y}\,\bigl[\hat\pi(\mathbf x) - iE_{\mathbf p}\hat\phi(\mathbf x),\ \hat\pi(\mathbf y) + iE_{\mathbf q}\hat\phi(\mathbf y)\bigr] .
> $$
>
> Of the four terms of the bracket only $iE_{\mathbf q}[\hat\pi(\mathbf x), \hat\phi(\mathbf y)] = iE_{\mathbf q}(-i)\delta^3 = E_{\mathbf q}\delta^3$ and $-iE_{\mathbf p}[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = -iE_{\mathbf p}(i)\delta^3 = E_{\mathbf p}\delta^3$ survive, so the bracket is $(E_{\mathbf p} + E_{\mathbf q})\delta^3(\mathbf x - \mathbf y)$. The $\mathbf y$ integral sets $\mathbf y = \mathbf x$ (step 4) and the $\mathbf x$ integral of $e^{i(p - q)\cdot x}$ (an identity in $\mathcal S'$ in $\mathbf p - \mathbf q$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]) is split as in [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-3|Derivation §C2a.2.3]], step 7:
>
> $$
> [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = \frac{E_{\mathbf p} + E_{\mathbf q}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\,e^{i(E_{\mathbf p} - E_{\mathbf q})t}\,(2\pi)^3\delta^3(\mathbf p - \mathbf q) ,
> $$
>
> which is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ on the support of the delta (Yu eq. (2.115); [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1, the prefactor being smooth). ⚑ By-product: the slice $t$ on which the commutator was computed drops out → [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 1.
>
> **What the derivation shows**
> - The commutator of two extracted operators is the Klein–Gordon product of their mode functions (step 4): the algebra is orthonormality in operator form.
> - Only equal-time relations are used; the result holds whichever slice is chosen.
> - The $\delta^3(\mathbf 0)$ at coincident momenta is the source of the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]).
> - Every step is an identity of distributions in $(\mathbf p, \mathbf q)$; smeared with test functions it becomes an identity between operators ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]).
> - Used next: $\hat H$ and $\hat{\mathbf P}$ in mode form, the ladder relations and the Fock space.

^der-c2a-2-6

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

> [!derivation]- Derivation (second route, ⇐: from the oscillator algebra back to the fields, as in Lecture 4)
> **1. Write both fields.** Use the $t = 0$ forms of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], with integration variable $\mathbf p$ for $\hat\phi(\mathbf x)$ and $\mathbf p'$ for $\hat\pi(\mathbf y)$. Both sides are distributions in $(\mathbf x, \mathbf y)$; paired with $f(\mathbf x)g(\mathbf y)$, $f, g \in \mathcal S$, the exponentials become $\tilde f(-\mathbf p)\,\tilde g(-\mathbf p')$, Schwartz functions, and every integral below converges:
>
> $$
> [\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = \int\frac{d^3p}{(2\pi)^3}\frac{d^3p'}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\mathbf p}}}(-i)\sqrt{\frac{E_{\mathbf p'}}{2}}\;\bigl[\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p},\ \hat a_{\mathbf p'} - \hat a^\dagger_{-\mathbf p'}\bigr]\;e^{i\mathbf p\cdot\mathbf x + i\mathbf p'\cdot\mathbf y} .
> $$
>
> **2. Expand the commutator into all four terms.**
>
> $$
> \bigl[\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p},\ \hat a_{\mathbf p'} - \hat a^\dagger_{-\mathbf p'}\bigr] = [\hat a_{\mathbf p}, \hat a_{\mathbf p'}] - [\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] + [\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] - [\hat a^\dagger_{-\mathbf p}, \hat a^\dagger_{-\mathbf p'}] .
> $$
>
> The first and last vanish. $[\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] = (2\pi)^3\delta^3(\mathbf p + \mathbf p')$ (the mode algebra composed with $\mathbf p' \mapsto -\mathbf p'$, a linear change of variables with Jacobian 1, [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]) and $[\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] = -[\hat a_{\mathbf p'}, \hat a^\dagger_{-\mathbf p}] = -(2\pi)^3\delta^3(\mathbf p + \mathbf p')$. The two surviving terms add: the bracket is $-2(2\pi)^3\delta^3(\mathbf p + \mathbf p')$.
>
> **3. Integrate the delta.** The $\mathbf p'$ integral sets $\mathbf p' = -\mathbf p$ (eliminating $\mathbf p'$; δ acting on the test function $\mathbf p' \mapsto \tilde g(-\mathbf p')\sqrt{E_{\mathbf p'}/2}$ of step 1), cancels one $(2\pi)^3$, turns $E_{\mathbf p'}$ into $E_{\mathbf p}$ and the exponent into $e^{i\mathbf p\cdot(\mathbf x - \mathbf y)}$. The numerical factors are $\frac{1}{\sqrt{2E_{\mathbf p}}}\sqrt{\frac{E_{\mathbf p}}{2}} = \frac12$, times $(-i)$, times $(-2)$, i.e. $+i$:
>
> $$
> [\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\int\frac{d^3p}{(2\pi)^3}\,e^{i\mathbf p\cdot(\mathbf x - \mathbf y)} = i\,\delta^3(\mathbf x - \mathbf y)
> $$
>
> by [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]. *Sense:* an identity in $\mathcal S'$ in $\mathbf x - \mathbf y$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); paired with $f\otimes g$ the middle expression is $i\int\frac{d^3p}{(2\pi)^3}\tilde f(-\mathbf p)\tilde g(\mathbf p) = i\int\frac{d^3p}{(2\pi)^3}\overline{\tilde f(\mathbf p)}\,\tilde g(\mathbf p) = i\int d^3x\,f\,g$ for real $f$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 4, and Plancherel, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 3), which is [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]].
>
> **4. The other two relations.** In $[\hat\phi(\mathbf x), \hat\phi(\mathbf y)]$ the bracket is $[\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'} + \hat a^\dagger_{-\mathbf p'}] = [\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] + [\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] = (2\pi)^3\delta^3(\mathbf p + \mathbf p') - (2\pi)^3\delta^3(\mathbf p + \mathbf p') = 0$. In $[\hat\pi(\mathbf x), \hat\pi(\mathbf y)]$ it is $[\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'} - \hat a^\dagger_{-\mathbf p'}] = -[\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] - [\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] = 0$ likewise.
>
> **What the derivation shows**
> - The relative sign in $\hat\pi$ and the factor $-i\sqrt{E/2}$ are exactly what make the two surviving terms add in step 2 and give $+i$ in step 3: the lecture's ansatz is fixed by the commutator.
> - $[\hat\phi, \hat\phi] = 0$ needs the two orderings to cancel: the first instance of the cancellation that makes the field commutator vanish at spacelike separation ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]).

^der-c2a-2-6b

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark: Two bookkeeping rules]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!definition] Definition §C2a.2.2: Smeared Mode Operators
> For $g \in \mathcal S(\mathbb R^3)$,
>
> $$
> \hat a(g) = \int\frac{d^3p}{(2\pi)^3}\,\overline{g(\mathbf p)}\,\hat a_{\mathbf p}, \qquad \hat a^\dagger(g) = \hat a(g)^\dagger = \int\frac{d^3p}{(2\pi)^3}\,g(\mathbf p)\,\hat a^\dagger_{\mathbf p} :
> $$
>
> $\hat a^\dagger$ is an operator-valued distribution on momentum space ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]), and so is $\hat a$ (antilinear in $g$: $g \mapsto \hat a(\bar g)$ is linear), and $\hat a^\dagger(g)$ creates one quantum in the wave packet $g$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points": $\hat a^\dagger_{\mathbf p}$ is an operator-valued distribution, defined after smearing; the packet operator of "Macroscopic occupation") · standard (Streater & Wightman, Ch. 3)*

^def-c2a-2-2

> [!theorem] Theorem §C2a.2.7: The Mode Algebra Smeared
> For $g, h \in \mathcal S(\mathbb R^3)$:
> 1. $[\hat a(g), \hat a^\dagger(h)] = \int\frac{d^3p}{(2\pi)^3}\,\overline{g(\mathbf p)}\,h(\mathbf p)$ and $[\hat a(g), \hat a(h)] = [\hat a^\dagger(g), \hat a^\dagger(h)] = 0$; [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]] is the kernel of these identities in $\mathcal S'(\mathbb R^6)$.
> 2. On wave-packet states $\hat a_{\mathbf p}$ gives vectors, e.g. $\hat a_{\mathbf p}\,\hat a^\dagger(h)|0\rangle = h(\mathbf p)|0\rangle$; but $\hat a^\dagger_{\mathbf p}|0\rangle$ is not normalizable, and $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf 0)$ has no value.
> 3. For real $f \in \mathcal S(\mathbb R^3)$ the smeared fields of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]] are $\hat\phi(f) = \hat a(g_f) + \hat a^\dagger(g_f)$ and $\hat\pi(f) = -i\bigl(\hat a(h_f) - \hat a^\dagger(h_f)\bigr)$, with $g_f = \tilde f/\sqrt{2E_{\mathbf p}}$ and $h_f = \sqrt{E_{\mathbf p}/2}\,\tilde f$ in $\mathcal S$ (for $m > 0$).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.5 (eq. (aadagger)) and §4.8 (Caution "Two honesty points") · stated and derived here as an identity of distributions (standard: Streater & Wightman, Ch. 3)*

^thm-c2a-2-7

> [!derivation]- Derivation
> **1. Smear the commutator.** By bilinearity and [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]],
>
> $$
> [\hat a(g), \hat a^\dagger(h)] = \int\frac{d^3p\,d^3q}{(2\pi)^6}\,\overline{g(\mathbf p)}\,h(\mathbf q)\,[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] ,
> $$
>
> where $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}]$ is the kernel of the bilinear map $(g, h) \mapsto [\hat a(g), \hat a^\dagger(h)]$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]). Insert $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]) and pair it with $\overline g\otimes h$, changing variables to $\mathbf u = \mathbf p - \mathbf q$, $\mathbf v = \mathbf q$ (Jacobian 1, [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]): the result is $\int\frac{d^3p}{(2\pi)^3}\overline{g(\mathbf p)}h(\mathbf p)$, finite. The other two kernels are $0$. Equivalently, by [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-5|Derivation §C2a.2.5]], step 1, $\hat a(g) = (f_g, \hat\phi)$ and the commutator is $(f_g, f_h)$ of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]].
>
> **2. Annihilators at a point act on wave packets.** $\hat a_{\mathbf p}|0\rangle = 0$, so $\hat a_{\mathbf p}\hat a^\dagger(h)|0\rangle = \int\frac{d^3q}{(2\pi)^3}h(\mathbf q)[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}]|0\rangle = h(\mathbf p)|0\rangle$, δ acting on the test function $h$: a vector for each $\mathbf p$, a Schwartz function of $\mathbf p$.
>
> **3. Creators at a point do not give states.** $\|\hat a^\dagger_{\mathbf p}|0\rangle\|^2 = \langle0|\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p}|0\rangle = [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf 0)$: δ evaluated at its singular point, which has no value ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], 3); in a box it is the volume ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]). By step 1 with $g = h$, $\|\hat a^\dagger(h)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3}|h|^2$, finite. ⚑ By-product: one-particle states are wave packets, and $\hat a^\dagger(h)$ is the operator that makes them → [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]].
>
> **4. Smear the field.** At $t = 0$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]), $\hat\phi(f) = \int d^3x\,f(\mathbf x)\int\frac{d^3p}{(2\pi)^3}\frac{\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}e^{i\mathbf p\cdot\mathbf x}$. Do the $\mathbf x$-integral first (Fubini for the test function $f$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]): $\int d^3x\,f(\mathbf x)e^{i\mathbf p\cdot\mathbf x} = \tilde f(-\mathbf p)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]), so
>
> $$
> \hat\phi(f) = \int\frac{d^3p}{(2\pi)^3}\,\frac{\tilde f(-\mathbf p)}{\sqrt{2E_{\mathbf p}}}\,\bigl(\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}\bigr) .
> $$
>
> **5. Identify the two terms.** $f$ is real, so $\tilde f(-\mathbf p) = \overline{\tilde f(\mathbf p)}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 4): the $\hat a$ term is $\int\frac{d^3p}{(2\pi)^3}\overline{g_f(\mathbf p)}\,\hat a_{\mathbf p} = \hat a(g_f)$. In the $\hat a^\dagger$ term substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$, $\tilde f(-\mathbf p) \to \tilde f(\mathbf p)$, $\hat a^\dagger_{-\mathbf p} \to \hat a^\dagger_{\mathbf p}$): it is $\hat a^\dagger(g_f)$.
>
> **6. The momentum density.** The same two steps with $(-i)\sqrt{E_{\mathbf p}/2}\,(\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p})$ give $\hat\pi(f) = -i\bigl(\hat a(h_f) - \hat a^\dagger(h_f)\bigr)$.
>
> **7. The smearing functions are test functions.** $\tilde f \in \mathcal S$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1), and for $m > 0$ the factors $E_{\mathbf p}^{\pm1/2}$ are smooth with polynomially bounded derivatives, so $g_f, h_f \in \mathcal S$. ⚑ By-product: for $m = 0$, $g_f$ has a $|\mathbf p|^{-1/2}$ singularity at $\mathbf p = \mathbf 0$, still square integrable but not a Schwartz function: the massless field needs more care in the infrared → [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] (assumption $m > 0$).
>
> **8. Check against the canonical relations.** For real $f$, $g$: $[\hat\phi(f), \hat\pi(g)] = [\hat a(g_f) + \hat a^\dagger(g_f), -i\hat a(h_g) + i\hat a^\dagger(h_g)] = i[\hat a(g_f), \hat a^\dagger(h_g)] - i[\hat a^\dagger(g_f), \hat a(h_g)]$, the other two commutators vanishing by part 1. By part 1, $[\hat a^\dagger(g_f), \hat a(h_g)] = -[\hat a(h_g), \hat a^\dagger(g_f)] = -\int\frac{d^3p}{(2\pi)^3}\overline{h_g}\,g_f$, so
>
> $$
> [\hat\phi(f), \hat\pi(g)] = i\int\frac{d^3p}{(2\pi)^3}\Bigl(\overline{g_f}\,h_g + \overline{h_g}\,g_f\Bigr) = \frac i2\int\frac{d^3p}{(2\pi)^3}\Bigl(\overline{\tilde f}\,\tilde g + \overline{\tilde g}\,\tilde f\Bigr) = i\int d^3x\,f\,g ,
> $$
>
> by Plancherel ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 3) for real $f$, $g$: [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], with every integral convergent.
>
> **What the derivation shows**
> - Every relation of the mode algebra is an identity between operators once both labels are smeared; $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is only its kernel.
> - Annihilators at sharp momentum act on wave packets; creators at sharp momentum do not produce states. This asymmetry is why $\langle0|\hat a_{\mathbf q}\hat a^\dagger_{\mathbf p}|0\rangle$ is a distribution and $\langle0|\hat a(g)\hat a^\dagger(h)|0\rangle$ a number.
> - The smeared field is one annihilator plus one creator, smeared with $\tilde f/\sqrt{2E_{\mathbf p}}$; so $\hat\phi(f)|0\rangle = \hat a^\dagger(g_f)|0\rangle$ is a state ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]]).

^der-c2a-2-7

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark]- Connections
> - Each mode carries the oscillator algebra, and its spectrum follows from the algebra alone exactly as for one oscillator; the field adds the continuous label and the $(2\pi)^3\delta^3$ — [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], [[§B4.1 Ladder Operators and the Spectrum#^thm-b4-1-5|QM Theorem §B4.1.5]].
> - The Klein–Gordon inner product is the indefinite density that defeated the single-particle reading of the Klein–Gordon equation; in the field theory its sign separates annihilators from creators — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-2|QM Theorem §C13.1.2]].
> - Extracting a mode by an inner product is Fourier's projection formula for coefficients, with an indefinite product in place of a positive one — [[§B4.1 Fourier Series#^thm-b4-1-2|WO Theorem §B4.1.2]], [[§22 Definition and Examples|556 §22]].
> - The plane-wave delta behind every orthonormality relation and every "$d^3x$ integral" of this section is an identity in $\mathcal S'$, not a convergent integral — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; the computations that use it are Fubini's theorem for wave packets, which also licenses the split-exponential rule — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]].
> - Plancherel's theorem is the wave-packet form of mode orthonormality: the Klein–Gordon product of two packets is the $L^2$ product of their momentum profiles ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]]) — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]; uniqueness of the transform in $\mathcal S'$ reads off coefficients ([[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-2|Derivation §C2a.2.2]], step 4) — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]].
> - Relabelling $\mathbf p \to -\mathbf p$, the trick that pairs $\hat a_{\mathbf p}$ with $\hat a^\dagger_{-\mathbf p}$, is a change of variables with Jacobian 1 — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]; the composition $\delta^3(\mathbf p + \mathbf p')$ is the same change applied to a distribution — [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]].
> - "Use the support of the delta" is multiplication of a distribution by a smooth function: $F(\mathbf q)\delta^3(\mathbf p - \mathbf q) = F(\mathbf p)\delta^3(\mathbf p - \mathbf q)$, and zero when $F$ vanishes there — [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]].
> - $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is one distribution in both momenta, the kernel of the smeared algebra ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]) — [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]; at coincident labels it is δ at its singular point, which only a box turns into a volume — [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].
> - Differentiating the mode integral in $t$ needs a dominating function, available for wave packets — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]].
