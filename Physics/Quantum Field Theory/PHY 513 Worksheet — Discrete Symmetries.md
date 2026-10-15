---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Discrete Symmetries (Solutions)|Solutions]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Worksheet — Discrete Symmetries

Eighteen problems on parity, charge conjugation, time reversal and CPT for the midterm (Fri Oct 16): on points and momenta, on oscillators and states, on the fields and on their bilinears, for the real scalar, the complex scalar and the Dirac field, and (★) for the electromagnetic field tensor. The order is that of Lectures 11–12 and of [[§C9.1 Discrete Lorentz Transformations|§C9.1]]–[[§C9.10 C, T and CPT for the Complex Scalar Field|§C9.10]]; the last problem is a short-response round in the format of Problem Set 7, Problem 1. Peskin–Schroeder (PS) pp. 64–71 derive $P$ on all bilinears, $T$ on $\mathsf S$, $\mathsf P$, $\mathsf V^\mu$ and $C$ on $\mathsf S$, $\mathsf P$, and only state the rest; the problems below aim at what PS leave out ($T$ on $\mathsf A^\mu$, $C$ on $\mathsf V^\mu$, $\mathsf A^\mu$ in steps, the tensor under $C$, $P$, $T$, the scalar fields of PS Problem 3.7). The grey line under each part says where it comes from: *[HW-literal …]* a homework part as it stood, *[variation of …]* the same computation on an object the homework or PS does not work out, *[extension of …]* one step further, *[new]* built from the lectures. ★ marks material beyond the lectures. Solutions, folded: [[PHY 513 Worksheet — Discrete Symmetries (Solutions)]]. Printable copies: `~/Downloads/PHY513_worksheet_discrete.pdf` (questions, no tags) and `~/Downloads/PHY513_worksheet_discrete_solutions.pdf`.

