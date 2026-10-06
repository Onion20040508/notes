---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C5b
section: C5b.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C5b.6 The Heisenberg Dirac Field]] · ↑ [[· C5b The Quantum Spinor Field]] · [[§C5b.8 Green's Functions and the Dirac Feynman Propagator]] →

*Sources: the user's PHY 513 notes, Ch. 10 §10.4 (Derivation "Why anticommutators are causal and commutators are not") · PHY 513 Lecture 10 (Larsen, 5 Oct 2026), slide 6 and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §3.5, pp. 53–58 and 62–63 · Yu Zhao-Huan, 量子场论讲义, §6.4.5 · the user's pre-course notes, §5.5 and "Time-ordered product and microcausality".*

This is the spinor counterpart of [[§C2b.2 The Wightman Function|§C2b.2]]–[[§C2b.4 Microcausality and the Commutator Function|§C2b.4]]. What do the vacuum correlations of the Dirac field look like, and is the field causal? Every answer is the scalar answer with the operator $i\slashed{\partial} + m$ in front: the Wightman function $D_W$ becomes the pair $S^\pm_W$, the commutator function $D$ becomes the anticommutator function $S$, and microcausality becomes a statement about anticommutators. The explicit forms of $D_W$ ([[§C2b.3 Explicit Forms of the Wightman Function|§C2b.3]]) carry over by differentiation and get no section of their own. The third of Lecture 10's checkpoints ends the section: with commutators the field would propagate outside the light cone ("a Wightman function plus a different Wightman function"). Conventions as in [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]; in addition $\xi = x - y$, $t = \xi^0$, slash $\slashed{a} = \gamma^\mu a_\mu$ ([[§C5a.3 The Dirac Equation and Its Lagrangian#^def-c5a-3-2|Def. §C5a.3.2]]); scalar two-point functions as in [[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-2|Def. §C2b.7.2]] ($iD = \langle0|[\phi, \phi]|0\rangle$, $D_1 = D_W(\xi) + D_W(-\xi)$); Fourier convention $f(\xi) = \int\frac{d^4p}{(2\pi)^4}\tilde f(p)e^{-ip\cdot\xi}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^def-ca-3-1|Def. §CA.3.1]]). Spinor indices $a, b$ are written only where needed: $S_{ab}(\xi)$ is a $4\times4$ matrix of distributions.

> [!caution] Caution: The letter S
> In this chapter $S$ means several things: the spinor generators $S^{\mu\nu}$ ([[§C5a.2 The Clifford Algebra and the Dirac Representation#^def-c5a-2-3|Def. §C5a.2.3]]); the Lorentz matrix of a spinor, written $\Lambda_{1/2}$ here and $S(\Lambda)$ or $S[\Lambda]$ by Yu and in the user's pre-course notes; the action; the S-matrix (QFT C10, planned); and in this section the anticommutator function $S$ and the propagators $S_F$, $S_R$, $S_A$. The name $S$ for the anticommutator function (with $iS = \{\psi, \bar\psi\}$, parallel to $iD = [\phi, \phi]$) follows Bjorken–Drell; PS name only $S_R$ and $S_F$, Yu only $S_F$.
>
> *Source: PS §3.5, eqs. (3.116), (3.121) · Yu §6.4.5, eq. (6.258)*

^cau-c5b-7-1

## The Wightman functions

> [!definition] Definition §C5b.7.1: Dirac Wightman Functions
> For the quantized Dirac field ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] with the algebra of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]) and its vacuum ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]]),
>
> $$
> S^+_W(x - y)_{ab} \equiv \langle0|\psi_a(x)\,\bar\psi_b(y)|0\rangle, \qquad S^-_W(x - y)_{ab} \equiv \langle0|\bar\psi_b(y)\,\psi_a(x)|0\rangle ,
> $$
>
> the kernels of $\langle0|\psi(f)\bar\psi(g)|0\rangle$ and $\langle0|\bar\psi(g)\psi(f)|0\rangle$ for spacetime test functions, as $D_W$ is for the scalar ([[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]]).
>
> *Scalar analogue:* [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]].
> *Source: PS §3.5, eqs. (3.114)–(3.115) · Yu §6.4.5, eqs. (6.259)–(6.260)*

