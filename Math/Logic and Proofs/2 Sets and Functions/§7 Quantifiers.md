---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: 7
eccles: "Ch. 7"
aliases: ["Eccles 7"]
tags: [logic-and-proofs, mat250]
---
← [[§6a Operations on Sets]] · ↑ [[· 2 Sets and Functions]] · [[§7a Several Quantifiers and the Cartesian Product]] →

*Eccles, Chapter 7 · MAT 250 HW3 (Exercises 7.2, 7.4, 7.5, 7.7) · MAT 200 HW1 (Problem 3) · MAT 200 Practice Midterm 1 (Problems 5–8, Example from L3) · MAT 200 supplement (Helfer).*

A predicate $P(a)$ becomes a proposition not only by substituting a value for $a$, but also by saying something about the set $\{a \in A \mid P(a)\}$ of values that make it true: that it is all of $A$ (a universal statement), or that it is non-empty (an existential statement). This section introduces the quantifiers $\forall$ and $\exists$ this way, shows how to prove, disprove and negate quantified statements, and studies statements with several quantifiers, where the order of the quantifiers matters ([[§7a Several Quantifiers and the Cartesian Product|§7a]]). Predicates in two variables define subsets of the Cartesian product, which gives a picture of each quantified statement.

## 7.1 Universal Statements

