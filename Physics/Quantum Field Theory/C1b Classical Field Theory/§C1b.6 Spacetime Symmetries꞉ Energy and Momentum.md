---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.5 Noether's Theorem]] · ↑ [[· C1b Classical Field Theory]] · [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor]] →

*Sources: the user's PHY 513 notes, Ch. 3 §3.5 (The general form; Examples II; Spacetime symmetries in general; Belinfante; Correspondence with Yu) · PHY 513 Lecture 3 (Larsen), Part C, Example 3 and "Energy Density"; Problem Set 2, Problem 4 (= PS Problem 2.1), with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2 · Yu Zhao-Huan, 量子场论讲义, §§1.7.1–1.7.3 and Exercise 1.10 · the user's pre-course notes, §1.7.*

What do translations conserve in a field theory, and how does Noether's theorem handle transformations that move the point? Energy and momentum, the integrals of the time row of one conserved tensor. Such symmetries move the point at which the field is evaluated, which the fixed-argument form of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]] cannot see directly; this section first gives Yu's general form of the theorem, with the displacement $\delta x^\mu$ built in, and its dictionary to the lecture's form, then the energy–momentum tensor for any collection of fields and its charges $P^\mu = (H, \mathbf P)$, and the energy and the momentum of the free scalar fields in field form, derived index by index, with the bracket statement that the momentum generates spatial translations as the Hamiltonian generates time evolution. Lorentz transformations (angular momentum, boost charges, the antisymmetric part of $T^{\mu\nu}$ and Belinfante's symmetric tensor) are [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.7]]. Field transformation laws are those of [[§C1b.1 Fields and Their Transformation Laws|§C1b.1]] ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]), the Lorentz parameters those of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]]; every computation runs [[P3 Noether's Procedure]].

## When the point moves: the general form

> [!theorem] Theorem §C1b.6.1: Total and Fixed-Argument Variations
> Let $x^\mu \to x'^\mu = x^\mu + \delta x^\mu$ and $\phi_a(x) \to \phi'_a(x')$, with total change $\delta\phi_a \equiv \phi'_a(x') - \phi_a(x)$ and fixed-argument change $\bar\delta\phi_a \equiv \phi'_a(x) - \phi_a(x)$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-1|Def. §C1b.5.1]]). To first order,
>
> $$
> \bar\delta\phi_a = \delta\phi_a - (\partial_\mu\phi_a)\,\delta x^\mu, \qquad \bar\delta(\partial_\mu\phi_a) = \partial_\mu(\bar\delta\phi_a), \qquad \delta(\partial_\mu\phi_a) = \partial_\mu(\delta\phi_a) - (\partial_\nu\phi_a)\,\partial_\mu(\delta x^\nu) .
> $$
>
> So $\bar\delta$ commutes with $\partial_\mu$, and $\delta$ does only when $\delta x$ is constant. The first relation holds for any local quantity, in particular $\bar\delta\mathcal L = \delta\mathcal L - (\partial_\mu\mathcal L)\,\delta x^\mu$.
>
> *Source: Yu §1.7.1, eqs. (1.189)–(1.193) · the user's PHY 513 notes, Ch. 3 §3.5, Definition "The instances of δ" and "Noether's theorem with δx^μ (Yu §1.7)" · the user's pre-course notes, §1.7, eq. (delta-relation)*

^thm-c1b-6-1

> [!derivation]- Derivation
> **1. Insert and subtract $\phi'_a(x)$.** $\delta\phi_a = \bigl[\phi'_a(x + \delta x) - \phi'_a(x)\bigr] + \bigl[\phi'_a(x) - \phi_a(x)\bigr] = \bigl[\phi'_a(x + \delta x) - \phi'_a(x)\bigr] + \bar\delta\phi_a$.
>
> **2. Taylor.** $\phi'_a(x + \delta x) - \phi'_a(x) = (\partial_\mu\phi'_a)(x)\,\delta x^\mu + O(\delta x^2)$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]).
>
> **3. Drop a second-order term.** $\phi'_a - \phi_a$ is first order, so $(\partial_\mu\phi'_a)\delta x^\mu = (\partial_\mu\phi_a)\delta x^\mu + O(\text{second order})$. Hence $\delta\phi_a = \bar\delta\phi_a + (\partial_\mu\phi_a)\delta x^\mu$, the first relation.
>
> **4. $\bar\delta$ commutes.** $\bar\delta(\partial_\mu\phi_a) \equiv (\partial_\mu\phi'_a)(x) - (\partial_\mu\phi_a)(x) = \partial_\mu(\phi'_a - \phi_a)(x) = \partial_\mu(\bar\delta\phi_a)$: both functions are evaluated at the same argument, and $\partial_\mu$ is linear.
>
> **5. The total change of a derivative.** Steps 1–3 apply to any local quantity, here $\partial_\mu\phi_a$: $\delta(\partial_\mu\phi_a) = \bar\delta(\partial_\mu\phi_a) + (\partial_\nu\partial_\mu\phi_a)\delta x^\nu = \partial_\mu(\bar\delta\phi_a) + (\partial_\nu\partial_\mu\phi_a)\delta x^\nu$ (Yu eq. (1.193)).
>
> **6. Compare with the derivative of the total change.** Differentiating the first relation by the product rule, $\partial_\mu(\delta\phi_a) = \partial_\mu(\bar\delta\phi_a) + (\partial_\mu\partial_\nu\phi_a)\delta x^\nu + (\partial_\nu\phi_a)\,\partial_\mu(\delta x^\nu)$. Partial derivatives commute, so subtracting step 5 leaves $\partial_\mu(\delta\phi_a) - \delta(\partial_\mu\phi_a) = (\partial_\nu\phi_a)\partial_\mu(\delta x^\nu)$, the third relation. ⚑ By-product: for translations $\delta x$ is constant and both variations commute with $\partial_\mu$; for Lorentz transformations $\partial_\mu\delta x^\nu = \omega^\nu{}_\mu \ne 0$, which is why the proof of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]] must use fixed-argument variations.
>
> **7. Any local quantity.** Steps 1–3 with $\mathcal L(x) = \mathcal L(\phi(x), \partial\phi(x))$ in place of $\phi_a$ give $\delta\mathcal L = \bar\delta\mathcal L + (\partial_\mu\mathcal L)\delta x^\mu$, where $\partial_\mu\mathcal L$ is the derivative of the composite function of $x$.
>
> **What the derivation shows**
> - Only first order is kept; the single dropped term (step 3) is second order.
> - Used next: [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]] (steps 3–4 there), [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-4|Theorem §C1b.6.4]].

^der-c1b-6-1

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-1|Def. §C1b.5.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]

> [!definition] Definition §C1b.6.1: Symmetry of a Transformation That Moves the Point
> A transformation $x^\mu \to x'^\mu = x^\mu + \delta x^\mu$, $\phi_a(x) \to \phi'_a(x') = \phi_a(x) + \delta\phi_a$, with $\mathcal L'(x') \equiv \mathcal L\bigl(\phi'(x'), \partial'\phi'(x')\bigr)$ the same function of the transformed fields, is a **symmetry** if, to first order and for every field configuration,
>
> $$
> \int_{R'}d^4x'\;\mathcal L'(x') = \int_Rd^4x\;\mathcal L(x)
> $$
>
> for every spacetime region $R$, with $R'$ its image. Examples: $\delta x^\mu = \varepsilon^\mu$ (constant) for a translation, $\delta x^\mu = \omega^\mu{}_\nu x^\nu$ for a Lorentz transformation, $\delta x^\mu = 0$ for an internal symmetry.
>
> *Source: Yu §1.7.1, eqs. (1.176)–(1.181) · the user's PHY 513 notes, Ch. 3 §3.5, "Noether's theorem with δx^μ"*

^def-c1b-6-1

> [!theorem] Theorem §C1b.6.2: The Volume Element to First Order
> Under $x'^\mu = x^\mu + \delta x^\mu$,
>
> $$
> d^4x' = \bigl[1 + \partial_\mu(\delta x^\mu)\bigr]\,d^4x
> $$
>
> to first order. The correction vanishes for translations and for Lorentz transformations, $\partial_\mu(\omega^\mu{}_\nu x^\nu) = \omega^\mu{}_\mu = 0$.
>
> *Source: Yu §1.7.1, eqs. (1.182)–(1.187) · the user's pre-course notes, §1.7, eqs. (det-expansion), (volume-transform)*

^thm-c1b-6-2

> [!derivation]- Derivation
> **1. Jacobian.** $J = \det(\partial x'^\mu/\partial x^\nu) = \det(\delta^\mu{}_\nu + \partial_\nu\delta x^\mu) = \det(1 + A)$, with $A^\mu{}_\nu \equiv \partial_\nu\delta x^\mu$ first order.
>
> **2. Determinant to first order.** In the Leibniz formula $\det(1 + A) = \sum_\sigma\operatorname{sgn}\sigma\prod_\mu(1 + A)^\mu{}_{\sigma(\mu)}$ ([[§37 Determinants#^ladr-9-46|LADR 9.46]]), the identity permutation contributes $\prod_\mu(1 + A^\mu{}_\mu) = 1 + \sum_\mu A^\mu{}_\mu + O(A^2)$. Any other permutation moves at least two indices, so its product contains at least two off-diagonal entries of $A$: $O(A^2)$. Hence $\det(1 + A) = 1 + \operatorname{tr}A + O(A^2)$, Jacobi's formula at the identity ([[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|591 Prop. §12.1]]; Yu uses $\det e^A = e^{\operatorname{tr}A}$).
>
> **3. The trace.** $\operatorname{tr}A = A^\mu{}_\mu = \partial_\mu\delta x^\mu$. Near the identity $J > 0$, so $\lvert J\rvert = J$ and $d^4x' = J\,d^4x$.
>
> **4. Translations and Lorentz transformations.** $\partial_\mu\varepsilon^\mu = 0$. For $\delta x^\mu = \omega^\mu{}_\nu x^\nu$: $\partial_\mu(\omega^\mu{}_\nu x^\nu) = \omega^\mu{}_\nu\delta^\nu{}_\mu = \omega^\mu{}_\mu = g^{\mu\rho}\omega_{\rho\mu} = 0$, a symmetric tensor contracted with an antisymmetric one ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]]). ⚑ By-product: Lorentz transformations preserve four-volume, the infinitesimal form of $\det\Lambda = 1$ for proper ones ([[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]]).
>
> **What the derivation shows**
> - For a dilatation $\delta x^\mu = \alpha x^\mu$ the correction is $4\alpha$: volume is not preserved → [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-7-4|★ Remark: Dilatations]].
> - Used next: step 1 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-3|Derivation §C1b.6.3]].

