---
subject: "[[Single Variable Analysis]]"
section: 1
chapter: 1
tags: [real-analysis, math451]
---
↑ [[· 1 Introduction]] · [[§2 The Set ℚ of Rational Numbers]] →

## The Peano Axioms

The natural numbers

$$
\mathbb{N} = \{1, 2, 3, \ldots\}
$$

are the numbers we first learn by counting. They feel so natural that one rarely bothers to ask how they are defined — but defining them rigorously is genuinely complicated. (What is $1$? Once we have $1$, we can define $2$ as its *successor*, and in general every $n \in \mathbb{N}$ has a successor $n+1$.) Rather than construct $\mathbb{N}$ from scratch, we *characterize* it by a list of basic properties.

> [!definition] Definition §1.1: Peano Axioms
> The set $\mathbb{N}$ satisfies the following five properties:
>
> 1. $1$ belongs to $\mathbb{N}$.
>
> 2. If $n \in \mathbb{N}$, then its successor $n+1 \in \mathbb{N}$.
>
> 3. $1$ is not the successor of any element of $\mathbb{N}$.
>
> 4. If $n$ and $m$ in $\mathbb{N}$ have the same successor, then $n = m$.
>
> 5. Let $S \subseteq \mathbb{N}$ be a subset. Suppose $S$ contains $1$, and contains $n+1$ whenever it contains $n$. Then $S = \mathbb{N}$.
>
> These give a characterization of $\mathbb{N}$.

^def-1-1

> [!remark] Remark
> The axioms all seem obvious — but not exactly so. We have not defined “successor,” and we have not defined addition; here we take them for granted. The content of the axioms is that these primitive notions behave the way counting suggests: N1–N2 generate the numbers, N3 says the counting has a starting point, N4 says no two numbers collide, and N5 says nothing else sneaks in.

^rem-1-1

## Mathematical Induction

Axiom N5 is the important one for us: it yields the method of proof by **mathematical induction**.

> [!theorem] Theorem §1.1: Principle of Mathematical Induction
> Let $P_n$ be a property of the natural number $n$. Suppose
>
> 1. $P_1$ is true  (*initial step*)
>
> 2. for every $n \in \mathbb{N}$, if $P_n$ is true, then $P_{n+1}$ is true.  (*induction step*)
>
> Then $P_n$ is true for all $n \in \mathbb{N}$.

^thm-1-1

> [!proof]+ Proof
> Let $S = \{n \in \mathbb{N} : P_n \text{ is true}\}$. By (I1), $1 \in S$. By (I2), whenever $n \in S$ we have $n+1 \in S$. By axiom N5, $S = \mathbb{N}$, i.e. $P_n$ is true for every $n \in \mathbb{N}$.

^pf-1-1

> [!remark] Remark
> When applying induction, it is important to state precisely what $P_n$ is. Many failed induction proofs fail at exactly this point: the statement being carried through the induction is not strong enough (see Example 1.2 below) or the starting point is wrong (see Example 1.3).

^rem-1-2

> [!example] Example §1.1: Sum of squares
> Prove by induction that for all $n \in \mathbb{N}$,
>
> $$
> 1^2 + 2^2 + \cdots + n^2 = \frac{1}{6}\, n(n+1)(2n+1).
> $$
>
> Here $P_n$ is the statement that the displayed equality holds for $n$.
>
> **Initial step.** For $n = 1$: the left side is $1^2 = 1$, and the right side is
>
> $$
> \frac{1}{6}\cdot 1 \cdot (1+1)(2\cdot 1 + 1) = \frac{1}{6}\cdot 2 \cdot 3 = 1.
> $$
>
> So $P_1$ is true.
>
> **Induction step.** Suppose $P_n$ is true. Then
>
> $$
> 1^2 + 2^2 + \cdots + n^2 + (n+1)^2
> = \left(1^2 + \cdots + n^2\right) + (n+1)^2
> = \frac{1}{6}\, n(n+1)(2n+1) + (n+1)^2,
> $$
>
> using $P_n$ in the last equality. We must show this equals
>
> $$
> \frac{1}{6}\,(n+1)(n+2)\bigl(2(n+1)+1\bigr) = \frac{1}{6}\,(n+1)(n+2)(2n+3).
> $$
>
> Dividing both expressions by the common factor $(n+1)$ (and multiplying by $6$), the claim reduces to
>
> $$
> n(2n+1) + 6(n+1) \overset{?}{=} (n+2)(2n+3).
> $$
>
> A direct computation gives
>
> $$
> \begin{align*}
> n(2n+1) + 6(n+1) &= 2n^2 + n + 6n + 6 = 2n^2 + 7n + 6,\\
> (n+2)(2n+3) &= 2n^2 + 3n + 4n + 6 = 2n^2 + 7n + 6.
> \end{align*}
> $$
>
> They are equal, so $P_{n+1}$ holds. By induction, $P_n$ is true for all $n \in \mathbb{N}$.

^ex-1-1

