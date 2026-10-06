---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2a.5 The Complex Scalar Field and Its Charge]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2b.1 Heisenberg Fields]] →

*Sources: the user's PHY 513 notes, Ch. 4 §4.10 · PHY 513 Problem Set 3, Problem 4, with the course solution.*

The field was quantized and produced particles ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]). The reverse question: when does a quantum field look like the classical field it came from? Not when it contains many quanta. For one oscillator, Quantum Mechanics answers with coherent states, the ground state displaced in phase space ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-3|QM Theorem §C3.4.3]]), with their Poisson statistics ([[§B4.3 Coherent States#^thm-b4-3-2|QM Theorem §B4.3.2]]). This section displaces all modes of the field at once. What the field adds: the label of the state is a function $\eta_{\mathbf k}$ on momentum space, its mean field is an arbitrary classical solution of the Klein–Gordon equation, and its fluctuations at every point are exactly the vacuum's.

## A definite number has no field

> [!theorem] Theorem §C2a.6.1: A State of Definite Particle Number Has No Mean Field
> If $N|\psi\rangle = n|\psi\rangle$, with $N$ the number operator of [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], then $\langle\psi|\phi(x)|\psi\rangle = 0$ for every $x$, however large $n$ is.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10 (Caution "A state of definite particle number has no field at all")*

^thm-c2a-6-1

> [!derivation]- Derivation
> **1. Number commutators.** $[N, a^\dagger_{\mathbf p}] = a^\dagger_{\mathbf p}$ and $[N, a_{\mathbf p}] = -a_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-2|Derivation §C2a.4.2]], step 5).
>
> **2. Shifted eigenvalues.** If $N|\psi\rangle = n|\psi\rangle$, then $Na^\dagger_{\mathbf p}|\psi\rangle = (a^\dagger_{\mathbf p}N + a^\dagger_{\mathbf p})|\psi\rangle = (n + 1)a^\dagger_{\mathbf p}|\psi\rangle$ and $Na_{\mathbf p}|\psi\rangle = (n - 1)a_{\mathbf p}|\psi\rangle$.
>
> **3. The field changes $N$ by one.** $\phi(x)$ is a superposition of $a_{\mathbf p}$ and $a^\dagger_{\mathbf p}$ with numerical coefficients ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]), so $\phi(x)|\psi\rangle$ is a sum of a vector in the eigenspace $n - 1$ and one in the eigenspace $n + 1$ of $N$.
>
> **4. Orthogonality.** $N$ is Hermitian, so its eigenspaces for $n \pm 1$ are orthogonal to $|\psi\rangle$: $\langle\psi|\phi(x)|\psi\rangle = 0$.
>
> **What the derivation shows**
> - Any operator linear in $a$, $a^\dagger$ has zero mean in a number eigenstate, however many quanta it holds.
> - A nonzero mean field needs a superposition of neighbouring particle numbers: the coherent state ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]]).

^der-c2a-6-1

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]

A state of $10^{20}$ quanta of definite number has exactly zero average field: whatever makes a field classical, it is not a large occupation number. It must be a superposition of different particle numbers, and the coherent state is the one that works. This is the field version of [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]], 2: an energy eigenstate of one oscillator never oscillates.

## Coherent states of the field

> [!definition] Definition §C2a.6.1: Coherent State of the Field
> For a complex function $\eta_{\mathbf k}$ on momentum space with $\bar N = \int\frac{d^3k}{(2\pi)^3}\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}} < \infty$, the **coherent state** is
>
> $$
> |\{\eta\}\rangle = e^{-\bar N/2}\exp\Bigl\{\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}\,a^\dagger_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\Bigr\}|0\rangle = D(\eta)|0\rangle, \qquad D(\eta) = \exp\int\frac{d^3k}{(2\pi)^3}\,\frac{\eta_{\mathbf k}a^\dagger_{\mathbf k} - \eta^*_{\mathbf k}a_{\mathbf k}}{\sqrt{2E_{\mathbf k}}} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, eq. (coherentstate) and Derivation "Three senses …", part 2 (displacement operator) · PHY 513 Problem Set 3, Problem 4*

^def-c2a-6-1

> [!theorem] Theorem §C2a.6.2: Coherent States Are Eigenstates of Every Annihilator
> For every $\mathbf p$,
>
> $$
> a_{\mathbf p}|\{\eta\}\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\,|\{\eta\}\rangle ,
> $$
>
> and $\langle\{\eta\}|\{\eta\}\rangle = 1$: the factor $e^{-\bar N/2}$ is the normalization, which requires $\bar N < \infty$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, eq. (coherenteigen) · PHY 513 Problem Set 3, Problem 4(a)–(b), course solution*

^thm-c2a-6-2

