---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.5 Green's Functions and Contours]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.7 Wick Rotation and the Two-Point Family]] →

*Sources: the user's PHY 513 notes, Ch. 5 §5.6 (time ordering) and Ch. 6 §§6.7, 6.9, 6.11–6.13 · PHY 513 Lecture 6 (Larsen, 21 Sep 2026), Part B · Peskin & Schroeder §2.4, pp. 29–31 · Yu §§6.2–6.3 and §6.4.1, eqs. (6.194)–(6.211) · PHY 513, Problem Set 4, Problem 4.*

Which Green's function is a vacuum expectation value of field operators? The Feynman propagator: the vacuum expectation value of the time-ordered product, defined here, computed with a contour of [[§C2b.5 Green's Functions and Contours|§C2b.5]] from the Wightman function of [[§C2b.2 The Wightman Function|§C2b.2]]. Its mirror image, the anti-Feynman function, is the vacuum expectation value of the anti-time-ordered product. The section shows that the Feynman propagator is a Green's function as an operator statement, relates time ordering to normal ordering (with the zero-point energy as the same subtraction at one point), and turns the contours into the $i\varepsilon$ prescription.

*Conventions* ([[Larsen PHY 513]]): Green's functions are normalized by $(\partial^2 + m^2)D_C = -i\delta^4$ (PS), so that $D_F = \langle0|T\{\phi\phi\}|0\rangle$ with no prefactor and $\tilde D_F = i/(p^2 - m^2 + i\varepsilon)$; Fourier conventions as in [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]; $\xi = x - y$, $t = \xi^0$, $E = E_{\mathbf p}$.

## Time ordering and the Feynman propagator

> [!definition] Definition §C2b.6.1: Time-Ordered Product
> For field operators at $x$ and $y$,
>
> $$
> T\{\phi(x)\phi(y)\} \equiv \theta(x^0 - y^0)\,\phi(x)\phi(y) + \theta(y^0 - x^0)\,\phi(y)\phi(x) ,
> $$
>
> the later operator to the left, with $\theta(0) = \frac12$. For $n$ fields, $T\{\phi(x_1)\cdots\phi(x_n)\} = \phi(x_{\sigma(1)})\cdots\phi(x_{\sigma(n)})$ with $x^0_{\sigma(1)} \ge \cdots \ge x^0_{\sigma(n)}$. The opposite ordering is the anti-time-ordered product ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|Def. §C2b.6.2]]). (Fermion fields will add a sign per exchange, [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]].) Names in other sources: [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-3|Caution: Names for the time-ordered product]].
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.6 (Definition "The time-ordered product") · PS §2.4, eq. (2.60) · Yu §6.2, eq. (6.108)*

^def-c2b-6-1

> [!caution] Caution: Names for the time-ordered product
> One operation, three bracket styles. These notes write $T\{\phi(x)\phi(y)\}$ everywhere, with braces, as Lecture 6 (slide "Green's Functions and Boundary Conditions": $\langle0|T\{\phi(x)\phi(y)\}|0\rangle$) and the user's PHY 513 notes (Ch. 5 §5.6) do, and the same for $\bar T$, for Dirac fields ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]) and for vector fields ([[§C4.9 Vector-Field Propagators#^def-c4-9-2|Def. §C4.9.2]]). Peskin–Schroeder write $T\phi(x)\phi(y)$ without brackets (eq. (2.60)) and $T[A_\mu(x)A_\nu(y)]$ with square ones (p. 124); Yu and the user's pre-course notes write $T[\phi(x)\phi(y)]$ (Yu eq. (6.108)). Earlier drafts of this vault sometimes dropped the braces ($\langle0|T\phi\phi|0\rangle$).
>
> *Source: Lecture 6, slide "Green's Functions and Boundary Conditions" · the user's PHY 513 notes, Ch. 5 §5.6 · PS §2.4, eq. (2.60); §4.8, p. 124 · Yu §6.2, eq. (6.108) · the user's pre-course notes, §6.2*

^cau-c2b-6-3

> [!theorem] Theorem §C2b.6.1: Properties of Time Ordering
> 1. $T$ reorders by time labels, so $T\{\phi(x)\phi(y)\} = T\{\phi(y)\phi(x)\}$.
> 2. At equal times both orders give the same operator for $\phi\phi$, so with $\theta(0) = \frac12$ the definition gives $\phi(x)\phi(y)$ there, whichever order is written; for $\phi$ and $\pi$ the two orders differ and the equal-time value is ambiguous.
> 3. $T\{\phi(x)\phi(y)\}$ is the same in every inertial frame, because of microcausality.
> 4. For any $A(x)$, $B(y)$: $\partial_{x^0}T\{A(x)B(y)\} = T\{\partial_0A(x)\,B(y)\} + \delta(x^0 - y^0)\,[A(x), B(y)]$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.6 (Derivation "Properties of time ordering"), Ch. 6 §6.7 (eq. (dT)) · Yu §6.2, eqs. (6.108)–(6.113)*

^thm-c2b-6-1

> [!derivation]- Derivation
> **Step 1** (symmetry). Writing the arguments in the other order exchanges the roles of the two step functions and the two products: $T\{\phi(y)\phi(x)\} = \theta(y^0 - x^0)\phi(y)\phi(x) + \theta(x^0 - y^0)\phi(x)\phi(y)$, the same two terms.
>
> **Step 2** (equal times). At $x^0 = y^0$, $\phi(x)\phi(y) - \phi(y)\phi(x) = [\phi(t, \mathbf x), \phi(t, \mathbf y)] = 0$ ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]), so $\theta(0)\phi\phi + \theta(0)\phi\phi$ is unambiguous once $\theta(0) + \theta(0) = 1$. For $\phi$ and $\pi$, $[\phi, \pi] = i\delta^3 \ne 0$ at equal times, and the ordering there is ambiguous.
>
> ⚑ By-product: the ambiguity for $\phi$ and $\pi$ is the origin of contact terms → part 4 and [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]; the convention $\theta(0) = \frac12$ → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-1|Caution: The step function at zero]].
>
> **Step 3** (timelike separation). For $(x - y)^2 > 0$ the sign of $x^0 - y^0$ is the same in every frame related by $SO^+(1,3)$ ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]), so every observer makes the same choice of term.
>
> **Step 4** (spacelike separation). For $(x - y)^2 < 0$ observers disagree on the order, but there $[\phi(x), \phi(y)] = 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]), so both terms are the same operator and the disagreement is harmless. This is part 3.
>
> **Step 5** (derivative). $\partial_{x^0}\theta(x^0 - y^0) = \delta(x^0 - y^0)$ and $\partial_{x^0}\theta(y^0 - x^0) = -\delta(x^0 - y^0)$ ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], 2). By the product rule,
>
> $$
> \partial_{x^0}T\{AB\} = \theta(x^0 - y^0)\,\partial_0A\,B + \theta(y^0 - x^0)\,B\,\partial_0A + \delta(x^0 - y^0)\bigl(AB - BA\bigr),
> $$
>
> and the first two terms are $T\{\partial_0A\,B\}$. (Sense: $\delta(x^0 - y^0)[A(x), B(y)]$ is the equal-time value of the commutator times δ, defined when the commutator is a smooth function of $x^0 - y^0$ with values in spatial distributions; for $A, B \in \{\phi, \pi\}$ of the free field it is, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]]. For interacting fields this is an assumption.)
>
> **What the derivation shows.**
> - Microcausality is exactly what makes time ordering relativistic: without it the definition would depend on the observer.
> - A time derivative passes into a time-ordered product at the price of an equal-time commutator, a contact term.

^der-c2b-6-1

*Uses:* [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]]

> [!remark] Remark: Why the later operator stands to the left
> In $\langle0|\cdots|0\rangle$ operators act on the state from right to left, so reading right to left is reading the history: the earliest acts first. Time evolution composes the same way, $U(t_3, t_2)U(t_2, t_1) = U(t_3, t_1)$ ([[§C3.1 The Time-Evolution Operator and the Schrödinger Equation|QM §C3.1]]), and Dyson's formula for interacting fields will order its exponential this way (QFT C6, planned). In the lecture's words: time starts on the right, things happen, and time ends on the left.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.6*

