---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.3
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.2 Transition Probabilities in a Box]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.4 Two-Body Scattering Kinematics]] →

*Sources: Yu Zhao-Huan, 量子场论讲义, §6.5.2 "散射截面", pp. 242–246, eqs. (6.307)–(6.331), Fig. 6.4 (page images checked, PDF pp. 250–254) · PHY 513 Lecture 15 (Larsen, 28 Oct 2026), Part A, slide 8 ("Cross-section … is a universal event rate"), slides 16, 20, 24, and transcript · the user's PHY 513 notes, Ch. 15 §15.2 (paragraph "Event counting (filled in)"), §15.5, §15.6 (eq. (moller)), §15.10 (paragraph "Correspondence with Yu") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.5, pp. 99–101, 106, eqs. (4.59)–(4.61), (4.79)–(4.80).*

**What is prepared.** A beam of particles $B$, all with the same velocity, falls on a target of particles $A$ at rest ([[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]). **What is measured.** The number $N$ of scattering events, with the final particles in a given range of momenta, during a time $t$. The cross section is that count with the beam and the target divided out ([[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]]). Applied to one $A$ and one $B$ in the box of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]], it is the rate of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]] divided by the flux, and the last power of the box volume cancels ([[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]]). The Møller velocity makes the result Lorentz invariant ([[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]]); for collinear beams it is the velocity difference $|\mathbf v_A - \mathbf v_B|$ ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]]), and the differential cross section ([[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]]) is the formula of the lecture. The section ends with that formula written once, every factor labelled by the box that produced it. Along the way the section collects what the cross section needs in every frame: the flux factor in invariant form ([[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]]), the phase space and its invariance ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]]), the dimension of $d\sigma$ ([[§C6b.3 The Cross Section#^thm-c6b-3-11|Theorem §C6b.3.11]]), and the centre-of-mass frame with the threshold of a process ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]], [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]]). Yu §6.5.2 is followed step by step; the course's own derivation of the same formula, with wave packets, comes after the decays, in [[§C6b.8 Wave Packets and the Cross Section|§C6b.8]]–[[§C6b.9 Evaluating the Cross Section|§C6b.9]].

*Conventions* ([[Larsen PHY 513]]): $\mathbf v = \mathbf p/E = \partial E_{\mathbf p}/\partial\mathbf p$, the group velocity of a packet peaked at $\mathbf p$; $a$ is the cross-sectional area of the beam (Yu: $A$) and $V$ the volume it sweeps (Yu: $V$), not the box volume $\tilde V$; $\mathcal R$ is a rate per unit volume, $R$ the rate of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]] ([[§C6b.2 Transition Probabilities in a Box#^cau-c6b-2-1|§C6b.2, Caution: Names in Yu's §6.5.1]]); $S_{\rm id}$ the identical-particle factor.

## The model and the definitions

> [!model] Model §C6b.3.1: Beam on a Fixed Target
> - *Target:* $N_A$ particles $A$ at rest, filling the volume $V$ with density $n_A = N_A/V$.
> - *Beam:* particles $B$ with one common velocity $\mathbf v_B = \mathbf p_B/E_B$, density $n_B$ (particles per volume), cross-sectional area $a$.
> - *Independence:* every event is one $A$ and one $B$ scattering once; the target is thin, so the beam is not depleted and no particle scatters twice; the targets do not shadow each other.
> - *Count:* $N$ = the number of events, with final momenta in a given range, in a time $t$.
> - *Each collision:* one $A$ and one $B$ in a box of volume $\tilde V$, [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], with its Hamiltonian, free states and range of validity.
>
> *Source: Yu §6.5.2, pp. 242–243, Fig. 6.4 ("束流打靶实验"), eqs. (6.307)–(6.308) · PHY 513 Lecture 15, slide 8 · PS §4.5, pp. 99–100*

^mod-c6b-3-1

> [!definition] Definition §C6b.3.1: Flux
> The **flux** (流密度) of the beam is the number of $B$ particles crossing unit area per unit time. The particles that cross the area $a$ in the time $t$ fill the cylinder of volume $a|\mathbf v_B|t$ behind it, $N_B = n_Ba|\mathbf v_B|t$, so
>
> $$
> j_B \equiv \frac{N_B}{a\,t} = \frac{n_Ba|\mathbf v_B|t}{a\,t} = n_B\,|\mathbf v_B| .
> $$
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]].
>
> *Source: Yu §6.5.2, eq. (6.307) (page image checked)*

^def-c6b-3-1

> [!caution] Caution: The beam density n_B is per unit volume in the box route
> Here $n_B$ is Yu's density, the number of beam particles per unit volume ([[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]), $[n_B] = 3$, and the flux is $j_B = n_B|\mathbf v_B|$ ([[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]]). The wave-packet route follows PS and uses the same letter for the number of $B$ particles per unit transverse area that pass the target in the time $t$, $n_B = j_Bt$, $[n_B] = 2$ ([[§C6b.8 Wave Packets and the Cross Section#^cau-c6b-8-3|§C6b.8, Caution: The beam density n_B is per unit area in the wave-packet route]]): that $n_B$ is this one times $|\mathbf v_B|\,t$. PS write the volume densities $\rho_{\mathcal A}$, $\rho_{\mathcal B}$ (eq. (4.59)). The flux $j_B$ and the cross section mean the same in both routes.
>
> *Source: Yu §6.5.2, eq. (6.307) · PS §4.5, eq. (4.59), p. 105*

^cau-c6b-3-3

> [!definition] Definition §C6b.3.2: Cross Section (Operational)
> The **cross section** $\sigma$ is the constant of proportionality in
>
> $$
> N = N_A\,j_B\,\sigma\,t ;
> $$
>
> it is an area, the effective area that one target particle presents to the beam (散射截面, "相当于发生散射的有效面积"). Unit: the barn, $1\,\mathrm b = 10^{-28}\,\mathrm m^2$; in natural units $1\,\mathrm b = 2.568\times10^3\,\mathrm{GeV}^{-2}$ and $1\,\mathrm{GeV}^{-2} = 3.894\times10^{-4}\,\mathrm b = 0.3894\,\mathrm{mb}$. When only final momenta in a range are counted, the constant is the differential cross section $d\sigma$.
>
> This is the course's definition of the cross section as a universal event rate, [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-1|Def. §C6b.8.1]] (slide 8), stated for Yu's set-up: the same $N_{\rm events} = \sigma N_Aj_Bt$.
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]].
>
> *Source: Yu §6.5.2, eqs. (6.308)–(6.311) (page image checked) · PHY 513 Lecture 15, slide 8 · PS §4.5, eqs. (4.59)–(4.61)*

^def-c6b-3-2

## From the box rate to the cross section

> [!theorem] Theorem §C6b.3.2: Events per Unit Volume and Time
> The number of events per unit volume and unit time is
>
> $$
> \mathcal R \equiv \frac{N}{V\,t} = n_A\,n_B\,\sigma\,|\mathbf v_B| .
> $$
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]].
>
> *Source: Yu §6.5.2, eq. (6.312) (page image checked)*

^thm-c6b-3-2

> [!derivation]- Derivation
> **Step 1** (insert the definitions). [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]], then [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], then $n_A = N_A/V$ ([[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]]):
>
> $$
> \frac{N}{Vt} = \frac{N_Aj_B\sigma t}{Vt} = \frac{N_Aj_B\sigma}{V} = \frac{N_An_B|\mathbf v_B|\sigma}{V} = n_An_B\sigma|\mathbf v_B| .
> $$
>
> **What the derivation shows.**
> - $\mathcal R$ is symmetric in the two densities: per unit volume, the event rate is $\sigma$ times the product of the densities times the speed at which the two populations pass through each other.

^der-c6b-3-2

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]]

