---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.8
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c, draft]
---
← [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.9 Spin and Statistics]] →

*Sources: Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 62–63 · Yu Zhao-Huan, 量子场论讲义, §6.4.5 · the user's pre-course notes, the Dirac parts of "Time-ordered product and microcausality" and §6.4 ("Feynman Propagators: Dirac spinor field").*

*Draft: the Dirac propagator is in the reading for Lecture 10 (PS §3.5, eqs. (3.116)–(3.121)) but was not covered in the lecture; written from the user's pre-course notes, Yu and Peskin–Schroeder; to be revised when fermion propagators enter the course (Lectures 13–17: Wick's theorem, Yukawa theory).*

This is the spinor counterpart of [[§C2b.5 Green's Functions and Contours|§C2b.5]]–[[§C2b.7 Wick Rotation and the Two-Point Family|§C2b.7]] and the single home of the Dirac propagator $S_F$. Every Green's function of the Dirac operator is $i\slashed{\partial} + m$ applied to a Klein–Gordon Green's function, with the boundary condition (the contour) inherited unchanged; the spin-specific additions are the numerator $\slashed{p} + m$ (the spin sum continued off the shell), the normalization $(i\slashed{\partial} - m)S = +i\delta^4$, and the minus sign of fermionic time ordering. The contour work is [[P2 Green's Functions by Contour Integration]] with a numerator. Conventions as in [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality|§C5b.7]]; the Dirac Green's functions are normalized by $(i\slashed{\partial} - m)S = i\delta^4$ (PS).

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
> *Source: PS §3.5, eqs. (3.116)–(3.120) · stated here as distributions*

^thm-c5b-8-1

> [!derivation]- Derivation
> **1. The operator identity.** $(i\slashed{\partial} - m)(i\slashed{\partial} + m) = -\slashed{\partial}\slashed{\partial} + im\slashed{\partial} - im\slashed{\partial} - m^2 = -(\partial^2 + m^2)$, with $\slashed{\partial}\slashed{\partial} = \partial^2$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]; the partial derivatives commute, also on distributions).
>
> **2. Green's function.** $(i\slashed{\partial} - m)S_C = -(\partial^2 + m^2)D_C = -(-i\delta^4) = i\delta^4$, in $\mathcal S'$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]]; for $D_F$, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]]). ⚑ By-product: the Dirac normalization $+i\delta^4$ differs in sign from the Klein–Gordon $-i\delta^4$ because of the minus sign in Step 1 → Conventions of this note.
>
> **3. Momentum space.** $(\slashed{p} - m)\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon} = \frac{i(p^2 - m^2)}{p^2 - m^2 + i\varepsilon} = i - \frac{i\cdot i\varepsilon}{p^2 - m^2 + i\varepsilon}$; the last term is $\varepsilon$ times a family converging in $\mathcal S'$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]]), so it tends to $0$.
>
> **4. $S_R = (i\slashed{\partial} + m)D_R$.** $D_R = \theta(\xi^0)iD$ ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 1). Apply $i\slashed{\partial} + m = i\gamma^0\partial_0 + i\gamma^j\partial_j + m$ slice by slice. The spatial derivatives and $m$ act on $iD$ only. The time derivative obeys the product rule with $\partial_0\theta(\xi^0) = \delta(\xi^0)$ ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], 2): $\partial_0[\theta(\xi^0)iD] = \delta(\xi^0)\,iD + \theta(\xi^0)\,\partial_0iD$. Hence $(i\slashed{\partial} + m)[\theta(\xi^0)iD] = \theta(\xi^0)(i\slashed{\partial} + m)iD + i\gamma^0\delta(\xi^0)\,iD$. In the last term, $D$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3), so $\delta(\xi^0)D$ is $\delta(\xi^0)\otimes D(0, \cdot)$, and $D(0, \cdot) = 0$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]]). Dropped: the contact term, because the scalar field commutes with itself at equal times. What remains is $\theta(\xi^0)(i\slashed{\partial} + m)iD = \theta(\xi^0)\,iS$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]). (The same contact term is dropped for $S_F$ in the second route under [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].) The same with $-\theta(-\xi^0)$ for $S_A$. The transform is $(\slashed{p} + m)\tilde D_R$ with $\tilde D_R$ of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] (PS (3.120): closing below for $x^0 > y^0$ picks up both poles and gives $S^+_W + S^-_W$).
>
> **5. Support.** $\operatorname{supp}D_R$ is the closed forward cone ([[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 3), and derivatives do not enlarge supports (Step 1 of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^der-c5b-7-3|Derivation §C5b.7.3]]).
>
> **What the derivation shows**
> - Every Dirac Green's function is $i\slashed{\partial} + m$ applied to a Klein–Gordon one; the boundary condition (contour) is inherited unchanged.

