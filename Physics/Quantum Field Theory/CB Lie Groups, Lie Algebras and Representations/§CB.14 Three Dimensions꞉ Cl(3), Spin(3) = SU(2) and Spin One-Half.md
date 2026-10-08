---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.14
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover]] →

*Sources: Differentiable Manifolds (591) §§41–42 (quaternions, $S^3 = SU(2)$, the double cover) · Quantum Mechanics §B6.1, §C5.2 · P. Woit, Quantum Theory, Groups and Representations, §6.2, §28.2, §29.2 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · PHY 513 TA (oral remark, Oct 2026) · the user's PHY 513 notes, Ch. 7 §7.2 · the rest written here.*

What does the general construction of §CB.13 give in three dimensions, where everything is already known? The Pauli matrices realize the Clifford algebra of Euclidean $\mathbb R^3$, its even part is the quaternions, $\mathrm{Spin}(3)$ is the group of unit quaternions $= SU(2)$, and $\rho$ is the familiar double cover $SU(2) \to SO(3)$ that 591 proves by quaternion conjugation. The Pauli module $\mathbb C^2$ restricted to $\mathrm{Spin}(3)$ is spin ½, the representation that SO(3) lacks; and every half-integer spin sits inside spin ½ ⊗ (a representation of SO(3)) — the TA's theorem in its first case, before the Lorentz case of [[§CB.15 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.15]]–[[§CB.17 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.17]]. It builds on [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.9]] and [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.13]].

## The Clifford algebra of ℝ³

> [!theorem] Theorem §CB.14.1: The Pauli Matrices Realize Cl(3, 0)
> The Pauli matrices satisfy $\sigma^i\sigma^j + \sigma^j\sigma^i = 2\delta^{ij}\mathbb 1$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]), so $e_i \mapsto \sigma^i$ extends to an algebra homomorphism $\mathrm{Cl}(3,0) \to M_2(\mathbb C)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-7|Theorem §CB.10.7]]); it is an isomorphism of real algebras $\mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, and sends the volume element $\omega = e_1e_2e_3$ to $\sigma^1\sigma^2\sigma^3 = i\mathbb 1$. The two irreducible complex Clifford modules ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-7|Theorem §CB.12.7]], 2) are $\mathbb C^2$ with $e_i \mapsto \sigma^i$ and with $e_i \mapsto -\sigma^i$.
>
> *Source: Woit, §28.2 · written here*

^thm-cb-14-1

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §28.2 ($\mathrm{Cliff}(3, 0, \mathbb R) = M(2, \mathbb C)$ via $\gamma_j \leftrightarrow \sigma_j$, with $\gamma_1\gamma_2\gamma_3 \leftrightarrow i\mathbb 1$) · the module statements written here from Theorem §CB.12.7.*
>
> **Step 1** (the isomorphism). This is the $\mathrm{Cl}(3,0)$ row of the proof of [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-11|Theorem §CB.11.11]]: the $\sigma^i$ satisfy $\sigma^i\sigma^j + \sigma^j\sigma^i = 2\delta^{ij}\mathbb 1$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 1), so $e_i \mapsto \sigma^i$ extends to a real algebra homomorphism $\pi : \mathrm{Cl}(3,0) \to M_2(\mathbb C)$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-7|Theorem §CB.10.7]]); its image contains $\mathbb 1$, $\sigma^k$, $\sigma^i\sigma^j = i\varepsilon^{ijk}\sigma^k$ ($i \ne j$) and $\sigma^1\sigma^2\sigma^3 = (i\sigma^3)\sigma^3 = i\mathbb 1$, hence the real basis $\mathbb 1, \sigma^k, i\mathbb 1, i\sigma^k$ of $M_2(\mathbb C)$; both sides have real dimension $8$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-6|Theorem §CB.11.6]]). The same computation gives $\pi(\omega) = \pi(e_1e_2e_3) = i\mathbb 1$.
>
> **Step 2** (two modules). $\pi$ composed with $M_2(\mathbb C) = \operatorname{End}_{\mathbb C}(\mathbb C^2)$ is a complex Clifford module on $\mathbb C^2$ ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-9|Def. §CB.10.9]]). So is $\pi^-$, $e_i \mapsto -\sigma^i$, since $(-\sigma^i)$ satisfy the same relations ([[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-10|Theorem §CB.10.10]]). Both are irreducible: their images are all of $M_2(\mathbb C)$ (for $\pi^-$ the image contains $\pm$ the same products), and only $0$ and $\mathbb C^2$ are invariant under all $2\times2$ matrices.
>
> **Step 3** (they are the two classes). With $n = 3$, $s = 0$, $\omega_{\mathbb C} = i^3e_1e_2e_3 = -i\omega$ ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-4|Def. §CB.12.4]]). Then $\pi(\omega_{\mathbb C}) = -i\cdot i\mathbb 1 = \mathbb 1$, while $\pi^-(\omega_{\mathbb C}) = -i(-\sigma^1)(-\sigma^2)(-\sigma^3) = -i(-i\mathbb 1) = -\mathbb 1$. By [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-7|Theorem §CB.12.7]], 2, the irreducible modules are classified by this sign, so $\pi$ and $\pi^-$ represent the two classes.
>
> **What the proof shows.**
> - Over $\mathbb R$, $\mathrm{Cl}(3,0)$ is already all of $M_2(\mathbb C)$: the "$i$" of the Pauli algebra is the volume element $e_1e_2e_3$, which is central and squares to $-1$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-9|Theorem §CB.11.9]]).