^rem-c2b-6-1

> [!caution] Caution: The step function at zero
> The step-function form must not double-count at $x^0 = y^0$, which needs $\theta(0) = \frac12$. Problem Set 3 uses $\theta(0) = 1$; with it the definition gives $\phi(x)\phi(y) + \phi(y)\phi(x)$ at equal times, twice too much. For $\phi\phi$ the order at equal times is then the only issue, and with $\theta(0) = \frac12$ there is none (Theorem §C2b.6.1, 2); in any case a single instant carries no weight once integrated against a smooth function of time.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.6, property 3*

^cau-c2b-6-1

> [!theorem] Theorem §C2b.6.2: The Feynman Propagator
> The **Feynman** contour $C_F$ passes below $-E_{\mathbf p}$ and above $+E_{\mathbf p}$. Then
>
> $$
> D_F(\xi) = \theta(\xi^0)\,D_W(\xi) + \theta(-\xi^0)\,D_W(-\xi) = \langle0|T\{\phi(x)\phi(y)\}|0\rangle .
> $$
>
> $D_F$ is even in $\xi$, Lorentz invariant, and $D_F = D_R + D_W(-\xi)$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7 · PHY 513 Lecture 6, "Evaluation of the Feynman Propagator" · PS §2.4, eqs. (2.59)–(2.60) · Yu §6.4.1, eqs. (6.194)–(6.211) · PHY 513, Problem Set 4, Problem 4(a)*

^thm-c2b-6-2

> [!derivation]- Derivation
> **Step 1** (set up; [[P2 Green's Functions by Contour Integration#^p2-2|P2, steps 2–4]]). As in Steps 1–2 of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], $D_F = \int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}G_F(t)$, and the arcs vanish in the lower half-plane for $t > 0$ and the upper one for $t < 0$.
>
> **Step 2** ($t > 0$). Close downward, clockwise. $C_F$ passes above $+E$, so $+E$ lies below the contour and is enclosed; it passes below $-E$, so $-E$ is not. Residue at $+E$: $\frac{i}{2\pi}\frac{e^{-iEt}}{2E}$. So $G_F = -2\pi i\cdot\frac{i}{2\pi}\frac{e^{-iEt}}{2E} = \frac{e^{-iEt}}{2E}$, and $\int\frac{d^3p}{(2\pi)^3\,2E}e^{-iEt + i\mathbf p\cdot\boldsymbol\xi} = D_W(\xi)$.
>
> **Step 3** ($t < 0$). Close upward. Closing upward always runs counterclockwise (the arc goes from right to left over the top). Only $-E$ is enclosed, with residue $\frac{i}{2\pi}\cdot\frac{-e^{iEt}}{2E}$. So $G_F = +2\pi i\cdot\frac{i}{2\pi}\cdot\frac{-e^{iEt}}{2E} = \frac{e^{iEt}}{2E}$.
>
> ⚑ By-product: the orientation, counterclockwise here and clockwise in the retarded case, is what turns the minus sign of the partial fractions into a plus → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|Caution: Signs that slip]].
>
> **Step 4** (relabel). In $\int\frac{d^3p}{(2\pi)^3\,2E}e^{iEt + i\mathbf p\cdot\boldsymbol\xi}$ substitute $\mathbf p \to -\mathbf p$ (Jacobian 1; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in $\mathcal S'$): $e^{iEt - i\mathbf p\cdot\boldsymbol\xi} = e^{-ip\cdot(-\xi)}$, so this is $D_W(-\xi)$. Steps 2–4 give $D_F = \theta(t)D_W(\xi) + \theta(-t)D_W(-\xi)$, the products taken slice by slice ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], 1).
>
> **Step 5** (the operator side). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]] and [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], $\langle0|T\{\phi(x)\phi(y)\}|0\rangle = \theta(t)\langle0|\phi(x)\phi(y)|0\rangle + \theta(-t)\langle0|\phi(y)\phi(x)|0\rangle = \theta(t)D_W(\xi) + \theta(-t)D_W(-\xi)$: the contour and the time-ordered product arrive independently at the same function.
>
> **Step 6** (properties). Evenness (of a distribution: $D_F[f(-\cdot)] = D_F[f]$, [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]]): $T$ is symmetric in its arguments ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], 1), so $D_F(-\xi) = D_F(\xi)$. Invariance: $T\{\phi\phi\}$ is frame-independent (Theorem §C2b.6.1, 3) and the vacuum is invariant. Relation: for $t > 0$, $D_R + D_W(-\xi) = D_W(\xi) - D_W(-\xi) + D_W(-\xi) = D_W(\xi)$; for $t < 0$, $0 + D_W(-\xi)$.
>
> **What the derivation shows.**
> - Where the retarded function says "the source acts, then there are consequences", the Feynman function is neutral about which of $x$ and $y$ came first and includes both, each with positive energy flowing forward.
> - $D_F$ is a Green's function by Theorem §C2b.5.3; the operator side of this fact is Theorem §C2b.6.5.
> - Used next: the contraction (Theorem §C2b.6.6), the $i\varepsilon$ form (Theorem §C2b.6.9), position space (Theorem §C2b.7.3).

^der-c2b-6-2

*Uses:* [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]], [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]]

> [!derivation]- Derivation (second route: from the time-ordered product, Yu's direction)
> **Step 1** (the operator definition). By Step 5 above and [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], with $\mathbf p \to -\mathbf p$ in the second term ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in $\mathcal S'$; the iterated integral read as in [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], Step 2),
>
> $$
> \langle0|T\{\phi(x)\phi(y)\}|0\rangle = \int\frac{d^3p}{(2\pi)^3}\,e^{i\mathbf p\cdot\boldsymbol\xi}\Bigl[\theta(t)\frac{e^{-iEt}}{2E} + \theta(-t)\frac{e^{iEt}}{2E}\Bigr].
> $$
>
> **Step 2** (a contour identity; Yu (6.198)). For $\varepsilon > 0$ let $f(p^0) = e^{-ip^0t}/\{[p^0 - (E - i\varepsilon)][p^0 + (E - i\varepsilon)]\}$, simple poles at $E - i\varepsilon$ (fourth quadrant) and $-E + i\varepsilon$ (second). For $t > 0$ close downward (clockwise), enclosing $E - i\varepsilon$: $\int_{\mathbb R}f = -2\pi i\frac{e^{-i(E - i\varepsilon)t}}{2(E - i\varepsilon)}$. For $t < 0$ close upward (counterclockwise), enclosing $-(E - i\varepsilon)$: $\int_{\mathbb R}f = 2\pi i\frac{e^{i(E - i\varepsilon)t}}{-2(E - i\varepsilon)}$. As $\varepsilon \to 0^+$,
>
> $$
> \int_{-\infty}^{\infty}dp^0\,f(p^0) \to -\frac{\pi i}{E}\bigl[\theta(t)e^{-iEt} + \theta(-t)e^{iEt}\bigr].
> $$
>
> **Step 3** (the denominator). $[p^0 - (E - i\varepsilon)][p^0 + (E - i\varepsilon)] = (p^0)^2 - (E - i\varepsilon)^2 = (p^0)^2 - E^2 + 2iE\varepsilon + \varepsilon^2 = p^2 - m^2 + i\varepsilon'$ with $\varepsilon' = 2E\varepsilon + O(\varepsilon^2) > 0$; only the sign of the infinitesimal matters (the limits in $\mathcal S'$ agree, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 3).
>
> **Step 4** (multiply by $i/2\pi$; Yu (6.207)–(6.208)). $\theta(t)\frac{e^{-iEt}}{2E} + \theta(-t)\frac{e^{iEt}}{2E} = \int\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{p^2 - m^2 + i\varepsilon}$. Inserting into Step 1 and combining $d^3p\,dp^0 = d^4p$, $e^{-ip^0t + i\mathbf p\cdot\boldsymbol\xi} = e^{-ip\cdot\xi}$ (the four-dimensional integral does not converge absolutely; the formula holds in $\mathcal S'(\mathbb R^4)$ in the limit $\varepsilon \to 0^+$, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]; at fixed $\mathbf p$ the limit of Step 2 is pointwise for $t \ne 0$ and bounded by $\pi/E$, so it is also a limit in $\mathcal S'(\mathbb R)$, [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]):
>
> $$
> \langle0|T\{\phi(x)\phi(y)\}|0\rangle = \int\frac{d^4p}{(2\pi)^4}\,\frac{i\,e^{-ip\cdot\xi}}{p^2 - m^2 + i\varepsilon} \qquad \text{(Yu (6.210))}.
> $$
>
> **What the derivation shows.**
> - The operator definition leads straight to the $i\varepsilon$ form of Theorem §C2b.6.9, without choosing a contour.
> - Evenness in $\xi$ is visible here by $p \to -p$ in the four-dimensional integral (Yu (6.211)).
>
> *Source: Yu §6.4.1, eqs. (6.195)–(6.211) · the user's PHY 513 notes, Ch. 6 §6.7 ("the same result Yu derives in the opposite direction")*

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]

> [!caution] Caution: Signs that slip
> - The relation is $D_F(x - y) = D_R(x - y) + D_W(y - x)$, with the Wightman arguments *exchanged*: with $D_W(x - y)$ the case $t < 0$ would come out wrong.
> - On a plane wave, $(\partial^2 + m^2)e^{-ip\cdot x} = (m^2 - p^2)e^{-ip\cdot x}$, not $(p^2 + m^2)$: check with $\partial_t^2 - \nabla^2 + m^2$ on $e^{-iEt + i\mathbf p\cdot\mathbf x}$, which gives $-E^2 + \mathbf p^2 + m^2$.
> - The Lecture 6 slide calls the leftover loop for $x^0 < y^0$ clockwise; closing upward is always counterclockwise. The conclusion on the slide is right, and it is the orientation that flips the sign relative to the retarded case.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7, §6.12 (Caution "Two slips to avoid")*

^cau-c2b-6-2

> [!definition] Definition §C2b.6.2: Anti-Time-Ordered Product
> For field operators at $x$ and $y$, the **anti-time-ordered** product puts the earlier operator to the left:
>
> $$
> \bar T\{\phi(x)\phi(y)\} \equiv \theta(y^0 - x^0)\,\phi(x)\phi(y) + \theta(x^0 - y^0)\,\phi(y)\phi(x),
> $$
>
> with $\theta(0) = \frac12$ as for $T$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]]); for $n$ fields the factors stand in order of increasing time.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.11 ($\bar T$, "the earlier operator to the left")*

