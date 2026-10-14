---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 Practice Midterm 2 (Extended Set)|Extended Set]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Practice Midterm: Solutions

Solutions to [[PHY 513 Practice Midterm]] (Part I) and to [[PHY 513 Practice Midterm 2 (Extended Set)]] (Part II), folded so that you can try first. Each question is embedded above its solution. Every solution is derived step by step in the course's conventions ([[Larsen PHY 513]]) and ends with the line that says how it was checked: *Checked against* names the home box in these notes (or the submitted solution, "as written"); *Derived here; check* marks a variation that has no home box, derived from boxes that do exist, with the special case or method it was checked against. A solution is not a substitute for the box: when an answer surprises you, open the link.

---

# Part I. The practice paper

## Problem 1. Short response

![[PHY 513 Practice Midterm#Problem 1 (20 points). Short response]]

> [!success]- Answers
> 1. (a) $[G] = M^{-2}$ ($[\psi] = M^{3/2}$, so $[(\bar\psi\psi)^2] = M^6$ and $[G] = 4 - 6$; irrelevant); $[\kappa] = M^1$ ($4 - 3$; relevant). [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]].
> 2. (b) $\partial_\mu\partial^\mu\phi + m^2\phi + \dfrac{\lambda}{3!}\phi^3 = 0$ (from $\partial\mathcal L/\partial\phi = -m^2\phi - \frac{4\lambda}{4!}\phi^3$). [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]]; the cubic case is [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-2|Example §C1b.2.2]].
> 3. (c) $\gamma_\mu\slashed p\slashed q\gamma^\mu = 4\,p\cdot q$ (times $\mathbb 1_4$). [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]].
> 4. (d) $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^5) = -4i\,\varepsilon^{\mu\nu\rho\sigma}$ with $\varepsilon^{0123} = +1$; convention-free check: $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = \operatorname{tr}(-i\gamma^5\gamma^5) = -4i$. [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-4|Theorem §C5a.11.4]]; Peskin–Schroeder's sign: [[§C5a.11 Gamma-Matrix Technology#^cau-c5a-11-1|§C5a.11, Caution: The sign of the ε trace across sources]].
> 5. (e) $F^{\mu\nu}$: $(1, 0)\oplus(0, 1)$; Dirac spinor: $(\frac12, 0)\oplus(0, \frac12)$; $\dim(1, 1) = (2\cdot1 + 1)^2 = 9$. [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]].
> 6. (f) $\varepsilon_{0123} = -1$; $\varepsilon^{2301} = +1$ (two exchanges, $0\leftrightarrow2$ and $1\leftrightarrow3$); $\varepsilon^{0321} = -1$ (one exchange, $1\leftrightarrow3$). [[§CB.0 Linear Algebra in Components꞉ Bases, Changes of Basis, Duals and Tensors#^def-cb-0-16|Def. §CB.0.16]], [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]].
> 7. (g) $\tilde D_A(p) = \dfrac{i}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2}$: both poles moved up to $\pm E_{\mathbf p} + i\varepsilon$, so the contour passes **below both poles**. [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]].
> 8. (h) $\{\hat\psi_a(t, \mathbf x), \hat\psi^\dagger_b(t, \mathbf y)\} = \delta_{ab}\,\delta^3(\mathbf x - \mathbf y)$. [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-6|Principle §C5b.1.6]].
> 9. (i) $\mathsf V^\mu$ and $\mathsf T^{\mu\nu}$ (the others are $C$-even); $\Theta\,\mathsf T^{\mu\nu}(x)\,\Theta^{-1} = +\mathsf T^{\mu\nu}(-x)$, the sign $(-1)^n$ with $n = 2$. [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]].
> 10. (j) Dirac spinor: $-1$ (first back to $+\mathbb 1$ at $4\pi$); four-vector: $+1$. [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|Theorem §CB.17.9]], [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]] (the user's submitted Problem Set 6, Problem 4(d), as written: $\mathbb 1_4$ and $-\mathbb 1_4$).

^sol-pm-1

## Problem 2. The Lorentz group, two representations

### (a) Commutators of J and K; the sign convention of K

![[PHY 513 Practice Midterm#^pm-2-a]]

> [!success]- Solution
> **Answer.** $[J_1, K_2] = iK_3$, $[K_1, K_2] = -iJ_3$; in general $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$. With $K' = -K$ (Problem Set 5) neither commutator changes form; $\mathbf J'_\pm = \mathbf J_\mp$, so the labels $(\frac12, 0)$ and $(0, \frac12)$ are exchanged.
>
> **Step 1** (the generators). $J_1 = \frac12(\varepsilon_{123}\mathcal J^{23} + \varepsilon_{132}\mathcal J^{32}) = \mathcal J^{23}$, $J_3 = \mathcal J^{12}$, and $K_i = \mathcal J^{0i}$.
>
> **Step 2** ($[J_1, K_2]$). Put $(\mu\nu) = (23)$, $(\rho\sigma) = (02)$ in the algebra: $[\mathcal J^{23}, \mathcal J^{02}] = i\bigl(g^{30}\mathcal J^{22} - g^{20}\mathcal J^{32} - g^{32}\mathcal J^{20} + g^{22}\mathcal J^{30}\bigr)$. Off-diagonal $g$'s vanish and $\mathcal J^{22} = 0$, so only $g^{22} = -1$ survives: $= -i\mathcal J^{30} = +i\mathcal J^{03} = iK_3$.
>
> **Step 3** ($[K_1, K_2]$). $(\mu\nu) = (01)$, $(\rho\sigma) = (02)$: $[\mathcal J^{01}, \mathcal J^{02}] = i\bigl(g^{10}\mathcal J^{02} - g^{00}\mathcal J^{12} - g^{12}\mathcal J^{00} + g^{02}\mathcal J^{10}\bigr) = -i\,g^{00}\mathcal J^{12} = -iJ_3$. Both agree with $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$ at $(i, j, k) = (1, 2, 3)$.
>
> **Step 4** (the other sign). With $K'_i = \mathcal J^{i0} = -K_i$: $[J_i, K'_j] = -[J_i, K_j] = -i\varepsilon_{ijk}K_k = i\varepsilon_{ijk}K'_k$ (linear in $K$ on both sides: same form) and $[K'_i, K'_j] = (-1)^2[K_i, K_j] = -i\varepsilon_{ijk}J_k$ (quadratic in $K$: same form). But $\mathbf J'_\pm = \frac12(\mathbf J \pm i\mathbf K') = \frac12(\mathbf J \mp i\mathbf K) = \mathbf J_\mp$: the two commuting $\mathfrak{su}(2)$'s trade names, and with them the labels $j_+ \leftrightarrow j_-$. Nothing physical changes.
>
> *Checked against:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] (the $\mathbf J$, $\mathbf K$ form with $K_i = \mathcal J^{0i}$); [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]]; the user's Problem Set 5, Problem 1(a) (in the problem set's $K^i = \mathcal J^{i0}$, kept as [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6, third route]]).

