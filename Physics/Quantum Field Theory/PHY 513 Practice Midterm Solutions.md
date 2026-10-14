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
> **Step 2** (units). In $e^{-mr}$ the exponent must be a pure number; $m$ is a mass and $r$ a length, and the only length built from $m$, $\hbar$, $c$ is $\hbar/mc$. So $e^{-mr} \to e^{-mcr/\hbar}$ and the decay length is $\hbar/(mc) = \hbar c/(mc^2) = \frac{197.3\ \text{MeV fm}}{140\ \text{MeV}} = 1.41$ fm.
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

## A. Relativity, index calculus, invariants

### X1.1.1 · Legal or illegal, and which are pseudoscalars
*[variation of PS1.1]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-1-1]]

> [!success]- Solution
> **Answer.** (a) legal, a Lorentz scalar that is a **pseudoscalar** ($=-8\,\mathbf E\cdot\mathbf B$); (b) illegal; (c) legal, a true scalar; (d) legal, a vector equation; (e) illegal; (f) legal, an equation between true scalars. Only (a) is a pseudoscalar.
>
> **Step 1** (the rules). In one term an index occurs at most twice, and then once up and once down (summed); an index occurring once is free, and both sides of an equation carry the same free indices at the same heights ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]]). A full contraction containing one $\varepsilon$ picks up $\det\Lambda$: $\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Lambda^\rho{}_\gamma\Lambda^\sigma{}_\delta\,\varepsilon^{\alpha\beta\gamma\delta} = (\det\Lambda)\,\varepsilon^{\mu\nu\rho\sigma}$ ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]]), so it is invariant under $\det\Lambda = +1$ and odd under $\mathcal P$: a pseudoscalar.
>
> **Step 2** ((a)). $\mu, \nu, \rho, \sigma$ each occur once up (on $\varepsilon$) and once down (on an $F$): no free index, a scalar under $SO^+(1,3)$. It contains one $\varepsilon$, so by Step 1 it is a pseudoscalar. Check with components: $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]), and $\mathbf E\cdot\mathbf B$ is odd under parity ($\mathbf E$ polar, $\mathbf B$ axial). With Peskin–Schroeder's $\varepsilon^{0123} = -1$ the value is $+8\,\mathbf E\cdot\mathbf B$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]]).
>
> **Step 3** ((b)). Left side: $\mu$ up on $F$, down on $\partial$, contracted; $\nu$ free and **up**. Right side: $\nu$ free and **down**. The heights differ: illegal. Repaired: $\partial_\mu F^{\mu\nu} = j^\nu$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]]), or equivalently $\partial^\mu F_{\mu\nu} = j_\nu$.
>
> **Step 4** ((c)). $\mu$: up on $x^\mu$, down on $x_\mu$; $\nu$: down on $\partial_\nu$, up on $x^\nu$. Both contracted, nothing free: legal, a scalar, with no $\varepsilon$, so a true scalar. With the parentheses $\partial_\nu$ acts on $x^\nu$ alone, $\partial_\nu x^\nu = 4$, and the expression is $4x^2$ (without them, acting on everything to its right, $x^\mu\partial_\nu(x^\nu x_\mu) = x^\mu(4x_\mu + x^\nu g_{\nu\mu}) = 5x^2$; [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]]). A scalar either way.
>
> **Step 5** ((d)). $T^{\mu\nu}{}_\nu$: $\nu$ once up, once down, contracted (a trace over the second and third slots); $\mu$ free, up. Right side: $\mu$ free, up. Legal: an equation between two (contravariant) vectors.
>
> **Step 6** ((e)). $\mu$ occurs three times (down, up, down): illegal; the sum $\sum_\mu a_\mu b^\mu c_\mu$ is not a component of any tensor. A legal neighbour is $(a_\nu b^\nu)c_\mu$, a covector.
>
> **Step 7** ((f)). The spinor indices are summed as a row times a matrix times a column, $\bar\psi_a(\gamma^\mu)_{ab}\partial_\mu\psi_b$; they are never moved with $g$ and play no role in the Lorentz bookkeeping ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-2|§C5b.2, Caution: u is not a four-vector]]). The spacetime index $\mu$ is up on $\gamma^\mu$ and down on $\partial_\mu$: contracted. Neither side has a free index: legal, an equation between Lorentz scalars. Under parity $\bar\psi\psi$ is even and $\bar\psi\gamma^\mu\psi$ is a true vector ([[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]]), and $\partial_\mu$ flips with the same $\mathcal P^\mu{}_\nu$, so both sides are true scalars, not pseudoscalars. Read as $\bar\psi$ times the Dirac equation.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]] (the rules, with the course solution SOL1, Problem 1), [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]] (the value of (a)) and [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]] (pseudotensor law).

^sol-px-1-1-1

### X1.2.1 · The defining condition in index form, and the inverse
*[variation of PS1.2(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-2-1]]

> [!success]- Solution
> **Answer.** $g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta}$, and then $\Lambda_\mu{}^\rho\,\Lambda^\mu{}_\sigma = \delta^\rho{}_\sigma$, so $(\Lambda^{-1})^\rho{}_\mu = \Lambda_\mu{}^\rho$; as matrices $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$.
>
> **Step 1** (index form). Matrix products join the second index of one factor to the first of the next, and the transpose exchanges the slots, $(\Lambda^{\mathsf T})_\alpha{}^\mu = \Lambda^\mu{}_\alpha$. So $(\Lambda^{\mathsf T}g\Lambda)_{\alpha\beta} = \Lambda^\mu{}_\alpha\,g_{\mu\nu}\,\Lambda^\nu{}_\beta$, and $\Lambda^{\mathsf T}g\Lambda = g$ reads
> $$
> g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta} \qquad (\ast)
> $$
> (sixteen equations, ten independent because both sides are symmetric in $\alpha\beta$).
>
> **Step 2** (the candidate). Define $\Lambda_\mu{}^\rho \equiv g_{\mu\alpha}g^{\rho\beta}\Lambda^\alpha{}_\beta$, read as a matrix with row index $\rho$ and column index $\mu$. Multiply it into $\Lambda$, contracting $\mu$:
> $$
> \Lambda_\mu{}^\rho\,\Lambda^\mu{}_\sigma = g^{\rho\beta}\bigl(g_{\mu\alpha}\Lambda^\alpha{}_\beta\Lambda^\mu{}_\sigma\bigr) = g^{\rho\beta}g_{\beta\sigma} = \delta^\rho{}_\sigma ,
> $$
> where the bracket is $(\ast)$ with the free indices $(\beta, \sigma)$ (and $g_{\mu\alpha} = g_{\alpha\mu}$), and the last step is $g^{\rho\beta}g_{\beta\sigma} = \delta^\rho{}_\sigma$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-2|Theorem §C1a.5.2]]).
>
> **Step 3** (left inverse is the inverse). Step 2 says the matrix $L^\rho{}_\mu = \Lambda_\mu{}^\rho$ satisfies $L\Lambda = \mathbb 1$; for square matrices a left inverse is the two-sided inverse. Hence $(\Lambda^{-1})^\rho{}_\mu = \Lambda_\mu{}^\rho$: the inverse is the transpose with both indices moved by the metric, $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$.
>
> **Step 4** (check on a boost). For a boost along $x^1$ with $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\eta$: $(\Lambda^{-1})^0{}_1 = \Lambda_1{}^0 = g_{11}g^{00}\Lambda^1{}_0 = -\sinh\eta$, the boost with rapidity $-\eta$, as it must be; the diagonal entries are unchanged ($g_{00}g^{00} = g_{11}g^{11} = 1$).
>
> *Checked against:* [[§C1a.4 The Lorentz Group#^def-c1a-4-1|Def. §C1a.4.1]] (the component form) and [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 2 (the same inverse, $(\Lambda^{-1})^\mu{}_\nu = \Lambda_\nu{}^\mu$).

^sol-px-1-2-1

### X1.2.2 · Symmetric times antisymmetric
*[variation of PS1.2(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-2-2]]

> [!success]- Solution
> **Answer.** $S^{\mu\nu}A_{\mu\nu} = 0$; $F^{\mu\nu}F_{\nu\mu} = -F_{\mu\nu}F^{\mu\nu}$; $F^\mu{}_\mu = 0$.
>
> **Step 1** (rename, then use the symmetries). Rename the dummies $\mu \leftrightarrow \nu$ (allowed: they are summed): $X \equiv S^{\mu\nu}A_{\mu\nu} = S^{\nu\mu}A_{\nu\mu}$. Now $S^{\nu\mu} = S^{\mu\nu}$ and $A_{\nu\mu} = -A_{\mu\nu}$, so $X = -S^{\mu\nu}A_{\mu\nu} = -X$, hence $X = 0$.
>
> **Step 2** ($F^{\mu\nu}F_{\nu\mu}$). $F$ is antisymmetric, $F_{\nu\mu} = -F_{\mu\nu}$, so $F^{\mu\nu}F_{\nu\mu} = -F^{\mu\nu}F_{\mu\nu} = -F_{\mu\nu}F^{\mu\nu}$ (a contracted pair may be seesawed). As matrices this is $\operatorname{tr}(FF)$ with one index pair crossed: the transpose costs the sign.
>
> **Step 3** ($F^\mu{}_\mu$). $F^\mu{}_\mu = g_{\mu\nu}F^{\mu\nu}$: the symmetric $g_{\mu\nu}$ contracted with the antisymmetric $F^{\mu\nu}$, zero by Step 1. It is a pure number, $0$, and does not involve $F_{\mu\nu}F^{\mu\nu}$ at all.
>
> **Step 4** (component check). $F_{\mu\nu}F^{\mu\nu} = 2(\mathbf B^2 - \mathbf E^2)$ ([[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]), so $F^{\mu\nu}F_{\nu\mu} = 2(\mathbf E^2 - \mathbf B^2)$; and $F^\mu{}_\mu = F^0{}_0 + F^i{}_i = 0$ because the diagonal of $F^{\mu\nu}$ vanishes and lowering one index multiplies each diagonal entry by $\pm1$.
>
> *Checked against:* [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2 (symmetric times antisymmetric is zero) and [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]], derivation step 2 ($g_{\mu\nu}T^{[\mu\nu]} = 0$).

^sol-px-1-2-2

### X1.3.1 · Four values of ε, in both conventions
*[variation of PS1.3(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-3-1]]

> [!success]- Solution
> **Answer.** Course ($\varepsilon^{0123} = +1$): $\varepsilon^{3012} = -1$, $\varepsilon^{2301} = +1$, $\varepsilon_{0123} = -1$, $\varepsilon_{1032} = -1$. Peskin–Schroeder ($\varepsilon^{0123} = -1$): $+1$, $-1$, $+1$, $+1$, every one reversed.
>
> **Step 1** ($\varepsilon^{3012}$). $(0123) \to (3012)$ moves $3$ to the front past three indices: three transpositions, odd. $\varepsilon^{3012} = (-1)^3\varepsilon^{0123} = -1$.
>
> **Step 2** ($\varepsilon^{2301}$). $(0123) \to (2301)$ exchanges $0 \leftrightarrow 2$ and $1 \leftrightarrow 3$: two transpositions, even. $\varepsilon^{2301} = +1$.
>
> **Step 3** ($\varepsilon_{0123}$). Lowering all four indices multiplies by $g_{00}g_{11}g_{22}g_{33} = (+1)(-1)^3 = -1 = \det g$: $\varepsilon_{0123} = -\varepsilon^{0123} = -1$; in general $\varepsilon_{\mu\nu\rho\sigma} = -\varepsilon^{\mu\nu\rho\sigma}$ as numbers.
>
> **Step 4** ($\varepsilon_{1032}$). $(0123) \to (1032)$ exchanges $0 \leftrightarrow 1$ and $2 \leftrightarrow 3$: even, so $\varepsilon^{1032} = +1$, and by Step 3 $\varepsilon_{1032} = -1$.
>
> **Step 5** (Peskin–Schroeder). Every value is $\pm\varepsilon^{0123}$ with a sign fixed by the permutation and by $\det g$, so all four reverse: $\varepsilon^{3012} = +1$, $\varepsilon^{2301} = -1$, $\varepsilon_{0123} = +1$, $\varepsilon_{1032} = +1$. Any quantity with one $\varepsilon$ flips between the conventions; products of two $\varepsilon$'s do not.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]], [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]], 2 ($\varepsilon_{\mu\nu\rho\sigma} = -\varepsilon^{\mu\nu\rho\sigma}$), and [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|Example §C1a.5.2]] ($\varepsilon_{2301} = \varepsilon_{0123} = -1$, two transpositions).

^sol-px-1-3-1

### X1.3.2 · Three conserved momenta and one ε
*[variation of PS1.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-3-2]]

> [!success]- Solution
> **Answer.** $\varepsilon^{\mu\nu\rho\sigma}p_{1\nu}p_{2\rho}p_{3\sigma} = 0$ for every $\mu$; and yes, $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}k_\sigma = 0$ for every $k$.
>
> **Step 1** (lower indices). $p_1^\mu + p_2^\mu + p_3^\mu = 0$; multiplying by $g_{\mu\alpha}$ gives $p_{1\alpha} + p_{2\alpha} + p_{3\alpha} = 0$, so $p_{3\sigma} = -(p_{1\sigma} + p_{2\sigma})$.
>
> **Step 2** (substitute).
> $$
> \varepsilon^{\mu\nu\rho\sigma}p_{1\nu}p_{2\rho}p_{3\sigma} = -\varepsilon^{\mu\nu\rho\sigma}p_{1\nu}p_{2\rho}p_{1\sigma} - \varepsilon^{\mu\nu\rho\sigma}p_{1\nu}p_{2\rho}p_{2\sigma} .
> $$
>
> **Step 3** (symmetric against antisymmetric). In the first term $p_{1\nu}p_{1\sigma}$ is symmetric in $\nu\sigma$ and $\varepsilon^{\mu\nu\rho\sigma}$ antisymmetric in $\nu\sigma$: rename $\nu \leftrightarrow \sigma$ and the term equals minus itself, so it is zero ([[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]], 2). The second term vanishes the same way in the pair $\rho\sigma$. This holds for each value of the free index $\mu$.
>
> **Step 4** (the full contraction with $k$). Move $\sigma$ to the front: $(\mu\nu\rho\sigma) \to (\sigma\mu\nu\rho)$ is three transpositions, so $\varepsilon^{\mu\nu\rho\sigma} = -\varepsilon^{\sigma\mu\nu\rho}$ and
> $$
> \varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}k_\sigma = -k_\sigma\bigl(\varepsilon^{\sigma\mu\nu\rho}p_{1\mu}p_{2\nu}p_{3\rho}\bigr) = -k_\sigma\cdot0 = 0
> $$
> by Steps 2–3 (with the free index called $\sigma$). Determinant reading: the contraction is $-\det[p_1|p_2|p_3|k]$ with lowered components, and the first three columns are linearly dependent ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 4), whatever $k$ is. A nonzero $\varepsilon$-contraction needs four linearly independent vectors.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]] (the four-momentum version, by the determinant route) and the course solution SOL1, Problem 3(b) (the symmetric–antisymmetric route used here).

^sol-px-1-3-2

### X1.3.3 · The ε-contraction of four momenta is a pseudoscalar
*[extension of PS1.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-3-3]]

> [!success]- Solution
> **Answer.** $I \to (\det\mathcal P)\,I = -I$, by $\varepsilon_{\mu\nu\rho\sigma}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$ with $A = \mathcal P$, $\det\mathcal P = -1$.
>
> **Step 1** ($\mathcal P$ is a Lorentz transformation). $\mathcal P^\mu{}_\nu = \operatorname{diag}(1, -1, -1, -1)$ is diagonal with entries $\pm1$, so $(\mathcal P^{\mathsf T}g\mathcal P)_{\alpha\beta} = \mathcal P^\alpha{}_\alpha\,g_{\alpha\beta}\,\mathcal P^\beta{}_\beta$ (no sum) $= g_{\alpha\beta}$, since $g$ is diagonal and $(\pm1)^2 = 1$. Every contraction $p_i\cdot p_j$ is therefore unchanged. But $\det\mathcal P = 1\cdot(-1)^3 = -1$.
>
> **Step 2** (all indices of $\varepsilon$ down). Seesaw each contracted pair: $I = \varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = \varepsilon_{\mu\nu\rho\sigma}p_1^\mu p_2^\nu p_3^\rho p_4^\sigma$.
>
> **Step 3** (transform). With $p_i^\mu \to \mathcal P^\mu{}_\alpha p_i^\alpha$,
> $$
> I' = \varepsilon_{\mu\nu\rho\sigma}\mathcal P^\mu{}_\alpha\mathcal P^\nu{}_\beta\mathcal P^\rho{}_\gamma\mathcal P^\sigma{}_\delta\;p_1^\alpha p_2^\beta p_3^\gamma p_4^\delta = (\det\mathcal P)\,\varepsilon_{\alpha\beta\gamma\delta}\,p_1^\alpha p_2^\beta p_3^\gamma p_4^\delta = -I .
> $$
> The identity used is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 1, which holds for every $4\times4$ matrix; for $\det\Lambda = +1$ it gives invariance, for $\mathcal P$ (and $\mathcal T$) a sign. $\Lambda^{\mathsf T}g\Lambda = g$ only gives $(\det\Lambda)^2 = 1$, and the remaining sign is exactly what $\varepsilon$ detects.
>
> **Step 4** (explicit check). By Theorem §C1a.5.4, 4, $I = -\det[p_1|p_2|p_3|p_4]$ (upper components as columns). $\mathcal P$ multiplies rows $1, 2, 3$ of that matrix by $-1$, so the determinant gets $(-1)^3$. Numerically, with $p_i^\mu = \delta^\mu_{i-1}$ (the four unit vectors): $I = \varepsilon_{0123} = -1$ before and $(-1)^3(-1) = +1$ after.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 1 and 4, and [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-4|REL Theorem §B2.2.4]], 1 (the pseudotensor law, odd under $\mathcal P$ and $\mathcal T$ separately).

^sol-px-1-3-3

### X1.4.1 · Antiproton threshold on a fixed target
*[variation of PS1.4(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-4-1]]

> [!success]- Solution
> **Answer.** $E_{\rm th} = 7m_pc^2 = 6.57$ GeV, kinetic energy $K_{\rm th} = 6m_pc^2 = 5.63$ GeV.
>
> **Step 1** ($s$ in the lab). Beam $p_a = (E, \mathbf p)$ with $E^2 - \mathbf p^2 = m^2$ ($m \equiv m_p$, $c = 1$); target $p_b = (m, \mathbf 0)$. Then $s = (p_a + p_b)^2 = p_a^2 + p_b^2 + 2p_a\cdot p_b = m^2 + m^2 + 2Em = 2m(E + m)$.
>
> **Step 2** ($s$ in the centre-of-mass frame, after the collision). There $P = (\sum_iE_i^\ast, \mathbf 0)$ with each $E_i^\ast \ge m$ for the four final particles ($p, p, p, \bar p$, all of mass $m$). So $s = (\sum_iE_i^\ast)^2 \ge (4m)^2$, with equality exactly when all four are at rest in that frame.
>
> **Step 3** (threshold). $s$ is invariant and conserved, so the reaction needs $2m(E + m) \ge 16m^2$, i.e. $E \ge 7m$. With $m_pc^2 = 0.938$ GeV: $E_{\rm th} = 7 \times 0.938 = 6.566 \simeq 6.57$ GeV and $K_{\rm th} = E_{\rm th} - m_pc^2 = 6 \times 0.938 = 5.628 \simeq 5.63$ GeV.
>
> **Step 4** (check). The general formula $E_{\rm th} = (M_f^2 - m_a^2 - m_b^2)/2m_b$ with $M_f = 4m$, $m_a = m_b = m$ gives $(16 - 2)m/2 = 7m$; the naive "mass difference" $2m$ of kinetic energy is three times too small, because the products must carry the beam's momentum.
>
> *Checked against:* [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-7|REL Theorem §B2.1.7]] ($N = 4$: $E_{\rm th} = (\frac12N^2 - 1)mc^2 = 7mc^2$), [[§A8.3 Particle Accelerators and Detectors#^ex-a8-3-2|QM Example §A8.3.2]] ($K_1 = 6m_pc^2 = 5.6$ GeV) and [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-1|§C1a.5, Remark: Compute invariants, not transformations]].

^sol-px-1-4-1

### X1.4.2 · π⁰ → γγ at rest and in flight
*[variation of PS1.4(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-4-2]]

> [!success]- Solution
> **Answer.** (a) $E_\gamma = m/2$ each. (b) $E_\gamma = \frac12(E + p\cos\theta^\ast)$, so $E_{\max} = \frac12(E + p)$ and $E_{\min} = \frac12(E - p)$.
>
> **Step 1** ((a)). At rest the total momentum is zero, so the photons have $\mathbf k_2 = -\mathbf k_1$. Both are null, $E_i = |\mathbf k_i|$, hence $E_1 = E_2$; energy conservation $E_1 + E_2 = m$ gives $E_\gamma = m/2$ each.
>
> **Step 2** (one photon in the rest frame). $k^{\ast\mu} = \frac m2(1, \hat{\mathbf n})$, with $\theta^\ast$ the angle between $\hat{\mathbf n}$ and the direction in which the pion moves in the other frame.
>
> **Step 3** (boost). The pion has $E = \gamma m$, $p = \gamma\beta m$ ($\gamma = E/m$, $\gamma\beta = p/m$). The energy component of a boosted four-vector is $k^0 = \gamma(k^{\ast0} + \beta k^\ast_\parallel)$, so
> $$
> E_\gamma = \gamma\frac m2(1 + \beta\cos\theta^\ast) = \frac12\bigl(E + p\cos\theta^\ast\bigr) .
> $$
>
> **Step 4** (extremes). $\cos\theta^\ast$ ranges over $[-1, 1]$ and $E_\gamma$ is increasing in it: the maximum $\frac12(E + p)$ is the photon emitted forward, the minimum $\frac12(E - p)$ the one emitted backward. The two are emitted together (back to back in the rest frame).
>
> **Step 5** (checks). The two photons of one decay have $\theta^\ast$ and $\theta^\ast + \pi$, and their energies add to $\frac12(E + p\cos\theta^\ast) + \frac12(E - p\cos\theta^\ast) = E$. $E_{\max}E_{\min} = \frac14(E^2 - p^2) = m^2/4$, invariant. For $p \to 0$ both tend to $m/2$, part (a).
>
> *Checked against:* [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-10|REL Theorem §B2.1.10]] ($\omega_{\rm obs} = \gamma(1 + \beta\cos\theta')\omega_s$ with $\omega_s = m/2$; its approaching and receding cases are $\frac m2\sqrt{(1\pm\beta)/(1\mp\beta)} = \frac12(E \pm p)$) and [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|Example §C1a.2.1]] (back-to-back null momenta share the energy equally).

^sol-px-1-4-2

### X1.4.3 · The reduced Compton wavelength
*[variation of PS1.4(b), (d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-4-3]]

> [!success]- Solution
> **Answer.** $1/m \to \bar\lambda_C = \dfrac{\hbar}{mc} = \dfrac{\hbar c}{mc^2}$: electron $386$ fm $\simeq 3.86\times10^{-13}$ m, pion $1.41$ fm.
>
> **Step 1** (the type). The target is a length, ordinary dimension $M^0L^1T^0$: $\alpha = 0$, $\beta = 1$, $\gamma = 0$, mass dimension $d = \alpha - \beta - \gamma = -1$, consistent with $1/m$.
>
> **Step 2** (restore). The exponent rule $Q = Q_{\rm nat}\,\hbar^{\beta + \gamma}c^{-\beta - 2\gamma}$ gives $\hbar^1c^{-1}$: $1/m \to \hbar/(mc)$. Check by dimensions: $\hbar$ is energy × time, $mc$ is energy/velocity, the ratio is velocity × time = length. To use $\hbar c$ in MeV fm, multiply top and bottom by $c$: $\hbar/(mc) = \hbar c/(mc^2)$.
>
> **Step 3** (numbers). Electron: $197.3\ \text{MeV fm}/0.511\ \text{MeV} = 386.1$ fm $= 3.86\times10^{-13}$ m. Pion: $197.3/140$ fm $= 1.41$ fm, about the size of a nucleon: the range of the one-pion-exchange (Yukawa) force.
>
> **Step 4** (convention). The unreduced Compton wavelength is $2\pi$ times larger, $h/(mc)$ ($2426$ fm for the electron); which one is quoted is a convention of $2\pi$, as for the photon wavelength in PS1.4(d).
>
> *Checked against:* [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|Theorem §C1a.2.1]] (its derivation, step 5: "$1/m$ restores to $\hbar/mc$, the reduced Compton wavelength") and [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|Example §C1a.2.1]] (the same $\hbar c = 197.3$ MeV fm conversion and the $2\pi$ remark).

^sol-px-1-4-3

### X1.5.1 · The Mandelstam sum rule
*[extension of PS1.5(e)–(f)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-5-1]]

> [!success]- Solution
> **Answer.** $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.
>
> **Step 1** (expand each square with $p_i^2 = m_i^2$).
> $$
> s = m_1^2 + m_2^2 + 2p_1\cdot p_2, \qquad t = m_1^2 + m_3^2 - 2p_1\cdot p_3, \qquad u = m_1^2 + m_4^2 - 2p_1\cdot p_4 .
> $$
>
> **Step 2** (add). $s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 + 2p_1\cdot(p_2 - p_3 - p_4)$.
>
> **Step 3** (conservation). $p_1 + p_2 = p_3 + p_4$ gives $p_2 - p_3 - p_4 = -p_1$, so the last term is $-2p_1^2 = -2m_1^2$, and $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.
>
> **Step 4** (check). Elastic equal-mass scattering in the centre-of-mass frame: X1.5.3 below finds $s = 4(m^2 + p'^2)$, $t = -2p'^2(1 - \cos\theta')$, $u = -2p'^2(1 + \cos\theta')$, whose sum is $4m^2$.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1, and its derivation, steps 1–2 (the same computation).

^sol-px-1-5-1

### X1.5.2 · The centre-of-mass momentum and the Källén function
*[variation of PS1.5(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-5-2]]

> [!success]- Solution
> **Answer.** $p'^2 = \dfrac{\lambda(s, m_1^2, m_2^2)}{4s}$, and with $s = m_1^2 + m_2^2 + 2m_2E_{\rm lab}$ one has $\lambda = 4m_2^2p_{\rm lab}^2$, so $p' = m_2p_{\rm lab}/\sqrt s = m_2p_{\rm lab}/E_{\rm cms}$.
>
> **Step 1** ($E_1'$ from invariants). In the centre-of-mass frame $P = p_1 + p_2 = (\sqrt s, \mathbf 0)$. Write $p_2 = P - p_1$ and square: $m_2^2 = s - 2P\cdot p_1 + m_1^2 = s - 2\sqrt s\,E_1' + m_1^2$, so
> $$
> E_1' = \frac{s + m_1^2 - m_2^2}{2\sqrt s} .
> $$
>
> **Step 2** ($p'^2$). $p'^2 = E_1'^2 - m_1^2 = \dfrac{(s + m_1^2 - m_2^2)^2 - 4sm_1^2}{4s}$. Expand the numerator: $s^2 + m_1^4 + m_2^4 + 2sm_1^2 - 2sm_2^2 - 2m_1^2m_2^2 - 4sm_1^2 = s^2 + m_1^4 + m_2^4 - 2sm_1^2 - 2sm_2^2 - 2m_1^2m_2^2 = \lambda(s, m_1^2, m_2^2)$.
>
> **Step 3** (a useful form of $\lambda$). $\lambda(a, b, c) = (a - b - c)^2 - 4bc$: expanding, $(a - b - c)^2 = a^2 + b^2 + c^2 - 2ab - 2ac + 2bc$, and $-4bc$ turns $+2bc$ into $-2bc$.
>
> **Step 4** (compare with the lab formula). By the lab evaluation of $s$, $s - m_1^2 - m_2^2 = 2m_2E_{\rm lab}$. Then Step 3 gives $\lambda = 4m_2^2E_{\rm lab}^2 - 4m_1^2m_2^2 = 4m_2^2(E_{\rm lab}^2 - m_1^2) = 4m_2^2p_{\rm lab}^2$, so $p'^2 = m_2^2p_{\rm lab}^2/s$ and $p' = m_2p_{\rm lab}/E_{\rm cms}$ with $E_{\rm cms} = \sqrt s$.
>
> **Step 5** (checks). $\lambda$ is symmetric in its three arguments, so $p'$ is the same computed from particle 2; at threshold, $\sqrt s = m_1 + m_2$, $\lambda = ((m_1 + m_2)^2 - m_1^2 - m_2^2)^2 - 4m_1^2m_2^2 = 0$: $p' = 0$, as it must.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|Example §C1a.5.2]] ($p' = m_2p_{\rm lab}/E_{\rm cm}$ from the transverse tensor component) and [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-1|§C1a.5, Remark: Compute invariants, not transformations]] ($E_{\rm cm}^2 = m_1^2 + m_2^2 + 2m_2E_{\rm lab}$). The Källén form itself has no vault box: *Derived here; check:* reproduces Example §C1a.5.2 exactly (Step 4) and vanishes at threshold (Step 5).

^sol-px-1-5-2

### X1.5.3 · u for equal-mass elastic scattering
*[variation of PS1.5(f)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-5-3]]

> [!success]- Solution
> **Answer.** $u = -2p'^2(1 + \cos\theta') = -4p'^2\cos^2\tfrac{\theta'}{2}$; with $s = 4(m^2 + p'^2)$ and $t = -2p'^2(1 - \cos\theta')$, $s + t + u = 4m^2$.
>
> **Step 1** (centre-of-mass momenta). All masses $m$; $p_1' = (E, \mathbf p')$, $p_2' = (E, -\mathbf p')$, $p_3' = (E, \mathbf q')$, $p_4' = (E, -\mathbf q')$, all with the same $E$ (equal masses and back-to-back momenta of equal size) and $|\mathbf q'| = |\mathbf p'| = p'$ (energy conservation, $2\sqrt{p'^2 + m^2} = 2\sqrt{q'^2 + m^2}$); $\mathbf p'\cdot\mathbf q' = p'^2\cos\theta'$.
>
> **Step 2** ($u$). $u = (p_1' - p_4')^2 = 2m^2 - 2p_1'\cdot p_4' = 2m^2 - 2\bigl(E^2 - \mathbf p'\cdot(-\mathbf q')\bigr) = 2m^2 - 2E^2 - 2p'^2\cos\theta'$. With $E^2 = m^2 + p'^2$: $u = -2p'^2 - 2p'^2\cos\theta' = -2p'^2(1 + \cos\theta')$, and $1 + \cos\theta' = 2\cos^2(\theta'/2)$.
>
> **Step 3** ($s$ and $t$). $s = (2E)^2 = 4(m^2 + p'^2)$; $t = 2m^2 - 2(E^2 - p'^2\cos\theta') = -2p'^2(1 - \cos\theta')$.
>
> **Step 4** (sum). $s + t + u = 4m^2 + 4p'^2 - 2p'^2 + 2p'^2\cos\theta' - 2p'^2 - 2p'^2\cos\theta' = 4m^2$, the sum rule of X1.5.1 with four equal masses. $u$ is $t$ with $\theta' \to \pi - \theta'$: exchanging the labels 3 and 4 of identical final particles.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 3 (the $t$ formula, derivation steps 4–5, of which this is the computation with $p_4'$ in place of $p_3'$) and part 1 (the sum rule).

^sol-px-1-5-3

### X1.6.1 · The d'Alembertian of ρ and ρ² in d dimensions
*[variation of PS1.6(c)–(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-6-1]]

> [!success]- Solution
> **Answer.** $\Box\rho = 2d$, $\ \Box\rho^2 = 4(d + 2)\rho$, $\ \Box^2\rho^2 = 8d(d + 2)$; for $d = 4$: $8$, $24\rho$, $192$.
>
> **Step 1** (first derivatives; rename the dummy). Write $\rho = x_\nu x^\nu = g_{\alpha\beta}x^\alpha x^\beta$ (never $\rho$ as an index). Product rule with $\partial_\mu x^\alpha = \delta^\alpha{}_\mu$: $\partial_\mu\rho = g_{\alpha\beta}(\delta^\alpha{}_\mu x^\beta + x^\alpha\delta^\beta{}_\mu) = 2x_\mu$. Once more, $\partial_\nu\partial_\mu\rho = 2g_{\mu\alpha}\delta^\alpha{}_\nu = 2g_{\mu\nu}$.
>
> **Step 2** ($\Box\rho$). $\Box\rho = g^{\mu\nu}\partial_\mu\partial_\nu\rho = 2g^{\mu\nu}g_{\mu\nu} = 2\delta^\mu{}_\mu = 2d$: the trace of the identity in $d$ dimensions is $d$, a plain sum with no signs.
>
> **Step 3** ($\Box\rho^2$). Chain rule: $\partial_\mu\rho^2 = 2\rho\,\partial_\mu\rho = 4\rho x_\mu$. Then
> $$
> \Box\rho^2 = \partial^\mu(4\rho x_\mu) = 4(\partial^\mu\rho)x_\mu + 4\rho\,\partial^\mu x_\mu = 4\cdot2x^\mu x_\mu + 4\rho\,d = (8 + 4d)\rho ,
> $$
> using $\partial^\mu\rho = 2x^\mu$ and $\partial^\mu x_\mu = \delta^\mu{}_\mu = d$.
>
> **Step 4** ($\Box^2\rho^2$). $\Box^2\rho^2 = \Box\bigl(4(d + 2)\rho\bigr) = 4(d + 2)\cdot2d = 8d(d + 2)$.
>
> **Step 5** (checks). The general formula $\Box f(\rho) = 2d\,f' + 4\rho f''$ (X1.6.2) gives for $f = \rho$: $2d$; for $f = \rho^2$: $2d\cdot2\rho + 4\rho\cdot2 = (4d + 8)\rho$. At $d = 4$: $8$, $24\rho$, $192$, the values of PS1.6(c)–(d).
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] ($\partial^2\rho = 8$, $\partial^2\rho^2 = 24\rho$, $(\partial^2)^2\rho^2 = 192$ at $d = 4$; the $d$-dimensional formula $2d\,f' + 4\rho f''$), [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]], and the course solution SOL1, Problem 6(c)–(d).

^sol-px-1-6-1

### X1.6.2 · Functions of x² harmonic away from the light cone
*[extension of PS1.6(f)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-1-6-2]]

> [!success]- Solution
> **Answer.** $\Box f(\rho) = 4\rho f'' + 2d\,f'$; the solutions of $\Box f = 0$ are $f = c_1\lvert\rho\rvert^{1 - d/2} + c_2$, with constants chosen separately on $\rho > 0$ and on $\rho < 0$; for $d = 4$, $c_1/\rho + c_2$.
>
> **Step 1** (first derivative). Chain rule: $\partial_\mu f(\rho) = f'(\rho)\,\partial_\mu\rho = 2x_\mu f'(\rho)$ (X1.6.1, Step 1).
>
> **Step 2** (second derivative). $\Box f = \partial^\mu(2x_\mu f') = 2(\partial^\mu x_\mu)f' + 2x_\mu\,\partial^\mu f'(\rho)$. The first term is $2d\,f'$. In the second, Step 1 applied to $f'$ gives $\partial^\mu f' = 2x^\mu f''$, so it is $2x_\mu\cdot2x^\mu f'' = 4\rho f''$. Total: $\Box f = 4\rho f'' + 2d\,f'$.
>
> **Step 3** (the ordinary differential equation). On an interval where $\rho \ne 0$, put $h = f'$: $4\rho h' + 2d\,h = 0$, i.e. $h'/h = -d/(2\rho)$ where $h \ne 0$, so $h = c\,\lvert\rho\rvert^{-d/2}$ (a first-order linear equation: this is every solution, $h \equiv 0$ included as $c = 0$).
>
> **Step 4** (integrate). For $d > 2$ the exponent $1 - d/2 \ne 0$, so $f = c_1\lvert\rho\rvert^{1 - d/2} + c_2$, separately on $\rho > 0$ and $\rho < 0$ (a function of $\rho$ alone cannot connect the two regions through $\rho = 0$, where it blows up). For $d = 4$: $\lvert\rho\rvert^{-1} = \pm1/\rho$, absorbed into $c_1$: $f = c_1/\rho + c_2$, PS1.6(f). ($d = 2$ is the excluded case: $h \propto 1/\rho$, $f = c_1\ln\lvert\rho\rvert + c_2$.)
>
> **Step 5** (direct check). For $\rho > 0$ and $f = \rho^a$, $a = 1 - d/2$: $4\rho f'' + 2d\,f' = a\rho^{a - 1}\bigl(4(a - 1) + 2d\bigr) = a\rho^{a - 1}(-2d + 2d) = 0$. For $\rho < 0$ and $f = (-\rho)^a$: $f' = -a(-\rho)^{a - 1}$, $f'' = a(a - 1)(-\rho)^{a - 2}$, and $4\rho f'' + 2d\,f' = -a(-\rho)^{a - 1}\bigl(4(a - 1) + 2d\bigr) = 0$.
>
> **Step 6** (why $\rho \ne 0$). The computation is pointwise off the light cone; across it $\lvert\rho\rvert^{1 - d/2}$ is not locally integrable and is no distribution by itself. Its boundary values ($x^2 - i0\,x^0$, or $x^2 - i0$) solve $\partial^2 D = 0$ or $\partial^2 D = -i\delta^4$ on all of spacetime (in $d = 4$): the source sits at the tip $x = 0$ of the cone, invisible to this calculation.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] and its derivation, step 4 ("in $d$ dimensions $f' \propto \rho^{-d/2}$, $f \propto \rho^{1 - d/2}$"), and [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]] (Step 6).

