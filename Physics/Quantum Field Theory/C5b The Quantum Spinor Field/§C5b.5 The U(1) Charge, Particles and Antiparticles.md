---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
← [[§C5b.4 Fermions, Fock Space and the Pauli Principle]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.6 The Heisenberg Dirac Field]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 54, 57, 61–62 · Yu Zhao-Huan, 量子场论讲义, §5.5.1, §5.5.3 · the user's pre-course notes, §5.5 · the user's PHY 513 notes, Ch. 10 §10.3 and §10.6 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), transcript.*

*Draft: Peskin–Schroeder §3.5 material (the reading for Lecture 10) that the lecture itself did not cover, except [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-2|Remark: Destroying a particle is not creating an antiparticle]] and the pairing of $a$ with $b^\dagger$ by charge; to be revised after Lecture 12 (charge conjugation).*

This is the spinor counterpart of [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]]: the Dirac field is complex, and like the complex scalar it has a conserved U(1) charge that distinguishes its two species. Classically the two fields have opposite pathologies — the complex scalar a positive energy and an indefinite charge, the Dirac field an indefinite energy and a positive charge density — and quantization with the matching statistics makes them alike: positive energy for both species, charge $+1$ for particles and $-1$ for antiparticles. The ordering of the charge is not a convention, since a vacuum charge would be observable. The section ends with the field reading of Dirac's sea. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

## The charge

The current has its home in Chapter C5a, where its conservation follows from the two Dirac equations (and from Noether's theorem for the phase symmetry); it is shown here as it stands there:

![[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9]]

Its charge, read as an operator, is the following.

> [!definition] Definition §C5b.5.1: The U(1) Charge of the Dirac Field
> The **charge** of the Dirac field is the space integral of the time component of the vector current $j^\mu = \bar\psi\gamma^\mu\psi$ of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]],
>
> $$
> Q \equiv \int d^3x\;\bar\psi\gamma^0\psi = \int d^3x\;\psi^\dagger\psi ,
> $$
>
> normalized as in PS; the Noether charge of $\psi \to e^{i\alpha}\psi$ in the sign convention of [[§C1b.5 Noether's Theorem#^cau-c1b-5-3|§C1b.5, Caution: Sign and normalization of the U(1) current]] is $-Q$. The electric charge is $Q$ times the charge of the fermion. As an operator, $Q$ is fixed only once its ordering is ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]]).
>
> *Scalar analogue:* [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]].
> *Source: PS §3.5, p. 62, eq. (3.113) · Yu §5.5.3, eqs. (5.264)–(5.267) · the user's pre-course notes, §5.5 ("$U(1)$ global symmetry")*

^def-c5b-5-1

> [!theorem] Theorem §C5b.5.1: The Charge in Modes, before Any Algebra
> For the charge $Q = \int d^3x\,\psi^\dagger\psi$ of [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|Def. §C5b.5.1]], the expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] gives, in the order as it arises,
>
> $$
> Q = \sum_s\int\frac{d^3p}{(2\pi)^3}\Bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} + b^s_{\mathbf p}b^{s\dagger}_{\mathbf p}\Bigr) .
> $$
>
> *Scalar analogue:* the charge of the complex field before reordering, in [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]].
> *Source: PS §3.5, p. 62 (first form of eq. (3.113)) · Yu §5.5.3, eqs. (5.264)–(5.267)*

^thm-c5b-5-1

> [!derivation]- Derivation
> **1. Differences from Derivation §C5b.3.2.** Replace $H_{\text{s.p.}}\psi$ by $\psi$: in Step 1 of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-2|Derivation §C5b.3.2]] the factor $E_{\mathbf q}$ becomes $1$ and the minus sign in front of the $b^\dagger$ term becomes a plus. Steps 2–4 then give
>
> $$
> Q = \int\frac{d^3p}{(2\pi)^3}\,\frac{1}{2E_{\mathbf p}}\sum_{s,r}\Bigl[u^{s\dagger}(p)u^r(p)\,a^{s\dagger}_{\mathbf p}a^r_{\mathbf p} + v^{s\dagger}(p)v^r(p)\,b^s_{\mathbf p}b^{r\dagger}_{\mathbf p} + u^{s\dagger}(p)v^r(\tilde p)\,a^{s\dagger}_{\mathbf p}b^{r\dagger}_{-\mathbf p}e^{2iE_{\mathbf p}t} + v^{s\dagger}(p)u^r(\tilde p)\,b^s_{\mathbf p}a^r_{-\mathbf p}e^{-2iE_{\mathbf p}t}\Bigr] .
> $$
>
> **2. Orthogonality and normalization.** The last two terms vanish by [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]; the first two give $2E_{\mathbf p}\delta^{rs}$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-3|Theorem §C5a.6.3]]), which cancels the $1/2E_{\mathbf p}$.
>
> **What the derivation shows**
> - Where $H$ had a relative minus sign between the species, $Q$ has a plus: the positive density $\psi^\dagger\psi$ in modes.

