---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.1 Canonical Quantization of the Dirac Field]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.3 Energy, Momentum and the Zero-Point Energy]] →

*Sources: the user's PHY 513 notes, Ch. 10 §§10.3–10.4 · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), Part B, slides and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 52–58 · Yu Zhao-Huan, 量子场论讲义, §5.4.3, §§5.5.1–5.5.2 · the user's pre-course notes, §5.5.*

This is the spinor counterpart of [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]], and, since the Dirac field is complex, of the two oscillator sets of the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]]). It expands the Dirac field on the plane-wave spinors $u^s(p)$, $v^s(p)$ of [[§C5a.9 Plane-Wave Solutions|§C5a.9]], extracts the coefficients with the positive product $\int\psi^\dagger\psi$, and shows Lecture 10's principle: anticommutators of the fields ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]) are equivalent to anticommutators of the oscillators. The spin-specific steps (spin labels, spin sums with the $\gamma^0$ of $\bar\psi$, signs from anticommutation) have their own boxes. The first of Lecture 10's checkpoints, where the commutator version would fail, closes the section. Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].

## The mode expansion

> [!theorem] Theorem §C5b.2.1: Mode Expansion of the Dirac Field
> Every solution of the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-1|Def. §C5a.7.1]]) is
>
> $$
> \psi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s=1,2}\Bigl(a^s_{\mathbf p}\,u^s(p)\,e^{-ip\cdot x} + b^{s\dagger}_{\mathbf p}\,v^s(p)\,e^{ip\cdot x}\Bigr), \qquad p^0 = E_{\mathbf p} ,
> $$
>
> with the spinors $u^s(p)$, $v^s(p)$ of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]] and four coefficients per momentum. Classically $a^s_{\mathbf p}$ and $b^{s\dagger}_{\mathbf p} \equiv \overline{b^s_{\mathbf p}}$ are complex amplitudes; quantization makes them operator-valued distributions $\hat a^s_{\mathbf p}$, $\hat b^{s\dagger}_{\mathbf p}$ in $\mathbf p$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], componentwise in $s$), and the field the operator-valued distribution $\hat\psi(x)$, the same expansion with $\hat a^s_{\mathbf p}$, $\hat b^{s\dagger}_{\mathbf p}$ in place of the amplitudes ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]). The conjugate fields $\hat\psi^\dagger$ and $\hat{\bar\psi}$: [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]].
>
> *Scalar analogue:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]; complex field [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]].
> *Source: Lecture 10, slides 10–11 · the user's PHY 513 notes, Ch. 10 §10.3 (Definition "Mode expansion of the Dirac field") · PS §3.5, eqs. (3.87), (3.99) · Yu §5.4, eqs. (5.216)–(5.217) · the user's pre-course notes, §5.4*

^thm-c5b-2-1

> [!derivation]- Derivation
> **1. Fourier transform in space.** Write $\psi(t, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}\tilde\psi(t, \mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$ (for a classical field in $\mathcal S$; in general in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]). Since $-i\nabla e^{i\mathbf p\cdot\mathbf x} = \mathbf p\,e^{i\mathbf p\cdot\mathbf x}$ (derivative ↔ multiplication, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]), the Dirac equation $i\partial_t\psi = H_{\text{s.p.}}\psi$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]) becomes, momentum by momentum,
>
> $$
> i\partial_t\tilde\psi(t, \mathbf p) = H_{\text{s.p.}}(\mathbf p)\,\tilde\psi(t, \mathbf p), \qquad H_{\text{s.p.}}(\mathbf p) = \boldsymbol\alpha\cdot\mathbf p + \beta m = \gamma^0\gamma^ip^i + \gamma^0m .
> $$
>
> **2. $H_{\text{s.p.}}(\mathbf p)$ is Hermitian with $H_{\text{s.p.}}(\mathbf p)^2 = E_{\mathbf p}^2$.** $\gamma^0$ is Hermitian and $\gamma^i$ anti-Hermitian ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]]), so $(\gamma^0\gamma^i)^\dagger = \gamma^{i\dagger}\gamma^0 = -\gamma^i\gamma^0 = \gamma^0\gamma^i$. From the Clifford algebra ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]]) with $(\gamma^0)^2 = 1$: $\alpha^i\alpha^j + \alpha^j\alpha^i = -(\gamma^i\gamma^j + \gamma^j\gamma^i) = -2g^{ij} = 2\delta^{ij}$ and $\alpha^i\beta + \beta\alpha^i = \gamma^0\gamma^i\gamma^0 + \gamma^i = -\gamma^i + \gamma^i = 0$. Squaring, $h^2 = \mathbf p^2 + m^2 = E_{\mathbf p}^2$, so the eigenvalues are $\pm E_{\mathbf p}$ (this is the second route of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]]).
>
> **3. The eigenvectors.** Multiplying $(\slashed{p} - m)u^s(p) = 0$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-1|Theorem §C5a.9.1]]; slash: [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]) by $\gamma^0$ gives $(E_{\mathbf p} - \gamma^0\gamma^ip^i - \gamma^0m)u^s = 0$: $H_{\text{s.p.}}(\mathbf p)u^s(p) = +E_{\mathbf p}u^s(p)$. Multiplying $(\slashed{\tilde p} + m)v^s(\tilde p) = 0$ by $\gamma^0$, with $\slashed{\tilde p} = \gamma^0E_{\mathbf p} + \gamma^ip^i$: $(E_{\mathbf p} + \gamma^0\gamma^ip^i + \gamma^0m)v^s(\tilde p) = 0$, i.e. $H_{\text{s.p.}}(\mathbf p)v^s(\tilde p) = -E_{\mathbf p}v^s(\tilde p)$. The four vectors $u^1(p), u^2(p), v^1(\tilde p), v^2(\tilde p)$ are orthogonal ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]), each of norm squared $2E_{\mathbf p}$: a basis of $\mathbb C^4$ (PS p. 53).
>
> **4. Solve the ordinary differential equation.** Expanding $\tilde\psi(t, \mathbf p)$ in this eigenbasis, each component evolves with its own phase:
>
> $$
> \tilde\psi(t, \mathbf p) = \frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\Bigl(a^s_{\mathbf p}\,u^s(p)\,e^{-iE_{\mathbf p}t} + \beta^s_{\mathbf p}\,v^s(\tilde p)\,e^{+iE_{\mathbf p}t}\Bigr) ,
> $$
>
> with four free coefficients per $\mathbf p$; the factor $1/\sqrt{2E_{\mathbf p}}$ is a normalization choice, as for the scalar ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]).
>
> **5. Back to space; relabel.** Insert into Step 1. In the second term substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$, and $\tilde p \to p$ because $(E_{\mathbf p}, -(-\mathbf p)) = p$): the exponential becomes $e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x} = e^{ip\cdot x}$ and the spinor $v^s(p)$. Name the coefficient $b^{s\dagger}_{\mathbf p} \equiv \beta^s_{-\mathbf p}$. This gives $\psi$ as stated; $\psi^\dagger$ and $\bar\psi = \psi^\dagger\gamma^0$ follow term by term ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]).
>
> ⚑ By-product: the name $\hat b^\dagger$ on the negative-frequency coefficient is a definition, not a result; whether $\hat b$ or $\hat b^\dagger$ annihilates the vacuum is decided only by positivity of the energy → [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-4|§C5b.3, Remark: Empty and filled are labels]].
>
> **6. Sense.** For the quantum field the coefficients are operator-valued distributions and the integral is read after smearing ([[§C5a.9 Plane-Wave Solutions#^rem-c5a-9-6|§C5a.9, Remark: In what sense a general solution is a superposition of these plane waves]]). The spinors are smooth and polynomially bounded in $\mathbf p$ for $m > 0$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|Theorem §C5a.9.6]]), so for $f \in \mathcal S(\mathbb R^3, \mathbb C^4)$ the functions $g_s(\mathbf p) = u^{s\dagger}(p)\tilde f(\mathbf p)/\sqrt{2E_{\mathbf p}}$ and $h_s(\mathbf p) = \tilde f(-\mathbf p)^\dagger v^s(p)/\sqrt{2E_{\mathbf p}}$ are in $\mathcal S$, and at $t = 0$, $\int d^3x\,f^\dagger\hat\psi = \sum_s\bigl(\hat a^s(g_s) + \hat b^{s\dagger}(h_s)\bigr)$ with the smeared operators of [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]].
>
> **What the derivation shows**
> - Four modes per momentum: two eigenvalues $\pm E_{\mathbf p}$ of $H_{\text{s.p.}}(\mathbf p)$, each twice; the negative-energy eigenvectors appear, after relabelling, as $v^s(p)e^{+ip\cdot x}$.
> - Assumptions used: $m > 0$ (smooth spinors), fall-off or smearing.
> - Lecture 10 did not derive the expansion: it posited it by analogy with the scalar and checked it through the anticommutators ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-1|Remark: Reading the expansion]]). The two routes meet as for the scalar ([[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|§C2b.1, Remark: Two routes that meet]]).
> - Used next: mode extraction ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]]) and $\hat H$ in modes ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]]).

