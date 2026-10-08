---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: CB
section: CB.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§CB.8 Complex Clifford Algebras and Clifford Modules]] · ↑ [[· CB Lie Groups, Lie Algebras and Representations]] · [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half]] →

*Sources (planned for the proofs; each to be checked against the text when the proof is written): PHY 513 TA (oral remark, Oct 2026) — the centrepiece, Theorem §CB.9.20 · J. Figueroa-O'Farrill, Spin Geometry, lecture notes (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf; not yet checked) · P. Woit, Quantum Theory, Groups and Representations, Ch. 29, §6.2 "Spin groups in three and four dimensions", Ch. 41 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · D. Tong, Lectures on Quantum Field Theory, chapter "The Dirac Equation" (https://www.damtp.cam.ac.uk/user/tong/qft.html) · Peskin & Schroeder, §3.2 · the user's PHY 513 notes, Ch. 8 §8.1 · the rest written here.*

Where do spinors come from? The answer the TA gave, and the one this section states: inside the Clifford algebra of a quadratic space sits a group, $\mathrm{Spin}(V)$, made of products of an even number of unit vectors; it acts on $V$ by conjugation, and that action is a two-to-one cover of $SO(V)$. A Clifford module is therefore automatically a representation of $\mathrm{Spin}(V)$ — and these representations are exactly the spinor representations: they do not descend to $SO(V)$, and every representation that does not descend is found inside spinor ⊗ tensor. The section builds on the Clifford algebra and its modules ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element|§CB.7]], [[§CB.8 Complex Clifford Algebras and Clifford Modules|§CB.8]]) and on coverings ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-23|Theorem §CB.1.23]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]). The three-dimensional case is [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.10]]; the Lorentz case, [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)|§CB.11]]–[[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.12]].

Throughout, $(V, q)$ is a nondegenerate real quadratic space of dimension $n$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]), $\mathrm{Cl} = \mathrm{Cl}(V, q)$ in the convention $vv = +q(v)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^cau-cb-7-1|Caution: Two sign conventions for the Clifford relation]]), $O(V)$ and $SO(V)$ are the linear maps preserving $q$ (with determinant $1$), and $SO(V)_0$ is the identity component ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]]); for $\mathbb R^{1,3}$, $SO(V)_0 = SO^+(1,3)$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]).

## Units, the twisted adjoint action and reflections

> [!definition] Definition §CB.9.1: Group of Units
> The **group of units** $\mathrm{Cl}^\times$ is the set of invertible elements of $\mathrm{Cl}$ under multiplication. Through left multiplication $\mathrm{Cl} \to \operatorname{End}_{\mathbb R}(\mathrm{Cl}) \cong M_{2^n}(\mathbb R)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]) it is a matrix Lie group, an open subset of $\mathrm{Cl}$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · written here*

^def-cb-9-1

> [!theorem] Theorem §CB.9.2: Non-Null Vectors Are Invertible
> If $v \in V$ and $q(v) \ne 0$, then $v \in \mathrm{Cl}^\times$ and $v^{-1} = v/q(v)$.
>
> *Source (planned): written here*

^thm-cb-9-2

> [!proof]- Proof
> $v\cdot\frac{v}{q(v)} = \frac{vv}{q(v)} = \frac{q(v)}{q(v)} = 1$ by the Clifford relation ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-6|Def. §CB.7.6]]), and likewise $\frac{v}{q(v)}\cdot v = 1$.

^pf-cb-9-2

> [!definition] Definition §CB.9.3: Twisted Adjoint Action
> The **twisted adjoint action** of $x \in \mathrm{Cl}^\times$ on $\mathrm{Cl}$ is $\tilde\rho(x)(y) = \alpha(x)\,y\,x^{-1}$, with $\alpha$ the grade automorphism ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-11|Theorem §CB.7.11]]); $\tilde\rho(xy) = \tilde\rho(x)\tilde\rho(y)$. On even $x$ it is ordinary conjugation, $\tilde\rho(x)(y) = xyx^{-1}$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked)*

^def-cb-9-3

