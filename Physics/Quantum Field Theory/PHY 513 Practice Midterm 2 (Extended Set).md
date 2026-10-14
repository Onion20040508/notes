---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 Practice Midterm Solutions|Solutions]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Practice Midterm 2: the Extended Set

A bank to pick from, organised by topic and technique (codes K1–K16 as in [[PHY 513 Midterm Review]]). For every problem of Problem Sets 1–7 there is one line pointing to its literal re-ask in [[PHY 513 PS Drill]] (Larsen: "a few of the questions are literally individual questions that were on the homeworks"), followed by 1–3 **variations** (the same computation on an object Peskin–Schroeder does not work out: another field, bilinear, symmetry, propagator, axis; Larsen: "The example in the book was the … axial, the pseudo vector. Oh, I guess I have to pick a vector, or maybe the other way around") and **extensions** (one step further, within Lectures 1–12). Each item is about one exam part: 5–10 minutes. Full solutions, checked against the home boxes, are in [[PHY 513 Practice Midterm Solutions]] (same item numbers). The exam-shaped paper is [[PHY 513 Practice Midterm]]; why each problem was set is in the review folder's `PURPOSE.md`.

Conventions throughout ([[Larsen PHY 513]]): $g = \mathrm{diag}(+1,-1,-1,-1)$; $\varepsilon^{0123} = +1$; $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$, $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$; $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$, chiral basis, $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$; $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$; $(\partial^2 + m^2)D_C = -i\delta^4$; discrete symmetries as $U\hat OU^{-1}$ with $U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$, $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i(\hat{\bar\psi}(x)\gamma^0\gamma^2)^{\mathsf T}$, $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$ (antiunitary); $\tilde x = (t, -\mathbf x)$, $x_T = (-t, \mathbf x)$; $\hat\psi^{\dagger\mathsf T}$ with $(\hat\psi^{\dagger\mathsf T})_a = (\hat\psi_a)^\dagger$.

**Counts.** 35 literal re-ask lines (every problem of PS1–PS7, Problem 0 of PS4 included) and 93 items: 52 variations and 29 extensions in sections A–G, and 12 short-response items in section H (10 variations, 2 literal).

---

## A. Relativity, index calculus, invariants (T1; K1, K2, K8)

