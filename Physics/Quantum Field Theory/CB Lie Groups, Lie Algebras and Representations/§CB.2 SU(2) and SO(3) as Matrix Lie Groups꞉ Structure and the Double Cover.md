---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings]] →

*Sources (proofs written from these, each checked against the text): for Theorems §CB.2.1–§CB.2.3 (CB ordering pass, restated from Quantum Mechanics): Sakurai §§3.1.1, 3.2.5, 3.3.2; the user's 511 notes; the user's series, Part IV, §§11–12 · for Theorem §CB.2.4: the user's PHY 513 notes, Ch. 7 §7.2 (the course's theorem of PHY 513 Lecture 7, Part A) · Yu Zhao-Huan, 量子场论讲义, §3.2 · Peskin & Schroeder, §3.1 · B. C. Hall, Quantum Theory for Mathematicians, Ch. 16 · the Math vault: Differentiable Manifolds (591) §§25, 42 · LADR §§26, 37 · Group Theory (493) §§15, 41.*

Which matrix groups describe rotations, and how can two different groups have the same Lie algebra? This section applies the exponential map and the Lie algebras of [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras|§CB.1]] to the course's first example, the rotation group $SO(3)$ and its double cover $SU(2)$: every rotation about an axis is an exponential $e^{\phi A_{\hat{\mathbf n}}}$ of a generator with $[A_i, A_j] = \varepsilon_{ijk}A_k$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]]); $SU(2)$ is the 3-sphere, and each of its elements is $e^{-i\phi\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-2|Theorem §CB.2.2]]); $U \mapsto R(U)$ is a homomorphism of $SU(2)$ onto $SO(3)$ with kernel $\{\pm\mathbb 1\}$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-3|Theorem §CB.2.3]]); and its differential is the isomorphism $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-4|Theorem §CB.2.4]]). The proofs use only [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors|§CB.0]] (the Levi-Civita symbol and the Pauli matrices), §CB.1 and the Math vault; their physics home is Quantum Mechanics (QM §C5.1–§C5.2, linked below), whose statements are restated here in the matrix form the rest of CB uses. What the common Lie algebra cannot decide — which representations belong to $SO(3)$ and which only to $SU(2)$ — needs the homomorphisms and coverings of [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings|§CB.3]] and is settled in [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan|§CB.10]]; the same covering returns as $\mathrm{Spin}(3) = SU(2)$ in [[§CB.15 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.15]]. Statements are numbered in reading order with one counter per section (Theorem §CB.2.1, …); boxes shown as embeds keep their home numbers.

## SU(2) and SO(3)

The rotation group and its double cover as matrix groups. The physics home of these statements is Quantum Mechanics ([[§C5.1 Rotations and the Angular-Momentum Commutation Relations|QM §C5.1]], [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations|QM §C5.2]]), and the Math vault proves the covering with quaternions ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]]); they are restated here, with their proofs, in the matrix form the rest of CB uses (CB ordering pass, 2026-10-08):

> [!theorem] Theorem §CB.2.1: Rotations about an Axis Are Exponentials
> For a unit vector $\hat{\mathbf n} \in \mathbb R^3$ and $\phi \in \mathbb R$ let $R(\hat{\mathbf n}, \phi)$ be the rotation by $\phi$ about $\hat{\mathbf n}$ (counterclockwise seen from the tip of $\hat{\mathbf n}$),
>
> $$
> R(\hat{\mathbf n}, \phi)\mathbf V = (\hat{\mathbf n}\cdot\mathbf V)\hat{\mathbf n} + \cos\phi\,\mathbf V_\perp + \sin\phi\,\hat{\mathbf n}\times\mathbf V_\perp, \qquad \mathbf V_\perp = \mathbf V - (\hat{\mathbf n}\cdot\mathbf V)\hat{\mathbf n} .
> $$
>
> 1. **Generators.** $R(\hat{\mathbf n}, \phi) \in SO(3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]), $R(\hat{\mathbf n}, \phi)R(\hat{\mathbf n}, \psi) = R(\hat{\mathbf n}, \phi + \psi)$, and
>
> $$
> R(\hat{\mathbf n}, \phi) = \exp(\phi A_{\hat{\mathbf n}}), \qquad A_{\hat{\mathbf n}}\mathbf V = \hat{\mathbf n}\times\mathbf V, \qquad (A_{\hat{\mathbf n}})_{ij} = -\varepsilon_{kij}\,n_k ;
> $$
>
> write $A_k$ for $A_{\hat{\mathbf e}_k}$, $(A_k)_{lm} = -\varepsilon_{klm}$.
> 2. **Their algebra.** $[A_i, A_j] = \varepsilon_{ijk}A_k$.
>
> *Source: Sakurai §3.1.1, eqs. (3.1)–(3.9) · the user's 511 notes, §"Rotations and Angular Momentum Commutation Relations", §"Finite Versus Infinitesimal Rotations" · the course's version: [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], 1–2, the same statement (QM adds the second-order failure of rotations to commute).*

