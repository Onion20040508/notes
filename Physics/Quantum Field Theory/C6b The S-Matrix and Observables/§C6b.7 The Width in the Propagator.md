---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6b
section: C6b.7
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6b.6 Decay Kinematics]] · ↑ [[· C6b The S-Matrix and Observables]] · [[§C6b.8 Wave Packets and the Cross Section]] →

<!-- HEADER-7 -->

## The width in the propagator

> [!model] Model §C6b.7.1: The Propagator of an Unstable Particle
> Near its mass shell, the propagator of an unstable scalar particle of mass $m$ and width $\Gamma$ is
>
> $$
> \frac{i}{p^2 - m^2 + im\Gamma} ,
> $$
>
> the Feynman propagator $\frac{i}{p^2 - m^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]) with the infinitesimal $\varepsilon$ replaced by the finite $m\Gamma$, which radiative corrections produce: the self-energy of an unstable particle has an imaginary part on its mass shell, $Z\operatorname{Im}\Pi(m^2) = -m\Gamma$ (Yu (10.265)), and near the pole the full propagator is $\frac{iZ}{p^2 - m^2 - iZ\operatorname{Im}\Pi(m^2)} = \frac{iZ}{p^2 - m^2 + im\Gamma}$ (Yu (10.270), here with $Z \simeq 1$; beyond the course so far: [[§C6b.7 The Width in the Propagator#^rem-c6b-7-2|★ Remark: Yu's route to the width]]).
> - *Assumptions:* a narrow width, $\Gamma \ll m$; $p^2$ near $m^2$; the field normalization of the full propagator set to 1.
> - *Applies:* resonances, "I hit something and [make] some resonance"; a stable particle is the limit $\Gamma \to 0$.
>
> *Source: PHY 513 Lecture 15, slide 23 ("Propagator in QFT with radiative corrections: $\frac{1}{p^2 - m^2 + im\Gamma}$"), and transcript ("you might be more happy if I actually give it dimensions … It's an $i m\Gamma$, where $\Gamma$ is a width") · the user's PHY 513 notes, Ch. 15 §15.8, eq. (BWprop) · PS §4.5, eq. (4.64) · Yu §10.6, eq. (10.270) (derived there from the self-energy, with $Z \simeq 1$)*

^mod-c6b-7-1

> [!theorem] Theorem §C6b.7.2: The Propagator Near Its Pole
> For $p^0$ near $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$,
>
> $$
> \frac{1}{p^2 - m^2 + im\Gamma} = \frac{1}{(p^0)^2 - E_{\mathbf p}^2 + im\Gamma} \simeq \frac{1}{2E_{\mathbf p}\bigl(p^0 - E_{\mathbf p} + i\frac{m}{E_{\mathbf p}}\frac\Gamma2\bigr)} ,
> $$
>
> a simple pole at $p^0 = E_{\mathbf p} - i\frac{m}{E_{\mathbf p}}\frac\Gamma2$, below the real axis; the exact pole $p^0 = \sqrt{E_{\mathbf p}^2 - im\Gamma}$ differs from it at order $\Gamma^2$.
>
> *Model:* [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]]; *applies:* narrow width, $p^0$ near $E_{\mathbf p}$; first order in $\Gamma$.
>
> *Source: PHY 513 Lecture 15, slide 23 ("$\frac{1}{p^2 - m^2 + im\Gamma} = \frac{1}{(p^0)^2 - E_{\vec p}^2 + im\Gamma} \simeq \frac{1}{2E_{\vec p}(p^0 - E_{\vec p} + i\frac{m}{E_{\vec p}}\frac{\Gamma}{2})}$. Approximation: $p^0 \sim E_{\vec p} = \sqrt{\vec p^2 + m^2}$."), and transcript · the user's PHY 513 notes, Ch. 15 §15.8, eq. (BWprop), paragraph "Checks (filled in)" · PS §4.5, eq. (4.64)*

^thm-c6b-7-2

> [!derivation]- Derivation
> **Step 1** (the first equality). With $E_{\mathbf p}^2 = \mathbf p^2 + m^2$,
>
> $$
> p^2 - m^2 = (p^0)^2 - \mathbf p^2 - m^2 = (p^0)^2 - E_{\mathbf p}^2 .
> $$
>
> **Step 2** (sum and difference). "Turn this into a sum and difference", and write the sum as $2E_{\mathbf p} + (p^0 - E_{\mathbf p})$:
>
> $$
> (p^0)^2 - E_{\mathbf p}^2 = (p^0 + E_{\mathbf p})(p^0 - E_{\mathbf p}) = 2E_{\mathbf p}(p^0 - E_{\mathbf p}) + (p^0 - E_{\mathbf p})^2 \simeq 2E_{\mathbf p}(p^0 - E_{\mathbf p}) ,
> $$
>
> the last term dropped near $p^0 = E_{\mathbf p}$, a relative error $O\bigl((p^0 - E_{\mathbf p})/E_{\mathbf p}\bigr)$.
>
> **Step 3** (factor out $2E_{\mathbf p}$).
>
> $$
> (p^0)^2 - E_{\mathbf p}^2 + im\Gamma \simeq 2E_{\mathbf p}(p^0 - E_{\mathbf p}) + im\Gamma = 2E_{\mathbf p}\Bigl(p^0 - E_{\mathbf p} + \frac{im\Gamma}{2E_{\mathbf p}}\Bigr) = 2E_{\mathbf p}\Bigl(p^0 - E_{\mathbf p} + i\frac{m}{E_{\mathbf p}}\frac\Gamma2\Bigr) ,
> $$
>
> whose zero is $p^0 = E_{\mathbf p} - i\frac{m}{E_{\mathbf p}}\frac\Gamma2$, with $\operatorname{Im}p^0 < 0$.
>
> **Step 4** (the exact pole). $(p^0)^2 = E_{\mathbf p}^2 - im\Gamma$; the root with positive real part, by the binomial series $\sqrt{1 - u} = 1 - \frac u2 - \frac{u^2}{8} + O(u^3)$ with $u = im\Gamma/E_{\mathbf p}^2$, $u^2 = -m^2\Gamma^2/E_{\mathbf p}^4$:
>
> $$
> p^0 = E_{\mathbf p}\sqrt{1 - \frac{im\Gamma}{E_{\mathbf p}^2}} = E_{\mathbf p}\Bigl(1 - \frac{im\Gamma}{2E_{\mathbf p}^2} + \frac{m^2\Gamma^2}{8E_{\mathbf p}^4} + O(\Gamma^3)\Bigr) = E_{\mathbf p} - \frac{im\Gamma}{2E_{\mathbf p}} + \frac{m^2\Gamma^2}{8E_{\mathbf p}^3} + O(\Gamma^3) ,
> $$
>
> which agrees with Step 3 to first order in $\Gamma$. ("At least I don't divide by zero anymore.") Numerically, $m = 2$, $\Gamma = 0.05$, $|\mathbf p| = 1.3$: $-2\operatorname{Im}p^0 = 0.041921$ against $\frac{m}{E_{\mathbf p}}\Gamma = 0.041922$ (`qft-C/tools/l15/checks.py`).
>
> **What the derivation shows.**
> - With $\varepsilon \to m\Gamma$ the pole at $+E_{\mathbf p}$ moves a finite distance below the real axis, where the Feynman prescription had put it infinitesimally ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]).

