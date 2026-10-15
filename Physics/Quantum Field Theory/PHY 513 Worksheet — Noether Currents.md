---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Noether Currents (Solutions)|Solutions]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Worksheet — Noether Currents

Eighteen problems on one technique: find the Noether current and charge of a continuous transformation, or show that the transformation is not a symmetry and find the divergence of the would-be current. The four fields of the course in order (real scalar, complex scalar, Dirac, vector), and for each the symmetries in the order of Lecture 3 and of [[§C1b.5 Noether's Theorem|§C1b.5]]–[[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor|§C1b.8]]: internal symmetries, translations, Lorentz transformations; the last problem is a short-response check of signs and normalizations. The grey line under each part says where it comes from: *[HW-literal …]* a homework part as it stood, *[variation of …]* the same computation on an object the homework or Peskin–Schroeder does not work out, *[extension of …]* one step further, *[new]* not in the homework. ★ marks material beyond the lectures (dilatations, Proca, gauge dependence of the spin). Solutions, folded: [[PHY 513 Worksheet — Noether Currents (Solutions)]]. Printable copies: `~/Downloads/PHY513_worksheet_noether.pdf` (questions, no tags) and `~/Downloads/PHY513_worksheet_noether_solutions.pdf`.

**Conventions** (the course's, [[Larsen PHY 513]]; the recipe is [[P3 Noether's Procedure]]): $g = \mathrm{diag}(+1,-1,-1,-1)$, $\hbar = c = 1$, $\varepsilon^{0123} = +1$. A transformation with constant parameter $\alpha$ acts at a fixed point as $\delta\phi_i = \alpha\Delta\phi_i$; it is a symmetry if $\delta\mathcal L = \alpha\,\partial_\mu\mathcal J^\mu$ for every configuration; the Noether current is $j^\mu = \sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Delta\phi_i - \mathcal J^\mu$, summed over every independent field ($\phi$ and $\phi^{\ast}$; $\psi$ and $\bar\psi$), and the charge is $Q = \int d^3x\,j^0$. Translations $x \to x - a$: $\phi(x) \to \phi(x + a)$, $\Delta_\nu\phi = \partial_\nu\phi$, $T^\mu{}_\nu = \sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\partial_\nu\phi_i - \delta^\mu{}_\nu\mathcal L$, $P^\nu = \int d^3x\,T^{0\nu}$. Lorentz transformations $\Lambda = 1 + \omega$ with parameters entering as $\frac12\omega_{\nu\rho}$; field law $\phi'_a(x') = D_a{}^b\phi_b(x)$, $D = 1 + \frac12\omega_{\mu\nu}S^{\mu\nu}$; charges $J^{\nu\rho} = \int d^3x\,\mathcal M^{0\nu\rho}$, $J^i = \frac12\varepsilon_{ijk}J^{jk}$, Noether boost charge $K^i \equiv J^{i0}$. Vector field: $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, $F^{0i} = -E^i$, $F^{ij} = -\varepsilon_{ijk}B^k$ (Heaviside–Lorentz). Dirac field: $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ with classical commuting components, chiral basis, $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \mathrm{diag}(-\mathbb 1, \mathbb 1)$, $P_{L,R} = \frac12(\mathbb 1 \mp \gamma^5)$, $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, $\Lambda_{1/2} = \exp(-\frac i2\omega_{\mu\nu}S^{\mu\nu})$; bilinears $\mathsf V^\mu = \bar\psi\gamma^\mu\psi$, $\mathsf A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$, $\mathsf P = \bar\psi\,i\gamma^5\psi$.

---

## The real scalar field

### W1. Shift symmetries

Take $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ and shifts of the field by a constant parameter $\alpha$.

^wn-1

(a) Let $m = 0$ and $\phi \to \phi + \alpha$. Find $\Delta\phi$, $\mathcal J^\mu$, the Noether current and its charge, and show that conservation of the current is the field equation.
*[variation of Lecture 3, Example 1]*

^wn-1-a

(b) Now $m \neq 0$. Compute $\delta\mathcal L$ to first order. Is it a total derivative? Find $\partial_\mu$ of the current of (a) on solutions and compare it with $\delta\mathcal L/\alpha$.
*[extension of Lecture 3, Example 1]*

^wn-1-b

