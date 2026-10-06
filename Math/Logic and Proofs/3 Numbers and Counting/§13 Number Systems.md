---
type: section
subject: "[[Logic and Proofs]]"
chapter: 3
section: 13
eccles: "Ch. 13"
aliases: ["Eccles 13"]
tags: [logic-and-proofs, mat250]
---
← [[§12★ Counting Functions and Subsets]] · ↑ [[· 3 Numbers and Counting]] · [[§14 Counting Infinite Sets]] →

*Eccles, Chapter 13 · MAT 250 HW4 (Exercises 13.1, 13.2, 13.5).*

Numbers arose for counting, which needs only the positive integers; subtraction brings in $0$ and the negative integers, division the rational numbers, and measuring lengths the real numbers. This section describes the rational numbers through fractions and checks that their arithmetic is well defined, proves the classical theorem that no rational number has square $2$, and introduces real numbers as infinite decimals, showing that $0.999\ldots = 1$ and that recurring decimals are rational. The construction of $\Q$ from $\Z$ is postponed to [[§22 Partitions and Equivalence Relations|§22]], where the language of equivalence relations is available.

> [!remark]- Remark: A Little History
> The Babylonians used sexagesimal (base $60$) fractions before 1800 B.C.; they survive in degrees, minutes and seconds. The Pythagoreans held that any two lengths are commensurable, so that every ratio of lengths is a ratio $m/n$ of positive integers. Around 400 B.C. they found that the diagonal and the side of a square are incommensurable: by Pythagoras's theorem the diagonal of a unit square has square $2$, and Theorem [[§13 Number Systems#^thm-13-4|§13.4]] below says no rational number has square $2$. Eudoxus's theory of proportion (Euclid, *Elements* Book V) separated "number" (positive integer) from "magnitude" (length); the two were reunited only in the nineteenth century, by Dedekind and others.

^rem-13-1

## 13.1 The Rational Numbers