^der-c5b-2-1

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-7|Def. §C5a.1.7]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-11|Theorem §C5a.1.11]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-1|Theorem §C5a.9.1]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-2|Theorem §C5a.9.2]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|Theorem §C5a.9.6]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]

*Procedure:* [[P1 Canonical Quantization#^p1-5|P1, step 5]]

> [!remark] Remark: Reading the expansion
> Each ingredient of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] has a counterpart in the scalar field ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]), and each change has a reason (Lecture 10):
> - *Hats* mark the operators, as in the lecture: $\hat\psi$, $\hat a$, $\hat b$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^cau-c5b-1-1|§C5b.1, Caution: Names for the Dirac field and its mode operators across sources]]); the classical field and the c-number spinors $u^s(p)$, $v^s(p)$, $u^{s\dagger}(p)$, $v^{s\dagger}(p)$ carry none. The measure $\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}$ is the scalar's, chosen for the same reason, Lorentz invariance ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]]).
> - *Heisenberg picture.* The exponentials $e^{\mp ip\cdot x}$ contain the time, so the field operator depends on time and the states do not ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]]).
> - *The quantum field satisfies the Dirac equation*, because it is expanded on solutions of it, $u^s(p)e^{-ip\cdot x}$ and $v^s(p)e^{ip\cdot x}$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]]). Where the scalar multiplies each oscillator by a plane wave solving the Klein–Gordon equation, the Dirac field multiplies it by a plane wave times a four-component column solving the Dirac equation. The operator carries the quantum, particle-like aspect; the column and the plane wave carry the wave aspect and all the Lorentz structure.
> - *A complete basis of solutions* needs both frequencies, as $e^{\mp ip\cdot x}$ did for the Klein–Gordon field, and both spins: at each momentum and frequency there are two independent spinors, so there are two oscillators of each kind.
> - *Independent $\hat a$ and $\hat b^\dagger$*, as for the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]; the slide cites Peskin–Schroeder Problem 2.2): the field is not Hermitian, so its particles and antiparticles are distinct.
>
> The lecture posited the expansion by analogy and validated it through the anticommutators ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], second route): "the mode expansion is just a change of variables". The derivation under Theorem §C5b.2.1 derives it from the classical solutions instead.
>
> *Source: Lecture 10, slides 10–12 · the user's PHY 513 notes, Ch. 10 §10.3 ("Reading the expansion") · Lecture 10 (transcript)*

^rem-c5b-2-1

> [!caution] Caution: What anticommutes and what does not
> The operators $\hat\psi$, $\hat a$, $\hat b$ and their adjoints anticommute among themselves ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]). The spinors $u^s(p)$, $v^s(p)$ and the exponentials are ordinary complex numbers (columns of them) and commute with everything. In every computation of this chapter the anticommutators act only on the operators; the $u$'s, $v$'s and exponentials ride along as coefficients. In components the adjoint raises no row-or-column question: the $b$-th component of $\hat\psi^\dagger$ contains $u^{s\ast}_b$, the complex conjugate of the $b$-th entry (Lecture 10: "components of $\hat\psi^\dagger$ are $\hat\psi^\ast$"). Three kinds of order are involved, and only two of them matter:
> 1. *Coefficients may sit anywhere in their term.* $u^s_a(p)$, $v^s_a(p)$ and $e^{\mp ip\cdot x}$ are c-numbers, so $\hat a\,u_a = u_a\,\hat a$. Peskin–Schroeder (eq. (3.99)), Lecture 10 and the user's notes write the operator first, $\hat a^s_{\mathbf p}u^s(p)e^{-ip\cdot x}$; Yu (eq. (5.216)) writes $u\,\hat a\,e^{-ip\cdot x}$: the same term. These notes keep the order operator, spinor, exponential.
> 2. *Operators may not be swapped freely.* $\hat a$, $\hat a^\dagger$, $\hat b$, $\hat b^\dagger$, $\hat\psi$, $\hat\psi^\dagger$ anticommute up to delta functions ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]); every computation of Chapter C5b moves only operators, by these anticommutators, and keeps the sign each exchange costs.
> 3. *Matrices in spinor space may not be swapped.* $\bar u u$ is a number, $u\bar u$ is a $4\times4$ matrix ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|Theorem §C5a.10.2]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]]): this is matrix order, not quantum order. With the indices written the entries are numbers, $\bar u_bu_a = u_a\bar u_b$, and the index placement says which object is meant.
> 4. *Both rules at once.* In $\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]]) the spinor structure is row, matrix, column, and $\hat\psi^\dagger$ stands left of $\hat\psi$ as operators; inside each term the $u$, $v$ and exponential coefficients may still be moved anywhere.
>
> *Source: Lecture 10, slides 12 and 22, and transcript ("a four column worth of different operators"; "these columns have become rows") · the user's PHY 513 notes, Ch. 10 §10.3 (Caution "What anticommutes and what does not") · PS §3.5, eqs. (3.99)–(3.101) · Yu §5.4.2, eq. (5.216) · items 3–4 written here*

^cau-c5b-2-1

