---
type: card
subject: "[[Quantum Field Theory]]"
level: C
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, card]
---
# Scalar Field Card

One-page reference for the free real and complex scalar field (canonical quantization, states, coherent states, two-point functions, classical source); every formula is stated and derived in its home box in [[· C2a The Quantum Scalar Field|C2a The Quantum Scalar Field]] and [[· C2b Two-Point Functions, Causality and Propagators|C2b Two-Point Functions, Causality and Propagators]] (the Poincaré action in [[· C3 Poincaré Symmetry and Particle States|C3]]), linked after it. Conventions: $\hbar = c = 1$, $g = \mathrm{diag}(+,-,-,-)$, $p^0 = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$ on shell, $\xi = x - y$.

## 1. Lagrangian, momentum, Hamiltonian; commutators

| | Real field | Complex field |
| --- | --- | --- |
| $\mathcal L$ | $\frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$ | $\partial_\mu\phi^\dagger\,\partial^\mu\phi - m^2\phi^\dagger\phi$ |
| momentum density | $\pi = \dot\phi$ | $\pi = \partial\mathcal L/\partial\dot\phi = \dot\phi^\dagger$, $\pi^\dagger = \dot\phi$ |
| $H = \int d^3x\,\mathcal H$ | $\mathcal H = \frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2$ | $\mathcal H = \pi^\dagger\pi + \nabla\phi^\dagger\cdot\nabla\phi + m^2\phi^\dagger\phi$ |
| equal-time relations | $[\phi(\mathbf x), \pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, $[\phi, \phi] = [\pi, \pi] = 0$ | $[\phi(\mathbf x), \pi(\mathbf y)] = [\phi^\dagger(\mathbf x), \pi^\dagger(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$; all others $0$, incl. $[\phi, \pi^\dagger]$, $[\phi, \phi^\dagger]$ |
| home | [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1\|Model §C2a.1.1]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2\|Principle §C2a.1.2]] | [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1\|Model §C2a.5.1]] |

- General postulate: $[\phi_a(\mathbf x), \pi_b(\mathbf y)] = i\,\delta_{ab}\,\delta^3(\mathbf x - \mathbf y)$, $[\phi_a, \phi_b] = [\pi_a, \pi_b] = 0$ — [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]]
- Classical modes: $H = \int\frac{d^3p}{(2\pi)^3}\frac12\bigl[|\tilde\pi(\mathbf p)|^2 + E_{\mathbf p}^2|\tilde\phi(\mathbf p)|^2\bigr]$, one oscillator of frequency $E_{\mathbf p}$ per $\mathbf p$ — [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-1|Theorem §C2a.2.1]]
- Heisenberg field $\phi(x) = e^{iHt}\phi_S(\mathbf x)e^{-iHt}$ — [[§C2b.1 Heisenberg Fields#^def-c2b-1-1|Def. §C2b.1.1]]; relations hold at every common time — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]]; $\partial_t\phi = \pi$, $\partial_t\pi = (\nabla^2 - m^2)\phi$, $(\partial_\mu\partial^\mu + m^2)\phi = 0$ — [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]]

## 2. Modes

| | Formula | Home |
| --- | --- | --- |
| real field | $\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(a_{\mathbf p}e^{-ip\cdot x} + a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$, $\pi(x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(a_{\mathbf p}e^{-ip\cdot x} - a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$ | [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4\|Theorem §C2b.1.4]] |
| real field at $t = 0$ | $\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(a_{\mathbf p} + a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x}$, $\pi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(a_{\mathbf p} - a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x}$ | [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2\|Theorem §C2a.2.2]] |
| Heisenberg modes | $e^{iHt}a_{\mathbf p}e^{-iHt} = a_{\mathbf p}e^{-iE_{\mathbf p}t}$, $e^{iHt}a^\dagger_{\mathbf p}e^{-iHt} = a^\dagger_{\mathbf p}e^{iE_{\mathbf p}t}$ | [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4\|Theorem §C2b.1.4]] |
| complex field | $\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(a_{\mathbf p}e^{-ip\cdot x} + b^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$, $\phi^\dagger(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(b_{\mathbf p}e^{-ip\cdot x} + a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2\|Theorem §C2a.5.2]] |
| mode algebra (real) | $[a_{\mathbf p}, a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $[a_{\mathbf p}, a_{\mathbf q}] = [a^\dagger_{\mathbf p}, a^\dagger_{\mathbf q}] = 0$ | [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6\|Theorem §C2a.2.6]] |
| mode algebra (complex) | $[a_{\mathbf p}, a^\dagger_{\mathbf q}] = [b_{\mathbf p}, b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$; all others $0$, incl. $[a, b]$, $[a, b^\dagger]$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3\|Theorem §C2a.5.3]] |
| KG inner product | $(f, g) = i\int d^3x\,\bigl(f^*\partial_tg - (\partial_tf^*)g\bigr)$; modes $f_{\mathbf p} = e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$ | [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1\|Def. §C2a.2.1]] |
| orthonormality | $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $(f^*_{\mathbf p}, f^*_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $(f_{\mathbf p}, f^*_{\mathbf q}) = 0$; $(f, g)$ time independent | [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3\|Theorem §C2a.2.3]] |
| mode extraction | $a_{\mathbf p} = (f_{\mathbf p}, \phi) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\bigl(\pi - iE_{\mathbf p}\phi\bigr)$, $a^\dagger_{\mathbf p} = -(f^*_{\mathbf p}, \phi)$ | [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5\|Theorem §C2a.2.5]] |
| extraction (complex) | $a_{\mathbf p} = (f_{\mathbf p}, \phi)$, $b_{\mathbf p} = (f_{\mathbf p}, \phi^\dagger)$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2\|Theorem §C2a.5.2]] |
| frequency split | $\phi^+ = \int\frac{d^3p}{(2\pi)^3}\frac{a_{\mathbf p}e^{-ip\cdot x}}{\sqrt{2E_{\mathbf p}}}$, $\phi^- = (\phi^+)^\dagger$; $\phi^+\lvert0\rangle = 0$, $\langle0\rvert\phi^- = 0$ | [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5\|Theorem §C2b.1.5]] |