(c) Let $m = 0$ and $\phi \to \phi + \alpha\,c_\mu x^\mu$, a shift growing linearly in $x$ ($c^\mu$ a fixed constant four-vector). Show that $\mathcal L$ changes by a total derivative, read off $\mathcal J^\mu$, find the current, and check that it is conserved on solutions. What is the charge for $c^\mu = (1, 0, 0, 0)$, and what does its conservation say? Is the transformation a symmetry for $m \neq 0$?
*[new]*

^wn-1-c

### W2. Rotations of N real fields

Take $N$ real fields with $\mathcal L = \frac12\partial_\mu\phi_i\,\partial^\mu\phi_i - V(\phi_i\phi_i)$ (summed over $i = 1, \dots, N$; $V$ smooth).

^wn-2

(a) For the rotation by an angle $\alpha$ in the $(a, b)$ plane, $\phi_a \to \cos\alpha\,\phi_a - \sin\alpha\,\phi_b$, $\phi_b \to \sin\alpha\,\phi_a + \cos\alpha\,\phi_b$, all other fields fixed: find the generators, show $\delta\mathcal L = 0$, and find the Noether current $j^\mu_{ab}$ and its charge. How many independent conserved currents does the theory have?
*[extension of PS2.3(c)–(d)]*

^wn-2-a

(b) Add $h\,\phi_N$ to $\mathcal L$ ($h$ a constant). Which rotations remain symmetries? For the rotation in the $(a, N)$ plane, $a < N$, find $\partial_\mu j^\mu_{aN}$ on solutions in two ways: from $\delta\mathcal L$ and from the field equations.
*[extension of PS2.3(c)–(d)]*

^wn-2-b

### W3. Translations: the real scalar's energy and momentum

Take $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - V(\phi)$.

^wn-3

(a) For $x \to x - a$, i.e. $\phi(x) \to \phi(x + a)$, find $\Delta_\nu\phi$, show that $\delta\mathcal L$ is a total derivative, read off $\mathcal J^\mu{}_\nu$ and the four currents $T^{\mu\nu}$. Is $T^{\mu\nu}$ symmetric?
*[variation of PS2.4(c)]*

^wn-3-a

(b) Find $T^{00}$ and $T^{0i}$, and write $H$ and $\mathbf P$ in terms of $\phi$ and $\pi = \dot\phi$.
*[variation of PS5.4(b)]*

^wn-3-b

(c) Verify $\partial_\mu T^{\mu\nu} = 0$ directly from the field equation.
*[variation of PS5.4(a)]*

^wn-3-c

(d) Add a fixed external source, $\mathcal L \to \mathcal L + J(x)\phi$. With $T^{\mu\nu}$ built from the full $\mathcal L$, show that $\partial_\mu T^{\mu\nu} = -(\partial^\nu J)\,\phi$ on solutions, and give $dH/dt$ and $dP^i/dt$.
*[extension of PS2.4(c)]*

^wn-3-d

### W4. Lorentz transformations: angular momentum and boosts of the real scalar

Take $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ and $\Lambda = 1 + \omega$, under which the scalar field becomes $\phi'(x) = \phi(\Lambda^{-1}x)$.

^wn-4

(a) Show that $\delta\phi = \frac12\omega_{\nu\rho}\Delta^{\nu\rho}\phi$ with $\Delta^{\nu\rho}\phi = x^\nu\partial^\rho\phi - x^\rho\partial^\nu\phi$, and that $\delta\mathcal L = \frac12\omega_{\nu\rho}\,\partial_\mu\mathcal J^{\mu\nu\rho}$ with $\mathcal J^{\mu\nu\rho} = (x^\nu g^{\mu\rho} - x^\rho g^{\mu\nu})\mathcal L$. Hence find the six Noether currents $\mathcal M^{\mu\nu\rho}$ in terms of $T^{\mu\nu}$.
*[extension of PS2.4(c)]*

^wn-4-a

(b) Show $\partial_\mu\mathcal M^{\mu\nu\rho} = 0$ on solutions using only $\partial_\mu T^{\mu\nu} = 0$ and the symmetry of $T^{\mu\nu}$.
*[extension of PS2.4(c)]*

^wn-4-b

(c) Show $\mathbf J = \int d^3x\;\mathbf x\times\boldsymbol{\mathcal P}$ with $\boldsymbol{\mathcal P} = -\pi\nabla\phi$, and $K^i = J^{i0} = \int d^3x\,x^i\mathcal H - tP^i$. What does $dK^i/dt = 0$ say?
*[new]*