^sol-pm-2-a

### (b) The boost along the 1-axis, vector and spinor

![[PHY 513 Practice Midterm#^pm-2-b]]

> [!success]- Solution
> **Answer.** With $C = \cosh\frac\eta2$, $S = \sinh\frac\eta2$,
> $$\Lambda(\eta) = \begin{pmatrix}\cosh\eta&\sinh\eta&0&0\\ \sinh\eta&\cosh\eta&0&0\\ 0&0&1&0\\ 0&0&0&1\end{pmatrix}, \qquad \Lambda_{1/2}(\eta) = \begin{pmatrix}C&-S&0&0\\ -S&C&0&0\\ 0&0&C&S\\ 0&0&S&C\end{pmatrix};$$
> $\Lambda(\eta)(m, 0, 0, 0) = (m\cosh\eta, m\sinh\eta, 0, 0)$: the particle moves along $+x$ with velocity $\tanh\eta$.
>
> **Step 1** (one generator). $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -\frac i2(\omega_{01}\mathcal J^{01} + \omega_{10}\mathcal J^{10}) = -\frac i2(\eta\mathcal J^{01} + (-\eta)(-\mathcal J^{01})) = -i\eta\mathcal J^{01} = -i\eta K_1$, by the antisymmetry of both $\omega$ and $\mathcal J$.
>
> **Step 2** (vector generator). $(-i\eta\mathcal J^{01})^\mu{}_\nu = -i\eta\cdot i(g^{0\mu}\delta^1{}_\nu - g^{1\mu}\delta^0{}_\nu) = \eta(g^{0\mu}\delta^1{}_\nu - g^{1\mu}\delta^0{}_\nu)$. Nonzero entries: $(\mu, \nu) = (0, 1)$: $\eta g^{00} = \eta$; $(\mu, \nu) = (1, 0)$: $-\eta g^{11} = +\eta$. So $-i\eta\mathcal J^{01} = \eta N$, $N = E_{01} + E_{10}$ (the matrix units in rows/columns $0, 1$).
>
> **Step 3** (exponentiate). $N^2 = E_{00} + E_{11}$, $N^3 = N$, so $e^{\eta N} = \mathbb 1 + (\cosh\eta - 1)N^2 + \sinh\eta\,N$: the matrix above. It is symmetric and satisfies $\Lambda^{\mathsf T}g\Lambda = g$ ($\cosh^2 - \sinh^2 = 1$).
>
> **Step 4** (spinor generator). $S^{01} = \frac i4[\gamma^0, \gamma^1] = \frac i2\gamma^0\gamma^1$ ($\gamma^0$, $\gamma^1$ anticommute), and in blocks $\gamma^0\gamma^1 = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}\begin{pmatrix}0&\sigma^1\\-\sigma^1&0\end{pmatrix} = \begin{pmatrix}-\sigma^1&0\\0&\sigma^1\end{pmatrix}$, so $K_1 = S^{01} = -\frac i2\operatorname{diag}(\sigma^1, -\sigma^1)$ and $-i\eta K_1 = -\frac\eta2\operatorname{diag}(\sigma^1, -\sigma^1)$.
>
> **Step 5** (exponentiate the spinor). $(\sigma^1)^2 = \mathbb 1$ gives $e^{\mp\eta\sigma^1/2} = \cosh\frac\eta2\,\mathbb 1 \mp \sinh\frac\eta2\,\sigma^1$; upper block $C - S\sigma^1 = \begin{pmatrix}C&-S\\-S&C\end{pmatrix}$, lower block $C + S\sigma^1 = \begin{pmatrix}C&S\\S&C\end{pmatrix}$. Written out, the $4\times4$ matrix above. It is not block-diagonal in the components (unlike the $z$-boost, which is diagonal), is Hermitian and not unitary.
>
> **Step 6** (direction). The rest vector goes to $(m\cosh\eta, m\sinh\eta, 0, 0)$: positive $p^1$, velocity $p^1/p^0 = \tanh\eta$ along $+x$ (active reading).
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], 2, and [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], 2, with $\hat{\mathbf n} = \hat{\mathbf x}$ ($n^1 = 1$, $n^2 = n^3 = 0$: entries $C - Sn^3 = C$, $-S(n^1 - in^2) = -S$, …); $K_1$ is in [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]]. The $z$-boost of the homework is part 1 of both theorems. Both matrices were also checked numerically, including $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ for all $\mu$.

^sol-pm-2-b

### (c) The γ's rotate as a vector

