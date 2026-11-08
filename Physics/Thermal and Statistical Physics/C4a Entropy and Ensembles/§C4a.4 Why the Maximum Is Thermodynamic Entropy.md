---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.4
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C4a.3 Maximum Entropy and Lagrange Multipliers]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.5 The Canonical and Grand-Canonical Ensembles]] →

*Sources: Mao, PHY 510 notes, §4.3.4, eqs. (4.26)–(4.34), adapted there from Cover and Thomas, Elements of Information Theory · PHY 510 Lecture 9/29. Mao marks this subsection as not required for the exam; its result, [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|Theorem §C4a.4.6]], is.*

[[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-2|Theorem §C4a.3.2]] settles the microcanonical case: there $k_BH_{\max} = k_B\ln\Omega$ is Chapter C2's entropy. With a prescribed mean energy the maximizer is not uniform, and nothing yet ties $k_BH_{\max}$ to thermodynamics. The link is a counting argument: $M$ weakly coupled copies form an isolated system, to which $S = k_B\ln\Omega$ applies, and their microstate count turns out to be $e^{MH_{\max} + o(M)}$.

**Setup.**
- $M$ identical copies of the system, each at its own site; energy can flow between them, particles cannot, and the coupling energy is negligible.
- One copy: fixed $V$, $N$; $K$ microstates $i$ with energies $E_i$.
- All copies together: isolated, total energy in a shell $[E_{\text{tot}} - \tfrac12\Delta E, E_{\text{tot}} + \tfrac12\Delta E]$.

> [!model] Model §C4a.4.1: An Isolated Collection of Copies
> - Collection microstate: $(i_1, \dots, i_M)$, energy $\sum_aE_{i_a}$.
> - Weights: uniform on the microstates in the shell ([[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^pr-c2-1-1|Principle §C2.1.1]]). The collection is microcanonical; a single copy is not, since its energy changes by exchange.
> - Populations: $m_i$ copies in state $i$, fraction $p_i = m_i/M$, with
>
> $$
> \sum_im_i = M, \qquad \sum_ip_i = 1, \qquad \sum_ip_iE_i = \frac{E_{\text{tot}}}{M} \equiv U .
> $$
>
> Drawing one copy uniformly at random, $\operatorname{Prob}(\text{state } i) = p_i$.
>
> *Assumes:* copies told apart by position; weak coupling; $K < \infty$.
>
> *Source: Mao §4.3.4, eq. (4.26)*

^mod-c4a-4-1

> [!theorem] Theorem §C4a.4.2: Assignments with Given Populations
> The number of microstates of the collection with population list $\{m_i\}$ is
>
> $$
> W(\{m_i\}) = \frac{M!}{\prod_im_i!}, \qquad \frac1M\ln W \longrightarrow -\sum_ip_i\ln p_i = H[p] \qquad (M \to \infty,\ p_i\ \text{fixed}) .
> $$
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]; *applies:* uniformly in the list, $|\ln W - MH[p]| \le K(1 + \ln M)$ (Step 3).
>
> *Source: Mao §4.3.4, eqs. (4.27)–(4.29)*

^thm-c4a-4-2

> [!derivation]- Derivation
> **Step 1** (count). A collection microstate is a map $a \mapsto i_a$ from labelled copies to states, and we need the maps with $m_i$ copies sent to each $i$. Pick the copies for state $1$, then for state $2$ from those left, and so on: $\binom{M}{m_1}\binom{M - m_1}{m_2}\cdots = M!/\prod_im_i!$.
>
> **Step 2** (Stirling, leading order). $\ln W \simeq M\ln M - M - \sum_i(m_i\ln m_i - m_i)$. The $-M$ and $+\sum_im_i$ cancel, and with $m_i = Mp_i$,
>
> $$
> M\ln M - \sum_iMp_i(\ln M + \ln p_i) = -M\sum_ip_i\ln p_i .
> $$
>
> **Step 3** (uniform error). Comparing $\ln n! = \sum_{k\le n}\ln k$ with $\int_1^n\ln x\,dx$ gives $\ln n! = n\ln n - n + r_n$ with $1 \le r_n \le 1 + \ln n$ for $n \ge 1$, and $r_0 = 0$ (an empty state adds nothing, as $0\ln0 = 0$). Hence $\ln W - MH[p] = r_M - \sum_ir_{m_i}$ lies between $1 - K(1 + \ln M)$ and $1 + \ln M$, for every list. The finer Stirling form [[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|Theorem §B4.1.5]] gives the $\tfrac12\ln(2\pi n)$ terms, $O(K\ln M)$ again.