^def-c2b-6-2

> [!theorem] Theorem §C2b.6.3: The Anti-Feynman Function
> The **anti-Feynman** contour $C_{\bar F}$ passes above $-E_{\mathbf p}$ and below $+E_{\mathbf p}$. Then
>
> $$
> D_{\bar F}(\xi) = -\theta(\xi^0)D_W(-\xi) - \theta(-\xi^0)D_W(\xi) = -\langle0|\bar T\{\phi(x)\phi(y)\}|0\rangle ,
> $$
>
> with $\bar T$ of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|Def. §C2b.6.2]], the products taken slice by slice.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.8 (table of contours, "every entry checked by integrating along the real axis at finite $\varepsilon$"), §6.11*

^thm-c2b-6-3

> [!derivation]- Derivation
> Steps 1–2 of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]] apply unchanged (same integrand, same arcs); the rest is [[P2 Green's Functions by Contour Integration#^p2-5|P2, steps 5–6]].
>
> **Step 1** ($t > 0$). Close downward, clockwise; $C_{\bar F}$ passes above $-E$ and below $+E$, so only $-E$ is enclosed: $G_{\bar F} = -2\pi i\cdot\frac{i}{2\pi}\cdot\frac{-e^{iEt}}{2E} = -\frac{e^{iEt}}{2E}$, which after $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in $\mathcal S'$) gives $-D_W(-\xi)$.
>
> **Step 2** ($t < 0$). Close upward, counterclockwise, around $+E$ only: $G_{\bar F} = 2\pi i\cdot\frac{i}{2\pi}\cdot\frac{e^{-iEt}}{2E} = -\frac{e^{-iEt}}{2E}$, giving $-D_W(\xi)$.
>
> **Step 3** (the operator form). $\bar T\{\phi(x)\phi(y)\} = \theta(t)\phi(y)\phi(x) + \theta(-t)\phi(x)\phi(y)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|Def. §C2b.6.2]]), whose vacuum expectation value is $\theta(t)D_W(-\xi) + \theta(-t)D_W(\xi)$ (slice products, as for $D_F$: [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], 1): minus Steps 1–2.
>
> **What the derivation shows.**
> - The anti-Feynman contour is the Feynman contour reflected in the real axis; its function is minus the vacuum expectation value of the anti-time-ordered product, and its transform carries $-i\varepsilon$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]).
> - With Theorems §C2b.5.5, §C2b.5.7 and §C2b.6.2 these exhaust the four contours.
> - Used next: $D_{\bar F} = -\overline{D_F}$ and $D_F - D_{\bar F} = D_1$ ([[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]]).

^der-c2b-6-3

*Uses:* [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2|Def. §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]

> [!theorem] Theorem §C2b.6.4: The Feynman Propagator as a Distribution: the Products θ·D_W
> 1. $D_W(\pm\xi)$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3), so $\theta(\pm\xi^0)D_W(\pm\xi)$ are defined slice by slice, as in [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1. Hence $D_F = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi) \in \mathcal S'(\mathbb R^4)$, equal to the contour's $D_F$; the value $\theta(0)$ does not enter (Caution: The step function at zero).
> 2. Away from $\xi = 0$ these are products with disjoint singular supports ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2). At $\xi = 0$ both factors are singular and no product rule applies there (compare [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1); the slice definition is the unique extension that is a fundamental solution, $(\partial^2 + m^2)D_F = -i\delta^4$. Any other extension differs by contact terms $\sum c_\alpha\partial^\alpha\delta^4$.
>
> *Source: the user's PHY 513 notes, Ch. 5 §5.6 (property 3, the step function at zero), Ch. 6 §6.2 ("Why this matters beyond tidiness": products), §6.7 · stated here as distributions*

^thm-c2b-6-4

> [!derivation]- Derivation
> **Step 1** (slice products). For $f \in \mathcal S(\mathbb R^4)$, $t \mapsto D_W(t, \cdot)[f(t, \cdot)] = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-iE_{\mathbf p}t}\tilde f_s(t, -\mathbf p)$ is continuous and rapidly decreasing in $t$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], Step 6), so $(\theta D_W)[f] \equiv \int_0^\infty dt\,D_W(t, \cdot)[f(t, \cdot)]$ converges and is bounded by a seminorm of $f$. The same for $\theta(-\xi^0)D_W(-\xi)$, with the spatial transform $e^{iE_{\mathbf p}t}/2E_{\mathbf p}$ of $D_W(-\xi)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], Step 7). A single time has measure zero, so no value of $\theta(0)$ is needed.
>
> **Step 2** (it is the contour's $D_F$). The Feynman contour gives, mode by mode, $G_F(t) = \theta(t)\frac{e^{-iEt}}{2E} + \theta(-t)\frac{e^{iEt}}{2E}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], Steps 2–3), and by Step 2 of Derivation §C2b.5.4 the contour's $D_F$ acts as $\int dt\int\frac{d^3p}{(2\pi)^3}G_F(t; E_{\mathbf p})\tilde f_s(t, -\mathbf p)$. For $t > 0$ this is $D_W(t, \cdot)[f(t, \cdot)]$; for $t < 0$, after $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1), it is $D_W(-\xi)$ at time $t$ applied to $f(t, \cdot)$. Integrating over $t$ gives Step 1. Part 1.
>
> **Step 3** (away from the origin). $\operatorname{sing\,supp}\theta(\pm\xi^0)$ is the plane $\xi^0 = 0$ and $\operatorname{sing\,supp}D_W(\pm\xi)$ the cone ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 2); they meet only at $\xi = 0$, so the products are defined on $\mathbb R^4\setminus\{0\}$ by [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2. Near a point with $\xi^0 = 0$, $\boldsymbol\xi \ne 0$ (spacelike) no product is needed: there $D_W(\xi) = D_W(-\xi)$, since $D$ vanishes ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]]), and $\theta(\xi^0) + \theta(-\xi^0) = 1$, so $D_F = D_W(\xi)$, a smooth function.
>
> **Step 4** (the fundamental solution, and only one). For $t > 0$, $D_W(\xi) = iD(\xi) + D_W(-\xi)$; for $t < 0$ the slice is $D_W(-\xi)$. So, slice by slice, $D_F = \theta(\xi^0)iD + D_W(-\xi) = D_R + D_W(-\xi)$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1). $D_R$ is a fundamental solution ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]) and $D_W(-\xi)$ a homogeneous one ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]), so $(\partial^2 + m^2)D_F = -i\delta^4$. Two extensions that agree off the origin differ by $\sum c_\alpha\partial^\alpha\delta^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]); if both are fundamental solutions the difference is zero ([[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], 3). Part 2.
>
> ⚑ By-product: for time-ordered products of composite or interacting fields the extension across coincident points is not fixed by a free field equation, and the freedom $\sum c_\alpha\partial^\alpha\delta^4$ becomes the local ambiguity that renormalization fixes (QFT C7, planned).
>
> **What the derivation shows.**
> - The step functions of time ordering multiply distributions safely because the two-point function is smooth in time with spatial-distribution values; the only problematic point is $\xi = 0$, where the field equation settles it.
> - $D_F$, $D_R$ and the $i\varepsilon$ limit ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]) are the same distribution reached three ways.
> - By power counting the same extension is singled out without the field equation: $D_W$ scales like $|\xi|^{-2}$ at the origin, every $\partial^\alpha\delta^4$ at least like $|\xi|^{-4}$, so the slice products are the only extensions no more singular than $D_W$ (scaling degree $2 < 4$; as in [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], quoted).

