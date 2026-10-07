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

The free field of [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]] lives at one instant: a mode expansion, a commutator and a spectrum, with no time in them. This section restores time in the Heisenberg picture ([[§C3.3 The Schrödinger and Heisenberg Pictures#^def-c3-3-1|QM Def. §C3.3.1]]) and asks how the field operator depends on time: first in field form, as an operator equation (the canonical relations hold at every time, and the Heisenberg equations are the Klein–Gordon equation), then through the solutions of that equation, which live on the mass shell and give the covariant mode expansion, and finally what the negative-frequency half of it means. The two-point functions of [[§C2b.2 The Wightman Function|§C2b.2]]–[[§C2b.4 Microcausality and the Commutator Function|§C2b.4]] are built from the Heisenberg field.

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ whenever $p$ is on shell, $[a_{\mathbf p}, a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}^\dagger|0\rangle$. Lecture 5 writes $\omega_{\mathbf p}$ for $E_{\mathbf p}$ ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution: Eₚ, not ωₚ; π, not Π]]). Unless stated otherwise $m > 0$; the massless case is stated separately where it differs.

## The Heisenberg field

> [!definition] Definition §C2b.1.1: Heisenberg Field
> Let $\phi_S(\mathbf x)$, $\pi_S(\mathbf x)$ be the Schrödinger-picture field operators and $H$ the Hamiltonian. The **Heisenberg fields** are
>
> $$
> \phi(x) = \phi(t, \mathbf x) \equiv e^{iHt}\,\phi_S(\mathbf x)\,e^{-iHt}, \qquad \pi(x) \equiv e^{iHt}\,\pi_S(\mathbf x)\,e^{-iHt},
> $$
>
> so that $\phi(0, \mathbf x) = \phi_S(\mathbf x)$. From here on a field with a spacetime argument is a Heisenberg operator, and states are frozen at $t = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1 · PS §2.4, eq. (2.43)*

^def-c2b-1-1

> [!remark] Remark: Why field theory works in the Heisenberg picture
> The definition is QM's Heisenberg picture ([[§C3.3 The Schrödinger and Heisenberg Pictures#^def-c3-3-1|QM Def. §C3.3.1]]) applied to an operator labelled by $\mathbf x$, and the two pictures give the same matrix elements ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-3|QM Theorem §C3.3.3]]). What is new is the reason for preferring it: a time-dependent *state* obeying a Schrödinger equation singles out time, while a time-dependent *operator* $\phi(t, \mathbf x)$ is a function on spacetime that can transform covariantly ([[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]], [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-12|Theorem §C3.5.12]]). Canonical quantization starts in the Schrödinger picture because diagonalizing $H$ at one instant is the continuation of ordinary quantum mechanics ([[P1 Canonical Quantization|P1]]); it then switches.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1*

^rem-c2b-1-1

## The Heisenberg equations

> [!theorem] Theorem §C2b.1.1: The Equal-Time Relations Hold at Every Time
> For every real $t$, the Heisenberg fields of [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]] obey the canonical relations of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]] at the common time $t$:
>
> $$
> [\phi(t, \mathbf x), \pi(t, \mathbf y)] = i\delta^3(\mathbf x - \mathbf y), \qquad [\phi(t, \mathbf x), \phi(t, \mathbf y)] = [\pi(t, \mathbf x), \pi(t, \mathbf y)] = 0 .
> $$
>
> Nothing is asserted for two different times.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 · PS §2.4, eqs. (2.44)–(2.45)*

^thm-c2b-1-1

> [!derivation]- Derivation
> **Step 1** (sandwich the commutator). Insert $\mathbf 1 = e^{-iHt}e^{iHt}$ between the two factors of each product:
>
> $$
> e^{iHt}[\phi_S(\mathbf x), \pi_S(\mathbf y)]e^{-iHt} = e^{iHt}\phi_Se^{-iHt}\,e^{iHt}\pi_Se^{-iHt} - e^{iHt}\pi_Se^{-iHt}\,e^{iHt}\phi_Se^{-iHt} = [\phi(t, \mathbf x), \pi(t, \mathbf y)] .
> $$
>
> One unitary sandwiches the whole product, so the *same* $t$ enters both fields.
>
> **Step 2** (the right side). The right side of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], $i\delta^3(\mathbf x - \mathbf y)$, is a number, so $e^{iHt}(i\delta^3)e^{-iHt} = i\delta^3$ is unchanged. (Sense: both sides are operator-valued distributions in $(\mathbf x, \mathbf y)$; smeared with test functions $f(\mathbf x)g(\mathbf y)$ the statement is $[\phi(t, f), \pi(t, g)] = i\int d^3x\,f g$, the smeared relation of [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]] conjugated by the unitary $e^{iHt}$.)
>
> **Step 3** (the other two relations). The same insertion in $[\phi_S(\mathbf x), \phi_S(\mathbf y)]$ and $[\pi_S(\mathbf x), \pi_S(\mathbf y)]$ gives $[\phi(t, \mathbf x), \phi(t, \mathbf y)]$ and $[\pi(t, \mathbf x), \pi(t, \mathbf y)]$, and their right sides, $0$, are unchanged.
>
> ⚑ By-product: nothing is said about *different* times → [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|Caution: Equal times only]]; the answer is Theorem §C2b.4.10.
>
> **What the derivation shows.**
> - Only the unitarity of $e^{iHt}$ was used, not the form of $H$: the statement holds for any Hamiltonian, free or interacting.
> - Used next: the Heisenberg equations ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]), which commute fields at one common time.

