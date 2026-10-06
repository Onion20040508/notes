---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C2b
section: C2b.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C2b.4 Microcausality and the Commutator Function]] · ↑ [[· C2b Two-Point Functions, Causality and Propagators]] · [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription]] →

*Sources: the user's PHY 513 notes, Ch. 6 §§6.1–6.4, 6.6, 6.8 and Ch. 5 §5.7 · PHY 513 Lecture 6 (Larsen, 21 Sep 2026), Parts A–B · Peskin & Schroeder §2.4, pp. 29–31 · PHY 513, Problem Set 4, Problem 0.*

How does a free field respond to a source, $(\partial^2 + m^2)\phi = j$? One solves the equation once, with a delta function on the right, and the answer is a Green's function. Fourier transformation makes this a division by $m^2 - p^2$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]]), which is impossible on the mass shell; the integral needs a contour in the complex $p^0$-plane ([[§CA.4 Contour Integration#^thm-ca-4-9|Theorem §CA.4.9]], [[P2 Green's Functions by Contour Integration|P2]]), and the choice of contour is the choice of boundary condition. The first contour worked out is the retarded one, and the retarded function is the causal commutator of [[§C2b.4 Microcausality and the Commutator Function|§C2b.4]].

*Conventions* ([[Larsen PHY 513]]): Green's functions are normalized by $(\partial^2 + m^2)D_C = -i\delta^4$ (PS), so that $D_F = \langle0|T\{\phi\phi\}|0\rangle$ with no prefactor and $\tilde D_F = i/(p^2 - m^2 + i\varepsilon)$; Fourier conventions as in [[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]; $\xi = x - y$, $t = \xi^0$, $E = E_{\mathbf p}$.

## Sources and Green's functions

> [!model] Model §C2b.5.1: Scalar Field with a Classical Source
> A real scalar field coupled to a prescribed real function $j(x)$, smooth and nonzero only for a finite time:
>
> $$
> \mathcal L = \tfrac12(\partial_\mu\phi)^2 - \tfrac12m^2\phi^2 + j\phi, \qquad (\partial^2 + m^2)\,\phi(x) = j(x) .
> $$
>
> *Assumptions:* $j$ is external and classical, prepared in the laboratory; it acts on the field, and the field does not act back on it. (Later the source is itself made of fields: interactions, QFT C6, planned.)
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.1 · PHY 513 Lecture 6, Part A · PS §2.4, eqs. (2.61)–(2.62)*

^mod-c2b-5-1

> [!definition] Definition §C2b.5.1: Green's Function of the Klein–Gordon Operator
> A **Green's function** $D_C$ solves
>
> $$
> (\partial_x^2 + m^2)\,D_C(x - y) = -i\,\delta^4(x - y) .
> $$
>
> Then for every source $\phi(x) = \phi_0(x) + i\int d^4y\,D_C(x - y)\,j(y)$, with $\phi_0$ any homogeneous solution, solves $(\partial^2 + m^2)\phi = j$. The label $C$ names the boundary condition, equivalently the contour of [[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]].
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.1 · PHY 513 Lecture 6, Part A · PS §2.4, eq. (2.56)*

^def-c2b-5-1

> [!remark] Remark: What a Green's "function" is, and why it is not unique
> *Check:* $\partial_x^2 + m^2$ acts on $x$ while the integral is over $y$, so it passes inside and gives $i\cdot(-i)\int d^4y\,\delta^4(x - y)j(y) = j(x)$: solving once with a delta function solves every source. (For a test-function source this is [[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]]: the derivative falls on $j$, and the result is smooth.) In the language of [[§CA.2 Generalized Functions#^def-ca-2-2|Def. §CA.2.2]], the sources of physics are test functions, and what is defined is the *linear map* $j \mapsto \phi$; "$D_C(x - y)$" is its kernel, not a function with values ([[§CA.2 Generalized Functions#^rem-ca-2-3|Remark: What the language buys in field theory]]). Adding a homogeneous solution to $D_C$ gives another Green's function: a differential equation has no unique solution without boundary conditions, so there is one map, and one kernel, per boundary condition (Problem Set 4, Problem 0). The factor $-i$ is PS's: Problem Set 4 writes $(-\Delta)G = \delta$ with $D_C = -iG$. (Its "$-\Delta = -\partial_\mu\partial^\mu + m^2$" has the sign of $\partial^2$ reversed for the metric $(+, -, -, -)$; the Klein–Gordon operator is $\partial_\mu\partial^\mu + m^2$.)
>
> *Source: the user's PHY 513 notes, Ch. 6 §§6.1–6.2 · PHY 513, Problem Set 4, Problem 0*

^rem-c2b-5-1

> [!theorem] Theorem §C2b.5.2: Free Fields Live on the Mass Shell
> If $(\partial^2 + m^2)f = 0$, the transform of $f$ is supported on $p^2 = m^2$, $\tilde f(p) = 2\pi\,\delta(p^2 - m^2)\,g(p)$, and
>
> $$
> f(x) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl[g(p)\,e^{-ip\cdot x} + g(-p)\,e^{ip\cdot x}\Bigr]_{p^0 = E_{\mathbf p}} ,
> $$
>
> the mode expansion, with $g(p) = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}$ for the free field. A Green's function, by contrast, has $\tilde D_C(p) = i/(p^2 - m^2)$ wherever $p^2 \ne m^2$: it lives off the shell.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.3 (Principle "Free fields live on the mass shell"), §6.4 · PS §2.4, eqs. (2.57)–(2.58)*

^thm-c2b-5-2

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
> **Step 5** (compare). Against [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], $g(p)/2E_{\mathbf p} = a_{\mathbf p}/\sqrt{2E_{\mathbf p}}$, so $g(p) = \sqrt{2E_{\mathbf p}}\,a_{\mathbf p}$; reality of $f$ gives $g(-p) = \overline{g(p)}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 4), here $\sqrt{2E}\,a^\dagger_{\mathbf p}$.
>
> **Step 6** (a Green's function). The same rule turns $(\partial^2 + m^2)D_C = -i\delta^4$ into $(m^2 - p^2)\tilde D_C = -i$ (with $\tilde\delta^4 = 1$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 3), so $\tilde D_C = i/(p^2 - m^2)$ wherever $p^2 \ne m^2$.
>
> ⚑ By-product: on the shell the equation does not determine $\tilde D_C$; the freedom is exactly a free field, i.e. a homogeneous solution → [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]].
>
> **What the derivation shows.**
> - The three-dimensional mode expansions are four-dimensional transforms restricted to the shell, and the invariant measure $d^3p/2E_{\mathbf p}$ is what the shell leaves behind.
> - A free field has no off-shell Fourier components; a Green's function must have them, and that is where the difficulty is.