> [!theorem] Theorem §C5b.2.2: The Conjugate Fields ψ† and ψ̄
> For $\hat\psi$ of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], the Hermitian conjugate field (a row spinor) is
>
> $$
> \hat\psi^\dagger(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s=1,2}\Bigl(\hat a^{s\dagger}_{\mathbf p}\,u^{s\dagger}(p)\,e^{ip\cdot x} + \hat b^s_{\mathbf p}\,v^{s\dagger}(p)\,e^{-ip\cdot x}\Bigr) ,
> $$
>
> and the Dirac conjugate $\hat{\bar\psi} = \hat\psi^\dagger\gamma^0$ ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]) is
>
> $$
> \hat{\bar\psi}(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s=1,2}\Bigl(\hat b^s_{\mathbf p}\,\bar v^s(p)\,e^{-ip\cdot x} + \hat a^{s\dagger}_{\mathbf p}\,\bar u^s(p)\,e^{ip\cdot x}\Bigr) .
> $$
>
> $\hat\psi$ annihilates particles ($\hat a$) and creates antiparticles ($\hat b^\dagger$); $\hat\psi^\dagger$ and $\hat{\bar\psi}$ both annihilate antiparticles ($\hat b$) and create particles ($\hat a^\dagger$), with the same operator content, because $\gamma^0$ only rearranges spinor components. $\hat\psi^\dagger$ is the field in the canonical structure: the conjugate momentum $\hat\pi_\psi = i\hat\psi^\dagger$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]) has the mode expansion $i$ times the first formula; $\hat\psi^\dagger$ enters the anticommutators $\{\hat\psi, \hat\psi^\dagger\}$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]) and the bilinears $\hat H = \int\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$, $\hat{\mathbf P} = \int\hat\psi^\dagger(-i\nabla)\hat\psi$ and $\hat Q = \int\hat\psi^\dagger\hat\psi$ ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]]); $\hat{\bar\psi}$ enters the covariant bilinears and the two-point functions.
>
> *Scalar analogue:* $\hat\phi^\dagger$ of the complex field and its momentum $\hat\pi = \dot{\hat\phi}^\dagger$, [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]].
> *Source: Lecture 10, slide 12 ($\hat\psi^\dagger_b$ at $t = 0$ in components, "components of $\hat\psi^\dagger$ are $\hat\psi^\ast$"), slides 18–19 ($\hat\psi^\dagger$ in the Hamiltonian) and slide 22 ($\hat{\bar\psi}$) · the user's PHY 513 notes, Ch. 10 §10.3 (Derivation "The conjugate field": Hermitian conjugate, then $\gamma^0$ on the right) · PS §3.5, eqs. (3.99)–(3.100) ($\hat\psi$ and $\hat{\bar\psi}$; $\hat\psi^\dagger$ is not displayed there) · Yu §5.4.2, eqs. (5.216)–(5.218) ($\hat\psi$, $\hat\psi^\dagger$, $\hat{\bar\psi}$), and §5.4.3, eq. (5.220) ($\hat\pi = i\hat\psi^\dagger$ in modes)*

^thm-c5b-2-2

> [!derivation]- Derivation
> **1. The adjoint of one term.** Each term of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] is a product $c\,\hat A\,w$ of a complex number $c$ (the exponential and the real prefactor), an operator $\hat A$ and a constant column spinor $w$ whose entries are numbers. Component by component, $(c\,\hat A\,w_b)^\dagger = c^{\ast}\hat A^\dagger w_b^{\ast}$, since the adjoint of a c-number times an operator is the complex conjugate times the adjoint operator; collecting the components $w_b^{\ast}$ into a row is $w^\dagger$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|Caution: What anticommutes and what does not]]: "components of $\hat\psi^\dagger$ are $\hat\psi^\ast$"). The c-numbers commute with $\hat A^\dagger$, so the order in which they are written is a convention; it is fixed here as operator, then row spinor, then exponential.
>
> **2. The four ingredients.** The exponentials: $(e^{-ip\cdot x})^{\ast} = e^{ip\cdot x}$ and $(e^{ip\cdot x})^{\ast} = e^{-ip\cdot x}$, since $p\cdot x$ is real. The operators: $(\hat a^s_{\mathbf p})^\dagger = \hat a^{s\dagger}_{\mathbf p}$ and $(\hat b^{s\dagger}_{\mathbf p})^\dagger = \hat b^s_{\mathbf p}$, because the adjoint of an adjoint is the operator itself. The spinors: the column $u^s(p)$ becomes the row $u^{s\dagger}(p)$, the column $v^s(p)$ the row $v^{s\dagger}(p)$. The prefactor $(2\pi)^{-3}(2E_{\mathbf p})^{-1/2}$ is real and unchanged. Hence
>
> $$
> \bigl(\hat a^s_{\mathbf p}\,u^s(p)\,e^{-ip\cdot x}\bigr)^\dagger = \hat a^{s\dagger}_{\mathbf p}\,u^{s\dagger}(p)\,e^{ip\cdot x}, \qquad \bigl(\hat b^{s\dagger}_{\mathbf p}\,v^s(p)\,e^{ip\cdot x}\bigr)^\dagger = \hat b^s_{\mathbf p}\,v^{s\dagger}(p)\,e^{-ip\cdot x} .
> $$
>
> **3. Through the integral and the sum.** The adjoint passes through $\int d^3p$ and $\sum_s$ because the expansion is read with smeared operators ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]]): the adjoint of $\hat a^s(g)$ is $\hat a^{s\dagger}(g)$, and that of $\int d^3x\,f^\dagger\hat\psi$ is $\int d^3x\,\hat\psi^\dagger f$. Summing the two terms of Step 2 gives the formula for $\hat\psi^\dagger$. The momentum field follows by multiplying with the constant $i$: $\hat\pi_\psi = i\hat\psi^\dagger$ term by term.
>
> **4. Multiply by $\gamma^0$ on the right.** The rows become barred spinors, $u^{s\dagger}(p)\gamma^0 = \bar u^s(p)$ and $v^{s\dagger}(p)\gamma^0 = \bar v^s(p)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]], applied to the c-number spinors), whose explicit rows $\bar u^s(p) = (\xi^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \xi^{s\dagger}\sqrt{p\cdot\sigma})$ and $\bar v^s(p) = (-\eta^{s\dagger}\sqrt{p\cdot\bar\sigma},\ \eta^{s\dagger}\sqrt{p\cdot\sigma})$ are [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]. The operators are untouched: $\gamma^0$ acts on the spinor index only. ⚑ By-product: each term of $\hat{\bar\psi}$ solves the conjugate equation from the right, $\bar u^s(p)(\slashed{p} - m) = 0$ and $\bar v^s(p)(\slashed{p} + m) = 0$ (same theorems, part 2), so $\hat{\bar\psi}$ satisfies the conjugate Dirac equation $i\,\partial_\mu\hat{\bar\psi}\,\gamma^\mu + m\hat{\bar\psi} = 0$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|Theorem §C5a.7.6]], 2) term by term: on $e^{ip\cdot x}$, $i\partial_\mu \to i(ip_\mu) = -p_\mu$, giving $-\bar u^s(\slashed{p} - m) = 0$; on $e^{-ip\cdot x}$, $i\partial_\mu \to i(-ip_\mu) = p_\mu$, giving $\bar v^s(\slashed{p} + m) = 0$.
>
> **5. Collect.** Writing the $\hat b$ term first gives the displayed formula for $\hat{\bar\psi}$.
>
> **What the derivation shows**
> - Daggering exchanges the operator content: $(\hat a, \hat b^\dagger) \to (\hat a^\dagger, \hat b)$. The positive-frequency part of $\hat\psi^\dagger$, and so of $\hat{\bar\psi}$, carries $\hat b$: both are $\hat\psi$ with particles and antiparticles interchanged → [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-2|Remark: ψ̄ is ψ with particles and antiparticles interchanged]].
> - ⚑ By-product: the conjugate momentum field has its own mode expansion, $\hat\pi_\psi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{i}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p}u^{s\dagger}(p)e^{ip\cdot x} + \hat b^s_{\mathbf p}v^{s\dagger}(p)e^{-ip\cdot x}\bigr)$ (Yu, eq. (5.220)), not a time derivative of $\hat\psi$ as for the scalar ($\hat\pi = \dot{\hat\phi}$), because the Dirac Lagrangian is first order ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-3|§C5b.1, Remark: A first-order system]]).
> - Used next: the extraction of $\hat a^\dagger$ and $\hat b$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]]), the mode algebra (Theorem §C5b.2.4, second route), $\hat H$, $\hat{\mathbf P}$ and $\hat Q$ in modes ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]]) and the two-point functions $\langle0|\hat\psi\hat{\bar\psi}|0\rangle$, $\langle0|\hat{\bar\psi}\hat\psi|0\rangle$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]).

