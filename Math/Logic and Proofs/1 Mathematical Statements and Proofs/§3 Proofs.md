---
type: section
subject: "[[Logic and Proofs]]"
chapter: 1
section: 3
eccles: "Ch. 3"
aliases: ["Eccles 3"]
tags: [logic-and-proofs, mat250]
---
← [[§2 Implications]] · ↑ [[· 1 Mathematical Statements and Proofs]] · [[§4 Proof by Contradiction]] →

*Eccles, Chapter 3 · MAT 250 HW1 (Exercises 3.1, 3.2, 3.5, 3.8).*

A proof of a statement is a logical argument, built from implications, which establishes that it is true. This section introduces the most basic method, the direct proof of an implication, together with proof by cases and the construction of a proof by working backwards from the goal. The examples are inequalities, so the order axioms for the real numbers are stated here; they are the starting point for every inequality in the subject.

## 3.1 Direct Proofs

Since $P \Rightarrow Q$ is automatically true when $P$ is false ([[§2 Implications#^def-2-1|Def. §2.1]]), only the case "$P$ true" needs an argument, and then $P \Rightarrow Q$ is true as long as $Q$ is.

> [!remark] Remark: The Direct Method
> To prove $P \Rightarrow Q$, assume $P$ and deduce $Q$. A **given–goal diagram** (Velleman) records the situation: the direct method moves the hypothesis into the givens and makes the conclusion the new goal. For [[§3 Proofs#^prop-3-1|Proposition §3.1]] below:
>
> | Given | Goal |
> |:--|:--|
> | $a, b$ positive real numbers | $a < b \Rightarrow a^2 < b^2$ |
>
> becomes
>
> | Given | Goal |
> |:--|:--|
> | $a, b$ positive real numbers; $a < b$ | $a^2 < b^2$ |
>
> A finished proof is written as prose, with words like "then", "hence", "it follows" showing how the sentences are related; it should point out where each hypothesis is used, and check that the conditions for each step hold. How much detail to give depends on the reader; while learning it is better to err on the side of pedantry, and to be sceptical: a proof that does not convince its author will convince nobody else.

^rem-3-1

> [!definition] Definition §3.1: The Order Axioms
> For real numbers $a$, $b$, $c$:
> 1. *Trichotomy law.* Exactly one of $a < b$, $a = b$, $a > b$ is true.
> 2. *Addition law.* $a < b \iff a + c < b + c$.
> 3. *Multiplication law.* If $c > 0$ then $a < b \iff ac < bc$; if $c < 0$ then $a < b \iff ac > bc$.
> 4. *Transitive law.* $a < b$ and $b < c$ $\Rightarrow$ $a < c$.
>
> Here $a > b$ means $b < a$; $a \leq b$ means $a < b$ or $a = b$; and $a \geq b$ means $b \leq a$. A number $a$ is **positive** if $a > 0$, **negative** if $a < 0$, **non-negative** if $a \geq 0$ and **non-positive** if $a \leq 0$.
>
> *Eccles: Axioms 3.1.2*

^def-3-1

> [!remark]- Connections
> - The axioms of an ordered field, phrased with $\leq$: [[§3 The Set ℝ of Real Numbers#^def-3-2|451 Def. §3.2]].

> [!theorem] Proposition §3.1: Squares of Positive Numbers
> For positive real numbers $a$ and $b$, $a < b \Rightarrow a^2 < b^2$.
>
> *Eccles: Proposition 3.1.1*

^prop-3-1

> [!proof]+ Proof
> Given positive real numbers $a$ and $b$, suppose that $a < b$. Then $a^2 < ab$ (multiplying through by $a > 0$) and $ab < b^2$ (multiplying through by $b > 0$). Hence $a^2 < b^2$ by the transitive law. It follows that $a < b \Rightarrow a^2 < b^2$.

^pf-3-1

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]]

The proof is a chain $a < b \Rightarrow (a^2 < ab \text{ and } ab < b^2) \Rightarrow a^2 < b^2$. Chaining is justified by the tautology $[(P \Rightarrow Q) \wedge (Q \Rightarrow R)] \Rightarrow (P \Rightarrow R)$ (the *syllogism*), and the conjunction in the middle was obtained by proving the two implications $a < b \Rightarrow a^2 < ab$ and $a < b \Rightarrow ab < b^2$ separately: [[§2 Implications#^prop-2-4|Proposition §2.4]](2) and (5).

### Proof by cases

> [!example] Example §3.1: Proof by Cases
> If $a = 1$ or $a = 2$, then $a^2 - 3a + 2 = 0$.
>
> **Solution.** If $a = 1$ then $a^2 - 3a + 2 = 1 - 3 + 2 = 0$. If $a = 2$ then $a^2 - 3a + 2 = 4 - 6 + 2 = 0$. Hence, if $a = 1$ or $a = 2$, then $a^2 - 3a + 2 = 0$.
>
> An implication $(P \vee Q) \Rightarrow R$ is proved by proving $P \Rightarrow R$ and $Q \Rightarrow R$ ([[§2 Implications#^prop-2-4|Proposition §2.4]](3)). Here the cases are the two values satisfying the hypothesis; more often the cases are infinite families which together are **exhaustive**, as in the proof that $101$ is odd ([[§2 Implications#^prop-2-5|Proposition §2.5]]), where every integer $q$ satisfies $q \leq 50$ or $q \geq 51$.
>
> *Eccles: Example 3.1.3*

^ex-3-1

*Uses:* [[§2 Implications#^prop-2-4|§2.4]]

> [!theorem] Proposition §3.2: Non-Zero Squares Are Positive
> For non-zero real numbers $a$, $a^2 > 0$.
>
> *Eccles: Proposition 3.1.4*

^prop-3-2

> [!proof]+ Proof
> Suppose that $a$ is a non-zero real number. By the trichotomy law (applied to $a$ and $0$), $a > 0$ or $a < 0$. If $a > 0$, multiplying $0 < a$ through by $a > 0$ gives $0 \cdot a < a \cdot a$, i.e. $0 < a^2$, since $0 \cdot a = 0$. If $a < 0$, multiplying $a < 0$ through by $a < 0$ reverses the inequality: $a \cdot a > 0 \cdot a = 0$. In either case $a^2 > 0$. Hence if $a \neq 0$ then $a^2 > 0$.

^pf-3-2

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§2 Implications#^ex-2-13|Ex. §2.13]], [[§2 Implications#^prop-2-4|§2.4]]

The hypothesis "$a > 0$ or $a < 0$" was handled by proving the conclusion in each case separately, and the trichotomy law provided the exhaustive cases.

> [!theorem] Corollary §3.3: Squares, One, and Products of Positive Numbers
> 1. For every real number $a$, $a^2 \geq 0$, with equality only for $a = 0$.
> 2. $1 > 0$.
> 3. If $a > 0$ and $b > 0$, then $ab > 0$.
>
> *Source: standard (used in Exercises 3.1 and 5.3); MAT 200 HW2 Problem 5 (part 3)*

^cor-3-3

> [!proof]+ Proof
> (1) If $a = 0$ then $a^2 = 0$ ([[§2 Implications#^ex-2-13|Ex. §2.13]]); if $a \neq 0$ then $a^2 > 0$ by [[§3 Proofs#^prop-3-2|Proposition §3.2]].
>
> (2) $1 = 1 \times 1 = 1^2$ and $1 \neq 0$ ([[§2 Implications#^def-2-8|Def. §2.8]]), so $1 > 0$ by (1).
>
> (3) Multiplying $0 < b$ through by $a > 0$ gives $a \cdot 0 < ab$, i.e. $0 < ab$.

^pf-3-3

*Uses:* [[§3 Proofs#^prop-3-2|§3.2]], [[§2 Implications#^ex-2-13|Ex. §2.13]], [[§2 Implications#^def-2-8|Def. §2.8]], [[§3 Proofs#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - The same facts for any ordered field, $a^2 \geq 0$ and $0 < 1$: [[§3 The Set ℝ of Real Numbers#^prop-3-1|451 Prop. §3.1]] (d), (e).

## 3.2 Constructing Proofs Backwards

When the goal is more complicated than the givens, it often pays to start from the goal and simplify it, working back towards what is given.

> [!theorem] Proposition §3.4: An Inequality Found Backwards
> For real numbers $a$ and $b$, $a < b \Rightarrow 4ab < (a + b)^2$.
>
> *Eccles: Proposition 3.2.1*

^prop-3-4

> [!proof]+ Proof
> Working backwards from the goal,
>
> $$
> \begin{aligned}
> 4ab < (a+b)^2 \;&\Leftarrow\; 4ab < a^2 + 2ab + b^2 \\
> &\Leftarrow\; 0 < a^2 - 2ab + b^2 \\
> &\Leftarrow\; 0 < (a - b)^2 \\
> &\Leftarrow\; a - b \neq 0 \\
> &\Leftarrow\; a \neq b \\
> &\Leftarrow\; a < b.
> \end{aligned}
> $$
>
> The first and third steps are algebra ($(a+b)^2 = a^2 + 2ab + b^2$ and $(a-b)^2 = a^2 - 2ab + b^2$); the second is the addition law (add $4ab$); the fourth is [[§3 Proofs#^prop-3-2|Proposition §3.2]]; the fifth holds because $a - b = 0$ would give $a = b$ (property 6 of [[§2 Implications#^def-2-8|Def. §2.8]]); and the last is the trichotomy law. Hence $a < b \Rightarrow 4ab < (a + b)^2$. Read forwards, the same chain is the direct proof
> $a < b \Rightarrow a \neq b \Rightarrow a - b \neq 0 \Rightarrow 0 < (a-b)^2 \Rightarrow 0 < a^2 - 2ab + b^2 \Rightarrow 4ab < a^2 + 2ab + b^2 \Rightarrow 4ab < (a+b)^2$.

^pf-3-4

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§3 Proofs#^prop-3-2|§3.2]], [[§2 Implications#^def-2-8|Def. §2.8]], [[§2 Implications#^prop-2-4|§2.4]]

> [!remark] Remark: The Direction of the Implications
> In a backwards construction the implications must point from the given towards the goal, as shown. Here every step except the last also holds in the other direction, but that is irrelevant to the proof. It does answer a further question: since $4ab < (a+b)^2 \iff a \neq b$, the condition $a < b$ is sufficient but not necessary for $4ab < (a+b)^2$ (take $a = 2$, $b = 1$: $8 < 9$), and the necessary and sufficient condition is $a \neq b$. The backwards presentation shows how the proof was found; the forwards one hides it.
>
> *Eccles: Exercise 3.7*

^rem-3-2

## Exercises from the Homework

> [!example] Example §3.2: An Identity and an Inequality in Three Variables
> Prove that for all real numbers $a$, $b$, $c$:
> (i) $(a + b - c)^2 = (a + b)^2 + (a - c)^2 + (b - c)^2 - a^2 - b^2 - c^2$;
> (ii) $bc + ac + ab \leq a^2 + b^2 + c^2$.
>
> **Solution.** (i) Multiplying out, the left side is $a^2 + b^2 + c^2 + 2ab - 2ac - 2bc$, and the right side is
>
> $$
> (a^2 + 2ab + b^2) + (a^2 - 2ac + c^2) + (b^2 - 2bc + c^2) - a^2 - b^2 - c^2 = a^2 + b^2 + c^2 + 2ab - 2ac - 2bc .
> $$
>
> (ii) Each of $(a - b)^2$, $(a - c)^2$, $(b - c)^2$ is $\geq 0$ ([[§3 Proofs#^cor-3-3|Corollary §3.3]]), and a sum of non-negative numbers is non-negative (if $x \geq 0$ and $y \geq 0$ then $x + y \geq 0 + y = y \geq 0$, by the addition and transitive laws). So
>
> $$
> 0 \leq (a - b)^2 + (a - c)^2 + (b - c)^2 = 2\bigl(a^2 + b^2 + c^2 - ab - ac - bc\bigr).
> $$
>
> Hence $x = a^2 + b^2 + c^2 - ab - ac - bc \geq 0$: multiplying by $\tfrac12$, or noting that if $x < 0$ then $2x = x + x < 0 + 0 = 0$ by the addition and transitive laws. Adding $ab + ac + bc$ to both sides gives $bc + ac + ab \leq a^2 + b^2 + c^2$.
>
> *Source: HW1*
> *Eccles: Exercise 3.1*

^ex-3-2

*Uses:* [[§3 Proofs#^cor-3-3|§3.3]], [[§3 Proofs#^def-3-1|Def. §3.1]], [[§2 Implications#^def-2-8|Def. §2.8]]

> [!example] Example §3.3: Divisibility Is Transitive; Squares of Even Integers
> (a) For all integers $a$, $b$, $c$: ($a \mid b$ and $b \mid c$) $\Rightarrow a \mid c$.
> (b) The square of an even integer is even.
>
> **Solution.** (a) Suppose $a \mid b$ and $b \mid c$. By [[§2 Implications#^def-2-6|Def. §2.6]], $b = aq$ for some integer $q$ and $c = bp$ for some integer $p$ (a different letter, since there is no reason for the two integers to be equal). Then $c = bp = (aq)p = a(qp)$, and $qp$ is an integer, so $a \mid c$.
>
> (b) If $a$ is even then $2 \mid a$; also $a \mid a^2$ since $a^2 = a \cdot a$. By (a), $2 \mid a^2$, so $a^2$ is even. (Directly: $a = 2q$ gives $a^2 = 2(2q^2)$.)
>
> *Source: HW1 (part (a))*
> *Eccles: Exercises 3.2 and 3.3*

^ex-3-3

*Uses:* [[§2 Implications#^def-2-6|Def. §2.6]], [[§2 Implications#^def-2-7|Def. §2.7]]

> [!example] Example §3.4: Multiplying a Weak Inequality
> If $a$, $b$, $c$ are real numbers with $a > 0$, then $b \geq c \Rightarrow ab \geq ac$.
>
> **Solution.** The hypothesis $b \geq c$ means $b > c$ or $b = c$, so we treat the two cases ([[§2 Implications#^prop-2-4|Proposition §2.4]](3)). If $b > c$, the multiplication law with $a > 0$ gives $ab > ac$, hence $ab \geq ac$. If $b = c$, then $ab = ac$, hence $ab \geq ac$. In both cases $ab \geq ac$.
>
> To *prove* an "or" statement such as $ab \geq ac$, it suffices to prove one of its parts; to *use* one, each part must separately lead to the conclusion.
>
> *Source: HW1*
> *Eccles: Exercise 3.5*

^ex-3-4

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§2 Implications#^prop-2-4|§2.4]]

> [!example] Example §3.5: Comparing Squares and Absolute Values
> Prove that for all real numbers $a$ and $b$:
> (i) $0 \leq a < b \Rightarrow a^2 < b^2$; (ii) $|a| < |b| \Rightarrow a^2 < b^2$; (iii) $|a| = |b| \Rightarrow a^2 = b^2$; (iv) $|a| \leq |b| \Rightarrow a^2 \leq b^2$.
>
> **Solution.** (i) Suppose $0 \leq a < b$; then $a = 0$ or $a > 0$. If $a > 0$, then $b > 0$ by transitivity, and $a^2 < b^2$ by [[§3 Proofs#^prop-3-1|Proposition §3.1]]. If $a = 0$, then $b > 0$, so $b^2 > 0 = a^2$ ([[§3 Proofs#^prop-3-2|Proposition §3.2]]).
>
> (ii) Since $|a| \geq 0$ ([[§1 The Language of Mathematics#^def-1-4|Def. §1.4]]), $|a| < |b|$ gives $0 \leq |a| < |b|$, so $|a|^2 < |b|^2$ by (i). As $|a|^2 = a^2$ and $|b|^2 = b^2$ ([[§1 The Language of Mathematics#^ex-1-3|Ex. §1.3]]), $a^2 < b^2$.
>
> (iii) If $|a| = |b|$ then $a^2 = |a|^2 = |b|^2 = b^2$.
>
> (iv) $|a| \leq |b|$ means $|a| < |b|$ or $|a| = |b|$; by (ii) and (iii), $a^2 < b^2$ or $a^2 = b^2$, i.e. $a^2 \leq b^2$.
>
> *Source: HW1*
> *Eccles: Exercise 3.8*
>
> *In (ii) the HW1 solution has the cases of $|a|$ interchanged ($|a| = -a$ for $a > 0$, $|a| = a$ for $a < 0$); since $(-a)^2 = a^2$, its conclusion $|a|^2 = a^2$ is unaffected.*

^ex-3-5

*Uses:* [[§3 Proofs#^prop-3-1|§3.1]], [[§3 Proofs#^prop-3-2|§3.2]], [[§3 Proofs#^def-3-1|Def. §3.1]], [[§1 The Language of Mathematics#^def-1-4|Def. §1.4]], [[§1 The Language of Mathematics#^ex-1-3|Ex. §1.3]]

The converses of (ii)–(iv) also hold; they are proved through the contrapositive in [[§4 Proof by Contradiction#^ex-4-5|Ex. §4.5]].