^pf-cb-14-1

*Uses:* [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-7|Theorem §CB.10.7]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-10-9|Def. §CB.10.9]], [[§CB.10 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-10-10|Theorem §CB.10.10]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-6|Theorem §CB.11.6]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-11|Theorem §CB.11.11]], [[§CB.12 Complex Clifford Algebras and Clifford Modules#^def-cb-12-4|Def. §CB.12.4]], [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-7|Theorem §CB.12.7]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!theorem] Theorem §CB.14.2: The Even Part Is the Quaternions
> The linear map $\mathrm{Cl}^0(3,0) \to \mathbb H$ with $1 \mapsto 1$, $e_3e_2 \mapsto i$, $e_1e_3 \mapsto j$, $e_2e_1 \mapsto k$ is an isomorphism of real algebras ([[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]; [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-11|Theorem §CB.11.11]]). Under Theorem §CB.14.1, $\mathrm{Cl}^0(3,0)$ is $\{a\mathbb 1 - i\,\mathbf b\cdot\boldsymbol\sigma : a \in \mathbb R, \mathbf b \in \mathbb R^3\}$, with $e_3e_2 \mapsto -i\sigma^1$, $e_1e_3 \mapsto -i\sigma^2$, $e_2e_1 \mapsto -i\sigma^3$.
>
> *Source: written here · Woit, §28.2 ($\mathrm{Cl}(0,2) \cong \mathbb H$), §29.2.1 · 591 §41*

^thm-cb-14-2

> [!proof]- Proof
> *Source: written here; the identification of $\mathrm{Cl}^0(3,0)$ with the quaternions is Woit, §29.2.1 ("generalizes … the one we gave in chapter 6 of $\mathrm{Spin}(3)$ in terms of unit length elements of the quaternion algebra"), and $\mathrm{Cl}(0,2) \cong \mathbb H$ with $\gamma_1 \leftrightarrow i$, $\gamma_2 \leftrightarrow j$ is Woit, §28.2.*
>
> **Step 1** (bijection). $\mathrm{Cl}^0(3,0)$ has the basis $1, e_1e_2, e_1e_3, e_2e_3$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-6|Theorem §CB.11.6]], Step 8), and $e_3e_2 = -e_2e_3$, $e_2e_1 = -e_1e_2$. So the linear map $\psi$ with $1 \mapsto 1$, $e_3e_2 \mapsto i$, $e_1e_3 \mapsto j$, $e_2e_1 \mapsto k$ sends a basis to a basis of $\mathbb H$ ([[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]]): it is a linear bijection.
>
> **Step 2** (products). Using $e_ae_b = -e_be_a$ ($a \ne b$) and $e_a^2 = 1$:
>
> $$
> (e_3e_2)^2 = -e_3e_3e_2e_2 = -1, \qquad (e_3e_2)(e_1e_3) = e_3e_2e_1e_3 = e_3e_3e_2e_1 = e_2e_1,
> $$
>
> (in the second, the last $e_3$ moves left past $e_1$ and $e_2$: two sign changes). In the same way $(e_1e_3)^2 = (e_2e_1)^2 = -1$, $(e_1e_3)(e_2e_1) = e_1e_1e_3e_2 = e_3e_2$, $(e_2e_1)(e_3e_2) = e_2e_2e_1e_3 = e_1e_3$, and reversing the order of two distinct bivectors gives the negative (e.g. $(e_1e_3)(e_3e_2) = e_1e_2 = -e_2e_1$). These are the relations $i^2 = j^2 = k^2 = -1$, $ij = -ji = k$, $jk = -kj = i$, $ki = -ik = j$. Since $\psi$ is linear and respects all products of basis elements, and both products are bilinear, $\psi$ is an algebra isomorphism.
>
> **Step 3** (Pauli form). Under $\pi$ of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], $e_3e_2 \mapsto \sigma^3\sigma^2 = -i\sigma^1$, $e_1e_3 \mapsto \sigma^1\sigma^3 = -i\sigma^2$, $e_2e_1 \mapsto \sigma^2\sigma^1 = -i\sigma^3$ (QM Theorem §B6.1.4, 1), so $a + b_1i + b_2j + b_3k \mapsto a\mathbb 1 - i\,\mathbf b\cdot\boldsymbol\sigma$.
>
> **What the proof shows.**
> - The quaternion units are the three rotation planes of $\mathbb R^3$ (bivectors); the same algebra appears as $\mathrm{Cl}(0,2)$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-11|Theorem §CB.11.11]]), now realized inside $\mathrm{Cl}(3,0)$.

