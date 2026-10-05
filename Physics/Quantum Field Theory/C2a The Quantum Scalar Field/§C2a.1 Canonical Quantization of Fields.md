---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2a
section: C2a.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum]] · ↑ [[· C2a The Quantum Scalar Field]] · [[§C2a.2 Mode Expansion and the Mode Algebra]] →

*Sources: the user's PHY 513 notes, Ch. 4 §§4.1–4.2 and Ch. 3 §3.4 · PHY 513 Lecture 4 (Larsen) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.3 · Yu Zhao-Huan, 量子场论讲义, §§2.1–2.2 · the user's pre-course notes, §§3.1–3.2.*

How is a field, a system with one coordinate at every point of space, turned into a quantum theory? The answer reuses three things the vault already has: the oscillator solved by its algebra alone ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]]), the passage from Poisson brackets to commutators ([[§B8.1 Poisson Brackets#^rem-b8-1-5|CM Remark: From brackets to commutators]]), and the classical free scalar field ([[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]]). This section states the one postulate of canonical quantization for fields, the equal-time commutation relations, and shows that the free field is already, classically, a set of independent oscillators, one per momentum. Quantizing those oscillators is [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]]; the whole recipe is [[P1 Canonical Quantization]].

*Conventions* ([[Larsen PHY 513]]): natural units $\hbar = c = 1$ ([[§C1.2 Natural Units and Dimensional Analysis#^def-c1-2-1|Def. §C1.2.1]]); $g = \operatorname{diag}(+,-,-,-)$, so $p\cdot x = p^0t - \mathbf p\cdot\mathbf x$; $E_{\mathbf p} = +\sqrt{\mathbf p^2 + m^2}$; spatial Fourier transforms $f(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\tilde f(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$, with $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$, an identity of tempered distributions in $\mathbf k$ and not a convergent integral ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; the other rules in [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]). Relativity B keeps $c$ explicit; here it is set to one.

> [!caution] Caution: Eₚ, not ωₚ; π, not Π
> Lectures 4–5 write the mode frequency as $\omega_{\mathbf p}$ and the momentum density as $\Pi(\mathbf x)$ (also Problem Set 3). These notes write $E_{\mathbf p}$ and $\pi(\mathbf x)$, as Peskin–Schroeder do from their eq. (2.33) on: the frequency of mode $\mathbf p$ *is* the energy of a particle of momentum $\mathbf p$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]). The user's PHY 513 notes use both, mostly $\omega_{\mathbf p}$ (Concordance: "both $\sqrt{\mathbf p^2 + m^2}$"); Yu writes $E_{\mathbf p}$, the user's pre-course notes $E_{\vec p}$, Quantum Mechanics (C13★, after Sakurai) $E_p$ with $c$ restored. A nonrelativistic oscillator keeps its own $\omega$. The lectures and the user's notes also put hats on operators, $\hat\phi$, $\hat\pi$, $\hat a_{\mathbf p}$; these notes drop them, as Peskin–Schroeder do.
>
> *Source: Lectures 4–5 · Problem Set 3 · PS §2.3, p. 22 · Yu §2.3 · the user's PHY 513 notes, Concordance · the user's pre-course notes, §3 · QM §C13.1★*

^cau-c2a-1-1

## The postulate

> [!remark] Remark: The oscillator, recalled in natural units
> With $\hbar = 1$ ([[§C1.2 Natural Units and Dimensional Analysis#^def-c1-2-1|Def. §C1.2.1]]) the oscillator $H = \frac{p^2}{2m} + \frac12m\omega^2x^2$ is rewritten by $x = (a + a^\dagger)/\sqrt{2m\omega}$, $p = -i\sqrt{m\omega/2}\,(a - a^\dagger)$; then $[x, p] = i \iff [a, a^\dagger] = 1$, $H = \frac\omega2(aa^\dagger + a^\dagger a) = \omega(a^\dagger a + \frac12)$, and $[H, a^\dagger] = \omega a^\dagger$ makes $a^\dagger$ raise the energy by $\omega$ ([[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], level B [[§B4.1 Ladder Operators and the Spectrum#^thm-b4-1-2|QM Theorem §B4.1.2]]). One check worth keeping: squaring $x$ and $p$ in order, the $a^2$ and $a^{\dagger2}$ terms cancel and the two orderings *add*; a minus sign between them would give the constant $H = \omega/2$. Everything below is this computation once per momentum.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.1 · PHY 513 Lecture 4, Part A · PS §2.3, eqs. (2.23)–(2.24)*

^rem-c2a-1-1

The classical Hamiltonian form is [[§C1.10 Hamiltonian Field Theory|§C1.10]] (Hamiltonian field theory: [[§C1.10 Hamiltonian Field Theory#^def-c1-10-1|Def. §C1.10.1]], [[§C1.10 Hamiltonian Field Theory#^thm-c1-10-2|Theorem §C1.10.2]]; the free real field: [[§C1.9 The Action Principle and the Euler–Lagrange Equations#^mod-c1-9-6|Model §C1.9.6]]). The one formula needed: for $\mathcal L(\phi, \partial_\mu\phi)$ the momentum density conjugate to $\phi$ and the Hamiltonian are $\pi(\mathbf x) = \partial\mathcal L/\partial\dot\phi(\mathbf x)$, $H = \int d^3x\,(\pi\dot\phi - \mathcal L)$ with $\dot\phi$ eliminated (the field version of [[§B7.1 The Legendre Transform and Hamilton's Equations#^def-b7-1-2|CM Def. §B7.1.2]]). For the free real field of [[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]], $\mathcal L = \frac12\dot\phi^2 - \frac12(\nabla\phi)^2 - \frac12m^2\phi^2$ gives $\pi = \dot\phi$ and

$$
H = \int d^3x\,\Bigl[\tfrac12\pi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2\Bigr] .
$$

> [!principle] Principle §C2a.1.1: Equal-Time Canonical Commutation Relations
> To quantize a field theory with canonical pairs $(\phi_a(\mathbf x), \pi_a(\mathbf x))$, promote them to operators on a Hilbert space with, at equal times,
>
> $$
> [\phi_a(\mathbf x), \pi_b(\mathbf y)] = i\,\delta_{ab}\,\delta^3(\mathbf x - \mathbf y), \qquad [\phi_a(\mathbf x), \phi_b(\mathbf y)] = [\pi_a(\mathbf x), \pi_b(\mathbf y)] = 0 ,
> $$
>
> real fields becoming Hermitian operators, and take as Hamiltonian the classical $H[\phi, \pi]$ read as an operator.
>
> *Domain:* bosonic fields with a Hamiltonian formulation; Schrödinger-picture operators, or Heisenberg-picture operators at a common time. Fermion fields take anticommutators instead ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-2|Principle §C5b.1.2]]). The operator ordering in $H$ is not fixed by this principle ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 (Principle "Canonical commutators for a field") · PHY 513 Lecture 4, Part B · PS §2.3, eq. (2.20) · Yu §2.2, eq. (2.76)*

^pr-c2a-1-1

> [!remark] Remark: Why a delta function, and not a Kronecker delta
> Divide space into cells $V_i$ and let $\Phi_i$ be the cell average of the field. The discrete system has ordinary canonical pairs $(\Phi_i, \Pi_i)$ with $\Pi_i = \partial L/\partial\dot\Phi_i \to V_i\,\pi(\mathbf x)$, because $L = \sum_iV_i\mathcal L_i$. So $[\Phi_i, \pi_j] = i\,\delta_{ij}/V_j$, and $\delta_{ij}/V_j \to \delta^3(\mathbf x - \mathbf y)$ as the cells shrink, which is exactly what turns $\sum_jV_jf_j\,\delta_{ij}/V_j = f_i$ into $\int d^3y\,f(\mathbf y)\,\delta^3(\mathbf x - \mathbf y) = f(\mathbf x)$. Two consequences: operators at different points commute, and $[\phi, \pi]$ has mass dimension 3, since $[\phi] = 1$ and $[\pi] = 2$. The cells are the bead chain of Waves and Optics run backwards ([[§B3.2 The Continuum Limit and the Wave Equation#^def-b3-2-1|WO Def. §B3.2.1]]). The cell average $\Phi_i$ is the field smeared with the indicator of the cell divided by its volume; smooth smearing functions in place of the cells give the operators of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], and "the cells shrink" is the statement that $\phi(\mathbf x)$ is only the kernel of those operators ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]]).
>
> *Source: Yu §2.2, eqs. (2.71)–(2.76) · the user's PHY 513 notes, Ch. 4 §4.2 · the user's pre-course notes, §3.2*

^rem-c2a-1-2

> [!definition] Definition §C2a.1.1: Smeared Field Operators
> For real test functions $f, g \in \mathcal S(\mathbb R^3)$ ([[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]), the **smeared field** and **smeared momentum density** on a time slice are
>
> $$
> \phi(f) = \int d^3x\,f(\mathbf x)\,\phi(\mathbf x), \qquad \pi(g) = \int d^3x\,g(\mathbf x)\,\pi(\mathbf x) ,
> $$
>
> Hermitian operators. $\phi$ and $\pi$ are operator-valued distributions on space ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]): the symbols $\phi(\mathbf x)$, $\pi(\mathbf x)$ are the kernels through which these operators are written, not operators themselves.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.8 (Caution "Two honesty points": "operator-valued distributions, defined after smearing with test functions") and App. A §A.4 ($\phi[\varphi] = \int d^4x\,\varphi(x)\phi(x)$), here on a time slice · standard (Streater & Wightman, Ch. 3)*

^def-c2a-1-1

> [!theorem] Theorem §C2a.1.2: The Canonical Relations Are Identities after Smearing
> For real $f, g \in \mathcal S(\mathbb R^3)$, [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]] means
>
> $$
> [\phi(f), \pi(g)] = i\int d^3x\,f(\mathbf x)\,g(\mathbf x), \qquad [\phi(f), \phi(g)] = [\pi(f), \pi(g)] = 0 :
> $$
>
> $i\delta^3(\mathbf x - \mathbf y)$ is the kernel of the bilinear map $(f, g) \mapsto [\phi(f), \pi(g)]$, an identity of distributions on $\mathbb R^6$. Read at one point, $\mathbf x = \mathbf y$, the relation would assign $[\phi(\mathbf x), \pi(\mathbf x)] = i\delta^3(\mathbf 0)$, which has no value: it is not an equation between operators at points.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 and §4.8 (Caution "Two honesty points"), App. A §A.4 · stated here as an identity of distributions (standard: Streater & Wightman, Ch. 3)*

^thm-c2a-1-2

> [!derivation]- Derivation
> **1. Pair the left side with $f \otimes g$.** The commutator is bilinear, so multiplying $[\phi(\mathbf x), \pi(\mathbf y)]$ by $f(\mathbf x)g(\mathbf y)$ and integrating over both points gives, by [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]],
>
> $$
> \int d^3x\,d^3y\;f(\mathbf x)\,g(\mathbf y)\,[\phi(\mathbf x), \pi(\mathbf y)] = \bigl[\phi(f), \pi(g)\bigr] .
> $$
>
> This is what the left side *is*: by the kernel theorem ([[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]]) the separately continuous bilinear map $(f, g) \mapsto \langle\Psi_1|[\phi(f), \pi(g)]|\Psi_2\rangle$ has exactly one kernel in $\mathcal S'(\mathbb R^6)$, and "$[\phi(\mathbf x), \pi(\mathbf y)]$" names it. The principle states what that kernel is.
>
> **2. The right side as a distribution on $\mathbb R^6$.** Change variables to $\mathbf u = \mathbf x - \mathbf y$, $\mathbf v = \mathbf y$ (inverse $\mathbf x = \mathbf u + \mathbf v$, $\mathbf y = \mathbf v$; Jacobian $1$; [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]). In the new variables $\delta^3(\mathbf x - \mathbf y)$ is $\delta^3(\mathbf u)$ times the constant $1$ in $\mathbf v$, so for $F(\mathbf x, \mathbf y) = f(\mathbf x)g(\mathbf y)$
>
> $$
> \delta^3(\mathbf x - \mathbf y)[F] = \int d^3v\;F(\mathbf u + \mathbf v, \mathbf v)\Big|_{\mathbf u = \mathbf 0} = \int d^3v\,f(\mathbf v)\,g(\mathbf v) .
> $$
>
> The same number is the limit of $\int d^3x\,d^3y\,\rho_\varepsilon(\mathbf x - \mathbf y)f(\mathbf x)g(\mathbf y)$ for any nascent delta $\rho_\varepsilon$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 3): the cells of [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-2|Remark: Why a delta function]] made smooth.
>
> **3. Equate.** Steps 1 and 2 give $[\phi(f), \pi(g)] = i\int d^3x\,f\,g$ times the identity operator. The other two relations have kernel $0$, so $[\phi(f), \phi(g)] = [\pi(f), \pi(g)] = 0$ for all $f$, $g$.
>
> **4. One canonical pair per smearing.** For $f$, $g$ with $\int d^3x\,f\,g = 1$ the operators $Q = \phi(f)$, $P = \pi(g)$ satisfy $[Q, P] = i$, the commutator of one particle on a line ([[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-1|Remark: The oscillator, recalled]]). For the cells, $f = \chi_{V_i}/V_i$ and $g = \chi_{V_j}$ give $[\Phi_i, \Pi_j] = i\,\delta_{ij}$.
>
> **5. No relation at a point.** Setting $\mathbf y = \mathbf x$ on the right means evaluating $\delta^3$ at its singular point. With a nascent delta $\rho_\varepsilon(\mathbf u) = \varepsilon^{-3}\rho(\mathbf u/\varepsilon)$ the would-be value is $\varepsilon^{-3}\rho(\mathbf 0)$, which diverges as $\varepsilon \to 0^+$ and depends on the shape $\rho$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3). So no family of operators $\phi(\mathbf x)$, $\pi(\mathbf y)$ labelled by points satisfies the relations as equations between operators. ⚑ By-product: the field at a point is not an observable; what is measured is a field averaged over a region, and the state $\phi(\mathbf x)|0\rangle$ has infinite norm while $\phi(f)|0\rangle$ is a state → [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-8|Theorem §C2a.4.8]].
>
> **What the derivation shows**
> - The postulate is a statement about smeared fields; its delta function is the kernel of $(f, g) \mapsto i\int f\,g$.
> - Each pair of smearing functions with $\int f\,g = 1$ is one canonical pair; the shrinking cells of the remark are a crude version of the same thing.
> - Used next: wherever a derivation "integrates $\delta^3(\mathbf x - \mathbf y)$" against mode functions ([[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-6|Derivation §C2a.2.6]], steps 3–4), it is this pairing, with the plane waves made into test functions by smearing in momentum ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-7|Theorem §C2a.2.7]]).