^der-c1b-6-2

*Uses:* [[§37 Determinants#^ladr-9-46|LADR 9.46]], [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|591 Prop. §12.1]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]]

> [!theorem] Theorem §C1b.6.3: Noether's Theorem, General Form
> If the transformation of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-1|Def. §C1b.6.1]] is a symmetry, the current
>
> $$
> j^\mu = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\,\bar\delta\phi_a + \mathcal L\,\delta x^\mu
> $$
>
> satisfies $\partial_\mu j^\mu = -\sum_a\bigl[\frac{\partial\mathcal L}{\partial\phi_a} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\bigr]\bar\delta\phi_a$ for every configuration, hence $\partial_\mu j^\mu = 0$ on shell. $j^\mu$ is first order in the parameters; their coefficients are the separate conserved currents.
>
> *Source: Yu §1.7.1, eqs. (1.188)–(1.198) · the user's PHY 513 notes, Ch. 3 §3.5, eq. (noethergeneral) · the user's pre-course notes, §1.7, Theorem "Noether's theorem, coordinate-transformation form"*

^thm-c1b-6-3

> [!derivation]- Derivation
> Write $\pi^\mu_a \equiv \partial\mathcal L/\partial(\partial_\mu\phi_a)$ and $\mathrm{EL}_a \equiv \partial\mathcal L/\partial\phi_a - \partial_\mu\pi^\mu_a$.
>
> **1. Change variables in the transformed action.** The map $x \mapsto x' = x + \delta x$ takes $R$ onto $R'$, so $\int_{R'}d^4x'\,\mathcal L'(x') = \int_Rd^4x\,J\,\mathcal L'(x + \delta x)$, with $J = 1 + \partial_\mu\delta x^\mu$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-2|Theorem §C1b.6.2]]).
>
> **2. Expand.** With $\mathcal L'(x') = \mathcal L(x) + \delta\mathcal L$ (total change),
>
> $$
> \delta S \equiv \int_{R'}d^4x'\,\mathcal L' - \int_Rd^4x\,\mathcal L = \int_Rd^4x\,\Bigl[(1 + \partial_\mu\delta x^\mu)(\mathcal L + \delta\mathcal L) - \mathcal L\Bigr] = \int_Rd^4x\,\bigl[\delta\mathcal L + \mathcal L\,\partial_\mu\delta x^\mu\bigr] ,
> $$
>
> the product $(\partial_\mu\delta x^\mu)\,\delta\mathcal L$ being second order and dropped.
>
> **3. Total to fixed-argument.** By [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]], $\delta\mathcal L = \bar\delta\mathcal L + (\partial_\mu\mathcal L)\delta x^\mu$, so the integrand is $\bar\delta\mathcal L + (\partial_\mu\mathcal L)\delta x^\mu + \mathcal L\,\partial_\mu\delta x^\mu = \bar\delta\mathcal L + \partial_\mu(\mathcal L\,\delta x^\mu)$ by the product rule. ⚑ By-product: the Jacobian and the shift of the argument assemble into one total derivative, $\partial_\mu(\mathcal L\,\delta x^\mu)$; it will be $-\alpha\,\partial_\mu\mathcal J^\mu$ in the lecture's language → [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-4|Theorem §C1b.6.4]].
>
> **4. Chain rule for $\bar\delta\mathcal L$.** $\bar\delta\mathcal L = \mathcal L(\phi'(x), \partial\phi'(x)) - \mathcal L(\phi(x), \partial\phi(x))$ compares the same function at the same $x$, so ([[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]], and $\bar\delta\partial = \partial\bar\delta$ from [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]])
>
> $$
> \bar\delta\mathcal L = \sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a}\,\bar\delta\phi_a + \pi^\mu_a\,\partial_\mu(\bar\delta\phi_a)\Bigr] .
> $$
>
> **5. Product rule.** $\pi^\mu_a\,\partial_\mu(\bar\delta\phi_a) = \partial_\mu(\pi^\mu_a\bar\delta\phi_a) - (\partial_\mu\pi^\mu_a)\bar\delta\phi_a$, so $\bar\delta\mathcal L = \sum_a\mathrm{EL}_a\,\bar\delta\phi_a + \partial_\mu\bigl(\sum_a\pi^\mu_a\bar\delta\phi_a\bigr)$.
>
> **6. Assemble.** $\delta S = \int_Rd^4x\,\bigl\{\sum_a\mathrm{EL}_a\,\bar\delta\phi_a + \partial_\mu j^\mu\bigr\}$ with $j^\mu$ as in the statement.
>
> **7. Localize.** A symmetry has $\delta S = 0$ for every region $R$ and every configuration. The integrand is continuous; if it were nonzero at a point, it would keep its sign on a small ball around that point, and the integral over that ball would not vanish. So $\sum_a\mathrm{EL}_a\,\bar\delta\phi_a + \partial_\mu j^\mu = 0$ pointwise: the off-shell identity. ⚑ By-product: "for every region" is what turns one integral condition into a local conservation law.
>
> **8. On shell.** $\mathrm{EL}_a = 0$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]), so $\partial_\mu j^\mu = 0$. Since the parameters are independent, each of their coefficients in $j^\mu$ is separately conserved (choose one parameter nonzero at a time).
>
> **What the derivation shows**
> - The displacement enters only through $J$ and the Taylor shift, and both end up in $\mathcal L\,\delta x^\mu$; no $\mathcal J$ has to be found by hand.
> - Assumptions: first order throughout; $\mathcal L'$ is $\mathcal L$ evaluated on the transformed fields; fields $C^2$.
> - Used next: [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-4|Theorem §C1b.6.4]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]] (second route), [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]].

^der-c1b-6-3

*Uses:* [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-1|Def. §C1b.6.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-2|Theorem §C1b.6.2]], [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]

> [!theorem] Theorem §C1b.6.4: The Two Forms of Noether's Theorem Agree
> A symmetry in the sense of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-1|Def. §C1b.6.1]] is a symmetry of the action in the sense of [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]], with
>
> $$
> \alpha^a\Delta_a\phi_i = \bar\delta\phi_i, \qquad \alpha^a\mathcal J^\mu_a = -\mathcal L\,\delta x^\mu, \qquad \bar\delta\mathcal L = -\partial_\mu\bigl(\mathcal L\,\delta x^\mu\bigr) ,
> $$
>
> and the currents of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]] and [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]] coincide term by term: $\alpha^aj^\mu_a = j^\mu$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, "The dictionary to the lecture's Δφ and 𝒥^μ" · the user's pre-course notes, §1.7, Remark "Equivalence with the formulation of [Fld. Theorem 9.2]"*

^thm-c1b-6-4

