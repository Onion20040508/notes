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

*Sources: P. Woit, Quantum Theory, Groups and Representations, §40.4 ("Spin and the Lorentz group": four-vectors as $x^0 + \mathbf x\cdot\boldsymbol\sigma$ and the action $\Omega(\cdot)\Omega^\dagger$) (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · through the course homes embedded below: the user's PHY 513 notes, Ch. 7 §7.4, Ch. 8 §8.2; PHY 513 Lecture 7; Yu Zhao-Huan, 量子场论讲义, Exercise 3.7; Peskin & Schroeder, §3.1–§3.2 · the Clifford route and the comparison of conventions written here.*

What is the spin group of Minkowski space, and what are its finite-dimensional representations? The course reaches $SL(2, \mathbb C)$ through Hermitian $2\times2$ matrices ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]–[[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) and the representations $(j_+, j_-)$ through the complexified algebra ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]). This section gives the Clifford route: $\mathrm{Cl}^0(1,3) \cong \mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, so $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$, with $\rho$ the course's covering map up to the automorphism $\lambda \mapsto (\lambda^\dagger)^{-1}$; then it identifies the finite-dimensional representations of $SL(2, \mathbb C)$ with pairs of $\mathfrak{sl}(2, \mathbb C)$-representations and the $(j_+, j_-)$, and decides which of them descend to $SO^+(1,3)$. It is the four-dimensional sequel of [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half|§CB.10]], using [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification|§CB.2]] (real forms, $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$) and [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)|§CB.9]].

Throughout, $V = \mathbb R^{1,3}$ with $q(x) = g(x, x)$, $g = \operatorname{diag}(+,-,-,-)$, and $e_0, \dots, e_3$ the standard basis ($q(e_0) = 1$, $q(e_i) = -1$).

## The even Clifford algebra of Minkowski space

