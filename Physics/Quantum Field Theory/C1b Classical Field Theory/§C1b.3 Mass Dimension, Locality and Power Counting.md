---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C1b
section: C1b.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C1b.2 The Action Principle and the Euler–Lagrange Equations]] · ↑ [[· C1b Classical Field Theory]] · [[§C1b.4 Hamiltonian Field Theory]] →

*Sources: the user's PHY 513 notes, Ch. 2 §2.4 (the action is dimensionless, dimensions in the scalar Lagrangian, units in the action, symmetry determines the action, locality and the principles of quantum field theory, relevant, marginal and irrelevant terms) · PHY 513 Lecture 2 (Larsen, 2 Sep 2026), Part C · Peskin & Schroeder, An Introduction to Quantum Field Theory, §2.2, §3.1 · Yu Zhao-Huan, 量子场论讲义, §1.2 and §1.6.2 · the user's pre-course notes, §1.2 and §1.6 · PHY 513, Problem Set 2, Problems 1(a) and 2(d), with the course solutions.*

Which terms may a relativistic Lagrangian contain, and which of them matter at long distances? The units are [[§C1a.2 Natural Units and Dimensional Analysis|§C1a.2]] (natural units, the mass dimension, the exponent rule and the counting rules, [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]]); the Lagrangian density and the action are [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-1|Def. §C1b.2.1]] and [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-2|Def. §C1b.2.2]], and the field laws they must respect are [[§C1b.1 Fields and Their Transformation Laws|§C1b.1]]. This section is Part C of Lecture 2, in its order: the action is dimensionless, which fixes the mass dimensions of fields and of couplings; locality and relativistic invariance restrict the form of the density; and power counting orders the remaining terms by their importance at low energy, which leaves the scalar Lagrangian with a handful of parameters.

*Conventions* ([[Larsen PHY 513]]): natural units $\hbar = c = 1$; $[Q]$ is the mass dimension of $Q$ ([[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-2|Def. §C1a.2.2]]); $g = \operatorname{diag}(+,-,-,-)$; $d$ is the number of spacetime dimensions, four unless stated otherwise.

## The action fixes the dimensions of fields and couplings


> [!theorem] Theorem §C1b.3.1: The Action Is Dimensionless
> In natural units every action is a pure number, $[S] = 0$. Consequently a Lagrangian density in $d$ spacetime dimensions has $[\mathcal L] = d$; in four dimensions
>
> $$
> [\mathcal L] = 4 .
> $$
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Principle "The master constraint") · PHY 513 Lecture 2, Part C · the user's pre-course notes, §1.2 (Note "Dimensions in natural units")*

^thm-c1b-3-1

> [!derivation]- Derivation
> **Step 1** (an action is a multiple of $\hbar$). An action has ordinary dimension $ML^2T^{-1}$ (energy times time). [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|Theorem §C1a.2.1]]: $d = 1 - 2 + 1 = 0$, and $a = \beta + \gamma = 1$, $b = -\beta - 2\gamma = 0$, so $S = (\text{pure number})\cdot\hbar$.
>
> **Step 2** (why it must be). In quantum mechanics the action enters only through the phase $e^{iS/\hbar}$ of the path integral ([[§C4.2 The Feynman Path Integral#^pr-c4-2-3|QM Principle §C4.2.3]]); the argument of the exponential must be dimensionless ([[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 2), which is Step 1 again.
>
> **Step 3** (the density). $S = \int d^dx\,\mathcal L$ ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-2|Def. §C1b.2.2]]). By rule 4 of Theorem §C1a.2.3, $[d^dx] = -d$, so $0 = [S] = -d + [\mathcal L]$ and $[\mathcal L] = d$.
>
> **Step 4** (check in ordinary units). With $S = \int dt\,d^3x\,\mathcal L_E$, $\mathcal L_E$ is an energy per volume, $ML^2T^{-2}\cdot L^{-3} = ML^{-1}T^{-2}$, and the exponent rule gives $d = 1 + 1 + 2 = 4$.
>
> **What the derivation shows.**
> - The four is the number of spacetime coordinates: the measure brings four powers of $(\text{mass})^{-1}$, and $\mathcal L$ must supply four powers of mass.
> - The user's notes take this as a principle ("the master constraint"); here it is a theorem, given the exponent rule and the phase $e^{iS/\hbar}$.
> - Used next: the dimensions of fields (Theorem §C1b.3.2) and couplings (Theorem §C1b.3.3).

^der-c1b-3-1

