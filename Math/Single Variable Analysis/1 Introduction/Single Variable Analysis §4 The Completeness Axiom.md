---
subject: "[[Single Variable Analysis]]"
section: 4
chapter: 1
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §3 The Set ℝ of Real Numbers]] · ↑ [[Single Variable Analysis — 1 Introduction]] · [[Single Variable Analysis §5 The Symbols +∞, −∞]] →

We have studied properties of $\mathbb{Z}$, $\mathbb{Q}$, and $\mathbb{R}$, emphasizing their similarities: for example, $\mathbb{Q}$ and $\mathbb{R}$ are both ordered fields, with the resulting notion of absolute value as a way to measure the size of a number. Of course they are not the same: $\mathbb{Q}$ is countable while $\mathbb{R}$ is not.

**Question.** What is the *really* important difference between $\mathbb{Q}$ and $\mathbb{R}$?

The answer is the **completeness** of $\mathbb{R}$. As mentioned before, this is crucial for analysis, since it is the basis of taking limits and hence of continuity. Two things are wanted: the *existence* of limits, and the property that limits of sequences of real numbers are again real numbers — a closedness property: we do not leave the real numbers when taking limits.

## Maximum, Minimum, and Bounds

> [!definition] Definition §4.1: Maximum and Minimum
> Let $S \subseteq \mathbb{R}$ be a nonempty subset. If $S$ contains a largest element $x_0$ — i.e. $x_0 \in S$ and $x \leq x_0$ for every $x \in S$ — then $x_0$ is called the **maximum** of $S$, written $x_0 = \max S$. Similarly one defines the **minimum** of $S$, denoted $\min S$.

^def-4-1

> [!theorem] Proposition §4.1: Uniqueness of the Maximum
> If $\max S$ exists, it is unique; similarly for $\min S$.

^prop-4-1

> [!proof]+ Proof
> Suppose $x_0$ and $x_0'$ are both maxima of $S$. Since $x_0' \in S$ and $x_0$ is a maximum, $x_0' \leq x_0$. Symmetrically, $x_0 \leq x_0'$. By antisymmetry (O2), $x_0 = x_0'$. The same argument works for minima.

^pf-4-1

> [!remark] Remark
> In mathematics, two things are always important about an object: **existence** and **uniqueness**. Uniqueness of $\max S$ is settled above; existence is a genuine issue, to which we return below.

^rem-4-1

> [!example] Example §4.1: Finite sets
> Every finite nonempty set $S \subset \mathbb{R}$ has both $\max S$ and $\min S$: we can make a finite list of its elements and order them. Two properties are being used here — that the list is *finite* (so the sorting terminates), and that any two elements can be *compared* (totality O1).

^ex-4-1

> [!example] Example §4.2: Sets without max or min
> $\mathbb{Z}$ has neither maximum nor minimum; $\mathbb{N}$ has no maximum. The non-closed finite intervals $(a,b)$, $(a,b]$, $[a,b)$ each fail to contain at least one endpoint: e.g. $(a,b)$ has neither $\max$ nor $\min$. The closed interval $[a,b]$, however, has both.

^ex-4-2

There is a big difference between $\mathbb{Z}$ and $(0,1)$ as examples: the interval fails to have a maximum while being “trapped” below some number. This is captured by the following definition.

> [!definition] Definition §4.2: Bounded Sets
> A subset $S \subseteq \mathbb{R}$ is **bounded from above** if there exists a number $M$ such that $x \leq M$ for all $x \in S$; any such $M$ is called an **upper bound** of $S$. Similarly one defines **bounded from below** and **lower bounds**. $S$ is called **bounded** if it has both an upper bound and a lower bound.

^def-4-2

> [!remark] Remark
> The difference between an upper bound and $\max S$: an upper bound $M$ does *not* have to be contained in $S$. Note also that the definition uses the order $\leq$ of $\mathbb{R}$ in an essential way. For subsets of $\mathbb{C}$ there is no order (§3), so upper and lower bounds cannot be defined — but boundedness still can: $S \subseteq \mathbb{C}$ is bounded if there exists $M$ with $|z| \leq M$ for all $z \in S$, using the modulus in place of the order.

^rem-4-2

## Supremum and Infimum

> [!theorem] Proposition §4.2: Max Is an Upper Bound
> If $S$ has a maximum $x_0 = \max S$, then $x_0$ is an upper bound of $S$. Similarly, $\min S$ is a lower bound if it exists. The converse is not true.

^prop-4-2