> [!theorem] Theorem §C6b.3.3: One Particle of Each Kind in the Box
> For one particle $A$ and one particle $B$ in the box of [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], each a plane wave spread uniformly over the volume $\tilde V$,
>
> $$
> n_A = n_B = \frac{1}{\tilde V} , \qquad j_B = n_B\,|\mathbf v_B| = \frac{|\mathbf v_B|}{\tilde V} , \qquad \mathcal R = \frac{R}{\tilde V} ,
> $$
>
> with $j_B$ the flux of [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], $\mathcal R$ the events per unit volume and time of [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] and $R$ the total rate of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]].
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] with $N_A = 1$ and a single beam particle, in the box of [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* plane waves (uniform densities), as there.
>
> *Source: Yu §6.5.2, before eq. (6.313) (page image checked: "可以看作在全空间体积 $\tilde V$ 中仅有这两个粒子，因而 $n_{\mathcal A} = n_{\mathcal B} = 1/\tilde V$，此时 $\mathcal R$ 可以用单位时间内的跃迁概率 $R$ 表示为 $\mathcal R = R/\tilde V$")*

^thm-c6b-3-3

> [!derivation]- Derivation
> **Step 1** (densities). One particle in the volume $\tilde V$, with a uniform probability density (a plane wave, [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], *Space*): the number per unit volume is $n_A = 1/\tilde V$, and the same for $B$.
>
> **Step 2** (flux). [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]] with $n_B = 1/\tilde V$: $j_B = n_B|\mathbf v_B| = |\mathbf v_B|/\tilde V$.
>
> **Step 3** (rate per volume). In a time $t$ the pair produces $N = Rt$ events ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]: $R$ is the transition probability per unit time, summed over the final states), all within the box, so
>
> $$
> \mathcal R = \frac{N}{\tilde V\,t} = \frac{Rt}{\tilde V\,t} = \frac{R}{\tilde V} .
> $$
>
> **What the derivation shows.**
> - This is Step 1 of [[§C6b.3 The Cross Section#^der-c6b-3-4|Derivation §C6b.3.4]]: inserted into [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] it turns the rate of the box into a cross section.
> - The careful route replaces the uniform density $1/\tilde V$ by an integral over impact parameters at unit density ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-4|Theorem §C6b.8.4]]).

^der-c6b-3-3

*Uses:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]

> [!theorem] Theorem §C6b.3.4: The Cross Section in the Rest Frame of A
> With $R$ the total rate of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]],
>
> $$
> \sigma = \frac{R\,\tilde V}{|\mathbf v_B|} = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_B|\mathbf v_B|}\;\prod_{j=1}^n\int\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2 .
> $$
>
> The box volume $\tilde V$ and the duration $\tilde T$ have cancelled: the result is finite and independent of the regularization.
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] with one $A$ and one $B$ in the box of [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there; $A$ at rest.
>
> *Source: Yu §6.5.2, eq. (6.313) (page image checked; "上式对 $\mathcal A$ 粒子静止的参考系成立")*

^thm-c6b-3-4

> [!derivation]- Derivation
> **Step 1** (one of each in the box). One $A$ and one $B$ in the volume $\tilde V$: $n_A = n_B = 1/\tilde V$. Their single event rate $R$ ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]) is spread over the box, so the rate per unit volume is $\mathcal R = R/\tilde V$ (Yu, before (6.313); [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]]).
>
> **Step 2** (solve for $\sigma$). [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]] solved for $\sigma$, with Step 1:
>
> $$
> \sigma = \frac{\mathcal R}{n_An_B|\mathbf v_B|} = \frac{R}{\tilde V}\cdot\frac{1}{\tilde V^{-1}\tilde V^{-1}|\mathbf v_B|} = \frac{R}{\tilde V}\cdot\frac{\tilde V^2}{|\mathbf v_B|} = \frac{R\,\tilde V}{|\mathbf v_B|} .
> $$
>
> Equivalently: the rate per target particle is $\sigma j_B$ ([[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]] with $N_A = 1$), and $j_B = n_B|\mathbf v_B| = |\mathbf v_B|/\tilde V$ ([[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]]), so $\sigma = R/j_B = R\tilde V/|\mathbf v_B|$.
>
> **Step 3** (insert the rate). [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]] has the prefactor $\frac{1}{S_{\rm id}}\frac{1}{4E_AE_B\tilde V}$; multiplied by $\tilde V/|\mathbf v_B|$ it becomes $\frac{1}{S_{\rm id}}\frac{1}{4E_AE_B|\mathbf v_B|}$, the statement (Yu (6.313)).
>
> **Step 4** (bookkeeping of the box). Every power of $\tilde V$ and $\tilde T$ along the chain of [[§C6b.2 Transition Probabilities in a Box|§C6b.2]]:
>
> | step | factor | power of $\tilde V$ | power of $\tilde T$ |
> |---|---|---|---|
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]] | $(2\pi)^4\delta^4(0) = \tilde V\tilde T$ | $+1$ | $+1$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4\|Theorem §C6b.2.4]], 2 | $1/\langle i\vert i\rangle = 1/(4E_AE_B\tilde V^2)$ | $-2$ | $0$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4\|Theorem §C6b.2.4]], 3 | $1/\langle f\vert f\rangle = 1/\prod_j(2E_j\tilde V)$ | $-n$ | $0$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-5\|Theorem §C6b.2.5]] | per unit time, $1/\tilde T$ | $0$ | $-1$ |
> | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6\|Theorem §C6b.2.6]] | states in the range, $\prod_j\tilde V\,d^3p_j/(2\pi)^3$ | $+n$ | $0$ |
> | this theorem | per unit flux, $\tilde V/\lvert\mathbf v_B\rvert$ | $+1$ | $0$ |
> | | total | $1 - 2 - n + n + 1 = 0$ | $1 - 1 = 0$ |
>
> **What the derivation shows.**
> - The flux of one plane-wave particle in the box is $|\mathbf v_B|/\tilde V$: its density is uniform, $1/\tilde V$. The careful route makes the same average explicit as an integral over the impact parameter at unit density ([[§C6b.8 Wave Packets and the Cross Section#^thm-c6b-8-4|Theorem §C6b.8.4]]) → [[§C6b.3 The Cross Section#^thm-c6b-3-3|Theorem §C6b.3.3]].
> - The result is finite and independent of the regularization: the box was only bookkeeping.
> - Only $E_B|\mathbf v_B| = |\mathbf p_B|$ and $E_A = m_A$ refer to the rest frame of $A$; the next two theorems remove that restriction.

^der-c6b-3-4

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]], [[§C6b.3 The Cross Section#^def-c6b-3-1|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^def-c6b-3-2|Def. §C6b.3.2]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-5|P7, step 5]]

## Any frame: the Møller velocity

In [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]] everything except the factor $(4E_AE_B|\mathbf v_B|)^{-1}$ is Lorentz invariant: $|\mathcal M|^2$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]]) and the measure ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]). In the rest frame of $A$, $|\mathbf v_B|$ is the speed of $B$ relative to $A$; Yu replaces it by an invariant that takes this value there.

> [!caution] Caution: The flux factor with the velocity difference is not a Lorentz scalar
> In [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]] everything but $(4E_AE_B|\mathbf v_B|)^{-1}$ is invariant, and for general directions of the two momenta $E_AE_B|\mathbf v_A - \mathbf v_B|$ is not a Lorentz invariant (Yu, after (6.314): "$E_{\mathcal A}E_{\mathcal B}v_{\rm rel}$ 并不是 Lorentz 不变量"). It differs from the invariant $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ by the cross product of the velocities ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]]):
>
> $$
> E_A^2E_B^2|\mathbf v_A - \mathbf v_B|^2 = (p_A\cdot p_B)^2 - m_A^2m_B^2 + E_A^2E_B^2|\mathbf v_A\times\mathbf v_B|^2 .
> $$
>
> Example: $A$ at rest and $B$ with momentum $p$ along $x$ give $E_AE_B|\mathbf v_A - \mathbf v_B| = m_Ap$. Boost along $y$ with speed $u$, $\gamma = (1 - u^2)^{-1/2}$: then $E_A' = \gamma m_A$, $\mathbf v_A' = (0, -u, 0)$, $E_B' = \gamma E_B$, $\mathbf p_B' = (p, -\gamma uE_B, 0)$, $\mathbf v_B' = (p/(\gamma E_B), -u, 0)$, so $|\mathbf v_A' - \mathbf v_B'| = p/(\gamma E_B)$ and $E_A'E_B'|\mathbf v_A' - \mathbf v_B'| = \gamma m_Ap \ne m_Ap$. This is why Yu defines $\sigma$ with the Møller velocity ([[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]], [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]]); for collinear beams the two agree ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]], 1), and the course's flux factor is invariant under boosts along the beam ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]]).
>
> *Source: Yu §6.5.2, eq. (6.314) and the sentence after it (page image checked); eqs. (6.322)–(6.329)*