*Uses:* [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|Theorem §C1a.2.1]], [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], [[§C4.2 The Feynman Path Integral#^pr-c4-2-3|QM Principle §C4.2.3]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^def-c1b-2-2|Def. §C1b.2.2]]

> [!theorem] Theorem §C1b.3.2: Mass Dimension of Fields
> In $d$ spacetime dimensions, with canonically normalized kinetic terms,
>
> $$
> \tfrac12\partial_\mu\phi\,\partial^\mu\phi \;\Rightarrow\; [\phi] = \tfrac{d-2}{2}, \qquad \bar\psi\,i\gamma^\mu\partial_\mu\psi \;\Rightarrow\; [\psi] = \tfrac{d-1}{2}, \qquad -\tfrac14F_{\mu\nu}F^{\mu\nu} \;\Rightarrow\; [A_\mu] = \tfrac{d-2}{2};
> $$
>
> in four dimensions $[\phi] = 1$, $[\psi] = \frac32$, $[A_\mu] = 1$. The kinetic term fixes the mass dimension; no choice of units changes it.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Derivation "Dimensions in the scalar Lagrangian"; "Symmetry determines the action" for $\psi$ and $A$) · PHY 513 Lecture 2, Part C · PHY 513, Problem Set 2, Problem 2(d), course solution*

^thm-c1b-3-2

> [!derivation]- Derivation
> **Step 1** (scalar). By rules 3–4 of [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], $[\partial_\mu\phi\,\partial^\mu\phi] = 2(1 + [\phi])$; the factor $\frac12$ is a pure number. Setting this equal to $[\mathcal L] = d$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]): $2 + 2[\phi] = d$, $[\phi] = (d - 2)/2$.
>
> **Step 2** (spinor). The $\gamma^\mu$ are numerical matrices, and $\bar\psi$ has the dimension of $\psi$: $[\bar\psi\,\gamma^\mu\partial_\mu\psi] = 2[\psi] + 1 = d$, so $[\psi] = (d - 1)/2$.
>
> **Step 3** (vector). $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ has $[F] = [A] + 1$, so $[F_{\mu\nu}F^{\mu\nu}] = 2[A] + 2 = d$ and $[A] = (d - 2)/2$.
>
> **Step 4** (why the normalization decides). Rescaling $\phi \to \kappa\phi$ with a dimensionful constant $\kappa$ would change $[\phi]$ but multiply the kinetic term by $\kappa^2$; "canonical" means the coefficient is the pure number $\frac12$ ($1$ for $\bar\psi i\slashed{\partial}\psi$, $-\frac14$ for $F^2$), and that requirement defines $[\phi]$.
>
> ⚑ By-product: a field may enter with a non-canonical, dimensionful coefficient, and then its own dimension is different (the dilaton, [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-1|Example §C1b.3.1]]); a coefficient that is a pure number other than $\frac12$ (Problem Set 2, Problem 2 has $\partial_\mu\phi_1\partial^\mu\phi_1$) changes factors of $2$ but not dimensions.
>
> **What the derivation shows.**
> - $[\phi] = 1$, $[\pi] = [\dot\phi] = 2$, and $[\delta^3] = 3$ are consistent with $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$ ([[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]): $1 + 2 = 3$.
> - Used next: the dimensions of couplings (Theorem §C1b.3.3). The spinor and vector kinetic terms are derived in QFT C5a ([[§C5a.3 The Dirac Equation and Its Lagrangian#^mod-c5a-3-4|Model §C5a.3.4]]) and C4 ([[§C4.2★ The Proca Field#^mod-c4-2-1|Model §C4.2.1]], [[§C4.2★ The Proca Field#^rem-c4-2-1|§C4.2★, Remark: Why F² plus a mass term]]; Maxwell: [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^mod-c4-6-2|Model §C4.6.2]]).

^der-c1b-3-2

*Uses:* [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]

> [!theorem] Theorem §C1b.3.3: Mass Dimension of Couplings
> A term $g_{\mathcal O}\,\mathcal O$ in $\mathcal L$, with $[\mathcal O]$ the sum of the dimensions of its fields plus the number of its derivatives, has
>
> $$
> [g_{\mathcal O}] = d - [\mathcal O]; \qquad\text{for } g_n\phi^n:\quad [g_n] = d - n\,\frac{d - 2}{2} .
> $$
>
> In four dimensions $[g_n] = 4 - n$: the mass term has $[m^2] = 2$, $\phi^3$ a coupling of dimension $1$, $\phi^4$ a dimensionless coupling, and every term with $[\mathcal O] > 4$ ($\phi$, $A_\mu$ and each derivative counting $1$, $\psi$ counting $\frac32$) a coupling of negative dimension.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Derivation "Dimensions in the scalar Lagrangian", "The rule in general dimension") · PHY 513 Lecture 2, Part C · PHY 513, Problem Set 2, Problem 2(d), course solution*

^thm-c1b-3-3

> [!derivation]- Derivation
> **Step 1** (general term). By rule 1 of [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]] every term of $\mathcal L$ has dimension $[\mathcal L] = d$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]); by rule 3, $[g_{\mathcal O}\mathcal O] = [g_{\mathcal O}] + [\mathcal O]$. So $[g_{\mathcal O}] = d - [\mathcal O]$.
>
> **Step 2** ($\phi^n$). $[\phi^n] = n[\phi] = n(d - 2)/2$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]), so $[g_n] = d - n(d - 2)/2$; at $d = 4$, $[g_n] = 4 - n$.
>
> **Step 3** (the four-dimensional list). $\frac12m^2\phi^2$: $[m^2] = 2$, i.e. $[m] = 1$, as a mass must. $\lambda\phi^4$: $[\lambda] = 0$. $c_6\phi^6$: $-2$. $(\partial_\mu\phi\,\partial^\mu\phi)^2$: $[\mathcal O] = 4 + 4 = 8$, coupling $-4$. $\phi\,(\partial^2)^2\phi$: $[\mathcal O] = 2 + 4 = 6$, coupling $-2$. Yukawa $\bar\psi\psi\phi$: $3 + 1 = 4$, coupling $0$. Gauge $\bar\psi\gamma^\mu\psi A_\mu$: $3 + 1 = 4$, coupling $0$. Four-fermion $(\bar\psi\psi)^2$: $6$, coupling $-2$.
>
> **Step 4** (other dimensions). $d = 3$: $[\phi] = \frac12$, $[g_6] = 3 - 3 = 0$. $d = 6$: $[\phi] = 2$, $[g_3] = 6 - 6 = 0$. $d = 2$: $[\phi] = 0$ and $[g_n] = 2$ for every $n$, so every $\phi^n$ term carries a coupling of the same dimension as the mass term.
>
> ⚑ By-product: a coupling of negative dimension $-k$ must be built from a scale, $g = \tilde g/\Lambda^k$; its effects at energy $E$ are suppressed by $(E/\Lambda)^k$, which is the classification into relevant, marginal and irrelevant terms → [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]. Fermi's constant $G_F \simeq 1.17\times10^{-5}\ \text{GeV}^{-2}$ announces such a scale, $G_F^{-1/2} \simeq 300$ GeV.
>
> **What the derivation shows.**
> - In four dimensions $\phi^4$, Yukawa and gauge couplings are exactly the dimensionless ones; in three dimensions $\phi^6$ takes that role, in six $\phi^3$.
> - Used next: the ordering of terms by relevance ([[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|Theorem §C1b.3.6]]).