^sol-px-1-6-2

---

## B. Classical fields, Euler–Lagrange, Hamiltonian, Noether

### X2.1.1 · The dilaton is a free field in disguise
*[extension of PS2.1(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-1-1]]

> [!success]- Solution
> **Answer.** $\Box\sigma = -e^{-\tau}\bigl[\Box\tau - (\partial\tau)^2\bigr]$, so $\Box\tau = (\partial\tau)^2 \iff \Box\sigma = 0$; and $(\partial\sigma)^2 = e^{-2\tau}(\partial\tau)^2$ gives $\mathcal L = -f^2(\partial\sigma)^2$.
>
> **Step 1** (first derivative). Chain rule: $\partial_\mu\sigma = \partial_\mu e^{-\tau} = -e^{-\tau}\,\partial_\mu\tau$.
>
> **Step 2** ($\Box\sigma$). Product rule on $\partial^\mu\bigl(-e^{-\tau}\partial_\mu\tau\bigr)$, with $\partial^\mu e^{-\tau} = -e^{-\tau}\partial^\mu\tau$:
> $$
> \Box\sigma = -(\partial^\mu e^{-\tau})\,\partial_\mu\tau - e^{-\tau}\,\Box\tau = e^{-\tau}(\partial\tau)^2 - e^{-\tau}\Box\tau = -e^{-\tau}\bigl[\Box\tau - (\partial\tau)^2\bigr] .
> $$
> If $\tau$ solves PS2.1(b), the bracket vanishes and $\Box\sigma = 0$. Conversely, $e^{-\tau} \ne 0$, so $\Box\sigma = 0$ implies the dilaton equation: the two equations are equivalent.
>
> **Step 3** (the Lagrangian). $(\partial\sigma)^2 = \partial_\mu\sigma\,\partial^\mu\sigma = (-e^{-\tau})^2\,\partial_\mu\tau\,\partial^\mu\tau = e^{-2\tau}(\partial\tau)^2$, so $\mathcal L = -f^2e^{-2\tau}(\partial\tau)^2 = -f^2(\partial\sigma)^2$.
>
> **Step 4** (consistency). The Euler–Lagrange equation of $\mathcal L = -f^2(\partial\sigma)^2$: $\partial\mathcal L/\partial(\partial_\mu\sigma) = -2f^2\partial^\mu\sigma$ (both factors respond), $\partial\mathcal L/\partial\sigma = 0$, so $-2f^2\Box\sigma = 0$, the free massless equation, in agreement with Step 2. The map $\tau \mapsto \sigma = e^{-\tau}$ is a bijection onto $\sigma > 0$: the dilaton is a free massless scalar written in nonlinear variables, $\sigma_c = \sqrt2f\sigma$ having $\mathcal L = -\frac12(\partial\sigma_c)^2$; the overall minus sign is the mostly-plus sign of the problem sheet, which does not affect the field equation.
>
> **Step 5** (numerical check). $\sigma = 1 + k\cdot x$ solves $\Box\sigma = 0$. Then $\tau = -\ln(1 + k\cdot x)$ has $\partial_\mu\tau = -k_\mu/(1 + k\cdot x)$, $(\partial\tau)^2 = k^2/(1 + k\cdot x)^2$, and $\Box\tau = \partial^\mu\bigl(-k_\mu(1 + k\cdot x)^{-1}\bigr) = k^2/(1 + k\cdot x)^2$: equal, as claimed.
>
> *Derived here; check:* Step 2 reproduces the field equation of [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-1|Example §C1b.2.1]] (where the same two $(\partial\tau)^2$ terms appear with the same relative sign), Step 4 uses [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^cau-c1b-2-3|§C1b.2, Caution: Rename the dummy index before differentiating]], and Step 5 is an explicit solution.

^sol-px-2-1-1

### X2.1.2 · A field-dependent kinetic term
*[variation of PS2.1(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-1-2]]

> [!success]- Solution
> **Answer.** $K(\phi)\,\Box\phi + \tfrac12K'(\phi)\,(\partial\phi)^2 + V'(\phi) = 0$; for $K = -2f^2e^{-2\phi}$, $V = 0$ it is $\Box\phi = (\partial\phi)^2$.
>
> **Step 1** ($\partial\mathcal L/\partial(\partial_\mu\phi)$). Rename the dummy: $\mathcal L = \frac12K(\phi)\,g^{\alpha\beta}\partial_\alpha\phi\,\partial_\beta\phi - V(\phi)$. Both factors respond, $\partial(\partial_\alpha\phi)/\partial(\partial_\mu\phi) = \delta^\mu{}_\alpha$: $\partial\mathcal L/\partial(\partial_\mu\phi) = \frac12K(g^{\mu\beta}\partial_\beta\phi + g^{\alpha\mu}\partial_\alpha\phi) = K\,\partial^\mu\phi$.
>
> **Step 2** (its divergence). Product rule, with $\partial_\mu K(\phi) = K'(\phi)\,\partial_\mu\phi$: $\partial_\mu(K\partial^\mu\phi) = K'(\partial\phi)^2 + K\,\Box\phi$.
>
> **Step 3** ($\partial\mathcal L/\partial\phi$). $\phi$ appears undifferentiated in $K$ and in $V$: $\partial\mathcal L/\partial\phi = \frac12K'(\partial\phi)^2 - V'$.
>
> **Step 4** (Euler–Lagrange). $K'(\partial\phi)^2 + K\Box\phi - \frac12K'(\partial\phi)^2 + V' = 0$, i.e. $K\Box\phi + \frac12K'(\partial\phi)^2 + V' = 0$. The derivative term of $K$ appears twice, once from the divergence (coefficient $1$) and once from $\partial\mathcal L/\partial\phi$ (coefficient $-\frac12$): only the difference $\frac12$ survives.
>
> **Step 5** (the dilaton). $K = -2f^2e^{-2\phi}$ makes $\frac12K(\partial\phi)^2 = -f^2e^{-2\phi}(\partial\phi)^2$, the PS2.1 density. $K' = 4f^2e^{-2\phi} = -2K$, so Step 4 with $V = 0$ is $K\Box\phi - K(\partial\phi)^2 = 0$; dividing by $K \ne 0$: $\Box\phi = (\partial\phi)^2$, PS2.1(b).
>
> **Step 6** (second check). $K = 1$, $V = \frac12m^2\phi^2$: $\Box\phi + m^2\phi = 0$, Klein–Gordon. (For $K > 0$ the variable $\chi = \int^\phi\sqrt{K}\,d\phi$ makes the kinetic term canonical, $\frac12(\partial\chi)^2$; for the dilaton's $K < 0$ the same with $\sqrt{\lvert K\rvert}$ gives $\chi = -\sqrt2fe^{-\phi}$ and $\mathcal L = -\frac12(\partial\chi)^2$, the free field of X2.1.1.)
>
> *Derived here; check:* reduces to [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-1|Example §C1b.2.1]] for the dilaton (Step 5; its terms $4f^2e^{-2\tau}(\partial\tau)^2$ and $2f^2e^{-2\tau}(\partial\tau)^2$ are $K'(\partial\phi)^2$ and $\frac12K'(\partial\phi)^2$ here, up to the overall sign) and to Klein–Gordon for $K = 1$; Euler–Lagrange as in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-4|Theorem §C1b.2.4]].

^sol-px-2-1-2

### X2.2.1 · Canonical normalization of the two-scalar theory
*[extension of PS2.2(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-2-1]]

> [!success]- Solution
> **Answer.** $\mathcal L = \frac12\partial_\mu\chi_1\partial^\mu\chi_1 + \frac12\partial_\mu\chi_2\partial^\mu\chi_2 - \frac12m^2\chi_1^2 - \dfrac{\mu}{2\sqrt2}\chi_1\chi_2^2 - \dfrac{\lambda}{4}\chi_1^2\chi_2^2$: $\chi_1$ has mass $m$, $\chi_2$ is massless; cubic coupling $\mu/(2\sqrt2)$ (coefficient of $-\chi_1\chi_2^2$), quartic coupling $\lambda/4$ (coefficient of $-\chi_1^2\chi_2^2$).
>
> **Step 1** (substitute term by term). With $\phi_i = \chi_i/\sqrt2$: $\partial_\mu\phi_i\partial^\mu\phi_i = \frac12\partial_\mu\chi_i\partial^\mu\chi_i$; $m^2\phi_1^2 = \frac12m^2\chi_1^2$; $\mu\phi_1\phi_2^2 = \mu\,2^{-1/2}2^{-1}\chi_1\chi_2^2 = \frac{\mu}{2\sqrt2}\chi_1\chi_2^2$; $\lambda\phi_1^2\phi_2^2 = \frac\lambda4\chi_1^2\chi_2^2$.
>
> **Step 2** (read off). The kinetic terms now have the canonical $\frac12$. A mass term is $-\frac12M^2\chi^2$: $M_1 = m$ for $\chi_1$; there is no $\chi_2^2$ term, so $\chi_2$ is massless (about $\chi = 0$). The interactions are $-\frac{\mu}{2\sqrt2}\chi_1\chi_2^2$ and $-\frac\lambda4\chi_1^2\chi_2^2$. (If one prefers to write them as $-\frac{g}{2}\chi_1\chi_2^2$ and $-\frac{\kappa}{4}\chi_1^2\chi_2^2$, then $g = \mu/\sqrt2$ and $\kappa = \lambda$: the "coupling" depends on the normalization chosen for the vertex, the Lagrangian does not.)
>
> **Step 3** (check against the field equations). The course solution's equation for $\phi_1$, $2\Box\phi_1 = -2m^2\phi_1 - \mu\phi_2^2 - 2\lambda\phi_1\phi_2^2$, with $\phi_i = \chi_i/\sqrt2$ and multiplied by $1/\sqrt2$, reads $\Box\chi_1 = -m^2\chi_1 - \frac{\mu}{2\sqrt2}\chi_2^2 - \frac\lambda2\chi_1\chi_2^2$. The Euler–Lagrange equation of the canonical $\mathcal L$ gives the same: $\Box\chi_1 = \partial\mathcal L/\partial\chi_1 = -m^2\chi_1 - \frac{\mu}{2\sqrt2}\chi_2^2 - \frac\lambda2\chi_1\chi_2^2$.
>
> **Step 4** (dimensions unchanged). $[\chi_i] = [\phi_i] = 1$, so $[\mu/(2\sqrt2)] = 1$ and $[\lambda/4] = 0$, as in PS2.2(d).
>
> *Derived here; check:* [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-2|§C1b.4, Remark: Several fields, and a non-canonical normalization]] ("rescaling $\phi \to \phi/\sqrt2$ restores the canonical form") and the course solution SOL2, Problem 2(a), whose field equation is reproduced in Step 3.

^sol-px-2-2-1

### X2.2.2 · Momentum and Hamiltonian with a wave-function factor Z
*[variation of PS2.2(b)–(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-2-2]]

> [!success]- Solution
> **Answer.** $\pi = Z\dot\phi$, $\ \mathcal H = \dfrac{\pi^2}{2Z} + \dfrac Z2(\nabla\phi)^2 + V(\phi)$.
>
> **Step 1** (split time and space). $\partial_\mu\phi\,\partial^\mu\phi = \dot\phi^2 - (\nabla\phi)^2$, so $\mathcal L = \frac Z2\dot\phi^2 - \frac Z2(\nabla\phi)^2 - V(\phi)$.
>
> **Step 2** (momentum). $\pi = \partial\mathcal L/\partial\dot\phi$, with $\phi$ and $\nabla\phi$ held fixed: $\pi = Z\dot\phi$. Since $Z > 0$ this can be solved, $\dot\phi = \pi/Z$.
>
> **Step 3** (Legendre transform, velocities eliminated).
> $$
> \mathcal H = \pi\dot\phi - \mathcal L = Z\dot\phi^2 - \tfrac Z2\dot\phi^2 + \tfrac Z2(\nabla\phi)^2 + V = \tfrac Z2\dot\phi^2 + \tfrac Z2(\nabla\phi)^2 + V = \frac{\pi^2}{2Z} + \frac Z2(\nabla\phi)^2 + V(\phi) .
> $$
> The last form is the Hamiltonian density proper: a function of $\phi$, $\nabla\phi$, $\pi$ only.
>
> **Step 4** (checks). $Z = 1$: $\pi = \dot\phi$, $\mathcal H = \frac12\pi^2 + \frac12(\nabla\phi)^2 + V$, the canonical case. $Z = 2$ (PS2.2, no $\frac12$): $\pi = 2\dot\phi$, $\mathcal H = \frac14\pi^2 + (\nabla\phi)^2 + V$, as in the course solution. Hamilton's equation $\dot\phi = \partial\mathcal H/\partial\pi = \pi/Z$ returns Step 2, and $\dot\pi = -\delta H/\delta\phi = Z\nabla^2\phi - V'$ with $\pi = Z\dot\phi$ gives $Z\Box\phi + V' = 0$, the Euler–Lagrange equation.
>
> *Checked against:* [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-1|Def. §C1b.4.1]], [[§C1b.4 Hamiltonian Field Theory#^def-c1b-4-2|Def. §C1b.4.2]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]] ($Z = 1$) and [[§C1b.4 Hamiltonian Field Theory#^rem-c1b-4-2|§C1b.4, Remark: Several fields, and a non-canonical normalization]] ($Z = 2$: $\pi = 2\dot\phi$, $\mathcal H = \frac14\pi^2 + (\nabla\phi)^2 + \dots$).

^sol-px-2-2-2

### X2.3.1 · Two complex fields: which phase rotation survives
*[variation of PS2.3(c)–(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-3-1]]

> [!success]- Solution
> **Answer.** Only the opposite rotation, $\phi_1 \to e^{i\alpha}\phi_1$, $\phi_2 \to e^{-i\alpha}\phi_2$, is a symmetry (for $g \ne 0$). Its current is
> $$
> j^\mu = i\bigl(\phi_1\partial^\mu\phi_1^{\ast} - \phi_1^{\ast}\partial^\mu\phi_1\bigr) - i\bigl(\phi_2\partial^\mu\phi_2^{\ast} - \phi_2^{\ast}\partial^\mu\phi_2\bigr) ,
> $$
> the PS2.3(d) current of $\phi_1$ minus that of $\phi_2$.
>
> **Step 1** (test both rotations). The kinetic and mass terms are sums of $\phi_i^{\ast}(\cdots)\phi_i$ and are invariant under any constant phases. The coupling: $\phi_1\phi_2 \to e^{i\alpha}e^{\pm i\alpha}\phi_1\phi_2$. With the lower sign, $e^{0} = 1$: $\delta\mathcal L = 0$ identically, a symmetry with $\mathcal J = 0$. With the upper sign, $\phi_1\phi_2 \to e^{2i\alpha}\phi_1\phi_2$ and to first order $\delta\mathcal L = -g\,2i\alpha(\phi_1\phi_2 - \phi_1^{\ast}\phi_2^{\ast})$, a nonzero function of the fields with no derivatives, not a divergence for every configuration: no symmetry (outcome (iii) of Def. §C1b.5.5). So $\phi_1$ carries charge $+1$ and $\phi_2$ charge $-1$, and the coupling $\phi_1\phi_2$ is neutral.
>
> **Step 2** (generators). With $\Delta\phi_1 = i\phi_1$: $\Delta\phi_1^{\ast} = -i\phi_1^{\ast}$, $\Delta\phi_2 = -i\phi_2$, $\Delta\phi_2^{\ast} = +i\phi_2^{\ast}$.
>
> **Step 3** (derivatives). $\phi_i$ and $\phi_i^{\ast}$ are independent variables; $\partial\mathcal L/\partial(\partial_\mu\phi_i) = \partial^\mu\phi_i^{\ast}$ and $\partial\mathcal L/\partial(\partial_\mu\phi_i^{\ast}) = \partial^\mu\phi_i$ (one factor responds each time; the coupling has no derivatives).
>
> **Step 4** (Noether, summed over all four fields).
> $$
> j^\mu = \partial^\mu\phi_1^{\ast}(i\phi_1) + \partial^\mu\phi_1(-i\phi_1^{\ast}) + \partial^\mu\phi_2^{\ast}(-i\phi_2) + \partial^\mu\phi_2(i\phi_2^{\ast}) ,
> $$
> which regroups into the Answer.
>
> **Step 5** (conservation check). The field equations (vary $\phi_1^{\ast}$, $\phi_1$, $\phi_2^{\ast}$, $\phi_2$): $\Box\phi_1 = -m^2\phi_1 - g\phi_2^{\ast}$, $\Box\phi_1^{\ast} = -m^2\phi_1^{\ast} - g\phi_2$, $\Box\phi_2 = -m^2\phi_2 - g\phi_1^{\ast}$, $\Box\phi_2^{\ast} = -m^2\phi_2^{\ast} - g\phi_1$. For $j_i^\mu = i(\phi_i\partial^\mu\phi_i^{\ast} - \phi_i^{\ast}\partial^\mu\phi_i)$ the $\partial\phi\cdot\partial\phi^{\ast}$ terms cancel and $\partial_\mu j_i^\mu = i(\phi_i\Box\phi_i^{\ast} - \phi_i^{\ast}\Box\phi_i)$. The $m^2$ terms cancel, leaving $\partial_\mu j_1^\mu = i(-g\phi_1\phi_2 + g\phi_1^{\ast}\phi_2^{\ast})$ and $\partial_\mu j_2^\mu = i(-g\phi_2\phi_1 + g\phi_2^{\ast}\phi_1^{\ast})$, the same. So $\partial_\mu(j_1^\mu - j_2^\mu) = 0$, while $j_1 + j_2$ (the would-be current of the upper-sign rotation) has divergence $-2ig(\phi_1\phi_2 - \phi_1^{\ast}\phi_2^{\ast}) \ne 0$, matching Step 1.
>
> *Derived here; check:* each $j_i$ is the current of [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]] (sign convention $\Delta\phi = +i\phi$, [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]); the current formula, summed over every field the parameter moves, is [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]; the symmetry test is [[§C1b.5 Noether's Theorem#^def-c1b-5-5|Def. §C1b.5.5]]; Step 5 verifies conservation on shell.

^sol-px-2-3-1

### X2.3.2 · The U(1) current in real components
*[variation of PS2.3(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-3-2]]

> [!success]- Solution
> **Answer.** $e^{i\alpha}$ rotates $(\phi_1, \phi_2)$ by the angle $\alpha$; the Noether current is $j^\mu = \phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$, identical to $i(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi)$.
>
> **Step 1** (the rotation). $e^{i\alpha}(\phi_1 + i\phi_2) = (\cos\alpha\,\phi_1 - \sin\alpha\,\phi_2) + i(\sin\alpha\,\phi_1 + \cos\alpha\,\phi_2)$, so
> $$
> \begin{pmatrix}\phi_1\\\phi_2\end{pmatrix} \to \begin{pmatrix}\cos\alpha & -\sin\alpha\\ \sin\alpha & \cos\alpha\end{pmatrix}\begin{pmatrix}\phi_1\\\phi_2\end{pmatrix} ,
> $$
> an $SO(2)$ rotation by $\alpha$ (U(1) $\cong$ SO(2)). Generators: $\Delta\phi_1 = -\phi_2$, $\Delta\phi_2 = +\phi_1$.
>
> **Step 2** (the Lagrangian in real fields). $\partial_\mu\phi^{\ast}\partial^\mu\phi = \frac12(\partial_\mu\phi_1 - i\partial_\mu\phi_2)(\partial^\mu\phi_1 + i\partial^\mu\phi_2) = \frac12\bigl[(\partial\phi_1)^2 + (\partial\phi_2)^2\bigr]$ (the cross terms cancel), and $\phi^{\ast}\phi = \frac12(\phi_1^2 + \phi_2^2)$. So $\mathcal L = \frac12(\partial\phi_1)^2 + \frac12(\partial\phi_2)^2 - \frac12m^2(\phi_1^2 + \phi_2^2) - V\bigl(\frac12(\phi_1^2 + \phi_2^2)\bigr)$: two canonical real fields, and every term depends only on rotation-invariant combinations, so $\delta\mathcal L = 0$, $\mathcal J = 0$.
>
> **Step 3** (Noether in real fields). $\partial\mathcal L/\partial(\partial_\mu\phi_i) = \partial^\mu\phi_i$, so $j^\mu = \partial^\mu\phi_1(-\phi_2) + \partial^\mu\phi_2(\phi_1) = \phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$.
>
> **Step 4** (compare). $\phi\,\partial^\mu\phi^{\ast} = \frac12(\phi_1 + i\phi_2)(\partial^\mu\phi_1 - i\partial^\mu\phi_2) = \frac12\bigl[\phi_1\partial^\mu\phi_1 + \phi_2\partial^\mu\phi_2 + i(\phi_2\partial^\mu\phi_1 - \phi_1\partial^\mu\phi_2)\bigr]$, and $\phi^{\ast}\partial^\mu\phi$ is its complex conjugate. Their difference is $i(\phi_2\partial^\mu\phi_1 - \phi_1\partial^\mu\phi_2)$, and multiplying by $i$: $i(\phi\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi) = -(\phi_2\partial^\mu\phi_1 - \phi_1\partial^\mu\phi_2) = \phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$. Same current, same sign: the generator $\Delta\phi = i\phi$ is the counterclockwise rotation.
>
> **Step 5** (conservation). $\partial_\mu j^\mu = \phi_1\Box\phi_2 - \phi_2\Box\phi_1$ (the $\partial\phi_1\cdot\partial\phi_2$ terms cancel). The field equations are $\Box\phi_i = -(m^2 + V')\phi_i$, since $\partial V/\partial\phi_i = V'\,\phi_i$; hence $\partial_\mu j^\mu = -(m^2 + V')(\phi_1\phi_2 - \phi_2\phi_1) = 0$. The charge $\int d^3x\,(\phi_1\dot\phi_2 - \phi_2\dot\phi_1)$ is the angular momentum of the rotation in field space.
>
> *Checked against:* [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]] (the complex form of the current) and [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]] (two canonical real fields for $\phi = (\phi_1 + i\phi_2)/\sqrt2$); the real-field form itself is *derived here*, checked by Step 4.

^sol-px-2-3-2

### X2.4.1 · The Proca equation and its constraint
*[variation of PS2.4(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-4-1]]

> [!success]- Solution
> **Answer.** $\partial_\mu F^{\mu\nu} + m^2A^\nu = 0$; its divergence gives $m^2\partial_\nu A^\nu = 0$, so $\partial_\nu A^\nu = 0$ for $m \ne 0$, and then $(\partial^2 + m^2)A^\nu = 0$.
>
> **Step 1** (derivatives). As in PS2.4(a), with the sixteen $\partial_\mu A_\nu$ independent, $\partial(F_{\alpha\beta}F^{\alpha\beta})/\partial(\partial_\mu A_\nu) = 4F^{\mu\nu}$ (both factors respond, and antisymmetry collects four equal terms), so $\partial\mathcal L/\partial(\partial_\mu A_\nu) = -\frac14\cdot4F^{\mu\nu} = -F^{\mu\nu}$. The mass term $\frac12m^2g^{\alpha\beta}A_\alpha A_\beta$ gives $\partial\mathcal L/\partial A_\nu = \frac12m^2(g^{\nu\beta}A_\beta + g^{\alpha\nu}A_\alpha) = m^2A^\nu$.
>
> **Step 2** (Euler–Lagrange). For each $A_\nu$: $\partial_\mu(-F^{\mu\nu}) - m^2A^\nu = 0$, i.e. $\partial_\mu F^{\mu\nu} + m^2A^\nu = 0$: Maxwell's equation with the current $J^\nu = -m^2A^\nu$.
>
> **Step 3** (divergence). $\partial_\nu\partial_\mu F^{\mu\nu} = 0$ identically: renaming $\mu \leftrightarrow \nu$ and using $F^{\nu\mu} = -F^{\mu\nu}$ and $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$, it equals minus itself. Applying $\partial_\nu$ to Step 2: $0 + m^2\partial_\nu A^\nu = 0$, and for $m \ne 0$, $\partial_\nu A^\nu = 0$: a consequence of the equation, not a gauge choice.
>
> **Step 4** (Klein–Gordon). $\partial_\mu F^{\mu\nu} = \partial_\mu\partial^\mu A^\nu - \partial^\nu(\partial_\mu A^\mu) = \partial^2A^\nu$ by Step 3, so Step 2 becomes $(\partial^2 + m^2)A^\nu = 0$ for each component. Conversely these two conditions give back Step 2.
>
> **Step 5** (the massless case). For $m = 0$ Step 3 is $0 = 0$: $\partial_\nu A^\nu$ is unconstrained, which is the gauge freedom of Maxwell theory (there the Lorenz condition is chosen). For $m \ne 0$ the constraint removes the spin-0 polarization $\varepsilon \propto p$, leaving three.
>
> *Checked against:* [[§C4.2★ The Proca Field#^thm-c4-2-2|Theorem §C4.2.2]] (the two derivatives), [[§C4.2★ The Proca Field#^thm-c4-2-3|Theorem §C4.2.3]] (the field equation), [[§C4.2★ The Proca Field#^thm-c4-2-4|Theorem §C4.2.4]] (the Lorenz condition, including the $m \ne 0$ by-product) and [[§C4.2★ The Proca Field#^thm-c4-2-5|Theorem §C4.2.5]] (Klein–Gordon plus Lorenz); the course solution SOL2, Problem 4(a), for the $m = 0$ derivative.

^sol-px-2-4-1

### X2.4.2 · The improved Maxwell tensor is traceless (in four dimensions)
*[extension of PS2.4(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-2-4-2]]

> [!success]- Solution
> **Answer.** $g_{\mu\nu}T_B^{\mu\nu} = -F_{\lambda\sigma}F^{\lambda\sigma} + \frac{d}{4}F_{\lambda\sigma}F^{\lambda\sigma} = \frac{d - 4}{4}F_{\lambda\sigma}F^{\lambda\sigma}$: zero for $d = 4$; in $d \ne 4$ dimensions the tensor is not traceless (except on configurations with $F_{\lambda\sigma}F^{\lambda\sigma} = 0$).
>
> **Step 1** (first term). $g_{\mu\nu}F^{\mu\lambda}F^\nu{}_\lambda = F^{\mu\lambda}\bigl(g_{\mu\nu}F^\nu{}_\lambda\bigr) = F^{\mu\lambda}F_{\mu\lambda} = F_{\lambda\sigma}F^{\lambda\sigma}$ (lowering $\nu$, then renaming dummies). So the first term contributes $-F_{\lambda\sigma}F^{\lambda\sigma}$.
>
> **Step 2** (second term). $g_{\mu\nu}g^{\mu\nu} = \delta^\mu{}_\mu = d$, a plain sum: $4$ in four dimensions. The second term contributes $\frac d4F_{\lambda\sigma}F^{\lambda\sigma}$.
>
> **Step 3** (sum). $g_{\mu\nu}T_B^{\mu\nu} = \bigl(\frac d4 - 1\bigr)F_{\lambda\sigma}F^{\lambda\sigma}$: zero exactly in $d = 4$, where the $\frac14$ of the Lagrangian matches the trace of the metric.
>
> **Step 4** (component check, $d = 4$). $T_B^{00} = \frac12(\mathbf E^2 + \mathbf B^2)$ and $T_B^{ij} = -(E^iE^j - \frac12\delta_{ij}\mathbf E^2) - (B^iB^j - \frac12\delta_{ij}\mathbf B^2)$ (§C1b.8, Connections), so $\sum_iT_B^{ii} = -(\mathbf E^2 - \frac32\mathbf E^2) - (\mathbf B^2 - \frac32\mathbf B^2) = \frac12(\mathbf E^2 + \mathbf B^2)$, and $g_{\mu\nu}T_B^{\mu\nu} = T_B^{00} - \sum_iT_B^{ii} = 0$: radiation has pressure one third of its energy density.
>
> **Step 5** (what changes in $d$ dimensions). The derivation of $T_B$ (PS2.4(c)–(d)) never used $d = 4$, so the same symmetric, conserved tensor exists for every $d$; only its trace changes, by $\frac{d - 4}{4}F^2$. A traceless symmetric tensor goes with scale invariance ([[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-4|§C1b.8, ★ Remark: Dilatations]]); $d = 4$ is also where the gauge coupling is dimensionless, $[A] = \frac{d - 2}{2}$ and $[e] = 1 - [A] = \frac{4 - d}{2}$.
>
> *Derived here; check:* the tensor is that of [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]], item 5 (and SOL2, Problem 4(d)); its trace is not computed there, so Steps 1–3 are new, and Step 4 checks them on the components of item 6 and the stress tensor of §C1b.8's Connections.

^sol-px-2-4-2

---

<!-- Fragment sol-CD: solutions to sections C (X3.1.1–X6.2.2) and D (X4.0.1–X4.4.3) of PHY 513 Practice Midterm 2 (Extended Set). Writer agent, 2026-10-14. -->

## C. Canonical quantization: modes, charges, states

### X3.1.1 · The invariant normalisation of momentum states
*[variation of PS3.1(e)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-1-1]]

> [!success]- Solution
> **Answer.** $E_{\mathbf p}\,\delta^3(\mathbf p - \mathbf q) = E_{\mathbf p'}\,\delta^3(\mathbf p' - \mathbf q')$ under every proper orthochronous $\Lambda$ (while $\delta^3$ alone picks up $E_{\mathbf p'}/E_{\mathbf p}$), so $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is invariant.
>
> **Step 1** (boost along $z$). With velocity $\beta$, on the shell $E = E_{\mathbf p}$: $p_3' = \gamma(p_3 + \beta E)$, $E' = \gamma(E + \beta p_3)$, $p_{1,2}' = p_{1,2}$. On the shell $dE/dp_3 = p_3/E$, so
> $$
> \frac{dp_3'}{dp_3} = \gamma\Bigl(1 + \beta\frac{p_3}{E}\Bigr) = \frac{\gamma(E + \beta p_3)}{E} = \frac{E'}{E} > 0 .
> $$
>
> **Step 2** (compose the δ). $p_3' - q_3'$, as a function of $p_3$ at fixed $\mathbf q$, has the single simple zero $p_3 = q_3$ (transverse components already equal), with derivative $E'/E$. The composition rule gives $\delta(p_3' - q_3') = \frac{E}{E'}\delta(p_3 - q_3)$; the transverse δ's are unchanged. Hence
> $$
> \delta^3(\mathbf p - \mathbf q) = \frac{E'}{E}\,\delta^3(\mathbf p' - \mathbf q') \quad\Longleftrightarrow\quad E\,\delta^3(\mathbf p - \mathbf q) = E'\,\delta^3(\mathbf p' - \mathbf q') .
> $$
>
> **Step 3** (every Λ). A proper orthochronous $\Lambda$ is a rotation times a boost along $z$ times a rotation; rotations fix $E$ and map $\delta^3(\mathbf p - \mathbf q)$ to $\delta^3(R\mathbf p - R\mathbf q)$ ($|\det R| = 1$). So $2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$ is invariant. Equivalently (the vault's first route): for a test function $g$, $g(\mathbf q) = \int\frac{d^3p}{2E_{\mathbf p}}\,[2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)]\,g(\mathbf p)$; the left side is a scalar and $d^3p/2E_{\mathbf p}$ is invariant (PS3.1(a)–(d)), so the kernel in brackets is invariant.
>
> **Step 4** (the overlap). With $|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\hat a^\dagger_{\mathbf p}|0\rangle$, $\hat a_{\mathbf p}|0\rangle = 0$ and $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$:
> $$
> \langle\mathbf p|\mathbf q\rangle = \sqrt{4E_{\mathbf p}E_{\mathbf q}}\,\langle0|\bigl(\hat a^\dagger_{\mathbf q}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf p - \mathbf q)\bigr)|0\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q) ,
> $$
> using $\sqrt{4E_{\mathbf p}E_{\mathbf q}} = 2E_{\mathbf p}$ on the support of the δ. By Step 3 and since $(2\pi)^3$ is a constant, this is invariant. *Physical reading:* a box of volume $V$ contracts to $V/\gamma$, so a density $\delta^3$ cannot be invariant; the factor $E$ compensates.
>
> *Checked against:* [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]] (both derivations: the reproducing kernel and the direct boost, $dp_3'/dp_3 = E'/E$) and [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]; composition rule [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2.

^sol-px-3-1-1

### X3.1.2 · The lower shell and the full shell
*[variation of PS3.1(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-1-2]]

> [!success]- Solution
> **Answer.** $\displaystyle\int d^4k\,\delta(k^2 - m^2)\,\theta(-k^0)\,f(k) = \int\frac{d^3k}{2E_{\mathbf k}}\,f(-E_{\mathbf k}, \mathbf k)$ and $\displaystyle\int d^4k\,\delta(k^2 - m^2)\,f(k) = \int\frac{d^3k}{2E_{\mathbf k}}\bigl[f(E_{\mathbf k}, \mathbf k) + f(-E_{\mathbf k}, \mathbf k)\bigr]$.
>
> **Step 1** (the δ in $k^0$). $k^2 - m^2 = (k^0)^2 - E_{\mathbf k}^2$ has the simple zeros $k^0 = \pm E_{\mathbf k}$, with $\bigl|\partial_{k^0}(k^2 - m^2)\bigr| = |2k^0| = 2E_{\mathbf k}$ at both. The composition rule gives
> $$
> \delta(k^2 - m^2) = \frac{\delta(k^0 - E_{\mathbf k}) + \delta(k^0 + E_{\mathbf k})}{2E_{\mathbf k}} .
> $$
>
> **Step 2** (lower shell). $\theta(-k^0)$ is $0$ at $k^0 = +E_{\mathbf k} > 0$ and $1$ at $k^0 = -E_{\mathbf k} < 0$ (for $m > 0$ neither root is at $k^0 = 0$, so $\theta(0)$ never matters). So $\int dk^0\,\delta(k^2 - m^2)\theta(-k^0)f(k) = f(-E_{\mathbf k}, \mathbf k)/2E_{\mathbf k}$; integrate over $\mathbf k$. Substituting $\mathbf k \to -\mathbf k$ (Jacobian 1, $E_{-\mathbf k} = E_{\mathbf k}$), this is $\int\frac{d^3k}{2E_{\mathbf k}}f(-k)\big|_{k^0 = E_{\mathbf k}}$: the upper-shell integral of $k \mapsto f(-k)$.
>
> **Step 3** (full shell). Without θ both roots contribute, each with weight $1/2E_{\mathbf k}$: the sum in the Answer. Equivalently $\delta(k^2 - m^2) = [\theta(k^0) + \theta(-k^0)]\,\delta(k^2 - m^2)$, the PS3.1(d) result plus Step 2.
>
> **Step 4** (invariance). Each lower-shell piece is invariant under proper orthochronous Λ (they preserve the sign of $k^0$ on timelike $k$). The full-shell measure is invariant under *every* Lorentz transformation, time reversal included: $|\det\Lambda| = 1$ and $k^2$ is a scalar, and no θ is left to be flipped. *Check:* for $f = 1$ near a fixed $\mathbf k$ the two weights are equal, $1/2E_{\mathbf k}$, as the symmetry $k^0 \to -k^0$ of $\delta(k^2 - m^2)$ requires.
>
> *Checked against:* [[§CA.2 Generalized Functions#^thm-ca-2-7|Theorem §CA.2.7]], 1 (the distributions $\theta(\pm p^0)\delta(p^2 - m^2)$, acting as $\varphi \mapsto \int d^3p\,\varphi(\pm E_{\mathbf p}, \mathbf p)/2E_{\mathbf p}$), [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]] (derivation, step 5, the upper sign) and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2.

^sol-px-3-1-2

### X3.2.1 · Ladder relations and charges of two-particle states
*[extension of PS3.2(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-2-1]]

> [!success]- Solution
> **Answer.** $[\hat Q, \hat a^\dagger_{\mathbf p}] = +\frac12\hat a^\dagger_{\mathbf p}$, $[\hat Q, \hat b^\dagger_{\mathbf p}] = -\frac12\hat b^\dagger_{\mathbf p}$; $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}|0\rangle$ has charge $0$, $(\hat a^\dagger_{\mathbf p})^2|0\rangle$ has charge $1$.
>
> **Step 1** (one number density). By $[AB, C] = A[B, C] + [A, C]B$ and $[\hat a^\dagger_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = 0$:
> $$
> [\hat a^\dagger_{\mathbf k}\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = \hat a^\dagger_{\mathbf k}[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = \hat a^\dagger_{\mathbf k}\,(2\pi)^3\delta^3(\mathbf k - \mathbf p) .
> $$
> The $\hat b$ density commutes with $\hat a^\dagger_{\mathbf p}$, since $[\hat b_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = [\hat b^\dagger_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = 0$.
>
> **Step 2** (integrate). $[\hat Q, \hat a^\dagger_{\mathbf p}] = \frac12\int\frac{d^3k}{(2\pi)^3}\hat a^\dagger_{\mathbf k}(2\pi)^3\delta^3(\mathbf k - \mathbf p) = \frac12\hat a^\dagger_{\mathbf p}$. In the same way $[\hat b^\dagger_{\mathbf k}\hat b_{\mathbf k}, \hat b^\dagger_{\mathbf p}] = \hat b^\dagger_{\mathbf k}(2\pi)^3\delta^3(\mathbf k - \mathbf p)$, and the minus sign in $\hat Q$ gives $[\hat Q, \hat b^\dagger_{\mathbf p}] = -\frac12\hat b^\dagger_{\mathbf p}$.
>
> **Step 3** (the vacuum). Every term of $\hat Q$ ends in an annihilator, so $\hat Q|0\rangle = 0$.
>
> **Step 4** (push $\hat Q$ to the right). $\hat Q\hat A^\dagger = \hat A^\dagger\hat Q + [\hat Q, \hat A^\dagger]$ at each creator:
> $$
> \hat Q\,\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}|0\rangle = \tfrac12\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}|0\rangle + \hat a^\dagger_{\mathbf p}\bigl(-\tfrac12\hat b^\dagger_{\mathbf q} + \hat b^\dagger_{\mathbf q}\hat Q\bigr)|0\rangle = \bigl(\tfrac12 - \tfrac12\bigr)\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}|0\rangle = 0 ,
> $$
> $$
> \hat Q\,(\hat a^\dagger_{\mathbf p})^2|0\rangle = \tfrac12(\hat a^\dagger_{\mathbf p})^2|0\rangle + \hat a^\dagger_{\mathbf p}\bigl(\tfrac12\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat Q\bigr)|0\rangle = 1\cdot(\hat a^\dagger_{\mathbf p})^2|0\rangle .
> $$
> A particle–antiparticle pair is neutral; two $a$-quanta carry twice the $a$-charge. In general $Q = \frac12(n_a - n_b)$.
>
> *Checked against:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]] (the ladder relations, derivation step 7) and [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]] ($Q = \frac12(n_a - n_b)$, derivation steps 2–3).

^sol-px-3-2-1

### X3.2.2 · The Noether charge against Q
*[variation of PS3.2(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-2-2]]

> [!success]- Solution
> **Answer.** $\displaystyle\int d^3x\,:\!\hat j^0\!: = \hat N_b - \hat N_a = -2\hat Q$. Physical: the ratio $-1$ of the two species' charges (and a neutral vacuum); the overall factor and sign are conventions (the sign of $\alpha$).
>
> **Step 1** (canonical form of $j^0$). With $\pi = \partial\mathcal L/\partial\dot\phi = \dot\phi^\ast$ and $\pi^\ast = \dot\phi$, $\partial^0 = \partial_t$:
> $$
> j^0 = i\bigl(\phi\,\dot\phi^\ast - \phi^\ast\dot\phi\bigr) = i\bigl(\phi\,\pi - \phi^\ast\pi^\ast\bigr) .
> $$
>
> **Step 2** (compare with $\hat Q$). $\hat Q = \frac i2\int d^3x\,:\!(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)\!:$. Inside the colons bosonic operators may be reordered freely ($:\!\hat\pi\hat\phi\!: = :\!\hat\phi\hat\pi\!:$), so
> $$
> :\!\hat j^0\!: = i\,:\!(\hat\phi\hat\pi - \hat\phi^\dagger\hat\pi^\dagger)\!: = -2\cdot\frac i2\,:\!(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)\!: \quad\Rightarrow\quad \int d^3x\,:\!\hat j^0\!: = -2\hat Q .
> $$
>
> **Step 3** (in modes). With $\hat Q = \frac12(\hat N_a - \hat N_b)$ (PS3.2(c)): $\int d^3x\,:\!\hat j^0\!: = \hat N_b - \hat N_a$. The $a$-quanta carry $-1$, the $b$-quanta $+1$.
>
> **Step 4** (sign check on one classical mode). For $\phi = Ae^{-iEt}$: $\dot\phi = -iE\phi$, $\dot\phi^\ast = iE\phi^\ast$, so $j^0 = i\bigl(iE|A|^2 - (-iE)|A|^2\bigr) = -2E|A|^2 < 0$. A positive-frequency ($a$-type) mode has negative Noether density, consistent with Step 3.
>
> **Step 5** (what is physical). The current comes from $\phi \to e^{i\alpha}\phi$; replacing $\alpha \to -\alpha$ flips $j^\mu$, and any constant multiple of a conserved current is conserved. Not fixed: the factor $-2$ between $\int:\!\hat j^0\!:$ and $\hat Q$. Fixed: the charges of $a$ and $b$ are opposite (ratio $-1$), both are conserved, and the vacuum is neutral after normal ordering. Lecture 3's slide writes the current with the opposite overall sign, which gives $\hat N_a - \hat N_b$.
>
> *Checked against:* [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]] (the current and "a positive-frequency solution has $j^0 < 0$"), [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]] ($\int:\!\hat j^0\!: = \hat N_b - \hat N_a$, $\hat Q = -\frac12\int:\!\hat j^0\!:$), [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]] ("$-\frac12$ times the Noether charge") and [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]].

