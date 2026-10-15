---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Relativity|Worksheet]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Worksheet — Relativity: Solutions

Solutions to [[PHY 513 Worksheet — Relativity]], folded so that you can try first; each question is embedded above its solution. Every solution is worked step by step in the course's conventions ([[Larsen PHY 513]]: $g = \operatorname{diag}(+1, -1, -1, -1)$, $\varepsilon^{0123} = +1$, active $\Lambda$, $K_i = \mathcal J^{0i}$) and ends with the line that says how it was checked: *Checked against* names the home box in these notes (or the user's submitted solution, "as written"); *Derived here; check* marks a result with no home box, derived from boxes that exist, with the special case it was checked against. All matrices, commutators and numbers below were also checked numerically (numpy/sympy, script `qft-C/review/worksheets/relativity/check*.py`). REL boxes are in [[Relativity]] level B, which keeps $c$, writes the metric $\eta_{\mu\nu}$ and reads $\Lambda$ passively ([[§C1a.4 The Lorentz Group#^cau-c1a-4-2|§C1a.4, Caution: Notation against Relativity level B]]).

---

# Lecture 1. The Lorentz group, tensors and electrodynamics

## Problem 1. The defining condition and the four components

![[PHY 513 Worksheet — Relativity#^wr-1]]

### (a) Index form, the time component and the determinant

![[PHY 513 Worksheet — Relativity#^wr-1-a]]

> [!success]- Solution
> **Answer.** $g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta}$; $(\Lambda^0{}_0)^2 - \sum_i(\Lambda^i{}_0)^2 = 1$; $\det\Lambda = \pm1$.
>
> **Step 1** (index form). $(\Lambda^{\mathsf T})_\alpha{}^\mu = \Lambda^\mu{}_\alpha$, so $(\Lambda^{\mathsf T}g\Lambda)_{\alpha\beta} = \Lambda^\mu{}_\alpha\,g_{\mu\nu}\,\Lambda^\nu{}_\beta$, and the condition is $g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta = g_{\alpha\beta}$.
>
> **Step 2** (the $00$ component). Put $\alpha = \beta = 0$; $g$ is diagonal, so only $\mu = \nu$ survives: $g_{00}(\Lambda^0{}_0)^2 + \sum_i g_{ii}(\Lambda^i{}_0)^2 = (\Lambda^0{}_0)^2 - \sum_i(\Lambda^i{}_0)^2 = g_{00} = 1$. The first column of $\Lambda$ is a unit timelike vector, and $(\Lambda^0{}_0)^2 \ge 1$: either $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$.
>
> **Step 3** (determinant). $\det(\Lambda^{\mathsf T}g\Lambda) = \det\Lambda^{\mathsf T}\det g\det\Lambda = (\det\Lambda)^2\det g$ must equal $\det g = -1 \ne 0$, so $(\det\Lambda)^2 = 1$.
>
> *Checked against:* [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]], 1–2 (with $\eta_{\mu\nu} \to g_{\mu\nu}$); the determinant step is step 2 of the derivation of [[§C1a.4 The Lorentz Group#^thm-c1a-4-1|Theorem §C1a.4.1]].

^sol-wr-1-a

### (b) The inverse without inverting

![[PHY 513 Worksheet — Relativity#^wr-1-b]]

> [!success]- Solution
> **Answer.** $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$, i.e. $(\Lambda^{-1})^\mu{}_\nu = \Lambda_\nu{}^\mu$; for $B_z(\eta)$, $\Lambda_\nu{}^\mu$ is the matrix of $B_z(-\eta)$.
>
> **Step 1.** Multiply $\Lambda^{\mathsf T}g\Lambda = g$ from the left by $g^{-1}$: $(g^{-1}\Lambda^{\mathsf T}g)\Lambda = \mathbb 1$, so $\Lambda^{-1} = g^{-1}\Lambda^{\mathsf T}g$.
>
> **Step 2** (entries). $(\Lambda^{-1})^\mu{}_\nu = g^{\mu\sigma}(\Lambda^{\mathsf T})_\sigma{}^\rho g_{\rho\nu} = g^{\mu\sigma}\Lambda^\rho{}_\sigma g_{\rho\nu} = g_{\nu\rho}\Lambda^\rho{}_\sigma g^{\sigma\mu} \equiv \Lambda_\nu{}^\mu$: the first index lowered and the second raised with the metric. The horizontal order matters: $\Lambda_\nu{}^\mu$ is the transpose with both indices moved, not $\Lambda^\mu{}_\nu$ again.
>
> **Step 3** ($B_z(\eta)$). Its nonzero off-identity entries are $\Lambda^0{}_0 = \Lambda^3{}_3 = \cosh\eta$, $\Lambda^0{}_3 = \Lambda^3{}_0 = \sinh\eta$. Then $\Lambda_0{}^0 = g_{00}\Lambda^0{}_0g^{00} = \cosh\eta$, $\Lambda_3{}^3 = g_{33}\Lambda^3{}_3g^{33} = \cosh\eta$, $\Lambda_3{}^0 = g_{33}\Lambda^3{}_0g^{00} = -\sinh\eta$, $\Lambda_0{}^3 = g_{00}\Lambda^0{}_3g^{33} = -\sinh\eta$. So $(\Lambda^{-1})^0{}_3 = (\Lambda^{-1})^3{}_0 = -\sinh\eta$: $B_z(\eta)^{-1} = B_z(-\eta)$, the boost back, as it must be.
>
> *Checked against:* [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 2; the entries $\Lambda_0{}^0 = \gamma$, $\Lambda_0{}^3 = -\gamma v$ are those used in [[§C1a.7 Relativistic Electrodynamics in Index Form#^ex-c1a-7-1|Example §C1a.7.1]].

^sol-wr-1-b

### (c) The four components

![[PHY 513 Worksheet — Relativity#^wr-1-c]]

> [!success]- Solution
> **Answer.** $\mathcal P$: $(-1, +)$, improper orthochronous. $\mathcal T$: $(-1, -)$, improper non-orthochronous. $\mathcal P\mathcal T = -\mathbb 1$: $(+1, -)$, proper non-orthochronous. $B_z(\eta)R_z(\theta)$: $(+1, +)$, $SO^+(1,3)$. Only $B_z(\eta)R_z(\theta)$ is an exponential. $SO(1,3)$ contains $-\mathbb 1$, which reverses time.
>
> **Step 1** (discrete ones). $\det\mathcal P = 1\cdot(-1)^3 = -1$, $\mathcal P^0{}_0 = 1$; $\det\mathcal T = -1$, $\mathcal T^0{}_0 = -1$; $\mathcal P\mathcal T = \operatorname{diag}(-1, -1, -1, -1) = -\mathbb 1$, $\det = (-1)^4 = +1$, $(-\mathbb 1)^0{}_0 = -1$.
>
> **Step 2** ($B_z(\eta)R_z(\theta)$). Both factors have determinant $1$ ($\cosh^2\eta - \sinh^2\eta = 1$, $\cos^2\theta + \sin^2\theta = 1$). $R_z(\theta)$ does not touch $e_0$, so $(B_zR_z)^0{}_0 = \cosh\eta \ge 1$.
>
> **Step 3** (exponentials). For real antisymmetric $\omega$, $s \mapsto \exp(-\frac{is}2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ is a continuous path from $\mathbb 1$; along it $\det$ (values $\pm1$) and $\Lambda^0{}_0$ (values in $\lvert\Lambda^0{}_0\rvert \ge 1$) cannot jump, so every exponential is in $SO^+(1,3)$. $\mathcal P$, $\mathcal T$, $-\mathbb 1$ are not, so they are not exponentials. $B_z(\eta)R_z(\theta) = e^{-i\eta K_3}e^{-i\theta J_3} = e^{-i\theta J_3 - i\eta K_3}$, one exponential, because $[J_3, K_3] = i\varepsilon_{33k}K_k = 0$.
>
> **Step 4** ($SO(1,3)$). $SO(1,3) = SO^+(1,3)\cup\mathcal P\mathcal T\cdot SO^+(1,3)$ contains $\mathcal P\mathcal T = -\mathbb 1$, which sends every future-pointing vector to a past-pointing one. "Lorentz invariant" means invariant under the identity component $SO^+(1,3)$; $\mathcal P$ and $\mathcal T$ are separate questions for the Lagrangian.
>
> *Checked against:* [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|Theorem §CB.3.12]] (the four cosets), [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-4|REL Theorem §B1.2.4]], 4 (the table), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]] (every exponential is proper orthochronous), [[§C1a.4 The Lorentz Group#^rem-c1a-4-1|§C1a.4, Remark: What "Lorentz invariant" means in field theory]], [[§B1.2 Lorentz Transformations and the Lorentz Group#^cau-b1-2-2|REL §B1.2, Caution: Names of the group]] ($SO(1,3)$ contains $PT$).

^sol-wr-1-c

## Problem 2. Rapidity

![[PHY 513 Worksheet — Relativity#^wr-2]]

### (a) Rapidities add along one axis

![[PHY 513 Worksheet — Relativity#^wr-2-a]]

> [!success]- Solution
> **Answer.** $B_z(\eta_1)B_z(\eta_2) = B_z(\eta_1 + \eta_2)$; $v = \dfrac{v_1 + v_2}{1 + v_1v_2}$; final velocity $\dfrac{1.4}{1.48} = \dfrac{35}{37} \approx 0.946$.
>
> **Step 1** (multiply the $(t, z)$ blocks). With $c_i = \cosh\eta_i$, $s_i = \sinh\eta_i$: $\begin{pmatrix}c_1 & s_1\\ s_1 & c_1\end{pmatrix}\begin{pmatrix}c_2 & s_2\\ s_2 & c_2\end{pmatrix} = \begin{pmatrix}c_1c_2 + s_1s_2 & c_1s_2 + s_1c_2\\ s_1c_2 + c_1s_2 & s_1s_2 + c_1c_2\end{pmatrix} = \begin{pmatrix}\cosh(\eta_1 + \eta_2) & \sinh(\eta_1 + \eta_2)\\ \sinh(\eta_1 + \eta_2) & \cosh(\eta_1 + \eta_2)\end{pmatrix}$ by the addition theorems; the $(x, y)$ block is $\mathbb 1\cdot\mathbb 1$.
>
> **Step 2** (velocities). A particle at rest, boosted by $\eta_1$, moves with $v_1 = \tanh\eta_1$; boosting it again by $\eta_2$ gives $B_z(\eta_2)B_z(\eta_1)(m, \mathbf 0) = B_z(\eta_1 + \eta_2)(m, \mathbf 0)$, velocity $\tanh(\eta_1 + \eta_2) = \dfrac{\tanh\eta_1 + \tanh\eta_2}{1 + \tanh\eta_1\tanh\eta_2}$.
>
> **Step 3** (numbers). $(0.6 + 0.8)/(1 + 0.48) = 35/37 = 0.9459$; equivalently $\operatorname{artanh}0.6 + \operatorname{artanh}0.8 = 0.6931 + 1.0986 = 1.7918$ and $\tanh1.7918 = 0.9459$. Additivity holds only for a common axis (Problem 16).
>
> *Checked against:* the paragraph after [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]] ("rapidities along one axis add"), [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-7|REL Theorem §B1.2.7]], 3–4; [[§B1.2 Lorentz Transformations and the Lorentz Group#^cau-b1-2-3|REL §B1.2, Caution: Rapidities add only along one axis]].

^sol-wr-2-a

### (b) Light-cone coordinates

![[PHY 513 Worksheet — Relativity#^wr-2-b]]

> [!success]- Solution
> **Answer.** $x'^\pm = e^{\pm\eta}x^\pm$; eigenvectors $e_0 + e_3$ (eigenvalue $e^{\eta}$) and $e_0 - e_3$ (eigenvalue $e^{-\eta}$), real, positive and reciprocal; $t^2 - z^2 = x^+x^-$ is multiplied by $e^{\eta}e^{-\eta} = 1$.
>
> **Step 1.** $t' = \cosh\eta\,t + \sinh\eta\,z$, $z' = \sinh\eta\,t + \cosh\eta\,z$. Adding, $t' + z' = (\cosh\eta + \sinh\eta)(t + z) = e^{\eta}(t + z)$; subtracting, $t' - z' = (\cosh\eta - \sinh\eta)(t - z) = e^{-\eta}(t - z)$.
>
> **Step 2** (eigenvectors). The vector with $x^- = 0$, i.e. $t = z$, is $e_0 + e_3$ (a light ray along $+z$), stretched by $e^{\eta}$; the one with $x^+ = 0$ is $e_0 - e_3$, shrunk by $e^{-\eta}$. Generator check: $K_3(e_0 \pm e_3) = \pm i(e_0 \pm e_3)$, so $e^{-i\eta K_3}$ multiplies them by $e^{-i\eta(\pm i)} = e^{\pm\eta}$.
>
> **Step 3.** $t^2 - z^2 = (t + z)(t - z) = x^+x^-$, and the two factors scale inversely. A boost is a squeeze along the light rays; it maps each light ray along $\pm z$ to itself.
>
> *Checked against:* [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-7|REL Theorem §B1.2.7]], 2 (passive, $u' = e^{\varphi}u$ for $u = ct - x$; the active $\eta$ is $-\varphi$); [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] (eigenvectors of $K_3$).

^sol-wr-2-b

### (c) The rapidity of a particle

![[PHY 513 Worksheet — Relativity#^wr-2-c]]

> [!success]- Solution
> **Answer.** $\tanh y = p_z/E$; $y \mapsto y + \eta$ under $B_z(\eta)$, $p_x$, $p_y$ fixed; $y_1 - y_2$ invariant; $y = \frac12\ln9 = \ln3 \approx 1.099$.
>
> **Step 1.** With $e^{2y} = (E + p_z)/(E - p_z)$: $\tanh y = \dfrac{e^{2y} - 1}{e^{2y} + 1} = \dfrac{(E + p_z) - (E - p_z)}{(E + p_z) + (E - p_z)} = \dfrac{p_z}{E}$.
>
> **Step 2.** $E \pm p_z$ are the light-cone components $p^\pm$ of $p$, so by (b) $p'^\pm = e^{\pm\eta}p^\pm$, and $\dfrac{E' + p'_z}{E' - p'_z} = e^{2\eta}\dfrac{E + p_z}{E - p_z}$, i.e. $y' = y + \eta$. $B_z$ acts as the identity on $(x, y)$, so $p_x$, $p_y$ are unchanged.
>
> **Step 3.** Every rapidity shifts by the same $\eta$, so $y_1 - y_2$ is invariant under boosts along $z$.
>
> **Step 4** (number). $y = \frac12\ln\frac{5 + 4}{5 - 4} = \frac12\ln9 = \ln3 = 1.0986$ (the particle has $m = \sqrt{25 - 16} = 3$, velocity $4/5 = \tanh(\ln3)$).
>
> *Derived here; check:* for $p_x = p_y = 0$, $p = B_z(\eta)(m, \mathbf 0) = (m\cosh\eta, 0, 0, m\sinh\eta)$ gives $e^{2y} = e^{2\eta}$, $y = \eta$: the particle's rapidity is the rapidity of [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]] of the boost that produced it from rest, and Step 2 is then the additivity of (a).

^sol-wr-2-c

## Problem 3. Index placement and covariance

![[PHY 513 Worksheet — Relativity#^wr-3]]

![[PHY 513 Worksheet — Relativity#^wr-3-a]]

![[PHY 513 Worksheet — Relativity#^wr-3-b]]

![[PHY 513 Worksheet — Relativity#^wr-3-c]]

![[PHY 513 Worksheet — Relativity#^wr-3-d]]

![[PHY 513 Worksheet — Relativity#^wr-3-e]]

![[PHY 513 Worksheet — Relativity#^wr-3-f]]

![[PHY 513 Worksheet — Relativity#^wr-3-g]]

> [!success]- Solution
> **The rules.** In a term an index appears at most twice; twice means once up and once down (summed); once means free, and both sides of an equation carry the same free indices at the same heights.
>
> 1. (a) **Illegal**: $\nu$ is up on the left, down on the right. Repair: $\partial_\mu F^{\mu\nu} = J^\nu$ (equivalently $\partial^\mu F_{\mu\nu} = J_\nu$), a vector equation.
> 2. (b) **Legal.** $\mu$, $\alpha$, $\beta$ are contracted (each once up, once down); $\gamma$ and $\nu$ are free, both up: a $(2,0)$ tensor $X^{\gamma\nu}$. It contains one $\varepsilon$, so it is a **pseudotensor**: under $\Lambda$ it picks up an extra $\det\Lambda$, a sign under $\mathcal P$ and $\mathcal T$.
> 3. (c) **Illegal**: $\mu$ up on the left, down on the right. Repair: $T^{\mu\nu}{}_\nu = S^\mu$; the left side is a vector (a contraction of the second and third slots).
> 4. (d) **Legal**: $\mu$ is contracted (up in $\Lambda^\mu{}_\nu$, down in $\Lambda_\mu{}^\rho$); $\nu$ (down) and $\rho$ (up) are free on both sides. **True**: $\Lambda_\mu{}^\rho = (\Lambda^{-1})^\rho{}_\mu$ (Problem 1(b)), so the left side is $(\Lambda^{-1})^\rho{}_\mu\Lambda^\mu{}_\nu = (\Lambda^{-1}\Lambda)^\rho{}_\nu = \delta^\rho{}_\nu$.
> 5. (e) **Illegal**: $\mu$ appears twice, both down. In components $\sum_\mu\partial_\mu\phi\,\partial_\mu\phi = (\partial_t\phi)^2 + (\nabla\phi)^2$, which is not invariant. Repair: $\partial_\mu\phi\,\partial^\mu\phi = (\partial_t\phi)^2 - (\nabla\phi)^2$, a scalar.
> 6. (f) $\nu$, $\rho$, $\sigma$ are contracted, $\mu$ (up) and $\lambda$ (up) are free: $B^{\mu\lambda} = A^\mu{}_\nu\,g^{\nu\rho}\,C_{\rho\sigma}\,D^{\sigma\lambda}$. Each contraction joins the second index of one factor to the first of the next, so it is the matrix product $B = A\,g^{-1}C\,D$ (numerically $g^{-1} = g$).
> 7. (g) Each free index carries one factor $\Lambda$ (up) or $\Lambda^{-1}$ (down), and each contracted pair carries $\Lambda^{-1}\Lambda = \mathbb 1$ (as in (d)). If both sides have the same free indices at the same heights, both transform with the same product of $\Lambda$'s: $L' = (\Lambda\cdots)L$, $R' = (\Lambda\cdots)R$, so $L = R$ in one frame implies $L' = R'$ in every frame.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-2|§C1a.5, Caution: Index bookkeeping: legal, illegal, and matrix products]] (the rules and the matrix-product reading), [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]] ((e)), [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 2 and 4 ((d), (g)), [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 1 (the factor $\det\Lambda$ of an $\varepsilon$, (b)); [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]] ((a)).

^sol-wr-3

## Problem 4. Symmetric meets antisymmetric

![[PHY 513 Worksheet — Relativity#^wr-4]]

### (a) The contraction vanishes

![[PHY 513 Worksheet — Relativity#^wr-4-a]]

> [!success]- Solution
> **Answer.** $S^{\mu\nu}A_{\mu\nu} = 0$.
>
> **Step 1.** Rename the dummies $\mu \leftrightarrow \nu$: $X \equiv S^{\mu\nu}A_{\mu\nu} = S^{\nu\mu}A_{\nu\mu}$.
>
> **Step 2.** Use the symmetries: $S^{\nu\mu} = S^{\mu\nu}$, $A_{\nu\mu} = -A_{\mu\nu}$, so $X = -S^{\mu\nu}A_{\mu\nu} = -X$, hence $X = 0$.
>
> *Checked against:* [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-5|REL Theorem §B2.2.5]] (cited for exactly this in [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]]).

^sol-wr-4-a

### (b) Maxwell's equations force current conservation

![[PHY 513 Worksheet — Relativity#^wr-4-b]]

> [!success]- Solution
> **Answer.** $\partial_\nu J^\nu = \partial_\nu\partial_\mu F^{\mu\nu} = 0$.
>
> **Step 1.** Apply $\partial_\nu$ to $\partial_\mu F^{\mu\nu} = J^\nu$: $\partial_\nu J^\nu = \partial_\nu\partial_\mu F^{\mu\nu}$.
>
> **Step 2.** For smooth $F$, $\partial_\nu\partial_\mu = \partial_\mu\partial_\nu$ is symmetric in $\mu\nu$ and $F^{\mu\nu}$ is antisymmetric: by (a) the double contraction vanishes. So a current that is not conserved cannot be a source of Maxwell's equations.
>
> *Checked against:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]] ("consistency of the first requires $\partial_\nu J^\nu = 0$"), [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-7|§C1a.5, Caution: The Hessian is not the wave operator]].

^sol-wr-4-b

### (c) The dual and the Bianchi identity

![[PHY 513 Worksheet — Relativity#^wr-4-c]]

> [!success]- Solution
> **Answer.** $\tilde F^{\mu\nu} = \varepsilon^{\mu\nu\rho\sigma}\partial_\rho A_\sigma$ and $\partial_\mu\tilde F^{\mu\nu} = \varepsilon^{\mu\nu\rho\sigma}\partial_\mu\partial_\rho A_\sigma = 0$.
>
> **Step 1.** $\tilde F^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}\partial_\rho A_\sigma - \frac12\varepsilon^{\mu\nu\rho\sigma}\partial_\sigma A_\rho$. In the second term rename $\rho \leftrightarrow \sigma$: $-\frac12\varepsilon^{\mu\nu\sigma\rho}\partial_\rho A_\sigma = +\frac12\varepsilon^{\mu\nu\rho\sigma}\partial_\rho A_\sigma$. The two halves add: $\tilde F^{\mu\nu} = \varepsilon^{\mu\nu\rho\sigma}\partial_\rho A_\sigma$.
>
> **Step 2.** $\partial_\mu\tilde F^{\mu\nu} = \varepsilon^{\mu\nu\rho\sigma}\partial_\mu\partial_\rho A_\sigma$: for fixed $\nu$, $\sigma$, the factor $\partial_\mu\partial_\rho A_\sigma$ is symmetric in $\mu\rho$ and $\varepsilon^{\mu\nu\rho\sigma}$ antisymmetric, so by (a) it vanishes. The homogeneous Maxwell equations are identities once $F$ comes from a potential.
>
> *Checked against:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]] ("the second holds identically when $F$ comes from a potential").

^sol-wr-4-c

### (d) Only the antisymmetric part couples to F

![[PHY 513 Worksheet — Relativity#^wr-4-d]]

> [!success]- Solution
> **Answer.** $T^{\mu\nu}F_{\mu\nu} = T^{[\mu\nu]}F_{\mu\nu}$; $F^\mu{}_\mu = 0$; $F^{\mu\nu}F_{\nu\mu} = -F^{\mu\nu}F_{\mu\nu}$.
>
> **Step 1.** $T^{\mu\nu} = T^{(\mu\nu)} + T^{[\mu\nu]}$ with $T^{(\mu\nu)} = \frac12(T^{\mu\nu} + T^{\nu\mu})$ symmetric; by (a) $T^{(\mu\nu)}F_{\mu\nu} = 0$.
>
> **Step 2.** $F^\mu{}_\mu = g_{\mu\nu}F^{\mu\nu}$: $g$ symmetric, $F$ antisymmetric, so $0$ by (a).
>
> **Step 3.** $F_{\nu\mu} = -F_{\mu\nu}$ gives $F^{\mu\nu}F_{\nu\mu} = -F^{\mu\nu}F_{\mu\nu}$.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]] (the decomposition into symmetric traceless, antisymmetric and trace parts), and (a).

^sol-wr-4-d

## Problem 5. The Levi-Civita symbol

![[PHY 513 Worksheet — Relativity#^wr-5]]

### (a) Values

![[PHY 513 Worksheet — Relativity#^wr-5-a]]

> [!success]- Solution
> **Answer.** $\varepsilon^{3012} = -1$, $\varepsilon^{3210} = +1$, $\varepsilon^{0213} = -1$, $\varepsilon_{0123} = -1$, $\varepsilon_{1032} = -1$. All five flip in Peskin–Schroeder's convention ($+1$, $-1$, $+1$, $+1$, $+1$).
>
> **Step 1** (count inversions). $(3012)$: the pairs $(3,0)$, $(3,1)$, $(3,2)$ are out of order, three inversions, odd: $-1$. $(3210)$: all $\binom42 = 6$ pairs inverted, even: $+1$. $(0213)$: one inversion $(2,1)$: $-1$.
>
> **Step 2** (lower indices). Lowering all four indices of a nonzero component multiplies it by $g_{00}g_{11}g_{22}g_{33} = -1$: $\varepsilon_{0123} = -\varepsilon^{0123} = -1$; $\varepsilon^{1032}$ has two inversions, $(1,0)$ and $(3,2)$, so $+1$, and $\varepsilon_{1032} = -1$.
>
> **Step 3** (Peskin–Schroeder). Their $\varepsilon^{0123} = -1$ is the negative of the course's symbol, so every component flips.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]] ("lowering all four indices always costs $\det g = -1$"; one $\varepsilon$ flips between the conventions), [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]] (the course's $\varepsilon^{1230} = -1$ by three transpositions); numerical check of all five.

^sol-wr-5-a

### (b) Two contractions

![[PHY 513 Worksheet — Relativity#^wr-5-b]]

> [!success]- Solution
> **Answer.** $-24$ and $-6\,\delta^\delta{}_\sigma$.
>
> **Step 1** (full contraction). Only the $4! = 24$ permutations of $(0123)$ contribute. For each, $\varepsilon_{\mu\nu\rho\sigma} = -\varepsilon^{\mu\nu\rho\sigma}$ (Step 2 of (a)) and $(\varepsilon^{\mu\nu\rho\sigma})^2 = 1$, so each term is $-1$: total $-24$.
>
> **Step 2** (three contracted). $X_\sigma{}^\delta = \varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\delta}$. A term is nonzero only if $\{\mu, \nu, \rho, \sigma\}$ and $\{\mu, \nu, \rho, \delta\}$ are both $\{0, 1, 2, 3\}$, which forces $\delta = \sigma$: $X$ is diagonal. For fixed $\sigma = \delta$ (no sum), $(\mu, \nu, \rho)$ runs over the $3! = 6$ orderings of the other three values, each term $-1$ as in Step 1: $X_\sigma{}^\delta = -6\,\delta^\delta{}_\sigma$. Its trace is $-24$, agreeing with Step 1.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-3|Theorem §C1a.5.3]], 1 ($\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\delta} = -6\delta^\delta_\sigma$, $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma} = -24$); numerical check.

^sol-wr-5-b

### (c) Momentum conservation kills the contraction (PS1.3(b))

![[PHY 513 Worksheet — Relativity#^wr-5-c]]

> [!success]- Solution
> **Answer.** The contraction vanishes.
>
> **Step 1** (lower-index conservation). Lowering is linear: $\sum_ip_{i\mu} = g_{\mu\nu}\sum_ip_i^\nu = 0$, so $p_{4\sigma} = -(p_{1\sigma} + p_{2\sigma} + p_{3\sigma})$.
>
> **Step 2** (substitute). $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = -\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{1\sigma} - \varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{2\sigma} - \varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{3\sigma}$.
>
> **Step 3** (each term is zero). In the first term $p_{1\mu}p_{1\sigma}$ is symmetric in $(\mu, \sigma)$ and $\varepsilon$ is antisymmetric in that pair: zero by Problem 4(a). Likewise $(\nu, \sigma)$ in the second and $(\rho, \sigma)$ in the third.
>
> **Second route.** $\varepsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma = -\det[a\,\vert\,b\,\vert\,c\,\vert\,d]$; adding the first three columns to the fourth gives the zero column.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]] (home of PS1.3(b), the determinant route through [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 4); the user's submitted Problem Set 1, Problem 3(b), as written, also takes the determinant route; the symmetric–antisymmetric route of Steps 2–3 is the course solution's.

^sol-wr-5-c

### (d) A pseudoscalar

![[PHY 513 Worksheet — Relativity#^wr-5-d]]

> [!success]- Solution
> **Answer.** $I \mapsto (\det\Lambda)\,I$: invariant under $SO(1,3)$, $I \mapsto -I$ under $\mathcal P$.
>
> **Step 1** (rewrite). Moving each contracted pair's heights, $I = \varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = \varepsilon_{\mu\nu\rho\sigma}p_1^\mu p_2^\nu p_3^\rho p_4^\sigma$.
>
> **Step 2** (transform). With $p'^\mu = \Lambda^\mu{}_\alpha p^\alpha$ and $\varepsilon$ a fixed array: $I' = \varepsilon_{\mu\nu\rho\sigma}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Lambda^\rho{}_\gamma\Lambda^\sigma{}_\delta\,p_1^\alpha p_2^\beta p_3^\gamma p_4^\delta = (\det\Lambda)\,\varepsilon_{\alpha\beta\gamma\delta}p_1^\alpha p_2^\beta p_3^\gamma p_4^\delta = (\det\Lambda)\,I$.
>
> **Step 3.** $\det\mathcal P = -1$ although $\mathcal P^{\mathsf T}g\mathcal P = g$: $I$ is a pseudoscalar.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 1; [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-1|Example §C1a.5.1]] ("a pseudoscalar, invariant only under $\det\Lambda = +1$").

^sol-wr-5-d

## Problem 6. Elastic scattering and the momentum transfer

![[PHY 513 Worksheet — Relativity#^wr-6]]

### (a) The momentum transfer in the laboratory (PS1.5(e))

![[PHY 513 Worksheet — Relativity#^wr-6-a]]

> [!success]- Solution
> **Answer.** $t = m_2^2 + m_4^2 - 2m_2E_4$, which for $m_2 = m_4$ is $-2m_4(E_4 - m_4)$.
>
> **Step 1** (bring in the target). Conservation $p_1 + p_2 = p_3 + p_4$ gives $q = p_1 - p_3 = p_4 - p_2$.
>
> **Step 2** (expand). $q^2 = p_4^2 + p_2^2 - 2p_2\cdot p_4 = m_4^2 + m_2^2 - 2p_2\cdot p_4$.
>
> **Step 3** (laboratory). $p_2 = (m_2, \mathbf 0)$, $p_4 = (E_4, \mathbf p_4)$, so $p_2\cdot p_4 = m_2E_4 - \mathbf 0\cdot\mathbf p_4 = m_2E_4$.
>
> **Step 4** (elastic). $m_2 = m_4$: $t = 2m_4^2 - 2m_4E_4 = -2m_4(E_4 - m_4) \le 0$, minus twice the target mass times the kinetic energy it receives. The form $p_4 - p_2$ is better than $p_1 - p_3$ because both of its momenta are of the particle at rest initially.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 2; the user's submitted Problem Set 1, Problem 5(e), as written (same route, $q = p_4 - p_2$).

^sol-wr-6-a

### (b) s and t in the centre-of-mass system (PS1.5(f))

![[PHY 513 Worksheet — Relativity#^wr-6-b]]

> [!success]- Solution
> **Answer.** $s = (E_1' + E_2')^2 = E_{\rm cms}^2$; $t = -2p'^2(1 - \cos\theta') = -4p'^2\sin^2(\theta'/2)$.
>
> **Step 1** ($s$). Both are invariants, so evaluate in the cms: $p_1 + p_2 = (E_1' + E_2', \mathbf p' - \mathbf p') = (E_{\rm cms}, \mathbf 0)$, so $s = E_{\rm cms}^2$.
>
> **Step 2** ($t$, general). $p_1' = (E_1', \mathbf p')$, $p_3' = (E_3', \mathbf q')$ with $\mathbf p'\cdot\mathbf q' = p'q'\cos\theta'$: $t = p_1^2 + p_3^2 - 2p_1\cdot p_3 = m_1^2 + m_3^2 - 2E_1'E_3' + 2p'q'\cos\theta'$.
>
> **Step 3** ($q' = p'$). Energy conservation in the cms with $m_3 = m_1$, $m_4 = m_2$: $\sqrt{p'^2 + m_1^2} + \sqrt{p'^2 + m_2^2} = \sqrt{q'^2 + m_1^2} + \sqrt{q'^2 + m_2^2}$, i.e. $f(p'^2) = f(q'^2)$ with $f(x) = \sqrt{x + m_1^2} + \sqrt{x + m_2^2}$ strictly increasing on $x \ge 0$. So $q' = p'$ and then $E_3' = E_1' = \sqrt{p'^2 + m_1^2}$.
>
> **Step 4** (simplify). $t = 2m_1^2 - 2(p'^2 + m_1^2) + 2p'^2\cos\theta' = -2p'^2(1 - \cos\theta') = -4p'^2\sin^2(\theta'/2)$, using $1 - \cos\theta' = 2\sin^2(\theta'/2)$. It is $\le 0$ and vanishes only for forward scattering.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 3; [[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]] ($s$ is the squared cms energy); the user's submitted Problem Set 1, Problem 5(f), as written (it proves $q' = p'$ by the strict monotonicity of Step 3, which the course solution states without proof).

^sol-wr-6-b

### (c) The sum rule and the variable u

![[PHY 513 Worksheet — Relativity#^wr-6-c]]

> [!success]- Solution
> **Answer.** $s + t + u = \sum_im_i^2$; for equal masses $u = -2p'^2(1 + \cos\theta') = -4p'^2\cos^2(\theta'/2)$; $-4p'^2 \le t, u \le 0$; $t = 0$ forward ($\theta' = 0$), $u = 0$ backward ($\theta' = \pi$).
>
> **Step 1** (sum rule). $s = m_1^2 + m_2^2 + 2p_1\cdot p_2$, $t = m_1^2 + m_3^2 - 2p_1\cdot p_3$, $u = m_1^2 + m_4^2 - 2p_1\cdot p_4$. Adding, $s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 + 2p_1\cdot(p_2 - p_3 - p_4)$, and conservation gives $p_2 - p_3 - p_4 = -p_1$, so the last term is $-2m_1^2$.
>
> **Step 2** ($u$, equal masses). In the cms all four energies equal $E' = \sqrt{p'^2 + m^2}$ (Step 3 of (b)), and $p_4' = (E', -\mathbf q')$. So $p_1 - p_4 = (0, \mathbf p' + \mathbf q')$ and $u = -\lvert\mathbf p' + \mathbf q'\rvert^2 = -(2p'^2 + 2p'^2\cos\theta') = -4p'^2\cos^2(\theta'/2)$.
>
> **Step 3** (check and ranges). $s = 4E'^2 = 4(p'^2 + m^2)$, so $s + t + u = 4p'^2 + 4m^2 - 4p'^2(\sin^2 + \cos^2)(\theta'/2) = 4m^2$. As $\theta'$ runs over $[0, \pi]$, $t$ runs from $0$ to $-4p'^2 = -(s - 4m^2)$ and $u$ the other way.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1 (the sum rule) and 3 ($t$). The formula for $u$ is derived here; check: $s + t + u = 4m^2$ by part 1 of that theorem.

^sol-wr-6-c

## Problem 7. Invariants in a convenient frame: thresholds and colliders

![[PHY 513 Worksheet — Relativity#^wr-7]]

### (a) Threshold for neutral-pion production

![[PHY 513 Worksheet — Relativity#^wr-7-a]]

> [!success]- Solution
> **Answer.** $K_{\rm th} = \dfrac{(2m_p + m_\pi)^2 - (2m_p)^2}{2m_p} = 2m_\pi + \dfrac{m_\pi^2}{2m_p} = 270.0 + 9.7 = 279.7$ MeV.
>
> **Step 1** (lab). Beam $p_a = (E, \mathbf p)$, target $p_b = (m_p, \mathbf 0)$: $s = (p_a + p_b)^2 = 2m_p^2 + 2m_pE$.
>
> **Step 2** (cms after the collision). $s = \bigl(\sum E_i^*\bigr)^2 \ge (2m_p + m_\pi)^2$, with equality exactly when all products are at rest in the cms. $s$ is conserved and invariant, so the threshold is $2m_p^2 + 2m_pE_{\rm th} = (2m_p + m_\pi)^2$.
>
> **Step 3** (kinetic energy). $K_{\rm th} = E_{\rm th} - m_p = \dfrac{(2m_p + m_\pi)^2 - 2m_p^2 - 2m_p^2}{2m_p} = \dfrac{4m_pm_\pi + m_\pi^2}{2m_p}$; numerically $2\cdot135.0 + 135.0^2/1876.6 = 279.7$ MeV.
>
> **Step 4** (why more than $m_\pi$). The products must carry the beam momentum; their common motion in the lab costs kinetic energy that cannot become mass.
>
> *Checked against:* [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-7|REL Theorem §B2.1.7]] (with $M_f = 2m_p + m_\pi$, $m_a = m_b = m_p$, $c = 1$) and [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^rem-b2-1-6|REL §B2.1, Remark: Why the threshold exceeds the mass difference]]; [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-1|§C1a.5, Remark: Compute invariants, not transformations]]; numerical check.

^sol-wr-7-a

### (b) The centre of mass at threshold

![[PHY 513 Worksheet — Relativity#^wr-7-b]]

> [!success]- Solution
> **Answer.** $\beta_{\rm cm} = \dfrac{\lvert\mathbf p_{\rm lab}\rvert}{E_{\rm lab} + m_p} \approx 0.360$ ($\gamma_{\rm cm} \approx 1.072$); in the cms all three final particles are at rest, so in the lab they move together with $\beta_{\rm cm}$.
>
> **Step 1.** $E_{\rm lab} = m_p + K_{\rm th} = 1218.0$ MeV, $\lvert\mathbf p_{\rm lab}\rvert = \sqrt{1218.0^2 - 938.3^2} = 776.6$ MeV.
>
> **Step 2.** The total four-momentum $P = (E_{\rm lab} + m_p, \mathbf p_{\rm lab})$ is timelike; the cms is its rest frame, which moves with $\mathbf P/P^0$: $\beta_{\rm cm} = 776.6/2156.3 = 0.360$; $\gamma_{\rm cm} = P^0/\sqrt s = 2156.3/2011.6 = 1.072$ with $\sqrt s = 2m_p + m_\pi$.
>
> *Checked against:* [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^thm-b2-1-7|REL Theorem §B2.1.7]] ("at threshold all products are at rest in the centre-of-mass frame and move together in the lab with velocity $\mathbf u_{\rm cm} = c^2\mathbf p_a/(E_a + m_bc^2)$"); numerical check.

^sol-wr-7-b

### (c) Colliders against fixed targets

![[PHY 513 Worksheet — Relativity#^wr-7-c]]

> [!success]- Solution
> **Answer.** $s = 4E^2$; $E_{\rm lab} = \dfrac{2E^2}{m} - m$; for $E = 6.8$ TeV protons $E_{\rm lab} \approx 9.9\times10^{7}$ GeV $\approx 10^{17}$ eV, about $1.4\times10^4$ times the beam energy.
>
> **Step 1** (collider). $p_1 = (E, \mathbf p)$, $p_2 = (E, -\mathbf p)$: $p_1 + p_2 = (2E, \mathbf 0)$, $s = 4E^2$.
>
> **Step 2** (fixed target). $s = 2m^2 + 2mE_{\rm lab}$ (Problem 7(a), Step 1). Equate: $E_{\rm lab} = (4E^2 - 2m^2)/2m = 2E^2/m - m$.
>
> **Step 3** (numbers). $2(6800)^2/0.9383 - 0.94 = 9.86\times10^7$ GeV. Since $E_{\rm cms} = \sqrt s$ grows only like $\sqrt{E_{\rm lab}}$ on a fixed target, colliding beams win.
>
> *Checked against:* [[§B2.1 Four-Velocity, Four-Momentum and Collisions#^rem-b2-1-6|REL §B2.1, Remark: Why the threshold exceeds the mass difference]] ("the energy of one beam particle in the rest frame of the other is $2E^2/mc^2 - mc^2$"); the $\sqrt{E_{\rm lab}}$ growth is Problem Set 1, Problem 5(c) ([[PHY 513 PS Drill#^ps1-5|PS Drill, PS1.5]]).

^sol-wr-7-c

## Problem 8. Derivatives with four-vectors, I (PS1.6(a)–(d))

![[PHY 513 Worksheet — Relativity#^wr-8]]

![[PHY 513 Worksheet — Relativity#^wr-8-a]]

![[PHY 513 Worksheet — Relativity#^wr-8-b]]

![[PHY 513 Worksheet — Relativity#^wr-8-c]]

![[PHY 513 Worksheet — Relativity#^wr-8-d]]

> [!success]- Solution
> **Answer.** (a) $2x_\mu$; (b) $2g_{\mu\nu}$; (c) $8$; (d) $192$.
>
> **Step 0** (rename the dummy). Write $\rho = x_\alpha x^\alpha = g_{\alpha\beta}x^\alpha x^\beta$, so that the derivative index $\mu$ does not clash with the summed one; use $\partial_\mu x^\alpha = \delta^\alpha{}_\mu$ and the constancy of $g$.
>
> **(a)** $\partial_\mu\rho = g_{\alpha\beta}(\delta^\alpha{}_\mu x^\beta + x^\alpha\delta^\beta{}_\mu) = x_\mu + x_\mu = 2x_\mu$.
>
> **(b)** $\partial_\mu\partial_\nu\rho = \partial_\mu(2x_\nu) = 2\partial_\mu(g_{\nu\beta}x^\beta) = 2g_{\nu\beta}\delta^\beta{}_\mu = 2g_{\mu\nu}$, symmetric as a second derivative must be.
>
> **(c)** $\Box\rho = g^{\mu\nu}\partial_\mu\partial_\nu\rho = 2g^{\mu\nu}g_{\mu\nu} = 2\delta^\mu{}_\mu = 2\cdot4 = 8$.
>
> **(d)** Chain rule: $\partial_\mu\rho^2 = 2\rho\,\partial_\mu\rho = 4\rho x_\mu$. Product rule: $\Box\rho^2 = \partial^\mu(4\rho x_\mu) = 4(\partial^\mu\rho)x_\mu + 4\rho\,\partial^\mu x_\mu = 4(2x^\mu)x_\mu + 4\rho\cdot4 = 8\rho + 16\rho = 24\rho$. Then $\Box^2\rho^2 = \Box(24\rho) = 24\cdot8 = 192$.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-7|Theorem §C1a.5.7]] ($\partial_\mu(x^2) = 2x_\mu$, $\partial_\mu\partial_\nu(x^2) = 2g_{\mu\nu}$, $\partial_\mu x^\mu = 4$), [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] ($\partial^2\rho = 8$, $\partial^2\rho^2 = 24\rho$); the user's submitted Problem Set 1, Problem 6(a)–(d), as written ($192$; the course solution agrees).

^sol-wr-8

## Problem 9. Derivatives with four-vectors, II

![[PHY 513 Worksheet — Relativity#^wr-9]]

### (a) A derivative of the radial derivative (PS1.6(e))

![[PHY 513 Worksheet — Relativity#^wr-9-a]]

> [!success]- Solution
> **Answer.** $\partial_\sigma\bigl(x^\mu\partial_\mu f(\rho)\bigr) = 4x_\sigma\bigl(f'(\rho) + \rho f''(\rho)\bigr) = 4x_\sigma\,\dfrac{d(\rho f')}{d\rho}$.
>
> **Step 1.** $\partial_\mu f(\rho) = f'(\rho)\,\partial_\mu\rho = 2x_\mu f'$, so $x^\mu\partial_\mu f = 2x^\mu x_\mu f' = 2\rho f'$.
>
> **Step 2.** $\partial_\sigma(2\rho f') = 2(\partial_\sigma\rho)f' + 2\rho f''\,\partial_\sigma\rho = 4x_\sigma f' + 4x_\sigma\rho f''$.
>
> **Step 3** (the other route). Product rule without simplifying first: $\partial_\sigma(x^\mu\partial_\mu f) = \delta^\mu{}_\sigma\partial_\mu f + x^\mu\partial_\sigma\partial_\mu f = 2x_\sigma f' + x^\mu\partial_\sigma(2x_\mu f') = 2x_\sigma f' + 2x^\mu g_{\sigma\mu}f' + 2x^\mu x_\mu\,2x_\sigma f'' = 4x_\sigma f' + 4\rho x_\sigma f''$: the same.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] ($\partial_\mu f = 2x_\mu f'$, $x^\mu\partial_\mu f = 2\rho f'$); the user's submitted Problem Set 1, Problem 6(e), as written ($4x_\sigma(f' + \rho f'')$; the course solution writes $4x_\sigma\,d(\rho f')/d\rho$).

^sol-wr-9-a

### (b) 1/ρ is harmonic away from the cone (PS1.6(f))

![[PHY 513 Worksheet — Relativity#^wr-9-b]]

> [!success]- Solution
> **Answer.** $\Box(c_1/\rho + c_2) = c_1\Box(1/\rho) = 0$ for $\rho \ne 0$.
>
> **Step 1.** $\Box c_2 = 0$. Chain rule: $\partial_\mu(1/\rho) = -\rho^{-2}\,2x_\mu$.
>
> **Step 2.** $\Box(1/\rho) = \partial^\mu(-2x_\mu\rho^{-2}) = -2(\partial^\mu x_\mu)\rho^{-2} - 2x_\mu(-2\rho^{-3})(2x^\mu) = -8\rho^{-2} + 8\rho\,\rho^{-3} = 0$, every step valid where $\rho \ne 0$.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] ("$f = c_1/\rho + c_2$ … $\partial^2(1/x^2) = 0$ wherever $x^2 \ne 0$"); the user's submitted Problem Set 1, Problem 6(f), as written.

^sol-wr-9-b

### (c) The general formula in d dimensions

![[PHY 513 Worksheet — Relativity#^wr-9-c]]

> [!success]- Solution
> **Answer.** $\Box f = 4\rho f'' + 2d\,f'$; the solutions away from $\rho = 0$ are $f = c_1\lvert\rho\rvert^{1 - d/2} + c_2$ on each of $\rho > 0$ and $\rho < 0$; for $d = 4$, $c_1/\rho + c_2$ (absorbing the sign into $c_1$ on $\rho < 0$).
>
> **Step 1.** $\Box f = \partial^\mu(2x_\mu f') = 2(\partial^\mu x_\mu)f' + 2x_\mu f''\,\partial^\mu\rho = 2d\,f' + 4x_\mu x^\mu f'' = 2d\,f' + 4\rho f''$, since $\partial^\mu x_\mu = \delta^\mu{}_\mu = d$.
>
> **Step 2** (solve). $\Box f = 0$ is first order in $h = f'$: $h'/h = -d/(2\rho)$, so $h = C\lvert\rho\rvert^{-d/2}$ on each side of $\rho = 0$, and integrating, $f = c_1\lvert\rho\rvert^{1 - d/2} + c_2$ ($d \ne 2$). Check with a power: $f = \rho^a$ gives $\Box f = 2a(d + 2a - 2)\rho^{a-1}$, zero for $a = 0$ or $a = 1 - d/2$.
>
> **Step 3** ($d = 4$). $1 - d/2 = -1$: $f = c_1/\rho + c_2$, part (b); and $\Box\rho = 2d = 8$, $\Box\rho^2 = 2d\cdot2\rho + 4\rho\cdot2 = 24\rho$, as in Problem 8.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] (the formula "in $d$ spacetime dimensions: $2d\,f' + 4\rho f''$" and the $d = 4$ solutions). The $d$-dimensional solutions are derived here; check: $d = 4$ gives the theorem's $c_1/\rho + c_2$.

^sol-wr-9-c

### (d) Where the source sits

![[PHY 513 Worksheet — Relativity#^wr-9-d]]

> [!success]- Solution
> **Answer.** $\rho = 0$ is the whole light cone, where $1/\rho$ blows up, so the pointwise computation says nothing there. As a distribution, $1/x^2$ is not even defined (it is not locally integrable across the cone, like $1/u$ at $u = 0$); distributions arise as boundary values, and different ones satisfy different equations: the Wightman boundary value $-\frac{1}{4\pi^2}\frac{1}{x^2 - i0\,x^0}$ (massless $D_W$) solves $\partial^2D_W = 0$ everywhere, while the Feynman one $-\frac{1}{4\pi^2}\frac{1}{x^2 - i0}$ (massless $D_F$) solves $\partial^2D_F = -i\delta^4(x)$: a source at the tip $x = 0$ of the cone, invisible to the computation at $\rho \ne 0$.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^rem-c1a-5-3|§C1a.5, Remark: In what sense 1/x² is harmonic, and where the source sits]].

^sol-wr-9-d

## Problem 10. Derivatives with respect to a four-vector or a tensor

![[PHY 513 Worksheet — Relativity#^wr-10]]

### (a) Momentum derivatives

![[PHY 513 Worksheet — Relativity#^wr-10-a]]

> [!success]- Solution
> **Answer.** $\dfrac{\partial(p\cdot q)}{\partial p^\mu} = q_\mu$; $\ \dfrac{\partial(p^2)^2}{\partial p_\mu} = 4p^2p^\mu$; $\ \dfrac{\partial}{\partial p^\mu}\dfrac{1}{p^2 - m^2 + i\epsilon} = -\dfrac{2p_\mu}{(p^2 - m^2 + i\epsilon)^2}$.
>
> **Step 1.** $p\cdot q = g_{\alpha\beta}p^\alpha q^\beta$ and $\partial p^\alpha/\partial p^\mu = \delta^\alpha{}_\mu$: $\partial(p\cdot q)/\partial p^\mu = g_{\mu\beta}q^\beta = q_\mu$. A derivative with respect to an upper component carries a lower index.
>
> **Step 2.** $\partial(p^2)/\partial p_\mu = 2p^\mu$ (the same computation with all heights flipped), so by the chain rule $\partial(p^2)^2/\partial p_\mu = 2p^2\cdot2p^\mu = 4p^2p^\mu$.
>
> **Step 3.** $\partial(p^2)/\partial p^\mu = 2p_\mu$ and $\frac{d}{du}(u - m^2 + i\epsilon)^{-1} = -(u - m^2 + i\epsilon)^{-2}$ give the third.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]], 1–3 ($\partial/\partial a^\mu$ is a covector; $\partial(a_\nu a^\nu)/\partial a^\mu = 2a_\mu$; $\partial(b_\nu a^\nu)/\partial a^\mu = b_\mu$).

^sol-wr-10-a

### (b) The Maxwell Lagrangian

![[PHY 513 Worksheet — Relativity#^wr-10-b]]

> [!success]- Solution
> **Answer.** $\partial(F_{\alpha\beta}F^{\alpha\beta})/\partial(\partial_\mu A_\nu) = 4F^{\mu\nu}$; the Euler–Lagrange equation is $\partial_\mu F^{\mu\nu} = J^\nu$.
>
> **Step 1** (one factor). $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$, and the sixteen $\partial_\mu A_\nu$ are independent: $\partial F_{\alpha\beta}/\partial(\partial_\mu A_\nu) = \delta_\alpha{}^\mu\delta_\beta{}^\nu - \delta_\beta{}^\mu\delta_\alpha{}^\nu$.
>
> **Step 2** (product). $F_{\alpha\beta}F^{\alpha\beta} = g^{\alpha\gamma}g^{\beta\delta}F_{\alpha\beta}F_{\gamma\delta}$; the product rule gives two equal terms, $2F^{\alpha\beta}\,\partial F_{\alpha\beta}/\partial(\partial_\mu A_\nu) = 2F^{\alpha\beta}(\delta_\alpha{}^\mu\delta_\beta{}^\nu - \delta_\beta{}^\mu\delta_\alpha{}^\nu) = 2(F^{\mu\nu} - F^{\nu\mu}) = 4F^{\mu\nu}$.
>
> **Step 3** (Euler–Lagrange). $\partial\mathcal L/\partial(\partial_\mu A_\nu) = -\frac14\cdot4F^{\mu\nu} = -F^{\mu\nu}$, $\partial\mathcal L/\partial A_\nu = -J^\nu$; so $\partial_\mu(-F^{\mu\nu}) - (-J^\nu) = 0$, i.e. $\partial_\mu F^{\mu\nu} = J^\nu$.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-11|Theorem §C1a.5.11]], 1 and 4; [[§C1a.7 Relativistic Electrodynamics in Index Form#^rem-c1a-7-2|§C1a.7, Remark: Electrodynamics as the template for field theory]] ($\partial\mathcal L/\partial(\partial_\mu A_\nu) = -F^{\mu\nu}$, $\partial\mathcal L/\partial A_\nu = -J^\nu$).

^sol-wr-10-b

### (c) Independent components

![[PHY 513 Worksheet — Relativity#^wr-10-c]]

> [!success]- Solution
> **Answer.** A partial derivative with respect to $p^\mu$ holds the other three components fixed. On the mass shell $p^0 = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ is a function of $\mathbf p$, so the four components are not independent and "$\partial/\partial p^0$ at fixed $\mathbf p$" moves off the shell. Differentiate first, treating all four as independent, then impose $p^2 = m^2$. Example: $\partial(p^2)/\partial p^\mu = 2p_\mu \ne 0$, although $p^2 = m^2$ is constant on the shell.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-10|Theorem §C1a.5.10]] (last sentence).

^sol-wr-10-c

## Problem 11. Maxwell's equations in covariant form

![[PHY 513 Worksheet — Relativity#^wr-11]]

### (a) The two invariants

![[PHY 513 Worksheet — Relativity#^wr-11-a]]

> [!success]- Solution
> **Answer.** $F_{\mu\nu}F^{\mu\nu} = 2(\mathbf B^2 - \mathbf E^2)$; $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$; in Peskin–Schroeder's convention $+8\,\mathbf E\cdot\mathbf B$.
>
> **Step 1** (lower components). $F_{0i} = g_{00}g_{ii}F^{0i} = -F^{0i} = E^i$ and $F_{ij} = g_{ii}g_{jj}F^{ij} = F^{ij} = -\varepsilon_{ijk}B^k$.
>
> **Step 2** (scalar). $F_{\mu\nu}F^{\mu\nu} = 2F_{0i}F^{0i} + F_{ij}F^{ij} = 2E^i(-E^i) + \varepsilon_{ijk}\varepsilon_{ijl}B^kB^l = -2\mathbf E^2 + 2\delta_{kl}B^kB^l = 2(\mathbf B^2 - \mathbf E^2)$ ($F_{00} = 0$; the factor $2$ counts $0i$ and $i0$).
>
> **Step 3** (pseudoscalar). A term is nonzero only if exactly one of the four indices is $0$. With $0$ in the first pair: $\varepsilon^{0ijk}F_{0i}F_{jk} + \varepsilon^{i0jk}F_{i0}F_{jk} = 2\varepsilon^{0ijk}F_{0i}F_{jk}$. With $0$ in the second pair: $\varepsilon^{jk0i} = \varepsilon^{0ijk}$ (moving $0$ and then $i$ to the front costs two transpositions each), so again $2\varepsilon^{0ijk}F_{0i}F_{jk}$. Total $4\varepsilon^{0ijk}F_{0i}F_{jk}$, with $\varepsilon^{0ijk} = \varepsilon_{ijk}$: $4\varepsilon_{ijk}E^i(-\varepsilon_{jkl}B^l) = -4\cdot2\delta_{il}E^iB^l = -8\,\mathbf E\cdot\mathbf B$.
>
> **Step 4** (Peskin–Schroeder). One $\varepsilon$: the sign flips, $+8\,\mathbf E\cdot\mathbf B$; the scalar has no $\varepsilon$ and does not change.
>
> *Checked against:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]], 2 (both invariants and the Peskin–Schroeder sign); [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]] ($F_{0i} = E^i$, $F_{ij} = -\varepsilon_{ijk}B^k$); numerical check with random $\mathbf E$, $\mathbf B$.

^sol-wr-11-a

### (b) The fields after a boost along x

![[PHY 513 Worksheet — Relativity#^wr-11-b]]

> [!success]- Solution
> **Answer.** $E'_x = E_x$, $E'_y = \gamma(E_y + vB_z)$, $E'_z = \gamma(E_z - vB_y)$; $B'_x = B_x$, $B'_y = \gamma(B_y - vE_z)$, $B'_z = \gamma(B_z + vE_y)$.
>
> **Step 1** (dictionary). $E^i = F^{i0}$; from $F^{ij} = -\varepsilon_{ijk}B^k$: $B_x = -F^{23}$, $B_y = -F^{31}$, $B_z = -F^{12}$, and $F^{21} = B_z$, $F^{31} = -B_y$, $F^{02} = -E_y$.
>
> **Step 2** (the boost). Only $\Lambda^0{}_0 = \Lambda^1{}_1 = \gamma$ and $\Lambda^0{}_1 = \Lambda^1{}_0 = \gamma v$ differ from the identity; indices $2$, $3$ are untouched.
>
> **Step 3** ($\mathbf E'$). $E'_x = F'^{10} = \Lambda^1{}_0\Lambda^0{}_1F^{01} + \Lambda^1{}_1\Lambda^0{}_0F^{10} = \gamma^2v^2(-E_x) + \gamma^2E_x = E_x$. $E'_y = F'^{20} = \Lambda^0{}_\beta F^{2\beta} = \gamma F^{20} + \gamma vF^{21} = \gamma(E_y + vB_z)$. $E'_z = F'^{30} = \gamma F^{30} + \gamma vF^{31} = \gamma(E_z - vB_y)$.
>
> **Step 4** ($\mathbf B'$). $B'_x = -F'^{23} = -F^{23} = B_x$. $B'_y = -F'^{31} = -\Lambda^1{}_\beta F^{3\beta} = -(\gamma vF^{30} + \gamma F^{31}) = \gamma(B_y - vE_z)$. $B'_z = -F'^{12} = -\Lambda^1{}_\alpha F^{\alpha2} = -(\gamma vF^{02} + \gamma F^{12}) = \gamma(B_z + vE_y)$.
>
> **Step 5** (check with the passive formula). The active boost by $+v\hat{\mathbf x}$ is the passive change to a frame moving with $\mathbf u = -v\hat{\mathbf x}$, and $\mathbf E'_\perp = \gamma(\mathbf E + \mathbf u\times\mathbf B)_\perp$, $\mathbf B'_\perp = \gamma(\mathbf B - \mathbf u\times\mathbf E)_\perp$ with $\mathbf u\times\mathbf B = -v(0, -B_z, B_y)$ reproduce Steps 3–4. The $z$-boost of Lecture 1 ($E'_x = \gamma(E_x + vB_y)$) is the same result with the axes relabelled cyclically.
>
> *Checked against:* [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-2|REL Theorem §B4.2.2]] (passive, $v \to -v$), [[§C1a.7 Relativistic Electrodynamics in Index Form#^ex-c1a-7-1|Example §C1a.7.1]] and [[§C1a.7 Relativistic Electrodynamics in Index Form#^cau-c1a-7-2|§C1a.7, Caution: The sign of the v × B term]] (active versus passive sign); numerical check $F' = \Lambda F\Lambda^{\mathsf T}$.

^sol-wr-11-b

### (c) E·B is invariant

![[PHY 513 Worksheet — Relativity#^wr-11-c]]

> [!success]- Solution
> **Answer.** $\mathbf E'\cdot\mathbf B' = E_xB_x + \gamma^2(1 - v^2)(E_yB_y + E_zB_z) = \mathbf E\cdot\mathbf B$.
>
> **Step 1.** $E'_yB'_y + E'_zB'_z = \gamma^2\bigl[(E_y + vB_z)(B_y - vE_z) + (E_z - vB_y)(B_z + vE_y)\bigr]$.
>
> **Step 2.** Expand: $E_yB_y - vE_yE_z + vB_zB_y - v^2B_zE_z + E_zB_z + vE_zE_y - vB_yB_z - v^2B_yE_y$; the four terms linear in $v$ cancel in pairs, leaving $(1 - v^2)(E_yB_y + E_zB_z)$, and $\gamma^2(1 - v^2) = 1$.
>
> *Checked against:* [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]] ($\mathbf E\cdot\mathbf B$ is, up to $-\frac18$, the invariant $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$); numerical check.

^sol-wr-11-c

### (d) A pure electric field, boosted

![[PHY 513 Worksheet — Relativity#^wr-11-d]]

> [!success]- Solution
> **Answer.** $\mathbf E' = \gamma E\,\hat{\mathbf y}$, $\mathbf B' = \gamma vE\,\hat{\mathbf z}$, and $\mathbf v\times\mathbf E' = v\hat{\mathbf x}\times\gamma E\hat{\mathbf y} = \gamma vE\,\hat{\mathbf z} = \mathbf B'$.
>
> **Step 1.** Put $E_y = E$, all else $0$, in (b): $E'_y = \gamma E$, $B'_z = \gamma vE$, the others vanish.
>
> **Step 2** (reading). The active boost sets the source moving with $+v\hat{\mathbf x}$; a moving charge has $\mathbf B = \mathbf v\times\mathbf E$. Both invariants check: $\mathbf E'\cdot\mathbf B' = 0$ and $\mathbf E'^2 - \mathbf B'^2 = \gamma^2(1 - v^2)E^2 = E^2$.
>
> *Checked against:* [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-2|REL Theorem §B4.2.2]] ("if $\mathbf B = 0$ in $S$, then $\mathbf B' = -\mathbf v\times\mathbf E'/c^2$" for the passive frame velocity $\mathbf v$; the active boost is $\mathbf v \to -\mathbf v$); numerical check.

^sol-wr-11-d

# Lecture 2. Natural units and causality

## Problem 12. Natural units

![[PHY 513 Worksheet — Relativity#^wr-12]]

### (a) Mass dimensions

![[PHY 513 Worksheet — Relativity#^wr-12-a]]

> [!success]- Solution
> **Answer.** $[x^\mu] = -1$, $[\partial_\mu] = 1$, $[d^4x] = -4$, $[\delta^4(x)] = 4$, $[d^3p/2E_{\mathbf p}] = 2$, $[\delta^3(\mathbf p)] = -3$, $[\phi] = 1$, $[\psi] = \frac32$.
>
> **Step 1.** A length is an inverse mass ($\hbar c/L$ is an energy): $[x^\mu] = -1$. A derivative divides by its variable, an integral multiplies: $[\partial_\mu] = 1$, $[d^4x] = -4$; $\int d^4x\,\delta^4(x) = 1$ forces $[\delta^4(x)] = 4$; $[d^3p] = 3$, $[E_{\mathbf p}] = 1$, $[\delta^3(\mathbf p)] = -3$.
>
> **Step 2** (fields). The action is dimensionless and $[d^4x] = -4$, so $[\mathcal L] = 4$; $\frac12\partial_\mu\phi\,\partial^\mu\phi$ gives $2 + 2[\phi] = 4$, $[\phi] = 1$; $\bar\psi\,i\slashed\partial\psi$ gives $1 + 2[\psi] = 4$, $[\psi] = \frac32$.
>
> **Step 3** (three reasons for $[\partial_\mu] = 1$). (i) Length is an inverse mass, $[x^\mu] = -1$. (ii) $\partial_\mu = \partial/\partial x^\mu$ divides by $x^\mu$. (iii) On a plane wave $\partial_\mu e^{-ip\cdot x} = -ip_\mu e^{-ip\cdot x}$: it brings down a momentum, of dimension $1$.
>
> *Checked against:* [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 4 (derivatives, integrals, deltas), [[§C1a.2 Natural Units and Dimensional Analysis#^rem-c1a-2-3|§C1a.2, Remark: Why a derivative has mass dimension one]] (the three readings and $[\phi] = 1$, $[\psi] = \frac32$).

^sol-wr-12-a

### (b) The decay length

![[PHY 513 Worksheet — Relativity#^wr-12-b]]

> [!success]- Solution
> **Answer.** $e^{-mr} \to e^{-mcr/\hbar}$; decay length $\hbar/m_\pi c = \hbar c/m_\pi c^2 = 197.3/139.6$ fm $= 1.41$ fm.
>
> **Step 1.** The argument of an exponential is dimensionless, so $mr = r/(1/m)$ must become $r$ divided by the length that $1/m$ stands for. A length has ordinary dimension $M^0L^1T^0$, so the exponent rule restores $1/m \to (1/m)\,\hbar^{1}c^{-1} = \hbar/mc$, and $e^{-mr} \to e^{-mcr/\hbar}$.
>
> **Step 2.** $\hbar c/(m_\pi c^2) = 197.3\ \text{MeV fm}/139.6\ \text{MeV} = 1.413$ fm: the range of the pion's correlations, the Yukawa range of the nuclear force.
>
> *Checked against:* [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-1|Theorem §C1a.2.1]], 2 (the exponent rule), [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 2 ("$e^{-mt}$ … hides a scale"), [[§C1a.2 Natural Units and Dimensional Analysis#^rem-c1a-2-2|§C1a.2, Remark: Mass dimensions of common quantities]] (length $\hbar/mc$), [[§C1a.3 Causal Structure and the Causality of a Single Particle#^thm-c1a-3-6|Theorem §C1a.3.6]] (the $e^{-m\rho}$ leak, damped over the Compton wavelength $1/m$); numerical check.

^sol-wr-12-b

### (c) Cross section and lifetime

![[PHY 513 Worksheet — Relativity#^wr-12-c]]

> [!success]- Solution
> **Answer.** $1\ \text{GeV}^{-2} = 0.3894$ mb; $\tau = \hbar/\Gamma = 2.63\times10^{-25}$ s.
>
> **Step 1** (cross section). Dimension $-2$, an area: multiply by $(\hbar c)^2 = (0.1973\ \text{GeV fm})^2 = 0.03894\ \text{GeV}^2\,\text{fm}^2$. So $\sigma = 0.03894\ \text{fm}^2 = 0.3894$ mb, with $1\ \text{mb} = 0.1\ \text{fm}^2$.
>
> **Step 2** (lifetime). A width is an energy; a time is $\hbar$ divided by an energy: $\tau = 6.582\times10^{-25}\ \text{GeV s}/2.50\ \text{GeV} = 2.63\times10^{-25}$ s.
>
> *Checked against:* [[§C1a.2 Natural Units and Dimensional Analysis#^def-c1a-2-1|Def. §C1a.2.1]] ($\hbar c \simeq 197.3$ MeV fm, $1\ \text{GeV}^{-1} \simeq 0.1973\ \text{fm} \simeq 6.582\times10^{-25}$ s), [[§C1a.2 Natural Units and Dimensional Analysis#^rem-c1a-2-2|§C1a.2, Remark: Mass dimensions of common quantities]] (cross section $(\hbar/mc)^2$, $d = -2$); numerical check.

^sol-wr-12-c

### (d) Restoring c in a sum

![[PHY 513 Worksheet — Relativity#^wr-12-d]]

> [!success]- Solution
> **Answer.** $E_{\rm cms}^2 = m_1^2c^4 + m_2^2c^4 + 2m_2c^2E_{\rm lab}$.
>
> **Step 1.** Target type: energy squared, term by term. $m_1^2 \to (m_1c^2)^2$, $m_2^2 \to (m_2c^2)^2$, and $m_2E_{\rm lab} \to (m_2c^2)E_{\rm lab}$. Each term is restored separately, because $c = 1$ may have merged terms with different powers of $c$.
>
> *Checked against:* [[P4 Restoring ħ and c#^p4-5|P4, step 5]] (each term of a sum separately); [[§C1a.2 Natural Units and Dimensional Analysis#^ex-c1a-2-1|Example §C1a.2.1]], Step 1 (the same pattern for $E_{\rm CM}$).

^sol-wr-12-d

## Problem 13. Causality, the light cone and the orbits

![[PHY 513 Worksheet — Relativity#^wr-13]]

### (a) Classify the separations

![[PHY 513 Worksheet — Relativity#^wr-13-a]]

> [!success]- Solution
> **Answer.** $AB$ spacelike ($x_B^2 = 1 - 4 = -3$); $AC$ timelike and future-pointing ($x_C^2 = 9 - 1 = 8 > 0$, $x_C^0 = 3 > 0$).
>
> *Checked against:* [[§B1.3 Causal Structure and Proper Time#^def-b1-3-1|REL Def. §B1.3.1]] (with $c = 1$; timelike means $a^2 > 0$ for $g = \operatorname{diag}(+1, -1, -1, -1)$).

^sol-wr-13-a

### (b) Who comes first depends on the frame, for spacelike pairs only

![[PHY 513 Worksheet — Relativity#^wr-13-b]]

> [!success]- Solution
> **Answer.** $t'_B = \cosh\eta\,(1 + 2\tanh\eta)$: $A$, $B$ simultaneous for $\tanh\eta = -\frac12$, order reversed ($B$ before $A$) for $\tanh\eta < -\frac12$. $t'_C = \cosh\eta\,(3 + \tanh\eta) > 0$ for every $\eta$.
>
> **Step 1.** $B_x(\eta)$: $t' = \cosh\eta\,t + \sinh\eta\,x$; $A$ stays at the origin, $t'_A = 0$.
>
> **Step 2.** $t'_B = \cosh\eta + 2\sinh\eta = \cosh\eta\,(1 + 2\tanh\eta)$; $\cosh\eta > 0$, so the sign is that of $1 + 2\tanh\eta$, zero at $\tanh\eta = -\frac12$ and negative below. Passively: an observer moving with velocity $+\frac12$ along $x$ sees $A$ and $B$ simultaneous, a faster one sees $B$ first.
>
> **Step 3.** $t'_C = 3\cosh\eta + \sinh\eta = \cosh\eta\,(3 + \tanh\eta) > 0$ since $\lvert\tanh\eta\rvert < 1$. More generally $(\Lambda x)^0$ has the sign of $x^0$ for timelike $x$ and orthochronous $\Lambda$.
>
> *Checked against:* [[§B1.3 Causal Structure and Proper Time#^thm-b1-3-1|REL Theorem §B1.3.1]], 2–3 (time order invariant for timelike and null separation, not for spacelike), [[§B1.3 Causal Structure and Proper Time#^ex-b1-3-1|REL Example §B1.3.1]] (the same crossings, passive); numerical check.

^sol-wr-13-b

### (c) Reversing a spacelike vector inside SO⁺(1,3)

![[PHY 513 Worksheet — Relativity#^wr-13-c]]

> [!success]- Solution
> **Answer.** $\Lambda = B_x(\eta_1)R_z(\pi)$ with $\tanh\eta_1 = \frac45$ ($\cosh\eta_1 = \frac53$, $\sinh\eta_1 = \frac43$): $\Lambda x_B = -x_B$. No $\Lambda \in SO^+(1,3)$ reverses $x_C$, because the future and past sheets $x^2 = 8$, $x^0 \gtrless 0$ are different orbits.
>
> **Step 1** (go to equal times). $\Lambda_1 = B_x(\eta_0)$ with $\tanh\eta_0 = -\frac12$, $\cosh\eta_0 = 2/\sqrt3$, $\sinh\eta_0 = -1/\sqrt3$: $\Lambda_1x_B = \bigl(\tfrac{2}{\sqrt3} - \tfrac{2}{\sqrt3},\ -\tfrac{1}{\sqrt3} + \tfrac{4}{\sqrt3}, 0, 0\bigr) = (0, \sqrt3, 0, 0)$.
>
> **Step 2** (turn round and go back). $R_z(\pi)$ sends $(0, \sqrt3, 0, 0) \mapsto (0, -\sqrt3, 0, 0) = -\Lambda_1x_B$, so $\Lambda = \Lambda_1^{-1}R_z(\pi)\Lambda_1$ gives $\Lambda x_B = -\Lambda_1^{-1}\Lambda_1x_B = -x_B$.
>
> **Step 3** (simplify). A rotation by $\pi$ about $z$ reverses the $x$ direction, so $R_z(\pi)B_x(\eta)R_z(\pi)^{-1} = B_x(-\eta)$ (Problem 15(c) at $\theta = \pi$); hence $\Lambda = B_x(-\eta_0)B_x(-\eta_0)R_z(\pi) = B_x(-2\eta_0)R_z(\pi)$, with $\tanh(-2\eta_0) = \frac{2\cdot\frac12}{1 + \frac14} = \frac45$. Check: $R_z(\pi)x_B = (1, -2, 0, 0)$, then $t' = \frac53 - \frac83 = -1$, $x' = \frac43 - \frac{10}3 = -2$. $\det\Lambda = 1$, $\Lambda^0{}_0 = \frac53 \ge 1$.
>
> **Step 4** ($x_C$). $x_C$ is future timelike; every $\Lambda \in SO^+(1,3)$ keeps $\operatorname{sgn}x^0$ on timelike vectors, so $-x_C$ (past) is not in the orbit of $x_C$.
>
> *Checked against:* [[§C1a.4 The Lorentz Group#^thm-c1a-4-3|Theorem §C1a.4.3]], 3, and step 5 of its derivation (the construction $\Lambda_1^{-1}R(\pi)\Lambda_1$); [[§C1a.4 The Lorentz Group#^thm-c1a-4-2|Theorem §C1a.4.2]] (the orbits); exact check with sympy.

^sol-wr-13-c

### (d) Microcausality and time ordering

![[PHY 513 Worksheet — Relativity#^wr-13-d]]

> [!success]- Solution
> **Answer.** $f(-\xi) = f(\Lambda\xi) = f(\xi)$; $D_W$ is invariant, so $D_W(x - y) - D_W(y - x) = 0$ at spacelike $x - y$; $T\{\hat\phi(x)\hat\phi(y)\}$ is frame independent because the time order of timelike or null separated points is invariant, and at spacelike separation, where the order is not, the two fields commute.
>
> **Step 1.** By (c) (the same construction works for every spacelike $\xi$: boost to equal times, rotate by $\pi$ about an axis perpendicular to $\boldsymbol\xi$, boost back), there is $\Lambda \in SO^+(1,3)$ with $\Lambda\xi = -\xi$; invariance gives $f(-\xi) = f(\Lambda\xi) = f(\xi)$.
>
> **Step 2** (commutator). $\langle0\rvert\hat\phi(x)\hat\phi(y)\lvert0\rangle = D_W(x - y)$ is Lorentz invariant, so with $\xi = x - y$ spacelike, $D_W(\xi) - D_W(-\xi) = 0$. Inside the cone $\xi$ and $-\xi$ lie in different orbits (part (c), Step 4) and the commutator need not vanish.
>
> **Step 3** (time ordering). $T\{\hat\phi(x)\hat\phi(y)\} = \theta(x^0 - y^0)\hat\phi(x)\hat\phi(y) + \theta(y^0 - x^0)\hat\phi(y)\hat\phi(x)$. For timelike or null $x - y$ the step functions are the same in every frame (part (b), Step 3). For spacelike $x - y$ another frame may swap the order, but then $[\hat\phi(x), \hat\phi(y)] = 0$, so both orders give the same operator.
>
> *Checked against:* [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]] and its derivation, Steps 1–5; [[§C2b.2 The Wightman Function#^thm-c2b-2-3|Theorem §C2b.2.3]] (invariance of $D_W$); [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-1|Theorem §C2b.6.1]], 3; [[§C1a.3 Causal Structure and the Causality of a Single Particle#^rem-c1a-3-1|§C1a.3, Remark: Why the future cannot be boosted into the past]].

^sol-wr-13-d

# Lecture 7. Generators, the algebra and representations

## Problem 14. Generators as 4×4 matrices

![[PHY 513 Worksheet — Relativity#^wr-14]]

### (a) The matrices

![[PHY 513 Worksheet — Relativity#^wr-14-a]]

> [!success]- Solution
> **Answer.** With $E_{ab}$ the matrix unit (row $a$, column $b$, rows and columns $0, \dots, 3$): $J_1 = -iE_{23} + iE_{32}$, $J_2 = iE_{13} - iE_{31}$, $K_2 = i(E_{02} + E_{20})$, $K_3 = i(E_{03} + E_{30})$, i.e.
> $$J_1 = \begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix},\quad J_2 = \begin{pmatrix}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&-i&0&0\end{pmatrix},\quad K_2 = \begin{pmatrix}0&0&i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0\end{pmatrix},\quad K_3 = \begin{pmatrix}0&0&0&i\\0&0&0&0\\0&0&0&0\\i&0&0&0\end{pmatrix}.$$
>
> **Step 1** ($J_2$). $J_2 = \frac12(\varepsilon_{231}\mathcal J^{31} + \varepsilon_{213}\mathcal J^{13}) = \frac12(\mathcal J^{31} - \mathcal J^{13}) = \mathcal J^{31}$, by $\mathcal J^{13} = -\mathcal J^{31}$; likewise $J_1 = \mathcal J^{23}$.
>
> **Step 2** (rotation entries). $(\mathcal J^{31})^\mu{}_\nu = i(g^{3\mu}\delta^1{}_\nu - g^{1\mu}\delta^3{}_\nu)$: the first term lives at $(\mu, \nu) = (3, 1)$ with value $ig^{33} = -i$; the second at $(1, 3)$ with value $-ig^{11} = +i$. Same for $\mathcal J^{23}$: $-i$ at $(2, 3)$, $+i$ at $(3, 2)$.
>
> **Step 3** (boost entries). $(\mathcal J^{0k})^\mu{}_\nu = i(g^{0\mu}\delta^k{}_\nu - g^{k\mu}\delta^0{}_\nu)$: $ig^{00} = i$ at $(0, k)$ and $-ig^{kk} = +i$ at $(k, 0)$.
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] (all six matrices) and steps 1–3 of its derivation; [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-2|§C1a.6, Caution: The sign pattern of the rotation about y]] (why $J_2 = \mathcal J^{31}$ has $+i$ at $(1, 3)$); numerical check.

^sol-wr-14-a

### (b) Commutators by matrix multiplication

![[PHY 513 Worksheet — Relativity#^wr-14-b]]

> [!success]- Solution
> **Answer.** $[J_2, K_3] = iK_1$ and $[K_2, K_3] = -iJ_1$, as the algebra says ($\varepsilon_{231} = 1$).
>
> **Step 1** (rule). $E_{ab}E_{cd} = \delta_{bc}E_{ad}$.
>
> **Step 2** ($[J_2, K_3]$). $J_2K_3 = (iE_{13} - iE_{31})\,i(E_{03} + E_{30})$: only $E_{13}E_{30} = E_{10}$ survives, so $J_2K_3 = i\cdot i\,E_{10} = -E_{10}$. $K_3J_2 = i(E_{03} + E_{30})(iE_{13} - iE_{31})$: only $E_{03}E_{31} = E_{01}$ survives, with coefficient $i(-i) = 1$, so $K_3J_2 = E_{01}$. Hence $[J_2, K_3] = -(E_{01} + E_{10}) = i\cdot i(E_{01} + E_{10}) = iK_1$.
>
> **Step 3** ($[K_2, K_3]$). $K_2K_3 = i^2(E_{02} + E_{20})(E_{03} + E_{30}) = -E_{20}E_{03} = -E_{23}$; $K_3K_2 = -E_{30}E_{02} = -E_{32}$. So $[K_2, K_3] = -E_{23} + E_{32}$, and $-iJ_1 = -i(-iE_{23} + iE_{32}) = -E_{23} + E_{32}$: equal.
>
> *Checked against:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] (the $\mathbf J$, $\mathbf K$ form); numerical check.

^sol-wr-14-b

### (c) The same from the covariant algebra

![[PHY 513 Worksheet — Relativity#^wr-14-c]]

> [!success]- Solution
> **Answer.** $[\mathcal J^{02}, \mathcal J^{03}] = -i\mathcal J^{23} = -iJ_1$.
>
> **Step 1.** $(\mu\nu) = (02)$, $(\rho\sigma) = (03)$: $[\mathcal J^{02}, \mathcal J^{03}] = i\bigl(g^{20}\mathcal J^{03} - g^{00}\mathcal J^{23} - g^{23}\mathcal J^{00} + g^{03}\mathcal J^{20}\bigr)$.
>
> **Step 2.** Off-diagonal $g$'s vanish, $\mathcal J^{00} = 0$, $g^{00} = 1$: $= -i\mathcal J^{23} = -iJ_1$.
>
> *Checked against:* [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]]; the same pattern as $[\mathcal J^{01}, \mathcal J^{02}] = -iJ_3$ in the user's Lorentz-representation review (2026-10-14), §2.

^sol-wr-14-c

### (d) Hermiticity and unitarity

![[PHY 513 Worksheet — Relativity#^wr-14-d]]

> [!success]- Solution
> **Answer.** The $J_i$ are Hermitian, the $K_i$ anti-Hermitian; $B_z(\eta)$ is real symmetric, not orthogonal, so not unitary. No contradiction: the $4\times4$ matrices act on the index of a field, while $U(\Lambda)$ acts on the infinite-dimensional Hilbert space; a noncompact group like $SO^+(1,3)$ has no nontrivial finite-dimensional unitary representation.
>
> **Step 1.** For real $A$, $(iA)^\dagger = -iA^{\mathsf T}$: $J_i = i\times$(real antisymmetric) gives $J_i^\dagger = J_i$; $K_i = i\times$(real symmetric) gives $K_i^\dagger = -K_i$.
>
> **Step 2.** $B_z(\eta)^\dagger B_z(\eta) = B_z(\eta)^2 = B_z(2\eta) \ne \mathbb 1$ for $\eta \ne 0$ (its $00$ entry is $\cosh2\eta$). A Lorentz matrix preserves $x^{\mathsf T}gx$, not the Euclidean length.
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] ("Hermitian … anti-Hermitian"), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^rem-c1a-6-2|§C1a.6, Remark: Hermitian generators do not make boosts unitary]].

^sol-wr-14-d

## Problem 15. Finite transformations by exponentiation

![[PHY 513 Worksheet — Relativity#^wr-15]]

### (a) The rotation about y

![[PHY 513 Worksheet — Relativity#^wr-15-a]]

> [!success]- Solution
> **Answer.**
> $$R_y(\theta) = \begin{pmatrix}1&0&0&0\\0&\cos\theta&0&\sin\theta\\0&0&1&0\\0&-\sin\theta&0&\cos\theta\end{pmatrix}:$$
> the minus sign sits in the lower left of the $(x, z)$ block, because a rotation about $y$ turns $z$ toward $x$ (cyclic order $y$, $z$, $x$).
>
> **Step 1** (one generator). $-\frac i2(\omega_{31}\mathcal J^{31} + \omega_{13}\mathcal J^{13}) = -\frac i2(\theta\mathcal J^{31} + (-\theta)(-\mathcal J^{31})) = -i\theta\mathcal J^{31} = -i\theta J_2$ (both $\omega$ and $\mathcal J$ antisymmetric; $\theta_2 = \frac12\varepsilon_{2jk}\omega_{jk} = \theta$).
>
> **Step 2** (the real exponent). $N = -iJ_2 = -i(iE_{13} - iE_{31}) = E_{13} - E_{31}$. Powers: $N^2 = -E_{13}E_{31} - E_{31}E_{13} = -(E_{11} + E_{33})$, $N^3 = -N$.
>
> **Step 3** (sum the series). $e^{\theta N} = \mathbb 1 + (\theta - \frac{\theta^3}{3!} + \dots)N + (\frac{\theta^2}{2!} - \frac{\theta^4}{4!} + \dots)N^2 = \mathbb 1 + \sin\theta\,N + (1 - \cos\theta)N^2$. Entries: $(1,1) = (3,3) = 1 - (1 - \cos\theta) = \cos\theta$; $(1,3) = +\sin\theta$; $(3,1) = -\sin\theta$; $(0,0) = (2,2) = 1$.
>
> **Step 4** (the sign). Column $1$ is the image of $\hat{\mathbf x}$: $\cos\theta\,\hat{\mathbf x} - \sin\theta\,\hat{\mathbf z}$, as $\delta\mathbf r = \theta\,\hat{\mathbf y}\times\mathbf r$ and $\hat{\mathbf y}\times\hat{\mathbf x} = -\hat{\mathbf z}$ require. In the order $(z, x)$ the block is the standard one.
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-2|§C1a.6, Caution: The sign pattern of the rotation about y]] (the matrix and the reason), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-6|Theorem §C1a.6.6]], 2 with $\hat{\mathbf n} = \hat{\mathbf y}$; numerical check against $\exp(-i\theta J_2)$.

^sol-wr-15-a

### (b) The boost along y

![[PHY 513 Worksheet — Relativity#^wr-15-b]]

> [!success]- Solution
> **Answer.**
> $$B_y(\eta) = \begin{pmatrix}\cosh\eta&0&\sinh\eta&0\\0&1&0&0\\\sinh\eta&0&\cosh\eta&0\\0&0&0&1\end{pmatrix},\qquad B_y(\eta)\,(m, 0, 0, 0) = (m\cosh\eta, 0, m\sinh\eta, 0).$$
>
> **Step 1.** As in (a), $-\frac i2(\omega_{02}\mathcal J^{02} + \omega_{20}\mathcal J^{20}) = -i\eta\mathcal J^{02} = -i\eta K_2$.
>
> **Step 2.** $N = -iK_2 = -i\cdot i(E_{02} + E_{20}) = E_{02} + E_{20}$, $N^2 = E_{00} + E_{22}$, $N^3 = N$.
>
> **Step 3.** $e^{\eta N} = \mathbb 1 + \sinh\eta\,N + (\cosh\eta - 1)N^2$: the matrix above, symmetric (no sign pattern, unlike rotations). Its first column is the image of $(1, \mathbf 0)$: a particle at rest gets velocity $\tanh\eta$ along $+y$.
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^cau-c1a-6-2|§C1a.6, Caution: The sign pattern of the rotation about y]] ($B_y(\eta)$), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], 2 with $\hat{\mathbf n} = \hat{\mathbf y}$, [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-3|Theorem §C1a.6.3]], 3; numerical check.

^sol-wr-15-b

### (c) Rotating a boost

![[PHY 513 Worksheet — Relativity#^wr-15-c]]

> [!success]- Solution
> **Answer.** $R_z(\theta)K_1R_z(\theta)^{-1} = \cos\theta\,K_1 + \sin\theta\,K_2 = \hat{\mathbf n}\cdot\mathbf K$, so $R_z(\theta)B_x(\eta)R_z(\theta)^{-1} = e^{-i\eta\,\hat{\mathbf n}\cdot\mathbf K} = \Lambda_{\hat{\mathbf n}}(\eta)$; to first order in $\theta$ this is $K_1 \mapsto K_1 - i\theta[J_3, K_1] = K_1 + \theta K_2$.
>
> **Step 1** (conjugate the generator). $K_1 = i(E_{01} + E_{10})$ with $E_{10} = e_1e_0^{\mathsf T}$, $E_{01} = e_0e_1^{\mathsf T}$. $R = R_z(\theta)$ fixes $e_0$ and is orthogonal on space, so $RE_{10}R^{-1} = (Re_1)(R^{-\mathsf T}e_0)^{\mathsf T} = (Re_1)e_0^{\mathsf T}$ and $RE_{01}R^{-1} = e_0(Re_1)^{\mathsf T}$, with $Re_1 = \cos\theta\,e_1 + \sin\theta\,e_2$. Hence $RK_1R^{-1} = \cos\theta\,K_1 + \sin\theta\,K_2$.
>
> **Step 2** (exponentiate). $Re^{X}R^{-1} = e^{RXR^{-1}}$ (term by term in the series), so $RB_x(\eta)R^{-1} = e^{-i\eta(\cos\theta K_1 + \sin\theta K_2)}$, the boost along $\hat{\mathbf n}$ of Theorem §C1a.6.7, 2.
>
> **Step 3** (first order). $R \approx \mathbb 1 - i\theta J_3$: $RK_1R^{-1} \approx K_1 - i\theta[J_3, K_1] = K_1 - i\theta(i\varepsilon_{312}K_2) = K_1 + \theta K_2$, the first-order term of Step 1. $[J_i, K_j] = i\varepsilon_{ijk}K_k$ says exactly that $\mathbf K$ turns like a vector under rotations.
>
> *Derived here; check:* the result is the boost of [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], 2 with $\hat{\mathbf n} = (\cos\theta, \sin\theta, 0)$ (checked numerically at $\theta = 0.7$, $\eta = 0.9$); the commutator is [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]].

^sol-wr-15-c

## Problem 16. Two boosts make a rotation

![[PHY 513 Worksheet — Relativity#^wr-16]]

### (a) The product

![[PHY 513 Worksheet — Relativity#^wr-16-a]]

> [!success]- Solution
> **Answer.**
> $$\Lambda = B_y(\eta_2)B_x(\eta_1) = \frac1{12}\begin{pmatrix}25&15&16&0\\9&15&0&0\\20&12&20&0\\0&0&0&12\end{pmatrix},$$
> a Lorentz transformation, not symmetric, hence not a pure boost.
>
> **Step 1** (the factors). $\tanh\eta_1 = \frac35$: $\cosh\eta_1 = \frac54$, $\sinh\eta_1 = \frac34$. $\tanh\eta_2 = \frac45$: $\cosh\eta_2 = \frac53$, $\sinh\eta_2 = \frac43$.
>
> **Step 2** (multiply). Row $0$ of $B_y$ is $(\frac53, 0, \frac43, 0)$: against the columns of $B_x$ it gives $(\frac53\cdot\frac54, \frac53\cdot\frac34, \frac43, 0) = (\frac{25}{12}, \frac{15}{12}, \frac{16}{12}, 0)$. Row $1$ of $B_y$ is $e_1^{\mathsf T}$: $(\frac34, \frac54, 0, 0)$. Row $2$ is $(\frac43, 0, \frac53, 0)$: $(\frac{20}{12}, \frac{12}{12}, \frac{20}{12}, 0)$.
>
> **Step 3** (Lorentz). A product of Lorentz matrices is one; directly, column $0$: $(25^2 - 9^2 - 20^2)/144 = 1$, columns $0$ and $1$: $(25\cdot15 - 9\cdot15 - 20\cdot12)/144 = 0$.
>
> **Step 4** (not a boost). Every pure boost is symmetric (Theorem §C1a.6.7, 2), but $\Lambda^0{}_1 = \frac{15}{12} \ne \Lambda^1{}_0 = \frac9{12}$. In the opposite order the product is $B_xB_y = \Lambda^{\mathsf T}$ (both factors symmetric), a different transformation: boosts in different directions do not commute.
>
> *Checked against:* [[§B1.2 Lorentz Transformations and the Lorentz Group#^ex-b1-2-2|REL Example §B1.2.2]] (the same speeds $0.6$ and $0.8$, passive reading); [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-7|Theorem §C1a.6.7]], 2 (boosts are symmetric); exact check with sympy.

^sol-wr-16-a

### (b) Boost times rotation: the Wigner rotation

![[PHY 513 Worksheet — Relativity#^wr-16-b]]

> [!success]- Solution
> **Answer.** $u = \Lambda e_0 = (\frac{25}{12}, \frac34, \frac53, 0)$: $\gamma = \frac{25}{12} = \gamma_1\gamma_2$, velocity $\boldsymbol\beta = (0.36, 0.80, 0)$, speed $0.877$. $R = R_z(\theta_W)$ with $\cos\theta_W = \frac{35}{37}$, $\sin\theta_W = \frac{12}{37}$: a rotation by $\theta_W = \arctan\frac{12}{35} = 18.9^\circ$ about $+z$. The boost part has rapidity $\operatorname{arcosh}\frac{25}{12} = 1.364 < \eta_1 + \eta_2 = 0.693 + 1.099 = 1.792$.
>
> **Step 1** (the boost part). $u$ is the first column of $\Lambda$; $\gamma = u^0 = \frac{25}{12}$, $\boldsymbol\beta = \mathbf u/u^0 = (\frac{9}{25}, \frac{20}{25}, 0)$.
>
> **Step 2** ($B(u)$). $B(u) = \begin{pmatrix}\gamma & \mathbf u^{\mathsf T}\\ \mathbf u & \mathbb 1_3 + \mathbf u\mathbf u^{\mathsf T}/(1 + \gamma)\end{pmatrix}$ with $1 + \gamma = \frac{37}{12}$; its inverse is $B(-u)$.
>
> **Step 3** ($R = B(-u)\Lambda$). It fixes $e_0$ ($B(-u)u = e_0$), so $R = \operatorname{diag}(1, O)$. One entry by hand: $O_{11} = -u^1\Lambda^0{}_1 + \bigl(1 + \frac{(u^1)^2}{1 + \gamma}\bigr)\Lambda^1{}_1 + \frac{u^1u^2}{1 + \gamma}\Lambda^2{}_1 = -\frac34\cdot\frac{15}{12} + \bigl(1 + \frac{9}{16}\cdot\frac{12}{37}\bigr)\frac{15}{12} + \frac{15}{12}\cdot\frac{12}{37}\cdot1 = \frac{35}{37}$. All of them (exact): $O = \frac1{37}\begin{pmatrix}35&-12&0\\12&35&0\\0&0&37\end{pmatrix}$, the active $R_z(\theta_W)$.
>
> **Step 4** (meaning). Two boosts in different directions compose to a boost times a rotation about the axis perpendicular to both (the Wigner rotation; along a curved path it accumulates into Thomas precession). Rapidities do not add: the boost part is slower than $\tanh(\eta_1 + \eta_2) = 0.946$.
>
> *Checked against:* [[§B1.2 Lorentz Transformations and the Lorentz Group#^ex-b1-2-2|REL Example §B1.2.2]] (the same $\gamma = \gamma_1\gamma_2 = \frac{25}{12}$, the same $R$ with $\frac{35}{37}$, $\frac{12}{37}$ and $18.9^\circ$, boost rapidity $1.36 < 1.79$; there in the passive reading, whose matrices are $\mathcal P\Lambda\mathcal P$: same $R$, opposite $\mathbf u$); [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-13|Theorem §CB.3.13]], 1 ($\Lambda = B(u)R$, the formula for $B(u)$); exact check with sympy.

^sol-wr-16-b

### (c) The infinitesimal version

![[PHY 513 Worksheet — Relativity#^wr-16-c]]

> [!success]- Solution
> **Answer.** $B_x(a)B_y(b)B_x(-a)B_y(-b) = \mathbb 1 + [A, B] + O(3)$ with $A = -iaK_1$, $B = -ibK_2$, and $[A, B] = -ab[K_1, K_2] = -ab(-iJ_3) = iab\,J_3$: since $R_z(\theta) = \mathbb 1 - i\theta J_3 + \dots$, this is a rotation by $\theta = -ab$ about $z$. The commutator responsible is $[K_1, K_2] = -iJ_3$. In $SO(4)$, $[\tilde K_i, \tilde K_j] = +i\varepsilon_{ijk}J_k$ and the rotation would be by $+ab$.
>
> **Step 1** (second order). Write the four factors as $e^{X_i} = \mathbb 1 + X_i + \frac12X_i^2 + O(3)$ with $(X_1, X_2, X_3, X_4) = (A, B, -A, -B)$. First order: $\sum_iX_i = 0$. Second order: $\frac12\sum_iX_i^2 + \sum_{i<j}X_iX_j = (A^2 + B^2) + (AB - A^2 - AB - BA - B^2 + AB) = AB - BA$. So the product is $\mathbb 1 + [A, B] + O(3)$.
>
> **Step 2.** $B_x(a) = e^{-iaK_1}$, $B_y(b) = e^{-ibK_2}$, and $[K_1, K_2] = -iJ_3$ give $[A, B] = (-i)^2ab(-iJ_3) = iab\,J_3$. In matrices, $iabJ_3 = ab(E_{12} - E_{21})$, while $R_z(\theta) - \mathbb 1 \approx \theta(E_{21} - E_{12})$: $\theta = -ab$.
>
> **Step 3** (the sign). The minus in $[K_i, K_j] = -i\varepsilon_{ijk}J_k$ comes from $g^{00} = +1$ against $g^{ii} = -1$; in Euclidean four dimensions the same computation gives $+i\varepsilon_{ijk}J_k$. This sign is the whole difference between $SO^+(1,3)$ and $SO(4)$.
>
> *Checked against:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-1|§C3.2, Remark: Two boosts make a rotation]]; [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]] ($[K_i, K_j] = -i\varepsilon_{ijk}J_k$); [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-4|Theorem §CB.6.4]] ($SO(4)$ sign); numerical check at $a = 10^{-3}$, $b = 2\cdot10^{-3}$.

^sol-wr-16-c

## Problem 17. The four-vector is (½, ½)

![[PHY 513 Worksheet — Relativity#^wr-17]]

### (a) Casimirs

![[PHY 513 Worksheet — Relativity#^wr-17-a]]

> [!success]- Solution
> **Answer.** $\mathbf J^2 = \operatorname{diag}(0, 2, 2, 2)$, $\mathbf K^2 = -\operatorname{diag}(3, 1, 1, 1)$, $\mathbf J\cdot\mathbf K = 0$; $\mathbf J_+^2 = \mathbf J_-^2 = \frac34\mathbb 1 = \frac12(\frac12 + 1)\mathbb 1$: $(j_+, j_-) = (\frac12, \frac12)$.
>
> **Step 1** ($\mathbf J^2$). $J_k$ acts on the spatial block as $(J_k)^l{}_m = -i\varepsilon_{klm}$; $J_k^2$ is the projector onto the two spatial directions perpendicular to $k$ (e.g. $J_3^2 = E_{11} + E_{22}$). Summing, each spatial direction is counted twice and $e_0$ never: $\operatorname{diag}(0, 2, 2, 2)$.
>
> **Step 2** ($\mathbf K^2$). $K_k = i(E_{0k} + E_{k0})$, $K_k^2 = -(E_{00} + E_{kk})$; summing over $k$: $-(3E_{00} + E_{11} + E_{22} + E_{33})$.
>
> **Step 3** ($\mathbf J\cdot\mathbf K$). $K_k$ maps $e_0 \mapsto ie_k$ and $e_k \mapsto ie_0$, and $J_k$ kills both $e_0$ and $e_k$; so $J_kK_k = 0$ and likewise $K_kJ_k = 0$.
>
> **Step 4.** $\mathbf J_\pm^2 = \frac14\sum_k(J_k \pm iK_k)^2 = \frac14\bigl(\mathbf J^2 - \mathbf K^2 \pm i(\mathbf J\cdot\mathbf K + \mathbf K\cdot\mathbf J)\bigr) = \frac14\bigl(\operatorname{diag}(0, 2, 2, 2) + \operatorname{diag}(3, 1, 1, 1)\bigr) = \frac34\mathbb 1$.
>
> *Checked against:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-2|Theorem §C3.2.2]] (all five values); numerical check.

^sol-wr-17-a

### (b) Weights

![[PHY 513 Worksheet — Relativity#^wr-17-b]]

> [!success]- Solution
> **Answer.**
>
> | vector | $J_3$ | $K_3$ | $(m_+, m_-)$ | factor under $B_z(\eta)$ |
> |---|---|---|---|---|
> | $e_1 + ie_2$ | $+1$ | $0$ | $(\frac12, \frac12)$ | $1$ |
> | $e_1 - ie_2$ | $-1$ | $0$ | $(-\frac12, -\frac12)$ | $1$ |
> | $e_0 + e_3$ | $0$ | $+i$ | $(-\frac12, \frac12)$ | $e^{\eta}$ |
> | $e_0 - e_3$ | $0$ | $-i$ | $(\frac12, -\frac12)$ | $e^{-\eta}$ |
>
> **Step 1** (eigenvalues). $J_3e_1 = ie_2$, $J_3e_2 = -ie_1$, so $J_3(e_1 \pm ie_2) = ie_2 \pm e_1 = \pm(e_1 \pm ie_2)$; $J_3e_0 = J_3e_3 = 0$. $K_3e_0 = ie_3$, $K_3e_3 = ie_0$, so $K_3(e_0 \pm e_3) = \pm i(e_0 \pm e_3)$; $K_3e_1 = K_3e_2 = 0$.
>
> **Step 2** (labels). Solve $m_+ + m_- = J_3$, $m_+ - m_- = iK_3$: e.g. $e_0 + e_3$: $m_+ + m_- = 0$, $m_+ - m_- = i\cdot i = -1$, so $(m_+, m_-) = (-\frac12, \frac12)$.
>
> **Step 3** (boost). $B_z(\eta) = e^{-i\eta K_3}$ multiplies a $K_3$-eigenvector by $e^{-i\eta K_3}$, i.e. $e^{-\eta(m_+ - m_-)}$: $e^{\eta}$ on $e_0 + e_3$, $e^{-\eta}$ on $e_0 - e_3$, $1$ on $e_1 \pm ie_2$ (part 2(b) again).
>
> *Checked against:* [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-5|Theorem §C1a.6.5]] (eigenvectors of $J_3$, $K_3$, step 5 of its derivation), [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-10|Theorem §CB.6.10]] (rotation weight $m_+ + m_-$, boost factor $e^{-\eta(m_+ - m_-)}$), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^ex-c3-2-1|Example §C3.2.1]] (the same weights, read on the components: $A^0 - A^3$, the coefficient of $e_0 - e_3$, has $(\frac12, -\frac12)$ and factor $e^{-\eta}$); numerical check.

^sol-wr-17-b

### (c) Dimensions, spins, signs

![[PHY 513 Worksheet — Relativity#^wr-17-c]]

> [!success]- Solution
> **Answer.**
>
> | $(j_+, j_-)$ | dimension | spins | $2\pi$ rotation | field |
> |---|---|---|---|---|
> | $(\frac12, \frac12)$ | $4$ | $0\oplus1$ | $+1$ | $A^\mu$, $\partial_\mu\phi$ |
> | $(1, 0)\oplus(0, 1)$ | $3 + 3$ | $1\oplus1$ | $+1$ | $F^{\mu\nu}$, as $\mathbf E \mp i\mathbf B$ |
> | $(1, 1)$ | $9$ | $0\oplus1\oplus2$ | $+1$ | symmetric traceless tensor |
> | $(1, \frac12)$ | $6$ | $\frac12\oplus\frac32$ | $-1$ | none in the course |
>
> **Rules.** Dimension $(2j_+ + 1)(2j_- + 1)$; under rotations $(j_+, j_-)$ is $j_+\otimes j_-$, containing each spin from $\lvert j_+ - j_-\rvert$ to $j_+ + j_-$ once; a $2\pi$ rotation gives $(-1)^{2(j_+ + j_-)}$. For $(1, \frac12)$: $3\cdot2 = 6$, spins $\frac12$ and $\frac32$, sign $(-1)^3 = -1$ (it occurs inside a vector-spinor $\psi_\mu$, beyond the course).
>
> *Checked against:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]] (the first three rows), [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|Theorem §CB.17.9]] (spins and sign); the $(1, \frac12)$ row is derived here from the same rules; check: its dimension $6 = 2 + 4$ is the sum of the spin multiplicities.

^sol-wr-17-c

### (d) The vector is not (1, 0) ⊕ (0, 0)

![[PHY 513 Worksheet — Relativity#^wr-17-d]]

> [!success]- Solution
> **Answer.** Two tests. (i) **Boost weights:** on the vector, the $J_3 = 0$ eigenvectors $e_0 \pm e_3$ have $K_3 = \pm i$ (a boost along $z$ mixes $t$ with $z$ and leaves $x$, $y$ alone), while on $(1, 0)\oplus(0, 0)$ the joint eigenvalues $(J_3, K_3)$ are $(\pm1, \mp i)$, $(0, 0)$, $(0, 0)$: the boost leaves the $m = 0$ components alone and rescales the $m = \pm1$ ones. (ii) **Complex conjugation:** the vector representation is real, so equivalent to its conjugate, while the conjugate of $(1, 0)\oplus(0, 0)$ is $(0, 1)\oplus(0, 0)$, not equivalent to it.
>
> **Step 1** (weights on $(1, 0)$). $\mathbf J_- = 0$, so $m_- = 0$ and $K_3 = -i(m_+ - 0) = -im_+$ with $m_+ \in \{1, 0, -1\}$, $J_3 = m_+$; on $(0, 0)$ everything vanishes.
>
> *Checked against:* [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^thm-c3-2-4|Theorem §C3.2.4]] (both tests), [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-10|Theorem §CB.6.10]].

^sol-wr-17-d

## Problem 18. Two-index tensors; the field strength is (1, 0) ⊕ (0, 1)

![[PHY 513 Worksheet — Relativity#^wr-18]]

### (a) The three invariant pieces

![[PHY 513 Worksheet — Relativity#^wr-18-a]]

> [!success]- Solution
> **Answer.** $16 = 9 + 6 + 1$: symmetric traceless $(1, 1)$, antisymmetric $(1, 0)\oplus(0, 1)$, trace $(0, 0)$; and $(\frac12, \frac12)\otimes(\frac12, \frac12) = (1\oplus0, 1\oplus0) = (1, 1)\oplus(1, 0)\oplus(0, 1)\oplus(0, 0)$, dimensions $9 + 3 + 3 + 1$.
>
> **Step 1** (symmetry is kept). If $T^{\alpha\beta} = \pm T^{\beta\alpha}$, then $T'^{\nu\mu} = \Lambda^\nu{}_\alpha\Lambda^\mu{}_\beta T^{\alpha\beta} = \Lambda^\mu{}_\beta\Lambda^\nu{}_\alpha(\pm T^{\beta\alpha}) = \pm T'^{\mu\nu}$ (rename $\alpha \leftrightarrow \beta$).
>
> **Step 2** (the trace is invariant). $g_{\mu\nu}T'^{\mu\nu} = g_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta T^{\alpha\beta} = g_{\alpha\beta}T^{\alpha\beta}$ by the Lorentz condition, so traceless stays traceless; and the pure-trace part $\frac14g^{\mu\nu}T^\rho{}_\rho$ goes to $\frac14\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta g^{\alpha\beta}T^\rho{}_\rho = \frac14g^{\mu\nu}T^\rho{}_\rho$, since $\Lambda g\Lambda^{\mathsf T} = g$.
>
> **Step 3** (count). Symmetric: $10 = 9 + 1$; antisymmetric: $6$. Labels: each slot of $(\frac12, \frac12)\otimes(\frac12, \frac12)$ is a product of two spins $\frac12$, i.e. $1\oplus0$ (Clebsch–Gordan), slot by slot; the $(1, 1)$ is the $9$, $(1, 0)\oplus(0, 1)$ the $6$, $(0, 0)$ the trace.
>
> *Checked against:* [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]] (the decomposition is preserved), [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]] (the labels); the user's Lorentz-representation review (2026-10-14), §8 (Two-index tensors) and §10 (Exam summary).

^sol-wr-18-a

### (b) The infinitesimal boost of E and B

![[PHY 513 Worksheet — Relativity#^wr-18-b]]

> [!success]- Solution
> **Answer.** $\delta\mathbf E = -\eta\,\hat{\mathbf x}\times\mathbf B = (0, \eta B_z, -\eta B_y)$, $\delta\mathbf B = \eta\,\hat{\mathbf x}\times\mathbf E = (0, -\eta E_z, \eta E_y)$: the first-order terms of Problem 11(b) ($\gamma \approx 1$, $\gamma v \approx \eta$).
>
> **Step 1** (mixed $\omega$). $\omega^0{}_1 = g^{00}\omega_{01} = \eta$, $\omega^1{}_0 = g^{11}\omega_{10} = (-1)(-\eta) = \eta$, all others zero.
>
> **Step 2** ($\delta\mathbf E$, $E^i = F^{i0}$). $\delta F^{i0} = \omega^i{}_\alpha F^{\alpha0} + \omega^0{}_\beta F^{i\beta} = \omega^i{}_0F^{00} + \eta F^{i1} = \eta F^{i1}$. So $\delta E_x = \eta F^{11} = 0$, $\delta E_y = \eta F^{21} = \eta B_z$, $\delta E_z = \eta F^{31} = -\eta B_y$.
>
> **Step 3** ($\delta\mathbf B$). $\delta F^{23} = 0$ (no $\omega$ touches $2$, $3$): $\delta B_x = 0$. $\delta F^{31} = \omega^1{}_0F^{30} = \eta E_z$, so $\delta B_y = -\delta F^{31} = -\eta E_z$. $\delta F^{12} = \omega^1{}_0F^{02} = -\eta E_y$, so $\delta B_z = -\delta F^{12} = \eta E_y$.
>
> **Step 4** (compare). Problem 11(b) to first order: $E'_y = E_y + \eta B_z$, $E'_z = E_z - \eta B_y$, $B'_y = B_y - \eta E_z$, $B'_z = B_z + \eta E_y$: the same.
>
> *Checked against:* [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]] ($\delta\mathbf E = \boldsymbol\theta\times\mathbf E - \boldsymbol\eta\times\mathbf B$, $\delta\mathbf B = \boldsymbol\theta\times\mathbf B + \boldsymbol\eta\times\mathbf E$ with $\boldsymbol\eta = \eta\hat{\mathbf x}$); numerical check.

^sol-wr-18-b

### (c) E − iB carries (1, 0)

![[PHY 513 Worksheet — Relativity#^wr-18-c]]

> [!success]- Solution
> **Answer.** $\mathbf E - i\mathbf B$ carries $(1, 0)$ and $\mathbf E + i\mathbf B$ carries $(0, 1)$ (with $K_i = \mathcal J^{0i}$ and $F^{ij} = -\varepsilon_{ijk}B^k$). For real $F$ the two are complex conjugates of each other, so a real field contains both; $(1, 0)$ alone would be a complex field.
>
> **Step 1.** $-i\eta\,\hat{\mathbf x}\times(\mathbf E - i\mathbf B) = -\eta\,\hat{\mathbf x}\times\mathbf B - i\,\eta\,\hat{\mathbf x}\times\mathbf E = \delta\mathbf E - i\,\delta\mathbf B$ by (b), using $(-i)(-i) = -1$. Likewise $+i\eta\,\hat{\mathbf x}\times(\mathbf E + i\mathbf B) = -\eta\,\hat{\mathbf x}\times\mathbf B + i\,\eta\,\hat{\mathbf x}\times\mathbf E = \delta\mathbf E + i\,\delta\mathbf B$.
>
> **Step 2** (which label). A Lorentz transformation acts as $e^{-i(\boldsymbol\theta - i\boldsymbol\eta)\cdot\mathbf J_+}e^{-i(\boldsymbol\theta + i\boldsymbol\eta)\cdot\mathbf J_-}$; on $(1, 0)$ only the first factor acts, a rotation of a three-vector by the complex angle $\boldsymbol\theta - i\boldsymbol\eta$, infinitesimally $\delta\mathbf v = (\boldsymbol\theta - i\boldsymbol\eta)\times\mathbf v$. That is the law of $\mathbf E - i\mathbf B$.
>
> **Step 3** (reality). Complex conjugation turns $\boldsymbol\theta - i\boldsymbol\eta$ into $\boldsymbol\theta + i\boldsymbol\eta$, i.e. $(1, 0)$ into $(0, 1)$, and $\mathbf E - i\mathbf B$ into $\mathbf E + i\mathbf B$; parity ($\mathbf E \to -\mathbf E$, $\mathbf B \to \mathbf B$) also exchanges them. A real six-component $F$ is therefore $(1, 0)\oplus(0, 1)$.
>
> *Checked against:* [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-7|Theorem §C3.3.7]], [[§C3.3 How Fields Transform under the Lorentz Group#^cau-c3-3-1|§C3.3, Caution: Which half of F is called (1, 0)]], [[§CB.6 The Lorentz Algebra꞉ the Split J±, Real Forms and 𝔰𝔩(2,ℂ) as a Real Lie Algebra#^thm-cb-6-3|Theorem §CB.6.3]] (the factorization), [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^ex-c3-2-2|Example §C3.2.2]] (on $(1, 0)$ a boost is a rotation by an imaginary angle; the field is $\mathbf E - i\mathbf B$); numerical check of $\delta(\mathbf E - i\mathbf B)$.

^sol-wr-18-c

## Problem 19. Orbital generators and how fields transform

![[PHY 513 Worksheet — Relativity#^wr-19]]

### (a) The orbital boost generator

![[PHY 513 Worksheet — Relativity#^wr-19-a]]

> [!success]- Solution
> **Answer.** $\phi(\Lambda^{-1}x) = \phi(x) - \eta(t\,\partial_z + z\,\partial_t)\phi(x) + O(\eta^2) = (1 - i\eta L^{03})\phi$ with $L^{03} = -i(t\,\partial_z + z\,\partial_t)$.
>
> **Step 1** (the inverse to first order). $\Lambda = \mathbb 1 + \omega + O(\omega^2)$ with $\omega^0{}_3 = g^{00}\omega_{03} = \eta$, $\omega^3{}_0 = g^{33}\omega_{30} = \eta$; so $\Lambda^{-1}x = x - \omega x$: $(\Lambda^{-1}x)^0 = t - \eta z$, $(\Lambda^{-1}x)^3 = z - \eta t$.
>
> **Step 2** (Taylor). $\phi(t - \eta z, x, y, z - \eta t) = \phi - \eta z\,\partial_t\phi - \eta t\,\partial_z\phi$.
>
> **Step 3** (match). $-\frac i2\omega_{\mu\nu}L^{\mu\nu} = -\frac i2(\eta L^{03} + (-\eta)L^{30}) = -i\eta L^{03}$, so $-i\eta L^{03} = -\eta(t\,\partial_z + z\,\partial_t)$. From the formula: $L^{03} = i(x^0\partial^3 - x^3\partial^0) = i(-t\,\partial_z - z\,\partial_t)$, the same.
>
> *Checked against:* [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-1|Theorem §C3.3.1]], 1–2 ($L^{0i} = -i(t\,\partial_i + x^i\partial_t)$), [[§C3.3 How Fields Transform under the Lorentz Group#^def-c3-3-1|Def. §C3.3.1]].

^sol-wr-19-a

### (b) The gradient is a covector field

![[PHY 513 Worksheet — Relativity#^wr-19-b]]

> [!success]- Solution
> **Answer.** $\partial_\mu\phi'(x) = (\Lambda^{-1})^\nu{}_\mu(\partial_\nu\phi)(\Lambda^{-1}x) = \Lambda_\mu{}^\nu(\partial_\nu\phi)(\Lambda^{-1}x)$, and $\partial_\mu\phi'\,\partial^\mu\phi'(x) = (\partial_\nu\phi\,\partial^\nu\phi)(\Lambda^{-1}x)$: a scalar field.
>
> **Step 1** (chain rule). With $y^\nu = (\Lambda^{-1})^\nu{}_\mu x^\mu$, $\partial y^\nu/\partial x^\mu = (\Lambda^{-1})^\nu{}_\mu$, so $\partial_\mu[\phi(y(x))] = (\Lambda^{-1})^\nu{}_\mu(\partial_\nu\phi)(y)$, and $(\Lambda^{-1})^\nu{}_\mu = \Lambda_\mu{}^\nu$ (Problem 1(b)).
>
> **Step 2** (contract). $g^{\mu\rho}\Lambda_\mu{}^\nu\Lambda_\rho{}^\sigma = (\Lambda^{-1}g^{-1}\Lambda^{-\mathsf T})^{\nu\sigma} = g^{\nu\sigma}$, because $\Lambda^{-1}$ is a Lorentz transformation. So $\partial_\mu\phi'\,\partial^\mu\phi'(x) = g^{\nu\sigma}(\partial_\nu\phi\,\partial_\sigma\phi)(\Lambda^{-1}x)$, the law of a scalar field.
>
> *Checked against:* [[§C3.3 How Fields Transform under the Lorentz Group#^ex-c3-3-1|Example §C3.3.1]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]], 2; [[§B1.2 Lorentz Transformations and the Lorentz Group#^thm-b1-2-3|REL Theorem §B1.2.3]], 2–4.

^sol-wr-19-b

### (c) Orbital plus spin

![[PHY 513 Worksheet — Relativity#^wr-19-c]]

> [!success]- Solution
> **Answer.** $A'^\alpha(x) = A^\alpha(x) - \frac i2\omega_{\mu\nu}\bigl(L^{\mu\nu}A^\alpha(x) + (\mathcal J^{\mu\nu})^\alpha{}_\beta A^\beta(x)\bigr) + O(\omega^2)$.
>
> **Step 1** (index factor). $\Lambda^\alpha{}_\beta = \delta^\alpha{}_\beta + \omega^\alpha{}_\beta + O(\omega^2)$, and the generators reproduce $\omega$: $\omega^\alpha{}_\beta = -\frac i2\omega_{\mu\nu}(\mathcal J^{\mu\nu})^\alpha{}_\beta$.
>
> **Step 2** (argument). $A^\beta(\Lambda^{-1}x) = A^\beta(x) - \frac i2\omega_{\mu\nu}L^{\mu\nu}A^\beta(x) + O(\omega^2)$, by the same Taylor step as (a) for each component.
>
> **Step 3** (product). $\Lambda^\alpha{}_\beta A^\beta(\Lambda^{-1}x) = \bigl(\delta^\alpha{}_\beta - \frac i2\omega_{\mu\nu}(\mathcal J^{\mu\nu})^\alpha{}_\beta\bigr)\bigl(A^\beta - \frac i2\omega_{\rho\sigma}L^{\rho\sigma}A^\beta\bigr)$; keep first order: $A^\alpha - \frac i2\omega_{\mu\nu}\bigl((\mathcal J^{\mu\nu})^\alpha{}_\beta A^\beta + L^{\mu\nu}A^\alpha\bigr)$. The orbital part moves the argument, the spin part mixes the components; under rotations their sum is $\mathbf L + \mathbf J$.
>
> *Checked against:* [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-5|Theorem §C3.3.5]], 1 (the formula), [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-3|Theorem §C3.3.3]] (orbital plus spin), [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-2|Theorem §C1a.6.2]] (the generators reproduce $\omega$), [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-1|Theorem §C3.3.1]], 1.

^sol-wr-19-c

# Short response

## Problem 20. Short response

![[PHY 513 Worksheet — Relativity#^wr-20]]

![[PHY 513 Worksheet — Relativity#^wr-20-a]]

> [!success]- Answers
> 1. (a) $\varepsilon^{1023} = -1$ (one transposition); $\varepsilon_{3210} = -\varepsilon^{3210} = -1$ (six inversions, then the lowering sign). [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]].
> 2. (b) $2m_e^2 + 2m_\mu^2$. [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-1|Theorem §C1a.5.1]], 1.
> 3. (c) $[\delta^4(p)] = -4$, $[\partial/\partial p^\mu] = -1$. [[§C1a.2 Natural Units and Dimensional Analysis#^thm-c1a-2-3|Theorem §C1a.2.3]], 4.
> 4. (d) $\Box(x^2)^2 = 24x^2$. [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-8|Theorem §C1a.5.8]] ($\partial^2\rho^2 = 24\rho$).
> 5. (e) $y = \frac12\ln\frac{13 + 12}{13 - 12} = \ln5 \approx 1.609$. Problem 2(c) (derived there).
> 6. (f) $[K_3, J_1] = -[J_1, K_3] = -i\varepsilon_{13k}K_k = -i\varepsilon_{132}K_2 = iK_2$. [[§CB.5 The Lorentz Algebra꞉ Generators and Commutation Relations#^thm-cb-5-6|Theorem §CB.5.6]]; numerical check.
> 7. (g) The proper non-orthochronous component ($\det = +1$, $\Lambda^0{}_0 = -1$), $\mathcal P\mathcal T\cdot SO^+(1,3)$; no, every exponential lies in $SO^+(1,3)$. [[§CB.3 Homomorphisms, Representations, the Identity Component and Coverings#^thm-cb-3-12|Theorem §CB.3.12]], [[§C1a.6 Infinitesimal Lorentz Transformations and Generators#^thm-c1a-6-4|Theorem §C1a.6.4]].
> 8. (h) $(\frac12, \frac12)$; $(0, 0)$; $(1, 1)$. [[§C3.2 The Lorentz Algebra and the Representations (j₊, j₋) of Fields#^rem-c3-2-3|§C3.2, Remark: The representations met in the course]], [[§C3.3 How Fields Transform under the Lorentz Group#^thm-c3-3-6|Theorem §C3.3.6]].
> 9. (i) Both zero: a plane wave is a null field ($\mathbf E\perp\mathbf B$, $\lvert\mathbf E\rvert = \lvert\mathbf B\rvert$). [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-4|REL Theorem §B4.2.4]], 3; [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-2|Theorem §C1a.7.2]].
> 10. (j) $+1$; $e^{\eta}$. [[§CB.17 The Lorentz Case II꞉ the Representations (j₊, j₋)#^thm-cb-17-9|Theorem §CB.17.9]]; Problem 2(b), Problem 17(b).

^sol-wr-20
