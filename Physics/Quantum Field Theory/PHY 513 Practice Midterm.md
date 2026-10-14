---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Practice Midterm Solutions|Solutions]] · [[PHY 513 Practice Midterm 2 (Extended Set)|Extended Set]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Practice Midterm

**Time:** 80 minutes (assumed: one class period). **Total:** 100 points, six problems. **Allowed:** Peskin–Schroeder (printed) and one handwritten sheet, both sides; no electronics, no problem-set solutions (syllabus; Lecture 13).
Built from Larsen's description of the exam (Lecture 13, Oct 14: "much more like homeworks, except homeworks are too long … a few of the questions are literally individual questions that were on the homeworks"; one problem is short-response "of exactly this type" as Problem Set 7, Problem 1; he avoids what the textbook answers literally, "the axial … I guess I have to pick a vector, or maybe the other way around"; he named Problem Set 4, Problem 3(b)). The grey line under each part says where it comes from: *[HW-literal: …]* a homework part as it stood, *[variation of …]* the same computation on an object the book does not work out, *[extension of …]* one step further. Cover the tags if you want an exam feel; a printable copy without tags is `~/Downloads/PHY513_practice_midterm.pdf`. Solutions: [[PHY 513 Practice Midterm Solutions]]; more problems of the same kinds: [[PHY 513 Practice Midterm 2 (Extended Set)]].

**Conventions** (the course's, [[Larsen PHY 513]]): $g = \mathrm{diag}(+1,-1,-1,-1)$, $\varepsilon^{0123} = +1$, natural units. $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ with $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$; $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$. Chiral basis $\gamma^0 = \begin{pmatrix}0&\mathbb 1\\\mathbb 1&0\end{pmatrix}$, $\gamma^i = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$, $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$; $S^{\mu\nu} = \frac i4[\gamma^\mu, \gamma^\nu]$, $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. Discrete symmetries act as $\hat O \to U\hat OU^{-1}$; $\tilde x = (t, -\mathbf x)$, $x_T = (-t, \mathbf x)$, $\mathcal P^\mu{}_\nu = \mathrm{diag}(1,-1,-1,-1)$. Bilinears $\mathsf S = \hat{\bar\psi}\hat\psi$, $\mathsf P = \hat{\bar\psi}\,i\gamma^5\hat\psi$, $\mathsf V^\mu = \hat{\bar\psi}\gamma^\mu\hat\psi$, $\mathsf A^\mu = \hat{\bar\psi}\gamma^\mu\gamma^5\hat\psi$, $\mathsf T^{\mu\nu} = \hat{\bar\psi}\sigma^{\mu\nu}\hat\psi$.

---

## Problem 1 (20 points). Short response

Short answers: a formula, a number, or a phrase. No derivations are needed. 2 points each.

(a) In four spacetime dimensions, give the mass dimensions, as $M^\alpha$, of the couplings $G$ and $\kappa$ in the Lagrangian-density terms $G\,(\bar\psi\psi)^2$ and $\frac{\kappa}{3!}\phi^3$ (each added to the free $\mathcal L$).
*[variation of PS7.1(a)]*

(b) Write the Euler–Lagrange equation for $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2 - \frac{\lambda}{4!}\phi^4$.
*[variation of PS7.1(b)]*

(c) Evaluate $\gamma_\mu\slashed p\slashed q\gamma^\mu$.
*[HW-literal: PS5.2(c)]*

(d) Evaluate $\operatorname{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma^5)$ (course conventions).
*[extension of PS5.5(c)]*

(e) Give the $(j_+, j_-)$ labels of an antisymmetric tensor field $F^{\mu\nu}$ and of a Dirac spinor, and the dimension of $(1, 1)$.
*[variation of PS7.1(d)]*

(f) Give $\varepsilon_{0123}$, $\varepsilon^{2301}$ and $\varepsilon^{0321}$.
*[variation of PS1.3(a)]*

(g) Write the momentum-space advanced propagator $\tilde D_A(p)$ with its $i\varepsilon$, and say on which side of the two poles its $p^0$ contour passes.
*[variation of PS4.4]*

(h) Give the equal-time anticommutator $\{\hat\psi_a(t, \mathbf x), \hat\psi^\dagger_b(t, \mathbf y)\}$.
*[variation of PS3.3(c), Dirac field]*

(i) Which of $\mathsf S$, $\mathsf P$, $\mathsf V^\mu$, $\mathsf A^\mu$, $\mathsf T^{\mu\nu}$ change sign under charge conjugation? What is $\Theta\,\mathsf T^{\mu\nu}(x)\,\Theta^{-1}$, $\Theta = U(\mathcal C)U(\mathcal P)U(\mathcal T)$?
*[variation of PS7.2]*

(j) By what factor is a Dirac spinor multiplied under a rotation by $2\pi$? A four-vector?
*[HW-literal: PS6.4(d)]*

^pm-1

---

## Problem 2 (15 points). The Lorentz group, two representations

(a) (5 points) From the Lorentz algebra $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho})$, compute $[J_1, K_2]$ and $[K_1, K_2]$. Problem Set 5 defined the boost generators with the opposite sign, $K^i = \mathcal J^{i0}$. Does the form of $[J_i, K_j]$ or $[K_i, K_j]$ change? What happens to $\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$?
*[variation of PS5.1(a)]*