^der-c2b-1-1

*Uses:* [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]

> [!theorem] Theorem §C2b.1.2: The Heisenberg Equations Are the Klein–Gordon Equation
> With the relations at a common time ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]) and $H = \int d^3x\,\bigl[\tfrac12\pi^2 + \tfrac12(\nabla\phi)^2 + \tfrac12m^2\phi^2\bigr]$ ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]), the Heisenberg equation $i\partial_t\mathcal O = [\mathcal O, H]$ gives $\partial_t\phi = \pi$ and $\partial_t\pi = (\nabla^2 - m^2)\phi$, hence the operator equation
>
> $$
> (\partial_\mu\partial^\mu + m^2)\,\phi(x) = 0 .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 · PS §2.4, eqs. (2.44)–(2.45)*

^thm-c2b-1-2

> [!derivation]- Derivation
> **Step 1** (equal-time relations at time $t$). By [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], $[\phi(t, \mathbf x), \pi(t, \mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$ and $[\phi(t, \mathbf x), \phi(t, \mathbf y)] = [\pi(t, \mathbf x), \pi(t, \mathbf y)] = 0$ at every common time $t$; only these are used below.
>
> **Step 2** (the Hamiltonian at time $t$). $H$ commutes with $e^{iHt}$, so $H = e^{iHt}He^{-iHt}$ is the Hamiltonian of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]] with every field replaced by its Heisenberg version at any common time; choose the time $t$ of the operator it will be commuted with (the squares of fields at one point are understood normal-ordered, [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]; the subtracted constant $E_0$ is a number and drops out of every commutator, Step 1 of Derivation §C2b.1.4):
>
> $$
> H = \int d^3x'\,\Bigl[\tfrac12\pi(t, \mathbf x')^2 + \tfrac12\bigl(\nabla'\phi(t, \mathbf x')\bigr)^2 + \tfrac12m^2\phi(t, \mathbf x')^2\Bigr].
> $$
>
> **Step 3** ($\phi$ against the three terms). Write $\phi = \phi(t, \mathbf x)$, $\phi' = \phi(t, \mathbf x')$, $\pi' = \pi(t, \mathbf x')$.
> - $[\phi, \pi'^2] = \pi'[\phi, \pi'] + [\phi, \pi']\pi' = 2i\delta^3(\mathbf x - \mathbf x')\,\pi'$: the commutator is a number, so the two terms are equal. (Sense: $\delta^3(\mathbf x - \mathbf x')\,\pi'$ is a $c$-number distribution times an operator-valued distribution in the same variable; smeared with $g(\mathbf x)$ it becomes $g(\mathbf x')\pi(t, \mathbf x')$, a test function times $\pi$, which is defined: [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]].)
> - $[\phi, (\nabla'\phi')^2] = 0$: $[\phi, \partial'_i\phi'] = \partial'_i[\phi, \phi'] = 0$, because $[\phi, \phi']$ vanishes for *all* $\mathbf x'$ and the difference quotient of an identically zero function is zero.
> - $[\phi, \phi'^2] = 0$.
>
> **Step 4** (the equation for $\phi$). By the Heisenberg equation ([[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]]),
>
> $$
> i\partial_t\phi(t, \mathbf x) = [\phi, H] = \int d^3x'\,\tfrac12\cdot2i\delta^3(\mathbf x - \mathbf x')\,\pi(t, \mathbf x') = i\pi(t, \mathbf x), \qquad\text{so}\qquad \partial_t\phi = \pi .
> $$
>
> (The $\mathbf x'$-integral against $\delta^3(\mathbf x - \mathbf x')$ is the action of δ; after smearing in $\mathbf x$ with $g$ it reads $\int d^3x'\,g(\mathbf x')\pi(t, \mathbf x') = \pi(t, g)$, [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]].)
>
> ⚑ By-product: $\pi = \partial_t\phi$ follows from the commutators alone, without the mode expansion; it agrees with [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], 3 → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|Remark: Two routes that meet]].
>
> **Step 5** (rewrite the gradient term). By [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]],
>
> $$
> \int d^3x'\,(\nabla'\phi')^2 = \oint_{|\mathbf x'| = L}dS\;\phi'\,\hat n\cdot\nabla'\phi' - \int d^3x'\,\phi'\,\nabla'^2\phi' \;\longrightarrow\; -\int d^3x'\,\phi'\,\nabla'^2\phi' \qquad (L \to \infty).
> $$
>
> ⚑ By-product: the surface term is dropped on the assumption that the field falls off at spatial infinity, i.e. for matrix elements between normalizable states (wave packets, [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]). So $H = \int d^3x'\,[\tfrac12\pi'^2 + \tfrac12\phi'(-\nabla'^2 + m^2)\phi']$.
>
> **Step 6** ($\pi$ against the two terms). $[\pi, \pi'^2] = 0$. For the second, with $[\pi, \phi'] = -i\delta^3(\mathbf x - \mathbf x')$,
>
> $$
> [\pi, \phi'(-\nabla'^2 + m^2)\phi'] = [\pi, \phi'](-\nabla'^2 + m^2)\phi' + \phi'(-\nabla'^2 + m^2)[\pi, \phi'] = -i\delta^3(\mathbf x - \mathbf x')(-\nabla'^2 + m^2)\phi' - i\,\phi'(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x').
> $$
>
> In the second term the operator acts on the $c$-number commutator: $(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x')$ is the distributional derivative of δ ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]).
>
> **Step 7** (integrate over $\mathbf x'$). The first term gives $-i(-\nabla^2 + m^2)\phi(t, \mathbf x)$. In the second, move $-\nabla'^2$ onto $\phi'$ by two integrations by parts; the surface terms vanish because the delta function is zero on any large sphere ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]); this is exactly the definition of the derivative of δ, moved onto the factor it multiplies ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]):
>
> $$
> -i\int d^3x'\,\phi'(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x') = -i\int d^3x'\,\bigl[(-\nabla'^2 + m^2)\phi'\bigr]\delta^3(\mathbf x - \mathbf x') = -i(-\nabla^2 + m^2)\phi(t, \mathbf x) .
> $$
>
> The two terms are equal and cancel the $\frac12$: $i\partial_t\pi = [\pi, H] = -i(-\nabla^2 + m^2)\phi$, i.e. $\partial_t\pi = (\nabla^2 - m^2)\phi$.
>
> **Step 8** (combine). Differentiate Step 4 in $t$: $\partial_t^2\phi = \partial_t\pi = (\nabla^2 - m^2)\phi$, i.e. $(\partial_t^2 - \nabla^2 + m^2)\phi = (\partial_\mu\partial^\mu + m^2)\phi = 0$.
>
> **What the derivation shows.**
> - Only the equal-time relations and the form of $H$ were used, never the mode expansion; the mode expansion is recovered by solving the operator equation ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]).
> - Assumption used: fall-off of the field at spatial infinity (Step 5).
> - Every manipulation with $\delta^3$ is an identity of distributions, valid after smearing in $\mathbf x$; the resulting operator equation means $\phi\bigl((\partial^2 + m^2)f\bigr) = 0$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-6|Theorem §C2b.1.6]], 3).
> - The two first-order equations are Hamilton's equations of the classical field ([[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-4|Theorem §C1b.4.4]]; this field: [[§C1b.4 Hamiltonian Field Theory#^ex-c1b-4-1|Example §C1b.4.1]]) with operators in place of functions.
> - Used next: every two-point function solves the homogeneous equation (Theorem §C2b.2.4), and the free Schwinger–Dyson equation ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]).