## 3. Energy, momentum, normal ordering

| | Formula | Home |
| --- | --- | --- |
| $H$ (real) | $\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}\bigl(a_{\mathbf p}a^\dagger_{\mathbf p} + a^\dagger_{\mathbf p}a_{\mathbf p}\bigr) = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}a^\dagger_{\mathbf p}a_{\mathbf p} + E_0$ | [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1\|Theorem §C2a.3.1]] |
| zero-point energy | $E_0 = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$, $V = (2\pi)^3\delta^3(\mathbf 0) = \int d^3x$; $\varepsilon_0 = E_0/V \approx \Lambda^4/16\pi^2$ | [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3\|Theorem §C2a.3.3]] |
| normal ordering | creators left of annihilators, e.g. $:\!a_{\mathbf p}a^\dagger_{\mathbf q}\!: = a^\dagger_{\mathbf q}a_{\mathbf p}$; $:\!H\!: = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}a^\dagger_{\mathbf p}a_{\mathbf p}$, $:\!H\!:\lvert0\rangle = 0$ | [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1\|Def. §C2a.3.1]] |
| $\mathbf P$ (real) | $\mathbf P = -\int d^3x\,\pi\nabla\phi = \int\frac{d^3p}{(2\pi)^3}\mathbf p\,a^\dagger_{\mathbf p}a_{\mathbf p}$ (no constant) | [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4\|Theorem §C2a.3.4]] |
| ladder relations | $[H, a^\dagger_{\mathbf p}] = E_{\mathbf p}a^\dagger_{\mathbf p}$, $[H, a_{\mathbf p}] = -E_{\mathbf p}a_{\mathbf p}$, $[\mathbf P, a^\dagger_{\mathbf p}] = \mathbf p\,a^\dagger_{\mathbf p}$, $[\mathbf P, a_{\mathbf p}] = -\mathbf p\,a_{\mathbf p}$ | [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-6\|Theorem §C2a.3.6]] |
| $H$ (complex) | $\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(a^\dagger_{\mathbf p}a_{\mathbf p} + b^\dagger_{\mathbf p}b_{\mathbf p}\bigr) + 2E_0$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4\|Theorem §C2a.5.4]] |
| $\mathbf P$ (complex) | $-\int d^3x\bigl(\pi\nabla\phi + \pi^\dagger\nabla\phi^\dagger\bigr) = \int\frac{d^3p}{(2\pi)^3}\mathbf p\bigl(a^\dagger_{\mathbf p}a_{\mathbf p} + b^\dagger_{\mathbf p}b_{\mathbf p}\bigr)$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5\|Theorem §C2a.5.5]] |

## 4. States

