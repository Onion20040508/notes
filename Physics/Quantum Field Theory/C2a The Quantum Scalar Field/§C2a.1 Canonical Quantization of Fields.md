---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2a.2 Mode Expansion and the Mode Algebra]] →

*Sources: the user's PHY 513 notes, Ch. 4 §§4.1–4.2 and Ch. 3 §§3.4–3.5 · PHY 513 Lecture 4 (Larsen) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2–§2.3 · Yu Zhao-Huan, 量子场论讲义, §§2.1–2.3 · the user's pre-course notes, §§3.1–3.3.*

How is a field, a system with one coordinate at every point of space, turned into a quantum theory? The answer reuses three things the vault already has: the oscillator solved by its algebra alone ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]]), the passage from Poisson brackets to commutators ([[§B8.1 Poisson Brackets#^rem-b8-1-5|CM Remark: From brackets to commutators]]), and the classical free scalar field ([[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]]). This section recalls the classical field from its home in Chapter C1b (Lagrangian, momentum density, Hamiltonian and field momentum, shown as embedded boxes), states the quantum model those formulas define, and the one postulate of canonical quantization for fields, the equal-time commutation relations. That the free field is already, classically, a set of independent oscillators, one per momentum, opens [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]; quantizing those oscillators is §C2a.2–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]]; the whole recipe is [[P1 Canonical Quantization]].

*Conventions* ([[Larsen PHY 513]]): natural units $\hbar = c = 1$ ([[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-1|Def. §C1a.2.1]]); $g = \operatorname{diag}(+,-,-,-)$, so $p\cdot x = p^0t - \mathbf p\cdot\mathbf x$; $E_{\mathbf p} = +\sqrt{\mathbf p^2 + m^2}$; spatial Fourier transforms $f(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\tilde f(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$, with $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$, an identity of tempered distributions in $\mathbf k$ and not a convergent integral ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; the other rules in [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]). Relativity B keeps $c$ explicit; here it is set to one.

> [!caution] Caution: Eₚ, not ωₚ; π, not Π
> Lectures 4–5 write the mode frequency as $\omega_{\mathbf p}$ and the momentum density as $\Pi(\mathbf x)$ (also Problem Set 3). These notes write $E_{\mathbf p}$ and $\pi(\mathbf x)$ (the operator: $\hat\pi(\mathbf x)$), as Peskin–Schroeder do from their eq. (2.33) on: the frequency of mode $\mathbf p$ *is* the energy of a particle of momentum $\mathbf p$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]]). The user's PHY 513 notes use both, mostly $\omega_{\mathbf p}$ (Concordance: "both $\sqrt{\mathbf p^2 + m^2}$"); Yu writes $E_{\mathbf p}$, the user's pre-course notes $E_{\vec p}$, Quantum Mechanics (C13★, after Sakurai) $E_p$ with $c$ restored. A nonrelativistic oscillator keeps its own $\omega$. **Hats.** As the lectures and the user's notes do (Lecture 10: "with ˆ to stress operators"), these notes put a hat on every quantum operator on the Hilbert (Fock) space: fields and momentum densities $\hat\phi$, $\hat\pi$, $\hat\psi$, $\hat{\bar\psi}$, $\hat A^\mu$, mode operators $\hat a_{\mathbf p}$, $\hat b^{s\dagger}_{\mathbf p}$, the charges $\hat H$, $\hat{\mathbf P}$, $\hat P^\mu$, $\hat Q$, $\hat N$ and generators $\hat J^{\mu\nu}$. Classical fields stay unhatted (Chapter C1b, the classical Dirac field of C5a, every classical box recalled in a quantum section), so the hat marks the step of quantization; c-numbers stay unhatted too: spinors $u^s(p)$, $v^s(p)$, polarization vectors, the matrices $\Lambda$, $S(\Lambda)$, $\gamma^\mu$, the single-particle $H_{\text{s.p.}}$, and the two-point functions $D_W$, $D_F$, $S_F$, which are vacuum expectation values. By convention the unitary operators $U(\Lambda, a)$, $U(R)$ that represent symmetries are unhatted, as are states. The reason for the hats is the dagger: $u^{s\dagger}(p)$ is a row spinor and $\hat a^{s\dagger}_{\mathbf p}$ a creation operator, and no formula has to say which is meant. A lowercase bold letter with a hat is a unit vector, $\hat{\mathbf p} = \mathbf p/|\mathbf p|$; the momentum operator is the capital $\hat{\mathbf P}$. Peskin–Schroeder drop the hats.
>
> *Source: Lectures 4–5 · Problem Set 3 · PS §2.3, p. 22 · Yu §2.3 · the user's PHY 513 notes, Concordance · the user's pre-course notes, §3 · QM §C13.1★ · Lecture 10, slide 10 · the user's PHY 513 notes, Ch. 10*

^cau-c2a-1-1

## The classical scalar field, recalled

The classical theory to be quantized has its home in Chapter C1b; its boxes are shown here as they stand there. The field and its Lagrangian ([[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]] with $\hbar = c = 1$), defined in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]:

