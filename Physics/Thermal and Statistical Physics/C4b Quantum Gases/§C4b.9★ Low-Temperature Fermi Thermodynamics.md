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
> \int_0^\infty\frac{\phi(x)\,dx}{e^{x-\xi} + 1} = \int_0^\xi\phi(x)\,dx + \frac{\pi^2}6\phi'(\xi) + \frac{7\pi^4}{360}\phi'''(\xi) + \cdots, \qquad G_q(e^\xi) = \frac{\xi^q}{\Gamma(q + 1)}\Bigl[1 + \frac{\pi^2q(q - 1)}{6\xi^2} + O(\xi^{-4})\Bigr] .
> $$
>
> The expansion is in powers of $1/\xi = k_BT/\mu$. The dilute series $G_q(z) = \sum_j(-1)^{j+1}z^j/j^q$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 1) is useless here: it has radius of convergence $1$, and $z = e^\xi \gg 1$.
>
> *Model:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]] for fermions; *applies:* $\xi \gg 1$, $\phi$ smooth on $(0, \infty)$ and of at most power growth; the omitted terms are $O(\xi^{-6})$ relative, plus exponentially small pieces $O(\xi^ne^{-\xi/2})$.
>
> *Source: Mao §4.6.8, eq. (4.163) · level-B home: [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-3|Theorem §B13.1.3]]*

^thm-c4b-9-1

> [!derivation]- Derivation
> **Step 1** (split at $\xi$). With $f(x) = 1/(e^{x-\xi} + 1)$, $\int_0^\infty\phi f = \int_0^\xi\phi - \int_0^\xi\phi(1 - f) + \int_\xi^\infty\phi f$. Put $x = \xi - t$ in the second integral and $x = \xi + t$ in the third, and use $1 - f(\xi - t) = f(\xi + t) = 1/(e^t + 1)$:
>
> $$
> \int_0^\infty\phi f = \int_0^\xi\phi\,dx + \int_0^\xi\frac{\phi(\xi + t) - \phi(\xi - t)}{e^t + 1}\,dt + \int_\xi^\infty\frac{\phi(\xi + t)}{e^t + 1}\,dt .
> $$
>
> The last term is $O(\xi^ne^{-\xi})$ for $\phi$ of power growth.
>
> **Step 2** (expand, then extend). Split the middle integral at $t = \xi/2$. For $t > \xi/2$ the factor $1/(e^t + 1) < e^{-\xi/2}$ makes the piece $O(\xi^ne^{-\xi/2})$. For $t < \xi/2$, $\phi(\xi \pm t)$ is evaluated on $[\xi/2, 3\xi/2]$, where Taylor's theorem applies; the difference is odd in $t$:
>
> $$
> \phi(\xi + t) - \phi(\xi - t) = 2t\,\phi'(\xi) + \frac{t^3}3\phi'''(\xi) + O(t^5\phi^{(5)}) .
> $$
>
> Now the integrands are polynomials times $1/(e^t + 1)$, so extending $\int_0^{\xi/2}$ to $\int_0^\infty$ again costs only $O(\xi^ne^{-\xi/2})$.
>
> **Step 3** (the constants). $\frac1{e^t + 1} = \sum_{j\ge1}(-1)^{j+1}e^{-jt}$ for $t > 0$, so $\int_0^\infty\frac{t^{s-1}dt}{e^t + 1} = \Gamma(s)\sum_j\frac{(-1)^{j+1}}{j^s} = \Gamma(s)(1 - 2^{1-s})\zeta(s)$. At $s = 2$: $\tfrac12\zeta(2) = \frac{\pi^2}{12}$; at $s = 4$: $6\cdot\tfrac78\cdot\frac{\pi^4}{90} = \frac{7\pi^4}{120}$ ([[§B10.2 Quantum and Classical Ideal Gases#^def-b10-2-2|Def. §B10.2.2]] for $\zeta(2) = \pi^2/6$, $\zeta(4) = \pi^4/90$). Hence $2\phi'\cdot\frac{\pi^2}{12} = \frac{\pi^2}6\phi'$ and $\frac13\phi'''\cdot\frac{7\pi^4}{120} = \frac{7\pi^4}{360}\phi'''$.
>
> **Step 4** ($G_q$). With $\phi = x^{q-1}/\Gamma(q)$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]]): $\int_0^\xi\phi = \xi^q/\Gamma(q + 1)$ and $\frac{\pi^2}6\phi'(\xi) = \frac{\pi^2(q - 1)\xi^{q-2}}{6\Gamma(q)} = \frac{\xi^q}{\Gamma(q + 1)}\cdot\frac{\pi^2q(q - 1)}{6\xi^2}$. The $\phi'''$ term is $\propto\xi^{q-4}$, which is the $O(\xi^{-4})$.