^der-c2b-6-4

*Uses:* [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

> [!theorem] Theorem §C2b.6.5: The Free Schwinger–Dyson Equation
> For distinct times $y_1^0, \dots, y_n^0$,
>
> $$
> (\partial_x^2 + m^2)\,T\{\phi(x)\phi(y_1)\cdots\phi(y_n)\} = -i\sum_{k=1}^n\delta^4(x - y_k)\,T\{\phi(y_1)\cdots\widehat{\phi(y_k)}\cdots\phi(y_n)\},
> $$
>
> the hat marking the omitted field. For $n = 1$ the vacuum expectation value is $(\partial^2 + m^2)D_F = -i\delta^4$: the Feynman propagator is a Green's function.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7 (Derivations "$D_F$ is a Green's function: the operator derivation", "Generalization: the free Schwinger–Dyson equation") · PHY 513, Problem Set 4, Problem 4(c)*

^thm-c2b-6-5

> [!derivation]- Derivation
> **Step 1** ($n = 1$: spatial derivatives and mass). Write $D_F = \theta(t)D_W(\xi) + \theta(-t)D_W(-\xi)$, all derivatives with respect to $x$. $-\nabla^2 + m^2$ does not touch the step functions: $(-\nabla^2 + m^2)D_F = \theta(t)(-\nabla^2 + m^2)D_W(\xi) + \theta(-t)(-\nabla^2 + m^2)D_W(-\xi)$.
>
> **Step 2** (first time derivative). By the product rule and $\partial_t\theta(\pm t) = \pm\delta(t)$ ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], 2; the product rule holds slice by slice because $D_W$ is smooth in $t$ with values in $\mathcal S'(\mathbb R^3)$, [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3):
>
> $$
> \partial_0D_F = \delta(t)\bigl[D_W(\xi) - D_W(-\xi)\bigr] + \theta(t)\,\partial_0D_W(\xi) + \theta(-t)\,\partial_0D_W(-\xi) .
> $$
>
> The bracket is $\langle[\phi(x), \phi(y)]\rangle$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]), and $\delta(t)$ evaluates it at equal times (a smooth function of $t$ times $\delta(t)$ is its value at $0$ times $\delta(t)$, here the spatial distribution $D(0, \cdot)$, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], 2), where it vanishes ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]). Dropped: this contact term, because $[\phi, \phi]_{\text{equal time}} = 0$.
>
> **Step 3** (second time derivative). Differentiate the two surviving terms:
>
> $$
> \partial_0^2D_F = \delta(t)\bigl[\partial_0D_W(\xi) - \partial_0D_W(-\xi)\bigr] + \theta(t)\,\partial_0^2D_W(\xi) + \theta(-t)\,\partial_0^2D_W(-\xi) .
> $$
>
> Now the bracket is $\partial_{x^0}\langle[\phi(x), \phi(y)]\rangle = \langle[\pi(x), \phi(y)]\rangle$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]), which at equal times is $-[\phi(y), \pi(x)] = -i\delta^3(\mathbf x - \mathbf y)$. The contact term is $\delta(t)(-i)\delta^3 = -i\delta^4(x - y)$ (a product of distributions in different variables, $\delta(t)\otimes\delta^3(\boldsymbol\xi) = \delta^4(\xi)$), and it is not zero.
>
> ⚑ By-product: the source of the Green's function is produced entirely by the switch between the two homogeneous pieces at $t = 0$, with strength set by the canonical commutator → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-2|Remark: The field equation inside time-ordered products]].
>
> **Step 4** (assemble, $n = 1$). With $\partial^2 = \partial_0^2 - \nabla^2$, Steps 1 and 3 give $(\partial^2 + m^2)D_F = -i\delta^4(x - y) + \theta(t)(\partial^2 + m^2)D_W(\xi) + \theta(-t)(\partial^2 + m^2)D_W(-\xi)$, and the last two vanish ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]). (Taking both time derivatives at once produces $\delta'(t)$, reduced to this by $\delta'(t)F(t) = F(0)\delta'(t) - F'(0)\delta(t)$; that is the route of Problem Set 4, Problem 4(c).)
>
> **Step 5** (general $n$, between the times). As a function of $x^0$, in each interval between consecutive $y_k^0$ the time-ordered product has $\phi(x)$ in a fixed slot, and there $(\partial_x^2 + m^2)$ acts on $\phi(x)$ alone and gives zero ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]).
>
> **Step 6** (general $n$, at $x^0 = y_k^0$). Across that point the product changes from $\cdots\phi(x)\phi(y_k)\cdots$ to $\cdots\phi(y_k)\phi(x)\cdots$. By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], 4, the first time derivative produces $\delta(x^0 - y_k^0)\cdots[\phi(x), \phi(y_k)]\cdots = 0$, and the second $\delta(x^0 - y_k^0)\cdots[\pi(x), \phi(y_k)]\cdots = -i\delta^4(x - y_k)\cdots$. The commutator is a $c$-number, so it leaves the remaining fields in time order. Summing over $k$ gives the formula.
>
> **What the derivation shows.**
> - The field equation holds inside time-ordered products except at coincident points, where the canonical commutator supplies delta functions.
> - With interactions the right side gains the interaction's contribution: the Schwinger–Dyson equations (QFT C10–C11, planned).

^der-c2b-6-5

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]

> [!remark] Remark: The field equation inside time-ordered products
> Theorem §C2b.6.5 says that the field equation holds inside time-ordered products except at coincident points, where delta functions of strength fixed by the canonical commutator replace it. This is the operator counterpart of Theorem §C2b.5.3, 1, where the same source appeared when $\partial^2 + m^2$ cancelled the denominator. With interactions the right side gains the interaction's contribution to the equation of motion: the Schwinger–Dyson equations, one route into perturbation theory (QFT C10–C11, planned).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7*

^rem-c2b-6-2

> [!theorem] Theorem §C2b.6.6: Contractions: Normal Ordering against Time Ordering
> With $\phi = \phi^+ + \phi^-$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]) and normal ordering $:\;:$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]),
>
> $$
> \phi(x)\phi(y) = \,:\!\phi(x)\phi(y)\!:\, + D_W(x - y), \qquad T\{\phi(x)\phi(y)\} = \,:\!\phi(x)\phi(y)\!:\, + D_F(x - y) .
> $$
>
> $D_F$ is the number that separates the time-ordered from the normal-ordered product: the **contraction** of the two fields.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7 (Derivation "Normal ordering and time ordering: a first look at Wick's theorem") · Yu §6.3, eqs. (6.132)–(6.133)*

^thm-c2b-6-6

