---
type: section
subject: "[[Logic and Proofs]]"
chapter: 4
section: 17
eccles: "Ch. 17"
aliases: ["Eccles 17"]
tags: [logic-and-proofs, mat250]
---
← [[§16 The Euclidean Algorithm]] · ↑ [[· 4 Arithmetic]] · [[§18★ Linear Diophantine Equations]] →

*Eccles, Chapter 17 · MAT 250 HW7 (Exercises 17.1, 17.2, 17.6; Problems IV, Q10, Q11).*

Run backwards (or, better, carried along), the Euclidean algorithm ([[§16 The Euclidean Algorithm#^thm-16-3|Theorem §16.3]]) writes $\gcd(a, b)$ as $am + bn$ with integers $m, n$. This fact (Bézout's identity) is both a computational tool and the theoretical key to elementary number theory. From it: every common divisor divides the gcd; $a$ and $b$ are coprime exactly when $am + bn = 1$ is solvable; and if $a \mid bc$ with $a, b$ coprime then $a \mid c$. The last of these is the lemma behind unique factorization ([[§23 The Sequence of Prime Numbers#^thm-23-5|Theorem §23.5]]).

## 17.1 Integral Linear Combinations

> [!theorem] Theorem §17.1: The gcd Is an Integral Linear Combination
> Let $a, b$ be integers, at least one of which is non-zero. Then there exist integers $m$ and $n$ such that
>
> $$
> \gcd(a, b) = am + bn.
> $$
>
> *Eccles: Theorem 17.1.1*

^thm-17-1

> [!definition] Definition §17.1: Integral Linear Combination
> Given integers $a$ and $b$, an integer $c$ is an **integral linear combination** of $a$ and $b$ if there exist integers $m$ and $n$ such that $c = am + bn$.
>
> *Eccles: Definition 17.1.2*

^def-17-1

So [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]] says that the greatest common divisor of two integers is an integral linear combination of them. The idea of the proof is visible in an example.

> [!example] Example §17.1: Writing 8 in Terms of 232 and 136
> The Euclidean algorithm gave $\gcd(232, 136) = 8$ ([[§16 The Euclidean Algorithm#^ex-16-2|Example §16.2]]). Solve each step for its remainder:
>
> $$
> 96 = 232 - 136 \times 1,\quad 40 = 136 - 96 \times 1,\quad 16 = 96 - 40 \times 2,\quad 8 = 40 - 16 \times 2 .
> $$
>
> **Method 1 (work up).** Start from the last equation and substitute the earlier ones:
>
> $$
> \begin{aligned}
> 8 &= 40 - 16 \times 2 = 40 - (96 - 40 \times 2) \times 2 = 96 \times (-2) + 40 \times 5\\
> &= 96 \times (-2) + (136 - 96) \times 5 = 136 \times 5 + 96 \times (-7)\\
> &= 136 \times 5 + (232 - 136) \times (-7) = 232 \times (-7) + 136 \times 12 .
> \end{aligned}
> $$
>
> **Method 2 (work down).** Write *every* $a_k$ as $232\, m_k + 136\, n_k$, starting from the two trivial rows. Each new row is the row two above minus $q$ times the row above, where $q$ is the quotient of that step. The same operation is applied to the multipliers, so only they need writing down:
>
> | $a_k$ | $= 232 \times m_k$ | $+\ 136 \times n_k$ | quotient |
> |---|---|---|---|
> | $232$ | $1$ | $0$ | |
> | $136$ | $0$ | $1$ | $(-1)$ |
> | $96$ | $1$ | $-1$ | $(-1)$ |
> | $40$ | $-1$ | $2$ | $(-2)$ |
> | $16$ | $3$ | $-5$ | $(-2)$ |
> | $\mathbf{8}$ | $\mathbf{-7}$ | $\mathbf{12}$ | $(-2)$ |
> | $0$ | | | |
>
> For instance, the row of $40$ is $(0 - 1, \ 1 - (-1)) = (-1, 2)$, and the row of $16$ is $(1 - (-1) \times 2, \ -1 - 2 \times 2) = (3, -5)$. Either way, $8 = 232 \times (-7) + 136 \times 12$. **Always check:** $-1624 + 1632 = 8$. Substituting the values back in is the best proof that they are a solution. Eccles uses Method 2 throughout, since sign slips are less likely.
>
> *Eccles: Example 17.1.3*

^ex-17-1

> [!proof]+ Proof of Theorem §17.1
> **Case $a, b > 0$.** Let $a_0, a_1, \ldots, a_N$ be the sequence of the Euclidean algorithm ([[§16 The Euclidean Algorithm#^thm-16-3|Theorem §16.3]]), so $a_N = \gcd(a, b)$, and for $1 \le k < N$ step $k$ gives $a_{k+1} = a_{k-1} - a_k q_k$. For $1 \le k \le N$ let $P(k)$ be the statement that each of $a_0, a_1, \ldots, a_k$ is an integral linear combination of $a$ and $b$. We prove $P(k)$ by induction on $k$.
> - *Base case.* $a_0 = a = a \times 1 + b \times 0$ and $a_1 = b = a \times 0 + b \times 1$.
> - *Inductive step.* Suppose $P(k)$ for some $1 \le k < N$, so $a_i = a m_i + b n_i$ with $m_i, n_i \in \Z$ for $0 \le i \le k$. Then
>
>   $$
>   a_{k+1} = a_{k-1} - a_k q_k = (a m_{k-1} + b n_{k-1}) - (a m_k + b n_k) q_k = a(m_{k-1} - q_k m_k) + b(n_{k-1} - q_k n_k),
>   $$
>
>   so $P(k+1)$ holds.
>
> By induction $P(N)$ holds; in particular $\gcd(a, b) = a_N$ is an integral linear combination of $a$ and $b$. The multipliers satisfy
>
> $$
> m_0 = 1,\ n_0 = 0,\quad m_1 = 0,\ n_1 = 1,\qquad m_{k+1} = m_{k-1} - q_k m_k,\quad n_{k+1} = n_{k-1} - q_k n_k ,
> $$
>
> which is exactly the table of Method 2.
>
> **One of $a, b$ is zero.** Say $b = 0$, so $a \neq 0$ and $\gcd(a, 0) = |a| = a \times (\pm 1) + 0 \times 0$, with the sign of $a$. The case $a = 0$ is the same.
>
> **General signs.** Since $c \mid x \iff c \mid -x$, $D(a, b) = D(|a|, |b|)$ ([[§16 The Euclidean Algorithm#^def-16-1|Def. §16.1]]), so $\gcd(a, b) = \gcd(|a|, |b|)$. By the first case, $\gcd(|a|, |b|) = |a| m_1 + |b| n_1$ for some integers $m_1, n_1$. Writing $|a| = \varepsilon a$ and $|b| = \delta b$ with $\varepsilon, \delta \in \{1, -1\}$ gives $\gcd(a, b) = a(\varepsilon m_1) + b(\delta n_1)$. (For example, if $a < 0 \le b$: $m = -m_1$, $n = n_1$.)

^pf-17-1

*Uses:* [[§16 The Euclidean Algorithm#^thm-16-3|§16.3]], [[§16 The Euclidean Algorithm#^def-16-1|Def. §16.1]], [[§17 Consequences of the Euclidean Algorithm#^def-17-1|Def. §17.1]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]] (induction)

> [!remark]- Connections
> - The same theorem in group theory: [[§5 A Zoo of Subgroups#^cor-5-2|493 Cor. §5.2]] ([[Bézout's Identity]]). There it is proved with subgroups: $a\Z + b\Z$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $\Z$, hence equal to $e\Z$ for some $e > 0$ ([[§5 A Zoo of Subgroups#^prop-5-1|493 Prop. §5.1]]), and then $e = \gcd(a, b)$. That proof only shows that $m$ and $n$ exist. Eccles's proof is the algorithm itself, so it also computes them. 493 computes them the same way when it needs an actual inverse: [[§8 Invertibility and Unit Groups#^ex-8-3|493 Ex. §8.3]].

> [!remark]- Remark: A Second Proof by Well-Ordering
> Eccles's Problems IV, Q14 gives a proof without the algorithm, which is the subgroup proof of 493 in elementary dress. Let $a, b > 0$ and let $S = \{am + bn \mid m, n \in \Z,\ am + bn > 0\}$. Then $a \in S$, so by the well-ordering principle ([[§5 The Induction Principle#^cor-5-7|Corollary §5.7]]) $S$ has a least element $c = am_0 + bn_0$.
> - *$c \mid a$.* Divide: $a = cq + r$ with $0 \le r < c$ ([[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]). Then $r = a - cq = a(1 - qm_0) + b(-qn_0)$ is an integral linear combination. If $r > 0$ then $r \in S$ and $r < c$, contradicting minimality. So $r = 0$. Likewise $c \mid b$.
> - *$c = \gcd(a,b)$.* By the first point $c \in D(a, b)$, so $c \le \gcd(a, b)$. Conversely $\gcd(a, b)$ divides $a$ and $b$, hence divides $am_0 + bn_0 = c$, so $\gcd(a, b) \le c$.
>
> This proof is shorter but gives no way of finding $m_0, n_0$.
>
> *Eccles: Problems IV, Q14*

^rem-17-1

> [!example] Example §17.2: Writing 68 in Terms of 7684 and 4148
> From [[§16 The Euclidean Algorithm#^ex-16-3|Example §16.3]], $\gcd(7684, 4148) = 68$. Working down (Method 2):
>
> | $a_k$ | $= 7684 \times m_k$ | $+\ 4148 \times n_k$ | quotient |
> |---|---|---|---|
> | $7684$ | $1$ | $0$ | |
> | $4148$ | $0$ | $1$ | $(-1)$ |
> | $3536$ | $1$ | $-1$ | $(-1)$ |
> | $612$ | $-1$ | $2$ | $(-5)$ |
> | $476$ | $6$ | $-11$ | $(-1)$ |
> | $136$ | $-7$ | $13$ | $(-3)$ |
> | $\mathbf{68}$ | $\mathbf{27}$ | $\mathbf{-50}$ | $(-2)$ |
>
> So $68 = 7684 \times 27 + 4148 \times (-50)$, i.e. $m = 27$, $n = -50$. Check: $207468 - 207400 = 68$.
>
> For $68 = 7684m - 4148n$ the same identity gives $m = 27$, $n = 50$. (Eccles prints $7648$ for $7684$ in both exercises; the intended number is $7684$, from Exercise 16.1.)
>
> *Eccles: Exercises 17.1, 17.2*
> *Source: HW7*

^ex-17-2

> [!example] Example §17.3: The Two gcds of Problems IV, Q6
> Carrying the multipliers through the runs of [[§16 The Euclidean Algorithm#^ex-16-3|Example §16.3]]:
>
> | $a_k$ | $= 252\,m_k + 165\,n_k$ | | $a_k$ | $= 4284\,m_k + 3480\,n_k$ |
> |---|---|---|---|---|
> | $87$ | $(1, -1)$ | | $804$ | $(1, -1)$ |
> | $78$ | $(-1, 2)$ | | $264$ | $(-4, 5)$ |
> | $9$ | $(2, -3)$ | | $\mathbf{12}$ | $\mathbf{(13, -16)}$ |
> | $6$ | $(-17, 26)$ | | | |
> | $\mathbf{3}$ | $\mathbf{(19, -29)}$ | | | |
>
> Hence $3 = 19 \times 252 - 29 \times 165$ (check: $4788 - 4785 = 3$) and $12 = 13 \times 4284 - 16 \times 3480$ (check: $55692 - 55680 = 12$).
>
> *Eccles: Problems IV, Q10*
> *Source: HW7*

^ex-17-3

> [!example] Example §17.4: The Multipliers Are Coprime
> Let $a, b > 0$, let $a_0, \ldots, a_N$ be the Euclidean sequence, and let $a_k = a m_k + b n_k$ be the expressions produced by the proof of [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]. Then
>
> $$
> m_k n_{k-1} - m_{k-1} n_k = (-1)^k \qquad (1 \le k \le N),
> $$
>
> and consequently $m_k$ and $n_k$ are coprime.
>
> **Proof.** By induction on $k$. For $k = 1$: $m_1 n_0 - m_0 n_1 = 0 \cdot 0 - 1 \cdot 1 = -1$. Suppose the identity holds for some $1 \le k < N$. Using $m_{k+1} = m_{k-1} - q_k m_k$ and $n_{k+1} = n_{k-1} - q_k n_k$,
>
> $$
> m_{k+1} n_k - m_k n_{k+1} = (m_{k-1} - q_k m_k) n_k - m_k (n_{k-1} - q_k n_k) = m_{k-1} n_k - m_k n_{k-1} = -(-1)^k = (-1)^{k+1}.
> $$
>
> *Coprimality.* If $c$ divides both $m_k$ and $n_k$, then $c$ divides $m_k n_{k-1} - m_{k-1} n_k = \pm 1$, so $c = \pm 1$. Also $m_k, n_k$ are not both zero, since their combination is $\pm 1$. So $\gcd(m_k, n_k) = 1$. For instance, in [[§17 Consequences of the Euclidean Algorithm#^ex-17-1|Example §17.1]] the last row gives $(-7)(-5) - 3 \cdot 12 = -1 = (-1)^5$.
>
> *Eccles: Problems IV, Q11*
> *Source: HW7*
>
> *The HW7 solution proves the identity; the deduction that $m_k$ and $n_k$ are coprime is added here.*

^ex-17-4

## 17.2 An Alternative Definition of the Greatest Common Divisor

> [!remark] Remark: Eccles's Definition and the Usual One
> Eccles's definition ([[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]]) asks that $\gcd(a, b)$ be a positive common divisor satisfying (ii): $c \mid a$ and $c \mid b$ $\Rightarrow$ $c \le d$. The usual definition replaces (ii) by the stronger-looking
>
> (ii)′ $d$ is a multiple of every common divisor: $c \mid a$ and $c \mid b$ $\Rightarrow$ $c \mid d$.
>
> Eccles avoids (ii)′ because it is not obvious from it that a gcd exists, and because (ii) says what the words "greatest common divisor" mean. The two definitions agree, and that is a consequence of [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]].

^rem-17-2

> [!theorem] Corollary §17.2: Common Divisors Divide the gcd
> Let $d = \gcd(a, b)$. Then $c$ is a common divisor of $a$ and $b$ if and only if $c$ divides $d$. That is, $D(a, b) = D(d)$, the set of divisors of $d$.
>
> *Eccles: Corollary 17.2.1*

^cor-17-2

> [!proof]+ Proof
> (*If.*) Suppose $c \mid d$. Since $d \mid a$, transitivity of divisibility ([[§3 Proofs#^ex-3-3|Example §3.3]], Eccles Exercise 3.2) gives $c \mid a$, and likewise $c \mid b$.
>
> (*Only if.*) By [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]], $d = am + bn$ for some $m, n \in \Z$. If $c \mid a$ and $c \mid b$, say $a = cq_1$ and $b = cq_2$, then $d = (cq_1)m + (cq_2)n = c(q_1 m + q_2 n)$, so $c \mid d$.

^pf-17-2

*Uses:* [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]], [[§16 The Euclidean Algorithm#^def-16-1|Def. §16.1]], [[§3 Proofs#^ex-3-3|Ex. §3.3]] (transitivity of "divides")

So $d = \gcd(a, b)$ satisfies (ii)′. Conversely, if a positive common divisor $d'$ satisfies (ii)′, then $d \mid d'$ (as $d$ is a common divisor), so $d \le d'$; and $d' \le d$ by (ii) for $d$. Hence $d' = d$, and the two definitions single out the same number.

> [!example] Example §17.5: Common Divisors of 30 and 72
> $D(30, 72) = \{-6, -3, -2, -1, 1, 2, 3, 6\}$ ([[§11 Properties of Finite Sets#^ex-11-4|Example §11.4]]). This is exactly $D(6)$, the set of divisors of $\gcd(30, 72) = 6$.
>
> *Eccles: Example 17.2.2*

^ex-17-5

> [!example] Example §17.6: The gcd of Three Numbers
> For non-zero integers $a, b, c$ let $\gcd(a, b, c)$ be the greatest element of $D(a, b, c) = \{x \in \Z \mid x \text{ divides } a, b \text{ and } c\}$. Then $\gcd(a, b, c) = \gcd(\gcd(a, b), c)$.
>
> **Proof.** By [[§17 Consequences of the Euclidean Algorithm#^cor-17-2|Corollary §17.2]], $D(a, b) = D(\gcd(a, b))$, so
>
> $$
> D(a, b, c) = D(a, b) \cap D(c) = D(\gcd(a, b)) \cap D(c) = D(\gcd(a, b), c).
> $$
>
> Equal sets have equal greatest elements.
>
> **Numerically.** $\gcd(11033442, 1102246) = 578$ ([[§16 The Euclidean Algorithm#^ex-16-3|Example §16.3]]). Then the algorithm on $(6035, 578)$ gives $6035 = 578 \cdot 10 + 255$, $578 = 255 \cdot 2 + 68$, $255 = 68 \cdot 3 + 51$, $68 = 51 \cdot 1 + 17$, $51 = 17 \cdot 3$. So $\gcd(11033442, 1102246, 6035) = 17$.
>
> *Eccles: Exercise 17.4*

^ex-17-6

## 17.3 Coprime Pairs

Recall ([[§11 Properties of Finite Sets#^def-11-3|Def. §11.3]]): integers $a, b$, not both zero, are **coprime** (relatively prime) when $\gcd(a, b) = 1$, i.e. their only common divisors are $1$ and $-1$.

> [!theorem] Proposition §17.3: Coprime Means 1 Is a Combination
> Two integers $a$ and $b$, not both zero, are coprime if and only if there exist integers $m$ and $n$ such that
>
> $$
> am + bn = 1.
> $$
>
> (Eccles states this for non-zero $a, b$; the proof only needs $\gcd(a,b)$ to be defined.)
>
> *Eccles: Proposition 17.3.1*

^prop-17-3

> [!remark] Remark: Using an Existence Statement
> One direction is a special case of [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]]. In the other direction we *start* from an existence statement, and the way to use one is to take particular elements that satisfy it: integers $m_0, n_0$ with $am_0 + bn_0 = 1$. (One often reuses the letters $m, n$; fresh symbols are clearer here, as recommended in [[§7 Quantifiers#^rem-7-2|the remark on proving ∀ and ∃ in §7]].) Then unpack the goal $\gcd(a, b) = 1$: for every integer $c$, if $c \mid a$ and $c \mid b$ then $c = \pm 1$. The direct method now finishes it by spelling out "divides".

^rem-17-3

> [!proof]+ Proof
> ($\Rightarrow$) If $\gcd(a, b) = 1$, [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|Theorem §17.1]] gives $m, n$ with $am + bn = 1$.
>
> ($\Leftarrow$) Let $m_0, n_0$ be integers with $am_0 + bn_0 = 1$, and let $c$ be a common divisor of $a$ and $b$: $a = cq_1$ and $b = cq_2$ with $q_1, q_2 \in \Z$. Then
>
> $$
> 1 = am_0 + bn_0 = cq_1 m_0 + cq_2 n_0 = c(q_1 m_0 + q_2 n_0),
> $$
>
> so $c \mid 1$, which forces $c = \pm 1$. Thus the only common divisors of $a$ and $b$ are $\pm 1$, and $\gcd(a, b) = 1$.

^pf-17-3

*Uses:* [[§17 Consequences of the Euclidean Algorithm#^thm-17-1|§17.1]]

> [!remark]- Connections
> - Read modulo $n$, $am + nk = 1$ says $am \equiv 1 \pmod n$: [[§8 Invertibility and Unit Groups#^prop-8-1|493 Prop. §8.1]] (a class $[a]$ is [[§21 Congruence Classes and the Arithmetic of Remainders#^def-21-5|invertible]] modulo $n$ iff $\gcd(a, n) = 1$; in these notes [[§21 Congruence Classes and the Arithmetic of Remainders#^cor-21-9|Corollary §21.9]]) is this proposition in that language.

> [!theorem] Theorem §17.4: Coprime Divisor of a Product
> Let $a$, $b$ and $c$ be integers with $a$ and $b$ coprime. Then
>
> $$
> a \mid bc \ \Rightarrow\ a \mid c .
> $$
>
> (Eccles states this for positive integers; the proof uses no signs, and §18 applies it with arbitrary signs.)
>
> *Eccles: Theorem 17.3.2*

^thm-17-4

> [!remark] Remark: Two Clever Steps
> This innocent-looking result is the key to many basic results in number theory, and it is harder than it looks. Unpacking the definitions does not suggest a proof, because the definition of gcd is hard to use directly. **First clever step:** replace "$\gcd(a, b) = 1$" by the logically simpler statement $am_0 + bn_0 = 1$ of [[§17 Consequences of the Euclidean Algorithm#^prop-17-3|Proposition §17.3]]. Now the givens are $am_0 + bn_0 = 1$ and $bc = aq$, and the goal is $c = ak$. **Second clever step:** multiply the first equation by $c$. That is the only way to get $c$ out of the givens with addition and multiplication; division may leave the integers. Then $c = acm_0 + bcn_0 = acm_0 + aqn_0$, and $k = cm_0 + qn_0$ works. As Eccles says, some proofs are just clever, and the steps look natural only in hindsight.

^rem-17-4

> [!proof]+ Proof
> Suppose $a \mid bc$, so $bc = aq$ for some $q \in \Z$. Since $\gcd(a, b) = 1$, [[§17 Consequences of the Euclidean Algorithm#^prop-17-3|Proposition §17.3]] gives integers $m_0, n_0$ with $1 = am_0 + bn_0$. Then
>
> $$
> c = (am_0 + bn_0)c = acm_0 + bcn_0 = acm_0 + aqn_0 = a(cm_0 + qn_0),
> $$
>
> so $a \mid c$.

^pf-17-4

*Uses:* [[§17 Consequences of the Euclidean Algorithm#^prop-17-3|§17.3]]

> [!remark]- Connections
> - Developed further in: [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|493 Lemma §9.1]] ([[Euclid's Lemma]]). It has the same general statement and the same proof from Bézout, with the prime case $p \mid ab \Rightarrow p \mid a$ or $p \mid b$ deduced from it (here [[§23 The Sequence of Prime Numbers#^thm-23-2|Theorem §23.2]]). That case gives unique factorization, here in [[§23 The Sequence of Prime Numbers#^thm-23-5|Theorem §23.5]] and in group theory as [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-2|493 Thm. §9.2]].

> [!example] Example §17.7: Equal Cross-Products of Coprime Pairs
> **Claim.** Let $a_1, a_2, b_1, b_2$ be positive integers with $\gcd(a_1, b_1) = 1$ and $\gcd(a_2, b_2) = 1$. If $a_1 b_2 = a_2 b_1$, then $a_1 = a_2$ and $b_1 = b_2$.
>
> **Proof.** Since $a_2 \mid a_2 b_1 = a_1 b_2 = b_2 a_1$ and $\gcd(a_2, b_2) = 1$, [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]] gives $a_2 \mid a_1$. Symmetrically, $a_1 \mid a_1 b_2 = a_2 b_1 = b_1 a_2$ and $\gcd(a_1, b_1) = 1$ give $a_1 \mid a_2$. For positive integers, $x \mid y$ implies $x \le y$ (as $y = xk$ with $k \ge 1$). So $a_2 \le a_1 \le a_2$, i.e. $a_1 = a_2$. Cancelling $a_1 \neq 0$ in $a_1 b_2 = a_1 b_1$ gives $b_1 = b_2$.
>
> Since $a_1/b_1 = a_2/b_2 \iff a_1 b_2 = a_2 b_1$ ([[§13 Number Systems#^prop-13-1|Proposition §13.1]]), this shows that a positive rational number has only one expression as a fraction in lowest terms ([[§13 Number Systems#^def-13-2|Definition §13.2]]). The same follows for every rational: a negative $q$ has numerator $< 0$ in every lowest-terms fraction, so apply the claim to $-q$; and $0 = 0/b$ is in lowest terms only for $b = \gcd(0, b) = 1$.
>
> *Eccles: Exercise 17.6*
> *Source: HW7*

^ex-17-7
