---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.10
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.9★ Low-Temperature Fermi Thermodynamics]] · ↑ [[· C4b Quantum Gases]] · [[§C5.1 Complete and Reduced Dynamics]] →

*Sources: PHY 510 Problem Set 6 (a quantum-gas comparison table), with official solution (Mao, Fall 2026); the two tables follow PS6 Solutions, Tables 1–2.*

*Quantum-gas chain:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]] → [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] → [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]] → [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] → [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]] → this section.

Everything in the chapter depends on the dispersion and the dimension only through one number, the exponent $\nu$ of the density of states $g(\epsilon) = A\epsilon^{\nu-1}$. The problem set builds the table that shows this, for $d = 1$ to $4$ and quadratic or linear dispersion, and derives every relation once for general $\nu$.

**Setup.** A periodic box of side $L$ in $d$ dimensions, $V_d = L^d$, $\rho_d = N/V_d$, $g_s$ internal states, no interactions, conserved $N$ (also for the linear dispersion here), lowest energy $0$, continuum for excited orbitals, condensate kept separately. Dispersion $\epsilon = bk^s$: $s = 2$, $b = \hbar^2/(2m)$, or $s = 1$, $b = \hbar c$.

> [!example] Example §C4b.10.1: Density of States in $d$ Dimensions
> 1. **Dispersions.** $e^{i(\mathbf k\cdot\mathbf r - \omega t)}$ in $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi$ gives $\hbar\omega = \hbar^2k^2/(2m)$ ($s = 2$); in $\partial_t^2\phi = c^2\nabla^2\phi$ it gives $\omega^2 = c^2k^2$, and $\omega > 0$ gives $\epsilon = \hbar ck$ ($s = 1$).
> 2. **Count.** As in [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-2|Theorem §C4b.3.2]], one $\mathbf k$ per cell $(2\pi/L)^d$, and the shell $[k, k + dk]$ has volume $S_{d-1}k^{d-1}dk$ ($S_0 = 2$, $S_1 = 2\pi$, $S_2 = 4\pi$, $S_3 = 2\pi^2$), so $g(k)\,dk = \frac{g_sV_d}{(2\pi)^d}S_{d-1}k^{d-1}dk$. In $d = 1$ the "shell" is the two intervals $k > 0$ and $k < 0$, hence $S_0 = 2$.
> 3. **Change variable.** $k = (\epsilon/b)^{1/s}$ gives $k^{d-1}dk = \frac1s\,b^{-d/s}\epsilon^{d/s-1}d\epsilon$, so
>
> $$
> g(\epsilon) = A\epsilon^{\nu-1}, \qquad \nu = \frac ds, \qquad A = \frac{g_sV_dS_{d-1}}{(2\pi)^ds}\,b^{-d/s} .
> $$
>
> 4. **Rows.** E.g. $d = 2$, $s = 2$: $\frac{A}{g_sV_2} = \frac{2\pi}{(2\pi)^2\cdot2}\cdot\frac{2m}{\hbar^2} = \frac{m}{2\pi\hbar^2}$; $d = 3$, $s = 1$: $\frac{4\pi}{(2\pi)^3}(\hbar c)^{-3} = \frac{1}{2\pi^2(\hbar c)^3}$. The $\lambda_T$ column is [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-2|Example §C4b.10.2]], the BEC column [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-3|Example §C4b.10.3]] (bosons, uniform box, thermodynamic limit).
>
> | $d$ | $\epsilon(k)$ | $\nu$ | $g(\epsilon)/(g_sV_d)$ | $\lambda_T$ | BEC at $T > 0$ |
> | --- | --- | --- | --- | --- | --- |
> | 1 | $\hbar^2k^2/2m$ | $\tfrac12$ | $\frac1\pi\sqrt{\frac{m}{2\hbar^2}}\,\epsilon^{-1/2}$ | $h/\sqrt{2\pi mk_BT}$ | no |
> | 2 | $\hbar^2k^2/2m$ | $1$ | $\frac{m}{2\pi\hbar^2}$ | $h/\sqrt{2\pi mk_BT}$ | no |
> | 3 | $\hbar^2k^2/2m$ | $\tfrac32$ | $\frac1{4\pi^2}\bigl(\frac{2m}{\hbar^2}\bigr)^{3/2}\epsilon^{1/2}$ | $h/\sqrt{2\pi mk_BT}$ | yes |
> | 4 | $\hbar^2k^2/2m$ | $2$ | $\frac{m^2}{4\pi^2\hbar^4}\,\epsilon$ | $h/\sqrt{2\pi mk_BT}$ | yes |
> | 1 | $\hbar ck$ | $1$ | $\frac1{\pi\hbar c}$ | $\pi\hbar c/k_BT$ | no |
> | 2 | $\hbar ck$ | $2$ | $\frac{\epsilon}{2\pi(\hbar c)^2}$ | $\sqrt{2\pi}\,\hbar c/k_BT$ | yes |
> | 3 | $\hbar ck$ | $3$ | $\frac{\epsilon^2}{2\pi^2(\hbar c)^3}$ | $\pi^{2/3}\hbar c/k_BT$ | yes |
> | 4 | $\hbar ck$ | $4$ | $\frac{\epsilon^3}{8\pi^2(\hbar c)^4}$ | $(4\pi^2/3)^{1/4}\hbar c/k_BT$ | yes |
>
> Since $\nu$ comes from $d$ and $s$ alone, the same $\nu$ serves bosons and fermions, and [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] (valid for every $\nu > 0$) assigns the orders: $G_\nu$ in $N$, $G_{\nu+1}$ in $\ln\Xi$, $U$ and $p_d$.
>
> *Source: PHY 510 Problem Set 6, parts (a)–(b), official solution, Table 1*

