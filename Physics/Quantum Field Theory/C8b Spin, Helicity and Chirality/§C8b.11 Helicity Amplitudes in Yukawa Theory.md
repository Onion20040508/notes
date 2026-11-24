---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.11
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8b.10 Helicity Suppression in Backward Compton Scattering|§C8b.10]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering|§C8b.12]] →

*Sources: PHY 513, Problem Set 11 ("Processes with Fermions and Helicity", due 22 Nov 2026), Problem 1 "Helicity Amplitudes in Yukawa Theory", parts (b)–(g): statement, and the user's solution (submitted; used as written) · PHY 513, Problem Set 5, Problem 6 (the helicity two-spinors; the user's solution) · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, eqs. (4.118)–(4.119) (the amplitude the statement refers to) · PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 24–25 (helicity two-spinors and four-spinors). Part (a) of the problem is in [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]] (Theorems §C8b.6.9–§C8b.6.10).*

What do the sixteen helicity amplitudes of fermion–fermion scattering look like when the force is carried by a scalar? In QED the vertex keeps the helicity of each fermion ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]); the Yukawa vertex has no $\gamma$ and flips it ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]]). This section follows Problem Set 11, Problem 1, as the user solved it: the selection rule leaves six of the sixteen amplitudes of $ff \to ff$ ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]]); with the explicit helicity spinors at high energy ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-2|Theorem §C8b.11.2]]) the rule is found again ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-3|Theorem §C8b.11.3]]), each vertex becomes an inner product of two-spinors ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5|Theorem §C8b.11.5]]), and the six amplitudes are constants: $2g^2$ twice and $-g^2$ four times ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-8|Theorem §C8b.11.8]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-9|Theorem §C8b.11.9]]), with spin average $3g^4$ ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-10|Theorem §C8b.11.10]]). The amplitude and its two diagrams are [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] (PS (4.119)); the helicity two-spinors are [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]; the method, explicit helicity spinors inserted in the amplitude, is the second method of Lecture 20 ([[P9 Helicity Amplitudes#^p9-7|P9, step 7]]).

**The mathematical picture.** Each diagram is a product of two scalar bilinears $\bar u(\text{out})\,u(\text{in})$, one per vertex, times a scalar propagator. In the chiral basis $\gamma^0$ exchanges the two halves of a row, so a scalar bilinear pairs the upper half of one spinor with the lower half of the other. At high energy a helicity spinor occupies one half only ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]), so the bilinear is zero for equal helicities and otherwise an inner product $\xi^\dagger\xi$ in $\mathbb C^2$ of two helicity two-spinors: the overlap of two spin-$\frac12$ states quantized along different directions, a function of half the angle between them.

**Setup.** Yukawa theory ([[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]) at order $g^2$: elastic scattering of two fermions, $f(p, \lambda)\,f(k, \mu) \to f(p', \lambda')\,f(k', \mu')$, free relativistic states over $|0\rangle$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]). Centre-of-mass frame; energies very large compared with the masses, $E/M \to \infty$ at fixed scattering angle $\theta$, with $\theta \ne 0, \pi$; the scalar mass is neglected as well in this limit. All statements about helicity are for this limit; corrections are of relative size $M/E$.

*Conventions* ([[Larsen PHY 513]]): the problem set writes $M$ for the fermion mass and $m$ (in part (f) $m_\phi$) for the scalar mass, where Model §C6d.1.1 writes $m$ and $m_\phi$; this section uses $M$ and $m_\phi$. $\lambda, \mu$ are the helicities of the incoming fermions $p, k$ and $\lambda', \mu'$ those of the outgoing fermions $p', k'$, each $R$ (numerical value $+1$, helicity $+\frac12$) or $L$ ($-1$, helicity $-\frac12$); $u_R$, $u_L$ are the spinors $u_+$, $u_-$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]]. $\bar u_\lambda \equiv \overline{u_\lambda}$. $c \equiv \cos\frac\theta2$, $s \equiv \sin\frac\theta2$. Chiral basis, $\gamma^0 = \bigl(\begin{smallmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{smallmatrix}\bigr)$. The statement prints the scalar mass term of the Lagrangian as $-m^2\phi^2$, without the $\frac12$ of Model §C6d.1.1; the scalar mass is neglected in everything below.

## Which amplitudes may be nonzero

> [!definition] Definition §C8b.11.1: Helicity Amplitudes of a 2 → 2 Fermion Process
> For the scattering of two fermions of definite helicities, $f(p, \lambda)\,f(k, \mu) \to f(p', \lambda')\,f(k', \mu')$, the **helicity amplitudes** are
>
> $$
> \langle p'\lambda'\,k'\mu', \text{out}\,|\,p\lambda\,k\mu, \text{in}\rangle \equiv i\mathcal M_{\lambda'\mu';\lambda\mu}(E_{\rm cm}, \theta) ,
> $$
>
> where $\theta$ is the scattering angle in the centre-of-mass frame and each index is $L$ or $R$: the two outgoing helicities stand before the semicolon, the two incoming ones after it. Varying all helicities there are $2^4 = 16$ amplitudes. The scattering of polarized particles, that is of particles with definite helicities, shows much about the nature of their interaction.
>
> *Equivalently,* $\mathcal M_{\lambda'\mu';\lambda\mu}$ is the invariant amplitude of [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]] between helicity eigenstates, with the factor $(2\pi)^4\delta^4(p + k - p' - k')$ stripped; Yu's $\mathcal M(\lambda_1, \lambda_2, \lambda_1', \lambda_2')$ (★ [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]]) lists the incoming helicities first.
>
> *Model:* any theory with spin-$\frac12$ particles; *applies:* $2 \to 2$ processes, helicity basis for every external fermion.
>
> *Source: PHY 513, Problem Set 11, Problem 1, statement, eq. (2), and Problem 2, statement*

^def-c8b-11-1