**Conventions** (the course's, [[Larsen PHY 513]]): $g = \mathrm{diag}(+1,-1,-1,-1)$, $\hbar = c = 1$, $\varepsilon^{0123} = +1$; hats on Hilbert-space operators. Discrete Lorentz matrices $\mathcal P^\mu{}_\nu = \mathrm{diag}(1,-1,-1,-1)$, $\mathcal T^\mu{}_\nu = \mathrm{diag}(-1,1,1,1)$; images $\tilde x = (t, -\mathbf x)$, $\tilde p = (p^0, -\mathbf p)$, $x_T = (-t, \mathbf x) = -\tilde x$. Operators are conjugated as $U\hat{\mathcal O}U^{-1}$ (Problem Set 6 writes $\mathcal P\hat{\mathcal O}\mathcal P^\dagger$ for $U(\mathcal P)\hat{\mathcal O}U(\mathcal P)^{-1}$). Chiral basis $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, $\gamma^i = \begin{pmatrix}0 & \sigma^i\\ -\sigma^i & 0\end{pmatrix}$, $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \mathrm{diag}(-\mathbb 1, \mathbb 1)$, $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. Dirac field $\hat\psi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(\hat a^s_{\mathbf p}u^s(p)e^{-ip\cdot x} + \hat b^{s\dagger}_{\mathbf p}v^s(p)e^{ip\cdot x}\bigr)$, $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, $u^s(p) = (\sqrt{p\cdot\sigma}\,\xi^s, \sqrt{p\cdot\bar\sigma}\,\xi^s)$, $v^s(p) = (\sqrt{p\cdot\sigma}\,\eta^s, -\sqrt{p\cdot\bar\sigma}\,\eta^s)$ with $\eta^s = \xi^{-s} \equiv -i\sigma^2(\xi^s)^{\ast}$; for any family labelled by $s$, $X^{-1} \equiv X^2$, $X^{-2} \equiv -X^1$. Transposed adjoint $\hat\psi^{\dagger\mathsf T}$, the column with entries $(\hat\psi^{\dagger\mathsf T})_a = (\hat\psi_a)^\dagger$ (PS and Problem Set 7 write $\psi^{\ast}$). The course's laws: $U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$; $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i\gamma^2\hat\psi^{\dagger\mathsf T}(x) = -i\bigl(\hat{\bar\psi}(x)\gamma^0\gamma^2\bigr)^{\mathsf T}$; $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$ with $U(\mathcal T)$ antiunitary, $U(\mathcal T)\,c\,U(\mathcal T)^{-1} = c^{\ast}$ for every number, Dirac-matrix entries included; $\Theta \equiv U(\mathcal C)U(\mathcal P)U(\mathcal T)$ (first $\mathcal T$, then $\mathcal P$, then $\mathcal C$). Bilinears, normal-ordered: $\mathsf S = \hat{\bar\psi}\hat\psi$, $\mathsf P = \hat{\bar\psi}\,i\gamma^5\hat\psi$, $\mathsf V^\mu = \hat{\bar\psi}\gamma^\mu\hat\psi$, $\mathsf A^\mu = \hat{\bar\psi}\gamma^\mu\gamma^5\hat\psi$, $\mathsf T^{\mu\nu} = \hat{\bar\psi}\sigma^{\mu\nu}\hat\psi$. Complex scalar $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$, $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = [\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, normal-ordered current $\hat j^\mu = i(\hat\phi\,\partial^\mu\hat\phi^\dagger - \hat\phi^\dagger\partial^\mu\hat\phi)$, charge $\hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$; Problem Set 7's $\phi^{\ast}$ is the operator $\hat\phi^\dagger$.

---

## The discrete Lorentz transformations

### W1. Points, momenta and derivatives

The matrices $\mathcal P$ and $\mathcal T$ act on four-vectors; $\tilde x = \mathcal Px$, $x_T = \mathcal Tx$.

^wd-1

(a) Give $\det\Lambda$ and $\Lambda^0{}_0$ for $\mathcal P$, $\mathcal T$ and $\mathcal P\mathcal T$. Lecture 11, slide 7, states that $\mathcal T$ and $\mathcal P$ have $\det\Lambda = 1$: correct it. Why can no product of boosts and rotations equal $\mathcal T$, and why is $\mathcal P\mathcal T$ not in $SO^+(1,3)$ although its determinant is $+1$?
*[new]*

^wd-1-a

(b) Show $\tilde p\cdot x = p\cdot\tilde x = p^0t + \mathbf p\cdot\mathbf x$ and $p\cdot x_T = -\tilde p\cdot x$. For a function $f$ on spacetime show $\partial_\mu[f(\tilde x)] = \mathcal P^\nu{}_\mu(\partial_\nu f)(\tilde x)$ and $\partial_\mu[f(x_T)] = -\mathcal P^\nu{}_\mu(\partial_\nu f)(x_T)$.
*[new]*

^wd-1-b

(c) For an on-shell momentum $p = (E_{\mathbf p}, \mathbf p)$, $E_{\mathbf p} > 0$, which of $\mathcal Pp$ and $\mathcal Tp$ lies on the upper mass shell? A movie of a particle run backwards shows a particle of positive energy: which momentum label must the time-reversed one-particle state carry, and which matrix acting on $p$ gives it?
*[new]*

^wd-1-c

## Parity

### W2. Parity on the real scalar field: scalar and pseudoscalar

Take the real field $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr)$ and a unitary $U(\mathcal P)$ with $U(\mathcal P)\hat a_{\mathbf p}U(\mathcal P)^{-1} = \eta\,\hat a_{-\mathbf p}$, $|\eta| = 1$, $U(\mathcal P)|0\rangle = |0\rangle$.

^wd-2

(a) Show that $U(\mathcal P)\hat\phi(x)U(\mathcal P)^{-1} = \eta\,\hat\phi(\tilde x)$ holds if and only if $\eta = \pm1$. Give $U(\mathcal P)|\mathbf p\rangle$ and $U(\mathcal P)^2$.
*[variation of PS7.4(a): the real field]*

^wd-2-a

(b) Find the images of $\hat\pi = \partial_t\hat\phi$ and of $\nabla\hat\phi$, and show that the free Lagrangian $\frac12\partial_\mu\hat\phi\,\partial^\mu\hat\phi - \frac12m^2\hat\phi^2$ goes to itself at $\tilde x$ for both signs of $\eta$.
*[new]*

^wd-2-b

(c) Couple $\hat\phi$ to a Dirac field through $g\,\hat\phi\,\mathsf S$ or $g'\,\hat\phi\,\mathsf P$ ($g, g'$ real), with $U(\mathcal P)\mathsf S(x)U(\mathcal P)^{-1} = \mathsf S(\tilde x)$, $U(\mathcal P)\mathsf P(x)U(\mathcal P)^{-1} = -\mathsf P(\tilde x)$, and $\hat\phi$, $\hat\psi$ acting on different factors of the Hilbert space. For which $\eta$ is each coupling parity invariant? What if both are present?
*[new]*

^wd-2-c

### W3. Parity on the complex scalar field

