---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.9
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.8 Wave Packets and the Cross Section]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential]] →

*Sources: the user's PHY 513 notes, Ch. 15 §15.3 (the completeness relation after eq. (Pb); the rest of §15.2–§15.3, the definitions, is the source of [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]]), §15.4 (eq. (dsigmafull), paragraph "Counting", Derivations "The $\delta$-functions and the one Jacobian", "A $\delta$-function of a function (filled in)", Caution "$1/f'(0)$ on the slide", paragraphs "Integrating over $\bar k_B^z$ instead", "A second zero (filled in)", "Smoothness"), §15.5 (Principle "Cross section for $2\to n$ scattering", paragraphs "Reading the formula", "Identical particles (filled in)"; its Derivation "Dimension check (filled in)" is [[§C6b.3 The Cross Section#^thm-c6b-3-11|Theorem §C6b.3.11]]) · the user's PHY 513 notes, Ch. 15 §15.6 (Derivation "The flux factor as an $\varepsilon$-tensor component", Principle "Same cross section in the CM and target frames", eq. (moller)), §15.10 (paragraph "Correspondence with Yu") · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part B, slides 13–16, Part C, slide 19, and transcript · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 103–106 and 108, eqs. (4.76)–(4.80) · Yu Zhao-Huan, 量子场论讲义, §6.5.1–§6.5.2, eqs. (6.276)–(6.331); §6.5.3, eqs. (6.336)–(6.366), by number only (worked in [[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]]).*

The quantum cross section of [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]], $d\sigma = \int d^2b\,\mathcal P(\mathbf b)$ ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]) for the two-packet state of [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3|Def. §C6b.8.3]], evaluated; away from the forward direction only $i\hat T$ contributes ([[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]]). The result, after fourteen integrals, one Jacobian and an argument from smoothness, is the longest formula of the course, [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]]: initial kinematics × $|\mathcal M|^2$ × final phase space. It is done once and never again. It is the careful version of [[§C6b.3 The Cross Section|§C6b.3]]: the result is [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], 2, which Yu reaches without wave packets, in a box of volume $\tilde V$ with $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ ([[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-10|Theorem §CA.4.10]]; [[§C6b.2 Transition Probabilities in a Box|§C6b.2]]); the table in the opening of [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]] maps every step below to the box step it replaces. Two lessons of the evaluation are boxes of their own: only one root of the longitudinal constraints contributes ([[§C6b.9 Evaluating the Cross Section#^lem-c6b-9-2|Lemma §C6b.9.2]]), and the Jacobian is a flux ([[§C6b.9 Evaluating the Cross Section#^rem-c6b-9-1|§C6b.9, Remark: Why a Jacobian is a flux]]). The section ends with the course's route to frame independence, Lecture 15, Part C: the flux factor is a component of an antisymmetric tensor and the cross section transforms like an area ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|Theorem §C6b.9.6]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]]); then Yu's routes.

*Conventions* ([[Larsen PHY 513]]): beams along the $z$-axis; $\perp$ marks the components $(x, y)$ transverse to it; $E_A \equiv E_{\mathbf k_A} = \sqrt{\mathbf k_A^2 + m_A^2}$ inside integrals and $E_A = E_{\mathbf p_A}$ in final formulas; $\mathbf v = \mathbf k/E = \partial E_{\mathbf k}/\partial\mathbf k$ is the velocity, the group velocity of a packet peaked at $\mathbf k$; barred momenta $\bar{\mathbf k}_A$, $\bar{\mathbf k}_B$ label the second, complex-conjugated copy of an amplitude; $\varepsilon^{0123} = +1$, hence $\varepsilon_{0123} = -1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]; PS have $-1$); $x, y = 1, 2$.

## Doing the integrals

Inserting [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3|Def. §C6b.8.3]] into [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]] and [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]], the square brings in a second, complex-conjugated copy of the packet integral, with its own variables $\bar{\mathbf k}_A$, $\bar{\mathbf k}_B$ (slide 13). For any integrable $f$, the modulus squared of an integral is a double integral, the second copy conjugated:

$$
\Bigl|\int d^3k\,f(\mathbf k)\Bigr|^2 = \int d^3k\,f(\mathbf k)\;\overline{\int d^3\bar k\,f(\bar{\mathbf k})} = \int d^3k\,d^3\bar k\;f(\mathbf k)\,f^\ast(\bar{\mathbf k}) ,
$$

applied here with $\mathbf k = (\mathbf k_A, \mathbf k_B)$ and $f$ the integrand of [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3|Def. §C6b.8.3]] times the amplitude:

$$
\begin{aligned}
d\sigma = {}&\Bigl(\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\Bigr)\int d^2b\,\frac{d^3k_A}{(2\pi)^3}\frac{d^3k_B}{(2\pi)^3}\frac{d^3\bar k_A}{(2\pi)^3}\frac{d^3\bar k_B}{(2\pi)^3}\;e^{-i\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B)}\\
&\times\frac{\phi_A(\mathbf k_A)}{\sqrt{2E_A}}\frac{\phi_B(\mathbf k_B)}{\sqrt{2E_B}}\frac{\phi_A^\ast(\bar{\mathbf k}_A)}{\sqrt{2\bar E_A}}\frac{\phi_B^\ast(\bar{\mathbf k}_B)}{\sqrt{2\bar E_B}}\;\langle\mathbf p_1\mathbf p_2\cdots|\mathbf k_A\mathbf k_B\rangle\,\langle\mathbf p_1\mathbf p_2\cdots|\bar{\mathbf k}_A\bar{\mathbf k}_B\rangle^\ast .
\end{aligned}
$$

The expression is complicated because probabilities are squares of amplitudes. There are 14 integrals, $3 + 3 + 3 + 3$ momenta and 2 components of $\mathbf b$; six of them give delta functions, which then remove six more, so two remain. The fourteen, and where each goes in [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]]:

| integrals | number | done by | step |
|---|---|---|---|
| $d^2b$ | 2 | $\int d^2b\,e^{-i\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B)} = (2\pi)^2\delta^2(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp)$: produces 2 deltas | 1 |
| $d^2\bar k_B^\perp$ | 2 | $\delta^2(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp)$ from $d^2b$ | 3 |
| $d^2\bar k_A^\perp$ | 2 | transverse part of $\delta^4(\bar k_A + \bar k_B - \sum p_i)$ | 3 |
| $d\bar k_A^z\,d\bar k_B^z$ | 2 | $z$ and energy parts of $\delta^4(\bar k_A + \bar k_B - \sum p_i)$, one Jacobian | 4 |
| $d^3k_A\,d^3k_B$ | 6 | smoothness and the normalization of the packets | 7–8 |

Six deltas ($2$ from $\mathbf b$, $4$ from the barred amplitude) do the six $\bar k$ integrals; the remaining six, over $\mathbf k_A$ and $\mathbf k_B$, collapse by the normalization of the packets (the user's notes, Ch. 15 §15.4, paragraph "Counting"); the $\delta^4$ of the unbarred amplitude is never used up.

> [!caution] Caution: The conjugated profiles on slide 13
> Slide 13 writes the factors of the second copy as $\phi(\bar k_A)$, $\phi(\bar k_B)$. They come from the complex conjugate of the amplitude and are $\phi_A^\ast(\bar{\mathbf k}_A)$, $\phi_B^\ast(\bar{\mathbf k}_B)$ (the phase $e^{+i\mathbf b\cdot\bar{\mathbf k}_B}$ in the slide's exponent is conjugated correctly). With the conjugates the smoothness step produces $|\phi_A(\mathbf k_A)|^2|\phi_B(\mathbf k_B)|^2$, as slide 15 says.
>
> *Source: PHY 513 Lecture 15, slides 13, 15 (page images) · PS §4.5, eq. (4.76) · the user's PHY 513 notes, Ch. 15 §15.4, eq. (dsigmafull)*

^cau-c6b-9-1

Why the integrals split into transverse and longitudinal ones: the impact parameter is transverse, $\mathbf b\cdot\mathbf k_B = \mathbf b\cdot\mathbf k_B^\perp$ ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-3|Theorem §C6b.8.3]], What the derivation shows), so the $\mathbf b$-integral constrains only $\bar{\mathbf k}_B^\perp$. With the transverse parts of the barred $\delta^4$ it fixes the four transverse barred components, and two longitudinal ones remain, $\bar k_A^z$, $\bar k_B^z$, with the $z$ and energy parts of the barred $\delta^4$. The next theorem does those two integrals.