^der-c5b-2-2

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]]

> [!remark] Remark: ψ̄ is ψ with particles and antiparticles interchanged
> Roughly, $\hat{\bar\psi}$ is $\hat\psi$ with the roles of $\hat a$ and $\hat b$ exchanged ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]). Neither field is preferred: particles and antiparticles are physically equivalent, each with two spin states and the same energies ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]]), and which of them is called the particle is a convention. Lecture 12 makes the symmetry that exchanges them explicit: charge conjugation (QFT C9, planned).
>
> *Source: Lecture 10, slide 22 ("Roughly: ψ̄ has particle and anti-particle interchanged") and transcript · the user's PHY 513 notes, Ch. 10 §10.3*

^rem-c5b-2-2

> [!remark] Remark: A spinor-valued operator, component by component
> $u^s(p)$ is a column of four complex numbers $u^s_a(p)$, $a = 1, \dots, 4$, and $\hat\psi(x)$ is a column of four operators,
>
> $$
> \hat\psi_a(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s=1,2}\Bigl(\hat a^s_{\mathbf p}\,u^s_a(p)\,e^{-ip\cdot x} + \hat b^{s\dagger}_{\mathbf p}\,v^s_a(p)\,e^{ip\cdot x}\Bigr) ,
> $$
>
> each a single operator, a linear combination of mode operators with numerical coefficients ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]); $(\hat a\,u)_a = \hat a\,u_a = u_a\,\hat a$. $\hat\psi^\dagger$ is the row $(\hat\psi^\dagger_1, \dots, \hat\psi^\dagger_4)$ whose $b$-th entry contains $\hat a^{s\dagger}_{\mathbf p}\,u^{s\ast}_b(p)$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]): the number is complex-conjugated, the operator daggered, and column to row is the transposition. Computing one entry at a time, with $u^{s\ast}_b$ rather than $u^\dagger$, is how Lecture 10 does the anticommutator check ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-4b|Derivation §C5b.2.4, second route]]): no row-or-column question can then go wrong.
>
> *Source: Lecture 10, slide 12 ($\hat\psi_a$ and $\hat\psi^\dagger_b$ at $t = 0$; "components of $\hat\psi^\dagger$ are $\hat\psi^\ast$; $a$, $b$ are spinor indices") and transcript · the user's PHY 513 notes, Ch. 10 §10.3 and §10.4 (Derivation "Oscillator anticommutators give the field anticommutators", Step 1: "the question of rows versus columns does not arise")*

^rem-c5b-2-3

> [!caution] Caution: u is not a four-vector
> $u^s(p)$ and $v^s(p)$ have four components, but the label $a$ is a spinor index, not a spacetime index $\mu$. Under a Lorentz transformation the components mix with $\Lambda_{1/2}$ of the Dirac representation ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]), not with $\Lambda$, and a rotation by $2\pi$ changes their sign ([[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-1|§C5a.3, Remark: Why half the angle]]). That a Dirac spinor has as many components as a four-vector is a coincidence of four dimensions ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]]). These notes write Latin $a, b$ for spinor indices and Greek $\mu, \nu$ for spacetime indices.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (paragraph "A coincidence of dimension", the table of indices), §8.5 ("a four-spinor, not a four-vector") · the index convention written here*

^cau-c5b-2-2

> [!remark]- ★ Remark: Where the Grassmann numbers go
> In the path-integral formulation (QFT C11, planned) the classical Dirac field is Grassmann-valued: its expansion has the form of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] with anticommuting numbers in place of $\hat a^s_{\mathbf p}$ and $\hat b^{s\dagger}_{\mathbf p}$. The spinors $u^s(p)$, $v^s(p)$ and the exponentials stay ordinary commuting numbers: the Grassmann property sits in the coefficients that replace the mode operators, exactly where the anticommutation sits here (item 2 of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|Caution: What anticommutes and what does not]]; the graded bracket of such variables: [[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-4|★ Def. §C5b.1.4]]).
>
> *Source: written here; none of the course sources (Lecture 10, the user's PHY 513 notes, PS §3.5, Yu §5.4) discusses it at this point*

^rem-c5b-2-4

## Mode extraction

> [!theorem] Theorem §C5b.2.3: Mode Extraction
> At any time $t$, with the spinors of [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-9|Theorem §C5a.9.9]] and [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]],
>
> $$
> \hat a^s_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\;e^{ip\cdot x}\,u^{s\dagger}(p)\,\hat\psi(x), \qquad \hat b^{s\dagger}_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\;e^{-ip\cdot x}\,v^{s\dagger}(p)\,\hat\psi(x) ,
> $$
>
> and by adjoints, with $\hat\psi^\dagger$ of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], $\hat a^{s\dagger}_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{-ip\cdot x}\hat\psi^\dagger(x)u^s(p)$, $\hat b^s_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\hat\psi^\dagger(x)v^s(p)$: $\hat a$ and $\hat b^\dagger$ come from $\hat\psi$, $\hat a^\dagger$ and $\hat b$ from $\hat\psi^\dagger$. The right sides do not depend on $t$. As identities of operator-valued distributions in $\mathbf p$ they hold after smearing, $\hat a^s(g) = \int d^3x\,(F^s_g)^\dagger\hat\psi$ with $F^s_g(x) = \int\frac{d^3p}{(2\pi)^3}\frac{g(\mathbf p)}{\sqrt{2E_{\mathbf p}}}u^s(p)e^{-ip\cdot x}$.
>
> *Scalar analogue:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], there with the indefinite Klein–Gordon product.
> *Source: Yu §5.4.3, eqs. (5.224)–(5.227) · the user's pre-course notes, §5.5 (verified there)*

^thm-c5b-2-3

