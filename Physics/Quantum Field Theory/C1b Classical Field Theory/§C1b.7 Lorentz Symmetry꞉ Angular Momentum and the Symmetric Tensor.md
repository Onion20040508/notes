---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum]] · ↑ [[· C1b Classical Field Theory]] · [[§C2a.1 Canonical Quantization of Fields]] →

*Sources: the user's PHY 513 notes, Ch. 3 §3.5 (The general form; Examples II; Spacetime symmetries in general; Belinfante; Correspondence with Yu) · PHY 513 Lecture 3 (Larsen), Part C; Problem Set 2, Problem 4 (= PS Problem 2.1), with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2 · Yu Zhao-Huan, 量子场论讲义, §§1.7.1–1.7.3 and Exercise 1.10 · the user's pre-course notes, §1.7.*

What do Lorentz transformations conserve in a field theory, and why does the energy–momentum tensor need repairing? Noether's theorem in the form that lets the point move, and the energy–momentum tensor with its charges $P^\mu$, are [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum|§C1b.6]] ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]]); the infinitesimal field laws, with their orbital and spin parts, are [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]], and the Lorentz parameters [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]]. This section runs the general form for Lorentz transformations: the Lorentz current with its orbital and spin parts, the angular-momentum and boost charges, the antisymmetric part of $T^{\mu\nu}$, the uniformly moving centre of energy, and Belinfante's symmetric tensor, which the electromagnetic field (Problem Set 2) needs. Every computation runs [[P3 Noether's Procedure]].

## Lorentz transformations: the angular-momentum tensor

> [!theorem] Theorem §C1b.7.1: The Lorentz Current
> Let $\mathcal L$ be a Lorentz scalar built from fields with the transformation law $\phi'_a(x') = D_a{}^b(\Lambda)\phi_b(x)$, $D = 1 + \frac12\omega_{\mu\nu}S^{\mu\nu}$ ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]). Under $\Lambda = 1 + \omega$, $\omega_{\mu\nu} = -\omega_{\nu\mu}$, the Noether current is $j^\mu = \frac12\omega_{\nu\rho}\mathcal M^{\mu\nu\rho}$ with
>
> $$
> \mathcal M^{\mu\nu\rho} = \underbrace{x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}}_{\text{orbital}} + \underbrace{\mathcal S^{\mu\nu\rho}}_{\text{spin}}, \qquad \mathcal S^{\mu\nu\rho} \equiv \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\,(S^{\nu\rho})_a{}^b\phi_b ,
> $$
>
> antisymmetric in $\nu\rho$, and $\partial_\mu\mathcal M^{\mu\nu\rho} = 0$ on shell: six conserved currents. For a scalar field $S^{\nu\rho} = 0$ and $\mathcal M$ is purely orbital.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 4, eq. (Mcurrent), and "Lorentz transformations, all fields at once", eq. (Mgeneral) · Yu §1.7.3, eqs. (1.229)–(1.239)*

^thm-c1b-7-1

> [!derivation]- Derivation
> $\pi^\mu_a \equiv \partial\mathcal L/\partial(\partial_\mu\phi_a)$.
>
> **1. Symmetry.** A Lorentz scalar satisfies $\mathcal L'(x') = \mathcal L(x)$, and $d^4x' = d^4x$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-2|Theorem §C1b.6.2]]), so [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-1|Def. §C1b.6.1]] holds for every region.
>
> **2. Displacement.** $x'^\mu = \Lambda^\mu{}_\nu x^\nu = x^\mu + \omega^\mu{}_\nu x^\nu$: $\delta x^\mu = \omega^\mu{}_\nu x^\nu$.
>
> **3. Total change of the field.** $\delta\phi_a = \phi'_a(x') - \phi_a(x) = (D - 1)_a{}^b\phi_b = \frac12\omega_{\nu\rho}(S^{\nu\rho})_a{}^b\phi_b$.
>
> **4. Fixed-argument change.** [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]]:
>
> $$
> \bar\delta\phi_a = \underbrace{\tfrac12\omega_{\nu\rho}(S^{\nu\rho})_a{}^b\phi_b}_{\text{the components rotated}} \;\underbrace{-\,(\partial_\sigma\phi_a)\,\omega^\sigma{}_\rho x^\rho}_{\text{the point moved}} .
> $$
>
> **5. Insert into the general current.** [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]] gives $j^\mu = \sum_a\pi^\mu_a\bar\delta\phi_a + \mathcal L\,\omega^\mu{}_\rho x^\rho$. The spin piece is $\frac12\omega_{\nu\rho}\mathcal S^{\mu\nu\rho}$. In the rest write $\omega^\mu{}_\rho x^\rho = \delta^\mu{}_\sigma\omega^\sigma{}_\rho x^\rho$:
>
> $$
> -\sum_a\pi^\mu_a(\partial_\sigma\phi_a)\,\omega^\sigma{}_\rho x^\rho + \delta^\mu{}_\sigma\mathcal L\,\omega^\sigma{}_\rho x^\rho = -T^\mu{}_\sigma\,\omega^\sigma{}_\rho x^\rho ,
> $$
>
> the energy–momentum tensor appearing by itself ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]]).
>
> **6. Move the metric.** $T^\mu{}_\sigma\omega^\sigma{}_\rho = T^{\mu\alpha}g_{\alpha\sigma}\omega^\sigma{}_\rho = T^{\mu\alpha}\omega_{\alpha\rho}$ (Yu eq. (1.235)); rename $\alpha \to \nu$: the orbital piece is $-T^{\mu\nu}\omega_{\nu\rho}x^\rho$.
>
> **7. Antisymmetrize.** Split into halves and relabel $\nu \leftrightarrow \rho$ in the second: $-\frac12T^{\mu\rho}\omega_{\rho\nu}x^\nu = +\frac12\omega_{\nu\rho}x^\nu T^{\mu\rho}$. Hence $-T^{\mu\nu}\omega_{\nu\rho}x^\rho = \frac12\omega_{\nu\rho}(x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu})$. ⚑ By-product: the $\frac12$ compensates the double counting of each antisymmetric pair, as in step 6 of [[§C1b.5 Noether's Theorem#^der-c1b-5-1|Derivation §C1b.5.1]].
>
> **8. Total.** $j^\mu = \frac12\omega_{\nu\rho}\bigl(x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu} + \mathcal S^{\mu\nu\rho}\bigr) = \frac12\omega_{\nu\rho}\mathcal M^{\mu\nu\rho}$. The orbital part is antisymmetric in $\nu\rho$ by inspection, the spin part because $S^{\nu\rho} = -S^{\rho\nu}$ ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]).
>
> **9. Six currents.** $\partial_\mu j^\mu = 0$ on shell for every antisymmetric $\omega$. Choose $\omega_{\nu\rho} = -\omega_{\rho\nu} = 1$ for one pair $\nu < \rho$ and all other components zero: $\frac12\omega_{\alpha\beta}\mathcal M^{\mu\alpha\beta} = \frac12(\mathcal M^{\mu\nu\rho} - \mathcal M^{\mu\rho\nu}) = \mathcal M^{\mu\nu\rho}$. So $\partial_\mu\mathcal M^{\mu\nu\rho} = 0$ for each of the six pairs.
>
> **What the derivation shows**
> - The energy–momentum tensor appears automatically in the Lorentz current (step 5); the Lorentz charges are its first moments plus spin.
> - The spin part comes only from the field's components rotating into each other (step 3).
> - Used next: [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-7-1|Def. §C1b.7.1]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]].

