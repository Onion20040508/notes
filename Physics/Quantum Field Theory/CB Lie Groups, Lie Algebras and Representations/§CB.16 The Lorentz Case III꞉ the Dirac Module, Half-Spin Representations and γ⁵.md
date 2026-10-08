---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.16
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.17 Projective Representations, Wigner's Theorem and Antiunitary Symmetries]] →

*Sources: PHY 513 TA (oral remark, Oct 2026) · through the course homes embedded below: Peskin & Schroeder, §§3.2–3.4; the user's PHY 513 notes, Ch. 8 §§8.1–8.3, §8.9; PHY 513 Lectures 7–8; Yu Zhao-Huan, 量子场论讲义, §5.1 · P. Woit, Quantum Theory, Groups and Representations, §41.2 "Dirac γ matrices and Cliff(3,1)" (the strategy: quadratic Clifford elements give the Lorentz algebra, and the chiral blocks give $(\frac12, 0)$ and $(0, \frac12)$; Woit uses signature $(3,1)$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the Clifford-module computations and the comparison of conventions written here.*

What is the Dirac spinor as a representation of $\mathrm{Spin}(1,3)_0 = SL(2, \mathbb C)$, and where do $\gamma^5$, the Weyl halves, the bispinor form of a four-vector and the sixteen bilinears come from? This section specializes the TA's theorem ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-21|Theorem §CB.12.21]]) to Minkowski space: the Dirac module $\mathbb C^4$ restricts to $S^-\oplus S^+ = (\frac12, 0)\oplus(0, \frac12)$, split by $\gamma^5$, the image of the complex volume element (of the opposite orientation, Theorem §CB.16.1); Clifford multiplication exchanges the halves; the complexified vector is $S^+\otimes S^-$; two-forms are $(1,0)\oplus(0,1)$; the Clifford algebra itself is $\Lambda V$ as a representation, which is the classification of bilinears; and every spinorial representation sits in Dirac ⊗ tensor. It builds on [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.14]]–[[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.15]]; the course's statements are shown as embeds where they become instances.

Notation as in §CB.14: $V = \mathbb R^{1,3}$, standard basis $e_\mu$, the isomorphism $\phi$ and $\theta(\lambda) = (\lambda^\dagger)^{-1}$ of [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]]. The Dirac module is the course's Clifford multiplication ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]): $\gamma(a) = \slashed a = a_\mu\gamma^\mu$ on $S = \mathbb C^4$, so $\gamma(e_\mu) = \gamma_\mu = g_{\mu\nu}\gamma^\nu$. It is a Clifford module of $(V, q)$ since $\slashed a\,\slashed a = a_\mu a^\mu$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-5|Theorem §C5a.1.5]], 2), so it extends to an algebra homomorphism $\gamma : \mathrm{Cl}(1,3)_{\mathbb C} \to \operatorname{End}(S)$ ([[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-7|Theorem §CB.9.7]]). The chiral basis is [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]].

> [!caution] Caution: Two Dirac modules, and the sign of γ⁵
> Both $e_\mu \mapsto \gamma_\mu$ (used here) and $e_\mu \mapsto \gamma^\mu$ are Clifford modules of $\mathbb R^{1,3}$; the second is the first composed with the automorphism $\hat{\mathcal P}$ of $\mathrm{Cl}(1,3)$ extending parity $\mathcal P = \operatorname{diag}(1, -1, -1, -1)$ (Theorem §CB.9.7), since $\gamma^\mu = \gamma(\mathcal Pe_\mu)$. Only the first makes $\gamma(x)$ the course's spinor matrix of $\rho(x)$: $\gamma(x) = \Lambda_{1/2}(\omega)$ when $\rho(x) = e^\omega$ (Theorem §CB.16.2); with $e_\mu \mapsto \gamma^\mu$ the same $\gamma(x)$ belongs to $\mathcal P\rho(x)\mathcal P$, boosts reversed. They also differ on the volume element: $e_\mu \mapsto \gamma^\mu$ sends $\omega_{\mathbb C} = ie_0e_1e_2e_3$ to $\gamma^5$ (the reading of [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-9|Theorem §CB.10.9]] and [[§CB.11 Complex Clifford Algebras and Clifford Modules#^def-cb-11-4|Def. §CB.11.4]]), $e_\mu \mapsto \gamma_\mu$ sends it to $-\gamma^5$ (Theorem §CB.16.1). So for the module used here the half-spin spaces $\omega_{\mathbb C} = \pm1$ of [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-18|Def. §CB.12.18]] are the course's $\gamma^5 = \mp1$ spaces. This section keeps the course's labels: $S^\pm$ is $\gamma^5 = \pm1$, and $S^-$ is left-handed.
>
> *Source: written here, checked against [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]*

^cau-cb-16-1

## The Dirac module and its two halves

