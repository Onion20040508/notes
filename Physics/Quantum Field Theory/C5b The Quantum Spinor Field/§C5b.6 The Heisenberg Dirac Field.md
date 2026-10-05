---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
← [[§C5b.5 The U(1) Charge, Particles and Antiparticles]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality]] →

*Sources: PHY 513 Lecture 10 (Larsen, 5 Oct 2026), slide 10 · the user's PHY 513 notes, Ch. 10 §10.3 ("Reading the expansion") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, eqs. (3.99)–(3.104), and §2.4, eqs. (2.44)–(2.47) (the scalar case) · Yu Zhao-Huan, 量子场论讲义, §5.5.2.*

*Draft: Lecture 10 stated only that the field is a Heisenberg operator ("$e^{\mp ipx}$ include time so operators time-dependent"); the theorems below are worked out here from the lecture's results and Peskin–Schroeder; to be revised when the Heisenberg and interaction pictures return (Lecture 13).*

This is the spinor counterpart of [[§C2b.1 Heisenberg Fields|§C2b.1]]. The quantized Dirac field of [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]–[[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]] was written with the time-dependent exponentials $e^{\mp ip\cdot x}$ of the classical solutions; here the time dependence is derived from the quantum Hamiltonian, the Heisenberg equation is shown to be the Dirac equation, and the field is split into its positive- and negative-frequency parts, whose matrix elements are the one-particle wave functions. The two-point functions of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]] are built from this field. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]; the Heisenberg field of a spinor is defined componentwise as in [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]], $\psi_a(t, \mathbf x) = e^{iHt}\psi_a(\mathbf x)e^{-iHt}$.

## Time dependence

> [!theorem] Theorem §C5b.6.1: Time Dependence of the Modes; the Covariant Mode Expansion
> With the Hamiltonian of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]]:
> 1. $e^{iHt}a^s_{\mathbf p}e^{-iHt} = a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$ and $e^{iHt}b^{s\dagger}_{\mathbf p}e^{-iHt} = b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$ (and the adjoints).
> 2. The Heisenberg field ([[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]]) is the expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] with time-independent operators and the exponentials $e^{\mp ip\cdot x}$, $p^0 = E_{\mathbf p}$; at $t = 0$ it is the Schrödinger field.
> 3. The equal-time anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]] hold at every common time $t$.
>
> *Scalar analogue:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]] and part 1 of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]].
> *Source: Lecture 10, slide 10 ("Field in Heisenberg representation") · the user's PHY 513 notes, Ch. 10 §10.3 · PS §3.5, eqs. (3.99), (3.104) · worked out here as in PS §2.4, eqs. (2.46)–(2.47)*

^thm-c5b-6-1

