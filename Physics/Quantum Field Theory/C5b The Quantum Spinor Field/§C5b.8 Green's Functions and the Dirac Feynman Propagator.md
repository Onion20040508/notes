---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.9 Spin and Statistics]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 62–63 · Yu Zhao-Huan, 量子场论讲义, §6.4.5 · the user's pre-course notes, the Dirac parts of "Time-ordered product and microcausality" and §6.4 ("Feynman Propagators: Dirac spinor field").*

*Taught in Lecture 17 (Nov 4; slide 17: fermionic time ordering and $S_F$, "two independent derivations of the propagator (see HW)"; its use in Wick's theorem and the Yukawa rules is in [[· C6d Feynman Rules for Fermions|C6d]]). Problem Set 9 has been submitted (restored 2026-11-05), so both derivations of $S_F$ are in (Theorem §C5b.8.1: from the Dirac equation with a source, and by solving for the Fourier transform, Problem 1(c); Theorem §C5b.8.3: from the mode expansion, Problem 1(a), and from $D_F$, Problem 1(d)), with the direct proof that the time-ordered product is a Green's function (Theorem §C5b.8.4, Problem 1(b)) and its two lessons (Theorems §C5b.8.5–§C5b.8.6); the section was written earlier from the user's pre-course notes, Yu and Peskin–Schroeder.*

This is the spinor counterpart of [[§C2b.5 Green's Functions and Contours|§C2b.5]]–[[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]] and the single home of the Dirac propagator $S_F$. Every Green's function of the Dirac operator is $i\slashed{\partial} + m$ applied to a Klein–Gordon Green's function, with the boundary condition (the contour) inherited unchanged; the spin-specific additions are the numerator $\slashed{p} + m$ (the spin sum continued off the shell), the normalization $(i\slashed{\partial} - m)S = +i\delta^4$, and the minus sign of fermionic time ordering. The contour work is [[P2 Green's Functions by Contour Integration]] with a numerator. Conventions as in [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]]; the Dirac Green's functions are normalized by $(i\slashed{\partial} - m)S = i\delta^4$ (PS).

**Setup.** The functions $S_R$, $S_A$, $S_F$ are vacuum values of the free Dirac field ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]) in the free vacuum $|0\rangle$, normalized by $(i\slashed{\partial} - m)S = i\delta^4$, $m > 0$. As Green's functions and distributions (Theorems §C5b.8.1, §C5b.8.7, §C5b.8.8) they are statements about functions, valid wherever they are used; their reading as vacuum values needs the free field. Fermionic time ordering (Def. §C5b.8.2) applies to any fermion operators. With interactions the two-point function in $|\Omega\rangle$ is not $S_F$ beyond lowest order (the line of Theorem §C5b.8.3).

## Green's functions of the Dirac operator

> [!definition] Definition §C5b.8.1: Retarded and Advanced Functions of the Dirac Field
> With the anticommutator function $S$ of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-2|Def. §C5b.7.2]], the **retarded** and **advanced** functions of the Dirac field are
>
> $$
> S_R(\xi) \equiv \theta(\xi^0)\,iS(\xi), \qquad S_A(\xi) \equiv -\theta(-\xi^0)\,iS(\xi) ,
> $$
>
> the products with $\theta$ taken slice by slice as for the scalar $D_R = \theta(\xi^0)iD$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1); that they are Green's functions is [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]].
>
> *Scalar analogue:* $D_R$, $D_A$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact.
>
> *Source: PS §3.5, eq. (3.116) ($S_R$) · named here after Bjorken–Drell ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^cau-c5b-7-1|§C5b.7, Caution: The letter S]])*

^def-c5b-8-1

> [!theorem] Theorem §C5b.8.1: Green's Functions of the Dirac Operator
> The propagators $S_C = (i\slashed{\partial} + m)D_C$ built from the scalar Green's functions $D_C$ ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]], normalized by $(\partial^2 + m^2)D_C = -i\delta^4$) are Green's functions of the Dirac operator:
>
> $$
> (i\slashed{\partial}_x - m)\,S_C(x - y) = i\delta^4(x - y)\,\mathbf 1, \qquad (\slashed{p} - m)\,\tilde S_C(p) = i\,\mathbf 1 \text{ (in the } \varepsilon \to 0^+ \text{ limit)} .
> $$
>
> For $C = F$ this is $S_F$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]); for $C = R, A$, $S_R = (i\slashed{\partial} + m)D_R$ and $S_A = (i\slashed{\partial} + m)D_A$ are the functions of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-1|Def. §C5b.8.1]], with $\tilde S_R = i(\slashed{p} + m)/\bigl((p^0 + i\varepsilon)^2 - E^2_{\mathbf p}\bigr)$; $S_R$ is supported in the closed forward cone.
>
> *Scalar analogue:* [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]].
>
> *Model:* any; *applies:* any theory (a statement about the functions); their reading as vacuum values in $|0\rangle$ needs the free field ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]).
>
> *Source: PS §3.5, eqs. (3.116)–(3.120) · stated here as distributions · second route: PHY 513, Problem Set 9, Problem 1(c) (the user's solution)*

^thm-c5b-8-1

> [!derivation]- Derivation
> **1. The operator identity.** $(i\slashed{\partial} - m)(i\slashed{\partial} + m) = -\slashed{\partial}\slashed{\partial} + im\slashed{\partial} - im\slashed{\partial} - m^2 = -(\partial^2 + m^2)$, with $\slashed{\partial}\slashed{\partial} = \partial^2$ ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]]; the partial derivatives commute, also on distributions).
>
> **2. Green's function.** $(i\slashed{\partial} - m)S_C = -(\partial^2 + m^2)D_C = -(-i\delta^4) = i\delta^4$, in $\mathcal S'$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]; for $D_F$, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]). ⚑ By-product: the Dirac normalization $+i\delta^4$ differs in sign from the Klein–Gordon $-i\delta^4$ because of the minus sign in Step 1 → Conventions of this note.
>
> **3. Momentum space.** $(\slashed{p} - m)\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon} = \frac{i(p^2 - m^2)}{p^2 - m^2 + i\varepsilon} = i - \frac{i\cdot i\varepsilon}{p^2 - m^2 + i\varepsilon}$; the last term is $\varepsilon$ times a family converging in $\mathcal S'$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]), so it tends to $0$.
>
> **4. $S_R = (i\slashed{\partial} + m)D_R$.** $D_R = \theta(\xi^0)iD$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1). Apply $i\slashed{\partial} + m = i\gamma^0\partial_0 + i\gamma^j\partial_j + m$ slice by slice. The spatial derivatives and $m$ act on $iD$ only. The time derivative obeys the product rule with $\partial_0\theta(\xi^0) = \delta(\xi^0)$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 2): $\partial_0[\theta(\xi^0)iD] = \delta(\xi^0)\,iD + \theta(\xi^0)\,\partial_0iD$. Hence $(i\slashed{\partial} + m)[\theta(\xi^0)iD] = \theta(\xi^0)(i\slashed{\partial} + m)iD + i\gamma^0\delta(\xi^0)\,iD$. In the last term, $D$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3), so $\delta(\xi^0)D$ is $\delta(\xi^0)\otimes D(0, \cdot)$, and $D(0, \cdot) = 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]]). Dropped: the contact term, because the scalar field commutes with itself at equal times. What remains is $\theta(\xi^0)(i\slashed{\partial} + m)iD = \theta(\xi^0)\,iS$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]). (The same contact term is dropped for $S_F$ in the second route under [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].) The same with $-\theta(-\xi^0)$ for $S_A$. The transform is $(\slashed{p} + m)\tilde D_R$ with $\tilde D_R$ of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] (PS (3.120): closing below for $x^0 > y^0$ picks up both poles and gives $S^+_W + S^-_W$).
>
> **5. Support.** $\operatorname{supp}D_R$ is the closed forward cone ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 3), and derivatives do not enlarge supports (Step 1 of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^der-c5b-7-3|Derivation §C5b.7.3]]).
>
> **What the derivation shows**
> - Every Dirac Green's function is $i\slashed{\partial} + m$ applied to a Klein–Gordon one; the boundary condition (contour) is inherited unchanged.

