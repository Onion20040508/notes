---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.4 Hamiltonian Field Theory]] · ↑ [[· C1b Classical Field Theory]] · [[§C1b.6 Conserved Charges and Internal Symmetries]] →

*Sources: the user's PHY 513 notes, Ch. 3 §3.5 (Definitions; The procedure; The table of examples; The theorem and its proof; From current to charge; Examples I) · PHY 513 Lecture 3 (Larsen), Part C, and Lecture 8, Part B (the Dirac Lagrangian, for Example §C1b.5.2); Problem Set 2, Problem 3, with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2 and §3.4, p. 51 · Yu Zhao-Huan, 量子场论讲义, §§1.6.2, 1.7.1, 1.7.4 · the user's pre-course notes, §1.7.*

Which quantities does a field theory conserve, and why? Noether's theorem answers: one conserved current for every continuous symmetry of the action. It starts from the action and the Euler–Lagrange equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]) and from the particle version in mechanics ([[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-2|CM Theorem §B6.4.2]]), and adds what fields need: a local conservation law $\partial_\mu j^\mu = 0$ at every point, and a charge that is conserved only up to what flows out through the boundary. Every object is defined before it is used (the instances of δ, the generator and the symmetry variation $\delta\phi = \alpha\Delta\phi$); then how $\delta\mathcal L$ is computed, by substitution or by the chain rule, and the test that decides whether a transformation is a symmetry and defines $\mathcal J$; the algorithm is [[P3 Noether's Procedure]]; then come the theorem with its proof and what the same algebra gives when the test fails. Charges, improvement terms and the internal-symmetry examples are [[§C1b.6 Conserved Charges and Internal Symmetries|§C1b.6]]. Spacetime symmetries, where the point moves, are [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]].

## The objects

> [!definition] Definition §C1b.5.1: The Instances of δ
> Noether's theorem uses one symbol for several first-order changes. All are differentials (linear, Leibniz, chain rule); they differ in what is changed and by how much:
>
> | instance | what is changed | by how much |
> | --- | --- | --- |
> | $\delta\phi(x) = \tilde\phi(x) - \phi(x)$ | the field value at fixed $x$ | an arbitrary small function (action principle) |
> | $\delta\phi(x) = \alpha\,\Delta\phi(x)$ | the field value at fixed $x$ | the shape of a given transformation (Noether) |
> | $\delta x^\mu = x'^\mu - x^\mu$ | the coordinates of a point | the displacement of a spacetime transformation |
> | $\bar\delta\phi = \phi'(x) - \phi(x)$ | the field value at fixed $x$ | induced by a transformation that also moves the point |
> | $\delta\phi = \phi'(x') - \phi(x)$ | the field, compared at the moved point | the total change when the point moves |
> | $\delta(\partial_\mu\phi)$, $\delta\mathcal L$, $\delta S$ | derived quantities | what the change of the inputs implies, by the chain rule |
>
> At fixed coordinates δ commutes with $\partial_\mu$; when the point moves only $\bar\delta$ does ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|Theorem §C1b.7.1]]). In this section the point never moves, and $\alpha\Delta\phi$ is a fixed-argument change: $\alpha\Delta\phi = \bar\delta\phi$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Definition "The instances of δ used by Noether's theorem" · Yu §1.7.1, eqs. (1.180), (1.189)*

^def-c1b-5-1

The first row is the variation of the action principle ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]); the second row, the symmetry variation, is [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]] (δ carries the parameter, Δ does not); the rows that move the point are used from [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum|§C1b.7]] on.

> [!definition] Definition §C1b.5.2: Continuous Transformation; Parameters
> Let $\mathcal L(\phi_i, \partial_\mu\phi_i)$ depend on $N$ real field components $\phi_1, \dots, \phi_N$ (a complex field counts as the pair $\phi$, $\phi^{\ast}$). A **continuous transformation** is a family $\phi_i \mapsto \phi'_i$ labelled by real **parameters** $\alpha^1, \dots, \alpha^{\dim G}$, all zero giving the identity. The parameters are **infinitesimal** (only first order is used) and **global** (constant over spacetime).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Definition "Transformation, parameter, generator", eq. (symdef) · PS §2.2, eq. (2.9) · Lecture 3, Part C*

^def-c1b-5-2