> [!derivation]- Derivation
> **1. The symmetry condition, pointwise.** By step 2 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-3|Derivation §C1b.6.3]], the condition of Def. §C1b.6.1 is $\int_Rd^4x\,[\delta\mathcal L + \mathcal L\,\partial_\mu\delta x^\mu] = 0$ for every $R$; localizing as in its step 7, $\delta\mathcal L + \mathcal L\,\partial_\mu\delta x^\mu = 0$ at every point.
>
> **2. The fixed-argument change of $\mathcal L$.** By [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]], $\bar\delta\mathcal L = \delta\mathcal L - (\partial_\mu\mathcal L)\delta x^\mu = -\mathcal L\,\partial_\mu\delta x^\mu - (\partial_\mu\mathcal L)\delta x^\mu = -\partial_\mu(\mathcal L\,\delta x^\mu)$.
>
> **3. Translate.** The lecture's formulation never moves the point: its field change is compared at the same $x$, which is $\bar\delta\phi_i$, so $\alpha^a\Delta_a\phi_i = \bar\delta\phi_i$; its $\delta\mathcal L$ is the change at fixed argument, $\bar\delta\mathcal L$. Step 2 then reads $\alpha^a\partial_\mu\mathcal J^\mu_a = -\partial_\mu(\mathcal L\,\delta x^\mu)$, satisfied by $\alpha^a\mathcal J^\mu_a = -\mathcal L\,\delta x^\mu$ (unique up to identically conserved vectors, [[§C1b.5 Noether's Theorem#^cau-c1b-5-2|§C1b.5, Caution: What the theorem does and does not say]]).
>
> **4. Compare the currents.** $\alpha^aj^\mu_a = \sum_i\pi^\mu_i\,\alpha^a\Delta_a\phi_i - \alpha^a\mathcal J^\mu_a = \sum_i\pi^\mu_i\,\bar\delta\phi_i + \mathcal L\,\delta x^\mu$, the current of Theorem §C1b.6.3.
>
> **What the derivation shows**
> - In the fixed-argument picture a spacetime symmetry is outcome (ii): $\mathcal L$ changes by the divergence of $-\mathcal L\,\delta x^\mu$ — a scalar density evaluated at a shifted point differs from the original by its gradient times the shift. This is the lecture's "action invariant but Lagrangian not".
> - Example: the lecture's translation $x \to x - a$ has $\delta x^\mu = -a^\mu$, so $\alpha\mathcal J^\mu = a^\mu\mathcal L$, which is $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]]).
> - Scope: the lecture's $\mathcal J$ also allows a total-derivative change unconnected with motion of the point (Galilean boosts of a Schrödinger field, for instance); the union of the two forms is $j^\mu = \sum\pi^\mu\bar\delta\phi + \mathcal L\,\delta x^\mu - \mathcal K^\mu$ with $\bar\delta\mathcal L = -\partial_\mu(\mathcal L\,\delta x^\mu) + \partial_\mu\mathcal K^\mu$. In every example of this chapter $\mathcal K = 0$.

^der-c1b-6-4

*Uses:* [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]

*Procedure:* [[P3 Noether's Procedure#^p3-3|P3, step 3]]

> [!caution] Caution: One picture at a time; the sign of the displacement
> - Never take $\Delta\phi$ from one picture and $\mathcal J$ from the other: the fixed-argument $\Delta\phi$ pairs with the $\mathcal J$ read off by the test; $\bar\delta\phi$ pairs with $\mathcal L\,\delta x^\mu$.
> - The lecture and PS translate by $x \to x - a$, so $\phi'(x) = \phi(x + a)$, $\Delta_\nu\phi = +\partial_\nu\phi$ and the current is $+T^\mu{}_\nu$ (PS eq. (2.17)). Yu translates by $x' = x + \varepsilon$ and gets $j^\mu = -\varepsilon^\rho T^\mu{}_\rho$ (eq. (1.209)). The tensor is the same; $\varepsilon = -a$.
> - The lecture's form is the lean one for internal symmetries, where the two coincide; Yu's form is the one to use when the point moves, since $\mathcal J$ then need not be found by hand.

^cau-c1b-6-1

## Translations: the energy–momentum tensor

> [!definition] Definition §C1b.6.2: Canonical Energy–Momentum Tensor
> For $\mathcal L(\phi_a, \partial_\mu\phi_a)$, summed over every field component present,
>
> $$
> T^\mu{}_\nu \equiv \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\,\partial_\nu\phi_a - \delta^\mu{}_\nu\,\mathcal L, \qquad T^{\mu\nu} = g^{\nu\rho}T^\mu{}_\rho = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\,\partial^\nu\phi_a - g^{\mu\nu}\mathcal L .
> $$
>
> $\mu$ is the current index, $\nu$ labels the translation, $a$ the field component. It is a Lorentz tensor when $\mathcal L$ is a Lorentz scalar.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eqs. (Tmunu), (Tgeneral) · PS §2.2, eq. (2.17) · Yu §1.7.2, eqs. (1.212), (1.234) · Lecture 3, Example 3*

^def-c1b-6-2

> [!theorem] Theorem §C1b.6.5: Translation Invariance Conserves the Energy–Momentum Tensor
> If $\mathcal L$ depends on $x$ only through the fields, translations are a symmetry with $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$, their Noether currents are $T^\mu{}_\nu$, and
>
> $$
> \partial_\mu T^{\mu\nu} = -\sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\Bigr]\partial^\nu\phi_a \quad \text{(off shell)}, \qquad \partial_\mu T^{\mu\nu} = 0 \quad \text{(on shell)} :
> $$
>
> four conserved currents, one per direction $\nu$. If $\mathcal L$ depends on $x$ explicitly (an external potential, a fixed source $J(x)\phi$), translations are not a symmetry.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 3 and "Translations, all fields at once" · Lecture 3, Example 3 · PS §2.2, p. 19 · Yu §1.7.2, eqs. (1.208)–(1.213)*

^thm-c1b-6-5

> [!derivation]- Derivation
> The steps of [[P3 Noether's Procedure]] for a general $\mathcal L$; $\pi^\mu_a \equiv \partial\mathcal L/\partial(\partial_\mu\phi_a)$, $\mathrm{EL}_a \equiv \partial\mathcal L/\partial\phi_a - \partial_\mu\pi^\mu_a$.
>
> **1. Generator.** $\Delta_\nu\phi_a = \partial_\nu\phi_a$ for every component ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]), so $\delta\phi_a = a^\nu\partial_\nu\phi_a$.
>
> **2. Substitute.** The constant $a^\nu$ passes through the derivative: $\delta(\partial_\mu\phi_a) = \partial_\mu(\delta\phi_a) = a^\nu\partial_\mu\partial_\nu\phi_a$. By the chain rule ([[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]), using $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$,
>
> $$
> \delta\mathcal L = \sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a}\,a^\nu\partial_\nu\phi_a + \pi^\mu_a\,a^\nu\partial_\nu\partial_\mu\phi_a\Bigr] = a^\nu\sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a}\,\partial_\nu\phi_a + \pi^\mu_a\,\partial_\nu(\partial_\mu\phi_a)\Bigr] .
> $$
>
> **3. Recognize the gradient of $\mathcal L$.** When $\mathcal L$ depends on $x$ only through $\phi_a(x)$ and $\partial_\mu\phi_a(x)$, the bracket is the chain-rule expansion of $\partial_\nu\mathcal L$, the derivative of the composite function along direction $\nu$. So $\delta\mathcal L = a^\nu\partial_\nu\mathcal L \ne 0$: a scalar function evaluated at a shifted point is a different function. ⚑ By-product: with explicit $x$-dependence the bracket misses $\partial\mathcal L/\partial x^\nu|_{\text{explicit}}$, $\delta\mathcal L$ is not $a^\nu\partial_\nu\mathcal L$, and step 4 fails: the last sentence of the statement. (For the scalar the bracket is checked in [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-6-1|Example §C1b.6.1]].)
>
> **4. Test: write a divergence, factor the parameter.** Each $a^\nu$ is constant, so $a^\nu\partial_\nu\mathcal L = \partial_0(a^0\mathcal L) + \partial_1(a^1\mathcal L) + \partial_2(a^2\mathcal L) + \partial_3(a^3\mathcal L) = \partial_\mu(a^\mu\mathcal L)$. To factor out the parameter, write $a^\mu = \delta^\mu{}_\nu a^\nu$: $\delta\mathcal L = a^\nu\,\partial_\mu(\delta^\mu{}_\nu\mathcal L)$. The four $a^\nu$ are independent (take one nonzero at a time), so $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$: outcome (ii), for the translation in direction $\nu$ a vector pointing in direction $\nu$ with magnitude $\mathcal L$. ⚑ By-product: what is forced is only $\partial_\mu\mathcal J^\mu{}_\nu = \partial_\nu\mathcal L$, which determines $\mathcal J^\mu{}_\nu$ up to $\partial_\lambda B^{\lambda\mu}{}_\nu$ with $B$ antisymmetric in $\lambda\mu$; the canonical tensor is the minimal choice, and the freedom is the improvement of [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], used in [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]].
>
> **5. Current.** By [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], one current per $\nu$: $j^\mu_\nu = \sum_a\pi^\mu_a\partial_\nu\phi_a - \delta^\mu{}_\nu\mathcal L = T^\mu{}_\nu$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]]).
>
> **6. Off-shell identity.** The same theorem with $\Delta_\nu\phi_a = \partial_\nu\phi_a$ gives $\partial_\mu T^\mu{}_\nu = -\sum_a\mathrm{EL}_a\,\partial_\nu\phi_a$. Contract with the constant $g^{\nu\rho}$, which commutes with $\partial_\mu$: $\partial_\mu T^{\mu\rho} = -\sum_a\mathrm{EL}_a\,\partial^\rho\phi_a$. On shell, zero.
>
> **7. Direct check.** By the product rule and step 3, $\partial_\mu T^\mu{}_\nu = \sum_a\bigl[(\partial_\mu\pi^\mu_a)\partial_\nu\phi_a + \pi^\mu_a\partial_\mu\partial_\nu\phi_a\bigr] - \sum_a\bigl[\frac{\partial\mathcal L}{\partial\phi_a}\partial_\nu\phi_a + \pi^\mu_a\partial_\nu\partial_\mu\phi_a\bigr]$; the second-derivative terms cancel, leaving $-\sum_a\mathrm{EL}_a\,\partial_\nu\phi_a$, as in step 6.
>
> **What the derivation shows**
> - Energy–momentum conservation needs only that $\mathcal L$ has no explicit $x$: homogeneity of spacetime.
> - $T^{\mu\nu}$ is determined up to improvement terms; the canonical one need not be symmetric ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-3|Remark: The canonical tensor of the standard fields]]).
> - Used next: [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]].