> [!theorem] Theorem §C8b.11.1: Six of the Sixteen Helicity Amplitudes May Be Nonzero
> ![[ph-qft-c8b-11-1.svg]]
> *The two diagrams of $f(p, \lambda)\,f(k, \mu) \to f(p', \lambda')\,f(k', \mu')$ at order $g^2$, time running to the right, after the user's drawing (Problem Set 11, Problem 1(b)); the helicity of each fermion is written at the end of its line.*
>
> At order $g^2$, in the high-energy limit:
> 1. the $t$-channel diagram, whose vertices join $p \to p'$ and $k \to k'$, is nonzero only if $\lambda' = -\lambda$ and $\mu' = -\mu$;
> 2. the $u$-channel diagram, whose vertices join $p \to k'$ and $k \to p'$, is nonzero only if $\mu' = -\lambda$ and $\lambda' = -\mu$;
> 3. the amplitude is the difference of the two diagrams, so it can be nonzero only if at least one of the two pairs of conditions holds. For each pair of incoming helicities:
>
> | $\lambda\mu$ | $t$-channel: $\lambda'\mu'$ | $u$-channel: $\lambda'\mu'$ |
> |---|---|---|
> | $RR$ | $LL$ | $LL$ |
> | $RL$ | $LR$ | $RL$ |
> | $LR$ | $RL$ | $LR$ |
> | $LL$ | $RR$ | $RR$ |
>
> 4. hence 6 of the 16 amplitudes may be nonvanishing,
>
> $$
> \mathcal M_{LL;RR} , \quad \mathcal M_{RR;LL} , \quad \mathcal M_{LR;RL} , \quad \mathcal M_{RL;LR} , \quad \mathcal M_{RL;RL} , \quad \mathcal M_{LR;LR} ,
> $$
>
> where both diagrams contribute to $\mathcal M_{LL;RR}$ and $\mathcal M_{RR;LL}$, only the $t$-channel to $\mathcal M_{LR;RL}$ and $\mathcal M_{RL;LR}$, and only the $u$-channel to $\mathcal M_{RL;RL}$ and $\mathcal M_{LR;LR}$. The other 10 vanish.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* order $g^2$, $E \gg M$; the ten zeros up to amplitudes of relative size $M/E$.
>
> *Source: PHY 513, Problem Set 11, Problem 1(b) (the user's solution) · the diagrams and the amplitude: PS §4.7, eq. (4.119), [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]] · checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-1

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(b).
>
> **Step 1** (the diagrams). At order $g^2$ the scattering $f(p, \lambda)\,f(k, \mu) \to f(p', \lambda')\,f(k', \mu')$ has two diagrams, the $t$-channel and the $u$-channel diagram of the figure.
>
> **Step 2** (each vertex flips). By part (a) ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]]), each vertex flips the helicity of the fermion passing through it. In the $t$-channel diagram the vertices join $p \to p'$ and $k \to k'$, so it is nonzero only if
>
> $$
> \lambda' = -\lambda , \qquad \mu' = -\mu .
> $$
>
> In the $u$-channel diagram the vertices join $p \to k'$ and $k \to p'$, so it is nonzero only if
>
> $$
> \mu' = -\lambda , \qquad \lambda' = -\mu .
> $$
>
> **Step 3** (the amplitude). The amplitude $\mathcal M_{\lambda'\mu';\lambda\mu}$ is the difference of the two diagrams, so it can be nonzero only if at least one of these two pairs of conditions holds. For each pair of incoming helicities $(\lambda, \mu)$, the outgoing helicities $(\lambda', \mu')$ allowed by each diagram are those of the table.
>
> **Step 4** (count). $RR \to LL$ and $LL \to RR$ are allowed by both diagrams; $RL \to LR$ and $LR \to RL$ by the $t$-channel only; $RL \to RL$ and $LR \to LR$ by the $u$-channel only. Hence the six amplitudes of part 4; the other 10 vanish. (End of the user's solution of part (b).)
>
> **What the derivation shows**
> - In every allowed amplitude both fermions change helicity along their lines. In the two that are diagonal in the labels, $\mathcal M_{RL;RL}$ and $\mathcal M_{LR;LR}$, the lines cross: the fermion that leaves along $\mathbf p'$ is the one that came in along $\mathbf k$.
> - The contrast with a vector vertex, which keeps the helicity along each line → [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering|§C8b.12]].

^der-c8b-11-1

*Uses:* [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]], [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^def-c8b-11-1|Def. §C8b.11.1]]

## The explicit spinors

