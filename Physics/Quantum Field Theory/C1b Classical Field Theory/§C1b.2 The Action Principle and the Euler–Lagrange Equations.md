---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.1 Fields and Their Transformation Laws]] · ↑ [[· C1b Classical Field Theory]] · [[§C1b.3 Mass Dimension, Locality and Power Counting]] →

*Sources: the user's PHY 513 notes, Ch. 2 §2.3 ("Actions and Lagrangian densities"), Ch. 3 §§3.1–3.3 · PHY 513 Lecture 2, Part B; Lecture 3, Part A (Larsen) · PHY 513 Problem Set 2, Problem 3(a), (c), with the course solution · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2, §3.1 · Yu Zhao-Huan, 量子场论讲义, §1.6 · the user's pre-course notes, §1.6.*

How does a field theory produce its equations of motion? The particle version is Hamilton's principle ([[§B6.2 Hamilton's Principle of Stationary Action#^pr-b6-2-1|CM Principle §B6.2.1]]), with the calculus of variations of [[§B5.1 The Euler–Lagrange Equation|CM §B5.1]]; Relativity has the action of one real scalar field and its Euler–Lagrange equation, with $c$ explicit ([[§B4.1 The Klein–Gordon Equation#^def-b4-1-1|REL Def. §B4.1.1]], [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-2|REL Theorem §B4.1.2]]). This section states the action principle for any number of field components in natural units, makes the variation and the functional derivative precise (the latter is a distribution), proves the Euler–Lagrange equations with every surface term accounted for, and is the single home of the Lagrangian densities of the free real and complex scalar fields. The Hamiltonian form is [[§C1b.4 Hamiltonian Field Theory|§C1b.4]], symmetries and currents [[§C1b.5 Noether's Theorem|§C1b.5]].

*Conventions* ([[Larsen PHY 513]]): natural units $\hbar = c = 1$, so $d^4x = dt\,d^3x$ and the action is dimensionless, $[\mathcal L] = 4$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]); $g = \operatorname{diag}(+,-,-,-)$; $(\partial\phi)^2 \equiv \partial_\mu\phi\,\partial^\mu\phi = \dot\phi^2 - (\nabla\phi)^2$. Relativity B writes $S = \frac1c\int\mathcal L\,d^4x$ with $x^0 = ct$; here $c = 1$.

## Action and Lagrangian density

> [!definition] Definition §C1b.2.1: Lagrangian Density
> For fields $\phi_a$, $a = 1, \dots, n$, a **Lagrangian density** is a function $\mathcal L(\phi_a, \partial_\mu\phi_a)$ of the fields and their first derivatives at one point.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3, eq. (actiondensity); Ch. 3 §3.2, eqs. (action3), (Lform) · PS §2.2, eq. (2.1) · Yu §1.6.2, eq. (1.163) · PHY 513 Lecture 3, Part A*

^def-c1b-2-1

> [!definition] Definition §C1b.2.2: Action
> The **action** of a configuration $\phi_a$ on a bounded spacetime region $R$ is the functional
>
> $$
> S_R[\phi] = \int_R d^4x\;\mathcal L\bigl(\phi_a(x), \partial_\mu\phi_a(x)\bigr) ,
> $$
>
> with $\mathcal L$ the Lagrangian density ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-1|Def. §C1b.2.1]]): a number for each configuration. For a slab $R$, $t_1 \le t \le t_2$, it is $S_R = \int dt\,L$ with the **Lagrangian** $L(t) = \int d^3x\;\mathcal L$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3, eq. (actiondensity); Ch. 3 §3.2, eqs. (action3), (Lform) · PS §2.2, eq. (2.1) · Yu §1.6.2, eq. (1.163) · PHY 513 Lecture 3, Part A*

^def-c1b-2-2

> [!caution] Caution: Action, Lagrangian, Lagrangian density
> Three objects related by integration: $S = \int dt\,L$, $L = \int d^3x\,\mathcal L$. Physicists, PS ("we will refer to $\mathcal L$ simply as the Lagrangian"), Yu and Problem Set 2 call $\mathcal L$ "the Lagrangian"; the same happens to the Hamiltonian $H$ and its density $\mathcal H$ ([[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]]). In relativistic field theory $L$ itself almost never appears, because it treats time and space differently. Where a problem asks for "the Hamiltonian", it means $H$, integrated.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.2 (Caution "Action, Lagrangian, Lagrangian density") · PHY 513 Lecture 3, Part A ("density often omitted, sorry") · PHY 513 Problem Set 2 (note on terminology)*

^cau-c1b-2-1

> [!remark] Remark: Why only first derivatives
> The restriction to $\mathcal L(\phi, \partial_\mu\phi)$ has content. It makes the field equations second order, so that a field and its time derivative on one time slice determine the solution, as in mechanics. Densities with higher derivatives generically give Hamiltonians unbounded below (Ostrogradsky's theorem, stated in the user's notes, not proved here). A second-order effect is obtained by squaring a first derivative, not by differentiating twice; and second derivatives that appear only inside a total divergence are harmless ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.2 · PHY 513 Lecture 3, Part A ("Comment: depends on first derivatives")*

^rem-c1b-2-1

