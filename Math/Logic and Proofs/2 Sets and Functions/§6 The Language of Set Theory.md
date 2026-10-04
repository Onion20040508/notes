---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: 6
eccles: "Ch. 6"
aliases: ["Eccles 6"]
tags: [logic-and-proofs, mat250]
---
← [[§5 The Induction Principle]] · ↑ [[· 2 Sets and Functions]] · [[§7 Quantifiers]] →

*Eccles, Chapter 6 · MAT 250 HW3 (Exercises 6.1, 6.3, 6.4, 6.6) · MAT 200 HW1 (Problem 5).*

This section sets up the vocabulary of sets that the rest of the subject is written in: how sets are specified, when two sets are equal, subsets, and the operations of intersection, union, difference and complement. Each operation is defined by a logical connective ([[§1 The Language of Mathematics|§1]]), so every identity between sets comes from a logical equivalence between statements. The proofs in this section show the three ways of proving such identities: truth tables, element-chasing, and algebra with identities already proved.

## 6.1 Sets

> [!definition] Definition §6.1: Set and Element
> A **set** is a well-defined collection of objects, its **elements** (or **members**, or **points**). We write $x \in E$ for the statement that $x$ is an element of the set $E$, and $x \notin E$ for its negation. A set is a single mathematical object; it may itself be an element of another set.
>
> *Eccles: Section 6.1*

^def-6-1

The standard sets of numbers, $\Z$, $\Z^+$, $\N = \{0, 1, 2, \ldots\}$, $\Q$, $\R$, $\R^+$, $\R^{\geq}$ and $\C$, were fixed in [[§1 The Language of Mathematics#^def-1-1|Def. §1.1]], together with the convention that $\N$ contains $0$ (Single Variable Analysis uses $\N = \{1, 2, \ldots\}$, our $\Z^+$).

> [!definition] Definition §6.2: Specifying a Set
> There are three basic ways to specify a set.
> 1. **Listing the elements** in curly brackets, $A = \{1, 3, \pi, -14\}$. Order and repetition do not matter: $\{1, 3, \pi, -14\} = \{\pi, 3, \pi, 1, -14, -14\}$. Dots mean "and so on": $\Z^+ = \{1, 2, 3, \ldots\}$.
> 2. **Conditional definition.** For a set $A$ and a predicate $P(x)$ with free variable $x$ ranging over $A$,
>
> $$
> \{x \in A \mid P(x)\}
> $$
>
> is the set of those $x \in A$ for which $P(x)$ is true; that is, for $a \in A$, $\ a \in \{x \in A \mid P(x)\} \iff P(a)$. The bar is read "such that". Several conditions after the bar are joined by "and".
> 3. **Constructive definition.** For a formula $f(x)$ defined for $x \in A$,
>
> $$
> \{f(x) \mid x \in A\}
> $$
>
> is the set of all values $f(x)$ as $x$ runs through $A$: an object $y$ is an element if and only if $y = f(x)$ for some $x \in A$.
>
> In (2) and (3) the variable $x$ is a **dummy variable**: it can be replaced by any symbol not already in use without changing the set.
>
> *Eccles: Section 6.1(a)–(c)*

^def-6-2

> [!example] Example §6.1: Three Ways of Writing Sets
> - $B = \{n \in \Z \mid 0 < n < 6\} = \{\alpha \in \Z \mid 0 < \alpha < 6\} = \{1, 2, 3, 4, 5\}$.
> - $\{n^2 \mid n \in \Z\} = \{0, 1, 4, 9, 16, \ldots\}$, the set of integer squares. Each non-zero square arises twice ($n^2 = (-n)^2$), which does not affect the set, so also $\{n^2 \mid n \in \Z\} = \{n^2 \mid n \in \N\}$.
> - $\{2q \mid q \in \Z\} = \{\ldots, -4, -2, 0, 2, 4, \ldots\}$ is the set of even integers.
> - $\Q = \{a/b \mid a, b \in \Z,\ b \neq 0\}$; the two conditions after the bar are both required.
>
> Note that $\{n \in \Z \mid 0 < n < 6\}$ is an object, not a statement: it is neither true nor false. Statements can be made about it, such as $2 \in \{n \in \Z \mid 0 < n < 6\}$ (true), or $m \in \{n \in \Z \mid 0 < n < 6\}$, which is the predicate "$m \in \Z$ and $0 < m < 6$".
>
> *Eccles: Section 6.1(a)–(c)*

^ex-6-1

> [!example] Example §6.2: Predicates Defining Given Sets
> Predicates on $\Z$ that determine the subsets $\{3\}$, $\{1, 2, 3\}$ and $\{1, 3\}$:
>
> $$
> \{3\} = \{x \in \Z \mid x = 3\}, \qquad \{1, 2, 3\} = \{x \in \Z \mid 0 < x < 4\}, \qquad \{1, 3\} = \{x \in \Z \mid 0 < x < 4 \text{ and } x \text{ is odd}\}.
> $$
>
> The first is immediate. For the second, the integers $x$ with $0 < x < 4$ are exactly $1, 2, 3$, since there is no integer strictly between two consecutive integers ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]). For the third, of these three only $1$ and $3$ are odd.
>
> *Source: HW3*
> *Eccles: Exercise 6.3*