^der-c1b-7-1

> [!derivation]- Derivation (second route: the lecture's form, real scalar field)
> For $\mathcal L = \frac12(\partial\phi)^2 - \frac12m^2\phi^2$, run [[P3 Noether's Procedure]] with fixed-argument variations.
>
> **1. Generator.** $\delta\phi = -\omega^\sigma{}_\rho x^\rho\partial_\sigma\phi = \frac12\omega_{\nu\rho}\Delta^{\nu\rho}\phi$, $\Delta^{\nu\rho}\phi = x^\nu\partial^\rho\phi - x^\rho\partial^\nu\phi$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]; [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]).
>
> **2. Substitute.** $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi) = -\omega^\sigma{}_\mu\partial_\sigma\phi - \omega^\sigma{}_\rho x^\rho\partial_\mu\partial_\sigma\phi$, the first term from $\partial_\mu x^\rho = \delta^\rho{}_\mu$. By the chain rule,
>
> $$
> \delta\mathcal L = -\omega^\sigma{}_\rho x^\rho\Bigl[\frac{\partial\mathcal L}{\partial\phi}\partial_\sigma\phi + \partial^\mu\phi\,\partial_\sigma\partial_\mu\phi\Bigr] - \omega^\sigma{}_\mu\,\partial^\mu\phi\,\partial_\sigma\phi .
> $$
>
> The bracket is $\partial_\sigma\mathcal L$ (step 3 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-5|Derivation §C1b.6.5]]). The last term is $\omega_{\sigma\mu}\partial^\mu\phi\,\partial^\sigma\phi = 0$, antisymmetric against symmetric ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]]). ⚑ By-product: for a field with an index, $\partial\mathcal L/\partial(\partial_\mu\phi_a)$ is not $\propto\partial^\mu\phi_a$, this term survives, and it is what the spin part accounts for.
>
> **3. Test.** $\delta\mathcal L = -\omega^\sigma{}_\rho x^\rho\partial_\sigma\mathcal L = -\partial_\sigma(\omega^\sigma{}_\rho x^\rho\mathcal L) + \omega^\sigma{}_\sigma\mathcal L = -\partial_\sigma(\omega^\sigma{}_\rho x^\rho\mathcal L)$, using $\omega^\sigma{}_\sigma = 0$. To factor $\frac12\omega_{\nu\rho}$: with $\mathcal J^{\sigma\nu\rho} \equiv (x^\nu g^{\sigma\rho} - x^\rho g^{\sigma\nu})\mathcal L$, $\frac12\omega_{\nu\rho}\mathcal J^{\sigma\nu\rho} = \frac12(\omega_\nu{}^\sigma x^\nu - \omega^\sigma{}_\rho x^\rho)\mathcal L = -\omega^\sigma{}_\rho x^\rho\mathcal L$, since $\omega_\nu{}^\sigma = -\omega^\sigma{}_\nu$. So $\delta\mathcal L = \frac12\omega_{\nu\rho}\partial_\sigma\mathcal J^{\sigma\nu\rho}$: outcome (ii).
>
> **4. Current.** $\partial^\mu\phi\,\Delta^{\nu\rho}\phi - \mathcal J^{\mu\nu\rho} = x^\nu(\partial^\mu\phi\,\partial^\rho\phi - g^{\mu\rho}\mathcal L) - x^\rho(\partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L) = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-6-1|Example §C1b.6.1]]): the orbital $\mathcal M^{\mu\nu\rho}$, as in the statement with $\mathcal S = 0$.
>
> **What the derivation shows**
> - For the scalar the two routes agree term by term: the $\mathcal J^{\sigma\nu\rho}$ found by the test satisfies $\frac12\omega_{\nu\rho}\mathcal J^{\sigma\nu\rho} = -\mathcal L\,\delta x^\sigma$ with $\delta x^\sigma = \omega^\sigma{}_\rho x^\rho$, the dictionary of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-4|Theorem §C1b.6.4]].
> - The only term that could have produced a spin current, $\omega^\sigma{}_\mu\,\partial^\mu\phi\,\partial_\sigma\phi$ in step 2, vanishes for a scalar (antisymmetric against symmetric); for a field with an index it survives and becomes $\mathcal S^{\mu\nu\rho}$.
> - Used next: the charges ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-7-1|Def. §C1b.7.1]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-1|Example §C1b.7.1]]).

