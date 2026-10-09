---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.18
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries]] →

*Sources: PHY 513 TA (oral remark, Oct 2026) · through the course homes embedded below: Peskin & Schroeder, §§3.2–3.4; the user's PHY 513 notes, Ch. 8 §§8.1–8.3, §8.9; PHY 513 Lectures 7–8; Yu Zhao-Huan, 量子场论讲义, §5.1 · P. Woit, Quantum Theory, Groups and Representations, §41.2 "Dirac γ matrices and Cliff(3,1)" (the strategy: quadratic Clifford elements give the Lorentz algebra, and the chiral blocks give $(\frac12, 0)$ and $(0, \frac12)$; Woit uses signature $(3,1)$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the Clifford-module computations and the comparison of conventions written here.*

What is the Dirac spinor as a representation of $\mathrm{Spin}(1,3)_0 = SL(2, \mathbb C)$, and where do $\gamma^5$, the Weyl halves, the bispinor form of a four-vector and the sixteen bilinears come from? This section specializes the TA's theorem ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-17|Theorem §CB.18.17]]) to Minkowski space: the Dirac module $\mathbb C^4$ restricts to $S^-\oplus S^+ = (\frac12, 0)\oplus(0, \frac12)$, split by $\gamma^5$, the image of the complex volume element (of the opposite orientation, Theorem §CB.18.2); Clifford multiplication exchanges the halves; the complexified vector is $S^+\otimes S^-$; two-forms are $(1,0)\oplus(0,1)$; the Clifford algebra itself is $\Lambda V$ as a representation, which is the classification of bilinears; and every spinorial representation sits in Dirac ⊗ tensor. It builds on [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.16]]–[[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)|§CB.17]]; the course's statements are shown as embeds where they become instances.

Notation as in §CB.16: $V = \mathbb R^{1,3}$, standard basis $e_\mu$, the isomorphism $\phi$ and $\theta(\lambda) = (\lambda^\dagger)^{-1}$ of [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-12|Theorem §CB.16.12]]. The Dirac module is the course's Clifford multiplication ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-1|Def. §CB.18.1]]): $\gamma(a) = \slashed a = a_\mu\gamma^\mu$ on $S = \mathbb C^4$, so $\gamma(e_\mu) = \gamma_\mu = g_{\mu\nu}\gamma^\nu$. It is a Clifford module of $(V, q)$ since $\slashed a\,\slashed a = a_\mu a^\mu$ ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]], 2), so it extends to an algebra homomorphism $\gamma : \mathrm{Cl}(1,3)_{\mathbb C} \to \operatorname{End}(S)$ ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-7|Theorem §CB.11.7]]). The chiral basis is [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-3|Def. §C5a.1.3]].

The course's Clifford multiplication, the map behind this notation (first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]):

> [!definition] Definition §CB.18.1: Clifford Multiplication
> Let $M = \mathbb R^{1,3}$ be Minkowski space with metric $g$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-11|Def. §CB.0.11]]). **Clifford multiplication** is the map
>
> $$
> M\times V \to V, \qquad (a, \psi) \mapsto \slashed{a}\,\psi \equiv a_\mu\Gamma^\mu\psi, \qquad a_\mu = g_{\mu\nu}a^\nu ,
> $$
>
> with the Dirac maps $\Gamma^\mu$ ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-14|Def. §CB.11.14]]). It is linear in $a$ and in $\psi$, and $\slashed{a}\,\slashed{a}\,\psi = (a\cdot a)\,\psi$ ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]], 2). As a tensor, $\Gamma = (\Gamma^\mu) \in M\otimes\operatorname{End}(V) \cong M\otimes V\otimes V'$, with components $(\gamma^\mu)_{ab}$: one Minkowski slot $\mu$, one $V$-slot $a$, one $V'$-slot $b$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-8|Def. §CB.0.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots": "$\gamma^\mu$ is an invariant tensor with one spacetime slot and two spinor slots") · PS §3.2, p. 42 · the name and the map formulation written here*

^def-cb-18-1

> [!caution] Caution: Two Dirac modules, and the sign of γ⁵
> Both $e_\mu \mapsto \gamma_\mu$ (used here) and $e_\mu \mapsto \gamma^\mu$ are Clifford modules of $\mathbb R^{1,3}$; the second is the first composed with the automorphism $\hat{\mathcal P}$ of $\mathrm{Cl}(1,3)$ extending parity $\mathcal P = \operatorname{diag}(1, -1, -1, -1)$ (Theorem §CB.11.7), since $\gamma^\mu = \gamma(\mathcal Pe_\mu)$. Only the first makes $\gamma(x)$ the course's spinor matrix of $\rho(x)$: $\gamma(x) = \Lambda_{1/2}(\omega)$ when $\rho(x) = e^\omega$ (Theorem §CB.18.3); with $e_\mu \mapsto \gamma^\mu$ the same $\gamma(x)$ belongs to $\mathcal P\rho(x)\mathcal P$, boosts reversed. They also differ on the volume element: $e_\mu \mapsto \gamma^\mu$ sends $\omega_{\mathbb C} = ie_0e_1e_2e_3$ to $\gamma^5$ (the reading of [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-13|Theorem §CB.12.13]] and [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-4|Def. §CB.13.4]]), $e_\mu \mapsto \gamma_\mu$ sends it to $-\gamma^5$ (Theorem §CB.18.2). So for the module used here the half-spin spaces $\omega_{\mathbb C} = \pm1$ of [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-24|Def. §CB.14.24]] are the course's $\gamma^5 = \mp1$ spaces. This section keeps the course's labels: $S^\pm$ is $\gamma^5 = \pm1$, and $S^-$ is left-handed.
>
> *Source: the slash notation is introduced with the Dirac equation, the course's [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-2|Def. §C5a.7.2]] (moved here from the statement, CB ordering pass) · written here, checked against [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-8|Theorem §CB.18.8]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]*

^cau-cb-18-1

## The Dirac module and its two halves

The Dirac maps, the Clifford module of the course, and $\gamma^5$, stated in §CB.11 and §CB.12 (first written in [[§C5a.1 Spinor Space and the Clifford Action|§C5a.1]] and [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]]); the module is irreducible of dimension $4 = 2^{4/2}$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-8|Theorem §CB.13.8]]).

> [!theorem] Theorem §CB.18.2: γ⁵ Is the Complex Volume Element (of the Opposite Orientation)
> In the Dirac module $\gamma(a) = \slashed a$, the complex volume element $\omega_{\mathbb C} = ie_0e_1e_2e_3$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-4|Def. §CB.13.4]]) goes to $\gamma(\omega_{\mathbb C}) = i\gamma_0\gamma_1\gamma_2\gamma_3 = -\gamma^5$, with $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|Def. §CB.12.14]]): $\gamma^5$ is the image of $-\omega_{\mathbb C}$, the complex volume element of the opposite orientation ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-13|Theorem §CB.12.13]], 1; [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-18-1|Caution: Two Dirac modules, and the sign of γ⁵]]). Hence $(\gamma^5)^2 = \mathbb 1$, $\gamma^5$ anticommutes with every $\gamma^\mu$ and commutes with $\gamma(\mathrm{Cl}^0)$, in particular with every $S^{\mu\nu}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]]; Theorem §CB.12.13, 3).
>
> *Source: written here · Peskin & Schroeder, §3.4 (the properties of $\gamma^5$), through [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]*

^thm-cb-18-2

> [!proof]- Proof
> **1. The phase.** In Def. §CB.13.4 take the orthonormal basis $(e_0, e_1, e_2, e_3)$: $n = 4$, one positive and $s = 3$ negative squares, so $i^{n(n-1)/2 + s} = i^{6 + 3} = i^9 = i$ and $\omega_{\mathbb C} = ie_0e_1e_2e_3$.
>
> **2. Its image.** $\gamma$ is an algebra homomorphism, so $\gamma(\omega_{\mathbb C}) = i\gamma_0\gamma_1\gamma_2\gamma_3$. With $\gamma_0 = \gamma^0$ and $\gamma_i = -\gamma^i$: $i\gamma_0\gamma_1\gamma_2\gamma_3 = i(-1)^3\gamma^0\gamma^1\gamma^2\gamma^3 = -\gamma^5$.
>
> **3. The opposite orientation.** $(e_1, e_0, e_2, e_3)$ is an orthonormal basis of the opposite orientation (one transposition), with the same signature, so its complex volume element is $ie_1e_0e_2e_3 = -ie_0e_1e_2e_3 = -\omega_{\mathbb C}$ (Theorem §CB.12.13, 1), and $\gamma(-\omega_{\mathbb C}) = \gamma^5$.
>
> **4. The square.** $\omega^2 = (-1)^{n(n-1)/2}(-1)^s = (-1)^6(-1)^3 = -1$ (Theorem §CB.12.13, 2), so $\omega_{\mathbb C}^2 = i^2\omega^2 = 1$ and $(\gamma^5)^2 = \gamma(\omega_{\mathbb C})^2 = \gamma(\omega_{\mathbb C}^2) = \mathbb 1$.
>
> **5. Anticommutation with the γ's.** $\omega v = (-1)^{n-1}v\omega = -v\omega$ for $v \in V$ (Theorem §CB.12.13, 3), so $\gamma^5\gamma_\mu = -\gamma_\mu\gamma^5$, and raising the index with $g^{\mu\nu}$, $\gamma^5\gamma^\mu = -\gamma^\mu\gamma^5$.
>
> **6. Commutation with the even part.** $\omega$ commutes with $\mathrm{Cl}^0$ (Theorem §CB.12.13, 3) — directly, $\gamma^5$ passes a product $\gamma_\mu\gamma_\nu$ with two sign changes. $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac i4g^{\mu\alpha}g^{\nu\beta}\gamma([e_\alpha, e_\beta])$ lies in $\gamma(\mathrm{Cl}^0_{\mathbb C})$, so $[\gamma^5, S^{\mu\nu}] = 0$, the course's statement [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|Theorem §CB.18.4]], 1 (read in the chiral basis in [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^ex-cb-12-16|Example §CB.12.16]]).
>
> **What the proof shows**
> - $\gamma^5$ is a volume element: its algebraic properties (square $1$, anticommuting with vectors, central in the even part) are those of $\omega_{\mathbb C}$ in even dimension, and nothing specific to the Dirac matrices was used.
> - ⚑ By-product (convention): which sign of the volume element is $\gamma^5$ depends on the orientation and on whether $e_\mu$ goes to $\gamma_\mu$ or $\gamma^\mu$ (Caution above); the course's $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ is $+\omega_{\mathbb C}$ for $e_\mu \mapsto \gamma^\mu$ and $-\omega_{\mathbb C}$ for Clifford multiplication.

^pf-cb-18-2

*Uses:* [[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-4|Def. §CB.13.4]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-13|Theorem §CB.12.13]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|Def. §CB.12.14]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]]

> [!theorem] Theorem §CB.18.3: The Dirac Module Restricted to SL(2,ℂ) Is (½, 0) ⊕ (0, ½)
> Restricted to $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ ([[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-12|Theorem §CB.16.12]]), the Dirac module is $S = S^-\oplus S^+$, $S^\pm$ the $\pm1$ eigenspaces of $\gamma^5$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-2|Theorem §CB.18.2]]); $S^-$ and $S^+$ are invariant, irreducible, two-dimensional and inequivalent ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]; Step 6 below). If $x \in \mathrm{Spin}(1,3)_0$ and $\lambda = \theta(\phi(x))$ is the element with $\rho(x) = \pi(\lambda)$ (Theorem §CB.16.12, 2), then $x$ acts on $S^-$ by a matrix equivalent to $\lambda$ and on $S^+$ by one equivalent to $(\lambda^\dagger)^{-1}$: $S^- = (\frac12, 0)$ and $S^+ = (0, \frac12)$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]). In particular $\gamma(x_\omega) = \Lambda_{1/2}(\omega)$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]]) for $x_\omega = \exp(\frac14\omega^{\mu\nu}e_\mu e_\nu) \in \mathrm{Spin}(1,3)_0$, which covers $\rho(x_\omega) = e^\omega$.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · Peskin & Schroeder, §3.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]] · written here · the course's version of the labels: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]] (left-handed spinors have $\gamma^5 = -1$; moved here from the statement, CB ordering pass)*

^thm-cb-18-3