^wn-4-c

### W5★. Dilatations of the massless scalar

Take $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ and the scale transformation $\phi'(x) = \lambda\,\phi(\lambda x)$, $\lambda = e^\alpha$ (the prefactor is $\lambda^{[\phi]}$, $[\phi] = 1$).

^wn-5

(a) Find $\Delta\phi$ and show that $\delta\mathcal L = \alpha\,\partial_\nu(x^\nu\mathcal L) + \alpha\,m^2\phi^2$.
*[new]*

^wn-5-a

(b) For $m = 0$, find the dilatation current and write it as $D^\mu = x_\nu T^{\mu\nu} + \phi\,\partial^\mu\phi$.
*[new]*

^wn-5-b

(c) For $m \neq 0$, show $\partial_\mu D^\mu = m^2\phi^2$ on solutions directly, using the trace $T^\mu{}_\mu$. Why does the mass break the symmetry?
*[new]*

^wn-5-c

## The complex scalar field

### W6. The U(1) current, its sign and its charge

Take $\mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi - V(\phi^{\ast}\phi)$, $V$ smooth.

^wn-6

(a) Find the Noether current of $\phi \to e^{i\alpha}\phi$, $\phi^{\ast} \to e^{-i\alpha}\phi^{\ast}$, and show that it is conserved on solutions for every $V$.
*[HW-literal PS2.3(d)]*

^wn-6-a

(b) Evaluate $j^0$ on the positive-frequency solution $\phi = A\,e^{-iEt + i\mathbf p\cdot\mathbf x}$ ($V = 0$, $E = E_{\mathbf p} > 0$). Which sign does it have? Lecture 3 writes the current with the opposite overall sign: is that a different physics, and what does $\alpha \to -\alpha$ do?
*[variation of PS2.3(d)]*

^wn-6-b

(c) After quantization the course, Peskin–Schroeder and Problem Set 3 use $\hat Q = \frac12(\hat N_a - \hat N_b)$. Express $\hat Q$ through the normal-ordered Noether charge $\int d^3x\,:\!\hat j^0\!:$, and say which part of the charge assignment is physical.
*[variation of PS3.2(c)]*

^wn-6-c

(d) Under charge conjugation, $U(\mathcal C)\hat\phi(x)U(\mathcal C)^{-1} = \hat\phi^\dagger(x)$ with $U(\mathcal C)$ unitary. How does the normal-ordered current $\hat j^\mu$ transform, and what happens to $\hat Q$?
*[HW-literal PS7.4(b), the C part]*

^wn-6-d

### W7. Breaking the U(1)

Add to the free complex field $\mathcal L_0 = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi$ a term that is not invariant under phases.

^wn-7

(a) $\mathcal L = \mathcal L_0 - \frac{\lambda}{2}(\phi^2 + \phi^{\ast 2})$, $\lambda$ real. Compute $\delta\mathcal L$ under the phase rotation, show it is not a divergence, and find $\partial_\mu j^\mu$ of the current of W6 on solutions in two ways (from $\delta\mathcal L$ and from the field equations). What is the extra term in real components $\phi = (\phi_1 + i\phi_2)/\sqrt2$?
*[variation of PS2.3(c)–(d)]*

^wn-7-a

(b) $\mathcal L = \mathcal L_0 - g(\phi^3 + \phi^{\ast 3})$, $g$ real. Find $\partial_\mu j^\mu$ on solutions. Which finite phase rotations are still symmetries, and why do they give no conserved current?
*[new]*

^wn-7-b

### W8. Translations and Lorentz transformations of the complex scalar

Take the free $\mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi$.

^wn-8

(a) Find the canonical $T^{\mu\nu}$, summed over $\phi$ and $\phi^{\ast}$. Is it symmetric?
*[variation of PS2.4(c)]*

^wn-8-a

(b) Show $T^{00} = \mathcal H = \pi^{\ast}\pi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi$ with $\pi = \dot\phi^{\ast}$, $\pi^{\ast} = \dot\phi$, and find the momentum $\mathbf P$ in field form.
*[variation of PS5.4(b)]*

^wn-8-b

(c) Write the Lorentz current $\mathcal M^{\mu\nu\rho}$. Why is there no spin part, although the field has two real components?
*[new]*