| | Formula | Home |
| --- | --- | --- |
| vacuum, Fock space | $a_{\mathbf p}\lvert0\rangle = 0$ for all $\mathbf p$; $\mathcal F = \bigoplus_{n\ge0}\mathcal H_n$, $\mathcal H_n = \operatorname{Sym}^n\mathcal H_1$; $\langle0\rvert a_{\mathbf q}a^\dagger_{\mathbf p}\lvert0\rangle = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ | [[§C2a.4 Particles and Relativistic Normalization#^pr-c2a-4-1\|Principle §C2a.4.1]] |
| spectrum | $a^\dagger_{\mathbf p_1}\cdots a^\dagger_{\mathbf p_n}\lvert0\rangle$: energy $\sum E_{\mathbf p_i}$, momentum $\sum\mathbf p_i$; $N = \int\frac{d^3p}{(2\pi)^3}a^\dagger_{\mathbf p}a_{\mathbf p}$, $[N, H] = [N, \mathbf P] = 0$; $:\!H\!:\,\ge 0$ | [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2\|Theorem §C2a.4.2]] |
| Bose statistics | $\langle0\rvert a_{\mathbf q_2}a_{\mathbf q_1}a^\dagger_{\mathbf p_1}a^\dagger_{\mathbf p_2}\lvert0\rangle = (2\pi)^6\bigl[\delta^3(\mathbf q_1 - \mathbf p_1)\delta^3(\mathbf q_2 - \mathbf p_2) + \delta^3(\mathbf q_1 - \mathbf p_2)\delta^3(\mathbf q_2 - \mathbf p_1)\bigr]$ | [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3\|Theorem §C2a.4.3]] |
| $\lvert\mathbf p\rangle$ | $\lvert\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,a^\dagger_{\mathbf p}\lvert0\rangle$, $\langle\mathbf p\vert\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ (Lorentz invariant) | [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1\|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5\|Theorem §C2a.4.5]] |
| invariant measure | $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}} = \int\frac{d^4p}{(2\pi)^4}2\pi\,\delta(p^2 - m^2)\theta(p^0)$ | [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2\|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4\|Theorem §C2a.4.4]] |
| Poincaré action | $U(\Lambda, a)\lvert\mathbf p\rangle = e^{i(\Lambda p)\cdot a}\lvert\Lambda\mathbf p\rangle$, $U(\Lambda, a)\lvert0\rangle = \lvert0\rangle$; $U a^\dagger_{\mathbf p}U^{-1} = e^{i(\Lambda p)\cdot a}\sqrt{E_{\Lambda\mathbf p}/E_{\mathbf p}}\,a^\dagger_{\Lambda\mathbf p}$; generators $P^\mu = \int\frac{d^3p}{(2\pi)^3}p^\mu a^\dagger_{\mathbf p}a_{\mathbf p}$ | [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-11\|Theorem §C3.5.11]] |
| field under $U$ | $U(\Lambda, a)\,\phi(x)\,U(\Lambda, a)^{-1} = \phi(\Lambda x + a)$ | [[§C3.5 Quantum Poincaré Transformations#^thm-c3-5-12\|Theorem §C3.5.12]] |
| completeness | $\mathbb 1_{1\text{-particle}} = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\lvert\mathbf p\rangle\langle\mathbf p\rvert$ | [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2\|Def. §C2a.4.2]] |
| field on vacuum | $\phi(\mathbf x)\lvert0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-i\mathbf p\cdot\mathbf x}\lvert\mathbf p\rangle$; $\langle0\rvert\phi(x)\lvert\mathbf p\rangle = e^{-ip\cdot x}$, $\langle\mathbf p\rvert\phi(x)\lvert0\rangle = e^{ip\cdot x}$ | [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-7\|Theorem §C2a.4.7]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5\|Theorem §C2b.1.5]] |
| charge (complex) | $Q = \frac i2\int d^3x\,:\!\bigl(\phi^\dagger\pi^\dagger - \pi\phi\bigr)\!: = \frac i2\int d^3x\,:\!\phi^\dagger\overleftrightarrow{\partial_t}\phi\!:$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1\|Def. §C2a.5.1]] |
| charge in modes | $Q = \frac12\int\frac{d^3p}{(2\pi)^3}\bigl(a^\dagger_{\mathbf p}a_{\mathbf p} - b^\dagger_{\mathbf p}b_{\mathbf p}\bigr) = \frac12(N_a - N_b)$; $[Q, a^\dagger_{\mathbf p}] = +\frac12a^\dagger_{\mathbf p}$, $[Q, b^\dagger_{\mathbf p}] = -\frac12b^\dagger_{\mathbf p}$; $[Q, H] = [Q, \mathbf P] = 0$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6\|Theorem §C2a.5.6]] |
| eigenvalues | $n_a$ $a$-quanta, $n_b$ $b$-quanta: $Q = \frac12(n_a - n_b)$; both species mass $m$, charges $\pm\frac12$; real field $Q \equiv 0$ | [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7\|Theorem §C2a.5.7]] |