> [!derivation]- Derivation
> **Step 1** (expand). $\phi(x)\phi(y) = \phi^+(x)\phi^+(y) + \phi^+(x)\phi^-(y) + \phi^-(x)\phi^+(y) + \phi^-(x)\phi^-(y)$.
>
> **Step 2** (normal order). Three terms already have every $\phi^-$ to the left of every $\phi^+$. The second does not: $\phi^+(x)\phi^-(y) = \phi^-(y)\phi^+(x) + [\phi^+(x), \phi^-(y)]$. So $\phi(x)\phi(y) = \,:\!\phi(x)\phi(y)\!:\, + [\phi^+(x), \phi^-(y)]$.
>
> **Step 3** (the commutator is a number). $[\phi^+(x), \phi^-(y)] = \int\frac{d^3p\,d^3q}{(2\pi)^6\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}[a_{\mathbf p}, a_{\mathbf q}^\dagger]e^{-ip\cdot x + iq\cdot y}$, a $c$-number (a distribution in $(x, y)$, the kernel of [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]). Take vacuum expectation values of Step 2: $\langle0|:\!\cdots\!:|0\rangle = 0$ because $\phi^+|0\rangle = 0 = \langle0|\phi^-$, so the number is $\langle0|\phi(x)\phi(y)|0\rangle = D_W(x - y)$.
>
> **Step 4** (time order). For boson fields $:\!\phi(x)\phi(y)\!:\, = \,:\!\phi(y)\phi(x)\!:$. Apply Step 2 to $\phi(x)\phi(y)$ for $x^0 > y^0$ and to $\phi(y)\phi(x)$ for $y^0 > x^0$: $T\{\phi(x)\phi(y)\} = \,:\!\phi\phi\!:\, + \theta(t)D_W(\xi) + \theta(-t)D_W(-\xi) = \,:\!\phi\phi\!:\, + D_F$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]).
>
> ⚑ By-product: at coincident points the same identity turns the zero-point energy into $D_W$ at zero separation → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]].
>
> **What the derivation shows.**
> - A product of free fields is its normal-ordered part plus the vacuum two-point function; this is the $n = 2$ case of Wick's theorem (QFT C6, planned).

^der-c2b-6-6

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]

> [!theorem] Theorem §C2b.6.7: Normal Ordering Removes the Coincident Singularity
> 1. Between finite-particle wave-packet states the matrix elements of $:\!\phi(x)\phi(y)\!:$ are smooth functions of $(x, y)$, including $x = y$. So $:\!\phi(x)^2\!:$ is defined, and for $f \in \mathcal S(\mathbb R^4)$, $:\!\phi^2\!:(f)\,|0\rangle$ is a normalizable two-particle state.
> 2. In $\phi(x)\phi(y) = \,:\!\phi(x)\phi(y)\!:\, + D_W(x - y)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]) the whole coincident singularity sits in the $c$-number $D_W$, which has no value at $x = y$ ($0 \in \operatorname{sing\,supp}D_W$, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]]; [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3). So $\phi(x)^2$ is undefined, and $:\!\phi(x)^2\!: = \lim_{y\to x}\bigl[\phi(x)\phi(y) - D_W(x - y)\bigr]$ ([[§CA.2 Generalized Functions#^rem-ca-2-2|Remark: Point splitting]]).
> 3. $T\{\phi(x)\phi(y)\} = \,:\!\phi(x)\phi(y)\!:\, + D_F(x - y)$ is an operator-valued distribution in $(x, y)$: θ multiplies the smooth matrix elements of the normal-ordered part, and the $c$-number part is [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2 ("Why this matters beyond tidiness"), §6.7 (the zero-point energy as the Wightman function at coincident points) · stated here as distributions (standard: Reed & Simon II, §X.7, Wick powers)*

^thm-c2b-6-7

> [!derivation]- Derivation
> **Step 1** (one-particle wave functions). For a wave packet $|g\rangle = \int\frac{d^3p}{(2\pi)^3}g(\mathbf p)a_{\mathbf p}^\dagger|0\rangle$, $g \in \mathcal S(\mathbb R^3)$, let $\psi_g(x) \equiv \langle0|\phi(x)|g\rangle = \int\frac{d^3p}{(2\pi)^3}\frac{g(\mathbf p)}{\sqrt{2E_{\mathbf p}}}e^{-ip\cdot x}$. The integral and all its $x$-derivatives converge absolutely, so $\psi_g$ is smooth ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], 2).
>
> **Step 2** (matrix elements). With $\phi = \phi^+ + \phi^-$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]]), $:\!\phi(x)\phi(y)\!: = \phi^-(x)\phi^-(y) + \phi^-(x)\phi^+(y) + \phi^-(y)\phi^+(x) + \phi^+(x)\phi^+(y)$. Since $\phi^+|0\rangle = 0 = \langle0|\phi^-$: $\langle0|:\!\phi(x)\phi(y)\!:|0\rangle = 0$; $\langle h|:\!\phi(x)\phi(y)\!:|g\rangle = \overline{\psi_h(x)}\psi_g(y) + \overline{\psi_h(y)}\psi_g(x)$; and $\langle0|:\!\phi(x)\phi(y)\!:|G\rangle = \langle0|\phi^+(x)\phi^+(y)|G\rangle$ for a two-particle packet $|G\rangle$, an absolutely convergent double mode integral with the Schwartz amplitude of $G$. For general finite-particle packets the matrix elements are finite sums of such terms. All are smooth in $(x, y)$, at $x = y$ too.
>
> **Step 3** (the Wick square on the vacuum). $:\!\phi^2\!:(f)|0\rangle = \int d^4x\,f(x)\phi^-(x)\phi^-(x)|0\rangle = \int\frac{d^3p\,d^3q}{(2\pi)^6}\frac{\tilde f(p + q)}{\sqrt{2E_{\mathbf p}2E_{\mathbf q}}}a_{\mathbf p}^\dagger a_{\mathbf q}^\dagger|0\rangle$, with $p^0 = E_{\mathbf p}$, $q^0 = E_{\mathbf q}$. Its squared norm, by the two pairings of $\langle0|a\,a\,a^\dagger a^\dagger|0\rangle$ ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]), is $2\int\frac{d^3p\,d^3q}{(2\pi)^6\,2E_{\mathbf p}2E_{\mathbf q}}|\tilde f(p + q)|^2$. The four-vector $p + q$ has time component $E_{\mathbf p} + E_{\mathbf q} \ge |\mathbf p| + |\mathbf q|$, so $|\tilde f(p + q)| \le C_N(1 + |\mathbf p| + |\mathbf q|)^{-N}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], 1) and the integral converges. Part 1.
>
> **Step 4** (where the singularity is). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], $\langle\Psi_1|\phi(x)\phi(y)|\Psi_2\rangle = \langle\Psi_1|:\!\phi(x)\phi(y)\!:|\Psi_2\rangle + D_W(x - y)\langle\Psi_1|\Psi_2\rangle$: a smooth function (Step 2) plus a $c$-number distribution. As $y \to x$ the first has a limit and the second has none: near $\xi = 0$, $D_W$ contains $\frac{1}{4\pi^2}\frac{1}{-\xi^2 + i0\,\xi^0}$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 3), and evaluating a distribution at a point of its singular support has no value ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 3). Subtracting $D_W(x - y)$ before the limit leaves the smooth function: point splitting. Part 2.
>
> ⚑ By-product: the subtracted $c$-number, differentiated and integrated over space, is the zero-point energy → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]].
>
> **Step 5** (time ordering). $:\!\phi(x)\phi(y)\!: = \,:\!\phi(y)\phi(x)\!:$, so $\theta(x^0 - y^0)$ and $\theta(y^0 - x^0)$ multiply the same smooth matrix elements and add to $1$ (θ times a smooth function, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1); the $c$-number parts add to $D_F$, defined by [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]. Part 3.
>
> **What the derivation shows.**
> - Normal ordering is the subtraction of exactly the singular $c$-number; the contraction $D_W$ (or $D_F$) is that $c$-number, singular at coincident points.
> - Wick powers need smearing in spacetime: the decay of $\tilde f(p + q)$ in the total energy is what makes Step 3 converge.
> - The same subtraction, with $(2\pi)^3\delta^3(\mathbf 0)$ in mode language, is the normal ordering of $H$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]).