The Dirac maps, the Clifford module of the course, and $\gamma^5$, defined in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] and [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (shown in §CB.9 and §CB.10); the module is irreducible of dimension $4 = 2^{4/2}$ ([[§CB.11 Complex Clifford Algebras and Clifford Modules#^thm-cb-11-7|Theorem §CB.11.7]]).

> [!theorem] Theorem §CB.16.1: γ⁵ Is the Complex Volume Element (of the Opposite Orientation)
> In the Dirac module $\gamma(a) = \slashed a$, the complex volume element $\omega_{\mathbb C} = ie_0e_1e_2e_3$ ([[§CB.11 Complex Clifford Algebras and Clifford Modules#^def-cb-11-4|Def. §CB.11.4]]) goes to $\gamma(\omega_{\mathbb C}) = i\gamma_0\gamma_1\gamma_2\gamma_3 = -\gamma^5$, with $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]): $\gamma^5$ is the image of $-\omega_{\mathbb C}$, the complex volume element of the opposite orientation ([[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-9|Theorem §CB.10.9]], 1; [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-16-1|Caution: Two Dirac modules, and the sign of γ⁵]]). Hence $(\gamma^5)^2 = \mathbb 1$, $\gamma^5$ anticommutes with every $\gamma^\mu$ and commutes with $\gamma(\mathrm{Cl}^0)$, in particular with every $S^{\mu\nu}$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]; Theorem §CB.10.9, 3).
>
> *Source: written here · Peskin & Schroeder, §3.4 (the properties of $\gamma^5$), through [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]*

^thm-cb-16-1

> [!proof]- Proof
> **1. The phase.** In Def. §CB.11.4 take the orthonormal basis $(e_0, e_1, e_2, e_3)$: $n = 4$, one positive and $s = 3$ negative squares, so $i^{n(n-1)/2 + s} = i^{6 + 3} = i^9 = i$ and $\omega_{\mathbb C} = ie_0e_1e_2e_3$.
>
> **2. Its image.** $\gamma$ is an algebra homomorphism, so $\gamma(\omega_{\mathbb C}) = i\gamma_0\gamma_1\gamma_2\gamma_3$. With $\gamma_0 = \gamma^0$ and $\gamma_i = -\gamma^i$: $i\gamma_0\gamma_1\gamma_2\gamma_3 = i(-1)^3\gamma^0\gamma^1\gamma^2\gamma^3 = -\gamma^5$.
>
> **3. The opposite orientation.** $(e_1, e_0, e_2, e_3)$ is an orthonormal basis of the opposite orientation (one transposition), with the same signature, so its complex volume element is $ie_1e_0e_2e_3 = -ie_0e_1e_2e_3 = -\omega_{\mathbb C}$ (Theorem §CB.10.9, 1), and $\gamma(-\omega_{\mathbb C}) = \gamma^5$.
>
> **4. The square.** $\omega^2 = (-1)^{n(n-1)/2}(-1)^s = (-1)^6(-1)^3 = -1$ (Theorem §CB.10.9, 2), so $\omega_{\mathbb C}^2 = i^2\omega^2 = 1$ and $(\gamma^5)^2 = \gamma(\omega_{\mathbb C})^2 = \gamma(\omega_{\mathbb C}^2) = \mathbb 1$.
>
> **5. Anticommutation with the γ's.** $\omega v = (-1)^{n-1}v\omega = -v\omega$ for $v \in V$ (Theorem §CB.10.9, 3), so $\gamma^5\gamma_\mu = -\gamma_\mu\gamma^5$, and raising the index with $g^{\mu\nu}$, $\gamma^5\gamma^\mu = -\gamma^\mu\gamma^5$.
>
> **6. Commutation with the even part.** $\omega$ commutes with $\mathrm{Cl}^0$ (Theorem §CB.10.9, 3) — directly, $\gamma^5$ passes a product $\gamma_\mu\gamma_\nu$ with two sign changes. $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac i4g^{\mu\alpha}g^{\nu\beta}\gamma([e_\alpha, e_\beta])$ lies in $\gamma(\mathrm{Cl}^0_{\mathbb C})$, so $[\gamma^5, S^{\mu\nu}] = 0$, the course's [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], 1.
>
> **What the proof shows**
> - $\gamma^5$ is a volume element: its algebraic properties (square $1$, anticommuting with vectors, central in the even part) are those of $\omega_{\mathbb C}$ in even dimension, and nothing specific to the Dirac matrices was used.
> - ⚑ By-product (convention): which sign of the volume element is $\gamma^5$ depends on the orientation and on whether $e_\mu$ goes to $\gamma_\mu$ or $\gamma^\mu$ (Caution above); the course's $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is $+\omega_{\mathbb C}$ for $e_\mu \mapsto \gamma^\mu$ and $-\omega_{\mathbb C}$ for Clifford multiplication.

^pf-cb-16-1

*Uses:* [[§CB.11 Complex Clifford Algebras and Clifford Modules#^def-cb-11-4|Def. §CB.11.4]], [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-9|Theorem §CB.10.9]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]]

> [!theorem] Theorem §CB.16.2: The Dirac Module Restricted to SL(2,ℂ) Is (½, 0) ⊕ (0, ½)
> Restricted to $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]]), the Dirac module is $S = S^-\oplus S^+$, $S^\pm$ the $\pm1$ eigenspaces of $\gamma^5$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-1|Theorem §CB.16.1]]); $S^-$ and $S^+$ are invariant, irreducible, two-dimensional and inequivalent ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-21|Theorem §CB.12.21]], 1). If $x \in \mathrm{Spin}(1,3)_0$ and $\lambda = \theta(\phi(x))$ is the element with $\rho(x) = \pi(\lambda)$ (Theorem §CB.14.4, 2), then $x$ acts on $S^-$ by a matrix equivalent to $\lambda$ and on $S^+$ by one equivalent to $(\lambda^\dagger)^{-1}$: $S^- = (\frac12, 0)$ and $S^+ = (0, \frac12)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]]), as in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]] (left-handed spinors have $\gamma^5 = -1$). In particular $\gamma(x_\omega) = \Lambda_{1/2}(\omega)$ ([[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]) for $x_\omega = \exp(\frac14\omega^{\mu\nu}e_\mu e_\nu) \in \mathrm{Spin}(1,3)_0$, which covers $\rho(x_\omega) = e^\omega$.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · Peskin & Schroeder, §3.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]] · written here*

^thm-cb-16-2

> [!proof]- Proof
> **1. The spinor matrices are Clifford exponentials.** $\frac14\omega^{\alpha\beta}e_\alpha e_\beta = \sum_{\alpha<\beta}\omega^{\alpha\beta}\cdot\frac12e_\alpha e_\beta$ ($\omega$ antisymmetric) lies in $\mathfrak{spin}(1,3)$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-13|Def. §CB.12.13]]), so $x_\omega \in \mathrm{Spin}(1,3)_0$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-14|Theorem §CB.12.14]], 1; [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], 2). By [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-5|Theorem §CB.14.5]], $\rho_\ast(\frac12e_\alpha e_\beta) = M_{\alpha\beta}$, so $\rho(x_\omega) = \exp(\frac12\omega^{\alpha\beta}M_{\alpha\beta}) = \exp(\frac12\omega_{\alpha\beta}M^{\alpha\beta}) = e^\omega$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]]; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]]). On the spinor side, $\gamma(\frac14\omega^{\alpha\beta}e_\alpha e_\beta) = \frac14\omega^{\alpha\beta}\gamma_\alpha\gamma_\beta = \frac14\omega_{\alpha\beta}\gamma^\alpha\gamma^\beta$ (moving the metric from the $\gamma$'s to $\omega$), and
>
> $$
> -\tfrac i2\omega_{\alpha\beta}S^{\alpha\beta} = -\tfrac i2\cdot\tfrac i4\,\omega_{\alpha\beta}\bigl(\gamma^\alpha\gamma^\beta - \gamma^\beta\gamma^\alpha\bigr) = \tfrac18\bigl(\omega_{\alpha\beta}\gamma^\alpha\gamma^\beta + \omega_{\beta\alpha}\gamma^\beta\gamma^\alpha\bigr) = \tfrac14\omega_{\alpha\beta}\gamma^\alpha\gamma^\beta ,
> $$
>
> using $\omega_{\alpha\beta} = -\omega_{\beta\alpha}$ and relabelling. $\gamma$ is a continuous algebra homomorphism, so it maps the exponential series term by term: $\gamma(x_\omega) = \exp(-\frac i2\omega_{\alpha\beta}S^{\alpha\beta}) = \Lambda_{1/2}(\omega)$.
>
> **2. The halves are invariant.** $\gamma(\mathrm{Spin}(1,3)_0) \subset \gamma(\mathrm{Cl}^0)$ commutes with $\gamma^5$ (Theorem §CB.16.1). If $\gamma^5\psi = \pm\psi$, then $\gamma^5\gamma(x)\psi = \gamma(x)\gamma^5\psi = \pm\gamma(x)\psi$. Since $(\gamma^5)^2 = \mathbb 1$, $S = S^-\oplus S^+$ via $\psi = \frac12(\mathbb 1 - \gamma^5)\psi + \frac12(\mathbb 1 + \gamma^5)\psi$ ([[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]]).
>
> **3. The even generators in the chiral basis.** With $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^i = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$ (Def. §C5a.1.11), $\gamma_0 = \gamma^0$, $\gamma_i = -\gamma^i$:
>
> $$
> \gamma(f_i) = \gamma_i\gamma_0 = \begin{pmatrix}0 & -\sigma^i\\ \sigma^i & 0\end{pmatrix}\begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix} = \begin{pmatrix}-\sigma^i & 0\\ 0 & \sigma^i\end{pmatrix} ,
> $$
>
> and $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ (Theorem §C5a.5.2, 2): $S^-$ is the upper block ($\psi_L$), $S^+$ the lower ($\psi_R$).
>
> **4. The whole even part.** With $\tilde\kappa(A) = \sigma^2\bar A\sigma^2$, $\tilde\kappa(\sigma^i) = -\sigma^i$ (Theorem §CB.14.4, Proof, step 2), the maps $a \mapsto \gamma(a)$ and $a \mapsto \operatorname{diag}(\tilde\kappa(\phi(a)), \phi(a))$ are real-algebra homomorphisms $\mathrm{Cl}^0(1,3) \to M_4(\mathbb C)$ that agree on the generators $f_i$ (step 3; [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-3|Theorem §CB.14.3]]), hence everywhere.
>
> **5. The group.** For $x \in \mathrm{Spin}(1,3)_0$, $\det\phi(x) = 1$, so $\tilde\kappa(\phi(x)) = \theta(\phi(x)) = \lambda$ (Theorem §CB.14.4, Proof, step 3) and $\phi(x) = \theta(\lambda) = (\lambda^\dagger)^{-1}$ ($\theta^2 = \mathrm{id}$). So
>
> $$
> \gamma(x) = \begin{pmatrix}\lambda & 0\\ 0 & (\lambda^\dagger)^{-1}\end{pmatrix}, \qquad \rho(x) = \pi(\lambda),
> $$
>
> the course's form $\operatorname{diag}(\lambda, (\lambda^\dagger)^{-1})$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], 2; for $x = x_\omega$, $\lambda = \pm\Lambda_L(\omega)$, matching step 1.
>
> **6. Labels, irreducibility, inequivalence.** On $S^-$, $x$ acts by $\lambda$, i.e. by $D^{(\frac12, 0)}(\lambda)$ ($\operatorname{Sym}^1\mathbb C^2 = \mathbb C^2$), on $S^+$ by $(\lambda^\dagger)^{-1} = D^{(0, \frac12)}(\lambda)$. Through the isomorphism $\theta\circ\phi : \mathrm{Spin}(1,3)_0 \to SL(2, \mathbb C)$ (Theorem §CB.14.4) these are irreducible, of dimension $2$, and inequivalent (Theorem §CB.15.5; directly, [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]). $-1 \in \mathrm{Spin}(1,3)_0$ has $\lambda = -\mathbb 1$ and acts as $-\mathbb 1_4$: the module is spinorial.
>
> **7. Any other basis.** Dirac matrices in another basis are $U\gamma^\mu U^{-1}$ ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]]); then $\gamma$ and $\gamma^5$ are conjugated by $U$, which maps the eigenspaces of $\gamma^5$ onto those of $U\gamma^5U^{-1}$ and intertwines the actions. So steps 2–6 hold in every basis.
>
> **What the proof shows**
> - The course's pair $(\Lambda_L, \Lambda_R)$ is the action of the spin group through the Clifford algebra: $\Lambda_{1/2}(\omega)$ is literally $\gamma(\exp\frac14\omega^{\mu\nu}e_\mu e_\nu)$.
> - ⚑ By-product (convention): the left-handed half carries $\lambda = \theta(\phi(x))$, not $\phi(x)$; with the Clifford identification $\phi$ alone the labels $(\frac12, 0)$, $(0, \frac12)$ would be exchanged (Theorem §CB.15.5, Proof).
> - Used next: Clifford multiplication between the halves (Theorem §CB.16.4) and the vector as a bispinor (Theorem §CB.16.5).