^der-c2b-1-2

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-4|QM Theorem §C3.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]]

> [!caution] Caution: Equal times only
> - The canonical relations were postulated at one instant. [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]] extends them to every *common* time; at different times nothing has been assumed, and the answer is a theorem ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]).
> - $\phi(\mathbf x)$ commutes with $\nabla\phi(\mathbf y)$ because $[\phi(\mathbf x), \phi(\mathbf y)]$ vanishes for *all* $\mathbf x, \mathbf y$. The same move on $[\phi, \pi]$ gives $\nabla\delta^3 \neq 0$.
> - Inside the commutator with $H$, $(-\nabla^2 + m^2)\phi$ may not be replaced by $-\partial_t^2\phi$: the equality is true, but a time derivative involves nearby *different* times, about which the postulates say nothing. Compute at equal times, then read off the time dependence.
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
> the mode expansion. For the Heisenberg field, which solves the equation as an operator ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]), $g(p) = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]]). (A Green's function, by contrast, lives off the shell: [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]].)
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Principle "Free fields live on the mass shell"), §6.4 · PS §2.4, eqs. (2.57)–(2.58)*

^thm-c2b-1-3

> [!derivation]- Derivation
> **Step 1** (transform). With $f(x) = \int\frac{d^4p}{(2\pi)^4}\tilde f(p)e^{-ip\cdot x}$ and $\partial^2 + m^2 \leftrightarrow m^2 - p^2$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 2), the equation becomes $(m^2 - p^2)\tilde f(p) = 0$ as generalized functions of $p$ (the derivative rule holds in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3; $f$ tempered).
>
> **Step 2** (support). Where $p^2 \ne m^2$ one may divide by the smooth nonzero factor (multiplication by the smooth function $1/(m^2 - p^2)$ on that open set, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1), so $\tilde f = 0$ there. On the shell, in the variable $s = p^2 - m^2$, the equation is $s\,T = 0$, whose solutions are multiples of $\delta(s)$: a derivative term is excluded because $s\,\delta'(s) = -\delta(s) \ne 0$. (Sense: near the shell, $(p^0, \mathbf p) \mapsto (s, \mathbf p)$ is a smooth change of variables because $\partial s/\partial p^0 = 2p^0 \ne 0$ there for $m > 0$; in the variable $s$ the distribution is supported at $s = 0$, so by [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]] it is a finite sum of derivatives of $\delta(s)$ with coefficients depending on $\mathbf p$; this is [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], 2.) So $\tilde f = 2\pi\delta(p^2 - m^2)g(p)$ for some $g$ on the shell.
>
> **Step 3** (do the $p^0$ integral). By the composition rule ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]]; as distributions, [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2, and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1), roots $p^0 = \pm E_{\mathbf p}$ with $|\partial_{p^0}(p^2 - m^2)| = 2E_{\mathbf p}$: $\delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}}$. Then
>
> $$
> f(x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl[g(E_{\mathbf p}, \mathbf p)\,e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} + g(-E_{\mathbf p}, \mathbf p)\,e^{iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x}\Bigr].
> $$
>
> **Step 4** (relabel the negative-energy term). Substitute $\mathbf p \to -\mathbf p$ there (Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in the pairing with a test function): it becomes $g(-E_{\mathbf p}, -\mathbf p)e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x} = g(-p)\,e^{ip\cdot x}$ with $p = (E_{\mathbf p}, \mathbf p)$. This is the stated formula.
>
> **Step 5** (compare with the field). Against the mode expansion of the Heisenberg field, obtained independently from the Hamiltonian in [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]] (the next theorem), $g(p)/2E_{\mathbf p} = a_{\mathbf p}/\sqrt{2E_{\mathbf p}}$, so $g(p) = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}$; reality of $f$ gives $g(-p) = \overline{g(p)}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 4), here $\sqrt{2E}\,a^\dagger_{\mathbf p}$.
>
> **What the derivation shows.**
> - The three-dimensional mode expansions are four-dimensional transforms restricted to the shell, and the invariant measure $d^3p/2E_{\mathbf p}$ is what the shell leaves behind.
> - A free field has no off-shell Fourier components; a Green's function must have them ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]]), and that is where the difficulty is.
> - Used next: the mode expansion of the Heisenberg field (Theorem §C2b.1.4), the support of homogeneous solutions in the uniqueness of $D_R$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]) and all fundamental solutions ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]).