^def-c5b-7-1

> [!theorem] Theorem §C5b.7.1: The Dirac Wightman Functions from the Scalar One
> With the scalar Wightman function $D_W$ of [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]],
>
> $$
> S^+_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}(\slashed{p} + m)\,e^{-ip\cdot\xi} = (i\slashed{\partial}_x + m)\,D_W(\xi), \qquad S^-_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}(\slashed{p} - m)\,e^{ip\cdot\xi} = -(i\slashed{\partial}_x + m)\,D_W(-\xi) ,
> $$
>
> $p^0 = E_{\mathbf p}$: tempered distributions (derivatives of $D_W$, [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]) with transforms $2\pi(\slashed{p} + m)\theta(p^0)\delta(p^2 - m^2)$ and $-2\pi(\slashed{p} + m)\theta(-p^0)\delta(p^2 - m^2)$. Both solve the Dirac equation $(i\slashed{\partial}_x - m)S^\pm_W = 0$.
>
> *Scalar analogue:* [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]].
> *Source: PS §3.5, eqs. (3.114)–(3.115) · Yu §6.4.5, eqs. (6.259)–(6.260)*

^thm-c5b-7-1

> [!derivation]- Derivation
> **1. Which terms survive.** In [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], $\bar\psi(y)|0\rangle$ keeps only the $a^\dagger$ term and $\langle0|\psi(x)$ only the $a$ term, since $a|0\rangle = b|0\rangle = 0$ ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]]):
>
> $$
> S^+_W = \int\frac{d^3p\,d^3q}{(2\pi)^6\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\sum_{r,s}u^r(p)\bar u^s(q)\,e^{-ip\cdot x + iq\cdot y}\,\langle0|a^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle .
> $$
>
> **2. The vacuum expectation.** $\langle0|a^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]; Step 2 of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^der-c5b-4-2|Derivation §C5b.4.2]]). Integrating $\mathbf q$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1) and summing $s$ with $\sum_su^s\bar u^s = \slashed{p} + m$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]]) gives the first integral.
>
> **3. Pull the matrix out.** $i\partial^x_\mu e^{-ip\cdot\xi} = p_\mu e^{-ip\cdot\xi}$, so $(\slashed{p} + m)e^{-ip\cdot\xi} = (i\slashed{\partial}_x + m)e^{-ip\cdot\xi}$ and the integral is $(i\slashed{\partial}_x + m)\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}e^{-ip\cdot\xi} = (i\slashed{\partial}_x + m)D_W(\xi)$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]]). *Sense:* the mode integral is the action of $D_W$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], 2), and taking $\partial_\mu$ out is the derivative of a tempered distribution, which in transform is multiplication by $-ip_\mu$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3); with $\tilde D_W = 2\pi\theta(p^0)\delta(p^2 - m^2)$, $i\slashed{\partial} + m \to \slashed{p} + m$.
>
> **4. $S^-_W$.** Now $\psi(x)|0\rangle$ keeps the $b^\dagger$ term and $\langle0|\bar\psi(y)$ the $b$ term; $\langle0|b^r_{\mathbf p}b^{s\dagger}_{\mathbf q}|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$ and $\sum_sv^s_a\bar v^s_b = (\slashed{p} - m)_{ab}$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-8|Theorem §C5a.6.8]]) give $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}(\slashed{p} - m)e^{ip\cdot\xi}$. Since $i\partial^x_\mu e^{ip\cdot\xi} = -p_\mu e^{ip\cdot\xi}$, $(\slashed{p} - m)e^{ip\cdot\xi} = -(i\slashed{\partial}_x + m)e^{ip\cdot\xi}$, and $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}e^{ip\cdot\xi} = D_W(-\xi)$. The transform of $D_W(-\xi)$ is $2\pi\theta(-p^0)\delta(p^2 - m^2)$ ([[§C2b.4 Microcausality and the Commutator Function#^der-c2b-4-4|Derivation §C2b.4.4]], Step 4). ⚑ By-product: the minus sign comes from $\sum v\bar v = \slashed{p} - m$ and the sign of the exponent; it is the sign that makes the anticommutator, not the commutator, causal → [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]].
>
> **5. Dirac equation.** $(i\slashed{\partial} - m)(i\slashed{\partial} + m) = -\slashed{\partial}\slashed{\partial} - m^2 = -(\partial^2 + m^2)$, by $\slashed{a}\slashed{a} = a^2$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]]; the derivatives commute), and $(\partial^2 + m^2)D_W(\pm\xi) = 0$ ([[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]]).
>
> **What the derivation shows**
> - All spinor structure sits in the numerator $\slashed{p} + m$ from the spin sum; the space–time dependence is the scalar one.
> - The coincident value $S^+_W(0)$ inherits the singularity of $D_W(0)$; it is what normal ordering subtracts in $:\!\bar\psi\Gamma\psi\!:$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]] for the scalar).

