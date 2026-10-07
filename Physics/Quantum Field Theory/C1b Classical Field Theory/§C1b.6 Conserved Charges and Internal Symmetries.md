---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.5 Noether's Theorem]] · ↑ [[· C1b Classical Field Theory]] · [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum]] →

*Sources: the user's PHY 513 notes, Ch. 3 §3.5 (From current to charge; Caution "What the theorem does and does not say"; Examples I) · PHY 513 Lecture 3 (Larsen), Part C ("Noether's Charge", Examples 1–2); Problem Set 2, Problems 3 and 4(d), with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2 · Yu Zhao-Huan, 量子场论讲义, §§1.7.1, 1.7.4 · the user's pre-course notes, §1.7.*

What does a conserved current conserve, how unique is it, and what do the internal symmetries of the scalar fields give? This section starts from Noether's theorem and its failure case ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]) and from the algorithm [[P3 Noether's Procedure]]. It turns a conserved current into a charge that changes only by the flux through a boundary (step 6), states the freedom left in the current (improvement terms), and runs the procedure on the internal symmetries: the shift of a real field, the U(1) phase of the complex field, the rotation of two real fields, and a mass splitting that breaks the phase. Spacetime symmetries, where the point moves, are [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]].

## From current to charge

> [!definition] Definition §C1b.6.1: Charge Density
> For a Noether current $j^\mu = (j^0, \mathbf j)$, with $\mathbf j$ the vector of components $j^i$, the **charge density** is $\rho \equiv j^0$. It need not be an electric charge density.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eq. (charge) · PS §2.2, eq. (2.13) · Lecture 3, "Noether's Charge" · Yu §1.7.1, eqs. (1.200), (1.202)*

^def-c1b-6-1

> [!definition] Definition §C1b.6.2: Noether Charge
> The **Noether charge** of a current $j^\mu$ in a fixed spatial region $V$ and in all of space is the integral of its charge density ([[§C1b.6 Conserved Charges and Internal Symmetries#^def-c1b-6-1|Def. §C1b.6.1]]),
>
> $$
> Q_V(t) \equiv \int_Vd^3x\;j^0(t, \mathbf x), \qquad Q \equiv \int d^3x\;j^0(t, \mathbf x) ;
> $$
>
> one charge per parameter, $Q_a = \int d^3x\,j^0_a$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eq. (charge) · PS §2.2, eq. (2.13) · Lecture 3, "Noether's Charge" · Yu §1.7.1, eqs. (1.200), (1.202)*

^def-c1b-6-2

> [!theorem] Theorem §C1b.6.1: Continuity Equation and Conservation of the Charge
> $\partial_\mu j^\mu = 0$ is the continuity equation $\partial_t\rho + \nabla\cdot\mathbf j = 0$, and for a fixed region $V$ with outward surface element $d\mathbf S$,
>
> $$
> \frac{dQ_V}{dt} = -\oint_{\partial V}\mathbf j\cdot d\mathbf S :
> $$
>
> the charge in a region changes only by the current through its surface. If $\lvert\mathbf j\rvert$ falls off faster than $1/r^2$ at spatial infinity, the total charge $Q$ is constant in time. A symmetry with $\dim G$ parameters gives $\dim G$ conserved charges.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eqs. (continuity), (dQdt) · Yu §1.7.1, eqs. (1.199)–(1.202) · PS §2.2 · Lecture 3, "Noether's Charge"*

^thm-c1b-6-1

> [!derivation]- Derivation
> **1. Components.** $x^\mu = (t, \mathbf x)$ and $\partial_\mu = \partial/\partial x^\mu = (\partial_t, \nabla)$, with $(\nabla)_i = \partial_i$. A lower index contracted with an upper index is a plain sum, with no metric: $\partial_\mu j^\mu = \partial_0j^0 + \partial_1j^1 + \partial_2j^2 + \partial_3j^3 = \partial_t\rho + \nabla\cdot\mathbf j$. ⚑ By-product: the sign between the two terms is $+$; the slides write $-$ → [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-1|Caution: The sign in the slides' continuity equation]].
>
> **2. Integrate over $V$ at fixed $t$.** $\int_Vd^3x\,\partial_t\rho = -\int_Vd^3x\,\nabla\cdot\mathbf j$.
>
> **3. Take $d/dt$ outside.** For bounded $V$ and continuous $\rho$, $\partial_t\rho$, differentiation under the integral sign is allowed ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]): $\int_Vd^3x\,\partial_t\rho = \frac{d}{dt}\int_Vd^3x\,\rho = dQ_V/dt$.
>
> **4. Divergence theorem.** $\int_Vd^3x\,\nabla\cdot\mathbf j = \oint_{\partial V}\mathbf j\cdot d\mathbf S$ ([[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|452 Thm. §32.1]]). With step 2, $dQ_V/dt = -\oint_{\partial V}\mathbf j\cdot d\mathbf S$.
>
> **5. All of space.** Take $V$ the ball $B_R$ of radius $R$. The flux through its sphere obeys $\bigl\lvert\oint_{S_R}\mathbf j\cdot d\mathbf S\bigr\rvert \le 4\pi R^2\max_{\lvert\mathbf x\rvert = R}\lvert\mathbf j\rvert \to 0$ as $R \to \infty$ if $\lvert\mathbf j\rvert = o(1/R^2)$. If moreover $\rho$ and $\partial_t\rho$ have an integrable bound uniform in $t$, dominated convergence ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]) gives $dQ/dt = \int d^3x\,\partial_t\rho = \lim_{R\to\infty}\int_{B_R}d^3x\,\partial_t\rho = -\lim_{R\to\infty}\oint_{S_R}\mathbf j\cdot d\mathbf S = 0$. ⚑ By-product: the fall-off is an assumption about the field configuration, a boundary condition, and the only place boundary conditions enter Noether's theorem → [[P3 Noether's Procedure#^p3-6|P3, step 6]].
>
> **What the derivation shows**
> - Conservation is local first: no charge is created or destroyed anywhere; global conservation needs the fall-off.
> - Nothing beyond $\partial_\mu j^\mu = 0$ was used: this is the same argument as for electric charge ([[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-6|REL Theorem §B4.2.6]]), here for any symmetry.
> - Used next: energy and momentum ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|Theorem §C1b.7.6]]), improvement terms ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]]).