^der-c4b-9-1

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^def-c4b-4-4|Def. §C4b.4.4]], [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]]

> [!theorem] Theorem §C4b.9.2: Low-Temperature Fermi Gas
> At fixed $N$, $V$, to order $(T/T_F)^2$,
>
> $$
> \mu(T) = E_F\Bigl[1 - \frac{\pi^2}{12}\Bigl(\frac{T}{T_F}\Bigr)^2\Bigr], \qquad U(T) = \frac35NE_F\Bigl[1 + \frac{5\pi^2}{12}\Bigl(\frac{T}{T_F}\Bigr)^2\Bigr], \qquad \frac{C_V}{Nk_B} = \frac{\pi^2}2\frac{T}{T_F} = \frac{\pi^2}{3}\frac{g(E_F)k_B^2T}{Nk_B} ,
> $$
>
> with $pV = \tfrac23U$. For any smooth density of states the shift is
>
> $$
> \mu - E_F = -\frac{\pi^2}{6}(k_BT)^2\frac{g'(E_F)}{g(E_F)} ,
> $$
>
> negative when $g$ increases at $E_F$, as for $g \propto \epsilon^{1/2}$.
>
> *Model:* the Setup; *applies:* $T \ll T_F$ (for $T \gg T_F$, $z \ll 1$ and [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-2|Theorem §C4b.5.2]] holds instead).
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
> **Step 2** ($\mu$). At $T = 0$, $N = \tfrac23AE_F^{3/2}$. Put $\mu = E_F + \delta\mu$, expand to first order, and inside the already small correction replace $k_BT/\mu$ by $k_BT/E_F = T/T_F$ (the difference is of higher order): $0 = \tfrac32\frac{\delta\mu}{E_F} + \frac{\pi^2}8\bigl(\frac T{T_F}\bigr)^2$, so $\delta\mu/E_F = -\frac{\pi^2}{12}(T/T_F)^2$.
>
> **Step 2′** (general $g$). [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-1|Theorem §C4b.9.1]] with $x = \epsilon/k_BT$ and $\phi(x) = k_BT\,g(k_BTx)$ gives $N = \int_0^\mu g\,d\epsilon + \frac{\pi^2}6(k_BT)^2g'(\mu) + \cdots$. Equating to $N = \int_0^{E_F}g\,d\epsilon$: $g(E_F)\,\delta\mu + \frac{\pi^2}6(k_BT)^2g'(E_F) = 0$ to this order. For $g \propto \epsilon^{1/2}$, $g'/g = 1/(2E_F)$, recovering Step 2.
>
> **Step 3** ($U$). $\mu^{5/2} = E_F^{5/2}[1 + \tfrac52\delta\mu/E_F]$, so the $T^2$ coefficient of $U/U(0)$ is $\frac{5\pi^2}8 - \frac52\cdot\frac{\pi^2}{12} = \frac{5\pi^2}{12}$; the second term is the contribution of the shift of $\mu$. $U(0) = \tfrac25AE_F^{5/2} = \tfrac35NE_F$.
>
> **Step 4** ($C_V$). $\partial_T$ of $\frac35NE_F\cdot\frac{5\pi^2}{12}T^2/T_F^2$ gives $\frac{\pi^2}2Nk_BT/T_F$. With $g(E_F) = \frac32N/E_F$, $\frac{\pi^2}3g(E_F)k_B^2T = \frac{\pi^2}2Nk_B\frac{k_BT}{E_F}$, the same.

^der-c4b-9-2

*Uses:* [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], [[§C4b.9★ Low-Temperature Fermi Thermodynamics#^thm-c4b-9-1|Theorem §C4b.9.1]], [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]]

> [!remark]- Connections
> - $C_V$ and the Pauli susceptibility both measure $g(E_F)$ — [[§B13.1★ The Degenerate Fermi Gas and Metals#^thm-b13-1-5|Theorem §B13.1.5]]; the measured linear term $\gamma T$ of metals — [[§B11.2★ Phonons and the Debye Model#^law-b11-2-3|Law §B11.2.3]].
> - The structure "a step plus a correction from its rounding" recurs wherever a Fermi function is integrated against a smooth function.