> [!derivation]- Derivation
> **1. One commutator.** Let $K = \int\frac{d^3k}{(2\pi)^3}\,\eta_{\mathbf k}a^\dagger_{\mathbf k}/\sqrt{2E_{\mathbf k}}$. By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]],
>
> $$
> [a_{\mathbf p}, K] = \int\frac{d^3k}{(2\pi)^3}\,\frac{\eta_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\,(2\pi)^3\delta^3(\mathbf p - \mathbf k) = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}} ,
> $$
>
> the delta eliminating $\mathbf k$ and cancelling the $(2\pi)^3$: a c-number. *Sense:* $K = a^\dagger(\eta/\sqrt{2E})$ is a smeared creator ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]), so its commutator with $a_{\mathbf p}$ is a function of $\mathbf p$, not a distribution ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 2); for $\eta/\sqrt{2E}$ square integrable but not Schwartz, by continuity from Schwartz profiles.
>
> **2. Powers.** $[a_{\mathbf p}, K^n] = \sum_{j=0}^{n-1}K^j\,[a_{\mathbf p}, K]\,K^{n-1-j} = nK^{n-1}[a_{\mathbf p}, K]$, because the c-number commutes with $K$. So $a_{\mathbf p}$ acts on functions of $K$ as $\frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\frac{d}{dK}$.
>
> **3. The exponential.** Summing the series term by term, $[a_{\mathbf p}, e^K] = \sum_{n\ge1}\frac{nK^{n-1}}{n!}[a_{\mathbf p}, K] = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\,e^K$.
>
> **4. Act on the vacuum.** $a_{\mathbf p}e^K|0\rangle = [a_{\mathbf p}, e^K]|0\rangle + e^Ka_{\mathbf p}|0\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}e^K|0\rangle$; multiplying by the constant $e^{-\bar N/2}$ gives the eigenvalue equation. ⚑ By-product: the eigenvalue is complex; $a_{\mathbf p}$ is not Hermitian, and its eigenvalue carries the amplitude and the phase of the classical mode → [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]].
>
> **5. The adjoint acts as a number too.** $K^\dagger = \int\frac{d^3k}{(2\pi)^3}\eta^{\ast}_{\mathbf k}a_{\mathbf k}/\sqrt{2E_{\mathbf k}}$, and by step 4
>
> $$
> K^\dagger e^K|0\rangle = \int\frac{d^3k}{(2\pi)^3}\,\frac{\eta^*_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\frac{\eta_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\,e^K|0\rangle = \bar N\,e^K|0\rangle, \qquad e^{K^\dagger}e^K|0\rangle = e^{\bar N}e^K|0\rangle .
> $$
>
> **6. Norm.** $\langle0|e^K|0\rangle = 1$, since $\langle0|K^n|0\rangle = 0$ for $n \ge 1$ ($\langle0|a^\dagger = 0$). So
>
> $$
> \langle\{\eta\}|\{\eta\}\rangle = e^{-\bar N}\,\langle0|e^{K^\dagger}e^K|0\rangle = e^{-\bar N}e^{\bar N}\langle0|e^K|0\rangle = 1 .
> $$
>
> ⚑ By-product: this needs $\bar N < \infty$; a classical configuration with infinitely many quanta (a plane wave filling all space) is not a state in the Fock space → [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]].
>
> **What the derivation shows**
> - $a_{\mathbf p}$ differentiates with respect to $K$; that one fact gives the eigenvalue and the norm.
> - The normalization $e^{-\bar N/2}$ is the Baker–Campbell–Hausdorff factor of the displacement form ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]]).
> - Used next: mean field, number statistics and fluctuations.

^der-c2a-6-2

*Uses:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]

> [!theorem] Theorem §C2a.6.3: A Coherent State Is the Displaced Vacuum
> $D(\eta)$ is unitary, $D(\eta)^\dagger a_{\mathbf p}D(\eta) = a_{\mathbf p} + \eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$, and $D(\eta)|0\rangle$ equals the exponential form of [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]]. The shifted operators $\tilde a_{\mathbf p} = a_{\mathbf p} - \eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$ obey the algebra of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]] and annihilate $|\{\eta\}\rangle$: the coherent state is the vacuum of $\tilde a$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, Derivation "Three senses in which a coherent state is classical", part 2*

^thm-c2a-6-3