^der-c1b-3-3

*Uses:* [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]

> [!example] Example §C1b.3.1: A Field in an Exponent: the Dilaton
> In four dimensions consider $\mathcal L = -f^2e^{-2\tau}(\partial\tau)^2$ with $(\partial\tau)^2 = \partial_\mu\tau\,\partial^\mu\tau$. Find the mass dimensions of $\tau$ and $f$.
>
> **Step 1.** $\tau$ sits in an exponent, so $[\tau] = 0$ ([[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 2).
>
> **Step 2.** $[\partial_\mu\tau] = 0 + 1$, so $[(\partial\tau)^2] = 2$ (rules 3–4); $[e^{-2\tau}] = 0$.
>
> **Step 3.** $[\mathcal L] = 4$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]) gives $2[f] + 0 + 2 = 4$, so $[f] = 1$: the whole dimension of the kinetic term is carried by the constant.
>
> **Step 4** (the canonical field). For small $\tau$, $e^{-2\tau} \simeq 1$ and $\mathcal L \simeq -f^2(\partial\tau)^2$, which is $-\frac12(\partial\varphi)^2$ for $\varphi = \sqrt2\,f\tau$, the canonical form up to its overall sign, and $[\varphi] = 1$ as [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]] requires. A dimensionless field is a canonical field divided by a mass.
>
> (The overall sign does not affect dimensions or the field equation; with $g = \operatorname{diag}(+, -, -, -)$ it gives $\dot\tau^2$ a negative coefficient, the form that is standard with the mostly-plus metric. The field equation $\partial^2\tau = (\partial\tau)^2$ of part (b) is an Euler–Lagrange computation, [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]].)
>
> *Source: PHY 513, Problem Set 2, Problem 1(a), with the course solution · the user's PHY 513 notes, Ch. 2 §2.4 (Derivation "Dimensions of a field in an exponent: the dilaton")*

^ex-c1b-3-1

## Putting the units back in the action