^cau-c6b-3-1

> [!definition] Definition §C6b.3.3: Møller Velocity
> For two particles with four-momenta $p_A$, $p_B$ and masses $m_A$, $m_B$, the **Møller velocity** is
>
> $$
> v_{\rm Møl} \equiv \frac{1}{E_AE_B}\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} .
> $$
>
> *Model:* any (kinematics); *applies:* any on-shell momenta $p_A$, $p_B$, in any inertial frame.
>
> *Source: Yu §6.5.2, eq. (6.315) (page image checked)*

^def-c6b-3-3

> [!theorem] Theorem §C6b.3.5: The Lorentz-Invariant Cross Section
> 1. The incident flux factor $E_AE_Bv_{\rm Møl} = \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ is Lorentz invariant.
> 2. In the rest frame of $A$, $v_{\rm Møl} = |\mathbf v_B|$.
> 3. Hence
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_Bv_{\rm Møl}}\;\prod_{j=1}^n\int\frac{d^3p_j}{(2\pi)^3\,2E_j}\;(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_{j=1}^np_j\Bigr)\,|\mathcal M|^2
> $$
>
> is Lorentz invariant and equals [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]] in the rest frame of $A$. Yu takes it as the definition of $\sigma$ in every frame (eq. (6.316)).
> 4. ★ The number of events per unit volume and time, $\mathcal R = n_An_B\sigma v_{\rm Møl}$, is Lorentz invariant; in the rest frame of $A$ it is [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]].
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] and [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], in any inertial frame; spinless particles (for $|\mathcal M|^2$ invariant).
>
> *Source: Yu §6.5.2, eqs. (6.313)–(6.317) (page image checked; part 4: "而且可以论证 $\mathcal R = n_{\mathcal A}n_{\mathcal B}\sigma v_{\rm Møl}$ 也是 Lorentz 不变的", stated without proof)*

^thm-c6b-3-5

> [!derivation]- Derivation
> **Step 1** (part 1). $p_A\cdot p_B$ and $m_A^2$, $m_B^2$ are Lorentz scalars, so $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}$ is, and by [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]] it equals $E_AE_Bv_{\rm Møl}$.
>
> **Step 2** (part 2). At rest $p_A = (m_A, \mathbf 0)$, so $p_A\cdot p_B = m_AE_B$, $E_A = m_A$, and with $E_B^2 - m_B^2 = |\mathbf p_B|^2$ (Yu (6.317)):
>
> $$
> v_{\rm Møl} = \frac{1}{m_AE_B}\sqrt{m_A^2E_B^2 - m_A^2m_B^2} = \frac{m_A\sqrt{E_B^2 - m_B^2}}{m_AE_B} = \frac{|\mathbf p_B|}{E_B} = |\mathbf v_B| .
> $$
>
> **Step 3** (the rest of the integrand). $|\mathcal M|^2$ is invariant ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]]); each $\frac{d^3p_j}{(2\pi)^32E_j}$ is invariant ([[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]]); and $\delta^4(\Lambda P - \sum_j\Lambda p_j) = |\det\Lambda|^{-1}\delta^4(P - \sum_jp_j) = \delta^4(P - \sum_jp_j)$ ([[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1). The same argument written out for the phase-space integral is [[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]].
>
> **Step 4** (part 3). By Steps 1 and 3 every factor of the expression is invariant. By Step 2 it equals [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]] in the rest frame of $A$ (with $4E_AE_B|\mathbf v_B| = 4E_AE_Bv_{\rm Møl}$ there), hence in every frame it takes the rest-frame value.
>
> **Step 5** (★ part 4). A population with rest-frame density $n_0$ moving with velocity $\mathbf v$ has the current $n^\mu = n_0u^\mu = n_0\gamma(1, \mathbf v)$; its density is the time component, $n = n^0 = n_0\gamma = n_0E/m$ (the volume is length-contracted by $1/\gamma$). So $n/E = n_0/m$ is invariant, and
>
> $$
> n_An_B\,\sigma\,v_{\rm Møl} = \frac{n_A}{E_A}\cdot\frac{n_B}{E_B}\cdot\sigma\cdot E_AE_Bv_{\rm Møl}
> $$
>
> is a product of four invariants (part 1 and part 3). In the rest frame of $A$, $v_{\rm Møl} = |\mathbf v_B|$ (part 2) and the product is $n_An_B\sigma|\mathbf v_B|$ of [[§C6b.3 The Cross Section#^thm-c6b-3-2|Theorem §C6b.3.2]]. Equivalently, $\mathcal R = dN/(d^3x\,dt)$ is a number of events, an invariant, per four-volume $d^4x$, also invariant ($|\det\Lambda| = 1$).
>
> **What the derivation shows.**
> - Yu's choice builds the invariance in; the course instead shows that $E_AE_B|\mathbf v_A - \mathbf v_B|$ is a component of an antisymmetric tensor, invariant under boosts along the beam ([[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]]). For collinear beams the two agree ([[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]]).
> - $E_AE_B|\mathbf v_A - \mathbf v_B|$ alone is not invariant for general directions (Yu, after (6.314): "$E_{\mathcal A}E_{\mathcal B}v_{\rm rel}$ 并不是 Lorentz 不变量") → [[§C6b.3 The Cross Section#^cau-c6b-3-1|§C6b.3, Caution: The flux factor with the velocity difference is not a Lorentz scalar]].

^der-c6b-3-5

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]], [[§C6b.3 The Cross Section#^thm-c6b-3-4|Theorem §C6b.3.4]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-6|Theorem §C6b.1.6]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!theorem] Theorem §C6b.3.6: The Møller Velocity and the Velocity Difference
> With $\mathbf v_A = \mathbf p_A/E_A$, $\mathbf v_B = \mathbf p_B/E_B$,
>
> $$
> v_{\rm Møl} = \sqrt{|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2} .
> $$
>
> 1. For collinear motion, $\mathbf v_A\times\mathbf v_B = \mathbf 0$ (one particle at rest, or the two moving along one line in the same or opposite directions, as in a collider), $v_{\rm Møl} = |\mathbf v_A - \mathbf v_B|$ exactly, and the flux factor is $E_AE_B|\mathbf v_A - \mathbf v_B|$.
> 2. For $|\mathbf v_A|, |\mathbf v_B| \ll 1$, $v_{\rm Møl} \simeq |\mathbf v_A - \mathbf v_B|$, the Newtonian relative velocity.
>
> *Model:* any (kinematics); *applies:* any on-shell momenta $p_A$, $p_B$, independent of the dynamics.
>
> *Source: Yu §6.5.2, eqs. (6.322)–(6.331) and the paragraphs after (6.329) (page images checked) · the user's PHY 513 notes, Ch. 15 §15.6, eq. (moller)*

^thm-c6b-3-6

> [!derivation]- Derivation
> **Step 1** (the angle). With $\alpha$ the angle between $\mathbf v_A$ and $\mathbf v_B$ (Yu (6.322)–(6.323)),
>
> $$
> \mathbf v_A\cdot\mathbf v_B = |\mathbf v_A||\mathbf v_B|\cos\alpha , \qquad |\mathbf v_A\times\mathbf v_B| = |\mathbf v_A||\mathbf v_B|\sin\alpha , \qquad (\mathbf v_A\cdot\mathbf v_B)^2 = |\mathbf v_A|^2|\mathbf v_B|^2(1 - \sin^2\alpha) = |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 .
> $$
>
> **Step 2** (square $1 - \mathbf v_A\cdot\mathbf v_B$). Expand, insert Step 1, and write $-2\mathbf v_A\cdot\mathbf v_B = |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A|^2 - |\mathbf v_B|^2$ (Yu (6.324)):
>
> $$
> \begin{aligned}
> (1 - \mathbf v_A\cdot\mathbf v_B)^2 &= 1 - 2\mathbf v_A\cdot\mathbf v_B + |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\\
> &= 1 + |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A|^2 - |\mathbf v_B|^2 + |\mathbf v_A|^2|\mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\\
> &= |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 + (1 - |\mathbf v_A|^2)(1 - |\mathbf v_B|^2) .
> \end{aligned}
> $$
>
> **Step 3** (the four-vector product). $p^\mu = (E, \mathbf p) = E(1, \mathbf v)$ (Yu (6.325)), so (Yu (6.326))
>
> $$
> p_A\cdot p_B = E_AE_B - \mathbf p_A\cdot\mathbf p_B = E_AE_B(1 - \mathbf v_A\cdot\mathbf v_B) .
> $$
>
> **Step 4** (the masses cancel). Square Step 3, insert Step 2, and use $E^2(1 - |\mathbf v|^2) = E^2 - |\mathbf p|^2 = m^2$ for each particle (Yu (6.327)–(6.328)):
>
> $$
> \begin{aligned}
> (p_A\cdot p_B)^2 - m_A^2m_B^2 &= E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) + E_A^2(1 - |\mathbf v_A|^2)\,E_B^2(1 - |\mathbf v_B|^2) - m_A^2m_B^2\\
> &= E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) + m_A^2m_B^2 - m_A^2m_B^2 = E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) .
> \end{aligned}
> $$
>
> **Step 5** (the statement). Divide by $E_A^2E_B^2$ and take the positive root ([[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]]; Yu (6.329)):
>
> $$
> v_{\rm Møl} = \frac{1}{E_AE_B}\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = \sqrt{|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2} .
> $$
>
> **Step 6** (parts 1–2). If $\mathbf v_A\times\mathbf v_B = \mathbf 0$, Step 5 is $\sqrt{|\mathbf v_A - \mathbf v_B|^2} = |\mathbf v_A - \mathbf v_B|$, and the flux factor is $E_AE_Bv_{\rm Møl} = E_AE_B|\mathbf v_A - \mathbf v_B|$ (Yu (6.330)–(6.331)). For small velocities $|\mathbf v_A\times\mathbf v_B|^2 = |\mathbf v_A|^2|\mathbf v_B|^2\sin^2\alpha$ is of fourth order in the velocities and $|\mathbf v_A - \mathbf v_B|^2$ of second order, so the cross product is negligible.
>
> **What the derivation shows.**
> - The Møller velocity is the relativistic generalization of the relative velocity; for collinear beams it is the velocity difference measured in one frame, which can exceed 1: head-on at the speed of light $|\mathbf v_A - \mathbf v_B| = 2$ (Yu after (6.331); [[§C6b.3 The Cross Section#^cau-c6b-3-2|§C6b.3, Caution: The velocity difference is not a relative velocity]]).
> - Multiplied by $E_AE_B$, Step 5 is the course's invariant form of the flux factor, [[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]].

^der-c6b-3-6

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]]

> [!theorem] Theorem §C6b.3.7: The Flux Factor in Invariant Form
> For collinear beams,
>
> $$
> E_AE_B\,|\mathbf v_A - \mathbf v_B| = \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} ,
> $$
>
> which is manifestly invariant. In general $\frac{1}{E_AE_B}\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = \sqrt{|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2}$, Yu's Møller velocity $v_{\rm Møl}$ ([[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]]). The statement is [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]], 1, multiplied by $E_AE_B$, and the invariant flux factor of [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], 1, written for collinear beams: the same result in the form the course uses (the user's notes, eq. (moller)); its form with the Källén function is ★ [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-3|Theorem §C6b.4.3]], in the next section.
>
> *Model:* any (kinematics); *applies:* collinear beams for the first equality; any momenta for the second.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.6, eq. (moller) (filled in) · Yu §6.5.2, eqs. (6.315), (6.322)–(6.329)*