## 5. Coherent states

| | Formula | Home |
| --- | --- | --- |
| definition | $\lvert\{\eta\}\rangle = e^{-\bar N/2}\exp\Bigl\{\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}a^\dagger_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}\Bigr\}\lvert0\rangle$, $\bar N = \int\frac{d^3k}{(2\pi)^3}\frac{\lvert\eta_{\mathbf k}\rvert^2}{2E_{\mathbf k}}$ | [[§C2a.6 Coherent States and the Classical Field#^def-c2a-6-1\|Def. §C2a.6.1]] |
| eigenstate | $a_{\mathbf p}\lvert\{\eta\}\rangle = \frac{\eta_{\mathbf p}}{\sqrt{2E_{\mathbf p}}}\lvert\{\eta\}\rangle$, $\langle\{\eta\}\vert\{\eta\}\rangle = 1$ | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-2\|Theorem §C2a.6.2]] |
| displaced vacuum | $\lvert\{\eta\}\rangle = D(\eta)\lvert0\rangle$, $D(\eta) = \exp\int\frac{d^3k}{(2\pi)^3}\frac{\eta_{\mathbf k}a^\dagger_{\mathbf k} - \eta^*_{\mathbf k}a_{\mathbf k}}{\sqrt{2E_{\mathbf k}}}$ unitary; $D^\dagger a_{\mathbf p}D = a_{\mathbf p} + \eta_{\mathbf p}/\sqrt{2E_{\mathbf p}}$ | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-3\|Theorem §C2a.6.3]] |
| mean field | $\bar\phi(x) = \langle\{\eta\}\rvert\phi(x)\lvert\{\eta\}\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}\bigl(\eta_{\mathbf p}e^{-ip\cdot x} + \eta^*_{\mathbf p}e^{ip\cdot x}\bigr)$, a real KG solution | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-4\|Theorem §C2a.6.4]] |
| evolution | $e^{-i:H:t}\lvert\{\eta_{\mathbf k}\}\rangle = \lvert\{\eta_{\mathbf k}e^{-iE_{\mathbf k}t}\}\rangle$ | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-5\|Theorem §C2a.6.5]] |
| Poisson statistics | $P(n) = e^{-\bar N}\bar N^n/n!$; $\langle N\rangle = \bar N$, $\langle(\Delta N)^2\rangle = \bar N$, $\Delta N/\bar N = 1/\sqrt{\bar N}$ | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-6\|Theorem §C2a.6.6]] |
| fluctuations | $\langle\{\eta\}\rvert(\phi(x) - \bar\phi(x))(\phi(y) - \bar\phi(y))\lvert\{\eta\}\rangle = \langle0\rvert\phi(x)\phi(y)\lvert0\rangle$ | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-7\|Theorem §C2a.6.7]] |
| number eigenstate | $N\lvert\psi\rangle = n\lvert\psi\rangle \Rightarrow \langle\psi\rvert\phi(x)\lvert\psi\rangle = 0$ | [[§C2a.6 Coherent States and the Classical Field#^thm-c2a-6-1\|Theorem §C2a.6.1]] |

## 6. Two-point functions

All entries are tempered distributions; the column "As a distribution" says in what sense. Homogeneous: $(\partial^2 + m^2)f = 0$. Green's: $(\partial_x^2 + m^2)D_C(x - y) = -i\delta^4(x - y)$ — [[§C2b.5 Green's Functions and Contours#^def-c2b-5-1|Def. §C2b.5.1]]. Momentum space below means $f(\xi) = \int\frac{d^4p}{(2\pi)^4}\tilde f(p)e^{-ip\cdot\xi}$; contours pass the poles $p^0 = -E_{\mathbf p}$ / $+E_{\mathbf p}$ ([[§C2b.5 Green's Functions and Contours#^def-c2b-5-2|Def. §C2b.5.2]]).

| Name | Definition | Momentum space / contour | Support, key property | As a distribution | Home |
| --- | --- | --- | --- | --- | --- |
| Wightman $D_W(\xi)$ (PS: $D$) | $\langle0\vert\phi(x)\phi(y)\vert0\rangle$ | $2\pi\theta(p^0)\delta(p^2 - m^2)$, i.e. $\int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-ip\cdot\xi}$ | homogeneous; nonzero outside the cone; $D_W(-\xi) = \overline{D_W(\xi)}$; Lorentz invariant | boundary value from $\operatorname{Im}\xi^0 < 0$; acts as $f \mapsto \int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}\tilde f(-p)$; singular on the cone — [[§C2b.2 The Wightman Function#^thm-c2b-2-2\|Theorem §C2b.2.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-6\|Theorem §C2b.3.6]] | [[§C2b.2 The Wightman Function#^def-c2b-2-1\|Def. §C2b.2.1]], [[§C2b.2 The Wightman Function#^thm-c2b-2-1\|Theorem §C2b.2.1]] |
| commutator $iD(\xi)$ | $\langle0\vert[\phi(x), \phi(y)]\vert0\rangle = [\phi(x), \phi(y)]$ | $2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ | homogeneous; $D = 2\operatorname{Im}D_W$, real, odd; $D = 0$ for $\xi^2 < 0$; $D(0, \boldsymbol\xi) = 0$, $\partial_0D(0, \boldsymbol\xi) = -\delta^3(\boldsymbol\xi)$ | difference of boundary values; vanishes on the open spacelike region — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4\|Theorem §C2b.4.4]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-6\|Theorem §C2b.4.6]] | [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-1\|Def. §C2b.4.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2\|Theorem §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-12\|Theorem §C2b.4.12]] |
| Hadamard $D_1(\xi)$ | $\langle0\vert\{\phi(x), \phi(y)\}\vert0\rangle$ | $2\pi\delta(p^2 - m^2)$ | homogeneous; $D_1 = 2\operatorname{Re}D_W$, real, even; nonzero outside the cone | sum of boundary values; massless: $-\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-4\|Theorem §C2b.4.4]] | [[§C2b.4 Microcausality and the Commutator Function#^def-c2b-4-2\|Def. §C2b.4.2]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3\|Theorem §C2b.4.3]] |
| retarded $D_R(\xi)$ | $\theta(\xi^0)\langle0\vert[\phi(x), \phi(y)]\vert0\rangle = \theta(\xi^0)\,iD(\xi)$ | $\frac{i}{(p^0 + i\varepsilon)^2 - E_{\mathbf p}^2}$; above / above | Green's; forward light cone (inside or on) | $\theta\cdot iD$ slice by slice; unique fundamental solution supported in $\xi^0 \ge 0$ — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6\|Theorem §C2b.5.6]] | [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-5\|Theorem §C2b.5.5]] |
| advanced $D_A(\xi)$ | $-\theta(-\xi^0)\langle0\vert[\phi(x), \phi(y)]\vert0\rangle = -\theta(-\xi^0)\,iD(\xi)$ | $\frac{i}{(p^0 - i\varepsilon)^2 - E_{\mathbf p}^2}$; below / below | Green's; backward light cone | mirror of $D_R$ — [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-6\|Theorem §C2b.5.6]] | [[§C2b.5 Green's Functions and Contours#^thm-c2b-5-7\|Theorem §C2b.5.7]] |
| Feynman $D_F(\xi)$ | $\langle0\vert T\{\phi(x)\phi(y)\}\vert0\rangle = \theta(\xi^0)D_W(\xi) + \theta(-\xi^0)D_W(-\xi)$ | $\frac{i}{p^2 - m^2 + i\varepsilon}$; below / above | Green's; even, Lorentz invariant; $D_F = D_R + D_W(-\xi)$; $D_F = \frac{mK_1(ms)}{4\pi^2s}$, $s = \sqrt{-\xi^2 + i\varepsilon}$ | limit $\varepsilon \to 0^+$ in $\mathcal S'$; extension of $\theta\cdot D_W$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10\|Theorem §C2b.6.10]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-4\|Theorem §C2b.6.4]] | [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2\|Theorem §C2b.6.2]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-3\|Theorem §C2b.7.3]] |
| anti-Feynman $D_{\bar F}(\xi)$ | $-\langle0\vert\bar T\{\phi(x)\phi(y)\}\vert0\rangle = -\theta(\xi^0)D_W(-\xi) - \theta(-\xi^0)D_W(\xi)$ | $\frac{i}{p^2 - m^2 - i\varepsilon}$; above / below | Green's; $D_{\bar F} = -\overline{D_F}$ | conjugate limit ($-i\varepsilon$) — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-10\|Theorem §C2b.6.10]] | [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-3\|Theorem §C2b.6.3]], [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-2\|Def. §C2b.6.2]] |
| principal $\bar D(\xi)$ | $\frac12(D_R + D_A) = \frac12\operatorname{sgn}(\xi^0)\,iD$ | $i\,\mathcal P\frac{1}{p^2 - m^2}$ | Green's; zero for $\xi^2 < 0$ | slice product $\frac12\operatorname{sgn}(\xi^0)\,iD$; transform a principal value — [[§CA.2 Generalized Functions#^def-ca-2-6\|Def. §CA.2.6]] | [[§C2b.5 Green's Functions and Contours#^def-c2b-5-3\|Def. §C2b.5.3]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5\|Theorem §C2b.7.5]] |
| Euclidean $D_E(x_E)$ | $D_E(\tau, \boldsymbol\xi) = D_F(-i\tau, \boldsymbol\xi)$, $\tau > 0$ | $\int\frac{d^4p_E}{(2\pi)^4}\frac{e^{ip_E\cdot x_E}}{p_E^2 + m^2}$; denominator never vanishes | $O(4)$ invariant; $D_E = \frac{mK_1(mR)}{4\pi^2R}$, $R = \lvert x_E\rvert$ | locally integrable function, singular only at $x_E = 0$; the same analytic function as $D_F$ — [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-4\|Theorem §C2b.7.4]] | [[§C2b.7 Wick Rotation and the Two-Point Family#^def-c2b-7-1\|Def. §C2b.7.1]], [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-2\|Theorem §C2b.7.2]], [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-1\|Theorem §C2b.3.1]] |

Relations:
- $D_W(\pm\xi) = \frac12\bigl(D_1(\xi) \pm iD(\xi)\bigr)$; $D = -\int\frac{d^3p}{(2\pi)^3}\frac{\sin(p\cdot\xi)}{E_{\mathbf p}}$, $D_1 = \int\frac{d^3p}{(2\pi)^3}\frac{\cos(p\cdot\xi)}{E_{\mathbf p}}$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-3|Theorem §C2b.4.3]]
- $D_R - D_A = iD$; $D_F = \frac12D_1 + \bar D$, $D_{\bar F} = -\frac12D_1 + \bar D$; $D_F - D_{\bar F} = D_1$; $D_F = D_R + D_W(-\xi) = D_A + D_W(\xi)$; spacelike: $D_R = D_A = \bar D = 0$, $D_F = D_W = \frac12D_1$ — [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-5|Theorem §C2b.7.5]]
- $\tilde D_R = \frac{i}{p^2 - m^2 + i\varepsilon\operatorname{sgn}p^0}$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]; $\tilde D_F - \tilde D_{\bar F} = 2\pi\delta(p^2 - m^2)$, $\tilde D_R - \tilde D_A = 2\pi\operatorname{sgn}(p^0)\delta(p^2 - m^2)$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-11|Theorem §C2b.6.11]]
- $T\{\phi(x)\phi(y)\} = \theta(x^0 - y^0)\phi(x)\phi(y) + \theta(y^0 - x^0)\phi(y)\phi(x)$, $\theta(0) = \frac12$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^def-c2b-6-1|Def. §C2b.6.1]]; $\phi(x)\phi(y) = \,:\!\phi(x)\phi(y)\!:\, + D_W(x - y)$, $T\{\phi(x)\phi(y)\} = \,:\!\phi(x)\phi(y)\!:\, + D_F(x - y)$ — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-6|Theorem §C2b.6.6]]
- Wick rotation: $\int\frac{d^4p}{(2\pi)^4}\frac{iF(p)}{p^2 - m^2 + i\varepsilon} = \int\frac{d^4p_E}{(2\pi)^4}\frac{F(ip_4, \mathbf p)}{p_E^2 + m^2}$ — [[§C2b.7 Wick Rotation and the Two-Point Family#^thm-c2b-7-1|Theorem §C2b.7.1]]

Explicit $D_W$:

| Region | $D_W(\xi)$ | Home |
| --- | --- | --- |
| spacelike, $\xi^2 = -r^2$ | $\frac{m}{4\pi^2r}K_1(mr)$; $\simeq\frac{1}{4\pi^2r^2}$ ($mr \ll 1$); $\simeq\frac{\sqrt m}{2(2\pi r)^{3/2}}e^{-mr}\bigl(1 + \frac{3}{8mr} + \cdots\bigr)$ ($mr \gg 1$) | [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-3\|Theorem §C2b.3.3]] |
| timelike, $\xi^2 = \tau^2$ | $\frac{m}{8\pi\tau}\bigl[Y_1(m\tau) + i\operatorname{sgn}(\xi^0)J_1(m\tau)\bigr]$; at $\boldsymbol\xi = 0$, $mt \gg 1$: $\simeq\frac{\sqrt m}{4\pi^2}\sqrt{\frac\pi2}\,e^{-3\pi i/4}t^{-3/2}e^{-imt}$ | [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-4\|Theorem §C2b.3.4]] |
| near the cone; massless | $-\frac{1}{4\pi^2[(\xi^0 - i\varepsilon)^2 - \boldsymbol\xi^2]} + \frac{m^2}{8\pi^2}\ln\frac{ms}{2} + \cdots$, $s = \sqrt{\boldsymbol\xi^2 - (\xi^0 - i\varepsilon)^2}$; first term exact for $m = 0$ | [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-5\|Theorem §C2b.3.5]] |
| one analytic function | $W(z, \boldsymbol\xi) = \frac{mK_1(ms)}{4\pi^2s}$, $s = \sqrt{\boldsymbol\xi^2 - z^2}$, $\operatorname{Im}z < 0$; $D_W(\xi) = \lim_{\varepsilon\to0^+}W(\xi^0 - i\varepsilon, \boldsymbol\xi)$ | [[§C2b.3 Explicit Forms of the Wightman Function#^thm-c2b-3-2\|Theorem §C2b.3.2]], [[§C2b.2 The Wightman Function#^thm-c2b-2-5\|Theorem §C2b.2.5]] |

- $D$ and $D_1$: $m = 0$: $D = -\frac{1}{2\pi}\operatorname{sgn}(\xi^0)\delta(\xi^2)$, $D_1 = -\frac{1}{2\pi^2}\mathcal P\frac{1}{\xi^2}$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-8|Theorem §C2b.4.8]]; $m > 0$: inside $D = \operatorname{sgn}(\xi^0)\frac{mJ_1(m\tau)}{4\pi\tau}$, $D_1 = \frac{mY_1(m\tau)}{4\pi\tau}$; outside $D = 0$, $D_1 = \frac{mK_1(mr)}{2\pi^2r}$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-9|Theorem §C2b.4.9]]

