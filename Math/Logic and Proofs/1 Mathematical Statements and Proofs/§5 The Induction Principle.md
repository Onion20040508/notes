---
type: section
subject: "[[Logic and Proofs]]"
chapter: 1
section: 5
eccles: "Ch. 5"
aliases: ["Eccles 5"]
tags: [logic-and-proofs, mat250]
---
← [[§4 Proof by Contradiction]] · ↑ [[· 1 Mathematical Statements and Proofs]] · [[§6 The Language of Set Theory]] →

*Eccles, Chapter 5 and Problems I (Q12, Q14, Q16, Q18, Q22) · MAT 250 HW1 (Exercises 5.1, 5.3, 5.4, 5.6, 5.7) · MAT 250 HW2 (Problems I Q12–Q22) · MAT 250 HW3 (Exercise 7.9).*

The rules of arithmetic and order do not capture the fact that every positive integer is reached from $1$ by adding $1$ enough times. The induction principle states this as an axiom, and it gives the most important method for proving statements about all positive integers. This section states the principle, shows how to write inductive proofs, moves the base case, uses induction to define sums, products, powers and factorials, and derives the strong induction principle, which handles sequences such as the Fibonacci numbers.

## 5.1 Proof by Induction

> [!definition] Definition §5.1: The Induction Principle
> **Axiom.** Let $P(n)$ be a statement involving a general positive integer $n$. Then $P(n)$ is true for all positive integers $n$ if
> 1. $P(1)$ is true (the **base case**), and
> 2. $P(k) \Rightarrow P(k + 1)$ for every positive integer $k$ (the **inductive step**; $P(k)$ is the **inductive hypothesis**).
>
> *Eccles: Axiom 5.1.1*

^def-5-1

> [!remark]- Connections
> - In analysis, with $\mathbb{N} = \{1, 2, \ldots\}$: induction is Peano's axiom N5 ([[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]]), from which the principle is derived ([[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 Thm. §1.1]]).

