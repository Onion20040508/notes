---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: "6a"
eccles: "Ch. 6"
aliases: ["Eccles 6 (cont.)"]
tags: [logic-and-proofs, mat250]
---
← [[§6 The Language of Set Theory]] · ↑ [[· 2 Sets and Functions]] · [[§7 Quantifiers]] →

*Eccles, Chapter 6 · MAT 250 HW3 (Exercises 6.1, 6.3, 6.4, 6.6) · MAT 200 HW1 (Problem 5).*

This section covers the operations of intersection, union, difference and complement, and the power set. Each operation is defined by a logical connective ([[§1 The Language of Mathematics|§1]]), so every identity between sets comes from a logical equivalence between statements. The proofs show the three ways of proving such identities: truth tables, element-chasing, and algebra with identities already proved.

## 6.2 Operations on Sets

> [!definition] Definition §6a.1: Intersection
> The **intersection** of sets $A$ and $B$ is the set of elements lying in both:
>
> $$
> A \cap B = \{x \mid x \in A \text{ and } x \in B\}.
> $$
>
> *Eccles: Definition 6.2.1*

^def-6a-1

> [!definition] Definition §6a.2: Disjoint Sets
> $A$ and $B$ are **disjoint** if $A \cap B = \emptyset$, i.e. they have no elements in common.
>
> *Eccles: Definition 6.2.1*

^def-6a-2

> [!definition] Definition §6a.3: Union
> The **union** of sets $A$ and $B$ is the set of elements lying in $A$ or in $B$ (or both):
>
> $$
> A \cup B = \{x \mid x \in A \text{ or } x \in B\}.
> $$
>
> *Eccles: Definition 6.2.2*

^def-6a-3

> [!definition] Definition §6a.4: Difference
> The **difference** of sets $A$ and $B$ is the set of elements lying in $A$ but not in $B$:
>
> $$
> A - B = \{x \mid x \in A \text{ and } x \notin B\}.
> $$
>
> It is also written $A \setminus B$ (in algebra $A - B$ sometimes means $\{a - b \mid a \in A, b \in B\}$).
>
> *Eccles: Definition 6.2.3*

^def-6a-4

> [!remark] Remark: First Identities
> Directly from the definitions: $A \cap A = A = A \cup A$ (since "$P$ and $P$" and "$P$ or $P$" are equivalent to $P$); $A \cap \emptyset = \emptyset$ and $A \cup \emptyset = A$ (since $x \in \emptyset$ is always false); $A - A = \emptyset$ (no $x$ has $x \in A$ and $x \notin A$); and $A - \emptyset = A$ (since $x \notin \emptyset$ is always true).

^rem-6a-2

> [!theorem] Proposition §6a.1: Splitting a Union
> For any sets $A$ and $B$, the three sets $A \cap B$, $A - B$ and $B - A$ are pairwise disjoint, and
>
> $$
> A \cup B = (A \cap B) \cup (A - B) \cup (B - A).
> $$
>
> *Eccles: Proposition 6.2.4*

^prop-6a-1

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

^pf-6a-1