^der-c1b-6-5

> [!derivation]- Derivation (second route: the general form)
> **1. Displacement and field change.** $x'^\mu = x^\mu + \varepsilon^\mu$ with constant $\varepsilon$; under a translation every field keeps its value at the physical point, $\phi'_a(x') = \phi_a(x)$ ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]] with $D = 1$), so $\delta\phi_a = 0$ and $\delta x^\mu = \varepsilon^\mu$.
>
> **2. Fixed-argument change.** [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-1|Theorem §C1b.6.1]]: $\bar\delta\phi_a = -\varepsilon^\rho\partial_\rho\phi_a$.
>
> **3. Symmetry.** $\mathcal L'(x') = \mathcal L(x)$ because $\mathcal L$ depends on $x$ only through the fields, and $d^4x' = d^4x$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-2|Theorem §C1b.6.2]]): Def. §C1b.6.1 holds.
>
> **4. Current.** [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]]: $j^\mu = -\sum_a\pi^\mu_a\varepsilon^\rho\partial_\rho\phi_a + \mathcal L\varepsilon^\mu = -\varepsilon^\rho\bigl(\sum_a\pi^\mu_a\partial_\rho\phi_a - \delta^\mu{}_\rho\mathcal L\bigr) = -\varepsilon^\rho T^\mu{}_\rho$, using $\varepsilon^\mu = \delta^\mu{}_\rho\varepsilon^\rho$. The four $\varepsilon^\rho$ are independent, so $\partial_\mu T^\mu{}_\rho = 0$ on shell. With $\varepsilon = -a$ this is $a^\rho T^\mu{}_\rho$, the first route's currents contracted with their parameters.
>
> **What the derivation shows**
> - In Yu's form no $\mathcal J$ has to be found: $\delta\phi_a = 0$, the Jacobian is $1$, and the whole current comes from $\bar\delta\phi_a$ and $\mathcal L\,\delta x^\mu$.
> - The two routes give the same tensor with opposite overall signs, because the displacements are opposite ($\varepsilon = -a$) → [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^cau-c1b-6-1|Caution: One picture at a time; the sign of the displacement]].
> - Used next: the same route for Lorentz transformations, where $\delta x$ depends on $x$ ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]]).

*Uses:* [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-3|Theorem §C1b.6.3]]

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, steps 1–5]]

> [!theorem] Theorem §C1b.6.6: Energy and Momentum of a Field
> The charges of translations are $P^\nu \equiv \int d^3x\,T^{0\nu}$, conserved for fields with $T^{i\nu}$ falling off faster than $1/r^2$. With the canonical momentum densities $\pi_a = \partial\mathcal L/\partial\dot\phi_a$ ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]),
>
> $$
> T^{00} = \sum_a\pi_a\dot\phi_a - \mathcal L = \mathcal H, \qquad H = P^0 = \int d^3x\,\mathcal H, \qquad T^{0i} = \sum_a\pi_a\,\partial^i\phi_a, \qquad \mathbf P = -\int d^3x\,\sum_a\pi_a\nabla\phi_a :
> $$
>
> energy is the charge of time translations, with density the Hamiltonian density, and momentum the charge of space translations.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eqs. (T00), (Pfield) · Lecture 3, "Energy Density" · PS §2.2, eqs. (2.18)–(2.19) · Yu §1.7.2, eqs. (1.214)–(1.218)*

^thm-c1b-6-6

> [!derivation]- Derivation
> **1. The time component of $\partial\mathcal L/\partial(\partial_\mu\phi_a)$.** $\partial_0 = \partial_t$, so $\pi^0_a = \partial\mathcal L/\partial(\partial_0\phi_a) = \partial\mathcal L/\partial\dot\phi_a = \pi_a$ ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]; [[§C1b.4 Hamiltonian Field Theory|§C1b.4]] explains why $\pi$ is only this component, [[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]]).
>
> **2. $T^{00}$.** In [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], $\partial^0 = g^{00}\partial_0 = \partial_t$ and $g^{00} = 1$: $T^{00} = \sum_a\pi_a\dot\phi_a - \mathcal L$, the Legendre transform that defines $\mathcal H$ ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]]). Expressed through $\phi$ and $\pi$ after eliminating the velocities, it is the same number at each point.
>
> **3. $T^{0i}$.** $g^{0i} = 0$, so $T^{0i} = \sum_a\pi_a\,\partial^i\phi_a$; with $\partial^i = g^{ij}\partial_j = -\partial_i$, $T^{0i} = -\sum_a\pi_a\partial_i\phi_a$, and since $(\nabla\phi)_i = \partial_i\phi$, $P^i = -\int d^3x\sum_a\pi_a\partial_i\phi_a$ is the $i$-th component of $\mathbf P = -\int d^3x\sum_a\pi_a\nabla\phi_a$ (PS eq. (2.19)).
>
> **4. Conservation.** For each fixed $\nu$, $T^{\mu\nu}$ is a conserved current ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]]); [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]] with $\mathbf j = (T^{1\nu}, T^{2\nu}, T^{3\nu})$ and the stated fall-off gives $dP^\nu/dt = 0$.
>
> **What the derivation shows**
> - The canonical construction (Legendre transform) and the Noether construction give the same energy density ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-1|Remark: Why the 00 component is the Hamiltonian density]]).
> - The momentum density $-\sum_a\pi_a\nabla\phi_a$ is built from $\pi$; $\pi$ itself is not the momentum carried by the field ([[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]]).
> - Used next: the free real and complex scalar fields, index by index ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7|Theorem §C1b.6.7]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-8|Theorem §C1b.6.8]]); the bracket form ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]]); the quantized $H$ and $\mathbf P$ in modes ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).

^der-c1b-6-6

*Uses:* [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]]