> [!derivation]- Derivation
> **1. A differential equation for the moved operator.** Let $F(t) \equiv e^{iHt}a^s_{\mathbf p}e^{-iHt}$. Differentiating (on wave-packet states, as in [[§C2b.1 Heisenberg Fields#^der-c2b-1-1|Derivation §C2b.1.1]]): $F'(t) = e^{iHt}\,i[H, a^s_{\mathbf p}]\,e^{-iHt}$. By [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], $[H, a^s_{\mathbf p}] = -E_{\mathbf p}a^s_{\mathbf p}$, so $F'(t) = -iE_{\mathbf p}F(t)$.
>
> **2. Solve.** With $F(0) = a^s_{\mathbf p}$: $F(t) = a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$. For $G(t) \equiv e^{iHt}b^{s\dagger}_{\mathbf p}e^{-iHt}$, $[H, b^{s\dagger}_{\mathbf p}] = +E_{\mathbf p}b^{s\dagger}_{\mathbf p}$ gives $G'(t) = +iE_{\mathbf p}G(t)$ and $G(t) = b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$. Adjoints give the other two. ⚑ By-product: it does not matter whether $H$ or $:\!H\!:$ is used; they differ by the constant $E^D_{\mathrm{vac}}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]), which commutes with everything and cancels between $e^{iHt}$ and $e^{-iHt}$.
>
> **3. The field.** The Schrödinger field is the expansion at $t = 0$, $\psi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(a^s_{\mathbf p}u^s(p)e^{i\mathbf p\cdot\mathbf x} + b^{s\dagger}_{\mathbf p}v^s(p)e^{-i\mathbf p\cdot\mathbf x}\bigr)$. The spinors and exponentials are c-numbers and pass through $e^{iHt}\cdots e^{-iHt}$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|§C5b.2, Caution: What anticommutes and what does not]]); by Step 2 the operators acquire $e^{-iE_{\mathbf p}t}$ and $e^{+iE_{\mathbf p}t}$, and $e^{-iE_{\mathbf p}t}e^{i\mathbf p\cdot\mathbf x} = e^{-ip\cdot x}$, $e^{iE_{\mathbf p}t}e^{-i\mathbf p\cdot\mathbf x} = e^{ip\cdot x}$: the expansion of Theorem §C5b.2.1. (The smeared mode operators make the exchange of $e^{iHt}$ with the $\mathbf p$-integral legitimate, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]].)
>
> **4. Equal times.** Insert $\mathbf 1 = e^{-iHt}e^{iHt}$ between the factors: $e^{iHt}\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\}e^{-iHt} = \{\psi_a(t, \mathbf x), \psi^\dagger_b(t, \mathbf y)\}$, while the right side $\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ is a c-number and unchanged; the same for the other two relations. This is Step 1 of [[§C2b.1 Heisenberg Fields#^der-c2b-1-3|Derivation §C2b.1.3]] with braces.
>
> **What the derivation shows**
> - The time dependence that Theorem §C5b.2.1 took from the classical solutions is the one generated by the quantum Hamiltonian: the two agree because $H$ assigns $+E_{\mathbf p}$ to $a^\dagger$ and to $b^\dagger$.
> - Used next: the Heisenberg equation ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]]) and the two-point functions at unequal times ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]).

^der-c5b-6-1

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]

> [!theorem] Theorem §C5b.6.2: The Heisenberg Equation Is the Dirac Equation
> With the equal-time anticommutators ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], 3) and $H = \int d^3y\,\psi^\dagger H_{\text{s.p.}}\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-1|Model §C5b.1.1]]), the Heisenberg equation $i\partial_t\psi_a = [\psi_a, H]$ ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]]) gives $i\partial_t\psi = H_{\text{s.p.}}\psi$, that is the operator Dirac equation
>
> $$
> (i\slashed{\partial} - m)\,\psi(x) = 0 .
> $$
>
> *Scalar analogue:* part 2 of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]].
> *Source: computed here (the fermionic version of PS §2.4, eqs. (2.44)–(2.45)) · the user's PHY 513 notes, Ch. 10 §10.3 ("The quantum field satisfies the Dirac equation")*

^thm-c5b-6-2

