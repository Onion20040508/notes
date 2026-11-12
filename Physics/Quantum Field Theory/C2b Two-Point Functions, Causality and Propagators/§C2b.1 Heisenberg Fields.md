---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.1
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2a.6 Coherent States and the Classical Field]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.2 The Wightman Function]] →

*Sources: the user's PHY 513 notes, Ch. 5 §§5.1–5.3, 5.7 and Ch. 6 §§6.3–6.4 (free fields on the mass shell), §6.7 (the frequency split) · PHY 513 Lecture 5 (Larsen, 16 Sep 2026; no slides, reconstructed in the user's notes) · Peskin & Schroeder §2.4, pp. 25–26 · Yu §6.3.*

The free field of [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] lives at one instant: a mode expansion, a commutator and a spectrum, with no time in them. This section restores time in the Heisenberg picture ([[§C3.3 The Schrödinger and Heisenberg Pictures#^def-c3-3-1|QM Def. §C3.3.1]]) and asks how the field operator depends on time: first in field form, as an operator equation (the canonical relations hold at every time, and the Heisenberg equations are the Klein–Gordon equation), then through the solutions of that equation, which live on the mass shell and give the covariant mode expansion, and finally what the negative-frequency half of it means. The two-point functions of [[§C2b.2 The Wightman Function|§C2b.2]]–[[§C2b.5 Microcausality and the Commutator Function|§C2b.5]] are built from the Heisenberg field.

**Setup.** The system is [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]: quantum, free, $m > 0$, Heisenberg picture with the free $\hat H$. The states are the Fock space over the free vacuum $|0\rangle$, relativistically normalized, $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$. The definition of the Heisenberg field and the canonical relations at every time hold for any time-independent $\hat H$; everything from the field equation on is exact for the free field only. With interactions the same mode expansion is the interaction-picture field, not the Heisenberg field ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-2|Caution: With interactions, the Heisenberg field is not the free mode expansion]]), and the one-particle matrix element carries $\sqrt Z$ ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|Caution: With interactions, the one-particle matrix element carries √Z]]).

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ whenever $p$ is on shell, $[\hat a_{\mathbf p}, \hat a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a_{\mathbf p}^\dagger|0\rangle$. Lecture 5 writes $\omega_{\mathbf p}$ for $E_{\mathbf p}$ ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution: Eₚ, not ωₚ; π, not Π]]). Unless stated otherwise $m > 0$; the massless case is stated separately where it differs.

## The Heisenberg field

> [!definition] Definition §C2b.1.1: Heisenberg Field
> Let $\hat\phi_S(\mathbf x)$, $\hat\pi_S(\mathbf x)$ be the Schrödinger-picture field operators and $\hat H$ the Hamiltonian. The **Heisenberg fields** are
>
> $$
> \hat\phi(x) = \hat\phi(t, \mathbf x) \equiv e^{i\hat Ht}\,\hat\phi_S(\mathbf x)\,e^{-i\hat Ht}, \qquad \hat\pi(x) \equiv e^{i\hat Ht}\,\hat\pi_S(\mathbf x)\,e^{-i\hat Ht},
> $$
>
> so that $\hat\phi(0, \mathbf x) = \hat\phi_S(\mathbf x)$. From here on a field with a spacetime argument is a Heisenberg operator, and states are frozen at $t = 0$.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* the definition holds for any time-independent $\hat H$; here $\hat H$ is the free one; with the full $\hat H$ of [[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]] it defines $\hat\phi_H$, which is not the free field ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-2|Caution: With interactions, the Heisenberg field is not the free mode expansion]]).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1 · PS §2.4, eq. (2.43)*

^def-c2b-1-1

> [!remark] Remark: Why field theory works in the Heisenberg picture
> The definition is QM's Heisenberg picture ([[§C3.3 The Schrödinger and Heisenberg Pictures#^def-c3-3-1|QM Def. §C3.3.1]]) applied to an operator labelled by $\mathbf x$, and the two pictures give the same matrix elements ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-3|QM Theorem §C3.3.3]]). What is new is the reason for preferring it: a time-dependent *state* obeying a Schrödinger equation singles out time, while a time-dependent *operator* $\hat\phi(t, \mathbf x)$ is a function on spacetime that can transform covariantly ([[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-5|Theorem §C3.5.5]]). Canonical quantization starts in the Schrödinger picture because diagonalizing $\hat H$ at one instant is the continuation of ordinary quantum mechanics ([[P1 Canonical Quantization|P1]]); it then switches.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1*

^rem-c2b-1-1

## The Heisenberg equations

> [!theorem] Theorem §C2b.1.1: The Equal-Time Relations Hold at Every Time
> For every real $t$, the Heisenberg fields of [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]] obey the canonical relations of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] at the common time $t$:
>
> $$
> [\hat\phi(t, \mathbf x), \hat\pi(t, \mathbf y)] = i\delta^3(\mathbf x - \mathbf y), \qquad [\hat\phi(t, \mathbf x), \hat\phi(t, \mathbf y)] = [\hat\pi(t, \mathbf x), \hat\pi(t, \mathbf y)] = 0 .
> $$
>
> Nothing is asserted for two different times.
>
> *Model:* any; *applies:* any time-independent $\hat H$, interacting ones included (conjugation by $e^{i\hat Ht}$ preserves commutators); exact.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 · PS §2.4, eqs. (2.44)–(2.45)*

^thm-c2b-1-1

> [!derivation]- Derivation
> **Step 1** (sandwich the commutator). Insert $\mathbf 1 = e^{-i\hat Ht}e^{i\hat Ht}$ between the two factors of each product:
>
> $$
> e^{i\hat Ht}[\hat\phi_S(\mathbf x), \hat\pi_S(\mathbf y)]e^{-i\hat Ht} = e^{i\hat Ht}\hat\phi_Se^{-i\hat Ht}\,e^{i\hat Ht}\hat\pi_Se^{-i\hat Ht} - e^{i\hat Ht}\hat\pi_Se^{-i\hat Ht}\,e^{i\hat Ht}\hat\phi_Se^{-i\hat Ht} = [\hat\phi(t, \mathbf x), \hat\pi(t, \mathbf y)] .
> $$
>
> One unitary sandwiches the whole product, so the *same* $t$ enters both fields.
>
> **Step 2** (the right side). The right side of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], $i\delta^3(\mathbf x - \mathbf y)$, is a number, so $e^{i\hat Ht}(i\delta^3)e^{-i\hat Ht} = i\delta^3$ is unchanged. (Sense: both sides are operator-valued distributions in $(\mathbf x, \mathbf y)$; smeared with test functions $f(\mathbf x)g(\mathbf y)$ the statement is $[\hat\phi(t, f), \hat\pi(t, g)] = i\int d^3x\,f g$, the smeared relation of [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]] conjugated by the unitary $e^{i\hat Ht}$.)
>
> **Step 3** (the other two relations). The same insertion in $[\hat\phi_S(\mathbf x), \hat\phi_S(\mathbf y)]$ and $[\hat\pi_S(\mathbf x), \hat\pi_S(\mathbf y)]$ gives $[\hat\phi(t, \mathbf x), \hat\phi(t, \mathbf y)]$ and $[\hat\pi(t, \mathbf x), \hat\pi(t, \mathbf y)]$, and their right sides, $0$, are unchanged.
>
> ⚑ By-product: nothing is said about *different* times → [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|Caution: Equal times only]]; the answer is Theorem §C2b.5.11.
>
> **What the derivation shows.**
> - Only the unitarity of $e^{i\hat Ht}$ was used, not the form of $\hat H$: the statement holds for any Hamiltonian, free or interacting.
> - Used next: the Heisenberg equations ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]), which commute fields at one common time.