*Procedure:* [[P3 Noether's Procedure#^p3-6|P3, step 6]]

> [!remark] Remark: Why the 00 component is the Hamiltonian density
> The Legendre transform of [[§C1b.4 Hamiltonian Field Theory|§C1b.4]] and Noether's theorem for time translations build the same density because the Hamiltonian is, by construction, what generates time translations, and Noether's theorem says that whatever generates time translations is conserved; the particle version is the energy function of [[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-3|CM Theorem §B6.4.3]]. It also answers the question left by §C1b.4, why the Hamiltonian is not a Lorentz scalar: $H$ is the time component of $P^\nu = (H, \mathbf P)$, the charges of a conserved Lorentz tensor. On the Hilbert space $H$ and $\mathbf P$ become the generators of translations ([[§C3.5 Quantum Poincaré Transformations#^def-c3-5-1|Def. §C3.5.1]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]]), whose mode forms are [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] and [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]].

^rem-c1b-6-1

> [!example] Example §C1b.6.1: The Real Scalar Field's Energy–Momentum Tensor
> For $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]):
> 1. $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi$, so $T^\mu{}_\nu = \partial^\mu\phi\,\partial_\nu\phi - \delta^\mu{}_\nu\mathcal L$; raising $\nu$ with $g^{\nu\rho}$, $T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L$. It is symmetric: $\partial^\mu\phi\,\partial^\nu\phi$ is a product of the same factor twice, and $g$ is symmetric.
> 2. **Step 3 of Derivation §C1b.6.5, checked.** $\partial\mathcal L/\partial\phi = -m^2\phi$, so the bracket is $-m^2\phi\,\partial_\nu\phi + \partial^\mu\phi\,\partial_\nu\partial_\mu\phi$. And $\partial_\nu\bigl(\frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2\bigr) = \frac12(\partial_\nu\partial_\mu\phi\,\partial^\mu\phi + \partial_\mu\phi\,\partial_\nu\partial^\mu\phi) - m^2\phi\,\partial_\nu\phi = \partial^\mu\phi\,\partial_\nu\partial_\mu\phi - m^2\phi\,\partial_\nu\phi$: both factors of the contraction respond, and lowering one index and raising the other makes the two terms equal, cancelling the $\frac12$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|Theorem §C1a.5.11]]). The two agree.
> 3. **Energy density.** $\partial_\mu\phi\,\partial^\mu\phi = \dot\phi^2 - (\nabla\phi)^2$, so $\mathcal L = \frac12\dot\phi^2 - \frac12(\nabla\phi)^2 - \frac12m^2\phi^2$ and
>
> $$
> T^{00} = \dot\phi\,\dot\phi - \mathcal L = \tfrac12\dot\phi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2 = \mathcal H ,
> $$
>
> the Hamiltonian density ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]]) with $\pi = \dot\phi$.
> 4. **Momentum.** $T^{0i} = \dot\phi\,\partial^i\phi$, $\mathbf P = -\int d^3x\,\pi\nabla\phi$.
> 5. **Conservation, directly.** $\partial_\mu T^{\mu\nu} = (\partial^2\phi)\partial^\nu\phi + \partial^\mu\phi\,\partial_\mu\partial^\nu\phi - \partial^\nu\mathcal L$, and by item 2 with the index raised, $\partial^\nu\mathcal L = \partial^\mu\phi\,\partial^\nu\partial_\mu\phi - m^2\phi\,\partial^\nu\phi$. The second-derivative terms cancel pairwise, leaving $\partial_\mu T^{\mu\nu} = (\partial^2\phi + m^2\phi)\,\partial^\nu\phi$: zero by the Klein–Gordon equation. Off shell it is $-\mathrm{EL}\,\partial^\nu\phi$ with $\mathrm{EL} = -(\partial^2 + m^2)\phi$, as [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]] requires.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 3, eqs. (Tscalar), (T00), and "Checking conservation of T^{μν} directly" · Lecture 3, Example 3 and "Energy Density" · PS §2.2, eqs. (2.17)–(2.19)*

^ex-c1b-6-1

*Procedure:* [[P3 Noether's Procedure#^p3-4|P3, steps 4–6]]

## Energy and momentum of the free scalar fields in field form

> [!theorem] Theorem §C1b.6.7: Energy and Momentum of the Free Real Scalar Field
> For the free real scalar field ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]), with the canonical momentum $\pi = \dot\phi$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]]), the Noether charges of time and space translations ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]) are
>
> $$
> H = P^0 = \int d^3x\,T^{00} = \int d^3x\,\mathcal H = \int d^3x\,\Bigl[\tfrac12\pi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2\Bigr], \qquad \mathbf P = \bigl(P^1, P^2, P^3\bigr) = -\int d^3x\;\pi\,\nabla\phi = -\int d^3x\;\dot\phi\,\nabla\phi ,
> $$
>
> with $P^i = \int d^3x\,T^{0i}$ and $T^{0i} = -\pi\,\partial_i\phi$. Together they form $P^\mu = \int d^3x\,T^{0\mu} = (H, \mathbf P)$, conserved on solutions whose fields fall off at spatial infinity.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 3, eqs. (Tscalar), (T00), (Pfield) · PHY 513 Lecture 3, Part C ("Energy Density") · PS §2.2, eqs. (2.17)–(2.19) · Yu §1.7.2, eqs. (1.214)–(1.218)*

^thm-c1b-6-7

> [!derivation]- Derivation
> **Step 1** (the coefficient of the current index). With $\mathcal L = \tfrac12g^{\rho\sigma}\partial_\rho\phi\,\partial_\sigma\phi - \tfrac12m^2\phi^2$ and the dummy indices renamed away from $\mu$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]]),
>
> $$
> \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)} = \tfrac12g^{\rho\sigma}\bigl(\delta^\mu{}_\rho\,\partial_\sigma\phi + \partial_\rho\phi\,\delta^\mu{}_\sigma\bigr) = \partial^\mu\phi .
> $$
>
> For $\mu = 0$: $\partial\mathcal L/\partial(\partial_0\phi) = \partial^0\phi = g^{00}\partial_0\phi = \dot\phi$, since $g^{00} = +1$; this is the canonical momentum, $\pi = \partial\mathcal L/\partial\dot\phi = \dot\phi$ ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]]).
>
> **Step 2** (the tensor). Insert Step 1 into [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]] (one field component, no sum over $a$):
>
> $$
> T^{\mu\nu} = \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial^\nu\phi - g^{\mu\nu}\mathcal L = \partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L ,
> $$
>
> as in item 1 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-6-1|Example §C1b.6.1]]. Only the row $\mu = 0$ enters the charges (Theorem §C1b.6.6).
>
> **Step 3** ($T^{00}$, the energy density). Put $\mu = \nu = 0$: $\partial^0\phi\,\partial^0\phi = \dot\phi^2$ and $g^{00} = 1$, so $T^{00} = \dot\phi^2 - \mathcal L$. Write $\mathcal L$ without indices, $\partial_\rho\phi\,\partial^\rho\phi = \dot\phi^2 - (\nabla\phi)^2$, so $\mathcal L = \tfrac12\dot\phi^2 - \tfrac12(\nabla\phi)^2 - \tfrac12m^2\phi^2$, and expand all three terms:
>
> $$
> T^{00} = \dot\phi^2 - \tfrac12\dot\phi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2 = \tfrac12\dot\phi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2 .
> $$
>
> With $\dot\phi = \pi$ this is $\tfrac12\pi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2 = \mathcal H$, the Hamiltonian density of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]]: $T^{00} = \pi\dot\phi - \mathcal L$ is the Legendre transform of [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]]. Hence $P^0 = \int d^3x\,T^{00} = \int d^3x\,\mathcal H = H$.
>
> ⚑ By-product: the Noether charge of time translations and the Legendre-transform Hamiltonian are one function of the canonical data → [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-1|Remark: Why the 00 component is the Hamiltonian density]].
>
> **Step 4** ($T^{0i}$, index by index). Put $\mu = 0$, $\nu = i \in \{1, 2, 3\}$: $T^{0i} = \partial^0\phi\,\partial^i\phi - g^{0i}\mathcal L$. The metric is diagonal, $g^{0i} = 0$, so the $\mathcal L$ term drops. The upper spatial derivative is $\partial^i = g^{i\nu}\partial_\nu = g^{ii}\partial_i$ (no sum; only $\nu = i$ survives in a diagonal metric) $= -\partial_i$, because $g^{ii} = -1$. With $\partial^0\phi = \dot\phi = \pi$ (Step 1),
>
> $$
> T^{0i} = \pi\,\partial^i\phi = -\pi\,\partial_i\phi = -\dot\phi\,\partial_i\phi .
> $$
>
> **Step 5** (the momentum vector). $P^i = \int d^3x\,T^{0i} = -\int d^3x\,\pi\,\partial_i\phi$. Here $\partial_i = \partial/\partial x^i$ with $x^i = (x, y, z)$ the ordinary Cartesian coordinates, so $(\partial_1\phi, \partial_2\phi, \partial_3\phi)$ are the components of $\nabla\phi$, and the three charges are the components of
>
> $$
> \mathbf P = -\int d^3x\;\pi\,\nabla\phi = -\int d^3x\;\dot\phi\,\nabla\phi .
> $$
>
> ⚑ By-product: the minus sign is the metric's: it comes from raising the spatial index, $\partial^i = -\partial_i$, and makes $\mathbf P$ point along the direction of propagation of a wave → [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-2|Remark: Why P is the momentum]]. The lower-index charges $P_i = -P^i = \int d^3x\,\pi\,\partial_i\phi$ are the Noether charges of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]] with the generator $\Delta_i\phi = \partial_i\phi$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]): $\int d^3x\,\pi\,\Delta\phi$.
>
> **Step 6** (conservation). On solutions, $\partial_\mu T^{\mu\nu} = (\partial^2\phi + m^2\phi)\,\partial^\nu\phi = 0$ (item 5 of Example §C1b.6.1), i.e. $\partial_0T^{0\nu} = -\partial_iT^{i\nu}$. Integrate over a ball of radius $R$ and use the divergence theorem ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]): $\frac{d}{dt}\int_{r<R}d^3x\,T^{0\nu} = -\oint_{r=R}dS_i\,T^{i\nu}$, with $T^{i\nu} = \partial^i\phi\,\partial^\nu\phi - g^{i\nu}\mathcal L$ quadratic in the fields and their derivatives. If these fall off faster than $1/r$, $T^{i\nu}$ falls off faster than $1/r^2$, the surface integral vanishes as $R \to \infty$, and $dP^\nu/dt = 0$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]]).
>
> **Step 7** (collect). $P^0 = H$ (Step 3) and $P^i$ (Step 5) are the four charges $P^\nu = \int d^3x\,T^{0\nu}$ of the four translation currents, one per direction $\nu$ of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]]: $P^\mu = (H, \mathbf P)$, and with the index lowered $P_\mu = (H, -\mathbf P)$.
>
> **What the derivation shows**
> - Energy and momentum come from one row of one tensor; the same canonical momentum $\pi$ multiplies $\dot\phi$ in $\mathcal H$ and $-\nabla\phi$ in the momentum density.
> - Assumptions: the field equation (for conservation only; the expressions for $H$ and $\mathbf P$ hold for any configuration) and fall-off faster than $1/r$ of $\phi$, $\pi$, $\nabla\phi$.
> - Used next: the bracket form ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]]); the quantum field's $H$ and $\mathbf P$ in modes ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]).