^thm-c6b-3-7

> [!derivation]- Derivation
> **Step 1** (the general identity). By [[§C6b.3 The Cross Section#^der-c6b-3-6|Derivation §C6b.3.6]], Steps 1–4 (Yu (6.322)–(6.328)): $p_A\cdot p_B = E_AE_B(1 - \mathbf v_A\cdot\mathbf v_B)$, $(1 - \mathbf v_A\cdot\mathbf v_B)^2 = |\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2 + (1 - |\mathbf v_A|^2)(1 - |\mathbf v_B|^2)$, and $E^2(1 - |\mathbf v|^2) = m^2$, which give
>
> $$
> (p_A\cdot p_B)^2 - m_A^2m_B^2 = E_A^2E_B^2\bigl(|\mathbf v_A - \mathbf v_B|^2 - |\mathbf v_A\times\mathbf v_B|^2\bigr) .
> $$
>
> Divided by $E_A^2E_B^2$, its square root is the second equality of the statement ([[§C6b.3 The Cross Section#^der-c6b-3-6|Derivation §C6b.3.6]], Step 5).
>
> **Step 2** (collinear beams). For collinear beams $\mathbf v_A\times\mathbf v_B = \mathbf 0$; take the square root of Step 1 ($E_AE_B > 0$):
>
> $$
> \sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2} = E_AE_B\,|\mathbf v_A - \mathbf v_B| .
> $$
>
> **Step 3** (check in the rest frame of $A$). $p_A = (m_A, \mathbf 0)$, $E_B^2 - m_B^2 = |\mathbf p_B|^2$:
>
> $$
> \sqrt{(m_AE_B)^2 - m_A^2m_B^2} = m_A\sqrt{E_B^2 - m_B^2} = m_A|\mathbf p_B| , \qquad E_AE_B|\mathbf v_A - \mathbf v_B| = m_AE_B\,\frac{|\mathbf p_B|}{E_B} = m_A|\mathbf p_B| .
> $$
>
> **What the derivation shows.**
> - For collinear beams the flux factor is a function of the invariant $p_A\cdot p_B$ alone, the algebraic reason behind the course's statement that the flux factor is invariant under boosts along the beam ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]], 1). The same invariant written with the antisymmetric tensor of the course's route is in [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-6|Derivation §C6b.9.6]], "What the derivation shows".
> - Checked numerically in `qft-C/tools/l15/checks.py`.

^der-c6b-3-7

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]], [[§C6b.3 The Cross Section#^def-c6b-3-3|Def. §C6b.3.3]]

> [!caution] Caution: The velocity difference is not a relative velocity
> $|\mathbf v_A - \mathbf v_B|$ is the difference of two velocities measured in the same frame, not the speed of one particle in the rest frame of the other. It is not bounded by 1: for a head-on collision of ultrarelativistic particles in the centre-of-mass frame it approaches 2. Nothing is wrong: it is the rate at which the two flux tubes sweep through each other. Names: PS call it "the relative velocity of the beams as viewed from the laboratory frame" (p. 106); Yu defines $v_{\rm rel} \equiv |\mathbf v_{\mathcal A} - \mathbf v_{\mathcal B}|$, "相对速度" (eq. (6.314)), and notes that for head-on ultrarelativistic beams $v_{\rm rel} = 2$, "no longer a relative velocity in the traditional sense" (p. 246); the true relative speed is the Møller-type invariant $\sqrt{(p_A\cdot p_B)^2 - m_A^2m_B^2}/(p_A\cdot p_B)$.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.6, Caution "$|\vec v_A - \vec v_B|$ is not a relative velocity" · PS §4.5, p. 106 · Yu §6.5.2, eq. (6.314), p. 246*

^cau-c6b-3-2

The course reaches frame independence by a second route: the flux factor $E_AE_B|\mathbf v_A - \mathbf v_B|$ of collinear beams is a component of an antisymmetric tensor, and the cross section transforms like an area, the same in the centre-of-mass frame and in a target frame ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|Theorem §C6b.9.6]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]]). It needs the cross section as an area in the plane of impact parameters, which the wave-packet route defines ([[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-6|Def. §C6b.8.6]]); it is therefore stated there, after the decays.