> [!proof]- Proof
> **1. The spinor matrices are Clifford exponentials.** $\frac14\omega^{\alpha\beta}e_\alpha e_\beta = \sum_{\alpha<\beta}\omega^{\alpha\beta}\cdot\frac12e_\alpha e_\beta$ ($\omega$ antisymmetric) lies in $\mathfrak{spin}(1,3)$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-13|Def. §CB.14.13]]), so $x_\omega \in \mathrm{Spin}(1,3)_0$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-14|Theorem §CB.14.14]], 1; [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], 2). By [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-13|Theorem §CB.16.13]], $\rho_\ast(\frac12e_\alpha e_\beta) = M_{\alpha\beta}$, so $\rho(x_\omega) = \exp(\frac12\omega^{\alpha\beta}M_{\alpha\beta}) = \exp(\frac12\omega_{\alpha\beta}M^{\alpha\beta}) = e^\omega$ ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-3|Theorem §CB.3.3]]; [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]). On the spinor side, $\gamma(\frac14\omega^{\alpha\beta}e_\alpha e_\beta) = \frac14\omega^{\alpha\beta}\gamma_\alpha\gamma_\beta = \frac14\omega_{\alpha\beta}\gamma^\alpha\gamma^\beta$ (moving the metric from the $\gamma$'s to $\omega$), and
>
> $$
> -\tfrac i2\omega_{\alpha\beta}S^{\alpha\beta} = -\tfrac i2\cdot\tfrac i4\,\omega_{\alpha\beta}\bigl(\gamma^\alpha\gamma^\beta - \gamma^\beta\gamma^\alpha\bigr) = \tfrac18\bigl(\omega_{\alpha\beta}\gamma^\alpha\gamma^\beta + \omega_{\beta\alpha}\gamma^\beta\gamma^\alpha\bigr) = \tfrac14\omega_{\alpha\beta}\gamma^\alpha\gamma^\beta ,
> $$
>
> using $\omega_{\alpha\beta} = -\omega_{\beta\alpha}$ and relabelling. $\gamma$ is a continuous algebra homomorphism, so it maps the exponential series term by term: $\gamma(x_\omega) = \exp(-\frac i2\omega_{\alpha\beta}S^{\alpha\beta}) = \Lambda_{1/2}(\omega)$.
>
> **2. The halves are invariant.** $\gamma(\mathrm{Spin}(1,3)_0) \subset \gamma(\mathrm{Cl}^0)$ commutes with $\gamma^5$ (Theorem §CB.18.2). If $\gamma^5\psi = \pm\psi$, then $\gamma^5\gamma(x)\psi = \gamma(x)\gamma^5\psi = \pm\gamma(x)\psi$. Since $(\gamma^5)^2 = \mathbb 1$, $S = S^-\oplus S^+$ via $\psi = \frac12(\mathbb 1 - \gamma^5)\psi + \frac12(\mathbb 1 + \gamma^5)\psi$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]]).
>
> **3. The even generators in the chiral basis.** With $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^i = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$ (Example §CB.11.13), $\gamma_0 = \gamma^0$, $\gamma_i = -\gamma^i$:
>
> $$
> \gamma(f_i) = \gamma_i\gamma_0 = \begin{pmatrix}0 & -\sigma^i\\ \sigma^i & 0\end{pmatrix}\begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix} = \begin{pmatrix}-\sigma^i & 0\\ 0 & \sigma^i\end{pmatrix} ,
> $$
>
> and $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ (Example §CB.12.16, 1): $S^-$ is the upper block ($\psi_L$), $S^+$ the lower ($\psi_R$).
>
> **4. The whole even part.** With $\tilde\kappa(A) = \sigma^2\bar A\sigma^2$, $\tilde\kappa(\sigma^i) = -\sigma^i$ (Theorem §CB.16.12, Proof, step 2), the maps $a \mapsto \gamma(a)$ and $a \mapsto \operatorname{diag}(\tilde\kappa(\phi(a)), \phi(a))$ are real-algebra homomorphisms $\mathrm{Cl}^0(1,3) \to M_4(\mathbb C)$ that agree on the generators $f_i$ (step 3; [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-11|Theorem §CB.16.11]]), hence everywhere.
>
> **5. The group.** For $x \in \mathrm{Spin}(1,3)_0$, $\det\phi(x) = 1$, so $\tilde\kappa(\phi(x)) = \theta(\phi(x)) = \lambda$ (Theorem §CB.16.12, Proof, step 3) and $\phi(x) = \theta(\lambda) = (\lambda^\dagger)^{-1}$ ($\theta^2 = \mathrm{id}$). So
>
> $$
> \gamma(x) = \begin{pmatrix}\lambda & 0\\ 0 & (\lambda^\dagger)^{-1}\end{pmatrix}, \qquad \rho(x) = \pi(\lambda),
> $$
>
> for $x = x_\omega$, $\lambda = \pm\Lambda_L(\omega)$, matching step 1.
>
> **6. Labels, irreducibility, inequivalence.** On $S^-$, $x$ acts by $\lambda$, i.e. by $D^{(\frac12, 0)}(\lambda)$ ($\operatorname{Sym}^1\mathbb C^2 = \mathbb C^2$), on $S^+$ by $(\lambda^\dagger)^{-1} = D^{(0, \frac12)}(\lambda)$. Through the isomorphism $\theta\circ\phi : \mathrm{Spin}(1,3)_0 \to SL(2, \mathbb C)$ (Theorem §CB.16.12) these are irreducible, of dimension $2$, and inequivalent (Theorem §CB.17.7; directly, [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]]). $-1 \in \mathrm{Spin}(1,3)_0$ has $\lambda = -\mathbb 1$ and acts as $-\mathbb 1_4$: the module is spinorial.
>
> **7. Any other basis.** Dirac matrices in another basis are $U\gamma^\mu U^{-1}$ ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-15|Theorem §CB.11.15]]); then $\gamma$ and $\gamma^5$ are conjugated by $U$, which maps the eigenspaces of $\gamma^5$ onto those of $U\gamma^5U^{-1}$ and intertwines the actions. So steps 2–6 hold in every basis.
>
> **What the proof shows**
> - Step 5 is the course's form $\operatorname{diag}(\lambda, (\lambda^\dagger)^{-1})$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], 2 (comparison moved here from step 5, CB ordering pass).
> - The course's pair $(\Lambda_L, \Lambda_R)$ is the action of the spin group through the Clifford algebra: $\Lambda_{1/2}(\omega)$ is literally $\gamma(\exp\frac14\omega^{\mu\nu}e_\mu e_\nu)$.
> - ⚑ By-product (convention): the left-handed half carries $\lambda = \theta(\phi(x))$, not $\phi(x)$; with the Clifford identification $\phi$ alone the labels $(\frac12, 0)$, $(0, \frac12)$ would be exchanged (Theorem §CB.17.7, Proof).
> - Used next: Clifford multiplication between the halves (Theorem §CB.18.9) and the vector as a bispinor (Theorem §CB.18.10).

^pf-cb-18-3

*Uses:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-13|Def. §CB.14.13]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-14|Theorem §CB.14.14]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-3|Theorem §CB.3.3]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-10|Theorem §CB.3.10]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-11|Theorem §CB.16.11]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-12|Theorem §CB.16.12]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-13|Theorem §CB.16.13]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-2|Theorem §CB.18.2]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-11-13|Example §CB.11.13]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-15|Theorem §CB.11.15]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^ex-cb-12-16|Example §CB.12.16]]

The same split from the volume element alone, without the spin group (the course's route, PS §3.4, p. 50); in the course's chiral basis it is read off in [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]] (physics):

> [!theorem] Theorem §CB.18.4: γ⁵ Commutes with the Spinor Generators and Splits the Dirac Module
> For $4\times4$ Dirac matrices ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]]) on $S = \mathbb C^4$, with $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|Def. §CB.12.14]]), the spinor generators $S^{\mu\nu}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]]), $J_i = \frac12\varepsilon_{ijk}S^{jk}$, $K_i = S^{0i}$ and $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$:
> 1. $[\gamma^5, S^{\mu\nu}] = 0$, hence $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$ for every $\Lambda_{1/2}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]]): $\gamma^5$ is a Lorentz scalar. Moreover $K_i = i\gamma^5J_i$, so $\mathbf J_\pm = \frac12(\mathbb 1 \mp \gamma^5)\,\mathbf J$.
> 2. In every basis, $S = S^-\oplus S^+$, the eigenspaces of $\gamma^5$ for $-1$ and $+1$; both are two-dimensional and invariant under every $S^{\mu\nu}$ and every $\Lambda_{1/2}$.
> 3. On $S^-$, $\mathbf J_- = 0$ and $\mathbf J_+ = \mathbf J$ has spin ½; on $S^+$, $\mathbf J_+ = 0$ and $\mathbf J_- = \mathbf J$ has spin ½. So $S^- \cong (\frac12, 0)$ and $S^+ \cong (0, \frac12)$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-2|Def. §CB.17.2]]).
> 4. $e^{-2\pi iJ_3} = -\mathbb 1$: the representation is spinorial ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-26|Def. §CB.14.26]]).
>
> Theorem §CB.18.3 reaches the same split through the spin group and $SL(2, \mathbb C)$; this theorem reaches it from the volume element alone, without choosing a basis.
>
> *Source: PS §3.4, p. 50 ("$[\gamma^5, S^{\mu\nu}] = 0$. Thus the Dirac representation must be reducible …"), eq. (3.72) · Yu §5.1, eq. (5.36) ($\gamma^5$ a Lorentz scalar) · PHY 513 Lecture 7, Part B ("4 dim. Dirac spinor representation is reducible") · the user's PHY 513 notes, Ch. 8 §8.2 ("How the two halves transform"), Ch. 9 §9.6 · part 1 as in the course (first written for [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]) · the basis-free route ($K_i = i\gamma^5J_i$ and parts 2–4) written here (the option-1 demo, 2026-10-08)*

^thm-cb-18-4

> [!proof]- Proof
> **1. γ⁵ commutes with products of two γ's.** $\gamma^5\gamma^\mu\gamma^\nu = -\gamma^\mu\gamma^5\gamma^\nu = \gamma^\mu\gamma^\nu\gamma^5$ (Theorem §CB.12.15, twice). Hence $\gamma^5$ commutes with $[\gamma^\mu, \gamma^\nu]$ and with $S^{\mu\nu}$, with every power of $A = -\frac i2\omega_{\mu\nu}S^{\mu\nu}$, and with $\Lambda_{1/2} = e^A$: $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$.
>
> **2. K = iγ⁵J.** Let $(i, j, k)$ be a cyclic permutation of $(1, 2, 3)$. Then $J_i = \frac12(S^{jk} - S^{kj}) = S^{jk} = \frac i2\gamma^j\gamma^k$ and $K_i = S^{0i} = \frac i2\gamma^0\gamma^i$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]]). A cyclic permutation of three anticommuting factors is two transpositions, so $\gamma^1\gamma^2\gamma^3 = \gamma^i\gamma^j\gamma^k$ and $\gamma^5 = i\gamma^0\gamma^i\gamma^j\gamma^k$. Then
>
> $$
> \gamma^5J_i = i\cdot\tfrac i2\,\gamma^0\gamma^i\,(\gamma^j\gamma^k\gamma^j\gamma^k) = -\tfrac12\gamma^0\gamma^i\bigl(-(\gamma^j)^2(\gamma^k)^2\bigr) = -\tfrac12\gamma^0\gamma^i\bigl(-(-1)(-1)\bigr) = \tfrac12\gamma^0\gamma^i = -iK_i ,
> $$
>
> using $\gamma^k\gamma^j = -\gamma^j\gamma^k$ and $(\gamma^j)^2 = (\gamma^k)^2 = -\mathbb 1$. So $K_i = i\gamma^5J_i$, and $\mathbf J_\pm = \frac12(\mathbf J \pm i\cdot i\gamma^5\mathbf J) = \frac12(\mathbb 1 \mp \gamma^5)\mathbf J$.
>
> **3. The two eigenspaces.** $(\gamma^5)^2 = \mathbb 1$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]]), so $P_\mp = \frac12(\mathbb 1 \mp \gamma^5)$ are complementary projections and $S = P_-S\oplus P_+S = S^-\oplus S^+$. $\operatorname{tr}\gamma^5 = 0$ (the same theorem), so the eigenvalues $-1$ and $+1$ occur equally often: $\dim S^\pm = 2$. A map commuting with $\gamma^5$ maps each eigenspace into itself; this holds for every $S^{\mu\nu}$ (step 1) and for $\Lambda_{1/2}$, a power series in them. In another basis everything is conjugated by the change-of-basis matrix ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-15|Theorem §CB.11.15]]), which maps eigenspaces to eigenspaces.
>
> **4. The labels.** On $S^-$, $\gamma^5 = -1$, so by step 2 $\mathbf J_+ = \mathbf J$ and $\mathbf J_- = 0$; on $S^+$ the reverse. The $J_i$ obey $[J_i, J_j] = i\varepsilon_{ijk}J_k$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|Theorem §CB.14.18]] for spatial indices), and $J_i^2 = -\frac14\gamma^j\gamma^k\gamma^j\gamma^k = \frac14(\gamma^j)^2(\gamma^k)^2 = \frac14\mathbb 1$. On the two-dimensional $S^-$, $J_3 = -i[J_1, J_2]$ is a commutator, so it is traceless; $J_3^2 = \frac14$ makes it diagonalizable with eigenvalues in $\{\frac12, -\frac12\}$, so its weights are $\frac12$ and $-\frac12$, once each, which by [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-6|Theorem §CB.10.6]] is spin ½. With $\mathbf J_- = 0$ this is $(\frac12, 0)$ (Def. §CB.17.2 with $j_+ = \frac12$, $j_- = 0$); likewise $S^+ \cong (0, \frac12)$.
>
> **5. The 2π rotation.** $(2J_3)^2 = \mathbb 1$, so $e^{-2\pi iJ_3} = e^{-i\pi(2J_3)} = \cos\pi\,\mathbb 1 - i\sin\pi\,(2J_3) = -\mathbb 1$.
>
> **What the proof shows**
> - No basis was chosen: the splitting is fixed by $\gamma^5$ alone, and any basis adapted to $S^-\oplus S^+$ makes all six generators block diagonal (in physics: the chiral basis, where $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]).
> - $S^\pm$ are irreducible and inequivalent ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-4|Theorem §CB.17.4]]): the half-spin representations, as in Theorem §CB.18.3.

^pf-cb-18-4

*Uses:* [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|Def. §CB.12.14]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-18|Theorem §CB.14.18]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-6|Theorem §CB.10.6]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^def-cb-17-2|Def. §CB.17.2]]

The course's comparison with the vector representation (first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]); its proof reads the Casimirs and the $2\pi$ rotation off the classification of §CB.17 (the course's chiral-basis computation follows as a remark):

> [!theorem] Theorem §CB.18.5: The Dirac Representation Is Not the Vector Representation
> The Dirac representation ($n = 4$ in [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]]) and the vector representation ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]) are both four-dimensional, but they are inequivalent ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-3-6|Def. §CB.3.6]]); these are the two tests of [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^rem-cb-17-1|§CB.17, Remark: Sums versus products]]:
> 1. on the Dirac representation the Casimirs ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-4|Theorem §CB.17.4]]) are $\mathbf J_+^2 = \operatorname{diag}(\frac34, \frac34, 0, 0)$ and $\mathbf J_-^2 = \operatorname{diag}(0, 0, \frac34, \frac34)$, on the vector representation $\mathbf J_\pm^2 = \frac34\mathbb 1$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|Theorem §CB.17.6]]);
> 2. a rotation by $2\pi$ is $-\mathbb 1$ on Dirac spinors and $+\mathbb 1$ on four-vectors;
> 3. under rotations the Dirac spinor is spin $\frac12\oplus\frac12$, the vector spin $0\oplus1$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (paragraph "Same dimension, different representation"), §8.2 (Derivation "… related by conjugation", paragraph "Why the Dirac spinor is not (½, ½)"; checked numerically there) · PHY 513 Lecture 7, Part B ("Unlike a 4-vector under rotation: spin-0 (time) and spin-1 (space)")*

^thm-cb-18-5