^pm-2-a

(b) (6 points) A boost along the 1-axis has $\omega_{01} = -\omega_{10} = \eta$ and all other $\omega_{\mu\nu} = 0$. Write $\Lambda(\eta)$ in the vector representation and $\Lambda_{1/2}(\eta)$ in the spinor representation, both as $4\times4$ matrices (no $2\times2$ blocks). In which direction does the vector $\Lambda(\eta)$ move a particle at rest?
*[variation of PS6.4(a)]*

^pm-2-b

(c) (4 points) Verify $[\gamma^\mu, S^{\rho\sigma}] = (\mathcal J^{\rho\sigma})^\mu{}_\nu\,\gamma^\nu$, using only $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$.
*[HW-literal: PS4.5(b)]*

^pm-2-c

---

## Problem 3 (20 points). The complex scalar field: current, momentum, C and P

Consider $\mathcal L = \partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi - V(\phi^{\ast}\phi)$, with $V$ a smooth function.

(a) (7 points) Find the Noether current of the phase rotation $\phi \to e^{i\alpha}\phi$, $\phi^{\ast} \to e^{-i\alpha}\phi^{\ast}$, and show that it is conserved on solutions for every $V$.
*[HW-literal: PS2.3(d)]*

^pm-3-a

(b) (8 points) Now $V = 0$, quantized with $\hat\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} + \hat b^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x}\bigr)$ at $t = 0$, the conjugate momentum $\hat\pi = \partial_t\hat\phi^\dagger$, $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = [\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and all other commutators of mode operators zero. Show that the field momentum
$$\hat{\mathbf P} = -\int d^3x\,\bigl(\hat\pi\,\nabla\hat\phi + \hat\pi^\dagger\,\nabla\hat\phi^\dagger\bigr) = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr),$$
and explain why no normal ordering is needed.
*[variation of PS6.1]*

^pm-3-b

(c) (5 points) Let $U(\mathcal C)\hat a_{\mathbf p}U(\mathcal C)^{-1} = \hat b_{\mathbf p}$, $U(\mathcal C)\hat b_{\mathbf p}U(\mathcal C)^{-1} = \hat a_{\mathbf p}$ and $U(\mathcal P)\hat a_{\mathbf p}U(\mathcal P)^{-1} = \hat a_{-\mathbf p}$, $U(\mathcal P)\hat b_{\mathbf p}U(\mathcal P)^{-1} = \hat b_{-\mathbf p}$, both unitary. With $\hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$, compute $U(\mathcal C)\hat{\mathbf P}U(\mathcal C)^{-1}$, $U(\mathcal C)\hat QU(\mathcal C)^{-1}$, $U(\mathcal P)\hat{\mathbf P}U(\mathcal P)^{-1}$ and $U(\mathcal P)\hat QU(\mathcal P)^{-1}$.
*[extension of PS7.4(a)]*

^pm-3-c

---

## Problem 4 (20 points). Two-point functions and Green's functions

For a free real scalar of mass $m$: $D_W(x) = \langle0|\hat\phi(x)\hat\phi(0)|0\rangle$, $iD(x) = \langle0|[\hat\phi(x), \hat\phi(0)]|0\rangle$, $D_1(x) = \langle0|\{\hat\phi(x), \hat\phi(0)\}|0\rangle$. At spacelike $x$, $x^2 = -r^2$,
$$D_W(x) = \frac{m}{4\pi^2r}\,K_1(mr).$$
You may use: $K_1(z)$ is real and positive for $z > 0$; $K_1(z) \simeq \sqrt{\pi/2z}\,e^{-z}\bigl(1 + \frac{3}{8z}\bigr)$ for $z \gg 1$; $K_1(z) \simeq 1/z$ for $z \ll 1$.

(a) (8 points) Compute the commutator and Hadamard functions $D$ and $D_1$ from the Wightman function at spacelike $x$. Then determine their behaviour at large distance, including the overall prefactor that is a power of $r$.
*[HW-literal: PS4.3(b)]*

^pm-4-a

(b) (4 points) Show that as $m \to 0$ (or $mr \ll 1$) the result reduces to the massless Wightman function $-1/(4\pi^2x^2)$. For a pion, $m_\pi c^2 = 140$ MeV, restore $\hbar$ and $c$ in the decay length of $D_1$ and give it in fm ($\hbar c = 197.3$ MeV fm).
*[extension of PS4.3(b)]*