*Uses:* [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-1|Def. §C1b.6.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-2|Theorem §C1b.6.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]]

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, steps 1–5]]

> [!definition] Definition §C1b.7.1: Angular-Momentum and Boost Charges
> The Lorentz charges are $J^{\nu\rho} \equiv \int d^3x\,\mathcal M^{0\nu\rho} = -J^{\rho\nu}$, six in all, split into orbital and spin parts,
>
> $$
> J^{\nu\rho} = L^{\nu\rho} + S^{\nu\rho}, \qquad L^{\nu\rho} = \int d^3x\,\bigl(x^\nu T^{0\rho} - x^\rho T^{0\nu}\bigr), \qquad S^{\nu\rho} = \int d^3x\,\mathcal S^{0\nu\rho} .
> $$
>
> The **angular momentum** is $J^i \equiv \frac12\varepsilon_{ijk}J^{jk}$, i.e. $\mathbf J = (J^{23}, J^{31}, J^{12})$, with $\varepsilon_{123} = 1$; the **boost charges** are $K^i \equiv J^{i0}$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 4 and eq. (Mgeneral) · Yu §1.7.3, eqs. (1.240)–(1.249)*

^def-c1b-7-1

> [!theorem] Theorem §C1b.7.2: The Antisymmetric Part of T Is a Divergence
> On shell,
>
> $$
> T^{\nu\rho} - T^{\rho\nu} = -\partial_\mu\mathcal S^{\mu\nu\rho} .
> $$
>
> The orbital current $x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$ is conserved by itself if and only if $T$ is symmetric. For scalar fields $\mathcal S = 0$ and $T$ is symmetric; for fields with spin the canonical $T$ is not, and Lorentz invariance requires only that its antisymmetric part be a divergence.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eq. (Tantisym) and Example 4 · Yu Exercise 1.10(a), eq. (1.273)*

^thm-c1b-7-2

> [!derivation]- Derivation
> **1. Divergence of a moment.** $\partial_\mu(x^\nu T^{\mu\rho}) = (\partial_\mu x^\nu)T^{\mu\rho} + x^\nu\partial_\mu T^{\mu\rho} = \delta^\nu{}_\mu T^{\mu\rho} + 0 = T^{\nu\rho}$ on shell ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]]).
>
> **2. The other moment.** Likewise $\partial_\mu(x^\rho T^{\mu\nu}) = T^{\rho\nu}$, so the orbital current has divergence $T^{\nu\rho} - T^{\rho\nu}$: zero for all $\nu\rho$ if and only if $T$ is symmetric.
>
> **3. Conservation of $\mathcal M$.** $0 = \partial_\mu\mathcal M^{\mu\nu\rho} = T^{\nu\rho} - T^{\rho\nu} + \partial_\mu\mathcal S^{\mu\nu\rho}$ ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]]).
>
> **4. Scalars.** $\mathcal S = 0$, so $T^{\nu\rho} = T^{\rho\nu}$, in agreement with [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-6-1|Example §C1b.6.1]].
>
> **What the derivation shows**
> - The table of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-3|Remark: The canonical tensor of the standard fields]] is explained: the antisymmetric part of the canonical $T$ is minus the divergence of the spin current.
> - ⚑ By-product: a divergence can be removed by an improvement term → [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]].

^der-c1b-7-2

*Uses:* [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]]

> [!example] Example §C1b.7.1: Angular Momentum and Boost Charges of the Scalar Field
> For the real scalar field ($\mathcal S = 0$), with the momentum density $\boldsymbol{\mathcal P} = -\pi\nabla\phi$, $\mathcal P^k = T^{0k}$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]):
> 1. **Rotations.** $J^{jk} = \int d^3x\,(x^j\mathcal P^k - x^k\mathcal P^j)$. Then $J^i = \frac12\varepsilon_{ijk}J^{jk} = \frac12\int d^3x\,(\varepsilon_{ijk}x^j\mathcal P^k - \varepsilon_{ijk}x^k\mathcal P^j)$; relabel $j \leftrightarrow k$ in the second term, $-\varepsilon_{ikj}x^j\mathcal P^k = +\varepsilon_{ijk}x^j\mathcal P^k$, so the two halves are equal and
>
> $$
> \mathbf J = \int d^3x\;\mathbf x\times\boldsymbol{\mathcal P} ,
> $$
>
> the angular momentum of the field, $\mathbf x\times\mathbf p$ integrated over space. For a scalar it is all orbital; spin is what a field with components adds, $S^{jk}$.
> 2. **Boosts.** $K^i = J^{i0} = \int d^3x\,(x^iT^{00} - x^0T^{0i})$; $x^0 = t$ is constant on the slice, so
>
> $$
> K^i = \int d^3x\;x^i\,\mathcal H - t\,P^i .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 4, "The charges: angular momentum" and "The charges: boosts" · Yu §1.7.3, eqs. (1.243)–(1.249)*

^ex-c1b-7-1