> [!definition] Definition §C1b.5.3: Generator of a Continuous Transformation
> The **generators** of a continuous transformation ([[§C1b.5 Noether's Theorem#^def-c1b-5-2|Def. §C1b.5.2]]) are its first-order coefficients at a fixed point $x$,
>
> $$
> \phi'_i(x) = \phi_i(x) + \alpha^a\,\Delta_a\phi_i(x) + O(\alpha^2), \qquad \Delta_a\phi_i \equiv \frac{\partial\phi'_i(x)}{\partial\alpha^a}\Big|_{\alpha = 0} ,
> $$
>
> one per pair (parameter $a$, field $i$); $\Delta_a\phi_i$ may depend on the fields, their derivatives and $x$. With one field and one parameter, $\phi \to \phi + \alpha\Delta\phi$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Definition "Transformation, parameter, generator", eq. (symdef) · PS §2.2, eq. (2.9) · Lecture 3, Part C*

^def-c1b-5-3

> [!definition] Definition §C1b.5.4: Symmetry Variation
> The **symmetry variation** of the fields under a continuous transformation ([[§C1b.5 Noether's Theorem#^def-c1b-5-2|Def. §C1b.5.2]]) is the first-order part of their change at a fixed point $x$,
>
> $$
> \delta\phi_i(x) \equiv \alpha^a\,\Delta_a\phi_i(x), \qquad \phi'_i(x) - \phi_i(x) = \delta\phi_i(x) + O(\alpha^2) ,
> $$
>
> with $\Delta_a\phi_i$ the generators ([[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]]). $\delta\phi_i$ contains the parameters and is linear in them; $\Delta_a\phi_i$ is $\delta\phi_i$ with the parameter stripped off and does not depend on $\alpha$. For one parameter, $\delta\phi = \alpha\Delta\phi$. This is the second instance of δ in [[§C1b.5 Noether's Theorem#^def-c1b-5-1|Def. §C1b.5.1]].
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Definition "Transformation, parameter, generator", eq. (symdef) ("so $\alpha^a\Delta_a\phi_i$ is the second instance of variation in the table") · PHY 513 Lecture 3, Part C ("Symmetry variation $\delta\phi = \alpha\Delta\phi$") · PS §2.2, eq. (2.9)*

^def-c1b-5-4

> [!remark] Remark: δ and Δ side by side, and why only first order
> Each finite transformation is written at the old point and expanded in its parameter; $\delta\phi$ is the first-order term and $\Delta\phi$ its coefficient (the expansions are derived in [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]):
>
> | transformation | $\phi'(x)$, finite | $\delta\phi$ | $\Delta\phi$ |
> | --- | --- | --- | --- |
> | shift | $\phi + \alpha$ | $\alpha$ | $1$ |
> | U(1) phase | $e^{i\alpha}\phi$; $e^{-i\alpha}\phi^{\ast}$ | $i\alpha\phi$; $-i\alpha\phi^{\ast}$ | $i\phi$; $-i\phi^{\ast}$ |
> | SO(2) rotation of $(\phi_1, \phi_2)$ | $\cos\alpha\,\phi_1 - \sin\alpha\,\phi_2$; $\sin\alpha\,\phi_1 + \cos\alpha\,\phi_2$ | $-\alpha\phi_2$; $\alpha\phi_1$ | $-\phi_2$; $\phi_1$ |
> | translation $x \to x - a$ | $\phi(x + a)$ | $a^\nu\partial_\nu\phi$ | $\Delta_\nu\phi = \partial_\nu\phi$, one per $a^\nu$ |
>
> With several parameters, $\delta\phi_i = \alpha^a\Delta_a\phi_i$ is one function and the $\Delta_a\phi_i$ are its coefficients along the independent parameters, read off by setting all but one $\alpha^a$ to zero. The $O(\alpha^2)$ remainder, for example $-\frac12\alpha^2\phi$ in $e^{i\alpha}\phi = \phi + i\alpha\phi - \frac12\alpha^2\phi + \dots$, is dropped for two reasons. First, the current is the coefficient of $\alpha$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]), and higher orders cannot change a first-order coefficient. Second, nothing about the symmetry is lost: a continuous symmetry is decided near the identity, because a first-order test passed by every configuration propagates along the whole one-parameter family ([[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]]). The current contains $\Delta\phi$ and not $\delta\phi$ because the size of $\alpha$ is arbitrary and must drop out of a conservation law.

^rem-c1b-5-1

> [!remark] Remark: The sign of a parameter is a convention
> Transforming by $+\alpha$ or by $-\alpha$ is a choice. It flips the sign of $\Delta\phi$ and of the current, never the conservation law, and every overall-sign disagreement between sources on Noether currents traces to it: the U(1) current ([[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|Caution: Sign and normalization of the U(1) current]]) and the translations ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^cau-c1b-7-1|§C1b.7, Caution: One picture at a time; the sign of the displacement]]). Nothing is lost by working to first order: a finite transformation of a connected family is a composition of small ones. "Global" is what lets the parameter pass through $\partial_\mu$ in the proof of [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]; a parameter $\alpha(x)$ is a gauge transformation ([[§C1b.6 Conserved Charges and Internal Symmetries#^rem-c1b-6-2|Remark: Global, internal, and what a local phase would need]]). The parameters drop out of every final formula, which is why the current contains $\Delta\phi$ and not $\delta\phi = \alpha\Delta\phi$.

^rem-c1b-5-2

> [!theorem] Theorem §C1b.5.1: Generators of the Standard Transformations
> For the transformations of this course (Def. §C1b.5.2):
>
> | transformation | parameters | generator |
> | --- | --- | --- |
> | shift, $\phi' = \phi + \alpha$ | $\alpha$ | $\Delta\phi = 1$ |
> | phase, $\phi' = e^{i\alpha}\phi$, $\phi^{*\prime} = e^{-i\alpha}\phi^*$ | $\alpha$ | $\Delta\phi = i\phi$, $\Delta\phi^* = -i\phi^*$ |
> | phases with charges $q_n$, $\phi'_n = e^{iq_n\alpha}\phi_n$ | $\alpha$ | $\Delta\phi_n = iq_n\phi_n$ |
> | rotation of two real fields by the angle $\alpha$ | $\alpha$ | $\Delta\phi_1 = -\phi_2$, $\Delta\phi_2 = \phi_1$ |
> | two independent shifts, $\phi'_k = \phi_k + \alpha^k$ | $\alpha^1$, $\alpha^2$ | $\Delta_k\phi_l = \delta_{kl}$ |
> | translation $x \to x - a$, any field | $a^\nu$ (four) | $\Delta_\nu\phi = \partial_\nu\phi$ |
> | Lorentz $x \to \Lambda x$, $\Lambda = 1 + \omega$, scalar field | $\omega_{\mu\nu}$ (six) | $\Delta^{\mu\nu}\phi = x^\mu\partial^\nu\phi - x^\nu\partial^\mu\phi$, entering as $\tfrac12\omega_{\mu\nu}\Delta^{\mu\nu}\phi$ |
> | scale, $\phi'(x) = \lambda\,\phi(\lambda x)$, $\lambda = e^\alpha$ | $\alpha$ | $\Delta\phi = \phi + x^\mu\partial_\mu\phi$ |
>
> Derivatives are not transformed independently: $\Delta(\partial_\mu\phi) = \partial_\mu(\Delta\phi)$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, "Computing Δφ (step 1)" · PS §2.2, eq. (2.15) and p. 18 · Lecture 3, Examples 1–3 · Yu §1.7.4, eq. (1.258)*

^thm-c1b-5-1

> [!derivation]- Derivation
> In each case: write $\phi'$ at the old point $x$, expand to first order in the parameter, read off the coefficient (Def. §C1b.5.2).
>
> **1. Shift.** $\phi'(x) = \phi(x) + \alpha$, so $\partial\phi'/\partial\alpha = 1$ at every $\alpha$: $\Delta\phi = 1$.
>
> **2. Phase.** The exponential series gives $e^{i\alpha} = 1 + i\alpha + O(\alpha^2)$, so $\phi' = \phi + i\alpha\phi + O(\alpha^2)$ and $\Delta\phi = i\phi$; conjugating, $\phi^{\ast \prime} = \phi^{\ast} - i\alpha\phi^{\ast} + O(\alpha^2)$, $\Delta\phi^{\ast} = -i\phi^{\ast}$. With charges, $e^{iq_n\alpha} = 1 + iq_n\alpha + O(\alpha^2)$ gives $\Delta\phi_n = iq_n\phi_n$.
>
> **3. Rotation of two real fields.** $\phi'_1 = \cos\alpha\,\phi_1 - \sin\alpha\,\phi_2$, $\phi'_2 = \sin\alpha\,\phi_1 + \cos\alpha\,\phi_2$. With $\cos\alpha = 1 + O(\alpha^2)$, $\sin\alpha = \alpha + O(\alpha^3)$: $\phi'_1 = \phi_1 - \alpha\phi_2$, $\phi'_2 = \phi_2 + \alpha\phi_1$, so $\Delta\phi_1 = -\phi_2$, $\Delta\phi_2 = \phi_1$. It is the phase in real components: with $\phi = (\phi_1 + i\phi_2)/\sqrt2$,
>
> $$
> e^{i\alpha}(\phi_1 + i\phi_2) = (\cos\alpha + i\sin\alpha)(\phi_1 + i\phi_2) = (\cos\alpha\,\phi_1 - \sin\alpha\,\phi_2) + i(\sin\alpha\,\phi_1 + \cos\alpha\,\phi_2) ,
> $$
>
> whose real and imaginary parts are $\phi'_1$ and $\phi'_2$.
>
> **4. Two independent shifts.** $\Delta_1\phi_1 = \partial(\phi_1 + \alpha^1)/\partial\alpha^1 = 1$, $\Delta_1\phi_2 = \partial(\phi_2 + \alpha^2)/\partial\alpha^1 = 0$, and likewise $\Delta_2\phi_1 = 0$, $\Delta_2\phi_2 = 1$: each parameter moves one field.
>
> **5. Translation.** The lecture's translation $x \to x - a$ is the Poincaré map of [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]] with $\Lambda = 1$ and translation parameter $-a$. The infinitesimal form of the field laws ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]) with $a \to -a$ gives
>
> $$
> \phi'(x) = \phi(x) + a^\nu\partial_\nu\phi(x) + O(a^2) ,
> $$
>
> the first-order form of $\phi'(x) = \phi(x + a)$. Hence $\partial\phi'/\partial a^\nu|_{a=0} = \partial_\nu\phi$: four parameters, four generators. Translations carry no matrix ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]), so every component of every field has the same generator, $\Delta_\nu\phi_i = \partial_\nu\phi_i$. ⚑ By-product: the argument shifts opposite to the coordinates; a bump at $x_0$ in $\phi$ sits at $x_0 - a$ in $\phi'$, because every label moved by $-a$ → [[§C1b.5 Noether's Theorem#^rem-c1b-5-2|Remark: The sign of a parameter is a convention]].
>
> **6. Lorentz.** For $x \to \Lambda x$, $\Lambda = 1 + \omega$, no translation, the same theorem (scalar case; it lowers the index on $\omega$ and antisymmetrizes, using $\omega_{\mu\nu} = -\omega_{\nu\mu}$, [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]]) gives
>
> $$
> \phi'(x) = \phi(x) + \tfrac12\omega_{\mu\nu}\bigl(x^\mu\partial^\nu\phi - x^\nu\partial^\mu\phi\bigr) + O(\omega^2) .
> $$
>
> The independent parameters are the six $\omega_{\mu\nu}$ with $\mu < \nu$; since both $\omega_{\mu\nu}$ and $\Delta^{\mu\nu}\phi$ are antisymmetric, $\tfrac12\sum_{\mu,\nu}\omega_{\mu\nu}\Delta^{\mu\nu}\phi = \sum_{\mu<\nu}\omega_{\mu\nu}\Delta^{\mu\nu}\phi$, so $\Delta^{\mu\nu}\phi = x^\mu\partial^\nu\phi - x^\nu\partial^\mu\phi$ is the generator attached to $\omega_{\mu\nu}$. ⚑ By-product: the factor $\tfrac12$ compensates the double counting of each antisymmetric pair; the same convention runs through [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]] and the field law $D = 1 + \tfrac12\omega_{\mu\nu}S^{\mu\nu}$ ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]). ⚑ By-product: this generator depends on $x$ explicitly, and a field with components gets an extra matrix term, the spin part of the same theorem → [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]].
>
> **7. Scale.** With $\lambda = e^\alpha = 1 + \alpha + O(\alpha^2)$ and the prefactor $\lambda^{[\phi]} = \lambda$ for a field of mass dimension 1 ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]): $\phi'(x) = (1 + \alpha)\,\phi(x + \alpha x) = (1 + \alpha)\bigl(\phi + \alpha x^\mu\partial_\mu\phi\bigr) + O(\alpha^2) = \phi + \alpha(\phi + x^\mu\partial_\mu\phi) + O(\alpha^2)$, so $\Delta\phi = \phi + x^\mu\partial_\mu\phi$. Whether it is a symmetry is not decided here → [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-4|§C1b.8, ★ Remark: Dilatations]].
>
> **8. Derivatives.** $\phi'$ is a fixed-argument change and the parameter is constant, so $\partial_\mu\phi' = \partial_\mu\phi + \alpha\,\partial_\mu(\Delta\phi) + O(\alpha^2)$: $\Delta(\partial_\mu\phi) = \partial_\mu(\Delta\phi)$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]]).
>
> **What the derivation shows**
> - Internal transformations (rows 1–5) have generators without derivatives or $x$; spacetime ones contain $\partial\phi$ and possibly $x$, because the point moved.
> - A point-moving transformation is first rewritten as a change at the old point, which the field laws do ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]); [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|Theorem §C1b.7.1]] does it for any displacement.
> - Assumptions: the transformation laws of the fields; for Lorentz, the antisymmetry of $\omega_{\mu\nu}$; only the lecture's sign of the translation parameter is new here.
> - Used next: step 2 of [[P3 Noether's Procedure]] in [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|Example §C1b.6.1]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|Theorem §C1b.7.5]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]].

^der-c1b-5-1

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-2|Def. §C1b.5.2]], [[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]], [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]]