> [!theorem] Theorem §C1b.2.1: A Scalar Lagrangian Density Gives an Invariant Action
> Let the fields transform by their laws, $\phi' = T(g)\phi$ for $g = (\Lambda, a)$ ([[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]]), and let $\mathcal L$ be a scalar: $\mathcal L(\phi'(x), \partial\phi'(x)) = \mathcal L(\phi(y), \partial\phi(y))$ at $y = g^{-1}x$. Then for every region $R$
>
> $$
> S_{gR}[\phi'] = S_R[\phi] ,
> $$
>
> and $\phi'$ makes the action stationary on $gR$ exactly when $\phi$ does on $R$: the transform of a solution is a solution.
>
> *Source: PS §3.1, eq. (3.5) and the sentence after it · Yu §1.6.2 (d⁴x invariant, ℒ a Lorentz scalar ⇒ S invariant) · the user's pre-course notes, §1.6 (Keypoint "Lorentz invariance of the action") · the user's PHY 513 notes, Ch. 3 §3.3 ("a Lorentz transform of a solution is again a solution")*

^thm-c1b-2-1

> [!derivation]- Derivation
> **1. Write out the transformed action.** By the scalar property, $S_{gR}[\phi'] = \int_{gR}d^4x\;\mathcal L\bigl(\phi(g^{-1}x), \partial\phi(g^{-1}x)\bigr)$.
>
> **2. Change variables.** Substitute $x = gy = \Lambda y + a$. The Jacobian matrix is $\partial x^\mu/\partial y^\nu = \Lambda^\mu{}_\nu$, so $d^4x = |\det\Lambda|\,d^4y = d^4y$, since $\det\Lambda = \pm1$ ([[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]]; [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]]); $x \in gR$ exactly when $y \in R$. By the change-of-variables theorem ([[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]]),
>
> $$
> S_{gR}[\phi'] = \int_R d^4y\;\mathcal L\bigl(\phi(y), \partial\phi(y)\bigr) = S_R[\phi] .
> $$
>
> **3. The kinetic term is a scalar (example of the hypothesis).** With $\phi'(x) = \phi(y)$, $\partial_\mu\phi'(x) = (\Lambda^{-1})^\nu{}_\mu(\partial_\nu\phi)(y)$ ([[§C1b.1 Fields and Their Transformation Laws#^der-c1b-1-3|Derivation §C1b.1.3]], step 2), so $g^{\mu\rho}\partial_\mu\phi'\,\partial_\rho\phi'(x) = g^{\mu\rho}(\Lambda^{-1})^\nu{}_\mu(\Lambda^{-1})^\sigma{}_\rho(\partial_\nu\phi\,\partial_\sigma\phi)(y) = (g^{\nu\sigma}\partial_\nu\phi\,\partial_\sigma\phi)(y)$ by invariance of $g$ (PS eqs. (3.3)–(3.5)). Any polynomial in $\phi$ is a scalar trivially.
>
> **4. Variations are carried along.** $T(g)$ is linear, so $T(g)(\phi + \varepsilon\eta) = \phi' + \varepsilon\,T(g)\eta$, and $(T(g)\eta)_a(x) = D(\Lambda)_a{}^b\,\eta_b(g^{-1}x)$ (for a scalar, $\eta(g^{-1}x)$) is smooth and supported in $g(\operatorname{supp}\eta)$, a compact subset of the interior of $gR$ when $\operatorname{supp}\eta$ is one of $R$. Conversely every such variation on $gR$ is $T(g)\eta$ for $\eta = T(g^{-1})\eta'$. By step 2 applied to $\phi + \varepsilon\eta$, $S_{gR}[\phi' + \varepsilon T(g)\eta] = S_R[\phi + \varepsilon\eta]$ for every $\varepsilon$, so the first variations agree ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]), and one vanishes for all variations exactly when the other does.
>
> **What the derivation shows**
> - Two invariances do all the work: of the measure ($|\det\Lambda| = 1$) and of the density. ⚑ By-product: for improper $\Lambda$ (parity, time reversal) the measure is still invariant, so the question is only whether $\mathcal L$ is (QFT C9, planned).
> - The field equations of a scalar $\mathcal L$ are therefore covariant without being checked; for Klein–Gordon the direct check is [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-3|Theorem §C1b.1.3]].
> - Used next: Noether's theorem is the infinitesimal, local version of this invariance ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-3|Theorem §C1b.7.3]]).

^der-c1b-2-1

*Uses:* [[§C1b.1 Fields and Their Transformation Laws#^thm-c1b-1-1|Theorem §C1b.1.1]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]], [[§25 Change of Variables on General Domains#^thm-25-6|452 Thm. §25.6]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]

## The action principle

> [!definition] Definition §C1b.2.3: Variation; First Variation
> A **variation** of a configuration on $R$ is $\phi_a \to \phi_a + \varepsilon\eta_a$ with $\eta_a$ smooth and vanishing outside a compact subset of the interior of $R$ (test functions, [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]]), compared **at the same point** $x$; $\delta\phi_a \equiv \varepsilon\eta_a$. The **first variation** is $\delta S[\phi; \eta] = \dfrac{d}{d\varepsilon}S_R[\phi + \varepsilon\eta]\Big|_{\varepsilon = 0}$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Definition "What a variation is, and when it commutes with ∂μ", eq. (vardef); the functional derivative "defined" by δS = ∫(δS/δφ)δφ + boundary terms) · [[§B5.1 The Euler–Lagrange Equation#^def-b5-1-2|CM Def. §B5.1.2]] (first variation) · Yu §1.6.1 (δt = 0)*

^def-c1b-2-3

> [!definition] Definition §C1b.2.4: Functional Derivative
> For a functional $S$ with first variation $\delta S[\phi; \eta]$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]), the **functional derivative** $\delta S/\delta\phi_a(x)$ is the distribution with
>
> $$
> \delta S[\phi; \eta] = \sum_a\int d^4x\;\frac{\delta S}{\delta\phi_a(x)}\,\eta_a(x) \qquad\text{for every test function } \eta .
> $$
>
> For functionals of fields on a time slice the same definitions hold with $d^3x$.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Definition "What a variation is, and when it commutes with ∂μ", eq. (vardef); the functional derivative "defined" by δS = ∫(δS/δφ)δφ + boundary terms) · [[§B5.1 The Euler–Lagrange Equation#^def-b5-1-2|CM Def. §B5.1.2]] (first variation) · Yu §1.6.1 (δt = 0)*

^def-c1b-2-4

> [!remark] Remark: The functional derivative is a distribution
> The first variation is linear in $\eta$; "$\delta S/\delta\phi(x)$" names its kernel, and nothing guarantees a kernel that is a function. The simplest functional, evaluation at a point, $F_y[\phi] = \phi(y)$, has $\delta F_y[\phi; \eta] = \eta(y) = \int d^4x\,\delta^4(x - y)\,\eta(x)$, so
>
> $$
> \frac{\delta\phi(y)}{\delta\phi(x)} = \delta^4(x - y) ,
> $$
>
> an identity of distributions in $x$ ([[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]): the continuum version of $\partial q_j/\partial q_i = \delta_{ij}$. For a local action the kernel is an ordinary continuous function ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]), and then it is unique, since a continuous function is fixed by its integrals against test functions ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2). Its mass dimension is $[\delta S/\delta\phi] = 4 - [\phi] = 3$ for a scalar. The same delta function, on a time slice, is the field Poisson bracket ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]]) and, after quantization, the canonical commutator ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (mass dimension 3; the fundamental lemma) and Ch. 2 §2.3 (Derivation "Taylor expansion in index notation": the functional Taylor series) · the delta-function form written out here*

^rem-c1b-2-2

> [!theorem] Theorem §C1b.2.2: The Variation Commutes with Derivatives
> For a variation at fixed argument, to first order in $\varepsilon$,
>
> $$
> \delta(\partial_\mu\phi_a) = \partial_\mu(\delta\phi_a), \qquad \delta\mathcal L = \sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a}\,\delta\phi_a + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\,\partial_\mu(\delta\phi_a)\Bigr] .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3, eq. (varcommute) · Yu §1.6.2, eq. (1.164) · PHY 513 Lecture 3, Part A ("Notes: δ(∂µϕ) = ∂µ(δϕ)")*

^thm-c1b-2-2