> [!example] Example §1.2: A two-term recursion: strengthening $P_n$
> Define a sequence $(x_n)$ by
>
> $$
> x_1 = 1, \qquad x_2 = 2, \qquad x_n = \tfrac{1}{2}(x_{n-1} + x_{n-2}) \quad \text{for } n \geq 3.
> $$
>
> Prove that $1 \leq x_n \leq 2$ for all $n \in \mathbb{N}$.
>
> **What is $P_n$?** The naive choice — $P_n$: “$1 \leq x_n \leq 2$” — is *not enough*: the recursion computes $x_{n+1}$ from the *two* previous terms, so knowing a bound on $x_n$ alone gives no control over $x_{n+1}$. Instead take the stronger statement
>
> $$
> P_n: \quad \text{for all } k \leq n,\ k \in \mathbb{N}, \quad 1 \leq x_k \leq 2.
> $$
>
> **Initial steps.** $P_1$ and $P_2$ are clear: $x_1 = 1$ and $x_2 = 2$ both lie in $[1,2]$.
>
> **Induction step.** Suppose $P_n$ is true for some $n \geq 2$. Since $n-1 \leq n$ and $n \leq n$, the hypothesis gives
>
> $$
> 1 \leq x_{n-1} \leq 2 \quad \text{and} \quad 1 \leq x_n \leq 2.
> $$
>
> This is the crucial point — $P_n$ controls *both* terms entering the recursion. Then
>
> $$
> x_{n+1} = \tfrac{1}{2}(x_n + x_{n-1}) \leq \tfrac{1}{2}(2 + 2) = 2,
> \qquad
> x_{n+1} = \tfrac{1}{2}(x_n + x_{n-1}) \geq \tfrac{1}{2}(1 + 1) = 1.
> $$
>
> Combined with $1 \leq x_k \leq 2$ for all $k \leq n$, this proves $P_{n+1}$. By induction, $P_n$ holds for all $n$, so $1 \leq x_n \leq 2$ for all $n \in \mathbb{N}$.

^ex-1-2

> [!remark] Remark
> The device in Example 1.2 — proving a statement for *all* $k \leq n$ rather than for $n$ alone — is often called **strong induction** (or complete induction). It is not a new axiom: it is ordinary induction applied to the strengthened property $P_n$.

^rem-1-3

> [!theorem] Theorem §1.2: Well-Ordering Principle
> Every nonempty subset $S \subseteq \mathbb{N}$ has a least element. Consequently, every nonempty set of integers that is bounded below has a least element.
>
> *Source: added to the vault (not in the MATH 451 notes); used throughout MATH 493.*

^thm-1-2

> [!proof]+ Proof
> Suppose $S \subseteq \mathbb{N}$ has no least element; we show $S = \varnothing$. Let $P_n$ be the statement "none of $1, 2, \ldots, n$ belongs to $S$."
>
> **Initial step.** If $1 \in S$, then $1$ would be the least element of $S$, since $1 \leq m$ for every $m \in \mathbb{N}$. So $1 \notin S$, i.e. $P_1$ is true.
>
> **Induction step.** Suppose $P_n$ is true. If $n + 1 \in S$, then every element of $S$ is a natural number different from $1, \ldots, n$, hence $\geq n + 1$; so $n + 1$ would be the least element of $S$. Hence $n + 1 \notin S$, and $P_{n+1}$ is true.
>
> By induction (Theorem 1.1, in the strengthened form of the remark above), $P_n$ holds for every $n$, so no natural number lies in $S$: $S = \varnothing$.
>
> For the second statement, let $T \subseteq \mathbb{Z}$ be nonempty with $t \geq b$ for all $t \in T$, where $b \in \mathbb{Z}$. Then $T' = \{t - b + 1 : t \in T\}$ is a nonempty subset of $\mathbb{N}$; if $m$ is its least element, then $m + b - 1$ is the least element of $T$.

^pf-1-2

> [!example] Example §1.3: Shifting the starting point
> Decide for which integers $n$ the inequality
>
> $$
> 2^n > n^2
> $$
>
> holds, and prove the answer by induction.
>
> **Checking small cases.** The inequality fails for negative integers (the left side is not an integer $> n^2$ there; e.g. $2^{-1} = \tfrac12 < 1$). For small $n \geq 0$:
>
> $$
> \begin{array}{c|c|c|c}
> n & 2^n & n^2 & 2^n > n^2? \\ \hline
> 0 & 1 & 0 & \text{yes} \\
> 1 & 2 & 1 & \text{yes} \\
> 2 & 4 & 4 & \text{no} \\
> 3 & 8 & 9 & \text{no} \\
> 4 & 16 & 16 & \text{no} \\
> 5 & 32 & 25 & \text{yes}
> \end{array}
> $$
>
> So the inequality holds for $n = 0, 1$ and, we guess, for all $n \geq 5$. We prove the latter by induction with starting point $n_0 = 5$.
>
> $P_n$ is the truth of $2^n > n^2$.
>
> **Initial step.** $P_5$: $2^5 = 32 > 25 = 5^2$. True.
>
> **Induction step.** Suppose $P_n$ is true for some $n \geq 5$. Then
>
> $$
> 2^{n+1} = 2 \cdot 2^n > 2n^2,
> $$
>
> so it suffices to show $2n^2 \geq (n+1)^2$ for $n \geq 5$. Indeed,
>
> $$
> 2n^2 - (n+1)^2 = n^2 - 2n - 1 = (n-1)^2 - 2 \geq 4^2 - 2 = 14 > 0
> $$
>
> for $n \geq 5$. Hence $2^{n+1} > (n+1)^2$, i.e. $P_{n+1}$ holds. By induction, $2^n > n^2$ for all integers $n \geq 5$ (and also for $n = 0, 1$ by direct check).

^ex-1-3

> [!remark] Remark
> Induction need not start at $1$. If $P_{n_0}$ is true and $P_n \implies P_{n+1}$ for all $n \geq n_0$, then $P_n$ is true for all $n \geq n_0$. (Apply the usual induction to $Q_m := P_{n_0 + m - 1}$.) The example above also shows why checking small cases first matters: the inequality is true at $n=1$, fails at $n = 2,3,4$, and only becomes true permanently at $n = 5$ — a naive induction from $n=1$ would break at the induction step.

^rem-1-4