> [!theorem] Theorem §C6b.9.1: The Longitudinal Integrals Give the Velocity Difference
> Let $P = \sum_ip_i$ be the total final four-momentum, $P^z$ its $z$-component and $E = P^0$ its energy, and fix the transverse momenta $\bar{\mathbf k}_A^\perp$, $\bar{\mathbf k}_B^\perp$ (in the cross section the $\mathbf b$-integral and the transverse delta functions fix them; the theorem is used in [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]], Step 4). Write $\bar E_A = \sqrt{\bar{\mathbf k}_A^2 + m_A^2}$, $\bar E_B = \sqrt{\bar{\mathbf k}_B^2 + m_B^2}$. For a smooth $g$, if the constraints have simple zeros,
>
> $$
> \int d\bar k_A^z\,d\bar k_B^z\;\delta\bigl(\bar k_A^z + \bar k_B^z - P^z\bigr)\,\delta\bigl(\bar E_A + \bar E_B - E\bigr)\,g = \sum_{\text{zeros}}\frac{g}{\bigl|\bar k_A^z/\bar E_A - \bar k_B^z/\bar E_B\bigr|} = \sum_{\text{zeros}}\frac{g}{|\bar v_A^z - \bar v_B^z|} .
> $$
>
> At the zero $\bar{\mathbf k} = \mathbf k$ of collinear beams along $z$ the factor is $1/|\mathbf v_A - \mathbf v_B|$.
>
> *Model:* any (kinematics); *applies:* any smooth $g$, constraints with simple zeros; independent of the dynamics.
>
> *Source: PHY 513 Lecture 15, slide 14 ("$= \frac{1}{|\frac{\bar k_A^z}{E_A} - \frac{\bar k_B^z}{E_B}|} = \frac{1}{|\vec v_A - \vec v_B|}$ … Final equality: $\vec k = \gamma m\vec v$, $E = \gamma m$"), and transcript · the user's PHY 513 notes, Ch. 15 §15.4, eq. (jacobian), paragraphs "Integrating over $\bar k_B^z$ instead", "A second zero (filled in)" · PS §4.5, eq. (4.77)*

^thm-c6b-9-1

> [!derivation]- Derivation
> **Step 1** (the linear delta). $\delta(\bar k_A^z + \bar k_B^z - P^z)$ does the $\bar k_B^z$ integral with Jacobian 1 ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1): "$\vec{\bar k}_B$ as determined by momentum conservation" (slide 14),
>
> $$
> \int d\bar k_B^z\;\delta\bigl(\bar k_B^z - (P^z - \bar k_A^z)\bigr)\,\delta\bigl(\bar E_A + \bar E_B - E\bigr)\,g = \delta\bigl(\bar E_A + \bar E_B - E\bigr)\,g\Big|_{\bar k_B^z = P^z - \bar k_A^z} .
> $$
>
> **Step 2** (the remaining delta). What is left is $\int d\bar k_A^z\,\delta(f(\bar k_A^z))\,g$ with
>
> $$
> f(x) = \sqrt{\bar{\mathbf k}_A^{\perp2} + x^2 + m_A^2} + \sqrt{\bar{\mathbf k}_B^{\perp2} + (P^z - x)^2 + m_B^2} - E ,
> $$
>
> a quite nonlinear function: both square roots depend on $x = \bar k_A^z$, the second through $\bar k_B^z = P^z - x$.
>
> **Step 3** (the derivative). $\frac{d}{dx}\sqrt{c + x^2} = \frac{x}{\sqrt{c + x^2}}$; for the second root, with $c' = \bar{\mathbf k}_B^{\perp2} + m_B^2$ and the chain rule, $\frac{d}{dx}\sqrt{c' + (P^z - x)^2} = \frac{(P^z - x)}{\sqrt{c' + (P^z - x)^2}}\cdot\frac{d(P^z - x)}{dx} = -\frac{\bar k_B^z}{\bar E_B}$. So
>
> $$
> f'(x) = \frac{x}{\sqrt{\bar{\mathbf k}_A^{\perp2} + x^2 + m_A^2}} - \frac{P^z - x}{\sqrt{\bar{\mathbf k}_B^{\perp2} + (P^z - x)^2 + m_B^2}} = \frac{\bar k_A^z}{\bar E_A} - \frac{\bar k_B^z}{\bar E_B} .
> $$
>
> **Step 4** (δ of a function). By [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2, over the simple zeros $x_0$ of $f$: the delta function becomes one over $f'$, evaluated at the zero.
>
> $$
> \int dx\;\delta\bigl(f(x)\bigr)\,g(x) = \int dx\sum_{x_0}\frac{\delta(x - x_0)}{|f'(x_0)|}\,g(x) = \sum_{x_0}\frac{g(x_0)}{|f'(x_0)|} = \sum_{x_0}\frac{g(x_0)}{\bigl|\bar k_A^z/\bar E_A - \bar k_B^z/\bar E_B\bigr|_{x_0}} .
> $$
>
> The absolute value is the orientation of the substitution $u = f(x)$; $f'$ is negative whenever $B$ moves faster in the $+z$ direction than $A$.
>
> **Step 5** (velocities). For a particle of mass $m$, $\mathbf k = \gamma m\mathbf v$ and $E = \gamma m$, so the ratio is the velocity:
>
> $$
> \frac{\mathbf k}{E} = \frac{\gamma m\mathbf v}{\gamma m} = \mathbf v , \qquad |f'| = \bigl|\bar v_A^z - \bar v_B^z\bigr| .
> $$
>
> At the zero $\bar{\mathbf k} = \mathbf k$ with both momenta along $z$, $\mathbf v_A^\perp = \mathbf v_B^\perp = 0$ and $|\mathbf v_A - \mathbf v_B| = \sqrt{0^2 + 0^2 + (v_A^z - v_B^z)^2} = |v_A^z - v_B^z|$.
>
> ⚑ By-product: with the transverse momenta fixed, conservation of $k^z$ and of energy for two particles has in general *two* solutions $\bar k_A^z$: $\bar k_A^z = k_A^z$, and a "reflected" configuration ($A$ and $B$ swapped in direction). In the centre-of-mass frame with $\bar{\mathbf k}^\perp = 0$, $P^z = 0$ and
>
> $$
> f(x) = \sqrt{x^2 + m_A^2} + \sqrt{x^2 + m_B^2} - E = f(-x) ,
> $$
>
> so $f(k_A^z) = 0$ implies $f(-k_A^z) = 0$: the second root is $\bar k_A^z = -k_A^z$. The reflected root lies far from the peak of $\phi_A$, so $\phi_A^\ast(\bar{\mathbf k}_A) \approx 0$ there and it does not contribute for sharply peaked packets (checked numerically, in the user's notes and here: $m_A = 1$, $m_B = 1.7$, $\mathbf k_A = (0.3, -0.2, 1.1)$, $\mathbf k_B = (0.1, 0.25, -0.8)$ give the roots $1.1$ and $-0.847$, and $1/|f'| = 1/|v_A - v_B| = 0.8767$ at the first) → [[§C6b.9 Evaluating the Cross Section#^lem-c6b-9-2|Lemma §C6b.9.2]].
>
> **What the derivation shows.**
> - The only non-trivial step of the whole computation is one Jacobian, and it is the kinematic velocity difference of the two beams, naturally a part of the kinematics of scattering.
> - Integrating over $\bar k_B^z$ instead, eliminating $\bar k_A^z$, gives $-f'$ and, with the absolute value, the same result.
> - Why a Jacobian is a flux: the factor is the inverse flux of one particle per box of the main line → [[§C6b.9 Evaluating the Cross Section#^rem-c6b-9-1|§C6b.9, Remark: Why a Jacobian is a flux]].

^der-c6b-9-1

*Uses:* [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!theorem] Lemma §C6b.9.2: The Reflected Root Does Not Contribute
> With the transverse momenta fixed, the two constraints of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]] have exactly two simple zeros whenever $\bar v_A^z \ne \bar v_B^z$ at one of them: $\bar k_A^z = k_A^z$, and a "reflected" configuration ($A$ and $B$ swapped in direction; in the centre-of-mass frame with $\bar{\mathbf k}^\perp = 0$, $\bar k_A^z = -k_A^z$). For packets narrower than the distance between the two zeros ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]]) only the first contributes: the profile $\phi_A^\ast(\bar{\mathbf k}_A)$ vanishes at the reflected root.
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* narrow packets, colliding beams ($v_A^z \ne v_B^z$).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.4 (paragraph "A second zero (filled in)") · PHY 513 Lecture 15, slide 14, and transcript*

^lem-c6b-9-2

> [!derivation]- Derivation
> **Step 1** (at most two zeros). In [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-1|Derivation §C6b.9.1]], Step 2, $f(x) = \sqrt{a + x^2} + \sqrt{b + (P^z - x)^2} - E$ with $a = \bar{\mathbf k}_A^{\perp2} + m_A^2 > 0$, $b = \bar{\mathbf k}_B^{\perp2} + m_B^2 > 0$. Each root is strictly convex,
>
> $$
> \frac{d^2}{dx^2}\sqrt{a + x^2} = \frac{a}{(a + x^2)^{3/2}} > 0 ,
> $$
>
> so $f$ is strictly convex and has at most two zeros; since $f \to +\infty$ as $x \to \pm\infty$, a zero with $f' \ne 0$ ($\bar v_A^z \ne \bar v_B^z$, [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-1|Derivation §C6b.9.1]], Step 3) has exactly one partner on the other side of the minimum of $f$, and the two merge only where $f' = 0$, i.e. where the packets do not approach each other.
>
> **Step 2** (the reflected root in the centre-of-mass frame). With $\bar{\mathbf k}^\perp = 0$ and $P^z = 0$, $f(x) = \sqrt{x^2 + m_A^2} + \sqrt{x^2 + m_B^2} - E = f(-x)$: if $k_A^z$ is a zero, so is $-k_A^z$ (the ⚑ of [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-1|Derivation §C6b.9.1]]).
>
> **Step 3** (suppression). $\phi_A$ is peaked at $\mathbf p_A$ with a width small compared with the distance between the two zeros ($2|k_A^z|$ in the centre-of-mass frame), so $\phi_A^\ast(\bar{\mathbf k}_A) \approx 0$ at the reflected root and its term in [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]] vanishes. Checked numerically (the user's notes, and here): $m_A = 1$, $m_B = 1.7$, $\mathbf k_A = (0.3, -0.2, 1.1)$, $\mathbf k_B = (0.1, 0.25, -0.8)$ give the roots $1.1$ and $-0.847$.
>
> **What the derivation shows.**
> - "Simply take $\bar k_A = k_A$" ([[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]], Step 5) rests on this lemma; it needs the beams to collide and the packets to be narrow.

^der-c6b-9-2

*Uses:* [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]]

