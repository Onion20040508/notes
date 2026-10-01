---
type: section
subject: "[[Logic and Proofs]]"
chapter: 5
section: 19
eccles: "Ch. 19"
aliases: ["Eccles 19"]
tags: [logic-and-proofs, mat250]
---
← [[§18★ Linear Diophantine Equations]] · ↑ [[· 5 Modular Arithmetic]] · [[§20 Linear Congruences]] →

*Eccles, Chapter 19 and Problems V · MAT 200 lecture (syllabus week 11: congruence modulo m, modular arithmetic, the remainder map). No homework survives for this chapter.*

Even and odd is the classification of integers by their remainder on division by $2$; congruence modulo $m$ does the same for any modulus $m$. This section defines congruence through divisibility alone, shows that it behaves like equality under $+$, $-$ and $\times$ (*modular arithmetic*), checks that it agrees with "same remainder" via the remainder map, and finds that division needs care. Throughout, $m$ is a fixed positive integer.

## 19.1 Basic Definitions

> [!definition] Definition §19.1: Congruence Modulo $m$
> Two integers $a$ and $b$ are **congruent modulo $m$** when $a - b$ is divisible by $m$, i.e. there is an integer $q$ with $a - b = mq$. We write
>
> $$
> a \equiv b \pmod m ,
> $$
>
> and, when the **modulus** $m$ is clear, simply $a \equiv b$. For example $14 \equiv 2 \pmod 3$ since $14 - 2 = 3 \times 4$, and $14 \equiv -10 \pmod 3$ since $14 - (-10) = 3 \times 8$; but $14 \not\equiv 1 \pmod 3$, since $13$ is not a multiple of $3$.
>
> Note that $a \equiv 0 \pmod m$ says exactly that $m$ divides $a$. Any two integers are congruent modulo $1$, so the interesting moduli are $m > 1$.
>
> *Eccles: Definition 19.1.1*

^def-19-1

> [!remark]- Connections
> - The same definition in group theory: [[§6 Divisibility and Congruence#^def-6-3|493 Def. §6.3]].

The definition (and the notation $\equiv$) is due to Gauss, *Disquisitiones arithmeticae* (1801). It uses only divisibility, not the division theorem; the link with remainders comes in 19.2. Congruence shares the three basic properties of equality.

> [!theorem] Proposition §19.1: Reflexive, Symmetric and Transitive
> For all integers $a, b, c$:
> 1. *Reflexive:* $a \equiv a \pmod m$.
> 2. *Symmetric:* if $a \equiv b \pmod m$, then $b \equiv a \pmod m$.
> 3. *Transitive:* if $a \equiv b \pmod m$ and $b \equiv c \pmod m$, then $a \equiv c \pmod m$.
>
> *Eccles: Proposition 19.1.2*

^prop-19-1

> [!proof]+ Proof
> (1) $a - a = 0 = m \times 0$.
>
> (2) If $a - b = mq$ with $q \in \mathbb{Z}$, then $b - a = m \times (-q)$ and $-q \in \mathbb{Z}$.
>
> (3) If $a - b = mq_1$ and $b - c = mq_2$ with $q_1, q_2 \in \mathbb{Z}$, then $a - c = (a - b) + (b - c) = m(q_1 + q_2)$ with $q_1 + q_2 \in \mathbb{Z}$.

^pf-19-1

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]]