> [!theorem] Theorem §CB.9.4: A Vector Acts as the Reflection in Its Orthogonal Hyperplane
> If $u \in V$ with $q(u) \ne 0$, then for every $v \in V$
>
> $$
> \tilde\rho(u)(v) = -u\,v\,u^{-1} = v - 2\,\frac{B(u, v)}{q(u)}\,u \equiv r_u(v),
> $$
>
> the reflection of $V$ in the hyperplane $u^\perp$: $r_u(u) = -u$, $r_u(w) = w$ for $w \perp u$; $r_u \in O(V)$ and $\det r_u = -1$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · written here*

^thm-cb-9-4

> [!proof]- Proof
> **1. The product $uvu$.** By Theorem §CB.7.8, $uv = -vu + 2B(u, v)$. Multiply on the right by $u$: $uvu = -vuu + 2B(u, v)u = -q(u)\,v + 2B(u, v)\,u$.
>
> **2. Divide by $q(u)$.** With $u^{-1} = u/q(u)$ (Theorem §CB.9.2), $uvu^{-1} = \frac{uvu}{q(u)} = -v + 2\frac{B(u, v)}{q(u)}u$. Since $\alpha(u) = -u$, $\tilde\rho(u)(v) = -uvu^{-1} = v - 2\frac{B(u, v)}{q(u)}u$.
>
> **3. Reflection.** For $v = u$: $u - 2\frac{q(u)}{q(u)}u = -u$. For $w$ with $B(u, w) = 0$: $r_u(w) = w$. Since $u \notin u^\perp$ ($B(u, u) = q(u) \ne 0$), $V = \mathbb Ru \oplus u^\perp$, so $r_u$ is $-1$ on a line and $+1$ on a complementary hyperplane: $\det r_u = -1$. It preserves $q$: $q(r_uv) = q(v) - 4\frac{B(u, v)}{q(u)}B(u, v) + 4\frac{B(u, v)^2}{q(u)^2}q(u) = q(v)$.

^pf-cb-9-4

## Pin and Spin

> [!definition] Definition §CB.9.5: The Pin Group
> $\mathrm{Pin}(V)$ is the set of products $u_1u_2\cdots u_k \in \mathrm{Cl}$ ($k \ge 0$) of vectors $u_i \in V$ with $q(u_i) = \pm1$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked)*

^def-cb-9-5

> [!definition] Definition §CB.9.6: The Spin Group
> $\mathrm{Spin}(V) = \mathrm{Pin}(V)\cap\mathrm{Cl}^0$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-5|Def. §CB.9.5]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]): the products of an *even* number of vectors $u_i$ with $q(u_i) = \pm1$. $\mathrm{Spin}(V)_0$ denotes its identity component; $\mathrm{Spin}(r, s) = \mathrm{Spin}(\mathbb R^{r,s})$, $\mathrm{Spin}(n) = \mathrm{Spin}(n, 0)$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · Woit, §6.2*

^def-cb-9-6

> [!theorem] Theorem §CB.9.7: Pin and Spin Are Matrix Lie Groups Acting on V
> 1. $\mathrm{Pin}(V)$ and $\mathrm{Spin}(V)$ are subgroups of $\mathrm{Cl}^\times$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-1|Def. §CB.9.1]]), with $(u_1\cdots u_k)^{-1} = \pm\,u_k\cdots u_1$, and closed, hence matrix Lie groups.
> 2. $\rho(x) = \tilde\rho(x)|_V$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-3|Def. §CB.9.3]]) maps $V$ to $V$ and defines a Lie group homomorphism $\rho : \mathrm{Pin}(V) \to O(V)$; on $\mathrm{Spin}(V)$, $\rho(x)v = xvx^{-1}$, and $\rho(u_1\cdots u_k) = r_{u_1}\cdots r_{u_k}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]]).
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked)*

^thm-cb-9-7

> [!proof]- Proof (to be filled)
> *To be filled (part 1: closure under products is the definition; inverses from Theorem §CB.9.2; closedness via a characterization of $\mathrm{Pin}$ by $\tilde\rho(x)V \subset V$ and the spinor norm, Theorem §CB.9.9; part 2 from Theorem §CB.9.4).*

^pf-cb-9-7

> [!definition] Definition §CB.9.8: Spinor Norm
> The **spinor norm** of $x \in \mathrm{Cl}$ is $N(x) = x\,t(x)$, with $t$ the reversal ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-14|Theorem §CB.7.14]]).
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked)*