^pf-cb-16-2

*Uses:* [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-13|Def. §CB.12.13]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-14|Theorem §CB.12.14]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-10|Theorem §CB.2.10]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-3|Theorem §CB.14.3]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-5|Theorem §CB.14.5]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-1|Theorem §CB.16.1]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-7|Theorem §C5a.1.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]

The course's two statements of this fact, proved in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] and [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]:

![[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4]]

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2]]

> [!theorem] Theorem §CB.16.3: The Two Halves Are Complex Conjugates of Each Other
> As representations of $SL(2, \mathbb C)$, $S^- \cong \overline{S^+}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-7|Def. §CB.6.7]]) and $S^\pm \cong (S^\pm)^\ast$ via $\varepsilon$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]); more generally $\overline{(j_+, j_-)} \cong (j_-, j_+)$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-8|Theorem §CB.6.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6, Ch. 8 §8.2 · the algebra form: [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-10|Theorem §CB.15.10]] · the group-level proof written here*

^thm-cb-16-3

> [!proof]- Proof
> By Theorem §CB.16.2, $S^-$ carries $\lambda$ and $S^+$ carries $\theta(\lambda) = (\lambda^\dagger)^{-1}$, $\lambda \in SL(2, \mathbb C)$. Let $\varepsilon = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$, a real matrix.
>
> **1. Two ε-identities.** By [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], 2, $(\lambda^{-1})^{\mathsf T} = \varepsilon\lambda\varepsilon^{-1}$; and $\theta(\lambda) = \varepsilon\bar\lambda\varepsilon^{-1}$ (Theorem §CB.14.4, Proof, step 3, with $\varepsilon\bar A\varepsilon^{-1} = \sigma^2\bar A\sigma^2$). Conjugating the second entrywise ($\varepsilon$ is real): $\overline{\theta(\lambda)} = \varepsilon\lambda\varepsilon^{-1}$.
>
> **2. The halves are conjugate.** The conjugate representation of $S^+$ has matrices $\overline{\theta(\lambda)}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-7|Def. §CB.6.7]]) $= \varepsilon\lambda\varepsilon^{-1}$ (step 1): $\varepsilon$ is an invertible intertwiner from $S^-$ to $\overline{S^+}$. So $S^- \cong \overline{S^+}$, and conjugating again $\overline{S^-} \cong S^+$.
>
> **3. Each half is self-dual.** The dual of $S^-$ has matrices $(\lambda^{-1})^{\mathsf T} = \varepsilon\lambda\varepsilon^{-1}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-6|Def. §CB.6.6]], step 1), so $(S^-)^\ast \cong S^-$ via $\varepsilon$. The dual of $S^+$ has matrices $(\theta(\lambda)^{-1})^{\mathsf T} = (\lambda^\dagger)^{\mathsf T} = \bar\lambda = \varepsilon^{-1}\theta(\lambda)\varepsilon$, so $(S^+)^\ast \cong S^+$ via $\varepsilon^{-1}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]).
>
> **4. General (j₊, j₋).** Entrywise conjugation commutes with tensor products and with restriction to $\operatorname{Sym}^k$ (a subspace defined by real equations), so $\overline{D^{(j_+, j_-)}(\lambda)} = \operatorname{Sym}^{2j_+}(\bar\lambda)\otimes\operatorname{Sym}^{2j_-}(\overline{\theta(\lambda)})$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]]). By step 1, $\bar\lambda = \varepsilon^{-1}\theta(\lambda)\varepsilon$ and $\overline{\theta(\lambda)} = \varepsilon\lambda\varepsilon^{-1}$; $\operatorname{Sym}^k$ of a conjugation is a conjugation by $\operatorname{Sym}^k(\varepsilon^{\mp1})$. Hence $\overline{D^{(j_+, j_-)}} \cong \operatorname{Sym}^{2j_+}(\theta(\lambda))\otimes\operatorname{Sym}^{2j_-}(\lambda)$, and the flip $u\otimes w \mapsto w\otimes u$ is an intertwiner onto $\operatorname{Sym}^{2j_-}(\lambda)\otimes\operatorname{Sym}^{2j_+}(\theta(\lambda)) = D^{(j_-, j_+)}(\lambda)$.
>
> **What the proof shows**
> - One invariant, $\varepsilon$, does all three jobs: it relates a half to its conjugate, to its dual, and (step 4) exchanges $j_+$ and $j_-$ under conjugation; at the algebra level this is [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-8|Theorem §CB.6.8]].
> - Used in the ★ Remark on Majorana spinors below: a conjugate-linear map can exchange $S^+$ and $S^-$.

^pf-cb-16-3

*Uses:* [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-6|Def. §CB.6.6]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-7|Def. §CB.6.7]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-2|Theorem §CB.16.2]]

## Clifford multiplication, vectors and two-forms