> [!derivation]- Derivation
> **1. Substitute.** Insert [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] with variable $\mathbf q$ and spin label $r$:
>
> $$
> \int d^3x\,e^{ip\cdot x}u^{s\dagger}(p)\hat\psi(x) = \int d^3x\int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r\Bigl(u^{s\dagger}(p)u^r(q)\,\hat a^r_{\mathbf q}\,e^{i(p-q)\cdot x} + u^{s\dagger}(p)v^r(q)\,\hat b^{r\dagger}_{\mathbf q}\,e^{i(p+q)\cdot x}\Bigr) .
> $$
>
> **2. Split the exponentials.** $e^{i(p-q)\cdot x} = e^{i(E_{\mathbf p} - E_{\mathbf q})t}e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x}$ and $e^{i(p+q)\cdot x} = e^{i(E_{\mathbf p} + E_{\mathbf q})t}e^{-i(\mathbf p + \mathbf q)\cdot\mathbf x}$; the time phases ride along ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], the split-exponential rule; exchange of the $\mathbf x$- and $\mathbf q$-integrals valid for wave packets).
>
> **3. The $d^3x$ integrals.** $\int d^3x\,e^{-i(\mathbf p \mp \mathbf q)\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p \mp \mathbf q)$, identities in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]).
>
> **4. Integrate the deltas over $\mathbf q$.** First term: $\mathbf q = \mathbf p$, phase $1$, $E_{\mathbf q} = E_{\mathbf p}$; the smooth prefactor is evaluated on the support ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1). Second term: $\mathbf q = -\mathbf p$, so $q = (E_{\mathbf p}, -\mathbf p) = \tilde p$ and the phase is $e^{2iE_{\mathbf p}t}$:
>
> $$
> \frac{1}{\sqrt{2E_{\mathbf p}}}\sum_r\Bigl(u^{s\dagger}(p)u^r(p)\,\hat a^r_{\mathbf p} + u^{s\dagger}(p)v^r(\tilde p)\,\hat b^{r\dagger}_{-\mathbf p}\,e^{2iE_{\mathbf p}t}\Bigr) .
> $$
>
> **5. Orthogonality.** $u^{s\dagger}(p)u^r(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]]); $u^{s\dagger}(p)v^r(\tilde p) = 0$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]). Dropped: the whole $\hat b^\dagger$ term, by the orthogonality of the $\pm E$ eigenvectors of $H_{\text{s.p.}}(\mathbf p)$, together with its time dependence. What remains is $\sqrt{2E_{\mathbf p}}\,\hat a^s_{\mathbf p}$; divide by $\sqrt{2E_{\mathbf p}}$.
>
> **6. The $\hat b^\dagger$ formula.** The same steps with $e^{-ip\cdot x}v^{s\dagger}(p)$: the $\hat a$ term now has $\int d^3x\,e^{-i(p+q)\cdot x}$, so $\mathbf q = -\mathbf p$ and the factor $v^{s\dagger}(p)u^r(\tilde p) = 0$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]); the $\hat b^\dagger$ term has $\mathbf q = \mathbf p$, phase $1$, and $v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]]). The adjoint formulas follow by taking adjoints, or by the same steps with the expansion of $\hat\psi^\dagger$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]) in place of that of $\hat\psi$.
>
> **7. Smeared form.** Multiply the $\hat a$ formula by $\overline{g(\mathbf p)}$ and integrate $\int\frac{d^3p}{(2\pi)^3}$: the $\mathbf p$-integral of $\overline{g}\,e^{ip\cdot x}u^{s\dagger}/\sqrt{2E}$ is $(F^s_g)^\dagger$, a Schwartz function of $\mathbf x$ for $g \in \mathcal S$ ([[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|Theorem §C5a.9.6]]), so $\hat a^s(g) = \int d^3x\,(F^s_g)^\dagger\hat\psi$ is a smeared field.
>
> ⚑ By-product: the extraction uses the positive product $\int d^3x\,\psi_1^\dagger\psi_2$, not the indefinite Klein–Gordon product → [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-5|Remark: A positive inner product]].
>
> **What the derivation shows**
> - Time independence comes from the mode functions solving the Dirac equation; the $\hat b^\dagger$ admixture is killed by $u^\dagger(p)v(\tilde p) = 0$, not by a mass-shell argument.
> - Used next: the algebra of the mode operators ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]).

^der-c5b-2-3

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|Theorem §C5a.9.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark] Remark: A positive inner product
> With $f^s_{\mathbf p} \equiv u^s(p)e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$ and $g^s_{\mathbf p} \equiv v^s(p)e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]] reads $\hat a^s_{\mathbf p} = \langle f^s_{\mathbf p}, \hat\psi\rangle$ and $\hat b^{s\dagger}_{\mathbf p} = \langle g^s_{\mathbf p}, \hat\psi\rangle$ with $\langle\chi, \psi\rangle = \int d^3x\,\chi^\dagger\psi$, a positive and conserved product (its density is the charge density $\psi^\dagger\psi$ of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]]). For the scalar the conserved product was the Klein–Gordon one, indefinite, and the negative-frequency coefficient came out with a minus sign, $\hat a^\dagger_{\mathbf p} = -(f^*_{\mathbf p}, \hat\phi)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|§C2a.2, Remark: Why this inner product, and why it is indefinite]]). Here both kinds of coefficient come out with a plus sign. The indefiniteness has not disappeared: it has moved into the energy ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]]).
>
> *Source: Yu §5.4.3, eqs. (5.224)–(5.227) · PS §3.5, p. 53 (eigenfunctions of $H_{\text{s.p.}}$)*

^rem-c5b-2-5

## The anticommutator algebra

> [!theorem] Theorem §C5b.2.4: The Mode Algebra of the Dirac Field
> Under [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], the mode operators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] satisfy
>
> $$
> \{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q) ,
> $$
>
> all other anticommutators vanish (including $\{\hat a, \hat b\}$, $\{\hat a, \hat b^\dagger\}$, $\{\hat a^\dagger, \hat a^\dagger\}$), and conversely these relations give back the principle: anticommutators of fields ⇔ anticommutators of oscillators (Lecture 10). As distributions in $(\mathbf p, \mathbf q)$: smeared as in [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-2|Def. §C2a.2.2]], $\{\hat a^r(g), \hat a^{s\dagger}(h)\} = \{\hat b^r(g), \hat b^{s\dagger}(h)\} = \delta^{rs}\int\frac{d^3p}{(2\pi)^3}\overline gh$, and $\hat a^s(g)$, $\hat b^s(g)$ are bounded with norm $\bigl(\int\frac{d^3p}{(2\pi)^3}|g|^2\bigr)^{1/2}$. Two independent species, each with two spin states.
>
> *Scalar analogue:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]; complex field [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]].
> *Source: Lecture 10, slides 12–13 and 23 · the user's PHY 513 notes, Ch. 10 §10.3 (eq. (diracoscillators)) and §10.4 · PS §3.5, eqs. (3.97), (3.101) · Yu §5.5.2, eqs. (5.240)–(5.246) · the user's pre-course notes, §5.5*

^thm-c5b-2-4