^ex-c4b-10-1

> [!example] Example §C4b.10.2: The Thermal Wavelength for Any Dispersion
> 1. **Classical number equation.** For $z \ll 1$, $f \simeq ze^{-\beta\epsilon}$ ([[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]]), so $N_{\text{cl}} = zA\int_0^\infty\epsilon^{\nu-1}e^{-\beta\epsilon}d\epsilon = zA\Gamma(\nu)(k_BT)^\nu$.
> 2. **Definition.** $\lambda_T$ is the length for which $N_{\text{cl}} = zg_sV_d/\lambda_T^d$, i.e. $\lambda_T^d = g_sV_d/[A\Gamma(\nu)(k_BT)^\nu]$.
> 3. **Insert $A$** of [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]]: $g_sV_d$ cancels and $\lambda_T^d = \frac{(2\pi)^d s}{S_{d-1}\Gamma(d/s)}\bigl(\frac{b}{k_BT}\bigr)^{d/s}$, so
>
> $$
> \lambda_T = 2\pi\Bigl(\frac{s}{S_{d-1}\Gamma(d/s)}\Bigr)^{1/d}\Bigl(\frac{b}{k_BT}\Bigr)^{1/s} .
> $$
>
> 4. **Check $s = 2$.** With $S_{d-1} = 2\pi^{d/2}/\Gamma(d/2)$, $(2/(S_{d-1}\Gamma(d/2)))^{1/d} = \pi^{-1/2}$, and $\lambda_T = 2\sqrt\pi\,\hbar/\sqrt{2mk_BT} = h/\sqrt{2\pi mk_BT}$ in every $d$ ([[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]]).
> 5. **$s = 1$.** E.g. $d = 3$: $2\pi(1/(4\pi\cdot2))^{1/3} = \pi^{2/3}$. For a linear dispersion there is no earlier $\lambda_T$ to match; step 2 is what fixes the prefactors in the table.
>
> *Source: PHY 510 Problem Set 6, part (d), official solution*

^ex-c4b-10-2