> [!derivation]- Derivation
> *Written in the CB ordering pass (2026-10-08) from the Clifford-module statements; the course's computation with the chiral-basis matrices is kept in the remark below.*
>
> **1. Casimirs.** By [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]] the Dirac module restricted to $SL(2, \mathbb C)$ is $S^-\oplus S^+$ with $S^- = (\frac12, 0)$ and $S^+ = (0, \frac12)$, so in a basis adapted to $S^-\oplus S^+$, $\mathbf J_+^2 = \operatorname{diag}(\frac34, \frac34, 0, 0)$ and $\mathbf J_-^2 = \operatorname{diag}(0, 0, \frac34, \frac34)$, by $\mathbf J_\pm^2 = j_\pm(j_\pm + 1)$ on $(j_+, j_-)$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-4|Theorem §CB.17.4]]). On the vector representation both are $\frac34\mathbb 1$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|Theorem §CB.17.6]]). An equivalence $D_{\rm Dirac} = UD_{\rm vec}U^{-1}$ would give $\mathbf J_+^2|_{\rm Dirac} = U\frac34\mathbb 1U^{-1} = \frac34\mathbb 1$: false.
>
> **2. 2π rotation.** A rotation by $2\pi$ acts on $(j_+, j_-)$ as $(-1)^{2(j_+ + j_-)}$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-8|Theorem §CB.17.8]], 2): as $-\mathbb 1_4$ on $(\frac12, 0)\oplus(0, \frac12)$ and as $+\mathbb 1_4$ on $(\frac12, \frac12)$; an equivalence maps $+\mathbb 1$ to $+\mathbb 1$.
>
> **3. Rotation content.** Under rotations $(j_+, j_-)$ contains the spins $|j_+ - j_-|, \dots, j_+ + j_-$ once each (Theorem §CB.17.8, 1): $(\frac12, 0)\oplus(0, \frac12)$ is spin $\frac12\oplus\frac12$, $(\frac12, \frac12)$ is spin $0\oplus1$ (directly: $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$ on the vector, Theorem §CB.17.6).
>
> **What the derivation shows**
> - In the Dirac spinor no component feels both copies $\mathbf J_\pm$ (a direct sum, $2 + 2$); in the vector every component feels both (a product, $2\times2$). The equality of dimensions is a coincidence of four dimensions ([Remark: What each Dirac index labels]).

^der-cb-18-5

*Uses:* [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-4|Theorem §CB.17.4]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|Theorem §CB.17.6]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-8|Theorem §CB.17.8]]

> [!remark]- Remark: The course's computation in the chiral basis
> The derivation of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]], kept here when the proof above was rewritten from the Clifford-module statements (CB ordering pass, 2026-10-08); it reads the Casimirs and the $2\pi$ rotation off the course's chiral-basis matrices.
>
> **1. Casimirs.** By Theorem §C5a.3.2, $\mathbf J_+ = \frac12\operatorname{diag}(\boldsymbol\sigma, 0)$, so $\mathbf J_+^2 = \frac14\operatorname{diag}(\boldsymbol\sigma\cdot\boldsymbol\sigma, 0) = \frac14\operatorname{diag}(3\cdot\mathbb 1, 0)$ ($\sigma_k^2 = \mathbb 1$ for each $k$); likewise $\mathbf J_-^2$. On the vector representation both are $\frac34\mathbb 1$ ([[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]). An equivalence $D_{\rm Dirac} = UD_{\rm vec}U^{-1}$ would give $\mathbf J_+^2|_{\rm Dirac} = U\frac34\mathbb 1U^{-1} = \frac34\mathbb 1$: false.
>
> **2. 2π rotation.** Theorem §C5a.4.3, step 4: $-\mathbb 1_4$ against $+\mathbb 1_4$; an equivalence maps $+\mathbb 1$ to $+\mathbb 1$.
>
> **3. Rotation content.** $\mathbf J = \frac12\boldsymbol\Sigma$ is spin ½ on each block; on the vector, $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$ (Theorem §C3.2.2): spin $0$ on $v^0$, spin $1$ on $\mathbf v$.
>
> **What the derivation shows**
> - In the Dirac spinor no component feels both copies $\mathbf J_\pm$ (a direct sum, $2 + 2$); in the vector every component feels both (a product, $2\times2$). The equality of dimensions is a coincidence of four dimensions ([[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|Remark: What each Dirac index labels]]).
>
> *Uses:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]]

^rem-cb-18-3


> [!theorem] Theorem §CB.18.6: The Two Halves Are Complex Conjugates of Each Other
> As representations of $SL(2, \mathbb C)$, $S^- \cong \overline{S^+}$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-7|Def. §CB.8.7]]) and $S^\pm \cong (S^\pm)^\ast$ via $\varepsilon$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]]); more generally $\overline{(j_+, j_-)} \cong (j_-, j_+)$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-8|Theorem §CB.8.8]]).
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.6, Ch. 8 §8.2 · the algebra form: [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-13|Theorem §CB.17.13]] · the group-level proof written here*

^thm-cb-18-6

> [!proof]- Proof
> By Theorem §CB.18.3, $S^-$ carries $\lambda$ and $S^+$ carries $\theta(\lambda) = (\lambda^\dagger)^{-1}$, $\lambda \in SL(2, \mathbb C)$. Let $\varepsilon = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$, a real matrix.
>
> **1. Two ε-identities.** By [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]], 2, $(\lambda^{-1})^{\mathsf T} = \varepsilon\lambda\varepsilon^{-1}$; and $\theta(\lambda) = \varepsilon\bar\lambda\varepsilon^{-1}$ (Theorem §CB.16.12, Proof, step 3, with $\varepsilon\bar A\varepsilon^{-1} = \sigma^2\bar A\sigma^2$). Conjugating the second entrywise ($\varepsilon$ is real): $\overline{\theta(\lambda)} = \varepsilon\lambda\varepsilon^{-1}$.
>
> **2. The halves are conjugate.** The conjugate representation of $S^+$ has matrices $\overline{\theta(\lambda)}$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-7|Def. §CB.8.7]]) $= \varepsilon\lambda\varepsilon^{-1}$ (step 1): $\varepsilon$ is an invertible intertwiner from $S^-$ to $\overline{S^+}$. So $S^- \cong \overline{S^+}$, and conjugating again $\overline{S^-} \cong S^+$.
>
> **3. Each half is self-dual.** The dual of $S^-$ has matrices $(\lambda^{-1})^{\mathsf T} = \varepsilon\lambda\varepsilon^{-1}$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|Def. §CB.8.6]], step 1), so $(S^-)^\ast \cong S^-$ via $\varepsilon$. The dual of $S^+$ has matrices $(\theta(\lambda)^{-1})^{\mathsf T} = (\lambda^\dagger)^{\mathsf T} = \bar\lambda = \varepsilon^{-1}\theta(\lambda)\varepsilon$, so $(S^+)^\ast \cong S^+$ via $\varepsilon^{-1}$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]]).
>
> **4. General (j₊, j₋).** Entrywise conjugation commutes with tensor products and with restriction to $\operatorname{Sym}^k$ (a subspace defined by real equations), so $\overline{D^{(j_+, j_-)}(\lambda)} = \operatorname{Sym}^{2j_+}(\bar\lambda)\otimes\operatorname{Sym}^{2j_-}(\overline{\theta(\lambda)})$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]). By step 1, $\bar\lambda = \varepsilon^{-1}\theta(\lambda)\varepsilon$ and $\overline{\theta(\lambda)} = \varepsilon\lambda\varepsilon^{-1}$; $\operatorname{Sym}^k$ of a conjugation is a conjugation by $\operatorname{Sym}^k(\varepsilon^{\mp1})$. Hence $\overline{D^{(j_+, j_-)}} \cong \operatorname{Sym}^{2j_+}(\theta(\lambda))\otimes\operatorname{Sym}^{2j_-}(\lambda)$, and the flip $u\otimes w \mapsto w\otimes u$ is an intertwiner onto $\operatorname{Sym}^{2j_-}(\lambda)\otimes\operatorname{Sym}^{2j_+}(\theta(\lambda)) = D^{(j_-, j_+)}(\lambda)$.
>
> **What the proof shows**
> - One invariant, $\varepsilon$, does all three jobs: it relates a half to its conjugate, to its dual, and (step 4) exchanges $j_+$ and $j_-$ under conjugation; at the algebra level this is [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-8|Theorem §CB.8.8]].
> - Used in the ★ Remark on Majorana spinors below: a conjugate-linear map can exchange $S^+$ and $S^-$.

^pf-cb-18-6

*Uses:* [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|Def. §CB.8.6]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-7|Def. §CB.8.7]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-12|Theorem §CB.16.12]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]]

## Clifford multiplication, vectors and two-forms

The course's statements (first written in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]): the finite form of [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|Theorem §CB.14.17]], and Clifford multiplication as an intertwiner, used by the theorem after them:

> [!theorem] Theorem §CB.18.7: The Dirac Matrices Are an Invariant Vector of Matrices
> For $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]]) and $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^def-cb-5-2|Def. §CB.5.2]]) built from the same $\omega$:
> 1. $\Lambda_{1/2}^{-1}\,\gamma^\mu\,\Lambda_{1/2} = \Lambda^\mu{}_\nu\,\gamma^\nu$;
> 2. $\Lambda_{1/2}^{-1}S^{\mu\nu}\Lambda_{1/2} = \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma S^{\rho\sigma}$, $\Lambda_{1/2}^{-1}\gamma_\mu\Lambda_{1/2} = (\Lambda^{-1})^\nu{}_\mu\gamma_\nu$, and $\Lambda_{1/2}^{-1}\mathbb 1\Lambda_{1/2} = \mathbb 1$;
> 3. in the chiral basis, with the Weyl matrices and $\sigma^\mu$, $\bar\sigma^\mu$ of [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^def-cb-16-6|Def. §CB.16.6]] and [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]], $\Lambda_L^{-1}\sigma^\mu\Lambda_R = \Lambda^\mu{}_\nu\sigma^\nu$ and $\Lambda_R^{-1}\bar\sigma^\mu\Lambda_L = \Lambda^\mu{}_\nu\bar\sigma^\nu$.
>
> *Source: PS §3.2, eq. (3.29) · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$") · the user's PHY 513 notes, Ch. 8 §8.1 (Derivation "The covariance of $\gamma^\mu$: finite transformations", eq. (gammacov), with its second proof and corollaries) · Yu §5.1, eqs. (5.17)–(5.31) · the user's pre-course notes, §5.1, eq. (gamma-vector)*

^thm-cb-18-7

> [!derivation]- Derivation
> Let $A = -\frac i2\omega_{\rho\sigma}S^{\rho\sigma}$, so $\Lambda_{1/2} = e^A$, and recall $-\frac i2\omega_{\rho\sigma}(\mathcal J^{\rho\sigma})^\mu{}_\nu = \omega^\mu{}_\nu$, so $\Lambda = e^{\omega}$ ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-3|Theorem §CB.5.3]]).
>
> **1. The infinitesimal statement.** By Theorem §CB.14.17, $[\gamma^\mu, A] = -\frac i2\omega_{\rho\sigma}[\gamma^\mu, S^{\rho\sigma}] = -\frac i2\omega_{\rho\sigma}(\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu = \omega^\mu{}_\nu\gamma^\nu$.
>
> **2. Two curves.** For $t \in [0, 1]$ put $F^\mu(t) = e^{-tA}\gamma^\mu e^{tA}$ and $G^\mu(t) = (e^{t\omega})^\mu{}_\nu\gamma^\nu$, four matrices each; $F^\mu(0) = G^\mu(0) = \gamma^\mu$.
>
> **3. The same linear equation.** $\frac{d}{dt}F^\mu = e^{-tA}(-A\gamma^\mu + \gamma^\mu A)e^{tA} = e^{-tA}[\gamma^\mu, A]e^{tA} = \omega^\mu{}_\nu e^{-tA}\gamma^\nu e^{tA} = \omega^\mu{}_\nu F^\nu$, by step 1 (the numbers $\omega^\mu{}_\nu$ pass through $e^{\pm tA}$). And $\frac{d}{dt}G^\mu = (\omega e^{t\omega})^\mu{}_\nu\gamma^\nu = \omega^\mu{}_\kappa G^\kappa$.
>
> **4. Uniqueness.** The difference $D^\mu = F^\mu - G^\mu$ obeys $\dot D^\mu = \omega^\mu{}_\nu D^\nu$, $D^\mu(0) = 0$. Then $\frac{d}{dt}\bigl[(e^{-t\omega})^\kappa{}_\mu D^\mu(t)\bigr] = -(e^{-t\omega}\omega)^\kappa{}_\mu D^\mu + (e^{-t\omega})^\kappa{}_\mu\omega^\mu{}_\nu D^\nu = 0$ ($\omega$ commutes with $e^{-t\omega}$), so $(e^{-t\omega})^\kappa{}_\mu D^\mu(t) = 0$ for all $t$; multiplying by $e^{t\omega}$, $D \equiv 0$. At $t = 1$: $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$.
>
> **5. Part 2.** $\Lambda_{1/2}^{-1}[\gamma^\mu, \gamma^\nu]\Lambda_{1/2} = [\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}, \Lambda_{1/2}^{-1}\gamma^\nu\Lambda_{1/2}]$ (insert $\Lambda_{1/2}\Lambda_{1/2}^{-1}$ between the factors) $= \Lambda^\mu{}_\rho\Lambda^\nu{}_\sigma[\gamma^\rho, \gamma^\sigma]$; times $\frac i4$ this is the law for $S$. For the lower index, $\gamma_\mu = g_{\mu\nu}\gamma^\nu$ gives $\Lambda_{1/2}^{-1}\gamma_\mu\Lambda_{1/2} = g_{\mu\nu}\Lambda^\nu{}_\rho g^{\rho\kappa}\gamma_\kappa$, and $\Lambda^{\mathsf T}g\Lambda = g$ means $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, i.e. $(\Lambda^{-1})^\kappa{}_\mu = g^{\kappa\rho}\Lambda^\nu{}_\rho g_{\nu\mu}$, which is the coefficient found.
>
> **6. Part 3.** In the chiral basis $\Lambda_{1/2} = \operatorname{diag}(\Lambda_L, \Lambda_R)$ (Theorem §CB.18.3), and block multiplication gives $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \begin{pmatrix}0 & \Lambda_L^{-1}\sigma^\mu\Lambda_R\\ \Lambda_R^{-1}\bar\sigma^\mu\Lambda_L & 0\end{pmatrix}$; compare the blocks of part 1. Since $\Lambda_L^{-1} = \Lambda_R^\dagger$ and $\Lambda_R^{-1} = \Lambda_L^\dagger$ ([[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-7|Theorem §CB.16.7]], 2), these are the invariance statements of [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-8|Theorem §CB.16.8]], 2, obtained here independently.
>
> **What the derivation shows**
> - Transforming the two spinor indices of $\gamma^\mu$ is the same as transforming its vector index: $\gamma^\mu$ is an invariant tensor with one vector slot and two spinor slots, as $g_{\mu\nu}$ is with two vector slots. "Take the vector index on $\gamma^\mu$ seriously" (PS): $\gamma^\mu\partial_\mu$ is a Lorentz-invariant operator on spinors ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]), and $\bar\psi\gamma^\mu\psi$ a vector ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]).
> - Part 2 for $S$ is the general law "the generators transform as a tensor" ([[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-8|Theorem §CB.5.8]]) for the Dirac representation.
> - Only the matched pair works: $\Lambda$ and $\Lambda_{1/2}$ from the same six numbers. The two-valuedness of $\Lambda_{1/2}$ is invisible here, since $\pm\Lambda_{1/2}$ give the same conjugation.

