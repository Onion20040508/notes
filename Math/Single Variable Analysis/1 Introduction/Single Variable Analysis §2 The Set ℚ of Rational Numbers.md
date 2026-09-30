---
subject: "[[Single Variable Analysis]]"
section: 2
chapter: 1
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §1 The Set ℕ of Natural Numbers]] · ↑ [[Single Variable Analysis — 1 Introduction]] · [[Single Variable Analysis §3 The Set ℝ of Real Numbers]] →

## From $\mathbb{N}$ to $\mathbb{Q}$: Algebraic Structures

There are four basic arithmetic operations: $+$, $-$, $\times$, and division. Probably the most basic one is $+$, and $\mathbb{N}$ is closed under it: for any $m, n \in \mathbb{N}$, we have $m + n \in \mathbb{N}$.

> [!definition] Definition §2.1: Semigroup
> This is related to an important notion in abstract algebra: a **semigroup** is an object with an (associative) operation $+$ under which it is closed. So $\mathbb{N}$ is a semigroup.

^def-2-1

But $\mathbb{N}$ is *not* closed under $-$: if $n > m$, then $m - n \notin \mathbb{N}$. So we need negative integers, and also the zero $0$. Adjoining to $\mathbb{N}$ the number $0$ and, for each $n \in \mathbb{N}$, its negative $-n$, we obtain the set of all integers $\mathbb{Z}$.

> [!definition] Definition §2.2: Group
> A **group** is a set with an operation $+$ such that every element $n$ has an inverse $-n$. So $\mathbb{Z}$ is a group under $+$, while $\mathbb{N}$ is only a semigroup.

^def-2-2

Next, $\mathbb{Z}$ is also closed under multiplication: for $m, n \in \mathbb{Z}$, $m \times n \in \mathbb{Z}$. We now have two operations $+, \times$, plus the inverse of $+$ (negative numbers), all compatible with each other, and $\mathbb{Z}$ is closed under all of them.

> [!definition] Definition §2.3: Ring
> A **ring** is a set with two compatible operations $+, \times$, closed under both, in which every element has an inverse for $+$ (but not necessarily for $\times$). So $\mathbb{Z}$ is a ring.

^def-2-3

Unfortunately, $\mathbb{Z}$ is not closed under division: for $m, n \in \mathbb{Z}$, the quotient $m/n$ may not belong to $\mathbb{Z}$. Writing

$$
m/n = m \times n^{-1},
$$

what is special about $n^{-1}$ is that $n \times n^{-1} = 1$: it is the inverse of $n$ with respect to *multiplication*. Including all such multiplicative inverses (of nonzero elements), we obtain the rational numbers $\mathbb{Q}$, which are closed under all four basic operations.

> [!definition] Definition §2.4: Field
> A **field** is a set with two compatible operations $+, \times$ *and their inverses* (the inverse for $\times$ existing for every nonzero element), closed under all of them. $\mathbb{Q}$ is an important example of a field; we will see that $\mathbb{R}$ and $\mathbb{C}$ are also fields. The precise list of field axioms is given in §3.

^def-2-4

> [!remark] Remark
> The notions of semigroup, group, ring, and field are all basic objects of abstract algebra; here they are stated informally, in the commutative setting relevant to numbers. Each stage of the chain $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q}$ is the closure of the previous one under one more operation.

^rem-2-1

## $\sqrt{2}$ Is Not Rational

So we should be happy with $\mathbb{Q}$ — but not so. One reason, mentioned in §1's overview: to take limits and have limits *exist*, we need the real numbers $\mathbb{R}$; this is the completeness of $\mathbb{R}$ (more later). But there was another reason, found much earlier by the Greeks: $\mathbb{Q}$ is not closed under taking square roots.

> [!theorem] Theorem §2.1: Irrationality of $\sqrt{2}$
> $\sqrt{2} \notin \mathbb{Q}$.

^thm-2-1

> [!proof]+ Proof
> Proof by contradiction. Suppose $\sqrt{2} = p/q$ with $p, q$ integers, $q \neq 0$. We may assume $p, q$ are *coprime*: this is the best representative, obtained by dividing out all common prime factors of $p$ and $q$.
>
> Squaring $\sqrt{2}\, q = p$ gives
>
> $$
> 2q^2 = p^2.
> $$
>
> Thus $2 \mid p^2$, which implies $2 \mid p$ (if $p$ were odd, say $p = 2k+1$, then $p^2 = 4k^2 + 4k + 1$ would be odd). Write $p = 2m$ with $m \in \mathbb{Z}$. Then
>
> $$
> 2q^2 = 4m^2, \qquad \text{hence} \qquad q^2 = 2m^2.
> $$
>
> By the same argument, $2 \mid q$. So $2$ divides both $p$ and $q$, contradicting the assumption that $p, q$ are coprime. Therefore $\sqrt{2} \notin \mathbb{Q}$.

