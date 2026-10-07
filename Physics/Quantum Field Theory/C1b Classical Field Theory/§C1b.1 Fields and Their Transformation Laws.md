---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1a.7 Relativistic Electrodynamics in Index Form]] · ↑ [[· C1b Classical Field Theory]] · [[§C1b.2 The Action Principle and the Euler–Lagrange Equations]] →

*Sources: the user's PHY 513 notes, Ch. 2 §2.3 (fields, the Klein–Gordon equation), Ch. 3 §3.1 and §3.5 (general field law), Ch. 7 (how fields transform) · PHY 513 Lecture 2 (Larsen), Part B; Lecture 3, Part A · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.1, §3.1 · Yu Zhao-Huan, 量子场论讲义, §1.6.2.*

What is a relativistic field, and how does it transform? Relativity already says how a scalar field's components behave under a change of frame ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]) and which wave equation is the simplest invariant one ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-1|REL Theorem §B4.1.1]]); the Lorentz group and its generators are [[§C1a.4 The Lorentz Group|§C1a.4]]–[[§C1a.6 Infinitesimal Lorentz Transformations and Generators|§C1a.6]]. This section adds the transformation law as an action on whole field configurations (a representation, with its infinitesimal form, for a scalar and for a field with components) and the covariance of the Klein–Gordon equation. The Lagrangian is [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]; the principles that restrict it, locality and relativistic invariance, together with dimensional analysis, are [[§C1b.3 Mass Dimension, Locality and Power Counting|§C1b.3]].

*Conventions* ([[Larsen PHY 513]]): natural units $\hbar = c = 1$; $g = \operatorname{diag}(+,-,-,-)$; $\partial_\mu = \partial/\partial x^\mu = (\partial_t, \nabla)$, $\partial^2 = \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2$; Lorentz transformations act on points as $x \mapsto \Lambda x$, Poincaré transformations as $g\cdot x = \Lambda x + a$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^def-b1-2-4|REL Def. §B1.2.4]]), and $\Lambda = 1 + \omega$ near the identity with $\omega_{\mu\nu} = -\omega_{\nu\mu}$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]]). Relativity B keeps $c$ explicit; here it is set to one.

## Fields

> [!definition] Definition §C1b.1.1: Classical Field; Field Configuration
> A **classical field** with $n$ real components is a collection of functions $\phi_a : \mathbb R^{1,3} \to \mathbb R$, $a = 1, \dots, n$, of the spacetime point $x = (t, \mathbf x)$; a complex component counts as two real ones. A **field configuration** is one such collection on all of spacetime. In a field theory the values $\phi_a(t, \mathbf x)$ at one time are the coordinates of the system: one set of $n$ coordinates for each point $\mathbf x$ of space.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 ("A field is a function of when and where you are") · Yu §1.6.2 (the field as generalized coordinate, every spatial point a degree of freedom) · PHY 513 Lecture 2, Part B*

^def-c1b-1-1

## The scalar transformation law

> [!definition] Definition §C1b.1.2: Transformation Law of a Scalar Field
> A one-component field $\phi$ is a **scalar field** (spin $0$) if two observers related by the Poincaré transformation $x' = \Lambda x + a$ describe it by functions $\phi$ and $\phi'$ with
>
> $$
> \phi'(x') = \phi(x), \qquad\text{equivalently}\qquad \phi'(x) = \phi\bigl(\Lambda^{-1}(x - a)\bigr) .
> $$
>
> The value carries no Lorentz index; only the label of the point changes.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Definition "Transformation law of a scalar field"), Ch. 3 §3.5 (the translation form), Ch. 7 (Definition "Active and passive, and the rule for a scalar") · PS §3.1, eq. (3.2) · PHY 513 Lecture 2, Part B*

^def-c1b-1-2

The first form is Relativity's ([[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]); the second, the same law solved for the new function, is the one quantum field theory uses, because it says what happens to the function as a whole: it is a map on configurations, $\phi \mapsto \phi'$.