> [!example] Example §C1b.3.2: Units Restored in the Scalar Action
> Restore $\hbar$ and $c$ in $S = \int d^4x\bigl(\frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2\bigr)$ and in the dispersion relation $\omega = \sqrt{\mathbf k^2 + m^2}$ of its plane waves.
>
> **Step 1** (target). $S/\hbar$ is a pure number ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]); so write $S/\hbar = \int d^4x\,\mathcal L$ and demand that this integral be dimensionless.
>
> **Step 2** (the measure). $d^4x = c\,dt\,d^3x$ has dimension $L^4$, so $\mathcal L$ must have dimension $L^{-4}$.
>
> **Step 3** (anchor: the gradient term). $\frac12(\nabla\phi)^2$ has dimension $[\phi]^2L^{-2}$; setting it equal to $L^{-4}$ gives $[\phi] = L^{-1}$ in this normalization ([[P4 Restoring ħ and c#^p4-5|P4, step 5]]).
>
> **Step 4** (match the time derivative). $(\partial_t\phi)^2$ has $[\phi]^2T^{-2}$; to match the anchor it needs $c^{-2}$: $\frac{1}{2c^2}(\partial_t\phi)^2$.
>
> **Step 5** (match the mass term). The coefficient of $\phi^2$ must be an inverse length squared; the length built from a mass is $\hbar/mc$ ([[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|Theorem §C1a.2.1]]), so $m^2 \to (mc/\hbar)^2 = m^2c^4/(\hbar c)^2$. Result:
>
> $$
> \frac S\hbar = \int c\,dt\,d^3x\,\Bigl[\frac{1}{2c^2}\Bigl(\frac{\partial\phi}{\partial t}\Bigr)^2 - \frac12(\nabla\phi)^2 - \frac12\Bigl(\frac{mc}{\hbar}\Bigr)^2\phi^2\Bigr].
> $$
>
> **Step 6** (dispersion). Everything an energy: $\omega \to \hbar\omega$, $k \to \hbar ck$, $m \to mc^2$, so $\hbar\omega = \sqrt{(\hbar c\mathbf k)^2 + (mc^2)^2}$, i.e. $E = \sqrt{(pc)^2 + (mc^2)^2}$ with $E = \hbar\omega$, $\mathbf p = \hbar\mathbf k$, the dispersion relation of [[§B4.1 The Klein–Gordon Equation#^thm-b4-1-5|REL Theorem §B4.1.5]].
>
> The Lecture 2 slide writes the first term as $\frac{1}{c^2}(\partial_t\phi)^2$ without the $\frac12$; the $\frac12$ is needed to match the natural-units Lagrangian.
>
> *Source: PHY 513 Lecture 2, Part C ("Dimensional Analysis") · the user's PHY 513 notes, Ch. 2 §2.4 (Derivation "Units in the scalar action")*

^ex-c1b-3-2

> [!caution] Caution: The physical dimension of a field is a normalization convention
> Example §C1b.3.2 found $[\phi] = L^{-1}$ because it put all constants into $\mathcal L$ and integrated over $c\,dt\,d^3x$. Requiring instead that $\mathcal L$ be an energy density, $ML^{-1}T^{-2}$, gives $[\phi] = (MLT^{-2})^{1/2}$, the dimension of the electrostatic potential in Heaviside–Lorentz units. Both are correct: they differ by a fixed power of $\hbar c$ absorbed into $\phi$, and both give mass dimension $1$ by [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|Theorem §C1a.2.1]]. What is not a convention is the mass dimension, fixed by the kinetic term ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Caution "The physical dimension of a field is a normalization convention")*

^cau-c1b-3-1

## Locality and symmetry

The action and its field equations are [[§C1b.2 The Action Principle and the Euler–Lagrange Equations|§C1b.2]]; dimensional analysis has fixed what each term costs. Two principles restrict which densities are allowed at all.

> [!principle] Principle §C1b.3.4: Locality
> The action of a field theory is the spacetime integral of a density,
>
> $$
> S = \int d^4x\;\mathcal L\bigl(\phi_a(x), \partial_\mu\phi_a(x), \dots\bigr) ,
> $$
>
> where $\mathcal L(x)$ depends on the fields and finitely many of their derivatives at the single point $x$.
>
> *Domain:* the long-distance description of any system, whatever its microscopic structure; nonlocal couplings of range $a$ appear at distances $\gg a$ as series of derivative terms ([[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-2|Remark: Why local terms dominate]]). The quantum statement of the same idea is microcausality ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Principle "Principles of quantum field theory": Locality) · PHY 513 Lecture 2, Part C ("Locality") · Yu §1.6.2 (局域: ℒ(x) depends on one spacetime point only) · PS §2.2, p. 15*

^pr-c1b-3-4

> [!principle] Principle §C1b.3.5: Relativistic Invariance
> The Lagrangian density is a scalar field when the fields transform by their laws ([[§C1b.1 Fields and Their Transformation Laws#^def-c1b-1-3|Def. §C1b.1.3]]): $\mathcal L'(x) = \mathcal L(\Lambda^{-1}(x - a))$ for every Poincaré transformation, and $\mathcal L$ is invariant under any internal symmetries the theory has. Then the action is invariant and the field equations are covariant ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-1|Theorem §C1b.2.1]]).
>
> *Domain:* relativistic field theory in flat spacetime; theories with a preferred frame (fluids, lattices, attempts at consistent violations of relativity) are outside it.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Principle "Principles of quantum field theory": Symmetry; "Symmetry determines the action") · PHY 513 Lecture 2, Part C ("The action is almost entirely determined by symmetry") · PS §3.1, eq. (3.5) · Yu §1.6.2 (relativistic field theory requires ℒ to be a Lorentz scalar) · the user's pre-course notes, §1.6 (Keypoint "Lorentz invariance of the action")*

^pr-c1b-3-5

> [!remark] Remark: The three principles of quantum field theory
> The lecture lists three: **locality** ([[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|Principle §C1b.3.4]]), **causality** (no effect outside the light cone; in the quantum theory, observables at spacelike separation commute: [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]) and **symmetry** ([[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-5|Principle §C1b.3.5]]), with dimensional analysis ordering the allowed terms by their importance at long distances ([[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]). The logic of the chapter: quantum field theory is a low-energy theory, and a low-energy theory is mostly determined by symmetry. That a single relativistic particle violates causality while the field does not is [[§C1a.3 Causal Structure and the Causality of a Single Particle|§C1a.3]] and [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]].
>
> *Source: PHY 513 Lecture 2, Part C ("Principles of Quantum Field Theory") · the user's PHY 513 notes, Ch. 2 §2.4*

^rem-c1b-3-1

> [!remark] Remark: Why local terms dominate at long distances
> The fundamental theory may be discrete (atoms on a lattice of spacing $a$) and may have nonlocal couplings, such as nearest-neighbour springs. A coupling between $\phi(\mathbf x)$ and $\phi(\mathbf x + \mathbf a)$, expanded for fields that vary slowly on the scale $a$, is $\phi(\mathbf x + \mathbf a) = \phi + a^i\partial_i\phi + \tfrac12a^ia^j\partial_i\partial_j\phi + \dots$: a series of local terms with more and more derivatives, each suppressed by one more power of $a$ times the inverse wavelength. This is how the bead chain becomes the wave equation ([[§B3.2 The Continuum Limit and the Wave Equation#^def-b3-2-1|WO Def. §B3.2.1]]). At long distances only the first few terms survive.
>
> *Source: PHY 513 Lecture 2, Part C ("Minor nonlocality becomes derivatives at long distance") · the user's PHY 513 notes, Ch. 2 §2.4 ("Locality and the principles of quantum field theory")*

^rem-c1b-3-2

## Power counting and the general scalar Lagrangian

By the theorems above, every term of $\mathcal L$ has mass dimension $4$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]]), a scalar field has $[\phi] = 1$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]), and a derivative $[\partial_\mu] = 1$. A term $g_{\mathcal O}\,\mathcal O$ built from an operator $\mathcal O$ with $n$ fields and $k$ derivatives therefore has a coupling of dimension $[g_{\mathcal O}] = 4 - [\mathcal O] = 4 - n - k$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]]).

