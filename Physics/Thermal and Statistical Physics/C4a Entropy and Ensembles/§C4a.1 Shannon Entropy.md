---
type: section
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
section: C4a.1
conventions: "[[Mao PHY 510]]"
tags: [thermal-physics, level-c]
---
← [[§C3.6 Spins, a Damped Pendulum and Two Particles in Three Orbitals]] · ↑ [[· C4a Entropy and Ensembles]] · [[§C4a.2 The Entropy of a Statistical State]] →

*Sources: Mao, PHY 510 notes, §4.1, eqs. (4.1)–(4.7) and boxes "Finding a prize", "Learning one of four outcomes in two stages", "Bits, binary codes, and information compression", "Information and surprisal" · Shannon, A Mathematical Theory of Communication (1948), §6 and Appendix 2 · PHY 510 Lectures 9/22, 9/24.*

Chapter C2 gave equal weights to the microstates of an isolated system. A system in contact with a bath has no such symmetry, and its probabilities have to come from somewhere else. Chapter C4 takes them from a principle of inference, maximum entropy, and this section supplies the quantity being maximized: a measure of how uncertain a probability distribution leaves us. Level B defines Shannon's entropy and its bounds ([[§B6.3 Entropy, Information and the Gibbs Paradox#^def-b6-3-2|Def. §B6.3.2]], [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]]); level C derives the formula from Shannon's requirements and reads it as an average number of yes–no questions.

**Setup.** An experiment with outcomes $i = 1, \dots, n$ and probabilities $p_i \ge 0$, $\sum_ip_i = 1$. Logarithms are to base $2$ in this section; from [[§C4a.2 The Entropy of a Statistical State|§C4a.2]] on they are natural.

## Uncertainty as a number of questions

> [!example] Example §C4a.1.1: Finding a Prize with Yes–No Questions
> A prize is in one of four boxes $A, B, C, D$, and each yes–no question costs one dollar.
>
> 1. If the boxes are equally likely, ask "$A$ or $B$?" and then one more question: always $2$ dollars.
> 2. If the probabilities are $(\tfrac12, \tfrac14, \tfrac18, \tfrac18)$, ask "$A$?", then "$B$?", then "$C$?" only if needed. The costs are $1, 2, 3, 3$ for the four boxes, with mean
>
> $$
> \tfrac12(1) + \tfrac14(2) + \tfrac18(3) + \tfrac18(3) = \tfrac74 .
> $$
>
> Same $n = 4$, mean cost $2$ versus $\tfrac74$: a measure of uncertainty must see the $p_i$, not just $n$.
>
> *Source: Mao §4.1, box "Finding a prize: one dollar per question" · Lecture 9/22*

^ex-c4a-1-1

> [!definition] Definition §C4a.1.1: Shannon's Requirements for a Measure of Uncertainty
> A measure $H(p_1, \dots, p_n)$, depending only on the probabilities and not on the names of the outcomes, should satisfy:
>
> 1. **Continuity:** small changes of the $p_i$ change $H$ little.
> 2. **Monotonicity:** $A(n) \equiv H(\tfrac1n, \dots, \tfrac1n)$ increases with $n$.
> 3. **Grouping:** if the outcomes are split into groups $G_a$ with probabilities $P_a = \sum_{i\in G_a}p_i$, then
>
> $$
> H(p_1, \dots, p_n) = H(P_1, \dots, P_r) + \sum_aP_a\,H\Bigl(\Bigl\{\frac{p_i}{P_a}\Bigr\}_{i\in G_a}\Bigr) ,
> $$
>
> that is, (cost of naming the group) $+$ (mean cost of naming the member inside it). Groups with $P_a = 0$ have no conditional distribution and are left out of the sum.
>
> *Source: Mao §4.1, eq. (4.2) · Shannon (1948), §6*

^def-c4a-1-1