^der-c5b-8-1

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]]

## Time ordering and the Feynman propagator

> [!definition] Definition §C5b.8.2: Time-Ordered Product of Fermion Fields
> For fermion fields the time-ordered product carries the sign of the permutation that puts the fields in time order:
>
> $$
> T\{\psi_a(x)\bar\psi_b(y)\} \equiv \theta(x^0 - y^0)\,\psi_a(x)\bar\psi_b(y) - \theta(y^0 - x^0)\,\bar\psi_b(y)\psi_a(x) ,
> $$
>
> and for $n$ fields $T\{\Phi_1\cdots\Phi_n\} = (-1)^P\,\Phi_{\sigma(1)}\cdots\Phi_{\sigma(n)}$ with times decreasing from left to right and $P$ the number of transpositions of fermion fields. This extends [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]], which it equals for boson fields.
>
> *Scalar analogue:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]].
> *Source: PS §3.5, eq. (3.121) and the text after it · Yu §6.4.5, eq. (6.258) and §6.3 · the user's pre-course notes, "Wick's theorem" (contractions of fermion fields)*

^def-c5b-8-2

> [!theorem] Theorem §C5b.8.2: Fermionic Time Ordering Is Frame Independent
> $T\{\psi_a(x)\bar\psi_b(y)\}$ of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]] is the same operator in every inertial frame. With a plus sign in place of the minus it would not be: at spacelike separation the two orderings would differ by $2\bar\psi_b(y)\psi_a(x) \ne 0$.
>
> *Scalar analogue:* Step 4 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-1|Derivation §C2b.6.1]] ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]]).
> *Source: the user's pre-course notes, "Time-ordered product and microcausality" ("the extra minus sign on swapping fermionic operators is what keeps $T[\psi_a(x)\bar\psi_b(y)]$ Lorentz invariant") · PS §3.5, p. 63*

^thm-c5b-8-2

> [!derivation]- Derivation
> **1. Timelike separation.** The sign of $x^0 - y^0$ is the same in every frame related by $SO^+(1,3)$ ([[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]]): every observer picks the same term.
>
> **2. Spacelike separation.** Observers disagree on which term applies. By [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], there $\psi_a(x)\bar\psi_b(y) = -\bar\psi_b(y)\psi_a(x)$, so the first term $\psi_a(x)\bar\psi_b(y)$ and the second $-\bar\psi_b(y)\psi_a(x)$ are the same operator: the disagreement is harmless. This is Step 4 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-1|Derivation §C2b.6.1]] with the anticommutator in place of the commutator.
>
> **3. With the wrong sign.** For $\theta\psi\bar\psi + \theta\bar\psi\psi$ the two terms at spacelike separation would be $\psi\bar\psi$ and $\bar\psi\psi = -\psi\bar\psi$, differing by $2\bar\psi\psi$, an operator with nonzero matrix elements (its vacuum value is $2S^-_W \ne 0$ there, [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).
>
> **What the derivation shows**
> - The sign in fermionic time ordering is not a convention: it is forced by Lorentz invariance once the fields anticommute outside the cone (PS: "this minus sign is extremely important in the quantum field theory of fermions").
> - At equal times and coincident points the anticommutator is $\gamma^0\delta^3$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]), the fermionic contact term; it is what makes $S_F$ a Green's function ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]).