Let $U(\mathcal P)\hat a_{\mathbf p}U(\mathcal P)^{-1} = \eta_a\hat a_{-\mathbf p}$, $U(\mathcal P)\hat b_{\mathbf p}U(\mathcal P)^{-1} = \eta_b\hat b_{-\mathbf p}$, $|\eta_a| = |\eta_b| = 1$, $U(\mathcal P)$ unitary, $U(\mathcal P)|0\rangle = |0\rangle$.

^wd-3

(a) Show that $U(\mathcal P)\hat\phi(x)U(\mathcal P)^{-1} = \eta_a\hat\phi(\tilde x)$ if and only if $\eta_b = \eta_a^{\ast}$, i.e. $\eta_a\eta_b = +1$.
*[variation of PS7.4(a): parity with general phases]*

^wd-3-a

(b) Find $U(\mathcal P)\hat\phi^\dagger(x)U(\mathcal P)^{-1}$ and the image of the current $\hat j^\mu$. Does it depend on $\eta_a$?
*[variation of PS7.4(b): parity with a phase]*

^wd-3-b

(c) Give the intrinsic parities of the particle and of the antiparticle, and the parity eigenvalue of the pair state $\int d^3p\,\Phi_{LM}(\mathbf p)\,\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}|0\rangle$ with $\Phi_{LM}(-\mathbf p) = (-1)^L\Phi_{LM}(\mathbf p)$.
*[new]*

^wd-3-c

(d) Show that $U(\mathcal P)' = e^{-i\theta\hat Q}U(\mathcal P)$ ($\theta$ real) is again a parity operator, and find its phases $\eta_a'$, $\eta_b'$. Which part of the parity phases is a convention, and which is physical?
*[new]*

^wd-3-d

### W4. Dirac parity from the modes

Let $U(\mathcal P)\hat a^s_{\mathbf p}U(\mathcal P)^{-1} = \eta_a\hat a^s_{-\mathbf p}$, $U(\mathcal P)\hat b^s_{\mathbf p}U(\mathcal P)^{-1} = \eta_b\hat b^s_{-\mathbf p}$ (spin labels unchanged), $U(\mathcal P)$ unitary, vacuum invariant.

^wd-4

(a) Show $p\cdot\sigma = \tilde p\cdot\bar\sigma$ and hence $u^s(\tilde p) = \gamma^0u^s(p)$ and $v^s(\tilde p) = -\gamma^0v^s(p)$.
*[new]*

^wd-4-a

(b) Derive $U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$ from the mode expansion, and show that it holds if and only if $\eta_b^{\ast} = -\eta_a$, i.e. $\eta_a\eta_b = -1$.
*[variation of PS7.4(a): the Dirac field]*

^wd-4-b

(c) Derive $U(\mathcal P)\hat{\bar\psi}(x)U(\mathcal P)^{-1}$. Give the intrinsic parities of fermion and antifermion and the parity of a fermion–antifermion pair with orbital angular momentum $L$. What does this say about the ground state of positronium, compared with a scalar particle–antiparticle pair (W3(c))?
*[new]*

^wd-4-c

### W5. Bilinears under parity

Use $U(\mathcal P)\hat\psi(x)U(\mathcal P)^{-1} = \eta_a\gamma^0\hat\psi(\tilde x)$ and the result of W4(c) for $\hat{\bar\psi}$.

^wd-5

(a) Verify the parity transformation properties of the pseudo-vector $\mathsf A^\mu = \hat{\bar\psi}\gamma^\mu\gamma^5\hat\psi$ and the tensor $\mathsf T^{\mu\nu} = \hat{\bar\psi}\sigma^{\mu\nu}\hat\psi$.
*[HW-literal PS7.2(a)]*

^wd-5-a

(b) Now the vector and the pseudoscalar, with a complex phase $\eta_a$, in the course's order $U\cdots U^{-1}$: find the images of $\mathsf V^\mu$ and $\mathsf P$. Where does $\eta_a^{\ast}$ come from, and would Peskin–Schroeder's $P\cdots P$ change any sign?
*[variation of PS7.2(a)]*

^wd-5-b

(c) ★ With $\hat\psi_{L,R} = P_{L,R}\hat\psi$, $P_{L,R} = \frac12(\mathbb 1 \mp \gamma^5)$, find the images of $\hat\psi_L$ and of the left-handed current $\overline{\hat\psi_L}\gamma^\mu\hat\psi_L$. Why does a theory that couples a gauge field to $\overline{\hat\psi_L}\gamma^\mu\hat\psi_L$ only violate parity?
*[extension of PS7.2(a)]*