> [!caution] Caution: What "the scalar does not change" does not mean
> The law is not $\phi(\Lambda x) = \phi(x)$. That equation involves one function and says that $\phi$ takes the same value at $x$ and at $\Lambda x$ for every $\Lambda$, i.e. that $\phi$ is a Lorentz-invariant *function*; a generic configuration is not. The law involves two functions, $\phi$ and $\phi'$, describing one physical field: what is unchanged is the value at a given physical point, not the functional form. (Invariant functions are rare: for the proper orthochronous group they depend only on $x^2$ and, inside and on the light cone, on the sign of $x^0$, as for $\theta(x^0)\theta(x^2)$; the user's notes say "only of functions of $x^2$", which omits that sign. The orbits behind this are [[§C1a.4 The Lorentz Group#^thm-c1a-4-4|Theorem §C1a.4.4]]; the invariant distributions of this kind are [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]].)
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Caution "What 'φ does not change' does not mean")*

^cau-c1b-1-1

> [!remark] Remark: Why the inverse, and the two readings
> *Passively* (the slides' picture), one event carries two labels, $x$ and $x' = \Lambda x + a$, and both observers read the same number there: $\phi'(x') = \phi(x)$. *Actively* (Peskin–Schroeder's picture), there is one set of axes and the configuration is moved: a bump of $\phi$ at $x_0$ becomes a bump of $\phi'$ at $\Lambda x_0 + a$. To find the new value at $x$, look up where that point came from, $\Lambda^{-1}(x - a)$: the inverse is not a typo. It is also forced by composition: with the inverse, "first $g_1$, then $g_2$" equals "$g_2g_1$" ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]]). The two readings, for points, are [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]] and [[§C1a.4 The Lorentz Group#^cau-c1a-4-1|§C1a.4, Caution: Active and passive readings]].
>
> *Source: the user's PHY 513 notes, Ch. 7 (Definition "Active and passive, and the rule for a scalar") · PS §3.1, Fig. 3.1(a) · PHY 513 Lecture 2, Part B*

^rem-c1b-1-1

![[ph-qft-c1-8-1.svg]]
*The scalar law read actively. Left: level curves of a configuration $\phi$ in the $(x^1, t)$ plane, with its maximum at $x_0$. Right: the boosted configuration $\phi'(x) = \phi(\Lambda^{-1}x)$; every level curve has been carried along by $\Lambda$, so the maximum sits at $\Lambda x_0$ with the same value, on the same hyperbola $x^2 = x_0^2$ (dotted; red arrow). The dashed null lines are preserved by $\Lambda$. The values are unchanged; only their locations moved.*

## The general transformation law

> [!definition] Definition §C1b.1.3: Transformation Law of a General Field
> A field with components $\phi_a$ transforms under $x' = \Lambda x + a$ as
>
> $$
> \phi'_a(x') = D(\Lambda)_a{}^b\,\phi_b(x), \qquad D(\Lambda) = 1 + \tfrac12\,\omega_{\mu\nu}S^{\mu\nu} + O(\omega^2) \quad\text{for } \Lambda = 1 + \omega ,
> $$
>
> where $D$ is a finite-dimensional representation ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-5|Def. §C3.1.5]]) of the Lorentz group on the component index, $D(\Lambda_2)D(\Lambda_1) = D(\Lambda_2\Lambda_1)$, and the six matrices $S^{\mu\nu} = -S^{\nu\mu}$ are its **spin generators**. Translations do not act on the index. A scalar has $D = 1$, $S^{\mu\nu} = 0$; four-vector and spinor fields are [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-5|Theorem §C3.4.5]] and [[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]] (these $S^{\mu\nu}$ are real-convention: [[§C3.4 How Fields Transform under the Lorentz Group#^cau-c3-4-2|§C3.4, Caution: Two meanings of S^μν]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (Definition "Transformation law of a general field", eq. (generalfieldlaw)), Ch. 7, eq. (fieldtransforms) · PS §3.1, eq. (3.8)*

^def-c1b-1-3

> [!theorem] Theorem §C1b.1.1: The Field Laws Represent the Poincaré Group
> For $g = (\Lambda, a)$ let $T(g)$ send a configuration to the transformed one, $(T(g)\phi)_a(x) = D(\Lambda)_a{}^b\,\phi_b(g^{-1}x)$, $g^{-1}x = \Lambda^{-1}(x - a)$. Then $T(g)$ is linear in $\phi$, $T(1, 0) = 1$, and
>
> $$
> T(g_2)\,T(g_1) = T(g_2g_1) .
> $$
>
> Without the inverse, $(S(g)\phi)(x) = \phi(gx)$ would compose in the reverse order, $S(g_2)S(g_1) = S(g_1g_2)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 (Definition "Active and passive", "The inverse is not a typo"; Principle "Components and functions") · standard group-action argument, written out here*

^thm-c1b-1-1

> [!derivation]- Derivation
> **1. The group law of points.** Poincaré transformations compose as $g_2g_1 = (\Lambda_2\Lambda_1, \Lambda_2a_1 + a_2)$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-8|REL Theorem §B1.2.8]], 1), so $(g_2g_1)x = g_2(g_1x)$, and inverses reverse the order: $(g_2g_1)^{-1} = g_1^{-1}g_2^{-1}$.
>
> **2. Apply $T(g_1)$, then $T(g_2)$.** Write $\psi = T(g_1)\phi$, i.e. $\psi_b(y) = D(\Lambda_1)_b{}^c\,\phi_c(g_1^{-1}y)$ for every $y$. By the definition with $\psi$ in place of $\phi$,
>
> $$
> \bigl(T(g_2)\psi\bigr)_a(x) = D(\Lambda_2)_a{}^b\,\psi_b(g_2^{-1}x) = D(\Lambda_2)_a{}^b\,D(\Lambda_1)_b{}^c\,\phi_c\bigl(g_1^{-1}(g_2^{-1}x)\bigr) ,
> $$
>
> the second step being $\psi_b$ evaluated at the point $y = g_2^{-1}x$.
>
> **3. Combine.** The matrices multiply to $D(\Lambda_2)D(\Lambda_1) = D(\Lambda_2\Lambda_1)$ because $D$ is a representation ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]); the argument is $g_1^{-1}g_2^{-1}x = (g_2g_1)^{-1}x$ by step 1. Hence $(T(g_2)T(g_1)\phi)_a(x) = D(\Lambda_2\Lambda_1)_a{}^c\,\phi_c((g_2g_1)^{-1}x) = (T(g_2g_1)\phi)_a(x)$, since $g_2g_1$ has Lorentz part $\Lambda_2\Lambda_1$.
>
> **4. Identity and linearity.** $D(1) = 1$ and $(1, 0)^{-1}x = x$ give $T(1, 0)\phi = \phi$. Each $\phi_b$ enters $T(g)\phi$ linearly, so $T(g)(\alpha\phi + \beta\chi) = \alpha T(g)\phi + \beta T(g)\chi$.
>
> **5. Without the inverse.** For a scalar, $(S(g_2)S(g_1)\phi)(x) = (S(g_1)\phi)(g_2x) = \phi(g_1g_2x) = (S(g_1g_2)\phi)(x)$: the order is reversed. ⚑ By-product: the inverse in $\phi(\Lambda^{-1}x)$ is what makes the law a representation; it is not a convention → [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-1|Remark: Why the inverse]].
>
> **6. The two forms agree.** Put $x' = gx$ in $\phi'(x') = D\phi(x)$: $\phi'(x') = D\phi(g^{-1}x')$ for every $x'$, which is $T(g)\phi$ with the argument renamed.
>
> **What the derivation shows**
> - Two representations act at once: $D$ on the components at a point (finite-dimensional) and the motion of the argument on the space of functions (infinite-dimensional) → [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-2|Remark: Two representations at once]].
> - Assumption used: $D$ itself is a representation; for spinors it is one only up to sign ([[§C5a.1 Weyl Spinors and SL(2,C)#^thm-c5a-1-9|Theorem §C5a.1.9]]).
> - Used next: the infinitesimal form ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]]); in the quantum theory $T(g)$ is implemented by unitary operators on states, $U^{-1}\phi U = T(g)\phi$ ([[§C3.5 Quantum Poincaré Transformations#^pr-c3-5-8|Principle §C3.5.8]]; for the free field a theorem, [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-12|Theorem §C3.5.12]]).

^der-c1b-1-1

*Uses:* [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-8|REL Theorem §B1.2.8]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]

> [!theorem] Theorem §C1b.1.2: Infinitesimal Form of the Field Laws
> For $\Lambda = 1 + \omega$ and $a$ infinitesimal, to first order in $\omega$ and $a$:
>
> $$
> \phi'(x) = \phi(x) - a^\mu\partial_\mu\phi(x) + \tfrac12\,\omega_{\mu\nu}\bigl(x^\mu\partial^\nu - x^\nu\partial^\mu\bigr)\phi(x) \qquad\text{(scalar)},
> $$
>
> $$
> \phi'_a(x) = \phi_a(x) - a^\mu\partial_\mu\phi_a(x) + \tfrac12\,\omega_{\mu\nu}\Bigl[\bigl(x^\mu\partial^\nu - x^\nu\partial^\mu\bigr)\delta_a{}^b + (S^{\mu\nu})_a{}^b\Bigr]\phi_b(x) \qquad\text{(general)}.
> $$
>
> The first bracket (**orbital** part) is the same for every field; the second (**spin** part) acts on the components only.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (Derivation "Computing Δφ", Lorentz case; "Lorentz transformations, all fields at once", step 1), Ch. 7 (Derivation "The generator of the scalar transformation law is the orbital operator") · PS §2.2, p. 18 (the translation)*

^thm-c1b-1-2

> [!derivation]- Derivation
> **1. The inverse to first order.** $(1 + \omega)(1 - \omega) = 1 - \omega^2$, so $\Lambda^{-1} = 1 - \omega + O(\omega^2)$, i.e. $(\Lambda^{-1})^\mu{}_\nu = \delta^\mu{}_\nu - \omega^\mu{}_\nu + O(\omega^2)$.
>
> **2. The shifted point.** $(g^{-1}x)^\mu = (\Lambda^{-1})^\mu{}_\nu(x^\nu - a^\nu) = x^\mu - a^\mu - \omega^\mu{}_\nu x^\nu + \omega^\mu{}_\nu a^\nu + O(\omega^2)$. The term $\omega^\mu{}_\nu a^\nu$ is a product of two first-order quantities and is dropped (second order). So $g^{-1}x = x + h$ with $h^\mu = -a^\mu - \omega^\mu{}_\nu x^\nu$.
>
> **3. Taylor's theorem.** For a $C^2$ field, $\phi_b(x + h) = \phi_b(x) + h^\mu\partial_\mu\phi_b(x) + O(h^2)$ (the expansion in index form: [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]). With step 2,
>
> $$
> \phi_b(g^{-1}x) = \phi_b(x) - a^\mu\partial_\mu\phi_b(x) - \omega^\mu{}_\nu\,x^\nu\,\partial_\mu\phi_b(x) + O(2) .
> $$
>
> **4. Lower the index on ω.** $\omega^\mu{}_\nu\partial_\mu = g^{\mu\rho}\omega_{\rho\nu}\partial_\mu = \omega_{\rho\nu}\partial^\rho$, so the last term is $-\omega_{\rho\nu}\,x^\nu\partial^\rho\phi_b$. Only index positions moved; no sign appears, because the metric was applied to a contracted pair ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-1|§C1a.5, Caution: A contraction is a plain sum]]).
>
> **5. Antisymmetrize.** Split $\omega_{\rho\nu}x^\nu\partial^\rho$ into two halves and in the second rename $\rho \leftrightarrow \nu$, then use $\omega_{\nu\rho} = -\omega_{\rho\nu}$: $\omega_{\rho\nu}x^\nu\partial^\rho = \tfrac12\omega_{\rho\nu}x^\nu\partial^\rho + \tfrac12\omega_{\nu\rho}x^\rho\partial^\nu = \tfrac12\omega_{\rho\nu}\bigl(x^\nu\partial^\rho - x^\rho\partial^\nu\bigr)$. Hence, renaming $\rho \to \mu$,
>
> $$
> -\omega_{\rho\nu}x^\nu\partial^\rho\phi_b = \tfrac12\,\omega_{\mu\nu}\bigl(x^\mu\partial^\nu - x^\nu\partial^\mu\bigr)\phi_b .
> $$
>
> Only the antisymmetric part of the operator survives contraction with $\omega$; writing it antisymmetric makes the coefficient of each independent parameter $\omega_{\mu\nu}$ ($\mu < \nu$) unique. ⚑ By-product: this coefficient is the orbital generator, $x^\mu\partial^\nu - x^\nu\partial^\mu = -i\hat L^{\mu\nu}$ with $\hat L^{\mu\nu} = i(x^\mu\partial^\nu - x^\nu\partial^\mu)$ ([[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-1|Def. §C3.4.1]]), the same differential operator for every field → [[§C1b.1 Fields and Their Transformation Laws#^rem-c1b-1-2|Remark: Two representations at once]].
>
> **6. Scalar.** $D = 1$: steps 3–5 give the first formula.
>
> **7. General field.** Multiply step 3 (with step 5) by $D(\Lambda)_a{}^b = \delta_a{}^b + \tfrac12\omega_{\mu\nu}(S^{\mu\nu})_a{}^b + O(\omega^2)$. The four products are: $\delta\cdot\phi_b \to \phi_a$; $\delta\cdot(\text{first-order terms}) \to$ those terms with $b = a$; $\tfrac12\omega S\cdot\phi_b \to \tfrac12\omega_{\mu\nu}(S^{\mu\nu})_a{}^b\phi_b$; $\tfrac12\omega S\cdot(\text{first-order terms})$, second order, dropped. The sum is the second formula. Translations carry no matrix ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]), so the $a$-term has $\delta_a{}^b$.
>
> **What the derivation shows**
> - The translation generator is $-\partial_\mu$ for every field: the argument shifts opposite to the coordinates (for $x' = x - a$, $\phi'(x) = \phi(x + a)$, as in PS §2.2).
> - Assumptions: $\phi$ is $C^1$ (here $C^2$ for the remainder estimate); first order means dropping $\omega^2$, $a^2$ and $\omega a$.
> - Used next: the generators $\Delta\phi$ of Noether's theorem for translations and Lorentz transformations ([[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]); the spin part produces the spin current of the Lorentz current and the antisymmetric part of the canonical energy–momentum tensor ([[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-2|Theorem §C1b.7.2]]).