^der-c2b-5-2

*Uses:* [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-1|EM Theorem §B1.2.1]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]

> [!definition] Definition §C2b.5.2: The Green's Function of a Contour
> Let $C$ be a contour in the complex $p^0$-plane that follows the real axis from $-\infty$ to $+\infty$ except near $p^0 = \pm E_{\mathbf p}$, each of which it passes above or below. Then
>
> $$
> D_C(\xi) \equiv \int\frac{d^3p}{(2\pi)^3}\,e^{i\mathbf p\cdot\boldsymbol\xi}\int_C\frac{dp^0}{2\pi}\,\frac{i\,e^{-ip^0\xi^0}}{(p^0)^2 - E_{\mathbf p}^2} .
> $$
>
> Without a contour, $\int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip\cdot\xi}}{p^2 - m^2}$ means nothing: $1/(p^0 \mp E_{\mathbf p})$ is not integrable at the pole.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.4 (eq. (DCdef)) · PHY 513 Lecture 6, "Important Mathematical Limitation"*

^def-c2b-5-2

> [!remark] Remark: The pole problem; two problems that are one
> Unlike every integral of [[§C2a.2 Mode Expansion and the Mode Algebra|§C2a.2]]–[[§C2b.4 Microcausality and the Commutator Function|§C2b.4]], this one is four-dimensional: $p^0$ is now a variable, not $E_{\mathbf p}$ ([[§C2b.1 Heisenberg Fields#^rem-c2b-1-2|Remark: What is covariant and what is not yet]]), and the integrand blows up exactly at the energy one "knows in one's heart" is the right one. Two problems were swept under the rug: one cannot divide by $p^2 - m^2$ on the shell, and one cannot solve a differential equation without boundary conditions. Theorem §C2b.5.3 shows they are the same problem. The lecture's insistence is worth keeping: without a $C$, the expression is not yet anything.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.4 · PHY 513 Lecture 6*

^rem-c2b-5-2

> [!theorem] Theorem §C2b.5.3: Contours Are Boundary Conditions
> 1. For every contour $C$ that passes the two poles, $(\partial^2 + m^2)D_C = -i\delta^4$.
> 2. Two such contours give Green's functions that differ by a homogeneous solution built from the on-shell waves $e^{\mp iE_{\mathbf p}\xi^0 + i\mathbf p\cdot\boldsymbol\xi}$.
>
> Choosing a contour is choosing which homogeneous solution to add: a boundary condition.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.8 (Principle "Contours are boundary conditions") · PS §2.4, p. 31*

^thm-c2b-5-3

> [!derivation]- Derivation
> **Step 1** (apply the operator). On $e^{-ip^0\xi^0 + i\mathbf p\cdot\boldsymbol\xi}$, $\partial_0^2 \to -(p^0)^2$ and $\nabla^2 \to -\mathbf p^2$, so $\partial^2 + m^2 \to -(p^0)^2 + \mathbf p^2 + m^2 = -\bigl((p^0)^2 - E_{\mathbf p}^2\bigr)$. Under the integrals,
>
> $$
> (\partial^2 + m^2)D_C(\xi) = \int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}\int_C\frac{dp^0}{2\pi}\,i\,e^{-ip^0\xi^0}\cdot(-1) = -i\int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}\int_C\frac{dp^0}{2\pi}e^{-ip^0\xi^0} :
> $$
>
> the denominator has cancelled. (Sense: "under the integrals" is the derivative moved onto a test function, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]; the rigorous version of Steps 1–3 is the Fourier-side computation of [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], Step 5.)
>
> **Step 2** (back to the real axis). $e^{-ip^0\xi^0}$ is entire, so the closed loop formed by $C$ and the real axis encloses no singularity, and by Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]) $\int_C = \int_{\mathbb R}$. (Sense: $\int dp^0\,e^{-ip^0\xi^0}$ converges for no $\xi^0$; paired with a test function $\chi(\xi^0)$ it becomes $\int dp^0\,\hat\chi(p^0)$ with $\hat\chi$ entire and rapidly decreasing in horizontal strips, and Cauchy's theorem applies to that.)
>
> **Step 3** (delta functions). $\int_{\mathbb R}\frac{dp^0}{2\pi}e^{-ip^0\xi^0} = \delta(\xi^0)$ and $\int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi} = \delta^3(\boldsymbol\xi)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], 1; identities in $\mathcal S'$, [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]). So $(\partial^2 + m^2)D_C = -i\delta^4(\xi)$, for every $C$. This is part 1.
>
> **Step 4** (two contours). If $C_1$ and $C_2$ pass a pole on different sides, $C_1 - C_2$ is a small closed loop around it, of orientation $\pm$; where they pass on the same side the difference is zero. By the residue theorem ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]) and the residues
>
> $$
> \operatorname*{Res}_{p^0 = \pm E}\frac{i}{2\pi}\frac{e^{-ip^0\xi^0}}{(p^0)^2 - E^2} = \pm\frac{i}{2\pi}\frac{e^{\mp iE\xi^0}}{2E}
> $$
>
> ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], 3), $D_{C_1} - D_{C_2} = \int\frac{d^3p}{(2\pi)^3\,2E}\bigl(c_+e^{-iE\xi^0} + c_-e^{iE\xi^0}\bigr)e^{i\mathbf p\cdot\boldsymbol\xi}$ with constants $c_\pm \in \{0, \pm1\}$: tempered distributions of the same type as $D_W(\pm\xi)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]), after $\mathbf p \to -\mathbf p$ in the $e^{iE\xi^0}$ term.
>
> **Step 5** (homogeneous). Each $e^{\mp iE\xi^0 + i\mathbf p\cdot\boldsymbol\xi}$ is on shell, so $(\partial^2 + m^2)$ annihilates it ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], Step 1, an identity in $\mathcal S'$). This is part 2.
>
> ⚑ By-product: there are four ways of passing two poles, hence four standard Green's functions (figure below; Theorems §C2b.5.5, §C2b.6.2, §C2b.7.5).
>
> **What the derivation shows.**
> - The ambiguity in giving the integral a meaning and the ambiguity of boundary conditions are the same ambiguity: the lecture's claim, made precise.
> - The operator side of part 1 is the contact term of time ordering ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]).