> [!theorem] Theorem §CB.16.4: Clifford Multiplication Exchanges the Halves Equivariantly
> The map $V\otimes S \to S$, $a\otimes\psi \mapsto \slashed a\psi$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]]), is an intertwiner of $SL(2, \mathbb C)$-representations ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-22|Theorem §CB.12.22]]) and maps $V\otimes S^\pm$ to $S^\mp$.
>
> *Source: written here · the course's form: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]]*

^thm-cb-16-4

> [!proof]- Proof
> **1. Equivariance.** For $x \in \mathrm{Spin}(1,3)$ and $a \in V$, $\rho(x)a = xax^{-1}$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-7|Theorem §CB.12.7]], 2), and $\gamma$ is an algebra homomorphism, so $\gamma(x)\,\slashed a\,\gamma(x)^{-1} = \gamma(xax^{-1}) = \slashed{(\rho(x)a)}$. Applied to $\gamma(x)\psi$: $\gamma(x)(\slashed a\psi) = \slashed{(\rho(x)a)}\,\gamma(x)\psi$, i.e. the map $a\otimes\psi \mapsto \slashed a\psi$ intertwines $\rho\otimes\gamma$ with $\gamma$ ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-3|Def. §CB.5.3]]); this is Theorem §CB.12.22 for $\mathbb R^{1,3}$, and extends complex-linearly to $V_{\mathbb C}\otimes S$. For $x = x_\omega$ (Theorem §CB.16.2) it reads $\Lambda_{1/2}(\slashed a\psi) = \slashed{(e^\omega a)}\Lambda_{1/2}\psi$, the course's [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]], 1.
>
> **2. The halves are exchanged.** $\gamma^5\slashed a = -\slashed a\gamma^5$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-1|Theorem §CB.16.1]]). If $\gamma^5\psi = \pm\psi$, then $\gamma^5\slashed a\psi = -\slashed a\gamma^5\psi = \mp\slashed a\psi$: $\slashed a$ maps $S^\pm$ to $S^\mp$.
>
> **What the proof shows**
> - Equivariance is automatic: the spin group acts on vectors by conjugation inside the same algebra in which $\slashed a$ multiplies spinors. The $\gamma$'s "do not transform" because they are this intertwiner.

^pf-cb-16-4

*Uses:* [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-7|Theorem §CB.12.7]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-3|Def. §CB.5.3]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-1|Theorem §CB.16.1]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-2|Theorem §CB.16.2]]

The course's statements, in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12]]

> [!theorem] Theorem §CB.16.5: The Complexified Vector Is S⁺ ⊗ S⁻
> The map $V_{\mathbb C} \to \operatorname{Hom}(S^+, S^-) \cong (S^+)^\ast\otimes S^- \cong S^+\otimes S^-$, $a \mapsto \slashed a|_{S^+}$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-4|Theorem §CB.16.4]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-9|Theorem §CB.6.9]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]]), is an equivalence of $SL(2, \mathbb C)$-representations: $V_{\mathbb C} \cong (\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$. In the chiral basis ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]) $\slashed a|_{S^+} : S^+ \to S^-$ has the matrix $a_\mu\sigma^\mu$, the course's $X$ for $a$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]), and $\slashed a|_{S^-} : S^- \to S^+$ has $a_\mu\bar\sigma^\mu$: $\sigma^\mu$ is an invariant tensor ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-10|Def. §CB.6.10]]) with one vector, one undotted and one dotted index.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 and Peskin & Schroeder, §3.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6|Theorem §C5a.5.6]] · written here*

^thm-cb-16-5

> [!proof]- Proof
> **1. An intertwiner.** By [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-4|Theorem §CB.16.4]], $\Phi(a) = \slashed a|_{S^+}$ lies in $\operatorname{Hom}(S^+, S^-)$, and $\Phi$ is complex-linear on $V_{\mathbb C}$. $\operatorname{Hom}(S^+, S^-)$ carries $x\cdot T = \gamma(x)|_{S^-}\,T\,(\gamma(x)|_{S^+})^{-1}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-9|Theorem §CB.6.9]]). Restricting $\gamma(x)\slashed a\gamma(x)^{-1} = \slashed{(\rho(x)a)}$ (Theorem §CB.16.4, Proof, step 1) to $S^+$, where $\gamma(x)$ preserves both halves: $x\cdot\Phi(a) = \Phi(\rho(x)a)$.
>
> **2. The matrix.** In the chiral basis $\slashed a = a_\mu\gamma^\mu = \begin{pmatrix}0 & a_\mu\sigma^\mu\\ a_\mu\bar\sigma^\mu & 0\end{pmatrix}$ (Def. §C5a.1.11). $S^+$ is the lower block (Theorem §CB.16.2, Proof, step 3), and $\slashed a\binom{0}{\psi_R} = \binom{a_\mu\sigma^\mu\psi_R}{0}$: the matrix of $\Phi(a)$ is $a_\mu\sigma^\mu$. Likewise $\slashed a\binom{\psi_L}{0} = \binom{0}{a_\mu\bar\sigma^\mu\psi_L}$.
>
> **3. Injective.** $\mathbb 1, \sigma^1, \sigma^2, \sigma^3$ are linearly independent over $\mathbb C$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 4), so $a_\mu\sigma^\mu = 0$ forces $a_\mu = 0$, also for complex $a$. (A null complex $a$ has $\slashed a\,\slashed a = 0$ but $\slashed a \ne 0$; injectivity comes from the two blocks, not from $\slashed a\,\slashed a = q(a)$.)
>
> **4. An equivalence.** $\dim V_{\mathbb C} = 4 = 2\cdot2 = \dim\operatorname{Hom}(S^+, S^-)$, so $\Phi$ is an invertible intertwiner. Further $\operatorname{Hom}(S^+, S^-) \cong (S^+)^\ast\otimes S^-$ (Theorem §CB.6.9) and $(S^+)^\ast \cong S^+$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-3|Theorem §CB.16.3]]), so $V_{\mathbb C} \cong S^+\otimes S^-$. In terms of $\lambda$ (Theorem §CB.16.2) this is $(\lambda^\dagger)^{-1}\otimes\lambda$, and the flip of the two factors is an intertwiner onto $\lambda\otimes(\lambda^\dagger)^{-1} = D^{(\frac12, \frac12)}(\lambda)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]]).
>
> **5. The invariant tensor.** $\Phi \in V_{\mathbb C}'\otimes\operatorname{Hom}(S^+, S^-)$ is fixed by the group (Theorem §CB.6.9, [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-10|Def. §CB.6.10]]), with $\Phi(e_\mu) = \sigma_\mu = g_{\mu\nu}\sigma^\nu$: the array $\sigma^\mu$ with one vector index, one index of $S^-$ (undotted) and one of $(S^+)^\ast$ (dotted, [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]). Check against the course: with $D_{S^-}(x) = \lambda$, $D_{S^+}(x) = (\lambda^\dagger)^{-1}$, step 1 reads $\lambda\,(a_\mu\sigma^\mu)\,\lambda^\dagger = (\rho(x)a)_\mu\sigma^\mu$, which for $\lambda = \Lambda_L(\omega)$, $\rho(x) = e^\omega$ is [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], 1.
>
> **What the proof shows**
> - ⚑ By-product (convention, resolving the choice left open before): with Clifford multiplication $\slashed a = a_\mu\gamma^\mu$ and the chiral basis, the map from right- to left-handed spinors is $a_\mu\sigma^\mu$ and the reverse map is $a_\mu\bar\sigma^\mu$. With the other Dirac module $e_\mu \mapsto \gamma^\mu$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-16-1|Caution: Two Dirac modules, and the sign of γ⁵]]) the first would be $a_\mu\bar\sigma^\mu$.
> - A four-vector is a bispinor: one undotted and one dotted index, as in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6|Theorem §C5a.5.6]].