^der-c2b-6-7

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-1|Theorem §CA.3.1]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^rem-ca-2-2|Remark: Point splitting]]

> [!theorem] Theorem §C2b.6.8: The Zero-Point Energy Is the Wightman Function at Coincident Points
> Splitting the products in $H$ ([[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]) by [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]] gives $H = \,:\!H\!:\, + \langle0|H|0\rangle$ with
>
> $$
> \langle0|H|0\rangle = \frac12\int d^3x\,\lim_{y\to x}\bigl(\partial_{x^0}\partial_{y^0} + \nabla_x\cdot\nabla_y + m^2\bigr)D_W(x - y) = V\int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2},
> $$
>
> the zero-point constant of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]. The limit $y \to x$ does not exist ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]]): at equal times with the damping $e^{-\varepsilon E_{\mathbf p}}$ the expression is finite for $\varepsilon > 0$ and diverges like $\varepsilon^{-4}$ as $\varepsilon \to 0^+$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7 (the zero-point energy as the Wightman function at coincident points); the $\varepsilon^{-4}$ rate derived here*

^thm-c2b-6-8

> [!derivation]- Derivation
> **Step 1** (point-split the Hamiltonian). At a common time $t$, $H = \int d^3x\,\bigl[\tfrac12\pi(x)^2 + \tfrac12\nabla\phi(x)\cdot\nabla\phi(x) + \tfrac12m^2\phi(x)^2\bigr]$ with $\pi = \partial_t\phi$ ([[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]). Write each product at one point as the limit of a product at two points $x$, $y$ with $y^0 = x^0$:
>
> $$
> H = \frac12\int d^3x\,\lim_{y\to x}\bigl(\partial_{x^0}\partial_{y^0} + \nabla_x\cdot\nabla_y + m^2\bigr)\,\phi(x)\phi(y) .
> $$
>
> **Step 2** (separate the $c$-number). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], $\phi(x)\phi(y) = \,:\!\phi(x)\phi(y)\!:\, + D_W(x - y)$. The derivatives act term by term (derivatives of operator-valued distributions, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]); the normal-ordered term has smooth matrix elements with a limit at $y = x$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], 1) and gives $:\!H\!:$; its vacuum expectation value is $0$ (Step 2 of Derivation §C2b.6.7). The $c$-number term, multiplied by $\langle0|0\rangle = 1$, is $\langle0|H|0\rangle$, the formula's first expression.
>
> **Step 3** (one mode). $D_W(x - y) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-ip\cdot(x - y)}$, $p^0 = E_{\mathbf p}$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]). On $e^{-ip\cdot(x - y)} = e^{-iE(x^0 - y^0) + i\mathbf p\cdot(\mathbf x - \mathbf y)}$: $\partial_{x^0} \to -iE$, $\partial_{y^0} \to +iE$, product $(-iE)(iE) = E^2$; $\nabla_x \to i\mathbf p$, $\nabla_y \to -i\mathbf p$, product $(i\mathbf p)\cdot(-i\mathbf p) = \mathbf p^2$; and $m^2$. So each mode contributes $\frac{E^2 + \mathbf p^2 + m^2}{2E}\,e^{-ip\cdot(x - y)} = \frac{2E^2}{2E}\,e^{-ip\cdot(x - y)} = E\,e^{-ip\cdot(x - y)}$, using $E^2 = \mathbf p^2 + m^2$.
>
> **Step 4** (equal times, regulated). At $y^0 = x^0$ the time phase is $1$; replace it by $e^{-\varepsilon E}$, i.e. take $y^0 = x^0 + i\varepsilon$, the damping of [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], Step 5. Then at $\mathbf y = \mathbf x$
>
> $$
> \langle0|H|0\rangle_\varepsilon = \frac12\int d^3x\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,e^{-\varepsilon E_{\mathbf p}} = V\int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\,e^{-\varepsilon E_{\mathbf p}},
> $$
>
> with $\int d^3x = V$ for the field in a box ([[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]]). The $\mathbf p$-integral converges for $\varepsilon > 0$.
>
> ⚑ By-product: the integrand does not depend on $\mathbf x$, so the energy density $\langle0|\mathcal H|0\rangle_\varepsilon$ is a constant, and the total is proportional to the volume.
>
> **Step 5** (the rate of divergence). For $m = 0$, $E = |\mathbf p| = p$ and $d^3p = 4\pi p^2dp$: $\int\frac{d^3p}{(2\pi)^3}\frac p2e^{-\varepsilon p} = \frac{4\pi}{2(2\pi)^3}\int_0^\infty p^3e^{-\varepsilon p}dp = \frac{1}{4\pi^2}\cdot\frac{3!}{\varepsilon^4} = \frac{3}{2\pi^2\varepsilon^4}$. For $m > 0$, $p \le E \le p + m$ gives $e^{-\varepsilon m}\,p\,e^{-\varepsilon p} \le E\,e^{-\varepsilon E} \le (p + m)\,e^{-\varepsilon p}$, so the integral lies between $e^{-\varepsilon m}\frac{3}{2\pi^2\varepsilon^4}$ and $\frac{3}{2\pi^2\varepsilon^4} + \frac{m}{4\pi^2}\cdot\frac{2}{\varepsilon^3}$, and diverges like $\varepsilon^{-4}$ as well.
>
> **Step 6** (compare). At $\varepsilon \to 0^+$ the expression is $V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$, which with $(2\pi)^3\delta^3(\mathbf 0) = V$ is the constant $E_0$ of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], found there by reordering $a\,a^\dagger$ in mode form.
>
> **What the derivation shows.**
> - Normal ordering $H$ ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]) is the subtraction of $D_W$ at coincident points, the point-splitting of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]] applied to $H$.
> - Assumptions: the field in a box (for $V$) and the damping $e^{-\varepsilon E}$; the divergence is ultraviolet, $\varepsilon^{-4}$ in four dimensions.
> - Used next: [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|Remark: One mechanism, two products]].

^der-c2b-6-8

*Uses:* [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]

> [!remark] Remark: One mechanism, two products
> The zero-point constant of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]] is the one that normal ordering drops ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]]). It is infinite because $D_W$ is singular on the light cone, like $-1/4\pi^2\xi^2$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]]), and coincident points are as lightlike as it gets. The zero-point constant and the Feynman propagator are one mechanism, applied once to an equal-time product at one point and once to a time-ordered product at two. With $n$ fields the same reasoning gives Wick's theorem: a time-ordered product is its normal-ordered part plus all ways of pairing fields into contractions $D_F$ (QFT C6, planned; PS §4.3; Yu §6.3).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.7*

^rem-c2b-6-3

## The $i\varepsilon$ prescription

> [!theorem] Theorem §C2b.6.9: The $i\varepsilon$ Prescriptions
> Keeping the $p^0$ integral on the real axis and moving the poles off it is equivalent to deforming the contour. With $\varepsilon \to 0^+$ at the end (a limit in $\mathcal S'$, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]),
>
> $$
> \tilde D_F = \frac{i}{p^2 - m^2 + i\varepsilon}, \quad \tilde D_{\bar F} = \frac{i}{p^2 - m^2 - i\varepsilon}, \quad \tilde D_R = \frac{i}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2} = \frac{i}{p^2 - m^2 + i\varepsilon\operatorname{sgn}p^0}, \quad \tilde D_A = \frac{i}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2} .
> $$
>
> $\tilde D_F$ depends on $p$ only through $p^2$ ($m^2 \to m^2 - i\varepsilon$) and is manifestly Lorentz invariant; $\tilde D_R$ is invariant under orthochronous transformations.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.9 · PHY 513 Lecture 6, "Deforming Integrand: the Feynman Propagator", "Relativistic Form of Feynman Propagator" · PS §2.4, eq. (2.59) · Yu §6.4.1, eq. (6.210)*

^thm-c2b-6-9

