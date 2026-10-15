---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Canonical Quantization in Modes (Solutions)|Solutions]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Worksheet — Canonical Quantization in Modes

Twenty problems on one technique: quantize a free field canonically and work in modes. Conjugate momenta and equal-time (anti)commutators; the mode expansion and the extraction of the mode operators; the ladder algebra derived in both directions, fields ⇒ oscillators and oscillators ⇒ fields; $\hat H$, $\hat{\mathbf P}$ and $\hat Q$ in modes, with the cancellation of the number-changing terms, the reordering constants and (fermionic) normal ordering; states and their normalization; Heisenberg fields; commutators with the charges and the momentum. The three fields in the order of the lectures and of the notes: the real scalar (Lecture 4; [[§C2a.1 Canonical Quantization of Fields|§C2a.1]]–[[§C2a.4 Particles and Relativistic Normalization|§C2a.4]], [[§C2b.1 Heisenberg Fields|§C2b.1]]), the complex scalar ([[§C2a.5 The Complex Scalar Field and Its Charge|§C2a.5]]), the Dirac field (Lectures 10 and 12; [[§C5b.1 Canonical Quantization of the Dirac Field|§C5b.1]]–[[§C5b.6 The Heisenberg Dirac Field|§C5b.6]], [[§C9.7 Physical Spin versus Wave-Function Spin|§C9.7]]); the last problem is a short-response check in the format of Problem Set 7, Problem 1. The recipe is [[P1 Canonical Quantization]]; the formulas are collected in the [[Scalar Field Card]] and the [[Spinor Field Card]]. The grey line under each part says where it comes from: *[HW-literal …]* a homework part as it stood (in the notation below), *[variation of …]* the same computation on an object the homework or Peskin–Schroeder does not work out, *[extension of …]* one step further, *[new]* not in the homework. Solutions, folded: [[PHY 513 Worksheet — Canonical Quantization in Modes (Solutions)]]. Printable copies: `~/Downloads/PHY513_worksheet_quantization.pdf` (questions, no tags) and `~/Downloads/PHY513_worksheet_quantization_solutions.pdf`.

**Conventions** (the course's, [[Larsen PHY 513]]): $g = \mathrm{diag}(+1,-1,-1,-1)$, $\hbar = c = 1$, $p\cdot x = E_{\mathbf p}t - \mathbf p\cdot\mathbf x$ with $p^0 = E_{\mathbf p} = +\sqrt{\mathbf p^2 + m^2}$ and $m > 0$ (Lectures 4–5 and Problem Set 3 write $\omega_{\mathbf p}$, and $\Pi$ for the momentum density); hats on Hilbert-space operators; $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$; $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$; $\lvert\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}\lvert0\rangle$; $V \equiv (2\pi)^3\delta^3(\mathbf 0)$, the volume of space (in a box of side $L$, $V = L^3$); normal ordering $:\!\cdots\!:$ puts creation operators to the left, with a factor $-1$ for each exchange of two fermion operators; $\hat N_a = \int\frac{d^3p}{(2\pi)^3}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$; the complex scalar's charge is $\hat Q = \frac12(\hat N_a - \hat N_b)$ (Problem Set 3, Peskin–Schroeder). Dirac field: $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, $\bar\psi = \psi^\dagger\gamma^0$, $H_{\text{s.p.}} = -i\boldsymbol\alpha\cdot\nabla + \beta m$ with $\alpha^j = \gamma^0\gamma^j$, $\beta = \gamma^0$; spinors $u^s(p)$, $v^s(p)$ with $u^{r\dagger}(p)u^s(p) = v^{r\dagger}(p)v^s(p) = 2E_{\mathbf p}\delta^{rs}$, $\tilde p \equiv (E_{\mathbf p}, -\mathbf p)$, rest-frame forms $u^s(0) = \sqrt m\,(\xi^s, \xi^s)$, $v^s(0) = \sqrt m\,(\eta^s, -\eta^s)$, and from Lecture 12 on $\eta^s = \xi^{-s}$; $\{A, B\} = AB + BA$.

---

## The real scalar field

### W1. Momentum density, equal-time relations, Heisenberg equations

Take $\mathcal L = \frac12\partial_\mu\phi\,\partial^\mu\phi - \frac12m^2\phi^2$.

^wq-1

(a) Find the momentum density $\pi$, the Hamiltonian density $\mathcal H$ and $H$ in terms of $\phi$ and $\pi$. State the equal-time commutation relations of the quantum field, and explain why their right side is $i\delta^3(\mathbf x - \mathbf y)$ and not a Kronecker delta. What is the mass dimension of $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)]$?
*[variation of PS3.2(a1)]*

