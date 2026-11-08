---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.10
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.9★ Density of States, Laplace and Legendre]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption]] →

*Sources: Mao, PHY 510 notes, §4.4.4, eqs. (4.89)–(4.92), the summary table and box "How conjugacy, means, and fluctuations fit together" · PHY 510 Problem Set 5, Problem 2, official solution · PHY 510 Lecture 10/6.*

An ensemble is specified by two lists: the quantities that take one value in all of its microstates (restrictions), and those that only have a prescribed average. An averaged quantity can be specified by its mean, as MaxEnt input, or by its multiplier, as set by a reservoir; the two are conjugate ([[§C4a.6 Massieu Functions and Thermodynamic Potentials|§C4a.6]]). Below, the three ensembles side by side, and the identity that turns fluctuations into responses: a variance is the derivative of a mean with respect to its conjugate. Level B has the canonical and grand-canonical fluctuation formulas ([[§B7.2 Free Energy from the Partition Function#^thm-b7-2-4|Theorem §B7.2.4]], [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-2|Theorem §B7.3.2]]).

**Setup.** $U = \langle E\rangle$, $\bar N = \langle N\rangle$, $\delta E = E - U$, $\delta N = N - \bar N$, $\eta_N = -\beta\mu$. In derivatives of $\ln Z$, $V$ and $N$ are fixed; in derivatives of $\ln\Xi(\beta, \eta_N, V)$, the other multiplier and $V$ are fixed. Energy levels do not depend on the multipliers.

> [!example] Example §C4a.10.1: The Three Ensembles at a Glance
> | ensemble (situation) | control variables | weight $p_i$ | generating function, potential | means; conjugate pairs | fluctuating; second moments |
> | --- | --- | --- | --- | --- | --- |
> | microcanonical (isolated, given $E$, $N$) | $E, V, N$ | $1/\Omega$ in the shell | $\ln\Omega$; $S_{\text{mc}} = k_B\ln\Omega$ | $U = E$, $\bar N = N$; restrictions only, no pairs | neither $E$ nor $N$: $\operatorname{Var}E = \operatorname{Var}N = \operatorname{Cov}(E, N) = 0$ |
> | canonical (heat exchange, fixed $N$) | $T, V, N$ | $e^{-\beta E_i}/Z$ | $\ln Z$; $F = -k_BT\ln Z$ | $U = -\partial_\beta\ln Z$, $\bar N = N$; $U \leftrightarrow \beta$ | $E$: $\operatorname{Var}E = \partial_\beta^2\ln Z = k_BT^2C_V$; $\operatorname{Var}N = \operatorname{Cov} = 0$ |
> | grand canonical (heat and particle exchange; independent orbitals) | $T, V, \mu$ | $e^{-\beta E_i - \eta_NN_i}/\Xi$ | $\ln\Xi$; $\Phi = -k_BT\ln\Xi$ | $U = -\partial_\beta\ln\Xi$, $\bar N = -\partial_{\eta_N}\ln\Xi$; $U \leftrightarrow \beta$, $\bar N \leftrightarrow \eta_N$ | $E$ and $N$, in general correlated: $\partial_\beta^2\ln\Xi$, $\partial_{\eta_N}^2\ln\Xi$, $\partial_\beta\partial_{\eta_N}\ln\Xi$ |
>
> The zeros in the first row idealize the shell as sharp; a shell of width $\Delta E$ allows $\operatorname{Var}E \le \Delta E^2/4$. Observables other than $E$ and $N$ fluctuate in every row.
>
> *Source: Mao §4.4.4, eq. (4.89) and table*

^ex-c4a-10-1

> [!theorem] Theorem §C4a.10.1: Fluctuations Are Second Derivatives of $\ln Z$
> For $p_i = Z^{-1}\exp[-\sum_\alpha\eta_\alpha A_\alpha(i)]$,
>
> $$
> \eta_\alpha = \frac{\partial H_{\max}}{\partial\bar A_\alpha}, \qquad \bar A_\alpha = -\frac{\partial\ln Z}{\partial\eta_\alpha}, \qquad \operatorname{Cov}(A_\alpha, A_\gamma) = \frac{\partial^2\ln Z}{\partial\eta_\alpha\partial\eta_\gamma} = -\frac{\partial\bar A_\alpha}{\partial\eta_\gamma} .
> $$
>
> Implicit subscripts: $\partial/\partial\bar A_\alpha$ at fixed $\bar A_{\gamma\neq\alpha}$; $\partial/\partial\eta_\alpha$ at fixed $\eta_{\gamma\neq\alpha}$.
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]; *applies:* exact.
>
> *Source: Mao §4.4.4, box "How conjugacy, means, and fluctuations fit together", eq. (4.90) · PHY 510 Problem Set 5, Problem 2(a), official solution*

^thm-c4a-10-1

> [!derivation]- Derivation
> **Step 1.** $\partial_{\eta_\gamma}p_i = -[A_\gamma(i) - \bar A_\gamma]p_i$: differentiating the exponent gives $-A_\gamma(i)p_i$ and differentiating $1/Z$ gives $+\bar A_\gamma p_i$ ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]).
>
> **Step 2.** $\partial_{\eta_\gamma}\bar A_\alpha = \sum_iA_\alpha(i)\partial_{\eta_\gamma}p_i = -\sum_iA_\alpha(i)[A_\gamma(i) - \bar A_\gamma]p_i = -\operatorname{Cov}(A_\alpha, A_\gamma)$.
>
> **Step 3.** $\bar A_\alpha = -\partial_{\eta_\alpha}\ln Z$, so $\partial^2_{\eta_\alpha\eta_\gamma}\ln Z = -\partial_{\eta_\gamma}\bar A_\alpha = \operatorname{Cov}(A_\alpha, A_\gamma)$. The first relation is [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]].