^thm-cb-2-1

> [!proof]- Proof
> *Adapted from the derivation of QM Theorem §C5.1.1 (Sakurai §3.1.1); the exponential is obtained from Theorem §CB.1.10 instead of a differential equation.*
>
> **1. A rotation.** Complete $\hat{\mathbf n}$ to a right-handed orthonormal basis $(\hat{\mathbf u}, \hat{\mathbf n}\times\hat{\mathbf u}, \hat{\mathbf n})$. On it $R(\hat{\mathbf n}, \phi)$ fixes $\hat{\mathbf n}$ and sends $\hat{\mathbf u} \mapsto \cos\phi\,\hat{\mathbf u} + \sin\phi\,\hat{\mathbf n}\times\hat{\mathbf u}$, $\hat{\mathbf n}\times\hat{\mathbf u} \mapsto -\sin\phi\,\hat{\mathbf u} + \cos\phi\,\hat{\mathbf n}\times\hat{\mathbf u}$ (because $\hat{\mathbf n}\times(\hat{\mathbf n}\times\hat{\mathbf u}) = -\hat{\mathbf u}$). Its matrix in this basis is $\begin{pmatrix} \cos\phi & -\sin\phi & 0 \\ \sin\phi & \cos\phi & 0 \\ 0 & 0 & 1 \end{pmatrix}$: orthogonal, of determinant $\cos^2\phi + \sin^2\phi = 1$. Orthogonality and the determinant do not depend on the orthonormal basis ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]] for the determinant; $O^{\mathsf T}O = \mathbb 1$ is preserved by orthogonal changes of basis), so $R(\hat{\mathbf n}, \phi) \in SO(3)$.
>
> **2. A one-parameter group.** In the same basis the $2\times2$ blocks multiply by the addition formulas of $\cos$ and $\sin$: $R(\hat{\mathbf n}, \phi)R(\hat{\mathbf n}, \psi) = R(\hat{\mathbf n}, \phi + \psi)$, and $R(\hat{\mathbf n}, 0) = \mathbb 1$. The entries are smooth in $\phi$. So $\phi \mapsto R(\hat{\mathbf n}, \phi)$ is a one-parameter subgroup ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|Def. §CB.1.9]]) and equals $\exp(\phi A)$ with $A = \frac{d}{d\phi}R(\hat{\mathbf n}, \phi)|_{\phi = 0}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]]).
>
> **3. The generator.** Differentiating the defining formula at $\phi = 0$: $A\mathbf V = \hat{\mathbf n}\times\mathbf V_\perp = \hat{\mathbf n}\times\mathbf V$ (the parallel part has zero cross product). Its $i$-th component is $\varepsilon_{ikj}n_kV_j = -\varepsilon_{kij}n_kV_j$, so $(A_{\hat{\mathbf n}})_{ij} = -\varepsilon_{kij}n_k$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]); for $\hat{\mathbf n} = \hat{\mathbf e}_k$, $(A_k)_{lm} = -\varepsilon_{klm}$.
>
> **4. The bracket.** For every $\mathbf V$, $[A_i, A_j]\mathbf V = \hat{\mathbf e}_i\times(\hat{\mathbf e}_j\times\mathbf V) - \hat{\mathbf e}_j\times(\hat{\mathbf e}_i\times\mathbf V) = (\hat{\mathbf e}_i\times\hat{\mathbf e}_j)\times\mathbf V$ (the Jacobi identity of the cross product, from $\mathbf a\times(\mathbf b\times\mathbf c) = \mathbf b(\mathbf a\cdot\mathbf c) - \mathbf c(\mathbf a\cdot\mathbf b)$), and $\hat{\mathbf e}_i\times\hat{\mathbf e}_j = \varepsilon_{ijk}\hat{\mathbf e}_k$. So $[A_i, A_j] = \varepsilon_{ijk}A_k$.
>
> **What the proof shows**
> - The real antisymmetric $A_k$ are a basis of $\mathfrak{so}(3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]); the physicists' generators are $J^k = iA_k$, with $[J^i, J^j] = i\varepsilon^{ijk}J^k$ (Theorem §CB.2.4 below).
> - That every element of $SO(3)$ is some $R(\hat{\mathbf n}, \phi)$, i.e. has an axis, is [[§42 SU(2) → SO(3)꞉ The Double Cover#^lem-42-2|591 Lemma §42.2]].
> - Equivalence: this is [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^thm-c5-1-1|QM Theorem §C5.1.1]], 1–2; QM writes the rotation operators of quantum states, $\mathscr D(R)$, on top of it.

^pf-cb-2-1

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-15|Theorem §CB.0.15]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-9|Def. §CB.1.9]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]]

