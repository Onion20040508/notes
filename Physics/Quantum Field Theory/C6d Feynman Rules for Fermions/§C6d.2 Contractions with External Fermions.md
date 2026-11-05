---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6d
section: C6d.2
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6d.1 Yukawa Theory]] · ↑ [[· C6d Feynman Rules for Fermions]] · [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule]] →

*Sources: PHY 513 Lecture 17 (Larsen, 4 Nov 2026), slides 9–12, and transcript · the user's PHY 513 notes, Lecture 17 update, §17.3 (eq. (fermionstates), eq. (psipsibarsplit), Derivation "An incoming particle", Principle "External fermion lines", Figure "extfermions", paragraphs "Asked in the lecture", "The arrows, again", "A check that cannot fail silently") · Peskin & Schroeder, An Introduction to Quantum Field Theory, §4.7, p. 117, eq. (4.114); p. 118 (rule 3, "External leg contractions"); p. 119, eqs. (4.117)–(4.118) · Yu Zhao-Huan, 量子场论讲义, §7.1, eqs. (7.8)–(7.20), (7.25)–(7.27), (7.29), (7.31)–(7.32), pp. 262–267; §7.1.2, eqs. (7.79)–(7.80), pp. 277–278 (page images checked).*

A scalar field in $\hat H_I$ that meets an external particle produces its wave function $e^{\mp ip\cdot x}$, and in momentum space the external line is "$1$" ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]). For fermions the same step gives a spinor times the plane wave, and the spinor stays when the plane wave is stripped: "wave factor is stripped off but wave function remains" (slide 12). There are four cases, particle or antiparticle, incoming or outgoing; "I can never for the life of me remember the rules, where the $u$'s are and the $v$'s are" (transcript), so this section derives all four from the frequency parts of $\hat\psi$ and $\hat{\bar\psi}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]) and the states ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]): [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]. Each vertex being $\hat{\bar\psi}\hat\psi$, every fermion line is then a row times matrices times a column, a number ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-4|Theorem §C6d.2.4]]). Several fields acting on one state contract from the inside out ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]]), and $n$ identical fermion fields on $n$ identical fermions give the $n!$ contractions with the signs of their permutations ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-3|Theorem §C6d.2.3]]): the fermion forms of [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]] and [[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]]. The one-particle wave functions $\langle0|\hat\psi(x)|\mathbf p, s\rangle$, $\langle0|\hat{\bar\psi}(x)|\mathbf p, s\rangle^c$ are already [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]]; here they are stated as contractions, the form the rules use. Yu derives the same contractions in §7.1, eqs. (7.13)–(7.18); PS show one, eq. (4.114).

**Setup.** Free Dirac field ([[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]) and free relativistically normalized states over $|0\rangle$: every statement is an exact identity of free operators and free states, used inside the Dyson series of [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] with the scope of [[§C6c.2 Contractions with External Particles|§C6c.2]] (lowest order; beyond it $\sqrt Z$).

*Conventions* ([[Larsen PHY 513]]): $u^s(p)$, $v^s(p)$ and their Dirac conjugates $\bar u^s = u^{s\dagger}\gamma^0$, $\bar v^s = v^{s\dagger}\gamma^0$ as in [[§C5a.11 The Spinors u(p), v(p) and Their Dirac Conjugates|§C5a.11]]; anticommutators $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, all others zero ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]); a contraction with an external particle is written with the bracket, $\overbracket{\hat\psi(x)|\mathbf p, s\rangle}$, as PS (4.114) and slide 12.

## The fields and the states

> [!definition] Definition §C6d.2.1: Positive- and Negative-Frequency Parts of ψ̂ and ψ̄̂
> Split the free fields of [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]] into the parts with annihilation operators ($+$, positive frequency $e^{-ip\cdot x}$) and with creation operators ($-$, $e^{+ip\cdot x}$):
>
> $$
> \hat\psi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\Bigl(\underbrace{\hat a^s_{\mathbf p}\,u^s(p)\,e^{-ip\cdot x}}_{\hat\psi^+}\; + \;\underbrace{\hat b^{s\dagger}_{\mathbf p}\,v^s(p)\,e^{+ip\cdot x}}_{\hat\psi^-}\Bigr) ,
> $$
>
> $$
> \hat{\bar\psi}(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\Bigl(\underbrace{\hat b^s_{\mathbf p}\,\bar v^s(p)\,e^{-ip\cdot x}}_{\hat{\bar\psi}^+}\; + \;\underbrace{\hat a^{s\dagger}_{\mathbf p}\,\bar u^s(p)\,e^{+ip\cdot x}}_{\hat{\bar\psi}^-}\Bigr) .
> $$
>
> So $\hat\psi^+|0\rangle = \hat{\bar\psi}^+|0\rangle = 0$ and $\langle0|\hat\psi^- = \langle0|\hat{\bar\psi}^- = 0$. $\hat{\bar\psi}^\pm$ is not the Dirac conjugate of $\hat\psi^\pm$: $\hat{\bar\psi}^+ = (\hat\psi^-)^\dagger\gamma^0$, $\hat{\bar\psi}^- = (\hat\psi^+)^\dagger\gamma^0$, since daggering exchanges $\hat a \leftrightarrow \hat a^\dagger$, $\hat b^\dagger \leftrightarrow \hat b$ and $e^{-ip\cdot x} \leftrightarrow e^{+ip\cdot x}$, and $\gamma^0$ on the right turns $u^\dagger$, $v^\dagger$ into $\bar u$, $\bar v$. This is the split of [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]], with the formulas written out; the scalar's is [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]].
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free (interaction-picture) Dirac field, exact.
>
> *Source: PHY 513 Lecture 17, slides 2, 10–11 (the expansions of $\hat\psi_I$ and $\bar\psi_I$), slide 21 ("positive ∝ $a^s_{\vec p}$ or $b^s_{\vec p}$ and negative ∝ $a^{s\dagger}_{\vec p}$ or $b^{s\dagger}_{\vec p}$ frequency parts") · the user's PHY 513 notes, Lecture 17 update, §17.3, eq. (psipsibarsplit) and the paragraph after it · PS §4.7, p. 116, eq. (4.108) ($\psi^+$, $\bar\psi^-$) · Yu §6.3, eqs. (6.138)–(6.139) ($\psi^{(\pm)}$); §6.4.5, eqs. (6.254)–(6.256) ($\bar\psi^{(\pm)}$; names: [[Larsen PHY 513]], row "Positive and negative frequency")*

^def-c6d-2-1