> [!remark] Remark: Why a Jacobian is a flux
> In the box route the factor $1/|\mathbf v_A - \mathbf v_B|$ of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]] comes from $\tilde V/|\mathbf v_B| = 1/j_B$, the inverse flux of one particle per box ([[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]], [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]]), whose $\tilde V$ cancels the last $1/\tilde V$ of the rate: in the rest frame of $A$
>
> $$
> \frac{1}{|\mathbf v_A - \mathbf v_B|}\bigg|_{\mathbf v_A = \mathbf 0} = \frac{1}{|\mathbf v_B|} = \frac{1}{\tilde V\,j_B} .
> $$
>
> Here the energy delta function measures how fast the two packets pass through each other along $z$: the rate at which they overlap, per unit transverse area.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.4, §15.10 (paragraph "Correspondence with Yu") · Yu §6.5.2, eq. (6.313)*

^rem-c6b-9-1

> [!caution] Caution: 1/f′(0) on slide 14
> Slide 14 states the rule as $\int\delta(f(x))\,dx = \frac{1}{f'(0)}$ with $x = \bar k_A^z$. Read "0" as "the point $x_0$ where $f = 0$": the derivative is evaluated at the zero of $f$, not at $x = 0$, and it needs an absolute value (the slide's next line has it), $1/|f'(x_0)|$; when $f$ has several zeros their contributions add ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 2).
>
> *Source: PHY 513 Lecture 15, slide 14 (page image) · the user's PHY 513 notes, Ch. 15 §15.4, Caution "$1/f'(0)$ on the slide"*

^cau-c6b-9-2