^wq-1-a

(b) With $\hat H = \int d^3x\,\bigl[\frac12\hat\pi^2 + \frac12(\nabla\hat\phi)^2 + \frac12m^2\hat\phi^2\bigr]$, compute $[\hat\phi(t, \mathbf x), \hat H]$ and $[\hat\pi(t, \mathbf x), \hat H]$ from the equal-time relations alone, and show that the Heisenberg equations $i\partial_t\hat{\mathcal O} = [\hat{\mathcal O}, \hat H]$ combine into the Klein–Gordon equation.
*[variation of PS3.2(a2)]*

^wq-1-b

(c) The relations are postulated for the Schrödinger operators $\hat\phi_S(\mathbf x)$, $\hat\pi_S(\mathbf x)$. Show that the Heisenberg fields $\hat\phi(t, \mathbf x) = e^{i\hat Ht}\hat\phi_S(\mathbf x)e^{-i\hat Ht}$, $\hat\pi(t, \mathbf x)$ obey them at every common time $t$. What do they say about two different times?
*[new]*

^wq-1-c

### W2. The Klein–Gordon product

For complex solutions $f$, $g$ of the Klein–Gordon equation let $(f, g) \equiv i\int d^3x\,\bigl(f^{\ast}\partial_tg - (\partial_tf^{\ast})\,g\bigr)$, the $d^3x$ integral taken at fixed time, and $f_{\mathbf p}(x) = e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$.

^wq-2

(a) Show that $(f, g)$ is independent of the time at which it is evaluated: take the time derivative and show that it vanishes by the Klein–Gordon equation.
*[HW-literal PS3.3(a)]*

^wq-2-a

(b) Compute $(f_{\mathbf p}, f_{\mathbf q})$, $(f_{\mathbf p}, f^{\ast}_{\mathbf q})$ and $(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q})$. Where is $E_{-\mathbf p} = E_{\mathbf p}$ used?
*[variation of PS3.3(b)]*

^wq-2-b

(c) Is $(f, f) \ge 0$ for every solution? Evaluate it for the positive- and negative-frequency wave packets $f_h = \int\frac{d^3p}{(2\pi)^3}h(\mathbf p)f_{\mathbf p}$ and $f^{\ast}_h$, and say in what sense $(\cdot, \cdot)$ is an inner product.
*[extension of PS3.3(a)]*

^wq-2-c

### W3. Mode extraction

The Heisenberg field is $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$, with $\partial_t\hat\phi = \hat\pi$, and $(\cdot, \cdot)$, $f_{\mathbf p}$ are those of W2.

^wq-3

(a) Show that $\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi)$; this inverts the expansions of $\hat\phi$ and $\hat\pi$ by writing $\hat a$ in terms of $\hat\phi$ and $\dot{\hat\phi} = \hat\pi$.
*[HW-literal PS3.3(b)]*

^wq-3-a

(b) Write (a) out as $\hat a_{\mathbf p} = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\bigl(\hat\pi(x) - iE_{\mathbf p}\hat\phi(x)\bigr)$ and check it by Fourier inversion: compute $\int d^3x\,e^{ip\cdot x}\hat\phi(x)$ and $\int d^3x\,e^{ip\cdot x}\hat\pi(x)$ separately at time $t$. What does each alone give, and what cancels in the combination?
*[extension of PS3.3(b)]*

^wq-3-b

(c) Show that $\hat a^\dagger_{\mathbf p} = -(f^{\ast}_{\mathbf p}, \hat\phi)$. Where does the minus sign come from?
*[variation of PS3.3(b)]*

^wq-3-c

### W4. The ladder algebra in both directions

Same field as W3; at equal times $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, $[\hat\phi, \hat\phi] = [\hat\pi, \hat\pi] = 0$.

^wq-4

(a) Express $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}]$ with W3(b) and its Hermitian conjugate; trade time derivatives for canonical momenta; use the equal-time commutators and simplify. You should recover $(2\pi)^3\delta^3(\mathbf k - \mathbf p)$.
*[HW-literal PS3.3(c)]*

^wq-4-a