> [!definition] Definition §C6d.2.2: External Fermion States and Their Order
> The one-particle states are those of [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]], fermion (particle) and antifermion (antiparticle, the superscript $c$ for "conjugate"), with their bras:
>
> $$
> |\mathbf p, s\rangle = \sqrt{2E_{\mathbf p}}\,\hat a^{s\dagger}_{\mathbf p}|0\rangle , \quad \langle\mathbf p, s| = \sqrt{2E_{\mathbf p}}\,\langle0|\hat a^s_{\mathbf p} ; \qquad |\mathbf p, s\rangle^c = \sqrt{2E_{\mathbf p}}\,\hat b^{s\dagger}_{\mathbf p}|0\rangle , \quad {}^c\langle\mathbf p, s| = \sqrt{2E_{\mathbf p}}\,\langle0|\hat b^s_{\mathbf p} .
> $$
>
> A state of several fermions and antifermions is the product of the creation operators **in the order the labels are listed**, and its bra is the Hermitian conjugate, with the annihilation operators in the **reversed** order: with $\hat c_j = \hat a$ or $\hat b$ for a particle or an antiparticle,
>
> $$
> |1, 2, \dots, n\rangle = \prod_j\sqrt{2E_j}\;\hat c^\dagger_1\hat c^\dagger_2\cdots\hat c^\dagger_n|0\rangle , \qquad \langle1, 2, \dots, n| = \bigl(|1, \dots, n\rangle\bigr)^\dagger = \prod_j\sqrt{2E_j}\;\langle0|\hat c_n\cdots\hat c_2\hat c_1 ;
> $$
>
> e.g. $|\mathbf p, \mathbf k\rangle = \sqrt{2E_{\mathbf p}2E_{\mathbf k}}\,\hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k}|0\rangle$ and $\langle\mathbf p', \mathbf k'| = \sqrt{2E_{\mathbf p'}2E_{\mathbf k'}}\,\langle0|\hat a_{\mathbf k'}\hat a_{\mathbf p'}$ (spin labels suppressed). Exchanging two fermion labels changes the sign of the state: the overall sign of an amplitude depends on this order ([[§C6d.5 Second Order#^rem-c6d-5-1|§C6d.5, Remark: The overall sign is a convention]]). Scalars are added as factors $\sqrt{2E}\,\hat a^\dagger_\phi$, which commute with everything fermionic.
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]], with the scalar of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free states over $|0\rangle$, relativistic normalization ([[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]]), exact.
>
> *Source: PHY 513 Lecture 17, slides 10–11 ("Incoming fermion $= |\vec p, s\rangle = \sqrt{2E_{\vec p}}\,\hat a^{s\dagger}_{\vec p}|0\rangle$ … Outgoing anti-fermion $= {}^c\langle\vec p, s| = \langle0|\hat b^s_{\vec p}\sqrt{2E_{\vec p}}$"), and transcript · the user's PHY 513 notes, Lecture 17 update, §17.3, eq. (fermionstates) ("the superscript $c$ of the handwritten notes for the conjugate (anti)particle"), §17.6, Derivation "The relative sign" (the two-particle states) · PS §4.7, p. 119, eq. (4.118) ($|\mathbf p, \mathbf k\rangle \sim a^\dagger_{\mathbf p}a^\dagger_{\mathbf k}|0\rangle$, $\langle\mathbf p', \mathbf k'| \sim \langle0|a_{\mathbf k'}a_{\mathbf p'}$, "so that $(|p, k\rangle)^\dagger = \langle p, k|$"); p. 122 (fermion–antifermion, $a^\dagger_{\mathbf p}b^\dagger_{\mathbf k}$) · Yu §7.1, eqs. (7.8)–(7.12) ($|\mathbf p^+, \lambda\rangle$, $|\mathbf p^-, \lambda\rangle$; his bras keep the order of the labels, [[§C6d.4 First Order#^cau-c6d-4-1|§C6d.4, Caution: Yu's (7.23)–(7.24) and his order of the bra]])*

^def-c6d-2-2

## The four external wave functions

