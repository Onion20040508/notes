---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.6
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8b.5 Helicity Spinors and the Massless Limit|§C8b.5]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]] →

*Sources: PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 3, 5–11 (Part A), and transcript · the user's PHY 513 notes, Lecture 20 update, chapter opening, §20.1 "Helicity and the chiral projectors" (Definitions "Helicity", "The chiral projectors", Principle "For antiparticles the wave function shows the opposite helicity", paragraph "Asked in the lecture: is this chirality?"), §20.2 "Helicity conservation at the QED vertex" (Derivation "Projecting one fermion projects the other", paragraphs "It is dynamics, not kinematics", "The physical picture", "Asked in the lecture: is helicity conservation tied to the center of mass?"), Summary, paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.2, pp. 141–142, eqs. (5.17)–(5.18), p. 145 (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.2.4, eqs. (8.108), (8.143)–(8.157); §8.3, eqs. (8.159)–(8.168), (8.174)–(8.189), the boxed statement after (8.189) and the paragraph on neutrinos, p. 334 (page images of the current build checked) · added 2026-11-23, after Problem Set 11 was submitted: Yu §8.3, eqs. (8.169)–(8.173) with the two boxed statements, the first sentence of p. 334, eqs. (8.190)–(8.199) and the closing paragraph of §8.3 · PHY 513 Lecture 20, transcript (the sentence on a vertex without a $\gamma$) and the user's Lecture 20 update, §20.2 (the sentence marked "Filled in") · PHY 513, Problem Set 11, Problem 1(a) (statement, and the user's solution, used as written) · PS §5.5, pp. 165–166 (the two sentences on the number of $\gamma$ matrices in the Compton amplitude) · Yu §8.6.3, eq. (8.451).*

What does $e^+e^- \to \mu^+\mu^-$ do spin by spin? The spin average of [[§C8a.7 The Spin-Averaged Squared Amplitude|§C8a.7]] summed over all spins, which may be what an unpolarized experiment measures, but hides what each spin configuration does. Lecture 20 does not average. It labels the spins by helicity, the spin along the motion, which is the natural label for fast particles, and follows them through the amplitude of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]] in two ways, in three parts:
1. **Helicity amplitudes by projection** (this section and the first half of [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]]): the chirality projectors $P_{L,R}$ select helicities, the QED vertex conserves them ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]), and the square is taken with projectors, giving traces with $\gamma^5$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-4|Theorem §C8b.7.4]]).
2. **$e^+e^-$ annihilation spin by spin**: $|\mathcal M|^2 = e^4(1 \pm \cos\theta)^2$, the polarized cross sections and their average, and angular momentum in the forward direction ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]–[[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]).
3. **Explicit helicity spinors**: the vertex as a spin-one polarization vector and the amplitude as a rotated vector ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]).

The steps are collected in [[P9 Helicity Amplitudes|P9]]. The helicity of a particle is [[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]. This section fixes the projected spinors, shows that for fast particles the projectors select helicity, with the reversal for antiparticles, and proves that both fermions at a QED vertex carry the same projection; it ends with Yu's form of the same facts for the fields: at high energy $\psi_L$ and $\psi_R$ are independent fields (Theorem §C8b.6.6). A closing part, added after Problem Set 11 was submitted, states which chiralities a bilinear with any number of $\gamma$'s joins (Theorem §C8b.6.7), what this means for the mass term (Theorem §C8b.6.8) and for the scalar vertex of Yukawa theory, which flips the helicity (Theorems §C8b.6.9–§C8b.6.10), and the selection rules for spinor bilinears at high energy (Theorem §C8b.6.11). Helicity of a Dirac spinor is [[§C8b.5 Helicity Spinors and the Massless Limit#^def-c8b-5-1|Def. §C8b.5.1]], chirality and its projectors are [[§C5a.5 Chirality and Weyl Spinors|§C5a.5]], the massless limit is [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], and the physical spin of antiparticles is [[§C9.8 Physical Spin versus Wave-Function Spin|§C9.8]]; they are linked, not restated.

**The mathematical picture.** The Dirac spinor carries a reducible representation of the Lorentz group, $(\frac12, 0)\oplus(0, \frac12)$, two components plus two ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]); $P_L$ and $P_R$ project onto the two irreducible pieces, the eigenspaces of the Lorentz-invariant $\gamma^5$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]]). The vector coupling $\bar\psi\gamma^\mu\psi$ respects the split: in the chiral basis $\gamma^0\gamma^\mu$ is block diagonal, so every spinor in a QED diagram may be read as a two-component spinor that never talks to the other two components ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]). For massless particles each piece has one helicity; that is what makes the split physical.

**Setup.** [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] at order $e^2$, free relativistic states over $|0\rangle$; the c-number spinors $u^s(p)$, $v^s(p)$ of the free Dirac field ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) with $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]). The projector algebra (Definition §C8b.6.1, Theorems §C8b.6.3–§C8b.6.4) is exact for every mass and every frame. Reading a projection as a helicity needs $m = 0$, or $E \gg m$ up to corrections of relative size $m/E$ (Theorems §C8b.6.1–§C8b.6.2); the picture of physical spins in Theorem §C8b.6.5 is in the centre-of-mass frame with the beams along $\hat{\mathbf z}$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|Remark: Frame and mass]]).

*Conventions* ([[Larsen PHY 513]]): chiral basis $\gamma^\mu = \bigl(\begin{smallmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{smallmatrix}\bigr)$, $\sigma^\mu = (\mathbb 1, \boldsymbol\sigma)$, $\bar\sigma^\mu = (\mathbb 1, -\boldsymbol\sigma)$ ([[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]); $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$; $\varepsilon^{0123} = +1$ ([[§C1a.5 Vectors, Tensors and Index Notation#^cau-c1a-5-5|§C1a.5, Caution: The sign of ε⁰¹²³]]); $\hat{\mathbf p}$ is the unit vector along the motion (a direction, not an operator). A subscript $R$ or $L$ on a particle ($e^-_R$, $e^+_L$) is its physical helicity; on a spinor ($u_R$, $v_R$) it is the projection (Definition §C8b.6.1). For particles the two agree; for antiparticles they are opposite (Theorem §C8b.6.2).

## Helicity and the projected spinors

> [!definition] Definition §C8b.6.1: The Projected Spinors
> With the chirality projectors of [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]], in the chiral basis
>
> $$
> P_L = \tfrac12(\mathbb 1 - \gamma^5) = \begin{pmatrix}\mathbb 1 & 0\\ 0 & 0\end{pmatrix}, \qquad P_R = \tfrac12(\mathbb 1 + \gamma^5) = \begin{pmatrix}0 & 0\\ 0 & \mathbb 1\end{pmatrix},
> $$
>
> every Dirac spinor splits into its upper ($L$) and lower ($R$) two components:
>
> $$
> u = u_L + u_R, \qquad u_L \equiv P_Lu, \quad u_R \equiv P_Ru ; \qquad v = v_L + v_R, \quad v_{L,R} \equiv P_{L,R}v ,
> $$
>
> with conjugates $\bar u_R \equiv \overline{u_R} = \bar uP_L$, $\bar v_R \equiv \overline{v_R} = \bar vP_L$, and likewise $\overline{u_L} = \bar uP_R$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 4). The subscript is the projection, not yet a helicity.
>
> *Equivalently,* $P_L$, $P_R$ are complete orthogonal projectors with $P_L\gamma^\mu = \gamma^\mu P_R$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 1–2), and $u_L$, $u_R$ are the four-component forms of the Weyl halves of [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]: using them in place of $u$ amounts to using Weyl spinors in place of Dirac spinors.
>
> *Source: PHY 513 Lecture 20, slide 7 ("Strategy: divide spinors in to Weyl components"; the two matrices; "Project 4-spinors onto upper (=L)/lower (=R) 2-spinors: $u(p) = u_L(p) + u_R(p) \equiv P_Lu(p) + P_Ru(p)$"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.1, Definition "The chiral projectors" · PS §5.2, p. 142, eq. (5.17) · Yu §8.3, eqs. (8.159)–(8.166)*

^def-c8b-6-1

The projector properties used below are those of [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]: $P_L^2 = P_L$, $P_R^2 = P_R$ (for $P_R$: $\frac14(\mathbb 1 + 2\gamma^5 + (\gamma^5)^2) = \frac14(2\cdot\mathbb 1 + 2\gamma^5)$, since $\gamma^5$ squares to $\mathbb 1$ and the cross term is $2\gamma^5$), $P_LP_R = 0$, $P_L + P_R = \mathbb 1$, $P_{L,R}^\dagger = P_{L,R}$, $P_L\gamma^\mu = \gamma^\mu P_R$, hence $P_R\gamma^0 = \gamma^0P_L$.

> [!theorem] Theorem §C8b.6.1: At High Energy the Projectors Select the Helicity of a Particle
> For the helicity spinors $u_\pm(p)$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]]:
> 1. at $m = 0$, $u_+(p) = \sqrt{2E}\,(0, \xi_+)^{\mathsf T} = P_Ru_+$ and $u_-(p) = \sqrt{2E}\,(\xi_-, 0)^{\mathsf T} = P_Lu_-$, while $P_Lu_+ = P_Ru_- = 0$;
> 2. for $E \gg m$ the same holds up to components of relative size $m/2E$.
>
> So for a fast particle (Definition §C8b.3.2) $u_R$ is the spinor of the right-handed particle and $u_L$ that of the left-handed one: replacing $u$ by $P_Ru$ in an amplitude keeps the right-handed electron and removes the left-handed one.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* helicity basis, part 1 exact at $m = 0$, part 2 for $E \gg m$.
>
> *Source: PHY 513 Lecture 20, slide 7 ("insert $P_R$: $\bar v(p')\gamma^\mu\frac{1 + \gamma^5}{2}u(p)$ keeps amplitude for $u_R(p)$ unchanged and removes $u_L(p)$"), slide 11 ("Particle wave functions $u_{R,L}$ = physical helicity"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.1 (the paragraph after Definition "The chiral projectors") · PS §5.2, p. 142 ("the amplitude for a right-handed electron is unchanged while that for a left-handed electron becomes zero") · Yu §8.3, eqs. (8.174)–(8.180)*

^thm-c8b-6-1

> [!derivation]- Derivation
> **Step 1** (the limit). Parts 1 and 2 of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]] give $u_+ \to \sqrt{2E}(0, \xi_+)$, $u_- \to \sqrt{2E}(\xi_-, 0)$, exactly at $m = 0$ and with relative corrections $m/2E$ for $E \gg m$.
>
> **Step 2** (projections). $P_R = \operatorname{diag}(0, \mathbb 1)$ keeps the lower two components and $P_L = \operatorname{diag}(\mathbb 1, 0)$ the upper two (Definition §C8b.6.1), so $P_R\sqrt{2E}(0, \xi_+) = \sqrt{2E}(0, \xi_+)$, $P_L\sqrt{2E}(0, \xi_+) = 0$, and the other way round for $u_-$.
>
> **Step 3** (helicity). $u_\pm$ has $h = \pm\frac12$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]]), and for a particle the helicity of $u$ is that of the state it describes (Definition §C8b.3.2).
>
> **What the derivation shows**
> - The projectors are chirality projectors; they act as helicity projectors because at $m = 0$ each helicity spinor lives in one Weyl half → [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-2|Remark: Chirality and helicity]].
> - For antiparticles the reading is reversed: next theorem.