> [!theorem] Theorem §C8b.11.2: The Helicity Spinors at Very High Energy
> For $\mathbf p = |\mathbf p|\,(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ and the helicity two-spinors $\xi_\pm$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]] (Problem Set 5, Problem 6),
>
> $$
> u_R(p) = \begin{pmatrix}\sqrt{E - |\mathbf p|}\;\xi_+\\ \sqrt{E + |\mathbf p|}\;\xi_+\end{pmatrix} , \qquad u_L(p) = \begin{pmatrix}\sqrt{E + |\mathbf p|}\;\xi_-\\ \sqrt{E - |\mathbf p|}\;\xi_-\end{pmatrix} ,
> $$
>
> and in the limit $E/M \to \infty$, with the angles kept fixed,
>
> $$
> u_R(p) = \sqrt{2E}\begin{pmatrix}0\\ 0\\ \cos\frac\theta2\\ e^{i\phi}\sin\frac\theta2\end{pmatrix} , \qquad u_L(p) = \sqrt{2E}\begin{pmatrix}-e^{-i\phi}\sin\frac\theta2\\ \cos\frac\theta2\\ 0\\ 0\end{pmatrix} .
> $$
>
> *Equivalently,* the first pair is $u_\pm(p)$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]] and the limit is [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], parts 1–2, $u_+ \to \sqrt{2E}\,(0, \xi_+)^{\mathsf T}$, $u_- \to \sqrt{2E}\,(\xi_-, 0)^{\mathsf T}$, with the two-spinors written out; Lecture 20 states the same spinors ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-9|Theorem §C8b.7.9]]).
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* chiral basis; the first pair exact for every $M$, the second for $E/M \to \infty$ (exact at $M = 0$).
>
> *Source: PHY 513, Problem Set 11, Problem 1(c) (statement: "HW5 prob 6 determined the explicit form of the two-spinors $\xi_\lambda(p)$ with definite helicity … find the explicit forms of the eigenspinors $u_\lambda(p)$ in the limit of very high energy"; the user's solution)*

^thm-c8b-11-2

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(c).
>
> **Step 1** (the solution for any spin). In the Weyl basis the positive-frequency solution of the Dirac equation with momentum $p$ is
>
> $$
> u(p) = \begin{pmatrix}\sqrt{E - \boldsymbol\sigma\cdot\mathbf p}\;\xi\\ \sqrt{E + \boldsymbol\sigma\cdot\mathbf p}\;\xi\end{pmatrix} ,
> $$
>
> which solves the Dirac equation for any two-spinor $\xi$ with $\xi^\dagger\xi = 1$; the choice of $\xi$ is the choice of spin state ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]]).
>
> **Step 2** (helicity). With $h = \frac{\mathbf p}{|\mathbf p|}\cdot\mathbf S$ and $\mathbf S = \frac12\operatorname{diag}(\boldsymbol\sigma, \boldsymbol\sigma)$, the matrix $\frac{\mathbf p}{|\mathbf p|}\cdot\boldsymbol\sigma$ commutes with $\sqrt{E \mp \boldsymbol\sigma\cdot\mathbf p}$, so $u(p)$ has helicity $\pm\frac12$ when $\xi$ does. By Problem Set 5, Problem 6, for $\mathbf p = |\mathbf p|\,(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ the two-spinors with $\bigl(\frac{\mathbf p}{|\mathbf p|}\cdot\frac{\boldsymbol\sigma}2\bigr)\xi_\pm = \pm\frac12\,\xi_\pm$ are
>
> $$
> \xi_+ = \begin{pmatrix}\cos\frac\theta2\\ e^{i\phi}\sin\frac\theta2\end{pmatrix} , \qquad \xi_- = \begin{pmatrix}-e^{-i\phi}\sin\frac\theta2\\ \cos\frac\theta2\end{pmatrix} .
> $$
>
> So $u_R$ has $\xi = \xi_+$ and $u_L$ has $\xi = \xi_-$.
>
> **Step 3** (the square roots become numbers). Since $(\boldsymbol\sigma\cdot\mathbf p)\,\xi_\pm = \pm|\mathbf p|\,\xi_\pm$, a function of $\boldsymbol\sigma\cdot\mathbf p$ acting on $\xi_\pm$ gives the same function of the eigenvalue:
>
> $$
> \sqrt{E - \boldsymbol\sigma\cdot\mathbf p}\;\xi_\pm = \sqrt{E \mp |\mathbf p|}\;\xi_\pm , \qquad \sqrt{E + \boldsymbol\sigma\cdot\mathbf p}\;\xi_\pm = \sqrt{E \pm |\mathbf p|}\;\xi_\pm .
> $$
>
> Hence the first pair of the statement.
>
> **Step 4** (the limit). With $E = \sqrt{|\mathbf p|^2 + M^2}$,
>
> $$
> E - |\mathbf p| = \frac{M^2}{E + |\mathbf p|} \to 0 , \qquad E + |\mathbf p| \to 2E \qquad \text{as } E/M \to \infty ,
> $$
>
> so the second pair follows. (End of the user's solution of part (c).)

^der-c8b-11-2

*Uses:* [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^def-c8b-5-1|Def. §C8b.5.1]]

> [!theorem] Theorem §C8b.11.3: The Selection Rule from the Explicit Spinors
> With the spinors of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-2|Theorem §C8b.11.2]] in the high-energy limit and $\bar u_\lambda \equiv \overline{u_\lambda} = u_\lambda^\dagger\gamma^0$:
> 1. the conjugates are
>
> $$
> \bar u_R(p) = \sqrt{2E}\,\bigl(\xi_+^\dagger,\ 0\bigr) = \sqrt{2E}\,\Bigl(\cos\tfrac\theta2,\ e^{-i\phi}\sin\tfrac\theta2,\ 0,\ 0\Bigr) , \qquad \bar u_L(p) = \sqrt{2E}\,\bigl(0,\ \xi_-^\dagger\bigr) = \sqrt{2E}\,\Bigl(0,\ 0,\ -e^{i\phi}\sin\tfrac\theta2,\ \cos\tfrac\theta2\Bigr) :
> $$
>
> $\bar u_R$ is nonzero only in the first two components and $\bar u_L$ only in the last two, while $u_R$ is nonzero only in the last two and $u_L$ only in the first two;
> 2. for a vertex with incoming momentum $p$ and outgoing momentum $p'$, with $\xi_\pm(p)$ and $\xi_\pm(p')$ the helicity two-spinors along $\mathbf p$ and $\mathbf p'$,
>
> $$
> \begin{aligned}
> \bar u_R(p')\,u_R(p) &= 0 , & \bar u_R(p')\,u_L(p) &= 2E\,\xi_+^\dagger(p')\,\xi_-(p) ,\\
> \bar u_L(p')\,u_L(p) &= 0 , & \bar u_L(p')\,u_R(p) &= 2E\,\xi_-^\dagger(p')\,\xi_+(p) ;
> \end{aligned}
> $$
>
> 3. the vertex $\bar u_{\lambda'}(p')\,u_\lambda(p)$ therefore vanishes for $\lambda' = \lambda$: the selection rule $\lambda' = -\lambda$ of [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]].
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (the vertex); *applies:* $E/M \to \infty$, any two directions $\mathbf p$, $\mathbf p'$, both fermions of energy $E$.
>
> *Source: PHY 513, Problem Set 11, Problem 1(d) (the user's solution) · checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-3

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(d).
>
> **Step 1** (the rows). With $\bar u_\lambda \equiv \overline{u_\lambda} = u_\lambda^\dagger\gamma^0$ as in part (a), and $\gamma^0 = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}$, which swaps the two halves of a row, $(a^\dagger, b^\dagger)\gamma^0 = (b^\dagger, a^\dagger)$, the spinors of part (c) give
>
> $$
> \bar u_R(p) = \sqrt{2E}\,\bigl(0,\ \xi_+^\dagger\bigr)\gamma^0 = \sqrt{2E}\,\bigl(\xi_+^\dagger,\ 0\bigr) = \sqrt{2E}\,\Bigl(\cos\tfrac\theta2,\ e^{-i\phi}\sin\tfrac\theta2,\ 0,\ 0\Bigr) ,
> $$
>
> $$
> \bar u_L(p) = \sqrt{2E}\,\bigl(\xi_-^\dagger,\ 0\bigr)\gamma^0 = \sqrt{2E}\,\bigl(0,\ \xi_-^\dagger\bigr) = \sqrt{2E}\,\Bigl(0,\ 0,\ -e^{i\phi}\sin\tfrac\theta2,\ \cos\tfrac\theta2\Bigr) .
> $$
>
> **Step 2** (where the entries are). So $\bar u_R$ is nonzero only in the first two components and $\bar u_L$ only in the last two, while $u_R$ is nonzero only in the last two and $u_L$ only in the first two.
>
> **Step 3** (the four products). For a vertex with incoming momentum $p$ and outgoing momentum $p'$, the row $\bar u_R(p')$ meets the column $u_R(p)$ in no component, and likewise $\bar u_L(p')$ and $u_L(p)$; the row $\bar u_R(p') = \sqrt{2E}(\xi_+^\dagger(p'), 0)$ meets $u_L(p) = \sqrt{2E}(\xi_-(p), 0)^{\mathsf T}$ in the first two components, and $\bar u_L(p')$ meets $u_R(p)$ in the last two. This gives part 2.
>
> **Step 4** (the rule). The vertex $\bar u_{\lambda'}(p')\,u_\lambda(p)$ therefore vanishes for $\lambda' = \lambda$, which is the selection rule $\lambda' = -\lambda$ of part (a). (End of the user's solution of part (d).)
>
> **What the derivation shows**
> - The rule is the block structure of the chiral basis: $\gamma^0$ exchanges the halves, and a helicity spinor at high energy fills one half. With a $\gamma^\mu$ in between the halves are exchanged once more, which is the block-diagonal $\gamma^0\gamma^\mu$ of [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]] and the opposite rule.
> - ⚑ By-product: every Yukawa vertex at high energy is $2E$ times an inner product of two helicity two-spinors → [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5|Theorem §C8b.11.5]].

^der-c8b-11-3

*Uses:* [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-2|Theorem §C8b.11.2]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]]

## Kinematics and the inner products