^der-c5b-8-1

*Uses:* [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]], [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]

> [!derivation]- Derivation (second route: solving for the Fourier transform)
> This route starts from the equation and solves for the transform, where the first derivation applies $i\slashed{\partial} - m$ to $(i\slashed{\partial} + m)D_C$; the two read one identity from opposite ends, and both give the contour of $S_C$ as that of $D_C$.
>
> **Step 1** (insert the Fourier form). Write $S_C(x - y)_{ab} = \int_C\frac{d^4p}{(2\pi)^4}\,\tilde S_C(p)_{ab}\,e^{-ip\cdot(x - y)}$, with $\int_Cd^4p = \int d^3p\int_Cdp^0$: $\mathbf p$ over $\mathbb R^3$ and, for each $\mathbf p$, $p^0$ along a contour $C$ from $-\infty$ to $+\infty$ ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]]). The operator $(i\slashed{\partial}_x - m)$ acts only on the exponential, where $i\slashed{\partial}_x\,e^{-ip\cdot(x - y)} = \slashed{p}\,e^{-ip\cdot(x - y)}$; with $\delta^4(x - y) = \int\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot(x - y)}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]) the equation $(i\slashed{\partial}_x - m)_{ca}S_C(x - y)_{ab} = i\delta^4(x - y)\,\delta_{cb}$ becomes, with only $a$ summed,
>
> $$
> \int_C\frac{d^4p}{(2\pi)^4}\,(\slashed{p} - m)_{ca}\,\tilde S_C(p)_{ab}\,e^{-ip\cdot(x - y)} = i\,\delta_{cb}\int\frac{d^4p}{(2\pi)^4}\,e^{-ip\cdot(x - y)} .
> $$
>
> **Step 2** (the detours do not change the right side). $C$ coincides with the real axis except for small detours, of radius $r$, around the poles of $\tilde S_C(p)$ at $p^0 = \pm E_{\mathbf p}$. On these pieces $C$ minus the real axis is the boundary of a half-disk, a closed loop $\gamma_\pm$. Since $e^{-ip\cdot(x - y)}$ is analytic in $p^0$, Cauchy's theorem ([[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]]) gives
>
> $$
> \int_Cdp^0\,e^{-ip\cdot(x - y)} - \int_{\mathbb R}dp^0\,e^{-ip\cdot(x - y)} = \oint_{\gamma_+}dp^0\,e^{-ip\cdot(x - y)} + \oint_{\gamma_-}dp^0\,e^{-ip\cdot(x - y)} = 0 ,
> $$
>
> so the right side of Step 1 is $\int_C\frac{d^4p}{(2\pi)^4}\,i\,\delta_{cb}\,e^{-ip\cdot(x - y)}$.
>
> **Step 3** (equate the integrands).
>
> $$
> (\slashed{p} - m)_{ca}\,\tilde S_C(p)_{ab} = i\,\delta_{cb}, \qquad\text{in matrix form}\qquad (\slashed{p} - m)\,\tilde S_C(p) = i\,\mathbf 1 .
> $$
>
> **Step 4** (invert). Multiply on the left by $\slashed{p} + m$ and use $\slashed{p}\slashed{p} = \frac12p_\mu p_\nu\{\gamma^\mu, \gamma^\nu\} = p^2$ ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]]):
>
> $$
> (\slashed{p} + m)(\slashed{p} - m)\,\tilde S_C(p) = (p^2 - m^2)\,\tilde S_C(p) = i(\slashed{p} + m) , \qquad\text{so, away from the poles,}\qquad \tilde S_C(p) = \frac{i(\slashed{p} + m)}{p^2 - m^2} .
> $$
>
> **Step 5** (pull the operator out). Insert into the Fourier form and use $\slashed{p}\,e^{-ip\cdot(x - y)} = i\slashed{\partial}_x\,e^{-ip\cdot(x - y)}$; the operator $(i\slashed{\partial}_x + m)$ does not depend on $p$:
>
> $$
> S_C(x - y)_{ab} = \int_C\frac{d^4p}{(2\pi)^4}\,\frac{i(\slashed{p} + m)_{ab}}{p^2 - m^2}\,e^{-ip\cdot(x - y)} = (i\slashed{\partial}_x + m)_{ab}\int_C\frac{d^4p}{(2\pi)^4}\,\frac{i}{p^2 - m^2}\,e^{-ip\cdot(x - y)} = (i\slashed{\partial}_x + m)_{ab}\,D_C(x - y) ,
> $$
>
> the scalar propagator of the same contour ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]]).
>
> **What the derivation shows**
> - Equating the integrands fixes $\tilde S_C$ only off the poles, where $p^2 \ne m^2$, as for the scalar ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]]); on the shell the contour, or equivalently the $i\varepsilon$, supplies the rest, and that both give one distribution is [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]] (for $C = F$).
> - With the Feynman contour this is $S_F = (i\slashed{\partial} + m)D_F$, the last form of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], reached without the time-ordered product.
>
> *Source: PHY 513, Problem Set 9, Problem 1(c) (the user's solution) · PHY 513 Lecture 17, slide 17 ("two independent derivations of the propagator (see HW)")*

^der-c5b-8-1b

*Uses:* [[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-2|Theorem §C2b.5.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.4 Contour Integration#^thm-ca-4-2|Theorem §CA.4.2]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]]

## Time ordering and the Feynman propagator

> [!definition] Definition §C5b.8.2: Time-Ordered Product of Fermion Fields
> For fermion fields the time-ordered product carries the sign of the permutation that puts the fields in time order:
>
> $$
> T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\} \equiv \theta(x^0 - y^0)\,\hat\psi_a(x)\hat{\bar\psi}_b(y) - \theta(y^0 - x^0)\,\hat{\bar\psi}_b(y)\hat\psi_a(x) ,
> $$
>
> and for $n$ fields $T\{\hat\Phi_1\cdots\hat\Phi_n\} = (-1)^P\,\hat\Phi_{\sigma(1)}\cdots\hat\Phi_{\sigma(n)}$ with times decreasing from left to right and $P$ the number of transpositions of fermion fields. This extends [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]], which it equals for boson fields.
>
> *Scalar analogue:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]].
>
> *Model:* any; *applies:* any fermion field operators, interacting ones included.
>
> *Source: PS §3.5, eq. (3.121) and the text after it · Yu §6.4.5, eq. (6.258) and §6.3 · the user's pre-course notes, "Wick's theorem" (contractions of fermion fields)*

^def-c5b-8-2

> [!theorem] Theorem §C5b.8.2: Fermionic Time Ordering Is Frame Independent
> $T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}$ of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]] is the same operator in every inertial frame. With a plus sign in place of the minus it would not be: at spacelike separation the two orderings would differ by $2\hat{\bar\psi}_b(y)\hat\psi_a(x) \ne 0$.
>
> *Scalar analogue:* Step 4 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-1|Derivation §C2b.6.1]] ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, exact, an operator statement; it uses only that the fields anticommute at spacelike separation ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]]).
>
> *Source: the user's pre-course notes, "Time-ordered product and microcausality" ("the extra minus sign on swapping fermionic operators is what keeps $T[\psi_a(x)\bar\psi_b(y)]$ Lorentz invariant") · PS §3.5, p. 63*

^thm-c5b-8-2

