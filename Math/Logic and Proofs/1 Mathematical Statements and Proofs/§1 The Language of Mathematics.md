---
type: section
subject: "[[Logic and Proofs]]"
chapter: 1
section: 1
eccles: "Ch. 1"
aliases: ["Eccles 1"]
tags: [logic-and-proofs, mat250]
---
↑ [[· 1 Mathematical Statements and Proofs]] · [[§2 Implications]] →

*Eccles, Chapter 1 (and the notation of Section 6.1) · MAT 200 supplement (Helfer) §1–§4 · MAT 200 Quiz 1 · MAT 200 HW1 (Problem 6) · MAT 200 practice midterm 1.*

Mathematics proceeds by formulating statements and deciding whether they are true. This section fixes what a statement is, how compound statements are built from simpler ones with the connectives "or", "and" and "not", and how their truth values are computed by truth tables. It then develops the algebra of connectives taught in the MAT 200 lectures: logical equivalence, tautologies and contradictions, De Morgan's laws, negation, and the conjunctive and disjunctive normal forms. Implication, the connective that drives proofs, is the subject of [[§2 Implications|§2]].

## Notation for Numbers

> [!definition] Definition §1.1: Number Sets
> Throughout this subject:
> - $\mathbb{Z}$ is the set of all **integers** $\ldots, -2, -1, 0, 1, 2, \ldots$;
> - $\mathbb{Z}^+ = \{1, 2, 3, \ldots\}$ is the set of **positive integers**;
> - $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$ is the set of **non-negative integers** (Eccles writes $\mathbb{Z}^{\geq}$);
> - $\mathbb{Q}$ is the set of **rational numbers** (fractions), $\mathbb{R}$ the set of **real numbers** (infinite decimals), and $\mathbb{C}$ the set of **complex numbers**;
> - $\mathbb{R}^+ = \{x \in \mathbb{R} \mid x > 0\}$ and $\mathbb{R}^{\geq} = \{x \in \mathbb{R} \mid x \geq 0\}$ are the positive and the non-negative reals.
>
> We write $x \in A$ for "$x$ is an element of $A$" (sets are the subject of [[§6 The Language of Set Theory|§6]]). As in Eccles, letters from the middle of the alphabet ($k, m, n, q$) usually denote integers and letters from the end ($x, y$) real numbers.
>
> *Eccles: Section 6.1; Section 2.1*

^def-1-1

> [!remark] Remark: Which Natural Numbers?
> Some authors include $0$ among the natural numbers and some do not, and Eccles avoids the phrase for this reason, saying "positive integers" ($\mathbb{Z}^+$) or "non-negative integers" ($\mathbb{Z}^{\geq}$). In these notes $\mathbb{N}$ always means $\{0, 1, 2, \ldots\}$, the convention of logic and set theory, and $\mathbb{Z}^+$ means $\{1, 2, 3, \ldots\}$. Single Variable Analysis (MAT 451, following Ross) writes $\mathbb{N} = \{1, 2, 3, \ldots\}$, which is $\mathbb{Z}^+$ here: see [[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]].

^rem-1-1

## 1.1 Mathematical Statements

> [!definition] Definition §1.2: Proposition, Predicate, Statement
> A **proposition** is a sentence which is either true or false, but not both. A **predicate** is a sentence containing one or more symbols, its **free variables**, which becomes a proposition whenever values are assigned to them; we write $P(n)$ or $P(m, n)$, listing the free variables. A **statement** is a proposition or a predicate; capital letters $P, Q, R$ denote statements. "True" and "false" (T and F) are the two **truth values**.
>
> *Eccles: Section 1.1*

^def-1-2