^der-c2b-5-3

*Uses:* [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-4|Theorem §CA.3.4]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]

![[ph-qft-c2-6-1.svg]]
*The four ways of passing the poles $p^0 = \pm E_{\mathbf p}$ and the Green's functions they define (Theorems §C2b.5.5, §C2b.6.2, §C2b.7.5; Def. §C2b.7.2). Adapted from the user's PHY 513 notes, Fig. 6.4.*

> [!theorem] Theorem §C2b.5.4: Each Contour Is a Fundamental Solution
> Let $C$ pass $+E_{\mathbf p}$ on the side $\sigma_+$ and $-E_{\mathbf p}$ on the side $\sigma_-$ ($\sigma = +1$ above, $-1$ below).
> 1. $D_C$ of [[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]] is a tempered distribution on $\mathbb R^4$, and at fixed $\mathbf p$ its transform in $p^0$ is a product of boundary values,
>
> $$
> \tilde D_C(p) = \frac{i}{\bigl(p^0 - E_{\mathbf p} + i0\,\sigma_+\bigr)\bigl(p^0 + E_{\mathbf p} + i0\,\sigma_-\bigr)} :
> $$
>
> passing a pole above is the boundary value with the pole moved below, and conversely.
> 2. $(\partial^2 + m^2)D_C = -i\delta^4$ holds in $\mathcal S'(\mathbb R^4)$: $D_C$ is a fundamental solution ([[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]). Every tempered fundamental solution is $D_C + H$ with $H$ a homogeneous solution whose transform lives on the shell ([[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]]); the four contours select four of them.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.2 (Principle "The Green's function is a linear map, and there is one per boundary condition"), §6.8–6.9 · stated here as distributions (standard: Hörmander I, §§3.3, 7.3)*

^thm-c2b-5-4

