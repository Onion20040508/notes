---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: 7
eccles: "Ch. 7"
aliases: ["Eccles 7"]
tags: [logic-and-proofs, mat250]
---
← [[§6 The Language of Set Theory]] · ↑ [[· 2 Sets and Functions]] · [[§8 Functions]] →

*Eccles, Chapter 7 · MAT 250 HW3 (Exercises 7.2, 7.4, 7.5, 7.7) · MAT 200 HW1 (Problem 3) · MAT 200 Practice Midterm 1 (Problems 5–8, Example from L3) · MAT 200 supplement (Helfer).*

A predicate $P(a)$ becomes a proposition not only by substituting a value for $a$, but also by saying something about the set $\{a \in A \mid P(a)\}$ of values that make it true: that it is all of $A$ (a universal statement), or that it is non-empty (an existential statement). This section introduces the quantifiers $\forall$ and $\exists$ this way, shows how to prove, disprove and negate quantified statements, and studies statements with several quantifiers, where the order of the quantifiers matters. Predicates in two variables define subsets of the Cartesian product, which gives a picture of each quantified statement.

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
> For integers $n$, if $n$ is even then $n^2$ is even. In symbols, with "even" spelled out ([[§2 Implications#^def-2-7|Def. §2.7]]):
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

*Uses:* [[§7 Quantifiers#^def-7-1|Def. §7.1]], [[§7 Quantifiers#^def-7-2|Def. §7.2]], [[§2 Implications#^def-2-7|Def. §2.7]]

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

*Uses:* [[§7 Quantifiers#^def-7-1|Def. §7.1]], [[§7 Quantifiers#^def-7-2|Def. §7.2]], [[§6 The Language of Set Theory#^prop-6-1|§6.1]], [[§6 The Language of Set Theory#^def-6-8|Def. §6.8]]

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

Combined with the laws of [[§1 The Language of Mathematics#^thm-1-1|Theorem §1.1]] and [[§2 Implications#^prop-2-1|Proposition §2.1]], [[§7 Quantifiers#^thm-7-2|Theorem §7.2]] produces a *useful denial* ([[§1 The Language of Mathematics#^def-1-7|Def. §1.7]]) of any quantified statement: switch each quantifier ($\forall \leftrightarrow \exists$), keeping its domain and the order of the quantifiers, and then deny the predicate using

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
> **Picture.** The set $\{(x, y) \in \R^2 \mid x + y > 3 \text{ or } x > 2\}$ is the union of the half-plane above the line $x + y = 3$ and the half-plane $x > 2$; the statement says that every vertical line $\{x\} \times \R$ meets it (compare the pictures in [[§7 Quantifiers#^ex-7-15|Example §7.15]] and [[§7 Quantifiers#^ex-7-16|Example §7.16]]).
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
> - This is axiom 3 of Peano's axioms in [[§9 Injections, Surjections and Bijections#^def-9-6|Def. §9.6]], and axiom 5 of [[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]] (Peano axioms), from which 451 derives induction ([[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 Thm. §1.1]]).

The strong induction principle ([[§5 The Induction Principle#^thm-5-6|Theorem §5.6]]) has a set form in the same way: [[§5 The Induction Principle#^ex-5-9|Example §5.9]].

## 7.6 Predicates Involving More Than One Free Variable

> [!remark] Remark: Statements With Two Quantifiers
> A predicate $P(a, b)$ with $a \in A$ and $b \in B$ gives the propositions
>
> $$
> \begin{aligned}
> &\text{(i) } \forall a \in A,\ \forall b \in B,\ P(a, b); && \text{(ii) } \exists a \in A,\ \exists b \in B,\ P(a, b); \\
> &\text{(iii) } \forall a \in A,\ \exists b \in B,\ P(a, b); && \text{(iv) } \exists b \in B,\ \forall a \in A,\ P(a, b); \\
> &\text{(v) } \forall b \in B,\ \exists a \in A,\ P(a, b); && \text{(vi) } \exists a \in A,\ \forall b \in B,\ P(a, b).
> \end{aligned}
> $$
>
> They are read from the left: in (iii), "$\exists b \in B,\ P(a, b)$" is a predicate in the single free variable $a$, and (iii) says it holds for every $a$. So in (iii) the $b$ may depend on $a$, while in (iv) one $b$ must work for every $a$. "$\forall a, b \in A$" abbreviates "$\forall a \in A,\ \forall b \in A$", and similarly for $\exists$. Examples already met: [[§3 Proofs#^prop-3-1|Proposition §3.1]] ($\forall a, b \in \R^+,\ a < b \Rightarrow a^2 < b^2$) and [[§4 Proof by Contradiction#^prop-4-1|Proposition §4.1]] (not $\exists m, n \in \Z,\ 14m + 20n = 101$).
>
> *Eccles: Section 7.6*

^rem-7-4

> [!theorem] Theorem §7.4: Interchanging Quantifiers
> Let $P(a, b)$ be a predicate with $a \in A$, $b \in B$.
> 1. $\forall a \in A,\ \forall b \in B,\ P(a, b) \iff \forall b \in B,\ \forall a \in A,\ P(a, b)$.
> 2. $\exists a \in A,\ \exists b \in B,\ P(a, b) \iff \exists b \in B,\ \exists a \in A,\ P(a, b)$.
> 3. $\exists a \in A,\ \forall b \in B,\ P(a, b) \implies \forall b \in B,\ \exists a \in A,\ P(a, b)$.
>
> The converse of 3 is false in general: quantifiers of different kinds may not be interchanged.
>
> *Source: MAT 200 lecture (syllabus week 2: "interchanging quantifiers"); MAT 200 Practice Midterm 1, Problem 6*

^thm-7-4

> [!proof]+ Proof
> (1) Both sides say that $P(a, b)$ is true for every choice of $a \in A$ and $b \in B$.
>
> (2) Both sides say that $P(a, b)$ is true for at least one choice of $a \in A$ and $b \in B$.
>
> (3) Suppose $\exists a \in A,\ \forall b \in B,\ P(a, b)$, and let $a_0 \in A$ be such that $P(a_0, b)$ holds for all $b \in B$. Given any $b \in B$, the element $a = a_0$ satisfies $P(a, b)$. Hence $\forall b \in B,\ \exists a \in A,\ P(a, b)$.
>
> For the converse, take $A = B = \Z^+$ and $P(a, b)$: $b < a$. Then $\forall b\ \exists a,\ b < a$ is true ($a = b + 1$), but $\exists a\ \forall b,\ b < a$ is false (for each $a$, $b = a$ fails); this is [[§7 Quantifiers#^ex-7-8|Example §7.8]] (a), (b).

^pf-7-4

*Uses:* [[§7 Quantifiers#^def-7-1|Def. §7.1]], [[§7 Quantifiers#^def-7-2|Def. §7.2]], [[§7 Quantifiers#^ex-7-8|Ex. §7.8]]

> [!remark]- Connections
> - The same quantifier move in analysis: continuity at every point ($\forall x\, \forall \varepsilon\, \exists \delta$) versus uniform continuity ($\forall \varepsilon\, \exists \delta\, \forall x$), [[§19 Uniform Continuity#^def-19-1|451 Def. §19.1]]; pointwise versus uniform convergence ($N$ depending on $x$ or not), [[§24 Uniform Convergence#^def-24-2|451 Def. §24.2]].

> [!example] Example §7.8: The Order of Quantifiers
> Consider the predicate $m < n$ for $m, n \in \Z^+$.
>
> **(a)** $\forall m \in \Z^+,\ \exists n \in \Z^+,\ m < n$ is **true**: it says $\{m \in \Z^+ \mid \exists n \in \Z^+,\ m < n\} = \Z^+$. Given $m \in \Z^+$, put $n = m + 1$; then $n \in \Z^+$ and $m < n$.
>
> **(b)** $\exists n \in \Z^+,\ \forall m \in \Z^+,\ m < n$ is **false**: such an $n$ would exceed every positive integer, including itself. For each $n \in \Z^+$, put $m = n$; then $m \in \Z^+$ and $m \not< n$, a counterexample to $\forall m,\ m < n$.
>
> **(c)** $\forall n \in \Z^+,\ \exists m \in \Z^+,\ m < n$ is **false**: $\{n \in \Z^+ \mid \exists m \in \Z^+,\ m < n\} = \Z^+ - \{1\}$. A counterexample is $n = 1$, since $m \not< 1$ for all $m \in \Z^+$.
>
> **(d)** $\exists m \in \Z^+,\ \forall n \in \Z^+,\ m < n$ is **false**: for each $m \in \Z^+$, put $n = m$; then $m \not< n$.
>
> Compare (b) and (d). Both use the implication $m = n \Rightarrow m \not< n$, but in (b) we start from a general $n$ and *define* $m = n$, while in (d) we start from a general $m$ and define $n = m$: the variable bound by the inner $\forall$ is the one we get to choose.
>
> *Eccles: Examples 7.6.1–7.6.4*

^ex-7-8

> [!example] Example §7.9: Quantifiers and ≤ on the Positive Integers
> For $m, n \in \Z^+$:
>
> | statement | value | reason |
> |---|---|---|
> | (i) $\forall m, n \in \Z^+,\ m \le n$ | false | counterexample $m = 2$, $n = 1$ |
> | (ii) $\exists m, n \in \Z^+,\ m \le n$ | true | example $m = n = 1$ |
> | (iii) $\forall m \in \Z^+,\ \exists n \in \Z^+,\ m \le n$ | true | given $m$, take $n = m$ (or $m + 1$) |
> | (iv) $\exists m \in \Z^+,\ \forall n \in \Z^+,\ m \le n$ | true | $m = 1$: every positive integer is $\ge 1$ ([[§5 The Induction Principle#^ex-5-2\|Ex. §5.2]]) |
> | (v) $\forall n \in \Z^+,\ \exists m \in \Z^+,\ m \le n$ | true | given $n$, take $m = n$ (or $m = 1$) |
> | (vi) $\exists n \in \Z^+,\ \forall m \in \Z^+,\ m \le n$ | false | for each $n$, $m = n + 1$ gives $m \not\le n$ |
>
> In (vi) the useful denial $\forall n \in \Z^+,\ \exists m \in \Z^+,\ m > n$ is proved, as in (iii), by the choice $m = n + 1$. Note that (iv) is true and therefore so is (v), by [[§7 Quantifiers#^thm-7-4|§7.4]](3) with the roles of the variables matched; but (iii) true does not force (vi).
>
> *Source: HW3*
> *Eccles: Exercise 7.2*

^ex-7-9

> [!example] Example §7.10: Quantifiers Over the Reals
> | statement | value | reason |
> |---|---|---|
> | (i) $\forall x \in \R,\ \exists y \in \R,\ x + y = 0$ | true | given $x$, take $y = -x$ |
> | (ii) $\exists y \in \R,\ \forall x \in \R,\ x + y = 0$ | false | for each $y$, $x = 1 - y$ gives $x + y = 1 \ne 0$ |
> | (iii) $\forall x \in \R,\ \exists y \in \R,\ xy = 0$ | true | take $y = 0$ |
> | (iv) $\exists y \in \R,\ \forall x \in \R,\ xy = 0$ | true | $y = 0$ works for every $x$ |
> | (v) $\forall x \in \R,\ \exists y \in \R,\ xy = 1$ | false | counterexample $x = 0$: $0 \cdot y = 0 \ne 1$ |
> | (vi) $\exists y \in \R,\ \forall x \in \R,\ xy = 1$ | false | for each $y$, $x = 0$ gives $xy = 0 \ne 1$ |
> | (vii) $\forall n \in \Z^+,\ (n \text{ even or } n \text{ odd})$ | true | "odd" means "not even" ([[§2 Implications#^def-2-7\|Def. §2.7]]), so this is $P \vee \neg P$ |
> | (viii) $(\forall n \in \Z^+,\ n \text{ even}) \text{ or } (\forall n \in \Z^+,\ n \text{ odd})$ | false | $1$ is not even and $2$ is not odd |
>
> In (iii)–(iv) one $y$ serves for all $x$; in (i)–(ii) the $y$ has to depend on $x$. Items (vii) and (viii) show that $\forall$ distributes over "or" in only one direction: (viii) $\Rightarrow$ (vii), but not conversely.
>
> *Source: HW3*
> *Eccles: Exercise 7.4*

^ex-7-10

> [!example] Example §7.11: Quantifiers Over Intervals
> Take $x \in [0, 2]$, $y \in [1, 3]$ and the predicate $y < x$.
>
> | statement | value | reason |
> |---|---|---|
> | (a) $\exists x \in [0,2],\ \exists y \in [1,3],\ y < x$ | true | $x = 2$, $y = 1$ |
> | (b) $\forall x \in [0,2],\ \forall y \in [1,3],\ y < x$ | false | denial $\exists x\, \exists y,\ y \ge x$: $x = 0$, $y = 2$ |
> | (c) $\exists x \in [0,2],\ \forall y \in [1,3],\ y < x$ | false | denial $\forall x\, \exists y,\ y \ge x$: take $y = 3 > 2 \ge x$ |
> | (d) $\forall y \in [1,3],\ \exists x \in [0,2],\ y < x$ | false | denial $\exists y\, \forall x,\ y \ge x$: $y = 3$ |
> | (e) $\exists y \in [1,3],\ \forall x \in [0,2],\ y < x$ | false | denial $\forall y\, \exists x,\ y \ge x$: take $x = 0$ |
> | (f) $\forall x \in [0,2],\ \exists y \in [1,3],\ y < x$ | false | denial $\exists x\, \forall y,\ y \ge x$: $x = 0$ |
>
> Geometrically, the truth set $\{(x, y) \in [0,2] \times [1,3] \mid y < x\}$ is the small triangle below the diagonal in the corner near $(2, 1)$. Statement (a) says it is non-empty, (b) that it is the whole rectangle, (c) that it contains a whole vertical segment $\{x\} \times [1, 3]$, (d) that every horizontal segment $[0,2] \times \{y\}$ meets it, (e) that it contains a whole horizontal segment, (f) that every vertical segment meets it. As [[§7 Quantifiers#^thm-7-4|§7.4]](3) predicts, (c) $\Rightarrow$ (d) and (e) $\Rightarrow$ (f); here all four are false.
>
> *Source: MAT 200 Practice Midterm 1, Problem 6*

^ex-7-11

> [!example] Example §7.12: All Quantified Forms of One Predicate
> For real $x, y$ consider $x^2 + xy + 1 = 0$. Solving: for $x \ne 0$ it holds iff $y = -(1 + x^2)/x$; as a quadratic in $x$ it has a real solution iff the discriminant $y^2 - 4 \ge 0$, i.e. $|y| \ge 2$.
>
> | statement | value | reason |
> |---|---|---|
> | (1) $\exists x\, \exists y$ | true | $x = -1$, $y = 2$: $1 - 2 + 1 = 0$ |
> | (2) $\exists y\, \exists x$ | true | equivalent to (1) ([[§7 Quantifiers#^thm-7-4\|§7.4]](2)) |
> | (3) $\forall x\, \forall y$ | false | $x = y = 0$ gives $1 \ne 0$ |
> | (4) $\forall y\, \forall x$ | false | equivalent to (3) |
> | (5) $\exists x\, \forall y$ | false | denial $\forall x\, \exists y,\ x^2 + xy + 1 \ne 0$: take $y = -x$, giving $1 \ne 0$ |
> | (6) $\forall x\, \exists y$ | false | counterexample $x = 0$: $0 + 0 + 1 \ne 0$ for every $y$ |
> | (7) $\exists y\, \forall x$ | false | denial $\forall y\, \exists x$: take $x = 0$ |
> | (8) $\forall y\, \exists x$ | false | counterexample $y = 0$: $x^2 + 1 \ne 0$ for every $x$ (any $|y| < 2$ works) |
>
> Since (8) is false, so is (5), by [[§7 Quantifiers#^thm-7-4|§7.4]](3); likewise (6) false forces (7) false.
>
> *Source: MAT 200 Practice Midterm 1, Problem 7*

^ex-7-12

> [!example] Example §7.13: Quantifiers With a Parameter
> For real $a$ and $x$ let $p_a(x) = x^2 - 2ax + 4a + 5$. Completing the square,
>
> $$
> p_a(x) = (x - a)^2 + c_a, \qquad c_a = -a^2 + 4a + 5 = -(a - 5)(a + 1),
> $$
>
> so $p_a(x) \ge c_a$ for all $x$, with equality at $x = a$. The values of $a$ for which each statement holds:
>
> **(a)** $\exists x,\ p_a(x) = 0$ $\iff$ $c_a \le 0$ $\iff$ $a \le -1$ or $a \ge 5$. If $c_a \le 0$, then $x = a + \sqrt{-c_a}$ works; if $c_a > 0$ then $p_a(x) \ge c_a > 0$ for all $x$.
>
> **(b)** $\forall x,\ p_a(x) = 0$ holds for **no** $a$: $p_a(a) = c_a$ and $p_a(a + 1) = c_a + 1$ cannot both be $0$.
>
> **(c)** $\exists x,\ p_a(x) > 0$ holds for **all** $a$: take $x = a + |c_a| + 1$; then $(x - a)^2 \ge |c_a| + 1 > -c_a$, so $p_a(x) > 0$.
>
> **(d)** $\forall x,\ p_a(x) > 0$ $\iff$ $c_a > 0$ $\iff$ $-1 < a < 5$. If $c_a > 0$ then $p_a(x) \ge c_a > 0$; if $c_a \le 0$ then $x = a$ is a counterexample.
>
> Note (b) $\Rightarrow$ (a) and (d) $\Rightarrow$ (c), since a universal statement over a non-empty set implies the existential one; and (d) is the negation of (a), as [[§7 Quantifiers#^thm-7-2|Theorem §7.2]] predicts once one notes that $\exists x,\ p_a(x) \le 0$ is equivalent to $\exists x,\ p_a(x) = 0$ here.
>
> *Source: MAT 200 Practice Midterm 1, Problem 8*

^ex-7-13

## 7.7 The Cartesian Product of Two Sets

> [!definition] Definition §7.5: Cartesian Product; Ordered Pair
> Given sets $X$ and $Y$, the **Cartesian product** $X \times Y$ is the set of all **ordered pairs** $(x, y)$ with $x \in X$ and $y \in Y$:
>
> $$
> X \times Y = \{(x, y) \mid x \in X \text{ and } y \in Y\}.
> $$
>
> "Ordered" means that $(x_1, y_1) = (x_2, y_2)$ if and only if $x_1 = x_2$ and $y_1 = y_2$; $x$ and $y$ are the **coordinates** of $(x, y)$. We write $X^2 = X \times X$. In pictures $X$ is drawn horizontally and $Y$ vertically.
>
> *Eccles: Definition 7.7.1*

^def-7-5

> [!example] Example §7.14: Products
> - For $X = \{a, b, c\}$ and $Y = \{a, b\}$: $X \times Y = \{(a,a), (a,b), (b,a), (b,b), (c,a), (c,b)\}$ and $Y \times X = \{(a,a), (a,b), (a,c), (b,a), (b,b), (b,c)\}$. These are different: $(c, a) \in X \times Y$ but $(c, a) \notin Y \times X$.
> - $\R^2 = \R \times \R$ is the Euclidean plane. A predicate $P(x, y)$ defines a subset $\{(x, y) \in \R^2 \mid P(x, y)\}$, e.g. the unit circle $\{(x, y) \in \R^2 \mid x^2 + y^2 = 1\}$, the set of points satisfying the *equation* $x^2 + y^2 = 1$.
>
> *Eccles: Examples 7.7.2*

^ex-7-14

> [!example] Example §7.15: Quantified Statements as Pictures
> A predicate $P(a, b)$ on $A \times B$ determines its truth set $T = \{(a, b) \in A \times B \mid P(a, b)\}$. Write $\{a\} \times B$ for the vertical line through $a$ and $A \times \{b\}$ for the horizontal line through $b$. Then:
> - $\forall a\, \exists b,\ P(a, b)$: every vertical line meets $T$;
> - $\exists a\, \forall b,\ P(a, b)$: some vertical line lies entirely in $T$;
> - $\forall b\, \exists a,\ P(a, b)$: every horizontal line meets $T$;
> - $\exists b\, \forall a,\ P(a, b)$: some horizontal line lies entirely in $T$.
>
> For $m < n$ on $\Z^+ \times \Z^+$ (figure below), this re-proves [[§7 Quantifiers#^ex-7-8|Example §7.8]]: (a) is true because the column $\{m\} \times \Z^+$ contains $(m, m + 1)$; (b) is false because each row $\Z^+ \times \{n\}$ contains $(n, n) \notin T$; (c) is false because the row $\Z^+ \times \{1\}$ misses $T$; (d) is false because each column $\{m\} \times \Z^+$ contains $(m, m) \notin T$.
>
> *Eccles: Example 7.7.3*

^ex-7-15

![[m250-7-1.svg]]
*The truth set of $m < n$ in $\Z^+ \times \Z^+$: solid dots above the diagonal. Every column, such as $\{3\} \times \Z^+$ (blue), contains a solid dot, so $\forall m\, \exists n,\ m < n$; the bottom row $\Z^+ \times \{1\}$ (red) contains none, so $\forall n\, \exists m,\ m < n$ fails at $n = 1$.*

> [!example] Example §7.16: An Implication as a Region of the Plane
> **Problem:** find all points $(x, y)$ for which the propositional form $2x + 3y > 6 \Rightarrow x \le y^2$ is true.
>
> Since $(P \Rightarrow Q) \equiv (\neg P \vee Q)$ ([[§2 Implications#^prop-2-1|Proposition §2.1]]), the truth set is
>
> $$
> \{(x, y) \in \R^2 \mid 2x + 3y \le 6\} \cup \{(x, y) \in \R^2 \mid x \le y^2\} ,
> $$
>
> the union of the closed half-plane on or below the line $2x + 3y = 6$ and the region on or to the left of the parabola $x = y^2$: a disjunction of conditions becomes a union of regions. The implication fails exactly on the complement, where $2x + 3y > 6$ and $x > y^2$: inside the parabola and strictly above the line. The line meets the parabola where $2y^2 + 3y - 6 = 0$, i.e. $y = \frac{-3 \pm \sqrt{57}}{4}$.
>
> *Source: MAT 200 Practice Midterm 1, Problem 5*

^ex-7-16

![[m250-7-2.svg]]
*The truth set of $2x + 3y > 6 \Rightarrow x \le y^2$ (shaded) is everything except the white region, which lies inside the parabola $x = y^2$ (blue) and above the line $2x + 3y = 6$ (dashed). Its lower-left edge (red, a piece of the line) belongs to the truth set, since there $2x + 3y = 6$ is not $> 6$.*

> [!theorem] Proposition §7.5: Products, Unions and Intersections
> For all sets $A$, $B$, $C$, $D$:
> 1. $A \times (B \cup C) = (A \times B) \cup (A \times C)$;
> 2. $A \times (B \cap C) = (A \times B) \cap (A \times C)$;
> 3. $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$;
> 4. $(A \times B) \cup (C \times D) \subseteq (A \cup C) \times (B \cup D)$.
>
> *Eccles: Proposition 7.7.4*

^prop-7-5

> [!proof]+ Proof
> Each part is proved from the definitions by following an element $(x, y)$; for the equalities both inclusions can be done at once with a chain of equivalences.
>
> (1) $(x, y) \in A \times (B \cup C) \iff x \in A$ and ($y \in B$ or $y \in C$) $\iff$ ($x \in A$ and $y \in B$) or ($x \in A$ and $y \in C$) $\iff (x, y) \in A \times B$ or $(x, y) \in A \times C \iff (x, y) \in (A \times B) \cup (A \times C)$, using the distributive law $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$.
>
> (2) $(x, y) \in A \times (B \cap C) \iff x \in A$ and $y \in B$ and $y \in C \iff (x, y) \in A \times B$ and $(x, y) \in A \times C \iff (x, y) \in (A \times B) \cap (A \times C)$.
>
> (3) $(x, y) \in (A \times B) \cap (C \times D) \iff x \in A$ and $y \in B$ and $x \in C$ and $y \in D \iff x \in A \cap C$ and $y \in B \cap D \iff (x, y) \in (A \cap C) \times (B \cap D)$.
>
> (4) Let $(x, y) \in (A \times B) \cup (C \times D)$. If $(x, y) \in A \times B$, then $x \in A \subseteq A \cup C$ and $y \in B \subseteq B \cup D$, so $(x, y) \in (A \cup C) \times (B \cup D)$. If $(x, y) \in C \times D$, then likewise $x \in C \subseteq A \cup C$ and $y \in D \subseteq B \cup D$.

^pf-7-5

*Uses:* [[§7 Quantifiers#^def-7-5|Def. §7.5]], [[§6 The Language of Set Theory#^def-6-6|Def. §6.6]], [[§6 The Language of Set Theory#^def-6-7|Def. §6.7]], [[§6 The Language of Set Theory#^thm-6-3|§6.3]]

> [!example] Example §7.17: The Inclusion in Part 4 Can Be Strict
> **Claim:** $(A \times B) \cup (C \times D) \subseteq (A \cup C) \times (B \cup D)$, and the two sets need not be equal.
>
> In logical form the inclusion says: for all $x, y$,
>
> $$
> (x \in A \wedge y \in B) \vee (x \in C \wedge y \in D) \ \Rightarrow\ (x \in A \vee x \in C) \wedge (y \in B \vee y \in D).
> $$
>
> Distributing, the left side is equivalent to $(x \in A \vee x \in C) \wedge (x \in A \vee y \in D) \wedge (y \in B \vee x \in C) \wedge (y \in B \vee y \in D)$, a conjunction of four statements whose first and last are the right side; and $P \wedge Q \Rightarrow P$. (This is a second proof of [[§7 Quantifiers#^prop-7-5|§7.5]](4).)
>
> **Counterexample to equality:** take $A = B = \{1\}$ and $C = D = \{2\}$. Then $(A \times B) \cup (C \times D) = \{(1,1), (2,2)\}$, while $(A \cup C) \times (B \cup D) = \{1, 2\}^2$ also contains $(1, 2)$ and $(2, 1)$. In the plane: two squares on the diagonal versus the large square containing them and the two off-diagonal squares.
>
> *Source: HW3*
> *Eccles: Exercise 7.7*

^ex-7-17