> [!derivation]- Derivation
> **1. The derivative of the varied field.** At the same point $x$, $\partial_\mu(\phi_a + \varepsilon\eta_a) - \partial_\mu\phi_a = \varepsilon\,\partial_\mu\eta_a = \partial_\mu(\delta\phi_a)$, by linearity of $\partial_\mu$. Both terms are functions of the same $x$; this is where "fixed argument" is used.
>
> **2. The density.** $\mathcal L$ is $C^2$ in its $5n$ arguments $(\phi_a, \partial_\mu\phi_a)$. Taylor's theorem in those arguments, with increments $\varepsilon\eta_a$ and $\varepsilon\partial_\mu\eta_a$ (step 1), gives $\mathcal L(\phi + \varepsilon\eta, \partial\phi + \varepsilon\partial\eta) - \mathcal L(\phi, \partial\phi) = \varepsilon\sum_a\bigl[\frac{\partial\mathcal L}{\partial\phi_a}\eta_a + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\partial_\mu\eta_a\bigr] + O(\varepsilon^2)$, the derivatives evaluated at the unvaried configuration. There is no third term because $\mathcal L$ has no second derivatives.
>
> **3. When the point moves.** If $\phi'(x') = \phi(x) + \delta\phi$ with $x' = x + \delta x$, then $\phi'(x') - \phi(x) = [\phi'(x) - \phi(x)] + \partial_\mu\phi\,\delta x^\mu + \dots$, and $\partial_\mu$ of the second piece contains $\partial_\mu(\delta x^\nu)$: the derivative does not commute with the total change. ⚑ By-product: Noether's theorem needs the fixed-argument part $\bar\delta\phi = \delta\phi - \partial_\mu\phi\,\delta x^\mu$ → [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|Theorem §C1b.7.1]].
>
> **What the derivation shows**
> - "$\delta$ obeys the rules of differentiation" is Taylor's theorem in the arguments of $\mathcal L$, valid because the variation is a difference of two functions of one point.
> - Assumption: $\mathcal L \in C^2$, $\eta$ smooth.
> - Used next: step 2 of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]]; in Noether's theorem with $\varepsilon\eta$ replaced by the symmetry variation $\alpha\Delta\phi$, which need not vanish on the boundary ([[§C1b.5 Noether's Theorem#^rem-c1b-5-4|§C1b.5, Remark: Why the variation passes inside the derivative]], [[§C1b.5 Noether's Theorem#^thm-c1b-5-2|Theorem §C1b.5.2]]).

^der-c1b-2-2

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]]

> [!remark] Remark: When the point moves, the variation no longer commutes with ∂
> The first identity of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]] fails for transformations that also move the point, $x \to x'$, where the total change $\phi'(x') - \phi(x)$ does not commute with $\partial_\mu$ (step 3 of the derivation). Noether's theorem therefore distinguishes the instances of $\delta$ ([[§C1b.5 Noether's Theorem#^def-c1b-5-1|Def. §C1b.5.1]]) and works with the fixed-argument part of the change ([[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-1|Theorem §C1b.7.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Definition "What a variation is, and when it commutes with ∂μ")*

^rem-c1b-2-3

> [!principle] Principle §C1b.2.3: Stationary Action for Fields
> A configuration $\phi_a$ is a classical solution exactly when, on every bounded region $R$, its action is stationary under all variations that vanish near the boundary of $R$:
>
> $$
> \delta S_R[\phi; \eta] = 0 \qquad\text{for every test function } \eta \text{ supported inside } R .
> $$
>
> *Domain:* classical fields with a local action ([[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|Principle §C1b.3.4]]). The name "least action" is historical: the condition is stationarity. In the quantum theory every configuration contributes with weight $e^{iS}$, and stationarity selects the dominant ones as $\hbar \to 0$ (QFT C11, planned).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Principle "Principle of least action") · PS §2.2, p. 15 · Yu §1.6.2 · the user's pre-course notes, §1.6 (Keypoint "Action principle") · PHY 513 Lecture 3, Part A*

^pr-c1b-2-3

This is Hamilton's principle ([[§B6.2 Hamilton's Principle of Stationary Action#^pr-b6-2-1|CM Principle §B6.2.1]]) with one coordinate per point of space: the fixed end configurations $q(t_1)$, $q(t_2)$ become a field held fixed on the whole boundary of $R$, including its spatial part.

> [!theorem] Theorem §C1b.2.4: Euler–Lagrange Equations for Fields
> Let $\mathcal L$ be $C^2$ and $\phi_a$ be $C^2$. Then $\phi$ satisfies [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^pr-c1b-2-3|Principle §C1b.2.3]] if and only if, for each $a$ and at every point,
>
> $$
> \partial_\mu\Bigl(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\Bigr) - \frac{\partial\mathcal L}{\partial\phi_a} = 0 .
> $$
>
> The functional derivative of the action is the continuous function $\dfrac{\delta S}{\delta\phi_a(x)} = \dfrac{\partial\mathcal L}{\partial\phi_a} - \partial_\mu\dfrac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}$; there is one equation per real component, whatever the components assemble into.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3, eq. (EL) (Derivation "Variational derivation of the Euler–Lagrange equation"; Derivation "The Euler–Lagrange equation for other kinds of field") · PS §2.2, eqs. (2.2)–(2.3) · Yu §1.6.2, eqs. (1.165)–(1.167) · PHY 513 Lecture 3, Part A*

^thm-c1b-2-4

> [!derivation]- Derivation
> **1. The varied action.** For a test function $\eta$ supported in a compact $K$ inside $R$,
>
> $$
> S_R[\phi + \varepsilon\eta] - S_R[\phi] = \int_Rd^4x\,\Bigl[\mathcal L\bigl(\phi + \varepsilon\eta, \partial\phi + \varepsilon\partial\eta\bigr) - \mathcal L(\phi, \partial\phi)\Bigr] .
> $$
>
> **2. Differentiate at ε = 0.** The integrand is $C^1$ in $\varepsilon$ with derivative continuous on the compact closure of $R$, so the derivative passes under the integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]). By [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]],
>
> $$
> \delta S[\phi; \eta] = \int_Rd^4x\,\sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a}\,\eta_a + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\,\partial_\mu\eta_a\Bigr] .
> $$
>
> **3. Product rule.** With $\Pi_a^\mu \equiv \partial\mathcal L/\partial(\partial_\mu\phi_a)$, a $C^1$ function of $x$ because $\mathcal L$ and $\phi$ are $C^2$: $\Pi_a^\mu\,\partial_\mu\eta_a = \partial_\mu(\Pi_a^\mu\eta_a) - (\partial_\mu\Pi_a^\mu)\,\eta_a$. Hence
>
> $$
> \delta S[\phi; \eta] = \int_Rd^4x\,\sum_a\Bigl[\frac{\partial\mathcal L}{\partial\phi_a} - \partial_\mu\Pi_a^\mu\Bigr]\eta_a + \int_Rd^4x\;\partial_\mu\Bigl(\sum_a\Pi_a^\mu\eta_a\Bigr) .
> $$
>
> **4. The boundary term.** The second integral is the integral of a divergence. By the divergence theorem in $\mathbb R^4$ ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]; four-dimensional form of [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]) it equals $\oint_{\partial R}d\sigma_\mu\sum_a\Pi_a^\mu\eta_a$, which is zero because $\eta$ vanishes near $\partial R$. (Equivalently: the vector field $\Pi^\mu\eta$ has compact support inside $R$; integrate the $\partial_\mu$ term first over $x^\mu$ by Fubini, [[§23 Fubini's Theorem#^thm-23-1|452 Thm. §23.1]], and the fundamental theorem of calculus gives the difference of two zeros.) ⚑ By-product: had the variation been allowed at the final time $t_2$ of a slab, the surviving term would be $\int d^3x\,\sum_a\Pi^0_a\,\delta\phi_a\big|_{t_2} = \int d^3x\,\sum_a\pi_a\,\delta\phi_a\big|_{t_2}$: the coefficient of the endpoint variation is the momentum density → [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-4|Remark: π multiplies the endpoint variation]]. No assumption about the fields at infinity was needed, only about the variations → [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-2|Caution: Boundary conditions are a choice]].
>
> **5. Read off the functional derivative.** $\delta S[\phi; \eta] = \int_Rd^4x\sum_aE_a\eta_a$ with $E_a = \partial\mathcal L/\partial\phi_a - \partial_\mu\Pi^\mu_a$ continuous. By [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|Def. §C1b.2.4]], $E_a = \delta S/\delta\phi_a$, and it is unique as a continuous function ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2).
>
> **6. Localize.** If every $E_a = 0$, then $\delta S = 0$ for all $\eta$. Conversely, suppose $\delta S = 0$ for all $\eta$. Take $\eta$ with only the component $a$ nonzero (the components vary independently): $\int_Rd^4x\,E_a\eta_a = 0$ for every test function $\eta_a$ inside $R$. If $E_a(x_0) > 0$ at some interior $x_0$, continuity makes $E_a > 0$ on a ball around $x_0$, and a nonnegative bump $\eta_a$ supported in that ball gives a positive integral, a contradiction; likewise for $E_a(x_0) < 0$. This is the fundamental lemma ([[§B5.1 The Euler–Lagrange Equation#^thm-b5-1-2|CM Lemma §B5.1.2]]) in four variables; in the language of distributions, the regular distribution of $E_a$ vanishes on all test functions, so $E_a = 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2). ⚑ By-product: the field equation holds point by point because variations can be localized anywhere; a nonlocal action would give integro-differential equations ([[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|Principle §C1b.3.4]]).
>
> **7. All regions.** Every point lies inside some bounded $R$, so the equations hold everywhere.
>
> **What the derivation shows**
> - The only surface term is $\oint d\sigma_\mu\,\Pi^\mu_a\delta\phi_a$, killed by the variations, not by the fields; its time component is $\pi\,\delta\phi$.
> - Assumptions actually used: $\mathcal L$, $\phi \in C^2$ (for the product rule), $\eta$ smooth with compact support (test functions), components independent.
> - Each step is covariant: $\Pi^\mu_a$ carries an upper index ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|Theorem §C1a.5.11]]) contracted with $\partial_\mu$, so a scalar $\mathcal L$ gives a scalar equation; errors can only be signs and factors of two.
> - Used next: the scalar fields below, the Hamiltonian form ([[§C1b.4 Hamiltonian Field Theory|§C1b.4]]), and Noether's theorem, where the same computation is run with the equations imposed and the boundary term kept ([[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]).

^der-c1b-2-4

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-4|Def. §C1b.2.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-2|Theorem §C1b.2.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^pr-c1b-2-3|Principle §C1b.2.3]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], [[§23 Fubini's Theorem#^thm-23-1|452 Thm. §23.1]], [[§B5.1 The Euler–Lagrange Equation#^thm-b5-1-2|CM Lemma §B5.1.2]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]]

![[ph-qft-c1-9-1.svg]]
*The setting of the action principle. The action is integrated over a bounded region $R$ of spacetime; a variation $\delta\phi = \varepsilon\eta$ is a test function whose support (shaded) lies inside $R$, so the surface term $\oint_{\partial R}d\sigma_\mu\,\Pi^\mu\delta\phi$ vanishes. On a slab $t_1 \le t \le t_2$ the parts of $\partial R$ at fixed time contribute $\int d^3x\,\pi\,\delta\phi$ when the variation is not zero there.*

> [!caution] Caution: Boundary conditions are a choice
> The derivation fixed the field on the boundary (variations vanish there): the Dirichlet choice, which is what "principle of stationary action" means here. Other problems are legitimate (fixing normal derivatives, asking how a solution depends on its boundary data), and each adjusts the boundary term. For the *field equations* the choice does not matter: they must hold for all allowed variations, and those supported in the interior are always among them. Bulk and boundary separate cleanly: the equation is fixed one region at a time by variations in the middle. That the fields themselves fall off at infinity is a separate assumption, needed later for conserved charges ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-1|Theorem §C1b.6.1]]) and for dropping surface terms in $H$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Caution "Boundary conditions are a choice, and the argument respects it") · PS §2.2, pp. 15–16 · PHY 513 Lecture 3, Part A ("we can impose boundary conditions so δϕ = 0 on the boundary")*