> [!derivation]- Derivation
> **Step 1** (fixed $\mathbf p$: the time function). Let $E = E_{\mathbf p} > 0$. On $C$, far from the poles $C$ is the real axis and the integrand $\frac{i}{2\pi}\frac{e^{-ip^0t}}{(p^0)^2 - E^2}$ is bounded by a constant times $1/|p^0|^2$, so $G_C(t) \equiv \int_C\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{(p^0)^2 - E^2}$ converges absolutely for every real $t$. By the residue evaluations ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]]) $G_C$ is a combination, with coefficients in $\{0, \pm1\}$, of $\theta(\pm t)e^{\mp iEt}/2E$; so $|G_C(t)| \le 1/E$.
>
> **Step 2** (a tempered distribution). Def. §C2b.5.2 is the iterated integral $D_C(\xi) = \int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}G_C(\xi^0; E_{\mathbf p})$. For $f \in \mathcal S(\mathbb R^4)$ with spatial transform $\tilde f_s(t, \mathbf k) = \int d^3\xi\,f(t, \boldsymbol\xi)e^{-i\mathbf k\cdot\boldsymbol\xi}$, define
>
> $$
> D_C[f] \equiv \int dt\int\frac{d^3p}{(2\pi)^3}\,G_C(t; E_{\mathbf p})\,\tilde f_s(t, -\mathbf p),
> $$
>
> the $\boldsymbol\xi$-integral of the test function done first ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]]). With $|G_C| \le 1/E_{\mathbf p}$ and $\tilde f_s$ Schwartz in $(t, \mathbf p)$ the integral converges absolutely and is bounded by a seminorm of $f$: $D_C \in \mathcal S'(\mathbb R^4)$.
>
> **Step 3** (the transform in $p^0$). Fix $\mathbf p$. For $\varepsilon > 0$ let $g_\varepsilon(p^0) = \dfrac{i}{(p^0 - E + i\varepsilon\sigma_+)(p^0 + E + i\varepsilon\sigma_-)}$, poles at $E - i\varepsilon\sigma_+$ and $-E - i\varepsilon\sigma_-$. Where $C$ passes above $E$ ($\sigma_+ = 1$), the moved pole is below the real axis, so it lies outside the region between $C$ and $\mathbb R$; likewise in every other case. Hence (Cauchy, [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]; the two paths coincide far out) $\int_{\mathbb R}\frac{dp^0}{2\pi}g_\varepsilon e^{-ip^0t} = \int_C\frac{dp^0}{2\pi}g_\varepsilon e^{-ip^0t}$. As $\varepsilon \to 0^+$:
> - on $C$, which keeps a fixed distance from $\pm E$, $g_\varepsilon \to g_0$ uniformly with a bound $c/|p^0|^2$, so the right side tends to $G_C(t)$ for every $t$ ([[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]]), boundedly by Step 1;
> - on $\mathbb R$, partial fractions $g_\varepsilon = \frac{i}{2E + i\varepsilon(\sigma_- - \sigma_+)}\Bigl[\frac{1}{p^0 - E + i\varepsilon\sigma_+} - \frac{1}{p^0 + E + i\varepsilon\sigma_-}\Bigr]$ and Sokhotski–Plemelj for each term ([[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]]) give $g_\varepsilon \to g_C$ in $\mathcal S'(\mathbb R)$, with $g_C$ the product of part 1 (the two factors are singular at the distinct points $\pm E$, so their product is defined, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2, and equals the partial-fraction form).
>
> The transform commutes with the limit ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2), and a bounded pointwise limit is also the distributional limit, so $G_C$ is the inverse transform of $g_C$.
>
> **Step 4** (four dimensions). Inserting Step 3 into Step 2, $D_C[f]$ is $\int\frac{d^3p}{(2\pi)^3}$ of $g_C(\cdot\,; E_{\mathbf p})$ applied to the $p^0$-transform of $\tilde f_s(\cdot, -\mathbf p)$: $\tilde D_C(p) = g_C(p^0; E_{\mathbf p})$, a distribution in $p^0$ depending smoothly on $\mathbf p$ ($E_{\mathbf p}$ is smooth for $m > 0$). Part 1.
>
> **Step 5** (the equation). $m^2 - p^2 = -(p^0 - E)(p^0 + E)$, a product of smooth factors. Since $x\cdot\frac{1}{x \pm i0} = x\,\mathcal P\frac1x \mp i\pi\,x\,\delta(x) = 1$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 3, and [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]]), each factor cancels its own boundary value:
>
> $$
> (m^2 - p^2)\,g_C = -i\,\frac{p^0 - E}{p^0 - E + i0\,\sigma_+}\cdot\frac{p^0 + E}{p^0 + E + i0\,\sigma_-} = -i .
> $$
>
> By the derivative rule in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3) and $\tilde\delta^4 = 1$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 3), $(\partial^2 + m^2)D_C = -i\delta^4$. Part 2, first half.
>
> **Step 6** (all fundamental solutions). By [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], 1–2, $G - D_C$ is homogeneous for every fundamental solution $G$, with transform supported on the shell; conversely $D_C + H$ is a fundamental solution for every such $H$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]]).
>
> ⚑ By-product: "the contour" and "the $i\varepsilon$" are the same object, the choice of $\frac{1}{p^0 \mp E \pm i0}$ at each pole → [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-7|Theorem §C2b.6.7]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-8|Theorem §C2b.6.8]].
>
> **What the derivation shows.**
> - The integral of Def. §C2b.5.2 is a distribution, not a function of $\xi$, and Theorem §C2b.5.3's formal manipulations are identities in $\mathcal S'$.
> - Without a contour, $i/(p^2 - m^2)$ is not a distribution near the shell; each contour is one way of making it one, and the ways differ by homogeneous solutions.
> - Used next: the retarded function (Theorem §C2b.5.5) and the product $\theta(\xi^0)D$ (Theorem §C2b.5.6).

^der-c2b-5-4

