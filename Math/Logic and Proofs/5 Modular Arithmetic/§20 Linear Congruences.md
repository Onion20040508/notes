---
type: section
subject: "[[Logic and Proofs]]"
chapter: 5
section: 20
eccles: "Ch. 20"
aliases: ["Eccles 20"]
tags: [logic-and-proofs, mat250]
---
← [[§19 Congruence of Integers]] · ↑ [[· 5 Modular Arithmetic]] · [[§21 Congruence Classes and the Arithmetic of Remainders]] →

*Eccles, Chapter 20 · MAT 200 lecture (syllabus week 11: linear congruences). No homework survives for this chapter.*

This section solves the linear congruence $ax \equiv b \pmod m$ completely: it has a solution exactly when $\gcd(a, m)$ divides $b$, and then it has $\gcd(a, m)$ solutions modulo $m$. The key is that a linear congruence is a linear diophantine equation in disguise ([[§18★ Linear Diophantine Equations|§18★]]), so the Euclidean algorithm ([[§16 The Euclidean Algorithm#^thm-16-3|Theorem §16.3]]) finds the solutions. Throughout, $m$ is a fixed positive integer.

## 20.1 A Criterion for the Existence of Solutions

> [!definition] Definition §20.1: Linear Congruence
> Given integers $a$ and $b$, the **linear congruence**
>
> $$
> ax \equiv b \pmod m
> $$
>
> is the problem of finding all integers $x$ that satisfy it; its **solution set** is $\{x \in \mathbb{Z} \mid ax \equiv b \pmod m\}$. If $x_0$ is a solution, so is every $x \equiv x_0 \pmod m$ (by modular arithmetic, $ax \equiv a x_0 \equiv b$). The solution is **unique modulo $m$** if the solutions are exactly the integers congruent to one of them; more generally, the **number of solutions modulo $m$** is the number of $r \in R_m$ that are solutions.
>
> *Eccles: Problem 20.0.1; text after Theorem 20.1.5*

^def-20-1

Propositions [[§19 Congruence of Integers#^prop-19-6|§19.6]] and [[§19 Congruence of Integers#^prop-19-7|§19.7]] let us divide $ax \equiv b \pmod m$ by common factors of $a$ and $b$, and also of $m$ when the factor divides $m$. What if $a$ and $m$ have a common factor that does *not* divide $b$?

> [!example] Example §20.1: A Congruence With No Solutions
> *Claim.* The linear congruence $6x \equiv 14 \pmod{21}$ has no solutions.
>
> The goal "$6x \not\equiv 14 \pmod{21}$ for every $x \in \mathbb{Z}$" is negative, which suggests a proof by contradiction ([[§4 Proof by Contradiction#^thm-4-2|Theorem §4.2]]).
>
> *Proof.* Suppose, for contradiction, that $x \in \mathbb{Z}$ satisfies $6x \equiv 14 \pmod{21}$. Then $6x - 14 = 21q$ for some $q \in \mathbb{Z}$, so
>
> $$
> 14 = 6x - 21q = 3(2x - 7q),
> $$
>
> and $3$ divides $14$. This is false, so the assumption was false: there is no solution.
>
> *Eccles: Example 20.1.1*

^ex-20-1

> [!theorem] Proposition §20.1: A Common Divisor Obstruction
> Let $a$ and $b$ be integers. If some common divisor of $a$ and $m$ does not divide $b$, then the linear congruence $ax \equiv b \pmod m$ has no solutions.
>
> *Eccles: Proposition 20.1.2*

^prop-20-1

> [!proof]+ Proof
> Let $c$ be a common divisor of $a$ and $m$ with $c \nmid b$, and suppose for contradiction that $a x_0 \equiv b \pmod m$ for some integer $x_0$. Then $a x_0 - b = mq$ for some $q \in \mathbb{Z}$. Write $a = c a_1$ and $m = c m_1$ with $a_1, m_1 \in \mathbb{Z}$. Then
>
> $$
> b = a x_0 - mq = c a_1 x_0 - c m_1 q = c(a_1 x_0 - m_1 q),
> $$
>
> so $c$ divides $b$, contradicting the hypothesis. Hence there is no solution.

^pf-20-1

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]]

> [!example] Example §20.2: Spotting the Obstruction
> The congruence $12468x \equiv 34567 \pmod{48732}$ has no solutions: $3$ divides $12468$ and $48732$ (digit sums $21$ and $24$) but not $34567$ (digit sum $25$), by the digit-sum test of [[§19 Congruence of Integers#^ex-19-4|Example §19.4]].
>
> *Eccles: Example 20.1.3*

^ex-20-2

[[§20 Linear Congruences#^prop-20-1|Proposition §20.1]] gives a necessary condition: if there is a solution, every common divisor of $a$ and $m$ divides $b$. "Every common divisor" sounds like a lot to check, but all common divisors divide $\gcd(a, m)$ ([[§17 Consequences of the Euclidean Algorithm#^cor-17-2|Corollary §17.2]]), so one divisibility captures it.

> [!theorem] Corollary §20.2: The gcd Condition Is Necessary
> If the linear congruence $ax \equiv b \pmod m$ has a solution, then $\gcd(a, m)$ divides $b$.
>
> *Eccles: Corollary 20.1.4*

^cor-20-2

> [!proof]+ Proof
> $\gcd(a, m)$ is a common divisor of $a$ and $m$; if it did not divide $b$, Proposition [[§20 Linear Congruences#^prop-20-1|§20.1]] would give no solutions.

^pf-20-2

*Uses:* [[§20 Linear Congruences#^prop-20-1|§20.1]]

The condition is also sufficient. The key case is $a$ coprime to $m$, where it holds automatically.

> [!theorem] Theorem §20.3: Coprime Coefficient
> Suppose that $a$ and $b$ are integers with $a$ and $m$ coprime. Then the linear congruence $ax \equiv b \pmod m$ has a solution, and the solution is unique modulo $m$: if $x_0$ is one solution, an integer $x$ is a solution if and only if $x \equiv x_0 \pmod m$.
>
> *Eccles: Theorem 20.1.5*

^thm-20-3

The proof is given in 20.2 below, after the link with diophantine equations. ([[§21 Congruence Classes and the Arithmetic of Remainders#^thm-21-6|Theorem §21.6]] gives a second, non-constructive proof by counting.)

> [!example] Example §20.3: Unique and Non-Unique Solutions
> (a) In Example [[§19 Congruence of Integers#^ex-19-6|§19.6]](b), $2x \equiv 5 \pmod 7 \iff x \equiv 6 \pmod 7$: one solution modulo $7$, as [[§20 Linear Congruences#^thm-20-3|Theorem §20.3]] predicts since $\gcd(2, 7) = 1$.
>
> (b) *Solve $3x \equiv 8 \pmod{11}$.* Since $\gcd(3, 11) = 1$ there is exactly one solution modulo $11$, and we may find it by trying each $x \in R_{11}$:
>
> | $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $r_{11}(3x)$ | $0$ | $3$ | $6$ | $9$ | $1$ | $4$ | $7$ | $10$ | $2$ | $5$ | $8$ |
>
> So $3x \equiv 8 \pmod{11} \iff x \equiv 10 \pmod{11}$. Quicker: $8 \equiv -3$, so $3x \equiv -3 \iff x \equiv -1 \equiv 10 \pmod{11}$ by Proposition [[§19 Congruence of Integers#^prop-19-7|§19.7]].
>
> (c) In Example §19.6(a), $4x \equiv 12 \pmod{14} \iff x \equiv 3$ or $10 \pmod{14}$. Here $\gcd(4, 14) = 2$: the coefficient is not coprime to the modulus, and there are *two* solutions modulo $14$.
>
> *Eccles: Examples 20.1.6*

^ex-20-3

Putting together [[§20 Linear Congruences#^thm-20-3|Theorem §20.3]], Proposition [[§19 Congruence of Integers#^prop-19-6|§19.6]] and [[§20 Linear Congruences#^cor-20-2|Corollary §20.2]] gives the complete answer. To see where the count comes from, look again at $6x \equiv 15 \pmod{21}$: it reduced to the unique solution $x \equiv 6 \pmod 7$, and the remainders modulo $21$ congruent to $6$ modulo $7$ are $6 + 7q$ for $q = 0, 1, 2$, three of them, and $3 = \gcd(6, 21)$.

> [!theorem] Theorem §20.4: Solvability and Number of Solutions
> The linear congruence $ax \equiv b \pmod m$ has a solution if and only if $\gcd(a, m)$ divides $b$. In this case the number of solutions modulo $m$ is $\gcd(a, m)$.
>
> *Eccles: Theorem 20.1.7*

^thm-20-4

> [!proof]+ Proof
> Write $d = \gcd(a, m)$ and $m_1 = m/d$, a positive integer.
>
> *Necessity* is Corollary [[§20 Linear Congruences#^cor-20-2|§20.2]].
>
> *Sufficiency.* Suppose $d \mid b$. Since $d$ divides $a$, $b$ and $m$, Proposition [[§19 Congruence of Integers#^prop-19-6|§19.6]] gives
>
> $$
> ax \equiv b \pmod m \iff \frac{a}{d}\, x \equiv \frac{b}{d} \pmod{m_1} .
> $$
>
> The integers $a/d$ and $m_1$ are coprime (by Bézout, [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]], $d = ar + ms$, so $1 = (a/d) r + m_1 s$; cf. [[§11 Properties of Finite Sets#^prop-11-10|Proposition §11.10]]). By Theorem [[§20 Linear Congruences#^thm-20-3|§20.3]] the right-hand congruence has a solution, unique modulo $m_1$. So solutions exist.
>
> *Counting.* Let $r_1 \in R_{m_1}$ represent the unique solution modulo $m_1$, so that an integer $x$ is a solution if and only if $x \equiv r_1 \pmod{m_1}$. Every integer $x$ is congruent modulo $m$ to exactly one $r \in R_m$ (Proposition [[§19 Congruence of Integers#^prop-19-4|§19.4]]), and since $m_1 \mid m$, $\ x \equiv r \pmod m$ implies $x \equiv r \pmod{m_1}$; so $x$ is a solution iff $r$ is, i.e. iff $r \equiv r_1 \pmod{m_1}$, i.e. iff $r = r_1 + m_1 q$ for some $q \in \mathbb{Z}$. For such $r$, using $0 \leq r_1 < m_1$ and $m = m_1 d$,
>
> $$
> 0 \leq r_1 + m_1 q < m \iff 0 \leq q < d .
> $$
>
> (If $q \geq 0$ then $r \geq 0$; if $q \leq -1$ then $r \leq r_1 - m_1 < 0$. If $q \leq d - 1$ then $r \leq r_1 + m - m_1 < m$; if $q \geq d$ then $r \geq m$.) So the solutions in $R_m$ are the $d$ distinct numbers $r_1, r_1 + m_1, \ldots, r_1 + (d-1) m_1$, and $x$ is a solution iff $x \equiv r_1 + m_1 q \pmod m$ for some $0 \leq q < d$.

^pf-20-4

*Uses:* [[§20 Linear Congruences#^cor-20-2|§20.2]], [[§20 Linear Congruences#^thm-20-3|§20.3]], [[§19 Congruence of Integers#^prop-19-4|§19.4]], [[§19 Congruence of Integers#^prop-19-6|§19.6]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]]

> [!remark] Remark: The Degenerate Case $a = 0$
> At first sight [[§20 Linear Congruences#^thm-20-4|Theorem §20.4]] says nothing sensible when $a = 0$; checking it there is a good test. Then $\gcd(0, m) = m$, so it says: $0 \cdot x \equiv b \pmod m$ is solvable iff $m \mid b$, and then there are $m$ solutions modulo $m$. Indeed the congruence reads $0 \equiv b \pmod m$, which does not involve $x$: it holds for every $x$ when $m \mid b$ (all $m$ remainders are solutions) and for no $x$ otherwise. A general result that fails in such a simple case would signal something missed.
>
> *Source: Eccles Exercise 20.3 and its solution*

^rem-20-1

> [!remark]- Connections
> - The same solvability criterion in group theory: [[§8 Invertibility and Unit Groups#^ex-8-4|493 Ex. §8.4]] (solving linear congruences); several congruences to different coprime moduli at once: [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|493 Thm. §9.3]] (Chinese remainder theorem).

## 20.2 Linear Congruences and Diophantine Equations

Now a systematic method, which also proves [[§20 Linear Congruences#^thm-20-3|Theorem §20.3]]. By definition, $ax \equiv b \pmod m$ iff $b - ax$ is a multiple of $m$, i.e. iff $b - ax = my$ for some integer $y$, i.e. $ax + my = b$. So solving the linear congruence is the same as solving the **linear diophantine equation** $ax + my = b$, whose solutions are ordered pairs $(x, y) \in \mathbb{Z}^2$ ([[§18★ Linear Diophantine Equations#^def-18-1|Def. §18.1]]). Precisely:

> [!theorem] Proposition §20.5: Congruences and Diophantine Equations
> For integers $a, b$ and a positive integer $m$, the map
>
> $$
> f : \{(x, y) \in \mathbb{Z}^2 \mid ax + my = b\} \to \{x \in \mathbb{Z} \mid ax \equiv b \pmod m\}, \qquad f(x, y) = x,
> $$
>
> is a bijection, with inverse $g(x) = \bigl(x, (b - ax)/m\bigr)$.
>
> *Eccles: Proposition 20.2.1*

^prop-20-5

> [!proof]+ Proof
> *$f$ maps into the codomain:* if $ax + my = b$, then $ax - b = m(-y)$, so $ax \equiv b \pmod m$.
>
> *$g$ is a well-defined map back:* if $ax_0 \equiv b \pmod m$, then $m$ divides $b - a x_0$, so $y_0 = (b - a x_0)/m$ is an integer, and $a x_0 + m y_0 = b$.
>
> *They are inverse:* $f(g(x_0)) = x_0$ is clear. Conversely, if $ax + my = b$, then $my = b - ax$ and, as $m \neq 0$, $y = (b - ax)/m$; so $g(f(x, y)) = (x, y)$. Thus every solution $x_0$ of the congruence has exactly one preimage, $\bigl(x_0, (b - ax_0)/m\bigr)$, and $f$ is a bijection.

^pf-20-5

*Uses:* [[§19 Congruence of Integers#^def-19-1|Def. §19.1]], [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]] (a map with a two-sided inverse is a bijection)

> [!proof]+ Proof of Theorem §20.3
> Let $a$ and $m$ be coprime. By Bézout ([[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]) there are integers $r, s$ with $ar + ms = 1$; multiplying by $b$, $\ a(rb) + m(sb) = b$. So the diophantine equation $ax + my = b$ has the solution $(rb, sb)$ — this is [[§18★ Linear Diophantine Equations#^thm-18-1|Theorem §18.1]] (Eccles 18.2.1) in the case $\gcd(a, m) = 1$ — and by Proposition [[§20 Linear Congruences#^prop-20-5|§20.5]], $x_0 = rb$ solves $ax \equiv b \pmod m$.
>
> *Uniqueness modulo $m$.* For any integer $x$,
>
> $$
> ax \equiv b \pmod m \iff ax \equiv a x_0 \pmod m \iff x \equiv x_0 \pmod m ,
> $$
>
> the first step because $b \equiv a x_0$, the second by Proposition [[§19 Congruence of Integers#^prop-19-7|§19.7]] since $\gcd(a, m) = 1$.

^pf-20-3

*Uses:* [[§20 Linear Congruences#^prop-20-5|§20.5]], [[§19 Congruence of Integers#^prop-19-7|§19.7]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]], [[§18★ Linear Diophantine Equations#^thm-18-1|§18.1]]

The proof is constructive: the Euclidean algorithm produces $r$ and $s$, hence the solution.

> [!example] Example §20.4: The Euclidean Algorithm Method
> *Solve $290x \equiv 5 \pmod{357}$.* Solve $290x + 357y = 5$. The Euclidean algorithm writes each remainder as an integral combination of $357$ and $290$ (in brackets, minus the quotients, as Eccles writes them: each row is the row two above plus the row above times that row's bracket):
>
> | remainder | | combination | $-$quotient |
> |---|---|---|---|
> | $357$ | $=$ | $357 \times 1 + 290 \times 0$ | |
> | $290$ | $=$ | $357 \times 0 + 290 \times 1$ | $(-1)$ |
> | $67$ | $=$ | $357 \times 1 + 290 \times (-1)$ | $(-4)$ |
> | $22$ | $=$ | $357 \times (-4) + 290 \times 5$ | $(-3)$ |
> | $1$ | $=$ | $357 \times 13 + 290 \times (-16)$ | $(-22)$ |
> | $0$ | | | |
>
> So $\gcd(290, 357) = 1$ and $290 \times (-16) + 357 \times 13 = 1$. Multiplying by $5$: $x = -80$, $y = 65$ solves the diophantine equation, so $x = -80$ solves the congruence. By uniqueness (Proposition [[§19 Congruence of Integers#^prop-19-7|§19.7]]), $290x \equiv 5 \iff 290x \equiv 290 \times (-80) \iff x \equiv -80 \pmod{357}$. Since $-80 \equiv 277$, the answer in least non-negative remainders is
>
> $$
> 290x \equiv 5 \pmod{357} \iff x \equiv 277 \pmod{357} .
> $$
>
> If only the congruence matters, one can work modulo $357$ throughout and track only the multiple of $290$: $357 \equiv 290 \times 0$, $290 \equiv 290 \times 1$, $67 \equiv 290 \times (-1)$, $22 \equiv 290 \times 5$, $1 \equiv 290 \times (-16)$.
>
> *Eccles: Example 20.2.2*

^ex-20-4

> [!example] Example §20.5: A Coefficient Not Coprime to the Modulus
> *Solve $255x \equiv 15 \pmod{621}$.* The Euclidean algorithm on $621, 255$ gives remainders $621, 255, 111, 33, 12, 9, 3, 0$ (quotients $2, 2, 3, 2, 1, 3$), so $\gcd(255, 621) = 3$, which divides $15$: by Theorem [[§20 Linear Congruences#^thm-20-4|§20.4]] there are $3$ solutions modulo $621$. Writing each remainder as a multiple of $255$ modulo $621$:
>
> $$
> 111 \equiv 255 \times (-2), \quad 33 \equiv 255 \times 5, \quad 12 \equiv 255 \times (-17), \quad 9 \equiv 255 \times 39, \quad 3 \equiv 255 \times (-56) .
> $$
>
> Multiplying the last by $5$: $255 \times (-280) \equiv 15$, and $-280 \equiv 341 \pmod{621}$, so $x = 341$ is a solution. To find all of them,
>
> $$
> \begin{aligned}
> 255x \equiv 15 \pmod{621} &\iff 255x \equiv 255 \times 341 \pmod{621} \\
> &\iff 85x \equiv 85 \times 341 \pmod{207} && \text{(§19.6, dividing by } 3) \\
> &\iff x \equiv 341 \equiv 134 \pmod{207} && \text{(§19.7, } \gcd(85, 207) = 1).
> \end{aligned}
> $$
>
> Modulo $621$: $255x \equiv 15 \pmod{621} \iff x \equiv 134, 341$ or $548 \pmod{621}$.
>
> *Eccles: Example 20.2.3*

^ex-20-5

The correspondence also runs the other way: congruence techniques solve diophantine equations.

> [!example] Example §20.6: A Diophantine Equation via Congruences
> *Solve $140x + 63y = 35$.* By Proposition [[§20 Linear Congruences#^prop-20-5|§20.5]], $(x, y) \mapsto x$ is a bijection from its solution set onto that of $140x \equiv 35 \pmod{63}$, and
>
> $$
> \begin{aligned}
> 140x \equiv 35 \pmod{63} &\iff 14x \equiv 35 \pmod{63} && (140 \equiv 14) \\
> &\iff 2x \equiv 5 \pmod 9 && \text{(§19.6, dividing by } 7) \\
> &\iff 2x \equiv 14 \pmod 9 \iff x \equiv 7 \pmod 9 && \text{(§19.7)} \\
> &\iff x = 7 + 9q \ \text{ for some } q \in \mathbb{Z} .
> \end{aligned}
> $$
>
> Substituting, $63y = 35 - 140(7 + 9q) = -945 - 1260q$, so $y = -15 - 20q$. The solutions are $(x, y) = (7 + 9q, \ -15 - 20q)$, $q \in \mathbb{Z}$ — the solution set of [[§18★ Linear Diophantine Equations#^ex-18-3|Example §18.3]] (Eccles 18.4.2), described differently.
>
> *Eccles: Example 20.2.4*

^ex-20-6

For small numbers the congruence manipulations are usually quickest; for large ones the Euclidean algorithm.