^cau-c1b-2-2

> [!theorem] Theorem §C1b.2.5: A Total Divergence Does Not Change the Field Equations
> Let $K^\mu$ be built locally from the fields, finitely many of their derivatives and $x$, and $C^1$ along every configuration. Then $\mathcal L$ and $\mathcal L' = \mathcal L + \partial_\mu K^\mu$ have the same first variation, $\delta S'[\phi; \eta] = \delta S[\phi; \eta]$ for every test function $\eta$, hence the same stationary configurations. If $K^\mu = K^\mu(\phi, x)$, both densities are of first order and their Euler–Lagrange expressions coincide identically.
>
> *Source: PS §2.2, p. 17 ("we can allow the action to change by a surface term, since the presence of such a term would not affect our derivation of the Euler–Lagrange equations") · PHY 513 Lecture 3, Part C ("L is invariant up to a total derivative") · the particle version: [[§B6.2 Hamilton's Principle of Stationary Action#^thm-b6-2-4|CM Theorem §B6.2.4]]*

^thm-c1b-2-5

> [!derivation]- Derivation
> **1. The difference of the actions.** $S'_R[\phi] - S_R[\phi] = \int_Rd^4x\,\partial_\mu K^\mu = \oint_{\partial R}d\sigma_\mu\,K^\mu$ by the divergence theorem ([[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]]).
>
> **2. Vary.** Replace $\phi$ by $\phi + \varepsilon\eta$. The test function $\eta$ and all its derivatives vanish in a neighbourhood of $\partial R$, so $K^\mu[\phi + \varepsilon\eta] = K^\mu[\phi]$ there ($K^\mu$ is local: its value at a point depends on the fields and derivatives at that point only). Hence $S'_R[\phi + \varepsilon\eta] - S_R[\phi + \varepsilon\eta] = \oint_{\partial R}d\sigma_\mu\,K^\mu[\phi]$, independent of $\varepsilon$.
>
> **3. First variations agree.** Differentiating step 2 at $\varepsilon = 0$: $\delta S'[\phi; \eta] - \delta S[\phi; \eta] = 0$. So [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^pr-c1b-2-3|Principle §C1b.2.3]] selects the same configurations for both.
>
> **4. Directly, for $K^\mu(\phi, x)$.** By the chain rule $\partial_\nu K^\nu = \sum_b\frac{\partial K^\nu}{\partial\phi_b}\partial_\nu\phi_b + \frac{\partial K^\nu}{\partial x^\nu}$, a first-order density. Its two Euler–Lagrange ingredients are
>
> $$
> \frac{\partial(\partial_\nu K^\nu)}{\partial(\partial_\mu\phi_a)} = \frac{\partial K^\mu}{\partial\phi_a}, \qquad \partial_\mu\frac{\partial K^\mu}{\partial\phi_a} = \sum_b\frac{\partial^2K^\mu}{\partial\phi_b\,\partial\phi_a}\partial_\mu\phi_b + \frac{\partial^2K^\mu}{\partial x^\mu\,\partial\phi_a} ,
> $$
>
> $$
> \frac{\partial(\partial_\nu K^\nu)}{\partial\phi_a} = \sum_b\frac{\partial^2K^\nu}{\partial\phi_a\,\partial\phi_b}\partial_\nu\phi_b + \frac{\partial^2K^\nu}{\partial\phi_a\,\partial x^\nu} .
> $$
>
> They are equal term by term (rename $\nu \to \mu$) because mixed partials commute for $C^2$ functions ([[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]): the Euler–Lagrange expression of $\partial_\mu K^\mu$ vanishes for every configuration, solution or not.
>
> **What the derivation shows**
> - "Same equations" holds in two strengths: same stationary configurations (always), and identical Euler–Lagrange expressions (when $\mathcal L'$ is still first order).
> - ⚑ By-product: not every derived quantity is unchanged. For $K^\mu(\phi, x)$ the momentum density shifts, $\pi'_a = \pi_a + \partial K^0/\partial\phi_a$, as the particle momenta do under $L \to L + d\Lambda/dt$ ([[§B6.2 Hamilton's Principle of Stationary Action#^rem-b6-2-5|CM Remark: What the freedom changes]]); the Noether current and the canonical energy–momentum tensor shift likewise ([[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]], [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^def-c1b-7-2|Def. §C1b.7.2]]).
> - Used next: a transformation is a symmetry if it changes $\mathcal L$ by a divergence $\alpha\,\partial_\mu\mathcal J^\mu$ (PS eq. (2.10)), and that $\mathcal J^\mu$ enters the Noether current ([[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-5|Remark: Why a total derivative is allowed]]); dropping $\partial_\mu(\phi\,\partial^\mu\phi)$ in [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|Theorem §C1b.3.6]] uses the general case ($K^\mu$ depends on $\partial\phi$).

^der-c1b-2-5

*Uses:* [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-3|Def. §C1b.2.3]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^pr-c1b-2-3|Principle §C1b.2.3]], [[§6 Equality of Mixed Partials#^thm-6-1|452 Thm. §6.1]]

## The free scalar fields

> [!model] Model §C1b.2.6: The Free Real Scalar Field
> A real field $\phi$ with the Lagrangian density
>
> $$
> \mathcal L = \tfrac12\,\partial_\mu\phi\,\partial^\mu\phi - \tfrac12m^2\phi^2 = \tfrac12\dot\phi^2 - \tfrac12(\nabla\phi)^2 - \tfrac12m^2\phi^2 .
> $$
>
> Its Euler–Lagrange equation is the Klein–Gordon equation $(\partial^2 + m^2)\phi = 0$.
>
> *Assumptions:* classical, real, free (quadratic $\mathcal L$: linear field equation, superposition); $m \ge 0$ a parameter; kinetic term normalized to $\frac12$, which fixes $[\phi] = 1$; flat spacetime.
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Definition "Lagrangian density for a real scalar field", eq. (scalarL)), Ch. 3 §3.3 · PHY 513 Lecture 2, Part B; Lecture 3, Part A · PS §2.2, eqs. (2.6)–(2.7)*

^mod-c1b-2-6

This is Relativity's free scalar field ([[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]]) with $\hbar = c = 1$, and the working model of the whole course; its quantization is [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], and why it is essentially the only choice is [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|Theorem §C1b.3.6]]. The Euler–Lagrange equation is computed exactly as in [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-4|REL Theorem §B4.1.4]]: $\partial\mathcal L/\partial\phi = -m^2\phi$, $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi$, and [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]] gives $\partial_\mu\partial^\mu\phi + m^2\phi = 0$.

> [!remark] Remark: The mass parameter after quantization
> In the classical model $m$ is only a parameter of the field equation, the curvature of the potential at its minimum ([[§C1b.3 Mass Dimension, Locality and Power Counting#^der-c1b-3-6|Derivation §C1b.3.6]], step 9). After quantization it is the mass of the quanta: a one-particle state of momentum $\mathbf p$ has energy $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Definition "Lagrangian density for a real scalar field")*

^rem-c1b-2-4

> [!caution] Caution: Rename the dummy index before differentiating
> In $\partial\mathcal L/\partial(\partial_\mu\phi)$ the index $\mu$ is already taken by the formula, so write the kinetic term with another dummy, $\tfrac12\partial_\nu\phi\,\partial^\nu\phi = \tfrac12g^{\nu\rho}\partial_\nu\phi\,\partial_\rho\phi$, and differentiate with $\partial(\partial_\nu\phi)/\partial(\partial_\mu\phi) = \delta^\mu{}_\nu$:
>
> $$
> \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)} = \tfrac12g^{\nu\rho}\bigl(\delta^\mu{}_\nu\,\partial_\rho\phi + \partial_\nu\phi\,\delta^\mu{}_\rho\bigr) = \tfrac12\bigl(\partial^\mu\phi + \partial^\mu\phi\bigr) = \partial^\mu\phi .
> $$
>
> Both factors respond, and the two halves add: treating $\partial_\mu\phi$ and $\partial^\mu\phi$ as independent loses this factor of two ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|Theorem §C1a.5.11]]). Using $\mu$ three times at once is where stray halves come from. Component check: $\partial(\frac12\dot\phi^2)/\partial\dot\phi = \dot\phi = \partial^0\phi$ and $\partial(-\frac12(\nabla\phi)^2)/\partial(\partial_i\phi) = -\partial_i\phi = \partial^i\phi$; the signs are those of the metric. The same hygiene applies when substituting $\mathcal L$ into $\pi = \partial\mathcal L/\partial\dot\phi$ or a Noether current: reserve the formula's indices, rename every dummy in $\mathcal L$, check the free indices at the end.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 ("Example: the Klein–Gordon equation from its Lagrangian", the "act of hygiene") · PHY 513 Lecture 3, Part A ("sloppy notation: (∂ϕ)² = ∂µϕ ∂^µϕ")*