^pm-4-b

(c) (8 points) The advanced Green's function is
$$D_A(x) = \int\frac{d^3p}{(2\pi)^3}\,e^{i\mathbf p\cdot\mathbf x}\int_{C_A}\frac{dp^0}{2\pi}\,\frac{i\,e^{-ip^0x^0}}{(p^0)^2 - E_{\mathbf p}^2},$$
with the contour $C_A$ along the real axis, passing below both poles. Do the $p^0$ integral for $x^0 > 0$ and for $x^0 < 0$, and show that $D_A(x) = -\theta(-x^0)\,\langle0|[\hat\phi(x), \hat\phi(0)]|0\rangle$.
*[variation of PS4.4(c); Peskin–Schroeder do the retarded case, eqs. (2.54)–(2.55)]*

^pm-4-c

---

## Problem 5 (15 points). Dirac algebra and spinors

(a) (7 points) Prove $\gamma_\mu\slashed k\slashed p\slashed q\gamma^\mu = -2\slashed q\slashed p\slashed k$ from the anticommutation relations. You may use $\gamma_\mu\gamma^\mu = 4$, $\gamma_\mu\slashed k\gamma^\mu = -2\slashed k$ and $\gamma_\mu\slashed p\slashed q\gamma^\mu = 4\,p\cdot q$.
*[HW-literal: PS5.2(d)]*

^pm-5-a

(b) (8 points) Let $v(p)$, $v(p')$ be negative-frequency spinors, $(\slashed p + m)v(p) = 0$ and $(\slashed p' + m)v(p') = 0$, $m > 0$, and $q = p' - p$. Derive
$$\bar v(p')\gamma^\mu v(p) = -\bar v(p')\Bigl[\frac{(p + p')^\mu}{2m} + \frac{i\sigma^{\mu\nu}q_\nu}{2m}\Bigr]v(p),$$
including the equation obeyed by $\bar v(p')$. Then check the forward limit $p' = p$ against $\bar v^r(p)v^s(p) = -2m\delta^{rs}$ and $v^{r\dagger}(p)v^s(p) = 2E_{\mathbf p}\delta^{rs}$.
*[variation of PS5.3]*

^pm-5-b

---

## Problem 6 (10 points). Discrete symmetries of the bilinears

Use $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$ with $U(\mathcal T)$ antiunitary, and $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i\bigl(\hat{\bar\psi}(x)\gamma^0\gamma^2\bigr)^{\mathsf T}$.

(a) (4 points) Show $U(\mathcal T)\,\mathsf A^\mu(x)\,U(\mathcal T)^{-1} = \mathcal P^\mu{}_\nu\,\mathsf A^\nu(x_T)$. You may use $U(\mathcal T)\hat{\bar\psi}(t, \mathbf x)U(\mathcal T)^{-1} = \hat{\bar\psi}(-t, \mathbf x)\gamma^3\gamma^1$.
*[variation of PS7.2(c): Peskin–Schroeder derive the vector and only say "you can verify" the axial vector]*

^pm-6-a

(b) (4 points) Show $U(\mathcal C)\,\mathsf T^{\mu\nu}(x)\,U(\mathcal C)^{-1} = -\mathsf T^{\mu\nu}(x)$. You may use the rule $U(\mathcal C)\,\hat{\bar\psi}\Gamma\hat\psi\,U(\mathcal C)^{-1} = \hat{\bar\psi}\,\gamma^0\gamma^2\,\Gamma^{\mathsf T}\gamma^0\gamma^2\,\hat\psi$ for a constant matrix $\Gamma$ (normal-ordered bilinears), but derive the transpose identity you need for $\gamma^\mu$.
*[variation of PS7.2(b): Peskin–Schroeder give the tensor only in their table]*

^pm-6-b

(c) (2 points) Given $U(\mathcal P)\mathsf T^{\mu\nu}(x)U(\mathcal P)^{-1} = \mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(\tilde x)$ and $U(\mathcal T)\mathsf T^{\mu\nu}(x)U(\mathcal T)^{-1} = -\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\mathsf T^{\rho\sigma}(x_T)$, find $\Theta\,\mathsf T^{\mu\nu}(x)\,\Theta^{-1}$ for $\Theta = U(\mathcal C)U(\mathcal P)U(\mathcal T)$, and compare with the rule for a bilinear with $n$ Lorentz indices.
*[extension of PS7.3]*

^pm-6-c

---

*Sources:* Problem Sets 4–7 (Larsen, PHY 513, Fall 2026); Lecture 13 (Oct 14) Q&A; Peskin–Schroeder pp. 27, 30, 66–71 for what the book derives. The purpose of each homework problem and how these variations were chosen: `qft-C/review/PURPOSE.md`.