^der-c2a-1-2

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]], [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]

*Procedure:* [[P1 Canonical Quantization#^p1-2|P1, step 2]]

> [!remark] Remark: A momentum with no time in sight
> The canonical coordinates are the values $\phi(\mathbf x)$ on one time slice, as the coordinate of mechanics is the number $q$, not the trajectory $q(t)$. The classical relation $\pi = \dot\phi$ is used once, in the Legendre transform, to decide which quantity is conjugate to $\phi$; after quantization "conjugate" means "fails to commute with $\phi$ by $i\delta^3$", as $p$ in quantum mechanics is the operator with $[x, p] = i$ and not $m\,dx/dt$ (which vanishes in the Schrödinger picture). Time is carried by the states; $\pi = \partial_t\phi$ returns as a *theorem* of the Heisenberg picture ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]). The argument of the field in the four formalisms:
>
> | formalism | argument of $\phi$ | role of $t$ |
> | --- | --- | --- |
> | Lagrangian ([[§C1.9 The Action Principle and the Euler–Lagrange Equations\|§C1.9]]) | $\phi(x)$, $x = (t, \mathbf x)$ | integrated over in $S = \int d^4x\,\mathcal L$ |
> | Hamiltonian, classical ([[§C1.10 Hamiltonian Field Theory\|§C1.10]]) | $\phi(\mathbf x)$, $\pi(\mathbf x)$ on a slice | parameter along the trajectory |
> | Schrödinger picture (§C2a.1–§C2a.6) | $\phi(\mathbf x)$, $\pi(\mathbf x)$ | carried by the states |
> | Heisenberg picture (§C2b.1–§C2b.4) | $\phi(t, \mathbf x)$ | carried by the operators; Klein–Gordon holds |
>
> The label $\mathbf x$ is not an operator: field theory has a field operator at each position, and no position operator.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 (Caution "The lecture's construction") · PS §2.3, p. 20*