> [!definition] Definition §C1b.3.1: Relevant, Marginal and Irrelevant Terms
> A term $g_{\mathcal O}\,\mathcal O$ of a Lagrangian density in four dimensions is **relevant** if $[g_{\mathcal O}] > 0$, **marginal** if $[g_{\mathcal O}] = 0$, and **irrelevant** if $[g_{\mathcal O}] < 0$, where $[g_{\mathcal O}] = 4 - [\mathcal O]$. In a theory valid below a scale $\Lambda$, an irrelevant coupling is $g_{\mathcal O} = \tilde g_{\mathcal O}/\Lambda^{k}$, $k = -[g_{\mathcal O}]$, with $\tilde g_{\mathcal O}$ of order one, and its effects at energy $E$ are suppressed by $(E/\Lambda)^{k}$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Definition "Relevant, marginal, irrelevant"; §"Dimensions order the terms") · PHY 513 Lecture 2, Part C ("Low Energy Effective Theory")*

^def-c1b-3-1

> [!remark] Remark: Why irrelevant terms die at low energy
> With nothing in the theory but $\Lambda$ to supply a negative dimension, $g_{\mathcal O} = \tilde g_{\mathcal O}\Lambda^{-k}$. In a process at energy $E$, fields vary on the scale $1/E$ ($\partial\phi \sim E\phi$), so the term competes with the marginal ones through the pure number $\tilde g_{\mathcal O}(E/\Lambda)^k \to 0$ for $E \ll \Lambda$. The lecture's slogan: derivatives are expensive, and since $[\phi] = [\partial_\mu]$, more fields cost as much as more derivatives. Relevant terms do the opposite: the mass term matters more, relative to $E$, the lower the energy.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 · PHY 513 Lecture 2, Part C*

^rem-c1b-3-3