*Procedure:* [[P3 Noether's Procedure#^p3-1|P3, step 1]]

> [!remark] Remark: What step 1 does not decide
> $\Delta\phi$ is the expansion of the transformation one was handed; whether $\mathcal L$ tolerates it is step 3 ([[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]]). The shift has a perfectly good generator in the massive theory, where it is not a symmetry ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|Example §C1b.6.1]]). In group language the $\Delta_a\phi_i$ represent the generators of the symmetry's Lie algebra on the fields ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]); for fields with indices a matrix acting on the components joins the orbital part $x\partial$ (Yu's $(I^{\mu\nu})_{ab}$, [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]]).

^rem-c1b-5-3

## Computing δℒ

Step 2 of [[P3 Noether's Procedure#^p3-2|P3]] asks for the first-order change of $\mathcal L$ under $\delta\phi = \alpha\Delta\phi$. Two facts make it mechanical: the variation passes inside $\partial_\mu$, and the change can be computed either by substituting or by the chain rule, with the same result.

> [!remark] Remark: Why the variation passes inside the derivative
> - **Fixed point.** $\delta\phi$ compares $\phi'$ and $\phi$ at the same $x$, so $\delta(\partial_\mu\phi) \equiv \partial_\mu\phi'(x) - \partial_\mu\phi(x) = \partial_\mu(\phi' - \phi)(x) = \partial_\mu(\delta\phi)$, by linearity of $\partial_\mu$. This is [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]] with $\varepsilon\eta$ replaced by the symmetry variation $\alpha\Delta\phi$; nothing new is needed.
> - **Constant parameter.** $\partial_\mu(\alpha\Delta\phi) = \alpha\,\partial_\mu(\Delta\phi)$ because $\partial_\mu\alpha = 0$. With the first point, $\Delta(\partial_\mu\phi) = \partial_\mu(\Delta\phi)$: derivatives of the field are never transformed on their own.
> - **When the point moves, it fails.** For a spacetime transformation the total change $\phi'(x') - \phi(x)$ compares two different points, and $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi) - (\partial_\nu\phi)\,\partial_\mu(\delta x^\nu)$; only the fixed-argument change $\bar\delta\phi$ commutes with $\partial_\mu$ ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|Theorem §C1b.7.1]]). That is why every $\Delta\phi$ of this section, the translation's $\partial_\nu\phi$ included, is a change at the old point ([[§C1b.5 Noether's Theorem#^def-c1b-5-1|Def. §C1b.5.1]], last paragraph).
> - **Why the proof keeps $\partial_\mu(\delta\phi)$ whole.** The chain rule produces $\pi^\mu\,\partial_\mu(\delta\phi)$, with $\pi^\mu = \partial\mathcal L/\partial(\partial_\mu\phi)$, and the product rule moves the derivative off $\delta\phi$ as a whole: $\pi^\mu\partial_\mu(\delta\phi) = \partial_\mu(\pi^\mu\delta\phi) - (\partial_\mu\pi^\mu)\,\delta\phi$ ([[§C1b.5 Noether's Theorem#^der-c1b-5-4|Derivation §C1b.5.4]], step 4). This identity holds for any fixed-argument $\delta\phi$, also for $\alpha(x)\Delta\phi$ with a position-dependent parameter. Constancy of $\alpha$ is used separately: at step 3 of that derivation, where $\partial_\mu(\alpha\Delta\phi) = \alpha\,\partial_\mu\Delta\phi$ and the by-product marks the extra term $(\partial_\mu\alpha)\Delta\phi$ a local parameter would produce, the term a gauge field must absorb ([[§C1b.6 Conserved Charges and Internal Symmetries#^rem-c1b-6-2|Remark: Global, internal, and what a local phase would need]]); and at step 6, to divide by $\alpha$.

^rem-c1b-5-4

> [!theorem] Theorem §C1b.5.2: Two Routes to δℒ
> Let $\mathcal L(\phi_i, \partial_\mu\phi_i)$ be $C^1$ in its arguments and $\delta\phi_i = \alpha^a\Delta_a\phi_i$ a symmetry variation with constant parameters ([[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]]). The first-order change $\delta\mathcal L$ at fixed $x$ is given equally by
> 1. **substitution**: the first-order part of $\mathcal L(\phi'_i, \partial_\mu\phi'_i) - \mathcal L(\phi_i, \partial_\mu\phi_i)$, with the transformed fields inserted, finite or truncated to $\phi_i + \alpha^a\Delta_a\phi_i$;
> 2. **the chain rule**:
>
> $$
> \delta\mathcal L = \alpha^a\sum_i\Bigl[\frac{\partial\mathcal L}{\partial\phi_i}\,\Delta_a\phi_i + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\,\partial_\mu(\Delta_a\phi_i)\Bigr] .
> $$
>
> The sum runs over every independent field variable; a complex field enters as $\phi$ and $\phi^{\ast}$, two variables with generators $\Delta\phi$ and $\Delta\phi^{\ast} = (\Delta\phi)^{\ast}$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]). A field whose derivatives do not occur in $\mathcal L$ has $\partial\mathcal L/\partial(\partial_\mu\phi_i) = 0$ and contributes through $\partial\mathcal L/\partial\phi_i$ alone. Neither route uses the equations of motion.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, "The procedure", step 2 ("Equivalently, by the chain rule") · PHY 513 Lecture 3, Part C ("Vary Lagrangean explicitly") · Yu §1.6.2, eq. (1.164)*

^thm-c1b-5-2

> [!derivation]- Derivation
> Fix a configuration and a point $x$, and write $\pi^\mu_i \equiv \partial\mathcal L/\partial(\partial_\mu\phi_i)$.
>
> **1. Route 1 as a derivative in the parameters.** Put $f(\alpha) \equiv \mathcal L\bigl(\phi_i + \alpha^a\Delta_a\phi_i,\ \partial_\mu\phi_i + \alpha^a\partial_\mu\Delta_a\phi_i\bigr)$ at $x$. The second argument is $\partial_\mu$ of the first because $\alpha$ is constant ([[§C1b.5 Noether's Theorem#^rem-c1b-5-4|Remark: Why the variation passes inside the derivative]]). $f$ is $C^1$, so $f(\alpha) - f(0) = \alpha^a\,\partial f/\partial\alpha^a|_{\alpha = 0} + o(\alpha)$, and the first-order part of the substitution is $\alpha^a\,\partial f/\partial\alpha^a|_0$.
>
> **2. Finite or truncated substitution.** The finite fields are $\phi'_i = \phi_i + \alpha^a\Delta_a\phi_i + O(\alpha^2)$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]]), so they and their derivatives differ from the arguments of $f$ by $O(\alpha^2)$; $\mathcal L$ is $C^1$, so $\mathcal L(\phi', \partial\phi')$ differs from $f(\alpha)$ by $O(\alpha^2)$ and has the same first-order part. ⚑ By-product: one may insert the exact $e^{i\alpha}\phi$ and expand at the end, which is often quickest → [[§C1b.5 Noether's Theorem#^ex-c1b-5-1|Example §C1b.5.1]].
>
> **3. Route 2 is the evaluation of that derivative.** Each argument of $\mathcal L$ in $f$ is linear in $\alpha$, so the chain rule ([[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]) gives
>
> $$
> \frac{\partial f}{\partial\alpha^a}\Big|_0 = \sum_i\Bigl[\frac{\partial\mathcal L}{\partial\phi_i}\,\frac{\partial(\phi_i + \alpha^b\Delta_b\phi_i)}{\partial\alpha^a} + \pi^\mu_i\,\frac{\partial(\partial_\mu\phi_i + \alpha^b\partial_\mu\Delta_b\phi_i)}{\partial\alpha^a}\Bigr] = \sum_i\Bigl[\frac{\partial\mathcal L}{\partial\phi_i}\,\Delta_a\phi_i + \pi^\mu_i\,\partial_\mu(\Delta_a\phi_i)\Bigr] ,
> $$
>
> the partial derivatives of $\mathcal L$ evaluated at the unvaried configuration. Multiplying by $\alpha^a$ and summing over $a$ gives Route 2.
>
> **4. Complex fields.** Take $\phi = (\phi_1 + i\phi_2)/\sqrt2$ and write $\mathcal L_{,j} \equiv \partial\mathcal L/\partial\phi_j$. In the real variables the undifferentiated part of step 3 is $\mathcal L_{,1}\,\delta\phi_1 + \mathcal L_{,2}\,\delta\phi_2$. Insert $\delta\phi = (\delta\phi_1 + i\delta\phi_2)/\sqrt2$, $\delta\phi^{\ast} = (\delta\phi_1 - i\delta\phi_2)/\sqrt2$ and the operators $\partial/\partial\phi = (\partial/\partial\phi_1 - i\,\partial/\partial\phi_2)/\sqrt2$, $\partial/\partial\phi^{\ast} = (\partial/\partial\phi_1 + i\,\partial/\partial\phi_2)/\sqrt2$ of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]:
>
> $$
> \frac{\partial\mathcal L}{\partial\phi}\,\delta\phi + \frac{\partial\mathcal L}{\partial\phi^{\ast}}\,\delta\phi^{\ast} = \tfrac12\Bigl[(\mathcal L_{,1} - i\mathcal L_{,2})(\delta\phi_1 + i\delta\phi_2) + (\mathcal L_{,1} + i\mathcal L_{,2})(\delta\phi_1 - i\delta\phi_2)\Bigr] = \mathcal L_{,1}\,\delta\phi_1 + \mathcal L_{,2}\,\delta\phi_2 ,
> $$
>
> the cross terms $i\mathcal L_{,1}\delta\phi_2$ and $i\mathcal L_{,2}\delta\phi_1$ appearing once with each sign. The terms with $\partial_\mu\phi$ and $\partial_\mu\phi^{\ast}$ recombine in the same way. So the pair $(\phi, \phi^{\ast})$ may replace $(\phi_1, \phi_2)$ in the sum, provided $\delta\phi^{\ast}$ is the conjugate of $\delta\phi$; for real $\alpha$ that is $\Delta\phi^{\ast} = (\Delta\phi)^{\ast}$.
>
> **5. A field without derivatives.** If $\mathcal L$ does not depend on $\partial_\mu\phi_i$, then $\pi^\mu_i = 0$ and only the first term of step 3 survives for that $i$. It does not drop out of $\delta\mathcal L$: its term $\frac{\partial\mathcal L}{\partial\phi_i}\Delta\phi_i$ can be needed for the cancellation ([[§C1b.5 Noether's Theorem#^ex-c1b-5-2|Example §C1b.5.2]], term (c)).
>
> **What the derivation shows**
> - Route 1 is the definition and Route 2 its evaluation, so they cannot disagree; a mismatch is an algebra slip. Route 1 is quickest when $\mathcal L$ is visibly invariant (phases cancelling term by term); Route 2 when it is not, and its ingredients $\pi^\mu_i$ are the ones the current needs anyway ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]).
> - Assumptions: $\alpha$ constant (step 1); $\mathcal L$ of class $C^1$ in its arguments; first order only. No equation of motion is used.
> - Used next: Formula 2 of [[§C1b.5 Noether's Theorem#^der-c1b-5-4|Derivation §C1b.5.4]] (Route 2 for an arbitrary $\delta\phi$, followed by the product rule); [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]; [[P3 Noether's Procedure#^p3-2|P3, step 2]].

^der-c1b-5-2

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]

*Procedure:* [[P3 Noether's Procedure#^p3-2|P3, step 2]]

> [!example] Example §C1b.5.1: δℒ for the Complex Scalar Phase, by Both Routes
> Take $\mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi - V(\phi^{\ast}\phi)$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]] with a potential, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-6|§C1b.2, Remark: The symmetry the real field lacks, and a potential]]) and $\phi \to e^{i\alpha}\phi$, $\phi^{\ast} \to e^{-i\alpha}\phi^{\ast}$ with constant $\alpha$, so $\Delta\phi = i\phi$, $\Delta\phi^{\ast} = -i\phi^{\ast}$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]).
>
> **Route 1, substitution.** Since $\partial_\mu\alpha = 0$, $\partial_\mu(e^{i\alpha}\phi) = e^{i\alpha}\partial_\mu\phi$. Term by term: $\partial_\mu(e^{-i\alpha}\phi^{\ast})\,\partial^\mu(e^{i\alpha}\phi) = e^{-i\alpha}e^{i\alpha}\,\partial_\mu\phi^{\ast}\partial^\mu\phi = \partial_\mu\phi^{\ast}\partial^\mu\phi$; $m^2e^{-i\alpha}\phi^{\ast}e^{i\alpha}\phi = m^2\phi^{\ast}\phi$; the argument of $V$ becomes $e^{-i\alpha}\phi^{\ast}e^{i\alpha}\phi = \phi^{\ast}\phi$. So $\mathcal L$ is unchanged for every $\alpha$, and $\delta\mathcal L = 0$.
>
> **Route 2, chain rule.** With $\phi$ and $\phi^{\ast}$ independent ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]], step 5 of its derivation), $V' \equiv dV/d(\phi^{\ast}\phi)$, and the chain rule through $V$ giving $\partial V/\partial\phi = V'\phi^{\ast}$:
>
> $$
> \frac{\partial\mathcal L}{\partial\phi} = -(m^2 + V')\,\phi^{\ast}, \quad \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)} = \partial^\mu\phi^{\ast}, \quad \frac{\partial\mathcal L}{\partial\phi^{\ast}} = -(m^2 + V')\,\phi, \quad \frac{\partial\mathcal L}{\partial(\partial_\mu\phi^{\ast})} = \partial^\mu\phi .
> $$
>
> The four terms of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], divided by $\alpha$:
> - (a) $\frac{\partial\mathcal L}{\partial\phi}\,\Delta\phi = -(m^2 + V')\,\phi^{\ast}(i\phi) = -i(m^2 + V')\,\phi^{\ast}\phi$;
> - (b) $\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\mu(\Delta\phi) = \partial^\mu\phi^{\ast}\,(i\,\partial_\mu\phi) = i\,\partial_\mu\phi\,\partial^\mu\phi^{\ast}$;
> - (c) $\frac{\partial\mathcal L}{\partial\phi^{\ast}}\,\Delta\phi^{\ast} = -(m^2 + V')\,\phi\,(-i\phi^{\ast}) = +i(m^2 + V')\,\phi\phi^{\ast}$;
> - (d) $\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^{\ast})}\,\partial_\mu(\Delta\phi^{\ast}) = \partial^\mu\phi\,(-i\,\partial_\mu\phi^{\ast}) = -i\,\partial^\mu\phi\,\partial_\mu\phi^{\ast}$.
>
> (a) + (c) $= 0$ because $\phi^{\ast}\phi = \phi\phi^{\ast}$; (b) + (d) $= 0$ because $\partial_\mu\phi\,\partial^\mu\phi^{\ast} = g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi^{\ast} = \partial^\nu\phi\,\partial_\nu\phi^{\ast}$ (the metric is symmetric). So $\delta\mathcal L = 0$, as by Route 1.
>
> Route 1 shows invariance to all orders at a glance; Route 2 shows where it comes from: each term of $\phi$ cancels the matching term of $\phi^{\ast}$, because the two generators are $+i$ and $-i$ times their fields. The current built from the same ingredients is [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]].
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Example 2, step 2 (Route 1), and "The procedure", step 2 (the chain-rule form) · PS §2.2, eq. (2.14) · PHY 513 Lecture 3, Part C, Example 2 · Route 2 written out here*