^rem-c2a-1-3

## The free field as oscillators

> [!theorem] Theorem §C2a.1.3: The Free Field Is a Set of Independent Oscillators
> Expand the classical free real field and its momentum density at a fixed time, $\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\tilde\phi(\mathbf p)\,e^{i\mathbf p\cdot\mathbf x}$ and likewise $\pi$, with $\tilde\phi(-\mathbf p) = \tilde\phi^*(\mathbf p)$, $\tilde\pi(-\mathbf p) = \tilde\pi^*(\mathbf p)$. Then
>
> $$
> H = \int\frac{d^3p}{(2\pi)^3}\;\frac12\Bigl[\,|\tilde\pi(\mathbf p)|^2 + E_{\mathbf p}^2\,|\tilde\phi(\mathbf p)|^2\Bigr], \qquad \ddot{\tilde\phi}(\mathbf p, t) + E_{\mathbf p}^2\,\tilde\phi(\mathbf p, t) = 0 ,
> $$
>
> a sum of independent oscillators of unit mass and frequency $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, one for each $\mathbf p$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 (Derivation "The decoupling is classical") · PS §2.3, eqs. (2.21)–(2.22) · PHY 513 Lecture 4, Part B ("modes decouple")*

^thm-c2a-1-3

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
> **4. Reality.** $\pi$ is real, so $\tilde\pi(-\mathbf p) = \tilde\pi^{\ast}(\mathbf p)$ and the integrand is $|\tilde\pi(\mathbf p)|^2$. ⚑ By-product: the $\mathbf x$ integral pairs each mode $\mathbf p$ with $-\mathbf p$ only (translation invariance), and reality makes the pair one oscillator's worth of variables → [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-4|Remark: Why the modes decouple]].
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
> **7. Add.** $\mathbf p^2 + m^2 = E_{\mathbf p}^2$ gives the Hamiltonian of the statement. ⚑ By-product: the frequency is fixed by the gradient term ($\mathbf p^2$) and the mass term ($m^2$) together; it is the mass-shell energy → [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-4|Remark: Why the frequency is the energy]].
>
> **8. The equation of motion.** Insert the expansion into $\ddot\phi - \nabla^2\phi + m^2\phi = 0$ ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-4|REL Theorem §B4.1.4]]): $\nabla^2e^{i\mathbf p\cdot\mathbf x} = -\mathbf p^2e^{i\mathbf p\cdot\mathbf x}$, so $\int\frac{d^3p}{(2\pi)^3}\bigl(\ddot{\tilde\phi} + (\mathbf p^2 + m^2)\tilde\phi\bigr)e^{i\mathbf p\cdot\mathbf x} = 0$, and uniqueness of the Fourier transform ([[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]]; in $\mathcal S'$, where the transform is a bijection, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2) gives $\ddot{\tilde\phi} + E_{\mathbf p}^2\tilde\phi = 0$ for each $\mathbf p$. Equivalently, Hamilton's equations for the mode Hamiltonian are $\dot{\tilde\phi} = \tilde\pi$, $\dot{\tilde\pi} = -E_{\mathbf p}^2\tilde\phi$. ⚑ By-product: the field must have a Fourier transform at each time (decay at infinity); plane-wave modes are idealizations → [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]].
>
> **What the derivation shows**
> - The free field decouples into independent oscillators already classically; quantization will only add the ordering of operators, i.e. the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]).
> - The frequency of mode $\mathbf p$ is $E_{\mathbf p}$: the mass shell enters through the gradient and mass terms.
> - Used next: the mode expansion ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]]) and the Hamiltonian in mode form ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]]).