^der-c5b-7-1

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^pr-c5b-4-1|Principle §C5b.4.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-8|Theorem §C5a.6.8]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-1|Theorem §C5a.7.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1|Theorem §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-2|Theorem §C2b.2.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

## The anticommutator function and microcausality

> [!definition] Definition §C5b.7.2: Anticommutator Function
> The **anticommutator function** $S(\xi)$ of the Dirac field is defined by
>
> $$
> iS(x - y)_{ab} \equiv \langle0|\{\psi_a(x), \bar\psi_b(y)\}|0\rangle ,
> $$
>
> the vacuum expectation value of the anticommutator of the Heisenberg fields ([[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]]), a $4\times4$ matrix of tempered distributions in $\xi = x - y$. The retarded and advanced functions built from it: [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-1|Def. §C5b.8.1]].
>
> *Scalar analogue:* the commutator function, $iD = \langle0|[\phi, \phi]|0\rangle$, [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|Def. §C2b.4.1]].
> *Source: PS §3.5, eqs. (3.116)–(3.117) · named here after Bjorken–Drell ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^cau-c5b-7-1|Caution: The letter S]])*

^def-c5b-7-2

> [!theorem] Theorem §C5b.7.2: The Field Anticommutator Is a c-Number
> For the quantized Dirac field ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]), at arbitrary $x$, $y$,
>
> $$
> \{\psi_a(x), \bar\psi_b(y)\} = iS_{ab}(x - y)\,\mathbf 1, \qquad S(\xi) = (i\slashed{\partial}_x + m)\,D(\xi), \qquad \{\psi_a(x), \psi_b(y)\} = 0 ,
> $$
>
> with the commutator function $D$ of [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|Def. §C2b.4.1]]: the same number in every state. As tempered distributions $\tilde S = -2\pi i\operatorname{sgn}(p^0)(\slashed{p} + m)\delta(p^2 - m^2)$, $(i\slashed{\partial} - m)S = 0$, and at equal times $iS(0, \boldsymbol\xi) = \gamma^0\delta^3(\boldsymbol\xi)$, which is [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]] again: $S$ carries the canonical anticommutators to all times.
>
> *Scalar analogue:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]].
> *Source: PS §3.5, p. 54 (the computation, there with commutators) and eq. (3.117) · the user's pre-course notes, "Time-ordered product and microcausality" (Note "The Dirac anticommutator from the spin sums")*

^thm-c5b-7-2