(b) Show in the same way that $[\hat a_{\mathbf k}, \hat a_{\mathbf p}] = 0$ and $[\hat a^\dagger_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = 0$. Which property of $E_{\mathbf p}$ is needed?
*[extension of PS3.3(c)]*

^wq-4-b

(c) Conversely, assume $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $[\hat a, \hat a] = [\hat a^\dagger, \hat a^\dagger] = 0$, and the $t = 0$ expansions
$$\hat\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x}, \qquad \hat\pi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}{2}}\bigl(\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\bigr)e^{i\mathbf p\cdot\mathbf x} .$$
Derive them from the expansion of W3 at $t = 0$, then show $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$ and $[\hat\phi(\mathbf x), \hat\phi(\mathbf y)] = [\hat\pi(\mathbf x), \hat\pi(\mathbf y)] = 0$. Which features of $\hat\pi$ make the two surviving terms add?
*[variation of PS3.3(c), the converse direction]*

^wq-4-c

### W5. The Hamiltonian in modes and the zero-point energy

Same field; $\hat H = \int d^3x\,\bigl[\frac12\hat\pi^2 + \frac12(\nabla\hat\phi)^2 + \frac12m^2\hat\phi^2\bigr]$, read as an operator in the order written.

^wq-5

(a) Substitute the $t = 0$ expansions of W4(c) and show $\hat H = \int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\bigr)$. Which terms cancel, and which relation makes them cancel?
*[variation of PS3.2(b)]*

^wq-5-a

(b) Reorder with the commutator: $\hat H = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + E_0$. Give $E_0$ in terms of $V$, explain why $\delta^3(\mathbf 0)$ has no value and what $E_0$ becomes in a periodic box of side $L$ with a momentum cutoff $\Lambda$, and estimate $E_0/V$ for $\Lambda \gg m$.
*[extension of PS3.2(b)]*

^wq-5-b

(c) Show $[\hat H, \hat a^\dagger_{\mathbf p}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p}$ and $[\hat H, \hat a_{\mathbf p}] = -E_{\mathbf p}\hat a_{\mathbf p}$. Why does $E_0$ not enter? With $:\!\hat H\!:$, give the energy of $\hat a^\dagger_{\mathbf p_1}\cdots\hat a^\dagger_{\mathbf p_n}\lvert0\rangle$ and the ground state.
*[extension of PS3.2(b)]*

^wq-5-c

### W6. The momentum in modes

^wq-6

(a) Verify PS eqn 2.33. In other words, show that the momentum operator $\hat{\mathbf P} = -\int d^3x\,:\!\hat\pi(\mathbf x)\nabla\hat\phi(\mathbf x)\!:$ can be written in terms of scalar field ladder operators as $\hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$. The colons mean normal ordering: the introduction of operators through quantization comes with the instruction that $\hat a_{\mathbf p}$ is placed to the right of $\hat a^\dagger_{\mathbf p}$ from the outset; it amounts to the prescription that the (potentially infinite) constant due to reordering of $\hat a_{\mathbf p}$ and $\hat a^\dagger_{\mathbf p}$ must be omitted.
*[HW-literal PS6.1]*

^wq-6-a

(b) Without the colons, $\hat{\mathbf P}$ and $\hat H$ each differ from their normal-ordered forms by a constant. Give both constants in terms of $V$, and say why one of them vanishes and the other does not.
*[extension of PS6.1]*

^wq-6-b

(c) Show $[\hat{\mathbf P}, \hat a^\dagger_{\mathbf p}] = \mathbf p\,\hat a^\dagger_{\mathbf p}$, and give the momentum of $\lvert0\rangle$ and of $\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}\lvert0\rangle$.
*[extension of PS6.1]*

^wq-6-c

### W7. States, normalization and the invariant measure

^wq-7

(a) With $\lvert\mathbf p\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^\dagger_{\mathbf p}\lvert0\rangle$ compute $\langle\mathbf p|\mathbf q\rangle$, and compute $\langle0|\hat a_{\mathbf q_2}\hat a_{\mathbf q_1}\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}|0\rangle$. What do its two terms say about the quanta?
*[new]*

^wq-7-a