![[PHY 513 Practice Midterm#^pm-2-c]]

> [!success]- Solution
> **Answer.** Both sides equal $i(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho)$.
>
> **Step 1** (the identity). $[A, BC] = ABC - BCA = (AB + BA)C - BAC - BCA = \{A, B\}C - B\{A, C\}$.
>
> **Step 2** (drop the metric part of $S$). $[\gamma^\rho, \gamma^\sigma] = 2\gamma^\rho\gamma^\sigma - \{\gamma^\rho, \gamma^\sigma\} = 2\gamma^\rho\gamma^\sigma - 2g^{\rho\sigma}$, so $S^{\rho\sigma} = \frac i2\gamma^\rho\gamma^\sigma - \frac i2g^{\rho\sigma}\mathbb 1$; the multiple of $\mathbb 1$ commutes with $\gamma^\mu$. Hence $[\gamma^\mu, S^{\rho\sigma}] = \frac i2[\gamma^\mu, \gamma^\rho\gamma^\sigma]$.
>
> **Step 3** (Clifford). By Step 1, $[\gamma^\mu, \gamma^\rho\gamma^\sigma] = \{\gamma^\mu, \gamma^\rho\}\gamma^\sigma - \gamma^\rho\{\gamma^\mu, \gamma^\sigma\} = 2g^{\mu\rho}\gamma^\sigma - 2g^{\mu\sigma}\gamma^\rho$ (the anticommutators are numbers times $\mathbb 1$, so they may stand anywhere). So $[\gamma^\mu, S^{\rho\sigma}] = i(g^{\mu\rho}\gamma^\sigma - g^{\mu\sigma}\gamma^\rho)$.
>
> **Step 4** (right-hand side). $(\mathcal J^{\rho\sigma})^\mu{}_\nu\gamma^\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)\gamma^\nu = i(g^{\rho\mu}\gamma^\sigma - g^{\sigma\mu}\gamma^\rho)$, equal to Step 3 since $g$ is symmetric.
>
> *Checked against:* [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^thm-cb-14-17|Theorem §CB.14.17]] (the same statement and route; the user's Problem Set 4, Problem 5(b), as written, uses the same reordering identity).

^sol-pm-2-c

## Problem 3. The complex scalar field

### (a) The U(1) current

![[PHY 513 Practice Midterm#^pm-3-a]]

> [!success]- Solution
> **Answer.** $j^\mu = i\bigl(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi\bigr)$ (with $\Delta\phi = +i\phi$; Peskin–Schroeder (2.16) has the same sign), conserved on solutions for every $V$.
>
> **Step 1** (symmetry, $\mathcal J^\mu = 0$). $\phi^{\ast}\phi \to e^{-i\alpha}e^{i\alpha}\phi^{\ast}\phi$, so $m^2\phi^{\ast}\phi$ and $V(\phi^{\ast}\phi)$ are invariant; since $\alpha$ is constant, $\partial_\mu\phi \to e^{i\alpha}\partial_\mu\phi$ and the kinetic term is invariant. $\delta\mathcal L = 0$, so $\mathcal J^\mu = 0$. Generators (with $\delta\phi = \alpha\Delta\phi$ to first order): $\Delta\phi = i\phi$, $\Delta\phi^{\ast} = -i\phi^{\ast}$.
>
> **Step 2** (Noether). $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi^{\ast}$ and $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = \partial^\mu\phi$ ($\phi$, $\phi^{\ast}$ independent). Summing over both fields: $j^\mu = \partial^\mu\phi^{\ast}\,(i\phi) + \partial^\mu\phi\,(-i\phi^{\ast}) - 0 = i(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi)$.
>
> **Step 3** (field equations). $\partial\mathcal L/\partial\phi^{\ast} = -m^2\phi - V'(\phi^{\ast}\phi)\,\phi$ (chain rule, $V'$ the derivative in the argument) and $\partial_\mu\bigl(\partial\mathcal L/\partial(\partial_\mu\phi^{\ast})\bigr) = \partial^2\phi$, so $\partial^2\phi = -m^2\phi - V'\phi$; likewise $\partial^2\phi^{\ast} = -m^2\phi^{\ast} - V'\phi^{\ast}$.
>
> **Step 4** (conservation). $\partial_\mu j^\mu = i\bigl(\partial_\mu\phi\,\partial^\mu\phi^{\ast} + \phi\,\partial^2\phi^{\ast} - \partial_\mu\phi^{\ast}\partial^\mu\phi - \phi^{\ast}\partial^2\phi\bigr) = i\bigl(\phi\,\partial^2\phi^{\ast} - \phi^{\ast}\partial^2\phi\bigr)$ (the first-derivative terms cancel). Insert Step 3: $i\bigl(\phi(-m^2 - V')\phi^{\ast} - \phi^{\ast}(-m^2 - V')\phi\bigr) = 0$ for every $V$: the potential depends only on $\phi^{\ast}\phi$.
>
> **Sign.** The overall sign follows the sign of $\alpha$; with this one a positive-frequency solution has $j^0 < 0$, and the quantum charge of the course, $\hat Q = \frac12(\hat N_a - \hat N_b)$, is $-\frac12\int d^3x\,:\!\hat j^0\!:$.
>
> *Checked against:* [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]] (same current, conserved for every $m$ and $V$); [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]] (the current formula); [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]. The user's Problem Set 2, Problem 3(d), as written, gives the same current; the course solution SOL2 adds the conservation check.

^sol-pm-3-a

### (b) The momentum operator of the complex field