> [!theorem] Theorem §C6b.9.3: The Cross Section for 2 → n Scattering
> For narrow wave packets and final states different from the initial state,
>
> $$
> d\sigma = \underbrace{\frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}}_{\text{kinematics of the initial particles}}\;\underbrace{|\mathcal M(p_A, p_B \to \{p_i\})|^2}_{\text{dynamics}}\;\underbrace{\Bigl(\prod_{i=1}^n\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\Bigr)(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_ip_i\Bigr)}_{\text{kinematics of the final particles}} ,
> $$
>
> with $\mathbf v_{A,B} = \mathbf p_{A,B}/E_{A,B}$ along the beam axis and $\mathcal M$ of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]. All dependence on the shapes of the packets has disappeared.
>
> *Assumptions* (each used once in the derivation): (1) narrow packets, $|\phi_A|^2$, $|\phi_B|^2$ peaked at $\mathbf p_A$, $\mathbf p_B$ (Steps 7–8; [[§C6b.9 Evaluating the Cross Section#^lem-c6b-9-2|Lemma §C6b.9.2]]); (2) $\mathcal M$, the energies and the velocities smooth on the scale of the packet widths (Step 7); (3) final states different from the initial one, no forward scattering ([[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]]); (4) a detector acceptance smooth on the same scale (the ⚑ of Step 7); (5) collinear beams along $z$ (Step 9).
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* as there (with $\mathcal M$ from the Feynman rules: exact if $\hat H_{\rm int}(t) \to 0$ for $|t| \to \infty$, lowest order for a permanent interaction).
>
> *Source: PHY 513 Lecture 15, slide 16 ("Final Result. Collect all factors: $d\sigma = \frac{1}{2E_A2E_B|\vec v_A - \vec v_B|}\cdot|\mathcal M|^2\cdot\bigl(\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\bigr)(2\pi)^4\delta^{(4)}(p_A + p_B - \sum_ip_i)$ … 1st factor: kinematics of initial particles. 3rd and 4th factor: kinematics of final particles. 2nd factor: the amplitude squared $|\mathcal M|^2$. This is dynamical information."), slides 13–15, and transcript · the user's PHY 513 notes, Ch. 15 §15.5, Principle "Cross section for $2\to n$ scattering" (a derived result: a theorem here) · PS §4.5, eq. (4.79) · Yu §6.5.2, eq. (6.320)*

^thm-c6b-9-3

> [!derivation]- Derivation
> Start from the 14-fold integral above (the definitions inserted, the square written as the product of the amplitude and its conjugate). The integrals are exchanged freely: the packets are smooth and rapidly decreasing, and every delta function is used against them (the physicists' route of [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]]).
>
> **Step 1** (the impact parameter; slide 13, item 1). $\mathbf b$ has only transverse components, so $\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B) = \mathbf b\cdot(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp)$ and, by [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] in two dimensions,
>
> $$
> \int d^2b\;e^{-i\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B)} = (2\pi)^2\,\delta^2\bigl(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp\bigr) .
> $$
>
> Because the $A$ particle and the $B$ particle are shifted by $b$ relative to each other and all $b$ are integrated over, the two copies of the momenta have to agree, but only in the transverse directions.
>
> **Step 2** (the amplitudes; slide 13, item 2). The final states differ from the initial one, so only $i\hat T$ contributes ([[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]]), and by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]
>
> $$
> \langle\mathbf p_1\cdots|\mathbf k_A\mathbf k_B\rangle = i\mathcal M\,(2\pi)^4\delta^4\Bigl(k_A + k_B - \sum_ip_i\Bigr), \qquad \langle\mathbf p_1\cdots|\bar{\mathbf k}_A\bar{\mathbf k}_B\rangle^\ast = -i\bar{\mathcal M}^\ast\,(2\pi)^4\delta^4\Bigl(\bar k_A + \bar k_B - \sum_ip_i\Bigr) ,
> $$
>
> with $\mathcal M \equiv \mathcal M(k_A, k_B \to \{p_i\})$, $\bar{\mathcal M} \equiv \mathcal M(\bar k_A, \bar k_B \to \{p_i\})$; the delta function is real, and $(i)(-i) = 1$. All four momenta $k_A, k_B, \bar k_A, \bar k_B$ are on the mass shell, $k^0 = E_{\mathbf k}$. Write $P \equiv \sum_ip_i$ (so $P^0 = \sum_iE_i$), $d\Phi_f \equiv \prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}$ and
>
> $$
> \Phi \equiv \frac{\phi_A(\mathbf k_A)}{\sqrt{2E_A}}\frac{\phi_B(\mathbf k_B)}{\sqrt{2E_B}} , \qquad \bar\Phi \equiv \frac{\phi_A^\ast(\bar{\mathbf k}_A)}{\sqrt{2\bar E_A}}\frac{\phi_B^\ast(\bar{\mathbf k}_B)}{\sqrt{2\bar E_B}} .
> $$
>
> Steps 1 and 2 inserted into the 14-fold integral:
>
> $$
> d\sigma = d\Phi_f\int\frac{d^3k_A\,d^3k_B}{(2\pi)^6}\int\frac{d^3\bar k_A\,d^3\bar k_B}{(2\pi)^6}\;(2\pi)^2\delta^2\bigl(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp\bigr)\;\Phi\,\bar\Phi\;\mathcal M\bar{\mathcal M}^\ast\;(2\pi)^4\delta^4(k_A + k_B - P)\;(2\pi)^4\delta^4(\bar k_A + \bar k_B - P) .
> $$
>
> **Step 3** (the transverse $\bar k$ integrals; slide 14, first bullet). Split the barred delta function by components,
>
> $$
> (2\pi)^4\delta^4(\bar k_A + \bar k_B - P) = (2\pi)^2\delta^2\bigl(\bar{\mathbf k}_A^\perp + \bar{\mathbf k}_B^\perp - \mathbf P^\perp\bigr)\cdot(2\pi)^2\delta\bigl(\bar k_A^z + \bar k_B^z - P^z\bigr)\,\delta\bigl(\bar E_A + \bar E_B - P^0\bigr) ,
> $$
>
> and write $d^3\bar k = d^2\bar k^\perp\,d\bar k^z$. The two transverse deltas do the four transverse integrals, $d^2\bar k_B^\perp$ first: for any smooth $G$,
>
> $$
> \int\frac{d^2\bar k_A^\perp}{(2\pi)^2}\frac{d^2\bar k_B^\perp}{(2\pi)^2}\;(2\pi)^2\delta^2\bigl(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp\bigr)\,(2\pi)^2\delta^2\bigl(\bar{\mathbf k}_A^\perp + \bar{\mathbf k}_B^\perp - \mathbf P^\perp\bigr)\,G = \int\frac{d^2\bar k_A^\perp}{(2\pi)^2}(2\pi)^2\delta^2\bigl(\bar{\mathbf k}_A^\perp + \mathbf k_B^\perp - \mathbf P^\perp\bigr)\,G\Big|_{\bar{\mathbf k}_B^\perp = \mathbf k_B^\perp} = G\Big|_{\bar{\mathbf k}_B^\perp = \mathbf k_B^\perp,\ \bar{\mathbf k}_A^\perp = \mathbf P^\perp - \mathbf k_B^\perp} .
> $$
>
> Factors of $2\pi$: $(2\pi)^{-2-2+2+2} = 1$.
>
> **Step 4** (the longitudinal $\bar k$ integrals; slide 14). What remains of the barred delta function, with the last two barred measures, is [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]] with $E = P^0$:
>
> $$
> \int\frac{d\bar k_A^z\,d\bar k_B^z}{(2\pi)^2}\;(2\pi)^2\delta\bigl(\bar k_A^z + \bar k_B^z - P^z\bigr)\,\delta\bigl(\bar E_A + \bar E_B - P^0\bigr)\,H = \frac{H}{\bigl|\bar v_A^z - \bar v_B^z\bigr|}\bigg|_{\text{contributing zero}} ,
> $$
>
> $(2\pi)^{-2+2} = 1$. All six $\bar k$ integrals are done, and no factor $2\pi$ is left from them.
>
> **Step 5** (the barred momenta equal the unbarred ones; slide 15). On the support of the integrand three sets of equations hold:
>
> $$
> \text{(i)}\ k_A + k_B = P\ \ \text{(kept }\delta^4\text{)}, \qquad \text{(ii)}\ \bar k_A + \bar k_B = P\ \ \text{(Steps 3–4)}, \qquad \text{(iii)}\ \bar{\mathbf k}_B^\perp = \mathbf k_B^\perp\ \ \text{(Step 3)} .
> $$
>
> (i) and (ii) give $\bar k_A + \bar k_B = k_A + k_B$; its transverse part with (iii) gives $\bar{\mathbf k}_A^\perp = \mathbf k_A^\perp$. Its $z$ and energy parts,
>
> $$
> \bar k_A^z + \bar k_B^z = k_A^z + k_B^z , \qquad \sqrt{\mathbf k_A^{\perp2} + (\bar k_A^z)^2 + m_A^2} + \sqrt{\mathbf k_B^{\perp2} + (\bar k_B^z)^2 + m_B^2} = E_A + E_B ,
> $$
>
> are the two equations that $(k_A^z, k_B^z)$ itself satisfies; their contributing solution is $\bar k_A^z = k_A^z$, $\bar k_B^z = k_B^z$ (the reflected zero is suppressed, ⚑ of [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-1|Derivation §C6b.9.1]]). Hence "simply take $\bar k_A = k_A$, $\bar k_B = k_B$":
>
> $$
> \bar{\mathbf k}_A = \mathbf k_A , \quad \bar{\mathbf k}_B = \mathbf k_B , \quad \bar E_{A,B} = E_{A,B} , \quad \bar v^z_{A,B} = v^z_{A,B} , \quad \bar{\mathcal M} = \mathcal M .
> $$
>
> **Step 6** (collect). At $\bar k = k$,
>
> $$
> \Phi\,\bar\Phi = \frac{\phi_A(\mathbf k_A)\phi_A^\ast(\mathbf k_A)\,\phi_B(\mathbf k_B)\phi_B^\ast(\mathbf k_B)}{\sqrt{2E_A\,2E_B\,2E_A\,2E_B}} = \frac{|\phi_A(\mathbf k_A)|^2|\phi_B(\mathbf k_B)|^2}{2E_A\,2E_B} , \qquad \mathcal M\bar{\mathcal M}^\ast = |\mathcal M(k_A, k_B \to \{p_i\})|^2
> $$
>
> (PS eq. (4.78)), and with Steps 3–4 the cross section is
>
> $$
> d\sigma = d\Phi_f\int\frac{d^3k_A}{(2\pi)^3}\frac{d^3k_B}{(2\pi)^3}\;|\phi_A(\mathbf k_A)|^2|\phi_B(\mathbf k_B)|^2\;F(k_A, k_B) , \qquad F(k_A, k_B) \equiv \frac{|\mathcal M(k_A, k_B \to \{p_i\})|^2}{2E_A\,2E_B\,|v_A^z - v_B^z|}\;(2\pi)^4\delta^4\Bigl(k_A + k_B - \sum_ip_i\Bigr) .
> $$
>
> **Step 7** (smoothness; slide 15). $|\phi_A(\mathbf k_A)|^2$ is smooth and sharply peaked at $\mathbf p_A$, $|\phi_B(\mathbf k_B)|^2$ at $\mathbf p_B$, while $\mathcal M$, the energies and the velocities in $F$ vary slowly on the scale of the packet widths. So "evaluate all other factors at $p_A$, $p_B$ rather than $k_A$, $k_B$" (the scale $K$ of "slowly" and the relative error $O((\Delta k)^2/K^2)$: the paragraph before [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]]):
>
> $$
> \int\frac{d^3k_A}{(2\pi)^3}\frac{d^3k_B}{(2\pi)^3}\;|\phi_A(\mathbf k_A)|^2|\phi_B(\mathbf k_B)|^2\,F(k_A, k_B) \simeq F(p_A, p_B)\int\frac{d^3k_A}{(2\pi)^3}|\phi_A(\mathbf k_A)|^2\int\frac{d^3k_B}{(2\pi)^3}|\phi_B(\mathbf k_B)|^2 .
> $$
>
> ⚑ By-product: the same is done inside the remaining delta function, $\delta^4(k_A + k_B - \sum p_i) \to \delta^4(p_A + p_B - \sum p_i)$; this assumes that the final-state acceptance is smooth on the scale of the packet widths, as for any real detector, which does not resolve the momentum spread of the initial packets (PS p. 106) → statement, assumption (4).
>
> **Step 8** (normalization; slide 15, last bullet). By [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]] each remaining integral is 1, so the right side of Step 7 is $F(p_A, p_B)\cdot1\cdot1$: the integral collapses completely, because of smoothness.
>
> **Step 9** (read off). With beams along $z$, $|v_A^z - v_B^z| = |\mathbf v_A - \mathbf v_B|$ ([[§C6b.9 Evaluating the Cross Section#^der-c6b-9-1|Derivation §C6b.9.1]], Step 5), and
>
> $$
> d\sigma = d\Phi_f\,F(p_A, p_B) = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\,|\mathcal M(p_A, p_B \to \{p_i\})|^2\,\Bigl(\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\Bigr)(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_ip_i\Bigr) :
> $$
>
> $\frac{1}{2E_A2E_B}$ from the packet factors, the Jacobian, $|\mathcal M|^2$, the final-state measure, and the one of the two delta functions that is still there. That is the statement.
>
> **What the derivation shows.**
> - Of the two $\delta^4$ of the squared amplitude, one is used up on the packets (steps 3–4) and the other becomes part of the final phase space: no $\delta^4(0)$ ever appears.
> - The details of the packets drop out entirely; only their normalization and their narrowness were used.
> - The assumptions: narrow packets, smooth $\mathcal M$, forward scattering excluded, a smooth detector acceptance, collinear beams (the *Assumptions* of the statement).

^der-c6b-9-3

*Uses:* [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3|Def. §C6b.8.3]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]], [[§C6b.8 Wave Packets and the Cross Section#^lem-c6b-8-5|Lemma §C6b.8.5]]

The first underbrace of the theorem, "kinematics of the initial particles" (slide 16), has two origins: $\frac{1}{2E_A2E_B}$ from the normalization of the packets (Step 6) and $\frac{1}{|\mathbf v_A - \mathbf v_B|}$ from the Jacobian (Step 4, [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1|Theorem §C6b.9.1]]). The annotated formula of [[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]] labels them separately, (a) and (b), with their box counterparts.

> [!remark] Remark: Reading the formula
> The formula is the longest of the course, not the most important one. The first factor is the kinematics of the initial state, the energies and the velocity difference of what came in; it is the same kinematics that appears in mechanics books, classical or non-relativistic, and has nothing to do with quantum field theory. The last factor, the $n$-particle relativistic phase space ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]), is the kinematics of the final state at fixed total momentum; which features of the final state are measured and which are integrated over is a separate question. The middle factor is the only place the theory enters: given $\mathcal M$, it is the quantity whose square gives the probability, because the initial state is expanded on a complete set of final states, each coefficient is squared, and the squares are summed over all the final states the measurement accepts. From now on the work is to compute $\mathcal M$; the conversion to $d\sigma$ is a formula to look up.
>
> *Source: PHY 513 Lecture 15, slide 16, and transcript · the user's PHY 513 notes, Ch. 15 §15.5 (paragraph "Reading the formula")*

