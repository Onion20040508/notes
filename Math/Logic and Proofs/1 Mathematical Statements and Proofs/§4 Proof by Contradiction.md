---
type: section
subject: "[[Logic and Proofs]]"
chapter: 1
section: 4
eccles: "Ch. 4"
aliases: ["Eccles 4"]
tags: [logic-and-proofs, mat250]
---
← [[§3 Proofs]] · ↑ [[· 1 Mathematical Statements and Proofs]] · [[§5 The Induction Principle]] →

*Eccles, Chapter 4 (and Problems I Q7, Q9) · MAT 250 HW1 (Exercises 4.2, 4.4, 4.5, 4.7) · MAT 250 HW2 (Problems I Q10, Q11).*

The direct method is awkward for negative statements, such as non-existence results, and for some implications. Proof by contradiction assumes that what we want to prove is false and derives a statement known to be false. This section justifies the method by a truth table, gives a template for writing it out, and treats two close relatives: proof by contrapositive, and the standard way of proving an "or" statement.

## 4.1 Proving Negative Statements by Contradiction

> [!definition] Definition §4.1: Contradiction
> A **contradiction** is a statement of the form "$P$ and (not $P$)", $P \wedge \neg P$. It is always false ([[§1 The Language of Mathematics#^thm-1-2|Theorem §1.2]]). For an integer $a$, "$a$ is even and $a$ is odd" is a contradiction, since "odd" means "not even".
>
> *Eccles: Section 4.1*

^def-4-1

> [!theorem] Proposition §4.1: A Non-Existence Result
> There do not exist integers $m$ and $n$ such that $14m + 20n = 101$.
>
> *Eccles: Proposition 4.1.1*

^prop-4-1

> [!proof]+ Proof
> Suppose, for contradiction, that $m$ and $n$ are integers with $14m + 20n = 101$. Since $14$ and $20$ are even, $101 = 14m + 20n = 2(7m + 10n)$ with $7m + 10n$ an integer, so $101$ is even. But $101$ is odd ([[§2 Implications#^prop-2-5|Proposition §2.5]]): a contradiction. Hence such integers $m$ and $n$ cannot exist.

^pf-4-1

*Uses:* [[§2 Implications#^def-2-6|Def. §2.6]], [[§2 Implications#^def-2-7|Def. §2.7]], [[§2 Implications#^prop-2-5|§2.5]]

We cannot check all pairs $(m, n)$ one at a time. Instead we showed that the negation of the goal leads to something known to be false: "When you have eliminated the impossible, whatever remains, however improbable, must be the truth" (Sherlock Holmes).

> [!theorem] Theorem §4.2: Proof by Contradiction Is Valid
> Let $P$ and $Q$ be statements. If $\neg P \Rightarrow Q$ is true and $Q$ is false, then $P$ is true. In particular, if $\neg P$ implies a contradiction $R \wedge \neg R$, then $P$ is true.
>
> *Eccles: Section 4.1*

^thm-4-2

> [!proof]+ Proof
> The truth table:
>
> | $P$ | $\neg P$ | $Q$ | $\neg P \Rightarrow Q$ |
> |:-:|:-:|:-:|:-:|
> | T | F | T | T |
> | T | F | F | T |
> | F | T | T | T |
> | F | T | F | F |
>
> The only row in which $\neg P \Rightarrow Q$ is true and $Q$ is false is the second, and there $P$ is true. A contradiction $R \wedge \neg R$ is false ([[§1 The Language of Mathematics#^thm-1-2|Theorem §1.2]]), so it may serve as $Q$.

^pf-4-2

*Uses:* [[§2 Implications#^def-2-1|Def. §2.1]], [[§1 The Language of Mathematics#^thm-1-2|§1.2]]

> [!remark] Remark: A Template for Proofs by Contradiction
> To prove a statement $P$ by contradiction, write:
>
> *Proof.* Suppose, for contradiction, that $P$ is false. Then [argument leading to a contradiction]. Hence our assumption that $P$ is false must be false. Thus $P$ is true, as required. $\square$
>
> The phrase "for contradiction" tells the reader which method is in use. A common failing is to leave unclear exactly what the contradiction is: state both of the contradictory statements.

^rem-4-1

> [!example] Example §4.1: 101 Is Odd, by Contradiction
> Since "odd" means "not even", [[§2 Implications#^prop-2-5|Proposition §2.5]] is also a non-existence statement: there is no integer $q$ with $2q = 101$. Division at school (2 into 101 goes 50 times, remainder 1) suggests a contradiction.
>
> **Solution.** Suppose, for contradiction, that $101 = 2q$ for some integer $q$. Then $1 = 101 - 100 = 2q - 2 \times 50 = 2(q - 50)$. If $q - 50 \leq 0$ then $2(q - 50) \leq 0 < 1$; so $q - 50$ is a positive integer, hence $q - 50 \geq 1$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]) and $1 = 2(q - 50) \geq 2$. This contradicts $1 < 2$. Hence $101$ is not even, so it is odd.
>
> *Eccles: Section 4.1*

^ex-4-1

*Uses:* [[§2 Implications#^def-2-6|Def. §2.6]], [[§2 Implications#^def-2-7|Def. §2.7]], [[§3 Proofs#^def-3-1|Def. §3.1]], [[§3 Proofs#^cor-3-3|§3.3]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]

## 4.2 Proving Implications by Contradiction

If $P \Rightarrow Q$ is false then $P$ is true and $Q$ is false ([[§2 Implications#^prop-2-1|Proposition §2.1]]). So $P \Rightarrow Q$ can be proved by showing that $P$ and $\neg Q$ together lead to a contradiction: add $\neg Q$ to the givens and make "a contradiction" the goal.

> [!theorem] Proposition §4.3: Cancelling a Factor in an Inequality
> If $a$, $b$, $c$ are integers with $a > b$, then $ac \leq bc \Rightarrow c \leq 0$.
>
> *Eccles: Proposition 4.2.1*

^prop-4-3

> [!proof]+ Proof
> For integers $a > b$, suppose that $ac \leq bc$ but, for contradiction, that $c > 0$. Then the multiplication law applied to $a > b$ gives $ac > bc$, contradicting $ac \leq bc$ (trichotomy). Hence the assumption $c > 0$ is false, i.e. $c \leq 0$. Thus $ac \leq bc \Rightarrow c \leq 0$.

^pf-4-3

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]

A direct proof is hard to find here, because the multiplication law depends on the sign of $c$, which is what we are trying to determine. (The same argument works for real $a$, $b$, $c$.)

## 4.3 Proof by Contrapositive

> [!remark] Remark: Proof by Contrapositive
> In the proof of [[§4 Proof by Contradiction#^prop-4-3|Proposition §4.3]] the contradiction involved the hypothesis $ac \leq bc$. Such proofs are better seen as proofs of the **contrapositive** $\neg Q \Rightarrow \neg P$, which is equivalent to $P \Rightarrow Q$ ([[§2 Implications#^prop-2-2|Proposition §2.2]]). In Proposition §4.3, $P$ is $ac \leq bc$ and $Q$ is $c \leq 0$, so $\neg P$ is $ac > bc$, $\neg Q$ is $c > 0$, and the contrapositive reads
>
> $$
> c > 0 \Rightarrow ac > bc \qquad (a, b, c \text{ integers with } a > b).
> $$
>
> *Second proof of Proposition §4.3.* The contrapositive of $ac \leq bc \Rightarrow c \leq 0$ is $c > 0 \Rightarrow ac > bc$, which is the multiplication law since $a > b$. Thus the proposition is true. $\square$

^rem-4-2

## 4.4 Proving "Or" Statements

To prove $P \Rightarrow (Q \vee R)$, assume $P$ and $\neg Q$, and deduce $R$: the two forms are equivalent ([[§2 Implications#^prop-2-4|Proposition §2.4]](4)), and the extra assumption $\neg Q$ gives more to work with.

> [!theorem] Proposition §4.4: Zero Products
> For real numbers $a$ and $b$, $ab = 0 \iff (a = 0 \text{ or } b = 0)$.
>
> *Eccles: Proposition 4.4.1*

^prop-4-4

> [!proof]+ Proof
> "$\Leftarrow$": $0 \times b = 0 = a \times 0$ ([[§2 Implications#^ex-2-13|Ex. §2.13]]), so if $a = 0$ or $b = 0$ then $ab = 0$.
>
> "$\Rightarrow$": Suppose that $ab = 0$. To see that $a = 0$ or $b = 0$, suppose that $a \neq 0$. Then we may divide by $a$: $b = a^{-1}(ab) = a^{-1} \times 0 = 0$. Hence $ab = 0 \Rightarrow (a = 0 \text{ or } b = 0)$.

^pf-4-4

*Uses:* [[§2 Implications#^ex-2-13|Ex. §2.13]], [[§2 Implications#^def-2-8|Def. §2.8]], [[§2 Implications#^prop-2-4|§2.4]]

> [!theorem] Proposition §4.5: Signs of a Product
> For real numbers $a$ and $b$:
> 1. $ab > 0$ if and only if $a$ and $b$ have the same sign: ($a > 0$ and $b > 0$) or ($a < 0$ and $b < 0$).
> 2. $ab < 0$ if and only if $a$ and $b$ have opposite signs: ($a > 0$ and $b < 0$) or ($a < 0$ and $b > 0$).
>
> *Eccles: Propositions 4.4.2 and 4.4.3*

^prop-4-5

> [!proof]+ Proof
> By trichotomy each of $a$, $b$ is negative, zero or positive, giving nine exhaustive cases, and in each the sign of $ab$ is determined:
>
> | | $a < 0$ | $a = 0$ | $a > 0$ |
> |:-:|:-:|:-:|:-:|
> | $b < 0$ | $ab > 0$ | $ab = 0$ | $ab < 0$ |
> | $b = 0$ | $ab = 0$ | $ab = 0$ | $ab = 0$ |
> | $b > 0$ | $ab < 0$ | $ab = 0$ | $ab > 0$ |
>
> The zero entries are [[§4 Proof by Contradiction#^prop-4-4|Proposition §4.4]]. The others come from the multiplication law: if $a > 0$, multiplying $b > 0$ or $b < 0$ by $a$ gives $ab > a \cdot 0 = 0$ or $ab < 0$; if $a < 0$, multiplying by $a$ reverses the inequality, giving $ab < 0$ for $b > 0$ and $ab > 0$ for $b < 0$.
>
> The right-to-left implications of (1) and (2) are read off from the table. For left to right we argue by contradiction: if $a$ and $b$ do not have the same sign, the table shows $ab = 0$ or $ab < 0$, so by trichotomy $ab > 0$ is false; similarly if they do not have opposite signs then $ab \geq 0$.

^pf-4-5

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§4 Proof by Contradiction#^prop-4-4|§4.4]], [[§2 Implications#^ex-2-13|Ex. §2.13]]

Proposition §4.4 is what we use to solve polynomial equations, and Proposition §4.5 to solve polynomial inequalities ([[§6 The Language of Set Theory#^ex-6-10|Ex. §6.10]]).

## Exercises from the Homework

> [!example] Example §4.2: Parity of Squares
> For every integer $n$: (a) $n^2$ odd $\Rightarrow$ $n$ odd; (b) $n^2$ even $\Rightarrow$ $n$ even.
>
> **Solution.** (a) Suppose that $n^2$ is odd and, for contradiction, that $n$ is even, say $n = 2q$. Then $n^2 = 4q^2 = 2(2q^2)$ with $2q^2$ an integer, so $n^2$ is even, contradicting the fact that $n^2$ is odd (odd means not even). Hence $n$ is odd. Alternatively, the contrapositive "$n$ even $\Rightarrow$ $n^2$ even" is [[§3 Proofs#^ex-3-3|Ex. §3.3]](b).
>
> (b) Suppose that $n^2$ is even, say $n^2 = 2b$, and, for contradiction, that $n$ is odd. Then $n \neq 0$, since $0 = 2 \times 0$ is even. If $n > 0$, then $n^2 + n$ is even ([[§5 The Induction Principle#^prop-5-2|Proposition §5.2]]), say $n^2 + n = 2a$, and so $n = (n^2 + n) - n^2 = 2(a - b)$ is even. If $n < 0$, then $m = -n$ is a positive integer with $m^2 = n^2$ even, so $m = 2c$ for an integer $c$ by the case just treated, and $n = 2(-c)$ is even. In every case $n$ is even, contradicting the assumption that $n$ is odd. Hence $n$ is even.
>
> *Source: HW1 (part (a))*
> *Eccles: Exercises 4.2 and 4.3; Problems I Q7*

^ex-4-2

*Uses:* [[§2 Implications#^def-2-6|Def. §2.6]], [[§2 Implications#^def-2-7|Def. §2.7]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]], [[§3 Proofs#^ex-3-3|Ex. §3.3]], [[§5 The Induction Principle#^prop-5-2|§5.2]]

Eccles's hint to Problems I Q7 instead assumes that the odd integers are exactly those of the form $2q + 1$, which is proved only later ([[§11 Properties of Finite Sets#^prop-11-11|Proposition §11.11]]); with that fact, (b) is the contrapositive of "$n = 2q + 1 \Rightarrow n^2 = 2p + 1$" ([[§7 Quantifiers#^ex-7-4|Ex. §7.4]]). The proof of (b) above needs only [[§5 The Induction Principle#^prop-5-2|Proposition §5.2]].

> [!example] Example §4.3: Proving an "Or" Conclusion
> If $a$ is a real number with $a^2 \geq 7a$, then $a \leq 0$ or $a \geq 7$.
>
> **Solution.** Suppose $a^2 \geq 7a$ and that $a \leq 0$ is false, i.e. $a > 0$; we show $a \geq 7$ ([[§2 Implications#^prop-2-4|Proposition §2.4]](4)). If, for contradiction, $a < 7$, then multiplying by $a > 0$ gives $a^2 < 7a$, contradicting $a^2 \geq 7a$. Hence $a \geq 7$. (Equivalently: divide $a^2 \geq 7a$ by $a > 0$.)
>
> *Source: HW1*
> *Eccles: Exercise 4.4*

^ex-4-3

*Uses:* [[§2 Implications#^prop-2-4|§2.4]], [[§3 Proofs#^def-3-1|Def. §3.1]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]

> [!example] Example §4.4: Antisymmetry of the Order
> For real numbers $a$ and $b$, ($a \leq b$ and $b \leq a$) $\Rightarrow a = b$.
>
> **Solution.** Suppose $a \leq b$ and $b \leq a$ and, for contradiction, $a \neq b$. By trichotomy, $a < b$ or $a > b$. If $a < b$, then by trichotomy neither $b < a$ nor $b = a$ holds, contradicting $b \leq a$. If $a > b$, then neither $a < b$ nor $a = b$ holds, contradicting $a \leq b$. Either way we have a contradiction, so $a = b$.
>
> *Source: HW1*
> *Eccles: Exercise 4.5*

^ex-4-4

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]

> [!example] Example §4.5: The Triangle Inequality
> For all real numbers $a$ and $b$, $|a + b| \leq |a| + |b|$, with equality if and only if $ab \geq 0$, i.e. if and only if $a, b \geq 0$ or $a, b \leq 0$.
>
> **Solution.** *Step 1 (comparing squares).* For all real $u$, $v$:
>
> $$
> |u| \leq |v| \iff u^2 \leq v^2, \qquad |u| < |v| \iff u^2 < v^2, \qquad |u| = |v| \iff u^2 = v^2 .
> $$
>
> The implications "$\Rightarrow$" are [[§3 Proofs#^ex-3-5|Ex. §3.5]]. For "$\Leftarrow$" take contrapositives of the same results with $u$ and $v$ interchanged: $|u| > |v| \Rightarrow u^2 > v^2$ gives $u^2 \leq v^2 \Rightarrow |u| \leq |v|$ (trichotomy), and $|u| \geq |v| \Rightarrow u^2 \geq v^2$ gives $u^2 < v^2 \Rightarrow |u| < |v|$. Finally $u^2 = v^2$ gives $|u| \leq |v|$ and $|v| \leq |u|$, so $|u| = |v|$ ([[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]]).
>
> *Step 2 ($|a||b| = |ab|$).* $|a||b| \geq 0$, so $\bigl||a||b|\bigr| = |a||b|$; and $(|a||b|)^2 = |a|^2|b|^2 = a^2 b^2 = (ab)^2$ ([[§1 The Language of Mathematics#^ex-1-3|Ex. §1.3]]). By Step 1, $|a||b| = |ab|$.
>
> *Step 3 (the inequality).* Suppose, for contradiction, that $|a + b| > |a| + |b|$. As $|a| + |b| \geq 0$, Step 1 gives $(a + b)^2 > (|a| + |b|)^2$, that is $a^2 + 2ab + b^2 > a^2 + 2|a||b| + b^2$, and so $ab > |a||b| = |ab|$. But $ab \leq |ab|$ always: if $ab \geq 0$ they are equal, and if $ab < 0$ then $ab < 0 \leq |ab|$. This contradiction proves $|a + b| \leq |a| + |b|$.
>
> *Step 4 (equality).* By Step 1 and the same expansion,
>
> $$
> |a + b| = |a| + |b| \iff (a + b)^2 = (|a| + |b|)^2 \iff 2ab = 2|ab| \iff ab = |ab| \iff ab \geq 0,
> $$
>
> since $|x| = x$ exactly when $x \geq 0$. By [[§4 Proof by Contradiction#^prop-4-5|Proposition §4.5]](2), $ab \geq 0$ means that $a$ and $b$ do not have opposite signs: $a, b \geq 0$ or $a, b \leq 0$.
>
> *Source: HW1*
> *Eccles: Exercises 4.6 and 4.7*
>
> *The HW1 solution states the equality condition ($a, b \geq 0$ or $a, b \leq 0$) without proof; Step 4 supplies it.*

^ex-4-5

*Uses:* [[§3 Proofs#^ex-3-5|Ex. §3.5]], [[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]], [[§1 The Language of Mathematics#^ex-1-3|Ex. §1.3]], [[§1 The Language of Mathematics#^def-1-4|Def. §1.4]], [[§2 Implications#^prop-2-2|§2.2]], [[§4 Proof by Contradiction#^prop-4-5|§4.5]]

> [!remark]- Connections
> - The triangle inequality and $|ab| = |a||b|$ in analysis, proved there by adding $-|a| \leq a \leq |a|$ and $-|b| \leq b \leq |b|$: [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 Thm. §3.3]].
> - Generalized to inner product spaces: [[Triangle inequality|LADR 6.17]].

> [!example] Example §4.6: The Largest Integer
> (a) There is no largest integer. (b) What is wrong with the following proof that $1$ is the largest integer, and what does it prove?
>
> *Let $n$ be the largest integer. Then, since $1$ is an integer, $1 \leq n$. On the other hand, since $n^2$ is also an integer, $n^2 \leq n$, from which it follows that $n \leq 1$. Thus, since $1 \leq n$ and $n \leq 1$, $n = 1$. Thus $1$ is the largest integer.*
>
> **Solution.** (a) Suppose, for contradiction, that there is a largest integer $n$. Then $n + 1$ is an integer, and $n + 1 > n$ since $1 > 0$ ([[§3 Proofs#^cor-3-3|Corollary §3.3]]). This contradicts the choice of $n$.
>
> (b) Every step is valid *given* that $n$ is the largest integer: $1 \leq n$ and $n^2 \leq n$ hold because $1$ and $n^2$ are integers; if $n > 1$ then $n \cdot n > 1 \cdot n = n$ (multiplying by $n > 0$), contradicting $n^2 \leq n$, so $n \leq 1$; and then $n = 1$ by antisymmetry. What the argument proves is the implication *if there is a largest integer, then it is $1$*. By (a) its hypothesis is false, so the implication is vacuously true ([[§2 Implications#^rem-2-1|Remark (vacuous truth)]]) and says nothing about $1$, which is indeed not the largest integer ($2 > 1$). The error is the opening assumption that a largest integer exists.
>
> *Source: HW2 (part (b))*
> *Eccles: Problems I Q9 and Q10*
>
> *The HW2 solution locates the error in the step $n^2 \leq n$; that step is valid under the assumption that $n$ is the largest integer, and the flaw is the assumption itself, which is false by (a).*

^ex-4-6

*Uses:* [[§3 Proofs#^cor-3-3|§3.3]], [[§3 Proofs#^def-3-1|Def. §3.1]], [[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]], [[§2 Implications#^rem-2-1|Remark (vacuous truth)]]

> [!example] Example §4.7: No Smallest Positive Real Number
> There does not exist a smallest positive real number.
>
> **Solution.** Suppose, for contradiction, that $r$ is the smallest positive real number. Then $r/2$ is a real number, and it is positive: if $r/2 \leq 0$ then $r = r/2 + r/2 \leq 0$. Moreover $r - r/2 = r/2 > 0$, so $r/2 < r$ (addition law). Thus $r/2$ is a positive real number smaller than $r$, contradicting the choice of $r$. Hence no smallest positive real number exists.
>
> By contrast $1$ is the smallest positive integer ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]); that every non-empty set of positive integers has a least element is the well-ordering principle ([[§5 The Induction Principle#^cor-5-7|Corollary §5.7]]).
>
> *Source: HW2*
> *Eccles: Problems I Q11*
>
> *The HW2 solution proves that there is no smallest real number, using $n - 1 < n$; for the positive reals $r - 1$ need not be positive, so $r/2$ is used instead.*

^ex-4-7

*Uses:* [[§3 Proofs#^def-3-1|Def. §3.1]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]