^pf-cb-14-2

*Uses:* [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-6|Theorem §CB.11.6]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-11|Theorem §CB.11.11]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], [[§41 The Unit Quaternions and SU(2)#^def-41-1|591 Def. §41.1]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

## Spin(3) = SU(2)

> [!theorem] Theorem §CB.14.3: Spin(3) Is SU(2), and ρ Is the Double Cover SU(2) → SO(3)
> Under Theorem §CB.14.1, $\mathrm{Spin}(3)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-6|Def. §CB.13.6]]) is the group of unit quaternions ([[§41 The Unit Quaternions and SU(2)#^prop-41-4|591 Prop. §41.4]]) and maps onto $SU(2)$; it is connected and simply connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]]). The covering $\rho : \mathrm{Spin}(3) \to SO(3)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-12|Theorem §CB.13.12]]), $\rho(x)v = xvx^{-1}$, is conjugation of pure quaternions by unit quaternions ([[§42 SU(2) → SO(3)꞉ The Double Cover#^prop-42-1|591 Prop. §42.1]]), i.e. the double cover of [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]] and [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; a unit quaternion $\cos\frac\theta2 + \sin\frac\theta2\,u$ gives a rotation through the angle $\theta$ (591 Prop. §41.1, 3), the half angle of spin ½.
>
> *Source: 591 §§41–42 · Woit, §29.2.1 · the dictionary written here*

^thm-cb-14-3

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §29.2.1 (the Clifford construction of $\mathrm{Spin}(n)$ "generalizes … the one we gave in chapter 6 of $\mathrm{Spin}(3)$ in terms of unit length elements of the quaternion algebra") · Differentiable Manifolds (591) §§41–42 (unit quaternions, $S^3 \cong SU(2)$, conjugation of pure quaternions, the double cover), whose results are used here and not re-proved. The dictionary between the two pictures (Steps 1–2) is written here.*
>
> Let $\psi : \mathrm{Cl}^0(3,0) \to \mathbb H$ be the isomorphism of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-2|Theorem §CB.14.2]], $\pi$ the Pauli map of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], and $\omega = e_1e_2e_3$.
>
> **Step 1** (reversal is quaternion conjugation; $\mathrm{Spin}(3)$ lies in the unit quaternions). The reversal $t$ ([[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-4|Theorem §CB.11.4]]) fixes $1$ and sends $e_3e_2 \mapsto e_2e_3 = -e_3e_2$, and likewise for $e_1e_3$, $e_2e_1$; so $\psi(t(x)) = \overline{\psi(x)}$ for $x \in \mathrm{Cl}^0(3,0)$. For $x \in \mathrm{Spin}(3)$, every unit vector has $q = +1$, so $N(x) = x\,t(x) = 1$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-9|Theorem §CB.13.9]]); hence $x^{-1} = t(x)$ and $\psi(x)\overline{\psi(x)} = \psi(x\,t(x)) = 1$, i.e. $|\psi(x)| = 1$ ([[§41 The Unit Quaternions and SU(2)#^prop-41-1|591 Prop. §41.1]]).
>
> **Step 2** ($\rho$ is conjugation of pure quaternions). Define $j : V = \mathbb R^3 \to \mathbb H_0$ by $j(v) = \psi(-\omega v)$ ($\omega v$ is even). Moving letters with $e_ae_b = -e_be_a$: $\omega e_1 = e_1e_2e_3e_1 = e_1e_1e_2e_3 = e_2e_3$, $\omega e_2 = -e_1e_2e_2e_3 = -e_1e_3$, $\omega e_3 = e_1e_2$; so $j(e_1) = \psi(e_3e_2) = i$, $j(e_2) = \psi(e_1e_3) = j$, $j(e_3) = \psi(e_2e_1) = k$: $j$ is the isometry $\mathbb R^3 \to \mathbb H_0$ of the standard bases. $\omega$ is central ($n = 3$ odd, [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-9|Theorem §CB.11.9]], 3), so for $x \in \mathrm{Spin}(3)$, using Step 1 and [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-7|Theorem §CB.13.7]], 2,
>
> $$
> j(\rho(x)v) = \psi\bigl(-\omega\,x v x^{-1}\bigr) = \psi\bigl(x(-\omega v)\,t(x)\bigr) = \psi(x)\,j(v)\,\overline{\psi(x)} = C_{\psi(x)}\bigl(j(v)\bigr),
> $$
>
> the conjugation of [[§42 SU(2) → SO(3)꞉ The Double Cover#^prop-42-1|591 Prop. §42.1]]: $j\,\rho(x)\,j^{-1} = C_{\psi(x)}$.
>
> **Step 3** ($\psi(\mathrm{Spin}(3)) = S^3$). Let $q \in S^3$. $C_q \in SO(3)$ (591 Prop. §42.1, 1), so $j^{-1}C_qj \in SO(V)$, and $SO(V) = \rho(\mathrm{Spin}(3))$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-11|Theorem §CB.13.11]]): there is $x \in \mathrm{Spin}(3)$ with $C_{\psi(x)} = C_q$, hence $\psi(x) = \pm q$ (591 Prop. §42.1, 2) and $q = \psi(\pm x)$ with $\pm x \in \mathrm{Spin}(3)$. With Step 1, $\psi$ restricts to a group isomorphism $\mathrm{Spin}(3) \to S^3$, the unit quaternions ([[§41 The Unit Quaternions and SU(2)#^prop-41-4|591 Prop. §41.4]]).
>
> **Step 4** ($\pi(\mathrm{Spin}(3)) = SU(2)$). By Theorem §CB.14.2, $\pi\psi^{-1}(x_0 + x_1i + x_2j + x_3k) = x_0\mathbb 1 - i(x_1\sigma^1 + x_2\sigma^2 + x_3\sigma^3) = \begin{pmatrix}x_0 - ix_3 & -x_2 - ix_1\\ x_2 - ix_1 & x_0 + ix_3\end{pmatrix}$, of the form $\begin{pmatrix}\alpha & \beta\\ -\bar\beta & \bar\alpha\end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = \sum_ax_a^2$. These matrices with $|\alpha|^2 + |\beta|^2 = 1$ are exactly $SU(2)$ (proof of [[§41 The Unit Quaternions and SU(2)#^prop-41-5|591 Prop. §41.5]], 2). So $\pi$ maps $\mathrm{Spin}(3)$ isomorphically onto $SU(2)$; as the restriction of an injective linear map it is a homeomorphism onto its image. $SU(2) \cong S^3$ is connected and simply connected ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]], 1).
>
> **Step 5** ($\rho$ is the double cover). By Step 2, $\rho$ is the covering $C : S^3 \to SO(3)$ of [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]] transported by $\psi$ and $j$. In Pauli form, $\pi(v) = \mathbf v\cdot\boldsymbol\sigma$ and $\pi$ is multiplicative, so $\pi(x)(\mathbf v\cdot\boldsymbol\sigma)\pi(x)^{-1} = \pi(xvx^{-1}) = (\rho(x)\mathbf v)\cdot\boldsymbol\sigma$: the conjugation $U(\mathbf v\cdot\boldsymbol\sigma)U^\dagger$ of [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]. The half angle: $q = \cos\frac\theta2 + \sin\frac\theta2\,u$ gives $C_q$ = rotation through $\theta$ about $u$ (591 Prop. §42.1, 3).
>
> **What the proof shows.**
> - The three descriptions of the double cover in the vault — even Clifford elements acting by $v \mapsto xvx^{-1}$, unit quaternions acting on $\mathbb H_0$ (591), $SU(2)$ acting on $\mathbf v\cdot\boldsymbol\sigma$ (QM) — are one map, related by $\psi$, $j$ and $\pi$.
> - ⚑ By-product: $j(v) = \psi(-\omega v)$ identifies vectors with bivectors (Hodge duality by the volume element); this is why in three dimensions a rotation generator can be labelled by an axis.

^pf-cb-14-3

*Uses:* [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-4|Theorem §CB.11.4]], [[§CB.11 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-11-9|Theorem §CB.11.9]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-7|Theorem §CB.13.7]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-9|Theorem §CB.13.9]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-11|Theorem §CB.13.11]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-2|Theorem §CB.14.2]], [[§41 The Unit Quaternions and SU(2)#^prop-41-1|591 Prop. §41.1]], [[§41 The Unit Quaternions and SU(2)#^prop-41-4|591 Prop. §41.4]], [[§41 The Unit Quaternions and SU(2)#^prop-41-5|591 Prop. §41.5]], [[§42 SU(2) → SO(3)꞉ The Double Cover#^prop-42-1|591 Prop. §42.1]], [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]

The double cover, proved in 591 by quaternion conjugation:

![[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4]]

> [!theorem] Theorem §CB.14.4: 𝔰𝔭𝔦𝔫(3) = 𝔰𝔲(2)
> Under Theorem §CB.14.1, $\mathfrak{spin}(3)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]]) is $\mathfrak{su}(2) = \operatorname{span}_{\mathbb R}\{-\frac i2\sigma^k\}$, with $\frac12e_ie_j \mapsto \frac i2\varepsilon_{ijk}\sigma^k$; and $\rho_\ast$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]]) is the isomorphism $\mathfrak{su}(2) \cong \mathfrak{so}(3)$, $-\frac i2\sigma^k \mapsto -iJ^k$, of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]].
>
> *Source: Woit, §29.2.2, eq. (29.5) · written here*

