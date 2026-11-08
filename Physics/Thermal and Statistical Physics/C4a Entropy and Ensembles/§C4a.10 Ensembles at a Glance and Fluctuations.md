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

The choice of ensemble says which quantities are fixed in every microstate and which may vary across the ensemble. The same distributions can be specified either by prescribed means (MaxEnt) or by the conjugate variables a reservoir imposes. This section collects the three ensembles and adds the relation that makes fluctuations useful: the variance of a fluctuating quantity is the response of its mean to its conjugate variable. Level B has the canonical and grand-canonical fluctuation formulas ([[§B7.2 Free Energy from the Partition Function#^thm-b7-2-4|Theorem §B7.2.4]], [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-2|Theorem §B7.3.2]]).

**Setup.** $U = \langle E\rangle$, $\bar N = \langle N\rangle$, $\delta E = E - U$, $\delta N = N - \bar N$, $\eta_N = -\beta\mu$. In derivatives of $\ln Z$, $V$ and $N$ are fixed; in derivatives of $\ln\Xi(\beta, \eta_N, V)$, the other multiplier and $V$ are fixed. Energy levels do not depend on the multipliers.

> [!example] Example §C4a.10.1: The Three Ensembles at a Glance
> | | microcanonical | canonical | grand canonical |
> | --- | --- | --- | --- |
> | use when | isolated, given $E$ and $N$ | heat exchange, fixed $N$ | heat and particle exchange; independent orbitals |
> | controlled | $E, V, N$ | $T, V, N$ | $T, V, \mu$ |
> | weight | $1/\Omega$ in the shell | $e^{-\beta E_i}/Z$ | $e^{-\beta E_i - \eta_NN_i}/\Xi$ |
> | means | $U = E$, $\bar N = N$ (sharp shell) | $U = -\partial_\beta\ln Z$, $\bar N = N$ | $U = -\partial_\beta\ln\Xi$, $\bar N = -\partial_{\eta_N}\ln\Xi$ |
> | fluctuates | neither $E$ nor $N$ by exchange | $E$ | $E$ and $N$, possibly correlated |
> | conjugate pairs | (restrictions only) | $U \leftrightarrow \beta$ | $U \leftrightarrow \beta$, $\bar N \leftrightarrow \eta_N$ |
> | $\operatorname{Var}(E)$ | $0$ (sharp shell) | $\partial_\beta^2\ln Z = k_BT^2C_V$ | $\partial_\beta^2\ln\Xi$ |
> | $\operatorname{Var}(N)$ | $0$ | $0$ | $\partial_{\eta_N}^2\ln\Xi$ |
> | $\operatorname{Cov}(E, N)$ | $0$ | $0$ | $\partial_\beta\partial_{\eta_N}\ln\Xi$ |
> | potential | $S_{\text{mc}} = k_B\ln\Omega$ | $F = -k_BT\ln Z$ | $\Phi = -k_BT\ln\Xi$ |
>
> A real microcanonical shell has a small finite width, which sets a residual energy spread; the zeros refer to the sharp idealization, and other observables still fluctuate.
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
> Other means are held fixed in entropy derivatives, other multipliers in partition-function derivatives.
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
> A reservoir fixes $T$, not the instantaneous energy, which fluctuates.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]] with a temperature-independent Hamiltonian; *applies:* the stated ensemble, not every microcanonical system.
>
> *Source: Mao §4.4.4, table · PHY 510 Problem Set 5, Problem 2(b), official solution · level-B home: [[§B7.2 Free Energy from the Partition Function#^thm-b7-2-4|Theorem §B7.2.4]]*

^thm-c4a-10-2

> [!derivation]- Derivation
> [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]] with $\eta = \beta$, $A = E$: $\operatorname{Var}(E) = \partial_\beta^2\ln Z = -\partial_\beta U$. Since $d\beta/dT = -1/(k_BT^2)$, $-\partial_\beta U = k_BT^2\partial_TU = k_BT^2C_V$, and a variance is nonnegative.

^der-c4a-10-2

*Uses:* [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]]

> [!theorem] Theorem §C4a.10.3: Grand-Canonical Fluctuations as Responses
> Changing from $\eta_N$ to $\mu$ at fixed $T$,
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
> So the grand-canonical energy variance is not $k_BT^2C_V$ at fixed particle number. For a homogeneous single-phase fluid, $\operatorname{Var}(N) = k_BT\bar N^2\kappa_T/V$ with $\kappa_T$ the isothermal compressibility.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]; *applies:* levels independent of $\mu$, $T$; the $\kappa_T$ form in the thermodynamic limit.
>
> *Source: Mao §4.4.4, eqs. (4.91)–(4.92) · PHY 510 Problem Set 5, Problem 2(c), official solution · level-B home: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-2|Theorem §B7.3.2]]*