^def-cb-9-8

> [!theorem] Theorem §CB.9.9: The Spinor Norm on Pin
> For $x = u_1\cdots u_k \in \mathrm{Pin}(V)$, $N(x) = q(u_1)\cdots q(u_k) \in \{\pm1\}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-8|Def. §CB.9.8]]); $N$ is a continuous homomorphism $\mathrm{Pin}(V) \to \{\pm1\}$, and $N = 1$ on $\mathrm{Spin}(V)_0$.
>
> *Source (planned): written here*

^thm-cb-9-9

> [!proof]- Proof
> **1. The value.** $t(u_1\cdots u_k) = u_k\cdots u_1$, so $N(x) = u_1\cdots u_{k-1}(u_ku_k)u_{k-1}\cdots u_1 = q(u_k)\,u_1\cdots u_{k-1}u_{k-1}\cdots u_1$, and repeating, $N(x) = q(u_k)q(u_{k-1})\cdots q(u_1)$, a product of numbers $\pm1$.
>
> **2. Homomorphism.** For $x, y \in \mathrm{Pin}(V)$, $N(xy) = xy\,t(y)t(x) = x\,N(y)\,t(x) = N(y)N(x)$, because $N(y)$ is a real number and commutes with everything.
>
> **3. Continuity and the identity component.** $N$ is the restriction of the continuous map $x \mapsto x\,t(x)$ on $\mathrm{Cl}$. A continuous map from the path-connected $\mathrm{Spin}(V)_0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]]) into $\{\pm1\}$ is constant, and $N(1) = 1$.

^pf-cb-9-9

## The double cover

> [!theorem] Theorem §CB.9.10: Cartan–Dieudonné
> Every element of $O(V)$ is a product of at most $n = \dim V$ reflections $r_u$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]]) with $q(u) \ne 0$; the elements of $SO(V)$ are the products of an even number of them.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · stated here for general $V$; the two cases the course needs are reached directly ($SU(2) \to SO(3)$: [[§41 SU(2) → SO(3)꞉ The Double Cover#^thm-41-4|591 Thm. §41.4]]; $SL(2, \mathbb C) \to SO^+(1,3)$: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]])*

^thm-cb-9-10

> [!proof]- Proof (to be filled)
> *To be filled (induction on $n$: for $R \in O(V)$ and a non-null $v$, either $Rv - v$ or $Rv + v$ is non-null, and one reflection reduces to $R$ fixing $v$).*

^pf-cb-9-10

> [!theorem] Theorem §CB.9.11: Spin(V) → SO(V) Is Onto with Kernel ±1
> $\rho(\mathrm{Pin}(V)) = O(V)$ and $\rho(\mathrm{Spin}(V)) = SO(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]]), and $\ker\rho = \{1, -1\}$ on both: $\rho(x) = \rho(y)$ iff $y = \pm x$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked)*

^thm-cb-9-11

> [!proof]- Proof (to be filled)
> *To be filled (onto: Theorem §CB.9.10, rescaling each $u$ to $q(u) = \pm1$; kernel on $\mathrm{Spin}$: an even $x$ commuting with every $v$ is central and even, hence real, [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], 4, and $N(x) = x^2 = \pm1$ gives $x = \pm1$).*

^pf-cb-9-11

> [!theorem] Theorem §CB.9.12: The Identity Component Is a Double Cover
> If $n \ge 3$ (more generally, if $V$ contains a two-dimensional subspace on which $q$ is definite), then $-1 \in \mathrm{Spin}(V)_0$ and $\rho : \mathrm{Spin}(V)_0 \to SO(V)_0$ is a surjective two-to-one Lie group homomorphism and a covering map ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-23|Theorem §CB.1.23]]) with kernel $\{\pm1\}$. For $n \ge 3$ and $V$ definite, $\mathrm{Spin}(n)$ is connected and simply connected, the universal covering group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]) of $SO(n)$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · Woit, §6.2 (n = 3, 4)*

^thm-cb-9-12