> [!example] Example §C4a.1.2: Two Stages for the Prize
> Group the prize boxes into $\{A\}$ and $\{B, C, D\}$, each of probability $\tfrac12$. The first stage costs $H(\tfrac12, \tfrac12)$. With probability $\tfrac12$ the box is known; with probability $\tfrac12$ the conditional probabilities of $B, C, D$ are $(\tfrac12, \tfrac14, \tfrac14)$. So
>
> $$
> H\bigl(\tfrac12, \tfrac14, \tfrac18, \tfrac18\bigr) = H\bigl(\tfrac12, \tfrac12\bigr) + \tfrac12H(1) + \tfrac12H\bigl(\tfrac12, \tfrac14, \tfrac14\bigr) ,
> $$
>
> with $H(1) = 0$. The weights $\tfrac12$ in front of the second-stage terms are the group probabilities $P_a$ of [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]] (3).
>
> *Source: Mao §4.1, box "Learning one of four outcomes in two stages"*

^ex-c4a-1-2

> [!theorem] Theorem §C4a.1.1: Shannon's Entropy Is the Only Such Measure
> The only functions satisfying [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]] are
>
> $$
> H[p] = -C\sum_ip_i\log_2p_i, \qquad C > 0 .
> $$
>
> Fixing $H(\tfrac12, \tfrac12) = 1$, one **bit**, gives $C = 1$:
>
> $$
> H[p] = -\sum_ip_i\log_2p_i, \qquad 0\log_20 \equiv 0 .
> $$
>
> A certain outcome has $H = 0$; $n$ equally likely outcomes have $H = \log_2n$.
>
> *Model:* finite outcome sets; *applies:* any distribution.
>
> *Source: Mao §4.1, eqs. (4.3)–(4.4) (proof cited to Shannon) · proof: Shannon (1948), Appendix 2, written out here · level-B home: [[§B6.3 Entropy, Information and the Gibbs Paradox#^def-b6-3-2|Def. §B6.3.2]]*

^thm-c4a-1-1

> [!derivation]- Derivation
> **Step 1** (uniform: powers). Split $s^m$ equally likely outcomes into $s$ groups of $s^{m-1}$. Grouping gives $A(s^m) = A(s) + A(s^{m-1})$, and by induction $A(s^m) = mA(s)$.
>
> **Step 2** (uniform: logarithm). Fix $s, t \ge 2$. For any $n$ choose $m$ with $s^m \le t^n < s^{m+1}$. Taking $\log_2$, $\frac mn \le \frac{\log_2t}{\log_2s} < \frac mn + \frac1n$. Monotonicity and Step 1 give $mA(s) \le nA(t) < (m + 1)A(s)$, so $\frac mn \le \frac{A(t)}{A(s)} < \frac mn + \frac1n$. Hence $\bigl|\frac{A(t)}{A(s)} - \frac{\log_2t}{\log_2s}\bigr| < \frac1n$ for every $n$, so $A(t) = C\log_2t$ with $C = A(s)/\log_2s$, positive because $A$ increases and $A(1) = 0$ (grouping one outcome into itself).
>
> **Step 3** (rational probabilities). Let $p_i = n_i/\sum_jn_j$ with integers $n_i$. Take $\sum_jn_j$ equally likely outcomes and group them into blocks of sizes $n_i$. Grouping gives
>
> $$
> C\log_2\sum_jn_j = H(p_1, \dots, p_n) + \sum_ip_i\,C\log_2n_i ,
> $$
>
> so $H = -C\sum_ip_i\log_2\frac{n_i}{\sum_jn_j} = -C\sum_ip_i\log_2p_i$.
>
> **Step 4** (all probabilities). Rational distributions are dense, and $H$ is continuous, so the formula holds everywhere.
>
> **Step 5** (unit). $H(\tfrac12, \tfrac12) = C$, so the bit fixes $C = 1$.

^der-c4a-1-1

*Uses:* [[§C4a.1 Shannon Entropy#^def-c4a-1-1|Def. §C4a.1.1]]

> [!theorem] Theorem §C4a.1.2: The Uniform Distribution Has the Most Uncertainty
> For $n$ outcomes, $0 \le H[p] \le \log_2n$, with $H = 0$ only for a certain outcome and $H = \log_2n$ only for the uniform distribution.
>
> *Model:* [[§C4a.1 Shannon Entropy#^thm-c4a-1-1|Theorem §C4a.1.1]]; *applies:* fixed number of outcomes.
>
> *Source: Mao §4.1 · level-B home: [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]]*

^thm-c4a-1-2

> [!derivation]- Derivation
> **Lower bound.** Each term $-p_i\log_2p_i \ge 0$ on $[0, 1]$, zero only at $p_i \in \{0, 1\}$.
>
> **Upper bound.** $\log_2$ is concave, so by Jensen's inequality over the outcomes with $p_i > 0$,
>
> $$
> H = \sum_ip_i\log_2\frac1{p_i} \le \log_2\sum_ip_i\frac1{p_i} \le \log_2n ,
> $$
>
> with equality iff all $1/p_i$ are equal and every outcome has $p_i > 0$, that is $p_i = 1/n$.

^der-c4a-1-2

## Bits and codes

> [!definition] Definition §C4a.1.2: Binary Prefix Code
> A **binary prefix code** assigns to each outcome $i$ a string of $\ell_i$ binary digits such that no codeword is the beginning of another. Concatenated codewords can then be read without separators.
>
> *Source: Mao §4.1, box "Bits, binary codes, and information compression"*

^def-c4a-1-2

> [!example] Example §C4a.1.3: A Code for the Prize
> For the probabilities $(\tfrac12, \tfrac14, \tfrac18, \tfrac18)$, write the answers of [[§C4a.1 Shannon Entropy#^ex-c4a-1-1|Example §C4a.1.1]] as digits, $0$ = yes and $1$ = no:
>
> | box | $A$ | $B$ | $C$ | $D$ |
> |---|---|---|---|---|
> | codeword | $0$ | $10$ | $110$ | $111$ |
>
> - Decoding: split the stream after each complete answer sequence, $10110111 = 10\,|\,110\,|\,111 = BCD$.
> - Length: $AAAB \mapsto 00010$ has $5$ digits; a fixed-length code ($2$ digits per box) would use $8$.
> - Each question here splits the remaining probability in half, so $p_i = 2^{-\ell_i}$ and
>
> $$
> \ell_i = -\log_2p_i, \qquad \langle\ell\rangle = \sum_ip_i\ell_i = \tfrac74 = H[p] .
> $$
>
> *Source: Mao §4.1, box "Bits, binary codes, and information compression", eq. (4.5)*

^ex-c4a-1-3

> [!theorem] Theorem §C4a.1.3: Shannon's Source-Coding Bound
> The shortest average length of a binary prefix code obeys
>
> $$
> H[p] \le \langle\ell\rangle_{\min} < H[p] + 1 .
> $$
>
> For blocks of $k$ independent outcomes coded as one symbol,
>
> $$
> \lim_{k\to\infty}\frac{\langle\ell_k\rangle_{\min}}{k} = H[p] ,
> $$
>
> so $H$ is the price in digits per outcome of lossless recording.
>
> *Model:* independent outcomes, known probabilities, shared code; *applies:* lossless prefix codes.
>
> *Source: Mao §4.1 (statement) · PHY 510 Problem Set 4, Problem 2(c) · proof via Kraft's inequality written here (Cover and Thomas, Elements of Information Theory, §5.2–§5.4, cited in Mao's bibliography)*

^thm-c4a-1-3

> [!derivation]- Derivation
> **Step 1** (Kraft). A prefix code satisfies $\sum_i2^{-\ell_i} \le 1$. Let $\ell_{\max}$ be the longest length. A codeword of length $\ell_i$ is the beginning of $2^{\ell_{\max}-\ell_i}$ strings of length $\ell_{\max}$, and the prefix property makes these sets disjoint for different $i$. There are $2^{\ell_{\max}}$ strings in all, so $\sum_i2^{\ell_{\max}-\ell_i} \le 2^{\ell_{\max}}$. Conversely, lengths with $\sum_i2^{-\ell_i} \le 1$ can be realized by a prefix code: sort $\ell_1 \le \ell_2 \le \dots$ and choose codewords in turn. At step $i$ the earlier codewords are beginnings of $\sum_{j<i}2^{\ell_i-\ell_j} < 2^{\ell_i}$ strings of length $\ell_i$ (strict since $\sum_{j\le i}2^{-\ell_j} \le 1$), so a free string of length $\ell_i$ remains; it is not a beginning of an earlier codeword, since those are no longer.
>
> **Step 2** (lower bound). With $q_i = 2^{-\ell_i}/\sum_j2^{-\ell_j}$,
>
> $$
> \langle\ell\rangle - H = \sum_ip_i\log_2\frac{p_i}{q_i} - \log_2\sum_j2^{-\ell_j} \ge 0 ,
> $$
>
> since the first term is a relative entropy, nonnegative by Gibbs' inequality [[§B6.3 Entropy, Information and the Gibbs Paradox#^thm-b6-3-3|Theorem §B6.3.3]] (Jensen over the $i$ with $p_i > 0$: $-\sum p_i\log_2(q_i/p_i) \ge -\log_2\sum_{p_i>0}q_i \ge 0$), and the second is $\ge 0$ by Step 1.
>
> **Step 3** (upper bound). Take $\ell_i = \lceil-\log_2p_i\rceil$. Then $\sum_i2^{-\ell_i} \le \sum_ip_i = 1$, so a prefix code with these lengths exists, and $\ell_i < -\log_2p_i + 1$ gives $\langle\ell\rangle < H + 1$.
>
> **Step 4** (blocks). For $k$ independent outcomes coded together the entropy is $kH$, so $kH \le \langle\ell_k\rangle_{\min} < kH + 1$, and the length per outcome lies within $1/k$ of $H$.

^der-c4a-1-3

*Uses:* [[§C4a.1 Shannon Entropy#^thm-c4a-1-1|Theorem §C4a.1.1]], [[§C4a.1 Shannon Entropy#^def-c4a-1-2|Def. §C4a.1.2]]

## Surprisal

> [!definition] Definition §C4a.1.3: Surprisal
> The **surprisal** (information content) of an outcome of probability $p_i$ is
>
> $$
> I_i = -\log_2p_i \ \text{bits}.
> $$
>
> 1. $I_i = 0$ for a certain outcome and grows as $p_i$ shrinks.
> 2. For independent outcomes, $-\log_2(pq) = -\log_2p - \log_2q$.
> 3. $I$ is a random variable on the outcomes, and $H$ is its expectation:
>
> $$
> \langle I\rangle = \sum_ip_i(-\log_2p_i) = H[p] .
> $$
>
> *Source: Mao §4.1, box "Information and surprisal", eqs. (4.6)–(4.7)*

^def-c4a-1-3

> [!example] Example §C4a.1.4: A Question That Rarely Pays
> In the prize game, "is it $D$?" has answers of probability $\tfrac18$ and $\tfrac78$:
>
> $$
> I_{\text{yes}} = 3\ \text{bits}, \qquad I_{\text{no}} = -\log_2\tfrac78 \simeq 0.193\ \text{bits}, \qquad H(\text{answer}) = \tfrac18(3) + \tfrac78(0.193) \simeq 0.544\ \text{bits} .
> $$
>
> So $I_{\text{yes}} > 1$ bit is possible, but by [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|Theorem §C4a.1.2]] with $n = 2$,
>
> $$
> H(\text{answer}) \le H\bigl(\tfrac12, \tfrac12\bigr) = 1\ \text{bit},
> $$
>
> with equality for "is it $A$?" (answers $\tfrac12, \tfrac12$). A question strategy is a prefix code, so by [[§C4a.1 Shannon Entropy#^thm-c4a-1-3|Theorem §C4a.1.3]] no strategy averages fewer than $H[p] = \tfrac74$ questions; the one in [[§C4a.1 Shannon Entropy#^ex-c4a-1-1|Example §C4a.1.1]] attains this.
>
> *Source: Mao §4.1, box "Information and surprisal"*

^ex-c4a-1-4

> [!remark]- Connections
> - The same entropy, in natural units and over microstates, is the quantity statistical mechanics maximizes — [[§C4a.2 The Entropy of a Statistical State|§C4a.2]], [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^pr-c4a-3-1|Principle §C4a.3.1]].
> - The binary entropy function of Chapter C2 is $H$ for two outcomes, in nats — [[§C2.2 Typicality in Large Systems#^def-c2-2-1|Def. §C2.2.1]].
> - A biased coin coded in pairs is worked in [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption#^ex-c4a-11-1|Example §C4a.11.1]].