The integers can be added, subtracted and multiplied, but not always divided: for integers $b \ne 0$ and $a$, the equation $bx = a$ has an integer solution only if $b \mid a$. The rational numbers satisfy all the basic algebraic properties of the integers ([[§2 Implications#^def-2-9|Definition §2.9]], Eccles Properties 2.3.1) and in addition: for integers $b \ne 0$ and $a$ there is a unique rational $q$ with $bq = a$; and they are just enough for this, since for every rational $q$ there are integers $b \ne 0$ and $a$ with $bq = a$. For now we take such a system as given and describe it through fractions; its construction from $\Z$ is in §22a ([[§22a Constructing ℚ and ℤ#^def-22a-2|Definition §22a.2]] and [[§22a Constructing ℚ and ℤ#^thm-22a-4|Theorem §22a.4]]; Eccles Example 22.3.5 and the Rational Number Project). A rational number and a fraction are different things: every rational number is represented by a fraction, but different fractions may represent the same rational number.

> [!definition] Definition §13.2: Fraction
> A **fraction** is an expression $a/b$ with $a, b \in \Z$ and $b \ne 0$; $a$ is its **numerator** and $b$ its **denominator**.
>
> *Eccles: Definition 13.1.1*

^def-13-1

> [!definition] Definition §13.3: The Rational Number a Fraction Represents
> The fraction $a/b$ **represents** the **rational number** $q$ with $bq = a$. As a temporary notation, write $q = \langle a/b \rangle$.
>
> *Eccles: Definition 13.1.1*

^def-13-2

Since $1x = a$ has the integer solution $a$, the integers sit inside the rationals: $a = \langle a/1 \rangle$.

> [!theorem] Proposition §13.1: When Two Fractions Are Equal
> Two fractions $a_1/b_1$ and $a_2/b_2$ represent the same rational number, $\langle a_1/b_1 \rangle = \langle a_2/b_2 \rangle$, if and only if $a_1 b_2 = a_2 b_1$.
>
> *Eccles: Proposition 13.1.2*

^prop-13-1

> [!proof]+ Proof
> Let $q_1 = \langle a_1/b_1 \rangle$ and $q_2 = \langle a_2/b_2 \rangle$, so $b_1 q_1 = a_1$ and $b_2 q_2 = a_2$. Multiplying by the non-zero numbers $b_2$, respectively $b_1$, and cancelling (commutativity, associativity, cancellation of non-zero factors),
>
> $$
> b_1 q_1 = a_1 \iff b_1 b_2 q_1 = a_1 b_2, \qquad b_2 q_2 = a_2 \iff b_1 b_2 q_2 = a_2 b_1.
> $$
>
> Hence $q_1 = q_2 \iff b_1 b_2 q_1 = b_1 b_2 q_2 \iff a_1 b_2 = a_2 b_1$.

^pf-13-1

*Uses:* [[§13 Number Systems#^def-13-1|Def. §13.1]], [[§13 Number Systems#^def-13-2|Def. §13.2]]

For example $\langle 2/3 \rangle = \langle 8/12 \rangle = \langle (-14)/(-21) \rangle$.

> [!definition] Definition §13.4: Lowest Terms
> The fraction $a/b$ is **in lowest terms** when $b$ is positive and $a$ and $b$ are coprime.
>
> *Eccles: Definition 13.1.3*

^def-13-3

> [!theorem] Proposition §13.2: Every Rational Number Has a Lowest-Terms Fraction
> Every rational number is represented by a fraction in lowest terms.
>
> *Eccles: Section 13.1 (text before Definition 13.1.3)*

^prop-13-2

> [!proof]+ Proof
> Let $q = \langle a/b \rangle$. Multiplying numerator and denominator by $-1$ if necessary (allowed by Proposition [[§13 Number Systems#^prop-13-1|§13.1]], since $(-a)b = a(-b)$), we may take $b > 0$. If $a = 0$ then $q = \langle 0/1 \rangle$ and $\gcd(0, 1) = 1$. Otherwise let $d = \gcd(a, b) > 0$; then $a/d$ and $b/d$ are coprime integers (Proposition [[§11 Properties of Finite Sets#^prop-11-10|§11.10]]), $b/d > 0$, and $\langle (a/d)/(b/d) \rangle = \langle a/b \rangle$ because $(a/d)\, b = a\, (b/d)$.

^pf-13-2

*Uses:* [[§13 Number Systems#^prop-13-1|§13.1]], [[§11 Properties of Finite Sets#^prop-11-10|§11.10]], [[§13 Number Systems#^def-13-3|Def. §13.3]]

The lowest-terms fraction is in fact unique; this needs [[§17 Consequences of the Euclidean Algorithm#^thm-17-4|Euclid's lemma]] and is proved later, in [[§17 Consequences of the Euclidean Algorithm#^ex-17-7|Example §17.7]] (Eccles Exercise 17.6). Nothing before §17 uses the uniqueness.

To see how sums look in terms of fractions, let $q_1 = \langle a/b \rangle$ and $q_2 = \langle c/d \rangle$, so $bq_1 = a$ and $dq_2 = c$. Then $bdq_1 = ad$ and $bdq_2 = bc$, so by distributivity $bd(q_1 + q_2) = ad + bc$: $q_1 + q_2$ is represented by $(ad + bc)/bd$. Similarly $bd\,q_1 q_2 = ac$, so $q_1 q_2$ is represented by $ac/bd$.

> [!definition] Definition §13.5: Sum and Product of Fractions
> $$
> \frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd}.
> $$
>
> *Eccles: Definition 13.1.4*

^def-13-4

Whenever an object has several expressions and an operation is defined using an expression, one must check that different expressions of the same object give the same answer: that the operation is **well defined**.

> [!theorem] Proposition §13.3: Arithmetic of Fractions Is Well Defined
> Addition and multiplication of rational numbers are well defined by the formulas of Definition [[§13 Number Systems#^def-13-4|§13.4]]: if $\langle a_1/b_1 \rangle = \langle a_2/b_2 \rangle$ and $\langle c_1/d_1 \rangle = \langle c_2/d_2 \rangle$, then
>
> $$
> \Bigl\langle \frac{a_1}{b_1} + \frac{c_1}{d_1} \Bigr\rangle = \Bigl\langle \frac{a_2}{b_2} + \frac{c_2}{d_2} \Bigr\rangle \quad \text{and} \quad \Bigl\langle \frac{a_1}{b_1} \times \frac{c_1}{d_1} \Bigr\rangle = \Bigl\langle \frac{a_2}{b_2} \times \frac{c_2}{d_2} \Bigr\rangle.
> $$
>
> *Eccles: Proposition 13.1.5*

^prop-13-3

> [!proof]+ Proof
> By Proposition [[§13 Number Systems#^prop-13-1|§13.1]] the hypotheses say $a_1 b_2 = a_2 b_1$ and $c_1 d_2 = c_2 d_1$, and the goals are $(a_1 d_1 + b_1 c_1)\, b_2 d_2 = (a_2 d_2 + b_2 c_2)\, b_1 d_1$ and $a_1 c_1\, b_2 d_2 = a_2 c_2\, b_1 d_1$. For the sum,
>
> $$
> (a_1 d_1 + b_1 c_1) b_2 d_2 = (a_1 b_2) d_1 d_2 + b_1 b_2 (c_1 d_2) = (a_2 b_1) d_1 d_2 + b_1 b_2 (c_2 d_1) = (a_2 d_2 + b_2 c_2) b_1 d_1 .
> $$
>
> For the product, $(a_1 c_1)(b_2 d_2) = (a_1 b_2)(c_1 d_2) = (a_2 b_1)(c_2 d_1) = (a_2 c_2)(b_1 d_1)$.

^pf-13-3

*Uses:* [[§13 Number Systems#^prop-13-1|§13.1]], [[§13 Number Systems#^def-13-4|Def. §13.4]]

The multiplication is consistent with Definition [[§13 Number Systems#^def-13-2|§13.2]]: if $q = \langle a/b \rangle$ then $bq = \langle b/1 \times a/b \rangle = \langle ab/b \rangle = \langle a/1 \rangle = a$. From now on we drop $\langle \ \rangle$ and write $a/b$ for the rational number it represents, so $a_1/b_1 = a_2/b_2 \iff a_1 b_2 = a_2 b_1$; the set of rational numbers is $\Q$. Subtraction and division by non-zero elements are always possible in $\Q$:

$$
\frac{a}{b} - \frac{c}{d} = \frac{a}{b} + \frac{-c}{d}, \qquad \frac{a}{b} \Big/ \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} \quad (c \ne 0).
$$

> [!remark]- Connections
> - Developed further in: [[§22a Constructing ℚ and ℤ#^def-22a-2|Def. §22a.2]] constructs $\Q$ as the set of classes of pairs $(a, b)$, $b \ne 0$, under $(a, b) \sim (c, d) \iff ad = bc$, the relation of Proposition [[§13 Number Systems#^prop-13-1|§13.1]]; the operations are well defined by [[§22a Constructing ℚ and ℤ#^prop-22a-3|§22a.3]] and $\Q$ is a field by [[§22a Constructing ℚ and ℤ#^thm-22a-4|§22a.4]].
> - "Well defined" as a general notion: [[§7 The Group ℤ∕nℤ#^def-7-2|493 Def. §7.2]]; $\Q$ is a field, [[§2 The Set ℚ of Rational Numbers#^def-2-4|451 Def. §2.4]].

## 13.2 The Irrationality of √2

A good number system should measure every length. By Pythagoras's theorem the diagonal of a unit square has length $\sqrt2$, a number whose square is $2$. There is no such rational number.

> [!remark] Remark: Constructing the Proof
> Every non-zero rational is $a/b$ with $a, b$ non-zero integers, so the claim is: there are no $a, b \in \Z - \{0\}$ with $2 = (a/b)^2$. A statement that something does *not* exist is hard to prove directly, which suggests contradiction: assume $a, b \in \Z - \{0\}$ with $a^2 = 2b^2$ and aim for a contradiction. So the theorem is really about integer solutions of $m^2 = 2n^2$, and the tool for showing an equation has no integer solutions is divisibility. From $a^2 = 2b^2$, $a^2$ is even, so $a$ is even, $a = 2a_1$; then $4a_1^2 = 2b^2$, $b^2 = 2a_1^2$, so $b$ is even too. That alone is no contradiction, but it would be if $a/b$ had been in lowest terms. So go back and insist on $\gcd(a, b) = 1$ from the start.

^rem-13-2

> [!theorem] Theorem §13.4: √2 Is Irrational
> There is no rational number whose square is $2$.
>
> *Eccles: Theorem 13.2.1*

^thm-13-4

> [!proof]+ Proof
> First, *if $a^2$ is even then $a$ is even* ([[§4 Proof by Contradiction#^ex-4-2|Example §4.2]]; Eccles Problems I Q7): if $a$ is odd then $a = 2q + 1$ ([[§11 Properties of Finite Sets#^prop-11-11|Proposition §11.11]]), and $a^2 = 2(2q^2 + 2q) + 1$ is odd, by the same proposition.
>
> Suppose for contradiction that $q \in \Q$ with $q^2 = 2$. Write $q = a/b$ in lowest terms (Proposition [[§13 Number Systems#^prop-13-2|§13.2]]), so $\gcd(a, b) = 1$. Then
>
> $$
> q^2 = 2 \Rightarrow \frac{a^2}{b^2} = 2 \Rightarrow a^2 = 2b^2 \Rightarrow a^2 \text{ is even} \Rightarrow a \text{ is even} \Rightarrow a = 2a_1 \text{ for some } a_1 \in \Z.
> $$
>
> But then $4a_1^2 = 2b^2$, so $b^2 = 2a_1^2$ is even and $b$ is even. So $2$ divides both $a$ and $b$, and $\gcd(a, b) \ge 2$, contradicting $\gcd(a, b) = 1$. Hence no rational number has square $2$.

^pf-13-4

*Uses:* [[§13 Number Systems#^prop-13-2|§13.2]], [[§11 Properties of Finite Sets#^prop-11-11|§11.11]], [[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]], [[§4 Proof by Contradiction#^ex-4-2|Ex. §4.2]]

> [!remark]- Connections
> - The same theorem in 451: [[§2 The Set ℚ of Rational Numbers#^thm-2-1|451 Thm. §2.1]]; its generalization to all non-square integers, [[§2 The Set ℚ of Rational Numbers#^prop-2-2|451 Prop. §2.2]], is proved there with unique factorization (here [[§23 The Sequence of Prime Numbers#^thm-23-5|Theorem §23.5]]; the irrationality of √2 by factorization is [[§23 The Sequence of Prime Numbers#^ex-23-6|Ex. §23.6]]).

> [!example] Example §13.1: √3 Is Irrational
> There is no rational number whose square is $3$. (As Eccles's exercise allows, assume that $3 \mid a^2$ if and only if $3 \mid a$; this is proved later, from the division theorem, as [[§15 The Division Theorem#^prop-15-3|Proposition §15.3]] (Eccles Proposition 15.2.1), whose proof does not use this section.)
>
> Suppose $x \in \Q$ with $x^2 = 3$, and write $x = p/q$ in lowest terms, $\gcd(p, q) = 1$. Then $p^2 = 3q^2$, so $3 \mid p^2$ and hence $3 \mid p$: $p = 3a$ with $a \in \Z$. Substituting, $9a^2 = 3q^2$, so $q^2 = 3a^2$ and as before $3 \mid q$. Then $3$ is a common divisor of $p$ and $q$, contradicting $\gcd(p, q) = 1$. So no such $x$ exists.
>
> *Eccles: Exercise 13.1*
> *Source: HW4*

^ex-13-1

*Uses:* [[§13 Number Systems#^prop-13-2|§13.2]], [[§15 The Division Theorem#^prop-15-3|§15.3]]

> [!example] Example §13.2: Where the Argument Fails for 4
> Mimic the proof for $4$: $q = a/b$ in lowest terms and $q^2 = 4$ give $a^2 = 4b^2$, so $4 \mid a^2$. But it does not follow that $4 \mid a$ ($a = 2$); all one gets is $2 \mid a$, $a = 2a_1$, and then $4a_1^2 = 4b^2$, i.e. $a_1^2 = b^2$, which says nothing about the parity of $b$. No contradiction arises, as there should not be: $2 = 2/1$ has square $4$. The step that matters in Theorem [[§13 Number Systems#^thm-13-4|§13.4]] is "$2 \mid a^2 \Rightarrow 2 \mid a$" together with the factor $2$ (not $4$) on the right.
>
> *Eccles: Exercise 13.3*

^ex-13-2

## 13.3 Real Numbers and Infinite Decimals

Theorem [[§13 Number Systems#^thm-13-4|§13.4]] shows that rational numbers do not measure all lengths. The **real numbers** extend the number system so that they do.

> [!definition] Definition §13.6: Irrational Number
> A real number which is not a rational number is **irrational**. Theorem [[§13 Number Systems#^thm-13-4|§13.4]] says: $\sqrt2$ is irrational.
>
> *Eccles: Section 13.3*

^def-13-5

Defining the real numbers needs the theory of limits and belongs to analysis. Here real numbers are described by **infinite decimals**: every non-negative real number is represented by an infinite decimal

$$
a_0 . a_1 a_2 \ldots a_i \ldots, \qquad a_0 \in \N, \quad a_i \in \{0, 1, \ldots, 9\} \text{ for } i \ge 1,
$$

and every infinite decimal represents a real number. A **finite decimal** $a_0.a_1 \ldots a_n$ (all later digits $0$) is a rational number:

$$
a_0.a_1 a_2 \ldots a_n = a_0 + \frac{a_1}{10} + \frac{a_2}{100} + \cdots + \frac{a_n}{10^n} = \frac{a_0 10^n + a_1 10^{n-1} + \cdots + a_n}{10^n}.
$$

The idea of an infinite decimal is that its truncations are better and better approximations.

> [!example] Example §13.3: The Decimal Expansion of √2
> The digits of the positive number whose square is $2$ are found one at a time, using that for non-negative reals $a < b \iff a^2 < b^2$ ([[§4 Proof by Contradiction#^ex-4-5|Example §4.5]], Step 1; Eccles Exercise 4.6).
> - Step 0: the largest integer whose square is less than $2$ is $1$, since $1^2 < 2 < 2^2$; so $1 < \sqrt2 < 2$ and $a_0 = 1$.
> - Step 1: square $1.0, 1.1, \ldots, 1.9$ and take the largest with square below $2$ (equality is impossible, $2$ not being a rational square): $(14/10)^2 = 196/100 < 2 < (15/10)^2 = 225/100$, so $1.4 < \sqrt2 < 1.5$ and $a_1 = 4$.
> - Step 2: $(141/100)^2 = 19881/10000 < 2 < (142/100)^2 = 20164/10000$, so $a_2 = 1$.
>
> Continuing gives $1.41421356237309504880\ldots$, with no apparent pattern. At step $n$ we have a finite decimal with $(a_0.a_1\ldots a_n)^2 < 2 < (a_0.a_1 \ldots a_n + 10^{-n})^2$, that is,
>
> $$
> a_0.a_1 \ldots a_n < \sqrt2 < a_0.a_1 \ldots a_n + \frac{1}{10^n}.
> $$
>
> For example $1.4142135^2 = 1.99999982358225 < 2 < 1.4142136^2 = 2.00000010642496$.
>
> *Eccles: Example 13.3.1*

^ex-13-3

> [!definition] Definition §13.7: The Real Number an Infinite Decimal Represents
> An infinite decimal $a_0.a_1 a_2 \ldots a_i \ldots$ **represents** the real number $a$, written $a = a_0.a_1a_2 \ldots a_i \ldots$, when
>
> $$
> a_0.a_1 a_2 \ldots a_n \ \le\ a\ \le\ a_0.a_1 a_2 \ldots a_n + \frac{1}{10^n} \qquad \text{for each } n \in \Z^+.
> $$
>
> *Eccles: Definition 13.3.2*

^def-13-6

The inequalities are $\le$, not $<$, so that rational numbers such as finite decimals are represented too. That every infinite decimal represents *some* real number is one form of the completeness axiom for $\R$. That it represents only one is a consequence of the Archimedean property.

> [!theorem] Proposition §13.5: An Infinite Decimal Represents at Most One Number
> If an infinite decimal represents both $a$ and $a'$, then $a = a'$.
>
> *Eccles: Section 13.3 (text after Definition 13.3.2)*

^prop-13-5

> [!proof]+ Proof
> Both $a$ and $a'$ lie in the interval $[a_0.a_1\ldots a_n,\ a_0.a_1 \ldots a_n + 10^{-n}]$, so $|a - a'| \le 10^{-n}$ for every $n \in \Z^+$. Suppose $a \ne a'$. By the Archimedean property there is an integer $n > 1/|a - a'|$, which we may take positive. Since $10^n > n$ (induction: $10 > 1$, and $10^{k+1} = 10 \cdot 10^k > 10k \ge k + 1$), we get $10^{-n} < 1/n < |a - a'|$, a contradiction. So $a = a'$. In other words, decimals representing distinct numbers $a \ne a'$ differ by the $n$th decimal place for such an $n$.

^pf-13-5

*Uses:* [[§13 Number Systems#^def-13-6|Def. §13.6]], [[§4 The Completeness Axiom#^thm-4-5|451 Thm. §4.5]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

> [!remark]- Connections
> - The two facts used about $\R$: the [[Completeness Axiom]] ([[§4 The Completeness Axiom#^def-4-4|451 Def. §4.4]]) and the [[Archimedean Property]] ([[§4 The Completeness Axiom#^thm-4-5|451 Thm. §4.5]]), which 451 derives from completeness. A construction of $\R$ from $\Q$: [[§6 Dedekind Cuts#^def-6-1|451 Def. §6.1]] (Dedekind cuts); ★ by classes of rational Cauchy sequences, [[§6★ ℝ from Cauchy Sequences of Rationals|451 §6★]], where this section's decimal expansion of √2 reappears as a Cauchy sequence ([[§6★ ℝ from Cauchy Sequences of Rationals#^ex-6s-2|451 Ex. §6★.2]]).

> [!example] Example §13.4: 0.999… = 1
> The **recurring** decimal $0.\dot9 = 0.999\ldots$ has every digit after the point equal to $9$. Each truncation is less than $1$:
>
> $$
> 0.\underbrace{99\ldots9}_{n} = \frac{10^n - 1}{10^n} = 1 - \frac{1}{10^n}.
> $$
>
> Intuition may suggest $0.\dot9 < 1$, a common misconception. Go back to what the words mean. If $a = 0.\dot9$, Definition [[§13 Number Systems#^def-13-6|§13.6]] says
>
> $$
> 1 - \frac{1}{10^n} \le a \le 1, \quad \text{i.e.} \quad 0 \le 1 - a \le \frac{1}{10^n} \qquad \text{for all } n \in \Z^+.
> $$
>
> So $1 - a \ge 0$. If $1 - a > 0$, choose an integer $k > 1/(1 - a)$; then $10^{-k} < 1/k < 1 - a$, so the inequality fails for $n = k$, a contradiction. Hence $1 - a = 0$:
>
> $$
> 0.\dot9 = 1.
> $$
>
> (Equivalently: $1$ itself satisfies the inequalities, so by Proposition [[§13 Number Systems#^prop-13-5|§13.5]] $0.\dot9$ and $1.000\ldots$ represent the same number.) The familiar $1/3 = 0.\dot3$ gives the same result on multiplying by $3$. So a number can have two decimal expansions; this happens exactly for finite decimals (Eccles Problems III Q26–27).
>
> *Eccles: Example 13.3.3*

^ex-13-4

*Uses:* [[§13 Number Systems#^def-13-6|Def. §13.6]], [[§13 Number Systems#^prop-13-5|§13.5]], [[§4 The Completeness Axiom#^thm-4-5|451 Thm. §4.5]]

> [!example] Example §13.5: The First Decimals of √3
> Since $1^2 < 3 < 2^2$, $1.7^2 = 2.89 < 3 < 3.24 = 1.8^2$ and $1.73^2 = 2.9929 < 3 < 3.0276 = 1.74^2$, and $a < b \iff a^2 < b^2$ for non-negative reals ([[§4 Proof by Contradiction#^ex-4-5|Example §4.5]]), we get $1.73 < \sqrt3 < 1.74$: $\sqrt3 = 1.73\ldots$
>
> *Eccles: Exercise 13.2*
> *Source: HW4*

^ex-13-5

### Recurring decimals and rationals

The arithmetic of infinite decimals is complicated, but multiplication by $10$ is easy: for a finite decimal,

$$
10 \times a_0.a_1 a_2 \ldots a_n = 10 a_0 + a_1 + \frac{a_2}{10} + \cdots + \frac{a_n}{10^{n-1}} = (10 a_0 + a_1).a_2 \ldots a_n ,
$$

so it moves the decimal point one place to the right, and the same holds for infinite decimals.

> [!theorem] Lemma §13.6: Moving the Decimal Point
> Let $x = a_0.a_1 a_2 \ldots$. Then
> 1. $10x = (10a_0 + a_1).a_2 a_3 \ldots$;
> 2. $x - a_0 = 0.a_1 a_2 \ldots$.
>
> Consequently, for every $k \ge 0$, $10^k x = N_k . a_{k+1} a_{k+2} \ldots$ with $N_k = 10^k a_0 + 10^{k-1} a_1 + \cdots + a_k \in \N$, and $10^k x - N_k = 0.a_{k+1}a_{k+2}\ldots$
>
> *Eccles: Section 13.3 (text before Theorem 13.3.4)*

^lem-13-6

> [!proof]+ Proof
> (1) For $n \in \Z^+$, the defining inequalities of $x$ at place $n + 1$ are
>
> $$
> a_0.a_1 \ldots a_{n+1} \le x \le a_0.a_1 \ldots a_{n+1} + 10^{-(n+1)};
> $$
>
> multiplying by $10$ and using the finite computation above, they become $(10a_0 + a_1).a_2 \ldots a_{n+1} \le 10x \le (10 a_0 + a_1).a_2 \ldots a_{n+1} + 10^{-n}$, which are the defining inequalities at place $n$ for the decimal $(10a_0 + a_1).a_2 a_3 \ldots$
>
> (2) The truncations of $0.a_1 a_2 \ldots$ are those of $x$ minus $a_0$, so subtracting $a_0$ from the inequalities for $x$ gives those for $x - a_0$.
>
> The last statement follows from (1) by induction on $k$, since $N_{k+1} = 10 N_k + a_{k+1}$, and then from (2).

^pf-13-6

*Uses:* [[§13 Number Systems#^def-13-6|Def. §13.6]], [[§5 The Induction Principle#^thm-5-3|§5.3]] (induction from $0$)

> [!definition] Definition §13.7: Recurring Decimal
> An infinite decimal $a_0.a_1a_2\ldots$ is **recurring** (or repeating) if there are integers $k \ge 0$ and $p \ge 1$ such that $a_{i+p} = a_i$ for all $i > k$: after the $k$th place a block of $p$ digits repeats forever. The repeating block is marked by dots over its first and last digits, as in $7.32\dot0081\dot4 = 7.320081400814\ldots$
>
> *Eccles: Example 13.3.3*

^def-13-7

> [!theorem] Theorem §13.7: Recurring Decimals Are Rational
> A recurring infinite decimal represents a rational number.
>
> *Eccles: Theorem 13.3.4*

^thm-13-7

The idea: if the repeating block has length $p$, multiply by $10^p$ and subtract the original number; the infinite tails cancel, leaving a finite decimal. (Eccles illustrates the method by an example; here is the general proof.)

> [!proof]+ Proof
> Let $x = a_0.a_1a_2\ldots$ with $a_{i+p} = a_i$ for all $i > k$. By Lemma [[§13 Number Systems#^lem-13-6|§13.6]],
>
> $$
> 10^{k+p}x - N_{k+p} = 0.a_{k+p+1}a_{k+p+2}\ldots \qquad \text{and} \qquad 10^k x - N_k = 0.a_{k+1}a_{k+2}\ldots
> $$
>
> By periodicity $a_{k+p+j} = a_{k+j}$ for all $j \ge 1$, so these are the same infinite decimal, and by Proposition [[§13 Number Systems#^prop-13-5|§13.5]] the two numbers are equal. Hence $(10^{k+p} - 10^k)\,x = N_{k+p} - N_k$, an integer, and
>
> $$
> x = \frac{N_{k+p} - N_k}{10^k (10^p - 1)} \in \Q .
> $$

^pf-13-7

*Uses:* [[§13 Number Systems#^lem-13-6|§13.6]], [[§13 Number Systems#^prop-13-5|§13.5]], [[§13 Number Systems#^def-13-7|Def. §13.7]]

> [!remark]- Connections
> - Stewart states both directions: [[§139 Numbers, Inequalities, and Absolute Values#^prop-139-1|Calc Prop. §139.1]].

> [!example] Example §13.6: 12.79317317… as a Fraction
> Let $x = 12.79\dot31\dot7 = 12.79317317317\ldots$ The block $317$ has length $3$, so multiply by $10^3$: $1000x = 12793.17\dot31\dot7$. Splitting off the finite parts (Lemma [[§13 Number Systems#^lem-13-6|§13.6]]),
>
> $$
> x = 12.79 + 0.00\dot31\dot7, \qquad 1000x = 12793.17 + 0.00\dot31\dot7 .
> $$
>
> Subtracting, $999x = 12793.17 - 12.79 = 12780.38 = 1278038/100$, so $x = 1278038/99900$. (In the notation of the proof, $k = 2$, $p = 3$, $N_5 - N_2 = 1279317 - 1279 = 1278038$.)
>
> *Eccles: Example 13.3.5*

^ex-13-6

*Uses:* [[§13 Number Systems#^thm-13-7|§13.7]], [[§13 Number Systems#^lem-13-6|§13.6]]

> [!example] Example §13.7: 1.7782345 2345… as a Fraction
> Let $x = 1.778\dot234\dot5 = 1.7782345\,2345\,2345\ldots$ The block $2345$ has length $4$, so
>
> $$
> x = 1.778 + 0.000\dot234\dot5, \qquad 10000x = 17782.345 + 0.000\dot234\dot5 .
> $$
>
> Subtracting, $9999x = 17782.345 - 1.778 = 17780.567$, so
>
> $$
> x = \frac{17780567}{9999000}.
> $$
>
> This is in lowest terms: $9999000 = 2^3 \cdot 3^2 \cdot 5^3 \cdot 11 \cdot 101$, and $17780567$ is odd, does not end in $0$ or $5$, has digit sum $41$ (not divisible by $3$), and is not divisible by $11$ or $101$.
>
> *Eccles: Exercise 13.5*
> *Source: HW4*

^ex-13-7

*Uses:* [[§13 Number Systems#^thm-13-7|§13.7]], [[§13 Number Systems#^lem-13-6|§13.6]]

The converse also holds: every rational number is represented by a recurring decimal (Eccles Problems IV Q5). Long division of $a$ by $b$ produces remainders in $\{0, 1, \ldots, b-1\}$; by the pigeonhole principle ([[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]]) some remainder recurs, and from then on the digits repeat (the division theorem, [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]], proved later; Eccles Exercise 15.6). So the rational numbers are exactly the recurring decimals, a finite decimal counting as recurring: $a_0.a_1\ldots a_n = a_0.a_1 \ldots a_n \dot0$.