> [!theorem] Theorem §CB.11.1: Cl⁰(1,3) ≅ Cl(3,0) ≅ M₂(ℂ)
> The elements $f_i = e_ie_0$ ($i = 1, 2, 3$) of $\mathrm{Cl}^0(1,3)$ satisfy $f_i^2 = +1$ and $f_if_j = -f_jf_i$ ($i \ne j$), and $e_i \mapsto f_i$ extends to an isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]] with $\epsilon = 1$). Composed with [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-1|Theorem §CB.10.1]] it gives an isomorphism of real algebras $\phi : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$, $\phi(f_i) = \sigma^i$, with $\phi(\omega) = i\mathbb 1$ for $\omega = e_0e_1e_2e_3 = f_1f_2f_3$. Under $\phi$ the map $x \mapsto xe_0$, $V \to \mathrm{Cl}^0$, sends $x = x^\mu e_\mu$ to the Hermitian matrix $\tilde x = x^0\mathbb 1 + x^i\sigma^i$, which is $\bar X = x_\mu\bar\sigma^\mu$ of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]] (not the course's $X = x_\mu\sigma^\mu$).
>
> *Source: written here · the matrices $x^0 + \mathbf x\cdot\boldsymbol\sigma$ for four-vectors: P. Woit, Quantum Theory, Groups and Representations, §40.4*

^thm-cb-11-1

> [!proof]- Proof
> Orthogonal vectors anticommute in $\mathrm{Cl}(1,3)$: $uv + vu = 2B(u, v)$ ([[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]]), and $e_\mu \perp e_\nu$ for $\mu \ne \nu$. Also $e_0^2 = q(e_0) = 1$ and $e_i^2 = q(e_i) = -1$.
>
> **1. Squares.** $f_i^2 = e_ie_0e_ie_0 = -e_ie_ie_0e_0 = -(-1)(1) = 1$, moving the middle $e_0$ past $e_i$ (one sign).
>
> **2. Anticommutation.** For $i \ne j$: $f_if_j = e_ie_0e_je_0 = -e_ie_je_0e_0 = -e_ie_j$, and likewise $f_jf_i = -e_je_i = e_ie_j$. So $f_if_j = -f_jf_i$. ⚑ By-product: $e_ie_j = -f_if_j$, used for the rotation generators in Theorem §CB.11.3.
>
> **3. The even subalgebra is Cl(3,0).** In Theorem §CB.7.20 take $e_0$ with $q(e_0) = \epsilon = 1$; then $V' = e_0^\perp = \operatorname{span}\{e_1, e_2, e_3\}$ with $q'(v') = -\epsilon q(v') = -q(v')$, so $q'(e_i) = +1$: $(V', q') = \mathbb R^{3,0}$. The isomorphism $\mathrm{Cl}(3,0) \cong \mathrm{Cl}^0(1,3)$ of that theorem is $v' \mapsto v'e_0$, i.e. $e_i \mapsto f_i$; steps 1–2 are the relations it requires.
>
> **4. The matrix algebra.** Theorem §CB.10.1 gives the real-algebra isomorphism $\mathrm{Cl}(3,0) \cong M_2(\mathbb C)$, $e_i \mapsto \sigma^i$. Composing with the inverse of step 3 gives $\phi$ with $\phi(f_i) = \sigma^i$. In particular the $f_i$ generate $\mathrm{Cl}^0(1,3)$ as a real algebra, since the $e_i$ generate $\mathrm{Cl}(3,0)$.
>
> **5. The volume element.** $f_1f_2 = -e_1e_2$ (step 2), so $f_1f_2f_3 = -e_1e_2e_3e_0$. Moving $e_0$ to the front past $e_3$, $e_2$, $e_1$ costs $(-1)^3$: $f_1f_2f_3 = e_0e_1e_2e_3 = \omega$. Hence $\phi(\omega) = \sigma^1\sigma^2\sigma^3 = i\mathbb 1$ (Theorem §CB.10.1).
>
> **6. Four-vectors.** $xe_0 = x^0e_0e_0 + x^ie_ie_0 = x^0 + x^if_i$, so $\phi(xe_0) = x^0\mathbb 1 + x^i\sigma^i$. With $x_0 = x^0$, $x_i = -x^i$ and $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ (Def. §C5a.1.10), $x_\mu\bar\sigma^\mu = x^0\mathbb 1 + x^i\sigma^i = \bar X$.
>
> **What the proof shows**
> - The course's Hermitian $2\times2$ picture of a four-vector is the Clifford product $xe_0$, read in $\mathrm{Cl}^0 \cong M_2(\mathbb C)$.
> - ⚑ By-product (a convention): the natural Clifford identification gives $\bar X = x_\mu\bar\sigma^\mu$, while the course's covering map is built on $X = x_\mu\sigma^\mu$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]]). The two differ by $\sigma^i \to -\sigma^i$; its effect on the group is worked out in Theorem §CB.11.2, 2.
> - Used next: Theorems §CB.11.2–§CB.11.3, and the Dirac module in §CB.12.

^pf-cb-11-1

*Uses:* [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-8|Theorem §CB.7.8]], [[§CB.7 Clifford Algebras꞉ Definition, Grading, Basis and Volume Element#^thm-cb-7-20|Theorem §CB.7.20]], [[§CB.10 Three Dimensions꞉ Cl(3), Spin(3) = SU(2) and Spin One-Half#^thm-cb-10-1|Theorem §CB.10.1]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-10|Def. §C5a.1.10]]

## Spin(1,3) and SL(2,ℂ)

> [!theorem] Theorem §CB.11.2: Spin(1,3)₀ Is SL(2,ℂ), and ρ Is the Course's Covering Map up to λ ↦ (λ†)⁻¹
> 1. The isomorphism $\phi$ of [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-1|Theorem §CB.11.1]] restricts to an isomorphism of Lie groups from $\mathrm{Spin}(1,3)_0$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-6|Def. §CB.9.6]]) onto $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-3|Def. §C5a.4.3]]).
> 2. For $x \in \mathrm{Spin}(1,3)_0$ and $\lambda = \phi(x)$, $\rho(x)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]]) acts on $\tilde x = x_\mu\bar\sigma^\mu$ (Theorem §CB.11.1) by $\tilde x \mapsto \lambda\tilde x\lambda^\dagger$, and $\ker\rho = \{\pm1\}$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-12|Theorem §CB.9.12]]). The course's covering $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]) acts instead on $X = x_\mu\sigma^\mu$ by $X \mapsto \mu X\mu^\dagger$, and
>
> $$
> \rho(x) = \pi\bigl(\theta(\phi(x))\bigr), \qquad \theta(\lambda) = (\lambda^\dagger)^{-1} .
> $$
>
> So the element of $\mathrm{Spin}(1,3)_0$ over $e^\omega$ is sent by $\phi$ to $\pm\Lambda_R(\omega)$ and by $\theta\circ\phi$ to $\pm\Lambda_L(\omega)$ (the Weyl matrices, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^def-c5a-4-1|Def. §C5a.4.1]]); $\theta\circ\phi$ is the restriction of the real-algebra isomorphism $\phi' : \mathrm{Cl}^0(1,3) \to M_2(\mathbb C)$ with $\phi'(f_i) = -\sigma^i$, $\phi'(xe_0) = X$, and $\rho = \pi\circ\phi'$ on $\mathrm{Spin}(1,3)_0$.
> 3. $\phi$ maps $\mathrm{Spin}(1,3)$ onto $\{A \in M_2(\mathbb C) : \det A = \pm1\}$. $\mathrm{Spin}(1,3)$ has two components, $\mathrm{Spin}(1,3)_0$ and $e_0e_1\,\mathrm{Spin}(1,3)_0$; $\rho(e_0e_1) = \operatorname{diag}(-1, -1, 1, 1)$, and $\rho$ maps the two components onto $SO^+(1,3)$ and onto $\mathcal P\mathcal T\cdot SO^+(1,3)$, the component of $SO(1,3)$ containing $\mathcal P\mathcal T$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]]).
>
> *Source: written here · the action $\Omega(\cdot)\Omega^\dagger$ on $x^0 + \mathbf x\cdot\boldsymbol\sigma$: P. Woit, Quantum Theory, Groups and Representations, §40.4 (https://www.math.columbia.edu/~woit/QM/qmbook.pdf) · the course's covering: [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (the user's PHY 513 notes, Ch. 8 §8.2; Yu Exercise 3.7)*

^thm-cb-11-2

> [!proof]- Proof
> Notation: $\tilde v = \phi(ve_0) = v_\mu\bar\sigma^\mu$ for $v \in V$ (Theorem §CB.11.1, 6); $\theta(\lambda) = (\lambda^\dagger)^{-1}$.
>
> **1. Conjugation by e₀.** Since $e_0^2 = 1$, $\kappa(a) = e_0ae_0$ is an algebra automorphism of $\mathrm{Cl}^0(1,3)$: $\kappa(ab) = e_0ae_0e_0be_0 = \kappa(a)\kappa(b)$. On the generators, $\kappa(f_i) = e_0e_ie_0e_0 = e_0e_i = -e_ie_0 = -f_i$.
>
> **2. Its matrix form.** $\tilde\kappa(A) = \sigma^2\bar A\sigma^2$ ($\bar A$ the entrywise conjugate) is a real-algebra automorphism of $M_2(\mathbb C)$: real-linear, $\tilde\kappa(AB) = \sigma^2\bar A\sigma^2\sigma^2\bar B\sigma^2 = \tilde\kappa(A)\tilde\kappa(B)$ because $(\sigma^2)^2 = \mathbb 1$, $\tilde\kappa(\mathbb 1) = \mathbb 1$. By [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], 3, $\sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$, so $\tilde\kappa(\sigma^i) = -\sigma^i$. Thus $\phi\circ\kappa$ and $\tilde\kappa\circ\phi$ are real-algebra homomorphisms $\mathrm{Cl}^0 \to M_2(\mathbb C)$ that agree on the generators $f_i$ (both give $-\sigma^i$; Theorem §CB.11.1, 4), hence everywhere: $\phi(\kappa(a)) = \tilde\kappa(\phi(a))$.
>
> **3. On determinant ±1, κ̃ is ±θ.** By [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-15|Theorem §CB.4.15]], 1, applied to $\bar A$: $\bar A^{\mathsf T}\varepsilon\bar A = \overline{\det A}\,\varepsilon$, so for invertible $A$, $\varepsilon\bar A\varepsilon^{-1} = \overline{\det A}\,(\bar A^{\mathsf T})^{-1} = \overline{\det A}\,(A^\dagger)^{-1}$. With $\varepsilon = i\sigma^2$, $\varepsilon^{-1} = -i\sigma^2$, the left side is $\sigma^2\bar A\sigma^2$. Hence
>
> $$
> \tilde\kappa(A) = \overline{\det A}\;\theta(A), \qquad \text{in particular } \tilde\kappa = \theta \text{ on } SL(2, \mathbb C) .
> $$
>
> **4. The determinant of a product of two vectors.** For $u, v \in V$: $uv = (ue_0)(e_0v)$ and $e_0v = e_0(ve_0)e_0 = \kappa(ve_0)$. So $\phi(uv) = \tilde u\,\tilde\kappa(\tilde v)$, and $\det\phi(uv) = \det\tilde u\cdot\overline{\det\tilde v} = q(u)\,q(v)$, since $\det\tilde v = \det(v_\mu\bar\sigma^\mu) = v_\mu v^\mu = q(v)$ is real ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], 2).
>
> **5. Spin(1,3)₀ lands in SL(2,ℂ).** Every $x \in \mathrm{Spin}(1,3)$ is $u_1u_2\cdots u_{2k}$ with $q(u_i) = \pm1$ (Def. §CB.9.6). Grouping the factors in pairs and using step 4 and $\det(AB) = \det A\det B$: $\det\phi(x) = \prod_iq(u_i) = \pm1$. On $\mathrm{Spin}(1,3)_0$, $\det\circ\phi$ is continuous with values in $\{\pm1\}$ and equals $1$ at $x = 1$; $\mathrm{Spin}(1,3)_0$ is connected ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], 1), so $\det\phi(x) = 1$.
>
> **6. The action on four-vectors.** For $x \in \mathrm{Spin}(1,3)$ and $v \in V$, $\rho(x)v = xvx^{-1}$ (Theorem §CB.9.7, 2). Inserting $e_0e_0 = 1$: $(\rho(x)v)e_0 = x(ve_0)(e_0x^{-1}e_0) = x\,(ve_0)\,\kappa(x^{-1})$. Apply $\phi$, step 2 and step 3 with $d = \det\phi(x) = \pm1$ (so $\overline{\det\phi(x)^{-1}} = d$ and $\theta(\lambda^{-1}) = \lambda^\dagger$):
>
> $$
> \widetilde{\rho(x)v} = \lambda\,\tilde v\,\tilde\kappa(\lambda^{-1}) = d\,\lambda\,\tilde v\,\lambda^\dagger, \qquad \lambda = \phi(x) .
> $$
>
> For $x \in \mathrm{Spin}(1,3)_0$ ($d = 1$, step 5) this is $\tilde v \mapsto \lambda\tilde v\lambda^\dagger$, the first claim of part 2.
>
> **7. Comparison with π.** $X = v_\mu\sigma^\mu = v^0\mathbb 1 - v^i\sigma^i = \tilde\kappa(\tilde v)$ (step 2, real coefficients). Applying the automorphism $\tilde\kappa$ to step 6 ($d = 1$): $X \mapsto \tilde\kappa(\lambda)\,X\,\tilde\kappa(\lambda^\dagger) = \theta(\lambda)\,X\,\theta(\lambda^\dagger)$, and $\theta(\lambda^\dagger) = \lambda^{-1} = \theta(\lambda)^\dagger$. So $\rho(x)$ acts on $X$ as $X \mapsto \mu X\mu^\dagger$ with $\mu = \theta(\lambda)$, which is the definition of $\pi(\mu)$ (Theorem §C5a.4.4): $\rho(x) = \pi(\theta(\phi(x)))$.
>
> **8. Onto SL(2,ℂ).** Let $\mu \in SL(2, \mathbb C)$. $\pi(\theta(\mu)) \in SO^+(1,3)$, and $SO^+(1,3)$ is the identity component of $O(1,3)$ ([[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], 2). $V = \mathbb R^{1,3}$ contains the negative definite plane $\operatorname{span}\{e_1, e_2\}$, so $\rho : \mathrm{Spin}(1,3)_0 \to SO^+(1,3)$ is onto and $-1 \in \mathrm{Spin}(1,3)_0$ (Theorem §CB.9.12). Pick $x$ with $\rho(x) = \pi(\theta(\mu))$; by step 7, $\pi(\theta(\phi(x))) = \pi(\theta(\mu))$, so $\theta(\phi(x)) = \pm\theta(\mu)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]]) and $\phi(x) = \pm\mu$ ($\theta$ is a bijection with $\theta(-\lambda) = -\theta(\lambda)$). If the sign is $-$, replace $x$ by $-x \in \mathrm{Spin}(1,3)_0$. So $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$.
>
> **9. Part 1.** $\phi$ is an injective algebra homomorphism and a linear isomorphism of finite-dimensional spaces, so its restriction to $\mathrm{Spin}(1,3)_0$ is an injective group homomorphism, continuous with continuous inverse, onto $SL(2, \mathbb C)$ by step 8: an isomorphism of Lie groups ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]).
>
> **10. The kernel and the Weyl matrices.** $\rho(x) = \mathbb 1$ iff $\theta(\phi(x)) = \pm\mathbb 1$ (step 7, Theorem §C5a.4.5) iff $\phi(x) = \pm\mathbb 1$ iff $x = \pm1$. Since $\pi(\Lambda_L(\omega)) = e^\omega$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], 1), $\rho(x) = e^\omega$ iff $\theta(\phi(x)) = \pm\Lambda_L(\omega)$ iff $\phi(x) = \pm\theta(\Lambda_L(\omega)) = \pm\Lambda_R(\omega)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], 2). Finally $\phi' = \tilde\kappa\circ\phi$ is a real-algebra isomorphism with $\phi'(f_i) = -\sigma^i$ and $\phi'(xe_0) = \tilde\kappa(\tilde x) = X$, equal to $\theta\circ\phi$ on $\mathrm{Spin}(1,3)_0$ (step 3), so $\rho = \pi\circ\phi'$ there.
>
> **11. Part 3.** By step 5, $\phi(\mathrm{Spin}(1,3)) \subset \{\det = \pm1\}$. $e_0e_1 \in \mathrm{Spin}(1,3)$, $e_0e_1 = -e_1e_0 = -f_1$, $\phi(e_0e_1) = -\sigma^1$ with determinant $-1$, and $(e_0e_1)^2 = -e_0e_0e_1e_1 = 1$. If $y \in \mathrm{Spin}(1,3)$ has $\det\phi(y) = -1$, then $e_0e_1y \in \mathrm{Spin}(1,3)$ has determinant $1$, so $\phi(e_0e_1y) \in SL(2, \mathbb C) = \phi(\mathrm{Spin}(1,3)_0)$ and, $\phi$ being injective, $e_0e_1y \in \mathrm{Spin}(1,3)_0$, i.e. $y \in e_0e_1\mathrm{Spin}(1,3)_0$. The two pieces are the preimages of $\det = 1$ and $\det = -1$, disjoint, open and closed, each connected (homeomorphic to $\mathrm{Spin}(1,3)_0$); their images under $\phi$ fill $\{\det = \pm1\}$ ($\phi(e_0e_1)SL(2, \mathbb C) = \{\det = -1\}$). By Theorem §CB.9.7, 2, $\rho(e_0e_1) = r_{e_0}r_{e_1}$, the product of the reflections $e_0 \mapsto -e_0$ and $e_1 \mapsto -e_1$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]]): $\operatorname{diag}(-1, -1, 1, 1)$, with determinant $+1$ and $\Lambda^0{}_0 = -1$, the same signs as $\mathcal P\mathcal T = -\mathbb 1$, so it lies in $\mathcal P\mathcal T\cdot SO^+(1,3)$ (Theorem §C1a.4.2, 1–2), and $\rho(e_0e_1\mathrm{Spin}(1,3)_0) = \rho(e_0e_1)\,SO^+(1,3) = \mathcal P\mathcal T\cdot SO^+(1,3)$.
>
> **What the proof shows**
> - The Clifford route and the course's route reach the same group, but the natural identifications differ by the automorphism $\theta(\lambda) = (\lambda^\dagger)^{-1}$, which exchanges $\Lambda_L$ and $\Lambda_R$. ⚑ By-product: "which matrix is $\lambda$" is a convention, fixed in the course by building $\pi$ on $X = x_\mu\sigma^\mu$; the Clifford algebra with $f_i \mapsto \sigma^i$ builds it on $\bar X$. Every later statement that names $(\frac12, 0)$ fixes the convention (Theorem §CB.11.5, Theorem §CB.12.2).
> - Step 6 for $d = -1$ shows that the other component acts by $\tilde v \mapsto -\lambda\tilde v\lambda^\dagger$: the minus sign reverses time, as $\mathcal P\mathcal T$ does.
> - Used next: the Lie algebra version (Theorem §CB.11.3) and the Dirac module restricted to $\mathrm{Spin}(1,3)_0$ (Theorem §CB.12.2).