> [!derivation]- Derivation
> **1. Timelike separation.** The sign of $x^0 - y^0$ is the same in every frame related by $SO^+(1,3)$ ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]): every observer picks the same term.
>
> **2. Spacelike separation.** Observers disagree on which term applies. By [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], there $\hat\psi_a(x)\hat{\bar\psi}_b(y) = -\hat{\bar\psi}_b(y)\hat\psi_a(x)$, so the first term $\hat\psi_a(x)\hat{\bar\psi}_b(y)$ and the second $-\hat{\bar\psi}_b(y)\hat\psi_a(x)$ are the same operator: the disagreement is harmless. This is Step 4 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-1|Derivation §C2b.6.1]] with the anticommutator in place of the commutator.
>
> **3. With the wrong sign.** For $\theta\hat\psi\hat{\bar\psi} + \theta\hat{\bar\psi}\hat\psi$ the two terms at spacelike separation would be $\hat\psi\hat{\bar\psi}$ and $\hat{\bar\psi}\hat\psi = -\hat\psi\hat{\bar\psi}$, differing by $2\hat{\bar\psi}\hat\psi$, an operator with nonzero matrix elements (its vacuum value is $2S^-_W \ne 0$ there, [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).
>
> **What the derivation shows**
> - The sign in fermionic time ordering is not a convention: it is forced by Lorentz invariance once the fields anticommute outside the cone (PS: "this minus sign is extremely important in the quantum field theory of fermions").
> - At equal times and coincident points the anticommutator is $\gamma^0\delta^3$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]), the fermionic contact term; it is what makes $S_F$ a Green's function ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]) → [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-6|Theorem §C5b.8.6]].

^der-c5b-8-2

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]

> [!theorem] Theorem §C5b.8.3: The Dirac Feynman Propagator
> The Feynman propagator of the Dirac field, the vacuum expectation value of the fermionic time-ordered product ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]), is
>
> $$
> S_F(x - y) \equiv \langle0|T\{\hat\psi(x)\hat{\bar\psi}(y)\}|0\rangle = \theta(\xi^0)S^+_W(\xi) - \theta(-\xi^0)S^-_W(\xi) = \int\frac{d^4p}{(2\pi)^4}\,\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon}\,e^{-ip\cdot\xi} = (i\slashed{\partial}_x + m)\,D_F(\xi) ,
> $$
>
> with $S^\pm_W$ of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], the Feynman contour, i.e. the $i\varepsilon$ prescription of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] ($\varepsilon \to 0^+$ in $\mathcal S'$, [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]]), and the scalar Feynman propagator $D_F$ of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]. $\tilde S_F(p) = i(\slashed{p} + m)/(p^2 - m^2 + i\varepsilon)$ is the factor of an internal fermion line.
>
> *Scalar analogue:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]].
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact; with interactions the vacuum value in $|\Omega\rangle$ is not $S_F$ beyond lowest order, as for the scalar ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-4|§C2b.6, Caution: With interactions, the two-point function is not D_F]]).
>
> *Source: PS §3.5, eq. (3.121) · Yu §6.4.5, eqs. (6.258)–(6.267) · the user's pre-course notes, §6.4 ("Dirac spinor field") · PHY 513, Problem Set 9, Problem 1(a) (the operator side, $S^\pm_W$ for each time ordering) and Problem 1(d) (the second route) (the user's solution)*

^thm-c5b-8-3

> [!derivation]- Derivation
> **1. The operator side** ([[P2 Green's Functions by Contour Integration|P2]] in reverse, as Yu). By [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]] and [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-1|Def. §C5b.7.1]], $S_F = \theta(t)S^+_W - \theta(-t)S^-_W$, and by [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], with $p^0 = E_{\mathbf p} \equiv E$,
>
> $$
> S_F(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E}\Bigl[\theta(t)(\slashed{p} + m)e^{-ip\cdot\xi} - \theta(-t)(\slashed{p} - m)e^{ip\cdot\xi}\Bigr] .
> $$
>
> **2. Relabel the second term.** $\mathbf p \to -\mathbf p$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1, in $\mathcal S'$; Jacobian $1$, $E$ unchanged): $e^{ip\cdot\xi} = e^{iEt - i\mathbf p\cdot\boldsymbol\xi} \to e^{iEt + i\mathbf p\cdot\boldsymbol\xi}$ and $\slashed{p} - m = \gamma^0E - \gamma^ip^i - m \to \gamma^0E + \gamma^ip^i - m$. Define the matrix polynomial $g(p^0) \equiv \gamma^0p^0 - \gamma^ip^i + m$ (that is $\slashed{p} + m$ at four-momentum $(p^0, \mathbf p)$, off the shell). Then $\slashed{p} + m$ on the shell is $g(E)$, and $-(\gamma^0E + \gamma^ip^i - m) = g(-E)$:
>
> $$
> S_F(\xi) = \int\frac{d^3p}{(2\pi)^3}\,e^{i\mathbf p\cdot\boldsymbol\xi}\;\frac{1}{2E}\Bigl[\theta(t)\,g(E)\,e^{-iEt} + \theta(-t)\,g(-E)\,e^{iEt}\Bigr] .
> $$
>
> ⚑ By-product: the fermionic minus sign of the time ordering and the minus sign of $\sum v\bar v = \slashed{p} - m$ combine into the single numerator $g(p^0) = \slashed{p} + m$ evaluated at the two poles; this is why one formula covers both orderings.
>
> **3. Poles and residues** ([[P2 Green's Functions by Contour Integration#^p2-2|P2, step 2]]). For $\varepsilon > 0$ consider $\int\frac{dp^0}{2\pi}\frac{i\,g(p^0)e^{-ip^0t}}{(p^0)^2 - E^2 + i\varepsilon}$; the poles are at $\pm E_\varepsilon$ with $E_\varepsilon = \sqrt{E^2 - i\varepsilon} = E - i\varepsilon'$, $\varepsilon' > 0$ (fourth and second quadrants: the Feynman contour, [[P2 Green's Functions by Contour Integration#^p2-3|P2, step 3]]). The residue at $E_\varepsilon$ is $\frac{i}{2\pi}\frac{g(E_\varepsilon)e^{-iE_\varepsilon t}}{2E_\varepsilon}$, at $-E_\varepsilon$ it is $\frac{i}{2\pi}\frac{g(-E_\varepsilon)e^{iE_\varepsilon t}}{-2E_\varepsilon}$ ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]]); $g$ is a polynomial, so it is simply evaluated at the pole (Yu (6.262)).
>
> **4. Close the contour** ([[P2 Green's Functions by Contour Integration#^p2-4|P2, steps 4–5]]). The integrand behaves like $g(p^0)/(p^0)^2 \sim 1/|p^0|$, which tends to zero but not fast enough for the ML estimate: Jordan's lemma is needed ([[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]; [[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]]: satisfied). For $t > 0$ close downward, clockwise, enclosing $E_\varepsilon$: $-2\pi i\cdot\frac{i}{2\pi}\frac{g(E_\varepsilon)e^{-iE_\varepsilon t}}{2E_\varepsilon} = \frac{g(E_\varepsilon)e^{-iE_\varepsilon t}}{2E_\varepsilon}$. For $t < 0$ close upward, counterclockwise, enclosing $-E_\varepsilon$: $2\pi i\cdot\frac{i}{2\pi}\frac{g(-E_\varepsilon)e^{iE_\varepsilon t}}{-2E_\varepsilon} = \frac{g(-E_\varepsilon)e^{iE_\varepsilon t}}{2E_\varepsilon}$ ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]). As $\varepsilon \to 0^+$ (pointwise for $t \ne 0$, bounded, hence in $\mathcal S'(\mathbb R)$, [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]):
>
> $$
> \int\frac{dp^0}{2\pi}\frac{i\,g(p^0)\,e^{-ip^0t}}{(p^0)^2 - E^2 + i\varepsilon} \to \frac{1}{2E}\Bigl[\theta(t)g(E)e^{-iEt} + \theta(-t)g(-E)e^{iEt}\Bigr] ,
> $$
>
> the bracket of Step 2. (The value at $t = 0$ is a single point and carries no weight.) The denominator $(p^0)^2 - E^2 + i\varepsilon = p^2 - m^2 + i\varepsilon$; writing $2E\varepsilon$ or poles at $\pm(E - i\varepsilon)$ instead gives the same limit ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 3).
>
> **5. Combine** ([[P2 Green's Functions by Contour Integration#^p2-6|P2, step 6]]). Inserting into Step 2, $d^3p\,dp^0 = d^4p$, $e^{-ip^0t + i\mathbf p\cdot\boldsymbol\xi} = e^{-ip\cdot\xi}$ and $g(p^0) = \slashed{p} + m$: the four-dimensional formula (Yu (6.266)–(6.267)), as a limit in $\mathcal S'(\mathbb R^4)$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]]); the iterated integral is read as in [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], Step 2.
>
> **6. In terms of $D_F$.** $\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon} = (\slashed{p} + m)\tilde D_F$ with $\tilde D_F = \frac{i}{p^2 - m^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]), and $\slashed{p} + m$ is the transform of $i\slashed{\partial} + m$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3): $S_F = (i\slashed{\partial} + m)D_F$ ([[P2 Green's Functions by Contour Integration#^p2-7|P2, step 7]] checks it: [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]).
>
> **What the derivation shows**
> - Every step of P2 goes through with a numerator analytic in $p^0$; only the arc estimate changes (Jordan instead of ML).
> - For $x^0 > y^0$ the propagator is the fermion amplitude $\langle0|\hat\psi\hat{\bar\psi}|0\rangle$; for $x^0 < y^0$ it is minus the antifermion amplitude; the $i\varepsilon$ is the scalar's.
>
> *Source of Step 1: PHY 513, Problem Set 9, Problem 1(a) (the user's solution: the mode expansion inserted for each ordering, $\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle = (i\slashed{\partial}_x + m)_{ab}D_W(x - y)$, $\langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle = -(i\slashed{\partial}_x + m)_{ab}D_W(y - x)$, the derivatives acting only on $D_W$)*

^der-c5b-8-3

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]

> [!derivation]- Derivation (second route: from the scalar propagator)
> **1. Apply $i\slashed{\partial} + m$ to $D_F$ slice by slice.** $D_F = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]; slice products, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]). With $\partial_0\theta(\pm\xi^0) = \pm\delta(\xi^0)$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 2) and the product rule,
>
> $$
> (i\slashed{\partial} + m)D_F = \theta(\xi^0)(i\slashed{\partial} + m)D_W(\xi) + \theta(-\xi^0)(i\slashed{\partial} + m)D_W(-\xi) + i\gamma^0\delta(\xi^0)\bigl[D_W(\xi) - D_W(-\xi)\bigr] .
> $$
>
> **2. The first two terms.** By [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]] they are $\theta(\xi^0)S^+_W - \theta(-\xi^0)S^-_W$, the operator side of Step 1 above.
>
> **3. The contact term vanishes.** $D_W(\xi) - D_W(-\xi) = iD(\xi)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]); $D$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$, so $\delta(\xi^0)D$ is the distribution $\delta(\xi^0)\otimes D(0, \cdot)$, and $D(0, \cdot) = 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]]). Dropped: the contact term, because the field commutes with itself at equal times. (PS make the same remark for $S_R$: "the term involving $\partial_0\theta(x^0 - y^0)$ vanishes".)
>
> **4. Transform.** $(\slashed{p} + m)\tilde D_F$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3), the four-dimensional formula.
>
> **What the derivation shows**
> - The Dirac propagator is a derivative of the scalar one; a contact term could have appeared and is absent because $[\hat\phi(t, \mathbf x), \hat\phi(t, \mathbf y)] = 0$.
>
> *Source: PS §3.5, eqs. (3.117), (3.121) · the user's pre-course notes, §6.4 ("the energy factors assemble into $\slashed{p}$") · Steps 1 and 3: PHY 513, Problem Set 9, Problem 1(d) (the user's solution; at $x^0 = y^0$ the user shows $D_W(x - y) - D_W(y - x) = 0$ directly, the two integrals $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}e^{\pm i\mathbf p\cdot\mathbf r}$ coinciding after $\mathbf p \to -\mathbf p$)*