^der-c4a-10-1

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]]

> [!theorem] Theorem §C4a.10.2: Canonical Energy Fluctuations
> $$
> \operatorname{Var}(E) = \frac{\partial^2\ln Z}{\partial\beta^2} = k_BT^2C_V, \qquad C_V = \Bigl(\frac{\partial U}{\partial T}\Bigr)_{V,N} \ge 0 .
> $$
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]], levels $E_i$ independent of $T$; *applies:* $C_V \ge 0$ is derived here from $\operatorname{Var}E \ge 0$, so it is a statement about canonical states.
>
> *Source: Mao §4.4.4, table · PHY 510 Problem Set 5, Problem 2(b), official solution · level-B home: [[§B7.2 Free Energy from the Partition Function#^thm-b7-2-4|Theorem §B7.2.4]]*

^thm-c4a-10-2

> [!derivation]- Derivation
> [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]] with $\eta = \beta$, $A = E$: $\operatorname{Var}(E) = \partial_\beta^2\ln Z = -\partial_\beta U$. Since $d\beta/dT = -1/(k_BT^2)$, $-\partial_\beta U = k_BT^2\partial_TU = k_BT^2C_V$, and a variance is nonnegative.

^der-c4a-10-2

*Uses:* [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]]

> [!theorem] Theorem §C4a.10.3: Grand-Canonical Fluctuations as Responses
> Changing from $\eta_N$ to $\mu$ at fixed $T$ ($\eta_N = -\beta\mu$),
>
> $$
> \bar N = k_BT\Bigl(\frac{\partial\ln\Xi}{\partial\mu}\Bigr)_{T,V}, \qquad \operatorname{Var}(N) = k_BT\Bigl(\frac{\partial\bar N}{\partial\mu}\Bigr)_{T,V}, \qquad \operatorname{Cov}(E, N) = k_BT\Bigl(\frac{\partial U}{\partial\mu}\Bigr)_{T,V} .
> $$
>
> At fixed $\mu$ instead of fixed $\eta_N$, the $\beta$-derivatives change meaning:
>
> $$
> -\Bigl(\frac{\partial\ln\Xi}{\partial\beta}\Bigr)_{\mu,V} = U - \mu\bar N, \qquad \Bigl(\frac{\partial^2\ln\Xi}{\partial\beta^2}\Bigr)_{\mu,V} = \operatorname{Var}(E - \mu N) .
> $$
>
> In the grand ensemble $\operatorname{Var}(E) = -(\partial U/\partial\beta)_{\eta_N,V}$, which in general $\neq k_BT^2C_V$ (that is a fixed-$N$ derivative). One homogeneous phase: $\operatorname{Var}(N) = k_BT\bar N^2\kappa_T/V$ with $\kappa_T$ the isothermal compressibility, so $\kappa_T \ge 0$.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]; *applies:* levels independent of $\mu$, $T$; the $\kappa_T$ form in the thermodynamic limit.
>
> *Source: Mao §4.4.4, eqs. (4.91)–(4.92) · PHY 510 Problem Set 5, Problem 2(c), official solution · level-B home: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-2|Theorem §B7.3.2]]*

^thm-c4a-10-3