^der-c1b-1-2

*Uses:* [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-1|Theorem §C1a.6.1]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]]

> [!example] Example §C1b.1.1: The Four-Vector Field
> A four-vector field $A^\alpha$ transforms with $D = \Lambda$: $A'^\alpha(x) = \Lambda^\alpha{}_\beta A^\beta(\Lambda^{-1}x)$. Its spin generators are the generators of the vector representation,
>
> $$
> (S^{\mu\nu})^\alpha{}_\beta = g^{\mu\alpha}\delta^\nu{}_\beta - g^{\nu\alpha}\delta^\mu{}_\beta, \qquad \tfrac12\,\omega_{\mu\nu}(S^{\mu\nu})^\alpha{}_\beta = \omega^\alpha{}_\beta .
> $$
>
> On lower components $A_\alpha$ the matrix is $D = \Lambda_\alpha{}^\beta$ and the generators are $(S^{\mu\nu})_\alpha{}^\beta = \delta^\mu_\alpha g^{\nu\beta} - \delta^\nu_\alpha g^{\mu\beta}$ (minus the transpose), with $\tfrac12\omega_{\mu\nu}(S^{\mu\nu})_\alpha{}^\beta = \omega_\alpha{}^\beta$.
>
> *Check.* $\tfrac12\omega_{\mu\nu}g^{\mu\alpha}\delta^\nu{}_\beta = \tfrac12\omega^\alpha{}_\beta$ and $-\tfrac12\omega_{\mu\nu}g^{\nu\alpha}\delta^\mu{}_\beta = -\tfrac12\omega_\beta{}^\alpha$. Antisymmetry, $\omega_{\beta\rho}g^{\rho\alpha} = -\omega_{\rho\beta}g^{\rho\alpha}$, gives $\omega_\beta{}^\alpha = -\omega^\alpha{}_\beta$, so the sum is $\omega^\alpha{}_\beta$, the first-order part of $\Lambda^\alpha{}_\beta$. For lower components, $\tfrac12\omega_{\mu\nu}\delta^\mu_\alpha g^{\nu\beta} = \tfrac12\omega_\alpha{}^\beta$ and $-\tfrac12\omega_{\mu\nu}\delta^\nu_\alpha g^{\mu\beta} = -\tfrac12\omega^\beta{}_\alpha = \tfrac12\omega_\alpha{}^\beta$; and $\Lambda_\alpha{}^\beta = g_{\alpha\mu}\Lambda^\mu{}_\nu g^{\nu\beta} = \delta_\alpha{}^\beta + \omega_\alpha{}^\beta$. The vector representation and its generators are [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] and [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]]; the vector field itself is [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-5|Theorem §C3.4.5]] (its quantization: massive, [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^pr-c4-4-2|Principle §C4.4.2]], [[§C4.4★ Quantizing the Proca Field꞉ Modes and the Mode Algebra#^thm-c4-4-7|Theorem §C4.4.7]]; photon, [[§C4.7 Covariant Quantization and the Indefinite Metric#^pr-c4-7-5|Principle §C4.7.5]], [[§C4.7 Covariant Quantization and the Indefinite Metric#^thm-c4-7-11|Theorem §C4.7.11]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.5 (Definition "Transformation law of a general field": the lower-component form with its check), Ch. 1 §1.6 (generators in the vector representation) · PS §3.1, p. 37*

^ex-c1b-1-1

> [!remark] Remark: Two representations at once
> The law $\phi'_a(x) = D(\Lambda)_a{}^b\phi_b(\Lambda^{-1}x)$ combines a finite-dimensional representation $D$, acting on the components at one point (generators $S^{\mu\nu}$), with an infinite-dimensional one, acting on functions by moving the point (generators $x^\mu\partial^\nu - x^\nu\partial^\mu$). For a scalar the first is trivial, every element represented by the number $1$ (in the classification of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], the representation $(0, 0)$: [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-4|Theorem §C3.4.4]]), but the scalar still changes through the second. Under parity a one-component field may still change sign: $D(P) = +1$ for a scalar, $-1$ for a pseudoscalar (QFT C9, planned). A Lagrangian density must lie in the trivial representation for the action to be invariant ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]]); "contract all indices" is the rule that extracts that piece.
>
> *Source: the user's PHY 513 notes, Ch. 7 (Principle "Components and functions: the scalar field carries the trivial representation")*

^rem-c1b-1-2

## The Klein–Gordon equation

The simplest invariant wave equation for a scalar field is the Klein–Gordon equation $(\partial^2 + m^2)\phi = 0$. Its home is [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-1|REL Theorem §B4.1.1]] (from the mass shell) and [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-4|REL Theorem §B4.1.4]] (from a Lagrangian); its plane waves $e^{-ik\cdot x}$ solve it exactly when $k^2 = m^2$, $\omega = \sqrt{\mathbf k^2 + m^2}$ ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]]), which with $\hbar = c = 1$ is $E = \sqrt{\mathbf p^2 + m^2}$. What field theory needs in addition is that the equation is invariant as an equation for configurations.

