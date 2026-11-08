---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.3
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.2 The Entropy of a Statistical State]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.4 Why the Maximum Is Thermodynamic Entropy]] →

*Sources: Mao, PHY 510 notes, §4.3.1–§4.3.3, eqs. (4.16)–(4.25) and box "Lagrange multipliers: a bead on a circular wire" · Jaynes, Information Theory and Statistical Mechanics (1957), §2–§3; II, §10 · PHY 510 Lectures 9/24, 9/29.*

Knowing only the mean energy of a system leaves many probability distributions possible. Which one describes it? Jaynes's answer is a rule of inference: take the distribution with the largest entropy among those that agree with what is known. This section states the rule, distinguishes the two kinds of information it can use, and solves the maximization in general with Lagrange multipliers. Level B stated the same principle as a remark and solved its main cases ([[§B6.3 Entropy, Information and the Gibbs Paradox#^rem-b6-3-2|Remark: The maximum-entropy principle]], [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-4|Theorem §B6.3.4]]); here it is the starting point of the ensembles.

**Setup.** A fixed set of allowed microstates $i$, with the values $A_\alpha(i)$ of some observables in each, and the entropy $H[p] = -\sum_ip_i\ln p_i$ of [[§C4a.2 The Entropy of a Statistical State#^def-c4a-2-1|Def. §C4a.2.1]]. External parameters such as $V$ are held fixed.

## The principle

> [!principle] Principle §C4a.3.1: Jaynes's Maximum-Entropy Principle
> When the available information is incomplete, assign the probability distribution that has the largest entropy $H[p]$ among all distributions compatible with that information. It builds in what is known and commits to nothing else about which microstate is occupied.
>
> For quantum systems the maximized quantity is $H_{\text{vN}}[\hat\rho]$, over density operators with the prescribed expectation values.
>
> *Domain:* statistical inference from macroscopic information; the microscopic alternatives (and, classically, the measure $d\Gamma$) must be fixed first, with distinct states of equal energy counted separately.
>
> *Source: Mao §4.3.1, box "Jaynes's maximum-entropy principle (MaxEnt)" · Jaynes (1957), §2–§3; II, §10 · Lecture 9/24*

^pr-c4a-3-1

> [!caution] Caution: Restricting the states versus prescribing a mean
> Information enters in two different places. A **restriction** removes microstates from the set: a fixed particle number excludes every state with another $N$. A **mean constraint** keeps the states and restricts the probabilities: a prescribed mean energy allows many $E_i$ but requires $\sum_ip_iE_i = U$. Getting the ensemble right means deciding which kind each piece of information is.

^cau-c4a-3-1

> [!definition] Definition §C4a.3.1: The Three Equilibrium Ensembles as MaxEnt Problems
> At fixed $V$, with normalization in every case:
>
> | Ensemble | allowed microstates | prescribed means |
> | --- | --- | --- |
> | microcanonical | fixed $N$, energy in a given shell | none |
> | canonical | fixed $N$, any energy | $\sum_ip_iE_i = U$ |
> | grand canonical | any energy and particle number | $\sum_ip_iE_i = U$, $\sum_ip_iN_i = \bar N$ |
>
> *Source: Mao §4.3.1, table*

^def-c4a-3-1

> [!theorem] Theorem §C4a.3.2: The Microcanonical Ensemble Maximizes Entropy in a Shell
> With $\Omega$ microstates in the shell and only normalization imposed,
>
> $$
> p_i^{\text{mc}} = \frac1\Omega\ \text{inside the shell}, \qquad H_{\max} = \ln\Omega ,
> $$
>
> and $p_i = 0$ outside. Comparing with $S_{\text{mc}} = k_B\ln\Omega$ ([[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]),
>
> $$
> S_{\text{mc}} = k_BH_{\max} .
> $$
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^def-c4a-3-1|Def. §C4a.3.1]], first row; *applies:* isolated system in a shell.
>
> *Source: Mao §4.3.2, eqs. (4.16)–(4.17)*

^thm-c4a-3-2

> [!derivation]- Derivation
> Within the shell this is [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|Theorem §C4a.1.2]] in nats: the maximum of $H$ over $\Omega$ alternatives is $\ln\Omega$, reached only by the uniform distribution. Multiplying by $k_B > 0$ does not move the maximum.

^der-c4a-3-1

*Uses:* [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|Theorem §C4a.1.2]], [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]

## The general solution

> [!theorem] Theorem §C4a.3.3: Maximum Entropy with Mean Constraints Is Exponential
> Maximize $H[p]$ over the allowed states subject to $\sum_ip_i = 1$ and
>
> $$
> \sum_ip_iA_\alpha(i) = \bar A_\alpha, \qquad \alpha = 1, \dots, r .
> $$
>
> The maximizer is
>
> $$
> p_i^\ast = \frac1Z\exp\Bigl[-\sum_\alpha\eta_\alpha A_\alpha(i)\Bigr], \qquad Z(\eta_1, \dots, \eta_r) = \sum_i\exp\Bigl[-\sum_\alpha\eta_\alpha A_\alpha(i)\Bigr] ,
> $$
>
> with the multipliers $\eta_\alpha$ fixed by
>
> $$
> \bar A_\alpha = -\frac{\partial\ln Z}{\partial\eta_\alpha} .
> $$
>
> It is the unique maximum when it exists.
>
> *Model:* a fixed set of allowed states; *applies:* when $Z$ converges and the prescribed means can be reached with all $p_i > 0$; at the edges of the allowed range the maximum can sit on fewer states.
>
> *Source: Mao §4.3.3, eqs. (4.18)–(4.25) · Lecture 9/29 · level-B home: [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-4|Theorem §B6.3.4]]*