> [!proof]+ Proof
> That $x_0$ is an upper bound is part of the definition of maximum. For the failure of the converse: $S = (0,1)$ is bounded — $1$ is an upper bound — but $S$ has no maximum, and $1 \notin S$.

^pf-4-2

What is special about the upper bound $1$ of $(0,1)$? Any number $t \geq 1$ is an upper bound of $(0,1)$, and conversely any upper bound $t$ satisfies $t \geq 1$. So $1$ is the *least* upper bound of $(0,1)$.

> [!definition] Definition §4.3: Supremum and Infimum
> The **least upper bound** $M$ of $S$ is an upper bound of $S$ that is less than or equal to any other upper bound. If $S \subseteq \mathbb{R}$ is bounded from above and has a least upper bound $M$, then $M$ is called the **supremum** of $S$, denoted $\sup S$. If $S$ is bounded from below and has a largest lower bound $m$, then $m$ is called the **infimum** of $S$, denoted $\inf S$.

^def-4-3

> [!remark] Remark
> If $\sup S$ or $\inf S$ exists, it is unique — by the same antisymmetry argument as for $\max S$: two least upper bounds are each $\leq$ the other.

^rem-4-3

> [!theorem] Proposition §4.3: Characterization of the Supremum
> Let $S \subseteq \mathbb{R}$ be nonempty. Then $M = \sup S$ if and only if
>
> 1. for any $x \in S$: $x \leq M$;  (*$M$ is an upper bound*)
>
> 2. for any $M_1 < M$, there exists $x_1 \in S$ such that $x_1 > M_1$.  (*nothing smaller is*)
>
> There is a similar characterization of $\inf S$: $m = \inf S$ if and only if $m$ is a lower bound and for any $m_1 > m$ there exists $x_1 \in S$ with $x_1 < m_1$.

^prop-4-3

![[m451-4-1.svg]]
*Proposition 4.3 on the line: $M = \sup S$ is an upper bound (1), and the upper bounds of $S$ are exactly the numbers $\geq M$ (gray); any $M_1 < M$ is beaten by some $x_1 \in S$ (red) (2). Here $M \notin S$ (hollow), so $S$ has a supremum but no maximum.*

> [!proof]+ Proof
> Condition (2) says precisely that no $M_1 < M$ is an upper bound of $S$. So (1) and (2) together say: $M$ is an upper bound, and every upper bound $t$ satisfies $t \geq M$ (for if $t < M$, then by (2) $t$ is not an upper bound). This is exactly the definition of least upper bound.

^pf-4-3

> [!example] Example §4.3: Verifying a supremum
> We verify the two conditions for $S = (1,2)$ and $M = 2$. (1) Every $x \in (1,2)$ satisfies $x < 2$. (2) Let $M_1 < 2$. Set
>
> $$
> x_1 = \frac{\max\{M_1, 1\} + 2}{2}.
> $$
>
> Then $x_1$ is the midpoint of the interval $(\max\{M_1,1\},\, 2)$, so $1 \leq \max\{M_1,1\} < x_1 < 2$, giving $x_1 \in S$; and $x_1 > \max\{M_1,1\} \geq M_1$. Hence $\sup(1,2) = 2$. Similarly $\sup(0,1) = 1$, and for $S = (-1,1)$: $\sup S = 1$, $\inf S = -1$.

^ex-4-3

## The Completeness Axiom

Finally, we come to the property that distinguishes $\mathbb{R}$.

> [!definition] Definition §4.4: The Completeness Axiom
> Every nonempty subset $S \subseteq \mathbb{R}$ that is bounded from above has a least upper bound: $\sup S$ exists.

^def-4-4

This is not obvious at all. It is the axiom we will assume for the rest of the semester, and use to prove other properties. Similarly, completeness can be formulated in terms of $\inf$: every nonempty subset bounded from below has a greatest lower bound. The two formulations are equivalent — each implies the other. Following the book, we assume the $\sup$ version and obtain the $\inf$ version as a corollary.

> [!theorem] Corollary §4.4: Completeness for Infima
> If a nonempty $S \subseteq \mathbb{R}$ is bounded from below, then $\inf S$ exists.

^cor-4-4

