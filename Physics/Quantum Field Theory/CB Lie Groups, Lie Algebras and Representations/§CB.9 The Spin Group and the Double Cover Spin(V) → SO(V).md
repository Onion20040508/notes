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

*Sources: PHY 513 TA (oral remark, Oct 2026) — the centrepiece, Theorem §CB.9.20 · E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes, University of Toronto, Fall 2009, Ch. 1 §§4, 6 and Ch. 2 §4 (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf; convention as here) · J. Figueroa-O'Farrill, Spin Geometry, lecture notes, Edinburgh 2010, version of 18 May 2017, Lecture 3 (https://empg.maths.ed.ac.uk/Activities/Spin/SpinNotes.pdf, read via the Internet Archive copy of 27 Sep 2024; convention $x^2 = -Q(x)$) · P. Woit, Quantum Theory, Groups and Representations, §6.2, §29.2 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · A. Hatcher, Algebraic Topology, Thm. 4.41, Prop. 4.48 (https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) · H. Georgi, Lie Algebras in Particle Physics, 2nd ed., §8.12, Ch. 21–23 · D. Tong, Lectures on Quantum Field Theory, chapter "The Dirac Equation" (https://www.damtp.cam.ac.uk/user/tong/qft.html) · Peskin & Schroeder, §3.2 · the user's PHY 513 notes, Ch. 8 §8.1 · the rest written here.*

Where do spinors come from? The answer the TA gave, and the one this section states: inside the Clifford algebra of a quadratic space sits a group, $\mathrm{Spin}(V)$, made of products of an even number of unit vectors; it acts on $V$ by conjugation, and that action is a two-to-one cover of $SO(V)$. A Clifford module is therefore automatically a representation of $\mathrm{Spin}(V)$ — and these representations are exactly the spinor representations: they do not descend to $SO(V)$, and every representation that does not descend is found inside spinor ⊗ tensor. The section builds on the Clifford algebra and its modules ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element|§CB.7]], [[§CB.8 Complex Clifford Algebras and Clifford Modules|§CB.8]]) and on coverings ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-23|Theorem §CB.1.23]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]). The three-dimensional case is [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.10]]; the Lorentz case, [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)|§CB.11]]–[[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵|§CB.12]].

Throughout, $(V, q)$ is a nondegenerate real quadratic space of dimension $n$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]), $\mathrm{Cl} = \mathrm{Cl}(V, q)$ in the convention $vv = +q(v)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^cau-cb-7-1|Caution: Two sign conventions for the Clifford relation]]), $O(V)$ and $SO(V)$ are the linear maps preserving $q$ (with determinant $1$), and $SO(V)_0$ is the identity component ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]]); for $\mathbb R^{1,3}$, $SO(V)_0 = SO^+(1,3)$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]).

## Units, the twisted adjoint action and reflections

> [!definition] Definition §CB.9.1: Group of Units
> The **group of units** $\mathrm{Cl}^\times$ is the set of invertible elements of $\mathrm{Cl}$ under multiplication. Through left multiplication $\mathrm{Cl} \to \operatorname{End}_{\mathbb R}(\mathrm{Cl}) \cong M_{2^n}(\mathbb R)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]) it is a matrix Lie group, an open subset of $\mathrm{Cl}$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §4.1 (the group $\mathrm{Cl}(V)^\times$) · written here*

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
> *Source: Figueroa-O'Farrill, Spin Geometry, §3.2, after eq. (61) (the twisted adjoint action) · Meinrenken, Clifford Algebras and Lie Groups, Def. 4.1 ($A_x(v) = \Pi(x)vx^{-1}$)*

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
> *Source: Figueroa-O'Farrill, Spin Geometry, eq. (61) · Meinrenken, Clifford Algebras and Lie Groups, proof of Thm. 4.2 ($A_v = R_v$) · Woit, §29.2.1*

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
> *Source: Figueroa-O'Farrill, Spin Geometry, Def. 3.1 · Meinrenken, Clifford Algebras and Lie Groups, Def. 4.3*

^def-cb-9-5

> [!definition] Definition §CB.9.6: The Spin Group
> $\mathrm{Spin}(V) = \mathrm{Pin}(V)\cap\mathrm{Cl}^0$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-5|Def. §CB.9.5]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-12|Def. §CB.7.12]]): the products of an *even* number of vectors $u_i$ with $q(u_i) = \pm1$. $\mathrm{Spin}(V)_0$ denotes its identity component; $\mathrm{Spin}(r, s) = \mathrm{Spin}(\mathbb R^{r,s})$, $\mathrm{Spin}(n) = \mathrm{Spin}(n, 0)$.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, Def. 3.4 · Woit, §29.2.1 (Definition of $\mathrm{Spin}(n)$), §6.2*

^def-cb-9-6

> [!theorem] Theorem §CB.9.7: Pin and Spin Are Matrix Lie Groups Acting on V
> 1. $\mathrm{Pin}(V)$ and $\mathrm{Spin}(V)$ are subgroups of $\mathrm{Cl}^\times$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-1|Def. §CB.9.1]]), with $(u_1\cdots u_k)^{-1} = \pm\,u_k\cdots u_1$, and closed, hence matrix Lie groups.
> 2. $\rho(x) = \tilde\rho(x)|_V$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-3|Def. §CB.9.3]]) maps $V$ to $V$ and defines a Lie group homomorphism $\rho : \mathrm{Pin}(V) \to O(V)$; on $\mathrm{Spin}(V)$, $\rho(x)v = xvx^{-1}$, and $\rho(u_1\cdots u_k) = r_{u_1}\cdots r_{u_k}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]]).
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Def. 4.1, Thm. 4.2, Def. 4.3 · Figueroa-O'Farrill, Spin Geometry, §3.2*