![[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6]]

The canonical momentum and the Hamiltonian, the Legendre transform of mechanics ([[§B7.1 The Legendre Transform and Hamilton's Equations#^def-b7-1-2|CM Def. §B7.1.2]]) done at each point, defined in [[§C1b.4 Hamiltonian Field Theory|§C1b.4]]:

![[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1]]

![[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2]]

For the free real field they are $\pi = \dot\phi$ and a sum of squares, derived in §C1b.4:

![[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2]]

The field momentum, the Noether charge of space translations, derived from the energy–momentum tensor in [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum|§C1b.6]] for any set of fields:

![[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6]]

and for this field, with $T^{0i} = \dot\phi\,\partial^i\phi$ worked out from $\mathcal L$:

![[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-6-1]]

The energy and the momentum of this field in field form, $H = P^0$ and $\mathbf P = -\int d^3x\,\pi\nabla\phi$, derived from $T^{0\mu}$ index by index, and the statement that $\mathbf P$ generates spatial translations through the bracket, as $H$ generates time evolution:

![[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7]]

![[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9]]

Quantization keeps these formulas and reads $\phi$, $\pi$, $H$ and $\mathbf P$ as operators, written with a hat: $\hat\phi$, $\hat\pi$, $\hat H$, $\hat{\mathbf P}$. The boxes recalled above are classical and stay unhatted; the hat marks the quantization step ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution: Eₚ, not ωₚ; π, not Π]]). What it adds is stated next: the quantum model (operators, with the ordering of $\hat H$ left open until [[§C2a.3 Energy, Momentum and the Zero-Point Energy|§C2a.3]]), and the postulate that fixes their algebra.

## The quantum model

> [!model] Model §C2a.1.1: The Free Real Scalar Quantum Field
> A Hermitian field $\hat\phi(\mathbf x)$ and momentum density $\hat\pi(\mathbf x)$ satisfying the equal-time relations of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], with Hamiltonian
>
> $$
> \hat H = \int d^3x\,\Bigl[\tfrac12\pi^2 + \tfrac12(\nabla\hat\phi)^2 + \tfrac12m^2\hat\phi^2\Bigr] ,
> $$
>
> and field momentum $\hat{\mathbf P} = -\int d^3x\,\hat\pi\nabla\hat\phi$: the quantization of $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]), for which classically $\pi = \dot\phi$, with the classical charges of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]] and [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]] (recalled above) read as operators. That these operators generate time and space translations of the field is [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]].
>
> *Assumptions:* free (quadratic $\mathcal L$: linear field equation, no interactions); $m > 0$; flat spacetime with an inertial time; infinite space, continuum (delta-function) normalization; the operator ordering in $\hat H$ is fixed in [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]; $\hat{\mathbf P}$ needs no ordering choice ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).
> *Source: the user's PHY 513 notes, Ch. 3 §3.4, Ch. 4 §4.2 and §4.7 · PHY 513 Lecture 4 · PS §2.3, eqs. (2.31)–(2.33) · Yu §2.3, eqs. (2.79), (2.123)–(2.124)*

^mod-c2a-1-1

The classical model is [[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]] with $c = \hbar = 1$; Quantum Mechanics quantized it in a box ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^def-c13-1-1|QM Def. §C13.1.1]]).

## The postulate

