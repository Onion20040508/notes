---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C8b
section: C8b.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]] · ↑ [[· C8b Spin, Helicity and Chirality]] · [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]] →

*Sources: PHY 513 Lecture 20 (Larsen, 16 Nov 2026), slides 5–6, 14–20 (Part B), 23–28 (Part C), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.3 "Squaring with projectors" (eq. (MRR), Derivation "The conjugate keeps the projector on the right", paragraphs "Asked in the lecture: where did the $\gamma^\nu$ go …", "Sum over spins anyway", Principle "The projected trace", paragraphs "Asked in the lecture: the second term looks like a tensor …", "The muon vertex", Derivation "Contracting the two vertices"), §20.4 "Polarized cross sections" (paragraph "The average", Figure "helcurves", subsection "Angular momentum in the forward direction", Figure "helJz"), §20.5 "Explicit helicity spinors" (paragraph "Ultrarelativistic spinors", Derivation "The vertex as a polarization vector" and the paragraphs after it), Caution "Slips in the handwritten notes" (items 1–3 as general pitfalls), Summary, paragraph "Correspondence with Yu" · Peskin & Schroeder, An Introduction to Quantum Field Theory, §5.2, pp. 141–146, eqs. (5.17)–(5.32), Figure 5.4 (page images checked) · Yu Zhao-Huan, 量子场论讲义, §8.2.4, eqs. (8.99)–(8.142), (8.158), Figure 8.4 (page images of the current build checked).*

Which helicity configurations of $e^+e^- \to \mu^+\mu^-$ occur, and with which angular distribution? With the projected spinors and helicity conservation of [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]], this section squares the amplitude one helicity configuration at a time. The square still reduces to traces through completeness, now with a $\gamma^5$, and the $\gamma^5$ produces $\varepsilon$ symbols whose contraction makes the result simpler, not harder: $|\mathcal M|^2 = \frac{16e^4}{q^4}(p\cdot k')(p'\cdot k)$, which is $e^4(1 + \cos\theta)^2$ in the centre-of-mass frame ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-5|Theorem §C8b.7.5]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]). The two final helicities have opposite forward–backward preferences, their average is the unpolarized $1 + \cos^2\theta$ of [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]] ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-7|Theorem §C8b.7.7]]), and their zeros are fixed by angular momentum along the beam ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]). The last part computes the amplitude itself with explicit helicity spinors: each vertex is a spin-one polarization vector, and the amplitude is the overlap of a vector with its rotated image ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]). The steps are [[P9 Helicity Amplitudes|P9]]; the trace theorems are [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-3|Theorem §C5a.13.3]] and [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-4|Theorem §C5a.13.4]], the $\varepsilon\varepsilon$ contraction is [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]].

**The mathematical picture.** Each fermion line, projected and spin-summed, is a two-index tensor over spinor traces: a symmetric part (half the unpolarized tensor) and an antisymmetric part $\propto i\varepsilon^{\mu\rho\nu\sigma}p'_\rho p_\sigma$; together they form a Hermitian matrix in $\mu\nu$. Contracting two such tensors, symmetric with antisymmetric gives zero, and $\varepsilon$ with $\varepsilon$ gives products of $\delta$'s ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-6|Theorem §C1a.5.6]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]). With explicit spinors the same amplitude is the Minkowski product of two complex four-vectors, the circular polarization of spin one along the beam and its image under the rotation by $\theta$ about $\hat{\mathbf y}$, and the angular factors $\frac12(1 \pm \cos\theta)$ are the spin-one rotation matrix elements $d^1_{1,\pm1}(\theta)$ ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-3|QM Theorem §C5.3.3]]).

**Setup.** [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] at order $e^2$, the amplitude of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]], free states over $|0\rangle$, both masses set to zero ($m_e = m_\mu = 0$; with masses the helicity-violating amplitudes are suppressed, [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|§C8b.6, Remark: Frame and mass]]); helicities as in [[§C8b.3 Massless Particles and Helicity#^def-c8b-3-2|Def. §C8b.3.2]]. The invariant results (Theorems §C8b.7.1–§C8b.7.5) hold in every frame; from Theorem §C8b.7.6 on, the centre-of-mass frame of [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-1|Theorem §C8a.8.1]] with $|\mathbf k| = E$: $e^-$ along $+\hat{\mathbf z}$, $\mu^-$ at angle $\theta$ in the $xz$ plane.

*Conventions* ([[Larsen PHY 513]]): as in [[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]]; $\varepsilon^{0123} = +1$, $\varepsilon_{0123} = -1$; $q = p + p'$, $q^4 \equiv (q^2)^2$; the subscript of a particle is its physical helicity, of a spinor its projection.

## Squaring with projectors

> [!theorem] Theorem §C8b.7.1: The Projected Amplitude
> Inserting $P_R$ at both vertices of the amplitude of [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]],
>
> $$
> i\mathcal M_{RR} = \frac{ie^2}{q^2}\bigl(\bar v(p')\gamma^\mu P_Ru(p)\bigr)\bigl(\bar u(k)\gamma_\mu P_Rv(k')\bigr) ,
> $$
>
> is, at $m_e = m_\mu = 0$, the amplitude for $e^-_Re^+_L \to \mu^-_R\mu^+_L$. Replacing the second $P_R$ by $P_L$ gives $e^-_Re^+_L \to \mu^-_L\mu^+_R$; $P_L$ at the first vertex gives the initial state $e^-_Le^+_R$. The choice at each vertex is free.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, $m_e = m_\mu = 0$, any frame, any spin labels $s, s', r, r'$ (the projectors select the helicities).
>
> *Source: PHY 513 Lecture 20, slides 5, 7, 14–15, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.3, eq. (MRR) and the paragraph after it · PS §5.2, p. 142 (the replacement after (5.17)), p. 143 (the muon half (5.20))*

^thm-c8b-7-1

> [!derivation]- Derivation
> **Step 1** (electron line). $P_Ru(p) = u_R$: the right-handed electron ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]]); the vertex projects $v(p')$ onto $v_R$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]), a left-handed positron ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]).
>
> **Step 2** (muon line). $\bar u(k)\gamma_\mu P_Rv(k') = \bar uP_L\gamma_\mu v$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 2) $= \overline{P_Ru}\,\gamma_\mu v$ (same theorem, 4): the outgoing $\mu^-$ is $u_R$, right-handed. The projector also stands on $v(k')$, so $v(k') \to v_R$: a left-handed $\mu^+$.
>
> **Step 3** ($P_L$). The same steps with $L \leftrightarrow R$ give $\mu^-_L\mu^+_R$, and at the first vertex $e^-_Le^+_R$.

^der-c8b-7-1

*Uses:* [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-2|P9, step 2]]

> [!theorem] Theorem §C8b.7.2: The Conjugate Keeps the Projector on the Right
> For any spinors $u$, $v$,
>
> $$
> \bigl(\bar v\gamma^\mu P_Ru\bigr)^\ast = \bar uP_L\gamma^\mu v = \bar u\gamma^\mu P_Rv ,
> $$
>
> and the same with $L \leftrightarrow R$: the conjugate of a projected vector bilinear is the reversed bilinear with the same projector, still to the right of $\gamma^\mu$.
>
> *Model:* none; *applies:* c-number spinors, any mass.
>
> *Source: PHY 513 Lecture 20, slide 14 (the second factor $\bar u(p)\gamma^\nu\frac{1 + \gamma^5}{2}v(p')$), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.3, Derivation "The conjugate keeps the projector on the right" · PS §5.2, p. 142 (the first line of the electron half)*

^thm-c8b-7-2

> [!derivation]- Derivation
> **Step 1** (conjugate as Hermitian conjugate). As in [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-1|Theorem §C8a.7.1]], $(\bar v\gamma^\mu P_Ru)^\ast = (v^\dagger\gamma^0\gamma^\mu P_Ru)^\dagger = u^\dagger P_R^\dagger\gamma^{\mu\dagger}\gamma^{0\dagger}v$.
>
> **Step 2** (Hermiticity). $P_R^\dagger = P_R$, $\gamma^{0\dagger} = \gamma^0$, and $\gamma^{\mu\dagger}\gamma^0 = \gamma^0\gamma^\mu$ (the step of [[§C8a.7 The Spin-Averaged Squared Amplitude#^der-c8a-7-1|Derivation §C8a.7.1]]): $= u^\dagger P_R\gamma^0\gamma^\mu v$.
>
> **Step 3** (move the projector). $P_R\gamma^0 = \gamma^0P_L$ ([[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]], 2): $= u^\dagger\gamma^0P_L\gamma^\mu v = \bar uP_L\gamma^\mu v = \bar u\gamma^\mu P_Rv$.
>
> **What the derivation shows**
> - The $\gamma^0$ hidden in the bar turns $P_R$ into $P_L$ when it moves past; written to the right of $\gamma^\mu$ the projector is again $P_R$, the same projector on every factor → [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^cau-c8b-7-1|Caution: The projector of the conjugate stands to the right of γ]].

^der-c8b-7-2

*Uses:* [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-1|Theorem §C8a.7.1]], [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-3|Theorem §C5a.5.3]]

> [!caution] Caution: The projector of the conjugate stands to the right of γ
> The conjugate of $\bar v\gamma^\mu P_Ru$ is $\bar u\gamma^\nu P_Rv = \bar uP_L\gamma^\nu v$, not $\bar uP_R\gamma^\nu v$ (a question in the lecture). Keep the projector consistently to the right of each $\gamma$. With the wrong placement one trace would contain $P_R$ and $P_L$ next to each other, $\operatorname{tr}[\slashed p'\gamma^\mu P_R\slashed p\gamma^\nu P_L] = \operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu P_RP_L] = 0$: the error shows up at once.
>
> *Source: PHY 513 Lecture 20, transcript · the user's PHY 513 notes, Lecture 20 update, §20.3, paragraph "Asked in the lecture: where did the $\gamma^\nu$ go …"; Caution "Slips in the handwritten notes", item 1*

^cau-c8b-7-1

> [!theorem] Theorem §C8b.7.3: With Projectors the Spin Sum Is Still a Trace
> At $m = 0$,
>
> $$
> \sum_{s, s'}\bigl(\bar v^{s'}(p')\gamma^\mu P_Ru^s(p)\bigr)\bigl(\bar u^s(p)\gamma^\nu P_Rv^{s'}(p')\bigr) = \operatorname{tr}\bigl[\slashed p'\gamma^\mu P_R\slashed p\gamma^\nu P_R\bigr] = \operatorname{tr}\Bigl[\slashed p'\gamma^\mu\slashed p\gamma^\nu\,\frac{1 + \gamma^5}{2}\Bigr] .
> $$
>
> 1. The projectors, not the labels $s$, $s'$, select the helicities: the terms of the wrong helicity are summed but vanish. So the sum over $s, s'$ may be taken with the completeness relations $\sum_su\bar u = \slashed p$, $\sum_sv\bar v = \slashed p'$ at $m = 0$ ([[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]]), exactly as in [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|Theorem §C8a.7.3]].
> 2. The result is **one** helicity configuration: there is no factor $\frac14$.
> 3. The masses are set to zero: the projectors select helicities only at $m = 0$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]]; [[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|§C8b.6, Remark: Frame and mass]]).
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]] (the spinors); *applies:* $m = 0$, on-shell momenta, any spin basis.
>
> *Source: PHY 513 Lecture 20, slide 14 ("Note: $u$ and $v$ both projected on 'R'. Completeness (for massless spinors): $u(p)\bar u(p) \to \slashed p$"; the trace and its reduction), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.3, paragraph "Sum over spins anyway" · PS §5.2, p. 142 ("of the four terms in the sum, only one (the one we want) is nonzero")*

