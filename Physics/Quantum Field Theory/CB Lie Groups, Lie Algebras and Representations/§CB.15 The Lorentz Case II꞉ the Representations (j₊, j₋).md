---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.15
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.16 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵]] →

*Sources: P. Woit, Quantum Theory, Groups and Representations, §40.4 ("Spin and the Lorentz group": four-vectors as $x^0 + \mathbf x\cdot\boldsymbol\sigma$ and the action $\Omega(\cdot)\Omega^\dagger$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · through the course homes embedded below: the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2; PHY 513 Lecture 7; Yu Zhao-Huan, 量子场论讲义, Exercise 3.7; Peskin & Schroeder, §3.1–§3.2 · the Clifford route and the comparison of conventions written here.*

What are the finite-dimensional representations of $SL(2, \mathbb C)$, and which of them are representations of the Lorentz group? With the spin group of [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover|§CB.14]] and the split $\mathbf J_\pm$ of [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms|§CB.4]], this section identifies the finite-dimensional representations of $SL(2, \mathbb C)$ with pairs of commuting $\mathfrak{sl}(2, \mathbb C)$-representations, lists the irreducible ones as the $(j_+, j_-)$, and decides which of them descend to $SO^+(1,3)$. It uses spin $j$ from [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.8]] and the descent criterion of [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.12]]. The course's labels ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]) and descent theorem ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]]) are shown as embeds where they become instances.

<!-- Planned content (OPTION1-PLAN §5, row "CB.11a"): batch B1 moves the C3.3 boxes here — Def §C3.3.1 and Thm §C3.3.1 replace their embeds after Theorem §CB.15.1, then Thm §C3.3.2; after Theorem §CB.15.2: Thm §C3.3.5, §C3.3.6, §C3.3.7, Remark "sums vs products", new box "parity automorphism exchanges the copies" (from Thm §C3.3.8), Thm §C3.3.9, Remark "what the labels mean", Thm §C3.3.10; then Theorem §CB.15.3; batch B2 moves Thm §C5a.4.8 here (replacing its embed). -->

## The finite-dimensional representations of SL(2,ℂ)

> [!theorem] Theorem §CB.15.1: Representations of SL(2,ℂ) Are Pairs of 𝔰𝔩(2,ℂ)-Representations
> For finite-dimensional representations on complex spaces, the following correspond bijectively, preserving invariant subspaces, irreducibility and intertwiners: continuous representations of $SL(2, \mathbb C)$; representations of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], $SL(2, \mathbb C)$ being simply connected, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]); commuting pairs $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-2|Theorem §CB.14.2]]); complex-linear representations of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]]). All of them are completely reducible ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-15|Theorem §CB.5.15]]).
>
> *Source: written here (assembly of the cited theorems)*

^thm-cb-15-1