^thm-cb-14-4

> [!proof]- Proof
> *Source: P. Woit, Quantum Theory, Groups and Representations, §29.2.2 (the identification $\epsilon_{jk} \leftrightarrow -\frac12\gamma_j\gamma_k$ of $\mathfrak{so}(n)$ with quadratic Clifford elements, eq. (29.5)) · written here for $n = 3$ from Theorem §CB.13.14.*
>
> **Step 1** ($\pi(\mathfrak{spin}(3)) = \mathfrak{su}(2)$). $\mathfrak{spin}(3) = \operatorname{span}_{\mathbb R}\{e_1e_2, e_1e_3, e_2e_3\}$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]]). For $i \ne j$, $\pi(\frac12e_ie_j) = \frac12\sigma^i\sigma^j = \frac i2\varepsilon_{ijk}\sigma^k$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 1). So $\pi(\mathfrak{spin}(3)) = \operatorname{span}_{\mathbb R}\{-\frac i2\sigma^k\}$, the traceless anti-Hermitian matrices $\mathfrak{su}(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]]); this is also the Lie algebra of $\pi(\mathrm{Spin}(3)) = SU(2)$, consistent with [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]], 1, and [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-3|Theorem §CB.14.3]].
>
> **Step 2** ($\rho_\ast$ in the basis). Take $(i, j, k)$ cyclic, so $\varepsilon_{ijk} = 1$ and $\pi(\frac12e_je_i) = -\frac i2\sigma^k$. By Theorem §CB.13.14, 2 (with $B(e_a, e_b) = \delta_{ab}$), $\rho_\ast(\frac12e_je_i)$ sends $v \mapsto B(e_i, v)e_j - B(e_j, v)e_i$, i.e. $e_i \mapsto e_j$, $e_j \mapsto -e_i$, $e_k \mapsto 0$. Its matrix entries are
>
> $$
> \bigl(\rho_\ast(\tfrac12e_je_i)\bigr)_{lm} = \delta_{lj}\delta_{mi} - \delta_{li}\delta_{mj} .
> $$
>
> **Step 3** (comparison with $-iJ^k$). $(J^k)_{lm} = -i\varepsilon^{klm}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]]), so $(-iJ^k)_{lm} = -\varepsilon^{klm} = -\varepsilon_{lmk}$. For $(l, m) = (j, i)$: $-\varepsilon_{jik} = \varepsilon_{ijk} = 1$; for $(l, m) = (i, j)$: $-\varepsilon_{ijk} = -1$; all other entries vanish. This is the matrix of Step 2. Hence $\rho_\ast(\pi^{-1}(-\frac i2\sigma^k)) = -iJ^k$ for $k = 1, 2, 3$, which is the isomorphism $-i\tau^k \mapsto -iJ^k$ of Theorem §CB.1.16 ($\tau^k = \frac12\sigma^k$).
>
> **What the proof shows.**
> - For cyclic $(i, j, k)$, $\frac12\sigma^k = -i\,\pi(\frac12e_ie_j)$: the physicists' spin generators are $-i$ times the rotation-plane bivectors, and the factor $\frac12$ is the same half that makes $\mathrm{Spin}$ a double cover (Step 1 of the proof of [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-12|Theorem §CB.13.12]]).

