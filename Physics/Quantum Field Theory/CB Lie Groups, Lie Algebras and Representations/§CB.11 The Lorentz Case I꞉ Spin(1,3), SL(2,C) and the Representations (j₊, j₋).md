---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.11
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2 · PHY 513 Lecture 7 · PHY 513, Problem Set 5, Problem 1 (as the user wrote it) · Yu Zhao-Huan, 量子场论讲义, Exercise 3.7 · Peskin & Schroeder, §3.1–§3.2 · P. Woit, Quantum Theory, Groups and Representations, §6.2, Ch. 40 (§40.4 "Spin and the Lorentz group"), §41.1 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · J. Figueroa-O'Farrill, Spin Geometry (to be checked) · the rest written here.*

What is the spin group of Minkowski space, and what are its finite-dimensional representations? The course reaches $SL(2, \mathbb C)$ through Hermitian $2\times2$ matrices ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) and the representations $(j_+, j_-)$ through the complexified algebra ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]). This section gives the Clifford route: $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, so $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ with $\rho$ the course's covering map; then it identifies the finite-dimensional representations of $SL(2, \mathbb C)$ with pairs of $\mathfrak{sl}(2, \mathbb C)$-representations and the $(j_+, j_-)$, and decides which of them descend to $SO^+(1,3)$. It is the four-dimensional sequel of [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.10]], using [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification|§CB.2]] (real forms, $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$) and [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.9]].

Throughout, $V = \mathbb R^{1,3}$ with $q(x) = g(x, x)$, $g = \operatorname{diag}(+,-,-,-)$, and $e_0, \dots, e_3$ the standard basis ($q(e_0) = 1$, $q(e_i) = -1$).

## The even Clifford algebra of Minkowski space

> [!theorem] Theorem §CB.11.1: Cl⁰(1,3) ≅ Cl(3,0) ≅ M₂(ℂ)
> The elements $f_i = e_ie_0$ ($i = 1, 2, 3$) of $\mathrm{Cl}^0(1,3)$ satisfy $f_i^2 = +1$ and $f_if_j = -f_jf_i$ ($i \ne j$), and $e_i \mapsto f_i$ extends to an isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]] with $\epsilon = 1$). Composed with [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-1|Theorem §CB.10.1]]: $\mathrm{Cl}^0(1,3) \cong M_2(\mathbb C)$, $f_i \mapsto \sigma^i$, and $\omega = e_0e_1e_2e_3 = f_1f_2f_3 \mapsto i\mathbb 1$. Under it the map $x \mapsto xe_0$, $V \to \mathrm{Cl}^0$, sends $x = x^\mu e_\mu$ to the Hermitian matrix $x^0\mathbb 1 + x^i\sigma^i$.
>
> *Source (planned): written here · Woit, §40.4 (to be checked)*

^thm-cb-11-1

> [!proof]- Proof (to be filled)
> *To be filled ($f_i^2 = e_ie_0e_ie_0 = -e_i^2e_0^2 = -(-1)(1) = 1$; $f_1f_2f_3 = e_1e_0e_2e_0e_3e_0 = e_0e_1e_2e_3$ by reordering; Theorem §CB.7.20).*

^pf-cb-11-1

## Spin(1,3) and SL(2,ℂ)

> [!theorem] Theorem §CB.11.2: Spin(1,3)₀ Is SL(2,ℂ), and ρ Is the Course's Covering Map
> 1. Under [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-1|Theorem §CB.11.1]], $\mathrm{Spin}(1,3)_0$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-6|Def. §CB.9.6]]) maps isomorphically onto $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]).
> 2. With $\tilde x = x^0\mathbb 1 + x^i\sigma^i$ (Theorem §CB.11.1), $\rho(\lambda)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]]) acts by $\tilde x \mapsto \lambda\tilde x\lambda^\dagger$: it is the covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]] (up to the sign conventions of [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]), with kernel $\{\pm\mathbb 1\}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-12|Theorem §CB.9.12]]).
> 3. $\mathrm{Spin}(1,3)$ has two components, $\mathrm{Spin}(1,3)_0$ and $e_0e_1\,\mathrm{Spin}(1,3)_0$; $\rho$ maps them onto $SO^+(1,3)$ and onto the component of $SO(1,3)$ containing $\mathcal P\mathcal T$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]]).
>
> *Source (planned): Woit, §40.4 · Figueroa-O'Farrill, Spin Geometry (to be checked) · written here*

^thm-cb-11-2

> [!proof]- Proof (to be filled)
> *To be filled (part 2: $\rho(\lambda)x\,e_0 = \lambda x\lambda^{-1}e_0 = \lambda(xe_0)(e_0^{-1}\lambda^{-1}e_0)$, and conjugation by $e_0$ acts on $\mathrm{Cl}^0 \cong M_2(\mathbb C)$ as $\sigma^i \mapsto -\sigma^i$, $i\mathbb 1 \mapsto -i\mathbb 1$, i.e. $A \mapsto \varepsilon\bar A\varepsilon^{-1}$, which is $(A^\dagger)^{-1}$ on $SL(2, \mathbb C)$, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-15|Theorem §CB.4.15]]; part 1 from part 2 and the course's Theorems §C5a.4.4–§C5a.4.7).*