> [!derivation]- Derivation
> **1. An identity for a bilinear.** For any operators $A$, $B$, $C$: $[A, BC] = \{A, B\}C - B\{A, C\}$. Expand the right side: $ABC + BAC - BAC - BCA = ABC - BCA$.
>
> **2. Write $H$ as a bilinear.** $H = \int d^3y\,\psi^\dagger_b(\mathbf y)\,C_b(\mathbf y)$ with $C_b \equiv (H_{\text{s.p.}}\psi)_b = \sum_c\bigl[\gamma^0(-i\gamma^j\partial_j + m)\bigr]_{bc}\psi_c$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]]), all at the common time $t$: a linear combination of the $\psi_c(\mathbf y)$ and their spatial derivatives.
>
> **3. The two anticommutators.** $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$. $\{\psi_a(\mathbf x), C_b(\mathbf y)\}$ is the same linear combination of $\{\psi_a(\mathbf x), \psi_c(\mathbf y)\}$ and of its $\mathbf y$-derivatives; since $\{\psi_a(\mathbf x), \psi_c(\mathbf y)\} = 0$ for *all* $\mathbf x$, $\mathbf y$, its derivatives vanish too. Dropped: the second term of Step 1. (Equal times only, as in [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|§C2b.1, Caution: Equal times only]].)
>
> **4. Integrate the delta.** $[\psi_a(\mathbf x), H] = \int d^3y\,\delta_{ab}\delta^3(\mathbf x - \mathbf y)\,C_b(\mathbf y) = C_a(\mathbf x) = (H_{\text{s.p.}}\psi)_a(\mathbf x)$, an identity of operator-valued distributions after smearing in $\mathbf x$ ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]).
>
> **5. The Dirac equation.** $i\partial_t\psi = H_{\text{s.p.}}\psi = \gamma^0(-i\gamma^j\partial_j + m)\psi$. Multiply by $\gamma^0$ on the left, $(\gamma^0)^2 = 1$: $i\gamma^0\partial_0\psi = (-i\gamma^j\partial_j + m)\psi$, i.e. $(i\gamma^\mu\partial_\mu - m)\psi = 0$ — Steps 1–2 of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-1|Derivation §C5b.3.1]] read backwards.
>
> ⚑ By-product: with commutators, $[A, BC] = [A, B]C + B[A, C]$ and the provisional relations of [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-3|§C5b.1, Caution: The provisional commutator quantization]] give the same result → [[§C5b.6 The Heisenberg Dirac Field#^rem-c5b-6-1|Remark: The field equation does not choose the statistics]].
>
> **What the derivation shows**
> - The canonical structure (π = iψ†, H, anticommutators) reproduces the classical field equation as an operator equation, as for the scalar; the mode expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] solves it, which is the "field first" route meeting the "oscillators first" one ([[§C2b.1 Heisenberg Fields#^rem-c2b-1-3|§C2b.1, Remark: Two routes that meet]]).

^der-c5b-6-2

*Uses:* [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-1|Model §C5b.1.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-1|Def. §C5b.1.1]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]

> [!remark] Remark: The field equation does not choose the statistics
> [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]] holds with commutators as well: $[\psi_a, \psi^\dagger_bC_b] = [\psi_a, \psi^\dagger_b]C_b + \psi^\dagger_b[\psi_a, C_b] = \delta_{ab}\delta^3\,C_b + 0$ with the provisional relations. The dynamics is the Dirac equation either way. What decides between commutators and anticommutators is the spectrum ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]) and causality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]), not the equation of motion; this is why Lecture 10 could write down the mode expansion before saying which bracket its oscillators obey ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-1|§C5b.2, Remark: Reading the expansion]]).
>
> *Source: computed here*

^rem-c5b-6-1

## Positive and negative frequency

> [!theorem] Theorem §C5b.6.3: Positive and Negative Frequency; One-Particle Wave Functions
> Split $\psi = \psi^+ + \psi^-$, with $\psi^+$ the $a$ part of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] (positive frequency, $e^{-ip\cdot x}$) and $\psi^-$ the $b^\dagger$ part (negative frequency); likewise $\bar\psi = \bar\psi^+ + \bar\psi^-$ with $\bar\psi^+$ the $b$ part and $\bar\psi^-$ the $a^\dagger$ part ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]). Then $\psi^+|0\rangle = \bar\psi^+|0\rangle = 0$, $\langle0|\psi^- = \langle0|\bar\psi^- = 0$, and for the one-particle states of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]
>
> $$
> \langle0|\psi(x)|\mathbf p, s\rangle = u^s(p)\,e^{-ip\cdot x}, \qquad \langle0|\bar\psi(x)|\mathbf p, s\rangle^c = \bar v^s(p)\,e^{-ip\cdot x} .
> $$
>
> *Scalar analogue:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]].
> *Source: computed here from Theorems §C5b.2.1–§C5b.2.2 and §C5b.4.2 (the spinors $u$, $\bar v$ are the external-line factors of the Feynman rules, PS §4.7, QFT C7, planned)*