^rem-c6b-9-2

## Identical particles and the sum of probabilities

> [!theorem] Theorem §C6b.9.4: Identical Final Particles: The Resolution of the Identity
> [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]] holds as it stands whether or not the final state contains identical particles. If it contains $n_k$ identical particles of species $k$, integrating it over *all* final momenta counts every physical final state $S_{\rm id} = \prod_kn_k!$ times, and the total cross section is
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\int d\sigma .
> $$
>
> At a given point of phase space (e.g. $d\sigma/d\Omega$ at a given angle) there is no factor. The box route obtains the same factor, for the rate, by counting ordered tuples of lattice momenta ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]): one result, two derivations.
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* as there; every order.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.5 (paragraph "Identical particles (filled in)") · PS §4.5, p. 108 ("divide by $n!$ after integrating over all sets of momenta") · Yu §6.5.1, eqs. (6.305)–(6.306); §6.5.2, eq. (6.321) · PHY 513, Problem Set 10, Problem 1(a3) (the user's solution: the case $n = 2$, Step 2 of the derivation, $\mathbb 1 = \frac{1}{2!}\int d\Pi_3\,d\Pi_4\,|p_3p_4\rangle\langle p_3p_4|$; used in [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^ex-c6c-8-2|Example §C6c.8.2]], Step 4, where one model has identical and distinguishable final particles: [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^thm-c6c-8-5|Theorem §C6c.8.5]])*

^thm-c6b-9-4

> [!derivation]- Derivation
> **Step 1** (the states are symmetric). For identical bosons the creation operators commute ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]]), so for every permutation $\pi \in S_n$
>
> $$
> |\mathbf p_{\pi(1)}\cdots\mathbf p_{\pi(n)}\rangle = \sqrt{2E_{\mathbf p_1}}\cdots\sqrt{2E_{\mathbf p_n}}\;\hat a^\dagger_{\mathbf p_{\pi(1)}}\cdots\hat a^\dagger_{\mathbf p_{\pi(n)}}|0\rangle = |\mathbf p_1\cdots\mathbf p_n\rangle .
> $$
>
> **Step 2** (the resolution of the identity). Take $n$ identical particles, the sector of the Fock space they span, and distinct momenta $\mathbf q_1, \dots, \mathbf q_n$. For $n = 2$, [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]] with the factors $\sqrt{2E}$ (which agree on the support of the deltas) gives
>
> $$
> \langle\mathbf p_1\mathbf p_2|\mathbf q_1\mathbf q_2\rangle = 2E_{\mathbf q_1}2E_{\mathbf q_2}(2\pi)^6\bigl[\delta^3(\mathbf p_1 - \mathbf q_1)\delta^3(\mathbf p_2 - \mathbf q_2) + \delta^3(\mathbf p_1 - \mathbf q_2)\delta^3(\mathbf p_2 - \mathbf q_1)\bigr] ,
> $$
>
> so, each delta doing one integral and $|\mathbf q_2\mathbf q_1\rangle = |\mathbf q_1\mathbf q_2\rangle$ by Step 1,
>
> $$
> \int\frac{d^3p_1}{(2\pi)^32E_{\mathbf p_1}}\frac{d^3p_2}{(2\pi)^32E_{\mathbf p_2}}\;|\mathbf p_1\mathbf p_2\rangle\langle\mathbf p_1\mathbf p_2|\mathbf q_1\mathbf q_2\rangle = |\mathbf q_1\mathbf q_2\rangle + |\mathbf q_2\mathbf q_1\rangle = 2\,|\mathbf q_1\mathbf q_2\rangle .
> $$
>
> For general $n$ the commutation relations give $\langle\mathbf p_1\cdots\mathbf p_n|\mathbf q_1\cdots\mathbf q_n\rangle = \sum_{\pi\in S_n}\prod_j2E_{\mathbf q_{\pi(j)}}(2\pi)^3\delta^3(\mathbf p_j - \mathbf q_{\pi(j)})$, one term per way of matching the $\mathbf p$'s to the $\mathbf q$'s, $n!$ terms. So
>
> $$
> \int\prod_j\frac{d^3p_j}{(2\pi)^32E_{\mathbf p_j}}\;|\mathbf p_1\cdots\mathbf p_n\rangle\langle\mathbf p_1\cdots\mathbf p_n|\mathbf q_1\cdots\mathbf q_n\rangle = \sum_{\pi\in S_n}|\mathbf q_{\pi(1)}\cdots\mathbf q_{\pi(n)}\rangle = n!\,|\mathbf q_1\cdots\mathbf q_n\rangle ,
> $$
>
> each delta function doing one integral and, by step 1, every permuted state equal to $|\mathbf q_1\cdots\mathbf q_n\rangle$. The identity on the sector is therefore $\frac{1}{n!}\int\prod_j\frac{d^3p_j}{(2\pi)^32E_{\mathbf p_j}}|\mathbf p_1\cdots\rangle\langle\mathbf p_1\cdots|$ (coincident momenta have measure zero).
>
> **Step 3** (the total probability). For the scattered state $|\psi\rangle$, the probability of ending in this sector is, with $\mathbb 1_n$ of Step 2 and $\mathcal P$ of [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]],
>
> $$
> \langle\psi|\mathbb 1_n|\psi\rangle = \frac{1}{n!}\int\prod_j\frac{d^3p_j}{(2\pi)^32E_{\mathbf p_j}}\;\bigl|\langle\mathbf p_1\cdots\mathbf p_n|\psi\rangle\bigr|^2 = \frac{1}{n!}\int\mathcal P .
> $$
>
> For several species the identity on the sector is the product of the factors, $\prod_k\frac{1}{n_k!} = \frac{1}{S_{\rm id}}$. The integrated cross section inherits the factor through [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]: $\sigma = \frac{1}{S_{\rm id}}\int d\sigma$.
>
> **Step 4** (no factor locally). In a small region $R$ of phase space around distinct momenta, the permuted region $\pi R$ ($\pi \ne \mathrm{id}$) is disjoint from $R$, so no two points of $R$ describe the same state (Step 1), and $d\sigma$ there is the probability per unit flux without correction.
>
> **What the derivation shows.**
> - The factor comes from counting final *states*, not from the amplitude: the amplitude for identical particles is computed separately and is already symmetric.
> - For two identical particles at $2 \to 2$ in the centre-of-mass frame, $\mathbf p_2 = -\mathbf p_1$, and the unit vector $\hat{\mathbf n}(\theta, \varphi) = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ satisfies $-\hat{\mathbf n}(\theta, \varphi) = \hat{\mathbf n}(\pi - \theta, \varphi + \pi)$; so $|\mathbf p\,\hat{\mathbf n}, -\mathbf p\,\hat{\mathbf n}\rangle = |-\mathbf p\,\hat{\mathbf n}, \mathbf p\,\hat{\mathbf n}\rangle$ (Step 1): the directions $(\theta, \varphi)$ and $(\pi - \theta, \varphi + \pi)$ of $\mathbf p_1$ are the same state, integrating over the full sphere counts it twice, and $S_{\rm id} = 2$ → [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-6|Theorem §C6b.4.6]].

^der-c6b-9-4

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-7|P7, step 7]]