![[PHY 513 Practice Midterm#^pm-3-b]]

> [!success]- Solution
> **Answer.** $\hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$: particles and antiparticles of label $\mathbf p$ both carry momentum $+\mathbf p$. The reordering constant is $\propto\int d^3p\,\mathbf p = 0$, so no ordering prescription is needed.
>
> **Step 1** (the expansions at $t = 0$). From $\hat\phi(x) = \int_{\mathbf p}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x})$ and its adjoint, writing $\int_{\mathbf p} = \int\frac{d^3p}{(2\pi)^3}$ and $E = E_{\mathbf p}$:
> $\hat\pi = \partial_t\hat\phi^\dagger = \int_{\mathbf p}i\sqrt{\tfrac E2}\,(\hat a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x} - \hat b_{\mathbf p}e^{i\mathbf p\cdot\mathbf x})$, $\hat\pi^\dagger = \int_{\mathbf p}(-i)\sqrt{\tfrac E2}\,(\hat a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} - \hat b^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x})$,
> $\nabla\hat\phi = \int_{\mathbf q}\frac{i\mathbf q}{\sqrt{2E_{\mathbf q}}}(\hat a_{\mathbf q}e^{i\mathbf q\cdot\mathbf x} - \hat b^\dagger_{\mathbf q}e^{-i\mathbf q\cdot\mathbf x})$, $\nabla\hat\phi^\dagger = \int_{\mathbf q}\frac{-i\mathbf q}{\sqrt{2E_{\mathbf q}}}(\hat a^\dagger_{\mathbf q}e^{-i\mathbf q\cdot\mathbf x} - \hat b_{\mathbf q}e^{i\mathbf q\cdot\mathbf x})$.
> ($\hat{\mathbf P}$ is conserved, so $t = 0$ suffices.)
>
> **Step 2** (first term). $-\int d^3x\,\hat\pi\nabla\hat\phi$: the prefactor is $-(i)(i) = +1$, times $\sqrt{E_{\mathbf p}/4E_{\mathbf q}}\,\mathbf q$. The $\mathbf x$ integrals give $(2\pi)^3\delta^3(\mathbf q - \mathbf p)$ for $\hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}$ and $\hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}$, and $(2\pi)^3\delta^3(\mathbf q + \mathbf p)$ for $-\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}$ and $-\hat b_{\mathbf p}\hat a_{\mathbf q}$. Doing the $\mathbf q$ integral ($E_{-\mathbf p} = E_{\mathbf p}$, so the root is $\frac12$):
> $$-\int d^3x\,\hat\pi\nabla\hat\phi = \int_{\mathbf p}\tfrac12\mathbf p\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p} + \hat b_{\mathbf p}\hat a_{-\mathbf p}\bigr)$$
> (at $\mathbf q = -\mathbf p$ the factor $\mathbf q = -\mathbf p$ turns the two minus signs into plus).
>
> **Step 3** (second term). $-\int d^3x\,\hat\pi^\dagger\nabla\hat\phi^\dagger$: prefactor $-(-i)(-i) = +1$; the same steps give
> $$\int_{\mathbf p}\tfrac12\mathbf p\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + \hat a_{\mathbf p}\hat b_{-\mathbf p} + \hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p}\bigr).$$
>
> **Step 4** (the number-changing terms cancel). Relabel $\mathbf p \to -\mathbf p$ (Jacobian 1) in $\int_{\mathbf p}\mathbf p\,\hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p} = -\int_{\mathbf p}\mathbf p\,\hat b^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p} = -\int_{\mathbf p}\mathbf p\,\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}$ ($\hat a^\dagger$, $\hat b^\dagger$ commute): it cancels $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}$. Likewise $\hat a_{\mathbf p}\hat b_{-\mathbf p}$ cancels $\hat b_{\mathbf p}\hat a_{-\mathbf p}$.
>
> **Step 5** (reorder). $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$, same for $\hat b$: $\hat{\mathbf P} = \int_{\mathbf p}\mathbf p\,(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}) + (2\pi)^3\delta^3(\mathbf 0)\int_{\mathbf p}\mathbf p$. The last integral is of an odd function over a symmetric region: zero (with a box of volume $V$, $(2\pi)^3\delta^3(\mathbf 0) = V$ and any rotation-invariant cutoff). So the ordering does not matter, unlike $\hat H$, whose constant $\int E_{\mathbf p} > 0$.
>
> *Checked against:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]] ("no constant and no ordering choice"); the mode expansion [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]]; the real-field computation of Problem Set 6, Problem 1 ([[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|Example §C2a.3.1]], the user's solution, which also notes the vanishing constant).

^sol-pm-3-b

### (c) C and P on the momentum and the charge

![[PHY 513 Practice Midterm#^pm-3-c]]

> [!success]- Solution
> **Answer.** $U(\mathcal C)\hat{\mathbf P}U(\mathcal C)^{-1} = \hat{\mathbf P}$, $U(\mathcal C)\hat QU(\mathcal C)^{-1} = -\hat Q$; $U(\mathcal P)\hat{\mathbf P}U(\mathcal P)^{-1} = -\hat{\mathbf P}$, $U(\mathcal P)\hat QU(\mathcal P)^{-1} = \hat Q$.
>
> **Step 1** (creators). For unitary $U$, $U\hat a^\dagger U^{-1} = (U\hat aU^{-1})^\dagger$, since $(U\hat aU^\dagger)^\dagger = U\hat a^\dagger U^\dagger$. So $U(\mathcal C)$: $\hat a^\dagger_{\mathbf p} \to \hat b^\dagger_{\mathbf p}$, $\hat b^\dagger_{\mathbf p} \to \hat a^\dagger_{\mathbf p}$; $U(\mathcal P)$: $\hat a^\dagger_{\mathbf p} \to \hat a^\dagger_{-\mathbf p}$, $\hat b^\dagger_{\mathbf p} \to \hat b^\dagger_{-\mathbf p}$.
>
> **Step 2** (products and integrals). $U\hat A\hat BU^{-1} = (U\hat AU^{-1})(U\hat BU^{-1})$, and the linear $U$ passes through the $\int d^3p$ and the c-number $\mathbf p$.
>
> **Step 3** ($C$). $\hat a^\dagger\hat a \leftrightarrow \hat b^\dagger\hat b$ at the same $\mathbf p$: $\hat{\mathbf P} = \int_{\mathbf p}\mathbf p\,(\hat a^\dagger\hat a + \hat b^\dagger\hat b)$ is symmetric under the exchange, $\hat Q = \frac12\int_{\mathbf p}(\hat a^\dagger\hat a - \hat b^\dagger\hat b)$ antisymmetric.
>
> **Step 4** ($P$). $\hat{\mathbf P} \to \int_{\mathbf p}\mathbf p\,(\hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p} + \hat b^\dagger_{-\mathbf p}\hat b_{-\mathbf p})$; substitute $\mathbf p \to -\mathbf p$: $= \int_{\mathbf p}(-\mathbf p)(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}) = -\hat{\mathbf P}$. In $\hat Q$ there is no factor $\mathbf p$, so the same substitution gives $\hat Q$ back.
>
> **Reading.** $C$ exchanges particles and antiparticles with the same momentum, so it flips the charge and keeps the momentum; $P$ reverses momenta and keeps the charge. (With parity phases $\eta_a$, $\eta_b$ the result is the same: $|\eta|^2 = 1$ in every $\hat a^\dagger\hat a$.)
>
> *Derived here; check:* the definitions [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-1|Def. §C9.10.1]] and [[§C9.2 Parity of the Scalar Field#^def-c9-2-1|Def. §C9.2.1]] (phases $1$, as in the user's Problem Set 7, Problem 4(a)); the parity part is [[§C9.2 Parity of the Scalar Field#^thm-c9-2-12|Theorem §C9.2.12]] for $\hat Q$; the field-level statements agree: the current flips under $C$ ([[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|Theorem §C9.10.4]]), so does its charge.

^sol-pm-3-c

## Problem 4. Two-point functions and Green's functions

### (a) Commutator and Hadamard functions at spacelike separation

![[PHY 513 Practice Midterm#^pm-4-a]]

> [!success]- Solution
> **Answer.** At spacelike $x$: $D = 0$, $D_1 = 2D_W = \dfrac{m}{2\pi^2r}K_1(mr)$; for $mr \gg 1$, $D_1 \simeq \sqrt{\dfrac{m}{8\pi^3}}\;r^{-3/2}\,e^{-mr}\Bigl(1 + \dfrac{3}{8mr}\Bigr)$: the prefactor is $r^{-3/2}$, the decay length $1/m$.
>
> **Step 1** ($D$, $D_1$ from $D_W$). $\hat\phi$ is Hermitian, so $\langle0|\hat\phi(0)\hat\phi(x)|0\rangle = \langle0|\hat\phi(x)\hat\phi(0)|0\rangle^{\ast} = D_W(x)^{\ast}$ (for any operators $\langle0|\hat A\hat B|0\rangle^{\ast} = \langle0|\hat B^\dagger\hat A^\dagger|0\rangle$). Hence $iD = D_W - D_W^{\ast} = 2i\operatorname{Im}D_W$ and $D_1 = D_W + D_W^{\ast} = 2\operatorname{Re}D_W$. Only hermiticity was used, so this holds for $m > 0$.
>
> **Step 2** (reality). At spacelike $x$, $r > 0$ and $mr > 0$ are real and $K_1(mr)$ is real and positive, so $D_W$ is real: $\operatorname{Im}D_W = 0$. Therefore $D = 0$ (microcausality) and $D_1 = 2D_W = \frac{m}{2\pi^2r}K_1(mr)$, nonzero.
>
> **Step 3** (large $r$). With $K_1(z) \simeq \sqrt{\pi/2z}\,e^{-z}(1 + \frac{3}{8z})$ at $z = mr$: $D_1 \simeq \frac{m}{2\pi^2r}\sqrt{\frac{\pi}{2mr}}\,e^{-mr} = \frac{\sqrt m\,\sqrt\pi}{2\sqrt2\,\pi^2}\,r^{-3/2}e^{-mr} = \sqrt{\frac{m}{8\pi^3}}\,r^{-3/2}e^{-mr}$, using $\frac{\sqrt\pi}{2\sqrt2\,\pi^2} = \frac{1}{2\sqrt2\,\pi^{3/2}} = \frac{1}{\sqrt{8\pi^3}}$; relative corrections $O(1/mr)$. $D$ stays $0$ at every spacelike distance.
>
> **Reading.** $D$ measures influence (zero outside the cone), $D_1$ correlation (the vacuum is correlated over the Compton length $1/m$).
>
> *Checked against:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]] (part 1, $D = 2\operatorname{Im}D_W$, $D_1 = 2\operatorname{Re}D_W$), [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]] (outside the cone $D = 0$, $D_1 = mK_1(mr)/2\pi^2r$), [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]] (the asymptotic form), [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]] (the $1 + 3/8mr$ correction); and the user's Problem Set 4, Problem 3(b), as written: $D = 0$, $D_1 = \frac{m}{2\pi^2r}K_1(mr)$, $D_1 \approx \sqrt{m/8\pi^3}\,r^{-3/2}e^{-mr}$, "The overall prefactor is the power $r^{-3/2}$". Drill: [[PHY 513 PS Drill#^ps4-3-b|PS Drill, PS4.3(b)]].

