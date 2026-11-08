---
type: convention
source: "PHY 510 (Mao)"
---
# Mao PHY 510

Conventions of level C of [[Thermal and Statistical Physics]], as in Mao's PHY 510 notes, compared with the problem-set solutions and with levels A and B. New rows are added as chapters are written.

| Item | Level C (Mao's notes) | Elsewhere |
| --- | --- | --- |
| Inexact differential | $\delta Q$, $\delta W$ ([[§C1.1 Systems, Equilibrium and the First Two Laws#^cau-c1-1-3\|§C1.1, Caution on d and δ]]) | levels A, B: $đQ$, $đW$ |
| Sign of work | $\delta W$ is work done **on** the system: $dU = \delta Q + \delta W$ ([[§C1.1 Systems, Equilibrium and the First Two Laws#^pr-c1-1-4\|Principle §C1.1.4]]; signs at [[§C1.1 Systems, Equilibrium and the First Two Laws#^cau-c1-1-2\|§C1.1, Caution: Sign of the work, and of the bar]]) | levels A, B: $\Delta U = Q - W$ with $W$ by the system; PS1 official solutions also use by-the-system in places |
| Pressure | $p$ | PS statements: $P$ |
| Generalized forces | $\delta W_{\text{rev}} = \sum_iY_i\,dX_i$, gas: $Y = -p$ ([[§C1.2 The Equilibrium Manifold and the Heat One-Form#^def-c1-2-2\|Def. §C1.2.2]]) | level B: $X\,dx$ with work by the system |
| Equilibrium manifold | $\mathcal E$, $d = \dim\mathcal E = n + 1$, coordinates $(U, X_1, \dots, X_n)$ ([[§C1.2 The Equilibrium Manifold and the Heat One-Form#^def-c1-2-1\|Def. §C1.2.1]]) | not used at levels A, B |
| Leaf label and factor | $\Sigma$, $\Theta$, with $\delta Q_{\text{rev}} = \Theta\,d\Sigma$, $\Theta = T\,g(\Sigma)$ | |
| Reservoir temperature | $T_b$; entropy produced $S_i$ | level B: $T$ of the reservoir |
| Time reversal | $\mathcal T$ on states ([[§C0.1 Microscopic Reversibility#^def-c0-1-1\|Def. §C0.1.1]]) | QM C8★ and QFT: other symbols, $U(\mathcal T)$ in QFT |
| Thermodynamic phase space | $\mathcal T$, coordinates $(U, q^a, p_a)$ ([[§C1.7 Thermodynamic Phase Space and Legendre Transforms#^def-c1-7-1\|Def. §C1.7.1]]) | Same letter as time reversal; the two never meet in one section |
| Physical constants | $\hbar$, $k_B$ explicit | |
| Accessible set and count | $\Gamma_{\text{acc}}$, $\Omega_{\text{acc}}$; macrostate $\Gamma_M$, multiplicity $\Omega(M)$ ([[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^def-c2-1-2\|Def. §C2.1.2]]) | level B: $\Omega$ |
| Binary entropy function | $h(n) = -n\ln n - (1-n)\ln(1-n)$, natural logarithms ([[§C2.2 Typicality in Large Systems#^def-c2-2-1\|Def. §C2.2.1]]) | |
| Inverse temperature | $\beta = (\partial\ln\Omega/\partial E)_{V,N} = 1/k_BT$ ([[§C2.4 Temperature and Entropy from Counting#^def-c2-4-1\|Def. §C2.4.1]]) | same at level B |
| Energy of a microcanonical system | $E$ (Ch. 2) and $U$ (Ch. 1) for the same quantity | |
| Phase-space measure | $d\Gamma = d^fq\,d^fp/h^f$; identical particles $d\Gamma_N = \prod d^dq_i\,d^dp_i/(N!\,h^{dN})$ ([[§C3.1 Microstates and Statistical States in Parallel#^def-c3-1-3\|Def. §C3.1.3]], [[§C3.5 Many-Particle States#^def-c3-5-2\|Def. §C3.5.2]]) | CM: plain phase volume |
| Classical density, density operator | $\rho_{\text{cl}}(X)$, $\hat\rho$ (hatted operators throughout Ch. 3) | QM C11: $\rho$ unhatted, populations $w_i$ |
| Poisson bracket | $\{F, G\}_{\text{PB}} = \sum_i(\partial_{q_i}F\,\partial_{p_i}G - \partial_{p_i}F\,\partial_{q_i}G)$; Liouville $\partial_t\rho_{\text{cl}} + \{\rho_{\text{cl}}, H\}_{\text{PB}} = 0$ | same convention as CM Def. §B8.1.1 |
| Partial trace | $\operatorname{Tr}_B$; reduced state $\hat\rho_A$ | QM C11: $\operatorname{tr}_B$ |
| Occupation numbers | $\lvert n_1, n_2, \dots\rangle$, $\hat H = \sum_\ell\epsilon_\ell\hat n_\ell$ | |
| Shannon entropy | $H[p] = -\sum_ip_i\ln p_i$ in nats from Ch. 4 on ($\log_2$, bits, only in §C4a.1); $H_{\max}$; $S_{\text{eq}} = k_BH_{\max}$ | level B: Gibbs entropy $S = -k_B\sum p\ln p$ |
| Multipliers | $\eta_\alpha$ for mean constraints; $\eta_E = \beta$, $\eta_N = -\beta\mu$, fugacity $z = e^{\beta\mu}$ | |
| Partition functions | $Z(\beta, V, N)$, $\Xi(\beta, \mu, V)$ or $\Xi(\beta, \eta_N, V)$; $\Delta(T, p, N)$ | level B: same $Z$; grand partition function $\mathcal Z$ in places |
| Grand potential | $\Phi = -k_BT\ln\Xi$ (Mao's PS5 writes $\Omega$) | level B: $\Phi$ |
| Massieu functions | $\ln Z = -\beta F$, $\ln\Xi = -\beta\Phi$ (dimensionless) | |
| Density of states | $g(E)$ of complete $N$-particle states (§C4a.9★) | level B: one-particle $g(\epsilon)$ |
