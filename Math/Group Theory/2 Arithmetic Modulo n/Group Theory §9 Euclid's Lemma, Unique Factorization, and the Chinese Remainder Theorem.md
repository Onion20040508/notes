---
type: section
subject: "[[Group Theory]]"
chapter: 2
section: 9
tags: [group-theory, math493]
---
← [[Group Theory §8 Invertibility and Unit Groups]] · ↑ [[Group Theory — 2 Arithmetic Modulo n]] · [[Group Theory §10 Cycle Notation and the Group S₃]] →

*Reference: Pinter Ch. 22 (factoring into primes), Ch. 23 (simultaneous congruences).*

> [!theorem] Lemma §9.1: Euclid's Lemma
> Let $p$ be prime and $a, b \in \mathbb{Z}$. If $p \mid ab$, then $p \mid a$ or $p \mid b$. More generally, if $\gcd(c, a) = 1$ and $c \mid ab$, then $c \mid b$.
>
> *Source: cf. Pinter Ch. 22*

^lem-9-1

> [!proof]+ Proof
> Suppose $\gcd(c, a) = 1$ and $c \mid ab$. By [[Group Theory §5 A Zoo of Subgroups#^cor-5-2|Bézout]], $cx + ay = 1$ for some $x, y$. Multiply by $b$: $b = cbx + aby$. Both terms are divisible by $c$ (the second since $c \mid ab$), so $c \mid b$. For prime $p$: if $p \nmid a$, then $\gcd(p, a) = 1$ (the only positive divisors of $p$ are $1$ and $p$), so the general statement gives $p \mid b$.

^pf-9-1

*Uses:* [[Group Theory §5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[Group Theory §6 Divisibility and Congruence#^def-6-1|Def. §6.1]], [[Group Theory §8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]]

> [!theorem] Theorem §9.2: Unique Prime Factorization
> Every integer $n \geq 2$ can be written as a product of primes $n = p_1 p_2 \cdots p_k$, and this expression is unique up to the order of the factors. Equivalently, $n = p_1^{a_1} \cdots p_r^{a_r}$ with distinct primes $p_i$ and exponents $a_i \geq 1$, uniquely.
>
> *Source: cf. Pinter Ch. 22, Thms. 4–5; MATH 412*

^thm-9-2

> [!proof]+ Proof
> **Existence** by strong induction on $n$: if $n$ is prime, done; otherwise $n = ab$ with $1 < a, b < n$, and each of $a, b$ is a product of primes by induction, so $n$ is too.
>
> **Uniqueness** by induction on $n$. Suppose $n = p_1 \cdots p_k = q_1 \cdots q_l$ with all $p_i, q_j$ prime. Then $p_1 \mid q_1 \cdots q_l$, so by [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]] (applied repeatedly) $p_1 \mid q_j$ for some $j$; as $q_j$ is prime, $p_1 = q_j$. Cancel this common factor: $p_2 \cdots p_k = \prod_{i \neq j} q_i$, a smaller number, whose factorization is unique by induction. So the multisets $\{p_i\}$ and $\{q_j\}$ coincide.

^pf-9-2

*Uses:* [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]], [[Single Variable Analysis §1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]], [[Single Variable Analysis §1 The Set ℕ of Natural Numbers#^rem-1-3|451 §1 (strong induction)]]

> [!theorem] Theorem §9.3: Chinese Remainder Theorem
> Let $m, n \geq 1$ with $\gcd(m, n) = 1$. Then the map
>
> $$ \rho: \mathbb{Z}/mn\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}, \qquad [x]_{mn} \mapsto ([x]_m, [x]_n), $$
>
> is a well-defined bijection, and a homomorphism of additive groups. Equivalently: for any $r, s \in \mathbb{Z}$ the system $x \equiv r \pmod m$, $x \equiv s \pmod n$ has a solution, unique modulo $mn$. The same holds for any finite family of pairwise coprime moduli $m_1, \ldots, m_k$, with $\mathbb{Z}/m_1 \cdots m_k \mathbb{Z} \to \prod_i \mathbb{Z}/m_i\mathbb{Z}$.
>
> *Source: cf. Pinter Ch. 23, Thms. 3–4; MATH 412*

^thm-9-3

> [!proof]+ Proof
> **Well-defined:** if $x \equiv x' \pmod{mn}$, then $mn \mid x - x'$, hence $m \mid x - x'$ and $n \mid x - x'$. **Homomorphism:** $\rho([x] + [y]) = ([x + y]_m, [x + y]_n) = \rho([x]) + \rho([y])$. **Injective:** if $\rho([x]) = \rho([y])$, then $m \mid x - y$ and $n \mid x - y$; write $x - y = mt$; then $n \mid mt$ with $\gcd(n, m) = 1$, so $n \mid t$ by [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]], and $mn \mid x - y$. **Surjective:** both sides have $mn$ elements and $\rho$ is injective. (Constructively: with $mu + nv = 1$ from [[Group Theory §5 A Zoo of Subgroups#^cor-5-2|Bézout]], $x = s\,mu + r\,nv$ satisfies $x \equiv r \pmod m$ and $x \equiv s \pmod n$.) The several-moduli version follows by induction, since $\gcd(m_1 \cdots m_{k-1}, m_k) = 1$ when the $m_i$ are pairwise coprime.

^pf-9-3

*Uses:* [[Group Theory §7 The Group ℤ∕nℤ#^def-7-1|Def. §7.1]], [[Group Theory §7 The Group ℤ∕nℤ#^def-7-2|Def. §7.2]], [[Group Theory §3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[Group Theory §15 Homomorphisms#^def-15-1|Def. §15.1]], [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]], [[Group Theory §5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[Single Variable Analysis §1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

> [!remark]- Connections
> - Applied to unit groups in [[Group Theory §21 The Structure of Uₙ#^thm-21-2|Uₙ as a Product of Prime-Power Unit Groups]] (PS 1.6(3)).

> [!example] Example §9.1: A CRT Computation
> Solve $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$. [[Group Theory §5 A Zoo of Subgroups#^cor-5-2|Bézout]]: $2 \cdot 3 - 1 \cdot 5 = 1$, so $u = 2$, $v = -1$ with $m = 3$, $n = 5$. Then $x = s\,mu + r\,nv = 3 \cdot 6 + 2 \cdot (-5) = 8$. Check: $8 \equiv 2 \pmod 3$, $8 \equiv 3 \pmod 5$; all solutions are $8 + 15k$.

^ex-9-1

> [!remark] Remark: The Dependency Chain in $\mathbb{Z}$
> Everything above descends from one idea: [[Group Theory §6 Divisibility and Congruence#^lem-6-1|division algorithm]] $\Rightarrow$ subgroups of $\mathbb{Z}$ are $n\mathbb{Z}$ ([[Group Theory §5 A Zoo of Subgroups#^prop-5-1|§5.1]]) $\Rightarrow$ [[Group Theory §5 A Zoo of Subgroups#^cor-5-2|Bézout]] $\Rightarrow$ [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]] $\Rightarrow$ [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|unique factorization]]; and Bézout $\Rightarrow$ [[Group Theory §8 Invertibility and Unit Groups#^prop-8-1|invertibility criterion]], $U_n$ is a group ([[Group Theory §8 Invertibility and Unit Groups#^prop-8-3|§8.3]]), and the [[Group Theory §9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Chinese Remainder Theorem]]. These are the “basic number-theoretic facts” that [[Group Theory — Problem Set 1|Problem Set 1]] permits as assumptions.

^rem-9-1

> [!remark] Remark: The Division-Algorithm Pattern
> “Take the smallest positive element, then divide with remainder” is a pattern to remember: the same argument classified subgroups of cyclic groups in the [[Topology §21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 notes]] and will return for ideals of $\mathbb{Z}$ and of polynomial rings. Note the corollary: *every* subgroup of $\mathbb{Z}$ is generated by a single element ([[Group Theory §5 A Zoo of Subgroups#^prop-5-1|§5.1]]).

^rem-9-2

> [!remark]- Connections
> - The same argument in this course: [[Group Theory §17 Cyclic Groups#^thm-17-4|Subgroups of Cyclic Groups Are Cyclic]].