> [!theorem] Theorem §C1b.1.3: The Klein–Gordon Equation Is Poincaré Covariant
> If $\phi$ is a $C^2$ scalar field and $\phi'(x) = \phi(\Lambda^{-1}(x - a))$, then
>
> $$
> \bigl((\partial^2 + m^2)\phi'\bigr)(x) = \bigl((\partial^2 + m^2)\phi\bigr)\bigl(\Lambda^{-1}(x - a)\bigr) .
> $$
>
> So $\phi'$ solves the Klein–Gordon equation if and only if $\phi$ does: the operator $\partial^2 + m^2$ commutes with every $T(g)$ of [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]], and the space of solutions is carried into itself.
>
> *Source: PS §3.1, eqs. (3.3)–(3.5) and the line after (3.5) · the user's PHY 513 notes, Ch. 2 §2.3 (Principle "Klein–Gordon equation": "invariant because ∂μ∂^μ is a contraction and φ is a scalar") · PHY 513 Lecture 2, Part B*

^thm-c1b-1-3

> [!derivation]- Derivation
> **1. The inner map.** Let $y = \Lambda^{-1}(x - a)$, i.e. $y^\rho = (\Lambda^{-1})^\rho{}_\sigma(x^\sigma - a^\sigma)$. Its derivatives are constants: $\partial y^\rho/\partial x^\mu = (\Lambda^{-1})^\rho{}_\mu$; the translation $a$ drops out.
>
> **2. One derivative.** By the chain rule ([[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]), $\partial_\mu\phi'(x) = \dfrac{\partial y^\rho}{\partial x^\mu}(\partial_\rho\phi)(y) = (\Lambda^{-1})^\rho{}_\mu\,(\partial_\rho\phi)(y)$.
>
> **3. Two derivatives.** Differentiate again; the coefficient is constant and passes through: $\partial_\nu\partial_\mu\phi'(x) = (\Lambda^{-1})^\rho{}_\mu(\Lambda^{-1})^\sigma{}_\nu\,(\partial_\sigma\partial_\rho\phi)(y)$.
>
> **4. Contract with the metric.** $\partial^2\phi'(x) = g^{\mu\nu}\partial_\nu\partial_\mu\phi'(x) = g^{\mu\nu}(\Lambda^{-1})^\rho{}_\mu(\Lambda^{-1})^\sigma{}_\nu\,(\partial_\sigma\partial_\rho\phi)(y)$. Since $\Lambda^{-1}$ is a Lorentz transformation ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]]) and $g^{\mu\nu}$ is an invariant tensor ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]]), $(\Lambda^{-1})^\rho{}_\mu(\Lambda^{-1})^\sigma{}_\nu g^{\mu\nu} = g^{\rho\sigma}$ (PS eq. (3.4)). Hence $\partial^2\phi'(x) = g^{\rho\sigma}(\partial_\sigma\partial_\rho\phi)(y) = (\partial^2\phi)(y)$.
>
> **5. The mass term.** $m^2\phi'(x) = m^2\phi(y)$ by the definition of $\phi'$. Adding step 4 gives the statement.
>
> **6. Both directions.** If $(\partial^2 + m^2)\phi = 0$ everywhere, the right side vanishes for every $x$, so $(\partial^2 + m^2)\phi' = 0$. Conversely $\phi = T(g^{-1})\phi'$ ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]]), and the same argument applies. ⚑ By-product: $\partial^2 + m^2$ commutes with the representation $T$; its solution space is a representation of the Poincaré group, the classical seed of the one-particle states of [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-11|Theorem §C3.5.11]], and the reason the Wightman function is invariant ([[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]]).
>
> **What the derivation shows**
> - Only two facts were used: derivatives of a scalar transform with $\Lambda^{-1}$ (a covector law, [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]]), and the metric is invariant. Any fully contracted equation behaves the same way.
> - Assumption: $\phi \in C^2$. For a distributional solution the same identity holds with derivatives taken in the sense of distributions and the change of variables of [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]].
> - Used next: the general statement that a scalar Lagrangian density gives an invariant action and covariant field equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]]).

