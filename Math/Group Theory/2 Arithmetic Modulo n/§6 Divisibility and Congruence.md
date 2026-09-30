---
type: section
subject: "[[Group Theory]]"
chapter: 2
section: 6
tags: [group-theory, math493]
---
← [[§5 A Zoo of Subgroups]] · ↑ [[2 Arithmetic Modulo n]] · [[§7 The Group ℤ∕nℤ]] →

*Reference: Pinter Ch. 21 (the division algorithm), Ch. 23 (congruences).*

> [!definition] Definition §6.1: Divisibility
> For integers $n, m$, we write $n \mid m$ and say **$n$ divides $m$** (or $m$ is a **multiple** of $n$) if $m = kn$ for some $k \in \mathbb{Z}$. Thus $3 \mid 12$ and $5 \mid -20$, while $4 \nmid 6$. Note that $n \mid m$ is a *statement* (true or false), not a number — not to be confused with the fraction $n/m$ or the absolute value $|x|$ — and the divisor is written on the left.

^def-6-1

> [!theorem] Lemma §6.1: Division Algorithm
> Let $m, n \in \mathbb{Z}$ with $n > 0$. There exist unique integers $q$ (the *quotient*) and $r$ (the *remainder*) with
>
> $$ m = qn + r, \qquad 0 \leq r < n. $$
>
> *Source: cf. Pinter Ch. 10, Thm. 2*

^lem-6-1