^der-c1b-6-7

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-6-1|Example §C1b.6.1]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]

*Procedure:* [[P3 Noether's Procedure#^p3-6|P3, step 6]], [[P1 Canonical Quantization#^p1-3|P1, step 3]]

> [!theorem] Theorem §C1b.6.8: Energy and Momentum of the Free Complex Scalar Field
> For the free complex scalar field ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]]), with $\phi$ and $\phi^{\ast}$ as independent coordinates and the canonical momenta $\pi = \dot\phi^{\ast}$, $\pi^{\ast} = \dot\phi$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]), the Noether charges of translations are
>
> $$
> H = P^0 = \int d^3x\,\mathcal H = \int d^3x\,\bigl(\pi^{\ast}\pi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi\bigr), \qquad \mathbf P = -\int d^3x\,\bigl(\pi\,\nabla\phi + \pi^{\ast}\,\nabla\phi^{\ast}\bigr) = -\int d^3x\,\bigl(\dot\phi^{\ast}\,\nabla\phi + \dot\phi\,\nabla\phi^{\ast}\bigr) ,
> $$
>
> one term per canonical pair. $\mathbf P$ is real, and for $\phi = (\phi_1 + i\phi_2)/\sqrt2$ it is the sum of the momenta of the two real fields, $\mathbf P = -\int d^3x\sum_{j=1}^2\pi_j\nabla\phi_j$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7|Theorem §C1b.6.7]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (table after eq. (Tgeneral), complex-scalar row), Ch. 3 §3.4 ("The complex scalar, worked") · the momentum in field form written out here*

^thm-c1b-6-8

> [!derivation]- Derivation
> **Step 1** (the coefficients). $\mathcal L = g^{\rho\sigma}\partial_\rho\phi^{\ast}\,\partial_\sigma\phi - m^2\phi^{\ast}\phi$. With $\phi$ and $\phi^{\ast}$ independent ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]), only one factor of the kinetic term responds to each: $\partial\mathcal L/\partial(\partial_\mu\phi) = g^{\rho\mu}\partial_\rho\phi^{\ast} = \partial^\mu\phi^{\ast}$ and $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = g^{\mu\sigma}\partial_\sigma\phi = \partial^\mu\phi$; there is no factor $2$, because $\phi^{\ast}$ is not $\phi$. For $\mu = 0$ these are $\pi = \dot\phi^{\ast}$ and $\pi^{\ast} = \dot\phi$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]).
>
> **Step 2** (the tensor). [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]] sums over both components $a \in \{\phi, \phi^{\ast}\}$:
>
> $$
> T^{\mu\nu} = \partial^\mu\phi^{\ast}\,\partial^\nu\phi + \partial^\mu\phi\,\partial^\nu\phi^{\ast} - g^{\mu\nu}\mathcal L .
> $$
>
> **Step 3** ($T^{00}$). $\mathcal L = \dot\phi^{\ast}\dot\phi - \nabla\phi^{\ast}\cdot\nabla\phi - m^2\phi^{\ast}\phi$ without indices, so
>
> $$
> T^{00} = \dot\phi^{\ast}\dot\phi + \dot\phi\,\dot\phi^{\ast} - \dot\phi^{\ast}\dot\phi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi = \dot\phi^{\ast}\dot\phi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi ,
> $$
>
> and with $\dot\phi^{\ast}\dot\phi = \pi\pi^{\ast}$ (Step 1) this is $\mathcal H$ of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]: $P^0 = \int d^3x\,\mathcal H = H$.
>
> **Step 4** ($T^{0i}$). $g^{0i} = 0$ removes the $\mathcal L$ term, and $\partial^i = -\partial_i$ (Step 4 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-7|Derivation §C1b.6.7]]):
>
> $$
> T^{0i} = \partial^0\phi^{\ast}\,\partial^i\phi + \partial^0\phi\,\partial^i\phi^{\ast} = -\dot\phi^{\ast}\,\partial_i\phi - \dot\phi\,\partial_i\phi^{\ast} = -\bigl(\pi\,\partial_i\phi + \pi^{\ast}\,\partial_i\phi^{\ast}\bigr) .
> $$
>
> Integrating, $P^i = -\int d^3x\,(\pi\,\partial_i\phi + \pi^{\ast}\,\partial_i\phi^{\ast})$, the components of the $\mathbf P$ of the statement.
>
> **Step 5** (reality). The second term is the complex conjugate of the first, $(\pi\,\partial_i\phi)^{\ast} = \pi^{\ast}\,\partial_i\phi^{\ast}$, so the integrand is $2\operatorname{Re}(\pi\,\partial_i\phi)$ and $\mathbf P$ is real.
>
> **Step 6** (real components). With $\phi = (\phi_1 + i\phi_2)/\sqrt2$ and $\pi = (\pi_1 - i\pi_2)/\sqrt2$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]), expand all four products:
>
> $$
> \pi\,\partial_i\phi = \tfrac12(\pi_1 - i\pi_2)(\partial_i\phi_1 + i\partial_i\phi_2) = \tfrac12\bigl(\pi_1\partial_i\phi_1 + \pi_2\partial_i\phi_2\bigr) + \tfrac i2\bigl(\pi_1\partial_i\phi_2 - \pi_2\partial_i\phi_1\bigr) ,
> $$
>
> using $(-i)(i) = 1$. Twice the real part is $\pi_1\partial_i\phi_1 + \pi_2\partial_i\phi_2$; the cross terms are imaginary and cancel against their conjugates. So $\mathbf P = -\int d^3x\,(\pi_1\nabla\phi_1 + \pi_2\nabla\phi_2)$, the momenta of two real fields ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7|Theorem §C1b.6.7]]), as $H$ is the sum of two real Hamiltonians (Step 5 of [[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-3|Derivation §C1b.4.3]]).
>
> **Step 7** (conservation). As in Step 6 of Derivation §C1b.6.7: $\partial_\mu T^{\mu\nu} = 0$ on solutions ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]]) and the surface flux vanishes for fields falling off faster than $1/r$.
>
> ⚑ By-product: the momentum has one term per canonical pair, $\pi\nabla\phi$ for $(\phi, \pi)$ and $\pi^{\ast}\nabla\phi^{\ast}$ for $(\phi^{\ast}, \pi^{\ast})$, as the Legendre transform has one term per coordinate; after quantization both become operator products whose ordering does not matter for $\mathbf P$ → [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]].
>
> **What the derivation shows**
> - The complex field carries the momentum of its two real components; nothing new beyond bookkeeping, unlike the $U(1)$ charge, which has no real-field analogue ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]).
> - Assumptions: as in Theorem §C1b.6.7; $\phi$, $\phi^{\ast}$ treated as independent coordinates.
> - Used next: the quantized complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]]).

^der-c1b-6-8

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-5|Theorem §C1b.6.5]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-7|Theorem §C1b.6.7]]