^cau-c1b-2-3

> [!example] Example §C1b.2.1: A Nonlinear Field Equation: the Dilaton
> The density $\mathcal L = -f^2e^{-2\tau}\,\partial_\mu\tau\,\partial^\mu\tau$ of a dimensionless field $\tau$ (with $[f] = 1$: [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-1|Example §C1b.3.1]]) gives, by [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], the nonlinear equation
>
> $$
> \partial^2\tau = (\partial\tau)^2 .
> $$
>
> *Computation.* With the dummy index renamed ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|Caution: Rename the dummy index]]), $\partial\mathcal L/\partial(\partial_\mu\tau) = -2f^2e^{-2\tau}\partial^\mu\tau$ (both factors of $(\partial\tau)^2$ respond) and $\partial\mathcal L/\partial\tau = -f^2(-2)e^{-2\tau}(\partial\tau)^2 = 2f^2e^{-2\tau}(\partial\tau)^2$. The derivative of the first, by the product rule with $\partial_\mu e^{-2\tau} = -2e^{-2\tau}\partial_\mu\tau$, is $\partial_\mu(-2f^2e^{-2\tau}\partial^\mu\tau) = 4f^2e^{-2\tau}(\partial\tau)^2 - 2f^2e^{-2\tau}\partial^2\tau$. Subtracting $\partial\mathcal L/\partial\tau$:
>
> $$
> 4f^2e^{-2\tau}(\partial\tau)^2 - 2f^2e^{-2\tau}\partial^2\tau - 2f^2e^{-2\tau}(\partial\tau)^2 = -2f^2e^{-2\tau}\bigl[\partial^2\tau - (\partial\tau)^2\bigr] = 0 ,
> $$
>
> and $e^{-2\tau} \neq 0$. Of the two contributions $4f^2e^{-2\tau}(\partial\tau)^2$ (from the exponential) and $2f^2e^{-2\tau}(\partial\tau)^2$ (from $\partial\mathcal L/\partial\tau$) only the difference survives, so a sign error in either changes the answer: the sign discipline the problem set was designed to test. The kinetic term is not canonically normalized, and the equation is nonlinear although no potential is present. (The overall sign of this density, the one standard with a mostly-plus metric, gives $\dot\tau^2$ a negative coefficient for $g = \operatorname{diag}(+,-,-,-)$; it does not affect the field equation: [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-1|Example §C1b.3.1]].)
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Derivation "Dimensions of a field in an exponent: the dilaton (Problem Set 2)": "The equation of motion") · PHY 513 Problem Set 2, Problem 1(b), course solution*