(b) With $\delta(f(x)) = \sum_i\frac{1}{\lvert f'(x_i)\rvert}\delta(x - x_i)$ (sum over the zeros of $f$), evaluate the $dk^0$ integral in $\int d^4k\,\delta(k^2 - m^2)\,\theta(k^0)$. Granted that $d^4k$ and $\delta(k^2 - m^2)\theta(k^0)$ are invariant under proper orthochronous Lorentz transformations, argue that $\int\frac{d^3k}{(2\pi)^3\,2E_{\mathbf k}}$ is Lorentz invariant.
*[HW-literal PS3.1(d)–(e)]*

^wq-7-b

(c) Show that $2E_{\mathbf p}\,\delta^3(\mathbf p - \mathbf q)$ is Lorentz invariant, so that $\langle\mathbf p|\mathbf q\rangle$ is. How does $\delta^3(\mathbf p - \mathbf q)$ alone transform, and what does that say about the normalization of $\hat a^\dagger_{\mathbf p}\lvert0\rangle$?
*[variation of PS3.1(e)]*

^wq-7-c

(d) Show that at $t = 0$, $\hat\phi(\mathbf x)\lvert0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-i\mathbf p\cdot\mathbf x}\lvert\mathbf p\rangle$, and that the Heisenberg field of W3 has $\langle0|\hat\phi(x)|\mathbf p\rangle = e^{-ip\cdot x}$.
*[new]*

^wq-7-d

### W8. The Heisenberg field and translations

Take $\hat H = \int\frac{d^3q}{(2\pi)^3}E_{\mathbf q}\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q} + E_0$ and the Schrödinger field $\hat\phi_S(\mathbf x) = \hat\phi(t = 0, \mathbf x)$ of W4(c).

^wq-8

(a) Show $e^{i\hat Ht}\hat a_{\mathbf p}e^{-i\hat Ht} = \hat a_{\mathbf p}e^{-iE_{\mathbf p}t}$ and $e^{i\hat Ht}\hat a^\dagger_{\mathbf p}e^{-i\hat Ht} = \hat a^\dagger_{\mathbf p}e^{iE_{\mathbf p}t}$.
*[extension of PS3.3 (its Heisenberg field)]*

^wq-8-a

(b) Conclude that $e^{i\hat Ht}\hat\phi_S(\mathbf x)e^{-i\hat Ht}$ is the covariant expansion of W3, and that $\hat\pi = \partial_t\hat\phi$.
*[extension of PS3.3 (its Heisenberg field)]*

^wq-8-b

(c) From the field form $\hat{\mathbf P} = -\int d^3y\,\hat\pi(\mathbf y)\nabla\hat\phi(\mathbf y)$ and the equal-time relations, show $[\hat\phi(\mathbf x), \hat{\mathbf P}] = -i\nabla\hat\phi(\mathbf x)$; check it with the mode form of W6. Conclude that $e^{i\mathbf a\cdot\hat{\mathbf P}}\hat\phi(\mathbf x)e^{-i\mathbf a\cdot\hat{\mathbf P}} = \hat\phi(\mathbf x - \mathbf a)$ to first order in $\mathbf a$.
*[new]*

^wq-8-c

## The complex scalar field

### W9. Quantizing the complex scalar: two species

A complex scalar field with $S = \int d^4x\,\bigl(\partial_\mu\phi^{\ast}\partial^\mu\phi - m^2\phi^{\ast}\phi\bigr)$, so that $\phi$ and $\phi^{\ast}$ each obey the Klein–Gordon equation; treat $\phi$ and $\phi^{\ast}$ as independent fields. After quantization $\phi^{\ast}$ becomes $\hat\phi^\dagger$.

^wq-9

(a) Find the momenta $\pi$ and $\pi^{\ast}$ conjugate to $\phi$ and $\phi^{\ast}$ and write down the canonical commutation relations. Show that $H = \int d^3x\,\bigl(\pi^{\ast}\pi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi\bigr)$. (Careful: with this Lagrangian $\pi = \partial\mathcal L/\partial\dot\phi$ is $\dot\phi^{\ast}$, not $\dot\phi$.)
*[HW-literal PS3.2(a1)]*

^wq-9-a

(b) Diagonalize $H$ by introducing creation and annihilation operators. Show that the theory contains two independent sets of particles, both of mass $m$. The conventional expansion is $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$. Composite operators are defined by normal ordering: $\hat a_{\mathbf p}$ is placed to the right of $\hat a^\dagger_{\mathbf p}$ (and $\hat b_{\mathbf p}$ of $\hat b^\dagger_{\mathbf p}$) from the outset; operators in the "wrong" order are first reordered without taking the commutator into account and only then promoted to noncommuting operators.
*[HW-literal PS3.2(b)]*