^thm-c5b-6-3

> [!derivation]- Derivation
> **1. The vacuum.** $a^s_{\mathbf p}|0\rangle = b^s_{\mathbf p}|0\rangle = 0$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]]), so $\psi^+|0\rangle = 0$ (only $a$'s) and $\bar\psi^+|0\rangle = 0$ (only $b$'s). Taking adjoints, $\langle0|a^{s\dagger}_{\mathbf p} = 0$ and $\langle0|b^{s\dagger}_{\mathbf p} = 0$, so $\langle0|\psi^- = 0$ (only $b^\dagger$'s) and $\langle0|\bar\psi^- = 0$ (only $a^\dagger$'s).
>
> **2. The fermion wave function.** By Step 1 only $\psi^+$ contributes: with variable $\mathbf q$ and label $r$,
>
> $$
> \langle0|\psi(x)|\mathbf p, s\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r u^r(q)\,e^{-iq\cdot x}\,\sqrt{2E_{\mathbf p}}\,\langle0|a^r_{\mathbf q}a^{s\dagger}_{\mathbf p}|0\rangle .
> $$
>
> $\langle0|a^r_{\mathbf q}a^{s\dagger}_{\mathbf p}|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)$ (Step 2 of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^der-c5b-4-2|Derivation §C5b.4.2]]). Integrating the delta sets $\mathbf q = \mathbf p$, $r = s$, and $\sqrt{2E_{\mathbf p}}/\sqrt{2E_{\mathbf q}} = 1$ on its support ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1): $u^s(p)e^{-ip\cdot x}$.
>
> **3. The antifermion wave function.** Only $\bar\psi^+$ contributes: $\int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r\bar v^r(q)e^{-iq\cdot x}\sqrt{2E_{\mathbf p}}\langle0|b^r_{\mathbf q}b^{s\dagger}_{\mathbf p}|0\rangle = \bar v^s(p)e^{-ip\cdot x}$, by the same delta.
>
> **4. Sense.** Both are identities of distributions in $\mathbf p$; for a packet $g$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]]), $\langle0|\psi(x)|g\rangle$ is a smooth positive-frequency solution of the Dirac equation.
>
> **What the derivation shows**
> - The coefficient of the positive-frequency solution destroys a quantum; the coefficient of the negative-frequency solution creates the *antiparticle*. No state of negative energy exists ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^cau-c5b-3-1|§C5b.3, Caution: Negative energies are a problem only if ψ is a wave function]]).
> - The wave function of an antifermion, as seen by the field that annihilates it, is $\bar v^s(p)e^{-ip\cdot x}$: positive frequency, with the spinor $\bar v$.

^der-c5b-6-3

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

> [!remark]- Connections
> - The Heisenberg field of a spinor is translated in time by the same $e^{iHt}$ as the scalar, and in space by $e^{-i\mathbf P\cdot\mathbf x}$; together with the Lorentz covariance of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^rem-c5b-4-1|§C5b.4, Remark: Lorentz covariance of the quantized field]] this is the spinor instance of the quantum Poincaré transformation of fields — [[§C3.4 Quantum Poincaré Transformations#^pr-c3-4-8|Principle §C3.4.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]].
> - The time dependence $a(t) = ae^{-iEt}$ is the single oscillator's in the Heisenberg picture; for a fermionic mode it holds although the mode has only two states — [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]].
> - The positive- and negative-frequency parts are what normal ordering separates, and the vacuum expectation values of their products are the two Wightman functions — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-1|Def. §C5b.7.1]].
> - The identity $[A, BC] = \{A, B\}C - B\{A, C\}$ is the fermionic tool that turns anticommutators into the commutators needed in Heisenberg's equation; its sibling $[AB, C] = A\{B, C\} - \{A, C\}B$ gave the ladder relations — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]].