> [!derivation]- Derivation
> **1. Unitarity.** $X = K - K^\dagger$ (with $K$ as in [[§C2a.6 Coherent States and the Classical Field#^der-c2a-6-2|Derivation §C2a.6.2]]) has $X^\dagger = -X$, so $D = e^X$ has $D^\dagger = e^{-X} = D^{-1}$.
>
> **2. A c-number commutator.** $[a_{\mathbf p}, X] = [a_{\mathbf p}, K] - [a_{\mathbf p}, K^\dagger] = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}} - 0$, since $K^\dagger$ contains only annihilators.
>
> **3. Conjugation.** By the Baker–Hausdorff lemma ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-2|QM Theorem §C3.3.2]]),
>
> $$
> e^{-X}a_{\mathbf p}e^{X} = a_{\mathbf p} + [a_{\mathbf p}, X] + \tfrac1{2!}\bigl[[a_{\mathbf p}, X], X\bigr] + \dots = a_{\mathbf p} + \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}} ,
> $$
>
> all higher terms vanishing because $[a_{\mathbf p}, X]$ is a number. The adjoint gives $D^\dagger a^\dagger_{\mathbf p}D = a^\dagger_{\mathbf p} + \eta^*_{\mathbf p}/\sqrt{2E_{\mathbf p}}$.
>
> **4. Split the exponential.** $[K, -K^\dagger] = -\int\!\!\int\frac{d^3k\,d^3q}{(2\pi)^6}\frac{\eta_{\mathbf k}\eta^{\ast}_{\mathbf q}}{\sqrt{4E_{\mathbf k}E_{\mathbf q}}}[a^\dagger_{\mathbf k}, a_{\mathbf q}] = \int\frac{d^3k}{(2\pi)^3}\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}} = \bar N$, using $[a^\dagger_{\mathbf k}, a_{\mathbf q}] = -(2\pi)^3\delta^3(\mathbf k - \mathbf q)$; this is [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 1, with $g = h = \eta/\sqrt{2E}$, $[K^\dagger, K] = \int\frac{d^3k}{(2\pi)^3}|\eta_{\mathbf k}|^2/2E_{\mathbf k}$. For $[A, B]$ a number, $e^{A + B} = e^Ae^Be^{-[A, B]/2}$ (proved in [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^der-c3-4-3|QM Derivation of Theorem §C3.4.3]], 2); with $A = K$, $B = -K^\dagger$: $D = e^Ke^{-K^\dagger}e^{-\bar N/2}$.
>
> **5. On the vacuum.** $K^\dagger|0\rangle = 0$, so $e^{-K^\dagger}|0\rangle = |0\rangle$ and $D|0\rangle = e^{-\bar N/2}e^K|0\rangle$. ⚑ By-product: the normalization of Def. §C2a.6.1 is exactly the BCH factor of step 4 → [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]] (statement: $D(\eta)|0\rangle$ equals the exponential form).
>
> **6. Shifted operators.** Shifting by numbers leaves every commutator unchanged, so $[\tilde a_{\mathbf p}, \tilde a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$; and $\tilde a_{\mathbf p}|\{\eta\}\rangle = 0$ by [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]. Equivalently $\tilde a_{\mathbf p} = Da_{\mathbf p}D^\dagger$ (step 3 with $\eta \to -\eta$), and $\tilde a_{\mathbf p}D|0\rangle = Da_{\mathbf p}|0\rangle = 0$. ⚑ By-product: the same algebra has many vacua, one for each displacement; for finite $\bar N$ they are related by the unitary $D$, and the Fock space is the same → [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-5|★ Remark: Other mode functions]].
>
> **What the derivation shows**
> - The coherent state carries the vacuum's structure, moved by a c-number in every mode; everything about its fluctuations follows by conjugation with $D$ ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]]).
> - This is QM's single-oscillator displacement applied to all modes at once.

^der-c2a-6-3

*Uses:* [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-2|QM Theorem §C3.3.2]], [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-3|QM Theorem §C3.4.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]

> [!theorem] Theorem §C2a.6.4: The Mean Field Is a Classical Solution
> With the Heisenberg field $\phi(x)$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]), the mean field
>
> $$
> \bar\phi(x) \equiv \langle\{\eta\}|\phi(x)|\{\eta\}\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl(\eta_{\mathbf p}\,e^{-ip\cdot x} + \eta^*_{\mathbf p}\,e^{ip\cdot x}\Bigr)\Big|_{p^0 = E_{\mathbf p}}
> $$
>
> is a real solution of the Klein–Gordon equation, and every real solution with $\bar N < \infty$ arises from exactly one $\eta$; the vacuum is $\eta = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, eq. (phibar) and Derivation "Three senses …", part 1 · PHY 513 Problem Set 3, Problem 4(c), course solution*

^thm-c2a-6-4

