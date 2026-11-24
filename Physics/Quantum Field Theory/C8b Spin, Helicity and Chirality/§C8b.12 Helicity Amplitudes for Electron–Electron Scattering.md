---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.12
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8b.11 Helicity Amplitudes in Yukawa Theory|§C8b.11]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C9.1 Discrete Lorentz Transformations|§C9.1]] →

*Sources: PHY 513, Problem Set 11 ("Processes with Fermions and Helicity", due 22 Nov 2026), Problem 2 "Helicity Amplitudes for Electron-Electron scattering": statement, and the user's solution (submitted; used as written) · PHY 513, Problem Set 5, Problem 3 (the Gordon identity; the user's solution) · PHY 513 Lecture 18 (the QED rules) and Lecture 20 (helicity conservation at the vertex), as cited in the homes linked below.*

Which helicity amplitudes of electron–electron scattering are large, and where? With a photon in place of the scalar of [[§C8b.11 Helicity Amplitudes in Yukawa Theory|§C8b.11]] the two diagrams are the same, but each vertex now carries a $\gamma^\mu$ and keeps the helicity instead of flipping it. This section follows Problem Set 11, Problem 2, as the user solved it: the amplitude of $e^-e^- \to e^-e^-$ with its relative sign ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]]); the vector vertex at equal momenta, $\bar u_{\lambda'}(p)\gamma^\mu u_\lambda(p) = 2p^\mu\delta_{\lambda\lambda'}$, from the Gordon identity ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]]); and with it the amplitudes that dominate near the forward direction ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|Theorem §C8b.12.3]]) and near the backward direction ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-4|Theorem §C8b.12.4]]).

**The mathematical picture.** Each vertex contributes a four-vector, the current $\bar u_{\lambda'}(p')\gamma^\mu u_\lambda(p)$ between two helicity spinors, and each diagram is the Minkowski product of two such currents divided by the square of the photon momentum (compare [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]], where the currents of $e^+e^- \to \mu^+\mu^-$ are polarization-like vectors). At equal momenta the current of a spin-$\frac12$ particle is $2p^\mu$ times the unit matrix in the helicity labels: its direction is that of the momentum, and it is diagonal in helicity. Near the direction in which a propagator has its pole the currents of that diagram are close to this form, so the dominant amplitudes are diagonal in the helicities along the lines of that diagram.

**Setup.** QED ([[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]) at order $e^2$, tree approximation, by the rules of [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]] in Feynman gauge: elastic scattering of two electrons, $e^-(p, \lambda)\,e^-(k, \mu) \to e^-(p', \lambda')\,e^-(k', \mu')$, free relativistic states over $|0\rangle$. The identity of [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]] is exact for every mass $m > 0$. The statements on the forward and backward directions are in the centre-of-mass frame, for $\theta \to 0$ with $\theta \ne 0$ and $\theta \to \pi$ with $\theta \ne \pi$.

*Conventions* ([[Larsen PHY 513]]): helicity amplitudes $\mathcal M_{\lambda'\mu';\lambda\mu}$ as in [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^def-c8b-11-1|Def. §C8b.11.1]]; $u_\lambda(p)$ is the helicity spinor $u_\pm(p)$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]] for $\lambda = R, L$; $m$ is the electron mass; $q = p' - p$ in the Gordon identity; $\sigma^{\mu\nu} = \frac i2[\gamma^\mu, \gamma^\nu]$. The index $\mu$ of $\gamma^\mu$ and the helicity $\mu$ of the electron $k$ are told apart by their position, as in the problem set.

## The amplitude

