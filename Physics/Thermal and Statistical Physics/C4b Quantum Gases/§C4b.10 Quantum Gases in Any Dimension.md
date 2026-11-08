---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4b
section: C4b.10
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4b.9★ Low-Temperature Fermi Thermodynamics]] · ↑ [[· C4b Quantum Gases]]

*Sources: PHY 510 Problem Set 6 (a quantum-gas comparison table), with official solution (Mao, Fall 2026).*

*Quantum-gas chain:* [[§C4b.3 Summing over Orbitals: the Density of States#^thm-c4b-3-3|Theorem §C4b.3.3]] → [[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]] → [[§C4b.5 Massive Gases and the Classical Limit#^thm-c4b-5-1|Theorem §C4b.5.1]] → [[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-3|Theorem §C4b.7.3]] → [[§C4b.8 The Degenerate Fermi Gas#^thm-c4b-8-1|Theorem §C4b.8.1]] → this section.

Everything in the chapter depends on the dispersion and the dimension only through one number, the exponent $\nu$ of the density of states $g(\epsilon) = A\epsilon^{\nu-1}$. The problem set builds the table that shows this, for $d = 1$ to $4$ and quadratic or linear dispersion, and derives every relation once for general $\nu$.

**Setup.** A periodic box of side $L$ in $d$ dimensions, $V_d = L^d$, $\rho_d = N/V_d$, $g_s$ internal states, no interactions, conserved $N$ (also for the linear dispersion here), lowest energy $0$, continuum for excited orbitals, condensate kept separately. Dispersion $\epsilon = bk^s$: $s = 2$, $b = \hbar^2/(2m)$, or $s = 1$, $b = \hbar c$.

> [!example] Example §C4b.10.1: Density of States in $d$ Dimensions
> 1. **Dispersions.** A plane wave in $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi$ gives $\epsilon = \hbar^2k^2/(2m)$; in $\partial_t^2\phi = c^2\nabla^2\phi$ the positive branch gives $\epsilon = \hbar ck$.
> 2. **Count.** Cells of volume $(2\pi/L)^d$ and a shell of volume $S_{d-1}k^{d-1}dk$, with $S_0 = 2$, $S_1 = 2\pi$, $S_2 = 4\pi$, $S_3 = 2\pi^2$:
>
> $$
> g(\epsilon) = A\epsilon^{\nu-1}, \qquad \nu = \frac ds, \qquad A = \frac{g_sV_dS_{d-1}}{(2\pi)^ds}\,b^{-d/s} .
> $$
>
> In one dimension $S_0 = 2$ counts $+k$ and $-k$.
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
> $\nu$ does not depend on the statistics. The number uses $G_\nu$; $\ln\Xi$, $U$ and $p_d$ use $G_{\nu+1}$ ([[§C4b.4 The Grand Partition Function and Polylogarithms#^thm-c4b-4-3|Theorem §C4b.4.3]], which holds for any $\nu > 0$).
>
> *Source: PHY 510 Problem Set 6, parts (a)–(b), official solution*

^ex-c4b-10-1

> [!example] Example §C4b.10.2: The Thermal Wavelength for Any Dispersion
> Define $\lambda_T$ by writing the classical number equation as $N_{\text{cl}} \simeq zg_sV_d/\lambda_T^d$. With $N_{\text{cl}} = zA\Gamma(\nu)(k_BT)^\nu$ ($G_\nu \simeq z$),
>
> $$
> \lambda_T^d = \frac{g_sV_d}{A\Gamma(\nu)(k_BT)^\nu}, \qquad \lambda_T = 2\pi\Bigl(\frac{s}{S_{d-1}\Gamma(d/s)}\Bigr)^{1/d}\Bigl(\frac{b}{k_BT}\Bigr)^{1/s} .
> $$
>
> For $s = 2$ this is $h/\sqrt{2\pi mk_BT}$ in every dimension ([[§C4b.5 Massive Gases and the Classical Limit#^def-c4b-5-1|Def. §C4b.5.1]]); for $s = 1$ it gives the dimension-dependent prefactors of the table, fixed by the normalization of the classical number equation.
>
> *Source: PHY 510 Problem Set 6, part (d), official solution*

^ex-c4b-10-2

> [!example] Example §C4b.10.3: Thermodynamics for General $\nu$
> | regime | relations |
> | --- | --- |
> | any degeneracy | $U = \nu p_dV_d$, $\Phi = -p_dV_d$ |
> | classical, $\rho_d\lambda_T^d/g_s \ll 1$ | $z \simeq \rho_d\lambda_T^d/g_s$, $\mu \simeq k_BT\ln(\rho_d\lambda_T^d/g_s)$, $p_dV_d = Nk_BT$, $U = \nu Nk_BT$, $C_V = \nu Nk_B$ |
> | fermions at $T = 0$ | $E_F = (\nu N/A)^{1/\nu}$, $U(0)/N = \frac{\nu}{\nu + 1}E_F$, $p_d(0)V_d/N = \frac{E_F}{\nu + 1}$ |
> | BEC onset | $\nu > 1$; $k_BT_c = \bigl(\frac{N}{A\Gamma(\nu)\zeta(\nu)}\bigr)^{1/\nu}$; none for $0 < \nu \le 1$ |
> | bosons below $T_c$ | $\mu = 0$, $N_0/N = 1 - (T/T_c)^\nu$ |
>
> The classical criterion $\rho_d\lambda_T^d/g_s \ll 1$ is $\lambda_T \ll (g_s/\rho_d)^{1/d}$: many thermally accessible orbitals per particle. It implies $\beta(\epsilon - \mu) \gg 1$ for all $\epsilon \ge 0$, which the continuum approximation alone does not. At $T = 0$, $N = \frac A\nu E_F^\nu$ and $U(0) = \frac{A}{\nu + 1}E_F^{\nu+1}$. For BEC, the integrand $g/(e^{\beta\epsilon} - 1) \simeq A\epsilon^{\nu-2}/\beta$ is integrable at $0$ only if $\nu > 1$ ([[§C4b.7 Bose–Einstein Condensation#^thm-c4b-7-4|Theorem §C4b.7.4]]).
>
> *Source: PHY 510 Problem Set 6, parts (c)–(f), official solution*

^ex-c4b-10-3

> [!example] Example §C4b.10.4: Different Systems, Same $\nu$
> The four-dimensional quadratic gas and the two-dimensional linear gas both have $\nu = 2$, with different prefactors $A$:
>
> $$
> k_BT_c^{(4,\text{quad})} = \frac{2\pi\hbar^2}m\Bigl(\frac{\rho_4}{g_s\zeta(2)}\Bigr)^{1/2}, \qquad k_BT_c^{(2,\text{lin})} = \hbar c\Bigl(\frac{2\pi\rho_2}{g_s\zeta(2)}\Bigr)^{1/2} .
> $$
>
> Their transition temperatures differ (even their densities have different units), but every dimensionless relation agrees when measured in each system's own scale: $U = 2p_dV_d$, $C_V^{\text{cl}} = 2Nk_B$, $U_F(0)/NE_F = \tfrac23$, $p_{d,F}(0)V_d/NE_F = \tfrac13$, $N_0/N = 1 - (T/T_c)^2$. The thermodynamics sees only the energies and their multiplicities. Likewise the two-dimensional quadratic gas and the one-dimensional linear gas share $\nu = 1$: a constant density of states and no condensation.
>
> *Source: PHY 510 Problem Set 6, part (g), official solution*

^ex-c4b-10-4

> [!remark]- Connections
> - Level B works the three-dimensional cases of these relations — [[§B10.2 Quantum and Classical Ideal Gases#^thm-b10-2-2|Theorem §B10.2.2]], [[§B12.1★ Bose–Einstein Condensation#^thm-b12-1-3|Theorem §B12.1.3]].
