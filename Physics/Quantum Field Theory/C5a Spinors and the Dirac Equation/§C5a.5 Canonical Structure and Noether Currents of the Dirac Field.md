---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5a
section: C5a.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5a.4 Bilinears, Chirality and the Weyl Equations]] · ↑ [[· C5a Spinors and the Dirac Equation]] · [[§C5a.6 Plane-Wave Solutions]] →

*Sources: the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The Dirac energy–momentum tensor is conserved, and the momentum operator", eq. (diracP)), Ch. 9 §9.4 and §9.6 (the current $\bar\psi\gamma^\mu\psi$), Ch. 3 §3.4 ("Other fields"), §3.5 (table of canonical tensors; Derivation "Belinfante: symmetrizing T with the spin current") · PHY 513 Lecture 10 (Larsen), slide 16 (the Hamiltonian density) · PHY 513, Problem Set 5, Problem 4 (as the user wrote it) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.4, pp. 50–51, eqs. (3.73)–(3.76), §3.5, p. 52, eqs. (3.84)–(3.85), p. 58, eq. (3.105) · Yu Zhao-Huan, 量子场论讲义, §1.7.3, eqs. (1.241)–(1.248), §5.3, eq. (5.94), §5.4.3, eqs. (5.219)–(5.222) · the user's pre-course notes, §5.3.*

What do Hamiltonian field theory and Noether's theorem give for the Dirac field? The Lagrangian and its field equations are [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]] ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]), the single-particle Hamiltonian is [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-4|Def. §C5a.3.4]], the bilinears and $\gamma^5$ are [[§C5a.4 Bilinears, Chirality and the Weyl Equations|§C5a.4]]; the general machinery is [[§C1b.4 Hamiltonian Field Theory|§C1b.4]] (momenta, Legendre transform, brackets) and [[§C1b.5 Noether's Theorem|§C1b.5]]–[[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.7]] ([[P3 Noether's Procedure]]). This section runs that machinery on the Dirac field in the order used for the scalar: the canonical momentum and the Hamiltonian density, the vector and axial currents, the canonical energy–momentum tensor, energy and momentum in field form with the bracket by which $\mathbf P$ generates translations, and the spin current with the symmetric tensor. The quantized field ([[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]) shows these boxes as embeds.

*Conventions* as in [[§C5a.3 The Dirac Equation and Its Lagrangian|§C5a.3]]; $\psi$ a classical field with commuting components; $\varepsilon^{0123} = +1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]); $a\overleftrightarrow{\partial}b \equiv a\,\partial b - (\partial a)\,b$.

## The canonical momentum and the Hamiltonian density

> [!theorem] Theorem §C5a.5.1: Canonical Momenta of the Dirac Field
> For [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]], with $\psi$ and $\bar\psi$ as the independent fields, the canonical momenta ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]) are
>
> $$
> \pi_\psi \equiv \frac{\partial\mathcal L}{\partial(\partial_0\psi)} = i\bar\psi\gamma^0 = i\psi^\dagger, \qquad \pi_{\bar\psi} \equiv \frac{\partial\mathcal L}{\partial(\partial_0\bar\psi)} = 0 .
> $$
>
> The momentum is not a function of the velocity $\dot\psi$: the Legendre map is not invertible, and $\psi$ and $\psi^\dagger$ are themselves canonically conjugate.
>
> *Source: PS §3.5, p. 52, above eq. (3.84) · the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The Dirac energy–momentum tensor …": "the canonical momentum $\pi = \partial\mathcal L/\partial(\partial_t\psi) = i\psi^\dagger$"), Ch. 3 §3.4 ("Other fields")*

^thm-c5a-5-1

> [!derivation]- Derivation
> **1. The time-derivative part of $\mathcal L$.** Split the contraction: $\bar\psi i\gamma^\nu\partial_\nu\psi = \bar\psi i\gamma^0\partial_0\psi + \bar\psi i\gamma^j\partial_j\psi$; only the first term contains $\partial_0\psi$.
>
> **2. Differentiate.** Component by component, $\partial(\bar\psi_a i(\gamma^0)_{ab}\partial_0\psi_b)/\partial(\partial_0\psi_c) = i\bar\psi_a(\gamma^0)_{ac} = i(\bar\psi\gamma^0)_c$. With $\bar\psi\gamma^0 = \psi^\dagger(\gamma^0)^2 = \psi^\dagger$: $\pi_\psi = i\psi^\dagger$ (a row, one entry per component $\psi_c$).
>
> **3. $\bar\psi$.** $\mathcal L$ contains no derivative of $\bar\psi$: $\pi_{\bar\psi} = 0$.
>
> **What the derivation shows**
> - The momentum conjugate to $\psi$ is (essentially) $\psi^\dagger$: the complex scalar's crossover $\pi_\phi = \dot\phi^*$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]) taken one step further, because $\mathcal L$ is first order in time ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]]). Phase space is spanned by the values of $\psi$ alone; half as many data as for a second-order equation.
> - ⚑ By-product: the momenta depend on the choice among Lagrangians differing by a divergence: $\mathcal L_{\rm sym}$ of Theorem §C5a.3.7 gives $\pi_\psi = \frac i2\psi^\dagger$, $\pi_{\psi^\dagger} = -\frac i2\psi$. The equal-time brackets built from either agree once the constraint is taken into account; the course uses $\pi_\psi = i\psi^\dagger$ → [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-5|★ Theorem §C5b.1.5]]; what quantization needs from the momenta: [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]].
> - Used next: the equal-time anticommutator $\{\hat\psi_a(\mathbf x), \hat\pi_{\psi,b}(\mathbf y)\} = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, i.e. $\{\hat\psi_a, \hat\psi_b^\dagger\} = \delta_{ab}\delta^3$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).

^der-c5a-5-1

*Uses:* [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]