^pf-2-1

> [!remark] Remark
> This is the method of **proof by contradiction**, one very important method of proof. The other basic method we have seen is proof by induction (§1).

^rem-2-2

> [!remark] Remark: Why this result was a big deal
> Pythagoras famously said that *all things are numbers*: all quantities can be measured by integers and rational numbers once some unit is chosen. His school was a secret society built partly on this belief. Now take a unit square, with sides of length $1$. By the Pythagorean Theorem, its diagonal has length $\sqrt{2}$ — a completely natural geometric quantity. The theorem above says this length *cannot* be measured by rational numbers: the sky was falling. Legend has it that the discoverer was thrown into the ocean to bury the secret.

^rem-2-3

The divisibility argument above adapts to $\sqrt3$, $\sqrt5$, and beyond — but a bookkeeping of prime factorizations settles *all* square roots of integers at once. We cite one standard fact from elementary number theory (not proved in this course):

> [!remark] Remark: Cited fact: the Fundamental Theorem of Arithmetic
> Every positive integer can be expressed as $\prod_{i=1}^{\infty} p_i^{\,n_i}$, where $p_1 < p_2 < \cdots$ lists the primes and the $n_i$ are nonnegative integers, all but finitely many zero (e.g. $1 = \prod_i p_i^0$, $2 = 2^1\cdot3^0\cdots$, $24 = 2^3\cdot3^1\cdot5^0\cdots$) — and this expression is *unique*: if $\prod_i p_i^{\alpha_i} = \prod_i p_i^{\beta_i}$, then $\alpha_i = \beta_i$ for every $i$.

^rem-2-4

> [!theorem] Proposition §2.2: Rational Square Roots of Integers (HW)
> Let $m$ be a positive integer. Then $\sqrt m \in \mathbb{Q}$ if and only if $m$ is a perfect square. Equivalently: if some prime appears in the factorization of $m$ with an *odd* exponent, then $\sqrt m \notin \mathbb{Q}$.

^prop-2-2

> [!proof]+ Proof
> If $m = d^2$, then $\sqrt m = d \in \mathbb{Q}$. Conversely, suppose $\sqrt m \in \mathbb{Q}$ and $m$ is not a perfect square; we derive a contradiction. Write $m = \prod_i p_i^{\,k_i}$; since $m$ is not a perfect square, some exponent is odd, say $k_j$. Since $\sqrt m > 0$, we may write
>
> $$
> \sqrt m = \frac{P}{Q}, \qquad P, Q \in \mathbb{Z}^+,
> $$
>
> so that $Q\sqrt m = P$. As positive integers, $P$ and $Q$ have their own factorizations,
>
> $$
> P = \prod_{i=1}^\infty p_i^{\,n_i}, \qquad Q = \prod_{i=1}^\infty p_i^{\,m_i},
> $$
>
> with all but finitely many exponents zero. Squaring $Q\sqrt m = P$:
>
> $$
> P^2 = Q^2 m, \qquad \text{i.e.} \qquad \prod_{i=1}^\infty p_i^{\,2n_i} = \prod_{i=1}^\infty p_i^{\,2m_i + k_i}.
> $$
>
> By the uniqueness part of the FTA, the exponents of $p_j$ on the two sides must agree:
>
> $$
> 2n_j = 2m_j + k_j.
> $$
>
> But the left side is even, while the right side is odd (since $k_j$ is odd) — contradiction. Hence $\sqrt m$ cannot be written as $\tfrac PQ$, so $\sqrt m \notin \mathbb{Q}$.

^pf-2-2

> [!example] Example §2.1: Instances (HW)
> $\sqrt3, \sqrt5, \sqrt7, \sqrt{31} \notin \mathbb{Q}$: each of $3, 5, 7, 31$ is prime, so it appears in itself with exponent $1$, odd. $\sqrt{24} \notin \mathbb{Q}$: here $24 = 2^3 \cdot 3^1$, and *both* exponents are odd — either prime alone yields the parity contradiction. The criterion also re-proves $\sqrt2 \notin \mathbb{Q}$ and covers $\sqrt6$ ($6 = 2^1\cdot3^1$), used below.

^ex-2-1

> [!remark] Remark
> Note what the parity proof does *not* need: no reduction of $\tfrac PQ$ to lowest terms. The coprimality assumption of Theorem 2.1 — and the “divide out common factors” step it rests on — is replaced wholesale by the uniqueness clause of the FTA, which tracks every prime at once.

^rem-2-5

## Algebraic Numbers