^wn-8-c

## The Dirac field

### W9. The vector U(1)

Take $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, $\psi$ and $\bar\psi$ independent, and $\psi \to e^{i\alpha}\psi$.

^wn-9

(a) Find $\Delta\psi$ and $\Delta\bar\psi$, and compute $\delta\mathcal L$ by the chain rule, term by term. Which term would be missed if $\bar\psi$ were dropped because $\mathcal L$ contains no $\partial_\mu\bar\psi$?
*[variation of PS6.5(c)]*

^wn-9-a

(b) Find the Noether current in the recipe of the course (the sign convention of PS6.5(d)), and check its conservation for general $m$ from the Dirac equation and its conjugate. Compare with the current $j^\mu = \bar\psi\gamma^\mu\psi$ of Peskin–Schroeder eq. (3.73).
*[variation of PS6.5(d)–(e)]*

^wn-9-b

(c) Show that the classical charge density $\bar\psi\gamma^0\psi$ is positive, unlike the complex scalar's (W6(b)). After quantization with anticommutators and normal ordering, what does $\hat Q = \int d^3x\,:\!\hat\psi^\dagger\hat\psi\!:$ count?
*[extension of PS6.2]*

^wn-9-c

### W10. The chiral rotation and its breaking by the mass

The chiral transformation $\psi \to e^{i\alpha\gamma^5}\psi$ gives $\bar\psi \to \bar\psi\,e^{i\alpha\gamma^5}$ (Problem Set 6, Problem 5(a)) and $\delta\mathcal L = -2i\alpha m\,\bar\psi\gamma^5\psi$ (5(c)).

^wn-10

(a) Determine the Noether current $j^\mu_5$ that follows from the symmetry in the massless case.
*[HW-literal PS6.5(d)]*

^wn-10-a

(b) Compute $\partial_\mu j^\mu_5$ using the Dirac equation for general $m$. It should vanish for $m = 0$ but not for $m \neq 0$.
*[HW-literal PS6.5(e)]*

^wn-10-b

(c) Restate (b) for the axial current $\mathsf A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$ (the $j^{\mu5}$ of the course and of Peskin–Schroeder) and compare with Peskin–Schroeder eq. (3.75). Check (b) against $\delta\mathcal L/\alpha$, and give $dQ_5/dt$ for $Q_5 = \int d^3x\,\mathsf A^0$.
*[variation of PS6.5(e)]*

^wn-10-c

### W11. Left and right currents

In the chiral basis, $\psi = (\psi_L, \psi_R)$ and $\mathcal L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L)$.

^wn-11

(a) For $m = 0$ the phases $\psi_L \to e^{i\alpha_L}\psi_L$ and $\psi_R \to e^{i\alpha_R}\psi_R$ are independent symmetries. Write them as $\psi \to e^{i\alpha_LP_L}\psi$, $\psi \to e^{i\alpha_RP_R}\psi$, and find their Noether currents (course sign convention) in Dirac and in Weyl form.
*[variation of PS6.5(d)]*

^wn-11-a

(b) Show that the currents of W9 and W10 are the combinations for $\alpha_L = \alpha_R$ and for $\alpha_L = -\alpha_R$. Which is which?
*[extension of PS6.5(d)]*

^wn-11-b

(c) For $m \neq 0$, compute $\delta\mathcal L$ for the left phase alone and give $\partial_\mu j^\mu_L$ on solutions in terms of $\mathsf P$. Which combination of the two currents stays conserved?
*[extension of PS6.5(e)]*

^wn-11-c

### W12. Translations: the Dirac energy–momentum tensor

Take $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$.

^wn-12

(a) Show that $x \to x - a$ gives $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ and the canonical tensor $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L$. Why does $\bar\psi$ contribute nothing to the first term?
*[extension of PS5.4]*

^wn-12-a

(b) Use the Dirac equation to show that the energy–momentum tensor is conserved.
*[HW-literal PS5.4(a)]*

^wn-12-b

(c) Write the momentum operator for the Dirac field (one equation), and show that $H = \int d^3x\,T^{00} = \int d^3x\,\psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$ for every configuration, $\alpha^j = \gamma^0\gamma^j$, $\beta = \gamma^0$, and $= \int d^3x\,\psi^\dagger i\partial_t\psi$ on solutions.
*[HW-literal PS5.4(b), with H as a variation]*

