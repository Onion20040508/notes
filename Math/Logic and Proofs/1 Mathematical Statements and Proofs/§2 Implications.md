---
type: section
subject: "[[Logic and Proofs]]"
chapter: 1
section: 2
eccles: "Ch. 2"
aliases: ["Eccles 2"]
tags: [logic-and-proofs, mat250]
---
← [[§1 The Language of Mathematics]] · ↑ [[· 1 Mathematical Statements and Proofs]] · [[§3 Proofs]] →

*Eccles, Chapter 2 (and Problems I Q1, Q5, Q6) · MAT 200 supplement (Helfer) §5 · MAT 200 HW1 (Problems 1, 2, 4) · MAT 200 Quiz 1 · MAT 200 practice midterm 1 (Problems 1–4) · MAT 250 HW2 (Problems I Q5).*

A proof is a chain of statements, each true because earlier ones are; the link between them is implication. This section defines $P \Rightarrow Q$ by its truth table, explains the many ways it is read ("only if", "whenever", "necessary", "sufficient"), introduces the converse, contrapositive and inverse and the biconditional, and collects the logical equivalences that later proofs rely on. It ends with the first definitions of arithmetic (divisibility, even and odd) and the algebraic properties of numbers taken as the starting point.

## 2.1 Implications

> [!definition] Definition §2.1: Implication
> For statements $P$ and $Q$, the **implication** $P \Rightarrow Q$ (read "$P$ implies $Q$", or "if $P$ then $Q$"; also written $Q \Leftarrow P$, and $P \to Q$ in logic) has the truth table
>
> | $P$ | $Q$ | $P \Rightarrow Q$ |
> |:-:|:-:|:-:|
> | T | T | T |
> | T | F | F |
> | F | T | T |
> | F | F | T |
>
> It is false only when $P$ is true and $Q$ is false. $P$ is the **hypothesis** (or antecedent) and $Q$ the **conclusion** (or consequent).
>
> *Eccles: Table 2.1.1*

^def-2-1

