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

This is the spinor counterpart of [[§C2b.1 Heisenberg Fields|§C2b.1]]. The quantized Dirac field of [[§C5b.2 Mode Expansion and the Anticommutator Algebra|§C5b.2]]–[[§C5b.4 Fermions, Fock Space and the Pauli Principle|§C5b.4]] was written with the time-dependent exponentials $e^{\mp ip\cdot x}$ of the classical solutions; here the time dependence is derived from the quantum Hamiltonian, the Heisenberg equation is shown to be the Dirac equation, and the field is split into its positive- and negative-frequency parts, whose matrix elements are the one-particle wave functions. The two-point functions of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]] are built from this field. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]; the Heisenberg field of a spinor is defined componentwise as in [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]], $\hat\psi_a(t, \mathbf x) = e^{i\hat Ht}\hat\psi_a(\mathbf x)e^{-i\hat Ht}$.

## Time dependence

> [!theorem] Theorem §C5b.6.1: Time Dependence of the Modes; the Covariant Mode Expansion
> With the Hamiltonian of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]:
> 1. $e^{i\hat Ht}\hat a^s_{\mathbf p}e^{-i\hat Ht} = \hat a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$ and $e^{i\hat Ht}\hat b^{s\dagger}_{\mathbf p}e^{-i\hat Ht} = \hat b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$ (and the adjoints).
> 2. The Heisenberg field ([[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]]) is the expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] with time-independent operators and the exponentials $e^{\mp ip\cdot x}$, $p^0 = E_{\mathbf p}$; at $t = 0$ it is the Schrödinger field.
> 3. The equal-time anticommutators of [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] hold at every common time $t$.
>
> *Scalar analogue:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]] and [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]].
> *Source: Lecture 10, slide 10 ("Field in Heisenberg representation") · the user's PHY 513 notes, Ch. 10 §10.3 · PS §3.5, eqs. (3.99), (3.104) · worked out here as in PS §2.4, eqs. (2.46)–(2.47)*

^thm-c5b-6-1

> [!derivation]- Derivation
> **1. A differential equation for the moved operator.** Let $\hat F(t) \equiv e^{i\hat Ht}\hat a^s_{\mathbf p}e^{-i\hat Ht}$. Differentiating (on wave-packet states, as in [[§C2b.1 Heisenberg Fields#^der-c2b-1-4|Derivation §C2b.1.4]]): $\hat F'(t) = e^{i\hat Ht}\,i[\hat H, \hat a^s_{\mathbf p}]\,e^{-i\hat Ht}$. By [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]], $[\hat H, \hat a^s_{\mathbf p}] = -E_{\mathbf p}\hat a^s_{\mathbf p}$, so $\hat F'(t) = -iE_{\mathbf p}\hat F(t)$.
>
> **2. Solve.** With $\hat F(0) = \hat a^s_{\mathbf p}$: $\hat F(t) = \hat a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$. For $\hat G(t) \equiv e^{i\hat Ht}\hat b^{s\dagger}_{\mathbf p}e^{-i\hat Ht}$, $[\hat H, \hat b^{s\dagger}_{\mathbf p}] = +E_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$ gives $\hat G'(t) = +iE_{\mathbf p}\hat G(t)$ and $\hat G(t) = \hat b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$. Adjoints give the other two. ⚑ By-product: it does not matter whether $\hat H$ or $:\!\hat H\!:$ is used; they differ by the constant $E_0^{(\rm D)}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]]), which commutes with everything and cancels between $e^{i\hat Ht}$ and $e^{-i\hat Ht}$.
>
> **3. The field.** The Schrödinger field is the expansion at $t = 0$, $\hat\psi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^s_{\mathbf p}u^s(p)e^{i\mathbf p\cdot\mathbf x} + \hat b^{s\dagger}_{\mathbf p}v^s(p)e^{-i\mathbf p\cdot\mathbf x}\bigr)$. The spinors and exponentials are c-numbers and pass through $e^{i\hat Ht}\cdots e^{-i\hat Ht}$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|§C5b.2, Caution: What anticommutes and what does not]]); by Step 2 the operators acquire $e^{-iE_{\mathbf p}t}$ and $e^{+iE_{\mathbf p}t}$, and $e^{-iE_{\mathbf p}t}e^{i\mathbf p\cdot\mathbf x} = e^{-ip\cdot x}$, $e^{iE_{\mathbf p}t}e^{-i\mathbf p\cdot\mathbf x} = e^{ip\cdot x}$: the expansion of Theorem §C5b.2.1. (The smeared mode operators make the exchange of $e^{i\hat Ht}$ with the $\mathbf p$-integral legitimate, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]].)
>
> **4. Equal times.** Insert $\mathbf 1 = e^{-i\hat Ht}e^{i\hat Ht}$ between the factors: $e^{i\hat Ht}\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\}e^{-i\hat Ht} = \{\hat\psi_a(t, \mathbf x), \hat\psi^\dagger_b(t, \mathbf y)\}$, while the right side $\delta_{ab}\delta^3(\mathbf x - \mathbf y)$ is a c-number and unchanged; the same for the other two relations. This is Step 1 of [[§C2b.1 Heisenberg Fields#^der-c2b-1-2|Derivation §C2b.1.2]] with braces.
>
> **What the derivation shows**
> - The time dependence that Theorem §C5b.2.1 took from the classical solutions is the one generated by the quantum Hamiltonian: the two agree because $\hat H$ assigns $+E_{\mathbf p}$ to $\hat a^\dagger$ and to $\hat b^\dagger$.
> - Used next: the Heisenberg equation ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]]) and the two-point functions at unequal times ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]).