^der-c2b-1-1

*Uses:* [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]

> [!theorem] Theorem §C2b.1.2: The Heisenberg Equations Are the Klein–Gordon Equation
> With the relations at a common time ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]) and $\hat H = \int d^3x\,\bigl[\tfrac12\hat\pi^2 + \tfrac12(\nabla\hat\phi)^2 + \tfrac12m^2\hat\phi^2\bigr]$ ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]), the Heisenberg equation $i\partial_t\hat{\mathcal O} = [\hat{\mathcal O}, \hat H]$ gives $\partial_t\hat\phi = \hat\pi$ and $\partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi$, hence the operator equation
>
> $$
> (\partial_\mu\partial^\mu + m^2)\,\hat\phi(x) = 0 .
> $$
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free $\hat H$, exact, an operator equation; with an interaction the Heisenberg equations give the interacting field equation instead ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-3|Theorem §C6a.1.3]]; [[§C2b.1 Heisenberg Fields#^cau-c2b-1-2|Caution: With interactions, the Heisenberg field is not the free mode expansion]]).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 · PS §2.4, eqs. (2.44)–(2.45)*

^thm-c2b-1-2

> [!derivation]- Derivation
> **Step 1** (equal-time relations at time $t$). By [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], $[\hat\phi(t, \mathbf x), \hat\pi(t, \mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$ and $[\hat\phi(t, \mathbf x), \hat\phi(t, \mathbf y)] = [\hat\pi(t, \mathbf x), \hat\pi(t, \mathbf y)] = 0$ at every common time $t$; only these are used below.
>
> **Step 2** (the Hamiltonian at time $t$). $\hat H$ commutes with $e^{i\hat Ht}$, so $\hat H = e^{i\hat Ht}\hat He^{-i\hat Ht}$ is the Hamiltonian of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] with every field replaced by its Heisenberg version at any common time; choose the time $t$ of the operator it will be commuted with (the squares of fields at one point are understood normal-ordered, [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]; the subtracted constant $E_0$ is a number and drops out of every commutator, Step 1 of Derivation §C2b.1.4):
>
> $$
> \hat H = \int d^3x'\,\Bigl[\tfrac12\hat\pi(t, \mathbf x')^2 + \tfrac12\bigl(\nabla'\hat\phi(t, \mathbf x')\bigr)^2 + \tfrac12m^2\hat\phi(t, \mathbf x')^2\Bigr].
> $$
>
> **Step 3** ($\hat\phi$ against the three terms). Write $\hat\phi = \hat\phi(t, \mathbf x)$, $\hat\phi' = \hat\phi(t, \mathbf x')$, $\hat\pi' = \hat\pi(t, \mathbf x')$.
> - $[\hat\phi, \hat\pi'^2] = \hat\pi'[\hat\phi, \hat\pi'] + [\hat\phi, \hat\pi']\hat\pi' = 2i\delta^3(\mathbf x - \mathbf x')\,\hat\pi'$: the commutator is a number, so the two terms are equal. (Sense: $\delta^3(\mathbf x - \mathbf x')\,\hat\pi'$ is a $c$-number distribution times an operator-valued distribution in the same variable; smeared with $g(\mathbf x)$ it becomes $g(\mathbf x')\hat\pi(t, \mathbf x')$, a test function times $\hat\pi$, which is defined: [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]].)
> - $[\hat\phi, (\nabla'\hat\phi')^2] = 0$: $[\hat\phi, \partial'_i\hat\phi'] = \partial'_i[\hat\phi, \hat\phi'] = 0$, because $[\hat\phi, \hat\phi']$ vanishes for *all* $\mathbf x'$ and the difference quotient of an identically zero function is zero.
> - $[\hat\phi, \hat\phi'^2] = 0$.
>
> **Step 4** (the equation for $\hat\phi$). By the Heisenberg equation ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]]),
>
> $$
> i\partial_t\hat\phi(t, \mathbf x) = [\hat\phi, \hat H] = \int d^3x'\,\tfrac12\cdot2i\delta^3(\mathbf x - \mathbf x')\,\hat\pi(t, \mathbf x') = i\hat\pi(t, \mathbf x), \qquad\text{so}\qquad \partial_t\hat\phi = \hat\pi .
> $$
>
> (The $\mathbf x'$-integral against $\delta^3(\mathbf x - \mathbf x')$ is the action of δ; after smearing in $\mathbf x$ with $g$ it reads $\int d^3x'\,g(\mathbf x')\hat\pi(t, \mathbf x') = \hat\pi(t, g)$, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]].)
>
> ⚑ By-product: $\hat\pi = \partial_t\hat\phi$ follows from the commutators alone, without the mode expansion; it agrees with [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], 3 → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|Remark: Two routes that meet]].
>
> **Step 5** (rewrite the gradient term). By [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]],
>
> $$
> \int d^3x'\,(\nabla'\hat\phi')^2 = \oint_{|\mathbf x'| = L}d\mathbf S\cdot\hat\phi'\,\nabla'\hat\phi' - \int d^3x'\,\hat\phi'\,\nabla'^2\hat\phi' \;\longrightarrow\; -\int d^3x'\,\hat\phi'\,\nabla'^2\hat\phi' \qquad (L \to \infty).
> $$
>
> ⚑ By-product: the surface term is dropped on the assumption that the field falls off at spatial infinity, i.e. for matrix elements between normalizable states (wave packets, [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]). So $\hat H = \int d^3x'\,[\tfrac12\hat\pi'^2 + \tfrac12\hat\phi'(-\nabla'^2 + m^2)\hat\phi']$.
>
> **Step 6** ($\hat\pi$ against the two terms). $[\hat\pi, \hat\pi'^2] = 0$. For the second, with $[\hat\pi, \hat\phi'] = -i\delta^3(\mathbf x - \mathbf x')$,
>
> $$
> [\hat\pi, \hat\phi'(-\nabla'^2 + m^2)\hat\phi'] = [\hat\pi, \hat\phi'](-\nabla'^2 + m^2)\hat\phi' + \hat\phi'(-\nabla'^2 + m^2)[\hat\pi, \hat\phi'] = -i\delta^3(\mathbf x - \mathbf x')(-\nabla'^2 + m^2)\hat\phi' - i\,\hat\phi'(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x').
> $$
>
> In the second term the operator acts on the $c$-number commutator: $(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x')$ is the distributional derivative of δ ([[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]).
>
> **Step 7** (integrate over $\mathbf x'$). The first term gives $-i(-\nabla^2 + m^2)\hat\phi(t, \mathbf x)$. In the second, move $-\nabla'^2$ onto $\hat\phi'$ by two integrations by parts; the surface terms vanish because the delta function is zero on any large sphere ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]); this is exactly the definition of the derivative of δ, moved onto the factor it multiplies ([[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]):
>
> $$
> -i\int d^3x'\,\hat\phi'(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x') = -i\int d^3x'\,\bigl[(-\nabla'^2 + m^2)\hat\phi'\bigr]\delta^3(\mathbf x - \mathbf x') = -i(-\nabla^2 + m^2)\hat\phi(t, \mathbf x) .
> $$
>
> The two terms are equal and cancel the $\frac12$: $i\partial_t\hat\pi = [\hat\pi, \hat H] = -i(-\nabla^2 + m^2)\hat\phi$, i.e. $\partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi$.
>
> **Step 8** (combine). Differentiate Step 4 in $t$: $\partial_t^2\hat\phi = \partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi$, i.e. $(\partial_t^2 - \nabla^2 + m^2)\hat\phi = (\partial_\mu\partial^\mu + m^2)\hat\phi = 0$.
>
> **What the derivation shows.**
> - Only the equal-time relations and the form of $\hat H$ were used, never the mode expansion; the mode expansion is recovered by solving the operator equation ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]).
> - Assumption used: fall-off of the field at spatial infinity (Step 5).
> - Every manipulation with $\delta^3$ is an identity of distributions, valid after smearing in $\mathbf x$; the resulting operator equation means $\hat\phi\bigl((\partial^2 + m^2)f\bigr) = 0$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], 3).
> - The two first-order equations are Hamilton's equations of the classical field ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]]; this field: [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|Example §C1b.4.1]]) with operators in place of functions.
> - Used next: every two-point function solves the homogeneous equation (Theorem §C2b.2.4), and the free Schwinger–Dyson equation ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-5|Theorem §C2b.7.5]]).