^sol-px-3-2-2

### X3.3.1 · Klein–Gordon products of the modes
*[variation of PS3.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-3-1]]

> [!success]- Solution
> **Answer.** $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and $(f^\ast_{\mathbf p}, f_{\mathbf q}) = 0$ (and, for completeness, $(f^\ast_{\mathbf p}, f^\ast_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$).
>
> **Step 1** (time derivatives). $f_{\mathbf q} = e^{-iE_{\mathbf q}t + i\mathbf q\cdot\mathbf x}/\sqrt{2E_{\mathbf q}}$, so $\partial_0f_{\mathbf q} = -iE_{\mathbf q}f_{\mathbf q}$ and $\partial_0f^\ast_{\mathbf p} = +iE_{\mathbf p}f^\ast_{\mathbf p}$.
>
> **Step 2** (positive with positive). 
> $$
> (f_{\mathbf p}, f_{\mathbf q}) = i\int d^3x\,\bigl(f^\ast_{\mathbf p}(-iE_{\mathbf q})f_{\mathbf q} - (iE_{\mathbf p})f^\ast_{\mathbf p}f_{\mathbf q}\bigr) = \frac{E_{\mathbf p} + E_{\mathbf q}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\,e^{i(E_{\mathbf p} - E_{\mathbf q})t}\int d^3x\,e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x} .
> $$
> The $\mathbf x$ integral is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ (an identity of distributions). On its support $E_{\mathbf q} = E_{\mathbf p}$, so the prefactor is $\frac{2E_{\mathbf p}}{2E_{\mathbf p}} = 1$ and the phase is $1$: $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ at every $t$.
>
> **Step 3** (negative with positive). The first slot is $f^\ast_{\mathbf p}$, whose conjugate is $f_{\mathbf p}$, with $\partial_0f_{\mathbf p} = -iE_{\mathbf p}f_{\mathbf p}$:
> $$
> (f^\ast_{\mathbf p}, f_{\mathbf q}) = i\int d^3x\,\bigl(f_{\mathbf p}(-iE_{\mathbf q})f_{\mathbf q} - (-iE_{\mathbf p})f_{\mathbf p}f_{\mathbf q}\bigr) = \frac{E_{\mathbf q} - E_{\mathbf p}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\,e^{-i(E_{\mathbf p} + E_{\mathbf q})t}\,(2\pi)^3\delta^3(\mathbf p + \mathbf q) .
> $$
> On the support $\mathbf q = -\mathbf p$, $E_{\mathbf q} = E_{\mathbf p}$: the prefactor vanishes, and a smooth function vanishing on the support of a δ times that δ is zero. The oscillating phase $e^{-2iE_{\mathbf p}t}$ is harmless only because its coefficient is zero.
>
> **Step 4** (check by conjugation). $(f^\ast, g^\ast) = -(f, g)^\ast$ gives $(f^\ast_{\mathbf p}, f_{\mathbf q}) = -(f_{\mathbf p}, f^\ast_{\mathbf q})^\ast$, and the vault's $(f_{\mathbf p}, f^\ast_{\mathbf q}) = 0$ agrees with Step 3. The product is indefinite: $+$ on positive frequencies, $-$ on negative ones, $0$ across.
>
> *Checked against:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]] (derivation steps 6–10, the same computations with the conjugate slot) and [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]].

^sol-px-3-3-1

### X3.3.2 · Extracting a and b from the complex field
*[variation of PS3.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-3-2]]

> [!success]- Solution
> **Answer.** $\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi)$, $\hat b_{\mathbf p} = (f_{\mathbf p}, \hat\phi^\dagger)$; equivalently $\hat b^\dagger_{\mathbf p} = -(f^\ast_{\mathbf p}, \hat\phi)$, $\hat a^\dagger_{\mathbf p} = -(f^\ast_{\mathbf p}, \hat\phi^\dagger)$. Explicitly, with $\partial_t\hat\phi = \hat\pi^\dagger$ and $\partial_t\hat\phi^\dagger = \hat\pi$:
> $$
> \hat a_{\mathbf p} = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\bigl(\hat\pi^\dagger - iE_{\mathbf p}\hat\phi\bigr), \qquad \hat b_{\mathbf p} = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\bigl(\hat\pi - iE_{\mathbf p}\hat\phi^\dagger\bigr) .
> $$
>
> **Step 1** (write the field in modes). $\hat\phi = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}f_{\mathbf q} + \hat b^\dagger_{\mathbf q}f^\ast_{\mathbf q}\bigr)$ and, taking the adjoint term by term, $\hat\phi^\dagger = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat b_{\mathbf q}f_{\mathbf q} + \hat a^\dagger_{\mathbf q}f^\ast_{\mathbf q}\bigr)$.
>
> **Step 2** (project with $f_{\mathbf p}$). The product is linear in its second slot and the operators are $x$-independent, so
> $$
> (f_{\mathbf p}, \hat\phi) = \int\frac{d^3q}{(2\pi)^3}\Bigl(\hat a_{\mathbf q}(f_{\mathbf p}, f_{\mathbf q}) + \hat b^\dagger_{\mathbf q}(f_{\mathbf p}, f^\ast_{\mathbf q})\Bigr) = \int\frac{d^3q}{(2\pi)^3}\hat a_{\mathbf q}(2\pi)^3\delta^3(\mathbf p - \mathbf q) = \hat a_{\mathbf p} ,
> $$
> by X3.3.1. The same with $\hat\phi^\dagger$ gives $(f_{\mathbf p}, \hat\phi^\dagger) = \hat b_{\mathbf p}$.
>
> **Step 3** (project with $f^\ast_{\mathbf p}$). $(f^\ast_{\mathbf p}, \hat\phi) = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}\cdot0 + \hat b^\dagger_{\mathbf q}\cdot(-(2\pi)^3\delta^3(\mathbf p - \mathbf q))\bigr) = -\hat b^\dagger_{\mathbf p}$: the negative norm of negative-frequency modes gives the minus sign.
>
> **Step 4** (explicit form). With $f^\ast_{\mathbf p} = e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $\partial_tf^\ast_{\mathbf p} = iE_{\mathbf p}f^\ast_{\mathbf p}$: $(f_{\mathbf p}, \hat\phi) = i\int d^3x\,f^\ast_{\mathbf p}\bigl(\partial_t\hat\phi - iE_{\mathbf p}\hat\phi\bigr)$, and $\partial_t\hat\phi = \hat\pi^\dagger$ (the crossover: $\hat\pi = \dot{\hat\phi}^\dagger$ is conjugate to $\hat\phi$). Likewise for $\hat b_{\mathbf p}$ with $\partial_t\hat\phi^\dagger = \hat\pi$. Both are independent of the slice $t$ (conservation of the product).
>
> **Step 5** (consistency). For any operator $\hat A$, $(f, \hat A)^\dagger = -i\int d^3x\,(f\,\partial_t\hat A^\dagger - (\partial_tf)\hat A^\dagger) = -(f^\ast, \hat A^\dagger)$. So $\hat a^\dagger_{\mathbf p} = (f_{\mathbf p}, \hat\phi)^\dagger = -(f^\ast_{\mathbf p}, \hat\phi^\dagger)$, matching Step 3 applied to $\hat\phi^\dagger$.
>
> *Checked against:* [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]] (states $\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi)$, $\hat b_{\mathbf p} = (f_{\mathbf p}, \hat\phi^\dagger)$) and the real-field case [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]] ($\hat a^\dagger_{\mathbf p} = -(f^\ast_{\mathbf p}, \hat\phi)$, with $\hat b = \hat a$).

^sol-px-3-3-2

### X3.3.3 · Extracting a from the Dirac field
*[variation of PS3.3(b), Dirac field]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-3-3]]

> [!success]- Solution
> **Answer.** The identity holds at every $t$; it needs $u^{s\dagger}(p)u^r(p) = 2E_{\mathbf p}\delta^{rs}$ and $u^{s\dagger}(p)v^r(\tilde p) = 0$, $\tilde p = (E_{\mathbf p}, -\mathbf p)$. (Here the product is the positive one, $\int d^3x\,\chi^\dagger\psi$, not the Klein–Gordon product.)
>
> **Step 1** (substitute, variable $\mathbf q$, label $r$).
> $$
> \int d^3x\,e^{ip\cdot x}u^{s\dagger}(p)\hat\psi(x) = \int d^3x\int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r\Bigl(u^{s\dagger}(p)u^r(q)\,\hat a^r_{\mathbf q}\,e^{i(p - q)\cdot x} + u^{s\dagger}(p)v^r(q)\,\hat b^{r\dagger}_{\mathbf q}\,e^{i(p + q)\cdot x}\Bigr) .
> $$
>
> **Step 2** (the $\mathbf x$ integrals). $e^{i(p\mp q)\cdot x} = e^{i(E_{\mathbf p}\mp E_{\mathbf q})t}e^{-i(\mathbf p\mp\mathbf q)\cdot\mathbf x}$ and $\int d^3x\,e^{-i(\mathbf p\mp\mathbf q)\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p\mp\mathbf q)$.
>
> **Step 3** (the $\mathbf q$ integrals). First term: $\mathbf q = \mathbf p$, $q = p$, phase $e^{0} = 1$. Second term: $\mathbf q = -\mathbf p$, so $q = (E_{\mathbf p}, -\mathbf p) = \tilde p$, phase $e^{2iE_{\mathbf p}t}$:
> $$
> \frac{1}{\sqrt{2E_{\mathbf p}}}\sum_r\Bigl(u^{s\dagger}(p)u^r(p)\,\hat a^r_{\mathbf p} + u^{s\dagger}(p)v^r(\tilde p)\,\hat b^{r\dagger}_{-\mathbf p}\,e^{2iE_{\mathbf p}t}\Bigr) .
> $$
>
> **Step 4** (spinor identities). $u^{s\dagger}(p)u^r(p) = 2E_{\mathbf p}\delta^{rs}$ collapses the first sum to $2E_{\mathbf p}\hat a^s_{\mathbf p}$. $u^{s\dagger}(p)v^r(\tilde p) = 0$ removes the $\hat b^\dagger$ term together with its time dependence ($u(p)$ and $v(\tilde p)$ are eigenvectors of the Hermitian $H_{\text{s.p.}}(\mathbf p)$ with eigenvalues $+E_{\mathbf p}$ and $-E_{\mathbf p}$). Note it is the orthogonality at *opposite* three-momenta that is needed; at equal momenta $u^{r\dagger}(p)v^s(p) \ne 0$ in general.
>
> **Step 5** (conclude). The left side equals $\frac{2E_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\hat a^s_{\mathbf p} = \sqrt{2E_{\mathbf p}}\,\hat a^s_{\mathbf p}$; multiplying by $1/\sqrt{2E_{\mathbf p}}$ gives the claim, with no $t$ left. By the same steps, $\hat b^{s\dagger}_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{-ip\cdot x}v^{s\dagger}(p)\hat\psi(x)$, using $v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ and $v^{s\dagger}(p)u^r(\tilde p) = 0$.
>
> *Checked against:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]] (statement and derivation steps 1–6), with [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]] and [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]; why the product is positive: [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-5|§C5b.2, Remark: A positive inner product]].

^sol-px-3-3-3

### X3.4.1 · The energy of a coherent state
*[extension of PS3.4(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-4-1]]

> [!success]- Solution
> **Answer.** $\displaystyle\langle\{\eta\}|\hat H|\{\eta\}\rangle = \int\frac{d^3k}{(2\pi)^3}\,E_{\mathbf k}\,\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}} = \frac12\int\frac{d^3k}{(2\pi)^3}\,|\eta_{\mathbf k}|^2$, the classical energy of the mean field $\bar\phi$.
>
> **Step 1** (eigenvalue rules). $\hat a_{\mathbf k}|\{\eta\}\rangle = \frac{\eta_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}|\{\eta\}\rangle$ (PS3.4(a)); its adjoint is $\langle\{\eta\}|\hat a^\dagger_{\mathbf k} = \frac{\eta^\ast_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\langle\{\eta\}|$; and $\langle\{\eta\}|\{\eta\}\rangle = 1$ (PS3.4(b)).
>
> **Step 2** (the given $\hat H$ is normal ordered). $\hat a^\dagger_{\mathbf k}$ stands left of $\hat a_{\mathbf k}$, so $\hat a_{\mathbf k}$ acts to the right and $\hat a^\dagger_{\mathbf k}$ to the left with no reordering:
> $$
> \langle\{\eta\}|\hat a^\dagger_{\mathbf k}\hat a_{\mathbf k}|\{\eta\}\rangle = \frac{\eta^\ast_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\frac{\eta_{\mathbf k}}{\sqrt{2E_{\mathbf k}}} = \frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}} .
> $$
>
> **Step 3** (integrate with weight $E_{\mathbf k}$). $\langle\hat H\rangle = \int\frac{d^3k}{(2\pi)^3}E_{\mathbf k}\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}} = \frac12\int\frac{d^3k}{(2\pi)^3}|\eta_{\mathbf k}|^2$. It is finite when $\int|\eta_{\mathbf k}|^2 < \infty$, a stronger condition at large $\mathbf k$ than $\bar N < \infty$ (extra factor $E_{\mathbf k}$).
>
> **Step 4** (sanity checks). (i) It is $\int\frac{d^3k}{(2\pi)^3}E_{\mathbf k}\,n_{\mathbf k}$ with the mean occupation density $n_{\mathbf k} = |\eta_{\mathbf k}|^2/2E_{\mathbf k}$ of PS3.4(d): energy per quantum times the number of quanta, mode by mode. (ii) The mean field $\bar\phi$ has classical amplitudes $a_{\mathbf k} = \eta_{\mathbf k}/\sqrt{2E_{\mathbf k}}$, and the classical $H$ in modes is $\int\frac{d^3k}{(2\pi)^3}E_{\mathbf k}|a_{\mathbf k}|^2$, the same number: the coherent state's energy is the classical field energy. (iii) One mode: $\hbar\omega|\alpha|^2$, the QM result $\hbar\omega(|\alpha|^2 + \frac12)$ without the zero-point $\frac12\hbar\omega$, removed here by normal ordering. (iv) $\eta$ evolves as $\eta_{\mathbf k}e^{-iE_{\mathbf k}t}$, so $\langle\hat H\rangle$ is constant.
>
> *Derived here; check:* the method is [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]], derivation step 1 (the mean of $\hat N$), with the weight $E_{\mathbf k}$ inserted; $\hat H$ is $:\!\hat H\!:$ of [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]; eigenvalue rule [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]]; single-mode limit against QM [[§B4.3 Coherent States#^thm-b4-3-2|QM Theorem §B4.3.2]]; conservation against [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5|Theorem §C2a.6.5]].

^sol-px-3-4-1

### X3.4.2 · The mean momentum field
*[variation of PS3.4(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-4-2]]

> [!success]- Solution
> **Answer.** $\displaystyle\bar\pi(x) = -\frac i2\int\frac{d^3p}{(2\pi)^3}\Bigl(\eta_{\mathbf p}e^{-ip\cdot x} - \eta^\ast_{\mathbf p}e^{ip\cdot x}\Bigr)\Big|_{p^0 = E_{\mathbf p}} = \partial_t\bar\phi(x)$.
>
> **Step 1** (mode expansion of $\hat\pi$). Differentiating the Heisenberg field, $\partial_te^{\mp ip\cdot x} = \mp iE_{\mathbf p}e^{\mp ip\cdot x}$:
> $$
> \hat\pi(x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\Bigl(\hat a_{\mathbf p}e^{-ip\cdot x} - \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\Bigr) .
> $$
>
> **Step 2** (expectation value). $\hat a_{\mathbf p}$ acts to the right ($\eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$), $\hat a^\dagger_{\mathbf p}$ to the left ($\eta^\ast_{\mathbf p}/\sqrt{2E_{\mathbf p}}$), the norm is $1$; the factors combine as $\sqrt{E_{\mathbf p}/2}\cdot1/\sqrt{2E_{\mathbf p}} = \frac12$:
> $$
> \bar\pi(x) = \int\frac{d^3p}{(2\pi)^3}\Bigl(-\frac i2\Bigr)\Bigl(\eta_{\mathbf p}e^{-ip\cdot x} - \eta^\ast_{\mathbf p}e^{ip\cdot x}\Bigr) .
> $$
>
> **Step 3** (compare with $\partial_t\bar\phi$). From $\bar\phi = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\bigl(\eta_{\mathbf p}e^{-ip\cdot x} + \eta^\ast_{\mathbf p}e^{ip\cdot x}\bigr)$ (PS3.4(c)):
> $$
> \partial_t\bar\phi = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\Bigl(-iE_{\mathbf p}\eta_{\mathbf p}e^{-ip\cdot x} + iE_{\mathbf p}\eta^\ast_{\mathbf p}e^{ip\cdot x}\Bigr) = -\frac i2\int\frac{d^3p}{(2\pi)^3}\Bigl(\eta_{\mathbf p}e^{-ip\cdot x} - \eta^\ast_{\mathbf p}e^{ip\cdot x}\Bigr) = \bar\pi .
> $$
> (Differentiation under the integral is fine when $E_{\mathbf p}|\eta_{\mathbf p}|$ is integrable; otherwise read both sides smeared.)
>
> **Step 4** (reading). $\bar\pi$ is real (the second term is the conjugate of the first), and $\bar\pi = \partial_t\bar\phi$ is the classical relation $\pi = \dot\phi$: Ehrenfest's theorem, exact for a free field. *Check at one mode:* $\eta_{\mathbf p} = \eta\,(2\pi)^3\delta^3(\mathbf p - \mathbf k)$ with $\eta$ real gives $\bar\phi = \frac{\eta}{E_{\mathbf k}}\cos(k\cdot x)$, $\bar\pi = -\eta\sin(k\cdot x)$, and $\partial_t\bar\phi = -\eta\sin(k\cdot x)$.
>
> *Derived here; check:* the same computation as [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4|Theorem §C2a.6.4]] (derivation steps 1–3) with the $\hat\pi$ expansion of [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] in place of $\hat\phi$; eigenvalue rule [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2|Theorem §C2a.6.2]].

^sol-px-3-4-2

### X3.4.3 · One mode: the Poisson distribution
*[extension of PS3.4(e)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-3-4-3]]

> [!success]- Solution
> **Answer.** $P(n) = e^{-|\alpha|^2}\dfrac{|\alpha|^{2n}}{n!}$ (Poisson), mean $\bar n = |\alpha|^2$, variance $\langle(\Delta\hat N)^2\rangle = |\alpha|^2$: (d) and (e) with $\bar N \to |\alpha|^2$.
>
> **Step 1** (expand). $(\hat a^\dagger)^n|0\rangle = \sqrt{n!}\,|n\rangle$ with $|n\rangle$ orthonormal, so
> $$
> |\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n\ge0}\frac{\alpha^n}{n!}(\hat a^\dagger)^n|0\rangle = e^{-|\alpha|^2/2}\sum_{n\ge0}\frac{\alpha^n}{\sqrt{n!}}|n\rangle .
> $$
>
> **Step 2** (probabilities). $P(n) = |\langle n|\alpha\rangle|^2 = e^{-|\alpha|^2}|\alpha|^{2n}/n!$; $\sum_nP(n) = e^{-|\alpha|^2}e^{|\alpha|^2} = 1$, confirming the normalisation $e^{-|\alpha|^2/2}$ of PS3.4(b).
>
> **Step 3** (mean). $\sum_n nP(n) = e^{-|\alpha|^2}\sum_{n\ge1}\frac{|\alpha|^{2n}}{(n-1)!} = |\alpha|^2e^{-|\alpha|^2}\sum_{m\ge0}\frac{|\alpha|^{2m}}{m!} = |\alpha|^2$.
>
> **Step 4** (variance). $\sum_nn(n-1)P(n) = |\alpha|^4$ by the same shift by two, so $\langle\hat N^2\rangle = |\alpha|^4 + |\alpha|^2$ and $\langle(\Delta\hat N)^2\rangle = |\alpha|^4 + |\alpha|^2 - |\alpha|^4 = |\alpha|^2$.
>
> **Step 5** (compare with (d)–(e)). The field state is a coherent state of one packet mode $\hat c$ with $\alpha = \sqrt{\bar N}$, $\bar N = \int\frac{d^3k}{(2\pi)^3}\frac{|\eta_{\mathbf k}|^2}{2E_{\mathbf k}}$; (d) gave $\bar N$ and (e) gave $\langle(\Delta\hat N)^2\rangle = \bar N$, both reproduced. The relative spread $1/|\alpha|$ is small iff $|\alpha|^2 \gg 1$: the classical condition of (e). Operator check: $\hat a|\alpha\rangle = \alpha|\alpha\rangle$ gives $\langle\hat a^\dagger\hat a\rangle = |\alpha|^2$ and $\langle\hat a^\dagger\hat a\hat a^\dagger\hat a\rangle = \langle\hat a^{\dagger2}\hat a^2\rangle + \langle\hat a^\dagger\hat a\rangle = |\alpha|^4 + |\alpha|^2$.
>
> *Checked against:* [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6|Theorem §C2a.6.6]] (Poisson statistics; derivation steps 4–5 reduce the field to one packet mode) and QM [[§B4.3 Coherent States#^thm-b4-3-2|QM Theorem §B4.3.2]] ($P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$, mean and variance $|\alpha|^2$).

^sol-px-3-4-3

### X6.1.1 · The ordering constants of P and H
*[extension of PS6.1]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-1-1]]

> [!success]- Solution
> **Answer.** $\hat{\mathbf P} - :\!\hat{\mathbf P}\!: = \frac12\delta^3(\mathbf 0)\int d^3p\,\mathbf p = \frac V2\int\frac{d^3p}{(2\pi)^3}\,\mathbf p = 0$; $\hat H - :\!\hat H\!: = E_0 = \frac12\delta^3(\mathbf 0)\int d^3p\,E_{\mathbf p} = \frac V2\int\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p} > 0$, divergent. $\mathbf p$ is odd under $\mathbf p \to -\mathbf p$, $E_{\mathbf p}$ is even and positive.
>
> **Step 1** (both before ordering). Substituting the modes at $t = 0$ and doing the $\mathbf x$ integral (PS6.1 for $\hat{\mathbf P}$; the same for $\hat H$), and removing the $\hat a\hat a$, $\hat a^\dagger\hat a^\dagger$ terms (for $\hat{\mathbf P}$ by oddness, for $\hat H$ because their coefficient $\frac14(\mathbf p^2 + m^2 - E_{\mathbf p}^2)/E_{\mathbf p}$ vanishes on the shell):
> $$
> \hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\,\frac{\mathbf p}{2}\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\bigr), \qquad \hat H = \int\frac{d^3p}{(2\pi)^3}\,\frac{E_{\mathbf p}}{2}\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\bigr) .
> $$
>
> **Step 2** (reorder). $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$, so each operator is its normal-ordered form plus
> $$
> \mathbf c_P = \int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}{2}(2\pi)^3\delta^3(\mathbf 0) = \frac V2\int\frac{d^3p}{(2\pi)^3}\mathbf p, \qquad c_H = \frac V2\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p} ,
> $$
> with $(2\pi)^3\delta^3(\mathbf 0) = \int d^3x = V$ in a box (the δ at its singular point has no value; the box gives it one).
>
> **Step 3** (why $\mathbf c_P = 0$). In the box the momenta form a lattice symmetric under $\mathbf k \to -\mathbf k$, and a rotation-invariant cutoff $|\mathbf k| < \Lambda$ keeps that symmetry; $\mathbf c_P = \frac12\sum_{|\mathbf k|<\Lambda}\mathbf k$ vanishes term by term ($\mathbf k$ against $-\mathbf k$). Physically: $\langle0|\hat{\mathbf P}|0\rangle$ is a vector, and a rotation-invariant vacuum has none to point along.
>
> **Step 4** (why $c_H \ne 0$). $c_H = \frac12\sum_{|\mathbf k|<\Lambda}E_{\mathbf k}$ is a sum of positive terms, $\frac12E$ per mode (the oscillator ground state $\frac12\omega$): no cancellation. It diverges with $V$ (infrared) and, per volume, as $\Lambda^4/16\pi^2$ (ultraviolet). It is a c-number, so it drops out of every commutator and energy difference.
>
> *Checked against:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]] (derivation step 7: the constant $\frac V2\int\frac{d^3p}{(2\pi)^3}\mathbf p$, zero for a rotation-invariant cutoff) and [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]] ($E_0 = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$, $V = (2\pi)^3\delta^3(\mathbf 0)$); [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]]; the user's PHY 513 Problem Set 6, Problem 1, closing remark, as written.

^sol-px-6-1-1

### X6.1.2 · The Dirac momentum in modes
*[variation of PS6.1, Dirac field]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-1-2]]

> [!success]- Solution
> **Answer.** $\hat{\mathbf P} = \sum_s\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr)$: the antifermion of label $\mathbf p$ carries momentum $+\mathbf p$.
>
> **Step 1** ($-i\nabla$ on the modes). $\pm q\cdot x$ contains $\mp\mathbf q\cdot\mathbf x$, so $-i\nabla e^{-iq\cdot x} = \mathbf q\,e^{-iq\cdot x}$ and $-i\nabla e^{iq\cdot x} = -\mathbf q\,e^{iq\cdot x}$:
> $$
> (-i\nabla)\hat\psi = \int\frac{d^3q}{(2\pi)^3}\frac{\mathbf q}{\sqrt{2E_{\mathbf q}}}\sum_r\Bigl(\hat a^r_{\mathbf q}u^r(q)e^{-iq\cdot x} - \hat b^{r\dagger}_{\mathbf q}v^r(q)e^{iq\cdot x}\Bigr) .
> $$
>
> **Step 2** (multiply by $\hat\psi^\dagger$, all four terms, order kept). With $\hat\psi^\dagger = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p}u^{s\dagger}(p)e^{ip\cdot x} + \hat b^s_{\mathbf p}v^{s\dagger}(p)e^{-ip\cdot x}\bigr)$:
> $$
> \hat\psi^\dagger(-i\nabla)\hat\psi \ni \frac{\mathbf q}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\Bigl[u^{s\dagger}(p)u^r(q)\hat a^{s\dagger}_{\mathbf p}\hat a^r_{\mathbf q}e^{i(p-q)\cdot x} - u^{s\dagger}(p)v^r(q)\hat a^{s\dagger}_{\mathbf p}\hat b^{r\dagger}_{\mathbf q}e^{i(p+q)\cdot x} + v^{s\dagger}(p)u^r(q)\hat b^s_{\mathbf p}\hat a^r_{\mathbf q}e^{-i(p+q)\cdot x} - v^{s\dagger}(p)v^r(q)\hat b^s_{\mathbf p}\hat b^{r\dagger}_{\mathbf q}e^{-i(p-q)\cdot x}\Bigr] .
> $$
>
> **Step 3** ($\mathbf x$ and $\mathbf q$ integrals). The $p - q$ terms give $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$: $\mathbf q = \mathbf p$, phase $1$, prefactor $\mathbf p/2E_{\mathbf p}$. The $p + q$ terms give $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$: $\mathbf q = -\mathbf p$, $q = \tilde p$, phases $e^{\pm2iE_{\mathbf p}t}$.
>
> **Step 4** (spinor products). Cross terms: $u^{s\dagger}(p)v^r(\tilde p) = v^{s\dagger}(p)u^r(\tilde p) = 0$, so the number-changing terms vanish with their time dependence. Diagonal terms: $u^{s\dagger}(p)u^r(p) = v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$, and $\frac{\mathbf p}{2E_{\mathbf p}}2E_{\mathbf p} = \mathbf p$:
> $$
> \hat{\mathbf P}_{\text{unordered}} = \sum_s\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\bigr) .
> $$
>
> **Step 5** (fermionic normal ordering). $:\!\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\!: = -\hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}$ (one exchange, one sign), so $-:\!\hat b\hat b^\dagger\!: = +\hat b^\dagger\hat b$: the Answer. The minus sign of the $v$ term (the $-\mathbf q$ of Step 1, the same relative sign as the $-E$ in $\hat H$) is cancelled by the fermion sign. Without colons the anticommutator gives instead the constant $-2V\int\frac{d^3p}{(2\pi)^3}\mathbf p$, zero by oddness as in X6.1.1.
>
> *Checked against:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]] (statement and derivation steps 1–3), with [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]; the same layout as the user's PHY 513 Problem Set 6, Problem 2 (charge), as written.

^sol-px-6-1-2

### X6.2.1 · Charges of the Dirac quanta
*[extension of PS6.2]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-2-1]]