^der-c8b-6-1

*Uses:* [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], [[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]], [[§C8b.6 Helicity Conservation at the QED Vertex#^def-c8b-6-1|Def. §C8b.6.1]]

> [!theorem] Theorem §C8b.6.2: For an Antiparticle the Spinor Shows the Opposite Helicity
> At $m = 0$ (and for $E \gg m$ up to relative corrections $m/2E$), the spinor $v(p)$ of an antiparticle of physical helicity $\lambda$ is built on the two-spinor $\eta = \xi_{-\lambda}(\hat{\mathbf p})$ (up to a phase) and lies in the Weyl half of the *opposite* chirality:
>
> $$
> P_Rv = v \iff \text{the antiparticle is left-handed}, \qquad P_Lv = v \iff \text{the antiparticle is right-handed}.
> $$
>
> So $v_R$ describes a physically left-handed antiparticle and $v_L$ a right-handed one. The reason is that a spin is the eigenvalue of the spin operator $\hat{\mathbf S} = \int d^3x\,\hat\psi^\dagger\frac12\boldsymbol\Sigma\hat\psi$ ([[§C9.8 Physical Spin versus Wave-Function Spin#^def-c9-8-2|Def. §C9.8.2]]; with $\hat\psi^\dagger$, not $\hat{\bar\psi}$), whose antiparticle term comes in the order $\hat b\hat b^\dagger$; reordering costs a sign ([[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-2|Theorem §C9.8.2]]). What counts is whether the state is an eigenstate of the spin operator and with which eigenvalue, not what the two-spinor looks like ([[§C9.8 Physical Spin versus Wave-Function Spin#^pr-c9-8-4|Principle §C9.8.4]]).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] (the spin operator) and [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (the spinors); *applies:* $\eta^s = \xi^{-s}$ ([[§C9.6 Charge Conjugation on Oscillators and Spinors#^def-c9-6-5|Def. §C9.6.5]]), the helicity axis $\hat{\mathbf p}$, $m = 0$ or $E \gg m$.
>
> *Source: PHY 513 Lecture 20, slide 10 ("Wave-function spin opposite physical spin for antiparticles"; "Antiparticles contribute to particle # with negative sign. … $bb^\dagger = -b^\dagger b$ in 'wrong' order"), slide 11 ("Anti-particle wave functions $v_{R,L}$ = opposite physical helicity"), slide 26 ("Wave function spin opposite physical spin for anti-particles"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.1, Principle "For antiparticles the wave function shows the opposite helicity" · PS §5.2, p. 142 ("the right-handed spinor $v(p')$ corresponds to a left-handed positron"), p. 144 · Yu §8.3, eqs. (8.181)–(8.189)*

^thm-c8b-6-2

> [!derivation]- Derivation
> **Step 1** (physical spin of an antiparticle). By [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-2|Theorem §C9.8.2]] and [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]] (stated with the quantization axis along the momentum, $\hat{\mathbf z}$; choose the axes so that $\hat{\mathbf z} = \hat{\mathbf p}$), the antiparticle created with two-spinor $\eta$ has physical spin along $\hat{\mathbf p}$ equal to *minus* the eigenvalue of $\frac12\hat{\mathbf p}\cdot\boldsymbol\sigma$ on $\eta$: the reordering $\hat b\hat b^\dagger = -\hat b^\dagger\hat b + \text{const}$ supplies the minus sign, and the constant is proportional to $\operatorname{tr}\sigma^3 = 0$. So helicity $\lambda$ needs $(\hat{\mathbf p}\cdot\boldsymbol\sigma)\eta = -\lambda\eta$, i.e. $\eta = \xi_{-\lambda}(\hat{\mathbf p})$ up to a phase ([[§C8b.5 Helicity Spinors and the Massless Limit#^def-c8b-5-2|Def. §C8b.5.2]]). This is the label convention of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]] (Yu's $v(p, \lambda)$ has two-spinor $\lambda\xi_{-\lambda}$; [[§C8b.5 Helicity Spinors and the Massless Limit#^der-c8b-5-3|Derivation §C8b.5.3]], first bullet).
>
> **Step 2** ($v$ at $m = 0$). $v = (\sqrt{p\cdot\sigma}\,\eta, -\sqrt{p\cdot\bar\sigma}\,\eta)$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]) with $p\cdot\sigma\,\xi_\pm = (E \mp |\mathbf p|)\xi_\pm$, $p\cdot\bar\sigma\,\xi_\pm = (E \pm |\mathbf p|)\xi_\pm$ (Step 1 of [[§C8b.5 Helicity Spinors and the Massless Limit#^der-c8b-5-2|Derivation §C8b.5.2]]). At $|\mathbf p| = E$: for $\eta = \xi_+$ the upper half is $\sqrt0\,\xi_+ = 0$ and the lower $-\sqrt{2E}\,\xi_+$, so $v = \sqrt{2E}(0, -\xi_+) = P_Rv$; for $\eta = \xi_-$ the lower half vanishes and $v = \sqrt{2E}(\xi_-, 0) = P_Lv$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 3, with Yu's phases).
>
> **Step 3** (combine). $\eta = \xi_+$ is helicity $\lambda = -$ by Step 1: $P_Rv = v$ is the left-handed antiparticle. $\eta = \xi_-$ is $\lambda = +$: $P_Lv = v$ is the right-handed one. For $E \gg m$ the other half has relative size $m/2E$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2).
>
> **What the derivation shows**
> - Two reversals: the $v$ spinor carries the conjugate two-spinor of the physical spin, and $\gamma^5$ on $v$ measures the helicity of that two-spinor. The physical helicity is the opposite of the projection.
> - Example used in [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]]: a positron along $-\hat{\mathbf z}$ with $\eta = (0, 1)^{\mathsf T}$ has $\hat{\mathbf p}\cdot\boldsymbol\sigma\,\eta = -\sigma^3\eta = +\eta$, so $\eta = \xi_+(-\hat{\mathbf z})$ and $v = \sqrt{2E}(0, 0, 0, -1)^{\mathsf T} = P_Rv$: a left-handed positron, physical spin along $+\hat{\mathbf z}$ (PS (5.28)). Checked numerically (`qft-C/tools/l20/verify.py`).

^der-c8b-6-2

*Uses:* [[§C9.8 Physical Spin versus Wave-Function Spin#^def-c9-8-2|Def. §C9.8.2]], [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-2|Theorem §C9.8.2]], [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^def-c8b-5-2|Def. §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]

## Helicity conservation at the QED vertex

> [!theorem] Theorem §C8b.6.3: In the Chiral Basis γ⁰γ^μ Is Block Diagonal
> $$
> \gamma^0\gamma^\mu = \begin{pmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{pmatrix}\begin{pmatrix}0 & \sigma^\mu\\ \bar\sigma^\mu & 0\end{pmatrix} = \begin{pmatrix}\bar\sigma^\mu & 0\\ 0 & \sigma^\mu\end{pmatrix} ,
> $$
>
> so every vector bilinear splits into an upper-upper and a lower-lower part: for any spinors $w_1 = (w_{1L}, w_{1R})$, $w_2 = (w_{2L}, w_{2R})$ (two-component halves),
>
> $$
> \bar w_1\gamma^\mu w_2 = w_1^\dagger\gamma^0\gamma^\mu w_2 = w_{1L}^\dagger\bar\sigma^\mu w_{2L} + w_{1R}^\dagger\sigma^\mu w_{2R} .
> $$
>
> Equivalently, $\gamma^5$ commutes with $\gamma^0\gamma^\mu$, a product of two $\gamma$'s.
>
> *Model:* none (Dirac algebra in the chiral basis, [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]); *applies:* any spinors, any mass.
>
> *Source: PHY 513 Lecture 20, slide 8 ("Equivalently, $\gamma^0\gamma^\mu$ is diagonal"), slide 27, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.2, Derivation "Projecting one fermion projects the other" ("checked numerically") · PS §5.2, p. 144, eq. (5.27) · Yu §8.2.4, eq. (8.108)*

^thm-c8b-6-3

> [!derivation]- Derivation
> **Step 1** (the product). $\gamma^0 = \bigl(\begin{smallmatrix}0 & \mathbb 1\\ \mathbb 1 & 0\end{smallmatrix}\bigr)$ (since $\sigma^0 = \bar\sigma^0 = \mathbb 1$). Block multiplication: the upper-left block is $0\cdot0 + \mathbb 1\cdot\bar\sigma^\mu = \bar\sigma^\mu$, the upper-right $0\cdot\sigma^\mu + \mathbb 1\cdot0 = 0$, the lower-left $\mathbb 1\cdot0 + 0\cdot\bar\sigma^\mu = 0$, the lower-right $\mathbb 1\cdot\sigma^\mu + 0 = \sigma^\mu$.
>
> **Step 2** (the bilinear). $\bar w_1 = w_1^\dagger\gamma^0$, and the block-diagonal matrix acts on the halves separately.
>
> **Step 3** ($\gamma^5$). $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$ commutes with every block-diagonal matrix. Basis-free: $\gamma^5\gamma^0\gamma^\mu = -\gamma^0\gamma^5\gamma^\mu = \gamma^0\gamma^\mu\gamma^5$, two anticommutations ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], 2).
>
> **What the derivation shows**
> - The block form is the Clebsch–Gordan statement of PS p. 145: the coefficients that would couple the vector (the photon) to an upper and a lower component are the off-diagonal blocks of $\gamma^0\gamma^\mu$, and they are zero.
> - Checked numerically (`qft-C/tools/l20/verify.py`).

^der-c8b-6-3

*Uses:* [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]

> [!theorem] Theorem §C8b.6.4: Helicity Conservation at the QED Vertex
> 1. Projecting one fermion of a vector bilinear projects the other: for any spinors $u$, $v$,
>
> $$
> \bar v\gamma^\mu P_Ru = \bar v_R\gamma^\mu u_R , \qquad \bar v\gamma^\mu P_Lu = \bar v_L\gamma^\mu u_L ,
> $$
>
> with $u_R = P_Ru$, $\bar v_R = \overline{P_Rv}$ (Definition §C8b.6.1); the same holds with $u$ and $v$ replaced by any two spinors.
> 2. For the field, $\bar\psi\gamma^\mu\psi = \bar\psi_L\gamma^\mu\psi_L + \bar\psi_R\gamma^\mu\psi_R$, with no $L$–$R$ cross terms. The QED vertex $-ie\gamma^\mu$ ([[§C8a.4 Feynman Rules for QED#^thm-c8a-4-3|Theorem §C8a.4.3]]) therefore joins two fermion lines of the same projection: **helicity conservation**.
> 3. In representation terms: the Dirac representation $(\frac12, 0)\oplus(0, \frac12)$ is reducible ([[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]]), and the vector coupling does not connect its two pieces.
>
> The statement is about projections (chiralities). Read with Theorems §C8b.6.1–§C8b.6.2, at $m = 0$ it is a statement about helicities: next theorem.
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]] (the vertex); *applies:* parts 1–3 are identities, exact for every mass and in every frame.
>
> *Source: PHY 513 Lecture 20, slide 8 ("Projectors can act repeatedly: $P_R^2 = P_R$ … Projection of $u(p)$ onto $u_R(p)$ also acts towards the left: … so $v(p')$ is also projected on to its 'R' part. … Helicity is conserved in QED"), slide 9 ("The Dirac spinor is a reducible representation of the Lorentz group. Projection divides it into irreducible components"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.2, Derivation "Projecting one fermion projects the other" and the paragraph after it · PS §5.2, p. 142, eq. (5.18) · Yu §8.3, eqs. (8.187)–(8.189)*

^thm-c8b-6-4

> [!derivation]- Derivation (the projector goes straight through)
> **Step 1** (square the projector). $P_R = P_R^2$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 1): $\bar v\gamma^\mu P_Ru = v^\dagger\gamma^0\gamma^\mu P_RP_Ru$.
>
> **Step 2** (move one factor to the left). $P_R = \frac12(\mathbb 1 + \gamma^5)$ commutes with $\gamma^0\gamma^\mu$ because $\gamma^5$ does ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]]): $v^\dagger\gamma^0\gamma^\mu P_RP_Ru = v^\dagger P_R\gamma^0\gamma^\mu P_Ru$.
>
> **Step 3** (read the left factor). $P_R$ is Hermitian, so $v^\dagger P_R = (P_Rv)^\dagger$ and $(P_Rv)^\dagger\gamma^0 = \overline{P_Rv} = \bar v_R$. Hence $\bar v\gamma^\mu P_Ru = \bar v_R\gamma^\mu u_R$. The same steps with $P_L$ give the second identity. Nothing used that $u$, $v$ are $u$ and $v$ spinors.
>
> **Step 4** (the field). Insert $\mathbb 1 = P_L + P_R$ to the right of $\gamma^\mu$: $\bar\psi\gamma^\mu\psi = \bar\psi\gamma^\mu P_L\psi + \bar\psi\gamma^\mu P_R\psi = \bar\psi_L\gamma^\mu\psi_L + \bar\psi_R\gamma^\mu\psi_R$ by part 1. The cross terms are absent: $\bar\psi_L\gamma^\mu\psi_R = \bar\psi P_R\gamma^\mu P_R\psi = \bar\psi\gamma^\mu P_LP_R\psi = 0$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 2 and 1).
>
> **Step 5** (part 3). The halves $P_L\psi$, $P_R\psi$ are the two Lorentz-invariant subspaces $(\frac12, 0)$ and $(0, \frac12)$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], 3); part 2 says the coupling to $A_\mu$ is a sum of one term for each.
>
> **What the derivation shows**
> - Projecting one fermion projects both: projecting only $u$ is enough; the vertex projects $v$.
> - The only input is that two $\gamma$'s stand between $v^\dagger$ and $u$ ($\gamma^0$ from the bar and $\gamma^\mu$ from the vertex), so $\gamma^5$ passes through them → [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-1|Remark: Dynamics, not kinematics]].

^der-c8b-6-4

> [!derivation]- Derivation (second route: block diagonal γ⁰γ^μ)
> By [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], $\bar v\gamma^\mu P_Ru = v^\dagger\operatorname{diag}(\bar\sigma^\mu, \sigma^\mu)(0, u_R)^{\mathsf T} = v_R^\dagger\sigma^\mu u_R$ (two-component halves), which only sees the lower half of $v$: it is $\overline{P_Rv}\gamma^\mu P_Ru$. Likewise $\bar\psi\gamma^\mu\psi = \psi_L^\dagger\bar\sigma^\mu\psi_L + \psi_R^\dagger\sigma^\mu\psi_R$, the Weyl form of the Dirac current, with the upper-upper and lower-lower blocks only.

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.3 The Lorentz Action on Spinor Space#^thm-c5a-3-3|Theorem §C5a.3.3]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.6 Helicity Conservation at the QED Vertex#^def-c8b-6-1|Def. §C8b.6.1]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-2|P9, step 2]]

> [!theorem] Theorem §C8b.6.5: An Electron Annihilates Only with a Positron of the Opposite Helicity
> ![[ph-qft-c8-12-h1.svg]]
> *ADDED figure: the four helicity combinations of a head-on $e^-e^+$ pair along the beam axis $\hat{\mathbf z}$. Thin arrows are momenta, thick arrows physical spins. Only the pairs with $J_z = \pm1$ couple to the photon.*
>
> In $e^+e^- \to \mu^+\mu^-$ at order $e^2$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]]) with $m_e = 0$:
> 1. the electron vertex is nonzero only for $e^-_Re^+_L$ and $e^-_Le^+_R$; for $e^-_Re^+_R$ and $e^-_Le^+_L$ it vanishes. Both spinors carry the same projection ($u_R$ with $v_R$, or $u_L$ with $v_L$), and by Theorem §C8b.6.2 the antiparticle's physical helicity is the opposite one;
> 2. head-on in the centre-of-mass frame, with $e^-$ along $+\hat{\mathbf z}$ and $e^+$ along $-\hat{\mathbf z}$, the two physical spins of an allowed pair point the same way: $J_z = +1$ for $e^-_Re^+_L$, $J_z = -1$ for $e^-_Le^+_R$; the pairs with $J_z = 0$ do not couple;
> 3. with $m_\mu = 0$ the same holds at the muon vertex: only $\mu^-_R\mu^+_L$ and $\mu^-_L\mu^+_R$ are produced, with total spin $\pm1$ along their own axis $\hat{\mathbf k}$.
>
> The annihilating pair couples only as a spin-one object, which is the photon's spin one.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, the massless limit $m_e = 0$ (part 3: $m_\mu = 0$); for $E \gg m$ the forbidden configurations are suppressed, not zero ([[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|Remark: Frame and mass]]); part 2 in the centre-of-mass frame.
>
> *Source: PHY 513 Lecture 20, slides 8, 11, 26–27 ("e⁻ and e⁺ with physical spins in $+\hat z$ direction combine to photon with '+' polarization"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.2, paragraph "The physical picture"; Summary, second bullet · PS §5.2, p. 142 ("the amplitude vanishes (in the massless limit) unless the electron and positron have opposite helicity, or equivalently, unless their spinors have the same helicity"), p. 145 · Yu §8.2.4 (the configurations $\lambda_1 = -\lambda_2$ of (8.136)–(8.139))*

^thm-c8b-6-5

> [!derivation]- Derivation
> **Step 1** (allowed pairs). $e^-_R$: $u = P_Ru$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]]). By [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], $\bar v\gamma^\mu u = \bar v\gamma^\mu P_Ru = \overline{P_Rv}\gamma^\mu u$: only $P_Rv$ contributes, which is a left-handed positron ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]).
>
> **Step 2** (forbidden pairs). $e^-_Re^+_R$: $u = P_Ru$ and, for a right-handed positron, $v = P_Lv$. Then $\bar v\gamma^\mu u = \overline{P_RP_Lv}\gamma^\mu u = 0$ ($P_RP_L = 0$). $e^-_Le^+_L$ the same with $L \leftrightarrow R$. (Checked numerically: `qft-C/tools/l20/verify.py`.)
>
> **Step 3** (spins along the beam). $e^-_R$ along $+\hat{\mathbf z}$: spin along its motion, $+\frac12$ along $\hat{\mathbf z}$. $e^+_L$ along $-\hat{\mathbf z}$: spin against its motion, i.e. along $+\hat{\mathbf z}$, $+\frac12$. Total $J_z = +1$; the orbital angular momentum of momenta along the $z$ axis has no $z$ component. For $e^-_Le^+_R$ both spins are reversed: $J_z = -1$. For the forbidden pairs the spins are opposite: $J_z = 0$.
>
> **Step 4** (muons). The muon bracket $\bar u(k)\gamma_\mu v(k')$ is a vector bilinear: Steps 1–3 with $\hat{\mathbf z} \to \hat{\mathbf k}$.
>
> **What the derivation shows**
> - The selection is a statement about $J_z$ along the beam: $J_z = \pm1$ couple, $J_z = 0$ does not. A spin-one particle has $J_z = \pm1$ and $0$; the virtual photon of a vector bilinear between massless spinors picks up only $\pm1$ here.
> - Used next: the polarized amplitudes have only four nonzero configurations, and their zeros come from $J_z$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]).