^der-c5b-8-2

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]

> [!theorem] Theorem §C5b.8.3: The Dirac Feynman Propagator
> The Feynman propagator of the Dirac field, the vacuum expectation value of the fermionic time-ordered product ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]]), is
>
> $$
> S_F(x - y) \equiv \langle0|T\{\psi(x)\bar\psi(y)\}|0\rangle = \theta(\xi^0)S^+_W(\xi) - \theta(-\xi^0)S^-_W(\xi) = \int\frac{d^4p}{(2\pi)^4}\,\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon}\,e^{-ip\cdot\xi} = (i\slashed{\partial}_x + m)\,D_F(\xi) ,
> $$
>
> with $S^\pm_W$ of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], the Feynman contour, i.e. the $i\varepsilon$ prescription of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]] ($\varepsilon \to 0^+$ in $\mathcal S'$, [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]]), and the scalar Feynman propagator $D_F$ of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]. $\tilde S_F(p) = i(\slashed{p} + m)/(p^2 - m^2 + i\varepsilon)$ is the factor of an internal fermion line.
>
> *Scalar analogue:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]].
> *Source: PS §3.5, eq. (3.121) · Yu §6.4.5, eqs. (6.258)–(6.267) · the user's pre-course notes, §6.4 ("Dirac spinor field")*

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
> **4. Close the contour** ([[P2 Green's Functions by Contour Integration#^p2-4|P2, steps 4–5]]). The integrand behaves like $g(p^0)/(p^0)^2 \sim 1/|p^0|$, which tends to zero but not fast enough for the ML estimate: Jordan's lemma is needed ([[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]; [[§CA.4 Contour Integration#^cau-ca-4-1|§CA.4, Caution: Jordan's lemma needs g → 0]]: satisfied). For $t > 0$ close downward, clockwise, enclosing $E_\varepsilon$: $-2\pi i\cdot\frac{i}{2\pi}\frac{g(E_\varepsilon)e^{-iE_\varepsilon t}}{2E_\varepsilon} = \frac{g(E_\varepsilon)e^{-iE_\varepsilon t}}{2E_\varepsilon}$. For $t < 0$ close upward, counterclockwise, enclosing $-E_\varepsilon$: $2\pi i\cdot\frac{i}{2\pi}\frac{g(-E_\varepsilon)e^{iE_\varepsilon t}}{-2E_\varepsilon} = \frac{g(-E_\varepsilon)e^{iE_\varepsilon t}}{2E_\varepsilon}$ ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]). As $\varepsilon \to 0^+$ (pointwise for $t \ne 0$, bounded, hence in $\mathcal S'(\mathbb R)$, [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]]):
>
> $$
> \int\frac{dp^0}{2\pi}\frac{i\,g(p^0)\,e^{-ip^0t}}{(p^0)^2 - E^2 + i\varepsilon} \to \frac{1}{2E}\Bigl[\theta(t)g(E)e^{-iEt} + \theta(-t)g(-E)e^{iEt}\Bigr] ,
> $$
>
> the bracket of Step 2. (The value at $t = 0$ is a single point and carries no weight.) The denominator $(p^0)^2 - E^2 + i\varepsilon = p^2 - m^2 + i\varepsilon$; writing $2E\varepsilon$ or poles at $\pm(E - i\varepsilon)$ instead gives the same limit ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 3).
>
> **5. Combine** ([[P2 Green's Functions by Contour Integration#^p2-6|P2, step 6]]). Inserting into Step 2, $d^3p\,dp^0 = d^4p$, $e^{-ip^0t + i\mathbf p\cdot\boldsymbol\xi} = e^{-ip\cdot\xi}$ and $g(p^0) = \slashed{p} + m$: the four-dimensional formula (Yu (6.266)–(6.267)), as a limit in $\mathcal S'(\mathbb R^4)$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]]); the iterated integral is read as in [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], Step 2.
>
> **6. In terms of $D_F$.** $\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon} = (\slashed{p} + m)\tilde D_F$ with $\tilde D_F = \frac{i}{p^2 - m^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]), and $\slashed{p} + m$ is the transform of $i\slashed{\partial} + m$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3): $S_F = (i\slashed{\partial} + m)D_F$ ([[P2 Green's Functions by Contour Integration#^p2-7|P2, step 7]] checks it: [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]).
>
> **What the derivation shows**
> - Every step of P2 goes through with a numerator analytic in $p^0$; only the arc estimate changes (Jordan instead of ML).
> - For $x^0 > y^0$ the propagator is the fermion amplitude $\langle0|\psi\bar\psi|0\rangle$; for $x^0 < y^0$ it is minus the antifermion amplitude; the $i\varepsilon$ is the scalar's.

^der-c5b-8-3

*Uses:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-2|Def. §C5b.8.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]], [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§CA.2 Generalized Functions#^thm-ca-2-4|Theorem §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-4|Theorem §C2b.5.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]

> [!derivation]- Derivation (second route: from the scalar propagator)
> **1. Apply $i\slashed{\partial} + m$ to $D_F$ slice by slice.** $D_F = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]; slice products, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]]). With $\partial_0\theta(\pm\xi^0) = \pm\delta(\xi^0)$ ([[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], 2) and the product rule,
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
> - The Dirac propagator is a derivative of the scalar one; a contact term could have appeared and is absent because $[\phi(t, \mathbf x), \phi(t, \mathbf y)] = 0$.
>
> *Source: PS §3.5, eqs. (3.117), (3.121) · the user's pre-course notes, §6.4 ("the energy factors assemble into $\slashed{p}$")*

^der-c5b-8-3b

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]], [[§CA.2 Generalized Functions#^thm-ca-2-3|Theorem §CA.2.3]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]

*Procedure:* [[P2 Green's Functions by Contour Integration#^p2-1|P2, steps 1–7]]

> [!remark] Remark: Fermion forward, antifermion backward
> For $x^0 > y^0$, $S_F = \langle0|\psi(x)\bar\psi(y)|0\rangle$: $\bar\psi(y)$ creates a fermion at $y$, $\psi(x)$ annihilates it at $x$. For $x^0 < y^0$, $S_F = -\langle0|\bar\psi(y)\psi(x)|0\rangle$: $\psi(x)$ creates an antifermion at $x$ and $\bar\psi(y)$ annihilates it at $y$, later. One function carries positive energy forward in time in both cases, the fermion from $y$ to $x$ and the antifermion from $x$ to $y$, as the complex scalar's $\langle0|T\{\phi\phi^\dagger\}|0\rangle$ does ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]); the arrow on a fermion line in a Feynman diagram follows the charge, not the time (QFT C7, planned).
>
> *Source: the user's pre-course notes, §6.4 ("Complex scalar field": "a particle from $y$ to $x$ or an antiparticle from $x$ to $y$") · PS §3.5, eq. (3.121)*

^rem-c5b-8-1

> [!theorem] Theorem §C5b.8.4: The Dirac Propagator as a Distribution
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
> *Source: stated and derived here from [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]] and [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]] · PS §3.5, eq. (3.121)*

^thm-c5b-8-4

> [!derivation]- Derivation
> **1. Finite $\varepsilon$.** Each entry of $\slashed{p} + m$ is a polynomial of degree $1$ and $|p^2 - m^2 + i\varepsilon|^{-1} \le \varepsilon^{-1}$: smooth with polynomial growth, hence tempered ([[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], 2).
>
> **2. The limit.** Multiplication by a polynomial is continuous on $\mathcal S'$ (it maps $\mathcal S$ to itself continuously; [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1, and [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]): if $T_\varepsilon \to T$ then $P\,T_\varepsilon[\varphi] = T_\varepsilon[P\varphi] \to T[P\varphi]$. With $T_\varepsilon = \tilde D^\varepsilon_F \to i\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2)$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], 1; [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 1) and $P = \slashed{p} + m$, part 1 in momentum space. The inverse transform is continuous on $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], 2), and the transform of $(\slashed{p} + m)\tilde D_F$ is $(i\slashed{\partial} + m)D_F$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3).
>
> **3. Slices.** $S^\pm_W = \pm(i\slashed{\partial} + m)D_W(\pm\xi)$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]); $D_W(\pm\xi)$ are smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 3; [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], Step 7), and so are their space and time derivatives. So the products with $\theta(\pm\xi^0)$ are defined as in Step 1 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-4|Derivation §C2b.6.4]]; they agree with part 1 by the second route of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]].
>
> **4. Uniqueness at the origin.** Away from $\xi = 0$, $\operatorname{sing\,supp}\theta(\pm\xi^0)$ (the plane $\xi^0 = 0$) and $\operatorname{sing\,supp}S^\pm_W$ (contained in the cone, as for $D_W$: [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], 2; derivatives do not enlarge it) meet only at $0$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 2). Two extensions agreeing off $0$ differ by $T = \sum_\alpha C_\alpha\partial^\alpha\delta^4$ with constant matrices $C_\alpha$ ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]). If both satisfy $(i\slashed{\partial} - m)S = i\delta^4$, then $(i\slashed{\partial} - m)T = 0$; in transform $(\slashed{p} - m)P(p) = 0$ for the polynomial $P = \tilde T$; multiplying by $\slashed{p} + m$, $(p^2 - m^2)P(p) = 0$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]), so $P = 0$.
>
> **What the derivation shows**
> - "$\varepsilon \to 0^+$ at the end" means the limit of distributions; the numerator does not interfere, being a polynomial.
> - The three definitions (contour, $i\varepsilon$, time-ordered product) give one distribution, as for the scalar.