> [!theorem] Theorem §CB.2.2: The Structure of SU(2)
> 1. Every element of $SU(2)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]]) is
>
> $$
> U(a, b) = \begin{pmatrix} a & b \\ -b^{\ast} & a^{\ast} \end{pmatrix}, \qquad |a|^2 + |b|^2 = 1,
> $$
>
> for unique $a, b \in \mathbb C$; with $a = x_0 + ix_3$, $b = x_2 + ix_1$ the map $U(a, b) \mapsto (x_0, x_1, x_2, x_3)$ is a homeomorphism of $SU(2)$ onto the unit sphere $S^3 \subset \mathbb R^4$. Every element of $U(2)$ is $e^{i\gamma}U(a, b)$ with $\gamma$ real.
> 2. $U(a_1, b_1)\,U(a_2, b_2) = U(a_1a_2 - b_1b_2^{\ast},\ a_1b_2 + a_2^{\ast}b_1)$ and $U(a, b)^{-1} = U(a^{\ast}, -b)$.
> 3. For a unit vector $\hat{\mathbf n}$ and $\phi \in \mathbb R$, with $\boldsymbol\sigma$ of [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-19|Def. §CB.0.19]],
>
> $$
> \exp\Bigl(-\frac{i\phi}{2}\,\hat{\mathbf n}\cdot\boldsymbol\sigma\Bigr) = \cos\frac\phi2\,\mathbb 1 - i\sin\frac\phi2\,\hat{\mathbf n}\cdot\boldsymbol\sigma = U(a, b), \quad \operatorname{Re}a = \cos\frac\phi2,\ \operatorname{Im}a = -n_3\sin\frac\phi2,\ \operatorname{Re}b = -n_2\sin\frac\phi2,\ \operatorname{Im}b = -n_1\sin\frac\phi2 ,
> $$
>
> and every element of $SU(2)$ arises in this way with $0 \le \phi \le 2\pi$.
> 4. At $\phi = 2\pi$ this matrix is $-\mathbb 1$, at $\phi = 4\pi$ it is $+\mathbb 1$.
>
> *Source: Sakurai §3.2.5, eqs. (3.60)–(3.67), and §3.3.2, eqs. (3.76)–(3.84) · the user's series, Part IV, §11–§12, eqs. (spin-rotation), (su2-param), (minus-one) · the user's 511 notes, §"Unitary Unimodular Group" · the course's version: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-5|QM Theorem §C5.2.5]] (parts 1–3), [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-1|QM Theorem §C5.2.1]] (the matrix form of the spin-½ rotation) and [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-3|QM Theorem §C5.2.3]] (part 4), stated there for spin-½ rotation operators.*