> [!theorem] Theorem §C1b.7.3: The Centre of Energy Moves Uniformly
> For a field with $\mathcal S = 0$ (a scalar) whose $T^{\mu\nu}$ falls off faster than $1/r^3$ at spatial infinity, conservation of $K^i$ and $P^i$ gives
>
> $$
> P^i = H\,\frac{dX^i_E}{dt}, \qquad X^i_E \equiv \frac1H\int d^3x\;x^i\,\mathcal H :
> $$
>
> the centre of energy moves with the constant velocity $\mathbf P/H$. For slow matter $H \approx M$ and this is the centre-of-mass theorem.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 4, "The charges: boosts" · Yu §1.7.3, eqs. (1.249)–(1.252)*

^thm-c1b-7-3

> [!derivation]- Derivation
> **1. Conservation of $K^i$.** $\mathcal M^{\mu i0}$ is a conserved current ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]]); its spatial components $x^iT^{j0} - tT^{ji}$ contain a factor $x$, so their flux through a sphere of radius $R$ vanishes as $R \to \infty$ only if $T$ falls off faster than $1/R^3$ (the stated assumption). Then [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]] gives $dK^i/dt = 0$. ⚑ By-product: the moment currents need a stronger fall-off than $P^\nu$.
>
> **2. Differentiate.** With [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-1|Example §C1b.7.1]], $0 = \frac{d}{dt}\Bigl(\int d^3x\,x^i\mathcal H - tP^i\Bigr) = \frac{d}{dt}\int d^3x\,x^i\mathcal H - P^i - t\frac{dP^i}{dt}$, and $dP^i/dt = 0$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]). So $P^i = \frac{d}{dt}\int d^3x\,x^i\mathcal H$.
>
> **3. Factor out $H$.** $H$ is constant (Theorem §C1b.6.6), so $\int d^3x\,x^i\mathcal H = H X^i_E$ gives $\frac{d}{dt}(HX^i_E) = H\,dX^i_E/dt$. Since $P^i$ and $H$ are both constant, $dX^i_E/dt$ is constant: uniform motion.
>
> **4. Slow matter.** When the energy is dominated by rest energy, $H \approx M$ (natural units) and $\mathbf P \approx M\,d\mathbf X/dt$: the centre of mass moves uniformly, as in [[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-5|CM Theorem §B6.4.5]], item 4.
>
> **What the derivation shows**
> - Boost invariance does not give a new constant of the fields alone: $K^i$ depends on $t$ explicitly, and its conservation is a statement about how the energy distribution moves.
> - For a field with spin, $K^i$ includes $S^{i0}$, and the statement holds as written only if $S^{i0}$ is separately conserved (Yu below eq. (1.249)); the Belinfante tensor removes the need ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]], 4).

^der-c1b-7-3

*Uses:* [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-1|Example §C1b.7.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]

> [!remark] Remark: What the boost charges are
> $K^i$ is conserved but depends on time explicitly; it is not "new" in the sense of $H$, $\mathbf P$, $\mathbf J$, but it is a genuine constraint, the relativistic centre-of-mass theorem. The particle version is the Galilean boost charge $M\mathbf X - \mathbf Pt$ of [[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-5|CM Theorem §B6.4.5]]. It is the reason the boost generators appear alongside $H$, $\mathbf P$ and $\mathbf J$ when the Poincaré algebra is represented on the Hilbert space ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-5|Theorem §C3.5.5]]; the boost generator is $J^{0i} = -K^i$, [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]]), with the same Lorentz algebra as the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]].

^rem-c1b-7-1

## The symmetric tensor

> [!theorem] Theorem §C1b.7.4: The Belinfante Tensor
> With $\mathcal S^{\lambda\mu\nu}$ of [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]], set
>
> $$
> K^{\lambda\mu\nu} \equiv \tfrac12\bigl(\mathcal S^{\lambda\mu\nu} + \mathcal S^{\mu\nu\lambda} + \mathcal S^{\nu\mu\lambda}\bigr), \qquad \hat T^{\mu\nu} \equiv T^{\mu\nu} + \partial_\lambda K^{\lambda\mu\nu} .
> $$
>
> Then $K^{\lambda\mu\nu} = -K^{\mu\lambda\nu}$, and on shell, for fields falling off fast enough at spatial infinity:
> 1. $\hat T^{\mu\nu} = \hat T^{\nu\mu}$;
> 2. $\partial_\mu\hat T^{\mu\nu} = 0$;
> 3. $\hat T$ has the same charges $P^\nu$ as $T$;
> 4. $x^\nu\hat T^{\mu\rho} - x^\rho\hat T^{\mu\nu}$ is conserved by itself, and its charges are the total $J^{\nu\rho} = L^{\nu\rho} + S^{\nu\rho}$: the spin is absorbed into the orbital moment of $\hat T$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, "Belinfante: symmetrizing T with the spin current", eq. (Belinfante) · Yu Exercise 1.10, eqs. (1.271)–(1.276)*

^thm-c1b-7-4