> [!derivation]- Derivation
> **1. The field.** $\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(a_{\mathbf p}e^{-ip\cdot x} + a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$ with $p^0 = E_{\mathbf p}$.
>
> **2. Matrix elements of the modes.** By [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]], $a_{\mathbf p}$ acting to the right gives $\eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$, and the adjoint equation $\langle\{\eta\}|a^\dagger_{\mathbf p} = \frac{\eta^{\ast}_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\langle\{\eta\}|$ lets $a^\dagger_{\mathbf p}$ act to the left. With $\langle\{\eta\}|\{\eta\}\rangle = 1$:
>
> $$
> \langle\{\eta\}|a_{\mathbf p}|\{\eta\}\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}, \qquad \langle\{\eta\}|a^\dagger_{\mathbf p}|\{\eta\}\rangle = \frac{\eta^*_{\mathbf p}}{\sqrt{2E_{\mathbf p}}} .
> $$
>
> **3. Substitute.** The two factors $1/\sqrt{2E_{\mathbf p}}$ combine into $1/2E_{\mathbf p}$, giving the formula of the statement. *Sense:* the integral converges absolutely when $\eta_{\mathbf p}/E_{\mathbf p}$ is integrable (for instance $\eta \in \mathcal S$); for a general $\eta$ with $\bar N < \infty$ the mean field is defined smeared, and it is finite for every test function ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]], 2). ⚑ By-product: the invariant measure $d^3p/(2\pi)^32E_{\mathbf p}$ appears by itself → [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]].
>
> **4. Real and on shell.** The second term is the complex conjugate of the first, so $\bar\phi$ is real; each exponential has $p^2 = m^2$, so $(\partial^2 + m^2)\bar\phi = 0$ (differentiating under the integral, [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], when $E_{\mathbf p}|\eta_{\mathbf p}|$ is integrable; in general as an identity of distributions, the derivative moved onto the test function, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]).
>
> **5. Every solution.** By [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] every real solution is $\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(a_{\mathbf p}e^{-ip\cdot x} + \text{c.c.})$ with unique amplitudes $a_{\mathbf p}$ (uniqueness of the transform, in $\mathcal S'$: [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2); it equals $\bar\phi$ iff $\eta_{\mathbf p} = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}$. The condition $\bar N = \int\frac{d^3p}{(2\pi)^3}|a_{\mathbf p}|^2 < \infty$ selects the solutions that are states. ⚑ By-product: choosing $\eta$ is choosing a classical field configuration, and $|a_{\mathbf p}|^2$ is the mean number of quanta per mode → [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]].
>
> **What the derivation shows**
> - Expectation values of $\phi$ in a coherent state are obtained by replacing operators by their eigenvalues: the quantum field's mean is a classical field.
> - Used next: time evolution ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5|Theorem §C2a.6.5]]) and the fluctuations about this mean ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]]).

^der-c2a-6-4

*Uses:* [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]]

> [!theorem] Theorem §C2a.6.5: Coherent States Stay Coherent
> Under the free evolution, $e^{-i:\!H\!:\,t}\,|\{\eta_{\mathbf k}\}\rangle = |\{\eta_{\mathbf k}e^{-iE_{\mathbf k}t}\}\rangle$, with the same $\bar N$; the mean field of the evolved state, $\langle\{\eta(t)\}|\phi(\mathbf x)|\{\eta(t)\}\rangle$, is $\bar\phi(t, \mathbf x)$ of [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]]: it follows the classical solution for all time.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, Derivation "Three senses …", part 3*

^thm-c2a-6-5

> [!derivation]- Derivation
> **1. Evolve one creator.** [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], 1 (derived there from the ladder relation $[H, a^\dagger_{\mathbf p}] = E_{\mathbf p}a^\dagger_{\mathbf p}$ of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6|Theorem §C2a.3.6]]) gives $e^{iHt}a^\dagger_{\mathbf p}e^{-iHt} = a^\dagger_{\mathbf p}e^{iE_{\mathbf p}t}$ for every real $t$; replacing $t$ by $-t$,
>
> $$
> e^{-iHt}a^\dagger_{\mathbf p}e^{iHt} = a^\dagger_{\mathbf p}\,e^{-iE_{\mathbf p}t} .
> $$
>
> The zero-point constant in $H$ drops out of this conjugation, so $H$ and $:\!H\!:$ give the same result.
>
> **2. Evolve the exponential.** Conjugation by $e^{-iHt}$ preserves products and sums, so $e^{-iHt}e^Ke^{iHt} = \exp\bigl(e^{-iHt}Ke^{iHt}\bigr) = \exp\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}e^{-iE_{\mathbf k}t}a^\dagger_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}$.
>
> **3. The vacuum does not move.** $:\!H\!:|0\rangle = 0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), so $e^{iHt}|0\rangle = |0\rangle$ and
>
> $$
> e^{-iHt}|\{\eta\}\rangle = e^{-\bar N/2}\,e^{-iHt}e^Ke^{iHt}\,|0\rangle = e^{-\bar N/2}\exp\Bigl\{\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}e^{-iE_{\mathbf k}t}\,a^\dagger_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\Bigr\}|0\rangle .
> $$
>
> ⚑ By-product: with the unordered $H$ the state would acquire the global phase $e^{-iE_0t}$, unobservable → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]] (a c-number).
>
> **4. Same normalization.** $|\eta_{\mathbf k}e^{-iE_{\mathbf k}t}| = |\eta_{\mathbf k}|$, so $\bar N$ is unchanged and the result is the coherent state with label $\eta_{\mathbf k}e^{-iE_{\mathbf k}t}$.
>
> **5. Mean field.** Apply [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]] at $t = 0$ to the label $\eta_{\mathbf p}e^{-iE_{\mathbf p}t}$: $\eta_{\mathbf p}e^{-iE_{\mathbf p}t}e^{i\mathbf p\cdot\mathbf x} = \eta_{\mathbf p}e^{-ip\cdot x}$, which is $\bar\phi(t, \mathbf x)$. ⚑ By-product: Schrödinger picture (state evolves, step 3) and Heisenberg picture (field evolves, $a_{\mathbf p}(t) = a_{\mathbf p}e^{-iE_{\mathbf p}t}$, [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]) give the same mean field → [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5|Theorem §C2a.6.5]] (statement).
>
> **What the derivation shows**
> - Each mode label turns clockwise at its own frequency, as for one oscillator ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-3|QM Theorem §C3.4.3]], 4).
> - Because the theory is free, Ehrenfest's theorem is exact: the mean field obeys the classical equation with no corrections ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-6|QM Theorem §C3.3.6]]).