^wn-12-c

### W13. Lorentz transformations: the Dirac spin current

Take $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ and the spinor law $\psi'(x') = \Lambda_{1/2}\psi(x)$, $\Lambda_{1/2} = 1 - \frac i2\omega_{\mu\nu}S^{\mu\nu} + O(\omega^2)$.

^wn-13

(a) Find the spin part $\mathcal S^{\lambda\mu\nu}$ of the Lorentz current $\mathcal M^{\lambda\mu\nu} = x^\mu T^{\lambda\nu} - x^\nu T^{\lambda\mu} + \mathcal S^{\lambda\mu\nu}$.
*[extension of PS5.4]*

^wn-13-a

(b) Using $S^{jk} = \frac12\varepsilon^{jkl}\Sigma^l$, $\Sigma^l = \mathrm{diag}(\sigma^l, \sigma^l)$, show that $\mathbf J = \int d^3x\,\psi^\dagger\bigl(\mathbf x\times(-i\nabla) + \frac12\boldsymbol\Sigma\bigr)\psi$.
*[new]*

^wn-13-b

(c) Are the orbital and spin parts separately conserved? Give $dS^{jk}/dt$ in terms of $T^{\mu\nu}$.
*[new]*

^wn-13-c

### W14. A Lagrangian changed by a total derivative

Take the symmetric Dirac Lagrangian $\mathcal L_{\rm sym} = \frac i2\bigl(\bar\psi\gamma^\mu\partial_\mu\psi - \partial_\mu\bar\psi\,\gamma^\mu\psi\bigr) - m\bar\psi\psi$, in which $\bar\psi$ now has a derivative.

^wn-14

(a) Show $\mathcal L_{\rm sym} = \mathcal L - \frac i2\partial_\mu(\bar\psi\gamma^\mu\psi)$. Why do both give the same field equations?
*[new]*

^wn-14-a

(b) Compute the U(1) Noether current from $\mathcal L_{\rm sym}$ and compare it with W9. Show in general that adding $\partial_\mu K^\mu(\phi)$ to $\mathcal L$ never changes the current of an internal symmetry.
*[new]*

^wn-14-b

(c) Compute the canonical $T^{\mu\nu}_{\rm sym}$ and show $T^{\mu\nu}_{\rm sym} - T^{\mu\nu} = \partial_\lambda B^{\lambda\mu\nu}$ with $B^{\lambda\mu\nu} = -B^{\mu\lambda\nu}$. Conclude that $P^\nu$ is unchanged. Is $T^{\mu\nu}_{\rm sym}$ symmetric?
*[new]*

^wn-14-c

## The vector field

### W15. Translations and the symmetric tensor of the Maxwell field

Take $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu}$ with the four components $A_\lambda$ as fields.

^wn-15

(a) Construct the energy–momentum tensor $T^{\mu\nu}$ by Noether's theorem (the canonical construction).
*[HW-literal PS2.4(c)]*

^wn-15-a

(b) Instead of being handed the improvement, build it: compute the spin current $\mathcal S^{\lambda\mu\nu}$ with the vector generators $(S^{\mu\nu})_\alpha{}^\beta = \delta^\mu_\alpha g^{\nu\beta} - \delta^\nu_\alpha g^{\mu\beta}$ on $A_\alpha$, evaluate Belinfante's $K^{\lambda\mu\nu} = \frac12(\mathcal S^{\lambda\mu\nu} + \mathcal S^{\mu\nu\lambda} + \mathcal S^{\nu\mu\lambda})$, show $K^{\lambda\mu\nu} = F^{\mu\lambda}A^\nu$, and find $T_B^{\mu\nu} = T^{\mu\nu} + \partial_\lambda K^{\lambda\mu\nu}$ on solutions.
*[variation of PS2.4(d)]*

^wn-15-b

(c) Under $A_\rho \to A_\rho + \partial_\rho\chi$ the tensor $T_B^{\mu\nu}$ is invariant. Show that the canonical $T^{\mu\nu}$ changes by an improvement term on solutions, so that $P^\nu$ is gauge invariant anyway.
*[new]*

^wn-15-c

### W16. Lorentz transformations: spin and orbital angular momentum of the vector field

Take $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu}$, $A^\mu = (A^0, \mathbf A)$.

^wn-16