^der-c2b-1-3

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

> [!theorem] Theorem §C2b.1.4: Time Dependence of the Modes; the Covariant Mode Expansion
> 1. The Schrödinger ladder operators acquire phases: $e^{iHt}a_{\mathbf p}e^{-iHt} = a_{\mathbf p}\,e^{-iE_{\mathbf p}t}$ and $e^{iHt}a_{\mathbf p}^\dagger e^{-iHt} = a_{\mathbf p}^\dagger\,e^{iE_{\mathbf p}t}$.
> 2. Hence, with $p^0 = E_{\mathbf p}$ (not an integration variable),
>
> $$
> \phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(a_{\mathbf p}\,e^{-ip\cdot x} + a_{\mathbf p}^\dagger\,e^{ip\cdot x}\Bigr), \qquad \pi(x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(a_{\mathbf p}\,e^{-ip\cdot x} - a_{\mathbf p}^\dagger\,e^{ip\cdot x}\Bigr) .
> $$
>
> 3. $\pi(x) = \partial_t\phi(x)$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1 · PS §2.4, eqs. (2.46)–(2.47)*

^thm-c2b-1-4

> [!derivation]- Derivation
> **Step 1** (the Hamiltonian in mode form). By [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], with the integration variable renamed $\mathbf q$ so that it cannot clash with the $\mathbf p$ of the operator being moved,
>
> $$
> H = \int\frac{d^3q}{(2\pi)^3}\,E_{\mathbf q}\,a_{\mathbf q}^\dagger a_{\mathbf q} + E_0 .
> $$
>
> ⚑ By-product: the zero-point constant $E_0$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]]) is a number, so it commutes with every operator and drops out of every commutator below; time evolution does not see it → [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]].
>
> **Step 2** (one commutator). With $[AB, C] = A[B, C] + [A, C]B$,
>
> $$
> [a_{\mathbf q}^\dagger a_{\mathbf q}, a_{\mathbf p}] = a_{\mathbf q}^\dagger\underbrace{[a_{\mathbf q}, a_{\mathbf p}]}_{=0} + [a_{\mathbf q}^\dagger, a_{\mathbf p}]\,a_{\mathbf q} = -(2\pi)^3\delta^3(\mathbf q - \mathbf p)\,a_{\mathbf q},
> $$
>
> using $[a_{\mathbf q}, a_{\mathbf p}] = 0$ and $[a_{\mathbf q}^\dagger, a_{\mathbf p}] = -[a_{\mathbf p}, a_{\mathbf q}^\dagger] = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]); the minus sign is there because this is the $a^\dagger a$ order, not the $aa^\dagger$ order that defines the normalization.
>
> **Step 3** (integrate the delta). The $\mathbf q$ integral is done by $\delta^3(\mathbf q - \mathbf p)$, which sets $\mathbf q = \mathbf p$ and $E_{\mathbf q} = E_{\mathbf p}$ (sense: $[a_{\mathbf q}^\dagger, a_{\mathbf p}]$ is an operator-valued distribution in $(\mathbf p, \mathbf q)$, [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]; for a smeared annihilator $a(g) = \int\frac{d^3p}{(2\pi)^3}g(\mathbf p)a_{\mathbf p}$, $g \in \mathcal S$, the step reads $[H, a(g)] = -a(E g)$, the delta acting on the smooth function $E_{\mathbf q}g(\mathbf q)$, [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]):
>
> $$
> [H, a_{\mathbf p}] = -\int\frac{d^3q}{(2\pi)^3}\,E_{\mathbf q}\,(2\pi)^3\delta^3(\mathbf q - \mathbf p)\,a_{\mathbf q} = -E_{\mathbf p}\,a_{\mathbf p}, \qquad\text{i.e.}\qquad Ha_{\mathbf p} = a_{\mathbf p}\,(H - E_{\mathbf p}) .
> $$
>
> **Step 4** (powers). By induction, $H^na_{\mathbf p} = a_{\mathbf p}(H - E_{\mathbf p})^n$: if it holds for $n$, then $H^{n+1}a_{\mathbf p} = H\,a_{\mathbf p}(H - E_{\mathbf p})^n = a_{\mathbf p}(H - E_{\mathbf p})^{n+1}$ by Step 3.
>
> **Step 5** (exponentiate). Summing the series term by term,
>
> $$
> e^{iHt}a_{\mathbf p} = \sum_{n=0}^\infty\frac{(it)^n}{n!}H^na_{\mathbf p} = a_{\mathbf p}\sum_{n=0}^\infty\frac{(it)^n}{n!}(H - E_{\mathbf p})^n = a_{\mathbf p}\,e^{iHt}e^{-iE_{\mathbf p}t},
> $$
>
> where $e^{i(H - E)t} = e^{iHt}e^{-iEt}$ because $E_{\mathbf p}$ is a number. Multiplying on the right by $e^{-iHt}$ gives part 1 for $a_{\mathbf p}$. (This is the Baker–Hausdorff lemma for $[G, A] = \kappa A$, [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-2|QM Theorem §C3.3.2]], exactly as for one oscillator in [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]].)
>
> **Step 6** (the adjoint). Taking the Hermitian conjugate of part 1 for $a_{\mathbf p}$, with $(e^{iHt})^\dagger = e^{-iHt}$, gives $e^{iHt}a_{\mathbf p}^\dagger e^{-iHt} = a_{\mathbf p}^\dagger e^{+iE_{\mathbf p}t}$.
>
> **Step 7** (the Schrödinger field, un-relabelled). [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] writes $\phi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(a_{\mathbf p} + a_{-\mathbf p}^\dagger)e^{i\mathbf p\cdot\mathbf x}$. In the $a^\dagger_{-\mathbf p}$ term substitute $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, valid in the pairing with a test function, i.e. after smearing in $\mathbf x$): the Jacobian is $|\det(-\mathbf 1)| = 1$, the domain $\mathbb R^3$ is unchanged, $E_{-\mathbf p} = E_{\mathbf p}$, and the exponent becomes $e^{-i\mathbf p\cdot\mathbf x}$. So
>
> $$
> \phi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(a_{\mathbf p}\,e^{i\mathbf p\cdot\mathbf x} + a_{\mathbf p}^\dagger\,e^{-i\mathbf p\cdot\mathbf x}\Bigr), \qquad \pi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(a_{\mathbf p}\,e^{i\mathbf p\cdot\mathbf x} - a_{\mathbf p}^\dagger\,e^{-i\mathbf p\cdot\mathbf x}\Bigr),
> $$
>
> the second by the same substitution in $\pi_S$.
>
> **Step 8** (conjugate term by term). $e^{iHt}$ passes through the numbers $e^{\pm i\mathbf p\cdot\mathbf x}$ and the integral (sense: smeared in $\mathbf x$ with $g \in \mathcal S(\mathbb R^3)$, the integral is $\int\frac{d^3p}{(2\pi)^3}\bigl(\tilde g(-\mathbf p)a_{\mathbf p} + \tilde g(\mathbf p)a^\dagger_{\mathbf p}\bigr)/\sqrt{2E_{\mathbf p}}$ with Schwartz coefficients, and a unitary passes through it in every matrix element), and acts on $a_{\mathbf p}$, $a_{\mathbf p}^\dagger$ by Steps 5–6:
>
> $$
> e^{iHt}\phi_S(\mathbf x)e^{-iHt} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(a_{\mathbf p}\,e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} + a_{\mathbf p}^\dagger\,e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x}\Bigr),
> $$
>
> and $-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x = -ip\cdot x$ with $p^0 = E_{\mathbf p}$. For $\pi$ only the coefficient differs, $-i\sqrt{E_{\mathbf p}/2}$ instead of $1/\sqrt{2E_{\mathbf p}}$, and the relative minus sign:
>
> $$
> e^{iHt}\pi_S(\mathbf x)e^{-iHt} = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(a_{\mathbf p}\,e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} - a_{\mathbf p}^\dagger\,e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x}\Bigr) .
> $$
>
> This is part 2.
>
> ⚑ By-product: $p^0$ in $e^{\mp ip\cdot x}$ is the function $E_{\mathbf p}$ of the integration variable, not a variable of its own; this is where the remaining non-covariance hides → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-2|Remark: What is covariant and what is not yet]].
>
> **Step 9** (differentiate). $\partial_te^{-ip\cdot x} = -iE_{\mathbf p}e^{-ip\cdot x}$ and $\partial_te^{ip\cdot x} = +iE_{\mathbf p}e^{ip\cdot x}$; differentiating under the integral (as a distribution, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]; concretely, smeared with $g \in \mathcal S(\mathbb R^3)$ the $t$-derivative brings down $\mp iE_{\mathbf p}$ against the Schwartz coefficient $\tilde g(\mp\mathbf p)$, still absolutely integrable in every wave-packet matrix element, so [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2 applies) and using $E_{\mathbf p}/\sqrt{2E_{\mathbf p}} = \sqrt{E_{\mathbf p}/2}$,
>
> $$
> \partial_t\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(-iE_{\mathbf p}\,a_{\mathbf p}e^{-ip\cdot x} + iE_{\mathbf p}\,a_{\mathbf p}^\dagger e^{ip\cdot x}\Bigr) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(a_{\mathbf p}e^{-ip\cdot x} - a_{\mathbf p}^\dagger e^{ip\cdot x}\Bigr) = \pi(x) .
> $$
>
> The sign check the lecture recommended: $\partial_t$ of the $a$ term must give $-iE_{\mathbf p}$.
>
> ⚑ By-product: $\pi = \partial_t\phi$, a definition in classical field theory and not even expressible in the Schrödinger picture, is now a theorem → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-4|Remark: Two routes that meet]].
>
> **What the derivation shows.**
> - Conjugation with $e^{iHt}$ does nothing to $a_{\mathbf p}$ but attach the phase of a positive-energy wave function; $a_{\mathbf p}$ itself stays the time-independent Schrödinger operator (PS's convention).
> - Only $[a, a^\dagger]$ and the mode form of $H$ were used; the zero-point constant never enters time evolution.
> - Used next: the two-point functions (Theorems §C2b.2.1, §C2b.4.2) and, through $\pi = \partial_t\phi$, the unequal-time commutators (Theorem §C2b.4.10).

^der-c2b-1-4

*Uses:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]], [[§C3.3 The Schrödinger and Heisenberg Pictures#^thm-c3-3-2|QM Theorem §C3.3.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!remark] Remark: What is covariant and what is not yet
> The spatial Fourier factors have become four-dimensional plane waves, the first manifestly covariant-looking expression of the quantum theory. But the integral still runs over three momenta: $p^0$ is not a variable, it means $E_{\mathbf p}$, a square root of the integration variable. The remaining non-covariance hides there, and the invariant measure $d^3p/(2\pi)^32E_{\mathbf p}$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]) is the bookkeeping that keeps it honest. In [[§C2b.5 Green's Functions and Contours|§C2b.5]], $p^0$ becomes an integration variable, and the poles at $p^0 = \pm E_{\mathbf p}$ are the price.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.1, §5.7 (closing paragraph)*

^rem-c2b-1-2

> [!theorem] Theorem §C2b.1.5: Positive and Negative Frequency
> Split $\phi = \phi^+ + \phi^-$ with
>
> $$
> \phi^+(x) = \int\frac{d^3p}{(2\pi)^3}\frac{a_{\mathbf p}\,e^{-ip\cdot x}}{\sqrt{2E_{\mathbf p}}}\quad\text{(positive frequency)}, \qquad \phi^- = (\phi^+)^\dagger\quad\text{(negative frequency)} .
> $$
>
> Then $\phi^+|0\rangle = 0$, $\langle0|\phi^- = 0$, and for the one-particle states $|\mathbf p\rangle$, with $p^0 = E_{\mathbf p} > 0$,
>
> $$
> \langle0|\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}, \qquad \langle\mathbf p|\phi(x)|0\rangle = e^{ip\cdot x} .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.3, Ch. 6 §6.7 (the split $\phi^\pm$) · PS §2.4, p. 26 · Yu §6.3, eqs. (6.132)–(6.133)*

^thm-c2b-1-5

> [!derivation]- Derivation
> **Step 1** (the vacuum). $a_{\mathbf p}|0\rangle = 0$ for every $\mathbf p$ ([[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]]), so $\phi^+(x)|0\rangle = 0$; taking adjoints, $\langle0|\phi^-(x) = 0$.
>
> **Step 2** (only $\phi^+$ contributes). $\langle0|\phi(x)|\mathbf p\rangle = \langle0|\phi^+(x)|\mathbf p\rangle + \langle0|\phi^-(x)|\mathbf p\rangle$, and the second term is zero by Step 1.
>
> **Step 3** (insert, with a new name for the field's momentum).
>
> $$
> \langle0|\phi^+(x)|\mathbf p\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E_{\mathbf q}}}\sqrt{2E_{\mathbf p}}\;\langle0|a_{\mathbf q}a_{\mathbf p}^\dagger|0\rangle .
> $$
>
> **Step 4** (reorder). $a_{\mathbf q}a_{\mathbf p}^\dagger = [a_{\mathbf q}, a_{\mathbf p}^\dagger] + a_{\mathbf p}^\dagger a_{\mathbf q}$; the second term annihilates $|0\rangle$, so $\langle0|a_{\mathbf q}a_{\mathbf p}^\dagger|0\rangle = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).
>
> **Step 5** (integrate the delta). It sets $\mathbf q = \mathbf p$, so $E_{\mathbf q} = E_{\mathbf p}$ and $q^0 = p^0$; the square roots cancel and $\langle0|\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$. (Sense: $|\mathbf p\rangle$ is not normalizable, so Steps 3–5 compute the kernel of $g \mapsto \langle0|\phi(x)|g\rangle$ for wave packets $|g\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}g(\mathbf p)|\mathbf p\rangle$, $g \in \mathcal S$, the delta acting on the smooth integrand; the result is a continuous function of $\mathbf p$, so the kernel has a value at every $\mathbf p$.)
>
> **Step 6** (the conjugate). $\phi$ is Hermitian, so $\langle\mathbf p|\phi(x)|0\rangle = \overline{\langle0|\phi(x)|\mathbf p\rangle} = e^{ip\cdot x}$.
>
> **What the derivation shows.**
> - The relativistic normalization ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]) is what makes the amplitude exactly a plane wave, with no $E_{\mathbf p}$-dependent factor; at $t = 0$ this is [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7|Theorem §C2a.4.7]].
> - Positive frequency goes with annihilation, negative frequency with creation → [[§C2b.1 Heisenberg Fields#^rem-c2b-1-3|Remark: Negative frequency is creation, not negative energy]].
> - Used next: the split $\phi^\pm$ gives normal ordering and the contraction ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]).