^der-c2b-1-2

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]

> [!caution] Caution: Equal times only
> - The canonical relations were postulated at one instant. [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]] extends them to every *common* time; at different times nothing has been assumed, and the answer is a theorem ([[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-11|Theorem §C2b.5.11]]).
> - $\hat\phi(\mathbf x)$ commutes with $\nabla\hat\phi(\mathbf y)$ because $[\hat\phi(\mathbf x), \hat\phi(\mathbf y)]$ vanishes for *all* $\mathbf x, \mathbf y$. The same move on $[\hat\phi, \hat\pi]$ gives $\nabla\delta^3 \neq 0$.
> - Inside the commutator with $\hat H$, $(-\nabla^2 + m^2)\hat\phi$ may not be replaced by $-\partial_t^2\hat\phi$: the equality is true, but a time derivative involves nearby *different* times, about which the postulates say nothing. Compute at equal times, then read off the time dependence.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 (Cautions "Equal times", "Two questions from the lecture")*

^cau-c2b-1-1

## Solving the field equation: modes and frequencies

> [!theorem] Theorem §C2b.1.3: Free Fields Live on the Mass Shell
> If $(\partial^2 + m^2)f = 0$, the transform of $f$ is supported on $p^2 = m^2$, $\tilde f(p) = 2\pi\,\delta(p^2 - m^2)\,g(p)$, and
>
> $$
> f(x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl[g(p)\,e^{-ip\cdot x} + g(-p)\,e^{ip\cdot x}\Bigr]_{p^0 = E_{\mathbf p}} ,
> $$
>
> the mode expansion.
>
> *Model:* any solution of the free Klein–Gordon equation, c-number or operator-valued; here [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* exact, for tempered solutions, $m > 0$; the operator reading holds for the free Heisenberg field only.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Principle "Free fields live on the mass shell"), §6.4 · PS §2.4, eq. (2.47) (the on-shell mode expansion); the rule $\partial^2 + m^2 \leftrightarrow m^2 - p^2$ as in the step before eq. (2.58)*

^thm-c2b-1-3

> [!derivation]- Derivation
> **Step 1** (transform). With $f(x) = \int\frac{d^4p}{(2\pi)^4}\tilde f(p)e^{-ip\cdot x}$ and $\partial^2 + m^2 \leftrightarrow m^2 - p^2$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], 2), the equation becomes $(m^2 - p^2)\tilde f(p) = 0$ as generalized functions of $p$ (the derivative rule holds in $\mathcal S'$, [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-5|Theorem §CA.4.5]], 3; $f$ tempered).
>
> **Step 2** (support). Where $p^2 \ne m^2$ one may divide by the smooth nonzero factor (multiplication by the smooth function $1/(m^2 - p^2)$ on that open set, [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], 1), so $\tilde f = 0$ there. On the shell, in the variable $s = p^2 - m^2$, the equation is $s\,T = 0$, whose solutions are multiples of $\delta(s)$: a derivative term is excluded because $s\,\delta'(s) = -\delta(s) \ne 0$. (Sense: near the shell, $(p^0, \mathbf p) \mapsto (s, \mathbf p)$ is a smooth change of variables because $\partial s/\partial p^0 = 2p^0 \ne 0$ there for $m > 0$; in the variable $s$ the distribution is supported at $s = 0$, so by [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]] it is a finite sum of derivatives of $\delta(s)$ with coefficients depending on $\mathbf p$; this is [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], 2.) So $\tilde f = 2\pi\delta(p^2 - m^2)g(p)$ for some $g$ on the shell.
>
> **Step 3** (do the $p^0$ integral). By the composition rule ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]]; as distributions, [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, and [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1), roots $p^0 = \pm E_{\mathbf p}$ with $|\partial_{p^0}(p^2 - m^2)| = 2E_{\mathbf p}$: $\delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}}$. Then
>
> $$
> f(x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl[g(E_{\mathbf p}, \mathbf p)\,e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} + g(-E_{\mathbf p}, \mathbf p)\,e^{iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x}\Bigr].
> $$
>
> **Step 4** (relabel the negative-energy term). Substitute $\mathbf p \to -\mathbf p$ there (Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$; [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], 1, in the pairing with a test function): it becomes $g(-E_{\mathbf p}, -\mathbf p)e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x} = g(-p)\,e^{ip\cdot x}$ with $p = (E_{\mathbf p}, \mathbf p)$. This is the stated formula.
>
> **Step 5** (real solutions). Reality of $f$ gives $g(-p) = \overline{g(p)}$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], 4).
>
> **What the derivation shows.**
> - The three-dimensional mode expansions are four-dimensional transforms restricted to the shell, and the invariant measure $d^3p/2E_{\mathbf p}$ is what the shell leaves behind.
> - A free field has no off-shell Fourier components; a Green's function must have them ([[§C2b.6 Green's Functions and Contours#^thm-c2b-6-2|Theorem §C2b.6.2]]), and that is where the difficulty is.
> - Used next: the mode expansion of the Heisenberg field (Theorem §C2b.1.4; the coefficient is identified there, $g(p) = \sqrt{2E_{\mathbf p}}\,\hat a_{\mathbf p}$, in the paragraph after its derivation), the support of homogeneous solutions in the uniqueness of $D_R$ ([[§C2b.6 Green's Functions and Contours#^thm-c2b-6-6|Theorem §C2b.6.6]]) and all fundamental solutions ([[§C2b.6 Green's Functions and Contours#^thm-c2b-6-4|Theorem §C2b.6.4]]).

^der-c2b-1-3

*Uses:* [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]]

> [!theorem] Theorem §C2b.1.4: Time Dependence of the Modes; the Covariant Mode Expansion
> 1. The Schrödinger ladder operators acquire phases: $e^{i\hat Ht}\hat a_{\mathbf p}e^{-i\hat Ht} = \hat a_{\mathbf p}\,e^{-iE_{\mathbf p}t}$ and $e^{i\hat Ht}\hat a_{\mathbf p}^\dagger e^{-i\hat Ht} = \hat a_{\mathbf p}^\dagger\,e^{iE_{\mathbf p}t}$.
> 2. Hence, with $p^0 = E_{\mathbf p}$ (not an integration variable),
>
> $$
> \hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p}\,e^{-ip\cdot x} + \hat a_{\mathbf p}^\dagger\,e^{ip\cdot x}\Bigr), \qquad \hat\pi(x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(\hat a_{\mathbf p}\,e^{-ip\cdot x} - \hat a_{\mathbf p}^\dagger\,e^{ip\cdot x}\Bigr) .
> $$
>
> 3. $\hat\pi(x) = \partial_t\hat\phi(x)$.
> 4. Mode extraction holds on every time slice: with $f_{\mathbf p} = e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$ and the Klein–Gordon product of [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], the Heisenberg fields $\hat\phi(x)$, $\hat\pi(x)$ of parts 2–3 give
>
> $$
> \hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\;e^{ip\cdot x}\bigl(\hat\pi(x) - iE_{\mathbf p}\,\hat\phi(x)\bigr), \qquad \hat a^\dagger_{\mathbf p} = -(f^*_{\mathbf p}, \hat\phi) ,
> $$
>
> independent of the time slice on which the integral is taken; the slice $t = 0$ is [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]].
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free vacuum $|0\rangle$, exact; with interactions this is the interaction-picture field ([[§C6a.2 The Interaction Picture#^thm-c6a-2-1|Theorem §C6a.2.1]]), not the Heisenberg field ([[§C2b.1 Heisenberg Fields#^cau-c2b-1-2|Caution: With interactions, the Heisenberg field is not the free mode expansion]]); the slice independence of part 4 uses the free field equation, so with interactions the extraction holds at the reference time only.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1 · PS §2.4, eqs. (2.46)–(2.47) · part 4: the sources of Theorem §C2a.2.5 (the user's PHY 513 notes, Ch. 4 §4.5; Yu §2.3.2, eqs. (2.106)–(2.113))*

^thm-c2b-1-4

> [!derivation]- Derivation
> **Step 1** (the Hamiltonian in mode form). By [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], with the integration variable renamed $\mathbf q$ so that it cannot clash with the $\mathbf p$ of the operator being moved,
>
> $$
> \hat H = \int\frac{d^3q}{(2\pi)^3}\,E_{\mathbf q}\,\hat a_{\mathbf q}^\dagger \hat a_{\mathbf q} + E_0 .
> $$
>
> ⚑ By-product: the zero-point constant $E_0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]) is a number, so it commutes with every operator and drops out of every commutator below; time evolution does not see it → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]].
>
> **Step 2** (one commutator). With $[AB, C] = A[B, C] + [A, C]B$,
>
> $$
> [\hat a_{\mathbf q}^\dagger \hat a_{\mathbf q}, \hat a_{\mathbf p}] = \hat a_{\mathbf q}^\dagger\underbrace{[\hat a_{\mathbf q}, \hat a_{\mathbf p}]}_{=0} + [\hat a_{\mathbf q}^\dagger, \hat a_{\mathbf p}]\,\hat a_{\mathbf q} = -(2\pi)^3\delta^3(\mathbf q - \mathbf p)\,\hat a_{\mathbf q},
> $$
>
> using $[\hat a_{\mathbf q}, \hat a_{\mathbf p}] = 0$ and $[\hat a_{\mathbf q}^\dagger, \hat a_{\mathbf p}] = -[\hat a_{\mathbf p}, \hat a_{\mathbf q}^\dagger] = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]); the minus sign is there because this is the $\hat a^\dagger\hat a$ order, not the $\hat a\hat a^\dagger$ order that defines the normalization.
>
> **Step 3** (integrate the delta). The $\mathbf q$ integral is done by $\delta^3(\mathbf q - \mathbf p)$, which sets $\mathbf q = \mathbf p$ and $E_{\mathbf q} = E_{\mathbf p}$ (sense: $[\hat a_{\mathbf q}^\dagger, \hat a_{\mathbf p}]$ is an operator-valued distribution in $(\mathbf p, \mathbf q)$, [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]; for a smeared annihilator $\hat a(g) = \int\frac{d^3p}{(2\pi)^3}g(\mathbf p)\hat a_{\mathbf p}$, $g \in \mathcal S$, the step reads $[\hat H, \hat a(g)] = -\hat a(E g)$, the delta acting on the smooth function $E_{\mathbf q}g(\mathbf q)$, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]):
>
> $$
> [\hat H, \hat a_{\mathbf p}] = -\int\frac{d^3q}{(2\pi)^3}\,E_{\mathbf q}\,(2\pi)^3\delta^3(\mathbf q - \mathbf p)\,\hat a_{\mathbf q} = -E_{\mathbf p}\,\hat a_{\mathbf p}, \qquad\text{i.e.}\qquad \hat H\hat a_{\mathbf p} = \hat a_{\mathbf p}\,(\hat H - E_{\mathbf p}) .
> $$
>
> **Step 4** (powers). By induction, $\hat H^n\hat a_{\mathbf p} = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})^n$: if it holds for $n$, then $\hat H^{n+1}\hat a_{\mathbf p} = \hat H\,\hat a_{\mathbf p}(\hat H - E_{\mathbf p})^n = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})^{n+1}$ by Step 3.
>
> **Step 5** (exponentiate). Summing the series term by term,
>
> $$
> e^{i\hat Ht}\hat a_{\mathbf p} = \sum_{n=0}^\infty\frac{(it)^n}{n!}\hat H^n\hat a_{\mathbf p} = \hat a_{\mathbf p}\sum_{n=0}^\infty\frac{(it)^n}{n!}(\hat H - E_{\mathbf p})^n = \hat a_{\mathbf p}\,e^{i\hat Ht}e^{-iE_{\mathbf p}t},
> $$
>
> where $e^{i(\hat H - E)t} = e^{i\hat Ht}e^{-iEt}$ because $E_{\mathbf p}$ is a number. Multiplying on the right by $e^{-i\hat Ht}$ gives part 1 for $\hat a_{\mathbf p}$. (This is the Baker–Hausdorff lemma for $[G, A] = \kappa A$, [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-2|QM Theorem §C3.3.2]], exactly as for one oscillator in [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]].)
>
> **Step 6** (the adjoint). Taking the Hermitian conjugate of part 1 for $\hat a_{\mathbf p}$, with $(e^{i\hat Ht})^\dagger = e^{-i\hat Ht}$, gives $e^{i\hat Ht}\hat a_{\mathbf p}^\dagger e^{-i\hat Ht} = \hat a_{\mathbf p}^\dagger e^{+iE_{\mathbf p}t}$.
>
> **Step 7** (the Schrödinger field, un-relabelled). [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] writes $\hat\phi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p} + \hat a_{-\mathbf p}^\dagger)e^{i\mathbf p\cdot\mathbf x}$. In the $\hat a^\dagger_{-\mathbf p}$ term substitute $\mathbf p \to -\mathbf p$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], 1, valid in the pairing with a test function, i.e. after smearing in $\mathbf x$): the Jacobian is $|\det(-\mathbf 1)| = 1$, the domain $\mathbb R^3$ is unchanged, $E_{-\mathbf p} = E_{\mathbf p}$, and the exponent becomes $e^{-i\mathbf p\cdot\mathbf x}$. So
>
> $$
> \hat\phi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p}\,e^{i\mathbf p\cdot\mathbf x} + \hat a_{\mathbf p}^\dagger\,e^{-i\mathbf p\cdot\mathbf x}\Bigr), \qquad \hat\pi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(\hat a_{\mathbf p}\,e^{i\mathbf p\cdot\mathbf x} - \hat a_{\mathbf p}^\dagger\,e^{-i\mathbf p\cdot\mathbf x}\Bigr),
> $$
>
> the second by the same substitution in $\hat\pi_S$.
>
> **Step 8** (conjugate term by term). $e^{i\hat Ht}$ passes through the numbers $e^{\pm i\mathbf p\cdot\mathbf x}$ and the integral (sense: smeared in $\mathbf x$ with $g \in \mathcal S(\mathbb R^3)$, the integral is $\int\frac{d^3p}{(2\pi)^3}\bigl(\tilde g(-\mathbf p)\hat a_{\mathbf p} + \tilde g(\mathbf p)\hat a^\dagger_{\mathbf p}\bigr)/\sqrt{2E_{\mathbf p}}$ with Schwartz coefficients, and a unitary passes through it in every matrix element), and acts on $\hat a_{\mathbf p}$, $\hat a_{\mathbf p}^\dagger$ by Steps 5–6:
>
> $$
> e^{i\hat Ht}\hat\phi_S(\mathbf x)e^{-i\hat Ht} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p}\,e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} + \hat a_{\mathbf p}^\dagger\,e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x}\Bigr),
> $$
>
> and $-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x = -ip\cdot x$ with $p^0 = E_{\mathbf p}$. For $\hat\pi$ only the coefficient differs, $-i\sqrt{E_{\mathbf p}/2}$ instead of $1/\sqrt{2E_{\mathbf p}}$, and the relative minus sign:
>
> $$
> e^{i\hat Ht}\hat\pi_S(\mathbf x)e^{-i\hat Ht} = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(\hat a_{\mathbf p}\,e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} - \hat a_{\mathbf p}^\dagger\,e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x}\Bigr) .
> $$
>
> This is part 2.
>
> ⚑ By-product: $p^0$ in $e^{\mp ip\cdot x}$ is the function $E_{\mathbf p}$ of the integration variable, not a variable of its own; this is where the remaining non-covariance hides → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-2|Remark: What is covariant and what is not yet]].
>
> **Step 9** (differentiate). $\partial_te^{-ip\cdot x} = -iE_{\mathbf p}e^{-ip\cdot x}$ and $\partial_te^{ip\cdot x} = +iE_{\mathbf p}e^{ip\cdot x}$; differentiating under the integral (as a distribution, [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]; concretely, smeared with $g \in \mathcal S(\mathbb R^3)$ the $t$-derivative brings down $\mp iE_{\mathbf p}$ against the Schwartz coefficient $\tilde g(\mp\mathbf p)$, still absolutely integrable in every wave-packet matrix element, so [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2 applies) and using $E_{\mathbf p}/\sqrt{2E_{\mathbf p}} = \sqrt{E_{\mathbf p}/2}$,
>
> $$
> \partial_t\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(-iE_{\mathbf p}\,\hat a_{\mathbf p}e^{-ip\cdot x} + iE_{\mathbf p}\,\hat a_{\mathbf p}^\dagger e^{ip\cdot x}\Bigr) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(\hat a_{\mathbf p}e^{-ip\cdot x} - \hat a_{\mathbf p}^\dagger e^{ip\cdot x}\Bigr) = \hat\pi(x) .
> $$
>
> The sign check the lecture recommended: $\partial_t$ of the $\hat a$ term must give $-iE_{\mathbf p}$.
>
> ⚑ By-product: $\hat\pi = \partial_t\hat\phi$, a definition in classical field theory and not even expressible in the Schrödinger picture, is now a theorem → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|Remark: Two routes that meet]].
>
> **Step 10** (mode extraction on any slice; part 4). Write out the Klein–Gordon product ([[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]]) on the slice of time $t$ with $f^{\ast}_{\mathbf p} = e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $\partial_tf^{\ast}_{\mathbf p} = iE_{\mathbf p}f^{\ast}_{\mathbf p}$ and $\partial_t\hat\phi = \hat\pi$ (Step 9):
>
> $$
> (f_{\mathbf p}, \hat\phi) = i\int d^3x\,\bigl(f^*_{\mathbf p}\,\hat\pi - iE_{\mathbf p}f^*_{\mathbf p}\,\hat\phi\bigr) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\;e^{ip\cdot x}\bigl(\hat\pi(x) - iE_{\mathbf p}\,\hat\phi(x)\bigr) .
> $$
>
> Part 2 is the expansion $\hat\phi = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}f_{\mathbf q} + \hat a^\dagger_{\mathbf q}f^{\ast}_{\mathbf q}\bigr)$ at time $t$, for which [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-5|Derivation §C2a.2.5]], steps 5–6, evaluate the integral at a general time: $\int d^3x\,e^{ip\cdot x}\hat\phi = \bigl(\hat a_{\mathbf p} + e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}\bigr)/\sqrt{2E_{\mathbf p}}$ and $\int d^3x\,e^{ip\cdot x}\hat\pi = -iE_{\mathbf p}\bigl(\hat a_{\mathbf p} - e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}\bigr)/\sqrt{2E_{\mathbf p}}$, so in $\hat\pi - iE_{\mathbf p}\hat\phi$ the $\hat a^\dagger_{-\mathbf p}$ terms, and with them all $t$-dependence, cancel and $(f_{\mathbf p}, \hat\phi) = \hat a_{\mathbf p}$ on every slice. The same follows from the orthonormality of the modes, which holds on every slice because the Klein–Gordon product of two solutions is conserved ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 1–2): steps 1–3 of that derivation then run at time $t$ unchanged. The adjoint gives $\hat a^\dagger_{\mathbf p} = -(f^{\ast}_{\mathbf p}, \hat\phi)$. *Sense:* an identity of operator-valued distributions in $\mathbf p$, exact after smearing with $\overline{g(\mathbf p)}$, as there.
>
> **What the derivation shows.**
> - Conjugation with $e^{i\hat Ht}$ does nothing to $\hat a_{\mathbf p}$ but attach the phase of a positive-energy wave function; $\hat a_{\mathbf p}$ itself stays the time-independent Schrödinger operator (PS's convention).
> - Only $[\hat a, \hat a^\dagger]$ and the mode form of $\hat H$ were used; the zero-point constant never enters time evolution.
> - The mode operators can be read off the Heisenberg field on any slice (part 4): $\hat a_{\mathbf p}$ is one operator, not one per time.
> - Used next: the two-point functions (Theorems §C2b.2.1, §C2b.5.2) and, through $\hat\pi = \partial_t\hat\phi$, the unequal-time commutators (Theorem §C2b.5.11).

^der-c2b-1-4

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-2|QM Theorem §C3.3.2]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]]