^pf-cb-11-2

*Uses:* [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-1|Theorem §CB.11.1]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-6|Def. §CB.9.6]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-4|Theorem §CB.9.4]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-7|Theorem §CB.9.7]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-12|Theorem §CB.9.12]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-15|Theorem §CB.4.15]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§C5a.1 Spinor Space and the Clifford Action#^thm-c5a-1-9|Theorem §C5a.1.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-1|Theorem §C5a.4.1]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]], [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]]

The course's route — four-vectors as Hermitian matrices, $SL(2, \mathbb C)$ connected and simply connected, the double cover — proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]] (both routes are kept):

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3]]

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7]]

> [!theorem] Theorem §CB.11.3: The Three Lie Algebras Agree
> Under $\phi$ ([[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-1|Theorem §CB.11.1]]), $\mathfrak{spin}(1,3)$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]]) maps isomorphically onto $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]]): $\frac12e_ie_j = -\frac12f_if_j \mapsto -\frac i2\varepsilon_{ijk}\sigma^k$ (rotations) and $\frac12e_ie_0 \mapsto \frac12\sigma^i$ (boosts). The differential $\rho_\ast$ ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]]) is $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu} = g_{\mu\alpha}g_{\nu\beta}M^{\alpha\beta}$, the generators of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]] with lowered indices; so $\rho_\ast\circ\phi^{-1}$ sends $-\frac i2\sigma^k \mapsto -iJ_k$ and $\frac12\sigma^k \mapsto -iK_k$ ([[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]]). It equals $\pi_\ast\circ\theta_\ast$, with $\pi_\ast$ the isomorphism of [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]] ($-\frac i2\sigma^k \mapsto -iJ_k$, $-\frac12\sigma^k \mapsto -iK_k$) and $\theta_\ast(Y) = -Y^\dagger$ the differential of $\theta(\lambda) = (\lambda^\dagger)^{-1}$ ([[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-2|Theorem §CB.11.2]]).
>
> *Source: written here*