^pf-cb-16-5

*Uses:* [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-2|Theorem §CB.16.2]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-3|Theorem §CB.16.3]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-4|Theorem §CB.16.4]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-9|Theorem §CB.6.9]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-10|Def. §CB.6.10]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-11|Def. §C5a.1.11]]

The course's bispinor, in [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]:

![[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6]]

The vector representation is $(\frac12, \frac12)$ also by direct computation with the course's $4\times4$ generators, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]] (physics: the same statement as Theorem §CB.16.5, read in the basis $v^0, \dots, v^3$).

> [!theorem] Theorem §CB.16.6: Two-Forms Are (1, 0) ⊕ (0, 1)
> $\Lambda^2V_{\mathbb C} \cong \Lambda^2(S^+\otimes S^-) \cong (\operatorname{Sym}^2S^+\otimes\Lambda^2S^-)\oplus(\Lambda^2S^+\otimes\operatorname{Sym}^2S^-) \cong \operatorname{Sym}^2S^+\oplus\operatorname{Sym}^2S^- = (1, 0)\oplus(0, 1)$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], 3; $\Lambda^2S^\pm$ trivial, [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]]). The two summands are the eigenspaces $\star = \pm i$ of duality ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]), exchanged by complex conjugation; on the real two-forms this is the second case of [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-16|Theorem §CB.3.16]].
>
> *Source: written here · the course's statements: [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]*

^thm-cb-16-6

> [!proof]- Proof
> All representations are of $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$, written through $\lambda$ (Theorem §CB.16.2): $S^-$ carries $\lambda$, $S^+$ carries $\theta(\lambda) = (\lambda^\dagger)^{-1}$, $V_{\mathbb C}$ carries $\rho(x)$.
>
> **1. Transport the equivalence.** If $T : A \to B$ is an equivalence, $T\otimes T$ restricted to $\Lambda^2A$ is an equivalence $\Lambda^2A \cong \Lambda^2B$. With [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]]: $\Lambda^2V_{\mathbb C} \cong \Lambda^2(S^+\otimes S^-)$.
>
> **2. Split the exterior square.** [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], 3, for $G_1 = G_2 = SL(2, \mathbb C)$ acting on $A = S^+$ and $B = S^-$, restricted to the diagonal $\lambda \mapsto (\lambda, \lambda)$ (an equivalence of $G_1\times G_2$-representations stays one on any subgroup): $\Lambda^2(S^+\otimes S^-) \cong (\operatorname{Sym}^2S^+\otimes\Lambda^2S^-)\oplus(\Lambda^2S^+\otimes\operatorname{Sym}^2S^-)$.
>
> **3. The two-dimensional exterior squares are trivial.** $\Lambda^2\mathbb C^2$ is the representation $A \mapsto \det A$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], 1), and $\det\lambda = \det(\lambda^\dagger)^{-1} = 1$. So $\Lambda^2V_{\mathbb C} \cong \operatorname{Sym}^2S^+\oplus\operatorname{Sym}^2S^-$, i.e. $D^{(0,1)}\oplus D^{(1,0)}$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]]), irreducible and inequivalent. Call the two summands $W_1 \cong (1, 0)$ and $W_2 \cong (0, 1)$ inside $\Lambda^2V_{\mathbb C}$.
>
> **4. The invariant subspaces of W₁ ⊕ W₂.** Let $E \subset W_1\oplus W_2$ be invariant, $p_k$ the projections onto $W_k$ (intertwiners). $E\cap W_k$ is invariant in the irreducible $W_k$, so it is $0$ or $W_k$. If $E \supset W_1$, then for $e = w_1 + w_2 \in E$ also $w_2 \in E$, so $E = W_1\oplus(E\cap W_2)$, i.e. $E = W_1$ or $E = W_1\oplus W_2$; likewise if $E \supset W_2$. If $E\cap W_1 = E\cap W_2 = 0$ and $E \ne 0$, take an irreducible invariant $E' \subset E$ (complete reducibility, [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]]): $p_1|_{E'}$ has kernel $E'\cap W_2 = 0$ and its image is a nonzero invariant subspace of $W_1$, hence $E' \cong W_1$; in the same way $E' \cong W_2$, contradicting $W_1 \not\cong W_2$. So the invariant subspaces are $0$, $W_1$, $W_2$, $W_1\oplus W_2$.
>
> **5. Duality picks the two summands.** By [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], 3, $\Lambda^2V_{\mathbb C}$ is the direct sum of the three-dimensional eigenspaces $E_\pm$ of $\star$ (eigenvalues $\pm i$), each invariant under every $\Lambda$ with $\det\Lambda = 1$, so under $\rho(\mathrm{Spin}(1,3)_0) = SO^+(1,3)$. By step 4 a three-dimensional invariant subspace is $W_1$ or $W_2$, and $E_+ \ne E_-$: $\{E_+, E_-\} = \{W_1, W_2\}$.
>
> **6. Conjugation exchanges them.** Let $c$ be complex conjugation of the components of $\Lambda^2V_{\mathbb C}$. $\star$ has real coefficients, so $\star c = c\star$; if $\star A = iA$ then $\star(cA) = c(iA) = -i\,cA$. So $c(E_\pm) = E_\mp$.
>
> **7. The real two-forms.** The $c$-stable invariant subspaces are $0$ and $W_1\oplus W_2$ (steps 4, 6: $c(W_1) = W_2$). By [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-16|Theorem §CB.3.16]], 1, the real representation $\Lambda^2V$ has no invariant subspaces but $0$ and itself: it is irreducible, and its complexification is $W\oplus c(W)$ with $W$ irreducible, the second case of Theorem §CB.3.16, 2.
>
> **What the proof shows**
> - A real two-form is irreducible, yet over $\mathbb C$ it splits into self-dual and anti-self-dual parts, the field strengths of the two helicities: $\mathbf E \pm i\mathbf B$ in electrodynamics.
> - Which of $(1, 0)$, $(0, 1)$ is $\star = +i$ depends on the sign of $\varepsilon^{0123}$ and on the labelling of the halves; the theorem does not need it.

^pf-cb-16-6

*Uses:* [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-16|Theorem §CB.3.16]]

The two-index tensors as a whole, the course's decomposition (the user's PHY 513 notes, Ch. 7 §7.4.5):

> [!theorem] Theorem §CB.16.7: Two-Index Tensors Are (0, 0) ⊕ (1, 0) ⊕ (0, 1) ⊕ (1, 1)
> The representation $\Lambda\otimes\Lambda$ of $SO^+(1,3)$ on two-index tensors $T^{\mu\nu}$, with generators $\mathcal J^{\mu\nu}\otimes\mathbb 1 + \mathbb 1\otimes\mathcal J^{\mu\nu}$, has over $\mathbb C$ the invariant pieces ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]])
>
> $$
> \underbrace{\tfrac14g^{\mu\nu}T^\rho{}_\rho}_{(0,\,0)}\ \oplus\ \underbrace{T^{[\mu\nu]}}_{(1,\,0)\oplus(0,\,1)}\ \oplus\ \underbrace{T^{(\mu\nu)} - \tfrac14g^{\mu\nu}T^\rho{}_\rho}_{(1,\,1)} ,
> $$
>
> the two halves of the antisymmetric part being the eigenspaces $\star A = \pm iA$ of duality ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]). Over $\mathbb R$, the six-dimensional real antisymmetric tensors are irreducible.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.5 (Derivation "Products: two-index tensors are (1,1)⊕(1,0)⊕(0,1)⊕(0,0)"; checked numerically there: "This proves the irreducibility that Section [tensors] could only quote") · the matching argument and the real case written out here*

