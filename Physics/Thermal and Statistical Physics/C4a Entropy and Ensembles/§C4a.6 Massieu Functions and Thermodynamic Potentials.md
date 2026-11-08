---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.6
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.5 The Canonical and Grand-Canonical Ensembles]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.7 Heat, Work and the Clausius Equality]] →

*Sources: Mao, PHY 510 notes, §4.3.7, eqs. (4.43)–(4.52) and the closing table · PHY 510 Lecture 10/1.*

MaxEnt produces the entropy as a function of the prescribed means; a partition function is naturally a function of the multipliers. The two are Legendre transforms of each other, exactly, for a system of any size. Multiplying by $-k_BT$ turns the transform of the entropy into the familiar free energies, so the structure of Chapter C1 ([[§C1.7 Thermodynamic Phase Space and Legendre Transforms|§C1.7]]) reappears, now in the entropy representation. Level B obtained $F = -k_BT\ln Z$ and $\Phi = -k_BT\ln\Xi$ directly ([[§B7.2 Free Energy from the Partition Function#^thm-b7-2-1|Theorem §B7.2.1]], [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-3|Theorem §B7.3.3]]).

**Setup.** The MaxEnt distribution $p_i^\ast = Z^{-1}\exp[-\sum_\alpha\eta_\alpha A_\alpha(i)]$ of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], with external parameters such as $V$ fixed. For the grand ensemble, $Z$ stands for $\Xi$.

> [!theorem] Theorem §C4a.6.1: The Maximum Entropy in Terms of $Z$
> $$
> H_{\max} = \ln Z + \sum_\alpha\eta_\alpha\bar A_\alpha, \qquad dH_{\max} = \sum_\alpha\eta_\alpha\,d\bar A_\alpha, \qquad \eta_\alpha = \frac{\partial H_{\max}}{\partial\bar A_\alpha}\Bigr|_{\bar A_{\gamma\neq\alpha}} .
> $$
>
> The identifications $\eta_E = \beta$ and $\eta_N = -\beta\mu$ of [[§C4a.5 The Canonical and Grand-Canonical Ensembles|§C4a.5]] are instances of the last relation.
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]; *applies:* exact, any system size.
>
> *Source: Mao §4.3.7, eqs. (4.43)–(4.45)*

^thm-c4a-6-1

> [!derivation]- Derivation
> **Step 1.** Insert $\ln p_i^\ast = -\ln Z - \sum_\alpha\eta_\alpha A_\alpha(i)$ into $H = -\sum_ip_i^\ast\ln p_i^\ast$:
>
> $$
> H_{\max} = \ln Z\sum_ip_i^\ast + \sum_\alpha\eta_\alpha\sum_ip_i^\ast A_\alpha(i) = \ln Z + \sum_\alpha\eta_\alpha\bar A_\alpha .
> $$
>
> **Step 2.** Differentiate and use $d\ln Z = -\sum_\alpha\bar A_\alpha\,d\eta_\alpha$ (the mean relation of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]):
>
> $$
> dH_{\max} = d\ln Z + \sum_\alpha\bar A_\alpha\,d\eta_\alpha + \sum_\alpha\eta_\alpha\,d\bar A_\alpha = \sum_\alpha\eta_\alpha\,d\bar A_\alpha .
> $$

^der-c4a-6-1

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]

> [!definition] Definition §C4a.6.1: Massieu Function
> A Legendre transform of the entropy is a **Massieu function**. In dimensionless form, transforming $S_{\text{eq}}/k_B = H_{\max}$ from the means $\bar A_\alpha$ to the multipliers $\eta_\alpha$ gives
>
> $$
> \ln Z(\{\eta_\alpha\}) = H_{\max}(\{\bar A_\alpha\}) - \sum_\alpha\eta_\alpha\bar A_\alpha ,
> $$
>
> with the pairs
>
> $$
> dH_{\max} = \sum_\alpha\eta_\alpha\,d\bar A_\alpha \;\longleftrightarrow\; d\ln Z = -\sum_\alpha\bar A_\alpha\,d\eta_\alpha, \qquad \eta_\alpha = \frac{\partial H_{\max}}{\partial\bar A_\alpha} \;\longleftrightarrow\; \bar A_\alpha = -\frac{\partial\ln Z}{\partial\eta_\alpha} .
> $$
>
> *Source: Mao §4.3.7, eq. (4.46) · Callen, Thermodynamics (cited by Mao)*

^def-c4a-6-1

