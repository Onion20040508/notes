---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.9
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c, extension]
---
← [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.10 Ensembles at a Glance and Fluctuations]] →

★ *Optional in PHY 510: Mao marks §4.4.1–§4.4.3 as reading not covered in class.*

*Sources: Mao, PHY 510 notes, §4.4.1–§4.4.3, eqs. (4.74)–(4.88) and boxes "From a Laplace transform to a Legendre transform", "Saddle point approximation beyond thermodynamics" · NIST DLMF §2.4 (cited by Mao).*

The partition function sums Boltzmann weights over microstates. Grouping the states by energy makes it a Laplace transform of the density of states, which is exact. For a large system, the logarithm of that Laplace transform becomes a Legendre transform of the microcanonical entropy: the sum over $E$ is dominated by the energy that minimizes $E - TS_{\text{mc}}(E)$. This section shows how, and why it is a different statement from the exact relation $\ln Z = -\beta F$ of [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]. Level B proves the equivalence of the ensembles more briefly ([[§B7.2 Free Energy from the Partition Function#^thm-b7-2-5|Theorem §B7.2.5]]).

**Setup.** Fixed $V$, $N$ unless they are summed over; temperatures $T > 0$; an extensive system, so that energies and entropies scale with $N$.

> [!definition] Definition §C4a.9.1: Density of States
> The **density of states** $g(E)$ counts complete $N$-particle microstates per unit energy:
>
> $$
> g(E) = \int d\Gamma_N(X)\,\delta\bigl(E - H_N(X)\bigr) \quad\text{(classical)}, \qquad g(E) = \operatorname{Tr}_{\mathcal H_N}\delta(E - \hat H) = \sum_\nu\delta(E - E_\nu) \quad\text{(quantum)} .
> $$
>
> $g$ carries units of $1/\text{energy}$; the logarithm is therefore taken of the shell count, a pure number:
>
> $$
> \Omega(E, \Delta E) = \int_E^{E+\Delta E}g(E')\,dE' \simeq g(E)\Delta E, \qquad S_{\text{mc}}(E, V, N) = k_B\ln\Omega \quad(\text{one fixed }\Delta E) .
> $$
>
> *Source: Mao §4.4.1, eqs. (4.74)–(4.76) · level B: [[§B10.1 Bose–Einstein and Fermi–Dirac Distributions#^def-b10-1-2|Def. §B10.1.2]] (one-particle density of states, a different object)*

^def-c4a-9-1

> [!theorem] Theorem §C4a.9.1: The Partition Function Is a Laplace Transform
> $$
> Z(\beta) = \sum_ie^{-\beta E_i} = \int dE\,g(E)\,e^{-\beta E} ,
> $$
>
> exactly, for discrete spectra too (with $g$ a sum of deltas).
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]]; *applies:* any system.
>
> *Source: Mao §4.4.1, eq. (4.77)*

^thm-c4a-9-1

> [!derivation]- Derivation
> $\int dE\,\sum_\nu\delta(E - E_\nu)e^{-\beta E} = \sum_\nu e^{-\beta E_\nu}$, the defining property of $\delta$; classically $\int dE\,\delta(E - H_N(X))e^{-\beta E} = e^{-\beta H_N(X)}$ inside $\int d\Gamma_N$.

^der-c4a-9-1

*Uses:* [[§C4a.9★ Density of States, Laplace and Legendre#^def-c4a-9-1|Def. §C4a.9.1]]

> [!theorem] Theorem §C4a.9.2: The Grand Partition Function Sums over $N$
> $$
> \Xi(\beta, z, V) = \sum_{N=0}^\infty z^NZ(\beta; N), \qquad z = e^{\beta\mu} .
> $$
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]; *applies:* exact.
>
> *Source: Mao §4.4.1, eq. (4.78)*

^thm-c4a-9-2

> [!derivation]- Derivation
> Group the terms of $\Xi = \sum_ie^{-\beta(E_i - \mu N_i)}$ by $N_i = N$: each group is $e^{\beta\mu N}\sum_{i:N_i=N}e^{-\beta E_i} = z^NZ(\beta; N)$.

^der-c4a-9-2

*Uses:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]

> [!theorem] Theorem §C4a.9.3: The Scaled Logarithm of a Laplace Transform Is a Legendre Transform
> Let $f_\lambda(x) = e^{\lambda h(x)}$ with $h$ smooth and concave, and suppose $h(x) - \tilde sx$ has a unique interior maximum $x^\ast$ with $h''(x^\ast) < 0$ and the integrals converge. Then
>
> $$
> \hat f_\lambda(\lambda\tilde s) = \int_0^\infty dx\,e^{\lambda[h(x) - \tilde sx]} \simeq e^{\lambda[h(x^\ast) - \tilde sx^\ast]}\sqrt{\frac{2\pi}{\lambda|h''(x^\ast)|}} ,
> $$
>
> $$
> \varphi(\tilde s) \equiv \lim_{\lambda\to\infty}\frac{\ln\hat f_\lambda(\lambda\tilde s)}{\lambda} = \max_{x\ge0}\bigl[h(x) - \tilde sx\bigr], \qquad h'(x^\ast) = \tilde s, \qquad \varphi'(\tilde s) = -x^\ast .
> $$
>
> 1. The Gaussian factor is $O(\lambda^{-1/2})$, so its logarithm is $O(\ln\lambda)$ and does not survive in $\varphi$.
> 2. With several maximizers, $\varphi = \sup_x[h(x) - \tilde sx]$ still holds (Legendre–Fenchel transform), and $\varphi$ has a kink where the maximizer jumps.
>
> *Model:* Laplace's method; *applies:* as stated.
>
> *Source: Mao §4.4.2, box "From a Laplace transform to a Legendre transform" · DLMF §2.4*

^thm-c4a-9-3

> [!derivation]- Derivation
> **Step 1** (expand). $h(x) - \tilde sx = h(x^\ast) - \tilde sx^\ast + \tfrac12h''(x^\ast)(x - x^\ast)^2 + O((x - x^\ast)^3)$.
>
> **Step 2** (Gaussian). $\int dx\,e^{-\frac\lambda2|h''|(x - x^\ast)^2} = \sqrt{2\pi/(\lambda|h''|)}$ ([[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-3|Theorem §B4.1.3]]). The region contributing has width $\lambda^{-1/2}$, so the cubic term is $O(\lambda^{-1/2})$ in the exponent. Outside $|x - x^\ast| < \delta$, concavity and uniqueness give $h - \tilde sx \le h(x^\ast) - \tilde sx^\ast - \epsilon$ for some $\epsilon(\delta) > 0$; if the integral converges at some $\lambda_0$, that part is at most $e^{(\lambda - \lambda_0)[h(x^\ast) - \tilde sx^\ast - \epsilon]}\hat f_{\lambda_0}(\lambda_0\tilde s)$ for $\lambda \ge \lambda_0$, exponentially smaller than the peak.
>
> **Step 3** (limit). $\frac1\lambda\ln\hat f_\lambda = h(x^\ast) - \tilde sx^\ast + O(\lambda^{-1}\ln\lambda)$.
>
> **Step 4** (Legendre). $d\varphi = [h'(x^\ast) - \tilde s]\,dx^\ast - x^\ast\,d\tilde s = -x^\ast\,d\tilde s$.

^der-c4a-9-3

*Uses:* [[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-3|Theorem §B4.1.3]]

> [!theorem] Theorem §C4a.9.4: $\ln Z$ as a Legendre Transform of the Shell Entropy
> For an extensive system, to leading order in $N$,
>
> $$
> \ln Z(\beta) \simeq \max_E\Bigl[\frac{S_{\text{mc}}(E)}{k_B} - \beta E\Bigr] = \frac{S_{\text{mc}}(E^\ast)}{k_B} - \beta E^\ast, \qquad F = -k_BT\ln Z \simeq \min_E\bigl[E - TS_{\text{mc}}(E)\bigr] ,
> $$
>
> with $(\partial S_{\text{mc}}/\partial E)_{V,N} = 1/T$ at $E^\ast$. Against the exact $\ln Z = S_{\text{eq}}(U)/k_B - \beta U$ of [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]],
>
> $$
> S_{\text{eq}}(U) - S_{\text{mc}}(E^\ast) = k_B\beta(U - E^\ast) + O(k_B\ln N), \qquad \frac{U - E^\ast}{N} \to 0 ,
> $$
>
> so the two entropies agree per particle, not exactly.
>
> *Model:* extensive, thermodynamically stable system ($S_{\text{mc}}$ strictly concave in $E$), unique maximum; *applies:* leading order in $N$.
>
> *Source: Mao §4.4.2, eqs. (4.79)–(4.84)*

^thm-c4a-9-4

> [!derivation]- Derivation
> **Step 1.** $g(E)\Delta E \simeq \Omega = e^{S_{\text{mc}}/k_B}$, so [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-1|Theorem §C4a.9.1]] becomes $Z \simeq \int\frac{dE}{\Delta E}\exp[S_{\text{mc}}(E)/k_B - \beta E]$. A finite lower energy bound $E_0$ factors out as $e^{-\beta E_0}$, leaving a one-sided transform.
>
> **Step 2.** Write $E = Nx$, $S_{\text{mc}}/k_B = Ns(x)$: the exponent is $N[s(x) - \beta x]$, and [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] with $\lambda = N$ gives the max formula; the prefactor, $\Delta E$ and the Jacobian $dE = N\,dx$ contribute $O(\ln N)$.
>
> **Step 3.** Multiply by $-k_BT$: a maximum of $S/k_B - \beta E$ is a minimum of $E - TS$. Stationarity gives $\partial S_{\text{mc}}/\partial E = k_B\beta = 1/T$.

^der-c4a-9-4

*Uses:* [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-1|Theorem §C4a.9.1]], [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]], [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]

> [!theorem] Theorem §C4a.9.5: Grand and Gibbs Potentials as Minima
> To leading order,
>
> $$
> \Phi(T, V, \mu) = -k_BT\ln\Xi \simeq \min_{E,N}\bigl[E - TS_{\text{mc}}(E, V, N) - \mu N\bigr], \qquad \frac{\partial S_{\text{mc}}}{\partial E} = \frac1T, \quad \frac{\partial S_{\text{mc}}}{\partial N} = -\frac\mu T ,
> $$
>
> and for the isothermal–isobaric ensemble,
>
> $$
> \Delta(T, p, N) = \int_0^\infty\frac{dV}{V_0}e^{-\beta pV}Z(\beta; V), \qquad G(T, p, N) = -k_BT\ln\Delta \simeq \min_V\bigl[F(T, V, N) + pV\bigr], \quad p = -\Bigl(\frac{\partial F}{\partial V}\Bigr)_{T,N} .
> $$
>
> | ensemble | summed over (fluctuates) | set by the reservoir |
> | --- | --- | --- |
> | canonical | $E$ | $T$ |
> | grand canonical | $E$, $N$ | $T$, $\mu$ |
> | isothermal–isobaric | $E$, $V$ | $T$, $p$ |
>
> The reference volume $V_0$ changes $G$ by $O(k_BT)$ only.
>
> *Model:* reservoirs of $T$ and $\mu$, or of $T$ and $p$; *applies:* leading order in system size; the partition-function definitions are exact.
>
> *Source: Mao §4.4.3, eqs. (4.85)–(4.88)*

^thm-c4a-9-5

> [!derivation]- Derivation
> **Grand.** [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|Theorem §C4a.9.2]] with $Z(\beta; N) \simeq \sum_E e^{S_{\text{mc}}/k_B - \beta E}$, then [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] in both $E$ and $N$; stationarity in each gives the two conditions. This uses the two-variable form of Laplace's method (Hessian of $S_{\text{mc}}(E, N)$ negative definite, i.e. joint concavity) and, for the sum over integer $N$, the bound $\max_N \le \sum_N \le (\#\text{terms})\max_N$, whose logarithm differs from $\ln\max_N$ by $O(\ln N)$.
>
> **Gibbs.** $Z(\beta; V) = e^{-\beta F(T,V,N)}$ exactly, so $\Delta = \int\frac{dV}{V_0}e^{-\beta[F + pV]}$, and [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] in $V$ gives the minimum; stationarity gives $p = -\partial F/\partial V$. $\ln V_0$ is $O(1)$, not extensive.