> [!proof]- Proof (to be filled)
> *To be filled ($-1$: for orthonormal $e_1$, $e_2$ spanning a definite plane, $(e_1e_2)^2 = -1$, and $s \mapsto \cos s + \sin s\,e_1e_2 = e^{se_1e_2}$ joins $1$ to $-1$ at $s = \pi$ inside $\mathrm{Spin}(V)$; covering from Theorem §CB.9.14 and Theorem §CB.1.23; simple connectivity of $\mathrm{Spin}(n)$ to be filled).*

^pf-cb-9-12

## The Lie algebra 𝔰𝔭𝔦𝔫(V)

> [!definition] Definition §CB.9.13: The Spin Lie Algebra
> $\mathfrak{spin}(V) \subset \mathrm{Cl}^0$ is the span of the products $e_ie_j$ ($i < j$) for an orthogonal basis of $V$; equivalently the span of all commutators $[v, w] = vw - wv$, $v, w \in V$; equivalently the image of $\Lambda^2V$ under [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-17|Theorem §CB.7.17]]. Its dimension is $n(n-1)/2$.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · Woit, Ch. 29*

^def-cb-9-13

> [!theorem] Theorem §CB.9.14: 𝔰𝔭𝔦𝔫(V) Is the Lie Algebra of Spin(V), Isomorphic to 𝔰𝔬(V)
> 1. $\mathfrak{spin}(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]]) is closed under the commutator and is the Lie algebra ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]) of $\mathrm{Spin}(V)$ inside $\mathrm{Cl}$.
> 2. The differential of $\rho$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]) is $\rho_\ast(X)(v) = [X, v]$, and for an orthogonal basis
>
> $$
> \rho_\ast\bigl(\tfrac12e_ie_j\bigr)(v) = B(e_j, v)\,e_i - B(e_i, v)\,e_j \qquad (i \ne j) .
> $$
>
> 3. $\rho_\ast : \mathfrak{spin}(V) \to \mathfrak{so}(V)$ is an isomorphism of Lie algebras.
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · the Minkowski case: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]*

^thm-cb-9-14

> [!proof]- Proof (to be filled)
> *To be filled (part 2: $[e_ie_j, v] = 2B(e_j, v)e_i - 2B(e_i, v)e_j$ by moving $v$ through with Theorem §CB.7.8; part 3: injective by part 2, dimensions $n(n-1)/2$ agree).*

^pf-cb-9-14

The course's spinor generators and their two theorems, the Minkowski case of Theorem §CB.9.14 in the physicists' normalization $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac i2\gamma(e_\mu e_\nu)$ ($\mu \ne \nu$, for the module with $e_\mu \mapsto \gamma^\mu$), in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]:

![[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1]]

![[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1]]

![[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2]]

> [!theorem] Theorem §CB.9.15: The Even Subalgebra Is Generated by 𝔰𝔭𝔦𝔫(V)
> Every element of $\mathrm{Cl}^0$ is a linear combination of $1$ and products of elements of $\mathfrak{spin}(V)$. Hence a subspace of a Clifford module is invariant under $\mathrm{Cl}^0$ iff it is invariant under $\mathfrak{spin}(V)$, iff (Theorem §C3.1.2, 2, as $\mathrm{Spin}(V)_0$ is connected) it is invariant under $\mathrm{Spin}(V)_0$.
>
> *Source (planned): written here*

^thm-cb-9-15

> [!proof]- Proof
> **1. Basis of the even part.** By Theorem §CB.7.16, $\mathrm{Cl}^0$ has the basis $e_I$ with $|I| = 2k$ even, $I = \{i_1 < i_2 < \cdots < i_{2k}\}$.
>
> **2. Pairing.** $e_I = (e_{i_1}e_{i_2})(e_{i_3}e_{i_4})\cdots(e_{i_{2k-1}}e_{i_{2k}})$, a product of $k$ elements $e_ie_j$ ($i < j$) of $\mathfrak{spin}(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]]); for $k = 0$, $e_\varnothing = 1$. So the algebra generated by $1$ and $\mathfrak{spin}(V)$ contains a basis of $\mathrm{Cl}^0$, hence equals $\mathrm{Cl}^0$ (it is contained in $\mathrm{Cl}^0$ by [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]]).
>
> **3. Invariant subspaces.** A subspace invariant under each $\gamma(X)$, $X \in \mathfrak{spin}(V)$, is invariant under their products and sums, hence under $\gamma(\mathrm{Cl}^0)$; the converse is immediate. The passage between $\mathfrak{spin}(V)$ and the connected group $\mathrm{Spin}(V)_0$ is [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-2|Theorem §C3.1.2]], 2, applied to the representation $x \mapsto \gamma(x)$ of $\mathrm{Spin}(V)_0$ whose differential is $\gamma|_{\mathfrak{spin}(V)}$ (Theorem §CB.9.14, 1).