^thm-c8b-7-3

> [!derivation]- Derivation
> **Step 1** (completeness). By the steps of [[§C8a.7 The Spin-Averaged Squared Amplitude#^der-c8a-7-3|Derivation §C8a.7.3]] with $\gamma^\mu P_R$ and $\gamma^\nu P_R$ in place of $\gamma^\mu$ and $\gamma^\nu$ (the general form is [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]] with $\Gamma = \gamma^\mu P_R$, $\bar\Gamma = \gamma^0P_R\gamma^{\mu\dagger}\gamma^0 = P_L\gamma^\mu = \gamma^\mu P_R$ as in Theorem §C8b.7.2, with $\mu$ renamed $\nu$): $\sum = \operatorname{tr}[(\sum_{s'}v^{s'}\bar v^{s'})\gamma^\mu P_R(\sum_su^s\bar u^s)\gamma^\nu P_R] = \operatorname{tr}[\slashed p'\gamma^\mu P_R\slashed p\gamma^\nu P_R]$.
>
> **Step 2** (one projector). $P_R$ commutes with $\slashed p\gamma^\nu$, two $\gamma$'s ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], Step 3): $\operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu P_RP_R] = \operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu P_R]$ ($P_R^2 = P_R$).
>
> **Step 3** (which terms survive). In the sum over $s$ only the spinor with $P_Ru^s \ne 0$ contributes, $u_+$ in the helicity basis ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]]); likewise only one $v^{s'}$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]). Of the four terms one is nonzero, and it is the configuration $e^-_Re^+_L$ itself, not an average.

^der-c8b-7-3

*Uses:* [[§C8a.7 The Spin-Averaged Squared Amplitude#^der-c8a-7-3|Derivation §C8a.7.3]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-7|Theorem §C8a.7.7]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-3|P9, step 3]]

> [!caution] Caution: No ¼ for one helicity configuration
> The projected $\sum_{s, s'}$ is a device for using completeness, not an average: it equals the squared amplitude of one helicity configuration. Writing $\frac14\sum_{\rm spin}$ in front of it would divide a single configuration by 4. The factor $\frac14$ belongs only to the average over the four initial helicity combinations ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-7|Theorem §C8b.7.7]]).
>
> *Source: the user's PHY 513 notes, Lecture 20 update, §20.3, paragraph "Sum over spins anyway"; Caution "Slips in the handwritten notes", item 2*

^cau-c8b-7-2

> [!theorem] Theorem §C8b.7.4: The Projected Traces
> For any four-vectors (here the massless momenta of the two lines), with $\varepsilon^{0123} = +1$:
>
> $$
> \operatorname{tr}\Bigl[\slashed p'\gamma^\mu\slashed p\gamma^\nu\,\frac{1 \pm \gamma^5}{2}\Bigr] = 2\bigl(p'^\mu p^\nu + p'^\nu p^\mu - g^{\mu\nu}\,p\cdot p'\bigr) \mp 2i\,\varepsilon^{\mu\rho\nu\sigma}p'_\rho p_\sigma ,
> $$
>
> $$
> \operatorname{tr}\Bigl[\slashed k\gamma_\mu\slashed k'\gamma_\nu\,\frac{1 \pm \gamma^5}{2}\Bigr] = 2\bigl(k_\mu k'_\nu + k_\nu k'_\mu - g_{\mu\nu}\,k\cdot k'\bigr) \mp 2i\,\varepsilon_{\mu\alpha\nu\beta}k^\alpha k'^\beta ,
> $$
>
> upper signs for $P_R$, lower for $P_L$.
> 1. The first part is half the unprojected trace of [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-5|Theorem §C8a.7.5]] at $m = 0$, the same as averaging over the spin; it is symmetric in $\mu\nu$.
> 2. The second part, the helicity dependence, comes from $\operatorname{tr}(\gamma^\alpha\gamma^\beta\gamma^\gamma\gamma^\delta\gamma^5) = -4i\varepsilon^{\alpha\beta\gamma\delta}$ ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-4|Theorem §C5a.13.4]]); it is antisymmetric in $\mu\nu$.
> 3. The muon trace is the electron trace with $p' \to k$, $p \to k'$ (the order along the muon line, [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|Theorem §C8a.7.3]]) and the indices lowered; its $\varepsilon$ term carries $k$ before $k'$.
>
> *Model:* none (Dirac algebra); *applies:* any four-vectors; the mass shell is not used.
>
> *Source: PHY 513 Lecture 20, slide 14 ("$= 2\bigl(\underbrace{p'^\mu p^\nu + p'^\nu p^\mu - g^{\mu\nu}p\cdot p'}_{\text{same as averaging over spin}} - \underbrace{i\epsilon^{\alpha\mu\beta\nu}p'_\alpha p_\beta}_{\text{helicity dependence}}\bigr)$", the same term since $\epsilon^{\alpha\mu\beta\nu} = \epsilon^{\mu\alpha\nu\beta}$), slides 15, 17, and transcript; the cheat sheet of slide 2 writes the $\gamma^5$ trace without the factor 4 (`qft-C/ERRATA.md`) · the user's PHY 513 notes, Lecture 20 update, §20.3, Principle "The projected trace", eq. (trgamma5) ("checked numerically"), paragraph "The muon vertex" · PS §5.2, p. 143, eqs. (5.19)–(5.20) (with the $\epsilon$ convention discussed in [[§C5a.13 Gamma-Matrix Technology#^cau-c5a-13-1|§C5a.13, Caution: The sign of the ε trace across sources]])*