^thm-cb-16-7

> [!derivation]- Derivation
> **1. Its decomposition.** With $\Lambda \cong (\frac12, \frac12)$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]]: $V_{\mathbb C} \cong S^+\otimes S^-$; in the course's matrices, Theorem §C3.2.2), Theorem §CB.15.8 gives $(1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, each once, of dimensions $9, 3, 3, 1$.
>
> **2. Four invariant subspaces.** By Theorem §C1a.5.6 the trace part (dimension $1$), the antisymmetric part ($6$) and the symmetric traceless part ($9$) are each mapped into themselves by every $\Lambda$; by Theorem §C1a.5.7, 3, the antisymmetric part is, over $\mathbb C$, the sum of two invariant three-dimensional eigenspaces of $\star$. So $\mathbb C^{16} = W_1\oplus W_3\oplus W_3'\oplus W_9$ with invariant $W_d$ of dimension $d$.
>
> **3. Match by dimension.** Each $W_d$ is a representation, hence a sum of pieces $(j_+, j_-)$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]]); joining these decompositions decomposes $\mathbb C^{16}$, and multiplicities are unique (Theorem §CB.15.4, step 9), so the pieces of the four $W_d$ together are exactly $(1, 1)$, $(1, 0)$, $(0, 1)$, $(0, 0)$, once each. The only piece of dimension $1$ is $(0, 0)$, so $W_1 = (0, 0)$. A three-dimensional $W_3$ must be made of pieces from $\{9, 3, 3\}$ with dimensions summing to $3$: a single $(1, 0)$ or $(0, 1)$, and $W_3$, $W_3'$ take one each. What remains, $W_9$, is $(1, 1)$.
>
> **4. Real irreducibility.** Let $U$ be a real subspace of the real antisymmetric tensors, invariant under every $\Lambda$. Its complexification $U_{\mathbb C} = U + iU$ is an invariant subspace of $(1, 0)\oplus(0, 1)$ and is closed under complex conjugation. The invariant subspaces of a sum of two inequivalent irreducible representations are $0$, either summand, or the whole (an invariant subspace is a sum of pieces, and with multiplicity one each piece is a fixed subspace). Complex conjugation maps the $(+i)$-eigenspace of the real map $\star$ to the $(-i)$-eigenspace (Theorem §C1a.5.7, 3), so neither summand alone is closed under it. Hence $U_{\mathbb C} = 0$ or everything, i.e. $U = 0$ or all six dimensions.
>
> **What the derivation shows**
> - The decomposition of Theorem §C1a.5.6 is the finest possible over $\mathbb R$; over $\mathbb C$ only the antisymmetric part splits further, and only by complex combinations (the duality eigenvalues are $\pm i$ because $\star^2 = -1$).
> - The field law of a two-index tensor field, and the reading of its pieces (spin content, which half is $(1, 0)$), is [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]] (physics).

^der-cb-16-7

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-4|Theorem §CB.15.4]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-8|Theorem §CB.15.8]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]

## The Clifford algebra as a representation, and the bilinears

> [!theorem] Theorem §CB.16.8: Cl(1,3) ≅ ΛV as a Representation; the Sixteen Bilinears
> 1. $\mathrm{Spin}(1,3)_0$ acts on $\mathrm{Cl}(1,3)$ by $a \mapsto xax^{-1}$; the vector-space isomorphism $\Lambda V \cong \mathrm{Cl}(1,3)$ of [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-7|Theorem §CB.10.7]] intertwines it with $\Lambda\rho$, so $\mathrm{Cl}(1,3)_{\mathbb C} \cong \Lambda^0\oplus\Lambda^1\oplus\Lambda^2\oplus\Lambda^3\oplus\Lambda^4$ of dimensions $1 + 4 + 6 + 4 + 1$.
> 2. $\operatorname{End}(S) \cong \mathrm{Cl}(1,3)_{\mathbb C}$ ([[§CB.11 Complex Clifford Algebras and Clifford Modules#^thm-cb-11-5|Theorem §CB.11.5]]) as representations, with $\operatorname{End}(S) \cong S\otimes S^\ast$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-9|Theorem §CB.6.9]]); through the Dirac form $S^\ast \cong \bar S$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-16|Theorem §CB.12.16]]), so $\bar\psi\Gamma\chi$ with $\Gamma$ in the $\Lambda^k$ piece transforms as a $k$-form: scalar, vector, tensor, axial vector, pseudoscalar ($\Lambda^3 \cong \Lambda^1$ and $\Lambda^4 \cong \Lambda^0$ through $\gamma^5$, up to orientation).
>
> *Source: Peskin & Schroeder, §3.4, and the user's PHY 513 notes, Ch. 8 §8.9, through [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]] and [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]] · the representation-theoretic proof written here*

^thm-cb-16-8

> [!proof]- Proof
> **1. Conjugation is the induced automorphism.** For $x \in \mathrm{Spin}(1,3)_0$, $a \mapsto xax^{-1}$ is an algebra automorphism of $\mathrm{Cl}(1,3)$ that maps $v \in V$ to $\rho(x)v \in V$ ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-7|Theorem §CB.12.7]], 2). By the uniqueness in [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-7|Theorem §CB.9.7]], it is the automorphism extending $v \mapsto \rho(x)v$.
>
> **2. Part 1.** The isomorphism $Q : \Lambda V \to \mathrm{Cl}(1,3)$ of [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-7|Theorem §CB.10.7]] commutes with the action of $O(V, q)$, on $\mathrm{Cl}$ by exactly these automorphisms. With $R = \rho(x)$ and step 1: $Q\bigl((\Lambda\rho(x))w\bigr) = x\,Q(w)\,x^{-1}$. $Q(\Lambda^kV)$ is the span of the $e_I$ with $|I| = k$, an invariant subspace of dimension $\binom4k$: $1, 4, 6, 4, 1$. Extending complex-linearly gives the statement for $\mathrm{Cl}(1,3)_{\mathbb C}$.
>
> **3. γ identifies the Clifford algebra with End(S).** $\gamma : \mathrm{Cl}(1,3)_{\mathbb C} \to \operatorname{End}(S)$ is an algebra homomorphism whose image contains $\mathbb 1$, $\gamma^\mu = g^{\mu\nu}\gamma(e_\nu)$ and their products, hence the sixteen matrices of [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], which span all $4\times4$ matrices ([[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]]). Both spaces have dimension $16$ ([[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-6|Theorem §CB.10.6]]), so $\gamma$ is bijective, as [[§CB.11 Complex Clifford Algebras and Clifford Modules#^thm-cb-11-5|Theorem §CB.11.5]] predicts. It is equivariant: $\gamma(xax^{-1}) = \gamma(x)\gamma(a)\gamma(x)^{-1}$, which is the action $T \mapsto \gamma(x)T\gamma(x)^{-1}$ on $\operatorname{End}(S) = \operatorname{Hom}(S, S) \cong S\otimes S^\ast$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-9|Theorem §CB.6.9]]).
>
> **4. The Dirac form.** Let $h_D(\psi, \chi) = \psi^\dagger\gamma^0\chi = \bar\psi\chi$ ([[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]). Every $\gamma^\mu$, hence every $\gamma(v) = v_\mu\gamma^\mu$ with real $v_\mu$, is self-adjoint for $h_D$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], 1). By [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-16|Theorem §CB.12.16]], $h_D(\gamma(x)\psi, \gamma(x)\chi) = h_D(\psi, \chi)$ for $x \in \mathrm{Spin}(1,3)_0$ (the course's [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]). Equivalently $\overline{\gamma(x)\psi} = \bar\psi\,\gamma(x)^{-1}$: the conjugate-linear bijection $\psi \mapsto \bar\psi = h_D(\psi, \cdot)$ intertwines $S$ with $S^\ast$, i.e. it is a complex-linear equivalence $\bar S \cong S^\ast$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-6|Def. §CB.6.6]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-7|Def. §CB.6.7]]).
>
> **5. Bilinears transform as forms.** For $a \in \mathrm{Cl}(1,3)_{\mathbb C}$ put $B_a(\psi, \chi) = \bar\psi\,\gamma(a)\,\chi$. By step 4 and step 3,
>
> $$
> B_a(\gamma(x)\psi, \gamma(x)\chi) = h_D\bigl(\psi, \gamma(x)^{-1}\gamma(a)\gamma(x)\chi\bigr) = B_{x^{-1}ax}(\psi, \chi) .
> $$
>
> So for fixed $\psi$, $\chi$ the linear functional $a \mapsto B_a(\psi, \chi)$ on $Q(\Lambda^kV_{\mathbb C})$ is transformed by precomposition with the action of $x^{-1}$, which is $\Lambda^k\rho(x)^{-1}$ by step 2: it is an element of $(\Lambda^kV_{\mathbb C})'$ with the dual representation (Def. §CB.6.6), a $k$-form. On basis elements, $B_{e_{\mu_1}\cdots e_{\mu_k}} = \bar\psi\gamma_{\mu_1}\cdots\gamma_{\mu_k}\chi$ for distinct $\mu_i$; for $k = 0, 1, 2$ these are $\bar\psi\chi$, $\bar\psi\gamma_\mu\chi$, $\bar\psi\gamma_\mu\gamma_\nu\chi = -i\bar\psi\sigma_{\mu\nu}\chi$ ($\mu \ne \nu$, since $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] = i\gamma^\mu\gamma^\nu$ there): scalar, vector, antisymmetric tensor, as in [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]].
>
> **6. Grades 3 and 4 through the volume element.** For $x \in \mathrm{Spin}(1,3)_0 \subset \mathrm{Cl}^0$, $x\omega x^{-1} = \omega$ ([[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-9|Theorem §CB.10.9]], 3), so right multiplication $R_\omega(a) = a\omega$ commutes with the action: $x(a\omega)x^{-1} = (xax^{-1})\omega$. It maps $e_I$ to $\pm e_{I^c}$ (each factor of $e_I$ meets its copy in $\omega$ after reordering and squares to $\pm1$; e.g. $e_0\omega = e_1e_2e_3$), so $Q(\Lambda^k) \to Q(\Lambda^{4-k})$, and it is invertible ($\omega^2 = -1$). Hence $\Lambda^3 \cong \Lambda^1$ and $\Lambda^4 \cong \Lambda^0$ as representations of $\mathrm{Spin}(1,3)_0$. Since $\omega = -i\omega_{\mathbb C}$ and $\gamma(\omega_{\mathbb C}) = -\gamma^5$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-1|Theorem §CB.16.1]]), $\gamma(\omega) = i\gamma^5$: the grade-3 and grade-4 bilinears are spanned by $\bar\psi\gamma_\mu\gamma^5\chi$ and $\bar\psi\,i\gamma^5\chi$, transforming as a vector and a scalar under $\mathrm{Spin}(1,3)_0$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]).
>
> **What the proof shows**
> - The classification of the sixteen bilinears is the grading of the Clifford algebra, $\mathrm{Cl} \cong \Lambda^0\oplus\dots\oplus\Lambda^4$, transported to $\operatorname{End}(S)$ by $\gamma$ and paired by the invariant Dirac form.
> - ⚑ By-product ("up to orientation"): $R_\omega$ commutes with $\mathrm{Spin}(1,3)_0$ but not with orientation-reversing elements, which send $\omega$ to $-\omega$ (Theorem §CB.10.9, 1). This sign is the "pseudo" in pseudoscalar and axial vector: they differ from $\bar\psi\psi$ and $\bar\psi\gamma^\mu\psi$ under parity ([[§C9.4 Fermion Bilinears under Parity|§C9.4]]).