> [!theorem] Theorem §C6b.9.5: The Scattering Probabilities Add Up to One
> Let $|\psi\rangle$ be a normalized state and assume the out states are complete. Summing over the particle contents of the final state, with $S_{\rm id}$ of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]] for each content,
>
> $$
> \sum_{\text{contents}}\frac{1}{S_{\rm id}}\int\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i}\;\bigl|{}_{\rm out}\langle\mathbf p_1\mathbf p_2\cdots|\psi\rangle\bigr|^2 = \langle\psi|\psi\rangle = 1 .
> $$
>
> For the two-packet state of [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3|Def. §C6b.8.3]] with profiles peaked at $\mathbf p_A \ne \mathbf p_B$ (or $A \ne B$), $\langle\phi_A\phi_B|\phi_A\phi_B\rangle = 1$ for every $\mathbf b$, so the $\mathcal P(\mathbf b)$ of [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]], integrated over all final momenta and summed over contents with $\frac{1}{S_{\rm id}}$, is 1.
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* exact, given complete out states of the full $\hat H$ (unitarity).
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.3 (after eq. (Pb): "the completeness relation for relativistically normalized states") · PS §4.5, p. 103 · the identical-particle factor: PS p. 108, Yu §6.5.1, eq. (6.305)*

^thm-c6b-9-5

> [!derivation]- Derivation
> **Step 1** (completeness by sectors). The out states of different particle contents are orthogonal, and in the sector of a content with $S_{\rm id} = \prod_kn_k!$ the identity is ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], 3, for one particle; [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-4|Derivation §C6b.9.4]], Step 2, for $n$ identical ones)
>
> $$
> \mathbb 1_{\rm content} = \frac{1}{S_{\rm id}}\int\prod_i\frac{d^3p_i}{(2\pi)^3\,2E_i}\;|\mathbf p_1\mathbf p_2\cdots\rangle_{\rm out}\,{}_{\rm out}\langle\mathbf p_1\mathbf p_2\cdots| , \qquad \mathbb 1 = \sum_{\text{contents}}\mathbb 1_{\rm content} .
> $$
>
> **Step 2** (sandwich). $\langle\psi|\mathbb 1|\psi\rangle = \sum\langle\psi|\mathbb 1_{\rm content}|\psi\rangle$, and each term is
>
> $$
> \langle\psi|\mathbb 1_{\rm content}|\psi\rangle = \frac{1}{S_{\rm id}}\int\prod_i\frac{d^3p_i}{(2\pi)^3\,2E_i}\;\langle\psi|\mathbf p_1\cdots\rangle_{\rm out}\,{}_{\rm out}\langle\mathbf p_1\cdots|\psi\rangle = \frac{1}{S_{\rm id}}\int\prod_i\frac{d^3p_i}{(2\pi)^3\,2E_i}\;\bigl|{}_{\rm out}\langle\mathbf p_1\cdots|\psi\rangle\bigr|^2 .
> $$
>
> **Step 3** (the two-packet norm). With $\Phi(\mathbf k_A, \mathbf k_B) = e^{-i\mathbf b\cdot\mathbf k_B}\frac{\phi_A(\mathbf k_A)\phi_B(\mathbf k_B)}{\sqrt{2E_A2E_B}}$ and the two-particle overlap of [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]] (factors $\sqrt{2E}$ of [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]),
>
> $$
> \begin{aligned}
> \langle\phi_A\phi_B|\phi_A\phi_B\rangle ={}& \int\frac{d^3k_A\,d^3k_B\,d^3k_A'\,d^3k_B'}{(2\pi)^{12}}\;\Phi^\ast(\mathbf k_A, \mathbf k_B)\,\Phi(\mathbf k_A', \mathbf k_B')\;2E_A2E_B(2\pi)^6\bigl[\delta^3(\mathbf k_A - \mathbf k_A')\delta^3(\mathbf k_B - \mathbf k_B') + \delta^3(\mathbf k_A - \mathbf k_B')\delta^3(\mathbf k_B - \mathbf k_A')\bigr]\\
> ={}& \int\frac{d^3k_A}{(2\pi)^3}|\phi_A(\mathbf k_A)|^2\int\frac{d^3k_B}{(2\pi)^3}|\phi_B(\mathbf k_B)|^2 + \Bigl|\int\frac{d^3k}{(2\pi)^3}\,e^{-i\mathbf b\cdot\mathbf k}\phi_A^\ast(\mathbf k)\phi_B(\mathbf k)\Bigr|^2 = 1\cdot1 + 0 ,
> \end{aligned}
> $$
>
> the exchange term (present only for $A = B$) vanishing because $\phi_A$ and $\phi_B$ are peaked at different momenta and do not overlap. The phase $e^{-i\mathbf b\cdot\mathbf k_B}$ has modulus 1 in the direct term, so the norm is 1 for every $\mathbf b$.
>
> **Step 4** (read off). With $|\psi\rangle = |\phi_A\phi_B\rangle_{\rm in}$, Steps 2–3 and [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]]: $\sum\frac{1}{S_{\rm id}}\int\mathcal P(\mathbf b) = 1$.
>
> **What the derivation shows.**
> - $\frac{d^3p}{(2\pi)^32E}$ is the measure that makes $\mathcal P$ a probability density; $\frac{1}{S_{\rm id}}$ is needed so that identical final particles are not counted $S_{\rm id}$ times.
> - The assumption is asymptotic completeness: every state is a superposition of out states.

^der-c6b-9-5

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-5|Theorem §C2a.4.5]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3|Def. §C6b.8.3]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-4|Def. §C6b.8.4]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-4|Theorem §C6b.9.4]]

> [!caution] Caution: Names for the identical-particle factor
> These notes write $S_{\rm id} = \prod_kn_k!$, to keep it apart from the $S$-matrix, the symmetry factor and the bilinear ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^cau-c6b-1-2|§C6b.1, Caution: Four S's]]). The user's notes write $S$; Yu writes $\mathcal S$, 末态对称性因子, and puts it into the total rate (eqs. (6.305)–(6.306)) and $\sigma = \frac{1}{\mathcal S}\int d\sigma$ (eq. (6.321)); PS give the rule in words (p. 108). Yu also writes $\mathcal S = 2$ in §7.3 (eq. (7.123)), next to the diagram symmetry factor (eq. (7.124)).
>
> *Source: Yu §6.5.1–§6.5.2, eqs. (6.305)–(6.306), (6.321); §7.3, eqs. (7.123)–(7.124) · PS §4.5, p. 108 · the user's PHY 513 notes, Ch. 15 §15.5*

^cau-c6b-9-3

## Lorentz invariance of the cross section

