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

The partition function sums Boltzmann weights over microstates. Grouping the states by energy makes it a Laplace transform of the density of states, which is exact. For a large system, the logarithm of that Laplace transform becomes a Legendre transform of the microcanonical entropy: summing over energies turns into minimizing $E - TS$. This section shows how, and why it is a different statement from the exact relation $\ln Z = -\beta F$ of [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]. Level B proves the equivalence of the ensembles more briefly ([[§B7.2 Free Energy from the Partition Function#^thm-b7-2-5|Theorem §B7.2.5]]).

**Setup.** Fixed $V$, $N$ unless they are summed over; temperatures $T > 0$; an extensive system, so that energies and entropies scale with $N$.

> [!definition] Definition §C4a.9.1: Density of States
> The **density of states** $g(E)$ counts complete $N$-particle microstates per unit energy:
>
> $$
> g(E) = \int d\Gamma_N(X)\,\delta\bigl(E - H_N(X)\bigr) \quad\text{(classical)}, \qquad g(E) = \operatorname{Tr}_{\mathcal H_N}\delta(E - \hat H) = \sum_\nu\delta(E - E_\nu) \quad\text{(quantum)} .
> $$
>
> It has dimensions of inverse energy. The number of states in a shell is dimensionless, $\Omega(E, \Delta E) = \int_E^{E+\Delta E}g(E')\,dE' \simeq g(E)\Delta E$, and $S_{\text{mc}}(E, V, N) = k_B\ln\Omega$ for one fixed shell convention.
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
> $Z$ sums over energies at fixed $N$, and $\Xi$ also over particle numbers.
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
> The prefactor, which records the width of the maximum, drops out of the limit. If the maximizer is not unique the max formula still holds (a Legendre–Fenchel transform), but $\varphi$ need not be differentiable.
>
> *Model:* Laplace's method; *applies:* as stated.
>
> *Source: Mao §4.4.2, box "From a Laplace transform to a Legendre transform" · DLMF §2.4*

^thm-c4a-9-3

> [!derivation]- Derivation
> **Step 1** (expand). $h(x) - \tilde sx = h(x^\ast) - \tilde sx^\ast + \tfrac12h''(x^\ast)(x - x^\ast)^2 + O((x - x^\ast)^3)$.
>
> **Step 2** (Gaussian). $\int dx\,e^{-\frac\lambda2|h''|(x - x^\ast)^2} = \sqrt{2\pi/(\lambda|h''|)}$ ([[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-3|Theorem §B4.1.3]]). The region contributing has width $\lambda^{-1/2}$, so the cubic term is $O(\lambda^{-1/2})$ in the exponent and the rest of the line is exponentially smaller.
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
> with $(\partial S_{\text{mc}}/\partial E)_{V,N} = 1/T$ at $E^\ast$: the selected energy has the reservoir's temperature. Compare the exact $\ln Z = S_{\text{eq}}(U)/k_B - \beta U$ ([[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|Theorem §C4a.6.2]]). The extra step replaces the entropy of the whole distribution by the entropy of one shell; for a stable system with a unique $E^\ast/N$, $U \simeq E^\ast$ and $S_{\text{eq}}(U) \simeq S_{\text{mc}}(E^\ast)$ at leading extensive order, but they differ at finite size.
>
> *Model:* extensive system, unique maximum; *applies:* leading order in $N$.
>
> *Source: Mao §4.4.2, eqs. (4.79)–(4.84)*

^thm-c4a-9-4

> [!derivation]- Derivation
> **Step 1.** $g(E)\Delta E \simeq \Omega = e^{S_{\text{mc}}/k_B}$, so [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-1|Theorem §C4a.9.1]] becomes $Z \simeq \int\frac{dE}{\Delta E}\exp[S_{\text{mc}}(E)/k_B - \beta E]$. A finite lower energy bound $E_0$ factors out as $e^{-\beta E_0}$, leaving a one-sided transform.
>
> **Step 2.** Write $E = Nx$, $S_{\text{mc}}/k_B = Ns(x)$: the exponent is $N[s(x) - \beta x]$, and [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] with $\lambda = N$ gives the max formula; the prefactor and $\Delta E$ contribute $O(\ln N)$.
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
> Each transform lets an extensive quantity fluctuate while a reservoir fixes its conjugate intensive variable. The reference volume $V_0$ does not affect bulk thermodynamics.
>
> *Model:* reservoirs of $T$ and $\mu$, or of $T$ and $p$; *applies:* leading order in system size; the partition-function definitions are exact.
>
> *Source: Mao §4.4.3, eqs. (4.85)–(4.88)*

^thm-c4a-9-5

> [!derivation]- Derivation
> **Grand.** [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|Theorem §C4a.9.2]] with $Z(\beta; N) \simeq \sum_E e^{S_{\text{mc}}/k_B - \beta E}$, then [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] in both $E$ and $N$; stationarity in each gives the two conditions.
>
> **Gibbs.** $Z(\beta; V) = e^{-\beta F(T,V,N)}$ exactly, so $\Delta = \int\frac{dV}{V_0}e^{-\beta[F + pV]}$, and [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]] in $V$ gives the minimum; stationarity gives $p = -\partial F/\partial V$. $\ln V_0$ is $O(1)$, not extensive.

^der-c4a-9-5

*Uses:* [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|Theorem §C4a.9.2]], [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|Theorem §C4a.9.3]]