^thm-cb-9-7

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 2 §4.1, Def. 4.1, Thm. 4.2 and its proof, Def. 4.3 (the Clifford group $\Gamma(V) = \{x \in \mathrm{Cl}^\times : \Pi(x)vx^{-1} \in V\}$, the computation $A_x \in O(V)$, Cartan–Dieudonné for surjectivity, and $\mathrm{Pin}$ as the norm $\pm1$ part; https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf) · J. Figueroa-O'Farrill, Spin Geometry, §3.2, Def. 3.1, eq. (61) and the kernel argument before Prop. 3.3. Steps 1 and 7 written here.*
>
> **Step 1** (subgroups). Products of elements of $\mathrm{Pin}(V)$ are again products of unit vectors, and $1$ is the empty product. For $q(u) = \pm1$, $u^{-1} = u/q(u) = q(u)\,u$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-2|Theorem §CB.9.2]]), so
>
> $$
> (u_1\cdots u_k)^{-1} = u_k^{-1}\cdots u_1^{-1} = q(u_1)\cdots q(u_k)\;u_k\cdots u_1 = \pm\,u_k\cdots u_1,
> $$
>
> again in $\mathrm{Pin}(V)$ (a sign is absorbed by $u_k \mapsto -u_k$, and $q(-u_k) = q(u_k)$). $\mathrm{Cl}^0$ is closed under products ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]]), and the inverse $\pm u_k\cdots u_1 = \pm t(x)$ of an even $x$ is even since $t$ commutes with $\alpha$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-14|Theorem §CB.7.14]]). So $\mathrm{Pin}(V)$ and $\mathrm{Spin}(V)$ are subgroups of $\mathrm{Cl}^\times$.
>
> **Step 2** (the action on $V$). $\tilde\rho$ is multiplicative ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-3|Def. §CB.9.3]]: $\alpha(xy)\,z\,(xy)^{-1} = \alpha(x)\bigl(\alpha(y)zy^{-1}\bigr)x^{-1}$), and $\tilde\rho(u)|_V = r_u$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]]). Hence $\rho(u_1\cdots u_k) = r_{u_1}\cdots r_{u_k}$ maps $V$ to $V$, lies in $O(V)$, and $\rho$ is a homomorphism $\mathrm{Pin}(V) \to O(V)$. On $\mathrm{Spin}(V)$, $\alpha(x) = x$ and $\rho(x)v = xvx^{-1}$. $\rho$ is continuous: $x \mapsto x^{-1}$ is continuous on $\mathrm{Cl}^\times$ (it is matrix inversion under left multiplication, [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-1|Def. §CB.9.1]]) and $(x, v) \mapsto \alpha(x)vx^{-1}$ is built from products and the linear map $\alpha$. So $\rho$ is a Lie group homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]) once the groups are known to be matrix Lie groups (Step 7).
>
> **Step 3** (the twisted action of a general element preserving $V$ is orthogonal). Let $x \in \mathrm{Cl}^\times$ with $A_x(v) := \alpha(x)vx^{-1} \in V$ for all $v \in V$. Applying $\alpha$ to $A_x(v) \in V$ gives $-A_x(v) = x(-v)\alpha(x)^{-1}$, i.e. $A_x(v) = xv\,\alpha(x)^{-1}$. Using the first form for the left factor and the second for the right factor,
>
> $$
> 2B(A_xv, A_xw) = A_x(v)A_x(w) + A_x(w)A_x(v) = \alpha(x)\,vx^{-1}x\,w\,\alpha(x)^{-1} + \alpha(x)\,wx^{-1}x\,v\,\alpha(x)^{-1} = \alpha(x)(vw + wv)\alpha(x)^{-1} = 2B(v, w),
> $$
>
> by [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]] (the scalar $2B(v, w)$ commutes with $\alpha(x)$). So $A_x \in O(V)$; and $A_{xy} = A_xA_y$ as in Step 2.
>
> **Step 4** (kernel lemma). Let $z \in \mathrm{Cl}^\times$ with $A_z = \mathbb 1$, i.e. $\alpha(z)v = vz$ for all $v$. Write $z = z_0 + z_1$ (even and odd parts, Theorem §CB.7.13), so $\alpha(z) = z_0 - z_1$, and
>
> $$
> z_0v - z_1v = vz_0 + vz_1 .
> $$
>
> $z_0v$ and $vz_0$ are odd, $z_1v$ and $vz_1$ even, so the odd and even parts give separately $z_0v = vz_0$ and $z_1v = -vz_1$ for all $v$. Then $z_0$ commutes with the generators, hence with $\mathrm{Cl}$, and is even, so $z_0 = \lambda1$, $\lambda \in \mathbb R$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], 4). And $z_1$ anticommutes with every $e_j$: by the sign table of Step 4 in the proof of Theorem §CB.7.19, conjugation by $e_j$ multiplies $e_I$ by $\varepsilon_j(I)$, and for $|I|$ odd and $j \in I$, $\varepsilon_j(I) = (-1)^{|I|-1} = +1$; so every coefficient of $z_1$ on a nonempty $I$ vanishes, and $z_1 = 0$ (an odd element has no $e_\varnothing$ component). Hence $z = \lambda1$ with $\lambda \ne 0$.
>
> **Step 5** (characterization of $\mathrm{Pin}$). Claim: $\mathrm{Pin}(V) = \{x \in \mathrm{Cl}^\times : A_x(V) \subset V,\ x\,t(x) \in \{\pm1\}\}$. "$\subset$": Step 2 and $N(x) = x\,t(x) = \pm1$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-9|Theorem §CB.9.9]], Step 1, a direct computation). "$\supset$": let $x$ be in the right side. By Step 3, $A_x \in O(V)$; by Cartan–Dieudonné ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-10|Theorem §CB.9.10]], proved below without using this theorem), $A_x = r_{u_1}\cdots r_{u_k}$ with $q(u_i) \ne 0$, and rescaling ($r_{cu} = r_u$) we may take $q(u_i) = \pm1$. Put $y = u_1\cdots u_k \in \mathrm{Pin}(V)$; $A_y = A_x$ by Step 2, so $z = y^{-1}x$ has $A_z = \mathbb 1$, and Step 4 gives $x = \lambda y$. Then $x\,t(x) = \lambda^2\,y\,t(y) = \pm\lambda^2$, which must be $\pm1$; as $\lambda$ is real, $\lambda^2 = 1$, $\lambda = \pm1$, and $x = (\pm u_1)u_2\cdots u_k \in \mathrm{Pin}(V)$.
>
> **Step 6** ($\mathrm{Pin}$ and $\mathrm{Spin}$ are closed). Each condition in Step 5 is closed in $\mathrm{Cl}^\times$: for a basis vector $e_j$, $x \mapsto A_x(e_j)$ is continuous and $V$ is a closed subspace of $\mathrm{Cl}$; $x \mapsto x\,t(x)$ is continuous and $\{\pm1\}$ is closed. So $\mathrm{Pin}(V)$ is closed in $\mathrm{Cl}^\times$, and $\mathrm{Spin}(V) = \mathrm{Pin}(V)\cap\mathrm{Cl}^0$ too ($\mathrm{Cl}^0$ is a closed subspace).
>
> **Step 7** (matrix Lie groups). Under left multiplication $L : \mathrm{Cl} \to \operatorname{End}_{\mathbb R}(\mathrm{Cl})$, $L(\mathrm{Cl}^\times) = L(\mathrm{Cl})\cap GL(\mathrm{Cl})$ is closed in $GL(\mathrm{Cl})$ ($L(\mathrm{Cl})$ is a linear subspace), and $L$ is a homeomorphism onto its image. A subgroup closed in a closed subgroup of $GL(\mathrm{Cl})$ is closed in $GL(\mathrm{Cl})$, so $L(\mathrm{Pin}(V))$ and $L(\mathrm{Spin}(V))$ are matrix Lie groups ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]).
>
> **What the proof shows.**
> - ⚑ By-product (Step 4): the only invertible elements whose twisted conjugation fixes $V$ pointwise are the real scalars. This is the kernel computation of Theorem §CB.9.11, and it is where the sign $\alpha$ in $\tilde\rho$ matters: with untwisted conjugation the odd element $\omega$ would survive for $n$ odd.
> - ⚑ By-product (Step 5): an invertible element that maps $V$ into $V$ by twisted conjugation and has norm $\pm1$ is automatically a product of unit vectors; this is how one recognizes $e^{X}$, $X \in \mathfrak{spin}(V)$, as an element of $\mathrm{Spin}(V)$ (Theorem §CB.9.14).

^pf-cb-9-7

*Uses:* [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-1|Def. §CB.9.1]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-2|Theorem §CB.9.2]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-3|Def. §CB.9.3]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-14|Theorem §CB.7.14]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-2|Def. §C3.1.2]]

