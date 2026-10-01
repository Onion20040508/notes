---
type: section
subject: "[[Logic and Proofs]]"
chapter: 6
section: 24
eccles: "Ch. 24"
aliases: ["Eccles 24"]
tags: [logic-and-proofs, mat250, extension]
---
← [[§23 The Sequence of Prime Numbers]] · ↑ [[· 6 Prime Numbers]] · [[§25 Surfaces and the Euler Characteristic]] →

*Eccles, Chapter 24 (with Problems VI Q14, Q17, Q18).*
★ *Not in the MAT 250 course record (no homework or syllabus entry for this chapter); included from Eccles to complete the arithmetic of primes, and because it is where group theory begins.*

Modulo a prime $p$, every nonzero congruence class is invertible ([[§21 Congruence Classes and the Arithmetic of Remainders#^cor-21-9|Corollary §21.9]]), and this makes arithmetic modulo $p$ unusually rigid. This section proves the two classical consequences, Fermat's little theorem $a^{p-1} \equiv 1$ and Wilson's theorem $(p-1)! \equiv -1 \pmod p$, both by counting arguments in $\mathbb{Z}_p$, and then asks how far Fermat's theorem can be turned into a test for primality. Ivory's proof of Fermat's theorem below is the special case of Lagrange's theorem that group theory later makes general.

## 24.1 Fermat's Little Theorem

Recall from [[§21 Congruence Classes and the Arithmetic of Remainders#^cor-21-9|Corollary §21.9]] that $[a]_m \in \mathbb{Z}_m$ has a multiplicative inverse if and only if $\gcd(a, m) = 1$. When $m = p$ is prime, every $a$ with $0 < a < p$ is coprime to $p$, so every nonzero class in $\mathbb{Z}_p$ is invertible.

> [!theorem] Theorem §24.1: Fermat's Little Theorem
> Let $p$ be a prime and $a$ an integer that is not a multiple of $p$. Then
>
> $$
> a^{p-1} \equiv 1 \pmod p ,
> $$
>
> i.e. $p$ divides $a^{p-1} - 1$.
>
> *Eccles: Theorem 24.1.1 (stated there for positive $a$; the proof uses only $p \nmid a$)*

^thm-24-1

> [!proof]+ Proof
> (James Ivory, 1806.) Since $p$ is prime and $p \nmid a$, $\gcd(a, p) = 1$. Define $f : \mathbb{Z}_p \to \mathbb{Z}_p$ by $f([x]_p) = [a]_p \times [x]_p = [ax]_p$, the function from the proof of Eccles's Theorem 21.4.1 ([[§21 Congruence Classes and the Arithmetic of Remainders#^thm-21-6|Theorem §21.6]]).
>
> *$f$ is a bijection.* If $[ax]_p = [ay]_p$, then $ax \equiv ay \pmod p$, and since $\gcd(a, p) = 1$ we may cancel $a$ (Eccles Proposition 19.3.2, [[§19 Congruence of Integers#^prop-19-7|§19.7]]), so $x \equiv y$. Thus $f$ is an injection from a finite set to itself, hence a bijection (Eccles Theorem 11.1.7, [[§11 Properties of Finite Sets#^thm-11-7|§11.7]], from the pigeonhole principle).
>
> *$f$ permutes the nonzero classes.* $f([0]_p) = [0]_p$, so by injectivity no nonzero class is sent to $[0]_p$; thus $f$ maps the $p - 1$ nonzero classes injectively, hence bijectively, onto themselves. In other words $[a]_p, [2a]_p, \ldots, [(p-1)a]_p$ are $[1]_p, [2]_p, \ldots, [p-1]_p$ in some order, and multiplying out (multiplication of classes is commutative),
>
> $$
> [a]_p \times [2a]_p \times \cdots \times [(p-1)a]_p = [1]_p \times [2]_p \times \cdots \times [p-1]_p ,
> $$
>
> that is, $a \cdot 2a \cdots (p-1)a \equiv 1 \cdot 2 \cdots (p-1) \pmod p$, or
>
> $$
> a^{p-1} (p-1)! \equiv (p-1)! \pmod p .
> $$
>
> *Cancel $(p-1)!$.* If $p \mid (p-1)! = 1 \cdot 2 \cdots (p-1)$, then $p \mid j$ for some $1 \le j \le p - 1$ ([[§23 The Sequence of Prime Numbers#^prop-23-4|§23.4]]), impossible since $0 < j < p$. So $p \nmid (p-1)!$, hence $\gcd((p-1)!, p) = 1$, and cancelling (Proposition 19.3.2 again) gives $a^{p-1} \equiv 1 \pmod p$.

^pf-24-1

*Uses:* [[§21 Congruence Classes and the Arithmetic of Remainders#^thm-21-6|§21.6]], [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-3|Def. §21.3]], [[§21 Congruence Classes and the Arithmetic of Remainders#^prop-21-4|§21.4]], [[§19 Congruence of Integers#^prop-19-7|§19.7]], [[§11 Properties of Finite Sets#^thm-11-7|§11.7]], [[§23 The Sequence of Prime Numbers#^prop-23-4|§23.4]]

> [!remark]- Connections
> - Developed further in: [[§27 The Index and Lagrange's Theorem#^cor-27-4|493 Cor. §27.4]] (Fermat's little theorem as $g^{\abs{G}} = e$ in the group $U_p$ of order $p - 1$, via Lagrange's theorem).
> - The bijection $[x] \mapsto [a][x]$ of the nonzero classes is [[§8 Invertibility and Unit Groups#^prop-8-2|493 Prop. §8.2]].

> [!theorem] Corollary §24.2: $a^p \equiv a$ for Every Integer
> If $p$ is prime, then $a^p \equiv a \pmod p$ for all integers $a$.
>
> *Eccles: Corollary 24.1.2*

^cor-24-2

> [!proof]+ Proof
> If $p \mid a$, then $p \mid a^p$, so $a^p \equiv 0 \equiv a \pmod p$. If $p \nmid a$, multiply $a^{p-1} \equiv 1$ ([[§24★ Congruence Modulo a Prime#^thm-24-1|Theorem §24.1]]) by $a$.

^pf-24-2

*Uses:* [[§24★ Congruence Modulo a Prime#^thm-24-1|§24.1]]

> [!example] Example §24.1: High Powers Modulo a Prime
> 1. $3^{203} \bmod 11$. By Fermat, $3^{10} \equiv 1 \pmod{11}$, and $203 = 20 \times 10 + 3$, so $3^{203} = (3^{10})^{20} \times 3^3 \equiv 1 \times 27 \equiv 5 \pmod{11}$.
> 2. $2^{1000000} \bmod 17$. By Fermat, $2^{16} \equiv 1 \pmod{17}$, and $16 \mid 10^6 = 2^6 5^6$, so $2^{1000000} = (2^{16})^{62500} \equiv 1$: the remainder is $1$.
> 3. *Inverses from Fermat.* Since $7 \cdot 7^{15} = 7^{16} \equiv 1 \pmod{17}$, the inverse of $7$ modulo $17$ is $7^{15}$ reduced: $7^2 = 49 \equiv -2$, $7^4 \equiv 4$, $7^8 \equiv 16 \equiv -1$, so $7^{15} = 7^8 \cdot 7^4 \cdot 7^2 \cdot 7 \equiv (-1)(4)(-2)(7) = 56 \equiv 5$. Check: $7 \times 5 = 35 = 2 \times 17 + 1$.
>
> *Eccles: Example 24.1.3; Exercises 24.1, 24.3*

^ex-24-1

Fermat's theorem need not give the *smallest* power of $a$ that is $\equiv 1$: trivially for $a = 1$, and for instance $2^3 = 8 \equiv 1 \pmod 7$, while $p - 1 = 6$.

> [!definition] Definition §24.1: Order Modulo $p$; Primitive Root
> Let $p$ be prime and $a \not\equiv 0 \pmod p$. The **order of $a$ modulo $p$** is the least positive integer $n$ with $a^n \equiv 1 \pmod p$; it exists because the set of such $n$ contains $p - 1$ ([[§24★ Congruence Modulo a Prime#^thm-24-1|Theorem §24.1]]) and so has a least element (well-ordering, [[§5 The Induction Principle#^cor-5-7|Corollary §5.7]]). An $a$ of order $p - 1$ is a **primitive root** modulo $p$.
>
> For example, modulo $7$ the powers of $2$ are $2, 4, 1, \ldots$, so $2$ has order $3$; the powers of $3$ are $3, 2, 6, 4, 5, 1$, so $3$ has order $6$ and is a primitive root. Every prime has a primitive root (Eccles quotes this; it is not proved here).
>
> *Eccles: §24.1 (text); Problems VI Q13 (order computations)*

^def-24-1

> [!theorem] Proposition §24.3: The Order Divides $p - 1$
> Let $p$ be prime, $a \not\equiv 0 \pmod p$, and $n$ the order of $a$ modulo $p$. Then for every $m \in \mathbb{N}$, $a^m \equiv 1 \pmod p$ if and only if $n \mid m$. In particular $n \mid p - 1$.
>
> *Eccles: Problems VI Q14 (which asks only for $n \mid p - 1$; the "if and only if" is added here)*

^prop-24-3

> [!proof]+ Proof
> If $m = qn$, then $a^m = (a^n)^q \equiv 1^q = 1$. Conversely, suppose $a^m \equiv 1$ and divide: $m = qn + r$ with $0 \le r < n$ ([[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]). Then $1 \equiv a^m = (a^n)^q a^r \equiv a^r$. If $r > 0$, this contradicts the minimality of $n$; so $r = 0$ and $n \mid m$. Taking $m = p - 1$ and using [[§24★ Congruence Modulo a Prime#^thm-24-1|Theorem §24.1]] gives $n \mid p - 1$.

^pf-24-3

*Uses:* [[§24★ Congruence Modulo a Prime#^def-24-1|Def. §24.1]], [[§24★ Congruence Modulo a Prime#^thm-24-1|§24.1]], [[§15 The Division Theorem#^thm-15-1|§15.1]]

> [!remark]- Connections
> - The group version: the order of an element divides $\abs{G}$, [[§27 The Index and Lagrange's Theorem#^cor-27-3|493 Cor. §27.3]]; for $G = U_p$, $\abs{G} = p - 1$.

## 24.2 Wilson's Theorem

> [!example] Example §24.2: Wilson's Theorem for $p = 11$
> Modulo $11$: $10 \equiv -1$, and the numbers $2, \ldots, 9$ pair off with their inverses,
>
> $$
> 9 \times 5 = 45 \equiv 1, \quad 8 \times 7 = 56 \equiv 1, \quad 6 \times 2 = 12 \equiv 1, \quad 4 \times 3 = 12 \equiv 1 .
> $$
>
> Hence $10! = 10 \times (9 \times 5) \times (8 \times 7) \times (6 \times 2) \times (4 \times 3) \equiv (-1) \times 1 \times 1 \times 1 \times 1 = -1 \pmod{11}$. The general proof pairs off in the same way.
>
> *Eccles: Example 24.2.2*

^ex-24-2

> [!theorem] Lemma §24.4: Square Roots of 1 Modulo a Prime
> Let $p$ be prime. For an integer $x$, $x^2 \equiv 1 \pmod p$ if and only if $x \equiv 1$ or $x \equiv -1 \pmod p$.
>
> *Eccles: proof of Theorem 24.2.1*

^lem-24-4

> [!proof]+ Proof
> $$
> \begin{aligned}
> x^2 \equiv 1 \!\!\pmod p
> &\iff p \mid x^2 - 1 = (x - 1)(x + 1) \\
> &\iff p \mid x - 1 \ \text{ or } \ p \mid x + 1 && \text{(Theorem §23.2, for arbitrary integers)} \\
> &\iff x \equiv 1 \ \text{ or } \ x \equiv -1 \!\!\pmod p .
> \end{aligned}
> $$
>
> (The backward direction of the middle step holds because $p$ dividing a factor divides the product.)

^pf-24-4

*Uses:* [[§23 The Sequence of Prime Numbers#^thm-23-2|§23.2]], [[§19 Congruence of Integers#^def-19-1|Def. §19.1]]

> [!theorem] Theorem §24.5: Wilson's Theorem
> If $p$ is prime, then $(p - 1)! \equiv -1 \pmod p$; equivalently, $p \mid (p-1)! + 1$.
>
> *Eccles: Theorem 24.2.1*

^thm-24-5

> [!proof]+ Proof
> For $p = 2$: $1! = 1 \equiv -1 \pmod 2$. Let $p \ge 3$.
>
> *Inverses.* Each $a$ with $1 \le a \le p - 1$ is coprime to $p$, so by Eccles's Theorem 20.1.5 ([[§20 Linear Congruences#^thm-20-3|Theorem §20.3]]) there is a unique $a' \in R_p = \{0, 1, \ldots, p - 1\}$ with $aa' \equiv 1 \pmod p$ — the inverse of $a$ modulo $p$. Clearly $a' \ne 0$, and $(a')' = a$, since $a$ satisfies $a' a \equiv 1$ and the inverse of $a'$ is unique.
>
> *Which $a$ are their own inverse.* $a' = a$ means $a^2 \equiv 1$, which by [[§24★ Congruence Modulo a Prime#^lem-24-4|Lemma §24.4]] happens exactly for $a \equiv \pm 1$, i.e. $a \in \{1, p - 1\}$.
>
> *Pairing.* Let $S = \{2, 3, \ldots, p - 2\}$ (empty when $p = 3$). For $a \in S$: $a' \ne 1$ (else $a \equiv 1$) and $a' \ne p - 1$ (else $-a \equiv 1$, i.e. $a \equiv -1$), so $a' \in S$, and $a' \ne a$. Since $(a')' = a$, the sets $\{a, a'\}$ for $a \in S$ are $2$-element subsets of $S$, and two of them that meet are equal (if $c \in \{a, a'\} \cap \{b, b'\}$ then both sets equal $\{c, c'\}$). So they partition $S$ into pairs whose product is $\equiv 1$, and
>
> $$
> 2 \times 3 \times \cdots \times (p - 2) \equiv 1 \pmod p .
> $$
>
> Therefore $(p - 1)! = 1 \times \bigl(2 \times \cdots \times (p-2)\bigr) \times (p - 1) \equiv p - 1 \equiv -1 \pmod p$.

^pf-24-5

*Uses:* [[§20 Linear Congruences#^thm-20-3|§20.3]], [[§24★ Congruence Modulo a Prime#^lem-24-4|§24.4]], [[§22 Partitions and Equivalence Relations#^def-22-1|Def. §22.1]]

> [!example] Example §24.3: Wilson's Theorem Characterizes Primes
> For an integer $n > 1$: $n$ is prime $\iff (n - 1)! \equiv -1 \pmod n$.
>
> *Solution.* ($\Rightarrow$) is [[§24★ Congruence Modulo a Prime#^thm-24-5|Wilson's theorem]]. ($\Leftarrow$) by contradiction: suppose $(n-1)! \equiv -1 \pmod n$ but $n$ is composite, with a divisor $a$, $1 < a < n$. Then $a \le n - 1$ is one of the factors of $(n-1)!$, so $(n-1)! \equiv 0 \pmod a$. But $a \mid n$ and $n \mid (n-1)! + 1$ give $(n-1)! \equiv -1 \pmod a$, so $a \mid 1$, contradicting $a > 1$. (For example $3! = 6 \equiv 2 \pmod 4$.)
>
> As a primality test this is useless in practice: computing $(n-1)!$ takes far longer than trial division.
>
> *Eccles: Exercise 24.4*

^ex-24-3

## 24.3 Looking for Primes

Fermat's theorem gives a way to prove that a number is composite *without finding a factor*.

> [!theorem] Corollary §24.6: A Compositeness Test
> Let $n$ be a positive integer. If $a^n \not\equiv a \pmod n$ for some integer $a$, then $n$ is not prime.
>
> *Eccles: Corollary 24.3.1*

^cor-24-6

> [!proof]+ Proof
> This is the contrapositive of [[§24★ Congruence Modulo a Prime#^cor-24-2|Corollary §24.2]].

^pf-24-6

*Uses:* [[§24★ Congruence Modulo a Prime#^cor-24-2|§24.2]], [[§2 Implications#^prop-2-2|§2.2]] (contrapositive)

> [!example] Example §24.4: 63 Is Not Prime
> $2^6 = 64 \equiv 1 \pmod{63}$, so $2^{63} = (2^6)^{10} \times 2^3 \equiv 8 \pmod{63}$. Since $8 \not\equiv 2$, [[§24★ Congruence Modulo a Prime#^cor-24-6|Corollary §24.6]] shows $63$ is composite — although $63 = 7 \times 9$ shows it faster. The point is that for large $n$, powers modulo $n$ are cheap to compute while factors are hard to find.
>
> *Eccles: Example 24.3.2*

^ex-24-4

The converse of [[§24★ Congruence Modulo a Prime#^cor-24-6|Corollary §24.6]] fails, even in its strongest form.

> [!example] Example §24.5: Pseudoprimes — 341 and 561
> *A lemma used twice.* If distinct primes $q_1, \ldots, q_k$ all divide $N$, then $q_1 \cdots q_k \mid N$. (Induction on $k$: if $q_1 \cdots q_{k-1} \mid N$, write $N = q_1 \cdots q_{k-1}\, c$; then $q_k \mid N$ and $q_k$ divides no $q_i$ with $i < k$, so $q_k \mid c$ by [[§23 The Sequence of Prime Numbers#^prop-23-4|Proposition §23.4]].)
>
> 1. **$2^{341} \equiv 2 \pmod{341}$, but $341 = 11 \times 31$.** By Fermat, $2^{10} \equiv 1 \pmod{11}$; and $2^5 = 32 \equiv 1 \pmod{31}$, so $2^{10} \equiv 1 \pmod{31}$. By the lemma $341 \mid 2^{10} - 1$, so $2^{340} = (2^{10})^{34} \equiv 1$ and $2^{341} \equiv 2 \pmod{341}$. So "$2^n \equiv 2 \pmod n \Rightarrow n$ prime" is false.
> 2. **$a^{560} \equiv 1 \pmod{561}$ for every $a$ coprime to $561$, but $561 = 3 \times 11 \times 17$.** If $\gcd(a, 561) = 1$, then $a$ is coprime to $3$, $11$ and $17$ (a common factor would divide $561$). By Fermat, $a^2 \equiv 1 \pmod 3$, $a^{10} \equiv 1 \pmod{11}$, $a^{16} \equiv 1 \pmod{17}$, and $2$, $10$, $16$ all divide $560$, so $a^{560} \equiv 1$ modulo each of $3, 11, 17$. By the lemma, $561 \mid a^{560} - 1$.
>
> So not even "$a^{n-1} \equiv 1 \pmod n$ for all $a$ coprime to $n$" forces $n$ to be prime. (Composite $n$ passing the test of Corollary §24.6 for a given $a$ are called *pseudoprimes to base $a$*; $561$, which passes for every coprime $a$, is the smallest *Carmichael number*.) Refinements of these ideas do give practical primality tests, an active research area.
>
> *Eccles: Examples 24.3.3, 24.3.4*

^ex-24-5

> [!remark] Remark: Three Proofs of Fermat's Theorem
> Problems VI gives two more proofs of [[§24★ Congruence Modulo a Prime#^thm-24-1|Theorem §24.1]].
> - *Euler's (Q17).* For $0 < i < p$ the binomial coefficient $\binom{p}{i} = \frac{p!}{i!\,(p-i)!}$ is a multiple of $p$: $p$ divides the numerator $p!$ but, by [[§23 The Sequence of Prime Numbers#^prop-23-4|§23.4]], not $i!\,(p-i)!$, whose factors are all $< p$. Hence $(a + b)^p \equiv a^p + b^p \pmod p$ (binomial theorem, [[§12★ Counting Functions and Subsets#^thm-12-10|Theorem §12.10]]), and induction on $a \geq 0$ gives $a^p = ((a - 1) + 1)^p \equiv (a-1)^p + 1 \equiv a$; this extends to all $a$ since $a^p \bmod p$ depends only on $a \bmod p$, and cancelling $a$ when $p \nmid a$ ([[§19 Congruence of Integers#^prop-19-7|§19.7]]) gives $a^{p-1} \equiv 1$.
> - *Gauss's (Q18).* On the nonzero residues define $x_1 \sim x_2 \iff x_1 \equiv x_2 a^k$ for some $k \in \mathbb{Z}^+$. This is an equivalence relation ([[§22 Partitions and Equivalence Relations#^def-22-3|Def. §22.3]]) whose classes $\{x, xa, \ldots, xa^{n-1}\}$ all have $n$ elements, $n$ the order of $a$. The classes partition the $p - 1$ nonzero residues, so $n \mid p - 1$ — Proposition §24.3 without using Fermat — and then $a^{p-1} = (a^n)^{(p-1)/n} \equiv 1$.
>
> Gauss's argument is exactly the proof of Lagrange's theorem: the classes are the cosets of the subgroup $\{1, a, \ldots, a^{n-1}\}$ of the nonzero residues.

^rem-24-1

> [!remark]- Connections
> - Developed further in: [[§27 The Index and Lagrange's Theorem#^thm-27-2|493 Thm. §27.2]] (Lagrange's theorem: cosets partition a group into sets of equal size) and [[§27 The Index and Lagrange's Theorem#^cor-27-4|493 Cor. §27.4]] (Fermat as its corollary).