> [!remark] Remark: The oscillator, recalled in natural units
> With $\hbar = 1$ ([[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-1|Def. §C1a.2.1]]) the oscillator $\hat H = \frac{\hat p^2}{2m} + \frac12m\omega^2\hat x^2$ is rewritten by $\hat x = (\hat a + \hat a^\dagger)/\sqrt{2m\omega}$, $\hat p = -i\sqrt{m\omega/2}\,(\hat a - \hat a^\dagger)$; then $[\hat x, \hat p] = i \iff [\hat a, \hat a^\dagger] = 1$, $\hat H = \frac\omega2(\hat a\hat a^\dagger + \hat a^\dagger \hat a) = \omega(\hat a^\dagger \hat a + \frac12)$, and $[\hat H, \hat a^\dagger] = \omega \hat a^\dagger$ makes $\hat a^\dagger$ raise the energy by $\omega$ ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], level B [[§B4.1 Ladder Operators and the Spectrum#^thm-b4-1-2|QM Theorem §B4.1.2]]). One check worth keeping: squaring $\hat x$ and $\hat p$ in order, the $\hat a^2$ and $\hat a^{\dagger2}$ terms cancel and the two orderings *add*; a minus sign between them would give the constant $\hat H = \omega/2$. Everything below is this computation once per momentum.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.1 · PHY 513 Lecture 4, Part A · PS §2.3, eqs. (2.23)–(2.24)*

^rem-c2a-1-1

> [!principle] Principle §C2a.1.2: Equal-Time Canonical Commutation Relations
> To quantize a field theory with canonical pairs $(\phi_a(\mathbf x), \pi_a(\mathbf x))$, promote them to operators $\hat\phi_a(\mathbf x)$, $\hat\pi_a(\mathbf x)$ on a Hilbert space with, at equal times,
>
> $$
> [\hat\phi_a(\mathbf x), \hat\pi_b(\mathbf y)] = i\,\delta_{ab}\,\delta^3(\mathbf x - \mathbf y), \qquad [\hat\phi_a(\mathbf x), \hat\phi_b(\mathbf y)] = [\hat\pi_a(\mathbf x), \hat\pi_b(\mathbf y)] = 0 ,
> $$
>
> real fields becoming Hermitian operators, and take as Hamiltonian the classical $H[\phi, \pi]$ read as an operator, $\hat H = H[\hat\phi, \hat\pi]$.
>
> *Domain:* bosonic fields with a Hamiltonian formulation; Schrödinger-picture operators, or Heisenberg-picture operators at a common time. Fermion fields take anticommutators instead ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]). The operator ordering in $\hat H$ is not fixed by this principle ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 (Principle "Canonical commutators for a field") · PHY 513 Lecture 4, Part B · PS §2.3, eq. (2.20) · Yu §2.2, eq. (2.76)*

^pr-c2a-1-2

> [!remark] Remark: Why a delta function, and not a Kronecker delta
> Divide space into cells $V_i$ and let $\Phi_i$ be the cell average of the field. The discrete system has ordinary canonical pairs $(\Phi_i, \Pi_i)$ with $\Pi_i = \partial L/\partial\dot\Phi_i \to V_i\,\pi(\mathbf x)$, because $L = \sum_iV_i\mathcal L_i$. So $[\hat\Phi_i, \hat\pi_j] = i\,\delta_{ij}/V_j$, and $\delta_{ij}/V_j \to \delta^3(\mathbf x - \mathbf y)$ as the cells shrink, which is exactly what turns $\sum_jV_jf_j\,\delta_{ij}/V_j = f_i$ into $\int d^3y\,f(\mathbf y)\,\delta^3(\mathbf x - \mathbf y) = f(\mathbf x)$. Two consequences: operators at different points commute, and $[\hat\phi, \hat\pi]$ has mass dimension 3, since $[\hat\phi] = 1$ and $[\hat\pi] = 2$. The cells are the bead chain of Waves and Optics run backwards ([[§B3.2 The Continuum Limit and the Wave Equation#^def-b3-2-1|WO Def. §B3.2.1]]). The cell average $\Phi_i$ is the field smeared with the indicator of the cell divided by its volume; smooth smearing functions in place of the cells give the operators of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], and "the cells shrink" is the statement that $\hat\phi(\mathbf x)$ is only the kernel of those operators ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]).
>
> *Source: Yu §2.2, eqs. (2.71)–(2.76) · the user's PHY 513 notes, Ch. 4 §4.2 · the user's pre-course notes, §3.2*

^rem-c2a-1-2

> [!definition] Definition §C2a.1.1: Smeared Field Operators
> For real test functions $f, g \in \mathcal S(\mathbb R^3)$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]), the **smeared field** and **smeared momentum density** on a time slice are
>
> $$
> \hat\phi(f) = \int d^3x\,f(\mathbf x)\,\hat\phi(\mathbf x), \qquad \hat\pi(g) = \int d^3x\,g(\mathbf x)\,\hat\pi(\mathbf x) ,
> $$
>
> Hermitian operators. $\hat\phi$ and $\hat\pi$ are operator-valued distributions on space ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]): the symbols $\hat\phi(\mathbf x)$, $\hat\pi(\mathbf x)$ are the kernels through which these operators are written, not operators themselves.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points": "operator-valued distributions, defined after smearing with test functions") and App. A §A.4 ($\hat\phi[\varphi] = \int d^4x\,\varphi(x)\hat\phi(x)$), here on a time slice · standard (Streater & Wightman, Ch. 3)*