> [!definition] Definition §CB.9.8: Spinor Norm
> The **spinor norm** of $x \in \mathrm{Cl}$ is $N(x) = x\,t(x)$, with $t$ the reversal ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-14|Theorem §CB.7.14]]).
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, §4.1 (the norm homomorphism $N(x) = x^\top x$; on $\mathrm{Pin}$ the two orders give the same value)*

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
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Ch. 1, Thm. 4.5 (Artin's proof) · stated in Figueroa-O'Farrill, Spin Geometry, Thm. 3.2, and Woit, §29.2.1 · the two cases the course needs are also reached directly ($SU(2) \to SO(3)$: [[§42 SU(2) → SO(3)꞉ The Double Cover#^thm-42-4|591 Thm. §42.4]]; $SL(2, \mathbb C) \to SO^+(1,3)$: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]])*

^thm-cb-9-10

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, lecture notes (Toronto, Fall 2009), Ch. 1 §4, Lemma 4.1 and Thm. 4.5 with its proof, "a small modification of Artin's proof" (https://www.math.toronto.edu/mein/teaching/LieClifford/cl12.pdf), followed case by case. Two changes, both written here: in Case 2 Meinrenken chooses $w_1 \perp w$, which exists only when $\dim V \ge 3$, and Step 5 below makes a choice that works in every dimension; in Case 3 the determinant is computed from $(A - \mathbb 1)^2 = 0$ instead of his Lemma 3.3 on split forms. Stated without proof in Figueroa-O'Farrill, Spin Geometry, Thm. 3.2, and Woit, §29.2.1.*
>
> Notation: $B$ is nondegenerate on $V$, $\dim V = n$; a vector $u$ is *non-isotropic* if $q(u) \ne 0$; $r_u$ is the reflection of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]]; for $A \in O(V)$ let $K = \ker(A - \mathbb 1)$ (fixed vectors) and $R = \operatorname{ran}(A - \mathbb 1)$.
>
> **Step 1** (orthogonal complements). For a subspace $F$, $F^\perp = (B^\flat)^{-1}(F^0)$, where $B^\flat(v) = B(v, \cdot)$ is an isomorphism $V \to V'$ (nondegeneracy) and $F^0$ the annihilator; so $\dim F^\perp = n - \dim F$ ([[§12 Duality#^ladr-3-125|LADR Thm. 3.125]]). Since $F \subset (F^\perp)^\perp$ and both have dimension $\dim F$, $(F^\perp)^\perp = F$. If $q(u) \ne 0$, $V = \mathbb Ru\oplus u^\perp$ and $B$ is nondegenerate on $u^\perp$ (Step 1 of the proof of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]]).
>
> **Step 2** (Meinrenken's Lemma 4.1: $R = K^\perp$). If $w \in K$ then $w = Aw$, so for every $v$, $B((A - \mathbb 1)v, w) = B(Av, Aw) - B(v, w) = 0$: $R \subset K^\perp$. By rank–nullity $\dim R = n - \dim K = \dim K^\perp$ (Step 1). Hence $R = K^\perp$.
>
> **Step 3** (induction; small $n$). Induction on $n$. For $n = 0$, $O(V) = \{\mathbb 1\}$, the empty product. Assume the theorem for nondegenerate spaces of dimension $< n$, and let $A \in O(V)$. A subspace on which every vector is isotropic has $B = 0$ on it (polarization, [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]]). Three cases exhaust all possibilities.
>
> **Step 4** (Case 1: $K$ contains a non-isotropic $v$). $A$ fixes $v$ and preserves $V_1 = v^\perp$ ($B(Aw, v) = B(Aw, Av) = B(w, v) = 0$ for $w \perp v$). $V_1$ is nondegenerate of dimension $n - 1$ (Step 1) and $A|_{V_1} \in O(V_1)$, so by induction $A|_{V_1} = r'_{u_1}\cdots r'_{u_k}$, $k \le n - 1$, with $u_i \in V_1$ non-isotropic and $r'$ the reflections of $V_1$. Each $r_{u_i}$ of $V$ fixes $v$ ($B(u_i, v) = 0$) and agrees with $r'_{u_i}$ on $V_1$; so $A = r_{u_1}\cdots r_{u_k}$ on $\mathbb Rv\oplus V_1 = V$, with $k \le n - 1$.
>
> **Step 5** (Case 2: $K$ totally isotropic, $R$ contains a non-isotropic vector). *Claim:* there is a non-isotropic $w$ with $v = (A - \mathbb 1)w$ non-isotropic. Suppose not: $A - \mathbb 1$ sends every non-isotropic vector to an isotropic one. Take $v_0 = (A - \mathbb 1)w_0 \in R$ non-isotropic; then $w_0$ is isotropic, $q(w_0) = 0$, and $w_0 \ne 0$. Pick any non-isotropic $u$ and a real $t \notin \{0,\ 2B(w_0, u)/q(u),\ -2B(w_0, u)/q(u)\}$, and put $w_1 = tu$. Then
>
> $$
> q(w_1) = t^2q(u) \ne 0, \qquad q(w_0 \pm w_1) = q(w_0) \pm 2tB(w_0, u) + t^2q(u) = t\bigl(tq(u) \pm 2B(w_0, u)\bigr) \ne 0 .
> $$
>
> By the supposition, $v_1 = (A - \mathbb 1)w_1$ and $v_0 \pm v_1 = (A - \mathbb 1)(w_0 \pm w_1)$ are isotropic. Expanding $q(v_0 + v_1) + q(v_0 - v_1) = 2q(v_0) + 2q(v_1)$ (the cross terms $\pm2B(v_0, v_1)$ cancel) gives $q(v_0) = \frac12\bigl(q(v_0 + v_1) + q(v_0 - v_1)\bigr) - q(v_1) = 0$, a contradiction. This proves the claim.
>
> Now with such $w$ and $v$: $(A + \mathbb 1)w \perp v$, because $B((A + \mathbb 1)w, (A - \mathbb 1)w) = q(Aw) - B(Aw, w) + B(w, Aw) - q(w) = 0$. So $r_v(A - \mathbb 1)w = -(A - \mathbb 1)w$ ($r_v v = -v$) and $r_v(A + \mathbb 1)w = (A + \mathbb 1)w$. Adding and dividing by $2$: $r_vAw = w$. So $r_vA$ fixes the non-isotropic $w$: Case 1 for $r_vA$ gives $r_vA = r_{u_1}\cdots r_{u_k}$, $k \le n - 1$, and $A = r_v\,r_{u_1}\cdots r_{u_k}$ ($r_v^2 = \mathbb 1$), at most $n$ reflections.
>
> **Step 6** (Case 3: $K$ and $R$ both totally isotropic). Then $K \subset K^\perp = R$ (Step 2) and $R \subset R^\perp = (K^\perp)^\perp = K$ (Step 1), so $K = R = K^\perp$ and $n = \dim K + \dim K^\perp = 2\dim K$ is even. $(A - \mathbb 1)$ maps $V$ into $R = K = \ker(A - \mathbb 1)$, so $(A - \mathbb 1)^2 = 0$: $N = A - \mathbb 1$ is nilpotent, has a strictly upper-triangular matrix in some basis ([[§30 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-18|LADR Thm. 8.18]]), and $\det A = \det(\mathbb 1 + N) = 1$ ([[§37 Determinants#^ladr-9-48|LADR Thm. 9.48]]). Pick a non-isotropic $u$ and set $A_1 = r_uA$; $\det A_1 = -1$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]], [[§37 Determinants#^ladr-9-49|LADR 9.49]]), so $A_1$ is not in Case 3 and, by Steps 4–5, $A_1 = r_{u_1}\cdots r_{u_k}$ with $k \le n$. Taking determinants, $(-1)^k = -1$, so $k$ is odd, and $n$ is even, so $k \le n - 1$. Then $A = r_uA_1$ is a product of $k + 1 \le n$ reflections.
>
> **Step 7** ($SO(V)$). Each $r_u$ has determinant $-1$, so a product of $k$ reflections has determinant $(-1)^k$: the elements of $SO(V)$ are exactly the products of an even number of reflections.
>
> **What the proof shows.**
> - The bound $n$ is sharp: $-\mathbb 1$ fixes no vector, and a product of $k$ reflections fixes the intersection of $k$ hyperplanes, of dimension $\ge n - k$, so $-\mathbb 1$ needs $n$ reflections (Meinrenken, Prop. 4.4, the lower bound $\dim\operatorname{ran}(A - \mathbb 1) \le l(A)$).
> - Case 3 needs a totally isotropic subspace of dimension $n/2$, so it occurs only in split signature ($r = s$, Meinrenken, Example 4.7, for $n = 4$). For Euclidean $V$ and for $\mathbb R^{1,3}$, whose totally isotropic subspaces are at most lines, the proof is Cases 1–2 alone.
> - ⚑ By-product: every Lorentz transformation is a product of at most four reflections in non-null hyperplanes, and every proper one of an even number — the geometric reason a spinor transformation is a product of pairs of $\gamma$ matrices (Theorem §CB.9.11).

^pf-cb-9-10

*Uses:* [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^def-cb-7-1|Def. §CB.7.1]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]], [[§12 Duality#^ladr-3-125|LADR Thm. 3.125]], [[§30 Generalized Eigenvectors and Nilpotent Operators#^ladr-8-18|LADR Thm. 8.18]], [[§37 Determinants#^ladr-9-48|LADR Thm. 9.48]], [[§37 Determinants#^ladr-9-49|LADR Thm. 9.49]]

> [!theorem] Theorem §CB.9.11: Spin(V) → SO(V) Is Onto with Kernel ±1
> $\rho(\mathrm{Pin}(V)) = O(V)$ and $\rho(\mathrm{Spin}(V)) = SO(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]]), and $\ker\rho = \{1, -1\}$ on both: $\rho(x) = \rho(y)$ iff $y = \pm x$.
>
> *Source: Meinrenken, Clifford Algebras and Lie Groups, Thm. 4.2 and Def. 4.3 · Figueroa-O'Farrill, Spin Geometry, Props. 3.3, 3.5*

^thm-cb-9-11

> [!proof]- Proof
> *Source: E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §4.1, Thm. 4.2 and the exact sequences after Def. 4.3 · J. Figueroa-O'Farrill, Spin Geometry, §3.2, Props. 3.3 and 3.5 and the argument before them (kernel by expansion in an orthonormal basis, then the norm forces $\alpha^2 = \pm1$, $\alpha = \pm1$).*
>
> **Step 1** (onto $O(V)$). Let $R \in O(V)$. By Cartan–Dieudonné ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-10|Theorem §CB.9.10]]), $R = r_{u_1}\cdots r_{u_k}$ with $q(u_i) \ne 0$. The formula of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]] is unchanged under $u \mapsto cu$, $c \ne 0$, so replace $u_i$ by $u_i/\sqrt{|q(u_i)|}$, with $q = \pm1$. Then $x = u_1\cdots u_k \in \mathrm{Pin}(V)$ and $\rho(x) = R$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], 2).
>
> **Step 2** (onto $SO(V)$). If $R \in SO(V)$, $k$ is even (Theorem §CB.9.10), so $x \in \mathrm{Pin}(V)\cap\mathrm{Cl}^0 = \mathrm{Spin}(V)$. Conversely every $x \in \mathrm{Spin}(V)$ is a product of an even number of unit vectors (an odd product is odd and nonzero, so not in $\mathrm{Cl}^0$, [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]]), hence $\det\rho(x) = (-1)^{2m} = 1$. So $\rho(\mathrm{Spin}(V)) = SO(V)$.
>
> **Step 3** (kernel). If $x \in \mathrm{Pin}(V)$ and $\rho(x) = \mathbb 1$, Step 4 of the proof of Theorem §CB.9.7 gives $x = \lambda1$, $\lambda \in \mathbb R$. Its norm is $N(x) = \lambda\,t(\lambda) = \lambda^2$, and $N(x) = \pm1$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-9|Theorem §CB.9.9]]); $\lambda^2 > 0$ forces $\lambda^2 = 1$, $x = \pm1$. Both lie in $\mathrm{Spin}(V)$: $1$ is the empty product, and for a unit vector $u$, $u(-u) = -q(u)$ and $uu = q(u)$, one of which is $-1$. And $\rho(\pm1) = \mathbb 1$. So $\ker\rho = \{\pm1\}$ on $\mathrm{Pin}(V)$ and on $\mathrm{Spin}(V)$.
>
> **Step 4** (fibres). $\rho(x) = \rho(y)$ iff $\rho(xy^{-1}) = \mathbb 1$ iff $xy^{-1} = \pm1$ iff $x = \pm y$.
>
> **What the proof shows.**
> - Surjectivity is exactly Cartan–Dieudonné; injectivity up to sign is the kernel lemma plus the normalization $N = \pm1$ (without it the kernel would be all of $\mathbb R^\times$, Meinrenken's Clifford group).
> - The theorem says nothing yet about topology: whether $\pm1$ lie in one component, and whether $\rho$ is a covering, is Theorem §CB.9.12.

^pf-cb-9-11

*Uses:* [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-10|Theorem §CB.9.10]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-13|Theorem §CB.7.13]]

