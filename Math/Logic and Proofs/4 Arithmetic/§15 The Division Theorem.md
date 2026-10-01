---
type: section
subject: "[[Logic and Proofs]]"
chapter: 4
section: 15
eccles: "Ch. 15"
aliases: ["Eccles 15"]
tags: [logic-and-proofs, mat250]
---
← [[§14 Counting Infinite Sets]] · ↑ [[· 4 Arithmetic]] · [[§16 The Euclidean Algorithm]] →

*Eccles, Chapter 15 · MAT 250 HW6 (Exercises 15.1–15.5).*

Arithmetic begins with division with remainder: every integer $a$ is $bq + r$ with $0 \le r < b$, and $q$, $r$ are unique. This generalizes the odd/even dichotomy of [[§11 Properties of Finite Sets#^prop-11-11|Proposition §11.11]] (the case $b = 2$), and its proof is a model of an existence-and-uniqueness argument. The uniqueness half is what makes the theorem useful: it turns a negative statement such as "$3 \nmid a$" into a positive one, "$a = 3q + 1$ or $a = 3q + 2$", on which we can compute.

## 15.1 The Division Theorem

> [!theorem] Theorem §15.1: The Division Theorem
> Let $a$ and $b$ be integers with $b > 0$. Then there are **unique** integers $q$ and $r$ such that
>
> $$
> a = bq + r \qquad\text{and}\qquad 0 \le r < b.
> $$
>
> *Eccles: Theorem 15.1.1*

^thm-15-1

> [!definition] Definition §15.1: Quotient and Remainder
> In [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]], $q$ is the **quotient** and $r$ the **remainder** on dividing $a$ by $b$. Since $r = a - bq$, the condition $0 \le r < b$ says $bq \le a < b(q+1)$: the quotient is the greatest integer $\le a/b$.
>
> *Eccles: Section 15.1*

^def-15-1

> [!remark] Remark: Constructing the Proof
> There are two separate claims: **existence** of $q, r$ and **uniqueness**. (Students often forget the second; it is the half used most.) Since $q$ determines $r = a - bq$, existence asks only for an integer $q$ with $bq \le a < b(q+1)$. For $a \ge 0$ we *define* $q$ as the maximum of the finite set $A = \{k \in \Z \mid k \ge 0 \text{ and } bk \le a\}$. Then $bq \le a$ because $q \in A$. The other inequality, $b(q+1) > a$, says exactly that $q + 1 \notin A$, which is what maximality gives. Negative $a$ is reduced to $-a$, as for $b = 2$ in [[§11 Properties of Finite Sets#^prop-11-11|Proposition §11.11]]. For uniqueness: two remainders differ by a multiple of $b$, and two numbers in $\{0, \ldots, b-1\}$ are less than $b$ apart, so the multiple is $0$.

^rem-15-1

> [!proof]+ Proof
> **Existence for $a \ge 0$.** Let $A = \{k \in \Z \mid k \ge 0 \text{ and } bk \le a\}$. Then $0 \in A$, since $b \cdot 0 = 0 \le a$. And $A$ is finite: if $k \in A$ then $k \le bk \le a$ (as $k \ge 0$ and $b \ge 1$), so $A \subseteq \{0, 1, \ldots, a\}$. A finite non-empty set of integers has a maximum element ([[§11 Properties of Finite Sets#^prop-11-9|Proposition §11.9]]); let $q = \max A$ and $r = a - bq$, so $a = bq + r$.
>
> Since $q \in A$, $bq \le a$, i.e. $r \ge 0$. Suppose, for contradiction, that $r \ge b$. Then $b(q+1) = bq + b \le bq + r = a$ and $q + 1 \ge 0$, so $q + 1 \in A$. But $q + 1 > q = \max A$, a contradiction. Hence $0 \le r < b$.
>
> **Existence for $a < 0$.** Then $-a > 0$, so by the first case $-a = bq_1 + r_1$ with $0 \le r_1 < b$, i.e. $a = b(-q_1) - r_1$.
> - If $r_1 = 0$, then $a = b(-q_1) + 0$: take $q = -q_1$, $r = 0$.
> - If $0 < r_1 < b$, then $a = b(-q_1 - 1) + (b - r_1)$ with $0 < b - r_1 < b$: take $q = -q_1 - 1$, $r = b - r_1$.
>
> **Uniqueness.** Suppose $a = bq_1 + r_1 = bq_2 + r_2$ with $0 \le r_1, r_2 < b$. Without loss of generality $q_1 \ge q_2$ (otherwise swap the labels). Then
>
> $$
> r_2 - r_1 = (a - bq_2) - (a - bq_1) = b(q_1 - q_2) \ge 0,
> $$
>
> and $r_2 - r_1 \le r_2 < b$. So $0 \le b(q_1 - q_2) < b$, and dividing by $b > 0$ gives $0 \le q_1 - q_2 < 1$. Since $q_1 - q_2$ is an integer, $q_1 = q_2$, and then $r_1 = a - bq_1 = a - bq_2 = r_2$.

^pf-15-1

*Uses:* [[§11 Properties of Finite Sets#^prop-11-9|§11.9]], proof by contradiction ([[§4 Proof by Contradiction|§4]])

> [!remark]- Connections
> - Same result, with existence proved by well-ordering (the route of Eccles's footnote): [[§6 Divisibility and Congruence#^lem-6-1|493 Lemma §6.1]] (the Division Algorithm), where $r$ is also written $a \bmod n$ ([[§6 Divisibility and Congruence#^def-6-2|493 Def. §6.2]]).
> - It is the only tool used to classify the subgroups of $\Z$: [[§5 A Zoo of Subgroups#^prop-5-1|493 Prop. §5.1]].

> [!remark]- Remark: Other Routes to Existence
> Eccles's footnote: drop the condition $k \ge 0$ and use $A' = \{k \in \Z \mid bk \le a\}$ for every $a$. This set is infinite, since it contains all large negative integers, but it is non-empty and bounded above by $|a|$, so it still has a maximum. Getting that maximum needs the well-ordering principle ([[§11 Properties of Finite Sets#^ex-11-3|Example §11.3]](c)) rather than the finite-set fact. Eccles keeps to finite sets, and in practice one handles $a < 0$ through $-a$ anyway, as in Example §15.1 below.

^rem-15-2

> [!example] Example §15.1: Quotient and Remainder by Calculator
> In practice $q$ is the greatest integer $\le a/b$, read off a calculator, and then $r = a - bq$.
> - $a = 1781293$, $b = 1481$: $a/b \approx 1202.76$, so $q = 1202$ and $r = 1781293 - 1481 \times 1202 = 1131$.
> - $a = -7856123$, $b = 9812$: $a/b \approx -800.66$, so $q = -801$. Rounding *down* increases the absolute value of a negative number. Then $r = -7856123 + 9812 \times 801 = 3289$.
>
> These check particular cases. They cannot prove the theorem: computing the decimal expansion of $a/b$ itself uses the division theorem repeatedly (Eccles Exercise 15.6), so the argument would be circular.
>
> *Eccles: Examples 15.1.2, 15.1.3*

^ex-15-1

> [!example] Example §15.2: Ten Divisions
> Write $a = bq + r$ with $0 \le r < b$.
>
> | | $a$ | $b$ | $q$ | $r$ | check |
> |---|---|---|---|---|---|
> | (i) | $100$ | $3$ | $33$ | $1$ | $3 \cdot 33 + 1 = 100$ |
> | (ii) | $3$ | $100$ | $0$ | $3$ | $100 \cdot 0 + 3 = 3$ |
> | (iii) | $100$ | $7$ | $14$ | $2$ | $7 \cdot 14 + 2 = 100$ |
> | (iv) | $-100$ | $7$ | $-15$ | $5$ | $7 \cdot (-15) + 5 = -100$ |
> | (v) | $-105$ | $7$ | $-15$ | $0$ | $7 \cdot (-15) = -105$ |
> | (vi) | $-3$ | $105$ | $-1$ | $102$ | $105 \cdot (-1) + 102 = -3$ |
> | (vii) | $7684$ | $4148$ | $1$ | $3536$ | $4148 + 3536 = 7684$ |
> | (viii) | $-7684$ | $4148$ | $-2$ | $612$ | $-8296 + 612 = -7684$ |
> | (ix) | $1234567$ | $1357$ | $909$ | $1054$ | $1233513 + 1054 = 1234567$ |
> | (x) | $0$ | $17$ | $0$ | $0$ | $17 \cdot 0 + 0 = 0$ |
>
> For negative $a$ the quotient is *not* the truncation of $a/b$ toward $0$. In (iv), $-100/7 \approx -14.3$ but $q = -15$, because $q = -14$ would leave $-100 - 7(-14) = -2 < 0$.
>
> *Eccles: Exercise 15.1*
> *Source: HW6*

^ex-15-2

![[m250-15-1.svg]]
*Case (iv) on the number line. The multiples $7q$ (blue) cut $\Z$ into blocks $[7q, 7(q+1))$, and every integer lies in exactly one block: that is existence and uniqueness in one picture. $a = -100$ lies in the block starting at $7 \cdot (-15) = -105$, so $q = -15$ and $r = 5$ (green). Rounding toward $0$ instead (gray) gives $-14$ and a "remainder" of $-2$, which is not allowed.*

## 15.2 Some Applications

The uniqueness half of the theorem is used through the following corollary.

> [!theorem] Corollary §15.2: Divisibility and the Remainder
> Let $a$ and $b$ be integers with $b > 0$, and suppose $a = bq + r$ with $q, r \in \Z$ and $0 \le r < b$. Then $b$ divides $a$ if and only if $r = 0$. Equivalently, $b$ does not divide $a$ if and only if $r > 0$.
>
> *Eccles: Corollary 15.2.2*

^cor-15-2

> [!proof]+ Proof
> If $r = 0$ then $a = bq$, so $b \mid a$. Conversely, if $b \mid a$ then $a = bq'$ for some $q' \in \Z$, i.e. $a = bq' + 0$ with $0 \le 0 < b$. This is a second expression of the required form, so by the uniqueness part of [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]], $r = 0$ (and $q = q'$).

^pf-15-2

*Uses:* [[§15 The Division Theorem#^thm-15-1|§15.1]]

> [!remark] Remark: Turning a Negative into a Positive
> To prove "$3 \mid a^2 \Rightarrow 3 \mid a$" directly we would write $a^2 = 3q$ and get stuck, since $a = 3(q/a)$ needs $a \mid q$, which is no easier. Getting back from $a^2$ to $a$ is the hard direction, so argue by contradiction: assume $3 \nmid a$. The division theorem with [[§15 The Division Theorem#^cor-15-2|Corollary §15.2]] turns this negative statement into a positive one, $a = 3q + 1$ or $a = 3q + 2$, and we can compute with that. This *case split on the remainder* is the basic technique of the chapter.

^rem-15-3

> [!theorem] Proposition §15.3: Divisibility by 3 of a Square
> Let $a$ be an integer. Then $a^2$ is divisible by $3$ if and only if $a$ is divisible by $3$.
>
> *Eccles: Proposition 15.2.1*

^prop-15-3

> [!proof]+ Proof
> ($\Leftarrow$) If $a = 3q$ then $a^2 = 9q^2 = 3(3q^2)$ is divisible by $3$.
>
> ($\Rightarrow$) Suppose $3 \mid a^2$ and, for contradiction, $3 \nmid a$. By [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]] $a = 3q + r$ with $r \in \{0, 1, 2\}$, and $r \neq 0$ by [[§15 The Division Theorem#^cor-15-2|Corollary §15.2]]. So $a = 3q + 1$ or $a = 3q + 2$, and
>
> $$
> (3q+1)^2 = 9q^2 + 6q + 1 = 3(3q^2 + 2q) + 1, \qquad (3q+2)^2 = 9q^2 + 12q + 4 = 3(3q^2 + 4q + 1) + 1.
> $$
>
> In either case $a^2 = 3q' + 1$ with $0 \le 1 < 3$, so by [[§15 The Division Theorem#^cor-15-2|Corollary §15.2]] $3 \nmid a^2$, a contradiction.

^pf-15-3

*Uses:* [[§15 The Division Theorem#^thm-15-1|§15.1]], [[§15 The Division Theorem#^cor-15-2|§15.2]]

> [!remark]- Connections
> - This is the fact asserted without proof in Eccles Exercise 13.1 (no rational number has square $3$; see [[§13 Number Systems|§13]]). The general version for every prime, $p \mid a^2 \Rightarrow p \mid a$, is the case $a = b$ of [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^lem-9-1|493 Lemma §9.1]] (Euclid's lemma), proved here as [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Theorem §17.4]].
> - Developed further in: [[§2 The Set ℚ of Rational Numbers#^prop-2-2|451 Prop. §2.2]] ($\sqrt m$ is rational only for perfect squares $m$).

The proof shows more than was asked: for every integer $a$, the remainder of $a^2$ on division by $3$ is $0$ or $1$, never $2$. That gives a quick test for non-squares.

> [!theorem] Proposition §15.4: Squares Modulo 3
> If $n \in \Z^+$ is a perfect square (the square of an integer), then $n = 3q$ or $n = 3q + 1$ for some $q \in \Z$.
>
> *Eccles: Proposition 15.2.3*

^prop-15-4

> [!proof]+ Proof
> Let $n = a^2$ with $a \in \Z$. By [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]], $a = 3q_0$, $3q_0 + 1$ or $3q_0 + 2$ for some $q_0 \in \Z$. Hence
>
> $$
> a^2 = 3(3q_0^2), \qquad a^2 = 3(3q_0^2 + 2q_0) + 1, \qquad\text{or}\qquad a^2 = 3(3q_0^2 + 4q_0 + 1) + 1,
> $$
>
> so $n = 3q$ or $n = 3q + 1$ for some $q \in \Z$.

^pf-15-4

*Uses:* [[§15 The Division Theorem#^thm-15-1|§15.1]]

> [!example] Example §15.3: A Repunit That Is Not a Square
> $11111111111 = 3 \times 3703703703 + 2$, so its remainder on division by $3$ is $2$. If it were a perfect square, [[§15 The Division Theorem#^prop-15-4|Proposition §15.4]] would give a second division by $3$ with remainder $0$ or $1$, contradicting uniqueness in [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]. So $11111111111$ is not the square of an integer.
>
> *Eccles: Example 15.2.4*

^ex-15-3

> [!example] Example §15.4: Divisibility by 5 of a Square
> **Claim.** For $a \in \Z$: $5 \mid a$ if and only if $5 \mid a^2$.
>
> ($\Rightarrow$) If $a = 5q$ then $a^2 = 25q^2 = 5(5q^2)$ is divisible by $5$.
>
> ($\Leftarrow$) Suppose $5 \mid a^2$ and, for contradiction, $5 \nmid a$. By [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]] and [[§15 The Division Theorem#^cor-15-2|Corollary §15.2]], $a = 5p + r$ with $r \in \{1, 2, 3, 4\}$. Then
>
> $$
> a^2 = 25p^2 + 10pr + r^2 = 5(5p^2 + 2pr) + r^2, \qquad r^2 \in \{1, 4, 9, 16\}.
> $$
>
> Since $5 \mid a^2$, $5$ divides $a^2 - 5(5p^2 + 2pr) = r^2$. But none of $1, 4, 9, 16$ is divisible by $5$. This contradiction shows $5 \mid a$.
>
> (Eccles's version reduces each case to the form $5q' + s$ with $0 < s < 5$: the remainders of $a^2$ are $1, 4, 4, 1$.)
>
> *Eccles: Exercise 15.2 (= Problems IV, Q2)*
> *Source: HW6*

^ex-15-4

> [!example] Example §15.5: Divisibility of a Square by 3 and by 9
> **Claim.** For $a \in \Z$: $3 \mid a^2$ if and only if $9 \mid a^2$.
>
> ($\Rightarrow$) If $3 \mid a^2$ then $3 \mid a$ by [[§15 The Division Theorem#^prop-15-3|Proposition §15.3]], so $a = 3q$ and $a^2 = 9q^2$ is divisible by $9$.
>
> ($\Leftarrow$) If $a^2 = 9q$ then $a^2 = 3(3q)$ is divisible by $3$.
>
> *Eccles: Exercise 15.3*
> *Source: HW6*

^ex-15-5

> [!example] Example §15.6: 98765432 Is Not a Square
> **Bracketing.** $9938^2 = 98763844$ and $9939^2 = 98783721$, so $9938^2 < 98765432 < 9939^2$. Suppose $a^2 = 98765432$ with $a \in \Z$. If $|a| \le 9938$ then $a^2 = |a|^2 \le 9938^2$. If $|a| \ge 9939$ then $a^2 \ge 9939^2$. Both are false, so $9938 < |a| < 9939$, and there is no integer strictly between two consecutive integers. Hence $98765432$ is not a square.
>
> **By remainders.** Alternatively, $98765432 = 3 \times 32921810 + 2$ has remainder $2$ on division by $3$, so [[§15 The Division Theorem#^prop-15-4|Proposition §15.4]] rules it out at once, as in [[§15 The Division Theorem#^ex-15-3|Example §15.3]].
>
> *Eccles: Exercise 15.4*
> *Source: HW6*

^ex-15-6

> [!example] Example §15.7: Squares Modulo 4
> **Claim.** If $n$ is a perfect square then $n = 4q$ or $n = 4q + 1$ for some $q \in \Z$. Hence $1234567$ is not a perfect square.
>
> Let $n = a^2$. By [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]], $a = 4q_0 + r$ with $r \in \{0, 1, 2, 3\}$, and
>
> $$
> \begin{aligned}
> (4q_0)^2 &= 4(4q_0^2), & (4q_0+1)^2 &= 4(4q_0^2 + 2q_0) + 1,\\
> (4q_0+2)^2 &= 4(4q_0^2 + 4q_0 + 1), & (4q_0+3)^2 &= 4(4q_0^2 + 6q_0 + 2) + 1.
> \end{aligned}
> $$
>
> So $n = 4q$ or $n = 4q + 1$. (Eccles's shorter route splits only into $a$ even or odd: $(2q_0)^2 = 4q_0^2$ and $(2q_0+1)^2 = 4(q_0^2 + q_0) + 1$.)
>
> Now $1234567 = 4 \times 308641 + 3$, so its remainder on division by $4$ is $3$. A square has remainder $0$ or $1$, and by uniqueness in [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]] the remainder is determined by the number. So $1234567$ is not a perfect square.
>
> *The HW6 solution stops after the first part; the deduction about $1234567$ is added here.*
>
> *Eccles: Exercise 15.5*
> *Source: HW6*

^ex-15-7
