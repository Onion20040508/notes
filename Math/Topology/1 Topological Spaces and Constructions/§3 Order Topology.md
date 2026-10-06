---
type: section
subject: "[[Topology]]"
chapter: 1
section: 3
munkres: "§3, §16"
tags: [topology, math590]
---
← [[§2 Basis for a Topology]] · ↑ [[· 1 Topological Spaces and Constructions]] · [[§4 Product Topology]] →

## Order Relations and Intervals

> [!definition] Definition §3.1: Order Relation
> A relation $<$ on a set $A$ is called an **order relation** (or **simple order**, **linear order**) if:
> 1. If $x \neq y$, then either $x < y$ or $y < x$.
> 2. For no $x \in A$, does $x < x$.
> 3. If $x < y$ and $y < z$, then $x < z$.

^def-3-1

> [!remark]- Connections
> - The same notion with ≤ (ordered set), together with partial orders: [[§3 The Set ℝ of Real Numbers#^def-3-3|451 Def. §3.3]] and [[§3 The Set ℝ of Real Numbers#^def-3-4|451 Def. §3.4]].

> [!example] Example §3.1
> $\mathbb{R}$ with the usual order relation. Another example: $\mathbb{R}$ with $<_{sq}$ defined by $x <_{sq} y$ if $x^2 < y^2$, or $x^2 = y^2$ and $x < y$.

^ex-3-1

> [!definition] Definition §3.2: Interval Notation
> If $X$ is a set with a $<$ relation, then:
>
> $$
> \begin{aligned}
> (a,b) &= \{x \mid a < x < b\} \\
> [a,b) &= \{x \mid a \leq x < b\} \\
> [a,b] &= \{x \mid a \leq x \leq b\} \\
> (a, \infty) &= \{x \mid x > a\} \\
> (-\infty, a) &= \{x \mid x < a\}
> \end{aligned}
> $$

^def-3-2

## Dictionary Order

> [!definition] Definition §3.3: Dictionary Order
> The **dictionary order** (or **lexicographic order**) $<$ on $A \times B$, where $(A, <_A)$ and $(B, <_B)$ are ordered sets, is defined by:
>
> $$
> a_1 \times b_1 < a_2 \times b_2 \quad \text{if} \quad a_1 <_A a_2 \quad \text{or} \quad (a_1 = a_2 \text{ and } b_1 <_B b_2)
> $$

^def-3-3

> [!remark] Remark
> This can easily extend to countable products of simply ordered sets.

^rem-3-1

> [!example] Example §3.2
> $A = \{a, b, \ldots, x, y, z\} \Rightarrow A \times A \times A$ gives “car” $<$ “cat” $<$ “dog”.

^ex-3-2

> [!example] Example §3.3: Dictionary Order on $\mathbb{R} \times \mathbb{R}$
> With the dictionary order on $\mathbb{R} \times \mathbb{R}$: $1 \times 2 \in \mathbb{R} \times \mathbb{R}$, and
>
> $$
> (1 \times 2, \infty) = \left\{x \times y \in \mathbb{R} \times \mathbb{R} \;\middle|\; \begin{array}{c} x = 1, y > 2 \\ \text{or } x > 1 \end{array}\right\}
> $$

^ex-3-3

> [!example] Example §3.4: Visualizing Dictionary Order Intervals
> In the dictionary order on $\mathbb{R} \times \mathbb{R}$, we move “up” along vertical lines first, then jump to the next vertical line. Here are some key interval types:
>
> **1. Open interval $(a \times b, c \times d)$ where $a < c$:**
>
> ![[m590-3-1.svg]]
> *The interval $(a \times b, c \times d)$, $a < c$ (blue): the part of the line $x = a$ above $b$, every full vertical line strictly between $a$ and $c$ (hatched strip), and the part of the line $x = c$ below $d$. The endpoints (hollow) and the dashed half-lines are not in the interval.*
>
> **2. Open interval $(a \times b, a \times d)$ on the same vertical line ($b < d$):**
>
> ![[m590-3-2.svg]]
> *The interval $(a \times b, a \times d)$: an open vertical segment on the line $x = a$ (blue, hollow endpoints). The rest of that line (dashed) is not in the interval.*
>
> **3. Ray $(a \times b, \infty)$:**
>
> ![[m590-3-3.svg]]
> *The ray $(a \times b, \infty)$: the part of the line $x = a$ above $b$ (hollow endpoint excluded), together with every full vertical line to its right (hatched, continuing forever to the right).*
>
> **4. Ray $(-\infty, c \times d)$:**
>
> ![[m590-3-4.svg]]
> *The ray $(-\infty, c \times d)$: every full vertical line to the left of $c$ (hatched, continuing forever to the left), together with the part of the line $x = c$ below $d$ (hollow endpoint excluded).*
>
> **Key insight:** Unlike the standard topology on $\mathbb{R}^2$ (where open sets are “blobs”), every open set in the dictionary order topology is a union of open vertical segments $\{a\} \times (b, d)$: each interval above is such a union. Horizontally the topology is discrete: the segment $\{a\} \times (b-1, b+1) = (a \times (b-1),\ a \times (b+1))$ is an open set containing $a \times b$ that meets no other vertical line. In fact it is the product topology $\mathbb{R}_{\text{discrete}} \times \mathbb{R}_{\text{std}}$ ([[§4 Product Topology#^ex-4-3|Example §4.3]]), which is strictly finer than the standard topology on $\mathbb{R}^2$.

^ex-3-4

> [!remark]- Connections
> - The dictionary order topology on $\mathbb{R} \times \mathbb{R}$ as a product: [[§4 Product Topology#^ex-4-3|Example §4.3 (HW2)]]; contrast with the [[§4 Product Topology#^ex-4-1|Standard Topology on ℝ²]].

## The Order Topology

> [!definition] Definition §3.4: Order Topology
> Let $X$ be a set with a simple order relation. Assume $X$ has more than one element. Let $\mathcal{B}$ be the basis consisting of:
> - Open intervals $(a, b)$, for $a, b \in X$
> - Intervals $[a_0, b)$, where $a_0$ is the smallest (if any) in $X$
> - Intervals $(a, b_0]$, where $b_0$ is the largest (if any) in $X$
>
> The [[§2 Basis for a Topology#^def-2-2|topology generated]] by $\mathcal{B}$ is the **order topology** on $X$.

^def-3-4

> [!remark]- Connections
> - Connectedness of linear continua in the order topology: [[§16 Connected Subspaces of ℝ#^thm-16-1|Linear Continuum is Connected]].
> - Order topology vs. subspace topology: [[§5 Subspace Topology#^ex-5-3|Subspace ≠ Order Topology: I × I]].

> [!example] Example §3.5
> The standard topology on $\mathbb{R}$ ([[§1 Topological Spaces#^ex-1-5|Ex. §1.5]]) is the same as the order topology on $\mathbb{R}$.

^ex-3-5

> [!example] Example §3.6: Order Topology on $\mathbb{Z}_+$
> What is the order topology on $\mathbb{Z}_+ = \{1, 2, 3, \ldots\}$?
>
> The basis $\mathcal{B} = \{(n, m), [1, n)\}$. The basis includes all one-point sets $\{n\}$:
> - $\{1\} = [1, 2)$
> - $\{n\} = (n-1, n+1)$ for $n \geq 2$
>
> Can form all subsets of $\mathbb{Z}_+$ by arbitrary unions of $\{n\}$'s. $\Rightarrow$ Same as [[§1 Topological Spaces#^ex-1-3|discrete topology]].

^ex-3-6

> [!remark]- Connections
> - The general principle: [[§2 Basis for a Topology#^rem-2-2|Characterization of Discrete Topology]].

> [!example] Example §3.7: Order Topology on a Product Set
> The set $X = \{1, 2\} \times \mathbb{Z}_+$ with order topology given by [[§3 Order Topology#^def-3-3|dictionary order]].
>
> **Q:** Is there a smallest element in $X$? Largest? Same as discrete?
>
> **A:**
> 1. Yes, $1 \times 1$ is the smallest.
> 2. No. Assume $a \times b >$ all other elements, so $a = 2$, but there's no largest element in $\mathbb{Z}_+$, so no.
> 3. $\{1 \times 1\} = [1 \times 1, 1 \times 2)$. Is $\{2 \times 1\}$ open in the order topology?
>
> Any open set containing $2 \times 1$ must contain a basis element $2 \times 1 \in (i \times a, j \times b)$ for some basis element with $i, j \in \{1, 2\}$.
>
> If $a, b \in \mathbb{Z}_+$: $2 \times 1 \in (1 \times a, 2 \times b) \Rightarrow$ any basis element containing $2 \times 1$ must contain more than one point.
>
> So $\neq$ discrete topology.

^ex-3-7

![[m590-3-5.svg]]
*$X = \{1,2\}\times\mathbb{Z}_+$ in the dictionary order: all of the column $\{1\}\times\mathbb{Z}_+$ comes before $2\times 1$. A basis element $(1\times a,\ 2\times b)$ containing $2\times 1$ (red; the hollow endpoints are excluded) contains the whole tail $1\times(a+1),\ 1\times(a+2), \ldots$ of the first column, so $\{2\times 1\}$ is not open and the topology is not discrete. (Drawn with $a=2$, $b=3$.)*