^der-cb-18-7

> [!derivation]- Derivation (second route: the nested-commutator series)
> **1. The series.** For matrices $A$, $B$ define $[B, A]_{(0)} = B$, $[B, A]_{(n+1)} = [[B, A]_{(n)}, A]$. The function $f(t) = e^{-tA}Be^{tA}$ satisfies $f'(t) = e^{-tA}[B, A]e^{tA}$ (as in step 3 above), and by induction $f^{(n)}(t) = e^{-tA}[B, A]_{(n)}e^{tA}$; $f$ is entire in $t$ (products of exponential series), so its Taylor series at $0$ converges at $t = 1$: $e^{-A}Be^A = \sum_{n\ge0}\frac1{n!}[B, A]_{(n)}$ (Yu (5.23), proved there by the binomial rearrangement (5.18)–(5.22)).
>
> **2. Iterate step 1 of the first route.** $[\gamma^\mu, A]_{(1)} = \omega^\mu{}_\nu\gamma^\nu$; if $[\gamma^\mu, A]_{(n)} = (\omega^n)^\mu{}_\nu\gamma^\nu$, then $[\gamma^\mu, A]_{(n+1)} = (\omega^n)^\mu{}_\nu[\gamma^\nu, A] = (\omega^n)^\mu{}_\nu\omega^\nu{}_\kappa\gamma^\kappa = (\omega^{n+1})^\mu{}_\kappa\gamma^\kappa$.
>
> **3. Sum.** $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \sum_n\frac1{n!}(\omega^n)^\mu{}_\nu\gamma^\nu = (e^\omega)^\mu{}_\nu\gamma^\nu = \Lambda^\mu{}_\nu\gamma^\nu$ (Yu (5.25)–(5.27)).
>
> *What this route shows:* the finite law is the infinitesimal one summed to all orders, term by term; the first route reaches it through uniqueness for a linear differential equation instead.

^der-cb-18-7b

*Uses:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|Theorem §CB.14.17]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-7|Theorem §CB.16.7]]

> [!theorem] Theorem §CB.18.8: Clifford Multiplication Is Lorentz Equivariant
> Let $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ and $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ be built from the same $\omega$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]]). Then, for Clifford multiplication ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-1|Def. §CB.18.1]]):
> 1. $\Lambda_{1/2}\bigl(\slashed{a}\,\psi\bigr) = \slashed{(\Lambda a)}\,\bigl(\Lambda_{1/2}\psi\bigr)$ for all $a \in M$, $\psi \in V$: moving the vector and the spinor together moves their product;
> 2. equivalently, transforming all three slots of $\gamma^\mu$ returns it: $\Lambda^\mu{}_\nu\,\Lambda_{1/2}\,\gamma^\nu\,\Lambda_{1/2}^{-1} = \gamma^\mu$.
>
> Both are the covariance of $\gamma^\mu$, $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]]), read as a statement about an intertwiner $M\otimes V \to V$ for the Lorentz group.
>
> *Source: PS §3.2, eq. (3.29) · PHY 513 Lecture 8, Part A (slides "'Transformation' of $\gamma^\mu$: Derivation", "Interpretation") · the user's PHY 513 notes, Ch. 8 §8.3 (Principle "Invariant tensors with mixed slots") · the equivariance form written here*

^thm-cb-18-8

> [!derivation]- Derivation
> **1. Conjugate the slash.** $\Lambda_{1/2}^{-1}\,\slashed{(\Lambda a)}\,\Lambda_{1/2} = (\Lambda a)_\mu\,\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}$ (the numbers $(\Lambda a)_\mu$ pull out) $= (\Lambda a)_\mu\,\Lambda^\mu{}_\nu\gamma^\nu$ (Theorem §CB.18.7, 1).
>
> **2. Lower the index explicitly.** $(\Lambda a)_\mu = g_{\mu\rho}\Lambda^\rho{}_\sigma a^\sigma$, so the coefficient of $\gamma^\nu$ is $g_{\mu\rho}\Lambda^\rho{}_\sigma\Lambda^\mu{}_\nu\,a^\sigma = g_{\sigma\nu}a^\sigma = a_\nu$, by the defining property $g_{\mu\rho}\Lambda^\mu{}_\nu\Lambda^\rho{}_\sigma = g_{\nu\sigma}$ of a Lorentz transformation ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]). Hence $\Lambda_{1/2}^{-1}\,\slashed{(\Lambda a)}\,\Lambda_{1/2} = a_\nu\gamma^\nu = \slashed{a}$.
>
> **3. Part 1.** Multiply step 2 on the left by $\Lambda_{1/2}$ and apply to $\psi$: $\slashed{(\Lambda a)}\,\Lambda_{1/2}\psi = \Lambda_{1/2}\,\slashed{a}\,\psi$.
>
> **4. Part 2.** From Theorem §CB.18.7, 1, multiply on the left by $\Lambda_{1/2}$ and on the right by $\Lambda_{1/2}^{-1}$: $\gamma^\mu = \Lambda_{1/2}\,\Lambda^\mu{}_\nu\gamma^\nu\,\Lambda_{1/2}^{-1} = \Lambda^\mu{}_\nu\,\Lambda_{1/2}\gamma^\nu\Lambda_{1/2}^{-1}$. The three factors are the slot rules: $\Lambda$ on the Minkowski index, $\Lambda_{1/2}$ on the $V$-index (left), $\Lambda_{1/2}^{-1}$ on the $V'$-index (right) — the slot rule of Theorem §CB.0.10 with the Lorentz matrices in place of $U$.
>
> **What the derivation shows**
> - This is the lecture's form $\gamma^\nu = \Lambda^\nu{}_\mu\Lambda_{1/2}\gamma^\mu\Lambda_{1/2}^{-1}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-2|§C5a.4, Remark: The lecture's form of the covariance]]). (moved here from the last step, CB ordering pass)
> - Clifford multiplication is a map between representations of the Lorentz group (vector ⊗ Dirac → Dirac) that commutes with the group action; such a map is an intertwiner, and its components $(\gamma^\mu)_{ab}$ are an invariant tensor. This is why a $\gamma$ matrix never acquires a transformation of its own under a Lorentz transformation.
> - Assumption used: $\Lambda$ and $\Lambda_{1/2}$ come from the same $\omega$, i.e. $\Lambda$ is the image of $\Lambda_{1/2}$ under the covering map $SL(2, \mathbb C) \to SO^+(1,3)$ ([[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-9|Theorem §CB.16.9]]); for a mismatched pair the identity fails ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-1|§C5a.4, Remark: One transformation, two matrices]]).
> - Used next: covariance of the Dirac equation ([[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]) is part 1 applied to $a = \partial$.

^der-cb-18-8

*Uses:* [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-1|Def. §CB.18.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-10|Theorem §CB.0.10]]

In terms of the two halves:

> [!theorem] Theorem §CB.18.9: Clifford Multiplication Exchanges the Halves Equivariantly
> The map $V\otimes S \to S$, $a\otimes\psi \mapsto \slashed a\psi$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-1|Def. §CB.18.1]]), is an intertwiner of $SL(2, \mathbb C)$-representations ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-27|Theorem §CB.14.27]]) and maps $V\otimes S^\pm$ to $S^\mp$.
>
> *Source: written here · the course's form: [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-8|Theorem §CB.18.8]]*

^thm-cb-18-9

> [!proof]- Proof
> **1. Equivariance.** For $x \in \mathrm{Spin}(1,3)$ and $a \in V$, $\rho(x)a = xax^{-1}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-10|Theorem §CB.14.10]], 2), and $\gamma$ is an algebra homomorphism, so $\gamma(x)\,\slashed a\,\gamma(x)^{-1} = \gamma(xax^{-1}) = \slashed{(\rho(x)a)}$. Applied to $\gamma(x)\psi$: $\gamma(x)(\slashed a\psi) = \slashed{(\rho(x)a)}\,\gamma(x)\psi$, i.e. the map $a\otimes\psi \mapsto \slashed a\psi$ intertwines $\rho\otimes\gamma$ with $\gamma$ ([[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-2|Def. §CB.7.2]]); this is Theorem §CB.14.27 for $\mathbb R^{1,3}$, and extends complex-linearly to $V_{\mathbb C}\otimes S$. For $x = x_\omega$ (Theorem §CB.18.3) it reads $\Lambda_{1/2}(\slashed a\psi) = \slashed{(e^\omega a)}\Lambda_{1/2}\psi$, the course's [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-8|Theorem §CB.18.8]], 1.
>
> **2. The halves are exchanged.** $\gamma^5\slashed a = -\slashed a\gamma^5$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-2|Theorem §CB.18.2]]). If $\gamma^5\psi = \pm\psi$, then $\gamma^5\slashed a\psi = -\slashed a\gamma^5\psi = \mp\slashed a\psi$: $\slashed a$ maps $S^\pm$ to $S^\mp$.
>
> **What the proof shows**
> - Equivariance is automatic: the spin group acts on vectors by conjugation inside the same algebra in which $\slashed a$ multiplies spinors. The $\gamma$'s "do not transform" because they are this intertwiner.

^pf-cb-18-9

*Uses:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-10|Theorem §CB.14.10]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-2|Def. §CB.7.2]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-2|Theorem §CB.18.2]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]]

> [!theorem] Theorem §CB.18.10: The Complexified Vector Is S⁺ ⊗ S⁻
> The map $V_{\mathbb C} \to \operatorname{Hom}(S^+, S^-) \cong (S^+)^\ast\otimes S^- \cong S^+\otimes S^-$, $a \mapsto \slashed a|_{S^+}$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-9|Theorem §CB.18.9]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]]), is an equivalence of $SL(2, \mathbb C)$-representations: $V_{\mathbb C} \cong (\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$. In the chiral basis ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-11-13|Example §CB.11.13]]) $\slashed a|_{S^+} : S^+ \to S^-$ has the matrix $a_\mu\sigma^\mu$, the course's $X$ for $a$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-20|Def. §CB.0.20]]), and $\slashed a|_{S^-} : S^- \to S^+$ has $a_\mu\bar\sigma^\mu$: $\sigma^\mu$ is an invariant tensor ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-10|Def. §CB.8.10]]) with one vector, one undotted and one dotted index.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.2 and Peskin & Schroeder, §3.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]] and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]] · written here*

^thm-cb-18-10

> [!proof]- Proof
> **1. An intertwiner.** By [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-9|Theorem §CB.18.9]], $\Phi(a) = \slashed a|_{S^+}$ lies in $\operatorname{Hom}(S^+, S^-)$, and $\Phi$ is complex-linear on $V_{\mathbb C}$. $\operatorname{Hom}(S^+, S^-)$ carries $x\cdot T = \gamma(x)|_{S^-}\,T\,(\gamma(x)|_{S^+})^{-1}$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]]). Restricting $\gamma(x)\slashed a\gamma(x)^{-1} = \slashed{(\rho(x)a)}$ (Theorem §CB.18.9, Proof, step 1) to $S^+$, where $\gamma(x)$ preserves both halves: $x\cdot\Phi(a) = \Phi(\rho(x)a)$.
>
> **2. The matrix.** In the chiral basis $\slashed a = a_\mu\gamma^\mu = \begin{pmatrix}0 & a_\mu\sigma^\mu\\ a_\mu\bar\sigma^\mu & 0\end{pmatrix}$ (Example §CB.11.13). $S^+$ is the lower block (Theorem §CB.18.3, Proof, step 3), and $\slashed a\binom{0}{\psi_R} = \binom{a_\mu\sigma^\mu\psi_R}{0}$: the matrix of $\Phi(a)$ is $a_\mu\sigma^\mu$. Likewise $\slashed a\binom{\psi_L}{0} = \binom{0}{a_\mu\bar\sigma^\mu\psi_L}$.
>
> **3. Injective.** $\mathbb 1, \sigma^1, \sigma^2, \sigma^3$ are linearly independent over $\mathbb C$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 4), so $a_\mu\sigma^\mu = 0$ forces $a_\mu = 0$, also for complex $a$. (A null complex $a$ has $\slashed a\,\slashed a = 0$ but $\slashed a \ne 0$; injectivity comes from the two blocks, not from $\slashed a\,\slashed a = q(a)$.)
>
> **4. An equivalence.** $\dim V_{\mathbb C} = 4 = 2\cdot2 = \dim\operatorname{Hom}(S^+, S^-)$, so $\Phi$ is an invertible intertwiner. Further $\operatorname{Hom}(S^+, S^-) \cong (S^+)^\ast\otimes S^-$ (Theorem §CB.8.9) and $(S^+)^\ast \cong S^+$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-6|Theorem §CB.18.6]]), so $V_{\mathbb C} \cong S^+\otimes S^-$. In terms of $\lambda$ (Theorem §CB.18.3) this is $(\lambda^\dagger)^{-1}\otimes\lambda$, and the flip of the two factors is an intertwiner onto $\lambda\otimes(\lambda^\dagger)^{-1} = D^{(\frac12, \frac12)}(\lambda)$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]).
>
> **5. The invariant tensor.** $\Phi \in V_{\mathbb C}'\otimes\operatorname{Hom}(S^+, S^-)$ is fixed by the group (Theorem §CB.8.9, [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-10|Def. §CB.8.10]]), with $\Phi(e_\mu) = \sigma_\mu = g_{\mu\nu}\sigma^\nu$: the array $\sigma^\mu$ with one vector index, one index of $S^-$ (undotted) and one of $(S^+)^\ast$ (dotted, [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]]). Check against the course: with $D_{S^-}(x) = \lambda$, $D_{S^+}(x) = (\lambda^\dagger)^{-1}$, step 1 reads $\lambda\,(a_\mu\sigma^\mu)\,\lambda^\dagger = (\rho(x)a)_\mu\sigma^\mu$, which for $\lambda = \Lambda_L(\omega)$, $\rho(x) = e^\omega$ is [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-8|Theorem §CB.16.8]], 1.
>
> **What the proof shows**
> - ⚑ By-product (convention, resolving the choice left open before): with Clifford multiplication $\slashed a = a_\mu\gamma^\mu$ and the chiral basis, the map from right- to left-handed spinors is $a_\mu\sigma^\mu$ and the reverse map is $a_\mu\bar\sigma^\mu$. With the other Dirac module $e_\mu \mapsto \gamma^\mu$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-18-1|Caution: Two Dirac modules, and the sign of γ⁵]]) the first would be $a_\mu\bar\sigma^\mu$.
> - A four-vector is a bispinor: one undotted and one dotted index, as in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]].