> [!derivation]- Derivation
> $\mathcal S^{\lambda\alpha\beta} = -\mathcal S^{\lambda\beta\alpha}$ (antisymmetric in its last two indices) is used throughout.
>
> **1. $K$ is antisymmetric in its first two indices.** $K^{\mu\lambda\nu} = \frac12(\mathcal S^{\mu\lambda\nu} + \mathcal S^{\lambda\nu\mu} + \mathcal S^{\nu\lambda\mu})$; flip the last two indices of each term: $= \frac12(-\mathcal S^{\mu\nu\lambda} - \mathcal S^{\lambda\mu\nu} - \mathcal S^{\nu\mu\lambda}) = -K^{\lambda\mu\nu}$.
>
> **2. Its antisymmetric part in the last two indices is $\mathcal S$.** $K^{\lambda\nu\mu} = \frac12(\mathcal S^{\lambda\nu\mu} + \mathcal S^{\nu\mu\lambda} + \mathcal S^{\mu\nu\lambda})$. Subtracting, the second and third terms of $K^{\lambda\mu\nu}$ cancel against the third and second of $K^{\lambda\nu\mu}$: $K^{\lambda\mu\nu} - K^{\lambda\nu\mu} = \frac12(\mathcal S^{\lambda\mu\nu} - \mathcal S^{\lambda\nu\mu}) = \frac12(\mathcal S^{\lambda\mu\nu} + \mathcal S^{\lambda\mu\nu}) = \mathcal S^{\lambda\mu\nu}$.
>
> **3. Symmetry.** $\hat T^{\mu\nu} - \hat T^{\nu\mu} = (T^{\mu\nu} - T^{\nu\mu}) + \partial_\lambda(K^{\lambda\mu\nu} - K^{\lambda\nu\mu}) = -\partial_\lambda\mathcal S^{\lambda\mu\nu} + \partial_\lambda\mathcal S^{\lambda\mu\nu} = 0$, by [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]] (renamed $\nu\rho \to \mu\nu$, $\mu \to \lambda$) and step 2.
>
> **4. Conservation.** For each fixed $\nu$, $B^{\lambda\mu} \equiv K^{\lambda\mu\nu}$ is antisymmetric (step 1), so $\partial_\mu\partial_\lambda K^{\lambda\mu\nu} = 0$ identically ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], 1), and $\partial_\mu\hat T^{\mu\nu} = \partial_\mu T^{\mu\nu} = 0$.
>
> **5. Same $P^\nu$.** Theorem §C1b.5.4, 2: $\int d^3x\,\partial_\lambda K^{\lambda0\nu} = \int d^3x\,\partial_iK^{i0\nu}$ (the $\lambda = 0$ term vanishes, $K^{00\nu} = 0$ by step 1), a surface term that vanishes with the fall-off.
>
> **6. The orbital current of $\hat T$.** As in steps 1–2 of [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^der-c1b-7-2|Derivation §C1b.7.2]], $\partial_\mu(x^\nu\hat T^{\mu\rho} - x^\rho\hat T^{\mu\nu}) = \hat T^{\nu\rho} - \hat T^{\rho\nu} = 0$ by steps 3–4.
>
> **7. Its charges.** The difference from $L^{\nu\rho}$ is $\int d^3x\,\bigl(x^\nu\partial_\lambda K^{\lambda0\rho} - x^\rho\partial_\lambda K^{\lambda0\nu}\bigr)$. The $\lambda = 0$ terms vanish ($K^{00\rho} = 0$). For $\lambda = i$, integrate by parts ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]], on a ball $B_R$, then $R \to \infty$): $\int d^3x\,x^\nu\partial_iK^{i0\rho} = \oint(\dots) - \int d^3x\,(\partial_ix^\nu)K^{i0\rho} = -\int d^3x\,\delta^\nu{}_iK^{i0\rho}$, the surface term vanishing if $K$ falls off faster than $1/R^3$. For $\nu = 0$ this is $0 = -\int K^{00\rho}$; for $\nu$ spatial it is $-\int K^{\nu0\rho}$; in all cases $-\int d^3x\,K^{\nu0\rho}$. So the difference is $-\int d^3x\,(K^{\nu0\rho} - K^{\rho0\nu})$, and
>
> $$
> K^{\nu0\rho} - K^{\rho0\nu} = \tfrac12\bigl(\mathcal S^{\nu0\rho} + \mathcal S^{0\rho\nu} + \mathcal S^{\rho0\nu}\bigr) - \tfrac12\bigl(\mathcal S^{\rho0\nu} + \mathcal S^{0\nu\rho} + \mathcal S^{\nu0\rho}\bigr) = \tfrac12\bigl(\mathcal S^{0\rho\nu} - \mathcal S^{0\nu\rho}\bigr) = -\mathcal S^{0\nu\rho} .
> $$
>
> The difference is $+\int d^3x\,\mathcal S^{0\nu\rho} = S^{\nu\rho}$: the orbital charges of $\hat T$ are $L^{\nu\rho} + S^{\nu\rho} = J^{\nu\rho}$.
>
> **What the derivation shows**
> - Lorentz invariance (through Theorem §C1b.7.2) is what makes the antisymmetric part removable; the improvement freedom of [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]] does the removal.
> - ⚑ By-product: the fall-off needed is $1/R^2$ for $P^\nu$ and $1/R^3$ for $J^{\nu\rho}$ (steps 5, 7).
> - Used next: the electromagnetic field ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-2|Example §C1b.7.2]]); the Dirac field gives $\hat T^{\mu\nu} = \frac i4\bar\psi\bigl(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu}\bigr)\psi$ (the user's notes; [[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-9|Theorem §C5a.5.9]]).

^der-c1b-7-4

*Uses:* [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^def-c1b-7-1|Def. §C1b.7.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]

> [!example] Example §C1b.7.2: The Electromagnetic Field
> $\mathcal L = -\frac14F_{\rho\sigma}F^{\rho\sigma}$ with the four fields $A_\lambda$ (source-free; [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]]).
> 1. **Translations.** Every component moves the same way, $\Delta_\nu A_\lambda = \partial_\nu A_\lambda$; $\mathcal L$ has no explicit $x$, so $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]]).
> 2. **The derivative.** $\partial\mathcal L/\partial(\partial_\mu A_\lambda) = -F^{\mu\lambda}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-12|Theorem §C1a.5.12]]).
> 3. **Canonical tensor,** summed over the field label $\lambda$:
>
> $$
> T^{\mu\nu} = -F^{\mu\lambda}\,\partial^\nu A_\lambda + \tfrac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma} .
> $$
>
> It is conserved, but it is not symmetric ($-F^{\mu\lambda}\partial^\nu A_\lambda$ depends on the order of $\mu\nu$) and not gauge invariant (under $A_\lambda \to A_\lambda + \partial_\lambda\chi$, $\partial^\nu A_\lambda$ gains $\partial^\nu\partial_\lambda\chi$).
> 4. **Improvement.** Take $K^{\lambda\mu\nu} = F^{\mu\lambda}A^\nu$, antisymmetric in $\lambda\mu$ because $F$ is. By the product rule, $\partial_\lambda K^{\lambda\mu\nu} = (\partial_\lambda F^{\mu\lambda})A^\nu + F^{\mu\lambda}\partial_\lambda A^\nu$, and the source-free Maxwell equations $\partial_\lambda F^{\lambda\mu} = 0$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]]) give $\partial_\lambda F^{\mu\lambda} = -\partial_\lambda F^{\lambda\mu} = 0$. On shell, $\partial_\lambda K^{\lambda\mu\nu} = F^{\mu\lambda}\partial_\lambda A^\nu$.
> 5. **Combine.** $\hat T^{\mu\nu} = -F^{\mu\lambda}\bigl(\partial^\nu A_\lambda - \partial_\lambda A^\nu\bigr) + \frac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma}$, and $\partial^\nu A_\lambda - \partial_\lambda A^\nu = F^{\nu\sigma}g_{\sigma\lambda} = F^\nu{}_\lambda$:
>
> $$
> \hat T^{\mu\nu} = -F^{\mu\lambda}F^\nu{}_\lambda + \tfrac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma} ,
> $$
>
> symmetric ($F^{\mu\lambda}F^\nu{}_\lambda = F^{\mu\lambda}g_{\lambda\sigma}F^{\nu\sigma}$ is unchanged by $\mu \leftrightarrow \nu$ after relabelling $\lambda \leftrightarrow \sigma$) and gauge invariant (built from $F$ alone).
> 6. **Components.** With $F^{0i} = -E^i$, $F^{ij} = -\varepsilon_{ijk}B^k$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]]) and one metric sign per lowered spatial index: $F_{\rho\sigma}F^{\rho\sigma} = 2F_{0i}F^{0i} + F_{ij}F^{ij} = -2\mathbf E^2 + \varepsilon_{ijk}\varepsilon_{ijl}B^kB^l = 2(\mathbf B^2 - \mathbf E^2)$. Then $F^0{}_0 = 0$ and $F^0{}_i = -F^{0i}$ give $-F^{0\lambda}F^0{}_\lambda = F^{0i}F^{0i} = \mathbf E^2$, and $F^i{}_j = -F^{ij}$ gives $-F^{0\lambda}F^i{}_\lambda = F^{0j}F^{ij} = \varepsilon_{ijk}E^jB^k$:
>
> $$
> \hat T^{00} = \mathbf E^2 + \tfrac12(\mathbf B^2 - \mathbf E^2) = \tfrac12\bigl(\mathbf E^2 + \mathbf B^2\bigr), \qquad \hat T^{0i} = (\mathbf E\times\mathbf B)^i :
> $$
>
> the energy density and the Poynting vector (Heaviside–Lorentz units).
> 7. **It is Belinfante's tensor.** For a vector, $(S^{\mu\nu})_\alpha{}^\beta = \delta^\mu{}_\alpha g^{\nu\beta} - \delta^\nu{}_\alpha g^{\mu\beta}$ ([[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|Example §C1b.1.1]]), so $\mathcal S^{\lambda\mu\nu} = -F^{\lambda\alpha}(\delta^\mu{}_\alpha g^{\nu\beta} - \delta^\nu{}_\alpha g^{\mu\beta})A_\beta = -F^{\lambda\mu}A^\nu + F^{\lambda\nu}A^\mu$. In [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]] the three terms give $A^\nu$-terms $-F^{\lambda\mu} + F^{\mu\lambda} = 2F^{\mu\lambda}$, $A^\mu$-terms $F^{\lambda\nu} + F^{\nu\lambda} = 0$ and $A^\lambda$-terms $-F^{\mu\nu} - F^{\nu\mu} = 0$, so $K^{\lambda\mu\nu} = F^{\mu\lambda}A^\nu$: the choice of item 4.
>
> *Source: PHY 513 Problem Set 2, Problem 4 (= PS Problem 2.1), with the course solution · the user's PHY 513 notes, Ch. 3 §3.5, Example 5, eqs. (TEMcanonical), (TEMsym), and the Belinfante check*

