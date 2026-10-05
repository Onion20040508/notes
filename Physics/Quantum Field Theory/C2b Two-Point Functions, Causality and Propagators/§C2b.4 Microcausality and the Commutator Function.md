---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.4
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.3 Explicit Forms of the Wightman Function]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.5 Green's Functions and Contours]] →

*Sources: the user's PHY 513 notes, Ch. 5 §§5.5, 5.7, App. A §A.5, Ch. 6 §§6.1, 6.11 · PHY 513 Lecture 5 (Larsen, 16 Sep 2026; no slides, reconstructed in the user's notes) · Peskin & Schroeder §2.4, pp. 28–29 · PHY 513, Problem Set 4, Problems 2 and 3(b).*

Is the theory causal? Microcausality asks that observables at spacelike separation commute; for the free field the commutator is a $c$-number, the antisymmetric part of the Wightman function of [[§C2b.2 The Wightman Function|§C2b.2]], and it vanishes outside the light cone. The section then follows the commutator to unequal times: the commutator function carries the equal-time relations of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]] to all times and propagates the field. The Green's functions of [[§C2b.5 Green's Functions and Contours|§C2b.5]] are built from it.

*Conventions* ([[Larsen PHY 513]]): $\hbar = c = 1$, $g = \operatorname{diag}(+, -, -, -)$, $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ whenever $p$ is on shell, $[a_{\mathbf p}, a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}^\dagger|0\rangle$. Lecture 5 writes $\omega_{\mathbf p}$ for $E_{\mathbf p}$ ([[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution: Eₚ, not ωₚ; π, not Π]]). Unless stated otherwise $m > 0$; the massless case is stated separately where it differs.

## Microcausality and the commutator function

> [!principle] Principle §C2b.4.1: Microcausality
> Local observables at spacelike separation commute:
>
> $$
> [\mathcal O_1(x), \mathcal O_2(y)] = 0 \qquad \text{for } (x - y)^2 < 0 .
> $$
>
> When the local observables are built from $\phi$ and its derivatives, it suffices that $[\phi(x), \phi(y)] = 0$ for $(x - y)^2 < 0$ (for a complex field also $[\phi(x), \phi^\dagger(y)] = 0$).
>
> *Domain:* relativistic quantum field theory, free or interacting (with interactions it is the locality axiom; its classical counterpart is the locality of the action, [[§C1.8 Scalar Field Theory꞉ Fields, Locality and Symmetry#^pr-c1-8-4|Principle §C1.8.4]]).
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 (Principle "The causality condition") · PS §2.4, p. 28*

^pr-c2b-4-1

> [!remark] Remark: Why the criterion is a commutator, not an amplitude
> Spacelike-separated events have no invariant order ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§B1.3 Causal Structure and Proper Time#^rem-b1-3-2|REL Remark: Causality as a statement about cones]]), so neither may influence the other: measurements there must be compatible, which in quantum mechanics means commuting operators. An *amplitude* to propagate outside the cone, such as $D_W \neq 0$ (Theorem §C2b.3.3) or the single-particle amplitude of [[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-7|Theorem §C1.3.7]], is not a signal. The condition is an operator identity, true in every state, not a vacuum expectation value. Derivatives pass through commutators and $[AB, C] = A[B, C] + [A, C]B$, which is why the field commutator suffices. Microcausality is a principle: the free field satisfies it as a theorem (Theorem §C2b.4.5), an interacting theory must be built so that it does.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 · PS §2.4, p. 28*

^rem-c2b-4-1

> [!definition] Definition §C2b.4.1: Commutator Function; Hadamard Function
> The **commutator function** $D$ (Pauli–Jordan function) and the **Hadamard function** $D_1$ are
>
> $$
> iD(x - y) \equiv \langle0|[\phi(x), \phi(y)]|0\rangle, \qquad D_1(x - y) \equiv \langle0|\{\phi(x), \phi(y)\}|0\rangle .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 · PHY 513, Problem Set 4, eqs. (9)–(10)*

^def-c2b-4-1

> [!caution] Caution: One letter, four objects
> PS's $D(x - y)$ is the Wightman function $D_W$ here, and PS name neither $D$ nor $D_1$. Yu calls the commutator itself the Pauli–Jordan function, $D_{\mathrm{PJ}}(x - y) \equiv [\phi(x), \phi(y)]$ (Yu eq. (6.111)), so $D_{\mathrm{PJ}} = iD$. The Lecture 6 slides write a bare $D(x - y)$ for a generic Green's function, which is $D_C$ here ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]]). The names here follow Problem Set 4.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 ("Correspondence with Yu"), Ch. 6 §6.1 (Notation)*

^cau-c2b-4-1

> [!theorem] Theorem §C2b.4.2: The Field Commutator Is a c-Number
> $$
> [\phi(x), \phi(y)] = D_W(x - y) - D_W(y - x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl(e^{-ip\cdot(x - y)} - e^{ip\cdot(x - y)}\Bigr)\,\mathbf 1 = iD(x - y)\,\mathbf 1 :
> $$
>
> the same number in every state; $iD = [\phi, \phi]$ holds as an operator identity.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 (Derivation "The commutator function") · PS §2.4, eq. (2.53)*

^thm-c2b-4-2

> [!derivation]- Derivation
> **Step 1** (two names). Insert [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]] (read smeared, $[\phi(f), \phi(g)]$ for test functions $f$, $g$: [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]) with momenta $\mathbf p$ for $\phi(x)$ and $\mathbf q$ for $\phi(y)$; the commutator of the products of brackets is the sum of four commutators, each with its exponentials:
>
> $$
> [\phi(x), \phi(y)] = \int\frac{d^3p\,d^3q}{(2\pi)^6\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}\Bigl([a_{\mathbf p}, a_{\mathbf q}]e^{-ip\cdot x - iq\cdot y} + [a_{\mathbf p}, a_{\mathbf q}^\dagger]e^{-ip\cdot x + iq\cdot y} + [a_{\mathbf p}^\dagger, a_{\mathbf q}]e^{ip\cdot x - iq\cdot y} + [a_{\mathbf p}^\dagger, a_{\mathbf q}^\dagger]e^{ip\cdot x + iq\cdot y}\Bigr).
> $$
>
> **Step 2** (the four commutators, [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]). $[a_{\mathbf p}, a_{\mathbf q}] = 0$; $[a_{\mathbf p}^\dagger, a_{\mathbf q}^\dagger] = 0$; $[a_{\mathbf p}, a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$; $[a_{\mathbf p}^\dagger, a_{\mathbf q}] = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$.
>
> **Step 3** (integrate the deltas). Both surviving terms set $\mathbf q = \mathbf p$ (the deltas act on the Schwartz coefficients $\tilde f(\mp p)\tilde g(\pm q)$ of the smeared form, as in Step 1 of Derivation §C2b.2.2), so $q^0 = p^0$ and the square roots give $1/2E_{\mathbf p}$: the second term becomes $e^{-ip\cdot(x - y)}$ and the third $-e^{ip\cdot(x - y)}$, which is the formula. By [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], $\int\frac{d^3p}{(2\pi)^32E}e^{ip\cdot\xi} = \int\frac{d^3p}{(2\pi)^32E}e^{-ip\cdot(-\xi)} = D_W(-\xi)$, with no relabelling needed.
>
> **Step 4** (a number). No operator is left: the commutator is a multiple of $\mathbf 1$, so its expectation value in any normalized state is itself, and in particular $\langle0|[\phi(x), \phi(y)]|0\rangle = [\phi(x), \phi(y)]$.
>
> ⚑ By-product: the commutator does not depend on the state; with it, causality and the retarded response belong to the dynamics, not to the state → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-6|★ Remark: Other states]].
>
> **What the derivation shows.**
> - Only the oscillator algebra was used.
> - The two terms are the two orderings, "create at $y$, annihilate at $x$" minus the reverse → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|Remark: Two orderings that cancel]].
> - Used next: Theorems §C2b.4.3–§C2b.4.5 and the retarded Green's function ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]]).