Microcausality:
- Postulate: $[\mathcal O_1(x), \mathcal O_2(y)] = 0$ for $(x - y)^2 < 0$; for fields built from $\phi$ it suffices that $[\phi(x), \phi(y)] = 0$ there (complex: also $[\phi(x), \phi^\dagger(y)] = 0$) — [[§C2b.4 Microcausality and the Commutator Function#^pr-c2b-4-1|Principle §C2b.4.1]]
- Free field: $[\phi(x), \phi(y)] = D_W(x - y) - D_W(y - x) = iD(x - y)\,\mathbf 1$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-2|Theorem §C2b.4.2]]; $D(\xi) = 0$ for $\xi^2 < 0$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-5|Theorem §C2b.4.5]]
- Unequal times: $[\phi(x), \pi(y)] = i\,\partial_{y^0}D(x - y)$, $[\pi(x), \pi(y)] = i\,\partial_{x^0}\partial_{y^0}D(x - y)$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]]; $\phi(x) = -\int d^3y\,\bigl[D(x - y)\pi(y) - \partial_{y^0}D(x - y)\phi(y)\bigr]$ — [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-13|Theorem §C2b.4.13]]

## 7. Classical source

| | Formula | Home |
| --- | --- | --- |
| model | $\mathcal L = \frac12(\partial_\mu\phi)^2 - \frac12m^2\phi^2 + j\phi$, $(\partial^2 + m^2)\phi = j$; $\tilde j(p) = \int d^4y\,e^{ip\cdot y}j(y)$ | [[§C2b.5 Green's Functions and Contours#^mod-c2b-5-1\|Model §C2b.5.1]] |
| late-time field | $\phi(x) = \phi_0(x) + i\int d^4y\,D_R(x - y)j(y)$; after the source, modes $b_{\mathbf p} = a_{\mathbf p} + \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\big\vert_{p^0 = E_{\mathbf p}}$ | [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-1\|Theorem §C2b.8.1]] |
| produced state | $b_{\mathbf p}\lvert0\rangle = \frac{i\tilde j(p)}{\sqrt{2E_{\mathbf p}}}\lvert0\rangle$: coherent state with $\eta_{\mathbf p} = i\tilde j(E_{\mathbf p}, \mathbf p)$, Poisson number | [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-2\|Theorem §C2b.8.2]] |
| energy and number | $\Delta E = \int\frac{d^3p}{(2\pi)^3}\frac12\lvert\tilde j(p)\rvert^2$, $\bar N = \int\frac{d^3p}{(2\pi)^3}\frac{\lvert\tilde j(p)\rvert^2}{2E_{\mathbf p}}$, $p^0 = E_{\mathbf p}$ | [[§C2b.8 Particle Production by a Classical Source#^thm-c2b-8-3\|Theorem §C2b.8.3]] |
| Gaussian point source | $j = g\,\delta^3(\mathbf x)\frac{e^{-t^2/2T^2}}{\sqrt{2\pi}T}$: $\bar N = \frac{g^2m^2}{16\pi^2}e^{-z}\bigl[K_1(z) - K_0(z)\bigr]$, $z = \frac12m^2T^2$ | [[§C2b.8 Particle Production by a Classical Source#^ex-c2b-8-1\|Example §C2b.8.1]] |

## 8. Procedures

**[[P1 Canonical Quantization]]**
1. Canonical pairs $\pi_a = \partial\mathcal L/\partial\dot\phi_a$, $H = \int d^3x\,(\sum_a\pi_a\dot\phi_a - \mathcal L)$ — [[P1 Canonical Quantization#^p1-1|P1, step 1]]
2. Impose $[\phi_a(\mathbf x), \pi_b(\mathbf y)] = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, others zero — [[P1 Canonical Quantization#^p1-2|P1, step 2]]
3. Expand in on-shell plane waves with $1/\sqrt{2E_{\mathbf p}}$ — [[P1 Canonical Quantization#^p1-3|P1, step 3]]
4. Extract modes by the KG product; derive $[a_{\mathbf p}, a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ — [[P1 Canonical Quantization#^p1-4|P1, step 4]]
5. $H$, $\mathbf P$, $Q$ in modes; normal order — [[P1 Canonical Quantization#^p1-5|P1, step 5]]
6. Vacuum, Fock space; read off mass, charge, statistics — [[P1 Canonical Quantization#^p1-6|P1, step 6]]
7. Normalize $\lvert\mathbf p\rangle = \sqrt{2E_{\mathbf p}}a^\dagger_{\mathbf p}\lvert0\rangle$; invariant measure — [[P1 Canonical Quantization#^p1-7|P1, step 7]]

**[[P2 Green's Functions by Contour Integration]]**
1. Fourier transform: $\tilde D_C = i/(p^2 - m^2)$ off shell — [[P2 Green's Functions by Contour Integration#^p2-1|P2, step 1]]
2. Separate $\int dp^0$; poles at $p^0 = \pm E_{\mathbf p}$, residues — [[P2 Green's Functions by Contour Integration#^p2-2|P2, step 2]]
3. Choose the contour ($\equiv$ $i\varepsilon$ $\equiv$ boundary condition) — [[P2 Green's Functions by Contour Integration#^p2-3|P2, step 3]]
4. Close down for $t > 0$, up for $t < 0$; check the arc — [[P2 Green's Functions by Contour Integration#^p2-4|P2, step 4]]
5. Down: $-2\pi i\sum\operatorname{Res}$; up: $+2\pi i\sum\operatorname{Res}$ — [[P2 Green's Functions by Contour Integration#^p2-5|P2, step 5]]
6. $\mathbf p \to -\mathbf p$ in negative-frequency terms; recognize $D_W(\pm\xi)$, $iD$ — [[P2 Green's Functions by Contour Integration#^p2-6|P2, step 6]]
7. Check: jump $-i$ in $G'$, support, on-shell differences, $m \to 0$ — [[P2 Green's Functions by Contour Integration#^p2-7|P2, step 7]]

## 9. Pitfalls

- $E_{\mathbf p}$ here is the lectures' $\omega_{\mathbf p}$, and $\pi$ their $\Pi$ — [[§C2a.1 Canonical Quantization of Fields#^cau-c2a-1-1|Caution §C2a.1]]
- $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$: the slides drop the $(2\pi)^3$ — [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-2|Caution §C2a.4]]
- Charge: $\frac12(N_a - N_b)$ here, PS and Problem Set 3; Noether current with $\Delta\phi = +i\phi$ gives $N_b - N_a$; Yu $q(N_a - N_b)$ — [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|Caution §C2a.5]], [[§C1b.5 Noether's Theorem#^cau-c1b-5-3|Caution §C1b.5]]
- $D_F(x - y) = D_R(x - y) + D_W(y - x)$ (arguments exchanged); $(\partial^2 + m^2)e^{-ip\cdot x} = (m^2 - p^2)e^{-ip\cdot x}$; closing up is counterclockwise, down clockwise — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^cau-c2b-6-2|Caution §C2b.6]]
- $(2\pi)^3\delta^3(\mathbf 0) = V$, i.e. $\delta^3(\mathbf 0) = V/(2\pi)^3$; a $\delta^3(\mathbf 0)$ from two different momenta signals a dropped sign — [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-3|Theorem §C2a.3.3]], [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-2|Remark §C2a.2]]
- PS's $D$ is $D_W$ here; Yu's $D_{\mathrm{PJ}} = iD$ — [[§C2b.4 Microcausality and the Commutator Function#^cau-c2b-4-1|Caution §C2b.4]]
