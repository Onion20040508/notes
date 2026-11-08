---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.11
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.10 Ensembles at a Glance and Fluctuations]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4b.1 Orbitals and Occupations]] →

*Sources: PHY 510 Problem Set 4, Problem 2, and Problem Set 5, Problems 1, 3, 4, with official solutions (Mao, Fall 2026).*

*MaxEnt chain:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] → [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]] → [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-2|Example §C4a.11.2]]. *Oscillator chain:* [[§C2.5 Two-State Units, Free Expansion and Oscillators#^ex-c2-5-4|Example §C2.5.4]] → [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-3|Example §C4a.11.3]].

The chapter's tools on four small systems: a biased coin coded in pairs, a polymer whose elasticity is pure entropy, the Einstein solid in a heat bath, and adsorption on independent sites from a particle reservoir.

**Setup.** Natural logarithms except in [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-1|Example §C4a.11.1]], which uses bits.

> [!example] Example §C4a.11.1: A Biased Coin, Coded in Pairs
> A coin gives heads with probability $\tfrac34$, tosses independent.
>
> 1. Surprisals: $I_H = \log_2\tfrac43 \simeq 0.415$ bits, $I_T = 2$ bits; entropy $H = \tfrac34\log_2\tfrac43 + \tfrac14(2) = 2 - \tfrac34\log_23 \simeq 0.811$ bits per toss, less than the fair coin's $1$ because heads is predictable ([[§C4a.1 Shannon Entropy#^def-c4a-1-3|Def. §C4a.1.3]]).
> 2. Pairs $HH, HT, TH, TT$ have probabilities $\tfrac9{16}, \tfrac3{16}, \tfrac3{16}, \tfrac1{16}$ and entropy $H_2 = 4 - \tfrac32\log_23 = 2H$: the second toss carries $H$ again whatever the first was (grouping, [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]]).
> 3. The prefix code $HH = 0$, $HT = 10$, $TH = 110$, $TT = 111$ decodes $01001101110$ as $0\,|\,10\,|\,0\,|\,110\,|\,111\,|\,0$, that is $HH\,HT\,HH\,TH\,TT\,HH$. Its mean length is $\tfrac9{16}(1) + \tfrac3{16}(2) + \tfrac3{16}(3) + \tfrac1{16}(3) = \tfrac{27}{16}$ digits per pair, $0.844$ per toss: below $1$, above $H \simeq 0.811$, and longer blocks approach $H$ ([[§C4a.1 Shannon Entropy#^thm-c4a-1-3|Theorem §C4a.1.3]]).
>
> *Source: PHY 510 Problem Set 4, Problem 2, official solution*

^ex-c4a-11-1

> [!example] Example §C4a.11.2: Entropic Elasticity of a Chain
> A one-dimensional chain of $L$ distinguishable links of length $a$, each pointing right ($s_j = +1$) or left ($s_j = -1$), all conformations of energy zero; a microstate is the whole list $(s_1, \dots, s_L)$, with displacement $X_i = a\sum_js_j$.
>
> 1. **MaxEnt with prescribed $\bar X$** ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]): $p_i^\ast = e^{-\eta X_i}/Z$ with $Z = [2\cosh(\eta a)]^L$. The weight factorizes, $p_i^\ast = \prod_jq(s_j)$ with $q(s) = e^{-\eta as}/[2\cosh(\eta a)]$, so the links are independent.
> 2. **Mean and multiplier.** $\bar X = -\partial_\eta\ln Z = -La\tanh(\eta a)$, also $La[q(+1) - q(-1)]$. Inverting, $\eta = -\frac1a\operatorname{artanh}\frac{\bar X}{La} = \frac1{2a}\ln\frac{La - \bar X}{La + \bar X}$, odd, decreasing, $\pm\infty$ at full extension.
> 3. **Force.** In a bath at $T$, $U = 0$, so $F = -k_BTH_{\max}$, and the applied force holding the mean extension is $f = (\partial F/\partial\bar X)_T = -k_BT\eta$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]]). For $|\bar X| \ll La$, $f \simeq \frac{k_BT}{La^2}\bar X$: a spring of stiffness $k_BT/(La^2)$, entirely entropic. The MaxEnt distribution is a constant-force ensemble, with weight $e^{fX_i/k_BT} = e^{-\eta X_i}$.
> 4. **Entropy.** $H_{\max} = L\{\ln[2\cosh(\eta a)] - \eta a\tanh(\eta a)\} = \ln Z + \eta\bar X$, exactly ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]]).
> 5. **Fixed ends instead.** If every conformation has $X_i = X$, the accessible set is the lists with $L_\pm = (L \pm X/a)/2$, $\Omega(X) = L!/(L_+!L_-!)$, and $S_{\text{mc}}/k_B \simeq -L[r\ln r + (1 - r)\ln(1 - r)]$ with $r = L_+/L$. At $X = \bar X$, $r = q(+1)$, so $S_{\text{mc}} \simeq k_BH_{\max}$ at leading order but not exactly: at zero extension $\ln\binom{L}{L/2} < L\ln2$. Fixing $X$ is not fixing only its mean.
> 6. **Fluctuations** ([[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]]): $\operatorname{Var}(X) = La^2\operatorname{sech}^2(\eta a) = La^2[1 - (\bar X/La)^2] = k_BT(\partial\bar X/\partial f)_T$.
>
> *Source: PHY 510 Problem Set 5, Problems 1 and 2(a), official solution*