^thm-c8b-7-4

> [!derivation]- Derivation
> **Step 1** (split). $\frac{1 \pm \gamma^5}{2}$: the trace is $\frac12\operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu] \pm \frac12\operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu\gamma^5]$.
>
> **Step 2** (the first half). $\operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu] = 4(p'^\mu p^\nu + p'^\nu p^\mu - g^{\mu\nu}p\cdot p')$ ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-5|Theorem §C8a.7.5]] at $m_e = 0$); half of it is the first part.
>
> **Step 3** (the $\gamma^5$ half). Write the slashes with their indices, $\slashed p' = p'_\rho\gamma^\rho$, $\slashed p = p_\sigma\gamma^\sigma$: $\operatorname{tr}[\slashed p'\gamma^\mu\slashed p\gamma^\nu\gamma^5] = p'_\rho p_\sigma\operatorname{tr}[\gamma^\rho\gamma^\mu\gamma^\sigma\gamma^\nu\gamma^5] = -4i\,\varepsilon^{\rho\mu\sigma\nu}p'_\rho p_\sigma$ ([[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-4|Theorem §C5a.13.4]]).
>
> **Step 4** (the index shuffle). $\varepsilon^{\rho\mu\sigma\nu} \to \varepsilon^{\mu\rho\sigma\nu}$ exchanges the first two indices (sign $-1$), and $\varepsilon^{\mu\rho\sigma\nu} \to \varepsilon^{\mu\rho\nu\sigma}$ the last two (sign $-1$): $\varepsilon^{\rho\mu\sigma\nu} = +\varepsilon^{\mu\rho\nu\sigma}$. So $\pm\frac12(-4i)\varepsilon^{\mu\rho\nu\sigma}p'_\rho p_\sigma = \mp2i\,\varepsilon^{\mu\rho\nu\sigma}p'_\rho p_\sigma$.
>
> **Step 5** (the muon line). The muon trace of [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|Theorem §C8a.7.3]] at $m_\mu = 0$, with $P$ moved as in [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^der-c8b-7-3|Derivation §C8b.7.3]], is $\operatorname{tr}[\slashed k\gamma_\mu\slashed k'\gamma_\nu P]$: Steps 1–4 with $p' \to k$, $p \to k'$ and lower indices, $\varepsilon^{\rho\mu\sigma\nu}k_\rho k'_\sigma \to \varepsilon_{\alpha\mu\beta\nu}k^\alpha k'^\beta = \varepsilon_{\mu\alpha\nu\beta}k^\alpha k'^\beta$.
>
> **What the derivation shows**
> - ⚑ By-product: the order of the two momenta in the $\varepsilon$ term follows the fermion line; exchanging them flips its sign → [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^cau-c8b-7-3|Caution: The εε contraction has −2 in Minkowski space]] (second paragraph).
> - Both traces checked numerically (`qft-C/tools/l20/verify.py`), also Hermiticity in $\mu\nu$ (next remark).

^der-c8b-7-4

*Uses:* [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-5|Theorem §C8a.7.5]], [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-4|Theorem §C5a.13.4]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-3|Theorem §C8a.7.3]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-4|P9, step 4]]

> [!remark] Remark: Two tensors of different symmetry, and why the γ⁵ trace is an ε
> Asked in the lecture: the second term looks like a tensor, yet the trace was already taken. The trace is over spinor indices; the Lorentz indices $\mu$, $\nu$ stay. Read $\slashed p'$ and $\slashed p$ for a moment as $\gamma^\rho$, $\gamma^\sigma$: four free indices give an $\varepsilon$, and contracting two of them with $p'$ and $p$ leaves a two-index object. Both terms are tensors with different structures: the first is symmetric in $\mu\nu$, the second antisymmetric, and the $i$ goes with the antisymmetry, since the whole trace is a Hermitian matrix in $\mu\nu$ (it is $\sum$ of a bilinear times its conjugate). Why the $\gamma^5$ trace is an $\varepsilon$: $\gamma^5$ is itself $i\gamma^0\gamma^1\gamma^2\gamma^3$, so the trace of four $\gamma$'s with $\gamma^5$ can be nonzero only if the four are $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ in some order, and it is antisymmetric in all four: an $\varepsilon$ symbol, with an explicit $i$ because $\gamma^5$ carries one ([[§C5a.13 Gamma-Matrix Technology#^der-c5a-13-4|Derivation §C5a.13.4]], Steps 4–6). Once $\gamma^5$'s are present, traces tend to give $\varepsilon$'s: a feature of helicity amplitudes.
>
> *Source: PHY 513 Lecture 20, transcript · the user's PHY 513 notes, Lecture 20 update, §20.3, paragraph "Asked in the lecture: the second term looks like a tensor, but we already took the trace?" and the paragraph before it*

^rem-c8b-7-1

> [!theorem] Theorem §C8b.7.5: The Polarized Squared Amplitudes in Invariants
> At order $e^2$ with $m_e = m_\mu = 0$, in any frame,
>
> $$
> |\mathcal M(e^-_Re^+_L \to \mu^-_R\mu^+_L)|^2 = \frac{16e^4}{q^4}\,(p\cdot k')(p'\cdot k) , \qquad |\mathcal M(e^-_Re^+_L \to \mu^-_L\mu^+_R)|^2 = \frac{16e^4}{q^4}\,(p\cdot k)(p'\cdot k') .
> $$
>
> 1. Of the two products of the unpolarized result ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] at zero masses) each configuration keeps one, with twice the weight: the $\varepsilon\varepsilon$ term cancels one and doubles the other.
> 2. The projection made the result simpler, not harder: a single product.
> 3. Checked numerically by the traces and by explicit spinors.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* order $e^2$, $m_e = m_\mu = 0$, fixed helicities, any frame.
>
> *Source: PHY 513 Lecture 20, slides 15–16 ("$|\mathcal M|^2 = \frac{4e^4}{q^4}[2(pk\,p'k' + p'k\,pk') - 2(pk\,p'k' - p'k\,pk')] = \frac{16e^4}{q^4}(pk')(p'k)$"), slides 17–18 ("L spinors for $e^-e^+$ or $\mu^-\mu^+$: $\epsilon\times\epsilon$ term changes sign"; $\frac{16e^4}{q^4}(pk)(p'k')$), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.3, Derivation "Contracting the two vertices", eq. (MRRinv) · PS §5.2, p. 143, eq. (5.21) (first three lines) · numerical check: `qft-C/tools/l20/verify.py`*

^thm-c8b-7-5