^thm-cb-2-2

> [!proof]- Proof
> *Adapted from the derivations of QM Theorems §C5.2.1, §C5.2.3 and §C5.2.5 (Sakurai §3.2.5, §3.3.2); the homeomorphism in part 1 is added.*
>
> **1. The form U(a, b).** The columns of a unitary matrix are orthonormal ([[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]]). If the first column is $(a, c)^{\mathsf T}$ with $|a|^2 + |c|^2 = 1$, the second, a unit vector orthogonal to it in $\mathbb C^2$, is $\lambda(-c^{\ast}, a^{\ast})^{\mathsf T}$ with $|\lambda| = 1$; then $\det U = \lambda(|a|^2 + |c|^2) = \lambda$. So $\det U = 1$ forces $\lambda = 1$, and with $b = -c^{\ast}$ the matrix is $U(a, b)$. Conversely $U(a, b)^\dagger U(a, b) = \mathbb 1$ by multiplication, and $\det U(a, b) = |a|^2 + |b|^2 = 1$. With $a = x_0 + ix_3$, $b = x_2 + ix_1$ the condition is $x_0^2 + x_1^2 + x_2^2 + x_3^2 = 1$. The map to $(x_0, \dots, x_3)$ reads off real and imaginary parts of two entries, and its inverse writes them back into the matrix: both are continuous (linear in the coordinates), so the bijection is a homeomorphism onto $S^3$. For $U \in U(2)$, $|\det U| = 1$ ([[§37 Determinants#^ladr-9-58|LADR Thm. 9.58]]); write $\det U = e^{2i\gamma}$, then $e^{-i\gamma}U \in SU(2)$.
>
> **2. Products and inverses.** Multiply the matrices: the first row of $U(a_1, b_1)U(a_2, b_2)$ is $(a_1a_2 - b_1b_2^{\ast},\ a_1b_2 + b_1a_2^{\ast})$, and the product lies in $SU(2)$ (a group, Def. §CB.1.1), so by step 1 it is $U$ of its first row. $U(a, b)U(a^{\ast}, -b)$ has first row $(aa^{\ast} + bb^{\ast},\ -ab + ba) = (1, 0)$, so it is $\mathbb 1$.
>
> **3. The exponential.** $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2 = \mathbb 1$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 3), so $(\hat{\mathbf n}\cdot\boldsymbol\sigma)^k$ is $\mathbb 1$ for even and $\hat{\mathbf n}\cdot\boldsymbol\sigma$ for odd $k$, and the exponential series ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]]) splits into the series of $\cos\frac\phi2$ and $\sin\frac\phi2$. With $\hat{\mathbf n}\cdot\boldsymbol\sigma = \begin{pmatrix} n_3 & n_1 - in_2 \\ n_1 + in_2 & -n_3\end{pmatrix}$ the result is
>
> $$
> \begin{pmatrix} \cos\frac\phi2 - in_3\sin\frac\phi2 & (-in_1 - n_2)\sin\frac\phi2 \\ (-in_1 + n_2)\sin\frac\phi2 & \cos\frac\phi2 + in_3\sin\frac\phi2 \end{pmatrix} ,
> $$
>
> which is $U(a, b)$ with the stated $a$, $b$ (the lower row is $(-b^{\ast}, a^{\ast})$). Conversely, given $U(a, b)$, choose $\phi \in [0, 2\pi]$ with $\cos\frac\phi2 = \operatorname{Re}a$; then $(\operatorname{Im}a)^2 + |b|^2 = 1 - (\operatorname{Re}a)^2 = \sin^2\frac\phi2$, so for $\sin\frac\phi2 \ne 0$ the vector $\hat{\mathbf n} = -(\operatorname{Im}b, \operatorname{Re}b, \operatorname{Im}a)/\sin\frac\phi2$ is a unit vector satisfying the four equations; for $\sin\frac\phi2 = 0$, $U = \pm\mathbb 1$ and any $\hat{\mathbf n}$ will do.
>
> **4. Two rotations.** At $\phi = 2\pi$, $\cos\pi = -1$ and $\sin\pi = 0$, so the matrix is $-\mathbb 1$; at $\phi = 4\pi$, $\cos2\pi = 1$, $\sin2\pi = 0$.
>
> **What the proof shows**
> - $SU(2)$ is the 3-sphere, and every element lies on a one-parameter subgroup $\phi \mapsto e^{-i\phi\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$; the half angle $\phi/2$ is why the loop $0 \le \phi \le 2\pi$ ends at $-\mathbb 1$ (part 4) → the covering of $SO(3)$, Theorem §CB.2.3.
> - Equivalence: parts 1–3 are QM Theorem §C5.2.5 with the matrix of QM Theorem §C5.2.1, part 4 is QM Theorem §C5.2.3; QM reads the matrices as spin-½ rotation operators acting on spinors.

^pf-cb-2-2

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-1|Def. §CB.1.1]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-4|Def. §CB.1.4]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-19|Def. §CB.0.19]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-57|LADR Thm. 7.57]], [[§37 Determinants#^ladr-9-58|LADR Thm. 9.58]]

> [!theorem] Theorem §CB.2.3: SU(2) Is a Double Cover of SO(3)
> For $U \in SU(2)$ define a linear map $R(U)$ of $\mathbb R^3$ by
>
> $$
> U\,(\mathbf x\cdot\boldsymbol\sigma)\,U^\dagger = \bigl(R(U)\,\mathbf x\bigr)\cdot\boldsymbol\sigma .
> $$
>
> Then
> 1. $R(U) \in SO(3)$, its entries are continuous in $U$, and $R(U_1U_2) = R(U_1)R(U_2)$: $R$ is a continuous homomorphism $SU(2) \to SO(3)$;
> 2. $R\bigl(\exp(-i\phi\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2)\bigr) = R(\hat{\mathbf n}, \phi)$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]]), so $R$ is onto;
> 3. $R(U) = R(U')$ if and only if $U' = \pm U$: the kernel is $\{\mathbb 1, -\mathbb 1\}$, and $SO(3) \cong SU(2)/\{\pm\mathbb 1\}$.
>
> Each rotation corresponds to exactly two elements $\pm U$; the rotation by $2\pi$, the identity of $SO(3)$, corresponds to $-\mathbb 1$ when reached continuously from $U = \mathbb 1$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-2|Theorem §CB.2.2]], 4).
>
> *Source: Sakurai §3.3.2, the paragraph after (3.84) · the user's series, Part IV, §12, eqs. (covering-map), (two-to-one) · the user's 511 notes, §"Relationship Between SO(3) and SU(2)" · the Math version, by conjugation of unit quaternions: [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]] · the course's version: [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]], the same statement.*