*Procedure:* [[P1 Canonical Quantization#^p1-1|P1, step 1]]

> [!theorem] Theorem §C5a.5.2: The Hamiltonian Density of the Dirac Field
> With $\pi_\psi = i\psi^\dagger$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]]), the Hamiltonian density ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]]) of [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] is
>
> $$
> \mathcal H \equiv \pi_\psi\,\dot\psi - \mathcal L = \bar\psi\bigl(-i\gamma^j\partial_j + m\bigr)\psi = \psi^\dagger\bigl(-i\boldsymbol\alpha\cdot\nabla + \beta m\bigr)\psi, \qquad \alpha^j = \gamma^0\gamma^j,\ \beta = \gamma^0 ,
> $$
>
> with $\boldsymbol\alpha$, $\beta$ Hermitian. On solutions of the Dirac equation $\mathcal H = i\psi^\dagger\partial_t\psi$. The bracket $H_{\text{s.p.}} = -i\boldsymbol\alpha\cdot\nabla + \beta m$ is the single-particle Hamiltonian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-4|Def. §C5a.3.4]]; names across sources: [[§C5a.3 The Dirac Equation and Its Lagrangian#^cau-c5a-3-2|§C5a.3, Caution: Names for the single-particle Hamiltonian]]), the one-particle Dirac Hamiltonian of [[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]], whose plane-wave eigenvalues are $\pm E_{\mathbf p}$: classically $\mathcal H$ is not bounded below.
>
> *Source: PS §3.5, eqs. (3.84)–(3.85) · the user's pre-course notes, §5.3 (note "First-order form: $\alpha$, $\beta$, and the positive density") · the user's PHY 513 notes, Ch. 3 §3.5 (table of canonical tensors; $T^{00} = i\psi^\dagger\partial_t\psi$)*

^thm-c5a-5-2

> [!derivation]- Derivation
> **1. Legendre transform.** By [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]] summed over both fields, $\mathcal H = \pi_\psi\dot\psi + \pi_{\bar\psi}\dot{\bar\psi} - \mathcal L = i\psi^\dagger\partial_0\psi + 0 - \mathcal L$ (Theorem §C5a.5.1).
>
> **2. Expand $\mathcal L$ into time and space parts.** $\mathcal L = i\bar\psi\gamma^0\partial_0\psi + i\bar\psi\gamma^j\partial_j\psi - m\bar\psi\psi$, and $i\bar\psi\gamma^0\partial_0\psi = i\psi^\dagger(\gamma^0)^2\partial_0\psi = i\psi^\dagger\partial_0\psi$.
>
> **3. Subtract.** The two $i\psi^\dagger\partial_0\psi$ cancel: $\mathcal H = -i\bar\psi\gamma^j\partial_j\psi + m\bar\psi\psi = \bar\psi(-i\gamma^j\partial_j + m)\psi$. (No equation of motion was used: the time derivatives cancel identically, as they must for a first-order Lagrangian.)
>
> **4. Write with $\psi^\dagger$.** $\bar\psi = \psi^\dagger\gamma^0$: $\mathcal H = \psi^\dagger(-i\gamma^0\gamma^j\partial_j + m\gamma^0)\psi$, with $\partial_j = \partial/\partial x^j$ the components of $\nabla$: $\psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$.
>
> **5. Hermiticity of $\alpha$, $\beta$.** $\beta^\dagger = \gamma^{0\dagger} = \gamma^0$. $(\gamma^0\gamma^j)^\dagger = \gamma^{j\dagger}\gamma^0 = (-\gamma^j)\gamma^0 = \gamma^0\gamma^j$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]]; distinct $\gamma$'s anticommute).
>
> **6. On shell.** Multiply the Dirac equation by $\gamma^0$: $i\partial_0\psi = (-i\gamma^0\gamma^j\partial_j + m\gamma^0)\psi = H_{\text{s.p.}}\psi$. Hence $\mathcal H = \psi^\dagger H_{\text{s.p.}}\psi = i\psi^\dagger\partial_t\psi$.
>
> **7. The spectrum of $H_{\text{s.p.}}$.** For $\psi \propto e^{i\mathbf p\cdot\mathbf x}$, $H_{\text{s.p.}} \to \boldsymbol\alpha\cdot\mathbf p + \beta m$; its square is $\mathbf p^2 + m^2$ because $\{\alpha^i, \alpha^j\} = 2\delta^{ij}$, $\{\alpha^i, \beta\} = 0$, $\beta^2 = 1$ (from the Clifford algebra: $\{\gamma^0\gamma^i, \gamma^0\gamma^j\} = -\gamma^i\gamma^j - \gamma^j\gamma^i = 2\delta^{ij}$; $\gamma^0\gamma^i\gamma^0 + \gamma^0\gamma^0\gamma^i = -\gamma^i + \gamma^i = 0$). So its eigenvalues are $\pm E_{\mathbf p}$, each twice, because $H_{\text{s.p.}}(\mathbf p)$ is traceless ($\alpha^j = \gamma^0\gamma^j$ and $\beta = \gamma^0$ are products of distinct $\gamma$'s, [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]], part 2); the same count from the plane-wave spinors is [[§C5a.6 Plane-Wave Solutions#^thm-c5a-6-2|Theorem §C5a.6.2]]. ⚑ By-product: a negative-frequency solution has negative classical energy $\int\psi^\dagger H_{\text{s.p.}}\psi < 0$; no ordering of commuting fields cures this ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]]), and the cure is anticommutation ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]).
>
> **What the derivation shows**
> - The first-order (Hamiltonian) form $i\partial_t\psi = H_{\text{s.p.}}\psi$ is the Dirac equation multiplied by $\gamma^0$: Dirac's original equation, with the algebra of $\boldsymbol\alpha$, $\beta$ derived from the Clifford algebra rather than postulated.
> - ⚑ By-product: $\mathcal L = 0$ on shell, so $\mathcal H = \pi\dot\psi$ there; the same fact simplifies the energy–momentum tensor ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-5|Theorem §C5a.5.5]]).
> - Used next: $H = \int d^3x\,\mathcal H$ in mode form ([[§C5b.3 Energy, Momentum and the Zero-Point Energy|§C5b.3]]); $\mathcal H = T^{00}$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-6|Theorem §C5a.5.6]]).

^der-c5a-5-2

*Uses:* [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-4|Theorem §C5a.2.4]]

*Procedure:* [[P1 Canonical Quantization#^p1-2|P1, step 2]]

This is Quantum Mechanics' $H = c\boldsymbol\alpha\cdot\mathbf p + \beta mc^2$ ([[§C13.2★ The Dirac Equation#^pr-c13-2-1|QM Principle §C13.2.1]]) as a density sandwiched between fields: there it is a postulated one-particle Hamiltonian acting on a wave function, here a derived density of a classical field whose integral becomes, after quantization, the Hamiltonian of the many-particle theory (rule 2: the layer changes from principle to theorem; the meaning of $\psi$ changes from amplitude to field).

## Currents

> [!theorem] Theorem §C5a.5.3: The Vector Current
> The global phase rotation $\psi \to e^{i\alpha}\psi$, $\bar\psi \to e^{-i\alpha}\bar\psi$ leaves the Dirac Lagrangian ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]) invariant ($\mathcal J = 0$, [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]]). Its Noether current ([[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]) is $j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$; with the conventional sign,
>
> $$
> j^\mu \equiv \bar\psi\gamma^\mu\psi, \qquad \partial_\mu j^\mu = 0 \ \ \text{on solutions}, \qquad Q = \int d^3x\,j^0 = \int d^3x\,\psi^\dagger\psi \ge 0 .
> $$
>
> $j^\mu$ is a real four-vector field, for every $m$. The sign convention is that of the complex scalar ([[§C1b.5 Noether's Theorem#^cau-c1b-5-3|§C1b.5, Caution: Sign and normalization of the U(1) current]]).
>
> *Source: PS §3.4, eqs. (3.73)–(3.74) and p. 51 (Noether currents of $\psi \to e^{i\alpha}\psi$) · the user's PHY 513 notes, Ch. 9 §9.4 ("it is the time component of the current $\bar\psi\gamma^\mu\psi$"), Ch. 9 §9.6 (paragraph "What the Gordon identity says") · Yu §5.3, eq. (5.94)*

^thm-c5a-5-3

> [!derivation]- Derivation
> The steps of [[P3 Noether's Procedure]]; two independent fields $\psi$, $\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], step 1).
>
> **1. Generators.** $\psi' = e^{i\alpha}\psi$, $\bar\psi' = (e^{i\alpha}\psi)^\dagger\gamma^0 = e^{-i\alpha}\bar\psi$ ($\alpha$ real). To first order $\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]]).
>
> **2. Substitute.** $\alpha$ is constant, so $\partial_\mu(e^{i\alpha}\psi) = e^{i\alpha}\partial_\mu\psi$ and $\mathcal L' = e^{-i\alpha}e^{i\alpha}\bar\psi(i\slashed{\partial} - m)\psi = \mathcal L$, exactly: every term has one $\bar\psi$ and one $\psi$.
>
> **3. Test.** $\delta\mathcal L = 0$: $\mathcal J^\mu = 0$.
>
> **4. Current.** $\partial\mathcal L/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu$, $\partial\mathcal L/\partial(\partial_\mu\bar\psi) = 0$ (Derivation §C5a.3.6, step 3). [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]: $j^\mu_{\rm N} = i\bar\psi\gamma^\mu(i\psi) + 0\cdot(-i\bar\psi) = -\bar\psi\gamma^\mu\psi$. Any constant multiple of a conserved current is conserved; the convention is $j^\mu = -j^\mu_{\rm N}$.
>
> **5. Check, directly.** Product rule: $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi$. The conjugate Dirac equation $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$ gives $(\partial_\mu\bar\psi)\gamma^\mu = im\bar\psi$; the Dirac equation $i\gamma^\mu\partial_\mu\psi = m\psi$ gives $\gamma^\mu\partial_\mu\psi = -im\psi$. So $\partial_\mu j^\mu = im\bar\psi\psi - im\bar\psi\psi = 0$. Both equations are used, one per field.
>
> **6. Charge.** $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger(\gamma^0)^2\psi = \psi^\dagger\psi = \sum_a\lvert\psi_a\rvert^2 \ge 0$. $Q$ is constant for fields falling off faster than $1/r^2$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]]). Reality: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]]; vector law: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]].
>
> **What the derivation shows**
> - ⚑ By-product: the classical charge is positive definite, unlike the scalar's ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]); it is Quantum Mechanics' probability density. After quantization with anticommutators, normal-ordered, it becomes particles minus antiparticles and can have either sign ([[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]]).
> - ⚑ By-product: the sign of the Noether current is opposite to the conventional one, as for the complex scalar ([[§C1b.5 Noether's Theorem#^cau-c1b-5-3|§C1b.5, Caution: Sign and normalization of the U(1) current]]).
> - Used next: coupled to the photon, $e\,j^\mu A_\mu$ (QFT C8, planned); its matrix elements are split by the Gordon identity ([[§C5a.8 Gamma-Matrix Technology#^thm-c5a-8-9|Theorem §C5a.8.9]]).

^der-c5a-5-3

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-3|Theorem §C5a.4.3]]

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, steps 1–6]], [[P1 Canonical Quantization#^p1-3|P1, step 3]]

> [!theorem] Theorem §C5a.5.4: The Axial Current
> For every solution of the Dirac equation ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-1|Def. §C5a.3.1]]), with $\gamma^5$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-7|Def. §C5a.2.7]],
>
> $$
> j^{\mu5} \equiv \bar\psi\gamma^\mu\gamma^5\psi, \qquad \partial_\mu j^{\mu5} = 2im\,\bar\psi\gamma^5\psi .
> $$
>
> It is conserved if and only if $m = 0$ (for generic solutions); then the **chiral transformation** $\psi \to e^{i\alpha\gamma^5}\psi$ is a symmetry, and the chiral currents $j^\mu_L = \bar\psi\gamma^\mu P_L\psi = \psi_L^\dagger\bar\sigma^\mu\psi_L$ and $j^\mu_R = \bar\psi\gamma^\mu P_R\psi = \psi_R^\dagger\sigma^\mu\psi_R$ are separately conserved ($P_{L,R}$: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-3|Def. §C5a.4.3]]; Weyl forms: [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]).
>
> *Source: PS §3.4, eqs. (3.73), (3.75)–(3.76) and p. 51 (the chiral transformation)*

