---
type: section
subject: "[[Measure Theory]]"
chapter: 1
section: 1
tags: [measure-theory, math551]
---
↑ [[· 1 Set Theory Prerequisites]] · [[§2 The Cantor–Bernstein Theorem]] →

## Countability of Sets

The notion of countability captures when we can “list” all elements of a set.

> [!definition] Definition §1.1: Countable Set
> A set $A$ is called **countable** if we can list its elements as a sequence:
>
> $$
> A = \{a_1, a_2, a_3, \ldots\}.
> $$
>
> Equivalently, $A$ is countable if there exists a bijection $f: A \to S$ where $S$ is a subset of $\mathbb{N}$. This includes both finite sets and countably infinite sets.

^def-1-1

> [!remark]- Connections
> - MATH 451 version: [[§2 The Set ℚ of Rational Numbers#^def-2-8|Countable (451 Def. §2.8)]], with [[§2 The Set ℚ of Rational Numbers#^def-2-9|Uncountable (451 Def. §2.9)]].

## Mappings and Functions

> [!definition] Definition §1.2: Mapping
> A **mapping** $f: X \to Y$ is a rule that assigns to each element $x \in X$ a unique element $f(x) \in Y$. We call $f$ a **function** if $Y = \mathbb{R}$, $\mathbb{C}$, or $\mathbb{N}$.

^def-1-2

> [!remark]- Connections
> - Elementary version: [[§8 Functions#^def-8-1|250 Def. §8.1]] (function, domain, codomain).

> [!definition] Definition §1.3: Injective (One-to-One)
> A mapping $f: X \to Y$ is **injective** (or **one-to-one**, written $1$-$1$) if for all $x_1, x_2 \in X$:
>
> $$
> x_1 \neq x_2 \implies f(x_1) \neq f(x_2).
> $$
>
> Equivalently, $f(x_1) = f(x_2) \implies x_1 = x_2$.

^def-1-3

> [!remark]- Connections
> - Same definition: [[§9 Injections, Surjections and Bijections#^def-9-1|250 Def. §9.1]].

> [!definition] Definition §1.4: Surjective (Onto)
> A mapping $f: X \to Y$ is **surjective** (or **onto**) if for every $y \in Y$, there exists $x \in X$ such that $f(x) = y$. In other words, $f(X) = Y$.

^def-1-4

> [!remark]- Connections
> - Same definition: [[§9 Injections, Surjections and Bijections#^def-9-2|250 Def. §9.2]], part 2.

> [!definition] Definition §1.5: Range
> The **range** of $f$ is $f(X) = \{f(x) \mid x \in X\}$. Note that $f: X \to Y$ is surjective if and only if $f(X) = Y$.

^def-1-5

> [!remark]- Connections
> - Same notion: the image of a function, [[§8 Functions#^def-8-10|250 Def. §8.10]].

> [!definition] Definition §1.6: Bijection
> If $f: X \to Y$ is both injective and surjective, we say $f$ is a **bijection** or a **one-to-one correspondence**.

^def-1-6

> [!remark]- Connections
> - Same definition: [[§9 Injections, Surjections and Bijections#^def-9-3|250 Def. §9.3]], part 3; the bijections are exactly the invertible functions, [[§9 Injections, Surjections and Bijections#^thm-9-2|250 Thm. §9.2]].

> [!example] Example §1.1: $f: \mathbb{N} \to 2\mathbb{N}$
> Define $f: \mathbb{N} \to 2\mathbb{N}$ by $f(n) = 2n$, where $2\mathbb{N} = \{2, 4, 6, \ldots\}$ denotes the even natural numbers. This is a bijection, showing that $\mathbb{N} \sim 2\mathbb{N}$.

^ex-1-1

> [!definition] Definition §1.7: Equivalence of Sets
> We say set $X$ is **equivalent** to set $Y$, written $X \sim Y$, if there exists a bijection $f: X \to Y$.

^def-1-7

> [!remark]- Connections
> - MATH 451 version: [[§2 The Set ℚ of Rational Numbers#^def-2-7|Same Size (451 Def. §2.7)]], e.g. [[§2 The Set ℚ of Rational Numbers#^thm-2-4|ℕ and ℤ have the same size]].
> - Elementary version: equipotent sets, [[§14 Counting Infinite Sets#^def-14-1|250 Def. §14.1]].

> [!definition] Definition §1.8: Countable (Formal)
> A set $A$ is **countable** if there exists a bijection $f: A \to S$ for some subset $S \subseteq \mathbb{N}$. This means $A$ is either finite or countably infinite.

^def-1-8

> [!remark]- Connections
> - Same notion: countable in [[§14 Counting Infinite Sets#^def-14-3|250 Def. §14.3]] (finite or denumerable); [[§14 Counting Infinite Sets#^cor-14-6|250 Cor. §14.6]] shows it is equivalent to an injection into ℤ⁺.

> [!example] Example §1.2: $2\mathbb{N}$ is countably infinite
> The set of even natural numbers $2\mathbb{N}$ is countably infinite since $f(n) = 2n$ gives a bijection $\mathbb{N} \to 2\mathbb{N}$.

^ex-1-2

## Properties of Equivalence

> [!theorem] Theorem §1.1: Properties of Equivalence
> For sets $A$, $B$, and $C$:
> - (i) $A \sim B \iff B \sim A$ (symmetry)
> - (ii) $A \sim B$ and $B \sim C \implies A \sim C$ (transitivity)

^thm-1-1

> [!proof]+ Proof
> (i) If $f: A \to B$ is a bijection, then $f^{-1}: B \to A$ is also a bijection.
>
> (ii) If $f: A \to B$ and $g: B \to C$ are bijections, then $g \circ f: A \to C$ is a bijection.

^pf-1-1

*Uses:* [[§1 Countability and Set Theory#^def-1-6|Def. §1.6]], [[§1 Countability and Set Theory#^def-1-7|Def. §1.7]]

> [!theorem] Theorem §1.2: Infinite Sets Have Countable Infinite Subsets
> Every infinite set has a countably infinite subset.

^thm-1-2

> [!proof]+ Proof
> Let $X$ be an infinite set. Choose $x_1 \in X$. Since $X$ is infinite, $X \setminus \{x_1\} \neq \emptyset$, so choose $x_2 \in X \setminus \{x_1\}$. Similarly, choose $x_3 \in X \setminus \{x_1, x_2\}$.
>
> Continuing inductively: assuming we have chosen $\{x_1, \ldots, x_n\}$ from $X$, since $X$ is infinite, $X \setminus \{x_1, \ldots, x_n\} \neq \emptyset$. Choose $x_{n+1} \in X \setminus \{x_1, \ldots, x_n\}$.
>
> Then $\{x_1, x_2, x_3, \ldots\}$ is a countably infinite subset of $X$.

^pf-1-2

*Uses:* [[§1 Countability and Set Theory#^def-1-8|Def. §1.8]]

> [!remark]- Connections
> - Elementary version: [[§14 Counting Infinite Sets#^lem-14-2|250 Lemma §14.2]] (the same inductive choice of distinct elements).

## Countability of $\mathbb{N} \times \mathbb{N}$

> [!example] Example §1.3: $\mathbb{N} \times \mathbb{N} \sim \mathbb{N}$
> The set $\mathbb{N} \times \mathbb{N}$ is countable. We can list its elements by diagonals:
>
> $$
> \mathbb{N} \times \mathbb{N} = \left\{
> \begin{array}{ccccc}
> (1,1), & (1,2), & (1,3), & (1,4), & \cdots \\
> (2,1), & (2,2), & (2,3), & \cdots & \\
> (3,1), & (3,2), & \cdots & & \\
> (4,1), & \cdots & & & \\
> \vdots & & & &
> \end{array}
> \right\}
> $$
>
> Listing by diagonals: $(1,1), (1,2), (2,1), (1,3), (2,2), (3,1), \ldots$
>
> More explicitly, every natural number $n$ can be written uniquely as $n = 2^{i-1}(2j-1)$ for some $i, j \in \mathbb{N}$. This gives a bijection $f: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ defined by $f(i,j) = 2^{i-1}(2j-1)$.

^ex-1-3

![[m551-1-1.svg]]
*Two ways to count $\mathbb{N} \times \mathbb{N}$, with $(i,j)$ in row $i$ and column $j$ as in the array above. Left: the listing by diagonals — each diagonal $i + j = \text{const}$ is finite, so it is run through (red) before jumping to the next one (grey dashed); the small numbers are the positions in the list. Right: the explicit bijection $f(i,j) = 2^{i-1}(2j-1)$ — row $i$ holds the odd numbers times $2^{i-1}$, so every $n$ appears exactly once, in the row given by the power of $2$ dividing it.*

> [!remark]- Connections
> - MATH 451: the same diagonal listing proves [[§2 The Set ℚ of Rational Numbers#^thm-2-5|ℚ is countable (451 §2.5)]].
> - Used for [[Countable Union of Countable Sets is Countable|Countable Union of Countable Sets]] and for the countability of the rational balls in [[§6 Open Covers and the Heine–Borel Theorem#^lem-6-1|Lemma §6.1]].
> - Elementary version: [[§14 Counting Infinite Sets#^prop-14-8|250 Prop. §14.8]] (the product of two denumerable sets is denumerable).