^der-c1b-6-1

*Uses:* [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.6 Conserved Charges and Internal Symmetries#^def-c1b-6-1|Def. §C1b.6.1]], [[§C1b.6 Conserved Charges and Internal Symmetries#^def-c1b-6-2|Def. §C1b.6.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|452 Thm. §32.1]]

*Procedure:* [[P3 Noether's Procedure#^p3-6|P3, step 6]]

> [!caution] Caution: The sign in the slides' continuity equation
> Lecture 3 (slide "Noether's Charge") writes $\partial_\mu j^\mu = \partial_0j^0 - \vec\nabla\cdot\vec j$ and $dQ/dt = +\int d^3x\,\vec\nabla\cdot\vec j$. With $j^\mu = (\rho, \mathbf j)$ the sign is $+$, $\partial_\mu j^\mu = \partial_t\rho + \nabla\cdot\mathbf j$, so $dQ/dt = -\oint\mathbf j\cdot d\mathbf S$; the conclusion, no flux at infinity and $dQ/dt = 0$, is unaffected.

^cau-c1b-6-1

> [!theorem] Theorem §C1b.6.2: Improvement Terms
> Let $B^{\nu\mu} = -B^{\mu\nu}$ be any twice-differentiable antisymmetric tensor built from the fields. Then
> 1. $\partial_\mu\partial_\nu B^{\nu\mu} = 0$ identically, so $j'^\mu = j^\mu + \partial_\nu B^{\nu\mu}$ is conserved whenever $j^\mu$ is;
> 2. if $B^{i0}$ falls off faster than $1/r^2$ at spatial infinity, $j'$ and $j$ have the same charge.
>
> A Noether current is therefore determined only up to such **improvement terms**.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Caution "What the theorem does and does not say" · PHY 513 Problem Set 2, Problem 4(d) (statement)*

^thm-c1b-6-2

> [!derivation]- Derivation
> **1. Symmetric against antisymmetric.** Partial derivatives of a $C^2$ function commute, so $\partial_\mu\partial_\nu$ is symmetric in $\mu\nu$. Relabel the dummies $\mu \leftrightarrow \nu$, then use both symmetries: $\partial_\mu\partial_\nu B^{\nu\mu} = \partial_\nu\partial_\mu B^{\mu\nu} = \partial_\mu\partial_\nu B^{\mu\nu} = -\partial_\mu\partial_\nu B^{\nu\mu}$, so the expression is zero ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]]). No equation of motion is used.
>
> **2. Conservation.** $\partial_\mu j'^\mu = \partial_\mu j^\mu + \partial_\mu\partial_\nu B^{\nu\mu} = \partial_\mu j^\mu$.
>
> **3. The charge density changes by a divergence.** $j'^0 - j^0 = \partial_\nu B^{\nu0} = \partial_0B^{00} + \partial_iB^{i0}$, and $B^{00} = -B^{00} = 0$. With $b^i \equiv B^{i0}$, $j'^0 - j^0 = \nabla\cdot\mathbf b$.
>
> **4. Its integral is a surface term.** $\int_{B_R}d^3x\,\nabla\cdot\mathbf b = \oint_{S_R}\mathbf b\cdot d\mathbf S$ ([[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|452 Thm. §32.1]]), which tends to $0$ as $R \to \infty$ under the fall-off, as in step 5 of [[§C1b.6 Conserved Charges and Internal Symmetries#^der-c1b-6-1|Derivation §C1b.6.1]]. So $Q' = Q$.
>
> **What the derivation shows**
> - Part 1 is identically true; part 2 needs the fall-off.
> - ⚑ By-product: this freedom is what symmetrizes the energy–momentum tensor → [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|Theorem §C1b.8.4]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]]. With an extra label, $B^{\lambda\mu}{}_\nu$ antisymmetric in $\lambda\mu$, the same argument holds for each $\nu$.

