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

*Sources: Linear Algebra (LADR) §§6, 12, 23–24, 35 · the user's PHY 513 notes, Ch. 8 §8.1 · B. C. Hall, Quantum Theory for Mathematicians, Def. 16.1, Examples 16.4, 16.22 · Y. Nakatsukasa, V. Noferini, arXiv:1711.00495, Thm. 1 · K. Conrad, Bilinear Forms (https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf), Thms. 3.12, 3.16, 3.21, 6.19, Def. 3.17 · I. I. Cotăescu, Elements of Linear Algebra (arXiv:1602.03006), §4.2 · J. Adams, D. Vogan, arXiv:1502.03304, Prop. 1.4 · the rest written here.*

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
> *Source: Y. Nakatsukasa, V. Noferini, Inertia laws and localization of real eigenvalues for generalized indefinite eigenvalue problems, arXiv:1711.00495, Thm. 1 and its proof (Sylvester's law for Hermitian matrices: diagonalize by the spectral theorem and rescale; $n_+(A)$ is the maximal dimension of a positive-definite subspace) · K. Conrad, Bilinear Forms (expository notes, https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf), Thm. 6.19 (the dimension argument, real case) · the same argument for the Dirac form: [[§C5a.2 The Dirac Form#^der-c5a-2-3|Derivation §C5a.2.3]] · the real analogue: [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-23|LADR Thm. 9.23]]*

^thm-cb-5-1

> [!proof]- Proof
> *The proof of Nakatsukasa–Noferini, Thm. 1, with the "maximal positive subspace" step written out as in Conrad, Thm. 6.19.*
>
> **1. Diagonalize the matrix.** Fix a basis $f_1, \dots, f_n$ of $V$ and let $H$ be the matrix of $h$; $H^\dagger = H$ and $\det H \ne 0$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], 1). As an operator on $\mathbb C^n$ with the standard inner product, $H$ is self-adjoint (its adjoint has the conjugate-transpose matrix, [[§23 Self-Adjoint and Normal Operators#^ladr-7-9|LADR Thm. 7.9]]), so its eigenvalues $\lambda_1, \dots, \lambda_n$ are real ([[§23 Self-Adjoint and Normal Operators#^ladr-7-12|LADR Thm. 7.12]]) and $\mathbb C^n$ has an orthonormal basis $u_1, \dots, u_n$ of eigenvectors, $Hu_a = \lambda_au_a$ ([[§24 Spectral Theorem#^ladr-7-31|LADR Thm. 7.31]]). No $\lambda_a$ is $0$, since $\det H = \prod_a\lambda_a \ne 0$. Order them so that $\lambda_1, \dots, \lambda_{p'} > 0$ and $\lambda_{p'+1}, \dots, \lambda_n < 0$; $p'$ is the number of positive eigenvalues of $H$.
>
> **2. The form in the eigenvector basis.** Let $g_a \in V$ have coordinate column $u_a$ in the basis $f$. Then
>
> $$
> h(g_a, g_b) = u_a^\dagger Hu_b = \lambda_b\,u_a^\dagger u_b = \lambda_b\,\delta_{ab} .
> $$
>
> **3. Rescale.** Put $e_a = g_a/\sqrt{|\lambda_a|}$. Conjugate-linearity in the first slot and linearity in the second give $h(e_a, e_b) = \lambda_b\delta_{ab}/|\lambda_b| = \operatorname{sgn}(\lambda_a)\,\delta_{ab}$: an $h$-orthonormal basis with $p'$ entries $+1$ and $n - p'$ entries $-1$.
>
> **4. The number of +1's is the signature.** Let $e_1, \dots, e_n$ be *any* $h$-orthonormal basis with $p'$ entries $+1$ (first) and $n - p'$ entries $-1$. For $\psi = \sum_a c_ae_a \ne 0$ in $P_0 = \operatorname{span}(e_1, \dots, e_{p'})$, $h(\psi, \psi) = \sum_{a \le p'}|c_a|^2 > 0$: $P_0$ is positive, so $p \ge p'$ ([[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]]). Let $P$ be any positive subspace and $N_0 = \operatorname{span}(e_{p'+1}, \dots, e_n)$, on which $h(\psi, \psi) = -\sum_{a > p'}|c_a|^2 \le 0$. A nonzero $\psi \in P\cap N_0$ would have $h(\psi, \psi) > 0$ and $\le 0$, so $P\cap N_0 = 0$, and $\dim P + (n - p') = \dim(P + N_0) \le n$ ([[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]): $\dim P \le p'$. Hence $p = p'$. The same argument with the signs exchanged gives $q = n - p'$, so $p + q = n$; and since $p$ is defined without a basis, every $h$-orthonormal basis has $p$ entries $+1$.
>
> **5. Matrix form.** Let $U$ be the change-of-basis matrix from $f$ to the basis $e$ of step 3. The matrix of $h$ in $e$ is $\eta$, and by [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], 2, $\eta = (U^{-1})^\dagger HU^{-1}$, i.e. $H = U^\dagger\eta U$, with $p = p'$ the number of positive eigenvalues of $H$ (steps 1 and 4).
>
> **What the proof shows**
> - The eigenvalues of $H$ change under a change of basis ($H \mapsto (U^{-1})^\dagger HU^{-1}$ is not a similarity unless $U$ is unitary), but the number of positive ones does not: that number is the basis-free maximal dimension of a positive subspace.
> - ⚑ By-product: every nondegenerate Hermitian form is, in a suitable basis, $h(\chi, \psi) = \sum_{a \le p}\bar\chi_a\psi_a - \sum_{a > p}\bar\chi_a\psi_a$; forms of the same signature differ only by a change of basis. This is what makes $U(p, q)$ well defined up to conjugation (Def. §CB.5.4).
> - Nondegeneracy is used only to exclude zero eigenvalues; for a degenerate form the same proof gives $p + q + n_0 = n$ with $n_0$ the dimension of the kernel.

^pf-cb-5-1

*Uses:* [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§C5a.2 The Dirac Form#^def-c5a-2-2|Def. §C5a.2.2]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-9|LADR Thm. 7.9]], [[§23 Self-Adjoint and Normal Operators#^ladr-7-12|LADR Thm. 7.12]], [[§24 Spectral Theorem#^ladr-7-31|LADR Thm. 7.31]], [[§6 Dimension#^ladr-2-43|LADR Thm. 2.43]]

## The adjoint for an indefinite form, and the pseudo-unitary groups

> [!definition] Definition §CB.5.2: The h-Adjoint
> Let $h$ be a nondegenerate Hermitian form on $V$. The **$h$-adjoint** of a linear map $A : V \to V$ is the linear map $A^{\dagger_h}$ with $h(A\chi, \psi) = h(\chi, A^{\dagger_h}\psi)$ for all $\chi, \psi$. $A$ is **$h$-self-adjoint** if $A^{\dagger_h} = A$.
>
> *Source: K. Conrad, Bilinear Forms, Def. 3.17 (the adjoint relative to a nondegenerate bilinear form) · I. I. Cotăescu, Elements of Linear Algebra (arXiv:1602.03006), §4.2.2, Def. 69 (the Dirac adjoint) · the Hermitian formulation written here*

^def-cb-5-2

> [!theorem] Theorem §CB.5.3: Properties of the h-Adjoint
> For $h$ nondegenerate with matrix $H$ in some basis ([[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]]):
> 1. $A^{\dagger_h}$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]) exists, is unique, and has matrix $H^{-1}A^\dagger H$;
> 2. $(AB)^{\dagger_h} = B^{\dagger_h}A^{\dagger_h}$, $(\lambda A)^{\dagger_h} = \bar\lambda A^{\dagger_h}$, $(A^{\dagger_h})^{\dagger_h} = A$, $\mathbb 1^{\dagger_h} = \mathbb 1$;
> 3. if $U$ is invariant under a set $\mathcal S$ of linear maps, its $h$-orthogonal complement $U^{\perp_h}$ is invariant under $\{A^{\dagger_h} : A \in \mathcal S\}$, and $\dim U^{\perp_h} = n - \dim U$.
>
> *Source: K. Conrad, Bilinear Forms (https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf), Def. 3.17, Thm. 3.16 (2)–(3), Thm. 3.21 ($[A^{\ast}] = M^{-1}[A]^{\mathsf T}M$, matrix proof) and Thm. 3.12 (2) ($\dim W + \dim W^\perp = \dim V$ for nondegenerate forms), all for bilinear forms, here with the conjugate-linear first slot · I. I. Cotăescu, Elements of Linear Algebra (lecture notes, arXiv:1602.03006), §4.2.2, Def. 69 and eq. (120) (the Dirac adjoint for an indefinite metric and its rules) · the positive-definite case: [[§23 Self-Adjoint and Normal Operators#^ladr-7-5|LADR Thm. 7.5]]*

^thm-cb-5-3

> [!proof]- Proof
> *Conrad's proofs for bilinear forms, transcribed to the Hermitian case (the only change: scalars come out of the first slot conjugated), with Cotăescu's rules (120) checked one by one.*
>
> **1. Existence: the matrix.** In a basis with matrix $H$ of $h$ ($\det H \ne 0$, [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], 1) let $B$ be the map with matrix $H^{-1}A^\dagger H$. Then for all coordinate columns
>
> $$
> h(A\chi, \psi) = (A\chi)^\dagger H\psi = \chi^\dagger A^\dagger H\psi = \chi^\dagger H\bigl(H^{-1}A^\dagger H\bigr)\psi = h(\chi, B\psi) ,
> $$
>
> so $B$ satisfies the defining property of $A^{\dagger_h}$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]).
>
> **2. Uniqueness (Conrad, Thm. 3.16 (2)–(3)).** If $h(\chi, B\psi) = h(\chi, B'\psi)$ for all $\chi, \psi$, then $h(\chi, (B - B')\psi) = 0$ for all $\chi$, so $(B - B')\psi = 0$ by nondegeneracy ([[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]]), for every $\psi$: $B = B'$. Part 1 is proved.
>
> **3. Part 2, each rule by uniqueness.** In each case the right side is shown to have the defining property, and step 2 identifies it with the left side.
> - $h(AB\chi, \psi) = h(B\chi, A^{\dagger_h}\psi) = h(\chi, B^{\dagger_h}A^{\dagger_h}\psi)$, so $(AB)^{\dagger_h} = B^{\dagger_h}A^{\dagger_h}$.
> - $h(\lambda A\chi, \psi) = \bar\lambda\,h(A\chi, \psi) = \bar\lambda\,h(\chi, A^{\dagger_h}\psi) = h(\chi, \bar\lambda A^{\dagger_h}\psi)$ (conjugate-linear first slot, linear second slot), so $(\lambda A)^{\dagger_h} = \bar\lambda A^{\dagger_h}$.
> - $h(A^{\dagger_h}\chi, \psi) = \overline{h(\psi, A^{\dagger_h}\chi)} = \overline{h(A\psi, \chi)} = h(\chi, A\psi)$ (Hermitian symmetry twice), so $(A^{\dagger_h})^{\dagger_h} = A$.
> - $h(\mathbb 1\chi, \psi) = h(\chi, \mathbb 1\psi)$, so $\mathbb 1^{\dagger_h} = \mathbb 1$.
>
> **4. Part 3: invariance of the complement.** $U^{\perp_h} = \{\psi : h(u, \psi) = 0\ \forall u \in U\}$. Let $A \in \mathcal S$, $\psi \in U^{\perp_h}$, $u \in U$. Then $Au \in U$, so $h(u, A^{\dagger_h}\psi) = h(Au, \psi) = 0$: $A^{\dagger_h}\psi \in U^{\perp_h}$.
>
> **5. Part 3: the dimension (Conrad, Thm. 3.12 (2)).** Let $\phi : V \to V'$, $\phi(v) = h(v, \cdot\,)$; each $h(v, \cdot\,)$ is linear, and $\phi$ is conjugate-linear. It is injective: $h(v, \psi) = 0$ for all $\psi$ gives $h(\psi, v) = \overline{h(v, \psi)} = 0$ for all $\psi$, so $v = 0$ by nondegeneracy. A conjugate-linear injection maps a basis to a linearly independent list (if $\sum c_a\phi(v_a) = 0$ then $\phi(\sum\bar c_av_a) = 0$, so all $c_a = 0$), and $\dim V' = \dim V$ ([[§12 Duality#^ladr-3-111|LADR Thm. 3.111]]), so $\phi$ is bijective and maps subspaces onto subspaces of the same dimension. Now $v \in U^{\perp_h}$ iff $h(u, v) = 0$ for all $u \in U$ iff $\phi(v) = h(v, \cdot\,) = \overline{h(\cdot\,, v)}$ vanishes on $U$, i.e. iff $\phi(v)$ lies in the annihilator $U^0$. So $\phi(U^{\perp_h}) = U^0$ and $\dim U^{\perp_h} = \dim U^0 = n - \dim U$ ([[§12 Duality#^ladr-3-125|LADR Thm. 3.125]]).
>
> **What the proof shows**
> - Only nondegeneracy is used, never positivity: the adjoint exists for every nondegenerate form, with the form's matrix $H$ appearing as $H^{-1}A^\dagger H$ (for $H = \mathbb 1$, the ordinary $A^\dagger$).
> - ⚑ By-product: for an indefinite form, $U^{\perp_h}$ has the complementary dimension but need not be a complement — $U\cap U^{\perp_h}$ can be nonzero (a null line, $h(u, u) = 0$, lies in its own orthogonal space). So invariance of $U^{\perp_h}$ does **not** give complete reducibility as it does for an inner product (Theorem §CB.3.14); compare the null vectors of the covariant photon space ([[§C4.7 Covariant Quantization and the Indefinite Metric#^rem-c4-7-3|§C4.7, Remark: A space with an indefinite inner product]]).
> - Used next: Theorem §CB.5.7 uses part 3 to transfer irreducibility from $\mathcal S$ to $\{A^{\dagger_h}\}$.

^pf-cb-5-3

*Uses:* [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]], [[§C5a.2 The Dirac Form#^def-c5a-2-1|Def. §C5a.2.1]], [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§12 Duality#^ladr-3-111|LADR Thm. 3.111]], [[§12 Duality#^ladr-3-125|LADR Thm. 3.125]]

> [!definition] Definition §CB.5.4: Pseudo-Unitary Group
> The **pseudo-unitary group** of a nondegenerate Hermitian form $h$ on $V$ is $U(V, h) = \{A \in GL(V) : h(A\chi, A\psi) = h(\chi, \psi)\ \forall\chi, \psi\} = \{A : A^{\dagger_h}A = \mathbb 1\}$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]). For signature $(p, q)$ and an $h$-orthonormal basis ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-5-1|Theorem §CB.5.1]]) it is $U(p, q) = \{A \in GL(n, \mathbb C) : A^\dagger\eta A = \eta\}$; $U(n, 0) = U(n)$.
>
> *Source: I. I. Cotăescu, Elements of Linear Algebra (arXiv:1602.03006), §4.2.2, Thm. 21 · B. C. Hall, Quantum Theory for Mathematicians, Example 16.4 (the case $U(n)$) · written here*

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
> *Source: B. C. Hall, Quantum Theory for Mathematicians, Def. 16.1 (closed subgroups) and Example 16.22 with its proof (the Lie algebra of $U(n)$: $e^{tX}$ unitary for all $t$ iff $X^{\ast} = -X$, by $(e^{tX})^{\ast} = e^{tX^{\ast}}$ and differentiation at $t = 0$), run with $\eta$ inserted · the case $U(n)$ in the Math vault: [[§23 The Orthogonal and Unitary Groups as Smooth Manifolds#^ex-23-2|591 Ex. §23.2]] · I. I. Cotăescu, Elements of Linear Algebra (arXiv:1602.03006), §4.2.2, Thm. 21 (the pseudo-unitary group as the group with $f^{-1} = \bar f$)*

^thm-cb-5-5

> [!proof]- Proof
> *Hall's proof for $U(n)$ (Example 16.22), with the identity matrix replaced by $\eta$; $\eta^\dagger = \eta = \eta^{-1}$ throughout.*
>
> **1. A subgroup.** If $A^\dagger\eta A = \eta$ and $B^\dagger\eta B = \eta$, then $(AB)^\dagger\eta(AB) = B^\dagger(A^\dagger\eta A)B = B^\dagger\eta B = \eta$. Multiplying $A^\dagger\eta A = \eta$ on the left by $(A^{-1})^\dagger = (A^\dagger)^{-1}$ and on the right by $A^{-1}$ gives $\eta = (A^{-1})^\dagger\eta A^{-1}$, so $A^{-1} \in U(p, q)$; and $\mathbb 1 \in U(p, q)$.
>
> **2. Closed (Hall, Def. 16.1).** $F(A) = A^\dagger\eta A - \eta$ is continuous on $M_n(\mathbb C)$ (its entries are polynomials in the entries of $A$ and $\bar A$), so $U(p, q) = F^{-1}(0)\cap GL(n, \mathbb C)$ is closed in $GL(n, \mathbb C)$: a matrix Lie group ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]).
>
> **3. The Lie algebra, ⊇.** By [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]] the Lie algebra is $\{X : e^{sX} \in U(p, q)\ \forall s \in \mathbb R\}$. Suppose $X^\dagger\eta + \eta X = 0$, i.e. $X^\dagger = -\eta X\eta^{-1}$. By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 4, $(e^{sX})^\dagger = e^{sX^\dagger} = e^{-s\eta X\eta^{-1}} = \eta\,e^{-sX}\eta^{-1}$, so
>
> $$
> (e^{sX})^\dagger\,\eta\,e^{sX} = \eta\,e^{-sX}\eta^{-1}\eta\,e^{sX} = \eta\,e^{-sX}e^{sX} = \eta ,
> $$
>
> using $e^{-sX}e^{sX} = \mathbb 1$ (Theorem §CB.1.2, 2). So $e^{sX} \in U(p, q)$ for every $s$.
>
> **4. The Lie algebra, ⊆.** Conversely, if $e^{sX^\dagger}\eta\,e^{sX} = \eta$ for all $s$, differentiate at $s = 0$ with the product rule and Theorem §CB.1.2, 5 ($\frac{d}{ds}e^{sY} = Ye^{sY}$): $X^\dagger\eta + \eta X = 0$.
>
> **5. The h-adjoint form.** In the $h$-orthonormal basis the matrix of $h$ is $\eta$, so $X^{\dagger_h} = \eta^{-1}X^\dagger\eta = \eta X^\dagger\eta$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-5-3|Theorem §CB.5.3]], 1). Then $X^{\dagger_h} = -X$ iff $\eta X^\dagger\eta = -X$ iff (multiply on the left by $\eta$) $X^\dagger\eta = -\eta X$: the same condition.
>
> **6. Dimension.** $X \mapsto \eta X$ is real-linear and its own inverse ($\eta^2 = \mathbb 1$). It maps $\mathfrak u(p, q)$ onto $\mathfrak u(n)$: $(\eta X)^\dagger = X^\dagger\eta = -\eta X$ iff $X \in \mathfrak u(p, q)$. So $\dim_{\mathbb R}\mathfrak u(p, q) = \dim_{\mathbb R}\mathfrak u(n) = n^2$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]: $n$ real diagonal parameters of $i\mathbb R$ and $\frac{n(n-1)}2$ complex entries above the diagonal, $n + n(n-1) = n^2$).
>
> **7. Physicists' form.** For $X = -iT$, $X^{\dagger_h} = (-iT)^{\dagger_h} = \overline{(-i)}\,T^{\dagger_h} = iT^{\dagger_h}$ (Theorem §CB.5.3, 2). So $X^{\dagger_h} = -X = iT$ iff $T^{\dagger_h} = T$; by steps 3–5, $e^{-isT} \in U(p, q)$ for all real $s$ iff $-iT \in \mathfrak u(p, q)$ iff $T$ is $h$-self-adjoint.
>
> **What the proof shows**
> - For $q = 0$ it is Hall's proof for $U(n)$ word for word; the indefinite form changes nothing in the argument, only the meaning of "self-adjoint".
> - ⚑ By-product: the generators of a pseudo-unitary group are $h$-self-adjoint, not Hermitian. In the Dirac representation the boost generators $S^{0i}$ are anti-Hermitian yet $h_D$-self-adjoint, which is how $\Lambda_{1/2}$ can preserve $\bar\psi\psi$ without being unitary ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]).
> - $\mathfrak u(p, q)$ and $\mathfrak u(n)$ have the same dimension and are isomorphic as real vector spaces by step 6, but not as Lie algebras for $p, q > 0$ ($X \mapsto \eta X$ does not preserve brackets); their complexifications are both $\mathfrak{gl}(n, \mathbb C)$.