> [!derivation]- Derivation
> **Step 1** (the product of the lines). $|\mathcal M|^2 = \frac{e^4}{q^4}E^{\mu\nu}M_{\mu\nu}$ with $E^{\mu\nu}$ the electron trace and $M_{\mu\nu}$ the muon trace of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-4|Theorem §C8b.7.4]] (Theorem §C8b.7.3 for each line; the factor $\frac{ie^2}{q^2}$ of Theorem §C8b.7.1 gives $\frac{e^4}{q^4}$). Write $E = S_e - 2i\,\varepsilon^{\mu\rho\nu\sigma}p'_\rho p_\sigma$, $M = S_\mu \mp 2i\,\varepsilon_{\mu\alpha\nu\beta}k^\alpha k'^\beta$ (upper sign $\mu^-_R\mu^+_L$, lower $\mu^-_L\mu^+_R$), with $S_e$, $S_\mu$ the symmetric parts. Four products:
>
> **Step 2** (symmetric × symmetric). $S_e = \frac12\cdot4A$, $S_\mu = \frac12\cdot4B$ with $A$, $B$ of [[§C8a.7 The Spin-Averaged Squared Amplitude#^der-c8a-7-6|Derivation §C8a.7.6]] at zero masses, where $A^{\mu\nu}B_{\mu\nu} = 2[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)]$ (its Step 3: the $(p\cdot p')(k\cdot k')$ terms cancel, $4 - 2 - 2 = 0$). So $S_eS_\mu = 4\cdot2[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)]$.
>
> **Step 3** (mixed). A symmetric tensor contracted with an antisymmetric one vanishes: $S^{\mu\nu}a_{\mu\nu} = S^{\nu\mu}a_{\mu\nu} = -S^{\nu\mu}a_{\nu\mu} = -S^{\mu\nu}a_{\mu\nu}$ (swap, then rename). Both mixed products are $0$.
>
> **Step 4** ($\varepsilon\varepsilon$, upper sign). $(-2i)(-2i)\,\varepsilon^{\mu\rho\nu\sigma}\varepsilon_{\mu\alpha\nu\beta}\,p'_\rho p_\sigma k^\alpha k'^\beta = -4\,\varepsilon^{\mu\rho\nu\sigma}\varepsilon_{\mu\alpha\nu\beta}\,p'_\rho p_\sigma k^\alpha k'^\beta$. Bring the contracted indices to the front of both symbols, one transposition each: $\varepsilon^{\mu\rho\nu\sigma}\varepsilon_{\mu\alpha\nu\beta} = (-\varepsilon^{\mu\nu\rho\sigma})(-\varepsilon_{\mu\nu\alpha\beta}) = -2(\delta^\rho_\alpha\delta^\sigma_\beta - \delta^\rho_\beta\delta^\sigma_\alpha)$ ([[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]], 1, the two-index contraction, upper and lower roles exchanged). Contracting, $-2[(p'\cdot k)(p\cdot k') - (p'\cdot k')(p\cdot k)]$, so the term is $-4\cdot(-2)[(p'\cdot k)(p\cdot k') - (p'\cdot k')(p\cdot k)] = 8[(p\cdot k')(p'\cdot k) - (p\cdot k)(p'\cdot k')]$.
>
> **Step 5** (add). $8[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)] + 8[(p\cdot k')(p'\cdot k) - (p\cdot k)(p'\cdot k')] = 16(p\cdot k')(p'\cdot k)$: one term cancels, one doubles. Times $\frac{e^4}{q^4}$: the first result.
>
> **Step 6** (lower sign). With $P_L$ on the muon line the $\varepsilon\varepsilon$ coefficient is $(-2i)(+2i) = +4$, the term of Step 4 changes sign, and the sum is $16(p\cdot k)(p'\cdot k')$: the second result.
>
> **What the derivation shows**
> - ⚑ By-product: the $\varepsilon\varepsilon$ term is the difference of the two products of the unpolarized result; it decides which of them survives. Its sign depends on the $-2$ of the Minkowski contraction and on the order of the momenta → [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^cau-c8b-7-3|Caution: The εε contraction has −2 in Minkowski space]].
> - The two configurations sum to $16[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)]$, twice the unpolarized bracket of Theorem §C8a.7.6 (used in [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-7|Theorem §C8b.7.7]]).
> - Checked numerically (`qft-C/tools/l20/verify.py`): every product, the identity, and the result against explicit helicity spinors.

^der-c8b-7-5

*Uses:* [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-3|Theorem §C8b.7.3]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-4|Theorem §C8b.7.4]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^der-c8a-7-6|Derivation §C8a.7.6]], [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-4|P9, step 4]]

> [!caution] Caution: The εε contraction has −2 in Minkowski space
> $\varepsilon^{\mu\rho\nu\sigma}\varepsilon_{\mu\alpha\nu\beta} = -2(\delta^\rho_\alpha\delta^\sigma_\beta - \delta^\rho_\beta\delta^\sigma_\alpha)$: the Euclidean identity has $+2$, and lowering all four indices of one symbol costs $\det g = -1$ ($\varepsilon_{0123} = -\varepsilon^{0123}$; [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]]). Combined with $(\mp2i)^2 = -4$ this gives the sign of Step 4 above.
>
> Slide 16 writes the contraction with $+2$, and slide 15 writes the muon $\varepsilon$ term with $k'$ before $k$ (from "same as $e^-e^+$ except $(p, p') \to (k, k')$"); the muon line maps onto the electron trace by $p' \to k$, $p \to k'$ (Theorem §C8b.7.4, 3), so the correct order is $k$ before $k'$. Each of the two changes flips the sign of the $\varepsilon\varepsilon$ term, and together they cancel: the slide's final $\frac{16e^4}{q^4}(pk')(p'k)$ is right, while either one alone would give $(1 - \cos\theta)^2$ in place of $(1 + \cos\theta)^2$ (checked numerically, `qft-C/tools/l20/verify.py`; `qft-C/ERRATA.md`).
>
> *Source: the user's PHY 513 notes, Lecture 20 update, §20.3, Derivation "Contracting the two vertices" ("with a minus sign in Minkowski space because $\varepsilon_{0123} = -\varepsilon^{0123}$"); Caution "Slips in the handwritten notes", item 3 · PHY 513 Lecture 20, slides 15–16*

^cau-c8b-7-3

## Polarized cross sections

> [!theorem] Theorem §C8b.7.6: The Polarized Cross Sections in the Centre-of-Mass Frame
> In the centre-of-mass frame with $m_e = m_\mu = 0$ and $\theta$ the angle of the $\mu^-$ to the $e^-$:
>
> $$
> |\mathcal M(e^-_Re^+_L \to \mu^-_R\mu^+_L)|^2 = e^4(1 + \cos\theta)^2 , \qquad |\mathcal M(e^-_Re^+_L \to \mu^-_L\mu^+_R)|^2 = e^4(1 - \cos\theta)^2 ,
> $$
>
> $$
> \frac{d\sigma}{d\Omega}(e^-_Re^+_L \to \mu^-_R\mu^+_L) = \frac{\alpha^2}{4E_{\rm cm}^2}(1 + \cos\theta)^2 , \qquad \frac{d\sigma}{d\Omega}(e^-_Re^+_L \to \mu^-_L\mu^+_R) = \frac{\alpha^2}{4E_{\rm cm}^2}(1 - \cos\theta)^2 .
> $$
>
> 1. *Parity.* For $e^-_Le^+_R$ the same two results hold with all helicities reversed: $e^-_Le^+_R \to \mu^-_L\mu^+_R$ has $(1 + \cos\theta)^2$ and $e^-_Le^+_R \to \mu^-_R\mu^+_L$ has $(1 - \cos\theta)^2$.
> 2. *The other twelve* helicity configurations ($e^-_Re^+_R$, $e^-_Le^+_L$, or a final pair $\mu^-_R\mu^+_R$, $\mu^-_L\mu^+_L$) vanish ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]]).
>
> *Model:* [[§C6b.2 Transition Probabilities in a Box#^mod-c6b-2-1|Model §C6b.2.1]] with [[§C6b.3 The Cross Section#^mod-c6b-3-1|Model §C6b.3.1]] for the cross section, [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]] for $\mathcal M$; *applies:* order $\alpha^2$, polarized beams and helicity-resolved detection, $m_e = m_\mu = 0$ ($E_{\rm cm} \gg 2m_\mu$).
>
> *Source: PHY 513 Lecture 20, slides 16, 18, 19 ("Final results (use $\alpha = \frac{e^2}{4\pi}$)"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.4, eqs. (Mhel), (dsdOhel), and the paragraph after them (parity: filled in) · PS §5.2, p. 143, eqs. (5.21)–(5.24) · Yu §8.2.4, eqs. (8.136)–(8.142) (with $\beta$ factors for finite masses; parity (8.140))*

^thm-c8b-7-6

> [!derivation]- Derivation
> **Step 1** (invariants). [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-2|Theorem §C8a.8.2]] with $|\mathbf k| = E$ ($m_\mu = 0$): $p\cdot k' = p'\cdot k = E^2(1 + \cos\theta)$, $p\cdot k = p'\cdot k' = E^2(1 - \cos\theta)$, $q^2 = 4E^2$, $q^4 = 16E^4$.
>
> **Step 2** ($|\mathcal M|^2$). [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-5|Theorem §C8b.7.5]]: $\frac{16e^4}{16E^4}E^4(1 + \cos\theta)^2 = e^4(1 + \cos\theta)^2$, and the same with $1 - \cos\theta$.
>
> **Step 3** (cross section). For massless particles in the centre-of-mass frame $\frac{d\sigma}{d\Omega} = \frac{|\mathcal M|^2}{64\pi^2E_{\rm cm}^2}$ ([[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]] with $E_A = E_B = \frac12E_{\rm cm}$, $|\mathbf v_A - \mathbf v_B| = 2$, $|\mathbf p_1| = \frac12E_{\rm cm}$, as in [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^der-c8a-8-4|Derivation §C8a.8.4]] at $m_\mu = 0$), here with $|\mathcal M|^2$ of one configuration in place of the spin average. With $e^4 = 16\pi^2\alpha^2$: $\frac{16\pi^2\alpha^2(1 \pm \cos\theta)^2}{64\pi^2E_{\rm cm}^2} = \frac{\alpha^2}{4E_{\rm cm}^2}(1 \pm \cos\theta)^2$.
>
> **Step 4** (parity). Parity reverses every momentum and keeps every spin, so it reverses every helicity and maps the configuration at angle $\theta$ to the reversed configuration at the same $\theta$ (all momenta reversed keep the angle between $\mathbf k$ and $\mathbf p$); QED is parity invariant, so $|\mathcal M|$ is unchanged ([[§C8b.3 Massless Particles and Helicity#^rem-c8b-3-3|§C8b.3, Remark: Parity pairs λ with −λ]]; [[§C9.4 Fermion Bilinears under Parity|§C9.4]]; Yu (8.140)). Directly: $P_L$ at both vertices changes the sign of both $\varepsilon$ terms, and the $\varepsilon\varepsilon$ product is unchanged.
>
> **Step 5** (the zeros). [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]] at each vertex.

^der-c8b-7-6

*Uses:* [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-2|Theorem §C8a.8.2]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-5|Theorem §C8b.7.5]], [[§C6b.4 Two-Body Scattering Kinematics#^thm-c6b-4-4|Theorem §C6b.4.4]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-5|P9, step 5]]

> [!remark] Remark: Exchanging the outgoing particles flips the muon helicities
> The two results are related geometrically. At fixed muon spins along the beam, exchanging which outgoing particle goes where puts the $\mu^-$ at $\pi - \theta$ instead of $\theta$ and turns a right-handed muon pair into a left-handed one; $\cos\theta \to -\cos\theta$ maps $(1 + \cos\theta)^2$ onto $(1 - \cos\theta)^2$. Slide 18 says the same as "final state rotated $\theta \to \theta + \pi$": both $\pi - \theta$ and $\theta + \pi$ send $\cos\theta$ to $-\cos\theta$.
>
> *Source: PHY 513 Lecture 20, slide 18 ("Net effect: $(1 + \cos\theta)^2 \to (1 - \cos\theta)^2$. Equivalently: final state rotated $\theta \to \theta + \pi$"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.4 (the paragraph after the parity sentence)*

^rem-c8b-7-2

> [!theorem] Theorem §C8b.7.7: The Average over Helicities Is the Unpolarized Result
> ![[ph-qft-c8-13-1.svg]]
> *The user's figure "helcurves" (Lecture 20 update, §20.4) redrawn: $|\mathcal M|^2/e^4$ for $e^-_Re^+_L \to \mu^-_R\mu^+_L$ (blue) and $\to \mu^-_L\mu^+_R$ (orange), each vanishing at one end, and their average over initial helicities, $1 + \cos^2\theta$ (dashed).*
>
> Averaging over the four initial helicity combinations and summing over the final ones,
>
> $$
> \frac14\sum_{\rm helicities}|\mathcal M|^2 = \frac14\,e^4\bigl[2(1 + \cos\theta)^2 + 2(1 - \cos\theta)^2\bigr] = e^4(1 + \cos^2\theta) ,
> $$
>
> which is [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]] at $m_\mu = 0$, and $\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{4E_{\rm cm}^2}(1 + \cos^2\theta)$ is [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-4|Theorem §C8a.8.4]] at $m_\mu = 0$. The unpolarized $1 + \cos^2\theta$ is the sum of two quite different distributions: the spin detail gives more than the average.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* as Theorem §C8b.7.6; unpolarized beams and undetected final helicities ([[§C8a.7 The Spin-Averaged Squared Amplitude#^def-c8a-7-1|Def. §C8a.7.1]]).
>
> *Source: PHY 513 Lecture 20, slide 19 ("$\frac{\alpha^2}{4E_{\rm cm}^2}(1 + \cos^2\theta)$, average"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.4, paragraph "The average" ("checked numerically"), Figure "helcurves" · PS §5.2, p. 143 (the paragraph after (5.24)) · Yu §8.2.4, eq. (8.158) (all sixteen with masses)*

^thm-c8b-7-7

> [!derivation]- Derivation
> **Step 1** (sixteen terms). Each of $e^-$, $e^+$, $\mu^-$, $\mu^+$ has two helicities: sixteen configurations. By [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]] four are nonzero: $(1 + \cos\theta)^2$ twice ($e^-_Re^+_L \to \mu^-_R\mu^+_L$, $e^-_Le^+_R \to \mu^-_L\mu^+_R$), $(1 - \cos\theta)^2$ twice.
>
> **Step 2** (sum). $2(1 + 2\cos\theta + \cos^2\theta) + 2(1 - 2\cos\theta + \cos^2\theta) = 4 + 4\cos^2\theta$; times $\frac14e^4$: $e^4(1 + \cos^2\theta)$.
>
> **Step 3** (compare). [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]] at $m_\mu = 0$ is $e^4(1 + \cos^2\theta)$. Equivalently, in invariants the four configurations sum to $2\cdot16[(p\cdot k)(p'\cdot k') + (p\cdot k')(p'\cdot k)]e^4/q^4$ (last bullet of [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^der-c8b-7-5|Derivation §C8b.7.5]], twice for the two initial pairs), and $\frac14$ of it is [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]] at zero masses. Checked numerically against the explicit sum over all sixteen spinor combinations (`qft-C/tools/l20/verify.py`).
>
> **What the derivation shows**
> - A second route to [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]] at high energy, through the helicities; the $\cos\theta$ terms cancel between the two final helicities, which is why the unpolarized distribution is forward–backward symmetric.