^pf-cb-11-2

The course's route — four-vectors as Hermitian matrices, $SL(2, \mathbb C)$ connected and simply connected, the double cover — proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (both routes are kept):

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7]]

> [!theorem] Theorem §CB.11.3: The Three Lie Algebras Agree
> Under Theorem §CB.11.1, $\mathfrak{spin}(1,3)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]]) is $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]]): $\frac12e_ie_j = -\frac12f_if_j \mapsto -\frac i2\varepsilon_{ijk}\sigma^k$ (rotations) and $\frac12e_ie_0 \mapsto \frac12\sigma^i$ (boosts); and $\rho_\ast$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]]) is the isomorphism $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]].
>
> *Source (planned): written here*

^thm-cb-11-3

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-11-3

## The finite-dimensional representations of SL(2,ℂ)

> [!theorem] Theorem §CB.11.4: Representations of SL(2,ℂ) Are Pairs of 𝔰𝔩(2,ℂ)-Representations
> For finite-dimensional representations on complex spaces, the following correspond bijectively, preserving invariant subspaces, irreducibility and intertwiners: continuous representations of $SL(2, \mathbb C)$; representations of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-24|Theorem §CB.1.24]], $SL(2, \mathbb C)$ being simply connected, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]); commuting pairs $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-19|Theorem §CB.2.19]]); complex-linear representations of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]]). All of them are completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]).
>
> *Source (planned): written here*

^thm-cb-11-4

> [!proof]- Proof (to be filled)
> *To be filled (assembly of the cited theorems).*

^pf-cb-11-4

The course's representations $(j_+, j_-)$ and their irreducibility, in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]]:

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1]]

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1]]

> [!theorem] Theorem §CB.11.5: The Irreducible Representations of SL(2,ℂ)
> For $j_+, j_- \in \frac12\mathbb Z_{\ge0}$,
>
> $$
> D^{(j_+, j_-)}(\lambda) = \operatorname{Sym}^{2j_+}(\lambda)\otimes\operatorname{Sym}^{2j_-}\bigl((\lambda^\dagger)^{-1}\bigr) \quad\text{on}\quad \operatorname{Sym}^{2j_+}\mathbb C^2\otimes\operatorname{Sym}^{2j_-}\mathbb C^2
> $$
>
> ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]]; $(\lambda^\dagger)^{-1} \cong \bar\lambda$ by [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-16|Theorem §CB.4.16]]) is an irreducible representation of $SL(2, \mathbb C)$ of dimension $(2j_+ + 1)(2j_- + 1)$, whose generators are those of $(j_+, j_-)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]; which factor carries $\mathbf J_+$ is fixed by [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]]). Every finite-dimensional irreducible continuous representation of $SL(2, \mathbb C)$ is equivalent to exactly one $D^{(j_+, j_-)}$.
>
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.4.3, Ch. 8 §8.2 · written here (from Theorems §CB.11.4, §CB.4.5, §CB.6.3)*

^thm-cb-11-5

> [!proof]- Proof (to be filled)
> *To be filled.*

^pf-cb-11-5

> [!theorem] Theorem §CB.11.6: Which (j₊, j₋) Descend to SO⁺(1,3)
> $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2(j_+ + j_-)}\mathbb 1$. Hence $D^{(j_+, j_-)}$ is tensorial ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]]), i.e. a representation of $SO^+(1,3)$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]), iff $j_+ + j_- \in \mathbb Z$, and spinorial iff $j_+ + j_- \in \frac12 + \mathbb Z$.
>
> *Source (planned): the user's PHY 513 notes, Ch. 7 §7.4.4 · written here*

^thm-cb-11-6

> [!proof]- Proof (to be filled)
> *To be filled ($-\mathbb 1$ acts as $(-1)^{2j_+}$ on $\operatorname{Sym}^{2j_+}$ and as $(-1)^{2j_-}$ on the other factor, Theorem §CB.6.5).*

^pf-cb-11-6

The course's descent theorem, proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8]]

> [!remark]- Connections
> - The two routes to $SL(2, \mathbb C)$ meet at Theorem §CB.11.1: the Hermitian matrix $x^0 + \mathbf x\cdot\boldsymbol\sigma$ of the course is the Clifford product $x\,e_0$, and $\lambda\tilde x\lambda^\dagger$ is conjugation in the Clifford algebra read through $e_0$.
> - The conjugation that exchanges the two $\mathfrak{sl}(2, \mathbb C)$ summands ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], 3) is, on the group, $\lambda \mapsto (\lambda^\dagger)^{-1}$, the same map that relates the two factors of $D^{(j_+, j_-)}$ and the two Weyl matrices $\Lambda_L$, $\Lambda_R$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]).
> - **Used in**: Theorems §CB.11.1–§CB.11.3 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]; Theorems §CB.11.4–§CB.11.5 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.11.6 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]].
