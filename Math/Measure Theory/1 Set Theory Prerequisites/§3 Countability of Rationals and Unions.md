---
type: section
subject: "[[Measure Theory]]"
chapter: 1
section: 3
tags: [measure-theory, math551]
---
← [[§2 The Cantor–Bernstein Theorem]] · ↑ [[· 1 Set Theory Prerequisites]] · [[§4 Uncountability]] →

> [!example] Example §3.1: $\mathbb{Q}$ is countable
> The set of rational numbers $\mathbb{Q}$ is countable.

^ex-3-1

> [!remark]- Connections
> - MATH 451 proof by listing lowest-terms fractions along diagonals: [[§2 The Set ℚ of Rational Numbers#^thm-2-5|ℚ is countable (451 §2.5)]].

> [!theorem] Proposition §3.1: Countable Union of Countable Sets
> The countable union of countable sets is countable.

^prop-3-1

> [!proof]+ Proof
> Let $A_n$ be countable sets for $n = 1, 2, 3, \ldots$. We want to show $\bigcup_n A_n$ is countable.
>
> Since each $A_n$ is countable, we can write $A_n = \{a_{n,1}, a_{n,2}, a_{n,3}, \ldots\}$.
>
> Then $\bigcup_n A_n$ is equivalent to a subset of $\mathbb{N} \times \mathbb{N}$ via the mapping that sends $a \in \bigcup_n A_n$ to $(n, m)$, where $n$ is the least index with $a \in A_n$ and $m$ is the least index with $a = a_{n,m}$. This is well defined even if the $A_n$ overlap or the lists repeat, and it is injective, since $a = a_{n,m}$ is recovered from $(n,m)$.
>
> Since $\mathbb{N} \times \mathbb{N} \sim \mathbb{N}$ ([[§1 Countability and Set Theory#^ex-1-3|Example §1.3]]), we have $\bigcup_n A_n$ equivalent to a subset of $\mathbb{N}$, hence countable.

^pf-3-1

*Uses:* [[§1 Countability and Set Theory#^def-1-1|Def. §1.1]], [[§1 Countability and Set Theory#^ex-1-3|Ex. §1.3]], [[§1 Countability and Set Theory#^thm-1-1|§1.1]], [[§1 Countability and Set Theory#^def-1-8|Def. §1.8]]

> [!remark]- Connections
> - The “product + union closure” step of [[Measure Theory Problem-Solving Techniques#^rem-19-5|Technique 1: Reduction to Known Countability Results]].
> - Used to count the dyadic cubes in [[§7 Structure of Open Sets#^prop-7-3|Proposition §7.3]].
> - Elementary version: [[§14 Counting Infinite Sets#^ex-14-4|250 Ex. §14.4]] (pairwise disjoint denumerable sets, then the general case).

> [!theorem] Corollary §3.2: $\mathbb{Q}$ is countable
> Since $\mathbb{Q}_+ = \bigcup_{n=1}^\infty \{\frac{m}{n} : m \in \mathbb{N}\}$ is a [[§3 Countability of Rationals and Unions#^prop-3-1|countable union of countable sets]], $\mathbb{Q}_+$ is countable. Similarly $\mathbb{Q}_- \cup \{0\}$ is countable, so $\mathbb{Q} = \mathbb{Q}_- \cup \{0\} \cup \mathbb{Q}_+$ is countable.
>
> Alternatively: Define $f: \mathbb{N} \times \mathbb{N} \to \mathbb{Q}_+$ by $f(n,m) = \frac{n}{m}$. This is surjective, so $\mathbb{Q}_+$ is countable: choosing one preimage under $f$ for each $q \in \mathbb{Q}_+$ gives an injection $\mathbb{Q}_+ \to \mathbb{N} \times \mathbb{N} \sim \mathbb{N}$.

^cor-3-2

*Uses:* [[§3 Countability of Rationals and Unions#^prop-3-1|§3.1]], [[§1 Countability and Set Theory#^ex-1-3|Ex. §1.3]]

![[m551-3-1.svg]]
*The first proof in a picture: row $n$ is $A_n = \{\tfrac mn : m \in \mathbb{N}\}$, and $\mathbb{Q}_+ = \bigcup_n A_n$. Walking the diagonals (red) as in Example §1.3 reaches every entry, so every positive rational gets listed; grey entries such as $\tfrac22 = \tfrac11$ are repeats and are simply skipped. Allowing repeats is exactly why a *surjection* $\mathbb{N} \times \mathbb{N} \to \mathbb{Q}_+$ is enough.*

> [!remark]- Connections
> - Elementary version: [[§14 Counting Infinite Sets#^thm-14-10|250 Thm. §14.10]] (Cantor, 1874).