*Procedure:* [[P1 Canonical Quantization#^p1-3|P1, step 3]]

> [!theorem] Theorem §C1b.6.9: The Field Momentum Generates Spatial Translations
> Let $\mathbf P = -\int d^3x\sum_a\pi_a\nabla\phi_a$ ([[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]]), with fields and momenta differentiable and falling off at spatial infinity, and take Poisson brackets as in [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]]. Then
> 1. $\{\phi_a(\mathbf x), \mathbf P\} = -\nabla\phi_a(\mathbf x)$ and $\{\pi_a(\mathbf x), \mathbf P\} = -\nabla\pi_a(\mathbf x)$, identities after smearing with test functions;
> 2. with $\{\phi_a, H\} = \dot\phi_a$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]]) and $P^0 = H$, in covariant form $\{\phi_a(x), P^\mu\} = \partial^\mu\phi_a(x)$, and likewise for $\pi_a$;
> 3. for a constant $a^\mu$, the first-order flow generated by $\varepsilon\,a_\mu P^\mu$ shifts the argument, $\phi_a(x) + \varepsilon\{\phi_a(x), a_\mu P^\mu\} = \phi_a(x + \varepsilon a) + O(\varepsilon^2)$;
> 4. $\{\mathbf P, H\} = 0$ when $\mathcal H$ does not depend on $\mathbf x$ explicitly.
>
> *Source: the particle version [[§B8.1 Poisson Brackets#^thm-b8-1-5|CM Theorem §B8.1.5]] (a conserved quantity generates a symmetry) · the user's PHY 513 notes, Ch. 3 §3.4 ("Canonical brackets") and §3.5 (eq. (Pfield)) · the field-momentum brackets written out here*

^thm-c1b-6-9

> [!derivation]- Derivation
> Write $P^i = -\int d^3z\sum_c\pi_c(\mathbf z)\,\partial_i\phi_c(\mathbf z)$ on one time slice.
>
> **Step 1** ($\delta P^i/\delta\pi_c$). Vary $\pi_c \to \pi_c + \varepsilon\zeta_c$ with $\zeta_c$ a test function on $\mathbb R^3$, $\phi$ fixed. $P^i$ is linear in $\pi$, so $\frac{d}{d\varepsilon}P^i\big|_0 = -\int d^3z\sum_c\zeta_c\,\partial_i\phi_c$, and by [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|Def. §C1b.2.4]] (on a slice)
>
> $$
> \frac{\delta P^i}{\delta\pi_c(\mathbf z)} = -\partial_i\phi_c(\mathbf z) .
> $$
>
> **Step 2** ($\delta P^i/\delta\phi_c$). Vary $\phi_c \to \phi_c + \varepsilon\eta_c$, $\pi$ fixed: $\frac{d}{d\varepsilon}P^i\big|_0 = -\int d^3z\sum_c\pi_c\,\partial_i\eta_c$. Move the derivative with the product rule, $\pi_c\,\partial_i\eta_c = \partial_i(\pi_c\eta_c) - (\partial_i\pi_c)\,\eta_c$; the first term integrates to zero because $\pi_c\eta_c$ has compact support ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]; [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]). Hence $\frac{d}{d\varepsilon}P^i\big|_0 = +\int d^3z\sum_c(\partial_i\pi_c)\,\eta_c$ and
>
> $$
> \frac{\delta P^i}{\delta\phi_c(\mathbf z)} = +\partial_i\pi_c(\mathbf z) .
> $$
>
> ⚑ By-product: the sign flips because the integration by parts moved $\partial_i$ from the variation onto $\pi$; this is where $\pi$ must be differentiable, an assumption of the statement.
>
> **Step 3** (part 1 for the field). Smear: $\phi_a(f) = \int d^3x\,f\phi_a$ has $\delta\phi_a(f)/\delta\phi_c = \delta_{ac}f$ and $\delta\phi_a(f)/\delta\pi_c = 0$ ([[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-5|Derivation §C1b.4.5]], step 1). Insert into the bracket of [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]]; the sum over $c$ eliminates $c$ against $\delta_{ac}$:
>
> $$
> \{\phi_a(f), P^i\} = \sum_c\int d^3z\,\Bigl(\delta_{ac}f(\mathbf z)\cdot\bigl(-\partial_i\phi_c(\mathbf z)\bigr) - 0\cdot\partial_i\pi_c(\mathbf z)\Bigr) = -\int d^3z\,f(\mathbf z)\,\partial_i\phi_a(\mathbf z) .
> $$
>
> In kernel form, $\{\phi_a(\mathbf x), P^i\} = -\partial_i\phi_a(\mathbf x)$.
>
> **Step 4** (part 1 for the momentum). $\pi_a(g) = \int d^3x\,g\pi_a$ has $\delta\pi_a(g)/\delta\phi_c = 0$ and $\delta\pi_a(g)/\delta\pi_c = \delta_{ac}g$, so only the second term of the bracket survives:
>
> $$
> \{\pi_a(g), P^i\} = \sum_c\int d^3z\,\Bigl(0\cdot\bigl(-\partial_i\phi_c\bigr) - \delta_{ac}g(\mathbf z)\,\partial_i\pi_c(\mathbf z)\Bigr) = -\int d^3z\,g(\mathbf z)\,\partial_i\pi_a(\mathbf z) ,
> $$
>
> i.e. $\{\pi_a(\mathbf x), P^i\} = -\partial_i\pi_a(\mathbf x)$. Since $\partial_i = \partial/\partial x^i$ are the Cartesian components of $\nabla$, Steps 3–4 are part 1.
>
> **Step 5** (part 2). Raise the index: $\partial^i = g^{ii}\partial_i = -\partial_i$ (Step 4 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-7|Derivation §C1b.6.7]]), so Step 3 reads $\{\phi_a, P^i\} = \partial^i\phi_a$. For $\mu = 0$: $P^0 = H$ (Theorem §C1b.6.6) and $\{\phi_a, H\} = \dot\phi_a = \partial_0\phi_a = \partial^0\phi_a$, since $g^{00} = 1$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]]). The four relations combine into $\{\phi_a(x), P^\mu\} = \partial^\mu\phi_a(x)$; the same steps with Step 4 and $\{\pi_a, H\} = \dot\pi_a$ give it for $\pi_a$.
>
> ⚑ By-product: the covariant form $\{\phi, P^\mu\} = \partial^\mu\phi$ is what canonical quantization turns, with $\{F, G\} \to -i[F, G]$ ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-5|§C1b.4, Remark: From brackets to commutators]]), into $[\phi, P^\mu] = i\partial^\mu\phi$, the statement that $P^\mu$ generates translations of the quantum field → [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]]; for the Dirac field, [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]].
>
> **Step 6** (part 3). With $a_\mu P^\mu = a^0H - \mathbf a\cdot\mathbf P$ (lowering the index, $a_i = -a^i$), bilinearity of the bracket and Step 5 give $\{\phi_a, a_\mu P^\mu\} = a_\mu\partial^\mu\phi_a = a^\mu\partial_\mu\phi_a$, the contraction being a plain sum ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum]]). By Taylor's theorem ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]), $\phi_a(x + \varepsilon a) = \phi_a(x) + \varepsilon a^\mu\partial_\mu\phi_a(x) + O(\varepsilon^2)$: part 3. ⚑ By-product: the flow moves the argument by $+\varepsilon a$, i.e. it is the field law of [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]] for the translation $x' = x - \varepsilon a$; for $a = (1, \mathbf 0)$ it is time evolution by $\varepsilon$.
>
> **Step 7** (part 4, for the free real field). $\delta H/\delta\pi = \pi$ and $\delta H/\delta\phi = m^2\phi - \nabla^2\phi$ ([[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|Example §C1b.4.1]]); with Steps 1–2,
>
> $$
> \{P^i, H\} = \int d^3z\,\Bigl(\partial_i\pi\cdot\pi - \bigl(-\partial_i\phi\bigr)\bigl(m^2\phi - \nabla^2\phi\bigr)\Bigr) = \int d^3z\,\Bigl(\partial_i\bigl(\tfrac12\pi^2\bigr) + \partial_i\bigl(\tfrac12m^2\phi^2\bigr) - \partial_i\phi\,\nabla^2\phi\Bigr) .
> $$
>
> The first two terms are total derivatives and integrate to zero (fall-off). In the third, integrate by parts in $z^j$: $\int\partial_i\phi\,\partial_j\partial_j\phi = -\int\partial_j\partial_i\phi\,\partial_j\phi = -\int\partial_i\bigl(\tfrac12(\nabla\phi)^2\bigr) = 0$. So $\{P^i, H\} = 0$, and by [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]] $d\mathbf P/dt = 0$, as Noether's theorem says. In general every term of $\{P^i, H\}$ assembles into $\int d^3z\,\partial_i(\cdots)$ exactly when $\mathcal H$ has no explicit $\mathbf z$-dependence.
>
> **What the derivation shows**
> - $\mathbf P$ acts on the canonical data as $-\nabla$, as $H$ acts as $\partial_t$: the field momentum is the generator of spatial translations in the same sense in which the Hamiltonian generates time evolution ([[§B8.1 Poisson Brackets#^thm-b8-1-5|CM Theorem §B8.1.5]]).
> - Assumptions: differentiable $\pi$ (Step 2) and fall-off at infinity (Steps 2 and 7).
> - Used next: the quantum generators ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]]), the Dirac field ([[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]]).