^der-c2b-4-2

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]

> [!theorem] Theorem §C2b.4.3: The Commutator and Hadamard Functions Are the Parts of the Wightman Function
> With $\xi = x - y$:
> 1. $D = 2\operatorname{Im}D_W$ and $D_1 = 2\operatorname{Re}D_W$, so $D_W(\pm\xi) = \tfrac12\bigl(D_1(\xi) \pm iD(\xi)\bigr)$; $D$ and $D_1$ are real, $D$ odd and $D_1$ even in $\xi$.
> 2. $\displaystyle D(\xi) = -\int\frac{d^3p}{(2\pi)^3}\,\frac{\sin(p\cdot\xi)}{E_{\mathbf p}}$ and $\displaystyle D_1(\xi) = \int\frac{d^3p}{(2\pi)^3}\,\frac{\cos(p\cdot\xi)}{E_{\mathbf p}}$; both solve the homogeneous Klein–Gordon equation.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 (Derivation "Both are parts of the Wightman function") · PHY 513, Problem Set 4, Problem 2*

^thm-c2b-4-3

> [!derivation]- Derivation
> **Step 1** ($D$). By [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]] and [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], 2, $iD(\xi) = D_W(\xi) - D_W(-\xi) = D_W(\xi) - \overline{D_W(\xi)} = 2i\operatorname{Im}D_W(\xi)$, so $D = 2\operatorname{Im}D_W$, real.
>
> **Step 2** ($D_1$). $\{\phi(x), \phi(y)\} = \phi(x)\phi(y) + \phi(y)\phi(x)$, so $D_1 = D_W(\xi) + D_W(-\xi) = D_W + \overline{D_W} = 2\operatorname{Re}D_W$, real.
>
> **Step 3** (inverting). Adding and subtracting Steps 1–2: $D_W(\xi) = \frac12(D_1 + iD)$, and $D_W(-\xi) = \overline{D_W(\xi)} = \frac12(D_1 - iD)$.
>
> **Step 4** (parity). Exchanging $x$ and $y$ reverses the commutator and preserves the anticommutator: $iD(-\xi) = \langle[\phi(y), \phi(x)]\rangle = -iD(\xi)$ and $D_1(-\xi) = D_1(\xi)$.
>
> **Step 5** (mode integrals; identities in $\mathcal S'$ with the $\xi$-integral done first, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 2). In Theorem §C2b.4.2's integrand, $e^{-i\theta} - e^{i\theta} = -2i\sin\theta$ with $\theta = p\cdot\xi$: $iD = \int\frac{d^3p}{(2\pi)^32E}(-2i\sin p\cdot\xi)$, so $D = -\int\frac{d^3p}{(2\pi)^3}\frac{\sin p\cdot\xi}{E}$. For $D_1$, $e^{-i\theta} + e^{i\theta} = 2\cos\theta$. Every mode is on shell, so both solve $(\partial^2 + m^2)f = 0$ (Theorem §C2b.2.4, 1).
>
> ⚑ By-product: $D_1$ is a vacuum expectation value of an operator ($\{\phi, \phi\}$ is not a $c$-number), so unlike $D$ it depends on the state → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-6|★ Remark: Other states]]; it is the covariance of the vacuum fluctuations → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|Remark: Influence and correlation]].
>
> **What the derivation shows.**
> - Microcausality ($D = 0$) is equivalent to the reality of $D_W$ (used in Theorem §C2b.4.5, second route).
> - Both $D$ and $D_1$ are homogeneous solutions, not Green's functions; Green's functions are built from them with step functions ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-6|Theorem §C2b.7.6]]).

^der-c2b-4-3

*Uses:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]

> [!theorem] Theorem §C2b.4.4: The Commutator and Hadamard Functions as Distributions
> 1. $iD(\xi) = D_W(\xi) - D_W(-\xi)$ and $D_1(\xi) = D_W(\xi) + D_W(-\xi)$ hold in $\mathcal S'(\mathbb R^4)$; $D$ and $D_1$ are real tempered distributions ($\overline T[f] \equiv \overline{T[\bar f]}$), with transforms $\tilde D = -2\pi i\operatorname{sgn}(p^0)\,\delta(p^2 - m^2)$ and $\tilde D_1 = 2\pi\,\delta(p^2 - m^2)$.
> 2. They act as $D[f] = -i\displaystyle\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\bigl(\tilde f(-p) - \tilde f(p)\bigr)$ and $D_1[f] = \displaystyle\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\bigl(\tilde f(-p) + \tilde f(p)\bigr)$, $p^0 = E_{\mathbf p}$.
> 3. Both solve $(\partial^2 + m^2)T = 0$ in $\mathcal S'$, both have the light cone as singular support, and both are smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$, with spatial transforms $-\sin(E_{\mathbf p}t)/E_{\mathbf p}$ and $\cos(E_{\mathbf p}t)/E_{\mathbf p}$ at $\xi^0 = t$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5, §5.7 · PHY 513, Problem Set 4, Problem 2 · stated here as distributions*

^thm-c2b-4-4

> [!derivation]- Derivation
> **Step 1** (as distributions). By [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]] read smeared, $[\phi(f), \phi(g)]$ has the kernel $D_W(x - y) - D_W(y - x)$, and $\{\phi(f), \phi(g)\}$ the kernel $D_W(x - y) + D_W(y - x)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 1). The reflected distribution $D_W(-\cdot)[f] \equiv D_W[f(-\cdot)]$ ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]) is tempered, so $iD$ and $D_1$ are.
>
> **Step 2** (the actions). $D_W[f] = \int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}\tilde f(-p)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 2); since $\widetilde{f(-\cdot)}(k) = \tilde f(-k)$, $D_W(-\cdot)[f] = \int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}\tilde f(p)$. Subtracting and dividing by $i$, and adding, gives part 2.
>
> **Step 3** (reality). $\overline{D_W[\bar f]} = D_W(-\cdot)[f]$ (Theorem §C2b.2.4, 2 as distributions). So $\overline{iD[\bar f]} = D_W(-\cdot)[f] - D_W[f] = -iD[f]$, i.e. $\overline{D[\bar f]} = D[f]$; the same computation gives $\overline{D_1[\bar f]} = D_1[f]$.
>
> **Step 4** (transforms). Reflection $\xi \to -\xi$ reflects the transform ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]): $D_W(-\xi)$ has transform $2\pi\theta(-p^0)\delta(p^2 - m^2)$. Hence $\widetilde{iD} = 2\pi[\theta(p^0) - \theta(-p^0)]\delta(p^2 - m^2) = 2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$, so $\tilde D = -2\pi i\operatorname{sgn}(p^0)\delta(p^2 - m^2)$; and $\tilde D_1 = 2\pi[\theta(p^0) + \theta(-p^0)]\delta(p^2 - m^2) = 2\pi\delta(p^2 - m^2)$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1).
>
> **Step 5** (homogeneous). $(m^2 - p^2)$ is a smooth function, so it may multiply these distributions ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1), and it vanishes where they are supported: $(m^2 - p^2)\tilde D = (m^2 - p^2)\tilde D_1 = 0$. By the derivative rule in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3), $(\partial^2 + m^2)D = (\partial^2 + m^2)D_1 = 0$.
>
> **Step 6** (singular support, [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]). $D_W(-\xi)$ has the reflected singular support, the same cone ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 2). Near a point of the cone, by Theorem §C2b.3.6, 3, $D = 2\operatorname{Im}D_W$ contains $-\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2)$ plus a locally integrable function, and $D_1 = 2\operatorname{Re}D_W$ contains $-\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$ plus a locally integrable function; neither $\delta(\xi^2)$ nor $\mathcal P\frac{1}{\xi^2}$ (which grows like $1/\operatorname{dist}$ from the cone, not integrable across it) is a function there. Off the cone both are smooth (Theorem §C2b.3.6, 1).
>
> **Step 7** (fixed time). By [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3, $D_W(t, \cdot)$ has spatial transform $e^{-iE_{\mathbf p}t}/2E_{\mathbf p}$. For $D_W(-\xi)$ at $\xi^0 = t$: $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}e^{iE_{\mathbf p}t - i\mathbf p\cdot\boldsymbol\xi}$, and the relabelling $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1) gives the spatial transform $e^{iE_{\mathbf p}t}/2E_{\mathbf p}$. Then $\frac{e^{-iEt} - e^{iEt}}{2E} = -i\frac{\sin Et}{E}$ gives $-\sin(Et)/E$ for $D$, and $\frac{e^{-iEt} + e^{iEt}}{2E} = \frac{\cos Et}{E}$ for $D_1$; both are smooth in $t$ with every $t$-derivative polynomially bounded in $\mathbf p$.
>
> **What the derivation shows.**
> - The sine and cosine integrals of Theorem §C2b.4.3 converge for no $\xi$; they are the actions of part 2, $\xi$-integral first.
> - $D$ and $D_1$ inherit everything from $D_W$: a shell transform, a cone of singularities, smoothness in time. The last is what gives meaning to equal-time values ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]) and to products with $\theta(\xi^0)$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]).