^wd-5-c

## Charge conjugation

### W6. Charge conjugation on oscillators and spinors

$U(\mathcal C)$ is unitary with $U(\mathcal C)\hat a^s_{\mathbf p}U(\mathcal C)^{-1} = \hat b^s_{\mathbf p}$, $U(\mathcal C)\hat b^s_{\mathbf p}U(\mathcal C)^{-1} = \hat a^s_{\mathbf p}$, $U(\mathcal C)|0\rangle = |0\rangle$.

^wd-6

(a) Find the images of $\hat a^{s\dagger}_{\mathbf p}$, $\hat b^{s\dagger}_{\mathbf p}$, of the one-particle states, and of the Dirac charge $\hat Q = \int\frac{d^3p}{(2\pi)^3}\sum_s(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p})$.
*[new]*

^wd-6-a

(b) Let $J\xi = -i\sigma^2\xi^{\ast}$ on two-spinors. Show that $J$ is antilinear, that $(\hat{\mathbf n}\cdot\boldsymbol\sigma)\xi = \lambda\xi$ implies $(\hat{\mathbf n}\cdot\boldsymbol\sigma)J\xi = -\lambda J\xi$ for every real unit vector $\hat{\mathbf n}$, and that $J^2 = -\mathbb 1$. Compute $\eta^s = J\xi^s$ for $\xi^1 = (1, 0)^{\mathsf T}$, $\xi^2 = (0, 1)^{\mathsf T}$.
*[new]*

^wd-6-b

(c) In the chiral basis, which $\gamma^\mu$ are symmetric, and which are imaginary? Show $(\gamma^\mu)^{\mathsf T}\gamma^0\gamma^2 = -\gamma^0\gamma^2\gamma^\mu$ for every $\mu$ and $(\gamma^0\gamma^2)^2 = \mathbb 1$.
*[new]*

^wd-6-c

(d) With $\eta^s = \xi^{-s}$, show $u^s(p)^{\ast} = -i\gamma^2v^s(p)$ (Peskin–Schroeder derive the conjugate of $v$ instead, eq. (3.144)).
*[variation of PS eq. (3.144)]*

^wd-6-d

### W7. Charge conjugation on the field, in any basis

Charge conjugation acts at the same point, by a matrix on the transposed adjoint; which matrix depends on the basis of $\gamma$'s.

^wd-7

(a) Using W6(d) and the mode expansion, show $U(\mathcal C)\hat\psi(x)U(\mathcal C)^{-1} = -i\gamma^2\hat\psi^{\dagger\mathsf T}(x)$. Show that the law fails if the antiparticle two-spinors are taken as $\eta^s = \xi^s$.
*[variation of PS eq. (3.145)]*

^wd-7-a

(b) Show $-i\gamma^2\hat\psi^{\dagger\mathsf T} = -i\bigl(\hat{\bar\psi}\gamma^0\gamma^2\bigr)^{\mathsf T}$ (the form of the Problem Set 6 conventions), and derive $U(\mathcal C)\hat{\bar\psi}(x)U(\mathcal C)^{-1}$ as the transpose of a column.
*[new]*

^wd-7-b

(c) In another basis of $\gamma$'s the law reads $U(\mathcal C)\hat\psi U(\mathcal C)^{-1} = B\hat\psi^{\dagger\mathsf T}$ with $B(\gamma^\mu)^{\ast}B^{-1} = -\gamma^\mu$. Show that $B\hat\psi^{\dagger\mathsf T}$ solves the Dirac equation when $\hat\psi$ does. Check $B = -i\gamma^2$ in the chiral basis and in the Dirac basis ($\gamma^0_D = \mathrm{diag}(\mathbb 1, -\mathbb 1)$, $\gamma^i_D = \gamma^i$), and find $B$ in the Majorana basis $\gamma^0_M = \begin{pmatrix}0 & \sigma^2\\ \sigma^2 & 0\end{pmatrix}$, $\gamma^1_M = \begin{pmatrix}i\sigma^3 & 0\\ 0 & i\sigma^3\end{pmatrix}$, $\gamma^2_M = \begin{pmatrix}0 & -\sigma^2\\ \sigma^2 & 0\end{pmatrix}$, $\gamma^3_M = \begin{pmatrix}-i\sigma^1 & 0\\ 0 & -i\sigma^1\end{pmatrix}$.
*[new]*

^wd-7-c

### W8. Charge conjugation on the bilinears