^wq-9-b

(c) With the product of W2, show $\hat a_{\mathbf p} = (f_{\mathbf p}, \hat\phi)$, $\hat b_{\mathbf p} = (f_{\mathbf p}, \hat\phi^\dagger)$, $\hat b^\dagger_{\mathbf p} = -(f^{\ast}_{\mathbf p}, \hat\phi)$. From which fields and momenta is each of $\hat a$, $\hat b$ built? Use this to show $[\hat a_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = 0$ at once and $[\hat a_{\mathbf p}, \hat b_{\mathbf q}] = 0$ with one computation.
*[variation of PS3.3(b)]*

^wq-9-c

### W10. The charge of the complex field

^wq-10

(a) The action is invariant under $\phi \to e^{i\alpha}\phi$, $\phi^{\ast} \to e^{-i\alpha}\phi^{\ast}$; the conserved charge, in Peskin–Schroeder's normalization, is $\hat Q = \int d^3x\,\frac i2\bigl(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi\bigr)$ (normal ordered). Rewrite $\hat Q$ in terms of creation and annihilation operators and determine the charge of the particles of each type.
*[HW-literal PS3.2(c)]*

^wq-10-a

(b) Compute $[\hat Q, \hat a^\dagger_{\mathbf p}]$ and $[\hat Q, \hat b^\dagger_{\mathbf p}]$, and the charges of $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}\lvert0\rangle$ and $(\hat a^\dagger_{\mathbf p})^2\lvert0\rangle$.
*[extension of PS3.2(c)]*

^wq-10-b

(c) Show $[\hat Q, \hat\phi(x)] = -\frac12\hat\phi(x)$ and $[\hat Q, \hat\phi^\dagger(x)] = +\frac12\hat\phi^\dagger(x)$, and conclude that $e^{i\theta\hat Q}\hat\phi\,e^{-i\theta\hat Q} = e^{-i\theta/2}\hat\phi$.
*[new]*

^wq-10-c

(d) The Noether current of Problem Set 2, Problem 3(d) is $j^\mu = i\bigl(\phi\,\partial^\mu\phi^{\ast} - \phi^{\ast}\partial^\mu\phi\bigr)$. Express $\int d^3x\,:\!\hat j^0\!:$ through $\hat N_a$, $\hat N_b$ and relate it to $\hat Q$. Which features of the two charges are conventions, and which is physical?
*[variation of PS3.2(c)]*

^wq-10-d

(e) What would $\hat Q$ be without normal ordering? Why is the ordering of $\hat Q$ forced, while that of $\hat H$ is a convenience?
*[extension of PS3.2(c)]*

^wq-10-e

### W11. Momentum and energy of the complex field

^wq-11

(a) Show that the field momentum $\hat{\mathbf P} = -\int d^3x\,\bigl(\hat\pi\,\nabla\hat\phi + \hat\pi^\dagger\,\nabla\hat\phi^\dagger\bigr)$ is $\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr)$. Which terms drop, and why is no normal ordering needed?
*[variation of PS6.1]*

^wq-11-a

(b) $\hat b^\dagger_{\mathbf p}$ multiplies $e^{+ip\cdot x}$, whose spatial factor is $e^{-i\mathbf p\cdot\mathbf x}$. Which momentum does $\hat b^\dagger_{\mathbf p}\lvert0\rangle$ carry, and where in the derivation is this decided?
*[extension of PS6.1]*

^wq-11-b

(c) Reordering the $\hat H$ of W9(b) with the commutators instead of normal ordering it from the outset gives a constant. Express it through the real field's $E_0$ (W5), and explain why setting $\hat b = \hat a$ in the complex field's $\hat H$ does not give the real field's $\hat H$.
*[extension of PS3.2(b)]*

^wq-11-c

## The Dirac field

### W12. The Dirac field as a canonical system

Take $\mathcal L = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ with $\psi$ and $\bar\psi$ independent.

^wq-12

(a) Find the canonical momenta $\pi_\psi = \partial\mathcal L/\partial\dot\psi$ and $\pi_{\bar\psi}$. How does $\pi_\psi$ differ from the scalar's $\pi = \dot\phi$, and what are the canonical pairs?
*[variation of PS3.2(a1)]*

^wq-12-a