> [!derivation]- Derivation
> **Step 1** (fixed $\beta$). With $\eta_N = -\beta\mu$, $(\partial/\partial\mu)_\beta = -\beta\,\partial/\partial\eta_N$. Apply this to [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]] with $(\eta_E, \eta_N) = (\beta, \eta_N)$:
>
> $$
> \bar N = -\partial_{\eta_N}\ln\Xi = \tfrac1\beta\partial_\mu\ln\Xi, \qquad \operatorname{Var}(N) = -\partial_{\eta_N}\bar N = \tfrac1\beta\partial_\mu\bar N, \qquad \operatorname{Cov}(E, N) = -\partial_{\eta_N}U = \tfrac1\beta\partial_\mu U .
> $$
>
> **Step 2** (fixed $\mu$). Now $(\partial/\partial\beta)_\mu = (\partial/\partial\beta)_{\eta_N} - \mu\,\partial/\partial\eta_N$, since $(\partial\eta_N/\partial\beta)_\mu = -\mu$. Hence $-(\partial_\beta\ln\Xi)_\mu = U - \mu\bar N$, and, $\mu$ being constant, $(\partial_\beta^2\ln\Xi)_\mu = \operatorname{Var}E - 2\mu\operatorname{Cov}(E, N) + \mu^2\operatorname{Var}N = \operatorname{Var}(E - \mu N)$ by [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]].
>
> **Step 3** ($\kappa_T$). At fixed $T$, $dp = n\,d\mu$ (Gibbs–Duhem, [[§B3.3 Chemical Potential and Conditions for Equilibrium#^thm-b3-3-3|Theorem §B3.3.3]]) with $n = \bar N/V$, so $(\partial n/\partial\mu)_T = (\partial n/\partial p)_T\,n = n^2\kappa_T$, and $\operatorname{Var}(N) = k_BTV(\partial n/\partial\mu)_T = k_BTVn^2\kappa_T$.

^der-c4a-10-3

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]], [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]], [[§B3.3 Chemical Potential and Conditions for Equilibrium#^thm-b3-3-3|Theorem §B3.3.3]]

> [!example] Example §C4a.10.2: How Small Are Relative Fluctuations?
> For a classical monatomic ideal gas, $U = \tfrac32Nk_BT$, $C_V = \tfrac32Nk_B$, $\kappa_T = 1/(nk_BT)$. Then
>
> $$
> \frac{\sqrt{\operatorname{Var}(E)}}{U} = \sqrt{\frac{2}{3N}}, \qquad \operatorname{Var}(N) = \bar N, \qquad \frac{\sqrt{\operatorname{Var}(N)}}{\bar N} = \frac{1}{\sqrt{\bar N}} .
> $$
>
> - $N = 10^{23}$: $\sqrt{2/3N} \simeq 2.6\times10^{-12}$, $1/\sqrt N \simeq 3.2\times10^{-12}$.
> - Scaling: mean $\propto N$ and variance $\propto N$, so $\sigma/\text{mean} = O(N^{-1/2})$ — level B's [[§B7.2 Free Energy from the Partition Function#^rem-b7-2-3|Remark: How small the fluctuations are]].
>
> *Source: PHY 510 Problem Set 5, Problem 2(d), official solution · level B: [[§B7.2 Free Energy from the Partition Function#^rem-b7-2-3|Remark: How small the fluctuations are]]*

^ex-c4a-10-2

> [!remark] Remark: Slopes in the two descriptions
> | | $S_{\text{eq}}(U, \bar N)$ (MaxEnt) | $S_{\text{mc}}(E, N)$ (one shell) |
> | --- | --- | --- |
> | the argument is | a prescribed mean of one ensemble | the label of the shell |
> | a derivative compares | two ensembles with nearby means | two neighbouring shells |
> | slopes | $\partial_US_{\text{eq}} = 1/T$, $\partial_{\bar N}S_{\text{eq}} = -\mu/T$ | $\partial_ES_{\text{mc}} = 1/T$, $\partial_NS_{\text{mc}} = -\mu/T$ |
>
> The microcanonical slopes take these values at the selected $E^\ast$ (and $N^\ast$): that is the stationarity condition of [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-4|Theorem §C4a.9.4]], [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-5|Theorem §C4a.9.5]].

^rem-c4a-10-1

> [!remark]- Connections
> - Fluctuations measure responses: this is the static case of the fluctuation–dissipation relations of Unit 2 — [[§C6.6 Frequency-Dependent Response#^thm-c6-6-5|Theorem §C6.6.5]].
> - Level B's discussion of how small canonical fluctuations are — [[§B7.2 Free Energy from the Partition Function#^rem-b7-2-3|Remark: How small the fluctuations are]].