^ex-c1b-5-1

*Procedure:* [[P3 Noether's Procedure#^p3-2|P3, step 2]]

> [!example] Example §C1b.5.2: δℒ for the Dirac Phase, by Both Routes
> This example uses chapter C5a; read it after [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]. Take $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, with $\psi$ and $\bar\psi$ independent, four classical commuting components each ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|Theorem §C5a.7.6]], step 1 of its derivation). The phase $\psi \to e^{i\alpha}\psi$ gives $\bar\psi = \psi^\dagger\gamma^0 \to e^{-i\alpha}\bar\psi$ for real $\alpha$, so $\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$ ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]], step 1 of its derivation).
>
> **Route 1, substitution.** $\alpha$ is constant, so it passes through $\partial_\mu$, and as a number it commutes with the matrices $\gamma^\mu$: $\bar\psi'(i\gamma^\mu\partial_\mu - m)\psi' = e^{-i\alpha}\bar\psi\,(i\gamma^\mu\partial_\mu - m)\,e^{i\alpha}\psi = e^{-i\alpha}e^{i\alpha}\,\bar\psi(i\gamma^\mu\partial_\mu - m)\psi = \mathcal L$. So $\delta\mathcal L = 0$.
>
> **Route 2, chain rule.** In components $\mathcal L = \sum_{a,b}\bar\psi_a\bigl[i(\gamma^\nu)_{ab}\partial_\nu\psi_b - m\delta_{ab}\psi_b\bigr]$, with the derivatives of [[§C5a.7 The Dirac Equation and Its Lagrangian#^der-c5a-7-6|Derivation §C5a.7.6]], steps 2–3:
>
> $$
> \frac{\partial\mathcal L}{\partial\psi_c} = -m\bar\psi_c, \quad \frac{\partial\mathcal L}{\partial(\partial_\mu\psi_c)} = i(\bar\psi\gamma^\mu)_c, \quad \frac{\partial\mathcal L}{\partial\bar\psi_a} = \bigl[(i\gamma^\nu\partial_\nu - m)\psi\bigr]_a, \quad \frac{\partial\mathcal L}{\partial(\partial_\mu\bar\psi_a)} = 0 .
> $$
>
> The sum of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]] runs over the eight variables $\psi_c$, $\bar\psi_a$; divided by $\alpha$:
> - (a) $\sum_c\frac{\partial\mathcal L}{\partial\psi_c}\,\Delta\psi_c = \sum_c(-m\bar\psi_c)(i\psi_c) = -im\,\bar\psi\psi$;
> - (b) $\sum_c\frac{\partial\mathcal L}{\partial(\partial_\mu\psi_c)}\,\partial_\mu(\Delta\psi_c) = \sum_c i(\bar\psi\gamma^\mu)_c\,(i\,\partial_\mu\psi_c) = -\bar\psi\gamma^\mu\partial_\mu\psi$;
> - (c) $\sum_a\frac{\partial\mathcal L}{\partial\bar\psi_a}\,\Delta\bar\psi_a = \sum_a(-i\bar\psi_a)\bigl[(i\gamma^\nu\partial_\nu - m)\psi\bigr]_a = \bar\psi\gamma^\nu\partial_\nu\psi + im\,\bar\psi\psi$;
> - (d) no term: $\mathcal L$ contains no derivative of $\bar\psi$.
>
> Renaming the dummy $\nu$ to $\mu$, (a) + (b) + (c) $= -im\,\bar\psi\psi - \bar\psi\gamma^\mu\partial_\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi + im\,\bar\psi\psi = 0$, as by Route 1.
>
> Term (c) is the case of a field without derivatives in [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]: $\bar\psi$ has no $\partial\mathcal L/\partial(\partial_\mu\bar\psi)$, yet its $\partial\mathcal L/\partial\bar\psi$ term is needed, since (a) + (b) alone leave $-im\,\bar\psi\psi - \bar\psi\gamma^\mu\partial_\mu\psi \ne 0$. The current uses only the derivatives with respect to $\partial_\mu$ of the fields, so there $\bar\psi$ contributes nothing: $j^\mu_{\rm N} = i\bar\psi\gamma^\mu(i\psi) = -\bar\psi\gamma^\mu\psi$ ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]]).
>
> *Source: PS §3.4, p. 51 (the Noether current of $\psi \to e^{i\alpha}\psi$) · the user's PHY 513 notes, Ch. 8 §8.8 (eq. (diracL)), Ch. 3 §3.5 ("The procedure", step 2) · PHY 513 Lecture 8, Part B (the Dirac Lagrangian) · Route 2 written out here*