(b) Show that the momentum form of the canonical anticommutators, $\{\hat\psi_a(\mathbf x), \hat\pi_{\psi,b}(\mathbf y)\} = i\delta_{ab}\delta^3(\mathbf x - \mathbf y)$, $\{\hat\pi_{\psi,a}, \hat\pi_{\psi,b}\} = 0$, is equivalent to $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, $\{\hat\psi^\dagger_a, \hat\psi^\dagger_b\} = 0$, and derive $\{\hat\psi_a(\mathbf x), \hat{\bar\psi}_b(\mathbf y)\}$ at equal times.
*[new]*

^wq-12-b

(c) Show that $\mathcal H = \pi_\psi\dot\psi - \mathcal L = \psi^\dagger H_{\text{s.p.}}\psi$ for every configuration, and $= i\psi^\dagger\partial_t\psi$ on solutions. Give the field momentum $\mathbf P$ (the Noether charge of space translations) in field form, and say how it differs from the canonical momentum.
*[variation of PS5.4(b)]*

^wq-12-c

### W13. Mode expansion and mode extraction

$\hat\psi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_{s=1,2}\bigl(\hat a^s_{\mathbf p}u^s(p)e^{-ip\cdot x} + \hat b^{s\dagger}_{\mathbf p}v^s(p)e^{ip\cdot x}\bigr)$.

^wq-13

(a) Write $\hat\psi^\dagger$ and $\hat{\bar\psi}$ in modes. Which of $\hat a$, $\hat a^\dagger$, $\hat b$, $\hat b^\dagger$ does each of $\hat\psi$, $\hat\psi^\dagger$, $\hat{\bar\psi}$ contain, and what does each field do to the particle content?
*[new]*

^wq-13-a

(b) Show that at any time $t$
$$\hat a^s_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\,u^{s\dagger}(p)\,\hat\psi(x), \qquad \hat b^{s\dagger}_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{-ip\cdot x}\,v^{s\dagger}(p)\,\hat\psi(x) .$$
Which spinor identities do you need, and at which momenta?
*[variation of PS3.3(b), Dirac field]*

^wq-13-b

(c) Compare with the scalar's extraction (W3): which conserved product of solutions is used here, is it positive, and why do both coefficients now come out with a plus sign?
*[extension of PS3.3(b)]*

^wq-13-c

### W14. The anticommutator algebra in both directions

^wq-14

(a) From the equal-time relations $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, $\{\hat\psi, \hat\psi\} = \{\hat\psi^\dagger, \hat\psi^\dagger\} = 0$, derive $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$.
*[variation of PS3.3(c), Dirac field]*

^wq-14-a

(b) Show $\{\hat a^r_{\mathbf p}, \hat b^s_{\mathbf q}\} = 0$ and $\{\hat a^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = 0$.
*[variation of PS3.3(c), Dirac field]*

^wq-14-b

(c) Conversely, from the oscillator anticommutators derive $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ at $t = 0$, using $\sum_su^s(p)\bar u^s(p) = \slashed{p} + m$ and $\sum_sv^s(p)\bar v^s(p) = \slashed{p} - m$. Why are both frequencies needed?
*[variation of PS3.3(c), the converse direction]*

^wq-14-c

(d) Suppose instead $[\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)] = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ with commutators. Redo (a): what are $[\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}]$ and $[\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}]$, and where does the difference come from?
*[new]*

^wq-14-d

### W15. The energy in modes, and why anticommutators

$\hat H = \int d^3x\,\hat\psi^\dagger H_{\text{s.p.}}\hat\psi$.

^wq-15

(a) Substitute the expansions of $\hat\psi$ and $\hat\psi^\dagger$ without using any (anti)commutation relation, and show $\hat H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\bigr)$. Which spinor identities remove the number-changing terms?
*[variation of PS6.2]*

^wq-15-a

(b) For a classical Dirac field (c-number amplitudes $a^s_{\mathbf p}$, $b^s_{\mathbf p}$), write $H$ and $Q = \int d^3x\,\psi^\dagger\psi$ in modes. Show that $H$ is unbounded below and $Q \ge 0$, and compare with the complex scalar.
*[extension of PS6.2]*

^wq-15-b