> [!remark] Remark: Why Induction Is an Axiom
> The integer $k + 1$ is the **successor** of $k$, and starting from $1$ and taking successors repeatedly we eventually reach any positive integer: from $P(1)$ and $P(1) \Rightarrow P(2)$ we get $P(2)$, then $P(2) \Rightarrow P(3)$ gives $P(3)$, and so on. Think of the positive integers as a line of dominoes: the inductive step says each domino knocks over the next, the base case that the first one falls. (The analogy is imperfect: dominoes take time to fall, while implication is outside time.) This seems obvious because our idea of the integers includes more than the facts that they can be added, multiplied and compared; the induction principle is exactly that extra content, an axiom in addition to the algebraic and order axioms ([[§2 Implications#^def-2-8|Def. §2.8]], [[§3 Proofs#^def-3-1|Def. §3.1]]). Checking cases is never a proof: the Goldbach conjecture ([[§1 The Language of Mathematics#^ex-1-1|Ex. §1.1]]) has been verified in an enormous number of cases and is still unproved. The integers are characterized as an ordered integral domain whose positive elements satisfy induction, and the positive integers alone by Peano's axioms, one of which is induction ([[§9 Injections, Surjections and Bijections#^def-9-6|Def. §9.6]], axiom 3): "the essence of the natural number concept is … closure under the successor operation" (Dedekind, 1888). In the language of sets the principle says that a subset of $\mathbb{Z}^+$ which contains $1$ and contains $k + 1$ whenever it contains $k$ is the whole of $\mathbb{Z}^+$; this **set form** is [[§7 Quantifiers#^def-7-4|Def. §7.4]], where it is shown to be equivalent to the version above.

^rem-5-1

> [!theorem] Proposition §5.1: Powers of Two Beat the Integers
> For all positive integers $n$, $n \leq 2^n$.
>
> *Eccles: Proposition 5.1.2*

^prop-5-1

> [!proof]+ Proof
> Here $P(n)$ is the statement $n \leq 2^n$. We use induction on $n$.
>
> *Base case.* For $n = 1$, $2^n = 2$, and $1 \leq 2$.
>
> *Inductive step.* Suppose, as inductive hypothesis, that $k \leq 2^k$ for a positive integer $k$. Then
>
> $$
> 2^{k+1} = 2 \times 2^k \geq 2k = k + k \geq k + 1,
> $$
>
> using the inductive hypothesis and then $k \geq 1$. So $k + 1 \leq 2^{k+1}$.
>
> *Conclusion.* Hence, by induction, $n \leq 2^n$ for all positive integers $n$.

^pf-5-1

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]], [[§3 Proofs#^ex-3-4|Ex. §3.4]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]

To find the inductive step we related the goal $k + 1 \leq 2^{k+1}$ to the hypothesis $k \leq 2^k$, starting from one side of the goal; starting from the other side also works: $k + 1 \leq 2^k + 1 \leq 2^k + k \leq 2^k + 2^k = 2^{k+1}$.

> [!remark] Remark: A Template for Proofs by Induction
> First identify the statement $P(n)$, and write down what $P(1)$, $P(k)$ and $P(k + 1)$ say. Then:
>
> *Proof.* We use induction on $n$.
> *Base case:* [prove $P(1)$].
> *Inductive step:* Suppose now, as inductive hypothesis, that [$P(k)$ is true] for some positive integer $k$. Then [deduce that $P(k+1)$ is true]. This proves the inductive step.
> *Conclusion:* Hence, by induction, [$P(n)$ is true] for all positive integers $n$. $\square$
>
> The first two parts verify the conditions of [[§5 The Induction Principle#^def-5-1|Def. §5.1]] and the last invokes it. Using a new letter $k$ in the inductive step, rather than $n$ again, makes $P(k + 1)$ easy to write down correctly by substituting $k + 1$ for $n$; getting $P(k + 1)$ wrong is the most common error in inductive proofs.

^rem-5-2

> [!theorem] Proposition §5.2: An Even Quadratic
> For all positive integers $n$, the number $n^2 + n$ is even.
>
> *Eccles: Proposition 5.1.3*

^prop-5-2

> [!proof]+ Proof
> We use induction on $n$. Here $P(n)$ is "$n^2 + n$ is even", i.e. "$n^2 + n = 2q$ for some integer $q$".
>
> *Base case.* For $n = 1$, $n^2 + n = 2 = 2 \times 1$, which is even.
>
> *Inductive step.* Suppose that $k^2 + k$ is even for some positive integer $k$: $k^2 + k = 2q$ for an integer $q$. The statement $P(k+1)$ is "$(k+1)^2 + (k+1)$ is even", and
>
> $$
> (k+1)^2 + (k+1) = k^2 + 2k + 1 + k + 1 = (k^2 + k) + 2k + 2 = 2q + 2k + 2 = 2(q + k + 1),
> $$
>
> where $q + k + 1$ is an integer. So $(k+1)^2 + (k+1)$ is even.
>
> *Conclusion.* Hence, by induction, $n^2 + n$ is even for all positive integers $n$.

^pf-5-2

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§2 Implications#^def-2-6|Def. §2.6]], [[§2 Implications#^def-2-7|Def. §2.7]]

## 5.2 Changing the Base Case

> [!theorem] Theorem §5.3: Induction from Any Base Case
> Let $n_0$ be an integer (positive, negative or zero) and $P(n)$ a statement involving a general integer $n \geq n_0$. If $P(n_0)$ is true, and $P(k) \Rightarrow P(k + 1)$ for every integer $k \geq n_0$, then $P(n)$ is true for all integers $n \geq n_0$. In particular ($n_0 = 0$), induction may be used on $\mathbb{N}$.
>
> *Eccles: Section 5.2*

^thm-5-3

> [!proof]+ Proof
> For positive integers $m$ let $Q(m)$ be the statement $P(m + n_0 - 1)$. Then $Q(1)$ is $P(n_0)$, which is true. If $Q(m)$ is true for a positive integer $m$, put $k = m + n_0 - 1$; then $k \geq n_0$ (as $m \geq 1$, [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]), so $P(k) \Rightarrow P(k+1)$ gives $P(k + 1)$, which is $Q(m + 1)$. By [[§5 The Induction Principle#^def-5-1|Def. §5.1]], $Q(m)$ holds for all positive integers $m$. Finally, if $n \geq n_0$ then $m = n - n_0 + 1 \geq 1$ is a positive integer, and $P(n) = Q(m)$ is true.

^pf-5-3

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]

> [!remark]- Connections
> - The same shift $Q_m := P_{n_0 + m - 1}$ in analysis: [[§1 The Set ℕ of Natural Numbers#^rem-1-4|451 §1, remark after Ex. §1.3]].

So the template is unchanged except that the base case is $P(n_0)$ and the inductive step is proved for $k \geq n_0$. Calculating $n^2$ and $2^n$ for small $n$ ($1, 4, 9, 16, 25, 36$ against $2, 4, 8, 16, 32, 64$) suggests the following.

> [!theorem] Proposition §5.4: Squares Against Powers of Two
> For all integers $n \geq 4$, $n^2 \leq 2^n$.
>
> *Eccles: Proposition 5.2.1*

^prop-5-4

> [!proof]+ Proof
> We use induction on $n$, with base case $n = 4$ ([[§5 The Induction Principle#^thm-5-3|Theorem §5.3]]).
>
> *Base case.* For $n = 4$, $n^2 = 16 = 2^n$, so $n^2 \leq 2^n$.
>
> *Inductive step.* Suppose $k^2 \leq 2^k$ for some $k \geq 4$. Then $2^{k+1} = 2 \times 2^k \geq 2k^2$, so it suffices to prove $2k^2 \geq (k+1)^2$, i.e. $2k^2 \geq k^2 + 2k + 1$, i.e. $k^2 \geq 2k + 1$. Since $k \geq 4$,
>
> $$
> k^2 \geq 4k = 2k + 2k \geq 2k + 2 \geq 2k + 1 .
> $$
>
> Hence $2^{k+1} \geq 2k^2 \geq (k+1)^2$.
>
> *Conclusion.* Hence, by induction, $n^2 \leq 2^n$ for all $n \geq 4$.

^pf-5-4

*Uses:* [[§5 The Induction Principle#^thm-5-3|§5.3]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]], [[§3 Proofs#^ex-3-4|Ex. §3.4]]

> [!remark]- Connections
> - The same inequality, $2^n > n^2$ for $n \geq 5$, in analysis: [[§1 The Set ℕ of Natural Numbers#^ex-1-3|451 Ex. §1.3]].

(The inequality holds for $n = 1, 2$ but fails for $n = 3$ ($9 > 8$). The inductive step works for every $k \geq 3$, since then $k^2 \geq 3k \geq 2k + 1$; but $P(3)$ is false, so the induction must start at $4$.)

## 5.3 Definition by Induction

A line of dots meaning "and so on", as in $1 + 2 + \cdots + n$, indicates a **definition by induction** (or by recursion): the base case says what the notation means for $n = 1$, and the inductive step what it means for $n = k + 1$ in terms of its meaning for $n = k$.

> [!definition] Definition §5.2: Sums and Products
> Given numbers $a(1), a(2), \ldots$, the numbers $\sum_{i=1}^n a(i)$ and $\prod_{i=1}^n a(i)$ for positive integers $n$ are defined inductively by
>
> $$
> \sum_{i=1}^{1} a(i) = a(1), \qquad \sum_{i=1}^{k+1} a(i) = \sum_{i=1}^{k} a(i) + a(k+1) \quad (k \geq 1);
> $$
>
> $$
> \prod_{i=1}^{1} a(i) = a(1), \qquad \prod_{i=1}^{k+1} a(i) = \Bigl(\prod_{i=1}^{k} a(i)\Bigr) a(k+1) \quad (k \geq 1).
> $$
>
> Sums and products starting from another index, such as $\sum_{i=0}^n$, are defined in the same way. For instance $\sum_{i=1}^3 a(i) = \sum_{i=1}^2 a(i) + a(3) = \sum_{i=1}^1 a(i) + a(2) + a(3) = a(1) + a(2) + a(3)$.
>
> *Eccles: Definition 5.3.2; Problems I Q18*

^def-5-2

> [!theorem] Proposition §5.5: The Sum of the First n Positive Integers
> For positive integers $n$,
>
> $$
> \sum_{i=1}^n i = \tfrac12 n(n+1).
> $$
>
> *Eccles: Proposition 5.3.1*

^prop-5-5

> [!proof]+ Proof
> We use induction on $n$.
>
> *Base case.* For $n = 1$, $\sum_{i=1}^1 i = 1$ and $\tfrac12 \cdot 1 \cdot 2 = 1$.
>
> *Inductive step.* Suppose $\sum_{i=1}^k i = \tfrac12 k(k+1)$ for some positive integer $k$. Then, by [[§5 The Induction Principle#^def-5-2|Def. §5.2]],
>
> $$
> \sum_{i=1}^{k+1} i = \sum_{i=1}^{k} i + (k + 1) = \tfrac12 k(k+1) + (k+1) = \tfrac12 (k+1)(k+2).
> $$
>
> *Conclusion.* Hence, by induction, $\sum_{i=1}^n i = \tfrac12 n(n+1)$ for all positive integers $n$.

^pf-5-5

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§5 The Induction Principle#^def-5-2|Def. §5.2]]

Inductive definitions are implicit in many familiar functions of the non-negative integers.

> [!definition] Definition §5.3: Powers
> For a real number $x$, the powers $x^n$ for $n \in \mathbb{N}$ are defined inductively by
>
> $$
> x^0 = 1, \qquad x^{k+1} = x \cdot x^k \quad (k \geq 0).
> $$
>
> In $x^n$, $n$ is the **index** or **exponent** and $x$ the **base**. The definition allows $x = 0$ and sets $0^0 = 1$, the right convention for formulas like $\sum_{i=0}^n x^i = 1 + x + \cdots + x^n$; in other contexts $0^0$ has no sensible value.
>
> *Eccles: Definition 5.3.3*

^def-5-3

> [!definition] Definition §5.4: Factorials
> For $n \in \mathbb{N}$, the numbers $n!$ (**factorial $n$**) are defined inductively by
>
> $$
> 0! = 1, \qquad (k+1)! = (k+1) \times k! \quad (k \geq 0).
> $$
>
> *Eccles: Definition 5.3.4*

^def-5-4

Even addition and multiplication of positive integers can be defined inductively from the successor operation ([[§9 Injections, Surjections and Bijections#^def-9-7|Def. §9.7]]).

## 5.4 The Strong Induction Principle

Sometimes $P(k + 1)$ follows not from $P(k)$ alone but from $P(k)$ together with some or all of $P(1), \ldots, P(k - 1)$.

> [!theorem] Theorem §5.6: The Strong Induction Principle
> Let $P(n)$ be a statement involving a general positive integer $n$. Then $P(n)$ is true for all positive integers $n$ if
> 1. $P(1)$ is true, and
> 2. for every positive integer $k$: [$P(n)$ holds for all positive integers $n \leq k$] $\Rightarrow$ $P(k + 1)$.
>
> *Eccles: Axiom 5.4.1*

^thm-5-6

> [!proof]+ Proof
> Eccles states this as an axiom and remarks that it is equivalent to [[§5 The Induction Principle#^def-5-1|Def. §5.1]]; we deduce it. Let $Q(n)$ be the statement "$P(m)$ is true for every positive integer $m \leq n$".
>
> *Base case.* A positive integer $m \leq 1$ satisfies $m \geq 1$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]), so $m = 1$ ([[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]]); hence $Q(1)$ says just $P(1)$, which is true by (1).
>
> *Inductive step.* Suppose $Q(k)$ for a positive integer $k$, i.e. $P(m)$ for all positive $m \leq k$. By (2), $P(k + 1)$ is true. A positive integer $m \leq k + 1$ satisfies $m \leq k$ or $m = k + 1$, since no integer lies strictly between $k$ and $k + 1$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]); so $P(m)$ holds for all positive $m \leq k + 1$, which is $Q(k+1)$.
>
> *Conclusion.* By induction $Q(n)$ is true for every positive integer $n$; taking $m = n$ in $Q(n)$ gives $P(n)$.

^pf-5-6

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]], [[§4 Proof by Contradiction#^ex-4-4|Ex. §4.4]]

> [!remark]- Connections
> - The same device (strengthening $P_n$ to "for all $k \leq n$") in analysis: [[§1 The Set ℕ of Natural Numbers#^ex-1-2|451 Ex. §1.2]] and the remark after it.

The template is that of [[§5 The Induction Principle#^rem-5-2|the remark above]], with inductive hypothesis "$P(n)$ is true for all positive integers $n \leq k$". Apart from the well-ordering principle below, Eccles next needs the method in [[§23 The Sequence of Prime Numbers#^prop-23-1|Proposition §23.1]] (every integer greater than $1$ is a product of primes).

> [!theorem] Corollary §5.7: The Well-Ordering Principle
> 1. Every non-empty set of positive integers has a least element.
> 2. More generally, for any integer $n_0$, every non-empty set of integers $n \geq n_0$ has a least element; in particular ($n_0 = 0$) every non-empty set of non-negative integers has one.
>
> Here a **least element** of $A$ is an $m \in A$ with $m \leq a$ for every $a \in A$.
>
> *Eccles: Example 11.2.2(c), Exercise 11.6*
> *Source: standard (part 2)*

^cor-5-7

> [!proof]+ Proof
> (1) We prove the contrapositive: if a set $A$ of positive integers has no least element, then $A$ is empty. Let $P(n)$ be the statement "$n \notin A$"; we use strong induction ([[§5 The Induction Principle#^thm-5-6|Theorem §5.6]]).
>
> *Base case.* Every positive integer is $\geq 1$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]), so if $1 \in A$ it would be the least element of $A$. Hence $1 \notin A$.
>
> *Inductive step.* Suppose that $n \notin A$ for every positive integer $n \leq k$. If $k + 1 \in A$, let $a \in A$. Then $a$ is a positive integer, and $a \leq k$ is impossible (such integers are not in $A$), so $a > k$ by trichotomy and hence $a \geq k + 1$ ([[§5 The Induction Principle#^ex-5-2|Ex. §5.2]]). Then $k + 1$ would be the least element of $A$. Hence $k + 1 \notin A$.
>
> *Conclusion.* No positive integer lies in $A$, so $A = \varnothing$.
>
> (2) Let $A$ be a non-empty set of integers $n \geq n_0$, and let $B$ be the set of the integers $a - n_0 + 1$ for $a \in A$. Each of them is $\geq 1$ (addition law), so $B$ is a non-empty set of positive integers, and by (1) it has a least element, $a_0 - n_0 + 1$ say, with $a_0 \in A$. For every $a \in A$, $a - n_0 + 1 \geq a_0 - n_0 + 1$, so $a \geq a_0$. Thus $a_0$ is the least element of $A$.

^pf-5-7

*Uses:* [[§5 The Induction Principle#^thm-5-6|§5.6]], [[§5 The Induction Principle#^ex-5-2|Ex. §5.2]], [[§3 Proofs#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - The same proof in analysis: [[§1 The Set ℕ of Natural Numbers#^thm-1-2|451 Thm. §1.2]].

Conversely, the induction principle can be deduced from well-ordering (Eccles, Problems III Q15; compare the second proof in [[§5 The Induction Principle#^ex-5-9|Ex. §5.9]]), so the two are equivalent. Arguments of the form "take the least counterexample" are applications of well-ordering. The positive reals have no such property ([[§4 Proof by Contradiction#^ex-4-7|Ex. §4.7]]); in [[§11 Properties of Finite Sets#^ex-11-3|Ex. §11.3]](c) well-ordering reappears among the properties of maxima and minima.

> [!definition] Definition §5.5: Fibonacci Numbers
> The **Fibonacci numbers** $u_n$, $n \in \mathbb{Z}^+$, are defined inductively by
>
> $$
> u_1 = 1, \qquad u_2 = 1, \qquad u_{k+1} = u_{k-1} + u_k \quad (k \geq 2).
> $$
>
> The sequence begins $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, \ldots$. Each term is determined by the previous *two*, so the first two must be given as base cases.
>
> *Eccles: Definition 5.4.2*

^def-5-5

> [!theorem] Proposition §5.8: The Binet Formula
> The Fibonacci numbers are given by
>
> $$
> u_n = \frac{\alpha^n - \beta^n}{\sqrt5}, \qquad \text{where } \alpha = \frac{1 + \sqrt5}{2}, \quad \beta = \frac{1 - \sqrt5}{2}.
> $$
>
> *Eccles: Proposition 5.4.3*

^prop-5-8

> [!proof]+ Proof
> The numbers $\alpha$ and $\beta$ are the roots of $x^2 - x - 1 = 0$: for instance $\alpha^2 = \frac{6 + 2\sqrt5}{4} = \frac{3 + \sqrt5}{2} = \alpha + 1$, and likewise $\beta^2 = \beta + 1$. We use strong induction on $n$ ([[§5 The Induction Principle#^thm-5-6|Theorem §5.6]]); $P(n)$ is the formula.
>
> *Base cases.* For $n = 1$: $(\alpha - \beta)/\sqrt5 = \sqrt5/\sqrt5 = 1 = u_1$. The recurrence only starts at $u_3$, so $n = 2$ is checked directly too: $(\alpha^2 - \beta^2)/\sqrt5 = ((\alpha + 1) - (\beta + 1))/\sqrt5 = (\alpha - \beta)/\sqrt5 = 1 = u_2$. This proves the inductive step for $k = 1$.
>
> *Inductive step.* Suppose the formula holds for all positive integers $n \leq k$, for some $k \geq 2$. Then
>
> $$
> \begin{aligned}
> u_{k+1} &= u_{k-1} + u_k = \frac{(\alpha^{k-1} - \beta^{k-1}) + (\alpha^k - \beta^k)}{\sqrt5} \\
> &= \frac{\alpha^{k-1}(1 + \alpha) - \beta^{k-1}(1 + \beta)}{\sqrt5} = \frac{\alpha^{k-1}\alpha^2 - \beta^{k-1}\beta^2}{\sqrt5} = \frac{\alpha^{k+1} - \beta^{k+1}}{\sqrt5},
> \end{aligned}
> $$
>
> using the inductive hypothesis for $n = k - 1$ and $n = k$, then $1 + \alpha = \alpha^2$, $1 + \beta = \beta^2$ and the laws of exponents ([[§5 The Induction Principle#^ex-5-5|Ex. §5.5]]).
>
> *Conclusion.* Hence, by strong induction, the formula holds for all positive integers $n$.

^pf-5-8

*Uses:* [[§5 The Induction Principle#^thm-5-6|§5.6]], [[§5 The Induction Principle#^def-5-5|Def. §5.5]], [[§5 The Induction Principle#^ex-5-5|Ex. §5.5]]

It is remarkable that a formula for these integers involves $\sqrt5$, which is not even rational (the proof for $\sqrt2$ in [[§13 Number Systems#^thm-13-4|Theorem §13.4]] adapts to it, and [[§23 The Sequence of Prime Numbers#^ex-23-6|Ex. §23.6]] covers $\sqrt p$ for every prime $p$). The ratio $u_{n+1}/u_n$ tends to $\alpha$, the **golden ratio** (since $|\beta| < 1$).

## Exercises from the Homework

> [!example] Example §5.1: Divisibility by 3
> For all positive integers $n$: (a) $3 \mid n^3 - n$; (b) $3 \mid 4^n + 5$.
>
> **Solution.** (a) *Base case:* $1^3 - 1 = 0 = 3 \times 0$. *Inductive step:* suppose $k^3 - k = 3q$ for an integer $q$. Then
>
> $$
> (k+1)^3 - (k+1) = k^3 + 3k^2 + 3k + 1 - k - 1 = (k^3 - k) + 3(k^2 + k) = 3(q + k^2 + k).
> $$
>
> (We name the new quotient $q + k^2 + k$; reusing the letter $q$ would be wrong.) By induction $3 \mid n^3 - n$ for all $n \in \mathbb{Z}^+$.
>
> (b) *Base case:* $4 + 5 = 9 = 3 \times 3$. *Inductive step:* suppose $4^k + 5 = 3q$. Then $4^{k+1} + 5 = 4(4^k + 5) - 15 = 12q - 15 = 3(4q - 5)$. By induction $3 \mid 4^n + 5$ for all $n \in \mathbb{Z}^+$.
>
> *Source: HW1 (part (a)); HW2 (part (b))*
> *Eccles: Exercise 5.1; Problems I Q12*

^ex-5-1

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§2 Implications#^def-2-6|Def. §2.6]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]]

> [!example] Example §5.2: Every Positive Integer Is at Least 1
> (a) For all positive integers $n$, $n \geq 1$. (b) Consequently, for integers $k$ and $m$, $m > k \Rightarrow m \geq k + 1$: no integer lies strictly between $k$ and $k + 1$.
>
> **Solution.** (a) We use induction on $n$. *Base case:* $1 \geq 1$. *Inductive step:* if $k \geq 1$, then $k + 1 > k$ (add $k$ to $1 > 0$, [[§3 Proofs#^cor-3-3|Corollary §3.3]]), so $k + 1 \geq 1$ by transitivity. Hence $n \geq 1$ for all positive integers $n$.
>
> (b) If $m > k$ then $m - k$ is an integer with $m - k > 0$, i.e. a positive integer, so $m - k \geq 1$ by (a), and $m \geq k + 1$ by the addition law.
>
> This looks too obvious to need proof, and it has been used as if self-evident (for instance in [[§2 Implications#^prop-2-5|Proposition §2.5]]); but it does not follow from the algebraic and order properties alone, and this is how it is deduced from the induction principle.
>
> *Source: HW1 (part (a))*
> *Eccles: Exercise 5.3*

^ex-5-2

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§3 Proofs#^cor-3-3|§3.3]], [[§3 Proofs#^def-3-1|Def. §3.1]]

> [!example] Example §5.3: Two Summation Formulas
> (a) For every real $x \neq 1$ and every $n \in \mathbb{N}$, $\displaystyle\sum_{i=0}^n x^i = \frac{1 - x^{n+1}}{1 - x}$ (the geometric progression).
> (b) For every positive integer $n$, $\displaystyle\sum_{i=1}^n \frac{1}{i(i+1)} = \frac{n}{n+1}$.
>
> **Solution.** (a) Induction on $n$ from $n = 0$ ([[§5 The Induction Principle#^thm-5-3|Theorem §5.3]]). *Base case:* $\sum_{i=0}^0 x^i = x^0 = 1 = \frac{1 - x}{1 - x}$. *Inductive step:* if the formula holds for $k \geq 0$, then
>
> $$
> \sum_{i=0}^{k+1} x^i = \frac{1 - x^{k+1}}{1 - x} + x^{k+1} = \frac{1 - x^{k+1} + x^{k+1} - x^{k+2}}{1 - x} = \frac{1 - x^{k+2}}{1 - x}.
> $$
>
> (b) *Base case:* $\frac{1}{1 \cdot 2} = \frac12 = \frac{1}{1+1}$. *Inductive step:* if the formula holds for $k$, then
>
> $$
> \sum_{i=1}^{k+1} \frac{1}{i(i+1)} = \frac{k}{k+1} + \frac{1}{(k+1)(k+2)} = \frac{k(k+2) + 1}{(k+1)(k+2)} = \frac{(k+1)^2}{(k+1)(k+2)} = \frac{k+1}{k+2}.
> $$
>
> (The sum telescopes, since $\frac{1}{i(i+1)} = \frac1i - \frac{1}{i+1}$.)
>
> *Source: HW1 (part (a)); HW2 (part (b))*
> *Eccles: Exercise 5.4; Problems I Q16*

^ex-5-3

*Uses:* [[§5 The Induction Principle#^thm-5-3|§5.3]], [[§5 The Induction Principle#^def-5-2|Def. §5.2]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]]

> [!example] Example §5.4: Solving a Recurrence
> Define $u_n$ for $n \in \mathbb{N}$ by $u_0 = 0$ and $u_{k+1} = 3u_k + 3^k$ for $k \geq 0$. Then $u_n = n \cdot 3^{n-1}$ for all $n \in \mathbb{N}$.
>
> **Solution.** Induction on $n$ from $n = 0$. *Base case:* $u_0 = 0 = 0 \cdot 3^{-1}$ (here $3^{-1} = \tfrac13$, but any value would give $0$). *Inductive step:* suppose $u_k = k \cdot 3^{k-1}$ for some $k \geq 0$. Then $3u_k = k \cdot 3^k$ (by [[§5 The Induction Principle#^def-5-3|Def. §5.3]] if $k \geq 1$; both sides are $0$ if $k = 0$), so
>
> $$
> u_{k+1} = 3u_k + 3^k = k \cdot 3^k + 3^k = (k + 1) \cdot 3^k,
> $$
>
> which is the formula for $n = k + 1$. Hence $u_n = n \cdot 3^{n-1}$ for all $n \in \mathbb{N}$.
>
> *Source: HW1*
> *Eccles: Exercise 5.6*

^ex-5-4

*Uses:* [[§5 The Induction Principle#^thm-5-3|§5.3]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]]

> [!example] Example §5.5: The Laws of Exponents
> For all real numbers $x$, $y$ and all $m, n \in \mathbb{N}$:
> (i) $x^n y^n = (xy)^n$; (ii) $x^{m+n} = x^m x^n$; (iii) $(x^m)^n = x^{mn}$.
>
> **Solution.** Each is proved by induction on $n$ from $n = 0$, with $m$ fixed, using [[§5 The Induction Principle#^def-5-3|Def. §5.3]].
>
> (i) *Base case:* $x^0 y^0 = 1 \cdot 1 = 1 = (xy)^0$. *Inductive step:* if $x^k y^k = (xy)^k$, then $x^{k+1} y^{k+1} = (x \cdot x^k)(y \cdot y^k) = (xy)(x^k y^k) = (xy)(xy)^k = (xy)^{k+1}$.
>
> (ii) *Base case:* $x^{m+0} = x^m = x^m \cdot 1 = x^m x^0$. *Inductive step:* if $x^{m+k} = x^m x^k$, then $x^{m+k+1} = x \cdot x^{m+k} = x \cdot x^m x^k = x^m (x \cdot x^k) = x^m x^{k+1}$.
>
> (iii) *Base case:* $(x^m)^0 = 1 = x^0 = x^{m \cdot 0}$. *Inductive step:* if $(x^m)^k = x^{mk}$, then $(x^m)^{k+1} = x^m (x^m)^k = x^m x^{mk} = x^{m + mk} = x^{m(k+1)}$, by the definition, the inductive hypothesis and (ii).
>
> *Source: HW1*
> *Eccles: Exercise 5.7*
>
> *In (iii) the first part of the HW1 solution, an induction on $m$, uses $(x^m \cdot x)^n = (x^{m+1})^n = x^{(m+1)n}$, which is the statement being proved; its second part, the induction on $n$ using (ii) given above, is valid on its own. (The "power rule" $x^n \cdot x = x^{n+1}$ proved there separately is [[§5 The Induction Principle#^def-5-3|Def. §5.3]] together with commutativity.)*

^ex-5-5

*Uses:* [[§5 The Induction Principle#^thm-5-3|§5.3]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]], [[§2 Implications#^def-2-8|Def. §2.8]]

> [!remark]- Connections
> - The laws for integer exponents in any group, with the same inductions: [[§4 Subgroups#^lem-4-4|493 Lemma §4.4]]. (Eccles extends them to negative exponents for non-zero reals in Problems I Q23.)

> [!example] Example §5.6: Bernoulli's Inequality
> For every $n \in \mathbb{N}$ and every real number $x > -1$, $(1 + x)^n \geq 1 + nx$.
>
> **Solution.** Induction on $n$ from $n = 0$. *Base case:* $(1 + x)^0 = 1 = 1 + 0 \cdot x$. *Inductive step:* suppose $(1 + x)^k \geq 1 + kx$ for some $k \geq 0$. Since $x > -1$, $1 + x > 0$, so multiplying by $1 + x$ preserves the inequality ([[§3 Proofs#^ex-3-4|Ex. §3.4]]):
>
> $$
> (1 + x)^{k+1} = (1 + x)(1 + x)^k \geq (1 + x)(1 + kx) = 1 + (k + 1)x + kx^2 \geq 1 + (k+1)x,
> $$
>
> because $kx^2 \geq 0$ ($k \geq 0$ and $x^2 \geq 0$, [[§3 Proofs#^cor-3-3|Corollary §3.3]]). This is the inequality for $n = k + 1$. The hypothesis $x > -1$ is used exactly once, to multiply by $1 + x$.
>
> *Source: HW2*
> *Eccles: Problems I Q14*

^ex-5-6

*Uses:* [[§5 The Induction Principle#^thm-5-3|§5.3]], [[§3 Proofs#^ex-3-4|Ex. §3.4]], [[§3 Proofs#^cor-3-3|§3.3]], [[§5 The Induction Principle#^def-5-3|Def. §5.3]]

> [!example] Example §5.7: A Telescoping Product
> For every positive integer $n$ and real $x \neq 1$,
>
> $$
> \prod_{i=1}^n \bigl(1 + x^{2^{i-1}}\bigr) = \frac{1 - x^{2^n}}{1 - x}.
> $$
>
> What happens if $x = 1$?
>
> **Solution.** *Base case:* $n = 1$: $1 + x = \frac{(1 - x)(1 + x)}{1 - x} = \frac{1 - x^2}{1 - x}$. *Inductive step:* if the formula holds for $k$, then by [[§5 The Induction Principle#^def-5-2|Def. §5.2]]
>
> $$
> \prod_{i=1}^{k+1} \bigl(1 + x^{2^{i-1}}\bigr) = \frac{1 - x^{2^k}}{1 - x}\bigl(1 + x^{2^k}\bigr) = \frac{1 - \bigl(x^{2^k}\bigr)^2}{1 - x} = \frac{1 - x^{2^{k+1}}}{1 - x},
> $$
>
> since $(x^{2^k})^2 = x^{2 \cdot 2^k} = x^{2^{k+1}}$ ([[§5 The Induction Principle#^ex-5-5|Ex. §5.5]](iii)). By induction the formula holds for all $n \in \mathbb{Z}^+$.
>
> If $x = 1$ the right side is undefined, but the product is defined: every factor is $1 + 1 = 2$, so the product is $2^n$ (a short induction). The two cases fit together: by [[§5 The Induction Principle#^ex-5-3|Ex. §5.3]](a), for $x \neq 1$ the right side equals $\sum_{i=0}^{2^n - 1} x^i$, and this sum is also $2^n$ at $x = 1$. So $\prod_{i=1}^n (1 + x^{2^{i-1}}) = \sum_{i=0}^{2^n - 1} x^i$ for every real $x$.
>
> *Source: HW2*
> *Eccles: Problems I Q18*
>
> *The HW2 solution leaves the case $x = 1$ as $0/0$; the product itself is defined there and equals $2^n$.*

^ex-5-7

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§5 The Induction Principle#^def-5-2|Def. §5.2]], [[§5 The Induction Principle#^ex-5-5|Ex. §5.5]], [[§5 The Induction Principle#^ex-5-3|Ex. §5.3]]

> [!example] Example §5.8: The Arithmetic–Geometric Mean Inequality
> For every positive integer $n$ and positive reals $x_1, \ldots, x_n$,
>
> $$
> \frac1n \sum_{i=1}^n x_i \;\geq\; \Bigl(\prod_{i=1}^n x_i\Bigr)^{1/n}.
> $$
>
> (Here $y^{1/n}$ is the positive real number whose $n$-th power is $y > 0$; its existence is assumed.)
>
> **Solution.** Two facts about non-negative reals, from [[§3 Proofs#^ex-3-4|Ex. §3.4]] and the multiplication law: (F1) if $0 \leq u \leq v$ then $u^n \leq v^n$, and if $0 \leq u < v$ then $u^n < v^n$ (induction on $n$: $u^{k+1} = u \cdot u^k \leq u \cdot v^k \leq v \cdot v^k$, with $<$ in the last step when $u < v$ and $v^k > 0$); (F2) if $0 \leq a \leq b$ and $0 \leq c \leq d$ then $ac \leq bc \leq bd$.
>
> Write $A$ for the mean $\frac1n \sum x_i$ and let $M(n)$ be the statement: $A^n \geq \prod_{i=1}^n x_i$ for all positive $x_1, \ldots, x_n$. This implies the inequality: if $A < G = (\prod x_i)^{1/n}$, then $A^n < G^n = \prod x_i$ by (F1). As Eccles's hint suggests, $M(n)$ is proved for powers of $2$ by induction and then extended downwards.
>
> *$M(2)$.* $\bigl(\frac{x_1 + x_2}{2}\bigr)^2 - x_1 x_2 = \bigl(\frac{x_1 - x_2}{2}\bigr)^2 \geq 0$.
>
> *$M(n) \Rightarrow M(2n)$.* Given $x_1, \ldots, x_{2n} > 0$, let $A'$ and $A''$ be the means of $x_1, \ldots, x_n$ and of $x_{n+1}, \ldots, x_{2n}$; the mean of all $2n$ is $A = \frac{A' + A''}{2}$. By $M(2)$, $A^2 \geq A'A'' > 0$, so by (F1), the laws of exponents ([[§5 The Induction Principle#^ex-5-5|Ex. §5.5]]), $M(n)$ twice and (F2),
>
> $$
> A^{2n} = (A^2)^n \geq (A'A'')^n = A'^n A''^n \geq \prod_{i=1}^n x_i \cdot \prod_{i=n+1}^{2n} x_i = \prod_{i=1}^{2n} x_i .
> $$
>
> Since $M(1)$ is trivial, induction on $m$ gives $M(2^m)$ for all $m \in \mathbb{N}$.
>
> *$M(k) \Rightarrow M(k - 1)$ for $k \geq 2$.* Given $x_1, \ldots, x_{k-1} > 0$ with mean $B$, put $x_k = B$. The mean of $x_1, \ldots, x_k$ is $\frac{(k-1)B + B}{k} = B$, so $M(k)$ gives $B^k \geq \bigl(\prod_{i=1}^{k-1} x_i\bigr) B$; dividing by $B > 0$, $B^{k-1} \geq \prod_{i=1}^{k-1} x_i$, which is $M(k-1)$.
>
> *Conclusion.* Given $n$, let $N = 2^n \geq n$ ([[§5 The Induction Principle#^prop-5-1|Proposition §5.1]]). $M(N)$ holds, and induction on $j$ (for $0 \leq j \leq N - n$, the backward step with $k = N - j \geq 2$) gives $M(N - j)$; at $j = N - n$ this is $M(n)$.
>
> *Source: HW2*
> *Eccles: Problems I Q22*

^ex-5-8

*Uses:* [[§5 The Induction Principle#^def-5-1|Def. §5.1]], [[§5 The Induction Principle#^def-5-2|Def. §5.2]], [[§5 The Induction Principle#^ex-5-5|Ex. §5.5]], [[§5 The Induction Principle#^prop-5-1|§5.1]], [[§3 Proofs#^ex-3-4|Ex. §3.4]], [[§3 Proofs#^cor-3-3|§3.3]]

> [!example] Example §5.9: Strong Induction for Subsets
> Reformulate the strong induction principle as a method of proving that a subset of $\mathbb{Z}^+$ is the whole set, in the manner of the set version of induction ([[§7 Quantifiers#^def-7-4|Def. §7.4]], Eccles's Axiom 7.5.1).
>
> *(Forward reference: this is Eccles's Exercise 7.9, placed here with strong induction. It is phrased in the language of sets of [[§6 The Language of Set Theory|§6]] and imitates the set form of induction in §7, but the solution uses only results of this section.)*
>
> **Solution.** *Let $A$ be a subset of $\mathbb{Z}^+$ such that (i) $1 \in A$, and (ii) for every positive integer $k$, if every positive integer $n \leq k$ lies in $A$ (that is, $\{1, \ldots, k\} \subseteq A$), then $k + 1 \in A$. Then $A = \mathbb{Z}^+$.*
>
> This is [[§5 The Induction Principle#^thm-5-6|Theorem §5.6]] applied to the statement $P(n)$: "$n \in A$". Conversely, Theorem §5.6 is recovered by applying it to $A = \{n \in \mathbb{Z}^+ \mid P(n)\}$.
>
> A second proof, by the least counterexample: suppose, for contradiction, that $A \neq \mathbb{Z}^+$. Then $F = \mathbb{Z}^+ - A$ is non-empty and has a least element $m$ (well-ordering, [[§5 The Induction Principle#^cor-5-7|Corollary §5.7]]). By (i), $m \neq 1$, so $k = m - 1$ is a positive integer. Every positive integer $n \leq k$ is less than $m$, hence not in $F$, hence in $A$; by (ii), $m = k + 1 \in A$, contradicting $m \in F$. So $A = \mathbb{Z}^+$. (Since Corollary §5.7 was itself proved by strong induction, this second proof is not a new derivation; what it shows is that well-ordering, if taken as the axiom, implies strong induction.)
>
> *Source: HW3*
> *Eccles: Exercise 7.9*
>
> *The HW3 solution writes "$F$ has no least element" as "for all $x \in F$ there is no $y \in F$ with $y \leq x$", which fails for $y = x$; the correct form is "for every $x \in F$ there is $y \in F$ with $y < x$" ([[§7 Quantifiers#^thm-7-2|Theorem §7.2]]), and the argument is completed by the well-ordering principle as above.*

^ex-5-9

*Uses:* [[§5 The Induction Principle#^thm-5-6|§5.6]], [[§5 The Induction Principle#^cor-5-7|§5.7]], [[§4 Proof by Contradiction#^thm-4-2|§4.2]]