*Uses:* [[§6a Operations on Sets#^def-6a-1|Def. §6a.1]], [[§6a Operations on Sets#^def-6a-2|Def. §6a.2]], [[§6a Operations on Sets#^def-6a-3|Def. §6a.3]], [[§6a Operations on Sets#^def-6a-4|Def. §6a.4]], [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§1 The Language of Mathematics#^def-1-5|Def. §1.5]]

![[m250-6-1.svg]]
*The Venn diagram of [[§6a Operations on Sets#^prop-6a-1|Proposition §6a.1]]: the four rows of the truth table are the four regions. $A - B$ (blue), $A \cap B$ (red) and $B - A$ (green) do not overlap, and together they fill $A \cup B$; the fourth row is the region outside both circles.*

> [!remark] Remark: Venn Diagrams
> A **Venn diagram** represents sets by regions of the page, and the regions cut out by $k$ overlapping regions correspond to the $2^k$ rows of a truth table. This makes identities like [[§6a Operations on Sets#^prop-6a-1|Proposition §6a.1]] visible, but a diagram is an illustration, not a proof: a region may be empty (the diagram above does not claim $A \cap B \ne \emptyset$), a careless drawing may omit a possible region, and a diagram may contain features with no set-theoretic meaning. The proofs are the truth tables and element arguments.

^rem-6a-3

## 6.3 The Power Set

> [!definition] Definition §6a.5: Power Set
> The **power set** $\mathcal{P}(X)$ of a set $X$ is the set of all subsets of $X$. Thus $A \in \mathcal{P}(X)$ is another way of writing $A \subseteq X$.
>
> *Eccles: Definition 6.3.1*

^def-6a-5

> [!remark]- Connections
> - Developed further in: [[§4 Uncountability#^def-4-1|551 Def. §4.1]] (power set), where Cantor's theorem ([[§4 Uncountability#^thm-4-1|551 Thm. §4.1]]) shows there is no surjection $X \to \mathcal{P}(X)$.

> [!definition] Definition §6a.6: Singleton
> A set $\{a\}$ with a single element is a **singleton**.
>
> *Eccles: Definition 6.3.1*

^def-6a-6

> [!example] Example §6a.1: The Power Set of a Three-Element Set
> If $X = \{a, b, c\}$ then
>
> $$
> \mathcal{P}(X) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, X\}.
> $$
>
> Note $\emptyset \in \mathcal{P}(X)$ for every set $X$, since $\emptyset \subseteq X$ ([[§6 The Language of Set Theory#^prop-6-1|Proposition §6.1]](4)), and $X \in \mathcal{P}(X)$. Here $X$ has $3$ elements and $\mathcal{P}(X)$ has $8 = 2^3$.
>
> *Eccles: Example 6.3.2*

^ex-6a-1

In general a set with $n$ elements has $2^n$ subsets: [[§12★ Counting Functions and Subsets#^prop-12-5|Proposition §12.5]].

> [!definition] Definition §6a.7: Universal Set
> Often all the sets under consideration are subsets of one fixed set $U$, the **universal set**.
>
> *Eccles: Definition 6.3.3*

^def-6a-7

> [!definition] Definition §6a.8: Complement
> Once $U$ is fixed, the **complement** of $A \in \mathcal{P}(U)$ is
>
> $$
> A^c = U - A = \{x \in U \mid x \notin A\}.
> $$
>
> For example, if $U = \Z$ and $E$ is the set of even integers, then $E^c$ is the set of odd integers.
>
> *Eccles: Definition 6.3.3*

^def-6a-8

Intersection, union and complement of subsets of $U$ correspond to the connectives "and", "or" and "not": for $x \in U$,

$$
x \in A \cap B \iff (x \in A) \wedge (x \in B), \qquad x \in A \cup B \iff (x \in A) \vee (x \in B), \qquad x \in A^c \iff \neg(x \in A).
$$

So each law of logic from [[§1 The Language of Mathematics|§1]] translates into a law of sets.

> [!theorem] Theorem §6a.2: The Laws of the Algebra of Sets
> Let $A$, $B$, $C$ be subsets of a universal set $U$. Then:
> 1. *associativity:* $A \cup (B \cup C) = (A \cup B) \cup C$ and $A \cap (B \cap C) = (A \cap B) \cap C$;
> 2. *commutativity:* $A \cup B = B \cup A$ and $A \cap B = B \cap A$;
> 3. *distributivity:* $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ and $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$;
> 4. *De Morgan laws:* $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$;
> 5. *complementation:* $A \cup A^c = U$ and $A \cap A^c = \emptyset$;
> 6. *double complement:* $(A^c)^c = A$.
>
> *Eccles: Theorem 6.3.4*

^thm-6a-2

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
> In (5), "always true" means every $x \in U$ lies in $A \cup A^c$, so $A \cup A^c = U$; "always false" means no $x$ lies in $A \cap A^c$, so $A \cap A^c = \emptyset$. Each equivalence is checked by a truth table with $2$ or $8$ rows (for the second distributive law this is done in [[§6a Operations on Sets#^ex-6a-2|Example §6a.2]]).
>
> The same reasoning can be written directly with elements. For instance, for $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$:
>
> "$\subseteq$": let $x \in A \cap (B \cup C)$. Then $x \in A$ and $x \in B \cup C$, so $x \in B$ or $x \in C$. If $x \in B$, then since $x \in A$ we get $x \in A \cap B \subseteq (A \cap B) \cup (A \cap C)$. If $x \notin B$, then $x \in C$, so $x \in A \cap C \subseteq (A \cap B) \cup (A \cap C)$.
>
> "$\supseteq$": let $x \in (A \cap B) \cup (A \cap C)$. If $x \in A \cap B$, then $x \in A$ and $x \in B \subseteq B \cup C$, so $x \in A \cap (B \cup C)$. Otherwise $x \in A \cap C$, so $x \in A$ and $x \in C \subseteq B \cup C$, and again $x \in A \cap (B \cup C)$.

^pf-6a-2

*Uses:* [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§6a Operations on Sets#^def-6a-1|Def. §6a.1]], [[§6a Operations on Sets#^def-6a-3|Def. §6a.3]], [[§6a Operations on Sets#^def-6a-7|Def. §6a.7]], [[§6a Operations on Sets#^def-6a-8|Def. §6a.8]], [[§6a Operations on Sets#^ex-6a-2|Ex. §6a.2]], [[§1 The Language of Mathematics#^thm-1-1|§1.1]], [[§1 The Language of Mathematics#^thm-1-2|§1.2]]

Once these laws are available, further identities follow by algebra, without returning to elements.

> [!theorem] Proposition §6a.3: Expanding a Product of Unions
> For sets $A$, $B$, $C$, $D$,
>
> $$
> (A \cup B) \cap (C \cup D) = (A \cap C) \cup (A \cap D) \cup (B \cap C) \cup (B \cap D).
> $$
>
> *Eccles: Proposition 6.3.5*

^prop-6a-3

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

^pf-6a-3

*Uses:* [[§6a Operations on Sets#^thm-6a-2|§6a.2]]

> [!example] Example §6a.2: Distributivity by Truth Table
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

^ex-6a-2

![[m250-6-2.svg]]
*Both sides of the distributive law shade the same region (red). On the left, $B \cup C$ (blue) is cut down to its part inside $A$; on the right, the two pieces $A \cap B$ (hatched) and $A \cap C$ are put together, overlapping in $A \cap B \cap C$ (the first row of the table).*

> [!example] Example §6a.3: A Proof by Contradiction with Sets
> **Claim:** if $A \cap B \subseteq C$ and $x \in B$, then $x \notin A - C$.
>
> The conclusion is a negative statement, which suggests contradiction. Suppose $A \cap B \subseteq C$ and $x \in B$, and suppose for contradiction that $x \in A - C$. By [[§6a Operations on Sets#^def-6a-4|Def. §6a.4]], $x \in A$ and $x \notin C$. Since also $x \in B$, we have $x \in A \cap B$, and so $x \in C$ because $A \cap B \subseteq C$. This contradicts $x \notin C$. Hence $x \notin A - C$.
>
> *Source: HW3*
> *Eccles: Exercise 6.6*

^ex-6a-3

> [!example] Example §6a.4: Inclusion in Terms of the Operations
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

^ex-6a-4

> [!example] Example §6a.5: Solving a Quadratic Inequality
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
> (iii) $(x - 1)(x + 2) > 0 \iff (x > 1$ and $x > -2)$ or $(x < 1$ and $x < -2) \iff x > 1$ or $x < -2$, since $x > 1$ already implies $x > -2$, and $x < -2$ already implies $x < 1$. This is membership of the union ([[§6a Operations on Sets#^def-6a-3|Def. §6a.3]]).
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

^ex-6a-5

*Uses:* [[§4 Proof by Contradiction#^prop-4-4|§4.4]], [[§4 Proof by Contradiction#^prop-4-5|§4.5]], [[§6 The Language of Set Theory#^def-6-3|Def. §6.3]], [[§6a Operations on Sets#^def-6a-3|Def. §6a.3]]