^der-c1b-6-2

*Uses:* [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|452 Thm. §32.1]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]

> [!caution] Caution: What the theorem does and does not say
> - The current is conserved **on solutions**; off shell, $\partial_\mu j^\mu$ is minus the Euler–Lagrange expression times $\Delta\phi$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]).
> - The charge is conserved **subject to boundary conditions** ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]).
> - The current is **not unique**: improvement terms change it without changing $\partial_\mu j^\mu$ or $Q$ ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]]). Likewise $\delta\mathcal L = 0$ says only $\partial_\mu\mathcal J^\mu = 0$; taking $\mathcal J = 0$ is a choice, the natural one because $\mathcal J$ is a name for whatever makes $\delta\mathcal L$ a total derivative. Any other admissible $\mathcal J$ shifts $j^\mu$ by an identically conserved vector and gives the same conservation law.
> - The theorem needs a Lagrangian and a continuous family; discrete symmetries (parity, charge conjugation) give no current (QFT C9, planned).

^cau-c1b-6-2

> [!remark]- ★ Remark: Every identically conserved local current is an improvement term
> A vector built locally from the fields (the fields and finitely many derivatives at a point) that is conserved for every field configuration and vanishes when the fields do has the form $\partial_\nu B^{\nu\mu}$ with $B$ antisymmetric: the algebraic Poincaré lemma, beyond this course and not proved here. Consequently the ambiguity of $\mathcal J$ when $\delta\mathcal L = 0$ is an improvement term and leaves $Q$ unchanged for fields that fall off at infinity. What Noether's theorem determines is the class of $j^\mu$ modulo identically conserved currents, and the physics lives in that class.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Caution "What the theorem does and does not say" (second paragraph)*

^rem-c1b-6-1

## Internal symmetries

In an internal symmetry the point is not moved; only the values of the fields change. Step 1 is a direct expansion, and step 3 typically gives outcome (i), $\mathcal J = 0$.

> [!example] Example §C1b.6.1: Shift Symmetry of the Massless Field
> $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi$, transformation $\phi \to \phi + \alpha$.
> 1. $\Delta\phi = 1$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]): the field changes by the same amount everywhere.
> 2. Substitute: $\mathcal L(\phi + \alpha) = \frac12\partial_\mu(\phi + \alpha)\,\partial^\mu(\phi + \alpha) = \frac12\partial_\mu\phi\,\partial^\mu\phi$, since $\partial_\mu\alpha = 0$. So $\delta\mathcal L = 0$.
> 3. Outcome (i): $\mathcal J^\mu = 0$.
> 4. With $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]), $j^\mu = \partial^\mu\phi\cdot1 = \partial^\mu\phi$.
> 5. For any $\phi$, $\partial_\mu j^\mu = \partial^2\phi$. The Euler–Lagrange expression is $\partial\mathcal L/\partial\phi - \partial_\mu(\partial^\mu\phi) = 0 - \partial^2\phi$, so $\partial_\mu j^\mu = -\mathrm{EL}\cdot1$, as the off-shell identity requires; it vanishes exactly on solutions. Conservation of this current *is* the massless equation of motion. (Formula 1 of the proof gave $\delta\mathcal L = 0$; Formula 2 gives $\alpha(-\partial^2\phi) + \alpha\,\partial_\mu\partial^\mu\phi = 0$ for every $\phi$: the two agree.)
> 6. $Q = \int d^3x\,j^0 = \int d^3x\,\partial^0\phi = \int d^3x\,\dot\phi$.
>
> **With a mass**, $\mathcal L = \frac12(\partial\phi)^2 - \frac12m^2\phi^2$, step 2 gives $-\frac12m^2(\phi + \alpha)^2 + \frac12m^2\phi^2 = -\alpha m^2\phi + O(\alpha^2)$, so $\delta\mathcal L = -\alpha m^2\phi$. This is outcome (iii). Suppose $-m^2\phi = \partial_\mu\mathcal J^\mu$ for every configuration, with $\mathcal J$ built locally from the fields, their derivatives and $x$. Take a bump configuration $\phi \ge 0$, $\phi \not\equiv 0$, supported inside a ball $B$, and integrate over $B$: by the divergence theorem the right side is the flux of $\mathcal J$ through $\partial B$, where the field and its derivatives vanish, so it equals the flux for the configuration $\phi = 0$, which is $\int_B(-m^2\cdot0) = 0$; but the left side is $-m^2\int_B\phi < 0$. No symmetry, and indeed $\partial_\mu\partial^\mu\phi = -m^2\phi \ne 0$ on shell: no conservation. This is [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]] with $X = \delta\mathcal L/\alpha = -m^2\phi$: on shell the divergence of the would-be current $\partial^\mu\phi$ equals $\delta\mathcal L/\alpha$, and the Klein–Gordon equation read as $\partial_\mu(\partial^\mu\phi) = -m^2\phi$ is that statement. The example shows both directions, symmetry with conservation and no symmetry without it.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 1 · Lecture 3, Example 1 · PS §2.2, p. 18*