^der-c1b-1-3

*Uses:* [[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-2|Def. §C1b.1.2]], [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]], [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]]

> [!remark] Remark: What the Klein–Gordon equation is, and what it is not
> - *A massive, polarization-free photon.* Its plane waves are light waves without a polarization index and with a mass. The mass keeps the kinematics honest: a sign error in the equation would show up as $\omega^2 = \mathbf k^2 - m^2$.
> - *Wave and particle at once.* The dispersion relation of the wave is the energy–momentum relation of the particle; which aspect one uses depends on the question.
> - *Not a limit of the Schrödinger equation.* Limits go the other way: the nonrelativistic limit of Klein–Gordon is Schrödinger's equation ([[§B4.1 The Klein–Gordon Equation|REL §B4.1]], Connections), but a relativistic theory cannot be derived from a nonrelativistic one. Klein–Gordon is a proposal, to be judged on its own terms; [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|Theorem §C1b.3.6]] says why it is essentially forced.
> - *A classical field equation.* Here, as in PS, it is the equation of a classical field, like Maxwell's, not a one-particle wave equation; read as the latter it fails ([[§C1a.1 Why Quantum Field Theory|§C1a.1]], [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-2|QM Theorem §C13.1.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Discussion), Ch. 3 §3.1 · PHY 513 Lecture 3, Part A ("Toy model for photon") · PS §2.2, p. 17*