**The Heisenberg field on the mass shell.** The Heisenberg field solves the Klein–Gordon equation as an operator ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]), so [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]] applies to it. Compared with the mode expansion of Theorem §C2b.1.4, 2, obtained independently from the Hamiltonian (its derivation does not use Theorem §C2b.1.3), $g(p)/2E_{\mathbf p} = \hat a_{\mathbf p}/\sqrt{2E_{\mathbf p}}$, so $g(p) = \sqrt{2E_{\mathbf p}}\,\hat a_{\mathbf p}$; and $g(-p) = \overline{g(p)}$ (Derivation §C2b.1.3, Step 5) is here $\sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}$.

> [!remark] Remark: What is covariant and what is not yet
> The spatial Fourier factors have become four-dimensional plane waves, the first manifestly covariant-looking expression of the quantum theory. But the integral still runs over three momenta: $p^0$ is not a variable, it means $E_{\mathbf p}$, a square root of the integration variable. The remaining non-covariance hides there, and the invariant measure $d^3p/(2\pi)^32E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) is the bookkeeping that keeps it honest. In [[§C2b.6 Green's Functions and Contours|§C2b.6]], $p^0$ becomes an integration variable, and the poles at $p^0 = \pm E_{\mathbf p}$ are the price.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1, §5.7 (closing paragraph)*

^rem-c2b-1-2

> [!caution] Caution: With interactions, the Heisenberg field is not the free mode expansion
> [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]] is the Heisenberg field of the free $\hat H$ ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]). With $\hat H = \hat H_0 + \hat H_{\rm int}$ ([[§C6a.1 From Free to Interacting Fields#^mod-c6a-1-1|Model §C6a.1.1]]) the same expansion is the interaction-picture field, and the Heisenberg field is obtained from it by the evolution operator $U(t) = e^{i\hat H_0t}e^{-i\hat Ht}$:
>
> $$
> \hat\phi_I(t, \mathbf x) = e^{i\hat H_0t}\,\hat\phi_S(\mathbf x)\,e^{-i\hat H_0t}\ \ (\text{the expansion of Theorem §C2b.1.4}), \qquad \hat\phi_H(t, \mathbf x) = e^{i\hat Ht}\,\hat\phi_S(\mathbf x)\,e^{-i\hat Ht} = U(t)^\dagger\,\hat\phi_I(t, \mathbf x)\,U(t) ,
> $$
>
> ([[§C6a.2 The Interaction Picture#^def-c6a-2-1|Def. §C6a.2.1]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-1|Theorem §C6a.2.1]], [[§C6a.2 The Interaction Picture#^thm-c6a-2-4|Theorem §C6a.2.4]]). The two agree at $t = 0$ only: for $\lambda \ne 0$ the ladder operators acquire no phases under $\hat H$ ([[§C6a.1 From Free to Interacting Fields#^thm-c6a-1-7|Theorem §C6a.1.7]], 2). The same holds for the Dirac field of [[§C5b.6 The Heisenberg Dirac Field|§C5b.6]].
>
> *Source: PHY 513 Lecture 13, slide 7 ("As a first approximation introduce interaction picture"; "Complete time dependence") · PS §4.2, pp. 82–83*

^cau-c2b-1-2

> [!theorem] Theorem §C2b.1.5: Positive and Negative Frequency
> Split $\hat\phi = \hat\phi^+ + \hat\phi^-$ with
>
> $$
> \hat\phi^+(x) = \int\frac{d^3p}{(2\pi)^3}\frac{\hat a_{\mathbf p}\,e^{-ip\cdot x}}{\sqrt{2E_{\mathbf p}}}\quad\text{(positive frequency)}, \qquad \hat\phi^- = (\hat\phi^+)^\dagger\quad\text{(negative frequency)} .
> $$
>
> Then $\hat\phi^+|0\rangle = 0$, $\langle0|\hat\phi^- = 0$, and for the one-particle states $|\mathbf p\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), with $p^0 = E_{\mathbf p} > 0$,
>
> $$
> \langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}, \qquad \langle\mathbf p|\hat\phi(x)|0\rangle = e^{ip\cdot x} .
> $$
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free vacuum $|0\rangle$, exact; with interactions: [[§C2b.1 Heisenberg Fields#^cau-c2b-1-3|Caution: With interactions, the one-particle matrix element carries √Z]].
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.3, Ch. 6 §6.7 (the split $\hat\phi^\pm$) · PS §2.4, p. 26 · Yu §6.3, eqs. (6.132)–(6.133)*

^thm-c2b-1-5

> [!derivation]- Derivation
> **Step 1** (the vacuum). $\hat a_{\mathbf p}|0\rangle = 0$ for every $\mathbf p$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-2|Principle §C2a.3.2]]), so $\hat\phi^+(x)|0\rangle = 0$; taking adjoints, $\langle0|\hat\phi^-(x) = 0$.
>
> **Step 2** (only $\hat\phi^+$ contributes). $\langle0|\hat\phi(x)|\mathbf p\rangle = \langle0|\hat\phi^+(x)|\mathbf p\rangle + \langle0|\hat\phi^-(x)|\mathbf p\rangle$, and the second term is zero by Step 1.
>
> **Step 3** (insert, with a new name for the field's momentum).
>
> $$
> \langle0|\hat\phi^+(x)|\mathbf p\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E_{\mathbf q}}}\sqrt{2E_{\mathbf p}}\;\langle0|\hat a_{\mathbf q}\hat a_{\mathbf p}^\dagger|0\rangle .
> $$
>
> **Step 4** (reorder). $\hat a_{\mathbf q}\hat a_{\mathbf p}^\dagger = [\hat a_{\mathbf q}, \hat a_{\mathbf p}^\dagger] + \hat a_{\mathbf p}^\dagger \hat a_{\mathbf q}$; the second term annihilates $|0\rangle$, so $\langle0|\hat a_{\mathbf q}\hat a_{\mathbf p}^\dagger|0\rangle = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).
>
> **Step 5** (integrate the delta). It sets $\mathbf q = \mathbf p$, so $E_{\mathbf q} = E_{\mathbf p}$ and $q^0 = p^0$; the square roots cancel and $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$. (Sense: $|\mathbf p\rangle$ is not normalizable, so Steps 3–5 compute the kernel of $g \mapsto \langle0|\hat\phi(x)|g\rangle$ for wave packets $|g\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}g(\mathbf p)|\mathbf p\rangle$, $g \in \mathcal S$, the delta acting on the smooth integrand; the result is a continuous function of $\mathbf p$, so the kernel has a value at every $\mathbf p$.)
>
> **Step 6** (the conjugate). $\hat\phi$ is Hermitian, so $\langle\mathbf p|\hat\phi(x)|0\rangle = \overline{\langle0|\hat\phi(x)|\mathbf p\rangle} = e^{ip\cdot x}$.
>
> **What the derivation shows.**
> - The relativistic normalization ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) is what makes the amplitude exactly a plane wave, with no $E_{\mathbf p}$-dependent factor; at $t = 0$ this is [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]].
> - Positive frequency goes with annihilation, negative frequency with creation → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-3|Remark: Negative frequency is creation, not negative energy]].
> - Used next: the split $\hat\phi^\pm$ gives normal ordering and the contraction ([[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-6|Theorem §C2b.7.6]]).

