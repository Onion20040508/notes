---
type: section
subject: "[[Logic and Proofs]]"
chapter: 6
section: 23
eccles: "Ch. 23"
aliases: ["Eccles 23"]
tags: [logic-and-proofs, mat250]
---
← [[§22b The Congruence 290x ≡ 5 (mod 357)]] · ↑ [[· 6 Prime Numbers]] · [[§24★ Congruence Modulo a Prime]] →

*Eccles, Chapter 23 (with Problems VI) · MAT 250 HW8 (Exercises 23.2, 23.4, 23.6; Problems VI Q3, Q7, Q8).*

Primes are the multiplicative building blocks of the positive integers. This section proves that every integer $n > 1$ is a product of primes, and that the product is unique apart from the order of the factors (the fundamental theorem of arithmetic); the key step is Euclid's property $p \mid ab \Rightarrow p \mid a$ or $p \mid b$, which rests on the Euclidean algorithm through [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]]. Unique factorization then gives the divisors and greatest common divisors of a number, a second proof that $\sqrt 2$ is irrational (first proved in [[§13 Number Systems#^thm-13-4|Theorem §13.4]]), and a toolkit for HW8. The section ends with Euclid's proof that there are infinitely many primes and a look at how they are distributed.

## 23.1 Definition and Basic Properties

> [!definition] Definition §23.1: Prime
> A positive integer $n$ is **prime** if $n > 1$ and the only positive divisors of $n$ are $1$ and $n$.
>
> If a prime $p = ab$ with $a, b$ positive, then $\{a, b\} = \{1, p\}$.
>
> *Eccles: Definition 23.1.1*

^def-23-1

> [!definition] Definition §23.2: Composite
> An integer $n > 1$ that is not prime is **composite**.
>
> Thus $n > 1$ is composite if and only if $n = ab$ for integers $a, b$ with $1 < a < n$ and $1 < b < n$ (a positive divisor $a \ne 1, n$ gives $b = n/a$, which also lies strictly between $1$ and $n$). The positive integers split into three disjoint sets: the primes $2, 3, 5, 7, 11, 13, \ldots$, the composites $4, 6, 8, 9, 10, \ldots$, and the single **unit** $1$.
>
> *Eccles: Definition 23.1.1*

^def-23-2

> [!theorem] Proposition §23.1: Existence of Prime Factorizations
> Every integer greater than $1$ can be written as a product of prime numbers. (A prime counts as a product of one prime; with the convention that the empty product is $1$, the statement extends to $n = 1$.)
>
> *Eccles: Proposition 23.1.2*

^prop-23-1