The cross section of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]] has three factors. $|\mathcal M|^2$ is Lorentz invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]]) and so is the final phase space, but the prefactor $E_AE_B|\mathbf v_A - \mathbf v_B|$ looks far from relativistically invariant, and $\sigma$ is an area, not a scalar. Part C of the lecture resolves the puzzle with a trick, to "undo the velocities": the flux factor is one component of an antisymmetric tensor, invariant under boosts along the beam and rotating like an area ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]]). It then makes the phase space explicit in the simplest case, two particles in the centre-of-mass frame ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]), and obtains the $2 \to 2$ differential cross section ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]]), which for equal masses is $|\mathcal M|^2/(64\pi^2E_{\rm cm}^2)$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-9|Theorem §C6b.4.9]]). Yu reaches the frame independence differently, with the Møller velocity, which is invariant by construction and equals $|\mathbf v_A - \mathbf v_B|$ for collinear beams: that is the main line of these notes, [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]], [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]] (§6.5.2, eqs. (6.314)–(6.331)). His two-body kinematics with the Källén function (§6.5.3, eqs. (6.336)–(6.366)) is [[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]]; the equation numbers are collected in [[§C6b.9 Evaluating the Cross Section#^rem-c6b-9-4|Remark: Yu's route to frame independence]], at the end.

Why an $\varepsilon$-tensor: the cross section is an area in the plane transverse to the beam, the plane of the impact parameter $d^2b$ ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]), and the Lorentz-covariant object attached to an oriented plane is an antisymmetric tensor. The component $F_{12} = \varepsilon_{12\mu\nu}p_A^\mu p_B^\nu$ is the one dual to the transverse area element $dx\wedge dy$ ([[§C6b.9 Evaluating the Cross Section#^der-c6b-9-7|Derivation §C6b.9.7]], Step 3): it is built from the two momenta alone, and it is unchanged by boosts along $z$, exactly as an area in the $xy$-plane is. "Undo the velocities" means writing $E_AE_Bv^z$ as $E_Bp_A^z$, after which the antisymmetric combination is visible.

> [!theorem] Theorem §C6b.9.6: The Flux Factor Is a Component of an Antisymmetric Tensor
> For momenta $p_A$, $p_B$ along the $z$-axis,
>
> $$
> E_AE_B\bigl(v_A^z - v_B^z\bigr) = E_Bp_A^z - E_Ap_B^z = \varepsilon_{xy\mu\nu}\,p_A^\mu p_B^\nu ,
> $$
>
> the $xy$ component of the antisymmetric tensor $F_{\rho\sigma} = \varepsilon_{\rho\sigma\mu\nu}p_A^\mu p_B^\nu$.
>
> *Model:* any (kinematics); *applies:* momenta along the $z$-axis, any masses; independent of the dynamics.
>
> *Source: PHY 513 Lecture 15, slide 19 ("$E_AE_B(v_A^z - v_B^z) = E_Bp_A^z - E_Ap_B^z = \epsilon_{xy\mu\nu}p_A^\mu p_B^\nu$ ⇒ prefactor transforms like an area"), and transcript ("as we just learned, momentum divided by $E$ gives velocity. That works the other way around as well") · the user's PHY 513 notes, Ch. 15 §15.6, eq. (fluxeps) · PS §4.5, p. 106 (with $|\epsilon_{\mu xy\nu}p_A^\mu p_B^\nu|$)*

^thm-c6b-9-6

> [!derivation]- Derivation
> **Step 1** (undo the velocities). $v^z = p^z/E$ ([[§C6b.9 Evaluating the Cross Section#^der-c6b-9-1|Derivation §C6b.9.1]], Step 5), so
>
> $$
> E_AE_B\bigl(v_A^z - v_B^z\bigr) = E_AE_B\frac{p_A^z}{E_A} - E_AE_B\frac{p_B^z}{E_B} = E_Bp_A^z - E_Ap_B^z .
> $$
>
> **Step 2** (which components survive). $\varepsilon_{12\mu\nu}$ vanishes when an index repeats, so $\mu, \nu \in \{0, 3\}$ with $\mu \ne \nu$. Of the 16 terms of the double sum only two remain:
>
> $$
> \varepsilon_{12\mu\nu}p_A^\mu p_B^\nu = \sum_{\mu,\nu=0}^3\varepsilon_{12\mu\nu}p_A^\mu p_B^\nu = \varepsilon_{1203}\,p_A^0p_B^3 + \varepsilon_{1230}\,p_A^3p_B^0 .
> $$
>
> **Step 3** (the signs). Count transpositions from $(0, 1, 2, 3)$:
>
> $$
> (0, 1, 2, 3) \to (1, 0, 2, 3) \to (1, 2, 0, 3) \to (1, 2, 3, 0) ,
> $$
>
> so $(1, 2, 0, 3)$ is two transpositions away (even) and $(1, 2, 3, 0)$ three (odd): $\varepsilon_{1203} = +\varepsilon_{0123} = -1$, $\varepsilon_{1230} = -\varepsilon_{0123} = +1$.
>
> **Step 4** (assemble). With $p^0 = E$, $p^3 = p^z$:
>
> $$
> \varepsilon_{12\mu\nu}p_A^\mu p_B^\nu = \varepsilon_{1203}\,E_A\,p_B^z + \varepsilon_{1230}\,p_A^z\,E_B = -E_Ap_B^z + E_Bp_A^z ,
> $$
>
> which is step 1.
>
> **What the derivation shows.**
> - With PS's $\varepsilon^{0123} = -1$ the middle expression changes sign; inside the absolute value of the flux factor it does not matter.
> - For collinear beams $F_{12}^2 = \frac12F_{\rho\sigma}F^{\rho\sigma} = (p_A\cdot p_B)^2 - m_A^2m_B^2$, by the contraction identity $\varepsilon_{\rho\sigma\mu\nu}\varepsilon^{\rho\sigma\alpha\beta} = -2(\delta^\alpha_\mu\delta^\beta_\nu - \delta^\alpha_\nu\delta^\beta_\mu)$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]) and because the other components of $F$ vanish: $|F_{12}|$ is the invariant form of the flux factor found algebraically in the box route ([[§C6b.3 The Cross Section#^thm-c6b-3-7|Corollary §C6b.3.7]]).
> - Checked numerically at random collinear momenta.

^der-c6b-9-6

*Uses:* [[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]] (the bullet on $F_{12}^2$)

> [!theorem] Theorem §C6b.9.7: The Cross Section Transforms Like an Area
> 1. $E_AE_B|\mathbf v_A - \mathbf v_B|$, and hence $d\sigma$ of [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]], is invariant under boosts along the beam axis $z$.
> 2. Under rotations the flux factor transforms like an area element in the plane transverse to the beam, as $\sigma$ does: $F'_{ij} = R_i{}^kR_j{}^lF_{kl}$, the law of $dx^i\wedge dx^j$, and $\sigma$ is an area in the plane of $d^2b$ ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]). Under a boost along $z$ both are unchanged (part 1).
> 3. In particular $d\sigma$ is the same in the centre-of-mass frame ($\mathbf p_{\rm tot} = \mathbf 0$) and in a target frame ($\mathbf p_A = \mathbf 0$ or $\mathbf p_B = \mathbf 0$).
>
> Neither the flux factor nor the cross section is a Lorentz scalar; they transform alike, which is all that is needed.
>
> *Model:* [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]]; *applies:* as there, with $|\mathcal M|^2$ Lorentz invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]]).
>
> *Source: PHY 513 Lecture 15, slide 19 ("Cross-section $\sigma$ really is an 'area', it transforms like one. Application: $d\sigma$ invariant under boosts in $z$-direction. Same in c.m.s. ($\vec p_{\rm tot} = 0$) and target frame ($\vec p_A = 0$ or $\vec p_B = 0$)."), and transcript ("it's not even exactly invariant. It should transform like an area, and it does") · the user's PHY 513 notes, Ch. 15 §15.6, Principle "Same cross section in the CM and target frames" (a derived result: a theorem here) · PS §4.5, p. 106*

^thm-c6b-9-7

> [!derivation]- Derivation
> **Step 1** (a boost along $z$). Such a boost acts only on the components $0$, $3$, as the matrix of [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]], and leaves $x$, $y$ alone. With $c = \cosh\eta$, $s = \sinh\eta$, each momentum becomes
>
> $$
> E' = c\,E + s\,p^z , \qquad p'^z = s\,E + c\,p^z , \qquad \mathbf p'^\perp = \mathbf p^\perp .
> $$
>
> **Step 2** (the component $F_{12}$ is invariant). By [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|Theorem §C6b.9.6]], $F_{12} = E_Bp_A^z - E_Ap_B^z$. Insert Step 1 and expand all eight products:
>
> $$
> \begin{aligned}
> F'_{12} = E'_Bp'^z_A - E'_Ap'^z_B ={}& (cE_B + s\,p_B^z)(sE_A + c\,p_A^z) - (cE_A + s\,p_A^z)(sE_B + c\,p_B^z)\\
> ={}& cs\,E_BE_A + c^2E_Bp_A^z + s^2p_B^zE_A + sc\,p_B^zp_A^z - cs\,E_AE_B - c^2E_Ap_B^z - s^2p_A^zE_B - sc\,p_A^zp_B^z\\
> ={}& (c^2 - s^2)\bigl(E_Bp_A^z - E_Ap_B^z\bigr) = F_{12} ,
> \end{aligned}
> $$
>
> since $\cosh^2\eta - \sinh^2\eta = 1$. In index form this is the determinant rule: restricted to $\mu, \nu \in \{0, 3\}$, $\varepsilon_{12\mu\nu} = -\epsilon_{\mu\nu}$ with the two-dimensional symbol $\epsilon_{03} = 1$ (Step 3 of [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-6|Derivation §C6b.9.6]]), and $\epsilon_{\mu\nu}L^\mu{}_\alpha L^\nu{}_\beta = \det L\,\epsilon_{\alpha\beta}$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]] in two dimensions) with $\det L = c^2 - s^2 = 1$. For collinear beams $|\mathbf v_A - \mathbf v_B| = |v_A^z - v_B^z|$, so $E_AE_B|\mathbf v_A - \mathbf v_B| = |F_{12}|$ is invariant; $|\mathcal M|^2$ and the phase space are invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]], [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]]): part 1.
>
> **Step 3** (rotations). $F_{\rho\sigma} = \varepsilon_{\rho\sigma\mu\nu}p_A^\mu p_B^\nu$ is an antisymmetric tensor; under a rotation $R$ its spatial components transform as
>
> $$
> F'_{ij} = R_i{}^kR_j{}^l\,F_{kl} , \qquad F_{12} = \tfrac12\,\varepsilon_{3jk}F_{jk} ,
> $$
>
> like the components of an area element $dx^i\wedge dx^j$, equivalently like the $z$ component of the axial vector $\frac12\varepsilon_{ijk}F_{jk}$, the normal to the plane. The flux factor is the component $F_{12}$, the area element in the plane transverse to the beam: part 2. The cross section is defined as an area in that plane ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5|Def. §C6b.8.5]]: an integral over $d^2b$).
>
> **Step 4** (frames). The centre-of-mass frame and the rest frames of $A$ or of $B$ are reached from one another by boosts along the common beam axis: with $\tanh\eta = v$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]]), $\cosh\eta = \gamma$, $\sinh\eta = \gamma v$ in Step 1 gives $p'^z = \gamma(vE + p^z)$, so the boost with $v = -\frac{p_A^z + p_B^z}{E_A + E_B}$ takes the total momentum to zero and the one with $v = -v_A^z$ takes $A$ to rest. Part 1 applies to each: part 3.
>
> **What the derivation shows.**
> - The flux factor is not a Lorentz scalar; the cross section is not either; they transform alike, which is all that is needed.
> - The same trick, a component transverse to a boost is invariant under it, gave the centre-of-mass momentum in Problem Set 1 — [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|Example §C1a.5.2]].