> [!derivation]- Derivation
> **1. Substitute both expansions.** In $\{\psi_a(x), \bar\psi_b(y)\}$, with [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] (variables $\mathbf p$, $\mathbf q$), only $\{a, a^\dagger\}$ and $\{b^\dagger, b\}$ are nonzero ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]), and they are c-numbers:
>
> $$
> \{\psi_a(x), \bar\psi_b(y)\} = \int\frac{d^3p\,d^3q}{(2\pi)^6\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\sum_{r,s}\Bigl(\{a^r_{\mathbf p}, a^{s\dagger}_{\mathbf q}\}u^r_a(p)\bar u^s_b(q)e^{-ip\cdot x + iq\cdot y} + \{b^{r\dagger}_{\mathbf p}, b^s_{\mathbf q}\}v^r_a(p)\bar v^s_b(q)e^{ip\cdot x - iq\cdot y}\Bigr) .
> $$
>
> **2. Integrate and sum.** As in Steps 2 and 4 of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^der-c5b-7-1|Derivation §C5b.7.1]]: $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}\bigl[(\slashed{p} + m)e^{-ip\cdot\xi} + (\slashed{p} - m)e^{ip\cdot\xi}\bigr] = S^+_W(\xi) + S^-_W(\xi)$ (the user's pre-course notes).
>
> **3. In terms of $D$.** By [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], $S^+_W + S^-_W = (i\slashed{\partial}_x + m)\bigl[D_W(\xi) - D_W(-\xi)\bigr] = (i\slashed{\partial}_x + m)\,iD(\xi)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]). Dividing by $i$: $S = (i\slashed{\partial} + m)D$. The transform follows from $\tilde D = -2\pi i\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 1) and the derivative rule ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]], 3).
>
> **4. Dirac equation.** $(i\slashed{\partial} - m)S = -(\partial^2 + m^2)D = 0$ (Step 5 of Derivation §C5b.7.1; [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3).
>
> **5. Equal times.** $D$ is smooth in $\xi^0$ with values in $\mathcal S'(\mathbb R^3)$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], 3), so its time derivatives may be restricted to $\xi^0 = 0$, and $D(0, \cdot) = 0$, $\partial_0D(0, \cdot) = -\delta^3$ ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]]). The spatial derivatives of $D(0, \cdot) = 0$ vanish, so $iS(0, \boldsymbol\xi) = i\cdot i\gamma^0\partial_0D(0, \boldsymbol\xi) = \gamma^0\delta^3(\boldsymbol\xi)$. On the other side, at equal times $\{\psi_a, \bar\psi_b\} = \{\psi_a, \psi^\dagger_c\}\gamma^0_{cb} = \gamma^0_{ab}\delta^3$ by [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]: consistent.
>
> **6. $\{\psi, \psi\}$.** Its expansion contains only $\{a, b^\dagger\}$ and $\{b^\dagger, a\}$, which vanish.
>
> **What the derivation shows**
> - The anticommutator is a c-number because the field is linear in mode operators whose anticommutators are c-numbers; the spinor structure is $i\slashed{\partial} + m$ acting on the scalar commutator function.
> - Used next: microcausality ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]]) and the retarded function ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]]).

^der-c5b-7-2

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-5|Theorem §CA.3.5]]

> [!theorem] Theorem §C5b.7.3: Microcausality of the Dirac Field
> 1. The anticommutator function $S$ of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^def-c5b-7-2|Def. §C5b.7.2]] vanishes, as a distribution, on the open spacelike region: $\operatorname{supp}S \subseteq \{\xi : \xi^2 \ge 0\}$ ([[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]]); at every spacelike $\xi$ it is the smooth function $0$.
> 2. For spacetime test functions $f, g \in \mathcal D(\mathbb R^4, \mathbb C^4)$ with spacelike-separated supports, $\{\psi(f), \bar\psi(g)\} = 0$, where $\psi(f) = \int d^4x\,f^\dagger\psi$, $\bar\psi(g) = \int d^4y\,\bar\psi g$: fermion fields smeared over spacelike-separated regions **anticommute**. Commutators of the fields do not vanish there.
>
> *Scalar analogue:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]].
> *Source: PS §3.5, p. 54 (with the anticommutator: p. 56) · the user's pre-course notes, "Time-ordered product and microcausality" · stated here as a support statement*

^thm-c5b-7-3

> [!derivation]- Derivation
> **1. Derivatives do not enlarge the support.** If a distribution $T$ vanishes on an open set $U$, so does $\partial_\mu T$: for $\varphi \in \mathcal D$ supported in $U$, $\partial_\mu T[\varphi] = -T[\partial_\mu\varphi] = 0$ because $\partial_\mu\varphi$ is supported in $U$ too ([[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]). Multiplication by constant matrices does not either.
>
> **2. Part 1.** $S = (i\slashed{\partial} + m)D$ ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]) and $D$ vanishes on the open spacelike region ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], 1), so $S$ does. There $D$ is the smooth function $0$, and so are its derivatives.
>
> **3. Part 2.** As in Step 2 of [[§C2b.4 Microcausality and the Commutator Function#^der-c2b-4-6|Derivation §C2b.4.6]]: $\{\psi(f), \bar\psi(g)\} = \int d^4x\,d^4y\,f^\dagger(x)\,iS(x - y)\,g(y)$, a pairing of $iS$ with a test function supported in $\{x - y\}$, a compact set of spacelike vectors; by part 1 it is zero.
>
> **4. The commutator does not vanish.** $[\psi_a(x), \bar\psi_b(y)] = 2\psi_a(x)\bar\psi_b(y) - \{\psi_a(x), \bar\psi_b(y)\}$; at spacelike separation this is $2\psi_a(x)\bar\psi_b(y)$, whose vacuum expectation $2S^+_W(\xi)$ is not zero there ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]; $D_W > 0$ at spacelike $\xi$, [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]).
>
> **What the derivation shows**
> - The scalar statement "the commutator vanishes outside the cone" becomes for fermions "the anticommutator vanishes outside the cone"; the support comes entirely from $D$.
> - The fields themselves therefore cannot be observables; observables built from them must still commute ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]]).