^sol-pm-4-a

### (b) The massless limit and the pion's correlation length

![[PHY 513 Practice Midterm#^pm-4-b]]

> [!success]- Solution
> **Answer.** $D_W \to \frac{1}{4\pi^2r^2} = -\frac{1}{4\pi^2x^2}$; decay length $\hbar/(m_\pi c) = \hbar c/(m_\pi c^2) = 197.3/140$ fm $\approx 1.41$ fm.
>
> **Step 1** (limit). For $mr \ll 1$, $K_1(mr) \simeq 1/(mr)$, so $D_W \simeq \frac{m}{4\pi^2r}\cdot\frac{1}{mr} = \frac{1}{4\pi^2r^2}$; with $x^2 = -r^2$ this is $-\frac{1}{4\pi^2x^2}$, the massless Wightman function at spacelike $x$ (where the $i\varepsilon$ is not needed). The mass drops out: at distances well inside the Compton length every field looks massless.
>
> **Step 2** (units). In $e^{-mr}$ the exponent must be a pure number; $[m] = $ mass, $[r] = $ length, and the only length built from $m$, $\hbar$, $c$ is $\hbar/mc$. So $e^{-mr} \to e^{-mcr/\hbar}$ and the decay length is $\hbar/(mc) = \hbar c/(mc^2) = \frac{197.3\ \text{MeV fm}}{140\ \text{MeV}} = 1.41$ fm.
>
> *Checked against:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]] ("$\simeq 1/4\pi^2r^2$ for $mr \ll 1$"), [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]] (the massless function as the leading term near the cone; Problem Set 4, Problem 2(a)); the restoration of units: [[P4 Restoring ħ and c]].

^sol-pm-4-b

### (c) The advanced Green's function by contour integration