(a) Show that the spin current is $\mathcal S^{\lambda\mu\nu} = F^{\lambda\nu}A^\mu - F^{\lambda\mu}A^\nu$, and that adding the Proca mass term $\frac12m^2A_\mu A^\mu$ does not change it.
*[extension of PS2.4(c)]*

^wn-16-a

(b) Show that the spin charges are $\mathbf S = (S^{23}, S^{31}, S^{12}) = \int d^3x\;\mathbf E\times\mathbf A$ and $S^{0k} = -\int d^3x\,A^0E^k$.
*[new]*

^wn-16-b

(c) Show $T^{0k} = E^l\,\partial_kA^l$ (summed over $l$), and hence $\mathbf L = \int d^3x\,E^l\,(\mathbf x\times\nabla)A^l$.
*[new]*

^wn-16-c

(d) ★ Under the gauge transformation $A^\mu \to A^\mu + \partial^\mu\chi$, i.e. $\mathbf A \to \mathbf A - \nabla\chi$, with $\chi$ of compact support at the time considered, show $\Delta\mathbf S = -\int d^3x\,\chi\,\nabla\times\mathbf E$ and that $\mathbf J = \mathbf L + \mathbf S$ is gauge invariant for the free field.
*[new]*

^wn-16-d

### W17. Gauge and shift symmetries of the vector field

Take $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu}$.

^wn-17

(a) The constant shift $A_\rho \to A_\rho + \alpha^\nu g_{\nu\rho}$ (four parameters $\alpha^\nu$; it is the gauge transformation with $\chi = \alpha_\nu x^\nu$). Find the four Noether currents, show that their conservation is the source-free Maxwell equation, and identify the charges.
*[new]*

^wn-17-a

(b) For a fixed smooth function $\chi(x)$, $A_\rho \to A_\rho + \alpha\,\partial_\rho\chi$ ($\alpha$ constant) is a symmetry for every $\chi$. Find its current $j^\mu_\chi$, show that on solutions $j^\mu_\chi = \partial_\rho(F^{\rho\mu}\chi)$, an identically conserved improvement term, and give its charge for $\chi$ of compact support.
*[new]*

^wn-17-b

(c) ★ Add the Proca mass term $\frac12m^2A_\mu A^\mu$. Show that the shift of (a) is no longer a symmetry, find $\partial_\mu j^\mu{}_\nu$ on solutions in two ways, and deduce the Lorenz condition $\partial_\mu A^\mu = 0$ for $m \neq 0$.
*[new]*

^wn-17-c

## All fields

### W18. Short response: signs and normalizations

Short answers: a formula, a number, or a phrase. No derivations are needed.
*[variation of PS7.1]*

^wn-18

(a) The lecture and Peskin–Schroeder translate by $x \to x - a$ and get the currents $+T^\mu{}_\nu$. What current does Yu's $x' = x + \varepsilon$ give?

^wn-18-a

(b) Give the Noether boost charge $K^i = J^{i0}$ of a scalar field in terms of $\mathcal H$ and $P^i$, and its relation to the course's Hilbert-space boost generator $\hat K^i = \hat J^{0i}$.

^wn-18-b

(c) What happens to the Lorentz charges if the $\frac12$ in $\delta\phi = \frac12\omega_{\nu\rho}\Delta^{\nu\rho}\phi$ is dropped?

^wn-18-c

(d) With $\Delta\phi = +i\phi$, what is the sign of $j^0$ for a positive-frequency complex scalar solution, and how is the course's $\hat Q$ related to $\int d^3x\,:\!\hat j^0\!:$?

^wn-18-d

(e) Give the Noether current of $\psi \to e^{i\alpha}\psi$ in the course's recipe, and the charge of one $a$-quantum (electron) under $\hat Q = \int d^3x\,:\!\hat\psi^\dagger\hat\psi\!:$.

^wn-18-e

(f) Give $\partial_\mu(\bar\psi\gamma^\mu\gamma^5\psi)$ on solutions of the Dirac equation.

^wn-18-f

(g) For which of the real scalar, complex scalar, Dirac and Maxwell fields is the canonical $T^{\mu\nu}$ symmetric?

^wn-18-g

(h) Which of $\mathbf L$, $\mathbf S$, $\mathbf J = \mathbf L + \mathbf S$ of the free Maxwell field are gauge invariant?

^wn-18-h
