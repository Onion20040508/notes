---
type: section
subject: "[[Measure Theory]]"
chapter: 1
section: 4
tags: [measure-theory, math551]
---
← [[§3 Countability of Rationals and Unions]] · ↑ [[· 1 Set Theory Prerequisites]] · [[§5 Topology of ℝⁿ]] →

## Uncountability of Binary Sequences

> [!example] Example §4.1: The set of binary sequences is uncountable
> Let $X = \{(a_n)_{n=1}^\infty \mid a_n = 0 \text{ or } 1\}$ be the set of all infinite binary sequences. Then $X$ is not countable.

^ex-4-1

> [!proof]+ Proof
> Suppose for contradiction that $X$ is countable. Then there exists a surjection $f: \mathbb{N} \to X$.
>
> Since $f$ is surjective, we can list all elements of $X$ as:
>
> $$
> X = \{(x)_1, (x)_2, (x)_3, \ldots\}
> $$
>
> where $(x)_j = f(j)$ for each $j \in \mathbb{N}$.
>
> Write each sequence explicitly: $(x)_j = (a_n^{(j)})_{n=1}^\infty$ where $a_n^{(j)} \in \{0, 1\}$ for all $n, j$.
>
> We can visualize this as an infinite matrix:
>
> $$
> \begin{array}{c|cccc}
>  & n=1 & n=2 & n=3 & \cdots \\
> \hline
> (x)_1 & \boxed{a_1^{(1)}} & a_2^{(1)} & a_3^{(1)} & \cdots \\
> (x)_2 & a_1^{(2)} & \boxed{a_2^{(2)}} & a_3^{(2)} & \cdots \\
> (x)_3 & a_1^{(3)} & a_2^{(3)} & \boxed{a_3^{(3)}} & \cdots \\
> \vdots & \vdots & \vdots & \vdots & \ddots
> \end{array}
> $$
>
> **Construct a sequence not in the list.** Define $x = (b_n)_{n=1}^\infty$ by:
>
> $$
> b_n = 1 - a_n^{(n)} = \begin{cases} 1 & \text{if } a_n^{(n)} = 0 \\ 0 & \text{if } a_n^{(n)} = 1 \end{cases}
> $$
>
> That is, $b_n$ is obtained by flipping the $n$-th diagonal entry.
>
> **Verify $x \in X$.** Since each $b_n \in \{0, 1\}$, we have $x = (b_n)_{n=1}^\infty \in X$.
>
> **Verify $x \neq (x)_j$ for all $j \in \mathbb{N}$.** For any $j \in \mathbb{N}$, compare $x$ and $(x)_j$ at position $n = j$:
>
> $$
> b_j = 1 - a_j^{(j)} \neq a_j^{(j)}
> $$
>
> Since $x$ and $(x)_j$ differ at the $j$-th position, we have $x \neq (x)_j$.
>
> **Contradiction.** We have $x \in X$ but $x \notin \{(x)_1, (x)_2, (x)_3, \ldots\} = X$.
>
> This contradicts that $f$ is surjective. Therefore $X$ is not countable.

^pf-ex-4-1