^thm-cb-11-3

> [!proof]- Proof
> **1. A basis.** $\mathfrak{spin}(1,3)$ is spanned by the six products $e_\mu e_\nu$, $\mu < \nu$ (Def. §CB.9.13), and it is the Lie algebra of $\mathrm{Spin}(1,3)$ (Theorem §CB.9.14, 1).
>
> **2. The images.** $\phi(e_ie_0) = \phi(f_i) = \sigma^i$. For $i \ne j$, $e_ie_j = -f_if_j$ (Theorem §CB.11.1, Proof, step 2), and $\sigma^i\sigma^j = i\varepsilon_{ijk}\sigma^k$ for $i \ne j$ ([[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], 3), so $\phi(\frac12e_ie_j) = -\frac12\sigma^i\sigma^j = -\frac i2\varepsilon_{ijk}\sigma^k$.
>
> **3. An isomorphism onto 𝔰𝔩(2,ℂ)_ℝ.** The images $\frac12\sigma^k$, $-\frac i2\sigma^k$ ($k = 1, 2, 3$) are a real basis of the traceless matrices, because $\sigma^1, \sigma^2, \sigma^3$ are a complex basis of them (QM Theorem §B6.1.4, 4). These form $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, of real dimension $6$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]]). $\phi$ is injective and multiplicative, so it preserves commutators, and its restriction is a Lie algebra isomorphism $\mathfrak{spin}(1,3) \cong \mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ — consistently with $\phi(\mathrm{Spin}(1,3)_0) = SL(2, \mathbb C)$ (Theorem §CB.11.2, 1).
>
> **4. The differential of ρ in components.** By Theorem §CB.9.14, 2, $\rho_\ast(\frac12e_\mu e_\nu)(v) = B(e_\nu, v)e_\mu - B(e_\mu, v)e_\nu = v_\nu e_\mu - v_\mu e_\nu$, i.e. the matrix $(\rho_\ast(\frac12e_\mu e_\nu))^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. Lowering both labels of $(M^{\alpha\beta})^\rho{}_\sigma = g^{\alpha\rho}\delta^\beta_\sigma - g^{\beta\rho}\delta^\alpha_\sigma$ (Def. §C1a.6.1): $g_{\mu\alpha}g_{\nu\beta}(M^{\alpha\beta})^\rho{}_\sigma = \delta^\rho_\mu g_{\nu\sigma} - \delta^\rho_\nu g_{\mu\sigma}$. So $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$.
>
> **5. Rotations and boosts.** For spatial $i, j$: $M_{ij} = g_{ii}g_{jj}M^{ij} = M^{ij} = -i\mathcal J^{ij} = -i\varepsilon_{ijk}J_k$, since $J_k = \frac12\varepsilon_{klm}\mathcal J^{lm}$ gives $\mathcal J^{ij} = \varepsilon_{ijk}J_k$ (Def. §C1a.6.2). With step 2: $\rho_\ast\phi^{-1}(-\frac i2\varepsilon_{ijk}\sigma^k) = -i\varepsilon_{ijk}J_k$, i.e. $-\frac i2\sigma^k \mapsto -iJ_k$. For boosts: $M_{k0} = g_{kk}g_{00}M^{k0} = -M^{k0} = M^{0k} = -i\mathcal J^{0k} = -iK_k$, and $\phi(\frac12e_ke_0) = \frac12\sigma^k$, so $\frac12\sigma^k \mapsto -iK_k$. Check on $v$: $\rho_\ast(\frac12e_ke_0)$ sends $e_0 \mapsto e_k$ and $e_k \mapsto e_0$, the generator of a boost along $+e_k$.
>
> **6. Comparison with the differential of π.** $\theta$ is a continuous homomorphism of $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 1), and $\theta(e^{sY}) = ((e^{sY})^\dagger)^{-1} = e^{-sY^\dagger}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], 2 and 4), so $\theta_\ast(Y) = \frac{d}{ds}e^{-sY^\dagger}\big|_0 = -Y^\dagger$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]]). Then $\theta_\ast(-\frac i2\sigma^k) = -\frac i2\sigma^k$ and $\theta_\ast(\frac12\sigma^k) = -\frac12\sigma^k$, and Theorem §CB.2.17 gives $\pi_\ast\theta_\ast(-\frac i2\sigma^k) = -iJ_k$, $\pi_\ast\theta_\ast(\frac12\sigma^k) = -iK_k$: the same values as step 5 on a basis, so $\rho_\ast\circ\phi^{-1} = \pi_\ast\circ\theta_\ast$. (This is also the chain rule applied to $\rho = \pi\circ\theta\circ\phi$, Theorem §CB.11.2, 2.)
>
> **What the proof shows**
> - $\rho_\ast(\frac12e_\mu e_\nu) = M_{\mu\nu}$: in the Clifford algebra the generator of the $\mu\nu$-plane is half the product of the two basis vectors, with the metric lowering the labels. Hence $\exp(\frac14\omega^{\mu\nu}e_\mu e_\nu)$ covers $e^\omega = \exp(\frac12\omega_{\mu\nu}M^{\mu\nu})$, used in Theorem §CB.12.2.
> - ⚑ By-product: rotations are the same through $\phi$ and through the course's $\pi$; boosts differ by a sign. That sign is the automorphism $\theta$, i.e. the exchange of $\Lambda_L$ and $\Lambda_R$ (Theorem §CB.11.2, 2).