These properties are used without comment from now on. They say that congruence modulo $m$ is an *equivalence relation* ([[§22 Partitions and Equivalence Relations#^def-22-3|Def. §22.3]]), the theme of [[§22 Partitions and Equivalence Relations|§22]].

> [!remark]- Connections
> - [[§6 Divisibility and Congruence#^prop-6-2|493 Prop. §6.2]] (congruence modulo $n$ is an equivalence relation).

The real power of congruence is that it respects the operations of arithmetic.

> [!theorem] Proposition §19.2: Modular Arithmetic
> Suppose that $a_1 \equiv a_2 \pmod m$ and $b_1 \equiv b_2 \pmod m$. Then
> 1. $a_1 + b_1 \equiv a_2 + b_2 \pmod m$,
> 2. $a_1 - b_1 \equiv a_2 - b_2 \pmod m$,
> 3. $a_1 b_1 \equiv a_2 b_2 \pmod m$.
>
> *Eccles: Proposition 19.1.3 and Exercise 19.2*

^prop-19-2

> [!proof]+ Proof
> Write $a_1 - a_2 = mq_1$ and $b_1 - b_2 = mq_2$ with $q_1, q_2 \in \mathbb{Z}$.
>
> (1) $(a_1 + b_1) - (a_2 + b_2) = (a_1 - a_2) + (b_1 - b_2) = m(q_1 + q_2)$.
>
> (2) $(a_1 - b_1) - (a_2 - b_2) = (a_1 - a_2) - (b_1 - b_2) = m(q_1 - q_2)$.
>
> (3) Since $a_1 = a_2 + mq_1$ and $b_1 = b_2 + mq_2$,
>
> $$
> a_1 b_1 = (a_2 + mq_1)(b_2 + mq_2) = a_2 b_2 + m(a_2 q_2 + q_1 b_2 + m q_1 q_2),
> $$
>
> so $a_1 b_1 - a_2 b_2$ is $m$ times an integer.

^pf-19-2

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]]

> [!remark]- Connections
> - The same computation makes addition of residue classes well defined: [[§7 The Group ℤ∕nℤ#^prop-7-1|493 Prop. §7.1]].

So as far as $+$, $-$, $\times$ are concerned, congruent integers are interchangeable, and calculations become chains of congruences just as ordinary calculations are chains of equalities. Applying (3) repeatedly gives powers and polynomials.

> [!theorem] Corollary §19.3: Powers and Polynomials
> If $a \equiv b \pmod m$, then $a^n \equiv b^n \pmod m$ for every $n \in \mathbb{N}$. More generally, for integers $c_0, c_1, \ldots, c_k$,
>
> $$
> c_k a^k + \cdots + c_1 a + c_0 \equiv c_k b^k + \cdots + c_1 b + c_0 \pmod m .
> $$
>
> *Eccles: used in Examples 19.1.4*

^cor-19-3

> [!proof]+ Proof
> Induction on $n$. For $n = 0$, $a^0 = 1 \equiv 1 = b^0$ by reflexivity. If $a^n \equiv b^n$, then $a^{n+1} = a \cdot a^n \equiv b \cdot b^n = b^{n+1}$ by Proposition [[§19 Congruence of Integers#^prop-19-2|§19.2]](3). For the polynomial: $c_i a^i \equiv c_i b^i$ by §19.2(3) (with $c_i \equiv c_i$), and the $k + 1$ terms add up by §19.2(1) and induction on the number of terms.

^pf-19-3

*Uses:* [[§19 Congruence of Integers#^prop-19-1|§19.1]], [[§19 Congruence of Integers#^prop-19-2|§19.2]], [[§5 The Induction Principle#^thm-5-3|§5.3]] (induction from $n = 0$)

> [!example] Example §19.1: Chains of Congruences
> (a) Modulo $5$: $97 \equiv 2$ (as $95 = 5 \times 19$) and $144 \equiv 4$ (as $140 = 5 \times 28$), so
>
> $$
> 97^3 + 144^2 \equiv 2^3 + 4^2 = 8 + 16 \equiv 3 + 1 = 4 \pmod 5 .
> $$
>
> (b) For all $n \geq 1$, $\ 4^n + 5 \equiv 1^n + 2 = 3 \equiv 0 \pmod 3$, so $3$ divides $4^n + 5$ — a one-line replacement for the induction proof of Problems I, Q12 ([[§5 The Induction Principle#^ex-5-1|Example §5.1]](b)).
>
> (c) *Days of the week.* Counting days modulo $7$ is counting days of the week: two days fall on the same weekday exactly when their day numbers are congruent modulo $7$. 1 January 1998 was a Thursday. The day number of 6 September 1998 in that year is
>
> $$
> 31 \times 5 + 30 \times 2 + 28 \times 1 + 6 \equiv 3 \times 5 + 2 \times 2 + 0 \times 1 + 6 = 25 \equiv 4 \pmod 7 ,
> $$
>
> so it is the same weekday as day $4$, 4 January 1998: a Sunday.
>
> (d) *6 September 2045.* Between 1 January 1998 and 1 January 2045 lie $47$ years, $12$ of them leap years ($2000, 2004, \ldots, 2044$). Counting 1 January 1998 as day $1$, the day number of 6 September 2045 is $366 \times 12 + 365 \times 35 + 249$. Since $366 \equiv 2$, $365 \equiv 1$ and $249 \equiv 4 \pmod 7$, this is $\equiv 24 + 35 + 4 = 63 \equiv 0 \equiv 7 \pmod 7$: the same weekday as 7 January 1998, a Wednesday.
>
> *Eccles: Examples 19.1.4, Exercise 19.1*

^ex-19-1

## 19.2 The Remainder Map

The introduction described congruence as "same remainder on division by $m$". We now check that this agrees with Definition [[§19 Congruence of Integers#^def-19-1|§19.1]].

> [!definition] Definition §19.2: Remainders Modulo $m$
> The set
>
> $$
> R_m = \{0, 1, 2, \ldots, m - 1\} = \{ i \in \mathbb{Z} \mid 0 \leq i < m \}
> $$
>
> is the set of **(least non-negative) remainders modulo $m$**, or the set of **residues modulo $m$**.
>
> *Eccles: Definition 19.2.1*

^def-19-2

> [!theorem] Proposition §19.4: Each Integer Has a Unique Remainder
> Given an integer $a$, there is a unique $r \in R_m$ such that $a \equiv r \pmod m$.
>
> *Eccles: Proposition 19.2.2*

^prop-19-4

> [!proof]+ Proof
> For $r \in R_m$, $\ a \equiv r \pmod m$ means $a = mq + r$ for some $q \in \mathbb{Z}$. By the division theorem ([[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]) there are unique $q, r$ with $a = mq + r$ and $0 \leq r < m$; so such an $r$ exists, and it is unique (if $a = mq + r = mq' + r'$ with $r, r' \in R_m$, uniqueness in the division theorem gives $r = r'$).

^pf-19-4

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]], [[§19 Congruence of Integers#^def-19-2|Def. §19.2]], [[§15 The Division Theorem#^thm-15-1|§15.1]]

> [!definition] Definition §19.3: The Remainder Map
> The **remainder map** $r_m : \mathbb{Z} \to R_m$ is defined by
>
> $$
> r_m(a) = r \iff a \equiv r \pmod m \ \text{ and } \ r \in R_m .
> $$
>
> It is well defined by Proposition [[§19 Congruence of Integers#^prop-19-4|§19.4]].
>
> *Eccles: Definition 19.2.3*

^def-19-3

> [!remark] Remark: What "Well-Defined" Means
> Definition §19.3 does not give a formula for $r_m(a)$; it gives a *condition* that the value must satisfy. Such a conditional definition defines a function only if, for each $a$ in the domain, the condition picks out **exactly one** element of the codomain: at least one (existence) and at most one (uniqueness). That is what "$r_m$ is well defined" asserts, and it is precisely the content of Proposition §19.4. The same check, in a different guise, recurs whenever a function is defined on congruence classes ([[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-3|Proposition §21.3]]) or on equivalence classes ([[§22 Partitions and Equivalence Relations#^prop-22-5|Proposition §22.5]]).

^rem-19-1

> [!remark]- Connections
> - $r_m(a)$ is "$a \bmod n$" of [[§6 Divisibility and Congruence#^def-6-2|493 Def. §6.2]]; the general notion: [[§7 The Group ℤ∕nℤ#^def-7-2|493 Def. §7.2]] (well-defined).

> [!theorem] Proposition §19.5: Congruent Means Same Remainder
> Two integers $a$ and $b$ are congruent modulo $m$ if and only if $r_m(a) = r_m(b)$.
>
> *Eccles: Proposition 19.2.4*

^prop-19-5

> [!proof]+ Proof
> Let $r' = r_m(a)$ and $r'' = r_m(b)$; by definition $a \equiv r'$ and $b \equiv r'' \pmod m$.
>
> ($\Leftarrow$) If $r' = r''$, then $a \equiv r' = r'' \equiv b$, so $a \equiv b \pmod m$ by symmetry and transitivity.
>
> ($\Rightarrow$) If $a \equiv b$, then $r' \equiv a \equiv b \equiv r''$, so $b \equiv r' \pmod m$ with $r' \in R_m$. But also $b \equiv r'' \pmod m$ with $r'' \in R_m$, and by the uniqueness in Proposition [[§19 Congruence of Integers#^prop-19-4|§19.4]], $r' = r''$.

^pf-19-5

*Uses:* [[§19 Congruence of Integers#^prop-19-1|§19.1]], [[§19 Congruence of Integers#^prop-19-4|§19.4]], [[§19 Congruence of Integers#^def-19-3|Def. §19.3]]

The last step is the standard way uniqueness results are used: if only one object has a property and two objects are known to have it, they are equal.

> [!remark]- Connections
> - [[§6 Divisibility and Congruence#^prop-6-2|493 Prop. §6.2]](1) ($a \equiv b \pmod n$ iff $a \bmod n = b \bmod n$).

The language of congruence shortens earlier case-by-case arguments: an integer is congruent to exactly one element of $R_m$, so a statement about all integers splits into $m$ cases.

> [!example] Example §19.2: $a$ Is Even If and Only If $a^2$ Is Even
> *Claim.* For an integer $a$, $a$ is even if and only if $a^2$ is even.
>
> *Solution.* An integer $n$ is even iff $n \equiv 0 \pmod 2$, and since $R_2 = \{0, 1\}$, $n \equiv 0 \pmod 2$ iff $n \not\equiv 1 \pmod 2$. By modular arithmetic,
>
> $$
> a \equiv 0 \Rightarrow a^2 \equiv 0 \pmod 2, \qquad a \equiv 1 \Rightarrow a^2 \equiv 1 \pmod 2 .
> $$
>
> The contrapositive of the second is $a^2 \equiv 0 \Rightarrow a \equiv 0 \pmod 2$. Together, $a \equiv 0 \iff a^2 \equiv 0 \pmod 2$.
>
> *Eccles: Example 19.2.5 (Exercise 3.3, Problems I Q7)*

^ex-19-2

> [!example] Example §19.3: Sums of Two Squares
> (a) *There are no integers $a, b$ with $a^2 + b^2 = 1234567$.* Modulo $4$ there are four cases:
>
> | $a \bmod 4$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|
> | $a^2 \bmod 4$ | $0$ | $1$ | $4 \equiv 0$ | $9 \equiv 1$ |
>
> So every square is $\equiv 0$ or $1 \pmod 4$ (the congruence form of [[§15 The Division Theorem#^ex-15-7|Example §15.7]]), and $a^2 + b^2 \equiv 0, 1$ or $2 \pmod 4$, never $3$. Suppose for contradiction that $a^2 + b^2 = 1234567$. Since $1234567 = 4 \times 308641 + 3 \equiv 3 \pmod 4$, this gives $a^2 + b^2 \equiv 3 \pmod 4$, a contradiction.
>
> (b) *For all integers $a, b$: $a^2 + b^2 \equiv 0, 1, 2, 4$ or $5 \pmod 8$; hence $a^2 + b^2 = 12345790$ has no integer solutions.* The squares of $0, 1, \ldots, 7$ are $\equiv 0, 1, 4, 1, 0, 1, 4, 1 \pmod 8$, so every square is $\equiv 0, 1$ or $4$. The sums of two of these are $0, 1, 2, 4, 5, 8 \equiv 0$, i.e. $a^2 + b^2 \equiv 0, 1, 2, 4$ or $5$. But $12345790 = 8 \times 1543223 + 6 \equiv 6 \pmod 8$.
>
> *Eccles: Example 19.2.6 (Problems IV Q1), Problems V Q2*

^ex-19-3

> [!example] Example §19.4: Divisibility Tests
> Let $n = a_k a_{k-1} \ldots a_1 a_0$ in decimal notation, i.e. $n = \sum_{i=0}^k a_i 10^i$ with $0 \leq a_i \leq 9$.
>
> (a) *$3 \mid n$ iff $3$ divides the digit sum $a_k + \cdots + a_1 + a_0$.* Since $10 \equiv 1 \pmod 3$, Corollary [[§19 Congruence of Integers#^cor-19-3|§19.3]] gives $n = \sum a_i 10^i \equiv \sum a_i 1^i = \sum a_i \pmod 3$. So $n \equiv 0$ iff $\sum a_i \equiv 0 \pmod 3$.
>
> (b) *$9 \mid n$ iff $9$ divides the digit sum.* The same argument, since $10 \equiv 1 \pmod 9$.
>
> (c) *$11 \mid n$ iff $11$ divides the alternating sum $a_0 - a_1 + a_2 - \cdots + (-1)^k a_k$.* Now $10 \equiv -1 \pmod{11}$, so $n \equiv \sum a_i (-1)^i \pmod{11}$.
>
> (d) *$99 \mid n$ iff $99$ divides the sum of the two-digit blocks $\overline{a_1 a_0} + \overline{a_3 a_2} + \cdots$.* Grouping digits in pairs writes $n = \sum_j B_j 100^j$ with $0 \leq B_j \leq 99$, and $100 \equiv 1 \pmod{99}$.
>
> For instance $34567$ has digit sum $25 \not\equiv 0 \pmod 3$, so $3 \nmid 34567$; and $12468$, $48732$ have digit sums $21$, $24$, so both are multiples of $3$.
>
> *Eccles: Exercise 19.3, Problems V Q3–Q5*

^ex-19-4

> [!example] Example §19.5: Powers Modulo $m$
> (a) *For positive integers $n$, $7 \mid 6^n + 1$ iff $n$ is odd.* Since $6 \equiv -1 \pmod 7$, $\ 6^n + 1 \equiv (-1)^n + 1 \pmod 7$. If $n$ is odd this is $-1 + 1 = 0$; if $n$ is even it is $2 \not\equiv 0 \pmod 7$.
>
> (b) *The last digit of $2^{1000}$ is $6$.* The last digit of a positive integer is its remainder modulo $10$. Now $2^4 = 16 \equiv 6 \pmod{10}$ and $6 \times 6 = 36 \equiv 6$, so by induction $6^k \equiv 6 \pmod{10}$ for all $k \geq 1$. Hence $2^{1000} = (2^4)^{250} \equiv 6^{250} \equiv 6 \pmod{10}$.
>
> *Eccles: Problems V Q1, Q7*

^ex-19-5

## 19.3 Division in Congruences

Division needs care. $30 \equiv 2 \pmod 4$, but halving both sides gives $15 \not\equiv 1 \pmod 4$. The reason: $30 - 2 = 4 \times 7$, and halving gives $15 - 1 = 4 \times \tfrac72$ with $\tfrac72 \notin \mathbb{Z}$. Halving the modulus instead, $15 - 1 = \tfrac42 \times 7 = 2 \times 7$, gives a true congruence $15 \equiv 1 \pmod 2$. This is the first of two clean cases.

> [!theorem] Proposition §19.6: Dividing by a Divisor of the Modulus
> Let $a$ be a positive integer dividing $m$, so that $m/a$ is a positive integer. Then for all integers $b_1, b_2$,
>
> $$
> a b_1 \equiv a b_2 \pmod m \iff b_1 \equiv b_2 \pmod{m/a} .
> $$
>
> (Eccles allows any divisor $a$ of $m$. For $a < 0$ the number $m/a$ is negative and so not a modulus; apply the result to $-a$ instead, since $ab_1 \equiv ab_2 \iff (-a)b_1 \equiv (-a)b_2$.)
>
> *Eccles: Proposition 19.3.1*

^prop-19-6

> [!proof]+ Proof
> $$
> \begin{aligned}
> a b_1 \equiv a b_2 \pmod m &\iff a(b_1 - b_2) = mq \ \text{ for some } q \in \mathbb{Z} \\
> &\iff b_1 - b_2 = (m/a)\, q \ \text{ for some } q \in \mathbb{Z} \\
> &\iff b_1 \equiv b_2 \pmod{m/a} .
> \end{aligned}
> $$
>
> The middle step divides by $a \neq 0$ (and multiplies back by $a$ for $\Leftarrow$); the last step needs $m/a$ to be a positive integer to be a modulus.

^pf-19-6

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]]

At the other extreme, division by an integer coprime to the modulus is harmless.

> [!theorem] Proposition §19.7: Dividing by an Integer Coprime to the Modulus
> Let $a$ be an integer with $\gcd(a, m) = 1$. Then for all integers $b_1, b_2$,
>
> $$
> a b_1 \equiv a b_2 \pmod m \iff b_1 \equiv b_2 \pmod m .
> $$
>
> *Eccles: Proposition 19.3.2*

^prop-19-7

> [!proof]+ Proof
> ($\Rightarrow$) If $ab_1 \equiv ab_2 \pmod m$, then $m$ divides $a(b_1 - b_2)$. Since $a$ and $m$ are coprime, $m$ divides $b_1 - b_2$ (Theorem [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|§17.4]], Eccles 17.3.2). Directly, and for integers of any sign: by Bézout ([[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]) write $1 = ar + ms$ with $r, s \in \mathbb{Z}$; then
>
> $$
> b_1 - b_2 = r \cdot a(b_1 - b_2) + m \cdot s(b_1 - b_2)
> $$
>
> is a sum of two multiples of $m$. So $b_1 \equiv b_2 \pmod m$.
>
> ($\Leftarrow$) This is Proposition [[§19 Congruence of Integers#^prop-19-2|§19.2]](3) with $a \equiv a$.

^pf-19-7

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]], [[§19 Congruence of Integers#^prop-19-2|§19.2]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|§17.4]]

> [!remark]- Connections
> - The divisibility step is the general form of [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|493 Lemma §9.1]] (Euclid's lemma); cancellation by $a$ is invertibility of $[a]$, [[§8 Invertibility and Unit Groups#^prop-8-1|493 Prop. §8.1]].

Combining the two propositions gives the general cancellation law.

> [!theorem] Corollary §19.8: General Cancellation
> For all integers $a, b_1, b_2$,
>
> $$
> a b_1 \equiv a b_2 \pmod m \iff b_1 \equiv b_2 \pmod{m/\gcd(a, m)} .
> $$
>
> (Here $\gcd(a, m)$ divides $m$, so $m/\gcd(a,m)$ is a positive integer.)
>
> *Eccles: Exercise 19.5*

^cor-19-8

> [!proof]+ Proof
> Put $d = \gcd(a, m) \geq 1$, $a = d a'$, $m = d m'$. First, $a'$ and $m'$ are coprime (cf. [[§11 Properties of Finite Sets#^prop-11-10|Proposition §11.10]]): by Bézout $d = ar + ms$ ([[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]), and dividing by $d$ gives $1 = a' r + m' s$, so every common divisor of $a'$ and $m'$ divides $1$. Now
>
> $$
> d a' b_1 \equiv d a' b_2 \pmod m \iff a' b_1 \equiv a' b_2 \pmod{m'} \iff b_1 \equiv b_2 \pmod{m'}
> $$
>
> by Proposition [[§19 Congruence of Integers#^prop-19-6|§19.6]] (with the divisor $d$ of $m$) and then Proposition [[§19 Congruence of Integers#^prop-19-7|§19.7]] (with modulus $m'$, coprime to $a'$).

^pf-19-8

*Uses:* [[§19 Congruence of Integers#^prop-19-6|§19.6]], [[§19 Congruence of Integers#^prop-19-7|§19.7]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]]

Division first arises in solving $ax = b$; in modular arithmetic it arises in solving the **linear congruence** $ax \equiv b \pmod m$, i.e. finding *all* integers $x$ satisfying it. For small numbers, Propositions §19.6 and §19.7 used in turn already do this: divide by common factors of $a$, $b$ and $m$ until none remain, then cancel factors coprime to the modulus.

> [!example] Example §19.6: Solving Linear Congruences by Division
> (a) *Solve $4x \equiv 12 \pmod{14}$.*
>
> $$
> \begin{aligned}
> 4x \equiv 12 \pmod{14} &\iff 2x \equiv 6 \pmod 7 && \text{(§19.6, dividing by } 2 \mid 14) \\
> &\iff x \equiv 3 \pmod 7 && \text{(§19.7, since } \gcd(2,7) = 1).
> \end{aligned}
> $$
>
> The "$\iff$" matters: $x \equiv 3 \pmod 7$ is necessary *and* sufficient, so the solution set is exactly $S = \{x \in \mathbb{Z} \mid x \equiv 3 \pmod 7\} = \{3 + 7q \mid q \in \mathbb{Z}\}$. In terms of the original modulus: the $r \in R_{14}$ with $r \equiv 3 \pmod 7$ are $3$ and $10$, so $4x \equiv 12 \pmod{14} \iff x \equiv 3$ or $10 \pmod{14}$.
>
> (b) *Solve $6x \equiv 15 \pmod{21}$.*
>
> $$
> \begin{aligned}
> 6x \equiv 15 \pmod{21} &\iff 2x \equiv 5 \pmod 7 && \text{(§19.6, dividing by } 3 \mid 21) \\
> &\iff 2x \equiv 12 \pmod 7 && (5 \equiv 12, \text{ to make the right side even}) \\
> &\iff x \equiv 6 \pmod 7 && \text{(§19.7)}.
> \end{aligned}
> $$
>
> The $r \in R_{21}$ with $r \equiv 6 \pmod 7$ are $6, 13, 20$, so $6x \equiv 15 \pmod{21} \iff x \equiv 6, 13$ or $20 \pmod{21}$.
>
> *Eccles: Examples 19.3.3, 19.3.4*

^ex-19-6

These ad hoc methods suit small numbers; [[§20 Linear Congruences|§20]] gives the general criterion and a systematic method via the Euclidean algorithm.