^der-c5b-7-3

*Uses:* [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§CA.2 Generalized Functions#^def-ca-2-3|Def. §CA.2.3]], [[§CA.2 Generalized Functions#^def-ca-2-4|Def. §CA.2.4]]

> [!theorem] Theorem §C5b.7.4: Bilinears Commute at Spacelike Separation
> For the fermion bilinears $\mathcal O_i(x) = \;:\!\bar\psi(x)\Gamma_i\psi(x)\!:$ of [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]] ($\Gamma_i$ constant $4\times4$ matrices; normal ordered, [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]),
>
> $$
> [\mathcal O_1(x), \mathcal O_2(y)] = 0 \qquad \text{for } (x - y)^2 < 0 ,
> $$
>
> as operator-valued distributions on the open set of spacelike pairs $(x, y)$. So the observables of the Dirac field (currents, energy and momentum densities) satisfy microcausality ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]).
>
> *Scalar analogue:* none needed for the scalar, whose field is itself an observable ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]).
> *Source: PS §3.5, p. 56 ("all reasonable observables … are built out of an even number of spinor fields") · the user's pre-course notes, "Time-ordered product and microcausality" · the commutator identity written out here*

^thm-c5b-7-4

> [!derivation]- Derivation
> **1. An identity.** For any operators $[AB, CD] = A\{B, C\}D - AC\{B, D\} + \{A, C\}DB - C\{A, D\}B$: expanding the right side gives $ABCD + ACBD - ACBD - ACDB + ACDB + CADB - CADB - CDAB = ABCD - CDAB$.
>
> **2. Apply it.** With $A = \bar\psi_a(x)(\Gamma_1)_{ab}$, $B = \psi_b(x)$, $C = \bar\psi_c(y)(\Gamma_2)_{cd}$, $D = \psi_d(y)$ (summed), and [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]]: $\{\psi_b(x), \bar\psi_c(y)\} = iS_{bc}(x - y)$, $\{\bar\psi_a(x), \psi_d(y)\} = iS_{da}(y - x)$, $\{\psi, \psi\} = \{\bar\psi, \bar\psi\} = 0$. So
>
> $$
> [\bar\psi\Gamma_1\psi(x), \bar\psi\Gamma_2\psi(y)] = \bar\psi(x)\Gamma_1\,iS(x - y)\,\Gamma_2\psi(y) - \bar\psi(y)\Gamma_2\,iS(y - x)\,\Gamma_1\psi(x) .
> $$
>
> **3. Normal ordering changes nothing.** $:\!\bar\psi\Gamma\psi\!:$ differs from $\bar\psi\Gamma\psi$ by a c-number (formally $-\operatorname{tr}\Gamma S^-_W(0)$, a coincident singularity removed by point splitting as for the scalar, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]), and c-numbers commute; the right side of Step 2 is then read with normal-ordered products plus c-number terms $\propto\operatorname{tr}\bigl(\Gamma_1S(x - y)\Gamma_2S^\pm_W(y - x)\bigr)$, each containing a factor $S(\pm(x - y))$.
>
> **4. Spacelike.** Every term carries $S(x - y)$ or $S(y - x)$, which vanishes on the open spacelike region ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], 1); there the remaining factors are distributions multiplied by the smooth function $0$ ([[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1), so each term is zero.
>
> **What the derivation shows**
> - Two anticommuting fermion fields make a commuting pair: the evenness of observables in $\psi$ is what reconciles anticommuting fields with commuting observables.

^der-c5b-7-4

*Uses:* [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-2|Theorem §C5b.7.2]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-3|Theorem §C5b.7.3]], [[§C5a.4 Bilinears, Chirality and the Weyl Equations#^def-c5a-4-1|Def. §C5a.4.1]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]], [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]]

> [!remark] Remark: Why a field may anticommute: observables are even
> Microcausality ([[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]) is a requirement on observables. A Dirac field is not one: it is not Hermitian, it changes the charge by one unit, and its matrix elements between states of fixed charge connect different charge sectors. Every quantity measured (charge, current, energy, momentum, particle number) contains an even number of spinor fields, and for those, anticommuting fields give commuting observables ([[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-4|Theorem §C5b.7.4]]). This is why the spin–statistics connection can put fermions on anticommutators without violating causality.
>
> *Source: PS §3.5, p. 56*

^rem-c5b-7-1

## Where the commutator version fails (third checkpoint)

> [!theorem] Theorem §C5b.7.5: A Dirac Field with Commutators Is Not Causal
> Let the Dirac field have the mode expansion of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] and a vacuum such that (i) $\langle0|\psi(x)\bar\psi(y)|0\rangle$ propagates only positive-energy fermions ($a$ annihilates the vacuum) and $\langle0|\bar\psi(y)\psi(x)|0\rangle$ only positive-energy antifermions ($b$ annihilates it); (ii) the vacuum is invariant under translations and rotations; (iii) norms are positive; (iv) the two-point functions are Lorentz invariant. Then
>
> $$
> \langle0|\psi(x)\bar\psi(y)|0\rangle = A\,S^+_W(\xi), \qquad \langle0|\bar\psi(y)\psi(x)|0\rangle = B\,S^-_W(\xi), \qquad A, B > 0 \text{ constants} ,
> $$
>
> with $S^\pm_W$ of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]]; and for $m > 0$ the vacuum expectation of $[\psi_a(x), \bar\psi_b(y)]$ is nonzero at every spacelike $\xi$, whereas that of $\{\psi_a(x), \bar\psi_b(y)\}$ vanishes at all spacelike $\xi$ if and only if $A = B$. Commutators are excluded by causality; anticommutators with $A = B = 1$ are the solution ([[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]]).
>
> *Scalar analogue:* none: for the scalar the commutator is the causal combination ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]).
> *Source: Lecture 10, slide 6 ("Propagation not causal. Commutators fail to vanish outside the light-cone") and transcript · the user's PHY 513 notes, Ch. 10 §10.1 and §10.4 · PS §3.5, pp. 54–56, eqs. (3.93)–(3.96)*

