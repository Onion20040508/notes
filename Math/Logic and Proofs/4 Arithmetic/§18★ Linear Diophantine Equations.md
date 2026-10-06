---
type: section
subject: "[[Logic and Proofs]]"
chapter: 4
section: 18
eccles: "Ch. 18"
aliases: ["Eccles 18"]
tags: [logic-and-proofs, mat250, extension]
---
← [[§17 Consequences of the Euclidean Algorithm]] · ↑ [[· 4 Arithmetic]] · [[§19 Congruence of Integers]] →

*Eccles, Chapter 18 (with Problems IV, Q12).*
★ *Not in the MAT 250 course record (no homework or syllabus entry for this chapter); included from Eccles because it is the direct application of the Bézout coefficients computed in HW7 ([[§17 Consequences of the Euclidean Algorithm#^ex-17-2|Example §17.2]]).*

An ancient problem, solved completely by Brahmagupta in the seventh century: **given integers $a, b, c$, find all integers $m, n$ with $am + bn = c$.** The answer has two parts. A solution exists exactly when $\gcd(a, b) \mid c$; necessity is the divisibility argument already used in [[§4 Proof by Contradiction#^prop-4-1|Proposition §4.1]], and sufficiency is Bézout ([[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]). If one solution exists, all of them are that solution plus the solutions of the *homogeneous* equation $am + bn = 0$, and those are found with [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]].

## 18.1 Diophantine Equations

> [!definition] Definition §18.1: Diophantine Equation
> A **diophantine equation** is an equation in one or more unknowns that is to be solved in the integers. A **linear diophantine equation** in two unknowns is one of the form
>
> $$
> am + bn = c \qquad (a, b, c \in \Z \text{ given}), \tag{18.1}
> $$
>
> and a **solution** is a pair $(m, n) \in \Z \times \Z = \Z^2$ satisfying it.
>
> *Eccles: Problem 18.0.1, Section 18.1*

^def-18-1

> [!remark]- Remark: History
> The name honours Diophantus (third century A.D.), whose *Arithmetica* is the high point of Greek number theory; he was usually content with one positive solution. In 1637 Fermat wrote in the margin of his copy that $x^n + y^n = z^n$ has no solutions in positive integers for $n \ge 3$, "a truly marvellous demonstration of which this margin is too narrow to contain". Fermat proved the case $n = 4$ and Euler (completed by Legendre) the case $n = 3$. The general case, Fermat's Last Theorem, was proved by Andrew Wiles in 1994. Closer to home, the theorem that $\sqrt2$ is irrational ([[§13 Number Systems#^thm-13-4|Theorem §13.4]]) is a statement about a diophantine equation: the only solution of $m^2 = 2n^2$ is $m = n = 0$.

^rem-18-1

## 18.2 A Condition for the Existence of Solutions

> [!theorem] Theorem §18.1: Existence of Solutions
> For positive integers $a$, $b$ and $c$, there exist integers $m$ and $n$ such that
>
> $$
> am + bn = c
> $$
>
> if and only if $\gcd(a, b)$ divides $c$.
>
> *Eccles: Theorem 18.2.1*

^thm-18-1

> [!proof]+ Proof
> (*Necessity.*) Suppose $am_0 + bn_0 = c$ with $m_0, n_0 \in \Z$, and let $d = \gcd(a, b)$. Since $d \mid a$ and $d \mid b$, $a = dq_1$ and $b = dq_2$ for some integers $q_1, q_2$. Hence $c = (dq_1)m_0 + (dq_2)n_0 = d(q_1 m_0 + q_2 n_0)$, so $d \mid c$.
>
> (*Sufficiency.*) The simplest case is $c = \gcd(a, b)$, and then [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]] is exactly the statement that a solution exists. In general, if $d \mid c$, write $c = dq$ with $q \in \Z$ and choose $m_0, n_0$ with $am_0 + bn_0 = d$ by Theorem §17.1. Then
>
> $$
> a(m_0 q) + b(n_0 q) = dq = c,
> $$
>
> so $m = m_0 q$, $n = n_0 q$ is a solution.

^pf-18-1

*Uses:* [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]]

Positivity is not used: the same proof works for any integers $a, b$, not both zero, and any $c$ (Eccles Exercise 18.2 does a case with a minus sign; see [[§18★ Linear Diophantine Equations#^ex-18-4|Example §18.4]]). For instance, [[§4 Proof by Contradiction#^prop-4-1|Proposition §4.1]] (Eccles Proposition 4.1.1) showed that $14m + 20n = 101$ has no integer solutions, because $2$ divides $14m + 20n$ but not $101$. In the language of the theorem, $\gcd(14, 20) = 2 \nmid 101$.

> [!example] Example §18.1: One Solution of 140m + 63n = 35
> Applying the [[§16 The Euclidean Algorithm#^thm-16-3|Euclidean algorithm]] to $140$ and $63$, and carrying the multipliers along as in [[§17 Consequences of the Euclidean Algorithm#^ex-17-1|Example §17.1]]:
>
> | $a_k$ | $= 140 \times m_k$ | $+\ 63 \times n_k$ | quotient |
> |---|---|---|---|
> | $140$ | $1$ | $0$ | |
> | $63$ | $0$ | $1$ | $(-2)$ |
> | $14$ | $1$ | $-2$ | $(-4)$ |
> | $\mathbf{7}$ | $\mathbf{-4}$ | $\mathbf{9}$ | $(-2)$ |
> | $0$ | | | |
>
> So $\gcd(140, 63) = 7$, and $7 \mid 35$, so a solution exists ([[§18★ Linear Diophantine Equations#^thm-18-1|Theorem §18.1]]). From $140 \times (-4) + 63 \times 9 = 7$, multiplying by $35/7 = 5$ gives $140 \times (-20) + 63 \times 45 = 35$: one solution is $m = -20$, $n = 45$.
>
> *Eccles: Example 18.2.2*

^ex-18-1

## 18.3 Finding All the Solutions: the Homogeneous Case

One solution is not the end of the story; there is no reason to expect only one. We start with $c = 0$, where $(0, 0)$ is always a solution.

> [!definition] Definition §18.2: Homogeneous Equation
> The diophantine equation
>
> $$
> am + bn = 0 \tag{18.2}
> $$
>
> is **homogeneous**. It is the homogeneous equation **associated with** (18.1); equation (18.1) is called **inhomogeneous** if $c \neq 0$.
>
> *Eccles: Section 18.3*

^def-18-2

> [!example] Example §18.2: All Solutions of 140m + 63n = 0
> Since $\gcd(140, 63) = 7$ ([[§18★ Linear Diophantine Equations#^ex-18-1|Example §18.1]]), divide through by $7$. For $m, n \in \Z$,
>
> $$
> 140m + 63n = 0 \iff 20m + 9n = 0 \iff 20m = -9n \ \Rightarrow\ 9 \mid 20m,
> $$
>
> since $-9n = 9(-n)$. As $9$ and $20$ are coprime, [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]] gives $9 \mid m$, say $m = 9q$. Substituting, $20 \times 9q = -9n$, so $n = -20q$. Conversely $(9q, -20q)$ is a solution for every $q$. So the solutions are
>
> $$
> (m, n) = (9q, -20q), \qquad q \in \Z,
> $$
>
> one for each integer $q$:
>
> | $q$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|---|---|
> | $(m, n)$ | $(-18, 40)$ | $(-9, 20)$ | $(0, 0)$ | $(9, -20)$ | $(18, -40)$ | $(27, -60)$ |
>
> (Dividing $am + bn = 0$ by $\gcd(a, b)$ always leaves coprime coefficients: [[§11 Properties of Finite Sets#^prop-11-10|Proposition §11.10]], Eccles Exercise 11.4.)
>
> *Eccles: Example 18.3.1*

^ex-18-2

The key part of this argument, abstracted:

> [!theorem] Proposition §18.2: The Homogeneous Equation with Coprime Coefficients
> Let $a$ and $b$ be coprime non-zero integers. Then for $(m, n) \in \Z^2$,
>
> $$
> am + bn = 0 \iff (m, n) = (bq, -aq) \text{ for some } q \in \Z .
> $$
>
> *Eccles: Proposition 18.3.2*

^prop-18-2

> [!proof]+ Proof
> ($\Leftarrow$) By substitution: $a(bq) + b(-aq) = 0$.
>
> ($\Rightarrow$) If $am + bn = 0$ then $am = b(-n)$, so $b \mid am$. Since $b$ and $a$ are coprime, [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]] gives $b \mid m$, say $m = bq$ with $q \in \Z$. Substituting, $abq + bn = 0$, i.e. $b(aq + n) = 0$. As $b \neq 0$, $n = -aq$.

^pf-18-2

*Uses:* [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|§17.4]]

With it, [[§18★ Linear Diophantine Equations#^ex-18-2|Example §18.2]] becomes two lines: $140m + 63n = 0 \iff 20m + 9n = 0 \iff (m, n) = (9q, -20q)$ for some $q \in \Z$, since $9$ and $20$ are coprime (Eccles Example 18.3.3). Take care to get $a$ and $b$ the right way round and the signs right. The safest check is to substitute the claimed solutions back into the equation.

> [!remark]- Remark: The Extra Row of the Table
> Continue Method 2 for one more row, the one with $a_{N+1} = 0$, to get $0 = a\,m_{N+1} + b\,n_{N+1}$. In [[§18★ Linear Diophantine Equations#^ex-18-1|Example §18.1]] the next row is $0 = 140 \times 9 + 63 \times (-20)$: exactly the generator $(9, -20)$ of [[§18★ Linear Diophantine Equations#^ex-18-2|Example §18.2]]. This always happens (Eccles Problems IV, Q12). For $a, b > 0$ the homogeneous solutions are precisely $(m_{N+1} q,\ n_{N+1} q)$, $q \in \Z$.
>
> *Why.* The identity of [[§17 Consequences of the Euclidean Algorithm#^ex-17-4|Example §17.4]] (HW7) extends to $k = N + 1$ with the same inductive step, so $m_{N+1}, n_{N+1}$ are coprime. Write $a = da'$, $b = db'$ with $d = \gcd(a, b)$, so that $a', b'$ are coprime ([[§11 Properties of Finite Sets#^prop-11-10|Proposition §11.10]]). Dividing $a m_{N+1} + b n_{N+1} = 0$ by $d$ and applying [[§18★ Linear Diophantine Equations#^prop-18-2|Proposition §18.2]] gives $(m_{N+1}, n_{N+1}) = (b't, -a't)$ for some $t \in \Z$. Since $t$ divides both $m_{N+1}$ and $n_{N+1}$, $t = \pm 1$. So the multiples of $(m_{N+1}, n_{N+1})$ are the multiples of $(b', -a')$, which are all the solutions by Proposition §18.2.
>
> *Eccles: Problems IV, Q12*

^rem-18-2

## 18.4 Finding All the Solutions: the General Case

Once (18.1) has one solution, all its solutions come from solving the associated homogeneous equation (18.2).

> [!theorem] Proposition §18.3: Particular Solution plus Homogeneous Solutions
> Suppose $(m_0, n_0) \in \Z^2$ is a solution of $am + bn = c$, i.e. $am_0 + bn_0 = c$. Then for $(m, n) \in \Z^2$,
>
> $$
> am + bn = c \iff a(m - m_0) + b(n - n_0) = 0 .
> $$
>
> *Eccles: Proposition 18.4.1*

^prop-18-3

> [!proof]+ Proof
> $$
> am + bn = c \iff am + bn = am_0 + bn_0 \iff a(m - m_0) + b(n - n_0) = 0 .
> $$

^pf-18-3

*Uses:* [[§2 Implications#^def-2-8|Def. §2.8]] (algebraic properties)

Putting the pieces together gives the complete answer to the problem. Eccles carries it out in examples; here it is in general form.

> [!theorem] Corollary §18.4: All Solutions of am + bn = c
> Let $a, b$ be non-zero integers, $d = \gcd(a, b)$, and write $a = da'$, $b = db'$. Then $a'$ and $b'$ are coprime. If $d \mid c$ and $(m_0, n_0)$ is one solution of $am + bn = c$, then the solutions are exactly
>
> $$
> (m, n) = \bigl(m_0 + b'q,\ \ n_0 - a'q\bigr), \qquad q \in \Z ,
> $$
>
> one for each $q$. In particular the equation has either no solutions ($d \nmid c$) or infinitely many.
>
> *Eccles: Sections 18.3–18.4 and Exercise 11.4 (assembled from Examples 18.3.1 and 18.4.2)*

^cor-18-4

> [!proof]+ Proof
> *$a', b'$ are coprime* by [[§11 Properties of Finite Sets#^prop-11-10|Proposition §11.10]]. (Alternatively, by Bézout: $d = am + bn = d(a'm + b'n)$ for some $m, n \in \Z$ ([[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]); cancelling $d$ gives $a'm + b'n = 1$, and [[§17 Consequences of the Euclidean Algorithm#^prop-17-3|Proposition §17.3]] applies.) They are non-zero since $a, b$ are.
>
> *The solutions.* By [[§18★ Linear Diophantine Equations#^prop-18-3|Proposition §18.3]] and cancelling $d \neq 0$,
>
> $$
> am + bn = c \iff d\bigl(a'(m - m_0) + b'(n - n_0)\bigr) = 0 \iff a'(m - m_0) + b'(n - n_0) = 0 ,
> $$
>
> and by [[§18★ Linear Diophantine Equations#^prop-18-2|Proposition §18.2]] this holds iff $(m - m_0, n - n_0) = (b'q, -a'q)$ for some $q \in \Z$. Different $q$ give different pairs since $b' \neq 0$. The last sentence follows from [[§18★ Linear Diophantine Equations#^thm-18-1|Theorem §18.1]] in its general form.

^pf-18-4

*Uses:* [[§11 Properties of Finite Sets#^prop-11-10|§11.10]], [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]], [[§17 Consequences of the Euclidean Algorithm#^prop-17-3|§17.3]], [[§18★ Linear Diophantine Equations#^thm-18-1|§18.1]], [[§18★ Linear Diophantine Equations#^prop-18-2|§18.2]], [[§18★ Linear Diophantine Equations#^prop-18-3|§18.3]]

![[m250-18-1.svg]]
*The solutions of $3m + 5n = 7$ (red) are the lattice points on a line. Here $\gcd(3, 5) = 1$, a particular solution is $(4, -1)$ (blue arrow), and consecutive solutions differ by $(b', -a') = (5, -3)$ (green). The homogeneous solutions $(5q, -3q)$ (black) lie on the parallel line through the origin. The red line is that line shifted by $(4, -1)$, which is [[§18★ Linear Diophantine Equations#^prop-18-3|Proposition §18.3]]. No lattice point of the red line lies between two consecutive red dots: that is the coprimality in [[§18★ Linear Diophantine Equations#^prop-18-2|Proposition §18.2]].*

> [!remark]- Connections
> - The same structure as for linear equations: the solution set is a translate $(m_0, n_0) + H$ of the solution set $H$ of the homogeneous equation, cf. [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR Def. 3.97]] (translate), where solvable inhomogeneous systems have the [[§8 Null Spaces and Ranges#^ladr-3-11|null space]] as $H$. Here $H = \{(b'q, -a'q)\}$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $\Z^2$ rather than a subspace.
> - The case $c = 1$ with $b = n$: $am + nk = 1$ is solvable iff $\gcd(a, n) = 1$, which is [[§8 Invertibility and Unit Groups#^prop-8-1|493 Prop. §8.1]] (inverses modulo $n$). Linear congruences return in [[§20 Linear Congruences#^thm-20-4|Theorem §20.4]], whose solvability condition is this theorem read modulo $n$ ([[§20 Linear Congruences#^prop-20-5|Proposition §20.5]]).

> [!example] Example §18.3: All Solutions of 140m + 63n = 35
> From [[§18★ Linear Diophantine Equations#^ex-18-1|Example §18.1]] the particular solution $(-20, 45)$, so by [[§18★ Linear Diophantine Equations#^prop-18-3|Proposition §18.3]] and [[§18★ Linear Diophantine Equations#^ex-18-2|Example §18.2]],
>
> $$
> \begin{aligned}
> 140m + 63n = 35 &\iff 140(m + 20) + 63(n - 45) = 0\\
> &\iff (m + 20,\ n - 45) = (9q, -20q) \text{ for some } q \in \Z\\
> &\iff (m, n) = (-20 + 9q,\ 45 - 20q) \text{ for some } q \in \Z .
> \end{aligned}
> $$
>
> | $q$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|---|---|
> | $m$ | $-38$ | $-29$ | $-20$ | $-11$ | $-2$ | $7$ |
> | $n$ | $85$ | $65$ | $45$ | $25$ | $5$ | $-15$ |
>
> Starting instead from the particular solution $(-2, 5)$ gives $(m, n) = (-2 + 9q, 5 - 20q)$. This is the same set, with $q$ shifted by $2$; a solution set does not depend on which particular solution is used to describe it.
>
> *Eccles: Example 18.4.2*

^ex-18-3

Eccles returns to this equation in Example 20.2.4 with a method using congruences: [[§20 Linear Congruences#^ex-20-6|Example §20.6]].

> [!example] Example §18.4: Using the HW7 Coefficients
> **$7684m + 4148n = 272$.** In HW7 ([[§17 Consequences of the Euclidean Algorithm#^ex-17-2|Example §17.2]]) we found $\gcd(7684, 4148) = 68$ and $7684 \times 27 + 4148 \times (-50) = 68$. Since $272 = 4 \times 68$, solutions exist, and multiplying by $4$ gives the particular solution $(108, -200)$. With $a' = 7684/68 = 113$ and $b' = 4148/68 = 61$, [[§18★ Linear Diophantine Equations#^cor-18-4|Corollary §18.4]] gives all solutions:
>
> $$
> (m, n) = (108 + 61q,\ -200 - 113q), \qquad q \in \Z .
> $$
>
> (The extra row of the HW7 table is $0 = 7684 \times (-61) + 4148 \times 113$, as the [[§18★ Linear Diophantine Equations#^rem-18-2|Remark]] predicts.)
>
> **$7684m - 4148n = 272$.** This holds iff $(m, -n)$ solves the first equation, so the solutions are $(m, n) = (108 + 61q,\ 200 + 113q)$, $q \in \Z$.
>
> *Eccles: Exercises 18.1, 18.2*

^ex-18-4

> [!example] Example §18.5: The Unique Positive Solution of 516m + 564n = 6432
> The Euclidean algorithm on $564, 516$ with multipliers:
>
> | $a_k$ | $= 564 \times m_k$ | $+\ 516 \times n_k$ | quotient |
> |---|---|---|---|
> | $564$ | $1$ | $0$ | |
> | $516$ | $0$ | $1$ | $(-1)$ |
> | $48$ | $1$ | $-1$ | $(-10)$ |
> | $36$ | $-10$ | $11$ | $(-1)$ |
> | $\mathbf{12}$ | $\mathbf{11}$ | $\mathbf{-12}$ | $(-3)$ |
> | $0$ | | | |
>
> So $\gcd = 12$ and $516 \times (-12) + 564 \times 11 = 12$. Since $6432 = 12 \times 536$, a particular solution is $m = -12 \times 536 = -6432$, $n = 11 \times 536 = 5896$. With $516 = 12 \times 43$ and $564 = 12 \times 47$, [[§18★ Linear Diophantine Equations#^cor-18-4|Corollary §18.4]] gives all solutions:
>
> $$
> (m, n) = (-6432 + 47q,\ 5896 - 43q), \qquad q \in \Z .
> $$
>
> **Positive solutions.** $m > 0 \iff 47q > 6432 \iff q > 136\tfrac{40}{47} \iff q \ge 137$, and $n > 0 \iff 43q < 5896 \iff q < 137\tfrac{5}{43} \iff q \le 137$. So $q = 137$ is the only possibility, giving the unique positive solution $(m, n) = (7, 5)$. Check: $516 \times 7 + 564 \times 5 = 3612 + 2820 = 6432$.
>
> (For positive solutions alone it is quicker to note $n < 6432/564$, so $n \le 11$, and test each $n$.)
>
> *Eccles: Exercise 18.3*

^ex-18-5