^ex-c1b-7-2

*Procedure:* [[P3 Noether's Procedure#^p3-4|P3, steps 1–5]]

> [!remark] Remark: Index moves for the electromagnetic tensor
> The moves of [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-2|Example §C1b.7.2]] are general; $F$ is only the example. Differentiating a contraction through the metric, where both factors respond and the $\frac14$ cancels, is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-12|Theorem §C1a.5.12]]. Then:
> 1. *Equate a scalar with a tensor by inserting δ*: $\partial_\nu\mathcal L = \partial_\mu(\delta^\mu{}_\nu\mathcal L)$ changes no value and supplies the index structure; it is legitimate because the parameter multiplying both sides is constant.
> 2. *Raise a label with the metric, not by hand*: $T^{\mu\nu} = g^{\nu\alpha}T^\mu{}_\alpha$ turns $\partial_\alpha A_\lambda$ into $\partial^\nu A_\lambda$ and $\delta^\mu{}_\alpha$ into $g^{\mu\nu}$, and nothing else.
> 3. *Prove symmetry by relabelling dummies*: a term is symmetric if swapping $\mu\nu$ and renaming dummies returns it, or a pair of terms if the swap exchanges them; a leftover such as $(\partial_\beta F^{\mu\beta})A^\nu$ must vanish on shell, and does by Maxwell's equations.
> 4. *Product rule, then the equations of motion, before expanding*: look for the equation of motion inside a divergence; expanding $F$ into $A$ first gives the same answer with much more algebra.
> 5. *Keep three kinds of index apart*: in $T^\mu{}_\nu = \frac{\partial\mathcal L}{\partial(\partial_\mu A_\lambda)}\partial_\nu A_\lambda - \delta^\mu{}_\nu\mathcal L$, $\lambda$ is the field component (summed away), $\nu$ says which translation, $\mu$ is the current index.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, "Index techniques for the Lagrangian and T^{μν} of the electromagnetic field (Problem Set 2)"*