^pf-cb-16-8

*Uses:* [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-7|Theorem §CB.12.7]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-16|Theorem §CB.12.16]], [[§CB.9 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-6|Theorem §CB.10.6]], [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-7|Theorem §CB.10.7]], [[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-10-9|Theorem §CB.10.9]], [[§CB.11 Complex Clifford Algebras and Clifford Modules#^thm-cb-11-5|Theorem §CB.11.5]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-6|Def. §CB.6.6]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-6-7|Def. §CB.6.7]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-9|Theorem §CB.6.9]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-1|Theorem §CB.16.1]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-6|Theorem §C5a.1.6]], [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]

The course's bilinears, in [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]]; the invariance of the Dirac form, an instance of [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-16|Theorem §CB.12.16]]:

![[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1]]

![[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3]]

## The TA's theorem for the Lorentz group

> [!theorem] Theorem §CB.16.9: Every Tensorial (j₊, j₋) Lies in a Tensor Power of the Vector
> If $k + l \in \mathbb Z$, then $(k, l)$ is equivalent to a subrepresentation of $V_{\mathbb C}^{\otimes N}$ with $N = 2\max(k, l)$, $V_{\mathbb C} = (\frac12, \frac12)$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]]).
>
> *Source: written here (the same count by Clebsch–Gordan on each copy: [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-10|Theorem §CB.8.10]])*

^thm-cb-16-9

> [!proof]- Proof
> Write representations of $\mathrm{Spin}(1,3)_0$ through $\lambda$ (Theorem §CB.16.2), with $\theta(\lambda) = (\lambda^\dagger)^{-1}$.
>
> **1. Spin k inside a tensor power of ℂ².** Let $A$ be $\lambda$ or $\theta(\lambda)$ acting on $\mathbb C^2$, and $M = 2k + 2m$ with $m \in \mathbb Z_{\ge0}$. $(\mathbb C^2)^{\otimes M} = (\mathbb C^2)^{\otimes2k}\otimes(\mathbb C^2\otimes\mathbb C^2)^{\otimes m}$ contains the invariant subspace $\operatorname{Sym}^{2k}\mathbb C^2\otimes(\Lambda^2\mathbb C^2)^{\otimes m}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], 1–2; a tensor product of invariant subspaces is invariant). $\Lambda^2\mathbb C^2$ is trivial for $\det A = 1$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], 1), so this subspace is $\operatorname{Sym}^{2k}(A)$, spin $k$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]]).
>
> **2. Tensor powers of the vector.** $V_{\mathbb C} \cong \lambda\otimes\theta(\lambda) = D^{(\frac12, \frac12)}$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]]), so $V_{\mathbb C}^{\otimes N} \cong (\lambda\otimes\theta(\lambda))^{\otimes N} \cong \lambda^{\otimes N}\otimes\theta(\lambda)^{\otimes N}$, the second equivalence being the permutation of tensor factors that collects the $\lambda$-slots first (a permutation of factors commutes with the diagonal action).
>
> **3. The parities match.** Let $N = 2\max(k, l)$, say $\max = k$ (the other case is symmetric). Then $N - 2k = 0$ and $N - 2l = 2(k - l)$ with $k - l = (k + l) - 2l \in \mathbb Z$ (since $k + l \in \mathbb Z$ and $2l \in \mathbb Z$) and $k - l \ge 0$.
>
> **4. Conclusion.** By step 1 with $A = \lambda$, $M = N$, $\lambda^{\otimes N} \supset \operatorname{Sym}^{2k}(\lambda)$; with $A = \theta(\lambda)$, $\theta(\lambda)^{\otimes N} \supset \operatorname{Sym}^{2l}(\theta(\lambda))\otimes(\text{trivial})$. Their tensor product is $D^{(k, l)}$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]]) inside $V_{\mathbb C}^{\otimes N}$ by step 2.
>
> **What the proof shows**
> - Each vector index is one undotted plus one dotted spinor slot; symmetrizing $2k$ undotted and $2l$ dotted slots and contracting the rest in pairs with $\varepsilon$ gives $(k, l)$. The condition $k + l \in \mathbb Z$ is exactly that the leftover slots of each kind pair up.