^der-c5b-8-3b

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]

*Procedure:* [[P2 Green's Functions by Contour Integration#^p2-1|P2, steps 1–7]]

> [!remark] Remark: Fermion forward, antifermion backward
> For $x^0 > y^0$, $S_F = \langle0|\hat\psi(x)\hat{\bar\psi}(y)|0\rangle$: $\hat{\bar\psi}(y)$ creates a fermion at $y$, $\hat\psi(x)$ annihilates it at $x$. For $x^0 < y^0$, $S_F = -\langle0|\hat{\bar\psi}(y)\hat\psi(x)|0\rangle$: $\hat\psi(x)$ creates an antifermion at $x$ and $\hat{\bar\psi}(y)$ annihilates it at $y$, later. One function carries positive energy forward in time in both cases, the fermion from $y$ to $x$ and the antifermion from $x$ to $y$, as the complex scalar's $\langle0|T\{\hat\phi\hat\phi^\dagger\}|0\rangle$ does ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]); the arrow on a fermion line in a Feynman diagram follows the charge, not the time ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|§C6d.1, Def. §C6d.1.1]]).
>
> *Source: the user's pre-course notes, §6.4 ("Complex scalar field": "a particle from $y$ to $x$ or an antiparticle from $x$ to $y$") · PS §3.5, eq. (3.121)*

^rem-c5b-8-1

> [!theorem] Theorem §C5b.8.4: The Free Dirac Schwinger–Dyson Equation
> The vacuum value of the fermionic time-ordered product ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]) is a Green's function of the Dirac operator:
>
> $$
> (i\slashed{\partial}_x - m)_{ca}\,\langle0|T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}|0\rangle = i\delta^4(x - y)\,\delta_{cb}, \qquad\text{that is}\qquad (i\slashed{\partial}_x - m)\,S_F(x - y) = i\delta^4(x - y)\,\mathbf 1 .
> $$
>
> It follows from three inputs and no mode expansion: the definition of $T$; the Dirac equation of the field operator, $(i\slashed{\partial} - m)\hat\psi = 0$ ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]]); and the equal-time anticommutator $\{\hat\psi_a(t, \mathbf x), \hat{\bar\psi}_b(t, \mathbf y)\} = (\gamma^0)_{ab}\,\delta^3(\mathbf x - \mathbf y)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] at every time, [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], 3; [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]). The source is the jump of $T$ at $x^0 = y^0$, met by the single time derivative ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]]); it is a $\delta$ because of the fermionic minus sign ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-6|Theorem §C5b.8.6]]).
>
> *Scalar analogue:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]] ($n = 1$).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact; an identity in $\mathcal S'$, the products with $\theta$ taken slice by slice ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]], 2).
>
> *Source: PHY 513, Problem Set 9, Problem 1(b) (the user's solution) · PHY 513 Lecture 17, slide 17 ("two independent derivations of the propagator (see HW)")*

^thm-c5b-8-4

> [!derivation]- Derivation
> **Step 1** (the definition). By [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]],
>
> $$
> S_F(x - y)_{ab} = \theta(x^0 - y^0)\,\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle - \theta(y^0 - x^0)\,\langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle .
> $$
>
> Both vacuum values are smooth in $x^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]; [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3), so the product rule holds slice by slice ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]], 2).
>
> **Step 2** (product rule). Applying $\slashed{\partial}_x$,
>
> $$
> \begin{aligned}
> (\gamma^\mu)_{ca}\,\partial_{x\mu}S_F(x - y)_{ab} ={}& (\gamma^\mu)_{ca}\bigl[\partial_{x\mu}\theta(x^0 - y^0)\bigr]\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle + (\gamma^\mu)_{ca}\,\theta(x^0 - y^0)\,\partial_{x\mu}\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle \\
> &- (\gamma^\mu)_{ca}\bigl[\partial_{x\mu}\theta(y^0 - x^0)\bigr]\langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle - (\gamma^\mu)_{ca}\,\theta(y^0 - x^0)\,\partial_{x\mu}\langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle .
> \end{aligned}
> $$
>
> **Step 3** (group the mass terms with the field terms). Multiply by $i$ and subtract $m\,\delta_{ca}S_F(x - y)_{ab}$. Since $\partial_{x\mu}$ does not act on $\hat{\bar\psi}_b(y)$, and $(\gamma^\mu)_{ca}$, $m\,\delta_{ca}$ are c-numbers, derivative and mass term move onto $\hat\psi_a(x)$ inside the vacuum values:
>
> $$
> \begin{aligned}
> (i\slashed{\partial}_x - m)_{ca}S_F(x - y)_{ab} ={}& i(\gamma^\mu)_{ca}\bigl[\partial_{x\mu}\theta(x^0 - y^0)\bigr]\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle - i(\gamma^\mu)_{ca}\bigl[\partial_{x\mu}\theta(y^0 - x^0)\bigr]\langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle \\
> &+ \theta(x^0 - y^0)\,\langle0|\bigl[(i\slashed{\partial}_x - m)_{ca}\hat\psi_a(x)\bigr]\hat{\bar\psi}_b(y)|0\rangle - \theta(y^0 - x^0)\,\langle0|\hat{\bar\psi}_b(y)\bigl[(i\slashed{\partial}_x - m)_{ca}\hat\psi_a(x)\bigr]|0\rangle .
> \end{aligned}
> $$
>
> **Step 4** (the field terms vanish). $(i\slashed{\partial}_x - m)_{ca}\hat\psi_a(x) = 0$ ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]]): the last two terms are zero. Dropped: the field terms, by the operator Dirac equation.
>
> **Step 5** (the jump). The step functions depend on $x$ only through $x^0$ ([[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], 2):
>
> $$
> \partial_{x\mu}\theta(x^0 - y^0) = \delta^0_\mu\,\delta(x^0 - y^0), \qquad \partial_{x\mu}\theta(y^0 - x^0) = -\delta^0_\mu\,\delta(x^0 - y^0) ,
> $$
>
> so only the $\gamma^0$ term is left, and the two minus signs (of $T$ and of the second derivative) make a plus:
>
> $$
> (i\slashed{\partial}_x - m)_{ca}S_F(x - y)_{ab} = i(\gamma^0)_{ca}\,\delta(x^0 - y^0)\Bigl(\langle0|\hat\psi_a(x)\hat{\bar\psi}_b(y)|0\rangle + \langle0|\hat{\bar\psi}_b(y)\hat\psi_a(x)|0\rangle\Bigr) .
> $$
>
> ⚑ By-product: one time derivative already produces the source → [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]]. ⚑ By-product: the plus sign in the bracket is the fermionic minus of $T$; with bosonic ordering the bracket would be a commutator → [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-6|Theorem §C5b.8.6]].
>
> **Step 6** (the bracket is the anticommutator at equal times). The bracket is $\langle0|\{\hat\psi_a(x), \hat{\bar\psi}_b(y)\}|0\rangle$, and $\delta(x^0 - y^0)$ sets it at equal times (a function smooth in $x^0$ with values in $\mathcal S'(\mathbb R^3)$ times $\delta(x^0 - y^0)$ is its value at $x^0 = y^0$ times $\delta$, as in Step 2 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-5|Derivation §C2b.6.5]]). With $\hat{\bar\psi}_b = \hat\psi^\dagger_d(\gamma^0)_{db}$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]]) and $\{\hat\psi_a(t, \mathbf x), \hat\psi^\dagger_d(t, \mathbf y)\} = \delta^3(\mathbf x - \mathbf y)\,\delta_{ad}$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]; at every $t$, [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], 3),
>
> $$
> \{\hat\psi_a(t, \mathbf x), \hat{\bar\psi}_b(t, \mathbf y)\} = \{\hat\psi_a(t, \mathbf x), \hat\psi^\dagger_d(t, \mathbf y)\}(\gamma^0)_{db} = \delta^3(\mathbf x - \mathbf y)\,(\gamma^0)_{ab} ,
> $$
>
> the equal-time value of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]].
>
> **Step 7** (assemble). With $\langle0|0\rangle = 1$ and $\delta(x^0 - y^0)\,\delta^3(\mathbf x - \mathbf y) = \delta^4(x - y)$ (a product of distributions in different variables),
>
> $$
> \begin{aligned}
> (i\slashed{\partial}_x - m)_{ca}S_F(x - y)_{ab} &= i(\gamma^0)_{ca}\,\delta(x^0 - y^0)\,\langle0|\delta^3(\mathbf x - \mathbf y)\,(\gamma^0)_{ab}|0\rangle \\
> &= i(\gamma^0)_{ca}(\gamma^0)_{ab}\,\delta(x^0 - y^0)\,\delta^3(\mathbf x - \mathbf y)\,\langle0|0\rangle = i(\gamma^0\gamma^0)_{cb}\,\delta^4(x - y) .
> \end{aligned}
> $$
>
> **Step 8** ($(\gamma^0)^2 = \mathbf 1$, [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]], 1). $(i\slashed{\partial}_x - m)_{ca}S_F(x - y)_{ab} = i\delta^4(x - y)\,\delta_{cb}$.
>
> **What the derivation shows**
> - The Dirac operator is first order in time: the source appears at the first derivative and is the equal-time anticommutator itself → [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]].
> - The source is a $\delta$ because the fermionic $T$ has a minus sign → [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-6|Theorem §C5b.8.6]].
> - The same equation was reached from the other end in [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]] (from $D_F$, and by solving for the transform); together with [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] it shows that the time-ordered product is the Feynman Green's function, not merely a function with the same transform.