^der-c6b-9-7

*Uses:* [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|Theorem §C6b.9.6]], [[§C1a.4 The Lorentz Group#^def-c1a-4-3|Def. §C1a.4.3]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-5|Theorem §C1a.5.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]], [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]]

## Yu's route

> [!remark] Remark: Yu's route
> Yu derives the same formula without wave packets (§6.5.1–§6.5.2); in these notes that derivation is the main line, [[§C6b.2 Transition Probabilities in a Box|§C6b.2]]–[[§C6b.3 The Cross Section|§C6b.3]], box by box: the transition probability $P_{fi} = |T_{fi}|^2/(\langle i|i\rangle\langle f|f\rangle)$ ([[§C6b.2 Transition Probabilities in a Box#^def-c6b-2-1|Def. §C6b.2.1]]; eq. (6.276)); the squared delta function $[(2\pi)^4\delta^4(p_i - p_f)]^2 = \tilde V\tilde T\,(2\pi)^4\delta^4(p_i - p_f)$ with $(2\pi)^4\delta^4(0) = \int d^4x = \tilde V\tilde T$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3|Theorem §C6b.2.3]]; eqs. (6.277)–(6.283); the box in spacetime is [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-10|Theorem §CA.4.10]]); the norms $\langle i|i\rangle = 4E_AE_B\tilde V^2$, $\langle f|f\rangle = \prod_j2E_j\tilde V$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4|Theorem §C6b.2.4]]; eqs. (6.284)–(6.290)); the rate per unit time ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5|Theorem §C6b.2.5]]; eq. (6.292)); the count $\sum \to \tilde V\int\frac{d^3p}{(2\pi)^3}$ of final states ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6|Theorem §C6b.2.6]]; eqs. (6.295)–(6.302)); the total rate with $\frac{1}{S_{\rm id}}$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7|Theorem §C6b.2.7]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]; eqs. (6.303)–(6.306)); and, for a beam of density $n_B$ on a target of density $n_A$, both per unit volume ([[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]], [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]]), the rate per unit volume $\mathcal R = n_An_B\sigma|\mathbf v_B|$ ([[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]]) with $n_A = n_B = 1/\tilde V$, so $\sigma = \mathcal R/(n_An_B|\mathbf v_B|)$ ([[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]]; eqs. (6.307)–(6.313)): all powers of $\tilde V$ and $\tilde T$ cancel. The route is shorter; the wave packets show why the $\delta(0)$'s are harmless (no $\delta^4(0)$ appears at all, [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3|Derivation §C6b.9.3]]). Yu's units, $1\,\mathrm b = 10^{-28}\,\mathrm m^2 = 2.568\times10^3\,\mathrm{GeV}^{-2}$, $1\,\mathrm{GeV}^{-2} = 0.3894\,\mathrm{mb}$ (eqs. (6.309)–(6.311)), are in [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]].
>
> *Source: Yu §6.5.1–§6.5.2, pp. 239–243, eqs. (6.276)–(6.313)*

^rem-c6b-9-3

> [!remark] Remark: Yu's route to frame independence
> In these notes Yu's route to the invariant cross section is the main line, [[§C6b.3 The Cross Section|§C6b.3]] ([[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]]–[[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]]). Yu writes the cross section first for a fixed target and then replaces $|\mathbf v_{\mathcal B}|$ by the **Møller velocity** $v_{\rm Møl} = \frac{1}{E_{\mathcal A}E_{\mathcal B}}\sqrt{(p_{\mathcal A}\cdot p_{\mathcal B})^2 - m_{\mathcal A}^2m_{\mathcal B}^2}$ (eq. (6.315)), which makes the incident flux $E_{\mathcal A}E_{\mathcal B}v_{\rm Møl}$ and $\sigma$ Lorentz invariant *by definition* (eq. (6.316)); $d\Pi_n$ is eq. (6.318), $d\sigma$ eq. (6.320). He shows $v_{\rm Møl} = \sqrt{|\mathbf v_{\mathcal A} - \mathbf v_{\mathcal B}|^2 - |\mathbf v_{\mathcal A}\times\mathbf v_{\mathcal B}|^2}$ (eqs. (6.322)–(6.329)), so for collinear beams the two definitions agree ([[§C6b.3 The Cross Section#^thm-c6b-3-7|Corollary §C6b.3.7]]); the course instead derives the transformation law of the flux factor (an area). His $2 \to 2$ kinematics in the centre-of-mass frame: eqs. (6.336)–(6.345) (two-body phase space (6.341)–(6.343), $d\sigma/d\Omega$ (6.345)), the Källén function (6.351) with $d\sigma/d\Omega$ in terms of it (6.353), special cases (6.356)–(6.366), all four masses equal (6.366).
>
> *Source: Yu §6.5.2–§6.5.3, pp. 244–250, eqs. (6.314)–(6.366)*

^rem-c6b-9-4

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]] — δ of a function: part 1 (linear argument, Jacobian 1) does the $\bar k_B^z$ integral; part 2, $\delta(f(x)) = \sum_{x_0}\delta(x - x_0)/|f'(x_0)|$ over the simple zeros, turns the energy delta function into $1/|\bar v_A^z - \bar v_B^z|$, the only Jacobian of the computation (Derivation §C6b.9.1, Steps 1 and 4; Caution: 1/f′(0) on slide 14).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-3|Theorem §CA.4.3]] — plane waves integrate to a delta function, here in two dimensions: $\int d^2b\,e^{-i\mathbf b\cdot(\mathbf k_B - \bar{\mathbf k}_B)} = (2\pi)^2\delta^2(\mathbf k_B^\perp - \bar{\mathbf k}_B^\perp)$ (Derivation §C6b.9.3, Step 1).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-7|Theorem §CA.4.7]] — the order of the fourteen integrals may be exchanged, every delta function being used against smooth, rapidly decreasing packets (Derivation §C6b.9.3, opening).
> - [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-10|Theorem §CA.4.10]] — the box in space and time, $(2\pi)^4\delta^4(0) = \tilde V\tilde T$, of the route this section is compared with (opening; Remark: Yu's route); no $\delta^4(0)$ occurs in the wave-packet route.

> [!remark]- Connections
> - Yu's box regularization $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ is the four-dimensional version of $(2\pi)^3\delta^3(0) = V$, the same factor that made the zero-point energy and the vacuum bubbles proportional to volumes — [[§CA.3 Products of Distributions and Operator-Valued Distributions#^thm-ca-3-3|Theorem §CA.3.3]], [[§CA.4 Fourier Transforms and Fourier Tricks#^thm-ca-4-10|Theorem §CA.4.10]], [[§C6a.12 The iε Limit and Vacuum Bubbles#^thm-c6a-12-3|Theorem §C6a.12.3]].
> - The Jacobian $1/|f'|$ of a delta function of a function is the same one that turns $\delta(p^2 - m^2)$ into $\delta(p^0 - E_{\mathbf p})/2E_{\mathbf p}$ in the invariant measure — [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]].
> - With a fixed classical target in place of the particle $A$ the same derivation has one packet, one energy delta function and one velocity: $d\sigma = \frac{1}{v_i}\frac{1}{2E_i}\frac{d^3p_f}{(2\pi)^32E_f}|\mathcal M|^2\,2\pi\delta(E_f - E_i)$ (PHY 513, Problem Set 10, Problem 2(b)) — [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^thm-c6b-10-4|Theorem §C6b.10.4]], with the reflected root in its one-particle form, [[§C6b.10 Scattering off a Fixed Target꞉ the Cross Section in an External Potential#^lem-c6b-10-3|Lemma §C6b.10.3]].
> - The identical-particle $1/n!$ is the Fock-space counting of symmetric states — [[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]].
> - "A component transverse to a boost is invariant under that boost": the same observation gave the centre-of-mass momentum from one tensor component in two frames — [[§C1a.5 Vectors, Tensors and Index Notation#^ex-c1a-5-2|Example §C1a.5.2]].
> - The flux factor $F_{12}$ is the dual, in the transverse plane, of the antisymmetric tensor built from the two momenta, as $\mathbf B$ is the dual of $F_{ij}$ in electrodynamics — [[§C1a.8 Relativistic Electrodynamics in Index Form|§C1a.8]].
> - The box route reaches the same $d\sigma$ with $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ and the Møller velocity, which is invariant by construction; for collinear beams it is the velocity difference whose transformation law [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|Theorem §C6b.9.6]]–[[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]] derive — [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]].