^thm-c4a-3-3

> [!derivation]- Derivation
> **Step 1** (Lagrangian). With a multiplier $\lambda_0$ for normalization and $\eta_\alpha$ for the means,
>
> $$
> \mathcal L = -\sum_ip_i\ln p_i - \lambda_0\Bigl(\sum_ip_i - 1\Bigr) - \sum_\alpha\eta_\alpha\Bigl(\sum_ip_iA_\alpha(i) - \bar A_\alpha\Bigr) .
> $$
>
> **Step 2** (stationarity). $\partial\mathcal L/\partial p_i = -(\ln p_i + 1) - \lambda_0 - \sum_\alpha\eta_\alpha A_\alpha(i) = 0$, so $p_i^\ast = e^{-1-\lambda_0}\exp[-\sum_\alpha\eta_\alpha A_\alpha(i)]$.
>
> **Step 3** (normalization). $1 = e^{-1-\lambda_0}Z$, so $e^{-1-\lambda_0} = 1/Z$, that is $\lambda_0 = \ln Z - 1$.
>
> **Step 4** (means). $-\partial_{\eta_\alpha}\ln Z = \frac1Z\sum_iA_\alpha(i)e^{-\sum_\gamma\eta_\gamma A_\gamma(i)} = \sum_ip_i^\ast A_\alpha(i)$, which must equal $\bar A_\alpha$.
>
> **Step 5** (maximum, unique). $H$ is strictly concave on the probability simplex: its second variation is $\delta^2H = -\sum_i(\delta p_i)^2/p_i < 0$ for every nonzero $\delta p$ with $p_i > 0$. The constraints are linear, so they cut out a convex set, and a stationary point of a strictly concave function on a convex set is its unique global maximum.

^der-c4a-3-2

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^pr-c4a-3-1|Principle §C4a.3.1]]

> [!example] Example §C4a.3.1: Lagrange Multipliers: a Bead on a Circular Wire
> A bead of mass $m$ slides on a vertical circular wire of radius $R$; find the extremes of $U = mgy$ subject to $q(x, y) = x^2 + y^2 = R^2$.
>
> 1. **Geometry.** Level curves of $q$ are circles and those of $U$ are horizontal lines. Where a line of constant $U$ crosses the wire, the bead can move along the wire to raise or lower $U$; the extremes are where a line of constant $U$ is tangent to the wire.
> 2. **Why $d\mathcal L = 0$ means tangency.** With $\mathcal L(x, y, \lambda) = U - \lambda(q - R^2)$ and $x$, $y$, $\lambda$ independent,
>
> $$
> d\mathcal L = \Bigl(\frac{\partial U}{\partial x} - \lambda\frac{\partial q}{\partial x}\Bigr)dx + \Bigl(\frac{\partial U}{\partial y} - \lambda\frac{\partial q}{\partial y}\Bigr)dy - (q - R^2)\,d\lambda = 0
> $$
>
> for all $dx$, $dy$, $d\lambda$ gives $\nabla U = \lambda\nabla q$ and $q = R^2$. Each gradient is normal to its own level curve, so parallel gradients mean tangent curves; $\lambda$ lets their sizes and signs differ. Mechanically, the force along the wire vanishes.
> 3. **Solution.** $0 = 2\lambda x$, $mg = 2\lambda y$, $x^2 + y^2 = R^2$. Since $mg \neq 0$, $\lambda \neq 0$, so $x = 0$ and $y = \pm R$: the minimum $-mgR$ at the bottom, the maximum $mgR$ at the top.
>
> In MaxEnt the variables are the $p_i$, and normalization and the prescribed means play the wire.
>
> *Source: Mao §4.3.3, box "Lagrange multipliers: a bead on a circular wire"*

^ex-c4a-3-1

![[ph-th-c4a-3-1.svg]]

*Figure: the bead of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^ex-c4a-3-1|Example §C4a.3.1]]. Lines of constant $U$ cross the wire except at the top and bottom, where they touch it and $\nabla U \parallel \nabla q$; at a generic point (grey) the two gradients point in different directions.*

> [!remark]- Connections
> - Whether the maximum of an information measure is the thermodynamic entropy is a physical question, answered by counting many copies — [[§C4a.4 Why the Maximum Is Thermodynamic Entropy|§C4a.4]].
> - With the energy as the only mean, the multiplier is $\beta$ and the distribution is the canonical one — [[§C4a.5 The Canonical and Grand-Canonical Ensembles|§C4a.5]].
> - The polymer of Problem Set 5 is a MaxEnt problem with a prescribed mean length — [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-2|Example §C4a.11.2]].