> [!theorem] Theorem §C8b.11.4: The Four Momenta in the Centre-of-Mass Frame and Their Two-Spinors
> In the centre-of-mass frame of $f(p)\,f(k) \to f(p')\,f(k')$, all four fermions of mass $M$:
> 1. $E_p = E_k = E_{p'} = E_{k'} = \dfrac{E_{\rm cm}}2 \equiv E$ and $|\mathbf p| = |\mathbf k| = |\mathbf p'| = |\mathbf k'|$;
> 2. with $\mathbf p$ along $+\hat{\mathbf z}$, $\mathbf k = -\mathbf p$ along $-\hat{\mathbf z}$, $\mathbf p'$ in the $x$–$z$ plane at the scattering angle $\theta$ to $\mathbf p$, and $\mathbf k' = -\mathbf p'$, the angles $(\theta, \phi)$ of the four directions and the two-spinors of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]] are
>
> | | $(\theta, \phi)$ | $\xi_+$ | $\xi_-$ |
> |---|---|---|---|
> | $p$ | $(0, \cdot)$ | $(1,\ 0)^{\mathsf T}$ | $(0,\ 1)^{\mathsf T}$ |
> | $k$ | $(\pi, 0)$ | $(0,\ 1)^{\mathsf T}$ | $(-1,\ 0)^{\mathsf T}$ |
> | $p'$ | $(\theta, 0)$ | $(c,\ s)^{\mathsf T}$ | $(-s,\ c)^{\mathsf T}$ |
> | $k'$ | $(\pi - \theta, \pi)$ | $(s,\ -c)^{\mathsf T}$ | $(c,\ s)^{\mathsf T}$ |
>
> with $c = \cos\frac\theta2$, $s = \sin\frac\theta2$;
> 3. the azimuth $\phi$ is undefined along the $z$-axis. For $p$ the spinors $\xi_\pm$ at $\theta = 0$ do not depend on $\phi$; for $k$ the choice $\phi = 0$ is made. Another choice multiplies the spinor of $k$ by a phase, which multiplies both diagrams, and hence the whole amplitude, by the same phase.
>
> *Equivalently,* these are the two-spinors of [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]] for the four momenta of $e^+e^- \to \mu^+\mu^-$ (there $p, p'$ are the beams and $k, k'$ the muons), except that the example takes the azimuth $\pi$ for the direction $-\hat{\mathbf z}$, which gives $(0, -1)^{\mathsf T}$ and $(1, 0)^{\mathsf T}$, the two-spinors of $k$ here times $-1$: the phase of item 3.
>
> *Model:* kinematics, and [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]; *applies:* centre-of-mass frame, equal masses, every $E$.
>
> *Source: PHY 513, Problem Set 11, Problem 1(e) (the user's solution, paragraph "Kinematics" and the table of "Inner products")*

^thm-c8b-11-4

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(e), paragraph "Kinematics", with the table of its second paragraph.
>
> **Step 1** (energies). In the centre-of-mass frame $\mathbf p + \mathbf k = 0$, so $|\mathbf k| = |\mathbf p|$; both fermions have mass $M$, so $E_k = E_p$, and $E_p + E_k = E_{\rm cm}$ gives $E_p = E_k = E_{\rm cm}/2$. Momentum conservation gives $\mathbf p' + \mathbf k' = \mathbf p + \mathbf k = 0$, so $|\mathbf k'| = |\mathbf p'|$ and $E_{k'} = E_{p'}$, and energy conservation, $E_{p'} + E_{k'} = E_{\rm cm}$, gives $E_{p'} = E_{k'} = E_{\rm cm}/2$. Hence part 1.
>
> **Step 2** (directions). Take $\mathbf p$ along $+\hat{\mathbf z}$, $\mathbf k = -\mathbf p$ along $-\hat{\mathbf z}$, $\mathbf p'$ in the $x$–$z$ plane at the scattering angle $\theta$ to $\mathbf p$, and $\mathbf k' = -\mathbf p'$. In the angles $(\theta, \phi)$ of the helicity spinors $\xi_\pm$ of part (c), the four directions are
>
> $$
> p:\ (0, \cdot) , \qquad k:\ (\pi, 0) , \qquad p':\ (\theta, 0) , \qquad k':\ (\pi - \theta, \pi) .
> $$
>
> **Step 3** (the azimuth on the axis). The azimuth $\phi$ is undefined along the $z$-axis. For $p$ the spinors $\xi_\pm$ at $\theta = 0$ do not depend on $\phi$; for $k$ fix $\phi = 0$. Another choice multiplies the spinor of $k$ by a phase, which multiplies both diagrams, and hence the whole amplitude, by the same phase.
>
> **Step 4** (the table). With $\xi_+(\theta, \phi) = (\cos\frac\theta2,\ e^{i\phi}\sin\frac\theta2)^{\mathsf T}$, $\xi_-(\theta, \phi) = (-e^{-i\phi}\sin\frac\theta2,\ \cos\frac\theta2)^{\mathsf T}$ and $c \equiv \cos\frac\theta2$, $s \equiv \sin\frac\theta2$, the spinors at the four directions are those of the table, where for $k'$ one uses $\cos\frac{\pi - \theta}2 = s$, $\sin\frac{\pi - \theta}2 = c$ and $e^{i\pi} = -1$. All entries are real.
>
> **What the derivation shows**
> - ⚑ By-product: the phases of the two-spinors on the collision axis are a choice, and the phase of an individual helicity amplitude depends on it ([[§C8b.5 Helicity Spinors and the Massless Limit#^cau-c8b-5-1|§C8b.5, Caution: No phase convention is smooth on the whole sphere]]); the moduli and the relative sign of the two diagrams do not.

^der-c8b-11-4

*Uses:* [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]]

> [!theorem] Theorem §C8b.11.5: The Four Inner Products
> With the spinors of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-2|Theorem §C8b.11.2]] at the four momenta of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]], in the high-energy limit:
>
> $$
> \begin{aligned}
> \bar u_R(p')\,u_L(p) &= 2E\sin\frac\theta2 , & \bar u_R(k')\,u_L(k) &= -2E\sin\frac\theta2 ,\\
> \bar u_R(p')\,u_L(k) &= -2E\cos\frac\theta2 , & \bar u_R(k')\,u_L(p) &= -2E\cos\frac\theta2 .
> \end{aligned}
> $$
>
> 1. The two products along the lines of the $t$-channel diagram ($p \to p'$, $k \to k'$) are $\pm2E\sin\frac\theta2$; they vanish in the forward direction.
> 2. The two products along the lines of the $u$-channel diagram ($k \to p'$, $p \to k'$) are $-2E\cos\frac\theta2$; they vanish in the backward direction.
> 3. The products with $R$ and $L$ exchanged follow from $\bigl(\bar u_a\,u_b\bigr)^{\ast} = \bar u_b\,u_a$ and the table of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]]; for example $\bar u_L(p')\,u_R(k) = 2E\cos\frac\theta2$.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (the vertices); *applies:* $E/M \to \infty$, the phase choices of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]].
>
> *Source: PHY 513, Problem Set 11, Problem 1(e) (the user's solution, paragraph "Inner products"); item 3: Problem 1(f), paragraph "Spinors" · checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-5

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(e), paragraph "Inner products".
>
> **Step 1** (the formula). By part (d) ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-3|Theorem §C8b.11.3]]), $\bar u_R(b)\,u_L(a) = 2E\,\xi_+^\dagger(b)\,\xi_-(a)$ for an incoming momentum $a$ and an outgoing momentum $b$.
>
> **Step 2** (the entries). All entries of the table of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]] are real, so $\xi_+^\dagger = \xi_+^{\mathsf T}$, and
>
> $$
> \begin{aligned}
> \bar u_R(p')\,u_L(p) &= 2E\,(c,\ s)\begin{pmatrix}0\\ 1\end{pmatrix} = 2E\sin\frac\theta2 ,\\
> \bar u_R(k')\,u_L(k) &= 2E\,(s,\ -c)\begin{pmatrix}-1\\ 0\end{pmatrix} = -2E\sin\frac\theta2 ,\\
> \bar u_R(p')\,u_L(k) &= 2E\,(c,\ s)\begin{pmatrix}-1\\ 0\end{pmatrix} = -2E\cos\frac\theta2 ,\\
> \bar u_R(k')\,u_L(p) &= 2E\,(s,\ -c)\begin{pmatrix}0\\ 1\end{pmatrix} = -2E\cos\frac\theta2 .
> \end{aligned}
> $$
>
> (End of the user's solution of part (e).)
>
> **Step 3** (item 3; from the user's part (f), paragraph "Spinors"). $\bigl(\bar u_a\,u_b\bigr)^{\ast} = \bar u_b\,u_a$, so
>
> $$
> \bar u_L(p')\,u_R(k) = \bigl[\bar u_R(k)\,u_L(p')\bigr]^{\ast} = \Bigl[2E\,(0,\ 1)\begin{pmatrix}-s\\ c\end{pmatrix}\Bigr]^{\ast} = 2E\cos\frac\theta2 .
> $$
>
> **What the derivation shows**
> - Each product is $2E$ times the overlap of two spin-$\frac12$ states along directions an angle $\theta$ or $\pi - \theta$ apart: the half angles are those of spin $\frac12$ (compare the $\cos\frac\theta2$, $\sin\frac\theta2$ of the muon two-spinors in [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]]).
> - A helicity flip at zero deflection is impossible: the overlap of $\xi_+$ and $\xi_-$ along the same direction is zero. This is why the $t$-channel products vanish at $\theta = 0$ and the $u$-channel ones at $\theta = \pi$.

^der-c8b-11-5

*Uses:* [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-3|Theorem §C8b.11.3]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]]

## The amplitudes

> [!theorem] Theorem §C8b.11.6: The Relative Sign of the Two Diagrams, by Counting Exchanges
> In terms of contractions in $\langle p'k'|\,(\hat{\bar\psi}\hat\psi\hat\phi)(z_1)\,(\hat{\bar\psi}\hat\psi\hat\phi)(z_2)\,|pk\rangle$, the two diagrams of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]] are:
> 1. $t$-channel ($p \to p'$, $k \to k'$): $\hat{\bar\psi}(z_1)$ with $p'$, $\hat\psi(z_1)$ with $p$, $\hat{\bar\psi}(z_2)$ with $k'$, $\hat\psi(z_2)$ with $k$, and $\hat\phi(z_1)$ with $\hat\phi(z_2)$;
> 2. $u$-channel ($p \to k'$, $k \to p'$): $\hat{\bar\psi}(z_1)$ with $k'$, $\hat\psi(z_1)$ with $p$, $\hat{\bar\psi}(z_2)$ with $p'$, $\hat\psi(z_2)$ with $k$, and $\hat\phi(z_1)$ with $\hat\phi(z_2)$.
>
> With $|pk\rangle = \hat a^\dagger_p\hat a^\dagger_k|0\rangle$ and $\langle p'k'| = \langle0|\,\hat a_{p'}\hat a_{k'}$ (normalization factors suppressed), bringing the contracted pairs together takes $7$ exchanges of fermionic operators for the $t$-channel, sign $-1$, and $6$ for the $u$-channel, sign $+1$. **The two diagrams enter with a relative minus sign.**
>
> *Equivalently,* this is [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]] (the relative sign from Fermi statistics); its second route counts the exchanges in the same way for the bra $\langle0|\hat a_{k'}\hat a_{p'}$ (Problem Set 9, Problem 4(a)) and finds $6$ and $5$: the same relative sign, the opposite overall sign (next caution).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* order $g^2$; the relative sign for any order of the external states, the two individual signs for the order stated.
>
> *Source: PHY 513, Problem Set 11, Problem 1(f) (the user's solution, the two contraction patterns and paragraph "Relative sign") · checked as parities of permutations (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-6

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(f), paragraph "Relative sign".
>
> **Step 1** (the string). With $|pk\rangle = \hat a^\dagger_p\hat a^\dagger_k|0\rangle$ and $\langle p'k'| = \langle0|\,\hat a_{p'}\hat a_{k'}$ (normalization factors suppressed), the fermionic operators in the matrix element appear in the order
>
> $$
> \hat a_{p'}\;\hat a_{k'}\;\hat{\bar\psi}(z_1)\;\hat\psi(z_1)\;\hat{\bar\psi}(z_2)\;\hat\psi(z_2)\;\hat a^\dagger_p\;\hat a^\dagger_k ,
> $$
>
> and $\hat\phi$ commutes with all of them. Each contraction is evaluated once its two operators are adjacent, and every exchange of two adjacent fermionic operators gives a factor $-1$.
>
> **Step 2** (the $t$-channel). The pairs are $(\hat a_{p'}\hat{\bar\psi}(z_1))$, $(\hat\psi(z_1)\hat a^\dagger_p)$, $(\hat a_{k'}\hat{\bar\psi}(z_2))$, $(\hat\psi(z_2)\hat a^\dagger_k)$. Moving $\hat a^\dagger_p$ to the left past $\hat\psi(z_2)$ and $\hat{\bar\psi}(z_2)$ (2 exchanges),
>
> $$
> \hat a_{p'}\;\hat a_{k'}\;\hat{\bar\psi}(z_1)\;\hat\psi(z_1)\;\hat a^\dagger_p\;\hat{\bar\psi}(z_2)\;\hat\psi(z_2)\;\hat a^\dagger_k ,
> $$
>
> then $\hat a_{p'}$ to the right past $\hat a_{k'}$ (1 exchange), and then $\hat a_{k'}$ to the right past $\hat a_{p'}$, $\hat{\bar\psi}(z_1)$, $\hat\psi(z_1)$, $\hat a^\dagger_p$ (4 exchanges),
>
> $$
> \bigl(\hat a_{p'}\hat{\bar\psi}(z_1)\bigr)\bigl(\hat\psi(z_1)\hat a^\dagger_p\bigr)\bigl(\hat a_{k'}\hat{\bar\psi}(z_2)\bigr)\bigl(\hat\psi(z_2)\hat a^\dagger_k\bigr) .
> $$
>
> This is $7$ exchanges, so the sign is $-1$.
>
> **Step 3** (the $u$-channel). The pairs are $(\hat a_{k'}\hat{\bar\psi}(z_1))$, $(\hat\psi(z_1)\hat a^\dagger_p)$, $(\hat a_{p'}\hat{\bar\psi}(z_2))$, $(\hat\psi(z_2)\hat a^\dagger_k)$. Moving $\hat a^\dagger_p$ to the left as before (2 exchanges) and then $\hat a_{p'}$ to the right past $\hat a_{k'}$, $\hat{\bar\psi}(z_1)$, $\hat\psi(z_1)$, $\hat a^\dagger_p$ (4 exchanges),
>
> $$
> \bigl(\hat a_{k'}\hat{\bar\psi}(z_1)\bigr)\bigl(\hat\psi(z_1)\hat a^\dagger_p\bigr)\bigl(\hat a_{p'}\hat{\bar\psi}(z_2)\bigr)\bigl(\hat\psi(z_2)\hat a^\dagger_k\bigr) .
> $$
>
> This is $6$ exchanges, so the sign is $+1$. The two diagrams therefore enter with a relative minus sign.
>
> **What the derivation shows**
> - Only the parity of the count matters: the sign is that of the permutation that takes the string of Step 1 to the paired order.

^der-c8b-11-6

*Uses:* [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]

> [!caution] Caution: The order of the bra in Problem Set 11
> The solution writes the final state as $\langle p'k'| = \langle0|\,\hat a_{p'}\hat a_{k'}$, the labels in the order written. The course convention takes each bra to be the adjoint of its ket, $\langle p'k'| = \bigl(\hat a^\dagger_{p'}\hat a^\dagger_{k'}|0\rangle\bigr)^\dagger = \langle0|\,\hat a_{k'}\hat a_{p'}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]; PS (4.118)), and PS (4.119), to which the statement of the problem refers, is written for it: there the $t$-term carries $+$ and the $u$-term $-$ ([[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]]). This is a choice of convention, not a slip: the exchange counts above are those of the bra as written. The two bras differ by a factor $-1$ ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign]]), so:
> 1. the relative sign of the two diagrams, every $|\mathcal M_{\lambda'\mu';\lambda\mu}|^2$ and the spin average are the same for both;
> 2. every helicity amplitude of this section has the sign opposite to the one that follows from PS (4.119) with the same spinor phases: there $\mathcal M_{RR;LL} = \mathcal M_{LL;RR} = -2g^2$ and the four others are $+g^2$.
>
> The signs of the individual amplitudes also depend on the phases of the two-spinors ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]], 3). The same order of the bra is used in [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-1|Theorem §C8b.12.1]].
>
> *Source: PHY 513, Problem Set 11, Problem 1(f) (the user's solution, paragraph "Relative sign"; line 469 of its tex source, `qft-C/lectures/hw11_user.tex`) against PS §4.7, eqs. (4.118)–(4.119) and [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] · both sign assignments checked (`qft-C/tools/hw11/verify.py`) · recorded in `qft-C/ERRATA.md`*

^cau-c8b-11-1

> [!theorem] Theorem §C8b.11.7: The Scalar Propagators at High Energy
> In the two diagrams of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]] the momentum through the scalar line is $q = p - p'$ ($t$-channel) and $q = p - k'$ ($u$-channel). In the centre-of-mass frame, for $M^2 \ll E^2$ and with $m_\phi^2$ neglected,
>
> $$
> (p - p')^2 \to -4E^2\sin^2\frac\theta2 , \qquad (p - k')^2 \to -4E^2\cos^2\frac\theta2 ,
> $$
>
> so the propagators are
>
> $$
> t\text{-channel: } \frac{i}{-4E^2\sin^2\frac\theta2} , \qquad u\text{-channel: } \frac{i}{-4E^2\cos^2\frac\theta2} .
> $$
>
> For $\theta \ne 0, \pi$ both denominators are strictly negative and of order $E^2$: they do not vanish, $m_\phi^2$ may be neglected against them, and the limit $\varepsilon \to 0$ may be taken.
>
> *Equivalently,* these are $t = -2\mathbf p^2(1 - \cos\theta)$ and $u = -2\mathbf p^2(1 + \cos\theta)$ of [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]] at $|\mathbf p| \to E$, in the labels $p, k \to p', k'$ of this section.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (the scalar line, [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]]); *applies:* centre-of-mass frame, $E \gg M, m_\phi$, $\theta \ne 0, \pi$.
>
> *Source: PHY 513, Problem Set 11, Problem 1(f) (statement: "with $\theta \ne 0, \pi$ … You may neglect the mass $m_\phi^2$ of the boson as well in this limit"; the user's solution, paragraph "Propagators")*

^thm-c8b-11-7

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(f), paragraph "Propagators".
>
> **Step 1** (the line). The $\hat\phi$–$\hat\phi$ contraction gives the scalar propagator $\dfrac{i}{q^2 - m_\phi^2 + i\varepsilon}$, and the $z_1$, $z_2$ integrals of the plane waves fix the momentum $q$ through the scalar line and leave $(2\pi)^4\delta^{(4)}(p + k - p' - k')$:
>
> $$
> t\text{-channel: } q = p - p' , \qquad u\text{-channel: } q = p - k' .
> $$
>
> **Step 2** (the products). With $p^2 = p'^2 = k'^2 = M^2$, all energies equal to $E$, and $\mathbf k' = -\mathbf p'$,
>
> $$
> p\cdot p' = E^2 - |\mathbf p|^2\cos\theta , \qquad p\cdot k' = E^2 + |\mathbf p|^2\cos\theta .
> $$
>
> **Step 3** (the squares). With $M^2 \ll E^2$ and $|\mathbf p| \to E$,
>
> $$
> (p - p')^2 = 2M^2 - 2\,p\cdot p' \to -2E^2(1 - \cos\theta) = -4E^2\sin^2\frac\theta2 , \qquad (p - k')^2 = 2M^2 - 2\,p\cdot k' \to -2E^2(1 + \cos\theta) = -4E^2\cos^2\frac\theta2 .
> $$
>
> **Step 4** (what may be dropped). Both are of order $E^2$, so $m_\phi^2$ is neglected, and for $\theta \ne 0, \pi$ both are strictly negative, so the denominators do not vanish and the limit $\varepsilon \to 0$ can be taken. This gives the two propagators of the statement.

^der-c8b-11-7

*Uses:* [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]]

> [!theorem] Theorem §C8b.11.8: The Amplitudes ℳ_RR;LL and ℳ_LR;LR
> In the high-energy limit at fixed $\theta \ne 0, \pi$, with the signs of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|Theorem §C8b.11.6]] and the phases of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]]:
> 1. each diagram contributes its sign from the exchanges, $(-ig)^2 = -g^2$, its spinor factor, and its propagator;
> 2. the spinor factors are
>
> $$
> \begin{aligned}
> \mathcal M_{RR;LL}:\quad & t:\ \bar u_R(p')u_L(p)\,\bar u_R(k')u_L(k) = -4E^2\sin^2\frac\theta2 , & u:\ \bar u_R(p')u_L(k)\,\bar u_R(k')u_L(p) = 4E^2\cos^2\frac\theta2 ,\\
> \mathcal M_{LR;LR}:\quad & t:\ 0 , & u:\ \bar u_L(p')u_R(k)\,\bar u_R(k')u_L(p) = -4E^2\cos^2\frac\theta2 ;
> \end{aligned}
> $$
>
> 3. the amplitudes are
>
> $$
> \mathcal M_{RR;LL} = 2g^2 , \qquad \mathcal M_{LR;LR} = -g^2 .
> $$
>
> They depend neither on the energy nor on the angle: in each diagram the spinor factor is, up to its sign, the denominator of the propagator.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* order $g^2$, centre-of-mass frame, $E \gg M$, $m_\phi$ neglected, $\theta \ne 0, \pi$; the signs for the bra and the phases stated ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^cau-c8b-11-1|Caution: The order of the bra in Problem Set 11]]).
>
> *Source: PHY 513, Problem Set 11, Problem 1(f) (the user's solution, paragraphs "Spinors" and "Amplitudes") · checked numerically, also with exact spinors of mass $M$ and a scalar of mass $m_\phi$ at increasing $E/M$ (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-8

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(f), paragraphs "Spinors" and "Amplitudes".
>
> **Step 1** (spinors). Each vertex contributes $-ig$ times the bilinear $\bar u(\text{out})\,u(\text{in})$ of its two fermions, given by part (e) and, for $\bar u_L(p')\,u_R(k)$, by $\bigl(\bar u_a\,u_b\bigr)^{\ast} = \bar u_b\,u_a$ ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5|Theorem §C8b.11.5]]). For the two amplitudes,
>
> $$
> \begin{aligned}
> \mathcal M_{RR;LL}:\quad t:\ & \bar u_R(p')u_L(p)\,\bar u_R(k')u_L(k) = \Bigl(2E\sin\frac\theta2\Bigr)\Bigl(-2E\sin\frac\theta2\Bigr) = -4E^2\sin^2\frac\theta2 ,\\
> u:\ & \bar u_R(p')u_L(k)\,\bar u_R(k')u_L(p) = \Bigl(-2E\cos\frac\theta2\Bigr)\Bigl(-2E\cos\frac\theta2\Bigr) = 4E^2\cos^2\frac\theta2 ,\\
> \mathcal M_{LR;LR}:\quad u:\ & \bar u_L(p')u_R(k)\,\bar u_R(k')u_L(p) = \Bigl(2E\cos\frac\theta2\Bigr)\Bigl(-2E\cos\frac\theta2\Bigr) = -4E^2\cos^2\frac\theta2 ,
> \end{aligned}
> $$
>
> and the $t$-channel of $\mathcal M_{LR;LR}$ vanishes by part (b).
>
> **Step 2** (amplitudes). Each diagram contributes its sign from the exchanges ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|Theorem §C8b.11.6]]), $(-ig)^2 = -g^2$, its spinor factor, and its propagator ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-7|Theorem §C8b.11.7]]). Hence
>
> $$
> \begin{aligned}
> i\mathcal M_{RR;LL} &= (-1)(-g^2)\Bigl(-4E^2\sin^2\frac\theta2\Bigr)\frac{i}{-4E^2\sin^2\frac\theta2} + (+1)(-g^2)\Bigl(4E^2\cos^2\frac\theta2\Bigr)\frac{i}{-4E^2\cos^2\frac\theta2}\\
> &= ig^2 + ig^2 = 2ig^2 ,\\
> i\mathcal M_{LR;LR} &= (+1)(-g^2)\Bigl(-4E^2\cos^2\frac\theta2\Bigr)\frac{i}{-4E^2\cos^2\frac\theta2} = -ig^2 ,
> \end{aligned}
> $$
>
> so $\mathcal M_{RR;LL} = 2g^2$ and $\mathcal M_{LR;LR} = -g^2$. (End of the user's solution of part (f).)
>
> **What the derivation shows**
> - ⚑ By-product: in $\mathcal M_{RR;LL}$ the two diagrams add. The relative minus sign of Fermi statistics is compensated by the opposite signs of the two spinor factors, $-4E^2\sin^2\frac\theta2$ against $+4E^2\cos^2\frac\theta2$.
> - The factor $\sin^2\frac\theta2$ of the $t$-channel spinors cancels the forward pole of its propagator, and $\cos^2\frac\theta2$ the backward pole of the $u$-channel: the helicity flip that the scalar vertex forces is what removes the peaks ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5|Theorem §C8b.11.5]], items 1–2).