^der-c2a-6-5

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]]

> [!theorem] Theorem §C2a.6.6: Poisson Number Statistics
> The particle number in $|\{\eta\}\rangle$ is Poisson distributed, $P(n) = e^{-\bar N}\bar N^n/n!$, with
>
> $$
> \langle N\rangle = \bar N = \int\frac{d^3k}{(2\pi)^3}\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}}, \qquad \langle(\Delta N)^2\rangle = \bar N, \qquad \frac{\Delta N}{\bar N} = \frac{1}{\sqrt{\bar N}} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, eq. (poisson) · PHY 513 Problem Set 3, Problem 4(d)–(e), course solution; the distribution $P(n)$ derived here*

^thm-c2a-6-6

> [!derivation]- Derivation
> **1. Mean.** $\langle N\rangle = \int\frac{d^3p}{(2\pi)^3}\langle\{\eta\}|a^\dagger_{\mathbf p}a_{\mathbf p}|\{\eta\}\rangle$; let $a_{\mathbf p}$ act to the right and $a^\dagger_{\mathbf p}$ to the left ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]): $\langle a^\dagger_{\mathbf p}a_{\mathbf p}\rangle = |\eta_{\mathbf p}|^2/2E_{\mathbf p}$, so $\langle N\rangle = \bar N$.
>
> **2. Second moment: reorder first.** $N^2 = \int\!\!\int\frac{d^3p\,d^3k}{(2\pi)^6}a^\dagger_{\mathbf p}a_{\mathbf p}a^\dagger_{\mathbf k}a_{\mathbf k}$, and $a_{\mathbf p}a^\dagger_{\mathbf k} = a^\dagger_{\mathbf k}a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf p - \mathbf k)$ gives
>
> $$
> N^2 = \int\!\!\int\frac{d^3p\,d^3k}{(2\pi)^6}\,a^\dagger_{\mathbf p}a^\dagger_{\mathbf k}a_{\mathbf p}a_{\mathbf k} + \int\frac{d^3p}{(2\pi)^3}\,a^\dagger_{\mathbf p}a_{\mathbf p} ,
> $$
>
> the delta eliminating $\mathbf k$ in the second term (an identity of quadratic forms; on the coherent state $a_{\mathbf p}|\{\eta\}\rangle$ is a square-integrable function of $\mathbf p$ times the state, [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]], so every integral below converges).
>
> **3. Replace by eigenvalues.** With all annihilators on the right and creators on the left, step 1's rule gives $\langle N^2\rangle = \bar N^2 + \bar N$, so $\langle(\Delta N)^2\rangle = \langle N^2\rangle - \langle N\rangle^2 = \bar N$. ⚑ By-product: the extra $\bar N$ is the commutator term of step 2; it is the whole variance → [[§C2a.6 Coherent States and the Classical Field#^rem-c2a-6-1|Remark: Why a definite field needs an indefinite particle number]].
>
> **4. One packet mode.** Write $K = \sqrt{\bar N}\,c^\dagger$ with $c^\dagger = \bar N^{-1/2}\int\frac{d^3k}{(2\pi)^3}\eta_{\mathbf k}a^\dagger_{\mathbf k}/\sqrt{2E_{\mathbf k}}$. Then $[c, c^\dagger] = \bar N^{-1}[K^\dagger, K] = \bar N^{-1}\bar N = 1$ (step 4 of [[§C2a.6 Coherent States and the Classical Field#^der-c2a-6-3|Derivation §C2a.6.3]]): $c^\dagger$ creates one quantum in the normalized wave packet shaped by $\eta$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], 2).
>
> **5. Expand.** $|\{\eta\}\rangle = e^{-\bar N/2}e^{\sqrt{\bar N}c^\dagger}|0\rangle = e^{-\bar N/2}\sum_n\frac{\bar N^{n/2}}{\sqrt{n!}}|n\rangle_c$ with $|n\rangle_c = (c^\dagger)^n|0\rangle/\sqrt{n!}$ orthonormal. Since $[N, c^\dagger] = c^\dagger$, $|n\rangle_c$ has exactly $n$ quanta, and $P(n) = |{}_c\langle n|\{\eta\}\rangle|^2 = e^{-\bar N}\bar N^n/n!$, the single-oscillator result ([[§B4.3 Coherent States#^thm-b4-3-2|QM Theorem §B4.3.2]]).
>
> **What the derivation shows**
> - A coherent state of the field is a coherent state of one oscillator, the packet mode $c$, with all other modes empty.
> - The relative spread $1/\sqrt{\bar N}$ makes the number sharp only for $\bar N \gg 1$: the classical regime.

^der-c2a-6-6

*Uses:* [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§B4.3 Coherent States#^thm-b4-3-2|QM Theorem §B4.3.2]]

> [!theorem] Theorem §C2a.6.7: The Field Fluctuates Exactly as in the Vacuum
> For every $x$, $y$ and every $\eta$,
>
> $$
> \langle\{\eta\}|\bigl(\phi(x) - \bar\phi(x)\bigr)\bigl(\phi(y) - \bar\phi(y)\bigr)|\{\eta\}\rangle = \langle0|\phi(x)\phi(y)|0\rangle ;
> $$
>
> in particular $\langle\phi^2\rangle - \bar\phi^2 = \langle0|\phi^2|0\rangle$, independent of the amplitude.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10, Derivation "Three senses …", part 2*

^thm-c2a-6-7

> [!derivation]- Derivation
> **1. Displace the field.** $\phi$ is linear in $a$ and $a^\dagger$ with numerical coefficients, so [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]] (for $a$ and $a^\dagger$) gives
>
> $$
> D^\dagger\phi(x)D = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl[\Bigl(a_{\mathbf p} + \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\Bigr)e^{-ip\cdot x} + \Bigl(a^\dagger_{\mathbf p} + \frac{\eta^*_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\Bigr)e^{ip\cdot x}\Bigr] = \phi(x) + \bar\phi(x) ,
> $$
>
> the c-number part being exactly the formula of [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]].
>
> **2. Insert $DD^\dagger = 1$.** With $|\{\eta\}\rangle = D|0\rangle$:
>
> $$
> \langle\{\eta\}|(\phi(x) - \bar\phi(x))(\phi(y) - \bar\phi(y))|\{\eta\}\rangle = \langle0|D^\dagger(\phi(x) - \bar\phi(x))D\;D^\dagger(\phi(y) - \bar\phi(y))D|0\rangle .
> $$
>
> **3. Use step 1.** $D^\dagger(\phi(x) - \bar\phi(x))D = \phi(x) + \bar\phi(x) - \bar\phi(x) = \phi(x)$ ($\bar\phi$ is a number, so $D^\dagger\bar\phi D = \bar\phi$). The right side is $\langle0|\phi(x)\phi(y)|0\rangle$.
>
> **4. Coincident points.** Setting $y = x$ gives the variance. ⚑ By-product: $\langle0|\phi(x)^2|0\rangle$ is the Wightman function at zero separation, which diverges; the statement is meaningful for fields averaged over a region → [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]].
>
> **What the derivation shows**
> - The mean grows with $|\eta|$ while the jitter stays at its vacuum value: the relative uncertainty falls like $1/|\eta|$, the field-variable form of the Poisson result.
> - Equivalently, $\phi = \bar\phi + \tilde\phi$, with $\tilde\phi$ built from the shifted $\tilde a$ for which $|\{\eta\}\rangle$ is the vacuum.

^der-c2a-6-7

*Uses:* [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]]

> [!theorem] Theorem §C2a.6.8: Smeared Fluctuations Are Finite and Independent of the Amplitude
> Let $f \in \mathcal S(\mathbb R^3)$ be real, $\phi_t(f) = \int d^3x\,f(\mathbf x)\,\phi(t, \mathbf x)$ the Heisenberg field smeared at time $t$, $d\mu = d^3p/(2\pi)^32E_{\mathbf p}$, and $\bar N < \infty$.
> 1. $\langle\{\eta\}|\bigl(\phi_t(f) - \bar\phi_t(f)\bigr)^2|\{\eta\}\rangle = \langle0|\phi_t(f)^2|0\rangle = \displaystyle\int d\mu\,|\tilde f(\mathbf p)|^2$: finite, and independent of $\eta$ and of $t$.
> 2. The smeared mean field $\bar\phi_t(f) = \langle\{\eta\}|\phi_t(f)|\{\eta\}\rangle = 2\operatorname{Re}\displaystyle\int d\mu\,\eta_{\mathbf p}\,e^{-iE_{\mathbf p}t}\,\overline{\tilde f(\mathbf p)}$ obeys $|\bar\phi_t(f)| \le 2\sqrt{\bar N}\,\bigl(\int d\mu\,|\tilde f|^2\bigr)^{1/2}$.
>
> This is the content of [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]], whose coincident-point form compares two divergent numbers.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10 (Derivation "Three senses …", part 2) and §4.8 (Caution "Two honesty points") · the smeared form stated and derived here*

^thm-c2a-6-8

> [!derivation]- Derivation
> **1. The smeared field in modes.** With $a_{\mathbf p}(t) = a_{\mathbf p}e^{-iE_{\mathbf p}t}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]), the computation of [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-7|Derivation §C2a.2.7]], steps 4–5, gives $\phi_t(f) = a(g_t) + a^\dagger(g_t)$ with $g_t(\mathbf p) = e^{iE_{\mathbf p}t}\tilde f(\mathbf p)/\sqrt{2E_{\mathbf p}}$, a Schwartz function ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]).
>
> **2. Displace.** By [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]], $D^\dagger a_{\mathbf p}D = a_{\mathbf p} + \eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$; smearing with $\overline{g_t}$, $D^\dagger a(g_t)D = a(g_t) + c$ with $c = \int\frac{d^3p}{(2\pi)^3}\overline{g_t}\,\eta/\sqrt{2E} = \int d\mu\,\eta_{\mathbf p}e^{-iE_{\mathbf p}t}\overline{\tilde f(\mathbf p)}$, and $D^\dagger a^\dagger(g_t)D = a^\dagger(g_t) + \overline c$. So $D^\dagger\phi_t(f)D = \phi_t(f) + 2\operatorname{Re}c$, and $2\operatorname{Re}c = \langle0|D^\dagger\phi_t(f)D|0\rangle = \bar\phi_t(f)$: part 2's formula. The integral defining $c$ converges for every $\eta$ with $\bar N < \infty$, by step 4.
>
> **3. Fluctuations.** Insert $DD^\dagger = 1$ as in [[§C2a.6 Coherent States and the Classical Field#^der-c2a-6-7|Derivation §C2a.6.7]], step 2: $\langle\{\eta\}|(\phi_t(f) - \bar\phi_t(f))^2|\{\eta\}\rangle = \langle0|\bigl(D^\dagger(\phi_t(f) - \bar\phi_t(f))D\bigr)^2|0\rangle = \langle0|\phi_t(f)^2|0\rangle$. Every operator here is a smeared field, so both sides are numbers.
>
> **4. The vacuum value.** $a(g_t)|0\rangle = 0$, so $\langle0|\phi_t(f)^2|0\rangle = \|a^\dagger(g_t)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3}|g_t|^2 = \int d\mu\,|\tilde f|^2$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], 1): the phase $e^{iE_{\mathbf p}t}$ has modulus 1, so $t$ drops out, and this is [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-8|Theorem §C2a.4.8]] at time $t$. For the bound of part 2, Cauchy–Schwarz in $L^2(d\mu)$ gives $|c| \le (\int d\mu\,|\eta|^2)^{1/2}(\int d\mu\,|\tilde f|^2)^{1/2}$, and $\int d\mu\,|\eta|^2 = \bar N$ ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]]).
>
> **5. Back to points.** Pairing the identity of [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]] (at equal times) with $f(\mathbf x)f(\mathbf y)$ gives part 1 ([[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]]: both sides are kernels of the same bilinear form). At $\mathbf y = \mathbf x$ without smearing both sides are $\langle0|\phi(x)^2|0\rangle$, the number that diverges like $\Lambda^2/8\pi^2$ ([[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-8|Derivation §C2a.4.8]], step 4).
>
> **What the derivation shows**
> - "A coherent state has the vacuum's fluctuations" is an identity between finite numbers once the field is averaged over a region; the size of the averaging region sets the size of the fluctuation, $\int d\mu\,|\tilde f|^2$.
> - The mean field grows like $\sqrt{\bar N}$ at fixed smearing while the fluctuation does not: the classical regime $\bar N \gg 1$ ([[§C2a.6 Coherent States and the Classical Field#^rem-c2a-6-1|Remark: Why a definite field needs an indefinite particle number]]).
> - The mean field of a state with $\bar N < \infty$ is always a well-defined distribution; it is a function when $\eta$ decays fast enough.

^der-c2a-6-8

*Uses:* [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3|Theorem §C2a.6.3]], [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]], [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-8|Theorem §C2a.4.8]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]]

