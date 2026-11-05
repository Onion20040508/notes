---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.5
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.4 Feynman Rules for Yukawa Theory]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.6★ The Yukawa Potential]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 19–20, 23, and transcript (from about 61 min) · the user's PHY 513 notes, Lecture 17 update, §17.6 (paragraph "The order", Derivation "The relative sign (filled in)", Principle "Fermion–fermion scattering in Yukawa theory", eq. (ffamp), Figure "ffscatt", paragraphs "Reading the result", "The relative sign from antisymmetry", "The overall sign is a convention", Caution "Slips in the handwritten notes for this example") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, pp. 116–120, eqs. (4.113)–(4.116), (4.118)–(4.119) · Yu Zhao-Huan, 量子场论讲义, §7.1.2, eqs. (7.59), (7.61), (7.78)–(7.82), Fig. 7.4–7.5, pp. 274–280.*

The lecture's worked example: two fermions scatter into two fermions at order $g^2$, $f(p) + f(k) \to f(p') + f(k')$. "Once we become pros, we should be able to just look at a process" and draw the diagrams; the lecture "did it the long way first", by contractions ([[§C6d.5 Fermion–Fermion Scattering#^ex-c6d-5-1|Example §C6d.5.1]]). Two diagrams appear, the $t$-channel and the $u$-channel exchange of the scalar, with a relative minus sign. That sign is physical and follows from Fermi statistics alone ([[§C6d.5 Fermion–Fermion Scattering#^thm-c6d-5-1|Theorem §C6d.5.1]]); the overall sign depends on how the states are written ([[§C6d.5 Fermion–Fermion Scattering#^rem-c6d-5-1|Remark: The overall sign is a convention]]). Larsen's pointer: "I could have not even paid attention, and said these two had better have a relative minus sign, but then I would regret it next week", when the nonrelativistic limit is compared with the force between charges ([[§C6d.6★ The Yukawa Potential|§C6d.6★]]). PS work the same process in §4.7 (eq. (4.119)); Yu in §7.1.2 (eq. (7.82)).

**Setup.** [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] at order $g^2$, the lowest order of $ff \to ff$: free relativistic states over $|0\rangle$ for the in and out states, exact at this order ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]). States ordered as in [[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]: $|\mathbf p, \mathbf k\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| = \sqrt{2E_{\mathbf p'}2E_{\mathbf k'}}\,\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'}$. Spin labels are suppressed: $u(p) \equiv u^{s_p}(p)$ and so on, each spinor carrying the spin of its particle.

## The amplitude

> [!example] Example §C6d.5.1: f f → f f at Order g², by Contractions
> ![[ph-qft-c6d-5-1.svg]]
>
> For $f(p) + f(k) \to f(p') + f(k')$ in Yukawa theory, at order $g^2$,
>
> $$
> i\mathcal M = (-ig)^2\Bigl[\bar u(p')u(p)\,\frac{i}{(p - p')^2 - m_\phi^2 + i\varepsilon}\,\bar u(k')u(k) \;-\; \bar u(k')u(p)\,\frac{i}{(p - k')^2 - m_\phi^2 + i\varepsilon}\,\bar u(p')u(k)\Bigr] ,
> $$
>
> the $t$-channel ($t = (p - p')^2$) and the $u$-channel ($u = (p - k')^2$) exchange of the scalar, with a relative minus sign.
>
> **Step 1** (the order). Four external fermions need four fermion fields: two vertices,
>
> $$
> \langle\mathbf p', \mathbf k'|\hat S|\mathbf p, \mathbf k\rangle^{(2)} = \frac{(-ig)^2}{2!}\int d^4x\,d^4y\;\langle\mathbf p', \mathbf k'|\,T\bigl\{\hat{\bar\psi}\hat\psi\hat\phi(x)\;\hat{\bar\psi}\hat\psi\hat\phi(y)\bigr\}\,|\mathbf p, \mathbf k\rangle
> $$
>
> ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-1|Theorem §C6d.4.1]], Step 1; slide 19).
>
> **Step 2** (who contracts with whom). The two scalar fields "have nowhere to go": there is no external scalar, so they contract with each other, $\overbracket{\hat\phi(x)\hat\phi(y)} = D_F(x - y)$. The two $\hat\psi$'s must absorb the incoming particles, through their $\hat a$ parts ("we don't want to hear anything about the $b$'s"), each giving a $u$; the two $\hat{\bar\psi}$'s must emit the outgoing ones, through their $\hat a^\dagger$ parts, each giving a $\bar u$ ([[§C6d.2 External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]; slide 20: "$\psi$'s contract with incoming particles, $\bar\psi$'s with outgoing"). A $\hat\psi$–$\hat{\bar\psi}$ contraction would leave only two fermion fields for four particles.
>
> **Step 3** (the four assignments). $\hat\psi(x)$ absorbs $p$ or $k$, $\hat{\bar\psi}(x)$ emits $p'$ or $k'$:
>
> | | $\hat\psi(x)$ | $\hat{\bar\psi}(x)$ | $\hat\psi(y)$ | $\hat{\bar\psi}(y)$ | pattern |
> |---|---|---|---|---|---|
> | A | $p$ | $p'$ | $k$ | $k'$ | $t$: $p \to p'$ at $x$ |
> | B | $k$ | $k'$ | $p$ | $p'$ | $t$: A with $x \leftrightarrow y$ |
> | C | $p$ | $k'$ | $k$ | $p'$ | $u$: $p \to k'$ at $x$ |
> | D | $k$ | $p'$ | $p$ | $k'$ | $u$: C with $x \leftrightarrow y$ |
>
> **Step 4** ($x \leftrightarrow y$ cancels $\frac{1}{2!}$). B is A with the integration variables renamed and the packages exchanged, which costs no sign ([[§C6d.1 Yukawa Theory#^thm-c6d-1-2|Theorem §C6d.1.2]]); likewise D and C. So $\frac{1}{2!}(A + B + C + D) = A + C$ ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-3|Theorem §C6d.4.3]]; PS p. 117: "there is a second, identical term that comes from interchanging $x$ and $y$").
>
> **Step 5** (signs). The fermion string is $\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'}\,\hat{\bar\psi}_x\hat\psi_x\,\hat{\bar\psi}_y\hat\psi_y\,\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle$, positions $1, \dots, 8$. Pattern A pairs $(2, 3)$, $(4, 7)$, $(1, 5)$, $(6, 8)$: $(4, 7)$ crosses $(1, 5)$ and $(6, 8)$, the others are nested or apart: **2 crossings, sign $+$**. Pattern C pairs $(1, 3)$, $(2, 5)$, $(4, 7)$, $(6, 8)$: $(1, 3)$–$(2, 5)$, $(2, 5)$–$(4, 7)$, $(4, 7)$–$(6, 8)$ cross: **3 crossings, sign $-$** ([[§C6d.3 Wick's Theorem with Fermions#^thm-c6d-3-4|Theorem §C6d.3.4]]; figure after that theorem). (The user's notes check this with a Jordan–Wigner representation of four fermionic modes: $+1$ and $-1$.)
>
> **Step 6** (values of A). In written order the pairs give $\bar u(p')e^{ip'\cdot x}$, $u(p)e^{-ip\cdot x}$, $\bar u(k')e^{ik'\cdot y}$, $u(k)e^{-ik\cdot y}$ ([[§C6d.2 External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]), the spinor indices joined at each vertex into $\bar u(p')u(p)$ and $\bar u(k')u(k)$ ([[§C6d.2 External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]]). With $D_F(x - y) = \int\frac{d^4q}{(2\pi)^4}\frac{ie^{-iq\cdot(x - y)}}{q^2 - m_\phi^2 + i\varepsilon}$ ([[§C2b.6 Time Ordering, the Feynman Propagator and the iε Prescription#^thm-c2b-6-9|Theorem §C2b.6.9]]),
>
> $$
> A = (-ig)^2\int\frac{d^4q}{(2\pi)^4}\,\frac{i}{q^2 - m_\phi^2 + i\varepsilon}\;\bar u(p')u(p)\,\bar u(k')u(k)\int d^4x\,e^{i(p' - p - q)\cdot x}\int d^4y\,e^{i(k' - k + q)\cdot y} .
> $$
>
> The vertex integrals are $(2\pi)^4\delta^4(p' - p - q)$ and $(2\pi)^4\delta^4(k' - k + q)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the first fixes $q = p' - p$ (equivalently $p - p'$, $D_F$ being even), the second becomes $(2\pi)^4\delta^4(p + k - p' - k')$:
>
> $$
> A = (-ig)^2\,\bar u(p')u(p)\,\frac{i}{(p - p')^2 - m_\phi^2 + i\varepsilon}\,\bar u(k')u(k)\;(2\pi)^4\delta^4(p + k - p' - k') .
> $$
>
> **Step 7** (values of C). The same with $p' \leftrightarrow k'$ in the outgoing factors: the chains $\bar u(k')u(p)$ at $x$, $\bar u(p')u(k)$ at $y$, $q = k' - p$, and the sign $-$ of Step 5:
>
> $$
> C = -(-ig)^2\,\bar u(k')u(p)\,\frac{i}{(p - k')^2 - m_\phi^2 + i\varepsilon}\,\bar u(p')u(k)\;(2\pi)^4\delta^4(p + k - p' - k') .
> $$
>
> **Step 8** (read off). $A + C = i\mathcal M\,(2\pi)^4\delta^4(\cdots)$ ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]]): the statement. By the rules directly ([[§C6d.4 Feynman Rules for Yukawa Theory#^thm-c6d-4-1|Theorem §C6d.4.1]]): two vertices $(-ig)^2$, one scalar propagator, each fermion line a chain $\bar uu$, the sign of each diagram from item 4. "The whole thing closed nicely, because it's a scalar over here": each vertex joins an incoming to an outgoing fermion into a number. Since $(-ig)^2\,i = -ig^2$, the bracket equals PS's form $-ig^2\bigl[\frac{\bar u(p')u(p)\,\bar u(k')u(k)}{(p' - p)^2 - m_\phi^2} - \frac{\bar u(p')u(k)\,\bar u(k')u(p)}{(p' - k)^2 - m_\phi^2}\bigr]$, with $(p' - k)^2 = (p - k')^2$ by $p + k = p' + k'$.
>
> *Source: PHY 513 Lecture 17, slides 19–20, and transcript ("So there really are two different Orderings here"; "they are like equally good diagrams") · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The order", Derivation "The relative sign (filled in)", Principle "Fermion–fermion scattering in Yukawa theory", eq. (ffamp), Figure "ffscatt" · PS §4.7, pp. 116–120, eqs. (4.113)–(4.116), (4.118)–(4.119) · Yu §7.1.2, eqs. (7.78)–(7.82) · Steps 5–7 written out here*

^ex-c6d-5-1

> [!theorem] Theorem §C6d.5.1: The Relative Sign from Fermi Statistics
> For identical external fermions the amplitude is antisymmetric under exchange of two final fermions together with their spins,
>
> $$
> \mathcal M\bigl(p, k \to (p', s'), (k', r')\bigr) = -\,\mathcal M\bigl(p, k \to (k', r'), (p', s')\bigr) ,
> $$
>
> and likewise for two initial fermions. In $ff \to ff$ the exchange $(p', s') \leftrightarrow (k', r')$ maps the $t$-diagram of [[§C6d.5 Fermion–Fermion Scattering#^ex-c6d-5-1|Example §C6d.5.1]] onto the $u$-diagram, so the two enter with opposite signs. Which of them carries the $-$ is fixed by the order of the states ([[§C6d.5 Fermion–Fermion Scattering#^rem-c6d-5-1|Remark: The overall sign is a convention]]); that they differ is not.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* any order, any theory of fermions (QED alike): a property of the states, not of the dynamics; at order $g^2$ it fixes the relative sign without any contraction bookkeeping.
>
> *Source: PHY 513 Lecture 17, slide 23 ("Relative signs enforce statistics of identical particles"), and transcript ("aren't these fermions? Therefore, if I change the two final states, it's supposed to be antisymmetric. Therefore … they better have opposite signs") · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The relative sign from antisymmetry" · PS §4.7, p. 120 ("The minus sign difference between these diagrams is a reflection of Fermi statistics") · Yu §7.1.2, p. 279 ("体现了交换末态全同费米子的反对称性") · proof written here*

^thm-c6d-5-1

> [!derivation]- Derivation
> **Step 1** (the states). By [[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] and $\{\hat a_{\mathbf k'}, \hat a_{\mathbf p'}\} = 0$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]),
>
> $$
> \langle(\mathbf p', s'), (\mathbf k', r')| = \sqrt{\cdots}\,\langle0|\hat a^{r'}_{\mathbf k'}\hat a^{s'}_{\mathbf p'} = -\sqrt{\cdots}\,\langle0|\hat a^{s'}_{\mathbf p'}\hat a^{r'}_{\mathbf k'} = -\langle(\mathbf k', r'), (\mathbf p', s')| :
> $$
>
> the state of two identical fermions is antisymmetric (the Pauli principle, [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]).
>
> **Step 2** (the amplitude). $\langle f|i\hat T|i\rangle$ is linear in $\langle f|$, and the delta $\delta^4(p + k - p' - k')$ is symmetric under $p' \leftrightarrow k'$; by [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], $\mathcal M$ changes sign. The initial pair: the same with $\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k} = -\hat a^\dagger_{\mathbf k}\hat a^\dagger_{\mathbf p}$.
>
> **Step 3** ($t \leftrightarrow u$). Call $\mathcal T(p', k') = \bar u(p')u(p)\frac{i}{(p - p')^2 - m_\phi^2}\bar u(k')u(k)$ the $t$-term. Exchanging $(p', s') \leftrightarrow (k', r')$ in it gives $\bar u(k')u(p)\frac{i}{(p - k')^2 - m_\phi^2}\bar u(p')u(k) = \mathcal T(k', p')$, the $u$-term. At order $g^2$ the amplitude is a combination $\alpha\,\mathcal T(p', k') + \beta\,\mathcal T(k', p')$ of the two diagrams ([[§C6d.5 Fermion–Fermion Scattering#^ex-c6d-5-1|Example §C6d.5.1]], Steps 2–4: no other contraction pattern exists), with $|\alpha| = |\beta| = g^2$ from the rules. Antisymmetry under $p' \leftrightarrow k'$ requires $\beta = -\alpha$. The initial exchange $p \leftrightarrow k$ also maps $t$ onto $u$, since $(k - p')^2 = (p - k')^2$ by momentum conservation.
>
> **What the derivation shows.**
> - The relative sign is Fermi statistics in the amplitude; for bosons the same argument gives $\beta = +\alpha$ (the $t$ and $u$ channels of [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|§C6c.6, Theorem §C6c.6.4]]).
> - ⚑ By-product: the interference term $-2\operatorname{Re}(\mathcal M_t^{\ast}\mathcal M_u)$ of $|\mathcal M|^2$ has its sign from here (Yu (7.75)) → cross sections (C8, planned).

^der-c6d-5-1

*Uses:* [[§C6d.2 External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^def-c6b-1-3|Def. §C6b.1.3]], [[§C6d.5 Fermion–Fermion Scattering#^ex-c6d-5-1|Example §C6d.5.1]]

> [!remark] Remark: The overall sign is a convention
> Writing $|\mathbf k, \mathbf p\rangle$ for $|\mathbf p, \mathbf k\rangle$, or $\langle\mathbf k', \mathbf p'|$ for $\langle\mathbf p', \mathbf k'|$, flips the sign of $\mathcal M$ ([[§C6d.5 Fermion–Fermion Scattering#^thm-c6d-5-1|Theorem §C6d.5.1]], Step 1); $|\mathcal M|^2$, and with it every cross section, is unchanged ("Overall sign usually irrelevant (only $|\mathcal M|^2$ appears in cross-section)", slide 23). The sources differ only here:
>
> | source | states | $t$-term | $u$-term |
> |---|---|---|---|
> | the user's notes (§17.6), PS (4.118)–(4.119), this section | bra the adjoint of the ket, $\langle0\vert\hat a_{\mathbf k'}\hat a_{\mathbf p'}$ | $+$ | $-$ |
> | Lecture 17, slide 20 and the board | not stated ("What exactly were those states?") | $-$ | $+$ |
> | Yu (7.82) | bra in the order of the labels, $\langle0\vert\hat a_{\mathbf q_1}\hat a_{\mathbf q_2}$ (7.12) | $-$ | $+$ |
>
> With the bra $\langle0|\hat a_{\mathbf p'}\hat a_{\mathbf k'}$ (labels in order) the string of Step 5 of [[§C6d.5 Fermion–Fermion Scattering#^ex-c6d-5-1|Example §C6d.5.1]] has the $t$-pairs $(1, 3)$, $(4, 7)$, $(2, 5)$, $(6, 8)$: three crossings, sign $-$, and the $u$-pattern two: the slide's and Yu's signs (derived here; the lecture: "I wrote minus a little bit randomly"). The overall sign becomes meaningful when the amplitude is compared with the unscattered term $\langle f|i\rangle$ of $\hat S = \mathbb 1 + i\hat T$, as in the Born approximation, where the convention $(|f\rangle)^\dagger = \langle f|$ of PS (4.118) is used: "next week a sign will matter" ([[§C6d.6★ The Yukawa Potential|§C6d.6★]]). The signs inside Wick's theorem, from reordering bilinears, never cause this ambiguity: they come in packages ([[§C6d.3 Wick's Theorem with Fermions#^rem-c6d-3-1|§C6d.3, Remark: Where the fermion signs go]]).
>
> *Source: PHY 513 Lecture 17, slides 20, 23, and transcript (about 70–75 min) · the user's PHY 513 notes, Lecture 17 update, §17.6, paragraph "The overall sign is a convention" · PS §4.7, p. 119, eq. (4.118), p. 120, eq. (4.119) · Yu §7.1, eq. (7.12); §7.1.2, eq. (7.82) · the crossing count for the label-ordered bra written here*

^rem-c6d-5-1

> [!caution] Caution: Slips in the handwritten notes and on slide 20 for this example
> The user's update lists three slips of the handwritten page (the page itself is not a source here):
> 1. The plane waves are written $e^{-ip\cdot x - ik\cdot y - ip'\cdot x - ik'\cdot y}$; outgoing particles give $e^{+ip'\cdot x}$, $e^{+ik'\cdot y}$ ([[§C6d.2 External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]), so the exponent is $-i(p - p')\cdot x - i(k - k')\cdot y$, which is what makes momentum conservation come out.
> 2. The second line has $\bar u(k)u(k)$ for $\bar u(k')u(k)$.
> 3. The result is written $(-ig)^2D_F(p - p')\bigl(\bar u(p')u(p)\bar u(k')u(k) + k \leftrightarrow p\bigr)$; the exchanged term has its own propagator, at $p - k'$, and enters with a relative minus sign; the diagrams below it carry the relative sign.
>
> Slide 20 has the analogue of item 3: "$i\mathcal M = (-ig)^2D_F(p - p')\bigl[(-)(\bar u(p')u(p))(\bar u(k')u(k)) + p \leftrightarrow k\bigr]$" factors the $t$-channel propagator out of both terms; the $p \leftrightarrow k$ image carries $D_F$ at $k - p'$, i.e. at $(p - k')^2$, as the slide's own second diagram ("$p - k'$") shows. Its first exponent, printed $e^{i(px' + k'y - px - ky)}$, means $p'\cdot x$. The lecture itself said "this was not done well" and that the diagrams are the better way to write it.
>
> *Source: the user's PHY 513 notes, Lecture 17 update, §17.6, Caution "Slips in the handwritten notes for this example" · PHY 513 Lecture 17, slide 20, and transcript · recorded in `qft-C/ERRATA.md`*

^cau-c6d-5-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the two vertex integrals give the momentum deltas that fix the exchanged momentum.

> [!remark]- Connections
> - The two diagrams are the $t$- and $u$-channels of a scalar theory, now with spinor chains and a relative sign; for identical bosons the sign would be $+$ — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], [[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-7|Theorem §C6b.1.7]].
> - In the elastic region the exchanged momentum $q = p - p'$ is spacelike, $q^2 = t \le 0$, so the scalar is off its mass shell and the propagator has no pole — [[§C6c.6 Feynman Rules for Amplitudes#^thm-c6c-6-4|Theorem §C6c.6.4]], 2.
> - Its nonrelativistic limit for distinguishable fermions is the attractive Yukawa potential; for a fermion and an antifermion the spinor products and the contraction sign both flip, and the force stays attractive — [[§C6d.6★ The Yukawa Potential|§C6d.6★]].
> - $|\mathcal M|^2$ summed over spins needs traces of $\gamma$ matrices; the same process in QED is Møller scattering, a process of C8 (planned) — [[§C5a.14 Gamma-Matrix Technology|§C5a.14]].