^der-c8b-11-8

*Uses:* [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5|Theorem §C8b.11.5]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|Theorem §C8b.11.6]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-7|Theorem §C8b.11.7]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-7|P9, step 7]]

> [!theorem] Theorem §C8b.11.9: The Six Helicity Amplitudes of ff → ff in Yukawa Theory
> In the high-energy limit, with the signs and phases of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-8|Theorem §C8b.11.8]],
>
> $$
> \mathcal M_{RR;LL} = \mathcal M_{LL;RR} = 2g^2 , \qquad \mathcal M_{LR;LR} = \mathcal M_{RL;RL} = \mathcal M_{LR;RL} = \mathcal M_{RL;LR} = -g^2 ,
> $$
>
> and the other ten amplitudes vanish ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]]).
>
> | amplitude | diagrams | spinor factor $t$ | spinor factor $u$ | $\mathcal M$ |
> |---|---|---|---|---|
> | $\mathcal M_{RR;LL}$ | both | $-4E^2\sin^2\frac\theta2$ | $4E^2\cos^2\frac\theta2$ | $2g^2$ |
> | $\mathcal M_{LL;RR}$ | both | $-4E^2\sin^2\frac\theta2$ | $4E^2\cos^2\frac\theta2$ | $2g^2$ |
> | $\mathcal M_{LR;RL}$ | $t$ only | $4E^2\sin^2\frac\theta2$ | — | $-g^2$ |
> | $\mathcal M_{RL;LR}$ | $t$ only | $4E^2\sin^2\frac\theta2$ | — | $-g^2$ |
> | $\mathcal M_{RL;RL}$ | $u$ only | — | $-4E^2\cos^2\frac\theta2$ | $-g^2$ |
> | $\mathcal M_{LR;LR}$ | $u$ only | — | $-4E^2\cos^2\frac\theta2$ | $-g^2$ |
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* as for [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-8|Theorem §C8b.11.8]].
>
> *Source: PHY 513, Problem Set 11, Problem 1(g) (the user's solution; the first and the last row are part (f)) · all sixteen amplitudes checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-9

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(g), up to its last display.
>
> By part (b), only the six amplitudes listed there contribute. Besides $\mathcal M_{RR;LL}$ and $\mathcal M_{LR;LR}$ from part (f), the other four are computed in the same way, with the signs, propagators and kinematics of part (f). By part (d), $\bar u_R(b)\,u_L(a) = 2E\,\xi_+^\dagger(b)\,\xi_-(a)$ and $\bar u_L(b)\,u_R(a) = 2E\,\xi_-^\dagger(b)\,\xi_+(a)$, with the spinors of the table in part (e), all of whose entries are real.
>
> **Step 1** ($\mathcal M_{LL;RR}$, both diagrams).
>
> $$
> \begin{aligned}
> t:\quad & \bar u_L(p')u_R(p)\,\bar u_L(k')u_R(k) = 2E\,(-s,\ c)\begin{pmatrix}1\\ 0\end{pmatrix}\cdot2E\,(c,\ s)\begin{pmatrix}0\\ 1\end{pmatrix} = (-2Es)(2Es) = -4E^2\sin^2\frac\theta2 ,\\
> u:\quad & \bar u_L(p')u_R(k)\,\bar u_L(k')u_R(p) = 2E\,(-s,\ c)\begin{pmatrix}0\\ 1\end{pmatrix}\cdot2E\,(c,\ s)\begin{pmatrix}1\\ 0\end{pmatrix} = (2Ec)(2Ec) = 4E^2\cos^2\frac\theta2 ,
> \end{aligned}
> $$
>
> $$
> i\mathcal M_{LL;RR} = (-1)(-g^2)\Bigl(-4E^2\sin^2\frac\theta2\Bigr)\frac{i}{-4E^2\sin^2\frac\theta2} + (+1)(-g^2)\Bigl(4E^2\cos^2\frac\theta2\Bigr)\frac{i}{-4E^2\cos^2\frac\theta2} = 2ig^2 .
> $$
>
> **Step 2** ($\mathcal M_{LR;RL}$, $t$-channel only).
>
> $$
> \bar u_L(p')u_R(p)\,\bar u_R(k')u_L(k) = (-2Es)(-2Es) = 4E^2\sin^2\frac\theta2 , \qquad i\mathcal M_{LR;RL} = (-1)(-g^2)\Bigl(4E^2\sin^2\frac\theta2\Bigr)\frac{i}{-4E^2\sin^2\frac\theta2} = -ig^2 .
> $$
>
> **Step 3** ($\mathcal M_{RL;LR}$, $t$-channel only).
>
> $$
> \bar u_R(p')u_L(p)\,\bar u_L(k')u_R(k) = (2Es)(2Es) = 4E^2\sin^2\frac\theta2 , \qquad i\mathcal M_{RL;LR} = (-1)(-g^2)\Bigl(4E^2\sin^2\frac\theta2\Bigr)\frac{i}{-4E^2\sin^2\frac\theta2} = -ig^2 .
> $$
>
> **Step 4** ($\mathcal M_{RL;RL}$, $u$-channel only).
>
> $$
> \bar u_R(p')u_L(k)\,\bar u_L(k')u_R(p) = (-2Ec)(2Ec) = -4E^2\cos^2\frac\theta2 , \qquad i\mathcal M_{RL;RL} = (+1)(-g^2)\Bigl(-4E^2\cos^2\frac\theta2\Bigr)\frac{i}{-4E^2\cos^2\frac\theta2} = -ig^2 .
> $$
>
> **Step 5** (collect). Together with part (f), $\mathcal M_{RR;LL} = \mathcal M_{LL;RR} = 2g^2$ and $\mathcal M_{LR;LR} = \mathcal M_{RL;RL} = \mathcal M_{LR;RL} = \mathcal M_{RL;LR} = -g^2$.
>
> **What the derivation shows**
> - Reversing all four helicities leaves each amplitude unchanged: $\mathcal M_{LL;RR} = \mathcal M_{RR;LL}$, $\mathcal M_{RL;LR} = \mathcal M_{LR;RL}$, $\mathcal M_{RL;RL} = \mathcal M_{LR;LR}$ (compare the parity relation of ★ [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-9|Theorem §C8b.8.9]] for QED).
> - Where one diagram contributes, the amplitude is $-g^2$ whichever diagram it is; where both contribute, $2g^2$.