^pf-cb-9-15

## Invariant Hermitian forms

> [!theorem] Theorem §CB.9.16: Spin Preserves a Form for Which the Clifford Generators Are Self-Adjoint
> Let $\gamma$ be a complex Clifford module of $(V, q)$ on $W$ and $h$ a nondegenerate Hermitian form on $W$ for which every $\gamma(v)$, $v \in V$, is $h$-self-adjoint ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-2|Def. §CB.5.2]]). Then for $x \in \mathrm{Pin}(V)$
>
> $$
> h(\gamma(x)\chi, \gamma(x)\psi) = N(x)\,h(\chi, \psi)
> $$
>
> ($N$ of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-8|Def. §CB.9.8]]); in particular $\gamma(\mathrm{Spin}(V)_0) \subset U(W, h)$ ([[§CB.5 Hermitian Forms, Signature and Pseudo-Unitary Groups#^def-cb-5-4|Def. §CB.5.4]]).
>
> *Source (planned): written here · the Dirac case: [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]]*

^thm-cb-9-16

> [!proof]- Proof
> For $x = u_1\cdots u_k$, $\gamma(x)^{\dagger_h} = \gamma(u_k)^{\dagger_h}\cdots\gamma(u_1)^{\dagger_h} = \gamma(u_k)\cdots\gamma(u_1) = \gamma(t(x))$ by Theorem §CB.5.3, 2 and self-adjointness. Hence $h(\gamma(x)\chi, \gamma(x)\psi) = h(\chi, \gamma(t(x))\gamma(x)\psi) = h(\chi, \gamma(t(x)x)\psi)$. Now $t(x)x = u_k\cdots u_1u_1\cdots u_k = q(u_1)\cdots q(u_k) = N(x)$ by the computation of Theorem §CB.9.9, step 1 (read from the inside out). So the right side is $N(x)h(\chi, \psi)$, and $N = 1$ on $\mathrm{Spin}(V)_0$ (Theorem §CB.9.9).

^pf-cb-9-16

## Spinor representations and the TA's theorem

> [!definition] Definition §CB.9.17: Spinorial and Tensorial Representations
> Let $\mathrm{Spin}(V)_0$ contain $-1$ (Theorem §CB.9.12). A representation $D$ of $\mathrm{Spin}(V)_0$ is **tensorial** if $D(-1) = \mathbb 1$ (equivalently, [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]], it comes from a representation of $SO(V)_0$) and **spinorial** if $D(-1) = -\mathbb 1$. For the Lorentz group these are the course's tensor and spinor representations ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]]), detected by the rotation through $2\pi$.
>
> *Source (planned): written here*

^def-cb-9-17

> [!definition] Definition §CB.9.18: Spinor Representation
> The **spinor representation** of $\mathrm{Spin}(V)$ is the restriction $x \mapsto \gamma(x)$ of an irreducible complex Clifford module $\gamma$ on $S$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]]) to $\mathrm{Spin}(V) \subset \mathrm{Cl}$; for $n$ even, the **half-spin representations** are its restrictions to $S^\pm$, the $\pm1$ eigenspaces of $\omega_{\mathbb C}$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-10|Theorem §CB.8.10]]). Its differential is $\gamma|_{\mathfrak{spin}(V)}$ (Theorem §CB.9.14).
>
> *Source (planned): Figueroa-O'Farrill, Spin Geometry (to be checked) · Woit, Ch. 31, Ch. 41*

^def-cb-9-18

> [!theorem] Theorem §CB.9.19: Every Representation Splits into a Tensorial and a Spinorial Part
> Every finite-dimensional representation $W$ of $\mathrm{Spin}(V)_0$ is $W = W_+\oplus W_-$ with $W_\pm = \{w : D(-1)w = \pm w\}$ invariant, $W_+$ tensorial and $W_-$ spinorial ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]]); an irreducible representation is one or the other.
>
> *Source (planned): written here · the Lorentz case: [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]]*