> [!proof]+ Proof
> **Existence:** The set $\{m - kn : k \in \mathbb{Z}\} \cap \mathbb{Z}_{\geq 0}$ is nonempty (take $k = -|m|$; then $m - kn = m + |m| n \geq 0$ since $n \geq 1$). By [[§1 The Set ℕ of Natural Numbers#^thm-1-2|well-ordering]] it has a least element $r = m - qn \geq 0$. If $r \geq n$, then $r - n = m - (q+1)n$ is a smaller nonnegative element, contradiction; so $r < n$.
>
> **Uniqueness:** If $m = qn + r = q'n + r'$ with $0 \leq r, r' < n$, then $(q - q')n = r' - r$, and $|r' - r| < n$. The left side is a multiple of $n$ with absolute value less than $n$, hence zero: $q = q'$ and $r = r'$.

^pf-6-1

*Uses:* [[§1 The Set ℕ of Natural Numbers#^thm-1-2|451 §1.2]]

> [!definition] Definition §6.2: Quotient and Remainder; “$a \bmod n$”
> For $n \geq 1$ and $a \in \mathbb{Z}$, write $a = qn + r$ with $0 \leq r < n$ as in the [[§6 Divisibility and Congruence#^lem-6-1|Division Algorithm]]. The integer $q$ is the **quotient** and $r$ the **remainder** of $a$ on division by $n$; the remainder is also called the **remainder of $a$ modulo $n$** and written $a \bmod n$. For example, $14 \bmod 12 = 2$, $\ 8 \bmod 5 = 3$, $\ 25 \bmod 8 = 1$, $\ -7 \bmod 5 = 3$ (since $-7 = (-2)\cdot 5 + 3$). Note that $n \mid a$ if and only if $a \bmod n = 0$.

^def-6-2

> [!definition] Definition §6.3: Congruence Modulo $n$
> For $n \geq 1$ and $a, b \in \mathbb{Z}$, we say $a$ is **congruent to $b$ modulo $n$**, written
>
> $$ a \equiv b \pmod n, $$
>
> if $n \mid a - b$, i.e. $a$ and $b$ differ by a multiple of $n$. The integer $n$ is called the **modulus**. For example, $14 \equiv 2 \pmod{12}$, $\ 6 \equiv 1 \pmod 5$, $\ 9 \equiv 1 \pmod 8$, $\ -1 \equiv 4 \pmod 5$.

^def-6-3

> [!theorem] Proposition §6.2: Congruence Is an Equivalence Relation with Remainder Classes
> Fix $n \geq 1$.
> 1. $a \equiv b \pmod n$ if and only if $a \bmod n = b \bmod n$.
> 2. Congruence modulo $n$ is an equivalence relation on $\mathbb{Z}$: it is reflexive, symmetric, and transitive.

^prop-6-2

> [!proof]+ Proof
> **(1)** Write $a = qn + r$ and $b = q'n + r'$ with $0 \leq r, r' < n$. Then $a - b = (q - q')n + (r - r')$. If $r = r'$, then $a - b = (q - q')n$ is a multiple of $n$. Conversely, if $n \mid a - b$, then $n \mid (a - b) - (q - q')n = r - r'$; since $|r - r'| < n$, this forces $r - r' = 0$.
>
> **(2)** Reflexive: $n \mid a - a = 0$. Symmetric: if $a - b = kn$, then $b - a = (-k)n$. Transitive: if $a - b = kn$ and $b - c = ln$, then $a - c = (k + l)n$. (Alternatively, all three follow at once from (1), since “having the same remainder” is visibly an equivalence relation.)

^pf-6-2

*Uses:* [[§6 Divisibility and Congruence#^lem-6-1|§6.1]], [[§6 Divisibility and Congruence#^def-6-1|Def. §6.1]], [[§6 Divisibility and Congruence#^def-6-2|Def. §6.2]], [[§6 Divisibility and Congruence#^def-6-3|Def. §6.3]]

> [!remark]- Connections
> - The general notion: [[§22 Equivalence Relations and Partitions#^def-22-1|Equivalence Relation]].
> - Congruence modulo $n$ is congruence modulo the subgroup $n\mathbb{Z}$: [[§26 Left and Right Cosets#^def-26-1|Congruence Modulo a Subgroup]].

> [!definition] Definition §6.4: Residue Classes
> Fix $n \geq 1$. The **residue class** (or **congruence class**) of $a \in \mathbb{Z}$ modulo $n$ is its equivalence class
>
> $$ [a] = a + n\mathbb{Z} = \{a + kn : k \in \mathbb{Z}\} = \{ b \in \mathbb{Z} : b \equiv a \pmod n \}. $$
>
> Any element of $[a]$ is called a **representative** of the class. By [[§6 Divisibility and Congruence#^prop-6-2|Congruence Is an Equivalence Relation with Remainder Classes]], $[a] = [b]$ iff $a \equiv b \pmod n$, and there are exactly $n$ distinct classes, $[0], [1], \ldots, [n-1]$, one for each possible remainder. For example, modulo $5$: $[3] = \{\ldots, -7, -2, 3, 8, 13, \ldots\}$, and $[8] = [3] = [-2]$.

^def-6-4

> [!remark]- Connections
> - The classes $a + n\mathbb{Z}$ are the cosets of $n\mathbb{Z}$ in $\mathbb{Z}$: [[§26 Left and Right Cosets#^def-26-2|Left and Right Cosets]], [[§22 Equivalence Relations and Partitions#^def-22-2|Equivalence Class]].
> - 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^ex-21-7|590 Ex. §21.7]].

> [!remark] Remark: The Clock Picture
> On a $12$-hour clock, $9$ o'clock plus $5$ hours is $2$ o'clock: compute $9 + 5 = 14$, then reduce, $14 \bmod 12 = 2$. Arithmetic modulo $n$ is exactly this “wrap-around” arithmetic: the infinite line $\mathbb{Z}$ is rolled up into a circle with $n$ points, and integers that land on the same point are identified. The residue classes are the points of the circle.

^rem-6-1

![[m493-6-1.svg]]
*The line $\mathbb{Z}$ rolled up, $12$ integers per turn (shown for $0, \ldots, 35$). Integers congruent modulo $12$ line up on one ray, so each ray is a residue class, e.g. $[2] = \{2, 14, 26, \ldots\}$ (red), and the $12$ rays are the points of the clock. Walking $5$ steps from $9$ (blue) lands on $14$, on the ray of $2$: $9 + 5 \equiv 2 \pmod{12}$.*