^der-c5b-8-4

*Uses:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4|Theorem §C2b.6.4]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6|Theorem §C2b.3.6]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§CA.2 Generalized Functions#^thm-ca-2-1|Theorem §CA.2.1]], [[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]]

> [!theorem] Theorem §C5b.8.5: The Matrix Form of the Propagator
> For $m > 0$ and $\varepsilon > 0$ the matrix $\slashed{p} - m + i\varepsilon$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]) is invertible for every real $p$, and as $\varepsilon \to 0^+$, in $\mathcal S'(\mathbb R^4)$,
>
> $$
> \frac{i}{\slashed{p} - m + i\varepsilon} \equiv i\,(\slashed{p} - m + i\varepsilon)^{-1} = \frac{i(\slashed{p} + m - i\varepsilon)}{p^2 - m^2 + 2im\varepsilon + \varepsilon^2} \;\to\; \tilde S_F(p) ,
> $$
>
> the limit of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]]. So $\tilde S_F = \dfrac{i}{\slashed{p} - m + i\varepsilon}$, PS's and the user's form, is a matrix inverse taken before the limit.
>
> *Source: the user's pre-course notes, §6.4 ("$1/(\slashed{p} - m + i\varepsilon)$ is understood as the inverse matrix") · PS §3.5, eq. (3.120) · the limit justified here*