^thm-cb-2-3

> [!proof]- Proof
> *Adapted from the derivation of QM Theorem §C5.2.6; the exponential is identified with Theorem §CB.1.10, and the axis of a rotation is quoted from 591.*
>
> **1. R(U) is a real linear map.** $X = \mathbf x\cdot\boldsymbol\sigma$ runs over the traceless Hermitian $2\times2$ matrices as $\mathbf x$ runs over $\mathbb R^3$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], 4). $UXU^\dagger$ is again Hermitian and has the same trace ($U^\dagger = U^{-1}$), so it is $\mathbf x'\cdot\boldsymbol\sigma$ for a unique real $\mathbf x'$, depending linearly on $\mathbf x$. By part 5 of the same theorem its components are $x'_i = \frac12\operatorname{tr}(UXU^\dagger\sigma^i)$, so $R(U)_{ij} = \frac12\operatorname{tr}(U\sigma^jU^\dagger\sigma^i)$, a polynomial in the entries of $U$ and $U^{\ast}$: continuous.
>
> **2. It preserves lengths.** $\det(\mathbf x\cdot\boldsymbol\sigma) = -x_3^2 - (x_1^2 + x_2^2) = -|\mathbf x|^2$, and $\det(UXU^\dagger) = \det X$. So $R(U)$ is orthogonal.
>
> **3. Homomorphism.** $U_1U_2X(U_1U_2)^\dagger = U_1(U_2XU_2^\dagger)U_1^\dagger$, and $R(\mathbb 1) = \mathbb 1$.
>
> **4. Part 2, and det R(U) = 1.** Let $U_\phi = \exp(-i\phi\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2)$, a one-parameter subgroup of $SU(2)$. By step 3, $\phi \mapsto R(U_\phi)$ is a one-parameter subgroup of $O(3)$, smooth in $\phi$ (step 1), so it is $\exp(\phi B)$ with $B$ its derivative at $0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]]). Differentiating $U_\phi XU_\phi^\dagger$ at $\phi = 0$ gives $-\frac i2[\hat{\mathbf n}\cdot\boldsymbol\sigma, \mathbf x\cdot\boldsymbol\sigma] = -\frac i2\cdot2i(\hat{\mathbf n}\times\mathbf x)\cdot\boldsymbol\sigma = (\hat{\mathbf n}\times\mathbf x)\cdot\boldsymbol\sigma$, by the vector form $[\mathbf a\cdot\boldsymbol\sigma, \mathbf b\cdot\boldsymbol\sigma] = 2i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$ (Theorem §CB.0.21, 3). So $B\mathbf x = \hat{\mathbf n}\times\mathbf x = A_{\hat{\mathbf n}}\mathbf x$, and $R(U_\phi) = \exp(\phi A_{\hat{\mathbf n}}) = R(\hat{\mathbf n}, \phi)$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]], 1). Every $U$ is some $U_\phi$ ([[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-2|Theorem §CB.2.2]], 3), so every $R(U)$ is a rotation, of determinant $+1$. Onto: every element of $SO(3)$ is a rotation $R(\hat{\mathbf n}, \phi)$ about some axis ([[§42 SU(2) → SO(3)꞉ The Double Cover#^lem-42-2|591 Lemma §42.2]]), which is $R(U_\phi)$.
>
> **5. Part 3.** $R(U) = \mathbb 1$ means $U\sigma^kU^\dagger = \sigma^k$, i.e. $U$ commutes with $\sigma^1, \sigma^2, \sigma^3$, hence with every $2\times2$ matrix (Theorem §CB.0.21, 4); with the matrix units $E_{12}$, $E_{21}$ this forces $U = \lambda\mathbb 1$, and $\det U = \lambda^2 = 1$ gives $\lambda = \pm1$. Both signs lie in the kernel, so the kernel is $\{\pm\mathbb 1\}$ ([[§15 Homomorphisms#^def-15-3|493 Def. §15.3]]), and $R(U) = R(U')$ iff $U^{-1}U'$ is in the kernel. $SU(2)/\{\pm\mathbb 1\} \cong SO(3)$ is the first isomorphism theorem ([[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]). Finally $U_{\phi + 2\pi} = -U_\phi$ (Theorem §CB.2.2, 3–4): continuing $\phi$ from $0$ to $2\pi$ walks from $\mathbb 1$ to $-\mathbb 1$ while $R(\hat{\mathbf n}, \phi)$ returns to $\mathbb 1$.
>
> **What the proof shows**
> - The half angle of $U_\phi$ becomes the full angle of $R(U_\phi)$ because $U$ acts on $X$ from both sides.
> - Near $U = \mathbb 1$ only $U$ itself, not $-U$, is close to $\mathbb 1$: the two groups are locally isomorphic, with the same Lie algebra (Theorem §CB.2.4 below), and globally different (Theorem §CB.10.8).
> - Equivalence: this is [[§C5.2 Spin One-Half, SU(2), SO(3) and Euler Rotations#^thm-c5-2-6|QM Theorem §C5.2.6]]; 591 proves the same covering as $q \mapsto (v \mapsto qv\bar q)$ on unit quaternions ([[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]]).

^pf-cb-2-3

*Uses:* [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-10|Theorem §CB.1.10]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-2|Theorem §CB.2.2]], [[§42 SU(2) → SO(3)꞉ The Double Cover#^lem-42-2|591 Lemma §42.2]], [[§15 Homomorphisms#^def-15-3|493 Def. §15.3]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|493 Thm. §41.1]]

The rotation case, the course's example (PHY 513 Lecture 7, Part A; the user's PHY 513 notes, Ch. 7 §7.2):

> [!theorem] Theorem §CB.2.4: SO(3) and SU(2) Have the Same Lie Algebra
> $\mathfrak{so}(3)$ is the space of real antisymmetric $3\times3$ matrices and $\mathfrak{su}(2)$ that of traceless anti-Hermitian $2\times2$ matrices; both are three-dimensional, with physicist's bases
>
> $$
> (J^k)_{lm} = -i\varepsilon^{klm}\ \ \text{on } \mathbb C^3, \qquad \tau^k = \tfrac12\sigma^k\ \ \text{on } \mathbb C^2, \qquad [J^i, J^j] = i\varepsilon^{ijk}J^k, \qquad [\tau^i, \tau^j] = i\varepsilon^{ijk}\tau^k .
> $$
>
> The map $-i\tau^k \mapsto -iJ^k$ is an isomorphism of Lie algebras, $\mathfrak{su}(2) \cong \mathfrak{so}(3)$: it is the differential at $\mathbb 1$ of the covering map $SU(2) \to SO(3)$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.2 (Definition "Group, algebra, representation"; Derivation "The representations of the rotation algebra", Examples) · Yu §3.2, eqs. (3.53)–(3.60) · PS §3.1, eqs. (3.11)–(3.14) · Hall, Prop. 16.22, Ex. 16.34*

^thm-cb-2-4

> [!derivation]- Derivation
> **1. The algebra of $SO(3)$.** If $e^{sX} \in SO(3)$ for all $s$, differentiate $(e^{sX})^{\mathsf T}e^{sX} = \mathbb 1$ at $s = 0$ (product rule, $(e^{sX})^{\mathsf T} = e^{sX^{\mathsf T}}$): $X^{\mathsf T} + X = 0$. Conversely, if $X^{\mathsf T} = -X$, then $(e^{sX})^{\mathsf T} = e^{-sX} = (e^{sX})^{-1}$, and $\det e^{sX} = e^{s\operatorname{tr}X} = 1$ because an antisymmetric matrix has zero diagonal. So $\mathfrak{so}(3)$ is the antisymmetric matrices, the tangent space of [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]]; a real antisymmetric $3\times3$ matrix has three free entries.
>
> **2. The algebra of $SU(2)$.** If $e^{sX} \in SU(2)$ for all $s$, differentiating $(e^{sX})^\dagger e^{sX} = \mathbb 1$ gives $X^\dagger = -X$, and $\det e^{sX} = e^{s\operatorname{tr}X} = 1$ for all $s$ forces $\operatorname{tr}X = 0$; the converse is as in step 1. An anti-Hermitian $2\times2$ matrix has four real parameters (two imaginary diagonal entries, one complex off-diagonal entry); zero trace removes one, leaving three. Since $\sigma^1, \sigma^2, \sigma^3$ are Hermitian, traceless and independent ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]), $\{-i\sigma^k/2\}$ is a basis.
>
> **3. Physicist's bases and brackets.** $(J^k)_{lm} = -i\varepsilon^{klm}$ is $i$ times the real antisymmetric matrix $(A_k)_{lm} = -\varepsilon^{klm}$ of [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]], whose bracket $[A_i, A_j] = \varepsilon^{ijk}A_k$ gives $[J^i, J^j] = i^2\varepsilon^{ijk}A_k = i\varepsilon^{ijk}J^k$. For $\tau^k$: $\sigma^i\sigma^j = \delta^{ij}\mathbb 1 + i\varepsilon^{ijk}\sigma^k$ ([[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]]) gives $[\sigma^i, \sigma^j] = i\varepsilon^{ijk}\sigma^k - i\varepsilon^{jik}\sigma^k = 2i\varepsilon^{ijk}\sigma^k$, and dividing by $4$, $[\tau^i, \tau^j] = i\varepsilon^{ijk}\tau^k$. (The Lecture 7 slide "Representations of angular momentum: examples" prints $\sigma^3$ as the identity matrix; $\sigma^3 = \operatorname{diag}(1, -1)$.)
>
> **4. The isomorphism.** The structure constants agree, so the linear bijection $-i\tau^k \mapsto -iJ^k$ preserves brackets. It is the differential of the covering homomorphism $R : SU(2) \to SO(3)$ of [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-3|Theorem §CB.2.3]]: by part 2 there, $R(e^{-i\theta\hat n\cdot\boldsymbol\sigma/2}) = R(\hat n, \theta) = e^{-i\theta\hat n\cdot\mathbf J}$, and differentiating at $\theta = 0$ sends $-i\hat n\cdot\boldsymbol\tau$ to $-i\hat n\cdot\mathbf J$. ⚑ By-product: the algebra, which sees only a neighbourhood of $\mathbb 1$, cannot tell the two groups apart; whether a representation of it belongs to $SO(3)$ or only to $SU(2)$ is a global question → [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-10|Theorem §CB.10.10]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-8|Theorem §CB.10.8]].
>
> **What the derivation shows**
> - Antisymmetry ($SO$) and anti-Hermiticity with zero trace ($SU$) are the linearized defining conditions; the dimension count $3 = 3$ is why the algebras can coincide.
> - The factor $i$ turns real antisymmetric and anti-Hermitian generators into Hermitian ones; it changes no structure constant → [[§CB.4 Real Lie Algebras, the Physicists' i and Complexification#^rem-cb-4-1|Remark: The physicist's i]].
> - The course's computation of the bracket of the $J^k$, with $\hbar$: [[§C5.1 Rotations and the Angular-Momentum Commutation Relations#^ex-c5-1-2|QM Example §C5.1.2]] (moved here from step 3, CB ordering pass).
> - Used next: every representation of either group is a representation of this one algebra ([[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-8|Theorem §CB.3.8]]).

^der-cb-2-4

*Uses:* [[§25 The Geometric Tangent Space#^thm-25-5|591 Thm. §25.5]], [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^thm-cb-0-21|Theorem §CB.0.21]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-1|Theorem §CB.2.1]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-3|Theorem §CB.2.3]]

> [!remark]- Connections
> - **Used in**: Theorem §CB.2.1 — [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-4|Theorem §CB.2.4]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-5|Theorem §CB.5.5]]; Theorem §CB.2.2 — [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-3|Theorem §CB.2.3]], [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-8|Theorem §CB.3.8]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-16|Theorem §CB.7.16]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-21|Theorem §CB.7.21]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-8|Theorem §CB.10.8]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-9|Theorem §CB.10.9]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-10|Theorem §CB.10.10]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-7|Theorem §CB.16.7]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-9|Theorem §CB.16.9]]; Theorem §CB.2.3 — [[§CB.2 SU(2) and SO(3) as Matrix Lie Groups꞉ Structure and the Double Cover#^thm-cb-2-4|Theorem §CB.2.4]], [[§CB.7 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-7-16|Theorem §CB.7.16]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-8|Theorem §CB.10.8]], [[§CB.10 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-10-10|Theorem §CB.10.10]], [[§CB.15 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-15-3|Theorem §CB.15.3]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-9|Theorem §CB.16.9]], [[§CB.16 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Double Cover#^thm-cb-16-10|Theorem §CB.16.10]]; Theorem §CB.2.4 — [[§C3.1 Index Slots, Rotations and Spin in Field Theory|§C3.1]] (embedded).