^thm-c5a-5-4

> [!derivation]- Derivation
> **1. Product rule.** $\partial_\mu(\bar\psi\gamma^\mu\gamma^5\psi) = (\partial_\mu\bar\psi)\gamma^\mu\gamma^5\psi + \bar\psi\gamma^\mu\gamma^5\partial_\mu\psi$ ($\gamma$'s constant).
>
> **2. First term.** $(\partial_\mu\bar\psi)\gamma^\mu = im\bar\psi$ (conjugate equation, as in Derivation §C5a.5.3, step 5): $im\bar\psi\gamma^5\psi$.
>
> **3. Second term.** Move $\gamma^5$ to the left: $\gamma^\mu\gamma^5 = -\gamma^5\gamma^\mu$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]]), so $\bar\psi\gamma^\mu\gamma^5\partial_\mu\psi = -\bar\psi\gamma^5\gamma^\mu\partial_\mu\psi = -\bar\psi\gamma^5(-im\psi) = im\bar\psi\gamma^5\psi$.
>
> **4. Add.** $\partial_\mu j^{\mu5} = 2im\bar\psi\gamma^5\psi$; for $m = 0$ it vanishes.
>
> **5. The chiral transformation.** $\psi' = e^{i\alpha\gamma^5}\psi$. Then $\psi'^\dagger = \psi^\dagger e^{-i\alpha\gamma^5}$ ($\gamma^5$ Hermitian) and $\bar\psi' = \psi^\dagger e^{-i\alpha\gamma^5}\gamma^0 = \bar\psi e^{+i\alpha\gamma^5}$, since $\gamma^5\gamma^0 = -\gamma^0\gamma^5$ term by term in the series. Kinetic term: $\bar\psi e^{i\alpha\gamma^5}\gamma^\mu e^{i\alpha\gamma^5}\partial_\mu\psi = \bar\psi\gamma^\mu e^{-i\alpha\gamma^5}e^{i\alpha\gamma^5}\partial_\mu\psi$: invariant. Mass term: $\bar\psi e^{2i\alpha\gamma^5}\psi \ne \bar\psi\psi$: not invariant unless $m = 0$. Noether: $\Delta\psi = i\gamma^5\psi$, $j^\mu_{\rm N} = i\bar\psi\gamma^\mu(i\gamma^5\psi) = -j^{\mu5}$ (with $\mathcal J = 0$ for $m = 0$).
>
> **6. Chiral currents.** $j^\mu \pm j^{\mu5}$ over 2 are $\bar\psi\gamma^\mu P_{R,L}\psi$; their Weyl forms are [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]. For $m = 0$ both $j^\mu$ and $j^{\mu5}$ are conserved, hence each combination.
>
> **What the derivation shows**
> - The mass is the only term that breaks chiral symmetry, because it is the only term that pairs $\psi_L$ with $\psi_R$ ([[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]).
> - ⚑ By-product: classical conservation for $m = 0$; whether it survives quantization is a separate question (it does not, in general: the axial anomaly, PS ch. 19, beyond the course).

^der-c5a-5-4

*Uses:* [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-13|Theorem §C5a.2.13]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^thm-c5a-4-5|Theorem §C5a.4.5]]

## Energy and momentum

> [!theorem] Theorem §C5a.5.5: The Canonical Energy–Momentum Tensor of the Dirac Field
> For [[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]] the canonical tensor ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]]) is
>
> $$
> T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L ,
> $$
>
> and $\partial_\mu T^{\mu\nu} = 0$ on solutions (the first index is the current index). On solutions $\mathcal L = 0$, so $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi$, which is not symmetric.
>
> *Source: PHY 513, Problem Set 5, Problem 4(a) (as the user wrote it) · the user's PHY 513 notes, Ch. 8 §8.8 (Derivation "The Dirac energy–momentum tensor is conserved, and the momentum operator"), Ch. 3 §3.5 (table of canonical tensors)*

^thm-c5a-5-5

> [!derivation]- Derivation (as the user wrote it for Problem Set 5, Problem 4(a))
> Write $\mathcal L = \bar\psi(i\gamma^\rho\partial_\rho - m)\psi$ with the summed index renamed $\rho$, apart from the free $\mu$, $\nu$.
>
> **1. The tensor.** $\partial\mathcal L/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu$ and $\partial\mathcal L/\partial(\partial_\mu\bar\psi) = 0$, so Def. §C1b.6.2 gives $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi + 0 - g^{\mu\nu}\mathcal L$.
>
> **2. The two equations of motion.** $i\gamma^\rho\partial_\rho\psi = m\psi$ and $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]]).
>
> **3. The divergence, by the product rule.** With $\partial_\mu g^{\mu\nu} = 0$ and $g^{\mu\nu}\partial_\mu = \partial^\nu$,
>
> $$
> \partial_\mu T^{\mu\nu} = i(\partial_\mu\bar\psi)\gamma^\mu\partial^\nu\psi + i\bar\psi\gamma^\mu\partial_\mu\partial^\nu\psi - (\partial^\nu\bar\psi)(i\gamma^\rho\partial_\rho - m)\psi - \bar\psi(i\gamma^\rho\partial_\rho - m)\partial^\nu\psi .
> $$
>
> The last two terms are $\partial^\nu\mathcal L$, the derivative hitting $\bar\psi$ and then $\psi$; $\gamma$'s and $m$ are constant.
>
> **4. Use the equations.** First term: $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$, so it is $-m\bar\psi\partial^\nu\psi$. Third term: $(i\gamma^\rho\partial_\rho - m)\psi = 0$, so it vanishes.
>
> **5. Expand the last term.** $-\bar\psi(i\gamma^\rho\partial_\rho - m)\partial^\nu\psi = -i\bar\psi\gamma^\rho\partial_\rho\partial^\nu\psi + m\bar\psi\partial^\nu\psi$.
>
> **6. Collect.**
>
> $$
> \partial_\mu T^{\mu\nu} = \bigl(-m\bar\psi\partial^\nu\psi + m\bar\psi\partial^\nu\psi\bigr) + \bigl(i\bar\psi\gamma^\mu\partial_\mu\partial^\nu\psi - i\bar\psi\gamma^\rho\partial_\rho\partial^\nu\psi\bigr) = 0 ,
> $$
>
> the mass terms cancelling and the second pair being equal ($\mu$, $\rho$ are both dummies).
>
> **What the derivation shows**
> - Both equations of motion are needed, one for each field; this is the general statement [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]] (off shell, $\partial_\mu T^{\mu\nu} = -\sum_a\mathrm{EL}_a\partial^\nu\phi_a$) for this $\mathcal L$, here checked directly.
> - ⚑ By-product: $T^{\mu\nu} - T^{\nu\mu} = i\bar\psi(\gamma^\mu\partial^\nu - \gamma^\nu\partial^\mu)\psi \ne 0$; the antisymmetric part is the divergence of the spin current ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]]; Theorem §C5a.5.8), and is removed in Theorem §C5a.5.9.
> - Assumption: $\psi \in C^2$ (second derivatives commute in the cancellation of step 6).