### PS1.1 Index bonanza, part 1
*Literal re-ask: [[PHY 513 PS Drill#^ps1-1|PS Drill, PS1.1]], parts (a)–(j).*

**X1.1.1** *[variation of PS1.1]* Legal or illegal? If legal, name the tensor type (scalar, vector, covector, …), and say whether the expression is a pseudoscalar.
(a) $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$; (b) $\partial_\mu F^{\mu\nu} = j_\nu$; (c) $x^\mu\,\partial_\nu x^\nu\,x_\mu$; (d) $T^{\mu\nu}{}_\nu = S^\mu$; (e) $a_\mu b^\mu c_\mu$; (f) $\bar\psi\gamma^\mu\partial_\mu\psi = m\bar\psi\psi$.

^px-1-1-1

### PS1.2 Index bonanza, part 2
*Literal re-ask: [[PHY 513 PS Drill#^ps1-2|PS Drill, PS1.2]], parts (a)–(d).*

**X1.2.1** *[variation of PS1.2(b)]* Write $\Lambda^{\mathsf T}g\Lambda = g$ in index form, and show that it implies $(\Lambda^{-1})^\rho{}_\mu = \Lambda_\mu{}^\rho \equiv g_{\mu\alpha}g^{\rho\beta}\Lambda^\alpha{}_\beta$.

^px-1-2-1

**X1.2.2** *[variation of PS1.2(d)]* Let $S^{\mu\nu}$ be symmetric and $A_{\mu\nu}$ antisymmetric. Show $S^{\mu\nu}A_{\mu\nu} = 0$. Then express $F^{\mu\nu}F_{\nu\mu}$ and $F^\mu{}_\mu$ through $F_{\mu\nu}F^{\mu\nu}$ and numbers.

^px-1-2-2

### PS1.3 The Levi-Civita symbol
*Literal re-ask: [[PHY 513 PS Drill#^ps1-3|PS Drill, PS1.3]], parts (a)–(b).*

**X1.3.1** *[variation of PS1.3(a)]* With the course's $\varepsilon^{0123} = +1$, give $\varepsilon^{3012}$, $\varepsilon^{2301}$, $\varepsilon_{0123}$, $\varepsilon_{1032}$. What are the same four numbers in Peskin–Schroeder's convention?

^px-1-3-1

**X1.3.2** *[variation of PS1.3(b)]* Three four-momenta satisfy $p_1 + p_2 + p_3 = 0$. Show that $\varepsilon^{\mu\nu\rho\sigma}p_{1\nu}p_{2\rho}p_{3\sigma} = 0$ for every $\mu$. Is $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}k_\sigma$ zero for an arbitrary fourth vector $k$?

^px-1-3-2

**X1.3.3** *[extension of PS1.3(b)]* Show that $I = \varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma}$ changes sign under parity, $p^\mu \to \mathcal P^\mu{}_\nu p^\nu$, although $\mathcal P$ satisfies $\mathcal P^{\mathsf T}g\mathcal P = g$. Which identity relating $\varepsilon$ and $\det\Lambda$ do you use?

^px-1-3-3

### PS1.4 Relativistic kinematics and natural units
*Literal re-ask: [[PHY 513 PS Drill#^ps1-4|PS Drill, PS1.4]], parts (a)–(d).*

**X1.4.1** *[variation of PS1.4(a)]* Antiproton production on a fixed target: $p + p \to p + p + p + \bar p$, the target proton at rest. Find the minimum (threshold) lab energy $E$ of the beam proton, and its kinetic energy in GeV ($m_pc^2 = 0.938$ GeV).

^px-1-4-1

**X1.4.2** *[variation of PS1.4(c)]* A $\pi^0$ of mass $m$ decays at rest, $\pi^0 \to \gamma\gamma$. (a) Give each photon's energy. (b) In a frame where the pion has energy $E$ and momentum $p$, find the largest and smallest possible photon energies.

^px-1-4-2

**X1.4.3** *[variation of PS1.4(b), (d)]* Restore $\hbar$ and $c$ in the reduced Compton wavelength $1/m$, and evaluate it for the electron ($m_ec^2 = 0.511$ MeV) and the pion ($m_\pi c^2 = 140$ MeV) in fm, with $\hbar c = 197.3$ MeV fm.

^px-1-4-3

### PS1.5 Two-body kinematics
*Literal re-ask: [[PHY 513 PS Drill#^ps1-5|PS Drill, PS1.5]], parts (a)–(f).*

**X1.5.1** *[extension of PS1.5(e)–(f)]* With $u \equiv (p_1 - p_4)^2$, show $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.

^px-1-5-1

**X1.5.2** *[variation of PS1.5(d)]* Show that the cms momentum is $p'^2 = \lambda(s, m_1^2, m_2^2)/4s$ with $\lambda(a, b, c) = a^2 + b^2 + c^2 - 2ab - 2bc - 2ca$, and check that it agrees with $p' = m_2p_{\rm lab}/E_{\rm cms}$.

^px-1-5-2

**X1.5.3** *[variation of PS1.5(f)]* For elastic scattering of equal masses, $m_1 = m_2 = m_3 = m_4 = m$, express $u$ through the cms momentum $p'$ and angle $\theta'$, and check $s + t + u = 4m^2$.

^px-1-5-3

### PS1.6 Derivatives with four-vectors
*Literal re-ask: [[PHY 513 PS Drill#^ps1-6|PS Drill, PS1.6]], parts (a)–(f).*

**X1.6.1** *[variation of PS1.6(c)–(d)]* In $d$ spacetime dimensions, with $\rho = x_\mu x^\mu$, compute $\Box\rho$, $\Box\rho^2$ and $\Box^2\rho^2$.

^px-1-6-1

**X1.6.2** *[extension of PS1.6(f)]* Show $\Box f(\rho) = 4\rho f''(\rho) + 2d\,f'(\rho)$, and find all $f(\rho)$ with $\Box f = 0$ for $\rho \ne 0$ in $d$ dimensions ($d > 2$).

^px-1-6-2

---

## B. Classical fields, Euler–Lagrange, Hamiltonian, Noether (T3, T4; K2, K8, K12)

### PS2.1 The dilaton
*Literal re-ask: [[PHY 513 PS Drill#^ps2-1|PS Drill, PS2.1]], parts (a)–(b).*

**X2.1.1** *[extension of PS2.1(b)]* Show that if $\tau$ solves $\Box\tau = (\partial\tau)^2$, then $\sigma \equiv e^{-\tau}$ solves $\Box\sigma = 0$, and that $\mathcal L = -f^2e^{-2\tau}(\partial\tau)^2 = -f^2(\partial\sigma)^2$: the dilaton is a free field in disguise.

^px-2-1-1

**X2.1.2** *[variation of PS2.1(b)]* For $\mathcal L = \frac12K(\phi)\,\partial_\mu\phi\,\partial^\mu\phi - V(\phi)$, derive the field equation. Check it against PS2.1(b) with $K = -2f^2e^{-2\phi}$, $V = 0$.

^px-2-1-2

### PS2.2 Two scalars without the canonical ½
*Literal re-ask: [[PHY 513 PS Drill#^ps2-2|PS Drill, PS2.2]], parts (a)–(d).*

**X2.2.1** *[extension of PS2.2(a)]* Rescale $\phi_i = \chi_i/\sqrt2$ in $\mathcal L = \partial_\mu\phi_1\partial^\mu\phi_1 + \partial_\mu\phi_2\partial^\mu\phi_2 - m^2\phi_1^2 - \mu\phi_1\phi_2^2 - \lambda\phi_1^2\phi_2^2$. Write $\mathcal L$ in canonical form and read off the masses of $\chi_1$, $\chi_2$ and the cubic and quartic couplings.

^px-2-2-1

**X2.2.2** *[variation of PS2.2(b)–(c)]* For $\mathcal L = \frac Z2\partial_\mu\phi\,\partial^\mu\phi - V(\phi)$ with a constant $Z > 0$, find $\pi$ and $\mathcal H$ in terms of $\phi$, $\pi$, $\nabla\phi$.

^px-2-2-2

### PS2.3 The complex scalar: Euler–Lagrange, Hamiltonian, U(1)
*Literal re-ask: [[PHY 513 PS Drill#^ps2-3|PS Drill, PS2.3]], parts (a)–(d).*

**X2.3.1** *[variation of PS2.3(c)–(d)]* Two complex fields with $\mathcal L = \sum_{i=1,2}\bigl(\partial_\mu\phi_i^{\ast}\partial^\mu\phi_i - m^2\phi_i^{\ast}\phi_i\bigr) - g\,(\phi_1\phi_2 + \phi_1^{\ast}\phi_2^{\ast})$, $g$ real. Of the two phase rotations $\phi_1 \to e^{i\alpha}\phi_1$, $\phi_2 \to e^{\pm i\alpha}\phi_2$, which is a symmetry? Give its Noether current (in the sign convention $\Delta\phi_1 = i\phi_1$).

^px-2-3-1

**X2.3.2** *[variation of PS2.3(d)]* Write $\phi = (\phi_1 + i\phi_2)/\sqrt2$ with real $\phi_1$, $\phi_2$. Show that the phase rotation is a rotation of $(\phi_1, \phi_2)$, and compute the Noether current directly in the real fields; compare with $j^\mu = i(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi)$.

^px-2-3-2

### PS2.4 Electromagnetism and its energy–momentum
*Literal re-ask: [[PHY 513 PS Drill#^ps2-4|PS Drill, PS2.4]], parts (a)–(e).*

**X2.4.1** *[variation of PS2.4(a)]* The Proca Lagrangian $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu} + \frac12m^2A_\mu A^\mu$. Derive the field equation, and show that for $m \ne 0$ it implies $\partial_\mu A^\mu = 0$ and $(\partial^2 + m^2)A^\nu = 0$.

^px-2-4-1

**X2.4.2** *[extension of PS2.4(d)]* Show that the improved tensor $\hat T^{\mu\nu} = -F^{\mu\lambda}F^\nu{}_\lambda + \frac14g^{\mu\nu}F_{\lambda\sigma}F^{\lambda\sigma}$ is traceless in four dimensions. What changes in $d$ dimensions?

^px-2-4-2

---

## C. Canonical quantization: modes, charges, states (T5, T9; K9, K10, K11)

### PS3.1 The Lorentz-invariant measure
*Literal re-ask: [[PHY 513 PS Drill#^ps3-1|PS Drill, PS3.1]], parts (a)–(e).*

**X3.1.1** *[variation of PS3.1(e)]* Show that $2E_{\mathbf p}\,\delta^3(\mathbf p - \mathbf q)$ is Lorentz invariant, and conclude that $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ is a Lorentz-invariant normalisation.

^px-3-1-1

**X3.1.2** *[variation of PS3.1(d)]* Evaluate $\int d^4k\,\delta(k^2 - m^2)\,\theta(-k^0)\,f(k)$ and $\int d^4k\,\delta(k^2 - m^2)\,f(k)$ as three-dimensional integrals.

^px-3-1-2

### PS3.2 Quantization of the complex scalar
*Literal re-ask: [[PHY 513 PS Drill#^ps3-2|PS Drill, PS3.2]], parts (a1), (a2), (b), (c).*

**X3.2.1** *[extension of PS3.2(c)]* With $\hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$, compute $[\hat Q, \hat a^\dagger_{\mathbf p}]$, $[\hat Q, \hat b^\dagger_{\mathbf p}]$ and the charge of $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}\lvert0\rangle$ and of $(\hat a^\dagger_{\mathbf p})^2\lvert0\rangle$.

^px-3-2-1

**X3.2.2** *[variation of PS3.2(c)]* The Noether current of PS2.3(d), $j^\mu = i(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi)$, quantized and normal-ordered: express $\int d^3x\,:\!\hat j^0\!:$ through $\hat N_a$, $\hat N_b$, and relate it to $\hat Q$ of X3.2.1. Which feature of the two charges is physical?

^px-3-2-2

### PS3.3 Canonical commutators imply the oscillator algebra
*Literal re-ask: [[PHY 513 PS Drill#^ps3-3|PS Drill, PS3.3]], parts (a)–(c).*

**X3.3.1** *[variation of PS3.3(b)]* With $f_{\mathbf p}(x) = e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$ and $(f, g) = i\int d^3x\,(f^{\ast}\partial_0g - (\partial_0f^{\ast})g)$, compute $(f_{\mathbf p}, f_{\mathbf q})$ and $(f^{\ast}_{\mathbf p}, f_{\mathbf q})$.

^px-3-3-1

**X3.3.2** *[variation of PS3.3(b)]* For the complex field $\hat\phi = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x})$, express $\hat a_{\mathbf p}$ and $\hat b_{\mathbf p}$ through the Klein–Gordon product.

^px-3-3-2

**X3.3.3** *[variation of PS3.3(b), Dirac field]* For $\hat\psi(x) = \int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r\bigl(\hat a^r_{\mathbf q}u^r(q)e^{-iq\cdot x} + \hat b^{r\dagger}_{\mathbf q}v^r(q)e^{iq\cdot x}\bigr)$, show $\hat a^s_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\,u^{s\dagger}(p)\,\hat\psi(x)$ at any fixed $t$. Which spinor identities do you need?

^px-3-3-3

### PS3.4 Coherent states
*Literal re-ask: [[PHY 513 PS Drill#^ps3-4|PS Drill, PS3.4]], parts (a)–(e).*

**X3.4.1** *[extension of PS3.4(d)]* Compute the energy expectation $\langle\{\eta\}\rvert\hat H\lvert\{\eta\}\rangle$ with $\hat H = \int\frac{d^3k}{(2\pi)^3}E_{\mathbf k}\hat a^\dagger_{\mathbf k}\hat a_{\mathbf k}$.

^px-3-4-1

**X3.4.2** *[variation of PS3.4(c)]* Compute $\bar\pi(x) = \langle\{\eta\}\rvert\hat\pi(x)\lvert\{\eta\}\rangle$, $\hat\pi = \partial_t\hat\phi$, and check $\bar\pi = \partial_t\bar\phi$.

^px-3-4-2

**X3.4.3** *[extension of PS3.4(e)]* For a single mode, $\lvert\alpha\rangle = e^{-|\alpha|^2/2}e^{\alpha\hat a^\dagger}\lvert0\rangle$ with $[\hat a, \hat a^\dagger] = 1$: find the probability of $n$ quanta and check its mean and variance against (d)–(e).

^px-3-4-3

### PS6.1 The momentum operator in modes
*Literal re-ask: [[PHY 513 PS Drill#^ps6-1|PS Drill, PS6.1]].*

**X6.1.1** *[extension of PS6.1]* Without the colons, $\hat{\mathbf P}$ and $\hat H$ of the real scalar each differ from their normal-ordered forms by a constant. Give both constants (in terms of $\delta^3(\mathbf 0)$ or the volume $V$), and say why one is zero and the other not.

^px-6-1-1

**X6.1.2** *[variation of PS6.1, Dirac field]* Show that $\hat{\mathbf P} = \int d^3x\,:\!\hat\psi^\dagger(-i\nabla)\hat\psi\!: = \int\frac{d^3p}{(2\pi)^3}\sum_s\mathbf p\,(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p})$.

^px-6-1-2

### PS6.2 The Dirac charge in modes
*Literal re-ask: [[PHY 513 PS Drill#^ps6-2|PS Drill, PS6.2]].*

**X6.2.1** *[extension of PS6.2]* With $\hat Q = \int\frac{d^3p}{(2\pi)^3}\sum_s(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p})$ and the anticommutators $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^3(\mathbf p - \mathbf q)\delta^{rs}$ (same for $\hat b$), compute $[\hat Q, \hat a^{s\dagger}_{\mathbf p}]$ and $[\hat Q, \hat b^{s\dagger}_{\mathbf p}]$. (Commutator, although the modes anticommute.)

^px-6-2-1

**X6.2.2** *[variation of PS6.2]* Show $\hat H = \int d^3x\,:\!\hat\psi^\dagger H_{\text{s.p.}}\hat\psi\!: = \int\frac{d^3p}{(2\pi)^3}\sum_sE_{\mathbf p}(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p})$, with $H_{\text{s.p.}}u^s(p) = E_{\mathbf p}u^s(p)$ and $H_{\text{s.p.}}v^s(\tilde p) = -E_{\mathbf p}v^s(\tilde p)$ in momentum space, and say where the sign of the antiparticle term comes from.

^px-6-2-2

---

## D. Two-point functions, Green's functions, contours (T6; K13, K14, K9)

### PS4.0 Generalized functions
*Literal re-ask: [[PHY 513 PS Drill#^ps4-0|PS Drill, PS4.0]] (no questions on the sheet).*

**X4.0.1** *[extension of PS4.0]* Show that $D_R - D_A = iD$ solves the homogeneous Klein–Gordon equation, as the non-uniqueness of Green's functions requires, using $D_R = \theta(\xi^0)iD$, $D_A = -\theta(-\xi^0)iD$.

^px-4-0-1

### PS4.1 Contour integration
*Literal re-ask: [[PHY 513 PS Drill#^ps4-1|PS Drill, PS4.1]], parts (a)–(i).*

**X4.1.1** *[variation of PS4.1(e)–(h)]* Compute $\int_{-\infty}^\infty\frac{dx}{(x^2 + a^2)^2}$, $a > 0$, by closing the contour.

^px-4-1-1

**X4.1.2** *[variation of PS4.1(e)–(h)]* Compute $\int_{-\infty}^\infty dx\,\frac{e^{ikx}}{x^2 + m^2}$ for real $k$ of either sign, $m > 0$. Which half-plane do you close in, and why?

^px-4-1-2

**X4.1.3** *[variation of PS4.2(b), eq. (11)]* For a smooth $f$ that falls off at infinity, express $\lim_{\varepsilon\to0^+}\int dx\,\frac{f(x)}{x - a + i\varepsilon}$ through a principal value; then find the imaginary part of $\frac{1}{p^2 - m^2 + i\varepsilon}$ as $\varepsilon \to 0^+$.

^px-4-1-3

### PS4.2 Green's functions of the massless field
*Literal re-ask: [[PHY 513 PS Drill#^ps4-2|PS Drill, PS4.2]], parts (a)–(b).*

**X4.2.1** *[extension of PS4.2(b)]* For $m = 0$, $D(\xi) = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\,\delta(\xi^2)$. Write $D_R = \theta(\xi^0)\,iD$ as a function of $t = \xi^0 > 0$ and $r = |\boldsymbol\xi|$. Where is it supported?

^px-4-2-1

**X4.2.2** *[variation of PS4.2(a)]* From $D_W(\xi) = -\frac{1}{4\pi^2}\frac{1}{(\xi^0 - i\varepsilon)^2 - \boldsymbol\xi^2}$ ($m = 0$), find $D_F(\xi) = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$ in one covariant formula.

^px-4-2-2

### PS4.3 Green's functions of the massive field
*Literal re-ask: [[PHY 513 PS Drill#^ps4-3|PS Drill, PS4.3]], parts (a), (b) — (b) is the part Larsen named in class; it is Problem 4(a) of [[PHY 513 Practice Midterm]].*

**X4.3.1** *[extension of PS4.3(b)]* From $D_W = \frac{m}{4\pi^2r}K_1(mr)$ at spacelike separation and $K_1(z) \simeq 1/z$ for $z \ll 1$, find $D_W$ for $mr \ll 1$ and compare with the massless function of PS4.2.

^px-4-3-1

**X4.3.2** *[extension of PS4.3(b)]* For $mr \gg 1$, $D_1 \simeq \sqrt{m/8\pi^3}\,r^{-3/2}e^{-mr}$. Restore $\hbar$ and $c$ in the decay length, and find the factor by which $D_1$ drops between $r$ and $r + 1$ fm for a pion ($m_\pi c^2 = 140$ MeV), at $r = 10$ fm.

^px-4-3-2

### PS4.4 The Feynman propagator
*Literal re-ask: [[PHY 513 PS Drill#^ps4-4|PS Drill, PS4.4]], parts (a)–(c).*

**X4.4.1** *[variation of PS4.4(c)]* Show by the product rule (the computation of PS4.4(c), PS (2.56)) that $D_A(x - y) = -\theta(y^0 - x^0)\langle0|[\hat\phi(x), \hat\phi(y)]|0\rangle$ satisfies $(\partial_x^2 + m^2)D_A = -i\delta^4(x - y)$.

^px-4-4-1

**X4.4.2** *[variation of PS4.4(a)]* Do the $p^0$ integral of $D_F(\xi) = \int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip\cdot\xi}}{p^2 - m^2 + i\varepsilon}$ by residues for $\xi^0 > 0$ and $\xi^0 < 0$, and recover $\theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$.

^px-4-4-2

**X4.4.3** *[extension of PS4.4(c)]* With $S_F(x - y) = (i\slashed\partial_x + m)D_F(x - y)$, show $(i\slashed\partial_x - m)S_F(x - y) = i\delta^4(x - y)$, and give $\tilde S_F(p)$.

^px-4-4-3

---

## E. Lorentz group, algebra, representations (T7; K3, K4, K16)

### PS4.5 Lorentz algebra
*Literal re-ask: [[PHY 513 PS Drill#^ps4-5|PS Drill, PS4.5]], parts (a)–(c); (b) is Problem 2(c) of [[PHY 513 Practice Midterm]].*

**X4.5.1** *[variation of PS4.5(a)]* From $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho})$ compute $[\mathcal J^{01}, \mathcal J^{12}]$ and $[\mathcal J^{12}, \mathcal J^{23}]$, and translate both into $\mathbf J$, $\mathbf K$.

^px-4-5-1

**X4.5.2** *[variation of PS4.5(b)]* Show $[\gamma^5, S^{\mu\nu}] = 0$. What does this say about the two chiral halves of a Dirac spinor?

^px-4-5-2

**X4.5.3** *[extension of PS4.5(b)]* For the spinor boost along $z$, $\Lambda_{1/2} = \operatorname{diag}(e^{-\eta/2}, e^{\eta/2}, e^{\eta/2}, e^{-\eta/2})$, check $\Lambda_{1/2}^{-1}\gamma^0\Lambda_{1/2} = \Lambda^0{}_\nu\gamma^\nu$ explicitly, with the vector boost $\Lambda^0{}_0 = \cosh\eta$, $\Lambda^0{}_3 = \sinh\eta$.

^px-4-5-3

### PS5.1 Representations of SO(1,3)
*Literal re-ask: [[PHY 513 PS Drill#^ps5-1|PS Drill, PS5.1]], parts (a)–(b).*

**X5.1.1** *[variation of PS5.1(a)]* Problem Set 5 used $K^i = \mathcal J^{i0}$; the course uses $K_i = \mathcal J^{0i}$. Show that $[J_i, J_j]$, $[J_i, K_j]$, $[K_i, K_j]$ have the same form in both conventions, and find how $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$ of the two conventions are related.

^px-5-1-1

**X5.1.2** *[variation of PS5.1(b)]* In the course convention, write the finite boost along $z$ with rapidity $\eta$ on the two-component spaces $(\frac12, 0)$ and $(0, \frac12)$. Which one grows on its upper component?

^px-5-1-2

**X5.1.3** *[extension of PS5.1(b)]* Give the dimension and the rotation content (spins) of $(\frac12, \frac12)$, $(1, 0)\oplus(0, 1)$, $(1, \frac12)$, and identify the fields of the course that carry the first two.

^px-5-1-3

### PS6.4 Lorentz transformations as 4×4 matrices
*Literal re-ask: [[PHY 513 PS Drill#^ps6-4|PS Drill, PS6.4]], parts (a)–(d); the boost along the 1-axis is Problem 2(b) of [[PHY 513 Practice Midterm]].*

**X6.4.1** *[variation of PS6.4(a)]* Boost along the 2-axis, $\omega_{02} = -\omega_{20} = \eta$: write the vector and spinor matrices as $4\times4$ matrices.

^px-6-4-1

**X6.4.2** *[variation of PS6.4(c)]* Rotation about the 1-axis, $\omega_{23} = -\omega_{32} = \theta$: write the vector and spinor matrices as $4\times4$ matrices, and give both at $\theta = 2\pi$.

^px-6-4-2

---

## F. γ matrices, spinors, Dirac fields (T8; K5, K6, K7)

### PS5.2 Contraction identities
*Literal re-ask: [[PHY 513 PS Drill#^ps5-2|PS Drill, PS5.2]], parts (a)–(d); (d) is Problem 5(a) of [[PHY 513 Practice Midterm]].*

**X5.2.1** *[variation of PS5.2(a)–(c)]* In $d$ spacetime dimensions ($\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$, $g^\mu{}_\mu = d$), compute $\gamma_\mu\gamma^\mu$, $\gamma_\mu\slashed k\gamma^\mu$, $\gamma_\mu\slashed p\slashed q\gamma^\mu$.

^px-5-2-1

**X5.2.2** *[variation of PS5.2(b)]* Compute $\gamma_\mu\gamma^5\gamma^\mu$ and $\gamma_\mu\gamma^\nu\gamma^5\gamma^\mu$ (four dimensions).

^px-5-2-2

**X5.2.3** *[extension of PS5.2]* Compute $\operatorname{tr}(\slashed p\slashed q)$, $\operatorname{tr}(\slashed p\slashed q\slashed k)$, and $\operatorname{tr}\bigl((\slashed p + m)\gamma^\mu(\slashed q - m)\gamma_\mu\bigr)$.

^px-5-2-3

### PS5.3 The Gordon identity
*Literal re-ask: [[PHY 513 PS Drill#^ps5-3|PS Drill, PS5.3]]; the $v$-spinor version is Problem 5(b) of [[PHY 513 Practice Midterm]].*

**X5.3.1** *[extension of PS5.3]* Forward limit: from the Gordon identity, show $\bar u^r(p)\gamma^\mu u^s(p) = 2p^\mu\delta^{rs}$, given $\bar u^r(p)u^s(p) = 2m\delta^{rs}$. Check $\mu = 0$ against $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$.

^px-5-3-1

**X5.3.2** *[variation of PS5.3]* Derive the axial Gordon identity $\bar u(p')\gamma^\mu\gamma^5u(p) = \frac{1}{2m}\bar u(p')\bigl[q^\mu + i\sigma^{\mu\nu}(p + p')_\nu\bigr]\gamma^5u(p)$, $q = p' - p$.

^px-5-3-2

### PS5.4 The Dirac energy–momentum tensor
*Literal re-ask: [[PHY 513 PS Drill#^ps5-4|PS Drill, PS5.4]], parts (a)–(b).*

**X5.4.1** *[variation of PS5.4(b)]* From $T^{\mu\nu} = i\bar\psi\gamma^\mu\partial^\nu\psi - g^{\mu\nu}\mathcal L$, show that on solutions $H = \int d^3x\,T^{00} = \int d^3x\,\psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$, $\boldsymbol\alpha = \gamma^0\boldsymbol\gamma$, $\beta = \gamma^0$.

^px-5-4-1

**X5.4.2** *[variation of PS5.4(a)]* Is the canonical $T^{\mu\nu}$ of the Dirac field symmetric? Compute $T^{0i} - T^{i0}$ on solutions and show it is not identically zero (one example suffices, or an argument).

^px-5-4-2

### PS5.5 The γ⁵ matrix
*Literal re-ask: [[PHY 513 PS Drill#^ps5-5|PS Drill, PS5.5]], parts (a)–(d).*

**X5.5.1** *[variation of PS5.5(b)]* Find $\gamma^5$ in the Dirac representation, $\gamma^\mu_D = U_D\gamma^\mu_WU_D^\dagger$, $U_D = \frac{1}{\sqrt2}\begin{pmatrix}\mathbb 1&\mathbb 1\\-\mathbb 1&\mathbb 1\end{pmatrix}$, $\gamma^5_W = \operatorname{diag}(-\mathbb 1, \mathbb 1)$.

^px-5-5-1

**X5.5.2** *[extension of PS5.5(c)]* From $\gamma^{[\kappa}\gamma^\lambda\gamma^\mu\gamma^{\nu]} = -i\varepsilon^{\kappa\lambda\mu\nu}\gamma^5$ derive $\operatorname{tr}(\gamma^\kappa\gamma^\lambda\gamma^\mu\gamma^\nu\gamma^5) = -4i\varepsilon^{\kappa\lambda\mu\nu}$, and check the convention-free value of $\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3\gamma^5)$.

^px-5-5-2

**X5.5.3** *[extension of PS5.5(d)]* Reduce $\gamma^\mu\gamma^\nu\gamma^\rho$ to the basis $\{\gamma^\mu, \gamma^\mu\gamma^5\}$, using $\gamma^{[\mu}\gamma^\nu\gamma^{\rho]} = i\varepsilon^{\mu\nu\rho\kappa}\gamma_\kappa\gamma^5$.

^px-5-5-3

### PS5.6 Helicity spinors
*Literal re-ask: [[PHY 513 PS Drill#^ps5-6|PS Drill, PS5.6]].*

**X5.6.1** *[variation of PS5.6]* Give $\xi_\pm(\hat{\mathbf p})$ for $\hat{\mathbf p} = -\hat{\mathbf z}$ ($\theta = \pi$, $\varphi = 0$) and for $\hat{\mathbf p} = +\hat{\mathbf x}$ ($\theta = \pi/2$, $\varphi = 0$) in the phase convention of the problem set, and check the eigenvalue equation for $+\hat{\mathbf x}$.

^px-5-6-1

**X5.6.2** *[extension of PS5.6]* Show that for $E_{\mathbf p} \gg m$, $u_+(p) \to \sqrt{2E_{\mathbf p}}\,(0, \xi_+)$ and $u_-(p) \to \sqrt{2E_{\mathbf p}}\,(\xi_-, 0)$: which chirality does each helicity become?

^px-5-6-2

### PS6.3 Representations of the Dirac matrices
*Literal re-ask: [[PHY 513 PS Drill#^ps6-3|PS Drill, PS6.3]], parts (a)–(d).*

**X6.3.1** *[variation of PS6.3(c)–(d)]* With $v(p) = (\sqrt{p\cdot\sigma}\,\eta, -\sqrt{p\cdot\bar\sigma}\,\eta)$ in the Weyl representation, find $v_D(p) = U_Dv(p)$ and check $\bar v_Dv_D = -2m$ ($\eta^\dagger\eta = 1$).

^px-6-3-1

**X6.3.2** *[variation of PS6.3(b)]* Find the boost generators $S^{0i}_D$ in the Dirac representation. Are they block diagonal?

^px-6-3-2

### PS6.5 Chiral symmetry
*Literal re-ask: [[PHY 513 PS Drill#^ps6-5|PS Drill, PS6.5]], parts (a)–(e).*

**X6.5.1** *[extension of PS6.5(b)–(c)]* Under $\psi \to e^{i\alpha\gamma^5}\psi$ (finite $\alpha$), find the images of $\mathsf S = \bar\psi\psi$, $\mathsf P = \bar\psi\,i\gamma^5\psi$ and $\mathsf A^\mu = \bar\psi\gamma^\mu\gamma^5\psi$.

^px-6-5-1

**X6.5.2** *[variation of PS6.5(d)]* Noether current of the vector phase $\psi \to e^{i\alpha}\psi$ in the same recipe and sign convention as PS6.5(d), and its divergence for general $m$.

^px-6-5-2

---

## G. Discrete symmetries (T10; K15, K5, K7)

### PS7.2 P, C, T for fermion bilinears
*Literal re-ask: [[PHY 513 PS Drill#^ps7-2|PS Drill, PS7.2]], parts (a)–(c). T on $\mathsf A^\mu$ and C on $\mathsf T^{\mu\nu}$ (the objects Peskin–Schroeder do not derive) are Problem 6 of [[PHY 513 Practice Midterm]].*

**X7.2.1** *[variation of PS7.2(c)]* Show $U(\mathcal T)\mathsf T^{\mu\nu}(x)U(\mathcal T)^{-1} = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$.

^px-7-2-1

**X7.2.2** *[variation of PS7.2(b)]* Show $U(\mathcal C)\mathsf P(x)U(\mathcal C)^{-1} = +\mathsf P(x)$, $\mathsf P = \hat{\bar\psi}\,i\gamma^5\hat\psi$, keeping track of the fermion sign.

^px-7-2-2

**X7.2.3** *[variation of PS7.2(a)]* Show $U(\mathcal P)\mathsf V^\mu(x)U(\mathcal P)^{-1} = \mathcal P^\mu{}_\nu\mathsf V^\nu(\tilde x)$ and $U(\mathcal P)\mathsf P(x)U(\mathcal P)^{-1} = -\mathsf P(\tilde x)$ in the course's $U\cdots U^{-1}$ convention.

^px-7-2-3

**X7.2.4** *[extension of PS7.2]* With $j^\mu_{L,R} = \hat{\bar\psi}\gamma^\mu\frac{1\mp\gamma^5}{2}\hat\psi$, find the images of $j^\mu_L$ under $C$ and under $P$.

^px-7-2-4

### PS7.3 CPT on the Dirac field
*Literal re-ask: [[PHY 513 PS Drill#^ps7-3|PS Drill, PS7.3]].*

**X7.3.1** *[extension of PS7.3]* From $\Theta\hat\psi(x)\Theta^{-1} = \eta_a\gamma^5\hat\psi^{\dagger\mathsf T}(-x)$ ($\Theta$ antiunitary), derive $\Theta\hat{\bar\psi}(x)\Theta^{-1}$.

^px-7-3-1

**X7.3.2** *[extension of PS7.3]* Using X7.3.1, show $\Theta\mathsf S(x)\Theta^{-1} = \mathsf S(-x)$ and $\Theta\mathsf V^\mu(x)\Theta^{-1} = -\mathsf V^\mu(-x)$ directly from the field law (fermion exchange included).

^px-7-3-2

**X7.3.3** *[variation of PS7.3]* With $\Theta' = U(\mathcal T)U(\mathcal P)U(\mathcal C)$ (first $C$), compute $\Theta'\hat\psi(x)\Theta'^{-1}$ and compare with $\Theta$.

^px-7-3-3

### PS7.4 C, P, T for the complex boson
*Literal re-ask: [[PHY 513 PS Drill#^ps7-4|PS Drill, PS7.4]], parts (a)–(c).*

**X7.4.1** *[variation of PS7.4(a)]* Real scalar field: $U(\mathcal P)\hat a_{\mathbf p}U(\mathcal P)^{-1} = \eta\,\hat a_{-\mathbf p}$, $|\eta| = 1$. Show that $U(\mathcal P)\hat\phi(x)U(\mathcal P)^{-1} = \eta\,\hat\phi(\tilde x)$ forces $\eta = \pm1$.

^px-7-4-1

**X7.4.2** *[extension of PS7.4(b)]* From the transformation of $J^\mu = i[\phi^{\ast}(\partial^\mu\phi) - (\partial^\mu\phi^{\ast})\phi]$ under $P$, $C$, $T$, find how the charge $\int d^3x\,J^0$ transforms under each, and under $\Theta$.

^px-7-4-2

**X7.4.3** *[extension of PS7.4(c)]* Let $\phi$ be the complex scalar and $\psi$ the Dirac field. Is $g\,\hat\phi\,\mathsf S + g^{\ast}\hat\phi^\dagger\mathsf S$ ($g$ complex) CPT invariant? Is $g\,\hat\phi\,\mathsf S$ alone? Use $\Theta\hat\phi(x)\Theta^{-1} = \hat\phi^\dagger(-x)$, $\Theta\mathsf S(x)\Theta^{-1} = \mathsf S(-x)$.

^px-7-4-3

---

## H. Short response (format of PS7.1; T3, T5–T10)

*Literal re-ask: [[PHY 513 PS Drill#^ps7-1|PS Drill, PS7.1]], parts (a)–(d) and the extra items X1–X8 there. A formula, a number or a phrase each; no derivation. Twelve more for the round of Problem 1 of [[PHY 513 Practice Midterm]] are below; aim for under a minute each.*

- **X7.1.1** *[variation of PS7.1(a)]* In $d = 3$ spacetime dimensions: $[\phi]$, $[\psi]$ and $[g]$ for $g\phi\bar\psi\psi$, as $M^\alpha$.
- **X7.1.2** *[variation of PS7.1(b)]* Euler–Lagrange equation for $\mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi - \lambda(\phi^{\ast}\phi)^2$ (the equation for $\phi$).
- **X7.1.3** *[HW-literal: PS5.2(d)]* $\gamma_\mu\slashed k\slashed p\slashed q\gamma^\mu = ?$
- **X7.1.4** *[variation of PS7.1(d)]* $(j_+, j_-)$ of the product of a $(\frac12, 0)$ and a $(0, \frac12)$ spinor; of a symmetric traceless tensor $h^{\mu\nu}$.
- **X7.1.5** *[variation of PS3.3(c)]* $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = ?$ and $\lvert\mathbf p\rangle = ?\,\hat a^\dagger_{\mathbf p}\lvert0\rangle$ (course normalisation).
- **X7.1.6** *[variation of PS4.4]* $\tilde D_R(p)$ with its $i\varepsilon$; on which side of the poles its contour passes.
- **X7.1.7** *[variation of PS4.3(b)]* $[\hat\phi(x), \hat\phi(y)]$ at spacelike $x - y$, and the principle's name.
- **X7.1.8** *[variation of PS6.2]* $:\!\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\!: = ?$
- **X7.1.9** *[HW-literal: PS7.3, with the phase]* $\Theta\hat\psi(x)\Theta^{-1} = ?$ for parity phase $\eta_a$.
- **X7.1.10** *[variation of PS7.2]* Under $\Theta$, a bilinear with $n$ Lorentz indices is multiplied by ? ; $U(\mathcal T)^2$ on a one-fermion state = ?
- **X7.1.11** *[variation of PS6.3(d)]* $\bar u^r(p)u^s(p)$, $\bar v^r(p)v^s(p)$, $u^{r\dagger}(p)u^s(p)$.
- **X7.1.12** *[variation of PS1.3(a)]* $\varepsilon^{0123}$ in Peskin–Schroeder; the sign of $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ in terms of $\mathbf E\cdot\mathbf B$ in the course's convention.

^px-7-1

---

*Sources:* Problem Sets 1–7 (Larsen, PHY 513, Fall 2026; all submitted); Peskin–Schroeder §§2.2–3.6 for what the book already derives (pp. 18, 27, 30, 42, 51, 66–71); Larsen's comments in Lecture 13 (Oct 14) and the PS7 PDF. Purpose of each homework problem: `qft-C/review/PURPOSE.md`.