^ex-c1b-5-2

*Procedure:* [[P3 Noether's Procedure#^p3-2|P3, step 2]]

## The symmetry test

> [!definition] Definition §C1b.5.5: Symmetry of the Action; the Vector 𝒥
> A continuous transformation is a **symmetry of the action**, for a given $\mathcal L$, if substituting $\phi_i + \alpha^a\Delta_a\phi_i$ into $\mathcal L$ changes it (computed by either route of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]), to first order and for every field configuration, by a total derivative,
>
> $$
> \delta\mathcal L = \alpha^a\,\partial_\mu\mathcal J^\mu_a ,
> $$
>
> for some local four-vectors $\mathcal J^\mu_a$, one per parameter; the equation **defines** $\mathcal J^\mu_a$. The test has three outcomes: (i) $\delta\mathcal L = 0$ identically, and one takes $\mathcal J = 0$; (ii) $\delta\mathcal L$ is a nonzero divergence, and $\mathcal J$ is read off; (iii) $\delta\mathcal L$ is not a divergence: no symmetry and no conserved current; what the would-be current then satisfies is [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]].
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Definition "Symmetry, and the definition of 𝒥", eq. (Jcal) · PS §2.2, eq. (2.10) · Lecture 3, Part C ("The total derivative defines $J^\mu$")*

^def-c1b-5-5

> [!remark] Remark: Why a total derivative is allowed
> $\int d^4x\,\partial_\mu(\alpha\mathcal J^\mu)$ is a boundary term ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]), so the action changes only on the boundary of spacetime, where the action principle holds the field fixed ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^pr-c1b-2-3|Principle §C1b.2.3]]). So $\mathcal L$ and $\mathcal L + \alpha\partial_\mu\mathcal J^\mu$ have the same stationary configurations, the same equations of motion ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]; for particles [[§B6.2 Hamilton's Principle of Stationary Action#^thm-b6-2-4|CM Theorem §B6.2.4]]). A symmetry of the action is therefore a symmetry of the equations of motion: it maps solutions to solutions. $\mathcal J$ is not an object with a formula of its own but the output of the test, "whatever had to be written inside a divergence", and depends on the transformation and $\mathcal L$ together. It carries one current index $\mu$ and as many labels as the parameter has: $\mathcal J^\mu$, $\mathcal J^\mu{}_\nu$ for translations, $\mathcal J^{\mu\nu\rho}$ for Lorentz transformations. In mechanics the same role is played by $K$ in $\delta\mathcal L = dK/dt$ ([[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^def-b6-4-2|CM Def. §B6.4.2]]).

^rem-c1b-5-5

> [!theorem] Theorem §C1b.5.3: The First-Order Test Decides the Whole Family
> Let $T_\alpha$ be a one-parameter group of transformations of the fields ($T_0 = \mathrm{id}$, $T_\beta T_\alpha = T_{\alpha + \beta}$), and suppose its first-order test ([[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]]) holds **for every configuration** $\chi$: $\mathcal L[T_\varepsilon\chi] - \mathcal L[\chi] = \varepsilon\,\partial_\mu\mathcal J^\mu[\chi] + O(\varepsilon^2)$, with $\mathcal J$ local. Then for every finite $\alpha$
>
> $$
> \mathcal L[T_\alpha\phi] = \mathcal L[\phi] + \partial_\mu K^\mu_\alpha[\phi], \qquad K^\mu_\alpha[\phi] \equiv \int_0^\alpha d\beta\;\mathcal J^\mu[T_\beta\phi] .
> $$
>
> In particular, $\delta\mathcal L = 0$ for every configuration implies $\mathcal L[T_\alpha\phi] = \mathcal L[\phi]$ exactly: the $O(\alpha^2)$ terms of [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]] impose no further condition.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Definition "Transformation, parameter, generator" ("nothing is lost, since finite transformations are compositions of small ones") · the integration along the family written out here*

^thm-c1b-5-3

> [!derivation]- Derivation
> Fix $\phi$ and $x$; write $\mathcal L[\chi]$ for $\mathcal L(\chi(x), \partial\chi(x))$ and $g(\beta) \equiv \mathcal L[T_\beta\phi]$.
>
> **1. A step along the family is a small transformation of the moved configuration.** By the group law, $T_{\beta + \varepsilon}\phi = T_\varepsilon(T_\beta\phi)$. With $\chi \equiv T_\beta\phi$, $g(\beta + \varepsilon) - g(\beta) = \mathcal L[T_\varepsilon\chi] - \mathcal L[\chi]$.
>
> **2. Apply the test at $\chi$.** The test holds for every configuration, so for $\chi$: $g(\beta + \varepsilon) - g(\beta) = \varepsilon\,\partial_\mu\mathcal J^\mu[\chi] + O(\varepsilon^2)$. Divide by $\varepsilon$ and let $\varepsilon \to 0$: $g'(\beta) = \partial_\mu\mathcal J^\mu[T_\beta\phi]$. ⚑ By-product: this is where "for every configuration" is used; a test passed only at $\phi$, or only on solutions, would say nothing about $T_\beta\phi$ → [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]].
>
> **3. Integrate in the parameter.** $g$ is $C^1$ when the family, $\mathcal L$ and $\mathcal J$ are, so by the fundamental theorem of calculus $g(\alpha) - g(0) = \int_0^\alpha d\beta\;\partial_\mu\mathcal J^\mu[T_\beta\phi]$.
>
> **4. Take $\partial_\mu$ outside.** The integrand is continuously differentiable in $(\beta, x)$ and $[0, \alpha]$ is compact, so the derivative in $x^\mu$ passes under $\int d\beta$ ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]): $\int_0^\alpha d\beta\;\partial_\mu\mathcal J^\mu[T_\beta\phi] = \partial_\mu\int_0^\alpha d\beta\;\mathcal J^\mu[T_\beta\phi] = \partial_\mu K^\mu_\alpha$. With $g(0) = \mathcal L[\phi]$ this is the statement; for $\mathcal J = 0$, $K = 0$.
>
> **5. Check on translations.** $T_t\phi(x) = \phi(x + tc)$ for a fixed four-vector $c$ (the lecture's translation by $a = tc$, [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]), whose test gives $\mathcal J^\mu = c^\mu\mathcal L$ ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|Theorem §C1b.7.5]]). Then $\partial_\mu K^\mu_t = \int_0^t ds\;c^\mu(\partial_\mu\mathcal L)(x + sc) = \int_0^t ds\;\frac{d}{ds}\mathcal L(x + sc) = \mathcal L(x + tc) - \mathcal L(x)$, which is $\mathcal L[T_t\phi] - \mathcal L[\phi]$, as claimed.
>
> **What the derivation shows**
> - A continuous symmetry is fixed by its generator: the first-order test, passed off shell, propagates along the whole family. This is why [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]] may drop $O(\alpha^2)$, and why Noether's theorem needs only $\Delta\phi$.
> - Several parameters: each one-parameter subgroup $\alpha^a = tc^a$ is covered by steps 1–4, and near the identity every element of a connected Lie group is a product of elements of one-parameter subgroups (a fact of Lie theory, not proved here); a composition of maps that each change $\mathcal L$ by a divergence changes it by a divergence.
> - Discrete transformations (parity, charge conjugation) have no generator and are not covered ([[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-2|Caution: What the theorem does and does not say]]).
> - Used in: [[§C1b.5 Noether's Theorem#^rem-c1b-5-1|Remark: δ and Δ side by side, and why only first order]].

^der-c1b-5-3

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|Theorem §C1b.7.5]]