^der-c8b-6-5

*Uses:* [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]

> [!remark] Remark: Dynamics, not kinematics
> Helicity conservation did not have to hold; it is a feature of QED. It rests on the $\gamma^\mu$ of the vertex $\bar\psi\gamma^\mu\psi A_\mu$: with $\gamma^0$ from the bar, two $\gamma$'s stand between the spinors, and $\gamma^5$ passes through them ([[§C8b.6 Helicity Conservation at the QED Vertex#^der-c8b-6-4|Derivation §C8b.6.4]], Step 2). It is therefore a property of QED's vector coupling, not of the kinematics of the collision. Physically it says that the two fermions at the vertex combine into the spin of the photon: the photon has spin one, and the vertex couples the pair only in its spin-one, $J_z = \pm1$ configurations ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]]). Read invariantly, helicity conservation is the statement that the photon has spin one and the vertex preserves helicity. Without a $\gamma$ at the vertex the opposite holds: a scalar vertex must flip the helicity ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]]).
>
> *Source: PHY 513 Lecture 20, slide 8, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.2, paragraph "It is dynamics, not kinematics"*

^rem-c8b-6-1

> [!remark] Remark: Chirality and helicity
> Asked in the lecture whether the projection is really about chirality: it is. **Chirality** is the eigenvalue of $\gamma^5$, a property of a field component ($\psi_L$ or $\psi_R$, [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]]); it is Lorentz invariant. **Helicity** is the spin along the motion, a property of a state (Definition §C8b.3.2). For massless particles they coincide, with the reversal for antiparticles ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]; [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]); for massive ones they differ at order $m/E$ (Yu §8.3). The projectors $P_{L,R}$ are chirality projectors; this section and [[§C8b.7 Polarized Cross Sections for Muon Pair Production|§C8b.7]] use them as helicity projectors, which is exact for $m = 0$. Yu §8.3 opens with the same projectors and projected fields, (8.159)–(8.168): $P_{L,R} = \frac12(\mathbb 1 \mp \gamma^5)$, their projector algebra and $P_L\gamma^\mu = \gamma^\mu P_R$ are [[§C5a.5 Chirality and Weyl Spinors#^def-c5a-5-1|Def. §C5a.5.1]] with [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], his $\psi_L = P_L\psi$ is the projection of Definition §C8b.6.1 applied to the field, and $\overline{\psi_L} = \bar\psi P_R$ is [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-2|Theorem §C8b.7.2]]. The word is Greek for "handedness" (*kheir*, hand).
>
> The two labels side by side (what each is, whether it is Lorentz invariant, whether it is constant in free motion, what it means for antiparticles), and the reading of slides 8, 9, 11 and 24 of Lecture 20 with that table, are in [[§C8b.4 Chirality#^rem-c8b-4-2|§C8b.4, Remark: Helicity versus chirality]] and [[§C8b.4 Chirality#^rem-c8b-4-3|§C8b.4, Remark: Reading the slides of Lecture 20 with the table]].
>
> *Source: PHY 513 Lecture 20, transcript, and slides 8, 9, 11, 24 · the user's PHY 513 notes, Lecture 20 update, §20.1, paragraph "Asked in the lecture: is this chirality?" · Yu §8.3, eqs. (8.174)–(8.189) · the comparison table and the reading of the four slides (user's question, 2026-11-18) moved to §C8b.4*

^rem-c8b-6-2

> [!remark] Remark: Frame and mass
> Asked in the lecture whether helicity conservation is tied to the centre-of-mass frame:
> 1. *The algebra is frame independent.* Theorems §C8b.6.3–§C8b.6.4 are identities between spinors in any frame.
> 2. *The reading as physical spin* is tied to head-on kinematics in the centre-of-mass frame, and more importantly to the ultrarelativistic limit. The helicity of a massive particle is not defined in its rest frame (it does not move: which is right and which is left?), and a frame moving faster than the particle reverses it ([[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-1|§C8b.5, Remark: The helicity of a massive particle depends on the frame]]; [[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-2|§C8b.3, Remark: Helicity of a massive particle]]; Lecture 20, slide 24: "helicity is not Lorentz-invariant except in the UR limit"). Helicity is a perfect proxy for spin only for massless particles, where it is Lorentz invariant ([[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]]).
> 3. *Slide 9* says: "Helicity depends on time (not conserved by the equation of motion) except for massless particles (the ultra-relativistic limit)." Its "helicity" is the R/L component of the projection, i.e. chirality; the spin along the momentum itself, $h = \hat{\mathbf p}\cdot\mathbf S$, commutes with the free Dirac Hamiltonian for every mass ([[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-1|§C8b.5, Remark: The helicity of a massive particle depends on the frame]]). For $m > 0$ a state of definite helicity is not a state of definite chirality (its other Weyl half has relative size $m/2E$, [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2), so the R/L components of a massive particle are not constant labels; at $m = 0$ both are.
> 4. *With masses kept* the helicity-violating amplitudes, zero in Theorem §C8b.6.5, appear, suppressed at high energy: the amplitude by a factor of order $m/E$ (the rate by $m^2/E^2$), so they vanish as $m \to 0$. Yu §8.2.4 lists all sixteen amplitudes of $e^+e^- \to \mu^+\mu^-$ with both masses: those with equal helicities in both pairs are proportional to $m_em_\mu\cos\theta/E_{\rm cm}^2$ (8.143)–(8.146), those with an equal-helicity $e^+e^-$ pair to $m_e\sin\theta/E_{\rm cm}$ (8.148)–(8.151), those with an equal-helicity $\mu^+\mu^-$ pair to $m_\mu\sin\theta/E_{\rm cm}$ (8.153)–(8.156), with cross sections (8.147), (8.152), (8.157), and their sum over all sixteen is the unpolarized result (8.158) (magnitudes checked numerically, `qft-C/tools/l20/verify.py`); the sixteen values with their signs, cross sections and angular zeros are ★ [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]]. Why a mass is what allows a helicity to flip: [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|Theorem §C8b.6.8]] and [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-5|Remark: Helicity suppression]].
>
> *Source: PHY 513 Lecture 20, slides 9 and 24, and transcript ("there will be a small helicity violating portion of m over e") · the user's PHY 513 notes, Lecture 20 update, §20.2, paragraph "Asked in the lecture: is helicity conservation tied to the center of mass?" (its Yu range is stated here as on Yu's pages: `qft-C/ERRATA.md`) · Yu §8.2.4, eqs. (8.143)–(8.158)*