^der-c8b-7-7

*Uses:* [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]], [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-6|Theorem §C8a.7.6]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-6|P9, step 6]]

> [!theorem] Theorem §C8b.7.8: Angular Momentum along the Beam Fixes the Zeros
> ![[ph-qft-c8-13-2.svg]]
> *The user's figure "helJz" (Lecture 20 update, §20.4; slide 20) redrawn: spins (thick) and momenta (thin) along the beam axis, $\hat{\mathbf z}$ to the right. The initial pair has $J_z = +1$; exactly forward only $\mu^-_R\mu^+_L$ matches it.*
>
> For $e^-_Re^+_L$ (initial $J_z = +1$ along the beam, [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]]):
> 1. at $\theta = 0$ the $\mu^-$ continues along $+\hat{\mathbf z}$; $\mu^-_R\mu^+_L$ has $J_z = +1$ (allowed), $\mu^-_L\mu^+_R$ has $J_z = -1$ (forbidden): $\frac{d\sigma}{d\Omega}(\theta = 0) = 0$ for $e^-_Re^+_L \to \mu^-_L\mu^+_R$, and $(1 - \cos\theta)^2$ vanishes there;
> 2. at $\theta = \pi$ the roles are exchanged: $\mu^-_R\mu^+_L$ has $J_z = -1$, and $(1 + \cos\theta)^2$ vanishes.
>
> Spin flip along the beam is forbidden by conservation of angular momentum.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* $m_e = m_\mu = 0$, centre-of-mass frame, $\theta = 0$ or $\pi$ exactly; this process.
>
> *Source: PHY 513 Lecture 20, slide 20 ("Spin Flip is Forbidden. … $\frac{d\sigma}{d\Omega}(\theta = 0) = 0$, $(e^-_Re^+_L \to \mu^-_L\mu^+_R)$ … Spin flip forbidden due to angular momentum conservation"), slide 28 ("Dependence on angle from angular momentum conservation!"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.4, subsection "Angular momentum in the forward direction", Figure "helJz" · PS §5.2, p. 144, Figure 5.4 (the zero of (5.22) at $\theta = 180°$) · Yu §8.2.4, Figure 8.4 and the text after (8.142)*

^thm-c8b-7-8

> [!derivation]- Derivation
> **Step 1** (initial). $e^-_R$ along $+\hat{\mathbf z}$ and $e^+_L$ along $-\hat{\mathbf z}$ both have spin $+\frac12$ along $\hat{\mathbf z}$: $J_z = +1$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^der-c8b-6-5|Derivation §C8b.6.5]], Step 3).
>
> **Step 2** ($\theta = 0$). The $\mu^-$ moves along $+\hat{\mathbf z}$, the $\mu^+$ along $-\hat{\mathbf z}$. $\mu^-_R$: spin $+\frac12$; $\mu^+_L$: spin against $-\hat{\mathbf z}$, $+\frac12$; total $+1$. $\mu^-_L$: $-\frac12$; $\mu^+_R$: $-\frac12$; total $-1$.
>
> **Step 3** (no orbital help). All momenta lie on the $z$ axis, and orbital angular momentum $\mathbf L = \mathbf x\times\mathbf p$ of motion along the axis has no $z$ component. So $J_z$ is the sum of the spins, and conservation of $J_z$ forbids $+1 \to -1$: the amplitude vanishes.
>
> **Step 4** ($\theta = \pi$). The $\mu^-$ moves along $-\hat{\mathbf z}$; the spins of $\mu^-_R\mu^+_L$ point along $-\hat{\mathbf z}$: $J_z = -1$, forbidden.
>
> **Step 5** (agreement). $(1 - \cos\theta)^2 = 0$ at $\theta = 0$ and $(1 + \cos\theta)^2 = 0$ at $\theta = \pi$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]).