^thm-c5b-8-5

> [!derivation]- Derivation
> **1. The inverse.** For a complex number $M$, $(\slashed{p} - M)(\slashed{p} + M) = \slashed{p}\slashed{p} - M^2 = p^2 - M^2$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]; $M$ commutes with everything). With $M = m - i\varepsilon$: $p^2 - M^2 = p^2 - m^2 + 2im\varepsilon + \varepsilon^2$, whose imaginary part $2m\varepsilon$ is nonzero. So $(\slashed{p} - m + i\varepsilon)^{-1} = (\slashed{p} + m - i\varepsilon)/(p^2 - m^2 + 2im\varepsilon + \varepsilon^2)$.
>
> **2. The denominator.** Replacing $\varepsilon$ by $2m\varepsilon$ ($c = 2m > 0$ constant) does not change the limit ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], 3); the added $\varepsilon^2$ moves the poles at fixed $\mathbf p$ to $\pm\sqrt{E^2 - \varepsilon^2 - 2im\varepsilon}$, on the same sides of the real axis, so the limit is again $\mathcal P\frac{1}{p^2 - m^2} - i\pi\delta(p^2 - m^2)$ (Step 3 of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^der-c2b-6-10|Derivation §C2b.6.10]]).
>
> **3. The numerator.** $-i\varepsilon\cdot i/(p^2 - m^2 + \dots)$ is $\varepsilon$ times a convergent family: it tends to $0$. The rest is $(\slashed{p} + m)$ times the scalar limit, which is $\tilde S_F$ (Step 2 of [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^der-c5b-8-4|Derivation §C5b.8.4]]).
>
> **What the derivation shows**
> - The compact form needs $m > 0$ for its $i\varepsilon$ to have a definite sign after inversion; for $m = 0$ use $i\slashed{p}/(p^2 + i\varepsilon)$.