^rem-c8b-6-3

## Chiral fields at high energy

> [!theorem] Theorem §C8b.6.6: At High Energy ψ_L and ψ_R Are Independent Fields
> In the helicity basis ($u^s = u_\lambda$, $v^s = v_\lambda$ with $s = 1, 2 \leftrightarrow \lambda = +, -$ and $\eta^s = \xi^{-s}$), neglecting the masses, the projections of the free Dirac field of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] are
>
> $$
> \hat\psi_L(x) = P_L\hat\psi(x) \simeq \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p,-}\,u_-(p)\,e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p,+}\,v_+(p)\,e^{ip\cdot x}\Bigr),
> $$
>
> $$
> \hat\psi_R(x) = P_R\hat\psi(x) \simeq \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\Bigl(\hat a_{\mathbf p,+}\,u_+(p)\,e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p,-}\,v_-(p)\,e^{ip\cdot x}\Bigr),
> $$
>
> and the conjugates $\overline{\hat\psi_L} = \hat{\bar\psi}P_R$, $\overline{\hat\psi_R} = \hat{\bar\psi}P_L$ contain the adjoint operators of the same modes. So at high energy $\hat\psi_L$ annihilates left-handed fermions and creates right-handed antifermions, $\hat\psi_R$ annihilates right-handed fermions and creates left-handed antifermions: the two chiral fields are built from disjoint sets of ladder operators and become independent fields.
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, helicity basis; every mode with $E_{\mathbf p} \gg m$, up to components of relative size $m/2E_{\mathbf p}$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2); exact at $m = 0$.
>
> *Source: Yu §8.3, eqs. (8.187)–(8.189) and the boxed statement after them ("在高能极限下，忽略质量，左手旋量场 ψ_L … 描述左旋极化的正费米子和右旋极化的反费米子 … ψ_L 和 ψ_R 成为两个相互独立的场"), with (8.179)–(8.186) · PHY 513 Lecture 20, slide 9 ("Projection divides it into irreducible components") and slide 11*

^thm-c8b-6-6

> [!derivation]- Derivation
> **1. The projector acts on the coefficients.** $P_L$ is a constant matrix, so it passes through the integral and the ladder operators of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]]: $P_L\hat\psi = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_\lambda\bigl(\hat a_{\mathbf p,\lambda}\,P_Lu_\lambda\,e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p,\lambda}\,P_Lv_\lambda\,e^{ip\cdot x}\bigr)$, and likewise for $P_R$.
>
> **2. The projected spinors.** At high energy $u_+ \simeq \sqrt{2E}(0, \xi_+)$, $u_- \simeq \sqrt{2E}(\xi_-, 0)$, $v_+ \simeq \sqrt{2E}(\xi_-, 0)$, $v_- \simeq \sqrt{2E}(0, \xi_+)$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], parts 1–3), and $P_L = \operatorname{diag}(\mathbb 1, 0)$, $P_R = \operatorname{diag}(0, \mathbb 1)$ in the chiral basis. So $P_Lu_- \simeq u_-$, $P_Lu_+ \simeq 0$, $P_Lv_+ \simeq v_+$, $P_Lv_- \simeq 0$, and $P_R$ keeps the other two (Yu (8.179)–(8.182); Theorems §C8b.6.1–§C8b.6.2). Inserting in step 1 leaves the two terms shown for each field.
>
> **3. What the operators do.** $\hat a_{\mathbf p,\lambda}$ annihilates a fermion of helicity $\lambda$ and $\hat b^\dagger_{\mathbf p,\lambda}$, which multiplies $v_\lambda$, creates an antifermion of helicity $\lambda$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]] with its by-product; [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]]). So $\hat\psi_L$ contains $\hat a_{\mathbf p,-}$ and $\hat b^\dagger_{\mathbf p,+}$, $\hat\psi_R$ contains $\hat a_{\mathbf p,+}$ and $\hat b^\dagger_{\mathbf p,-}$.
>
> **4. The conjugates.** $(P_L\hat\psi)^\dagger\gamma^0 = \hat\psi^\dagger P_L\gamma^0 = \hat\psi^\dagger\gamma^0P_R = \hat{\bar\psi}P_R$, because $\gamma^5$ is Hermitian and anticommutes with $\gamma^0$ (Yu (8.167)–(8.168); [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-2|Theorem §C8b.7.2]]); with step 2 conjugated (Yu (8.183)–(8.186)), $\overline{\hat\psi_L} \simeq \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(\hat a^\dagger_{\mathbf p,-}\bar u_-\,e^{ip\cdot x} + \hat b_{\mathbf p,+}\bar v_+\,e^{-ip\cdot x}\bigr)$, and $\overline{\hat\psi_R}$ with $(+, -)$ (Yu (8.189)).
>
> **5. Disjoint.** The sets $\{\hat a_{\mathbf p,-}, \hat b_{\mathbf p,+}\}$ and $\{\hat a_{\mathbf p,+}, \hat b_{\mathbf p,-}\}$ have no member in common, with all their adjoints; no mode appears in both fields.
>
> **What the derivation shows**
> - The statement is the field form of Theorems §C8b.6.1–§C8b.6.2: a left-handed field component carries left-handed particles and right-handed antiparticles, the CPT-conjugate pair.

^der-c8b-6-6