> [!remark]- ★ Remark: Saddle points beyond thermodynamics
> The step from a Laplace transform to a Legendre transform is the saddle-point method, named for the shape of the exponent in the complex plane, and it recurs across physics.
>
> 1. **Classical mechanics.** With the action $A[q] = \int dt\,(\tfrac m2\dot q^2 - W(q))$, the classical path makes $A$ stationary, $\delta A = 0$, which gives $m\ddot q = -W'(q)$; it need not be a minimum.
> 2. **Quantum amplitudes.** Feynman's propagator is $K = \int\mathcal Dq\,e^{iA[q]/\hbar}$. Paths away from $\delta A = 0$ have rapidly varying phases that cancel when the action changes by many $\hbar$, and stationary phase recovers classical mechanics. The $i$ makes the paths interfere instead of adding as positive weights.
> 3. **Imaginary time.** Setting $t = -i\tau$ (a Wick rotation) turns $e^{-i\hat Ht/\hbar}$ into $e^{-\hat H\tau/\hbar}$ and $e^{iA/\hbar}$ into $e^{-A_E/\hbar}$ with $A_E = \int d\tau\,[\tfrac m2(dq/d\tau)^2 + W(q)]$. With $\tau_f = \beta\hbar$ the trace closes the paths:
>
> $$
> Z = \operatorname{Tr}e^{-\beta\hat H} = \int_{q(0) = q(\beta\hbar)}\mathcal Dq\,e^{-A_E[q]/\hbar} .
> $$
>
> 4. **Fields.** After a Wick rotation, a quantum field theory in $d$ space dimensions has the form of a statistical field theory in $d + 1$ Euclidean dimensions; at temperature $T$ the extra direction has length $\beta\hbar$, with bosonic fields periodic and fermionic fields antiperiodic around it. Reading the weights as probabilities needs a real Euclidean action and a suitable measure, which not every quantum field theory has.
>
> The shared lesson: a sum over many possibilities yields a variational principle when the stationary contributions dominate.
>
> *Source: Mao §4.4.2, box "Saddle point approximation beyond thermodynamics" (citing Feynman Lectures II, Ch. 19; Feynman 1948; Tong, Statistical Field Theory, §2.3; Laine and Vuorinen) · QM home of path integrals: [[§C4.2 The Feynman Path Integral|QM §C4.2]]*

^rem-c4a-9-1

> [!remark]- Connections
> - Equivalence of ensembles and when it fails — [[§B7.2 Free Energy from the Partition Function#^thm-b7-2-5|Theorem §B7.2.5]], [[§B7.2 Free Energy from the Partition Function#^cau-b7-2-2|Caution: When the ensembles differ]].
> - The Legendre transform here has the same form as in Chapter C1, now with $\tilde s = \beta$ — [[§C1.7 Thermodynamic Phase Space and Legendre Transforms#^ex-c1-7-2|Example §C1.7.2]].
