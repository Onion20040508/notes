---
type: section
subject: "[[Group Theory]]"
chapter: 5
section: 21
tags: [group-theory, math493]
---
← [[§20 The Sign Homomorphism and the Alternating Group]] · ↑ [[5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] · [[§22 Equivalence Relations and Partitions]] →

*Reference: Pinter Ch. 23.*

*Source: [[493 Problem Set 1#^hw-1-6|PS 1.6(3)]].*

> [!theorem] Lemma §21.1: Coprime to Each Factor, Coprime to the Product
> If $\gcd(m, P) = 1$ and $\gcd(m, Q) = 1$, then $\gcd(m, PQ) = 1$. Hence if $\gcd(m, P_i) = 1$ for $i = 1, \ldots, r$, then $\gcd(m, P_1 \cdots P_r) = 1$.

^lem-21-1

> [!proof]+ Proof
> By [[§5 A Zoo of Subgroups#^cor-5-2|Bézout]], $mx + Py = 1$ and $mu + Qv = 1$; multiplying, $1 = m(mxu + xQv + Pyu) + PQ(yv)$, so any common divisor of $m$ and $PQ$ divides $1$. Induct on $r$ for the second statement. (This is the [[§8 Invertibility and Unit Groups#^prop-8-3|closure computation]] of $U_n$ with the roles of the arguments exchanged.)

^pf-21-1

*Uses:* [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

> [!theorem] Theorem §21.2: $U_n$ as a Product of Prime-Power Unit Groups
> Let $n = p_1^{a_1} \cdots p_r^{a_r}$ be the prime factorization of $n$, and write $P_i = p_i^{a_i}$. The map
>
> $$
> \varphi: (\mathbb{Z}/n\mathbb{Z})^\times \to \prod_{i=1}^r (\mathbb{Z}/P_i\mathbb{Z})^\times, \qquad [m]_n \mapsto \big([m]_{P_1}, \ldots, [m]_{P_r}\big),
> $$
>
> is an isomorphism of groups. In particular $|U_n| = \prod_i |U_{P_i}|$.
>
> *Source: PS 1.6(3)*

^thm-21-2

> [!proof]+ Proof
> The $P_i$ are pairwise coprime (a common prime factor of $P_i$ and $P_j$ would be both $p_i$ and $p_j$ by [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|unique factorization]]), so the [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Chinese Remainder Theorem]] applies to them, and the product group is a group by iterating [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|§18.3]].
>
> **Well-defined.** If $m' = m + kn$, then since $P_i \mid n$, $m' \equiv m \pmod{P_i}$ for each $i$, so the tuple depends only on $[m]_n$. And if $\gcd(m, n) = 1$, then $\gcd(m, P_i) = 1$ for each $i$ (a common divisor of $m$ and $P_i$ divides $n$), so the tuple lies in the product of unit groups.
>
> **Homomorphism.** $[ab]_{P_i} = [a]_{P_i}[b]_{P_i}$ for each $i$ ([[§8 Invertibility and Unit Groups#^prop-8-3|well-definedness of multiplication]] modulo $P_i$), so $\varphi([a][b]) = \varphi([ab]) = \varphi([a])\varphi([b])$ componentwise.
>
> **Injective.** If $\varphi([a]) = \varphi([b])$, then $a \equiv b \pmod{P_i}$ for every $i$, so by the uniqueness clause of the [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Chinese Remainder Theorem]], $a \equiv b \pmod n$. (Alternatively: $P_1 \mid a - b$, and inductively $P_1 \cdots P_j \mid a - b$ implies $P_1 \cdots P_{j+1} \mid a - b$ by [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]], since $\gcd(P_{j+1}, P_1 \cdots P_j) = 1$.)
>
> **Surjective.** Given $([m_1]_{P_1}, \ldots, [m_r]_{P_r})$ with $\gcd(m_i, P_i) = 1$, the existence clause of the [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Chinese Remainder Theorem]] gives $m$ with $m \equiv m_i \pmod{P_i}$ for all $i$. Then $\gcd(m, P_i) = \gcd(m_i, P_i) = 1$ for each $i$, so $\gcd(m, n) = 1$ by [[§21 The Structure of Uₙ#^lem-21-1|Coprime to Each Factor, Coprime to the Product]], $[m]_n \in U_n$, and $\varphi([m]_n)$ is the given tuple.

^pf-21-2

*Uses:* [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|§9.2]], [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9.3]], [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]], [[§18 Conjugation, Products, and Pointwise Products#^prop-18-3|§18.3]], [[§8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]], [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]], [[§21 The Structure of Uₙ#^lem-21-1|§21.1]], [[§16 Isomorphisms#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - Products of groups in MATH 590: [[§21 Algebra Prerequisites꞉ Groups#^def-21-5|Direct Product of Groups]] (590 §21.5).

> [!theorem] Corollary §21.3: Euler's Totient Formula
> If $n = p_1^{a_1} \cdots p_r^{a_r}$ is the prime factorization of $n$, then
>
> $$
> \varphi(n) = \prod_{i=1}^{r} \varphi(p_i^{a_i}) = \prod_{i=1}^{r} (p_i - 1)\,p_i^{a_i - 1}.
> $$

^cor-21-3

> [!proof]+ Proof
> The first equality is $|U_n| = \prod_i |U_{p_i^{a_i}}|$, from the theorem $U_n$ as a Product of Prime-Power Unit Groups ([[§21 The Structure of Uₙ#^thm-21-2|§21.2]]). For a prime power $p^a$, an integer $m$ with $0 \leq m < p^a$ fails to be coprime to $p^a$ iff $p \mid m$ (the only prime dividing $p^a$ is $p$), and there are $p^{a-1}$ such $m$, namely $0, p, 2p, \ldots, (p^{a-1} - 1)p$. So $\varphi(p^a) = p^a - p^{a-1} = (p - 1)p^{a-1}$.

^pf-21-3

*Uses:* [[§21 The Structure of Uₙ#^thm-21-2|§21.2]], [[§8 Invertibility and Unit Groups#^def-8-3|Def. §8.3]], [[§8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]]

> [!example] Example §21.1: Unit Groups via the Decomposition
> Combined with the facts stated without proof on the [[493 Problem Set 1#^hw-1-6|problem set]] — $U_{p^a}$ is cyclic of order $(p-1)p^{a-1}$ for odd $p$, and $U_{2^a}$ is trivial ($a = 1$), $\mathbb{Z}/2\mathbb{Z}$ ($a = 2$), or $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2^{a-2}\mathbb{Z}$ ($a \geq 3$) — the theorem describes every $U_n$ as a product of cyclic groups. Examples: $U_{15} \cong U_3 \times U_5 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ (not cyclic); $U_{10} \cong U_2 \times U_5 \cong \mathbb{Z}/4\mathbb{Z}$ (cyclic, generated by $3$); $U_{24} \cong U_8 \times U_3 \cong (\mathbb{Z}/2\mathbb{Z})^3$ (every element of order $\leq 2$, as observed in the 412 material).

^ex-21-1

![[m493-21-1.svg]]
*[[§21 The Structure of Uₙ#^thm-21-2|Theorem §21.2]] for $n = 15 = 3 \cdot 5$: the class of $m$ sits in row $m \bmod 3$ and column $m \bmod 5$, and by the Chinese Remainder Theorem each cell holds exactly one class. The units (blue) are exactly the cells avoiding row $0$ and column $0$, a $2 \times 4$ block $U_3 \times U_5$; hence $U_{15} \cong U_3 \times U_5$ and $\varphi(15) = 2 \cdot 4 = 8$.*

> [!remark]- Connections
> - Replacing factors by isomorphic ones: [[§21 Algebra Prerequisites꞉ Groups#^thm-21-7|Products of Isomorphic Groups]] (590 §21.7).