Use $U(\mathcal C)\hat\psi U(\mathcal C)^{-1} = -i(\hat{\bar\psi}\gamma^0\gamma^2)^{\mathsf T}$, the result of W7(b) for $\hat{\bar\psi}$, and normal ordering.

^wd-8

(a) Verify the transformations under charge conjugation of the vector $\mathsf V^\mu = \hat{\bar\psi}\gamma^\mu\hat\psi$ and the pseudo-vector $\mathsf A^\mu = \hat{\bar\psi}\gamma^\mu\gamma^5\hat\psi$.
*[HW-literal PS7.2(b)]*

^wd-8-a

(b) Show $U(\mathcal C)\mathsf T^{\mu\nu}(x)U(\mathcal C)^{-1} = -\mathsf T^{\mu\nu}(x)$. More generally, show that $\gamma^0\gamma^2\bigl(\gamma^{\mu_1}\cdots\gamma^{\mu_k}\bigr)^{\mathsf T}\gamma^0\gamma^2 = (-1)^k\gamma^{\mu_k}\cdots\gamma^{\mu_1}$.
*[variation of PS7.2(b): the tensor, which PS give only in their table]*

^wd-8-b

(c) Redo $\mathsf S$ and $\mathsf V^\mu$ treating the components of $\hat\psi$ as commuting numbers. Which signs come out wrong? Without normal ordering, what would be left over in $\mathsf V^0$?
*[extension of PS7.2(b)]*

^wd-8-c

(d) ★ Show that $C$ exchanges the chiral currents: $\overline{\hat\psi_L}\gamma^\mu\hat\psi_L \to -\overline{\hat\psi_R}\gamma^\mu\hat\psi_R$.
*[extension of PS7.2(b)]*

^wd-8-d

### W9. The physical spin of an antiparticle

With $\eta^s = \xi^{-s}$ and the standard $\xi^s$, $v^1$ is built on $\eta^1 = (0, 1)^{\mathsf T}$, spin down, yet $U(\mathcal C)$ maps $\hat a^1$ to $\hat b^1$. The spin operator is $\hat{\mathbf S} = \int d^3x\,\hat\psi^\dagger\frac12\boldsymbol\Sigma\hat\psi$, $\Sigma^k = \mathrm{diag}(\sigma^k, \sigma^k)$.

^wd-9

(a) At momenta along the $z$ axis the antiparticle part of $\hat S^3$ is $\sum_{r,s}\hat b^r_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\,\eta^{r\dagger}\frac{\sigma^3}2\eta^s$ (per unit momentum measure). Reorder it into number operators, and show that the ordering constant vanishes.
*[new]*

^wd-9-a

(b) Show that $\hat b^{1\dagger}_{\mathbf 0}|0\rangle$ has $\hat J_z = +\frac12$ and $\hat b^{2\dagger}_{\mathbf 0}|0\rangle$ has $\hat J_z = -\frac12$, as for $\hat a^{s\dagger}_{\mathbf 0}|0\rangle$. Which two minus signs compensate?
*[new]*

^wd-9-b

(c) What would $\hat b^{1\dagger}_{\mathbf 0}|0\rangle$ carry had $\eta^s = \xi^s$ been chosen, and which law of charge conjugation would then fail?
*[new]*

^wd-9-c

## Time reversal

### W10. Why time reversal is antiunitary

Let $U$ be an invertible operator with $[U, \hat H] = 0$ and $U\hat\psi(t, \mathbf x)U^{-1} = M\hat\psi(-t, \mathbf x)$ for a constant invertible matrix $M$; the Heisenberg field is $\hat\psi(t, \mathbf x) = e^{i\hat Ht}\hat\psi(0, \mathbf x)e^{-i\hat Ht}$.

^wd-10

(a) Show that $U$ cannot be linear. Why does $U\hat HU^{-1} = -\hat H$ with $U$ linear not rescue it?
*[new]*

^wd-10-a

(b) Show that an antilinear $U$ with $UcU^{-1} = c^{\ast}$ works: compute $Ue^{-i\hat Ht}U^{-1}$.
*[new]*

^wd-10-b

(c) For an antiunitary $U$, show $U(cA)U^{-1} = c^{\ast}UAU^{-1}$, $U(AB)U^{-1} = (UAU^{-1})(UBU^{-1})$ and $UA^\dagger U^{-1} = (UAU^{-1})^\dagger$. Which of these makes a $\gamma$-matrix entry, but not the order of two field operators, change under time reversal?
*[new]*

^wd-10-c

### W11. Time reversal on oscillators, spinors and the Dirac field