^der-c6b-7-2

*Uses:* [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]]

> [!definition] Definition §C6b.7.1: The Non-Relativistic Decay Constant
> In non-relativistic quantum theory a decaying state has an energy with a negative imaginary part; its **decay constant** $\Gamma_{\rm NR}$ is defined by
>
> $$
> \psi \sim e^{-iEt} = e^{-iE^0t - \frac{\Gamma_{\rm NR}}{2}t} \quad\Rightarrow\quad |\psi|^2 = e^{-\Gamma_{\rm NR}t} :
> $$
>
> the probability that the particle is still there decreases at the rate $\Gamma_{\rm NR}$.
>
> *Model:* none (non-relativistic quantum mechanics); *applies:* one decaying state, $t > 0$.
>
> *Source: PHY 513 Lecture 15, slide 23 ("In non-relativistic quantum theory: $\Gamma_{\rm NR}$ is decay constant. Wave function $\psi \sim e^{-iEt} = e^{-iE^0t - \frac{\Gamma_{\rm NR}}{2}t}$ ⇒ $|\psi|^2 = e^{-\Gamma_{\rm NR}t}$"), and transcript ("this wave function … gives me the $e^{-\Gamma t}$ decay instead of the wave function having norm one") · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Relation to non-relativistic decay")*

^def-c6b-7-1