^pf-cb-11-3

*Uses:* [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-13|Def. §CB.9.13]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-9-14|Theorem §CB.9.14]], [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-1|Theorem §CB.11.1]], [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-2|Theorem §CB.11.2]], [[§B6.1 Spin One-Half and the Pauli Matrices#^thm-b6-1-4|QM Theorem §B6.1.4]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-2|Theorem §CB.1.2]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-11|Theorem §CB.1.11]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-1|Def. §C1a.6.1]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]

## The finite-dimensional representations of SL(2,ℂ)

> [!theorem] Theorem §CB.11.4: Representations of SL(2,ℂ) Are Pairs of 𝔰𝔩(2,ℂ)-Representations
> For finite-dimensional representations on complex spaces, the following correspond bijectively, preserving invariant subspaces, irreducibility and intertwiners: continuous representations of $SL(2, \mathbb C)$; representations of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-24|Theorem §CB.1.24]], $SL(2, \mathbb C)$ being simply connected, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]); commuting pairs $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-19|Theorem §CB.2.19]]); complex-linear representations of $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]]). All of them are completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]).
>
> *Source: written here (assembly of the cited theorems)*

^thm-cb-11-4

> [!proof]- Proof
> **1. Group to algebra.** A continuous representation $D : SL(2, \mathbb C) \to GL(W)$ is a Lie group homomorphism ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]]); its differential $d = D_\ast$ is a representation of the Lie algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^def-cb-2-16|Def. §CB.2.16]]).
>
> **2. Algebra to group, bijectively.** $SL(2, \mathbb C)$ is connected and simply connected ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]]), so every representation $d$ of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ is $D_\ast$ for exactly one $D$ ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-24|Theorem §CB.1.24]]). Two representations with the same differential are equal ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]]). So $D \mapsto D_\ast$ is a bijection.
>
> **3. Intertwiners agree.** Let $T : W_1 \to W_2$ be linear. If $TD_1(g) = D_2(g)T$ for all $g$, then differentiating $TD_1(e^{sX}) = D_2(e^{sX})T$ at $s = 0$ gives $Td_1(X) = d_2(X)T$ (Theorem §CB.1.14). Conversely, if $Td_1(X) = d_2(X)T$, then $Td_1(X)^n = d_2(X)^nT$ for all $n$, and summing the series $TD_1(e^X) = Te^{d_1(X)} = e^{d_2(X)}T = D_2(e^X)T$; every $g$ is a product of exponentials ([[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], 3), so $TD_1(g) = D_2(g)T$. In particular $D_1 \cong D_2$ iff $d_1 \cong d_2$ (invertible intertwiners, [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]]).
>
> **4. Invariant subspaces agree.** If $W' \subset W$ is invariant under all $D(g)$, then $d(X)w = \lim_{s\to0}\frac1s(D(e^{sX})w - w) \in W'$ for $w \in W'$ ($W'$ is closed, being finite-dimensional). If $W'$ is invariant under all $d(X)$, it is invariant under every power and hence under $e^{d(X)} = D(e^X)$, and so under all products of exponentials, i.e. all of $SL(2, \mathbb C)$ (Theorem §CB.1.16, 3). Hence irreducibility agrees too.
>
> **5. The other two descriptions.** A representation of the real algebra $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on the complex space $W$ is the same as a commuting pair $(\rho_1, \rho_2)$ of a complex-linear and an antilinear representation ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-19|Theorem §CB.2.19]]), and the same as a complex-linear representation of its complexification ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], 1), with the same invariant subspaces and intertwiners (Theorem §CB.2.6, 2). The complexification is isomorphic to $\mathfrak{sl}(2, \mathbb C)\oplus\mathfrak{sl}(2, \mathbb C)$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]]), and pulling back along an isomorphism of Lie algebras changes neither invariant subspaces nor intertwiners. The isomorphism $\mathfrak{sl}(2, \mathbb C)_{\mathbb R} \cong \mathfrak{so}(1,3)$ is [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]].
>
> **6. Complete reducibility.** Every finite-dimensional representation of $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$ on a complex space is completely reducible ([[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]); by step 4 the same decomposition into invariant subspaces works for the group.
>
> **What the proof shows**
> - Simple connectivity of $SL(2, \mathbb C)$ is what makes every algebra representation a group representation; for $SO^+(1,3)$ only those with $D(-\mathbb 1) = \mathbb 1$ survive (Theorem §CB.11.6).
> - Continuity is the only regularity assumed on the group side: differentiability comes from the matrix Lie group theory of §CB.1.

^pf-cb-11-4

*Uses:* [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^def-cb-1-12|Def. §CB.1.12]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-14|Theorem §CB.1.14]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-16|Theorem §CB.1.16]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-17|Theorem §CB.1.17]], [[§CB.1 Matrix Lie Groups, the Exponential Map and Lie Algebras#^thm-cb-1-24|Theorem §CB.1.24]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-3|Theorem §C5a.4.3]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-18|Theorem §CB.2.18]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-19|Theorem §CB.2.19]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^def-cb-3-1|Def. §CB.3.1]], [[§CB.3 Representations꞉ Intertwiners, Schur's Lemma, Complete Reducibility and Casimirs#^thm-cb-3-15|Theorem §CB.3.15]]

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
> ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]]; $(\lambda^\dagger)^{-1} \cong \bar\lambda$ by [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-16|Theorem §CB.4.16]]) is an irreducible representation of $SL(2, \mathbb C)$ of dimension $(2j_+ + 1)(2j_- + 1)$, whose generators, read through the course's covering $\pi$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), are those of $(j_+, j_-)$: $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1}$ is equivalent to the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]; which factor carries $\mathbf J_+$ is fixed by [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]]). Every finite-dimensional irreducible continuous representation of $SL(2, \mathbb C)$ is equivalent to exactly one $D^{(j_+, j_-)}$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.3, Ch. 8 §8.2, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]] and [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]] · written here (from Theorems §CB.11.4, §CB.4.5, §CB.6.3)*

