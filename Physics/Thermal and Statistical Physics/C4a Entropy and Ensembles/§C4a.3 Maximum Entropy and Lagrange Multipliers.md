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

A prescribed mean energy is a single linear condition on the $p_i$, met by a whole family of distributions. Jaynes's rule of inference selects the member of largest entropy ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^pr-c4a-3-1|Principle §C4a.3.1]]); information enters either by removing states or by fixing means ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^cau-c4a-3-1|§C4a.3, Caution: Restricting the states versus prescribing a mean]]); and Lagrange multipliers solve the general problem ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]). Level B stated the same principle as a remark and solved its main cases ([[§B6.3 Entropy, Information and the Gibbs Paradox#^rem-b6-3-2|Remark: The maximum-entropy principle]], [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-4|Theorem §B6.3.4]]); here it is the starting point of the ensembles.

**Setup.** A fixed set of allowed microstates $i$, with the values $A_\alpha(i)$ of some observables in each, and the entropy $H[p] = -\sum_ip_i\ln p_i$ of [[§C4a.2 The Entropy of a Statistical State#^def-c4a-2-1|Def. §C4a.2.1]]. External parameters such as $V$ are held fixed.

## The principle

> [!principle] Principle §C4a.3.1: Jaynes's Maximum-Entropy Principle
> Let the available information define a set $\mathcal C$ of compatible distributions. Assign
>
> $$
> p^\ast = \arg\max_{p\in\mathcal C}H[p] ,
> $$
>
> and in quantum mechanics
>
> $$
> \hat\rho^\ast = \arg\max\bigl\{H_{\text{vN}}[\hat\rho] : \hat\rho \ge 0,\ \operatorname{Tr}\hat\rho = 1,\ \operatorname{Tr}\hat\rho\hat A_\alpha = \bar A_\alpha\bigr\} .
> $$
>
> Any other member of $\mathcal C$ has lower entropy, so it asserts more about the microstate than the data contain.
>
> *Domain:* inference from macroscopic data. Fixed beforehand:
> - the list of microstates, each counted once even when several share an energy;
> - classically, the measure $d\Gamma$ ([[§C4a.2 The Entropy of a Statistical State#^cau-c4a-2-1|§C4a.2, Caution: The reference measure must be fixed]]).
>
> *Source: Mao §4.3.1, box "Jaynes's maximum-entropy principle (MaxEnt)" · Jaynes (1957), §2–§3; II, §10 · Lecture 9/24*

^pr-c4a-3-1

> [!caution] Caution: Restricting the states versus prescribing a mean
> | kind of information | what it changes | example |
> | --- | --- | --- |
> | **restriction** | the index set of $\sum_i$ | exact $N$: other particle numbers are not in the set |
> | **mean constraint** | a linear condition on the $p_i$, i.e. a hyperplane in the simplex | $\sum_ip_iE_i = U$, with every $E_i$ still allowed |
>
> Treating one kind as the other gives a different ensemble ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^def-c4a-3-1|Def. §C4a.3.1]]).

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
> *Model:* a fixed set of allowed states; *applies:* $Z(\eta)$ finite and $(\bar A_\alpha)$ inside the range of attainable means; at an endpoint such as $U = E_{\min}$ no finite $\eta$ exists and the maximizer lives on a subset of the states.
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
> **Step 5** (maximum, unique). Let $q$ be any distribution on the allowed states meeting the constraints. Since every $p_i^\ast > 0$, Gibbs' inequality [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]] gives
>
> $$
> H[q] \le -\sum_iq_i\ln p_i^\ast = \sum_iq_i\Bigl[\ln Z + \sum_\alpha\eta_\alpha A_\alpha(i)\Bigr] = \ln Z + \sum_\alpha\eta_\alpha\bar A_\alpha = H[p^\ast] ,
> $$
>
> with equality iff $q = p^\ast$. The last equality is the same computation with $q = p^\ast$. This covers countably many states as well.

^der-c4a-3-2

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^pr-c4a-3-1|Principle §C4a.3.1]], [[§C4a.2 The Entropy of a Statistical State#^def-c4a-2-1|Def. §C4a.2.1]], [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]]

> [!example] Example §C4a.3.1: Lagrange Multipliers: a Bead on a Circular Wire
> A bead of mass $m$ slides on a vertical circular wire of radius $R$; find the extremes of $U = mgy$ subject to $q(x, y) = x^2 + y^2 = R^2$.
>
> 1. **Direct route.** On the wire $x = R\sin\theta$, $y = -R\cos\theta$, so $U(\theta) = -mgR\cos\theta$ and $dU/d\theta = mgR\sin\theta$ vanishes at $\theta = 0$ (bottom) and $\theta = \pi$ (top).
> 2. **Multiplier route.** With $\mathcal L(x, y, \lambda) = U - \lambda(q - R^2)$ and $x$, $y$, $\lambda$ independent,
>
> $$
> d\mathcal L = \Bigl(\frac{\partial U}{\partial x} - \lambda\frac{\partial q}{\partial x}\Bigr)dx + \Bigl(\frac{\partial U}{\partial y} - \lambda\frac{\partial q}{\partial y}\Bigr)dy - (q - R^2)\,d\lambda = 0
> $$
>
> for all $dx$, $dy$, $d\lambda$ gives $\nabla U = \lambda\nabla q$ and $q = R^2$.
> 3. **The two routes agree.** The wire's tangent is $t = \partial_\theta(x, y)/R = (\cos\theta, \sin\theta)$, and $\nabla q = 2(x, y) \perp t$, $\nabla q \ne 0$. In the plane, $\nabla U = \lambda\nabla q$ for some $\lambda$ iff $\nabla U\cdot t = 0$, and $\nabla U\cdot t = R^{-1}dU/d\theta$.
> 4. **Solution.** $0 = 2\lambda x$, $mg = 2\lambda y$, $x^2 + y^2 = R^2$. Since $mg \neq 0$, $\lambda \neq 0$, so $x = 0$ and $y = \pm R$: the minimum $-mgR$ at the bottom, the maximum $mgR$ at the top.
>
> [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] is the multiplier route with $(p_i)$ for $(x, y)$ and the $1 + r$ linear constraints for $q = R^2$.
>
> *Source: Mao §4.3.3, box "Lagrange multipliers: a bead on a circular wire"*

^ex-c4a-3-1

![[ph-th-c4a-3-1.svg]]

*Figure: the bead of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^ex-c4a-3-1|Example §C4a.3.1]]. Lines of constant $U$ cross the wire except at the top and bottom, where they touch it and $\nabla U \parallel \nabla q$; at a generic point (grey) the two gradients point in different directions.*

> [!remark]- Connections
> - Whether the maximum of an information measure is the thermodynamic entropy is a physical question, answered by counting many copies — [[§C4a.4 Why the Maximum Is Thermodynamic Entropy|§C4a.4]].
> - With the energy as the only mean, the multiplier is $\beta$ and the distribution is the canonical one — [[§C4a.5 The Canonical and Grand-Canonical Ensembles|§C4a.5]].
> - The polymer of Problem Set 5 is a MaxEnt problem with a prescribed mean length — [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-2|Example §C4a.11.2]].