^pf-cb-14-4

*Uses:* [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-13|Def. §CB.13.13]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-14|Theorem §CB.13.14]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-3|Theorem §CB.14.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-15|Theorem §CB.1.15]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

## Spin ½ as the spinor representation, and the TA's theorem in three dimensions

> [!theorem] Theorem §CB.14.5: The Spinor Representation of Spin(3) Is Spin ½
> The spinor representation of $\mathrm{Spin}(3)$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-18|Def. §CB.13.18]]) on the Pauli module $\mathbb C^2$ is, under $\mathrm{Spin}(3) \cong SU(2)$, the defining representation $D^{(1/2)}$: irreducible, with $-1 \mapsto -\mathbb 1$, hence spinorial and not a representation of $SO(3)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], 2). Both irreducible Clifford modules give equivalent spinor representations ([[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-10|Theorem §CB.12.10]], 2).
>
> *Source: written here*

^thm-cb-14-5

> [!proof]- Proof
> *Source: written here from Theorems §CB.14.1, §CB.14.3 and §CB.12.10 (P. Woit, Quantum Theory, Groups and Representations, §29.2.1, points to his Ch. 6 for $\mathrm{Spin}(3)$ as the unit quaternions).*
>
> **Step 1** (the restriction is the defining representation). The spinor representation is $x \mapsto \pi(x)$ on $\mathbb C^2$ ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-18|Def. §CB.13.18]], with the irreducible module $\pi$ of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]]). The isomorphism $\mathrm{Spin}(3) \cong SU(2)$ of [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-3|Theorem §CB.14.3]] is $\pi$ itself, so, read on $SU(2)$, the representation is $U \mapsto U$: the defining representation. It is $D^{(1/2)}$: on the degree-one polynomials $P(z) = c^{\mathsf T}z$ of [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], 1, $(D(U)P)(z) = c^{\mathsf T}U^{\mathsf T}z = (Uc)^{\mathsf T}z$, i.e. $c \mapsto Uc$.
>
> **Step 2** (irreducible and spinorial). The real span of $SU(2) = \{a\mathbb 1 - i\,\mathbf b\cdot\boldsymbol\sigma : a^2 + |\mathbf b|^2 = 1\}$ contains $\mathbb 1$ and the $-i\sigma^k$, so its complex span is all of $M_2(\mathbb C)$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 4); a subspace invariant under $SU(2)$ is invariant under $M_2(\mathbb C)$, hence $0$ or $\mathbb C^2$. And $\pi(-1) = -\mathbb 1$, so the representation is spinorial ([[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-17|Def. §CB.13.17]]) and, by Theorem §CB.9.8, 2 (half-integer $j$), not a representation of $SO(3)$.
>
> **Step 3** (both modules). The other irreducible module $\pi^-$, $e_i \mapsto -\sigma^i$, agrees with $\pi$ on every product of an even number of vectors (the signs cancel), hence on $\mathrm{Cl}^0(3,0) \supset \mathrm{Spin}(3)$: the two spinor representations are not just equivalent but equal (Step 5 of the proof of [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-10|Theorem §CB.12.10]]).
>
> **What the proof shows.**
> - The Pauli module restricted to the even part is the spin-½ representation of QM; the parity-odd information ($e_i \mapsto \pm\sigma^i$) is invisible to rotations, which is why spin ½ comes in one kind while the Clifford module comes in two.