^thm-cb-11-5

> [!proof]- Proof
> Write $\theta(\lambda) = (\lambda^\dagger)^{-1}$ and $\operatorname{Sym}^k(A)$ for the restriction of $A^{\otimes k}$ to $\operatorname{Sym}^k\mathbb C^2$.
>
> **1. A continuous representation.** $\operatorname{Sym}^k\mathbb C^2$ is invariant under $A^{\otimes k}$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], 1), and $(AB)^{\otimes k} = A^{\otimes k}B^{\otimes k}$, so $A \mapsto \operatorname{Sym}^k(A)$ is a homomorphism. $\theta$ is a homomorphism of $SL(2, \mathbb C)$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 1), and a tensor product of representations is one. The entries of $D^{(j_+, j_-)}(\lambda)$ are polynomials in the entries of $\lambda$ and $\bar\lambda$ ($\lambda^{-1}$ is the adjugate, since $\det\lambda = 1$), so $D^{(j_+, j_-)}$ is continuous. Its dimension is $\dim\operatorname{Sym}^{2j_+}\mathbb C^2\cdot\dim\operatorname{Sym}^{2j_-}\mathbb C^2 = (2j_+ + 1)(2j_- + 1)$ (Theorem §CB.4.13, 1, $\binom{2j+1}{2j} = 2j + 1$).
>
> **2. It is the course's representation.** By [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]], $\operatorname{Sym}^{2j}\mathbb C^2$ with $\operatorname{Sym}^{2j}(\lambda)$ is equivalent to the polynomial realization $P(z) \mapsto P(\lambda^{\mathsf T}z)$ on homogeneous polynomials of degree $2j$. The tensor product of the two equivalences is an equivalence of $D^{(j_+, j_-)}$ with $\tilde D(\lambda) = D^{(j_+)}(\lambda)\otimes D^{(j_-)}(\theta(\lambda))$ of Theorem §C5a.4.8.
>
> **3. Its generators.** Theorem §C5a.4.8, 1: $\tilde D(\Lambda_L(s\omega)) = \exp(-\frac{is}2\omega_{\mu\nu}D(\mathcal J^{\mu\nu}))$ with $D(\mathcal J^{\mu\nu})$ the generators of $(j_+, j_-)$ ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]]). $s \mapsto \Lambda_L(s\omega) = e^{sA_L(\omega)}$ is a one-parameter subgroup with $\pi_\ast(A_L(\omega)) = -\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}$ (it covers $e^{s\omega}$, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]]). Differentiating at $s = 0$: $\tilde D_\ast(A_L(\omega)) = d\bigl(\pi_\ast(A_L(\omega))\bigr)$, where $d$ is the representation $(j_+, j_-)$ of $\mathfrak{so}(1,3)$, $d(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu}) = -\frac i2\omega_{\mu\nu}D(\mathcal J^{\mu\nu})$. The $A_L(\omega)$ fill $\mathfrak{sl}(2, \mathbb C)_{\mathbb R}$, so $\tilde D_\ast = d\circ\pi_\ast$, and by step 2 $D^{(j_+, j_-)}_\ast\circ\pi_\ast^{-1} \cong d$ (equivalent group representations have equivalent differentials, [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-4|Theorem §CB.11.4]]).
>
> **4. Irreducible.** $(j_+, j_-)$ is irreducible ([[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]]), and $\pi_\ast$ is a bijection ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]]), so $D^{(j_+, j_-)}_\ast$ has no invariant subspaces but $0$ and the whole space; by Theorem §CB.11.4 neither has $D^{(j_+, j_-)}$.
>
> **5. Every irreducible representation is one of them.** Let $E$ be a finite-dimensional irreducible continuous representation. $E_\ast\circ\pi_\ast^{-1}$ is an irreducible representation of $\mathfrak{so}(1,3)$ (Theorem §CB.11.4). Its complex-linear extension to $\mathfrak{so}(1,3)_{\mathbb C} = \mathfrak a_+\oplus\mathfrak a_-$ ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], 2) is irreducible ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], 2), hence equivalent to $W_+\boxtimes W_-$ with $W_\pm$ irreducible representations of $\mathfrak a_\pm \cong \mathfrak{sl}(2, \mathbb C)$ ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-5|Theorem §CB.4.5]], 2), and each $W_\pm$ is some $V_{j_\pm}$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]], 3): $\mathbf J_+$ acts as $\mathbf J^{(j_+)}\otimes\mathbb 1$ and $\mathbf J_-$ as $\mathbb 1\otimes\mathbf J^{(j_-)}$, which is Def. §C3.3.1 (equivalently, [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]] with one summand). By step 3, $E_\ast \cong D^{(j_+, j_-)}_\ast$, so $E \cong D^{(j_+, j_-)}$ (Theorem §CB.11.4).
>
> **6. Exactly one.** If $D^{(j_+, j_-)} \cong D^{(k_+, k_-)}$, their differentials are equivalent, so $(j_+, j_-) \cong (k_+, k_-)$ as $\mathfrak{so}(1,3)$-representations, and the labels coincide (Theorem §C3.3.1, last clause).
>
> **What the proof shows**
> - $(j_+, j_-)$ is $2j_+$ symmetrized slots carrying $\lambda$ and $2j_-$ carrying $(\lambda^\dagger)^{-1}$ — undotted and dotted indices ([[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-16|Theorem §CB.4.16]]).
> - ⚑ By-product (convention): the labels are tied to $\pi$. Read through $\rho$ and the Clifford identification $\phi$, $x \mapsto D^{(j_+, j_-)}(\phi(x))$ is $D^{(j_+, j_-)}\circ\theta$ in the course's parametrization ($\phi = \theta\circ(\theta\circ\phi)$, Theorem §CB.11.2, 2), which is equivalent to $D^{(j_-, j_+)}$: the two factors exchange roles. This is the group form of [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^cau-c3-3-1|§C3.3, Caution: Which one is (½, 0) depends on the sign of K]].