> [!theorem] Theorem §C1b.3.6: Symmetry and Power Counting Fix the Scalar Lagrangian
> Let $\mathcal L$ be a local ([[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|Principle §C1b.3.4]]), Lorentz-invariant ([[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-5|Principle §C1b.3.5]]) polynomial in one real scalar field and its derivatives, with only relevant and marginal terms, a positive kinetic term and a potential bounded below. Up to total derivatives, a constant, a shift and a rescaling of $\phi$,
>
> $$
> \mathcal L = \tfrac12\,\partial_\mu\phi\,\partial^\mu\phi - V(\phi), \qquad V(\phi) = \tfrac12m^2\phi^2 + \frac{g}{3!}\phi^3 + \frac{\lambda}{4!}\phi^4 ,
> $$
>
> with $[m] = [g] = 1$, $[\lambda] = 0$, $\lambda \ge 0$. If $\mathcal L$ is invariant under $\phi \to -\phi$ and $V$ is smallest at $\phi = 0$, then $g = 0$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 ("Symmetry determines the action", eq. (V)) · PHY 513 Lecture 2, Part C ("Symmetry", "Low Energy Effective Theory": $V = \frac12m^2\phi^2 + \frac{1}{24}\lambda\phi^4$)*

^thm-c1b-3-6

> [!derivation]- Derivation
> **1. Monomials.** By locality, $\mathcal L$ is a finite sum of terms $c\,\mathcal O$, each $\mathcal O$ a product of $n$ factors $\phi$ and $k$ derivatives $\partial_{\mu_1}, \dots, \partial_{\mu_k}$ distributed over the factors, at one point.
>
> **2. Dimension.** $[\mathcal O] = n\,[\phi] + k\,[\partial] = n + k$, so $[c] = 4 - n - k$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]]). Relevant or marginal means $n + k \le 4$.
>
> **3. Lorentz invariance.** $\mathcal O$ carries $k$ lower indices; to be a scalar they must be contracted with invariant tensors, $g^{\mu\nu}$ or $\varepsilon^{\mu\nu\rho\sigma}$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]]; for ε, [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]). Each $g$ uses two indices and each $\varepsilon$ four, so $k$ is even. An $\varepsilon$ needs four derivatives, hence $k = 4$ and $n = 0$ by step 2: no field at all. So $k \in \{0, 2\}$, and every contraction is with $g$.
>
> **4. No derivatives, $k = 0$.** $n \le 4$: the operators $1, \phi, \phi^2, \phi^3, \phi^4$.
>
> **5. Two derivatives, $k = 2$.** $n \le 2$. For $n = 1$: $\partial_\mu\partial^\mu\phi = \partial_\mu(\partial^\mu\phi)$. For $n = 2$: $\partial_\mu\phi\,\partial^\mu\phi$ and $\phi\,\partial_\mu\partial^\mu\phi$. By the product rule $\phi\,\partial_\mu\partial^\mu\phi = \partial_\mu(\phi\,\partial^\mu\phi) - \partial_\mu\phi\,\partial^\mu\phi$.
>
> **6. Drop total derivatives.** $\partial_\mu(\partial^\mu\phi)$ and $\partial_\mu(\phi\,\partial^\mu\phi)$ are divergences and do not change the field equations ([[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]]). What remains is $\mathcal L = \tfrac Z2\,\partial_\mu\phi\,\partial^\mu\phi - (c_0 + c_1\phi + c_2\phi^2 + c_3\phi^3 + c_4\phi^4)$.
>
> **7. Normalize.** $Z > 0$ by assumption (a negative $Z$ makes the energy unbounded below: the Hamiltonian of [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]] with $\pi^2$ entering negatively). Rescale $\phi \to \phi/\sqrt Z$: the kinetic term becomes $\tfrac12\partial_\mu\phi\,\partial^\mu\phi$, and this normalization is what fixes $[\phi] = 1$.
>
> **8. The constant.** $c_0$ does not enter the field equations ($\partial\mathcal L/\partial\phi$ and $\partial\mathcal L/\partial(\partial_\mu\phi)$ do not see it). ⚑ By-product: it is a vacuum energy density, invisible to the field equations and to energy differences; gravity alone would see it. The quantum zero-point energy is a constant of the same kind ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]).
>
> **9. The linear term.** $V$ is a quartic polynomial bounded below, so $c_4 \ge 0$ and $V$ has a minimum at some $v$ (if $c_4 = 0$, boundedness forces $c_3 = 0$ and $c_2 \ge 0$; take $c_2 > 0$, or the theory is free and massless with $c_1 = 0$). Shift $\phi = v + \varphi$. Taylor's theorem for the polynomial gives $V(v + \varphi) = V(v) + V'(v)\varphi + \tfrac12V''(v)\varphi^2 + \tfrac16V'''(v)\varphi^3 + \tfrac1{24}V''''(v)\varphi^4$, exactly, and $V'(v) = 0$ at the minimum: the linear term is gone. $\partial_\mu\phi = \partial_\mu\varphi$ because $v$ is constant. ⚑ By-product: the shift is the choice of the vacuum, the configuration of least energy; $m^2 = V''(v) \ge 0$ is the curvature of $V$ there, and $\lambda = V''''(v) = 24c_4 \ge 0$ → [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-5|Remark: What the counting leaves out]].
>
> **10. Name the coefficients.** $V(v)$ is dropped (step 8). With $m^2 = V''(v)$, $g = V'''(v)$, $\lambda = V''''(v)$, $V = \tfrac12m^2\varphi^2 + \tfrac{g}{3!}\varphi^3 + \tfrac{\lambda}{4!}\varphi^4$; rename $\varphi \to \phi$. Dimensions by step 2: $[m^2] = 2$, $[g] = 1$, $[\lambda] = 0$.
>
> **11. The symmetry $\phi \to -\phi$.** If $\mathcal L$ is invariant, $V$ is even: $c_1 = c_3 = 0$. If moreover the minimum is at $v = 0$, no shift is needed, $g = V'''(0) = 6c_3 = 0$, and $V = \tfrac12m^2\phi^2 + \tfrac1{24}\lambda\phi^4$, the lecture's potential. ⚑ By-product: if instead $V$ is smallest at $v \neq 0$ ($c_2 < 0$), the shift of step 9 produces $g = \lambda v \neq 0$: the symmetry of $\mathcal L$ is not a symmetry of the vacuum (spontaneous symmetry breaking, beyond this chapter).
>
> **What the derivation shows**
> - Lorentz invariance removed every odd number of derivatives; power counting removed everything beyond two derivatives and four fields; total derivatives and field redefinitions removed the rest. Four numbers remain, one of them ($m$) already in the free theory.
> - Assumptions: polynomial $\mathcal L$ (locality with finitely many terms), positive kinetic term, $V$ bounded below; the counting is classical ("tree level").
> - Used next: the free theory ($g = \lambda = 0$) is [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^mod-c1b-2-6|Model §C1b.2.6]]; interactions $\phi^3$, $\phi^4$ are QFT C6 (planned).

