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

For the microcanonical ensemble the maximum entropy is $\ln\Omega$, which Chapter C2 already identified with thermodynamic entropy ([[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-2|Theorem §C4a.3.2]]). A canonical distribution is not uniform, and the energy of the system fluctuates. Why should its maximal Shannon entropy be thermodynamic entropy? The answer is to put many copies of the system in weak contact, so that the collection is isolated and microcanonical, count its microstates, and take the entropy per copy. The counting reduces to Shannon's entropy of the fractions of copies in each microstate.

**Setup.** $M$ identical systems at distinct places, in weak thermal contact: they exchange energy, not particles, and the coupling adds negligible energy. Each has fixed $V$, $N$ and a finite set of $K$ microstates $i$ with energies $E_i$. The collection is isolated with total energy $E_{\text{tot}}$ in a shell.

> [!model] Model §C4a.4.1: An Isolated Collection of Copies
> A microstate of the collection is the list $(i_1, \dots, i_M)$ of the states of all copies, with energy $\sum_aE_{i_a}$. By the fundamental assumption ([[§C2.1 Microstates, Macrostates and the Microcanonical Ensemble#^pr-c2-1-1|Principle §C2.1.1]]) all lists in the total-energy shell are equally likely: the collection is microcanonical, while each copy exchanges energy with the others. Let $m_i$ copies be in state $i$, and write $p_i = m_i/M$:
>
> $$
> \sum_im_i = M, \qquad \sum_ip_i = 1, \qquad \sum_ip_iE_i = \frac{E_{\text{tot}}}{M} \equiv U .
> $$
>
> $p_i$ is also the probability that a randomly chosen copy is in state $i$.
>
> *Assumes:* copies distinguishable by position; weak coupling; finitely many states per copy.
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
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]; *applies:* the correction to $\ln W$ is at most of order $\ln M$, so it vanishes per copy.
>
> *Source: Mao §4.3.4, eqs. (4.27)–(4.29)*

^thm-c4a-4-2

> [!derivation]- Derivation
> **Step 1** (count). Choose which $m_1$ copies are in state $1$, then which $m_2$ of the rest are in state $2$, and so on: $\binom{M}{m_1}\binom{M - m_1}{m_2}\cdots = M!/\prod_im_i!$. Copies sit at different places, so exchanging the states of two copies in different states gives a new microstate; the $m_i!$ remove exchanges within one state.
>
> **Step 2** (Stirling, leading order). $\ln W \simeq M\ln M - M - \sum_i(m_i\ln m_i - m_i)$. The $-M$ and $+\sum_im_i$ cancel, and with $m_i = Mp_i$,
>
> $$
> M\ln M - \sum_iMp_i(\ln M + \ln p_i) = -M\sum_ip_i\ln p_i .
> $$
>
> **Step 3** (corrections). The next Stirling terms are $\tfrac12\ln(2\pi M) - \sum_i\tfrac12\ln(2\pi m_i)$, at most $O(K\ln M)$. States with $m_i = 0$ contribute $0! = 1$ and $0\ln0 = 0$.

^der-c4a-4-1

*Uses:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]], [[§B4.1 Probability Distributions and the Gaussian#^thm-b4-1-5|Theorem §B4.1.5]]

> [!theorem] Theorem §C4a.4.3: The Most Probable Fractions Are the MaxEnt Probabilities
> Each population list has probability $W(\{m_i\})/\Omega_{\text{tot}}$ with $\Omega_{\text{tot}} = \sum_{\{m_i\}\ \text{allowed}}W(\{m_i\})$. Since $W \simeq e^{MH[p]}$, the most probable fractions maximize $H[p]$ subject to exactly the normalization and mean-energy constraints of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]], so they approach $p_i^\ast$. A list whose entropy is lower by a fixed $\delta H > 0$ is suppressed by a factor of order $e^{-M\delta H}$.
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]; *applies:* $M \to \infty$.
>
> *Source: Mao §4.3.4*

^thm-c4a-4-3

> [!derivation]- Derivation
> All microstates of the collection are equally likely ([[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]), so a population list is as probable as the number of microstates it contains, $W$. By [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]], $\ln W = MH[p] + O(\ln M)$, and the allowed lists are those with $\sum_ip_i = 1$ and $\sum_ip_iE_i = U$, the constraints of [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]. Two lists with entropies differing by $\delta H$ have weights in the ratio $e^{M\delta H + O(\ln M)}$.

^der-c4a-4-2

*Uses:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]], [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|Theorem §C4a.3.3]]