^ex-c1b-6-1

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, steps 1–6]]

> [!theorem] Theorem §C1b.6.3: The U(1) Current of the Complex Scalar Field
> For $\mathcal L = \partial_\mu\phi^*\partial^\mu\phi - m^2\phi^*\phi - V(\phi^*\phi)$, with $V$ any smooth function, the global phase rotation $\phi \to e^{i\alpha}\phi$, $\phi^* \to e^{-i\alpha}\phi^*$ is a symmetry with $\mathcal J = 0$, and its Noether current
>
> $$
> j^\mu = i\bigl(\phi\,\partial^\mu\phi^* - \phi^*\partial^\mu\phi\bigr)
> $$
>
> is conserved on solutions, for every $m$ and $V$. Its charge $Q = \int d^3x\,j^0 = i\int d^3x\,(\phi\dot\phi^{\ast} - \phi^{\ast}\dot\phi)$ is the **number charge**; a positive-frequency solution has $j^0 < 0$ in this sign convention.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 2, eq. (U1current) · PS §2.2, eqs. (2.14)–(2.16) · PHY 513 Problem Set 2, Problem 3(c)–(d), with the course solution · Lecture 3, Example 2 · Yu §1.7.4, eqs. (1.253)–(1.263)*

^thm-c1b-6-3

