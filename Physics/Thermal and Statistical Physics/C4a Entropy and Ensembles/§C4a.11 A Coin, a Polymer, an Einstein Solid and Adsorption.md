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
> 1. **One toss.**
>
> | outcome | $p$ | surprisal $I$ (bits) |
> | --- | --- | --- |
> | $H$ | $\tfrac34$ | $\log_2\tfrac43 \simeq 0.415$ |
> | $T$ | $\tfrac14$ | $2$ |
>
> $H = \langle I\rangle = 2 - \tfrac34\log_23 \simeq 0.811$ bits, below $H(\tfrac12, \tfrac12) = 1$ ([[§C4a.1 Shannon Entropy#^def-c4a-1-3|Def. §C4a.1.3]], [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|Theorem §C4a.1.2]]).
> 2. **Pairs.** $p(HH, HT, TH, TT) = (\tfrac9{16}, \tfrac3{16}, \tfrac3{16}, \tfrac1{16})$ and $H_2 = 4 - \tfrac32\log_23 = 2H$: for independent tosses the surprisals add ([[§C4a.1 Shannon Entropy#^def-c4a-1-3|Def. §C4a.1.3]] (2)), hence so do their means.
> 3. **A pair code.** $HH \mapsto 0$, $HT \mapsto 10$, $TH \mapsto 110$, $TT \mapsto 111$ (prefix-free). Example: $01001101110 = 0\,|\,10\,|\,0\,|\,110\,|\,111\,|\,0 = HH\,HT\,HH\,TH\,TT\,HH$.
> 4. **Length.** $\langle\ell_2\rangle = \tfrac9{16}(1) + \tfrac3{16}(2) + \tfrac3{16}(3) + \tfrac1{16}(3) = \tfrac{27}{16}$ per pair, i.e. $0.844$ per toss. Check against [[§C4a.1 Shannon Entropy#^thm-c4a-1-3|Theorem §C4a.1.3]] with $k = 2$: $2H \simeq 1.623 \le 1.6875 < 2H + 1$; longer blocks bring the per-toss length down to $H$.
>
> *Source: PHY 510 Problem Set 4, Problem 2, official solution*

^ex-c4a-11-1

> [!example] Example §C4a.11.2: Entropic Elasticity of a Chain
> $L$ distinguishable links of length $a$ on a line, $s_j = \pm1$; microstate $i = (s_1, \dots, s_L)$, energy $0$, displacement $X_i = a\sum_js_j$. Write $h(r) = -r\ln r - (1 - r)\ln(1 - r)$.
>
> 1. **MaxEnt at prescribed $\bar X$** ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]). $p_i^\ast = e^{-\eta X_i}/Z$, and $e^{-\eta X_i} = \prod_je^{-\eta as_j}$ gives $Z = [2\cosh(\eta a)]^L$ and $p_i^\ast = \prod_jq(s_j)$, $q(s) = e^{-\eta as}/[2\cosh(\eta a)]$: a product of one-link distributions, so the links are independent.
> 2. **$\bar X$ and $\eta$.** $\bar X = -\partial_\eta\ln Z = -La\tanh(\eta a) = La[q(+1) - q(-1)]$, inverted as $\eta = -\frac1a\operatorname{artanh}\frac{\bar X}{La} = \frac1{2a}\ln\frac{La - \bar X}{La + \bar X}$: odd, decreasing, $\eta \to \mp\infty$ as $\bar X \to \pm La$.
> 3. **Force.** The problem set takes $F = U - TS = -k_BTH_{\max}$ at prescribed $\bar X$ (here $U = 0$) as the free energy; with $\partial H_{\max}/\partial\bar X = \eta$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]]), $f = (\partial F/\partial\bar X)_T = -k_BT\eta$. Small extensions: $f \simeq k_BT\bar X/(La^2)$, a purely entropic spring. Since $e^{-\eta X_i} = e^{fX_i/k_BT}$, the MaxEnt state is the constant-force ensemble.
> 4. **Prescribed mean versus fixed ends.**
>
> | | prescribed mean $\bar X$ (MaxEnt) | fixed $X$ (microcanonical) |
> | --- | --- | --- |
> | allowed lists | all $2^L$ | $L_\pm = (L \pm X/a)/2$ links each way |
> | weights | $\prod_jq(s_j)$ | $1/\Omega(X)$, $\Omega(X) = L!/(L_+!L_-!)$ |
> | entropy$/k_B$ | $H_{\max} = L\,h(q(+1)) = L\{\ln[2\cosh(\eta a)] - \eta a\tanh(\eta a)\} = \ln Z + \eta\bar X$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]]) | $\ln\Omega(X) \simeq L\,h(r)$, $r = L_+/L$ (Stirling) |
> | $\operatorname{Var}(X)$ | $La^2\operatorname{sech}^2(\eta a) = La^2[1 - (\bar X/La)^2] = k_BT(\partial\bar X/\partial f)_T$ ([[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]]) | $0$ |
>
> 5. **Comparison.** At $X = \bar X$ one has $r = q(+1)$, so the entropies agree at leading order in $L$. They are not equal: at $X = 0$, $\binom{L}{L/2}$ is a single term of $\sum_k\binom Lk = 2^L$, so $\ln\binom{L}{L/2} < L\ln2 = H_{\max}(0)$.
>
> *Source: PHY 510 Problem Set 5, Problems 1 and 2(a), official solution*

