---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.9
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c, extension]
---
← [[§C4b.8 The Degenerate Fermi Gas]] · ↑ [[· C4b Quantum Gases]] · [[§C4b.10 Quantum Gases in Any Dimension]] →

★ *Optional in PHY 510: Mao marks §4.6.8 as optional.*

*Sources: Mao, PHY 510 notes, §4.6.8, eqs. (4.163)–(4.167).*

The thermal-shell estimate ([[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-2|Theorem §C4b.8.2]]) gives $C_V \sim Nk_BT/T_F$ without a coefficient. The coefficient comes from the polylogarithm that already generates the gas thermodynamics ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]]), evaluated where $\ln z = \mu/k_BT$ is large: the Sommerfeld expansion. One subtlety decides the answer: at fixed $N$ the chemical potential moves with $T$, and that shift contributes to the energy. Level B proves the Sommerfeld expansion directly ([[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-3|Theorem §B13.1.3]]).

**Setup.** Fermions, $G_q(z) = -\operatorname{Li}_q(-z)$; $\xi \equiv \ln z = \mu/k_BT \gg 1$; the three-dimensional gas of [[§C4b.8 The Degenerate Fermi Gas|§C4b.8]].

> [!theorem] Theorem §C4b.9.1: Sommerfeld Expansion of the Fermi Polylogarithm
> $$
> \int_0^\infty\frac{\phi(x)\,dx}{e^{x-\xi} + 1} \sim \int_0^\xi\phi(x)\,dx + \frac{\pi^2}6\phi'(\xi) + \cdots, \qquad G_q(e^\xi) = \frac{\xi^q}{\Gamma(q + 1)}\Bigl[1 + \frac{\pi^2q(q - 1)}{6\xi^2} + O(\xi^{-4})\Bigr] .
> $$
>
> The first term counts the filled states; the correction rounds the step. The small parameter is $1/\xi = k_BT/\mu$; the small-$z$ series does not converge here.
>
> *Model:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]] for fermions; *applies:* $\xi \gg 1$, $\phi$ smooth and of at most power growth.
>
> *Source: Mao §4.6.8, eq. (4.163) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-3|Theorem §B13.1.3]]*

^thm-c4b-9-1

> [!derivation]- Derivation
> **Step 1.** Split at $\xi$: $\int_0^\infty\phi\,f = \int_0^\xi\phi - \int_0^\xi\phi(1 - f) + \int_\xi^\infty\phi f$, with $f = 1/(e^{x-\xi} + 1)$ and $1 - f(\xi - t) = f(\xi + t)$.
>
> **Step 2.** With $x = \xi \mp t$, the last two terms combine to $\int_0^\infty[\phi(\xi + t) - \phi(\xi - t)]\frac{dt}{e^t + 1}$, the lower limit $t = \xi$ pushed to $\infty$ at exponentially small cost.
>
> **Step 3.** $\phi(\xi + t) - \phi(\xi - t) = 2t\phi'(\xi) + O(t^3)$ and $\int_0^\infty\frac{t\,dt}{e^t + 1} = \frac{\pi^2}{12}$, giving $\frac{\pi^2}6\phi'(\xi)$.
>
> **Step 4.** With $\phi = x^{q-1}/\Gamma(q)$: $\int_0^\xi\phi = \xi^q/\Gamma(q + 1)$ and $\frac{\pi^2}6\phi'(\xi) = \frac{\pi^2(q - 1)\xi^{q-2}}{6\Gamma(q)} = \frac{\xi^q}{\Gamma(q + 1)}\cdot\frac{\pi^2q(q - 1)}{6\xi^2}$.

^der-c4b-9-1

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-1|Def. §C4b.4.1]]