^der-c2a-1-3

*Uses:* [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-4|REL Theorem §B4.1.4]], [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-1|WO Theorem §B4.4.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]

*Procedure:* [[P1 Canonical Quantization#^p1-3|P1, step 3]] (classical preparation)

> [!remark] Remark: Why the modes decouple, and why the frequency is the energy
> - **Decoupling is translation invariance.** The $d^3x$ integral of a product of two fields forces opposite momenta, so $\mathbf p$ meets only $-\mathbf p$, which is the same mode after $\mathbf p \to -\mathbf p$. In position space the gradient term couples each point to its neighbours, which is what stopped $H$ from reading as an oscillator; in momentum space it is just part of the frequency. This is the normal-coordinate decoupling of coupled oscillators ([[§B2.2 Normal-Mode Solutions and Energy Exchange#^thm-b2-2-1|WO Theorem §B2.2.1]]), with plane waves as normal modes because the system is translation invariant.
> - **The frequency is not bookkeeping.** $E_{\mathbf p}^2 = \mathbf p^2 + m^2$ comes from the gradient term ($\mathbf p^2$) and the mass term ($m^2$): a wave equation with a restoring term, $\omega^2 = \omega_p^2 + c^2k^2$ ([[§B6.2 Dispersion, Phase Velocity and Group Velocity#^thm-b6-2-1|WO Theorem §B6.2.1]], 2), with the plasma frequency replaced by $m$ ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]]). It is the mass-shell relation, and it is why the quanta will be relativistic particles.
> - **Counting.** $\tilde\phi(\mathbf p)$ is complex but $\tilde\phi(-\mathbf p) = \tilde\phi^{\ast}(\mathbf p)$, so each pair $\{\mathbf p, -\mathbf p\}$ carries two real oscillators: one per $\mathbf p$. Quantum Mechanics' box version quantizes each pair as a two-dimensional isotropic oscillator ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^def-c13-1-1|QM Def. §C13.1.1]]); the mode expansion of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] does the same bookkeeping with $a_{\mathbf p}$ and $a^\dagger_{-\mathbf p}$.
>
> *Source: the user's PHY 513 notes, Ch. 4 §4.2 and §4.6 (Caution "Why the decoupling had to happen")*

^rem-c2a-1-4

Quantization is now "a formality" (the user's notes): quantize each oscillator, $\tilde\phi(\mathbf p) \sim (a + a^\dagger)/\sqrt{2E_{\mathbf p}}$, $\tilde\pi(\mathbf p) \sim -i\sqrt{E_{\mathbf p}/2}\,(a - a^\dagger)$ (Lecture 4's sketch). [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] make this precise, and the one thing the quantum computation adds is the operator ordering, hence the zero-point energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|Remark: Why the zero-point energy is dropped]]). The steps are [[P1 Canonical Quantization#^p1-1|P1, steps 1–2]].

> [!remark]- Connections
> - The oscillator algebra that each mode will carry, and the fact that its spectrum follows from $[a, a^\dagger] = 1$ alone, is Quantum Mechanics' — [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-1|QM Theorem §C3.4.1]], [[§B4.1 Ladder Operators and the Spectrum#^thm-b4-1-4|QM Theorem §B4.1.4]].
> - The equal-time relations are Dirac's rule $\{\,,\} \to [\,,]/i$ applied to the field's Poisson brackets $\{\phi(\mathbf x), \pi(\mathbf y)\} = \delta^3(\mathbf x - \mathbf y)$ ([[§C1.10 Hamiltonian Field Theory#^thm-c1-10-5|Theorem §C1.10.5]]), the continuum version of the fundamental brackets — [[§B8.1 Poisson Brackets#^thm-b8-1-1|CM Theorem §B8.1.1]], [[§B8.1 Poisson Brackets#^rem-b8-1-5|CM Remark: From brackets to commutators]].
> - In quantum mechanics the canonical commutator is derived from translations ([[§C2.2 Translation and Momentum as Its Generator#^thm-c2-2-6|QM Theorem §C2.2.6]]); for fields it is postulated, and the generator property is recovered afterwards: the mode-form momentum of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]] generates translations of $\phi$, as momentum does in [[§C2.2 Translation and Momentum as Its Generator#^pr-c2-2-4|QM Principle §C2.2.4]].
> - A field is the continuum limit of a chain of coupled masses, and its normal modes are the chain's modes in that limit — [[§B3.2 The Continuum Limit and the Wave Equation#^thm-b3-2-2|WO Theorem §B3.2.2]]; the Klein–Gordon field is the chain with an extra spring tying each mass to its rest position, whose dispersion relation is the plasma relation — [[§B6.2 Dispersion, Phase Velocity and Group Velocity#^thm-b6-2-1|WO Theorem §B6.2.1]].
> - The delta function with zero width and unit area that replaces $\delta_{ij}$ is the one of Waves and Optics, and it cannot be a ket's wave function, which is why field operators are operator-valued distributions ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]) — [[§B4.4 Fourier Transforms and the Delta Function#^def-b4-4-2|WO Def. §B4.4.2]], [[§32 Position Eigenstates and Continuous Resolutions#^rem-32-2|556 Remark: What the position eigenstate would have to be]], [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|Caution: Plane-wave states are not normalizable]].
> - Quantum Mechanics previewed the quantized Klein–Gordon field in a box, with Sakurai's normalization; Chapters C2a–C2b are its full home — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^def-c13-1-1|QM Def. §C13.1.1]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-6|QM Theorem §C13.1.6]].
> - The Heisenberg picture, where $\pi = \partial_t\phi$ and the Klein–Gordon equation become operator theorems — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]; and the alternative to the canonical route, in which the Lagrangian keeps the central role and Lorentz invariance stays manifest, is the path integral — QFT C11 (planned).
> - Operator-valued distributions are the language of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]: a field is a linear map from test functions to operators, as a generalized function is a linear map from test functions to numbers — [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]].
> - The kernel theorem is what makes "$[\phi(\mathbf x), \pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$" a single, well-defined distribution in both points, determined by the smeared commutators of [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]] — [[§CA.2 Generalized Functions#^thm-ca-2-16|Theorem §CA.2.16]].
> - A linear change of variables turns $\delta^3(\mathbf x - \mathbf y)$ on $\mathbb R^6$ into $\delta^3$ of the difference with the other variable free, which is why it pairs $f\otimes g$ into $\int f\,g$ ([[§C2a.1 Canonical Quantization of Fields#^der-c2a-1-2|Derivation §C2a.1.2]], step 2) — [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]; nascent deltas make the same pairing the limit of the shrinking cells — [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]].
> - The relation has no value at coinciding points for the same reason the zero-point energy contains $\delta^3(\mathbf 0)$: δ evaluated at its singular point — [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]].
> - The plane-wave delta of the decoupling computation is an identity in $\mathcal S'$, and the computation itself is Fubini's theorem for wave packets — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]; uniqueness of the transform, used to read off one equation per mode, holds in $\mathcal S'$ — [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]; differentiating under the integral needs a dominating function — [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]].