> [!derivation]- Derivation
> **1. The canonical relation in both orders.** With $\hat\pi_b = i\hat\psi^\dagger_b$, $\{\hat\psi_a, \hat\pi_b\} = i\delta_{ab}\delta^3$ is $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]); an anticommutator is symmetric, so also $\{\hat\psi^\dagger_b(\mathbf y), \hat\psi_a(\mathbf x)\} = +\delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **2. $\{\hat a, \hat a^\dagger\}$.** Use [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]] at a common time $t$, $\hat a^r_{\mathbf p}$ with variable $\mathbf x$ and $\hat a^{s\dagger}_{\mathbf q}$ with variable $\mathbf y$. The spinors and phases are c-numbers and come out of the anticommutator ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|Caution: What anticommutes and what does not]]):
>
> $$
> \{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\;e^{ip\cdot x - iq\cdot y}\,u^{r\dagger}_a(p)\,\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\}\,u^s_b(q) = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\;e^{i(p-q)\cdot x}\,u^{r\dagger}(p)u^s(q) ,
> $$
>
> the $\delta^3(\mathbf x - \mathbf y)$ having been integrated over $\mathbf y$ (the pairing of [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]], part 1, with the mode functions made test functions by smearing in momentum) and $\delta_{ab}$ having contracted the spinor indices. Split $e^{i(p-q)\cdot x} = e^{i(E_{\mathbf p} - E_{\mathbf q})t}e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]); the $d^3x$ integral is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). On its support the phase is $1$, $E_{\mathbf q} = E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1) and $u^{r\dagger}(p)u^s(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]]): $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$.
>
> **3. $\{\hat b, \hat b^\dagger\}$: the field relation in the opposite order.** By Theorem §C5b.2.3 (with $\hat\psi^\dagger$ of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]), $\hat b^r_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\hat\psi^\dagger(x)v^r(p)$ is built from $\hat\psi^\dagger$ and $\hat b^{s\dagger}_{\mathbf q} = \frac{1}{\sqrt{2E_{\mathbf q}}}\int d^3y\,e^{-iq\cdot y}v^{s\dagger}(q)\hat\psi(y)$ from $\hat\psi$:
>
> $$
> \{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\;e^{ip\cdot x - iq\cdot y}\,v^{s\dagger}_b(q)\,\{\hat\psi^\dagger_a(\mathbf x), \hat\psi_b(\mathbf y)\}\,v^r_a(p) = +\frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\;e^{i(p-q)\cdot x}\,v^{s\dagger}(q)v^r(p)
> $$
>
> by Step 1. The same delta and $v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]]) give $+(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, the normal sign (Yu, after eq. (5.242)). ⚑ By-product: $\hat\psi^\dagger$ stands to the left of $\hat\psi$ here, the opposite order to Step 2; for an anticommutator this costs nothing, for a commutator it costs a sign → [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-7|Remark: One algebraic fact]].
>
> **4. Mixed: $\{\hat a, \hat b\}$.** $\hat a^r_{\mathbf p}$ comes from $\hat\psi$ and $\hat b^s_{\mathbf q}$ from $\hat\psi^\dagger$: $\{\hat a^r_{\mathbf p}, \hat b^s_{\mathbf q}\} = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\,e^{ip\cdot x + iq\cdot y}u^{r\dagger}_a(p)\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\}v^s_b(q) = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p+q)\cdot x}u^{r\dagger}(p)v^s(q)$. Now $e^{i(p+q)\cdot x} = e^{i(E_{\mathbf p} + E_{\mathbf q})t}e^{-i(\mathbf p + \mathbf q)\cdot\mathbf x}$, the $d^3x$ integral is $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$, and on its support $q = (E_{\mathbf p}, -\mathbf p) = \tilde p$: the result is $\frac{e^{2iE_{\mathbf p}t}}{2E_{\mathbf p}}(2\pi)^3\delta^3(\mathbf p + \mathbf q)\,u^{r\dagger}(p)v^s(\tilde p) = 0$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]). Dropped: the whole term, because the spinor product vanishes on the support of δ (the $\pm E_{\mathbf p}$ eigenvectors of $H_{\text{s.p.}}(\mathbf p)$ are orthogonal).
>
> **5. Like pairs and the rest.** $\{\hat a, \hat a\}$ and $\{\hat a, \hat b^\dagger\}$ contain only $\{\hat\psi, \hat\psi\} = 0$; $\{\hat b, \hat b\}$ and $\{\hat a^\dagger, \hat b\}$ only $\{\hat\psi^\dagger, \hat\psi^\dagger\} = 0$; the remaining ones are adjoints of these.
>
> **6. Smeared, and bounded.** Pairing with $\overline{g(\mathbf p)}h(\mathbf q)$ and integrating gives the smeared relations (as in [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]). With $\hat A = \hat a^s(g)$, $\{\hat A, \hat A\} = 0$ and $\{\hat A, \hat A^\dagger\} = \int\frac{d^3p}{(2\pi)^3}|g|^2$: Steps 2–4 of [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-8|Derivation §C5b.1.8]] give $\|\hat a^s(g)\|^2 = \int\frac{d^3p}{(2\pi)^3}|g|^2$; the same for $\hat b$.
>
> **What the derivation shows**
> - Nothing in the computation depends on the statistics except the symmetry of the bracket in Step 3, and with the anticommutator the antiparticle algebra has the positive sign.
> - $(\hat a^{s\dagger}(g))^2 = 0$: each smeared mode is occupied at most once.
> - Direction: fields ⇒ oscillators, as Yu, eqs. (5.240)–(5.246). The lecture went the other way (second route below); together the two directions make the mode expansion a change of variables.

^der-c5b-2-4

*Uses:* [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-8|Theorem §C5b.1.8]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]