*Uses:* [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], [[§C9.8 Physical Spin versus Wave-Function Spin#^thm-c9-8-3|Theorem §C9.8.3]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-2|Theorem §C8b.7.2]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]

> [!remark] Remark: Neutrinos in the Standard Model
> In the Standard Model the massless neutrino of each generation is described by a left-handed field $\psi_L(x)$ alone: in the expansion of Theorem §C8b.6.6, $\hat a^\dagger_{\mathbf p,-}$ creates the left-handed neutrinos and $\hat b^\dagger_{\mathbf p,+}$ the right-handed antineutrinos, each other's antiparticles; no neutrino is described by a right-handed field. This is the two-component Weyl field of [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]] and the helicities $\mp\frac12$ of [[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-3|§C8b.3, Remark: Parity pairs λ with −λ]].
>
> *Source: Yu §8.3, p. 334 (the paragraph after (8.189) on neutrinos)*

^rem-c8b-6-4

## Which chiralities a bilinear joins

The vector vertex keeps the two chiralities apart (Theorem §C8b.6.4) because one $\gamma$ stands between $\bar\psi$ and $\psi$. What decides is only how many $\gamma$'s stand there: each one changes the projector that passes through it, $P_L\gamma^\mu = \gamma^\mu P_R$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 2). This part states the rule for any number of $\gamma$'s (Theorem §C8b.6.7), applies it to the mass term (Theorem §C8b.6.8) and to a vertex without a $\gamma$, the scalar vertex of Yukawa theory, where the helicity must flip (Theorems §C8b.6.9–§C8b.6.10), and lists the resulting selection rules for $u$ and $v$ spinors at high energy (Theorem §C8b.6.11). The helicity amplitudes of Yukawa theory built on Theorem §C8b.6.10 are [[§C8b.11 Helicity Amplitudes in Yukawa Theory|§C8b.11]]; those of $e^-e^- \to e^-e^-$, built on Theorem §C8b.6.4, are [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering|§C8b.12]].

> [!theorem] Theorem §C8b.6.7: An Even Number of γ's Joins Opposite Chiralities, an Odd Number Equal Ones
> Let $\psi_{L,R} = P_{L,R}\psi$ with conjugates $\overline{\psi_L} = \bar\psi P_R$, $\overline{\psi_R} = \bar\psi P_L$ (Definition §C8b.6.1; [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 4). Then
> 1. no $\gamma$: $\bar\psi\psi = \overline{\psi_R}\psi_L + \overline{\psi_L}\psi_R$;
> 2. one $\gamma$: $\bar\psi\gamma^\mu\psi = \overline{\psi_L}\gamma^\mu\psi_L + \overline{\psi_R}\gamma^\mu\psi_R$ (Theorem §C8b.6.4, 2);
> 3. two $\gamma$'s: $\bar\psi\gamma^\mu\gamma^\nu\psi = \overline{\psi_R}\gamma^\mu\gamma^\nu\psi_L + \overline{\psi_L}\gamma^\mu\gamma^\nu\psi_R$;
> 4. three $\gamma$'s: $\bar\psi\gamma^\mu\gamma^\nu\gamma^\rho\psi = \overline{\psi_L}\gamma^\mu\gamma^\nu\gamma^\rho\psi_L + \overline{\psi_R}\gamma^\mu\gamma^\nu\gamma^\rho\psi_R$;
> 5. in general, for a product $\Gamma_n = \gamma^{\mu_1}\cdots\gamma^{\mu_n}$ of $n$ Dirac matrices,
>
> $$
> \bar\psi\,\Gamma_n\,\psi = \begin{cases}\overline{\psi_R}\,\Gamma_n\,\psi_L + \overline{\psi_L}\,\Gamma_n\,\psi_R , & n \text{ even},\\[2pt] \overline{\psi_L}\,\Gamma_n\,\psi_L + \overline{\psi_R}\,\Gamma_n\,\psi_R , & n \text{ odd},\end{cases}
> $$
>
> and the terms not written vanish identically.
>
> **A spinor bilinear with an even (odd) number of Dirac matrices couples spinor fields of opposite (equal) chirality.** The same holds with $\bar\psi$ and $\psi$ replaced by any two spinors $\bar w_1$, $w_2$, in particular by $\bar u(p')$, $u(p)$.
>
> *Equivalently,* in two-component form the cases $n = 0$ and $n = 1$ are $\bar\psi\chi = \psi_R^\dagger\chi_L + \psi_L^\dagger\chi_R$ and $\bar\psi\gamma^\mu\chi = \psi_L^\dagger\bar\sigma^\mu\chi_L + \psi_R^\dagger\sigma^\mu\chi_R$ of [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]], and the rule is the reading of [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], 2: every $\gamma^\mu$ flips the chirality. A factor $\gamma^5$ does not change the count, since $P_{L,R}\gamma^5 = \mp P_{L,R}$.
>
> *Model:* none (Dirac algebra); *applies:* any spinors or fields, every mass, every frame, exact. It is a statement about chiralities; read with Theorems §C8b.6.1–§C8b.6.2 it is a statement about helicities for $m = 0$ or $E \gg m$ (Theorem §C8b.6.11).
>
> *Source: Yu §8.3, eqs. (8.169)–(8.172) and the boxed statement after them ("包含偶数（奇数）个 Dirac 矩阵的旋量场双线性型耦合手征性相反（相同）的旋量场") · the user's PHY 513 notes, Lecture 20 update, §20.2, paragraph "It is dynamics, not kinematics" (the sentence marked "Filled in": a bilinear $\bar\psi\Gamma\psi$ with an odd number of $\gamma$'s in $\Gamma$ joins equal chiralities, one with an even number opposite ones) · part 5 for general $n$ written here (checked numerically for $n \le 4$, `qft-C/tools/hw11/verify.py`)*

^thm-c8b-6-7

> [!derivation]- Derivation
> **Step 1** (insert the projectors). $\mathbb 1 = P_L + P_R = P_L^2 + P_R^2$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 1), placed to the right of $\Gamma_n$:
>
> $$
> \bar\psi\,\Gamma_n\,\psi = \bar\psi\,\Gamma_n\,P_LP_L\,\psi + \bar\psi\,\Gamma_n\,P_RP_R\,\psi .
> $$
>
> **Step 2** (move one projector to the left). Each $\gamma$ changes the projector, $\gamma^\mu P_L = P_R\gamma^\mu$ and $\gamma^\mu P_R = P_L\gamma^\mu$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 2). After $n$ matrices,
>
> $$
> \Gamma_n\,P_L = \begin{cases}P_L\,\Gamma_n , & n \text{ even},\\ P_R\,\Gamma_n , & n \text{ odd},\end{cases} \qquad \Gamma_n\,P_R = \begin{cases}P_R\,\Gamma_n , & n \text{ even},\\ P_L\,\Gamma_n , & n \text{ odd}.\end{cases}
> $$
>
> **Step 3** (read the left factor). $\bar\psi P_L = \overline{\psi_R}$ and $\bar\psi P_R = \overline{\psi_L}$. For $n$ even: $\bar\psi\,\Gamma_nP_LP_L\,\psi = \bar\psi P_L\,\Gamma_n\,P_L\psi = \overline{\psi_R}\,\Gamma_n\,\psi_L$ and $\bar\psi\,\Gamma_nP_RP_R\,\psi = \overline{\psi_L}\,\Gamma_n\,\psi_R$. For $n$ odd: $\bar\psi\,\Gamma_nP_LP_L\,\psi = \bar\psi P_R\,\Gamma_n\,P_L\psi = \overline{\psi_L}\,\Gamma_n\,\psi_L$ and $\bar\psi\,\Gamma_nP_RP_R\,\psi = \overline{\psi_R}\,\Gamma_n\,\psi_R$. Part 5; parts 1–4 are $n = 0, 1, 2, 3$ (Yu writes these four, each in one line, e.g. $\bar\psi\gamma^\mu\psi = \bar\psi\gamma^\mu(P_L^2 + P_R^2)\psi = \bar\psi P_R\gamma^\mu P_L\psi + \bar\psi P_L\gamma^\mu P_R\psi$).
>
> **Step 4** (the terms not written). For $n$ even, $\overline{\psi_L}\,\Gamma_n\,\psi_L = \bar\psi P_R\,\Gamma_n\,P_L\psi = \bar\psi\,\Gamma_n\,P_RP_L\,\psi = 0$, and the same for $R$; for $n$ odd, $\overline{\psi_R}\,\Gamma_n\,\psi_L = \bar\psi P_L\,\Gamma_n\,P_L\psi = \bar\psi\,\Gamma_n\,P_RP_L\,\psi = 0$, and the same with $L \leftrightarrow R$ ($P_RP_L = P_LP_R = 0$).
>
> **What the derivation shows**
> - The count is of the $\gamma$'s between $\bar\psi$ and $\psi$. Between $\psi^\dagger$ and $\psi$ there is one more, the $\gamma^0$ of the bar: Theorem §C8b.6.3 and the two $\gamma$'s of [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-1|Remark: Dynamics, not kinematics]] are the case $n = 1$.
> - ⚑ By-product ($n = 0$): the mass term couples the two chiralities → [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-8|Theorem §C8b.6.8]]; a vertex without a $\gamma$ joins opposite chiralities → [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]].
> - ⚑ By-product (spinors of definite helicity): the selection rules at high energy → [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-11|Theorem §C8b.6.11]].

^der-c8b-6-7

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^def-c8b-6-1|Def. §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]