^der-c4a-4-1

*Uses:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]], [[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|Theorem §B4.1.5]]

> [!theorem] Theorem §C4a.4.3: Population Lists Concentrate on the MaxEnt Fractions
> A population list $\ell$ (fractions $p_\ell$) has $\operatorname{Prob}(\ell) = W_\ell/\Omega_{\text{tot}}$, $\Omega_{\text{tot}} = \sum_{\ell\ \text{allowed}}W_\ell$, and for two allowed lists
>
> $$
> \frac{\operatorname{Prob}(\ell)}{\operatorname{Prob}(\ell')} = e^{M[H(p_\ell) - H(p_{\ell'})] + O(K\ln M)} .
> $$
>
> The allowed $p_\ell$ obey the constraints of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]] (normalization, mean energy $U$ up to the shell width over $M$), so as $M \to \infty$ the fractions concentrate on $\arg\max H = p^\ast$.
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]; *applies:* $M \to \infty$.
>
> *Source: Mao §4.3.4*

^thm-c4a-4-3

> [!derivation]- Derivation
> Uniform weights on collection microstates ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]) give $\operatorname{Prob}(\ell) \propto W_\ell$; insert the uniform estimate of [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]] for both lists. Let $H^\ast_M$ be the largest $H(p_\ell)$ over allowed lists. The lists with $H(p_\ell) \le H^\ast_M - \delta H$ number at most $(M + 1)^K$, so together they carry at most $(M + 1)^Ke^{-M\delta H + O(K\ln M)} \to 0$ times the weight of the best list.

^der-c4a-4-2

*Uses:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]], [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]

> [!theorem] Lemma §C4a.4.4: The Count Splits into Which List and Which Assignment
> Label the allowed lists by $\ell$, with multiplicities $W_\ell$ and $q_\ell = W_\ell/\Omega_{\text{tot}}$. Then exactly
>
> $$
> \ln\Omega_{\text{tot}} = \underbrace{-\sum_\ell q_\ell\ln q_\ell}_{H_{\text{list}}} + \underbrace{\sum_\ell q_\ell\ln W_\ell}_{H_{\text{realization}}} .
> $$
>
> This is the grouping rule [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]] (3) for the uniform distribution on the $\Omega_{\text{tot}}$ collection microstates, with the lists as the groups.
>
> *Source: Mao §4.3.4, eq. (4.31) · the grouping requirement of [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]]*

^lem-c4a-4-4

> [!derivation]- Derivation
> $\sum_\ell q_\ell(\ln W_\ell - \ln q_\ell) = \sum_\ell q_\ell\ln(W_\ell/q_\ell) = \sum_\ell q_\ell\ln\Omega_{\text{tot}} = \ln\Omega_{\text{tot}}$.

^der-c4a-4-3

> [!theorem] Theorem §C4a.4.5: The Collection's Entropy Is $M$ Times the Maximum
> $$
> \ln\Omega_{\text{tot}} = MH_{\max}(U) + o(M) ,
> $$
>
> with $o(M)/M \to 0$.
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]] with $K$ states per copy; *applies:* $M \to \infty$, with the collection's shell wide enough that some allowed list has fractions within $O(1/M)$ of $p^\ast$: true if $\Delta E \ge 2K\max_i|E_i|$ (rounding $Mp_i^\ast$ to integers then stays in the shell), and $\Delta E = o(M)$.
>
> *Source: Mao §4.3.4, eq. (4.32); the shell condition and the exact bound of Step 2 are added here*

^thm-c4a-4-5