> [!success]- Solution
> **Answer.** $[\hat Q, \hat a^{s\dagger}_{\mathbf p}] = +\hat a^{s\dagger}_{\mathbf p}$, $[\hat Q, \hat b^{s\dagger}_{\mathbf p}] = -\hat b^{s\dagger}_{\mathbf p}$: fermions carry charge $+1$, antifermions $-1$.
>
> **Step 1** (the mixed identity). For any operators, $A\{B, C\} - \{A, C\}B = ABC + ACB - ACB - CAB = [AB, C]$. A bilinear commutes like a bosonic operator, so the commutator is the right bracket even though the modes anticommute.
>
> **Step 2** ($a$-density with $\hat a^\dagger$). $A = \hat a^{r\dagger}_{\mathbf q}$, $B = \hat a^r_{\mathbf q}$, $C = \hat a^{s\dagger}_{\mathbf p}$:
> $$
> [\hat a^{r\dagger}_{\mathbf q}\hat a^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}] = \hat a^{r\dagger}_{\mathbf q}(2\pi)^3\delta^3(\mathbf q - \mathbf p)\delta^{rs} - \{\hat a^{r\dagger}_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\}\hat a^r_{\mathbf q} = \hat a^{r\dagger}_{\mathbf q}(2\pi)^3\delta^3(\mathbf q - \mathbf p)\delta^{rs} .
> $$
> The $b$-density gives $\hat b^{r\dagger}_{\mathbf q}\{\hat b^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\} - \{\hat b^{r\dagger}_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\}\hat b^r_{\mathbf q} = 0$ (different species anticommute). Integrating $\int\frac{d^3q}{(2\pi)^3}\sum_r$: $[\hat Q, \hat a^{s\dagger}_{\mathbf p}] = \hat a^{s\dagger}_{\mathbf p}$.
>
> **Step 3** ($b$-density with $\hat b^\dagger$). In the same way $[\hat b^{r\dagger}_{\mathbf q}\hat b^r_{\mathbf q}, \hat b^{s\dagger}_{\mathbf p}] = \hat b^{r\dagger}_{\mathbf q}(2\pi)^3\delta^3(\mathbf q - \mathbf p)\delta^{rs}$, the $a$-density contributes $0$, and the minus sign in $\hat Q$ gives $[\hat Q, \hat b^{s\dagger}_{\mathbf p}] = -\hat b^{s\dagger}_{\mathbf p}$.
>
> **Step 4** (states). $\hat Q|0\rangle = 0$ (every term ends in an annihilator), so $\hat Q\,\hat a^{s\dagger}_{\mathbf p}|0\rangle = [\hat Q, \hat a^{s\dagger}_{\mathbf p}]|0\rangle = +\hat a^{s\dagger}_{\mathbf p}|0\rangle$ and $\hat Q\,\hat b^{s\dagger}_{\mathbf p}|0\rangle = -\hat b^{s\dagger}_{\mathbf p}|0\rangle$. *Why not the anticommutator:* with $\{AB, C\} = A\{B, C\} - [A, C]B$ and $[\hat a^{r\dagger}_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}] = 2\hat a^{r\dagger}_{\mathbf q}\hat a^{s\dagger}_{\mathbf p}$ (they anticommute), one finds $\{\hat Q, \hat a^{s\dagger}_{\mathbf p}\} = \hat a^{s\dagger}_{\mathbf p}(1 + 2\hat Q)$, which depends on the state it acts on; only the commutator is a ladder relation.
>
> *Checked against:* [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]] (the four relations) and [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]] (the identity $[AB, C] = A\{B, C\} - \{A, C\}B$ and derivation step 2, with weight $\pm1$ in place of $E_{\mathbf q}$).

^sol-px-6-2-1

### X6.2.2 · The Dirac Hamiltonian in modes
*[variation of PS6.2]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-2-2]]

> [!success]- Solution
> **Answer.** $:\!\hat H\!: = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr)$. The antiparticle term is positive because two signs multiply: $-E_{\mathbf p}$ from $H_{\text{s.p.}}$ on the $v$ modes, and $-1$ from moving $\hat b^\dagger$ past $\hat b$ (fermionic normal ordering).
>
> **Step 1** ($H_{\text{s.p.}}$ on the modes). On $e^{i\mathbf k\cdot\mathbf x}$, $H_{\text{s.p.}} = \gamma^0(-i\boldsymbol\gamma\cdot\nabla + m)$ acts as $H_{\text{s.p.}}(\mathbf k)$. The $u$ term of $\hat\psi$ has $\mathbf k = \mathbf q$: $H_{\text{s.p.}}(\mathbf q)u^r(q) = E_{\mathbf q}u^r(q)$. The $v$ term, $v^r(q)e^{iq\cdot x}$, has $\mathbf k = -\mathbf q$, and $H_{\text{s.p.}}(-\mathbf q)v^r(q) = -E_{\mathbf q}v^r(q)$ (the given relation with $\mathbf p \to -\mathbf q$, $\tilde p \to q$). So
> $$
> H_{\text{s.p.}}\hat\psi = \int\frac{d^3q}{(2\pi)^3}\frac{E_{\mathbf q}}{\sqrt{2E_{\mathbf q}}}\sum_r\Bigl(\hat a^r_{\mathbf q}u^r(q)e^{-iq\cdot x} - \hat b^{r\dagger}_{\mathbf q}v^r(q)e^{iq\cdot x}\Bigr) .
> $$
> This is Step 1 of X6.1.2 with $\mathbf q \to E_{\mathbf q}$.
>
> **Step 2** (multiply, integrate). Exactly Steps 2–4 of X6.1.2 with weight $E_{\mathbf q}$: the $\mathbf x$ integral gives $\delta^3(\mathbf p \mp \mathbf q)$; the cross terms carry $u^{s\dagger}(p)v^r(\tilde p) = v^{s\dagger}(p)u^r(\tilde p) = 0$ and vanish; the diagonal terms have prefactor $\frac{E_{\mathbf p}}{2E_{\mathbf p}}\cdot2E_{\mathbf p}\delta^{rs} = E_{\mathbf p}\delta^{rs}$:
> $$
> \hat H_{\text{unordered}} = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\bigr) ,
> $$
> time independent, with no algebra used yet.
>
> **Step 3** (normal order). $:\!\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\!: = -\hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}$, so $-E_{\mathbf p}:\!\hat b\hat b^\dagger\!: = +E_{\mathbf p}\hat b^\dagger\hat b$: the Answer. Without colons the anticommutator gives $-\hat b\hat b^\dagger = \hat b^\dagger\hat b - (2\pi)^3\delta^3(\mathbf 0)$ and the negative constant $E_0^{(\mathrm D)} = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}$.
>
> **Step 4** (where the sign comes from). First minus: the $v$ modes are the $-E_{\mathbf p}$ eigenvectors of $H_{\text{s.p.}}$ (wave-function aspect). Second minus: the anticommutator, $\hat b\hat b^\dagger = -\hat b^\dagger\hat b + \{\hat b, \hat b^\dagger\}$ (operator aspect). Had $\hat b$ been quantized with commutators, $-\hat b\hat b^\dagger = -\hat b^\dagger\hat b - (2\pi)^3\delta^3(\mathbf 0)$ and the antiparticle energies would stay negative: positivity of the energy requires Fermi statistics. Each quantum then adds $+E_{\mathbf p}$, and $:\!\hat H\!: \ge 0$.
>
> *Checked against:* [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]] (the unordered form and its derivation), [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]] (the eigenvalues $\pm E_{\mathbf p}$) and [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-1|§C5b.3, Remark: Two minus signs make a plus]].

^sol-px-6-2-2

## D. Two-point functions, Green's functions, contours

### X4.0.1 · Retarded minus advanced is homogeneous
*[extension of PS4.0]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-0-1]]

> [!success]- Solution
> **Answer.** $D_R - D_A = [\theta(\xi^0) + \theta(-\xi^0)]\,iD = iD$, and $(\partial^2 + m^2)\,iD = 0$: the difference of two Green's functions is a solution of the homogeneous equation, as it must be.
>
> **Step 1** (the difference). $D_R - D_A = \theta(\xi^0)iD - (-\theta(-\xi^0)iD) = [\theta(\xi^0) + \theta(-\xi^0)]\,iD$. The bracket is $1$ for $\xi^0 \ne 0$. On the slice $\xi^0 = 0$ (where it would be $2$ with $\theta(0) = 1$) nothing is lost: $D(0, \boldsymbol\xi) = 0$ (Cauchy data of $D$), and the products $\theta(\pm\xi^0)\,iD$ are defined slice by slice, so the value of $\theta(0)$ never enters. Hence $D_R - D_A = iD$.
>
> **Step 2** ($iD$ is homogeneous). $iD(\xi) = \langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle = D_W(\xi) - D_W(-\xi)$. With $D_W(\xi) = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-ip\cdot\xi}$, $p^0 = E_{\mathbf p}$: $\partial^2e^{-ip\cdot\xi} = (-ip_\mu)(-ip^\mu)e^{-ip\cdot\xi} = -p^2e^{-ip\cdot\xi} = -m^2e^{-ip\cdot\xi}$, so $(\partial_x^2 + m^2)D_W(x - y) = 0$. For $D_W(y - x)$ as a function of $x$: $\partial_x = -\partial_\xi$ and $\partial^2$ is even, so it is homogeneous too. Hence $(\partial_x^2 + m^2)\,iD = 0$.
>
> **Step 3** (the same from the Green's-function equations). $(\partial^2 + m^2)D_R = -i\delta^4$ and $(\partial^2 + m^2)D_A = -i\delta^4$; subtracting, the δ's cancel: $(\partial^2 + m^2)(D_R - D_A) = 0$, consistent with Step 2. Conversely $D_A = D_R - iD$: adding any homogeneous solution to a Green's function gives another one, and the boundary condition (support in the future or the past) picks which.
>
> **Step 4** (check, one mode). Mode by mode $D_R \to \theta(t)(-i\sin E_{\mathbf p}t)/E_{\mathbf p}$ and $D_A \to \theta(-t)(i\sin E_{\mathbf p}t)/E_{\mathbf p}$; the difference is $-i\sin(E_{\mathbf p}t)/E_{\mathbf p}$ for all $t$, a solution of $\ddot f + E_{\mathbf p}^2f = 0$, with no kink at $t = 0$ (it vanishes there, and its derivative $-i$ is continuous). Each of $D_R$, $D_A$ alone has the same jump $-i$ in its first derivative at $t = 0$ ($D_R$: from $0$ to $-i$; $D_A$: from $+i$ to $0$), which is what produces $-i\delta(t)$ in $\ddot f + E_{\mathbf p}^2f$; the jumps cancel in the difference.
>
> *Checked against:* [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]] (both forms and the mode-by-mode forms), [[§C2b.2 The Wightman Function#^thm-c2b-2-4|Theorem §C2b.2.4]], 1, [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12|Theorem §C2b.4.12]] ($D(0, \boldsymbol\xi) = 0$), [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-7|Theorem §CA.6.7]], 1, and [[§C2b.5 Green's Functions and Contours#^rem-c2b-5-1|§C2b.5, Remark: What a Green's "function" is, and why it is not unique]].

^sol-px-4-0-1

### X4.1.1 · A double pole
*[variation of PS4.1(e)–(h)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-1-1]]

> [!success]- Solution
> **Answer.** $\displaystyle\int_{-\infty}^\infty\frac{dx}{(x^2 + a^2)^2} = \frac{\pi}{2a^3}$.
>
> **Step 1** (close). $f(z) = \frac{1}{(z - ia)^2(z + ia)^2}$ has double poles at $\pm ia$. On the upper semicircle of radius $R > a$, $|z^2 + a^2| \ge R^2 - a^2$, so $|f| \le (R^2 - a^2)^{-2}$ and the arc contributes at most $\pi R/(R^2 - a^2)^2 \to 0$ (ML). The closed contour, counterclockwise, encloses $ia$ only.
>
> **Step 2** (residue at a double pole). $\operatorname{Res}_{ia}f = \frac{d}{dz}\Bigl[(z - ia)^2f\Bigr]_{z = ia} = \frac{d}{dz}(z + ia)^{-2}\Big|_{ia} = -2(2ia)^{-3} = \frac{-2}{-8ia^3} = \frac{1}{4ia^3}$, using $(2ia)^3 = 8i^3a^3 = -8ia^3$.
>
> **Step 3** (residue theorem). $\int = 2\pi i\cdot\frac{1}{4ia^3} = \frac{\pi}{2a^3}$.
>
> **Step 4** (checks). (i) Differentiate the known Lorentzian integral in $a^2$: $\frac{1}{(x^2 + a^2)^2} = -\frac{\partial}{\partial(a^2)}\frac{1}{x^2 + a^2}$, so the integral is $-\frac{\partial}{\partial(a^2)}\frac{\pi}{(a^2)^{1/2}} = \frac\pi2(a^2)^{-3/2} = \frac{\pi}{2a^3}$. (ii) Closing downward, clockwise round $-ia$: $\operatorname{Res}_{-ia} = -2(-2ia)^{-3} = -\frac{1}{4ia^3}$, and $-2\pi i\cdot(-\frac{1}{4ia^3}) = \frac{\pi}{2a^3}$, the same. (iii) Dimension: $[x]^{-3}$, as $a^{-3}$.
>
> *Derived here; check:* the method of [[§CA.4 Contour Integration#^ex-ca-4-1|Example §CA.4.1]] (the simple-pole case, $\pi/a$, used in check (i)), with the order-$k$ residue formula of [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], 2, [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]] and the arc estimate [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], 1.

^sol-px-4-1-1

### X4.1.2 · The Lorentzian with a phase
*[variation of PS4.1(e)–(h)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-1-2]]

> [!success]- Solution
> **Answer.** $\displaystyle\int_{-\infty}^\infty dx\,\frac{e^{ikx}}{x^2 + m^2} = \frac\pi m\,e^{-m|k|}$. Close upward for $k > 0$, downward for $k < 0$ (either for $k = 0$): $|e^{ikz}| = e^{-k\operatorname{Im}z}$ must decay on the arc.
>
> **Step 1** (which half-plane). On $z = Re^{i\theta}$, $|e^{ikz}| = e^{-kR\sin\theta}$. For $k > 0$ this is $\le 1$ in the upper half-plane and the arc vanishes by Jordan's lemma ($g = 1/(z^2 + m^2) \to 0$ on the arc); in the lower half-plane it would blow up like $e^{|k|R|\sin\theta|}$. For $k < 0$ the roles swap. (Here even the ML estimate works, $g = O(R^{-2})$, since $|e^{ikz}| \le 1$ on the chosen arc.)
>
> **Step 2** ($k > 0$). Counterclockwise around $z = im$: $\operatorname{Res}_{im}\frac{e^{ikz}}{(z - im)(z + im)} = \frac{e^{ik(im)}}{2im} = \frac{e^{-km}}{2im}$. So the integral is $2\pi i\cdot\frac{e^{-km}}{2im} = \frac\pi me^{-km}$.
>
> **Step 3** ($k < 0$). Clockwise around $z = -im$: $\operatorname{Res}_{-im} = \frac{e^{ik(-im)}}{-2im} = \frac{e^{km}}{-2im}$, and $-2\pi i\cdot\frac{e^{km}}{-2im} = \frac\pi me^{km} = \frac\pi me^{-m|k|}$.
>
> **Step 4** (checks). At $k = 0$: $\pi/m$, the PS4.1 Lorentzian integral with $a = m$. The result is even in $k$, as it must be (the integrand's real part $\cos(kx)/(x^2 + m^2)$ is even in $k$, the imaginary part odd in $x$ and integrates to $0$). The kink at $k = 0$ is where the contour switches; it makes the result $2\pi$ times the one-dimensional Green's function of $-\partial_k^2 + m^2$: $(-\partial_k^2 + m^2)\frac\pi me^{-m|k|} = 2\pi\delta(k)$ (the kink gives $\partial_k^2e^{-m|k|} \ni -2m\delta(k)$), a Yukawa profile of range $1/m$.
>
> *Checked against:* [[§CA.4 Contour Integration#^ex-ca-4-1|Example §CA.4.1]] (the same integral with $a$ in place of $m$: $\frac\pi ae^{-a|k|}$) and [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], 2 (Jordan's lemma; "$e^{ikz}$ upward for $k > 0$, downward for $k < 0$").

^sol-px-4-1-2

### X4.1.3 · The iε as a principal value plus a delta
*[variation of PS4.2(b), eq. (11)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-1-3]]

> [!success]- Solution
> **Answer.** $\displaystyle\lim_{\varepsilon\to0^+}\int dx\,\frac{f(x)}{x - a + i\varepsilon} = \mathcal P\!\!\int dx\,\frac{f(x)}{x - a} - i\pi f(a)$, and $\displaystyle\operatorname{Im}\frac{1}{p^2 - m^2 + i\varepsilon} \to -\pi\,\delta(p^2 - m^2) = -\frac{\pi}{2E_{\mathbf p}}\bigl[\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})\bigr]$.
>
> **Step 1** (split at finite ε). With $s = x - a$: $\dfrac{1}{s + i\varepsilon} = \dfrac{s - i\varepsilon}{s^2 + \varepsilon^2} = \dfrac{s}{s^2 + \varepsilon^2} - i\dfrac{\varepsilon}{s^2 + \varepsilon^2}$.
>
> **Step 2** (imaginary part). Substitute $s = \varepsilon u$: $\int f(a + s)\frac{\varepsilon\,ds}{s^2 + \varepsilon^2} = \int f(a + \varepsilon u)\frac{du}{1 + u^2} \to f(a)\int\frac{du}{1 + u^2} = \pi f(a)$ (dominated convergence, $|f|$ bounded). So $\frac{\varepsilon}{s^2 + \varepsilon^2} \to \pi\delta(s)$, and this piece gives $-i\pi f(a)$.
>
> **Step 3** (real part). Subtract $f(a)$ on a symmetric interval $[-L, L]$ (the subtracted term $\int_{-L}^Lf(a)\frac{s\,ds}{s^2 + \varepsilon^2}$ vanishes by oddness): $\int_{-L}^L\frac{f(a + s) - f(a)}{s}\frac{s^2}{s^2 + \varepsilon^2}ds \to \int_{-L}^L\frac{f(a + s) - f(a)}{s}ds$, the difference quotient being bounded; the tails $|s| > L$ have no singularity and converge to $\int\frac{f}{s}$ directly. Together: $\mathcal P\!\int\frac{f(x)}{x - a}dx$. (Equivalently: keeping the path real with the pole at $a - i\varepsilon$ is passing *above* the pole, a clockwise half-circle giving $-i\pi f(a)$.)
>
> **Step 4** (the propagator denominator). At fixed $\mathbf p$ use $s = p^2 - m^2 = (p^0)^2 - E_{\mathbf p}^2$ in place of $x - a$: $\operatorname{Im}\frac{1}{s + i\varepsilon} = -\frac{\varepsilon}{s^2 + \varepsilon^2} \to -\pi\delta(s)$. Composing δ with $s(p^0)$, simple zeros $\pm E_{\mathbf p}$, $|ds/dp^0| = 2E_{\mathbf p}$: $\delta(p^2 - m^2) = \frac{\delta(p^0 - E_{\mathbf p}) + \delta(p^0 + E_{\mathbf p})}{2E_{\mathbf p}}$. So the imaginary part sits on both sheets of the mass shell, with the same sign; then $\frac{i}{p^2 - m^2 + i\varepsilon} \to i\mathcal P\frac{1}{p^2 - m^2} + \pi\delta(p^2 - m^2)$.
>
> **Step 5** (check). In PS4.2(b)'s form, $\frac{1}{s - i\varepsilon} = \mathcal P\frac1s + i\pi\delta(s)$: the conjugate of Step 1, as it must be.
>
> *Checked against:* [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]] (Sokhotski–Plemelj, $\frac{1}{x - x_0 + i\varepsilon} \to \mathcal P\frac{1}{x - x_0} - i\pi\delta(x - x_0)$, and its derivation steps 1–6), [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-6|Theorem §CA.6.6]], 1 (the propagator denominator), [[§CA.2 Generalized Functions#^def-ca-2-10|Def. §CA.2.10]] and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2.

^sol-px-4-1-3

### X4.2.1 · The massless retarded function
*[extension of PS4.2(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-2-1]]

> [!success]- Solution
> **Answer.** $D_R = -\dfrac{i}{2\pi}\theta(\xi^0)\,\delta(\xi^2) = -\dfrac{i}{4\pi r}\,\delta(t - r)$ for $t > 0$ (and $0$ for $t < 0$): supported on the forward light cone $t = r$ only, not inside it.
>
> **Step 1** (insert $D$). $D_R = \theta(\xi^0)\,iD = -\frac{i}{2\pi}\theta(\xi^0)\operatorname{sgn}(\xi^0)\,\delta(\xi^2) = -\frac{i}{2\pi}\theta(\xi^0)\,\delta(\xi^2)$, since $\theta\cdot\operatorname{sgn} = \theta$ for $\xi^0 \ne 0$ (the slice $\xi^0 = 0$ does not matter: $\delta(\xi^2)$ there would need $r = 0$, and the products are taken slice by slice).
>
> **Step 2** (compose the δ). At fixed $r > 0$, $\xi^2 = t^2 - r^2$ has the simple zeros $t = \pm r$ with $|\partial_t(t^2 - r^2)| = 2r$ at both: $\delta(t^2 - r^2) = \frac{\delta(t - r) + \delta(t + r)}{2r}$. For $t > 0$ only $t = r$ survives (for $r > 0$, $t + r > 0$):
> $$
> D_R = -\frac{i}{2\pi}\cdot\frac{\delta(t - r)}{2r} = -\frac{i}{4\pi r}\,\delta(t - r) .
> $$
>
> **Step 3** (support). $D_R \ne 0$ only on $t = r$, $t > 0$: the surface of the future cone (sharp propagation at the speed of light; Huygens' principle in $3 + 1$ dimensions). For $m > 0$ the commutator also has the tail $\frac{m}{4\pi\tau}J_1(m\tau)$ inside the cone, and $D_R$ is supported in the whole closed forward cone.
>
> **Step 4** (check: retarded potentials). For a source $j$, $\phi(x) = i\int d^4y\,D_R(x - y)j(y) = \int d^3y\,\frac{j(t - |\mathbf x - \mathbf y|, \mathbf y)}{4\pi|\mathbf x - \mathbf y|}$, using $i\cdot(-i) = 1$ and the δ to do the $y^0$ integral. For a static source this is $\int d^3y\,j(\mathbf y)/4\pi|\mathbf x - \mathbf y|$, the solution of $-\nabla^2\phi = j$: the sign and the $1/4\pi r$ are right.
>
> *Checked against:* [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6|Theorem §C2b.5.6]], 3 ("for $m = 0$, $D_R = -\frac{i}{2\pi}\theta(\xi^0)\delta(\xi^2) = -\frac{i}{4\pi r}\delta(\xi^0 - r)$", derivation step 6), [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]] ($D = -\frac{1}{4\pi r}[\delta(t - r) - \delta(t + r)]$) and [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]] (the massive interior tail).

^sol-px-4-2-1

### X4.2.2 · The massless Feynman function
*[variation of PS4.2(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-2-2]]

> [!success]- Solution
> **Answer.** $D_F(\xi) = -\dfrac{1}{4\pi^2}\,\dfrac{1}{\xi^2 - i\varepsilon} = \dfrac{1}{4\pi^2}\,\dfrac{1}{-\xi^2 + i\varepsilon}$, for both signs of $\xi^0$.
>
> **Step 1** ($\xi^0 = t > 0$). $(t - i\varepsilon)^2 - r^2 = t^2 - r^2 - 2i\varepsilon t - \varepsilon^2 = \xi^2 - i\varepsilon'$ with $\varepsilon' = 2\varepsilon t + \varepsilon^2 \to 0^+$. So $\theta(t)D_W(\xi) = -\frac{1}{4\pi^2}\frac{1}{\xi^2 - i\varepsilon'}$.
>
> **Step 2** ($t < 0$). $D_W(-\xi) = -\frac{1}{4\pi^2}\frac{1}{(-t - i\varepsilon)^2 - r^2}$, and $(-t - i\varepsilon)^2 = (t + i\varepsilon)^2 = t^2 + 2i\varepsilon t - \varepsilon^2$. With $t < 0$, $2i\varepsilon t = -2i\varepsilon|t|$: again $\xi^2 - i\varepsilon''$, $\varepsilon'' = 2\varepsilon|t| + \varepsilon^2 \to 0^+$.
>
> **Step 3** (one formula). Only the sign of the infinitesimal matters in the limit, so both halves are $-\frac{1}{4\pi^2}\frac{1}{\xi^2 - i\varepsilon}$, and the step functions add to $1$: the Answer. (At $t = 0$, $\xi^2 = -r^2 < 0$ and nothing is singular.) The Wightman function has $-i\varepsilon\,\xi^0$, odd in $t$; time ordering replaces it by $-i\varepsilon$, even: $D_F$ is even in $\xi$ and Lorentz invariant, as it must be.
>
> **Step 4** (checks). (i) Off the cone $D_F = -1/4\pi^2\xi^2$, equal to $D_W$ there; at spacelike $\xi$ it is real, $1/4\pi^2r^2$. (ii) It is the $m \to 0$ limit of $D_F = \frac{mK_1(ms)}{4\pi^2s}$, $s = \sqrt{-\xi^2 + i\varepsilon}$, since $K_1(z) \simeq 1/z$: $\frac{m}{4\pi^2s}\cdot\frac{1}{ms} = \frac{1}{4\pi^2s^2} = \frac{1}{4\pi^2(-\xi^2 + i\varepsilon)}$. (iii) Imaginary part on the cone by Sokhotski–Plemelj: $\frac{1}{-\xi^2 + i\varepsilon} \to -\mathcal P\frac{1}{\xi^2} - i\pi\delta(\xi^2)$, so $D_F = -\frac{1}{4\pi^2}\mathcal P\frac{1}{\xi^2} - \frac{i}{4\pi}\delta(\xi^2)$. This is $D_F = \frac12D_1 + \frac i2\operatorname{sgn}(\xi^0)D$ (from $D_W(\pm\xi) = \frac12(D_1 \pm iD)$) with the massless $D_1 = -\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$ and $\operatorname{sgn}(\xi^0)D = -\frac{1}{2\pi}\delta(\xi^2)$.
>
> *Derived here; check:* from the massless $D_W$ of [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]] and the definition of [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]]; limit (ii) against [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3|Theorem §C2b.7.3]] with [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3; (iii) against [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]] and [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions#^thm-ca-6-2|Theorem §CA.6.2]].

^sol-px-4-2-2

### X4.3.1 · Small distances: the massless limit
*[extension of PS4.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-3-1]]

> [!success]- Solution
> **Answer.** $D_W \simeq \dfrac{1}{4\pi^2r^2} = -\dfrac{1}{4\pi^2\xi^2}$ for $mr \ll 1$: the massless Wightman function at spacelike separation. Likewise $D_1 \simeq \frac{1}{2\pi^2r^2}$, $D = 0$.
>
> **Step 1** (insert the small-argument form). With $K_1(z) \simeq 1/z$, $z = mr$:
> $$
> D_W = \frac{m}{4\pi^2r}K_1(mr) \simeq \frac{m}{4\pi^2r}\cdot\frac{1}{mr} = \frac{1}{4\pi^2r^2} .
> $$
> The mass cancels: at distances much shorter than the Compton length $1/m$ the field does not feel its mass.
>
> **Step 2** (compare with PS4.2). The massless function is $D_W = -\frac{1}{4\pi^2}\frac{1}{(\xi^0 - i\varepsilon)^2 - \boldsymbol\xi^2}$. At spacelike $\xi$ the denominator does not vanish, so $\varepsilon \to 0$ may be taken: $D_W = -\frac{1}{4\pi^2\xi^2} = \frac{1}{4\pi^2r^2}$ with $\xi^2 = -r^2$. Same as Step 1.
>
> **Step 3** (first correction). $K_1(z) = \frac1z + \frac z2\ln\frac z2 + O(z)$ gives $D_W = \frac{1}{4\pi^2r^2} + \frac{m^2}{8\pi^2}\ln\frac{mr}{2} + O(m^2)$: the mass enters first through a logarithm, integrable, so the singularity on the cone is the massless one.
>
> **Step 4** ($D$ and $D_1$). $D_W$ is real at spacelike $\xi$, so $D = 2\operatorname{Im}D_W = 0$ and $D_1 = 2D_W \simeq \frac{1}{2\pi^2r^2}$, matching the massless $D_1 = -\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$ off the cone.
>
> *Checked against:* [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]] ("$\simeq 1/4\pi^2r^2$ for $mr \ll 1$"), [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5|Theorem §C2b.3.5]] (the massless leading term and the $\frac{m^2}{8\pi^2}\ln\frac{ms}{2}$ correction), [[§CA.5 Gaussian Integrals, Stationary Phase and Bessel Functions#^thm-ca-5-3|Theorem §CA.5.3]], 3, and [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]].

^sol-px-4-3-1

### X4.3.2 · The decay length with units: the pion
*[extension of PS4.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-3-2]]

> [!success]- Solution
> **Answer.** $e^{-mr} \to e^{-r/\lambda}$ with $\lambda = \hbar/mc$ (the reduced Compton wavelength); for the pion $\lambda = \hbar c/m_\pi c^2 = 197.3\ \text{MeV fm}/140\ \text{MeV} \approx 1.41$ fm, and $D_1(11\ \text{fm})/D_1(10\ \text{fm}) \approx 0.43$ ($D_1$ drops by a factor $\approx 2.3$).
>
> **Step 1** (the exponent). The argument of an exponential must be a pure number. In natural units $mr$ is mass × length; the only length made from $m$, $\hbar$, $c$ is $\hbar/mc$, so $mr \to mcr/\hbar = r/\lambda$. The prefactor becomes $\sqrt{mc/\hbar}\,r^{-3/2}$, of dimension length$^{-2}$, the same as the short-distance $1/2\pi^2r^2$ (any overall field normalization cancels in the ratio below).
>
> **Step 2** (numbers). $\hbar c = 197.33$ MeV fm, so $\lambda = 197.33/140 = 1.4095$ fm, and $r/\lambda = 7.09$ at $r = 10$ fm: well in the regime $mr \gg 1$.
>
> **Step 3** (the ratio). Both factors of $D_1 \simeq \sqrt{m/8\pi^3}\,r^{-3/2}e^{-mr}$ change:
> $$
> \frac{D_1(r + \Delta)}{D_1(r)} = \Bigl(\frac{r}{r + \Delta}\Bigr)^{3/2}e^{-\Delta/\lambda} = \Bigl(\frac{10}{11}\Bigr)^{3/2}e^{-1/1.4095} = 0.867\times0.492 = 0.426 .
> $$
> The power law accounts for about $13\%$ of the drop, the exponential for the rest.
>
> **Step 4** (size of the neglected terms). The next term of the asymptotic series, $(1 + \frac{3}{8mr})$, changes from $1.053$ at $mr = 7.09$ to $1.048$ at $mr = 7.80$, multiplying the ratio by $0.995$: $0.424$. So $\approx 0.43$ to the accuracy asked. Physically: the vacuum correlations of the pion field fall by $1/e$ every $1.4$ fm, the range of the Yukawa force between nucleons.
>
> *Checked against:* [[§C2b.4 Microcausality and the Commutator Function#^rem-c2b-4-3|§C2b.4, Remark: Influence and correlation]] ($D_1 \simeq \sqrt{m/8\pi^3}\,r^{-3/2}e^{-mr}$), [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3|Theorem §C2b.3.3]] (the correction $1 + \frac{3}{8mr}$), the unit restoration of [[§C2b.3 Explicit Forms of the Wightman Function#^ex-c2b-3-1|Example §C2b.3.1]] ($m\rho \to mc\rho/\hbar$) and [[P4 Restoring ħ and c#^p4-2|P4, step 2]]; the large-distance form as in the user's PHY 513 Problem Set 4, Problem 3(b), as written.

^sol-px-4-3-2

### X4.4.1 · The advanced function is a Green's function
*[variation of PS4.4(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-4-1]]

> [!success]- Solution
> **Answer.** $(\partial_x^2 + m^2)D_A(x - y) = \delta(x^0 - y^0)\,\langle0|[\hat\pi(x), \hat\phi(y)]|0\rangle = -i\delta^4(x - y)$; the only contribution is the contact term of the second time derivative.
>
> **Step 1** (notation). $\xi = x - y$, $t = \xi^0$, $iD(\xi) = \langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle$, so $D_A = -\theta(-t)\,iD$. Derivatives are in $x$; $\partial_{x^0}\theta(y^0 - x^0) = \partial_t\theta(-t) = -\delta(t)$.
>
> **Step 2** (spatial part and mass). $-\nabla^2 + m^2$ does not touch θ: $(-\nabla^2 + m^2)D_A = -\theta(-t)(-\nabla^2 + m^2)\,iD$.
>
> **Step 3** (first time derivative). Product rule:
> $$
> \partial_0D_A = -(\partial_0\theta(-t))\,iD - \theta(-t)\,\partial_0iD = \delta(t)\,iD(\xi) - \theta(-t)\,\partial_0iD .
> $$
> $\delta(t)\,iD$ evaluates the commutator at equal times, $\langle0|[\hat\phi(t, \mathbf x), \hat\phi(t, \mathbf y)]|0\rangle = 0$: dropped.
>
> **Step 4** (second time derivative).
> $$
> \partial_0^2D_A = \delta(t)\,\partial_0iD(\xi) - \theta(-t)\,\partial_0^2iD .
> $$
> Since $\partial_0\hat\phi(x) = \hat\pi(x)$, $\partial_{x^0}iD = \langle0|[\hat\pi(x), \hat\phi(y)]|0\rangle$, which at equal times is $-\langle0|[\hat\phi(\mathbf y), \hat\pi(\mathbf x)]|0\rangle = -i\delta^3(\mathbf x - \mathbf y)$. So the contact term is $\delta(t)(-i)\delta^3(\boldsymbol\xi) = -i\delta^4(x - y)$.
>
> **Step 5** (assemble). $(\partial^2 + m^2)D_A = -i\delta^4(x - y) - \theta(-t)(\partial^2 + m^2)\,iD$, and $(\partial^2 + m^2)iD = 0$ since $iD = D_W(\xi) - D_W(-\xi)$ and each $D_W$ solves the homogeneous equation. Hence $(\partial_x^2 + m^2)D_A = -i\delta^4(x - y)$. Note the sign bookkeeping: $D_A$ carries an overall $-$ and $\partial_0\theta(-t) = -\delta$; the two minus signs give the same $+\delta(t)\partial_0iD$ as for $D_R = \theta(t)\,iD$.
>
> **Step 6** (check by reflection). $D_A(\xi) = D_R(-\xi)$; $\partial^2$ is even under $\xi \to -\xi$ and $\delta^4$ is even, so $D_A$ inherits $(\partial^2 + m^2)D_R = -i\delta^4$. As a second check, $D_A = D_F - D_W(\xi)$ (for $t > 0$: $0 = D_W(\xi) - D_W(\xi)$; for $t < 0$: $-iD = D_W(-\xi) - D_W(\xi)$), and $D_W$ is homogeneous.
>
> *Checked against:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-5|Theorem §C2b.6.5]] (derivation steps 1–4, the same product-rule computation for $D_F$, one derivative at a time), [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7|Theorem §C2b.5.7]] ($D_A = -\theta(-\xi^0)iD = D_R(-\xi)$), [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]] and [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]].

^sol-px-4-4-1

### X4.4.2 · The p⁰ integral of the Feynman propagator
*[variation of PS4.4(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-4-2]]

