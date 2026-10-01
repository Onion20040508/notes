---
type: section
subject: "[[Group Theory]]"
chapter: 2
section: 9
tags: [group-theory, math493]
---
← [[§8 Invertibility and Unit Groups]] · ↑ [[· 2 Arithmetic Modulo n]] · [[§10 Cycle Notation and the Group S₃]] →

*Reference: Pinter Ch. 22 (factoring into primes), Ch. 23 (simultaneous congruences).*

> [!theorem] Lemma §9.1: Euclid's Lemma
> Let $p$ be prime and $a, b \in \mathbb{Z}$. If $p \mid ab$, then $p \mid a$ or $p \mid b$. More generally, if $\gcd(c, a) = 1$ and $c \mid ab$, then $c \mid b$.
>
> *Source: cf. Pinter Ch. 22*

^lem-9-1

> [!proof]+ Proof
> Suppose $\gcd(c, a) = 1$ and $c \mid ab$. By [[§5 A Zoo of Subgroups#^cor-5-2|Bézout]], $cx + ay = 1$ for some $x, y$. Multiply by $b$: $b = cbx + aby$. Both terms are divisible by $c$ (the second since $c \mid ab$), so $c \mid b$. For prime $p$: if $p \nmid a$, then $\gcd(p, a) = 1$ (the only positive divisors of $p$ are $1$ and $p$), so the general statement gives $p \mid b$.

^pf-9-1

*Uses:* [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[§6 Divisibility and Congruence#^def-6-1|Def. §6.1]], [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - Elementary versions: [[§23 The Sequence of Prime Numbers#^thm-23-2|250 Thm. §23.2]] (prime case) and [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|250 Thm. §17.4]] (coprime case).

> [!theorem] Theorem §9.2: Unique Prime Factorization
> Every integer $n \geq 2$ can be written as a product of primes $n = p_1 p_2 \cdots p_k$, and this expression is unique up to the order of the factors. Equivalently, $n = p_1^{a_1} \cdots p_r^{a_r}$ with distinct primes $p_i$ and exponents $a_i \geq 1$, uniquely.
>
> *Source: cf. Pinter Ch. 22, Thms. 4–5; MATH 412*

^thm-9-2

> [!proof]+ Proof
> **Existence** by strong induction on $n$: if $n$ is prime, done; otherwise $n = ab$ with $1 < a, b < n$, and each of $a, b$ is a product of primes by induction, so $n$ is too.
>
> **Uniqueness** by induction on $n$. Suppose $n = p_1 \cdots p_k = q_1 \cdots q_l$ with all $p_i, q_j$ prime. Then $p_1 \mid q_1 \cdots q_l$, so by [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]] (applied repeatedly) $p_1 \mid q_j$ for some $j$; as $q_j$ is prime, $p_1 = q_j$. Cancel this common factor: $p_2 \cdots p_k = \prod_{i \neq j} q_i$, a smaller number, whose factorization is unique by induction. So the multisets $\{p_i\}$ and $\{q_j\}$ coincide.

^pf-9-2

*Uses:* [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]], [[§1 The Set ℕ of Natural Numbers#^rem-1-3|451 §1 (strong induction)]]

> [!remark]- Connections
> - Elementary version: [[§23 The Sequence of Prime Numbers#^thm-23-5|250 Thm. §23.5]] (Fundamental Theorem of Arithmetic), with existence in [[§23 The Sequence of Prime Numbers#^prop-23-1|250 Prop. §23.1]].

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
> **Well-defined:** if $x \equiv x' \pmod{mn}$, then $mn \mid x - x'$, hence $m \mid x - x'$ and $n \mid x - x'$. **Homomorphism:** $\rho([x] + [y]) = ([x + y]_m, [x + y]_n) = \rho([x]) + \rho([y])$. **Injective:** if $\rho([x]) = \rho([y])$, then $m \mid x - y$ and $n \mid x - y$; write $x - y = mt$; then $n \mid mt$ with $\gcd(n, m) = 1$, so $n \mid t$ by [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]], and $mn \mid x - y$. **Surjective:** both sides have $mn$ elements and $\rho$ is injective. (Constructively: with $mu + nv = 1$ from [[§5 A Zoo of Subgroups#^cor-5-2|Bézout]], $x = s\,mu + r\,nv$ satisfies $x \equiv r \pmod m$ and $x \equiv s \pmod n$.) The several-moduli version follows by induction, since $\gcd(m_1 \cdots m_{k-1}, m_k) = 1$ when the $m_i$ are pairwise coprime.

^pf-9-3

*Uses:* [[§7 The Group ℤ∕nℤ#^def-7-1|Def. §7.1]], [[§7 The Group ℤ∕nℤ#^def-7-2|Def. §7.2]], [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§15 Homomorphisms#^def-15-1|Def. §15.1]], [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]], [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 §1.1]]

> [!remark]- Connections
> - Applied to unit groups in [[§21 The Structure of Uₙ#^thm-21-2|Uₙ as a Product of Prime-Power Unit Groups]] (PS 1.6(3)).

> [!example] Example §9.1: A CRT Computation
> Solve $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$. [[§5 A Zoo of Subgroups#^cor-5-2|Bézout]]: $2 \cdot 3 - 1 \cdot 5 = 1$, so $u = 2$, $v = -1$ with $m = 3$, $n = 5$. Then $x = s\,mu + r\,nv = 3 \cdot 6 + 2 \cdot (-5) = 8$. Check: $8 \equiv 2 \pmod 3$, $8 \equiv 3 \pmod 5$; all solutions are $8 + 15k$.

^ex-9-1

![[m493-9-1.svg]]
*$\mathbb{Z}/15\mathbb{Z} \to \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z}$ as a grid: each $x \in \{0, \ldots, 14\}$ sits in row $x \bmod 3$ and column $x \bmod 5$, and every cell is filled exactly once, which is the bijectivity of $\rho$. (Counting $0, 1, 2, \ldots$ steps diagonally, wrapping around in both directions.) The system of the example asks for row $2$ (blue) and column $3$ (red); they meet in the single cell $8$.*

> [!remark] Remark: The Dependency Chain in $\mathbb{Z}$
> Everything above descends from one idea: [[§6 Divisibility and Congruence#^lem-6-1|division algorithm]] $\Rightarrow$ subgroups of $\mathbb{Z}$ are $n\mathbb{Z}$ ([[§5 A Zoo of Subgroups#^prop-5-1|§5.1]]) $\Rightarrow$ [[§5 A Zoo of Subgroups#^cor-5-2|Bézout]] $\Rightarrow$ [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|Euclid's lemma]] $\Rightarrow$ [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|unique factorization]]; and Bézout $\Rightarrow$ [[§8 Invertibility and Unit Groups#^prop-8-1|invertibility criterion]], $U_n$ is a group ([[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]]), and the [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|Chinese Remainder Theorem]]. These are the “basic number-theoretic facts” that [[493 Problem Set 1|Problem Set 1]] permits as assumptions.

^rem-9-1

> [!remark] Remark: The Division-Algorithm Pattern
> “Take the smallest positive element, then divide with remainder” is a pattern to remember: the same argument classified subgroups of cyclic groups in the [[§21 Algebra Prerequisites꞉ Groups#^prop-21-1|590 notes]] and will return for ideals of $\mathbb{Z}$ and of polynomial rings. Note the corollary: *every* subgroup of $\mathbb{Z}$ is generated by a single element ([[§5 A Zoo of Subgroups#^prop-5-1|§5.1]]).

^rem-9-2

> [!remark]- Connections
> - The same argument in this course: [[§17 Cyclic Groups#^thm-17-4|Subgroups of Cyclic Groups Are Cyclic]].