$U(\mathcal T)$ is antiunitary with $U(\mathcal T)\hat a^s_{\mathbf p}U(\mathcal T)^{-1} = \hat a^{-s}_{-\mathbf p}$, $U(\mathcal T)\hat b^s_{\mathbf p}U(\mathcal T)^{-1} = \hat b^{-s}_{-\mathbf p}$, $U(\mathcal T)|0\rangle = |0\rangle$.

^wd-11

(a) Show that $\gamma^1\gamma^3 = \mathrm{diag}(i\sigma^2, i\sigma^2)$ is real, $(\gamma^1\gamma^3)^2 = -\mathbb 1$, and $(\gamma^\mu)^{\ast}\gamma^1\gamma^3 = \gamma^1\gamma^3\gamma_\mu$ with the lower index.
*[new]*

^wd-11-a

(b) For $\mathbf p$ along $z$ and the standard $\xi^s$, verify $u^s(p)^{\ast} = \gamma^1\gamma^3u^{-s}(\tilde p)$ for $s = 1, 2$.
*[new]*

^wd-11-b

(c) Derive $U(\mathcal T)\hat\psi(t, \mathbf x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(-t, \mathbf x)$, using also $v^s(p)^{\ast} = \gamma^1\gamma^3v^{-s}(\tilde p)$. Why must the oscillator law carry $\hat a^{-2} = -\hat a^1$ rather than $+\hat a^1$? Compare with Peskin–Schroeder's eq. (3.139).
*[variation of PS eq. (3.139)]*

^wd-11-c

(d) Show $U(\mathcal T)^2 = (-1)^{\hat N_a + \hat N_b}$ on the Dirac Fock space. What is $U(\mathcal T)^2$ for the complex scalar with $U(\mathcal T)\hat a_{\mathbf p}U(\mathcal T)^{-1} = \hat a_{-\mathbf p}$, $U(\mathcal T)\hat b_{\mathbf p}U(\mathcal T)^{-1} = \hat b_{-\mathbf p}$?
*[new]*

^wd-11-d

### W12. Time reversal on the bilinears

Use $U(\mathcal T)\hat\psi(x)U(\mathcal T)^{-1} = \gamma^1\gamma^3\hat\psi(x_T)$ with $U(\mathcal T)$ antiunitary.

^wd-12

(a) Verify the transformations under time-reversal of the pseudo-scalar $\mathsf P = i\hat{\bar\psi}\gamma^5\hat\psi$ and the vector $\mathsf V^\mu = \hat{\bar\psi}\gamma^\mu\hat\psi$.
*[HW-literal PS7.2(c)]*

^wd-12-a

(b) Show $U(\mathcal T)\mathsf A^\mu(x)U(\mathcal T)^{-1} = \mathcal P^\mu{}_\nu\mathsf A^\nu(x_T)$ (Peskin–Schroeder: "You can verify that the pseudo-vector transforms in exactly the same way").
*[variation of PS7.2(c)]*

^wd-12-b

(c) Find $U(\mathcal T)\mathsf T^{\mu\nu}(x)U(\mathcal T)^{-1}$. Which components flip, and how does that compare with parity? Where does the extra sign come from?
*[variation of PS7.2(c): the tensor]*

^wd-12-c

## The complex scalar under C and T

### W13. C, P and T for the complex boson

Adapted from PS Problem 3.7(b)+(c). The problem set's $\phi^{\ast}$ is the operator $\hat\phi^\dagger$ here, and its $\mathcal P$, $\mathcal C$, $\mathcal T$ are $U(\mathcal P)$, $U(\mathcal C)$, $U(\mathcal T)$, with $\mathcal P^\dagger = \mathcal P^{-1}$ and so on.

^wd-13

(a) Let $\hat\phi(x)$ be a complex-valued Klein–Gordon field. Find unitary operators $\mathcal P$, $\mathcal C$, and an anti-unitary operator $\mathcal T$, that give $\mathcal P\hat\phi(t, \mathbf x)\mathcal P^\dagger = \hat\phi(t, -\mathbf x)$, $\mathcal C\hat\phi(t, \mathbf x)\mathcal C^\dagger = \hat\phi^\dagger(t, \mathbf x)$, $\mathcal T\hat\phi(t, \mathbf x)\mathcal T^\dagger = \hat\phi(-t, \mathbf x)$. The operators should all be defined in terms of their action on the annihilation operators $\hat a_{\mathbf p}$, $\hat b_{\mathbf p}$.
*[HW-literal PS7.4(a)]*

^wd-13-a

(b) Find the transformation properties of the current $J^\mu = i[\hat\phi^\dagger(\partial^\mu\hat\phi) - (\partial^\mu\hat\phi^\dagger)\hat\phi]$ under $\mathcal P$, $\mathcal C$ and $\mathcal T$.
*[HW-literal PS7.4(b)]*

^wd-13-b

(c) Find the images of $\hat Q$ and of the momentum $\hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$ under $\mathcal P$, $\mathcal C$ and $\mathcal T$.
*[extension of PS7.4(b)]*

^wd-13-c

(d) For the real field of W2, show that an antiunitary $U(\mathcal T)$ with $U(\mathcal T)\hat a_{\mathbf p}U(\mathcal T)^{-1} = \hat a_{-\mathbf p}$ gives $\hat\phi(x_T)$, and that every unitary $U$ with $U\hat a_{\mathbf p}U^{-1} = \eta_C\hat a_{\mathbf p}$ and $U\hat\phi U^{-1} \propto \hat\phi$ has $\eta_C = \pm1$. Why is there no charge conjugation exchanging two species?
*[variation of PS7.4(a): the real field]*

^wd-13-d

## CPT

### W14. CPT on the Dirac field

Use the three field laws of the conventions. Problem Set 7's $\psi^{\ast}(x) \equiv (\psi(x)^\dagger)^{\mathsf T}$ is $\hat\psi^{\dagger\mathsf T}(x)$ here, and $\Theta^\dagger = \Theta^{-1}$.

^wd-14

(a) CPT is the operation that performs the three discrete symmetry transformations in succession; define $\Theta \equiv \mathcal C\mathcal P\mathcal T$. Show that under $\Theta$ the Dirac field transforms as $\Theta\hat\psi(x)\Theta^\dagger = \gamma^5\hat\psi^{\dagger\mathsf T}(-x)$. Take the phase associated with parity $\eta_a = 1$.
*[HW-literal PS7.3]*

^wd-14-a

(b) Redo (a) with a general parity phase $\eta_a$. Is $\eta_a$ conjugated? Is $\Theta$ unitary or antiunitary?
*[variation of PS7.3]*

^wd-14-b

(c) Compute $\Theta'\hat\psi(x)\Theta'^{-1}$ for $\Theta' = U(\mathcal T)U(\mathcal P)U(\mathcal C)$ (first $\mathcal C$, then $\mathcal P$, then $\mathcal T$), and show that $\Theta'$ and $\Theta$ act in the same way on every bilinear.
*[variation of PS7.3: the other order]*

^wd-14-c

### W15. CPT on bilinears and on the scalar; the (−1)^n rule

Use the $C$, $P$, $T$ laws found above and $\Theta = U(\mathcal C)U(\mathcal P)U(\mathcal T)$, first $\mathcal T$.

^wd-15

(a) From the $C$, $P$ and $T$ laws of W5, W8 and W12, find $\Theta\mathsf A^\mu(x)\Theta^{-1}$ and $\Theta\mathsf T^{\mu\nu}(x)\Theta^{-1}$, and $\Theta$ on a derivative $\partial_\mu$ of a field. State the rule for a bilinear with $n$ Lorentz indices.
*[extension of PS7.3]*

^wd-15-a

(b) For the complex scalar with all phases $1$, find $\Theta\hat\phi(x)\Theta^{-1}$, $\Theta\,\partial^\mu\hat\phi(x)\,\Theta^{-1}$ and $\Theta\hat j^\mu(x)\Theta^{-1}$.
*[extension of PS7.4(b)]*

^wd-15-b

(c) Argue that any Hermitian, local, Lorentz-scalar operator built from a Dirac spinor $\hat\psi(x)$, a complex scalar $\hat\phi(x)$ and their conjugates is invariant under CPT. You are not expected to present anything close to a formal proof, just a qualitative argument that captures why the conclusion is difficult to avoid.
*[HW-literal PS7.4(c)]*

^wd-15-c

(d) Which of $C$, $P$, $T$, $CPT$ leave each of $\mathsf V_\mu\mathsf A^\mu$, $\partial_\mu\mathsf A^\mu$ and $i\mathsf S$ invariant (up to the move of the point)? What goes wrong with $i\mathsf S$?
*[extension of PS7.4(c)]*

^wd-15-d

## Invariance of the free Lagrangians

### W16. The free Lagrangians under C, P and T

The Lagrangians are normal-ordered; a transformation is a symmetry of the theory if it maps the action to itself.

^wd-16

(a) Show that the free complex-scalar Lagrangian $\partial_\mu\hat\phi^\dagger\partial^\mu\hat\phi - m^2\hat\phi^\dagger\hat\phi$ (normal-ordered) is invariant under $\mathcal P$, $\mathcal C$, $\mathcal T$ of W13(a).
*[extension of PS7.4(b)]*

^wd-16-a

(b) Show $U(\mathcal C)\hat{\mathcal L}_D(x)U(\mathcal C)^{-1} = \hat{\mathcal L}_D(x) - i\partial_\mu\mathsf V^\mu(x)$ for $\hat{\mathcal L}_D = i\hat{\bar\psi}\gamma^\mu\partial_\mu\hat\psi - m\hat{\bar\psi}\hat\psi$. Why is the theory still $C$ invariant?
*[new]*

^wd-16-b

(c) Show $U(\mathcal T)\hat{\mathcal L}_D(t, \mathbf x)U(\mathcal T)^{-1} = \hat{\mathcal L}_D(-t, \mathbf x)$: name the three signs that meet in the kinetic term.
*[new]*

^wd-16-c

(d) Add $m'\,\mathsf P$ ($m'$ real) to $\hat{\mathcal L}_D$. Which of $C$, $P$, $T$, $CP$ and $CPT$ does it violate?
*[new]*