^der-c2b-1-5

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1|Principle §C2a.4.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]]

> [!remark] Remark: Negative frequency is creation, not negative energy
> A complete set of solutions of the Klein–Gordon equation has both $e^{-iEt}$ and $e^{+iEt}$, and a Hermitian field needs both. Read as single-particle wave functions they would be states of energy $\pm E$, the old difficulty of relativistic wave mechanics ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-2|QM Theorem §C13.1.2]]). In the field, the coefficient of the positive-frequency solution is the operator that *destroys* a quantum, and $\langle0|\phi|\mathbf p\rangle = e^{-ip\cdot x}$ is a positive-energy wave function; the coefficient of the negative-frequency solution *creates* one. No state of negative energy exists in the spectrum ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]). Wave and particle sit in one formula: the plane waves are the wave aspect, the operator coefficients with $[a, a^\dagger] = (2\pi)^3\delta^3$ the particle aspect. Notation: $\phi^{(+)}$ in PS and Yu is the positive-frequency, annihilating part, as here.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.3 · PS §2.4, p. 26*

^rem-c2b-1-3

## The field on spacetime

> [!theorem] Theorem §C2b.1.6: The Heisenberg Field Is an Operator-Valued Distribution on Spacetime
> For $f \in \mathcal S(\mathbb R^4)$ let $\phi(f) \equiv \int d^4x\,f(x)\,\phi(x)$, the spacetime version of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], and $\tilde f(p) = \int d^4x\,f(x)\,e^{ip\cdot x}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]). With $p^0 = E_{\mathbf p}$:
> 1. $\displaystyle\phi(f) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\tilde f(-p)\,a_{\mathbf p} + \tilde f(p)\,a_{\mathbf p}^\dagger\Bigr)$, and $\phi(f)|0\rangle$ is a one-particle state with $\|\phi(f)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}|\tilde f(p)|^2 < \infty$. So $\phi$ is an operator-valued tempered distribution on $\mathbb R^4$ ([[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]]); $\phi(x)$ unsmeared is not an operator.
> 2. $\phi(f)$ depends on $\tilde f$ only through its values on the mass shell $p^2 = m^2$.
> 3. The Klein–Gordon equation holds as an identity of operator-valued distributions: $\phi\bigl((\partial^2 + m^2)f\bigr) = 0$ for every $f$, which is what $(\partial^2 + m^2)\phi = 0$ means.
>
> *Source: the user's PHY 513 notes, App. A §A.4 ($\phi[\varphi] = \int d^4x\,\varphi(x)\phi(x)$), Ch. 6 §6.2 ("operator-valued distribution") · stated here for the Heisenberg field (standard: Streater & Wightman, Ch. 3; Reed & Simon II, §X.7)*