## The procedure

The algorithm is [[P3 Noether's Procedure]]: six steps, the same for every symmetry. Steps 1–4 are algebra on $\mathcal L$ and produce the current; step 5 is the theorem below, the only place the equations of motion enter; step 6 is its physical content, the only place boundary conditions enter. Step 2 can be done by substitution or by the chain rule ([[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]). Symmetries differ only in the size of the answers at steps 1 and 3: whether the point moves (then $\Delta\phi$ contains derivatives of $\phi$) and whether $\mathcal L$ is invariant outright ($\mathcal J = 0$) or only up to a divergence.

![[ph-qft-c1-11-1.svg]]
*Noether's procedure as a flow; each arrow is labelled with what that step needs. Everything up to the current is algebra on the Lagrangian; the equations of motion are used only to conclude that the current is conserved (orange), and boundary conditions only to conclude that the charge is.*

The answers for every symmetry of the course, side by side before any is derived, for $\mathcal L = \frac12(\partial\phi)^2 - \frac12m^2\phi^2$ or the complex $\mathcal L = \partial_\mu\phi^*\partial^\mu\phi - m^2\phi^*\phi$:

| operation | parameter | step 1: $\Delta\phi$ | steps 2–3: $\delta\mathcal L$ and $\mathcal J$ | steps 4, 6: current, charge | derived in |
| --- | --- | --- | --- | --- | --- |
| shift, $m = 0$ | $\alpha$ | $1$ | $\delta\mathcal L = 0$; $\mathcal J^\mu = 0$ | $j^\mu = \partial^\mu\phi$; $Q = \int d^3x\,\dot\phi$ | [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1\|Example §C1b.6.1]] |
| shift, $m \ne 0$ | $\alpha$ | $1$ | $\delta\mathcal L = -\alpha m^2\phi$: not a divergence | no symmetry; the would-be $j^\mu = \partial^\mu\phi$ has $\partial_\mu j^\mu = -m^2\phi$ on shell | [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1\|Example §C1b.6.1]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-5\|Theorem §C1b.5.5]] |
| phase (complex field) | $\alpha$ | $i\phi$, $-i\phi^*$ | $\delta\mathcal L = 0$; $\mathcal J^\mu = 0$ | $j^\mu = i(\phi\,\partial^\mu\phi^* - \phi^*\partial^\mu\phi)$; number charge | [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3\|Theorem §C1b.6.3]] |
| phase, with the mass splitting $-\frac{\lambda}{2}(\phi^2 + \phi^{\ast 2})$ | $\alpha$ | $i\phi$, $-i\phi^{\ast}$ | $\delta\mathcal L = -i\alpha\lambda(\phi^2 - \phi^{\ast 2})$: not a divergence | no symmetry; the would-be U(1) current has $\partial_\mu j^\mu = -i\lambda(\phi^2 - \phi^{\ast 2})$ on shell | [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3\|Example §C1b.6.3]] |
| translation | $a^\nu$ (four) | $\partial_\nu\phi$ | $\delta\mathcal L = a^\nu\partial_\nu\mathcal L$; $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ | $T^\mu{}_\nu = \partial^\mu\phi\,\partial_\nu\phi - \delta^\mu{}_\nu\mathcal L$; $P^\mu = (H, \mathbf P)$ | [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5\|Theorem §C1b.7.5]] |
| Lorentz | $\omega_{\nu\rho}$ (six) | $x^\nu\partial^\rho\phi - x^\rho\partial^\nu\phi$ | $\delta\mathcal L = \frac12\omega_{\nu\rho}\partial_\mu\mathcal J^{\mu\nu\rho}$; $\mathcal J^{\mu\nu\rho} = (x^\nu g^{\mu\rho} - x^\rho g^{\mu\nu})\mathcal L$ | $\mathcal M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$; $\mathbf J$, $\mathbf K$ | [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1\|Theorem §C1b.8.1]] |

The pattern: the current is always $\partial\mathcal L/\partial(\partial_\mu\phi)$ times the generator, minus $\mathcal J$, and in these examples $\mathcal J \ne 0$ exactly when the point moves; in Yu's formulation $\alpha\mathcal J^\mu = -\mathcal L\,\delta x^\mu$ throughout ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-4|Theorem §C1b.7.4]]). When the test fails, the same expression with $\mathcal J = 0$ is not conserved, and its divergence on shell is $\delta\mathcal L/\alpha$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]).

## The theorem

> [!theorem] Theorem §C1b.5.4: Noether's Theorem
> Let a transformation with generators $\Delta_a\phi_i$ be a symmetry of the action with vectors $\mathcal J^\mu_a$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]]). Then the **Noether currents**
>
> $$
> j^\mu_a = \sum_{i=1}^N\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\,\Delta_a\phi_i - \mathcal J^\mu_a
> $$
>
> satisfy, for every field configuration (off shell),
>
> $$
> \partial_\mu j^\mu_a = -\sum_i\Bigl[\frac{\partial\mathcal L}{\partial\phi_i} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Bigr]\Delta_a\phi_i ,
> $$
>
> and therefore $\partial_\mu j^\mu_a = 0$ on solutions of the Euler–Lagrange equations (on shell): one conserved current per parameter, summed over every field that parameter moves.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, Principle "Noether's theorem", eqs. (noethercurrentdef)–(noethercurrent) · PS §2.2, eqs. (2.11)–(2.12) · Lecture 3, Part C*

^thm-c1b-5-4

> [!derivation]- Derivation
> One field and one parameter; the general case adds $\sum_i$ and the label $a$ throughout (step 9). Write $\pi^\mu \equiv \partial\mathcal L/\partial(\partial_\mu\phi)$. The proof computes the same quantity, the change $\delta\mathcal L$ under $\delta\phi = \alpha\Delta\phi$, in two independent ways.
>
> **1. Formula 1, from the symmetry.** By [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]], for every configuration, $\delta\mathcal L = \alpha\,\partial_\mu\mathcal J^\mu$. This is a fact about $\mathcal L$ and the transformation, established by substitution; no equation of motion is involved.
>
> **2. Formula 2, the chain rule.** For any variation $\delta\phi$ at fixed $x$, $\mathcal L(\phi, \partial_\mu\phi)$ changes by ([[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]; Route 2 of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], here before $\delta\phi$ is specified)
>
> $$
> \delta\mathcal L = \frac{\partial\mathcal L}{\partial\phi}\,\delta\phi + \pi^\mu\,\delta(\partial_\mu\phi) + O(\delta\phi^2) .
> $$
>
> **3. The variation of the derivative.** $\delta\phi = \alpha\Delta\phi$ compares two functions at the same $x$, and $\alpha$ is constant, so $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi) = \alpha\,\partial_\mu(\Delta\phi)$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]]; [[§C1b.5 Noether's Theorem#^rem-c1b-5-4|Remark: Why the variation passes inside the derivative]]). ⚑ By-product: this is where "global" is used; for $\alpha(x)$ one would get $\partial_\mu(\alpha\Delta\phi) = \alpha\,\partial_\mu\Delta\phi + (\partial_\mu\alpha)\Delta\phi$, and the extra term is what a gauge field must absorb → [[§C1b.6 Conserved Charges and Internal Symmetries#^rem-c1b-6-2|Remark: Global, internal, and what a local phase would need]].
>
> **4. Move the derivative, keep the total derivative.** By the product rule, $\pi^\mu\,\partial_\mu(\delta\phi) = \partial_\mu(\pi^\mu\delta\phi) - (\partial_\mu\pi^\mu)\,\delta\phi$, an identity at each point. Nothing is integrated and nothing is dropped. ⚑ By-product: in the derivation of the Euler–Lagrange equations the same total derivative was a boundary term and was discarded ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]]); here it is kept, and it becomes the current.
>
> **5. Assemble Formula 2.** With steps 3–4,
>
> $$
> \delta\mathcal L = \Bigl[\frac{\partial\mathcal L}{\partial\phi} - \partial_\mu\pi^\mu\Bigr]\alpha\Delta\phi + \alpha\,\partial_\mu\bigl(\pi^\mu\Delta\phi\bigr) ,
> $$
>
> valid for every configuration. The bracket is the Euler–Lagrange expression, $\mathrm{EL} \equiv \partial\mathcal L/\partial\phi - \partial_\mu\pi^\mu$.
>
> **6. Equate.** Both formulas are the first-order change of the same function:
>
> $$
> \alpha\,\partial_\mu\mathcal J^\mu = \mathrm{EL}\,\alpha\Delta\phi + \alpha\,\partial_\mu\bigl(\pi^\mu\Delta\phi\bigr) .
> $$
>
> Both sides are linear in $\alpha$ at this order; divide by $\alpha \ne 0$.
>
> **7. Collect the divergences.** $\partial_\mu\bigl(\pi^\mu\Delta\phi - \mathcal J^\mu\bigr) = -\mathrm{EL}\,\Delta\phi$. The vector in parentheses is $j^\mu$, and this is the off-shell identity.
>
> **8. On shell.** On a solution $\mathrm{EL} = 0$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]), so $\partial_\mu j^\mu = 0$.
>
> **9. Several fields, several parameters.** When one parameter moves several fields, the total change of $\mathcal L$ is the sum of their contributions, so steps 2–5 carry $\sum_i$: the current is summed over fields. With parameters $\alpha^a$, choose all but one equal to zero; each $a$ gives its own identity and its own current.
>
> **What the derivation shows**
> - Steps 1–7 hold for every configuration; the equations of motion enter only at step 8. The off-shell identity is the practical check of any current ([[P3 Noether's Procedure#^p3-5|P3, step 5]]).
> - No integral and no boundary term appear: the theorem is local.
> - Assumptions used: the parameter is constant (step 3); $\mathcal L$ depends on $\phi$ and first derivatives only; fields are twice differentiable ([[§C1b.5 Noether's Theorem#^rem-c1b-5-9|Remark: In what sense these identities hold]]).
> - Only step 1 uses the symmetry. With a $\delta\mathcal L$ that is not a divergence, steps 2–8 give the divergence of the would-be current instead of zero ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]).
> - Used next: the charge ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]), every example, and the general form ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-3|Theorem §C1b.7.3]]).