*Uses:* [[§1 Countability and Set Theory#^def-1-1|Def. §1.1]], [[§1 Countability and Set Theory#^def-1-4|Def. §1.4]]

![[m551-4-1.svg]]
*Cantor's diagonal argument on the first five sequences of a proposed list. The diagonal digits $a_n^{(n)}$ (red boxes) are flipped to build $x = (b_n)$ (blue): $x$ differs from $(x)_1$ in position $1$, from $(x)_2$ in position $2$, and so on, so $x$ is missing from the list no matter how the list was chosen.*

> [!remark]- Connections
> - Topology: the same set $\{0,1\}^\omega$ is an uncountable discrete subspace of $\mathbb{R}^\omega$ with the uniform metric, which is therefore not second-countable ([[§18 Countability Axioms#^ex-18-6|590 Ex. §18.6]]).

> [!remark] Note
> If a set can only be written as a finite sequence, then it is countable.

^rem-4-1

## Uncountability of $[0,1]$

> [!example] Example §4.2: The interval $[0,1]$ is uncountable
> The interval $[0,1]$ is not countable.

^ex-4-2

> [!proof]+ Proof
> Using the binary representation, every $x \in [0,1]$ can be written as $x = 0.a_1a_2a_3\ldots = \sum_{i=1}^\infty \frac{a_i}{2^i}$ where $a_i \in \{0,1\}$.

^pf-ex-4-2

*Uses:* [[§4 Uncountability#^ex-4-1|Ex. §4.1]], [[Countable Union of Countable Sets is Countable|§3.1]], [[§1 Countability and Set Theory#^def-1-7|Def. §1.7]]

> [!remark] Remark
> The representation is not unique. For example, $\frac{1}{2} = 0.1000\ldots = 0.0111\ldots$.

^rem-4-2

![[m551-4-2.svg]]
*Binary digits as successive halvings: $a_k$ records whether $x$ lies in the left ($0$) or right ($1$) half of the current dyadic interval, and the blue intervals shrink to $x = 0.7 = 0.1011\ldots$. A dyadic rational such as $\tfrac12$ (red) is an endpoint shared by two halves, so it has two expansions, $0.1000\ldots$ and $0.0111\ldots$ — the reason the countable set $D$ of dyadic rationals (and the eventually constant sequences $Y$, $Y'$) is set aside in the proof.*

> [!proof]+ Proof (continued)
> The set $D = \{\frac{k}{2^n} \mid n \in \mathbb{N},\ k = 0, 1, \ldots, 2^n\}$ of dyadic rationals in $[0,1]$ is countable (it's a [[§3 Countability of Rationals and Unions#^prop-3-1|countable union of finite sets]]).
>
> Let $Y = \{(a_n)_{n=1}^\infty \mid a_n \in \{0,1\}, \text{ and } \exists k \in \mathbb{N} \text{ s.t. } a_n = 0 \text{ for all } n > k\}$. These are sequences that are eventually constantly $0$, corresponding to finite binary representations. Let $Y'$ be the set of sequences that are eventually constantly $1$.
>
> Then $Y \sim D \setminus \{1\}$ (send a sequence to the number it represents), so $Y$ is countable; likewise $Y' \sim D \setminus \{0\}$ is countable.
>
> A number $x \in [0,1] \setminus D$ has exactly one binary expansion, and it is neither eventually $0$ nor eventually $1$; conversely such a sequence represents a number in $[0,1] \setminus D$. So $x \mapsto (a_n)$ is a bijection from $[0,1] \setminus D$ to $X \setminus (Y \cup Y')$ (where $X$ is the set of all binary sequences). Since:
> - $Y \cup Y'$ is countable
> - $X \setminus (Y \cup Y')$ is not countable (as $X$ is uncountable, [[§4 Uncountability#^ex-4-1|Ex. §4.1]])
> - $X$ not countable, $Y \cup Y'$ countable $\Rightarrow$ $X \setminus (Y \cup Y')$ not countable
>
> Thus $[0,1] \setminus D$, and hence $[0,1]$, is uncountable.

^pf-ex-4-2-c

> [!remark]- Connections
> - MATH 451 states “$\mathbb{R}$ is uncountable” when proving [[§2 The Set ℚ of Rational Numbers#^thm-2-7|Existence of Transcendental Numbers (451 §2.7)]].
> - Expansions in a base (ternary digits mapped to binary ones) show that the Cantor set is uncountable: [[§11 Borel Sets and Measure Spaces#^prop-11-21|Proposition §11.21]].
> - Elementary version: ℝ is uncountable, [[§14 Counting Infinite Sets#^thm-14-12|250 Thm. §14.12]], by Cantor's diagonal argument on decimal expansions.

## Power Sets

> [!definition] Definition §4.1: Power Set
> Let $X$ be a set. The **power set** of $X$ is
>
> $$
> \mathcal{P}(X) = \{A \mid A \subseteq X\}.
> $$

^def-4-1

> [!remark]- Connections
> - Same definition: [[§6 The Language of Set Theory#^def-6-9|250 Def. §6.9]].

> [!theorem] Theorem §4.1: Cantor's Theorem
> For any set $X$, we have $X \not\sim \mathcal{P}(X)$. That is, there is no bijection from $X$ to its power set.

^thm-4-1

> [!proof]+ Proof
> Suppose for contradiction that there exists a bijection $f: X \to \mathcal{P}(X)$.
>
> Let $A = \{x \in X \mid x \notin f(x)\}$. Then $A \subseteq X$, so $A \in \mathcal{P}(X)$.
>
> Since $f$ is surjective, there exists $y \in X$ such that $A = f(y)$.
>
> **Case 1:** If $y \in A = f(y)$, then by definition of $A$, we have $y \notin f(y)$. Contradiction.
>
> **Case 2:** If $y \notin A = f(y)$, then by definition of $A$, we have $y \in A$. Contradiction.
>
> Thus $f$ is not surjective, hence not a bijection.

^pf-4-1

*Uses:* [[§4 Uncountability#^def-4-1|Def. §4.1]], [[§1 Countability and Set Theory#^def-1-4|Def. §1.4]], [[§1 Countability and Set Theory#^def-1-6|Def. §1.6]]

> [!remark]- Connections
> - Elementary version: [[§14 Counting Infinite Sets#^thm-14-13|250 Thm. §14.13]] (stated as an inequality of cardinalities, with the same diagonal set).