> [!proof]+ Proof
> By strong induction on $n \ge 2$, the classic example of the method.
>
> *Base case.* $2$ is prime, so it is a product of a single prime.
>
> *Inductive step.* Suppose, for some $k \ge 2$, that every $n$ with $2 \le n \le k$ is a product of primes. If $k + 1$ is prime, it is a product of one prime. Otherwise $k + 1$ is composite, so $k + 1 = ab$ with $2 \le a, b \le k$ ([[§23 The Sequence of Prime Numbers#^def-23-2|Def. §23.2]]). By the inductive hypothesis $a$ and $b$ are products of primes, and putting the two products side by side writes $k + 1$ as a product of primes.
>
> *Conclusion.* By strong induction, every $n \ge 2$ is a product of primes.

^pf-23-1

*Uses:* [[§23 The Sequence of Prime Numbers#^def-23-1|Def. §23.1]], [[§23 The Sequence of Prime Numbers#^def-23-2|Def. §23.2]], [[§5 The Induction Principle#^thm-5-6|§5.6]] (strong induction)

> [!theorem] Theorem §23.2: Euclid's Property of Primes
> Let $p$ be a prime and $a, b$ positive integers. If $p \mid ab$, then $p \mid a$ or $p \mid b$.
>
> The same holds for arbitrary integers $a, b$.
>
> *Eccles: Theorem 23.1.3 (stated for positive $a, b$; extended here to all integers)*

^thm-23-2

> [!proof]+ Proof
> Suppose $p \mid ab$ and $p \nmid a$. The positive divisors of $p$ are $1$ and $p$, and $p$ is not a divisor of $a$, so the only positive common divisor of $p$ and $a$ is $1$: $\gcd(p, a) = 1$. By [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]], $p \mid ab$ with $\gcd(p, a) = 1$ gives $p \mid b$. Hence $p \mid a$ or $p \mid b$.
>
> For arbitrary integers: if $a = 0$ or $b = 0$, then $p$ divides that factor. Otherwise $p \mid ab$ gives $p \mid \abs{a}\,\abs{b}$, the first part gives $p \mid \abs{a}$ or $p \mid \abs{b}$, and $p \mid \abs{x} \iff p \mid x$.

^pf-23-2

*Uses:* [[§23 The Sequence of Prime Numbers#^def-23-1|Def. §23.1]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|§17.4]], [[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]], [[§11 Properties of Finite Sets#^def-11-3|Def. §11.3]]

> [!remark]- Connections
> - Same result in group theory, proved there via Bézout: [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|493 Lemma §9.1]] (Euclid's lemma, together with the general form $\gcd(c, a) = 1,\ c \mid ab \Rightarrow c \mid b$).

> [!remark] Remark: Constructing the Proof
> The conclusion is an "or" statement, so we prove it by assuming that the first alternative fails and deducing the second (as in [[§4 Proof by Contradiction#^ex-4-3|Example §4.3]]):
>
> | Given | Goal |
> |---|---|
> | $p$ prime, $p \mid ab$, $p \nmid a$ | $p \mid b$ |
>
> Because $p$ is prime, its only divisors are $\pm 1$ and $\pm p$, so these are the only candidates for a common divisor of $p$ and $a$; if $p \nmid a$, only $\pm 1$ remain, and $p$ and $a$ are coprime. The rest is already proved, as [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]] (Eccles 17.3.2): *if $a$ and $b$ are coprime and $a \mid bc$, then $a \mid c$.* So the proof above only has to check coprimality and cite it; the Bézout argument is not repeated.

^rem-23-1

> [!remark] Remark: Euclid's Property Characterizes the Primes
> Conversely, an integer $n > 1$ with the property "$n \mid ab \Rightarrow n \mid a$ or $n \mid b$" is prime. For if $n$ is composite, write $n = ab$ with $1 < a, b < n$; then $n \mid ab$, but $n \nmid a$ and $n \nmid b$ since $0 < a, b < n$. So among the integers $n > 1$, Euclid's property is equivalent to being prime, and in more advanced algebra (rings other than $\mathbb{Z}$) it is taken as the definition of a prime element. [[§23 The Sequence of Prime Numbers#^ex-23-2|Example §23.2]] shows a number system where the two notions come apart.

^rem-23-2

## 23.2 The Sieve of Eratosthenes

To decide whether $n$ is prime one can try all smaller divisors; the next result shows that it suffices to try the primes up to $\sqrt n$.

> [!theorem] Proposition §23.3: A Composite Number Has a Small Prime Factor
> If $n \ge 2$ is composite, then $n$ has a prime factor $p \le \sqrt n$.
>
> *Eccles: Proposition 23.2.1*

^prop-23-3

> [!proof]+ Proof
> Write $n = ab$ with $1 < a, b < n$. If $a \le \sqrt n$, then $a \ge 2$ has a prime factor $p$ ([[§23 The Sequence of Prime Numbers#^prop-23-1|Prop. §23.1]]), and $p \mid a \mid n$ with $p \le a \le \sqrt n$. If $a > \sqrt n$, then $b = n/a < n/\sqrt n = \sqrt n$, and a prime factor of $b$ works in the same way.

^pf-23-3

*Uses:* [[§23 The Sequence of Prime Numbers#^def-23-1|Def. §23.1]], [[§23 The Sequence of Prime Numbers#^def-23-2|Def. §23.2]], [[§23 The Sequence of Prime Numbers#^prop-23-1|§23.1]]

> [!example] Example §23.1: The Primes up to 100
> Write out $2, 3, \ldots, 100$. The first number, $2$, is prime; cross out its other multiples, which are composite. The first number not crossed out, $3$, is prime (it is not a multiple of a smaller prime); cross out its other multiples. Continue with $5$ and $7$. Since every composite $n \le 100$ has a prime factor $\le \sqrt{100} = 10$ ([[§23 The Sequence of Prime Numbers#^prop-23-3|Prop. §23.3]]), and the primes $\le 10$ are $2, 3, 5, 7$, every composite number has now been crossed out. What remains are the primes below $100$:
>
> $$
> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 \qquad (25 \text{ in all}).
> $$
>
> (Eccles's Exercise 23.1 continues to $200$, using the primes up to $13$; there are $46$ primes below $200$.)
>
> *Eccles: Example 23.2.2*

^ex-23-1

![[m250-23-1.svg]]
*The sieve on $1, \ldots, 100$. Each composite is coloured by the round in which it is first crossed out (multiples of $2$, then of $3$, $5$, $7$); after four rounds nothing composite is left, because every composite up to $100$ has a prime factor at most $10$. The framed numbers are the $25$ primes; $1$, neither prime nor composite, is left plain.*

## 23.3 The Fundamental Theorem of Arithmetic

Factorization into primes is not unique as written, since the factors can be reordered: $12 = 2 \times 2 \times 3 = 2 \times 3 \times 2 = 3 \times 2 \times 2$. Writing the factors in non-decreasing order removes this freedom, and then the factorization is unique. The proof needs Euclid's property for products of more than two factors.

> [!theorem] Proposition §23.4: A Prime Dividing a Product Divides a Factor
> Let $p$ be a prime and $a_1, \ldots, a_m$ positive integers. If $p \mid a_1 a_2 \cdots a_m$, then $p \mid a_i$ for some $i$ with $1 \le i \le m$.
>
> *Eccles: Proposition 23.3.2*

^prop-23-4

> [!proof]+ Proof
> By induction on $m$. For $m = 1$ the statement reads "$p \mid a_1 \Rightarrow p \mid a_1$", which is true. Suppose the result holds for $m = k$, and let $p \mid a_1 \cdots a_k a_{k+1}$. Then
>
> $$
> \begin{aligned}
> p \mid (a_1 \cdots a_k)\, a_{k+1}
> &\;\Rightarrow\; p \mid a_1 \cdots a_k \ \text{ or } \ p \mid a_{k+1} && \text{(Theorem §23.2)} \\
> &\;\Rightarrow\; p \mid a_i \text{ for some } 1 \le i \le k \ \text{ or } \ p \mid a_{k+1} && \text{(inductive hypothesis)} \\
> &\;\Rightarrow\; p \mid a_i \text{ for some } 1 \le i \le k + 1 ,
> \end{aligned}
> $$
>
> which is the statement for $m = k + 1$. By induction it holds for all $m \in \mathbb{Z}^+$.

^pf-23-4

*Uses:* [[§23 The Sequence of Prime Numbers#^thm-23-2|§23.2]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

> [!theorem] Theorem §23.5: Fundamental Theorem of Arithmetic
> Every integer $n > 1$ can be written uniquely as a product of primes with the factors in non-decreasing order. Equivalently, $n$ can be written uniquely as
>
> $$
> n = p_1^{k_1} p_2^{k_2} \cdots p_r^{k_r}, \qquad r \ge 1,\quad k_i \in \mathbb{Z}^+,\quad p_1 < p_2 < \cdots < p_r \text{ primes}.
> $$
>
> *Eccles: Theorem 23.3.1*

^thm-23-5

> [!proof]+ Proof
> Existence is [[§23 The Sequence of Prime Numbers#^prop-23-1|Proposition §23.1]] (then sort the factors). We prove uniqueness by contradiction. Suppose some $n > 1$ has two different factorizations
>
> $$
> n = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s, \qquad p_1 \le \cdots \le p_r,\quad q_1 \le \cdots \le q_s ,
> $$
>
> all $p_i, q_j$ prime. Whenever some $p_i$ equals some $q_j$, cancel it from both sides (cancellation by a nonzero integer); repeat until no prime on the left equals a prime on the right. We are left with an equation $p'_1 \cdots p'_u = q'_1 \cdots q'_v$ in which $p'_i \ne q'_j$ for all $i, j$.
> - If $u = v = 0$, everything cancelled: the two lists contain the same primes, each the same number of times, and so written in non-decreasing order they are identical — contrary to our assumption.
> - If exactly one of $u, v$ is $0$, one side is $1$ and the other is a nonempty product of primes, hence $\ge 2$: impossible.
> - So $u, v \ge 1$. Now $p'_1$ divides the left side, hence $p'_1 \mid q'_1 \cdots q'_v$, and by [[§23 The Sequence of Prime Numbers#^prop-23-4|Proposition §23.4]] $p'_1 \mid q'_j$ for some $j$. As $q'_j$ is prime and $p'_1 > 1$, this forces $p'_1 = q'_j$, contradicting $p'_i \ne q'_j$.
>
> Every case is impossible, so the factorization is unique. The second form is the first with equal primes collected into powers.

^pf-23-5

*Uses:* [[§23 The Sequence of Prime Numbers#^prop-23-1|§23.1]], [[§23 The Sequence of Prime Numbers#^prop-23-4|§23.4]], [[§23 The Sequence of Prime Numbers#^def-23-1|Def. §23.1]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]

> [!remark]- Connections
> - Same theorem in group theory: [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|493 Thm. §9.2]] (uniqueness there by induction on $n$ rather than by contradiction).

> [!definition] Definition §23.3: Standard Prime Factorization
> The unique expression $n = p_1^{k_1} \cdots p_r^{k_r}$ of [[§23 The Sequence of Prime Numbers#^thm-23-5|Theorem §23.5]] (primes $p_1 < \cdots < p_r$, exponents $k_i \ge 1$) is the **standard prime factorization** of $n$; for $n = 1$ take $r = 0$ (the empty product). When comparing two numbers it is convenient to list all primes occurring in either and allow exponents $0$: by uniqueness, $p_1^{k_1} \cdots p_r^{k_r} = p_1^{l_1} \cdots p_r^{l_r}$ (distinct primes, exponents $\ge 0$) implies $k_i = l_i$ for every $i$.
>
> *Eccles: §23.3 (text after Theorem 23.3.1)*

^def-23-3

> [!example] Example §23.2: Unique Factorization Fails for E-primes
> Let $E$ be the set of even integers, and call an even integer **E-prime** if it is not the product of two other even integers. Then $60$ is a product of E-primes in two genuinely different ways:
>
> $$
> 60 = 2 \times 30 = 6 \times 10 .
> $$
>
> *Which positive even numbers are E-prime.* A positive even $n$ is E-prime if and only if $n = 2k$ with $k$ odd. If $k$ is odd and $2k = (2s)(2t)$ with $s, t$ integers, then $2k = 4st$, so $k = 2st$ is even, a contradiction; so $2k$ is E-prime. If instead $4 \mid n$, say $n = 4m$, then $n = 2 \cdot 2m$ is a product of two even integers different from $n$, so $n$ is not E-prime.
>
> *The two factorizations.* $2 = 2 \cdot 1$, $30 = 2 \cdot 15$, $6 = 2 \cdot 3$ and $10 = 2 \cdot 5$ all have the form $2 \times \text{odd}$, so all four factors are E-prime, and the factorizations $\{2, 30\}$ and $\{6, 10\}$ are not reorderings of each other.
>
> What goes wrong is Euclid's property: inside $E$, $2$ "divides" $6 \times 10 = 2 \times 30$, but $2$ divides neither $6$ nor $10$ within $E$ ($6 = 2 \times 3$ and $3 \notin E$). Compare [[§23 The Sequence of Prime Numbers#^rem-23-2|the remark on Euclid's property]]. (Eccles's Exercise 23.7 asks for another example, among the numbers $4q + 1$; his solution: the "pseudo-primes" $9, 21, 49$ give $441 = 9 \times 49 = 21 \times 21$.)
>
> *Source: HW8*
> *Eccles: Problems VI Q3*

^ex-23-2

## 23.4 Applications of the Fundamental Theorem

> [!theorem] Proposition §23.6: The Divisors of a Number
> Let $a = p_1^{k_1} p_2^{k_2} \cdots p_r^{k_r}$ be the standard prime factorization of a positive integer $a$. Then a positive integer $b$ divides $a$ if and only if
>
> $$
> b = p_1^{l_1} p_2^{l_2} \cdots p_r^{l_r} \qquad \text{with } 0 \le l_i \le k_i \text{ for } 1 \le i \le r .
> $$
>
> *Eccles: Proposition 23.4.1*

^prop-23-6

> [!proof]+ Proof
> ($\Leftarrow$) If $b$ has this form, then $a = bq$ with $q = p_1^{k_1 - l_1} \cdots p_r^{k_r - l_r}$, an integer since every $k_i - l_i \ge 0$.
>
> ($\Rightarrow$) Let $a = bq$ with $b, q$ positive. Every prime $p$ dividing $b$ divides $a = p_1 \cdots p_1 \, p_2 \cdots p_r$ (each $p_i$ written $k_i$ times), so $p = p_i$ for some $i$ by [[§23 The Sequence of Prime Numbers#^prop-23-4|Proposition §23.4]] (a prime dividing a prime equals it). The same applies to $q$. So $b = p_1^{l_1} \cdots p_r^{l_r}$ and $q = p_1^{m_1} \cdots p_r^{m_r}$ with exponents $\ge 0$, and
>
> $$
> p_1^{k_1} \cdots p_r^{k_r} = a = bq = p_1^{l_1 + m_1} \cdots p_r^{l_r + m_r} .
> $$
>
> By uniqueness ([[§23 The Sequence of Prime Numbers#^def-23-3|Def. §23.3]]), $k_i = l_i + m_i$, so $0 \le l_i \le k_i$.

^pf-23-6

*Uses:* [[§23 The Sequence of Prime Numbers#^prop-23-4|§23.4]], [[§23 The Sequence of Prime Numbers#^thm-23-5|§23.5]], [[§23 The Sequence of Prime Numbers#^def-23-3|Def. §23.3]]

> [!theorem] Corollary §23.7: The gcd from Prime Factorizations
> Let $a, b$ be positive integers and $p_1 < \cdots < p_r$ the primes occurring in the factorization of $a$ or of $b$, so that $a = p_1^{k_1} \cdots p_r^{k_r}$ and $b = p_1^{l_1} \cdots p_r^{l_r}$ with $k_i, l_i \ge 0$. Then
>
> $$
> \gcd(a, b) = p_1^{m_1} \cdots p_r^{m_r}, \qquad m_i = \min(k_i, l_i).
> $$
>
> *Eccles: Corollary 23.4.3*

^cor-23-7

> [!proof]+ Proof
> By [[§23 The Sequence of Prime Numbers#^prop-23-6|Proposition §23.6]] (primes with exponent $0$ simply do not occur), the positive common divisors of $a$ and $b$ are exactly the numbers $p_1^{e_1} \cdots p_r^{e_r}$ with $e_i \le k_i$ and $e_i \le l_i$, i.e. $0 \le e_i \le m_i$. One of them is $d = p_1^{m_1} \cdots p_r^{m_r}$, and by the same proposition every other one divides $d$, hence is $\le d$. So $d$ is the greatest common divisor.

^pf-23-7

*Uses:* [[§23 The Sequence of Prime Numbers#^prop-23-6|§23.6]], [[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]]

> [!example] Example §23.3: Divisors of 72; gcd(72, 30)
> $72 = 2^3 \times 3^2$, so its divisors are $2^{l_1} 3^{l_2}$ with $0 \le l_1 \le 3$, $0 \le l_2 \le 2$: these are $1, 2, 4, 8, 3, 6, 12, 24, 9, 18, 36, 72$ — twelve divisors, $(3 + 1)(2 + 1)$. With $30 = 2 \times 3 \times 5$, write $72 = 2^3 \times 3^2 \times 5^0$ and $30 = 2^1 \times 3^1 \times 5^1$; then $\gcd(72, 30) = 2^1 \times 3^1 \times 5^0 = 6$, as found by listing divisors in [[§11 Properties of Finite Sets#^ex-11-4|Example §11.4]] and by the Euclidean algorithm in [[§16 The Euclidean Algorithm#^ex-16-1|Example §16.1]].
>
> This is not a practical way to find the gcd of large numbers: factorizing is slow, while the Euclidean algorithm is fast.
>
> *Eccles: Examples 23.4.2, 23.4.4*

^ex-23-3

*Chain: earlier in [[§18b The Pair (72, 30)|Chapter 4]]*

> [!example] Example §23.4: gcd(4148, 7684) by Factorization
> *Factorize.* $4148 = 4 \times 1037$, and trying primes up to $\sqrt{1037} < 33$ finds $1037 = 17 \times 61$; $61$ is prime (no prime $\le 7$ divides it, [[§23 The Sequence of Prime Numbers#^prop-23-3|Prop. §23.3]]). Similarly $7684 = 4 \times 1921$ and $1921 = 17 \times 113$, with $113$ prime (no prime $\le 10$ divides it). So
>
> $$
> 4148 = 2^2 \times 17 \times 61, \qquad 7684 = 2^2 \times 17 \times 113 .
> $$
>
> *gcd.* By [[§23 The Sequence of Prime Numbers#^cor-23-7|Corollary §23.7]], $\gcd(4148, 7684) = 2^2 \times 17 = 68$ — the value the Euclidean algorithm gave in HW7 ([[§16 The Euclidean Algorithm#^ex-16-3|Example §16.3]]), with less work there.
>
> *Source: HW8*
> *Eccles: Exercise 23.2*

^ex-23-4

*Chain: earlier in [[§18a The Pair (7684, 4148)|Chapter 4]]*

> [!example] Example §23.5: Euler's Totient of a Prime Power
> Euler's totient $\phi(n)$ is the number of integers $m$ with $1 \le m \le n$ and $\gcd(m, n) = 1$. For a prime $p$ and $k \ge 1$,
>
> $$
> \phi(p^k) = p^k - p^{k-1} .
> $$
>
> *Solution.* The positive divisors of $p^k$ are $1, p, \ldots, p^k$ ([[§23 The Sequence of Prime Numbers#^prop-23-6|Prop. §23.6]]), so $\gcd(m, p^k) \in \{1, p, \ldots, p^k\}$, and $\gcd(m, p^k) \ne 1$ exactly when $p \mid m$. The multiples of $p$ in $\{1, \ldots, p^k\}$ are $pq$ with $1 \le q \le p^{k-1}$: there are $p^{k-1}$ of them. The remaining $p^k - p^{k-1}$ numbers are coprime to $p^k$. For example $\phi(8) = 4$ (namely $1, 3, 5, 7$) and $\phi(9) = 6$.
>
> *Eccles: Exercise 23.5*

^ex-23-5

> [!remark]- Connections
> - The totient in group theory: [[§8 Invertibility and Unit Groups#^def-8-3|493 Def. §8.3]] ($\phi(n) = \abs{U_n}$), and the general formula $\phi(p_1^{a_1} \cdots p_r^{a_r}) = \prod (p_i - 1) p_i^{a_i - 1}$, [[§22 The Structure of Uₙ#^cor-22-3|493 Cor. §22.3]] (Eccles sets it as Problems VI Q10).

> [!example] Example §23.6: No Rational Square or Cube Root of 2
> **(a) $\sqrt 2$** (a second proof of [[§13 Number Systems#^thm-13-4|Theorem §13.4]], Eccles 13.2.1, which is proved there by parity). Suppose $q \in \mathbb{Q}$ with $q^2 = 2$. Since $(-q)^2 = q^2$ we may assume $q > 0$, and write $q = a/b$ with $a, b \in \mathbb{Z}^+$. Then $a^2 = 2b^2$. Let $2 < p_2 < \cdots < p_r$ be the odd primes occurring in $a$ or $b$, and write $a = 2^{k_1} p_2^{k_2} \cdots p_r^{k_r}$, $b = 2^{l_1} p_2^{l_2} \cdots p_r^{l_r}$ with exponents $\ge 0$. Then
>
> $$
> a^2 = 2^{2k_1} p_2^{2k_2} \cdots p_r^{2k_r}, \qquad 2b^2 = 2^{2l_1 + 1} p_2^{2l_2} \cdots p_r^{2l_r} .
> $$
>
> By uniqueness ([[§23 The Sequence of Prime Numbers#^def-23-3|Def. §23.3]]) the exponents of $2$ agree: $2k_1 = 2l_1 + 1$, an even number equal to an odd one. Contradiction.
>
> *What this proof adds.* The proof in §13 needs a fraction in lowest terms and the lemma "$a^2$ even $\Rightarrow$ $a$ even", and has to be redone for each new case. Here neither is needed: the only input is unique factorization, and the contradiction is a count of exponents. The same count works for cube roots in (b), for $\sqrt p$ with any prime $p$ (the exponent of $p$ gives $2k = 2l + 1$), and for $\sqrt n$ whenever some prime occurs in $n$ to an odd power; it also explains [[§13 Number Systems#^ex-13-2|Example §13.2]], since $4 = 2^2$ has even exponents.
>
> **(b) $\sqrt[3]{2}$.** Suppose $q \in \mathbb{Q}$ with $q^3 = 2$. If $q \le 0$ then $q^3 \le 0$; so $q > 0$ and $q = a/b$ with $a, b \in \mathbb{Z}^+$, and $a^3 = 2b^3$. With $a, b$ factorized as in (a),
>
> $$
> a^3 = 2^{3k_1} p_2^{3k_2} \cdots p_r^{3k_r}, \qquad 2b^3 = 2^{3l_1 + 1} p_2^{3l_2} \cdots p_r^{3l_r},
> $$
>
> and uniqueness gives $3k_1 = 3l_1 + 1$, i.e. $3(k_1 - l_1) = 1$, impossible for integers. So no rational number has cube $2$.
>
> The same argument shows that $\sqrt[n]{2}$ is irrational for every $n \ge 2$: the exponent of $2$ would satisfy $n k_1 = n l_1 + 1$.
>
> *Source: HW8*
> *Eccles: Theorem 13.2.1 (proof in §23.4); Exercise 23.6*
>
> *The HW8 solution of (b) takes $a, b \in \mathbb{Z}$; factorization into primes needs $a, b > 0$, which is arranged by first noting $q > 0$.*

^ex-23-6

> [!remark]- Connections
> - [[§2 The Set ℚ of Rational Numbers#^thm-2-1|451 Thm. §2.1]] (irrationality of $\sqrt 2$) and its generalization [[§2 The Set ℚ of Rational Numbers#^prop-2-2|451 Prop. §2.2]] (rational square roots of integers are integers).

*Chain: earlier in [[§14b √2|Chapter 3]]*

> [!example] Example §23.7: Coprime to Each Factor, Coprime to the Product
> Let $a, b, c$ be positive integers. If $\gcd(a, b) = 1$ and $\gcd(a, c) = 1$, then $\gcd(a, bc) = 1$.
>
> *Solution.* Suppose for contradiction that $d = \gcd(a, bc) > 1$. Then $d$ has a prime factor $p$ ([[§23 The Sequence of Prime Numbers#^prop-23-1|Prop. §23.1]]), and $p \mid a$, $p \mid bc$. By [[§23 The Sequence of Prime Numbers#^thm-23-2|Theorem §23.2]], $p \mid b$ or $p \mid c$. In the first case $p > 1$ is a common divisor of $a$ and $b$, contradicting $\gcd(a, b) = 1$; in the second it is a common divisor of $a$ and $c$, contradicting $\gcd(a, c) = 1$. Hence $\gcd(a, bc) = 1$. (Signs play no role, since $\gcd$ depends only on $\abs{a}, \abs{b}, \abs{c}$.)
>
> *Source: HW8*
> *Eccles: Problems VI Q7 (printed "$a$ and $be$" for "$a$ and $bc$")*
>
> *The HW8 page leaves this question blank.*

^ex-23-7

> [!remark]- Connections
> - The same statement, proved with Bézout and used for the structure of $U_n$: [[§22 The Structure of Uₙ#^lem-22-1|493 Lemma §22.1]].

> [!example] Example §23.8: Coprime Factors of a Square
> Let $a, b$ be coprime positive integers. Then $ab$ is a perfect square if and only if $a$ and $b$ are both perfect squares. (Positivity matters: $a = b = -1$ are coprime and $ab = 1$ is a square.)
>
> *Step 1: squares in terms of exponents.* A positive integer $n = p_1^{k_1} \cdots p_r^{k_r}$ (standard factorization) is a perfect square if and only if every $k_i$ is even. If all $k_i = 2e_i$, then $n = (p_1^{e_1} \cdots p_r^{e_r})^2$. Conversely, if $n = m^2$ and $m = q_1^{e_1} \cdots q_s^{e_s}$ is the standard factorization of $m$, then $n = q_1^{2e_1} \cdots q_s^{2e_s}$ is a standard factorization of $n$, so by uniqueness ([[§23 The Sequence of Prime Numbers#^thm-23-5|Theorem §23.5]]) the $p_i$ are the $q_i$ and $k_i = 2e_i$.
>
> *Step 2.* Write $a = p_1^{k_1} \cdots p_m^{k_m}$ and $b = q_1^{l_1} \cdots q_n^{l_n}$ (standard factorizations). No $p_i$ equals any $q_j$, for a common prime would be a common divisor $> 1$ of $a$ and $b$. Hence
>
> $$
> ab = p_1^{k_1} \cdots p_m^{k_m}\, q_1^{l_1} \cdots q_n^{l_n}
> $$
>
> is, after sorting, the standard factorization of $ab$, and its exponents are exactly the $k_i$ together with the $l_j$. By Step 1: $ab$ is a square $\iff$ all $k_i$ and all $l_j$ are even $\iff$ $a$ and $b$ are both squares.
>
> *Source: HW8*
> *Eccles: Problems VI Q8*

^ex-23-8

## 23.5 The Distribution of Prime Numbers

The sequence of primes is very irregular, but it never stops. The proof is from Book IX of Euclid's *Elements* and is one of the classic proofs by contradiction.

> [!theorem] Theorem §23.8: There Are Infinitely Many Primes
> The set of prime numbers is infinite.
>
> *Eccles: Theorem 23.5.1*

^thm-23-8

> [!proof]+ Proof
> Suppose for contradiction that the set $P$ of primes is finite, say $P = \{p_1, p_2, \ldots, p_n\}$. Consider
>
> $$
> m = p_1 p_2 \cdots p_n + 1 .
> $$
>
> For each $i$, $m = p_i \cdot \bigl(\prod_{j \ne i} p_j\bigr) + 1$ with $0 \le 1 < p_i$, so by the division theorem ([[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]) the remainder of $m$ on division by $p_i$ is $1$, and $p_i \nmid m$. But $m \ge 2 + 1 > 1$, so $m$ is a product of primes ([[§23 The Sequence of Prime Numbers#^prop-23-1|Proposition §23.1]]) and is divisible by some prime $p$. This $p$ is not any $p_i$, so $p \notin P$ — contradicting that $P$ contains all primes. Hence the set of primes is infinite.

^pf-23-8

*Uses:* [[§23 The Sequence of Prime Numbers#^prop-23-1|§23.1]], [[§15 The Division Theorem#^thm-15-1|§15.1]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]

> [!example] Example §23.9: Arbitrarily Long Runs of Composite Numbers
> For each positive integer $n$ there are $n$ consecutive integers that are all composite: the numbers
>
> $$
> (n+1)! + 2,\ (n+1)! + 3,\ \ldots,\ (n+1)! + (n+1) .
> $$
>
> *Solution.* Let $2 \le i \le n + 1$. Since $i$ is one of the factors of $(n+1)! = 1 \cdot 2 \cdots (n+1)$,
>
> $$
> (n+1)! + i = i \left( \frac{(n+1)!}{i} + 1 \right),
> $$
>
> where $(n+1)!/i = 1 \cdot 2 \cdots (i-1)(i+1) \cdots (n+1)$ is a positive integer. Both factors are at least $2$ and so less than the product, hence $(n+1)! + i$ is composite. As $i$ runs from $2$ to $n + 1$ we get $n$ consecutive composite integers. (For $n = 3$: $26, 27, 28$.) So although there are infinitely many primes, the gaps between consecutive primes are unbounded.
>
> *Source: HW8*
> *Eccles: Exercise 23.4*

^ex-23-9

> [!example] Example §23.10: Formulas That Look Prime but Are Not
> - Euler showed that $n^2 - n + 41$ is prime for $1 \le n \le 40$, but it is not prime for every $n$: at $n = 41$ it equals $41^2 - 41 + 41 = 41^2$.
> - The number $m = p_1 \cdots p_n + 1$ in Euclid's proof need not itself be prime: $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$. The proof only uses that its prime factors are new.
>
> *Eccles: Exercise 23.3 and its solution; §23.5 (text)*
> *Source: standard (the example $30031$)*

^ex-23-10

> [!definition] Definition §23.4: The Prime-Counting Function
> For $n \in \mathbb{Z}^+$, $\pi(n)$ denotes the number of primes not exceeding $n$. Thus $\pi(2) = 1$, $\pi(10) = 4$, $\pi(100) = 25$, $\pi(1000) = 168$, $\pi(10^6) = 78498$.
>
> *Eccles: Definition 23.5.2*

^def-23-4

> [!theorem] Theorem §23.9: Prime Number Theorem
> The ratio of $\pi(n)$ to $n / \log_e n$ tends to $1$ as $n$ grows without bound: the sequence $n \mapsto \dfrac{\pi(n) \log_e n}{n} - 1$ is a null sequence ([[§8 Functions#^def-8-9|Def. §8.9]]).
>
> (Stated without proof.)
>
> *Eccles: Theorem 23.5.3*

^thm-23-9

> [!remark]- Remark: How Good Is the Estimate?
> | $n$ | $\pi(n)$ | $n / \log_e n$ | ratio |
> |---|---|---|---|
> | $10^3$ | $168$ | $144.8$ | $1.161$ |
> | $10^6$ | $78498$ | $72382.4$ | $1.084$ |
> | $10^9$ | $50847534$ | $48254942.4$ | $1.054$ |
> | $10^{12}$ | $37607912018$ | $36191206825.3$ | $1.039$ |
>
> Gauss conjectured the theorem in 1793 from tables of primes, and also the sharper estimate $\int_a^b dx / \log_e x$ for the number of primes between $a$ and $b$; it was proved in 1896 by Hadamard and de la Vallée-Poussin with complex analysis, far beyond this course. The logarithmic integral $\operatorname{li}(n) = \int_0^n dx / \log_e x$ is a better approximation still; Littlewood proved (1914) that $\operatorname{li}(n) - \pi(n)$ changes sign infinitely often, although it is positive for every $n$ ever computed — a pure existence result.

^rem-23-3