^pf-cb-18-10

*Uses:* [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-6|Theorem §CB.18.6]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-9|Theorem §CB.18.9]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-10|Def. §CB.8.10]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-16|Theorem §CB.8.16]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-11-13|Example §CB.11.13]]

The course's bispinor is the index form of this theorem, in the dotted-index calculus of physics: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]].

The vector representation is $(\frac12, \frac12)$ also by direct computation with the course's $4\times4$ generators, [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]] (physics: the same statement as Theorem §CB.18.10, read in the basis $v^0, \dots, v^3$).

> [!theorem] Theorem §CB.18.11: Two-Forms Are (1, 0) ⊕ (0, 1)
> $\Lambda^2V_{\mathbb C} \cong \Lambda^2(S^+\otimes S^-) \cong (\operatorname{Sym}^2S^+\otimes\Lambda^2S^-)\oplus(\Lambda^2S^+\otimes\operatorname{Sym}^2S^-) \cong \operatorname{Sym}^2S^+\oplus\operatorname{Sym}^2S^- = (1, 0)\oplus(0, 1)$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], 3; $\Lambda^2S^\pm$ trivial, [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]]). The two summands are the eigenspaces $\star = \pm i$ of duality ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-18|Theorem §CB.8.18]]), exchanged by complex conjugation; on the real two-forms this is the second case of [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-17|Theorem §CB.4.17]].
>
> *Source: written here · the course's statements: [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]]*

^thm-cb-18-11

> [!proof]- Proof
> All representations are of $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$, written through $\lambda$ (Theorem §CB.18.3): $S^-$ carries $\lambda$, $S^+$ carries $\theta(\lambda) = (\lambda^\dagger)^{-1}$, $V_{\mathbb C}$ carries $\rho(x)$.
>
> **1. Transport the equivalence.** If $T : A \to B$ is an equivalence, $T\otimes T$ restricted to $\Lambda^2A$ is an equivalence $\Lambda^2A \cong \Lambda^2B$. With [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]]: $\Lambda^2V_{\mathbb C} \cong \Lambda^2(S^+\otimes S^-)$.
>
> **2. Split the exterior square.** [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], 3, for $G_1 = G_2 = SL(2, \mathbb C)$ acting on $A = S^+$ and $B = S^-$, restricted to the diagonal $\lambda \mapsto (\lambda, \lambda)$ (an equivalence of $G_1\times G_2$-representations stays one on any subgroup): $\Lambda^2(S^+\otimes S^-) \cong (\operatorname{Sym}^2S^+\otimes\Lambda^2S^-)\oplus(\Lambda^2S^+\otimes\operatorname{Sym}^2S^-)$.
>
> **3. The two-dimensional exterior squares are trivial.** $\Lambda^2\mathbb C^2$ is the representation $A \mapsto \det A$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]], 1), and $\det\lambda = \det(\lambda^\dagger)^{-1} = 1$. So $\Lambda^2V_{\mathbb C} \cong \operatorname{Sym}^2S^+\oplus\operatorname{Sym}^2S^-$, i.e. $D^{(0,1)}\oplus D^{(1,0)}$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]), irreducible and inequivalent. Call the two summands $W_1 \cong (1, 0)$ and $W_2 \cong (0, 1)$ inside $\Lambda^2V_{\mathbb C}$.
>
> **4. The invariant subspaces of W₁ ⊕ W₂.** Let $E \subset W_1\oplus W_2$ be invariant, $p_k$ the projections onto $W_k$ (intertwiners). $E\cap W_k$ is invariant in the irreducible $W_k$, so it is $0$ or $W_k$. If $E \supset W_1$, then for $e = w_1 + w_2 \in E$ also $w_2 \in E$, so $E = W_1\oplus(E\cap W_2)$, i.e. $E = W_1$ or $E = W_1\oplus W_2$; likewise if $E \supset W_2$. If $E\cap W_1 = E\cap W_2 = 0$ and $E \ne 0$, take an irreducible invariant $E' \subset E$ (complete reducibility, [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-1|Theorem §CB.17.1]]): $p_1|_{E'}$ has kernel $E'\cap W_2 = 0$ and its image is a nonzero invariant subspace of $W_1$, hence $E' \cong W_1$; in the same way $E' \cong W_2$, contradicting $W_1 \not\cong W_2$. So the invariant subspaces are $0$, $W_1$, $W_2$, $W_1\oplus W_2$.
>
> **5. Duality picks the two summands.** By [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-18|Theorem §CB.8.18]], 3, $\Lambda^2V_{\mathbb C}$ is the direct sum of the three-dimensional eigenspaces $E_\pm$ of $\star$ (eigenvalues $\pm i$), each invariant under every $\Lambda$ with $\det\Lambda = 1$, so under $\rho(\mathrm{Spin}(1,3)_0) = SO^+(1,3)$. By step 4 a three-dimensional invariant subspace is $W_1$ or $W_2$, and $E_+ \ne E_-$: $\{E_+, E_-\} = \{W_1, W_2\}$.
>
> **6. Conjugation exchanges them.** Let $c$ be complex conjugation of the components of $\Lambda^2V_{\mathbb C}$. $\star$ has real coefficients, so $\star c = c\star$; if $\star A = iA$ then $\star(cA) = c(iA) = -i\,cA$. So $c(E_\pm) = E_\mp$.
>
> **7. The real two-forms.** The $c$-stable invariant subspaces are $0$ and $W_1\oplus W_2$ (steps 4, 6: $c(W_1) = W_2$). By [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-17|Theorem §CB.4.17]], 1, the real representation $\Lambda^2V$ has no invariant subspaces but $0$ and itself: it is irreducible, and its complexification is $W\oplus c(W)$ with $W$ irreducible, the second case of Theorem §CB.4.17, 2.
>
> **What the proof shows**
> - A real two-form is irreducible, yet over $\mathbb C$ it splits into self-dual and anti-self-dual parts, the field strengths of the two helicities: $\mathbf E \pm i\mathbf B$ in electrodynamics.
> - Which of $(1, 0)$, $(0, 1)$ is $\star = +i$ depends on the sign of $\varepsilon^{0123}$ and on the labelling of the halves; the theorem does not need it.

^pf-cb-18-11

*Uses:* [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-1|Theorem §CB.17.1]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-18|Theorem §CB.8.18]], [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-4-17|Theorem §CB.4.17]]

The two-index tensors as a whole, the course's decomposition (the user's PHY 513 notes, Ch. 7 §7.4.5):

> [!theorem] Theorem §CB.18.12: Two-Index Tensors Are (0, 0) ⊕ (1, 0) ⊕ (0, 1) ⊕ (1, 1)
> The representation $\Lambda\otimes\Lambda$ of $SO^+(1,3)$ on two-index tensors $T^{\mu\nu}$, with generators $\mathcal J^{\mu\nu}\otimes\mathbb 1 + \mathbb 1\otimes\mathcal J^{\mu\nu}$, has over $\mathbb C$ the invariant pieces ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-17|Theorem §CB.8.17]])
>
> $$
> \underbrace{\tfrac14g^{\mu\nu}T^\rho{}_\rho}_{(0,\,0)}\ \oplus\ \underbrace{T^{[\mu\nu]}}_{(1,\,0)\oplus(0,\,1)}\ \oplus\ \underbrace{T^{(\mu\nu)} - \tfrac14g^{\mu\nu}T^\rho{}_\rho}_{(1,\,1)} ,
> $$
>
> the two halves of the antisymmetric part being the eigenspaces $\star A = \pm iA$ of duality ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-18|Theorem §CB.8.18]]). Over $\mathbb R$, the six-dimensional real antisymmetric tensors are irreducible.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.5 (Derivation "Products: two-index tensors are (1,1)⊕(1,0)⊕(0,1)⊕(0,0)"; checked numerically there: "This proves the irreducibility that Section [tensors] could only quote") · the matching argument and the real case written out here*

^thm-cb-18-12

> [!derivation]- Derivation
> **1. Its decomposition.** With $\Lambda \cong (\frac12, \frac12)$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]]: $V_{\mathbb C} \cong S^+\otimes S^-$; in the course's matrices, Theorem §CB.17.6), Theorem §CB.17.11 gives $(1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, each once, of dimensions $9, 3, 3, 1$.
>
> **2. Four invariant subspaces.** By [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-17|Theorem §CB.8.17]] the trace part (dimension $1$), the antisymmetric part ($6$) and the symmetric traceless part ($9$) are each mapped into themselves by every $\Lambda$; by [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-18|Theorem §CB.8.18]], 3, the antisymmetric part is, over $\mathbb C$, the sum of two invariant three-dimensional eigenspaces of $\star$. So $\mathbb C^{16} = W_1\oplus W_3\oplus W_3'\oplus W_9$ with invariant $W_d$ of dimension $d$.
>
> **3. Match by dimension.** Each $W_d$ is a representation, hence a sum of pieces $(j_+, j_-)$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|Theorem §CB.17.5]]); joining these decompositions decomposes $\mathbb C^{16}$, and multiplicities are unique (Theorem §CB.17.5, step 9), so the pieces of the four $W_d$ together are exactly $(1, 1)$, $(1, 0)$, $(0, 1)$, $(0, 0)$, once each. The only piece of dimension $1$ is $(0, 0)$, so $W_1 = (0, 0)$. A three-dimensional $W_3$ must be made of pieces from $\{9, 3, 3\}$ with dimensions summing to $3$: a single $(1, 0)$ or $(0, 1)$, and $W_3$, $W_3'$ take one each. What remains, $W_9$, is $(1, 1)$.
>
> **4. Real irreducibility.** Let $U$ be a real subspace of the real antisymmetric tensors, invariant under every $\Lambda$. Its complexification $U_{\mathbb C} = U + iU$ is an invariant subspace of $(1, 0)\oplus(0, 1)$ and is closed under complex conjugation. The invariant subspaces of a sum of two inequivalent irreducible representations are $0$, either summand, or the whole (an invariant subspace is a sum of pieces, and with multiplicity one each piece is a fixed subspace). Complex conjugation maps the $(+i)$-eigenspace of the real map $\star$ to the $(-i)$-eigenspace (Theorem §CB.8.18, 3), so neither summand alone is closed under it. Hence $U_{\mathbb C} = 0$ or everything, i.e. $U = 0$ or all six dimensions.
>
> **What the derivation shows**
> - The decomposition of Theorem §C1a.5.5 is the finest possible over $\mathbb R$; over $\mathbb C$ only the antisymmetric part splits further, and only by complex combinations (the duality eigenvalues are $\pm i$ because $\star^2 = -1$).
> - The field law of a two-index tensor field, and the reading of its pieces (spin content, which half is $(1, 0)$), is [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]] (physics).

^der-cb-18-12

*Uses:* [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-17|Theorem §CB.8.17]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-18|Theorem §CB.8.18]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|Theorem §CB.17.5]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-11|Theorem §CB.17.11]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-6|Theorem §CB.17.6]]

## The Clifford algebra as a representation, and the bilinears

The invariance of the Dirac form under the spinor Lorentz matrices, an instance of [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-21|Theorem §CB.14.21]], in the course's form (first written in [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]]); the course's bilinears built on it are [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]] (physics), and the classification below uses it:

> [!theorem] Theorem §CB.18.13: Λ½ Is Pseudo-Unitary
> For every real $\omega_{\mu\nu}$, the Dirac-representation matrix $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]]) and $\gamma^0$ ([[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^def-cb-11-11|Def. §CB.11.11]]) satisfy
>
> $$
> \Lambda_{1/2}^\dagger\,\gamma^0 = \gamma^0\,\Lambda_{1/2}^{-1}, \qquad\text{equivalently}\qquad \Lambda_{1/2}^\dagger\,\gamma^0\,\Lambda_{1/2} = \gamma^0, \qquad \Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0 .
> $$
>
> $\gamma^0$ is a Hermitian form on $\mathbb C^4$ preserved by every $\Lambda_{1/2}$; it is indefinite, with eigenvalues $+1$, $+1$, $-1$, $-1$.
>
> *Source: the user's PHY 513 notes, Ch. 8 §8.1 (eq. (pseudounitary)), §8.7 (Derivation "Why $\psi^\dagger\psi$ fails, and how $\gamma^0$ repairs it: the lecture's route", Steps 2–3, eq. (gammaSdagger)) · PHY 513 Lecture 8, Part B ("The Dirac Conjugate Spinor") · PS §3.2, p. 43 · Yu §5.3, eqs. (5.86)–(5.89)*

^thm-cb-18-13