^thm-c4a-10-3

> [!derivation]- Derivation
> **Step 1.** At fixed $T$, $V$, $\partial_\mu$ of each weight $e^{-\beta(E_i - \mu N_i)}$ brings down $\beta N_i$, so $\partial_\mu\ln\Xi = \beta\bar N$ and $\partial_\mu^2\ln\Xi = \beta^2\operatorname{Var}(N)$; with $\partial_\mu\bar N = \beta\operatorname{Var}(N)$ the second formula follows. The covariance is the same with $E_i$ in place of one $N_i$.
>
> **Step 2.** At fixed $\mu$, $\partial_\beta$ brings down $-(E_i - \mu N_i)$, which gives the last two formulas.
>
> **Step 3** ($\kappa_T$). At fixed $T$, $dp = n\,d\mu$ (Gibbs–Duhem, [[§B3.3 Chemical Potential and Conditions for Equilibrium#^thm-b3-3-3|Theorem §B3.3.3]]) with $n = \bar N/V$, so $(\partial n/\partial\mu)_T = (\partial n/\partial p)_T\,n = n^2\kappa_T$, and $\operatorname{Var}(N) = k_BTV(\partial n/\partial\mu)_T = k_BTVn^2\kappa_T$.

^der-c4a-10-3

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]], [[§B3.3 Chemical Potential and Conditions for Equilibrium#^thm-b3-3-3|Theorem §B3.3.3]]

> [!example] Example §C4a.10.2: How Small Are Relative Fluctuations?
> For a classical monatomic ideal gas, $U = \tfrac32Nk_BT$, $C_V = \tfrac32Nk_B$, $\kappa_T = 1/(nk_BT)$. Then
>
> $$
> \frac{\sqrt{\operatorname{Var}(E)}}{U} = \sqrt{\frac{2}{3N}}, \qquad \operatorname{Var}(N) = \bar N, \qquad \frac{\sqrt{\operatorname{Var}(N)}}{\bar N} = \frac{1}{\sqrt{\bar N}} .
> $$
>
> For $10^{23}$ particles these are about $2.6\times10^{-12}$ and $3.2\times10^{-12}$. Means grow like the system size and spreads like its square root, so relative fluctuations are small though extensive quantities do fluctuate. These are equilibrium fluctuations, not measurement noise.
>
> *Source: PHY 510 Problem Set 5, Problem 2(d), official solution · level B: [[§B7.2 Free Energy from the Partition Function#^rem-b7-2-3|Remark: How small the fluctuations are]]*

^ex-c4a-10-2

> [!remark] Remark: Slopes in the two descriptions
> In the MaxEnt description the entropy slopes are $\partial_US_{\text{eq}} = 1/T$ and $\partial_{\bar N}S_{\text{eq}} = -\mu/T$, derivatives with respect to prescribed means. For the microcanonical entropy the same values are $\partial_ES_{\text{mc}} = 1/T$ and $\partial_NS_{\text{mc}} = -\mu/T$, which compare different shells rather than different means within one shell.

^rem-c4a-10-1

> [!remark]- Connections
> - Fluctuations measure responses: this is the static case of the fluctuation–dissipation relations of Unit 2 — Mao §6.6 (level C to come).
> - Level B's discussion of how small canonical fluctuations are — [[§B7.2 Free Energy from the Partition Function#^rem-b7-2-3|Remark: How small the fluctuations are]].