^thm-c5b-7-5

> [!derivation]- Derivation
> **1. The amplitude.** By (i) only $a$ in $\psi(x)$ and $a^\dagger$ in $\bar\psi(y)$ contribute: $\langle0|\psi(x)\bar\psi(y)|0\rangle = \int\frac{d^3p\,d^3q}{(2\pi)^6\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\sum_{r,s}u^r(p)\bar u^s(q)e^{-ip\cdot x + iq\cdot y}\langle0|a^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle$ (PS (3.93)), with no algebra assumed.
>
> **2. Translations and rotations.** If $e^{i\mathbf P\cdot\mathbf x}|0\rangle = |0\rangle$ and $a^{s\dagger}_{\mathbf q}$ creates momentum $\mathbf q$, then $\langle0|a^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle = e^{i(\mathbf p - \mathbf q)\cdot\mathbf x}\langle0|a^r_{\mathbf p}a^{s\dagger}_{\mathbf q}|0\rangle$ for all $\mathbf x$, so it is supported at $\mathbf p = \mathbf q$; rotation invariance makes it diagonal in $r, s$. PS write it as $(2\pi)^3\delta^3(\mathbf p - \mathbf q)\delta^{rs}A(\mathbf p)$.
>
> **3. Positivity.** For a packet, $\langle0|a^s(g)a^{s\dagger}(g)|0\rangle = \|a^{s\dagger}(g)|0\rangle\|^2 = \int\frac{d^3p}{(2\pi)^3}|g|^2A(\mathbf p) \ge 0$ for every $g$, so $A \ge 0$, and $A > 0$ if the fermion states exist.
>
> **4. Lorentz invariance.** Inserting Step 2 and $\sum_su^s\bar u^s = \slashed{p} + m$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]]): $\int\frac{d^3p}{(2\pi)^3 2E_{\mathbf p}}(\slashed{p} + m)A(\mathbf p)e^{-ip\cdot\xi}$. This is covariant only if $A$ is a function of $p^2 = m^2$, a constant (PS (3.94)). So $\langle0|\psi\bar\psi|0\rangle = A\,S^+_W$.
>
> **5. The other ordering.** The same steps with $b$, $b^\dagger$ and $\sum_sv^s\bar v^s = \slashed{p} - m$ ([[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-8|Theorem §C5a.6.8]]) give $\langle0|\bar\psi\psi|0\rangle = B\,S^-_W = -B(i\slashed{\partial}_x + m)D_W(-\xi)$ with $B > 0$ (PS (3.95)). The minus sign is the one of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^der-c5b-7-1|Derivation §C5b.7.1]], Step 4.
>
> **6. At spacelike $\xi$.** There $D_W(\xi) = D_W(-\xi) = D_W(r) = \frac{m}{4\pi^2r}K_1(mr)$, smooth and positive ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]; equal because $D$ vanishes there, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]]), as functions on an open set, so also their derivatives agree. Hence
>
> $$
> \langle0|[\psi, \bar\psi]|0\rangle = AS^+_W - BS^-_W = (A + B)(i\slashed{\partial} + m)D_W, \qquad \langle0|\{\psi, \bar\psi\}|0\rangle = AS^+_W + BS^-_W = (A - B)(i\slashed{\partial} + m)D_W .
> $$
>
> **7. Traces.** $\operatorname{tr}\gamma^\mu = 0$ ([[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]]), so $\operatorname{tr}\bigl[(i\slashed{\partial} + m)D_W\bigr] = 4mD_W(r) > 0$. The commutator has trace $4m(A + B)D_W \ne 0$: it does not vanish at any spacelike point. The anticommutator has trace $4m(A - B)D_W$, nonzero unless $A = B$; for $A = B$ it vanishes identically. (For $m = 0$ use the $\gamma$ part: $D_W = 1/4\pi^2r^2$ has nonzero gradient, and the same conclusion follows.)
>
> **What the derivation shows**
> - In the scalar commutator the particle term and the antiparticle term cancel outside the cone ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|§C2b.4, Remark: Two orderings that cancel; why antiparticles must exist]]); for the Dirac field the spin sum $\slashed{p} - m$ flips the sign of the antiparticle term, and the cancellation needs an anticommutator.
> - Assumptions used: (i)–(iv) and $m > 0$ or the gradient argument.