> [!success]- Solution
> **Answer.** $\displaystyle\int\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{p^2 - m^2 + i\varepsilon} = \theta(t)\frac{e^{-iE_{\mathbf p}t}}{2E_{\mathbf p}} + \theta(-t)\frac{e^{iE_{\mathbf p}t}}{2E_{\mathbf p}}$, and the $\mathbf p$ integral gives $D_F(\xi) = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$.
>
> **Step 1** (the poles). At fixed $\mathbf p$, $p^2 - m^2 + i\varepsilon = (p^0)^2 - E_{\mathbf p}^2 + i\varepsilon = (p^0 - E')(p^0 + E')$ with $E' = \sqrt{E_{\mathbf p}^2 - i\varepsilon} = E_{\mathbf p} - i\varepsilon/2E_{\mathbf p} + O(\varepsilon^2)$. Poles: $p^0 = E_{\mathbf p} - i\varepsilon'$ (below the axis) and $p^0 = -E_{\mathbf p} + i\varepsilon'$ (above), $\varepsilon' = \varepsilon/2E_{\mathbf p} > 0$.
>
> **Step 2** (which way to close). $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$: for $t > 0$ it decays in the lower half-plane, for $t < 0$ in the upper. The integrand falls like $|p^0|^{-2}$, so the arc vanishes.
>
> **Step 3** ($t > 0$). Close downward, clockwise ($-2\pi i$), enclosing $E'$. Residue of $\frac{i\,e^{-ip^0t}}{(p^0 - E')(p^0 + E')}$ there: $\frac{i\,e^{-iE't}}{2E'}$. So
> $$
> \int\frac{dp^0}{2\pi}(\cdots) = \frac{1}{2\pi}(-2\pi i)\frac{i\,e^{-iE't}}{2E'} = \frac{e^{-iE't}}{2E'} \to \frac{e^{-iE_{\mathbf p}t}}{2E_{\mathbf p}} .
> $$
> With $\int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot\boldsymbol\xi}$: $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-iE_{\mathbf p}t + i\mathbf p\cdot\boldsymbol\xi} = D_W(\xi)$.
>
> **Step 4** ($t < 0$). Close upward, counterclockwise ($+2\pi i$), enclosing $-E'$. Residue: $\frac{i\,e^{iE't}}{-2E'}$. So $\frac{1}{2\pi}(2\pi i)\frac{i\,e^{iE't}}{-2E'} = \frac{e^{iE't}}{2E'} \to \frac{e^{iE_{\mathbf p}t}}{2E_{\mathbf p}}$. Then $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{iE_{\mathbf p}t + i\mathbf p\cdot\boldsymbol\xi}$; substitute $\mathbf p \to -\mathbf p$ (Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$): $e^{iE_{\mathbf p}t - i\mathbf p\cdot\boldsymbol\xi} = e^{-ip\cdot(-\xi)}$, so this is $D_W(-\xi)$.
>
> **Step 5** (assemble, and the two minus signs). $D_F = \theta(t)D_W(\xi) + \theta(-t)D_W(-\xi)$. Both pieces come out positive although the residues have opposite signs ($\pm1/2E$): the orientation ($-2\pi i$ below, $+2\pi i$ above) compensates. As $\varepsilon \to 0^+$ the limit is pointwise for $t \ne 0$ and bounded by $1/2E_{\mathbf p}$, so it holds as distributions. *Check:* at $t \to 0^\pm$ both sides give $\frac{1}{2E_{\mathbf p}}$: mode by mode $D_F$ is $e^{-iE_{\mathbf p}|t|}/2E_{\mathbf p}$, continuous in $t$ with a jump $-i$ in its $t$-derivative, which is the $-i\delta(t)$ of the Green's-function equation (PS4.4(c)).
>
> *Checked against:* [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]] (derivation, both routes; the second route is this $i\varepsilon$ computation, Yu (6.198)–(6.210)), [[§CA.4 Contour Integration#^thm-ca-4-4|Theorem §CA.4.4]], 3, [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|§C2b.6, Caution: Signs that slip]] and the procedure [[P2 Green's Functions by Contour Integration#^p2-2|P2, steps 2–7]] (step 7: the jump $-i$ in $G'$).

^sol-px-4-4-2

### X4.4.3 · The Dirac Feynman propagator from the scalar one
*[extension of PS4.4(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-4-3]]

> [!success]- Solution
> **Answer.** $(i\slashed\partial_x - m)S_F(x - y) = -(\partial_x^2 + m^2)D_F(x - y)\,\mathbf 1 = i\delta^4(x - y)\,\mathbf 1$, and $\tilde S_F(p) = \dfrac{i(\slashed p + m)}{p^2 - m^2 + i\varepsilon}$ ($= \dfrac{i}{\slashed p - m + i\varepsilon}$ as a matrix inverse).
>
> **Step 1** ($\slashed\partial^2 = \partial^2$). $\slashed\partial\slashed\partial = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \frac12\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu = g^{\mu\nu}\partial_\mu\partial_\nu = \partial^2$, using that $\partial_\mu\partial_\nu$ is symmetric (the antisymmetric half of $\gamma^\mu\gamma^\nu$ drops) and $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$.
>
> **Step 2** (factor the Klein–Gordon operator). The constant matrices commute with $\partial$, so
> $$
> (i\slashed\partial - m)(i\slashed\partial + m) = i^2\slashed\partial\slashed\partial + im\slashed\partial - im\slashed\partial - m^2 = -(\partial^2 + m^2)\,\mathbf 1 .
> $$
>
> **Step 3** (apply to $D_F$). $(i\slashed\partial_x - m)S_F = (i\slashed\partial_x - m)(i\slashed\partial_x + m)D_F = -(\partial_x^2 + m^2)D_F\,\mathbf 1 = -(-i\delta^4(x - y))\mathbf 1 = i\delta^4(x - y)\,\mathbf 1$, by $(\partial^2 + m^2)D_F = -i\delta^4$ (PS4.4(c)). (Derivatives of distributions commute, so the order of the two first-order operators is immaterial.)
>
> **Step 4** (momentum space). $D_F = \int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip\cdot\xi}}{p^2 - m^2 + i\varepsilon}$ and $i\partial_\mu e^{-ip\cdot\xi} = i(-ip_\mu)e^{-ip\cdot\xi} = p_\mu e^{-ip\cdot\xi}$, so $i\slashed\partial \to \slashed p$ and $\tilde S_F(p) = (\slashed p + m)\frac{i}{p^2 - m^2 + i\varepsilon}$.
>
> **Step 5** (checks). (i) Momentum-space Green's equation: $(\slashed p - m)(\slashed p + m) = \slashed p\slashed p - m^2 = p^2 - m^2$, so $(\slashed p - m)\tilde S_F = \frac{i(p^2 - m^2)}{p^2 - m^2 + i\varepsilon} \to i\,\mathbf 1$, the transform of $i\delta^4$. (ii) Matrix-inverse form: $(\slashed p - m)^{-1} = (\slashed p + m)/(p^2 - m^2)$, the same identity. (iii) Same factor for every contour: $S_R = (i\slashed\partial + m)D_R$, $S_A = (i\slashed\partial + m)D_A$ are Green's functions by the same Steps 2–3. Sign check against the scalar: the Dirac operator's normalization $+i\delta^4$ versus the scalar's $-i\delta^4$ is the $-1$ of Step 2.
>
> *Checked against:* [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-1|Theorem §C5b.8.1]] ($S_C = (i\slashed\partial + m)D_C$, $(i\slashed\partial_x - m)S_C = i\delta^4\mathbf 1$, $(\slashed p - m)\tilde S_C = i\mathbf 1$), [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]] ($\tilde S_F = i(\slashed p + m)/(p^2 - m^2 + i\varepsilon)$) and [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-5|Theorem §C5b.8.5]] (the matrix form).

^sol-px-4-4-3

---

<!-- Fragment sol-EF: sections E and F of PHY 513 Practice Midterm 2 (Extended Set). Writer agent, 2026-10-14. Numerical checks: scratchpad ef/check_ef.py, check_T.py, check_T2.py, check_d.py (numpy/scipy, chiral basis). -->

## E. Lorentz group, algebra, representations

### X4.5.1 · Two commutators of the Lorentz algebra
*[variation of PS4.5(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-5-1]]

> [!success]- Solution
> **Answer.** $[\mathcal J^{01}, \mathcal J^{12}] = -i\mathcal J^{02}$, i.e. $[K_1, J_3] = -iK_2$, equivalently $[J_3, K_1] = iK_2$; and $[\mathcal J^{12}, \mathcal J^{23}] = -i\mathcal J^{13} = i\mathcal J^{31}$, i.e. $[J_3, J_1] = iJ_2$.
>
> **Step 1** (first commutator, $\mu\nu\rho\sigma = 0112$). The four metric factors of the algebra are $g^{\nu\rho} = g^{11} = -1$, $g^{\mu\rho} = g^{01} = 0$, $g^{\nu\sigma} = g^{12} = 0$, $g^{\mu\sigma} = g^{02} = 0$, so only the first term survives:
>
> $$
> [\mathcal J^{01}, \mathcal J^{12}] = i\bigl(g^{11}\mathcal J^{02} - g^{01}\mathcal J^{12} - g^{12}\mathcal J^{01} + g^{02}\mathcal J^{11}\bigr) = i(-1)\mathcal J^{02} = -i\mathcal J^{02} .
> $$
>
> **Step 2** (second commutator, $\mu\nu\rho\sigma = 1223$). Now $g^{\nu\rho} = g^{22} = -1$ and $g^{\mu\rho} = g^{12}$, $g^{\nu\sigma} = g^{23}$, $g^{\mu\sigma} = g^{13}$ all vanish:
>
> $$
> [\mathcal J^{12}, \mathcal J^{23}] = i\bigl(g^{22}\mathcal J^{13} - g^{12}\mathcal J^{23} - g^{23}\mathcal J^{12} + g^{13}\mathcal J^{22}\bigr) = -i\mathcal J^{13} = +i\mathcal J^{31} ,
> $$
>
> using the antisymmetry $\mathcal J^{13} = -\mathcal J^{31}$.
>
> **Step 3** (translate into $\mathbf J$, $\mathbf K$). With $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, i.e. $\mathbf J = (\mathcal J^{23}, \mathcal J^{31}, \mathcal J^{12})$, and $K_i = \mathcal J^{0i}$: $\mathcal J^{01} = K_1$, $\mathcal J^{02} = K_2$, $\mathcal J^{12} = J_3$, $\mathcal J^{23} = J_1$, $\mathcal J^{31} = J_2$. Step 1 reads $[K_1, J_3] = -iK_2$, so $[J_3, K_1] = +iK_2 = i\varepsilon_{312}K_2$; Step 2 reads $[J_3, J_1] = iJ_2 = i\varepsilon_{312}J_2$. These are instances of $[J_i, K_j] = i\varepsilon_{ijk}K_k$ (a rotation and a boost give a boost: $\mathbf K$ is a vector under rotations) and $[J_i, J_j] = i\varepsilon_{ijk}J_k$ (two rotations give a rotation).
>
> **Step 4** (check). With the $4\times4$ vector generators $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$ both commutators were verified numerically (numpy).
>
> *Checked against:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] (both forms of the algebra), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^def-c1a-6-2|Def. §C1a.6.2]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] (the matrices); drill: [[PHY 513 PS Drill#^ps4-5-a|PS Drill, PS4.5(a)]], Q7.

^sol-px-4-5-1

### X4.5.2 · γ⁵ commutes with the spinor generators
*[variation of PS4.5(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-5-2]]

> [!success]- Solution
> **Answer.** $[\gamma^5, S^{\mu\nu}] = 0$, hence $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$ for every spinor Lorentz transformation. The eigenspaces $\gamma^5 = -1$ (left-handed, $(\frac12, 0)$) and $\gamma^5 = +1$ (right-handed, $(0, \frac12)$) are each mapped to themselves: the two chiral halves of a Dirac spinor transform separately, and the Dirac representation is reducible.
>
> **Step 1** ($\gamma^5$ commutes with a product of two $\gamma$'s). $\gamma^5\gamma^\mu = -\gamma^\mu\gamma^5$ for every $\mu$. Moving $\gamma^5$ through two factors costs two signs:
>
> $$
> \gamma^5\gamma^\mu\gamma^\nu = -\gamma^\mu\gamma^5\gamma^\nu = +\gamma^\mu\gamma^\nu\gamma^5 .
> $$
>
> The same with $\mu \leftrightarrow \nu$; subtracting, $\gamma^5[\gamma^\mu, \gamma^\nu] = [\gamma^\mu, \gamma^\nu]\gamma^5$, and multiplying by $\frac i4$: $[\gamma^5, S^{\mu\nu}] = 0$, with $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$.
>
> **Step 2** (finite transformations). $\Lambda_{1/2} = \exp(X)$ with $X = -\frac i2\omega_{\mu\nu}S^{\mu\nu}$. By Step 1, $\gamma^5X = X\gamma^5$, hence $\gamma^5X^n = X^n\gamma^5$ for every power, and term by term in the exponential series $\gamma^5\Lambda_{1/2} = \Lambda_{1/2}\gamma^5$, i.e. $\Lambda_{1/2}^{-1}\gamma^5\Lambda_{1/2} = \gamma^5$: $\gamma^5$ is a Lorentz scalar matrix (unlike $\gamma^\mu$, which rotates as a vector, $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$).
>
> **Step 3** (the chiral halves). If $\gamma^5\psi = \mp\psi$, then $\gamma^5(\Lambda_{1/2}\psi) = \Lambda_{1/2}\gamma^5\psi = \mp\Lambda_{1/2}\psi$: the transformed spinor has the same chirality. Equivalently the projectors $P_{L,R} = \frac12(\mathbb 1 \mp \gamma^5)$ commute with $\Lambda_{1/2}$, so $\psi_L = P_L\psi$ and $\psi_R = P_R\psi$ never mix under Lorentz transformations, in every basis. In the chiral basis this is visible: $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ and every $S^{\mu\nu}$ is block diagonal, $S^{ij} = \frac12\varepsilon^{ijk}\operatorname{diag}(\sigma^k, \sigma^k)$, $S^{0i} = -\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$. The halves are not the same representation: $K_i = i\gamma^5J_i$, so the boost generators are $-iJ_i$ on the left-handed half and $+iJ_i$ on the right-handed one; the labels are $(\frac12, 0)$ for $\gamma^5 = -1$ and $(0, \frac12)$ for $\gamma^5 = +1$.
>
> **Step 4** (what does mix them). $\gamma^\mu$ anticommutes with $\gamma^5$, so it maps one eigenspace to the other; this is why the mass term $\bar\psi\psi$ pairs $\psi_L$ with $\psi_R$ while the kinetic term does not. (Step 1 verified numerically for all 16 $S^{\mu\nu}$.)
>
> *Checked against:* [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|Theorem §CB.18.4]] (parts 1–3, including $K_i = i\gamma^5J_i$), [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]].

^sol-px-4-5-2

### X4.5.3 · The spinor boost acting on γ⁰
*[extension of PS4.5(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-4-5-3]]

> [!success]- Solution
> **Answer.** $\Lambda_{1/2}^{-1}\gamma^0\Lambda_{1/2}$ has the entries $e^{\eta}, e^{-\eta}, e^{-\eta}, e^{\eta}$ at the positions $(1,3), (2,4), (3,1), (4,2)$ and zeros elsewhere; this is exactly $\cosh\eta\,\gamma^0 + \sinh\eta\,\gamma^3 = \Lambda^0{}_\nu\gamma^\nu$.
>
> **Step 1** (conjugating by a diagonal matrix). Write $b = e^{\eta/2}$, so $\Lambda_{1/2} = D = \operatorname{diag}(b^{-1}, b, b, b^{-1})$ and $D^{-1} = \operatorname{diag}(b, b^{-1}, b^{-1}, b)$. For any matrix $M$, $(D^{-1}MD)_{AB} = (D^{-1})_{AA}\,M_{AB}\,D_{BB}$ (no sum): entry $(A, B)$ is multiplied by $f_{AB} = (D^{-1})_{AA}D_{BB}$.
>
> **Step 2** (the left side). $\gamma^0 = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ has entries $1$ at $(1,3), (2,4), (3,1), (4,2)$. The factors there:
>
> $$
> f_{13} = b\cdot b = e^{\eta}, \qquad f_{24} = b^{-1}\cdot b^{-1} = e^{-\eta}, \qquad f_{31} = b^{-1}\cdot b^{-1} = e^{-\eta}, \qquad f_{42} = b\cdot b = e^{\eta} .
> $$
>
> **Step 3** (the right side). Row $0$ of the vector boost has $\Lambda^0{}_0 = \cosh\eta$, $\Lambda^0{}_3 = \sinh\eta$, $\Lambda^0{}_1 = \Lambda^0{}_2 = 0$, so $\Lambda^0{}_\nu\gamma^\nu = \cosh\eta\,\gamma^0 + \sinh\eta\,\gamma^3$. $\gamma^3 = \begin{pmatrix}0&\sigma^3\\-\sigma^3&0\end{pmatrix}$ has entries $+1, -1, -1, +1$ at $(1,3), (2,4), (3,1), (4,2)$. So the right side has, at the same four positions, $\cosh\eta + \sinh\eta = e^{\eta}$, $\cosh\eta - \sinh\eta = e^{-\eta}$, $\cosh\eta - \sinh\eta = e^{-\eta}$, $\cosh\eta + \sinh\eta = e^{\eta}$, and zeros elsewhere. Equal to Step 2.
>
> **Step 4** (reading). Each entry of $\gamma^0$ joins a component stretched by $e^{\mp\eta/2}$ to one stretched by $e^{\pm\eta/2}$; the two half-rapidities multiply to $e^{\pm\eta}$, the eigenvalues of the vector boost on $e_0 \pm e_3$. The check needs the matched pair: the same $\eta$ in $\Lambda_{1/2}$ and in $\Lambda$. Verified numerically ($\eta = 0.7$: $2.0138, 0.4966, 0.4966, 2.0138$).
>
> *Checked against:* [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^ex-c5a-4-2|Example §C5a.4.2]] (step 5 of its derivation: the same entries), [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]], 1, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], 1, [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], 1.

^sol-px-4-5-3

### X5.1.1 · The two signs of K
*[variation of PS5.1(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-1-1]]

> [!success]- Solution
> **Answer.** In both conventions $[J_i, J_j] = i\varepsilon_{ijk}J_k$, $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$. The split is exchanged: $\mathbf J_\pm^{\rm (PS5)} = \mathbf J_\mp^{\rm (course)}$, so Problem Set 5's label $(j_+, j_-)$ is the course's $(j_-, j_+)$, and its boost parameter is $\boldsymbol\beta = -\boldsymbol\eta$.
>
> **Step 1** (the course's relations). With $K_i = \mathcal J^{0i}$ the algebra in rotation–boost form is $[J_i, J_j] = i\varepsilon_{ijk}J_k$, $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$. For instance, from the covariant algebra with $\mu\nu\rho\sigma = 0i0j$:
>
> $$
> [\mathcal J^{0i}, \mathcal J^{0j}] = i\bigl(g^{i0}\mathcal J^{0j} - g^{00}\mathcal J^{ij} - g^{ij}\mathcal J^{00} + g^{0j}\mathcal J^{i0}\bigr) = -i\mathcal J^{ij} = -i\varepsilon_{ijk}J_k ,
> $$
>
> since $g^{i0} = g^{0j} = 0$, $\mathcal J^{00} = 0$, $g^{00} = 1$ and $\mathcal J^{ij} = \varepsilon_{ijk}J_k$.
>
> **Step 2** (Problem Set 5's generators). $K'_i \equiv \mathcal J^{i0} = -\mathcal J^{0i} = -K_i$, same $\mathbf J$. Then
> - $[J_i, J_j]$ contains no $\mathbf K$: unchanged;
> - $[J_i, K'_j] = -[J_i, K_j] = -i\varepsilon_{ijk}K_k = i\varepsilon_{ijk}K'_k$: same form;
> - $[K'_i, K'_j] = (-1)^2[K_i, K_j] = -i\varepsilon_{ijk}J_k$: same form.
>
> Each relation is invariant under $\mathbf K \to -\mathbf K$ (one $\mathbf K$ on each side of the second, two on the left and none on the right of the third). The user's submitted solution, in Problem Set 5's convention, obtains exactly these: $[K^i, K^j] = [J^{i0}, J^{j0}] = -iJ^{ij} = -i\epsilon^{ijk}L^k$ and $[L^i, K^j] = i\epsilon^{ijk}K^k$ (as written).
>
> **Step 3** (the split). $\mathbf J'_\pm = \frac12(\mathbf J \pm i\mathbf K') = \frac12(\mathbf J \mp i\mathbf K) = \mathbf J_\mp$. A representation in which $\mathbf J'_+$ acts as spin $j_+$ and $\mathbf J'_-$ as spin $j_-$ is therefore one in which the course's $\mathbf J_-$ acts as spin $j_+$ and $\mathbf J_+$ as spin $j_-$: the course's $(j_-, j_+)$.
>
> **Step 4** (the parameter). The same transformation is $1 - i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\beta\cdot\mathbf K' = 1 - i\boldsymbol\theta\cdot\mathbf J - i\boldsymbol\eta\cdot\mathbf K$, so $-\boldsymbol\beta\cdot\mathbf K = \boldsymbol\eta\cdot\mathbf K$, $\boldsymbol\beta = -\boldsymbol\eta$. Check: Problem Set 5's $(\frac12, 0)$ law $1 - i\boldsymbol\theta\cdot\frac{\boldsymbol\sigma}2 - \boldsymbol\beta\cdot\frac{\boldsymbol\sigma}2$ becomes $1 - i\boldsymbol\theta\cdot\frac{\boldsymbol\sigma}2 + \boldsymbol\eta\cdot\frac{\boldsymbol\sigma}2$, the course's $(0, \frac12)$ law: one object, two labels. Nothing physical depends on the labels; mixing the conventions exchanges them. (The sign invariance of all three relations verified numerically in the vector representation.)
>
> *Checked against:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]], [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^der-cb-5-6c|Derivation §CB.5.6 (the J, K form)]] (the user's Problem Set 5, Problem 1(a), rewritten with $K_i = \mathcal J^{0i}$), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-2|Theorem §CB.6.2]]; drill: [[PHY 513 PS Drill#^ps5-1-a|PS Drill, PS5.1(a)]], Q4.

^sol-px-5-1-1

### X5.1.2 · A finite boost on the two Weyl halves
*[variation of PS5.1(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-1-2]]

> [!success]- Solution
> **Answer.** On $(\frac12, 0)$: $D = e^{-\eta\sigma^3/2} = \operatorname{diag}(e^{-\eta/2}, e^{\eta/2})$; on $(0, \frac12)$: $D = e^{+\eta\sigma^3/2} = \operatorname{diag}(e^{\eta/2}, e^{-\eta/2})$. For $\eta > 0$ the $(0, \frac12)$ spinor (right-handed, $\psi_R$) grows on its upper component; the $(\frac12, 0)$ spinor grows on its lower one.
>
> **Step 1** (the generators). In the course's convention ($K_i = \mathcal J^{0i}$) both halves have $\mathbf J = \frac12\boldsymbol\sigma$, and $\mathbf K = -\frac i2\boldsymbol\sigma$ on $(\frac12, 0)$, $\mathbf K = +\frac i2\boldsymbol\sigma$ on $(0, \frac12)$: from $\mathbf K = -i(\mathbf J_+ - \mathbf J_-)$ with $(\mathbf J_+, \mathbf J_-) = (\frac12\boldsymbol\sigma, 0)$ or $(0, \frac12\boldsymbol\sigma)$.
>
> **Step 2** (the exponent). A boost along $z$ has $\boldsymbol\theta = 0$, $\boldsymbol\eta = \eta\hat{\mathbf z}$, so $D = e^{-i\eta K_3}$. On $(\frac12, 0)$: $-i\eta\bigl(-\frac i2\sigma^3\bigr) = (-i)(-i)\frac\eta2\sigma^3 = -\frac\eta2\sigma^3$. On $(0, \frac12)$: $-i\eta\bigl(+\frac i2\sigma^3\bigr) = +\frac\eta2\sigma^3$.
>
> **Step 3** (exponentiate). $\sigma^3 = \operatorname{diag}(1, -1)$ is diagonal, so the exponential is taken entry by entry: $e^{-\eta\sigma^3/2} = \operatorname{diag}(e^{-\eta/2}, e^{\eta/2})$ and $e^{\eta\sigma^3/2} = \operatorname{diag}(e^{\eta/2}, e^{-\eta/2})$. Both are real, positive, Hermitian, with determinant $1$, and not unitary: finite-dimensional boosts never are.
>
> **Step 4** (cross-check). Stacked, $(\psi_L, \psi_R)$ transforms with $\operatorname{diag}(e^{-\eta/2}, e^{\eta/2}, e^{\eta/2}, e^{-\eta/2})$, the chiral-basis Dirac boost $e^{-i\eta S^{03}}$. So boosting a particle at rest with spin up along $+z$, $u_0 = \sqrt m(\xi, \xi)$, $\xi = (1, 0)^{\mathsf T}$, enhances the upper component of $\psi_R$: positive helicity ends up right-handed, as in X5.6.2. In Problem Set 5's convention ($\boldsymbol\beta = -\boldsymbol\eta$, X5.1.1) the labels $(\frac12, 0)$ and $(0, \frac12)$ are exchanged. (Verified numerically, $\eta = 0.7$.)
>
> *Checked against:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-1|Theorem §C3.2.1]] (table, and step 5 of its derivation: $D = \operatorname{diag}(e^{-\eta/2}, e^{\eta/2})$ on $(\frac12, 0)$), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], 1, [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-2|Theorem §C5a.3.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^cau-c3-2-2|§C3.2, Caution: Which one is (½, 0) depends on the sign of K]].

^sol-px-5-1-2

### X5.1.3 · Dimensions and spins of three representations
*[extension of PS5.1(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-1-3]]

> [!success]- Solution
> **Answer.**
>
> | $(j_+, j_-)$ | dimension | spins under rotations | $2\pi$ rotation | field of the course |
> |---|---|---|---|---|
> | $(\frac12, \frac12)$ | $4$ | $0\oplus1$ | $+1$ | four-vector $A^\mu$ (also $\partial_\mu\phi$) |
> | $(1, 0)\oplus(0, 1)$ | $3 + 3 = 6$ | $1\oplus1$ | $+1$ | antisymmetric tensor $F^{\mu\nu}$, halves $\mathbf E \mp i\mathbf B$ |
> | $(1, \frac12)$ | $6$ | $\frac12\oplus\frac32$ | $-1$ | none |
>
> **Step 1** (dimension). $(j_+, j_-)$ is $\mathbb C^{2j_++1}\otimes\mathbb C^{2j_-+1}$, of dimension $(2j_+ + 1)(2j_- + 1)$: $(\frac12, \frac12)$: $2\cdot2 = 4$; $(1, 0)$ and $(0, 1)$: $3\cdot1 = 3$ each, $6$ for the sum; $(1, \frac12)$: $3\cdot2 = 6$.
>
> **Step 2** (rotation content). Rotations are generated by $\mathbf J = \mathbf J_+ + \mathbf J_-$, so under rotations $(j_+, j_-)$ is the product of spin $j_+$ and spin $j_-$, containing $j = |j_+ - j_-|, \dots, j_+ + j_-$ once each: $(\frac12, \frac12)$: $0\oplus1$ ($1 + 3 = 4$); $(1, 0)$ and $(0, 1)$: $1$ each; $(1, \frac12)$: $\frac12\oplus\frac32$ ($2 + 4 = 6$).
>
> **Step 3** ($2\pi$ rotation). $e^{-2\pi i\hat{\mathbf n}\cdot\mathbf J} = (-1)^{2(j_+ + j_-)}$: $+1$ for $(\frac12, \frac12)$ and for $(1, 0)$, $(0, 1)$ (tensor representations of $SO^+(1,3)$); $(-1)^3 = -1$ for $(1, \frac12)$ (a spinor representation).
>
> **Step 4** (the fields). $(\frac12, \frac12)$ is the vector representation: the Casimirs of the $4\times4$ generators are $\mathbf J_+^2 = \mathbf J_-^2 = \frac34$, and a four-vector is time (spin $0$) plus space (spin $1$). $(\frac12, \frac12)\otimes(\frac12, \frac12) = (1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, $16 = 9 + 3 + 3 + 1$; the six antisymmetric components $F^{\mu\nu}$ are $(1, 0)\oplus(0, 1)$, carried as $\mathbf E \mp i\mathbf B$, which parity exchanges. $(1, \frac12)$ belongs to no field of the course; it occurs, by the same product rule, in a vector-spinor, $(\frac12, \frac12)\otimes(\frac12, 0) = (1, \frac12)\oplus(0, \frac12)$, $8 = 6 + 2$ (the spin-$\frac32$ Rarita–Schwinger field, beyond the course).
>
> *Checked against:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]] (the first two rows), [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-5|Theorem §CB.17.5]] (dimension), [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|Theorem §CB.17.9]] (rotation content, sign), [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-12|Theorem §CB.17.12]] (products), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-3|Theorem §C3.2.3]]. The $(1, \frac12)$ row is not in the catalogue: *Derived here; check:* Theorems §CB.17.5 and §CB.17.9 applied to $(1, \frac12)$, and the count $6 + 2 = 8$ of the product.

^sol-px-5-1-3

### X6.4.1 · Boost along the 2-axis as 4×4 matrices
*[variation of PS6.4(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-4-1]]

> [!success]- Solution
> **Answer.** With $C = \cosh\frac\eta2$, $S = \sinh\frac\eta2$:
>
> $$
> \Lambda^\mu{}_\nu(\eta) = \begin{pmatrix} \cosh\eta & 0 & \sinh\eta & 0 \\ 0 & 1 & 0 & 0 \\ \sinh\eta & 0 & \cosh\eta & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad \Lambda_{1/2}(\eta) = \begin{pmatrix} C & iS & 0 & 0 \\ -iS & C & 0 & 0 \\ 0 & 0 & C & -iS \\ 0 & 0 & iS & C \end{pmatrix} .
> $$
>
> **Step 1** (one generator). With $\omega_{02} = -\omega_{20} = \eta$ and $\mathcal J^{20} = -\mathcal J^{02}$: $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -\frac i2\bigl(\eta\,\mathcal J^{02} + (-\eta)(-\mathcal J^{02})\bigr) = -i\eta\,\mathcal J^{02} = -i\eta K_2$, in every representation.
>
> **Step 2** (vector). $(\mathcal J^{02})^\mu{}_\nu = i(g^{0\mu}\delta^2{}_\nu - g^{2\mu}\delta^0{}_\nu)$ is nonzero only at $(\mu, \nu) = (0, 2)$, value $ig^{00} = i$, and $(2, 0)$, value $-ig^{22} = i$. So $-i\eta\,\mathcal J^{02}$ has $\eta$ at $(0, 2)$ and $(2, 0)$: on the $(x^0, x^2)$ block it is $\eta N$, $N = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $N^2 = \mathbb 1$. Even powers give $\cosh\eta$, odd powers $\sinh\eta\,N$; $x^1$, $x^3$ untouched. On $(1, 0, 0, 0)$: $(\cosh\eta, 0, \sinh\eta, 0)$, a boost toward $+x^2$.
>
> **Step 3** (spinor, chiral basis). $S^{02} = -\frac i2\operatorname{diag}(\sigma^2, -\sigma^2)$, so $-i\eta S^{02} = (-i)(-\frac i2)\eta\operatorname{diag}(\sigma^2, -\sigma^2) = -\frac\eta2\operatorname{diag}(\sigma^2, -\sigma^2)$. Since $(\sigma^2)^2 = \mathbb 1$, $e^{\mp\eta\sigma^2/2} = C\,\mathbb 1 \mp S\,\sigma^2$, and with $\sigma^2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$: upper block $C - S\sigma^2 = \begin{pmatrix}C&iS\\-iS&C\end{pmatrix}$, lower block $C + S\sigma^2 = \begin{pmatrix}C&-iS\\iS&C\end{pmatrix}$. Written out as the $4\times4$ matrix above.
>
> **Step 4** (checks). $\Lambda_{1/2}$ is Hermitian, not unitary, $\det = (C^2 - S^2)^2 = 1$, the two blocks inverse to each other. Theorem §C5a.4.5, 2 with $\hat{\mathbf n} = (0, 1, 0)$ gives the same entries: $-S(n^1 - in^2) = iS$, $-S(n^1 + in^2) = -iS$ upstairs, the opposite downstairs. The pair satisfies $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ for all four $\mu$ (verified numerically with numpy for $\eta = 0.9$, as were both matrices against $\exp(-i\eta\,\mathcal J^{02})$ and $\exp(-i\eta S^{02})$).
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], 2 (with $\hat{\mathbf n} = \hat{\mathbf y}$), [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-5|Theorem §C5a.4.5]], 2, [[§C5a.3 The Lorentz Action on Spinor Space#^ex-c5a-3-1|Example §C5a.3.1]] ($K_2 = S^{02}$), [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-7|Theorem §CB.18.7]]; the $z$-axis version is the user's Problem Set 6, Problem 4(a) ([[PHY 513 PS Drill#^ps6-4-a|PS Drill, PS6.4(a)]]).

^sol-px-6-4-1

### X6.4.2 · Rotation about the 1-axis, and 2π
*[variation of PS6.4(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-4-2]]

> [!success]- Solution
> **Answer.** With $c = \cos\frac\theta2$, $s = \sin\frac\theta2$:
>
> $$
> \Lambda^\mu{}_\nu(\theta) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \cos\theta & -\sin\theta \\ 0 & 0 & \sin\theta & \cos\theta \end{pmatrix}, \qquad \Lambda_{1/2}(\theta) = \begin{pmatrix} c & -is & 0 & 0 \\ -is & c & 0 & 0 \\ 0 & 0 & c & -is \\ 0 & 0 & -is & c \end{pmatrix} ;
> $$
>
> at $\theta = 2\pi$: $\Lambda = \mathbb 1_4$, $\Lambda_{1/2} = -\mathbb 1_4$.
>
> **Step 1** (one generator). $-\frac i2\bigl(\omega_{23}\mathcal J^{23} + \omega_{32}\mathcal J^{32}\bigr) = -\frac i2\bigl(\theta\,\mathcal J^{23} + (-\theta)(-\mathcal J^{23})\bigr) = -i\theta\,\mathcal J^{23} = -i\theta J_1$ (indeed $\theta_1 = \frac12\varepsilon_{1jk}\omega_{jk} = \frac12(\omega_{23} - \omega_{32}) = \theta$).
>
> **Step 2** (vector). $(\mathcal J^{23})^\mu{}_\nu = i(g^{2\mu}\delta^3{}_\nu - g^{3\mu}\delta^2{}_\nu)$: at $(2, 3)$ the value $ig^{22} = -i$, at $(3, 2)$ the value $-ig^{33} = +i$. So $-i\theta\,\mathcal J^{23}$ has $(-i)(-i)\theta = -\theta$ at $(2, 3)$ and $(-i)(i)\theta = +\theta$ at $(3, 2)$: on the $(x^2, x^3)$ block it is $\theta\epsilon$, $\epsilon = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\epsilon^2 = -\mathbb 1$. Even powers give $\cos\theta$, odd powers $\sin\theta\,\epsilon$. $e_2 \mapsto \cos\theta\,e_2 + \sin\theta\,e_3$: counterclockwise about $+x^1$ ($y$ toward $z$).
>
> **Step 3** (spinor). $S^{23} = \frac12\varepsilon^{231}\Sigma^1 = \frac12\operatorname{diag}(\sigma^1, \sigma^1)$, so $-i\theta S^{23} = -\frac{i\theta}2\operatorname{diag}(\sigma^1, \sigma^1)$. With $(\sigma^1)^2 = \mathbb 1$: $e^{-i\theta\sigma^1/2} = c\,\mathbb 1 - is\,\sigma^1 = \begin{pmatrix}c&-is\\-is&c\end{pmatrix}$, the same block on $\psi_L$ and $\psi_R$ (rotations do not distinguish the halves). Unitary, $\det = c^2 + s^2 = 1$.
>
> **Step 4** ($\theta = 2\pi$). Vector: $\cos2\pi = 1$, $\sin2\pi = 0$, so $\Lambda = \mathbb 1_4$. Spinor: $c = \cos\pi = -1$, $s = \sin\pi = 0$, so $\Lambda_{1/2} = -\mathbb 1_4$, $\psi \to -\psi$; it first returns to $+\mathbb 1_4$ at $\theta = 4\pi$. $-\mathbb 1_4$ is the same in every basis ($U(-\mathbb 1)U^\dagger = -\mathbb 1$). This is $(-1)^{2(j_+ + j_-)}$: $+1$ on $(\frac12, \frac12)$, $-1$ on $(\frac12, 0)\oplus(0, \frac12)$.
>
> **Step 5** (checks). Theorem §C1a.6.6, 2 with $\hat{\mathbf n} = \hat{\mathbf x}$: $R^2{}_3 = -\sin\theta\,\varepsilon_{231}n^1 = -\sin\theta$, $R^3{}_2 = -\sin\theta\,\varepsilon_{321}n^1 = +\sin\theta$. Theorem §C5a.4.4, 2 with $\hat{\mathbf n} = \hat{\mathbf x}$: $c - isn^3 = c$, $-is(n^1 \mp in^2) = -is$. Both matrices, the covariance $\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2} = \Lambda^\mu{}_\nu\gamma^\nu$ and the $2\pi$ values verified numerically (numpy, $\theta = 0.6$ and $2\pi$).
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], 2, [[§C5a.4 SL(2,C) and the Group Action on Spinor Space#^thm-c5a-4-4|Theorem §C5a.4.4]], 2, [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]], [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|Theorem §CB.17.9]], 2; the $z$-axis version with the same signs is the user's Problem Set 6, Problem 4(c)–(d) ([[PHY 513 PS Drill#^ps6-4-c|PS Drill, PS6.4(c)]], [[PHY 513 PS Drill#^ps6-4-d|PS Drill, PS6.4(d)]]).

^sol-px-6-4-2

---

## F. γ matrices, spinors, Dirac fields

### X5.2.1 · Contraction identities in d dimensions
*[variation of PS5.2(a)–(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-2-1]]

> [!success]- Solution
> **Answer.** $\gamma_\mu\gamma^\mu = d$, $\quad\gamma_\mu\slashed k\gamma^\mu = -(d - 2)\slashed k$, $\quad\gamma_\mu\slashed p\slashed q\gamma^\mu = 4\,p\cdot q - (4 - d)\,\slashed p\slashed q$ (times $\mathbb 1$ where needed). At $d = 4$: $4$, $-2\slashed k$, $4\,p\cdot q$.
>
> **Step 1** (no $\gamma$ inside). $\gamma_\mu\gamma^\mu = g_{\mu\nu}\gamma^\nu\gamma^\mu$. $g_{\mu\nu}$ is symmetric, so only the symmetric part of $\gamma^\nu\gamma^\mu$ survives: $= \frac12g_{\mu\nu}\{\gamma^\nu, \gamma^\mu\} = g_{\mu\nu}g^{\nu\mu}\,\mathbb 1 = \delta^\mu{}_\mu\,\mathbb 1 = d\,\mathbb 1$. The number is the spacetime dimension, not the size of the matrices.
>
> **Step 2** (the moving rule). From $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ contracted with $a_\nu$: $\slashed a\gamma^\mu = 2a^\mu - \gamma^\mu\slashed a$, for any vector $a$ (components are numbers and commute with the $\gamma$'s).
>
> **Step 3** (one slash). $\gamma_\mu\slashed k\gamma^\mu = \gamma_\mu(2k^\mu - \gamma^\mu\slashed k) = 2\slashed k - (\gamma_\mu\gamma^\mu)\slashed k = 2\slashed k - d\,\slashed k = -(d - 2)\slashed k$, using $\gamma_\mu k^\mu = \slashed k$ and Step 1.
>
> **Step 4** (two slashes). Move the last $\gamma^\mu$ past $\slashed q$ (Step 2), then use Step 3:
>
> $$
> \gamma_\mu\slashed p\slashed q\gamma^\mu = \gamma_\mu\slashed p(2q^\mu - \gamma^\mu\slashed q) = 2\slashed q\slashed p - (\gamma_\mu\slashed p\gamma^\mu)\slashed q = 2\slashed q\slashed p + (d - 2)\slashed p\slashed q .
> $$
>
> With $\slashed q\slashed p = 2p\cdot q - \slashed p\slashed q$: $= 4p\cdot q - 2\slashed p\slashed q + (d - 2)\slashed p\slashed q = 4p\cdot q - (4 - d)\slashed p\slashed q$.
>
> **Step 5** (checks). $d = 4$ gives the four-dimensional identities. Numerically (numpy) verified in $d = 2$ ($\gamma^0 = \sigma^1$, $\gamma^1 = i\sigma^2$), $d = 3$ ($\gamma^0 = \sigma^3$, $\gamma^{1,2} = i\sigma^{1,2}$) and $d = 4$ (chiral basis), for random vectors.
>
> *Derived here; check:* reduces at $d = 4$ to [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]] (its derivation, step 1, notes $\gamma_\mu\gamma^\mu = d$ as a by-product; the steps are those of its covariant route), with the moving rule of [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]]; drill: [[PHY 513 PS Drill#^ps5-2-a|PS Drill, PS5.2(a)]], Q3, and [[PHY 513 PS Drill#^ps5-2-b|PS Drill, PS5.2(b)]], Q4.

^sol-px-5-2-1

### X5.2.2 · Contractions around γ⁵
*[variation of PS5.2(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-2-2]]

> [!success]- Solution
> **Answer.** $\gamma_\mu\gamma^5\gamma^\mu = -4\gamma^5$ and $\gamma_\mu\gamma^\nu\gamma^5\gamma^\mu = 2\gamma^\nu\gamma^5$.
>
> **Step 1** (first). $\gamma^5\gamma^\mu = -\gamma^\mu\gamma^5$ for every $\mu$, so $\gamma_\mu\gamma^5\gamma^\mu = -\gamma_\mu\gamma^\mu\gamma^5 = -4\gamma^5$, by $\gamma_\mu\gamma^\mu = 4$.
>
> **Step 2** (second). Move $\gamma^5$ to the right end past $\gamma^\mu$ (one sign): $\gamma^\nu\gamma^5\gamma^\mu = -\gamma^\nu\gamma^\mu\gamma^5$. Then
>
> $$
> \gamma_\mu\gamma^\nu\gamma^5\gamma^\mu = -(\gamma_\mu\gamma^\nu\gamma^\mu)\gamma^5 = -(-2\gamma^\nu)\gamma^5 = 2\gamma^\nu\gamma^5 ,
> $$
>
> using the free-index form $\gamma_\mu\gamma^\nu\gamma^\mu = -2\gamma^\nu$ of the one-slash identity. Contracted with $k_\nu$: $\gamma_\mu\slashed k\gamma^5\gamma^\mu = 2\slashed k\gamma^5$.
>
> **Step 3** (reading). Compared with $\gamma_\mu\gamma^\nu\gamma^\mu = -2\gamma^\nu$, the extra $\gamma^5$ costs one sign. Both steps use $\{\gamma^5, \gamma^\mu\} = 0$, a four-dimensional statement ($\gamma^5$ is the product of all four $\gamma$'s). Both identities verified numerically (numpy, chiral basis).
>
> *Derived here; check:* [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]] (the free-index form $\gamma_\mu\gamma^\nu\gamma^\mu = -2\gamma^\nu$ and $\gamma_\mu\gamma^\mu = 4$) and [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]] (anticommutation of $\gamma^5$).

^sol-px-5-2-2

### X5.2.3 · Three traces
*[extension of PS5.2]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-2-3]]