^der-c1b-3-6

*Uses:* [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|Principle §C1b.3.4]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-5|Principle §C1b.3.5]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-2|REL Theorem §B2.2.2]], [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]]

> [!remark] Remark: Why not contract one derivative with a vector, A^μ∂_μφ
> A single derivative can be made invariant by contracting it with a vector $A^\mu$. But $A^\mu\partial_\mu\phi = \partial_\mu(A^\mu\phi) - \phi\,\partial_\mu A^\mu$. If $A^\mu$ is a constant vector, the term is a total derivative and does nothing, and a constant vector singles out a direction in spacetime, a preferred frame, which [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-5|Principle §C1b.3.5]] forbids. If $A^\mu$ is itself a field, what survives is $-\phi\,\partial_\mu A^\mu$, a coupling of two fields that presupposes a vector field with its own dynamics: the beginning of the spin-1 story ([[§C4.2★ The Proca Field#^mod-c4-2-1|Model §C4.2.1]], [[§C4.2★ The Proca Field#^rem-c4-2-1|§C4.2★, Remark: Why F² plus a mass term]]), not a kinetic term for $\phi$.
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (Discussion "Why not contract the derivative against a vector")*

^rem-c1b-3-4

> [!remark] Remark: What the counting leaves out
> - *Quantum corrections.* The labels are those of classical dimension counting. Quantum effects shift operator dimensions slightly, and a marginal coupling such as $\lambda$ acquires a slow, logarithmic dependence on energy: renormalization, later in the course.
> - *Naturalness.* A relevant term is dangerous as well as important: $m \ll \Lambda$ is natural only if something prevents the microphysics from generating $m \sim \Lambda$. Why scalars are light compared with the cutoff is a question, not an answer.
> - *Other spins.* The same counting gives $[\psi] = \tfrac32$ from $\bar\psi i\gamma^\mu\partial_\mu\psi$ and $[A_\mu] = 1$ from $F_{\mu\nu}F^{\mu\nu}$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]]), so the Yukawa coupling $\bar\psi\psi\phi$ and the gauge coupling $\bar\psi\gamma^\mu\psi A_\mu$ are marginal while a four-fermion term $(\bar\psi\psi)^2$ has a coupling of dimension $-2$. Fermi's constant $G_F \simeq 1.17\times10^{-5}\ \mathrm{GeV}^{-2}$ therefore announces the scale $G_F^{-1/2} \simeq 300\ \mathrm{GeV}$, where the weak interaction needs a better description (the electroweak theory, beyond PHY 513).
>
> *Source: the user's PHY 513 notes, Ch. 2 §2.4 (the two remarks after the Definition "Relevant, marginal, irrelevant"; "Symmetry determines the action")*

^rem-c1b-3-5