> [!derivation]- Derivation
> **Step 1** (moving a pole is moving the contour). For a pole at real $E$: the real axis with the pole moved to $E - i\varepsilon$ can be deformed, without crossing it, into a contour that passes above $E$; as $\varepsilon \to 0^+$ this is the contour above the pole ([[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]]; as distributions, Step 3 of Derivation §C2b.5.4). Passing below is moving the pole up.
>
> **Step 2** (Feynman: below $-E$, above $+E$). Move $+E \to E - i\varepsilon$ and $-E \to -E + i\varepsilon$, i.e. poles at $\pm(E - i\varepsilon)$. The denominator is $(p^0)^2 - (E - i\varepsilon)^2 = (p^0)^2 - E^2 + 2iE\varepsilon - \varepsilon^2$. Dropped: $\varepsilon^2$, of higher order; and $2E\varepsilon \to \varepsilon$, since $E > 0$ and only the sign of the infinitesimal matters (precisely: the limits in $\mathcal S'$ coincide, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 3). With $(p^0)^2 - E^2 = p^2 - m^2$: $p^2 - m^2 + i\varepsilon$.
>
> **Step 3** (anti-Feynman). The mirror image: poles at $\pm(E + i\varepsilon)$, denominator $p^2 - m^2 - i\varepsilon$.
>
> **Step 4** (retarded: above both). Poles at $\pm E - i\varepsilon$, i.e. $(p^0 + i\varepsilon)^2 - E^2 = p^2 - m^2 + 2ip^0\varepsilon - \varepsilon^2 \to p^2 - m^2 + i\varepsilon\operatorname{sgn}p^0$ (the infinitesimal's sign is that of $p^0$; the limit in $\mathcal S'$ is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 2). *Advanced:* poles at $\pm E + i\varepsilon$, $(p^0 - i\varepsilon)^2 - E^2$.
>
> **Step 5** (invariance). $p^2$ is invariant. (As distributions: $\mathcal P\frac{1}{p^2 - m^2}$, $\delta(p^2 - m^2)$ and $\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ are invariant, [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1.) $\operatorname{sgn}p^0$ is invariant under $SO^+(1,3)$ for timelike $p$ ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]), and the infinitesimal matters only near the shell, where $p$ is timelike.
>
> ⚑ By-product: the Feynman prescription is the only one of the four that is a function of $p^2$ alone; it is the one that continues to Euclidean signature → [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]].
>
> **What the derivation shows.**
> - "$i\varepsilon$" is a contour in disguise; no contour needs to be drawn once the poles are moved.
> - The differences between prescriptions are delta functions on the shell (Theorem §C2b.6.11).

^der-c2b-6-9

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-7|Theorem §CA.4.7]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]

![[ph-qft-c2-6-2.svg]]
*The prescriptions as shifted poles with the contour on the real axis: (a) Feynman, poles in the second and fourth quadrants; (b) retarded, both poles below (advanced and anti-Feynman are the mirror images). (c) Because the first and third quadrants are free of Feynman poles, the real axis can be rotated counterclockwise onto $p^0 = ip_4$ (Theorem §C2b.7.1). Adapted from the user's PHY 513 notes, Figs. 6.5–6.6.*

> [!theorem] Theorem §C2b.6.10: The $i\varepsilon$ Prescription Is a Limit in 𝒮′
> 1. For $\varepsilon > 0$, $\tilde D_F^\varepsilon(p) = i/(p^2 - m^2 + i\varepsilon)$ is smooth and bounded by $1/\varepsilon$, a tempered distribution. As $\varepsilon \to 0^+$, $\tilde D_F^\varepsilon \to i\,\mathcal P\frac{1}{p^2 - m^2} + \pi\,\delta(p^2 - m^2)$ in $\mathcal S'(\mathbb R^4)$: Sokhotski–Plemelj on $p^2 - m^2$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 1). For $\tilde D_R$, $\tilde D_A$ the delta term carries $\pm\operatorname{sgn}(p^0)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 2); $\tilde D_{\bar F}$ is the complex conjugate.
> 2. The limit does not depend on how the infinitesimal is written: $\varepsilon$, $2E_{\mathbf p}\varepsilon$, or poles at $\pm(E_{\mathbf p} - i\varepsilon)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 3).
> 3. The transform commutes with the limit ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2): $D_F[f] = \lim_{\varepsilon\to0^+}\int\frac{d^4p}{(2\pi)^4}\frac{i\,\tilde f(-p)}{p^2 - m^2 + i\varepsilon}$ for every test function $f$, and this is the contour's $D_F$. The four-dimensional integral $\int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip\cdot\xi}}{p^2 - m^2 + i\varepsilon}$ converges absolutely for no $\xi$; "$\varepsilon \to 0^+$ at the end" means this limit.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.9 (Derivation "The distributional version: Sokhotski–Plemelj"; "only the sign of the infinitesimal matters") · stated here as a limit in $\mathcal S'$*

^thm-c2b-6-10

> [!derivation]- Derivation
> **Step 1** (finite $\varepsilon$). $\operatorname{Im}(p^2 - m^2 + i\varepsilon) = \varepsilon \ne 0$, so the denominator never vanishes on $\mathbb R^4$, the function is smooth, and $|\tilde D_F^\varepsilon| \le 1/\varepsilon$: a bounded function, hence a tempered distribution ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2). For the retarded form, $(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2 = (p^0)^2 - \varepsilon^2 - E_{\mathbf p}^2 + 2i\varepsilon p^0$ vanishes only if $p^0 = 0$ and $-\varepsilon^2 - E_{\mathbf p}^2 = 0$, which never happens.
>
> **Step 2** (the limit in $p$). At fixed $\mathbf p$, $(p^0)^2 - E^2 + i\varepsilon = (p^0 - E_\varepsilon)(p^0 + E_\varepsilon)$ with $E_\varepsilon = \sqrt{E^2 - i\varepsilon} = E - \frac{i\varepsilon}{2E} + O(\varepsilon^2)$: poles at $E - i\varepsilon'$ and $-E + i\varepsilon'$, $\varepsilon' > 0$. Partial fractions and [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]] give, in $p^0$,
>
> $$
> \frac{1}{(p^0)^2 - E^2 + i\varepsilon} \to \frac{1}{2E}\Bigl[\mathcal P\frac{1}{p^0 - E} - i\pi\delta(p^0 - E) - \mathcal P\frac{1}{p^0 + E} - i\pi\delta(p^0 + E)\Bigr] = \mathcal P\frac{1}{p^2 - m^2} - i\pi\,\delta(p^2 - m^2),
> $$
>
> using $\delta(p^2 - m^2) = [\delta(p^0 - E) + \delta(p^0 + E)]/2E$ ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2). The convergence is uniform enough in $\mathbf p$ to integrate against a test function in four variables; this is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 1. Multiplying by $i$: $i\,\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2)$. The retarded and advanced forms are [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 2. Part 1.
>
> **Step 3** (the form of the infinitesimal). [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 3: replacing $\varepsilon$ by $\varepsilon c(\mathbf p)$ with $c$ smooth and positive does not change the limit. $2E_{\mathbf p}\varepsilon$ and the poles at $\pm(E_{\mathbf p} - i\varepsilon)$ of Theorem §C2b.6.9 are such forms (the $\varepsilon^2$ terms do not change the side of the poles). Part 2.
>
> **Step 4** (back to position space). The transform is continuous on $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2), so the inverse transforms converge: $D_F^\varepsilon \to D_F$ in $\mathcal S'(\mathbb R^4)$. Moving the transform onto the test function ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), $D_F^\varepsilon[f] = \int\frac{d^4p}{(2\pi)^4}\tilde D_F^\varepsilon(p)\,\tilde f(-p)$, absolutely convergent for $\varepsilon > 0$ because $\tilde f$ is Schwartz.
>
> **Step 5** (it is the contour's $D_F$). At fixed $\mathbf p$ the limit of Step 2 is $\frac{i}{(p^0 - E + i0)(p^0 + E - i0)}$: $+i0$ at $+E$ (the Feynman contour passes above $+E$) and $-i0$ at $-E$ (it passes below $-E$). By [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], 1, this is the transform of the contour's $D_F$.
>
> **Step 6** (no pointwise integral). For fixed $\varepsilon$ the integrand of $\int d^4p\,e^{-ip\cdot\xi}/(p^2 - m^2 + i\varepsilon)$ decays only like $1/|p|^2$ in Euclidean directions, and $\int d^4p/|p|^2$ diverges; only the pairing with $\tilde f(-p)$ converges. Part 3.
>
> **What the derivation shows.**
> - "$i\varepsilon$" is a device for choosing a boundary value; it is removed at the end as a limit of distributions, never of numbers at fixed $\xi$, except where the result is a smooth function (off the light cone, [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]]).
> - The momentum-space $+i\varepsilon$ and the position-space $\xi^0 - i\varepsilon$ of [[§C2b.2 The Wightman Function#^thm-c2b-2-5|Theorem §C2b.2.5]] are the same positivity of energy, read on the two sides of the transform.

^der-c2b-6-10

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]

> [!theorem] Theorem §C2b.6.11: Differences on the Mass Shell
> As generalized functions of $p$,
>
> $$
> \tilde D_F - \tilde D_{\bar F} = 2\pi\,\delta(p^2 - m^2), \qquad \tilde D_R - \tilde D_A = 2\pi\operatorname{sgn}(p^0)\,\delta(p^2 - m^2), \qquad \tilde D_W(p) = 2\pi\,\theta(p^0)\,\delta(p^2 - m^2) .
> $$
>
> The homogeneous solutions that separate the Green's functions are built from the on-shell measure of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.9 (Derivation "The distributional version: Sokhotski–Plemelj")*

^thm-c2b-6-11

> [!derivation]- Derivation
> **Step 1** (Sokhotski–Plemelj). In the variable $s = p^2 - m^2$ (legitimate because $\partial_{p^0}(p^2 - m^2) = 2p^0 \ne 0$ on the shell for $m > 0$; the composed statement in four variables is [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 1), $\frac{1}{s \pm i\varepsilon} \to \mathcal P\frac1s \mp i\pi\delta(s)$ ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]), so $\frac{1}{s + i\varepsilon} - \frac{1}{s - i\varepsilon} \to -2\pi i\,\delta(s)$.
>
> **Step 2** ($F - \bar F$). Multiply by $i$: $i\cdot(-2\pi i)\delta(s) = 2\pi\delta(p^2 - m^2)$.
>
> **Step 3** ($R - A$). By [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] the infinitesimal is $\varepsilon\operatorname{sgn}p^0$ instead of $\varepsilon$, so the same steps ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 2) give $2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$.
>
> **Step 4** ($D_W$). This is [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], as a distribution [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]].
>
> **What the derivation shows.**
> - This is Theorem §C2b.5.3, 2 in momentum space: the differences live on the shell, $2\pi\delta(p^2 - m^2) = 2\pi[\theta(p^0) + \theta(-p^0)]\delta(p^2 - m^2)$ splitting into the transforms of $D_W(\xi)$ and $D_W(-\xi)$, whose sum is $D_1$.