> [!proof]- Proof
> **1. Group to algebra.** A continuous representation $D : SL(2, \mathbb C) \to GL(W)$ is a Lie group homomorphism ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]]); its differential $d = D_\ast$ is a representation of the Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^def-cb-4-5|Def. §CB.4.5]]).
>
> **2. Algebra to group, bijectively.** $SL(2, \mathbb C)$ is connected and simply connected ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]), so every representation $d$ of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ is $D_\ast$ for exactly one $D$ ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]]). Two representations with the same differential are equal ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-6|Theorem §CB.2.6]]). So $D \mapsto D_\ast$ is a bijection.
>
> **3. Intertwiners agree.** Let $T : W_1 \to W_2$ be linear. If $TD_1(g) = D_2(g)T$ for all $g$, then differentiating $TD_1(e^{sX}) = D_2(e^{sX})T$ at $s = 0$ gives $Td_1(X) = d_2(X)T$ (Theorem §CB.2.3). Conversely, if $Td_1(X) = d_2(X)T$, then $Td_1(X)^n = d_2(X)^nT$ for all $n$, and summing the series $TD_1(e^X) = Te^{d_1(X)} = e^{d_2(X)}T = D_2(e^X)T$; every $g$ is a product of exponentials ([[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-5|Theorem §CB.2.5]], 3), so $TD_1(g) = D_2(g)T$. In particular $D_1 \cong D_2$ iff $d_1 \cong d_2$ (invertible intertwiners, [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-1|Def. §CB.5.1]]).
>
> **4. Invariant subspaces agree.** If $W' \subset W$ is invariant under all $D(g)$, then $d(X)w = \lim_{s\to0}\frac1s(D(e^{sX})w - w) \in W'$ for $w \in W'$ ($W'$ is closed, being finite-dimensional). If $W'$ is invariant under all $d(X)$, it is invariant under every power and hence under $e^{d(X)} = D(e^X)$, and so under all products of exponentials, i.e. all of $SL(2, \mathbb C)$ (Theorem §CB.2.5, 3). Hence irreducibility agrees too.
>
> **5. The other two descriptions.** A representation of the real algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on the complex space $W$ is the same as a commuting pair $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-2|Theorem §CB.14.2]]), and the same as a complex-linear representation of its complexification ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], 1), with the same invariant subspaces and intertwiners (Theorem §CB.3.6, 2). The complexification is isomorphic to $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]]), and pulling back along an isomorphism of Lie algebras changes neither invariant subspaces nor intertwiners. The isomorphism $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ is [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]].
>
> **6. Complete reducibility.** Every finite-dimensional representation of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on a complex space is completely reducible ([[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-15|Theorem §CB.5.15]]); by step 4 the same decomposition into invariant subspaces works for the group.
>
> **What the proof shows**
> - Simple connectivity of $SL(2, \mathbb C)$ is what makes every algebra representation a group representation; for $SO^+(1,3)$ only those with $D(-\mathbb 1) = \mathbb 1$ survive (Theorem §CB.15.3).
> - Continuity is the only regularity assumed on the group side: differentiability comes from the matrix Lie group theory of §CB.1–§CB.2.

^pf-cb-15-1

*Uses:* [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^def-cb-2-1|Def. §CB.2.1]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-5|Theorem §CB.2.5]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-6|Theorem §CB.2.6]], [[§CB.2 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-2-13|Theorem §CB.2.13]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-1|Theorem §CB.14.1]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-2|Theorem §CB.14.2]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-5-1|Def. §CB.5.1]], [[§CB.5 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-5-15|Theorem §CB.5.15]]

The course's representations $(j_+, j_-)$ and their irreducibility, in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]]:

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1]]

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1]]

> [!theorem] Theorem §CB.15.2: The Irreducible Representations of SL(2,ℂ)
> For $j_+, j_- \in \frac12\mathbb Z_{\ge0}$,
>
> $$
> D^{(j_+, j_-)}(\lambda) = \operatorname{Sym}^{2j_+}(\lambda)\otimes\operatorname{Sym}^{2j_-}\bigl((\lambda^\dagger)^{-1}\bigr) \quad\text{on}\quad \operatorname{Sym}^{2j_+}\mathbb C^2\otimes\operatorname{Sym}^{2j_-}\mathbb C^2
> $$
>
> ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-5|Theorem §CB.8.5]]; $(\lambda^\dagger)^{-1} \cong \bar\lambda$ by [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]) is an irreducible representation of $SL(2, \mathbb C)$ of dimension $(2j_+ + 1)(2j_- + 1)$, whose generators, read through the course's covering $\pi$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), are those of $(j_+, j_-)$: $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1}$ is equivalent to the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]; which factor carries $\mathbf J_+$ is fixed by [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]]). Every finite-dimensional irreducible continuous representation of $SL(2, \mathbb C)$ is equivalent to exactly one $D^{(j_+, j_-)}$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3, Ch. 8 §8.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]] and [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]] · written here (from Theorems §CB.15.1, §CB.6.5, §CB.8.3)*

^thm-cb-15-2