^ex-c1b-2-1

> [!remark] Remark: Kinetic minus potential, read term by term
> - $\frac12\dot\phi^2$ is the kinetic term; it has no mass in front, because each point's "coordinate" $\phi$ has unit inertia.
> - $\frac12m^2\phi^2$ is a potential energy: it costs energy to have field at all (PS: the energy cost "of having the field around at all").
> - $\frac12(\nabla\phi)^2$ is also a potential energy: neighbouring points are coupled like the springs of a lattice, which favour configurations that do not vary across space; it costs energy at one instant, with nothing moving (PS: the cost of "shearing" in space).
> - Which part is kinetic depends on the observer, since observers disagree on the time direction; relativity packages the first two into $\frac12\partial_\mu\phi\,\partial^\mu\phi$ and fixes their relative coefficient. A fluid or an elastic medium has the same structure with unrelated coefficients (often first order in time): action densities work for any field theory, and relativity is what restricts the examples so severely.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (the three terms; Discussion "The Lagrangian of a mechanical wave looks similar; is it relativistic?") · PS §2.2, p. 17 · PHY 513 Lecture 2, Part B*

^rem-c1b-2-5

> [!model] Model §C1b.2.7: The Free Complex Scalar Field
> A complex field $\phi$ with the real Lagrangian density
>
> $$
> \mathcal L = \partial_\mu\phi^*\,\partial^\mu\phi - m^2\phi^*\phi ,
> $$
>
> written without a factor $\frac12$. Its field equations are $(\partial^2 + m^2)\phi = 0$ and the conjugate ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]).
>
> *Assumptions:* those of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]], for two real components of equal mass ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|Theorem §C1b.2.8]]).
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Definition "Lagrangian density for a complex scalar field", eq. (complexL)), Ch. 3 §3.3 · PS §2.2, eq. (2.14) · PHY 513 Lecture 3, Part C (Example 2) · PHY 513 Problem Set 2, Problem 3 (with $V = 0$)*

^mod-c1b-2-7

> [!theorem] Theorem §C1b.2.8: The Complex Field Is Two Real Fields of Equal Mass
> Write $\phi = (\phi_1 + i\phi_2)/\sqrt2$ with $\phi_1$, $\phi_2$ real. Then
>
> $$
> \partial_\mu\phi^*\,\partial^\mu\phi - m^2\phi^*\phi = \sum_{j = 1}^2\Bigl[\tfrac12\,\partial_\mu\phi_j\,\partial^\mu\phi_j - \tfrac12m^2\phi_j^2\Bigr] ,
> $$
>
> two copies of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]] with the same mass. The phase rotation $\phi \to e^{i\alpha}\phi$ is the rotation of $(\phi_1, \phi_2)$ by the angle $\alpha$, and leaves $\mathcal L$ unchanged.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Definition "Lagrangian density for a complex scalar field": "It is exactly two real fields, which explains the missing ½"; "It has a symmetry the real field lacks") · PHY 513 Problem Set 2, Problem 3(c), course solution · PS §2.2, p. 18*

^thm-c1b-2-8

> [!derivation]- Derivation
> **1. The mass term.** $\phi^{\ast}\phi = \tfrac12(\phi_1 - i\phi_2)(\phi_1 + i\phi_2) = \tfrac12\bigl(\phi_1^2 + i\phi_1\phi_2 - i\phi_2\phi_1 + \phi_2^2\bigr) = \tfrac12(\phi_1^2 + \phi_2^2)$: the two cross terms cancel because real numbers commute.
>
> **2. The kinetic term.** $\partial_\mu\phi^{\ast}\,\partial^\mu\phi = \tfrac12\bigl(\partial_\mu\phi_1 - i\partial_\mu\phi_2\bigr)\bigl(\partial^\mu\phi_1 + i\partial^\mu\phi_2\bigr) = \tfrac12\bigl(\partial_\mu\phi_1\partial^\mu\phi_1 + i\,\partial_\mu\phi_1\partial^\mu\phi_2 - i\,\partial_\mu\phi_2\partial^\mu\phi_1 + \partial_\mu\phi_2\partial^\mu\phi_2\bigr)$. The cross terms cancel because the contraction is symmetric, $\partial_\mu\phi_1\,\partial^\mu\phi_2 = g^{\mu\nu}\partial_\mu\phi_1\partial_\nu\phi_2 = \partial_\mu\phi_2\,\partial^\mu\phi_1$ ($g$ symmetric).
>
> **3. Add.** $\mathcal L = \tfrac12\sum_j\partial_\mu\phi_j\partial^\mu\phi_j - \tfrac12m^2\sum_j\phi_j^2$. ⚑ By-product: the $\frac12$ of the real field is hidden in the $1/\sqrt2$ of $\phi$; with this normalization each real component is canonically normalized, and the quantized complex field has twice the zero-point energy of the real one ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]]).
>
> **4. The phase.** $e^{i\alpha}\phi = \tfrac1{\sqrt2}(\cos\alpha + i\sin\alpha)(\phi_1 + i\phi_2) = \tfrac1{\sqrt2}\bigl[(\phi_1\cos\alpha - \phi_2\sin\alpha) + i(\phi_1\sin\alpha + \phi_2\cos\alpha)\bigr]$, so $(\phi_1, \phi_2) \to (\phi_1\cos\alpha - \phi_2\sin\alpha,\ \phi_1\sin\alpha + \phi_2\cos\alpha)$, a rotation. For constant $\alpha$ the derivatives rotate the same way, and $\mathcal L$ depends only on the rotation invariants $\phi_1^2 + \phi_2^2$ and $\partial\phi_1\cdot\partial\phi_1 + \partial\phi_2\cdot\partial\phi_2$ (directly: $\phi^{\ast}\phi$ and $\partial\phi^{\ast}\cdot\partial\phi$ pick up $e^{-i\alpha}e^{i\alpha} = 1$). ⚑ By-product: $\mathrm U(1) = \mathrm{SO}(2)$; only a constant $\alpha$ works, since for $\alpha(x)$ the derivative also hits $e^{i\alpha(x)}$ (that is gauge invariance, QFT C8, planned); the conserved current is [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]].
>
> **What the derivation shows**
> - Nothing new is in the complex field except bookkeeping: two real fields of equal mass, combined so that a symmetry is manifest.
> - Used next: the field equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]]), the Hamiltonian ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]), the quantization with a particle and a distinct antiparticle ([[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]).

^der-c1b-2-8

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]]