^der-c5b-6-1

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]

> [!theorem] Theorem §C5b.6.2: The Heisenberg Equation Is the Dirac Equation
> With the equal-time anticommutators ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], 3) and $\hat H = \int d^3y\,\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]), the Heisenberg equation $i\partial_t\hat\psi_a = [\hat\psi_a, \hat H]$ ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]]) gives $i\partial_t\hat\psi = H_{\text{s.p.}}\hat\psi$, that is the operator Dirac equation
>
> $$
> (i\slashed{\partial} - m)\,\hat\psi(x) = 0 .
> $$
>
> *Scalar analogue:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]].
> *Source: computed here (the fermionic version of PS §2.4, eqs. (2.44)–(2.45)) · the user's PHY 513 notes, Ch. 10 §10.3 ("The quantum field satisfies the Dirac equation")*

^thm-c5b-6-2

> [!derivation]- Derivation
> **1. An identity for a bilinear.** For any operators $A$, $B$, $C$: $[A, BC] = \{A, B\}C - B\{A, C\}$. Expand the right side: $ABC + BAC - BAC - BCA = ABC - BCA$.
>
> **2. Write $\hat H$ as a bilinear.** $\hat H = \int d^3y\,\hat\psi^\dagger_b(\mathbf y)\,\hat C_b(\mathbf y)$ with $\hat C_b \equiv (H_{\text{s.p.}}\hat\psi)_b = \sum_c\bigl[\gamma^0(-i\gamma^j\partial_j + m)\bigr]_{bc}\hat\psi_c$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-4|Def. §C5a.3.4]]), all at the common time $t$: a linear combination of the $\hat\psi_c(\mathbf y)$ and their spatial derivatives.
>
> **3. The two anticommutators.** $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$. $\{\hat\psi_a(\mathbf x), \hat C_b(\mathbf y)\}$ is the same linear combination of $\{\hat\psi_a(\mathbf x), \hat\psi_c(\mathbf y)\}$ and of its $\mathbf y$-derivatives; since $\{\hat\psi_a(\mathbf x), \hat\psi_c(\mathbf y)\} = 0$ for *all* $\mathbf x$, $\mathbf y$, its derivatives vanish too. Dropped: the second term of Step 1. (Equal times only, as in [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|§C2b.1, Caution: Equal times only]].)
>
> **4. Integrate the delta.** $[\hat\psi_a(\mathbf x), \hat H] = \int d^3y\,\delta_{ab}\delta^3(\mathbf x - \mathbf y)\,\hat C_b(\mathbf y) = \hat C_a(\mathbf x) = (H_{\text{s.p.}}\hat\psi)_a(\mathbf x)$, an identity of operator-valued distributions after smearing in $\mathbf x$ ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]).
>
> **5. The Dirac equation.** $i\partial_t\hat\psi = H_{\text{s.p.}}\hat\psi = \gamma^0(-i\gamma^j\partial_j + m)\hat\psi$. Multiply by $\gamma^0$ on the left, $(\gamma^0)^2 = 1$: $i\gamma^0\partial_0\hat\psi = (-i\gamma^j\partial_j + m)\hat\psi$, i.e. $(i\gamma^\mu\partial_\mu - m)\hat\psi = 0$ — Steps 1–2 of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-1|Derivation §C5b.3.1]] read backwards.
>
> ⚑ By-product: with commutators, $[A, BC] = [A, B]C + B[A, C]$ and the provisional relations of [[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-2|§C5b.1, Caution: The provisional commutator quantization]] give the same result → [[§C5b.6 The Heisenberg Dirac Field#^rem-c5b-6-1|Remark: The field equation does not choose the statistics]].
>
> **What the derivation shows**
> - The canonical structure ($\hat\pi = i\hat\psi^\dagger$, $\hat H$, anticommutators) reproduces the classical field equation as an operator equation, as for the scalar; the mode expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] solves it, which is the "field first" route meeting the "oscillators first" one ([[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|§C2b.1, Remark: Two routes that meet]]).

^der-c5b-6-2

*Uses:* [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-4|Def. §C5a.3.4]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]