^thm-c2b-1-6

> [!derivation]- Derivation
> **Step 1** (smear term by term). Take finite-particle wave-packet states $\Psi_1$, $\Psi_2$ (Schwartz amplitudes; [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-1|§C2a.4, Caution: Plane-wave states are not normalizable]]). The matrix elements $\langle\Psi_1|a_{\mathbf p}|\Psi_2\rangle$ and $\langle\Psi_1|a_{\mathbf p}^\dagger|\Psi_2\rangle$ are Schwartz functions of $\mathbf p$, so in $\langle\Psi_1|\phi(x)|\Psi_2\rangle$, written with [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], the $\mathbf p$-integral converges absolutely for every $x$, and $\int d^4x\int d^3p\,|f(x)|\,|\langle\Psi_1|a_{\mathbf p}|\Psi_2\rangle|/\sqrt{2E_{\mathbf p}} < \infty$. Fubini therefore lets the $x$-integral go inside ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], "after smearing"):
>
> $$
> \int d^4x\,f(x)\,e^{-ip\cdot x} = \tilde f(-p), \qquad \int d^4x\,f(x)\,e^{ip\cdot x} = \tilde f(p), \qquad p^0 = E_{\mathbf p} .
> $$
>
> This is the formula of part 1, read in every such matrix element.
>
> **Step 2** (decay on the shell). $\tilde f \in \mathcal S(\mathbb R^4)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1), so $|\tilde f(k)| \le C_N(1 + |k^0| + |\mathbf k|)^{-N}$ for every $N$. On the shell $|\pm\mathbf p| = |\mathbf p|$, hence $|\tilde f(\pm E_{\mathbf p}, \pm\mathbf p)| \le C_N(1 + |\mathbf p|)^{-N}$.
>
> **Step 3** (on the vacuum). $a_{\mathbf p}|0\rangle = 0$ removes the first term: $\phi(f)|0\rangle = \int\frac{d^3p}{(2\pi)^3}\frac{\tilde f(p)}{\sqrt{2E_{\mathbf p}}}a_{\mathbf p}^\dagger|0\rangle$. With $\langle0|a_{\mathbf q}a_{\mathbf p}^\dagger|0\rangle = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]; the delta acts on the Schwartz coefficient as in [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]]),
>
> $$
> \|\phi(f)|0\rangle\|^2 = \int\frac{d^3q\,d^3p}{(2\pi)^6}\frac{\overline{\tilde f(q)}\,\tilde f(p)}{\sqrt{2E_{\mathbf q}\,2E_{\mathbf p}}}(2\pi)^3\delta^3(\mathbf q - \mathbf p) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,|\tilde f(p)|^2,
> $$
>
> finite by Step 2 with $N = 2$: $1/2E_{\mathbf p} \le 1/2|\mathbf p|$ is integrable near $\mathbf p = 0$ in three dimensions (so $m = 0$ is included).
>
> ⚑ By-product: concentrating $f$ at one point, $\tilde f(p) \to e^{ip\cdot x}$, turns the norm into $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \infty$, the divergence of Step 6 of Derivation §C2b.2.1: $\phi(x)|0\rangle$ is not a vector, and the vacuum two-point function needs the same smearing → [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]].
>
> **Step 4** (only the shell). By Step 1, $\phi(f)$ involves $\tilde f$ only at the points $(\pm E_{\mathbf p}, \pm\mathbf p)$. This is part 2.
>
> **Step 5** (the field equation). The derivative rule in $\mathcal S$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 2; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3) gives $\widetilde{(\partial^2 + m^2)f}(k) = (m^2 - k^2)\tilde f(k)$, which vanishes on the shell. By Step 4, $\phi\bigl((\partial^2 + m^2)f\bigr) = 0$. The derivative of an operator-valued distribution is defined by moving it onto the test function ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), two derivatives with sign $(-1)^2 = 1$: $\bigl((\partial^2 + m^2)\phi\bigr)(f) \equiv \phi\bigl((\partial^2 + m^2)f\bigr) = 0$. This is part 3.
>
> **What the derivation shows.**
> - Smearing in time as well as in space turns the mode integral into an absolutely convergent one in every matrix element; the decay comes from $\tilde f$ on the shell.
> - Part 3 is the distributional content of the operator equation of Theorem §C2b.1.2: the free field ignores every off-shell component of a test function.
> - Used next: the vacuum two-point function as a distribution (Theorem §C2b.2.2), unequal-time commutators (Theorem §C2b.4.11) and the particle number produced by a source (Theorem §C2b.8.4).