^pf-cb-14-5

*Uses:* [[§CB.12 Complex Clifford Algebras and Clifford Modules#^thm-cb-12-10|Theorem §CB.12.10]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-17|Def. §CB.13.17]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-13-18|Def. §CB.13.18]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-1|Theorem §CB.14.1]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-3|Theorem §CB.14.3]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]]

> [!theorem] Theorem §CB.14.6: The TA's Theorem in Three Dimensions
> Let $j \in \frac12 + \mathbb Z_{\ge0}$. Then $V_j$ is equivalent to a subrepresentation of $V_{1/2}\otimes V_{j - 1/2}$, where $V_{1/2}$ is the spinor representation (Theorem §CB.14.5) and $V_{j-1/2}$, of integer spin, is a representation of $SO(3)$ contained in $(\mathbb C^3)^{\otimes(j-1/2)}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]]). Hence every spinorial representation of $SU(2) = \mathrm{Spin}(3)$ is contained in $S\otimes T$ with $T$ tensorial: part 3 of [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]] for $n = 3$.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · proof written here from the Clebsch–Gordan series, [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]]*

^thm-cb-14-6

> [!proof]- Proof
> *Source: the statement is the PHY 513 TA's (oral remark, Oct 2026); proof written here from the Clebsch–Gordan series (Theorem §CB.9.10) and complete reducibility for $SU(2)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], 3).*
>
> **Step 1** ($V_j \subset V_{1/2}\otimes V_{j-1/2}$). Let $j \in \frac12 + \mathbb Z_{\ge0}$, so $l = j - \frac12$ is a nonnegative integer. By [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]] with $j_1 = \frac12$, $j_2 = l$,
>
> $$
> V_{1/2}\otimes V_l \cong \bigoplus_{J = |\frac12 - l|}^{l + \frac12}V_J = \begin{cases}V_j\oplus V_{j-1} & l \ge 1,\\ V_{1/2} & l = 0,\end{cases}
> $$
>
> since the range $|\frac12 - l| \le J \le l + \frac12$ in integer steps is $\{j - 1, j\}$ for $l \ge 1$ and $\{\frac12\}$ for $l = 0$. The equivalence maps the summand $V_j$ onto a subrepresentation of $V_{1/2}\otimes V_l$ equivalent to $V_j$.
>
> **Step 2** (the factors). $V_{1/2}$ is the spinor representation of $\mathrm{Spin}(3) = SU(2)$ ([[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-5|Theorem §CB.14.5]]). $V_l$ has $-\mathbb 1$ acting as $(-1)^{2l} = 1$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]]), so it is tensorial, a representation of $SO(3)$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-11|Theorem §CB.9.11]]), equivalent to the traceless symmetric tensors in $(\mathbb C^3)^{\otimes l}$ ([[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], 2), with $\mathbb C^3$ the complexified vector representation (Theorem §CB.9.12, 1).
>
> **Step 3** (a general spinorial representation). Let $W$ be a finite-dimensional representation of $SU(2)$ with $-\mathbb 1 \mapsto -\mathbb 1$. By Theorem §CB.9.8, 3, $W \cong V_{j_1}\oplus\cdots\oplus V_{j_r}$; on $V_{j_a}$, $-\mathbb 1$ acts as $(-1)^{2j_a}$ (Theorem §CB.9.8, 1), so every $j_a$ is a half-integer. By Step 1, $V_{j_a} \subset V_{1/2}\otimes T_a$ with $T_a = V_{j_a - 1/2}$, and since the tensor product distributes over direct sums,
>
> $$
> W \cong \bigoplus_aV_{j_a} \subset \bigoplus_a\bigl(V_{1/2}\otimes T_a\bigr) = V_{1/2}\otimes T, \qquad T = \bigoplus_aT_a \subset \bigoplus_a(\mathbb C^3)^{\otimes(j_a - 1/2)} .
> $$
>
> $T$ is tensorial (Step 2). This is part 3 of [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]] for $n = 3$, including the tensor-power refinement.
>
> **What the proof shows.**
> - A spin-$j$ field with half-integer $j$ is a spinor index on a symmetric traceless tensor of rank $j - \frac12$, with the lower spin $j - 1$ to be projected out — the pattern of Rarita–Schwinger ($j = \frac32$: $V_{1/2}\otimes V_1 = V_{3/2}\oplus V_{1/2}$).
> - Here $T$ is the minimal choice; the general construction $T = S'\otimes W$ of Theorem §CB.13.21 (Step 7 of its proof) would give $S'\otimes V_j \cong V_{1/2}\otimes V_j \cong V_{j+1/2}\oplus V_{j-1/2}$ ($V_{1/2}$ is self-dual, by $\varepsilon$), larger but also tensorial.

