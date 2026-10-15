---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Noether Currents|Worksheet]] · [[PHY 513 Practice Midterm Solutions|Practice Midterm Solutions]]

# PHY 513 Worksheet — Noether Currents (Solutions)

Solutions to [[PHY 513 Worksheet — Noether Currents]], folded so that you can try first; each problem is embedded above its solution. Every solution runs the six steps of [[P3 Noether's Procedure]] in the course's conventions ([[Larsen PHY 513]]): generator $\Delta\phi$, $\delta\mathcal L$ (by substitution or by the chain rule), the test that defines $\mathcal J^\mu$, the current $j^\mu = \sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_i)}\Delta\phi_i - \mathcal J^\mu$, conservation on shell (or the divergence $X = $ the non-divergence part of $\delta\mathcal L/\alpha$, [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]), and the charge. Each ends with the line that says how it was checked: *Checked against* names the home box in these notes (or the submitted solution, "as written"); *Derived here; check* marks a result with no home box, derived from boxes that exist, with the special case or independent computation it was checked against. A printable copy is `~/Downloads/PHY513_worksheet_noether_solutions.pdf`.

---

## The real scalar field

### W1. Shift symmetries

![[PHY 513 Worksheet — Noether Currents#^wn-1]]

![[PHY 513 Worksheet — Noether Currents#^wn-1-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-1-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-1-c]]

> [!success]- Solution
> **Answers.** (a) $\Delta\phi = 1$, $\mathcal J^\mu = 0$, $j^\mu = \partial^\mu\phi$, $Q = \int d^3x\,\dot\phi$; $\partial_\mu j^\mu = \partial^2\phi$, which is the field equation. (b) $\delta\mathcal L = -\alpha m^2\phi$, not a divergence; $\partial_\mu j^\mu = -m^2\phi = \delta\mathcal L/\alpha$ on solutions. (c) $\mathcal J^\mu = c^\mu\phi$, $j^\mu = (c\cdot x)\,\partial^\mu\phi - c^\mu\phi$, conserved; for $c = (1, \mathbf 0)$, $Q = tQ_{\rm shift} - \int d^3x\,\phi$; no symmetry for $m \neq 0$.
>
> **(a) Step 1** (generator). $\phi'(x) = \phi(x) + \alpha$, so $\Delta\phi = \partial\phi'/\partial\alpha = 1$.
>
> **Step 2** ($\delta\mathcal L$). $\alpha$ is constant, so $\partial_\mu\phi' = \partial_\mu\phi$ and $\mathcal L(\phi') = \frac12\partial_\mu\phi\,\partial^\mu\phi$: $\delta\mathcal L = 0$, outcome (i), $\mathcal J^\mu = 0$.
>
> **Step 3** (current). $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi$ (both factors of the contraction respond, cancelling the $\frac12$), so $j^\mu = \partial^\mu\phi\cdot 1 - 0 = \partial^\mu\phi$.
>
> **Step 4** (conservation). $\partial_\mu j^\mu = \partial_\mu\partial^\mu\phi = \partial^2\phi$. The Euler–Lagrange equation is $\partial\mathcal L/\partial\phi - \partial_\mu(\partial^\mu\phi) = -\partial^2\phi = 0$. So $\partial_\mu j^\mu = 0$ exactly on solutions, and conversely: the conservation law of this current is the massless field equation.
>
> **Step 5** (charge). $j^0 = \partial^0\phi = \dot\phi = \pi$, so $Q = \int d^3x\,\dot\phi$, the total conjugate momentum (the field version of a cyclic coordinate).
>
> **(b) Step 1** ($\delta\mathcal L$). The kinetic term is unchanged as in (a); the mass term gives $-\frac12m^2(\phi + \alpha)^2 + \frac12m^2\phi^2 = -\alpha m^2\phi + O(\alpha^2)$. So $\delta\mathcal L = -\alpha m^2\phi$.
>
> **Step 2** (not a divergence). Suppose $-m^2\phi = \partial_\mu\mathcal J^\mu$ for every configuration, with $\mathcal J$ built locally from the fields. Take a bump $\phi \ge 0$, $\phi \not\equiv 0$, supported inside a ball $B$ of spacetime. By the divergence theorem $\int_B\partial_\mu\mathcal J^\mu$ is the flux through $\partial B$, where the field and its derivatives vanish, so it equals the flux for $\phi \equiv 0$, which is $\int_B(-m^2\cdot0) = 0$; but $\int_B(-m^2\phi) < 0$. Contradiction: outcome (iii), $X = -m^2\phi$.
>
> **Step 3** (divergence of the would-be current). The mass term has no derivatives, so the current of (a) is unchanged, $j^\mu = \partial^\mu\phi$. On solutions, $(\partial^2 + m^2)\phi = 0$, so $\partial_\mu j^\mu = \partial^2\phi = -m^2\phi = X = \delta\mathcal L/\alpha$, as [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]] requires. The charge changes, $dQ/dt = -m^2\int d^3x\,\phi$.
>
> **(c) Step 1** (generator). $\phi' = \phi + \alpha\,c_\nu x^\nu$: $\Delta\phi = c_\nu x^\nu \equiv c\cdot x$, a function of $x$ only, and $\partial_\mu(\Delta\phi) = c_\nu\delta^\nu{}_\mu = c_\mu$.
>
> **Step 2** ($\delta\mathcal L$, chain rule). $\partial\mathcal L/\partial\phi = 0$ for $m = 0$, so $\delta\mathcal L = \alpha\,\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial_\mu(\Delta\phi) = \alpha\,\partial^\mu\phi\,c_\mu = \alpha\,c^\mu\partial_\mu\phi = \alpha\,\partial_\mu(c^\mu\phi)$, since $c$ is constant.
>
> **Step 3** (test). A divergence, outcome (ii): $\mathcal J^\mu = c^\mu\phi \neq 0$.
>
> **Step 4** (current). $j^\mu = \partial^\mu\phi\,(c\cdot x) - c^\mu\phi$.
>
> **Step 5** (check, off shell). $\partial_\mu j^\mu = (\partial^2\phi)(c\cdot x) + \partial^\mu\phi\,c_\mu - c^\mu\partial_\mu\phi = (c\cdot x)\,\partial^2\phi = -\mathrm{EL}\cdot\Delta\phi$ with $\mathrm{EL} = -\partial^2\phi$: the off-shell identity of [[§C1b.5 Noether's Theorem#^thm-c1b-5-4|Theorem §C1b.5.4]]; zero on solutions. Dropping $\mathcal J$ would leave $\partial_\mu(\partial^\mu\phi\,c\cdot x) = c^\mu\partial_\mu\phi \neq 0$: a false "broken symmetry".
>
> **Step 6** (charge for $c^\mu = (1, 0, 0, 0)$). Then $c\cdot x = t$, $c^0 = 1$, $j^0 = t\dot\phi - \phi$ and $Q = t\int d^3x\,\pi - \int d^3x\,\phi = tQ_{\rm shift} - \int d^3x\,\phi$. Its conservation says that $\int d^3x\,\phi$ grows linearly in time at the rate $Q_{\rm shift}$ of (a). Direct check: $dQ/dt = \int d^3x\,(\dot\phi + t\ddot\phi - \dot\phi) = t\int d^3x\,\nabla^2\phi = 0$ (surface term, on solutions $\ddot\phi = \nabla^2\phi$).
>
> **Step 7** ($m \neq 0$). The mass term adds $-\alpha m^2\phi\,(c\cdot x)$ to $\delta\mathcal L$; a bump $\phi \ge 0$ placed where $c\cdot x > 0$ shows by the argument of (b) that it is not a divergence: no symmetry.
>
> *Checked against:* (a)–(b) [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-1|Example §C1b.6.1]] (current $\partial^\mu\phi$, charge $\int\dot\phi$, $\delta\mathcal L = -\alpha m^2\phi$, the bump argument, divergence $-m^2\phi$); the shift row of [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]. *Derived here; check:* (c) has no home box; it is outcome (ii) of [[§C1b.5 Noether's Theorem#^rem-c1b-5-10|§C1b.5, Remark: The three outcomes of the test and their currents]], verified by the off-shell identity (Step 5) and by the direct $dQ/dt$ (Step 6).

^sol-wn-1

### W2. Rotations of N real fields

![[PHY 513 Worksheet — Noether Currents#^wn-2]]

![[PHY 513 Worksheet — Noether Currents#^wn-2-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-2-b]]

> [!success]- Solution
> **Answers.** (a) $\Delta\phi_a = -\phi_b$, $\Delta\phi_b = \phi_a$; $j^\mu_{ab} = \phi_a\partial^\mu\phi_b - \phi_b\partial^\mu\phi_a$, $Q_{ab} = \int d^3x\,(\phi_a\pi_b - \phi_b\pi_a)$; $N(N-1)/2$ currents. (b) the $O(N-1)$ rotations of $\phi_1, \dots, \phi_{N-1}$ survive; $\partial_\mu j^\mu_{aN} = h\,\phi_a$.
>
> **(a) Step 1** (generators). With $\cos\alpha = 1 + O(\alpha^2)$, $\sin\alpha = \alpha + O(\alpha^3)$: $\phi'_a = \phi_a - \alpha\phi_b$, $\phi'_b = \phi_b + \alpha\phi_a$, so $\Delta\phi_a = -\phi_b$, $\Delta\phi_b = \phi_a$, and $\Delta\phi_c = 0$ for $c \neq a, b$.
>
> **Step 2** ($\delta\mathcal L = 0$). With $\rho \equiv \phi_i\phi_i$: $\delta\rho = 2\alpha(\phi_a\Delta\phi_a + \phi_b\Delta\phi_b) = 2\alpha(-\phi_a\phi_b + \phi_b\phi_a) = 0$, so $V(\rho)$ is invariant. Kinetic term: $\delta(\frac12\partial_\mu\phi_i\partial^\mu\phi_i) = \alpha(\partial_\mu\phi_a\,\partial^\mu\Delta\phi_a + \partial_\mu\phi_b\,\partial^\mu\Delta\phi_b) = \alpha(-\partial_\mu\phi_a\,\partial^\mu\phi_b + \partial_\mu\phi_b\,\partial^\mu\phi_a) = 0$. Outcome (i): $\mathcal J^\mu = 0$.
>
> **Step 3** (current). $\partial\mathcal L/\partial(\partial_\mu\phi_i) = \partial^\mu\phi_i$; one parameter moves two fields, so $j^\mu_{ab} = \partial^\mu\phi_a(-\phi_b) + \partial^\mu\phi_b\,\phi_a = \phi_a\partial^\mu\phi_b - \phi_b\partial^\mu\phi_a$.
>
> **Step 4** (conservation). $\partial_\mu j^\mu_{ab} = \phi_a\partial^2\phi_b - \phi_b\partial^2\phi_a$ (the terms $\partial_\mu\phi_a\partial^\mu\phi_b$ cancel). The field equations are $\partial^2\phi_i = -\partial V/\partial\phi_i = -2V'(\rho)\,\phi_i$, so $\partial_\mu j^\mu_{ab} = -2V'(\phi_a\phi_b - \phi_b\phi_a) = 0$.
>
> **Step 5** (charges and their number). $j^0_{ab} = \phi_a\dot\phi_b - \phi_b\dot\phi_a$, $\pi_i = \dot\phi_i$, so $Q_{ab} = \int d^3x\,(\phi_a\pi_b - \phi_b\pi_a)$, the field-space analogue of $xp_y - yp_x$. One current per parameter: $j_{ba} = -j_{ab}$, so the independent ones are labelled by planes $a < b$, $N(N-1)/2 = \dim SO(N)$ of them. For $N = 2$ there is one, $\phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$, the U(1) current of $\phi = (\phi_1 + i\phi_2)/\sqrt2$.
>
> **(b) Step 1** (which rotations survive). The kinetic term and $V$ are invariant as before; $h\phi_N$ changes by $\alpha h\,\Delta\phi_N$. For a rotation among $\phi_1, \dots, \phi_{N-1}$, $\Delta\phi_N = 0$: still a symmetry, $(N-1)(N-2)/2$ conserved currents ($O(N-1)$).
>
> **Step 2** (the $(a, N)$ rotation, from $\delta\mathcal L$). $\Delta\phi_a = -\phi_N$, $\Delta\phi_N = \phi_a$, so $\delta\mathcal L = \alpha h\,\phi_a$. It is not a divergence (a bump $\phi_a \ge 0$, $\phi_a \not\equiv 0$, as in W1(b)): $\mathcal J = 0$, $X = h\phi_a$. The new term has no derivatives, so the current is still $j^\mu_{aN} = \phi_a\partial^\mu\phi_N - \phi_N\partial^\mu\phi_a$, and on solutions $\partial_\mu j^\mu_{aN} = X = h\,\phi_a$.
>
> **Step 3** (from the field equations). Now $\partial^2\phi_i = -2V'\phi_i + h\,\delta_{iN}$. Then $\partial_\mu j^\mu_{aN} = \phi_a\partial^2\phi_N - \phi_N\partial^2\phi_a = \phi_a(-2V'\phi_N + h) - \phi_N(-2V'\phi_a) = h\,\phi_a$: the same. The $N - 1$ currents $j_{aN}$ are broken by the term that singles out the direction $N$.
>
> *Derived here; check:* the case $N = 2$ is [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-2|Example §C1b.6.2]](a) (generators, $\mathcal J = 0$, the current $\phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1$) with the rotation row of [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]; the broken case is [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]] with $X = h\phi_a$, verified in Step 3 by the field equations, the pattern of [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|Example §C1b.6.3]].

^sol-wn-2

### W3. Translations: the real scalar's energy and momentum

![[PHY 513 Worksheet — Noether Currents#^wn-3]]

![[PHY 513 Worksheet — Noether Currents#^wn-3-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-3-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-3-c]]

![[PHY 513 Worksheet — Noether Currents#^wn-3-d]]

> [!success]- Solution
> **Answers.** (a) $\Delta_\nu\phi = \partial_\nu\phi$, $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$, $T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L$, symmetric. (b) $T^{00} = \frac12\pi^2 + \frac12(\nabla\phi)^2 + V = \mathcal H$, $T^{0i} = -\pi\,\partial_i\phi$; $H = \int d^3x\,\mathcal H$, $\mathbf P = -\int d^3x\,\pi\nabla\phi$. (c) $\partial_\mu T^{\mu\nu} = (\partial^2\phi + V')\,\partial^\nu\phi = 0$. (d) $\partial_\mu T^{\mu\nu} = -(\partial^\nu J)\phi$; $dH/dt = -\int d^3x\,(\partial_tJ)\phi$, $dP^i/dt = \int d^3x\,(\partial_iJ)\phi$.
>
> **(a) Step 1** (generator). $\phi(x + a) = \phi(x) + a^\nu\partial_\nu\phi(x) + O(a^2)$: four parameters $a^\nu$, $\Delta_\nu\phi = \partial_\nu\phi$.
>
> **Step 2** ($\delta\mathcal L$). Chain rule with $\partial_\mu(\delta\phi) = a^\nu\partial_\mu\partial_\nu\phi$: $\delta\mathcal L = a^\nu\bigl[\frac{\partial\mathcal L}{\partial\phi}\partial_\nu\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial_\nu\partial_\mu\phi\bigr] = a^\nu\partial_\nu\mathcal L$, the derivative of the composite function, because $\mathcal L$ depends on $x$ only through $\phi$ and $\partial\phi$.
>
> **Step 3** (test). $a^\nu\partial_\nu\mathcal L = \partial_\mu(a^\mu\mathcal L) = a^\nu\partial_\mu(\delta^\mu{}_\nu\mathcal L)$ ($a$ constant; $a^\mu = \delta^\mu{}_\nu a^\nu$ factors out the parameter). Outcome (ii): $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$.
>
> **Step 4** (currents). $j^\mu{}_\nu = \partial^\mu\phi\,\partial_\nu\phi - \delta^\mu{}_\nu\mathcal L = T^\mu{}_\nu$; raising $\nu$ with $g^{\nu\rho}$: $T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L$, symmetric because $\partial^\mu\phi\,\partial^\nu\phi$ and $g^{\mu\nu}$ are.
>
> **(b)** $\partial_\mu\phi\,\partial^\mu\phi = \dot\phi^2 - (\nabla\phi)^2$, so $\mathcal L = \frac12\dot\phi^2 - \frac12(\nabla\phi)^2 - V$ and, with $\partial^0 = \partial_t$, $g^{00} = 1$:
>
> $$
> T^{00} = \dot\phi^2 - \mathcal L = \tfrac12\pi^2 + \tfrac12(\nabla\phi)^2 + V(\phi) = \mathcal H .
> $$
>
> $g^{0i} = 0$ and $\partial^i = -\partial_i$ give $T^{0i} = \dot\phi\,\partial^i\phi = -\pi\,\partial_i\phi$. Hence $H = P^0 = \int d^3x\,\mathcal H$ and $\mathbf P = -\int d^3x\,\pi\nabla\phi$.
>
> **(c)** Product rule: $\partial_\mu(\partial^\mu\phi\,\partial^\nu\phi) = \partial^2\phi\,\partial^\nu\phi + \partial^\mu\phi\,\partial_\mu\partial^\nu\phi$, and $\partial^\nu\mathcal L = \partial^\mu\phi\,\partial^\nu\partial_\mu\phi - V'\,\partial^\nu\phi$. Subtracting, the second-derivative terms cancel: $\partial_\mu T^{\mu\nu} = (\partial^2\phi + V')\,\partial^\nu\phi$. The field equation $\partial\mathcal L/\partial\phi - \partial_\mu\partial^\mu\phi = -V' - \partial^2\phi = 0$ makes it vanish.
>
> **(d) Step 1** (the field equation). $\partial\mathcal L/\partial\phi = -V' + J$, so $\partial^2\phi + V' - J = 0$.
>
> **Step 2** (divergence). Now $T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}(\mathcal L + J\phi)$ and $\partial^\nu(J\phi) = (\partial^\nu J)\phi + J\,\partial^\nu\phi$. As in (c),
>
> $$
> \partial_\mu T^{\mu\nu} = (\partial^2\phi + V' - J)\,\partial^\nu\phi - (\partial^\nu J)\,\phi = -(\partial^\nu J)\,\phi \quad\text{on solutions.}
> $$
>
> The explicit $x$-dependence of $\mathcal L$ is the obstruction: $\partial_\mu T^\mu{}_\nu = -\partial\mathcal L/\partial x^\nu|_{\rm explicit} = -(\partial_\nu J)\phi$.
>
> **Step 3** (charges). Integrate over space, dropping the flux $\int\partial_iT^{i\nu}$: $dH/dt = -\int d^3x\,(\partial_tJ)\,\phi$ and $dP^i/dt = -\int d^3x\,(\partial^iJ)\phi = \int d^3x\,(\partial_iJ)\,\phi$. A static source conserves energy but not momentum (it absorbs momentum, like a fixed wall).
>
> *Checked against:* [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|Theorem §C1b.7.5]] ($\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$; Derivation §C1b.7.5, step 3, for the explicit-$x$ divergence $-\partial\mathcal L/\partial x^\nu|_{\rm explicit}$); [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^ex-c1b-7-1|Example §C1b.7.1]] ($T^{\mu\nu}$, $T^{00} = \mathcal H$, $T^{0i}$ and the direct conservation for $V = \frac12m^2\phi^2$); [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-7|Theorem §C1b.7.7]] ($H$, $\mathbf P$). The general $V$ and the source term only add terms that the same steps handle.

^sol-wn-3

### W4. Lorentz transformations: angular momentum and boosts of the real scalar

![[PHY 513 Worksheet — Noether Currents#^wn-4]]

![[PHY 513 Worksheet — Noether Currents#^wn-4-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-4-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-4-c]]

> [!success]- Solution
> **Answers.** (a) $\mathcal M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$, purely orbital. (b) $\partial_\mu\mathcal M^{\mu\nu\rho} = T^{\nu\rho} - T^{\rho\nu} = 0$. (c) $\mathbf J = \int\mathbf x\times\boldsymbol{\mathcal P}$, $K^i = \int x^i\mathcal H - tP^i$; its conservation says that the centre of energy moves uniformly with velocity $\mathbf P/H$.
>
> **(a) Step 1** (generator). $\Lambda^{-1}x = x - \omega x$ to first order, so $\phi'(x) = \phi(x) - \omega^\sigma{}_\rho x^\rho\,\partial_\sigma\phi$. Lower $\sigma$ on $\omega$ and raise it on $\partial$: $-\omega^\sigma{}_\rho x^\rho\partial_\sigma\phi = -\omega_{\sigma\rho}x^\rho\partial^\sigma\phi = \omega_{\rho\sigma}x^\rho\partial^\sigma\phi$; rename $\rho \to \nu$, $\sigma \to \rho$ and split into halves, relabelling $\nu \leftrightarrow \rho$ in the second and using $\omega_{\rho\nu} = -\omega_{\nu\rho}$:
>
> $$
> \delta\phi = \omega_{\nu\rho}x^\nu\partial^\rho\phi = \tfrac12\omega_{\nu\rho}\bigl(x^\nu\partial^\rho\phi - x^\rho\partial^\nu\phi\bigr) = \tfrac12\omega_{\nu\rho}\Delta^{\nu\rho}\phi .
> $$
>
> **Step 2** ($\delta\mathcal L$). $\partial_\mu(\delta\phi) = -\omega^\sigma{}_\mu\partial_\sigma\phi - \omega^\sigma{}_\rho x^\rho\partial_\mu\partial_\sigma\phi$ (the first term from $\partial_\mu x^\rho = \delta^\rho{}_\mu$). Chain rule:
>
> $$
> \delta\mathcal L = -\omega^\sigma{}_\rho x^\rho\bigl[-m^2\phi\,\partial_\sigma\phi + \partial^\mu\phi\,\partial_\sigma\partial_\mu\phi\bigr] - \omega^\sigma{}_\mu\,\partial^\mu\phi\,\partial_\sigma\phi .
> $$
>
> The bracket is $\partial_\sigma\mathcal L$. The last term is $\omega_{\sigma\mu}\partial^\mu\phi\,\partial^\sigma\phi = 0$, antisymmetric against symmetric.
>
> **Step 3** (test). $\delta\mathcal L = -\omega^\sigma{}_\rho x^\rho\partial_\sigma\mathcal L = -\partial_\sigma(\omega^\sigma{}_\rho x^\rho\mathcal L) + \omega^\sigma{}_\sigma\mathcal L$, and $\omega^\sigma{}_\sigma = g^{\sigma\rho}\omega_{\rho\sigma} = 0$. With the given $\mathcal J$: $\frac12\omega_{\nu\rho}\mathcal J^{\sigma\nu\rho} = \frac12(\omega_\nu{}^\sigma x^\nu - \omega^\sigma{}_\rho x^\rho)\mathcal L = -\omega^\sigma{}_\rho x^\rho\mathcal L$ (since $\omega_\nu{}^\sigma = -\omega^\sigma{}_\nu$). So $\delta\mathcal L = \frac12\omega_{\nu\rho}\,\partial_\sigma\mathcal J^{\sigma\nu\rho}$: outcome (ii), $\mathcal J \neq 0$ because the point moves.
>
> **Step 4** (current). Coefficient of $\frac12\omega_{\nu\rho}$ (six independent currents):
>
> $$
> \mathcal M^{\mu\nu\rho} = \partial^\mu\phi\,\Delta^{\nu\rho}\phi - \mathcal J^{\mu\nu\rho} = x^\nu\bigl(\partial^\mu\phi\,\partial^\rho\phi - g^{\mu\rho}\mathcal L\bigr) - x^\rho\bigl(\partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L\bigr) = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu} .
> $$
>
> **(b)** $\partial_\mu(x^\nu T^{\mu\rho}) = \delta^\nu{}_\mu T^{\mu\rho} + x^\nu\partial_\mu T^{\mu\rho} = T^{\nu\rho}$ on solutions, and likewise for the other term: $\partial_\mu\mathcal M^{\mu\nu\rho} = T^{\nu\rho} - T^{\rho\nu} = 0$ because the scalar's $T$ is symmetric (W3(a)).
>
> **(c) Step 1** (rotations). $J^{jk} = \int d^3x\,(x^jT^{0k} - x^kT^{0j})$ with $T^{0k} = \mathcal P^k = -\pi\,\partial_k\phi$ (W3(b)). Then $J^i = \frac12\varepsilon_{ijk}J^{jk}$; relabelling $j \leftrightarrow k$ in the second term makes the two halves equal, so $J^i = \int d^3x\,\varepsilon_{ijk}x^j\mathcal P^k$, i.e. $\mathbf J = \int d^3x\;\mathbf x\times\boldsymbol{\mathcal P}$, all orbital.
>
> **Step 2** (boosts). $K^i = J^{i0} = \int d^3x\,(x^iT^{00} - x^0T^{0i})$ and $x^0 = t$ is constant on the slice: $K^i = \int d^3x\,x^i\mathcal H - tP^i$.
>
> **Step 3** (meaning). $K^i$ depends on $t$ explicitly. $0 = dK^i/dt = \frac{d}{dt}\int d^3x\,x^i\mathcal H - P^i$ (with $dP^i/dt = 0$), so $\frac{d}{dt}X^i_E = P^i/H$ for the centre of energy $X^i_E = \frac1H\int d^3x\,x^i\mathcal H$: it moves uniformly (fields falling off faster than $1/r^3$, since the current carries a factor $x$). Sign: the course's Hilbert-space boost generator is $\hat K^i = \hat J^{0i} = -\hat K^i_{\rm N}$.
>
> *Checked against:* the Lorentz row of [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]] ($\Delta^{\nu\rho}\phi$); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]], second derivation (the lecture's form for the real scalar: the same $\mathcal J^{\sigma\nu\rho}$ and $\mathcal M$); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-2|Theorem §C1b.8.2]] (b); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-1|Example §C1b.8.1]] and [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-3|Theorem §C1b.8.3]] (c); the generator sign [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]].

^sol-wn-4

### W5★. Dilatations of the massless scalar

![[PHY 513 Worksheet — Noether Currents#^wn-5]]

![[PHY 513 Worksheet — Noether Currents#^wn-5-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-5-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-5-c]]

> [!success]- Solution
> **Answers.** (a) $\Delta\phi = \phi + x^\mu\partial_\mu\phi$. (b) $\mathcal J^\mu = x^\mu\mathcal L$, $D^\mu = x_\nu T^{\mu\nu} + \phi\,\partial^\mu\phi$. (c) $\partial_\mu D^\mu = m^2\phi^2$; the mass is the only dimensionful parameter.
>
> **(a) Step 1** (generator). $\lambda = 1 + \alpha + O(\alpha^2)$: $\phi'(x) = (1 + \alpha)\,\phi(x + \alpha x) = (1 + \alpha)(\phi + \alpha x^\mu\partial_\mu\phi) + O(\alpha^2)$, so $\Delta\phi = \phi + x^\mu\partial_\mu\phi$.
>
> **Step 2** (kinetic part). $\partial_\mu(\Delta\phi) = \partial_\mu\phi + \delta^\nu{}_\mu\partial_\nu\phi + x^\nu\partial_\mu\partial_\nu\phi = 2\partial_\mu\phi + x^\nu\partial_\nu\partial_\mu\phi$. With $\mathcal L_{\rm kin} = \frac12(\partial\phi)^2$: $\delta\mathcal L_{\rm kin} = \alpha\,\partial^\mu\phi\,(2\partial_\mu\phi + x^\nu\partial_\nu\partial_\mu\phi) = \alpha\,(4\mathcal L_{\rm kin} + x^\nu\partial_\nu\mathcal L_{\rm kin}) = \alpha\,\partial_\nu(x^\nu\mathcal L_{\rm kin})$, using $\partial_\nu\mathcal L_{\rm kin} = \partial^\mu\phi\,\partial_\nu\partial_\mu\phi$ and $\partial_\nu x^\nu = 4$.
>
> **Step 3** (mass part). With $\mathcal L_{\rm m} = -\frac12m^2\phi^2$: $\delta\mathcal L_{\rm m} = -\alpha m^2\phi(\phi + x^\nu\partial_\nu\phi) = \alpha(2\mathcal L_{\rm m} + x^\nu\partial_\nu\mathcal L_{\rm m}) = \alpha\bigl[\partial_\nu(x^\nu\mathcal L_{\rm m}) - 2\mathcal L_{\rm m}\bigr] = \alpha\bigl[\partial_\nu(x^\nu\mathcal L_{\rm m}) + m^2\phi^2\bigr]$.
>
> **Step 4** (total). $\delta\mathcal L = \alpha\,\partial_\nu(x^\nu\mathcal L) + \alpha m^2\phi^2$.
>
> **(b)** For $m = 0$: outcome (ii), $\mathcal J^\mu = x^\mu\mathcal L$. Current: $D^\mu = \partial^\mu\phi\,(\phi + x^\nu\partial_\nu\phi) - x^\mu\mathcal L = \phi\,\partial^\mu\phi + x_\nu\bigl(\partial^\mu\phi\,\partial^\nu\phi - g^{\mu\nu}\mathcal L\bigr) = x_\nu T^{\mu\nu} + \phi\,\partial^\mu\phi$.
>
> **(c) Step 1** (from $\delta\mathcal L$). Split $\delta\mathcal L = \alpha(\partial_\nu\mathcal J^\nu + X)$ with $\mathcal J^\nu = x^\nu\mathcal L$, $X = m^2\phi^2$. $X$ is not a divergence (it integrates to a positive number against a bump, while a divergence integrates to the flux of the zero configuration, zero). [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]: $\partial_\mu D^\mu = m^2\phi^2$ on solutions, with the same $D^\mu$ ($\mathcal J$ and $\partial\mathcal L/\partial(\partial_\mu\phi)$ as before).
>
> **Step 2** (directly). $T^\mu{}_\mu = (\partial\phi)^2 - 4\mathcal L = (\partial\phi)^2 - 2(\partial\phi)^2 + 2m^2\phi^2 = -(\partial\phi)^2 + 2m^2\phi^2$. With $\partial_\mu T^{\mu\nu} = 0$ and $\partial_\mu x_\nu = g_{\mu\nu}$:
>
> $$
> \partial_\mu D^\mu = T^\mu{}_\mu + x_\nu\partial_\mu T^{\mu\nu} + (\partial\phi)^2 + \phi\,\partial^2\phi = 2m^2\phi^2 + \phi(-m^2\phi) = m^2\phi^2 .
> $$
>
> The two agree. For $m = 0$ the trace $T^\mu{}_\mu = -(\partial\phi)^2$ is cancelled by the $\phi\,\partial^\mu\phi$ term, and $D$ is conserved.
>
> **Step 3** (why). Scale invariance needs every coupling dimensionless; $m$ has dimension 1 and sets a length $1/m$ that a dilatation would change.
>
> *Checked against:* [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^rem-c1b-8-4|§C1b.8, ★ Remark: Dilatations]] (the same $\delta\mathcal L = \alpha\,\partial_\nu(x^\nu\mathcal L) + \alpha m^2\phi^2$, $\mathcal J^\mu = x^\mu\mathcal L$, current $x_\nu T^{\mu\nu} + \phi\,\partial^\mu\phi$, broken by $m$); the scale row of [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]]. *Derived here; check:* the direct divergence of Step 2 (not in the remark) agrees with $X$ of Step 1.

^sol-wn-5

## The complex scalar field

### W6. The U(1) current, its sign and its charge

![[PHY 513 Worksheet — Noether Currents#^wn-6]]

![[PHY 513 Worksheet — Noether Currents#^wn-6-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-6-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-6-c]]

![[PHY 513 Worksheet — Noether Currents#^wn-6-d]]

> [!success]- Solution
> **Answers.** (a) $j^\mu = i(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi)$. (b) $j^0 = -2E\lvert A\rvert^2 < 0$; the opposite sign on the slide is a slip, not a convention, and $\alpha \to -\alpha$ flips only the overall sign. (c) $\hat Q = -\frac12\int d^3x\,:\!\hat j^0\!:$, $\int d^3x\,:\!\hat j^0\!: = \hat N_b - \hat N_a$; only the ratio $-1$ of the two species' charges is physical. (d) $\hat j^\mu \to -\hat j^\mu$, $\hat Q \to -\hat Q$.
>
> **(a) Step 1** (generators, symmetry). $\Delta\phi = i\phi$, $\Delta\phi^{\ast} = -i\phi^{\ast}$. Every term of $\mathcal L$ pairs one $\phi$ with one $\phi^{\ast}$, and $\partial_\mu(e^{i\alpha}\phi) = e^{i\alpha}\partial_\mu\phi$ for constant $\alpha$, so $\mathcal L$ is invariant, $V(\phi^{\ast}\phi)$ included: $\mathcal J^\mu = 0$.
>
> **Step 2** (current). $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi^{\ast}$, $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = \partial^\mu\phi$; summing over both fields,
>
> $$
> j^\mu = \partial^\mu\phi^{\ast}\,(i\phi) + \partial^\mu\phi\,(-i\phi^{\ast}) = i\bigl(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi\bigr) .
> $$
>
> **Step 3** (field equations). $\partial\mathcal L/\partial\phi^{\ast} = -(m^2 + V')\phi$ (chain rule, $V' = dV/d(\phi^{\ast}\phi)$), so $\partial^2\phi = -(m^2 + V')\phi$ and $\partial^2\phi^{\ast} = -(m^2 + V')\phi^{\ast}$.
>
> **Step 4** (conservation). $\partial_\mu j^\mu = i(\partial_\mu\phi\,\partial^\mu\phi^{\ast} + \phi\,\partial^2\phi^{\ast} - \partial_\mu\phi^{\ast}\partial^\mu\phi - \phi^{\ast}\partial^2\phi) = i(\phi\,\partial^2\phi^{\ast} - \phi^{\ast}\partial^2\phi)$, the first-derivative terms cancelling (symmetric metric). Step 3 gives $i\bigl(-(m^2 + V')\phi\phi^{\ast} + (m^2 + V')\phi^{\ast}\phi\bigr) = 0$ for every $V$.
>
> **(b)** $\dot\phi = -iE\phi$, $\dot\phi^{\ast} = iE\phi^{\ast}$, so $j^0 = i\bigl(\phi\,(iE\phi^{\ast}) - \phi^{\ast}(-iE\phi)\bigr) = i\cdot 2iE\lvert A\rvert^2 = -2E\lvert A\rvert^2 < 0$. Lecture 3 (slide 22) writes $j^\mu = -i\bigl((\partial^\mu\phi^{\ast})\phi - (\partial^\mu\phi)\phi^{\ast}\bigr)$; with the slide's own $\Delta\phi = i\phi$ and its definition of $j^\mu$ the first line gives the sign of (a), so the printed line is a sign slip, not another physics. Replacing $\alpha$ by $-\alpha$ flips $\Delta\phi$, hence $j^\mu$, as a whole; conservation and the ratio of charges are unchanged.
>
> **(c) Step 1** (reorder under normal ordering). Quantized, $\phi^{\ast} \to \hat\phi^\dagger$ and $\hat j^0 = i(\hat\phi\,\partial_t\hat\phi^\dagger - \hat\phi^\dagger\partial_t\hat\phi)$. Inside $:\;:$ bosonic operators commute, so $:\!\hat\phi\,\partial_t\hat\phi^\dagger\!: = :\!\partial_t\hat\phi^\dagger\,\hat\phi\!:$ and $:\!\hat j^0\!: = -i\,:\!(\hat\phi^\dagger\partial_t\hat\phi - \partial_t\hat\phi^\dagger\,\hat\phi)\!:$.
>
> **Step 2** (compare). The course's charge is $\hat Q = \frac i2\int d^3x\,:\!(\hat\phi^\dagger\partial_t\hat\phi - \partial_t\hat\phi^\dagger\,\hat\phi)\!: = \frac12(\hat N_a - \hat N_b)$. So $\hat Q = -\frac12\int d^3x\,:\!\hat j^0\!:$ and $\int d^3x\,:\!\hat j^0\!: = -2\hat Q = \hat N_b - \hat N_a$: particles counted $-1$, as (b) predicts for positive frequency.
>
> **Step 3** (what is physical). The overall factor and sign are conventions (the sign of $\alpha$, the normalization of the charge); the ratio $-1$ between $a$- and $b$-quanta, and the neutral vacuum fixed by normal ordering, are not.
>
> **(d)** $U(\mathcal C)$ is unitary and constant, so it passes through $\partial^\mu$ and maps $\hat\phi \to \hat\phi^\dagger$, $\hat\phi^\dagger \to \hat\phi$ (adjoint of the first). Then $\hat j^\mu \to i\,:\!(\hat\phi^\dagger\partial^\mu\hat\phi - \hat\phi\,\partial^\mu\hat\phi^\dagger)\!: = -\hat j^\mu$, reordering inside the normal ordering at no cost. So $\hat Q \to -\hat Q$, equivalently $\hat N_a \leftrightarrow \hat N_b$.
>
> *Checked against:* [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]] (the current, conserved for every $m$ and $V$; $j^0 = -2E\lvert A\rvert^2$ in its derivation, step 6); [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]] (the slide's sign); [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]], [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]] (c); [[§C9.10 C, T and CPT for the Complex Scalar Field#^thm-c9-10-4|Theorem §C9.10.4]] (d). The user's Problem Set 2, Problem 3(d), as written, gives the current of (a); the user's Problem Set 7, Problem 4(b), as written, gives $-J^\mu$ under $\mathcal C$ for $J^\mu = -\hat j^\mu$, the same rule.

^sol-wn-6

### W7. Breaking the U(1)

![[PHY 513 Worksheet — Noether Currents#^wn-7]]

![[PHY 513 Worksheet — Noether Currents#^wn-7-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-7-b]]

> [!success]- Solution
> **Answers.** (a) $\delta\mathcal L = -i\alpha\lambda(\phi^2 - \phi^{\ast 2})$; $\partial_\mu j^\mu = -i\lambda(\phi^2 - \phi^{\ast 2}) = 2\lambda\phi_1\phi_2$; the term is a mass splitting $m_{1,2}^2 = m^2 \pm \lambda$. (b) $\partial_\mu j^\mu = -3ig(\phi^3 - \phi^{\ast 3}) = 6g\,\mathrm{Im}(\phi^3)$; only $\alpha \in \frac{2\pi}3\mathbb Z$ survive, a discrete $\mathbb Z_3$ with no current.
>
> **(a) Step 1** ($\delta\mathcal L$). $\mathcal L_0$ is invariant (W6). $(e^{i\alpha}\phi)^2 = \phi^2 + 2i\alpha\phi^2 + O(\alpha^2)$ and $(e^{-i\alpha}\phi^{\ast})^2 = \phi^{\ast 2} - 2i\alpha\phi^{\ast 2} + O(\alpha^2)$, so $\delta\mathcal L = -\frac\lambda2(2i\alpha\phi^2 - 2i\alpha\phi^{\ast 2}) = -i\alpha\lambda(\phi^2 - \phi^{\ast 2})$.
>
> **Step 2** (real components). $\phi^2 + \phi^{\ast 2} = \phi_1^2 - \phi_2^2$, so $\mathcal L = \frac12(\partial\phi_1)^2 + \frac12(\partial\phi_2)^2 - \frac12(m^2 + \lambda)\phi_1^2 - \frac12(m^2 - \lambda)\phi_2^2$: two real fields with different masses. And $\phi^2 - \phi^{\ast 2} = 2i\phi_1\phi_2$, so $X = \delta\mathcal L/\alpha = 2\lambda\phi_1\phi_2$.
>
> **Step 3** (not a divergence). Take $\phi_1 = \phi_2 = f \ge 0$, a bump: $\int 2\lambda f^2 \neq 0$, while a divergence integrates to the flux of the zero configuration, $0$. Outcome (iii).
>
> **Step 4** (from $\delta\mathcal L$). The new term has no derivatives, so the current of W6 is unchanged, and on solutions $\partial_\mu j^\mu = X = -i\lambda(\phi^2 - \phi^{\ast 2}) = 2\lambda\phi_1\phi_2$.
>
> **Step 5** (from the field equations). $\partial^2\phi = \partial\mathcal L/\partial\phi^{\ast} = -m^2\phi - \lambda\phi^{\ast}$ and $\partial^2\phi^{\ast} = -m^2\phi^{\ast} - \lambda\phi$. With W6, Step 4: $\partial_\mu j^\mu = i(\phi\,\partial^2\phi^{\ast} - \phi^{\ast}\partial^2\phi) = i(-\lambda\phi^2 + \lambda\phi^{\ast 2}) = -i\lambda(\phi^2 - \phi^{\ast 2})$, the mass terms cancelling. In real components: $\partial_\mu(\phi_1\partial^\mu\phi_2 - \phi_2\partial^\mu\phi_1) = (m_1^2 - m_2^2)\phi_1\phi_2 = 2\lambda\phi_1\phi_2$. Both agree; $dQ/dt = 2\lambda\int d^3x\,\phi_1\phi_2$.
>
> **(b) Step 1** ($\delta\mathcal L$). $(e^{i\alpha}\phi)^3 = \phi^3 + 3i\alpha\phi^3 + O(\alpha^2)$, $(e^{-i\alpha}\phi^{\ast})^3 = \phi^{\ast 3} - 3i\alpha\phi^{\ast 3} + O(\alpha^2)$: $\delta\mathcal L = -3i\alpha g(\phi^3 - \phi^{\ast 3}) = 6\alpha g\,\mathrm{Im}(\phi^3)$ (using $\phi^3 - \phi^{\ast 3} = 2i\,\mathrm{Im}\,\phi^3$).
>
> **Step 2** (not a divergence). Take $\phi = e^{i\pi/6}f$ with a bump $f \ge 0$: $\phi^3 = i f^3$, $\int 6g f^3 \neq 0$. So $X = -3ig(\phi^3 - \phi^{\ast 3})$ and $\partial_\mu j^\mu = X$ on solutions.
>
> **Step 3** (direct check). $\partial\mathcal L/\partial\phi^{\ast} = -m^2\phi - 3g\phi^{\ast 2}$, so $\partial^2\phi = -m^2\phi - 3g\phi^{\ast 2}$ and $\partial^2\phi^{\ast} = -m^2\phi^{\ast} - 3g\phi^2$. Then $i(\phi\,\partial^2\phi^{\ast} - \phi^{\ast}\partial^2\phi) = i(-3g\phi^3 + 3g\phi^{\ast 3}) = -3ig(\phi^3 - \phi^{\ast 3})$: the same.
>
> **Step 4** (the finite remnant). The cubic term is invariant when $e^{3i\alpha} = 1$, $\alpha \in \frac{2\pi}{3}\mathbb Z$. These form a discrete group $\mathbb Z_3$ that contains no transformation near the identity, so there is no generator $\Delta\phi$, no first-order test and no Noether current: the charge is conserved only modulo 3 in processes (each term changes $\hat N_a - \hat N_b$ by $\pm3$ after quantization), not as a local continuity equation.
>
> *Checked against:* (a) [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|Example §C1b.6.3]] (the same $\delta\mathcal L$, $X = 2\lambda\phi_1\phi_2$, both checks, $dQ/dt$). *Derived here; check:* (b) by the field equations (Step 3) against [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]]; that discrete symmetries give no current is [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-2|§C1b.6, Caution: What the theorem does and does not say]] and [[§C1b.5 Noether's Theorem#^thm-c1b-5-3|Theorem §C1b.5.3]] (a continuous family is decided by its generator). The remark on $\hat N_a - \hat N_b$ mod 3 is a reading of the term, not a box.

^sol-wn-7

### W8. Translations and Lorentz transformations of the complex scalar

![[PHY 513 Worksheet — Noether Currents#^wn-8]]

![[PHY 513 Worksheet — Noether Currents#^wn-8-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-8-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-8-c]]

> [!success]- Solution
> **Answers.** (a) $T^{\mu\nu} = \partial^\mu\phi^{\ast}\partial^\nu\phi + \partial^\mu\phi\,\partial^\nu\phi^{\ast} - g^{\mu\nu}\mathcal L$, symmetric. (b) $\mathbf P = -\int d^3x\,(\pi\nabla\phi + \pi^{\ast}\nabla\phi^{\ast}) = -\int d^3x\,(\dot\phi^{\ast}\nabla\phi + \dot\phi\,\nabla\phi^{\ast})$. (c) $\mathcal M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$: both $\phi$ and $\phi^{\ast}$ are Lorentz scalars.
>
> **(a)** $\Delta_\nu\phi = \partial_\nu\phi$, $\Delta_\nu\phi^{\ast} = \partial_\nu\phi^{\ast}$, $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ as in W3. With $\partial\mathcal L/\partial(\partial_\mu\phi) = \partial^\mu\phi^{\ast}$ and $\partial\mathcal L/\partial(\partial_\mu\phi^{\ast}) = \partial^\mu\phi$, one term per field: $T^\mu{}_\nu = \partial^\mu\phi^{\ast}\partial_\nu\phi + \partial^\mu\phi\,\partial_\nu\phi^{\ast} - \delta^\mu{}_\nu\mathcal L$, and raising $\nu$ gives the answer. Exchanging $\mu \leftrightarrow \nu$ swaps the first two terms: symmetric.
>
> **(b) Step 1** ($T^{00}$). $\partial_\mu\phi^{\ast}\partial^\mu\phi = \dot\phi^{\ast}\dot\phi - \nabla\phi^{\ast}\cdot\nabla\phi$, so $T^{00} = 2\dot\phi^{\ast}\dot\phi - \mathcal L = \dot\phi^{\ast}\dot\phi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi = \pi^{\ast}\pi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi = \mathcal H$, with $\pi = \partial\mathcal L/\partial\dot\phi = \dot\phi^{\ast}$, $\pi^{\ast} = \dot\phi$.
>
> **Step 2** ($T^{0i}$). $g^{0i} = 0$, $\partial^i = -\partial_i$: $T^{0i} = \dot\phi^{\ast}\partial^i\phi + \dot\phi\,\partial^i\phi^{\ast} = -(\pi\,\partial_i\phi + \pi^{\ast}\partial_i\phi^{\ast})$, one term per canonical pair, so $\mathbf P = -\int d^3x\,(\pi\nabla\phi + \pi^{\ast}\nabla\phi^{\ast})$. The two terms are complex conjugates of each other, so $\mathbf P$ is real; in $\phi = (\phi_1 + i\phi_2)/\sqrt2$ it is the sum of two real-field momenta.
>
> **(c)** The spin part of [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]] is $\sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}(S^{\nu\rho})_a{}^b\phi_b$, and $S^{\nu\rho}$ acts on Lorentz indices. $\phi$ and $\phi^{\ast}$ are each a scalar, $\phi'(x') = \phi(x)$, so $S^{\nu\rho} = 0$ for both and $\mathcal M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}$, conserved because $T$ is symmetric (W4(b)). The two real components are an internal label (the U(1) of W6), not a spacetime index: a spin current needs components that the Lorentz group mixes.
>
> *Checked against:* [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-3|§C1b.7, Remark: The canonical tensor of the standard fields]] (complex row: $T^{\mu\nu}$, symmetric, $T^{00}$); [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-8|Theorem §C1b.7.8]] ($H$, $\mathbf P$); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]] and [[§C1b.5 Noether's Theorem#^rem-c1b-5-8|§C1b.5, Remark: What the sum over fields runs over]] (c). The mode form of $\hat{\mathbf P}$ is [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]].

^sol-wn-8

## The Dirac field

### W9. The vector U(1)

![[PHY 513 Worksheet — Noether Currents#^wn-9]]

![[PHY 513 Worksheet — Noether Currents#^wn-9-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-9-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-9-c]]

> [!success]- Solution
> **Answers.** (a) $\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$; $\delta\mathcal L = 0$, with the $\bar\psi$ term $\bar\psi\gamma^\mu\partial_\mu\psi + im\,\bar\psi\psi$ needed for the cancellation. (b) $j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$, conserved for every $m$; Peskin–Schroeder's $j^\mu = \bar\psi\gamma^\mu\psi = -j^\mu_{\rm N}$. (c) $\bar\psi\gamma^0\psi = \psi^\dagger\psi = \sum_a\lvert\psi_a\rvert^2 \ge 0$; $\hat Q = \hat N_a - \hat N_b$.
>
> **(a) Step 1** (generators). $\psi' = e^{i\alpha}\psi$ and, for real $\alpha$, $\bar\psi' = (e^{i\alpha}\psi)^\dagger\gamma^0 = e^{-i\alpha}\bar\psi$: $\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$.
>
> **Step 2** (the derivatives of $\mathcal L$). In components $\mathcal L = \bar\psi_a\bigl[i(\gamma^\nu)_{ab}\partial_\nu\psi_b - m\psi_a\bigr]$: $\partial\mathcal L/\partial\psi_c = -m\bar\psi_c$, $\partial\mathcal L/\partial(\partial_\mu\psi_c) = i(\bar\psi\gamma^\mu)_c$, $\partial\mathcal L/\partial\bar\psi_a = [(i\gamma^\nu\partial_\nu - m)\psi]_a$, $\partial\mathcal L/\partial(\partial_\mu\bar\psi_a) = 0$.
>
> **Step 3** (Route 2, divided by $\alpha$). Over the eight variables $\psi_c$, $\bar\psi_a$:
> - $\sum_c(-m\bar\psi_c)(i\psi_c) = -im\,\bar\psi\psi$;
> - $\sum_ci(\bar\psi\gamma^\mu)_c(i\,\partial_\mu\psi_c) = -\bar\psi\gamma^\mu\partial_\mu\psi$;
> - $\sum_a(-i\bar\psi_a)[(i\gamma^\nu\partial_\nu - m)\psi]_a = \bar\psi\gamma^\nu\partial_\nu\psi + im\,\bar\psi\psi$;
> - no $\partial_\mu\bar\psi$ term.
>
> The sum is $0$ (rename $\nu \to \mu$). Dropping the third term, because $\bar\psi$ has no derivative in $\mathcal L$, would leave $-im\,\bar\psi\psi - \bar\psi\gamma^\mu\partial_\mu\psi \neq 0$ and a false "broken symmetry". Route 1 agrees at once: $e^{-i\alpha}e^{i\alpha} = 1$ in every term.
>
> **(b) Step 1** (current). Outcome (i), $\mathcal J^\mu = 0$. Only $\psi$ has a derivative in $\mathcal L$, so $j^\mu_{\rm N} = i\bar\psi\gamma^\mu(i\psi) + 0 = -\bar\psi\gamma^\mu\psi$.
>
> **Step 2** (the two field equations). The Dirac equation $i\gamma^\mu\partial_\mu\psi = m\psi$ gives $\gamma^\mu\partial_\mu\psi = -im\psi$; its conjugate $i\,\partial_\mu\bar\psi\,\gamma^\mu + m\bar\psi = 0$ gives $\partial_\mu\bar\psi\,\gamma^\mu = im\bar\psi$.
>
> **Step 3** (conservation). $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi = im\,\bar\psi\psi - im\,\bar\psi\psi = 0$, for every $m$. One equation per field is used.
>
> **Step 4** (versus PS). Peskin–Schroeder (3.73) call $j^\mu = \bar\psi\gamma^\mu\psi$ the Noether current of $\psi \to e^{i\alpha}\psi$; the recipe with $\Delta\psi = +i\psi$ gives its negative, exactly as for the complex scalar. A constant multiple of a conserved current is conserved; the conventional sign makes the classical charge positive.
>
> **(c)** $j^0 = \bar\psi\gamma^0\psi = \psi^\dagger(\gamma^0)^2\psi = \psi^\dagger\psi = \sum_a\lvert\psi_a\rvert^2 \ge 0$, a probability-like density; the scalar's $j^0$ was indefinite (W6(b)). After quantization with anticommutators the $\hat b\hat b^\dagger$ term is reordered with the fermion sign, $:\!\hat b\hat b^\dagger\!: = -\hat b^\dagger\hat b$, and $\hat Q = \int d^3x\,:\!\hat\psi^\dagger\hat\psi\!: = \sum_s\int\frac{d^3p}{(2\pi)^3}(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}) = \hat N_a - \hat N_b$: fermions minus antifermions, either sign.
>
> *Checked against:* [[§C1b.5 Noether's Theorem#^ex-c1b-5-2|Example §C1b.5.2]] (both routes, the four terms, the role of term (c)); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]] ($j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$, the direct check, $Q \ge 0$); [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]] ($\hat Q = \hat N_a - \hat N_b$); Peskin–Schroeder p. 50, eq. (3.73), and p. 51, eq. (3.74) (read on the page).

^sol-wn-9

### W10. The chiral rotation and its breaking by the mass

![[PHY 513 Worksheet — Noether Currents#^wn-10]]

![[PHY 513 Worksheet — Noether Currents#^wn-10-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-10-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-10-c]]

> [!success]- Solution
> **Answers.** (a) $j^\mu_5 = -\bar\psi\gamma^\mu\gamma^5\psi = -\mathsf A^\mu$. (b) $\partial_\mu j^\mu_5 = -2im\,\bar\psi\gamma^5\psi = -2m\,\mathsf P$. (c) $\partial_\mu\mathsf A^\mu = 2im\,\bar\psi\gamma^5\psi = 2m\,\mathsf P$, exactly Peskin–Schroeder (3.75); $dQ_5/dt = 2m\int d^3x\,\mathsf P$.
>
> **(a) Step 1** (generators). $\Delta\psi = \frac{d}{d\alpha}e^{i\alpha\gamma^5}\psi\big|_0 = i\gamma^5\psi$; from $\bar\psi' = \bar\psi e^{i\alpha\gamma^5}$, $\Delta\bar\psi = i\bar\psi\gamma^5$.
>
> **Step 2** (test). For $m = 0$, $\delta\mathcal L = 0$ (given, 5(c)): $\mathcal J^\mu = 0$.
>
> **Step 3** (current). The eight fields $\psi_a$, $\bar\psi_a$ are independent; $\partial\mathcal L/\partial(\partial_\mu\psi_a) = (i\bar\psi\gamma^\mu)_a$ and $\partial\mathcal L/\partial(\partial_\mu\bar\psi_a) = 0$. Row times column:
>
> $$
> j^\mu_5 = \sum_a(i\bar\psi\gamma^\mu)_a(i\gamma^5\psi)_a = -\bar\psi\gamma^\mu\gamma^5\psi .
> $$
>
> The mass term has no derivatives, so the same expression is the would-be current for every $m$.
>
> **(b) Step 1** (product rule). $\partial_\mu j^\mu_5 = -(\partial_\mu\bar\psi)\gamma^\mu\gamma^5\psi - \bar\psi\gamma^\mu\gamma^5\partial_\mu\psi = -\bigl((\partial_\mu\bar\psi)\gamma^\mu\bigr)\gamma^5\psi + \bar\psi\gamma^5\bigl(\gamma^\mu\partial_\mu\psi\bigr)$, using $\gamma^\mu\gamma^5 = -\gamma^5\gamma^\mu$ in the second term.
>
> **Step 2** (the two Dirac equations). $\gamma^\mu\partial_\mu\psi = \frac mi\psi$; the Hermitian conjugate times $\gamma^0$, with $\gamma^0\gamma^{\mu\dagger}\gamma^0 = \gamma^\mu$, gives $-i(\partial_\mu\bar\psi)\gamma^\mu = m\bar\psi$, i.e. $(\partial_\mu\bar\psi)\gamma^\mu = -\frac mi\bar\psi$.
>
> **Step 3** (result). $\partial_\mu j^\mu_5 = \frac mi\bar\psi\gamma^5\psi + \frac mi\bar\psi\gamma^5\psi = \frac{2m}{i}\bar\psi\gamma^5\psi = -2im\,\bar\psi\gamma^5\psi$; zero for $m = 0$.
>
> **Step 4** (not identically zero for $m \neq 0$). In the chiral basis $\bar\psi\gamma^5\psi = \psi_L^\dagger\psi_R - \psi_R^\dagger\psi_L$; for $\psi_R = i\psi_L \neq 0$ it is $2i\,\psi_L^\dagger\psi_L \neq 0$, a value that can be prescribed as initial data at a point.
>
> **(c) Step 1** (the course's axial current). $\mathsf A^\mu = -j^\mu_5$, so $\partial_\mu\mathsf A^\mu = 2im\,\bar\psi\gamma^5\psi = 2m\,\mathsf P$ with $\mathsf P = \bar\psi\,i\gamma^5\psi$ real. Peskin–Schroeder (3.75) is $\partial_\mu j^{\mu5} = 2im\,\bar\psi\gamma^5\psi$ for $j^{\mu5} = \bar\psi\gamma^\mu\gamma^5\psi$ (3.73), with the same $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ (3.68): identical. What differs is only that PS call $j^{\mu5}$ the Noether current of $e^{i\alpha\gamma^5}$, while the recipe gives $-j^{\mu5}$, as for the vector current (W9(b)).
>
> **Step 2** (check against $\delta\mathcal L$). $\delta\mathcal L = -2i\alpha m\,\bar\psi\gamma^5\psi$ contains no derivatives, so it is no divergence for $m \neq 0$: $\mathcal J = 0$, $X = -2im\,\bar\psi\gamma^5\psi$, and [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]] predicts $\partial_\mu j^\mu_5 = X$ on solutions, which is (b).
>
> **Step 3** (axial charge). $Q_5 = \int d^3x\,\mathsf A^0 = \int d^3x\,\psi^\dagger\gamma^5\psi$; integrating $\partial_\mu\mathsf A^\mu = 2m\mathsf P$ over space and dropping the flux, $dQ_5/dt = 2m\int d^3x\,\mathsf P = 2im\int d^3x\,\bar\psi\gamma^5\psi$. The mass is the rate at which axial charge is created.
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|Example §C5a.8.1]] (results 4–5, $j^\mu_5 = -\mathsf A^\mu$, $\partial_\mu j^\mu_5 = -2im\,\bar\psi\gamma^5\psi$, the $\psi_R = i\psi_L$ example); its derivations are the user's Problem Set 6, Problem 5(d)–(e), as written; [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|Theorem §C5a.8.4]] ($\partial_\mu j^{\mu5} = 2im\,\bar\psi\gamma^5\psi$); Peskin–Schroeder p. 51, eq. (3.75), and p. 50, eqs. (3.68), (3.73) (read on the page).

^sol-wn-10

### W11. Left and right currents

![[PHY 513 Worksheet — Noether Currents#^wn-11]]

![[PHY 513 Worksheet — Noether Currents#^wn-11-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-11-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-11-c]]

> [!success]- Solution
> **Answers.** (a) $j^\mu_{L,{\rm N}} = -\bar\psi\gamma^\mu P_L\psi = -\psi_L^\dagger\bar\sigma^\mu\psi_L$, $j^\mu_{R,{\rm N}} = -\bar\psi\gamma^\mu P_R\psi = -\psi_R^\dagger\sigma^\mu\psi_R$. (b) $\alpha_L = \alpha_R$: the vector current $j_{L,{\rm N}} + j_{R,{\rm N}}$; $\alpha_R = -\alpha_L = \alpha$: the chiral current $j_{R,{\rm N}} - j_{L,{\rm N}}$. (c) $\delta\mathcal L = \alpha m\,\mathsf P$, $\partial_\mu j^\mu_{L,{\rm N}} = m\,\mathsf P$ and $\partial_\mu j^\mu_{R,{\rm N}} = -m\,\mathsf P$; the sum (vector) is conserved.
>
> **(a) Step 1** (the transformation in Dirac form). In the chiral basis $P_L\psi = (\psi_L, 0)$; since $P_L^2 = P_L$, $e^{i\alpha_LP_L} = \mathbb 1 + (e^{i\alpha_L} - 1)P_L$ multiplies $\psi_L$ by $e^{i\alpha_L}$ and leaves $\psi_R$. Generator $\Delta_L\psi = iP_L\psi$. For $\bar\psi$: $P_L\gamma^0 = \gamma^0P_R$ ($\gamma^5$ anticommutes with $\gamma^0$), so $\bar\psi' = \psi^\dagger e^{-i\alpha_LP_L}\gamma^0 = \bar\psi\,e^{-i\alpha_LP_R}$, $\Delta_L\bar\psi = -i\bar\psi P_R$.
>
> **Step 2** (symmetry for $m = 0$). In the Weyl form each kinetic term contains $\psi_L^\dagger\cdots\psi_L$ or $\psi_R^\dagger\cdots\psi_R$, so the phases cancel: $\delta\mathcal L = 0$, $\mathcal J = 0$, for each phase separately.
>
> **Step 3** (currents). $j^\mu_{L,{\rm N}} = i\bar\psi\gamma^\mu(iP_L\psi) = -\bar\psi\gamma^\mu P_L\psi$. With the Weyl form of the bilinear, $\bar\psi\gamma^\mu\chi = \psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R$ at $\chi = P_L\psi = (\psi_L, 0)$: $j^\mu_{L,{\rm N}} = -\psi_L^\dagger\bar\sigma^\mu\psi_L$. The same from the Weyl Lagrangian: $\partial\mathcal L/\partial(\partial_\mu\psi_L) = i\psi_L^\dagger\bar\sigma^\mu$ times $\Delta\psi_L = i\psi_L$. Likewise $j^\mu_{R,{\rm N}} = -\bar\psi\gamma^\mu P_R\psi = -\psi_R^\dagger\sigma^\mu\psi_R$. The conventional-sign currents are $j^\mu_{L,R} = \bar\psi\gamma^\mu P_{L,R}\psi$, Peskin–Schroeder (3.76).
>
> **(b)** The current is linear in the generator. $\alpha_L = \alpha_R = \alpha$: $\Delta\psi = i(P_L + P_R)\psi = i\psi$, the vector phase, $j_{\rm N} = j_{L,{\rm N}} + j_{R,{\rm N}} = -\bar\psi\gamma^\mu\psi$ (W9). The chiral rotation is $e^{i\alpha\gamma^5} = e^{-i\alpha}P_L + e^{i\alpha}P_R$, i.e. $\alpha_L = -\alpha$, $\alpha_R = \alpha$: $\Delta\psi = i(P_R - P_L)\psi = i\gamma^5\psi$ and $j_{5,{\rm N}} = j_{R,{\rm N}} - j_{L,{\rm N}} = -\bar\psi\gamma^\mu(P_R - P_L)\psi = -\bar\psi\gamma^\mu\gamma^5\psi$ (W10).
>
> **(c) Step 1** ($\delta\mathcal L$ for the left phase, $m \neq 0$). The kinetic terms are invariant (Step 2 of (a)). Mass term: $\psi_L^\dagger\psi_R \to e^{-i\alpha}\psi_L^\dagger\psi_R$, $\psi_R^\dagger\psi_L \to e^{i\alpha}\psi_R^\dagger\psi_L$, so $\delta\mathcal L = -m(-i\alpha\,\psi_L^\dagger\psi_R + i\alpha\,\psi_R^\dagger\psi_L) = \alpha m\cdot i(\psi_L^\dagger\psi_R - \psi_R^\dagger\psi_L) = \alpha m\,\mathsf P$, using $\bar\psi\,i\gamma^5\psi = i(\psi_L^\dagger\psi_R - \psi_R^\dagger\psi_L)$.
>
> **Step 2** (divergences). No derivatives in $\delta\mathcal L$: $\mathcal J = 0$, $X_L = m\,\mathsf P$, so $\partial_\mu j^\mu_{L,{\rm N}} = m\,\mathsf P$ on solutions. For the right phase the two exponentials are reversed: $\delta\mathcal L = -\alpha m\,\mathsf P$ and $\partial_\mu j^\mu_{R,{\rm N}} = -m\,\mathsf P$.
>
> **Step 3** (consistency). Sum: $\partial_\mu(j_{L,{\rm N}} + j_{R,{\rm N}})^\mu = 0$, the vector current of W9, conserved for every $m$. Difference: $\partial_\mu(j_{R,{\rm N}} - j_{L,{\rm N}})^\mu = -2m\,\mathsf P = -2im\,\bar\psi\gamma^5\psi$, W10(b). In the conventional sign, $\partial_\mu j^\mu_L = -m\,\mathsf P$: half of $\partial_\mu(\mathsf V - \mathsf A)^\mu = -2m\,\mathsf P$. The mass is the only term that pairs $\psi_L$ with $\psi_R$, so it breaks $U(1)_L\times U(1)_R$ to the diagonal $U(1)$.
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|Theorem §C5a.8.4]] (the chiral currents $j^\mu_{L,R} = \bar\psi\gamma^\mu P_{L,R}\psi$ in Weyl form, separately conserved for $m = 0$; $\partial_\mu j^{\mu5} = 2im\,\bar\psi\gamma^5\psi$, which gives $\partial_\mu j^\mu_L = -m\,\mathsf P$); [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-9|Theorem §C5a.7.9]] (Weyl forms of $\mathcal L$, $\bar\psi\gamma^\mu\chi$ and $\bar\psi\,i\gamma^5\chi$); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^ex-c5a-8-1|Example §C5a.8.1]] ($\delta\mathcal L = -2\alpha m\,\mathsf P$ for the chiral rotation $= R - L$). The left-phase $\delta\mathcal L$ itself is derived here.

^sol-wn-11

### W12. Translations: the Dirac energy–momentum tensor

![[PHY 513 Worksheet — Noether Currents#^wn-12]]

![[PHY 513 Worksheet — Noether Currents#^wn-12-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-12-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-12-c]]

> [!success]- Solution
> **Answers.** (a) $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L$; $\partial\mathcal L/\partial(\partial_\mu\bar\psi) = 0$. (b) conserved on solutions. (c) $\mathbf P = \int d^3x\,\psi^\dagger(-i\nabla)\psi$; $H = \int d^3x\,\psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi \overset{\text{on shell}}{=} \int d^3x\,\psi^\dagger i\partial_t\psi$.
>
> **(a)** Every component translates the same way: $\Delta_\nu\psi = \partial_\nu\psi$, $\Delta_\nu\bar\psi = \partial_\nu\bar\psi$. $\mathcal L$ has no explicit $x$, so $\delta\mathcal L = a^\nu\partial_\nu\mathcal L = a^\nu\partial_\mu(\delta^\mu{}_\nu\mathcal L)$ and $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ (as in W3). Summing over both fields: $T^\mu{}_\nu = i\bar\psi\gamma^\mu\partial_\nu\psi + 0\cdot\partial_\nu\bar\psi - \delta^\mu{}_\nu\mathcal L$; raising $\nu$ gives the stated $T^{\mu\nu}$. $\bar\psi$ contributes nothing to the first term because $\mathcal L$ contains no derivative of $\bar\psi$ (its role is only in $\delta\mathcal L$, cf. W9(a)).
>
> **(b) Step 1** (divergence). Rename the dummy in $\mathcal L = \bar\psi(i\gamma^\rho\partial_\rho - m)\psi$; with $\partial_\mu g^{\mu\nu} = 0$ and $g^{\mu\nu}\partial_\mu = \partial^\nu$,
>
> $$
> \partial_\mu T^{\mu\nu} = i(\partial_\mu\bar\psi)\gamma^\mu\partial^\nu\psi + i\bar\psi\gamma^\mu\partial_\mu\partial^\nu\psi - (\partial^\nu\bar\psi)(i\gamma^\rho\partial_\rho - m)\psi - \bar\psi(i\gamma^\rho\partial_\rho - m)\partial^\nu\psi .
> $$
>
> **Step 2** (the equations). $i(\partial_\mu\bar\psi)\gamma^\mu = -m\bar\psi$ turns the first term into $-m\bar\psi\,\partial^\nu\psi$; $(i\gamma^\rho\partial_\rho - m)\psi = 0$ kills the third.
>
> **Step 3** (collect). The last term is $-i\bar\psi\gamma^\rho\partial_\rho\partial^\nu\psi + m\bar\psi\,\partial^\nu\psi$. The mass terms cancel, and $i\bar\psi\gamma^\mu\partial_\mu\partial^\nu\psi - i\bar\psi\gamma^\rho\partial_\rho\partial^\nu\psi = 0$ ($\mu$, $\rho$ dummies): $\partial_\mu T^{\mu\nu} = 0$. Both equations of motion are used, one per field.
>
> **(c) Step 1** (momentum). $T^{0i} = i\bar\psi\gamma^0\partial^i\psi - g^{0i}\mathcal L = i\psi^\dagger\partial^i\psi = -i\psi^\dagger\partial_i\psi$ ($\bar\psi\gamma^0 = \psi^\dagger$, $g^{0i} = 0$, $\partial^i = -\partial_i$). So
>
> $$
> \mathbf P = \int d^3x\;\psi^\dagger(-i\nabla)\psi = -\int d^3x\;\pi_\psi\nabla\psi, \qquad \pi_\psi = i\psi^\dagger ,
> $$
>
> the Noether charge of spatial translations, not the canonical momentum $\pi_\psi$.
>
> **Step 2** (energy). $T^{00} = i\psi^\dagger\partial_t\psi - \mathcal L$, and $\mathcal L = \bar\psi(i\gamma^0\partial_0 + i\gamma^j\partial_j - m)\psi = i\psi^\dagger\partial_t\psi + \bar\psi(i\gamma^j\partial_j - m)\psi$. So, for every configuration, $T^{00} = \bar\psi(-i\gamma^j\partial_j + m)\psi = \psi^\dagger\gamma^0(-i\gamma^j\partial_j + m)\psi = \psi^\dagger(-i\alpha^j\partial_j + \beta m)\psi$. On solutions $\mathcal L = 0$ (the Dirac equation inside $\mathcal L$), so $T^{00} = \psi^\dagger i\partial_t\psi$ there.
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-5|Theorem §C5a.8.5]] ($T^{\mu\nu}$; its derivation is the user's Problem Set 5, Problem 4(a), as written); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-6|Theorem §C5a.8.6]] ($H$, $\mathbf P$, $T^{0i} = -\pi_\psi\partial_i\psi$; the user's Problem Set 5, Problem 4(b), as written); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|Theorem §C5a.8.2]] ($\mathcal H = \psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$); [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^thm-c1b-7-5|Theorem §C1b.7.5]] ($\mathcal J^\mu{}_\nu$).

^sol-wn-12

### W13. Lorentz transformations: the Dirac spin current

![[PHY 513 Worksheet — Noether Currents#^wn-13]]

![[PHY 513 Worksheet — Noether Currents#^wn-13-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-13-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-13-c]]

> [!success]- Solution
> **Answers.** (a) $\mathcal S^{\lambda\mu\nu} = \bar\psi\gamma^\lambda S^{\mu\nu}\psi = \frac i4\bar\psi\gamma^\lambda[\gamma^\mu, \gamma^\nu]\psi$. (b) spin part $\int\psi^\dagger\frac12\boldsymbol\Sigma\psi$, orbital part $\int\psi^\dagger\,\mathbf x\times(-i\nabla)\,\psi$. (c) no: $dS^{jk}/dt = \int d^3x\,(T^{kj} - T^{jk}) = -dL^{jk}/dt$; only $\mathbf J$ is conserved.
>
> **(a) Step 1** (the generator in the real convention). The general theorem writes $D = 1 + \frac12\omega_{\mu\nu}S^{\mu\nu}_{\rm real}$; the spinor law has $D = \Lambda_{1/2} = 1 - \frac i2\omega_{\mu\nu}S^{\mu\nu}$. Both generators are antisymmetric and $\omega$ is arbitrary antisymmetric, so $S^{\mu\nu}_{\rm real} = -iS^{\mu\nu}$.
>
> **Step 2** (spin current). $\mathcal S^{\lambda\mu\nu} = \sum_a\frac{\partial\mathcal L}{\partial(\partial_\lambda\phi_a)}(S^{\mu\nu}_{\rm real}\phi)_a$ over $\psi$ and $\bar\psi$; the $\bar\psi$ term is zero, and the $\psi$ term is $i\bar\psi\gamma^\lambda(-iS^{\mu\nu}\psi) = \bar\psi\gamma^\lambda S^{\mu\nu}\psi$. The orbital part $x^\mu T^{\lambda\nu} - x^\nu T^{\lambda\mu}$ comes with the canonical $T$ of W12.
>
> **(b) Step 1** (spin charges). $\int d^3x\,\mathcal S^{0\mu\nu} = \int d^3x\,\bar\psi\gamma^0S^{\mu\nu}\psi = \int d^3x\,\psi^\dagger S^{\mu\nu}\psi$. With $S^{jk} = \frac12\varepsilon^{jkl}\Sigma^l$: $\frac12\varepsilon_{ijk}S^{jk} = \frac14\varepsilon_{ijk}\varepsilon_{jkl}\Sigma^l = \frac14\cdot2\delta_{il}\Sigma^l = \frac12\Sigma^i$ ($\varepsilon_{jkl} = \varepsilon_{ljk}$ and $\varepsilon_{ijk}\varepsilon_{ljk} = 2\delta_{il}$). Spin part of $J^i$: $\int d^3x\,\psi^\dagger\frac12\Sigma^i\psi$.
>
> **Step 2** (orbital charges). $T^{0k} = i\psi^\dagger\partial^k\psi = -i\psi^\dagger\partial_k\psi$ (W12(c); no $\mathcal L$ term since $g^{0k} = 0$). $L^{jk} = \int d^3x\,(x^jT^{0k} - x^kT^{0j}) = \int d^3x\,\psi^\dagger(-i)(x^j\partial_k - x^k\partial_j)\psi$, and $\frac12\varepsilon_{ijk}L^{jk} = \int d^3x\,\psi^\dagger(-i)\varepsilon_{ijk}x^j\partial_k\psi = \int d^3x\,\psi^\dagger\bigl(\mathbf x\times(-i\nabla)\bigr)_i\psi$, the two halves equal after $j \leftrightarrow k$.
>
> **Step 3** (total). $J^i = L^i + S^i$ gives $\mathbf J = \int d^3x\,\psi^\dagger\bigl(\mathbf x\times(-i\nabla) + \frac12\boldsymbol\Sigma\bigr)\psi$: orbital plus spin $\frac12$ ($\frac12\Sigma^i\frac12\Sigma^i = \frac34\mathbb 1$).
>
> **(c)** Conservation of $\mathcal M$ with $\partial_\lambda(x^\mu T^{\lambda\nu}) = T^{\mu\nu}$ gives $\partial_\lambda\mathcal S^{\lambda\mu\nu} = T^{\nu\mu} - T^{\mu\nu}$. For the Dirac field $T^{jk} - T^{kj} = i\bar\psi(\gamma^j\partial^k - \gamma^k\partial^j)\psi \neq 0$ in general (W12: $T$ is not symmetric). Integrating over space with $(\mu, \nu) = (j, k)$ and dropping the flux $\int\partial_i\mathcal S^{ijk}$: $dS^{jk}/dt = \int d^3x\,(T^{kj} - T^{jk})$, and since $J^{jk}$ is conserved, $dL^{jk}/dt = -dS^{jk}/dt$. Only the total is conserved; Belinfante's symmetric tensor absorbs the spin into the orbital moment ([[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-9|Theorem §C5a.8.9]]).
>
> *Checked against:* [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-8|Theorem §C5a.8.8]] ($\mathcal S^{\lambda\mu\nu}$, the conversion $S_{\rm real} = -iS$, $\mathbf J$); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-1|Theorem §C1b.8.1]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-2|Theorem §C1b.8.2]] (c); the vector-field analogue of (c) is [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-6|Theorem §C4.1.6]].

^sol-wn-13

### W14. A Lagrangian changed by a total derivative

![[PHY 513 Worksheet — Noether Currents#^wn-14]]

![[PHY 513 Worksheet — Noether Currents#^wn-14-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-14-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-14-c]]

> [!success]- Solution
> **Answers.** (a) by the product rule; a total divergence of a function of the fields does not change the Euler–Lagrange equations. (b) $j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$, the same. (c) $T^{\mu\nu}_{\rm sym} - T^{\mu\nu} = \partial_\lambda B^{\lambda\mu\nu}$, $B^{\lambda\mu\nu} = \frac i2(g^{\mu\nu}\mathsf V^\lambda - g^{\lambda\nu}\mathsf V^\mu)$; same $P^\nu$; $T_{\rm sym}$ is still not symmetric (its symmetric part on shell is Belinfante's $T_B$).
>
> **(a)** $\partial_\mu(\bar\psi\gamma^\mu\psi) = \partial_\mu\bar\psi\,\gamma^\mu\psi + \bar\psi\gamma^\mu\partial_\mu\psi$, so $\mathcal L - \frac i2\partial_\mu(\bar\psi\gamma^\mu\psi) = i\bar\psi\gamma^\mu\partial_\mu\psi - \frac i2\partial_\mu\bar\psi\,\gamma^\mu\psi - \frac i2\bar\psi\gamma^\mu\partial_\mu\psi - m\bar\psi\psi = \mathcal L_{\rm sym}$. The added term is $\partial_\mu K^\mu$ with $K^\mu = -\frac i2\bar\psi\gamma^\mu\psi$ a function of the fields only; its integral is a boundary term, so both Lagrangians have the same first variation and the same field equations.
>
> **(b) Step 1** (derivatives). Now both fields carry derivatives: $\partial\mathcal L_{\rm sym}/\partial(\partial_\mu\psi_a) = \frac i2(\bar\psi\gamma^\mu)_a$ and $\partial\mathcal L_{\rm sym}/\partial(\partial_\mu\bar\psi_a) = -\frac i2(\gamma^\mu\psi)_a$.
>
> **Step 2** (current). Every term pairs one $\bar\psi$ with one $\psi$, so $\delta\mathcal L_{\rm sym} = 0$, $\mathcal J = 0$. With $\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$:
>
> $$
> j^\mu = \tfrac i2\bar\psi\gamma^\mu(i\psi) + \sum_a\bigl(-\tfrac i2\gamma^\mu\psi\bigr)_a(-i\bar\psi_a) = -\tfrac12\bar\psi\gamma^\mu\psi - \tfrac12\bar\psi\gamma^\mu\psi = -\bar\psi\gamma^\mu\psi ,
> $$
>
> the current of W9: half now comes from $\bar\psi$.
>
> **Step 3** (in general). Let $\mathcal L' = \mathcal L + \partial_\mu K^\mu(\phi)$ and an internal symmetry ($x$ fixed). Then $\partial(\partial_\nu K^\nu)/\partial(\partial_\mu\phi_i) = \partial K^\mu/\partial\phi_i$, so $\pi'^\mu_i = \pi^\mu_i + \partial K^\mu/\partial\phi_i$; and $\delta\mathcal L' = \delta\mathcal L + \partial_\mu(\delta K^\mu)$ with $\delta K^\mu = \alpha\sum_i(\partial K^\mu/\partial\phi_i)\Delta\phi_i$, so $\mathcal J'^\mu = \mathcal J^\mu + \sum_i(\partial K^\mu/\partial\phi_i)\Delta\phi_i$. In $j' = \sum_i\pi'^\mu_i\Delta\phi_i - \mathcal J'^\mu$ the two extra terms cancel: $j' = j$. (Here $\sum_i(\partial K^\mu/\partial\phi_i)\Delta\phi_i = -\frac i2(-i + i)\bar\psi\gamma^\mu\psi = 0$, consistent with $\mathcal J' = 0$.)
>
> **(c) Step 1** ($T_{\rm sym}$). $T^{\mu\nu}_{\rm sym} = \frac i2\bar\psi\gamma^\mu\partial^\nu\psi - \frac i2(\partial^\nu\bar\psi)\gamma^\mu\psi - g^{\mu\nu}\mathcal L_{\rm sym}$.
>
> **Step 2** (difference). With $\mathsf V^\mu = \bar\psi\gamma^\mu\psi$ and $\mathcal L - \mathcal L_{\rm sym} = \frac i2\partial_\lambda\mathsf V^\lambda$:
>
> $$
> T^{\mu\nu}_{\rm sym} - T^{\mu\nu} = -\tfrac i2\bar\psi\gamma^\mu\partial^\nu\psi - \tfrac i2(\partial^\nu\bar\psi)\gamma^\mu\psi + \tfrac i2g^{\mu\nu}\partial_\lambda\mathsf V^\lambda = \tfrac i2\bigl(g^{\mu\nu}\partial_\lambda\mathsf V^\lambda - \partial^\nu\mathsf V^\mu\bigr) = \partial_\lambda B^{\lambda\mu\nu} ,
> $$
>
> with $B^{\lambda\mu\nu} = \frac i2(g^{\mu\nu}\mathsf V^\lambda - g^{\lambda\nu}\mathsf V^\mu)$, antisymmetric under $\lambda \leftrightarrow \mu$.
>
> **Step 3** (same charges). For each $\nu$, $\partial_\mu\partial_\lambda B^{\lambda\mu\nu} = 0$ identically, and $\int d^3x\,\partial_\lambda B^{\lambda0\nu} = \int d^3x\,\partial_iB^{i0\nu}$ ($B^{00\nu} = 0$) is a surface term: $P^\nu_{\rm sym} = P^\nu$ for fields falling off at infinity. The general case: $\mathcal L' = \mathcal L + \partial_\mu K^\mu$ gives $T'^\mu{}_\nu = T^\mu{}_\nu + \partial_\nu K^\mu - \delta^\mu{}_\nu\partial_\lambda K^\lambda$, again an improvement.
>
> **Step 4** (not symmetric). On solutions $\mathcal L_{\rm sym} = 0$ and $T^{\mu\nu}_{\rm sym} = \frac i2\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi$, with $a\overleftrightarrow{\partial}b = a\,\partial b - (\partial a)b$: not symmetric in $\mu\nu$. Its symmetrization $\frac12(T^{\mu\nu}_{\rm sym} + T^{\nu\mu}_{\rm sym}) = \frac i4\bar\psi(\gamma^\mu\overleftrightarrow{\partial^\nu} + \gamma^\nu\overleftrightarrow{\partial^\mu})\psi$ is the Belinfante tensor. A total derivative moves the canonical tensor within its improvement class; it does not by itself make it symmetric.
>
> *Checked against:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^thm-c5a-7-7|Theorem §C5a.7.7]] ($\mathcal L_{\rm sym} = \mathcal L - \frac i2\partial_\mu(\bar\psi\gamma^\mu\psi)$; its derivation, step 6, notes that the canonical $T^{\mu\nu}$ changes by an improvement); [[§C1b.2 The Action Principle and the Euler–Lagrange Equations#^thm-c1b-2-5|Theorem §C1b.2.5]] (a); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]] (the current of (b)); [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]] (improvement terms, same charge); [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-9|Theorem §C5a.8.9]] ($T_B$). *Derived here:* the general statement of (b), Step 3, and the explicit $B^{\lambda\mu\nu}$; for the vector field the same freedom changes the spin charge, [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-14|Theorem §C4.6.14]].

^sol-wn-14

## The vector field

### W15. Translations and the symmetric tensor of the Maxwell field

![[PHY 513 Worksheet — Noether Currents#^wn-15]]

![[PHY 513 Worksheet — Noether Currents#^wn-15-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-15-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-15-c]]

> [!success]- Solution
> **Answers.** (a) $T^{\mu\nu} = -F^{\mu\lambda}\partial^\nu A_\lambda + \frac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma}$. (b) $\mathcal S^{\lambda\mu\nu} = F^{\lambda\nu}A^\mu - F^{\lambda\mu}A^\nu$, $K^{\lambda\mu\nu} = F^{\mu\lambda}A^\nu$, $T_B^{\mu\nu} = -F^{\mu\lambda}F^\nu{}_\lambda + \frac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma}$. (c) $\Delta T^{\mu\nu} = \partial_\lambda(F^{\lambda\mu}\partial^\nu\chi)$ on solutions.
>
> **(a) Step 1** (the derivative). Vary $A$: $\delta(-\frac14F_{\rho\sigma}F^{\rho\sigma}) = -\frac12F^{\rho\sigma}\delta F_{\rho\sigma} = -\frac12F^{\rho\sigma}(\partial_\rho\delta A_\sigma - \partial_\sigma\delta A_\rho) = -F^{\rho\sigma}\partial_\rho\delta A_\sigma$ (both factors respond; antisymmetry of $F$ doubles the first term). So $\partial\mathcal L/\partial(\partial_\mu A_\lambda) = -F^{\mu\lambda}$, and $\partial\mathcal L/\partial A_\lambda = 0$.
>
> **Step 2** (Noether). $\Delta_\nu A_\lambda = \partial_\nu A_\lambda$ for every component, $\mathcal J^\mu{}_\nu = \delta^\mu{}_\nu\mathcal L$ (no explicit $x$). Summing over the field label $\lambda$: $T^\mu{}_\nu = -F^{\mu\lambda}\partial_\nu A_\lambda + \frac14\delta^\mu{}_\nu F_{\rho\sigma}F^{\rho\sigma}$; raise $\nu$. Not symmetric, and not gauge invariant ($\partial^\nu A_\lambda$ appears bare).
>
> **(b) Step 1** (spin current). With the fields $A_\alpha$ and $(S^{\mu\nu})_\alpha{}^\beta = \delta^\mu_\alpha g^{\nu\beta} - \delta^\nu_\alpha g^{\mu\beta}$: $\mathcal S^{\lambda\mu\nu} = \sum_\alpha(-F^{\lambda\alpha})(\delta^\mu_\alpha g^{\nu\beta} - \delta^\nu_\alpha g^{\mu\beta})A_\beta = -F^{\lambda\mu}A^\nu + F^{\lambda\nu}A^\mu$.
>
> **Step 2** (Belinfante's K, term by term).
> - $\mathcal S^{\lambda\mu\nu} = -F^{\lambda\mu}A^\nu + F^{\lambda\nu}A^\mu$;
> - $\mathcal S^{\mu\nu\lambda} = -F^{\mu\nu}A^\lambda + F^{\mu\lambda}A^\nu$;
> - $\mathcal S^{\nu\mu\lambda} = -F^{\nu\mu}A^\lambda + F^{\nu\lambda}A^\mu$.
>
> Collect by the bare potential: $A^\nu$: $-F^{\lambda\mu} + F^{\mu\lambda} = 2F^{\mu\lambda}$; $A^\mu$: $F^{\lambda\nu} + F^{\nu\lambda} = 0$; $A^\lambda$: $-F^{\mu\nu} - F^{\nu\mu} = 0$. So $K^{\lambda\mu\nu} = \frac12\cdot2F^{\mu\lambda}A^\nu = F^{\mu\lambda}A^\nu$, antisymmetric in $\lambda\mu$ because $F$ is: the $K$ that Problem Set 2, Problem 4(d) hands out.
>
> **Step 3** ($T_B$). $\partial_\lambda K^{\lambda\mu\nu} = (\partial_\lambda F^{\mu\lambda})A^\nu + F^{\mu\lambda}\partial_\lambda A^\nu$, and the source-free Maxwell equation $\partial_\lambda F^{\lambda\mu} = 0$ kills the first term on solutions. Then $T_B^{\mu\nu} = -F^{\mu\lambda}(\partial^\nu A_\lambda - \partial_\lambda A^\nu) + \frac14g^{\mu\nu}F^2$, and $\partial^\nu A_\lambda - \partial_\lambda A^\nu = F^\nu{}_\lambda$:
>
> $$
> T_B^{\mu\nu} = -F^{\mu\lambda}F^\nu{}_\lambda + \tfrac14g^{\mu\nu}F_{\rho\sigma}F^{\rho\sigma} ,
> $$
>
> symmetric ($F^{\mu\lambda}g_{\lambda\sigma}F^{\nu\sigma}$ is unchanged by $\mu \leftrightarrow \nu$ after $\lambda \leftrightarrow \sigma$) and built from $F$ alone. Components: $T_B^{00} = \frac12(\mathbf E^2 + \mathbf B^2)$, $T_B^{0i} = (\mathbf E\times\mathbf B)^i$.
>
> **(c)** $F$ is gauge invariant, so only $\partial^\nu A_\lambda \to \partial^\nu A_\lambda + \partial^\nu\partial_\lambda\chi$ changes: $\Delta T^{\mu\nu} = -F^{\mu\lambda}\partial_\lambda\partial^\nu\chi = -\partial_\lambda(F^{\mu\lambda}\partial^\nu\chi) + (\partial_\lambda F^{\mu\lambda})\partial^\nu\chi = \partial_\lambda(F^{\lambda\mu}\partial^\nu\chi)$ on solutions. $B^{\lambda\mu\nu} = F^{\lambda\mu}\partial^\nu\chi$ is antisymmetric in $\lambda\mu$: an improvement term, identically conserved, whose charge $\int d^3x\,\partial_iB^{i0\nu}$ is a surface term. So $P^\nu$ of the canonical tensor is gauge invariant for fields (and $\chi$) falling off at infinity, although the density is not.
>
> *Checked against:* [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-2|Example §C1b.8.2]] (items 1–3: the canonical tensor; 4–5: $K = F^{\mu\lambda}A^\nu$ and $T_B$; 6: components; 7: $K$ from Belinfante's formula with the same three-term count); [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-4|Theorem §C1b.8.4]]; the user's Problem Set 2, Problem 4(c)–(d), as summarized in the PS Drill (the same tensors). *Derived here; check:* (c) by [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]] and the gauge invariance of $F$, [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-3|Theorem §C4.6.3]].

^sol-wn-15

### W16. Lorentz transformations: spin and orbital angular momentum of the vector field

![[PHY 513 Worksheet — Noether Currents#^wn-16]]

![[PHY 513 Worksheet — Noether Currents#^wn-16-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-16-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-16-c]]

![[PHY 513 Worksheet — Noether Currents#^wn-16-d]]

> [!success]- Solution
> **Answers.** (a) as stated, for every mass. (b) $\mathbf S = \int\mathbf E\times\mathbf A$, $S^{0k} = -\int A^0E^k$. (c) $\mathbf L = \int E^l(\mathbf x\times\nabla)A^l$. (d) $\Delta\mathbf S = -\int\chi\,\nabla\times\mathbf E = \int\chi\,\partial_t\mathbf B$, $\Delta\mathbf L = -\Delta\mathbf S$ when $\nabla\cdot\mathbf E = 0$.
>
> **(a)** W15(b), Step 1: $\mathcal S^{\lambda\mu\nu} = -F^{\lambda\mu}A^\nu + F^{\lambda\nu}A^\mu$, built from $\partial\mathcal L/\partial(\partial_\lambda A_\alpha) = -F^{\lambda\alpha}$ and the vector generators. The Proca term $\frac12m^2A_\mu A^\mu$ contains no derivative of $A$, so $\partial\mathcal L/\partial(\partial_\lambda A_\alpha)$, hence $\mathcal S$, is the same for every $m$.
>
> **(b)** At $\lambda = 0$, with $F^{0i} = -E^i$, $F^{00} = 0$: $\mathcal S^{0jk} = F^{0k}A^j - F^{0j}A^k = E^jA^k - E^kA^j$ and $\mathcal S^{00k} = F^{0k}A^0 - F^{00}A^k = -E^kA^0$. Then $S^i = \frac12\varepsilon_{ijk}S^{jk} = \frac12\int d^3x\,(\varepsilon_{ijk}E^jA^k - \varepsilon_{ijk}E^kA^j) = \int d^3x\,\varepsilon_{ijk}E^jA^k$ (rename $j \leftrightarrow k$ in the second), i.e. $\mathbf S = \int d^3x\,\mathbf E\times\mathbf A$; and $S^{0k} = -\int d^3x\,A^0E^k$.
>
> **(c)** $T^{0k} = -F^{0\lambda}\partial^kA_\lambda - g^{0k}\mathcal L = -F^{0l}\partial^kA_l = E^l\partial^kA_l$ ($F^{00} = 0$, $g^{0k} = 0$). Two signs, $\partial^k = -\partial_k$ and $A_l = -A^l$: $T^{0k} = E^l\partial_kA^l$. Then $L^i = \frac12\varepsilon_{ijk}L^{jk} = \int d^3x\,\varepsilon_{ijk}x^jT^{0k} = \int d^3x\,E^l\varepsilon_{ijk}x^j\partial_kA^l = \int d^3x\,E^l\bigl((\mathbf x\times\nabla)A^l\bigr)^i$.
>
> **(d) Step 1** (the spin). Only the bare $\mathbf A$ changes: $\Delta\mathbf S = \int d^3x\,\mathbf E\times(-\nabla\chi)$. Integrate by parts: $(\mathbf E\times\nabla\chi)^i = \varepsilon_{ijk}E^j\partial_k\chi = \partial_k(\varepsilon_{ijk}E^j\chi) - \varepsilon_{ijk}(\partial_kE^j)\chi$, the first a divergence (zero for compact $\chi$) and $-\varepsilon_{ijk}\partial_kE^j = (\nabla\times\mathbf E)^i$. So $\Delta\mathbf S = -\int d^3x\,\chi\,\nabla\times\mathbf E = \int d^3x\,\chi\,\partial_t\mathbf B$, using Faraday's law $\nabla\times\mathbf E = -\partial_t\mathbf B$ (from $\mathbf E = -\nabla A^0 - \partial_t\mathbf A$).
>
> **Step 2** (the orbital part). $\Delta L^i = -\int d^3x\,E^l\varepsilon_{ijk}x^j\partial_k\partial_l\chi = \int d^3x\,\partial_l(E^l\varepsilon_{ijk}x^j)\,\partial_k\chi$ (by parts in $\partial_l$) $= \int d^3x\,\bigl[(\nabla\cdot\mathbf E)(\mathbf x\times\nabla\chi)^i + (\mathbf E\times\nabla\chi)^i\bigr]$, and by Step 1 the last term integrates to $\int\chi\,(\nabla\times\mathbf E)^i$.
>
> **Step 3** (the total). $\Delta\mathbf J = \Delta\mathbf L + \Delta\mathbf S = \int d^3x\,(\nabla\cdot\mathbf E)\,\mathbf x\times\nabla\chi = 0$ by Gauss's law of the free field. For radiation $\nabla\times\mathbf E \neq 0$, so $\mathbf S$ and $\mathbf L$ separately depend on the gauge; only $\mathbf J = \int d^3x\,\mathbf x\times(\mathbf E\times\mathbf B)$ is an observable.
>
> *Checked against:* [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-4|Theorem §C4.1.4]] (a), [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-5|Theorem §C4.1.5]] (b), [[§C4.1 The Vector Field and Its Lorentz Transformation#^thm-c4-1-6|Theorem §C4.1.6]] (c), [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-13|Theorem §C4.6.13]] (d; the same $\Delta\mathbf S$, $\Delta\mathbf L$, $\Delta\mathbf J$), [[§C4.1 The Vector Field and Its Lorentz Transformation#^rem-c4-1-3|§C4.1, Remark: Spin hidden in the Poynting vector]] (the gauge-invariant form of $\mathbf J$). C4 is largely written ahead of the lectures (§C4.6 is a draft); the computations use only §C1b.8 and §C1a.7.

^sol-wn-16

### W17. Gauge and shift symmetries of the vector field

![[PHY 513 Worksheet — Noether Currents#^wn-17]]

![[PHY 513 Worksheet — Noether Currents#^wn-17-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-17-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-17-c]]

> [!success]- Solution
> **Answers.** (a) $j^{\mu\nu} = -F^{\mu\nu}$ (one current per $\nu$), conserved by $\partial_\mu F^{\mu\nu} = 0$; charges $Q^0 = 0$, $\mathbf Q = \int d^3x\,\mathbf E$. (b) $j^\mu_\chi = -F^{\mu\rho}\partial_\rho\chi = \partial_\rho(F^{\rho\mu}\chi)$ on solutions; $Q_\chi = \oint\chi\,\mathbf E\cdot d\mathbf S = 0$. (c) $\partial_\mu j^\mu{}_\nu = m^2A_\nu$; then $m^2\partial_\nu A^\nu = 0$.
>
> **(a) Step 1** (generators, symmetry). $A'_\rho = A_\rho + \alpha^\nu g_{\nu\rho}$: $\Delta_\nu A_\rho = g_{\nu\rho}$, constant, so $\partial_\mu(\Delta_\nu A_\rho) = 0$, and $\mathcal L$ depends on $A$ only through $\partial A$: $\delta\mathcal L = 0$, $\mathcal J = 0$. (As a gauge transformation with $\chi = \alpha_\nu x^\nu$: $\partial_\rho\chi = \alpha_\rho = \alpha^\nu g_{\nu\rho}$.)
>
> **Step 2** (currents). $j^\mu{}_\nu = \sum_\rho\frac{\partial\mathcal L}{\partial(\partial_\mu A_\rho)}\Delta_\nu A_\rho = -F^{\mu\rho}g_{\rho\nu} = -F^\mu{}_\nu$; raising $\nu$, $j^{\mu\nu} = -F^{\mu\nu}$.
>
> **Step 3** (conservation). $\partial_\mu j^{\mu\nu} = -\partial_\mu F^{\mu\nu}$, which vanishes exactly by the source-free Maxwell equation: the four conservation laws are the four field equations (as for the massless shift of W1(a)).
>
> **Step 4** (charges). $Q^\nu = \int d^3x\,j^{0\nu} = -\int d^3x\,F^{0\nu}$: $Q^0 = 0$ ($F^{00} = 0$) and $Q^i = -\int d^3x\,F^{0i} = \int d^3x\,E^i$. Check: the $\nu = i$ Maxwell equation $\partial_0F^{0i} + \partial_jF^{ji} = 0$ reads $\partial_t\mathbf E = \nabla\times\mathbf B$, so $\frac{d}{dt}\int d^3x\,\mathbf E = \int d^3x\,\nabla\times\mathbf B$, a surface term. The $\nu = 0$ law is Gauss's law $\nabla\cdot\mathbf E = 0$, a constraint with zero charge.
>
> **(b) Step 1** (current). $\Delta_\chi A_\rho = \partial_\rho\chi$; $F$ and $\mathcal L$ are gauge invariant, so $\delta\mathcal L = 0$, $\mathcal J = 0$, and $j^\mu_\chi = -F^{\mu\rho}\partial_\rho\chi$.
>
> **Step 2** (an improvement term). Product rule: $\partial_\rho(F^{\rho\mu}\chi) = (\partial_\rho F^{\rho\mu})\chi + F^{\rho\mu}\partial_\rho\chi = 0 - F^{\mu\rho}\partial_\rho\chi = j^\mu_\chi$ on solutions. $F^{\rho\mu}\chi$ is antisymmetric in $\rho\mu$, so $\partial_\mu\partial_\rho(F^{\rho\mu}\chi) = 0$ identically: the conservation law carries no information beyond the field equations.
>
> **Step 3** (charge). $Q_\chi = \int d^3x\,\partial_\rho(F^{\rho0}\chi) = \int d^3x\,\partial_i(F^{i0}\chi) = \int d^3x\,\nabla\cdot(\chi\mathbf E) = \oint\chi\,\mathbf E\cdot d\mathbf S$ ($F^{i0} = E^i$), zero for $\chi$ of compact support. A local symmetry gives no new conserved charge; its content is the constraint (Gauss's law). For $\chi = \alpha_\nu x^\nu$ the surface term survives and reproduces (a): $j^\mu_\chi = -F^{\mu\rho}\alpha_\rho = \alpha^\nu j^\mu{}_\nu$.
>
> **(c) Step 1** ($\delta\mathcal L$). $\mathcal L_m = \frac12m^2A_\rho A^\rho$ gives $\delta\mathcal L = m^2A^\rho\,\alpha^\nu g_{\nu\rho} = \alpha^\nu m^2A_\nu$. No derivatives: not a divergence (a bump in $A_\nu$), so $\mathcal J = 0$ and $X_\nu = m^2A_\nu$.
>
> **Step 2** (two ways). The mass term has no derivatives, so $j^\mu{}_\nu = -F^\mu{}_\nu$ as before, and [[§C1b.5 Noether's Theorem#^thm-c1b-5-5|Theorem §C1b.5.5]] gives $\partial_\mu j^\mu{}_\nu = m^2A_\nu$ on solutions. Directly, the Proca equation $\partial_\mu F^{\mu\nu} + m^2A^\nu = 0$ gives $\partial_\mu(-F^{\mu\nu}) = m^2A^\nu$: the same.
>
> **Step 3** (Lorenz condition). Apply $\partial_\nu$: $\partial_\nu\partial_\mu F^{\mu\nu} = 0$ (symmetric against antisymmetric), so $m^2\partial_\nu A^\nu = 0$, and for $m \neq 0$, $\partial_\nu A^\nu = 0$. The same mass term breaks the full gauge symmetry: $\delta\mathcal L_m = \alpha\,m^2A^\rho\partial_\rho\chi$ to first order.
>
> *Derived here; check:* (a)–(b) against [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-3|Theorem §C4.6.3]] (gauge invariance of $F$ and of $\mathcal L$, broken by the mass), [[§C1a.7 Relativistic Electrodynamics in Index Form#^thm-c1a-7-1|Theorem §C1a.7.1]] (Maxwell's equations; Gauss and Ampère–Maxwell), [[§C1a.7 Relativistic Electrodynamics in Index Form#^def-c1a-7-2|Def. §C1a.7.2]] ($F^{0i} = -E^i$, $F^{i0} = E^i$), [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-2|Theorem §C1b.6.2]] (improvement terms); (c) against [[§C4.2★ The Proca Field#^thm-c4-2-3|Theorem §C4.2.3]] and [[§C4.2★ The Proca Field#^thm-c4-2-4|Theorem §C4.2.4]] (Proca equation; the Lorenz condition follows), with the divergence computed both ways in Step 2.

^sol-wn-17

## All fields

### W18. Short response: signs and normalizations

![[PHY 513 Worksheet — Noether Currents#^wn-18]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-a]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-b]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-c]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-d]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-e]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-f]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-g]]

![[PHY 513 Worksheet — Noether Currents#^wn-18-h]]

> [!success]- Answers
> 1. (a) $-\varepsilon^\rho T^\mu{}_\rho$: the same tensor with the opposite overall sign, because $\varepsilon = -a$. [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^cau-c1b-7-1|§C1b.7, Caution: One picture at a time; the sign of the displacement]].
> 2. (b) $K^i = \int d^3x\,x^i\mathcal H - tP^i$; the course's generator is its negative, $\hat K^i = \hat J^{0i} = -\hat K^i_{\rm N}$. [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^ex-c1b-8-1|Example §C1b.8.1]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]], [[§C3.4 Quantum Poincaré Transformations and the Poincaré Algebra#^cau-c3-4-1|§C3.4, Caution: Signs and names across the sources]].
> 3. (c) Every Lorentz charge doubles (the $\frac12$ compensates the double count of each antisymmetric pair). [[P3 Noether's Procedure]], Pitfalls; [[§C1b.5 Noether's Theorem#^thm-c1b-5-1|Theorem §C1b.5.1]], derivation step 6.
> 4. (d) Negative, $j^0 = -2E\lvert A\rvert^2$; $\hat Q = \frac12(\hat N_a - \hat N_b) = -\frac12\int d^3x\,:\!\hat j^0\!:$. [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]].
> 5. (e) $j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$; $+1$ ($\hat Q = \hat N_a - \hat N_b$). [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]].
> 6. (f) $2im\,\bar\psi\gamma^5\psi = 2m\,\mathsf P$ (as Peskin–Schroeder (3.75)). [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-4|Theorem §C5a.8.4]].
> 7. (g) Real and complex scalar: symmetric; Dirac and Maxwell: not (fields with an index). [[§C1b.7 Spacetime Symmetries꞉ Energy and Momentum#^rem-c1b-7-3|§C1b.7, Remark: The canonical tensor of the standard fields]], [[§C1b.8 Lorentz Symmetry꞉ Angular Momentum and the Symmetric Tensor#^thm-c1b-8-2|Theorem §C1b.8.2]].
> 8. (h) Only $\mathbf J$. [[§C4.6 The Maxwell Field, Gauge Symmetry and Gauge Fixing#^thm-c4-6-13|Theorem §C4.6.13]].
>
> *Checked against:* the boxes named in each line.

^sol-wn-18