> [!derivation]- Derivation
> **Step 1** (few lists). $H_{\text{list}}$ is the entropy of a distribution on the allowed lists, so by [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|Theorem §C4a.1.2]] it is at most the log of their number. Each $m_i$ lies in $\{0, \dots, M\}$, so $0 \le H_{\text{list}} \le K\ln(M + 1) = o(M)$.
>
> **Step 2** (exact bound on one list). For a list with fractions $p_i = m_i/M$, expand by the multinomial theorem and keep one term:
>
> $$
> 1 = \Bigl(\sum_ip_i\Bigr)^M = \sum_{\{n_i\}}W(\{n_i\})\prod_ip_i^{n_i} \ge W(\{m_i\})\prod_ip_i^{m_i} = W(\{m_i\})\,e^{-MH[p]} .
> $$
>
> So $W(\{m_i\}) \le e^{MH[p]}$ for every list and every $M$, with no Stirling error.
>
> **Step 3** (upper bound). An allowed list is normalized and has mean energy $U_\ell$ within $\Delta E/2M$ of $U$, so $H(p_\ell) \le H_{\max}(U_\ell)$ by the definition of $H_{\max}$ as the constrained maximum ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]). $H_{\max}$ is concave in $U$ (mixing feasible $p$, $p'$ is feasible for the mixed mean, and $H$ is concave), hence continuous inside its range, and $\Delta E/M \to 0$; so $H_{\max}(U_\ell) \le H_{\max}(U) + \varepsilon_M$ with $\varepsilon_M \to 0$. By Step 2, $H_{\text{realization}} = \sum_\ell q_\ell\ln W_\ell \le M[H_{\max}(U) + \varepsilon_M]$, and with Step 1 and [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^lem-c4a-4-4|Lemma §C4a.4.4]], $\ln\Omega_{\text{tot}} \le MH_{\max} + o(M)$.
>
> **Step 4** (lower bound). Round the $Mp_i^\ast$ to integers $m_i^\ast$ with $\sum_im_i^\ast = M$ and $|m_i^\ast - Mp_i^\ast| < 1$. The total energy moves by less than $K\max_i|E_i| \le \tfrac12\Delta E$, so this list $\ell^\ast$ is allowed (*applies* line). Then $\Omega_{\text{tot}} \ge W_{\ell^\ast}$, and by the uniform estimate of [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]] and continuity of $H$, $\ln W_{\ell^\ast} \ge MH(p_{\ell^\ast}) - K(1 + \ln M) = MH_{\max} - o(M)$.
>
> **Step 5.** Steps 3 and 4 give $\ln\Omega_{\text{tot}} = MH_{\max}(U) + o(M)$.

^der-c4a-4-4

*Uses:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^lem-c4a-4-4|Lemma §C4a.4.4]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]], [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|Theorem §C4a.1.2]], [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]

> [!theorem] Theorem §C4a.4.6: Maximum Shannon Entropy Is Thermodynamic Entropy
> The equilibrium entropy of one system is
>
> $$
> S_{\text{eq}} = \lim_{M\to\infty}\frac{S_{\text{tot}}}{M} = k_BH_{\max} ,
> $$
>
> with $H_{\max}$ the constrained maximum of $-\sum_ip_i\ln p_i$ over the probabilities $p_i$ of one system's microstates.
>
> 1. Energy exchange only: $H_{\max} = H_{\max}(U, V, N)$ as above.
> 2. Particle exchange too: $\sum_im_iN_i = N_{\text{tot}}$ joins the list conditions, and
>
> $$
> S_{\text{eq}} = k_BH_{\max}(U, \bar N, V), \qquad \bar N = \frac{N_{\text{tot}}}{M} ;
> $$
>
> each further exchanged additive conserved quantity $Q$ adds the mean constraint $\sum_ip_iQ_i = Q_{\text{tot}}/M$.
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]; *applies:* weak coupling, so $S_{\text{tot}} = k_B\ln\Omega_{\text{tot}}$ by [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]; only $M$ is large, so the single system may be small, and its energy fluctuates.
>
> *Source: Mao §4.3.4, eqs. (4.33)–(4.34) and the boxed note marking this result as the one to retain*

^thm-c4a-4-6

> [!derivation]- Derivation
> The collection is isolated, so $S_{\text{tot}} = k_B\ln\Omega_{\text{tot}}$ ([[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]); divide by $M$ and use [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-5|Theorem §C4a.4.5]]. Calling $S_{\text{tot}}/M$ the entropy of one copy uses additivity over weakly coupled parts, $S_{AB} = S_A + S_B$ ([[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]), and the identity of the copies. For item 2 repeat [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-5|Theorem §C4a.4.5]] with the extra list condition.

^der-c4a-4-5

*Uses:* [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-5|Theorem §C4a.4.5]]

> [!remark]- Connections
> - The copies are Gibbs's ensemble taken literally; level B obtains the canonical distribution from a large reservoir instead, a route repeated in [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-5|Theorem §C4a.5.5]] — [[§B7.1 The Boltzmann Factor and the Partition Function#^thm-b7-1-1|Theorem §B7.1.1]].
> - The same "lists are polynomially many, assignments exponentially many" argument underlies the method of types in information theory (Cover and Thomas, Ch. 11).