^ex-c4a-11-2

![[ph-th-c4a-11-1.svg]]

*Figure: force needed to hold the chain of [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-2|Example §C4a.11.2]] at mean extension $\bar X$, $fa/k_BT = \operatorname{artanh}(\bar X/La)$, against its linear spring approximation. The force diverges at full extension, where no conformations are left to give up.*

> [!example] Example §C4a.11.3: The Einstein Solid in a Heat Bath
> $3N$ independent distinguishable oscillators of frequency $\omega$, $E_n = \hbar\omega(n + \tfrac12)$, $x = \hbar\omega/k_BT = \theta_E/T$.
>
> 1. $z = \sum_ne^{-x(n+1/2)} = e^{-x/2}/(1 - e^{-x})$ and $Z = z^{3N}$, with no $1/N!$: the oscillators are labelled by site and direction, so exchanging excitations makes a different state.
> 2. $F = 3N[\tfrac{\hbar\omega}{2} + k_BT\ln(1 - e^{-x})]$, $U = \tfrac32N\hbar\omega + \frac{3N\hbar\omega}{e^x - 1}$ (zero-point plus thermal), $C_V = 3Nk_B\frac{x^2e^x}{(e^x - 1)^2}$.
> 3. High $T$: $C_V = 3Nk_B[1 - x^2/12 + O(x^4)] \to 3Nk_B$, equipartition. Low $T$: $C_V \simeq 3Nk_B(\theta_E/T)^2e^{-\theta_E/T}$, exponentially small across the gap $\hbar\omega$. $S = 3Nk_B[\frac{x}{e^x - 1} - \ln(1 - e^{-x})] \to 0$ as $T \to 0$.
> 4. $\operatorname{Var}(E) = 3N(\hbar\omega)^2\frac{e^x}{(e^x - 1)^2}$ ([[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-2|Theorem §C4a.10.2]]); the zero-point energy is a constant and contributes to neither $C_V$ nor $\operatorname{Var}(E)$.
>
> *Model:* Einstein solid; the low-temperature form is a property of this model's single gap.
>
> *Source: PHY 510 Problem Set 5, Problem 3, official solution · level-B home: [[§B8.2 Equipartition and the Heat Capacities of Molecules#^thm-b8-2-7|Theorem §B8.2.7]]*

^ex-c4a-11-3

> [!example] Example §C4a.11.4: Adsorption on Independent Sites
> $M$ distinguishable sites, each empty (energy $0$) or holding one molecule (energy $-\epsilon$), in contact with a reservoir at $T$, $\mu$. With $y = e^{\beta(\mu + \epsilon)}$:
>
> 1. $\xi = 1 + y$ per site, $\Xi = (1 + y)^M$, $\Phi = -Mk_BT\ln(1 + y)$ ([[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]], [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-3|Theorem §C4a.6.3]]).
> 2. Coverage $\vartheta = \bar N/M = \frac{1}{1 + e^{-\beta(\mu + \epsilon)}}$, and $P(N) = \binom MN\vartheta^N(1 - \vartheta)^{M-N}$, counting the $\binom MN$ occupied subsets.
> 3. Half coverage at $\mu = -\epsilon$; full coverage for $\mu + \epsilon \gg k_BT$; nearly empty, $\vartheta \simeq e^{\beta(\mu + \epsilon)}$, for $\mu + \epsilon \ll -k_BT$.
>
> *Source: PHY 510 Problem Set 5, Problem 4, official solution · level-B home: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-5|Theorem §B7.3.5]]*

^ex-c4a-11-4

> [!remark]- Connections
> - The coverage formula has the Fermi–Dirac form: one site is one orbital that holds at most one particle — Mao §4.5.3 (level C to come); level B: [[§B7.3 The Grand Canonical Ensemble#^rem-b7-3-3|Remark: The Fermi–Dirac shape]].
> - The entropic spring returns in polymer physics and in rubber — [[§B3.4★ Rods, Bubbles and Magnets#^ex-b3-4-1|Example §B3.4.1]].