^der-c5b-5-1

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-2|Derivation §C5b.3.2]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-6|Theorem §C5a.6.6]]

> [!theorem] Theorem §C5b.5.2: The Classical Dirac Energy Is Unbounded Below; the Classical Charge Is Positive
> For a classical Dirac field with c-number amplitudes $a^s, b^s \in \mathcal S(\mathbb R^3)$ in the expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], with $H$ and $Q$ of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]] and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]],
>
> $$
> H = \sum_s\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\bigl(|a^s_{\mathbf p}|^2 - |b^s_{\mathbf p}|^2\bigr), \qquad Q = \sum_s\int\frac{d^3p}{(2\pi)^3}\bigl(|a^s_{\mathbf p}|^2 + |b^s_{\mathbf p}|^2\bigr) = \int d^3x\,\psi^\dagger\psi \ge 0 :
> $$
>
> $H$ takes every real value and is unbounded below; $Q$ vanishes only for $\psi = 0$. These are the negative energies and the positive density of the Dirac equation of Quantum Mechanics ([[§C13.2★ The Dirac Equation#^thm-c13-2-2|QM Theorem §C13.2.2]], [[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]), now for the classical field.
>
> *Source: PS §3.5, p. 54 (after eq. (3.90)) · Yu §5.5.1, after eq. (5.237) · the user's pre-course notes, §5.4 (end) and §5.5*

^thm-c5b-5-2

> [!derivation]- Derivation
> **1. c-numbers commute.** For complex amplitudes $b^sb^{s\ast} = |b^s|^2$, so [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]] and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]] become the displayed integrals (absolutely convergent for Schwartz amplitudes).
>
> **2. Unbounded below.** Take $a = 0$ and $b^1 = \lambda g$ with $g \ne 0$: $H = -\lambda^2\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}|g|^2 \to -\infty$ as $\lambda \to \infty$. With $b = 0$, $H$ is as large as one likes; by continuity in $\lambda$ every real value occurs.
>
> **3. Positive charge.** $Q$ is a sum of squares; it is $\int d^3x\,\psi^\dagger\psi$ by its definition, and vanishes only if every amplitude does, i.e. $\psi = 0$ (Plancherel, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]).
>
> **What the derivation shows**
> - Classically the Dirac field has the opposite pathology from the complex scalar, whose charge was indefinite and energy positive ([[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-3|§C2a.5, Remark: Charge, not probability]]). Quantization has to exchange the two roles.

^der-c5b-5-2

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]]

> [!theorem] Theorem §C5b.5.3: The Charge Counts Fermions Minus Antifermions
> The normal-ordered charge ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]) of the current of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-9|Theorem §C5a.4.9]] is
>
> $$
> Q = \int d^3x\;:\!\psi^\dagger\psi\!: \; = \sum_s\int\frac{d^3p}{(2\pi)^3}\bigl(a^{s\dagger}_{\mathbf p}a^s_{\mathbf p} - b^{s\dagger}_{\mathbf p}b^s_{\mathbf p}\bigr) = N_a - N_b ,
> $$
>
> conserved, $[Q, H] = [Q, \mathbf P] = 0$. Without normal ordering $Q$ would contain the constant $+2V\int\frac{d^3p}{(2\pi)^3}$ (normalization and sign as in [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|Def. §C5b.5.1]]; electric charge = $Q$ times the charge of the fermion).
>
> *Scalar analogue:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]].
> *Source: PS §3.5, eq. (3.113) · Yu §5.5.3, eq. (5.267) (with $q = 1$) · the user's pre-course notes, §5.5 ("$U(1)$ global symmetry")*

^thm-c5b-5-3