> [!success]- Solution
> **Answer.** $\operatorname{tr}(\slashed p\slashed q) = 4\,p\cdot q$; $\operatorname{tr}(\slashed p\slashed q\slashed k) = 0$; $\operatorname{tr}\bigl((\slashed p + m)\gamma^\mu(\slashed q - m)\gamma_\mu\bigr) = -8\,p\cdot q - 16m^2$.
>
> **Step 1** (two slashes). $\operatorname{tr}(\slashed p\slashed q) = p_\mu q_\nu\operatorname{tr}(\gamma^\mu\gamma^\nu) = p_\mu q_\nu\,4g^{\mu\nu} = 4\,p\cdot q$. (Directly: $\operatorname{tr}(\slashed p\slashed q) = \frac12\operatorname{tr}\{\slashed p, \slashed q\} = \frac12\operatorname{tr}(2p\cdot q\,\mathbb 1)$ by cyclicity, $= 4p\cdot q$.)
>
> **Step 2** (three slashes). An odd number of $\gamma$'s: insert $(\gamma^5)^2 = \mathbb 1$, anticommute one $\gamma^5$ through the three factors ($(-1)^3$), use cyclicity: $\operatorname{tr}(M) = -\operatorname{tr}(M)$, so $\operatorname{tr}(\slashed p\slashed q\slashed k) = 0$.
>
> **Step 3** (expand the last trace into four terms).
>
> $$
> \operatorname{tr}\bigl((\slashed p + m)\gamma^\mu(\slashed q - m)\gamma_\mu\bigr) = \operatorname{tr}(\slashed p\,\gamma^\mu\slashed q\gamma_\mu) - m\operatorname{tr}(\slashed p\,\gamma^\mu\gamma_\mu) + m\operatorname{tr}(\gamma^\mu\slashed q\gamma_\mu) - m^2\operatorname{tr}(\gamma^\mu\gamma_\mu) .
> $$
>
> **Step 4** (contract first, then trace). $\gamma^\mu\slashed q\gamma_\mu = -2\slashed q$ and $\gamma^\mu\gamma_\mu = 4$ (index position of the contracted pair is immaterial). The four terms: $\operatorname{tr}(\slashed p(-2\slashed q)) = -8\,p\cdot q$ (Step 1); $-m\operatorname{tr}(4\slashed p) = 0$ (one $\gamma$); $m\operatorname{tr}(-2\slashed q) = 0$; $-m^2\operatorname{tr}(4\cdot\mathbb 1) = -16m^2$. Sum: $-8\,p\cdot q - 16m^2$.
>
> **Step 5** (check). For $q = p$ on shell, $p^2 = m^2$: $-8m^2 - 16m^2 = -24m^2$; direct: $(\slashed p + m)\gamma^\mu(\slashed p - m)\gamma_\mu = (\slashed p + m)(-2\slashed p - 4m) = -2m^2 - 6m\slashed p - 4m^2$, trace $-24m^2$. All three traces verified numerically (numpy, random vectors, $m = 1.3$).
>
> *Checked against:* [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-3|Theorem §C5a.11.3]] (first two traces, $\operatorname{tr}\mathbb 1 = 4$), [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]] (contractions); the third trace is assembled here from these two boxes.

^sol-px-5-2-3

### X5.3.1 · The forward limit of the Gordon identity
*[extension of PS5.3]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-3-1]]

> [!success]- Solution
> **Answer.** $\bar u^r(p)\gamma^\mu u^s(p) = 2p^\mu\,\delta^{rs}$; at $\mu = 0$ it is $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$.
>
> **Step 1** (the identity applies for any labels). The Gordon identity $\bar u(p')\gamma^\mu u(p) = \bar u(p')\bigl[\frac{(p + p')^\mu}{2m} + \frac{i\sigma^{\mu\nu}q_\nu}{2m}\bigr]u(p)$ uses only $\slashed pu(p) = mu(p)$ and $\bar u(p')\slashed p' = m\bar u(p')$, which hold for each spin label separately; so take $u(p) = u^s(p)$, $\bar u(p') = \bar u^r(p)$.
>
> **Step 2** (forward limit). $p' = p$ gives $q = p' - p = 0$, so the spin term vanishes, and $(p + p')^\mu/2m = p^\mu/m$:
>
> $$
> \bar u^r(p)\gamma^\mu u^s(p) = \frac{p^\mu}{m}\,\bar u^r(p)u^s(p) = \frac{p^\mu}{m}\,2m\,\delta^{rs} = 2p^\mu\,\delta^{rs} .
> $$
>
> **Step 3** ($\mu = 0$). $\bar u^r\gamma^0u^s = u^{r\dagger}\gamma^0\gamma^0u^s = u^{r\dagger}u^s$ (since $(\gamma^0)^2 = \mathbb 1$), and $2p^0\delta^{rs} = 2E_{\mathbf p}\delta^{rs}$: the normalization $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$, recovered.
>
> **Step 4** (reading). $\bar uu = 2m$ is a scalar, $u^\dagger u = 2E_{\mathbf p}$ is the time component of the four-vector $\bar u\gamma^\mu u = 2p^\mu$: its frame dependence is that of $p^0$. A single plane wave carries the current $\propto p^\mu$, pure convection. (Verified numerically for all $r, s, \mu$ at a random $\mathbf p$.)
>
> *Checked against:* [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|Theorem §C5a.10.2]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], and [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-1|§C5a.10, Remark: Why u†u depends on the frame and ūu does not]] (which states this result).

^sol-px-5-3-1

### X5.3.2 · The axial Gordon identity
*[variation of PS5.3]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-3-2]]

> [!success]- Solution
> **Answer.** For on-shell positive-frequency spinors, $m \ne 0$, $q = p' - p$, $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$:
>
> $$
> \bar u(p')\gamma^\mu\gamma^5u(p) = \frac1{2m}\,\bar u(p')\bigl[q^\mu + i\sigma^{\mu\nu}(p + p')_\nu\bigr]\gamma^5u(p) .
> $$
>
> **Step 1** (the two on-shell conditions). $\slashed pu(p) = mu(p)$, and by Hermitian conjugation with $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$, $\bar u(p')\slashed p' = m\bar u(p')$. Each acts only when the slash stands next to its own spinor.
>
> **Step 2** (split in half). Write half of the left side with $u(p) = \frac{\slashed p}mu(p)$ and half with $\bar u(p') = \bar u(p')\frac{\slashed p'}m$:
>
> $$
> \bar u'\gamma^\mu\gamma^5u = \frac1{2m}\,\bar u'\bigl(\gamma^\mu\gamma^5\slashed p + \slashed p'\gamma^\mu\gamma^5\bigr)u ,
> $$
>
> with $\bar u' = \bar u(p')$, $u = u(p)$.
>
> **Step 3** (move $\gamma^5$ to the right). $\gamma^5\slashed p = -\slashed p\gamma^5$, so $\gamma^\mu\gamma^5\slashed p = -\gamma^\mu\slashed p\gamma^5$, and the bracket is $(\slashed p'\gamma^\mu - \gamma^\mu\slashed p)\gamma^5$. This one sign is the only difference from the vector case, where the bracket is $\slashed p'\gamma^\mu + \gamma^\mu\slashed p$.
>
> **Step 4** (symmetric and antisymmetric parts). $\gamma^\mu\gamma^\nu = g^{\mu\nu} - i\sigma^{\mu\nu}$. Contracting with $p_\nu$: $\gamma^\mu\slashed p = p^\mu - i\sigma^{\mu\nu}p_\nu$. In the other order, $\slashed p'\gamma^\mu = p'_\nu\gamma^\nu\gamma^\mu = p'^\mu - i\sigma^{\nu\mu}p'_\nu = p'^\mu + i\sigma^{\mu\nu}p'_\nu$ ($\sigma$ antisymmetric).
>
> **Step 5** (subtract). $\slashed p'\gamma^\mu - \gamma^\mu\slashed p = p'^\mu - p^\mu + i\sigma^{\mu\nu}p'_\nu + i\sigma^{\mu\nu}p_\nu = q^\mu + i\sigma^{\mu\nu}(p + p')_\nu$. Inserting into Step 2 gives the answer. Compared with the vector identity, $(p + p')^\mu$ and $q_\nu$ have exchanged places. Verified numerically (numpy, chiral basis) for random on-shell $p$, $p'$, all four spin pairs and all $\mu$ ($m = 1.3$).
>
> *Derived here; check:* the steps of the first route of [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-9|Theorem §C5a.11.9]] (its derivation, steps 1–4) with one anticommutation of $\gamma^5$ ([[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]]); the split $\gamma^\mu\gamma^\nu = g^{\mu\nu} - i\sigma^{\mu\nu}$ is [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-1|Theorem §C5a.11.1]]; the conjugate condition is [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-10|Theorem §C5a.9.10]]; $\sigma^{\mu\nu}$ normalization: [[§C5a.6 The Dirac Conjugate and the Bilinears#^cau-c5a-6-1|§C5a.6, Caution: Three normalizations of σ^μν]].

^sol-px-5-3-2

### X5.4.1 · The Hamiltonian from T⁰⁰
*[variation of PS5.4(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-4-1]]

> [!success]- Solution
> **Answer.** $T^{00} = \psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$, so $H = \int d^3x\,T^{00} = \int d^3x\,\psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$; this holds for every field configuration, and on solutions it also equals $\int d^3x\,\psi^\dagger\,i\partial_t\psi$.
>
> **Step 1** (the $00$ component). With $\mu = \nu = 0$: $\partial^0 = g^{00}\partial_0 = \partial_t$, $g^{00} = 1$, and $\bar\psi\gamma^0 = \psi^\dagger(\gamma^0)^2 = \psi^\dagger$, so $T^{00} = i\bar\psi\gamma^0\partial^0\psi - \mathcal L = i\psi^\dagger\partial_t\psi - \mathcal L$.
>
> **Step 2** (split $\mathcal L$ into time and space parts). $\mathcal L = \bar\psi(i\gamma^0\partial_0 + i\gamma^j\partial_j - m)\psi = i\psi^\dagger\partial_t\psi + i\bar\psi\gamma^j\partial_j\psi - m\bar\psi\psi$, using $\bar\psi\gamma^0 = \psi^\dagger$ again.
>
> **Step 3** (subtract). The two $i\psi^\dagger\partial_t\psi$ cancel identically (no equation of motion used):
>
> $$
> T^{00} = -i\bar\psi\gamma^j\partial_j\psi + m\bar\psi\psi = \psi^\dagger\bigl(-i\gamma^0\gamma^j\partial_j + m\gamma^0\bigr)\psi = \psi^\dagger\bigl(-i\boldsymbol\alpha\cdot\nabla + \beta m\bigr)\psi ,
> $$
>
> with $\bar\psi = \psi^\dagger\gamma^0$, $\alpha^j = \gamma^0\gamma^j$, $\beta = \gamma^0$, and $\partial_j = \partial/\partial x^j$ the components of $\nabla$ (lower index: no sign). Integrating gives $H$. So the hypothesis "on solutions" is not needed for this form.
>
> **Step 4** (on solutions). $\mathcal L = \bar\psi(i\slashed\partial - m)\psi = 0$ when $\psi$ solves the Dirac equation, so Step 1 gives $T^{00} = i\psi^\dagger\partial_t\psi$; multiplying the Dirac equation by $\gamma^0$, $i\partial_t\psi = (-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi = H_{\text{s.p.}}\psi$, so the two forms agree there. $\boldsymbol\alpha$ and $\beta$ are Hermitian ($(\gamma^0\gamma^j)^\dagger = \gamma^{j\dagger}\gamma^0 = -\gamma^j\gamma^0 = \gamma^0\gamma^j$), and $H$ is real for fields falling off at infinity.
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|Theorem §C5a.8.2]] (steps 1–6 of its derivation), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-6|Theorem §C5a.8.6]] (step 3: $T^{00} = \mathcal H$ identically), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-5|Theorem §C5a.8.5]]; drill: [[PHY 513 PS Drill#^ps5-4-b|PS Drill, PS5.4(b)]].

^sol-px-5-4-1

### X5.4.2 · The canonical Dirac tensor is not symmetric
*[variation of PS5.4(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-4-2]]

> [!success]- Solution
> **Answer.** No. On solutions, $T^{0i} - T^{i0} = -\varepsilon^{ijk}\psi^\dagger\Sigma^k\partial_j\psi + m\,\psi^\dagger\gamma^i\psi$ ($\Sigma^k = \operatorname{diag}(\sigma^k, \sigma^k)$). For the solution with initial datum $\psi(0, \mathbf x) = e^{-|\mathbf x|^2/2}(1, 0, 1, 0)^{\mathsf T}$, at $t = 0$: $T^{01} - T^{10} = 2x^2e^{-|\mathbf x|^2}$ ($x^2$ the second coordinate), nonzero off the plane $x^2 = 0$.
>
> **Step 1** (the two components). $T^{0i} = i\bar\psi\gamma^0\partial^i\psi - g^{0i}\mathcal L = i\psi^\dagger\partial^i\psi = -i\psi^\dagger\partial_i\psi$ ($g^{0i} = 0$, $\partial^i = -\partial_i$). $T^{i0} = i\bar\psi\gamma^i\partial^0\psi - g^{i0}\mathcal L = i\bar\psi\gamma^i\partial_t\psi$.
>
> **Step 2** (eliminate $\partial_t$ with the Dirac equation). $i\partial_t\psi = (-i\gamma^0\gamma^j\partial_j + m\gamma^0)\psi$, i.e. $\partial_t\psi = (-\gamma^0\gamma^j\partial_j - im\gamma^0)\psi$. With $\bar\psi = \psi^\dagger\gamma^0$ and $\gamma^0\gamma^i\gamma^0 = -\gamma^i$:
>
> $$
> T^{i0} = i\psi^\dagger\gamma^0\gamma^i\bigl(-\gamma^0\gamma^j\partial_j - im\gamma^0\bigr)\psi = i\psi^\dagger\gamma^i\gamma^j\partial_j\psi - m\,\psi^\dagger\gamma^i\psi .
> $$
>
> **Step 3** (the product of two spatial $\gamma$'s). In the chiral basis $\gamma^i\gamma^j = \operatorname{diag}(-\sigma^i\sigma^j, -\sigma^i\sigma^j)$ and $\sigma^i\sigma^j = \delta^{ij} + i\varepsilon^{ijk}\sigma^k$, so $\gamma^i\gamma^j = -\delta^{ij} - i\varepsilon^{ijk}\Sigma^k$ (basis-free: $g^{ij} - i\sigma^{ij}$). Hence $i\psi^\dagger\gamma^i\gamma^j\partial_j\psi = -i\psi^\dagger\partial_i\psi + \varepsilon^{ijk}\psi^\dagger\Sigma^k\partial_j\psi$, and $T^{i0} = T^{0i} + \varepsilon^{ijk}\psi^\dagger\Sigma^k\partial_j\psi - m\,\psi^\dagger\gamma^i\psi$: the formula of the answer.
>
> **Step 4** (a single plane wave is not enough). For $\psi = u^s(p)e^{-ip\cdot x}$, $\partial^\nu\psi = -ip^\nu\psi$ and $T^{\mu\nu} = p^\nu\,\bar u\gamma^\mu u = 2p^\mu p^\nu$ (X5.3.1): symmetric. The antisymmetric part needs a spin density that varies in space.
>
> **Step 5** (the example). The Dirac equation is first order in time, $i\partial_t\psi = H_{\text{s.p.}}\psi$, so every smooth datum $\psi(0, \mathbf x)$ defines a solution, and Step 2 used only the equation at $t = 0$. Take $\psi(0, \mathbf x) = f(\mathbf x)\,w$, $f = e^{-|\mathbf x|^2/2}$, $w = (1, 0, 1, 0)^{\mathsf T}$ ($\psi_L = \psi_R = (1, 0)^{\mathsf T}$, spin up along $z$). Then $\Sigma^3w = w$, $w^\dagger\Sigma^3w = 2$, $w^\dagger\Sigma^{1,2}w = 0$, so $\psi^\dagger\Sigma^k\partial_j\psi = 2\delta^{k3}f\,\partial_jf = \delta^{k3}\partial_j(f^2)$. The mass term vanishes: $\psi^\dagger\gamma^i\psi = f^2(\psi_L^\dagger\sigma^i\psi_R - \psi_R^\dagger\sigma^i\psi_L) = 0$ for $\psi_L = \psi_R$. Hence $T^{0i} - T^{i0} = -\varepsilon^{ij3}\partial_j(f^2)$:
>
> $$
> T^{01} - T^{10} = -\partial_2(f^2) = 2x^2e^{-|\mathbf x|^2}, \qquad T^{02} - T^{20} = +\partial_1(f^2) = -2x^1e^{-|\mathbf x|^2}, \qquad T^{03} - T^{30} = 0 .
> $$
>
> **Step 6** (reading). Here $T^{0i} - T^{i0} = -(\nabla\times\mathbf s)^i$ with the spin density $\mathbf s = \frac12\psi^\dagger\boldsymbol\Sigma\psi = f^2\hat{\mathbf z}$: the antisymmetric part is the divergence of the spin current, which the Belinfante tensor removes. The value is real and is the same for the tensor of the symmetrized Lagrangian. (Step 3's formula verified numerically for a random datum $w\,e^{i\mathbf k\cdot\mathbf x}$; Step 5 at $\mathbf x = (0.3, 0.5, 0.2)$, both tensors; numpy.)
>
> *Derived here; check:* the by-product of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-5|Theorem §C5a.8.5]] (its derivation: $T^{\mu\nu} - T^{\nu\mu} = i\bar\psi(\gamma^\mu\partial^\nu - \gamma^\nu\partial^\mu)\psi \ne 0$), [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-2|Theorem §C1b.8.2]] (antisymmetric part $= -\partial_\mu\mathcal S^{\mu\nu\rho}$), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-8|Theorem §C5a.8.8]] (the spin current), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-9|Theorem §C5a.8.9]] (the symmetric tensor); the elimination of $\partial_t$ is step 6 of the derivation of [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|Theorem §C5a.8.2]].

^sol-px-5-4-2

### X5.5.1 · γ⁵ in the Dirac basis
*[variation of PS5.5(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-5-1]]

> [!success]- Solution
> **Answer.** $\gamma^5_D = U_D\gamma^5_WU_D^\dagger = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$: off-diagonal, while $\gamma^0_D = \operatorname{diag}(\mathbb 1, -\mathbb 1)$ is diagonal.
>
> **Step 1** ($U_D\gamma^5_W$). In $2\times2$ blocks, $U_D\gamma^5_W = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1&\mathbb 1\\-\mathbb 1&\mathbb 1\end{pmatrix}\begin{pmatrix}-\mathbb 1&0\\0&\mathbb 1\end{pmatrix} = \frac1{\sqrt2}\begin{pmatrix}-\mathbb 1&\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix}$.
>
> **Step 2** (times $U_D^\dagger$). $U_D^\dagger = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1&-\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix}$, so
>
> $$
> \gamma^5_D = \frac12\begin{pmatrix}-\mathbb 1&\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix}\begin{pmatrix}\mathbb 1&-\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix} = \frac12\begin{pmatrix}-\mathbb 1 + \mathbb 1 & \mathbb 1 + \mathbb 1\\ \mathbb 1 + \mathbb 1 & -\mathbb 1 + \mathbb 1\end{pmatrix} = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix} .
> $$
>
> **Step 3** (check with the definition). Conjugation preserves products, so $\gamma^5_D = i\gamma^0_D\gamma^1_D\gamma^2_D\gamma^3_D$. Explicitly, $\gamma^i_D = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$ gives $\gamma^1_D\gamma^2_D = \operatorname{diag}(-\sigma^1\sigma^2, -\sigma^1\sigma^2) = -i\operatorname{diag}(\sigma^3, \sigma^3)$, then $\gamma^1_D\gamma^2_D\gamma^3_D = -i\begin{pmatrix}0&(\sigma^3)^2\\-(\sigma^3)^2&0\end{pmatrix} = \begin{pmatrix}0&-i\mathbb 1\\i\mathbb 1&0\end{pmatrix}$; multiplying by $\gamma^0_D = \operatorname{diag}(\mathbb 1, -\mathbb 1)$ gives $\begin{pmatrix}0&-i\mathbb 1\\-i\mathbb 1&0\end{pmatrix}$, and by $i$: $\begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$. Equal. (Also verified numerically.)
>
> **Step 4** (reading). $\gamma^5_D$ anticommutes with $\gamma^0_D$ and its eigenvectors are $\frac1{\sqrt2}(\chi, \pm\chi)$: in the Dirac basis chirality mixes upper and lower components. $\gamma^0$ and $\gamma^5$ cannot both be diagonal in one basis; the Dirac basis diagonalizes $\gamma^0$ (rest energy, nonrelativistic limit), the chiral basis $\gamma^5$ (Lorentz structure).
>
> *Checked against:* [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]] (states $\gamma^5_D = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ and $U_D$; the user's Problem Set 6, Problem 3(b)), [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-17|Theorem §CB.12.17]], [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^def-cb-12-14|Def. §CB.12.14]].

^sol-px-5-5-1

### X5.5.2 · The ε trace
*[extension of PS5.5(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-5-2]]

> [!success]- Solution
> **Answer.** $\operatorname{tr}(\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu\gamma^5) = -4i\,\varepsilon^{\kappa\lambda\mu\nu}$ ($\varepsilon^{0123} = +1$); the convention-free value is $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = -4i$.
>
> **Step 1** (distinct indices). If $\kappa\lambda\mu\nu$ are distinct, each of the 24 terms of $\gamma^{[\kappa}\gamma^\lambda\gamma^\mu\gamma^{\nu]}$, reordered by anticommuting distinct $\gamma$'s, equals the plain product (the sign of the permutation appears twice), so $\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^{[\kappa}\gamma^\lambda\gamma^\mu\gamma^{\nu]} = -i\varepsilon^{\kappa\lambda\mu\nu}\gamma^5$.
>
> **Step 2** (multiply by $\gamma^5$ and trace). $\operatorname{tr}(\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu\gamma^5) = -i\varepsilon^{\kappa\lambda\mu\nu}\operatorname{tr}\bigl((\gamma^5)^2\bigr) = -i\varepsilon^{\kappa\lambda\mu\nu}\operatorname{tr}\mathbb 1 = -4i\,\varepsilon^{\kappa\lambda\mu\nu}$.
>
> **Step 3** (a repeated index). Then $\varepsilon^{\kappa\lambda\mu\nu} = 0$. On the left, anticommute one copy of the repeated $\gamma^\alpha$ next to the other (signs only), replace the pair by $(\gamma^\alpha)^2 = g^{\alpha\alpha}$: what remains is $\pm g^{\alpha\alpha}\operatorname{tr}(\gamma^\rho\gamma^\sigma\gamma^5)$, and $\operatorname{tr}(\gamma^\rho\gamma^\sigma\gamma^5) = 0$. So the identity holds for all index values.
>
> **Step 4** (convention-free value). From $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, multiplying by $-i$: $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$, so $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5) = -i\operatorname{tr}((\gamma^5)^2) = -4i$, whatever sign is given to $\varepsilon^{0123}$. With $\varepsilon^{0123} = +1$ Step 2 gives the same $-4i$; with Peskin–Schroeder's stated $\varepsilon^{0123} = -1$ the covariant formula would read $+4i\varepsilon^{\kappa\lambda\mu\nu}$. (All 256 index combinations verified numerically.)
>
> *Checked against:* [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-4|Theorem §C5a.11.4]] (the result and its derivation, steps 3–6), [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-5|Theorem §C5a.11.5]] (the antisymmetrized product), [[§C5a.11 Gamma-Matrix Technology#^cau-c5a-11-1|§C5a.11, Caution: The sign of the ε trace across sources]].

^sol-px-5-5-2

### X5.5.3 · Reducing a product of three γ's
*[extension of PS5.5(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-5-3]]

> [!success]- Solution
> **Answer.**
>
> $$
> \gamma^\mu\gamma^\nu\gamma^\rho = g^{\mu\nu}\gamma^\rho - g^{\mu\rho}\gamma^\nu + g^{\nu\rho}\gamma^\mu + i\varepsilon^{\mu\nu\rho\kappa}\gamma_\kappa\gamma^5 .
> $$
>
> **Step 1** (rewrite each permutation). Let $A = \gamma^\mu\gamma^\nu\gamma^\rho$. Using $\gamma^\alpha\gamma^\beta = 2g^{\alpha\beta} - \gamma^\beta\gamma^\alpha$ one swap at a time:
> - $\gamma^\mu\gamma^\rho\gamma^\nu = 2g^{\nu\rho}\gamma^\mu - A$;
> - $\gamma^\nu\gamma^\mu\gamma^\rho = 2g^{\mu\nu}\gamma^\rho - A$;
> - $\gamma^\nu\gamma^\rho\gamma^\mu = 2g^{\mu\rho}\gamma^\nu - \gamma^\nu\gamma^\mu\gamma^\rho = 2g^{\mu\rho}\gamma^\nu - 2g^{\mu\nu}\gamma^\rho + A$;
> - $\gamma^\rho\gamma^\mu\gamma^\nu = 2g^{\mu\rho}\gamma^\nu - \gamma^\mu\gamma^\rho\gamma^\nu = 2g^{\mu\rho}\gamma^\nu - 2g^{\nu\rho}\gamma^\mu + A$;
> - $\gamma^\rho\gamma^\nu\gamma^\mu = 2g^{\nu\rho}\gamma^\mu - \gamma^\nu\gamma^\rho\gamma^\mu = 2g^{\nu\rho}\gamma^\mu - 2g^{\mu\rho}\gamma^\nu + 2g^{\mu\nu}\gamma^\rho - A$.
>
> **Step 2** (antisymmetrize). $6\gamma^{[\mu}\gamma^\nu\gamma^{\rho]} = A - \gamma^\mu\gamma^\rho\gamma^\nu - \gamma^\nu\gamma^\mu\gamma^\rho + \gamma^\nu\gamma^\rho\gamma^\mu + \gamma^\rho\gamma^\mu\gamma^\nu - \gamma^\rho\gamma^\nu\gamma^\mu$. Inserting Step 1, the $A$'s add to $6A$; the $g^{\nu\rho}\gamma^\mu$ terms to $-2 - 2 - 2 = -6$; the $g^{\mu\nu}\gamma^\rho$ terms to $-2 - 2 - 2 = -6$; the $g^{\mu\rho}\gamma^\nu$ terms to $+2 + 2 + 2 = +6$. Dividing by 6:
>
> $$
> \gamma^{[\mu}\gamma^\nu\gamma^{\rho]} = A - g^{\mu\nu}\gamma^\rho + g^{\mu\rho}\gamma^\nu - g^{\nu\rho}\gamma^\mu .
> $$
>
> **Step 3** (insert the given identity). Solve for $A$ and use $\gamma^{[\mu}\gamma^\nu\gamma^{\rho]} = i\varepsilon^{\mu\nu\rho\kappa}\gamma_\kappa\gamma^5$: the answer. Every term is $\gamma^\mu$ or $\gamma_\kappa\gamma^5$ times numbers built from $g$ and $\varepsilon$ (odd number of $\gamma$'s: only odd basis elements).
>
> **Step 4** (checks by contraction). With $g_{\mu\nu}$: left $\gamma_\mu\gamma^\mu\gamma^\rho = 4\gamma^\rho$; right $4\gamma^\rho - \gamma^\rho + \gamma^\rho + 0 = 4\gamma^\rho$ ($\varepsilon$ against the symmetric $g$ vanishes). With $g_{\mu\rho}$: left $\gamma_\mu\gamma^\nu\gamma^\mu = -2\gamma^\nu$; right $\gamma^\nu - 4\gamma^\nu + \gamma^\nu = -2\gamma^\nu$. Both agree with the contraction identities. The full identity verified numerically for all 64 index triples.
>
> *Checked against:* [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-8|Theorem §C5a.11.8]] (step 3 of its derivation states $\gamma^\lambda\gamma^\mu\gamma^\nu = \gamma^{[\lambda\mu\nu]} + g^{\lambda\mu}\gamma^\nu - g^{\lambda\nu}\gamma^\mu + g^{\mu\nu}\gamma^\lambda$, case-checked under [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-9|Theorem §C5a.8.9]]), [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-6|Theorem §C5a.11.6]], [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]].

^sol-px-5-5-3

### X5.6.1 · Helicity spinors along −z and +x
*[variation of PS5.6]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-6-1]]