^der-c1b-5-4

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-2|Def. §C1b.5.2]], [[§C1b.5 Noether's Theorem#^def-c1b-5-3|Def. §C1b.5.3]], [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]

*Procedure:* [[P3 Noether's Procedure#^p3-4|P3, steps 4–5]]

> [!remark] Remark: The action principle's computation, run backwards
> Formula 2 is the manipulation that derives the Euler–Lagrange equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]]), with the logic reversed. There, $\delta\phi$ was arbitrary and vanished on the boundary, and the equation of motion was *concluded* from $\delta S = 0$. Here, $\delta\phi$ is the specific shape of a symmetry and need not vanish anywhere (a constant shift does not), and the equation of motion is *assumed*: one works with a solution and maps it to another. The line on the Lecture 3 slide, $\alpha\,\partial_\mu\bigl(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\Delta\phi\bigr) = \alpha\,\partial_\mu\mathcal J^\mu$, is the off-shell identity with the Euler–Lagrange term already dropped: it holds on shell only. In the user's notes the theorem is boxed as a principle; it is derived here from [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]] and the Euler–Lagrange equations, so it is a theorem. What is new compared with [[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-2|CM Theorem §B6.4.2]]: a conserved number $I = \sum p_i\eta_i - K$ along each motion becomes a continuity equation at every point, and the number becomes the integral of a density ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]).

^rem-c1b-5-6

> [!remark] Remark: Several fields, several parameters
> The sum over $i$ is the whole rule for theories with several fields: one current per parameter, summed over every field the parameter moves. The number of currents is $\dim G$, the number of parameters, not the number of fields ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|Example §C1b.6.2]]). The spacetime currents $T^{\mu\nu}$ and $\mathcal M^{\mu\nu\rho}$ are accordingly sums over all fields present, and $T^{00} = \mathcal H$ holds with the summed Hamiltonian density ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-2|§C1b.4, Remark: Several fields, and a non-canonical normalization]]; [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-6|Theorem §C1b.7.6]]). For a complex field, $\phi$ and $\phi^*$ are two of the $\phi_i$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]).

^rem-c1b-5-7

