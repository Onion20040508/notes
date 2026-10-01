---
type: section
subject: "[[Group Theory]]"
chapter: 2
section: 8
tags: [group-theory, math493]
---
← [[§7 The Group ℤ∕nℤ]] · ↑ [[· 2 Arithmetic Modulo n]] · [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem]] →

*Reference: Pinter Ch. 22 (greatest common divisors), Ch. 23, Thm. 1 (linear congruences).*

> [!definition] Definition §8.1: Greatest Common Divisor; Coprime
> For integers $a, b$ not both zero, the **greatest common divisor** $\gcd(a, b)$ is the largest positive integer dividing both $a$ and $b$. We say $a$ and $b$ are **coprime** (or **relatively prime**) if $\gcd(a, b) = 1$, i.e. they share no factor other than $1$. For example, $\gcd(12, 18) = 6$; $\gcd(3, 8) = 1$; $\gcd(2, 8) = 2$; $\gcd(a, p) = 1$ for every prime $p$ and every $a \in \{1, \ldots, p-1\}$.

^def-8-1

> [!remark]- Connections
> - Same definitions: [[§11 Properties of Finite Sets#^def-11-2|250 Def. §11.2]] (gcd) and [[§11 Properties of Finite Sets#^def-11-3|250 Def. §11.3]] (coprime); the gcd is computed by [[§16 The Euclidean Algorithm#^thm-16-3|250 Thm. §16.3]] (Euclidean algorithm).

> [!definition] Definition §8.2: Invertibility Modulo $n$
> Fix $n \geq 1$. An integer $a$ (or its class $[a]$) is **invertible modulo $n$** if there is an integer $x$ with
>
> $$ ax \equiv 1 \pmod n, $$
>
> i.e. $ax = 1 + kn$ for some $k$: some multiple of $a$ is one more than a multiple of $n$. Such an $x$ is called an **inverse of $a$ modulo $n$**, and $[x]$ is written $[a]^{-1}$. An invertible class is also called a **unit** modulo $n$.

^def-8-2

> [!remark]- Connections
> - Same definition: [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-5|250 Def. §21.5]].

> [!example] Example §8.1: Inverses Modulo 5 and Modulo 8
> Modulo $5$: $2 \cdot 3 = 6 \equiv 1$, so $[2]^{-1} = [3]$ and $[3]^{-1} = [2]$; $4 \cdot 4 = 16 \equiv 1$, so $[4]^{-1} = [4]$ (unsurprising, as $[4] = [-1]$); and $[1]^{-1} = [1]$. Every nonzero class is invertible.
>
> Modulo $8$: $3 \cdot 3 = 9 \equiv 1$, $\ 5 \cdot 5 = 25 \equiv 1$, $\ 7 \cdot 7 = 49 \equiv 1$, so $[3], [5], [7]$ are each their own inverse. But $[2]$ is *not* invertible: the multiples of $2$ modulo $8$ are $2, 4, 6, 0, 2, 4, 6, 0, \ldots$ — all even, while $1 + 8k$ is always odd — so $2x \equiv 1 \pmod 8$ has no solution. The same argument rules out $[4]$ and $[6]$, and $[0]$ is never invertible. The invertible classes modulo $8$ are exactly $\{[1], [3], [5], [7]\}$.

^ex-8-1

> [!remark] Remark: Why Integers Have No Inverses but Classes Can
> In $\mathbb{Z}$ itself, $2x = 1$ has no solution, so $(\mathbb{Z}, \cdot)$ is not a group. Passing to classes modulo $n$ relaxes “$= 1$” to “$= 1 + kn$”, and $2 \cdot 3 = 6 = 1 + 5$ is now good enough modulo $5$. Nothing has been added to $\mathbb{Z}$; rather, $1$ has been identified with all its translates $1 + 5k$, and one of them happens to be a multiple of $2$. This is why modular arithmetic can turn multiplication into a group operation while ordinary integer multiplication never can.

^rem-8-1

> [!theorem] Proposition §8.1: Invertibility Criterion
> Fix $n \geq 1$ and $a \in \mathbb{Z}$. Then $[a]$ is invertible modulo $n$ if and only if $\gcd(a, n) = 1$.

^prop-8-1

> [!proof]+ Proof
> ($\Rightarrow$) Suppose $ax = 1 + kn$, so $ax - kn = 1$. Any positive integer $d$ dividing both $a$ and $n$ divides $ax - kn = 1$, hence $d = 1$. So $\gcd(a, n) = 1$.
>
> ($\Leftarrow$) Suppose $\gcd(a, n) = 1$. By [[§5 A Zoo of Subgroups#^cor-5-2|Bézout's identity]] (proved later in this section as a corollary of the classification of subgroups of $\mathbb{Z}$), there are integers $x, y$ with $ax + ny = 1$. Reading this modulo $n$: $ax = 1 - ny \equiv 1 \pmod n$, so $[x]$ is an inverse of $[a]$.

^pf-8-1

*Uses:* [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]], [[§8 Invertibility and Unit Groups#^def-8-2|Def. §8.2]], [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]]

> [!remark]- Connections
> - Same result: [[§21 Congruence Classes and the Arithmetic of Remainders#^cor-21-9|250 Cor. §21.9]]; the Bézout step is [[§17 Consequences of the Euclidean Algorithm#^prop-17-3|250 Prop. §17.3]].

> [!example] Example §8.2: Deciding Invertibility Modulo 5, 6, 7, and 8
> Applying the criterion to every class (inverses found by trial multiplication):
>
> **$n = 5$**
>
> | $a$ | $\gcd(a,5)$ | $[a]^{-1}$ |
> |---|---|---|
> | $0$ | $5$ | — |
> | $1$ | $1$ | $[1]$ |
> | $2$ | $1$ | $[3]$ |
> | $3$ | $1$ | $[2]$ |
> | $4$ | $1$ | $[4]$ |
>
> **$n = 6$**
>
> | $a$ | $\gcd(a,6)$ | $[a]^{-1}$ |
> |---|---|---|
> | $0$ | $6$ | — |
> | $1$ | $1$ | $[1]$ |
> | $2$ | $2$ | — |
> | $3$ | $3$ | — |
> | $4$ | $2$ | — |
> | $5$ | $1$ | $[5]$ |
>
> **$n = 7$**
>
> | $a$ | $\gcd(a,7)$ | $[a]^{-1}$ |
> |---|---|---|
> | $0$ | $7$ | — |
> | $1$ | $1$ | $[1]$ |
> | $2$ | $1$ | $[4]$ |
> | $3$ | $1$ | $[5]$ |
> | $4$ | $1$ | $[2]$ |
> | $5$ | $1$ | $[3]$ |
> | $6$ | $1$ | $[6]$ |
>
> **$n = 8$**
>
> | $a$ | $\gcd(a,8)$ | $[a]^{-1}$ |
> |---|---|---|
> | $0$ | $8$ | — |
> | $1$ | $1$ | $[1]$ |
> | $2$ | $2$ | — |
> | $3$ | $1$ | $[3]$ |
> | $4$ | $4$ | — |
> | $5$ | $1$ | $[5]$ |
> | $6$ | $2$ | — |
> | $7$ | $1$ | $[7]$ |
>
> Checks: mod $5$, $2 \cdot 3 = 6 \equiv 1$ and $4 \cdot 4 = 16 \equiv 1$; mod $6$, $5 \cdot 5 = 25 \equiv 1$; mod $7$, $2 \cdot 4 = 8 \equiv 1$, $3 \cdot 5 = 15 \equiv 1$, $6 \cdot 6 = 36 \equiv 1$; mod $8$, $3^2 = 9$, $5^2 = 25$, $7^2 = 49$, all $\equiv 1$.
>
> Observations. For the primes $5$ and $7$, every nonzero class is invertible, and the inverses pair up ($2 \leftrightarrow 3$ mod $5$; $2 \leftrightarrow 4$, $3 \leftrightarrow 5$ mod $7$) except for $[1]$ and $[-1]$, which are their own inverses. For $n = 6$, only $[1]$ and $[5] = [-1]$ survive. For $n = 8$, all four units are their own inverses — a feature not shared by $U_5$, even though both have four elements. In each case the invertible classes are exactly those coprime to $n$.

^ex-8-2

> [!example] Example §8.3: Computing an Inverse by the Extended Euclidean Algorithm
> Find $[7]^{-1}$ modulo $26$. Since $\gcd(7, 26) = 1$, an inverse exists; to *compute* it, run the Euclidean algorithm and back-substitute to obtain [[§5 A Zoo of Subgroups#^cor-5-2|Bézout]] coefficients:
>
> $$ 26 = 3 \cdot 7 + 5, \qquad 7 = 1 \cdot 5 + 2, \qquad 5 = 2 \cdot 2 + 1. $$
>
> Working backwards,
>
> $$ 1 = 5 - 2 \cdot 2 = 5 - 2(7 - 5) = 3 \cdot 5 - 2 \cdot 7 = 3(26 - 3 \cdot 7) - 2 \cdot 7 = 3 \cdot 26 - 11 \cdot 7. $$
>
> So $7 \cdot (-11) \equiv 1 \pmod{26}$, and $[7]^{-1} = [-11] = [15]$. Check: $7 \cdot 15 = 105 = 4 \cdot 26 + 1$. For small moduli, trial multiplication is faster (as in the mod-$8$ table), but this algorithm is the general method.

^ex-8-3

> [!remark]- Connections
> - The same back-substitution in 250: [[§17 Consequences of the Euclidean Algorithm#^ex-17-1|250 Ex. §17.1]].

> [!example] Example §8.4: Solving Linear Congruences
> **Invertible coefficient.** Solve $3x \equiv 5 \pmod 7$. Since $\gcd(3, 7) = 1$, $[3]$ is invertible, with $[3]^{-1} = [5]$ (as $3 \cdot 5 = 15 \equiv 1$). Multiplying through: $x \equiv 5 \cdot 5 = 25 \equiv 4 \pmod 7$, and this is the *unique* solution modulo $7$ ([[§2 First Consequences of the Axioms#^prop-2-7|Unique Solvability]]). Check: $3 \cdot 4 = 12 \equiv 5$.
>
> **Non-invertible coefficient.** Consider $4x \equiv b \pmod 6$. Here $\gcd(4, 6) = 2$, so $[4]$ is not invertible and the equation is not guaranteed a unique solution. The values of $4x \bmod 6$ for $x = 0, \ldots, 5$ are $0, 4, 2, 0, 4, 2$. So $4x \equiv 1$ has *no* solution, while $4x \equiv 2$ has *two* solutions, $x \equiv 2$ and $x \equiv 5$. Both failures — nonexistence and nonuniqueness — are exactly what the absence of an inverse permits; an invertible coefficient rules out both.

^ex-8-4

> [!remark]- Connections
> - The general rule behind both cases: [[§20 Linear Congruences#^thm-20-4|250 Thm. §20.4]] (solvable iff $\gcd(a, n) \mid b$, then with $\gcd(a, n)$ solutions).

> [!definition] Definition §8.3: Euler's Totient Function
> For $n \geq 1$, **Euler's totient** $\varphi(n)$ is the number of integers $a$ with $1 \leq a \leq n$ and $\gcd(a, n) = 1$, i.e. the number of invertible classes modulo $n$. Once $U_n$ is defined [[§8 Invertibility and Unit Groups#^def-8-4|below]], $\varphi(n) = |U_n|$.

^def-8-3

> [!remark]- Connections
> - Computed from the prime factorization in [[§21 The Structure of Uₙ#^cor-21-3|Euler's Totient Formula]].
> - Same definition in 250, with $\varphi(p^k)$ computed: [[§23 The Sequence of Prime Numbers#^ex-23-5|250 Ex. §23.5]].

> [!example] Example §8.5: The Unit Groups for Small $n$
> Listing the classes coprime to $n$:
>
> | $n$ | $U_n$ | $\vert U_n\vert$ |
> |---|---|---|
> | $2$ | $\{1\}$ | $1$ |
> | $3$ | $\{1, 2\}$ | $2$ |
> | $4$ | $\{1, 3\}$ | $2$ |
> | $5$ | $\{1, 2, 3, 4\}$ | $4$ |
> | $6$ | $\{1, 5\}$ | $2$ |
> | $7$ | $\{1, 2, 3, 4, 5, 6\}$ | $6$ |
> | $8$ | $\{1, 3, 5, 7\}$ | $4$ |
> | $9$ | $\{1, 2, 4, 5, 7, 8\}$ | $6$ |
> | $10$ | $\{1, 3, 7, 9\}$ | $4$ |
> | $11$ | $\{1, 2, \ldots, 10\}$ | $10$ |
> | $12$ | $\{1, 5, 7, 11\}$ | $4$ |
>
> (Brackets omitted.) For prime $p$, $U_p$ is everything except $[0]$, of size $p - 1$. The sizes are the values of Euler's totient $\varphi(n)$; note that it is not monotone in $n$ ($\varphi(12) = 4 < \varphi(11) = 10$). Observe also that $U_5$, $U_8$, $U_{10}$, $U_{12}$ all have four elements but need not be “the same” group — comparing them is the subject of [[· 4 Homomorphisms and Isomorphisms|Worksheet 2]].

^ex-8-5

> [!theorem] Proposition §8.2: Multiplication by a Nonzero Class Permutes the Nonzero Classes Modulo $p$
> Let $p$ be prime and $p \nmid a$. Then $[x] \mapsto [a][x]$ is a bijection of $\{[1], \ldots, [p-1]\}$ onto itself. In particular $[a]$ is invertible modulo $p$.

^prop-8-2

> [!proof]+ Proof
> For $1 \leq x \leq p-1$, $p \nmid ax$ by Euclid's Lemma ([[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]]; it depends only on Bézout, [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]]), so the products land among the nonzero classes. They are pairwise distinct: if $ai \equiv aj$, then $p \mid a(i-j)$, so $p \mid i - j$ by Euclid's Lemma, forcing $i = j$. So the $p - 1$ products occupy $p - 1$ distinct nonzero classes, i.e. all of them, including $[1]$: some $x$ has $ax \equiv 1$.

^pf-8-2

*Uses:* [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|§9.1]], [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[§6 Divisibility and Congruence#^def-6-4|Def. §6.4]], [[§8 Invertibility and Unit Groups#^def-8-2|Def. §8.2]]

> [!remark]- Connections
> - The same bijection drives the proof of Fermat's little theorem in [[§24★ Congruence Modulo a Prime#^thm-24-1|250 Thm. §24.1]].

> [!remark] Remark: Finiteness Plus Cancellation
> This is a second proof of ($\Leftarrow$) of the [[§8 Invertibility and Unit Groups#^prop-8-1|Invertibility Criterion]] for prime moduli, and it exposes the real reason inverses exist. In $\mathbb{Z}$ the argument collapses: the multiples $2, 4, 6, \ldots$ are all distinct, but there are infinitely many slots, so nothing forces one of them to be $1$. *Finiteness plus cancellation forces inverses.*

^rem-8-2

![[m493-8-1.svg]]
*Finiteness plus cancellation. Left: multiplication by $3$ on the six nonzero classes modulo $7$ is injective, hence onto, so some arrow must land on $1$: here $3 \cdot 5 \equiv 1$ (red), i.e. $[3]^{-1} = [5]$. Right: multiplication by $4$ on $\mathbb{Z}/6\mathbb{Z}$, where $\gcd(4, 6) = 2$, sends two classes to each even class and misses $1, 3, 5$ (dashed red), so $4x \equiv 1$ has no solution and $4x \equiv 2$ has two, as in Example §8.4.*

> [!definition] Definition §8.4: The Unit Group $(\mathbb{Z}/n\mathbb{Z})^\times = U_n$
> Fix an integer $n \geq 1$. Define
>
> $$ U_n = (\mathbb{Z}/n\mathbb{Z})^\times = \{[a] \in \mathbb{Z}/n\mathbb{Z} : \gcd(a, n) = 1\}, \qquad [a] \cdot [b] := [ab]. $$
>
> Then $U_n$ is an abelian group under multiplication, with identity $[1]$, called the **unit group modulo $n$**. By the [[§8 Invertibility and Unit Groups#^prop-8-1|Invertibility Criterion]], $U_n$ is precisely the set of classes that are invertible (“units”) modulo $n$: $U_n$ is what remains of $\mathbb{Z}/n\mathbb{Z}$ after discarding every class that has no multiplicative inverse. For example, $U_5 = \{[1],[2],[3],[4]\}$, $U_6 = \{[1],[5]\}$, $U_8 = \{[1],[3],[5],[7]\}$, and $U_p = \{[1], \ldots, [p-1]\}$ for $p$ prime.

^def-8-4

> [!theorem] Proposition §8.3: $U_n$ Is a Group
> The set $U_n$ with the operation $[a][b] = [ab]$ is a well-defined abelian group.

^prop-8-3

> [!proof]+ Proof
> We verify each point in turn. Throughout we use [[§5 A Zoo of Subgroups#^cor-5-2|Bézout's identity]]: $\gcd(a, n) = 1$ if and only if there exist $x, y \in \mathbb{Z}$ with $ax + ny = 1$ (as in the [[§8 Invertibility and Unit Groups#^prop-8-1|Invertibility Criterion]] above).
>
> **Membership is well-defined:** If $[a] = [a']$, then $a' = a + kn$, and $\gcd(a', n) = \gcd(a + kn, n) = \gcd(a, n)$ (any common divisor of $a$ and $n$ divides $a + kn$, and conversely). So the condition $\gcd(a, n) = 1$ depends only on the class $[a]$.
>
> **The operation is well-defined:** If $a' = a + kn$ and $b' = b + ln$, then $a'b' = ab + n(al + bk + kln) \equiv ab \pmod n$, so $[a'b'] = [ab]$.
>
> **Closure:** Suppose $\gcd(a, n) = \gcd(b, n) = 1$. Choose $x, y, u, v \in \mathbb{Z}$ with $ax + ny = 1$ and $bu + nv = 1$. Multiplying:
>
> $$ 1 = (ax + ny)(bu + nv) = (ab)(xu) + n(axv + byu + nyv), $$
>
> which exhibits $\gcd(ab, n) = 1$ by Bézout. So $[a][b] = [ab] \in U_n$.
>
> **Identity:** $\gcd(1, n) = 1$, so $[1] \in U_n$, and $[1][a] = [a][1] = [a]$.
>
> **Inverses:** Given $[a] \in U_n$, choose $x, y$ with $ax + ny = 1$. Then $ax \equiv 1 \pmod n$, so $[a][x] = [x][a] = [1]$. Moreover $[x] \in U_n$: the same equation $xa + ny = 1$ exhibits $\gcd(x, n) = 1$. So $[a]^{-1} = [x]$.
>
> **Associativity and commutativity** are inherited from $\mathbb{Z}$ exactly as for $\mathbb{Z}/n\mathbb{Z}$ ([[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]]).

^pf-8-3

*Uses:* [[§5 A Zoo of Subgroups#^cor-5-2|§5.2]], [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]], [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]], [[§8 Invertibility and Unit Groups#^def-8-4|Def. §8.4]], [[§7 The Group ℤ∕nℤ#^def-7-2|Def. §7.2]], [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]], [[§1 The Definition of a Group#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - The structure of $U_n$ via the Chinese Remainder Theorem: [[§21 The Structure of Uₙ#^thm-21-2|Uₙ as a Product of Prime-Power Unit Groups]] (PS 1.6(3)).
> - Its multiplication tables for small $n$: [[§14 Multiplication Tables#^ex-14-3|Table of U₇]], [[§14 Multiplication Tables#^ex-14-4|Table of U₈]].

> [!remark] Remark: Computing Inverses in $U_n$
> The proof is constructive: the extended Euclidean algorithm computes the Bézout coefficients, hence the inverse. E.g. in $U_{10} = \{[1], [3], [7], [9]\}$: from $3 \cdot 7 = 21 \equiv 1$, $[3]^{-1} = [7]$.

^rem-8-3

> [!theorem] Proposition §8.4: $\mathbb{Z}/n\mathbb{Z}$ Is a Field if and only if $n$ Is Prime
> For $n \geq 2$, $\mathbb{Z}/n\mathbb{Z}$ with its addition and multiplication is a field if and only if $n$ is prime. For $p$ prime this field is written $\mathbb{F}_p$, and $\mathbb{F}_p^\times = U_p = \mathbb{Z}/p\mathbb{Z} \setminus \{[0]\}$.

^prop-8-4

> [!proof]+ Proof
> $(\mathbb{Z}/n\mathbb{Z}, +)$ is an abelian group, and multiplication of classes is well defined, associative, commutative, has identity $[1] \neq [0]$, and distributes over addition, all inherited from $\mathbb{Z}$ exactly as in the verification for $U_n$ ([[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]]). So $\mathbb{Z}/n\mathbb{Z}$ is a field iff every nonzero class is invertible. If $n = p$ is prime, every $a \in \{1, \ldots, p-1\}$ has $\gcd(a, p) = 1$, so every nonzero class is a unit by the [[§8 Invertibility and Unit Groups#^prop-8-1|Invertibility Criterion]]. If $n = ab$ with $1 < a, b < n$, then $[a] \neq [0]$ but $\gcd(a, n) = a \neq 1$, so $[a]$ is not invertible (indeed $[a][b] = [0]$).

^pf-8-4

*Uses:* [[§3 Basic Examples of Groups#^def-3-3|Def. §3.3]], [[§7 The Group ℤ∕nℤ#^prop-7-1|§7.1]], [[§8 Invertibility and Unit Groups#^prop-8-3|§8.3]], [[§8 Invertibility and Unit Groups#^prop-8-1|§8.1]], [[§8 Invertibility and Unit Groups#^def-8-1|Def. §8.1]]

> [!remark]- Connections
> - Finite fields beyond $\mathbb{F}_p$: [[§39 Simple Groups#^ex-39-2|The Field F₉]] and the [[§39 Simple Groups#^thm-39-12|Classification of Finite Fields]].