^der-c5b-8-4

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-2|Theorem §C5b.6.2]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-1|Theorem §C5a.1.1]]

> [!theorem] Theorem §C5b.8.5: One Time Derivative: the Source Is the Equal-Time Anticommutator Itself
> The Dirac operator contains one time derivative, $i\gamma^0\partial_0$. Applied to the time-ordered product it meets the jump at $x^0 = y^0$ once, and the source is the equal-time anticommutator itself:
>
> $$
> (i\slashed{\partial}_x - m)_{ca}\,\langle0|T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}|0\rangle = i(\gamma^0)_{ca}\,\delta(x^0 - y^0)\,\langle0|\{\hat\psi_a(x), \hat{\bar\psi}_b(y)\}|0\rangle\Big|_{x^0 = y^0}, \qquad \{\hat\psi_a, \hat{\bar\psi}_b\}\Big|_{x^0 = y^0} = (\gamma^0)_{ab}\,\delta^3(\mathbf x - \mathbf y) .
> $$
>
> For the scalar the first time derivative meets $\langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle = 0$ at equal times, and the source comes only from the second, through $\langle0|[\hat\pi(x), \hat\phi(y)]|0\rangle = -i\delta^3(\mathbf x - \mathbf y)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]). The difference is the order of the field equation: the Dirac field's conjugate momentum $\hat\pi_a = i\hat\psi^\dagger_a$ is the field itself ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact.
>
> *Source: derived here from Step 5 of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-4|Derivation §C5b.8.4]] (PHY 513, Problem Set 9, Problem 1(b), the user's solution) and Steps 2–3 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-5|Derivation §C2b.6.5]]*

^thm-c5b-8-5

> [!derivation]- Derivation
> **Step 1** (Dirac: the jump at first order). Steps 2–5 of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-4|Derivation §C5b.8.4]]: of $i\slashed{\partial}_x - m = i\gamma^0\partial_0 + i\gamma^j\partial_j - m$ only $i\gamma^0\partial_0$ acts on the step functions, once, and leaves $i(\gamma^0)_{ca}\delta(x^0 - y^0)$ times the bracket $\langle0|\hat\psi_a\hat{\bar\psi}_b|0\rangle + \langle0|\hat{\bar\psi}_b\hat\psi_a|0\rangle = \langle0|\{\hat\psi_a(x), \hat{\bar\psi}_b(y)\}|0\rangle$; the rest acts on the fields and vanishes.
>
> **Step 2** (its value). Step 6 there: $\{\hat\psi_a, \hat{\bar\psi}_b\} = (\gamma^0)_{ab}\delta^3(\mathbf x - \mathbf y)$ at equal times.
>
> **Step 3** (the scalar, for comparison). Step 2 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-5|Derivation §C2b.6.5]]: $\partial_0D_F = \delta(t)\bigl[D_W(\xi) - D_W(-\xi)\bigr] + \dots$, with the bracket $\langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle$, zero at equal times; Step 3 there: $\partial_0^2D_F = \delta(t)\,\partial_{x^0}\langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle + \dots = \delta(t)\langle0|[\hat\pi(x), \hat\phi(y)]|0\rangle + \dots = -i\delta^4(x - y) + \dots$.
>
> **Step 4** (why the orders differ). The Klein–Gordon operator is second order in time, and its canonical pair is $(\hat\phi, \hat\pi = \partial_0\hat\phi)$: the commutator that is not zero pairs the field with its time derivative, so it appears only after one derivative has been taken. The Dirac Lagrangian is first order, its canonical pair is $(\hat\psi, i\hat\psi^\dagger)$ ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]), and the nonzero anticommutator pairs the field with its own adjoint: it appears at the first derivative.
>
> **What the derivation shows**
> - The order of the field equation decides which derivative produces the source; in both cases its strength is the canonical (anti)commutator.

