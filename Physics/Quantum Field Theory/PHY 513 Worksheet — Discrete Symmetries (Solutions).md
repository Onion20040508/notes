---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Discrete Symmetries|Worksheet]] · [[PHY 513 Practice Midterm Solutions|Practice Midterm Solutions]]

# PHY 513 Worksheet — Discrete Symmetries (Solutions)

Solutions to [[PHY 513 Worksheet — Discrete Symmetries]], folded so that you can try first; each problem is embedded above its solution. Every solution works in the course's conventions ([[Larsen PHY 513]]: $U\hat{\mathcal O}U^{-1}$, $\eta_a\gamma^0$, $-i\gamma^2\hat\psi^{\dagger\mathsf T}$, $\gamma^1\gamma^3$ with $U(\mathcal T)$ antiunitary, $\Theta = U(\mathcal C)U(\mathcal P)U(\mathcal T)$) and ends with the line that says how it was checked: *Checked against* names the home box in these notes (or the user's submitted solution, "as written"); *Derived here; check* marks a result with no home box, derived from boxes that exist, with the independent check that was made. Every sign of a bilinear was also compared with the table on Peskin–Schroeder p. 71 (rendered and read), which agrees entry by entry with [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]]. All matrix identities below, the spinor relations (random momenta and spin axes), the charge-conjugation matrix in three bases and in a random unitary basis, and the $C$, $T$, $CPT$ signs of all sixteen bilinears at the operator level (fermion exchange included, on the Fock space of four fermionic modes) were checked numerically: `qft-C/review/worksheets/discrete/check.py`. A printable copy is `~/Downloads/PHY513_worksheet_discrete_solutions.pdf`.

---

## The discrete Lorentz transformations

### W1. Points, momenta and derivatives