> [!theorem] Theorem §C1b.2.9: Field and Conjugate as Independent Variables
> Let $\mathcal L$ be a real density of a complex field, written as a function of $\phi$, $\phi^*$ and their derivatives, and define $\dfrac{\partial}{\partial\phi} = \dfrac{1}{\sqrt2}\Bigl(\dfrac{\partial}{\partial\phi_1} - i\dfrac{\partial}{\partial\phi_2}\Bigr)$, $\dfrac{\partial}{\partial\phi^*} = \dfrac{1}{\sqrt2}\Bigl(\dfrac{\partial}{\partial\phi_1} + i\dfrac{\partial}{\partial\phi_2}\Bigr)$ (likewise for $\partial_\mu\phi$, $\partial_\mu\phi^*$). The two real Euler–Lagrange equations of $\phi_1$, $\phi_2$ hold if and only if
>
> $$
> \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^*)} - \frac{\partial\mathcal L}{\partial\phi^*} = 0 ,
> $$
>
> whose complex conjugate is the same equation with $\phi \leftrightarrow \phi^*$. For [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]] it reads $(\partial^2 + m^2)\phi = 0$, and the conjugate $(\partial^2 + m^2)\phi^* = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 ("φ and φ* are treated as independent variables"), Ch. 3 §3.3 (Derivation "The Euler–Lagrange equation for other kinds of field": "an invertible linear change of variables") · PHY 513 Problem Set 2, Problem 3(a), course solution · PS §2.2, p. 18 ("We treat φ and φ* as independent fields")*

^thm-c1b-2-9

> [!derivation]- Derivation
> **1. The real equations.** $\phi_1$, $\phi_2$ are two real components, so [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]] gives $E_j \equiv \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_j)} - \frac{\partial\mathcal L}{\partial\phi_j} = 0$, $j = 1, 2$; each $E_j$ is real because $\mathcal L$ is real.
>
> **2. The derivative operators are consistent.** From $\phi = (\phi_1 + i\phi_2)/\sqrt2$, $\phi^{\ast} = (\phi_1 - i\phi_2)/\sqrt2$: $\frac{\partial\phi}{\partial\phi} = \frac1{\sqrt2}\bigl(\frac1{\sqrt2} - i\cdot\frac{i}{\sqrt2}\bigr) = \frac12(1 + 1) = 1$ and $\frac{\partial\phi^{\ast}}{\partial\phi} = \frac1{\sqrt2}\bigl(\frac1{\sqrt2} - i\cdot\frac{-i}{\sqrt2}\bigr) = \frac12(1 - 1) = 0$; likewise $\partial\phi^{\ast}/\partial\phi^{\ast} = 1$, $\partial\phi/\partial\phi^{\ast} = 0$. So a polynomial in $\phi$, $\phi^{\ast}$ is differentiated by these operators as if $\phi$ and $\phi^{\ast}$ were independent variables.
>
> **3. Recombine.** The map $(E_1, E_2) \mapsto \bigl((E_1 + iE_2)/\sqrt2,\ (E_1 - iE_2)/\sqrt2\bigr)$ is linear, and by step 2's definitions (applied to $\partial\mathcal L/\partial\phi_j$ and to $\partial\mathcal L/\partial(\partial_\mu\phi_j)$, with $\partial_\mu$ commuting with constant coefficients)
>
> $$
> \frac{E_1 + iE_2}{\sqrt2} = \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^*)} - \frac{\partial\mathcal L}{\partial\phi^*}, \qquad \frac{E_1 - iE_2}{\sqrt2} = \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)} - \frac{\partial\mathcal L}{\partial\phi} .
> $$
>
> **4. Invertibility.** The matrix $\frac1{\sqrt2}\begin{pmatrix}1 & i\\ 1 & -i\end{pmatrix}$ has determinant $\frac12(-i - i) = -i \ne 0$, so $E_1 = E_2 = 0$ exactly when both right-hand sides vanish. Since $E_1$, $E_2$ are real, the second right-hand side is the complex conjugate of the first: one complex equation carries both real ones.
>
> **5. The free complex field.** Write $\mathcal L = g^{\nu\rho}\partial_\nu\phi^{\ast}\,\partial_\rho\phi - m^2\phi^{\ast}\phi$. Then $\partial\mathcal L/\partial\phi^{\ast} = -m^2\phi$ and $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = g^{\nu\rho}\delta^\mu{}_\nu\,\partial_\rho\phi = \partial^\mu\phi$: only one factor responds, so no factor $2$ arises. The equation of step 3 is $\partial_\mu\partial^\mu\phi + m^2\phi = 0$. ⚑ By-product: with $\phi$ and $\phi^{\ast}$ independent each appears once in the kinetic term, which is why the complex density needs no $\frac12$ to give the canonically normalized equation; the same factor-of-two point as in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|Caution: Rename the dummy index]].
>
> **What the derivation shows**
> - "Treat $\phi$ and $\phi^*$ as independent" is an invertible linear change of variables, legitimate for any real $\mathcal L$; varying $\phi^*$ gives the equation for $\phi$.
> - Assumption: $\mathcal L$ real (otherwise the two equations are not conjugate and the system is overdetermined).
> - Used next: the conjugate momenta cross over, $\pi = \dot\phi^*$ ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]]).

^der-c1b-2-9

*Uses:* [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-7|Model §C1b.2.7]]

> [!remark] Remark: The symmetry the real field lacks, and a potential
> The phase rotation of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|Theorem §C1b.2.8]] gives a conserved current, the number current (essentially the electric current once the field is coupled to light; [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]]). After quantization the two real degrees of freedom become a particle and a distinct antiparticle of opposite charge, whereas a real field describes a neutral particle that is its own antiparticle ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]). A potential depending only on the invariant, $V(\phi^*\phi)$, keeps the symmetry and enters the $\phi^*$ equation through the chain rule, $(\partial^2 + m^2)\phi = -V'(\phi^*\phi)\,\phi$, and the $\phi$ equation as its conjugate.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Definition "Lagrangian density for a complex scalar field": "Where this is used"), Ch. 3 §3.4 ("A potential depending only on the invariant combination") · PHY 513 Problem Set 2, Problem 3(a), course solution*

^rem-c1b-2-6