The universal statements met informally in [[§2 Implications#^def-2-2|Def. §2.2]] are made precise here.

> [!definition] Definition §7.1: Universal Statement
> For a predicate $P(a)$ with free variable $a$ ranging over a set $A$, the notation
>
> $$
> \forall a \in A,\ P(a)
> $$
>
> is an alternative way of writing $\{a \in A \mid P(a)\} = A$. It is read "for each (every, all, any) $a$ in $A$, $P(a)$ is true". The symbol $\forall$ is the **universal quantifier**. Equivalently, it is the **universal implication** $a \in A \Rightarrow P(a)$.
>
> The variable $a$ is a **dummy** (or **bound**) variable: it may be replaced by any symbol not already in use. Quantifiers are written before the predicate they govern.
>
> *Eccles: Definition 7.1.1*

^def-7-1

> [!example] Example §7.1: Three Ways to Write a Universal Statement
> "$a^2 > 0$ for every non-zero real number $a$" ([[§3 Proofs#^prop-3-2|Proposition §3.2]]) can be written
>
> $$
> \forall a \in \R - \{0\},\ a^2 > 0, \qquad \{a \in \R - \{0\} \mid a^2 > 0\} = \R - \{0\}, \qquad a \in \R - \{0\} \Rightarrow a^2 > 0 ,
> $$
>
> and also as $\forall x \in \R - \{0\},\ x^2 > 0$. The third form is the one used to prove it: take a general non-zero real $a$ and deduce $a^2 > 0$.
>
> *Eccles: Section 7.1*

^ex-7-1

## 7.2 Existential Statements

> [!definition] Definition §7.2: Existential Statement
> For a predicate $P(a)$ with $a$ ranging over $A$, the notation
>
> $$
> \exists a \in A,\ P(a)
> $$
>
> is an alternative way of writing $\{a \in A \mid P(a)\} \ne \emptyset$. It is read "for some $a$ in $A$, $P(a)$ is true", "for at least one $a \in A$, $P(a)$", or "there exists $a \in A$ such that $P(a)$". The symbol $\exists$ is the **existential quantifier**.
>
> *Eccles: Definition 7.2.1*

^def-7-2

> [!remark] Remark: The Word "Any"
> "Any" usually means "every": "$a^2 \ge 0$ for any real $a$" is $\forall a \in \R,\ a^2 \ge 0$. But in negative and interrogative sentences it means "some": "there is not any real $a$ with $a^2 < 0$" denies $\exists a \in \R,\ a^2 < 0$, and "is there any real $a$ with $a^2 = 2$?" asks whether $\exists a \in \R,\ a^2 = 2$. A question like "is $a \ge 1$ for any integer $a$?" is ambiguous between $\exists a \in \Z,\ a \ge 1$ (true) and $\forall a \in \Z,\ a \ge 1$ (false); write the quantifier instead.
>
> *Eccles: Remarks 7.2.2*

^rem-7-1

> [!definition] Definition §7.3: Unique Existence
> For a predicate $P(a)$ with $a$ ranging over $A$, the statement
>
> $$
> \exists!\, a \in A,\ P(a)
> $$
>
> ("there exists a unique $a \in A$ such that $P(a)$") means that $P(a)$ holds for exactly one $a \in A$, i.e. the set $\{a \in A \mid P(a)\}$ has exactly one element. In terms of $\forall$ and $\exists$,
>
> $$
> \exists!\, a \in A,\ P(a) \quad\iff\quad \exists a \in A,\ \big(P(a) \text{ and } \forall b \in A,\ (P(b) \Rightarrow b = a)\big).
> $$
>
> So a proof of $\exists!$ has two parts: **existence** (find an $a$ with $P(a)$) and **uniqueness** (show that any $b$ with $P(b)$ equals it; equivalently, if $P(b_1)$ and $P(b_2)$ then $b_1 = b_2$).
>
> *Source: MAT 200 supplement §6; MAT 200 lecture (syllabus week 2)*

^def-7-3

> [!example] Example §7.2: Existence With and Without Uniqueness
> - $\exists!\, x \in \R,\ 2x + 1 = 5$. Existence: $x = 2$ works. Uniqueness: if $2b + 1 = 5$ then $2b = 4$, so $b = 2$.
> - $\exists x \in \R,\ x^2 = 4$ is true but $\exists!\, x \in \R,\ x^2 = 4$ is false, since both $2$ and $-2$ satisfy it.
> - $\exists!\, n \in \Z^+,\ \forall m \in \Z^+,\ n \le m$ (there is exactly one least positive integer, namely $1$): existence by $n = 1$, since every positive integer is $\ge 1$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]); if $n_1, n_2$ both have the property, then $n_1 \le n_2$ and $n_2 \le n_1$, so $n_1 = n_2$ ([[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]]).
>
> *Source: MAT 200 supplement §6*

^ex-7-2

Uniqueness statements of this kind recur throughout: the inverse of a bijection ([[§9 Injections, Surjections and Bijections#^thm-9-2|Theorem §9.2]]), the quotient and remainder of the division theorem ([[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]).

## 7.3 Proving Statements Involving Quantifiers

> [!remark] Remark: How to Prove ∀ and ∃
> - To prove $\forall a \in A,\ P(a)$, rewrite it as the universal implication $a \in A \Rightarrow P(a)$: take a *general* element $a \in A$, about which nothing else is assumed, and deduce $P(a)$.
> - To prove $\exists a \in A,\ P(a)$, the most direct way is **proof by example**: exhibit one particular $a \in A$ and check $P(a)$. (Indirect existence proofs, such as counting arguments, come later: the pigeonhole principle, [[§11 Properties of Finite Sets#^thm-11-2|Theorem §11.2]].)
> - To *use* a hypothesis $\exists q,\ Q(q)$ in a proof, name a specific element with the property ("let $q_1$ be an integer with $n = 2q_1$") and work with it; use a fresh letter each time a definition involving $\exists$ is unpacked.
>
> *Eccles: Section 7.3*

^rem-7-2

> [!example] Example §7.3: Proof by Example
> $\exists n \in \Z,\ n^2 = 9$: indeed $3 \in \Z$ and $3^2 = 9$.
>
> *Eccles: Example 7.3.1*

^ex-7-3

> [!theorem] Proposition §7.1: Squares of Even Integers Are Even
> For integers $n$, if $n$ is even then $n^2$ is even. In symbols, with "even" spelled out ([[§2 Implications#^def-2-8|Def. §2.8]]):
>
> $$
> \forall n \in \Z,\ \big( (\exists q \in \Z,\ n = 2q) \Rightarrow (\exists p \in \Z,\ n^2 = 2p) \big).
> $$
>
> *Eccles: Proposition 7.3.2*

^prop-7-1

> [!proof]+ Proof
> Let $n$ be an integer, and suppose $n$ is even. Then $\exists q \in \Z,\ n = 2q$, so let $q_1$ be an integer with $n = 2q_1$. Then
>
> $$
> n^2 = (2q_1)^2 = 4q_1^2 = 2(2q_1^2),
> $$
>
> and $p = 2q_1^2$ is an integer, so $\exists p \in \Z,\ n^2 = 2p$: $n^2$ is even.
>
> The statement has a universal quantifier on the outside and an existential one in both the hypothesis and the conclusion. The hypothesis is *used* by naming a witness $q_1$; the conclusion is *proved* by constructing a witness $p$ from it. Writing "$n = 2q$ for some $q$" and then "$n^2 = 2(2q^2)$" blurs the existential statement with the specific integer it provides; this is harmless as long as a new letter is used for each new witness.

^pf-7-1

*Uses:* [[§7 Quantifiers#^def-7-1|Def. §7.1]], [[§7 Quantifiers#^def-7-2|Def. §7.2]], [[§2 Implications#^def-2-8|Def. §2.8]]

> [!example] Example §7.4: Squares of Odd Integers Are Odd
> **Claim:** for $n \in \Z$, $\ (\exists q \in \Z,\ n = 2q + 1) \Rightarrow (\exists p \in \Z,\ n^2 = 2p + 1)$.
>
> Suppose $\exists q \in \Z,\ n = 2q + 1$, and let $q_1 \in \Z$ satisfy $n = 2q_1 + 1$. Then
>
> $$
> n^2 = (2q_1 + 1)^2 = 4q_1^2 + 4q_1 + 1 = 2(2q_1^2 + 2q_1) + 1 ,
> $$
>
> so $p = 2q_1^2 + 2q_1 \in \Z$ satisfies $n^2 = 2p + 1$. The hypothesis is used through a named witness $q_1$, and the conclusion is proved by exhibiting the witness $p$.
>
> *Source: HW3*
> *Eccles: Exercise 7.5*

^ex-7-4

## 7.4 Disproving and Negating Quantified Statements

Disproving a statement $S$ is the same as proving its negation "not $S$". For quantified statements the negation has a simple form.

> [!theorem] Theorem §7.2: Negating Quantifiers
> For a predicate $P(a)$ with $a$ ranging over $A$:
>
> $$
> \text{not}\,(\forall a \in A,\ P(a)) \iff \exists a \in A,\ \text{not}\, P(a), \qquad\qquad \text{not}\,(\exists a \in A,\ P(a)) \iff \forall a \in A,\ \text{not}\, P(a).
> $$
>
> The second negation is also written $\nexists a \in A,\ P(a)$.
>
> *Eccles: Section 7.4(a), (b)*

^thm-7-2

> [!proof]+ Proof
> Let $S = \{a \in A \mid P(a)\} \subseteq A$; then $A - S = \{a \in A \mid \text{not}\, P(a)\}$.
>
> First: $\forall a \in A,\ P(a)$ means $S = A$. Since $S \subseteq A$, by [[§6 The Language of Set Theory#^prop-6-1|Proposition §6.1]](1) $S = A$ fails exactly when $A \not\subseteq S$, i.e. when some element of $A$ is not in $S$, i.e. $A - S \ne \emptyset$. That is the statement $\exists a \in A,\ \text{not}\, P(a)$.
>
> Second: $\exists a \in A,\ P(a)$ means $S \ne \emptyset$, so its negation is $S = \emptyset$. Now $S = \emptyset$ holds if and only if every $a \in A$ lies outside $S$, i.e. $A - S = A$, which is $\forall a \in A,\ \text{not}\, P(a)$.

^pf-7-2

*Uses:* [[§7 Quantifiers#^def-7-1|Def. §7.1]], [[§7 Quantifiers#^def-7-2|Def. §7.2]], [[§6 The Language of Set Theory#^prop-6-1|§6.1]], [[§6a Operations on Sets#^def-6a-4|Def. §6a.4]]

So a universal statement is disproved by a single **counterexample**, an $a \in A$ with $P(a)$ false; an existential statement is disproved either by proving $\forall a \in A,\ \text{not}\, P(a)$ or by showing that $P(a)$ with $a \in A$ leads to a contradiction ([[§4 Proof by Contradiction#^thm-4-2|Theorem §4.2]]).

> [!example] Example §7.5: Disproof by Counterexample
> $\forall x \in \R,\ x^2 > 2$ is false: $x = 1$ is a counterexample, since $1 \in \R$ and $1^2 = 1 \not> 2$.
>
> *Eccles: Example 7.4.1*

^ex-7-5

> [!theorem] Proposition §7.3: −1 Has No Real Square Root
> There does not exist a real number $x$ such that $x^2 = -1$.
>
> *Eccles: Proposition 7.4.2*

^prop-7-3

> [!proof]+ Proof
> By [[§7 Quantifiers#^thm-7-2|Theorem §7.2]] we must show $\forall x \in \R,\ x^2 \ne -1$. For every $x \in \R$ we have $x^2 \ge 0 > -1$, so $x^2 \neq -1$.

^pf-7-3

*Uses:* [[§7 Quantifiers#^thm-7-2|§7.2]]

> [!remark] Remark: Negation in Everyday Speech
> "All the members of the class are not here" is normally meant as the negation of "all the members are here", i.e. "*some* member is not here". Read literally it says "every member is absent", which is a different statement: compare "all the numbers in the set are not even", which can only mean "all the numbers are odd". To express the negation of a universal statement unambiguously, say "not all the members are here".
>
> *Eccles: Section 7.4(a)*

^rem-7-3

Combined with the laws of [[§1 The Language of Mathematics#^thm-1-1|Theorem §1.1]] and [[§2 Implications#^prop-2-1|Proposition §2.1]], [[§7 Quantifiers#^thm-7-2|Theorem §7.2]] produces a *useful denial* ([[§1 The Language of Mathematics#^def-1-10|Def. §1.10]]) of any quantified statement: switch each quantifier ($\forall \leftrightarrow \exists$), keeping its domain and the order of the quantifiers, and then deny the predicate using

$$
\neg\neg P \equiv P, \qquad \neg(P \wedge Q) \equiv \neg P \vee \neg Q, \qquad \neg(P \vee Q) \equiv \neg P \wedge \neg Q, \qquad \neg(P \Rightarrow Q) \equiv P \wedge \neg Q ,
$$

until "not" is absorbed into the simplest statements ($\neg(x > 2)$ becomes $x \le 2$), as in the unquantified denial of [[§2 Implications#^ex-2-9|Ex. §2.9]](c). For example, the denial of $\forall \varepsilon > 0\ \exists N\ \forall n\ (n \ge N \Rightarrow |a_n| < \varepsilon)$ is $\exists \varepsilon > 0\ \forall N\ \exists n\ (n \ge N \wedge |a_n| \ge \varepsilon)$.

> [!example] Example §7.6: From English to Symbols
> **(a)** "There exists a positive integer $n$ such that $n$ is greater than $3$ but two times $n$ is not greater than $3$":
>
> $$
> \exists n \in \Z^+,\ (n > 3) \wedge (2n \le 3).
> $$
>
> "But" is logically "and", and "not greater than" is $\le$. (The statement is false: $n > 3$ gives $2n > 6 > 3$.)
>
> **(b)** "For every pair of real numbers $x, y$, either $x^2 < y$ or $y^2 < x$":
>
> $$
> \forall x, y \in \R,\ (x^2 < y) \vee (y^2 < x).
> $$
>
> Its useful denial is $\exists x, y \in \R,\ (x^2 \ge y) \wedge (y^2 \ge x)$, which is true ($x = y = 0$), so (b) is false.
>
> *Source: MAT 200 HW1, Problem 3*

^ex-7-6

> [!example] Example §7.7: A Useful Denial
> *For every real number $x$, one can find a real number $y$ such that $x > 2$ whenever $x + y \le 3$.*
>
> **Symbols.** "Whenever $x + y \le 3$" is the hypothesis of an implication, so the statement is
>
> $$
> \forall x \in \R,\ \exists y \in \R,\ (x + y \le 3 \Rightarrow x > 2).
> $$
>
> **Useful denial.** Switching the quantifiers and using $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$ ([[§2 Implications#^prop-2-1|Proposition §2.1]]):
>
> $$
> \exists x \in \R,\ \forall y \in \R,\ (x + y \le 3 \wedge x \le 2).
> $$
>
> **Truth value.** The statement is true and the denial false. Since $(P \Rightarrow Q) \equiv (\neg P \vee Q)$ ([[§2 Implications#^prop-2-1|Proposition §2.1]]), the statement says $\forall x\ \exists y,\ (x + y > 3 \vee x > 2)$. Given $x$, take $y = 4 - x$: then $x + y = 4 > 3$, so the implication has a false hypothesis and is true. (The denial fails for the same reason: no $x$ has $x + y \le 3$ for *all* $y$.)
>
> **Picture.** The set $\{(x, y) \in \R^2 \mid x + y > 3 \text{ or } x > 2\}$ is the union of the half-plane above the line $x + y = 3$ and the half-plane $x > 2$; the statement says that every vertical line $\{x\} \times \R$ meets it (compare the pictures in [[§7a Several Quantifiers and the Cartesian Product#^ex-7a-8|Example §7a.8]] and [[§7a Several Quantifiers and the Cartesian Product#^ex-7a-9|Example §7a.9]]).
>
> *Source: MAT 200 Practice Midterm 1 ("Example from L3")*

^ex-7-7

## 7.5 Proof by Induction in the Language of Sets

A statement $\forall n \in \Z^+,\ P(n)$ says that the subset $\{n \in \Z^+ \mid P(n)\}$ is all of $\Z^+$. So induction ([[§5 The Induction Principle#^def-5-1|Def. §5.1]]; strong induction and well-ordering are also in [[§5 The Induction Principle|§5]]) is a method for proving that certain subsets of $\Z^+$ are the whole set.

> [!definition] Definition §7.4: The Induction Principle, Set Form
> Let $A$ be a subset of $\Z^+$. Then $A = \Z^+$ if
> 1. $1 \in A$, and
> 2. $\forall k \in \Z^+,\ (k \in A \Rightarrow k + 1 \in A)$.
>
> *Eccles: Axiom 7.5.1*

^def-7-4

> [!proof]- Proof (equivalence with the induction principle of §5)
> The induction principle ([[§5 The Induction Principle#^def-5-1|Def. §5.1]], Eccles Axiom 5.1.1) says: if $P(n)$ is a statement about a general positive integer $n$, $P(1)$ is true, and $P(k) \Rightarrow P(k + 1)$ for all $k \in \Z^+$, then $P(n)$ is true for all $n \in \Z^+$.
>
> *Axiom 5.1.1 implies the set form:* given $A \subseteq \Z^+$ satisfying 1 and 2, let $P(n)$ be the statement $n \in A$. Then $P(1)$ holds and $P(k) \Rightarrow P(k + 1)$ for all $k$, so $n \in A$ for all $n \in \Z^+$, i.e. $\Z^+ \subseteq A$; with $A \subseteq \Z^+$ this gives $A = \Z^+$.
>
> *The set form implies Axiom 5.1.1:* given $P(n)$ with $P(1)$ true and $P(k) \Rightarrow P(k + 1)$, put $A = \{n \in \Z^+ \mid P(n)\}$. Then $1 \in A$ and $k \in A \Rightarrow k + 1 \in A$, so $A = \Z^+$, which says $\forall n \in \Z^+,\ P(n)$.

^pf-def-7-4

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§6 The Language of Set Theory#^prop-6-1|§6.1]], [[§7 Quantifiers#^def-7-1|Def. §7.1]]

> [!remark]- Connections
> - This is axiom 3 of Peano's axioms in [[§9 Injections, Surjections and Bijections#^def-9-9|Def. §9.9]], and axiom 5 of [[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]] (Peano axioms), from which 451 derives induction ([[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 Thm. §1.1]]).

The strong induction principle ([[§5 The Induction Principle#^thm-5-6|Theorem §5.6]]) has a set form in the same way: [[§5 The Induction Principle#^ex-5-9|Example §5.9]].

Statements with several quantifiers and the Cartesian product continue in [[§7a Several Quantifiers and the Cartesian Product]].