(c) Quantize with the commutators of W14(d). Show: if $\hat b^s_{\mathbf p}\lvert0\rangle = 0$, then $\hat b^{s\dagger}(g)\lvert0\rangle = \int\frac{d^3p}{(2\pi)^3}g(\mathbf p)\hat b^{s\dagger}_{\mathbf p}\lvert0\rangle$ has negative squared norm; if instead $\hat d^s_{\mathbf p} \equiv \hat b^{s\dagger}_{\mathbf p}$ annihilates the vacuum, the energy is unbounded below.
*[new]*

^wq-15-c

(d) State the spin–statistics theorem as the course states it, and say what the free Dirac and scalar fields check of it.
*[new]*

^wq-15-d

### W16. The Dirac Hamiltonian: fermionic reordering and the zero-point energy

^wq-16

(a) With the anticommutators of W14(a), reorder the $\hat H$ of W15(a): show $\hat H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr) + E_0^{(\rm D)}$, find $E_0^{(\rm D)}$ in terms of the real scalar's $E_0$ of the same mass, and show that $:\!\hat H\!: \ge 0$ with $:\!\hat H\!:\lvert0\rangle = 0$.
*[extension of PS6.2]*

^wq-16-a

(b) In a box, with $\{\hat c, \hat c^\dagger\} = 1$ for each mode, write each of the four modes per momentum as a fermionic oscillator and find its ground-state energy. Compare with the bosonic oscillator $\omega(\hat a^\dagger\hat a + \frac12)$.
*[new]*

^wq-16-b

(c) Using $[AB, C] = A\{B, C\} - \{A, C\}B$, show $[\hat H, \hat b^{s\dagger}_{\mathbf p}] = E_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$ and $[\hat H, \hat a^s_{\mathbf p}] = -E_{\mathbf p}\hat a^s_{\mathbf p}$, and conclude $e^{i\hat Ht}\hat a^s_{\mathbf p}e^{-i\hat Ht} = \hat a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$, $e^{i\hat Ht}\hat b^{s\dagger}_{\mathbf p}e^{-i\hat Ht} = \hat b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$. Does it matter whether $\hat H$ or $:\!\hat H\!:$ is used?
*[new]*

^wq-16-c

### W17. Momentum and charge in modes

^wq-17

(a) Verify PS eqn 3.113, i.e. show that the charge operator $\hat Q = \int d^3x\,:\!\hat\psi^\dagger(x)\hat\psi(x)\!:$ can be written in terms of fermionic ladder operators as $\hat Q = \int\frac{d^3p}{(2\pi)^3}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr)$.
*[HW-literal PS6.2]*

^wq-17-a

(b) Show that the field momentum $\hat{\mathbf P} = \int d^3x\,:\!\hat\psi^\dagger(-i\nabla)\hat\psi\!:$ is $\sum_s\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr)$.
*[variation of PS6.1, Dirac field]*

^wq-17-b

(c) Without the colons, what constants appear in $\hat Q$ and in $\hat{\mathbf P}$? Compare the sign of the vacuum charge with the complex scalar's (W10(e)).
*[extension of PS6.2]*

^wq-17-c

### W18. Charges of states and fields; translations

$\hat Q$ and $\hat{\mathbf P}$ are those of W17, with the anticommutators of W14(a).

^wq-18

(a) Compute $[\hat Q, \hat a^{s\dagger}_{\mathbf p}]$ and $[\hat Q, \hat b^{s\dagger}_{\mathbf p}]$ (commutators, although the modes anticommute), and the charges of $\lvert\mathbf p, s\rangle = \sqrt{2E_{\mathbf p}}\hat a^{s\dagger}_{\mathbf p}\lvert0\rangle$, $\lvert\mathbf p, s\rangle^c = \sqrt{2E_{\mathbf p}}\hat b^{s\dagger}_{\mathbf p}\lvert0\rangle$ and $\hat a^{r\dagger}_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\lvert0\rangle$.
*[extension of PS6.2]*

^wq-18-a

(b) Show $[\hat Q, \hat\psi(x)] = -\hat\psi(x)$ and $[\hat Q, \hat{\bar\psi}(x)] = +\hat{\bar\psi}(x)$, and conclude $e^{i\alpha\hat Q}\hat\psi\,e^{-i\alpha\hat Q} = e^{-i\alpha}\hat\psi$. Which two processes does $\hat\psi$ describe, and what do they have in common?
*[extension of PS6.2]*

^wq-18-b