> [!proof]- Proof
> Write $\theta(\lambda) = (\lambda^\dagger)^{-1}$ and $\operatorname{Sym}^k(A)$ for the restriction of $A^{\otimes k}$ to $\operatorname{Sym}^k\mathbb C^2$.
>
> **1. A continuous representation.** $\operatorname{Sym}^k\mathbb C^2$ is invariant under $A^{\otimes k}$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], 1), and $(AB)^{\otimes k} = A^{\otimes k}B^{\otimes k}$, so $A \mapsto \operatorname{Sym}^k(A)$ is a homomorphism. $\theta$ is a homomorphism of $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 1), and a tensor product of representations is one. The entries of $D^{(j_+, j_-)}(\lambda)$ are polynomials in the entries of $\lambda$ and $\bar\lambda$ ($\lambda^{-1}$ is the adjugate, since $\det\lambda = 1$), so $D^{(j_+, j_-)}$ is continuous. Its dimension is $\dim\operatorname{Sym}^{2j_+}\mathbb C^2\cdot\dim\operatorname{Sym}^{2j_-}\mathbb C^2 = (2j_+ + 1)(2j_- + 1)$ (Theorem §CB.6.13, 1, $\binom{2j+1}{2j} = 2j + 1$).
>
> **2. It is the course's representation.** By [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-5|Theorem §CB.8.5]], $\operatorname{Sym}^{2j}\mathbb C^2$ with $\operatorname{Sym}^{2j}(\lambda)$ is equivalent to the polynomial realization $P(z) \mapsto P(\lambda^{\mathsf T}z)$ on homogeneous polynomials of degree $2j$. The tensor product of the two equivalences is an equivalence of $D^{(j_+, j_-)}$ with $\tilde D(\lambda) = D^{(j_+)}(\lambda)\otimes D^{(j_-)}(\theta(\lambda))$ of Theorem §C5a.4.8.
>
> **3. Its generators.** Theorem §C5a.4.8, 1: $\tilde D(\Lambda_L(s\omega)) = \exp(-\frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ with $D(\mathcal J^{\mu\nu})$ the generators of $(j_+, j_-)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]). $s \mapsto \Lambda_L(s\omega) = e^{sA_L(\omega)}$ is a one-parameter subgroup with $\pi_\ast(A_L(\omega)) = -\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ (it covers $e^{s\omega}$, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]). Differentiating at $s = 0$: $\tilde D_\ast(A_L(\omega)) = d\bigl(\pi_\ast(A_L(\omega))\bigr)$, where $d$ is the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$, $d(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}) = -\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})$. The $A_L(\omega)$ fill $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, so $\tilde D_\ast = d\circ\pi_\ast$, and by step 2 $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1} \cong d$ (equivalent group representations have equivalent differentials, [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]]).
>
> **4. Irreducible.** $(j_+, j_-)$ is irreducible ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]), and $\pi_\ast$ is a bijection ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]]), so $D^{(j_+, j_-)}_\ast$ has no invariant subspaces but $0$ and the whole space; by Theorem §CB.15.1 neither has $D^{(j_+, j_-)}$.
>
> **5. Every irreducible representation is one of them.** Let $E$ be a finite-dimensional irreducible continuous representation. $E_\ast\circ\pi_\ast^{-1}$ is an irreducible representation of $\mathfrak{so}(1,3)$ (Theorem §CB.15.1). Its complex-linear extension to $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+\oplus\mathfrak a_-$ ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-1|Theorem §CB.4.1]], 2) is irreducible ([[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], 2), hence equivalent to $W_+\boxtimes W_-$ with $W_\pm$ irreducible representations of $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-5|Theorem §CB.6.5]], 2), and each $W_\pm$ is some $V_{j_\pm}$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-3|Theorem §CB.8.3]], 3): $\mathbf J_+$ acts as $\mathbf J^{(j_+)}\otimes\mathbb 1$ and $\mathbf J_-$ as $\mathbb 1\otimes\mathbf J^{(j_-)}$, which is Def. §C3.3.1 (equivalently, [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]] with one summand). By step 3, $E_\ast \cong D^{(j_+, j_-)}_\ast$, so $E \cong D^{(j_+, j_-)}$ (Theorem §CB.15.1).
>
> **6. Exactly one.** If $D^{(j_+, j_-)} \cong D^{(k_+, k_-)}$, their differentials are equivalent, so $(j_+, j_-) \cong (k_+, k_-)$ as $\mathfrak{so}(1,3)$-representations, and the labels coincide (Theorem §C3.3.1, last clause).
>
> **What the proof shows**
> - $(j_+, j_-)$ is $2j_+$ symmetrized slots carrying $\lambda$ and $2j_-$ carrying $(\lambda^\dagger)^{-1}$ — undotted and dotted indices ([[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-16|Theorem §CB.6.16]]).
> - ⚑ By-product (convention): the labels are tied to $\pi$. Read through $\rho$ and the Clifford identification $\phi$, $x \mapsto D^{(j_+, j_-)}(\phi(x))$ is $D^{(j_+, j_-)}\circ\theta$ in the course's parametrization ($\phi = \theta\circ(\theta\circ\phi)$, Theorem §CB.14.4, 2), which is equivalent to $D^{(j_-, j_+)}$: the two factors exchange roles. This is the group form of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]].