^ex-6-2

> [!definition] Definition §6.3: Equality of Sets
> Two sets $A$ and $B$ are **equal**, written $A = B$, if they have precisely the same elements:
>
> $$
> A = B \quad\text{means}\quad x \in A \iff x \in B .
> $$
>
> So a set is determined by its elements, and proving $A = B$ means proving two things: every element of $A$ is an element of $B$, and every element of $B$ is an element of $A$.
>
> *Eccles: Definition 6.1.1*

^def-6-3

> [!example] Example §6.3: A Solution Set
> $\{x \in \R \mid x^2 - x - 2 = 0\} = \{-1, 2\}$.
>
> By [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]] this says: for a real number $x$, $\ x^2 - x - 2 = 0 \iff x = -1 \text{ or } x = 2$. Indeed
>
> $$
> x^2 - x - 2 = 0 \iff (x - 2)(x + 1) = 0 \iff x - 2 = 0 \text{ or } x + 1 = 0 \iff x = 2 \text{ or } x = -1,
> $$
>
> the middle step because a product of real numbers is zero exactly when one factor is zero ([[§4 Proof by Contradiction#^prop-4-4|Proposition §4.4]]).
>
> *Eccles: Example 6.1.2*

^ex-6-3

Quadratic inequalities are solved in the same way, with the sign rules for products in place of the zero-product rule: [[§6 The Language of Set Theory#^ex-6-10|Example §6.10]].

> [!definition] Definition §6.4: The Empty Set
> The **empty set** $\emptyset$ is the unique set which has no elements at all. (Uniqueness: [[§6 The Language of Set Theory#^prop-6-1|Proposition §6.1]](4).)
>
> For example, "$x^2 + 2x + 2 = 0$ has no real solutions" may be written $\{x \in \R \mid x^2 + 2x + 2 = 0\} = \emptyset$.
>
> *Eccles: Definition 6.1.3*

^def-6-4

> [!definition] Definition §6.5: Subset; Proper Subset
> Given sets $A$ and $B$, $A$ is a **subset** of $B$, written $A \subseteq B$ or $B \supseteq A$, when every element of $A$ is an element of $B$:
>
> $$
> A \subseteq B \quad\text{means}\quad x \in A \Rightarrow x \in B .
> $$
>
> If in addition $A \ne B$, so that $B$ contains some element not in $A$, then $A$ is a **proper subset** of $B$, written $A \subset B$.
>
> *Eccles: Definition 6.1.4 (some authors write $\subset$ for $\subseteq$)*

^def-6-5

> [!theorem] Proposition §6.1: Basic Facts About Subsets
> Let $A$, $B$, $C$ be sets.
> 1. $A = B \iff (A \subseteq B \text{ and } B \subseteq A)$.
> 2. $a \in A \iff \{a\} \subseteq A$.
> 3. If $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.
> 4. $\emptyset \subseteq A$ for every set $A$, and $A \subseteq \emptyset$ only if $A = \emptyset$. There is only one set with no elements.
> 5. If sets are defined by predicates on a set $A$, then "$P(a) \Rightarrow Q(a)$ for all $a \in A$" is equivalent to $\{a \in A \mid P(a)\} \subseteq \{a \in A \mid Q(a)\}$: implication between predicates corresponds to inclusion between their solution sets.
>
> *Eccles: Section 6.1 (after Definition 6.1.4)*

^prop-6-1

> [!proof]- Proof
> (1) $A = B$ means $x \in A \iff x \in B$, i.e. ($x \in A \Rightarrow x \in B$) and ($x \in B \Rightarrow x \in A$), which is $A \subseteq B$ and $B \subseteq A$.
>
> (2) $\{a\} \subseteq A$ means $x = a \Rightarrow x \in A$ for every $x$. If $a \in A$ this holds; conversely, taking $x = a$ gives $a \in A$.
>
> (3) Let $x \in A$. Then $x \in B$ since $A \subseteq B$, and so $x \in C$ since $B \subseteq C$.
>
> (4) For any $x$ the statement $x \in \emptyset$ is false, so the implication $x \in \emptyset \Rightarrow x \in A$ is true ([[§2 Implications#^def-2-1|Def. §2.1]]: an implication with false hypothesis is true). Hence $\emptyset \subseteq A$. If $A \subseteq \emptyset$, then together with $\emptyset \subseteq A$, (1) gives $A = \emptyset$. Finally, if $E$ and $E'$ both have no elements, the argument just given shows $E \subseteq E'$ and $E' \subseteq E$, so $E = E'$ by (1).
>
> (5) Write $S_P = \{a \in A \mid P(a)\}$ and $S_Q = \{a \in A \mid Q(a)\}$. For $a \in A$ we have $a \in S_P \iff P(a)$ and $a \in S_Q \iff Q(a)$, and every element of $S_P$ lies in $A$. So $S_P \subseteq S_Q$, i.e. $a \in S_P \Rightarrow a \in S_Q$ for all $a$, says exactly that $P(a) \Rightarrow Q(a)$ for all $a \in A$.

^pf-6-1

*Uses:* [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§6 The Language of Set Theory#^def-6-4|Def. §6.4]], [[§6 The Language of Set Theory#^def-6-5|Def. §6.5]], [[§6 The Language of Set Theory#^def-6-2|Def. §6.2]], [[§2 Implications#^def-2-1|Def. §2.1]]

> [!remark] Remark: Membership Versus Inclusion
> The symbols $\in$ and $\subseteq$ must be kept apart: $a \in A$ relates an element to a set, $A \subseteq B$ relates two sets, and they are linked by $a \in A \iff \{a\} \subseteq A$. For instance $1 \in \{1, 2\}$ and $\{1\} \subseteq \{1, 2\}$, but $\{1\} \notin \{1, 2\}$. Likewise a singleton $\{a\}$ is not the element $a$, and $\{\emptyset\} \neq \emptyset$: a box containing an empty box is not an empty box.

^rem-6-1

> [!example] Example §6.4: Which of These Sets Are Equal?
> Consider the following sets of real numbers:
>
> $$
> \begin{aligned}
> &A = \{x + y \mid x, y \in \R\}, && B = \{x \in \R \mid x \ge 0\}, && C = \{x \in \R \mid x^2 \ge 0\}, \\
> &D = \emptyset, && E = \{0, 1\}, && F = \{x \in \R \mid x = x + 1\}, \\
> &G = \{x \in \R \mid x^2 = x\}, && H = \R, && I = \{x^2 \mid x \in \R\}.
> \end{aligned}
> $$
>
> **Answer:** $A = C = H$, $\ B = I$, $\ D = F$, $\ E = G$, and no other equalities hold.
>
> - $A = \R$: each $x + y$ is real; conversely every real $z$ equals $z + 0$.
> - $C = \R$: $x^2 \ge 0$ for every real $x$.
> - $B = I$: if $x \in \R$ then $x^2 \ge 0$, so $I \subseteq B$; if $y \ge 0$ then $y = (\sqrt{y})^2 \in I$, so $B \subseteq I$.
> - $F = \emptyset$: $x = x + 1$ would give $0 = 1$, so no real number satisfies it.
> - $G = E$: $x^2 = x \iff x(x - 1) = 0 \iff x = 0$ or $x = 1$.
>
> The four sets $\R$, $\{x \ge 0\}$, $\{0, 1\}$, $\emptyset$ are pairwise distinct: $-1$ lies in the first but not the second, $2$ in the second but not the third, and $0$ in the third but not the fourth; and the first three are non-empty.
>
> *Source: MAT 200 HW1, Problem 5*

^ex-6-4

> [!example] Example §6.5: Real Intervals
> For real numbers $a, b$ the **real intervals** with endpoints $a$ and $b$ are
>
> $$
> (a, b) = \{x \in \R \mid a < x < b\}, \quad [a, b] = \{x \in \R \mid a \le x \le b\}, \quad [a, b) = \{x \in \R \mid a \le x < b\}, \quad (a, b] = \{x \in \R \mid a < x \le b\}.
> $$
>
> **(i)** $0 \notin (0, 1)$ and $0 \notin (0, 1]$, since $0 < 0$ is false; $0 \in [0, 1]$ and $0 \in [0, 1)$, since $0 \le 0 \le 1$ and $0 \le 0 < 1$.
>
> **(ii)** If $a \le b$, then $[a, b] - (a, b) = \{a, b\}$. For $x \in \R$,
>
> $$
> \begin{aligned}
> x \in [a, b] - (a, b) &\iff a \le x \le b \text{ and not } (a < x < b) \\
> &\iff a \le x \le b \text{ and } (x \le a \text{ or } x \ge b) \\
> &\iff (a \le x \le b \text{ and } x \le a) \text{ or } (a \le x \le b \text{ and } x \ge b) \\
> &\iff x = a \text{ or } x = b ,
> \end{aligned}
> $$
>
> where the last step uses $a \le b$ (for $x = a$ we need $a \le a \le b$). Without $a \le b$ the claim fails: then $[a, b] = \emptyset$ by (iii), so the difference is empty.
>
> **(iii)** $(a, b) = \emptyset \iff a \ge b$. A non-existence statement is awkward to prove directly, so we prove the contrapositive $(a, b) \ne \emptyset \iff a < b$. If $x \in (a, b)$, then $a < x < b$, so $a < b$. Conversely, if $a < b$, then $2a < a + b < 2b$, so $a < \frac{a + b}{2} < b$ and $\frac{a+b}{2} \in (a, b)$. The other intervals:
>
> $$
> [a, b] = \emptyset \iff a > b, \qquad [a, b) = \emptyset \iff a \ge b, \qquad (a, b] = \emptyset \iff a \ge b.
> $$
>
> For $[a, b]$: an element $x$ gives $a \le x \le b$, so $a \le b$; and if $a \le b$ then $a \in [a, b]$. For $[a, b)$: an element gives $a \le x < b$, so $a < b$; and if $a < b$ then $a \in [a, b)$. For $(a, b]$ the same argument works with $b \in (a, b]$.
>
> **(iv)** If $a \le b$, then $[a, b] \subseteq (c, d) \iff c < a \text{ and } b < d$. If $[a, b] \subseteq (c, d)$, then $a, b \in [a, b]$ (as $a \le b$) give $c < a$ and $b < d$. Conversely, if $c < a$ and $b < d$, then $x \in [a, b]$ gives $c < a \le x \le b < d$, so $x \in (c, d)$.
>
> *Source: HW3*
> *Eccles: Exercise 6.1*

^ex-6-5

## 6.2 Operations on Sets

> [!definition] Definition §6.6: Intersection; Disjoint Sets
> The **intersection** of sets $A$ and $B$ is the set of elements lying in both:
>
> $$
> A \cap B = \{x \mid x \in A \text{ and } x \in B\}.
> $$
>
> $A$ and $B$ are **disjoint** if $A \cap B = \emptyset$, i.e. they have no elements in common.
>
> *Eccles: Definition 6.2.1*

^def-6-6

> [!definition] Definition §6.7: Union
> The **union** of sets $A$ and $B$ is the set of elements lying in $A$ or in $B$ (or both):
>
> $$
> A \cup B = \{x \mid x \in A \text{ or } x \in B\}.
> $$
>
> *Eccles: Definition 6.2.2*

^def-6-7

> [!definition] Definition §6.8: Difference
> The **difference** of sets $A$ and $B$ is the set of elements lying in $A$ but not in $B$:
>
> $$
> A - B = \{x \mid x \in A \text{ and } x \notin B\}.
> $$
>
> It is also written $A \setminus B$ (in algebra $A - B$ sometimes means $\{a - b \mid a \in A, b \in B\}$).
>
> *Eccles: Definition 6.2.3*

^def-6-8

> [!remark] Remark: First Identities
> Directly from the definitions: $A \cap A = A = A \cup A$ (since "$P$ and $P$" and "$P$ or $P$" are equivalent to $P$); $A \cap \emptyset = \emptyset$ and $A \cup \emptyset = A$ (since $x \in \emptyset$ is always false); $A - A = \emptyset$ (no $x$ has $x \in A$ and $x \notin A$); and $A - \emptyset = A$ (since $x \notin \emptyset$ is always true).

^rem-6-2

> [!theorem] Proposition §6.2: Splitting a Union
> For any sets $A$ and $B$, the three sets $A \cap B$, $A - B$ and $B - A$ are pairwise disjoint, and
>
> $$
> A \cup B = (A \cap B) \cup (A - B) \cup (B - A).
> $$
>
> *Eccles: Proposition 6.2.4*

^prop-6-2

> [!proof]+ Proof
> Since each set is defined from the statements $x \in A$ and $x \in B$, its membership is determined by the truth values of these two statements, and there are four cases. (The columns are headed by *statements*, which are true or false, not by the sets themselves.)
>
> | $x \in A$ | $x \in B$ | $x \in A \cap B$ | $x \in A - B$ | $x \in B - A$ | $x \in (A \cap B) \cup (A - B) \cup (B - A)$ | $x \in A \cup B$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | F | F | T | T |
> | T | F | F | T | F | T | T |
> | F | T | F | F | T | T | T |
> | F | F | F | F | F | F | F |
>
> No row has more than one T among the columns for $A \cap B$, $A - B$, $B - A$, so no $x$ lies in two of these sets: they are pairwise disjoint. The last two columns agree in every row, so $x \in (A \cap B) \cup (A - B) \cup (B - A) \iff x \in A \cup B$, which is the equality of sets ([[§6 The Language of Set Theory#^def-6-3|Def. §6.3]]).

^pf-6-2

*Uses:* [[§6 The Language of Set Theory#^def-6-6|Def. §6.6]], [[§6 The Language of Set Theory#^def-6-7|Def. §6.7]], [[§6 The Language of Set Theory#^def-6-8|Def. §6.8]], [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§1 The Language of Mathematics#^def-1-3|Def. §1.3]]

![[m250-6-1.svg]]
*The Venn diagram of Proposition §6.2: the four rows of the truth table are the four regions. $A - B$ (blue), $A \cap B$ (red) and $B - A$ (green) do not overlap, and together they fill $A \cup B$; the fourth row is the region outside both circles.*

> [!remark] Remark: Venn Diagrams
> A **Venn diagram** represents sets by regions of the page, and the regions cut out by $k$ overlapping regions correspond to the $2^k$ rows of a truth table. This makes identities like Proposition §6.2 visible, but a diagram is an illustration, not a proof: a region may be empty (the diagram above does not claim $A \cap B \ne \emptyset$), a careless drawing may omit a possible region, and a diagram may contain features with no set-theoretic meaning. The proofs are the truth tables and element arguments.

^rem-6-3

## 6.3 The Power Set

> [!definition] Definition §6.9: Power Set; Singleton
> The **power set** $\mathcal{P}(X)$ of a set $X$ is the set of all subsets of $X$. Thus $A \in \mathcal{P}(X)$ is another way of writing $A \subseteq X$. A set $\{a\}$ with a single element is a **singleton**.
>
> *Eccles: Definition 6.3.1*

^def-6-9

> [!remark]- Connections
> - Developed further in: [[§4 Uncountability#^def-4-1|551 Def. §4.1]] (power set), where Cantor's theorem ([[§4 Uncountability#^thm-4-1|551 Thm. §4.1]]) shows there is no surjection $X \to \mathcal{P}(X)$.

> [!example] Example §6.6: The Power Set of a Three-Element Set
> If $X = \{a, b, c\}$ then
>
> $$
> \mathcal{P}(X) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, X\}.
> $$
>
> Note $\emptyset \in \mathcal{P}(X)$ for every set $X$, since $\emptyset \subseteq X$ ([[§6 The Language of Set Theory#^prop-6-1|Proposition §6.1]](4)), and $X \in \mathcal{P}(X)$. Here $X$ has $3$ elements and $\mathcal{P}(X)$ has $8 = 2^3$.
>
> *Eccles: Example 6.3.2*

^ex-6-6

In general a set with $n$ elements has $2^n$ subsets: [[§12★ Counting Functions and Subsets#^prop-12-4|Proposition §12.4]].

> [!definition] Definition §6.10: Universal Set; Complement
> Often all the sets under consideration are subsets of one fixed set $U$, the **universal set**. Once $U$ is fixed, the **complement** of $A \in \mathcal{P}(U)$ is
>
> $$
> A^c = U - A = \{x \in U \mid x \notin A\}.
> $$
>
> For example, if $U = \Z$ and $E$ is the set of even integers, then $E^c$ is the set of odd integers.
>
> *Eccles: Definition 6.3.3*

^def-6-10

Intersection, union and complement of subsets of $U$ correspond to the connectives "and", "or" and "not": for $x \in U$,

$$
x \in A \cap B \iff (x \in A) \wedge (x \in B), \qquad x \in A \cup B \iff (x \in A) \vee (x \in B), \qquad x \in A^c \iff \neg(x \in A).
$$

So each law of logic from [[§1 The Language of Mathematics|§1]] translates into a law of sets.

> [!theorem] Theorem §6.3: The Laws of the Algebra of Sets
> Let $A$, $B$, $C$ be subsets of a universal set $U$. Then:
> 1. *associativity:* $A \cup (B \cup C) = (A \cup B) \cup C$ and $A \cap (B \cap C) = (A \cap B) \cap C$;
> 2. *commutativity:* $A \cup B = B \cup A$ and $A \cap B = B \cap A$;
> 3. *distributivity:* $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ and $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$;
> 4. *De Morgan laws:* $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$;
> 5. *complementation:* $A \cup A^c = U$ and $A \cap A^c = \emptyset$;
> 6. *double complement:* $(A^c)^c = A$.
>
> *Eccles: Theorem 6.3.4*

^thm-6-3

> [!proof]+ Proof
> In every identity both sides are subsets of $U$, so by [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]] it suffices to show that each $x \in U$ lies in the left side if and only if it lies in the right side. Fix $x \in U$ and write $P$, $Q$, $R$ for the statements $x \in A$, $x \in B$, $x \in C$. By the correspondence displayed above, each side's membership condition is a propositional form in $P, Q, R$, and the identity reduces to a logical equivalence that holds for all truth values of $P, Q, R$ ([[§1 The Language of Mathematics#^thm-1-1|Theorem §1.1]], [[§1 The Language of Mathematics#^thm-1-2|Theorem §1.2]]):
>
> | identity | membership condition, left $\equiv$ right |
> |---|---|
> | 1 | $P \vee (Q \vee R) \equiv (P \vee Q) \vee R$, $\ P \wedge (Q \wedge R) \equiv (P \wedge Q) \wedge R$ |
> | 2 | $P \vee Q \equiv Q \vee P$, $\ P \wedge Q \equiv Q \wedge P$ |
> | 3 | $P \vee (Q \wedge R) \equiv (P \vee Q) \wedge (P \vee R)$, $\ P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$ |
> | 4 | $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$, $\ \neg(P \wedge Q) \equiv \neg P \vee \neg Q$ |
> | 5 | $P \vee \neg P$ is always true; $P \wedge \neg P$ is always false |
> | 6 | $\neg\neg P \equiv P$ |
>
> In (5), "always true" means every $x \in U$ lies in $A \cup A^c$, so $A \cup A^c = U$; "always false" means no $x$ lies in $A \cap A^c$, so $A \cap A^c = \emptyset$. Each equivalence is checked by a truth table with $2$ or $8$ rows (for the second distributive law this is done in [[§6 The Language of Set Theory#^ex-6-7|Example §6.7]]).
>
> The same reasoning can be written directly with elements. For instance, for $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$:
>
> "$\subseteq$": let $x \in A \cap (B \cup C)$. Then $x \in A$ and $x \in B \cup C$, so $x \in B$ or $x \in C$. If $x \in B$, then since $x \in A$ we get $x \in A \cap B \subseteq (A \cap B) \cup (A \cap C)$. If $x \notin B$, then $x \in C$, so $x \in A \cap C \subseteq (A \cap B) \cup (A \cap C)$.
>
> "$\supseteq$": let $x \in (A \cap B) \cup (A \cap C)$. If $x \in A \cap B$, then $x \in A$ and $x \in B \subseteq B \cup C$, so $x \in A \cap (B \cup C)$. Otherwise $x \in A \cap C$, so $x \in A$ and $x \in C \subseteq B \cup C$, and again $x \in A \cap (B \cup C)$.

^pf-6-3

*Uses:* [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§6 The Language of Set Theory#^def-6-6|Def. §6.6]], [[§6 The Language of Set Theory#^def-6-7|Def. §6.7]], [[§6 The Language of Set Theory#^def-6-10|Def. §6.10]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^thm-1-2|§1.2]]

Once these laws are available, further identities follow by algebra, without returning to elements.

> [!theorem] Proposition §6.4: Expanding a Product of Unions
> For sets $A$, $B$, $C$, $D$,
>
> $$
> (A \cup B) \cap (C \cup D) = (A \cap C) \cup (A \cap D) \cup (B \cap C) \cup (B \cap D).
> $$
>
> *Eccles: Proposition 6.3.5*

^prop-6-4

> [!proof]+ Proof
> Commutativity turns distributivity on the left into distributivity on the right: $(X \cup Y) \cap Z = Z \cap (X \cup Y) = (Z \cap X) \cup (Z \cap Y) = (X \cap Z) \cup (Y \cap Z)$. Hence
>
> $$
> \begin{aligned}
> (A \cup B) \cap (C \cup D) &= \big(A \cap (C \cup D)\big) \cup \big(B \cap (C \cup D)\big) && \text{(distributivity on the right)} \\
> &= (A \cap C) \cup (A \cap D) \cup (B \cap C) \cup (B \cap D) && \text{(distributivity).}
> \end{aligned}
> $$
>
> By associativity of $\cup$ no further brackets are needed.

^pf-6-4

*Uses:* [[§6 The Language of Set Theory#^thm-6-3|§6.3]]

> [!example] Example §6.7: Distributivity by Truth Table
> **Claim:** $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.
>
> | $x \in A$ | $x \in B$ | $x \in C$ | $x \in B \cup C$ | $x \in A \cap B$ | $x \in A \cap C$ | $x \in A \cap (B \cup C)$ | $x \in (A \cap B) \cup (A \cap C)$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | T | T | T | T | T |
> | T | T | F | T | T | F | T | T |
> | T | F | T | T | F | T | T | T |
> | T | F | F | F | F | F | F | F |
> | F | T | T | T | F | F | F | F |
> | F | T | F | T | F | F | F | F |
> | F | F | T | T | F | F | F | F |
> | F | F | F | F | F | F | F | F |
>
> The last two columns agree in all eight rows, so $x \in A \cap (B \cup C) \iff x \in (A \cap B) \cup (A \cap C)$, and the sets are equal. In the Venn diagram below, both sides are the region of $A$ that meets $B$ or $C$, made of the first three rows.
>
> *Source: HW3*
> *Eccles: Exercise 6.4*

^ex-6-7

![[m250-6-2.svg]]
*Both sides of the distributive law shade the same region (red). On the left, $B \cup C$ (blue) is cut down to its part inside $A$; on the right, the two pieces $A \cap B$ (hatched) and $A \cap C$ are put together, overlapping in $A \cap B \cap C$ (the first row of the table).*

> [!example] Example §6.8: A Proof by Contradiction with Sets
> **Claim:** if $A \cap B \subseteq C$ and $x \in B$, then $x \notin A - C$.
>
> The conclusion is a negative statement, which suggests contradiction. Suppose $A \cap B \subseteq C$ and $x \in B$, and suppose for contradiction that $x \in A - C$. By [[§6 The Language of Set Theory#^def-6-8|Def. §6.8]], $x \in A$ and $x \notin C$. Since also $x \in B$, we have $x \in A \cap B$, and so $x \in C$ because $A \cap B \subseteq C$. This contradicts $x \notin C$. Hence $x \notin A - C$.
>
> *Source: HW3*
> *Eccles: Exercise 6.6*

^ex-6-8

> [!example] Example §6.9: Inclusion in Terms of the Operations
> For sets $A$, $B$ (subsets of $U$ in the last part):
> 1. $A \subseteq B \iff A \cup B = B$;
> 2. $A \subseteq B \iff A \cap B = A$;
> 3. $A \subseteq B \iff B^c \subseteq A^c$.
>
> (1) Always $B \subseteq A \cup B$. If $A \subseteq B$, then $x \in A \cup B$ means $x \in A$ or $x \in B$, and in either case $x \in B$; so $A \cup B \subseteq B$ and equality holds by [[§6 The Language of Set Theory#^prop-6-1|Proposition §6.1]](1). Conversely, if $A \cup B = B$, then $A \subseteq A \cup B = B$.
>
> (2) Always $A \cap B \subseteq A$. If $A \subseteq B$, then $x \in A$ gives $x \in B$, so $x \in A \cap B$; hence $A \subseteq A \cap B$ and equality holds. Conversely, if $A \cap B = A$, then $A = A \cap B \subseteq B$.
>
> (3) For $x \in U$, $A \subseteq B$ says $x \in A \Rightarrow x \in B$, and $B^c \subseteq A^c$ says $x \notin B \Rightarrow x \notin A$. These implications are contrapositives of each other, hence equivalent ([[§2 Implications#^prop-2-2|Proposition §2.2]]).
>
> *Eccles: Exercises 6.5, 6.7*

^ex-6-9

> [!example] Example §6.10: Solving a Quadratic Inequality
> Prove that
> (i) $\{x \in \R \mid x^2 + x - 2 = 0\} = \{1, -2\}$;
> (ii) $\{x \in \R \mid x^2 + x - 2 < 0\} = (-2, 1)$;
> (iii) $\{x \in \R \mid x^2 + x - 2 > 0\} = \{x \in \R \mid x < -2\} \cup \{x \in \R \mid x > 1\}$.
>
> **Solution.** Factor $x^2 + x - 2 = (x - 1)(x + 2)$, and use the sign of a product ([[§4 Proof by Contradiction#^prop-4-4|Proposition §4.4]], [[§4 Proof by Contradiction#^prop-4-5|Proposition §4.5]]). For a real number $x$:
>
> (i) $(x - 1)(x + 2) = 0 \iff x - 1 = 0$ or $x + 2 = 0 \iff x = 1$ or $x = -2$, as in [[§6 The Language of Set Theory#^ex-6-3|Example §6.3]].
>
> (ii) $(x - 1)(x + 2) < 0 \iff (x - 1 > 0$ and $x + 2 < 0)$ or $(x - 1 < 0$ and $x + 2 > 0) \iff (x > 1$ and $x < -2)$ or $(x < 1$ and $x > -2)$. The first alternative never holds, since $x > 1$ and $x < -2$ would give $1 < -2$. So the condition is $-2 < x < 1$, i.e. $x \in (-2, 1)$.
>
> (iii) $(x - 1)(x + 2) > 0 \iff (x > 1$ and $x > -2)$ or $(x < 1$ and $x < -2) \iff x > 1$ or $x < -2$, since $x > 1$ already implies $x > -2$, and $x < -2$ already implies $x < 1$. This is membership of the union ([[§6 The Language of Set Theory#^def-6-7|Def. §6.7]]).
>
> The three cases can be read off at once from a table of signs:
>
> | | $x - 1$ | $x + 2$ | $(x - 1)(x + 2)$ |
> |:-:|:-:|:-:|:-:|
> | $x < -2$ | $-$ | $-$ | $+$ |
> | $x = -2$ | $-$ | $0$ | $0$ |
> | $-2 < x < 1$ | $-$ | $+$ | $-$ |
> | $x = 1$ | $0$ | $+$ | $0$ |
> | $x > 1$ | $+$ | $+$ | $+$ |
>
> *Eccles: Exercise 6.2*

^ex-6-10

*Uses:* [[§4 Proof by Contradiction#^prop-4-4|§4.4]], [[§4 Proof by Contradiction#^prop-4-5|§4.5]], [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§6 The Language of Set Theory#^def-6-7|Def. §6.7]]