> [!derivation]- Derivation (the lecture's route: which generators γ⁰ commutes with)
> **1. $\gamma^0$ commutes with $S^{ij}$.** For $i \ne j$, $[\gamma^i, \gamma^j] = 2\gamma^i\gamma^j$ (distinct $\gamma$'s anticommute, [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]]), so $S^{ij} = \frac i2\gamma^i\gamma^j$. Moving $\gamma^0$ through $\gamma^i$ and then $\gamma^j$ costs two signs: $\gamma^0\gamma^i\gamma^j = (-\gamma^i\gamma^0)\gamma^j = \gamma^i\gamma^j\gamma^0$. Hence $\gamma^0S^{ij} = S^{ij}\gamma^0$.
>
> **2. $\gamma^0$ anticommutes with $S^{0i}$.** $S^{0i} = \frac i2\gamma^0\gamma^i$. Then $\gamma^0S^{0i} = \frac i2(\gamma^0)^2\gamma^i = \frac i2\gamma^i$, using $(\gamma^0)^2 = \mathbb 1$; and $S^{0i}\gamma^0 = \frac i2\gamma^0\gamma^i\gamma^0 = \frac i2\gamma^0(-\gamma^0\gamma^i) = -\frac i2\gamma^i$. Hence $\gamma^0S^{0i} = -S^{0i}\gamma^0$.
>
> **3. Combine with the Hermiticity pattern.** By [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-22|Theorem §CB.14.22]], $S^{ij\dagger} = S^{ij}$ and $S^{0i\dagger} = -S^{0i}$. Therefore $S^{ij\dagger}\gamma^0 = S^{ij}\gamma^0 = \gamma^0S^{ij}$ (step 1) and $S^{0i\dagger}\gamma^0 = -S^{0i}\gamma^0 = \gamma^0S^{0i}$ (step 2). In every case
>
> $$
> S^{\mu\nu\dagger}\,\gamma^0 = \gamma^0\,S^{\mu\nu} :
> $$
>
> the generators that fail to be Hermitian are exactly those that anticommute with $\gamma^0$, so the two signs cancel.
>
> **4. The exponent.** Let $X = \omega_{\mu\nu}S^{\mu\nu}$ (summed). Since the $\omega_{\mu\nu}$ are real, $X^\dagger = \omega_{\mu\nu}S^{\mu\nu\dagger}$, and step 3 gives $X^\dagger\gamma^0 = \gamma^0X$. By induction on $n$, $(X^\dagger)^n\gamma^0 = (X^\dagger)^{n-1}\gamma^0X = \cdots = \gamma^0X^n$.
>
> **5. The series.** $\Lambda_{1/2} = \exp(-\frac i2X)$, and the adjoint of a norm-convergent series is the series of adjoints, so $\Lambda_{1/2}^\dagger = \exp(+\frac i2X^\dagger)$. Term by term with step 4,
>
> $$
> \Lambda_{1/2}^\dagger\gamma^0 = \sum_{n=0}^\infty\frac1{n!}\Bigl(\frac i2\Bigr)^n(X^\dagger)^n\gamma^0 = \gamma^0\sum_{n=0}^\infty\frac1{n!}\Bigl(\frac i2\Bigr)^nX^n = \gamma^0\exp\Bigl(+\frac i2X\Bigr) = \gamma^0\Lambda_{1/2}^{-1} ,
> $$
>
> the last step because $\exp(\frac i2X)\exp(-\frac i2X) = \mathbb 1$ ($X$ commutes with itself).
>
> **6. The other forms.** Multiply step 5 by $\Lambda_{1/2}$ on the right: $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2} = \gamma^0$. Multiply step 5 by $\gamma^0$ on the right and use $(\gamma^0)^2 = \mathbb 1$: $\Lambda_{1/2}^\dagger = \gamma^0\Lambda_{1/2}^{-1}\gamma^0$.
>
> **7. The form is indefinite.** $\gamma^0$ is Hermitian with $(\gamma^0)^2 = \mathbb 1$, so its eigenvalues are $\pm1$; it is traceless ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-10|Theorem §CB.12.10]]), so each occurs twice. In the chiral basis $\gamma^0$ swaps the upper and lower blocks, with eigenvectors $(\xi, \xi)$ and $(\xi, -\xi)$. ⚑ By-product: $\psi^\dagger\gamma^0\psi$ can have either sign; the invariant of a Dirac spinor is not a norm → [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]] (it pairs left- with right-handed components).
>
> **What the derivation shows**
> - $\Lambda_{1/2}$ preserves the Hermitian form $\gamma^0$ as $\Lambda$ preserves $g$ ($\Lambda^{\mathsf T}g\Lambda = g$): $\gamma^0$ plays the role of the metric for the Dirac spinor slot; both forms are indefinite.
> - ⚑ By-product: the sign ambiguity $\pm\Lambda_{1/2}$ cancels in $\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2}$.
> - Used next: the Dirac conjugate (Def. §C5a.2.1, Theorem §C5a.6.1).

^der-cb-18-13

> [!derivation]- Derivation (second route: from the Hermiticity of the γ's)
> **1.** In a Hermitian basis ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-11|Def. §CB.13.11]]; e.g. the chiral one, [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-11-13|Example §CB.11.13]]), $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$; multiplying by $\gamma^0$ on the right, $\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu$.
>
> **2.** $S^{\mu\nu\dagger} = (\frac i4[\gamma^\mu, \gamma^\nu])^\dagger = -\frac i4[\gamma^{\nu\dagger}, \gamma^{\mu\dagger}] = -\frac i4\bigl(\gamma^{\nu\dagger}\gamma^{\mu\dagger} - \gamma^{\mu\dagger}\gamma^{\nu\dagger}\bigr)$ (the adjoint reverses products and conjugates $i$).
>
> **3.** Multiply on the right by $\gamma^0$ and push it left with step 1, twice in each product: $\gamma^{\nu\dagger}\gamma^{\mu\dagger}\gamma^0 = \gamma^{\nu\dagger}\gamma^0\gamma^\mu = \gamma^0\gamma^\nu\gamma^\mu$. Hence $S^{\mu\nu\dagger}\gamma^0 = -\frac i4\gamma^0(\gamma^\nu\gamma^\mu - \gamma^\mu\gamma^\nu) = \frac i4\gamma^0[\gamma^\mu, \gamma^\nu] = \gamma^0S^{\mu\nu}$, step 3 of the first route.
>
> **4.** Steps 4–6 of the first route follow unchanged.
>
> **What the derivation shows**
> - No explicit matrices and no case split between rotations and boosts: the result follows from $\gamma^{\mu\dagger} = \gamma^0\gamma^\mu\gamma^0$ alone, hence holds in every basis in which that relation holds (every unitary change of the chiral basis, [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-12|Theorem §CB.13.12]]).

^der-cb-18-13b

*Uses:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-22|Theorem §CB.14.22]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^ex-cb-11-13|Example §CB.11.13]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-12|Theorem §CB.11.12]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-19|Def. §CB.14.19]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-10|Theorem §CB.12.10]]

The sixteen products as a representation:

> [!theorem] Theorem §CB.18.14: Cl(1,3) ≅ ΛV as a Representation; the Sixteen Bilinears
> 1. $\mathrm{Spin}(1,3)_0$ acts on $\mathrm{Cl}(1,3)$ by $a \mapsto xax^{-1}$; the vector-space isomorphism $\Lambda V \cong \mathrm{Cl}(1,3)$ of [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-11|Theorem §CB.12.11]] intertwines it with $\Lambda\rho$, so $\mathrm{Cl}(1,3)_{\mathbb C} \cong \Lambda^0\oplus\Lambda^1\oplus\Lambda^2\oplus\Lambda^3\oplus\Lambda^4$ of dimensions $1 + 4 + 6 + 4 + 1$.
> 2. $\operatorname{End}(S) \cong \mathrm{Cl}(1,3)_{\mathbb C}$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-5|Theorem §CB.13.5]]) as representations, with $\operatorname{End}(S) \cong S\otimes S^\ast$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]]); through the Dirac form $S^\ast \cong \bar S$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-21|Theorem §CB.14.21]]), so $\bar\psi\Gamma\chi$ with $\Gamma$ in the $\Lambda^k$ piece transforms as a $k$-form: scalar, vector, tensor, axial vector, pseudoscalar ($\Lambda^3 \cong \Lambda^1$ and $\Lambda^4 \cong \Lambda^0$ through $\gamma^5$, up to orientation).
>
> *Source: Peskin & Schroeder, §3.4, and the user's PHY 513 notes, Ch. 8 §8.9, through [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]] and [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]] · the representation-theoretic proof written here*

^thm-cb-18-14

> [!proof]- Proof
> **1. Conjugation is the induced automorphism.** For $x \in \mathrm{Spin}(1,3)_0$, $a \mapsto xax^{-1}$ is an algebra automorphism of $\mathrm{Cl}(1,3)$ that maps $v \in V$ to $\rho(x)v \in V$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-10|Theorem §CB.14.10]], 2). By the uniqueness in [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-7|Theorem §CB.11.7]], it is the automorphism extending $v \mapsto \rho(x)v$.
>
> **2. Part 1.** The isomorphism $Q : \Lambda V \to \mathrm{Cl}(1,3)$ of [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-11|Theorem §CB.12.11]] commutes with the action of $O(V, q)$, on $\mathrm{Cl}$ by exactly these automorphisms. With $R = \rho(x)$ and step 1: $Q\bigl((\Lambda\rho(x))w\bigr) = x\,Q(w)\,x^{-1}$. $Q(\Lambda^kV)$ is the span of the $e_I$ with $|I| = k$, an invariant subspace of dimension $\binom4k$: $1, 4, 6, 4, 1$. Extending complex-linearly gives the statement for $\mathrm{Cl}(1,3)_{\mathbb C}$.
>
> **3. γ identifies the Clifford algebra with End(S).** $\gamma : \mathrm{Cl}(1,3)_{\mathbb C} \to \operatorname{End}(S)$ is an algebra homomorphism whose image contains $\mathbb 1$, $\gamma^\mu = g^{\mu\nu}\gamma(e_\nu)$ and their products, hence the sixteen matrices of [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-9|Theorem §CB.12.9]], which span all $4\times4$ matrices ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-9|Theorem §CB.12.9]]). Both spaces have dimension $16$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-6|Theorem §CB.12.6]]), so $\gamma$ is bijective, as [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-5|Theorem §CB.13.5]] predicts. It is equivariant: $\gamma(xax^{-1}) = \gamma(x)\gamma(a)\gamma(x)^{-1}$, which is the action $T \mapsto \gamma(x)T\gamma(x)^{-1}$ on $\operatorname{End}(S) = \operatorname{Hom}(S, S) \cong S\otimes S^\ast$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]]).
>
> **4. The Dirac form.** Let $h_D(\psi, \chi) = \psi^\dagger\gamma^0\chi = \bar\psi\chi$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^def-cb-13-15|Def. §CB.13.15]]). Every $\gamma^\mu$, hence every $\gamma(v) = v_\mu\gamma^\mu$ with real $v_\mu$, is self-adjoint for $h_D$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-16|Theorem §CB.13.16]], 1). By [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-21|Theorem §CB.14.21]], $h_D(\gamma(x)\psi, \gamma(x)\chi) = h_D(\psi, \chi)$ for $x \in \mathrm{Spin}(1,3)_0$ (the course's [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-13|Theorem §CB.18.13]]). Equivalently $\overline{\gamma(x)\psi} = \bar\psi\,\gamma(x)^{-1}$: the conjugate-linear bijection $\psi \mapsto \bar\psi = h_D(\psi, \cdot)$ intertwines $S$ with $S^\ast$, i.e. it is a complex-linear equivalence $\bar S \cong S^\ast$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|Def. §CB.8.6]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-7|Def. §CB.8.7]]).
>
> **5. Bilinears transform as forms.** For $a \in \mathrm{Cl}(1,3)_{\mathbb C}$ put $B_a(\psi, \chi) = \bar\psi\,\gamma(a)\,\chi$. By step 4 and step 3,
>
> $$
> B_a(\gamma(x)\psi, \gamma(x)\chi) = h_D\bigl(\psi, \gamma(x)^{-1}\gamma(a)\gamma(x)\chi\bigr) = B_{x^{-1}ax}(\psi, \chi) .
> $$
>
> So for fixed $\psi$, $\chi$ the linear functional $a \mapsto B_a(\psi, \chi)$ on $Q(\Lambda^kV_{\mathbb C})$ is transformed by precomposition with the action of $x^{-1}$, which is $\Lambda^k\rho(x)^{-1}$ by step 2: it is an element of $(\Lambda^kV_{\mathbb C})'$ with the dual representation (Def. §CB.8.6), a $k$-form. On basis elements, $B_{e_{\mu_1}\cdots e_{\mu_k}} = \bar\psi\gamma_{\mu_1}\cdots\gamma_{\mu_k}\chi$ for distinct $\mu_i$; for $k = 0, 1, 2$ these are $\bar\psi\chi$, $\bar\psi\gamma_\mu\chi$, $\bar\psi\gamma_\mu\gamma_\nu\chi = -i\bar\psi\sigma_{\mu\nu}\chi$ ($\mu \ne \nu$, since $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] = i\gamma^\mu\gamma^\nu$ there): scalar, vector, antisymmetric tensor.
>
> **6. Grades 3 and 4 through the volume element.** For $x \in \mathrm{Spin}(1,3)_0 \subset \mathrm{Cl}^0$, $x\omega x^{-1} = \omega$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-13|Theorem §CB.12.13]], 3), so right multiplication $R_\omega(a) = a\omega$ commutes with the action: $x(a\omega)x^{-1} = (xax^{-1})\omega$. It maps $e_I$ to $\pm e_{I^c}$ (each factor of $e_I$ meets its copy in $\omega$ after reordering and squares to $\pm1$; e.g. $e_0\omega = e_1e_2e_3$), so $Q(\Lambda^k) \to Q(\Lambda^{4-k})$, and it is invertible ($\omega^2 = -1$). Hence $\Lambda^3 \cong \Lambda^1$ and $\Lambda^4 \cong \Lambda^0$ as representations of $\mathrm{Spin}(1,3)_0$. Since $\omega = -i\omega_{\mathbb C}$ and $\gamma(\omega_{\mathbb C}) = -\gamma^5$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-2|Theorem §CB.18.2]]), $\gamma(\omega) = i\gamma^5$: the grade-3 and grade-4 bilinears are spanned by $\bar\psi\gamma_\mu\gamma^5\chi$ and $\bar\psi\,i\gamma^5\chi$, transforming as a vector and a scalar under $\mathrm{Spin}(1,3)_0$.
>
> **What the proof shows**
> - The course's bilinears (comparisons moved here from steps 5–6, CB ordering pass): scalar, vector, antisymmetric tensor as in [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]; the axial vector and pseudoscalar as in [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]].
> - The classification of the sixteen bilinears is the grading of the Clifford algebra, $\mathrm{Cl} \cong \Lambda^0\oplus\dots\oplus\Lambda^4$, transported to $\operatorname{End}(S)$ by $\gamma$ and paired by the invariant Dirac form.
> - ⚑ By-product ("up to orientation"): $R_\omega$ commutes with $\mathrm{Spin}(1,3)_0$ but not with orientation-reversing elements, which send $\omega$ to $-\omega$ (Theorem §CB.12.13, 1). This sign is the "pseudo" in pseudoscalar and axial vector: they differ from $\bar\psi\psi$ and $\bar\psi\gamma^\mu\psi$ under parity ([[§C9.4 Fermion Bilinears under Parity|§C9.4]]).

^pf-cb-18-14