> [!theorem] Theorem §C8b.6.8: The Mass Term Couples ψ_L and ψ_R
> The mass term of the Dirac Lagrangian ([[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]) decomposes as
>
> $$
> -m\,\bar\psi\psi = -m\,\bigl(\overline{\psi_R}\psi_L + \overline{\psi_L}\psi_R\bigr) .
> $$
>
> 1. Regarded as an interaction term, **the mass $m$ couples the left-handed field $\psi_L(x)$ to the right-handed field $\psi_R(x)$**. The kinetic term $\bar\psi\,i\gamma^\mu\partial_\mu\psi$ has one $\gamma$ and acts within each chirality (Theorem §C8b.6.7, 2).
> 2. As a perturbation of the high-energy limit, in which $\psi_L$ and $\psi_R$ are independent fields (Theorem §C8b.6.6), the mass term couples left-handed ($\lambda = -$) and right-handed ($\lambda = +$) fermions, and likewise left- and right-handed antifermions. In this sense the mass can flip the helicity.
>
> *Equivalently,* this is the Dirac Lagrangian in Weyl components, $\mathcal L = i\psi_L^\dagger\bar\sigma^\mu\partial_\mu\psi_L + i\psi_R^\dagger\sigma^\mu\partial_\mu\psi_R - m(\psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L)$ ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]]), with the field equations $i\bar\sigma^\mu\partial_\mu\psi_L = m\psi_R$, $i\sigma^\mu\partial_\mu\psi_R = m\psi_L$, in which only the mass couples the two blocks ([[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]]); for a plane wave it is the wrong-chirality component of relative size $m/2E$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^rem-c8b-5-2|§C8b.5, Remark: The mass is what connects the two chiral blocks]]).
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* an identity for every $m$; part 2 for modes with $E_{\mathbf p} \gg m$.
>
> *Source: Yu §8.3, eq. (8.173) and the boxed statement after it ("质量 $m$ 将左手旋量场 $\psi_L(x)$ 与右手旋量场 $\psi_R(x)$ 耦合起来"); p. 334, first sentence ("作为对高能极限的微扰，质量项 … 耦合着左旋极化与右旋极化的正费米子，也耦合着左旋极化与右旋极化的反费米子，所以我们在 8.2.4 小节中说'质量可以翻转螺旋度'") · the user's PHY 513 notes, Lecture 20 update, §20.2, paragraph "It is dynamics, not kinematics" ("the mass term $-m\bar\psi\psi$ is of the second kind, which is why masses spoil helicity conservation")*

^thm-c8b-6-8

> [!derivation]- Derivation
> **Step 1.** Theorem §C8b.6.7, part 1, multiplied by $-m$.
>
> **Step 2** (two-component form). In the chiral basis $\psi = (\psi_L, \psi_R)^{\mathsf T}$, $P_L\psi = (\psi_L, 0)^{\mathsf T}$, $P_R\psi = (0, \psi_R)^{\mathsf T}$, and $\gamma^0$ exchanges the halves of a row: $\overline{\psi_R} = (0, \psi_R^\dagger)\gamma^0 = (\psi_R^\dagger, 0)$, $\overline{\psi_L} = (\psi_L^\dagger, 0)\gamma^0 = (0, \psi_L^\dagger)$. Hence $\overline{\psi_R}\psi_L = \psi_R^\dagger\psi_L$ and $\overline{\psi_L}\psi_R = \psi_L^\dagger\psi_R$, the mass term of [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]].
>
> **Step 3** (part 2). In the expansions of Theorem §C8b.6.6, $\overline{\hat\psi_R}$ contains $\hat a^\dagger_{\mathbf p,+}$ and $\hat b_{\mathbf p,-}$, and $\hat\psi_L$ contains $\hat a_{\mathbf p,-}$ and $\hat b^\dagger_{\mathbf p,+}$: the product $\overline{\hat\psi_R}\hat\psi_L$ has a term $\hat a^\dagger_{\mathbf p,+}\hat a_{\mathbf q,-}$, which removes a left-handed fermion and creates a right-handed one, and a term $\hat b_{\mathbf p,-}\hat b^\dagger_{\mathbf q,+}$ for the antifermions; $\overline{\hat\psi_L}\hat\psi_R$ has the reverse.
>
> **What the derivation shows**
> - The mass is the one term of the free Lagrangian with no $\gamma$ between $\bar\psi$ and $\psi$. Every helicity-violating amplitude of QED at high energy carries a factor of a mass → [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-5|Remark: Helicity suppression]].

^der-c8b-6-8

*Uses:* [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-6|Theorem §C8b.6.6]], [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]], [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]]

> [!theorem] Theorem §C8b.6.9: Chirality and Helicity of a Solution of the Dirac Equation
> Let $u(p)$ solve $\slashed p\,u = Mu$ with $\mathbf p \ne 0$, and let $h = \hat{\mathbf p}\cdot\mathbf S$ be the helicity operator ([[§C8b.5 Helicity Spinors and the Massless Limit#^def-c8b-5-1|Def. §C8b.5.1]]). Then, exactly,
>
> $$
> \gamma^5u = \frac{|\mathbf p|}{E}\,2h\,u + \frac{M}{E}\,\gamma^5\gamma^0u .
> $$
>
> For $E \gg M$, $|\mathbf p|/E = \sqrt{1 - M^2/E^2} \to 1$ and the last term is suppressed by $M/E$:
>
> $$
> \gamma^5u = 2h\,u \qquad (E \gg M) .
> $$
>
> So a right-handed fermion, $h = +\frac12$, has $\gamma^5u = u$, that is $P_Ru = u$, and a left-handed one, $h = -\frac12$, has $P_Lu = u$: the spinor of a fermion of helicity $\lambda$ is $u_\lambda(p) = P_\lambda u(p)$, with $R \leftrightarrow h = +\frac12$ and $L \leftrightarrow h = -\frac12$.
>
> *Equivalently,* this is Theorem §C8b.6.1 and [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], which read the same limit off the explicit helicity spinors; here only the Dirac equation and $\gamma^5\gamma^0\gamma^i = 2S^i$ are used, and the size of the correction is displayed for every $E$.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* c-number positive-frequency spinors, chiral basis; the first relation exact for every $M \ge 0$, the second for $E \gg M$ (exact at $M = 0$).
>
> *Source: PHY 513, Problem Set 11, Problem 1(a) (the user's solution, paragraph "Chirality and helicity"; the statement gives $u_\lambda(p) = P_\lambda u(p)$ as the helicity spinors) · checked numerically (`qft-C/tools/hw11/verify.py`)*

^thm-c8b-6-9

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(a), paragraph "Chirality and helicity".
>
> **Step 1** (the helicity operator). For $\mathbf p \ne 0$ the helicity operator on Dirac spinors is the spin along the direction of motion,
>
> $$
> h \equiv \frac{\mathbf p}{|\mathbf p|}\cdot\mathbf S , \qquad \mathbf S = \frac12\begin{pmatrix}\boldsymbol\sigma & 0\\ 0 & \boldsymbol\sigma\end{pmatrix} ,
> $$
>
> and a spinor with $h = +\frac12$ ($-\frac12$) is called right-handed (left-handed).
>
> **Step 2** (a product of three matrices). In the Weyl basis, $\gamma^0\gamma^i = \operatorname{diag}(-\sigma^i, \sigma^i)$ and $\gamma^5 = \operatorname{diag}(-\mathbb 1, \mathbb 1)$, so
>
> $$
> \gamma^5\gamma^0\gamma^i = \begin{pmatrix}\sigma^i & 0\\ 0 & \sigma^i\end{pmatrix} = 2S^i .
> $$
>
> **Step 3** (the Dirac equation). A particle spinor satisfies $\slashed p\,u = Mu$, with $\slashed p = E\gamma^0 - \mathbf p\cdot\boldsymbol\gamma$. Multiplying on the left by $\gamma^5\gamma^0$ and using $(\gamma^0)^2 = \mathbb 1$,
>
> $$
> E\,\gamma^5u - \gamma^5\gamma^0(\mathbf p\cdot\boldsymbol\gamma)\,u = M\,\gamma^5\gamma^0u ,
> $$
>
> and since $\gamma^5\gamma^0(\mathbf p\cdot\boldsymbol\gamma) = 2\,\mathbf p\cdot\mathbf S = 2|\mathbf p|\,h$,
>
> $$
> \gamma^5u = \frac{|\mathbf p|}{E}\,2h\,u + \frac{M}{E}\,\gamma^5\gamma^0u .
> $$
>
> **Step 4** (high energy). For $E \gg M$, $|\mathbf p|/E = \sqrt{1 - M^2/E^2} \to 1$ and the last term is suppressed by $M/E$, so $\gamma^5u = 2h\,u$. A right-handed fermion, $h = +\frac12$, therefore has $\gamma^5u = u$, i.e. $P_Ru = u$, and a left-handed one, $h = -\frac12$, has $P_Lu = u$. The spinor of a fermion with helicity $\lambda$ is thus $u_\lambda(p) = P_\lambda u(p)$, with $R \leftrightarrow h = +\frac12$ and $L \leftrightarrow h = -\frac12$. (End of the user's paragraph.)
>
> **What the derivation shows**
> - The chirality of a solution differs from twice its helicity by two effects of the mass: the factor $|\mathbf p|/E$, the speed, and the term $\frac ME\gamma^5\gamma^0u$, which lies in the other Weyl half (it is the component of relative size $M/2E$ of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2).
> - The "Weyl basis" of the problem set is the chiral basis of [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]]; $M$ is the fermion mass of the problem ($m$ there is the scalar mass).

^der-c8b-6-9

*Uses:* [[§C8b.5 Helicity Spinors and the Massless Limit#^def-c8b-5-1|Def. §C8b.5.1]], [[§C5a.1 Spinor Space and the Clifford Action#^def-c5a-1-4|Def. §C5a.1.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^thm-c5a-10-1|Theorem §C5a.10.1]]

> [!theorem] Theorem §C8b.6.10: The Scalar Vertex Flips the Helicity
> A Yukawa vertex ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]) joining an incoming fermion of momentum $p$ to an outgoing fermion of momentum $p'$ contributes the bilinear $\bar u(p')\,u(p)$, with no $\gamma$ between the spinors. With $u_\lambda(p) = P_\lambda u(p)$ and $\bar u_\lambda \equiv \overline{u_\lambda} = (P_\lambda u)^\dagger\gamma^0$, where $\lambda$ takes the value $R$, associated with $+1$, or $L$, associated with $-1$:
> 1. $\bar u(p')\,u(p) = \bar u_L(p')\,u_R(p) + \bar u_R(p')\,u_L(p)$;
> 2. for an incoming fermion of helicity $\lambda$ and an outgoing fermion of helicity $\lambda'$,
>
> $$
> \bar u_{\lambda'}(p')\,u_\lambda(p) = \bar u(p')\,P_{-\lambda'}P_\lambda\,u(p) , \qquad \text{which vanishes unless } \lambda' = -\lambda ;
> $$
>
> 3. **the Yukawa vertex flips the helicity of the fermion passing through it.** Helicity conservation in QED rests on the $\gamma^\mu$ of its vertex (Theorem §C8b.6.4); without it, as at a Yukawa vertex, the helicity flip is mandatory. Which of the two happens is dynamics, not kinematics.
>
> Parts 1–2 are the case $n = 0$ of Theorem §C8b.6.7, for the projections. They are statements about helicity at high energy, where $u_\lambda(p) = P_\lambda u(p)$ is the spinor of a fermion of helicity $\lambda$ (Theorem §C8b.6.9).
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] (the vertex $-ig$); *applies:* parts 1–2 are identities for every mass; part 3 for $E \gg M$, up to amplitudes of relative size $M/E$.
>
> *Source: PHY 513 Lecture 20 (16 Nov 2026), transcript, at slide 8 (helicity conservation holds because of the $\gamma^\nu$ in the vertex: "If I didn't have a $\gamma^\nu$ … helicity flip is mandatory"; "it's not something that is … kinematic, something that's dynamical") and again at slide 20 (for Yukawa the spin flip "is going to be mandatory") · the user's PHY 513 notes, Lecture 20 update, §20.2, paragraph "It is dynamics, not kinematics" ("A Yukawa vertex has no $\gamma$ between $\bar\psi$ and $\psi$, and then $\bar\psi\psi = \bar\psi_L\psi_R + \bar\psi_R\psi_L$") · PHY 513, Problem Set 11, Problem 1(a) (statement: "Derive the selection rule satisfied by helicity in the present context … Do not consider the explicit form of $u_\lambda(p)$"; the user's solution) · Yu §8.3, eqs. (8.169), (8.190)–(8.192)*

^thm-c8b-6-10

> [!derivation]- Derivation
> This is the user's submitted solution of PHY 513, Problem Set 11, Problem 1(a).
>
> **Step 1** (the bilinear in two parts). A Yukawa vertex joining an incoming fermion of momentum $p$ to an outgoing fermion of momentum $p'$ contributes the bilinear $\bar u(p')\,u(p)$. Since $P_R + P_L = \mathbb 1$, it separates into two parts,
>
> $$
> \bar u(p')\,u(p) = \bar u(p')\,P_R\,u(p) + \bar u(p')\,P_L\,u(p) .
> $$
>
> Since $P_R^2 = P_R$ and $P_L^2 = P_L$,
>
> $$
> \bar u(p')\,u(p) = \bar u(p')\,P_RP_R\,u(p) + \bar u(p')\,P_LP_L\,u(p) .
> $$
>
> **Step 2** (the left projector). The right projector in each term acts on $u(p)$ and gives $u_\lambda(p) = P_\lambda u(p)$. For the left one, $\{\gamma^5, \gamma^0\} = 0$ gives $\gamma^0P_R = P_L\gamma^0$ and $\gamma^0P_L = P_R\gamma^0$, and $(\gamma^5)^\dagger = \gamma^5$ gives $P_\lambda^\dagger = P_\lambda$. Hence
>
> $$
> \bar u(p')\,P_R = u^\dagger(p')\,\gamma^0P_R = u^\dagger(p')\,P_L\gamma^0 = \bigl(P_Lu(p')\bigr)^\dagger\gamma^0 = \bar u_L(p') ,
> $$
>
> and likewise $\bar u(p')\,P_L = \bar u_R(p')$, where $\bar u_\lambda \equiv \overline{u_\lambda} = (P_\lambda u)^\dagger\gamma^0$ denotes the Dirac conjugate of the projected spinor. Therefore
>
> $$
> \bar u(p')\,u(p) = \bar u_L(p')\,u_R(p) + \bar u_R(p')\,u_L(p) .
> $$
>
> **Step 3** (chirality and helicity). The user's second paragraph shows that for $E \gg M$ the spinor of a fermion with helicity $\lambda$ is $u_\lambda(p) = P_\lambda u(p)$; it has its own box, [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-9|Theorem §C8b.6.9]].
>
> **Step 4** (selection rule). For an incoming fermion of helicity $\lambda$ and an outgoing fermion of helicity $\lambda'$, the vertex is $\bar u_{\lambda'}(p')\,u_\lambda(p)$. As above, $\bar u_{\lambda'}(p') = \bar u(p')\,P_{-\lambda'}$, so
>
> $$
> \bar u_{\lambda'}(p')\,u_\lambda(p) = \bar u(p')\,P_{-\lambda'}P_\lambda\,u(p) ,
> $$
>
> which vanishes unless $-\lambda' = \lambda$, since $P_RP_L = P_LP_R = 0$. With $R = +1$ and $L = -1$,
>
> $$
> \lambda' = -\lambda :
> $$
>
> the Yukawa vertex flips the helicity of the fermion passing through it. (End of the user's solution of part (a).)
>
> **What the derivation shows**
> - Nothing about the explicit spinors is used, only the projector algebra; the same rule from the explicit high-energy spinors is [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-3|Theorem §C8b.11.3]] (Problem 1(d)).
> - ⚑ By-product: the conjugate of a projected spinor carries the opposite projector on its right, $\bar u_\lambda = \bar uP_{-\lambda}$; this is [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-2|Theorem §C8b.7.2]] for a bilinear without a $\gamma$.
> - Used next: which of the sixteen helicity amplitudes of $ff \to ff$ may be nonzero → [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]].

^der-c8b-6-10

*Uses:* [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^def-c8b-6-1|Def. §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-9|Theorem §C8b.6.9]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-2|P9, step 2]]