^der-c8b-7-8

*Uses:* [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]

> [!remark]- ★ Remark: In between, the amplitudes are spin-one rotation matrices
> The $\mu^+\mu^-$ pair has $J = 1$ with projection $\pm1$ along its own axis $\hat{\mathbf k}$, and the initial pair $J = 1$, $J_z = +1$. The overlap of $|1, +1\rangle_{\hat{\mathbf z}}$ with $|1, \pm1\rangle_{\hat{\mathbf k}}$ is the reduced rotation matrix element $d^1_{1,\pm1}(\theta) = \frac12(1 \pm \cos\theta)$ ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-3|QM Theorem §C5.3.3]]). Squared these are $\frac14(1 \pm \cos\theta)^2$, the two distributions of Theorem §C8b.7.6 up to normalization. The explicit spinors below see the same thing directly. Checked numerically (`qft-C/tools/l20/verify.py`).
>
> *Source: the user's PHY 513 notes, Lecture 20 update, §20.4.1 (paragraph "Filled in: in between, the amplitudes are the rotation matrices of spin one") · beyond the lecture*

^rem-c8b-7-3

## Explicit helicity spinors

Instead of projectors, $\gamma^5$'s and $\varepsilon$'s, one may insert the spinors of definite helicity and compute the amplitude itself, not $\frac14\sum|\mathcal M|^2$. The advantages: the dynamics and the spinors are seen explicitly. The disadvantages: a frame is chosen from the outset, so Lorentz invariance is broken, and except at very high energy (with finite masses) it is harder work than the traces (Lecture 20, slide 23).