^pf-cb-11-5

*Uses:* [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-5|Theorem §CB.4.5]], [[§CB.4 New Representations from Old꞉ Tensor Products, Duals, Conjugates and Invariant Tensors#^thm-cb-4-13|Theorem §CB.4.13]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-3|Theorem §CB.6.3]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-6|Theorem §CB.2.6]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], [[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-17|Theorem §CB.2.17]], [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-4|Theorem §CB.11.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-6|Theorem §C5a.4.6]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]]

> [!theorem] Theorem §CB.11.6: Which (j₊, j₋) Descend to SO⁺(1,3)
> $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2(j_+ + j_-)}\mathbb 1$. Hence $D^{(j_+, j_-)}$ is tensorial ([[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]]), i.e. a representation of $SO^+(1,3)$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]), iff $j_+ + j_- \in \mathbb Z$, and spinorial iff $j_+ + j_- \in \frac12 + \mathbb Z$.
>
> *Source: the user's PHY 513 notes, Ch. 7 §7.4.4, through [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], Derivation, step 6 · written here*

^thm-cb-11-6

> [!proof]- Proof
> **1. The value on −1.** $\operatorname{Sym}^{2j}(-\mathbb 1)$ is $(-\mathbb 1)^{\otimes2j} = (-1)^{2j}\mathbb 1$ restricted to $\operatorname{Sym}^{2j}\mathbb C^2$ ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]]), and $((-\mathbb 1)^\dagger)^{-1} = -\mathbb 1$. So $D^{(j_+, j_-)}(-\mathbb 1) = (-1)^{2j_+}\mathbb 1\otimes(-1)^{2j_-}\mathbb 1 = (-1)^{2(j_+ + j_-)}\mathbb 1$.
>
> **2. Tensorial or spinorial.** Under $\mathrm{Spin}(1,3)_0 \cong SL(2, \mathbb C)$ the element $-1$ goes to $-\mathbb 1$ ([[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-2|Theorem §CB.11.2]], 1, for either identification $\phi$ or $\theta\circ\phi$). $2(j_+ + j_-)$ is an integer; $(-1)^{2(j_+ + j_-)} = 1$ iff it is even, i.e. $j_+ + j_- \in \mathbb Z$ (tensorial, [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]]), and $= -1$ iff $j_+ + j_- \in \frac12 + \mathbb Z$ (spinorial).
>
> **3. Descent.** $\pi : SL(2, \mathbb C) \to SO^+(1,3)$ is a surjective covering homomorphism with kernel $\{\pm\mathbb 1\}$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]), as is $\rho$ on $\mathrm{Spin}(1,3)_0$ (Theorem §CB.11.2, 2). By the descent lemma ([[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]]) $D^{(j_+, j_-)}$ is $D\circ\pi$ for a representation $D$ of $SO^+(1,3)$ iff $D^{(j_+, j_-)}(-\mathbb 1) = \mathbb 1$, i.e. iff $j_+ + j_- \in \mathbb Z$, and then $D$ is irreducible.
>
> **What the proof shows**
> - The sign is the parity of the total number $2j_+ + 2j_-$ of spinor slots, each slot contributing one factor $-1$.