^thm-cb-9-19

> [!proof]- Proof
> **1. Projections.** $P = D(-1)$ satisfies $P^2 = D((-1)^2) = D(1) = \mathbb 1$. Put $P_\pm = \frac12(\mathbb 1 \pm P)$: $P_+ + P_- = \mathbb 1$, $P_\pm^2 = \frac14(\mathbb 1 \pm 2P + P^2) = \frac14(2\mathbb 1 \pm 2P) = P_\pm$, and $P_+P_- = \frac14(\mathbb 1 - P^2) = 0$. So $W = P_+W\oplus P_-W$, and $PP_\pm = \pm P_\pm$ shows $P_\pm W = W_\pm$.
>
> **2. Invariance.** $-1$ is central in $\mathrm{Spin}(V)_0$ (it is a real number in $\mathrm{Cl}$), so $D(g)P = PD(g)$ and $D(g)$ maps each eigenspace of $P$ into itself.
>
> **3. Irreducible case.** If $W$ is irreducible, one of the invariant subspaces $W_\pm$ is $0$ and the other is $W$.

^pf-cb-9-19

The course's definition and theorem for the Lorentz group, in [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra|§C3.3]]:

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2]]

![[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6]]

> [!theorem] Theorem §CB.9.20: The TA's Theorem — Clifford Modules Restricted to Spin Are Exactly the Spinor Representations, and Every Spinorial Representation Lies in Spinor ⊗ Tensor
> Let $(V, q)$ be nondegenerate real with $n = \dim V \ge 3$, and $S$ an irreducible complex Clifford module.
> 1. **Restriction.** The spinor representation $S|_{\mathrm{Spin}(V)_0}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-18|Def. §CB.9.18]]) is spinorial ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]]): $-1 \in \mathrm{Spin}(V)_0$ acts as $-\mathbb 1$, so it is not a representation of $SO(V)_0$. For $n$ odd it is irreducible of dimension $2^{(n-1)/2}$; for $n$ even, $S = S^+\oplus S^-$ with $S^\pm$ irreducible, inequivalent, of dimension $2^{n/2-1}$, and $\gamma(v)$ maps $S^\pm$ to $S^\mp$.
> 2. **Exactly the spinor representations.** Up to equivalence, the irreducible representations of $\mathrm{Spin}(V)_0$ obtained by restricting Clifford modules — that is, the irreducible representations of $\mathfrak{spin}(V)$ that extend to representations of the algebra $\mathrm{Cl}^0$ — are exactly $S$ ($n$ odd), resp. $S^+$ and $S^-$ ($n$ even); every finite-dimensional Clifford module restricts to a direct sum of copies of them.
> 3. **Spinor ⊗ tensor.** Every finite-dimensional spinorial representation of $\mathrm{Spin}(V)_0$ is equivalent to a subrepresentation of $S\otimes T$ for a tensorial representation $T$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]); $T$ can be taken inside a tensor power $(V_{\mathbb C})^{\otimes k}$ of the complexified vector representation, $x \mapsto \rho(x)$.
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · planned for the proofs: Figueroa-O'Farrill, Spin Geometry (to be checked); highest-weight theory for part 3 in general (not developed in CB) · the cases proved in CB: $n = 3$, Theorem §CB.10.6; $\mathbb R^{1,3}$, Theorem §CB.12.9*

^thm-cb-9-20

> [!proof]- Proof (to be filled)
> *Parts 1–2 to be filled from Theorem §CB.8.10 and Theorem §CB.9.15 (invariant subspaces of $\mathrm{Spin}(V)_0$ are those of $\mathrm{Cl}^0$), with $-1 \mapsto \gamma(-1) = -\mathbb 1$. Part 3 in general needs highest weights of $\mathfrak{so}(n, \mathbb C)$; it is proved in CB only for the two cases the course uses (Theorems §CB.10.6 and §CB.12.9), by the Clebsch–Gordan series.*

^pf-cb-9-20

