---
type: section
subject: "[[Logic and Proofs]]"
chapter: 4
section: 16
eccles: "Ch. 16"
aliases: ["Eccles 16"]
tags: [logic-and-proofs, mat250]
---
← [[§15 The Division Theorem]] · ↑ [[· 4 Arithmetic]] · [[§17 Consequences of the Euclidean Algorithm]] →

*Eccles, Chapter 16 · MAT 250 HW7 (Exercises 16.1–16.4; Problems IV, Q6–Q8).*

The greatest common divisor was defined in [[§11 Properties of Finite Sets#^def-11-2|Definition §11.2]] as the largest common divisor, and computed there by listing all divisors. That is hopeless for large numbers. Euclid's algorithm (*Elements*, Book VII, found independently in China) computes it by repeated division with remainder ([[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]). Two lemmas drive it: if $b \mid a$ the answer is $b$, and otherwise $\gcd(a, b) = \gcd(b, r)$ where $r$ is the remainder. The proof that the algorithm is correct is an induction hidden behind "and so on". Its by-products, the integral linear combinations of [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]], are the real payoff.

## 16.1 Finding the Greatest Common Divisor

Recall ([[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]]): for integers $a, b$, not both zero, the **greatest common divisor** $\gcd(a, b)$ is the unique positive integer $d$ such that (i) $d \mid a$ and $d \mid b$, and (ii) $c \mid a$ and $c \mid b$ $\Rightarrow$ $c \le d$. Eccles also writes it simply $(a, b)$.

> [!definition] Definition §16.1: Common Divisors
> For integers $a$ and $b$, the set of **common divisors** of $a$ and $b$ is
>
> $$
> D(a, b) = \{c \in \Z \mid c \text{ divides } a \text{ and } c \text{ divides } b\}.
> $$
>
> So $D(a, b) = D(a) \cap D(b)$ in the notation of §11.3. When $a, b$ are not both zero, $D(a, b)$ is finite and non-empty ($1 \in D(a,b)$), and $\gcd(a, b) = \max D(a, b)$ ([[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]]).
>
> *Eccles: Section 16.1 (from Section 11.3)*

^def-16-1

Since $c \mid a \iff c \mid -a$, we have $D(a, b) = D(\pm a, \pm b)$, so signs do not affect the gcd. Also $\gcd(a, 0) = a$ for $a > 0$. So it suffices to find $\gcd(a, b)$ for **positive** $a$ and $b$.

> [!theorem] Lemma §16.1: A Divisor Is the Greatest Common Divisor
> If a positive integer $b$ divides $a$, then $\gcd(a, b) = b$.
>
> *Eccles: Lemma 16.1.1*

^lem-16-1

> [!proof]+ Proof
> Since $b \mid a$ and $b \mid b$, $b \in D(a, b)$. If $c \in D(a, b)$ then $c \mid b$, say $b = ck$. Here $k \neq 0$ because $b \neq 0$, so $|k| \ge 1$ and $|c| \le |c||k| = |b| = b$. Hence $c \le b$, and $b$ is the greatest common divisor.

^pf-16-1

*Uses:* [[§16 The Euclidean Algorithm#^def-16-1|Def. §16.1]]

If $b \nmid a$, the division theorem gives $a = bq + r$ with $0 < r < b$ ([[§15 The Division Theorem#^cor-15-2|Corollary §15.2]]), and the second key observation applies.

> [!theorem] Lemma §16.2: Replacing a by the Remainder
> Let $a$ and $b$ be non-zero integers, and suppose $a = bq + r$ with $q, r \in \Z$. Then $D(a, b) = D(b, r)$, and in particular
>
> $$
> \gcd(a, b) = \gcd(b, r).
> $$
>
> *Eccles: Lemma 16.1.2; the inclusion $D(b,r) \subseteq D(a,b)$ is Exercise 16.4*
> *Source: HW7 (Exercise 16.4)*

^lem-16-2

> [!remark] Remark: Prove Something Stronger
> The definition of $\gcd$ gives no formula in terms of $a$ and $b$, so comparing $\gcd(a, b)$ with $\gcd(b, r)$ head-on is awkward. It is *easier* to prove the stronger statement that the two sets of common divisors are equal: their greatest elements are then equal automatically. Set equality is two inclusions, and each is a one-line computation with the definition of "divides".

^rem-16-1

> [!proof]+ Proof
> ($\subseteq$) Let $c \in D(a, b)$, so $a = cq_1$ and $b = cq_2$ for some $q_1, q_2 \in \Z$. Then
>
> $$
> r = a - bq = cq_1 - cq_2 q = c(q_1 - q_2 q),
> $$
>
> so $c \mid r$. As $c \mid b$ too, $c \in D(b, r)$.
>
> ($\supseteq$, Exercise 16.4) Let $c \in D(b, r)$, so $b = ck_1$ and $r = ck_2$ for some $k_1, k_2 \in \Z$. Then
>
> $$
> a = bq + r = ck_1 q + ck_2 = c(k_1 q + k_2),
> $$
>
> so $c \mid a$. As $c \mid b$ too, $c \in D(a, b)$.
>
> Hence $D(a, b) = D(b, r)$. Both $\gcd$s exist ($b \neq 0$) and are the maxima of the same set, so they are equal.

^pf-16-2

*Uses:* [[§16 The Euclidean Algorithm#^def-16-1|Def. §16.1]]

> [!example] Example §16.1: The gcd of 72 and 30
> $72 = 30 \times 2 + 12$, so $\gcd(72, 30) = \gcd(30, 12)$ by [[§16 The Euclidean Algorithm#^lem-16-2|Lemma §16.2]]. Next $30 = 12 \times 2 + 6$, so $\gcd(30, 12) = \gcd(12, 6)$. Finally $6 \mid 12$, so $\gcd(12, 6) = 6$ by [[§16 The Euclidean Algorithm#^lem-16-1|Lemma §16.1]]. Altogether
>
> $$
> \gcd(72, 30) = \gcd(30, 12) = \gcd(12, 6) = 6,
> $$
>
> as found by listing divisors in [[§11 Properties of Finite Sets#^ex-11-4|Example §11.4]].
>
> *Eccles: Example 16.1.3*

^ex-16-1

![[m250-16-1.svg]]
*The same computation as geometry. Cut as many $30 \times 30$ squares as possible from a $72 \times 30$ rectangle (blue, quotient $2$). The leftover $12 \times 30$ strip takes two $12$-squares (green), and the leftover $12 \times 6$ strip takes two $6$-squares (red) exactly. The last square side, $6$, measures every side in the picture, so it is a common divisor of $72$ and $30$. [[§16 The Euclidean Algorithm#^lem-16-2|Lemma §16.2]] says no larger common measure can have been lost along the way.*

## 16.2 The Euclidean Algorithm

> [!theorem] Theorem §16.3: The Euclidean Algorithm
> Let $a$ and $b$ be positive integers. The following procedure defines a finite sequence of positive integers $a_0, a_1, \ldots, a_n$ with $a_n = \gcd(a, b)$.
> - Put $a_0 = a$, $a_1 = b$.
> - **Step $k$** ($k \ge 1$): $a_0, \ldots, a_k$ having been defined, use the division theorem to write
>
>   $$
>   a_{k-1} = a_k q_k + r_k, \qquad q_k, r_k \in \Z, \quad 0 \le r_k < a_k .
>   $$
>
>   If $r_k = 0$, stop (with $n = k$). Otherwise put $a_{k+1} = r_k$ and carry out step $k + 1$.
>
> *Eccles: Theorem 16.2.1*

^thm-16-3

> [!remark]- Remark: About the Algorithm
> An *algorithm* is a sequence of steps necessarily leading to a desired conclusion. Here $b = a_1 > a_2 > \cdots > a_n > 0$, so the procedure stops after at most $b$ steps. That crude bound would make it a poor algorithm, but in fact the number of steps never exceeds five times the number of decimal digits of the smaller number (written second). This is Lamé's theorem (1845), proved in [[§16 The Euclidean Algorithm#^ex-16-6|Example §16.6]]. The procedure is a loop of four instructions (divide, test the remainder, shift $a_k, a_{k+1}$ down, repeat), which is why it is easy to program. Eccles prints it as a nine-line BASIC program in which `Q=INT(A/B)` is the quotient.
>
> *Eccles: Remarks 16.2.2*

^rem-16-2

> [!example] Example §16.2: The gcd of 232 and 136
> | step | division | |
> |---|---|---|
> | 1 | $232 = 136 \times 1 + 96$ | $a_2 = 96$ |
> | 2 | $136 = 96 \times 1 + 40$ | $a_3 = 40$ |
> | 3 | $96 = 40 \times 2 + 16$ | $a_4 = 16$ |
> | 4 | $40 = 16 \times 2 + 8$ | $a_5 = 8$ |
> | 5 | $16 = 8 \times 2 + 0$ | stop |
>
> So $a_0 = 232$, $a_1 = 136$, $a_2 = 96$, $a_3 = 40$, $a_4 = 16$, $a_5 = 8$, and $\gcd(232, 136) = 8$. By hand it is enough to write the column of the $a_k$, each followed by the multiple subtracted to get the next one (the quotient):
>
> $$
> 232,\quad 136\ (-1),\quad 96\ (-1),\quad 40\ (-2),\quad 16\ (-2),\quad 8\ (-2),\quad 0.
> $$
>
> This shorthand means nothing to a reader who has not been told the convention, so preface it with "applying the Euclidean algorithm gives the following sequence of remainders".
>
> *Eccles: Example 16.2.3*

^ex-16-2

> [!remark] Remark: The Dots Are an Induction
> In the example, repeated use of [[§16 The Euclidean Algorithm#^lem-16-2|Lemma §16.2]] gives $\gcd(232, 136) = \gcd(136, 96) = \gcd(96, 40) = \gcd(40, 16) = \gcd(16, 8) = 8$. In general, $\gcd(a, b) = \gcd(a_0, a_1) = \gcd(a_1, a_2) = \cdots = \gcd(a_{n-1}, a_n) = a_n$. That is the whole idea of the proof. The dots ("and so on") signal that, strictly, the induction principle ([[§5 The Induction Principle#^def-5-1|Definition §5.1]]) is being used, and the formal proof below makes the induction explicit.

^rem-16-3

> [!proof]+ Proof
> **The procedure stops.** At every step that does not stop, the new term is a remainder: $a_{k+1} = r_k < a_k$, and $a_{k+1} = r_k > 0$. Hence $b = a_1 > a_2 > a_3 > \cdots$ are positive integers, and by induction on $k$, $a_k \le b - (k - 1)$ for every $k \ge 1$ for which $a_k$ is defined. As $a_k \ge 1$, this forces $k \le b$. So the procedure cannot run past step $b$: for some $n \le b$ we get $r_n = 0$, and it stops with $a_0, a_1, \ldots, a_n$.
>
> **The last term is the gcd.** For $1 \le k \le n$ let $P(k)$ be the statement $\gcd(a_0, a_1) = \gcd(a_{k-1}, a_k)$. We prove $P(k)$ for all $1 \le k \le n$ by induction on $k$.
> - *Base case.* $P(1)$ says $\gcd(a_0, a_1) = \gcd(a_0, a_1)$.
> - *Inductive step.* Suppose $P(k)$ holds for some $k$ with $1 \le k < n$. Step $k$ did not stop, so $a_{k-1} = a_k q_k + a_{k+1}$, with $a_{k-1}, a_k$ non-zero. By [[§16 The Euclidean Algorithm#^lem-16-2|Lemma §16.2]], $\gcd(a_{k-1}, a_k) = \gcd(a_k, a_{k+1})$, so with $P(k)$, $\gcd(a_0, a_1) = \gcd(a_k, a_{k+1})$. This is $P(k+1)$.
>
> So $P(n)$ holds: $\gcd(a, b) = \gcd(a_0, a_1) = \gcd(a_{n-1}, a_n)$. At step $n$ the remainder is $r_n = 0$, so $a_{n-1} = a_n q_n$, i.e. the positive integer $a_n$ divides $a_{n-1}$. By [[§16 The Euclidean Algorithm#^lem-16-1|Lemma §16.1]], $\gcd(a_{n-1}, a_n) = a_n$. Hence $\gcd(a, b) = a_n$.

^pf-16-3

*Uses:* [[§15 The Division Theorem#^thm-15-1|§15.1]], [[§16 The Euclidean Algorithm#^lem-16-1|§16.1]], [[§16 The Euclidean Algorithm#^lem-16-2|§16.2]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]] (induction)

> [!remark]- Connections
> - The gcd in group theory: [[§8 Invertibility and Unit Groups#^def-8-1|493 Def. §8.1]]. There the algorithm, run backwards, computes an [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-5|inverse]] modulo $26$: [[§8 Invertibility and Unit Groups#^ex-8-3|493 Ex. §8.3]].

> [!example] Example §16.3: Four gcd Computations
> Applying the Euclidean algorithm:
>
> | step | $(7684,\ 4148)$ | $(11033442,\ 1102246)$ | $(252,\ 165)$ | $(4284,\ 3480)$ |
> |---|---|---|---|---|
> | 1 | $7684 = 4148 \cdot 1 + 3536$ | $11033442 = 1102246 \cdot 10 + 10982$ | $252 = 165 \cdot 1 + 87$ | $4284 = 3480 \cdot 1 + 804$ |
> | 2 | $4148 = 3536 \cdot 1 + 612$ | $1102246 = 10982 \cdot 100 + 4046$ | $165 = 87 \cdot 1 + 78$ | $3480 = 804 \cdot 4 + 264$ |
> | 3 | $3536 = 612 \cdot 5 + 476$ | $10982 = 4046 \cdot 2 + 2890$ | $87 = 78 \cdot 1 + 9$ | $804 = 264 \cdot 3 + 12$ |
> | 4 | $612 = 476 \cdot 1 + 136$ | $4046 = 2890 \cdot 1 + 1156$ | $78 = 9 \cdot 8 + 6$ | $264 = 12 \cdot 22 + 0$ |
> | 5 | $476 = 136 \cdot 3 + 68$ | $2890 = 1156 \cdot 2 + 578$ | $9 = 6 \cdot 1 + 3$ | |
> | 6 | $136 = 68 \cdot 2 + 0$ | $1156 = 578 \cdot 2 + 0$ | $6 = 3 \cdot 2 + 0$ | |
> | **gcd** | $68$ | $578$ | $3$ | $12$ |
>
> A seven-digit pair took six steps, far below the bound $5 \times 7 = 35$ of [[§16 The Euclidean Algorithm#^ex-16-6|Lamé's theorem]].
>
> *Eccles: Exercises 16.1, 16.2; Problems IV, Q6*
> *Source: HW7*

^ex-16-3

> [!example] Example §16.4: Does the Order of a and b Matter?
> The *result* cannot depend on the order, since $D(a, b) = D(b, a)$; only the run changes. Suppose $a < b$ and we start with $a_0 = a$, $a_1 = b$. Step 1 reads
>
> $$
> a = b \times 0 + a, \qquad 0 \le a < b,
> $$
>
> so $q_1 = 0$ and $a_2 = a$. Now $(a_1, a_2) = (b, a)$, and from here on the steps are exactly those of the run started with the larger number first. Writing the smaller number first costs one extra step, which simply swaps the two numbers. (If $a = b$, both orders stop after one step.)
>
> *Eccles: Exercise 16.3*
> *Source: HW7*

^ex-16-4

> [!example] Example §16.5: Consecutive Fibonacci Numbers
> Let $u_1 = u_2 = 1$, $u_{m+1} = u_m + u_{m-1}$ be the Fibonacci numbers ([[§5 The Induction Principle#^def-5-5|Definition §5.5]]). The problem asks to show that the Euclidean algorithm takes precisely $n$ steps to show $\gcd(u_{n+1}, u_n) = 1$. With the step count of [[§16 The Euclidean Algorithm#^thm-16-3|Theorem §16.3]] (every division counts, including the last), the exact count is:
>
> **Claim.** For $n \ge 2$ the algorithm on $a = u_{n+1}$, $b = u_n$ takes exactly $n - 1$ steps, with $a_k = u_{n+1-k}$ and $q_k = 1$ before the last step. Equivalently, the pair $(u_{n+2}, u_{n+1})$ takes exactly $n$ steps for every $n \ge 1$.
>
> **Proof.** First, $1 = u_2 < u_3 < u_4 < \cdots$: for $m \ge 2$, $u_{m+1} = u_m + u_{m-1} > u_m$ since $u_{m-1} \ge 1$. So for $j \ge 3$,
>
> $$
> u_{j+1} = u_j \times 1 + u_{j-1}, \qquad 0 \le u_{j-1} < u_j ,
> $$
>
> is *the* division of $u_{j+1}$ by $u_j$ (uniqueness, [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]), with non-zero remainder $u_{j-1}$. By induction on $k$, for $1 \le k \le n - 2$ step $k$ divides $a_{k-1} = u_{n+2-k}$ by $a_k = u_{n+1-k}$ (here $j = n + 1 - k \ge 3$), with quotient $1$, and produces $a_{k+1} = u_{n-k}$. So $a_{n-2} = u_3 = 2$ and $a_{n-1} = u_2 = 1$, and step $n - 1$ is $2 = 1 \times 2 + 0$: the algorithm stops with $\gcd = a_{n-1} = 1$ after $n - 1$ steps. (For $n = 2$ this is the single step $2 = 1 \times 2 + 0$.) Replacing $n$ by $n + 1$ gives the second form.
>
> The pairs $(u_{n+2}, u_{n+1})$ are the slowest possible: by [[§16 The Euclidean Algorithm#^ex-16-6|Example §16.6]], an $n$-step run needs $b \ge u_{n+1}$.
>
> *Eccles: Problems IV, Q7*
> *Source: HW7*
>
> *As printed, the count in Problems IV Q7 is off by one: with $u_1 = u_2 = 1$ the run on $(u_{n+1}, u_n)$ ends at $u_3 = 2 \cdot u_2$. The HW7 solution reaches $n$ by continuing the chain to $(u_2, u_1)$, but $u_3 = u_2 \cdot 1 + u_1$ is not a division step, since its remainder $u_1 = 1$ is not less than $u_2 = 1$.*

^ex-16-5

> [!example] Example §16.6: Lamé's Theorem
> Let $a \ge b$ be positive integers, and let $a_0, a_1, \ldots, a_n$ be the sequence generated by the Euclidean algorithm, so that $a_n = \gcd(a, b)$ and the algorithm takes $n$ steps. Let $u_m$ be the Fibonacci numbers ([[§16 The Euclidean Algorithm#^ex-16-5|Example §16.5]]).
> 1. $a_{n-k} \ge u_{k+2}$ for $0 \le k \le n - 1$. In particular $b \ge u_{n+1}$.
> 2. **(Lamé)** If $b$ has $r$ decimal digits, then $n \le 5r$.
>
> *Eccles: Problems IV, Q8*
> *Source: HW7*

^ex-16-6

> [!proof]- Solution
> **Facts about the run.** For $1 \le k \le n$, step $k$ reads $a_{k-1} = a_k q_k + a_{k+1}$, where we write $a_{n+1} = r_n = 0$. Moreover $a_1 > a_2 > \cdots > a_n \ge 1$, and $a_0 = a \ge b = a_1$. Every quotient satisfies $q_k \ge 1$: if $q_k \le 0$ then $a_{k-1} = a_k q_k + a_{k+1} \le a_{k+1} < a_k$, contradicting $a_{k-1} \ge a_k$. If $n \ge 2$ then also $q_n \ge 2$, since $a_{n-1} = a_n q_n$ with $a_{n-1} > a_n$.
>
> **Part 1**, by induction on $k$ in which each step uses the *two* preceding cases (strong induction, [[§5 The Induction Principle#^thm-5-6|Theorem §5.6]]); so two base cases are needed.
> - $k = 0$: $a_n \ge 1 = u_2$.
> - $k = 1$ (when $n \ge 2$): $a_{n-1} = a_n q_n \ge 1 \cdot 2 = 2 = u_3$.
> - *Step.* Let $1 \le k \le n - 2$ and suppose $a_{n-k} \ge u_{k+2}$ and $a_{n-k+1} \ge u_{k+1}$. Step $n - k$ gives
>
>   $$
>   a_{n-k-1} = a_{n-k}\, q_{n-k} + a_{n-k+1} \ \ge\ a_{n-k} + a_{n-k+1} \ \ge\ u_{k+2} + u_{k+1} = u_{k+3},
>   $$
>
>   which is the statement for $k + 1$.
>
> Hence $a_{n-k} \ge u_{k+2}$ for $0 \le k \le n - 1$, and $k = n - 1$ gives $b = a_1 \ge u_{n+1}$.
>
> **A lower bound for Fibonacci numbers.** Let $\alpha = (1 + \sqrt5)/2$, so $\alpha > 1$ and $\alpha^2 = \alpha + 1$. Then $u_m \ge \alpha^{m-2}$ for all $m \ge 1$. Again two base cases: $u_1 = 1 \ge \alpha^{-1}$ and $u_2 = 1 = \alpha^0$. Step: for $m \ge 2$,
>
> $$
> u_{m+1} = u_m + u_{m-1} \ \ge\ \alpha^{m-2} + \alpha^{m-3} = \alpha^{m-3}(\alpha + 1) = \alpha^{m-3}\alpha^2 = \alpha^{m-1}.
> $$
>
> **The hint: $\log_{10}\alpha > 1/5$, i.e. $\alpha^5 > 10$.** From $\alpha^2 = \alpha + 1$: $\alpha^3 = 2\alpha + 1$, $\alpha^4 = 3\alpha + 2$, $\alpha^5 = 5\alpha + 3 = (11 + 5\sqrt5)/2$. Since $2.2^2 = 4.84 < 5$, $\sqrt5 > 2.2$ and $\alpha^5 > (11 + 11)/2 = 11 > 10$.
>
> **Part 2.** If $b$ has $r$ digits then $b < 10^r$. By Part 1 and the bound, $\alpha^{n-1} \le u_{n+1} \le b < 10^r$. Taking $\log_{10}$ (an increasing function),
>
> $$
> \frac{n-1}{5} \ \le\ (n - 1)\log_{10}\alpha \ <\ r ,
> $$
>
> so $n - 1 < 5r$. Since $n$ and $5r$ are integers, $n \le 5r$.
>
> *The HW7 solution's two inductions (for $a_{n-k} \ge u_{k+2}$, and for $u_m > \alpha^{m-2}$ from $m = 3$) each start from one base case, although each inductive step uses the two preceding cases; the second base case is supplied here.*

^pf-ex-16-6

*Uses:* [[§16 The Euclidean Algorithm#^thm-16-3|§16.3]], [[§16 The Euclidean Algorithm#^ex-16-5|Ex. §16.5]], [[§5 The Induction Principle#^def-5-5|Def. §5.5]], [[§5 The Induction Principle#^thm-5-6|§5.6]] (strong induction)