^der-c8b-11-9

*Uses:* [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-3|Theorem §C8b.11.3]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-4|Theorem §C8b.11.4]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-6|Theorem §C8b.11.6]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-7|Theorem §C8b.11.7]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-8|Theorem §C8b.11.8]]

> [!theorem] Theorem §C8b.11.10: The Spin Average of the Squared Amplitude, by Explicit Averaging
> The spin average averages over the $2 \times 2 = 4$ helicity combinations of the incoming fermions and sums over those of the outgoing fermions,
>
> $$
> \overline{|\mathcal M|^2} = \frac14\sum_{\lambda, \mu}\sum_{\lambda', \mu'}\bigl|\mathcal M_{\lambda'\mu';\lambda\mu}\bigr|^2 ,
> $$
>
> and with the six amplitudes of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-9|Theorem §C8b.11.9]],
>
> $$
> \overline{|\mathcal M|^2} = \frac14\bigl(2\cdot4g^4 + 4\cdot g^4\bigr) = 3g^4 .
> $$
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* order $g^2$, $E \gg M$, $m_\phi$ neglected, $\theta \ne 0, \pi$; independent of the order of the bra and of the phases of the two-spinors.
>
> *Source: PHY 513, Problem Set 11, Problem 1(g) (statement: "Determine the spin-averaged form of the amplitude squared, by explicit averaging of the amplitudes found in (f)"; the user's solution) · checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-11-10

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(g), first and last displays.
>
> **Step 1** (the average). The spin average averages over the $2 \times 2 = 4$ helicity combinations of the incoming fermions and sums over those of the outgoing fermions: the first display of the statement.
>
> **Step 2** (the terms). By part (b), only the six amplitudes of [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-9|Theorem §C8b.11.9]] contribute: two of modulus $2g^2$, each giving $4g^4$, and four of modulus $g^2$, each giving $g^4$.
>
> **Step 3** (the sum). $\overline{|\mathcal M|^2} = \frac14\bigl(2\cdot4g^4 + 4\cdot g^4\bigr) = \frac14\cdot12g^4 = 3g^4$. (End of the user's solution of Problem 1.)

^der-c8b-11-10

*Uses:* [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-9|Theorem §C8b.11.9]]