> [!remark]- Connections
> - $[S] = 0$ is the statement that $S/\hbar$ is a phase in Feynman's sum over paths ([[§C4.2 The Feynman Path Integral#^pr-c4-2-3|QM Principle §C4.2.3]]); the classical limit is the regime $S \gg \hbar$ ([[§C4.2 The Feynman Path Integral#^ex-c4-2-2|QM Example §C4.2.2]]).
> - The mode expansion of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] is dimensionally consistent: $[\hat\phi] = 1 = [d^3p] - \frac12[E_{\mathbf p}] + [\hat a_{\mathbf p}]$ gives $[\hat a_{\mathbf p}] = -\frac32$, matching $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ of dimension $-3$ ([[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]); then $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\hat a^\dagger_{\mathbf p}|0\rangle$ has dimension $-1$ and $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3$ dimension $-2$ ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]). The zero-point energy $V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$ has $-3 + 3 + 1 = 1$, an energy ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]).
> - The counting of [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]] is what makes "quantum field theory is the long-distance description" ([[§C1a.1 Why Quantum Field Theory#^rem-c1a-1-3|Remark: Fields as the long-distance description]]) operational: only finitely many couplings are not suppressed by powers of $E/\Lambda$ ([[§C1b.3 Mass Dimension, Locality and Power Counting#^def-c1b-3-1|Def. §C1b.3.1]]); the dimensionless ones (in four dimensions $\phi^4$, Yukawa, gauge) are those of the renormalizable theories of QFT C6–C8 (planned).
> - Theorems §C1b.3.2–§C1b.3.3 for $N$ scalar fields: the renormalizable potential has couplings of mass dimension 3, 2, 1 and 0, and the mass matrix is the only relevant coupling with two field indices ([[§R1.1 N Real Scalar Fields and Their Potential#^thm-r1-1-2|Thesis Thm. §R1.1.2]]).
> - Locality of the action and microcausality of the quantum field are two forms of one requirement: interactions happen at points, and observables at spacelike separation commute — [[§C1b.3 Mass Dimension, Locality and Power Counting#^pr-c1b-3-4|Principle §C1b.3.4]], [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-5|Remark: Microcausality and the domain of dependence are one statement]].
> - A lattice with nearest-neighbour springs becomes a local field theory at long wavelengths, the gradient term arising from the springs; with an extra spring to each site's rest position the mass term appears — [[§C1b.3 Mass Dimension, Locality and Power Counting#^rem-c1b-3-2|Remark: Why local terms dominate]], [[§B3.2 The Continuum Limit and the Wave Equation#^def-b3-2-1|WO Def. §B3.2.1]], [[§B4.1 The Klein–Gordon Equation#^rem-b4-1-2|REL Remark: The building blocks, and why the signs are physics]].
> - Relativity B already found the free scalar Lagrangian as "the most general quadratic density"; power counting is the stronger statement that interactions are limited to $\phi^3$ and $\phi^4$ — [[§B4.1 The Klein–Gordon Equation#^mod-b4-1-3|REL Model §B4.1.3]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-6|Theorem §C1b.3.6]].
> - The constant dropped from $\mathcal L$ and the zero-point energy dropped by normal ordering are the same kind of quantity, a vacuum energy invisible to the dynamics of flat spacetime — [[§C1b.3 Mass Dimension, Locality and Power Counting#^der-c1b-3-6|Derivation §C1b.3.6]], step 8; [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|Remark: Why the zero-point energy is dropped]].
> - The mass of the field is the curvature of the potential at its minimum, as the frequency of small oscillations is the curvature of a mechanical potential — [[§C1b.3 Mass Dimension, Locality and Power Counting#^der-c1b-3-6|Derivation §C1b.3.6]], step 9; [[§B6.5 Small Oscillations about Equilibrium|CM §B6.5]].
> - Dimensional analysis in natural units supplies $[\phi] = 1$ and $[\mathcal L] = 4$, on which the classification of terms rests — [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-1|Theorem §C1b.3.1]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]].
> - The scalar Lagrangian of Theorem §C1b.3.6 with $N$ real fields is the setup of the honors-thesis scalar-mass notes; the kinetic term can be made canonical, after which the only freedom of basis is $O(N)$ and the quadratic coupling is a mass matrix ([[§R1.1 N Real Scalar Fields and Their Potential#^mod-r1-1-1|Thesis Model §R1.1.1]], [[§R1.1 N Real Scalar Fields and Their Potential#^thm-r1-1-7|Thesis Thm. §R1.1.7]]).
> - Read the other way, the estimate of Remark: Why irrelevant terms die at low energy says a relevant coupling is naturally of order $\Lambda^{[g]}$; for a scalar mass this is the hierarchy problem ([[§R1.5★ Radiative Corrections, Naturalness and the Hierarchy Problem#^def-r1-5-3|Thesis Def. §R1.5.3]]), with its Wilsonian reading and 't Hooft's technical naturalness in [[§R1.5★ Radiative Corrections, Naturalness and the Hierarchy Problem#^rem-r1-5-6|Thesis Remark §R1.5.6]] and [[§R1.5★ Radiative Corrections, Naturalness and the Hierarchy Problem#^def-r1-5-4|Thesis Def. §R1.5.4]].