## The differential cross section

> [!definition] Definition §C6b.3.4: The n-Particle Relativistic Phase Space (Yu: n-Body Invariant Phase Space)
> The **$n$-particle phase-space factor** of a final state of $n$ particles with total four-momentum $P$ — the course's **$n$-particle relativistic phase space**, Yu's **$n$-body invariant phase space** — is
>
> $$
> d\Pi_n = \Bigl(\prod_{j=1}^n\frac{d^3p_j}{(2\pi)^3\,2E_j}\Bigr)\,(2\pi)^4\delta^4\Bigl(P - \sum_{j=1}^np_j\Bigr) ,
> $$
>
> with $P = p_A + p_B$ for $2 \to n$ scattering with initial momenta $p_A$, $p_B$, and $P = p_A$ for a decay ([[§C6b.5 Decay Widths|§C6b.5]]): the kinematics of the $n$ final particles. An explicit $d\Pi_n$ requires a specific final state and coordinate system. It is Lorentz invariant ([[§C6b.3 The Cross Section#^thm-c6b-3-8|Theorem §C6b.3.8]]).
>
> *Model:* any (kinematics); *applies:* the measure of relativistically normalized final states ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]); independent of the dynamics.
>
> *Source: PHY 513 Lecture 15, slide 20 ("The $n$-particle phase space factor $d\Pi_n = (\prod_i\frac{d^3p_i}{(2\pi)^3}\frac{1}{2E_i})\cdot(2\pi)^4\delta^{(4)}(p_A + p_B - \sum_ip_i)$"), slide 25 ("The phase space factor is kinematics of $n$ final particles … Explicit $d\Pi_n$: specific final state and coordinate system"), slide 22 (with $p_A$), and transcript ("this whole thing here is sometimes called the $n$ particle relativistic phase space") · the user's PHY 513 notes, Ch. 15 §15.7, eq. (dPin) · PS §4.5, eq. (4.80) ("relativistically invariant $n$-body phase space") · Yu §6.5.2, eq. (6.318) ("$n$ 体不变相空间", for $P = p_A + p_B$)*

^def-c6b-3-4

With it, [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]] reads $d\sigma = \frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}\,|\mathcal M|^2\,d\Pi_n$ (slide 24).

> [!theorem] Theorem §C6b.3.8: The Phase Space Is Lorentz Invariant
> For every scalar function $F$ of the momenta and every $\Lambda \in SO^+(1, 3)$, $\int d\Pi_n\,F(p_1, \dots, p_n)$ with total momentum $\Lambda P$ equals the same integral of $F(\Lambda p_1, \dots, \Lambda p_n)$ with total momentum $P$: $d\Pi_n$ is an invariant measure on the final states.
>
> *Model:* any (kinematics); *applies:* independent of the dynamics.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.6 (first paragraph) and §15.7 (Definition "The $n$-body relativistic phase space": "It is Lorentz invariant") · PS §4.5, p. 106 ("manifestly Lorentz invariant") · Yu §6.5.1, eq. (6.304)*

^thm-c6b-3-8

> [!derivation]- Derivation
> **Step 1** (each one-particle factor). By [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]] and [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], substituting $p = \Lambda p'$:
>
> $$
> \int\frac{d^3p}{(2\pi)^32E_{\mathbf p}}\,G(p) = \int\frac{d^4p}{(2\pi)^4}\,2\pi\delta(p^2 - m^2)\theta(p^0)\,G(p) = \int\frac{d^4p'}{(2\pi)^4}\,|\det\Lambda|\,2\pi\delta\bigl((\Lambda p')^2 - m^2\bigr)\theta\bigl((\Lambda p')^0\bigr)\,G(\Lambda p') = \int\frac{d^3p'}{(2\pi)^32E_{\mathbf p'}}\,G(\Lambda p') ,
> $$
>
> using $|\det\Lambda| = 1$, $(\Lambda p')^2 = p'^2$, and $\theta((\Lambda p')^0) = \theta(p'^0)$ on the mass shell.
>
> **Step 2** (the delta function). By linearity and [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1,
>
> $$
> \delta^4\Bigl(\Lambda P - \sum_i\Lambda p_i'\Bigr) = \delta^4\Bigl(\Lambda\bigl(P - \textstyle\sum_ip_i'\bigr)\Bigr) = |\det\Lambda|^{-1}\,\delta^4\Bigl(P - \sum_ip_i'\Bigr) = \delta^4\Bigl(P - \sum_ip_i'\Bigr) .
> $$
>
> **Step 3** (combine). Substitute $p_i = \Lambda p_i'$ in every factor of the integral with total momentum $\Lambda P$; by Step 1 each measure is unchanged, by Step 2 the delta function loses its $\Lambda$:
>
> $$
> \int\prod_i\frac{d^3p_i}{(2\pi)^32E_i}\,(2\pi)^4\delta^4\Bigl(\Lambda P - \sum_ip_i\Bigr)F(p_1, \dots, p_n) = \int\prod_i\frac{d^3p_i'}{(2\pi)^32E_i'}\,(2\pi)^4\delta^4\Bigl(P - \sum_ip_i'\Bigr)F(\Lambda p_1', \dots, \Lambda p_n') .
> $$
>
> **What the derivation shows.**
> - "It is built up from invariant 3-momentum integrals constrained by a 4-momentum delta function" (PS p. 106); the invariance holds for the measure as a whole, not for its explicit form in a chosen frame.

^der-c6b-3-8

*Uses:* [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]], [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]]

> [!theorem] Theorem §C6b.3.9: The Differential Cross Section
> 1. Without the integral over the final momenta,
>
> $$
> d\sigma = \frac{1}{4E_AE_Bv_{\rm Møl}}\,|\mathcal M|^2\,d\Pi_n , \qquad \sigma = \frac{1}{S_{\rm id}}\int d\sigma .
> $$
>
> 2. For collinear beams,
>
> $$
> d\sigma = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\;|\mathcal M(p_A, p_B \to \{p_j\})|^2\;d\Pi_n .
> $$
>
> This is the formula of the lecture, derived there with wave packets ([[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]]; PS (4.79)).
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] and [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]]; *applies:* as there.
>
> *Source: Yu §6.5.2, eqs. (6.319)–(6.321), (6.330)–(6.331) (page images checked: "计算微分截面 $d\sigma$ 时不会对全同量子态重复计数，因而不需要考虑末态对称性因子") · PHY 513 Lecture 15, slides 16, 24*

^thm-c6b-3-9