![[PHY 513 Practice Midterm#^pm-4-c]]

> [!success]- Solution
> **Answer.** $G_A(t) \equiv \int_{C_A}\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{(p^0)^2 - E^2} = \theta(-t)\,\frac{i\sin Et}{E}$, and $D_A(x) = -\theta(-x^0)\,[D_W(x) - D_W(-x)] = -\theta(-x^0)\langle0|[\hat\phi(x), \hat\phi(0)]|0\rangle$.
>
> **Step 1** (the integrand). $\frac{i\,e^{-ip^0t}}{(p^0 - E)(p^0 + E)}$, $t = x^0$, $E = E_{\mathbf p}$: simple poles at $p^0 = \pm E$, with residues $\frac{i}{2\pi}\frac{e^{-iEt}}{2E}$ at $+E$ and $\frac{i}{2\pi}\frac{e^{iEt}}{-2E}$ at $-E$ (including the $\frac{1}{2\pi}$).
>
> **Step 2** (which half-plane). $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$. For $t > 0$ it is bounded by $1$ in the lower half-plane, for $t < 0$ in the upper. On a semicircle of radius $R > E$ the rest of the integrand is at most $\frac{1}{2\pi}\frac{1}{R^2 - E^2}$, so the arc contributes at most $\frac{\pi R}{2\pi(R^2 - E^2)} \to 0$ (ML bound; the $1/R^2$ decay makes Jordan's lemma unnecessary).
>
> **Step 3** ($t > 0$). Close downward. $C_A$ runs below both poles, so the closed contour (the real line plus the lower arc) encloses neither: $G_A = 0$ by Cauchy's theorem. $D_A$ vanishes for $x^0 > 0$.
>
> **Step 4** ($t < 0$). Close upward: the loop runs counterclockwise and encloses both poles, $G_A = 2\pi i\sum\operatorname{Res} = 2\pi i\cdot\frac{i}{2\pi}\cdot\frac{e^{-iEt} - e^{iEt}}{2E} = -\frac{e^{-iEt} - e^{iEt}}{2E} = \frac{i\sin Et}{E}$.
>
> **Step 5** (recognize $D_W$). For $t < 0$, $D_A = -\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\bigl[e^{-iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x} - e^{iE_{\mathbf p}t + i\mathbf p\cdot\mathbf x}\bigr]$. The first exponent is $-ip\cdot x$ ($p^0 = E_{\mathbf p}$): this term is $D_W(x)$. In the second substitute $\mathbf p \to -\mathbf p$: $e^{iEt - i\mathbf p\cdot\mathbf x} = e^{ip\cdot x} = e^{-ip\cdot(-x)}$, so it is $D_W(-x)$. Hence $D_A = -\theta(-x^0)[D_W(x) - D_W(-x)]$, and $D_W(x) - D_W(-x) = \langle0|\hat\phi(x)\hat\phi(0)|0\rangle - \langle0|\hat\phi(0)\hat\phi(x)|0\rangle = \langle0|[\hat\phi(x), \hat\phi(0)]|0\rangle = iD(x)$ (translation invariance for the second term).
>
> **Reading.** The time mirror of Peskin–Schroeder's retarded computation (2.54)–(2.55): $D_A(x) = D_R(-x)$, supported in the backward cone; it is again a Green's function, $(\partial^2 + m^2)D_A = -i\delta^4$, as every contour is.
>
> *Checked against:* [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]] and its derivation (same contour, same residues, mode by mode $\theta(-t)\,i\sin(E_{\mathbf p}t)/E_{\mathbf p}$); the retarded case [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]]; the procedure [[P2 Green's Functions by Contour Integration]].

^sol-pm-4-c

## Problem 5. Dirac algebra and spinors

### (a) The four-slash contraction

![[PHY 513 Practice Midterm#^pm-5-a]]

> [!success]- Solution
> **Answer.** $\gamma_\mu\slashed k\slashed p\slashed q\gamma^\mu = -2\slashed q\slashed p\slashed k$.
>
> **Step 1** (slash identities from Clifford). $\slashed a\slashed b + \slashed b\slashed a = a_\mu b_\nu\{\gamma^\mu, \gamma^\nu\} = 2a\cdot b$, and $\slashed q\gamma^\mu = q_\nu\gamma^\nu\gamma^\mu = 2q^\mu - \gamma^\mu\slashed q$.
>
> **Step 2** (move $\gamma^\mu$ left past $\slashed q$). $\gamma_\mu\slashed k\slashed p\slashed q\gamma^\mu = \gamma_\mu\slashed k\slashed p(2q^\mu - \gamma^\mu\slashed q) = 2\slashed q\,\slashed k\slashed p - (\gamma_\mu\slashed k\slashed p\gamma^\mu)\slashed q$, using $\gamma_\mu q^\mu = \slashed q$ in the first term.
>
> **Step 3** (the known contraction). $\gamma_\mu\slashed k\slashed p\gamma^\mu = 4\,k\cdot p$, so the second term is $-4(k\cdot p)\slashed q$.
>
> **Step 4** (reverse $\slashed k\slashed p$). $\slashed k\slashed p = 2k\cdot p - \slashed p\slashed k$, so $2\slashed q\slashed k\slashed p = 4(k\cdot p)\slashed q - 2\slashed q\slashed p\slashed k$. Total: $4(k\cdot p)\slashed q - 2\slashed q\slashed p\slashed k - 4(k\cdot p)\slashed q = -2\slashed q\slashed p\slashed k$.
>
> **Check.** $k = p = q$: left $\gamma_\mu\slashed k\slashed k\slashed k\gamma^\mu = k^2\gamma_\mu\slashed k\gamma^\mu = -2k^2\slashed k$; right $-2\slashed k^3 = -2k^2\slashed k$.
>
> *Checked against:* [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]] (fourth identity; its derivation moves $\gamma^\mu$ through one slash at a time, and keeps the user's Problem Set 5, Problem 2 as the second route); [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]] (slash algebra).

^sol-pm-5-a

### (b) The Gordon identity for v spinors

![[PHY 513 Practice Midterm#^pm-5-b]]

> [!success]- Solution
> **Answer.** $\bar v(p')\gamma^\mu v(p) = -\dfrac{1}{2m}\bar v(p')\bigl[(p + p')^\mu + i\sigma^{\mu\nu}q_\nu\bigr]v(p)$: the $u$-spinor identity with $m \to -m$. Forward: $\bar v^r(p)\gamma^\mu v^s(p) = 2p^\mu\delta^{rs}$.
>
> **Step 1** (the equation for $\bar v(p')$). Take the adjoint of $(p'_\mu\gamma^\mu + m)v(p') = 0$ ($p'$ real): $v^\dagger(p')(p'_\mu\gamma^{\mu\dagger} + m) = 0$. Multiply on the right by $\gamma^0$ and insert $\gamma^0\gamma^0 = \mathbb 1$ on the left of the bracket: $v^\dagger(p')\gamma^0\bigl(p'_\mu\gamma^0\gamma^{\mu\dagger}\gamma^0 + m\bigr) = 0$, and $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$. So $\bar v(p')(\slashed p' + m) = 0$, i.e. $\bar v(p')\slashed p' = -m\,\bar v(p')$; and $\slashed p\,v(p) = -m\,v(p)$.
>
> **Step 2** (split $\gamma^\mu$ in half). Using $v(p) = -\frac{\slashed p}{m}v(p)$ on the right and $\bar v(p') = -\bar v(p')\frac{\slashed p'}{m}$ on the left, once each:
> $$\bar v(p')\gamma^\mu v(p) = \tfrac12\bar v(p')\gamma^\mu\Bigl(-\tfrac{\slashed p}{m}\Bigr)v(p) + \tfrac12\bar v(p')\Bigl(-\tfrac{\slashed p'}{m}\Bigr)\gamma^\mu v(p) = -\frac{1}{2m}\bar v(p')\bigl(\gamma^\mu\slashed p + \slashed p'\gamma^\mu\bigr)v(p).$$
>
> **Step 3** (symmetric and antisymmetric parts). $\gamma^\mu\gamma^\nu = \frac12\{\gamma^\mu, \gamma^\nu\} + \frac12[\gamma^\mu, \gamma^\nu] = g^{\mu\nu} - i\sigma^{\mu\nu}$ (since $[\gamma^\mu, \gamma^\nu] = -2i\sigma^{\mu\nu}$). Contract: $\gamma^\mu\slashed p = p^\mu - i\sigma^{\mu\nu}p_\nu$, and $\slashed p'\gamma^\mu = p'_\nu(g^{\nu\mu} - i\sigma^{\nu\mu}) = p'^\mu + i\sigma^{\mu\nu}p'_\nu$ ($\sigma$ antisymmetric). Sum: $(p + p')^\mu + i\sigma^{\mu\nu}(p' - p)_\nu$. Insert in Step 2.
>
> **Step 4** (forward limit). $p' = p$, $q = 0$, spins $r$, $s$: $\bar v^r(p)\gamma^\mu v^s(p) = -\frac{2p^\mu}{2m}\bar v^r(p)v^s(p) = -\frac{p^\mu}{m}(-2m\delta^{rs}) = 2p^\mu\delta^{rs}$. At $\mu = 0$: $\bar v\gamma^0v = v^\dagger\gamma^0\gamma^0v = v^\dagger v = 2E_{\mathbf p}\delta^{rs}$, consistent.
>
> *Derived here; check:* the $u$-spinor route [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]] (its derivation, step for step, with $\slashed pu = mu$ replaced by $\slashed pv = -mv$, i.e. $m \to -m$); the conjugate equation $\bar v\slashed p = -m\bar v$ is [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-12|Theorem §C5a.9.12]], 2; the normalizations [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|Theorem §C5a.10.4]]. The identity was also checked numerically (explicit chiral-basis $v(p)$, $v(p')$ for random momenta, all four $\mu$).

^sol-pm-5-b

## Problem 6. Discrete symmetries of the bilinears

### (a) The axial vector under time reversal

![[PHY 513 Practice Midterm#^pm-6-a]]

> [!success]- Solution
> **Answer.** $U(\mathcal T)\mathsf A^\mu(x)U(\mathcal T)^{-1} = \mathcal P^\mu{}_\nu\mathsf A^\nu(x_T)$: $\mathsf A^0$ even, $\mathsf A^i$ odd, exactly like $\mathsf V^\mu$.
>
> **Step 1** (antiunitarity, no exchange). In components $\mathsf A^\mu = \sum_{a,b}\hat{\bar\psi}_a\Gamma_{ab}\hat\psi_b$ with $\Gamma = \gamma^\mu\gamma^5$. $U = U(\mathcal T)$ conjugates the numbers $\Gamma_{ab}$ and keeps the order of the operators; inserting $U^{-1}U = \mathbb 1$ between the fields,
> $U\mathsf A^\mu U^{-1} = \sum_{a,b}(U\hat{\bar\psi}_aU^{-1})\,\Gamma^{\ast}_{ab}\,(U\hat\psi_bU^{-1}) = \hat{\bar\psi}(x_T)\,\gamma^3\gamma^1\,\Gamma^{\ast}\,\gamma^1\gamma^3\,\hat\psi(x_T)$. No fermion exchange: $\hat{\bar\psi}$ stays on the left.
>
> **Step 2** (conjugate). $\Gamma^{\ast} = (\gamma^\mu)^{\ast}(\gamma^5)^{\ast} = (\gamma^\mu)^{\ast}\gamma^5$: $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ is real in the chiral basis.
>
> **Step 3** (split the sandwich). Insert $\mathbb 1 = \gamma^1\gamma^3\gamma^3\gamma^1$ ($\gamma^1\gamma^3\gamma^3\gamma^1 = \gamma^1(\gamma^3)^2\gamma^1 = -(\gamma^1)^2 = \mathbb 1$) between $(\gamma^\mu)^{\ast}$ and $\gamma^5$:
> $\gamma^3\gamma^1(\gamma^\mu)^{\ast}\gamma^5\gamma^1\gamma^3 = \bigl(\gamma^3\gamma^1(\gamma^\mu)^{\ast}\gamma^1\gamma^3\bigr)\bigl(\gamma^3\gamma^1\gamma^5\gamma^1\gamma^3\bigr)$.
>
> **Step 4** (the two factors). First: $(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$ (lower index; check: $\gamma^0$ real and commutes with $\gamma^1\gamma^3$; $\gamma^1$, $\gamma^3$ real and anticommute with it; $\gamma^2$ imaginary, $(\gamma^2)^{\ast} = -\gamma^2$, and commutes with it), so it is $\gamma^3\gamma^1\gamma^1\gamma^3\gamma_\mu = \gamma_\mu$. Second: $\gamma^5$ anticommutes with $\gamma^1$ and $\gamma^3$, so it commutes with $\gamma^1\gamma^3$: $\gamma^3\gamma^1\gamma^5\gamma^1\gamma^3 = \gamma^5\gamma^3\gamma^1\gamma^1\gamma^3 = \gamma^5$.
>
> **Step 5** (assemble). $U\mathsf A^\mu(x)U^{-1} = \hat{\bar\psi}(x_T)\gamma_\mu\gamma^5\hat\psi(x_T)$, and componentwise $\gamma_\mu = \mathcal P^\mu{}_\nu\gamma^\nu$: $= \mathcal P^\mu{}_\nu\mathsf A^\nu(x_T)$. Normal ordering is preserved ($U$ maps annihilators to annihilators).
>
> **Reading.** Under $T$ the extra $\gamma^5$ adds nothing (real, and commutes with $\gamma^1\gamma^3$); under $P$ it adds a sign, under $C$ it removes one. Peskin–Schroeder's table, row $T$, column $\bar\psi\gamma^\mu\gamma^5\psi$: $(-1)^\mu$, the same.
>
> *Checked against:* [[§C9.8 Time Reversal#^thm-c9-8-13|Theorem §C9.8.13]] and its derivation (the same insertion of $\gamma^1\gamma^3\gamma^3\gamma^1$); the rule [[§C9.8 Time Reversal#^thm-c9-8-10|Theorem §C9.8.10]]; the identity $(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$ is [[§C9.8 Time Reversal#^thm-c9-8-4|Theorem §C9.8.4]], 4; the user's Problem Set 7, Problem 2(c) (as written, for $\mathsf V^\mu$: $\gamma^1\gamma^3$ commutes with $\gamma^0$, $\gamma^2$ and anticommutes with $\gamma^1$, $\gamma^3$, giving $(-1)^\mu$).

^sol-pm-6-a

### (b) The tensor under charge conjugation

![[PHY 513 Practice Midterm#^pm-6-b]]

> [!success]- Solution
> **Answer.** $U(\mathcal C)\mathsf T^{\mu\nu}(x)U(\mathcal C)^{-1} = -\mathsf T^{\mu\nu}(x)$.
>
> **Step 1** (the transpose identity). In the chiral basis $\gamma^0$, $\gamma^2$ are symmetric and $\gamma^1$, $\gamma^3$ antisymmetric; $\gamma^0\gamma^2$ anticommutes with $\gamma^0$ and $\gamma^2$ and commutes with $\gamma^1$ and $\gamma^3$ (each of these anticommutes with both factors). Hence for every $\mu$: $(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$ (e.g. $\mu = 1$: $(\gamma^1)^{\mathsf T}\gamma^0\gamma^2 = -\gamma^1\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^1$). With $(\gamma^0\gamma^2)^2 = -(\gamma^0)^2(\gamma^2)^2 = \mathbb 1$: $\gamma^0\gamma^2(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = -(\gamma^0\gamma^2)^2\gamma^\mu = -\gamma^\mu$.
>
> **Step 2** (transpose $\sigma^{\mu\nu}$). $(\sigma^{\mu\nu})^{\mathsf T} = \frac i2\bigl((\gamma^\nu)^{\mathsf T}(\gamma^\mu)^{\mathsf T} - (\gamma^\mu)^{\mathsf T}(\gamma^\nu)^{\mathsf T}\bigr)$: the transpose reverses each product, $i$ is a number.
>
> **Step 3** (sandwich each product). Insert $(\gamma^0\gamma^2)^2 = \mathbb 1$ between the two factors: $\gamma^0\gamma^2(\gamma^\nu)^{\mathsf T}(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = \bigl(\gamma^0\gamma^2(\gamma^\nu)^{\mathsf T}\gamma^0\gamma^2\bigr)\bigl(\gamma^0\gamma^2(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2\bigr) = (-\gamma^\nu)(-\gamma^\mu) = \gamma^\nu\gamma^\mu$; likewise the other product gives $\gamma^\mu\gamma^\nu$.
>
> **Step 4** (the commutator reverses). $\gamma^0\gamma^2(\sigma^{\mu\nu})^{\mathsf T}\gamma^0\gamma^2 = \frac i2(\gamma^\nu\gamma^\mu - \gamma^\mu\gamma^\nu) = -\sigma^{\mu\nu}$. By the given rule, $\mathsf T^{\mu\nu} \to \hat{\bar\psi}(-\sigma^{\mu\nu})\hat\psi = -\mathsf T^{\mu\nu}$, at the same point $x$.
>
> **Where the rule's signs are.** The rule already contains $(-i)^2 = -1$ from the two field laws and $-1$ from exchanging the fermion fields inside the normal-ordered product; they cancel. Each $\gamma$ then contributes a sign and the transpose reverses the order: an antisymmetric product of two $\gamma$'s flips.
>
> *Checked against:* [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-10|Theorem §C9.6.10]] and its derivation (the same three steps); the rule [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|Theorem §C9.6.7]], 1; the transposes [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-4|Theorem §C9.5.4]], 1, 4, 5; Peskin–Schroeder's table (p. 71), row $C$, column $\bar\psi\sigma^{\mu\nu}\psi$: $-1$.

^sol-pm-6-b

### (c) The tensor under CPT

![[PHY 513 Practice Midterm#^pm-6-c]]

> [!success]- Solution
> **Answer.** $\Theta\,\mathsf T^{\mu\nu}(x)\,\Theta^{-1} = +\mathsf T^{\mu\nu}(-x)$: two Lorentz indices, sign $(-1)^2 = +1$.
>
> **Step 1** ($T$ first). $\Theta\hat O\Theta^{-1} = U(\mathcal C)U(\mathcal P)\bigl[U(\mathcal T)\hat OU(\mathcal T)^{-1}\bigr]U(\mathcal P)^{-1}U(\mathcal C)^{-1}$, and $U(\mathcal T)\mathsf T^{\mu\nu}(x)U(\mathcal T)^{-1} = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$.
>
> **Step 2** ($P$ at the point $x_T$). The real numbers $-\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma$ pass through the linear $U(\mathcal P)$; $U(\mathcal P)\mathsf T^{\rho\sigma}(x_T)U(\mathcal P)^{-1} = \mathcal P^\rho{}_\alpha\mathcal P^\sigma{}_\beta\mathsf T^{\alpha\beta}(\widetilde{x_T})$ with $\widetilde{x_T} = (-t, -\mathbf x) = -x$. Since $\mathcal P^\mu{}_\rho\mathcal P^\rho{}_\alpha = \delta^\mu{}_\alpha$: $-\mathsf T^{\mu\nu}(-x)$.
>
> **Step 3** ($C$ at $-x$). By (b), $U(\mathcal C)\mathsf T^{\mu\nu}(-x)U(\mathcal C)^{-1} = -\mathsf T^{\mu\nu}(-x)$, so the total is $-(-\mathsf T^{\mu\nu}(-x)) = +\mathsf T^{\mu\nu}(-x)$.
>
> **Rule.** Under $\Theta$ a bilinear with $n$ Lorentz indices is multiplied by $(-1)^n$ and moved to $-x$; $n = 2$ gives $+1$, as found.
>
> *Checked against:* [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]] (row $\mathsf T^{\mu\nu}$, column $CPT$: $+\mathsf T^{\mu\nu}$ at $-x$); the same three-step composition for $\mathsf A^\mu$ is [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|Example §C9.9.1]]; the two given laws are [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]], row 5, and [[§C9.8 Time Reversal#^thm-c9-8-14|Theorem §C9.8.14]].

^sol-pm-6-c

---

# Part II. The extended set

The solutions below are numbered as the items of [[PHY 513 Practice Midterm 2 (Extended Set)]].

<!-- PART-II -->