> [!theorem] Theorem §C8b.6.11: Selection Rules for Spinor Bilinears at High Energy
> Let $u(\mathbf p, \lambda) = u_\lambda(p)$ and $v(\mathbf p, \lambda) = v_\lambda(p)$ be the helicity spinors of [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]] and [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]] ($v(\mathbf p, \lambda)$ for an antifermion of helicity $\lambda$), $\lambda = \pm$, and let $\mathbf q$, $\mathbf p$ be any two momenta. In the high-energy limit, neglecting the mass ($\simeq$):
>
> | $\gamma$'s between the spinors | two $u$'s or two $v$'s | one $u$ and one $v$ |
> |---|---|---|
> | none | $\bar u(\mathbf q, \lambda)\,u(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, \lambda)\,v(\mathbf p, \lambda) \simeq 0$ | $\bar u(\mathbf q, -\lambda)\,v(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, -\lambda)\,u(\mathbf p, \lambda) \simeq 0$ |
> | one | $\bar u(\mathbf q, -\lambda)\gamma^\mu u(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, -\lambda)\gamma^\mu v(\mathbf p, \lambda) \simeq 0$ | $\bar u(\mathbf q, \lambda)\gamma^\mu v(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, \lambda)\gamma^\mu u(\mathbf p, \lambda) \simeq 0$ |
> | two | $\bar u(\mathbf q, \lambda)\gamma^\mu\gamma^\nu u(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, \lambda)\gamma^\mu\gamma^\nu v(\mathbf p, \lambda) \simeq 0$ | $\bar u(\mathbf q, -\lambda)\gamma^\mu\gamma^\nu v(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, -\lambda)\gamma^\mu\gamma^\nu u(\mathbf p, \lambda) \simeq 0$ |
> | three | $\bar u(\mathbf q, -\lambda)\gamma^\mu\gamma^\nu\gamma^\rho u(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, -\lambda)\gamma^\mu\gamma^\nu\gamma^\rho v(\mathbf p, \lambda) \simeq 0$ | $\bar u(\mathbf q, \lambda)\gamma^\mu\gamma^\nu\gamma^\rho v(\mathbf p, \lambda) \simeq 0$, $\ \bar v(\mathbf q, \lambda)\gamma^\mu\gamma^\nu\gamma^\rho u(\mathbf p, \lambda) \simeq 0$ |
>
> In words:
> 1. between two $u$'s, or two $v$'s, an even number of $\gamma$'s can couple only opposite helicities and an odd number only equal ones;
> 2. between a $u$ and a $v$ it is the other way round, because $v(\mathbf p, \lambda)$ has the chirality opposite to its helicity label (Theorem §C8b.6.2);
> 3. with no $\gamma$ this is the plane-wave form of the decomposition of $\bar\psi\psi$ (Theorem §C8b.6.7, 1): two spinors with nothing between them cannot couple equal helicities;
> 4. with the mass kept, each bilinear of the table is proportional to the mass instead of zero.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* helicity basis, any directions $\mathbf q$, $\mathbf p$; exact at $m = 0$, for $E \gg m$ up to terms of relative size $m/E$.
>
> *Source: Yu §8.3, eqs. (8.190)–(8.199) and the sentence between (8.191) and (8.192) ("此时两个平面波旋量系数之间夹着零个 Dirac 矩阵，不能耦合相同螺旋度，只能耦合相反螺旋度，这是左右手投影分解式 (8.169) 在平面波旋量系数上的体现") · the table and items 1–2, 4 arranged here (all sixteen relations and the proportionality to $m$ checked numerically, `qft-C/tools/hw11/verify.py`)*

^thm-c8b-6-11

> [!derivation]- Derivation
> **Step 1** (the projections at high energy). By Theorems §C8b.6.1–§C8b.6.2 with [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]] (Yu (8.179)–(8.186)): $u(\mathbf p, +) \simeq P_Ru(\mathbf p, +)$, $u(\mathbf p, -) \simeq P_Lu(\mathbf p, -)$, $v(\mathbf p, +) \simeq P_Lv(\mathbf p, +)$, $v(\mathbf p, -) \simeq P_Rv(\mathbf p, -)$, and for the conjugates $\bar u(\mathbf q, +) \simeq \bar u(\mathbf q, +)P_L$, $\bar u(\mathbf q, -) \simeq \bar u(\mathbf q, -)P_R$, $\bar v(\mathbf q, +) \simeq \bar v(\mathbf q, +)P_R$, $\bar v(\mathbf q, -) \simeq \bar v(\mathbf q, -)P_L$.
>
> **Step 2** (no $\gamma$; Yu (8.190)–(8.191)). The two projectors meet:
>
> $$
> \bar u(\mathbf q, -)\,u(\mathbf p, -) \simeq \bar u(\mathbf q, -)\,P_RP_L\,u(\mathbf p, -) = 0 , \qquad \bar u(\mathbf q, +)\,u(\mathbf p, +) \simeq \bar u(\mathbf q, +)\,P_LP_R\,u(\mathbf p, +) = 0 ,
> $$
>
> $$
> \bar v(\mathbf q, -)\,v(\mathbf p, -) \simeq \bar v(\mathbf q, -)\,P_LP_R\,v(\mathbf p, -) = 0 , \qquad \bar v(\mathbf q, +)\,v(\mathbf p, +) \simeq \bar v(\mathbf q, +)\,P_RP_L\,v(\mathbf p, +) = 0 .
> $$
>
> **Step 3** ($n$ matrices). Insert the projections of Step 1 and move the right projector to the left through $\Gamma_n$ (Step 2 of [[§C8b.6 Helicity Conservation at the QED Vertex#^der-c8b-6-7|Derivation §C8b.6.7]]): it arrives unchanged for $n$ even and exchanged for $n$ odd, and the product with the projector of the conjugate vanishes when the two differ. For two $u$'s: $\bar u(\mathbf q, \lambda')\,\Gamma_n\,u(\mathbf p, \lambda) \simeq \bar u(\mathbf q, \lambda')\,P_{-\lambda'}\,\Gamma_n\,P_\lambda\,u(\mathbf p, \lambda)$ (with $P_+ \equiv P_R$, $P_- \equiv P_L$), which is $\bar u\,P_{-\lambda'}P_\lambda\,\Gamma_n\,u$ for $n$ even, zero unless $\lambda' = -\lambda$, and $\bar u\,P_{-\lambda'}P_{-\lambda}\,\Gamma_n\,u$ for $n$ odd, zero unless $\lambda' = \lambda$. For two $v$'s every projector is the opposite one and the conclusion is the same. Left column.
>
> **Step 4** (a $u$ and a $v$). For $\bar u(\mathbf q, \lambda')\,\Gamma_n\,v(\mathbf p, \lambda)$ the right projector is $P_{-\lambda}$ in place of $P_\lambda$: the bilinear vanishes unless $\lambda' = \lambda$ for $n$ even and unless $\lambda' = -\lambda$ for $n$ odd; the same for $\bar v\,\Gamma_n\,u$. Right column.
>
> **Step 5** (item 4). With the mass kept, each spinor has its other Weyl half with amplitude $m/\sqrt{E + |\mathbf p|}$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2); a bilinear of the table then receives one large half and one small half, and is linear in $m$ to lowest order.
>
> **What the derivation shows**
> - One $\gamma$, a $u$ and a $v$ (Yu (8.197)): $\bar v(\mathbf q, \lambda)\gamma^\mu u(\mathbf p, \lambda) \simeq 0$ is Theorem §C8b.6.5, 1: a fermion does not annihilate with an antifermion of the same helicity.
> - No $\gamma$, two $u$'s (Yu (8.192)): the scalar vertex cannot keep the helicity → [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]].
> - Three $\gamma$'s and two $\gamma$'s between two $u$'s (Yu (8.195), (8.194)): the two terms of a fermion propagator between two vector vertices → [[§C8b.6 Helicity Conservation at the QED Vertex#^ex-c8b-6-1|Example §C8b.6.1]].

^der-c8b-6-11

*Uses:* [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-7|Theorem §C8b.6.7]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-2|Theorem §C8b.5.2]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-3|Theorem §C8b.5.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-2|P9, step 2]]