> [!remark] Remark: What the sum over fields runs over
> The index $i$ in $\sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Delta\phi_i$ runs over a complete set of independent field variables of $\mathcal L$: every real component, with each complex component entered either as its real and imaginary parts or as the pair (field, conjugate) treated as independent ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]); both choices give the same sum (step 4 of [[§C1b.5 Noether's Theorem#^der-c1b-5-2|Derivation §C1b.5.2]]). The field label is a spacetime index only for a vector field:
>
> | field | independent variables in the sum | the label |
> | --- | --- | --- |
> | real scalar $\phi$ | $\phi$: 1 real | none |
> | complex scalar $\phi$ | $\phi$, $\phi^{\ast}$ (equivalently $\phi_1$, $\phi_2$): 2 real | none |
> | vector $A^\mu$ | $A^0$, $A^1$, $A^2$, $A^3$: 4 real | a spacetime index: under Lorentz transformations the components mix with $\Lambda$ ([[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1\|Example §C1b.1.1]]) |
> | Dirac $\psi$ | $\psi_1, \dots, \psi_4$ and $\bar\psi_1, \dots, \bar\psi_4$: 4 complex components, 8 real | a spinor index $a$, not a spacetime index: the components mix with $\Lambda_{1/2}$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2\|§C5b.2, Caution: u is not a four-vector]]) |
>
> For the Dirac field the sum over $a$ is a row times a column, $\sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\psi_a)}\Delta\psi_a = i\bar\psi\gamma^\mu\Delta\psi$, and the $\bar\psi_a$ add nothing to the current because $\mathcal L$ has no $\partial_\mu\bar\psi$ ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|Theorem §C5a.8.1]]); they do contribute to $\delta\mathcal L$ ([[§C1b.5 Noether's Theorem#^ex-c1b-5-2|Example §C1b.5.2]]). That a Dirac spinor has as many components as a four-vector is special to four dimensions: in $d$ spacetime dimensions it has $2^{\lfloor d/2\rfloor}$ components against $d$ ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]]).

^rem-c1b-5-8

> [!remark] Remark: In what sense these identities hold
> The fields here are classical: twice continuously differentiable real or complex functions on spacetime, and every identity of this section holds pointwise. No generalized function appears. Two assumptions are added where they are used: the current falls off at spatial infinity fast enough that its flux through a large sphere vanishes, and $d/dt$ may be taken under $\int d^3x$ ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]); both enter only in [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]. After quantization the same currents are products of operator-valued distributions at one point ([[§CA.2 Generalized Functions#^def-ca-2-11|Def. §CA.2.11]]); they become operators only after normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]), and the ordering constant of a charge is not harmless ([[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]]).

^rem-c1b-5-9

## When the test fails

The algebra of the proof does not need the symmetry until its last line. Run with a $\delta\mathcal L$ that is not a divergence, it gives the divergence of the would-be current instead of zero.

> [!theorem] Theorem §C1b.5.5: The Divergence of the Current When the Test Fails
> Let $\delta\phi_i = \alpha\Delta\phi_i$ be any continuous transformation with a constant parameter ([[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]]), and split its $\delta\mathcal L$, computed by either route of [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], as
>
> $$
> \delta\mathcal L = \alpha\bigl(\partial_\mu\mathcal J^\mu + X\bigr) ,
> $$
>
> with $\mathcal J^\mu$ the part written as a divergence (possibly $0$) and $X$ the remainder. Then $j^\mu \equiv \sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Delta\phi_i - \mathcal J^\mu$ satisfies
>
> $$
> \partial_\mu j^\mu = X - \sum_i\Bigl[\frac{\partial\mathcal L}{\partial\phi_i} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Bigr]\Delta\phi_i \quad \text{(off shell)}, \qquad \partial_\mu j^\mu = X \quad \text{(on shell)} .
> $$
>
> For $X = 0$ this is [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]. If $X$ is not a divergence, the transformation is no symmetry (outcome (iii) of [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]]), and on solutions the divergence of the would-be current is the non-divergence part of $\delta\mathcal L/\alpha$; with $\mathcal J = 0$, simply $\partial_\mu j^\mu = \delta\mathcal L/\alpha$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5, eq. (noetheroffshell) and Example 1 ("With a mass, step 2 gives $\delta\mathcal L = -\alpha m^2\phi$ … and indeed $\partial_\mu\partial^\mu\phi = -m^2\phi \neq 0$") · PHY 513 Lecture 3, Part C ("Vary Lagrangean explicitly") · the identity with $\delta\mathcal L$ not a divergence written out here*

^thm-c1b-5-5

> [!derivation]- Derivation
> One parameter; several fields carry $\sum_i$ throughout. Write $\pi^\mu_i \equiv \partial\mathcal L/\partial(\partial_\mu\phi_i)$ and $\mathrm{EL}_i \equiv \partial\mathcal L/\partial\phi_i - \partial_\mu\pi^\mu_i$. Steps 1–4 assume no symmetry and no equation of motion.
>
> **1. Route 2.** By [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], for every configuration, $\delta\mathcal L = \alpha\sum_i\bigl[\frac{\partial\mathcal L}{\partial\phi_i}\Delta\phi_i + \pi^\mu_i\,\partial_\mu(\Delta\phi_i)\bigr]$.
>
> **2. Product rule.** At each point $\pi^\mu_i\,\partial_\mu(\Delta\phi_i) = \partial_\mu(\pi^\mu_i\Delta\phi_i) - (\partial_\mu\pi^\mu_i)\,\Delta\phi_i$, as in step 4 of [[§C1b.5 Noether's Theorem#^der-c1b-5-4|Derivation §C1b.5.4]]. Hence
>
> $$
> \delta\mathcal L = \alpha\sum_i\mathrm{EL}_i\,\Delta\phi_i + \alpha\,\partial_\mu\Bigl(\sum_i\pi^\mu_i\Delta\phi_i\Bigr) .
> $$
>
> **3. Equate with the substitution result.** Both are the first-order change of the same function ([[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]), so $\alpha(\partial_\mu\mathcal J^\mu + X) = \alpha\sum_i\mathrm{EL}_i\,\Delta\phi_i + \alpha\,\partial_\mu\bigl(\sum_i\pi^\mu_i\Delta\phi_i\bigr)$. Divide by $\alpha \ne 0$.
>
> **4. Collect the divergences.** Move $\partial_\mu\mathcal J^\mu$ to the right and $\sum_i\mathrm{EL}_i\Delta\phi_i$ to the left: $\partial_\mu\bigl(\sum_i\pi^\mu_i\Delta\phi_i - \mathcal J^\mu\bigr) = X - \sum_i\mathrm{EL}_i\,\Delta\phi_i$. The vector in parentheses is $j^\mu$: the off-shell identity.
>
> **5. On shell.** On a solution every $\mathrm{EL}_i = 0$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]), so $\partial_\mu j^\mu = X$.
>
> **6. The split is not unique; the statement is.** If $X = X' + \partial_\mu K^\mu$ with $K$ local, the same $\delta\mathcal L$ reads $\alpha(\partial_\mu\mathcal J'^\mu + X')$ with $\mathcal J' = \mathcal J + K$, and the current becomes $j' = j - K$. Then on shell $\partial_\mu j'^\mu = \partial_\mu j^\mu - \partial_\mu K^\mu = X - \partial_\mu K^\mu = X'$: current and remainder shift together. ⚑ By-product: a shift removes $X$ entirely only if $X$ is itself a divergence, which is outcome (ii); otherwise no choice of $\mathcal J$ gives a conserved current of this form → [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]].
>
> **7. The charge.** Steps 2–5 of [[§C1b.6 Conserved Charges and Internal Symmetries#^der-c1b-6-1|Derivation §C1b.6.1]], run with $\partial_tj^0 = X - \nabla\cdot\mathbf j$ in place of $\partial_tj^0 = -\nabla\cdot\mathbf j$, give for a fixed region $V$
>
> $$
> \frac{dQ_V}{dt} = \int_Vd^3x\;X - \oint_{\partial V}\mathbf j\cdot d\mathbf S ,
> $$
>
> and, with the fall-off assumed there and $X$ integrable, $dQ/dt = \int d^3x\,X$. ⚑ By-product: $X$ is the local rate at which the non-invariant term creates charge.
>
> **What the derivation shows**
> - Noether's theorem and its failure are one computation; only the input $\delta\mathcal L$ differs, and the equations of motion enter only at step 5.
> - Cross-check: a divergence computed directly from the field equations must equal $X$; a mismatch is an error in $\delta\mathcal L$ or in the current ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|Example §C1b.6.1]], massive case; [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|Example §C1b.6.3]]; for a Dirac field, the chiral rotation, $\delta\mathcal L = -2i\alpha m\,\bar\psi\gamma^5\psi$ by both routes of Theorem §C1b.5.2 and $\partial_\mu j^\mu_5 = -2im\,\bar\psi\gamma^5\psi$ from the Dirac equation, Problem Set 6, Problem 5: [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|Example §C5a.8.1]]).
> - Assumptions: $\alpha$ constant (step 1); $\mathcal L$ with first derivatives only; for step 7, the fall-off of [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]] and an integrable $X$.
> - Used next: [[§C1b.5 Noether's Theorem#^rem-c1b-5-10|Remark: The three outcomes of the test and their currents]]; [[P3 Noether's Procedure#^p3-3|P3, steps 3 and 5]].

^der-c1b-5-5

*Uses:* [[§C1b.5 Noether's Theorem#^def-c1b-5-4|Def. §C1b.5.4]], [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]

*Procedure:* [[P3 Noether's Procedure#^p3-3|P3, step 3]], [[P3 Noether's Procedure#^p3-5|P3, step 5]]

> [!remark] Remark: The three outcomes of the test and their currents
> | outcome ([[§C1b.5 Noether's Theorem#^def-c1b-5-5\|Def. §C1b.5.5]]) | $\delta\mathcal L$ | current | $\partial_\mu j^\mu$ on shell | examples |
> | --- | --- | --- | --- | --- |
> | (i) invariant | $0$ | $\sum_i\pi^\mu_i\Delta\phi_i$, no extra term | $0$ | massless shift ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1\|Example §C1b.6.1]]); complex phase ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3\|Theorem §C1b.6.3]]); rotation of two fields ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2\|Example §C1b.6.2]]); Dirac phase ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3\|Theorem §C5a.8.3]]) |
> | (ii) a divergence | $\alpha\,\partial_\mu\mathcal J^\mu$ | $\sum_i\pi^\mu_i\Delta\phi_i - \mathcal J^\mu$ | $0$ | translations, $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5\|Theorem §C1b.7.5]]); Lorentz transformations ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1\|Theorem §C1b.8.1]]) |
> | (iii) not a divergence | $\alpha X$ | $\sum_i\pi^\mu_i\Delta\phi_i$, not conserved | $X$ | massive shift, $X = -m^2\phi$ ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1\|Example §C1b.6.1]]); mass splitting, $X = 2\lambda\phi_1\phi_2$ ([[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3\|Example §C1b.6.3]]); chiral rotation of a massive Dirac field, $X = -2im\,\bar\psi\gamma^5\psi$ ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1\|Example §C5a.8.1]]) |
>
> All three rows are [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]], with $X = 0$ in (i) and (ii). Forgetting $\mathcal J$ in case (ii) manufactures a false case (iii): for translations $\sum_i\pi^\mu_i\partial_\nu\phi_i = T^\mu{}_\nu + \delta^\mu{}_\nu\mathcal L$ ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-2|Def. §C1b.7.2]]) has divergence $\partial_\nu\mathcal L \ne 0$ on shell, although energy and momentum are conserved. Conversely, a divergence computed directly from the field equations is checked against $\delta\mathcal L/\alpha - \partial_\mu\mathcal J^\mu$: the two must agree.

^rem-c1b-5-10

> [!remark]- Connections
> - The charge of each current, the freedom of improvement terms, and the procedure run on the internal symmetries (shift, U(1) phase, rotation of two real fields, a symmetry-breaking mass splitting) are [[§C1b.6 Conserved Charges and Internal Symmetries|§C1b.6]] ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|Example §C1b.6.3]]).
> - The particle theorem [[§B6.4 Symmetries, Conservation Laws and Noether's Theorem#^thm-b6-4-2|CM Theorem §B6.4.2]] is the one-dimensional case: its $K$ is $\mathcal J$, its conserved $I = \sum_ip_i\eta_i - K$ is the charge, and $p_i = \partial\mathcal L/\partial\dot q_i$ becomes $\partial\mathcal L/\partial(\partial_\mu\phi)$, the time derivative becoming a four-divergence; field theory turns the conserved number into a local continuity equation.
> - A continuous symmetry is fixed by its generator ([[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]]), the field-level counterpart of a one-parameter group being the exponential of its generator ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]]); this is why the infinitesimal $\Delta\phi$ carries all the information Noether's theorem uses.
> - A transformation that fails the test still has a useful current: its divergence on shell is the variation of $\mathcal L$ ([[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]), the same identity that gives exact conservation when the variation is a divergence; an explicitly $x$-dependent $\mathcal L$ is the spacetime case, where $\partial_\mu T^\mu{}_\nu$ equals minus the explicit derivative $\partial\mathcal L/\partial x^\nu$ ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^der-c1b-7-5|Derivation §C1b.7.5]], step 3).
> - Math: the chain rule [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]; the divergence theorem in $\mathbb R^n$ [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]] (why a total derivative is allowed); differentiation under the integral [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]].