> [!theorem] Theorem §CB.9.12: The Identity Component Is a Double Cover
> If $n \ge 3$ (more generally, if $V$ contains a two-dimensional subspace on which $q$ is definite), then $-1 \in \mathrm{Spin}(V)_0$ and $\rho : \mathrm{Spin}(V)_0 \to SO(V)_0$ is a surjective two-to-one Lie group homomorphism and a covering map ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-23|Theorem §CB.1.23]]) with kernel $\{\pm1\}$. For $n \ge 3$ and $V$ definite, $\mathrm{Spin}(n)$ is connected and simply connected, the universal covering group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]) of $SO(n)$.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, §3.2 after Prop. 3.5 · Meinrenken, Clifford Algebras and Lie Groups, Ch. 2, Thm. 4.4, Example 4.6, and Ch. 1, Lemma 6.2 ($\pi_1(SO(n)) = \mathbb Z_2$, $n \ge 3$) · Woit, §6.2 ($n = 3, 4$)*

^thm-cb-9-12

> [!proof]- Proof
> *Source: $-1 \in \mathrm{Spin}(V)_0$: J. Figueroa-O'Farrill, Spin Geometry, §3.2, after Prop. 3.5 (the curve $a(t) = (e_1\cos t + e_2\sin t)(e_2\sin t - e_1\cos t)$ in a definite plane) and E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2, Thm. 4.4 and Example 4.6 ($x(\theta) = \cos\frac\theta2 + \sin\frac\theta2\,e_1e_2$, $x(\theta + 2\pi) = -x(\theta)$) · simple connectivity: Meinrenken, Ch. 2 after Thm. 4.4 ("since $\pi_1(SO(n)) = \mathbb Z_2$ for $n \ge 3$, the connected double cover $\mathrm{Spin}(n)$ is the universal cover") with Ch. 1, Lemma 6.2. The covering argument of Step 7 is written out here with the 590 lifting lemmas; the path argument of Step 5 is written here (it replaces the fibre-bundle proof that $SO(n)$ is connected).*
>
> **Step 1** ($-1 \in \mathrm{Spin}(V)_0$). Let $e_1, e_2$ be orthonormal spanning a plane on which $q$ is definite: $q(e_1) = q(e_2) = \epsilon \in \{\pm1\}$, $B(e_1, e_2) = 0$. For real $s$, $u(s) = \cos s\,e_1 + \sin s\,e_2$ has $q(u(s)) = \epsilon(\cos^2s + \sin^2s) = \epsilon$. Put $x(s) = \cos s + \sin s\,e_1e_2$. Using $e_1e_1 = \epsilon$:
>
> $$
> \epsilon = +1:\ \ e_1\,u(s) = \cos s\,e_1e_1 + \sin s\,e_1e_2 = x(s), \qquad \epsilon = -1:\ \ (-e_1)\,u(-s) = -\cos s\,e_1e_1 + \sin s\,e_1e_2 = x(s) .
> $$
>
> Either way $x(s)$ is a product of two vectors with $q = \pm1$, so $x(s) \in \mathrm{Spin}(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-6|Def. §CB.9.6]]). It is continuous in $s$, $x(0) = 1$ and $x(\pi) = -1$: so $-1 \in \mathrm{Spin}(V)_0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]]). (Since $(e_1e_2)^2 = -e_1e_1e_2e_2 = -\epsilon^2 = -1$, the series gives $x(s) = e^{s\,e_1e_2}$.) For $n \ge 3$ such a plane exists: with $r$ positive and $s'$ negative basis vectors, $r + s' \ge 3$ forces $r \ge 2$ or $s' \ge 2$.
>
> ⚑ By-product: by Theorem §CB.9.14, 2, $\rho_\ast(e_1e_2)$ sends $e_1 \mapsto -2\epsilon e_2$, $e_2 \mapsto 2\epsilon e_1$, so $\rho(x(s)) = e^{s\rho_\ast(e_1e_2)}$ is the rotation through the angle $2s$ in the $e_1e_2$-plane: the path from $1$ to $-1$ in $\mathrm{Spin}$ lies over the full rotation by $2\pi$. This is the half angle of spin ½ and the sign of a $2\pi$ rotation ([[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-3|Theorem §CB.10.3]]).
>
> **Step 2** ($\mathrm{Spin}(V)_0$ is a connected matrix Lie group with Lie algebra $\mathfrak{spin}(V)$). $\mathrm{Spin}(V)$ is a matrix Lie group ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]]); its identity component is a subgroup, closed in it ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], 1), hence a matrix Lie group, path-connected by definition. If $e^{sX} \in \mathrm{Spin}(V)$ for all $s$, the path $s \mapsto e^{sX}$ lies in $\mathrm{Spin}(V)_0$; so both groups have the Lie algebra $\mathfrak{spin}(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]], 1; its proof does not use the present theorem). Likewise $SO(V)_0$ has the Lie algebra $\mathfrak{so}(V)$.
>
> **Step 3** (the covering). $\rho$ maps the path-connected $\mathrm{Spin}(V)_0$ continuously into $SO(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-11|Theorem §CB.9.11]]) with $\rho(1) = \mathbb 1$, hence into $SO(V)_0$. Its differential $\rho_\ast : \mathfrak{spin}(V) \to \mathfrak{so}(V)$ is a Lie algebra isomorphism (Theorem §CB.9.14, 3). By [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-23|Theorem §CB.1.23]], $\rho : \mathrm{Spin}(V)_0 \to SO(V)_0$ is surjective and a covering map, with kernel $\ker\rho\cap\mathrm{Spin}(V)_0 = \{\pm1\}$ (Theorem §CB.9.11 and Step 1). Each fibre is $\{x, -x\}$ (Theorem §CB.9.11), and $-x \in \mathrm{Spin}(V)_0$ when $x$ is: two-to-one.
>
> **Step 4** ($\mathrm{Spin}(V)_0 = \rho^{-1}(SO(V)_0)$). If $x \in \mathrm{Spin}(V)$ and $\rho(x) \in SO(V)_0$, Step 3 gives $y \in \mathrm{Spin}(V)_0$ with $\rho(y) = \rho(x)$, so $x = \pm y \in \mathrm{Spin}(V)_0$. This is Meinrenken's definition of $\mathrm{Spin}_0$ (the preimage of the identity component), shown connected in his Thm. 4.4.
>
> **Step 5** (definite $V$, $n \ge 2$: $\mathrm{Spin}(V)$ and $SO(V)$ are connected). Now $q(u) = \epsilon$ for every unit vector, and in an orthonormal basis the unit vectors form the sphere $S^{n-1}$, path-connected for $n \ge 2$ (the image of the path-connected $\mathbb R^n\setminus\{0\}$ under $v \mapsto v/|v|$). For $x = u_1\cdots u_{2k} \in \mathrm{Spin}(V)$ choose paths $u_i(s)$ of unit vectors from $u_i$ to $e_1$; then $u_1(s)\cdots u_{2k}(s)$ is a path in $\mathrm{Spin}(V)$ from $x$ to $e_1^{2k} = \epsilon^k = \pm1$, and $\pm1 \in \mathrm{Spin}(V)_0$ (Step 1, $n \ge 2$ definite). So $\mathrm{Spin}(V) = \mathrm{Spin}(V)_0$, and $SO(V) = \rho(\mathrm{Spin}(V))$ is path-connected, $SO(V) = SO(V)_0$.
>
> **Step 6** (the input from topology). For $n \ge 3$, $\pi_1(SO(n)) \cong \mathbb Z_2$ (for $q$ negative definite, $O(V, q) = O(V, -q)$, the same group). For $n = 3$ this is [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], 2 ($SO(3) \cong \mathbb{RP}^3$). For $n \ge 4$ it is **not proved in the vault**: Meinrenken, Ch. 1, Lemma 6.2, proves it from the fibre bundle $SO(n-1) \to SO(n) \to S^{n-1}$ (evaluation at $e_n$) and its long exact sequence of homotopy groups, $\pi_2(S^{n-1}) \to \pi_1(SO(n-1)) \to \pi_1(SO(n)) \to \pi_1(S^{n-1})$, whose outer terms vanish for $n \ge 4$, so $\pi_1(SO(n)) \cong \pi_1(SO(n-1)) \cong \cdots \cong \pi_1(SO(3))$; the exact sequence is A. Hatcher, Algebraic Topology, Thm. 4.41, with Prop. 4.48 for bundles (https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
>
> **Step 7** (definite $V$, $n \ge 3$: $\mathrm{Spin}(V)$ is simply connected). Write $p = \rho : E = \mathrm{Spin}(V) \to B = SO(V)$, a covering (Steps 3, 5) with fibre $p^{-1}(\mathbb 1) = \{\pm1\}$ and $E$ path-connected. (a) The lifting correspondence $\phi : \pi_1(B, \mathbb 1) \to \{\pm1\}$ is surjective ([[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]], 1); both sets have two elements (Step 6), so $\phi$ is bijective. (b) Let $\gamma$ be a loop in $E$ at $1$. The lift of $p\circ\gamma$ starting at $1$ is $\gamma$ itself (uniqueness, [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|590 Lemma §32.1]]), which ends at $1$; so $\phi([p\circ\gamma]) = 1 = \phi([\text{const}])$ and, $\phi$ being injective, $p\circ\gamma$ is path-homotopic to the constant loop by some $F$. (c) Lift $F$ to $\tilde F$ with $\tilde F(0, 0) = 1$, a path homotopy ([[§32 Lifting and the Fundamental Group of the Circle#^lem-32-2|590 Lemma §32.2]]). Its bottom edge is a lift of $p\circ\gamma$ from $1$, hence $\gamma$; its top edge is a lift of a constant path from $1$, hence constant. So $\gamma$ is path-homotopic to the constant loop: $E$ is simply connected ([[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]). With Step 3, $\rho : \mathrm{Spin}(V) \to SO(V)$ is a universal covering group ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]]).
>
> **What the proof shows.**
> - The two-valuedness of spinors is Step 1: the loop of rotations through $0 \dots 2\pi$ lifts to a path from $1$ to $-1$, not to a loop.
> - Simple connectivity needs the topological input of Step 6 and holds for definite $V$; it fails in general for indefinite signature (Meinrenken, after Thm. 4.4: $\pi_1(SO_0(r, s)) = \pi_1(SO(r))\times\pi_1(SO(s))$). For $\mathbb R^{1,3}$, $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ is simply connected by a separate argument (§CB.11).
> - ⚑ By-product (Steps 4–5): $\mathrm{Spin}(V)_0$ is the full preimage of $SO(V)_0$, and $SO(n)$ is connected, both obtained here without fibre bundles.

^pf-cb-9-12

*Uses:* [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-6|Def. §CB.9.6]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-11|Theorem §CB.9.11]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-15|Def. §CB.1.15]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-21|Def. §CB.1.21]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-23|Theorem §CB.1.23]], [[§C3.1 Groups, Algebras and Representations of Rotations#^thm-c3-1-8|Theorem §C3.1.8]], [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-1|590 Lemma §32.1]], [[§32 Lifting and the Fundamental Group of the Circle#^lem-32-2|590 Lemma §32.2]], [[§32 Lifting and the Fundamental Group of the Circle#^thm-32-4|590 Thm. §32.4]], [[§29 The Fundamental Group#^def-29-3|590 Def. §29.3]]

## The Lie algebra 𝔰𝔭𝔦𝔫(V)

> [!definition] Definition §CB.9.13: The Spin Lie Algebra
> $\mathfrak{spin}(V) \subset \mathrm{Cl}^0$ is the span of the products $e_ie_j$ ($i < j$) for an orthogonal basis of $V$; equivalently the span of all commutators $[v, w] = vw - wv$, $v, w \in V$; equivalently the image of $\Lambda^2V$ under [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-17|Theorem §CB.7.17]]. Its dimension is $n(n-1)/2$.
>
> *Source: Figueroa-O'Farrill, Spin Geometry, §3.1, eq. (55) · Woit, §29.2.2 · Meinrenken, Clifford Algebras and Lie Groups, §2.11, §4.1*

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
> *Source: Figueroa-O'Farrill, Spin Geometry, §3.1, eqs. (55)–(57) · Meinrenken, Clifford Algebras and Lie Groups, §4.1 after Prop. 4.5 · Woit, §29.2.2, eqs. (29.4)–(29.5) · the Minkowski case: [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]]*

^thm-cb-9-14

> [!proof]- Proof
> *Source: J. Figueroa-O'Farrill, Spin Geometry, §3.1, eqs. (53)–(57) (the embedding $\mathfrak{so}(V) \to C\ell(V)$, $u\curlywedge v \mapsto \frac14(uv - vu)$, with $[\rho(u\curlywedge v), x] = (u\curlywedge v)(x)$, an injective Lie algebra homomorphism; his sign convention) · E. Meinrenken, Clifford Algebras and Lie Groups, Ch. 2 §4.1, after Prop. 4.5 ($A(v) = [\gamma(A), v]$, $\exp(A)(v) = e^{\gamma(A)}ve^{-\gamma(A)}$, $e^{\gamma(A)} \in \mathrm{Spin}(V)$ since $\gamma(A)^\top = -\gamma(A)$ gives norm $1$; "the group $\mathrm{Spin}(V)$ has Lie algebra $\gamma(\mathfrak o(V))$") · P. Woit, Quantum Theory, Groups and Representations, §29.2.2, eqs. (29.4)–(29.5). The inclusion "$\subset$" in Step 6 is written here.*
>
> Fix an orthogonal (here orthonormal) basis $e_i$, $q_i = q(e_i) = \pm1$, and write $\mathrm{ad}_X(y) = [X, y] = Xy - yX$.
>
> **Step 1** (the commutator with a vector). For $u, w, v \in V$, move $v$ to the left through $uw$ with $wv = -vw + 2B(w, v)$ and $uv = -vu + 2B(u, v)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]]):
>
> $$
> uwv = u\bigl(-vw + 2B(w, v)\bigr) = -uvw + 2B(w, v)u = \bigl(vu - 2B(u, v)\bigr)w + 2B(w, v)u = vuw - 2B(u, v)w + 2B(w, v)u .
> $$
>
> Hence $[uw, v] = 2B(w, v)\,u - 2B(u, v)\,w \in V$, and with $u = e_i$, $w = e_j$, $i \ne j$: $\mathrm{ad}_{\frac12e_ie_j}(v) = B(e_j, v)e_i - B(e_i, v)e_j$ — the formula of part 2. So $\mathrm{ad}_X$ maps $V$ to $V$ for every $X \in \mathfrak{spin}(V)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]]).
>
> **Step 2** ($\mathrm{ad}_X|_V \in \mathfrak{so}(V)$). For $X = \frac12e_ie_j$:
>
> $$
> B(\mathrm{ad}_Xv, w) + B(v, \mathrm{ad}_Xw) = B(e_j, v)B(e_i, w) - B(e_i, v)B(e_j, w) + B(e_j, w)B(e_i, v) - B(e_i, w)B(e_j, v) = 0,
> $$
>
> the four terms cancelling in pairs. So $\mathrm{ad}_X|_V$ is skew for $B$, i.e. in $\mathfrak{so}(V)$, and by linearity for all $X \in \mathfrak{spin}(V)$.
>
> **Step 3** ($X \mapsto \mathrm{ad}_X|_V$ is a linear isomorphism $\mathfrak{spin}(V) \to \mathfrak{so}(V)$). On basis vectors, Step 1 gives $\mathrm{ad}_{\frac12e_ie_j}e_k = q_j\delta_{jk}e_i - q_i\delta_{ik}e_j$. For $X = \sum_{i<j}c_{ij}\frac12e_ie_j$,
>
> $$
> \mathrm{ad}_Xe_k = q_k\Bigl(\sum_{i<k}c_{ik}\,e_i - \sum_{j>k}c_{kj}\,e_j\Bigr),
> $$
>
> which vanishes for all $k$ only if all $c_{ij} = 0$ ($q_k \ne 0$, the $e_i$ independent). So the map is injective. $\dim\mathfrak{spin}(V) = \binom n2$ (the $e_ie_j$, $i < j$, are part of the basis of [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]]), and $\dim\mathfrak{so}(V) = \frac{n(n-1)}2$: in an orthonormal basis with Gram matrix $\eta = \operatorname{diag}(q_i)$, $A \in \mathfrak{so}(V)$ iff $A^{\mathsf T}\eta + \eta A = 0$ iff $\eta A$ is antisymmetric, and $A \mapsto \eta A$ is a bijection. Equal dimensions: the map is an isomorphism.
>
> **Step 4** ($e^{sX} \in \mathrm{Spin}(V)$ for $X \in \mathfrak{spin}(V)$). $e^{sX}$ is invertible and even ($X$ is even and $\mathrm{Cl}^0$ is a closed subalgebra). For $v \in V$, $e^{sX}ve^{-sX} = e^{s\,\mathrm{ad}_X}v$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], 3, in the matrix Lie group $\mathrm{Cl}^\times$), which lies in $V$ by Step 1; since $e^{sX}$ is even, this is $\tilde\rho(e^{sX})v$. Next, $t(e_ie_j) = e_je_i = -e_ie_j$ for $i \ne j$, so $t(X) = -X$; $t$ is linear and reverses products, so $t(X^m) = t(X)^m$ and, $t$ being continuous, $t(e^{sX}) = e^{s\,t(X)} = e^{-sX}$. Hence $N(e^{sX}) = e^{sX}e^{-sX} = 1$. By the characterization of $\mathrm{Pin}$ in Step 5 of the proof of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], $e^{sX} \in \mathrm{Pin}(V)\cap\mathrm{Cl}^0 = \mathrm{Spin}(V)$. So $\mathfrak{spin}(V) \subset \operatorname{Lie}(\mathrm{Spin}(V))$ ([[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]).
>
> **Step 5** (the differential). For $X \in \operatorname{Lie}(\mathrm{Spin}(V))$, $\rho(e^{sX})v = e^{sX}ve^{-sX}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], 2), and differentiating at $s = 0$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]) gives $\rho_\ast(X)v = Xv - vX = [X, v]$, the formula of part 2; $\rho_\ast(X) \in \mathfrak{so}(V)$ because $\rho$ takes values in $SO(V)$ (Theorem §CB.9.11).
>
> **Step 6** ($\operatorname{Lie}(\mathrm{Spin}(V)) \subset \mathfrak{spin}(V)$). Let $e^{sX} \in \mathrm{Spin}(V)$ for all $s$. Then $X = \frac{d}{ds}e^{sX}|_{s=0} \in \mathrm{Cl}^0$. By Step 5, $\mathrm{ad}_X|_V = \rho_\ast(X) \in \mathfrak{so}(V)$, and by Step 3 there is $Y \in \mathfrak{spin}(V)$ with $\mathrm{ad}_Y|_V = \mathrm{ad}_X|_V$. Then $Z = X - Y$ is even and commutes with every $v \in V$, hence with all of $\mathrm{Cl}$, so $Z = c1$, $c \in \mathbb R$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], 4). Finally $N(e^{sX}) = e^{sX}e^{s\,t(X)}$ is continuous in $s$, takes values in $\{\pm1\}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-9|Theorem §CB.9.9]]) and equals $1$ at $s = 0$, so it is $1$; its derivative at $0$ is $X + t(X) = 0$. But $X + t(X) = (Y + c) + (-Y + c) = 2c$, so $c = 0$ and $X = Y \in \mathfrak{spin}(V)$.
>
> **Step 7** (conclusion). By Steps 4 and 6, $\operatorname{Lie}(\mathrm{Spin}(V)) = \mathfrak{spin}(V)$, which is therefore closed under the commutator ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]]): part 1. Part 2 is Steps 1 and 5. $\rho_\ast$ is a Lie algebra homomorphism (Theorem §CB.1.14) and, being $X \mapsto \mathrm{ad}_X|_V$, a linear isomorphism onto $\mathfrak{so}(V)$ (Step 3): part 3.
>
> **What the proof shows.**
> - In the course's Dirac module $e_\mu \mapsto \gamma_\mu$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-12-1|Caution: Two Dirac modules, and the sign of γ⁵]]), the dual basis $e^\mu = g^{\mu\nu}e_\nu$ goes to $\gamma^\mu$, and $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac i2\gamma^\mu\gamma^\nu = i\,\gamma\bigl(\tfrac12e^\mu e^\nu\bigr)$ for $\mu \ne \nu$: the physicists' generators are $i$ times elements of $\mathfrak{spin}(1,3)$, and part 2 is the statement that they rotate the $\gamma^\mu$ like a vector ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]]).
> - ⚑ By-product (Step 6): an element of the Lie algebra of $\mathrm{Spin}$ is reversal-odd, $t(X) = -X$; the scalar $c$ is excluded only by the norm condition, which is why $\mathrm{Spin}$ is cut out by $N = \pm1$ and not merely by "conjugation preserves $V$".
> - Used in: Theorem §CB.9.12 (covering), Theorem §CB.9.15, and $\mathfrak{spin}(3) = \mathfrak{su}(2)$ ([[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-4|Theorem §CB.10.4]]).