> [!derivation]- Derivation
> The steps of [[P3 Noether's Procedure]]. Here $N = 2$ fields ($\phi$ and $\phi^*$, independent, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]) and $\dim G = 1$: one parameter moves both.
>
> **1. Generators.** $\Delta\phi = i\phi$, $\Delta\phi^{\ast} = -i\phi^{\ast}$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]). The generator depends on the field itself.
>
> **2. Substitute.** $\alpha$ is constant, so $\partial_\mu(e^{i\alpha}\phi) = e^{i\alpha}\partial_\mu\phi$ and $\partial^\mu(e^{-i\alpha}\phi^{\ast}) = e^{-i\alpha}\partial^\mu\phi^{\ast}$. Term by term: the kinetic term becomes $e^{-i\alpha}e^{i\alpha}\partial_\mu\phi^{\ast}\partial^\mu\phi = \partial_\mu\phi^{\ast}\partial^\mu\phi$; the mass term $e^{-i\alpha}e^{i\alpha}m^2\phi^{\ast}\phi = m^2\phi^{\ast}\phi$; the argument of $V$ becomes $e^{-i\alpha}\phi^{\ast}\,e^{i\alpha}\phi = \phi^{\ast}\phi$. So $\mathcal L$ is unchanged to all orders, and $\delta\mathcal L = 0$: every term pairs one $\phi$ with one $\phi^{\ast}$.
>
> **3. Test.** Outcome (i): $\mathcal J^\mu = 0$.
>
> **4. Current.** $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi^{\ast}$ and $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = \partial^\mu\phi$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]). One current with two terms:
>
> $$
> j^\mu = \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\Delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi^*)}\,\Delta\phi^* = \partial^\mu\phi^*\,(i\phi) + \partial^\mu\phi\,(-i\phi^*) = i\bigl(\phi\,\partial^\mu\phi^* - \phi^*\partial^\mu\phi\bigr) .
> $$
>
> **5. Check, off shell.** By the product rule,
>
> $$
> \partial_\mu j^\mu = i\bigl(\partial_\mu\phi\,\partial^\mu\phi^* + \phi\,\partial^2\phi^* - \partial_\mu\phi^*\partial^\mu\phi - \phi^*\partial^2\phi\bigr) .
> $$
>
> The cross terms are equal, $\partial_\mu\phi\,\partial^\mu\phi^* = g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi^* = \partial_\nu\phi^*\partial^\nu\phi$ (symmetric metric), and cancel identically, leaving $i(\phi\,\partial^2\phi^* - \phi^*\partial^2\phi)$. The Euler–Lagrange expressions are $\mathrm{EL}_{\phi^*} = \partial\mathcal L/\partial\phi^* - \partial_\mu\partial^\mu\phi = -(m^2 + V')\phi - \partial^2\phi$ and $\mathrm{EL}_\phi = -(m^2 + V')\phi^* - \partial^2\phi^*$, with $V' = dV/d(\phi^*\phi)$. Substitute $\partial^2\phi = -\mathrm{EL}_{\phi^*} - (m^2 + V')\phi$ and $\partial^2\phi^* = -\mathrm{EL}_\phi - (m^2 + V')\phi^*$:
>
> $$
> i(\phi\,\partial^2\phi^* - \phi^*\partial^2\phi) = i\bigl(-\phi\,\mathrm{EL}_\phi + \phi^*\mathrm{EL}_{\phi^*}\bigr) - i(m^2 + V')(\phi\phi^* - \phi^*\phi) = -\bigl[\mathrm{EL}_\phi\,(i\phi) + \mathrm{EL}_{\phi^*}(-i\phi^*)\bigr] ,
> $$
>
> the off-shell identity of [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]; the potential terms cancel because $\phi\phi^* = \phi^*\phi$. On shell both $\mathrm{EL}$ vanish and $\partial_\mu j^\mu = 0$, with a mass and with $V$.
>
> **6. Charge.** $\partial^0 = \partial_t$, so $j^0 = i(\phi\dot\phi^{\ast} - \phi^{\ast}\dot\phi)$. ⚑ By-product: for a positive-frequency solution $\phi = A\,e^{-iEt + i\mathbf p\cdot\mathbf x}$, $E > 0$, one has $\dot\phi = -iE\phi$, $\dot\phi^{\ast} = iE\phi^{\ast}$, and $j^0 = i(iE + iE)\lvert A\rvert^2 = -2E\lvert A\rvert^2 < 0$ → [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|Caution: Sign and normalization of the U(1) current]].
>
> **What the derivation shows**
> - Invariance is exact, not just first order, because $\phi$ and $\phi^*$ appear in pairs; neither the mass nor $V(\phi^*\phi)$ breaks it (the course solution of Problem Set 2, Problem 3(c), adds: only for constant $\alpha$).
> - The equations of motion enter only in step 5.
> - Used next: the quantum charge [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]] is $-\frac12$ times this charge, normal ordered.

^der-c1b-6-3

*Uses:* [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, steps 1–6]], [[P1 Canonical Quantization#^p1-3|P1, step 3]]

> [!caution] Caution: Sign and normalization of the U(1) current
> The overall sign of $j^\mu$ is the sign of $\alpha$ ([[§C1b.5 Noether's Theorem#^rem-c1b-5-2|Remark: The sign of a parameter is a convention]]). With $\Delta\phi = +i\phi$, as here and in PS eq. (2.16), a positive-frequency solution has $j^0 = -2E\lvert A\rvert^2 < 0$, and after quantization, with normal ordering $:\!\;\!:$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), $\int d^3x\,:\!\hat j^0\!: = \hat N_b - \hat N_a$, particles counted negative. Lecture 3 and the board write $j^\mu = -i\bigl((\partial^\mu\phi^*)\phi - (\partial^\mu\phi)\phi^*\bigr)$, the opposite sign, which gives $\hat N_a - \hat N_b$. Yu's $J^\mu = iq\,\phi^*\overleftrightarrow{\partial^\mu}\phi$ (eq. (1.262)) is $-q$ times the current here. The quantum charge used in this subject is $\hat Q = \frac12(\hat N_a - \hat N_b) = -\frac12\int d^3x\,:\!\hat j^0\!:$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]]); the full dictionary is [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]], and [[Larsen PHY 513]] records the choice. Only the ratio $-1$ of particle and antiparticle charges is physical.

^cau-c1b-6-3

> [!remark] Remark: Global, internal, and what a local phase would need
> The phases $e^{i\alpha}$ form the group U(1) $\cong$ SO(2) (Yu eq. (1.255)); in real components the phase is a rotation of the pair $(\phi_1, \phi_2)$ ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|Example §C1b.6.2]]), and the current $\phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$ is the field-space analogue of $xp_y - yp_x$. The symmetry is **internal** (the point is fixed, $\delta x = 0$) and **global** ($\alpha$ the same everywhere). For $\alpha(x)$, step 2 fails: $\partial_\mu(e^{i\alpha(x)}\phi) = e^{i\alpha}(\partial_\mu\phi + i\,\partial_\mu\alpha\,\phi)$, so the kinetic term changes by terms in $\partial_\mu\alpha$, and restoring invariance needs a gauge field coupled to $j^\mu$ (QFT C8, planned; for the wave function, minimal coupling [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^pr-c13-1-3|QM Principle §C13.1.3]]). Several species of charges $q_n$ have $\Delta\phi_n = iq_n\phi_n$, and each term of the current carries its $q_n$. If the field is electrically charged, $Q$ times the unit charge is the electric charge, and charge conservation is Noether's theorem for this phase symmetry.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 2 (closing paragraph) · Yu §1.7.4*

