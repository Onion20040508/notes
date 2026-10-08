---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): Linear Algebra (LADR) Def. 6.2, Def. 9.4, Thm. 9.7, Thm. 9.23 (the real analogues) · the user's PHY 513 notes, Ch. 8 §8.1 · Peskin & Schroeder, §3.2 · the rest written here.*

Which structure does $\bar\psi = \psi^\dagger\gamma^0$ add to spinor space, and why is it fixed by the Dirac matrices? An inner product ([[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]]) is a positive-definite Hermitian form; finite-dimensional representations of the Lorentz group admit none that is invariant ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-16|Theorem §CB.3.16]]), but they can preserve an *indefinite* one. This section states the layer of Hermitian forms the spinor chapter uses — matrices and changes of basis, Sylvester's law of inertia, the adjoint for an indefinite form, the pseudo-unitary groups $U(p,q)$ — and the uniqueness theorem: on an irreducible representation, an invariant Hermitian form is unique up to a real factor. It builds on [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs|§CB.3]] (Schur).

<!-- MOVE rows (CB-INVENTORY): Def §C5a.2.1, Thm §C5a.2.1 and Def §C5a.2.2 are embedded below; they are to be moved here in batch 4 (SPEC-CB: "CB.4–CB.6 (+ §C5a.2 move)"). -->

## Hermitian forms and their matrices

A Hermitian form, its matrix, its change of basis and its signature, defined and proved in [[§C5a.2 The Dirac Form|§C5a.2]]:

![[§C5a.2 The Dirac Form#^def-c5a-2-1]]

![[§C5a.2 The Dirac Form#^thm-c5a-2-1]]

![[§C5a.2 The Dirac Form#^def-c5a-2-2]]

> [!theorem] Theorem §CB.5.1: Sylvester's Law of Inertia for Hermitian Forms
> Let $h$ be a nondegenerate Hermitian form ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]) on an $n$-dimensional complex space $V$, of signature $(p, q)$ ([[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]]). Then $p + q = n$, and $V$ has a basis $e_1, \dots, e_n$ with $h(e_a, e_b) = \eta_{ab}$, $\eta = \operatorname{diag}(\mathbb 1_p, -\mathbb 1_q)$ (an **$h$-orthonormal basis**). In every $h$-orthonormal basis the number of $+1$'s is $p$; equivalently, every Hermitian matrix $H$ with $\det H \ne 0$ is $H = U^\dagger\eta U$ for some invertible $U$, with $p$ the number of positive eigenvalues of $H$.
>
> *Source (planned): LADR Thm. 9.23 (the real case) · written here*

^thm-cb-5-1

> [!proof]- Proof (to be filled)
> *To be written in batch 4 (spectral theorem for the Hermitian matrix $H$, [[§24 Spectral Theorem|LADR §24]], then rescaling).*

^pf-cb-5-1

## The adjoint for an indefinite form, and the pseudo-unitary groups

> [!definition] Definition §CB.5.2: The h-Adjoint
> Let $h$ be a nondegenerate Hermitian form on $V$. The **$h$-adjoint** of a linear map $A : V \to V$ is the linear map $A^{\dagger_h}$ with $h(A\chi, \psi) = h(\chi, A^{\dagger_h}\psi)$ for all $\chi, \psi$. $A$ is **$h$-self-adjoint** if $A^{\dagger_h} = A$.
>
> *Source (planned): written here*

^def-cb-5-2

> [!theorem] Theorem §CB.5.3: Properties of the h-Adjoint
> For $h$ nondegenerate with matrix $H$ in some basis ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]):
> 1. $A^{\dagger_h}$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]) exists, is unique, and has matrix $H^{-1}A^\dagger H$;
> 2. $(AB)^{\dagger_h} = B^{\dagger_h}A^{\dagger_h}$, $(\lambda A)^{\dagger_h} = \bar\lambda A^{\dagger_h}$, $(A^{\dagger_h})^{\dagger_h} = A$, $\mathbb 1^{\dagger_h} = \mathbb 1$;
> 3. if $U$ is invariant under a set $\mathcal S$ of linear maps, its $h$-orthogonal complement $U^{\perp_h}$ is invariant under $\{A^{\dagger_h} : A \in \mathcal S\}$, and $\dim U^{\perp_h} = n - \dim U$.
>
> *Source (planned): written here*

^thm-cb-5-3

> [!proof]- Proof (to be filled)
> *To be written in batch 4.*

^pf-cb-5-3

> [!definition] Definition §CB.5.4: Pseudo-Unitary Group
> The **pseudo-unitary group** of a nondegenerate Hermitian form $h$ on $V$ is $U(V, h) = \{A \in GL(V) : h(A\chi, A\psi) = h(\chi, \psi)\ \forall\chi, \psi\} = \{A : A^{\dagger_h}A = \mathbb 1\}$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]). For signature $(p, q)$ and an $h$-orthonormal basis ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-5-1|Theorem §CB.5.1]]) it is $U(p, q) = \{A \in GL(n, \mathbb C) : A^\dagger\eta A = \eta\}$; $U(n, 0) = U(n)$.
>
> *Source (planned): written here*