> [!derivation]- Derivation (second route, Lecture 10: from the oscillators back to the field)
> **1. Equal time, with a common Fourier factor.** At $t = 0$ (any common time works the same way), relabel the antiparticle term of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] by $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1: Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$; allowed because $\mathbf p$ runs over all values), so that both terms carry the same $e^{i\mathbf p\cdot\mathbf x}$; the relabelled spinor is $v^s$ at the same energy and flipped momentum, $v^s(\tilde p)$. The second field is $\hat\psi^\dagger$ of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]] in components at $t = 0$, relabelled the same way, with its own variables $\mathbf p'$, $s$:
>
> $$
> \hat\psi_a(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\sqrt{2E_{\mathbf p}}}\sum_r\Bigl(\hat a^r_{\mathbf p}u^r_a(p) + \hat b^{r\dagger}_{-\mathbf p}v^r_a(\tilde p)\Bigr), \qquad \hat\psi^\dagger_b(\mathbf y) = \int\frac{d^3p'}{(2\pi)^3}\frac{e^{-i\mathbf p'\cdot\mathbf y}}{\sqrt{2E_{\mathbf p'}}}\sum_s\Bigl(\hat a^{s\dagger}_{\mathbf p'}u^{s\ast}_b(p') + \hat b^s_{-\mathbf p'}v^{s\ast}_b(\tilde p')\Bigr) .
> $$
>
> In components $u^{s\ast}_b$ is the complex conjugate of the $b$-th entry, so no row or column has to be tracked ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|Caution: What anticommutes and what does not]]).
>
> **2. The operators first: only $\hat a$ with $\hat a^\dagger$ and $\hat b^\dagger$ with $\hat b$ talk.** Of the four products, $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf p'}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf p')$ and $\{\hat b^{r\dagger}_{-\mathbf p}, \hat b^s_{-\mathbf p'}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf p')$ (the statement, with $\delta^3(-\mathbf p + \mathbf p') = \delta^3(\mathbf p - \mathbf p')$); $\{\hat a, \hat b\}$ and $\{\hat b^\dagger, \hat a^\dagger\}$ vanish ($\hat a$ and $\hat b$ are different operators; and two annihilators or two creators anticommute anyway). Each surviving delta sets $\mathbf p' = \mathbf p$ and $s = r$, cancels one $(2\pi)^3$ and one integral, and turns $1/\sqrt{2E_{\mathbf p}}\sqrt{2E_{\mathbf p'}}$ into $1/2E_{\mathbf p}$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1):
>
> $$
> \{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \int\frac{d^3p}{(2\pi)^3}\,\frac{e^{i\mathbf p\cdot(\mathbf x - \mathbf y)}}{2E_{\mathbf p}}\sum_{s=1,2}\Bigl(u^s_a(p)u^{s\ast}_b(p) + v^s_a(\tilde p)v^{s\ast}_b(\tilde p)\Bigr) .
> $$
>
> **3. Then the spin sum, with the $\gamma^0$ put back.** The completeness relations are for $u\bar u$ and $v\bar v$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]]), and $\bar u_c = (u^\dagger\gamma^0)_c$; multiplying on the right by $\gamma^0$ and using $(\gamma^0)^2 = 1$: $\sum_su^s(p)u^{s\dagger}(p) = (\slashed{p} + m)\gamma^0$ and $\sum_sv^s(\tilde p)v^{s\dagger}(\tilde p) = (\slashed{\tilde p} - m)\gamma^0$, with $\slashed{\tilde p} = \gamma^0E_{\mathbf p} + \gamma^ip^i$. (Asked in the lecture: the $\gamma^0$ must be put back, because the spin sums contain $\bar u$, not $u^\dagger$. Slide 13 writes $\bar u^{s\dagger}_b$, $\bar v^{s\dagger}_b$ in its completeness line; the relations contain $\bar u^s_b$, $\bar v^s_b$.) Adding, the masses cancel and so do the spatial parts, $\slashed{p} + \slashed{\tilde p} = (\gamma^0E_{\mathbf p} - \gamma^ip^i) + (\gamma^0E_{\mathbf p} + \gamma^ip^i) = 2E_{\mathbf p}\gamma^0$:
>
> $$
> \sum_{s=1,2}\Bigl(u^s_a(p)u^{s\ast}_b(p) + v^s_a(\tilde p)v^{s\ast}_b(\tilde p)\Bigr) = \bigl[(\slashed{p} + m) + (\slashed{\tilde p} - m)\bigr]_{ac}(\gamma^0)_{cb} = 2E_{\mathbf p}(\gamma^0\gamma^0)_{ab} = 2E_{\mathbf p}\,\delta_{ab} .
> $$
>
> **4. Last, the Fourier integral.** The energies cancel, and $\int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot(\mathbf x - \mathbf y)} = \delta^3(\mathbf x - \mathbf y)$, an identity in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]): $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **5. The other two relations.** $\{\hat\psi, \hat\psi\}$ contains only $\{\hat a, \hat b^\dagger\}$, $\{\hat a, \hat a\}$, $\{\hat b^\dagger, \hat b^\dagger\}$, $\{\hat b^\dagger, \hat a\}$; $\{\hat\psi^\dagger, \hat\psi^\dagger\}$ only their adjoints: all zero.
>
> **What the derivation shows**
> - Both frequencies and both spins of the classical solutions were needed: without the $v$'s the spin sum gives $(\slashed{p} + m)\gamma^0$, not a multiple of the identity, and the field would not be local ([[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-2|§C5a.10, Remark: Why neither spin sum is the identity]]).
> - The relabelling $\mathbf p \to -\mathbf p$ is the price of a common Fourier factor; it is why the antiparticle spinor appears at $\tilde p$ (Lecture 10).
>
> *Source: Lecture 10, slides 12–13 and transcript · the user's PHY 513 notes, Ch. 10 §10.4 (Derivation "Oscillator anticommutators give the field anticommutators") · PS §3.5, eq. (3.89) (with anticommutators in place of their commutators)*

^der-c5b-2-4b

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-6|P1, step 6]]

> [!remark] Remark: One thing at a time
> Many things happen at once in the second route of Derivation §C5b.2.4: operators, spinor components, Fourier factors, the relabelling $\mathbf p \to -\mathbf p$. Lecture 10's advice: do them one at a time — first the operators (only $\hat a$ with $\hat a^\dagger$ and $\hat b^\dagger$ with $\hat b$ talk; spinors and exponentials are coefficients), then the spin sum, then the Fourier integral — and practise by writing the two expansions down at home without looking. The slips the lecture made and corrected on the board mark the traps: the second integral needs its own variables ($\mathbf p'$, $s$), the second field is evaluated at $\mathbf y$, the spinors carry four-momenta (the relabelled one is $\tilde p$, not just "$-\mathbf p$"), and the completeness relations contain $\bar u$, not $u^\dagger$, so a $\gamma^0$ must be put back.
>
> *Source: Lecture 10 (transcript) · the user's PHY 513 notes, Ch. 10 §10.4 ("Advice from the lecture")*

^rem-c5b-2-6

## Where the commutator version fails (first checkpoint)

Lecture 10 did the quantization with anticommutators only and named the places where commutators would fail ([[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-1|§C5b.1, Remark: Lecture 10's route]]). The first is the mode algebra itself.

> [!theorem] Theorem §C5b.2.5: Commutators Give the Antiparticle Modes a Negative Algebra
> Suppose the canonical pairs $(\psi_a, \pi_a = i\psi^\dagger_a)$ of [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] are quantized, as operators $\hat\psi_a$, $\hat\pi_a = i\hat\psi^\dagger_a$, by the bosonic rule of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], i.e. at equal times
>
> $$
> [\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)] = \delta_{ab}\,\delta^3(\mathbf x - \mathbf y), \qquad [\hat\psi_a(\mathbf x), \hat\psi_b(\mathbf y)] = [\hat\psi^\dagger_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)] = 0 .
> $$
>
> Then the mode operators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] obey
>
> $$
> [\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}] = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q), \qquad [\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}] = -(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q) ,
> $$
>
> and all other commutators, including the mixed ones, vanish (identities of distributions in $(\mathbf p, \mathbf q)$; smeared, $[\hat b^r(g), \hat b^{s\dagger}(h)] = -\delta^{rs}\int\frac{d^3p}{(2\pi)^3}\overline gh$).
>
> *Scalar analogue:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], where the same computation gives the positive sign for both species.
> *Source: Yu §5.5.1, eqs. (5.228)–(5.236) · the user's pre-course notes, §5.5 ("Failure of canonical commutation relations") · PS §3.5, eqs. (3.86)–(3.90) · Lecture 10, slide 6 and transcript (the commutator version, not computed in the lecture)*

^thm-c5b-2-5