^der-c5a-5-5

*Uses:* [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]]

*Procedure:* [[P3 Noether's Procedure#^p3-4|P3, steps 4–5]]

> [!theorem] Theorem §C5a.5.6: Energy and Momentum of the Dirac Field
> The charges $P^\nu = \int d^3x\,T^{0\nu}$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]) of the canonical tensor of [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-5|Theorem §C5a.5.5]] are, with $\mathcal H$ of [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-2|Theorem §C5a.5.2]] and $\pi_\psi = i\psi^\dagger$ of [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]],
>
> $$
> H = P^0 = \int d^3x\,\mathcal H = \int d^3x\,\psi^\dagger\bigl(-i\boldsymbol\alpha\cdot\nabla + \beta m\bigr)\psi \;\overset{\text{on shell}}{=}\; \int d^3x\,\psi^\dagger\,i\partial_t\psi, \qquad \mathbf P = \int d^3x\,\psi^\dagger\bigl(-i\nabla\bigr)\psi = -\int d^3x\;\pi_\psi\,\nabla\psi ,
> $$
>
> with $P^i = \int d^3x\,T^{0i}$ and $T^{0i} = -i\psi^\dagger\partial_i\psi = -\pi_\psi\,\partial_i\psi$. $\mathbf P$ is the Noether charge of spatial translations, not the canonical momentum $\pi_\psi = i\psi^\dagger$; both $H$ and $\mathbf P$ are real for fields falling off at spatial infinity.
>
> *Source: PHY 513, Problem Set 5, Problem 4(b) (as the user wrote it) · the user's PHY 513 notes, Ch. 8 §8.8, eq. (diracP) · PS §3.5, eqs. (3.84), (3.105) · the index-by-index computation written out here, as for the scalar ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7|Theorem §C1b.6.7]])*

^thm-c5a-5-6

> [!derivation]- Derivation
> **Step 1** (the coefficients of the current index). With $\mathcal L = \bar\psi(i\gamma^\rho\partial_\rho - m)\psi$, the fields $\psi$ and $\bar\psi$ independent, $\partial\mathcal L/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu$ and $\partial\mathcal L/\partial(\partial_\mu\bar\psi) = 0$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-6|Derivation §C5a.3.6]], step 3). For $\mu = 0$: $i\bar\psi\gamma^0 = i\psi^\dagger(\gamma^0)^2 = i\psi^\dagger = \pi_\psi$, the canonical momentum ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]]); $\bar\psi$ has none.
>
> **Step 2** (the tensor). [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], summed over both fields, the $\bar\psi$ term being zero: $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-5|Theorem §C5a.5.5]]). Only the row $\mu = 0$ enters the charges (Theorem §C1b.6.6).
>
> **Step 3** ($T^{00}$, the energy density). Put $\mu = \nu = 0$: $\partial^0 = g^{00}\partial_0 = \partial_t$ and $g^{00} = 1$, so $T^{00} = i\bar\psi\gamma^0\partial_t\psi - \mathcal L = i\psi^\dagger\partial_t\psi - \mathcal L = \pi_\psi\dot\psi - \mathcal L$ (Step 1). This is the Legendre transform, $\mathcal H$ of [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-2|Theorem §C5a.5.2]], identically: $P^0 = \int d^3x\,\mathcal H = H$. On shell $\mathcal L = 0$ (the Dirac equation sets $(i\slashed{\partial} - m)\psi = 0$ inside $\mathcal L$), so $T^{00} = i\psi^\dagger\partial_t\psi$ there.
>
> ⚑ By-product: the Noether charge of time translations and the Legendre-transform Hamiltonian are one function of the canonical data, as for the scalar → [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-1|§C1b.6, Remark: Why the 00 component is the Hamiltonian density]].
>
> **Step 4** ($T^{0i}$, index by index). Put $\mu = 0$, $\nu = i \in \{1, 2, 3\}$: $T^{0i} = i\bar\psi\gamma^0\partial^i\psi - g^{0i}\mathcal L$. The metric is diagonal, $g^{0i} = 0$, so the $\mathcal L$ term drops. $\bar\psi\gamma^0 = \psi^\dagger$ (Step 1). The upper spatial derivative is $\partial^i = g^{ii}\partial_i = -\partial_i$ (no sum; $g^{ii} = -1$; Step 4 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-7|Derivation §C1b.6.7]]). Hence
>
> $$
> T^{0i} = i\psi^\dagger\partial^i\psi = -i\psi^\dagger\partial_i\psi = -\pi_\psi\,\partial_i\psi .
> $$
>
> **Step 5** (the momentum vector). $P^i = \int d^3x\,T^{0i} = \int d^3x\,\psi^\dagger(-i\partial_i)\psi$. With $\partial_i = \partial/\partial x^i$ the Cartesian components of $\nabla$, the three charges are the components of $\mathbf P = \int d^3x\,\psi^\dagger(-i\nabla)\psi = -\int d^3x\,\pi_\psi\nabla\psi$.
>
> ⚑ By-product: the minus sign is the metric's ($\partial^i = -\partial_i$), as for the scalar, and $\mathbf P$ has the general form $-\int d^3x\sum_a\pi_a\nabla\phi_a$ of Theorem §C1b.6.6 with the single canonical pair $(\psi, \pi_\psi)$: $\bar\psi$ contributes nothing because its momentum is zero → [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^rem-c5a-5-1|Remark: Why P is the momentum, for the Dirac field]].
>
> **Step 6** (reality). The densities are not real pointwise, but their integrals are. For $\mathbf P$: $\bigl(\psi^\dagger(-i\partial_i)\psi\bigr)^{\ast} = i(\partial_i\psi^\dagger)\psi = \psi^\dagger(-i\partial_i)\psi + i\partial_i(\psi^\dagger\psi)$ by the product rule, and the last term is a total derivative, which integrates to zero for fields falling off at infinity ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]). For $H$ the same holds term by term: $\beta$ and $\boldsymbol\alpha$ are Hermitian ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-5-2|Derivation §C5a.5.2]], step 5), so $(\psi^\dagger\beta m\psi)^{\ast} = \psi^\dagger\beta m\psi$, and the $\boldsymbol\alpha\cdot\nabla$ term changes by $i\partial_j(\psi^\dagger\alpha^j\psi)$.
>
> **Step 7** (conservation). By Theorem §C5a.5.5 ($\partial_\mu T^{\mu\nu} = 0$ on solutions) and [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]], $dP^\nu/dt = 0$ for fields with $T^{i\nu}$ falling off faster than $1/r^2$.
>
> **Step 8** (collect). $P^0 = H$ (Step 3) and $P^i$ (Step 5) are the four charges $P^\mu = (H, \mathbf P)$.
>
> **What the derivation shows**
> - $\mathbf P$ is the expectation of the one-particle momentum operator $-i\nabla$ in the "wave function" $\psi$, and $H$ that of $H_{\text{s.p.}}$: the field charges look like one-particle expectation values, the reason the Dirac sea picture works as far as it does.
> - ⚑ By-product: classically $H$ is unbounded below (negative-frequency modes, [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-2|Theorem §C5a.5.2]]); in mode form after quantization it is positive only with anticommutators ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]]).
> - The canonical momentum $\pi_\psi = i\psi^\dagger$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]]) is a field, conjugate to $\psi$ in the brackets; $\mathbf P$ is a number (an operator after quantization) generating translations. Problem Set 5's note makes the same distinction.
> - Assumptions: the field equation (for $T^{00} = i\psi^\dagger\partial_t\psi$ and for conservation only; the expressions for $H$ and $\mathbf P$ hold for any configuration) and fall-off at spatial infinity (reality, conservation).
> - Used next: $\hat{\mathbf P}$ generates spatial translations ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-7|Theorem §C5a.5.7]]); the quantized field's $\hat H$ and $\hat{\mathbf P}$ in modes ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]]).