^der-c5b-8-5

*Uses:* [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10|Theorem §C2b.6.10]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4|Theorem §C5b.8.4]]

## The two-point functions, all together

> [!definition] Definition §C5b.8.3: The Dirac Two-Point Family
> With $\xi = x - y$, vacuum expectation values in the vacuum of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], "homogeneous" meaning $(i\slashed{\partial} - m)S = 0$ and "Green's" meaning $(i\slashed{\partial} - m)S = i\delta^4$, each entry is $i\slashed{\partial} + m$ applied to the scalar function of [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]] in the same row:
>
> | name | definition | from the scalar family | momentum space (times $\int\frac{d^4p}{(2\pi)^4}e^{-ip\cdot\xi}$) | type, as a distribution |
> | --- | --- | --- | --- | --- |
> | Wightman $S^+_W$ | $\langle0\vert\psi(x)\bar\psi(y)\vert0\rangle$ | $(i\slashed{\partial} + m)D_W(\xi)$ | $2\pi(\slashed{p} + m)\theta(p^0)\delta(p^2 - m^2)$ | homogeneous; derivative of a boundary value — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1\|Theorem §C5b.7.1]] |
> | reversed $S^-_W$ | $\langle0\vert\bar\psi(y)\psi(x)\vert0\rangle$ | $-(i\slashed{\partial} + m)D_W(-\xi)$ | $-2\pi(\slashed{p} + m)\theta(-p^0)\delta(p^2 - m^2)$ | homogeneous — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1\|Theorem §C5b.7.1]] |
> | anticommutator $iS$ | $\langle0\vert\{\psi(x), \bar\psi(y)\}\vert0\rangle$ | $(i\slashed{\partial} + m)\,iD$ | $2\pi(\slashed{p} + m)\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ | homogeneous; supported in the closed cone — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3\|Theorem §C5b.7.3]] |
> | retarded $S_R$ | $\theta(\xi^0)\,iS$ | $(i\slashed{\partial} + m)D_R$ | $\frac{i(\slashed{p} + m)}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2}$ | Green's; slice product, forward support — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1\|Theorem §C5b.8.1]] |
> | advanced $S_A$ | $-\theta(-\xi^0)\,iS$ | $(i\slashed{\partial} + m)D_A$ | $\frac{i(\slashed{p} + m)}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2}$ | Green's; backward support — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1\|Theorem §C5b.8.1]] |
> | Feynman $S_F$ | $\langle0\vert T\{\psi(x)\bar\psi(y)\}\vert0\rangle$ | $(i\slashed{\partial} + m)D_F$ | $\frac{i(\slashed{p} + m)}{p^2 - m^2 + i\varepsilon}$ | Green's; limit $\varepsilon \to 0^+$ in $\mathcal S'$ — [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-4\|Theorem §C5b.8.4]] |
>
> *Scalar analogue:* [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]].
> *Source: PS §3.5, eqs. (3.114)–(3.121) · Yu §6.4.5 · assembled here*