From the algebraic point of view, what comes after $\mathbb{Q}$? We know $\mathbb{Q}$ is not closed under square roots: $\sqrt{2}, \sqrt{3}, \sqrt{5} \notin \mathbb{Q}$.

**Question.** If we adjoin to $\mathbb{Q}$ all square roots of rationals, do we get a field (i.e. a set closed under all the basic operations)?

**Answer.** No! For example, the sum $\sqrt{2} + \sqrt{3}$ would have to lie in this set — but is $\sqrt{2} + \sqrt{3}$ equal to $\sqrt{p/q}$ for some rational $p/q$? It is not: squaring gives

$$
(\sqrt{2} + \sqrt{3})^2 = 5 + 2\sqrt{6},
$$

which is irrational (if $5 + 2\sqrt{6}$ were rational, then $\sqrt{6}$ would be rational — but $6$ is not a perfect square, contradicting the proposition above), whereas $(\sqrt{p/q})^2 = p/q$ is rational.

To get a field containing all such numbers, we need a new notion. What is $\sqrt{2}$, structurally? It is a solution of $x^2 - 2 = 0$ — a solution of an algebraic equation with coefficients in $\mathbb{Z}$.

> [!definition] Definition §2.5: Algebraic Number
> A number is called an **algebraic number** if it is a solution of an algebraic equation with coefficients in $\mathbb{Z}$:
>
> $$
> a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 = 0.
> $$
>
> (We may equivalently allow all coefficients in $\mathbb{Q}$: by clearing denominators, we can assume $a_n, \ldots, a_0$ are integers.) The set of all algebraic numbers is denoted $\overline{\mathbb{Q}}$, and it forms a field.

^def-2-5

> [!definition] Definition §2.6: Algebraic Integer
> If moreover $a_n = 1$, the solution $x$ is called an **algebraic integer**.

^def-2-6

> [!example] Example §2.2: $\sqrt{2}$ is an algebraic integer
> $\sqrt{2}$ solves $x^2 - 2 = 0$, a monic equation with integer coefficients. Similarly $\sqrt{2} + \sqrt{3}$ is an algebraic integer: it solves $x^4 - 10x^2 + 1 = 0$ (square $x = \sqrt{2}+\sqrt{3}$ twice: $x^2 = 5 + 2\sqrt{6}$, so $x^2 - 5 = 2\sqrt{6}$, and squaring again gives $x^4 - 10x^2 + 25 = 24$).

^ex-2-2

It looks like we are getting more and more numbers:

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \overline{\mathbb{Q}}.
$$

**Question.** Are there more integers in $\mathbb{Z}$ than natural numbers in $\mathbb{N}$?

The instinctive answer is “of course, yes!” — but this is not so obvious, and in fact *not true*, once we make precise what “more” means.

## Comparing Infinite Sets: Countability

**Question.** What do we mean when we say two sets have the same number of elements?

To compare the sizes of two classes of students, we count. The same works for any finite sets. For infinite sets we cannot count this way (life is short!), so we need another method: instead of counting each set, we *match up* their elements.

> [!theorem] Theorem §2.3: Finite sets
> Two finite sets $A$ and $B$ have the same number of elements if and only if there exists a one-to-one correspondence (a bijective map, i.e. injective and onto)
>
> $$
> f: A \to B.
> $$

^thm-2-3

This matching criterion makes sense even when counting does not, so we turn it into a definition:

> [!definition] Definition §2.7: Same Size
> Two infinite sets $A$ and $B$ are said to have the **same size** if there exists a bijective map $f: A \to B$.

^def-2-7

> [!theorem] Theorem §2.4: $\mathbb{N}$ and $\mathbb{Z}$ have the same size
> There exists a bijection $f: \mathbb{N} \to \mathbb{Z}$.

^thm-2-4

> [!proof]+ Proof
> Make a list of all integers in $\mathbb{Z}$:
>
> $$
> 0,\ 1,\ -1,\ 2,\ -2,\ 3,\ -3,\ \ldots
> $$
>
> Every integer appears in this list exactly once, so sending $n \in \mathbb{N}$ to the $n$-th entry of the list is a bijection. Explicitly,
>
> $$
> f(n) =
> \begin{cases}
> \ n/2 & n \text{ even}, \\
> \ -(n-1)/2 & n \text{ odd},
> \end{cases}
> $$
>
> so $f(1) = 0$, $f(2) = 1$, $f(3) = -1$, $f(4) = 2$, $f(5) = -2$, …

^pf-2-4

> [!definition] Definition §2.8: Countable
> An infinite set $A$ is said to be **countable** if it has the same size as $\mathbb{N}$. This is reasonable terminology, since $\mathbb{N}$ itself arises from counting.

^def-2-8

> [!theorem] Theorem §2.5: $\mathbb{Q}$ is countable
> There exists a bijection $f: \mathbb{Q} \to \mathbb{N}$.