^der-c4a-9-5

*Uses:* [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|Theorem §C4a.9.2]], [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]]

> [!remark]- ★ Remark: Saddle points beyond thermodynamics
> [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] is the real-exponent case of the saddle-point method. Other cases, with their homes:
>
> 1. **Stationary action**, $\delta A = 0$ for $A[q] = \int dt\,(\tfrac m2\dot q^2 - W(q))$, as the dominant path: [[§C4.2 The Feynman Path Integral#^rem-c4-2-2|QM Remark: Hamilton's principle, from axiom to consequence]].
> 2. **Oscillating exponent** $e^{iA[q]/\hbar}$ in $K = \int\mathcal Dq\,e^{iA/\hbar}$: stationary phase [[§C4.2 The Feynman Path Integral#^thm-c4-2-5|QM Theorem §C4.2.5]] and the classical limit [[§C4.2 The Feynman Path Integral#^thm-c4-2-6|QM Theorem §C4.2.6]].
> 3. **Imaginary time**, $t = -i\tau$, so $iA \to -A_E$ with $A_E = \int_0^{\beta\hbar}d\tau\,[\tfrac m2(dq/d\tau)^2 + W(q)]$, and the trace closes the paths ([[§C4.2 The Feynman Path Integral#^rem-c4-2-4|QM Remark: Imaginary time and statistical mechanics]]):
>
> $$
> Z = \operatorname{Tr}e^{-\beta\hat H} = \int_{q(0) = q(\beta\hbar)}\mathcal Dq\,e^{-A_E[q]/\hbar} .
> $$
>
> 4. **Fields at temperature $T$**: the same construction in $d + 1$ dimensions, with boundary conditions $\phi(\tau + \beta\hbar) = \pm\phi(\tau)$ ($+$ bosons, $-$ fermions); the weights $e^{-A_E/\hbar}$ are probabilities only when $A_E$ is real (Tong, *Statistical Field Theory*, §2.3).
>
> *Source: Mao §4.4.2, box "Saddle point approximation beyond thermodynamics" (citing Feynman Lectures II, Ch. 19; Feynman 1948; Tong, Statistical Field Theory, §2.3; Laine and Vuorinen) · QM home of path integrals: [[§C4.2 The Feynman Path Integral|QM §C4.2]]*

^rem-c4a-9-1

> [!remark]- Connections
> - Equivalence of ensembles and when it fails — [[§B7.2 Free Energy from the Partition Function#^thm-b7-2-5|Theorem §B7.2.5]], [[§B7.2 Free Energy from the Partition Function#^cau-b7-2-2|Caution: When the ensembles differ]].
> - The Legendre transform here has the same form as in Chapter C1, now with $\tilde s = \beta$ — [[§C1.7 Thermodynamic Phase Space and Legendre Transforms#^ex-c1-7-2|Example §C1.7.2]].