^pf-cb-14-6

*Uses:* [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-11|Theorem §CB.9.11]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.13 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-13-21|Theorem §CB.13.21]], [[§CB.14 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-14-5|Theorem §CB.14.5]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]]

> [!remark]- Connections
> - Three dimensions is where every step of §CB.13 can be checked by hand: 591 proves the surjectivity of $SU(2) \to SO(3)$ directly ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]]), without Cartan–Dieudonné; the proof of Theorem §CB.14.3 uses Cartan–Dieudonné (through Theorem §CB.13.11) only to see that every unit quaternion is a product of two unit vectors; and the spinor representation is the spin ½ of Quantum Mechanics ([[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]]: the sign of a $2\pi$ rotation).
> - The same pattern reappears for $\mathbb R^{1,3}$: Theorem §CB.11.10 turns $\mathrm{Cl}^0(1,3)$ into this section's $\mathrm{Cl}(3,0)$, so the Lorentz spin group is built from the Pauli matrices again (§CB.15).
> - **Used in**: Theorems §CB.14.1–§CB.14.4 — [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-7|Theorem §CB.9.7]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-1|§C5a.4, Remark: The rotation story, one level up]]; Theorem §CB.14.5 — [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-9-8|Theorem §CB.9.8]], [[§CB.18 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-18-7|Theorem §CB.18.7]]; Theorem §CB.14.6 — [[§CB.9 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^rem-cb-9-3|§CB.9, Remark: Spin j is 2j symmetrized spin-½ slots]], [[§C3.6★ Particle States and the Little Group#^thm-c3-6-8|Theorem §C3.6.8]].