^der-c2b-4-4

*Uses:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]

> [!theorem] Theorem §C2b.4.5: The Free Field Is Microcausal
> $D(\xi) = 0$ for $\xi^2 < 0$: the free field satisfies [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]. Inside the light cone $D$ does not vanish identically.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 · PS §2.4, eq. (2.53), Fig. 2.4*

^thm-c2b-4-5

> [!derivation]- Derivation
> **Steps 1–3** (a Lorentz transformation that reverses $\xi$). Let $\xi^2 < 0$. By [[§C1.4 The Lorentz Group#^thm-c1-4-5|Theorem §C1.4.5]], 3, there is $\Lambda \in SO^+(1,3)$ with $\Lambda\xi = -\xi$. Its construction there: boost and rotate $\xi$ to $(0, \boldsymbol\eta)$ with $|\boldsymbol\eta| = \sqrt{-\xi^2}$ (the velocity $\xi^0/|\boldsymbol\xi|$ is less than $1$ because $\xi$ is spacelike), rotate by $\pi$ about an axis perpendicular to $\boldsymbol\eta$, and conjugate back. (In 1+1 dimensions there is no such rotation and parity is needed instead; see the remark on orbits in §C1.4.)
>
> **Step 4** (conclude). By [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], $D_W(-\xi) = D_W(\Lambda\xi) = D_W(\xi)$, so $iD(\xi) = D_W(\xi) - D_W(-\xi) = 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]). (Pointwise use of invariance is legitimate here: at spacelike $\xi$, $D_W$ is a continuous function, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1, and invariant pointwise there, Theorem §C2b.2.3.) Concretely, at equal times both terms are $D_W(r)$ of [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]].
>
> **Step 5** (inside the cone). For $\xi^2 > 0$ every $\Lambda \in SO^+(1,3)$ preserves $\operatorname{sgn}\xi^0$ ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]), so Steps 1–3 are impossible, and indeed by [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]] and [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], $D = 2\operatorname{Im}D_W = \operatorname{sgn}(\xi^0)\,mJ_1(m\tau)/4\pi\tau$, which vanishes only on the isolated hyperbolas where $J_1(m\tau) = 0$.
>
> **What the derivation shows.**
> - The orbit structure of the Lorentz group places the boundary between "commute" and "do not commute" exactly on the light cone.
> - Each Wightman function separately is nonzero outside the cone; only their difference vanishes.
> - Used next: time ordering is frame-independent ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]]); the retarded function is supported in the forward cone ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]]).

^der-c2b-4-5

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§C1.4 The Lorentz Group#^thm-c1-4-5|Theorem §C1.4.5]]

> [!derivation]- Derivation (second route: causality is the reality of the Wightman function)
> **Step 1.** By [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], $[\phi(x), \phi(y)] = 2i\operatorname{Im}D_W(\xi)$: microcausality says exactly that $D_W$ is real at spacelike separation.
>
> **Step 2.** By [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], Steps 1–3, there (where $D_W$ is a function, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1) the boundary value of $W$ is approached from a region where $s^2 = \boldsymbol\xi^2 - z^2$ tends to a positive number, and $K_1$ of a positive argument is real. So $D = 0$.
>
> **Step 3.** Inside the cone the two signs of $\xi^0$ approach the cut of $s$ from opposite sides (Theorem §C2b.3.4, Step 1); the values are complex conjugates, and the commutator is the discontinuity of one analytic function across its cut.
>
> **What the derivation shows.**
> - In this language causality is not a cancellation to be checked but a property of analyticity: $D_W$, as a function of $\xi^2$, has its cut only along the timelike axis.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 ("Causality is the reality of $D_W$")*

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]

> [!theorem] Theorem §C2b.4.6: Microcausality as a Support Statement
> 1. $D$ vanishes as a distribution on the open spacelike region ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]): $\operatorname{supp}D \subseteq \{\xi : \xi^2 \ge 0\}$, the closed light cone. For $m = 0$, $\operatorname{supp}D$ is the cone surface $\xi^2 = 0$; for $m > 0$ it is the whole closed cone.
> 2. Equivalently, for real $f, g \in \mathcal D(\mathbb R^4)$ whose supports are spacelike separated ($(x - y)^2 < 0$ for all $x \in \operatorname{supp}f$, $y \in \operatorname{supp}g$), $[\phi(f), \phi(g)] = 0$. This is the precise form of [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]] for the free field: field operators smeared over spacelike-separated regions commute.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5, App. A §A.4 (smeared operators) · stated here as a support statement (standard: Streater & Wightman, Ch. 3, locality axiom)*

^thm-c2b-4-6