^der-c5b-8-5

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-4|Derivation §C5b.8.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-5|Derivation §C2b.6.5]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]

> [!theorem] Theorem §C5b.8.6: The Fermionic Minus Sign of T Makes S_F a Green's Function
> With bosonic ordering, $T_{\rm B}\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\} \equiv \theta(x^0 - y^0)\,\hat\psi_a(x)\hat{\bar\psi}_b(y) + \theta(y^0 - x^0)\,\hat{\bar\psi}_b(y)\hat\psi_a(x)$, the jump term is the vacuum commutator at equal times,
>
> $$
> (i\slashed{\partial}_x - m)_{ca}\,\langle0|T_{\rm B}\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\}|0\rangle = i(\gamma^0)_{ca}\,\delta(x^0 - y^0)\,\langle0|[\hat\psi_a(x), \hat{\bar\psi}_b(y)]|0\rangle\Big|_{x^0 = y^0} ,
> $$
>
> and with $\mathbf r = \mathbf x - \mathbf y$, $\mathbf p\cdot\boldsymbol\gamma \equiv p^j\gamma^j$,
>
> $$
> \langle0|[\hat\psi_a(t, \mathbf x), \hat{\bar\psi}_b(t, \mathbf y)]|0\rangle = \int\frac{d^3p}{(2\pi)^3}\,\frac{(m - \mathbf p\cdot\boldsymbol\gamma)_{ab}}{E_{\mathbf p}}\,e^{i\mathbf p\cdot\mathbf r} = 2\bigl(m + i\gamma^j\partial_{r^j}\bigr)_{ab}\,D_W(0, \mathbf r) ,
> $$
>
> a function of $\mathbf r$ that is nonzero at every $\mathbf r \ne 0$ ($D_W$ at spacelike separation, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]), not $(\gamma^0)_{ab}\delta^3(\mathbf r)$. The source would then not be $i\delta^4$, and $\langle0|T_{\rm B}|0\rangle$ would not be a Green's function. The minus sign of fermionic time ordering turns the bracket into the anticommutator, whose equal-time value is $\gamma^0\delta^3$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]]). The other reason for the sign is frame independence ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-2|Theorem §C5b.8.2]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact.
>
> *Source: derived here; the positive half from PHY 513, Problem Set 9, Problem 1(b) (the user's solution: "The bracket is the vacuum expectation value of the anticommutator")*

^thm-c5b-8-6

> [!derivation]- Derivation
> **Step 1** (the same steps with a plus sign). Steps 1–5 of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-4|Derivation §C5b.8.4]] with $+\theta(y^0 - x^0)$: the field terms vanish by the Dirac equation as before, and the jump terms are $i(\gamma^0)_{ca}\bigl[\delta(x^0 - y^0)\langle0|\hat\psi_a\hat{\bar\psi}_b|0\rangle + (-\delta(x^0 - y^0))\langle0|\hat{\bar\psi}_b\hat\psi_a|0\rangle\bigr] = i(\gamma^0)_{ca}\,\delta(x^0 - y^0)\,\langle0|[\hat\psi_a(x), \hat{\bar\psi}_b(y)]|0\rangle$.
>
> **Step 2** (the commutator from the Wightman functions). $\langle0|[\hat\psi_a(x), \hat{\bar\psi}_b(y)]|0\rangle = S^+_W(\xi)_{ab} - S^-_W(\xi)_{ab}$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-1|Def. §C5b.7.1]]), and by [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], with $p^0 = E_{\mathbf p} \equiv E$,
>
> $$
> S^+_W(\xi) - S^-_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E}\Bigl[(\slashed{p} + m)\,e^{-ip\cdot\xi} - (\slashed{p} - m)\,e^{ip\cdot\xi}\Bigr] .
> $$
>
> **Step 3** (equal times). Restricting to $\xi^0 = 0$ is allowed ($S^\pm_W$ are smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$, [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3). There $p\cdot\xi = -\mathbf p\cdot\mathbf r$, so $e^{-ip\cdot\xi} = e^{i\mathbf p\cdot\mathbf r}$, $e^{ip\cdot\xi} = e^{-i\mathbf p\cdot\mathbf r}$, and $\slashed{p} = \gamma^0E - \mathbf p\cdot\boldsymbol\gamma$:
>
> $$
> S^+_W - S^-_W\Big|_{\xi^0 = 0} = \int\frac{d^3p}{(2\pi)^3\,2E}\Bigl[(\gamma^0E - \mathbf p\cdot\boldsymbol\gamma + m)\,e^{i\mathbf p\cdot\mathbf r} - (\gamma^0E - \mathbf p\cdot\boldsymbol\gamma - m)\,e^{-i\mathbf p\cdot\mathbf r}\Bigr] .
> $$
>
> **Step 4** (relabel the second term). $\mathbf p \to -\mathbf p$ there ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], 1; Jacobian $1$, $E$ unchanged) gives $(\gamma^0E + \mathbf p\cdot\boldsymbol\gamma - m)\,e^{i\mathbf p\cdot\mathbf r}$. The difference of the brackets is
>
> $$
> (\gamma^0E - \mathbf p\cdot\boldsymbol\gamma + m) - (\gamma^0E + \mathbf p\cdot\boldsymbol\gamma - m) = 2(m - \mathbf p\cdot\boldsymbol\gamma) :
> $$
>
> the $\gamma^0E$ terms cancel, and $\frac{2(m - \mathbf p\cdot\boldsymbol\gamma)}{2E}$ gives the first form of the statement.
>
> **Step 5** (in terms of $D_W$). With $\mathbf p\,e^{i\mathbf p\cdot\mathbf r} = -i\nabla_{\mathbf r}e^{i\mathbf p\cdot\mathbf r}$, so $-\mathbf p\cdot\boldsymbol\gamma\,e^{i\mathbf p\cdot\mathbf r} = i\gamma^j\partial_{r^j}e^{i\mathbf p\cdot\mathbf r}$, and $\int\frac{d^3p}{(2\pi)^3\,2E}\,e^{i\mathbf p\cdot\mathbf r} = D_W(0, \mathbf r)$ ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]]), the integral is $2(m + i\gamma^j\partial_{r^j})D_W(0, \mathbf r)$. At $\mathbf r \ne 0$ the point $(0, \mathbf r)$ is spacelike, where $D_W = \frac{m}{4\pi^2r}K_1(mr) \ne 0$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]): the function is not supported at $\mathbf r = 0$, so it is not a multiple of $\delta^3(\mathbf r)$.
>
> **Step 6** (the anticommutator, for comparison). With the fermionic sign the brackets of Step 4 are added: $(\gamma^0E - \mathbf p\cdot\boldsymbol\gamma + m) + (\gamma^0E + \mathbf p\cdot\boldsymbol\gamma - m) = 2\gamma^0E$, the $\frac{1}{2E}$ cancels, and $\int\frac{d^3p}{(2\pi)^3}\,\gamma^0e^{i\mathbf p\cdot\mathbf r} = \gamma^0\delta^3(\mathbf r)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]): the equal-time value of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]] again, by a second route.
>
> **What the derivation shows**
> - Only the sum $S^+_W + S^-_W$ is local at equal times; the difference is a smeared, nonzero function. The sign of $T$ is fixed twice: by frame independence ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-2|Theorem §C5b.8.2]]) and by the Green's-function property (this theorem).