> [!derivation]- Derivation
> **1. The canonical relation in terms of $\hat\psi^\dagger$.** $[\hat\psi_a, \hat\pi_b] = i\delta_{ab}\delta^3$ with $\hat\pi_b = i\hat\psi_b^\dagger$ is $[\hat\psi_a, \hat\psi_b^\dagger] = \delta_{ab}\delta^3$; reversed, $[\hat\psi_b^\dagger(\mathbf y), \hat\psi_a(\mathbf x)] = -\delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **2. $[\hat a, \hat a^\dagger]$.** With [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]] at a common time $t$, pulling the c-number spinors and phases out of the commutator,
>
> $$
> [\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}] = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\;e^{ip\cdot x - iq\cdot y}\,u^{r\dagger}_a(p)\,[\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)]\,u^s_b(q) = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\;e^{i(p-q)\cdot x}\,u^{r\dagger}(p)u^s(q) ,
> $$
>
> the $\delta^3(\mathbf x - \mathbf y)$ having been integrated over $\mathbf y$ (the pairing of [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], with the mode functions made test functions by smearing in momentum). The $d^3x$ integral is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)e^{i(E_{\mathbf p} - E_{\mathbf q})t}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); on its support the phase is $1$ and $u^{r\dagger}(p)u^s(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]]): $+(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$.
>
> **3. $[\hat b, \hat b^\dagger]$: the same relation in the opposite order.** Now $\hat b^r_{\mathbf p}$ is built from $\hat\psi^\dagger$ and $\hat b^{s\dagger}_{\mathbf q}$ from $\hat\psi$:
>
> $$
> [\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}] = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\;e^{ip\cdot x - iq\cdot y}\,v^{s\dagger}_b(q)\,[\hat\psi^\dagger_a(\mathbf x), \hat\psi_b(\mathbf y)]\,v^r_a(p) = -\frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\;e^{i(p-q)\cdot x}\,v^{s\dagger}(q)v^r(p) ,
> $$
>
> by Step 1. The same delta and $v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]]) give $-(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$. ⚑ By-product: the sign comes only from the order in which the canonical relation enters → [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-7|Remark: One algebraic fact]].
>
> **4. Mixed: $[\hat a, \hat b]$.** Both $\hat a^r_{\mathbf p}$ (from $\hat\psi$) and $\hat b^s_{\mathbf q}$ (from $\hat\psi^\dagger$) enter: $[\hat a^r_{\mathbf p}, \hat b^s_{\mathbf q}] = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p+q)\cdot x}u^{r\dagger}(p)v^s(q) = \frac{e^{2iE_{\mathbf p}t}}{2E_{\mathbf p}}(2\pi)^3\delta^3(\mathbf p + \mathbf q)\,u^{r\dagger}(p)v^s(\tilde p) = 0$ ([[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]). Dropped: the spinor product, on the support of δ.
>
> **5. The rest.** $[\hat a, \hat a]$ and $[\hat a, \hat b^\dagger]$ involve only $[\hat\psi, \hat\psi] = 0$; $[\hat b, \hat b]$ and $[\hat a^\dagger, \hat b]$ only $[\hat\psi^\dagger, \hat\psi^\dagger] = 0$; the remaining ones are adjoints of these.
>
> **6. Smeared.** Multiply Step 3 by $\overline{g(\mathbf p)}h(\mathbf q)$ and integrate (as in [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]): $[\hat b^r(g), \hat b^{s\dagger}(h)] = -\delta^{rs}\int\frac{d^3p}{(2\pi)^3}\overline gh$.
>
> **What the derivation shows**
> - The computation is that of the scalar fields ([[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-3|Derivation §C2a.5.3]]) with the positive Dirac product in place of the Klein–Gordon product; the minus sign is not a slip but the order of $\hat\psi^\dagger$ and $\hat\psi$.

^der-c5b-2-5

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]

> [!remark] Remark: One algebraic fact
> $\hat a$ is extracted from $\hat\psi$ and $\hat a^\dagger$ from $\hat\psi^\dagger$, but $\hat b$ from $\hat\psi^\dagger$ and $\hat b^\dagger$ from $\hat\psi$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]]). So $[\hat a, \hat a^\dagger]$ contains $[\hat\psi, \hat\psi^\dagger]$ and $[\hat b, \hat b^\dagger]$ contains $[\hat\psi^\dagger, \hat\psi]$: the same canonical relation, in the opposite order. A commutator changes sign under that exchange, $[\hat\psi^\dagger, \hat\psi] = -[\hat\psi, \hat\psi^\dagger]$; an anticommutator does not, $\{\hat\psi^\dagger, \hat\psi\} = \{\hat\psi, \hat\psi^\dagger\}$. This single fact is the whole difference between the two quantizations of the Dirac field.
>
> *Source: the user's pre-course notes, §5.5 ("the same canonical relation enters the two computations in opposite order")*

^rem-c5b-2-7

> [!remark] Remark: What the field adds to the anticommutators of second quantization
> The relations of [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] have the form of the field-operator relations of nonrelativistic second quantization ([[§C12.2★ Second Quantization#^thm-c12-2-3|QM Theorem §C12.2.3]], fermion sign), and the mode algebra of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]] has the form of [[§C12.2★ Second Quantization#^thm-c12-2-1|QM Theorem §C12.2.1]]. Rule 2 applies; the field adds:
> - **Two kinds of quanta in one local field.** The nonrelativistic $\hat\psi(\mathbf x)$ contains only annihilators and $\hat\psi^\dagger(\mathbf x)|\mathbf 0\rangle$ is a particle at $\mathbf x$. The Dirac $\hat\psi$ annihilates fermions *and* creates antifermions ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]); it does not annihilate the vacuum.
> - **Spinors and relativistic normalization.** The mode functions carry $u^s$, $v^s$ and the factors $(2\pi)^3$, $1/\sqrt{2E_{\mathbf p}}$; the covariant combination is $\{\hat\psi, \hat{\bar\psi}\} = \gamma^0\delta^3$ at equal times ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]).
> - **The statistics is not chosen.** Quantum Mechanics postulates the symmetry type per species ([[§C12.1★ Permutation Symmetry and the Symmetrization Postulate#^pr-c12-1-4|QM Principle §C12.1.4]]); here commutators are excluded by positivity ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]) and by causality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]]).
>
> *Source: the user's pre-course notes, §5.5 ("this single algebraic fact is the entire difference") · PS §3.5, pp. 57–58*

^rem-c5b-2-8

> [!remark]- Connections
> - The mode functions $u^s(p)e^{-ip\cdot x}$ and $v^s(p)e^{ip\cdot x}$ are the eigenfunctions of the single-particle Hamiltonian with eigenvalues $\pm E_{\mathbf p}$, so the expansion diagonalizes the classical Hamiltonian, as the scalar's expansion decoupled the field into oscillators — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]].
> - The positive Dirac product $\int\psi^\dagger\psi$ replaces the indefinite Klein–Gordon product of the scalar; it is the classical charge, which is why the antiparticle coefficients come out without a minus sign — [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-5|Remark: A positive inner product]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]].
> - "Anticommutators of fields ⇔ anticommutators of oscillators" is the fermionic version of the scalar's mode algebra; in both, the mode expansion is a change of variables and the algebra follows from the canonical relations — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]].
> - The spin sums enter here as the completeness of the four spinors at one momentum; the same sums are the numerators of the two-point functions and the propagator — [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
> - The commutator checkpoint is the same computation as the complex scalar's mode algebra with the Dirac product in place of the Klein–Gordon one; the sign it produces reappears as negative norms or unbounded energy and as acausal propagation — [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]].
> - A change of basis of spinor space acts on the index $a$ of $\hat\psi_a$ and of $u^s_a(p)$, $v^s_a(p)$ by one matrix $U$ and never on the mode operators; with a unitary $U$ the anticommutators and $\bar{\hat\psi}$ keep their form — [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-2|Theorem §C5a.1.2]], [[§C5a.2 The Dirac Form#^thm-c5a-2-4|Theorem §C5a.2.4]].