> [!derivation]- Derivation
> **Step 1** (the open spacelike region). On $\{\xi^2 < 0\}$, $D_W$ is a continuous function ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 1), so $D = 2\operatorname{Im}D_W$ is the continuous function $2\operatorname{Im}D_W(\xi)$ there ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]]), which is $0$ by [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]. So $D[h] = 0$ for every $h \in \mathcal D$ supported in that open set: $D$ vanishes there, and its support lies in the complement, $\xi^2 \ge 0$.
>
> **Step 2** (smeared fields). By [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]] and the kernel form ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 1), $[\phi(f), \phi(g)] = i\int d^4x\,d^4y\,f(x)g(y)D(x - y) = iD[h]$ with $h(\xi) = \int d^4y\,f(\xi + y)g(y)$ ([[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]). $h(\xi) \ne 0$ requires $\xi + y \in \operatorname{supp}f$ for some $y \in \operatorname{supp}g$, so $\operatorname{supp}h \subseteq \{x - y\}$, a compact set of spacelike vectors. By Step 1, $D[h] = 0$. Conversely, if $[\phi(f), \phi(g)] = 0$ for all such pairs, every $h \in \mathcal D$ supported in the spacelike region can be approximated by sums of such convolutions, and $D$ vanishes there.
>
> **Step 3** (the support exactly). For $m = 0$, $D = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]]), a measure on the cone surface that is nonzero near each of its points. For $m > 0$ the tail $\operatorname{sgn}(\xi^0)mJ_1(m\tau)/4\pi\tau$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]) is nonzero except on the hyperbolas $J_1(m\tau) = 0$, a set with empty interior, so the closure of where $D \ne 0$ is the whole closed cone.
>
> **What the derivation shows.**
> - Microcausality is not a statement about values at points, which $D$ does not have on the cone, but about where the distribution vanishes.
> - The commutator is a $c$-number, so "vanishes" holds as an operator identity, in every state.
> - Used next: the support of the retarded function and its uniqueness ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]]), the domain of dependence ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]]).

^der-c2b-4-6

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]

> [!remark] Remark: Two orderings that cancel; why antiparticles must exist
> The commutator contains an $aa^\dagger$ term, creating at $y$ and annihilating at $x$, and an $a^\dagger a$ term, creating at $x$ and annihilating at $y$. At spacelike separation observers disagree on which point comes first; the theory includes both amplitudes, and they cancel (for the single-particle amplitude, forward plus backward propagation is causal: [[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-9|Theorem §C1.3.9]]). For a complex field ([[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]) the two terms are visibly different:
>
> $$
> [\phi(x), \phi^\dagger(y)] = \underbrace{D_W(x - y)}_{\text{particle } y \to x\ (a,\,a^\dagger)} - \underbrace{D_W(y - x)}_{\text{antiparticle } x \to y\ (b^\dagger,\,b)} = 0 \qquad ((x - y)^2 < 0) .
> $$
>
> The cancellation needs both species, with the same mass: causality requires every particle to have an antiparticle with opposite charge (for the real field, itself). This is the honest content of "antiparticles are particles moving backwards in time"; the lecture's advice was not to be too disturbed by such narrations of the second term.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 (Caution "What the cancellation means, and what it does not") · PS §2.4, p. 29*

^rem-c2b-4-2

> [!remark] Remark: Influence and correlation
> At spacelike separation $D = 0$ but, by Theorem §C2b.3.3,
>
> $$
> D_1(\xi) = 2D_W(\xi) = \frac{m}{2\pi^2r}K_1(mr) \simeq \sqrt{\frac{m}{8\pi^3}}\;r^{-3/2}e^{-mr} \qquad (\xi^2 = -r^2,\ mr \gg 1).
> $$
>
> The two functions answer different questions. $D$ measures *influence*: a disturbance at $y$ changes what is measured at $x$ only through the commutator (made precise by the retarded response, [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-4|§C2b.5, Remark: Measurable response is a retarded commutator]]). $D_1$ measures *correlation*: it is the covariance of the vacuum fluctuations at the two points. Outside the cone the vacuum is correlated over the Compton length, yet nothing done at one point can affect the other, the field-theory version of correlation without signalling for entangled systems ([[§C11.3 Composite Systems and Reduced Density Matrices#^thm-c11-3-5|QM Theorem §C11.3.5]]); it is also why the vacuum restricted to a region is a mixed state.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.5 ("At spacelike separation: correlated, not causally connected") · PHY 513, Problem Set 4, Problem 3(b)*

^rem-c2b-4-3

> [!theorem] Theorem §C2b.4.7: Commutator and Hadamard Functions of the Massless Field
> For $m = 0$, with $t = \xi^0$ and $r = |\boldsymbol\xi| > 0$,
>
> $$
> D(\xi) = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\,\delta(\xi^2) = -\frac{1}{4\pi r}\bigl[\delta(t - r) - \delta(t + r)\bigr], \qquad D_1(\xi) = -\frac{1}{2\pi^2}\,\mathcal P\frac{1}{\xi^2} :
> $$
>
> the commutator lives on the light cone only. Both are identities in $\mathcal S'(\mathbb R^4)$ ([[§CA.2 Generalized Functions#^thm-ca-2-13|Theorem §CA.2.13]]): $D$ acts as $f \mapsto -\frac{1}{4\pi}\int d^3\xi\,\bigl[f(r, \boldsymbol\xi) - f(-r, \boldsymbol\xi)\bigr]/r$, and $\mathcal P\frac{1}{\xi^2}$ is the real part of the light-cone boundary value.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 (Derivation "Explicit forms", massless), App. A §A.5 (Caution "What the formula does and does not say", example) · PHY 513, Problem Set 4, Problem 2(b)*

^thm-c2b-4-7

> [!derivation]- Derivation
> **Step 1** (the massless Wightman function). For $m = 0$, Theorem §C2b.3.5 is exact: $D_W = -\frac{1}{4\pi^2}\,\frac{1}{(t - i\varepsilon)^2 - r^2}$.
>
> **Step 2** (partial fractions in $t$). $(t - i\varepsilon)^2 - r^2 = (t - i\varepsilon - r)(t - i\varepsilon + r)$ and $\frac{1}{(a - r)(a + r)} = \frac{1}{2r}\bigl[\frac{1}{a - r} - \frac{1}{a + r}\bigr]$ (check: the numerator is $(a + r) - (a - r) = 2r$). So
>
> $$
> D_W = -\frac{1}{8\pi^2r}\Bigl[\frac{1}{t - r - i\varepsilon} - \frac{1}{t + r - i\varepsilon}\Bigr].
> $$
>
> **Step 3** (Sokhotski–Plemelj; sense: as distributions in $t$ at fixed $r > 0$, then integrated against test functions over $\boldsymbol\xi$ with $d^3\xi = r^2dr\,d\Omega$, where the prefactor $1/r$ is integrable, so the identity holds in $\mathcal S'(\mathbb R^4)$ including $r = 0$; this is [[§CA.2 Generalized Functions#^thm-ca-2-13|Theorem §CA.2.13]], 1–2). As generalized functions of $t$ at fixed $r > 0$, $\frac{1}{s - i\varepsilon} \to \mathcal P\frac1s + i\pi\delta(s)$ with $s = t \mp r$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]):
>
> $$
> D_W = -\frac{1}{8\pi^2r}\Bigl[\mathcal P\frac{1}{t - r} - \mathcal P\frac{1}{t + r}\Bigr] - \frac{i\pi}{8\pi^2r}\bigl[\delta(t - r) - \delta(t + r)\bigr].
> $$
>
> **Step 4** (imaginary part). $\operatorname{Im}D_W = -\frac{1}{8\pi r}[\delta(t - r) - \delta(t + r)]$, and $D = 2\operatorname{Im}D_W$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]]) $= -\frac{1}{4\pi r}[\delta(t - r) - \delta(t + r)]$.
>
> **Step 5** (covariant form). $\delta(t^2 - r^2)$ has roots $t = \pm r$ with $|\partial_t(t^2 - r^2)| = 2r$, so $\delta(t^2 - r^2) = \frac{\delta(t - r) + \delta(t + r)}{2r}$ ([[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]]; as a distributional limit, [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2, and on $\mathbb R^4$ the Lorentz-invariant $\operatorname{sgn}(x^0)\delta(x^2)$ of [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, acting as $f \mapsto \int d^3x\,[f(r, \mathbf x) - f(-r, \mathbf x)]/2r$) and $\operatorname{sgn}(t)\delta(t^2 - r^2) = \frac{\delta(t - r) - \delta(t + r)}{2r}$. Hence $D = -\frac{1}{2\pi}\operatorname{sgn}(t)\delta(\xi^2)$.
>
> **Step 6** (real part). $\mathcal P\frac{1}{t - r} - \mathcal P\frac{1}{t + r} = \mathcal P\frac{2r}{t^2 - r^2}$ (the definition of $\mathcal P\frac{1}{x^2}$ in [[§CA.2 Generalized Functions#^thm-ca-2-13|Theorem §CA.2.13]], 2), so $\operatorname{Re}D_W = -\frac{1}{4\pi^2}\mathcal P\frac{1}{t^2 - r^2}$ and $D_1 = 2\operatorname{Re}D_W = -\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$.
>
> **What the derivation shows.**
> - $D$ vanishes outside the cone (microcausality) *and* strictly inside it: Huygens' principle → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-4|Remark: Sharp and blurred propagation]].
> - The $i\varepsilon$ of the boundary value decides the sign of the delta terms; the principal value is the correlation part.
> - Used next: the light-cone part of the massive function (Theorem §C2b.4.8) and the massless retarded function ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]]).

^der-c2b-4-7

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]]

> [!theorem] Theorem §C2b.4.8: Commutator and Hadamard Functions of the Massive Field
> For $m > 0$, with $\tau = \sqrt{\xi^2}$ inside the cone and $r = \sqrt{-\xi^2}$ outside:
> - inside: $D = \operatorname{sgn}(\xi^0)\dfrac{m\,J_1(m\tau)}{4\pi\tau}$, $D_1 = \dfrac{m\,Y_1(m\tau)}{4\pi\tau}$; outside: $D = 0$, $D_1 = \dfrac{m\,K_1(mr)}{2\pi^2r}$;
> - altogether, the Pauli–Jordan function is
>
> $$
> D(\xi) = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\Bigl[\delta(\xi^2) - \frac{m}{2\sqrt{\xi^2}}\,\theta(\xi^2)\,J_1\bigl(m\sqrt{\xi^2}\bigr)\Bigr].
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 (Derivation "Explicit forms", massive) · PHY 513, Problem Set 4, Problem 3(b)*

^thm-c2b-4-8

> [!derivation]- Derivation
> **Step 1** (inside). By [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], $D_W = \frac{m}{8\pi\tau}[Y_1 + i\operatorname{sgn}(\xi^0)J_1]$, so $D = 2\operatorname{Im}D_W = \operatorname{sgn}(\xi^0)\frac{mJ_1(m\tau)}{4\pi\tau}$ and $D_1 = 2\operatorname{Re}D_W = \frac{mY_1(m\tau)}{4\pi\tau}$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]]).
>
> **Step 2** (outside). $D = 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]) and $D_1 = 2D_W = \frac{mK_1(mr)}{2\pi^2r}$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).
>
> **Step 3** (on the cone: the delta function). By [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]] (as distributions, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 3) the singular part of $D_W$ is the massless function, whose imaginary part gives the massless $D$ of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]]: the term $-\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2)$.
>
> **Step 4** (on the cone: no further delta, a finite jump). The next term, $\frac{m^2}{8\pi^2}\ln\frac{ms}{2}$, is locally integrable, so it contributes no delta function. Across the future cone $\ln s$ changes from real (outside) to $\ln\tau + i\pi/2$ (inside, $s = i\tau$), so $\operatorname{Im}D_W$ jumps by $\frac{m^2}{8\pi^2}\cdot\frac\pi2 = \frac{m^2}{16\pi}$ and $D$ by $\frac{m^2}{8\pi}$, which is the $\tau \to 0$ limit of Step 1: $\frac{mJ_1(m\tau)}{4\pi\tau} \to \frac{m}{4\pi\tau}\cdot\frac{m\tau}{2} = \frac{m^2}{8\pi}$ (using $J_1(x) \simeq x/2$).
>
> **Step 5** (assemble; as distributions on $\mathbb R^4$: the tail $\theta(\xi^2)J_1(m\sqrt{\xi^2})/\sqrt{\xi^2}$ is bounded, since $J_1(x)/x \to \frac12$, hence locally integrable and a regular distribution, [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2). Inside the cone, $-\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\bigl(-\frac{m}{2\tau}J_1\bigr) = \operatorname{sgn}(\xi^0)\frac{mJ_1}{4\pi\tau}$, matching Step 1; outside, $\theta(\xi^2) = 0$ and $\delta(\xi^2) = 0$, matching Step 2; on the cone, Step 3.
>
> **What the derivation shows.**
> - Besides the light-cone singularity, a massive commutator has a tail filling the inside of the cone: massive waves do not obey sharp Huygens propagation.
> - $D_1 \to -1/2\pi^2\xi^2$ near the cone reproduces the massless Hadamard function.
> - Used next: the support picture (figure below) and the domain of dependence (Theorem §C2b.4.12).

^der-c2b-4-8

*Uses:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4|Theorem §C2b.3.4]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]]