^rem-c1b-6-2

> [!example] Example §C1b.6.2: Two Real Fields: One Rotation or Two Shifts
> Take two real fields with $\mathcal L = \frac12(\partial\phi_1)^2 + \frac12(\partial\phi_2)^2 - \frac12m^2(\phi_1^2 + \phi_2^2)$, which is the complex $\mathcal L$ with $V = 0$ written in $\phi = (\phi_1 + i\phi_2)/\sqrt2$: $\partial_\mu\phi^*\partial^\mu\phi = \frac12(\partial_\mu\phi_1 - i\partial_\mu\phi_2)(\partial^\mu\phi_1 + i\partial^\mu\phi_2) = \frac12(\partial\phi_1)^2 + \frac12(\partial\phi_2)^2$, the cross terms cancelling, and $m^2\phi^*\phi = \frac12m^2(\phi_1^2 + \phi_2^2)$.
>
> **(a) One rotation.** $\Delta\phi_1 = -\phi_2$, $\Delta\phi_2 = \phi_1$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]). Step 2: the kinetic terms change by $\alpha(\partial\phi_1\cdot\partial(-\phi_2) + \partial\phi_2\cdot\partial\phi_1) = 0$, the mass term by $-m^2\alpha(\phi_1(-\phi_2) + \phi_2\phi_1) = 0$: $\mathcal J = 0$. Step 4, one current from two fields:
>
> $$
> j^\mu = \partial^\mu\phi_1\,(-\phi_2) + \partial^\mu\phi_2\,\phi_1 = \phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1 .
> $$
>
> It is the U(1) current of [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]]: $\phi\,\partial\phi^* = \frac12\bigl[\phi_1\partial\phi_1 + \phi_2\partial\phi_2 + i(\phi_2\partial\phi_1 - \phi_1\partial\phi_2)\bigr]$ and $\phi^*\partial\phi = \frac12\bigl[\phi_1\partial\phi_1 + \phi_2\partial\phi_2 + i(\phi_1\partial\phi_2 - \phi_2\partial\phi_1)\bigr]$, so $i(\phi\,\partial\phi^* - \phi^*\partial\phi) = i\cdot i(\phi_2\partial\phi_1 - \phi_1\partial\phi_2) = \phi_1\partial\phi_2 - \phi_2\partial\phi_1$.
>
> **(b) Two shifts ($m = 0$).** $\Delta_k\phi_l = \delta_{kl}$, $\dim G = 2$; each shift leaves the massless $\mathcal L$ invariant as in [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|Example §C1b.6.1]], and there are two single-term currents, $j^\mu_1 = \partial^\mu\phi_1$ and $j^\mu_2 = \partial^\mu\phi_2$.
>
> The same fields, different families: the number of currents follows the number of parameters, not of fields. For $m = 0$ both families are symmetries, three currents in all; for $m \ne 0$ only the rotation survives.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, "Computing Δφ (step 1)" and Example 2 (closing paragraph)*

^ex-c1b-6-2