> [!theorem] Theorem §CB.9.21: Clifford Multiplication Is Spin-Equivariant
> For a Clifford module $\gamma$ on $W$, $x \in \mathrm{Spin}(V)$ and $v \in V$:
>
> $$
> \gamma(x)\,\gamma(v)\,\gamma(x)^{-1} = \gamma\bigl(\rho(x)v\bigr) .
> $$
>
> So the map $V\otimes W \to W$, $v\otimes w \mapsto \gamma(v)w$, is an intertwiner ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]) from $\rho\otimes\gamma|_{\mathrm{Spin}}$ to $\gamma|_{\mathrm{Spin}}$; equivalently $\gamma \in V'\otimes\operatorname{End}(W)$ is an invariant tensor ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-10|Def. §CB.4.10]]). For $n$ even it maps $V\otimes S^\pm$ to $S^\mp$.
>
> *Source (planned): written here · the Dirac case: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]]*

^thm-cb-9-21

> [!proof]- Proof
> $\gamma$ is an algebra homomorphism, so $\gamma(x)\gamma(v)\gamma(x)^{-1} = \gamma(xvx^{-1})$, and $xvx^{-1} = \rho(x)v$ for even $x$ (Theorem §CB.9.7, 2). For $v\otimes w$: $\gamma(x)\bigl(\gamma(v)w\bigr) = \gamma(\rho(x)v)\gamma(x)w$, which is the intertwining property. For $n$ even, $\gamma(v)$ maps $S^\pm$ to $S^\mp$ because $\omega_{\mathbb C}$ anticommutes with $v$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], 3).

^pf-cb-9-21

> [!remark] Remark: What the TA's theorem explains
> The course meets spinors three times: as the space on which the Dirac matrices act (C5a.1), as the representation $(\frac12, 0)\oplus(0, \frac12)$ of the Lorentz algebra (C5a.3), and as the two-valued representations of $SO^+(1,3)$ (C3.3, C5a.4). Theorem §CB.9.20 says these are one object: the Clifford module *is* a representation of the group $\mathrm{Spin}$, generated by $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$ (Theorem §CB.9.14), it is two-valued on $SO$ because $-1 \in \mathrm{Spin}$ acts as $-1$ (Theorem §CB.9.12), and every other two-valued representation is a spinor index together with tensor indices — Rarita–Schwinger's $\psi_\mu$ being the first example beyond Dirac.

^rem-cb-9-1

> [!remark]- Connections
> - The reflections of Theorem §CB.9.4 are the Clifford form of the parity and time-reversal matrices: a single vector $e_0$ or $e_i$ acts as a reflection, which is why discrete Lorentz transformations act on spinors by single $\gamma$ matrices ([[§C9.1 Discrete Lorentz Transformations#^def-c9-1-2|Def. §C9.1.2]]; [[§C9.3 Parity on States, Spinors and the Dirac Field|§C9.3]]).
> - Theorem §CB.9.16 explains why $\bar\psi\psi$ is a scalar while $\psi^\dagger\psi$ is not: the Dirac form makes $\gamma(v)$ self-adjoint and is therefore preserved by $\mathrm{Spin}(1,3)_0$, whereas no positive form is ([[§C5a.6 The Dirac Conjugate and the Bilinears#^rem-c5a-6-1|§C5a.6, Remark: Why ψ†ψ is not a scalar]]).
> - **Used in**: Theorems §CB.9.4–§CB.9.11 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C9.1 Discrete Lorentz Transformations#^def-c9-1-2|Def. §C9.1.2]]; Theorem §CB.9.12 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.9.14 — [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-1|Def. §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^def-c5a-3-2|Def. §C5a.3.2]]; Theorem §CB.9.16 — [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-1|Theorem §C5a.6.1]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]; Definition §CB.9.17–Theorem §CB.9.19 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-2|Def. §C3.3.2]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.4 How Fields Transform under the Lorentz Group#^def-c3-4-2|Def. §C3.4.2]]; Theorem §CB.9.20 — [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-4|Theorem §C5a.3.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.0 Why Spinors꞉ the Square Root of the Klein–Gordon Equation#^rem-c5a-0-5|§C5a.0, Remark: The structure of spinor space, layer by layer]]; Theorem §CB.9.21 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-4|Def. §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-11|Theorem §C5a.4.11]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-12|Theorem §C5a.4.12]].