> [!remark] Remark: Sharp and blurred propagation
> For $m = 0$ the commutator is supported on the cone alone: a massless disturbance travels exactly at the speed of light and leaves nothing behind, Huygens' principle in its sharp form, which holds for the wave equation in three (more generally odd, $\ge 3$) space dimensions (compare [[§A4.4 Huygens's Principle|WO §A4.4]] and the retarded potentials of [[§B11.1★ Potentials, Gauges and Retarded Potentials#^thm-b11-1-4|EM Theorem §B11.1.4]]). For $m > 0$ a $J_1$ tail fills the inside of the cone: the components of a massive wave travel at all group velocities below 1 ([[§B4.1 The Klein–Gordon Equation#^thm-b4-1-6|REL Theorem §B4.1.6]]), so the signal arrives on the cone and keeps arriving afterwards.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7*

^rem-c2b-4-4

## Commutators at unequal times

> [!theorem] Theorem §C2b.4.9: Commutators at Unequal Times
> All commutators of the free field are $c$-numbers fixed by $D$:
>
> $$
> [\phi(x), \phi(y)] = iD(x - y), \qquad [\phi(x), \pi(y)] = i\,\partial_{y^0}D(x - y) = i\int\frac{d^3p}{(2\pi)^3}\cos\bigl(p\cdot(x - y)\bigr), \qquad [\pi(x), \pi(y)] = i\,\partial_{x^0}\partial_{y^0}D(x - y) .
> $$
>
> At equal times they reduce to the canonical relations. Only the equal-time relations are postulated; the equation of motion carries them to every pair of times.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 (Principle "What is postulated and what is derived", Derivation "Reduction to one function, and the mode integrals")*

^thm-c2b-4-9

> [!derivation]- Derivation
> **Step 1** (derivatives pass through the commutator). $\pi(y) = \partial_{y^0}\phi(y)$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], 3) and $\phi(x)$ does not depend on $y$, so by the product rule $\partial_{y^0}\bigl(\phi(x)\phi(y) - \phi(y)\phi(x)\bigr) = \phi(x)\pi(y) - \pi(y)\phi(x) = [\phi(x), \pi(y)]$ (derivatives of distributions, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]; concretely the smeared form of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]). With $[\phi(x), \phi(y)] = iD(x - y)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]), $[\phi(x), \pi(y)] = i\partial_{y^0}D(x - y)$; applying $\partial_{x^0}$ in the same way, $[\pi(x), \pi(y)] = i\partial_{x^0}\partial_{y^0}D$.
>
> **Step 2** (the phase). In $p\cdot\xi = E_{\mathbf p}(x^0 - y^0) - \mathbf p\cdot(\mathbf x - \mathbf y)$: $\partial_{y^0}(p\cdot\xi) = -E_{\mathbf p}$ and $\partial_{x^0}(p\cdot\xi) = +E_{\mathbf p}$.
>
> **Step 3** (mode integrals). From $iD = -i\int\frac{d^3p}{(2\pi)^3}\frac{\sin p\cdot\xi}{E}$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]]):
>
> $$
> [\phi(x), \pi(y)] = -i\int\frac{d^3p}{(2\pi)^3}\frac{\cos(p\cdot\xi)\cdot(-E_{\mathbf p})}{E_{\mathbf p}} = i\int\frac{d^3p}{(2\pi)^3}\cos(p\cdot\xi), \qquad [\pi(x), \pi(y)] = i\int\frac{d^3p}{(2\pi)^3}\bigl(-\sin(p\cdot\xi)\bigr)E_{\mathbf p} .
> $$
>
> **Step 4** (check at equal times). At $x^0 = y^0$ the phase is $-\mathbf p\cdot(\mathbf x - \mathbf y)$. The sine integrals vanish, being odd under $\mathbf p \to -\mathbf p$ (Jacobian 1, $E_{-\mathbf p} = E_{\mathbf p}$; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in the pairing with a test function). The cosine integral is the real part of $\int\frac{d^3p}{(2\pi)^3}e^{-i\mathbf p\cdot(\mathbf x - \mathbf y)} = \delta^3(\mathbf x - \mathbf y)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 1), its imaginary part being odd (the plane-wave delta, an identity in $\mathcal S'(\mathbb R^3)$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]; the equal-time restriction is the limit $y^0 \to x^0$ in $\mathcal S'(\mathbb R^3)$ of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], 2). So $[\phi, \pi] = i\delta^3$ and $[\phi, \phi] = [\pi, \pi] = 0$: [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]] is recovered.
>
> **What the derivation shows.**
> - At unequal times the phases $E_{\mathbf p}(x^0 - y^0)$ smear the delta function out: $[\phi, \pi]$ is the canonical delta function, propagated.
> - With interactions these commutators become genuine operators → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-7|★ Remark: With interactions]].
> - Used next: the contact terms of time-ordered products ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]).