^pf-cb-16-9

*Uses:* [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-15|Theorem §CB.6.15]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-2|Theorem §CB.16.2]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-5|Theorem §CB.16.5]]

> [!theorem] Theorem §CB.16.10: The TA's Theorem for the Lorentz Group
> Every spinorial irreducible representation $(j_+, j_-)$ ($j_+ + j_- \in \frac12 + \mathbb Z$, [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-12|Theorem §CB.15.12]]) is equivalent to a subrepresentation of $S\otimes T$, $S = (\frac12, 0)\oplus(0, \frac12)$ the Dirac module and $T$ tensorial: $(j_+, j_-) \subset (\frac12, 0)\otimes(j_+ - \frac12, j_-)$ if $j_+ \ge \frac12$, and $(j_+, j_-) \subset (0, \frac12)\otimes(j_+, j_- - \frac12)$ otherwise; and $T$ lies in a tensor power of $V_{\mathbb C}$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-9|Theorem §CB.16.9]]). With complete reducibility ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]]) every finite-dimensional spinorial representation lies in $S\otimes T$ with $T$ a direct sum of subrepresentations of tensor powers of $V_{\mathbb C}$: part 3 of [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-12-21|Theorem §CB.12.21]] for $\mathbb R^{1,3}$, with $T$ inside a single tensor power when the representation is irreducible.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · the decomposition of products: [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-8|Theorem §CB.15.8]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-10|Theorem §CB.8.10]] · written here*

^thm-cb-16-10

> [!proof]- Proof
> Representations are written through $\lambda$, $\theta(\lambda) = (\lambda^\dagger)^{-1}$ (Theorem §CB.16.2); $D^{(j_+, j_-)}(\lambda) = \operatorname{Sym}^{2j_+}(\lambda)\otimes\operatorname{Sym}^{2j_-}(\theta(\lambda))$ ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]]).
>
> **1. Case j₊ ≥ ½.** $D^{(\frac12, 0)}\otimes D^{(j_+ - \frac12, j_-)} = \lambda\otimes\operatorname{Sym}^{2j_+ - 1}(\lambda)\otimes\operatorname{Sym}^{2j_-}(\theta(\lambda))$. The first two factors are $V_{1/2}\otimes V_{j_+ - 1/2}$ for $\lambda$, which contains $V_{j_+}$ (the top term of the Clebsch–Gordan series, Theorem §CB.8.10, as $j_+ = \frac12 + (j_+ - \frac12)$). Tensoring with $\operatorname{Sym}^{2j_-}(\theta(\lambda))$: $D^{(\frac12, 0)}\otimes D^{(j_+ - \frac12, j_-)} \supset D^{(j_+, j_-)}$.
>
> **2. Case j₊ = 0.** Then $j_- \in \frac12 + \mathbb Z$, so $j_- \ge \frac12$, and the same argument on the second factor gives $D^{(0, \frac12)}\otimes D^{(0, j_- - \frac12)} \supset D^{(0, j_-)}$.
>
> **3. The second factor is tensorial.** Its labels add to $j_+ + j_- - \frac12 \in \mathbb Z$, so it is tensorial ([[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-12|Theorem §CB.15.12]]), and by [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-9|Theorem §CB.16.9]] it is a subrepresentation of $V_{\mathbb C}^{\otimes N}$ for some $N$. $D^{(\frac12, 0)}$ and $D^{(0, \frac12)}$ are $S^-$ and $S^+$, subrepresentations of the Dirac module $S$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-2|Theorem §CB.16.2]]). Tensoring inclusions gives $(j_+, j_-) \subset S\otimes V_{\mathbb C}^{\otimes N}$.
>
> **4. Reducible representations.** A finite-dimensional spinorial $W$ is a direct sum of irreducible $W_i$ (Theorem §CB.15.1); $-1$ acts as $-\mathbb 1$ on $W$, so on each $W_i$, and each $W_i \cong D^{(j_+, j_-)}$ with $j_+ + j_- \in \frac12 + \mathbb Z$ (Theorems §CB.15.5, §CB.15.12). By step 3, $W_i \subset S\otimes T_i$ with $T_i \subset V_{\mathbb C}^{\otimes N_i}$, so $W \subset \bigoplus_i(S\otimes T_i) = S\otimes\bigl(\bigoplus_iT_i\bigr)$, and $\bigoplus_iT_i$ is tensorial.
>
> **What the proof shows**
> - A spinorial field of any spin is a Dirac spinor with tensor indices, projected: one spinor slot carries the half-integer part, the remaining slots pair into vector indices. The Rarita–Schwinger field $\psi_\mu$ is the first case beyond the Dirac field, $(1, \frac12)\oplus(\frac12, 1) \subset S\otimes V_{\mathbb C}$.
> - Step 4 gives a direct sum of tensor powers; putting all $T_i$ into one tensor power needs an extra multiplicity count (the $T_i$ can be chosen of one parity class, using also $(\frac12, 0)\otimes(j_+ + \frac12, j_-) \supset (j_+, j_-)$), not carried out here.

^pf-cb-16-10

*Uses:* [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-10|Theorem §CB.8.10]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-5|Theorem §CB.15.5]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-12|Theorem §CB.15.12]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-2|Theorem §CB.16.2]], [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-9|Theorem §CB.16.9]]

> [!remark]- ★ Remark: Majorana spinors as a real structure (forward pointer)
> $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$ has no real four-dimensional module ([[§CB.10 Clifford Algebras꞉ Grading, Basis and the Volume Element#^rem-cb-10-1|§CB.10, ★ Remark: The real classification]]), but the Dirac module carries a conjugate-linear map $\mathcal C$ commuting with $\mathrm{Spin}(1,3)_0$ and with $\mathcal C^2 = \mathbb 1$ (charge conjugation); its fixed vectors are the Majorana spinors, a real form of $S$ for the group, exchanging $S^+$ with $S^-$ ([[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-16-3|Theorem §CB.16.3]]). To be stated and proved with the Majorana field (QFT C9, planned); [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]].

^rem-cb-16-1

> [!remark]- Connections
> - This section is the TA's picture for the course's spinors in one place: the Dirac module is a Clifford module (C5a.1), restricted to the spin group it is $(\frac12, 0)\oplus(0, \frac12)$ (C5a.3), $\gamma^5$ is the volume element (C5a.5), and vectors and two-forms are bispinors (C3.3, C3.4).
> - Theorem §CB.16.10 is why higher-spin fermion fields (Rarita–Schwinger $\psi_\mu$, a spinor with a vector index) are built as spinor ⊗ tensor and then projected.
> - **Used in**: Theorems §CB.16.1–§CB.16.3 — [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-2|Def. §C5a.5.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]], [[§C9.4 Fermion Bilinears under Parity|§C9.4]]; Theorem §CB.16.4 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]], [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]; Theorem §CB.16.5 — [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-6|Theorem §C5a.5.6]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]; Theorem §CB.16.6 — [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]; Theorem §CB.16.8 — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]], [[§C5a.11 Gamma-Matrix Technology#^rem-c5a-11-3|§C5a.11, ★ Remark: The simplest Fierz identity]]; Theorem §CB.16.10 — [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-7|Theorem §CB.15.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]].