^pf-cb-11-6

*Uses:* [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-5|Theorem §CB.6.5]], [[§CB.6 SU(2) and SO(3)꞉ Spin j, Symmetric Powers and Clebsch–Gordan#^thm-cb-6-7|Theorem §CB.6.7]], [[§CB.9 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-9-17|Def. §CB.9.17]], [[§CB.11 The Lorentz Case I꞉ Spin(1,3), SL(2,C) and the Representations (j₊, j₋)#^thm-cb-11-2|Theorem §CB.11.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]]

The course's descent theorem, proved in [[§C5a.4 SL(2,C) and the Group Action on Spinor Space|§C5a.4]]:

![[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8]]

> [!remark]- Connections
> - The two routes to $SL(2, \mathbb C)$ meet at Theorem §CB.11.1: the Hermitian matrix $x^0 + \mathbf x\cdot\boldsymbol\sigma = x_\mu\bar\sigma^\mu$ is the Clifford product $x\,e_0$, and $\lambda\tilde x\lambda^\dagger$ is conjugation in the Clifford algebra read through $e_0$. The course builds its covering on $x_\mu\sigma^\mu$ instead; the two differ by $\lambda \mapsto (\lambda^\dagger)^{-1}$ (Theorem §CB.11.2, 2), which is why the Clifford identification calls $\Lambda_R$ what the course calls $\Lambda_L$.
> - The conjugation that exchanges the two $\mathfrak{sl}(2, \mathbb C)$ summands ([[§CB.2 Real Lie Algebras, the Physicists' i and Complexification#^thm-cb-2-12|Theorem §CB.2.12]], 3) is, on the group, $\lambda \mapsto (\lambda^\dagger)^{-1}$, the same map that relates the two factors of $D^{(j_+, j_-)}$ and the two Weyl matrices $\Lambda_L$, $\Lambda_R$ ([[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]).
> - **Used in**: Theorems §CB.11.1–§CB.11.3 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-2|Theorem §C5a.4.2]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-7|Theorem §C5a.4.7]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]; Theorems §CB.11.4–§CB.11.5 — [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^def-c3-3-1|Def. §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-1|Theorem §C3.3.1]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-2|Theorem §C3.3.2]], [[§C3.2 The Lorentz Algebra#^thm-c3-2-4|Theorem §C3.2.4]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-9|Theorem §C5a.4.9]]; Theorem §CB.11.6 — [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-8|Theorem §C5a.4.8]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-5|Theorem §C3.3.5]], [[§C3.3 Finite-Dimensional Representations of the Lorentz Algebra#^thm-c3-3-6|Theorem §C3.3.6]].