^der-c2b-4-9

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]

> [!theorem] Theorem §C2b.4.10: Commutators at Unequal Times as Distributions
> For real $f, g \in \mathcal S(\mathbb R^3)$ and sharp-time fields $\phi(t, f) = \int d^3x\,f(\mathbf x)\phi(t, \mathbf x)$ ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]] at time $t$):
> 1. The relations of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]] hold as identities of bilinear forms, e.g. $[\phi(x^0, f), \pi(y^0, g)] = i\int d^3x\,d^3y\,f(\mathbf x)g(\mathbf y)\,\partial_{y^0}D(x - y)$. At fixed $t = x^0 - y^0$ the three kernels are tempered distributions in $\mathbf x - \mathbf y$ with spatial transforms $-\sin(E_{\mathbf p}t)/E_{\mathbf p}$, $\cos(E_{\mathbf p}t)$ and $-E_{\mathbf p}\sin(E_{\mathbf p}t)$ (times $i$), smooth in $t$.
> 2. As $t \to 0$ the kernels tend in $\mathcal S'(\mathbb R^3)$ to $0$, $i\delta^3$ and $0$: the canonical relations ([[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]]) are the equal-time limits. The integral $\int\frac{d^3p}{(2\pi)^3}\cos(p\cdot\xi)$ converges for no $\xi$; it means this distribution.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 (Derivation "Reduction to one function, and the mode integrals") · stated here as distributions*

^thm-c2b-4-10

> [!derivation]- Derivation
> **Step 1** (smeared fields at two times). With the spatial transform $\tilde f(\mathbf k) = \int d^3x\,f(\mathbf x)e^{-i\mathbf k\cdot\mathbf x}$, [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]] smeared at time $t$ gives $\phi(t, f) = \int\frac{d^3p}{(2\pi)^3\sqrt{2E_{\mathbf p}}}\bigl(e^{-iE_{\mathbf p}t}\tilde f(-\mathbf p)\,a_{\mathbf p} + e^{iE_{\mathbf p}t}\tilde f(\mathbf p)\,a_{\mathbf p}^\dagger\bigr)$, Schwartz coefficients ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], Step 1).
>
> **Step 2** (the commutator). With $[a_{\mathbf p}, a_{\mathbf q}^\dagger] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ acting on Schwartz coefficients, and $t = x^0 - y^0$,
>
> $$
> [\phi(x^0, f), \phi(y^0, g)] = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl(e^{-iE_{\mathbf p}t}\tilde f(-\mathbf p)\tilde g(\mathbf p) - e^{iE_{\mathbf p}t}\tilde f(\mathbf p)\tilde g(-\mathbf p)\Bigr) = \int\frac{d^3p}{(2\pi)^3}\,\tilde f(-\mathbf p)\tilde g(\mathbf p)\,\frac{-i\sin E_{\mathbf p}t}{E_{\mathbf p}},
> $$
>
> after $\mathbf p \to -\mathbf p$ in the second term ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1; absolutely convergent).
>
> **Step 3** (the kernel). For $h(\boldsymbol\xi) = \int d^3y\,f(\boldsymbol\xi + \mathbf y)g(\mathbf y)$, $\tilde h(\mathbf k) = \tilde f(\mathbf k)\tilde g(-\mathbf k)$ (translation ↔ phase, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 1), and the distribution with spatial transform $-\sin(Et)/E$, $D(t, \cdot)$ of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3, acts on $h$ as $\int\frac{d^3k}{(2\pi)^3}\frac{-\sin E_{\mathbf k}t}{E_{\mathbf k}}\tilde h(-\mathbf k)$. Comparing with Step 2, $[\phi(x^0, f), \phi(y^0, g)] = i\,D(t, \cdot)[h] = i\int d^3x\,d^3y\,f(\mathbf x)g(\mathbf y)D(x - y)$.
>
> **Step 4** (time derivatives). $\pi(y^0, g) = \partial_{y^0}\phi(y^0, g)$ on wave-packet states ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], 3, smeared). Differentiating Step 2 under the absolutely convergent integral ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2) brings $\partial_{y^0} = -\partial_t$ onto $-i\sin(Et)/E$, giving $i\cos(Et)$; $\partial_{x^0}\partial_{y^0} = -\partial_t^2$ gives $-iE\sin(Et)$. Each is polynomially bounded in $\mathbf p$, so the kernels are tempered in $\boldsymbol\xi$ and smooth in $t$. Part 1.
>
> **Step 5** (equal times). As $t \to 0$, $\sin(Et)/E \to 0$, $\cos(Et) \to 1$, $E\sin(Et) \to 0$ pointwise, bounded by $|t|$, $1$, $E^2|t|$; dominated convergence against $\tilde h(-\mathbf k)$ gives convergence of the pairings ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]). The limit transform $1$ is that of $\delta^3$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 3; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). Part 2.
>
> **What the derivation shows.**
> - "Unequal times" means: a smooth function of the time difference with values in spatial distributions. Its value at $t = 0$, and products with $\delta(x^0 - y^0)$, are therefore defined: the contact terms of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], Step 7, and [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]].
> - The equal-time relations are recovered as limits, not as values: the derived commutators contain the postulated ones continuously.

^der-c2b-4-10

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-2|Theorem §C2a.1.2]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]