^der-c5b-8-6

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-4|Derivation §C5b.8.4]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-1|Def. §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]

> [!theorem] Theorem §C5b.8.7: The Dirac Propagator as a Distribution
> 1. For $\varepsilon > 0$, $\tilde S^\varepsilon_F(p) = i(\slashed{p} + m)/(p^2 - m^2 + i\varepsilon)$ is a smooth matrix function of polynomial growth, a tempered distribution; as $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R^4)$,
>
> $$
> \tilde S^\varepsilon_F \to i(\slashed{p} + m)\,\mathcal P\frac{1}{p^2 - m^2} + \pi(\slashed{p} + m)\,\delta(p^2 - m^2) = (\slashed{p} + m)\tilde D_F ,
> $$
>
> the Sokhotski–Plemelj limit of $\tilde D_F$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]) multiplied by the polynomial $\slashed{p} + m$; the transform carries the limit to position space, so $S_F = \lim_{\varepsilon\to0^+}S^\varepsilon_F = (i\slashed{\partial} + m)D_F$ in $\mathcal S'$.
> 2. $S_F = \theta(\xi^0)S^+_W - \theta(-\xi^0)S^-_W$ is defined slice by slice: $S^\pm_W$ are smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$, and the value $\theta(0)$ does not enter.
> 3. Off $\xi = 0$ the products have disjoint singular supports; at $\xi = 0$ the slice definition is the unique extension that is a fundamental solution of the Dirac operator ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]).
>
> *Scalar analogue:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]].
>
> *Model:* any; *applies:* any theory (a statement about the function); its reading as a vacuum value in $|0\rangle$ needs the free field ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]).
>
> *Source: stated and derived here from [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]] and [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]] · PS §3.5, eq. (3.121)*

^thm-c5b-8-7

> [!derivation]- Derivation
> **1. Finite $\varepsilon$.** Each entry of $\slashed{p} + m$ is a polynomial of degree $1$ and $|p^2 - m^2 + i\varepsilon|^{-1} \le \varepsilon^{-1}$: smooth with polynomial growth, hence tempered ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2).
>
> **2. The limit.** Multiplication by a polynomial is continuous on $\mathcal S'$ (it maps $\mathcal S$ to itself continuously; [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1, and [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]): if $T_\varepsilon \to T$ then $P\,T_\varepsilon[\varphi] = T_\varepsilon[P\varphi] \to T[P\varphi]$. With $T_\varepsilon = \tilde D^\varepsilon_F \to i\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], 1; [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 1) and $P = \slashed{p} + m$, part 1 in momentum space. The inverse transform is continuous on $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2), and the transform of $(\slashed{p} + m)\tilde D_F$ is $(i\slashed{\partial} + m)D_F$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3).
>
> **3. Slices.** $S^\pm_W = \pm(i\slashed{\partial} + m)D_W(\pm\xi)$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]); $D_W(\pm\xi)$ are smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3; [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], Step 7), and so are their space and time derivatives. So the products with $\theta(\pm\xi^0)$ are defined as in Step 1 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-4|Derivation §C2b.6.4]]; they agree with part 1 by the second route of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
>
> **4. Uniqueness at the origin.** Away from $\xi = 0$, $\operatorname{sing\,supp}\theta(\pm\xi^0)$ (the plane $\xi^0 = 0$) and $\operatorname{sing\,supp}S^\pm_W$ (contained in the cone, as for $D_W$: [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 2; derivatives do not enlarge it) meet only at $0$ ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 2). Two extensions agreeing off $0$ differ by $T = \sum_\alpha C_\alpha\partial^\alpha\delta^4$ with constant matrices $C_\alpha$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]). If both satisfy $(i\slashed{\partial} - m)S = i\delta^4$, then $(i\slashed{\partial} - m)T = 0$; in transform $(\slashed{p} - m)P(p) = 0$ for the polynomial $P = \tilde T$; multiplying by $\slashed{p} + m$, $(p^2 - m^2)P(p) = 0$ ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]]), so $P = 0$.
>
> **What the derivation shows**
> - "$\varepsilon \to 0^+$ at the end" means the limit of distributions; the numerator does not interfere, being a polynomial.
> - The three definitions (contour, $i\varepsilon$, time-ordered product) give one distribution, as for the scalar.

^der-c5b-8-7

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]], [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]]

> [!theorem] Theorem §C5b.8.8: The Matrix Form of the Propagator
> For $m > 0$ and $\varepsilon > 0$ the matrix $\slashed{p} - m + i\varepsilon$ ([[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]]) is invertible for every real $p$, and as $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R^4)$,
>
> $$
> \frac{i}{\slashed{p} - m + i\varepsilon} \equiv i\,(\slashed{p} - m + i\varepsilon)^{-1} = \frac{i(\slashed{p} + m - i\varepsilon)}{p^2 - m^2 + 2im\varepsilon + \varepsilon^2} \;\to\; \tilde S_F(p) ,
> $$
>
> the limit of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]]. So $\tilde S_F = \dfrac{i}{\slashed{p} - m + i\varepsilon}$, PS's and the user's form, is a matrix inverse taken before the limit.
>
> *Model:* any; *applies:* any theory (a statement about the matrix function), $m > 0$; its reading as $\langle0|T\{\hat\psi\hat{\bar\psi}\}|0\rangle$ needs the free field ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]).
>
> *Source: the user's pre-course notes, §6.4 ("$1/(\slashed{p} - m + i\varepsilon)$ is understood as the inverse matrix") · PS §3.5, eq. (3.120) · the limit justified here*

^thm-c5b-8-8

> [!derivation]- Derivation
> **1. The inverse.** For a complex number $M$, $(\slashed{p} - M)(\slashed{p} + M) = \slashed{p}\slashed{p} - M^2 = p^2 - M^2$ ([[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]]; $M$ commutes with everything). With $M = m - i\varepsilon$: $p^2 - M^2 = p^2 - m^2 + 2im\varepsilon + \varepsilon^2$, whose imaginary part $2m\varepsilon$ is nonzero. So $(\slashed{p} - m + i\varepsilon)^{-1} = (\slashed{p} + m - i\varepsilon)/(p^2 - m^2 + 2im\varepsilon + \varepsilon^2)$.
>
> **2. The denominator.** Replacing $\varepsilon$ by $2m\varepsilon$ ($c = 2m > 0$ constant) does not change the limit ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 3); the added $\varepsilon^2$ moves the poles at fixed $\mathbf p$ to $\pm\sqrt{E^2 - \varepsilon^2 - 2im\varepsilon}$, on the same sides of the real axis, so the limit is again $\mathcal P\frac{1}{p^2 - m^2} - i\pi\delta(p^2 - m^2)$ (Step 3 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-10|Derivation §C2b.6.10]]).
>
> **3. The numerator.** $-i\varepsilon\cdot i/(p^2 - m^2 + \dots)$ is $\varepsilon$ times a convergent family: it tends to $0$. The rest is $(\slashed{p} + m)$ times the scalar limit, which is $\tilde S_F$ (Step 2 of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-7|Derivation §C5b.8.7]]).
>
> **What the derivation shows**
> - The compact form needs $m > 0$ for its $i\varepsilon$ to have a definite sign after inversion; for $m = 0$ use $i\slashed{p}/(p^2 + i\varepsilon)$.