> [!proof]+ Proof
> The idea: consider the negative set $-S = \{-x \mid x \in S\}$ and apply the [[Completeness Axiom|completeness axiom]] to $-S$. If $m$ is a lower bound of $S$, then for $x \in S$ we have $x \geq m$, hence $-x \leq -m$; so $-S$ is nonempty and bounded above (by $-m$), and $M = \sup(-S)$ exists.
>
> **Claim:** $-M = \inf S$. We check the two conditions.
>
> (1) *$-M$ is a lower bound of $S$.* For any $x \in S$, $-x \in -S$, so $-x \leq M$, hence $x \geq -M$.
>
> (2) *$-M$ is the greatest lower bound.* Let $m$ be any lower bound of $S$. As computed above, $-m$ is then an upper bound of $-S$. Since $M$ is the *least* upper bound of $-S$, we get $M \leq -m$, which gives $m \leq -M$.
>
> Hence $-M$ is a lower bound that dominates every lower bound: $\inf S = -M = -\sup(-S)$.

^pf-4-4

The important point is that this completeness property does *not* hold in $\mathbb{Q}$: there exist bounded subsets of $\mathbb{Q}$ that have no supremum or infimum *in $\mathbb{Q}$*. (Of course, viewing $\mathbb{Q} \subset \mathbb{R}$, their $\sup$ and $\inf$ exist in $\mathbb{R}$.)

> [!example] Example §4.4: Incompleteness of $\mathbb{Q}$
> Consider the set of rational numbers in the interval $(-\sqrt{2}, \sqrt{2})$:
>
> $$
> S = \{a \in \mathbb{Q} \mid -\sqrt{2} < a < \sqrt{2}\} \subset \mathbb{Q}.
> $$
>
> As a subset of $\mathbb{R}$, its supremum is $\sqrt{2}$ and its infimum is $-\sqrt{2}$ (using the density of $\mathbb{Q}$, proved below, to verify condition (2) of the characterization). But we proved in §2 that $\sqrt{2} \notin \mathbb{Q}$, so $S$ has no least upper bound *within* $\mathbb{Q}$. This example exhibits the incompleteness of $\mathbb{Q}$.

^ex-4-4

## The Archimedean Property and the Density of $\mathbb{Q}$

As an application of completeness, we prove an “obvious” property: $\mathbb{Q}$ is **dense** in $\mathbb{R}$ — the rational points are dense in the real line. More precisely: given any two real numbers $a < b$, there exists a rational number $r$ with $a < r < b$. Equivalently, there is no open interval that avoids the rational points. (Later, when studying topology, open intervals correspond to open neighborhoods: every neighborhood in $\mathbb{R}$ contains rational points — that is why we say $\mathbb{Q}$ is dense *everywhere* in $\mathbb{R}$.)

> [!remark] Remark: Convincing ourselves first
> To prove something rigorously, we should first be convinced it is true — and the convincing may suggest the proof. Represent $\mathbb{R}$ by the real line and mark rational points in stages. **Stage 0:** mark all integer points $\mathbb{Z}$; removing them leaves intervals of length $1$. **Stage 1:** between every pair $n, n+1$, mark the midpoint $n + \tfrac{1}{2}$ — clearly rational; removing all marked points leaves intervals of length $\tfrac{1}{2}$. **Stage $n$** (inductively): mark the midpoints of the current intervals; the remaining intervals have length $1/2^n$. Now, given an open interval $(a,b)$, choose $n$ with $1/2^n < b - a$: if $(a,b)$ avoided all points marked up to stage $n$, it would sit inside one of the leftover intervals of length $1/2^n$ — shorter than $b - a$, impossible. So $(a,b)$ contains a marked point, which is rational.
>
> **Is this a rigorous proof?** Reasonable, but not rigorous enough at one specific step: the claim that the real line is covered by the intervals $[n, n+1]$, $n \in \mathbb{Z}$ — equivalently, that every $x \in \mathbb{R}$ satisfies $n > x$ for some integer $n$. “Obvious,” one says: write $x$ in decimal form and take $[x] + 1$. But the decimal expression of $x$ is *not* among the properties of $\mathbb{R}$ we have so far! (It will in fact be a consequence of completeness.) What is needed is exactly the [[Archimedean Property|Archimedean Property]] below.

^rem-4-4

> [!theorem] Theorem §4.5: Archimedean Property
> For any two positive real numbers $a > 0$, $b > 0$, there exists $n \in \mathbb{N}$ such that
>
> $$
> na > b.
> $$
>
> Equivalently (taking $a' = 1$, $b' = b/a$): for every $x \in \mathbb{R}$ there exists $n \in \mathbb{N}$ with $n > x$.

^thm-4-5