^wd-16-d

## The vector field

### W17★. The field tensor under C, P and T

Take a classical external potential $A^\mu(x)$ coupled to the Dirac field through $\hat{\mathcal L}_{\rm int} = -e\,A_\mu\mathsf V^\mu$ ($e$ real), $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, $F^{0i} = -E^i$, $F^{ij} = -\varepsilon_{ijk}B^k$.

^wd-17

(a) Find how $A^\mu$ must transform under each of $C$, $P$, $T$ (as a function: $A^\mu(x) \to A'^\mu(x)$) so that $U\int d^4x\,\hat{\mathcal L}_{\rm int}[A]\,U^{-1} = \int d^4x\,\hat{\mathcal L}_{\rm int}[A']$.
*[new]*

^wd-17-a

(b) Deduce the laws of $F^{\mu\nu}$, $\mathbf E$ and $\mathbf B$. Compare with $\mathsf T^{\mu\nu}$, and check that the Pauli term $\mathsf T^{\mu\nu}F_{\mu\nu}$ is $C$, $P$ and $T$ invariant.
*[new]*

^wd-17-b

(c) Which of $F_{\mu\nu}F^{\mu\nu}$ and $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$ are $P$ and $T$ invariant? Is $\mathbf E\cdot\mathbf B$ CPT invariant?
*[new]*