*Uses:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-10|Theorem §CB.14.10]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-21|Theorem §CB.14.21]], [[§CB.11 Clifford Algebras꞉ Definition, Universal Property and Clifford Modules#^thm-cb-11-7|Theorem §CB.11.7]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-6|Theorem §CB.12.6]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-11|Theorem §CB.12.11]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-13|Theorem §CB.12.13]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-5|Theorem §CB.13.5]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|Def. §CB.8.6]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-7|Def. §CB.8.7]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-2|Theorem §CB.18.2]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-9|Theorem §CB.12.9]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-16|Theorem §CB.13.16]]

## The TA's theorem for the Lorentz group

> [!theorem] Theorem §CB.18.15: Every Tensorial (j₊, j₋) Lies in a Tensor Power of the Vector
> If $k + l \in \mathbb Z$, then $(k, l)$ is equivalent to a subrepresentation of $V_{\mathbb C}^{\otimes N}$ with $N = 2\max(k, l)$, $V_{\mathbb C} = (\frac12, \frac12)$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]]).
>
> *Source: written here (the same count by Clebsch–Gordan on each copy: [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-11|Theorem §CB.17.11]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-14|Theorem §CB.10.14]])*

^thm-cb-18-15

> [!proof]- Proof
> Write representations of $\mathrm{Spin}(1,3)_0$ through $\lambda$ (Theorem §CB.18.3), with $\theta(\lambda) = (\lambda^\dagger)^{-1}$.
>
> **1. Spin k inside a tensor power of ℂ².** Let $A$ be $\lambda$ or $\theta(\lambda)$ acting on $\mathbb C^2$, and $M = 2k + 2m$ with $m \in \mathbb Z_{\ge0}$. $(\mathbb C^2)^{\otimes M} = (\mathbb C^2)^{\otimes2k}\otimes(\mathbb C^2\otimes\mathbb C^2)^{\otimes m}$ contains the invariant subspace $\operatorname{Sym}^{2k}\mathbb C^2\otimes(\Lambda^2\mathbb C^2)^{\otimes m}$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], 1–2; a tensor product of invariant subspaces is invariant). $\Lambda^2\mathbb C^2$ is trivial for $\det A = 1$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]], 1), so this subspace is $\operatorname{Sym}^{2k}(A)$, spin $k$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-12|Theorem §CB.10.12]]).
>
> **2. Tensor powers of the vector.** $V_{\mathbb C} \cong \lambda\otimes\theta(\lambda) = D^{(\frac12, \frac12)}$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]]), so $V_{\mathbb C}^{\otimes N} \cong (\lambda\otimes\theta(\lambda))^{\otimes N} \cong \lambda^{\otimes N}\otimes\theta(\lambda)^{\otimes N}$, the second equivalence being the permutation of tensor factors that collects the $\lambda$-slots first (a permutation of factors commutes with the diagonal action).
>
> **3. The parities match.** Let $N = 2\max(k, l)$, say $\max = k$ (the other case is symmetric). Then $N - 2k = 0$ and $N - 2l = 2(k - l)$ with $k - l = (k + l) - 2l \in \mathbb Z$ (since $k + l \in \mathbb Z$ and $2l \in \mathbb Z$) and $k - l \ge 0$.
>
> **4. Conclusion.** By step 1 with $A = \lambda$, $M = N$, $\lambda^{\otimes N} \supset \operatorname{Sym}^{2k}(\lambda)$; with $A = \theta(\lambda)$, $\theta(\lambda)^{\otimes N} \supset \operatorname{Sym}^{2l}(\theta(\lambda))\otimes(\text{trivial})$. Their tensor product is $D^{(k, l)}$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]) inside $V_{\mathbb C}^{\otimes N}$ by step 2.
>
> **What the proof shows**
> - Each vector index is one undotted plus one dotted spinor slot; symmetrizing $2k$ undotted and $2l$ dotted slots and contracting the rest in pairs with $\varepsilon$ gives $(k, l)$. The condition $k + l \in \mathbb Z$ is exactly that the leftover slots of each kind pair up.

^pf-cb-18-15

*Uses:* [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-13|Theorem §CB.8.13]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-15|Theorem §CB.8.15]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-12|Theorem §CB.10.12]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-10|Theorem §CB.18.10]]

> [!theorem] Theorem §CB.18.16: The TA's Theorem for the Lorentz Group
> Every spinorial irreducible representation $(j_+, j_-)$ ($j_+ + j_- \in \frac12 + \mathbb Z$, [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|Theorem §CB.17.15]]) is equivalent to a subrepresentation of $S\otimes T$, $S = (\frac12, 0)\oplus(0, \frac12)$ the Dirac module and $T$ tensorial: $(j_+, j_-) \subset (\frac12, 0)\otimes(j_+ - \frac12, j_-)$ if $j_+ \ge \frac12$, and $(j_+, j_-) \subset (0, \frac12)\otimes(j_+, j_- - \frac12)$ otherwise; and $T$ lies in a tensor power of $V_{\mathbb C}$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-15|Theorem §CB.18.15]]). With complete reducibility ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-1|Theorem §CB.17.1]]) every finite-dimensional spinorial representation lies in $S\otimes T$ with $T$ a direct sum of subrepresentations of tensor powers of $V_{\mathbb C}$, with $T$ inside a single tensor power when the representation is irreducible.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · the decomposition of products: [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-11|Theorem §CB.17.11]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-14|Theorem §CB.10.14]] · written here · this is part 3 of the TA's theorem in general, [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-17|Theorem §CB.18.17]], for $\mathbb R^{1,3}$ (pointer moved here from the statement, CB ordering pass)*

^thm-cb-18-16

> [!proof]- Proof
> Representations are written through $\lambda$, $\theta(\lambda) = (\lambda^\dagger)^{-1}$ (Theorem §CB.18.3); $D^{(j_+, j_-)}(\lambda) = \operatorname{Sym}^{2j_+}(\lambda)\otimes\operatorname{Sym}^{2j_-}(\theta(\lambda))$ ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]]).
>
> **1. Case j₊ ≥ ½.** $D^{(\frac12, 0)}\otimes D^{(j_+ - \frac12, j_-)} = \lambda\otimes\operatorname{Sym}^{2j_+ - 1}(\lambda)\otimes\operatorname{Sym}^{2j_-}(\theta(\lambda))$. The first two factors are $V_{1/2}\otimes V_{j_+ - 1/2}$ for $\lambda$, which contains $V_{j_+}$ (the top term of the Clebsch–Gordan series, Theorem §CB.10.14, as $j_+ = \frac12 + (j_+ - \frac12)$). Tensoring with $\operatorname{Sym}^{2j_-}(\theta(\lambda))$: $D^{(\frac12, 0)}\otimes D^{(j_+ - \frac12, j_-)} \supset D^{(j_+, j_-)}$.
>
> **2. Case j₊ = 0.** Then $j_- \in \frac12 + \mathbb Z$, so $j_- \ge \frac12$, and the same argument on the second factor gives $D^{(0, \frac12)}\otimes D^{(0, j_- - \frac12)} \supset D^{(0, j_-)}$.
>
> **3. The second factor is tensorial.** Its labels add to $j_+ + j_- - \frac12 \in \mathbb Z$, so it is tensorial ([[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|Theorem §CB.17.15]]), and by [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-15|Theorem §CB.18.15]] it is a subrepresentation of $V_{\mathbb C}^{\otimes N}$ for some $N$. $D^{(\frac12, 0)}$ and $D^{(0, \frac12)}$ are $S^-$ and $S^+$, subrepresentations of the Dirac module $S$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]]). Tensoring inclusions gives $(j_+, j_-) \subset S\otimes V_{\mathbb C}^{\otimes N}$.
>
> **4. Reducible representations.** A finite-dimensional spinorial $W$ is a direct sum of irreducible $W_i$ (Theorem §CB.17.1); $-1$ acts as $-\mathbb 1$ on $W$, so on each $W_i$, and each $W_i \cong D^{(j_+, j_-)}$ with $j_+ + j_- \in \frac12 + \mathbb Z$ (Theorems §CB.17.7, §CB.17.15). By step 3, $W_i \subset S\otimes T_i$ with $T_i \subset V_{\mathbb C}^{\otimes N_i}$, so $W \subset \bigoplus_i(S\otimes T_i) = S\otimes\bigl(\bigoplus_iT_i\bigr)$, and $\bigoplus_iT_i$ is tensorial.
>
> **What the proof shows**
> - A spinorial field of any spin is a Dirac spinor with tensor indices, projected: one spinor slot carries the half-integer part, the remaining slots pair into vector indices. The Rarita–Schwinger field $\psi_\mu$ is the first case beyond the Dirac field, $(1, \frac12)\oplus(\frac12, 1) \subset S\otimes V_{\mathbb C}$.
> - Step 4 gives a direct sum of tensor powers; putting all $T_i$ into one tensor power needs an extra multiplicity count (the $T_i$ can be chosen of one parity class, using also $(\frac12, 0)\otimes(j_+ + \frac12, j_-) \supset (j_+, j_-)$), not carried out here.

^pf-cb-18-16

*Uses:* [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-14|Theorem §CB.10.14]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-1|Theorem §CB.17.1]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-7|Theorem §CB.17.7]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-15|Theorem §CB.17.15]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-3|Theorem §CB.18.3]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-15|Theorem §CB.18.15]]

## The TA's theorem in general

The statement for every nondegenerate $(V, q)$ of dimension $n \ge 3$, first stated in [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.14]] and moved here in the CB ordering pass, because its proof uses its two cases proved in CB, $n = 3$ ([[§CB.15 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-15-6|Theorem §CB.15.6]]) and $\mathbb R^{1,3}$ (Theorems §CB.18.15–§CB.18.16 above):

> [!theorem] Theorem §CB.18.17: The TA's Theorem — Clifford Modules Restricted to Spin Are Exactly the Spinor Representations, and Every Spinorial Representation Lies in Spinor ⊗ Tensor
> Let $(V, q)$ be nondegenerate real with $n = \dim V \ge 3$, and $S$ an irreducible complex Clifford module.
> 1. **Restriction.** The spinor representation $S|_{\mathrm{Spin}(V)_0}$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-24|Def. §CB.14.24]]) is spinorial ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-23|Def. §CB.14.23]]): $-1 \in \mathrm{Spin}(V)_0$ acts as $-\mathbb 1$, so it is not a representation of $SO(V)_0$. For $n$ odd it is irreducible of dimension $2^{(n-1)/2}$; for $n$ even, $S = S^+\oplus S^-$ with $S^\pm$ irreducible, inequivalent, of dimension $2^{n/2-1}$, and $\gamma(v)$ maps $S^\pm$ to $S^\mp$.
> 2. **Exactly the spinor representations.** Up to equivalence, the irreducible representations of $\mathrm{Spin}(V)_0$ obtained by restricting Clifford modules — that is, the irreducible representations of $\mathfrak{spin}(V)$ that extend to representations of the algebra $\mathrm{Cl}^0$ — are exactly $S$ ($n$ odd), resp. $S^+$ and $S^-$ ($n$ even); every finite-dimensional Clifford module restricts to a direct sum of copies of them.
> 3. **Spinor ⊗ tensor.** Every finite-dimensional spinorial representation $W$ of $\mathrm{Spin}(V)_0$ is equivalent to a subrepresentation of $S\otimes T$ for a tensorial representation $T$ ([[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-1|Def. §CB.8.1]]); one may take $T = S'\otimes W$ ($S'$ the dual, [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|Def. §CB.8.6]]). Moreover $T$ can be taken inside a direct sum of tensor powers $(V_{\mathbb C})^{\otimes k}$ of the complexified vector representation $x \mapsto \rho(x)$: proved in CB for $n = 3$ ([[§CB.15 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-15-6|Theorem §CB.15.6]]) and $\mathbb R^{1,3}$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-16|Theorem §CB.18.16]]); for general $n$ by highest-weight theory (reference in the proof).
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · J. Figueroa-O'Farrill, Spin Geometry, Lecture 3 (introduction: spinorial representations are those "not contained in any tensor product of the fundamental (vector) representation"; Def. 3.7 and §3.3) · H. Georgi, Lie Algebras in Particle Physics, 2nd ed., §8.12, Ch. 21–23 (highest weights, for part 3 in general) · the cases proved in CB: $n = 3$, Theorem §CB.15.6; $\mathbb R^{1,3}$, Theorem §CB.18.16*

^thm-cb-18-17

