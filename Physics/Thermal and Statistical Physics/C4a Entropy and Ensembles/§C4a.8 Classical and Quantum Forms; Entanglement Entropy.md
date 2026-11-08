---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.8
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.7 Heat, Work and the Clausius Equality]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.9★ Density of States, Laplace and Legendre]] →

*Sources: Mao, PHY 510 notes, §4.3.9–§4.3.10, eqs. (4.62)–(4.73) · PHY 510 Lecture 10/1.*

Everything so far used a list of discrete microstates. Here the list is replaced by phase space ($\sum_i \to \int d\Gamma_N$, $E_i \to H_N(X)$) or by a Hilbert space ($\sum_i \to \operatorname{Tr}$, $E_i \to \hat H$), and the quantum MaxEnt state is proved for constraint operators that need not commute. Since $-\operatorname{Tr}\hat\rho\ln\hat\rho$ never refers to equilibrium, it can also be evaluated on the reduced state of a part, which gives subsystem and entanglement entropy. The quantum canonical operator has its home in Quantum Mechanics ([[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^thm-c11-2-5|QM Theorem §C11.2.5]]), as does the entanglement entropy ([[§C11.3 Composite Systems and Reduced Density Matrices#^def-c11-3-2|QM Def. §C11.3.2]]).

**Setup.** Classical $N$-particle phase space with $d\Gamma_N$ of [[§C3.5 Many-Particle States#^def-c3-5-2|Def. §C3.5.2]]; quantum $N$-particle space $\mathcal H_N$ and Fock space $\mathcal F = \bigoplus_{N=0}^\infty\mathcal H_N$ ([[§C12.2★ Second Quantization#^def-c12-2-1|QM Def. §C12.2.1]]; its occupation-number basis: [[§C3.5 Many-Particle States#^def-c3-5-3|Def. §C3.5.3]]).

> [!theorem] Theorem §C4a.8.1: Classical and Quantum Forms of the MaxEnt State
> The maximum-entropy states for prescribed means $\bar A_\alpha$ are
>
> $$
> \rho_{\text{cl}}^\ast(X) = \frac{1}{Z_{\text{cl}}}\exp\Bigl[-\sum_\alpha\eta_\alpha A_\alpha(X)\Bigr], \qquad \hat\rho^\ast = \frac1{Z_q}\exp\Bigl[-\sum_\alpha\eta_\alpha\hat A_\alpha\Bigr],
> $$
>
> with $Z_{\text{cl}} = \int d\Gamma(X)\exp[-\sum_\alpha\eta_\alpha A_\alpha(X)]$ and $Z_q = \operatorname{Tr}\exp[-\sum_\alpha\eta_\alpha\hat A_\alpha]$. The dictionary is
>
> $$
> \sum_i \longleftrightarrow \int d\Gamma_N \longleftrightarrow \operatorname{Tr}_{\mathcal H_N}, \qquad E_i \longleftrightarrow H_N(X) \longleftrightarrow \hat H .
> $$
>
> *Model:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], [[§C4a.2 The Entropy of a Statistical State#^def-c4a-2-3|Def. §C4a.2.3]], [[§C4a.2 The Entropy of a Statistical State#^def-c4a-2-4|Def. §C4a.2.4]]; *applies:* $Z_{\text{cl}}$, $Z_q$ finite; the $\hat A_\alpha$ need not commute. When they do (e.g. $\hat H$, $\hat N$ with $N$ conserved), a joint eigenbasis turns $\hat\rho^\ast$ into the $p_i^\ast$ of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]].
>
> *Source: Mao §4.3.9, eqs. (4.62)–(4.63), (4.67)*

^thm-c4a-8-1

> [!derivation]- Derivation
> **Classical.** Replace $p_i$ by $\rho_{\text{cl}}(X)$ and $\sum_i$ by $\int d\Gamma$ in [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^der-c4a-3-2|Derivation §C4a.3.2]]; stationarity of $-\int\rho\ln\rho\,d\Gamma - \lambda_0(\int\rho\,d\Gamma - 1) - \sum_\alpha\eta_\alpha(\int\rho A_\alpha\,d\Gamma - \bar A_\alpha)$ under variations $\delta\rho(X)$ gives the same exponential pointwise. It is the maximum: for any admissible $\rho$, Gibbs' inequality for densities w.r.t. $d\Gamma$ gives $H_{\text{cl}}[\rho] \le -\int\rho\ln\rho_{\text{cl}}^\ast\,d\Gamma = \ln Z_{\text{cl}} + \sum_\alpha\eta_\alpha\bar A_\alpha = H_{\text{cl}}[\rho_{\text{cl}}^\ast]$.
>
> **Quantum** (Gibbs' variational principle). $\hat\rho^\ast$ is positive definite with $\ln\hat\rho^\ast = -\ln Z_q - \sum_\alpha\eta_\alpha\hat A_\alpha$. Let $\hat\rho$ be any density operator with $\operatorname{Tr}\hat\rho\hat A_\alpha = \bar A_\alpha$, and $S(\hat\rho\|\hat\rho^\ast) = \operatorname{Tr}\hat\rho(\ln\hat\rho - \ln\hat\rho^\ast)$ its relative entropy. Then
>
> $$
> 0 \le S(\hat\rho\|\hat\rho^\ast) = -H_{\text{vN}}[\hat\rho] - \operatorname{Tr}\hat\rho\ln\hat\rho^\ast = -H_{\text{vN}}[\hat\rho] + \ln Z_q + \sum_\alpha\eta_\alpha\bar A_\alpha = H_{\text{vN}}[\hat\rho^\ast] - H_{\text{vN}}[\hat\rho] ,
> $$
>
> where the last step is the same trace with $\hat\rho = \hat\rho^\ast$. No commutation of the $\hat A_\alpha$ with each other or with $\hat\rho$ is used. For $\hat H$ alone this is [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^thm-c11-2-5|QM Theorem §C11.2.5]].
>
> *Klein's inequality* ($S \ge 0$, equality iff $\hat\rho = \hat\rho^\ast$). Write $\hat\rho = \sum_ar_a|a\rangle\langle a|$, $\hat\rho^\ast = \sum_bs_b|b\rangle\langle b|$ and $P_{ab} = |\langle a|b\rangle|^2$, whose rows and columns each sum to $1$. Jensen's inequality for the concave $\ln$ gives $-\operatorname{Tr}\hat\rho\ln\hat\rho^\ast = -\sum_ar_a\sum_bP_{ab}\ln s_b \ge -\sum_ar_a\ln t_a$ with $t_a = \sum_bP_{ab}s_b$, a probability distribution; so $S \ge \sum_ar_a\ln(r_a/t_a) \ge 0$ by Gibbs' inequality [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]]. Equality forces $t_a = r_a$ and, for $r_a > 0$, $|a\rangle$ inside one eigenspace of $\hat\rho^\ast$, so $\hat\rho^\ast|a\rangle = r_a|a\rangle$; these eigenvalues already sum to $1 = \operatorname{Tr}\hat\rho^\ast$, and positive definiteness leaves no room for other eigenvectors, so $\hat\rho^\ast = \hat\rho$.

^der-c4a-8-1

*Uses:* [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], [[§C4a.2 The Entropy of a Statistical State#^def-c4a-2-4|Def. §C4a.2.4]], [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]]

> [!example] Example §C4a.8.1: The Three Ensembles, Classically and Quantum Mechanically
> | | classical | quantum |
> | --- | --- | --- |
> | microcanonical | $\rho_{\text{mc}} = \mathbb 1_{\text{shell}}(X)/\Omega_{\text{cl}}$, $\Omega_{\text{cl}} = \int d\Gamma_N\,\mathbb 1_{\text{shell}}$ | $\hat\rho_{\text{mc}} = \hat P_{\text{shell}}/\Omega_q$, $\Omega_q = \operatorname{Tr}_{\mathcal H_N}\hat P_{\text{shell}}$ |
> | canonical | $e^{-\beta H_N(X)}/Z_{\text{cl}}$, $Z_{\text{cl}} = \int d\Gamma_N\,e^{-\beta H_N}$ | $e^{-\beta\hat H}/Z_q$, $Z_q = \operatorname{Tr}_{\mathcal H_N}e^{-\beta\hat H}$ |
> | grand canonical | $e^{-\beta(H_N(X) - \mu N)}/\Xi_{\text{cl}}$, $\Xi_{\text{cl}} = \sum_N\int d\Gamma_N\,e^{-\beta(H_N - \mu N)}$ | $e^{-\beta(\hat H - \mu\hat N)}/\Xi_q$, $\Xi_q = \operatorname{Tr}_{\mathcal F}e^{-\beta(\hat H - \mu\hat N)}$ |
>
> $\mathbb 1_{\text{shell}}$ is $1$ in the energy shell and $0$ outside; $\hat P_{\text{shell}}$ projects on the shell's subspace.
>
> *Source: Mao §4.3.9, eqs. (4.64)–(4.71) · level B: [[§B8.1 The Partition Function of the Ideal Gas#^thm-b8-1-3|Theorem §B8.1.3]] (classical gas), QM home of the quantum canonical operator: [[§C11.2 Density-Operator Dynamics and Quantum Statistical Mechanics#^thm-c11-2-5|QM Theorem §C11.2.5]]*

^ex-c4a-8-1

## Entanglement entropy

> [!definition] Definition §C4a.8.1: Entropy of a Subsystem
> The entropy of a subsystem $A$ is the von Neumann entropy of its reduced state ([[§C3.4 Composite Systems and Reduced States#^thm-c3-4-2|Theorem §C3.4.2]]):
>
> $$
> \hat\rho_A = \operatorname{Tr}_B\hat\rho_{AB}, \qquad S_A = -k_B\operatorname{Tr}_A(\hat\rho_A\ln\hat\rho_A) = -k_B\sum_\alpha\lambda_\alpha\ln\lambda_\alpha ,
> $$
>
> with $\lambda_\alpha$ the eigenvalues of $\hat\rho_A$. The definition refers to no equilibrium; when $\hat\rho_A \approx e^{-\beta\hat H_A}/Z_A$, $S_A$ is the canonical entropy of [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy#^thm-c4a-8-1|Theorem §C4a.8.1]] at that $\beta$.
>
> *Source: Mao §4.3.10, eq. (4.72)*

^def-c4a-8-1

> [!theorem] Theorem §C4a.8.2: Entanglement Entropy of a Pure Whole
> If $\hat\rho_{AB}$ is pure, $\hat\rho_A$ and $\hat\rho_B$ have the same nonzero eigenvalues, so
>
> $$
> S_{\text{ent}}(A : B) = S_A = S_B, \qquad S_{AB} = 0 .
> $$
>
> $S_{\text{ent}}$ is the **entanglement entropy** of [[§C11.3 Composite Systems and Reduced Density Matrices#^def-c11-3-2|QM Def. §C11.3.2]]. For a pure whole, $S_A > 0$ iff $|\Psi\rangle$ has more than one nonzero Schmidt coefficient, i.e. is entangled. For a mixed whole see [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy#^ex-c4a-8-2|Example §C4a.8.2]].
>
> *Model:* [[§C3.4 Composite Systems and Reduced States#^def-c3-4-3|Def. §C3.4.3]], pure joint state; *applies:* finite dimensions.
>
> *Source: Mao §4.3.10, eq. (4.73) · QM homes: [[§C11.3 Composite Systems and Reduced Density Matrices#^thm-c11-3-2|QM Theorem §C11.3.2]], [[§C11.3 Composite Systems and Reduced Density Matrices#^def-c11-3-2|QM Def. §C11.3.2]]*

^thm-c4a-8-2

> [!derivation]- Derivation
> **Step 1** (Schmidt form). Write $|\Psi\rangle = \sum_{ab}c_{ab}|ab\rangle$ and take the singular-value decomposition of the matrix $c = U\Sigma V^\dagger$. In the bases $|u_k\rangle = \sum_aU_{ak}|a\rangle$, $|v_k\rangle = \sum_bV_{bk}^{\ast}|b\rangle$, $|\Psi\rangle = \sum_k\sigma_k|u_k\rangle|v_k\rangle$ with $\sigma_k \ge 0$, $\sum_k\sigma_k^2 = 1$ ([[§C11.3 Composite Systems and Reduced Density Matrices#^thm-c11-3-2|QM Theorem §C11.3.2]]).
>
> **Step 2** (both reduced states). $\operatorname{Tr}_B|\Psi\rangle\langle\Psi| = \sum_k\sigma_k^2|u_k\rangle\langle u_k|$ and $\operatorname{Tr}_A|\Psi\rangle\langle\Psi| = \sum_k\sigma_k^2|v_k\rangle\langle v_k|$ by [[§C3.4 Composite Systems and Reduced States#^thm-c3-4-2|Theorem §C3.4.2]], with the same eigenvalues $\sigma_k^2$, so $S_A = S_B$. A pure state has one eigenvalue $1$, so $S_{AB} = 0$. $S_A = 0$ iff a single $\sigma_k$ is nonzero, i.e. $|\Psi\rangle$ is a product.

^der-c4a-8-2

*Uses:* [[§C3.4 Composite Systems and Reduced States#^thm-c3-4-2|Theorem §C3.4.2]]

> [!example] Example §C4a.8.2: Two Qubit Pairs with the Same Halves
> | joint state | $\hat\rho_A$ | $S_A$ | $S_{AB}$ | entangled? |
> | --- | --- | --- | --- | --- |
> | Bell pair ([[§C3.4 Composite Systems and Reduced States#^ex-c3-4-3|Example §C3.4.3]]), pure | $\tfrac12\mathbb 1$ | $k_B\ln2$ | $0$ | yes |
> | $\hat\rho_{AB} = \tfrac14\mathbb 1 = \tfrac12\mathbb 1\otimes\tfrac12\mathbb 1$ | $\tfrac12\mathbb 1$ | $k_B\ln2$ | $2k_B\ln2$ | no (product) |
>
> In both rows $\hat\rho_A$ has eigenvalues $\tfrac12, \tfrac12$, so $S_A = -k_B(2\cdot\tfrac12\ln\tfrac12) = k_B\ln2$. The second row shows that once the whole is mixed, $S_A > 0$ is no evidence of entanglement; [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy#^thm-c4a-8-2|Theorem §C4a.8.2]] needs the pure whole.
>
> *Source: Mao §4.3.10, after eq. (4.73) (Bell pair and the mixed-whole caveat); the product counter-example is added here*

^ex-c4a-8-2

> [!remark]- Connections
> - A subsystem of a large pure system can look thermal, with $S_A$ its thermal entropy; this is the quantum side of the "reduced description" of [[§C3.3 Liouville Theorems and Stationary Ensembles#^rem-c3-3-1|§C3.3, Remark: Two levels of dynamics]].
> - Entropy of a whole versus its parts: for a pure whole $S_{AB} = 0 \le S_A + S_B$, strict iff entangled, while for weakly coupled systems in equilibrium entropy is additive ([[§C1.4 Temperature and Entropy#^thm-c1-4-4|Theorem §C1.4.4]]); the difference is the correlation.