^pf-cb-9-14

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-16|Theorem §CB.7.16]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-19|Theorem §CB.7.19]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-9|Theorem §CB.9.9]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-11|Theorem §CB.9.11]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-8|Theorem §CB.1.8]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-20|Theorem §CB.1.20]], [[§C3.1 Groups, Algebras and Representations of Rotations#^def-c3-1-3|Def. §C3.1.3]]

The course's spinor generators and their two theorems, the Minkowski case of Theorem §CB.9.14 in the physicists' normalization $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu] = \frac i2\gamma(e^\mu e^\nu)$ ($\mu \ne \nu$, $e^\mu = g^{\mu\nu}e_\nu$, for the course's module $e_\mu \mapsto \gamma_\mu$ of [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-12-1|Caution: Two Dirac modules, and the sign of γ⁵]]), in [[§C5a.3 The Lorentz Action on Spinor Space|§C5a.3]]:

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
> The **spinor representation** of $\mathrm{Spin}(V)$ is the restriction $x \mapsto \gamma(x)$ of an irreducible complex Clifford module $\gamma$ on $S$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]]) to $\mathrm{Spin}(V) \subset \mathrm{Cl}$; for $n$ even, the **half-spin representations** are its restrictions to $S^\pm$, the $\pm1$ eigenspaces of $\omega_{\mathbb C}$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-10|Theorem §CB.8.10]]); for $\mathbb R^{1,3}$ and the course's module $e_\mu \mapsto \gamma_\mu$ these are the $\gamma^5 = \mp1$ spaces, so this $S^+$ is the course's left-handed $(\frac12, 0)$ (which §CB.12 labels $S^-$, [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^cau-cb-12-1|Caution: Two Dirac modules, and the sign of γ⁵]]). Its differential is $\gamma|_{\mathfrak{spin}(V)}$ (Theorem §CB.9.14).
>
> *Source: Figueroa-O'Farrill, Spin Geometry, Def. 3.7 and §3.3 · Woit, Ch. 31, Ch. 41*

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
> 3. **Spinor ⊗ tensor.** Every finite-dimensional spinorial representation $W$ of $\mathrm{Spin}(V)_0$ is equivalent to a subrepresentation of $S\otimes T$ for a tensorial representation $T$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-1|Def. §CB.4.1]]); one may take $T = S'\otimes W$ ($S'$ the dual, [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-6|Def. §CB.4.6]]). Moreover $T$ can be taken inside a direct sum of tensor powers $(V_{\mathbb C})^{\otimes k}$ of the complexified vector representation $x \mapsto \rho(x)$: proved in CB for $n = 3$ ([[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-6|Theorem §CB.10.6]]) and $\mathbb R^{1,3}$ ([[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-9|Theorem §CB.12.9]]); for general $n$ by highest-weight theory (reference in the proof).
>
> *Source: PHY 513 TA (oral remark, Oct 2026) · J. Figueroa-O'Farrill, Spin Geometry, Lecture 3 (introduction: spinorial representations are those "not contained in any tensor product of the fundamental (vector) representation"; Def. 3.7 and §3.3) · H. Georgi, Lie Algebras in Particle Physics, 2nd ed., §8.12, Ch. 21–23 (highest weights, for part 3 in general) · the cases proved in CB: $n = 3$, Theorem §CB.10.6; $\mathbb R^{1,3}$, Theorem §CB.12.9*