> [!remark] Remark: One equation for every kind of field
> Nothing in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]] used what the components assemble into. For a **vector field** $A_\nu$ there are four equations, and the field index becomes a free index, so the equations form a tensor equation: from $\mathcal L = -\frac14F_{\alpha\beta}F^{\alpha\beta} - J^\alpha A_\alpha$, $\partial\mathcal L/\partial(\partial_\mu A_\nu) = -F^{\mu\nu}$ and $\partial\mathcal L/\partial A_\nu = -J^\nu$ give Maxwell's equations $\partial_\mu F^{\mu\nu} = J^\nu$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]]; the derivative with respect to $\partial_\mu A_\nu$ is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-12|Theorem §C1a.5.12]]; [[§B4.2 The Electromagnetic Field Tensor|REL §B4.2]]). Since $F_{00} = 0$, $A_0$ has no time derivative in $\mathcal L$: its equation (Gauss's law) is a constraint, not an evolution equation, and $A_0$ has no conjugate momentum ([[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-3|Remark: Constraints and first-order Lagrangians]]). A mass term $\frac12m^2A_\mu A^\mu$ would be the only undifferentiated $A$ besides the coupling, and gauge invariance forbids it; the coupling survives because $J^\mu\partial_\mu\lambda$ is a divergence when $\partial_\mu J^\mu = 0$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]). For a **Dirac field** the density $\bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ is first order, and varying $\bar\psi$ gives the Dirac equation directly ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-6|Theorem §C5a.7.6]]). In all cases $\mathcal L$ must be real.
>
> *Source: the user's PHY 513 notes, Ch. 3 §3.3 (Derivation "The Euler–Lagrange equation for other kinds of field") · PS §2.2, p. 16 ("If the Lagrangian contains more than one field, there is one such equation for each")*

^rem-c1b-2-7

> [!remark] Remark: The second variation is the operator whose inverse is the propagator
> Vary the free real action twice, in two directions $\eta_1$, $\eta_2$. Since $S$ is quadratic, $\frac{\partial^2}{\partial\varepsilon_1\partial\varepsilon_2}S[\phi + \varepsilon_1\eta_1 + \varepsilon_2\eta_2] = \int d^4x\,\bigl(\partial_\mu\eta_1\,\partial^\mu\eta_2 - m^2\eta_1\eta_2\bigr) = -\int d^4x\,\eta_1(\partial^2 + m^2)\eta_2$, after one integration by parts with no surface term (test functions). As a bilinear map on test functions it has the kernel
>
> $$
> \frac{\delta^2S}{\delta\phi(x)\,\delta\phi(y)} = -(\partial_x^2 + m^2)\,\delta^4(x - y) ,
> $$
>
> a distribution on $\mathbb R^8$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]). Its first variation set to zero is the field equation; its inverses are the Green's functions $G$ with $(\partial^2 + m^2)G = -\delta^4$, i.e. $D_C = iG$ in the normalization of [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]]. The inverse is not unique; a boundary condition, equivalently a contour, picks one ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]]), and the vacuum boundary condition of the path integral picks $D_F$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|Remark: Preview: the propagator as a Gaussian covariance]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.3 (Derivation "Taylor expansion in index notation", "Three expansions, not one": "the second variation, (□ + m²)δ⁴(x − y) for the free field, is the operator whose inverse will be the propagator") · the sign and the integration by parts written out here*

^rem-c1b-2-8

> [!remark]- Connections
> - The field action principle is Hamilton's principle with the index $i$ of $q_i$ made continuous; the fundamental lemma used to localize is the particle one in four variables — [[§B6.2 Hamilton's Principle of Stationary Action#^pr-b6-2-1|CM Principle §B6.2.1]], [[§B5.1 The Euler–Lagrange Equation#^thm-b5-1-2|CM Lemma §B5.1.2]], [[§B5.1 The Euler–Lagrange Equation#^thm-b5-1-4|CM Theorem §B5.1.4]].
> - Relativity derived the same equation for one real field with $c$ explicit; here it holds for any number of components, in natural units, with the functional derivative identified — [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-2|REL Theorem §B4.1.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]].
> - The derivative of a field value with respect to the field is a delta function: the same object becomes the field Poisson bracket and then the canonical commutator, which is why fields are operator-valued distributions — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-2|Remark: The functional derivative is a distribution]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-5|Theorem §C1b.4.5]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]].
> - Variations are test functions, and the fundamental lemma is the injectivity of $\psi \mapsto T_\psi$: the calculus of variations is already distribution theory — [[§CA.2 Generalized Functions#^def-ca-2-1|Def. §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]].
> - The surface term $\oint d\sigma_\mu\,\Pi^\mu\delta\phi$ discarded here is the term Noether's theorem keeps: with the field equations imposed and $\delta\phi$ a symmetry, it becomes the divergence of the conserved current — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^der-c1b-2-4|Derivation §C1b.2.4]], step 4; [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]], [[§C1b.5 Noether's Theorem#^rem-c1b-5-6|Remark: The action principle's computation, run backwards]].
> - The time component of that surface term is $\int d^3x\,\pi\,\delta\phi$, the field version of $p\,\delta q$ at the endpoint, whose dependence on the final configuration makes the on-shell action Hamilton's principal function — [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-4|Remark: π multiplies the endpoint variation]], [[§B8.3 The Hamilton–Jacobi Equation|CM §B8.3]].
> - Adding a divergence to the density is the field form of adding $d\Lambda/dt$ to a Lagrangian; it is also the freedom that lets Noether symmetries change $\mathcal L$ "up to a total derivative" — [[§B6.2 Hamilton's Principle of Stationary Action#^thm-b6-2-4|CM Theorem §B6.2.4]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]], [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]].
> - The quadratic action's kernel $-(\partial^2 + m^2)\delta^4$ and the Green's functions of [[§C2b.5 Green's Functions and Contours|§C2b.5]] are inverse to each other up to boundary conditions; the path integral turns this into "the propagator is $i$ times the inverse of the quadratic form" — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-8|Remark: The second variation]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|Remark: Preview: the propagator as a Gaussian covariance]], QFT C11 (planned).
> - The complex field's two real components with one mass are the classical root of particle and antiparticle; the phase rotation is a rotation in field space, whose Noether charge is the field-space analogue of angular momentum $xp_y - yp_x$ — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-8|Theorem §C1b.2.8]], [[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]], [[§B8.1 Poisson Brackets#^thm-b8-1-6|CM Theorem §B8.1.6]].
> - Quantum mechanics quantized the same two real fields in a box and combined them into a charged field; the Lagrangian origin of that construction is here — [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-7|QM Theorem §C13.1.7]].
> - The four-dimensional integration by parts that kills the surface term is the three-dimensional rule of the methods chapter, one dimension up — [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-1|452 Thm. §28.1]].
> - Electromagnetism level C: the action principle for the Maxwell field in SI units, with the field equations in weak (distributional) form as the direct output of $\delta S = 0$; its static reduction, Poisson's equation as the Euler–Lagrange equation of an action whose minimum is $-U_E$; and how a quadratic Lagrangian is read — [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-2|EM Theorem §C1.2.2]], [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-2|EM Theorem §C2.1.2]], [[§C1.1 Building the Maxwell Action#^rem-c1-1-4|EM Remark: How a quadratic Lagrangian is read]].
> - With $N$ fields and a mass matrix, the Euler–Lagrange equations of the quadratic Lagrangian decouple, after an orthogonal rotation to the mass basis, into $N$ copies of Model §C1b.2.6 ([[§R1.3 Diagonalization into N Free Klein–Gordon Fields#^thm-r1-3-2|Thesis Thm. §R1.3.2]]); Theorem §C1b.2.8 is the case $N = 2$ of an $O(N)$-symmetric potential, whose mass matrix is a multiple of the identity ([[§R1.4 Examples꞉ Structured Mass Matrices#^ex-r1-4-1|Thesis Ex. §R1.4.1]]).