^pf-cb-5-5

*Uses:* [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]]

## Invariant Hermitian forms of a representation

> [!definition] Definition §CB.5.6: Invariant Hermitian Form
> A nondegenerate Hermitian form $h$ on the space $W$ of a representation is **invariant** if, for a group representation $D$, every $D(g) \in U(W, h)$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]]); for a Lie algebra representation $d$, every $d(X)$ is $h$-anti-self-adjoint, $d(X)^{\dagger_h} = -d(X)$. For a Clifford module ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-9|Def. §CB.7.9]]) the condition used is that every Clifford generator $\gamma(v)$, $v$ real, is $h$-self-adjoint.
>
> *Source: written here · the Dirac form: [[§C5a.2 The Dirac Form#^def-c5a-2-4|Def. §C5a.2.4]]*

^def-cb-5-6

> [!theorem] Theorem §CB.5.7: Forms with the Same Adjoint on an Irreducible Set Are Proportional
> Let $\mathcal S$ be a set of linear maps of a finite-dimensional complex space $W$ with no invariant subspaces other than $0$ and $W$, and let $h_1$, $h_2$ be nondegenerate Hermitian forms on $W$ with $A^{\dagger_{h_1}} = A^{\dagger_{h_2}}$ for every $A \in \mathcal S$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]). Then $h_1 = c\,h_2$ for a real $c \ne 0$. Consequences:
> 1. an irreducible finite-dimensional representation of a group or Lie algebra has, up to a nonzero real factor, at most one invariant Hermitian form ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-6|Def. §CB.5.6]]);
> 2. on an irreducible Clifford module, a nondegenerate Hermitian form for which every $\gamma(v)$ is self-adjoint is unique up to a nonzero real factor.
>
> *Source: the argument of [[§C5a.2 The Dirac Form#^der-c5a-2-2|Derivation §C5a.2.2]], steps 2–4 (the Dirac case: the form is fixed up to a real factor because $\gamma^0H$ commutes with all $\gamma^\mu$), with Schur's lemma for the general irreducible set · K. Conrad, Bilinear Forms, Thm. 3.16 (4) (every form is $B(v, Aw)$ for a unique linear $A$) · the statement for irreducible group representations: J. Adams, D. Vogan, Parameters for twisted representations (arXiv:1502.03304), Prop. 1.4 ("Schur's Lemma", stated without proof)*

^thm-cb-5-7

> [!proof]- Proof
> *Derivation §C5a.2.2 generalized: there the commuting matrix is $\gamma^0H$ and the irreducible set is the four $\gamma^\mu$; here the commuting operator is $S$ and the irreducible set is $\{A^{\dagger_{h_2}}\}$.*
>
> **1. Compare the forms through an operator.** Let $H_1$, $H_2$ be the matrices of $h_1$, $h_2$ in one basis ($\det H_2 \ne 0$, [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], 1) and $S$ the map with matrix $H_2^{-1}H_1$. Then $h_2(\chi, S\psi) = \chi^\dagger H_2H_2^{-1}H_1\psi = h_1(\chi, \psi)$ for all $\chi, \psi$ (Conrad, Thm. 3.16 (4), in Hermitian form). $S$ is invertible since $\det H_1 \ne 0$.
>
> **2. S commutes with the common adjoints.** Write $A^\dagger$ for the common value $A^{\dagger_{h_1}} = A^{\dagger_{h_2}}$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]), $A \in \mathcal S$. Compute $h_1(A\chi, \psi)$ in two ways:
>
> $$
> h_1(A\chi, \psi) = h_1(\chi, A^\dagger\psi) = h_2(\chi, SA^\dagger\psi), \qquad h_1(A\chi, \psi) = h_2(A\chi, S\psi) = h_2(\chi, A^\dagger S\psi) .
> $$
>
> The two right sides agree for all $\chi$, so by nondegeneracy of $h_2$, $SA^\dagger\psi = A^\dagger S\psi$ for all $\psi$: $SA^\dagger = A^\dagger S$ for every $A \in \mathcal S$.
>
> **3. The adjoints form an irreducible set.** Let $U$ be invariant under every $A^\dagger$, $A \in \mathcal S$. By [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-5-3|Theorem §CB.5.3]], 3 (for $h_2$), $U^{\perp_{h_2}}$ is invariant under every $(A^\dagger)^{\dagger_{h_2}} = A$ (Theorem §CB.5.3, 2), so $U^{\perp_{h_2}} \in \{0, W\}$, and $\dim U = n - \dim U^{\perp_{h_2}} \in \{n, 0\}$: $U = W$ or $U = 0$.
>
> **4. Schur.** The operators $A^\dagger$ generate an algebra of operators on $W$ with the same invariant subspaces (complex combinations of products), i.e. an irreducible representation of an associative algebra ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]]), and $S$ commutes with all of it by step 2. By Schur's lemma ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-8|Theorem §CB.3.8]]) $S = c\,\mathbb 1$, so $h_1 = c\,h_2$, and $c \ne 0$ because $S$ is invertible.
>
> **5. c is real.** Choose $\chi, \psi$ with $h_2(\chi, \psi) \ne 0$ (nondegeneracy). Hermitian symmetry of both forms: $c\,h_2(\chi, \psi) = h_1(\chi, \psi) = \overline{h_1(\psi, \chi)} = \overline{c\,h_2(\psi, \chi)} = \bar c\,h_2(\chi, \psi)$, so $c = \bar c$.
>
> **6. Consequence 1.** For an invariant form of a group representation, $D(g)^{\dagger_h}D(g) = \mathbb 1$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]]), so $D(g)^{\dagger_h} = D(g)^{-1} = D(g^{-1})$, the same for every invariant $h$; for a Lie algebra representation, $d(X)^{\dagger_h} = -d(X)$ for every invariant $h$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-6|Def. §CB.5.6]]). With $\mathcal S = D(G)$ or $d(\mathfrak g)$, irreducible, the theorem applies to any two invariant forms.
>
> **7. Consequence 2.** If every $\gamma(v)$ is self-adjoint for $h_1$ and for $h_2$, then $\gamma(v)^{\dagger_{h_1}} = \gamma(v) = \gamma(v)^{\dagger_{h_2}}$; the $\gamma(v)$ generate the module action, so on an irreducible Clifford module the set $\{\gamma(v)\}$ is irreducible and the theorem applies.
>
> **What the proof shows**
> - Only the *adjoint operation* of a form matters: two forms with the same adjoint on an irreducible set differ by a real factor. The Dirac case ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], 2) is consequence 2 for $Cl(1,3)$.
> - ⚑ By-product: the factor $c$ may be negative, which exchanges $p$ and $q$ (Theorem §CB.5.1). So the signature of an invariant Hermitian form on an irreducible representation is determined up to the swap $(p, q) \leftrightarrow (q, p)$, and its overall sign is a convention (Adams–Vogan, Prop. 1.4).
> - Irreducibility is essential: on $V\oplus V$ the forms $h\oplus h$ and $h\oplus(-h)$ have the same adjoints for the diagonal action but are not proportional.