^der-c5b-7-5

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-7|Theorem §C5a.6.7]], [[§C5a.6 Normalization, Spin Sums and Helicity#^thm-c5a-6-8|Theorem §C5a.6.8]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]]

> [!derivation]- Derivation (second route, Lecture 10: "a Wightman function plus a different Wightman function")
> **1. The two orderings.** With $a|0\rangle = b|0\rangle = 0$ and $\langle0|aa^\dagger|0\rangle = \langle0|bb^\dagger|0\rangle = (2\pi)^3\delta^3$, the normalization the commutator version also has for its vacuum expectation values ($A = B = 1$ in the statement), [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]] gives
>
> $$
> \langle0|\psi_a(x)\bar\psi_b(y)|0\rangle = (i\slashed{\partial}_x + m)_{ab}D_W(x - y), \qquad \langle0|\bar\psi_b(y)\psi_a(x)|0\rangle = -(i\slashed{\partial}_x + m)_{ab}D_W(y - x) .
> $$
>
> The minus sign of the second comes from $\sum_sv^s\bar v^s = \slashed{p} - m$ and from $(i\slashed{\partial}_x + m)e^{ip\cdot(x-y)} = -(\slashed{p} - m)e^{ip\cdot(x-y)}$ (Step 4 of [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^der-c5b-7-1|Derivation §C5b.7.1]]).
>
> **2. Anticommutator: the difference.** Adding the two lines, $\langle0|\{\psi_a(x), \bar\psi_b(y)\}|0\rangle = (i\slashed{\partial}_x + m)_{ab}\bigl[D_W(x - y) - D_W(y - x)\bigr] = (i\slashed{\partial}_x + m)_{ab}\,iD(x - y)$, the commutator function of [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]] differentiated. It vanishes at spacelike separation, where $D$ vanishes on a whole neighbourhood and so do its derivatives ([[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]]).
>
> **3. Commutator: the sum.** Subtracting instead, $\langle0|[\psi_a(x), \bar\psi_b(y)]|0\rangle = (i\slashed{\partial}_x + m)_{ab}\bigl[D_W(x - y) + D_W(y - x)\bigr] = (i\slashed{\partial}_x + m)_{ab}\,D_1(x - y)$, the Hadamard function of [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|Def. §C2b.4.1]] differentiated.
>
> **4. The Hadamard function lives outside the cone.** At spacelike $\xi$, $D_W(\xi) = D_W(-\xi) = D_W(r) = \frac{m}{4\pi^2r}K_1(mr) > 0$ ([[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]]), so $D_1 = 2D_W$ there, a smooth positive function on an open set; its trace part $\operatorname{tr}[(i\slashed{\partial} + m)D_1] = 4m\cdot2D_W \ne 0$ ($\operatorname{tr}\gamma^\mu = 0$, [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]]). The commutator version propagates outside the light cone, "and not by a little bit" (Lecture 10).
>
> **What the derivation shows**
> - The minus sign that causality needs between the two Wightman terms is supplied by the anticommutator; for the scalar it was supplied by the commutator itself ([[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|§C2b.4, Remark: Two orderings that cancel; why antiparticles must exist]]).
> - This is the special case $A = B = 1$ of the first derivation; Peskin–Schroeder make the same comparison in eqs. (3.113)–(3.117).
>
> *Source: Lecture 10 (transcript: "you get a Wightman function plus a different Wightman function. Not good.") · the user's PHY 513 notes, Ch. 10 §10.4 (Derivation "Why anticommutators are causal and commutators are not (filled in)") · PS §3.5, pp. 54–56*