^thm-2-5

> [!proof]+ Proof
> We must make a list of all elements of $\mathbb{Q}$ *without repetition or omission*. This requires a reduction and a strategy.
>
> **Reduction.** We first list only the positive rational numbers. The negative rationals can then be listed similarly, and the two lists are combined with $0$ by interleaving:
>
> $$
> 0,\ r_1,\ -r_1,\ r_2,\ -r_2,\ \ldots
> $$
>
> where $r_1, r_2, \ldots$ is the list of positive rationals.
>
> **Strategy.** Write each positive rational uniquely as $p/q$ with $p, q$ *coprime* positive integers. Use the sum $p + q$ as a measure of the size of $p/q$, and list the fractions in order of increasing $p + q$ (it is reasonable to list smaller ones first). For each given value $n = p + q$, there are at most $n - 1$ pairs to consider, and we list *only the coprime ones*. For example, for $n = 6$ we list only
>
> $$
> (1,5), \quad (5,1) \qquad \text{i.e.} \quad \tfrac{1}{5},\ 5,
> $$
>
> but not $(2,4), (3,3), (4,2)$, since those pairs are not coprime (each of those fractions already appeared earlier in lowest terms). In this way:
>
> - *no omission*: every positive rational $p/q$ in lowest terms appears when we reach $n = p + q$;
>
> - *no repetition*: each positive rational has a unique lowest-terms representative, and we list only those.
>
> Hence we get a bijection from $\mathbb{N}$ onto the positive rationals, and by the reduction above, a bijection $f: \mathbb{Q} \to \mathbb{N}$.

^pf-2-5

> [!theorem] Theorem §2.6: $\overline{\mathbb{Q}}$ is countable
> The set $\overline{\mathbb{Q}}$ of algebraic numbers is countable.

^thm-2-6

This is more difficult; we do not prove it here.

> [!remark] Remark: Idea of the proof
> A polynomial with integer coefficients is determined by finitely many integers, so the polynomials of each fixed degree can be listed, and hence (by a diagonal-type argument, as for $\mathbb{Q}$) *all* such polynomials can be listed. Each polynomial has only finitely many roots. Listing the roots of the first polynomial, then the second, and so on (skipping repetitions) lists all of $\overline{\mathbb{Q}}$.

^rem-2-6

> [!definition] Definition §2.9: Uncountable
> An infinite set $A$ is called **uncountable** if it does *not* have the same size as $\mathbb{N}$. In this case it has more elements than $\mathbb{N}$.

^def-2-9

Later we will see that $\mathbb{R}$ is uncountable.

## Transcendental Numbers

> [!definition] Definition §2.10: Transcendental Number
> A number $x$ is called **transcendental** if it is not an algebraic number.

^def-2-10

> [!example] Example §2.3: $\pi$ and $e$
> $\pi$ and $e$ are transcendental. (Both facts are hard theorems.) It is not easy to name more — after all, how do we write down numbers? If we define them as solutions of algebraic equations, we only ever get algebraic numbers.

^ex-2-3

> [!theorem] Theorem §2.7: Existence of Transcendental Numbers
> There are infinitely many transcendental numbers in $\mathbb{R}$.

^thm-2-7

> [!proof]+ Proof
> Decompose
>
> $$
> \mathbb{R} = \bigl(\mathbb{R} \cap \overline{\mathbb{Q}}\bigr) \cup \bigl(\mathbb{R} \setminus (\mathbb{R} \cap \overline{\mathbb{Q}})\bigr).
> $$
>
> The set $\mathbb{R} \cap \overline{\mathbb{Q}}$ consists of the real algebraic numbers, and $\mathbb{R} \setminus (\mathbb{R} \cap \overline{\mathbb{Q}})$ consists of the real transcendental numbers. Since $\overline{\mathbb{Q}}$ is countable (Theorem 2.5), so is its subset $\mathbb{R} \cap \overline{\mathbb{Q}}$; and $\mathbb{R}$ is uncountable (to be proved later). If $\mathbb{R} \setminus (\mathbb{R} \cap \overline{\mathbb{Q}})$ were countable (or finite), then $\mathbb{R}$ would be a union of two countable sets, hence countable — a contradiction. Therefore $\mathbb{R} \setminus (\mathbb{R} \cap \overline{\mathbb{Q}})$ is uncountable; in particular it is infinite.

^pf-2-7

> [!remark] Remark
> Note what the argument actually shows: the transcendental numbers are not merely infinite but *uncountable* — in the sense of size, almost all real numbers are transcendental, even though it is hard to name any single one. This existence proof (due to Cantor) produces infinitely many transcendental numbers without exhibiting even one.

^rem-2-7