> [!theorem] Theorem §C8b.7.9: Spinors in the Ultrarelativistic Limit
> For $|\mathbf p| = E$ ($m = 0$, or $E \to \infty$), with $\hat{\mathbf p}$ the unit vector along the motion,
>
> $$
> u(p) = \begin{pmatrix}\sqrt{p\cdot\sigma}\,\xi\\ \sqrt{p\cdot\bar\sigma}\,\xi\end{pmatrix} = \sqrt{2E}\begin{pmatrix}\frac12(1 - \hat{\mathbf p}\cdot\boldsymbol\sigma)\,\xi\\ \frac12(1 + \hat{\mathbf p}\cdot\boldsymbol\sigma)\,\xi\end{pmatrix}, \qquad v(p) = \sqrt{2E}\begin{pmatrix}\frac12(1 - \hat{\mathbf p}\cdot\boldsymbol\sigma)\,\eta\\ -\frac12(1 + \hat{\mathbf p}\cdot\boldsymbol\sigma)\,\eta\end{pmatrix} ,
> $$
>
> for any two-spinors $\xi$, $\eta$. With the helicity two-spinors $\hat{\mathbf p}\cdot\boldsymbol\sigma\,\xi_\pm = \pm\xi_\pm$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]): $u_R = \sqrt{2E}(0, \xi_+)^{\mathsf T}$, $u_L = \sqrt{2E}(\xi_-, 0)^{\mathsf T}$, and $v$ the same with a minus sign on the lower half. These spinors need a direction of motion: at rest there is none.
>
> *Model:* [[§C5a.7 The Dirac Equation and Its Lagrangian#^mod-c5a-7-3|Model §C5a.7.3]]; *applies:* exact at $m = 0$; leading order for $E \gg m$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-4|Theorem §C8b.5.4]], 2).
>
> *Source: PHY 513 Lecture 20, slide 25 ("In the limit where the fermion energy $E \to \infty$ … Used (for $|\vec p| = E$): $p\cdot\sigma = E - \vec p\cdot\vec\sigma = 2E\cdot\frac12(1 - \hat p\cdot\vec\sigma)$, 0 or 1. Can remove square root on 0 or 1"), slide 24 (helicity two-spinors $\xi_R$, $\xi_L$), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.5, paragraph "Ultrarelativistic spinors" · PS §5.2, p. 144, eq. (5.26)*

^thm-c8b-7-9

> [!derivation]- Derivation
> **Step 1** (projectors). At $|\mathbf p| = E$: $p\cdot\sigma = E - \mathbf p\cdot\boldsymbol\sigma = 2E\cdot\frac12(1 - \hat{\mathbf p}\cdot\boldsymbol\sigma)$ and $p\cdot\bar\sigma = 2E\cdot\frac12(1 + \hat{\mathbf p}\cdot\boldsymbol\sigma)$. Since $(\hat{\mathbf p}\cdot\boldsymbol\sigma)^2 = \mathbb 1$, $\Pi_\mp \equiv \frac12(1 \mp \hat{\mathbf p}\cdot\boldsymbol\sigma)$ satisfy $\Pi_\mp^2 = \frac14(1 \mp 2\hat{\mathbf p}\cdot\boldsymbol\sigma + 1) = \Pi_\mp$: projectors, eigenvalues $0$ and $1$.
>
> **Step 2** (the root). The square root is defined spectrally ([[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]]), and $\sqrt0 = 0$, $\sqrt1 = 1$: $\sqrt{2E\,\Pi} = \sqrt{2E}\,\Pi$. Insert into $u$ and $v$ ([[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]]).
>
> **Step 3** (helicity spinors). $\Pi_-\xi_+ = 0$, $\Pi_+\xi_+ = \xi_+$, and the reverse for $\xi_-$; this is [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]] again. Checked numerically for a general direction (`qft-C/tools/l20/verify.py`).

^der-c8b-7-9

*Uses:* [[§C5a.10 Plane-Wave Solutions꞉ the Eigenvalue Problem, the Rest Frame and the Boost#^def-c5a-10-5|Def. §C5a.10.5]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-1|Theorem §C5a.11.1]], [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates#^thm-c5a-11-3|Theorem §C5a.11.3]], [[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]

> [!theorem] Theorem §C8b.7.10: The Vertex Is a Circular Polarization Vector
> ![[ph-qft-c8-13-3.svg]]
> *ADDED figure: the spatial part of the currents in the $xz$ plane. The beam current has $\mathrm{Re}\,\boldsymbol\epsilon \propto \hat{\mathbf x}$; for the muon pair along $\hat{\mathbf k}$ it is turned by $\theta$ about $\hat{\mathbf y}$, which is unchanged.*
>
> With $e^-_R$ along $+\hat{\mathbf z}$ ($\xi = (1, 0)^{\mathsf T}$) and $e^+_L$ along $-\hat{\mathbf z}$ ($\eta = (0, 1)^{\mathsf T}$, physical spin along $+\hat{\mathbf z}$, [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]):
> 1. $u_R(p) = \sqrt{2E}\,(0, 0, 1, 0)^{\mathsf T}$, $v(p') = \sqrt{2E}\,(0, 0, 0, -1)^{\mathsf T} = P_Rv(p')$, and
>
> $$
> \bar v(p')\gamma^\mu u(p) = -2E\,(0, 1, i, 0) ,
> $$
>
> the circular polarization vector with $J_z = +1$, $\boldsymbol\epsilon_+ \propto \hat{\mathbf x} + i\hat{\mathbf y}$: two spin-½ particles combine into a photon of polarization $+1$;
> 2. the muon currents are the same object rotated by $\theta$ in the $xz$ plane and complex conjugated (an outgoing pair): up to a phase fixed by the conventions for $\xi$ and $\eta$,
>
> $$
> \bar u(k)\gamma^\mu v(k') = -2E\,(0, \cos\theta, -i, -\sin\theta) \quad (\mu^-_R\mu^+_L), \qquad -2E\,(0, \cos\theta, i, -\sin\theta) \quad (\mu^-_L\mu^+_R) ;
> $$
>
> 3. with $q^2 = 4E^2$ and the Minkowski product, $\mathcal M = \frac{e^2}{q^2}J_e\cdot J_\mu$:
>
> $$
> \mathcal M(e^-_Re^+_L \to \mu^-_R\mu^+_L) = -e^2(1 + \cos\theta) , \qquad \mathcal M(e^-_Re^+_L \to \mu^-_L\mu^+_R) = e^2(1 - \cos\theta) ,
> $$
>
> whose squares are Theorem §C8b.7.6. The signs are the slide's and Yu's phase conventions; only $|\mathcal M| = e^2(1 \pm \cos\theta)$ is convention free.
>
> *Model:* [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^mod-c8a-6-1|Model §C8a.6.1]]; *applies:* $m_e = m_\mu = 0$, centre-of-mass frame, $\mathbf k$ in the $xz$ plane ($\varphi = 0$).
>
> *Source: PHY 513 Lecture 20, slides 26–28 ("$\bar v(p')\gamma^\mu u(p) = 2E(0\ {-1})\sigma^\mu\binom10 = -2E(0\ 1\ i\ 0)^\mu$"; "Physics interpretation: $e^-$ and $e^+$ with physical spins in $+\hat z$ direction combine to photon with '+' polarization"; "Outgoing $\mu^-_R\mu^+_L$ vertex: complex conjugated relative to 'in' amplitude and rotated in $x - z$ plane by $\theta$: … $= -2E(0\ \cos\theta\ i\ {-\sin\theta})^\ast$"; "$\mathcal M(e^-_Re^+_L \to \mu^-_R\mu^+_L) = -(2E)^2(1 + \cos\theta)\cdot\frac{e^2}{4E^2} = -e^2(1 + \cos\theta)$"), and transcript · the user's PHY 513 notes, Lecture 20 update, §20.5, Derivation "The vertex as a polarization vector" (its amplitudes $e^2(1 \mp \cos\theta)$ with its own phases) · PS §5.2, pp. 145–146, eqs. (5.28)–(5.32) · Yu §8.2.4, eqs. (8.118) ($E_{\rm cm}(0, -1, -i, 0)$, the same current), (8.132)–(8.133), (8.136)–(8.139)*

^thm-c8b-7-10

> [!derivation]- Derivation
> **Step 1** (spinors). [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-9|Theorem §C8b.7.9]] with $\hat{\mathbf p} = \hat{\mathbf z}$, $\xi = (1, 0)^{\mathsf T} = \xi_+$: $u = \sqrt{2E}(0, 0, 1, 0)^{\mathsf T}$. For the positron $\hat{\mathbf p}' = -\hat{\mathbf z}$ and $\hat{\mathbf p}'\cdot\boldsymbol\sigma\,\eta = -\sigma^3(0, 1)^{\mathsf T} = +\eta$, so the upper half $\frac12(1 - \hat{\mathbf p}'\cdot\boldsymbol\sigma)\eta = 0$ and the lower half is $-\eta$: $v = \sqrt{2E}(0, 0, 0, -1)^{\mathsf T}$, only lower components, as $P_Rv$ must be ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]]).
>
> **Step 2** (the current). $\bar v\gamma^\mu u = v^\dagger\gamma^0\gamma^\mu u$ with $\gamma^0\gamma^\mu = \operatorname{diag}(\bar\sigma^\mu, \sigma^\mu)$ ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]]) uses the lower halves only: $2E\,(0, -1)\sigma^\mu(1, 0)^{\mathsf T}$. Component by component: $\sigma^0(1, 0)^{\mathsf T} = (1, 0)^{\mathsf T}$, so $0$; $\sigma^1(1, 0)^{\mathsf T} = (0, 1)^{\mathsf T}$, so $-1$; $\sigma^2(1, 0)^{\mathsf T} = (0, i)^{\mathsf T}$, so $-i$; $\sigma^3(1, 0)^{\mathsf T} = (1, 0)^{\mathsf T}$, so $0$. Hence $2E(0, -1, -i, 0) = -2E(0, 1, i, 0)$.
>
> **Step 3** (muon currents by rotation). A vector bilinear transforms as a four-vector ([[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]]), so for a pair along $\hat{\mathbf k}$ with the same helicities the incoming-type current $\bar v(k')\gamma^\mu u(k)$ is the beam current rotated by $\theta$ about $\hat{\mathbf y}$: $\hat{\mathbf x} \to (\cos\theta, 0, -\sin\theta)$, $\hat{\mathbf y} \to \hat{\mathbf y}$, giving $-2E(0, \cos\theta, i, -\sin\theta)$, up to the phase that the rotation gives the spinors. The outgoing current is its conjugate, $\bar u(k)\gamma^\mu v(k') = (\bar v(k')\gamma^\mu u(k))^\ast$ ([[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-1|Theorem §C8a.7.1]]): $-2E(0, \cos\theta, -i, -\sin\theta)$ for $\mu^-_R\mu^+_L$. For $\mu^-_L\mu^+_R$ start from the $e^-_Le^+_R$ current $-2E(0, 1, -i, 0)$ (Steps 1–2 with $\xi = (0, 1)^{\mathsf T}$, $\eta = (1, 0)^{\mathsf T}$; PS p. 146), rotate and conjugate: $-2E(0, \cos\theta, i, -\sin\theta)$.
>
> **Step 4** (the amplitudes). $\mathcal M = \frac{e^2}{q^2}J_e^\mu J_{\mu\mu}$ ([[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]], the $i$ removed). The time components vanish, so the Minkowski product is minus the spatial dot product. $\mu^-_R\mu^+_L$: $(-2E)^2\cdot[-(1\cdot\cos\theta + i\cdot(-i) + 0)] = -4E^2(1 + \cos\theta)$, and with $\frac{e^2}{4E^2}$: $-e^2(1 + \cos\theta)$. $\mu^-_L\mu^+_R$: $4E^2\cdot[-(\cos\theta + i\cdot i)] = 4E^2(1 - \cos\theta)$, so $e^2(1 - \cos\theta)$.
>
> **What the derivation shows**
> - The amplitude is an overlap of two polarization vectors: $1 \pm \cos\theta$ is what a unit vector along $\hat{\mathbf x}$, turned about $\hat{\mathbf y}$ like an ordinary three-vector, gives → next remark.
> - Phases: the update's direct computation with θ-dependent spinors gives $2E(0, \cos\theta, -i, -\sin\theta)$ and $\mathcal M = e^2(1 + \cos\theta)$ for $\mu^-_R\mu^+_L$, PS (5.32) has $-e^2(1 - \cos\theta)$ for $\mu^-_L\mu^+_R$, Yu (8.136), (8.138) agree with the signs above. All currents and amplitudes checked numerically up to these phases (`qft-C/tools/l20/verify.py`).

^der-c8b-7-10

*Uses:* [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-9|Theorem §C8b.7.9]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[§C5a.6 The Dirac Conjugate and the Bilinears#^thm-c5a-6-2|Theorem §C5a.6.2]], [[§C8a.7 The Spin-Averaged Squared Amplitude#^thm-c8a-7-1|Theorem §C8a.7.1]], [[§C8a.6 Electron–Positron Annihilation꞉ the Amplitude and the Virtual Photon#^thm-c8a-6-2|Theorem §C8a.6.2]]

*Procedure:* [[P9 Helicity Amplitudes#^p9-7|P9, step 7]]

> [!remark] Remark: The spin-one part is rotated, the spin-zero part does nothing
> $1 \pm \cos\theta$ is what one expects for a unit vector in the $x$ direction rotated about $y$ like an ordinary three-vector ([[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^ex-c5-3-2|QM Example §C5.3.2]]: spherical components rotate with the $j = 1$ matrix). The two initial spins, a half plus a half, contain a spin-zero part, to which nothing happens, and a spin-one part, which the photon picks up and which is rotated as a spin one ([[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]]). This is why it matters that the photon has spin one. The angular dependence that the traces produce by hard work is the rotation of a vector.
>
> *Source: PHY 513 Lecture 20, slide 28, and transcript · the user's PHY 513 notes, Lecture 20 update, §20.5 (the paragraph after Derivation "The vertex as a polarization vector")*

^rem-c8b-7-4

> [!remark] Remark: θ-dependent spinors and the half angle
> Asked in the lecture whether the muon vertex could be computed directly with $\theta$-dependent spinors: yes. The helicity two-spinors along $\hat{\mathbf k}$ are those along $\hat{\mathbf z}$ rotated by $\theta/2$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]: $\cos\frac\theta2$, $\sin\frac\theta2$). Two of them multiply in a bilinear, and $\cos^2\frac\theta2 - \sin^2\frac\theta2 = \cos\theta$, $2\sin\frac\theta2\cos\frac\theta2 = \sin\theta$ turn the half angle into the full rotation by $\theta$ (Yu (8.101)–(8.105), (8.125)–(8.133)). What matters is the direction of motion: helicity is spin projected along the motion, not along the axis one happened to call $z$.
>
> *Source: PHY 513 Lecture 20, transcript · the user's PHY 513 notes, Lecture 20 update, §20.5, paragraph "Asked in the lecture: could the muon vertex be computed directly …" · Yu §8.2.4 (the remark after (8.105): spinors turn by $\theta/2$ when momenta turn by $\theta$)*

^rem-c8b-7-5

> [!remark] Remark: The azimuthal phase cancels
> Asked in the lecture whether the azimuth matters: with $\mathbf k$ in the $xz$ plane, $\varphi = 0$. For general $\varphi$ the helicity spinors carry $e^{\pm i\varphi}$ ([[§C8b.5 Helicity Spinors and the Massless Limit#^thm-c8b-5-1|Theorem §C8b.5.1]]); the process is symmetric under rotations about the beam, so the phases cancel in $|\mathcal M|^2$. An external magnetic field could single out a sense of rotation, but that is the physics of the detector, not of the collision.
>
> *Source: PHY 513 Lecture 20, transcript · the user's PHY 513 notes, Lecture 20 update, §20.5, paragraph "Asked in the lecture: is the azimuthal phase important?"*

^rem-c8b-7-6

> [!remark] Remark: Spin is what makes QED amplitudes angular
> In $\phi^4$ theory the $2 \to 2$ amplitude has no angular dependence at all, $i\mathcal M = -i\lambda$ ([[§C6c.1 Amplitudes from Correlation Functions#^ex-c6c-1-2|Example §C6c.1.2]]): there is no spin. In QED the amplitude is essentially the inner product of an initial and a final four-vector, and its angular dependence is the spin. Processes with external photons add more of the same.
>
> *Source: PHY 513 Lecture 20, transcript · the user's PHY 513 notes, Lecture 20 update, §20.5, paragraph "Spin is what makes QED angular"*

^rem-c8b-7-7

> [!remark] Remark: Lecture 20 at a glance
> - Helicity is spin along the motion; for massless fermions $P_{R,L} = \frac12(1 \pm \gamma^5)$ project onto it, with the physical helicity reversed for antiparticles ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-1|Theorem §C8b.6.1]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-2|Theorem §C8b.6.2]]).
> - The QED vertex conserves chirality, $\bar\psi\gamma^\mu\psi = \bar\psi_L\gamma^\mu\psi_L + \bar\psi_R\gamma^\mu\psi_R$, so $e^-_R$ annihilates only with $e^+_L$, into $J_z = \pm1$: the photon's spin one ([[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-4|Theorem §C8b.6.4]], [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-5|Theorem §C8b.6.5]]).
> - With projectors the squared amplitude still reduces to traces, now with $\gamma^5$ and $\varepsilon$ symbols, and the result is simpler: $\frac{16e^4}{q^4}(p\cdot k')(p'\cdot k) = e^4(1 + \cos\theta)^2$ for $e^-_Re^+_L \to \mu^-_R\mu^+_L$, $e^4(1 - \cos\theta)^2$ for $\mu^-_L\mu^+_R$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-5|Theorem §C8b.7.5]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-6|Theorem §C8b.7.6]]).
> - Each vanishes where angular momentum along the beam would flip; their average is the unpolarized $1 + \cos^2\theta$ ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-7|Theorem §C8b.7.7]], [[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-8|Theorem §C8b.7.8]]).
> - Explicit helicity spinors turn each vertex into a spin-one polarization vector and the amplitude into the overlap of a vector with its rotated image ([[§C8b.7 Polarized Cross Sections for Muon Pair Production#^thm-c8b-7-10|Theorem §C8b.7.10]]). The steps: [[P9 Helicity Amplitudes|P9]].
>
> *Source: the user's PHY 513 notes, Lecture 20 update, §20.6, Principle "Helicity structure" · PHY 513 Lecture 20, slide 3*

^rem-c8b-7-8

> [!remark] Remark: Correspondence with Yu and Peskin–Schroeder
> PS §5.2 does both methods for massless fermions: projectors and traces, (5.17)–(5.24), then explicit spinors, (5.25)–(5.32). Yu §8.2.4 uses explicit helicity spinors throughout and keeps both masses: the amplitude (8.99); helicity two-spinors along $\hat{\mathbf z}$ and turned by $\theta$, (8.100)–(8.107); $\gamma^0\gamma^\mu$ block diagonal (8.108); the $e^+e^-$ currents (8.114)–(8.121), with (8.118) $= E_{\rm cm}(0, -1, -i, 0)$ the current of Theorem §C8b.7.10; the muon currents (8.122)–(8.135); the four unsuppressed amplitudes $\mp e^2(1 \pm \cos\theta)$, (8.136)–(8.139), exact with masses, parity (8.140) and the cross sections (8.141)–(8.142) with $\beta$ factors; the mass-suppressed amplitudes (8.143)–(8.157) ([[§C8b.6 Helicity Conservation at the QED Vertex#^rem-c8b-6-3|§C8b.6, Remark: Frame and mass]]); and the sum of all sixteen, (8.158); with masses these are written out in ★ [[§C8b.8★ Polarized Amplitudes with Masses|§C8b.8★]]. Yu §8.3 treats chirality and helicity separately ([[§C8b.6 Helicity Conservation at the QED Vertex|§C8b.6]]). The $\gamma^5$-trace method is PS's. Yu labels the incoming momenta $k_1, k_2$ and the outgoing $p_1, p_2$ (reversed against the course; [[Larsen PHY 513]]).
>
> *Source: Yu §8.2.4, eqs. (8.99)–(8.158) (pages checked; the update's range for the suppressed amplitudes is corrected in `qft-C/ERRATA.md`) · PS §5.2, pp. 141–146 · the user's PHY 513 notes, Lecture 20 update, paragraph "Correspondence with Yu"*

^rem-c8b-7-9

> [!abstract]- Mathematical background
> Proved in CB, in C1a and in Quantum Mechanics; each line says what the physics above relies on.
>
> - [[§CB.13 Clifford Algebras꞉ Grading, Basis and the Volume Element#^thm-cb-13-15|Theorem §CB.13.15]] — $\gamma^5$ squares to $\mathbb 1$ and anticommutes with each $\gamma^\mu$: the projectors and the $\gamma^5$ traces (physics form: [[§C5a.5 Chirality and Weyl Spinors#^thm-c5a-5-1|Theorem §C5a.5.1]], [[§C5a.13 Gamma-Matrix Technology#^thm-c5a-13-4|Theorem §C5a.13.4]]).
> - [[§C1a.5 Vectors, Tensors and Index Notation#^thm-c1a-5-4|Theorem §C1a.5.4]] — the contraction of two Levi-Civita symbols, with the factor $\det g = -1$ of Minkowski space.
> - [[§C5.3 The Angular-Momentum Spectrum and Rotation Matrices#^thm-c5-3-3|QM Theorem §C5.3.3]] — the spin-one rotation matrix $d^{(1)}(\theta)$, whose entries $\frac12(1 \pm \cos\theta)$ are the amplitudes up to normalization.

> [!remark]- Connections
> - The unpolarized computation is the sum over these helicity configurations; its $1 + \cos^2\theta$ is the average of $(1 + \cos\theta)^2$ and $(1 - \cos\theta)^2$ — [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-3|Theorem §C8a.8.3]], [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^rem-c8a-8-2|§C8a.8, Remark: Kinematics and dynamics]]; the procedure — [[P8 Unpolarized Cross Section from Diagrams]] against [[P9 Helicity Amplitudes]].
> - The circular polarization vector of the virtual photon is the spherical basis vector of spin one, the same vectors that describe real photons of helicity $\pm1$ — [[§C8b.3 Massless Particles and Helicity|§C8b.3]], [[§C4.10 The Gupta–Bleuler Condition and Physical Photons|§C4.10]].
> - Near threshold the opposite limit holds: the muons come out in an s-wave with total spin one (PS §5.3), and the distribution becomes isotropic — [[§C8a.8 The Unpolarized Cross Section for Muon Pair Production#^thm-c8a-8-4|Theorem §C8a.8.4]].
> - The vertex as a spin-one object is the Clebsch–Gordan statement of PS p. 145 — [[§C8b.6 Helicity Conservation at the QED Vertex#^thm-c8b-6-3|Theorem §C8b.6.3]], [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]].