^ex-c4a-11-2

![[ph-th-c4a-11-1.svg]]

*Figure: force needed to hold the chain of [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-2|Example §C4a.11.2]] at mean extension $\bar X$, $fa/k_BT = \operatorname{artanh}(\bar X/La)$, against its linear spring approximation. Near $\bar X = \pm La$ only a few conformations remain, and the force needed grows without bound.*

> [!example] Example §C4a.11.3: The Einstein Solid in a Heat Bath
> $3N$ oscillators labelled by site and direction, frequency $\omega$, $E_n = \hbar\omega(n + \tfrac12)$, $x = \hbar\omega/k_BT = \theta_E/T$.
>
> 1. **$Z$.** $z = \sum_ne^{-x(n+1/2)} = e^{-x/2}/(1 - e^{-x})$ and $Z = z^{3N}$; labelled oscillators give a plain product, with no $1/N!$ (counting as in [[§C2.5 Two-State Units, Free Expansion and Oscillators#^ex-c2-5-4|Example §C2.5.4]]).
> 2. **$F$, $U$.** $F = 3N[\tfrac{\hbar\omega}{2} + k_BT\ln(1 - e^{-x})]$, $U = \tfrac32N\hbar\omega + \frac{3N\hbar\omega}{e^x - 1}$ (zero-point plus thermal).
> 3. **$C_V$ from the variance** ([[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-2|Theorem §C4a.10.2]]). $\operatorname{Var}(E) = \partial_\beta^2\ln Z = 3N(\hbar\omega)^2\frac{e^x}{(e^x - 1)^2}$, so $C_V = \operatorname{Var}(E)/k_BT^2 = 3Nk_B\frac{x^2e^x}{(e^x - 1)^2}$. The zero-point part of $\ln Z$, $-\tfrac32N\beta\hbar\omega$, is linear in $\beta$, so it drops out of both.
> 4. **Limits.**
>
> | | $C_V$ | |
> | --- | --- | --- |
> | $x \to 0$ (high $T$) | $3Nk_B[1 - x^2/12 + O(x^4)] \to 3Nk_B$ | equipartition |
> | $x \to \infty$ (low $T$) | $3Nk_B(\theta_E/T)^2e^{-\theta_E/T}$ | activated across $\hbar\omega$ |
>
> and $S = 3Nk_B[\frac{x}{e^x - 1} - \ln(1 - e^{-x})] \to 0$ as $T \to 0$.
>
> *Model:* Einstein solid, one frequency; the activated low-$T$ law comes from that single gap.
>
> *Source: PHY 510 Problem Set 5, Problem 3, official solution · level-B home: [[§B8.2 Equipartition and the Heat Capacities of Molecules#^thm-b8-2-7|Theorem §B8.2.7]]*

^ex-c4a-11-3

> [!example] Example §C4a.11.4: Adsorption on Independent Sites
> $M$ distinguishable sites, each empty (energy $0$) or singly occupied (energy $-\epsilon$); reservoir at $T$, $\mu$; $y = e^{\beta(\mu + \epsilon)}$.
>
> 1. **$\Xi$.** Sites are independent, so $\Xi = \xi^M$ with $\xi = 1 + y$, and $\Phi = -Mk_BT\ln(1 + y)$ ([[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]], [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-3|Theorem §C4a.6.3]]).
> 2. **Coverage.** $\vartheta = \bar N/M = y/(1 + y) = 1/(1 + e^{-\beta(\mu + \epsilon)})$.
> 3. **Distribution of $N$.** Each site is filled independently with probability $\vartheta$, so $P(N) = \binom MN\vartheta^N(1 - \vartheta)^{M-N}$, the binomial factor choosing the filled sites.
> 4. **Regimes.**
>
> | $\mu + \epsilon$ | $\vartheta$ |
> | --- | --- |
> | $\ll -k_BT$ | $\simeq e^{\beta(\mu + \epsilon)}$ (dilute) |
> | $0$ | $\tfrac12$ |
> | $\gg k_BT$ | $\to 1$ |
>
> *Source: PHY 510 Problem Set 5, Problem 4, official solution · level-B home: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-5|Theorem §B7.3.5]]*

^ex-c4a-11-4

> [!remark]- Connections
> - The coverage formula has the Fermi–Dirac form: one site is one orbital that holds at most one particle — [[§C4b.2 One Orbital in the Grand Ensemble#^thm-c4b-2-1|Theorem §C4b.2.1]]; level B: [[§B7.3 The Grand Canonical Ensemble#^rem-b7-3-3|Remark: The Fermi–Dirac shape]].
> - The entropic spring returns in polymer physics and in rubber — [[§B3.4★ Rods, Bubbles and Magnets#^ex-b3-4-1|Example §B3.4.1]].