Quantum mechanics derives this behaviour, with the complex energy shift $\Delta_i$ of a level coupled to a continuum and $\Gamma = -2\operatorname{Im}\Delta_i$ the golden-rule rate ([[§C9.6 The Interaction Picture and the Atom–Field Interaction#^thm-c9-6-11|QM Theorem §C9.6.11]]); there the energy distribution of the decaying state is a Lorentzian of full width $\Gamma$, the non-relativistic form of [[§C6b.7 The Width in the Propagator#^thm-c6b-7-4|Theorem §C6b.7.4]].

> [!theorem] Theorem §C6b.7.3: The Width Is Invariant; the Decay Rate Is Time-Dilated
> The propagator of [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]], at fixed $\mathbf p$ and for $t > 0$, describes an amplitude $\propto e^{-iE_{\mathbf p}t - \frac{\Gamma_{\rm NR}}{2}t}$ with
>
> $$
> \Gamma_{\rm NR} = \frac{m}{E_{\mathbf p}}\,\Gamma = \frac{\Gamma}{\gamma} .
> $$
>
> $\Gamma$ in $p^2 - m^2 + im\Gamma$ is a Lorentz-invariant notion, the decay rate in the rest frame; a particle moving with energy $E_{\mathbf p}$ decays at the slower rate $\Gamma_{\rm NR}$ and lives $\gamma$ times longer.
>
> *Model:* [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]]; *applies:* as there; first order in $\Gamma$, $t > 0$.
>
> *Source: PHY 513 Lecture 15, slide 23 ("Relativistic decay rate has additional time dilatation: $\frac{m}{E_{\vec p}}\Gamma = \Gamma_{\rm NR}$"), and transcript ("our $\Gamma$ here really is a relativistically invariant notion … there's an additional time dilation, non-relativistic quantum mechanics would never take [into account]") · the user's PHY 513 notes, Ch. 15 §15.8, Principle "The width is invariant; the decay rate is time-dilated", eq. (GammaNR) (a derived result: a theorem here) · PS §4.5, p. 101 (after eq. (4.64))*

^thm-c6b-7-3

> [!derivation]- Derivation
> **Step 1** (back to time). At fixed $\mathbf p$, the time dependence of the propagator is its Fourier transform in $p^0$ (the convention $f(t) = \int\frac{dp^0}{2\pi}\tilde f(p^0)e^{-ip^0t}$ of [[Larsen PHY 513]]). Near the pole, by [[§C6b.7 The Width in the Propagator#^thm-c6b-7-2|Theorem §C6b.7.2]], with $a = E_{\mathbf p} - i\frac{\Gamma'}{2}$, $\Gamma' = \frac{m}{E_{\mathbf p}}\Gamma$:
>
> $$
> \int\frac{dp^0}{2\pi}\,e^{-ip^0t}\,\frac{i}{2E_{\mathbf p}(p^0 - a)} .
> $$
>
> **Step 2** (close the contour). For $t > 0$, $|e^{-ip^0t}| = e^{t\operatorname{Im}p^0}$ decays for $\operatorname{Im}p^0 < 0$, so the contour is closed in the lower half plane, clockwise, by Jordan's lemma ([[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]); it encloses the pole at $a$ ($\operatorname{Im}a = -\Gamma'/2 < 0$). The residue theorem ([[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]]) with the clockwise sign $-2\pi i$:
>
> $$
> \operatorname*{Res}_{p^0 = a}\frac{i\,e^{-ip^0t}}{2E_{\mathbf p}(p^0 - a)} = \frac{i\,e^{-iat}}{2E_{\mathbf p}} , \qquad \frac{1}{2\pi}(-2\pi i)\frac{i\,e^{-iat}}{2E_{\mathbf p}} = \frac{e^{-iat}}{2E_{\mathbf p}} = \frac{1}{2E_{\mathbf p}}\,e^{-iE_{\mathbf p}t}\,e^{i\cdot i\frac{\Gamma'}{2}t} = \frac{1}{2E_{\mathbf p}}\,e^{-iE_{\mathbf p}t}\,e^{-\frac{\Gamma'}{2}t} .
> $$
>
> (The far pole near $p^0 = -E_{\mathbf p}$, dropped in the approximation, lies above the axis and contributes for $t < 0$, as for $D_F$, [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]].)
>
> **Step 3** (compare). Match with $\psi$ of [[§C6b.7 The Width in the Propagator#^def-c6b-7-1|Def. §C6b.7.1]] term by term:
>
> $$
> e^{-iE_{\mathbf p}t}\,e^{-\frac{\Gamma'}{2}t} = e^{-iE^0t - \frac{\Gamma_{\rm NR}}{2}t} \quad\Rightarrow\quad E^0 = E_{\mathbf p} , \qquad \Gamma_{\rm NR} = \Gamma' = \frac{m}{E_{\mathbf p}}\Gamma = \frac{m}{\gamma m}\Gamma = \frac\Gamma\gamma ,
> $$
>
> using $E_{\mathbf p} = \gamma m$.
>
> **Step 4** (invariance). $m\Gamma$ in $p^2 - m^2 + im\Gamma$ is a Lorentz scalar, so $\Gamma$ is the same in every frame. In the rest frame $\mathbf p = 0$:
>
> $$
> E_{\mathbf 0} = m \quad\Rightarrow\quad \Gamma_{\rm NR} = \frac{m}{m}\Gamma = \Gamma ,
> $$
>
> so $\Gamma$ is the rest-frame decay rate of [[§C6b.5 Decay Widths#^def-c6b-5-1|Def. §C6b.5.1]]. In another frame the lifetime $1/\Gamma_{\rm NR} = \gamma/\Gamma = \gamma\tau$ is the dilated proper lifetime ([[§A2.1 Time Dilation#^thm-a2-1-2|REL Theorem §A2.1.2]]).
>
> **What the derivation shows.**
> - Non-relativistic quantum mechanics cannot see the factor $m/E$: there $E \approx m$; "so there's some translation there that occasionally people … can get wrong".
> - The decay formula of [[§C6b.5 Decay Widths#^thm-c6b-5-6|Theorem §C6b.5.6]] gives the same factor in a moving frame, $\frac{1}{2E_A}$ instead of $\frac{1}{2m_A}$ (its second ⚑).

^der-c6b-7-3

*Uses:* [[§C6b.7 The Width in the Propagator#^thm-c6b-7-2|Theorem §C6b.7.2]], [[§C6b.7 The Width in the Propagator#^def-c6b-7-1|Def. §C6b.7.1]], [[§CA.4 Contour Integration#^thm-ca-4-5|Theorem §CA.4.5]], [[§CA.4 Contour Integration#^thm-ca-4-6|Theorem §CA.4.6]]

*Procedure:* [[P2 Green's Functions by Contour Integration|P2]]

<!-- NEW cau-c6b-7-1 -->

> [!theorem] Theorem §C6b.7.4: The Breit–Wigner Shape and Its Width
> If the propagator of [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]] carries the total momentum of a process, $p^2 = s$ (e.g. $s = E_{\rm cm}^2$), the cross section near $\sqrt s = m$ has the factor
>
> $$
> \Bigl|\frac{1}{s - m^2 + im\Gamma}\Bigr|^2 = \frac{1}{(s - m^2)^2 + m^2\Gamma^2} \simeq \frac{1}{4m^2}\,\frac{1}{(\sqrt s - m)^2 + \Gamma^2/4} ,
> $$
>
> a bell shape in $\sqrt s$ peaked at $m$ with full width at half maximum $\Gamma$ (narrow width). The normalized shape $f_{\rm BW}(\sqrt s) = \frac{\Gamma}{2\pi}\frac{1}{(\sqrt s - m)^2 + \Gamma^2/4}$ tends to $\delta(\sqrt s - m)$ as $\Gamma \to 0$: a stable particle.
>
> *Model:* [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]]; *applies:* as there; $\sqrt s$ near $m$, narrow width.
>
> *Source: PHY 513 Lecture 15, transcript ("if you were to take the norm squared of this, you will see that this is a perfectly good … bell shape … the limit where the width goes to zero") · the user's PHY 513 notes, Ch. 15 §15.8, Figure "breitwigner", paragraph "Checks (filled in)" · Yu §10.6, eqs. (10.271)–(10.275) · PS §4.5, eq. (4.63) (the non-relativistic form)*

^thm-c6b-7-4

> [!derivation]- Derivation
> **Step 1** (modulus). With $x = s - m^2$, $y = m\Gamma$ real,
>
> $$
> \Bigl|\frac{1}{x + iy}\Bigr|^2 = \frac{1}{(x + iy)(x - iy)} = \frac{1}{x^2 + y^2} = \frac{1}{(s - m^2)^2 + m^2\Gamma^2} .
> $$
>
> **Step 2** (near the peak). $s - m^2 = (\sqrt s - m)(\sqrt s + m)$ and $\sqrt s + m \simeq 2m$ for $\sqrt s$ near $m$ (Yu eq. (10.273)):
>
> $$
> (s - m^2)^2 + m^2\Gamma^2 \simeq 4m^2(\sqrt s - m)^2 + m^2\Gamma^2 = 4m^2\Bigl[(\sqrt s - m)^2 + \frac{\Gamma^2}{4}\Bigr] .
> $$
>
> **Step 3** (half maximum). The maximum is at $\sqrt s = m$; half of it is reached where
>
> $$
> \frac{1}{4m^2}\,\frac{1}{(\sqrt s - m)^2 + \Gamma^2/4} = \frac12\cdot\frac{1}{4m^2}\,\frac{4}{\Gamma^2} \;\Leftrightarrow\; (\sqrt s - m)^2 + \frac{\Gamma^2}{4} = \frac{\Gamma^2}{2} \;\Leftrightarrow\; \sqrt s = m \pm \frac\Gamma2 ,
> $$
>
> a full width $(m + \frac\Gamma2) - (m - \frac\Gamma2) = \Gamma$. "That's why it's called the width" (Yu after eq. (10.274)). For the exact form the full width is $\Gamma$ only to leading order: $1.00008\,\Gamma$ at $\Gamma/m = 1/40$, $1.0013\,\Gamma$ at $\Gamma/m = 1/10$ (`qft-C/tools/l15/checks.py`).
>
> **Step 4** (normalization and limit). With $x = \sqrt s - m$, $c = \Gamma/2$ and the range of $\sqrt s$ extended to $\pm\infty$ (harmless for $\Gamma \ll m$),
>
> $$
> \int_{-\infty}^\infty\frac{dx}{x^2 + c^2} = \frac1c\Bigl[\arctan\frac xc\Bigr]_{-\infty}^{\infty} = \frac1c\Bigl(\frac\pi2 + \frac\pi2\Bigr) = \frac\pi c = \frac{2\pi}{\Gamma} \quad\Rightarrow\quad \int_{-\infty}^\infty f_{\rm BW}\,dx = \frac{\Gamma}{2\pi}\cdot\frac{2\pi}{\Gamma} = 1 .
> $$
>
> With $\rho(x) = \frac{1}{\pi}\frac{1}{1 + x^2}$ ($\int\rho = 1$) and $\varepsilon = \Gamma/2$,
>
> $$
> \rho_\varepsilon(x) = \frac1\varepsilon\,\rho\Bigl(\frac x\varepsilon\Bigr) = \frac{1}{\pi}\,\frac{\varepsilon}{\varepsilon^2 + x^2} = \frac{\Gamma}{2\pi}\,\frac{1}{x^2 + \Gamma^2/4} = f_{\rm BW} ,
> $$
>
> a nascent delta function: $f_{\rm BW} \to \delta(\sqrt s - m)$ as $\Gamma \to 0$ ([[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], 3).
>
> **What the derivation shows.**
> - The width of the resonance peak equals the decay rate: an unstable particle "does not have a fixed mass" but a distribution of width $\Gamma$ (Yu p. 482), and the peak height grows like $(m\Gamma)^{-2}$ as the width shrinks.
> - The same Lorentzian, with $E$ for $\sqrt s$, is PS's non-relativistic Breit–Wigner formula (4.63) and the natural line shape of quantum mechanics ([[§C9.6 The Interaction Picture and the Atom–Field Interaction#^thm-c9-6-11|QM Theorem §C9.6.11]], 4).

^der-c6b-7-4

*Uses:* [[§C6b.7 The Width in the Propagator#^mod-c6b-7-1|Model §C6b.7.1]], [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]]

![[ph-qft-c6-15-1.svg]]
*The Breit–Wigner shape $\lvert1/(s - m^2 + im\Gamma)\rvert^2$ as a function of $\sqrt s$, for $m/\Gamma = 10$ (solid), normalized to its peak; the full width at half maximum is $\Gamma$. Dashed: half the width (same $m$); as $\Gamma \to 0$ the normalized curve becomes $\delta(\sqrt s - m)$, a stable particle. Added figure, from the user's notes (Figure "breitwigner").*

> [!remark] Remark: Why mΓ, not Γ
> The term added to $p^2 - m^2$ must be a Lorentz scalar of dimension two; $\Gamma$ alone has dimension one, and $m\Gamma$ is the combination whose pole reproduces the rest-frame decay rate, $\Gamma_{\rm NR} = \Gamma$ at $E_{\mathbf p} = m$ ([[§C6b.7 The Width in the Propagator#^thm-c6b-7-3|Theorem §C6b.7.3]]). In the lecture: "you might be more happy if I actually give it dimensions … It's an $i\,m\Gamma$." The infinitesimal $i\varepsilon$ of a stable particle is the limit $\Gamma \to 0$; "if it weren't stable, … it actually would make life a little harder for you because this one would be finite."
>
> *Source: PHY 513 Lecture 15, transcript · the user's PHY 513 notes, Ch. 15 §15.8 (paragraph "Checks (filled in)")*

^rem-c6b-7-1

> [!remark]- ★ Remark: Yu's route to the width
> Yu derives the width in the propagator in §10.6, beyond this course so far. The optical theorem applied to $A \to A$ gives $2\operatorname{Im}\mathcal M(A \to A) = \sum_f\frac{1}{\mathcal S_f}\int d\Pi_f|\mathcal M(A \to f)|^2 = 2m_A\sum_f\Gamma_f$ (eq. (10.259), using his decay formula (6.377)), so $\operatorname{Im}\mathcal M(A \to A) = m_A\Gamma_A$ (eq. (10.261)). For a scalar the full propagator is $\frac{i}{p^2 - m^2 - \delta m^2 - \Pi(p^2) + i\epsilon}$ with the one-particle-irreducible self-energy $-i\Pi$ (eqs. (10.262)–(10.263)); $i\mathcal M(\phi \to \phi) = -iZ\Pi(m^2)$ (eq. (10.264)) gives $\Gamma = -\frac{Z}{m}\operatorname{Im}\Pi(m^2)$ (eq. (10.265)). With the renormalization conditions moved to the real part (eqs. (10.267)–(10.268)), near the pole $\tilde G^{(2)} \simeq \frac{iZ}{p^2 - m^2 - iZ\operatorname{Im}\Pi(m^2)} = \frac{iZ}{p^2 - m^2 + im\Gamma} \simeq \frac{i}{p^2 - m^2 + im\Gamma}$ (eq. (10.270)), the last step with $Z \simeq 1$; the narrow-width condition is $\Gamma \ll m$ (eq. (10.272)); the Breit–Wigner shape and its limit are eqs. (10.271)–(10.275), and the same $+im\Gamma$ rule for internal lines of vector and Dirac particles follows (box after eq. (10.275)). This is the "corollary of studying interacting wave function" of slide 22, read backwards.
>
> *Source: Yu §10.6, pp. 481–483, eqs. (10.259)–(10.275)*

^rem-c6b-7-2

> [!remark]- Connections
> - A complex energy shift from coupling to a continuum, $\Gamma = -2\operatorname{Im}\Delta$, is the non-relativistic origin of $+im\Gamma$; its golden-rule rate is the non-relativistic decay formula — [[§C9.6 The Interaction Picture and the Atom–Field Interaction#^thm-c9-6-11|QM Theorem §C9.6.11]], [[§C9.5 Fermi's Golden Rule#^thm-c9-5-1|QM Theorem §C9.5.1]].
> - The time-dilated decay rate is the time dilation of special relativity, seen in cosmic-ray muons reaching the ground — [[§A2.1 Time Dilation#^thm-a2-1-2|REL Theorem §A2.1.2]], [[§A2.1 Time Dilation#^ex-a2-1-2|REL Example §A2.1.2]].
> - The $+i\varepsilon$ that a finite width replaces is the Feynman prescription; with $\varepsilon \to m\Gamma$ the poles leave the real axis for good, and the Fourier transform back to time is the contour integral of the Feynman propagator — [[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-2|Theorem §C2b.6.2]], [[P2 Green's Functions by Contour Integration|P2]].
> - A Lorentzian of width $\varepsilon$ is the standard nascent delta function; the Breit–Wigner limit $\Gamma \to 0$ and the Sokhotski–Plemelj limit of $1/(x + i\varepsilon)$ are the same family — [[§CA.2 Generalized Functions#^thm-ca-2-5|Theorem §CA.2.5]], [[§CA.6 Boundary Values, iε Limits and Fundamental Solutions|§CA.6]].
<!-- CONN-7 -->