> [!example] Example §C8b.6.1: The Two Terms of the Electron Propagator in Compton Scattering
> ![[ph-qft-c8a-15-1.svg]]
> *The two diagrams of Compton scattering (the figure of [[§C8a.15 Compton Scattering꞉ the Amplitude and Its Square#^thm-c8a-15-1|Theorem §C8a.15.1]]). The example concerns diagram (b), the $u$-channel diagram, whose virtual electron carries $p - k'$.*
>
> At high energy the spinor string of diagram (b) is
>
> $$
> \bar u(p')\,\gamma^\nu\epsilon_\nu(k)\,\bigl(\slashed p - \slashed k' + m\bigr)\,\gamma^\mu\epsilon^\ast_\mu(k')\,u(p) .
> $$
>
> 1. The term with $\slashed p - \slashed k'$ has **three** $\gamma$'s between $\bar u$ and $u$. By Theorem §C8b.6.11 (three $\gamma$'s, two $u$'s) it vanishes for opposite helicities: if the initial electron is right-handed, the final electron must also be right-handed.
> 2. The term with $m$ has **two** $\gamma$'s between $\bar u$ and $u$. By Theorem §C8b.6.11 (two $\gamma$'s) it vanishes for equal helicities: it converts a right-handed electron into a left-handed electron.
> 3. So the electron keeps its helicity through the two vector vertices and the momentum part of the propagator, and the mass in the numerator of the propagator is what flips it.
>
> The block multiplication that shows both statements for this string, with the $2\times2$ matrices that result, is [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]]; what they imply for the backward peak is [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]].
>
> *Model:* [[§C8a.1 The QED Lagrangian and the Covariant Derivative#^mod-c8a-1-1|Model §C8a.1.1]] at order $e^2$; *applies:* $E, \omega \gg m$, helicity spinors in their high-energy form.
>
> *Source: PS §5.5, p. 165 ("Since this term contains three $\gamma$-matrices in (5.97) between the $\bar u$ and the $u$, the final electron must also be right-handed"), p. 166 ("This term contains only two gamma matrices and so converts a right-handed electron into a left-handed electron") · Yu §8.6.3, eq. (8.451), $\bar u(\mathbf p_1, -\lambda)\,\slashed\varepsilon(\mathbf k_2, \lambda_2)(\slashed k_1 - \slashed p_2)\slashed\varepsilon^\ast(\mathbf p_2, \lambda_2')\,u(\mathbf k_1, \lambda) \simeq 0$, obtained there from (8.195) (his labels: $k_1$, $p_1$ the incoming and outgoing electron, $k_2$, $p_2$ the photons) · checked numerically (`qft-C/tools/hw11/verify.py`)*

^ex-c8b-6-1

> [!remark] Remark: Helicity suppression
> In the high-energy limit, with the masses neglected, Theorem §C8b.6.11 leaves only the helicity configurations $\lambda_1 = -\lambda_2$, $\lambda_1' = -\lambda_2'$ of $e^+e^- \to \mu^+\mu^-$ with a nonzero amplitude (Theorem §C8b.6.5), in agreement with the explicit calculation ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]; ★ [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-4|Theorem §C8b.8.4]]). If the masses are not neglected, the other configurations contribute in proportion to the masses. This effect is called **helicity suppression**: an amplitude that violates helicity conservation is not forbidden but carries a factor $m/E$ for every helicity that a mass has to flip (Theorem §C8b.6.8, 2). The values for $e^+e^- \to \mu^+\mu^-$, with one or two such factors, are ★ [[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-5|Theorem §C8b.8.5]]–[[§C8b.8★ Polarized Amplitudes with Masses#^thm-c8b-8-7|Theorem §C8b.8.7]]; in backward Compton scattering the suppressed amplitude is the one that survives exactly backward ([[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-4|Theorem §C8b.10.4]]).
>
> *Source: Yu §8.3, p. 334, closing paragraph ("在高能极限下，忽略质量，只有 $\lambda_1 = -\lambda_2$ 且 $\lambda_1' = -\lambda_2'$ 的螺旋度构型对 $e^+e^- \to \mu^+\mu^-$ 极化振幅 (8.99) 的贡献非零 … 如果不忽略质量，则其它螺旋度构型的贡献正比于质量，表现出螺旋度压低效应")*

^rem-c8b-6-5

> [!abstract]- Mathematical background
> Proved in CB; each line says what the physics above relies on.
>
> - [[§CB.19 The Lorentz Case III꞉ the Dirac Module, Half-Spin Representations and γ⁵#^thm-cb-19-4|Theorem §CB.19.4]] — the eigenspaces of $\gamma^5$ are the Lorentz-invariant halves $(\frac12, 0)$, $(0, \frac12)$ in every basis: the two pieces that $P_L$, $P_R$ project onto and that the vector coupling keeps apart (physics form: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-2|Theorem §C5a.5.2]], Theorem §C8b.6.4, 3).
> - [[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-13-15|Theorem §CB.13.15]] — $(\gamma^5)^2 = \mathbb 1$, $\{\gamma^5, \gamma^\mu\} = 0$: $P_{L,R}$ are complementary projectors and $\gamma^5$ commutes with a product of two $\gamma$'s (physics form: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]]).

> [!remark]- Connections
> - Helicity of states for massless particles, its Lorentz invariance and why a massless particle has two helicities — [[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]], [[§C8b.3 Massless Particles and Helicity#^thm-c8b-3-5|Theorem §C8b.3.5]]; the Weyl fields that carry one helicity each — [[§C5a.8 The Weyl Form and the Weyl Equations#^mod-c5a-8-3|Model §C5a.8.3]].
> - Parity reverses helicity (momentum flips, spin does not), which is why the $e^-_Le^+_R$ results follow from the $e^-_Re^+_L$ ones — [[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-3|§C8b.3, Remark: Parity pairs λ with −λ]], [[§C9.3 Parity on States, Spinors and the Dirac Field|§C9.3]]; used in [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]].
> - The reversal for antiparticles is the same two-minus-signs mechanism as the positive antiparticle energy — [[§C9.8 Physical Spin versus Wave-Function Spin#^pr-c9-8-4|Principle §C9.8.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-1|§C5b.3, Remark: Two minus signs make a plus]].
> - The spin sums of [[§C8a.7 The Spin-Averaged Squared Amplitude|§C8a.7]] add the four allowed and the twelve vanishing helicity configurations; with projectors the same completeness relations give one configuration at a time — [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-3|Theorem §C8b.7.3]].
> - Mott's factor $1 - \beta^2\sin^2\frac\theta2$ and the spin term of ★ Theorem §C8a.11.6 concern the spin of an electron at the same vector vertex, scattered by a static field — see [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-3|Theorem §C8a.11.3]], 3, and [[§C8a.11 Mott's Formula꞉ the Relativistic Electron in a Coulomb Field#^thm-c8a-11-6|★ Theorem §C8a.11.6]].
> - The spin-one content of two spin-½ particles, $\frac12\otimes\frac12 = 0\oplus1$ — [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]].
> - A vertex without a $\gamma$ flips the helicity instead of keeping it; the helicity amplitudes of fermion–fermion scattering by scalar exchange, six of sixteen nonzero and all of them constants — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-10|Theorem §C8b.6.10]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-1|Theorem §C8b.11.1]], [[§C8b.11 Helicity Amplitudes in Yukawa Theory#^thm-c8b-11-9|Theorem §C8b.11.9]].
> - The same two diagrams with a photon: the vector vertex at equal momenta is $2p^\mu\delta_{\lambda\lambda'}$ for every mass, and the helicity-conserving amplitudes dominate near the forward and backward directions — [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-2|Theorem §C8b.12.2]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-3|Theorem §C8b.12.3]], [[§C8b.12 Helicity Amplitudes for Electron–Electron Scattering#^thm-c8b-12-4|Theorem §C8b.12.4]].
> - The mass term as the only term of the Dirac Lagrangian that joins the two Weyl fields, and the Dirac equation in two-component form — [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-1|Theorem §C5a.8.1]], [[§C5a.8 The Weyl Form and the Weyl Equations#^thm-c5a-8-2|Theorem §C5a.8.2]]; the electron propagator between two vector vertices, where the mass term of the numerator flips the helicity — [[§C8b.10 Helicity Suppression in Backward Compton Scattering#^thm-c8b-10-2|Theorem §C8b.10.2]].