^pf-cb-5-7

*Uses:* [[§C5a.2 The Dirac Form#^thm-c5a-2-1|Theorem §C5a.2.1]], [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]], [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^thm-cb-5-3|Theorem §CB.5.3]], [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]], [[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-6|Def. §CB.5.6]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-7|Def. §CB.3.7]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-8|Theorem §CB.3.8]]

The Dirac form, the instance of consequence 2, in [[§C5a.2 The Dirac Form|§C5a.2]]:

![[§C5a.2 The Dirac Form#^thm-c5a-2-2]]

> [!remark] Remark: Which spinor-chapter facts are instances
> The Dirac form has signature $(2, 2)$ ([[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]]), so the spinor Lorentz matrices lie in $U(2, 2)$ ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]); why $\mathrm{Spin}(1,3)$ preserves it is Theorem §CB.9.16. The covariant photon space carries an indefinite form of the same kind, now on an infinite-dimensional space ([[§C4.7 Covariant Quantization and the Indefinite Metric#^rem-c4-7-3|§C4.7, Remark: A space with an indefinite inner product]]).

^rem-cb-5-1

> [!remark]- Connections
> - The uniqueness theorem (Theorem §CB.5.7) is a basis-free definition of $\bar\psi$: the Dirac maps alone fix the Dirac form up to a real factor, and the overall sign is a convention ([[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]]).
> - Inner products are the positive-definite case ([[§20 Inner Products and Norms#^ladr-6-2|LADR Def. 6.2]]); the vault's real analogues are bilinear forms and Sylvester's law over $\mathbb R$ ([[§35 Bilinear Forms and Quadratic Forms#^ladr-9-7|LADR Thm. 9.7]], [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-23|LADR Thm. 9.23]]).
> - **Used in**: Theorem §CB.5.1 — [[§C5a.2 The Dirac Form#^thm-c5a-2-3|Theorem §C5a.2.3]], [[§C5a.2 The Dirac Form#^def-c5a-2-3|Def. §C5a.2.3]]; Definitions §CB.5.2–Theorem §CB.5.5 — [[§C5a.2 The Dirac Form#^thm-c5a-2-4|Theorem §C5a.2.4]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-5|Theorem §C5a.3.5]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-5|Theorem §C5a.6.5]]; Theorem §CB.5.7 — [[§C5a.2 The Dirac Form#^thm-c5a-2-2|Theorem §C5a.2.2]], [[§C5a.2 The Dirac Form#^def-c5a-2-5|Def. §C5a.2.5]]; the indefinite metric in general — [[§C4.7 Covariant Quantization and the Indefinite Metric|§C4.7]], [[§C4.8 The Gupta–Bleuler Condition and Physical Photons|§C4.8]].