> [!example] Example §1.1: Recognizing Statements
> In the following list, (i)–(v) are propositions, (vi)–(viii) are predicates, and (ix)–(x) are not statements.
> 1. $1 + 1 = 2$ — a true proposition.
> 2. $\pi = 3$ — a false proposition.
> 3. $12$ may be written as the sum of two primes — true, since $12 = 5 + 7$. (A **prime** is an integer greater than $1$ divisible only by $1$ and itself; see [[§23 The Sequence of Prime Numbers|§23]].)
> 4. Every even integer greater than $2$ is the sum of two primes — a proposition whose truth value is unknown (the **Goldbach conjecture**, 1742).
> 5. The square of every even integer is even — true; it is proved in [[§3 Proofs#^ex-3-3|Ex. §3.3]].
> 6. $n$ is a prime number — a predicate: true for $n = 2$ and $n = 3$, false for $n = 4$.
> 7. $n^2 - 2n > 0$ — a predicate: false for $n = 2$, true for $n = 3$.
> 8. $m < n$ — a predicate with two free variables: true for $m = 2, n = 3$, false for $m = 3, n = 2$.
> 9. "$12 - 11$." — not a sentence.
> 10. "$\pi$ is a special number" — meaningless until "special" is given a technical meaning, as "prime" and "even" have been.
>
> *Eccles: Section 1.1*

^ex-1-1

## 1.2 Logical Connectives

> [!definition] Definition §1.3: Disjunction, Conjunction, Negation
> For statements $P$ and $Q$, the **disjunction** "$P$ or $Q$" ($P \vee Q$), the **conjunction** "$P$ and $Q$" ($P \wedge Q$) and the **negation** "not $P$" ($\neg P$) have the truth values
>
> | $P$ | $Q$ | $P \vee Q$ | $P \wedge Q$ |
> |:-:|:-:|:-:|:-:|
> | T | T | T | T |
> | T | F | T | F |
> | F | T | T | F |
> | F | F | F | F |
>
> | $P$ | $\neg P$ |
> |:-:|:-:|
> | T | F |
> | F | T |
>
> So $P \vee Q$ is true when at least one of $P, Q$ is true: mathematical "or" is always **inclusive**, never the "one or the other but not both" of everyday speech. $P \wedge Q$ is true exactly when both are true, and $\neg P$ has the opposite truth value to $P$.
>
> *Eccles: Tables 1.2.1 and 1.2.2, Exercise 1.1*

^def-1-3

> [!example] Example §1.2: Hidden Connectives
> Connectives are often hidden in notation.
> - $a \leq b$ is shorthand for "$a < b$ or $a = b$". So $1 \leq 2$ and $2 \leq 2$ are both true, while for $(a, b) = (2, 1)$ and $(-2, 1)$ the statement $a \leq b$ is false and true respectively.
> - $a = \pm b$ is shorthand for "$a = b$ or $a = -b$": it asserts that at least one of two equalities holds, not that a single one does. Thus "if $x^2 = 1$ then $x = \pm 1$" is true while "if $x^2 = 1$ then $x = 1$" is false. (See the table below, whose last column is read off from the two before it by the table for "or".)
> - $3 < \pi < 4$ is shorthand for "$\pi > 3$ and $\pi < 4$", a conjunction.
>
> | $a$ | $b$ | $a = b$ | $a = -b$ | $a = \pm b$ |
> |:-:|:-:|:-:|:-:|:-:|
> | $1$ | $2$ | F | F | F |
> | $1$ | $1$ | T | F | T |
> | $2$ | $-2$ | F | T | T |
> | $0$ | $0$ | T | T | T |
>
> *Eccles: Section 1.2, Exercise 1.3*

^ex-1-2

> [!definition] Definition §1.4: Absolute Value
> The **absolute value** (or modulus) of a real number $a$ is
>
> $$
> |a| = \begin{cases} \ a & \text{if } a \geq 0, \\ \ -a & \text{if } a \leq 0. \end{cases}
> $$
>
> The two cases overlap only at $a = 0$, where both give $0$, so $|a|$ is well defined; in either case $|a| \geq 0$. The statement $a = \pm b$ can be written as the single equation $|a| = |b|$.
>
> *Eccles: Section 1.2*

^def-1-4

> [!remark]- Connections
> - The same definition in analysis, with the triangle inequality and $|ab| = |a||b|$: [[§3 The Set ℝ of Real Numbers#^def-3-4|451 Def. §3.4]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 Thm. §3.3]].

> [!example] Example §1.3: The Square of the Absolute Value
> For every real number $a$, $|a|^2 = a^2$.
>
> **Solution.** If $a \geq 0$ then $|a| = a$ and $|a|^2 = a^2$. If $a \leq 0$ then $|a| = -a$ and $|a|^2 = (-a)^2 = a^2$ by the rule of signs ([[§2 Implications#^ex-2-13|Ex. §2.13]]). Every real $a$ satisfies $a \geq 0$ or $a \leq 0$, so $|a|^2 = a^2$ always.
>
> *Eccles: Exercise 1.5*

^ex-1-3

*Uses:* [[§1 The Language of Mathematics#^def-1-4|Def. §1.4]], [[§2 Implications#^ex-2-13|Ex. §2.13]]

The negation of a statement is obtained by inserting "not", but this needs care, since everyday speech uses "not" loosely.

> [!example] Example §1.4: Negations Need Care
> **(a)** Let $f(x)$ be a polynomial with real coefficients and consider the statement (i) *For real numbers $a$, if $f(a) = 0$ then $a$ is positive*, and the candidate negations:
> - (ii) for real $a$, if $f(a) = 0$ then $a$ is negative;
> - (iii) for real $a$, if $f(a) = 0$ then $a$ is non-positive;
> - (iv) for real $a$, if $f(a) \neq 0$ then $a$ is positive;
> - (v) for real $a$, if $a$ is positive then $f(a) = 0$;
> - (vi) for real $a$, if $a$ is positive then $f(a) \neq 0$;
> - (vii) for real $a$, if $a$ is non-positive then $f(a) \neq 0$;
> - (viii) for some non-positive real number $a$, $f(a) = 0$.
>
> Only (viii) is the negation: a negation must have the opposite truth value to (i) for *every* $f$. For $f(x) = x^3 - x = x(x+1)(x-1)$, statement (i) is false, since $f(0) = 0$ but $0$ is not positive. Its negation must then be true, and (viii) is (take $a = 0$), whereas each of (ii)–(vii) is false for this $f$: (ii) and (iii) fail at $a = 1$, (iv) at $a = -2$, (v) at $a = 2$, (vi) at $a = 1$ and (vii) at $a = 0$. The negation of (i) is analysed formally in [[§2 Implications#^ex-2-2|Ex. §2.2]].
>
> **(b)** The negation of (i) *All girls are good at mathematics* is (v) *Some girl is not good at mathematics*, not (ii) *All girls are bad at mathematics*, (iii) *All girls are not good at mathematics* or (iv) *Some girl is bad at mathematics*: "bad" is stronger than "not good", and "all girls are not good" denies the statement for every girl rather than for one. Statement (vii) *All children who are not good at mathematics are boys* has the same meaning as (i) (every child being a boy or a girl), while (vi) *All children who are good at mathematics are girls* does not.
>
> *Eccles: Example 1.2.3, Exercise 1.4*

^ex-1-4

## Logical Equivalence

The MAT 200 lectures supplemented Chapter 1 with an algebra of the connectives, in which statements are manipulated like algebraic expressions.

> [!definition] Definition §1.5: Propositional Form; Logical Equivalence
> A **propositional form** is an expression such as $A \wedge (B \vee \neg C)$ built by connectives from **propositional variables** $A, B, C, \ldots$, which stand for arbitrary statements. Each assignment of truth values to its variables gives the form a truth value, computed from the tables of [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]]; the **truth table** of a form in $k$ variables lists all $2^k$ assignments. Two forms $F$ and $G$ are **logically equivalent**, written $F \equiv G$, if they have the same truth value for every assignment; such an equivalence is called a **logical identity**.
>
> Two individual propositions are called logically equivalent when they have the same truth value. This is a weak notion ("the square of every even number is even" and "$1 + 1 = 2$" are equivalent merely because both are true); it becomes interesting for predicates, which may be equivalent for every value of the free variable ("$x^2$ is even" and "$(x+1)^2$ is odd", for integers $x$), and for propositional forms.
>
> *Source: MAT 200 supplement §1; Sundstrom §2.2*

^def-1-5

> [!theorem] Theorem §1.1: Logical Identities
> For all propositional forms $A$, $B$, $C$:
> 1. *Commutativity.* $A \wedge B \equiv B \wedge A$ and $A \vee B \equiv B \vee A$.
> 2. *Associativity.* $A \wedge (B \wedge C) \equiv (A \wedge B) \wedge C$ and $A \vee (B \vee C) \equiv (A \vee B) \vee C$.
> 3. *Idempotence.* $A \wedge A \equiv A$ and $A \vee A \equiv A$.
> 4. *Distributivity.* $A \wedge (B \vee C) \equiv (A \wedge B) \vee (A \wedge C)$ and $A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)$.
> 5. *Double negation.* $\neg(\neg A) \equiv A$.
> 6. *De Morgan's laws.* $\neg(A \wedge B) \equiv \neg A \vee \neg B$ and $\neg(A \vee B) \equiv \neg A \wedge \neg B$.
>
> *Source: MAT 200 supplement §1; MAT 200 Quiz 1; Sundstrom §2.2 (Theorems 2.5 and 2.8)*
> *Eccles: Exercise 1.2*

^thm-1-1

> [!proof]+ Proof
> By [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]], a conjunction is true exactly when both parts are true, and a disjunction exactly when at least one part is true. We check, for each identity, that the two sides are true for the same assignments.
>
> (1)–(3): Both sides of each conjunction identity are true exactly when all the forms involved are true; both sides of each disjunction identity are true exactly when at least one of them is true.
>
> (4): $A \wedge (B \vee C)$ is true $\iff$ $A$ is true and at least one of $B, C$ is true $\iff$ ($A$ and $B$ are true) or ($A$ and $C$ are true) $\iff$ $(A \wedge B) \vee (A \wedge C)$ is true. Dually, $A \vee (B \wedge C)$ is false $\iff$ $A$ is false and at least one of $B, C$ is false $\iff$ $A \vee B$ is false or $A \vee C$ is false $\iff$ $(A \vee B) \wedge (A \vee C)$ is false.
>
> (5): Negating twice reverses the truth value twice.
>
> (6): The truth table for the first law:
>
> | $A$ | $B$ | $A \wedge B$ | $\neg(A \wedge B)$ | $\neg A$ | $\neg B$ | $\neg A \vee \neg B$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | F | F | F | F |
> | T | F | F | T | F | T | T |
> | F | T | F | T | T | F | T |
> | F | F | F | T | T | T | T |
>
> The fourth and seventh columns agree. For the second law: $\neg(A \vee B)$ is true $\iff$ $A \vee B$ is false $\iff$ $A$ and $B$ are both false $\iff$ $\neg A \wedge \neg B$ is true.

^pf-1-1

*Uses:* [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]], [[§1 The Language of Mathematics#^def-1-5|Def. §1.5]]

> [!remark] Remark: Substitution
> The truth value of a compound form depends only on the truth values of its parts. Hence replacing a part of a form by a logically equivalent form gives a logically equivalent form, and the identities of [[§1 The Language of Mathematics#^thm-1-1|Theorem §1.1]] may be used exactly like the laws of algebra. By associativity, brackets in repeated conjunctions and disjunctions may be dropped: $A \wedge B \wedge C$, $A_1 \vee A_2 \vee \cdots \vee A_k$. A conjunction of several forms is true exactly when all of them are, a disjunction exactly when at least one is, and De Morgan's laws extend to several terms: $\neg(A_1 \wedge \cdots \wedge A_k) \equiv \neg A_1 \vee \cdots \vee \neg A_k$ and $\neg(A_1 \vee \cdots \vee A_k) \equiv \neg A_1 \wedge \cdots \wedge \neg A_k$.
>
> *Source: MAT 200 supplement §1*

^rem-1-2

> [!definition] Definition §1.6: Tautology and Contradiction
> A propositional form is a **tautology** if it is true for every assignment of truth values to its variables, and a **contradiction** (or **absurdity**) if it is false for every assignment. We write $\top$ for a fixed tautology (or any true statement) and $\bot$ for a fixed contradiction (or any false statement).
>
> *Source: MAT 200 supplement §2; Sundstrom §2.1*

^def-1-6

> [!theorem] Theorem §1.2: Excluded Middle, Non-Contradiction, Identity and Annihilation
> For every propositional form $A$:
> 1. $A \vee \neg A$ is a tautology (*law of the excluded middle*).
> 2. $A \wedge \neg A$ is a contradiction (*law of non-contradiction*, or *law of consistency*).
> 3. $A \wedge \top \equiv A$ and $A \vee \bot \equiv A$ (*identity laws*).
> 4. $A \wedge \bot \equiv \bot$ and $A \vee \top \equiv \top$ (*annihilation laws*).
>
> *Source: MAT 200 supplement §2*

^thm-1-2

> [!proof]+ Proof
> For every assignment exactly one of $A$, $\neg A$ is true ([[§1 The Language of Mathematics#^def-1-3|Def. §1.3]]). So $A \vee \neg A$ always has a true part and is true, and $A \wedge \neg A$ always has a false part and is false. Since $\top$ is always true, $A \wedge \top$ is true exactly when $A$ is, and $A \vee \top$ is always true; since $\bot$ is always false, $A \vee \bot$ is true exactly when $A$ is, and $A \wedge \bot$ is always false.

^pf-1-2

*Uses:* [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]], [[§1 The Language of Mathematics#^def-1-6|Def. §1.6]]

A contradiction $P \wedge \neg P$ is what a proof by contradiction aims to reach: [[§4 Proof by Contradiction#^def-4-1|Def. §4.1]].

## Negation and Normal Forms

> [!definition] Definition §1.7: Denial
> A **denial** of a statement $P$ is any statement logically equivalent to its negation $\neg P$. A **useful denial** (a denial "in affirmative terms") is one in which negation is applied only to the simplest component statements and, where possible, absorbed into them: $\neg(x < 0)$ becomes $x \geq 0$, and $\neg(x = 2)$ becomes $x \neq 2$.
>
> *Source: MAT 200 supplement §3; MAT 200 lecture (practice midterm 1)*

^def-1-7

> [!example] Example §1.5: Denying a Compound Statement
> Let $P$ be $A \wedge (\neg B \vee C)$. By De Morgan's laws and double negation ([[§1 The Language of Mathematics#^thm-1-1|Theorem §1.1]]),
>
> $$
> \neg P \equiv \neg A \vee \neg(\neg B \vee C) \equiv \neg A \vee (\neg\neg B \wedge \neg C) \equiv \neg A \vee (B \wedge \neg C).
> $$
>
> So a denial of "Ottawa is the capital of Canada and (the Earth does not revolve around the sun or helium is heavier than hydrogen)" is "Ottawa is not the capital of Canada or (the Earth revolves around the sun and helium is not heavier than hydrogen)".
>
> *Source: MAT 200 supplement §3*

^ex-1-5

*Uses:* [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^rem-1-2|Remark (substitution)]]

> [!definition] Definition §1.8: Disjunctive and Conjunctive Normal Form
> A **literal** is a propositional variable or the negation of one. A propositional form is in **disjunctive normal form (DNF)** if it is a disjunction of conjunctions of literals, and in **conjunctive normal form (CNF)** if it is a conjunction of disjunctions of literals. (A single conjunction or disjunction, or a single literal, counts as a one-term case.) For example
>
> $$
> (A \wedge B \wedge \neg D) \vee (A \wedge \neg C) \vee (B \wedge C \wedge D) \quad \text{(DNF)}, \qquad (A \vee B \vee \neg D) \wedge (A \vee \neg C) \wedge (B \vee C \vee D) \quad \text{(CNF)}.
> $$
>
> *Source: MAT 200 supplement §4*

^def-1-8

> [!theorem] Theorem §1.3: Existence of Normal Forms
> Every propositional form is logically equivalent to a form in disjunctive normal form and to a form in conjunctive normal form.
>
> *Source: MAT 200 supplement §4; standard*

^thm-1-3

> [!proof]+ Proof
> Let $F$ be a form in the variables $A_1, \ldots, A_k$. For each assignment (row) $r$ of truth values to $A_1, \ldots, A_k$, let $C_r = L_1 \wedge \cdots \wedge L_k$, where $L_i = A_i$ if $A_i$ is true in $r$ and $L_i = \neg A_i$ if $A_i$ is false in $r$. Every $L_i$ is true in row $r$, and in any other row some $A_i$ has the other value, making $L_i$ false; so $C_r$ is true in row $r$ and in no other row.
>
> *DNF.* If $F$ is true in at least one row, let $D$ be the disjunction of the $C_r$ over all rows $r$ in which $F$ is true. Then $D$ is true in a row $s$ $\iff$ some $C_r$ in $D$ is true in $s$ $\iff$ $s$ is one of these rows $\iff$ $F$ is true in $s$. So $F \equiv D$, which is in DNF. If $F$ is true in no row, then $F \equiv A_1 \wedge \neg A_1$ ([[§1 The Language of Mathematics#^thm-1-2|Theorem §1.2]]), which is in DNF.
>
> *CNF.* Apply the DNF case to $\neg F$: $\neg F \equiv \bigvee_r (L_{r,1} \wedge \cdots \wedge L_{r,k})$. Negating both sides and using double negation and De Morgan's laws for several terms,
>
> $$
> F \equiv \neg\neg F \equiv \bigwedge_r \bigl(\neg L_{r,1} \vee \cdots \vee \neg L_{r,k}\bigr),
> $$
>
> and each $\neg L_{r,i}$ is $\neg A_i$ or $\neg\neg A_i \equiv A_i$, a literal. This is in CNF.

^pf-1-3

*Uses:* [[§1 The Language of Mathematics#^def-1-8|Def. §1.8]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^thm-1-2|§1.2]], [[§1 The Language of Mathematics#^rem-1-2|Remark (substitution)]]

> [!remark] Remark: Computing Normal Forms by Rewriting
> The construction in the proof is often long. In practice one rewrites: (i) push negations inwards with De Morgan's laws, (ii) remove double negations, (iii) distribute $\wedge$ over $\vee$ (for DNF) or $\vee$ over $\wedge$ (for CNF). For example
>
> $$
> A \wedge (B \vee \neg(\neg C \vee D)) \equiv A \wedge (B \vee (\neg\neg C \wedge \neg D)) \equiv A \wedge (B \vee (C \wedge \neg D)) \equiv (A \wedge B) \vee (A \wedge C \wedge \neg D),
> $$
>
> by De Morgan, double negation and distributivity; the result is in DNF.
>
> *Source: MAT 200 supplement §4*

^rem-1-3

> [!example] Example §1.6: CNF and DNF of a Form
> Reduce $(A \wedge B) \vee \neg(\neg C \wedge D)$ to disjunctive and to conjunctive normal form.
>
> **Solution.** By De Morgan's law and double negation,
>
> $$
> (A \wedge B) \vee \neg(\neg C \wedge D) \equiv (A \wedge B) \vee (\neg\neg C \vee \neg D) \equiv (A \wedge B) \vee C \vee \neg D,
> $$
>
> which is in DNF, with the three disjuncts $A \wedge B$, $C$ and $\neg D$. Distributing $\vee$ over $\wedge$,
>
> $$
> (A \wedge B) \vee (C \vee \neg D) \equiv \bigl(A \vee C \vee \neg D\bigr) \wedge \bigl(B \vee C \vee \neg D\bigr),
> $$
>
> which is in CNF.
>
> *Source: MAT 200 HW1 Problem 6*

^ex-1-6

*Uses:* [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^def-1-8|Def. §1.8]]

> [!theorem] Corollary §1.4: Every Truth Table Comes from Not, And, Or
> 1. A propositional form in $k$ variables has one of $2^{2^k}$ possible truth tables, and every one of them is the truth table of a form built from $\neg$, $\wedge$, $\vee$ alone. In particular there are exactly $2^4 = 16$ binary connectives, and each is expressible by $\neg$, $\wedge$, $\vee$.
> 2. Writing $P \uparrow Q$ for "$P$ notand $Q$", that is $\neg(P \wedge Q)$,
>
> $$
> \neg P \equiv P \uparrow P, \qquad P \wedge Q \equiv (P \uparrow Q) \uparrow (P \uparrow Q), \qquad P \vee Q \equiv (P \uparrow P) \uparrow (Q \uparrow Q),
> $$
>
> so every truth table is realized by a form using the single connective $\uparrow$.
>
> *Source: MAT 200 lecture (practice midterm 1)*
> *Eccles: Problems I Q3*

^cor-1-4

> [!proof]+ Proof
> (1) A truth table in $k$ variables has $2^k$ rows, and in each row the value is T or F, giving $2^{2^k}$ tables; for $k = 2$ this is $2^4 = 16$. Given any table, the construction in the proof of [[§1 The Language of Mathematics#^thm-1-3|Theorem §1.3]] (the disjunction of the $C_r$ over the rows marked T, or $A_1 \wedge \neg A_1$ if there are none) produces a form in $\neg, \wedge, \vee$ with exactly that table.
>
> (2) By idempotence, $P \uparrow P = \neg(P \wedge P) \equiv \neg P$. Hence $(P \uparrow Q) \uparrow (P \uparrow Q) \equiv \neg(P \uparrow Q) = \neg\neg(P \wedge Q) \equiv P \wedge Q$, and by De Morgan $(P \uparrow P) \uparrow (Q \uparrow Q) \equiv \neg(\neg P \wedge \neg Q) \equiv \neg\neg P \vee \neg\neg Q \equiv P \vee Q$. Substituting these into a form from (1) gives a form in $\uparrow$ alone.

^pf-1-4

*Uses:* [[§1 The Language of Mathematics#^thm-1-3|§1.3]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^rem-1-2|Remark (substitution)]]