> [!remark] Remark: The field equation does not choose the statistics
> [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]] holds with commutators as well: $[\hat\psi_a, \hat\psi^\dagger_b\hat C_b] = [\hat\psi_a, \hat\psi^\dagger_b]\hat C_b + \hat\psi^\dagger_b[\hat\psi_a, \hat C_b] = \delta_{ab}\delta^3\,\hat C_b + 0$ with the provisional relations. The dynamics is the Dirac equation either way. What decides between commutators and anticommutators is the spectrum ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]) and causality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]), not the equation of motion; this is why Lecture 10 could write down the mode expansion before saying which bracket its oscillators obey ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-1|§C5b.2, Remark: Reading the expansion]]).
>
> *Source: computed here*

^rem-c5b-6-1

## Positive and negative frequency

> [!theorem] Theorem §C5b.6.3: Positive and Negative Frequency; One-Particle Wave Functions
> Split $\hat\psi = \hat\psi^+ + \hat\psi^-$, with $\hat\psi^+$ the $\hat a$ part of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] (positive frequency, $e^{-ip\cdot x}$) and $\hat\psi^-$ the $\hat b^\dagger$ part (negative frequency); likewise $\hat{\bar\psi} = \hat{\bar\psi}^+ + \hat{\bar\psi}^-$ with $\hat{\bar\psi}^+$ the $\hat b$ part and $\hat{\bar\psi}^-$ the $\hat a^\dagger$ part ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]). Then $\hat\psi^+|0\rangle = \hat{\bar\psi}^+|0\rangle = 0$, $\langle0|\hat\psi^- = \langle0|\hat{\bar\psi}^- = 0$, and for the one-particle states of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]
>
> $$
> \langle0|\hat\psi(x)|\mathbf p, s\rangle = u^s(p)\,e^{-ip\cdot x}, \qquad \langle0|\hat{\bar\psi}(x)|\mathbf p, s\rangle^c = \bar v^s(p)\,e^{-ip\cdot x} .
> $$
>
> *Scalar analogue:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]].
> *Source: computed here from Theorems §C5b.2.1–§C5b.2.2 and §C5b.4.1 (the spinors $u$, $\bar v$ are the external-line factors of the Feynman rules, PS §4.7, QFT C7, planned)*