> [!remark] Remark: Yukawa and QED side by side
> The two theories differ at the vertex by one $\gamma$, and their helicity amplitudes are complementary:
>
> | | scalar exchange (Yukawa) | photon exchange (QED) |
> |---|---|---|
> | bilinear at the vertex | $\bar u(\text{out})\,u(\text{in})$, no $\gamma$ | $\bar u(\text{out})\gamma^\mu u(\text{in})$, one $\gamma$ |
> | helicity along a fermion line at high energy | flips ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10\|Theorem §C8b.6.10]]) | is kept ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4\|Theorem §C8b.6.4]]) |
> | vertex at zero deflection | zero: $2E\,\xi_\pm^\dagger\xi_\mp = 0$ ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-5\|Theorem §C8b.11.5]]) | $2p^\mu\delta_{\lambda\lambda'}$ ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2\|Theorem §C8b.12.2]]) |
> | near the forward and backward directions | the spinor factors cancel the poles of the propagators; the amplitudes are constants ([[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-8\|Theorem §C8b.11.8]]) | the helicity-keeping amplitudes grow like $1/\theta^2$ and $1/(\pi - \theta)^2$ ([[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3\|Theorem §C8b.12.3]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-4\|Theorem §C8b.12.4]]) |
>
> *Source: the homes linked in each row (Problem Set 11, Problems 1 and 2, the user's solutions)*

^rem-c8b-11-1

> [!remark]- Connections
> - The amplitude whose helicity components are computed here, with its two diagrams and their relative sign — [[§C6d.5 Second Order#^ex-c6d-5-2|Example §C6d.5.2]], [[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]]; the rules — [[§C6d.6 Momentum-Space Feynman Rules#^thm-c6d-6-2|Theorem §C6d.6.2]].
> - The selection rule of the scalar vertex and the general rule for any number of $\gamma$'s — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|Theorem §C8b.6.11]].
> - The helicity two-spinors and the high-energy limit of the helicity spinors — [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]; the same two-spinors for $e^+e^- \to \mu^+\mu^-$ — [[§C8b.5 Helicity Spinors and the Massless Limit#^ex-c8b-5-1|Example §C8b.5.1]].
> - Explicit helicity spinors in QED, where each vertex is a four-vector instead of a number — [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]; the same process with a photon in place of the scalar — [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering|§C8b.12]].
> - The $t$- and $u$-channel propagators and where each is largest — [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^ex-c8a-14-1|Example §C8a.14.1]], [[§C8a.14 Crossing Symmetry and Mandelstam Variables#^thm-c8a-14-7|Theorem §C8a.14.7]].
> - The recipe — [[P9 Helicity Amplitudes|P9]].