![[PHY 513 Worksheet — Discrete Symmetries#^wd-1]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-1-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-1-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-1-c]]

> [!success]- Solution
> **Answers.** (a) $\mathcal P$: $\det = -1$, $\Lambda^0{}_0 = +1$; $\mathcal T$: $\det = -1$, $\Lambda^0{}_0 = -1$; $\mathcal P\mathcal T = -\mathbb 1$: $\det = +1$, $\Lambda^0{}_0 = -1$. Boosts and rotations keep $\Lambda^0{}_0 \ge 1$, and the sign of $\Lambda^0{}_0$ cannot jump; $\mathcal P\mathcal T \in SO(1,3)$ but is not orthochronous. (b) As stated. (c) $\mathcal Pp$ is on the upper shell, $\mathcal Tp$ on the lower; the time-reversed state carries $-\mathbf p$, the momentum $-\mathcal Tp = \mathcal Pp = \tilde p$.
>
> **(a) Step 1** (the numbers). Both matrices are diagonal, so the determinant is the product of the diagonal entries: $\det\mathcal P = 1\cdot(-1)^3 = -1$, $\det\mathcal T = (-1)\cdot1^3 = -1$, $\det(\mathcal P\mathcal T) = \det(-\mathbb 1_4) = (-1)^4 = +1$. $\Lambda^0{}_0$ is the first entry: $+1$, $-1$, $-1$. Slide 7's "$\det\Lambda = 1$" for $\mathcal T$ and $\mathcal P$ is a slip; it is $\mathcal P\mathcal T$ that has determinant $+1$.
>
> **Step 2** (no path from the identity). Every $\Lambda \in O(1,3)$ has $(\Lambda^0{}_0)^2 = 1 + \sum_i(\Lambda^i{}_0)^2 \ge 1$, so $\Lambda^0{}_0$ never lies in $(-1, 1)$, and both $\det\Lambda = \pm1$ and the sign of $\Lambda^0{}_0$ are continuous functions on the group with values in a disconnected set: constant along any continuous path. Boosts have $\Lambda^0{}_0 = \cosh\eta \ge 1$, rotations $\Lambda^0{}_0 = 1$, and products of them keep $\Lambda^0{}_0 \ge 1$ and $\det = 1$. So $\mathcal T$ ($\det = -1$, $\Lambda^0{}_0 = -1$) is out of reach; so is $\mathcal P\mathcal T$, which has the right determinant but $\Lambda^0{}_0 = -1$: $SO(1,3) = \{\det\Lambda = 1\}$ has two components, and only the one with $\Lambda^0{}_0 \ge 1$ is $SO^+(1,3)$. An exponential $\exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ lies on the path $s \mapsto \exp(-\frac i2s\,\omega_{\mu\nu}\mathcal J^{\mu\nu})$ from $\mathbb 1$, so it is never discrete.
>
> **(b) Step 1** (products). $\tilde p\cdot x = p^0t - (-\mathbf p)\cdot\mathbf x = p^0t + \mathbf p\cdot\mathbf x$ and $p\cdot\tilde x = p^0t - \mathbf p\cdot(-\mathbf x)$, the same. $p\cdot x_T = p^0(-t) - \mathbf p\cdot\mathbf x = -(p^0t + \mathbf p\cdot\mathbf x) = -\tilde p\cdot x$.
>
> **Step 2** (chain rule). $y^\nu = \tilde x^\nu = \mathcal P^\nu{}_\rho x^\rho$ has $\partial y^\nu/\partial x^\mu = \mathcal P^\nu{}_\mu$, so $\partial_\mu[f(\tilde x)] = \mathcal P^\nu{}_\mu(\partial_\nu f)(\tilde x)$: $\partial_0$ unchanged, $\partial_i \to -\partial_i$. For $x_T^\nu = \mathcal T^\nu{}_\rho x^\rho$ with $\mathcal T = -\mathcal P$: $\partial_\mu[f(x_T)] = \mathcal T^\nu{}_\mu(\partial_\nu f)(x_T) = -\mathcal P^\nu{}_\mu(\partial_\nu f)(x_T)$: $\partial_0 \to -\partial_0$, $\partial_i$ unchanged.
>
> **(c) Step 1** (the shells). $\mathcal Pp = (E_{\mathbf p}, -\mathbf p)$: positive energy, on shell, the momentum with label $-\mathbf p$. $\mathcal Tp = (-E_{\mathbf p}, \mathbf p)$: negative time component, on the lower sheet; $\mathcal T$ exchanges the two sheets.
>
> **Step 2** (the time-reversed state). Running the movie backwards keeps the energy positive and reverses the velocity, $\mathbf p \to -\mathbf p$. The on-shell vector with these properties is $(E_{\mathbf p}, -\mathbf p) = -\mathcal Tp = \mathcal Pp = \tilde p$, not $\mathcal Tp$. This is why time reversal maps $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$ (and, for spin, $s \to -s$), and why its law involves $\tilde p$ although the point goes to $x_T$: by (b), $e^{-ip\cdot x_T} = e^{i\tilde p\cdot x}$, and the sign of the exponent can only be repaired by an antilinear operator (W10).
>
> *Checked against:* (a) [[§C9.1 Discrete Lorentz Transformations#^cau-c9-1-2|§C9.1, Caution: Slide 7's determinants]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]], [[§C9.1 Discrete Lorentz Transformations#^rem-c9-1-2|§C9.1, Remark: What Lecture 11 adds to the four pieces]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]]; (b) [[§C9.1 Discrete Lorentz Transformations#^thm-c9-1-1|Theorem §C9.1.1]] (items 3–4), [[§C9.8 Time Reversal#^def-c9-8-1|Def. §C9.8.1]], the $\partial_\mu$ row of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]] and step 2 of [[§C9.8 Time Reversal#^der-c9-8-15|Derivation §C9.8.15]]; (c) [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], [[§C9.8 Time Reversal#^def-c9-8-2|Def. §C9.8.2]], [[§C9.8 Time Reversal#^rem-c9-8-1|§C9.8, Remark: A movie run backwards]].

^sol-wd-1

## Parity

### W2. Parity on the real scalar field: scalar and pseudoscalar

![[PHY 513 Worksheet — Discrete Symmetries#^wd-2]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-2-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-2-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-2-c]]

> [!success]- Solution
> **Answers.** (a) $\eta = \pm1$; $U(\mathcal P)|\mathbf p\rangle = \eta|-\mathbf p\rangle$, $U(\mathcal P)^2 = \mathbb 1$. (b) $\hat\pi \to \eta\hat\pi(\tilde x)$, $\nabla\hat\phi \to -\eta(\nabla\hat\phi)(\tilde x)$, $\hat{\mathcal L} \to \hat{\mathcal L}(\tilde x)$ for $\eta = \pm1$. (c) $g\hat\phi\mathsf S$ needs $\eta = +1$ (scalar), $g'\hat\phi\mathsf P$ needs $\eta = -1$ (pseudoscalar); with both, parity is broken.
>
> **(a) Step 1** (creators). $U(\mathcal P)$ is unitary, so $U\hat a^\dagger_{\mathbf p}U^{-1} = (U\hat a_{\mathbf p}U^{-1})^\dagger = \eta^{\ast}\hat a^\dagger_{-\mathbf p}$.
>
> **Step 2** (the field). The numbers $1/\sqrt{2E_{\mathbf p}}$ and $e^{\mp ip\cdot x}$ pass the linear $U$:
>
> $$
> U\hat\phi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\eta\,\hat a_{-\mathbf p}e^{-ip\cdot x} + \eta^{\ast}\hat a^\dagger_{-\mathbf p}e^{ip\cdot x}\bigr) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\eta\,\hat a_{\mathbf p}e^{-ip\cdot\tilde x} + \eta^{\ast}\hat a^\dagger_{\mathbf p}e^{ip\cdot\tilde x}\bigr) ,
> $$
>
> relabelling $\mathbf p \to -\mathbf p$ (Jacobian $1$, $E_{-\mathbf p} = E_{\mathbf p}$, $p \to \tilde p$ in the exponents) and $\tilde p\cdot x = p\cdot\tilde x$ (W1(b)).
>
> **Step 3** (compare). $\eta\hat\phi(\tilde x)$ carries $\eta$ in front of both terms. The difference is $(\eta^{\ast} - \eta)\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\hat a^\dagger_{\mathbf p}e^{ip\cdot\tilde x}$; its commutator with $\hat a_{\mathbf q}$ is $(\eta^{\ast} - \eta)e^{iq\cdot\tilde x}/\sqrt{2E_{\mathbf q}}$, zero for all $x$ only if $\eta^{\ast} = \eta$. With $|\eta| = 1$: $\eta = \pm1$. (Shortcut: $\hat\phi$ is Hermitian, and so is $U\hat\phi U^{-1}$; $\eta\hat\phi(\tilde x)$ is Hermitian only for real $\eta$.)
>
> **Step 4** (states). $U|\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,(U\hat a^\dagger_{\mathbf p}U^{-1})\,U|0\rangle = \eta^{\ast}|-\mathbf p\rangle = \eta|-\mathbf p\rangle$. $U^2\hat a_{\mathbf p}U^{-2} = \eta^2\hat a_{\mathbf p} = \hat a_{\mathbf p}$ and $U^2|0\rangle = |0\rangle$, so $U^2 = \mathbb 1$ on the Fock space.
>
> **(b) Step 1** (derivatives). $U$ does not depend on $x$, so $U\partial_\mu\hat\phi(x)U^{-1} = \partial_\mu\bigl(\eta\hat\phi(\tilde x)\bigr) = \eta\,\mathcal P^\nu{}_\mu(\partial_\nu\hat\phi)(\tilde x)$ (W1(b)): $\hat\pi = \partial_t\hat\phi \to \eta\hat\pi(\tilde x)$ and $\nabla\hat\phi \to -\eta(\nabla\hat\phi)(\tilde x)$.
>
> **Step 2** (the Lagrangian). $U(\hat A\hat B)U^{-1} = (U\hat AU^{-1})(U\hat BU^{-1})$. In $\hat{\mathcal L} = \frac12\hat\pi^2 - \frac12(\nabla\hat\phi)^2 - \frac12m^2\hat\phi^2$ each term is quadratic, so it acquires $\eta^2 = 1$ (and $(-\eta)^2 = 1$ for the gradient term): $U\hat{\mathcal L}(x)U^{-1} = \hat{\mathcal L}(\tilde x)$, and $\int d^4x$ is unchanged by $x \to \tilde x$ (Jacobian $|\det\mathcal P| = 1$). The free theory does not decide the sign of $\eta$.
>
> **(c)** The two factors act on different Hilbert-space factors, so their images multiply: $U(\hat\phi\mathsf S)(x)U^{-1} = \eta\,\hat\phi\mathsf S(\tilde x)$ and $U(\hat\phi\mathsf P)(x)U^{-1} = -\eta\,\hat\phi\mathsf P(\tilde x)$. The first coupling is invariant (up to $x \to \tilde x$, harmless in the action) iff $\eta = +1$: $\hat\phi$ is a scalar field; the second iff $\eta = -1$: a pseudoscalar field. With both couplings present no $\eta$ works: parity is violated. Which parity a real field has is decided by its interactions (the pions couple like pseudoscalars).
>
> *Checked against:* [[§C9.2 Parity of the Scalar Field#^thm-c9-2-10|Theorem §C9.2.10]] with [[§C9.2 Parity of the Scalar Field#^der-c9-2-10|Derivation §C9.2.10]] and [[§C9.2 Parity of the Scalar Field#^der-c9-2-10b|Derivation §C9.2.10b]]; [[§C9.2 Parity of the Scalar Field#^thm-c9-2-5|Theorem §C9.2.5]]; [[§C9.2 Parity of the Scalar Field#^thm-c9-2-11|Theorem §C9.2.11]]; [[§C9.2 Parity of the Scalar Field#^def-c9-2-3|Def. §C9.2.3]] and [[§C9.2 Parity of the Scalar Field#^rem-c9-2-5|§C9.2, Remark: Which parity a real field has is decided by its interactions]].

^sol-wd-2

### W3. Parity on the complex scalar field

![[PHY 513 Worksheet — Discrete Symmetries#^wd-3]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-3-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-3-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-3-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-3-d]]

> [!success]- Solution
> **Answers.** (a) Holds iff $\eta_b = \eta_a^{\ast}$. (b) $\hat\phi^\dagger \to \eta_a^{\ast}\hat\phi^\dagger(\tilde x)$; $\hat j^\mu \to \mathcal P^\mu{}_\nu\hat j^\nu(\tilde x)$, independent of $\eta_a$. (c) $\eta_a^{\ast}$ and $\eta_b^{\ast} = \eta_a$, product $+1$; the pair has parity $(-1)^L$. (d) $\eta_a' = e^{i\theta/2}\eta_a$, $\eta_b' = e^{-i\theta/2}\eta_b$; the single phase is a convention, the product $\eta_a\eta_b = 1$ is physical.
>
> **(a) Step 1** (transform). As in W2: $U\hat b^\dagger_{\mathbf p}U^{-1} = \eta_b^{\ast}\hat b^\dagger_{-\mathbf p}$, and after relabelling $\mathbf p \to -\mathbf p$,
>
> $$
> U\hat\phi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\eta_a\,\hat a_{\mathbf p}e^{-ip\cdot\tilde x} + \eta_b^{\ast}\,\hat b^\dagger_{\mathbf p}e^{ip\cdot\tilde x}\bigr) .
> $$
>
> **Step 2** (compare with $\eta_a\hat\phi(\tilde x)$). The $\hat a$ terms agree. The difference is $(\eta_b^{\ast} - \eta_a)\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\hat b^\dagger_{\mathbf p}e^{ip\cdot\tilde x}$, whose commutator with $\hat b_{\mathbf q}$ is $(\eta_b^{\ast} - \eta_a)e^{iq\cdot\tilde x}/\sqrt{2E_{\mathbf q}}$: it vanishes iff $\eta_b^{\ast} = \eta_a$, i.e. $\eta_b = \eta_a^{\ast}$, and then $\eta_a\eta_b = |\eta_a|^2 = 1$. With $\eta_a = \eta_b = 1$, $U(\mathcal P)$ gives the law the problem set asks for, $\hat\phi(t, -\mathbf x)$.
>
> **(b) Step 1** (adjoint). $U\hat\phi^\dagger U^{-1} = (U\hat\phi U^{-1})^\dagger = \eta_a^{\ast}\hat\phi^\dagger(\tilde x)$.
>
> **Step 2** (current). By W1(b), $U\partial^\mu\hat\phi(x)U^{-1} = \eta_a\mathcal P^\mu{}_\nu(\partial^\nu\hat\phi)(\tilde x)$ (raised index; $\mathcal P$ is diagonal) and $U\partial^\mu\hat\phi^\dagger U^{-1} = \eta_a^{\ast}\mathcal P^\mu{}_\nu(\partial^\nu\hat\phi^\dagger)(\tilde x)$. Each term of $\hat j^\mu = i(\hat\phi\,\partial^\mu\hat\phi^\dagger - \hat\phi^\dagger\partial^\mu\hat\phi)$ contains one $\hat\phi$ and one $\hat\phi^\dagger$, hence the factor $\eta_a\eta_a^{\ast} = 1$, and one derivative: $U\hat j^\mu(x)U^{-1} = \mathcal P^\mu{}_\nu\hat j^\nu(\tilde x)$, a vector: $\hat j^0$ even, $\hat{\mathbf j}$ odd. The problem set's $J^\mu = -\hat j^\mu$ obeys the same rule.
>
> **(c) Step 1** (intrinsic parities). $U|\mathbf p\rangle = \eta_a^{\ast}|-\mathbf p\rangle$ and $U|\mathbf p\rangle^c = \eta_b^{\ast}|-\mathbf p\rangle^c = \eta_a|-\mathbf p\rangle^c$; at rest these are eigenvalue equations. Product $\eta_a^{\ast}\eta_b^{\ast} = (\eta_a\eta_b)^{\ast} = 1$.
>
> **Step 2** (the pair). $U\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}|0\rangle = \eta_a^{\ast}\eta_b^{\ast}\,\hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p}|0\rangle = \hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p}|0\rangle$. In $\int d^3p\,\Phi_{LM}(\mathbf p)\hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p}|0\rangle$ substitute $\mathbf p \to -\mathbf p$: $\int d^3p\,\Phi_{LM}(-\mathbf p)\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}|0\rangle = (-1)^L$ times the original state.
>
> **(d) Step 1** (the charge rotation). $[\hat Q, \hat a_{\mathbf p}] = -\frac12\hat a_{\mathbf p}$ and $[\hat Q, \hat b_{\mathbf p}] = +\frac12\hat b_{\mathbf p}$ (from $[\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a_{\mathbf p}] = -(2\pi)^3\delta^3(\mathbf q - \mathbf p)\hat a_{\mathbf q}$). The Baker–Hausdorff series then sums to $e^{-i\theta\hat Q}\hat a_{\mathbf p}e^{i\theta\hat Q} = e^{i\theta/2}\hat a_{\mathbf p}$, $e^{-i\theta\hat Q}\hat b_{\mathbf p}e^{i\theta\hat Q} = e^{-i\theta/2}\hat b_{\mathbf p}$.
>
> **Step 2** (the new operator). $U' = e^{-i\theta\hat Q}U(\mathcal P)$ is unitary, $U'|0\rangle = |0\rangle$ ($\hat Q|0\rangle = 0$), and $U'\hat a_{\mathbf p}U'^{-1} = e^{-i\theta\hat Q}\eta_a\hat a_{-\mathbf p}e^{i\theta\hat Q} = e^{i\theta/2}\eta_a\hat a_{-\mathbf p}$, likewise $\eta_b' = e^{-i\theta/2}\eta_b$. Then $\eta_b' = \eta_a'^{\ast}$ still holds, so $U'\hat\phi U'^{-1} = \eta_a'\hat\phi(\tilde x)$, and $\eta_a'\eta_b' = \eta_a\eta_b = 1$. Since $\theta$ is arbitrary, $\eta_a'$ can be any phase: it is a convention, the freedom to combine parity with a charge rotation, which commutes with it ($[U(\mathcal P), \hat Q] = 0$). The product, and hence the parity $(-1)^L$ of a particle–antiparticle pair, is not. For the real field $\hat Q = 0$ and $\eta = \pm1$ is fixed (W2).
>
> *Checked against:* [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|Theorem §C9.2.2]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-3|Theorem §C9.2.3]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-4|Theorem §C9.2.4]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-6|Theorem §C9.2.6]] (row $\hat j^\mu$), [[§C9.2 Parity of the Scalar Field#^thm-c9-2-8|Theorem §C9.2.8]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-9|Theorem §C9.2.9]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-12|Theorem §C9.2.12]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-13|Theorem §C9.2.13]] and [[§C9.2 Parity of the Scalar Field#^thm-c9-2-14|Theorem §C9.2.14]] (with $q = \frac12$ for this $\hat Q$, [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]]); the problem set's $J^\mu = -\hat j^\mu$: [[§C9.10 C, T and CPT for the Complex Scalar Field#^cau-c9-10-1|§C9.10, Caution: The star of a scalar field operator is the adjoint]].

^sol-wd-3

### W4. Dirac parity from the modes

![[PHY 513 Worksheet — Discrete Symmetries#^wd-4]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-4-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-4-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-4-c]]

> [!success]- Solution
> **Answers.** (a) $p\cdot\sigma = p^0 - \mathbf p\cdot\boldsymbol\sigma = \tilde p\cdot\bar\sigma$; $u^s(\tilde p) = \gamma^0u^s(p)$, $v^s(\tilde p) = -\gamma^0v^s(p)$. (b) The law holds iff $\eta_b^{\ast} = -\eta_a$, i.e. $\eta_a\eta_b = -1$. (c) $U(\mathcal P)\hat{\bar\psi}(x)U(\mathcal P)^{-1} = \eta_a^{\ast}\hat{\bar\psi}(\tilde x)\gamma^0$; intrinsic parities $\eta_a^{\ast}$, $\eta_b^{\ast}$ with product $-1$; pair parity $(-1)^{L+1}$; positronium's $L = 0$ ground state is parity odd, a scalar pair's even.
>
> **(a) Step 1** (the $2\times2$ identity). With $\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$: $p\cdot\sigma = p^0 - \mathbf p\cdot\boldsymbol\sigma$ and $\tilde p\cdot\bar\sigma = p^0 - (-\mathbf p)\cdot(-\boldsymbol\sigma) = p^0 - \mathbf p\cdot\boldsymbol\sigma$: equal. Likewise $p\cdot\bar\sigma = \tilde p\cdot\sigma$. For on-shell $p$ both are positive matrices, so their positive square roots agree too.
>
> **Step 2** (the spinors). $u^s(\tilde p) = \bigl(\sqrt{\tilde p\cdot\sigma}\,\xi^s, \sqrt{\tilde p\cdot\bar\sigma}\,\xi^s\bigr) = \bigl(\sqrt{p\cdot\bar\sigma}\,\xi^s, \sqrt{p\cdot\sigma}\,\xi^s\bigr)$: the two blocks of $u^s(p)$ swapped, which is what $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$ does. $v^s(\tilde p) = \bigl(\sqrt{p\cdot\bar\sigma}\,\eta^s, -\sqrt{p\cdot\sigma}\,\eta^s\bigr)$, while $\gamma^0v^s(p) = \bigl(-\sqrt{p\cdot\bar\sigma}\,\eta^s, \sqrt{p\cdot\sigma}\,\eta^s\bigr)$: so $v^s(\tilde p) = -\gamma^0v^s(p)$. The relative minus sign is the one of the lower block of $v$.
>
> **(b) Step 1** (act on the operators). The spinors and exponentials are numbers for $U$; with $U\hat b^{s\dagger}_{\mathbf p}U^{-1} = \eta_b^{\ast}\hat b^{s\dagger}_{-\mathbf p}$,
>
> $$
> U\hat\psi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\eta_a\hat a^s_{-\mathbf p}u^s(p)e^{-ip\cdot x} + \eta_b^{\ast}\hat b^{s\dagger}_{-\mathbf p}v^s(p)e^{ip\cdot x}\bigr) .
> $$
>
> **Step 2** (relabel and use (a)). $\mathbf p \to -\mathbf p$ turns $p$ into $\tilde p$ in the spinors and exponents; $e^{\mp i\tilde p\cdot x} = e^{\mp ip\cdot\tilde x}$; $u^s(\tilde p) = \gamma^0u^s(p)$, $v^s(\tilde p) = -\gamma^0v^s(p)$; the constant $\gamma^0$ comes out of the integral:
>
> $$
> U\hat\psi(x)U^{-1} = \gamma^0\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\eta_a\hat a^s_{\mathbf p}u^s(p)e^{-ip\cdot\tilde x} - \eta_b^{\ast}\hat b^{s\dagger}_{\mathbf p}v^s(p)e^{ip\cdot\tilde x}\bigr) .
> $$
>
> **Step 3** (compare with $\eta_a\gamma^0\hat\psi(\tilde x)$). The $\hat a$ terms agree; the $\hat b^\dagger$ terms agree iff $-\eta_b^{\ast} = \eta_a$ (otherwise the difference has a nonzero anticommutator with $\hat b^r_{\mathbf q}$, as in W3). So $\eta_b^{\ast} = -\eta_a$, and multiplying by $\eta_b$: $1 = -\eta_a\eta_b$.
>
> **(c) Step 1** ($\hat{\bar\psi}$). Componentwise $U\hat\psi_a^\dagger U^{-1} = (U\hat\psi_aU^{-1})^\dagger$, so as a row $U\hat\psi^\dagger U^{-1} = \eta_a^{\ast}\hat\psi^\dagger(\tilde x)\gamma^0$ ($\gamma^0$ Hermitian), and $U\hat{\bar\psi}U^{-1} = \eta_a^{\ast}\hat\psi^\dagger(\tilde x)\gamma^0\gamma^0 = \eta_a^{\ast}\hat\psi^\dagger(\tilde x) = \eta_a^{\ast}\hat{\bar\psi}(\tilde x)\gamma^0$, using $\hat\psi^\dagger = \hat{\bar\psi}\gamma^0$.
>
> **Step 2** (intrinsic parities and the pair). $U|\mathbf p, s\rangle = \eta_a^{\ast}|-\mathbf p, s\rangle$, $U|\mathbf p, s\rangle^c = \eta_b^{\ast}|-\mathbf p, s\rangle^c$, with $\eta_a^{\ast}\eta_b^{\ast} = (\eta_a\eta_b)^{\ast} = -1$: opposite intrinsic parities (for real phases $\eta_b = -\eta_a$). For $\sum_{s,s'}\int d^3p\,\Phi_L(\mathbf p)C_{ss'}\hat a^{s\dagger}_{\mathbf p}\hat b^{s'\dagger}_{-\mathbf p}|0\rangle$, parity gives the factor $-1$, leaves the spins alone, and flips the momenta; relabelling as in W3(c) gives $(-1)^L$: total $(-1)^{L+1}$. Positronium in its $L = 0$ ground state has parity $-1$ (as do the pions, $q\bar q$ with $L = 0$: pseudoscalars), a scalar particle–antiparticle pair $+1$.
>
> *Checked against:* [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-2|Theorem §C9.3.2]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-3|Theorem §C9.3.3]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-4|Theorem §C9.3.4]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-5|Theorem §C9.3.5]] with [[§C9.3 Parity on States, Spinors and the Dirac Field#^der-c9-3-5|Derivation §C9.3.5]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-6|Theorem §C9.3.6]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|Theorem §C9.4.1]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-7|Theorem §C9.3.7]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-8|Theorem §C9.3.8]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^rem-c9-3-4|§C9.3, Remark: Positronium and the pions]]; the spinor relations also numerically (random $\mathbf p$ and spin axis).

^sol-wd-4

### W5. Bilinears under parity

![[PHY 513 Worksheet — Discrete Symmetries#^wd-5]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-5-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-5-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-5-c]]

> [!success]- Solution
> **Answers.** (a) $\mathsf A^\mu(x) \to -\mathcal P^\mu{}_\nu\mathsf A^\nu(\tilde x)$ ($\mathsf A^0$ flips, $\mathsf A^i$ do not); $\mathsf T^{\mu\nu}(x) \to \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(\tilde x)$ ($\mathsf T^{0i}$ flips, $\mathsf T^{ij}$ does not). (b) $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$, $\mathsf P \to -\mathsf P(\tilde x)$; $\eta_a^{\ast}$ comes from the adjoint and cancels against $\eta_a$; PS's order changes nothing. (c) $\hat\psi_L \to \eta_a\gamma^0\hat\psi_R(\tilde x)$; $\overline{\hat\psi_L}\gamma^\mu\hat\psi_L \to \mathcal P^\mu{}_\nu\overline{\hat\psi_R}\gamma^\nu\hat\psi_R(\tilde x)$.
>
> **(a) Step 1** (the general bilinear). With $U\hat{\bar\psi}U^{-1} = \eta_a^{\ast}\hat{\bar\psi}(\tilde x)\gamma^0$ (W4(c)) and $U\hat\psi U^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$, inserting $U^{-1}U = \mathbb 1$ between the fields and using $|\eta_a|^2 = 1$: $U\hat{\bar\psi}\Gamma\hat\psi(x)U^{-1} = \hat{\bar\psi}(\tilde x)\,\gamma^0\Gamma\gamma^0\,\hat\psi(\tilde x)$.
>
> **Step 2** (one identity for all $\mu$). From $\{\gamma^\mu, \gamma^0\} = 2g^{\mu0}$ and $(\gamma^0)^2 = \mathbb 1$: $\gamma^0\gamma^\mu\gamma^0 = \gamma^0(2g^{\mu0} - \gamma^0\gamma^\mu) = 2g^{\mu0}\gamma^0 - \gamma^\mu$, i.e. $\gamma^0$ for $\mu = 0$ and $-\gamma^i$ for $\mu = i$: $\gamma^0\gamma^\mu\gamma^0 = \mathcal P^\mu{}_\nu\gamma^\nu$.
>
> **Step 3** (axial vector). $\gamma^5$ anticommutes with $\gamma^0$, so $\gamma^0\gamma^\mu\gamma^5\gamma^0 = -\gamma^0\gamma^\mu\gamma^0\gamma^5 = -\mathcal P^\mu{}_\nu\gamma^\nu\gamma^5$, and $U\mathsf A^\mu(x)U^{-1} = -\mathcal P^\mu{}_\nu\mathsf A^\nu(\tilde x)$: $\mathsf A^0 \to -\mathsf A^0(\tilde x)$, $\mathsf A^i \to +\mathsf A^i(\tilde x)$, "exactly the wrong way" for a vector.
>
> **Step 4** (tensor). Insert $(\gamma^0)^2 = \mathbb 1$ between the two $\gamma$'s: $\gamma^0\gamma^\mu\gamma^\nu\gamma^0 = (\gamma^0\gamma^\mu\gamma^0)(\gamma^0\gamma^\nu\gamma^0) = \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\gamma^\rho\gamma^\sigma$, and the same for the commutator, so $\gamma^0\sigma^{\mu\nu}\gamma^0 = \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\sigma^{\rho\sigma}$ and $U\mathsf T^{\mu\nu}(x)U^{-1} = \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(\tilde x)$: one sign per spatial index, $\mathsf T^{0i} \to -\mathsf T^{0i}$, $\mathsf T^{ij} \to +\mathsf T^{ij}$ (and $\mathsf T^{00} = 0$). In the problem set's notation: $-(-1)^\mu\mathsf A^\mu$ and $(-1)^\mu(-1)^\nu\mathsf T^{\mu\nu}$ (no sum).
>
> **(b) Step 1** (where the phases go). $\eta_a^{\ast}$ enters through $U\hat\psi^\dagger U^{-1} = (U\hat\psi U^{-1})^\dagger$: the dagger conjugates the number $\eta_a$. Every bilinear contains one $\hat{\bar\psi}$ and one $\hat\psi$, so the factor is $\eta_a^{\ast}\eta_a = 1$ for every complex $\eta_a$.
>
> **Step 2** (the two rows). Step 2 of (a): $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$, like $x^\mu$. $\gamma^0(i\gamma^5)\gamma^0 = -i\gamma^5(\gamma^0)^2 = -i\gamma^5$, so $\mathsf P \to -\mathsf P(\tilde x)$ (the $i$ is a number and passes the linear $U$).
>
> **Step 3** (Peskin–Schroeder's $P\cdots P$). Replacing $U$ by $U^{-1}$ replaces each phase by its conjugate; since no bilinear depends on the phases, no sign changes (for $U^2 = \mathbb 1$, i.e. real phases, the two forms coincide anyway).
>
> **(c) ★ Step 1** (the projectors past $\gamma^0$). $\gamma^5\gamma^0 = -\gamma^0\gamma^5$ gives $P_L\gamma^0 = \gamma^0P_R$. So $U\hat\psi_L(x)U^{-1} = P_L\,\eta_a\gamma^0\hat\psi(\tilde x) = \eta_a\gamma^0P_R\hat\psi(\tilde x) = \eta_a\gamma^0\hat\psi_R(\tilde x)$, and likewise $L \leftrightarrow R$.
>
> **Step 2** (the current). $\overline{\hat\psi_L} = \hat{\bar\psi}P_R$, so $\overline{\hat\psi_L}\gamma^\mu\hat\psi_L = \hat{\bar\psi}P_R\gamma^\mu P_L\hat\psi = \hat{\bar\psi}\gamma^\mu P_L\hat\psi$. By (a), its image is $\hat{\bar\psi}(\tilde x)\gamma^0\gamma^\mu P_L\gamma^0\hat\psi(\tilde x) = \hat{\bar\psi}\gamma^0\gamma^\mu\gamma^0P_R\hat\psi(\tilde x) = \mathcal P^\mu{}_\nu\overline{\hat\psi_R}\gamma^\nu\hat\psi_R(\tilde x)$. (Equivalently $\hat{\bar\psi}\gamma^\mu P_L\hat\psi = \frac12(\mathsf V^\mu - \mathsf A^\mu)$ goes to $\frac12\mathcal P(\mathsf V + \mathsf A)$.) A gauge field coupled to the left current alone would, after parity, be coupled to the right one: a different theory, so parity is violated (the weak interaction).
>
> *Checked against:* (a) the user's Problem Set 7, Problem 2(a), as written: [[§C9.4 Fermion Bilinears under Parity#^der-c9-4-4b|Derivation §C9.4.4b]]; [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-2|Theorem §C9.4.2]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-3|Theorem §C9.4.3]], [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]]; PS p. 71, row $P$; (b) [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-1|Theorem §C9.4.1]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^cau-c9-3-1|§C9.3, Caution: Which side the inverse is on, and the names of the phases]], [[§C9.4 Fermion Bilinears under Parity#^cau-c9-4-3|§C9.4, Caution: The (−1)^μ notation and the lowered index of slide 23]]; (c) [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-7|★ Theorem §C9.4.7]], [[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-4|§C9.4, Remark: Discrete symmetries in nature]].

^sol-wd-5

## Charge conjugation

### W6. Charge conjugation on oscillators and spinors

![[PHY 513 Worksheet — Discrete Symmetries#^wd-6]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-6-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-6-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-6-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-6-d]]

> [!success]- Solution
> **Answers.** (a) $\hat a^{s\dagger}_{\mathbf p} \leftrightarrow \hat b^{s\dagger}_{\mathbf p}$, $|\mathbf p, s\rangle \leftrightarrow |\mathbf p, s\rangle^c$, $\hat Q \to -\hat Q$. (b) $\eta^1 = (0, 1)^{\mathsf T}$, $\eta^2 = (-1, 0)^{\mathsf T}$. (c) $\gamma^0$, $\gamma^2$ symmetric, $\gamma^1$, $\gamma^3$ antisymmetric; only $\gamma^2$ is imaginary. (d) As stated.
>
> **(a)** $U(\mathcal C)$ is unitary, so $U\hat a^{s\dagger}_{\mathbf p}U^{-1} = (U\hat a^s_{\mathbf p}U^{-1})^\dagger = \hat b^{s\dagger}_{\mathbf p}$ and $U\hat b^{s\dagger}_{\mathbf p}U^{-1} = \hat a^{s\dagger}_{\mathbf p}$. On states, $U|\mathbf p, s\rangle = \sqrt{2E_{\mathbf p}}\,(U\hat a^{s\dagger}_{\mathbf p}U^{-1})U|0\rangle = |\mathbf p, s\rangle^c$, and back: same momentum, same label $s$. In $\hat Q$, $U(\hat a^\dagger\hat a)U^{-1} = \hat b^\dagger\hat b$ and vice versa, so $U\hat QU^{-1} = \sum_s\int(\hat b^{s\dagger}\hat b^s - \hat a^{s\dagger}\hat a^s) = -\hat Q$.
>
> **(b) Step 1** (antilinear). $J(c\xi) = -i\sigma^2(c\xi)^{\ast} = c^{\ast}J\xi$.
>
> **Step 2** (spin reversal). $-i\sigma^2 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ is real with inverse $i\sigma^2$, and $(-i\sigma^2)(\sigma^i)^{\ast}(i\sigma^2) = \sigma^2(\sigma^i)^{\ast}\sigma^2 = -\sigma^i$ for each $i$ ($\sigma^1, \sigma^3$ real and anticommuting with $\sigma^2$; $(\sigma^2)^{\ast} = -\sigma^2$ commuting with it). So $\sigma^i(-i\sigma^2) = -(-i\sigma^2)(\sigma^i)^{\ast}$, and for real $\hat{\mathbf n}$ and $\lambda$: $(\hat{\mathbf n}\cdot\boldsymbol\sigma)J\xi = -(-i\sigma^2)\bigl((\hat{\mathbf n}\cdot\boldsymbol\sigma)\xi\bigr)^{\ast} = -\lambda J\xi$.
>
> **Step 3** ($J^2$). $J^2\xi = (-i\sigma^2)\bigl((-i\sigma^2)\xi^{\ast}\bigr)^{\ast} = (-i\sigma^2)^2\xi = -\mathbb 1\,\xi$ (the matrix is real).
>
> **Step 4** (the antiparticle spinors). $\eta^1 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}\begin{pmatrix}1\\ 0\end{pmatrix} = \begin{pmatrix}0\\ 1\end{pmatrix}$, $\eta^2 = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}\begin{pmatrix}0\\ 1\end{pmatrix} = \begin{pmatrix}-1\\ 0\end{pmatrix}$: spin down and spin up, with the sign that $J^2 = -1$ requires.
>
> **(c) Step 1** (symmetry and reality). $\gamma^0$ is real and symmetric. $(\gamma^i)^{\mathsf T} = \begin{pmatrix}0 & -(\sigma^i)^{\mathsf T}\\ (\sigma^i)^{\mathsf T} & 0\end{pmatrix}$; $\sigma^1$, $\sigma^3$ are symmetric and $\sigma^2$ antisymmetric, so $(\gamma^1)^{\mathsf T} = -\gamma^1$, $(\gamma^3)^{\mathsf T} = -\gamma^3$, $(\gamma^2)^{\mathsf T} = +\gamma^2$. Only $\sigma^2$ is imaginary, so only $\gamma^2$ is: $(\gamma^2)^{\ast} = -\gamma^2$.
>
> **Step 2** (the identity). $\gamma^0\gamma^2$ anticommutes with $\gamma^0$ and $\gamma^2$ (one exchange with the other factor, and $\gamma^\mu$ commutes with itself) and commutes with $\gamma^1$, $\gamma^3$ (two exchanges). For $\mu = 0, 2$: $(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = \gamma^\mu\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$; for $\mu = 1, 3$: $-\gamma^\mu\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$. And $\gamma^0\gamma^2\gamma^0\gamma^2 = -(\gamma^0)^2(\gamma^2)^2 = -(\mathbb 1)(-\mathbb 1) = \mathbb 1$.
>
> **(d) Step 1** (the matrix). $-i\gamma^2 = \begin{pmatrix}0 & -i\sigma^2\\ i\sigma^2 & 0\end{pmatrix}$, so $-i\gamma^2v^s(p) = \bigl(i\sigma^2\sqrt{p\cdot\bar\sigma}\,\eta^s, i\sigma^2\sqrt{p\cdot\sigma}\,\eta^s\bigr)$.
>
> **Step 2** (insert $\eta^s = -i\sigma^2(\xi^s)^{\ast}$). $i\sigma^2(-i\sigma^2) = (\sigma^2)^2 = \mathbb 1$ is not what appears; what appears is $i\sigma^2 f(\cdot)(-i\sigma^2) = \sigma^2f(\cdot)\sigma^2$. From Step 2 of (b), $\sigma^2(\mathbf p\cdot\boldsymbol\sigma)\sigma^2 = -\mathbf p\cdot\boldsymbol\sigma^{\ast}$, so $\sigma^2(p\cdot\bar\sigma)\sigma^2 = p^0 - \mathbf p\cdot\boldsymbol\sigma^{\ast} = (p\cdot\sigma)^{\ast}$; conjugation by the unitary $\sigma^2$ commutes with the positive square root, and the square root of $(p\cdot\sigma)^{\ast}$ is $\bigl(\sqrt{p\cdot\sigma}\bigr)^{\ast}$. Hence the upper block is $\sqrt{p\cdot\sigma}^{\,\ast}(\xi^s)^{\ast}$ and the lower $\sqrt{p\cdot\bar\sigma}^{\,\ast}(\xi^s)^{\ast}$: together $u^s(p)^{\ast}$.
>
> **Step 3** (the partner). $(-i\gamma^2)^2 = \mathbb 1$ and $-i\gamma^2$ is real, so also $v^s = -i\gamma^2u^{s\ast}$, $u^s = -i\gamma^2v^{s\ast}$, $v^{s\ast} = -i\gamma^2u^s$ (PS (3.144) is the last two).
>
> *Checked against:* [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-1|Theorem §C9.5.1]], [[§C9.6 Charge Conjugation on the Field and Bilinears#^rem-c9-6-4|§C9.6, Remark: The number current flips]] ($\hat Q \to -\hat Q$; [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]]); [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-3|Theorem §C9.5.3]], [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-5|Def. §C9.5.5]], [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-2|§C9.5, Caution: The sign in ξ^{−s}]]; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-4|Theorem §C9.5.4]]; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-5|Theorem §C9.5.5]], [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-6|Theorem §C9.5.6]]; PS eq. (3.144) (p. 70, read); all relations numerically.

^sol-wd-6

### W7. Charge conjugation on the field, in any basis

![[PHY 513 Worksheet — Discrete Symmetries#^wd-7]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-7-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-7-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-7-c]]

> [!success]- Solution
> **Answers.** (a) The law follows from $v^s = -i\gamma^2u^{s\ast}$, $u^s = -i\gamma^2v^{s\ast}$; with $\eta^s = \xi^s$ the $\hat a^\dagger$ terms come back with the wrong spinors. (b) $U(\mathcal C)\hat{\bar\psi}(x)U(\mathcal C)^{-1} = \bigl(-i\gamma^0\gamma^2\hat\psi(x)\bigr)^{\mathsf T}$. (c) $B = -i\gamma^2$ (chiral and Dirac bases), $B = \mathbb 1$ (Majorana basis, up to a phase).
>
> **(a) Step 1** (the left side). $U(\mathcal C)$ is linear and swaps $\hat a \leftrightarrow \hat b$ at fixed $\mathbf p$, $s$ (W6(a)):
>
> $$
> U\hat\psi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat b^s_{\mathbf p}u^s(p)e^{-ip\cdot x} + \hat a^{s\dagger}_{\mathbf p}v^s(p)e^{ip\cdot x}\bigr) .
> $$
>
> **Step 2** (the right side). Taking the dagger of each component (operators) and the complex conjugate of each number, $\hat\psi^{\dagger\mathsf T}(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p}u^s(p)^{\ast}e^{ip\cdot x} + \hat b^s_{\mathbf p}v^s(p)^{\ast}e^{-ip\cdot x}\bigr)$. Multiply by the constant $-i\gamma^2$ and use W6(d): $-i\gamma^2u^{s\ast} = v^s$, $-i\gamma^2v^{s\ast} = u^s$. Term by term this is Step 1. The point $x$ does not move.
>
> **Step 3** (only if). The coefficient of $e^{ip\cdot x}$ is extracted by anticommuting with $\hat a^r_{\mathbf q}$: equality of the two sides requires $v^s(p) = -i\gamma^2u^s(p)^{\ast}$ for each $s$. With $\eta^s = \xi^s$, $-i\gamma^2u^s(p)^{\ast}$ is the negative-frequency spinor built on $-i\sigma^2(\xi^s)^{\ast} = \xi^{-s}$, not on $\xi^s$: for the standard basis the right side would carry $\hat a^{1\dagger}$ with the spinor of $s = 2$ and $\hat a^{2\dagger}$ with minus that of $s = 1$. The law fails; this is why the course fixes $\eta^s = \xi^{-s}$.
>
> **(b) Step 1** (the conventions' form). $\hat{\bar\psi}\gamma^0\gamma^2 = \hat\psi^\dagger(\gamma^0)^2\gamma^2 = \hat\psi^\dagger\gamma^2$, a row; its transpose is the column $(\gamma^2)^{\mathsf T}\hat\psi^{\dagger\mathsf T} = \gamma^2\hat\psi^{\dagger\mathsf T}$ ($\gamma^2$ symmetric). So $-i(\hat{\bar\psi}\gamma^0\gamma^2)^{\mathsf T} = -i\gamma^2\hat\psi^{\dagger\mathsf T}$; no operators are reordered, only arranged.
>
> **Step 2** ($\hat\psi^\dagger$). Componentwise, $U\hat\psi_a^\dagger U^{-1} = (U\hat\psi_aU^{-1})^\dagger = \bigl(-i\sum_b(\gamma^2)_{ab}\hat\psi_b^\dagger\bigr)^\dagger = i\sum_b(\gamma^2)^{\ast}_{ab}\hat\psi_b = -i\sum_b(\gamma^2)_{ab}\hat\psi_b$: the row $U\hat\psi^\dagger U^{-1} = (-i\gamma^2\hat\psi)^{\mathsf T}$.
>
> **Step 3** ($\hat{\bar\psi}$). $U\hat{\bar\psi}U^{-1} = (-i\gamma^2\hat\psi)^{\mathsf T}\gamma^0 = \bigl((\gamma^0)^{\mathsf T}(-i\gamma^2)\hat\psi\bigr)^{\mathsf T} = \bigl(-i\gamma^0\gamma^2\hat\psi\bigr)^{\mathsf T}$, PS eq. (3.146).
>
> **(c) Step 1** (Dirac equation). Take the Dirac equation $(i\gamma^\mu\partial_\mu - m)\hat\psi = 0$ component by component and apply the dagger: the numbers $i(\gamma^\mu)_{ab}$ are conjugated, $\bigl(-i(\gamma^\mu)^{\ast}\partial_\mu - m\bigr)\hat\psi^{\dagger\mathsf T} = 0$. Multiply by $B$ and insert $B^{-1}B$: $-iB(\gamma^\mu)^{\ast}B^{-1}\partial_\mu(B\hat\psi^{\dagger\mathsf T}) - mB\hat\psi^{\dagger\mathsf T} = (i\gamma^\mu\partial_\mu - m)B\hat\psi^{\dagger\mathsf T} = 0$.
>
> **Step 2** (chiral basis). $(-i\gamma^2)^{-1} = -i\gamma^2$. For $\mu = 0, 1, 3$ ($\gamma^\mu$ real): $(-i\gamma^2)\gamma^\mu(-i\gamma^2) = -\gamma^2\gamma^\mu\gamma^2 = \gamma^\mu(\gamma^2)^2 = -\gamma^\mu$. For $\mu = 2$: $(-i\gamma^2)(-\gamma^2)(-i\gamma^2) = (\gamma^2)^3 = -\gamma^2$. So $B = -i\gamma^2$ works.
>
> **Step 3** (Dirac basis). $\gamma^i_D = \gamma^i$, and $\gamma^0_D = \mathrm{diag}(\mathbb 1, -\mathbb 1)$ is real and anticommutes with $\gamma^2$; Step 2 used only that, so again $B_D = -i\gamma^2$. (Also: the two bases are related by a real orthogonal $M$, and $B' = MB(M^{\ast})^{-1}$.)
>
> **Step 4** (Majorana basis). Each $\gamma^\mu_M$ is purely imaginary ($\sigma^2$ imaginary; $i\sigma^3$, $-i\sigma^1$ imaginary), so $(\gamma^\mu_M)^{\ast} = -\gamma^\mu_M$ and $B_M = \mathbb 1$ satisfies the condition: charge conjugation is plain $\hat\psi \to \hat\psi^{\dagger\mathsf T}$, and the Dirac equation is real. $B$ is unique up to a factor (a phase, for unitary $B$).
>
> *Checked against:* [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|Theorem §C9.6.2]] ("if and only if $\eta^s = \xi^{-s}$"), [[§C9.5 Charge Conjugation on Oscillators and Spinors#^thm-c9-5-2|Theorem §C9.5.2]], [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-2|§C9.7, Remark: Why charge conjugation is consistent]]; [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-3|Theorem §C9.6.3]], [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-4|Theorem §C9.6.4]], PS eqs. (3.145)–(3.146) (p. 70, read); [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-1|Theorem §C9.6.1]] (part 2), [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^def-cb-18-18|Def. §CB.18.18]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-18-19|Theorem §CB.18.19]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^ex-cb-18-22|Example §CB.18.22]] (the same three bases), [[§C9.5 Charge Conjugation on Oscillators and Spinors#^cau-c9-5-4|§C9.5, Caution: −iγ² is a statement about the chiral basis]]; all three $B$'s and a random unitary basis numerically.

^sol-wd-7

### W8. Charge conjugation on the bilinears

![[PHY 513 Worksheet — Discrete Symmetries#^wd-8]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-8-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-8-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-8-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-8-d]]

> [!success]- Solution
> **Answers.** (a) $\mathsf V^\mu \to -\mathsf V^\mu(x)$, $\mathsf A^\mu \to +\mathsf A^\mu(x)$. (b) $\mathsf T^{\mu\nu} \to -\mathsf T^{\mu\nu}(x)$; a product of $k$ $\gamma$'s goes to the reversed product times $(-1)^k$. (c) With commuting components every sign is reversed: $\mathsf S \to -\mathsf S$ and $\mathsf V^\mu \to +\mathsf V^\mu$; without normal ordering, $\hat\psi^\dagger\hat\psi \to -\hat\psi^\dagger\hat\psi + 4\delta^3(\mathbf 0)$. (d) As stated.
>
> **(a) Step 1** (insert both laws). In components $\hat{\bar\psi}\Gamma\hat\psi = \sum_{c,d}\hat{\bar\psi}_c\Gamma_{cd}\hat\psi_d$. By W7(b), $U\hat{\bar\psi}_cU^{-1} = -i\sum_a(\gamma^0\gamma^2)_{ca}\hat\psi_a$ and $U\hat\psi_dU^{-1} = -i\sum_b\hat{\bar\psi}_b(\gamma^0\gamma^2)_{bd}$. Inserting $U^{-1}U$ between the fields,
>
> $$
> U\hat{\bar\psi}\Gamma\hat\psi U^{-1} = (-i)^2\sum_{a,b}M_{ab}\,\hat\psi_a\hat{\bar\psi}_b, \qquad M = (\gamma^0\gamma^2)^{\mathsf T}\,\Gamma\,(\gamma^0\gamma^2)^{\mathsf T} .
> $$
>
> First sign: $(-i)^2 = -1$.
>
> **Step 2** (the fermion exchange). $U(\mathcal C)$ maps annihilators to annihilators and creators to creators, so it maps the normal-ordered bilinear to a normal-ordered product, inside which $\hat\psi_a\hat{\bar\psi}_b = -\hat{\bar\psi}_b\hat\psi_a$ with no c-number. Second sign: $-1$. Transposing the number matrix, $U\hat{\bar\psi}\Gamma\hat\psi U^{-1} = +\hat{\bar\psi}\,M^{\mathsf T}\hat\psi$ with $M^{\mathsf T} = \gamma^0\gamma^2\,\Gamma^{\mathsf T}\,\gamma^0\gamma^2$, at the same point.
>
> **Step 3** (vector). By W6(c), $\gamma^0\gamma^2(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = \gamma^0\gamma^2(-\gamma^0\gamma^2\gamma^\mu) = -\gamma^\mu$: $\mathsf V^\mu \to -\mathsf V^\mu(x)$, all four components (PS (3.149)).
>
> **Step 4** (axial vector). $(\gamma^\mu\gamma^5)^{\mathsf T} = (\gamma^5)^{\mathsf T}(\gamma^\mu)^{\mathsf T} = \gamma^5(\gamma^\mu)^{\mathsf T}$ ($\gamma^5$ diagonal), and $\gamma^5$ commutes with $\gamma^0\gamma^2$ (two anticommutations): $\gamma^0\gamma^2\gamma^5(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = \gamma^5(-\gamma^\mu) = \gamma^\mu\gamma^5$. So $\mathsf A^\mu \to +\mathsf A^\mu(x)$ (PS (3.150)): the extra $\gamma^5$, moved once past $\gamma^\mu$, supplies the second sign.
>
> **(b) Step 1** (a product). $(\gamma^{\mu_1}\cdots\gamma^{\mu_k})^{\mathsf T} = (\gamma^{\mu_k})^{\mathsf T}\cdots(\gamma^{\mu_1})^{\mathsf T}$. Insert $(\gamma^0\gamma^2)^2 = \mathbb 1$ between neighbours: $\gamma^0\gamma^2(\cdots)^{\mathsf T}\gamma^0\gamma^2 = \prod_{j = k}^{1}\bigl(\gamma^0\gamma^2(\gamma^{\mu_j})^{\mathsf T}\gamma^0\gamma^2\bigr) = (-\gamma^{\mu_k})\cdots(-\gamma^{\mu_1}) = (-1)^k\gamma^{\mu_k}\cdots\gamma^{\mu_1}$.
>
> **Step 2** (tensor). For $k = 2$: $\gamma^\mu\gamma^\nu \to \gamma^\nu\gamma^\mu$, so $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu] \to \frac i2[\gamma^\nu, \gamma^\mu] = -\sigma^{\mu\nu}$ ($i$ is a number, untouched by the linear $U$): $\mathsf T^{\mu\nu} \to -\mathsf T^{\mu\nu}(x)$.
>
> **Step 3** (consistency with the rest of the column). $k = 0$: $\mathsf S$ even. $i\gamma^5 = i\cdot i\gamma^0\gamma^1\gamma^2\gamma^3$ with $k = 4$: reversed order $\gamma^3\gamma^2\gamma^1\gamma^0 = \gamma^0\gamma^1\gamma^2\gamma^3$ (six exchanges), so $\mathsf P$ even. $\gamma^\mu\gamma^5$, $k = 5$: $-\gamma^5\gamma^\mu = +\gamma^\mu\gamma^5$, as in (a).
>
> **(c) Step 1** (commuting components). Without the exchange sign of Step 2 the result would be $-\hat{\bar\psi}M^{\mathsf T}\hat\psi$: $\mathsf S \to -\mathsf S$ and $\mathsf V^\mu \to +\mathsf V^\mu$. A classical commuting Dirac field would have a $C$-invariant current, i.e. $C$ would not reverse charge; the fermion sign is what makes particles and antiparticles carry opposite charge.
>
> **Step 2** (without normal ordering). Then $\hat\psi_a\hat\psi_b^\dagger = -\hat\psi_b^\dagger\hat\psi_a + \{\hat\psi_a, \hat\psi_b^\dagger\}$ at the same point. For $\mathsf V^0 = \hat\psi^\dagger\hat\psi$ the matrix is $B^\dagger B = \mathbb 1$ ($B = -i\gamma^2$ unitary): $U\hat\psi^\dagger\hat\psi U^{-1} = \sum_c\hat\psi_c\hat\psi_c^\dagger = -\hat\psi^\dagger\hat\psi + \sum_c\{\hat\psi_c, \hat\psi_c^\dagger\} = -\hat\psi^\dagger\hat\psi + 4\delta^3(\mathbf 0)$. The unordered density contains the vacuum charge density $2\delta^3(\mathbf 0)$ (the constant $2V\int\frac{d^3p}{(2\pi)^3}$ in $\hat Q$), which does not change sign; a charged vacuum would not be $C$ invariant. With normal ordering the constant is absent and $\mathsf V^0 \to -\mathsf V^0$ exactly (PS p. 71).
>
> **(d) ★** $\overline{\hat\psi_L}\gamma^\mu\hat\psi_L = \hat{\bar\psi}\gamma^\mu P_L\hat\psi = \frac12(\mathsf V^\mu - \mathsf A^\mu)$. By (a) it goes to $\frac12(-\mathsf V^\mu - \mathsf A^\mu) = -\hat{\bar\psi}\gamma^\mu P_R\hat\psi = -\overline{\hat\psi_R}\gamma^\mu\hat\psi_R$: $C$ alone, like $P$ alone, maps the left-handed current to a right-handed one; $CP$ maps it to a left-handed one (W5(c)).
>
> *Checked against:* (a) the user's Problem Set 7, Problem 2(b), as written: [[§C9.6 Charge Conjugation on the Field and Bilinears#^der-c9-6-9|Derivation §C9.6.9]]; [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-6|Theorem §C9.6.6]], [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-9|Theorem §C9.6.9]], [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-7|Theorem §C9.6.7]]; PS (3.149)–(3.150) and p. 71, row $C$; (b) [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-10|Theorem §C9.6.10]] and its derivation's closing bullet ($(-1)^k$ and the reversed order), [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-8|Theorem §C9.6.8]]; (c) [[§C9.6 Charge Conjugation on the Field and Bilinears#^der-c9-6-5|Derivation §C9.6.5]] (first bullet: with commuting fields $\mathsf S$ would flip), [[§C9.6 Charge Conjugation on the Field and Bilinears#^rem-c9-6-4|§C9.6, Remark: The number current flips]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]] (the unordered constant); the $4\delta^3(\mathbf 0)$ line derived here, consistent with that constant; (d) [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-12|★ Theorem §C9.6.12]]. All signs also at the operator level numerically.

^sol-wd-8

### W9. The physical spin of an antiparticle

![[PHY 513 Worksheet — Discrete Symmetries#^wd-9]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-9-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-9-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-9-c]]

> [!success]- Solution
> **Answers.** (a) $-\sum_{r,s}\hat b^{s\dagger}_{\mathbf p}\hat b^r_{\mathbf p}\,\eta^{r\dagger}\frac{\sigma^3}2\eta^s = \frac12\hat b^{1\dagger}\hat b^1 - \frac12\hat b^{2\dagger}\hat b^2$; the constant is $\propto\operatorname{tr}\sigma^3 = 0$. (b) $\hat J_z = \pm\frac12$ for $s = 1, 2$, as for particles; the wave-function sign and the reordering sign compensate. (c) $-\frac12$; the law $U(\mathcal C)\hat\psi U(\mathcal C)^{-1} = -i\gamma^2\hat\psi^{\dagger\mathsf T}$ would fail.
>
> **(a) Step 1** (reorder). $\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf p} = -\hat b^{s\dagger}_{\mathbf p}\hat b^r_{\mathbf p} + (2\pi)^3\delta^{rs}\delta^3(\mathbf 0)$.
>
> **Step 2** (the constant). It multiplies $\sum_r\eta^{r\dagger}\frac{\sigma^3}2\eta^r = \frac12\operatorname{tr}\bigl(\sigma^3\sum_r\eta^r\eta^{r\dagger}\bigr) = \frac12\operatorname{tr}\sigma^3 = 0$ (completeness of the orthonormal $\eta^r$): no ordering constant, the vacuum has no spin.
>
> **Step 3** (matrix elements). $\sigma^3\eta^1 = \sigma^3(0, 1)^{\mathsf T} = -\eta^1$ and $\sigma^3\eta^2 = \sigma^3(-1, 0)^{\mathsf T} = +\eta^2$, so $\eta^{r\dagger}\frac{\sigma^3}2\eta^s = \mp\frac12\delta^{rs}$ ($-$ for $r = 1$): the wave-function spins. The antiparticle term is $-\bigl(-\frac12\hat b^{1\dagger}\hat b^1 + \frac12\hat b^{2\dagger}\hat b^2\bigr) = +\frac12\hat b^{1\dagger}\hat b^1 - \frac12\hat b^{2\dagger}\hat b^2$.
>
> **(b) Step 1** (particles). The particle term of $\hat S^3$ at such momenta is $\sum_{r,s}\hat a^{r\dagger}\hat a^s\,\xi^{r\dagger}\frac{\sigma^3}2\xi^s = \frac12\hat a^{1\dagger}\hat a^1 - \frac12\hat a^{2\dagger}\hat a^2$.
>
> **Step 2** (states at rest). At $\mathbf p = \mathbf 0$ the orbital part gives nothing, $\hat J_z|0\rangle = 0$, and the pair terms vanish along $z$; so $\hat J_z\hat c^\dagger_{\mathbf 0}|0\rangle = [\hat J_z, \hat c^\dagger_{\mathbf 0}]|0\rangle$ with the number-operator form of (a): $[\hat b^{1\dagger}\hat b^1, \hat b^{1\dagger}_{\mathbf 0}] \propto \hat b^{1\dagger}_{\mathbf 0}$ with coefficient $+\frac12$. So $\hat J_z\hat b^{1\dagger}_{\mathbf 0}|0\rangle = +\frac12\hat b^{1\dagger}_{\mathbf 0}|0\rangle$, $\hat J_z\hat b^{2\dagger}_{\mathbf 0}|0\rangle = -\frac12\hat b^{2\dagger}_{\mathbf 0}|0\rangle$, the same as for $\hat a^{s\dagger}_{\mathbf 0}|0\rangle$.
>
> **Step 3** (two signs). One minus sign from the wave function ($\eta^1$ is spin down), one from fermion reordering ($\hat b\hat b^\dagger \to -\hat b^\dagger\hat b$). Physical spin is the eigenvalue of the operator, not what the mode function shows.
>
> **(c)** With $\eta^s = \xi^s$, $\eta^{r\dagger}\frac{\sigma^3}2\eta^s = \pm\frac12\delta^{rs}$ and the reordering sign alone would give $\hat J_z\hat b^{1\dagger}_{\mathbf 0}|0\rangle = -\frac12\hat b^{1\dagger}_{\mathbf 0}|0\rangle$; then $U(\mathcal C)$, mapping $\hat a^1 \to \hat b^1$, would flip the spin. That choice is exactly the one under which $U(\mathcal C)\hat\psi U(\mathcal C)^{-1} = -i\gamma^2\hat\psi^{\dagger\mathsf T}$ fails (W7(a), Step 3). The convention $\eta^s = \xi^{-s}$ makes the label $s$ mean physical spin for both species and makes the field law hold.
>
> *Checked against:* [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-1|Theorem §C9.7.1]], [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-2|Theorem §C9.7.2]] with [[§C9.7 Physical Spin versus Wave-Function Spin#^der-c9-7-2|Derivation §C9.7.2]], [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|Theorem §C9.7.3]] with [[§C9.7 Physical Spin versus Wave-Function Spin#^der-c9-7-3|Derivation §C9.7.3]], [[§C9.7 Physical Spin versus Wave-Function Spin#^pr-c9-7-4|Principle §C9.7.4]], [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-2|§C9.7, Remark: Why charge conjugation is consistent]]; the wave-function spins of $\eta^1$, $\eta^2$ numerically.

^sol-wd-9

## Time reversal

### W10. Why time reversal is antiunitary

![[PHY 513 Worksheet — Discrete Symmetries#^wd-10]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-10-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-10-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-10-c]]

> [!success]- Solution
> **Answers.** (a) A linear $U$ gives $M\hat\psi(t, \mathbf x)$, not $M\hat\psi(-t, \mathbf x)$; $U\hat HU^{-1} = -\hat H$ would make the spectrum unbounded below. (b) $Ue^{-i\hat Ht}U^{-1} = e^{i\hat Ht}$. (c) Part 1 conjugates the matrix entries; part 2 keeps the order of the fields.
>
> **(a) Step 1** (linear $U$). Insert $U^{-1}U$: $U\hat\psi(t, \mathbf x)U^{-1} = (Ue^{i\hat Ht}U^{-1})(U\hat\psi(0, \mathbf x)U^{-1})(Ue^{-i\hat Ht}U^{-1})$. A linear $U$ commuting with $\hat H$ commutes with every power series in $\hat H$, so $Ue^{\pm i\hat Ht}U^{-1} = e^{\pm i\hat Ht}$, and with the law at $t = 0$: $U\hat\psi(t, \mathbf x)U^{-1} = e^{i\hat Ht}M\hat\psi(0, \mathbf x)e^{-i\hat Ht} = M\hat\psi(t, \mathbf x)$. Equating with $M\hat\psi(-t, \mathbf x)$ would require $\hat\psi(t, \mathbf x) = \hat\psi(-t, \mathbf x)$, false: the coefficient of $\hat a^s_{\mathbf p}$ carries $e^{-iE_{\mathbf p}t}$ on one side and $e^{+iE_{\mathbf p}t}$ on the other, and no constant matrix changes a time dependence.
>
> **Step 2** ($U\hat HU^{-1} = -\hat H$). Then $Ue^{i\hat Ht}U^{-1} = e^{-i\hat Ht}$ and the time dependence would come out right, but an eigenstate $|E\rangle$ would go to $U|E\rangle$ with $\hat HU|E\rangle = -EU|E\rangle$: the spectrum of $\hat H$, $[0, \infty)$, would have to contain $(-\infty, 0]$. Excluded.
>
> **(b)** With $UcU^{-1} = c^{\ast}$ and $[U, \hat H] = 0$: $Ue^{-i\hat Ht}U^{-1} = \sum_n U\frac{(-it)^n}{n!}\hat H^nU^{-1} = \sum_n\frac{(it)^n}{n!}\hat H^n = e^{i\hat Ht}$. Then $U\hat\psi(t, \mathbf x)U^{-1} = e^{-i\hat Ht}\bigl(U\hat\psi(0, \mathbf x)U^{-1}\bigr)e^{i\hat Ht}$, the time dependence of $\hat\psi(-t, \mathbf x)$. Preserving transition probabilities then makes $U$ antiunitary, $\langle U\Psi_1, U\Psi_2\rangle = \langle\Psi_1, \Psi_2\rangle^{\ast}$.
>
> **(c) Step 1** (numbers). For any state $\Psi$: $U(cA)U^{-1}\Psi = U\bigl(cAU^{-1}\Psi\bigr) = c^{\ast}UAU^{-1}\Psi$ by antilinearity.
>
> **Step 2** (products). $U(AB)U^{-1} = UAU^{-1}UBU^{-1}$: inserting $U^{-1}U = \mathbb 1$ needs no linearity, so the order of operators is kept.
>
> **Step 3** (adjoints). For antiunitary $U$, $\langle U\Psi_1, UA^\dagger U^{-1}U\Psi_2\rangle = \langle\Psi_1, A^\dagger\Psi_2\rangle^{\ast} = \langle A\Psi_1, \Psi_2\rangle^{\ast} = \langle UA\Psi_1, U\Psi_2\rangle = \langle UAU^{-1}U\Psi_1, U\Psi_2\rangle$; as $U\Psi_{1,2}$ run over all states, $UA^\dagger U^{-1} = (UAU^{-1})^\dagger$.
>
> **Step 4** (in a bilinear). In $\sum_{a,b}\hat{\bar\psi}_a\Gamma_{ab}\hat\psi_b$ Step 1 turns $\Gamma_{ab}$ into $\Gamma^{\ast}_{ab}$ ("$U(\mathcal T)$ conjugates the Dirac matrices", Problem Set 6), while Step 2 keeps $\hat{\bar\psi}$ on the left: no fermion exchange, unlike $C$.
>
> *Checked against:* [[§C9.8 Time Reversal#^thm-c9-8-1|Theorem §C9.8.1]] with [[§C9.8 Time Reversal#^der-c9-8-1|Derivation §C9.8.1]] (and the vacuum route of [[§C9.8 Time Reversal#^der-c9-8-1b|Derivation §C9.8.1b]], PS p. 67), [[§C9.8 Time Reversal#^thm-c9-8-2|Theorem §C9.8.2]], [[§C9.8 Time Reversal#^thm-c9-8-3|Theorem §C9.8.3]], [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^def-cb-19-4|Def. §CB.19.4]], [[§CB.19 Projective Representations, Wigner's Theorem and Antiunitary Symmetries#^thm-cb-19-16|Theorem §CB.19.16]].

^sol-wd-10

### W11. Time reversal on oscillators, spinors and the Dirac field

![[PHY 513 Worksheet — Discrete Symmetries#^wd-11]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-11-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-11-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-11-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-11-d]]

> [!success]- Solution
> **Answers.** (a) As stated. (b) Both hold. (c) The law follows; with $\hat a^{-2} = +\hat a^1$ the $s = 2$ terms would return with a relative sign; PS's $-\gamma^1\gamma^3$ is an overall phase. (d) $U(\mathcal T)^2 = -1$ on states with an odd number of fermions; $U(\mathcal T)^2 = \mathbb 1$ for the scalar.
>
> **(a) Step 1** (the matrix). $\gamma^1\gamma^3 = \begin{pmatrix}0 & \sigma^1\\ -\sigma^1 & 0\end{pmatrix}\begin{pmatrix}0 & \sigma^3\\ -\sigma^3 & 0\end{pmatrix} = \begin{pmatrix}-\sigma^1\sigma^3 & 0\\ 0 & -\sigma^1\sigma^3\end{pmatrix}$, and $\sigma^1\sigma^3 = -i\sigma^2$, so the blocks are $i\sigma^2 = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$: real. $(i\sigma^2)^2 = -\mathbb 1$.
>
> **Step 2** ($(\gamma^\mu)^{\ast}\gamma^1\gamma^3$). $\gamma^0$ and $\gamma^2$ anticommute with both $\gamma^1$, $\gamma^3$, hence commute with $\gamma^1\gamma^3$; $\gamma^1$, $\gamma^3$ anticommute with it. $\mu = 0$: $\gamma^0\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma^0 = \gamma^1\gamma^3\gamma_0$. $\mu = 1, 3$ (real): $\gamma^i\gamma^1\gamma^3 = -\gamma^1\gamma^3\gamma^i = \gamma^1\gamma^3\gamma_i$. $\mu = 2$: $(\gamma^2)^{\ast}\gamma^1\gamma^3 = -\gamma^2\gamma^1\gamma^3 = -\gamma^1\gamma^3\gamma^2 = \gamma^1\gamma^3\gamma_2$. So $(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$.
>
> **(b)** For $\mathbf p = p\hat{\mathbf z}$: $p\cdot\sigma = \mathrm{diag}(E - p, E + p)$, $p\cdot\bar\sigma = \mathrm{diag}(E + p, E - p)$, and for $\tilde p$ the two are exchanged. $u^1(p) = (\sqrt{E - p}, 0, \sqrt{E + p}, 0)^{\mathsf T}$, real, so $u^1(p)^{\ast} = u^1(p)$. $u^{-1}(\tilde p) = u^2(\tilde p) = (0, \sqrt{E - p}, 0, \sqrt{E + p})^{\mathsf T}$, and $i\sigma^2(0, c)^{\mathsf T} = (c, 0)^{\mathsf T}$ in each block: $\gamma^1\gamma^3u^2(\tilde p) = u^1(p)^{\ast}$. For $s = 2$: $u^2(p)^{\ast} = (0, \sqrt{E + p}, 0, \sqrt{E - p})^{\mathsf T}$; $u^{-2}(\tilde p) = -u^1(\tilde p) = -(\sqrt{E + p}, 0, \sqrt{E - p}, 0)^{\mathsf T}$, and $i\sigma^2(-c, 0)^{\mathsf T} = (0, c)^{\mathsf T}$: $\gamma^1\gamma^3u^{-2}(\tilde p) = u^2(p)^{\ast}$.
>
> **(c) Step 1** (act antilinearly). $U(\mathcal T)$ conjugates the numbers ($u \to u^{\ast}$, $v \to v^{\ast}$, $e^{\mp ip\cdot x} \to e^{\pm ip\cdot x}$, same $t$, $\mathbf x$) and maps $\hat a^s_{\mathbf p} \to \hat a^{-s}_{-\mathbf p}$, $\hat b^{s\dagger}_{\mathbf p} \to \hat b^{-s\dagger}_{-\mathbf p}$ (adjoints preserved, W10(c)):
>
> $$
> U\hat\psi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^{-s}_{-\mathbf p}u^s(p)^{\ast}e^{ip\cdot x} + \hat b^{-s\dagger}_{-\mathbf p}v^s(p)^{\ast}e^{-ip\cdot x}\bigr) .
> $$
>
> **Step 2** (spinors). $u^s(p)^{\ast} = \gamma^1\gamma^3u^{-s}(\tilde p)$, $v^s(p)^{\ast} = \gamma^1\gamma^3v^{-s}(\tilde p)$; pull $\gamma^1\gamma^3$ out.
>
> **Step 3** (relabel $s \to -s$). $\sum_s\hat a^{-s}u^{-s} = \hat a^2u^2 + (-\hat a^1)(-u^1) = \sum_s\hat a^su^s$; the same for $\hat b^\dagger v$. Had the oscillator law been $\hat a^{-2} = +\hat a^1$, the $s = 2$ term would be $\hat a^1(-u^1)$ and the sum would not reassemble into a field: the sign is forced by the spinors.
>
> **Step 4** (relabel $\mathbf p \to -\mathbf p$). $\tilde p \to p$ in the spinors, $p \to \tilde p$ in the exponents, and $e^{i\tilde p\cdot x} = e^{-ip\cdot x_T}$ (W1(b)): the integral is $\hat\psi(x_T)$, so $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$.
>
> **Step 5** (PS). PS eq. (3.139) has $(-\gamma^1\gamma^3)$; their spinor relation $u^{-s}(\tilde p) = -\gamma^1\gamma^3[u^s(p)]^{\ast}$ (p. 68) is the one of (b) multiplied by $(\gamma^1\gamma^3)^{-1} = -\gamma^1\gamma^3$, and inserted into their own line it gives $+\gamma^1\gamma^3$. The overall sign is a phase of $U(\mathcal T)$ and cancels in every bilinear, where the matrix and its inverse appear together.
>
> **(d) Step 1** (twice on the oscillators). $\hat a^1_{\mathbf p} \to \hat a^2_{-\mathbf p} \to \hat a^{-2}_{\mathbf p} = -\hat a^1_{\mathbf p}$ and $\hat a^2_{\mathbf p} \to -\hat a^1_{-\mathbf p} \to -\hat a^2_{\mathbf p}$ (the real $-1$ is untouched by antilinearity): $U^2\hat a^s_{\mathbf p}U^{-2} = -\hat a^s_{\mathbf p}$, likewise for $\hat b$; $U^2$ is linear and unitary, so also $U^2\hat a^{s\dagger}U^{-2} = -\hat a^{s\dagger}$.
>
> **Step 2** (states). $U^2|0\rangle = |0\rangle$, and a state with $n$ creators gets $(-1)^n$: $U(\mathcal T)^2 = (-1)^{\hat N_a + \hat N_b}$, $-1$ on one fermion (the sign of a $2\pi$ rotation of spin $\frac12$; Kramers). For the scalar, $\hat a_{\mathbf p} \to \hat a_{-\mathbf p} \to \hat a_{\mathbf p}$: $U(\mathcal T)^2 = \mathbb 1$.
>
> *Checked against:* [[§C9.8 Time Reversal#^thm-c9-8-4|Theorem §C9.8.4]], [[§C9.8 Time Reversal#^thm-c9-8-5|Theorem §C9.8.5]], [[§C9.8 Time Reversal#^thm-c9-8-6|Theorem §C9.8.6]], [[§C9.8 Time Reversal#^thm-c9-8-7|Theorem §C9.8.7]] with [[§C9.8 Time Reversal#^der-c9-8-7|Derivation §C9.8.7]] (step 3's by-product), [[§C9.8 Time Reversal#^cau-c9-8-4|§C9.8, Caution: Signs and names in Peskin–Schroeder and Yu]] and PS pp. 68–69 (read), [[§C9.8 Time Reversal#^thm-c9-8-16|Theorem §C9.8.16]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^rem-c9-10-1|§C9.10, Remark: Time reversal twice is +1 on the scalar field]]; the spinor relations for random $\mathbf p$ and spin axes numerically.

^sol-wd-11

### W12. Time reversal on the bilinears

![[PHY 513 Worksheet — Discrete Symmetries#^wd-12]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-12-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-12-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-12-c]]

> [!success]- Solution
> **Answers.** (a) $\mathsf P \to -\mathsf P(x_T)$, $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(x_T)$. (b) As stated: $\mathsf A^0$ even, $\mathsf A^i$ odd. (c) $\mathsf T^{\mu\nu} \to -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$: $\mathsf T^{0i}$ even, $\mathsf T^{ij}$ odd, the opposite of parity; the extra sign is the conjugated $i$ in $\sigma^{\mu\nu}$.
>
> **(a) Step 1** (the conjugate field). $U\hat\psi^\dagger U^{-1} = (U\hat\psi U^{-1})^\dagger = \hat\psi^\dagger(x_T)(\gamma^1\gamma^3)^\dagger = \hat\psi^\dagger(x_T)\gamma^3\gamma^1$ ($(\gamma^i)^\dagger = -\gamma^i$). The $\gamma^0$ of $\hat{\bar\psi} = \hat\psi^\dagger\gamma^0$ is real, so antilinearity leaves it, and $\gamma^3\gamma^1$ commutes with $\gamma^0$: $U\hat{\bar\psi}(x)U^{-1} = \hat{\bar\psi}(x_T)\gamma^3\gamma^1$.
>
> **Step 2** (general bilinear). The numbers $\Gamma_{ab}$ are conjugated and the order of the fields kept (W10(c)): $U\hat{\bar\psi}\Gamma\hat\psi(x)U^{-1} = \hat{\bar\psi}(x_T)\,\gamma^3\gamma^1\Gamma^{\ast}\gamma^1\gamma^3\,\hat\psi(x_T)$. No exchange sign; normal ordering is preserved.
>
> **Step 3** (pseudoscalar). $\Gamma = i\gamma^5$: $\Gamma^{\ast} = -i\gamma^5$ ($\gamma^5$ real). $\gamma^5$ commutes with $\gamma^3\gamma^1$ (two anticommutations) and $\gamma^3\gamma^1\gamma^1\gamma^3 = \gamma^3(-\mathbb 1)\gamma^3 = \mathbb 1$: matrix $-i\gamma^5$, so $\mathsf P \to -\mathsf P(x_T)$; the whole sign is the conjugated $i$ (PS: "acquires an extra minus sign when $T$ goes through the $i$").
>
> **Step 4** (vector). By W11(a), $\gamma^3\gamma^1(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^3\gamma^1\gamma^1\gamma^3\gamma_\mu = \gamma_\mu$, whose components are $\mathcal P^\mu{}_\nu\gamma^\nu$ ($+\gamma^0$, $-\gamma^i$): $\mathsf V^\mu(x) \to \mathcal P^\mu{}_\nu\mathsf V^\nu(x_T)$, charge density even, current odd. Case by case: $\gamma^1\gamma^3$ flips $\gamma^1$, $\gamma^3$; complex conjugation flips $\gamma^2$.
>
> **(b)** $\Gamma = \gamma^\mu\gamma^5$, $\Gamma^{\ast} = (\gamma^\mu)^{\ast}\gamma^5$. Insert $\gamma^1\gamma^3\gamma^3\gamma^1 = \mathbb 1$ between the factors: $\gamma^3\gamma^1(\gamma^\mu)^{\ast}\gamma^5\gamma^1\gamma^3 = \bigl(\gamma^3\gamma^1(\gamma^\mu)^{\ast}\gamma^1\gamma^3\bigr)\bigl(\gamma^3\gamma^1\gamma^5\gamma^1\gamma^3\bigr) = \gamma_\mu\gamma^5$. So $\mathsf A^\mu(x) \to \mathcal P^\mu{}_\nu\mathsf A^\nu(x_T)$, exactly as $\mathsf V^\mu$: $\gamma^5$ is real and commutes with $\gamma^1\gamma^3$, so it adds nothing under $T$ (under $P$ it added a sign, under $C$ it removed one).
>
> **(c)** $(\sigma^{\mu\nu})^{\ast} = -\frac i2[(\gamma^\mu)^{\ast}, (\gamma^\nu)^{\ast}]$. Inserting $\gamma^1\gamma^3\gamma^3\gamma^1$ between the two $\gamma$'s, $\gamma^3\gamma^1(\gamma^\mu)^{\ast}(\gamma^\nu)^{\ast}\gamma^1\gamma^3 = \gamma_\mu\gamma_\nu$, so the matrix is $-\frac i2[\gamma_\mu, \gamma_\nu] = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\sigma^{\rho\sigma}$: $\mathsf T^{\mu\nu}(x) \to -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$. $\mathsf T^{0i}$: $-(+1)(-1) = +1$; $\mathsf T^{ij}$: $-(-1)(-1) = -1$. Parity gives $\mathsf T^{0i}$ odd, $\mathsf T^{ij}$ even: the opposite, the extra sign being the conjugated $i$, as for $\mathsf P$. (Like $\mathbf E \leftrightarrow \mathsf T^{0i}$ and $\mathbf B \leftrightarrow \mathsf T^{ij}$: W17.)
>
> *Checked against:* (a) the user's Problem Set 7, Problem 2(c), as written: [[§C9.8 Time Reversal#^thm-c9-8-12|Theorem §C9.8.12]] and [[§C9.8 Time Reversal#^der-c9-8-9b|Derivation §C9.8.9b]]; [[§C9.8 Time Reversal#^thm-c9-8-8|Theorem §C9.8.8]], [[§C9.8 Time Reversal#^thm-c9-8-10|Theorem §C9.8.10]], [[§C9.8 Time Reversal#^thm-c9-8-9|Theorem §C9.8.9]]; PS (3.140)–(3.142) (p. 69, read); (b) [[§C9.8 Time Reversal#^thm-c9-8-13|Theorem §C9.8.13]]; (c) [[§C9.8 Time Reversal#^thm-c9-8-14|Theorem §C9.8.14]]; PS p. 71, row $T$ ($(-1)^\mu$ for both vectors, $-(-1)^\mu(-1)^\nu$ for the tensor); all numerically, including at the operator level.

^sol-wd-12

## The complex scalar under C and T

### W13. C, P and T for the complex boson

![[PHY 513 Worksheet — Discrete Symmetries#^wd-13]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-13-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-13-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-13-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-13-d]]

> [!success]- Solution
> **Answers.** (a) $\mathcal P$: $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$, $\hat b_{\mathbf p} \to \hat b_{-\mathbf p}$ (unitary); $\mathcal C$: $\hat a_{\mathbf p} \leftrightarrow \hat b_{\mathbf p}$ (unitary); $\mathcal T$: $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$, $\hat b_{\mathbf p} \to \hat b_{-\mathbf p}$ (antiunitary); vacuum invariant. (b) $J^\mu \to \mathcal P^\mu{}_\nu J^\nu(\tilde x)$, $-J^\mu(x)$, $\mathcal P^\mu{}_\nu J^\nu(x_T)$. (c) $\hat Q$: $+$, $-$, $+$; $\hat{\mathbf P}$: $-$, $+$, $-$. (d) $\hat\phi(x_T)$; $\eta_C = \pm1$; a real field is its own antiparticle.
>
> **(a) Step 1** (the general step). For a linear $U$ the numbers pass: the coefficient of $e^{-ip\cdot x}$ in $U\hat\phi U^{-1}$ is $U\hat a_{\mathbf p}U^{-1}$, that of $e^{ip\cdot x}$ is $U\hat b^\dagger_{\mathbf p}U^{-1}$. For an antilinear $U$ the exponentials are conjugated, and the roles swap: $U\hat a_{\mathbf p}U^{-1}$ multiplies $e^{+ip\cdot x}$.
>
> **Step 2** (matching). $e^{\mp ip\cdot x}$ have opposite signs of frequency for every $\mathbf p$; the Klein–Gordon product extracts each coefficient, so two such expansions agree iff the coefficients agree separately. The images must obey the same algebra: a map $\hat a_{\mathbf p} \to \hat c^\dagger_{\mathbf k}$ (annihilator to creator) would give $[\hat c^\dagger_{\mathbf k}, \hat c_{\mathbf k'}] = -(2\pi)^3\delta^3(\mathbf k - \mathbf k')$, the wrong sign. So annihilators go to annihilators.
>
> **Step 3** (parity). $\hat\phi(\tilde x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{-\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{-\mathbf p}e^{ip\cdot x}\bigr)$ after $\mathbf p \to -\mathbf p$ and $p\cdot\tilde x = \tilde p\cdot x$: annihilators with $e^{-ip\cdot x}$, so $U$ is linear with $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$, $\hat b_{\mathbf p} \to \hat b_{-\mathbf p}$ (W3 with $\eta_a = \eta_b = 1$).
>
> **Step 4** (charge conjugation). $\hat\phi^\dagger(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$: the annihilator $\hat b_{\mathbf p}$ sits with $e^{-ip\cdot x}$, so $U$ is linear (the antilinear option would need $U\hat b^\dagger_{\mathbf p}U^{-1} = \hat b_{\mathbf p}$, excluded by Step 2), with $\hat a_{\mathbf p} \to \hat b_{\mathbf p}$ and $\hat b^\dagger_{\mathbf p} \to \hat a^\dagger_{\mathbf p}$, i.e. $\hat b_{\mathbf p} \to \hat a_{\mathbf p}$.
>
> **Step 5** (time reversal). With $p\cdot x_T = -\tilde p\cdot x$ and $\mathbf p \to -\mathbf p$: $\hat\phi(x_T) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{-\mathbf p}e^{ip\cdot x} + \hat b^\dagger_{-\mathbf p}e^{-ip\cdot x}\bigr)$: the annihilators multiply $e^{+ip\cdot x}$. A linear $U$ would need $U\hat a_{\mathbf p}U^{-1} = \hat b^\dagger_{-\mathbf p}$, excluded; the antilinear option gives $\hat a_{\mathbf p} \to \hat a_{-\mathbf p}$, $\hat b_{\mathbf p} \to \hat b_{-\mathbf p}$. These preserve the commutators (real, even $\delta$'s), so the operators are unitary, unitary and antiunitary.
>
> **(b) Step 1** (the adjoint field). $U\hat\phi^\dagger U^{-1} = (U\hat\phi U^{-1})^\dagger$ in all three cases: $\hat\phi^\dagger(\tilde x)$, $\hat\phi(x)$, $\hat\phi^\dagger(x_T)$.
>
> **Step 2** (derivatives). $U$ is $x$-independent, so $U\partial^\mu\hat\phi U^{-1} = \partial^\mu(U\hat\phi U^{-1})$, also for the antilinear $U$ (the derivative has real coefficients): $\mathcal P^\mu{}_\nu(\partial^\nu\hat\phi)(\tilde x)$, $\partial^\mu\hat\phi^\dagger(x)$, $-\mathcal P^\mu{}_\nu(\partial^\nu\hat\phi)(x_T)$ (W1(b)).
>
> **Step 3** ($\mathcal P$). Both terms of $J^\mu$ get $\mathcal P^\mu{}_\nu$: $J^\mu(x) \to \mathcal P^\mu{}_\nu J^\nu(\tilde x)$.
>
> **Step 4** ($\mathcal C$). $J^\mu \to i[\hat\phi(\partial^\mu\hat\phi^\dagger) - (\partial^\mu\hat\phi)\hat\phi^\dagger]$. The fields are bosonic and the current is normal-ordered (which $U(\mathcal C)$ preserves), so each product may be put back in order without sign or c-number: $= -i[\hat\phi^\dagger(\partial^\mu\hat\phi) - (\partial^\mu\hat\phi^\dagger)\hat\phi] = -J^\mu(x)$.
>
> **Step 5** ($\mathcal T$). The antilinear $U$ conjugates the explicit $i$ and keeps the order: $J^\mu \to -i[\hat\phi^\dagger(-\mathcal P^\mu{}_\nu\partial^\nu\hat\phi) - (-\mathcal P^\mu{}_\nu\partial^\nu\hat\phi^\dagger)\hat\phi](x_T) = \mathcal P^\mu{}_\nu J^\nu(x_T)$: the two signs ($i \to -i$, $\partial^0 \to -\partial^0$) cancel on $J^0$, and the spatial current flips.
>
> **(c) Step 1** ($\hat Q$). $\hat Q = \frac12\int d^3x\,J^0$ ($J^\mu = -\hat j^\mu$). Integrate the laws of (b) for $\mu = 0$ over space at fixed time: under $\mathcal P$, $\int d^3x\,J^0(t, -\mathbf x) = \int d^3x\,J^0(t, \mathbf x)$; under $\mathcal C$, $-$; under $\mathcal T$, $\int d^3x\,J^0(-t, \mathbf x)$, equal by charge conservation. In modes: $\mathcal C$ swaps $\hat a^\dagger\hat a \leftrightarrow \hat b^\dagger\hat b$, $\hat Q \to -\hat Q$; $\mathcal P$, $\mathcal T$ relabel $\mathbf p$ (real coefficients), $\hat Q \to \hat Q$.
>
> **Step 2** ($\hat{\mathbf P}$). $\mathcal C$: $\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}$ is symmetric under the swap: $\hat{\mathbf P}$. $\mathcal P$ and $\mathcal T$: $\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,(\hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p} + \hat b^\dagger_{-\mathbf p}\hat b_{-\mathbf p})$; the vector $\mathbf p$ is real, so antilinearity does not touch it; $\mathbf p \to -\mathbf p$ gives $-\hat{\mathbf P}$.
>
> **(d) Step 1** (time reversal of the real field). Step 5 of (a) with $\hat b = \hat a$: $U\hat\phi(x)U^{-1} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{-\mathbf p}e^{ip\cdot x} + \hat a^\dagger_{-\mathbf p}e^{-ip\cdot x}\bigr) = \hat\phi(x_T)$; and $U^2 = \mathbb 1$.
>
> **Step 2** (no exchange). There is one species: $\hat\phi^\dagger = \hat\phi$, so the scalar's $\mathcal C$ law $\hat\phi \to \hat\phi^\dagger$ is trivial. A unitary $U$ with $U\hat a_{\mathbf p}U^{-1} = \eta_C\hat a_{\mathbf p}$ gives $U\hat\phi U^{-1} = \int(\eta_C\hat a e^{-ip\cdot x} + \eta_C^{\ast}\hat a^\dagger e^{ip\cdot x})/\cdots$, proportional to $\hat\phi$ iff $\eta_C = \eta_C^{\ast}$; with $|\eta_C| = 1$, $\eta_C = \pm1$ (Hermiticity of $U\hat\phi U^{-1}$, as in W2(a)): a $C$-parity, not an exchange.
>
> *Checked against:* (a)–(b) the user's Problem Set 7, Problem 4(a)–(b), as written: [[§C9.10 C, T and CPT for the Complex Scalar Field#^der-c9-10-1|Derivation §C9.10.1]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^der-c9-10-2|Derivation §C9.10.2]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^der-c9-10-4|Derivation §C9.10.4]]; [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-1|Def. §C9.10.1]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^def-c9-10-2|Def. §C9.10.2]], [[§C9.2 Parity of the Scalar Field#^thm-c9-2-2|Theorem §C9.2.2]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-3|Theorem §C9.10.3]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|Theorem §C9.10.4]] (the same rules for $\hat j^\mu = -J^\mu$). *Derived here; check:* (c) has no single home: $\hat Q$ against the last bullet of Derivation §C9.10.4 and [[§C9.2 Parity of the Scalar Field#^thm-c9-2-12|Theorem §C9.2.12]]; $\hat{\mathbf P}$ under $\mathcal C$, $\mathcal P$ against the Practice Midterm's Problem 3(c) solution, under $\mathcal T$ by the same relabelling; (d) is Derivation §C9.10.2 with $\hat b = \hat a$, the Hermiticity step of [[§C9.2 Parity of the Scalar Field#^der-c9-2-10b|Derivation §C9.2.10b]], and [[§C9.10 C, T and CPT for the Complex Scalar Field#^rem-c9-10-1|§C9.10, Remark: Time reversal twice is +1 on the scalar field]].

^sol-wd-13

## CPT

### W14. CPT on the Dirac field

![[PHY 513 Worksheet — Discrete Symmetries#^wd-14]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-14-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-14-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-14-c]]

> [!success]- Solution
> **Answers.** (a) $\Theta\hat\psi(x)\Theta^\dagger = \gamma^5\hat\psi^{\dagger\mathsf T}(-x)$. (b) $\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$, $\eta_a$ not conjugated; $\Theta$ is antiunitary. (c) $\Theta'\hat\psi(x)\Theta'^{-1} = -\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$; the sign cancels in bilinears.
>
> **(a) Step 1** (inside out). $\Theta^\dagger = \mathcal T^\dagger\mathcal P^\dagger\mathcal C^\dagger$, so $\Theta\hat\psi\Theta^\dagger = \mathcal C\mathcal P(\mathcal T\hat\psi\mathcal T^\dagger)\mathcal P^\dagger\mathcal C^\dagger$: first $\mathcal T$, then $\mathcal P$, then $\mathcal C$. The matrices produced at each step are numbers; $\mathcal P$ and $\mathcal C$ are linear and pass them unchanged.
>
> **Step 2** ($\mathcal T$ and $\mathcal P$). $\mathcal T\hat\psi(t, \mathbf x)\mathcal T^\dagger = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$, then $\mathcal P(\cdot)\mathcal P^\dagger = \gamma^1\gamma^3\gamma^0\hat\psi(-t, -\mathbf x) = \gamma^1\gamma^3\gamma^0\hat\psi(-x)$ (the parity image of $x_T$ is $-x$; $\eta_a = 1$).
>
> **Step 3** ($\mathcal C$ at $-x$). $\mathcal C\hat\psi(-x)\mathcal C^\dagger = -i(\hat{\bar\psi}(-x)\gamma^0\gamma^2)^{\mathsf T} = -i\gamma^2\hat\psi^{\dagger\mathsf T}(-x)$ (W7(b)). So $\Theta\hat\psi(x)\Theta^\dagger = -i\,\gamma^1\gamma^3\gamma^0\gamma^2\,\hat\psi^{\dagger\mathsf T}(-x)$.
>
> **Step 4** (the matrix). $\gamma^1\gamma^3$ commutes with $\gamma^0$ and $\gamma^2$: $\gamma^1\gamma^3\gamma^0\gamma^2 = \gamma^0\gamma^2\gamma^1\gamma^3 = -\gamma^0\gamma^1\gamma^2\gamma^3 = -(-i\gamma^5) = i\gamma^5$, with $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$ from $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ (the course's sign; $\varepsilon^{0123} = +1$). Hence $\Theta\hat\psi(x)\Theta^\dagger = -i(i\gamma^5)\hat\psi^{\dagger\mathsf T}(-x) = \gamma^5\hat\psi^{\dagger\mathsf T}(-x)$: a $\gamma^5$, the transposed adjoint, and the whole four-vector reversed.
>
> **(b) Step 1** (the phase). Repeat with $\eta_a$: after Step 2 the field is $\eta_a\gamma^1\gamma^3\gamma^0\hat\psi(-x)$. The antilinear $\mathcal T$ has already acted when $\eta_a$ appears, and $\mathcal C$ is linear, so $\eta_a$ is not conjugated: $\Theta\hat\psi(x)\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$.
>
> **Step 2** (antiunitary). A product of two unitary operators and one antiunitary one is antilinear and maps inner products to their conjugates: $\Theta$ is antiunitary, $\Theta c\Theta^{-1} = c^{\ast}$, $\Theta^{-1} = U(\mathcal T)^{-1}U(\mathcal P)^{-1}U(\mathcal C)^{-1}$.
>
> **(c) Step 1** ($\mathcal C$ first). $-i\sum_b(\gamma^2)_{ab}\hat\psi_b^\dagger(x)$.
>
> **Step 2** (then $\mathcal P$, on the adjoint). $U(\mathcal P)\hat\psi_b^\dagger U(\mathcal P)^{-1} = \bigl(\eta_a\sum_c\gamma^0_{bc}\hat\psi_c(\tilde x)\bigr)^\dagger = \eta_a^{\ast}\sum_c\gamma^0_{bc}\hat\psi_c^\dagger(\tilde x)$: the column $-i\eta_a^{\ast}\gamma^2\gamma^0\hat\psi^{\dagger\mathsf T}(\tilde x)$.
>
> **Step 3** (then $\mathcal T$, conjugating the numbers). $(-i)^{\ast} = i$, $(\eta_a^{\ast})^{\ast} = \eta_a$, $(\gamma^2)^{\ast} = -\gamma^2$, $\gamma^0$ real; $U(\mathcal T)\hat\psi_c^\dagger(y)U(\mathcal T)^{-1} = \sum_d(\gamma^1\gamma^3)_{cd}\hat\psi_d^\dagger(y_T)$ ($\gamma^1\gamma^3$ real), and $y = \tilde x$ has $y_T = -x$. Altogether $\Theta'\hat\psi\Theta'^{-1} = -i\eta_a\,\gamma^2\gamma^0\gamma^1\gamma^3\,\hat\psi^{\dagger\mathsf T}(-x)$.
>
> **Step 4** (the matrix). $\gamma^2\gamma^0\gamma^1\gamma^3 = -\gamma^0\gamma^2\gamma^1\gamma^3 = +\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$, so $\Theta'\hat\psi(x)\Theta'^{-1} = (-i)(-i)\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x) = -\eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$.
>
> **Step 5** (bilinears). $\Theta'\hat\psi_c\Theta'^{-1} = -\Theta\hat\psi_c\Theta^{-1}$ for every component, hence (adjoints) also for $\hat\psi_c^\dagger$, and $\hat{\bar\psi}_b = \sum_c\hat\psi_c^\dagger\gamma^0_{cb}$ with real $\gamma^0$. A bilinear contains one of each, so the two signs give $(-1)^2 = 1$: "any order will do".
>
> *Checked against:* (a) the user's Problem Set 7, Problem 3, as written: [[§C9.9 CPT and the CPT Theorem#^der-c9-9-3b|Derivation §C9.9.3b]]; (b) [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-3|Theorem §C9.9.3]] with [[§C9.9 CPT and the CPT Theorem#^der-c9-9-3|Derivation §C9.9.3]], [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-1|Theorem §C9.9.1]], [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|Theorem §C9.9.2]], [[§C9.9 CPT and the CPT Theorem#^cau-c9-9-1|§C9.9, Caution: The transposed adjoint in CPT]]; (c) [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-4|Theorem §C9.9.4]] with [[§C9.9 CPT and the CPT Theorem#^der-c9-9-4|Derivation §C9.9.4]] (its last bullet for Step 5); the three matrix products numerically ($\gamma^1\gamma^3\gamma^0(-i\gamma^2) = \gamma^5$, $i(-\gamma^2)\gamma^0\gamma^1\gamma^3 = -\gamma^5$).

^sol-wd-14

### W15. CPT on bilinears and on the scalar; the (−1)^n rule

![[PHY 513 Worksheet — Discrete Symmetries#^wd-15]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-15-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-15-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-15-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-15-d]]

> [!success]- Solution
> **Answers.** (a) $\Theta\mathsf A^\mu(x)\Theta^{-1} = -\mathsf A^\mu(-x)$, $\Theta\mathsf T^{\mu\nu}(x)\Theta^{-1} = +\mathsf T^{\mu\nu}(-x)$, $\partial_\mu \to -\partial_\mu$: a bilinear with $n$ Lorentz indices gets $(-1)^n$ and moves to $-x$. (b) $\hat\phi^\dagger(-x)$, $-(\partial^\mu\hat\phi^\dagger)(-x)$, $-\hat j^\mu(-x)$. (c) See below. (d) $\mathsf V_\mu\mathsf A^\mu$: $C$ odd, $P$ odd, $T$ even, $CPT$ even; $\partial_\mu\mathsf A^\mu$: $C$ even, $P$ odd, $T$ odd, $CPT$ even; $i\mathsf S$: $C$, $P$ even, $T$ odd, $CPT$ odd, because it is not Hermitian.
>
> **(a) Step 1** (the composition). $\Theta X\Theta^{-1} = U(\mathcal C)U(\mathcal P)\bigl(U(\mathcal T)XU(\mathcal T)^{-1}\bigr)U(\mathcal P)^{-1}U(\mathcal C)^{-1}$. Write the laws as $X \to t_X\mathcal P^{(n)}X(x_T)$, $p_X\mathcal P^{(n)}X(\tilde x)$, $c_XX(x)$, with real signs and one factor $\mathcal P$ per index. The real numbers pass the linear $U(\mathcal P)$, which acts at $x_T$ and sends it to $-x$; $\mathcal P^{(n)}\mathcal P^{(n)} = \mathbb 1$; then $U(\mathcal C)$. Result: $c_Xp_Xt_X\,X(-x)$.
>
> **Step 2** (axial vector, the slides' example). $\mathsf A^\mu \xrightarrow{T} \mathcal P^\mu{}_\nu\mathsf A^\nu(x_T) \xrightarrow{P} -\mathsf A^\mu(-x) \xrightarrow{C} -\mathsf A^\mu(-x)$: signs $(+)(-)(+)$.
>
> **Step 3** (tensor). $\mathsf T^{\mu\nu} \xrightarrow{T} -\mathcal P\mathcal P\mathsf T(x_T) \xrightarrow{P} -\mathsf T^{\mu\nu}(-x) \xrightarrow{C} +\mathsf T^{\mu\nu}(-x)$: $(-)(+)(-)$.
>
> **Step 4** (derivative). $\partial_\mu \to -\mathcal P^\nu{}_\mu\partial_\nu$ under $T$, $\mathcal P^\nu{}_\mu\partial_\nu$ under $P$, unchanged under $C$: $-\partial_\mu$, the chain rule for $x \to -x$. With $\mathsf S$, $\mathsf P$ ($(+)(+)(+)$, $(+)(-)(-)$) and $\mathsf V^\mu$ ($(-)(+)(+)$) the column is $+, +, -, -, +, -$ for $n = 0, 0, 1, 1, 2, 1$: the factor is $(-1)^n$. The separate signs vary from row to row; their product does not.
>
> **(b)** With all phases $1$: $\hat\phi(x) \xrightarrow{T} \hat\phi(x_T) \xrightarrow{P} \hat\phi(-x) \xrightarrow{C} \hat\phi^\dagger(-x)$; $\Theta\hat\phi^\dagger\Theta^{-1} = \hat\phi(-x)$ by the adjoint. $\Theta$ is $x$-independent, so $\Theta\partial^\mu\hat\phi(x)\Theta^{-1} = \partial^\mu[\hat\phi^\dagger(-x)] = -(\partial^\mu\hat\phi^\dagger)(-x)$. The current: $\Theta$ conjugates the $i$ and keeps the order, $\hat j^\mu \to -i\bigl(\hat\phi^\dagger(-\partial^\mu\hat\phi) - \hat\phi(-\partial^\mu\hat\phi^\dagger)\bigr)(-x) = i(\hat\phi^\dagger\partial^\mu\hat\phi - \hat\phi\,\partial^\mu\hat\phi^\dagger)(-x) = -\hat j^\mu(-x)$ (normal ordering lets the bosonic factors be reordered freely): one index, $(-1)^1$, as for $\mathsf V^\mu$.
>
> **(c) Step 1** (building blocks). $\Theta\hat\phi(x)\Theta^{-1} = \hat\phi^\dagger(-x)$ and $\Theta\hat\psi(x)\Theta^{-1} = \gamma^5\hat\psi^{\dagger\mathsf T}(-x)$. $\Theta$ does three things to a term $c\,\hat X_1\cdots\hat X_k(x)$, each $\hat X_j$ being $\hat\phi$, $\hat\phi^\dagger$, a bilinear $\hat{\bar\psi}\Gamma\hat\psi$ or a derivative of these.
>
> **Step 2** ($PT$: $x \to -x$). The operator is local, so all its factors sit at $x$, and all move to the common point $-x$.
>
> **Step 3** (indices). $\mathcal P\mathcal T = -\mathbb 1$ on four-vectors, so every Lorentz index gives $-1$: derivatives by the chain rule, bilinears by (a) (the $\gamma^5$ of the field law and the fermion reordering together produce $(-1)^n$), the scalar current by (b).
>
> **Step 4** ($C$ with the antilinear $T$: Hermitian conjugation). $\Theta\hat X_j\Theta^{-1} = (-1)^{n_j}\hat X_j^\dagger(-x)$ and $\Theta c\Theta^{-1} = c^{\ast}$, so $\Theta\,c\hat X_1\cdots\hat X_k\,\Theta^{-1} = (-1)^nc^{\ast}\hat X_1^\dagger\cdots\hat X_k^\dagger(-x)$. Hermitian conjugation would reverse the order, but the blocks are bosonic (a bilinear holds two fermion fields) and normal-ordered, so the order is immaterial: $\Theta\hat O(x)\Theta^{-1} = (-1)^n\hat O^\dagger(-x)$.
>
> **Step 5** (the hypotheses). In a Lorentz scalar every index is contracted with $g_{\mu\nu}$ or $\varepsilon_{\mu\nu\rho\sigma}$, so $n$ is even; $\hat O^\dagger = \hat O$ by Hermiticity. Hence $\Theta\hat O(x)\Theta^{-1} = \hat O(-x)$, and for a Lagrangian density the action is invariant ($y = -x$, Jacobian $1$). Each hypothesis removes one obstruction: locality gives the common point, Lorentz invariance makes the signs cancel, Hermiticity undoes the conjugation; nothing about the particular interaction enters. That is why the conclusion is hard to avoid.
>
> **(d) Step 1** ($\mathsf V_\mu\mathsf A^\mu$). $C$: $(-1)(+1) = -1$. $P$: $\mathsf V \to \mathcal P\mathsf V$, $\mathsf A \to -\mathcal P\mathsf A$, and $\mathcal P^{\mathsf T}g\mathcal P = g$: $-1$. $T$: both get $+\mathcal P$: $+1$. $CPT$: $(-1)^2 = +1$. (The $V - A$ structure of the weak interaction violates $C$ and $P$.)
>
> **Step 2** ($\partial_\mu\mathsf A^\mu$). $C$: $+1$. $P$: $\partial_\mu[-\mathcal P^\mu{}_\nu\mathsf A^\nu(\tilde x)] = -\mathcal P^\mu{}_\nu\mathcal P^\rho{}_\mu(\partial_\rho\mathsf A^\nu)(\tilde x) = -(\partial\cdot\mathsf A)(\tilde x)$. $T$: $\partial_\mu[\mathcal P^\mu{}_\nu\mathsf A^\nu(x_T)] = -(\partial\cdot\mathsf A)(x_T)$. $CPT$: $+1$. The pattern of $\mathsf P$, as it must be: on solutions $\partial_\mu\mathsf A^\mu = 2m\mathsf P$.
>
> **Step 3** ($i\mathsf S$). $C$, $P$: the number $i$ passes, $+1$. $T$: $i \to -i$, $-1$. $CPT$: $\Theta(i\mathsf S)(x)\Theta^{-1} = -i\mathsf S(-x)$: odd, although $n = 0$. $i\mathsf S$ is anti-Hermitian: the rule $\Theta\hat O\Theta^{-1} = (-1)^n\hat O^\dagger(-x)$ of (c) gives $(i\mathsf S)^\dagger = -i\mathsf S$, and the Hermiticity hypothesis is the one that fails.
>
> *Checked against:* (a) [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]] with [[§C9.9 CPT and the CPT Theorem#^der-c9-9-5|Derivation §C9.9.5]], [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|Example §C9.9.1]], PS p. 71 row $CPT$ (read: $+1, +1, -1, -1, +1, -1$); (b) [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-6|Theorem §C9.10.6]]; (c) the user's Problem Set 7, Problem 4(c), as written: [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-2|Example §C9.9.2]], with [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-6|Theorem §C9.9.6]]. *Derived here; check:* (d) from the table of Theorem §C9.9.5; the $CPT$ entries agree with the $(-1)^n$ rule and with the $\Theta\hat O\Theta^{-1} = (-1)^n\hat O^\dagger(-x)$ of (c); $\partial_\mu\mathsf A^\mu = 2m\mathsf P$ is [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|Theorem §C5a.8.4]], whose $\mathsf P$ row agrees.

^sol-wd-15

## Invariance of the free Lagrangians

### W16. The free Lagrangians under C, P and T

![[PHY 513 Worksheet — Discrete Symmetries#^wd-16]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-16-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-16-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-16-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-16-d]]

> [!success]- Solution
> **Answers.** (a) $\hat{\mathcal L} \to \hat{\mathcal L}(\tilde x)$, $\hat{\mathcal L}(x)$, $\hat{\mathcal L}(x_T)$. (b) The extra term is a total derivative; the action is invariant. (c) The conjugated $i$, the lower index of $\gamma_\mu$, and $\partial_0 \to -\partial_0$. (d) $m'\mathsf P$ violates $P$, $T$ and $CP$; it respects $C$ and $CPT$.
>
> **(a)** By W13(b) Step 2: $\mathcal P$: $\partial_\mu\hat\phi^\dagger\partial^\mu\hat\phi \to \mathcal P^\nu{}_\mu\mathcal P^\mu{}_\rho(\partial_\nu\hat\phi^\dagger\partial^\rho\hat\phi)(\tilde x) = (\partial_\mu\hat\phi^\dagger\partial^\mu\hat\phi)(\tilde x)$ and $\hat\phi^\dagger\hat\phi \to \hat\phi^\dagger\hat\phi(\tilde x)$. $\mathcal C$: $\partial_\mu\hat\phi\,\partial^\mu\hat\phi^\dagger - m^2\hat\phi\hat\phi^\dagger$, the same normal-ordered operator (bosons). $\mathcal T$: the two derivatives give $(-\mathcal P)(-\mathcal P) = \mathcal P\mathcal P$, contracted to $+1$, and $m^2$ is real: $\hat{\mathcal L}(x_T)$. The actions are invariant ($d^4x$ unchanged under $x \to \tilde x$, $x_T$).
>
> **(b) Step 1** (mass term). $\mathsf S \to \mathsf S$ (W8(b), $k = 0$).
>
> **Step 2** (kinetic term). As in W8(a), with the derivative on the second field: $U\hat{\bar\psi}\gamma^\mu\partial_\mu\hat\psi U^{-1} = -\sum_{a,b}M_{ab}\hat\psi_a\partial_\mu\hat{\bar\psi}_b$, $M = (\gamma^0\gamma^2)^{\mathsf T}\gamma^\mu(\gamma^0\gamma^2)^{\mathsf T}$; the exchange inside the normal-ordered product gives $+(\partial_\mu\hat{\bar\psi})\gamma^0\gamma^2(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2\hat\psi = -(\partial_\mu\hat{\bar\psi})\gamma^\mu\hat\psi$.
>
> **Step 3** (product rule). $-(\partial_\mu\hat{\bar\psi})\gamma^\mu\hat\psi = \hat{\bar\psi}\gamma^\mu\partial_\mu\hat\psi - \partial_\mu\mathsf V^\mu$; times $i$: $\hat{\mathcal L}_D \to \hat{\mathcal L}_D - i\partial_\mu\mathsf V^\mu$. The total derivative integrates to a surface term that vanishes for fields falling off at infinity, so the action, and with it the field equations, are $C$ invariant.
>
> **(c) Step 1** (mass term). $\mathsf S(x) \to \mathsf S(x_T)$, $m$ real.
>
> **Step 2** (kinetic term). $U\partial_\mu\hat\psi(x)U^{-1} = \partial_\mu[\gamma^1\gamma^3\hat\psi(x_T)] = \epsilon_\mu\gamma^1\gamma^3(\partial_\mu\hat\psi)(x_T)$ with $\epsilon_0 = -1$, $\epsilon_i = +1$ (no sum). With W12(a) Step 2 and $i \to -i$: $i\hat{\bar\psi}\gamma^\mu\partial_\mu\hat\psi \to -i\sum_\mu\hat{\bar\psi}(x_T)\gamma_\mu\,\epsilon_\mu(\partial_\mu\hat\psi)(x_T)$. $\gamma_\mu\epsilon_\mu = -\gamma^\mu$ for every $\mu$ ($(+\gamma^0)(-1)$ and $(-\gamma^i)(+1)$), so the term is $-i\cdot(-1)\hat{\bar\psi}\gamma^\mu\partial_\mu\hat\psi(x_T)$: invariant. Three signs: the conjugated $i$, the lowered index from $\gamma^1\gamma^3$ and complex conjugation, and the reversed time derivative.
>
> **(d)** From the table: $\mathsf P$ is $C$ even, $P$ odd, $T$ odd. So $m'\mathsf P$ violates $P$ and $T$, and $CP$ ($(+)(-) = -1$); it respects $C$ and $CPT$ ($n = 0$, Hermitian). (In the free theory a chiral rotation $\hat\psi \to e^{i\alpha\gamma^5}\hat\psi$, under which $\mathsf S \to \cos2\alpha\,\mathsf S + \sin2\alpha\,\mathsf P$ and the kinetic term is invariant, rotates the $\mathsf P$ mass into an $\mathsf S$ mass; the violation becomes observable only together with other couplings.)
>
> *Checked against:* (a) [[§C9.2 Parity of the Scalar Field#^thm-c9-2-7|Theorem §C9.2.7]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-5|Theorem §C9.10.5]]; (b) [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-11|Theorem §C9.6.11]] with [[§C9.6 Charge Conjugation on the Field and Bilinears#^der-c9-6-11|Derivation §C9.6.11]]; (c) [[§C9.8 Time Reversal#^thm-c9-8-15|Theorem §C9.8.15]] with [[§C9.8 Time Reversal#^der-c9-8-15|Derivation §C9.8.15]]; PS p. 71 ("invariant under $C$, $P$, and $T$ separately"). *Derived here; check:* (d) from the $\mathsf P$ row of [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]]; the chiral rotation of $\mathsf S$ from $\hat{\bar\psi} \to \hat{\bar\psi}e^{i\alpha\gamma^5}$ (Problem Set 6, Problem 5(a); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field|§C5a.8]]): $\hat{\bar\psi}e^{2i\alpha\gamma^5}\hat\psi = \cos2\alpha\,\mathsf S + \sin2\alpha\,\mathsf P$.

^sol-wd-16

## The vector field

### W17★. The field tensor under C, P and T

![[PHY 513 Worksheet — Discrete Symmetries#^wd-17]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-17-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-17-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-17-c]]

> [!success]- Solution
> **Answers.** (a) $C$: $A'^\mu(x) = -A^\mu(x)$; $P$: $A'^\mu(x) = \mathcal P^\mu{}_\nu A^\nu(\tilde x)$; $T$: $A'^\mu(x) = \mathcal P^\mu{}_\nu A^\nu(x_T)$. (b) $F \to -F$ ($\mathbf E, \mathbf B \to -\mathbf E, -\mathbf B$); $F^{\mu\nu} \to \mathcal P\mathcal PF(\tilde x)$ ($\mathbf E \to -\mathbf E$, $\mathbf B \to \mathbf B$); $F^{\mu\nu} \to -\mathcal P\mathcal PF(x_T)$ ($\mathbf E \to \mathbf E$, $\mathbf B \to -\mathbf B$): the signs of $\mathsf T^{\mu\nu}$; $\mathsf T^{\mu\nu}F_{\mu\nu}$ is invariant. (c) $F_{\mu\nu}F^{\mu\nu}$ is invariant under all; $\mathbf E\cdot\mathbf B$ is $P$ odd, $T$ odd, $C$ even, $CPT$ even.
>
> **(a) Step 1** ($C$). $A^\mu$ is a c-number and passes the linear $U(\mathcal C)$; $\mathsf V^\mu \to -\mathsf V^\mu$ (W8(a)): $-eA_\mu\mathsf V^\mu \to -e(-A_\mu)\mathsf V^\mu$, so $A' = -A$.
>
> **Step 2** ($P$). $U\int d^4x\,(-eA_\mu\mathsf V^\mu)U^{-1} = -e\int d^4x\,A_\mu(x)\mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x) = -e\int d^4y\,A_\mu(\tilde y)\mathcal P^\mu{}_\nu\mathsf V^\nu(y)$ (substitute $x = \tilde y$, Jacobian $1$). So $A'_\nu(y) = \mathcal P^\mu{}_\nu A_\mu(\tilde y)$, and raising the index ($\mathcal P$ and $g$ are diagonal) $A'^\nu(y) = \mathcal P^\nu{}_\mu A^\mu(\tilde y)$: the scalar potential even, $\mathbf A$ odd.
>
> **Step 3** ($T$). $U(\mathcal T)$ conjugates numbers: $e$ and the real function $A_\mu(x)$ are unchanged. With $\mathsf V^\mu \to \mathcal P^\mu{}_\nu\mathsf V^\nu(x_T)$ (W12(a)) the same substitution gives $A'^\nu(y) = \mathcal P^\nu{}_\mu A^\mu(y_T)$: $A^0$ even, $\mathbf A$ odd, as for the current that produces it.
>
> **(b) Step 1** (the tensor). By W1(b) with the index raised, $\partial^\mu[f(\tilde x)] = \mathcal P^\mu{}_\rho(\partial^\rho f)(\tilde x)$ and $\partial^\mu[f(x_T)] = -\mathcal P^\mu{}_\rho(\partial^\rho f)(x_T)$. So under $P$, $F'^{\mu\nu}(x) = \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma F^{\rho\sigma}(\tilde x)$, and under $T$, $F'^{\mu\nu}(x) = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma F^{\rho\sigma}(x_T)$; under $C$, $F' = -F$.
>
> **Step 2** ($\mathbf E$, $\mathbf B$). $E^i = F^{i0}$ has one spatial index, $B^i = -\frac12\varepsilon_{ijk}F^{jk}$ two. $P$: $\mathbf E \to -\mathbf E(\tilde x)$, $\mathbf B \to +\mathbf B(\tilde x)$ (a polar and an axial vector). $T$: $\mathbf E \to +\mathbf E(x_T)$, $\mathbf B \to -\mathbf B(x_T)$ (charges stay, currents reverse). $C$: both flip.
>
> **Step 3** (comparison). $\mathsf T^{\mu\nu}$: $C$ $-1$, $P$ $+\mathcal P\mathcal P$, $T$ $-\mathcal P\mathcal P$ (W8(b), W5(a), W12(c)): the same as $F^{\mu\nu}$. In $\mathsf T^{\mu\nu}F_{\mu\nu}$ the signs square: $C$ $(-1)^2$; $P$ and $T$ $(\pm1)^2$ times $\mathcal P\mathcal P$ contracted with $\mathcal P\mathcal P$, which is $+1$. The Pauli term is $C$, $P$, $T$ invariant.
>
> **(c)** $F_{\mu\nu}F^{\mu\nu} = 2(\mathbf B^2 - \mathbf E^2)$: every sign squares, invariant. $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$: under $P$, $(-\mathbf E)\cdot\mathbf B$, odd; under $T$, $\mathbf E\cdot(-\mathbf B)$, odd; under $C$, $(-\mathbf E)\cdot(-\mathbf B)$, even; under $CPT$, even, as $(-1)^4$ for four contracted indices requires. (A $\theta\,\mathbf E\cdot\mathbf B$ term violates $P$ and $T$ but not $CPT$.)
>
> *Derived here; check:* no vault box transforms $A^\mu$ or $F^{\mu\nu}$ under $C$, $P$, $T$. The $P$ law agrees with [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-3|Theorem §C1a.7.3]] (part 2: parity sends $\mathbf E + i\mathbf B \to -(\mathbf E - i\mathbf B)$, i.e. $\mathbf E \to -\mathbf E$, $\mathbf B \to \mathbf B$); $E^i = F^{i0}$, $B^i = -\frac12\varepsilon_{ijk}F^{jk}$ from [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]]; the invariants from [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]]; the current laws from [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]], whose $\mathsf T^{\mu\nu}$ row has the same signs as $F^{\mu\nu}$ here; the vector coupling as the parity-conserving one: [[§C9.4 Fermion Bilinears under Parity#^rem-c9-4-4|§C9.4, Remark: Discrete symmetries in nature]]. The $\mathbf E$, $\mathbf B$ maps checked numerically for a random $F$.

^sol-wd-17

## All fields

### W18. Short response

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-a]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-b]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-c]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-d]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-e]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-f]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-g]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-h]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-i]]

![[PHY 513 Worksheet — Discrete Symmetries#^wd-18-j]]

> [!success]- Answers
> 1. (a) $\mathcal P$: $(-1, +)$; $\mathcal T$: $(-1, -)$; $\mathcal P\mathcal T$: $(+1, -)$. [[§C9.1 Discrete Lorentz Transformations#^cau-c9-1-2|§C9.1, Caution: Slide 7's determinants]].
> 2. (b) $+1$ (scalar), $-1$ (Dirac); positronium at $L = 0$: $-1$. [[§C9.2 Parity of the Scalar Field#^thm-c9-2-3|Theorem §C9.2.3]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-6|Theorem §C9.3.6]], [[§C9.3 Parity on States, Spinors and the Dirac Field#^thm-c9-3-8|Theorem §C9.3.8]].
> 3. (c) $U(\mathcal T)$ and $\Theta$. [[§C9.8 Time Reversal#^thm-c9-8-2|Theorem §C9.8.2]], [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-2|Theorem §C9.9.2]].
> 4. (d) $-i\gamma^2$; $\mathbb 1$ (up to a phase). [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-2|Theorem §C9.6.2]], [[§CB.18 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^ex-cb-18-22|Example §CB.18.22]].
> 5. (e) $\gamma^1\gamma^3$; $-\gamma^1\gamma^3$; no (an overall phase, cancelled by $\gamma^3\gamma^1$ on $\hat{\bar\psi}$). [[§C9.8 Time Reversal#^cau-c9-8-4|§C9.8, Caution: Signs and names in Peskin–Schroeder and Yu]].
> 6. (f) $P$: $\mathsf T^{0i}$ $-$, $\mathsf T^{ij}$ $+$; $T$: $\mathsf T^{0i}$ $+$, $\mathsf T^{ij}$ $-$; $C$: both $-$. [[§C9.4 Fermion Bilinears under Parity#^thm-c9-4-4|Theorem §C9.4.4]], [[§C9.8 Time Reversal#^thm-c9-8-14|Theorem §C9.8.14]], [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-10|Theorem §C9.6.10]].
> 7. (g) $-\mathsf A^\mu(-x)$; $+(\partial_\mu\mathsf A^\mu)(-x)$. [[§C9.9 CPT and the CPT Theorem#^ex-c9-9-1|Example §C9.9.1]], [[§C9.9 CPT and the CPT Theorem#^thm-c9-9-5|Theorem §C9.9.5]].
> 8. (h) $-1$; $+1$. [[§C9.8 Time Reversal#^thm-c9-8-16|Theorem §C9.8.16]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^rem-c9-10-1|§C9.10, Remark: Time reversal twice is +1 on the scalar field]].
> 9. (i) $+\frac12$; its wave-function spin is $-\frac12$ ($\eta^1 = (0, 1)^{\mathsf T}$). [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|Theorem §C9.7.3]], [[§C9.7 Physical Spin versus Wave-Function Spin#^rem-c9-7-1|§C9.7, Remark: The puzzle]].
> 10. (j) $C$: both flip; $T$: both unchanged (moved to $x_T$). [[§C9.6 Charge Conjugation on the Field and Bilinears#^thm-c9-6-6|Theorem §C9.6.6]], [[§C9.8 Time Reversal#^thm-c9-8-9|Theorem §C9.8.9]], [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|Theorem §C9.10.4]].
>
> *Checked against:* the boxes named in each line, and PS p. 71 for (f), (g).

^sol-wd-18