^def-c2a-1-1

> [!theorem] Theorem §C2a.1.3: The Canonical Relations Are Identities after Smearing
> For real $f, g \in \mathcal S(\mathbb R^3)$, [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] means
>
> $$
> [\hat\phi(f), \hat\pi(g)] = i\int d^3x\,f(\mathbf x)\,g(\mathbf x), \qquad [\hat\phi(f), \hat\phi(g)] = [\hat\pi(f), \hat\pi(g)] = 0 :
> $$
>
> $i\delta^3(\mathbf x - \mathbf y)$ is the kernel of the bilinear map $(f, g) \mapsto [\hat\phi(f), \hat\pi(g)]$, an identity of distributions on $\mathbb R^6$. Read at one point, $\mathbf x = \mathbf y$, the relation would assign $[\hat\phi(\mathbf x), \hat\pi(\mathbf x)] = i\delta^3(\mathbf 0)$, which has no value: it is not an equation between operators at points.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 and §4.8 (Caution "Two honesty points"), App. A §A.4 · stated here as an identity of distributions (standard: Streater & Wightman, Ch. 3)*

^thm-c2a-1-3

> [!derivation]- Derivation
> **1. Pair the left side with $f \otimes g$.** The commutator is bilinear, so multiplying $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)]$ by $f(\mathbf x)g(\mathbf y)$ and integrating over both points gives, by [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]],
>
> $$
> \int d^3x\,d^3y\;f(\mathbf x)\,g(\mathbf y)\,[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = \bigl[\hat\phi(f), \hat\pi(g)\bigr] .
> $$
>
> This is what the left side *is*: by the kernel theorem ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]) the separately continuous bilinear map $(f, g) \mapsto \langle\Psi_1|[\hat\phi(f), \hat\pi(g)]|\Psi_2\rangle$ has exactly one kernel in $\mathcal S'(\mathbb R^6)$, and "$[\hat\phi(\mathbf x), \hat\pi(\mathbf y)]$" names it. The principle states what that kernel is.
>
> **2. The right side as a distribution on $\mathbb R^6$.** Change variables to $\mathbf u = \mathbf x - \mathbf y$, $\mathbf v = \mathbf y$ (inverse $\mathbf x = \mathbf u + \mathbf v$, $\mathbf y = \mathbf v$; Jacobian $1$; [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]). In the new variables $\delta^3(\mathbf x - \mathbf y)$ is $\delta^3(\mathbf u)$ times the constant $1$ in $\mathbf v$, so for $F(\mathbf x, \mathbf y) = f(\mathbf x)g(\mathbf y)$
>
> $$
> \delta^3(\mathbf x - \mathbf y)[F] = \int d^3v\;F(\mathbf u + \mathbf v, \mathbf v)\Big|_{\mathbf u = \mathbf 0} = \int d^3v\,f(\mathbf v)\,g(\mathbf v) .
> $$
>
> The same number is the limit of $\int d^3x\,d^3y\,\rho_\varepsilon(\mathbf x - \mathbf y)f(\mathbf x)g(\mathbf y)$ for any nascent delta $\rho_\varepsilon$ ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 3): the cells of [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-2|Remark: Why a delta function]] made smooth.
>
> **3. Equate.** Steps 1 and 2 give $[\hat\phi(f), \hat\pi(g)] = i\int d^3x\,f\,g$ times the identity operator. The other two relations have kernel $0$, so $[\hat\phi(f), \hat\phi(g)] = [\hat\pi(f), \hat\pi(g)] = 0$ for all $f$, $g$.
>
> **4. One canonical pair per smearing.** For $f$, $g$ with $\int d^3x\,f\,g = 1$ the operators $\hat Q = \hat\phi(f)$, $\hat P = \hat\pi(g)$ satisfy $[\hat Q, \hat P] = i$, the commutator of one particle on a line ([[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|Remark: The oscillator, recalled]]). For the cells, $f = \chi_{V_i}/V_i$ and $g = \chi_{V_j}$ give $[\hat\Phi_i, \hat\Pi_j] = i\,\delta_{ij}$.
>
> **5. No relation at a point.** Setting $\mathbf y = \mathbf x$ on the right means evaluating $\delta^3$ at its singular point. With a nascent delta $\rho_\varepsilon(\mathbf u) = \varepsilon^{-3}\rho(\mathbf u/\varepsilon)$ the would-be value is $\varepsilon^{-3}\rho(\mathbf 0)$, which diverges as $\varepsilon \to 0^+$ and depends on the shape $\rho$ ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], 3). So no family of operators $\hat\phi(\mathbf x)$, $\hat\pi(\mathbf y)$ labelled by points satisfies the relations as equations between operators. ⚑ By-product: the field at a point is not an observable; what is measured is a field averaged over a region, and the state $\hat\phi(\mathbf x)|0\rangle$ has infinite norm while $\hat\phi(f)|0\rangle$ is a state → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]].
>
> **What the derivation shows**
> - The postulate is a statement about smeared fields; its delta function is the kernel of $(f, g) \mapsto i\int f\,g$.
> - Each pair of smearing functions with $\int f\,g = 1$ is one canonical pair; the shrinking cells of the remark are a crude version of the same thing.
> - Used next: wherever a derivation "integrates $\delta^3(\mathbf x - \mathbf y)$" against mode functions ([[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-6|Derivation §C2a.2.6]], steps 3–4), it is this pairing, with the plane waves made into test functions by smearing in momentum ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]).