^der-c5a-5-6

*Uses:* [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-5|Theorem §C5a.5.5]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^der-c5a-3-6|Derivation §C5a.3.6]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-7|Derivation §C1b.6.7]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]

*Procedure:* [[P3 Noether's Procedure#^p3-6|P3, step 6]], [[P1 Canonical Quantization#^p1-3|P1, step 3]]

> [!theorem] Theorem §C5a.5.7: The Dirac Momentum Generates Spatial Translations
> Treat the four complex components $\psi_a$ as coordinates and $\pi_a = i\psi^\dagger_a$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]]) as their momenta, with the Poisson bracket of [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]] on these pairs, $\{\psi_a(\mathbf x), \pi_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, i.e. $\{\psi_a(\mathbf x), \psi^\dagger_b(\mathbf y)\} = -i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$: $\psi^\dagger$ is the momentum, not a second coordinate ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]]; that these are the brackets compatible with the constraint $\pi_\psi = i\psi^\dagger$ is the Dirac bracket of [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]]). For commuting components, differentiable and falling off at spatial infinity, and $\mathbf P = -\int d^3x\,\pi_\psi\nabla\psi = \int d^3x\,\psi^\dagger(-i\nabla)\psi$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-6|Theorem §C5a.5.6]]), as identities after smearing with test functions:
> 1. $\{\psi_a(\mathbf x), \mathbf P\} = -\nabla\psi_a(\mathbf x)$ and $\{\psi^\dagger_a(\mathbf x), \mathbf P\} = -\nabla\psi^\dagger_a(\mathbf x)$;
> 2. $\{\psi_a(\mathbf x), H\} = -i\bigl(H_{\text{s.p.}}\psi\bigr)_a(\mathbf x)$ with $H_{\text{s.p.}}$ of [[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-4|Def. §C5a.3.4]], which is $\partial_t\psi_a$ on solutions of the Dirac equation; with $P^0 = H$, in covariant form $\{\psi_a(x), P^\mu\} = \partial^\mu\psi_a(x)$ on solutions;
> 3. $\{\mathbf P, H\} = 0$.
>
> *Source: the scalar statement, [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]] (for particles [[§B8.1 Poisson Brackets#^thm-b8-1-5|CM Theorem §B8.1.5]]), applied here to the Dirac canonical pairs; the classical root of [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]]; written out here*

^thm-c5a-5-7

> [!derivation]- Derivation
> Write $P^i = -\int d^3z\sum_c\pi_c(\mathbf z)\,\partial_i\psi_c(\mathbf z)$ on one time slice (Theorem §C5a.5.6): the form of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]] with the four pairs $(\phi_c, \pi_c) = (\psi_c, \pi_c)$. The fields are complex; $\psi_c$ and $\pi_c$ are the independent variables of the functionals, as $\phi$ and $\phi^{\ast}$ were for the complex scalar ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]), and $\psi^\dagger_c = -i\pi_c$ is not varied separately.
>
> **Step 1** ($\delta P^i/\delta\pi_c$). Vary $\pi_c \to \pi_c + \varepsilon\zeta_c$, $\zeta_c$ a test function, $\psi$ fixed. $P^i$ is linear in $\pi$: $\frac{d}{d\varepsilon}P^i\big|_0 = -\int d^3z\sum_c\zeta_c\,\partial_i\psi_c$, so ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|Def. §C1b.2.4]], on a slice)
>
> $$
> \frac{\delta P^i}{\delta\pi_c(\mathbf z)} = -\partial_i\psi_c(\mathbf z) .
> $$
>
> **Step 2** ($\delta P^i/\delta\psi_c$). Vary $\psi_c \to \psi_c + \varepsilon\eta_c$, $\pi$ fixed: $\frac{d}{d\varepsilon}P^i\big|_0 = -\int d^3z\sum_c\pi_c\,\partial_i\eta_c$. With $\pi_c\,\partial_i\eta_c = \partial_i(\pi_c\eta_c) - (\partial_i\pi_c)\eta_c$ and the first term integrating to zero ($\eta_c$ has compact support; [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]):
>
> $$
> \frac{\delta P^i}{\delta\psi_c(\mathbf z)} = +\partial_i\pi_c(\mathbf z) .
> $$
>
> ⚑ By-product: as for the scalar, the sign flips because the integration by parts moved $\partial_i$ onto $\pi$; this needs $\pi = i\psi^\dagger$ differentiable.
>
> **Step 3** (part 1 for $\psi$). Smear: $\psi_a(f) = \int d^3x\,f\psi_a$ has $\delta\psi_a(f)/\delta\psi_c = \delta_{ac}f$ and $\delta\psi_a(f)/\delta\pi_c = 0$. The bracket of Def. §C1b.4.3, with the sum over $c$ eliminating $c$ against $\delta_{ac}$:
>
> $$
> \{\psi_a(f), P^i\} = \sum_c\int d^3z\,\Bigl(\delta_{ac}f(\mathbf z)\cdot\bigl(-\partial_i\psi_c(\mathbf z)\bigr) - 0\cdot\partial_i\pi_c(\mathbf z)\Bigr) = -\int d^3z\,f(\mathbf z)\,\partial_i\psi_a(\mathbf z) ,
> $$
>
> i.e. $\{\psi_a(\mathbf x), P^i\} = -\partial_i\psi_a(\mathbf x)$.
>
> **Step 4** (part 1 for $\psi^\dagger$). For $\pi_a(g) = \int d^3x\,g\pi_a$ only the second term of the bracket survives: $\{\pi_a(g), P^i\} = \sum_c\int d^3z\,\bigl(0 - \delta_{ac}g(\mathbf z)\,\partial_i\pi_c(\mathbf z)\bigr) = -\int d^3z\,g\,\partial_i\pi_a$, i.e. $\{\pi_a(\mathbf x), P^i\} = -\partial_i\pi_a(\mathbf x)$. Since $\psi^\dagger_a = -i\pi_a$ and the bracket is linear, $\{\psi^\dagger_a(\mathbf x), P^i\} = -i\bigl(-\partial_i\pi_a(\mathbf x)\bigr) = -\partial_i\psi^\dagger_a(\mathbf x)$. Steps 3–4 are part 1.
>
> ⚑ By-product: the same result follows from the Dirac bracket of [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-4|★ Theorem §C5b.1.4]] and the form $\mathbf P = \int\psi^\dagger(-i\nabla)\psi$, because a Dirac bracket allows the constraint $\pi_\psi - i\psi^\dagger = 0$ to be imposed before it is computed ([[§C5b.1 Canonical Quantization of the Dirac Field#^def-c5b-1-3|★ Def. §C5b.1.3]]): the two forms of $\mathbf P$ have the same brackets.
>
> **Step 5** (part 2). $H = \int d^3z\,\psi^\dagger H_{\text{s.p.}}\psi = \int d^3z\sum_b(-i)\pi_b(H_{\text{s.p.}}\psi)_b$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-2|Theorem §C5a.5.2]], with $\psi^\dagger = -i\pi$) is linear in $\pi$ and contains no derivative of $\pi$, so $\delta H/\delta\pi_a(\mathbf z) = -i(H_{\text{s.p.}}\psi)_a(\mathbf z)$, and as in Step 3, $\{\psi_a(\mathbf x), H\} = \delta H/\delta\pi_a(\mathbf x) = -i(H_{\text{s.p.}}\psi)_a(\mathbf x)$. On solutions $i\partial_t\psi = H_{\text{s.p.}}\psi$ (the Dirac equation multiplied by $\gamma^0$, [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-5-2|Derivation §C5a.5.2]], step 6), so $\{\psi_a, H\} = \partial_t\psi_a = \partial^0\psi_a$ ($g^{00} = 1$). With $\partial^i = -\partial_i$, Step 3 reads $\{\psi_a, P^i\} = \partial^i\psi_a$; together $\{\psi_a(x), P^\mu\} = \partial^\mu\psi_a(x)$. (Hamilton's equations of these pairs in full, both of them, are [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-3|Theorem §C5b.1.3]].)
>
> **Step 6** (part 3). Write $H = \int d^3z\,\mathcal H(\psi, \partial_j\psi, \pi)$ with $\mathcal H = -i\pi_b(H_{\text{s.p.}}\psi)_b$, which contains no derivative of $\pi$ and no explicit $\mathbf z$. Then $\delta H/\delta\pi_c = \partial\mathcal H/\partial\pi_c$ and $\delta H/\delta\psi_c = \partial\mathcal H/\partial\psi_c - \partial_j\bigl(\partial\mathcal H/\partial(\partial_j\psi_c)\bigr)$ (integration by parts, fall-off). With Steps 1–2,
>
> $$
> \{P^i, H\} = \int d^3z\sum_c\Bigl(\partial_i\pi_c\,\frac{\delta H}{\delta\pi_c} + \partial_i\psi_c\,\frac{\delta H}{\delta\psi_c}\Bigr) = \int d^3z\,\Bigl(\partial_i\mathcal H - \partial_j\Bigl(\sum_c\partial_i\psi_c\,\frac{\partial\mathcal H}{\partial(\partial_j\psi_c)}\Bigr)\Bigr) ,
> $$
>
> using the chain rule $\partial_i\mathcal H = \sum_c\bigl(\frac{\partial\mathcal H}{\partial\pi_c}\partial_i\pi_c + \frac{\partial\mathcal H}{\partial\psi_c}\partial_i\psi_c + \frac{\partial\mathcal H}{\partial(\partial_j\psi_c)}\partial_i\partial_j\psi_c\bigr)$ (no explicit $\mathbf z$) and the product rule on the last term. Both terms are total derivatives and integrate to zero (fall-off): $\{\mathbf P, H\} = 0$, as in Step 7 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-9|Derivation §C1b.6.9]].
>
> **What the derivation shows**
> - $\mathbf P$ acts on $\psi$ and on its momentum $i\psi^\dagger$ as $-\nabla$, as for the scalar: the Noether momentum is the generator of spatial translations, now for a first-order system in which the momentum is the adjoint field.
> - Assumptions: commuting components; differentiable $\pi = i\psi^\dagger$ (Step 2); fall-off (Steps 2, 6); the Dirac equation only for the time component (Step 5).
> - Used next: quantization turns $\{F, G\} \to -i[\hat F, \hat G]$ ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-5|§C1b.4, Remark: From brackets to commutators]]), and part 1 becomes $[\hat\psi_a, \hat{\mathbf P}] = -i\nabla\hat\psi_a$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]]), with anticommuting fields but a bilinear $\hat{\mathbf P}$.