![[ph-qft-c2-4-1.svg]]
*One mode of the field, $x = (a + a^\dagger)/\sqrt2$, in two states with mean occupation 4 (computed). Left: the number distribution, Poisson for the coherent state with $\eta/\sqrt{2E} = 2$, a single bar for $|4\rangle$ (Theorem §C2a.6.6). Right: $\langle x\rangle \pm \Delta x$ against $\omega t$. The coherent state oscillates like a classical wave with the vacuum's spread $1/\sqrt2$ (Theorems §C2a.6.4, §C2a.6.5, §C2a.6.7); the number state has no oscillating field at all (Theorem §C2a.6.1), only a larger spread $\sqrt{4 + \frac12}$ centred on zero. Right panel adapted from the user's PHY 513 notes, Ch. 4.*

> [!remark] Remark: Why a definite field needs an indefinite particle number
> The field is built from $a + a^\dagger$ and the number from $a^\dagger a$; they do not commute, and the resulting trade-off is the field-theory form of the number–phase uncertainty of quantum optics. A number eigenstate has a perfectly definite $N$ and a completely undetermined phase, hence no mean field; a coherent state fixes the phase at the cost of $\Delta N = \sqrt{\bar N}$. "The field has a definite value" means [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]]: the mean grows with $|\eta|$ while the jitter stays at its irreducible vacuum value, so the relative uncertainty falls like $1/|\eta|$, the Poisson result read in field variables. The classical regime is $\bar N \gg 1$ (Problem Set 3, Problem 4(e)), which is why a radio wave or a laser beam, with astronomically many quanta in phase, is described by a classical field; macroscopic occupation alone ([[§C2a.4 Particles and Relativistic Normalization#^rem-c2a-4-1|Remark: What the spectrum says]]) does not suffice without that phase coherence. The vacuum fluctuation at a single point, $\langle0|\phi(x)^2|0\rangle$, is itself divergent (it is the two-point function at coincident points, [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]); the statement is meaningful for the field averaged over a region ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10 (Caution "Why the two must be traded"; Derivation, part 2)*

^rem-c2a-6-1

> [!remark] Remark: What changes from the single oscillator
> For one oscillator, Quantum Mechanics' [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-3|QM Theorem §C3.4.3]] already contains the mechanism: displacement by $D(\lambda)$, eigenstate of $a$, Poisson statistics, the ground state's spreads at all times, and the label turning as $\lambda e^{-i\omega t}$. The derivation of Theorem §C2a.6.6 shows that a coherent state of the free field *is* a coherent state of one oscillator, the wave packet $c^\dagger$ shaped by $\eta$, with all other modes in their vacuum; so those results transfer mode by mode (rule: same result, same argument, linked). What is new is the reading: the label $\eta_{\mathbf k}$ is a classical field configuration, the invariant measure $d^3p/(2\pi)^32E_{\mathbf p}$ appears in $\bar\phi$ on its own, and the "phase-space point" of the oscillator becomes a solution of the Klein–Gordon equation. Because the theory is free, Ehrenfest's theorem is exact: the mean field obeys the classical equation with no corrections ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-6|QM Theorem §C3.3.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.10*

^rem-c2a-6-2

> [!remark]- Connections
> - A classical source coupled linearly to the field, $\mathcal L \ni j(x)\phi(x)$, turns the vacuum into exactly such a coherent state, with $\eta_{\mathbf p} \propto \tilde j(p)$ on shell, and the Poisson distribution of Theorem §C2a.6.6 is the distribution of the number of particles produced — [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2|Theorem §C2b.8.2]].
> - The single-oscillator theory: coherent states as eigenstates of $a$ and as displaced ground states, their Poisson statistics and their rigid motion in phase space — [[§B4.3 Coherent States#^def-b4-3-1|QM Def. §B4.3.1]], [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^def-c3-4-1|QM Def. §C3.4.1]], [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-3|QM Theorem §C3.4.3]].
> - The classical Klein–Gordon field and its plane-wave solutions, of which $\bar\phi$ is the general superposition — [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]]; wave packets of a dispersive medium, which is what $\bar\phi$ is for a localized $\eta$ — [[§B6.2 Dispersion, Phase Velocity and Group Velocity#^thm-b6-2-3|WO Theorem §B6.2.3]].
> - A superposition of two coherent states loses its coherence when coupled to an environment, which is one reason macroscopic fields look classical rather than like superpositions of classical fields — [[§C11.5★ Open Quantum Systems and Decoherence#^ex-c11-5-2|QM Example §C11.5.2]].
> - The same construction for the photon field gives the classical electromagnetic wave as a coherent state of photons, the basis of quantum optics — the photon mode algebra and Fock space are in [[§C4.6 Covariant Quantization and the Indefinite Metric#^thm-c4-6-8|Theorem §C4.6.8]] and [[§C4.6 Covariant Quantization and the Indefinite Metric#^pr-c4-6-13|Principle §C4.6.13]]; the coherent states themselves are not yet written (QFT C8, planned).
> - A coherent state is the exponential of a smeared creator, $K = a^\dagger(\eta/\sqrt{2E})$, which is why its eigenvalue relation and norm involve functions and not distributions; "finite $\bar N$" is "$\eta/\sqrt{2E}$ square integrable" — [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]].
> - Fluctuations at a point are the coincident value of a distribution; smeared, they are the finite number $\int d\mu\,|\tilde f|^2$, and the kernel theorem is what lets the pointwise identity stand for the smeared one ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-8|Theorem §C2a.6.8]]) — [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-8|Theorem §C2a.4.8]]; the bound on the smeared mean field is Cauchy–Schwarz in $L^2$ of the invariant measure — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]].
> - The mean field obeys the Klein–Gordon equation by differentiation under the integral, or as a distribution when $\eta$ decays slowly; its amplitudes are unique because the transform is injective on $\mathcal S'$ — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]].
> - The vacuum fluctuation that a coherent state carries is the two-point function $D_W(x - y) = \langle0|\phi(x)\phi(y)|0\rangle$ — [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]].