> [!example] Example §2.1: Why This Truth Table?
> For an integer $n$, the implication $n > 3 \Rightarrow n > 0$ is certainly true. Write $P(n)$ for $n > 3$ and $Q(n)$ for $n > 0$:
>
> | | $P(n)$ | $Q(n)$ |
> |:-:|:-:|:-:|
> | $n \leq 0$ | F | F |
> | $n = 1, 2, 3$ | F | T |
> | $n > 3$ | T | T |
>
> The values $n = 5$, $n = 2$ and $n = -2$ realize rows 1, 3 and 4 of the table in [[§2 Implications#^def-2-1|Def. §2.1]], and no $n$ makes $P(n)$ true and $Q(n)$ false: that is exactly what "if $P(n)$ is true then $Q(n)$ is true" means. Similarly $n = 1 \Rightarrow (n-1)(n-2) = 0$ is true for every integer $n$: $n = 1$ gives row 1, $n = 2$ row 3, and every other $n$ row 4.
>
> Implication in mathematics carries no idea of causation. Since $3 < \pi < 4$, the table makes
>
> $$
> (\pi < 4) \Rightarrow (1 + 1 = 2), \qquad (\pi < 3) \Rightarrow (1 + 1 = 2), \qquad (\pi < 3) \Rightarrow (1 + 1 = 3)
> $$
>
> true and $(\pi < 4) \Rightarrow (1 + 1 = 3)$ false, although the size of $\pi$ has nothing to do with $1 + 1$.
>
> *Eccles: Section 2.1*

^ex-2-1

> [!remark] Remark: Vacuous Truth
> An implication with a false hypothesis is true whatever its conclusion; it is then called **vacuously** true. For instance "$\sqrt{2}$ is rational only if $2$ is not a perfect square" and "$\sqrt{2}$ is rational only if $2$ is a perfect square" are both true, because $\sqrt{2}$ is not rational (proved in [[§13 Number Systems#^thm-13-4|Theorem §13.4]]). So a proof of $P \Rightarrow Q$ says nothing about $Q$ until $P$ is known to be true: the "proof that $1$ is the largest integer" in [[§4 Proof by Contradiction#^ex-4-6|Ex. §4.6]] proves a vacuous implication.
>
> *Source: MAT 200 lecture (practice midterm 1)*

^rem-2-1

> [!theorem] Proposition §2.1: Negating and Rewriting an Implication
> For statements $P$ and $Q$:
> 1. $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$; we write $P \not\Rightarrow Q$ for this.
> 2. $P \Rightarrow Q \equiv \neg P \vee Q$.
> 3. $P \vee Q \equiv \neg P \Rightarrow Q$.
>
> *Eccles: Section 2.1, Exercise 2.5(ii)*
> *Source: MAT 200 HW1 Problem 1(b)*

^prop-2-1

> [!proof]+ Proof
> (1) Both sides are true in exactly one row of the truth table, the row $P = $ T, $Q = $ F ([[§2 Implications#^def-2-1|Def. §2.1]], [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]]).
>
> (2) Negate both sides of (1): by double negation and De Morgan's law, $P \Rightarrow Q \equiv \neg\neg(P \Rightarrow Q) \equiv \neg(P \wedge \neg Q) \equiv \neg P \vee \neg\neg Q \equiv \neg P \vee Q$.
>
> (3) Apply (2) with $\neg P$ in place of $P$: $\neg P \Rightarrow Q \equiv \neg\neg P \vee Q \equiv P \vee Q$.

^pf-2-1

*Uses:* [[§2 Implications#^def-2-1|Def. §2.1]], [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]]

Part (3) is familiar from speech: "Read the lecture notes or you won't understand the lecture" means "If you don't read the lecture notes, you won't understand the lecture."

### Universal implications

> [!definition] Definition §2.2: Universal Statement; Counterexample
> An implication between predicates, such as $n > 3 \Rightarrow n > 0$ "for integers $n$", is normally asserted as a **universal statement**: it claims that the implication is true for *every* value of the free variable in the stated range (which should be made explicit). It is false precisely when there is at least one value for which the hypothesis is true and the conclusion false; such a value is a **counterexample**. The statement that a counterexample exists, written $P(x) \not\Rightarrow Q(x)$, is an **existence statement**. Quantifiers make this precise in [[§7 Quantifiers|§7]].
>
> *Eccles: Section 2.1*

^def-2-2

> [!example] Example §2.2: The Range of the Variable Matters
> **(a)** For real numbers $x$, consider $x > 0 \Rightarrow x \geq 1$:
>
> | | $x > 0$ | $x \geq 1$ | $x > 0 \Rightarrow x \geq 1$ |
> |:-:|:-:|:-:|:-:|
> | $x \leq 0$ | F | F | T |
> | $0 < x < 1$ | T | F | F |
> | $x \geq 1$ | T | T | T |
>
> The middle row contains counterexamples, for instance $x = \tfrac12$; so $x > 0 \not\Rightarrow x \geq 1$ for real $x$.
>
> **(b)** For integers $n$, however, $n > 0 \Rightarrow n \geq 1$ is true: every integer satisfies $n \leq 0$ or $n \geq 1$ (there is no integer strictly between $0$ and $1$, [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]), and both rows $n \leq 0$ (F, F) and $n \geq 1$ (T, T) give T.
>
> **(c)** Statement (i) of [[§1 The Language of Mathematics#^ex-1-4|Ex. §1.4]] is the universal implication $f(a) = 0 \Rightarrow a > 0$ for real $a$. Its negation says that the implication fails for some real $a$, i.e. by [[§2 Implications#^prop-2-1|Proposition §2.1]](1): $f(a) = 0$ and $a \leq 0$ for some real number $a$. This is statement (viii) there.
>
> *Eccles: Table 2.1.2, Exercise 2.2*

^ex-2-2

*Uses:* [[§2 Implications#^def-2-2|Def. §2.2]], [[§2 Implications#^prop-2-1|§2.1]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]

## Reading Implications

> [!definition] Definition §2.3: Ways of Reading an Implication
> Each of the following means $P \Rightarrow Q$:
> 1. If $P$ then $Q$.
> 2. $P$ implies $Q$.
> 3. $Q$ if $P$.
> 4. $P$ only if $Q$.
> 5. $Q$ whenever $P$.
> 6. $P$ is **sufficient** for $Q$.
> 7. $Q$ is **necessary** for $P$.
>
> In (4), "$P$ only if $Q$" says that $P$ can hold only when $Q$ holds. In (6)–(7), the truth of $P$ suffices to guarantee $Q$, and $P$ cannot be true without $Q$.
>
> *Eccles: Section 2.1*

^def-2-3

> [!definition] Definition §2.4: Converse, Contrapositive, Inverse
> For the implication $P \Rightarrow Q$:
> - its **converse** is $Q \Rightarrow P$;
> - its **contrapositive** is $\neg Q \Rightarrow \neg P$;
> - its **inverse** is $\neg P \Rightarrow \neg Q$.
>
> *Eccles: Section 2.1 (converse), Section 4.3 (contrapositive)*
> *Source: MAT 200 supplement §5 (inverse)*

^def-2-4

> [!theorem] Proposition §2.2: Contrapositive, Converse and Inverse
> For statements $P$ and $Q$:
> 1. An implication is equivalent to its contrapositive: $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$.
> 2. The converse is equivalent to the inverse: $Q \Rightarrow P \equiv \neg P \Rightarrow \neg Q$.
> 3. An implication is *not* equivalent to its converse.
>
> *Eccles: Exercise 2.5(i), Problems I Q1*
> *Source: MAT 200 supplement §5*

^prop-2-2

> [!proof]+ Proof
> The truth table:
>
> | $P$ | $Q$ | $P \Rightarrow Q$ | $\neg Q$ | $\neg P$ | $\neg Q \Rightarrow \neg P$ | $Q \Rightarrow P$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | F | F | T | T |
> | T | F | F | T | F | F | T |
> | F | T | T | F | T | T | F |
> | F | F | T | T | T | T | T |
>
> The third and sixth columns agree, proving (1). Applying (1) to the implication $Q \Rightarrow P$ gives (2). The third and last columns differ in rows 2 and 3, proving (3).

^pf-2-2

*Uses:* [[§2 Implications#^def-2-1|Def. §2.1]], [[§2 Implications#^def-2-4|Def. §2.4]]

> [!example] Example §2.3: Converses and Contrapositives
> **(a)** For integers $n$, $n > 3 \Rightarrow n > 0$ is true but its converse $n > 0 \Rightarrow n > 3$ is false ($n = 1$); $n = 1 \Rightarrow (n-1)(n-2) = 0$ is true but its converse is false ($n = 2$). So "$Q$ if $P$" and "$Q$ only if $P$" must not be confused.
>
> **(b)** In [[§1 The Language of Mathematics#^ex-1-4|Ex. §1.4]](a), statement (v) is the converse of (i), and (iv) and (vi) are converses of each other. The contrapositive of (i), $f(a) = 0 \Rightarrow a > 0$, is $a \leq 0 \Rightarrow f(a) \neq 0$, which is (vii); and (iii), $f(a) = 0 \Rightarrow a \leq 0$, and (vi), $a > 0 \Rightarrow f(a) \neq 0$, are contrapositives of each other. Indeed (i) and (vii) were both false for $f(x) = x^3 - x$, as [[§2 Implications#^prop-2-2|Proposition §2.2]] predicts.
>
> *Eccles: Section 2.1, Problems I Q1*

^ex-2-3

*Uses:* [[§2 Implications#^def-2-4|Def. §2.4]], [[§2 Implications#^prop-2-2|§2.2]]

> [!definition] Definition §2.5: Biconditional
> $P \Leftrightarrow Q$ means $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$. It is read: $P$ is **equivalent** to $Q$; $P$ is necessary and sufficient for $Q$; $P$ **if and only if** $Q$ ($P$ iff $Q$); $P$ precisely when $Q$.
>
> *Eccles: Section 2.1*

^def-2-5

> [!theorem] Proposition §2.3: The Biconditional and Logical Equivalence
> 1. $P \Leftrightarrow Q$ is true exactly when $P$ and $Q$ have the same truth value.
> 2. Two propositional forms $F$ and $G$ are logically equivalent if and only if $F \Leftrightarrow G$ is a tautology.
>
> *Eccles: Exercise 2.3*
> *Source: MAT 200 supplement §1*

^prop-2-3

> [!proof]+ Proof
> (1) From the columns of $P \Rightarrow Q$ and $Q \Rightarrow P$ in the proof of [[§2 Implications#^prop-2-2|Proposition §2.2]], their conjunction has the values T, F, F, T in the rows (T, T), (T, F), (F, T), (F, F): it is true exactly when $P$ and $Q$ agree.
>
> (2) By (1), $F \Leftrightarrow G$ is true for a given assignment exactly when $F$ and $G$ have the same truth value for it. So $F \Leftrightarrow G$ is true for every assignment if and only if $F$ and $G$ agree for every assignment, i.e. $F \equiv G$ ([[§1 The Language of Mathematics#^def-1-5|Def. §1.5]], [[§1 The Language of Mathematics#^def-1-6|Def. §1.6]]).

^pf-2-3

*Uses:* [[§2 Implications#^def-2-5|Def. §2.5]], [[§2 Implications#^prop-2-2|§2.2]], [[§1 The Language of Mathematics#^def-1-5|Def. §1.5]], [[§1 The Language of Mathematics#^def-1-6|Def. §1.6]]

> [!example] Example §2.4: Reading the Same Equation Many Ways
> Since $n^2 - n - 2 = (n - 2)(n + 1)$, for integers $n$ we have $n^2 - n - 2 = 0 \Leftrightarrow (n = 2 \text{ or } n = -1)$ ([[§4 Proof by Contradiction#^prop-4-4|Proposition §4.4]]). Write $E$ for $n^2 - n - 2 = 0$. As universal statements about integers $n$:
>
> | | statement | means | truth |
> |:-:|:--|:--|:-:|
> | (i) | $n = 2$ only if $E$ | $n = 2 \Rightarrow E$ | T |
> | (ii) | $n = 2$ if $E$ | $E \Rightarrow n = 2$ | F ($n = -1$) |
> | (iii) | $n = 2$ is sufficient for $E$ | $n = 2 \Rightarrow E$ | T |
> | (iv) | $n = 2$ is necessary for $E$ | $E \Rightarrow n = 2$ | F ($n = -1$) |
> | (v) | $E \Rightarrow (n = 2 \text{ and } n = -1)$ | | F ($n = 2$) |
> | (vi) | $E \Rightarrow (n = 2 \text{ or } n = -1)$ | | T |
> | (vii) | $E \Leftrightarrow (n = 2 \text{ or } n = -1)$ | | T |
> | (viii) | $E \Leftarrow (n = 2 \text{ and } n = -1)$ | | T (vacuously) |
> | (ix) | $(E \Rightarrow n = 2) \text{ or } (E \Rightarrow n = -1)$ | | F |
> | (x) | $(E \Leftarrow n = 2) \text{ or } (E \Leftarrow n = -1)$ | | T |
> | (xi) | $(E \Leftarrow n = 2) \text{ and } (E \Leftarrow n = -1)$ | | T |
>
> In (viii) the hypothesis is false for every $n$. Statement (ix) is ambiguous: read as "($E \Rightarrow n = 2$ for all $n$) or ($E \Rightarrow n = -1$ for all $n$)" it is false, both universal implications failing (at $n = -1$ and $n = 2$ respectively); read as "for every $n$, ($E \Rightarrow n = 2$) or ($E \Rightarrow n = -1$)" it is true, since for each single $n$ one of the two implications holds. The first reading is the normal one; quantifiers ([[§7 Quantifiers|§7]]) remove the ambiguity.
>
> *Eccles: Exercise 2.1*

^ex-2-4

*Uses:* [[§2 Implications#^def-2-3|Def. §2.3]], [[§2 Implications#^def-2-5|Def. §2.5]], [[§4 Proof by Contradiction#^prop-4-4|§4.4]], [[§2 Implications#^rem-2-1|Remark (vacuous truth)]]

## Logical Forms with Implications

> [!remark] Remark: Order of Operations
> Unless brackets say otherwise, $\neg$ is applied first, then $\wedge$, then $\vee$, then $\Rightarrow$, and $\Leftrightarrow$ last. For instance $P \Rightarrow Q \vee R$ means $P \Rightarrow (Q \vee R)$, and $x^2 = 4 \Rightarrow x = 2 \vee x < 0$ means $x^2 = 4 \Rightarrow (x = 2 \vee x < 0)$.
>
> *Source: MAT 200 lecture (practice midterm 1)*

^rem-2-2

> [!theorem] Proposition §2.4: Equivalences Used in Proofs
> For statements $P$, $Q$, $R$:
> 1. $P \Rightarrow (Q \Rightarrow R) \;\equiv\; (P \wedge Q) \Rightarrow R$.
> 2. $P \Rightarrow (Q \wedge R) \;\equiv\; (P \Rightarrow Q) \wedge (P \Rightarrow R)$.
> 3. $(P \vee Q) \Rightarrow R \;\equiv\; (P \Rightarrow R) \wedge (Q \Rightarrow R)$.
> 4. $P \Rightarrow (Q \vee R) \;\equiv\; (P \wedge \neg Q) \Rightarrow R$.
> 5. $[(P \Rightarrow Q) \wedge (Q \Rightarrow R)] \Rightarrow (P \Rightarrow R)$ is a tautology.
>
> So: to prove an implication with a conjunction as conclusion, prove both implications (2); to prove one with a disjunction as hypothesis, treat each case separately (3); to prove "$P \Rightarrow Q$ or $R$", assume $P$ and not $Q$ and deduce $R$ (4); and implications may be chained (5).
>
> *Eccles: Sections 3.1 and 4.4*
> *Source: MAT 200 HW1 Problem 1(a); Sundstrom §2.2 (Theorem 2.8)*

^prop-2-4

> [!proof]+ Proof
> By [[§2 Implications#^prop-2-1|Proposition §2.1]](2), $X \Rightarrow Y \equiv \neg X \vee Y$; we combine this with the identities of [[§1 The Language of Mathematics#^thm-1-1|Theorem §1.1]].
>
> (1) $P \Rightarrow (Q \Rightarrow R) \equiv \neg P \vee (\neg Q \vee R) \equiv (\neg P \vee \neg Q) \vee R \equiv \neg(P \wedge Q) \vee R \equiv (P \wedge Q) \Rightarrow R$.
>
> (2) $P \Rightarrow (Q \wedge R) \equiv \neg P \vee (Q \wedge R) \equiv (\neg P \vee Q) \wedge (\neg P \vee R) \equiv (P \Rightarrow Q) \wedge (P \Rightarrow R)$, by distributivity.
>
> (3) $(P \vee Q) \Rightarrow R \equiv \neg(P \vee Q) \vee R \equiv (\neg P \wedge \neg Q) \vee R \equiv (\neg P \vee R) \wedge (\neg Q \vee R) \equiv (P \Rightarrow R) \wedge (Q \Rightarrow R)$, by De Morgan, distributivity and commutativity.
>
> (4) $P \Rightarrow (Q \vee R) \equiv \neg P \vee Q \vee R \equiv (\neg P \vee \neg\neg Q) \vee R \equiv \neg(P \wedge \neg Q) \vee R \equiv (P \wedge \neg Q) \Rightarrow R$.
>
> (5) In a row where $P \Rightarrow R$ is false, $P$ is true and $R$ is false. If $Q$ is false there, $P \Rightarrow Q$ is false; if $Q$ is true, $Q \Rightarrow R$ is false. Either way the hypothesis $(P \Rightarrow Q) \wedge (Q \Rightarrow R)$ is false, so the whole implication is true. In every other row its conclusion $P \Rightarrow R$ is true, so again it is true.

^pf-2-4

*Uses:* [[§2 Implications#^prop-2-1|§2.1]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^rem-1-2|Remark (substitution)]]

> [!example] Example §2.5: Equivalences by Truth Tables
> Show by truth tables that the statements in each pair are equivalent: (a) $P \Rightarrow (Q \Rightarrow R)$ and $(P \wedge Q) \Rightarrow R$; (b) $\neg(P \Rightarrow Q)$ and $P \wedge \neg Q$; (c) $P \Rightarrow (P \wedge Q)$ and $P \Rightarrow Q$.
>
> **Solution.** (a)
>
> | $P$ | $Q$ | $R$ | $Q \Rightarrow R$ | $P \Rightarrow (Q \Rightarrow R)$ | $P \wedge Q$ | $(P \wedge Q) \Rightarrow R$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | T | T | T |
> | T | T | F | F | F | T | F |
> | T | F | T | T | T | F | T |
> | T | F | F | T | T | F | T |
> | F | T | T | T | T | F | T |
> | F | T | F | F | T | F | T |
> | F | F | T | T | T | F | T |
> | F | F | F | T | T | F | T |
>
> (b)
>
> | $P$ | $Q$ | $P \Rightarrow Q$ | $\neg(P \Rightarrow Q)$ | $\neg Q$ | $P \wedge \neg Q$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | F | F | F |
> | T | F | F | T | T | T |
> | F | T | T | F | F | F |
> | F | F | T | F | T | F |
>
> (c)
>
> | $P$ | $Q$ | $P \wedge Q$ | $P \Rightarrow (P \wedge Q)$ | $P \Rightarrow Q$ |
> |:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | T |
> | T | F | F | F | F |
> | F | T | F | T | T |
> | F | F | F | T | T |
>
> In each table the two columns being compared agree in every row, so the statements are equivalent. ((a) and (b) are also [[§2 Implications#^prop-2-4|Proposition §2.4]](1) and [[§2 Implications#^prop-2-1|Proposition §2.1]](1).)
>
> *Source: MAT 200 HW1 Problem 1*

^ex-2-5

*Uses:* [[§2 Implications#^def-2-1|Def. §2.1]], [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]]

> [!example] Example §2.6: Tautologies and an Absurdity
> **(a)** $(P \wedge \neg Q) \Rightarrow (P \vee Q)$ is a tautology. In a row where $P$ is false the hypothesis $P \wedge \neg Q$ is false, so the implication is true; in a row where $P$ is true the conclusion $P \vee Q$ is true, so the implication is true.
>
> **(b)** By the same reasoning $P \Rightarrow (P \vee Q)$ and $(P \wedge Q) \Rightarrow P$ are tautologies, and so is $P \Rightarrow (Q \Rightarrow P)$: if $P$ is true then $Q \Rightarrow P$ is true, and if $P$ is false the outer implication is vacuously true.
>
> **(c)** $(P \wedge \neg P) \vee (Q \wedge \neg Q)$ is an absurdity: both disjuncts are contradictions ([[§1 The Language of Mathematics#^thm-1-2|Theorem §1.2]]), so in every row both are false, and so is their disjunction.
>
> *Source: MAT 200 HW1 Problem 2; MAT 200 Quiz 1 Problem 2*
> *Eccles: Exercise 2.4*

^ex-2-6

*Uses:* [[§2 Implications#^def-2-1|Def. §2.1]], [[§1 The Language of Mathematics#^def-1-6|Def. §1.6]], [[§1 The Language of Mathematics#^thm-1-2|§1.2]]

> [!example] Example §2.7: Order of Operations and a Tautology
> Indicate the order of operations in
>
> $$
> P \Rightarrow Q \vee R \Leftrightarrow P \wedge \neg R \Rightarrow Q,
> $$
>
> and decide whether it is a tautology, a contradiction, or neither.
>
> **Solution.** By the order of operations the steps are: (1) $\neg R$; (2) $P \wedge \neg R$; (3) $Q \vee R$; (4) $P \Rightarrow (Q \vee R)$; (5) $(P \wedge \neg R) \Rightarrow Q$; (6) the $\Leftrightarrow$ between (4) and (5). Rewriting both sides with $X \Rightarrow Y \equiv \neg X \vee Y$:
>
> $$
> P \Rightarrow (Q \vee R) \equiv \neg P \vee Q \vee R, \qquad (P \wedge \neg R) \Rightarrow Q \equiv \neg(P \wedge \neg R) \vee Q \equiv \neg P \vee R \vee Q.
> $$
>
> The two sides are equivalent, so by [[§2 Implications#^prop-2-3|Proposition §2.3]](2) the form is a **tautology**. (This is [[§2 Implications#^prop-2-4|Proposition §2.4]](4) with $Q$ and $R$ interchanged.)
>
> *Source: MAT 200 practice midterm 1 Problem 1*

^ex-2-7

*Uses:* [[§2 Implications#^rem-2-2|Remark (order of operations)]], [[§2 Implications#^prop-2-1|§2.1]], [[§2 Implications#^prop-2-3|§2.3]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]]

## Converse, Inverse, Contrapositive and Conditions in Practice

> [!example] Example §2.8: Converse, Inverse and Contrapositive
> Let $a, b$ be real numbers and let $S$ be: *if $a + b > 0$, then $a > 0$ and $b > 0$.* Write down the converse, inverse and contrapositive, and decide which of the four statements are true.
>
> **Solution.** By [[§2 Implications#^def-2-4|Def. §2.4]] and De Morgan's law ($\neg(a > 0 \wedge b > 0) \equiv a \leq 0 \vee b \leq 0$):
>
> | | statement | truth |
> |:--|:--|:-:|
> | $S$ | $a + b > 0 \Rightarrow (a > 0 \wedge b > 0)$ | F |
> | converse | $(a > 0 \wedge b > 0) \Rightarrow a + b > 0$ | T |
> | inverse | $a + b \leq 0 \Rightarrow (a \leq 0 \vee b \leq 0)$ | T |
> | contrapositive | $(a \leq 0 \vee b \leq 0) \Rightarrow a + b \leq 0$ | F |
>
> $S$ is false: $a = 2$, $b = -1$ give $a + b = 1 > 0$ but $b < 0$; the same values refute the contrapositive, as they must ([[§2 Implications#^prop-2-2|Proposition §2.2]]). The converse is true: if $a > 0$ and $b > 0$ then $a + b > 0 + b = b > 0$ by the addition and transitive laws ([[§3 Proofs#^def-3-1|Def. §3.1]]). The inverse is equivalent to the converse, so it is true as well.
>
> *Source: MAT 200 HW1 Problem 4*

^ex-2-8

*Uses:* [[§2 Implications#^def-2-4|Def. §2.4]], [[§2 Implications#^prop-2-2|§2.2]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§3 Proofs#^def-3-1|Def. §3.1]]

> [!example] Example §2.9: "Only If" and "Whenever"
> Let $x$ be a real number and consider: *$x^2 = 4$ only if $x = 2$ or $x < 0$.*
> (a) Write it in symbols, indicating the order of operations. (b) Rewrite it using "whenever". (c) Give a useful denial. (d) Is it true?
>
> **Solution.** (a) "$P$ only if $Q$" is $P \Rightarrow Q$, so the statement is $x^2 = 4 \Rightarrow (x = 2 \vee x < 0)$: first the disjunction, then the implication.
>
> (b) "$x = 2$ or $x < 0$ whenever $x^2 = 4$."
>
> (c) By [[§2 Implications#^prop-2-1|Proposition §2.1]](1) and De Morgan's law,
>
> $$
> \neg\bigl(x^2 = 4 \Rightarrow (x = 2 \vee x < 0)\bigr) \equiv x^2 = 4 \wedge \neg(x = 2 \vee x < 0) \equiv x^2 = 4 \wedge x \neq 2 \wedge x \geq 0.
> $$
>
> (As a universal statement about all real $x$, its denial asserts that *some* $x$ satisfies $x^2 = 4$, $x \neq 2$ and $x \geq 0$.)
>
> (d) True. $x^2 = 4 \iff (x - 2)(x + 2) = 0 \iff x = 2$ or $x = -2$ ([[§4 Proof by Contradiction#^prop-4-4|Proposition §4.4]]). If $x = 2$ the conclusion holds; if $x = -2$ then $x < 0$ and it holds again. Equivalently, the denial has no solution: $x^2 = 4$ forces $x = \pm 2$, and $x \neq 2$, $x \geq 0$ exclude both.
>
> *Source: MAT 200 practice midterm 1 Problem 2*

^ex-2-9

*Uses:* [[§2 Implications#^def-2-3|Def. §2.3]], [[§2 Implications#^prop-2-1|§2.1]], [[§1 The Language of Mathematics#^def-1-7|Def. §1.7]], [[§4 Proof by Contradiction#^prop-4-4|§4.4]]

That the negation of "for all $x$, $P(x)$" is "for some $x$, not $P(x)$" is [[§7 Quantifiers#^thm-7-2|Theorem §7.2]], where denials of quantified statements are treated systematically.

> [!example] Example §2.10: A Necessary Condition for Convergence
> Calculus proves: *if a series $\sum_{n=1}^\infty a_n$ converges, then $\lim_{n \to \infty} a_n = 0$.*
>
> (a) This is $P \Rightarrow Q$ with $P$ "$\sum a_n$ converges" and $Q$ "$a_n \to 0$", so $a_n \to 0$ is a **necessary** condition for convergence ([[§2 Implications#^def-2-3|Def. §2.3]]).
>
> (b) The contrapositive: *if $a_n$ does not tend to $0$, then $\sum a_n$ diverges* (the "divergence test"). It is true, being equivalent to the theorem ([[§2 Implications#^prop-2-2|Proposition §2.2]]). Note that $\neg Q$ includes the case where $\lim a_n$ does not exist.
>
> (c) The converse: *if $a_n \to 0$, then $\sum a_n$ converges.* False: the harmonic series $\sum 1/n$ diverges although $1/n \to 0$.
>
> (d) The inverse: *if $\sum a_n$ diverges, then $a_n$ does not tend to $0$.* False, being equivalent to the converse; the harmonic series is again a counterexample.
>
> *Source: MAT 200 practice midterm 1 Problem 3*

^ex-2-10

*Uses:* [[§2 Implications#^def-2-3|Def. §2.3]], [[§2 Implications#^def-2-4|Def. §2.4]], [[§2 Implications#^prop-2-2|§2.2]]

> [!remark]- Connections
> - The theorem and the counterexample are proved in analysis: [[§14 Series#^cor-14-2|451 Cor. §14.2]] (terms of a convergent series tend to zero) and [[§14 Series#^thm-14-5|451 Thm. §14.5]] (divergence of the harmonic series).

> [!example] Example §2.11: Conditions for a Parallelogram
> A convex quadrilateral is a **parallelogram** if both pairs of opposite sides are parallel.
> - *Sufficient but not necessary:* "it is a rectangle". Every rectangle is a parallelogram, but a parallelogram with an angle other than a right angle is not a rectangle.
> - *Necessary but not sufficient:* "it has a pair of parallel opposite sides". Every parallelogram has one, but a trapezoid with exactly one such pair is not a parallelogram.
> - *Necessary and sufficient:* "both pairs of opposite sides are parallel" (the definition). Classical theorems of Euclidean geometry give others, such as "one pair of opposite sides is parallel and of equal length" and "the diagonals bisect each other".
>
> *Source: MAT 200 practice midterm 1 Problem 4*

^ex-2-11

*Uses:* [[§2 Implications#^def-2-3|Def. §2.3]], [[§2 Implications#^def-2-5|Def. §2.5]]

## 2.2 Arithmetic

When we meet a new word, or a familiar word in a new setting, we must find out what the writer means by it, not decide how we might have defined it. Here is a familiar example.

> [!definition] Definition §2.6: Divisibility
> For integers $a$ and $b$, we say that **$b$ divides $a$**, or **$a$ is a multiple of $b$**, written $b \mid a$, if there is an integer $q$ such that $a = bq$. For example $3 \mid 6$ since $6 = 3 \times 2$, $-14 \mid 28$ since $28 = (-14)(-2)$, and $b \mid 0$ for every integer $b$ since $0 = b \times 0$.
>
> *Eccles: Definition 2.2.1*

^def-2-6

> [!remark]- Connections
> - The same definition in group theory, where it leads to congruences and $\mathbb{Z}/n\mathbb{Z}$: [[§6 Divisibility and Congruence#^def-6-1|493 Def. §6.1]].

> [!definition] Definition §2.7: Even and Odd
> An integer $a$ is **even** if $2$ divides $a$, and **odd** if it is not even.
>
> *Eccles: Definitions 2.2.2 and 2.2.3*

^def-2-7

The definition of "odd" uses that of "even", which uses that of "divides": to use a definition one works back through the chain.

> [!theorem] Proposition §2.5: 101 Is Odd
> $101$ is an odd integer.
>
> *Eccles: Proposition 2.2.4*

^prop-2-5

> [!proof]+ Proof
> By [[§2 Implications#^def-2-7|Def. §2.7]], "$101$ is odd" means "$101$ is not even", i.e. $2$ does not divide $101$, i.e. ([[§2 Implications#^def-2-6|Def. §2.6]]) there is no integer $q$ with $2q = 101$. We cannot check the integers one at a time, but every integer $q$ satisfies $q \leq 50$ or $q \geq 51$, since no integer lies strictly between $50$ and $51$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]). Multiplying by $2 > 0$ ([[§3 Proofs#^def-3-1|Def. §3.1]]), either $2q \leq 100$ or $2q \geq 102$, and in both cases $2q \neq 101$. Hence $101$ is not even, so it is odd.

^pf-2-5

*Uses:* [[§2 Implications#^def-2-6|Def. §2.6]], [[§2 Implications#^def-2-7|Def. §2.7]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]], [[§3 Proofs#^def-3-1|Def. §3.1]]

The proof rests on the two universal implications $q \leq 50 \Rightarrow 2q \leq 100$ and $q \geq 51 \Rightarrow 2q \geq 102$; a second proof, by contradiction, is in [[§4 Proof by Contradiction#^ex-4-1|Ex. §4.1]]. (Arguing "$101/2 = 50\tfrac12$ is not an integer" is also valid, but uses the rational numbers.)

> [!example] Example §2.12: Necessary and Sufficient Conditions for Divisibility by 6
> Which of the following conditions are necessary, and which sufficient, for a positive integer $n$ to be divisible by $6$?
> (i) $3 \mid n$; (ii) $9 \mid n$; (iii) $12 \mid n$; (iv) $n = 12$; (v) $6 \mid n^2$; (vi) $2 \mid n$ and $3 \mid n$; (vii) $2 \mid n$ or $3 \mid n$.
>
> **Solution.** A condition $C$ is necessary when $6 \mid n \Rightarrow C$ and sufficient when $C \Rightarrow 6 \mid n$; a single counterexample refutes either implication.
>
> | | necessary | sufficient |
> |:-:|:-:|:-:|
> | (i) $3 \mid n$ | yes | no ($n = 3$) |
> | (ii) $9 \mid n$ | no ($n = 6$) | no ($n = 9$) |
> | (iii) $12 \mid n$ | no ($n = 6$) | yes |
> | (iv) $n = 12$ | no ($n = 6$) | yes |
> | (v) $6 \mid n^2$ | yes | yes |
> | (vi) $2 \mid n$ and $3 \mid n$ | yes | yes |
> | (vii) $2 \mid n$ or $3 \mid n$ | yes | no ($n = 2$) |
>
> *Necessity.* If $n = 6k$ then $n = 3(2k) = 2(3k)$, giving (i), (vi) and hence (vii); and $n^2 = 6(6k^2)$, giving (v).
>
> *Sufficiency.* (iii): $n = 12k = 6(2k)$; (iv): $12 = 6 \times 2$. (vi): if $n = 2a$ and $n = 3b$, then $b = 3b - 2b = 2a - 2b = 2(a - b)$, so $n = 3b = 6(a - b)$. (v): suppose $6 \mid n^2$, say $n^2 = 6k$; then $n^2 = 2(3k) = 3(2k)$, so $2 \mid n^2$ and $3 \mid n^2$. An integer whose square is even is even ([[§4 Proof by Contradiction#^ex-4-2|Ex. §4.2]](b)), so $2 \mid n$. For $3$: from $n^2 = 3c$ we get $n^3 = n \cdot n^2 = 3(nc)$, and $n^3 - n = 3d$ for an integer $d$ since $n$ is a positive integer ([[§5 The Induction Principle#^ex-5-1|Ex. §5.1]](a)); hence $n = n^3 - (n^3 - n) = 3(nc - d)$, and $3 \mid n$. Now (vi) gives $6 \mid n$.
>
> *Source: HW2*
> *Eccles: Problems I Q5*

^ex-2-12

*Uses:* [[§2 Implications#^def-2-3|Def. §2.3]], [[§2 Implications#^def-2-6|Def. §2.6]], [[§4 Proof by Contradiction#^ex-4-2|Ex. §4.2]], [[§5 The Induction Principle#^ex-5-1|Ex. §5.1]]

Once the division theorem is available, the step $3 \mid n^2 \Rightarrow 3 \mid n$ also follows by dividing $n$ by $3$ and squaring the possible remainders: [[§15 The Division Theorem#^prop-15-3|Proposition §15.3]].

## 2.3 Mathematical Truth

Proofs must start somewhere. Euclid's *Elements* began from axioms regarded as self-evident truths; in the modern view, axioms are simply statements assumed to be true, and mathematics explores what follows from them by accepted rules of deduction. (The discovery of non-Euclidean geometries in the nineteenth century showed that different axiom systems can be equally valid.) Developing arithmetic formally from axioms would be cumbersome here: we take the basic algebraic properties of numbers for granted, and state the order properties as axioms in [[§3 Proofs#^def-3-1|Def. §3.1]]. The positive integers have a particularly simple axiom system, Peano's axioms ([[§9 Injections, Surjections and Bijections#^def-9-6|Def. §9.6]]), one of which is the induction principle of [[§5 The Induction Principle#^def-5-1|Def. §5.1]].

> [!definition] Definition §2.8: Algebraic Properties of the Real Numbers
> Any two real numbers $a, b$ have a **sum** $a + b$ and a **product** $ab$ (also $a \cdot b$, $a \times b$), which are real numbers, and:
> 1. *Commutativity.* $a + b = b + a$ and $ab = ba$.
> 2. *Associativity.* $(a + b) + c = a + (b + c)$ and $(ab)c = a(bc)$.
> 3. *Distributivity.* $a(b + c) = ab + ac$ and $(a + b)c = ac + bc$.
> 4. *Zero.* $a + 0 = a = 0 + a$.
> 5. *Unity.* $a \times 1 = a = 1 \times a$.
> 6. *Subtraction.* The equation $a + x = 0$ has the unique solution $x = -a$, so $a + x = b \Leftrightarrow x = b + (-a) = b - a$. (We can cancel: $a + x_1 = a + x_2 \Rightarrow x_1 = x_2$.)
> 7. *Division.* If $a \neq 0$, the equation $ax = b$ has the unique solution $x = b/a = ba^{-1}$. (We can cancel: $ax_1 = ax_2 \Rightarrow x_1 = x_2$ when $a \neq 0$.)
>
> We also take for granted that $0 \neq 1$. Sums, products and differences of integers are integers; $b/a$ is an integer only if $a \mid b$. Rational numbers are closed under all four operations (division by non-zero numbers).
>
> *Eccles: Properties 2.3.1*

^def-2-8

> [!remark]- Connections
> - These are the field axioms: [[§3 The Set ℝ of Real Numbers#^def-3-1|451 Def. §3.1]]. In Eccles's terms, $\mathbb{Q}$ and $\mathbb{R}$ are fields and $\mathbb{Z}$ is an integral domain.

> [!example] Example §2.13: Multiplying by Zero and the Rule of Signs
> For all real numbers $a$ and $b$: (i) $a \times 0 = 0 = 0 \times a$; (ii) $(-a)b = -(ab) = a(-b)$; (iii) $(-a)(-b) = ab$.
>
> **Solution.** (i) By zero and distributivity, $a \times 0 + a \times 0 = a(0 + 0) = a \times 0 = a \times 0 + 0$; cancelling $a \times 0$ (property 6) gives $a \times 0 = 0$, and $0 \times a = a \times 0$ by commutativity.
>
> (ii) $ab + (-a)b = (a + (-a))b = 0 \times b = 0$ by (i), so $(-a)b$ solves $ab + x = 0$, whose unique solution is $-(ab)$. Likewise $ab + a(-b) = a(b + (-b)) = a \times 0 = 0$ gives $a(-b) = -(ab)$.
>
> (iii) By (ii) twice, $(-a)(-b) = -(a(-b)) = -(-(ab))$. For any $c$, $-(-c) = c$, since $c$ solves $(-c) + x = 0$, whose unique solution is $-(-c)$. Hence $(-a)(-b) = ab$.
>
> *Eccles: Problems I Q6*

^ex-2-13

*Uses:* [[§2 Implications#^def-2-8|Def. §2.8]]