^der-c2a-1-3

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]

*Procedure:* [[P1 Canonical Quantization#^p1-4|P1, step 4]]

> [!remark] Remark: A momentum with no time in sight
> The canonical coordinates are the values $\phi(\mathbf x)$ on one time slice, as the coordinate of mechanics is the number $q$, not the trajectory $q(t)$. The classical relation $\pi = \dot\phi$ is used once, in the Legendre transform, to decide which quantity is conjugate to $\phi$; after quantization "conjugate" means "fails to commute with $\hat\phi$ by $i\delta^3$", as $\hat p$ in quantum mechanics is the operator with $[\hat x, \hat p] = i$ and not $m\,dx/dt$ (which vanishes in the Schrödinger picture). Time is carried by the states; $\hat\pi = \partial_t\hat\phi$ returns as a *theorem* of the Heisenberg picture ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]]). The argument of the field in the four formalisms:
>
> | formalism | argument of $\phi$ | role of $t$ |
> | --- | --- | --- |
> | Lagrangian ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations\|§C1b.2]]) | $\phi(x)$, $x = (t, \mathbf x)$ | integrated over in $S = \int d^4x\,\mathcal L$ |
> | Hamiltonian, classical ([[§C1b.4 Hamiltonian Field Theory\|§C1b.4]]) | $\phi(\mathbf x)$, $\pi(\mathbf x)$ on a slice | parameter along the trajectory |
> | Schrödinger picture (§C2a.1–§C2a.6) | $\hat\phi(\mathbf x)$, $\hat\pi(\mathbf x)$ | carried by the states |
> | Heisenberg picture (§C2b.1–§C2b.4) | $\hat\phi(t, \mathbf x)$ | carried by the operators; Klein–Gordon holds |
>
> The label $\mathbf x$ is not an operator: field theory has a field operator at each position, and no position operator.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 (Caution "The lecture's construction") · PS §2.3, p. 20*

^rem-c2a-1-3