*Uses:* [[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-3|Theorem §C2b.5.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-6|Theorem §CA.3.6]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§CA.1 Exchanging Limits, Derivatives and Integrals#^thm-ca-1-1|Theorem §CA.1.1]], [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.2 Generalized Functions#^def-ca-2-6|Def. §CA.2.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]]

## The retarded function

> [!theorem] Theorem §C2b.5.5: The Retarded Green's Function
> The **retarded** contour $C_R$ passes above both poles. Then
>
> $$
> D_R(\xi) = \theta(\xi^0)\bigl[D_W(\xi) - D_W(-\xi)\bigr] = \theta(\xi^0)\,\langle0|[\phi(x), \phi(y)]|0\rangle = \theta(\xi^0)\,iD(\xi) .
> $$
>
> $D_R$ vanishes unless $x$ lies in the causal future of $y$ (inside or on the forward light cone). Mode by mode it is $\theta(t)\,(-i\sin E_{\mathbf p}t)/E_{\mathbf p}$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.6 · PHY 513 Lecture 6, "Retarded Green's Function: Explicit Evaluation" · PS §2.4, eqs. (2.54)–(2.56)*

^thm-c2b-5-5

> [!derivation]- Derivation
> Follow [[P2 Green's Functions by Contour Integration|P2]].
>
> **Step 1** (separate the time integral; [[P2 Green's Functions by Contour Integration#^p2-2|P2, step 2]]; the iterated integral is read as in [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], Step 2). $D_R(\xi) = \int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}\,G_R(t)$ with $G_R(t) = \int_{C_R}\frac{dp^0}{2\pi}\,\frac{i\,e^{-ip^0t}}{(p^0 - E)(p^0 + E)}$: two simple poles on the real axis.
>
> **Step 2** (the arcs; [[P2 Green's Functions by Contour Integration#^p2-4|P2, step 4]]). On $|p^0| = R > E$, $\bigl|\frac{i}{(p^0)^2 - E^2}\bigr| \le \frac{1}{R^2 - E^2}$, and $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$ is at most $1$ on the lower semicircle if $t > 0$ and on the upper one if $t < 0$. On that semicircle the contribution is at most $\frac{1}{2\pi}\cdot\pi R\cdot\frac{1}{R^2 - E^2} \to 0$ (ML, [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]); the $1/(p^0)^2$ decay makes Jordan's lemma, which Yu invokes, unnecessary.
>
> **Step 3** ($t < 0$). Close upward. $C_R$ passes above both poles, so both lie below the closed contour: none is enclosed, and $G_R(t) = 0$ by Cauchy's theorem.
>
> **Step 4** ($t > 0$: residues; [[P2 Green's Functions by Contour Integration#^p2-5|P2, step 5]]). Close downward: the loop runs clockwise and encloses both poles. The residues of $\frac{i}{2\pi}\frac{e^{-ip^0t}}{(p^0)^2 - E^2}$ are $\frac{i}{2\pi}\frac{e^{-iEt}}{2E}$ at $+E$ and $\frac{i}{2\pi}\frac{-e^{iEt}}{2E}$ at $-E$ ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], 3). Clockwise means $-2\pi i\sum\operatorname{Res}$ ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]):
>
> $$
> G_R(t) = -2\pi i\cdot\frac{i}{2\pi}\cdot\frac{e^{-iEt} - e^{iEt}}{2E} = \frac{e^{-iEt} - e^{iEt}}{2E} = -\frac{i\sin Et}{E} .
> $$
>
> **Step 5** (recognize $D_W$; [[P2 Green's Functions by Contour Integration#^p2-6|P2, step 6]]). For $t > 0$, $D_R = \int\frac{d^3p}{(2\pi)^3\,2E}\bigl[e^{-iEt + i\mathbf p\cdot\boldsymbol\xi} - e^{iEt + i\mathbf p\cdot\boldsymbol\xi}\bigr]$. The first exponent is $-ip\cdot\xi$: this term is $D_W(\xi)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]). In the second substitute $\mathbf p \to -\mathbf p$ (Jacobian 1, $E$ unchanged; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in $\mathcal S'$): $e^{iEt - i\mathbf p\cdot\boldsymbol\xi} = e^{ip\cdot\xi} = e^{-ip\cdot(-\xi)}$, so it is $D_W(-\xi)$. Hence $D_R = \theta(t)[D_W(\xi) - D_W(-\xi)] = \theta(t)\,iD(\xi)$, the product taken slice by slice ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1) ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]).
>
> ⚑ By-product: the residue at $+E$ carries the wave with the right energy, the one at $-E$ the wave $e^{+iEt}$; the relabelling turns it into the reversed Wightman function. Since $D = 0$ outside the cone ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]), $D_R$ is supported in the closed forward cone: causal in both senses at once → [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-3|Remark: Retarded means late]].
>
> **Step 6** (check, mode by mode; [[P2 Green's Functions by Contour Integration#^p2-7|P2, step 7]]). $G_R(t) = \theta(t)(-i\sin Et)/E$ is continuous at $0$ (θ times a smooth function, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1; $g(t)\delta(t) = g(0)\delta(t)$ for smooth $g$, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]). With $\theta' = \delta$ ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], 2): $G_R' = \delta(t)\cdot\frac{-i\sin0}{E} + \theta(t)(-i\cos Et) = \theta(t)(-i\cos Et)$, which jumps by $-i$ at $t = 0$; $G_R'' = -i\delta(t) + \theta(t)\,iE\sin Et$. Hence $G_R'' + E^2G_R = -i\delta(t)$.
>
> **Step 7** (check, operator form; PS eq. (2.56)). With $\partial^2 = \partial_0^2 - \nabla^2$ acting on $\theta(x^0 - y^0)\langle[\phi(x), \phi(y)]\rangle$: $\partial_0^2\theta = \delta'$, the cross term is $2\delta(x^0 - y^0)\partial_0\langle[\phi(x), \phi(y)]\rangle$, and $(\partial^2 + m^2)$ on the commutator gives $0$. Using $\delta'(s)F(s) = F(0)\delta'(s) - F'(0)\delta(s)$ and $\langle[\phi, \phi]\rangle = 0$ at equal times (these products are defined because $F(s) = \langle[\phi(x), \phi(y)]\rangle$ is a smooth function of $s = x^0 - y^0$ with values in $\mathcal S'(\mathbb R^3)$, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]),
>
> $$
> (\partial^2 + m^2)D_R = -\delta(x^0 - y^0)\langle[\pi(x), \phi(y)]\rangle + 2\delta(x^0 - y^0)\langle[\pi(x), \phi(y)]\rangle = \delta(x^0 - y^0)\cdot(-i)\delta^3(\mathbf x - \mathbf y) = -i\delta^4(x - y),
> $$
>
> with the equal-time commutator of [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]].
>
> **What the derivation shows.**
> - The sign of $t$ decides the half-plane; for $t < 0$ the poles are on the wrong side, and that is retardation.
> - The jump of $G_R'$ by $-i$, i.e. the data $D_R = 0$, $\partial_0D_R = -i\delta^3(\boldsymbol\xi)$ at $t = 0^+$, is $i$ times the Cauchy data of the commutator function ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]]).
> - Used next: the Feynman function differs from $D_R$ by $D_W(-\xi)$ (Theorem §C2b.6.2); particle production ([[§C2b.8 Particle Production by a Classical Source|§C2b.8]]).

^der-c2b-5-5

*Uses:* [[P2 Green's Functions by Contour Integration|P2]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]

> [!remark] Remark: Retarded means late; the sign of the exponent carries causality
> The source at $y$ affects the field at $x$ only if $y$ comes first: causality in its plainest form, and since the commutator vanishes outside the cone, the retarded function is causal in both senses at once. Why not take complex conjugates and halve the bookkeeping? Conjugation flips $e^{-ip^0t} \to e^{+ip^0t}$, i.e. $t \to -t$, exchanging "$y$ before $x$" with "$y$ after $x$". The sign of the exponent decides where the contour may be closed, so it carries the information about what comes first ([[§CA.4 Contour Integration#^ex-ca-4-2|Example §CA.4.2]] is the same mechanism in one line).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.6 (Caution "Why the sign of the exponent is not innocent") · PHY 513 Lecture 6, "Retarded Contour: Qualitative Behavior"*

^rem-c2b-5-3

> [!theorem] Theorem §C2b.5.6: The Product θ(ξ⁰)D Is Defined; Retarded Means Supported in the Future
> 1. $D$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3), so $\theta(\xi^0)D$ is defined slice by slice: $(\theta D)[f] \equiv \int_0^\infty dt\,D(t, \cdot)\bigl[f(t, \cdot)\bigr]$. The contour's $D_R$ equals $\theta(\xi^0)\,iD$ in this sense; the value $\theta(0)$ plays no role.
> 2. Away from $\xi = 0$ this is a product with disjoint singular supports (the plane $\xi^0 = 0$ for θ, the cone for $D$, [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2). At $\xi = 0$ no product rule applies: extensions of $\theta(\xi^0)D$ from $\mathbb R^4\setminus\{0\}$ differ by $\sum c_\alpha\partial^\alpha\delta^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]), and exactly one of them, times $i$, is a fundamental solution: $D_R$, the slice product of part 1.
> 3. $D_R$ is the only tempered fundamental solution that vanishes for $\xi^0 < 0$: the retarded boundary condition is a support condition. For $m = 0$, $D_R = -\frac{i}{2\pi}\theta(\xi^0)\,\delta(\xi^2) = -\frac{i}{4\pi r}\,\delta(\xi^0 - r)$.
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.6, Ch. 6 §6.2 ("one Green's function per boundary condition"), App. A §A.4 (products) · stated here as distributions (standard: Hörmander I, §§3.3, 6.2)*

^thm-c2b-5-6

> [!derivation]- Derivation
> **Step 1** (the slice product). For $f \in \mathcal S(\mathbb R^4)$, $t \mapsto D(t, \cdot)[f(t, \cdot)] = \int\frac{d^3p}{(2\pi)^3}\frac{-\sin E_{\mathbf p}t}{E_{\mathbf p}}\tilde f_s(t, -\mathbf p)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3) is continuous and, since $|\sin(Et)/E| \le |t|$, bounded by $|t|$ times a rapidly decreasing function of $t$. So $\int_0^\infty dt$ of it converges and is bounded by a seminorm of $f$: $\theta D \in \mathcal S'(\mathbb R^4)$. A single value of $t$ has measure zero, so $\theta(0)$ never enters.
>
> **Step 2** (it is the contour's $D_R$). Mode by mode the retarded contour gives $G_R(t) = \theta(t)(-i\sin Et)/E$ (Step 4 of Derivation §C2b.5.5), and by Step 2 of Derivation §C2b.5.4, $D_R[f] = \int dt\int\frac{d^3p}{(2\pi)^3}G_R(t; E_{\mathbf p})\tilde f_s(t, -\mathbf p) = i\int_0^\infty dt\int\frac{d^3p}{(2\pi)^3}\frac{-\sin E_{\mathbf p}t}{E_{\mathbf p}}\tilde f_s(t, -\mathbf p) = i\,(\theta D)[f]$. Part 1.
>
> **Step 3** (away from the origin). $\operatorname{sing\,supp}\theta(\xi^0) = \{\xi^0 = 0\}$ ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]) and $\operatorname{sing\,supp}D$ is the cone ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3); they meet only at $\xi = 0$, so on $\mathbb R^4\setminus\{0\}$ the product is defined by [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2. It agrees with Step 1: near a point with $\xi^0 \ne 0$, θ is the constant $0$ or $1$; near a point with $\xi^0 = 0$, $\boldsymbol\xi \ne 0$, the point is spacelike and $D$ vanishes there ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]]), so both products are $0$.
>
> **Step 4** (the one extension that is a fundamental solution). Two extensions of $\theta(\xi^0)D$ agree on $\mathbb R^4\setminus\{0\}$, so their difference is supported at the origin and is $\sum_{|\alpha| \le N}c_\alpha\partial^\alpha\delta^4$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]). If both, multiplied by $i$, are fundamental solutions, $i$ times the difference is a homogeneous solution supported at a point, hence zero ([[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], 3). The slice product times $i$ is $D_R$ (Step 2), a fundamental solution ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]), so the slice product is that extension. Part 2.
>
> ⚑ By-product: an extension that is not a fundamental solution differs from $D_R$ by contact terms $\sum c_\alpha\partial^\alpha\delta^4$; for products of interacting fields the same freedom reappears as the local ambiguity of renormalization (QFT C7, planned).
>
> **Step 5** (causal uniqueness). Let $G$ be a tempered fundamental solution with $G = 0$ on $\{\xi^0 < 0\}$, and $H = G - D_R$. $H$ is homogeneous, tempered and vanishes for $\xi^0 < 0$. By [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]] its spatial transform at time $t$ is $\alpha(\mathbf p)e^{-iE_{\mathbf p}t} + \beta(\mathbf p)e^{iE_{\mathbf p}t}$ with distributions $\alpha$, $\beta$ in $\mathbf p$, smooth in $t$. It vanishes for all $t < 0$, and so does its $t$-derivative $-iE(\alpha e^{-iEt} - \beta e^{iEt})$; at any fixed $t < 0$ this $2\times2$ system for $(\alpha, \beta)$ has determinant $2iE_{\mathbf p} \ne 0$, smooth in $\mathbf p$, so $\alpha = \beta = 0$ (as in Step 3 of Derivation §C2b.4.11). Hence $G = D_R$.
>
> **Step 6** ($m = 0$). By [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]], $D = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2)$, and at fixed $t > 0$, $D(t, \cdot) = -\frac{1}{4\pi r}\delta(t - r)$. The slice product of Step 1 is $\int_0^\infty dt\,D(t, \cdot)[f(t, \cdot)] = -\frac{1}{2\pi}\int d^3\xi\,\frac{f(r, \boldsymbol\xi)}{2r}$, which is $-\frac{1}{2\pi}\theta(\xi^0)\delta(\xi^2)[f]$ by [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, a distribution on all of $\mathbb R^4$, tip included. Multiplying by $i$ gives part 3's formula; $\delta(t^2 - r^2) = \delta(t - r)/2r$ for $t > 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 2).
>
> **What the derivation shows.**
> - "θ times a distribution" is harmless here for a structural reason: $D$ is smooth in time, its singularities lie on the cone, and the cone meets the plane $\xi^0 = 0$ only at one point, where the field equation fixes the extension.
> - The retarded boundary condition, "nothing before the source", is precisely a statement about support.
> - A second characterization of the same extension, by power counting: near $\xi = 0$, $D$ scales like $|\xi|^{-2}$ ($\delta(\lambda^2\xi^2) = \lambda^{-2}\delta(\xi^2)$), while every $\partial^\alpha\delta^4$ scales at least like $|\xi|^{-4}$; so the slice product is the only extension no more singular at the origin than $D$ itself (scaling degree $2 <$ dimension $4$; Brunetti–Fredenhagen, Commun. Math. Phys. 208 (2000), Thm. 5.2; quoted, not proved here).
> - Used next: the same three readings for $D_F$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3|Theorem §C2b.6.3]]); the retarded solution of a sourced equation ([[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1|Theorem §C2b.8.1]]).