^der-c2b-1-6

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]], [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!remark] Remark: Two routes that meet
> Theorem §C2b.1.2 never used the mode expansion. One could start from it: postulate the commutators and $H$, derive the Klein–Gordon equation, expand its solutions in $e^{\mp ip\cdot x}$ (they live on the mass shell, [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]), name the coefficients $a_{\mathbf p}$, $a_{\mathbf p}^\dagger$, and compute their algebra. That is the "field first" route of Yu §2.3 and of the user's notes; the lecture went "oscillators first", diagonalizing $H$ and discovering afterwards that the result solves a wave equation ([[P1 Canonical Quantization|P1]]). That the two routes meet is Theorem §C2b.1.4 against Theorem §C2b.1.2. Level change: QM's preview asserted the operator Klein–Gordon equation for the mode sum it wrote down ([[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^thm-c13-1-6|QM Theorem §C13.1.6]], 1); here it follows from the canonical structure alone, and $\pi = \partial_t\phi$, a definition in classical field theory, becomes a consequence of the commutators.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.2 ("The logic run backwards")*

^rem-c2b-1-4

> [!remark]- Connections
> - [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]] is the time component of a four-dimensional statement, $\phi(x) = e^{iP\cdot x}\phi(0)e^{-iP\cdot x}$, equivalently $[\phi, P^\mu] = i\partial^\mu\phi$: translation invariance on the Hilbert space — [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-9|Theorem §C3.5.9]].
> - Theorem §C2b.1.4 is the field version of the oscillator in the Heisenberg picture, $a(t) = ae^{-i\omega t}$: [[§C3.4 The Harmonic Oscillator and Coherent States Revisited#^thm-c3-4-2|QM Theorem §C3.4.2]]; the same phase makes a coherent state stay coherent in [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5|Theorem §C2a.6.5]].
> - The Heisenberg field is the operator whose vacuum correlations are the two-point functions: the Wightman function is built from it in [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], and its commutator at unequal times is the commutator function of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]; the positive- and negative-frequency parts of [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]] are what normal ordering and contractions separate — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]].
> - A free field has its Fourier transform on the mass shell ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]), while a Green's function must have off-shell components ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]]): the pole problem of [[§C2b.5 Green's Functions and Contours|§C2b.5]] is the clash of the two. [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]] and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] (homogeneous solutions, composition of δ) give the on-shell form.
> - [[§CA.2 Generalized Functions#^def-ca-2-8|Def. §CA.2.8]] (operator-valued distributions) is what the Heisenberg field is: Theorem §C2b.1.6 smears it over spacetime, the four-dimensional version of the time-slice smearing of [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]].
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]] (the transform maps $\mathcal S$ to $\mathcal S$) supplies the on-shell decay of $\tilde f$ that makes $\phi(f)|0\rangle$ normalizable; the same decay makes the particle number of a source finite ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-4|Theorem §C2b.8.4]]).
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]] (exchanging the $x$- and $p$-integrals) is the step that turns the formal mode expansion into $\phi(f)$, valid because the coefficients are smeared.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] (relabelling $\mathbf p \to -\mathbf p$) rewrites the Schrödinger field in Step 7 of Derivation §C2b.1.4.
> - [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]] (derivatives moved onto the test function) and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-8|Theorem §CA.3.8]] (integration by parts against δ) give $\partial_t\phi = \pi$ and the $\nabla^2\phi$ of the Heisenberg equations; [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]] licenses the $t$-derivative under the smeared mode integral.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]] (derivative rule) turns the Klein–Gordon equation into "the field ignores off-shell test functions", Theorem §C2b.1.6, 3.