^der-c2b-6-11

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]

> [!remark] Remark: Preview: the propagator as a Gaussian covariance
> In the path integral (QFT C11, planned; PS §9.1–9.2; Yu §11.1–11.2) time-ordered vacuum correlators are averages over field histories, $\langle0|T\{\phi(x)\phi(y)\}|0\rangle = \int\mathcal D\phi\,\phi(x)\phi(y)e^{iS}/\int\mathcal D\phi\,e^{iS}$, with $S = \frac12\int\phi(-\partial^2 - m^2)\phi$. In momentum space this is a Gaussian with kernel $K = p^2 - m^2$, which converges only with a damping $e^{-\frac\varepsilon2\int\phi^2}$; its covariance is then $i(K + i\varepsilon)^{-1} = \tilde D_F$. The $i\varepsilon$ prescribed here becomes the condition for the integral to exist, time ordering is produced rather than imposed, and with $t = -i\tau$ the weight becomes $e^{-S_E}$, whose covariance is $D_E$. Choosing the vacuum as initial and final state selects the Feynman inverse of the Klein–Gordon operator (the second variation of the action, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^rem-c1b-2-8|§C1b.2, Remark: The second variation is the operator whose inverse is the propagator]]), not the retarded one: contours are boundary conditions once more. The integral of a total derivative gives $(\partial^2 + m^2)D_F = -i\delta^4$ in one line, the free Schwinger–Dyson equation.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.13 (Principle "Looking ahead: the path integral (Lectures 23–24)")*

^rem-c2b-6-4

> [!remark]- Connections
> - The $\pm i\varepsilon$ as boundary conditions has a nonrelativistic twin: the outgoing and incoming resolvents $(E - H_0 \pm i\varepsilon)^{-1}$ of scattering theory, whose $k$-plane contour is closed exactly as here ([[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^thm-c10-1-3|QM Theorem §C10.1.3]], [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^rem-c10-1-2|QM Remark: Why the sign of iε matters]]), and the causal energy transform of the propagator ([[§C4.1 Propagators#^thm-c4-1-7|QM Theorem §C4.1.7]]).
> - The contraction $D_F$ is the building block of Wick's theorem and of every internal line of a Feynman diagram (QFT C6–C7, planned); for spinor and vector fields the numerator changes but the $i\varepsilon$ does not (spinor: [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], numerator [[§C5a.7 Normalization, Spin Sums and Helicity#^thm-c5a-7-7|Theorem §C5a.7.7]]; vector: [[§C4.9 Vector-Field Propagators#^thm-c4-9-3|Theorem §C4.9.3]] massive, [[§C4.9 Vector-Field Propagators#^thm-c4-9-6|Theorem §C4.9.6]] photon in the Feynman gauge; Yu eq. (6.262)).
> - Normal ordering ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]) and time ordering meet in Theorem §C2b.6.6; the zero-point energy is the same divergence as the light-cone singularity of $D_W$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]]).
> - The anti-Feynman function ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]]) is the Feynman function of the time-reversed ordering; its $-i\varepsilon$ reappears as the complex conjugate amplitude in the Schwinger–Keldysh (closed-time-path) formalism and on the far side of Cutkosky cuts (QFT C7, planned).
> - [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]] (products with disjoint singular supports) and [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]] (θ·δ and δ at its singular point have no value) say which products of time ordering exist: $\theta(\xi^0)D_W$ away from the origin, but not $D_W(0)$ or $\phi(x)^2$.
> - [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]] and [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]] (point-supported distributions; fundamental solutions that agree off a point) fix the extension of $D_F$ across $\xi = 0$ and name the contact-term ambiguity.
> - [[§CA.2 Generalized Functions#^rem-ca-2-2|Remark: Point splitting]] and [[§CA.2 Generalized Functions#^thm-ca-2-9|Theorem §CA.2.9]] (the box) are the two regularizations of the coincident product: normal ordering subtracts $D_W(x - y)$ (Theorem §C2b.6.7), the box turns $\int d^3x$ into $V$.
> - [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]] (Sokhotski–Plemelj, on $p^0$ and on $p^2 - m^2$) make the $i\varepsilon$ a distributional limit and give the on-shell differences; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]] carries the limit to position space.
> - [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]] ($\theta' = \delta$) and [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]] (limits) are the calculus of the contact terms and of the $\varepsilon \to 0^+$ limits at fixed $\mathbf p$.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] (relabelling) and [[§CA.2 Generalized Functions#^def-ca-2-5|Def. §CA.2.5]] (reflection, invariance) turn the negative-frequency term into $D_W(-\xi)$ and make evenness and Lorentz invariance of $D_F$ statements about distributions.
> - With $N$ fields the Feynman propagator becomes the matrix $i(p^2\mathbb 1 - M^2 + i\varepsilon)^{-1}$, a sum of the propagators of Theorem §C2b.6.2 over the mass eigenstates ([[§R1.3 Diagonalization into N Free Klein–Gordon Fields#^thm-r1-3-4|Thesis Thm. §R1.3.4]]). As a function of $p^2$ it is the resolvent of the mass matrix, and the $i\varepsilon$ is the $i0$ of Stieltjes inversion, which recovers the spectrum of a random mass matrix ([[§R3.4 The Semicircle Law II꞉ Stieltjes Transform and Coulomb Gas#^rem-r3-4-1|Thesis §R3.4, Remark]], [[§R3.4 The Semicircle Law II꞉ Stieltjes Transform and Coulomb Gas#^thm-r3-4-3|Thesis Thm. §R3.4.3]]).