^der-c5a-5-7

*Uses:* [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-6|Theorem §C5a.5.6]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-5-2|Derivation §C5a.5.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|Def. §C1b.2.4]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]

> [!remark] Remark: Why P is the momentum, for the Dirac field
> - *On a plane wave.* A positive-frequency plane wave $\psi = w\,e^{-ip\cdot x}$, $p^0 = E_{\mathbf p} > 0$, with a constant column $w$ solving the Dirac equation (so $H_{\text{s.p.}}(\mathbf p)w = E_{\mathbf p}w$, [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^der-c5a-5-2|Derivation §C5a.5.2]], steps 6–7), has $-i\nabla\psi = \mathbf p\,\psi$ and $i\partial_t\psi = E_{\mathbf p}\psi$, so the momentum density is $\psi^\dagger(-i\nabla)\psi = \mathbf p\,w^\dagger w$, the energy density $\psi^\dagger i\partial_t\psi = E_{\mathbf p}\,w^\dagger w$ and the charge density $\psi^\dagger\psi = w^\dagger w > 0$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-3|Theorem §C5a.5.3]]). Per unit charge the wave carries momentum $\mathbf p$ and energy $E_{\mathbf p}$, with no averaging needed (unlike the real scalar wave of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-2|§C1b.6, Remark: Why P is the momentum]]): after quantization this is $\mathbf p$ per particle ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]]).
> - *Not the canonical momentum.* $\pi_\psi = i\psi^\dagger$ is conjugate to the field value $\psi(\mathbf x)$ at one point, a momentum in field space; $\psi^\dagger$ itself is not the momentum density. The momentum carried through space is $T^{0i} = -\pi_\psi\,\partial_i\psi$, built from $\pi_\psi$ and the generator $\partial_i\psi$ of the translation, the pattern $\int d^3x\,\pi\,\Delta\phi$ of every Noether charge ([[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]]).
> - *Negative frequency.* $\psi = w\,e^{+ip\cdot x}$ has momentum density $-\mathbf p\,w^\dagger w$ and energy density $-E_{\mathbf p}\,w^\dagger w$: classically it carries the momentum opposite to its label and negative energy (Theorem §C5a.5.2). After quantization with anticommutators the $\hat b$ term of $\hat{\mathbf P}$ arrives as $-\hat b\,\hat b^\dagger$; reordering it gives $+\hat b^\dagger\hat b$ plus a constant $\propto\int d^3p\,\mathbf p$, which vanishes by reflection symmetry, so the antiparticle of label $\mathbf p$ carries $+\mathbf p$ and no ordering choice is involved ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]]); for $\hat H$ the same reordering leaves the negative fermionic zero-point energy ([[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.8, eq. (diracP) · PS §3.5, eq. (3.105) · the plane-wave densities worked out here*

^rem-c5a-5-1

## Spin and the symmetric tensor

> [!theorem] Theorem §C5a.5.8: The Spin Current and the Angular Momentum of the Dirac Field
> The spin part of the Lorentz current of [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]] is, for the Dirac field,
>
> $$
> \mathcal S^{\lambda\mu\nu} = \bar\psi\gamma^\lambda S^{\mu\nu}\psi = \tfrac i4\,\bar\psi\gamma^\lambda[\gamma^\mu, \gamma^\nu]\psi ,
> $$
>
> with the Hermitian-convention generators $S^{\mu\nu}$ of [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]] (which are $i$ times the real-convention ones of Theorem §C1b.7.1: [[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-2|§C3.4, Caution: Two meanings of S^μν]]); and on solutions the angular momentum $J^i = \frac12\varepsilon_{ijk}J^{jk}$ ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-7-1|Def. §C1b.7.1]]) is
>
> $$
> \mathbf J = \int d^3x\,\psi^\dagger\Bigl(\mathbf x\times(-i\nabla) + \tfrac12\boldsymbol\Sigma\Bigr)\psi, \qquad \boldsymbol\Sigma = \begin{pmatrix}\boldsymbol\sigma & 0\\ 0 & \boldsymbol\sigma\end{pmatrix} :
> $$
>
> orbital plus spin $\frac12$, with $\frac12\boldsymbol\Sigma = \mathbf S$ the spin matrices ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-6|Def. §C5a.2.6]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (eq. (Mgeneral); "the Dirac spin $\frac12$") · Yu §1.7.3, eqs. (1.241)–(1.248) (orbital and spin split) · computed here from [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]]*

^thm-c5a-5-8