(c) The Noether current of $\psi \to e^{i\alpha}\psi$ in the course's recipe ($\Delta\psi = i\psi$, $\Delta\bar\psi = -i\bar\psi$) is $j^\mu_{\rm N} = -\bar\psi\gamma^\mu\psi$. Relate $\int d^3x\,:\!\hat j^0_{\rm N}\!:$ to $\hat Q$, and compare with the complex scalar (W10(d)).
*[variation of PS6.5(d)]*

^wq-18-c

(d) With $\hat{\mathbf P} = \int d^3y\,\hat\psi^\dagger(-i\nabla)\hat\psi$ and the equal-time anticommutators, show $[\hat\psi_a(\mathbf x), \hat{\mathbf P}] = -i\nabla\hat\psi_a(\mathbf x)$, using $[A, BC] = \{A, B\}C - B\{A, C\}$.
*[new]*

^wq-18-d

### W19. The physical spin of the antiparticle

$\hat{\mathbf J} = \int d^3x\,:\!\hat\psi^\dagger\bigl(\mathbf x\times(-i\nabla) + \frac12\boldsymbol\Sigma\bigr)\hat\psi\!:$ with $\boldsymbol\Sigma = \mathrm{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$, so that $\hat J_z\lvert0\rangle = 0$.

^wq-19

(a) Show $\hat J_z\,\hat a^{s\dagger}_{\mathbf 0}\lvert0\rangle = \sum_r\bigl(\xi^{r\dagger}\frac{\sigma^3}{2}\xi^s\bigr)\hat a^{r\dagger}_{\mathbf 0}\lvert0\rangle$.
*[new]*

^wq-19-a

(b) Show $\hat J_z\,\hat b^{s\dagger}_{\mathbf 0}\lvert0\rangle = -\sum_r\bigl(\eta^{s\dagger}\frac{\sigma^3}{2}\eta^r\bigr)\hat b^{r\dagger}_{\mathbf 0}\lvert0\rangle$. Where does the minus sign come from?
*[new]*

^wq-19-b

(c) With $\xi^1 = (1, 0)^{\mathsf T}$, $\xi^2 = (0, 1)^{\mathsf T}$: which $J_z$ do $\hat a^{s\dagger}_{\mathbf 0}\lvert0\rangle$ and $\hat b^{s\dagger}_{\mathbf 0}\lvert0\rangle$ have if $\eta^s = \xi^s$, and if $\eta^s = \xi^{-s}$ as in the course from Lecture 12 on?
*[new]*

^wq-19-c

## All fields

### W20. Short response: quantization in modes

Short answers: a formula, a number, or a phrase. No derivations are needed.
*[variation of PS7.1]*

^wq-20

(a) $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = ?$, $\lvert\mathbf p\rangle = ?\,\hat a^\dagger_{\mathbf p}\lvert0\rangle$ and $\langle\mathbf p|\mathbf q\rangle = ?$ in the course's normalization; the invariant measure that goes with it.

^wq-20-a

(b) The momentum conjugate to $\phi$ for the real scalar, for the complex scalar, and to $\psi$ for the Dirac field.

^wq-20-b

(c) $:\!\hat a_{\mathbf p}\hat a^\dagger_{\mathbf q}\!: = ?$ and $:\!\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\!: = ?$ for the Dirac field.

^wq-20-c

(d) The zero-point energies of the real scalar, the complex scalar and the Dirac field of the same mass, in terms of $V$ and $E_{\mathbf p}$.

^wq-20-d

(e) The charge $\hat Q$ in terms of number operators, and the charge of $\hat b^\dagger_{\mathbf p}\lvert0\rangle$, for the complex scalar and for the Dirac field.

^wq-20-e

(f) $[\hat\phi(\mathbf x), \hat{\mathbf P}] = ?$; $[\hat Q, \hat\psi] = ?$; $e^{i\hat Ht}\hat b^{s\dagger}_{\mathbf p}e^{-i\hat Ht} = ?$

^wq-20-f

(g) The momentum of $\hat b^{s\dagger}_{\mathbf p}\lvert0\rangle$, and the spinor and exponential that multiply $\hat b^{s\dagger}_{\mathbf p}$ in $\hat\psi$.

^wq-20-g

(h) $\{\hat\psi_a(\mathbf x), \hat{\bar\psi}_b(\mathbf y)\}$ at equal times, and $u^{r\dagger}(p)v^s(\tilde p)$.

^wq-20-h

(i) Which terms of $\hat H$ and $\hat{\mathbf P}$ of the real scalar change the number of quanta, and what removes them in each case?

^wq-20-i