> [!theorem] Theorem §C2b.4.11: Cauchy Data of the Commutator Function
> $D$ is the unique solution of $(\partial^2 + m^2)D = 0$ with
>
> $$
> D(0, \boldsymbol\xi) = 0, \qquad \partial_0D(0, \boldsymbol\xi) = -\delta^3(\boldsymbol\xi) .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 (Derivation "Why the equal-time data suffice: a Cauchy problem")*

^thm-c2b-4-11

> [!derivation]- Derivation
> **Step 1** (it is a solution). Every mode of $D$ is on shell ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], 2).
>
> **Step 2** (the data). At $\xi^0 = 0$, $D = -\int\frac{d^3p}{(2\pi)^3}\frac{\sin(-\mathbf p\cdot\boldsymbol\xi)}{E_{\mathbf p}} = 0$ by oddness. Differentiating, $\partial_0D = -\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}\cos(p\cdot\xi)}{E_{\mathbf p}}$, which at $\xi^0 = 0$ is $-\delta^3(\boldsymbol\xi)$ (in $\mathcal S'(\mathbb R^3)$: the spatial transform $-\cos(E\cdot0) = -1$, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3) as in Step 4 of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]]. Equivalently, $\partial_{x^0}D = -i[\pi(x), \phi(y)] = -i\cdot(-i)\delta^3 = -\delta^3$ at equal times.
>
> **Step 3** (uniqueness; for tempered solutions, whose transforms are distributions supported on the shell, [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], with $\alpha_{\mathbf p}$, $\beta_{\mathbf p}$ distributions in $\mathbf p$ and the $2\times2$ system solved by multiplying with smooth functions of $\mathbf p$, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1). A solution with a spatial Fourier transform has the form $f(t, \mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\sqrt{2E_{\mathbf p}}}\bigl(\alpha_{\mathbf p}e^{-iE_{\mathbf p}t} + \beta_{\mathbf p}e^{iE_{\mathbf p}t}\bigr)$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]]). At $t = 0$ its data have transforms $\tilde f = (\alpha + \beta)/\sqrt{2E}$ and $\tilde{\dot f} = -iE(\alpha - \beta)/\sqrt{2E}$. This $2\times2$ linear system for $(\alpha, \beta)$ has determinant $\frac{1}{2E}\cdot\det\begin{pmatrix}1 & 1\\ -iE & iE\end{pmatrix} = \frac{2iE}{2E} = i \ne 0$, so the data fix $\alpha_{\mathbf p}$, $\beta_{\mathbf p}$, hence $f$. Two solutions with the same data are equal.
>
> **What the derivation shows.**
> - Quantizing on a single time slice is enough: the canonical relations at one instant, carried by the field equation, determine every commutator at every pair of times.
> - $E_{\mathbf p} > 0$ is used in Step 3 (for $m = 0$ it fails only at $\mathbf p = 0$, a set of measure zero).
> - Used next: Theorem §C2b.4.12 and the retarded Green's function, whose data are the same ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]]).

^der-c2b-4-11

*Uses:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]]

> [!theorem] Theorem §C2b.4.12: The Commutator Function Propagates the Field
> For every time $y^0$,
>
> $$
> \phi(x) = -\int d^3y\;D(x - y)\overleftrightarrow{\partial}_{y^0}\phi(y) = -\int d^3y\,\Bigl[D(x - y)\,\pi(y) - \partial_{y^0}D(x - y)\,\phi(y)\Bigr],
> $$
>
> with $f\overleftrightarrow{\partial}_0g = f\partial_0g - (\partial_0f)g$. Since $D$ vanishes outside the cone, $\phi(x)$ is fixed by the data $(\phi, \pi)$ on any earlier slice inside the backward light cone of $x$, and for $m = 0$ by the data on the surface of that cone alone.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 (Derivation "The commutator function propagates the field")*

^thm-c2b-4-12

> [!derivation]- Derivation
> *Sense of the formula:* smear in $\mathbf x$ at fixed $x^0$ with $f \in \mathcal S(\mathbb R^3)$. Then $\int d^3x\,f(\mathbf x)D(x - y) = \bigl(D(x^0 - y^0, \cdot) \ast  f\bigr)(\mathbf y)$ is a Schwartz function of $\mathbf y$ (at fixed time $D$ has compact spatial support, $|\boldsymbol\xi| \le |\xi^0|$, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]]), so every $d^3y$ integral below is a sharp-time smeared field ([[§C2a.1 Canonical Quantization of Fields#^def-c2a-1-1|Def. §C2a.1.1]]) and the identity is one between operators.
>
> **Step 1** (both factors solve the equation in $y$). $\phi(y)$ does ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]]). $D(x - y)$, as a function of $y$, does too: $\partial_{y^\mu} = -\partial_{\xi^\mu}$, and second derivatives carry two minus signs, so $(\partial_y^2 + m^2)D(x - y) = (\partial_\xi^2 + m^2)D(\xi) = 0$.
>
> **Step 2** (independence of $y^0$). Let $F(y^0) = \int d^3y\,(D\,\partial_0\phi - \partial_0D\,\phi)$, derivatives with respect to $y^0$. Then $F' = \int d^3y\,(\partial_0D\,\partial_0\phi + D\,\partial_0^2\phi - \partial_0^2D\,\phi - \partial_0D\,\partial_0\phi)$; the first and last terms cancel. By Step 1, $\partial_0^2 = \nabla^2 - m^2$ on both, the $m^2$ terms cancel, and $F' = \int d^3y\,(D\nabla^2\phi - \nabla^2D\,\phi)$. Two integrations by parts (Green's second identity) turn this into a surface integral $\oint dS\,(D\,\hat n\cdot\nabla\phi - \hat n\cdot\nabla D\,\phi)$ over a large sphere, which vanishes: at fixed $y^0$, $D(x - y)$ is zero for $|\mathbf y - \mathbf x| > |x^0 - y^0|$ (Theorem §C2b.4.5), so the sphere can be taken where $D$ and $\nabla D$ vanish. This is the conservation of the Klein–Gordon product ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]], 1).
>
> ⚑ By-product: no fall-off of $\phi$ is needed here; microcausality itself makes the surface term vanish.
>
> **Step 3** (the value at $y^0 = x^0$). There $D(x - y) = 0$ and $\partial_{y^0}D(x - y) = -\partial_{x^0}D(x - y) = -(-\delta^3(\mathbf x - \mathbf y)) = \delta^3(\mathbf x - \mathbf y)$ (equal-time limits in $\mathcal S'(\mathbb R^3)$, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], 2) ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]]). So $-F(x^0) = -\int d^3y\,\bigl(0 - \delta^3(\mathbf x - \mathbf y)\phi(x^0, \mathbf y)\bigr) = \phi(x)$.
>
> **Step 4** (every $y^0$). By Step 2, $-F(y^0) = -F(x^0) = \phi(x)$ for every $y^0$. The support statements follow from [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]] and [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]].
>
> **What the derivation shows.**
> - Microcausality and "no signal outside the light cone" are one statement, once a commutator and once a propagation kernel → [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-5|Remark: Microcausality and the domain of dependence are one statement]].
> - The same structure, a solution expressed by its Cauchy data through a kernel, is the classical Cauchy problem; here it holds for operators.

^der-c2b-4-12

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-3|Theorem §C2b.1.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]]