> [!theorem] Lemma §C4a.4.4: The Count Splits into Which List and Which Assignment
> Label the allowed lists by $\ell$, with multiplicities $W_\ell$ and $q_\ell = W_\ell/\Omega_{\text{tot}}$. Then exactly
>
> $$
> \ln\Omega_{\text{tot}} = \underbrace{-\sum_\ell q_\ell\ln q_\ell}_{H_{\text{list}}} + \underbrace{\sum_\ell q_\ell\ln W_\ell}_{H_{\text{realization}}} :
> $$
>
> the uncertainty about which list occurs, plus the average uncertainty about which copies are in which states.
>
> *Source: Mao §4.3.4, eq. (4.31) · the grouping requirement of [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]]*

^lem-c4a-4-4

> [!derivation]- Derivation
> $\ln W_\ell - \ln q_\ell = \ln\Omega_{\text{tot}}$ for every $\ell$. Multiply by $q_\ell$ and sum, using $\sum_\ell q_\ell = 1$.

^der-c4a-4-3

> [!theorem] Theorem §C4a.4.5: The Collection's Entropy Is $M$ Times the Maximum
> $$
> \ln\Omega_{\text{tot}} = MH_{\max}(U) + o(M) ,
> $$
>
> with $o(M)/M \to 0$.
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]] with $K$ states per copy; *applies:* $M \to \infty$.
>
> *Source: Mao §4.3.4, eq. (4.32)*

^thm-c4a-4-5

> [!derivation]- Derivation
> **Step 1** (lists are few). A list is $K$ numbers in $\{0, \dots, M\}$, so there are at most $(M + 1)^K$ lists, and $H_{\text{list}} \le \ln(M + 1)^K = K\ln(M + 1) = o(M)$.
>
> **Step 2** (realizations). $H_{\text{realization}} = \sum_\ell q_\ell\ln W_\ell \le \max_\ell\ln W_\ell = MH_{\max} + O(\ln M)$ by [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]] and [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-3|Theorem §C4a.4.3]]. For the lower bound, $\Omega_{\text{tot}} \ge W_{\ell^\ast}$ for a list $\ell^\ast$ with fractions within $O(1/M)$ of $p^\ast$, so $\ln\Omega_{\text{tot}} \ge MH_{\max} - o(M)$.
>
> **Step 3.** Combine with [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^lem-c4a-4-4|Lemma §C4a.4.4]]: $MH_{\max} - o(M) \le \ln\Omega_{\text{tot}} \le MH_{\max} + o(M)$.

^der-c4a-4-4

*Uses:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^lem-c4a-4-4|Lemma §C4a.4.4]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|Theorem §C4a.4.2]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-3|Theorem §C4a.4.3]]

> [!theorem] Theorem §C4a.4.6: Maximum Shannon Entropy Is Thermodynamic Entropy
> The equilibrium entropy of one system is
>
> $$
> S_{\text{eq}} = \lim_{M\to\infty}\frac{S_{\text{tot}}}{M} = k_BH_{\max} ,
> $$
>
> with $H_{\max}$ the maximum of $-\sum_ip_i\ln p_i$ under the system's constraints, $p_i$ the probability of microstate $i$. This holds although one system is not microcanonical, and the copies need not be macroscopic. With particle exchange as well, fix $N_{\text{tot}}$ and add $\sum_im_iN_i = N_{\text{tot}}$: the entropy per system is $k_BH_{\max}(U, \bar N, V)$ with $\bar N = N_{\text{tot}}/M$, and likewise for any exchanged additive conserved quantity.
>
> *Model:* [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|Model §C4a.4.1]]; *applies:* weak coupling, so the collection's entropy is $S_{\text{tot}} = k_B\ln\Omega_{\text{tot}}$ by [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]].
>
> *Source: Mao §4.3.4, eqs. (4.33)–(4.34) and the boxed note marking this result as the one to retain*

^thm-c4a-4-6

> [!derivation]- Derivation
> $S_{\text{tot}} = k_B\ln\Omega_{\text{tot}}$ ([[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]]), and $\ln\Omega_{\text{tot}}/M \to H_{\max}$ by [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-5|Theorem §C4a.4.5]]. With negligible coupling the entropy is shared equally by identical copies.

^der-c4a-4-5

*Uses:* [[§C2.4 Temperature and Entropy from Counting#^thm-c2-4-6|Theorem §C2.4.6]], [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-5|Theorem §C4a.4.5]]

> [!remark]- Connections
> - The copies are Gibbs's ensemble taken literally; level B obtains the canonical distribution from a large reservoir instead, a route repeated in [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-5|Theorem §C4a.5.5]] — [[§B7.1 The Boltzmann Factor and the Partition Function#^thm-b7-1-1|Theorem §B7.1.1]].
> - The same "lists are polynomially many, assignments exponentially many" argument underlies the method of types in information theory (Cover and Thomas, Ch. 11).