^thm-c5b-6-3

> [!derivation]- Derivation
> **1. The vacuum.** $\hat a^s_{\mathbf p}|0\rangle = \hat b^s_{\mathbf p}|0\rangle = 0$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]]), so $\hat\psi^+|0\rangle = 0$ (only $\hat a$'s) and $\hat{\bar\psi}^+|0\rangle = 0$ (only $\hat b$'s). Taking adjoints, $\langle0|\hat a^{s\dagger}_{\mathbf p} = 0$ and $\langle0|\hat b^{s\dagger}_{\mathbf p} = 0$, so $\langle0|\hat\psi^- = 0$ (only $\hat b^\dagger$'s) and $\langle0|\hat{\bar\psi}^- = 0$ (only $\hat a^\dagger$'s).
>
> **2. The fermion wave function.** By Step 1 only $\hat\psi^+$ contributes: with variable $\mathbf q$ and label $r$,
>
> $$
> \langle0|\hat\psi(x)|\mathbf p, s\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r u^r(q)\,e^{-iq\cdot x}\,\sqrt{2E_{\mathbf p}}\,\langle0|\hat a^r_{\mathbf q}\hat a^{s\dagger}_{\mathbf p}|0\rangle .
> $$
>
> $\langle0|\hat a^r_{\mathbf q}\hat a^{s\dagger}_{\mathbf p}|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)$ (Step 2 of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^der-c5b-4-1|Derivation §C5b.4.1]]). Integrating the delta sets $\mathbf q = \mathbf p$, $r = s$, and $\sqrt{2E_{\mathbf p}}/\sqrt{2E_{\mathbf q}} = 1$ on its support ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1): $u^s(p)e^{-ip\cdot x}$.
>
> **3. The antifermion wave function.** Only $\hat{\bar\psi}^+$ contributes: $\int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r\bar v^r(q)e^{-iq\cdot x}\sqrt{2E_{\mathbf p}}\langle0|\hat b^r_{\mathbf q}\hat b^{s\dagger}_{\mathbf p}|0\rangle = \bar v^s(p)e^{-ip\cdot x}$, by the same delta.
>
> **4. Sense.** Both are identities of distributions in $\mathbf p$; for a packet $g$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-3|Def. §C2a.4.3]]), $\langle0|\hat\psi(x)|g\rangle$ is a smooth positive-frequency solution of the Dirac equation.
>
> **What the derivation shows**
> - The coefficient of the positive-frequency solution destroys a quantum; the coefficient of the negative-frequency solution creates the *antiparticle*. No state of negative energy exists ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^cau-c5b-3-1|§C5b.3, Caution: Negative energies are a problem only if ψ is a wave function]]).
> - The wave function of an antifermion, as seen by the field that annihilates it, is $\bar v^s(p)e^{-ip\cdot x}$: positive frequency, with the spinor $\bar v$.

^der-c5b-6-3

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

> [!remark]- Connections
> - The Heisenberg field of a spinor is translated in time by the same $e^{i\hat Ht}$ as the scalar, and in space by $e^{-i\hat{\mathbf P}\cdot\mathbf x}$; together with the Lorentz covariance of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^rem-c5b-4-1|§C5b.4, Remark: Lorentz covariance of the quantized field]] this is the spinor instance of the quantum Poincaré transformation of fields — [[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8|Principle §C3.5.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]].
> - The time dependence $\hat a(t) = \hat a e^{-iEt}$ is the single oscillator's in the Heisenberg picture; for a fermionic mode it holds although the mode has only two states — [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]].
> - The positive- and negative-frequency parts are what normal ordering separates, and the vacuum expectation values of their products are the two Wightman functions — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-1|Def. §C5b.7.1]].
> - The identity $[A, BC] = \{A, B\}C - B\{A, C\}$ is the fermionic tool that turns anticommutators into the commutators needed in Heisenberg's equation; its sibling $[AB, C] = A\{B, C\} - \{A, C\}B$ gave the ladder relations — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]].