^pf-cb-15-2

*Uses:* [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-5|Theorem §CB.6.5]], [[§CB.6 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-6-13|Theorem §CB.6.13]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-3|Theorem §CB.8.3]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-5|Theorem §CB.8.5]], [[§CB.3 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-3-6|Theorem §CB.3.6]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-1|Theorem §CB.4.1]], [[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-6|Theorem §CB.4.6]], [[§CB.15 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-15-1|Theorem §CB.15.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]]

> [!theorem] Theorem §CB.15.3: Which (j₊, j₋) Descend to SO⁺(1,3)
> $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2(j_+ + j_-)}\mathbb 1$. Hence $D^{(j_+, j_-)}$ is tensorial ([[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-17|Def. §CB.12.17]]), i.e. a representation of $SO^+(1,3)$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-7|Theorem §CB.8.7]]), iff $j_+ + j_- \in \mathbb Z$, and spinorial iff $j_+ + j_- \in \frac12 + \mathbb Z$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 6 · written here*

^thm-cb-15-3

> [!proof]- Proof
> **1. The value on −1.** $\operatorname{Sym}^{2j}(-\mathbb 1)$ is $(-\mathbb 1)^{\otimes2j} = (-1)^{2j}\mathbb 1$ restricted to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-5|Theorem §CB.8.5]]), and $((-\mathbb 1)^\dagger)^{-1} = -\mathbb 1$. So $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2j_+}\mathbb 1\otimes(-1)^{2j_-}\mathbb 1 = (-1)^{2(j_+ + j_-)}\mathbb 1$.
>
> **2. Tensorial or spinorial.** Under $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ the element $-1$ goes to $-\mathbb 1$ ([[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], 1, for either identification $\phi$ or $\theta\circ\phi$). $2(j_+ + j_-)$ is an integer; $(-1)^{2(j_+ + j_-)} = 1$ iff it is even, i.e. $j_+ + j_- \in \mathbb Z$ (tensorial, [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-17|Def. §CB.12.17]]), and $= -1$ iff $j_+ + j_- \in \frac12 + \mathbb Z$ (spinorial).
>
> **3. Descent.** $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ is a surjective covering homomorphism with kernel $\{\pm\mathbb 1\}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), as is $\rho$ on $\mathrm{Spin}(1,3)_0$ (Theorem §CB.14.4, 2). By the descent lemma ([[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-7|Theorem §CB.8.7]]) $D^{(j_+, j_-)}$ is $D\circ\pi$ for a representation $D$ of $SO^+(1,3)$ iff $D^{(j_+, j_-)}(-\mathbb 1) = \mathbb 1$, i.e. iff $j_+ + j_- \in \mathbb Z$, and then $D$ is irreducible.
>
> **What the proof shows**
> - The sign is the parity of the total number $2j_+ + 2j_-$ of spinor slots, each slot contributing one factor $-1$.

^pf-cb-15-3

*Uses:* [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-5|Theorem §CB.8.5]], [[§CB.8 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-8-7|Theorem §CB.8.7]], [[§CB.12 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-12-17|Def. §CB.12.17]], [[§CB.14 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-14-4|Theorem §CB.14.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]

The course's descent theorem, proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8]]

> [!remark]- Connections
> - The conjugation that exchanges the two $\mathfrak{sl}(2, \mathbb C)$ summands ([[§CB.4 The Lorentz Algebra꞉ Generators, the Split J± and Real Forms#^thm-cb-4-1|Theorem §CB.4.1]], 3) is, on the group, $\lambda \mapsto (\lambda^\dagger)^{-1}$, the same map that relates the two factors of $D^{(j_+, j_-)}$ and the two Weyl matrices $\Lambda_L$, $\Lambda_R$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]).
> - **Used in**: Theorems §CB.15.1–§CB.15.2 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.15.3 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]].