^der-c1b-6-9

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|Def. §C1b.2.4]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-3|Def. §C1b.4.3]], [[§C1b.4 Hamiltonian Field Theory#^der-c1b-4-5|Derivation §C1b.4.5]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-6|Theorem §C1b.4.6]], [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|Example §C1b.4.1]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]

> [!remark] Remark: Why P is the momentum
> - *On a wave.* The real solution $\phi = A\cos\theta$, $\theta = \omega t - \mathbf k\cdot\mathbf x$, $\omega = \sqrt{\mathbf k^2 + m^2}$, has $\pi = \dot\phi = -A\omega\sin\theta$ and $\nabla\phi = A\mathbf k\sin\theta$, so the momentum density is $-\pi\nabla\phi = A^2\omega\,\mathbf k\sin^2\theta$ and the energy density $\mathcal H = \tfrac12A^2(\omega^2 + \mathbf k^2)\sin^2\theta + \tfrac12m^2A^2\cos^2\theta$. Averaged over a period ($\langle\sin^2\rangle = \langle\cos^2\rangle = \tfrac12$): $\langle\mathcal H\rangle = \tfrac14A^2(\omega^2 + \mathbf k^2 + m^2) = \tfrac12A^2\omega^2$ and $\langle-\pi\nabla\phi\rangle = \tfrac12A^2\omega\,\mathbf k$. The momentum points along the propagation, and momentum per energy is $\mathbf k/\omega$, the group velocity $\partial\omega/\partial\mathbf k$. A wave packet narrow in $\mathbf k$ with energy $N\omega$ carries momentum $N\mathbf k$: per quantum $E = \omega$, $\mathbf p = \mathbf k$ ($\hbar = 1$), the particles of [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]].
> - *Not the canonical momentum.* $\pi$ is conjugate to the field value $\phi(\mathbf x)$ at one point, a momentum in field space with $[\pi] = 2$; the momentum carried through space is $T^{0i} = -\pi\,\partial_i\phi$, with $[T^{0i}] = 4$, built from $\pi$ and the generator $-\partial_i\phi$ of the translation it belongs to ([[§C1b.4 Hamiltonian Field Theory#^cau-c1b-4-1|§C1b.4, Caution: What the conjugate momentum is not]]). This is the pattern of every Noether charge, $\int d^3x\,\pi\,\Delta\phi$ (Step 5 of [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-6-7|Derivation §C1b.6.7]]), and in mechanics the total momentum of $N$ particles is likewise $\sum_jp_j$ contracted with the translation of each coordinate.
> - *The electromagnetic analogue.* For the Maxwell field the momentum density is the Poynting vector, $\hat T^{0i} = (\mathbf E\times\mathbf B)^i$ in Heaviside–Lorentz units ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-2|Example §C1b.7.2]]; in SI $T^{0i} = S_i/c = c\,g_i$, [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-3|EM Theorem §C1.5.3]]), while the momentum canonically conjugate to $A_i$ is the electric field ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|§C1b.4, Remark: Constraints and first-order Lagrangians]]): there too the momentum of the field is built from the canonical momentum, not equal to it.
> - *No ordering choice after quantization.* In modes $\mathbf P = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,a^\dagger_{\mathbf p}a_{\mathbf p}$ with no constant ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]): the would-be zero-point term $\propto\int d^3p\,\mathbf p$ vanishes by reflection symmetry, unlike the zero-point energy of $H$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eq. (Pfield), and Ch. 4 §4.7 · PS §2.2, eq. (2.19), and §2.3, eq. (2.33) · the plane-wave averages worked out here*

^rem-c1b-6-2

> [!remark] Remark: The canonical tensor of the standard fields
> Running [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-6-2|Def. §C1b.6.2]] on the standard Lagrangians:
>
> | field | $\mathcal L$ | $\partial\mathcal L/\partial(\partial_\mu\phi_a)$ | canonical $T^{\mu\nu}$ | symmetric |
> | --- | --- | --- | --- | --- |
> | real scalar | $\frac12(\partial\phi)^2 - \frac12m^2\phi^2$ | $\partial^\mu\phi$ | $\partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L$ | yes |
> | complex scalar | $\partial_\rho\phi^*\partial^\rho\phi - m^2\phi^*\phi$ | $\partial^\mu\phi^*$ (for $\phi$), $\partial^\mu\phi$ (for $\phi^*$) | $\partial^\mu\phi^*\partial^\nu\phi + \partial^\mu\phi\,\partial^\nu\phi^* - g^{\mu\nu}\mathcal L$ | yes |
> | vector | $-\frac14F_{\rho\sigma}F^{\rho\sigma}$ | $-F^{\mu\rho}$ (for $A_\rho$) | $-F^{\mu\rho}\partial^\nu A_\rho + \frac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma}$ | no |
> | Dirac | $\bar\psi(i\gamma^\rho\partial_\rho - m)\psi$ | $i\bar\psi\gamma^\mu$ (for $\psi$), $0$ (for $\bar\psi$) | $i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L$ | no |
>
> Checks on $T^{00}$: the complex scalar gives $\dot\phi^*\dot\phi + \dot\phi\dot\phi^* - \mathcal L = \lvert\dot\phi\rvert^2 + \lvert\nabla\phi\rvert^2 + m^2\lvert\phi\rvert^2$, its Hamiltonian density ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]); the vector gives the canonical tensor of [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-2|Example §C1b.7.2]]; the Dirac field gives $i\psi^\dagger\partial_t\psi$, and since the Dirac equation sets $\mathcal L = 0$ on shell, $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi$ there ([[§C5a.5 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-5-5|Theorem §C5a.5.5]]). The pattern is exact: a scalar gives a symmetric $T$ because $\partial^\mu\phi\,\partial^\nu\phi$ is symmetric by inspection; a field with an index gives a non-symmetric canonical $T$, because $\partial\mathcal L/\partial(\partial_\mu\phi_a)$ carries the field's own index structure ($F^{\mu\rho}$, $\gamma^\mu$), which does not pair symmetrically with $\partial^\nu$. [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]] explains the pattern and [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-4|Theorem §C1b.7.4]] repairs it.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, table after eq. (Tgeneral)*

^rem-c1b-6-3

> [!remark]- Connections
> - The field momentum generates spatial translations through the Poisson bracket exactly as $H$ generates time evolution; quantized, the same statement is $[\phi, P^\mu] = i\partial^\mu\phi$ for the scalar and $[\psi, \mathbf P] = -i\nabla\psi$ for the Dirac field — [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-9|Theorem §C1b.6.9]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-13|Theorem §C3.5.13]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]], [[§B8.1 Poisson Brackets#^thm-b8-1-5|CM Theorem §B8.1.5]].
> - The momentum density of the field is not its canonical momentum but $\pi$ contracted with the translation generator, as the electromagnetic momentum density is the Poynting vector rather than the momentum conjugate to $A_i$ — [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-6-2|Remark: Why P is the momentum]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-7-2|Example §C1b.7.2]], [[§C1.5 The Electromagnetic Energy–Momentum Tensor#^thm-c1-5-3|EM Theorem §C1.5.3]].
> - The mechanics of a closed system ([[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-5|CM Theorem §B6.4.5]]) has the same four conclusions from homogeneity and isotropy: momentum, angular momentum, energy, and the uniform motion of the centre of mass; here each is the charge of one component of $T^{\mu\nu}$ or $\mathcal M^{\mu\nu\rho}$.
> - The Klein–Gordon field's $T^{\mu\nu}$ and energy density with $c$ restored are quoted in [[§B4.1 The Klein–Gordon Equation|REL §B4.1]] (Connections), and the electromagnetic energy–momentum tensor is anticipated in [[§B4.2 The Electromagnetic Field Tensor|REL §B4.2]]; this section is their home.
> - After quantization $H$ and $\mathbf P$ are the normal-ordered charges of this section ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]]); the zero-point energy is the ordering constant of $\int d^3x\,T^{00}$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]); they generate translations of states as momentum does in quantum mechanics ([[§C2.2 Translation and Momentum as Its Generator|QM §C2.2]]).
> - Math: Jacobi's formula ([[Jacobi's Formula]], [[§12 The Classical Groups Are Topological Manifolds#^prop-12-1|591 Prop. §12.1]]) for the Jacobian; the chain rule [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]].