^rem-c1b-7-2

> [!remark]- ★ Remark: Why there is a right symmetric tensor
> The improved $\hat T^{\mu\nu}$ is not merely convenient. Defined as the response of the action to a change of the metric, $T_{\mu\nu} = \frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g^{\mu\nu}}$, equivalently $T^{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g_{\mu\nu}}$, with $g = \operatorname{diag}(+,-,-,-)$ (for the scalar, $\delta\sqrt{-g} = -\frac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ gives $T_{\mu\nu} = \partial_\mu\phi\,\partial_\nu\phi - g_{\mu\nu}\mathcal L$, with $T_{00} = \mathcal H > 0$; the user's notes write $T^{\mu\nu} = +\frac{2}{\sqrt{-g}}\frac{\delta S}{\delta g_{\mu\nu}}$, the mostly-plus form, which in this signature gives $-T^{\mu\nu}$), the energy–momentum tensor is symmetric by construction (as $g_{\mu\nu}$ is), gauge invariant, and the source of gravity; for scalars it coincides with the canonical tensor, and for fields with spin it reproduces Belinfante's (Yu calls it the tensor to put into Einstein's equations, Exercise 1.10). That is the deeper reason the canonical tensor of $A_\mu$ needed fixing while the scalar's did not. Gravity is Relativity level C (planned).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, end of "Belinfante: symmetrizing T with the spin current" · Yu Exercise 1.10*

^rem-c1b-7-3

> [!remark]- ★ Remark: Dilatations
> The scale transformation has the generator $\Delta\phi = \phi + x^\mu\partial_\mu\phi$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]). Step 2 for $\mathcal L = \frac12(\partial\phi)^2 - \frac12m^2\phi^2$ (computed here; the user's notes state only the outcome): $\delta(\partial_\mu\phi) = \alpha\,\partial_\mu(\phi + x^\nu\partial_\nu\phi) = \alpha(2\partial_\mu\phi + x^\nu\partial_\nu\partial_\mu\phi)$, so the kinetic part changes by $\alpha\,\partial^\mu\phi(2\partial_\mu\phi + x^\nu\partial_\nu\partial_\mu\phi) = \alpha(4\mathcal L_{\rm kin} + x^\nu\partial_\nu\mathcal L_{\rm kin}) = \alpha\,\partial_\nu(x^\nu\mathcal L_{\rm kin})$, using $\partial_\nu x^\nu = 4$. The mass part changes by $-\alpha m^2\phi(\phi + x^\nu\partial_\nu\phi) = \alpha(2\mathcal L_{\rm m} + x^\nu\partial_\nu\mathcal L_{\rm m}) = \alpha\bigl[\partial_\nu(x^\nu\mathcal L_{\rm m}) + m^2\phi^2\bigr]$. In total $\delta\mathcal L = \alpha\,\partial_\nu(x^\nu\mathcal L) + \alpha m^2\phi^2$. For $m = 0$ this is outcome (ii) with $\mathcal J^\mu = x^\mu\mathcal L$, and the dilatation current is $j^\mu = \partial^\mu\phi(\phi + x^\nu\partial_\nu\phi) - x^\mu\mathcal L = x_\nu T^{\mu\nu} + \phi\,\partial^\mu\phi$. For $m \ne 0$ the leftover $m^2\phi^2$ is not a divergence (its integral against a bump configuration is positive, while a divergence integrates to the flux of the zero configuration, zero; the argument of [[§C1b.5 Noether's Theorem#^ex-c1b-5-1|Example §C1b.5.1]]): the mass, a dimensionful parameter, breaks scale invariance ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]). In Yu's form, $\phi'(x) = \lambda\phi(\lambda x)$ reads $\phi'(x') = \lambda\phi(x)$ at $x' = x/\lambda$, so the displacement is $\delta x^\mu = -\alpha x^\mu$ (opposite in sign to the parameter, like the lecture's translation $\delta x = -a$); it changes the volume element by $1 - 4\alpha$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-2|Theorem §C1b.6.2]]), which the field's weight compensates for $m = 0$ ($\mathcal L_{\rm kin}'(x') = \lambda^4\mathcal L_{\rm kin}(x)$), and the dictionary of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-4|Theorem §C1b.6.4]], $\alpha\mathcal J^\mu = -\mathcal L\,\delta x^\mu = \alpha x^\mu\mathcal L$, reproduces the $\mathcal J^\mu$ found above.

^rem-c1b-7-4

> [!caution] Caution: Notation in Yu and in the conventions table
> - Yu writes the field's Lorentz transformation as $\Phi'_a(x') = \bigl(\delta_{ab} - \frac i2\omega_{\mu\nu}(I^{\mu\nu})_{ab}\bigr)\Phi_b(x)$ (eq. (1.230)), so his generator matrices are $I^{\mu\nu} = iS^{\mu\nu}$; his spin term $-i\,\pi_a(I^{\nu\rho})_{ab}\Phi_b$ is $\mathcal S^{\nu\rho}$ here, and his $J^{\mu\nu\rho}$ (eq. (1.238)) is $\mathcal M^{\mu\nu\rho}$.
> - Yu's Belinfante–Rosenfeld tensor $\Theta^{\mu\nu} = T^{\mu\nu} + \frac12\partial_\rho(S^{\mu\nu\rho} + S^{\nu\mu\rho} - S^{\rho\nu\mu})$ (eq. (1.272)), with $S^{\mu\nu\rho} = \mathcal S^{\mu\nu\rho}$ (derivative index first), is $\hat T^{\mu\nu}$: rename $\lambda \to \rho$ in $\partial_\lambda K^{\lambda\mu\nu}$ and use $-\mathcal S^{\rho\nu\mu} = \mathcal S^{\rho\mu\nu}$.
> - Yu reads Lorentz transformations passively, the lecture actively ([[Larsen PHY 513]]); the formulas in $\omega_{\mu\nu}$ agree.
> - The boost charge here is $K^i \equiv J^{i0} = \int x^i\mathcal H - tP^i$ (Yu's $L^{i0}$). The conventions table's "boost generator $K^i = J^{0i}$" refers to the generators of Lorentz transformations ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]), not to these Noether charges; how the charges represent the generators on the Hilbert space, with signs and factors of $i$, is [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]]; the boost generator is $J^{0i} = -K^i$ ([[§C3.5 Quantum Poincaré Transformations#^cau-c3-5-1|§C3.5, Caution: Signs and names across the sources]]).

^cau-c1b-7-1

> [!remark]- Connections
> - Poynting's theorem ([[§B9.1 Charge, Energy and Poynting's Theorem#^thm-b9-1-2|EM Theorem §B9.1.2]]) is the $\nu = 0$ component of $\partial_\mu\hat T^{\mu\nu} = 0$ for the free field: $\hat T^{00}$ and $\hat T^{0i}$ are the energy density and Poynting vector of [[§B9.1 Charge, Energy and Poynting's Theorem#^def-b9-1-1|EM Def. §B9.1.1]] in Heaviside–Lorentz units. The $\nu = i$ components are momentum conservation ([[§B9.2 Momentum and Angular Momentum of Fields#^thm-b9-2-2|EM Theorem §B9.2.2]]), with $\hat T^{ij} = -(E^iE^j - \frac12\delta_{ij}\mathbf E^2) - (B^iB^j - \frac12\delta_{ij}\mathbf B^2)$ minus the Maxwell stress tensor ([[§B9.2 Momentum and Angular Momentum of Fields#^def-b9-2-1|EM Def. §B9.2.1]]), i.e. the momentum flux of [[§B9.2 Momentum and Angular Momentum of Fields#^cau-b9-2-1|EM Caution: Stress tensor or momentum flux]]. That the Poynting vector is both energy flux and momentum density is the symmetry $\hat T^{0i} = \hat T^{i0}$.
> - The spin part $\mathcal S$ is zero for scalars, the photon's spin for $A_\mu$: $\mathcal S^{\lambda\mu\nu} = F^{\lambda\nu}A^\mu - F^{\lambda\mu}A^\nu$ and $\mathbf S = \int d^3x\,\mathbf E\times\mathbf A$ ([[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-4|Theorem §C4.1.4]], [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-5|Theorem §C4.1.5]]; orbital part and total [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-6|Theorem §C4.1.6]]), not gauge invariant by itself ([[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-13|Theorem §C4.6.13]]); quantized, it gives spin one and the helicities of the massive quanta ([[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-12|Theorem §C4.5.12]], agreeing with [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-8|Theorem §C4.5.8]]; not conserved alone, [[§C4.5★ Energy, Momentum and the Spin-One Quanta of the Proca Field#^thm-c4-5-11|Theorem §C4.5.11]]) and the photon helicities $\pm1$ ([[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-8-11|Theorem §C4.8.11]], agreeing with [[§C4.8 The Gupta–Bleuler Condition and Physical Photons#^thm-c4-8-8|Theorem §C4.8.8]]) and the Dirac spin $\frac12$ for $\psi$ ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-8|Theorem §C5a.5.8]]; its quanta: [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]]); the decomposition $\mathbf J = \mathbf L + \mathbf S$ of quantum mechanics ([[§C5.1 Rotations and the Angular-Momentum Commutation Relations|QM §C5.1]]) is its quantum shadow.
> - The six charges $J^{\nu\rho}$ carry the same index structure and antisymmetry as the Lorentz generators [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]; their algebra with $P^\nu$ is the Poincaré algebra ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-5|Theorem §C3.5.5]]).
> - The ★ dilatation current and the trace of $T$ connect to the mass dimension of couplings ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]): a theory with no dimensionful parameter is classically scale invariant.
> - Electromagnetism level C: the electromagnetic tensor in SI units — canonical tensor, Belinfante improvement, components $u$, $\vec S$ and the Maxwell stress, conservation with sources, positivity, and angular momentum with the centre of energy — [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-1|EM Theorem §C1.5.1]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-2|EM Theorem §C1.5.2]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^def-c1-5-1|EM Def. §C1.5.1]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-3|EM Theorem §C1.5.3]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-4|EM Theorem §C1.5.4]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-5|EM Theorem §C1.5.5]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-6|EM Theorem §C1.5.6]].