^def-c5b-8-3

> [!remark] Remark: Preview: contractions of fermion fields
> As for the scalar ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]), $T\{\psi_a(x)\bar\psi_b(y)\} = \;:\!\psi_a(x)\bar\psi_b(y)\!: + S_F(x - y)_{ab}$ with the fermionic normal ordering of [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]: $S_F$ is the contraction of $\psi$ with $\bar\psi$, while $\langle0|T\{\psi\psi\}|0\rangle = \langle0|T\{\bar\psi\bar\psi\}|0\rangle = 0$ (Yu (6.257)). Contractions of fermion fields change sign under exchange of the two fields, and Wick's theorem for fermions carries the sign of every permutation (QFT C6, planned; PS §4.7). Each internal fermion line of a Feynman diagram is a factor $\tilde S_F(p)$ (PS, after eq. (3.121); QFT C7, planned).
>
> *Source: Yu §6.4.5, eq. (6.257), §6.3 · the user's pre-course notes, "Wick's theorem" · PS §3.5, p. 63*

^rem-c5b-8-2

> [!remark]- Connections
> - The Dirac Green's functions are the scalar ones with $i\slashed{\partial} + m$ in front, the same relation that ties the Dirac two-point functions to $D_W$ and $D$ — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.7 Wick Rotation and the Two-Point Family#^rem-c2b-7-2|§C2b.7, Remark: The two-point functions at a glance]].
> - The numerator $\slashed{p} + m$ of the propagator is the spin sum $\sum u\bar u$ continued off the shell; on the shell it projects onto the positive-energy spinors, which is why a propagator near its pole describes a real particle of spin $\frac12$ — [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-10|Theorem §C5a.6.10]].
> - The one-particle propagator of Quantum Mechanics is retarded: its transform has the energy spectrum as poles, all pushed below the real axis by $E \to E + i\varepsilon$ ([[§C4.1 Propagators#^thm-c4-1-7|QM Theorem §C4.1.7]]). $S_F$ instead has its poles at $p^0 = \pm E_{\mathbf p}$ on opposite sides (the Feynman prescription), and the negative-frequency pole, which the one-particle Dirac theory read as a negative-energy state or a hole in the sea, is here an antifermion carried forward in time — [[§C13.2★ The Dirac Equation#^rem-c13-2-7|QM Remark: The Dirac sea, the positron, and CPT]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-3|§C5b.5, Remark: The Dirac sea, read in the field]].
> - The CA tools used: derivatives and supports of distributions ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]), multiplication by polynomials and products with disjoint singular supports ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]), point-supported distributions ([[§CA.2 Generalized Functions#^thm-ca-2-2|Theorem §CA.2.2]]), the derivative rule and transforms in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-2|Theorem §CA.3.2]]), relabelling ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]), the $i\varepsilon$ limits ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-11|Theorem §CA.3.11]]), residues and Jordan's lemma ([[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]).
> - Forward: Wick's theorem with fermion signs and the Yukawa and QED Feynman rules use $S_F$ for every internal fermion line — QFT C6–C8 (planned); charge conjugation and the CPT theorem, which guarantees equal masses of fermion and antifermion in general — QFT C9 (planned); the path integral over anticommuting (Grassmann) fields reproduces $S_F$ as a Gaussian covariance — QFT C11 (planned), as [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-4|§C2b.6, Remark: Preview: the propagator as a Gaussian covariance]] does for $D_F$.