> [!success]- Solution
> **Answer.** With $\xi_+ = (\cos\frac\theta2, e^{i\varphi}\sin\frac\theta2)^{\mathsf T}$, $\xi_- = (-e^{-i\varphi}\sin\frac\theta2, \cos\frac\theta2)^{\mathsf T}$: for $\hat{\mathbf p} = -\hat{\mathbf z}$, $\xi_+ = (0, 1)^{\mathsf T}$, $\xi_- = (-1, 0)^{\mathsf T}$; for $\hat{\mathbf p} = +\hat{\mathbf x}$, $\xi_+ = \frac1{\sqrt2}(1, 1)^{\mathsf T}$, $\xi_- = \frac1{\sqrt2}(-1, 1)^{\mathsf T}$.
>
> **Step 1** (the phase convention). The problem set's solution, with phases fixed so that $\xi_+ = (1, 0)^{\mathsf T}$, $\xi_- = (0, 1)^{\mathsf T}$ at $\theta = 0$, is the pair quoted in the answer (valid for $0 \le \theta \le \pi$, checked directly there).
>
> **Step 2** ($-\hat{\mathbf z}$: $\theta = \pi$, $\varphi = 0$). $\cos\frac\pi2 = 0$, $\sin\frac\pi2 = 1$, $e^{\pm i0} = 1$: $\xi_+ = (0, 1)^{\mathsf T}$, $\xi_- = (-1, 0)^{\mathsf T}$. Check: $\hat{\mathbf p}\cdot\boldsymbol\sigma = -\sigma^3 = \operatorname{diag}(-1, 1)$, so $-\sigma^3(0, 1)^{\mathsf T} = (0, 1)^{\mathsf T}$ (eigenvalue $+1$) and $-\sigma^3(-1, 0)^{\mathsf T} = (1, 0)^{\mathsf T} = -(-1, 0)^{\mathsf T}$ (eigenvalue $-1$). At $\theta = \pi$ the general formula gives $\xi_+ = (0, e^{i\varphi})^{\mathsf T}$: the phase depends on the meaningless $\varphi$; the question fixes $\varphi = 0$.
>
> **Step 3** ($+\hat{\mathbf x}$: $\theta = \frac\pi2$, $\varphi = 0$). $\cos\frac\pi4 = \sin\frac\pi4 = \frac1{\sqrt2}$: $\xi_+ = \frac1{\sqrt2}(1, 1)^{\mathsf T}$, $\xi_- = \frac1{\sqrt2}(-1, 1)^{\mathsf T}$.
>
> **Step 4** (eigenvalue equation for $+\hat{\mathbf x}$). $\hat{\mathbf p}\cdot\frac{\boldsymbol\sigma}2 = \frac12\sigma^1 = \frac12\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which swaps the two components:
>
> $$
> \tfrac12\sigma^1\,\tfrac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix} = +\tfrac12\cdot\tfrac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}, \qquad \tfrac12\sigma^1\,\tfrac1{\sqrt2}\begin{pmatrix}-1\\1\end{pmatrix} = \tfrac12\cdot\tfrac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix} = -\tfrac12\cdot\tfrac1{\sqrt2}\begin{pmatrix}-1\\1\end{pmatrix} .
> $$
>
> Both are normalized ($\frac12(1 + 1) = 1$) and orthogonal ($\frac12(-1 + 1) = 0$). (All four eigenvalue equations verified numerically.)
>
> *Checked against:* [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-11|Theorem §C5a.10.11]] (the same formula; the user's Problem Set 5, Problem 6), [[§C5a.10 Normalization, Spin Sums and Helicity#^cau-c5a-10-2|§C5a.10, Caution: No phase convention is smooth on the whole sphere]]; drill: [[PHY 513 PS Drill#^ps5-6|PS Drill, PS5.6]].

^sol-px-5-6-1

### X5.6.2 · High energy: helicity becomes chirality
*[extension of PS5.6]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-5-6-2]]

> [!success]- Solution
> **Answer.** $u_+ \to \sqrt{2E_{\mathbf p}}\,(0, \xi_+)$ lies in the lower, right-handed half ($\gamma^5 = +1$); $u_- \to \sqrt{2E_{\mathbf p}}\,(\xi_-, 0)$ lies in the upper, left-handed half ($\gamma^5 = -1$). Positive helicity becomes right chirality, negative helicity left chirality; the small half is suppressed by $m/2E_{\mathbf p}$.
>
> **Step 1** (the square roots act as numbers). $p\cdot\sigma = E_{\mathbf p} - |\mathbf p|\,\hat{\mathbf p}\cdot\boldsymbol\sigma$ and $p\cdot\bar\sigma = E_{\mathbf p} + |\mathbf p|\,\hat{\mathbf p}\cdot\boldsymbol\sigma$. On $\xi_\pm$, $\hat{\mathbf p}\cdot\boldsymbol\sigma = \pm1$, so $p\cdot\sigma\,\xi_\pm = (E_{\mathbf p} \mp |\mathbf p|)\xi_\pm$, $p\cdot\bar\sigma\,\xi_\pm = (E_{\mathbf p} \pm |\mathbf p|)\xi_\pm$; the positive square root of a positive Hermitian matrix has the same eigenvectors and the square roots of the eigenvalues:
>
> $$
> u_\pm(p) = \begin{pmatrix}\sqrt{E_{\mathbf p} \mp |\mathbf p|}\;\xi_\pm\\ \sqrt{E_{\mathbf p} \pm |\mathbf p|}\;\xi_\pm\end{pmatrix} .
> $$
>
> **Step 2** (the two amplitudes for $E_{\mathbf p} \gg m$). $|\mathbf p| = \sqrt{E_{\mathbf p}^2 - m^2} = E_{\mathbf p} - \frac{m^2}{2E_{\mathbf p}} + \dots$, so $\sqrt{E_{\mathbf p} + |\mathbf p|} = \sqrt{2E_{\mathbf p}}\,(1 + O(m^2/E_{\mathbf p}^2))$, while $\sqrt{E_{\mathbf p} - |\mathbf p|} = \sqrt{\frac{E_{\mathbf p}^2 - |\mathbf p|^2}{E_{\mathbf p} + |\mathbf p|}} = \frac{m}{\sqrt{E_{\mathbf p} + |\mathbf p|}} \approx \frac{m}{\sqrt{2E_{\mathbf p}}}$. The ratio small/large is $m/(E_{\mathbf p} + |\mathbf p|) \approx m/2E_{\mathbf p} \to 0$.
>
> **Step 3** (the limits). For $u_+$ the upper entry has $\sqrt{E - |\mathbf p|}$ and drops out: $u_+ \to \sqrt{2E_{\mathbf p}}\,(0, \xi_+)$. For $u_-$ the lower entry has $\sqrt{E - |\mathbf p|}$: $u_- \to \sqrt{2E_{\mathbf p}}\,(\xi_-, 0)$.
>
> **Step 4** (chirality). In the chiral basis $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$: the lower half ($\psi_R$) has $\gamma^5 = +1$, the upper ($\psi_L$) $\gamma^5 = -1$. So $\gamma^5u_\pm \to \pm u_\pm$: helicity $\pm\frac12$ becomes chirality $\pm1$, exactly at $m = 0$. (Numerically, at $E/m = 10$ and $1000$ the small half relative to $\sqrt{2E}$ is $5.0\times10^{-2}$ and $5.0\times10^{-4}$, i.e. $m/2E$.)
>
> *Checked against:* [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-12|Theorem §C5a.10.12]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-14|Theorem §C5a.10.14]], 1–2, [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], 1.

^sol-px-5-6-2

### X6.3.1 · The v spinor in the Dirac basis
*[variation of PS6.3(c)–(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-3-1]]

> [!success]- Solution
> **Answer.** $v_D(p) = U_Dv(p) = -\dfrac{1}{\sqrt{E_{\mathbf p} + m}}\begin{pmatrix}\boldsymbol\sigma\cdot\mathbf p\;\eta\\ (E_{\mathbf p} + m)\,\eta\end{pmatrix}$ and $\bar v_Dv_D = -2m$ for $\eta^\dagger\eta = 1$ ($\eta$ is the two-spinor, not a rapidity).
>
> **Step 1** (apply $U_D$). With $v = (a, b)$, $a = \sqrt{p\cdot\sigma}\,\eta$, $b = -\sqrt{p\cdot\bar\sigma}\,\eta$, and $U_D = \frac1{\sqrt2}\begin{pmatrix}\mathbb 1&\mathbb 1\\-\mathbb 1&\mathbb 1\end{pmatrix}$:
>
> $$
> v_D = \frac1{\sqrt2}\begin{pmatrix}a + b\\ -a + b\end{pmatrix} = \frac1{\sqrt2}\begin{pmatrix}\bigl(\sqrt{p\cdot\sigma} - \sqrt{p\cdot\bar\sigma}\bigr)\eta\\ -\bigl(\sqrt{p\cdot\sigma} + \sqrt{p\cdot\bar\sigma}\bigr)\eta\end{pmatrix} .
> $$
>
> **Step 2** (explicit square roots). $\sqrt{p\cdot\sigma} = \frac{p\cdot\sigma + m}{\sqrt{2(E_{\mathbf p} + m)}}$, $\sqrt{p\cdot\bar\sigma} = \frac{p\cdot\bar\sigma + m}{\sqrt{2(E_{\mathbf p} + m)}}$, with $p\cdot\sigma = E_{\mathbf p} - \boldsymbol\sigma\cdot\mathbf p$, $p\cdot\bar\sigma = E_{\mathbf p} + \boldsymbol\sigma\cdot\mathbf p$. The $m$'s cancel in the difference: $\sqrt{p\cdot\sigma} - \sqrt{p\cdot\bar\sigma} = \frac{-2\boldsymbol\sigma\cdot\mathbf p}{\sqrt{2(E_{\mathbf p} + m)}}$; the sum is $\frac{2(E_{\mathbf p} + m)}{\sqrt{2(E_{\mathbf p} + m)}}$.
>
> **Step 3** (collect). The prefactor $\frac1{\sqrt2}\cdot\frac1{\sqrt{2(E_{\mathbf p} + m)}} = \frac1{2\sqrt{E_{\mathbf p} + m}}$, so the upper block is $-\frac{\boldsymbol\sigma\cdot\mathbf p\,\eta}{\sqrt{E_{\mathbf p} + m}}$ and the lower $-\frac{(E_{\mathbf p} + m)\eta}{\sqrt{E_{\mathbf p} + m}}$: the answer.
>
> **Step 4** (normalization). $\gamma^0_D = \operatorname{diag}(\mathbb 1, -\mathbb 1)$ and $(\boldsymbol\sigma\cdot\mathbf p)^\dagger = \boldsymbol\sigma\cdot\mathbf p$, so $\bar v_D = v_D^\dagger\gamma^0_D = -\frac1{\sqrt{E_{\mathbf p} + m}}\bigl(\eta^\dagger\boldsymbol\sigma\cdot\mathbf p,\ -(E_{\mathbf p} + m)\eta^\dagger\bigr)$ and
>
> $$
> \bar v_Dv_D = \frac{1}{E_{\mathbf p} + m}\,\eta^\dagger\Bigl((\boldsymbol\sigma\cdot\mathbf p)^2 - (E_{\mathbf p} + m)^2\Bigr)\eta = \frac{|\mathbf p|^2 - E_{\mathbf p}^2 - 2E_{\mathbf p}m - m^2}{E_{\mathbf p} + m} = \frac{-2m(E_{\mathbf p} + m)}{E_{\mathbf p} + m} = -2m ,
> $$
>
> using $(\boldsymbol\sigma\cdot\mathbf p)^2 = |\mathbf p|^2$, $|\mathbf p|^2 = E_{\mathbf p}^2 - m^2$, $\eta^\dagger\eta = 1$. The value is that of the chiral basis: $U_D$ is unitary, so $\bar\psi\chi$ is basis independent.
>
> **Step 5** (reading). At rest $v_D = -\sqrt{2m}\,(0, \eta)$: in the Dirac basis the negative-frequency solutions live in the lower components (the $\gamma^0_D = -1$ eigenspace), as $u_D$ lives in the upper ones; at rest $(\gamma^0_D + \mathbb 1)\,v_D = 0$, i.e. $(\slashed p + m)v = 0$ for $p = (m, \mathbf 0)$. (The formula and $\bar v_Dv_D = -2m$ verified numerically for both $\eta^s$ at a random $\mathbf p$.)
>
> *Derived here; check:* the computation of $u_D$ in [[§C5a.9 Plane-Wave Solutions#^ex-c5a-9-1|Example §C5a.9.1]] (the user's Problem Set 6, Problem 3(c)–(d)) with the sign of the lower Weyl block reversed; [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-11|Theorem §C5a.9.11]] ($v$), [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-6|Theorem §C5a.9.6]] (square roots), [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|Theorem §C5a.10.4]] ($\bar vv = -2m$), [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]] ($U_D$).

^sol-px-6-3-1

### X6.3.2 · Boost generators in the Dirac basis
*[variation of PS6.3(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-3-2]]

> [!success]- Solution
> **Answer.** $S^{0i}_D = \dfrac i2\begin{pmatrix}0&\sigma^i\\\sigma^i&0\end{pmatrix}$: off-diagonal, not block diagonal. The rotation generators stay block diagonal, $S^{ij}_D = \frac12\varepsilon^{ijk}\operatorname{diag}(\sigma^k, \sigma^k)$.
>
> **Step 1** (directly from the Dirac matrices). $\gamma^0_D$ and $\gamma^i_D$ anticommute, so $[\gamma^0_D, \gamma^i_D] = 2\gamma^0_D\gamma^i_D$ and
>
> $$
> S^{0i}_D = \frac i4[\gamma^0_D, \gamma^i_D] = \frac i2\gamma^0_D\gamma^i_D = \frac i2\begin{pmatrix}\mathbb 1&0\\0&-\mathbb 1\end{pmatrix}\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix} = \frac i2\begin{pmatrix}0&\sigma^i\\\sigma^i&0\end{pmatrix} .
> $$
>
> **Step 2** (by conjugation, second route). $S^{0i}_W = -\frac i2\operatorname{diag}(\sigma^i, -\sigma^i)$. For a block $A$, $U_D\operatorname{diag}(A, -A)U_D^\dagger = \frac12\begin{pmatrix}A&-A\\-A&-A\end{pmatrix}\begin{pmatrix}\mathbb 1&-\mathbb 1\\\mathbb 1&\mathbb 1\end{pmatrix} = \begin{pmatrix}0&-A\\-A&0\end{pmatrix}$, so $S^{0i}_D = -\frac i2\begin{pmatrix}0&-\sigma^i\\-\sigma^i&0\end{pmatrix}$, the same. For a block-scalar $\operatorname{diag}(A, A)$, $U_D$ commutes with it, so $S^{ij}_D = S^{ij}_W$.
>
> **Step 3** (third route, via $\gamma^5$). $K_i = i\gamma^5J_i$ in every basis. With $J_i = \frac12\operatorname{diag}(\sigma^i, \sigma^i)$ (unchanged, Step 2) and $\gamma^5_D = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$ (X5.5.1): $i\gamma^5_DJ_i = \frac i2\begin{pmatrix}0&\sigma^i\\\sigma^i&0\end{pmatrix}$. Same.
>
> **Step 4** (reading). Boosts mix the upper and lower Dirac components: the Dirac basis does not separate the two Lorentz-invariant halves (those are the $\gamma^5$ eigenspaces, $\frac1{\sqrt2}(\chi, \pm\chi)$ here). Block diagonality of all six generators is special to the basis that diagonalizes $\gamma^5$, the chiral one. (All six generators verified numerically.)
>
> *Derived here; check:* [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-1|Theorem §C5a.3.1]] conjugated with $U_D$ of [[§C5a.5 Chirality and Weyl Spinors#^ex-c5a-5-1|Example §C5a.5.1]], and [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-4|Theorem §CB.18.4]] ($K_i = i\gamma^5J_i$); [[§CB.14 The Spin Group and the Double Cover Spin(V) → SO(V)#^def-cb-14-16|Def. §CB.14.16]].

^sol-px-6-3-2

### X6.5.1 · The bilinears under a finite chiral rotation
*[extension of PS6.5(b)–(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-5-1]]

> [!success]- Solution
> **Answer.** $\mathsf S \to \cos2\alpha\,\mathsf S + \sin2\alpha\,\mathsf P$, $\quad\mathsf P \to -\sin2\alpha\,\mathsf S + \cos2\alpha\,\mathsf P$, $\quad\mathsf A^\mu \to \mathsf A^\mu$: $(\mathsf S, \mathsf P)$ is rotated by the angle $2\alpha$, $\mathsf A^\mu$ (like $\mathsf V^\mu$) is invariant.
>
> **Step 1** (the tools). $\bar\psi \to \bar\psi\,e^{i\alpha\gamma^5}$ (same sign in the exponent); $e^{i\alpha\gamma^5}\gamma^\mu = \gamma^\mu e^{-i\alpha\gamma^5}$ (one sign per power of $\gamma^5$ in the series); $\gamma^5$ commutes with $e^{i\alpha\gamma^5}$; and since $(\gamma^5)^2 = \mathbb 1$, $e^{2i\alpha\gamma^5} = \cos2\alpha\,\mathbb 1 + i\sin2\alpha\,\gamma^5$.
>
> **Step 2** ($\mathsf S$). $\bar\psi e^{i\alpha\gamma^5}e^{i\alpha\gamma^5}\psi = \bar\psi e^{2i\alpha\gamma^5}\psi = \cos2\alpha\,\bar\psi\psi + \sin2\alpha\,\bar\psi\,i\gamma^5\psi = \cos2\alpha\,\mathsf S + \sin2\alpha\,\mathsf P$.
>
> **Step 3** ($\mathsf P$). $\bar\psi e^{i\alpha\gamma^5}\,i\gamma^5\,e^{i\alpha\gamma^5}\psi = i\bar\psi\gamma^5e^{2i\alpha\gamma^5}\psi = i\bar\psi\gamma^5(\cos2\alpha + i\sin2\alpha\,\gamma^5)\psi = \cos2\alpha\,\bar\psi\,i\gamma^5\psi - \sin2\alpha\,\bar\psi\psi = \cos2\alpha\,\mathsf P - \sin2\alpha\,\mathsf S$, using $i\cdot i = -1$ and $(\gamma^5)^2 = \mathbb 1$.
>
> **Step 4** ($\mathsf A^\mu$). $\bar\psi e^{i\alpha\gamma^5}\gamma^\mu\gamma^5e^{i\alpha\gamma^5}\psi = \bar\psi\gamma^\mu e^{-i\alpha\gamma^5}\gamma^5e^{i\alpha\gamma^5}\psi = \bar\psi\gamma^\mu\gamma^5e^{-i\alpha\gamma^5}e^{i\alpha\gamma^5}\psi = \bar\psi\gamma^\mu\gamma^5\psi$: the extra $\gamma^5$ commutes with the exponentials and changes nothing.
>
> **Step 5** (reading). $\mathsf S^2 + \mathsf P^2$ is invariant. In the chiral basis $e^{i\alpha\gamma^5}\psi = (e^{-i\alpha}\psi_L, e^{i\alpha}\psi_R)$: $\mathsf V^\mu$, $\mathsf A^\mu$ pair each half with itself and are invariant; $\mathsf S$, $\mathsf P$ pair $\psi_L$ with $\psi_R$ and pick up $e^{\pm2i\alpha}$. At $\alpha = \frac\pi2$: $\mathsf S \to -\mathsf S$, $\mathsf P \to -\mathsf P$. To first order $\delta\mathsf S = 2\alpha\mathsf P$, so $\delta(-m\mathsf S) = -2\alpha m\,\mathsf P$, the $\delta\mathcal L$ of PS6.5(c). (All three laws verified numerically for a random spinor, $\alpha = 0.4$.)
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|Example §C5a.8.1]] (parts 1–3; its derivation states $\mathsf S \to \cos2\alpha\,\mathsf S + \sin2\alpha\,\mathsf P$; the user's Problem Set 6, Problem 5(a)–(c)), [[§CB.12 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-12-15|Theorem §CB.12.15]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^def-c5a-6-2|Def. §C5a.6.2]]. The laws for $\mathsf P$ and $\mathsf A^\mu$ are not stated there: *Derived here; check:* the same series steps as Example §C5a.8.1, parts 1–2.

^sol-px-6-5-1

### X6.5.2 · Noether current of the vector phase
*[variation of PS6.5(d)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-6-5-2]]

> [!success]- Solution
> **Answer.** $j^\mu = -\bar\psi\gamma^\mu\psi = -\mathsf V^\mu$, with $\partial_\mu j^\mu = 0$ on solutions for every $m$ (conventionally one uses $j^\mu = +\bar\psi\gamma^\mu\psi$).
>
> **Step 1** (the recipe of PS6.5(d)). $j^\mu = \sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Delta\phi_i - \mathcal J^\mu$, with $\delta\phi_i = \alpha\Delta\phi_i$, $\delta\mathcal L = \alpha\,\partial_\mu\mathcal J^\mu$, the eight independent fields $\psi_a$, $\bar\psi_a$.
>
> **Step 2** (generators). $\psi' = e^{i\alpha}\psi$, $\bar\psi' = (e^{i\alpha}\psi)^\dagger\gamma^0 = e^{-i\alpha}\bar\psi$ ($\alpha$ real). So $\Delta\psi_a = i\psi_a$, $\Delta\bar\psi_a = -i\bar\psi_a$.
>
> **Step 3** ($\mathcal J^\mu$). Every term of $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ has one $\bar\psi$ and one $\psi$, and $\alpha$ is constant, so $\mathcal L' = e^{-i\alpha}e^{i\alpha}\mathcal L = \mathcal L$ exactly, for every $m$ (the mass term included, unlike the chiral case): $\mathcal J^\mu = 0$.
>
> **Step 4** (the current). $\frac{\partial\mathcal L}{\partial(\partial_\mu\psi_a)} = (i\bar\psi\gamma^\mu)_a$ and $\frac{\partial\mathcal L}{\partial(\partial_\mu\bar\psi_a)} = 0$ (no derivative of $\bar\psi$ in $\mathcal L$), so only the $\psi$ sum survives, a row times a column:
>
> $$
> j^\mu = \sum_a(i\bar\psi\gamma^\mu)_a(i\psi)_a = i\cdot i\,\bar\psi\gamma^\mu\psi = -\bar\psi\gamma^\mu\psi .
> $$
>
> **Step 5** (divergence, general $m$). Product rule: $\partial_\mu j^\mu = -(\partial_\mu\bar\psi)\gamma^\mu\psi - \bar\psi\gamma^\mu\partial_\mu\psi$. The Dirac equation $i\gamma^\mu\partial_\mu\psi = m\psi$ gives $\gamma^\mu\partial_\mu\psi = \frac mi\psi$; its Hermitian conjugate times $\gamma^0$ (with $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$) gives $(\partial_\mu\bar\psi)\gamma^\mu = -\frac mi\bar\psi$. Hence
>
> $$
> \partial_\mu j^\mu = -\Bigl(-\frac mi\Bigr)\bar\psi\psi - \frac mi\,\bar\psi\psi = 0 .
> $$
>
> Compare PS6.5(e): there the $\gamma^5$ between the two terms flips one sign and the terms add to $-2im\,\bar\psi\gamma^5\psi$; here they cancel. The Noether sign is the opposite of the conventional current $j^\mu = \mathsf V^\mu$ with $Q = \int d^3x\,\psi^\dagger\psi$; any constant multiple of a conserved current is conserved.
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]] ($j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$ and the direct check, steps 4–5 of its derivation), [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|Example §C5a.8.1]] (the recipe and the two Dirac equations as the user wrote them for PS6.5(d)–(e)), [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]; drill: [[PHY 513 PS Drill#^ps6-5-d|PS Drill, PS6.5(d)]].

^sol-px-6-5-2

---

## G. Discrete symmetries

### X7.2.1 · Time reversal on the tensor bilinear
*[variation of PS7.2(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-2-1]]

> [!success]- Solution
> **Answer.** $U(\mathcal T)\mathsf T^{\mu\nu}(x)U(\mathcal T)^{-1} = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$, i.e. $\mathsf T^{0i} \to +\mathsf T^{0i}(x_T)$, $\mathsf T^{ij} \to -\mathsf T^{ij}(x_T)$: the opposite of parity, the extra sign being the conjugated $i$ of $\sigma^{\mu\nu}$.
>
> **Step 1** (the two field laws). $U(\mathcal T)\hat\psi(x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(x_T)$, $x_T = (-t, \mathbf x)$. Taking the adjoint (an antiunitary $U$ commutes with $\dagger$) gives $\hat\psi^\dagger(x_T)(\gamma^1\gamma^3)^\dagger = \hat\psi^\dagger(x_T)\gamma^3\gamma^1$; right-multiplying by $\gamma^0$ (real, so $U(\mathcal T)$ leaves it alone; it commutes with $\gamma^3\gamma^1$) gives $U(\mathcal T)\hat{\bar\psi}(x)U(\mathcal T)^{-1} = \hat{\bar\psi}(x_T)\gamma^3\gamma^1$.
>
> **Step 2** (antilinearity on the bilinear). In components $\mathsf T^{\mu\nu} = \sum_{a,b}\hat{\bar\psi}_a(\sigma^{\mu\nu})_{ab}\hat\psi_b$. Inserting $U^{-1}U = \mathbb 1$ between the fields, $U(\mathcal T)$ conjugates the numbers $(\sigma^{\mu\nu})_{ab}$ and keeps the order of the two operators, so there is no fermion exchange:
>
> $$
> U(\mathcal T)\mathsf T^{\mu\nu}(x)U(\mathcal T)^{-1} = \hat{\bar\psi}(x_T)\,\gamma^3\gamma^1(\sigma^{\mu\nu})^\ast\gamma^1\gamma^3\,\hat\psi(x_T) .
> $$
>
> **Step 3** (the $i$ flips). $(\sigma^{\mu\nu})^\ast = \bigl(\frac i2[\gamma^\mu, \gamma^\nu]\bigr)^\ast = -\frac i2[(\gamma^\mu)^\ast, (\gamma^\nu)^\ast]$.
>
> **Step 4** (one $\gamma$ at a time). In the chiral basis only $\gamma^2$ is imaginary, and $\gamma^1\gamma^3$ commutes with $\gamma^0, \gamma^2$ and anticommutes with $\gamma^1, \gamma^3$; together $(\gamma^\mu)^\ast\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$ (lower index), i.e. $\gamma^3\gamma^1(\gamma^\mu)^\ast\gamma^1\gamma^3 = \gamma_\mu$ since $\gamma^3\gamma^1\gamma^1\gamma^3 = \gamma^3(-\mathbb 1)\gamma^3 = \mathbb 1$. Insert $\mathbb 1 = \gamma^1\gamma^3\gamma^3\gamma^1$ ($= \gamma^1(-\mathbb 1)\gamma^1 = \mathbb 1$) between the two factors of each product: $\gamma^3\gamma^1(\gamma^\mu)^\ast(\gamma^\nu)^\ast\gamma^1\gamma^3 = \gamma_\mu\gamma_\nu$. Hence $\gamma^3\gamma^1(\sigma^{\mu\nu})^\ast\gamma^1\gamma^3 = -\frac i2[\gamma_\mu, \gamma_\nu]$.
>
> **Step 5** (back to upper indices). Componentwise $\gamma_\mu = \mathcal P^\mu{}_\rho\gamma^\rho$ ($\gamma_0 = \gamma^0$, $\gamma_i = -\gamma^i$), so $-\frac i2[\gamma_\mu, \gamma_\nu] = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\,\frac i2[\gamma^\rho, \gamma^\sigma] = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\sigma^{\rho\sigma}$. The numbers $\mathcal P$ come out of the bilinear: the answer. Components: $(0, i)$: $-(+1)(-1) = +1$; $(i, j)$: $-(-1)(-1) = -1$.
>
> **Step 6** (a component check). $\sigma^{12} = i\gamma^1\gamma^2$ is real ($\gamma^1$ real, $\gamma^2$ imaginary), so $(\sigma^{12})^\ast = \sigma^{12}$; $\gamma^1\gamma^3$ commutes with $\gamma^2$ and anticommutes with $\gamma^1$, hence anticommutes with $\gamma^1\gamma^2$: $\gamma^3\gamma^1\sigma^{12}\gamma^1\gamma^3 = -\sigma^{12}\gamma^3\gamma^1\gamma^1\gamma^3 = -\sigma^{12}$. So $\mathsf T^{12} \to -\mathsf T^{12}(x_T)$, as in Step 5. (All sixteen components of $\gamma^3\gamma^1(\sigma^{\mu\nu})^\ast\gamma^1\gamma^3 = -\mathcal P^\mu{}_\mu\mathcal P^\nu{}_\nu\sigma^{\mu\nu}$, no sum, also checked numerically.)
>
> *Checked against:* [[§C9.8 Time Reversal#^thm-c9-8-14|Theorem §C9.8.14]] (same statement and route), [[§C9.8 Time Reversal#^thm-c9-8-10|Theorem §C9.8.10]] (the general rule of Step 2), [[§C9.8 Time Reversal#^thm-c9-8-4|Theorem §C9.8.4]] (part 4, used in Step 4), [[§C9.8 Time Reversal#^thm-c9-8-8|Theorem §C9.8.8]], and the $T$ column of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]]; the field laws as the user wrote them in [[PHY 513 PS Drill#^ps7-2-c|PS Drill, PS7.2(c)]].

^sol-px-7-2-1

### X7.2.2 · Charge conjugation on the pseudoscalar
*[variation of PS7.2(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-2-2]]

> [!success]- Solution
> **Answer.** $U(\mathcal C)\mathsf P(x)U(\mathcal C)^{-1} = +\mathsf P(x)$: the sign $(-i)^2 = -1$ from the two field laws and the sign $-1$ from exchanging the fermion fields cancel, and the matrix $i\gamma^5$ comes back unchanged.
>
> **Step 1** (field laws in components). $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i(\hat{\bar\psi}\gamma^0\gamma^2)^{\mathsf T}$, i.e. $U\hat\psi_dU^{-1} = -i\sum_b\hat{\bar\psi}_b(\gamma^0\gamma^2)_{bd}$; and $U(\mathcal C)\hat{\bar\psi}(x)U(\mathcal C)^{-1} = (-i\gamma^0\gamma^2\hat\psi)^{\mathsf T}$, i.e. $U\hat{\bar\psi}_cU^{-1} = -i\sum_a(\gamma^0\gamma^2)_{ca}\hat\psi_a$, all at the same point $x$.
>
> **Step 2** (insert). $\mathsf P = \sum_{c,d}\hat{\bar\psi}_c(i\gamma^5)_{cd}\hat\psi_d$. $U(\mathcal C)$ is linear, so the numbers $(i\gamma^5)_{cd}$, the $i$ included, pass through unchanged. Inserting $U^{-1}U = \mathbb 1$:
>
> $$
> U\mathsf PU^{-1} = (-i)^2\sum_{a,b,c,d}(\gamma^0\gamma^2)_{ca}(i\gamma^5)_{cd}(\gamma^0\gamma^2)_{bd}\,\hat\psi_a\hat{\bar\psi}_b = -\sum_{a,b}M_{ab}\,\hat\psi_a\hat{\bar\psi}_b, \qquad M = (\gamma^0\gamma^2)^{\mathsf T}(i\gamma^5)(\gamma^0\gamma^2)^{\mathsf T} .
> $$
>
> **Step 3** (fermion exchange). $U(\mathcal C)$ maps annihilators to annihilators and creators to creators, so the normal-ordered $\mathsf P$ goes to a normal-ordered product, inside which fermion operators anticommute with no c-number left over: $\hat\psi_a\hat{\bar\psi}_b \to -\hat{\bar\psi}_b\hat\psi_a$. So $U\mathsf PU^{-1} = +\sum_{a,b}\hat{\bar\psi}_b(M^{\mathsf T})_{ba}\hat\psi_a = \hat{\bar\psi}\,M^{\mathsf T}\hat\psi$ with $M^{\mathsf T} = \gamma^0\gamma^2\,(i\gamma^5)^{\mathsf T}\,\gamma^0\gamma^2$.
>
> **Step 4** (the matrix). $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ is symmetric, $(i\gamma^5)^{\mathsf T} = i\gamma^5$; $\gamma^5$ anticommutes with $\gamma^0$ and with $\gamma^2$, so it commutes with $\gamma^0\gamma^2$; and $\gamma^0\gamma^2\gamma^0\gamma^2 = -\gamma^0\gamma^0\gamma^2\gamma^2 = -(\mathbb 1)(-\mathbb 1) = \mathbb 1$. Hence $M^{\mathsf T} = i\gamma^5\,\gamma^0\gamma^2\gamma^0\gamma^2 = i\gamma^5$ and $U\mathsf P(x)U^{-1} = \hat{\bar\psi}i\gamma^5\hat\psi(x) = +\mathsf P(x)$.
>
> **Sign bookkeeping.** $(-i)^2 = -1$ (Step 2) times $-1$ (Step 3) times $+1$ (Step 4) $= +1$. With commuting fields the same computation would give $-\mathsf P$.
>
> *Checked against:* [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-8|Theorem §C9.6.8]], the general rule [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|Theorem §C9.6.7]] (part 1), the exchange step of [[§C9.6 Charge Conjugation on the Field and Bilinears#^der-c9-6-5|Derivation §C9.6.5]], the field laws [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-3|Theorem §C9.6.3]] and [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|Theorem §C9.6.4]], [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-4|Theorem §C9.5.4]] (part 5); the same steps for $\mathsf V^\mu$, $\mathsf A^\mu$ in the user's [[PHY 513 PS Drill#^ps7-2-b|PS Drill, PS7.2(b)]].

^sol-px-7-2-2

### X7.2.3 · Parity on the vector and the pseudoscalar
*[variation of PS7.2(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-2-3]]

> [!success]- Solution
> **Answer.** $U(\mathcal P)\mathsf V^\mu(x)U(\mathcal P)^{-1} = \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$ and $U(\mathcal P)\mathsf P(x)U(\mathcal P)^{-1} = -\mathsf P(\tilde x)$, independent of the phase $\eta_a$.
>
> **Step 1** (the field). $U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$, $\tilde x = (t, -\mathbf x)$, $\lvert\eta_a\rvert = 1$.
>
> **Step 2** (the conjugate field). $U(\mathcal P)$ is unitary, so $U\hat\psi^\dagger U^{-1} = (U\hat\psi U^{-1})^\dagger = \bigl(\eta_a\gamma^0\hat\psi(\tilde x)\bigr)^\dagger = \eta_a^\ast\hat\psi^\dagger(\tilde x)\gamma^0$ ($\gamma^{0\dagger} = \gamma^0$). The c-number $\gamma^0$ in $\hat{\bar\psi} = \hat\psi^\dagger\gamma^0$ is untouched by $U$: $U\hat{\bar\psi}(x)U^{-1} = \eta_a^\ast\hat\psi^\dagger(\tilde x)\gamma^0\gamma^0 = \eta_a^\ast\hat{\bar\psi}(\tilde x)\gamma^0$.
>
> **Step 3** (any bilinear). With $U^{-1}U = \mathbb 1$ inserted and the numbers $\Gamma_{ab}$ passing the linear $U$: $U\hat{\bar\psi}\Gamma\hat\psi(x)U^{-1} = \eta_a^\ast\eta_a\,\hat{\bar\psi}(\tilde x)\gamma^0\Gamma\gamma^0\hat\psi(\tilde x) = \hat{\bar\psi}(\tilde x)\gamma^0\Gamma\gamma^0\hat\psi(\tilde x)$. The fields keep their order: no fermion sign.
>
> **Step 4** (vector). $\gamma^0\gamma^0\gamma^0 = \gamma^0$; for $i = 1, 2, 3$, $\gamma^0\gamma^i\gamma^0 = -\gamma^i\gamma^0\gamma^0 = -\gamma^i$. Both are $\gamma^0\gamma^\mu\gamma^0 = \mathcal P^\mu{}_\nu\gamma^\nu$, so $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$: $\mathsf V^0$ even, $\mathsf V^i$ odd.
>
> **Step 5** (pseudoscalar). $\gamma^5$ anticommutes with $\gamma^0$: $\gamma^0(i\gamma^5)\gamma^0 = -i\gamma^5\gamma^0\gamma^0 = -i\gamma^5$; the $i$ is a number that the unitary $U(\mathcal P)$ does not touch. So $\mathsf P \to -\mathsf P(\tilde x)$.
>
> **The convention.** The course conjugates as $U\hat OU^{-1}$ (Problem Set 6's $\mathcal P\psi\mathcal P^\dagger$ is the same thing); the order $U^{-1}\hat OU$ would replace $\eta_a$ by $\eta_a^\ast$ in Steps 1–2, which cancels in Step 3, so both bilinear rules hold in either order.
>
> *Checked against:* [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]] (rows 2–3), [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|Theorem §C9.4.1]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-2|Theorem §C9.4.2]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-3|Theorem §C9.4.3]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-1|§C9.3, Caution: Which side the inverse is on, and the names of the phases]]; the same steps for $\mathsf A^\mu$, $\mathsf T^{\mu\nu}$ in the user's [[PHY 513 PS Drill#^ps7-2-a|PS Drill, PS7.2(a)]].

^sol-px-7-2-3

### X7.2.4 · The chiral currents under C and P
*[extension of PS7.2]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-2-4]]