> [!derivation]- Derivation
> **Step 1** (drop the integral). Write [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]] with [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]] (Yu (6.319)):
>
> $$
> \sigma = \frac{1}{S_{\rm id}}\,\frac{1}{4E_AE_Bv_{\rm Møl}}\int d\Pi_n\,|\mathcal M|^2 = \frac{1}{S_{\rm id}}\int\Bigl[\frac{1}{4E_AE_Bv_{\rm Møl}}\,|\mathcal M|^2\,d\Pi_n\Bigr] ,
> $$
>
> and the bracket is the cross section into the range $d\Pi_n$ of final momenta (Yu (6.320)).
>
> **Step 2** (no $S_{\rm id}$ in $d\sigma$). The factor of [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]] corrects a sum over all orderings of the final momenta. A small range around pairwise different momenta and its permuted copies are disjoint, so each state in it is counted once: $d\sigma$ carries no factor, and $\sigma = \frac{1}{S_{\rm id}}\int d\sigma$ (Yu (6.321)).
>
> **Step 3** (collinear beams). By [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]], 1, $v_{\rm Møl} = |\mathbf v_A - \mathbf v_B|$, and $4E_AE_B = 2E_A\cdot2E_B$:
>
> $$
> \frac{1}{4E_AE_Bv_{\rm Møl}} = \frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|} .
> $$
>
> **What the derivation shows.**
> - Box route and wave-packet route give the same $d\sigma$; the course's form holds in every frame reached from the rest frame of $A$ along the beam axis, the centre-of-mass frame included ([[§C6b.3 The Cross Section#^thm-c6b-3-7|Theorem §C6b.3.7]]).
> - Dimension: $[d\sigma] = -2$ for every $n$ ([[§C6b.3 The Cross Section#^thm-c6b-3-11|Theorem §C6b.3.11]]).

^der-c6b-3-9

*Uses:* [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], [[§C6b.3 The Cross Section#^thm-c6b-3-6|Theorem §C6b.3.6]], [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]]

*Procedure:* [[P7 From ℳ to σ or Γ#^p7-6|P7, step 6]]

> [!definition] Definition §C6b.3.5: Unpolarized Cross Section
> For particles with spin, $\mathcal M$ depends on the spin projections $m = s, s - 1, \dots, -s$, the $2s + 1$ states of a massive particle of spin $s$ at each momentum ([[§C3.6★ Particle States and the Little Group#^thm-c3-6-9|Theorem §C3.6.9]]). If the initial spins are not prepared and the final ones not measured, the **unpolarized** cross section averages over the initial projections and sums over the final ones: [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]] with $|\mathcal M|^2$ replaced by
>
> $$
> \overline{|\mathcal M|^2} \equiv \frac{1}{(2s_A + 1)(2s_B + 1)}\sum_{m_A, m_B}\;\sum_{m_1, \dots, m_n}|\mathcal M|^2 , \qquad d\sigma = \frac{1}{4E_AE_Bv_{\rm Møl}}\,\overline{|\mathcal M|^2}\,d\Pi_n .
> $$
>
> A massless particle of spin $s \ge \frac12$ in a theory with parity symmetry (photon, graviton) has two helicity states, $\lambda = \pm s$, not $2s + 1$ ([[§C3.7★ Massless Particles and Helicity#^rem-c3-7-2|§C3.7, Remark: Parity pairs λ with −λ: photon, graviton, neutrino]]): its average is $\frac12\sum_{\lambda = \pm s}$. A massless particle with a single helicity (the neutrino of the massless idealization, same remark) has one state and is not averaged.
>
> Course form (Lecture 19), for two spin-$\frac12$ particles in and two out: $\overline{|\mathcal M|^2} = \frac14\sum_{\rm spins}|\mathcal M|^2$, the spin average ([[§C8.7 The Spin-Averaged Squared Amplitude#^def-c8-7-1|Def. §C8.7.1]]).
>
> *Model:* as in [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]]; *applies:* as there, unpolarized beams and undetected final spins.
>
> *Source: PHY 513, Problem Set 9, Problem 5 (Larsen: "the unpolarized differential cross sections"; the user's solution: "Averaging over the initial and summing over the final spins") · PHY 513 Lecture 19 (Larsen, 11 Nov 2026), slide 12 · the user's PHY 513 notes, Lecture 19 update, §19.2, Definition "Spin average" · PS §5.1, p. 132 · written here for general spins*

^def-c6b-3-5

> [!theorem] Theorem §C6b.3.10: Spin Sums Are Traces: Independent of the Spin Basis
> At fixed momenta, let $\{|m\rangle\}$ be an orthonormal basis of the spin states of one particle and $|\psi\rangle$ any state.
> 1. The sum over final projections is $\sum_{m_f}|\langle m_f|\psi\rangle|^2 = \langle\psi|\mathbf 1_{\rm spin}|\psi\rangle$ by completeness.
> 2. The average over initial projections of an operator $X$ on the spin space is $\frac{1}{2s + 1}\sum_{m_i}\langle m_i|X|m_i\rangle = \frac{1}{2s + 1}\operatorname{Tr}X$.
> 3. Both are independent of the orthonormal basis: $\overline{|\mathcal M|^2}$ of [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]] may be computed with each particle's spin quantized along any axis.
>
> For Dirac particles the two spin states are carried by the spinors $u^s$, $v^s$, the completeness relation is $\sum_su^s\bar u^s = \slashed p + m$, $\sum_sv^s\bar v^s = \slashed p - m$, and the sum over spins becomes a trace over spinor indices (Lecture 19: [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-3|Theorem §C8.7.3]]; in general, with the average of [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]: [[§C8.7 The Spin-Averaged Squared Amplitude#^thm-c8-7-7|Theorem §C8.7.7]]).
>
> *Model:* as in [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]]; *applies:* any spins, any order; linear algebra on each particle's spin space.
>
> *Source: PHY 513, Problem Set 9, Problem 5 (the user's solution, paragraph "Choice of spin axis") · the sentence on Dirac particles: PHY 513 Lecture 19 (Larsen, 11 Nov 2026), slide 12*

^thm-c6b-3-10

> [!derivation]- Derivation
> **Step 1** (part 1). $\sum_{m_f}|\langle m_f|\psi\rangle|^2 = \sum_{m_f}\langle\psi|m_f\rangle\langle m_f|\psi\rangle = \langle\psi|\bigl(\sum_{m_f}|m_f\rangle\langle m_f|\bigr)|\psi\rangle = \langle\psi|\mathbf 1_{\rm spin}|\psi\rangle$ (completeness of an orthonormal basis, [[§47 The Completeness Relation#^prop-47-1|556 Prop. §47.1]]).
>
> **Step 2** (part 2). $\sum_{m_i}\langle m_i|X|m_i\rangle$ is the trace of $X$ in the basis $\{|m_i\rangle\}$.
>
> **Step 3** (part 3). Another orthonormal basis is $|m'\rangle = V|m\rangle$ with $V$ unitary: $\sum_{m'}|m'\rangle\langle m'| = V\mathbf 1V^\dagger = \mathbf 1$ and $\sum_{m'}\langle m'|X|m'\rangle = \operatorname{Tr}(V^\dagger XV) = \operatorname{Tr}X$ (cyclicity). With $\mathcal M$ the coefficient of the same $(2\pi)^4\delta^4$ for every choice of spins ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]), $\sum|\mathcal M|^2$ over final spins is part 1 and the initial average part 2, applied particle by particle.
>
> **What the derivation shows.**
> - Only the completeness of an orthonormal basis and the cyclicity of the trace are used: the unpolarized $\overline{|\mathcal M|^2}$ needs no choice of spin axis, and each particle may have its own.
> - Used next where the axis is chosen for convenience: the spins quantized along the normal to the scattering plane in [[§C9.13 Time Reversal of the S-Matrix and Detailed Balance#^thm-c9-13-5|Theorem §C9.13.5]], and the counting $2s + 1$ of detailed balance ([[§C9.13 Time Reversal of the S-Matrix and Detailed Balance#^thm-c9-13-6|Theorem §C9.13.6]]).

^der-c6b-3-10

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-5|Def. §C6b.3.5]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§47 The Completeness Relation#^prop-47-1|556 Prop. §47.1]], [[§C1.4 Change of Basis and Unitary Equivalence#^thm-c1-4-2|QM Theorem §C1.4.2]]

> [!theorem] Theorem §C6b.3.11: The Cross Section Is an Area for Every n
> With $N = 2 + n$ external particles, $[d\sigma] = -2$ for every $n$: the dimension of an area.
>
> *Model:* [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] with [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]], or [[§C6b.8 Wave Packets and the Cross Section#^mod-c6b-8-1|Model §C6b.8.1]] (the dimension does not depend on the route); *applies:* relativistic normalization, four spacetime dimensions; every order.
>
> *Source: the user's PHY 513 notes, Ch. 15 §15.5, Derivation "Dimension check (filled in)"*

^thm-c6b-3-11

> [!derivation]- Derivation
> **Step 1** (the amplitude). By [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]] with $N = 2 + n$,
>
> $$
> [\mathcal M] = 4 - (2 + n) = 2 - n , \qquad [|\mathcal M|^2] = 2(2 - n) = 4 - 2n .
> $$
>
> **Step 2** (phase space). With $[d^3p] = 3$, $[E] = 1$, $[\delta^4] = -4$ and $(2\pi)$'s dimensionless,
>
> $$
> \Bigl[\prod_{i=1}^n\frac{d^3p_i}{(2\pi)^32E_i}\,(2\pi)^4\delta^4\Bigr] = n(3 - 1) + (-4) = 2n - 4 .
> $$
>
> **Step 3** (flux). Velocities are dimensionless, so
>
> $$
> \Bigl[\frac{1}{2E_A\,2E_B\,|\mathbf v_A - \mathbf v_B|}\Bigr] = -(1 + 1 + 0) = -2 .
> $$
>
> **Step 4** (sum).
>
> $$
> [d\sigma] = -2 + (4 - 2n) + (2n - 4) = -2 .
> $$
>
> **What the derivation shows.**
> - The growth of $|\mathcal M|^2$'s dimension with $n$ is exactly compensated by the phase space; checked for $n = 1, \dots, 5$ in `qft-C/tools/l15/checks.py`.

^der-c6b-3-11

*Uses:* [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]], [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-3|Theorem §C6b.9.3]]

## The centre-of-mass frame

> [!definition] Definition §C6b.3.6: Centre-of-Mass Frame and Centre-of-Mass Energy
> For a $2 \to n$ process the **centre-of-mass frame** is the inertial frame in which the total three-momentum vanishes, $\mathbf p_A + \mathbf p_B = \sum_{j=1}^n\mathbf p_j = \mathbf 0$. The **centre-of-mass energy** $E_{\rm cm}$ is the total energy there, $E_{\rm cm} = E_A + E_B = \sum_jE_j$. Because $(p_A + p_B)^2 = (E_A + E_B)^2 - |\mathbf p_A + \mathbf p_B|^2$ is a Lorentz scalar and equals $E_{\rm cm}^2$ in that frame, in every frame
>
> $$
> E_{\rm cm} = \sqrt{(p_A + p_B)^2} = \sqrt{(p_1 + p_2 + \cdots + p_n)^2} = \sqrt s ,
> $$
>
> with $s$ the first Mandelstam variable ([[§C1a.5 Vectors, Tensors and Index Notation#^def-c1a-5-2|Def. §C1a.5.2]]).
>
> *Model:* any (kinematics); *applies:* any $2 \to n$ process (the second form by $p_A + p_B = \sum_jp_j$, the support of $d\Pi_n$); for a decay the same definition with $p_A$ alone gives $E_{\rm cm} = m_A$ ([[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]]).
>
> *Source: Yu §6.5.2, eqs. (6.332)–(6.334) (page image checked: "质心系定义为使系统总动量为零的参考系", "$E_{\rm CM}$ 是 Lorentz 不变量") · PHY 513 Lecture 15, slide 19 ("c.m.s. ($\vec p_{\rm tot} = 0$)"), slide 20 · PS §4.5, p. 106*

^def-c6b-3-6

> [!theorem] Theorem §C6b.3.12: The Threshold of a 2 → n Process
> A $2 \to n$ process ($n \ge 2$) with final masses $m_1, \dots, m_n$ can occur only if
>
> $$
> E_{\rm cm} > \sum_{j=1}^nm_j ,
> $$
>
> with $E_{\rm cm}$ of [[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]. At $E_{\rm cm} = \sum_jm_j$ the final particles are all at rest in the centre-of-mass frame and the phase space $\int d\Pi_n$ ([[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]]) has zero volume; below it $d\Pi_n$ has no support. The condition is the same in every frame.
>
> *Model:* any (kinematics); *applies:* every frame, independent of the dynamics.
>
> *Source: Yu §6.5.2, eq. (6.335) (page image checked, boxed: "若 $E_{\rm CM} = \sum_jm_j$，则末态相空间体积为零，散射过程不能发生"); §6.5.3, eq. (6.339) for $n = 2$*

^thm-c6b-3-12

> [!derivation]- Derivation
> **Step 1** (the centre-of-mass frame exists). $P = p_A + p_B$ has $P^0 = E_A + E_B > 0$ and $P^2 = (E_A + E_B)^2 - |\mathbf p_A + \mathbf p_B|^2 \ge (E_A + E_B)^2 - (|\mathbf p_A| + |\mathbf p_B|)^2 \ge 0$, using $E \ge |\mathbf p|$; for massive particles $E > |\mathbf p|$ and $P^2 > 0$. The boost with velocity $-\mathbf P/P^0$ ([[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], along $\mathbf P$, read actively; $|\mathbf P|/P^0 < 1$) takes $P$ to $(\sqrt{P^2}, \mathbf 0)$.
>
> **Step 2** (energies in that frame). The delta function of $d\Pi_n$ requires $\sum_j\mathbf p_j = \mathbf 0$ and $\sum_jE_j = E_{\rm cm}$. Each energy satisfies
>
> $$
> E_j = \sqrt{\mathbf p_j^2 + m_j^2} \ge m_j , \qquad \text{with equality if and only if } \mathbf p_j = \mathbf 0 ,
> $$
>
> so $E_{\rm cm} = \sum_jE_j \ge \sum_jm_j$, with equality only at $\mathbf p_1 = \cdots = \mathbf p_n = \mathbf 0$.
>
> **Step 3** (below and at threshold). For $E_{\rm cm} < \sum_jm_j$ the energy delta function has no zero on the integration region: $d\Pi_n = 0$. Just above threshold write $Q = E_{\rm cm} - \sum_jm_j$ and $E_j = m_j + \frac{\mathbf p_j^2}{2m_j} + O(\mathbf p_j^4)$: after the $\delta^3$ has removed $\mathbf p_n$, the energy constraint is $\sum_j\frac{\mathbf p_j^2}{2m_j} = Q$ in $3(n - 1)$ dimensions. The region $\sum_j\mathbf p_j^2/2m_j < Q$ is an ellipsoid of volume $\propto Q^{3(n-1)/2}$; the energy delta function is its derivative in $Q$, so
>
> $$
> \int d\Pi_n \propto \frac{d}{dQ}Q^{3(n-1)/2} \propto Q^{(3n-5)/2} \;\longrightarrow\; 0 \quad (Q \to 0^+,\ n \ge 2) .
> $$
>
> For $n = 2$ this is $\int d\Pi_2 = |\mathbf p_1|/(4\pi E_{\rm cm})$ with $|\mathbf p_1| \propto Q^{1/2}$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-2|Theorem §C6b.4.2]]).
>
> **Step 4** (every frame). $E_{\rm cm}$ and the masses are Lorentz invariants ([[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]]), so the condition does not depend on the frame: a process possible in the centre-of-mass frame is possible in every frame.
>
> **What the derivation shows.**
> - $E_{\rm cm}$ is the energy available to make the final particles; Yu calls it the effective energy that excites the internal interactions.
> - The same argument with $E_{\rm cm} = m_A$ is the decay threshold ([[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]]).

^der-c6b-3-12

*Uses:* [[§C6b.3 The Cross Section#^def-c6b-3-6|Def. §C6b.3.6]], [[§C6b.3 The Cross Section#^def-c6b-3-4|Def. §C6b.3.4]], [[§C1a.4 The Lorentz Group#^def-c1a-4-2|Def. §C1a.4.2]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-1|Theorem §C6b.4.1]]

## The annotated formula

$$
d\sigma = \underbrace{\underbrace{\frac{1}{2E_A\,2E_B}}_{\text{(a)}}\;\underbrace{\frac{1}{|\mathbf v_A - \mathbf v_B|}}_{\text{(b)}}}_{\text{flux factor}}\;\;\underbrace{|\mathcal M|^2}_{\text{(c) dynamics}}\;\;\underbrace{\prod_{j=1}^n\underbrace{\frac{d^3p_j}{(2\pi)^3}}_{\text{(d)}}\,\underbrace{\frac{1}{2E_j}}_{\text{(e)}}\;\underbrace{(2\pi)^4\delta^4\Bigl(p_A + p_B - \sum_jp_j\Bigr)}_{\text{(f)}}}_{\text{phase space }d\Pi_n}
$$

| label | factor | where it comes from | box | careful route |
|---|---|---|---|---|
| (a) | $\frac{1}{2E_A\,2E_B}$ | the norm of the initial state, $\langle i\vert i\rangle = 2E_A\tilde V\cdot2E_B\tilde V$: relativistic normalization of the two incoming particles | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4\|Theorem §C6b.2.4]], 2 | the packet factor $1/\sqrt{2E}$, [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-3\|Def. §C6b.8.3]]; [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3\|Derivation §C6b.9.3]], Step 6 |
| (b) | $\frac{1}{\lvert\mathbf v_A - \mathbf v_B\rvert}$ | the flux $j_B = n_B\lvert\mathbf v_B\rvert = \lvert\mathbf v_B\rvert/\tilde V$: cross section = rate / flux; in any collinear frame the Møller velocity | [[§C6b.3 The Cross Section#^def-c6b-3-1\|Def. §C6b.3.1]], [[§C6b.3 The Cross Section#^thm-c6b-3-4\|Theorem §C6b.3.4]], [[§C6b.3 The Cross Section#^thm-c6b-3-6\|Theorem §C6b.3.6]] | the Jacobian of the longitudinal delta functions, [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-1\|Theorem §C6b.9.1]] |
| (c) | $\lvert\mathcal M\rvert^2$ | the squared amplitude with the $\delta^4$ taken out: the only dynamical factor | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]] | $\mathcal M\bar{\mathcal M}^\ast$ at $\bar k = k$, [[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3\|Derivation §C6b.9.3]], Steps 2, 5–6 |
| (d) | $\frac{d^3p_j}{(2\pi)^3}$ | the number of box states in $d^3p_j$, $\tilde V\,d^3p_j/(2\pi)^3$, with $\tilde V$ cancelled | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-6\|Theorem §C6b.2.6]], [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7\|Theorem §C6b.2.7]] | the completeness measure in $\mathcal P(\mathbf b)$, [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-5\|Def. §C6b.8.5]] |
| (e) | $\frac{1}{2E_j}$ | the norm of the final state, $\langle f\vert f\rangle = \prod_j2E_j\tilde V$ | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-4\|Theorem §C6b.2.4]], 3; [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-7\|Theorem §C6b.2.7]] | the same measure ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2\|Def. §C2a.4.2]]) |
| (f) | $(2\pi)^4\delta^4(\cdots)$ | the second copy of $\delta^4$ in the squared amplitude; the first became $\tilde V\tilde T$ | [[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-3\|Theorem §C6b.2.3]] | the $\delta^4$ of the unbarred amplitude, never used up ([[§C6b.9 Evaluating the Cross Section#^der-c6b-9-3\|Derivation §C6b.9.3]], Step 9) |

Two more factors do not appear in $d\sigma$. $\frac{1}{S_{\rm id}}$ enters only when $d\sigma$ is integrated over all final momenta ([[§C6b.2 Transition Probabilities in a Box#^thm-c6b-2-8|Theorem §C6b.2.8]], [[§C6b.3 The Cross Section#^thm-c6b-3-9|Theorem §C6b.3.9]]). The box volume $\tilde V$ and the duration $\tilde T$ cancel (table in [[§C6b.3 The Cross Section#^der-c6b-3-4|Derivation §C6b.3.4]], Step 4).

> [!remark] Remark: Dynamics and kinematics
> Yu, after (6.318): in the cross section "不变振幅模方 $|\mathcal M|^2$ 是动力学因素，而其它部分都属于运动学因素" (the squared invariant amplitude is the dynamical factor, everything else is kinematics). Factors (a), (b) belong to the initial state, (d)–(f) to the final state, and only (c) knows the theory; this is the course's "dynamical data" ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^rem-c6b-1-3|§C6b.1, Remark: What "dynamical" means]]) and the lecture's reading of the formula ([[§C6b.9 Evaluating the Cross Section#^rem-c6b-9-2|§C6b.9, Remark: Reading the formula]]).
>
> *Source: Yu §6.5.2, p. 244 · PHY 513 Lecture 15, slide 16*

^rem-c6b-3-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^thm-ca-2-6|Theorem §CA.2.6]], 1 — δ under a linear change of variables, $\delta^4(\Lambda q) = |\det\Lambda|^{-1}\delta^4(q) = \delta^4(q)$: the momentum-conserving delta function is Lorentz invariant, so the cross section (Derivation §C6b.3.5, Step 3) and the phase space $d\Pi_n$ (Derivation §C6b.3.8, Step 2) are.
>
> From the Math vault: [[§47 The Completeness Relation#^prop-47-1|556 Prop. §47.1]] — completeness of an orthonormal basis, which turns the sum over final spins into $\langle\psi|\mathbf 1_{\rm spin}|\psi\rangle$ (Theorem §C6b.3.10, 1).

> [!remark]- Connections
> - The operational cross section and its classical meaning as an area in the plane of impact parameters — [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-1|Def. §C6b.8.1]], [[§C6b.8 Wave Packets and the Cross Section#^def-c6b-8-2|Def. §C6b.8.2]], [[§B4.2 Scattering Cross-Sections and Rutherford Scattering#^def-b4-2-1|CM Def. §B4.2.1]].
> - Quantum mechanics divides a transition rate by a probability current in the same way — [[§C10.1 The Lippmann–Schwinger Equation and the Born Approximation#^def-c10-1-1|QM Def. §C10.1.1]].
> - The flux factor as a component of an antisymmetric tensor and the cross section as an area (the course's route to frame independence) — [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-6|Theorem §C6b.9.6]], [[§C6b.9 Evaluating the Cross Section#^thm-c6b-9-7|Theorem §C6b.9.7]].
> - The same chain with one initial particle and no flux gives the decay rate, $\frac{1}{2E_A}$ in place of $\frac{1}{2E_A2E_B|\mathbf v_A - \mathbf v_B|}$ — [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]].
> - The invariant measure of the phase space is the one that makes $\langle\mathbf p|\mathbf q\rangle$ invariant and that appears in every mode expansion — [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]].
> - A density is the time component of a current, $n = n_0\gamma$, like the charge density $\rho = j^0$; this is why $n/E$ is invariant and the event rate per unit volume $\mathcal R$ is a Lorentz scalar — ★ [[§C6b.3 The Cross Section#^thm-c6b-3-5|Theorem §C6b.3.5]], 4.
> - The centre-of-mass energy is $\sqrt s$; its threshold for a $2 \to n$ process becomes $m_A > \sum_jm_j$ for a decay, and $E_{\rm cm} \to \sqrt{s_{12}}$ gives the energies in the rest frame of a pair — [[§C6b.5 Decay Widths#^thm-c6b-5-8|Theorem §C6b.5.8]], ★ [[§C6b.6 Decay Kinematics#^thm-c6b-6-8|Theorem §C6b.6.8]].
> - Two-body phase space and the $2 \to 2$ cross section in the centre-of-mass frame, with the Källén function — [[§C6b.4 Two-Body Scattering Kinematics|§C6b.4]].