^thm-cb-9-20

> [!proof]- Proof
> *Source: the statement is the PHY 513 TA's (oral remark, Oct 2026). Parts 1–2: J. Figueroa-O'Farrill, Spin Geometry, Def. 3.7 ("a spinor representation of $\mathrm{Spin}(V)$ is the restriction of an irreducible representation of $C\ell(V)^0$") and §3.3 (for $d$ even the eigenspaces of $\omega$ in the pinor representation are the spinor representations; for $d$ odd both pinor representations restrict to the spinor one), assembled here from Theorems §CB.8.7, §CB.8.10, §CB.9.12, §CB.9.15. Part 3, first claim: written here (the canonical invariant of $S\otimes S'$). Part 3, tensor powers for general $n$: not proved in CB; see Step 8.*
>
> **Step 1** ($-1$ acts as $-\mathbb 1$). $n \ge 3$, so $-1 \in \mathrm{Spin}(V)_0$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-12|Theorem §CB.9.12]]). $\gamma$ is a unital algebra homomorphism, so $\gamma(-1) = -\gamma(1) = -\mathbb 1$: the restriction is spinorial ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]]). It is not of the form $D\circ\rho$, since that would give $D(\rho(-1)) = D(\mathbb 1) = \mathbb 1$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]).
>
> **Step 2** (same invariant subspaces). For a Clifford module, a subspace is invariant under $\mathrm{Spin}(V)_0$ iff under $\mathrm{Cl}^0$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-15|Theorem §CB.9.15]]).
>
> **Step 3** (same intertwiners). Let $\gamma_1$, $\gamma_2$ be Clifford modules on $W_1$, $W_2$ and $A : W_1 \to W_2$ linear. If $A\gamma_1(x) = \gamma_2(x)A$ for all $x \in \mathrm{Cl}^0$, this holds in particular on $\mathrm{Spin}(V)_0 \subset \mathrm{Cl}^0$. Conversely, suppose it holds on $\mathrm{Spin}(V)_0$. For $X \in \mathfrak{spin}(V)$, $e^{sX} \in \mathrm{Spin}(V)_0$ (Step 4 of the proof of [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]]; the path $s \mapsto e^{sX}$ starts at $1$), and $\gamma_i(e^{sX}) = e^{s\gamma_i(X)}$ ($\gamma_i$ is linear and multiplicative, hence maps the exponential series termwise, and continuous). Differentiating $Ae^{s\gamma_1(X)} = e^{s\gamma_2(X)}A$ at $s = 0$ gives $A\gamma_1(X) = \gamma_2(X)A$; then $A$ intertwines all products of such $X$ and $1$, which span $\mathrm{Cl}^0$ (Theorem §CB.9.15). So equivalences of the restrictions to $\mathrm{Spin}(V)_0$ are the same as equivalences of $\mathrm{Cl}^0$-modules.
>
> **Step 4** (part 1, $n$ odd). $S$ is irreducible as a $\mathrm{Cl}^0$-module ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-10|Theorem §CB.8.10]], 2), so irreducible under $\mathrm{Spin}(V)_0$ by Step 2; $\dim S = 2^{(n-1)/2}$ ([[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]], 2).
>
> **Step 5** (part 1, $n$ even). $S = S^+\oplus S^-$ with $S^\pm$ irreducible and inequivalent $\mathrm{Cl}^0$-modules of dimension $2^{n/2-1}$, and $\gamma(v)S^\pm \subset S^\mp$ (Theorem §CB.8.10, 1). By Steps 2–3 the same holds for $\mathrm{Spin}(V)_0$.
>
> **Step 6** (part 2). (a) A finite-dimensional Clifford module $W$ is a direct sum of irreducible Clifford modules (Theorem §CB.8.7, 3), each equivalent, by an intertwiner that in particular intertwines $\mathrm{Cl}^0$, to a fixed $S$; for $n$ odd both classes of $S$ restrict to the same $\mathrm{Cl}^0$-module (Theorem §CB.8.10, 2). So $W|_{\mathrm{Spin}(V)_0}$ is a direct sum of copies of $S$ ($n$ odd), resp. of $S^+$ and $S^-$ ($n$ even). (b) An irreducible representation of $\mathrm{Spin}(V)_0$ that is the restriction of a representation of the algebra $\mathrm{Cl}^0$ (for instance an irreducible $\mathrm{Spin}(V)_0$-invariant subspace $U$ of a Clifford module: $U$ is $\mathrm{Cl}^0$-invariant and $\mathrm{Cl}^0$-irreducible by Step 2) is an irreducible $\mathrm{Cl}^0$-module, hence equivalent to $S$, resp. $S^+$ or $S^-$ (Theorem §CB.8.10, 3), as a $\mathrm{Cl}^0$-module and so (Step 3) as a representation of $\mathrm{Spin}(V)_0$. By Steps 4–5 all of these occur.
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
> the element $\sum_as_a\otimes s^a$ is invariant (it corresponds to the identity intertwiner under [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-9|Theorem §CB.4.9]]). Hence $\iota(D_W(x)w) = (D_S\otimes D_S^\ast\otimes D_W)(x)\,\iota(w)$: $\iota$ is an intertwiner ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]). It is injective: the contraction $s\otimes\varphi\otimes w \mapsto \varphi(s)w$ sends $\iota(w)$ to $\sum_as^a(s_a)w = (\dim S)\,w$. So $W$ is equivalent to the subrepresentation $\iota(W)$ of $S\otimes T$.
>
> **Step 8** (part 3, tensor powers). $T$ is tensorial, hence $T = D\circ\rho$ for a representation $D$ of $SO(V)_0$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]], with the covering of Theorem §CB.9.12). It remains to place representations of $SO(V)_0$ inside sums of tensor powers of $V_{\mathbb C}$. For $n = 3$ this is [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-8|Theorem §CB.6.8]] (every representation of $SO(3)$ lies in a sum of tensor powers of $\mathbb C^3$), and [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-6|Theorem §CB.10.6]] gives the sharper $V_j \subset V_{1/2}\otimes V_{j-1/2}$; for $\mathbb R^{1,3}$ it is [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-8|Theorem §CB.12.8]] with [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-9|Theorem §CB.12.9]]. For general $n$ it is **not proved in CB**. It follows from highest-weight theory: the irreducible representation of highest weight $\mu = \sum_j\ell_j\mu_j$ lies in the tensor product of $\ell_j$ copies of each fundamental representation (H. Georgi, Lie Algebras in Particle Physics, 2nd ed., §8.12, eq. (8.75)); for $\mathfrak{so}(2n+1)$ and $\mathfrak{so}(2n+2)$ the fundamental weights are listed in Georgi eqs. (21.9) and (22.4), the last one (resp. two) being the spinor representations, the others having the highest weights $e_1 + \cdots + e_j$ of the antisymmetric tensors $\Lambda^jV_{\mathbb C} \subset V_{\mathbb C}^{\otimes j}$; and a product of two spinor representations is a sum of antisymmetric tensors (Georgi, §23.3 and the table of §23.4). Since $-1$ acts as $-\mathbb 1$ on each spinor factor and trivially on the others, it acts on that tensor product, hence on the irreducible representation inside it, as $(-1)^{\ell}$ with $\ell$ the number of spinor factors; a tensorial irreducible representation therefore has $\ell$ even and lies in a product of antisymmetric tensors and pairs of spinors, hence in a sum of tensor powers of $V_{\mathbb C}$.
>
> **What the proof shows.**
> - The three faces of spinors in the course are one object: a Clifford module (C5a.1), restricted to $\mathrm{Spin}$, is irreducible or splits into the Weyl halves (C5a.5), and $-1$ acts as $-1$, which is the two-valuedness on $SO$ (C3.3, C5a.4).
> - ⚑ By-product (Step 7): "spinor ⊗ tensor" needs no classification at all — any spinorial $W$ sits in $S\otimes(S'\otimes W)$ through the invariant $\sum_as_a\otimes s^a$; the content of the TA's remark is the further statement (Step 8) that the tensorial factor is built from vectors, which is where highest weights (or, for $n = 3$ and $\mathbb R^{1,3}$, Clebsch–Gordan) enter.
> - Step 3 is why the course may work with the generators $S^{\mu\nu}$ instead of the group: on a Clifford module, invariance and equivalence under $\mathrm{Spin}(V)_0$, under $\mathfrak{spin}(V)$ and under $\mathrm{Cl}^0$ are the same.

^pf-cb-9-20

*Uses:* [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-15|Theorem §CB.9.15]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]], [[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-7|Theorem §CB.8.7]], [[§CB.8 Complex Clifford Algebras and Clifford Modules#^thm-cb-8-10|Theorem §CB.8.10]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-8|Theorem §CB.6.8]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^def-cb-4-6|Def. §CB.4.6]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-9|Theorem §CB.4.9]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]], [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-6|Theorem §CB.10.6]], [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-8|Theorem §CB.12.8]], [[§CB.12 The Lorentz Case II꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-12-9|Theorem §CB.12.9]]

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