> [!success]- Solution
> **Answer.** $U(\mathcal C)j^\mu_L(x)U(\mathcal C)^{-1} = -j^\mu_R(x)$ and $U(\mathcal P)j^\mu_L(x)U(\mathcal P)^{-1} = \mathcal P^\mu{}_\nu j^\nu_R(\tilde x)$: each of $C$ and $P$ turns a left-handed current into a right-handed one (and their product keeps it left-handed: $j^\mu_L \to -\mathcal P^\mu{}_\nu j^\nu_L(\tilde x)$ under $CP$).
>
> **Step 1** (split into $\mathsf V$ and $\mathsf A$). $\gamma^\mu\frac{1 \mp \gamma^5}{2} = \frac12(\gamma^\mu \mp \gamma^\mu\gamma^5)$ and $\Gamma \mapsto \hat{\bar\psi}\Gamma\hat\psi$ is linear, so $j^\mu_L = \frac12(\mathsf V^\mu - \mathsf A^\mu)$, $j^\mu_R = \frac12(\mathsf V^\mu + \mathsf A^\mu)$. (Equivalently $j^\mu_L = \overline{\hat\psi_L}\gamma^\mu\hat\psi_L$ with $\hat\psi_L = P_L\hat\psi$, by $\overline{P_L\hat\psi} = \hat{\bar\psi}P_R$, $P_R\gamma^\mu = \gamma^\mu P_L$, $P_L^2 = P_L$.)
>
> **Step 2** (C). $U(\mathcal C)$ is linear, so $\frac12$ passes; $\mathsf V^\mu \to -\mathsf V^\mu(x)$, $\mathsf A^\mu \to +\mathsf A^\mu(x)$. Hence $j^\mu_L \to \frac12(-\mathsf V^\mu - \mathsf A^\mu)(x) = -j^\mu_R(x)$, and likewise $j^\mu_R \to \frac12(-\mathsf V^\mu + \mathsf A^\mu) = -j^\mu_L(x)$.
>
> **Step 3** (P). $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$, $\mathsf A^\mu \to -\mathcal P^\mu{}_\nu\mathsf A^\nu(\tilde x)$. Hence $j^\mu_L \to \frac12\mathcal P^\mu{}_\nu(\mathsf V^\nu + \mathsf A^\nu)(\tilde x) = \mathcal P^\mu{}_\nu j^\nu_R(\tilde x)$.
>
> **Step 4** ($CP$, as a check). With $U(\mathcal C)U(\mathcal P)$ (first $P$): $j^\mu_L(x) \to \mathcal P^\mu{}_\nu j^\nu_R(\tilde x) \to \mathcal P^\mu{}_\nu\bigl(-j^\nu_L(\tilde x)\bigr)$, the number $\mathcal P^\mu{}_\nu$ passing the linear $U(\mathcal C)$. A theory coupling only $j^\mu_L$ (the charged weak current) violates $C$ and $P$ separately but can respect $CP$.
>
> *Checked against:* [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-12|★ Theorem §C9.6.12]] (C; its derivation is Step 2) and [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-7|★ Theorem §C9.4.7]] (part 3, P), the rows $\mathsf V^\mu$, $\mathsf A^\mu$ of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]], and [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]] for Step 1.

^sol-px-7-2-4

### X7.3.1 · CPT on the Dirac conjugate field
*[extension of PS7.3]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-3-1]]

> [!success]- Solution
> **Answer.** $\Theta\hat{\bar\psi}(x)\Theta^{-1} = \eta_a^\ast\,\hat\psi^{\mathsf T}(-x)\,\gamma^5\gamma^0 = \eta_a^\ast\bigl(\gamma^0\gamma^5\hat\psi(-x)\bigr)^{\mathsf T}$, componentwise $\Theta\hat{\bar\psi}_b(x)\Theta^{-1} = \eta_a^\ast\sum_c\hat\psi_c(-x)(\gamma^5\gamma^0)_{cb}$: a row whose entries are the components of the column $\eta_a^\ast\gamma^0\gamma^5\hat\psi(-x)$.
>
> **Step 1** (the rules for an antiunitary $\Theta$). $\Theta$ is antiunitary, and conjugation by it (i) complex-conjugates every c-number coefficient, (ii) keeps the order of operators in a product, (iii) commutes with the adjoint: $\Theta\hat A^\dagger\Theta^{-1} = (\Theta\hat A\Theta^{-1})^\dagger$. Spinor indices below are $b, c, d$ ($a$ is reserved for the phase $\eta_a$).
>
> **Step 2** (the given law in components). $(\hat\psi^{\dagger\mathsf T})_c = (\hat\psi_c)^\dagger$, so $\Theta\hat\psi_d(x)\Theta^{-1} = \eta_a\sum_c(\gamma^5)_{dc}\,\hat\psi_c^\dagger(-x)$. This law already contains $\Theta$'s own conjugation (it was derived with $T$ acting first).
>
> **Step 3** (the adjoint). By (iii), $\Theta\hat\psi_d^\dagger(x)\Theta^{-1} = \bigl(\eta_a\sum_c(\gamma^5)_{dc}\hat\psi_c^\dagger(-x)\bigr)^\dagger = \eta_a^\ast\sum_c(\gamma^5)_{dc}^\ast\,\hat\psi_c(-x) = \eta_a^\ast\sum_c(\gamma^5)_{dc}\,\hat\psi_c(-x)$. Here the numbers are conjugated by the dagger, not by $\Theta$: $\eta_a \to \eta_a^\ast$, and $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ is real.
>
> **Step 4** (the $\gamma^0$ of $\hat{\bar\psi}$). $\hat{\bar\psi}_b = \sum_d\hat\psi_d^\dagger(\gamma^0)_{db}$. By (i) $\Theta$ conjugates the numbers $(\gamma^0)_{db}$, which are real, so they are unchanged:
>
> $$
> \Theta\hat{\bar\psi}_b(x)\Theta^{-1} = \sum_d\bigl(\Theta\hat\psi_d^\dagger\Theta^{-1}\bigr)(\gamma^0)_{db}^\ast = \eta_a^\ast\sum_{c,d}\hat\psi_c(-x)\,(\gamma^5)_{dc}(\gamma^0)_{db} = \eta_a^\ast\sum_c\hat\psi_c(-x)\,\bigl((\gamma^5)^{\mathsf T}\gamma^0\bigr)_{cb} ,
> $$
>
> and $(\gamma^5)^{\mathsf T} = \gamma^5$, so $\Theta\hat{\bar\psi}\Theta^{-1} = \eta_a^\ast\hat\psi^{\mathsf T}(-x)\gamma^5\gamma^0$. As a transposed column: $\sum_c(\gamma^5\gamma^0)_{cb}\hat\psi_c = \bigl((\gamma^5\gamma^0)^{\mathsf T}\hat\psi\bigr)_b = (\gamma^0\gamma^5\hat\psi)_b$ ($\gamma^0$, $\gamma^5$ symmetric); no operators are reordered.
>
> **Step 5** (cross-check: compose $T$, $P$, $C$). $T$: $\hat{\bar\psi}(x) \to \hat{\bar\psi}(x_T)\gamma^3\gamma^1$. $P$ (linear, at the point $x_T$, whose parity image is $-x$; $\gamma^3\gamma^1$ passes): $\eta_a^\ast\hat{\bar\psi}(-x)\gamma^0\gamma^3\gamma^1$. The $\eta_a^\ast$ comes from parity on $\hat{\bar\psi}$ and is not conjugated again, because the antilinear step has already acted. $C$ (linear, at $-x$): $\eta_a^\ast\bigl(-i\gamma^0\gamma^2\hat\psi(-x)\bigr)^{\mathsf T}\gamma^0\gamma^3\gamma^1 = -i\eta_a^\ast\hat\psi^{\mathsf T}(\gamma^0\gamma^2)^{\mathsf T}\gamma^0\gamma^3\gamma^1 = -i\eta_a^\ast\hat\psi^{\mathsf T}\gamma^2\gamma^0\gamma^0\gamma^3\gamma^1 = -i\eta_a^\ast\hat\psi^{\mathsf T}\gamma^2\gamma^3\gamma^1$. The matrix: $\gamma^2\gamma^3\gamma^1 = \gamma^1\gamma^2\gamma^3$ (two exchanges), and $\gamma^5\gamma^0 = i\gamma^0\gamma^1\gamma^2\gamma^3\gamma^0 = -i\gamma^1\gamma^2\gamma^3$ (three exchanges to move the last $\gamma^0$ to the front, then $(\gamma^0)^2 = \mathbb 1$). So $-i\gamma^2\gamma^3\gamma^1 = \gamma^5\gamma^0$: the same result (the matrix identity also checked numerically with the chiral matrices).
>
> *Derived here; check:* no vault box states $\Theta\hat{\bar\psi}\Theta^{-1}$. Step 5 composes [[§C9.8 Time Reversal#^thm-c9-8-8|Theorem §C9.8.8]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|Theorem §C9.4.1]] and [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|Theorem §C9.6.4]] in the order of [[§C9.9 CPT and the CPT Theorem#^def-c9-9-1|Def. §C9.9.1]] and agrees with Steps 2–4, which start from [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|Theorem §C9.9.3]] and use [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-19-16|Theorem §CB.19.16]] (parts 1–3) with [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|Theorem §C9.9.2]]; X7.3.2 then reproduces the CPT column of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]].

^sol-px-7-3-1

### X7.3.2 · S and V under CPT from the field law
*[extension of PS7.3]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-3-2]]

> [!success]- Solution
> **Answer.** $\Theta\mathsf S(x)\Theta^{-1} = +\mathsf S(-x)$ and $\Theta\mathsf V^\mu(x)\Theta^{-1} = -\mathsf V^\mu(-x)$. In general $\Theta\,\hat{\bar\psi}\Gamma\hat\psi(x)\,\Theta^{-1} = \hat{\bar\psi}(-x)\,\gamma^5\bar\Gamma\gamma^5\,\hat\psi(-x)$ with $\bar\Gamma = \gamma^0\Gamma^\dagger\gamma^0$.
>
> **Step 1** (insert both laws). Write $\hat{\bar\psi}\Gamma\hat\psi = \sum_{b,e}\hat{\bar\psi}_b\Gamma_{be}\hat\psi_e$. $\Theta$ conjugates the numbers $\Gamma_{be}$ and keeps the order of the two fields; with X7.3.1 for $\hat{\bar\psi}$ and $\Theta\hat\psi_e\Theta^{-1} = \eta_a\sum_d(\gamma^5)_{ed}\hat\psi_d^\dagger(-x)$:
>
> $$
> \Theta\,\hat{\bar\psi}\Gamma\hat\psi(x)\,\Theta^{-1} = \sum_{b,e}\bigl(\Theta\hat{\bar\psi}_b\Theta^{-1}\bigr)\Gamma^\ast_{be}\bigl(\Theta\hat\psi_e\Theta^{-1}\bigr) = \eta_a^\ast\eta_a\sum_{c,d}\hat\psi_c\,M_{cd}\,\hat\psi_d^\dagger, \qquad M = \gamma^5\gamma^0\,\Gamma^\ast\,\gamma^5 ,
> $$
>
> all fields at $-x$; $\eta_a^\ast\eta_a = 1$.
>
> **Step 2** (the fermion exchange). $T$, $P$, $C$ each map annihilators to annihilators and creators to creators, so $\Theta$ maps the normal-ordered bilinear to a normal-ordered product, inside which $\hat\psi_c\hat\psi_d^\dagger = -\hat\psi_d^\dagger\hat\psi_c$ with no c-number. So the result is $-\sum_{c,d}\hat\psi_d^\dagger(M^{\mathsf T})_{dc}\hat\psi_c = -\hat\psi^\dagger M^{\mathsf T}\hat\psi = -\hat{\bar\psi}\,\gamma^0M^{\mathsf T}\hat\psi$ (using $\hat\psi^\dagger = \hat{\bar\psi}\gamma^0$), with $M^{\mathsf T} = (\gamma^5)^{\mathsf T}(\Gamma^\ast)^{\mathsf T}(\gamma^0)^{\mathsf T}(\gamma^5)^{\mathsf T} = \gamma^5\Gamma^\dagger\gamma^0\gamma^5$. The matrix is $N = -\gamma^0\gamma^5\Gamma^\dagger\gamma^0\gamma^5$.
>
> **Step 3** ($\mathsf S$, $\Gamma = \mathbb 1$). $N = -\gamma^0\gamma^5\gamma^0\gamma^5 = +\gamma^0\gamma^0\gamma^5\gamma^5 = \mathbb 1$ (one anticommutation of $\gamma^5$ past $\gamma^0$). So $\Theta\mathsf S(x)\Theta^{-1} = +\mathsf S(-x)$: the exchange sign is cancelled by the $\gamma^5\gamma^0$ anticommutation.
>
> **Step 4** ($\mathsf V^\mu$, $\Gamma = \gamma^\mu$). The conjugation: $(\gamma^\mu)^\ast$ flips $\gamma^2$ only; the transpose in $M^{\mathsf T}$ flips $\gamma^1$, $\gamma^3$; together $((\gamma^\mu)^\ast)^{\mathsf T} = (\gamma^\mu)^\dagger = \gamma^0\gamma^\mu\gamma^0$ for every $\mu$. Then $N = -\gamma^0\gamma^5(\gamma^0\gamma^\mu\gamma^0)\gamma^0\gamma^5 = -\gamma^0\gamma^5\gamma^0\gamma^\mu\gamma^5 = +\gamma^5\gamma^\mu\gamma^5 = -\gamma^\mu\gamma^5\gamma^5 = -\gamma^\mu$. So $\Theta\mathsf V^\mu(x)\Theta^{-1} = -\mathsf V^\mu(-x)$.
>
> **Step 5** (the general rule, a check on the whole column). Since $-\gamma^0\gamma^5 = \gamma^5\gamma^0$, $N = \gamma^5(\gamma^0\Gamma^\dagger\gamma^0)\gamma^5 = \gamma^5\bar\Gamma\gamma^5$. For the five standard matrices $\bar\Gamma = \Gamma$, and $\gamma^5$ anticommutes with each $\gamma^\mu$, so $\gamma^5\Gamma\gamma^5 = (-1)^n\Gamma$ with $n$ the number of $\gamma^\mu$'s: $\mathsf S, \mathsf P \to +$, $\mathsf V, \mathsf A \to -$, $\mathsf T \to +$, the $CPT$ column with $n$ = number of Lorentz indices (the matrix $N$ checked numerically for all five, with the chiral matrices).
>
> *Derived here; check:* the CPT column of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]] ($\mathsf S \to +\mathsf S(-x)$, $\mathsf V^\mu \to -\mathsf V^\mu(-x)$), obtained there as the product of the $C$, $P$, $T$ signs ([[§C9.9 CPT and the CPT Theorem#^der-c9-9-5|Derivation §C9.9.5]]); the exchange step as in [[§C9.6 Charge Conjugation on the Field and Bilinears#^der-c9-6-5|Derivation §C9.6.5]]; $\bar\Gamma = \Gamma$ from [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-4|Theorem §C5a.6.4]]; the axial row of Step 5 against [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|Example §C9.9.1]].

^sol-px-7-3-2

### X7.3.3 · CPT in the other order
*[variation of PS7.3]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-3-3]]

> [!success]- Solution
> **Answer.** $\Theta'\hat\psi(x)\Theta'^{-1} = -\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$: the law of $\Theta$ up to an overall sign; on every bilinear the sign enters twice and cancels, so $\Theta'$ and $\Theta$ act identically on bilinears.
>
> **Step 1** (C first, linear). $U(\mathcal C)\hat\psi_c(x)U(\mathcal C)^{-1} = -i\sum_b(\gamma^2)_{cb}\hat\psi_b^\dagger(x)$.
>
> **Step 2** (then P, linear, on the adjoint field). $U(\mathcal P)\hat\psi_b^\dagger(x)U(\mathcal P)^{-1} = \bigl(\eta_a\sum_d(\gamma^0)_{bd}\hat\psi_d(\tilde x)\bigr)^\dagger = \eta_a^\ast\sum_d(\gamma^0)_{bd}\hat\psi_d^\dagger(\tilde x)$ ($\gamma^0$ real). The numbers $-i(\gamma^2)_{cb}$ pass the linear $U(\mathcal P)$; as a column the field is now $-i\eta_a^\ast\gamma^2\gamma^0\hat\psi^{\dagger\mathsf T}(\tilde x)$.
>
> **Step 3** (then T, antilinear: conjugate every number). $(-i)^\ast = i$, $(\eta_a^\ast)^\ast = \eta_a$, $(\gamma^2)^\ast = -\gamma^2$, $(\gamma^0)^\ast = \gamma^0$. On the operators, $U(\mathcal T)\hat\psi_d^\dagger(y)U(\mathcal T)^{-1} = \bigl(\sum_e(\gamma^1\gamma^3)_{de}\hat\psi_e(y_T)\bigr)^\dagger = \sum_e(\gamma^1\gamma^3)_{de}\hat\psi_e^\dagger(y_T)$ ($\gamma^1\gamma^3$ real), and $y = \tilde x = (t, -\mathbf x)$ gives $y_T = (-t, -\mathbf x) = -x$. Altogether
>
> $$
> \Theta'\hat\psi(x)\Theta'^{-1} = i\,\eta_a\,(-\gamma^2)\gamma^0\gamma^1\gamma^3\,\hat\psi^{\dagger\mathsf T}(-x) = -i\eta_a\,\gamma^2\gamma^0\gamma^1\gamma^3\,\hat\psi^{\dagger\mathsf T}(-x) .
> $$
>
> **Step 4** (the matrix). $\gamma^2\gamma^0\gamma^1\gamma^3 = -\gamma^0\gamma^2\gamma^1\gamma^3 = +\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$ (two exchanges; $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$ from $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$). So $\Theta'\hat\psi\Theta'^{-1} = (-i)(-i)\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x) = -\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$.
>
> **Step 5** (comparison). $\Theta = U(\mathcal C)U(\mathcal P)U(\mathcal T)$ gives $+\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$. In $\Theta$ the phase $\eta_a$ is conjugated zero times (parity acts after the antilinear $T$); in $\Theta'$ twice (by the adjoint in Step 2 and by $T$ in Step 3), so it ends up unconjugated in both. The overall sign comes from the order of the $\gamma$'s, $\gamma^1\gamma^3\gamma^0(-i\gamma^2) = +\gamma^5$ versus $i(-\gamma^2)\gamma^0\gamma^1\gamma^3 = -\gamma^5$. Taking adjoints, $\Theta'\hat\psi^\dagger_c\Theta'^{-1} = -\Theta\hat\psi^\dagger_c\Theta^{-1}$ as well (the real $\gamma^0$ of $\hat{\bar\psi}$ is unaffected), so in $\hat{\bar\psi}\Gamma\hat\psi$ the two signs give $(-1)^2 = +1$: "any order will do" for bilinears.
>
> *Checked against:* [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|Theorem §C9.9.4]] and [[§C9.9 CPT and the CPT Theorem#^der-c9-9-4|Derivation §C9.9.4]] (same steps and sign), [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|Theorem §C9.9.3]] for $\Theta$, [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|Theorem §C9.9.1]] (part 3: any order gives $\pm\gamma^5$), [[§C9.8 Time Reversal#^thm-c9-8-3|Theorem §C9.8.3]] for Step 3.

^sol-px-7-3-3

### X7.4.1 · The parity phase of a real scalar field
*[variation of PS7.4(a)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-4-1]]

> [!success]- Solution
> **Answer.** The field law holds if and only if $\eta^\ast = \eta$; with $\lvert\eta\rvert = 1$, $\eta = \pm1$ (scalar or pseudoscalar). Then $U(\mathcal P)\lvert\mathbf p\rangle = \eta\lvert-\mathbf p\rangle$ and $U(\mathcal P)^2 = \mathbb 1$.
>
> **Step 1** (the creator). $U(\mathcal P)$ is unitary, so the adjoint of the defining relation is $U(\mathcal P)\hat a^\dagger_{\mathbf p}U(\mathcal P)^{-1} = (\eta\hat a_{-\mathbf p})^\dagger = \eta^\ast\hat a^\dagger_{-\mathbf p}$.
>
> **Step 2** (transform the field). With $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$ and the c-numbers passing the linear $U$:
>
> $$
> U\hat\phi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\eta\,\hat a_{-\mathbf p}e^{-ip\cdot x} + \eta^\ast\hat a^\dagger_{-\mathbf p}e^{ip\cdot x}\bigr) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\eta\,\hat a_{\mathbf p}e^{-ip\cdot\tilde x} + \eta^\ast\hat a^\dagger_{\mathbf p}e^{ip\cdot\tilde x}\bigr) ,
> $$
>
> relabelling $\mathbf p \to -\mathbf p$ ($d^3p$ and $E_{\mathbf p}$ unchanged, $p \to \tilde p$) and using $\tilde p\cdot x = p\cdot\tilde x$.
>
> **Step 3** (compare). $\eta\hat\phi(\tilde x)$ has $\eta$ in front of both terms. The difference is $(\eta^\ast - \eta)\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\hat a^\dagger_{\mathbf p}e^{ip\cdot\tilde x}$; its commutator with $\hat a_{\mathbf q}$ is $(\eta^\ast - \eta)\,e^{iq\cdot\tilde x}/\sqrt{2E_{\mathbf q}}$ by $[\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf q - \mathbf p)$, which vanishes for all $x$ only if $\eta^\ast = \eta$. So $\eta$ is real and, with $\lvert\eta\rvert = 1$, $\eta = \pm1$.
>
> **Step 4** (the short route). $\hat\phi$ is Hermitian and conjugation by a unitary preserves Hermiticity: $\eta\hat\phi(\tilde x) = U\hat\phi U^{-1} = (U\hat\phi U^{-1})^\dagger = \eta^\ast\hat\phi(\tilde x)$, so $\eta = \eta^\ast$.
>
> **Step 5** (states). $U\lvert\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,U\hat a^\dagger_{\mathbf p}U^{-1}U\lvert0\rangle = \eta^\ast\lvert-\mathbf p\rangle = \eta\lvert-\mathbf p\rangle$; $U^2\hat a_{\mathbf p}U^{-2} = \eta^2\hat a_{\mathbf p} = \hat a_{\mathbf p}$, so $U(\mathcal P)^2 = \mathbb 1$ on the Fock space.
>
> *Checked against:* [[§C9.2 Parity of the Scalar Field#^thm-c9-2-10|Theorem §C9.2.10]] with [[§C9.2 Parity of the Scalar Field#^der-c9-2-10|Derivation §C9.2.10]] (Steps 1–3, 5) and [[§C9.2 Parity of the Scalar Field#^der-c9-2-10b|Derivation §C9.2.10b]] (Step 4); for the complex field the condition becomes $\eta_b = \eta_a^\ast$ ([[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|Theorem §C9.2.2]]).

^sol-px-7-4-1

### X7.4.2 · The scalar charge under P, C, T and CPT
*[extension of PS7.4(b)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-4-2]]

> [!success]- Solution
> **Answer.** With $Q_J \equiv \int d^3x\,J^0$ ($= 2\hat Q$ in the course normalisation): $P$: $Q_J \to +Q_J$; $C$: $Q_J \to -Q_J$; $T$: $Q_J \to +Q_J$; $\Theta$: $Q_J \to -Q_J$.
>
> **Step 1** (the current laws). As the user found in PS7.4(b) (all phases 1): $U(\mathcal P)J^\mu(x)U(\mathcal P)^{-1} = \mathcal P^\mu{}_\nu J^\nu(\tilde x)$, $U(\mathcal C)J^\mu(x)U(\mathcal C)^{-1} = -J^\mu(x)$, $U(\mathcal T)J^\mu(x)U(\mathcal T)^{-1} = \mathcal P^\mu{}_\nu J^\nu(x_T)$; under $T$ the conjugated $i$ and the flipped $\partial^0$ cancel. For $\mu = 0$, $\mathcal P^0{}_0 = 1$: $J^0 \to J^0(\tilde x)$, $-J^0(x)$, $J^0(x_T)$. The measure $d^3x$ is real, so even the antilinear $U(\mathcal T)$ passes the integral unchanged.
>
> **Step 2** (P). $\int d^3x\,J^0(t, -\mathbf x) = \int d^3y\,J^0(t, \mathbf y)$ with $\mathbf y = -\mathbf x$, Jacobian $\lvert\det(-\mathbb 1_3)\rvert = 1$: $+Q_J$.
>
> **Step 3** (C). Same time, same point: $-Q_J$.
>
> **Step 4** (T). $\int d^3x\,J^0(-t, \mathbf x) = Q_J(-t) = Q_J(t)$: the charge is conserved, $[\hat Q, \hat H] = 0$ (equivalently $\partial_\mu J^\mu = 0$). So $+Q_J$.
>
> **Step 5** ($\Theta$, first $T$, then $P$, then $C$). $J^0(x) \to J^0(x_T) \to J^0(-x) \to -J^0(-x)$, i.e. $\Theta J^\mu(x)\Theta^{-1} = -J^\mu(-x)$ (one index, $(-1)^1$). Integrating, $\int d^3x\,\bigl(-J^0(-t, -\mathbf x)\bigr) = -Q_J(-t) = -Q_J$, with Steps 2 and 4.
>
> **Step 6** (check in modes). $\hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$. $P$ and $T$ send $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$, $\hat b_{\mathbf p} \to \hat b_{-\mathbf p}$ (real coefficients, so antilinearity changes nothing), and relabelling $\mathbf p \to -\mathbf p$ returns $\hat Q$; $C$ exchanges $\hat a \leftrightarrow \hat b$ and gives $-\hat Q$; hence $\Theta$ gives $-\hat Q$: CPT maps a particle to its antiparticle, of opposite charge. The normalisation: $J^\mu = i[\hat\phi^\dagger\partial^\mu\hat\phi - (\partial^\mu\hat\phi^\dagger)\hat\phi] = -\hat j^\mu$ and $\hat Q = -\frac12\int d^3x\,\hat j^0$, so $Q_J = 2\hat Q$; the overall factor does not affect any rule.
>
> *Checked against:* [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|Theorem §C9.10.4]] (the current laws; its derivation's last bullet integrates them: $\hat Q \to -\hat Q$ under $C$, $\hat Q$ under $P$ and $T$), [[§C9.2 Parity of the Scalar Field#^thm-c9-2-12|Theorem §C9.2.12]] (parity commutes with the charge, both routes), [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-6|Theorem §C9.10.6]] (part 3, $\Theta\hat j^\mu\Theta^{-1} = -\hat j^\mu(-x)$; the integrated $\Theta$ line is composed here), [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]] and [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^cau-c9-10-1|§C9.10, Caution: The star of a scalar field operator is the adjoint]] ($J^\mu = -\hat j^\mu$); the user's [[PHY 513 PS Drill#^ps7-4-b|PS Drill, PS7.4(b)]].

^sol-px-7-4-2

### X7.4.3 · A Yukawa coupling of the complex scalar under CPT
*[extension of PS7.4(c)]* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-4-3]]

> [!success]- Solution
> **Answer.** $g\hat\phi\mathsf S + g^\ast\hat\phi^\dagger\mathsf S$ is CPT invariant: $\Theta\,\hat{\mathcal O}(x)\,\Theta^{-1} = \hat{\mathcal O}(-x)$ and $\Theta\int d^4x\,\hat{\mathcal O}\,\Theta^{-1} = \int d^4x\,\hat{\mathcal O}$, for every complex $g$. $g\hat\phi\mathsf S$ alone is not: it goes to $g^\ast\hat\phi^\dagger\mathsf S(-x)$, a different operator, whatever $g$ is.
>
> **Step 1** (one term). $\Theta$ is antiunitary: it conjugates the number $g$ and keeps the order of the factors. With $\Theta\hat\phi(x)\Theta^{-1} = \hat\phi^\dagger(-x)$ and $\Theta\mathsf S(x)\Theta^{-1} = \mathsf S(-x)$:
>
> $$
> \Theta\,g\hat\phi(x)\mathsf S(x)\,\Theta^{-1} = g^\ast\,\bigl(\Theta\hat\phi(x)\Theta^{-1}\bigr)\bigl(\Theta\mathsf S(x)\Theta^{-1}\bigr) = g^\ast\,\hat\phi^\dagger(-x)\mathsf S(-x) .
> $$
>
> **Step 2** (the other term). $\Theta\hat\phi^\dagger(x)\Theta^{-1} = \hat\phi(-x)$ (the adjoint of the first law), and $(g^\ast)^\ast = g$: $\Theta\,g^\ast\hat\phi^\dagger\mathsf S(x)\,\Theta^{-1} = g\,\hat\phi\,\mathsf S(-x)$.
>
> **Step 3** (the sum). $\Theta\bigl(g\hat\phi\mathsf S + g^\ast\hat\phi^\dagger\mathsf S\bigr)(x)\Theta^{-1} = \bigl(g^\ast\hat\phi^\dagger\mathsf S + g\hat\phi\mathsf S\bigr)(-x)$: the two terms are exchanged, the operator is the same, at $-x$. For the action, substitute $y = -x$ (Jacobian $\lvert\det(-\mathbb 1_4)\rvert = 1$).
>
> **Step 4** (why: Hermiticity). $\hat\phi$ and the bilinear $\mathsf S$ are built from different fields and commute, and $\mathsf S^\dagger = \mathsf S$, so $(g\hat\phi\mathsf S)^\dagger = g^\ast\mathsf S\hat\phi^\dagger = g^\ast\hat\phi^\dagger\mathsf S$: the sum is Hermitian, local, and a Lorentz scalar with $n = 0$ indices, the case of the qualitative argument, $\Theta\hat{\mathcal O}(x)\Theta^{-1} = (-1)^n\hat{\mathcal O}^\dagger(-x)$. The single term $g\hat\phi\mathsf S$ is not Hermitian; its image $g^\ast\hat\phi^\dagger\mathsf S(-x)$ equals $g\hat\phi\mathsf S(-x)$ only if $g^\ast\hat\phi^\dagger = g\hat\phi$, impossible for $g \neq 0$ ($\hat\phi$ annihilates particles, $\hat\phi^\dagger$ antiparticles).
>
> **Step 5** (what the phase of $g$ does instead). Under $T$ alone, with $\hat\phi \to \hat\phi(x_T)$ and $\mathsf S \to \mathsf S(x_T)$, the sum goes to $(g^\ast\hat\phi\mathsf S + g\hat\phi^\dagger\mathsf S)(x_T)$; under $CP$ ($\hat\phi \to \hat\phi^\dagger(\tilde x)$, $\mathsf S \to \mathsf S(\tilde x)$, phases 1) to $(g\hat\phi^\dagger\mathsf S + g^\ast\hat\phi\mathsf S)(\tilde x)$. Each is invariant only for real $g$, while $CPT$ is invariant for any $g$: a complex $g$ violates $T$ and $CP$ together. (For this single coupling the phase can be removed by rephasing $\hat\phi \to e^{-i\arg g}\hat\phi$, which the free Lagrangian allows; a physical violation needs a second coupling fixing the phase.)
>
> *Derived here; check:* the $n = 0$ case of [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-2|Example §C9.9.2]] (the user's PS7.4(c) argument), with [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-6|Theorem §C9.10.6]] (part 1), the $\mathsf S$ row of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]] and [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|Theorem §C9.9.2]]; Step 5 uses [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-1|Theorem §C9.10.1]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-2|Theorem §C9.10.2]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|Theorem §C9.2.2]] and the $C$, $P$, $T$ columns of Theorem §C9.9.5; consistent with [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-6|Theorem §C9.9.6]].

^sol-px-7-4-3

## H. Short response

### Short response X7.1.1–X7.1.12
*10 variations, 2 HW-literal (X7.1.3: PS5.2(d); X7.1.9: PS7.3)* · question: ![[PHY 513 Practice Midterm 2 (Extended Set)#^px-7-1]]

> [!success]- Solution
> 1. **X7.1.1** $[\phi] = M^{1/2}$, $[\psi] = M^1$, $[g] = M^{1/2}$. ($[\mathcal L] = M^3$; $[\phi] = \frac{d-2}{2}$, $[\psi] = \frac{d-1}{2}$; $[g] = 3 - \frac12 - 2\cdot1$.) — [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-2|Theorem §C1b.3.2]], [[§C1b.3 Mass Dimension, Locality and Power Counting#^thm-c1b-3-3|Theorem §C1b.3.3]]; the $d = 4$ case is [[§C1b.3 Mass Dimension, Locality and Power Counting#^ex-c1b-3-2|Example §C1b.3.2]].
> 2. **X7.1.2** $\partial^2\phi + m^2\phi + 2\lambda(\phi^\ast\phi)\phi = 0$. (Vary $\phi^\ast$: $\partial\mathcal L/\partial(\partial_\mu\phi^\ast) = \partial^\mu\phi$, $\partial\mathcal L/\partial\phi^\ast = -m^2\phi - 2\lambda(\phi^\ast\phi)\phi$; the factor 2 from $(\phi^\ast)^2$.) — [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-9|Theorem §C1b.2.9]] (derived here for the quartic term; method as in [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^ex-c1b-2-2|Example §C1b.2.2]]).
> 3. **X7.1.3** $\gamma_\mu\slashed k\slashed p\slashed q\gamma^\mu = -2\slashed q\slashed p\slashed k$ (reversed order). — [[§C5a.11 Gamma-Matrix Technology#^thm-c5a-11-2|Theorem §C5a.11.2]]; [[PHY 513 PS Drill#^ps5-2-d|PS Drill, PS5.2(d)]].
> 4. **X7.1.4** $(\frac12, 0)\otimes(0, \frac12) = (\frac12, \frac12)$, the four-vector; symmetric traceless $h^{\mu\nu}$: $(1, 1)$, dimension $9$. — [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-12|Theorem §CB.17.12]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]], [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]].
> 5. **X7.1.5** $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$; $\lvert\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}\lvert0\rangle$. — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]].
> 6. **X7.1.6** $\tilde D_R(p) = \dfrac{i}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2}$; its poles sit at $p^0 = \pm E_{\mathbf p} - i\varepsilon$, so the contour passes above both poles. — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]], [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5|Theorem §C2b.5.5]].
> 7. **X7.1.7** $0$ (it is the c-number $iD(x - y)$, which vanishes for $(x - y)^2 < 0$); microcausality. — [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]].
> 8. **X7.1.8** $:\!\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\!: = -\hat b^{s\dagger}_{\mathbf q}\hat b^r_{\mathbf p}$ (one fermion exchange, one sign). — [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]].
> 9. **X7.1.9** $\Theta\hat\psi(x)\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$. — [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|Theorem §C9.9.3]]; [[PHY 513 PS Drill#^ps7-3|PS Drill, PS7.3]] ($\eta_a = 1$).
> 10. **X7.1.10** $(-1)^n$, with the point moved to $-x$ (a derivative counts as an index); $U(\mathcal T)^2 = -1$ on a one-fermion state ($U(\mathcal T)^2 = (-1)^{\hat N_a + \hat N_b}$). — [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]], [[§C9.8 Time Reversal#^thm-c9-8-16|Theorem §C9.8.16]].
> 11. **X7.1.11** $\bar u^r(p)u^s(p) = 2m\,\delta^{rs}$, $\bar v^r(p)v^s(p) = -2m\,\delta^{rs}$, $u^{r\dagger}(p)u^s(p) = 2E_{\mathbf p}\,\delta^{rs}$. — [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-2|Theorem §C5a.10.2]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-4|Theorem §C5a.10.4]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]].
> 12. **X7.1.12** Peskin–Schroeder: $\varepsilon^{0123} = -1$. Course ($\varepsilon^{0123} = +1$): $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$ ($+8\,\mathbf E\cdot\mathbf B$ in Peskin–Schroeder). (With $F_{0i} = E^i$, $F_{jk} = -\varepsilon_{jkl}B^l$: $4\varepsilon^{0ijk}F_{0i}F_{jk} = -4\varepsilon_{ijk}\varepsilon_{jkl}E^iB^l = -8\,\mathbf E\cdot\mathbf B$.) — [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³: these notes versus Peskin–Schroeder]], [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]].
>
> *Checked against:* each home box above (printed and read); X7.1.1 and X7.1.2 are the $d = 3$ and quartic variants, computed here from Theorems §C1b.3.2–§C1b.3.3 and Theorem §C1b.2.9.

^sol-px-7-1