> [!derivation]- Derivation
> **1. The generator in the convention of Theorem §C1b.7.1.** There $D = 1 + \frac12\omega_{\mu\nu}S^{\mu\nu}_{(C1.8)}$, with $S^{\mu\nu}_{(C1.8)}$ the real-convention generators of [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]; for the Dirac field $D = \Lambda_{1/2} = 1 - \frac i2\omega_{\mu\nu}S^{\mu\nu} + O(\omega^2)$. The $\omega_{\mu\nu}$ are arbitrary antisymmetric and both generators antisymmetric, so $S^{\mu\nu}_{(C1.8)} = -iS^{\mu\nu}$ ([[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-2|§C3.4, Caution: Two meanings of S^μν]]).
>
> **2. The spin current.** $\mathcal S^{\lambda\mu\nu} = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\lambda\phi_a)}(S^{\mu\nu}_{(C1.8)}\phi)_a$, summed over $\psi$ and $\bar\psi$. The $\bar\psi$ term is zero ($\partial\mathcal L/\partial(\partial_\lambda\bar\psi) = 0$). The $\psi$ term: $i\bar\psi\gamma^\lambda\cdot(-iS^{\mu\nu}\psi) = \bar\psi\gamma^\lambda S^{\mu\nu}\psi$, and $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]]).
>
> **3. The spin charges.** $S^{\mu\nu}_{\rm charge} = \int d^3x\,\mathcal S^{0\mu\nu} = \int d^3x\,\bar\psi\gamma^0S^{\mu\nu}\psi = \int d^3x\,\psi^\dagger S^{\mu\nu}\psi$.
>
> **4. Spatial generators.** In the chiral basis $S^{jk} = \frac12\varepsilon^{jkl}\Sigma^l$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]]), so $\frac12\varepsilon_{ijk}S^{jk} = \frac14\varepsilon_{ijk}\varepsilon_{jkl}\Sigma^l = \frac14\cdot2\delta_{il}\Sigma^l = \frac12\Sigma^i$, using $\varepsilon_{ijk}\varepsilon_{ljk} = 2\delta_{il}$ (with $\varepsilon_{jkl} = \varepsilon_{ljk}$, cyclic). The spin part of $J^i$ is $\int\psi^\dagger\frac12\Sigma^i\psi$.
>
> **5. The orbital part.** On shell $T^{0\rho} = i\psi^\dagger\partial^\rho\psi$ (Derivation §C5a.5.6). $L^{jk} = \int d^3x\,(x^jT^{0k} - x^kT^{0j}) = \int d^3x\,\psi^\dagger\,i(x^j\partial^k - x^k\partial^j)\psi = \int d^3x\,\psi^\dagger(-i)(x^j\partial_k - x^k\partial_j)\psi$ ($\partial^k = -\partial_k$). Then $\frac12\varepsilon_{ijk}L^{jk} = \int\psi^\dagger(-i)\varepsilon_{ijk}x^j\partial_k\psi = \int\psi^\dagger\bigl(\mathbf x\times(-i\nabla)\bigr)_i\psi$ (the two terms of the antisymmetric bracket give equal contributions after renaming $j \leftrightarrow k$).
>
> **6. Total.** $J^i = L^i + S^i$ by [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-7-1|Def. §C1b.7.1]].
>
> **What the derivation shows**
> - ⚑ By-product: the Dirac field carries spin $\frac12$: $\frac12\boldsymbol\Sigma$ has $(\frac12\Sigma^i)(\frac12\Sigma^i) = \frac34\mathbb 1$, two spin-½ doublets, one per Weyl block. Peskin–Schroeder prove the particle's spin from this charge after quantization ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]).
> - Only $\mathbf J$ is conserved, not $\mathbf L$ and $\mathbf S$ separately: $\partial_\lambda\mathcal S^{\lambda\mu\nu} = T^{\nu\mu} - T^{\mu\nu} \ne 0$ ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]]).
> - Used next: the symmetric tensor (Theorem §C5a.5.9).

^der-c5a-5-8

*Uses:* [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-7-1|Def. §C1b.7.1]], [[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-2|§C3.4, Caution: Two meanings of S^μν]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^thm-c5a-2-8|Theorem §C5a.2.8]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]

This is Quantum Mechanics' $\mathbf J = \mathbf L + \frac\hbar2\boldsymbol\Sigma$, conserved while $\mathbf L$ and $\mathbf S$ are not ([[§C13.2★ The Dirac Equation#^thm-c13-2-4|QM Theorem §C13.2.4]]), now as Noether charges of a field: there it follows from commutators with $H$, here from rotation invariance of the action (rule 2).

> [!theorem] Theorem §C5a.5.9: The Symmetric Energy–Momentum Tensor of the Dirac Field
> The Belinfante tensor ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]]) of the Dirac field is, on solutions,
>
> $$
> \hat T^{\mu\nu} = \frac i4\,\bar\psi\bigl(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu}\bigr)\psi - g^{\mu\nu}\mathcal L = \frac i4\,\bar\psi\bigl(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu}\bigr)\psi :
> $$
>
> with $a\overleftrightarrow{\partial}b = a\,\partial b - (\partial a)\,b$: symmetric, conserved, with the same $P^\nu$ as the canonical tensor ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-5|Theorem §C5a.5.5]]) and with orbital moments that give the total $J^{\nu\rho}$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-8|Theorem §C5a.5.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (Derivation "Belinfante: symmetrizing T with the spin current", last sentence: the Dirac result, stated) · derived here from [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]]*

^thm-c5a-5-9

