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

This section sets up the vocabulary of sets that the rest of the subject is written in: how sets are specified, when two sets are equal, subsets, and the operations of intersection, union, difference and complement (the operations in [[§6a Operations on Sets|§6a]]). Each operation is defined by a logical connective ([[§1 The Language of Mathematics|§1]]), so every identity between sets comes from a logical equivalence between statements. The proofs in this section and its continuation [[§6a Operations on Sets|§6a]] show the three ways of proving such identities: truth tables, element-chasing, and algebra with identities already proved.

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

The operations on sets and the power set continue in [[§6a Operations on Sets]].