> [!proof]+ Proof
> This follows from the completeness axiom, by contradiction. Suppose the property fails: there exists a pair $a, b > 0$ such that $na \leq b$ for all $n \in \mathbb{N}$. Then the set
>
> $$
> S = \{na \mid n \in \mathbb{N}\}
> $$
>
> is nonempty and bounded from above by $b$. By the completeness axiom, $s_0 = \sup S$ exists.
>
> Since $a > 0$, we have $s_0 - a < s_0$, so $s_0 - a$ is *not* an upper bound of $S$ (it is smaller than the least upper bound). By the [[Characterization of the Supremum|characterization of the supremum]], there exists $n_0 \in \mathbb{N}$ such that
>
> $$
> n_0 a > s_0 - a, \qquad \text{i.e.} \qquad (n_0 + 1)a > s_0.
> $$
>
> Since $n_0 + 1 \in \mathbb{N}$, the element $(n_0+1)a$ belongs to $S$ and exceeds $s_0$ — so $s_0$ is not an upper bound of $S$. This contradicts $s_0 = \sup S$. (Where does the contradiction come from? From the assumption that $S$ is bounded above, i.e. that the Archimedean property fails.)

^pf-4-5

![[m451-4-2.svg]]
*The contradiction in the proof: the multiples $a, 2a, 3a, \ldots$ are spaced exactly $a$ apart, so the window $(s_0 - a,\, s_0]$ of length $a$ must catch some $n_0 a$ (as $s_0 - a$ is not an upper bound) — and then the next multiple $(n_0+1)a$ (red), which also belongs to $S$, lands beyond $s_0$.*

> [!theorem] Proposition §4.6: Two-Sided Archimedean Bounds (HW)
> If $a > 0$, then there exists $n \in \mathbb{N}$ such that
>
> $$
> \frac1n < a < n.
> $$

^prop-4-6

> [!proof]+ Proof
> By trichotomy, exactly one of $a \geq 1$ or $0 < a < 1$ holds.
>
> *Case $a \geq 1$.* By the Archimedean property, choose $n \in \mathbb{N}$ with $n > a$. Since $n > a \geq 1$ and $n$ is an integer, $n \geq 2$, so
>
> $$
> \frac1n < 1 \leq a < n.
> $$
>
> *Case $0 < a < 1$.* Then $\tfrac1a > 1$; choose $n \in \mathbb{N}$ with $n > \tfrac1a$. Then $a < 1 < n$; and multiplying $n > \tfrac1a$ by $a > 0$ gives $na > 1$, hence $\tfrac1n < a$ (order properties of §3). So $\tfrac1n < a < n$ in either case.

^pf-4-6

> [!theorem] Theorem §4.7: Density of $\mathbb{Q}$ in $\mathbb{R}$
> For any $a, b \in \mathbb{R}$ with $a < b$, there exists $r \in \mathbb{Q}$ such that $a < r < b$.

^thm-4-7

> [!proof]+ Proof
> Since $b - a > 0$, the Archimedean property (with the pair $b-a$ and $1$) gives $n \in \mathbb{N}$ such that
>
> $$
> n(b - a) > 1.
> $$
>
> Next we find an integer just above $na$. The set $J = \{j \in \mathbb{Z} \mid j > na\}$ is nonempty (by the Archimedean property, some natural number exceeds $na$) and bounded below (by the Archimedean property applied to $-na$, some natural number $k$ satisfies $k > -na$, so every $j \in J$ satisfies $j > na > -k$). A nonempty set of integers bounded below has a least element; let $m = \min J$. Then
>
> $$
> m > na \qquad \text{and} \qquad m - 1 \leq na,
> $$
>
> the latter since $m - 1 \notin J$. Combining,
>
> $$
> na < m \leq na + 1 < na + n(b-a) = nb,
> $$
>
> using $n(b-a) > 1$ in the strict inequality. Dividing by $n > 0$ (property (f)–(g) of §3 guarantees this preserves the inequalities):
>
> $$
> a < \frac{m}{n} < b,
> $$
>
> and $r = m/n \in \mathbb{Q}$ is the required rational number.

^pf-4-7

![[m451-4-3.svg]]
*The proof of density, scaled up by $n$: the interval $(na, nb)$ has length $n(b-a) > 1$, so the first integer $m > na$ (red) satisfies $m \leq na + 1 < nb$. Dividing by $n$ carries the picture back and puts the rational $\tfrac{m}{n}$ inside $(a,b)$.*

> [!remark] Remark
> The lecture emphasized: try to prove density yourself before reading the book, and after reading, try to come up with new proofs. The proof above is the standard one; the dyadic-midpoint picture in the earlier remark, once the Archimedean property justifies its covering step, gives an alternative proof.

^rem-4-5