^def-cb-5-4

> [!theorem] Theorem §CB.5.5: U(p, q) Is a Matrix Lie Group
> $U(p, q)$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]]) is a closed subgroup of $GL(n, \mathbb C)$, so a matrix Lie group ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]), with Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]])
>
> $$
> \mathfrak u(p, q) = \{X \in M_n(\mathbb C) : X^\dagger\eta + \eta X = 0\} = \{X : X^{\dagger_h} = -X\}, \qquad \dim_{\mathbb R}\mathfrak u(p, q) = n^2 .
> $$
>
> In the physicists' form $X = -iT$: a one-parameter subgroup $e^{-isT}$ lies in $U(p, q)$ iff $T$ is $h$-self-adjoint.
>
> *Source (planned): written here (as for $U(n)$, [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|591 Ex. §23.2]])*

^thm-cb-5-5

> [!proof]- Proof (to be filled)
> *To be written in batch 4.*

^pf-cb-5-5

## Invariant Hermitian forms of a representation

> [!definition] Definition §CB.5.6: Invariant Hermitian Form
> A nondegenerate Hermitian form $h$ on the space $W$ of a representation is **invariant** if, for a group representation $D$, every $D(g) \in U(W, h)$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]]); for a Lie algebra representation $d$, every $d(X)$ is $h$-anti-self-adjoint, $d(X)^{\dagger_h} = -d(X)$. For a Clifford module ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]]) the condition used is that every Clifford generator $\gamma(v)$, $v$ real, is $h$-self-adjoint.
>
> *Source (planned): written here · the Dirac form: [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]*

^def-cb-5-6

> [!theorem] Theorem §CB.5.7: Forms with the Same Adjoint on an Irreducible Set Are Proportional
> Let $\mathcal S$ be a set of linear maps of a finite-dimensional complex space $W$ with no invariant subspaces other than $0$ and $W$, and let $h_1$, $h_2$ be nondegenerate Hermitian forms on $W$ with $A^{\dagger_{h_1}} = A^{\dagger_{h_2}}$ for every $A \in \mathcal S$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]). Then $h_1 = c\,h_2$ for a real $c \ne 0$. Consequences:
> 1. an irreducible finite-dimensional representation of a group or Lie algebra has, up to a nonzero real factor, at most one invariant Hermitian form ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-6|Def. §CB.5.6]]);
> 2. on an irreducible Clifford module, a nondegenerate Hermitian form for which every $\gamma(v)$ is self-adjoint is unique up to a nonzero real factor.
>
> *Source (planned): written here · the Dirac case: [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], 2*

^thm-cb-5-7

> [!proof]- Proof (to be filled)
> *To be written in batch 4 (write $h_1(\chi, \psi) = h_2(\chi, S\psi)$; then $S$ commutes with every $A^{\dagger_{h_2}}$, a set with no invariant subspaces by Theorem §CB.5.3, 3; Schur, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-8|Theorem §CB.3.8]], gives $S = c\mathbb 1$; Hermiticity makes $c$ real).*

^pf-cb-5-7

The Dirac form, the instance of consequence 2, in [[§C5a.2 The Dirac Form|§C5a.2]]:

![[§C5a.2 The Dirac Form#^thm-c5a-2-2]]

> [!remark] Remark: Which spinor-chapter facts are instances
> The Dirac form has signature $(2, 2)$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]]), so the spinor Lorentz matrices lie in $U(2, 2)$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]); why $\mathrm{Spin}(1,3)$ preserves it is Theorem §CB.9.16. The covariant photon space carries an indefinite form of the same kind, now on an infinite-dimensional space ([[§C4.7 Covariant Quantization and the Indefinite Metric#^rem-c4-7-3|§C4.7, Remark: A space with an indefinite inner product]]).

^rem-cb-5-1

> [!remark]- Connections
> - The uniqueness theorem (Theorem §CB.5.7) is a basis-free definition of $\bar\psi$: the Dirac maps alone fix the Dirac form up to a real factor, and the overall sign is a convention ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]).
> - Inner products are the positive-definite case ([[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]]); the vault's real analogues are bilinear forms and Sylvester's law over $\mathbb R$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-23|LADR Thm. 9.23]]).
> - **Used in**: Theorem §CB.5.1 — [[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Dirac Form#^def-c5a-2-3|Def. §C5a.2.3]]; Definitions §CB.5.2–Theorem §CB.5.5 — [[§C5a.2 The Dirac Form#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-5|Theorem §C5a.6.5]]; Theorem §CB.5.7 — [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], [[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]; the indefinite metric in general — [[§C4.7 Covariant Quantization and the Indefinite Metric|§C4.7]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons|§C4.8]].
