---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): Differentiable Manifolds (591) §§40–41 (quaternions, $S^3 = SU(2)$, the double cover) · Quantum Mechanics §B6.1, §C5.2 · P. Woit, Quantum Theory, Groups and Representations, §6.2, Ch. 7 (§7.1 "The spinor representation"), Ch. 8 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · PHY 513 TA (oral remark, Oct 2026) · the user's PHY 513 notes, Ch. 7 §7.2 · the rest written here.*

What does the general construction of §CB.9 give in three dimensions, where everything is already known? The Pauli matrices realize the Clifford algebra of Euclidean $\mathbb R^3$, its even part is the quaternions, $\mathrm{Spin}(3)$ is the group of unit quaternions $= SU(2)$, and $\rho$ is the familiar double cover $SU(2) \to SO(3)$ that 591 proves by quaternion conjugation. The Pauli module $\mathbb C^2$ restricted to $\mathrm{Spin}(3)$ is spin ½, the representation that SO(3) lacks; and every half-integer spin sits inside spin ½ ⊗ (a representation of SO(3)) — the TA's theorem in its first case, before the Lorentz case of [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)|§CB.11]]–[[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.12]]. It builds on [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.6]] and [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.9]].

## The Clifford algebra of ℝ³

> [!theorem] Theorem §CB.10.1: The Pauli Matrices Realize Cl(3, 0)
> The Pauli matrices satisfy $\sigma^i\sigma^j + \sigma^j\sigma^i = 2\delta^{ij}\mathbb 1$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]), so $e_i \mapsto \sigma^i$ extends to an algebra homomorphism $\mathrm{Cl}(3,0) \to M_2(\mathbb C)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-7|Theorem §CB.7.7]]); it is an isomorphism of real algebras $\mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, and sends the volume element $\omega = e_1e_2e_3$ to $\sigma^1\sigma^2\sigma^3 = i\mathbb 1$. The two irreducible complex Clifford modules ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]], 2) are $\mathbb C^2$ with $e_i \mapsto \sigma^i$ and with $e_i \mapsto -\sigma^i$.
>
> *Source (planned): Woit, §6.2 · written here*

^thm-cb-10-1

> [!proof]- Proof (to be filled)
> *To be filled (surjective: $1$, $\sigma^i$, $i\sigma^i = \sigma^j\sigma^k$, $i\mathbb 1 = \sigma^1\sigma^2\sigma^3$ span $M_2(\mathbb C)$ over $\mathbb R$; both sides have real dimension $8$, Theorem §CB.7.16).*

^pf-cb-10-1

> [!theorem] Theorem §CB.10.2: The Even Part Is the Quaternions
> The linear map $\mathrm{Cl}^0(3,0) \to \mathbb H$ with $1 \mapsto 1$, $e_3e_2 \mapsto i$, $e_1e_3 \mapsto j$, $e_2e_1 \mapsto k$ is an isomorphism of real algebras ([[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]; [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-21|Theorem §CB.7.21]]). Under Theorem §CB.10.1, $\mathrm{Cl}^0(3,0)$ is $\{a\mathbb 1 - i\,\mathbf b\cdot\boldsymbol\sigma : a \in \mathbb R, \mathbf b \in \mathbb R^3\}$, with $e_3e_2 \mapsto -i\sigma^1$, $e_1e_3 \mapsto -i\sigma^2$, $e_2e_1 \mapsto -i\sigma^3$.
>
> *Source (planned): 591 §41–§42 · written here*

^thm-cb-10-2

> [!proof]- Proof (to be filled)
> *To be filled (the relations $i^2 = j^2 = k^2 = -1$, $ij = k$, $jk = i$, $ki = j$ follow from Theorem §CB.7.8; e.g. $(e_3e_2)(e_1e_3) = e_2e_1$).*

^pf-cb-10-2

## Spin(3) = SU(2)