> [!theorem] Theorem §C4a.6.2: Canonical: $\ln Z = -\beta F$
> With only the energy constrained, the pair is $(U, \beta)$ and
>
> $$
> \ln Z(\beta, V, N) = \frac{S_{\text{eq}}}{k_B} - \beta U, \qquad S_{\text{eq}} = k_B(\ln Z + \beta U), \qquad F(T, V, N) = U - TS_{\text{eq}} = -k_BT\ln Z .
> $$
>
> In the entropy representation $\ln Z$ trades $U$ for $\beta$; in the energy representation of Chapter C1, $F$ trades $S$ for $T$ ([[§C1.7 Thermodynamic Phase Space and Legendre Transforms#^ex-c1-7-1|Example §C1.7.1]]). The two describe one family of canonical states, related by $\ln Z = -\beta F$.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]]; *applies:* exact, any size.
>
> *Source: Mao §4.3.7, eqs. (4.47)–(4.49) · level-B home: [[§B7.2 Free Energy from the Partition Function#^thm-b7-2-1|Theorem §B7.2.1]]*

^thm-c4a-6-2

> [!derivation]- Derivation
> [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]] with one constraint, $\eta_E = \beta$, $\bar A_E = U$, and $H_{\max} = S_{\text{eq}}/k_B$ ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]]). Multiply by $-k_BT$: $-k_BT\ln Z = U - TS_{\text{eq}} = F$.

^der-c4a-6-2

*Uses:* [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]], [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|Theorem §C4a.5.2]]

> [!theorem] Theorem §C4a.6.3: Grand Canonical: $\ln\Xi = -\beta\Phi$
> With pairs $(U, \beta)$ and $(\bar N, \eta_N)$, $\eta_N = -\beta\mu$,
>
> $$
> \ln\Xi(\beta, \eta_N, V) = \frac{S_{\text{eq}}}{k_B} - \beta(U - \mu\bar N), \qquad d\ln\Xi = -U\,d\beta - \bar N\,d\eta_N ,
> $$
>
> $$
> \Phi(T, V, \mu) = U - TS_{\text{eq}} - \mu\bar N = -k_BT\ln\Xi .
> $$
>
> $\Phi$ trades $(S, \bar N)$ for $(T, \mu)$.
>
> *Model:* [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]; *applies:* exact, any size.
>
> *Source: Mao §4.3.7, eqs. (4.50)–(4.52) · level-B home: [[§B7.3 The Grand Canonical Ensemble#^thm-b7-3-3|Theorem §B7.3.3]]*

^thm-c4a-6-3

> [!derivation]- Derivation
> [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]] with two constraints: $\ln\Xi = H_{\max} - \beta U - \eta_N\bar N = S_{\text{eq}}/k_B - \beta U + \beta\mu\bar N$. Multiply by $-k_BT$.

^der-c4a-6-3

*Uses:* [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|Theorem §C4a.6.1]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]], [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|Theorem §C4a.5.4]]

> [!caution] Caution: Fixed fugacity is not fixed $\mu$
> In $U = -(\partial\ln\Xi/\partial\beta)_{\eta_N, V}$ the multiplier $\eta_N = -\ln z$ is held fixed, which means fixed fugacity $z = e^{\beta\mu}$. Holding $\mu$ fixed instead gives a different derivative, $-(\partial\ln\Xi/\partial\beta)_{\mu,V} = U - \mu\bar N$ ([[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-3|Theorem §C4a.10.3]]).

^cau-c4a-6-1

> [!example] Example §C4a.6.1: The Entropy Representation at a Glance
> With $S = S_{\text{eq}}$, $\beta = 1/k_BT$, $V$ fixed (and $N$ in the canonical column):
>
> | | general MaxEnt | canonical | grand canonical |
> | --- | --- | --- | --- |
> | entropy | $dH_{\max} = \sum_\alpha\eta_\alpha\,d\bar A_\alpha$ | $d(S/k_B) = \beta\,dU$ | $d(S/k_B) = \beta\,dU - \beta\mu\,d\bar N$ |
> | Massieu | $d\ln Z = -\sum_\alpha\bar A_\alpha\,d\eta_\alpha$ | $d(-\beta F) = -U\,d\beta$ | $d(-\beta\Phi) = -U\,d\beta + \bar N\,d(\beta\mu)$ |
> | relation | $\ln Z = H_{\max} - \sum_\alpha\eta_\alpha\bar A_\alpha$ | $\ln Z = -\beta F = S/k_B - \beta U$ | $\ln\Xi = -\beta\Phi = S/k_B - \beta U + \beta\mu\bar N$ |
>
> In entropy units the Massieu functions are $k_B\ln Z = -F/T$ and $k_B\ln\Xi = -\Phi/T$.
>
> *Source: Mao §4.3.7, closing table*

^ex-c4a-6-1

> [!caution] Caution: These relations are exact
> Nothing here replaced the ensemble by a single energy shell; $\ln Z = -\beta F$ with $F = U - TS_{\text{eq}}$ holds for any system size. The large-system step, which relates $S_{\text{eq}}$ to the microcanonical $S_{\text{mc}}$ of one shell, is separate ([[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-4|Theorem §C4a.9.4]]).

^cau-c4a-6-2

> [!remark]- Connections
> - Chapter C1 built the same family in the energy representation, from $U(S, V, N)$ — [[§C1.7 Thermodynamic Phase Space and Legendre Transforms#^thm-c1-7-2|Theorem §C1.7.2]].
> - Second derivatives of $\ln Z$ are covariances — [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|Theorem §C4a.10.1]].