> [!theorem] Theorem §C6d.2.1: The Four External Fermion Wave Functions
> With [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]] and [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]:
>
> | external fermion | contraction | wave function | momentum space |
> |---|---|---|---|
> | incoming particle | $\hat\psi^+(x)\,\vert\mathbf p, s\rangle = u^s(p)\,e^{-ip\cdot x}\,\vert0\rangle$ | $u^s(p)\,e^{-ip\cdot x}$ | $u^s(p)$ |
> | outgoing antiparticle | ${}^c\langle\mathbf p, s\vert\,\hat\psi^-(x) = \langle0\vert\,v^s(p)\,e^{+ip\cdot x}$ | $v^s(p)\,e^{+ip\cdot x}$ | $v^s(p)$ |
> | outgoing particle | $\langle\mathbf p, s\vert\,\hat{\bar\psi}^-(x) = \langle0\vert\,\bar u^s(p)\,e^{+ip\cdot x}$ | $\bar u^s(p)\,e^{+ip\cdot x}$ | $\bar u^s(p)$ |
> | incoming antiparticle | $\hat{\bar\psi}^+(x)\,\vert\mathbf p, s\rangle^c = \bar v^s(p)\,e^{-ip\cdot x}\,\vert0\rangle$ | $\bar v^s(p)\,e^{-ip\cdot x}$ | $\bar v^s(p)$ |
>
> Equivalently, the contractions are the $c$-numbers $\sqrt{2E_{\mathbf p}}\{\hat\psi^+_a(x), \hat a^{s\dagger}_{\mathbf p}\} = u^s_a(p)e^{-ip\cdot x}$, $\sqrt{2E_{\mathbf p}}\{\hat b^s_{\mathbf p}, \hat\psi^-_a(x)\} = v^s_a(p)e^{ip\cdot x}$, $\sqrt{2E_{\mathbf p}}\{\hat a^s_{\mathbf p}, \hat{\bar\psi}^-_a(x)\} = \bar u^s_a(p)e^{ip\cdot x}$, $\sqrt{2E_{\mathbf p}}\{\hat{\bar\psi}^+_a(x), \hat b^{s\dagger}_{\mathbf p}\} = \bar v^s_a(p)e^{-ip\cdot x}$, and all other pairings vanish: $\hat\psi$ meets only an incoming particle or an outgoing antiparticle ("either do one or the other"), $\hat{\bar\psi}$ only an outgoing particle or an incoming antiparticle. In momentum space the plane waves go into the vertex deltas and the spinor remains; an external scalar gives $1$ ([[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]).
>
> *Equivalently,* the scalar case is [[§C6c.2 Contractions with External Particles#^lem-c6c-2-1|Lemma §C6c.2.1]] and [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]: the same contractions, with the spinors $u$, $\bar u$, $\bar v$, $v$ replaced by $1$.
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free fields and free one-particle states, exact; in a scattering amplitude, the external factors at lowest order (beyond it $\sqrt Z$, [[§C6c.1 Amplitudes from Correlation Functions#^cau-c6c-1-2|§C6c.1, Caution: The rule is stated at lowest order]]).
>
> *Source: PHY 513 Lecture 17, slides 10–12 (slide 10: "Contraction: $\psi^+_I(x)|\vec p, s\rangle = u^s(p)e^{-ipx}|0\rangle$ … ${}^c\langle\vec p, s|\psi^-_I(x) = \langle0|v^s(p)e^{ipx}$"; slide 11: [[§C6d.2 Contractions with External Fermions#^cau-c6d-2-2|Caution: The plane wave of an incoming antifermion]]; slide 12: the four lines in momentum space), and transcript · the user's PHY 513 notes, Lecture 17 update, §17.3, Derivation "An incoming particle" (the first case; "the same three steps give the other three") and Principle "External fermion lines" (a principle there, a theorem here because all four are derived) · PS §4.7, p. 117, eq. (4.114), p. 118 (rule 3) · Yu §7.1, eqs. (7.13)–(7.18) ((7.15), (7.18): the scalar) · the other three derivations written here*

^thm-c6d-2-1

> [!derivation]- Derivation
> In each case the integration and summation variables are renamed $\mathbf q$, $r$, so that they are not confused with the labels $\mathbf p$, $s$ of the state ("the things I integrate over and sum over should obviously not be the same as the things I'm acting on", transcript).
>
> **1. Incoming particle.** Insert $\hat\psi^+$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]) and $|\mathbf p, s\rangle$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]):
>
> $$
> \hat\psi^+(x)|\mathbf p, s\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{\sqrt{2E_{\mathbf p}}}{\sqrt{2E_{\mathbf q}}}\sum_r u^r(q)\,e^{-iq\cdot x}\;\hat a^r_{\mathbf q}\hat a^{s\dagger}_{\mathbf p}|0\rangle .
> $$
>
> Since $\hat a^r_{\mathbf q}|0\rangle = 0$, $\hat a^r_{\mathbf q}\hat a^{s\dagger}_{\mathbf p}|0\rangle = \bigl(\{\hat a^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\} - \hat a^{s\dagger}_{\mathbf p}\hat a^r_{\mathbf q}\bigr)|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)|0\rangle$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]]): an anticommutator, but the term with the opposite order vanishes, so "don't worry about any signs at this point". The $\delta^3$ does the $\mathbf q$ integral ($\mathbf q = \mathbf p$, $q^0 = E_{\mathbf p}$, so $q = p$), the $(2\pi)^3$ cancels, $\sqrt{2E_{\mathbf p}}/\sqrt{2E_{\mathbf q}} = 1$ on the support ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], 1), and $\delta^{rs}$ does the spin sum:
>
> $$
> \hat\psi^+(x)|\mathbf p, s\rangle = u^s(p)\,e^{-ip\cdot x}\,|0\rangle .
> $$
>
> **2. Outgoing antiparticle.** The bra ${}^c\langle\mathbf p, s| = \sqrt{2E_{\mathbf p}}\langle0|\hat b^s_{\mathbf p}$ needs a $\hat b^\dagger$, which sits in $\hat\psi^-$:
>
> $$
> {}^c\langle\mathbf p, s|\hat\psi^-(x) = \int\frac{d^3q}{(2\pi)^3}\frac{\sqrt{2E_{\mathbf p}}}{\sqrt{2E_{\mathbf q}}}\sum_r\langle0|\hat b^s_{\mathbf p}\hat b^{r\dagger}_{\mathbf q}\;v^r(q)\,e^{+iq\cdot x} .
> $$
>
> $\langle0|\hat b^s_{\mathbf p}\hat b^{r\dagger}_{\mathbf q} = \langle0|\bigl(\{\hat b^s_{\mathbf p}, \hat b^{r\dagger}_{\mathbf q}\} - \hat b^{r\dagger}_{\mathbf q}\hat b^s_{\mathbf p}\bigr) = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)\langle0|$, since $\langle0|\hat b^{r\dagger}_{\mathbf q} = (\hat b^r_{\mathbf q}|0\rangle)^\dagger = 0$. The same three steps (delta, $\sqrt{2E}$, Kronecker delta) give ${}^c\langle\mathbf p, s|\hat\psi^-(x) = \langle0|\,v^s(p)\,e^{+ip\cdot x}$.
>
> **3. Outgoing particle.** $\langle\mathbf p, s| = \sqrt{2E_{\mathbf p}}\langle0|\hat a^s_{\mathbf p}$ needs the $\hat a^\dagger$ of $\hat{\bar\psi}^-$:
>
> $$
> \langle\mathbf p, s|\hat{\bar\psi}^-(x) = \int\frac{d^3q}{(2\pi)^3}\frac{\sqrt{2E_{\mathbf p}}}{\sqrt{2E_{\mathbf q}}}\sum_r\langle0|\hat a^s_{\mathbf p}\hat a^{r\dagger}_{\mathbf q}\;\bar u^r(q)\,e^{+iq\cdot x} = \langle0|\,\bar u^s(p)\,e^{+ip\cdot x} ,
> $$
>
> with $\langle0|\hat a^s_{\mathbf p}\hat a^{r\dagger}_{\mathbf q} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)\langle0|$ as in Step 2.
>
> **4. Incoming antiparticle.** $|\mathbf p, s\rangle^c = \sqrt{2E_{\mathbf p}}\hat b^{s\dagger}_{\mathbf p}|0\rangle$ needs the $\hat b$ of $\hat{\bar\psi}^+$:
>
> $$
> \hat{\bar\psi}^+(x)|\mathbf p, s\rangle^c = \int\frac{d^3q}{(2\pi)^3}\frac{\sqrt{2E_{\mathbf p}}}{\sqrt{2E_{\mathbf q}}}\sum_r\bar v^r(q)\,e^{-iq\cdot x}\;\hat b^r_{\mathbf q}\hat b^{s\dagger}_{\mathbf p}|0\rangle = \bar v^s(p)\,e^{-ip\cdot x}\,|0\rangle ,
> $$
>
> with $\hat b^r_{\mathbf q}\hat b^{s\dagger}_{\mathbf p}|0\rangle = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)|0\rangle$ as in Step 1.
>
> **5. The pairings that vanish.** $\hat\psi^+$ has only $\hat a$'s: $\hat a^r_{\mathbf q}\hat b^{s\dagger}_{\mathbf p}|0\rangle = -\hat b^{s\dagger}_{\mathbf p}\hat a^r_{\mathbf q}|0\rangle = 0$, so $\hat\psi^+|\mathbf p, s\rangle^c = 0$; $\hat\psi^-$ has only $\hat b^\dagger$'s: $\langle0|\hat a^s_{\mathbf p}\hat b^{r\dagger}_{\mathbf q} = -\langle0|\hat b^{r\dagger}_{\mathbf q}\hat a^s_{\mathbf p} = 0$, so $\langle\mathbf p, s|\hat\psi^- = 0$; and $\hat\psi^-|\mathbf p, s\rangle$, $\langle\mathbf p, s|\hat\psi^+$ do not reduce to the vacuum (they add a particle or remove one from $\langle0|$). The same for $\hat{\bar\psi}$ with $\hat a \leftrightarrow \hat b$. So $\hat\psi$ connects only to $|\mathbf p, s\rangle$ and ${}^c\langle\mathbf p, s|$, and $\hat{\bar\psi}$ only to $\langle\mathbf p, s|$ and $|\mathbf p, s\rangle^c$.
>
> **6. The anticommutator form.** In Steps 1–4 the field part and the operator of the state met through one anticommutator, $\{\hat\psi^+_a(x), \hat a^{s\dagger}_{\mathbf p}\} = \frac{1}{\sqrt{2E_{\mathbf p}}}u^s_a(p)e^{-ip\cdot x}$ and so on (the integral and the deltas evaluated as above), a $c$-number: this is the form in which a contraction with an external particle enters a longer operator string ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]).
>
> **7. Momentum space.** In a diagram the plane wave of each contraction joins the others at its vertex, and $\int d^4x$ turns them into $(2\pi)^4\delta^4(\cdot)$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); the spinor has nowhere to go and remains.
>
> **What the derivation shows.**
> - The wave functions have the correct frequencies: $e^{-ip\cdot x}$ for incoming, $e^{+ip\cdot x}$ for outgoing particles of both kinds; "it's not one of these wrong frequency solutions" (transcript).
> - Which spinor appears is decided by which operator the field must supply: an incoming antiparticle needs a $\hat b$, found only in $\hat{\bar\psi}$, so it carries $\bar v$; an outgoing antiparticle needs a $\hat b^\dagger$, found only in $\hat\psi$, so $v$ ([[§C6d.2 Contractions with External Fermions#^cau-c6d-2-1|Caution: The outgoing antiparticle comes from ψ̂, not ψ̄̂]]).
> - Steps 1 and 4 are the two formulas of [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]], taken with $\langle0|$; Steps 2–3 are their adjoints' counterparts.

^der-c6d-2-1

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]], [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

![[ph-qft-c6d-2-1.svg]]
*[[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]: the four external fermion lines (the shaded blob is the rest of the diagram). Black arrow: fermion number ([[§C6d.1 Yukawa Theory#^def-c6d-1-1|Def. §C6d.1.1]]); orange arrow: momentum. For particles they agree; for antiparticles they are opposite, so an incoming antiparticle has its fermion arrow pointing out of the diagram. Added figure, after slide 12 and the user's Figure "extfermions".*

> [!caution] Caution: The outgoing antiparticle comes from ψ̂, not ψ̄̂
> Asked in the lecture: shouldn't the outgoing antiparticle come from $\hat{\bar\psi}$? No: the bra ${}^c\langle\mathbf p, s| = \sqrt{2E}\langle0|\hat b^s_{\mathbf p}$ needs a $\hat b^\dagger$ to its right, and $\hat b^\dagger$ is in $\hat\psi$ ($\hat\psi^-$), while $\hat{\bar\psi}$ contains $\hat b$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]). "I was just about getting persuaded to do the wrong thing. Will happen again, and you will also have to discuss with yourself, wait, was it the other way around?" The mode expansions settle it each time (Step 2 of [[§C6d.2 Contractions with External Fermions#^der-c6d-2-1|Derivation §C6d.2.1]]).
>
> *Source: PHY 513 Lecture 17, transcript (a student's question, about 29 min) · the user's PHY 513 notes, Lecture 17 update, §17.3, paragraph "Asked in the lecture: shouldn't the outgoing antiparticle come from $\bar\psi$?"*

^cau-c6d-2-1

> [!caution] Caution: The plane wave of an incoming antifermion
> Slide 11 writes the contraction of $\bar\psi_I$ with an incoming antifermion as $\bar\psi_I(x)|\vec p, s\rangle^c = \bar v^s(p)e^{ipx}|0\rangle$. The $\hat b$ that absorbs the antifermion sits in $\hat{\bar\psi}^+$ with $e^{-ip\cdot x}$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], slide 11's own expansion), so the wave function is $\bar v^s(p)\,e^{-ip\cdot x}$ (Step 4 of [[§C6d.2 Contractions with External Fermions#^der-c6d-2-1|Derivation §C6d.2.1]]; PS p. 117; Yu (7.14)): incoming particles of either kind have positive frequency. In momentum space the factor is $\bar v^s(p)$ either way (slide 12).
>
> *Source: PHY 513 Lecture 17, slide 11 · recorded in `qft-C/ERRATA.md`*

^cau-c6d-2-2

## Several fermions in one state

> [!theorem] Theorem §C6d.2.2: Several Fields on One State Contract from the Inside Out
> Let $|1, 2, \dots, n\rangle = \prod_j\sqrt{2E_j}\;\hat c^\dagger_1\hat c^\dagger_2\cdots\hat c^\dagger_n|0\rangle$ be a free state of [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]] (fermions, antifermions and scalars), and let $F_1, \dots, F_n$ be positive-frequency parts of free fields (components of $\hat\psi^+$, $\hat{\bar\psi}^+$, $\hat\phi^+$, [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]) such that $F_j$ can absorb particle $j$ and no other particle of the state (e.g. particles of pairwise different kinds). Then
>
> $$
> F_n\cdots F_2F_1\,|1, 2, \dots, n\rangle = w_1\,w_2\cdots w_n\,|0\rangle ,
> $$
>
> $w_j$ the wave function of particle $j$ at its field ($u^s(p)e^{-ip\cdot x}$, $\bar v^s(p)e^{-ip\cdot x}$, $e^{-ip\cdot x}$: [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]): the field written next to the state takes the first particle, the next field the second, and so on **from the inside out**, with no sign. Likewise for the bra $\langle1, \dots, n| = \prod_j\sqrt{2E_j}\,\langle0|\hat c_n\cdots\hat c_1$ and negative-frequency parts $G_j$ that can emit particle $j$ only,
>
> $$
> \langle1, 2, \dots, n|\,G_1G_2\cdots G_n = \langle0|\,\bar w_1\,\bar w_2\cdots\bar w_n ,
> $$
>
> the fields now in the order of the labels ($\bar w_j = \bar u^s(p)e^{ip\cdot x}$, $v^s(p)e^{ip\cdot x}$, $e^{ip\cdot x}$). Written in another order, the fermion fields give the same product times the sign of the permutation that restores this order: the contraction lines then cross ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1). Example (Yu (7.19)), with $|\mathbf p, s; \mathbf q, s'; \mathbf k\rangle = \sqrt{8E_{\mathbf p}E_{\mathbf q}E_{\mathbf k}}\,\hat a^{s\dagger}_{\mathbf p}\hat b^{s'\dagger}_{\mathbf q}\hat a^\dagger_{\phi,\mathbf k}|0\rangle$:
>
> $$
> \hat\phi^+(x)\,\hat{\bar\psi}^+_a(x)\,\hat\psi^+_a(x)\,|\mathbf p, s; \mathbf q, s'; \mathbf k\rangle = e^{-ik\cdot x}\;\bar v^{s'}_a(q)\,e^{-iq\cdot x}\;u^s_a(p)\,e^{-ip\cdot x}\;|0\rangle = \bar v^{s'}(q)u^s(p)\,e^{-i(p + q + k)\cdot x}\,|0\rangle .
> $$
>
> *Equivalently,* for scalars alone the order does not matter and the statement is [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 1; what fermions add is the order.
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]] with the scalar of [[§C2a.1 Canonical Quantization of Fields#^mod-c2a-1-1|Model §C2a.1.1]]; *applies:* free fields and free states over $|0\rangle$, exact, independent of the dynamics.
>
> *Source: Yu §7.1, eqs. (7.19)–(7.20), p. 264 ("第一步中三个正能解场算符的排列次序保证第二步中场算符与初态粒子由内至外依次进行缩并"; "从最内层开始，缩并掉一个场算符和相应的产生算符之后，得到的 c 数可以跟剩下的场算符交换位置"); eqs. (7.11)–(7.12) (his bra keeps the order of the labels, so his (7.20) writes the fields in the opposite order: [[§C6d.4 First Order#^cau-c6d-4-1|§C6d.4, Caution: Yu's (7.23)–(7.24) and his order of the bra]]) · PS §4.7, p. 119, eq. (4.118) · proof written here*

^thm-c6d-2-2

> [!derivation]- Derivation
> Write $[A, B\}_\epsilon = AB - \epsilon BA$ with $\epsilon = -1$ if $A$ and $B$ are both fermion operators and $\epsilon = +1$ otherwise ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-2|Theorem §C6d.3.2]]'s conventions); $[F, \hat c^\dagger\}_\epsilon$ is a $c$-number for every frequency part $F$ and creation operator $\hat c^\dagger$ ([[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]).
>
> **Step 1** (the innermost field). Move $F_1$ to the right through the creation operators:
>
> $$
> F_1\,\hat c^\dagger_1\hat c^\dagger_2\cdots\hat c^\dagger_n|0\rangle = [F_1, \hat c^\dagger_1\}_\epsilon\;\hat c^\dagger_2\cdots\hat c^\dagger_n|0\rangle + \epsilon\,\hat c^\dagger_1\,F_1\,\hat c^\dagger_2\cdots\hat c^\dagger_n|0\rangle .
> $$
>
> In the second term $F_1$ cannot absorb particles $2, \dots, n$, so $[F_1, \hat c^\dagger_j\}_\epsilon = 0$ for $j \ge 2$ and $F_1$ passes them with signs only, $F_1\hat c^\dagger_2\cdots\hat c^\dagger_n|0\rangle = \pm\,\hat c^\dagger_2\cdots\hat c^\dagger_nF_1|0\rangle = 0$ ($F_1$ contains only annihilation operators). With the normalization, $\sqrt{2E_1}\,[F_1, \hat c^\dagger_1\}_\epsilon = w_1$ (Step 6 of [[§C6d.2 Contractions with External Fermions#^der-c6d-2-1|Derivation §C6d.2.1]]; for a scalar [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], 2):
>
> $$
> F_1\,|1, 2, \dots, n\rangle = w_1\,|2, \dots, n\rangle .
> $$
>
> **Step 2** (inside out). $w_1$ is a number (a spinor component times a plane wave) and commutes with $F_2$. Step 1 for $F_2$ on $|2, \dots, n\rangle$: $F_2F_1|1, \dots, n\rangle = w_1F_2|2, \dots, n\rangle = w_1w_2|3, \dots, n\rangle$, and after $n$ steps $w_1\cdots w_n|0\rangle$. No sign has appeared: each field met the creation operator standing directly to its right.
>
> **Step 3** (another order). Let $F_2$ act first: $F_2\,\hat c^\dagger_1\hat c^\dagger_2\cdots|0\rangle = \epsilon_{21}\,\hat c^\dagger_1\,F_2\,\hat c^\dagger_2\cdots|0\rangle$, since $[F_2, \hat c^\dagger_1\}_\epsilon = 0$; $\epsilon_{21} = -1$ if $F_2$ and $\hat c^\dagger_1$ are both fermionic. Then Step 1 for $F_2$ and $\hat c^\dagger_2$, and $F_1$ last meets $\hat c^\dagger_1$: $F_1F_2|1, 2, \dots\rangle = \epsilon_{21}\,w_1w_2|3, \dots\rangle$. In general every fermion field that has to pass the creation operator of a fermion it does not absorb gives $-1$; drawn as arcs over the string $F_{\sigma(n)}\cdots F_{\sigma(1)}\hat c^\dagger_1\cdots\hat c^\dagger_n$ these are the crossings of [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1, and the product of the signs is the sign of the permutation.
>
> **Step 4** (the bra). Take the adjoint of Steps 1–2 for the outgoing particles, or repeat them from the left: $\langle0|\hat c_n\cdots\hat c_2\hat c_1\,G_1 = \langle0|\hat c_n\cdots\hat c_2\,[\hat c_1, G_1\}_\epsilon$, the other term vanishing as in Step 1 ($\langle0|G_1 = 0$). The field written next to $\hat c_1$ is the first field of the string: with the bra the inside-out order is the order of the labels. The $c$-numbers are $\sqrt{2E_j}[\hat c_j, G_j\}_\epsilon = \bar w_j$ ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]).
>
> **Step 5** (the example, as Yu (7.19)). $\hat\psi^+_a(x)$ absorbs the fermion: $\sqrt{2E_{\mathbf p}}\{\hat\psi^+_a(x), \hat a^{s\dagger}_{\mathbf p}\} = u^s_a(p)e^{-ip\cdot x}$, leaving $\sqrt{4E_{\mathbf q}E_{\mathbf k}}\,\hat b^{s'\dagger}_{\mathbf q}\hat a^\dagger_{\phi,\mathbf k}|0\rangle$. $\hat{\bar\psi}^+_a(x)$ absorbs the antifermion: $\sqrt{2E_{\mathbf q}}\{\hat{\bar\psi}^+_a(x), \hat b^{s'\dagger}_{\mathbf q}\} = \bar v^{s'}_a(q)e^{-iq\cdot x}$, leaving $\sqrt{2E_{\mathbf k}}\,\hat a^\dagger_{\phi,\mathbf k}|0\rangle$. $\hat\phi^+(x)$ absorbs the scalar: $e^{-ik\cdot x}|0\rangle$. The index $a$ is summed: $\bar v^{s'}_a(q)u^s_a(p) = \bar v^{s'}(q)u^s(p)$.
>
> **What the derivation shows.**
> - Contracting from the inside out is the order that costs no sign; in any other order the sign is the parity of the crossings → [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-5|Theorem §C6d.3.5]].
> - With several identical fermions $F_1$ could also absorb particles $2, \dots, n$: Step 1 then has more terms → [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-3|Theorem §C6d.2.3]].

^der-c6d-2-2

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^der-c6d-2-1|Derivation §C6d.2.1]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]], [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]]