> [!theorem] Theorem §CB.10.3: Spin(3) Is SU(2), and ρ Is the Double Cover SU(2) → SO(3)
> Under Theorem §CB.10.1, $\mathrm{Spin}(3)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-6|Def. §CB.9.6]]) is the group of unit quaternions ([[§41 The Unit Quaternions and SU(2)#^prop-41-4|591 Prop. §41.4]]) and maps onto $SU(2)$; it is connected and simply connected ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]]). The covering $\rho : \mathrm{Spin}(3) \to SO(3)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-12|Theorem §CB.9.12]]), $\rho(x)v = xvx^{-1}$, is conjugation of pure quaternions by unit quaternions ([[§42 SU(2) → SO(3)꞉ The Double Cover#^prop-42-1|591 Prop. §42.1]]), i.e. the double cover of [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]] and [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; a unit quaternion $\cos\frac\theta2 + \sin\frac\theta2\,u$ gives a rotation through the angle $\theta$ (591 Prop. §41.1, 3), the half angle of spin ½.
>
> *Source (planned): 591 §§40–41 · Woit, §6.2*

^thm-cb-10-3

> [!proof]- Proof (to be filled)
> *To be filled (an even product of unit vectors in $\mathbb R^3$ is a unit quaternion and conversely, by Theorem §CB.10.2; the rest is 591).*

^pf-cb-10-3

The double cover, proved in 591 by quaternion conjugation:

![[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4]]

> [!theorem] Theorem §CB.10.4: 𝔰𝔭𝔦𝔫(3) = 𝔰𝔲(2)
> Under Theorem §CB.10.1, $\mathfrak{spin}(3)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]]) is $\mathfrak{su}(2) = \operatorname{span}_{\mathbb R}\{-\frac i2\sigma^k\}$, with $\frac12e_ie_j \mapsto \frac i2\varepsilon_{ijk}\sigma^k$; and $\rho_\ast$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]]) is the isomorphism $\mathfrak{su}(2) \cong \mathfrak{so}(3)$, $-\frac i2\sigma^k \mapsto -iJ^k$, of [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]].
>
> *Source (planned): written here*

^thm-cb-10-4

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-10-4

## Spin ½ as the spinor representation, and the TA's theorem in three dimensions

> [!theorem] Theorem §CB.10.5: The Spinor Representation of Spin(3) Is Spin ½
> The spinor representation of $\mathrm{Spin}(3)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-18|Def. §CB.9.18]]) on the Pauli module $\mathbb C^2$ is, under $\mathrm{Spin}(3) \cong SU(2)$, the defining representation $D^{(1/2)}$: irreducible, with $-1 \mapsto -\mathbb 1$, hence spinorial and not a representation of $SO(3)$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], 2). Both irreducible Clifford modules give equivalent spinor representations ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-10|Theorem §CB.8.10]], 2).
>
> *Source (planned): Woit, §7.1 · written here*

^thm-cb-10-5

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-10-5

> [!theorem] Theorem §CB.10.6: The TA's Theorem in Three Dimensions
> Let $j \in \frac12 + \mathbb Z_{\ge0}$. Then $V_j$ is equivalent to a subrepresentation of $V_{1/2}\otimes V_{j - 1/2}$, where $V_{1/2}$ is the spinor representation (Theorem §CB.10.5) and $V_{j-1/2}$, of integer spin, is a representation of $SO(3)$ contained in $(\mathbb C^3)^{\otimes(j-1/2)}$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-8|Theorem §CB.6.8]]). Hence every spinorial representation of $SU(2) = \mathrm{Spin}(3)$ is contained in $S\otimes T$ with $T$ tensorial: part 3 of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-20|Theorem §CB.9.20]] for $n = 3$.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · planned for the proof: the Clebsch–Gordan series, [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-6|Theorem §CB.6.6]]*

^thm-cb-10-6

> [!proof]- Proof (to be filled)
> *To be filled ($V_{1/2}\otimes V_{j-1/2} \cong V_j\oplus V_{j-1}$ by Theorem §CB.6.6; complete reducibility and Theorem §CB.9.19 for a general spinorial representation).*

^pf-cb-10-6

> [!remark]- Connections
> - Three dimensions is where every step of §CB.9 can be checked by hand: Cartan–Dieudonné is unnecessary because 591 proves surjectivity of $SU(2) \to SO(3)$ directly ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]]), and the spinor representation is the spin ½ of Quantum Mechanics ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]: the sign of a $2\pi$ rotation).
> - The same pattern reappears for $\mathbb R^{1,3}$: Theorem §CB.7.20 turns $\mathrm{Cl}^0(1,3)$ into this section's $\mathrm{Cl}(3,0)$, so the Lorentz spin group is built from the Pauli matrices again (§CB.11).
> - **Used in**: Theorems §CB.10.1–§CB.10.4 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-1|Theorem §C3.1.1]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-1|§C5a.4, Remark: The rotation story, one level up]]; Theorem §CB.10.5 — [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-7|Theorem §C3.1.7]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-9|Theorem §C3.1.9]]; Theorem §CB.10.6 — [[§C3.1 Groups, Algebras and Representations of Rotations#^rem-c3-1-6|§C3.1, Remark: Spin j is 2j symmetrized spin-½ slots]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]].