> [!derivation]- Derivation
> Work on solutions; write $V^\mu \equiv \frac i2\bar\psi\gamma^\mu\psi = \frac i2j^\mu$ and let $\gamma^{[\lambda\mu\nu]}$ be the totally antisymmetrized product, weight $1/3!$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]).
>
> **1. Split a product of three $\gamma$'s.** For all $\lambda, \mu, \nu$:
>
> $$
> \gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^{[\lambda\mu\nu]} + g^{\lambda\mu}\gamma^\nu - g^{\lambda\nu}\gamma^\mu + g^{\mu\nu}\gamma^\lambda .
> $$
>
> Check case by case, using only the Clifford algebra (distinct $\gamma$'s anticommute, $(\gamma^\lambda)^2 = g^{\lambda\lambda}$, no sum): all distinct, the antisymmetrization is the product itself (each of the six terms, reordered, carries its sign twice) and all $g$'s vanish; $\lambda = \mu \ne \nu$: left $g^{\lambda\lambda}\gamma^\nu$, right $0 + g^{\lambda\lambda}\gamma^\nu$; $\lambda = \nu \ne \mu$: left $\gamma^\lambda\gamma^\mu\gamma^\lambda = -g^{\lambda\lambda}\gamma^\mu$, right $-g^{\lambda\lambda}\gamma^\mu$; $\mu = \nu \ne \lambda$: both $g^{\mu\mu}\gamma^\lambda$; all equal: left $g^{\lambda\lambda}\gamma^\lambda$, right $g^{\lambda\lambda}\gamma^\lambda(1 - 1 + 1)$. (A repeated index kills the antisymmetrized product: its terms cancel in pairs.)
>
> **2. The spin current in pieces.** Subtract step 1 with $\mu \leftrightarrow \nu$: $\gamma^\lambda[\gamma^\mu, \gamma^\nu] = 2\gamma^{[\lambda\mu\nu]} + 2g^{\lambda\mu}\gamma^\nu - 2g^{\lambda\nu}\gamma^\mu$ (the $g^{\mu\nu}\gamma^\lambda$ terms cancel, the antisymmetric part doubles). With Theorem §C5a.5.8,
>
> $$
> \mathcal S^{\lambda\mu\nu} = A^{\lambda\mu\nu} + g^{\lambda\mu}V^\nu - g^{\lambda\nu}V^\mu, \qquad A^{\lambda\mu\nu} \equiv \tfrac i2\bar\psi\gamma^{[\lambda\mu\nu]}\psi \ \ \text{(totally antisymmetric)} .
> $$
>
> **3. Belinfante's $K$.** $K^{\lambda\mu\nu} = \frac12(\mathcal S^{\lambda\mu\nu} + \mathcal S^{\mu\nu\lambda} + \mathcal S^{\nu\mu\lambda})$. The $A$ parts: $A^{\mu\nu\lambda} = A^{\lambda\mu\nu}$ (cyclic) and $A^{\nu\mu\lambda} = -A^{\lambda\mu\nu}$ (one transposition), total $A^{\lambda\mu\nu}$. The $V$ parts: $(g^{\lambda\mu}V^\nu - g^{\lambda\nu}V^\mu) + (g^{\mu\nu}V^\lambda - g^{\mu\lambda}V^\nu) + (g^{\nu\mu}V^\lambda - g^{\nu\lambda}V^\mu) = 2g^{\mu\nu}V^\lambda - 2g^{\lambda\nu}V^\mu$. Hence
>
> $$
> K^{\lambda\mu\nu} = \tfrac12A^{\lambda\mu\nu} + g^{\mu\nu}V^\lambda - g^{\lambda\nu}V^\mu ,
> $$
>
> antisymmetric in $\lambda\mu$ as it must be.
>
> **4. Its divergence.** $\partial_\lambda K^{\lambda\mu\nu} = \frac12\partial_\lambda A^{\lambda\mu\nu} + g^{\mu\nu}\partial_\lambda V^\lambda - \partial^\nu V^\mu$. The middle term vanishes on shell ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-3|Theorem §C5a.5.3]]).
>
> **5. The vector piece symmetrizes the derivative.** $T^{\mu\nu} - \partial^\nu V^\mu = i\bar\psi\gamma^\mu\partial^\nu\psi - \frac i2(\partial^\nu\bar\psi)\gamma^\mu\psi - \frac i2\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L = \frac i2\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi - g^{\mu\nu}\mathcal L$.
>
> **6. The divergence of $A$.** Write $\gamma^{[\lambda\mu\nu]}$ by step 1 in two ways: $= \gamma^\lambda\gamma^\mu\gamma^\nu - g^{\lambda\mu}\gamma^\nu + g^{\lambda\nu}\gamma^\mu - g^{\mu\nu}\gamma^\lambda$ (for the term with $\partial_\lambda\bar\psi$), and, since $\gamma^{[\lambda\mu\nu]} = \gamma^{[\mu\nu\lambda]}$, $= \gamma^\mu\gamma^\nu\gamma^\lambda - g^{\mu\nu}\gamma^\lambda + g^{\mu\lambda}\gamma^\nu - g^{\nu\lambda}\gamma^\mu$ (for the term with $\partial_\lambda\psi$). With $(\partial_\lambda\bar\psi)\gamma^\lambda = im\bar\psi$ and $\gamma^\lambda\partial_\lambda\psi = -im\psi$:
>
> $$
> (\partial_\lambda\bar\psi)\gamma^{[\lambda\mu\nu]}\psi = im\bar\psi\gamma^\mu\gamma^\nu\psi - (\partial^\mu\bar\psi)\gamma^\nu\psi + (\partial^\nu\bar\psi)\gamma^\mu\psi - im\,g^{\mu\nu}\bar\psi\psi ,
> $$
>
> $$
> \bar\psi\gamma^{[\lambda\mu\nu]}\partial_\lambda\psi = -im\bar\psi\gamma^\mu\gamma^\nu\psi + im\,g^{\mu\nu}\bar\psi\psi + \bar\psi\gamma^\nu\partial^\mu\psi - \bar\psi\gamma^\mu\partial^\nu\psi .
> $$
>
> Adding, all four mass terms cancel: $\partial_\lambda(\bar\psi\gamma^{[\lambda\mu\nu]}\psi) = \bar\psi\gamma^\nu\overleftrightarrow{\partial^\mu}\psi - \bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi$, so $\frac12\partial_\lambda A^{\lambda\mu\nu} = \frac i4\bigl(\bar\psi\gamma^\nu\overleftrightarrow{\partial^\mu}\psi - \bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi\bigr)$.
>
> **7. Assemble.** $\hat T^{\mu\nu} = T^{\mu\nu} + \partial_\lambda K^{\lambda\mu\nu} = \frac i2\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi + \frac i4\bar\psi\gamma^\nu\overleftrightarrow{\partial^\mu}\psi - \frac i4\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi - g^{\mu\nu}\mathcal L = \frac i4\bar\psi(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu})\psi - g^{\mu\nu}\mathcal L$, and $\mathcal L = 0$ on shell. Symmetric by inspection.
>
> **What the derivation shows**
> - The improvement has two parts: a vector part that turns $\overrightarrow\partial$ into $\frac12\overleftrightarrow\partial$ (the same as passing to $\mathcal L_{\rm sym}$, [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-7|Theorem §C5a.3.7]]), and the totally antisymmetric spin part, which removes the antisymmetric part of $T$.
> - ⚑ By-product: $\hat T^{00} = \frac i2\bar\psi\gamma^0\overleftrightarrow{\partial^0}\psi = \frac i2(\psi^\dagger\dot\psi - \dot\psi^\dagger\psi)$, real, and it differs from $T^{00}$ by a total derivative; $H$ is unchanged (property 3 of Theorem §C1b.7.4, for fields falling off at infinity).
> - Both equations of motion and the conservation of $j^\mu$ were used; off shell $\hat T$ is not symmetric.
> - This is the tensor that couples to gravity ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.7]]).

^der-c5a-5-9

*Uses:* [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-8|Theorem §C5a.5.8]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-6|Theorem §C5a.3.6]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]

> [!remark]- Connections
> - Treating $\psi$ and $\bar\psi$ as independent is the complex scalar's device; the first-order Lagrangian pushes the crossover of momenta to its end, $\pi_\psi = i\psi^\dagger$, which is why fermions are quantized by a bracket between $\psi$ and $\psi^\dagger$ alone — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]], [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]].
> - The unbounded classical energy of Theorem §C5a.5.2 is the Dirac version of the indefinite Klein–Gordon density of Quantum Mechanics; in both cases the field theory reinterprets negative frequency as antiparticles, but only anticommutators make the Dirac Hamiltonian positive — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]], [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]].
> - The procedure of canonical quantization starts from exactly the data assembled here (Lagrangian, momenta, Hamiltonian density) — [[P1 Canonical Quantization#^p1-1|P1, steps 1–3]].
> - The positive conserved density $\psi^\dagger\psi$ is Quantum Mechanics' probability density; in the field theory it is the time component of a Noether current, and after quantization a charge of either sign — [[§C13.2★ The Dirac Equation#^thm-c13-2-3|QM Theorem §C13.2.3]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles|§C5b.5]].
> - The spin current $\bar\psi\gamma^\lambda S^{\mu\nu}\psi$ is the field-theoretic origin of the electron's spin $\frac12$ and of the non-conservation of $\mathbf L$ alone; Belinfante's improvement moves the spin into a symmetric $\hat T$ — [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]], [[§C13.2★ The Dirac Equation#^thm-c13-2-4|QM Theorem §C13.2.4]].
> - The same Noether procedure gave the scalar's U(1) current and $T^{\mu\nu}$; for the Dirac field every step is identical except that only $\psi$, not $\bar\psi$, has a derivative in $\mathcal L$ — [[P3 Noether's Procedure]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-3|§C1b.6, Remark: The canonical tensor of the standard fields]].
> - The field momentum and its bracket follow the scalar's and the vector's pattern index by index, $T^{0i} = -\sum_a\pi_a\partial_i\phi_a$ and $\{\phi_a, \mathbf P\} = -\nabla\phi_a$; for the Dirac field the only canonical pair is $(\psi, i\psi^\dagger)$, so $\bar\psi$ contributes nothing, and the bracket becomes the quantum translation law once the brackets become anticommutators — [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7|Theorem §C1b.6.7]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]], [[§C4.2★ The Proca Field#^thm-c4-2-13|Theorem §C4.2.13]], [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-7|Theorem §C5a.5.7]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]].