> [!proof]- Proof
> *Source: the statement is the PHY 513 TA's (oral remark, Oct 2026). Parts 1–2: J. Figueroa-O'Farrill, Spin Geometry, Def. 3.7 ("a spinor representation of $\mathrm{Spin}(V)$ is the restriction of an irreducible representation of $C\ell(V)^0$") and §3.3 (for $d$ even the eigenspaces of $\omega$ in the pinor representation are the spinor representations; for $d$ odd both pinor representations restrict to the spinor one), assembled here from Theorems §CB.13.8, §CB.13.20, §CB.14.15, §CB.14.20. Part 3, first claim: written here (the canonical invariant of $S\otimes S'$). Part 3, tensor powers for general $n$: not proved in CB; see Step 8.*
>
> **Step 1** ($-1$ acts as $-\mathbb 1$). $n \ge 3$, so $-1 \in \mathrm{Spin}(V)_0$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-15|Theorem §CB.14.15]]). $\gamma$ is a unital algebra homomorphism, so $\gamma(-1) = -\gamma(1) = -\mathbb 1$: the restriction is spinorial ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-23|Def. §CB.14.23]]). It is not of the form $D\circ\rho$, since that would give $D(\rho(-1)) = D(\mathbb 1) = \mathbb 1$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-15|Theorem §CB.10.15]]).
>
> **Step 2** (same invariant subspaces). For a Clifford module, a subspace is invariant under $\mathrm{Spin}(V)_0$ iff under $\mathrm{Cl}^0$ ([[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-20|Theorem §CB.14.20]]).
>
> **Step 3** (same intertwiners). Let $\gamma_1$, $\gamma_2$ be Clifford modules on $W_1$, $W_2$ and $A : W_1 \to W_2$ linear. If $A\gamma_1(x) = \gamma_2(x)A$ for all $x \in \mathrm{Cl}^0$, this holds in particular on $\mathrm{Spin}(V)_0 \subset \mathrm{Cl}^0$. Conversely, suppose it holds on $\mathrm{Spin}(V)_0$. For $X \in \mathfrak{spin}(V)$, $e^{sX} \in \mathrm{Spin}(V)_0$ (Step 4 of the proof of [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-14|Theorem §CB.14.14]]; the path $s \mapsto e^{sX}$ starts at $1$), and $\gamma_i(e^{sX}) = e^{s\gamma_i(X)}$ ($\gamma_i$ is linear and multiplicative, hence maps the exponential series termwise, and continuous). Differentiating $Ae^{s\gamma_1(X)} = e^{s\gamma_2(X)}A$ at $s = 0$ gives $A\gamma_1(X) = \gamma_2(X)A$; then $A$ intertwines all products of such $X$ and $1$, which span $\mathrm{Cl}^0$ (Theorem §CB.14.20). So equivalences of the restrictions to $\mathrm{Spin}(V)_0$ are the same as equivalences of $\mathrm{Cl}^0$-modules.
>
> **Step 4** (part 1, $n$ odd). $S$ is irreducible as a $\mathrm{Cl}^0$-module ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-20|Theorem §CB.13.20]], 2), so irreducible under $\mathrm{Spin}(V)_0$ by Step 2; $\dim S = 2^{(n-1)/2}$ ([[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-8|Theorem §CB.13.8]], 2).
>
> **Step 5** (part 1, $n$ even). $S = S^+\oplus S^-$ with $S^\pm$ irreducible and inequivalent $\mathrm{Cl}^0$-modules of dimension $2^{n/2-1}$, and $\gamma(v)S^\pm \subset S^\mp$ (Theorem §CB.13.20, 1). By Steps 2–3 the same holds for $\mathrm{Spin}(V)_0$.
>
> **Step 6** (part 2). (a) A finite-dimensional Clifford module $W$ is a direct sum of irreducible Clifford modules (Theorem §CB.13.8, 3), each equivalent, by an intertwiner that in particular intertwines $\mathrm{Cl}^0$, to a fixed $S$; for $n$ odd both classes of $S$ restrict to the same $\mathrm{Cl}^0$-module (Theorem §CB.13.20, 2). So $W|_{\mathrm{Spin}(V)_0}$ is a direct sum of copies of $S$ ($n$ odd), resp. of $S^+$ and $S^-$ ($n$ even). (b) An irreducible representation of $\mathrm{Spin}(V)_0$ that is the restriction of a representation of the algebra $\mathrm{Cl}^0$ (for instance an irreducible $\mathrm{Spin}(V)_0$-invariant subspace $U$ of a Clifford module: $U$ is $\mathrm{Cl}^0$-invariant and $\mathrm{Cl}^0$-irreducible by Step 2) is an irreducible $\mathrm{Cl}^0$-module, hence equivalent to $S$, resp. $S^+$ or $S^-$ (Theorem §CB.13.20, 3), as a $\mathrm{Cl}^0$-module and so (Step 3) as a representation of $\mathrm{Spin}(V)_0$. By Steps 4–5 all of these occur.
>
> **Step 7** (part 3, first claim). Let $D_W$ be a spinorial representation on $W$, $D_S(x) = \gamma(x)$ on $S$, and $D_S^\ast$ the dual representation on $S'$, $(D_S^\ast(x)\varphi)(s) = \varphi(D_S(x)^{-1}s)$. Put $T = S'\otimes W$. Then $D_T(-1) = D_S^\ast(-1)\otimes D_W(-1) = (-\mathbb 1)\otimes(-\mathbb 1) = \mathbb 1$ (the dual of $-\mathbb 1$ is $-\mathbb 1$): $T$ is tensorial. Let $s_a$ be a basis of $S$ and $s^a$ the dual basis, and define
>
> $$
> \iota : W \to S\otimes T = S\otimes S'\otimes W, \qquad \iota(w) = \sum_as_a\otimes s^a\otimes w .
> $$
>
> With $M = D_S(x)$, $Ms_a = \sum_cM_{ca}s_c$ and $D_S^\ast(x)s^a = \sum_b(M^{-1})_{ab}s^b$ (evaluate on $s_b$: $s^a(M^{-1}s_b) = (M^{-1})_{ab}$), so
>
> $$
> \sum_aD_S(x)s_a\otimes D_S^\ast(x)s^a = \sum_{a,b,c}M_{ca}(M^{-1})_{ab}\,s_c\otimes s^b = \sum_{b,c}\delta_{cb}\,s_c\otimes s^b = \sum_as_a\otimes s^a :
> $$
>
> the element $\sum_as_a\otimes s^a$ is invariant (it corresponds to the identity intertwiner under [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]]). Hence $\iota(D_W(x)w) = (D_S\otimes D_S^\ast\otimes D_W)(x)\,\iota(w)$: $\iota$ is an intertwiner ([[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-2|Def. §CB.7.2]]). It is injective: the contraction $s\otimes\varphi\otimes w \mapsto \varphi(s)w$ sends $\iota(w)$ to $\sum_as^a(s_a)w = (\dim S)\,w$. So $W$ is equivalent to the subrepresentation $\iota(W)$ of $S\otimes T$.
>
> **Step 8** (part 3, tensor powers). $T$ is tensorial, hence $T = D\circ\rho$ for a representation $D$ of $SO(V)_0$ ([[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-15|Theorem §CB.10.15]], with the covering of Theorem §CB.14.15). It remains to place representations of $SO(V)_0$ inside sums of tensor powers of $V_{\mathbb C}$. For $n = 3$ this is [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-16|Theorem §CB.10.16]] (every representation of $SO(3)$ lies in a sum of tensor powers of $\mathbb C^3$), and [[§CB.15 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-15-6|Theorem §CB.15.6]] gives the sharper $V_j \subset V_{1/2}\otimes V_{j-1/2}$; for $\mathbb R^{1,3}$ it is [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-15|Theorem §CB.18.15]] with [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-16|Theorem §CB.18.16]]. For general $n$ it is **not proved in CB**. It follows from highest-weight theory: the irreducible representation of highest weight $\mu = \sum_j\ell_j\mu_j$ lies in the tensor product of $\ell_j$ copies of each fundamental representation (H. Georgi, Lie Algebras in Particle Physics, 2nd ed., §8.12, eq. (8.75)); for $\mathfrak{so}(2n+1)$ and $\mathfrak{so}(2n+2)$ the fundamental weights are listed in Georgi eqs. (21.9) and (22.4), the last one (resp. two) being the spinor representations, the others having the highest weights $e_1 + \cdots + e_j$ of the antisymmetric tensors $\Lambda^jV_{\mathbb C} \subset V_{\mathbb C}^{\otimes j}$; and a product of two spinor representations is a sum of antisymmetric tensors (Georgi, §23.3 and the table of §23.4). Since $-1$ acts as $-\mathbb 1$ on each spinor factor and trivially on the others, it acts on that tensor product, hence on the irreducible representation inside it, as $(-1)^{\ell}$ with $\ell$ the number of spinor factors; a tensorial irreducible representation therefore has $\ell$ even and lies in a product of antisymmetric tensors and pairs of spinors, hence in a sum of tensor powers of $V_{\mathbb C}$.
>
> **What the proof shows.**
> - The three faces of spinors in the course are one object: a Clifford module (C5a.1), restricted to $\mathrm{Spin}$, is irreducible or splits into the Weyl halves (C5a.5), and $-1$ acts as $-1$, which is the two-valuedness on $SO$ (C3.3, C5a.4).
> - ⚑ By-product (Step 7): "spinor ⊗ tensor" needs no classification at all — any spinorial $W$ sits in $S\otimes(S'\otimes W)$ through the invariant $\sum_as_a\otimes s^a$; the content of the TA's remark is the further statement (Step 8) that the tensorial factor is built from vectors, which is where highest weights (or, for $n = 3$ and $\mathbb R^{1,3}$, Clebsch–Gordan) enter.
> - Step 3 is why the course may work with the generators $S^{\mu\nu}$ instead of the group: on a Clifford module, invariance and equivalence under $\mathrm{Spin}(V)_0$, under $\mathfrak{spin}(V)$ and under $\mathrm{Cl}^0$ are the same.

^pf-cb-18-17

*Uses:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-15|Theorem §CB.14.15]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-14|Theorem §CB.14.14]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-20|Theorem §CB.14.20]], [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-23|Def. §CB.14.23]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-8|Theorem §CB.13.8]], [[§CB.13 Complex Clifford Algebras and Clifford Modules#^thm-cb-13-20|Theorem §CB.13.20]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-15|Theorem §CB.10.15]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-16|Theorem §CB.10.16]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-8-6|Def. §CB.8.6]], [[§CB.8 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-8-9|Theorem §CB.8.9]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-7-2|Def. §CB.7.2]], [[§CB.15 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-15-6|Theorem §CB.15.6]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-15|Theorem §CB.18.15]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-16|Theorem §CB.18.16]]

> [!remark] Remark: What the TA's theorem explains
> The course meets spinors three times: as the space on which the Dirac matrices act (C5a.1), as the representation $(\frac12, 0)\oplus(0, \frac12)$ of the Lorentz algebra (C5a.3), and as the two-valued representations of $SO^+(1,3)$ (C3.3, C5a.4). Theorem §CB.18.17 says these are one object: the Clifford module *is* a representation of the group $\mathrm{Spin}$, generated by $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Theorem §CB.14.14), it is two-valued on $SO$ because $-1 \in \mathrm{Spin}$ acts as $-1$ (Theorem §CB.14.15), and every other two-valued representation is a spinor index together with tensor indices — Rarita–Schwinger's $\psi_\mu$ being the first example beyond Dirac.

^rem-cb-18-2

> [!remark]- ★ Remark: Majorana spinors as a real structure (forward pointer)
> $\mathrm{Cl}(1,3) \cong M_2(\mathbb H)$ has no real four-dimensional module ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^rem-cb-12-1|§CB.12, ★ Remark: The real classification]]), but the Dirac module carries a conjugate-linear map $\mathcal C$ commuting with $\mathrm{Spin}(1,3)_0$ and with $\mathcal C^2 = \mathbb 1$ (charge conjugation); its fixed vectors are the Majorana spinors, a real form of $S$ for the group, exchanging $S^+$ with $S^-$ ([[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-6|Theorem §CB.18.6]]). To be stated and proved with the Majorana field (QFT C9, planned); [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-6|§C5a.5, ★ Remark: The Majorana basis]].

^rem-cb-18-1

> [!remark]- Connections
> - This section is the TA's picture for the course's spinors in one place: the Dirac module is a Clifford module (C5a.1), restricted to the spin group it is $(\frac12, 0)\oplus(0, \frac12)$ (C5a.3), $\gamma^5$ is the volume element (C5a.5), and vectors and two-forms are bispinors (C3.3, C3.4).
> - Theorem §CB.18.16 is why higher-spin fermion fields (Rarita–Schwinger $\psi_\mu$, a spinor with a vector index) are built as spinor ⊗ tensor and then projected.
> - **Used in**: Definition §CB.18.1 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]]); Theorem §CB.18.2 — [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded), [[§C5a.11 Gamma-Matrix Technology|§C5a.11]] (embedded); Theorems §CB.18.2–§CB.18.6 — [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§C9.4 Fermion Bilinears under Parity|§C9.4]]; Theorem §CB.18.3 — [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded); Theorem §CB.18.4 — [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded; cited in [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]), [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] (embedded; cited in [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]]), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded), [[§C5a.10 Normalization, Spin Sums and Helicity|§C5a.10]] (embedded), [[§C9.4 Fermion Bilinears under Parity|§C9.4]] (embedded; cited in [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-2|§C9.4, Caution: Slide 19's γ⁵]]); Theorem §CB.18.5 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorem §CB.18.7 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (cited in [[§C3.3 How Fields Transform under the Lorentz Group#^rem-c3-3-5|§C3.3, Remark: Invariant Lagrangians are (0, 0) pieces]]), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (cited in [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-3|§C5a.3, Remark: What the calculations use]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded; cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-1|Example §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]]), [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] (embedded; cited in [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]]), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^rem-c5a-7-1|§C5a.7, Remark: What covariance shows and what it does not]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-1|Theorem §C5a.7.1]]), [[§C5a.10 Normalization, Spin Sums and Helicity|§C5a.10]] (embedded; cited in [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-9|Theorem §C5a.10.9]]), [[§C9.4 Fermion Bilinears under Parity|§C9.4]] (embedded; cited in [[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-1|§C9.4, Remark: Why bilinears]]), [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation|§C5a.0]] (cited in [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-2|§C5a.0, Remark: What the Clifford relation induces]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-3|§C5a.0, Remark: Four jobs of the γ's]]), [[§C13.2★ The Dirac Equation|QM §C13.2★]] (cited in [[§C13.2★ The Dirac Equation#^rem-c13-2-4|QM §C13.2, Remark: Lorentz covariance and the rapidity]]); Theorem §CB.18.8 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (embedded); Theorem §CB.18.9 — [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-8|Theorem §CB.18.8]], [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]]; Theorem §CB.18.10 — [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-5|Theorem §C5a.5.5]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]], [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (embedded); Theorem §CB.18.11 — [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]], [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (embedded); Theorem §CB.18.13 — [[§C5a.2 The Dirac Form|§C5a.2]] (cited in [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Dirac Form#^rem-c5a-2-1|§C5a.2, Remark: γ⁰ in two roles]]), [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]] (embedded; cited in [[§C5a.3 The Lorentz Action on Spinor Space#^rem-c5a-3-2|§C5a.3, Remark: Spinor boosts are not unitary]]), [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] (embedded; cited in [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]), [[§C5a.7 The Dirac Equation and Its Lagrangian|§C5a.7]] (embedded; cited in [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]]), [[§C5a.9 Plane-Wave Solutions|§C5a.9]] (embedded; cited in [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]], [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]]), [[§C5a.10 Normalization, Spin Sums and Helicity|§C5a.10]] (embedded; cited in [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-9|Theorem §C5a.10.9]]), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (cited in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^rem-c5a-4-1|§C5a.4, Remark: One transformation, two matrices]]), [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]] (cited in [[§C5a.5 Chirality and Weyl Spinors#^rem-c5a-5-4|§C5a.5, Remark: What each Dirac index labels]]); Theorem §CB.18.14 — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-3|Theorem §C5a.6.3]], [[§C5a.11 Gamma-Matrix Technology#^rem-c5a-11-3|§C5a.11, ★ Remark: The simplest Fierz identity]], [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] (embedded); Theorem §CB.18.16 — [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-10|Theorem §CB.17.10]], [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-2|Def. §C3.3.2]]; Theorem §CB.18.12 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded; cited in [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]]), [[§C1a.5 Vectors, Tensors and Index Notation|§C1a.5]] (cited in [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]]), [[§C5a.6 The Dirac Conjugate and the Bilinears|§C5a.6]] (embedded); Theorem §CB.18.11 — [[§C3.3 How Fields Transform under the Lorentz Group|§C3.3]] (embedded); Theorem §CB.18.17 — [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-5|§C5a.0, Remark: The structure of spinor space, layer by layer]].