> [!derivation]- Derivation
> **1. Unreordered form.** $\int d^3x\,\psi^\dagger\psi = \sum_s\int\frac{d^3p}{(2\pi)^3}(a^{s\dagger}a^s + b^sb^{s\dagger})$ ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]]).
>
> **2. Reorder.** $b^sb^{s\dagger} = -b^{s\dagger}b^s + (2\pi)^3\delta^3(\mathbf 0)$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]): $\int\psi^\dagger\psi = \sum_s\int(a^{s\dagger}a^s - b^{s\dagger}b^s) + 2V\int\frac{d^3p}{(2\pi)^3}$. ⚑ By-product: a positive infinite vacuum charge (in the box, $+2\mathcal N(V, \Lambda)$, two per momentum cell) → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-1|Remark: The vacuum charge, and why the order is forced]]. Normal ordering drops it ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]).
>
> **3. Conservation.** $Q$, $:\!H\!:$ and $\mathbf P$ are integrals of the number densities $a^{s\dagger}_{\mathbf p}a^s_{\mathbf p}$, $b^{s\dagger}_{\mathbf p}b^s_{\mathbf p}$. These commute with each other. By the Leibniz rule $[AB, X] = A[B, X] + [A, X]B$ and the identity $[X, CD] = \{X, C\}D - C\{X, D\}$ (expand: $XCD - CDX = XCD + CXD - CXD - CDX$), $[a^\dagger_{\mathbf p}a_{\mathbf p}, a^\dagger_{\mathbf q}a_{\mathbf q}] = a^\dagger_{\mathbf p}[a_{\mathbf p}, a^\dagger_{\mathbf q}a_{\mathbf q}] + [a^\dagger_{\mathbf p}, a^\dagger_{\mathbf q}a_{\mathbf q}]a_{\mathbf p} = a^\dagger_{\mathbf p}\{a_{\mathbf p}, a^\dagger_{\mathbf q}\}a_{\mathbf q} - a^\dagger_{\mathbf q}\{a^\dagger_{\mathbf p}, a_{\mathbf q}\}a_{\mathbf p}$ (other anticommutators zero) $= (2\pi)^3\delta^3(\mathbf p - \mathbf q)(a^\dagger_{\mathbf p}a_{\mathbf q} - a^\dagger_{\mathbf q}a_{\mathbf p}) = 0$ on the support of δ; across species the anticommutators vanish. So $[Q, H] = [Q, \mathbf P] = 0$.
>
> **What the derivation shows**
> - Classically $\int\psi^\dagger\psi \ge 0$ ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]]); the reordering sign makes the antifermions count negatively. The roles of $H$ and $Q$ are now those of the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]]).

^der-c5b-5-3

*Uses:* [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-4|Theorem §C5b.3.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!remark] Remark: The vacuum charge, and why the order is forced
> As for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]]), an ordering constant in the charge would be observable: the unordered $\int\psi^\dagger\psi$ gives the vacuum the charge $+2V\int\frac{d^3p}{(2\pi)^3}$ (Yu's "zero-point charge", eq. (5.267)), of the opposite sign to the scalar's. The vacuum must be neutral, so the order is fixed by physics. Normal ordering achieves it; so does the antisymmetrized density $\frac12[\psi^\dagger_a, \psi_a]$ (summed over $a$): in modes $\psi_a\psi^\dagger_a$ gives $aa^\dagger + b^\dagger b$ where $\psi^\dagger_a\psi_a$ gave $a^\dagger a + bb^\dagger$, and $\frac12\bigl[(a^\dagger a + bb^\dagger) - (aa^\dagger + b^\dagger b)\bigr] = a^\dagger a - b^\dagger b$ with the constants cancelling (computed here). The positive density of the Dirac equation ([[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]]) thus becomes, after quantization, a charge density with eigenvalues of both signs: rule 2, the same density with a new meaning.
>
> *Source: Yu §5.5.3, eq. (5.267) · the user's pre-course notes, §5.5 (Remark "Antiparticles without hole theory": "$Q/q$ counts particles minus antiparticles")*

^rem-c5b-5-1

## Particles and antiparticles

> [!theorem] Theorem §C5b.5.4: Particles and Antiparticles Carry Opposite Charge
> With the normal-ordered $Q$ of [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]] and the algebra of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]],
>
> $$
> [Q, a^{s\dagger}_{\mathbf p}] = a^{s\dagger}_{\mathbf p}, \quad [Q, b^{s\dagger}_{\mathbf p}] = -b^{s\dagger}_{\mathbf p}, \quad [Q, a^s_{\mathbf p}] = -a^s_{\mathbf p}, \quad [Q, b^s_{\mathbf p}] = b^s_{\mathbf p}, \qquad [Q, \psi] = -\psi, \quad [Q, \bar\psi] = \bar\psi .
> $$
>
> So the one-particle states of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]] have $Q|\mathbf p, s\rangle = +|\mathbf p, s\rangle$ and $Q|\mathbf p, s\rangle^c = -|\mathbf p, s\rangle^c$, and $\psi$ lowers the charge by one unit, both by annihilating a particle and by creating an antiparticle.
>
> *Scalar analogue:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]].
> *Source: Yu §5.5.3, eq. (5.267) and §5.5.2 (the commutator identity, eqs. (5.248)–(5.251)) · PS §3.5, p. 62 · the user's PHY 513 notes, Ch. 10 §10.6 ("both lower the charge by one unit") · the user's pre-course notes, §5.5 ("$Q/q$ counts particles minus antiparticles")*