^der-c2b-1-5

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^pr-c2a-3-2|Principle §C2a.3.2]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]]

> [!remark] Remark: Negative frequency is creation, not negative energy
> A complete set of solutions of the Klein–Gordon equation has both $e^{-iEt}$ and $e^{+iEt}$, and a Hermitian field needs both. Read as single-particle wave functions they would be states of energy $\pm E$, the old difficulty of relativistic wave mechanics ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-2|QM Theorem §C13.1.2]]). In the field, the coefficient of the positive-frequency solution is the operator that *destroys* a quantum, and $\langle0|\hat\phi|\mathbf p\rangle = e^{-ip\cdot x}$ is a positive-energy wave function; the coefficient of the negative-frequency solution *creates* one. No state of negative energy exists in the spectrum ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]]). Wave and particle sit in one formula: the plane waves are the wave aspect, the operator coefficients with $[\hat a, \hat a^\dagger] = (2\pi)^3\delta^3$ the particle aspect. Notation: PS's $\phi^+$ and Yu's $\phi^{(+)}$ are the positive-frequency, annihilating part, as here.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.3 · PS §2.4, p. 26*

^rem-c2b-1-3

> [!caution] Caution: With interactions, the one-particle matrix element carries √Z
> [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]] is a free-field result: $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$ with $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}|0\rangle$. In an interacting theory ([[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]]), with $|\mathbf p\rangle$ a relativistically normalized one-particle state of $\hat H$ and the phase chosen real,
>
> $$
> \langle\Omega|\hat\phi_H(x)|\mathbf p\rangle = \sqrt Z\,e^{-ip\cdot x} , \qquad p^0 = \sqrt{\mathbf p^2 + m_{\rm ph}^2} ,
> $$
>
> with $m_{\rm ph}$ the physical mass; the $x$-dependence is translation invariance: $\hat\phi_H(x) = e^{i\hat P\cdot x}\hat\phi_H(0)e^{-i\hat P\cdot x}$, $\hat{\mathbf P}|\Omega\rangle = 0$, and the vacuum energy $E_0$ of [[§C6a.4 The Interacting Vacuum and the Two-Point Function#^def-c6a-4-1|Def. §C6a.4.1]] cancels between $\langle\Omega|$ and $|\mathbf p\rangle$ (energy $E_0 + p^0$). The factor $\sqrt Z$ per external particle is what the amputation rule leaves out at lowest order ([[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]; the LSZ formula, deferred by the course to the second semester, QFT C10 (planned)).
>
> *Source: Yu §10.2, p. 447, eqs. (10.64)–(10.65) ($\langle p|\phi(0)|0\rangle = \sqrt Z$ with the phase set to 1, then $\langle p|\phi(x)|0\rangle = \sqrt Z\,e^{ip\cdot x}$; Yu's $|0\rangle$ is $|\Omega\rangle$, [[§C6a.0 Setups and Observables#^cau-c6a-0-1|§C6a.0, Caution: Names for the vacua]]) · Yu §10.5.3, eq. (10.235)*

^cau-c2b-1-3

## The field on spacetime

> [!theorem] Theorem §C2b.1.6: The Heisenberg Field Is an Operator-Valued Distribution on Spacetime
> For $f \in \mathcal S(\mathbb R^4)$ let $\hat\phi(f) \equiv \int d^4x\,f(x)\,\hat\phi(x)$, the spacetime version of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], and $\tilde f(p) = \int d^4x\,f(x)\,e^{ip\cdot x}$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^def-ca-4-1|Def. §CA.4.1]]). With $p^0 = E_{\mathbf p}$:
> 1. $\displaystyle\hat\phi(f) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\tilde f(-p)\,\hat a_{\mathbf p} + \tilde f(p)\,\hat a_{\mathbf p}^\dagger\Bigr)$, and $\hat\phi(f)|0\rangle$ is a one-particle state with $\|\hat\phi(f)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\tilde f(p)|^2 < \infty$. So $\hat\phi$ is an operator-valued tempered distribution on $\mathbb R^4$ ([[§CA.3 Products of Distributions and Operator-Valued Distributions#^def-ca-3-1|Def. §CA.3.1]]); $\hat\phi(x)$ unsmeared is not an operator.
> 2. $\hat\phi(f)$ depends on $\tilde f$ only through its values on the mass shell $p^2 = m^2$.
> 3. The Klein–Gordon equation holds as an identity of operator-valued distributions: $\hat\phi\bigl((\partial^2 + m^2)f\bigr) = 0$ for every $f$, which is what $(\partial^2 + m^2)\hat\phi = 0$ means.
>
> *Model:* [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free field, free vacuum $|0\rangle$, exact.
>
> *Source: the user's PHY 513 notes, App. A §A.4 ($\hat\phi[\varphi] = \int d^4x\,\varphi(x)\hat\phi(x)$), Ch. 6 §6.2 ("operator-valued distribution") · stated here for the Heisenberg field (standard: Streater & Wightman, Ch. 3; Reed & Simon II, §X.7)*

^thm-c2b-1-6

> [!derivation]- Derivation
> **Step 1** (smear term by term). Take finite-particle wave-packet states $\Psi_1$, $\Psi_2$ (Schwartz amplitudes; [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]). The matrix elements $\langle\Psi_1|\hat a_{\mathbf p}|\Psi_2\rangle$ and $\langle\Psi_1|\hat a_{\mathbf p}^\dagger|\Psi_2\rangle$ are Schwartz functions of $\mathbf p$, so in $\langle\Psi_1|\hat\phi(x)|\Psi_2\rangle$, written with [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], the $\mathbf p$-integral converges absolutely for every $x$, and $\int d^4x\int d^3p\,|f(x)|\,|\langle\Psi_1|\hat a_{\mathbf p}|\Psi_2\rangle|/\sqrt{2E_{\mathbf p}} < \infty$. Fubini therefore lets the $x$-integral go inside ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]], "after smearing"):
>
> $$
> \int d^4x\,f(x)\,e^{-ip\cdot x} = \tilde f(-p), \qquad \int d^4x\,f(x)\,e^{ip\cdot x} = \tilde f(p), \qquad p^0 = E_{\mathbf p} .
> $$
>
> This is the formula of part 1, read in every such matrix element.
>
> **Step 2** (decay on the shell). $\tilde f \in \mathcal S(\mathbb R^4)$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-1|Theorem §CA.4.1]], 1), so $|\tilde f(k)| \le C_N(1 + |k^0| + |\mathbf k|)^{-N}$ for every $N$. On the shell $|\pm\mathbf p| = |\mathbf p|$, hence $|\tilde f(\pm E_{\mathbf p}, \pm\mathbf p)| \le C_N(1 + |\mathbf p|)^{-N}$.
>
> **Step 3** (on the vacuum). $\hat a_{\mathbf p}|0\rangle = 0$ removes the first term: $\hat\phi(f)|0\rangle = \int\frac{d^3p}{(2\pi)^3}\frac{\tilde f(p)}{\sqrt{2E_{\mathbf p}}}\hat a_{\mathbf p}^\dagger|0\rangle$. With $\langle0|\hat a_{\mathbf q}\hat a_{\mathbf p}^\dagger|0\rangle = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]; the delta acts on the Schwartz coefficient as in [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]),
>
> $$
> \|\hat\phi(f)|0\rangle\|^2 = \int\frac{d^3q\,d^3p}{(2\pi)^6}\frac{\overline{\tilde f(q)}\,\tilde f(p)}{\sqrt{2E_{\mathbf q}\,2E_{\mathbf p}}}(2\pi)^3\delta^3(\mathbf q - \mathbf p) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,|\tilde f(p)|^2,
> $$
>
> finite by Step 2 with $N = 2$: $1/2E_{\mathbf p} \le 1/2|\mathbf p|$ is integrable near $\mathbf p = 0$ in three dimensions (so $m = 0$ is included).
>
> ⚑ By-product: concentrating $f$ at one point, $\tilde f(p) \to e^{ip\cdot x}$, turns the norm into $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \infty$, the divergence of Step 6 of Derivation §C2b.2.1: $\hat\phi(x)|0\rangle$ is not a vector, and the vacuum two-point function needs the same smearing → [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]].
>
> **Step 4** (only the shell). By Step 1, $\hat\phi(f)$ involves $\tilde f$ only at the points $(\pm E_{\mathbf p}, \pm\mathbf p)$. This is part 2.
>
> **Step 5** (the field equation). The derivative rule in $\mathcal S$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], 2; [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-5|Theorem §CA.4.5]], 3) gives $\widetilde{(\partial^2 + m^2)f}(k) = (m^2 - k^2)\tilde f(k)$, which vanishes on the shell. By Step 4, $\hat\phi\bigl((\partial^2 + m^2)f\bigr) = 0$. The derivative of an operator-valued distribution is defined by moving it onto the test function ([[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]), two derivatives with sign $(-1)^2 = 1$: $\bigl((\partial^2 + m^2)\hat\phi\bigr)(f) \equiv \hat\phi\bigl((\partial^2 + m^2)f\bigr) = 0$. This is part 3.
>
> **What the derivation shows.**
> - Smearing in time as well as in space turns the mode integral into an absolutely convergent one in every matrix element; the decay comes from $\tilde f$ on the shell.
> - Part 3 is the distributional content of the operator equation of Theorem §C2b.1.2: the free field ignores every off-shell component of a test function.
> - Used next: the vacuum two-point function as a distribution (Theorem §C2b.2.2), unequal-time commutators (Theorem §C2b.5.12) and the particle number produced by a source (Theorem §C2b.9.1).

^der-c2b-1-6

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§CA.3 Products of Distributions and Operator-Valued Distributions#^def-ca-3-1|Def. §CA.3.1]], [[§CA.4 Fourier Transforms and Fourier Tricks#^def-ca-4-1|Def. §CA.4.1]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-1|Theorem §CA.4.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]

> [!remark] Remark: Two routes that meet
> Theorem §C2b.1.2 never used the mode expansion. One could start from it: postulate the commutators and $\hat H$, derive the Klein–Gordon equation, expand its solutions in $e^{\mp ip\cdot x}$ (they live on the mass shell, [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]), name the coefficients $\hat a_{\mathbf p}$, $\hat a_{\mathbf p}^\dagger$, and compute their algebra. That is the "field first" route of Yu §2.3 and of the user's notes; the lecture went "oscillators first", diagonalizing $\hat H$ and discovering afterwards that the result solves a wave equation ([[P1 Canonical Quantization|P1]]). That the two routes meet is Theorem §C2b.1.4 against Theorem §C2b.1.2. Level change: QM's preview asserted the operator Klein–Gordon equation for the mode sum it wrote down ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-6|QM Theorem §C13.1.6]], 1); here it follows from the canonical structure alone, and $\hat\pi = \partial_t\hat\phi$, a definition in classical field theory, becomes a consequence of the commutators.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 ("The logic run backwards")*