> [!remark]- Connections
> - The oscillator algebra that each mode will carry, and the fact that its spectrum follows from $[\hat a, \hat a^\dagger] = 1$ alone, is Quantum Mechanics' — [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], [[§B4.1 Ladder Operators and the Spectrum#^thm-b4-1-4|QM Theorem §B4.1.4]].
> - The equal-time relations are Dirac's rule $\{\,,\} \to [\,,]/i$ applied to the field's Poisson brackets $\{\phi(\mathbf x), \pi(\mathbf y)\} = \delta^3(\mathbf x - \mathbf y)$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]]), the continuum version of the fundamental brackets — [[§B8.1 Poisson Brackets#^thm-b8-1-1|CM Theorem §B8.1.1]], [[§B8.1 Poisson Brackets#^rem-b8-1-5|CM Remark: From brackets to commutators]].
> - In quantum mechanics the canonical commutator is derived from translations ([[§C2.2 Translation and Momentum as Its Generator#^thm-c2-2-6|QM Theorem §C2.2.6]]); for fields it is postulated, and the generator property is recovered afterwards: the mode-form momentum of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]] generates translations of $\hat\phi$, as momentum does in [[§C2.2 Translation and Momentum as Its Generator#^pr-c2-2-4|QM Principle §C2.2.4]].
> - A field is the continuum limit of a chain of coupled masses, and its normal modes are the chain's modes in that limit — [[§B3.2 The Continuum Limit and the Wave Equation#^thm-b3-2-2|WO Theorem §B3.2.2]]; the Klein–Gordon field is the chain with an extra spring tying each mass to its rest position, whose dispersion relation is the plasma relation — [[§B6.2 Dispersion, Phase Velocity and Group Velocity#^thm-b6-2-1|WO Theorem §B6.2.1]].
> - The delta function with zero width and unit area that replaces $\delta_{ij}$ is the one of Waves and Optics, and it cannot be a ket's wave function, which is why field operators are operator-valued distributions ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]) — [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]], [[§37 Position Eigenstates and Continuous Resolutions#^rem-37-2|556 Remark: What the position eigenstate would have to be]], [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]].
> - Quantum Mechanics previewed the quantized Klein–Gordon field in a box, with Sakurai's normalization; Chapters C2a–C2b are its full home — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^def-c13-1-1|QM Def. §C13.1.1]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-6|QM Theorem §C13.1.6]].
> - The Heisenberg picture, where $\hat\pi = \partial_t\hat\phi$ and the Klein–Gordon equation become operator theorems — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]; and the alternative to the canonical route, in which the Lagrangian keeps the central role and Lorentz invariance stays manifest, is the path integral — QFT C11 (planned).
> - Operator-valued distributions are the language of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]: a field is a linear map from test functions to operators, as a generalized function is a linear map from test functions to numbers — [[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]].
> - The kernel theorem is what makes "$[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$" a single, well-defined distribution in both points, determined by the smeared commutators of [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]] — [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]].
> - A linear change of variables turns $\delta^3(\mathbf x - \mathbf y)$ on $\mathbb R^6$ into $\delta^3$ of the difference with the other variable free, which is why it pairs $f\otimes g$ into $\int f\,g$ ([[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-3|Derivation §C2a.1.3]], step 2) — [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]; nascent deltas make the same pairing the limit of the shrinking cells — [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]].
> - The relation has no value at coinciding points for the same reason the zero-point energy contains $\delta^3(\mathbf 0)$: δ evaluated at its singular point — [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].
> - The plane-wave delta of the decoupling computation is an identity in $\mathcal S'$, and the computation itself is Fubini's theorem for wave packets — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]; uniqueness of the transform, used to read off one equation per mode, holds in $\mathcal S'$ — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]; differentiating under the integral needs a dominating function — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]].
> - Principle §C2a.1.1 is preserved by orthogonal rotations among $N$ fields, so diagonalizing a mass matrix gives $N$ independent free fields, each quantized as in Theorem §C2a.1.3 ([[§R1.3 Diagonalization into N Free Klein–Gordon Fields#^thm-r1-3-3|Thesis Thm. §R1.3.3]], [[§R1.3 Diagonalization into N Free Klein–Gordon Fields#^thm-r1-3-4|Thesis Thm. §R1.3.4]]).