> [!example] Example §C4b.10.3: Thermodynamics for General $\nu$
> | regime | condition | relations |
> | --- | --- | --- |
> | any degeneracy | bulk continuum | $U = \nu p_dV_d$, $\Phi = -p_dV_d$ |
> | classical | $\rho_d\lambda_T^d/g_s \ll 1$ | $z \simeq \rho_d\lambda_T^d/g_s$, $\mu \simeq k_BT\ln(\rho_d\lambda_T^d/g_s)$, $p_dV_d = Nk_BT$, $U = \nu Nk_BT$, $C_V = \nu Nk_B$ |
> | fermions | $T = 0$ | $E_F = (\nu N/A)^{1/\nu}$, $U(0)/N = \frac{\nu}{\nu + 1}E_F$, $p_d(0)V_d/N = \frac{E_F}{\nu + 1}$ |
> | BEC onset | bosons, $\nu > 1$, uniform box, thermodynamic limit at fixed $\rho_d$ | $k_BT_c = \bigl(\frac{N}{A\Gamma(\nu)\zeta(\nu)}\bigr)^{1/\nu}$; none for $0 < \nu \le 1$ |
> | bosons below $T_c$ | $\nu > 1$, $T < T_c$, bulk | $\mu = 0$, $N_0/N = 1 - (T/T_c)^\nu$ |
>
> Derivations, row by row:
>
> 1. **Any degeneracy.** [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] for general $\nu > 0$: $\ln\Xi = A\Gamma(\nu)\beta^{-\nu}G_{\nu+1}$, $U = \nu A\Gamma(\nu)\beta^{-\nu-1}G_{\nu+1}$, $p_dV_d = A\Gamma(\nu)\beta^{-\nu-1}G_{\nu+1}$; compare.
> 2. **Classical.** Step 1 of [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-2|Example §C4b.10.2]] gives $z \simeq \rho_d\lambda_T^d/g_s$ and $\mu = k_BT\ln z$. With $G_{\nu+1} \simeq z$ too, $\ln\Xi \simeq N$, so $p_dV_d = k_BT\ln\Xi = Nk_BT$, $U = \nu Nk_BT$, $C_V = \nu Nk_B$. The criterion reads $\lambda_T \ll (g_s/\rho_d)^{1/d}$, and it gives $\beta(\epsilon - \mu) \ge -\ln z \gg 1$ at every $\epsilon$. Replacing sums by integrals ([[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-4|Theorem §C4b.3.4]]) is a separate approximation, about level spacing, and holds also in the degenerate rows.
> 3. **Fermions at $T = 0$.** Filling to $E_F$: $N = \int_0^{E_F}A\epsilon^{\nu-1}d\epsilon = \frac A\nu E_F^\nu$, solved for $E_F$; $U(0) = \int_0^{E_F}A\epsilon^\nu d\epsilon = \frac{A}{\nu + 1}E_F^{\nu+1}$, divided by $N$; $p_d(0)V_d = U(0)/\nu$ by row 1.
> 4. **BEC onset.** Near $\epsilon = 0$, $g/(e^{\beta\epsilon} - 1) \simeq A\epsilon^{\nu-2}/\beta$: integrable iff $\nu > 1$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-4|Theorem §C4b.7.4]]); at $\nu = 1$ the excited capacity diverges like $\ln$, for $\nu < 1$ like a power, so $\mu < 0$ can always absorb $N$. For $\nu > 1$, $N_{\text{ex}}^{\max} = A\Gamma(\nu)(k_BT)^\nu\zeta(\nu)$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-2|Theorem §C4b.4.2]], part 4); set it equal to $N$ at $T_c$.
> 5. **Below $T_c$.** $N_{\text{ex}} = N_{\text{ex}}^{\max}(T) = N(T/T_c)^\nu$ and $N_0 = N - N_{\text{ex}}$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-2|Theorem §C4b.7.2]]).
>
> *Source: PHY 510 Problem Set 6, parts (c)–(f), official solution, Table 2*

^ex-c4b-10-3

> [!example] Example §C4b.10.4: Different Systems, Same $\nu$
> **The pair $\nu = 2$:** the four-dimensional quadratic gas and the two-dimensional linear gas.
>
> 1. **Prefactors** ([[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-1|Example §C4b.10.1]]): $A_{4,\text{quad}} = g_sV_4m^2/(4\pi^2\hbar^4)$ and $A_{2,\text{lin}} = g_sV_2/(2\pi(\hbar c)^2)$.
> 2. **$T_c$** from [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-3|Example §C4b.10.3]], row 4, with $\Gamma(2) = 1$:
>
> $$
> k_BT_c^{(4,\text{quad})} = \Bigl(\frac{4\pi^2\hbar^4\rho_4}{g_sm^2\zeta(2)}\Bigr)^{1/2} = \frac{2\pi\hbar^2}m\Bigl(\frac{\rho_4}{g_s\zeta(2)}\Bigr)^{1/2}, \qquad k_BT_c^{(2,\text{lin})} = \hbar c\Bigl(\frac{2\pi\rho_2}{g_s\zeta(2)}\Bigr)^{1/2} .
> $$
>
> 3. **What agrees.** $\nu$ fixes the energy dependence of $g$, $A$ only its scale. So the two $T_c$ are different functions of densities with different units ($\text{m}^{-4}$, $\text{m}^{-2}$); nothing forces them to be equal, though particular densities could make them so. Comparing bosons with bosons and fermions with fermions, every dimensionless ratio of [[§C4b.10 Quantum Gases in Any Dimension#^ex-c4b-10-3|Example §C4b.10.3]] at $\nu = 2$ is the same once each gas is measured in its own $T_c$ or $E_F$: $U = 2p_dV_d$, $C_V^{\text{cl}} = 2Nk_B$, $U_F(0)/NE_F = \tfrac23$, $p_{d,F}(0)V_d/NE_F = \tfrac13$, $N_0/N = 1 - (T/T_c)^2$. The reason is that every sum over orbitals sees only $g(\epsilon)$.
>
> **The pair $\nu = 1$:** the two-dimensional quadratic and one-dimensional linear gases both have a constant $g$, so by row 4 neither condenses at $T > 0$ (uniform box, thermodynamic limit).
>
> *Source: PHY 510 Problem Set 6, part (g), official solution*

^ex-c4b-10-4

> [!remark]- Connections
> - Level B works the three-dimensional cases of these relations — [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-2|Theorem §B10.2.2]], [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-3|Theorem §B12.1.3]].