^rem-c2b-1-4

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]] — δ acts on test functions: the deltas of the Heisenberg equations and of the mode algebra are read after smearing.
> - [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]] (derivatives moved onto the test function) and [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]] (integration by parts against δ) give $\partial_t\hat\phi = \hat\pi$ and the $\nabla^2\hat\phi$ of the Heisenberg equations; [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]] licenses the $t$-derivative under the smeared mode integral.
> - [[§CA.3 Products of Distributions and Operator-Valued Distributions#^def-ca-3-1|Def. §CA.3.1]] (operator-valued distributions) is what the Heisenberg field is: Theorem §C2b.1.6 smears it over spacetime, the four-dimensional version of the time-slice smearing of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]].
> - [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-1|Theorem §CA.3.1]], 1 — division by the smooth nonzero factor $m^2 - p^2$ off the shell, and the form of a distribution supported on the shell (Theorem §C2b.1.3).
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1 — $\delta(p^2 - m^2)$ composed with the shell: the $p^0$ integral leaves $d^3p/2E_{\mathbf p}$ at $p^0 = \pm E_{\mathbf p}$.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^def-ca-4-1|Def. §CA.4.1]] — the spacetime Fourier convention $\tilde f(p) = \int d^4x\,f(x)\,e^{ip\cdot x}$ of the smeared field (Theorem §C2b.1.6).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-1|Theorem §CA.4.1]] (the transform maps $\mathcal S$ to $\mathcal S$) supplies the on-shell decay of $\tilde f$ that makes $\hat\phi(f)|0\rangle$ normalizable; the same decay makes the particle number of a source finite ([[§C2b.9 Particle Production by a Classical Source#^thm-c2b-9-1|Theorem §C2b.9.1]]).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-4|Theorem §CA.4.4]] (derivative rule) turns the Klein–Gordon equation into "the field ignores off-shell test functions", Theorem §C2b.1.6, 3.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-5|Theorem §CA.4.5]], 3 — the derivative rule in $\mathcal S'$: the Klein–Gordon equation becomes $(m^2 - p^2)\tilde f = 0$ for a tempered solution.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]] (exchanging the $x$- and $p$-integrals) is the step that turns the formal mode expansion into $\hat\phi(f)$, valid because the coefficients are smeared.
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-6|Theorem §CA.4.6]] (relabelling $\mathbf p \to -\mathbf p$) rewrites the Schrödinger field in Step 7 of Derivation §C2b.1.4.
> - [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], 2 — homogeneous solutions of the Klein–Gordon operator have their transform on the mass shell (Theorem §C2b.1.3).

> [!remark]- Connections
> - [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]] is the time component of a four-dimensional statement, $\hat\phi(x) = e^{i\hat P\cdot x}\hat\phi(0)e^{-i\hat P\cdot x}$, equivalently $[\hat\phi, \hat P^\mu] = i\partial^\mu\hat\phi$: translation invariance on the Hilbert space — [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-2|Theorem §C3.5.2]].
> - Theorem §C2b.1.4 is the field version of the oscillator in the Heisenberg picture, $\hat a(t) = \hat a\,e^{-i\omega t}$: [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]]; the same phase makes a coherent state stay coherent in [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5|Theorem §C2a.6.5]].
> - The Heisenberg field is the operator whose vacuum correlations are the two-point functions: the Wightman function is built from it in [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], and its commutator at unequal times is the commutator function of [[§C2b.5 Microcausality and the Commutator Function#^thm-c2b-5-11|Theorem §C2b.5.11]]; the positive- and negative-frequency parts of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]] are what normal ordering and contractions separate — [[§C2b.7 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-7-6|Theorem §C2b.7.6]].
> - A free field has its Fourier transform on the mass shell ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]), while a Green's function must have off-shell components ([[§C2b.6 Green's Functions and Contours#^thm-c2b-6-2|Theorem §C2b.6.2]]): the pole problem of [[§C2b.6 Green's Functions and Contours|§C2b.6]] is the clash of the two. [[§CA.7 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-7-7|Theorem §CA.7.7]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] and [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]] (homogeneous solutions, composition of δ) give the on-shell form.