^der-c5b-8-8

*Uses:* [[§C5a.14 Gamma-Matrix Technology#^thm-c5a-14-1|Theorem §C5a.14.1]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7|Theorem §C5b.8.7]]

## The two-point functions, all together

> [!definition] Definition §C5b.8.3: The Dirac Two-Point Family
> With $\xi = x - y$, vacuum expectation values in the vacuum of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^pr-c5b-3-4|Principle §C5b.3.4]], "homogeneous" meaning $(i\slashed{\partial} - m)S = 0$ and "Green's" meaning $(i\slashed{\partial} - m)S = i\delta^4$, each entry is $i\slashed{\partial} + m$ applied to the scalar function of [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]] in the same row:
>
> | name | definition | from the scalar family | momentum space (times $\int\frac{d^4p}{(2\pi)^4}e^{-ip\cdot\xi}$) | type, as a distribution |
> | --- | --- | --- | --- | --- |
> | Wightman $S^+_W$ | $\langle0\vert\hat\psi(x)\hat{\bar\psi}(y)\vert0\rangle$ | $(i\slashed{\partial} + m)D_W(\xi)$ | $2\pi(\slashed{p} + m)\theta(p^0)\delta(p^2 - m^2)$ | homogeneous; derivative of a boundary value — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1\|Theorem §C5b.7.1]] |
> | reversed $S^-_W$ | $\langle0\vert\hat{\bar\psi}(y)\hat\psi(x)\vert0\rangle$ | $-(i\slashed{\partial} + m)D_W(-\xi)$ | $-2\pi(\slashed{p} + m)\theta(-p^0)\delta(p^2 - m^2)$ | homogeneous — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1\|Theorem §C5b.7.1]] |
> | anticommutator $iS$ | $\langle0\vert\{\hat\psi(x), \hat{\bar\psi}(y)\}\vert0\rangle$ | $(i\slashed{\partial} + m)\,iD$ | $2\pi(\slashed{p} + m)\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ | homogeneous; supported in the closed cone — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3\|Theorem §C5b.7.3]] |
> | retarded $S_R$ | $\theta(\xi^0)\,iS$ | $(i\slashed{\partial} + m)D_R$ | $\frac{i(\slashed{p} + m)}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2}$ | Green's; slice product, forward support — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1\|Theorem §C5b.8.1]] |
> | advanced $S_A$ | $-\theta(-\xi^0)\,iS$ | $(i\slashed{\partial} + m)D_A$ | $\frac{i(\slashed{p} + m)}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2}$ | Green's; backward support — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1\|Theorem §C5b.8.1]] |
> | Feynman $S_F$ | $\langle0\vert T\{\hat\psi(x)\hat{\bar\psi}(y)\}\vert0\rangle$ | $(i\slashed{\partial} + m)D_F$ | $\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon}$ | Green's; limit $\varepsilon \to 0^+$ in $\mathcal S'$ — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-7\|Theorem §C5b.8.7]] |
>
> *Scalar analogue:* [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]].
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free vacuum $|0\rangle$, exact; with interactions the vacuum values in $|\Omega\rangle$ differ beyond lowest order (as for $S_F$, [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]).
>
> *Source: PS §3.5, eqs. (3.114)–(3.121) · Yu §6.4.5 · assembled here*

^def-c5b-8-3

> [!remark] Remark: Contractions of fermion fields (preview)
> As for the scalar ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]), $T\{\hat\psi_a(x)\hat{\bar\psi}_b(y)\} = \;:\!\hat\psi_a(x)\hat{\bar\psi}_b(y)\!: + S_F(x - y)_{ab}$ with the fermionic normal ordering of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]: $S_F$ is the contraction of $\hat\psi$ with $\hat{\bar\psi}$, while $\langle0|T\{\hat\psi\hat\psi\}|0\rangle = \langle0|T\{\hat{\bar\psi}\hat{\bar\psi}\}|0\rangle = 0$ (Yu (6.257)). Contractions of fermion fields change sign under exchange of the two fields, and Wick's theorem for fermions carries the sign of every permutation (the bosonic theorem is [[§C6a.6 Wick's Theorem#^thm-c6a-6-2|Theorem §C6a.6.2]]; fermions: [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|§C6d.3, Theorem §C6d.3.2]]; PS §4.7). Each internal fermion line of a Feynman diagram is a factor $\tilde S_F(p)$ (PS, after eq. (3.121); [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|§C6d.6, Theorem §C6d.6.2]]).
>
> *Source: Yu §6.4.5, eq. (6.257), §6.3 · the user's pre-course notes, "Wick's theorem" · PS §3.5, p. 63*

^rem-c5b-8-2

> [!remark]- Connections
> - The Dirac Green's functions are the scalar ones with $i\slashed{\partial} + m$ in front, the same relation that ties the Dirac two-point functions to $D_W$ and $D$ — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]].
> - The numerator $\slashed{p} + m$ of the propagator is the spin sum $\sum u\bar u$ continued off the shell; on the shell it projects onto the positive-energy spinors, which is why a propagator near its pole describes a real particle of spin $\frac12$ — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-10|Theorem §C5a.12.10]].
> - The one-particle propagator of Quantum Mechanics is retarded: its transform has the energy spectrum as poles, all pushed below the real axis by $E \to E + i\varepsilon$ ([[§C4.1 Propagators#^thm-c4-1-7|QM Theorem §C4.1.7]]). $S_F$ instead has its poles at $p^0 = \pm E_{\mathbf p}$ on opposite sides (the Feynman prescription), and the negative-frequency pole, which the one-particle Dirac theory read as a negative-energy state or a hole in the sea, is here an antifermion carried forward in time — [[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]].
> - The CA tools used: derivatives and supports of distributions ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), multiplication by polynomials and products with disjoint singular supports ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]), point-supported distributions ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]), the derivative rule and transforms in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]), relabelling ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]), the $i\varepsilon$ limits ([[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]]), residues and Jordan's lemma ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]).
> - Forward: Wick's theorem with fermion signs and the Yukawa and QED Feynman rules use $S_F$ for every internal fermion line — [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-1|§C6d.3, Theorem §C6d.3.1]], [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|§C6d.6, Theorem §C6d.6.2]] (Yukawa, Lecture 17; the QED rules follow in C6d, processes in C8, planned); charge conjugation and the CPT theorem, which guarantees equal masses of fermion and antifermion in general — [[§C9.6 Charge Conjugation on Oscillators and Spinors|§C9.6]], [[§C9.11 CPT and the CPT Theorem#^thm-c9-11-6|Theorem §C9.11.6]]; the path integral over anticommuting (Grassmann) fields reproduces $S_F$ as a Gaussian covariance — QFT C11 (planned), as [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|§C2b.6, Remark: The propagator as a Gaussian covariance (preview)]] does for $D_F$.
> - **Used in** (C6a): Theorem §C5b.8.3 — Dirac lines are oriented, $S_F$ not being even ([[§C6a.7 Feynman Diagrams for Correlation Functions#^thm-c6a-7-2|Theorem §C6a.7.2]], 2).