> [!theorem] Theorem §C6d.2.3: n Identical Fermion Fields on n Identical Fermions Give the n! Contractions with the Signs of the Permutations
> Let $|k_1\cdots k_n\rangle = \prod_i\sqrt{2E_i}\;\hat a^{s_1\dagger}_{\mathbf k_1}\cdots\hat a^{s_n\dagger}_{\mathbf k_n}|0\rangle$ be $n$ fermions of one Dirac field ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]; $k_i$ stands for $(\mathbf k_i, s_i)$, all different), and $\hat\psi^+_{a_j}(y_j)$, $\hat{\bar\psi}^-_{a_j}(y_j)$, $j = 1, \dots, n$, the frequency parts of [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]. Then
>
> $$
> \hat\psi^+_{a_n}(y_n)\cdots\hat\psi^+_{a_1}(y_1)\,|k_1\cdots k_n\rangle = \sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n u^{s_i}_{a_{\sigma(i)}}(k_i)\,e^{-ik_i\cdot y_{\sigma(i)}}\;|0\rangle ,
> $$
>
> $$
> \langle k_1\cdots k_n|\,\hat{\bar\psi}^-_{a_1}(y_1)\cdots\hat{\bar\psi}^-_{a_n}(y_n) = \langle0|\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n\bar u^{s_i}_{a_{\sigma(i)}}(k_i)\,e^{+ik_i\cdot y_{\sigma(i)}} ,
> $$
>
> $\sigma(i)$ the field that takes particle $i$: $n$ identical positive- (negative-) frequency fermion fields acting on $n$ identical incoming (outgoing) fermions give the sum of the $n!$ contractions, each with the **sign of its permutation**; the identity, the inside-out order of [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]], has $+$. The same holds for antifermions with $\hat{\bar\psi}^+$, $\bar v$ (incoming) and $\hat\psi^-$, $v$ (outgoing). For $n = 2$, in Yu's order of the fields (7.79):
>
> $$
> \hat\psi^+_a(x)\,\hat\psi^+_b(y)\,|k_1k_2\rangle = \bigl[u_b(k_1)u_a(k_2)\,e^{-i(k_1\cdot y + k_2\cdot x)} - u_b(k_2)u_a(k_1)\,e^{-i(k_2\cdot y + k_1\cdot x)}\bigr]|0\rangle :
> $$
>
> antisymmetric under $k_1 \leftrightarrow k_2$, the Pauli principle in the wave function ([[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]). In Yukawa theory each vertex holds one $\hat\psi$ and one $\hat{\bar\psi}$, so the $n$ fields sit at $n$ different vertices and the $n!$ terms are different contraction patterns with relative signs; at $n = 2$ they are the two diagrams of $ff \to ff$ with their relative minus sign ([[§C6d.5 Second Order#^thm-c6d-5-3|Theorem §C6d.5.3]], [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]]).
>
> *Equivalently,* the scalar case is [[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]]: the same $n!$ terms, all with $+$ (and, for fields at one point, all equal).
>
> *Model:* [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]; *applies:* free field, free states over $|0\rangle$, exact, independent of the dynamics; with $|k\rangle = \hat a^\dagger_{\mathbf k}|0\rangle$ each term carries $\prod_i(2E_i)^{-1/2}$ ([[§C6c.2 Contractions with External Particles#^cau-c6c-2-1|§C6c.2, Caution: Two normalizations of one-particle states]]).
>
> *Source: Yu §7.1.2, eqs. (7.79)–(7.80), pp. 277–278 ("这种作用对应于场算符与初态粒子的两种可能缩并"; "倒数第二、三步中第二项前面的负号体现了交换全同费米子的反对称性"), and the boxed rule p. 281 for bosons, eqs. (7.86)–(7.87) · PS §4.7, p. 117 ("there is a second, identical term from interchanging x and y" and the two contractions with $\langle\mathbf p', \mathbf k'|$) · proof written here*

^thm-c6d-2-3

> [!derivation]- Derivation
> **Step 1** (one field on $n$ fermions). $\hat\psi^+_a(y)$ contains only $\hat a$'s ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]]), and $\{\hat\psi^+_a(y), \hat a^{s\dagger}_{\mathbf k}\}$ is the $c$-number $u^s_a(k)e^{-ik\cdot y}/\sqrt{2E_{\mathbf k}}$ (Step 6 of [[§C6d.2 Contractions with External Fermions#^der-c6d-2-1|Derivation §C6d.2.1]]). Anticommute $\hat\psi^+_a(y)$ to the right through $\hat a^\dagger_1\cdots\hat a^\dagger_m$ (short for $\hat a^{s_i\dagger}_{\mathbf k_i}$): passing $\hat a^\dagger_1, \dots, \hat a^\dagger_{i-1}$ costs $(-1)^{i-1}$, and at $\hat a^\dagger_i$ the anticommutator splits off,
>
> $$
> \hat\psi^+_a(y)\,\hat a^\dagger_1\cdots\hat a^\dagger_m|0\rangle = \sum_{i=1}^m(-1)^{i-1}\{\hat\psi^+_a(y), \hat a^\dagger_i\}\;\hat a^\dagger_1\cdots\widehat{\hat a^\dagger_i}\cdots\hat a^\dagger_m|0\rangle ,
> $$
>
> the hat meaning "omitted"; the last term, $(-1)^m\hat a^\dagger_1\cdots\hat a^\dagger_m\hat\psi^+_a(y)|0\rangle$, vanishes.
>
> **Step 2** ($n$ fields). Apply $\hat\psi^+_{a_1}(y_1)$, then $\hat\psi^+_{a_2}(y_2)$, …: field $j$ takes one of the particles still present, particle $i_j$ say, with sign $(-1)^{r_j}$, $r_j$ the number of particles still present that stand before $i_j$ in the list $1, \dots, n$. After all $n$ fields every particle is taken once: a bijection, $\sigma(i_j) = j$. The total sign is $(-1)^{\sum_jr_j}$, and $\sum_jr_j$ counts the pairs $i < i'$ with $i'$ taken first, i.e. $\sigma(i') < \sigma(i)$: the number of inversions of $\sigma$. So the sign is $\operatorname{sgn}(\sigma)$, and with the normalization $\prod_i\sqrt{2E_i}$ each term is $\operatorname{sgn}(\sigma)\prod_iu^{s_i}_{a_{\sigma(i)}}(k_i)e^{-ik_i\cdot y_{\sigma(i)}}$.
>
> **Step 3** (check with the crossings). In the string $\hat\psi^+_{a_n}(y_n)\cdots\hat\psi^+_{a_1}(y_1)\hat a^\dagger_1\cdots\hat a^\dagger_n$ field $j$ sits at position $n + 1 - j$ and particle $i$ at $n + i$. Two arcs $(n + 1 - \sigma(i), n + i)$ and $(n + 1 - \sigma(i'), n + i')$ with $i < i'$ cross iff their left ends are in the same order as their right ends, i.e. iff $\sigma(i) > \sigma(i')$: crossings = inversions, $(-1)^{\#\text{crossings}} = \operatorname{sgn}(\sigma)$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], 1).
>
> **Step 4** (the bra). $\langle k_1\cdots k_n| = \prod\sqrt{2E_i}\,\langle0|\hat a_n\cdots\hat a_1$ ([[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]]). The same steps from the left: $\langle0|\hat a_n\cdots\hat a_1\,\hat{\bar\psi}^-_{a_1}(y_1)$ splits off $\{\hat a_i, \hat{\bar\psi}^-_{a_1}(y_1)\} = \bar u^{s_i}_{a_1}(k_i)e^{ik_i\cdot y_1}/\sqrt{2E_i}$ with the sign $(-1)^{\#\text{operators between}}$; positions: particle $i$ at $n + 1 - i$, field $j$ at $n + j$; arcs cross iff $\sigma(i) > \sigma(i')$ for $i < i'$, the same count.
>
> **Step 5** ($n = 2$, Yu's order). In $\hat\psi^+_a(x)\hat\psi^+_b(y)|k_1k_2\rangle$ the inner field is $\hat\psi^+_b(y)$. Step 1 for it: $\{\hat\psi^+_b(y), \hat a^\dagger_1\}\hat a^\dagger_2|0\rangle - \{\hat\psi^+_b(y), \hat a^\dagger_2\}\hat a^\dagger_1|0\rangle$ (times $\sqrt{4E_1E_2}$); then $\hat\psi^+_a(x)$ takes the remaining particle with sign $+$:
>
> $$
> u_b(k_1)e^{-ik_1\cdot y}\,u_a(k_2)e^{-ik_2\cdot x}|0\rangle - u_b(k_2)e^{-ik_2\cdot y}\,u_a(k_1)e^{-ik_1\cdot x}|0\rangle ,
> $$
>
> the statement; exchanging $k_1 \leftrightarrow k_2$ (with the spins) turns the bracket into its negative.
>
> **What the derivation shows.**
> - The sign of each attachment is fixed by the order of the operators alone; no dynamics enters → the relative sign of two diagrams, [[§C6d.5 Second Order#^thm-c6d-5-4|Theorem §C6d.5.4]].

^der-c6d-2-3

*Uses:* [[§C6d.2 Contractions with External Fermions#^def-c6d-2-1|Def. §C6d.2.1]], [[§C6d.2 Contractions with External Fermions#^def-c6d-2-2|Def. §C6d.2.2]], [[§C6d.2 Contractions with External Fermions#^der-c6d-2-1|Derivation §C6d.2.1]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^lem-c6d-3-3|Lemma §C6d.3.3]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]]

## Fermion lines as spinor chains

> [!theorem] Theorem §C6d.2.4: A Fermion Line Is a Spinor Chain
> In a diagram of [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]] every fermion line runs through vertices with one arrow in and one out ([[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]]), so it is either **open**, from an external fermion to another, or **closed**. Written **against the arrow**, starting at the end where the arrow leaves the diagram, an open line through $k$ vertices with $k - 1$ internal fermion propagators $\tilde S_F(q) = \frac{i(\slashed q + m)}{q^2 - m^2 + i\varepsilon}$ ([[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]) is the number
>
> $$
> (\text{row})\;\tilde S_F(q_{k-1})\cdots\tilde S_F(q_1)\;(\text{column}) , \qquad \text{row} \in \{\bar u(p), \bar v(p)\} , \quad \text{column} \in \{u(p), v(p)\} ,
> $$
>
> the row from the $\hat{\bar\psi}$ at the arrow's head (an outgoing particle $\bar u$ or an incoming antiparticle $\bar v$), the column from the $\hat\psi$ at its tail (an incoming particle $u$ or an outgoing antiparticle $v$), each Yukawa vertex a unit matrix. At first order the line is one of $\bar uu$, $\bar uv$, $\bar vu$, $\bar vv$. A closed line is a trace ([[§C6d.4 First Order#^thm-c6d-4-6|Theorem §C6d.4.6]]). "If you end up trying to contract things that don't contract, you made a mistake": a line that does not close into row · matrices · column has been mis-assigned.
>
> *Equivalently,* the scalar case is [[§C6c.2 Contractions with External Particles#^thm-c6c-2-4|Theorem §C6c.2.4]]: there a vertex only collects the momenta of its lines; with fermions it also joins the spinor indices along the line.
>
> *Model:* [[§C6d.1 Yukawa Theory#^mod-c6d-1-1|Model §C6d.1.1]]; *applies:* every diagram, every order (the spinor structure only; the sign of the diagram is [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^thm-c6d-3-4|Theorem §C6d.3.4]]).
>
> *Source: PHY 513 Lecture 17, transcript ("you just should, in the end of the day, have an ordinary wave function multiplied by a bar, that could end up being $u$ bar $v$ … If you end up trying to contract things that don't contract. You made a mistake") · the user's PHY 513 notes, Lecture 17 update, §17.3, paragraph "A check that cannot fail silently" · PS §4.7, p. 119, eq. (4.117) ("the Dirac indices contract together along the fermion lines") · Yu §7.1, after eq. (7.29) ("逆着费米子线上的方向逐项写出来 … 得到的是数 $\bar v(q, \lambda')u(p, \lambda)$，而非矩阵 $u(p, \lambda)\bar v(q, \lambda')$"); §7.2, p. 288 · proof written here*

^thm-c6d-2-4

> [!derivation]- Derivation
> **Step 1** (indices at a vertex). The vertex $\hat{\bar\psi}_c(z)\hat\psi_c(z)$ ([[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]]) joins the index of its incoming line (the $\hat\psi_c$ leg, arrow in) to that of its outgoing line (the $\hat{\bar\psi}_c$ leg, arrow out) by $\delta$.
>
> **Step 2** (indices of the pieces). An internal line from $\hat{\bar\psi}_b(y)$ to $\hat\psi_a(x)$ is $S_F(x - y)_{ab}$ ([[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^def-c6d-3-1|Def. §C6d.3.1]]): first index at the arrow's head, second at its tail. External contractions ([[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]]): $\hat{\bar\psi}_a$ gives a row component $\bar u_a$ or $\bar v_a$; $\hat\psi_a$ gives a column component $u_a$ or $v_a$.
>
> **Step 3** (assemble). Follow an open line against its arrow from its head: the outgoing end contributes $\bar w_{e}$ (row; $\hat{\bar\psi}_e(z_k)$ at the last vertex $z_k$); the vertex $z_k$ passes $e$ to its $\hat\psi_e(z_k)$, contracted with $\hat{\bar\psi}_d(z_{k-1})$: $S_F(z_k - z_{k-1})_{ed}$; and so on down to the first vertex $z_1$, whose $\hat\psi_c(z_1)$ meets the incoming end, $w'_c$ (column). Summing over repeated indices,
>
> $$
> \bar w_e\,S_F(z_k - z_{k-1})_{ed}\cdots S_F(z_2 - z_1)_{\cdot c}\,w'_c = \bar w\,S_F\cdots S_F\,w' ,
> $$
>
> a row times $4\times4$ matrices times a column: a number. In momentum space each $S_F$ becomes $\tilde S_F(q)$ with $q$ along the arrow ([[§C6d.6 Momentum-Space Feynman Rules#^rem-c6d-6-1|§C6d.6, Remark: The direction of momentum on fermion lines]]).
>
> **Step 4** (the four first-order chains). At $k = 1$ there are no propagators: row $\in \{\bar u, \bar v\}$, column $\in \{u, v\}$, four products.
>
> **What the derivation shows.**
> - Written along the arrow instead, the same factors would form the $4\times4$ matrix $w'\bar w$, not a number (Yu: "而非矩阵 $u\bar v$"): the reading direction is forced by the index structure.

^der-c6d-2-4

*Uses:* [[§C6d.1 Yukawa Theory#^thm-c6d-1-3|Theorem §C6d.1.3]], [[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]], [[§C6d.3 Wick's Theorem with Fermions and the Contraction Rule#^def-c6d-3-1|Def. §C6d.3.1]], [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-1|Theorem §C6d.2.1]], [[§C5b.8 Green's Functions and the Dirac Feynman Propagator#^thm-c5b-8-3|Theorem §C5b.8.3]]

*Procedure:* [[P6 Tree Amplitude from a Lagrangian#^p6-4|P6, step 4]]

> [!remark] Remark: Charge arrow and momentum arrow
> The fermion arrow on an external line is redundant given the spinor and the momentum: a $\bar v$ must be an incoming antiparticle. The redundancy is useful: it makes every vertex "one arrow in, one out" ([[§C6d.1 Yukawa Theory#^thm-c6d-1-5|Theorem §C6d.1.5]]). An antiparticle going out carries anticharge out, "which is like a charge coming in". So one diagram, a scalar line and two fermion lines with arrows pointing away and towards a vertex, can mean "a scalar comes in and creates a particle and an antiparticle", and only the momentum arrows say which way the particles move; drawing both arrows on antiparticle lines removes the doubt (slide 12; PS p. 119).
>
> *Source: PHY 513 Lecture 17, slide 12, and transcript (about 39–42 min) · the user's PHY 513 notes, Lecture 17 update, §17.3, paragraph "The arrows, again" · PS §4.7, p. 119 ("For external antiparticles, however, the momentum flows opposite to the arrow; it helps to show this explicitly by drawing a second arrow next to the line")*

^rem-c6d-2-1

> [!abstract]- Mathematical background
> Proved in CA; each line says what the physics above relies on.
>
> - [[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]] — $\sqrt{2E_{\mathbf p}}/\sqrt{2E_{\mathbf q}}$ may be evaluated on the support of $\delta^3(\mathbf q - \mathbf p)$.
> - [[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]] — the plane waves of external lines become momentum deltas at the vertices, leaving the spinors.

> [!remark]- Connections
> - The scalar's external line "$1$" is the same contraction with no spinor: $\hat\phi^+|\mathbf p\rangle = e^{-ip\cdot x}|0\rangle$ — [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]]; for photons the leftover is a polarization vector (C6d, QED rules (planned); PS §4.8).
> - The one-particle wave functions of the free Dirac field are the external factors: $\langle0|\hat\psi|\mathbf p, s\rangle = u^se^{-ip\cdot x}$, $\langle0|\hat{\bar\psi}|\mathbf p, s\rangle^c = \bar v^se^{-ip\cdot x}$ — [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-3|Theorem §C5b.6.3]].
> - Which spinor is a row and which a column is the statement that $\hat{\bar\psi}$ is $\hat\psi$ with particles and antiparticles exchanged, made explicit by charge conjugation — [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-2|§C5b.2, Remark: ψ̄ is ψ with particles and antiparticles interchanged]], [[§C9.7 Charge Conjugation on the Field and Bilinears|§C9.7]].
> - Squared and summed over spins, a chain becomes a trace of $(\slashed p \pm m)$'s: the spin sums turn $|\bar uv|^2$ into $\operatorname{tr}[(\slashed p + m)(\slashed q - m)]$ (Yu (7.46)–(7.47)) — [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-7|Theorem §C5a.12.7]], [[§C5a.12 Normalization and Spin Sums#^thm-c5a-12-8|Theorem §C5a.12.8]], [[§C5a.14 Gamma-Matrix Technology|§C5a.14]].
> - Several fields on one state contract from the inside out without sign; for scalars the order does not matter at all — [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-2|Theorem §C6d.2.2]], [[§C6c.2 Contractions with External Particles#^lem-c6c-2-2|Lemma §C6c.2.2]].
> - The $n!$ contractions of identical fermions carry $\operatorname{sgn}\sigma$: the Pauli principle of the states seen from the fields; for bosons all signs are $+$ — [[§C6d.2 Contractions with External Fermions#^thm-c6d-2-3|Theorem §C6d.2.3]], [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-2|Theorem §C5b.4.2]], [[§C6c.2 Contractions with External Particles#^thm-c6c-2-3|Theorem §C6c.2.3]].