> [!theorem] Theorem §C4b.9.2: Low-Temperature Fermi Gas
> At fixed $N$, $V$, to order $(T/T_F)^2$,
>
> $$
> \mu(T) = E_F\Bigl[1 - \frac{\pi^2}{12}\Bigl(\frac{T}{T_F}\Bigr)^2\Bigr], \qquad U(T) = \frac35NE_F\Bigl[1 + \frac{5\pi^2}{12}\Bigl(\frac{T}{T_F}\Bigr)^2\Bigr], \qquad \frac{C_V}{Nk_B} = \frac{\pi^2}2\frac{T}{T_F} ,
> $$
>
> with $pV = \tfrac23U$. Equivalently $C_V = \frac{\pi^2}3g(E_F)k_B^2T$: the heat capacity measures the density of states at the Fermi energy. $\mu$ falls because the three-dimensional density of states grows with energy, so rounding the step at fixed $\mu$ would add more particles above $\mu$ than it removes below.
>
> *Model:* the Setup; *applies:* $T \ll T_F$. For $T \gg T_F$ the classical results of [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-2|Theorem §C4b.5.2]] return.
>
> *Source: Mao §4.6.8, eqs. (4.164)–(4.167) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-4|Theorem §B13.1.4]]*

^thm-c4b-9-2

> [!derivation]- Derivation
> **Step 1** ($N$ and $U$). From [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], $N = A\Gamma(\tfrac32)(k_BT)^{3/2}G_{3/2}(z)$ and $U = A\Gamma(\tfrac52)(k_BT)^{5/2}G_{5/2}(z)$ (recall $U = \nu A\Gamma(\nu)\cdots$ and $\nu\Gamma(\nu) = \Gamma(\nu + 1)$). With [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-1|Theorem §C4b.9.1]], $(k_BT)^q\xi^q = \mu^q$:
>
> $$
> N = \tfrac23A\mu^{3/2}\Bigl[1 + \frac{\pi^2}8\Bigl(\frac{k_BT}\mu\Bigr)^2\Bigr], \qquad U = \tfrac25A\mu^{5/2}\Bigl[1 + \frac{5\pi^2}8\Bigl(\frac{k_BT}\mu\Bigr)^2\Bigr] ,
> $$
>
> from $q(q - 1)/6 = \tfrac18$ at $q = \tfrac32$ and $\tfrac58$ at $q = \tfrac52$.
>
> **Step 2** ($\mu$). At $T = 0$, $N = \tfrac23AE_F^{3/2}$. Put $\mu = E_F + \delta\mu$ and expand to first order: $0 = \tfrac32\frac{\delta\mu}{E_F} + \frac{\pi^2}8\bigl(\frac T{T_F}\bigr)^2$, so $\delta\mu/E_F = -\frac{\pi^2}{12}(T/T_F)^2$.
>
> **Step 3** ($U$). $\mu^{5/2} = E_F^{5/2}[1 + \tfrac52\delta\mu/E_F]$, so the $T^2$ coefficient of $U/U(0)$ is $\frac{5\pi^2}8 - \frac52\cdot\frac{\pi^2}{12} = \frac{5\pi^2}{12}$. Holding $\mu = E_F$ would miss the second term. $U(0) = \tfrac25AE_F^{5/2} = \tfrac35NE_F$.
>
> **Step 4** ($C_V$). $\partial_T$ of $\frac35NE_F\cdot\frac{5\pi^2}{12}T^2/T_F^2$ gives $\frac{\pi^2}2Nk_BT/T_F$. With $g(E_F) = \frac32N/E_F$, $\frac{\pi^2}3g(E_F)k_B^2T = \frac{\pi^2}2Nk_B\frac{k_BT}{E_F}$, the same.

^der-c4b-9-2

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-1|Theorem §C4b.9.1]], [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]]

> [!remark]- Connections
> - Pauli paramagnetism measures the same $g(E_F)$ — [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-5|Theorem §B13.1.5]].
> - The structure "a step plus a correction from its rounding" recurs wherever a Fermi function is integrated against a smooth function.