^wd-17-c

## All fields

### W18. Short response

Short answers: a formula, a number, or a phrase. No derivations are needed.
*[variation of PS7.1]*

^wd-18

(a) $\det\Lambda$ and the sign of $\Lambda^0{}_0$ for $\mathcal P$, $\mathcal T$, $\mathcal P\mathcal T$.

^wd-18-a

(b) $\eta_a\eta_b$ for the complex scalar and for the Dirac field; the parity of the $L = 0$ ground state of positronium.

^wd-18-b

(c) Which of $U(\mathcal P)$, $U(\mathcal C)$, $U(\mathcal T)$, $\Theta$ are antiunitary?

^wd-18-c

(d) The matrix multiplying $\hat\psi^{\dagger\mathsf T}$ under $C$ in the chiral basis and in a Majorana basis.

^wd-18-d

(e) The matrix in $U(\mathcal T)\hat\psi U(\mathcal T)^{-1}$ in the course and in Peskin–Schroeder eq. (3.139); does the difference change any bilinear?

^wd-18-e

(f) The signs of $\mathsf T^{0i}$ and $\mathsf T^{ij}$ under $P$, under $T$ and under $C$.

^wd-18-f

(g) $\Theta\mathsf A^\mu(x)\Theta^{-1}$; $\Theta\,\partial_\mu\mathsf A^\mu(x)\,\Theta^{-1}$.

^wd-18-g

(h) $U(\mathcal T)^2$ on a one-fermion state and on a one-scalar state.

^wd-18-h

(i) The physical spin $\hat J_z$ of $\hat b^{1\dagger}_{\mathbf 0}|0\rangle$ and the wave-function spin of its $\eta^1$.

^wd-18-i

(j) Under $C$ and under $T$, the charge densities $\mathsf V^0$ (Dirac) and $\hat j^0$ (complex scalar).

^wd-18-j