> [!example] Example §C1b.6.3: A Mass Splitting Breaks the Phase Symmetry
> Add to the free complex field ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]]) a term that is not invariant under phases, with a real constant $\lambda$ of mass dimension 2 (unrelated to a quartic coupling):
>
> $$
> \mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi - \frac{\lambda}{2}\bigl(\phi^2 + \phi^{\ast 2}\bigr) .
> $$
>
> 1. **What the term is.** With $\phi = (\phi_1 + i\phi_2)/\sqrt2$: $\phi^2 = \frac12(\phi_1^2 - \phi_2^2 + 2i\phi_1\phi_2)$ and $\phi^{\ast 2} = \frac12(\phi_1^2 - \phi_2^2 - 2i\phi_1\phi_2)$, so $\phi^2 + \phi^{\ast 2} = \phi_1^2 - \phi_2^2$. With the kinetic and mass terms of [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|Example §C1b.6.2]], $\mathcal L = \frac12(\partial\phi_1)^2 + \frac12(\partial\phi_2)^2 - \frac12(m^2 + \lambda)\phi_1^2 - \frac12(m^2 - \lambda)\phi_2^2$: two real fields of masses $m_1^2 = m^2 + \lambda$, $m_2^2 = m^2 - \lambda$ (both real for $\lvert\lambda\rvert < m^2$). The extra term is a mass splitting.
> 2. **Step 2, Route 1.** $\Delta\phi = i\phi$, $\Delta\phi^{\ast} = -i\phi^{\ast}$; the kinetic and mass terms are unchanged ([[§C1b.5 Noether's Theorem#^ex-c1b-5-1|Example §C1b.5.1]]). In the new term $(e^{i\alpha}\phi)^2 = e^{2i\alpha}\phi^2 = \phi^2 + 2i\alpha\phi^2 + O(\alpha^2)$ and $(e^{-i\alpha}\phi^{\ast})^2 = \phi^{\ast 2} - 2i\alpha\phi^{\ast 2} + O(\alpha^2)$, so
>
> $$
> \delta\mathcal L = -\frac{\lambda}{2}\bigl(2i\alpha\phi^2 - 2i\alpha\phi^{\ast 2}\bigr) = -i\alpha\lambda\bigl(\phi^2 - \phi^{\ast 2}\bigr) .
> $$
>
> 3. **Step 2, Route 2.** The new term has $\partial/\partial\phi = -\lambda\phi$ and $\partial/\partial\phi^{\ast} = -\lambda\phi^{\ast}$ and no derivatives of the fields, so it adds $(-\lambda\phi)(i\phi) + (-\lambda\phi^{\ast})(-i\phi^{\ast}) = -i\lambda(\phi^2 - \phi^{\ast 2})$ to the four terms of [[§C1b.5 Noether's Theorem#^ex-c1b-5-1|Example §C1b.5.1]], which cancel as there (with $V = 0$). Times $\alpha$: the same $\delta\mathcal L$.
> 4. **Step 3: not a divergence.** $\phi^2 - \phi^{\ast 2} = 2i\phi_1\phi_2$ (step 1), so $X \equiv \delta\mathcal L/\alpha = -i\lambda\cdot 2i\phi_1\phi_2 = 2\lambda\phi_1\phi_2$. Take $\phi_1 = \phi_2 = f$ with $f \ge 0$, $f \not\equiv 0$, supported inside a ball $B$. A divergence of a local $\mathcal J$ integrates over $B$ to the flux through $\partial B$, where the fields vanish, which equals the flux for the zero configuration, $0$ (the argument of [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|Example §C1b.6.1]]); but $\int_Bd^4x\,2\lambda f^2 \ne 0$ for $\lambda \ne 0$. Outcome (iii): no symmetry.
> 5. **The would-be current and its divergence.** The kinetic term is unchanged, so $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi^{\ast}$, $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = \partial^\mu\phi$, and $j^\mu = i(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi) = \phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$ ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|Example §C1b.6.2]]). [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]] with $\mathcal J = 0$: on shell
>
> $$
> \partial_\mu j^\mu = X = -i\lambda\bigl(\phi^2 - \phi^{\ast 2}\bigr) = 2\lambda\,\phi_1\phi_2 .
> $$
>
> 6. **Cross-check, directly.** The field equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]) are $\partial_\mu\partial^\mu\phi = \partial\mathcal L/\partial\phi^{\ast} = -m^2\phi - \lambda\phi^{\ast}$ and the conjugate $\partial^2\phi^{\ast} = -m^2\phi^{\ast} - \lambda\phi$. For any field, $\partial_\mu j^\mu = i(\phi\,\partial^2\phi^{\ast} - \phi^{\ast}\partial^2\phi)$, the cross terms cancelling (step 5 of [[§C1b.6 Conserved Charges and Internal Symmetries#^der-c1b-6-3|Derivation §C1b.6.3]]). Substituting: $i\bigl[\phi(-m^2\phi^{\ast} - \lambda\phi) - \phi^{\ast}(-m^2\phi - \lambda\phi^{\ast})\bigr] = i(-\lambda\phi^2 + \lambda\phi^{\ast 2}) = -i\lambda(\phi^2 - \phi^{\ast 2})$, the mass terms cancelling. In real components, $\partial^2\phi_1 = -m_1^2\phi_1$, $\partial^2\phi_2 = -m_2^2\phi_2$ and $\partial_\mu j^\mu = \phi_1\partial^2\phi_2 - \phi_2\partial^2\phi_1 = (m_1^2 - m_2^2)\,\phi_1\phi_2 = 2\lambda\,\phi_1\phi_2$. Both agree with step 5: the rotation of $(\phi_1, \phi_2)$ is broken by the difference of the two masses.
> 7. **Charge.** $dQ/dt = \int d^3x\,2\lambda\,\phi_1\phi_2$ for fields falling off at infinity (step 7 of [[§C1b.5 Noether's Theorem#^der-c1b-5-5|Derivation §C1b.5.5]]): the number charge is not conserved, and at $\lambda = 0$ symmetry and conservation return together.
>
> *Source: written here as an illustration of [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]; the U(1) current from the user's PHY 513 notes, Ch. 3 §3.5, Example 2 · PS §2.2, eq. (2.14)*

^ex-c1b-6-3

*Procedure:* [[P3 Noether's Procedure#^p3-3|P3, steps 1–5]]

> [!remark]- Connections
> - Every current here comes from [[§C1b.5 Noether's Theorem|§C1b.5]]: the definitions of δ and Δ, the two routes to δℒ and the symmetry test ([[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]]), Noether's theorem itself, and, for the broken examples, the divergence of the would-be current ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]).
> - The shift-symmetric massless field is the field version of a cyclic coordinate ([[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-1|CM Theorem §B6.4.1]]): $\mathcal L$ depends on $\phi$ only through $\partial\phi$, and the conserved charge $\int d^3x\,\dot\phi = \int d^3x\,\pi$ is the total conjugate momentum ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]).
> - In Hamiltonian form the charge generates its own symmetry through Poisson brackets ([[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^rem-b6-4-6|CM Remark: Noether in Hamiltonian form]], [[§B8.1 Poisson Brackets#^thm-b8-1-5|CM Theorem §B8.1.5]]); after quantization commutators take over: the U(1) charge counts quanta with $[\hat Q, \hat a^\dagger] = \frac12\hat a^\dagger$ ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]]), the way a conserved generator commutes with $\hat H$ in quantum mechanics ([[§C8.1★ Symmetries, Conservation Laws and Degeneracies#^thm-c8-1-2|QM Theorem §C8.1.2]]).
> - The indefinite Klein–Gordon density that wrecked the probability interpretation ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-1|QM Theorem §C13.1.1]]) is this U(1) charge density; its negative values become antiparticles after quantization ([[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-3|§C2a.5, Remark: Charge, not probability]]).
> - Electric charge conservation, the template of every continuity equation ([[§B9.1 Charge, Energy and Poynting's Theorem#^rem-b9-1-1|EM Remark: Charge conservation as the template]], [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-6|REL Theorem §B4.2.6]]), is Theorem §C1b.6.1 for the phase symmetry of a charged field; making the phase local requires the gauge field (QFT C8, planned).
> - Improvement terms ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]]) are what makes the electromagnetic energy–momentum tensor symmetric and gauge invariant ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]]), and Belinfante's construction ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|Theorem §C1b.8.4]]) does it for every field.
> - The quantum charges are these classical charges with operator fields inserted and normal ordered ([[P1 Canonical Quantization#^p1-7|P1, steps 7–8]]; [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]]).
> - Electromagnetism level C: making the phase local, classically — minimal coupling turns the global U(1) of a charged field into a gauge symmetry, the coupling is gauge invariant if and only if charge is conserved, and gauge invariance makes the field equations dependent (the Noether-identity form) — [[§C1.3 Gauge Symmetry and Charge Conservation#^thm-c1-3-4|EM Theorem §C1.3.4]], [[§C1.3 Gauge Symmetry and Charge Conservation#^thm-c1-3-1|EM Theorem §C1.3.1]], [[§C1.3 Gauge Symmetry and Charge Conservation#^thm-c1-3-2|EM Theorem §C1.3.2]].
> - Math: the chain rule [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]; the divergence theorem [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^thm-32-1|452 Thm. §32.1]] and in $\mathbb R^n$ [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], whose continuity-equation form is [[§29 Conservation of Mass and Laplace's Equation#^thm-29-1|452 Thm. §29.1]]; differentiation under the integral [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]].
