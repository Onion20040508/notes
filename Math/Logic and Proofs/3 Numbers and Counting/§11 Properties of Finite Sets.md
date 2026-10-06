---
type: section
subject: "[[Logic and Proofs]]"
chapter: 3
section: 11
eccles: "Ch. 11"
aliases: ["Eccles 11"]
tags: [logic-and-proofs, mat250]
---
← [[§10 Counting]] · ↑ [[· 3 Numbers and Counting]] · [[§12★ Counting Functions and Subsets]] →

*Eccles, Chapter 11 and Problems III (Q5, Q9–Q11, Q14) · MAT 200 lecture (syllabus week 14).*

Finite sets allow two special kinds of argument: an element with a property can be found by testing the elements one at a time, a search that must end; and a "counting argument" can show that an element with a property exists without looking at any element individually. This section first recalls the lemma that §10 proves ([[§10 Counting#^lem-10-2|Lemma §10.2]]), which is the pigeonhole principle in disguise, then shows that finite sets of real numbers have a greatest and a least element, and uses this to define the greatest common divisor and to write odd integers as $2q + 1$.

## 11.1 The Pigeonhole Principle

The key step in showing that cardinality is well defined was [[§10 Counting#^lem-10-2|Lemma §10.2]]: *if there is an injection $\N_m \to \N_n$, then $m \le n$.* Its proof, which Eccles gives at the start of Chapter 11, is given with the lemma in §10: [[§10 Counting#^pf-10-2|proof of Lemma §10.2]].

The lemma passes at once from the standard sets $\N_n$ to arbitrary finite sets, by composing with bijections.

> [!theorem] Corollary §11.1: Injections Between Finite Sets
> Let $X$ and $Y$ be non-empty finite sets. If there is an injection $f : X \to Y$, then $|X| \le |Y|$.
>
> *Eccles: Corollary 11.1.1*

^cor-11-1

> [!proof]+ Proof
> Let $|X| = m$ and $|Y| = n$, with bijections $g_1 : \N_m \to X$ and $g_2 : \N_n \to Y$. Then $g_2^{-1} \circ f \circ g_1 : \N_m \to X \to Y \to \N_n$ is a composite of injections, hence an injection, and Lemma [[§10 Counting#^lem-10-2|§10.2]] gives $m \le n$.

^pf-11-1

*Uses:* [[§10 Counting#^lem-10-2|§10.2]], [[§9 Injections, Surjections and Bijections#^ex-9-8|Ex. §9.8]]

For example, if a group of people sit in a room on separate chairs, the number of people is at most the number of chairs. The contrapositive is the form usually quoted; Dirichlet called it the "drawer principle".

> [!theorem] Theorem §11.2: The Pigeonhole Principle
> Let $f : X \to Y$ be a function between non-empty finite sets with $|X| > |Y|$. Then $f$ is not an injection: there are distinct $x_1, x_2 \in X$ with $f(x_1) = f(x_2)$.
>
> *Eccles: Theorem 11.1.2*
> *Source: MAT 200 lecture (syllabus week 14)*

^thm-11-2

> [!proof]+ Proof
> This is the contrapositive of Corollary [[§11 Properties of Finite Sets#^cor-11-1|§11.1]].

^pf-11-2

*Uses:* [[§11 Properties of Finite Sets#^cor-11-1|§11.1]]

The same statement holds for infinite sets, with $|X| > |Y|$ in the sense of [[§14 Counting Infinite Sets#^def-14-3|Definition §14.3]]; there it is the Cantor–Schröder–Bernstein theorem in disguise ([[§14 Counting Infinite Sets#^cor-14-15|Corollary §14.15]]).

> [!remark]- Connections
> - The pigeonhole principle in group theory: every element of a finite group has finite order, [[§4 Subgroups#^prop-4-8|493 Prop. §4.8]] (and its remark on where finiteness enters).

> [!example] Example §11.1: Birthdays and Friends
> (a) In any group of more than twelve people, two have their birthdays in the same month: apply the pigeonhole principle to the function sending each person to the month of their birthday.
>
> (b) In a set $X$ of $n \ge 2$ people, two have the same number of friends in $X$ (friendship being mutual). Let $f : X \to \{0, 1, \ldots, n - 1\}$ send $x$ to the number of friends of $x$ in $X$. If $n - 1$ is a value of $f$, say $f(x_0) = n - 1$, then $x_0$ is a friend of everyone else and nobody has $0$ friends. So the distinct numbers $0$ and $n - 1$ are not both values of $f$, and $f$ is really a function into a set of $n - 1$ numbers ($\{0, \ldots, n-2\}$ or $\{1, \ldots, n-1\}$). Since $|X| = n > n - 1$, the pigeonhole principle gives $x_1 \ne x_2$ with $f(x_1) = f(x_2)$.
>
> *Eccles: Examples 11.1.3*

^ex-11-1

*Uses:* [[§11 Properties of Finite Sets#^thm-11-2|§11.2]]

> [!example] Example §11.2: A Divisor Pair
> Let $n \in \Z^+$ and let $A \subseteq \N_{2n}$ with $|A| = n + 1$. Then $A$ contains distinct $a, b$ with $a \mid b$.
>
> Every positive integer factors as $a = 2^k c$ with $k \ge 0$ and $c$ odd, $c$ being the greatest odd divisor of $a$. Let $f(a) = c$. For $a \in \N_{2n}$, $f(a)$ is an odd number in $\N_{2n}$, and there are exactly $n$ of these, $1, 3, \ldots, 2n - 1$. Since $|A| = n + 1 > n$, the pigeonhole principle gives $a \ne b$ in $A$ with the same odd part $c$: $a = 2^k c$ and $b = 2^l c$ with $k \ne l$. If $k < l$ then $b = 2^{l-k} a$, so $a \mid b$; if $l < k$ then $b \mid a$. The bound is sharp: $\{n + 1, n + 2, \ldots, 2n\}$ has $n$ elements and no such pair.
>
> *Eccles: Problems III Q14*

^ex-11-2

*Uses:* [[§11 Properties of Finite Sets#^thm-11-2|§11.2]]

Mimicking the proof of Lemma [[§10 Counting#^lem-10-2|§10.2]] gives a version in which the domain is not known in advance to be finite.

> [!theorem] Proposition §11.3: Sets That Inject into a Finite Set
> If $f : X \to \N_n$ is an injection, then $X$ is finite and $|X| \le n$.
>
> *Eccles: Proposition 11.1.4 (proof: Problems III Q9)*

^prop-11-3

> [!proof]+ Proof
> If $X = \emptyset$ then $X$ is finite with $|X| = 0 \le n$, so let $X \ne \emptyset$. Induction on $n$, the statement being the proposition for all sets $X$.
>
> *Base case $n = 1$.* All values of $f$ are $1$, so injectivity allows only one element: $X = \{x\}$, and $1 \mapsto x$ is a bijection $\N_1 \to X$. So $|X| = 1$.
>
> *Inductive step.* Suppose the result holds for $n = k$ and let $f : X \to \N_{k+1}$ be injective. (i) If $k + 1$ is not a value of $f$, then $f$ is an injection $X \to \N_k$, so $X$ is finite with $|X| \le k < k + 1$. (ii) If $f(x_0) = k + 1$, then for $x \ne x_0$ we have $f(x) \ne k + 1$, so $f$ restricts to an injection $X - \{x_0\} \to \N_k$. By the inductive hypothesis $X - \{x_0\}$ is finite with $|X - \{x_0\}| \le k$, and since $X = (X - \{x_0\}) \cup \{x_0\}$ is a disjoint union, the addition principle gives that $X$ is finite with $|X| = |X - \{x_0\}| + 1 \le k + 1$.

^pf-11-3

*Uses:* [[§10 Counting#^thm-10-4|§10.4]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

The following is intuitively obvious, but a proof has to rest on the definitions.

> [!theorem] Corollary §11.4: Subsets of Finite Sets
> If $X \subseteq Y$ and $Y$ is finite, then $X$ is finite and $|X| \le |Y|$.
>
> *Eccles: Corollary 11.1.5*

^cor-11-4

> [!proof]+ Proof
> If $Y = \emptyset$ then $X = \emptyset$. Otherwise let $|Y| = n$ and $f : \N_n \to Y$ a bijection. The inclusion $i : X \to Y$, $i(x) = x$, is injective, so $f^{-1} \circ i : X \to \N_n$ is injective, and Proposition [[§11 Properties of Finite Sets#^prop-11-3|§11.3]] shows that $X$ is finite with $|X| \le n$.

^pf-11-4

*Uses:* [[§11 Properties of Finite Sets#^prop-11-3|§11.3]], [[§9 Injections, Surjections and Bijections#^thm-9-2|§9.2]], [[§9 Injections, Surjections and Bijections#^ex-9-8|Ex. §9.8]]

> [!theorem] Corollary §11.5: Proper Subsets Are Smaller
> Let $X \subseteq Y$ with $Y$ finite. Then $X = Y$ if and only if $|X| = |Y|$, and $X \ne Y$ if and only if $|X| < |Y|$.
>
> *Eccles: Exercise 11.5*

^cor-11-5

> [!proof]+ Proof
> $X$ and $Y - X$ are finite by Corollary [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], and $Y = X \cup (Y - X)$ is a disjoint union, so $|Y| = |X| + |Y - X|$ by the addition principle. Now $X = Y$ iff $Y - X = \emptyset$ iff $|Y - X| = 0$ iff $|X| = |Y|$; and otherwise $|Y - X| \ge 1$, so $|X| < |Y|$.

^pf-11-5

*Uses:* [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], [[§10 Counting#^thm-10-4|§10.4]]

So a finite set is never equipotent to a proper subset of itself; [[§14 Counting Infinite Sets#^thm-14-3|Theorem §14.3]] shows that this property characterizes finite sets.

The results so far concern injectivity; there are matching results for surjectivity.

> [!theorem] Theorem §11.6: No Surjection onto a Larger Set
> Let $f : X \to Y$ be a function between non-empty finite sets with $|X| < |Y|$. Then $f$ is not a surjection: some element of $Y$ is not a value of $f$.
>
> *Eccles: Theorem 11.1.6 (proof: Problems III Q10)*

^thm-11-6

> [!proof]+ Proof
> We show that a surjection $f : X \to Y$ forces $|Y| \le |X|$, by building an injection $Y \to X$. Let $|X| = m$ and $h : \N_m \to X$ a bijection. For $y \in Y$ the set $\{ i \in \N_m \mid f(h(i)) = y \}$ is a non-empty set of positive integers, because $f$ and $h$ are surjective; let $i_y$ be its least element (the well-ordering principle, [[§5 The Induction Principle#^cor-5-7|Corollary §5.7]]) and put $g(y) = h(i_y)$. Then $f(g(y)) = y$ for every $y$, so $g(y_1) = g(y_2)$ implies $y_1 = f(g(y_1)) = f(g(y_2)) = y_2$: $g : Y \to X$ is an injection. By Corollary [[§11 Properties of Finite Sets#^cor-11-1|§11.1]], $|Y| \le |X|$. Contrapositively, if $|X| < |Y|$ then $f$ is not a surjection.

^pf-11-6

*Uses:* [[§11 Properties of Finite Sets#^cor-11-1|§11.1]], [[§5 The Induction Principle#^cor-5-7|§5.7]] (well-ordering)

If two finite sets are known to have the same size, checking that a function between them is a bijection takes half the work.

> [!theorem] Theorem §11.7: Injective Iff Surjective for Equal Sizes
> Let $X$ and $Y$ be non-empty finite sets with $|X| = |Y|$. Then a function $f : X \to Y$ is an injection if and only if it is a surjection. So to prove that $f$ is a bijection it suffices to check one of injectivity and surjectivity.
>
> *Eccles: Theorem 11.1.7 (proof: Problems III Q11)*

^thm-11-7

> [!proof]+ Proof
> Let $|X| = |Y| = n$.
>
> ($\Rightarrow$) Suppose $f$ is injective but not surjective, say $y_0 \in Y$ is not a value. Then $f$ is an injection $X \to Y - \{y_0\}$, and $Y - \{y_0\}$ is finite ([[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]) with $|Y - \{y_0\}| = n - 1$ by the addition principle. If $n = 1$ this set is empty, and there is no function from the non-empty $X$ into it; if $n \ge 2$, then $|X| = n > n - 1$ and the pigeonhole principle says $f$ is not injective. Either way, a contradiction.
>
> ($\Leftarrow$) Suppose $f$ is surjective but not injective, say $f(x_1) = f(x_2)$ with $x_1 \ne x_2$. Then the restriction of $f$ to $X - \{x_2\}$ is still surjective, because the value $f(x_2)$ is also taken at $x_1$. Here $|X - \{x_2\}| = n - 1$, as before. If $n = 1$ then $X - \{x_2\} = \emptyset$ cannot map onto the non-empty $Y$; if $n \ge 2$, Theorem [[§11 Properties of Finite Sets#^thm-11-6|§11.6]] says no function from a set of $n - 1$ elements onto $Y$ exists. Either way, a contradiction.

^pf-11-7

*Uses:* [[§11 Properties of Finite Sets#^thm-11-2|§11.2]], [[§11 Properties of Finite Sets#^thm-11-6|§11.6]], [[§10 Counting#^thm-10-4|§10.4]], [[§11 Properties of Finite Sets#^cor-11-4|§11.4]]

> [!remark]- Connections
> - The linear-algebra twin: a linear map between spaces of the same finite dimension is injective iff surjective, [[Injectivity is equivalent to surjectivity (if dim V = dim W ＜ ∞)|LADR 3.65]]; dimension plays the role of cardinality. Both fail for infinite sets ($n \mapsto n + 1$ on $\Z^+$ is injective and not surjective).
> - Matrix version: for a square matrix, one-to-one iff onto, part of the Invertible Matrix Theorem [[§13 Characterizations of Invertible Matrices#^thm-13-1|235 Thm. §13.1]].

## 11.2 Finite Sets of Real Numbers

When we look for an element of a finite set with some property, each element can be tested in turn and the search ends. A typical case is looking for the greatest element of a set of real numbers. Some sets of numbers have none (the integers, $\Z^+$); every finite non-empty one does.

> [!definition] Definition §11.1: Minimum and Maximum
> Let $A \subseteq \R$. Then $b$ is a **minimum element** of $A$, written $b = \min A$, when
> 1. $b \in A$, and
> 2. $b$ is less than or equal to every element of $A$: $a \in A \Rightarrow b \le a$.
>
> Similarly $c$ is a **maximum element** of $A$, $c = \max A$, when $c \in A$ and $a \in A \Rightarrow c \ge a$.
>
> *Eccles: Definition 11.2.1*

^def-11-1

> [!theorem] Proposition §11.8: Uniqueness of the Maximum
> A set of real numbers has at most one maximum element and at most one minimum element. So $\max A$ and $\min A$, when they exist, are well defined.
>
> *Eccles: Exercise 11.2*

^prop-11-8

> [!proof]+ Proof
> If $c_1$ and $c_2$ are maximum elements of $A$, then $c_1 \ge c_2$ because $c_1$ is a maximum and $c_2 \in A$, and $c_2 \ge c_1$ likewise; so $c_1 = c_2$. The same argument works for minima.

^pf-11-8

*Uses:* [[§11 Properties of Finite Sets#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - In 451: [[§4 The Completeness Axiom#^def-4-1|451 Def. §4.1]] and [[§4 The Completeness Axiom#^prop-4-1|451 Prop. §4.1]]; for infinite bounded sets the maximum is replaced by the supremum, [[§4 The Completeness Axiom#^def-4-3|451 Def. §4.3]].

> [!example] Example §11.3: Maxima and Minima
> (a) For $A = \{-1, 17, 12, -78, 8\}$, $\min A = -78$ and $\max A = 17$.
>
> (b) $\min \Z^+ = 1$, but $\Z^+$ has no maximum element.
>
> (c) Every non-empty set of positive integers has a minimum element. This is the **well-ordering principle**, proved from induction in [[§5 The Induction Principle#^cor-5-7|Corollary §5.7]] (Eccles Exercise 11.6); conversely it implies the induction principle (Problems III Q15), so the two are equivalent.
>
> (d) The set $\R^+ = \{ x \in \R \mid x > 0 \}$ has no minimum and no maximum: given $a \in \R^+$, $a/2 \in \R^+$ is smaller and $2a$ is larger.
>
> *Eccles: Examples 11.2.2*

^ex-11-3

*Uses:* [[§5 The Induction Principle#^cor-5-7|§5.7]]

> [!theorem] Proposition §11.9: Finite Sets Have a Maximum and a Minimum
> Every finite non-empty set $A$ of real numbers has a minimum element and a maximum element.
>
> *Eccles: Proposition 11.2.3 (minimum: Problems III Q5)*

^prop-11-9

The statement mentions no integer, but there is one hidden in it: $|A|$. The informal search ("compare $a_1$ with $a_2$, keep the larger, compare with $a_3$, and so on") becomes an induction on $|A|$. The hypothesis "non-empty" matters: $\emptyset$ is finite and has neither.

> [!proof]+ Proof
> We prove by induction on $n \in \Z^+$ that every set of real numbers with $n$ elements has a maximum; this is the proposition, since a finite non-empty set has $n$ elements for some $n \in \Z^+$.
>
> For $n = 1$ the single element is the maximum. Suppose all sets of $k$ real numbers have a maximum and let $A = \{a_1, \ldots, a_k, a_{k+1}\}$ have $k + 1$ elements. By the inductive hypothesis $A' = \{a_1, \ldots, a_k\}$ has a maximum $a'$. If $a' \ge a_{k+1}$ then $a'$ is the maximum of $A$; if $a' < a_{k+1}$ then $a_{k+1}$ is, since it exceeds $a'$ and hence every element of $A'$. Either way $A$ has a maximum, completing the induction.
>
> The minimum is found by the same induction with the inequalities reversed (or: $\min A = -\max\{-a \mid a \in A\}$).

^pf-11-9

*Uses:* [[§11 Properties of Finite Sets#^def-11-1|Def. §11.1]], [[§5 The Induction Principle#^def-5-1|Def. §5.1]]

## 11.3 Two Applications of Finiteness

### The greatest common divisor

Recall ([[§2 Implications#^def-2-6|Definition §2.6]]) that $d$ **divides** $a$, $d \mid a$, when $a = dq$ for some integer $q$; then $d$ is a **divisor** or **factor** of $a$ and $a$ is a **multiple** of $d$. Here, as in Eccles, divisors are taken non-zero; every non-zero integer divides $0$. If $a \ne 0$ and $a = dq$, then $q \ne 0$, so $|q| \ge 1$ and $|a| \ge |d|$. Hence for $a \ne 0$ the set of divisors

$$
D(a) = \{ n \in \Z \mid n \text{ divides } a \}
$$

is finite, with $\min D(a) = -|a|$ and $\max D(a) = |a|$. For integers $a, b$ not both zero, the common divisors form $D(a) \cap D(b)$, a finite set (a subset of $D(a)$ or $D(b)$, whichever argument is non-zero, [[§11 Properties of Finite Sets#^cor-11-4|Corollary §11.4]]) containing $1$. By Proposition [[§11 Properties of Finite Sets#^prop-11-9|§11.9]] it has a maximum.

> [!definition] Definition §11.2: Greatest Common Divisor
> Let $a$ and $b$ be integers, at least one of them non-zero. The **greatest common divisor** (or highest common factor) of $a$ and $b$ is the unique positive integer $d$ such that
> 1. $d$ is a common divisor: $d \mid a$ and $d \mid b$, and
> 2. $d$ is greater than every other common divisor: $c \mid a$ and $c \mid b$ $\Rightarrow$ $c \le d$.
>
> It is written $\gcd(a, b)$. (Eccles writes simply $(a, b)$, which could be confused with an ordered pair or an interval; these notes use $\gcd(a, b)$ throughout.)
>
> *Eccles: Definition 11.3.1*

^def-11-2

> [!definition] Definition §11.3: Coprime
> Integers $a$ and $b$, not both zero, are **coprime** (or **relatively prime**) when $\gcd(a, b) = 1$: their only common factors are $1$ and $-1$.
>
> *Eccles: Definition 11.3.2*

^def-11-3

> [!remark]- Connections
> - In 493: [[§8 Invertibility and Unit Groups#^def-8-1|493 Def. §8.1]]. The computation of gcds by the Euclidean algorithm is [[§16 The Euclidean Algorithm#^thm-16-3|Theorem §16.3]].

> [!example] Example §11.4: A gcd by Listing Divisors
> $$
> \begin{aligned}
> D(30) &= \{\pm 1, \pm 2, \pm 3, \pm 5, \pm 6, \pm 10, \pm 15, \pm 30\}, \\
> D(72) &= \{\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 8, \pm 9, \pm 12, \pm 18, \pm 24, \pm 36, \pm 72\},
> \end{aligned}
> $$
>
> so the common divisors are $D(30) \cap D(72) = \{\pm 1, \pm 2, \pm 3, \pm 6\}$ and $\gcd(30, 72) = 6$.
>
> *Eccles: Example 11.3.3*

^ex-11-4

*Chain: later in [[§18b The Pair (72, 30)|Chapter 4]]*

> [!theorem] Proposition §11.10: Dividing Out the gcd
> If $a$ and $b$ are non-zero integers with $\gcd(a, b) = d$, then $a/d$ and $b/d$ are coprime.
>
> *Eccles: Exercise 11.4*

^prop-11-10

> [!proof]+ Proof
> Let $c$ be a positive common divisor of $a/d$ and $b/d$: $a/d = cq$ and $b/d = cq'$ with $q, q' \in \Z$. Then $a = (cd)q$ and $b = (cd)q'$, so $cd$ is a common divisor of $a$ and $b$, and $cd \le d$ by the definition of $d$. Since $d > 0$, $c \le 1$. So the greatest common divisor of $a/d$ and $b/d$ is $1$.

^pf-11-10

*Uses:* [[§11 Properties of Finite Sets#^def-11-2|Def. §11.2]], [[§11 Properties of Finite Sets#^def-11-3|Def. §11.3]]

This is what puts fractions in lowest terms in [[§13 Number Systems#^prop-13-2|Proposition §13.2]].

### Odd and even integers

"Odd" was defined to mean "not divisible by $2$" ([[§2 Implications#^def-2-7|Definition §2.7]]). The familiar description of odd numbers as $2q + 1$ is a special case of the division theorem, proved later as [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]], and finiteness gives a direct proof now.

> [!theorem] Proposition §11.11: Odd Integers
> An integer $a$ is odd if and only if $a = 2q + 1$ for some integer $q$.
>
> *Eccles: Proposition 11.3.4*

^prop-11-11

> [!proof]+ Proof
> *Sufficiency.* Let $a = 2q + 1$ with $q \in \Z$, and suppose for contradiction that $a$ is even, $a = 2p$. Then $2p = 2q + 1$, so $1 = 2(p - q)$; as $p - q$ is an integer, either $p - q \le 0$ and $2(p-q) \le 0$, or $p - q \ge 1$ and $2(p - q) \ge 2$. Neither equals $1$. So $a$ is odd.
>
> *Necessity.* The difficulty is to get hold of $q$. One way to construct an element is as the maximum of a finite set: in practice one doubles integers until getting as close to $a$ as possible.
>
> (a) Let $a$ be a positive odd integer and
>
> $$
> A = \{ k \in \Z \mid k \ge 0 \text{ and } a \ge 2k \}.
> $$
>
> $A$ is non-empty since $0 \in A$, and finite since $k \in A \Rightarrow 0 \le k \le 2k \le a$, so $A \subseteq \{0, 1, \ldots, a\}$. Let $q = \max A$. Since $q \in A$, $a \ge 2q$; since $a$ is odd, $a \ne 2q$; so $a \ge 2q + 1$. Since $q + 1 \notin A$ (it exceeds the maximum) and $q + 1 \ge 0$, we have $a < 2(q + 1) = 2q + 2$, so $a \le 2q + 1$. Hence $a = 2q + 1$.
>
> (b) If $a$ is a negative odd integer, then $-a$ is a positive odd integer, so $-a = 2q_1 + 1$ by (a), and $a = -2q_1 - 1 = 2(-q_1 - 1) + 1$. Take $q = -q_1 - 1$.

^pf-11-11

*Uses:* [[§11 Properties of Finite Sets#^prop-11-9|§11.9]], [[§11 Properties of Finite Sets#^cor-11-4|§11.4]], [[§2 Implications#^def-2-7|Def. §2.7]]

> [!remark]- Connections
> - The general statement, $a = bq + r$ with $0 \le r < b$, is [[§15 The Division Theorem#^thm-15-1|Theorem §15.1]]; in 493 it is the [[§6 Divisibility and Congruence#^lem-6-1|493 Lemma §6.1]] (Division Algorithm), proved there by well-ordering, the infinite counterpart of taking a maximum.