^der-c5b-7-5b

*Uses:* [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-1|Theorem §C5b.7.1]], [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1|Def. §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6|Theorem §C2b.4.6]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]], [[§C5a.7 Gamma-Matrix Technology#^thm-c5a-7-3|Theorem §C5a.7.3]]

> [!remark]- Connections
> - Every Dirac two-point function is $i\slashed{\partial} + m$ on a Klein–Gordon one, the field-theory form of "Dirac squares to Klein–Gordon": $(i\slashed{\partial} - m)(i\slashed{\partial} + m) = -(\partial^2 + m^2)$ — [[§C5a.3 The Dirac Equation and Its Lagrangian#^thm-c5a-3-10|Theorem §C5a.3.10]], [[§C2b.2 The Wightman Function#^def-c2b-2-1|Def. §C2b.2.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^def-c5b-8-3|Def. §C5b.8.3]].
> - Causality selects the statistics for the same reason it required antiparticles for the scalar: the particle and antiparticle terms of a two-point function must cancel outside the cone, and the spin sum $\slashed{p} - m$ supplies the sign that makes an anticommutator, not a commutator, do it — [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-2|§C2b.4, Remark: Two orderings that cancel; why antiparticles must exist]], [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^thm-c5b-7-5|Theorem §C5b.7.5]], [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]].
> - The anticommutator function carries the canonical anticommutators to all times, $iS(0, \boldsymbol\xi) = \gamma^0\delta^3(\boldsymbol\xi)$, as the commutator function carried the canonical commutators — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-11|Theorem §C2b.4.11]], [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]].
> - The coincident value of $S^\pm_W$ is the singular product that normal ordering subtracts in bilinears, the fermionic counterpart of the zero-point energy as a coincident Wightman function — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^rem-c2b-6-3|§C2b.6, Remark: The zero-point energy is the Wightman function at coincident points]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]].
> - Fields that anticommute at spacelike separation cannot themselves be observables; the evenness of observables in $\psi$ is a superselection statement that returns with charge conjugation and fermion number — [[§C5b.7 Wightman Functions, the Anticommutator Function and Microcausality#^rem-c5b-7-1|Remark: Why a field may anticommute: observables are even]], QFT C9 (planned).