^der-c2b-5-6

*Uses:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

> [!remark] Remark: Measurable response is a retarded commutator
> Couple the quantum field to a classical source as in [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1|Model §C2b.5.1]], which adds $-\int d^3x\,j\phi$ to $H$. The retarded solution changes the expectation value of the field by
>
> $$
> \delta\langle0|\phi(x)|0\rangle = i\int d^4y\,D_R(x - y)\,j(y) = i\int d^4y\;\theta(x^0 - y^0)\,\langle0|[\phi(x), \phi(y)]|0\rangle\,j(y) :
> $$
>
> the response of the field is the retarded unequal-time commutator. This is the simplest case of the Kubo formula of linear response, $\delta\langle\mathcal O(x)\rangle = i\int d^4y\,\theta(x^0 - y^0)\langle[\mathcal O(x), \phi(y)]\rangle\,j(y)$, and the reason the retarded function is the central object of condensed matter. Influence travels only through the commutator ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]]).
>
> *Source: the user's PHY 513 notes, Ch. 6 §6.6 ("Measurable response is a retarded commutator"), Ch. 5 §5.7*

^rem-c2b-5-4

> [!remark]- Connections
> - Mode by mode the retarded function is $\theta(t)(-i\sin Et)/E$, the impulse response of an undamped oscillator; the damped version $\theta(t)e^{-\gamma t/2}\sin\omega_dt/m\omega_d$ is [[§B4.4 Fourier Transforms and the Delta Function#^thm-b4-4-6|WO Theorem §B4.4.6]], whose transfer function $\chi(\omega)$ has its poles in one half-plane exactly as $\tilde D_R$ does. A field is one such oscillator per $\mathbf p$.
> - The massless retarded function, $D_R = -\frac{i}{4\pi r}\delta(t - r)$ for $t > 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-7|Theorem §C2b.4.7]]), turns $i\int D_Rj$ into $\int d^3y\,j(t - |\mathbf x - \mathbf y|, \mathbf y)/4\pi|\mathbf x - \mathbf y|$: the retarded potentials of [[§B11.1★ Potentials, Gauges and Retarded Potentials#^thm-b11-1-4|EM Theorem §B11.1.4]] (with $\partial^2 = -\Box$ in EM's sign).
> - A static point source $j = g\,\delta^3(\mathbf y)$ gives, through the retarded function integrated over $y^0$, $\phi = g\int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\mathbf p^2 + m^2} = \frac{g}{4\pi}\frac{e^{-mr}}{r}$: the Yukawa field of [[§B4.1 The Klein–Gordon Equation#^rem-b4-1-4|REL Remark: Static solutions and the Yukawa potential]], the $p^0 = 0$ slice of $\tilde D$.
> - Electromagnetism level C: at $m = 0$ the static slice is electrostatics; there the Green functions of Poisson's equation with boundaries (Dirichlet, Neumann) are fundamental solutions in this section's sense, $i\varepsilon_0G$ in the $-i$ normalization, each the free one plus a harmonic function; the Lorenz-gauge potentials are retarded solutions of this section — [[§C7.3 Green Functions for Poisson’s Equation#^def-c7-3-1|EM Def. §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^cau-c7-3-1|EM Caution: Normalizations of the Green function]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-1|EM Theorem §C7.3.1]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-4|EM Theorem §C7.3.4]], [[§C1.4 Gauge Fixing and the Two Polarizations#^thm-c1-4-1|EM Theorem §C1.4.1]].
> - The procedure behind every contour in this section is [[P2 Green's Functions by Contour Integration|P2]]; the classical source of Model §C2b.5.1 produces particles in [[§C2b.8 Particle Production by a Classical Source|§C2b.8]].
> - [[§CA.2 Generalized Functions#^def-ca-2-7|Def. §CA.2.7]] and [[§CA.2 Generalized Functions#^thm-ca-2-14|Theorem §CA.2.14]] (fundamental solutions and their differences) are what a Green's function is: Theorem §C2b.5.4 shows each contour gives one, and they differ by on-shell homogeneous solutions.
> - [[§CA.2 Generalized Functions#^thm-ca-2-15|Theorem §CA.2.15]] (convolution with a fundamental solution) is the statement that $\phi = i\int D_Cj$ solves the sourced equation when $j$ is a test function.
> - [[§CA.2 Generalized Functions#^thm-ca-2-11|Theorem §CA.2.11]] (Sokhotski–Plemelj) identifies passing a pole with the boundary value $1/(p^0 \mp E \pm i0)$; [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]] (products with disjoint singular supports, and $x\,\mathcal P\frac1x = 1$) makes the product of the two pole factors, the cancellation in $(m^2 - p^2)\tilde D_C = -i$, and the product $\theta(\xi^0)D$ away from the origin legitimate.
> - [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]] (distributions supported at a point) is why the extension of $\theta(\xi^0)D$ across the origin is ambiguous only by $\sum c_\alpha\partial^\alpha\delta^4$, removed by requiring a fundamental solution.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]] and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] (derivative rule in $\mathcal S'$, transform of distributions, plane-wave delta) turn the Klein–Gordon operator into multiplication by $m^2 - p^2$ and $\delta^4$ into $1$.
> - [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]] and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] (composition of δ, the forward-cone distribution $\theta(x^0)\delta(x^2)$) give the on-shell form of free fields and the massless retarded function.
> - [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]] (Cauchy's theorem) moves contours, and [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]] (relabelling) turns the negative-frequency residue into $D_W(-\xi)$.