^thm-c5b-5-4

> [!derivation]- Derivation
> **1. The identity.** $[AB, C] = A\{B, C\} - \{A, C\}B$ (Step 1 of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-7|Derivation §C5b.3.7]]).
>
> **2. $Q$ and $a^\dagger$.** By Step 2 of Derivation §C5b.3.7, $[a^{r\dagger}_{\mathbf q}a^r_{\mathbf q}, a^{s\dagger}_{\mathbf p}] = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)\,a^{r\dagger}_{\mathbf q}$, and $[b^{r\dagger}_{\mathbf q}b^r_{\mathbf q}, a^{s\dagger}_{\mathbf p}] = b^{r\dagger}_{\mathbf q}\{b^r_{\mathbf q}, a^{s\dagger}_{\mathbf p}\} - \{b^{r\dagger}_{\mathbf q}, a^{s\dagger}_{\mathbf p}\}b^r_{\mathbf q} = 0$ (mixed anticommutators vanish). With the weight $+1$ for $a^\dagger a$ and $-1$ for $b^\dagger b$ in $Q = \sum_r\int\frac{d^3q}{(2\pi)^3}(a^{r\dagger}_{\mathbf q}a^r_{\mathbf q} - b^{r\dagger}_{\mathbf q}b^r_{\mathbf q})$, integrating the delta: $[Q, a^{s\dagger}_{\mathbf p}] = a^{s\dagger}_{\mathbf p}$.
>
> **3. $Q$ and $b^\dagger$.** The same computation with the species exchanged gives $[b^{r\dagger}_{\mathbf q}b^r_{\mathbf q}, b^{s\dagger}_{\mathbf p}] = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)\,b^{r\dagger}_{\mathbf q}$; with the weight $-1$, $[Q, b^{s\dagger}_{\mathbf p}] = -b^{s\dagger}_{\mathbf p}$.
>
> **4. The annihilators, by adjoints.** $Q$ is Hermitian, so $([Q, a^\dagger])^\dagger = (Qa^\dagger - a^\dagger Q)^\dagger = aQ - Qa = -[Q, a]$. From Step 2, $-[Q, a^s_{\mathbf p}] = a^s_{\mathbf p}$, i.e. $[Q, a^s_{\mathbf p}] = -a^s_{\mathbf p}$; from Step 3, $[Q, b^s_{\mathbf p}] = +b^s_{\mathbf p}$.
>
> **5. The constant does not matter.** The unordered charge differs by a c-number ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]]), which commutes with everything, so Steps 2–4 hold for it too.
>
> **6. The states.** $Q|0\rangle = 0$, every term of the normal-ordered $Q$ ending in an annihilator ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]]). Then $Q\,a^{s\dagger}_{\mathbf p}|0\rangle = [Q, a^{s\dagger}_{\mathbf p}]|0\rangle + a^{s\dagger}_{\mathbf p}Q|0\rangle = a^{s\dagger}_{\mathbf p}|0\rangle$, and $Q\,b^{s\dagger}_{\mathbf p}|0\rangle = -b^{s\dagger}_{\mathbf p}|0\rangle$; multiply by $\sqrt{2E_{\mathbf p}}$.
>
> **7. The field.** $Q$ commutes with the c-number spinors and exponentials ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|§C5b.2, Caution: What anticommutes and what does not]]), so it acts on the operators in [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] term by term (after smearing): $[Q, \psi] = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl([Q, a^s_{\mathbf p}]u^se^{-ip\cdot x} + [Q, b^{s\dagger}_{\mathbf p}]v^se^{ip\cdot x}\bigr) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(-a^s_{\mathbf p}u^se^{-ip\cdot x} - b^{s\dagger}_{\mathbf p}v^se^{ip\cdot x}\bigr) = -\psi$. For $\bar\psi$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]) the operators are $b$ and $a^\dagger$, both with eigenvalue-change $+1$: $[Q, \bar\psi] = \bar\psi$.
>
> **What the derivation shows**
> - The pairing of $a$ with $b^\dagger$ in $\psi$ is a pairing by charge, not by energy: both lower $Q$ by one, while both $a^\dagger$ and $b^\dagger$ raise the energy ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]]) → [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-2|Remark: Destroying a particle is not creating an antiparticle]].
> - ⚑ By-product: since $\psi$ changes $Q$, its expectation value vanishes in every eigenstate of $Q$ → [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^rem-c5b-4-2|§C5b.4, Remark: Why the Dirac field has no coherent states]].