^rem-c1b-1-3

> [!caution] Caution: Localized solutions
> The user's notes (Ch. 3 §3.1, Discussion) answer "Are there solutions with compact support?" with "No; any superposition of plane waves is spread out." Read literally this is too strong. A real solution with compactly supported Cauchy data $(\phi, \dot\phi)$ at $t = 0$ exists, and by finite propagation speed it stays inside the light cones of that region, so it has compact support in space at every time. What is true: (i) no nonzero solution has compact support in *spacetime* (it would vanish with its time derivative at some early time, and the Cauchy problem has a unique solution); (ii) a single plane wave, or any solution of one frequency sign, cannot be confined, which is the point the notes make and the one that matters for particles ([[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.1 (Discussion "Are there solutions with compact support?"); (i) and the finite propagation speed are standard (Hörmander I; here [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-13|Theorem §C2b.4.13]], whose propagator vanishes outside the cone)*

^cau-c1b-1-2

> [!remark]- Connections
> - The scalar law $\phi'(x') = \phi(x)$ is the rank-zero case of Relativity's tensor-field law; field theory reads it as a map on whole configurations, which is what makes it a representation — [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]], [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]].
> - The inverse in $\phi(\Lambda^{-1}x)$ is the same inverse that makes $\psi(x) \mapsto \psi(x - a)$ the translation of a wave function in quantum mechanics, generated by the momentum; for fields the generator is $-\partial_\mu$, and the Noether charge of translations is the momentum — [[§C2.2 Translation and Momentum as Its Generator#^pr-c2-2-4|QM Principle §C2.2.4]], [[§C1b.6 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-6-6|Theorem §C1b.6.6]].
> - The orbital operator $x^\mu\partial^\nu - x^\nu\partial^\mu$ of the infinitesimal law contains, for spatial indices, the orbital angular momentum $\mathbf x \times \nabla$ of quantum mechanics; the spin matrices $S^{\mu\nu}$ add the spin, so $J = L + S$ is already visible classically, and the Noether charges of rotations split the same way — [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-2|Theorem §C1b.1.2]], [[§C1b.7 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-7-1|Theorem §C1b.7.1]], [[§C3.4 How Fields Transform under the Lorentz Group#^thm-c3-4-3|Theorem §C3.4.3]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-10|Theorem §C3.5.10]].
> - The spin generators of a vector field are exactly the generators of the vector representation; for a Dirac spinor they will be $\frac14[\gamma^\mu, \gamma^\nu]$ — [[§C1b.1 Fields and Their Transformation Laws#^ex-c1b-1-1|Example §C1b.1.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-4|Def. §C5a.2.4]], [[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-5|Def. §C5a.2.5]].
> - That $\partial^2 + m^2$ commutes with every Poincaré transformation is why a Poincaré transform of a solution is a solution, why the quantum field's two-point function is invariant, and why its solution space carries the one-particle representation — [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-3|Theorem §C1b.1.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-11|Theorem §C3.5.11]].
> - The transformation law is what the principle of relativistic invariance asks the Lagrangian density to respect; together with locality and power counting it leaves the scalar Lagrangian with four parameters — [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-5|Principle §C1b.3.5]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|Theorem §C1b.3.6]].
> - Invariant functions and distributions on spacetime depend only on $x^2$ and, on and inside the cone, on the sign of $x^0$ — [[§C1b.1 Fields and Their Transformation Laws#^cau-c1b-1-1|Caution: What "the scalar does not change" does not mean]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]].