> [!theorem] Theorem §C8b.12.1: The Amplitude of e⁻e⁻ → e⁻e⁻ at Order e²
> ![[ph-qft-c8b-12-1.svg]]
> *The two diagrams of $e^-(p, \lambda)\,e^-(k, \mu) \to e^-(p', \lambda')\,e^-(k', \mu')$ at order $e^2$, time running to the right, after the user's drawing (Problem Set 11, Problem 2(a)).*
>
> With $|pk\rangle = \hat a^\dagger_p\hat a^\dagger_k|0\rangle$ and $\langle p'k'| = \langle0|\,\hat a_{p'}\hat a_{k'}$,
>
> $$
> i\mathcal M_{\lambda'\mu';\lambda\mu} = ie^2\biggl[-\frac{\bar u_{\lambda'}(p')\gamma^\mu u_\lambda(p)\;\bar u_{\mu'}(k')\gamma_\mu u_\mu(k)}{(p - p')^2 + i\varepsilon} + \frac{\bar u_{\mu'}(k')\gamma^\mu u_\lambda(p)\;\bar u_{\lambda'}(p')\gamma_\mu u_\mu(k)}{(p - k')^2 + i\varepsilon}\biggr] .
> $$
>
> 1. The first term is the $t$-channel diagram ($p \to p'$, $k \to k'$, photon momentum $q = p - p'$), the second the $u$-channel diagram ($p \to k'$, $k \to p'$, $q = p - k'$).
> 2. **The two diagrams enter with a relative minus sign**: the electron fields are contracted exactly as the fermion fields of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|Theorem §C8b.11.6]], and the photon field commutes with the fermionic operators.
> 3. The amplitude changes sign when the two final electrons are exchanged together with their helicities, $(p', \lambda') \leftrightarrow (k', \mu')$: the exchange maps each term onto minus the other.
>
> *Equivalently,* this is the Yukawa amplitude of [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] with the vertex $-ig \to -ie\gamma^\mu$ and the scalar propagator replaced by $\frac{-ig_{\mu\nu}}{q^2 + i\varepsilon}$; item 3 is [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]], which holds in QED alike.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, Feynman gauge, any helicities, any mass; the overall sign for the bra stated ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^cau-c8b-12-1|Caution: The overall sign of the electron–electron amplitude]]).
>
> *Source: PHY 513, Problem Set 11, Problem 2(a) (statement: "Draw the two Feynman diagrams … Write the corresponding transition amplitudes. Justify your choice of relative sign between the two terms"; the user's solution) · the rules: [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]] · item 3 and the formula checked numerically with massive helicity spinors (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-12-1

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 2(a).
>
> **Step 1** (the diagrams). At order $e^2$ the scattering $e^-(p, \lambda)\,e^-(k, \mu) \to e^-(p', \lambda')\,e^-(k', \mu')$ has two diagrams, those of the figure.
>
> **Step 2** (the rules). The interaction is $\mathcal H_I = e\,\bar\psi\gamma^\mu\psi A_\mu$, with vertex factor $-ie\gamma^\mu$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]) and, in Feynman gauge, photon propagator $\dfrac{-ig_{\mu\nu}}{q^2 + i\varepsilon}$ ([[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|Theorem §C8a.3.5]]).
>
> **Step 3** (the contractions and the relative sign). In terms of contractions in $\langle p'k'|\,(\hat{\bar\psi}\gamma^\mu\hat\psi\hat A_\mu)(z_1)\,(\hat{\bar\psi}\gamma^\nu\hat\psi\hat A_\nu)(z_2)\,|pk\rangle$, the electron fields are contracted exactly as in Problem 1(f), $t$-channel ($p \to p'$, $k \to k'$) and $u$-channel ($p \to k'$, $k \to p'$), and the two $\hat A$'s are contracted with each other. The photon field commutes with the fermionic operators, so the fermionic operators appear in the same order as in Problem 1(f), with $|pk\rangle = \hat a^\dagger_p\hat a^\dagger_k|0\rangle$ and $\langle p'k'| = \langle0|\,\hat a_{p'}\hat a_{k'}$, and the same exchanges bring the contracted pairs together: $7$ for the $t$-channel, sign $-1$, and $6$ for the $u$-channel, sign $+1$ ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^der-c8b-11-6|Derivation §C8b.11.6]]). The two diagrams therefore enter with a relative minus sign.
>
> **Step 4** (assemble). With $q = p - p'$ for the $t$-channel and $q = p - k'$ for the $u$-channel, and $(-ie)^2(-i) = ie^2$, the two terms are those of the statement. (End of the user's solution of part (a).)
>
> **Step 5** (item 3). Under $(p', \lambda') \leftrightarrow (k', \mu')$ the numerator and the denominator of the first term become those of the second and conversely, while the signs in front stay: the bracket goes into minus itself.
>
> **What the derivation shows**
> - The relative sign is found once, for the fermion operators; it does not depend on which boson is exchanged ([[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]).
> - Each diagram is a product of two currents: the first joins the helicities $\lambda \to \lambda'$ and $\mu \to \mu'$ along its lines, the second $\lambda \to \mu'$ and $\mu \to \lambda'$.

^der-c8b-12-1

*Uses:* [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]], [[§C8a.4 Feynman Rules for QED#^thm-c8a-4-4|Theorem §C8a.4.4]], [[§C8a.3 Photon Lines꞉ the Quantized Photon Field, Polarizations and the Propagator#^thm-c8a-3-5|Theorem §C8a.3.5]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|Theorem §C8b.11.6]], [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-1|P9, step 1]]

> [!caution] Caution: The overall sign of the electron–electron amplitude
> The signs $-$ ($t$-channel) and $+$ ($u$-channel) of [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]] are those of the bra $\langle p'k'| = \langle0|\,\hat a_{p'}\hat a_{k'}$, as in Problem 1(f). With the bra taken as the adjoint of the ket, $\langle0|\,\hat a_{k'}\hat a_{p'}$ (the course convention, [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]), both signs are reversed. This is a choice of convention ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^cau-c8b-11-1|§C8b.11, Caution: The order of the bra in Problem Set 11]]): the relative sign, every $|\mathcal M_{\lambda'\mu';\lambda\mu}|^2$ and the lists of the largest amplitudes below are the same for both.
>
> *Source: PHY 513, Problem Set 11, Problem 2(a) (the user's solution; line 634 of its tex source, `qft-C/lectures/hw11_user.tex`) against [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] and [[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign]] · recorded in `qft-C/ERRATA.md`*

^cau-c8b-12-1

## The vector vertex at equal momenta

> [!theorem] Theorem §C8b.12.2: In the Forward Direction the Vector Coupling Conserves Helicity
> For the helicity spinors $u_\lambda(p)$ of an electron of mass $m$, with $\xi_{\lambda'}^\dagger\xi_\lambda = \delta_{\lambda\lambda'}$,
>
> $$
> \bar u_{\lambda'}(p)\,\gamma^\mu\,u_\lambda(p) = 2p^\mu\,\delta_{\lambda\lambda'} .
> $$
>
> 1. It is the Gordon identity ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-9|Theorem §C5a.13.9]]) at $p' = p$, where $q = 0$ and the spin term drops out, together with $\bar u_{\lambda'}(p)\,u_\lambda(p) = 2m\,\delta_{\lambda\lambda'}$.
> 2. The factor $m$ cancels: the identity holds for every $m > 0$, and by continuity at $m = 0$.
> 3. The same identity holds in any orthonormal spin basis, $\bar u^r(p)\gamma^\mu u^s(p) = 2p^\mu\delta^{rs}$; nothing in the derivation uses that $\xi_\lambda$ is a helicity eigenvector.
>
> *Equivalently,* for $v$ spinors the Gordon identity with $m \to -m$ gives $\bar v^r(p)\gamma^\mu v^s(p) = 2p^\mu\delta^{rs}$, the forward limit worked out in [[PHY 513 Practice Midterm Solutions#^sol-pm-5-b|Practice Midterm, Problem 5(b), Solution]]; the component $\mu = 0$ is the normalization $u^{r\dagger}u^s = 2E_{\mathbf p}\delta^{rs}$ of [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-1|Theorem §C5a.12.1]]. At high energy the vector vertex joins equal helicities at every angle, not only at $p' = p$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]); the identity here is exact for every mass but holds at equal momenta only.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number positive-frequency spinors on shell, both at the same momentum $p$, any orthonormal spin basis; exact.
>
> *Source: PHY 513, Problem Set 11, Problem 2(b) (statement: "Show that, in the forward direction where $p'_\mu = p_\mu$, the vector coupling is helicity-conserving … Hint: Refer to the Gordon identity"; the user's solution) · checked numerically for random momenta, all four $\mu$ (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-12-2

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 2(b).
>
> **Step 1** (the spinors). Here $u_\lambda(p)$ is the helicity eigenspinor, the solution $u(p)$ of the Dirac equation with the two-spinor $\xi = \xi_\lambda$ of definite helicity,
>
> $$
> u_\lambda(p) = \begin{pmatrix}\sqrt{p\cdot\sigma}\;\xi_\lambda\\ \sqrt{p\cdot\bar\sigma}\;\xi_\lambda\end{pmatrix} , \qquad \xi_{\lambda'}^\dagger\xi_\lambda = \delta_{\lambda\lambda'} .
> $$
>
> **Step 2** (the Gordon identity). For any two spinors $u(p)$, $u(p')$ of mass $m$ satisfying the Dirac equation, the Gordon identity (Problem Set 5, Problem 3; [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-9|Theorem §C5a.13.9]]) is
>
> $$
> \bar u(p')\,\gamma^\mu\,u(p) = \bar u(p')\biggl[\frac{p'^\mu + p^\mu}{2m} + \frac{i\sigma^{\mu\nu}q_\nu}{2m}\biggr]u(p) , \qquad q = p' - p , \qquad \sigma^{\mu\nu} = \frac i2\bigl[\gamma^\mu, \gamma^\nu\bigr] .
> $$
>
> **Step 3** (forward). In the forward direction $p' = p$, so $q = 0$ and $p'^\mu + p^\mu = 2p^\mu$:
>
> $$
> \bar u_{\lambda'}(p)\,\gamma^\mu\,u_\lambda(p) = \frac{p^\mu}{m}\,\bar u_{\lambda'}(p)\,u_\lambda(p) .
> $$
>
> **Step 4** (the scalar product). With $\bar u = u^\dagger\gamma^0$ and $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$,
>
> $$
> \bar u_{\lambda'}(p)\,u_\lambda(p) = \xi_{\lambda'}^\dagger\Bigl[\sqrt{p\cdot\bar\sigma}\,\sqrt{p\cdot\sigma} + \sqrt{p\cdot\sigma}\,\sqrt{p\cdot\bar\sigma}\Bigr]\xi_\lambda .
> $$
>
> The matrices $p\cdot\sigma = E - \boldsymbol\sigma\cdot\mathbf p$ and $p\cdot\bar\sigma = E + \boldsymbol\sigma\cdot\mathbf p$ are both functions of $\boldsymbol\sigma\cdot\mathbf p$, so their square roots commute, and $(p\cdot\sigma)(p\cdot\bar\sigma) = E^2 - (\boldsymbol\sigma\cdot\mathbf p)^2 = E^2 - |\mathbf p|^2 = m^2$. Hence each term in the bracket is $m$, and
>
> $$
> \bar u_{\lambda'}(p)\,u_\lambda(p) = 2m\,\xi_{\lambda'}^\dagger\xi_\lambda = 2m\,\delta_{\lambda\lambda'}
> $$
>
> ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]]).
>
> **Step 5** (the result). Therefore
>
> $$
> \bar u_{\lambda'}(p)\,\gamma^\mu\,u_\lambda(p) = \frac{p^\mu}{m}\cdot2m\,\delta_{\lambda\lambda'} = 2p^\mu\,\delta_{\lambda\lambda'} .
> $$
>
> (End of the user's solution of part (b).)
>
> **What the derivation shows**
> - At zero momentum transfer only the convection term of the Gordon identity is left; the spin term, which is what can change the spin state, is proportional to $q$ ([[§C5a.13 Gamma-Matrix Technology#^rem-c5a-13-4|§C5a.13, Remark: What the Gordon identity says]]).
> - ⚑ By-product: $2p^\mu\delta_{\lambda\lambda'}$ is the current of a particle that is not deflected and keeps its spin: the form the vertices take next to a pole of the photon propagator → [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|Theorem §C8b.12.3]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-4|Theorem §C8b.12.4]].

^der-c8b-12-2

*Uses:* [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-9|Theorem §C5a.13.9]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-2|Theorem §C5a.12.2]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]]

## The forward and the backward direction

> [!theorem] Theorem §C8b.12.3: Near the Forward Direction the Helicity-Conserving Amplitudes Are Largest
> In the centre-of-mass frame, for $\theta \to 0$ with $\theta \ne 0$ (so $p' \approx p$, $k' \approx k$):
> 1. the first term of [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]] dominates: its photon propagator is $1/(p - p')^2$ with $(p - p')^2 \to 0$, while the second has $1/(p - k')^2$ with $p - k' \approx p - k$, which stays finite;
> 2. both vertices of the first term join nearly equal momenta, so by [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]], with corrections of order $\theta$,
>
> $$
> \bar u_{\lambda'}(p')\gamma^\mu u_\lambda(p) \approx 2p^\mu\,\delta_{\lambda\lambda'} , \qquad \bar u_{\mu'}(k')\gamma_\mu u_\mu(k) \approx 2k_\mu\,\delta_{\mu\mu'} ;
> $$
>
> 3. hence
>
> $$
> i\mathcal M_{\lambda'\mu';\lambda\mu} \approx -ie^2\,\frac{2p^\mu\,\delta_{\lambda\lambda'}\;2k_\mu\,\delta_{\mu\mu'}}{(p - p')^2} = -\frac{4ie^2\,(p\cdot k)}{(p - p')^2}\,\delta_{\lambda\lambda'}\,\delta_{\mu\mu'} ,
> $$
>
> which grows like $1/\theta^2$ as $\theta \to 0$; the corrections of order $\theta$ at the vertices contribute at most order $1/\theta$, and the second term is finite;
> 4. the largest amplitudes are therefore those with $\lambda' = \lambda$ and $\mu' = \mu$, with $\lambda$ and $\mu$ free,
>
> $$
> \mathcal M_{RR;RR} , \qquad \mathcal M_{LL;LL} , \qquad \mathcal M_{RL;RL} , \qquad \mathcal M_{LR;LR} ,
> $$
>
> in which each electron keeps its helicity.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, centre-of-mass frame, $\theta \to 0$, $\theta \ne 0$, any mass; the phase of the right-hand sides of items 2–3 depends on the phases of the helicity two-spinors ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^cau-c8b-12-2|Caution: The phases of the helicity two-spinors near the forward direction]]).
>
> *Source: PHY 513, Problem Set 11, Problem 2(c) (the user's solution) · checked numerically for $m/E = 0$, $0.025$ and $0.5$: the four largest amplitudes, their modulus $4e^2(p\cdot k)/|(p - p')^2|$ and the growth $1/\theta^2$ (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-12-3

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 2(c).
>
> **Step 1** (which term). In the near-forward direction the scattering angle $\theta$ is small, $\theta \to 0$ with $\theta \ne 0$, so $p' \approx p$ and $k' \approx k$. In the amplitude of part (a), the first term has the photon propagator $1/(p - p')^2$ with $(p - p')^2 \to 0$, while the second has $1/(p - k')^2$ with $p - k' \approx p - k$, which stays finite. The first term therefore dominates.
>
> **Step 2** (its vertices). Both of its vertices join nearly equal momenta, $p \to p' \approx p$ and $k \to k' \approx k$, so by part (b)
>
> $$
> \bar u_{\lambda'}(p')\gamma^\mu u_\lambda(p) \approx 2p^\mu\,\delta_{\lambda\lambda'} , \qquad \bar u_{\mu'}(k')\gamma_\mu u_\mu(k) \approx 2k_\mu\,\delta_{\mu\mu'} ,
> $$
>
> with corrections of order $\theta$.
>
> **Step 3** (the amplitude). Hence
>
> $$
> i\mathcal M_{\lambda'\mu';\lambda\mu} \approx -ie^2\,\frac{2p^\mu\,\delta_{\lambda\lambda'}\;2k_\mu\,\delta_{\mu\mu'}}{(p - p')^2} = -\frac{4ie^2\,(p\cdot k)}{(p - p')^2}\,\delta_{\lambda\lambda'}\,\delta_{\mu\mu'} ,
> $$
>
> which grows like $1/\theta^2$ as $\theta \to 0$. The corrections of order $\theta$ at the vertices contribute at most order $1/\theta$, and the second term is finite.
>
> **Step 4** (the list). The largest amplitudes are therefore those with $\lambda' = \lambda$ and $\mu' = \mu$, with $\lambda$ and $\mu$ free: $\mathcal M_{RR;RR}$, $\mathcal M_{LL;LL}$, $\mathcal M_{RL;RL}$, $\mathcal M_{LR;LR}$, in which each electron keeps its helicity. (End of the user's solution of part (c).)
>
> **What the derivation shows**
> - The forward peak is that of the $t$-channel pole ([[§C8a.14 Crossing Symmetry and Mandelstam Variables#^ex-c8a-14-1|Example §C8a.14.1]], item 2; [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-5|Theorem §C8a.14.5]], 3), and the pole selects the helicity-diagonal part of each vertex: a photon that is nearly on shell and carries almost no momentum does not turn the spin.

^der-c8b-12-3

*Uses:* [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]]

> [!caution] Caution: The phases of the helicity two-spinors near the forward direction
> [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]] is an identity between spinors at one momentum, built on one pair of two-spinors. Its use at nearly equal momenta, $\bar u_{\mu'}(k')\gamma_\mu u_\mu(k) \approx +2k_\mu\delta_{\mu\mu'}$, holds when the helicity two-spinors of $k'$ go over continuously into those of $k$ as $\theta \to 0$. Problem 2 fixes no phases. With the azimuths chosen in Problem 1(e) ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]]: $\phi = 0$ for $k$, $\phi = \pi$ for $k'$) one has $\xi_\pm(k') \to -\xi_\pm(k)$, so that vertex tends to $-2k_\mu\delta_{\mu\mu'}$ and the forward amplitude to $+\frac{4ie^2(p\cdot k)}{(p - p')^2}\delta_{\lambda\lambda'}\delta_{\mu\mu'}$; for the vertex $p \to p'$, and for both vertices of the backward direction ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-4|Theorem §C8b.12.4]]), the same azimuths give the signs as written. This is a matter of phase convention at the south pole ([[§C8b.5 Helicity Spinors and the Massless Limit#^cau-c8b-5-1|§C8b.5, Caution: No phase convention is smooth on the whole sphere]]). The moduli, the growth like $1/\theta^2$ and the list of the largest amplitudes do not depend on it.
>
> *Source: PHY 513, Problem Set 11, Problem 2(c) (the user's solution; lines 680–684 of its tex source, `qft-C/lectures/hw11_user.tex`) · both phase choices checked numerically (`qft-C/tools/hw11/verify.py`) · recorded in `qft-C/ERRATA.md`*

^cau-c8b-12-2

> [!theorem] Theorem §C8b.12.4: Near the Backward Direction the Helicities Follow the Directions
> In the centre-of-mass frame, for $\theta \to \pi$ with $\theta \ne \pi$:
> 1. $\mathbf p' \approx -\mathbf p = \mathbf k$ and $\mathbf k' \approx \mathbf p$, and all four energies are equal, so $p' \approx k$, $k' \approx p$;
> 2. the second term of [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]] now dominates: its photon propagator is $1/(p - k')^2$ with $(p - k')^2 \to 0$, while the first has $1/(p - p')^2$ with $p - p' \approx p - k$, which stays finite;
> 3. its vertices join $p \to k' \approx p$ and $k \to p' \approx k$, so by [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]]
>
> $$
> \bar u_{\mu'}(k')\gamma^\mu u_\lambda(p) \approx 2p^\mu\,\delta_{\lambda\mu'} , \qquad \bar u_{\lambda'}(p')\gamma_\mu u_\mu(k) \approx 2k_\mu\,\delta_{\mu\lambda'} ,
> $$
>
> and
>
> $$
> i\mathcal M_{\lambda'\mu';\lambda\mu} \approx ie^2\,\frac{2p^\mu\,\delta_{\lambda\mu'}\;2k_\mu\,\delta_{\mu\lambda'}}{(p - k')^2} = \frac{4ie^2\,(p\cdot k)}{(p - k')^2}\,\delta_{\lambda\mu'}\,\delta_{\mu\lambda'} ,
> $$
>
> which grows like $1/(\pi - \theta)^2$ as $\theta \to \pi$;
> 4. the largest amplitudes are therefore those with $\mu' = \lambda$ and $\lambda' = \mu$,
>
> $$
> \mathcal M_{RR;RR} , \qquad \mathcal M_{LL;LL} , \qquad \mathcal M_{LR;RL} , \qquad \mathcal M_{RL;LR} ,
> $$
>
> in which the electron emerging along $\mathbf p$ has the helicity of the incoming electron $p$, and the one emerging along $\mathbf k$ that of the incoming electron $k$.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]]; *applies:* order $e^2$, centre-of-mass frame, $\theta \to \pi$, $\theta \ne \pi$, any mass; the phases of item 3 as for [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|Theorem §C8b.12.3]].
>
> *Source: PHY 513, Problem Set 11, Problem 2(d) (statement: "Which helicity amplitudes are largest near the backward direction? Hint: this is an easy question"; the user's solution) · checked numerically as for [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|Theorem §C8b.12.3]] (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-12-4

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 2(d).
>
> **Step 1** (kinematics). In the backward direction $\theta \to \pi$ with $\theta \ne \pi$, so in the centre-of-mass frame $\mathbf p' \approx -\mathbf p = \mathbf k$ and $\mathbf k' \approx \mathbf p$. All four energies are equal, so
>
> $$
> p' \approx k , \qquad k' \approx p .
> $$
>
> **Step 2** (which term). In the amplitude of part (a), the second term now has the photon propagator $1/(p - k')^2$ with $(p - k')^2 \to 0$, while the first has $1/(p - p')^2$ with $p - p' \approx p - k$, which stays finite. The second term therefore dominates.
>
> **Step 3** (its vertices). Its vertices join $p \to k' \approx p$ and $k \to p' \approx k$, so by part (b)
>
> $$
> \bar u_{\mu'}(k')\gamma^\mu u_\lambda(p) \approx 2p^\mu\,\delta_{\lambda\mu'} , \qquad \bar u_{\lambda'}(p')\gamma_\mu u_\mu(k) \approx 2k_\mu\,\delta_{\mu\lambda'} ,
> $$
>
> and
>
> $$
> i\mathcal M_{\lambda'\mu';\lambda\mu} \approx ie^2\,\frac{2p^\mu\,\delta_{\lambda\mu'}\;2k_\mu\,\delta_{\mu\lambda'}}{(p - k')^2} = \frac{4ie^2\,(p\cdot k)}{(p - k')^2}\,\delta_{\lambda\mu'}\,\delta_{\mu\lambda'} ,
> $$
>
> which grows like $1/(\pi - \theta)^2$ as $\theta \to \pi$.
>
> **Step 4** (the list). The largest amplitudes are therefore those with $\mu' = \lambda$ and $\lambda' = \mu$: $\mathcal M_{RR;RR}$, $\mathcal M_{LL;LL}$, $\mathcal M_{LR;RL}$, $\mathcal M_{RL;LR}$, in which the electron emerging along $\mathbf p$ has the helicity of the incoming electron $p$, and the one emerging along $\mathbf k$ that of the incoming electron $k$. (End of the user's solution of Problem 2.)
>
> **What the derivation shows**
> - Backward scattering of identical particles is forward scattering with the two final labels exchanged: the $u$-channel diagram is the $t$-channel diagram with $(p', \lambda') \leftrightarrow (k', \mu')$, and the list of part 4 is that of [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|Theorem §C8b.12.3]] with $\lambda' \leftrightarrow \mu'$.
> - $\mathcal M_{RR;RR}$ and $\mathcal M_{LL;LL}$ are large in both directions; $\mathcal M_{RL;RL}$, $\mathcal M_{LR;LR}$ only forward, $\mathcal M_{LR;RL}$, $\mathcal M_{RL;LR}$ only backward.

^der-c8b-12-4

*Uses:* [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]]

> [!remark] Remark: The same lists from angular momentum along the beam
> The two lists agree with conservation of the angular momentum along the collision axis, the argument of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]] for $e^+e^- \to \mu^+\mu^-$. With $\mathbf p$ along $+\hat{\mathbf z}$ and $\mathbf k$ along $-\hat{\mathbf z}$ the initial state has $J_z = \frac12(\lambda - \mu)$, in units where $R = +1$, $L = -1$: the spin of $k$ points against $\hat{\mathbf z}$ when its helicity is positive. Exactly forward the final electrons move along the same axes, $J_z = \frac12(\lambda' - \mu')$, and $\lambda' = \lambda$, $\mu' = \mu$ conserves it. Exactly backward $\mathbf p'$ is along $-\hat{\mathbf z}$ and $\mathbf k'$ along $+\hat{\mathbf z}$, $J_z = \frac12(\mu' - \lambda')$, and $\mu' = \lambda$, $\lambda' = \mu$ conserves it. On the axis the orbital angular momentum has no $z$ component, so the spins must balance by themselves.
>
> *Source: written here from [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]] and the lists of Problem Set 11, Problem 2(c)–(d) (the user's solution); not part of the problem set · checked (`qft-C/tools/hw11/verify.py`)*

^rem-c8b-12-1

> [!remark]- Connections
> - The same two diagrams with a scalar in place of the photon, where each vertex flips the helicity and the amplitudes have no forward or backward peak — [[§C8b.11 Helicity Amplitudes in Yukawa Theory|§C8b.11]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^rem-c8b-11-1|§C8b.11, Remark: Yukawa and QED side by side]].
> - Helicity conservation at the QED vertex at high energy, at every angle — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]; the rule for any number of $\gamma$'s — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]].
> - The Gordon identity and its reading as convection plus spin — [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-9|Theorem §C5a.13.9]], [[§C5a.13 Gamma-Matrix Technology#^rem-c5a-13-4|§C5a.13, Remark: What the Gordon identity says]].
> - The relative sign of two diagrams that differ by exchanged fermions, and the overall sign — [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]], [[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign]].
> - The $t$- and $u$-channel and their characteristic angular dependence; $u$ as $t$ with the outgoing momenta exchanged — [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^def-c8a-14-2|Def. §C8a.14.2]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^ex-c8a-14-1|Example §C8a.14.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^rem-c8a-14-2|§C8a.14, Remark: The variable u for identical particles]].
> - Scattering of two distinguishable fermions by photon exchange, which has the $t$-channel diagram only — [[§C8a.12 Electron–Muon Scattering and the Crossing Substitution#^thm-c8a-12-1|Theorem §C8a.12.1]]; its nonrelativistic limit, the Coulomb potential — [[§C8a.5 The Coulomb Potential, and Why Like Charges Repel#^thm-c8a-5-3|Theorem §C8a.5.3]].
> - The recipe — [[P9 Helicity Amplitudes|P9]].