^der-c5b-5-4

*Uses:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark] Remark: Destroying a particle is not creating an antiparticle
> Asked in Lecture 10: should $a$ not do something similar to $b^\dagger$? Not with energy. Creating a particle costs energy $E_{\mathbf p}$, and so does creating an antiparticle ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]); destroying a particle releases it. The pairing that appears in $\psi$, $a$ with $b^\dagger$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]), is about charge: both lower the charge by one unit ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]]). Treating the Dirac equation as a one-particle equation leads to exactly this kind of confusion ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^cau-c5b-3-1|§C5b.3, Caution: Negative energies are a problem only if ψ is a wave function]]); and the one-particle Dirac equation by itself also lacks the exclusion principle, which the field delivers ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-6|§C5b.1, Remark: Spin and statistics are an output]]).
>
> *Source: Lecture 10 (transcript, question after slide 21) · the user's PHY 513 notes, Ch. 10 §10.6 ("Destroying a particle is not creating an antiparticle")*

^rem-c5b-5-2

> [!remark] Remark: The Dirac sea, read in the field
> Second-quantize the one-particle Dirac Hamiltonian $H_{\text{s.p.}}$ as a one-body operator in the manner of [[§C12.2★ Second Quantization#^thm-c12-2-4|QM Theorem §C12.2.4]]: one fermionic mode $c$ per eigenvector of $H_{\text{s.p.}}(\mathbf p)$, $H = \sum(E\,c_+^\dagger c_+ - E\,c_-^\dagger c_-)$. That is [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]] with $c_+ = a$ and $c_- = b^\dagger$. Dirac's sea ([[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]]) is the state with every negative-energy mode filled, annihilated by every $c_-^\dagger = b$: it *is* the field vacuum of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]]. Its energy relative to the empty state, $-\sum E$ over the negative modes, is $E_0^{(\rm D)}$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]); its electron number is the vacuum charge $+2V\int\frac{d^3p}{(2\pi)^3}$ ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-1|Remark: The vacuum charge, and why the order is forced]]); a hole has the reversed spin ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-4|Theorem §C5b.4.4]]). For the free field the two pictures are the same Fock space. What the field adds:
> - the vacuum is defined directly, and normal ordering removes the sea's infinite energy and charge, instead of positing an unobservable background;
> - antiparticles are the quanta of $b^\dagger$ for bosons too ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]), where no sea can be filled;
> - exclusion, which hole theory needed as an input to stabilize the sea, is a consequence of the anticommutators ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]).
>
> *Source: PS §3.5, pp. 57, 61 ("This reversal of sign agrees with the prediction of Dirac hole theory") · the user's pre-course notes, §5.5 (Remark "Antiparticles without hole theory") · the identification $c_- = b^\dagger$ written out here*

^rem-c5b-5-3

> [!remark]- Connections
> - The complex scalar and the Dirac field have the same two-species structure, with the roles reversed classically (scalar: positive energy, indefinite charge; Dirac: indefinite energy, positive charge) and made equal by quantization with the matching statistics — [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-3|§C2a.5, Remark: Charge, not probability]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]].
> - The positive density $\psi^\dagger\psi$ that made the Dirac equation look like a one-particle theory in Quantum Mechanics becomes a charge density with eigenvalues of both signs — [[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-1|Remark: The vacuum charge, and why the order is forced]].
> - The charge $Q$ becomes the electric charge once $\psi$ is coupled to the photon by a local phase, which makes the Dirac field the matter of quantum electrodynamics — QFT C8 (planned); charge conjugation, which exchanges $a$ and $b$ and is a symmetry of the free Dirac theory, is Lecture 12 — QFT C9 (planned).
> - The sign convention of the charge (PS's $Q$ against the Noether charge) is the one already met for the complex scalar — [[§C1b.5 Noether's Theorem#^cau-c1b-5-3|§C1b.5, Caution: Sign and normalization of the U(1) current]], [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]].