![[ph-qft-c2-5-2.svg]]
*Where the commutator function lives (Theorems §C2b.4.7–§C2b.4.8). (a) $m = 0$: only on the light cone. (b) $m > 0$: the cone plus a $J_1$ tail inside it, changing sign on the hyperbolas $m\tau = 3.83,\ 7.02,\ 10.17$ (dotted); blue $D > 0$, red $D < 0$, the pattern reversed between future and past; outside the cone $D = 0$. (c) Theorem §C2b.4.12 as a picture: the data on an earlier slice that determine $\phi(x)$, the whole ball for $m > 0$, its boundary only for $m = 0$. Adapted from the user's PHY 513 notes, Fig. 5.2.*

> [!remark] Remark: Microcausality and the domain of dependence are one statement
> Theorem §C2b.4.12 reads the commutator function as a propagation kernel; Principle §C2b.4.1 reads it as a compatibility condition. The two say the same thing: what happens at $x$ depends only on the past light cone of $x$. That a quantization on one time slice suffices ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-1|Principle §C2a.1.1]]) is the operator version of the classical Cauchy problem.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7*

^rem-c2b-4-5

> [!remark]- ★ Remark: Other states: what belongs to the dynamics and what to the state
> In any state $\rho$, $\operatorname{Tr}(\rho[\phi(x), \phi(y)]) = iD(x - y)$, because the commutator is a $c$-number (Theorem §C2b.4.2): $D$, and with it causality and the retarded response, belong to the dynamics. Everything state-dependent is in the symmetric part $D_1^\rho(x, y) = \operatorname{Tr}(\rho\{\phi(x), \phi(y)\})$, which need not depend on $x - y$ alone.
> - *Thermal state* $\rho = e^{-\beta H}/Z$: the modes are independent oscillators with $\langle a_{\mathbf p}^\dagger a_{\mathbf q}\rangle_\beta = (2\pi)^3\delta^3(\mathbf p - \mathbf q)\,n(E_{\mathbf p})$, $n(E) = (e^{\beta E} - 1)^{-1}$ ([[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^thm-b10-1-2|TH Theorem §B10.1.2]]), $\langle a_{\mathbf p}a_{\mathbf q}^\dagger\rangle_\beta = (2\pi)^3\delta^3(\mathbf p - \mathbf q)(1 + n)$ by the commutator, and $\langle aa\rangle_\beta = \langle a^\dagger a^\dagger\rangle_\beta = 0$. With $1 + 2n = \coth(\beta E/2)$,
>
> $$
> D_1^\beta(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\,\coth\frac{\beta E_{\mathbf p}}{2}\,\bigl(e^{-ip\cdot\xi} + e^{ip\cdot\xi}\bigr) \;\xrightarrow{\beta\to\infty}\; D_1(\xi):
> $$
>
> heating enlarges the fluctuations of each mode by $\coth(\beta E/2) \ge 1$ and leaves the commutator untouched.
> - *Coherent state* ([[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1|Def. §C2a.6.1]]): $\phi = \bar\phi + \tilde\phi$, with $\bar\phi$ the classical field and $\tilde\phi$ carrying vacuum correlations ([[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7|Theorem §C2a.6.7]]), so $D_1^{\mathrm{coh}}(x, y) = 2\bar\phi(x)\bar\phi(y) + D_1(x - y)$: the vacuum's fluctuations riding on a classical wave.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.11 (Derivation "Generalization: other states")*

^rem-c2b-4-6

> [!remark]- ★ Remark: With interactions: the Källén–Lehmann representation
> Unequal-time commutators of an interacting field are genuine operators. Two things survive: the equal-time relations remain the postulate, and microcausality becomes an axiom. The vacuum expectation value of the commutator becomes a superposition of free commutator functions over masses, $\langle0|[\phi(x), \phi(y)]|0\rangle = \int d\mu^2\,\rho(\mu^2)\,iD_\mu(x - y)$, and applying the equal-time relation to both sides (Theorem §C2b.4.11: $\partial_0D_\mu = -\delta^3$ for every $\mu$) gives the sum rule $\int d\mu^2\,\rho(\mu^2) = 1$. PS §7.1 derives the representation.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.7 ("With interactions (preview)")*

^rem-c2b-4-7

> [!remark]- Connections
> - [[§C1.3 Causal Structure and the Causality of a Single Particle|§C1.3]] tests causality with the single-particle amplitude $\langle\mathbf x|e^{-iHt}|\mathbf 0\rangle$ for $H = \sqrt{\mathbf p^2 + m^2}$ and finds a leak $\propto e^{-m\sqrt{r^2 - t^2}}$ ([[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-6|Theorem §C1.3.6]], [[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-7|Theorem §C1.3.7]]); it uses Theorem §C2b.3.1, since that amplitude is $-2\partial_\tau$ of the Euclidean function, continued to $\tau = it$. The repair is Theorem §C2b.4.5; at the level of the amplitude, forward plus backward propagation is already causal ([[§C1.3 Causal Structure and the Causality of a Single Particle#^thm-c1-3-9|Theorem §C1.3.9]]).
> - Microcausality is the relativistic form of no-signalling: operators on spacelike-separated regions commute as operators on different tensor factors do ([[§C11.3 Composite Systems and Reduced Density Matrices#^thm-c11-3-5|QM Theorem §C11.3.5]]), and $D_1 \neq 0$ there is correlation without communication ([[§C11.4★ Entanglement, EPR and Bell's Inequality#^rem-c11-4-4|QM Remark: Correlation without communication]]).
> - The light-cone boundary between commuting and non-commuting points comes from the orbit structure of $SO^+(1,3)$ ([[§B1.3 Causal Structure and Proper Time#^rem-b1-3-1|REL Remark: Normal forms, and the orbits of the Lorentz group]]); the invariance of $\operatorname{sgn}p^0$ that makes $\theta(p^0)\delta(p^2 - m^2)$ invariant is the same fact for momenta ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]).
> - The massless commutator $-\frac{1}{4\pi r}[\delta(t - r) - \delta(t + r)]$ is, up to the factor $i$ and the step function, the retarded kernel of the wave equation behind the retarded potentials ([[§B11.1★ Potentials, Gauges and Retarded Potentials#^thm-b11-1-4|EM Theorem §B11.1.4]]); the full statement is the retarded Green's function of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]].
> - Forward: $D_W$ and time ordering give the Feynman propagator ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]); the product of two free fields is its normal-ordered part plus $D_W$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]); the commutator function becomes the retarded response to a source ([[§C2b.8 Particle Production by a Classical Source|§C2b.8]]); for spin, QFT C5b ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]]) repeats the analysis with anticommutators.
> - [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]] (support and singular support) is the language of microcausality: $D$ vanishes on the open spacelike region (Theorem §C2b.4.6) and is singular exactly on the cone (Theorem §C2b.4.4).
> - [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]] (Sokhotski–Plemelj) splits the massless $D_W$ into the principal-value correlation $D_1$ and the delta-function commutator $D$; [[§CA.2 Generalized Functions#^thm-ca-2-13|Theorem §CA.2.13]] is the same split on all of $\mathbb R^4$, tip included.
> - [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]] and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] (composition of δ, the invariant cone distribution $\operatorname{sgn}(x^0)\delta(x^2)$) turn $\delta(t \mp r)/2r$ into the covariant massless commutator.
> - [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]] (reflection) and [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]] (multiplication by a smooth function) give the transforms of $D$, $D_1$ and their field equation.
> - [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]] (regular distributions) makes the $J_1$ tail of the massive commutator an honest locally integrable function.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] (plane-wave delta, translation ↔ phase, relabelling) reduce the unequal-time commutators to one spatial distribution per time difference (Theorem §C2b.4.10); [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]] takes its equal-time limit.
