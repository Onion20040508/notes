---
subject: "[[Single Variable Analysis]]"
section: 3
chapter: 1
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §2 The Set ℚ of Rational Numbers]] · ↑ [[Single Variable Analysis — 1 Introduction]] · [[Single Variable Analysis §4 The Completeness Axiom]] →

## Field Axioms

Recall that $\mathbb{Q}$ is a field: it carries the two operations of addition and multiplication, satisfying the following compatibility properties.

> [!definition] Definition §3.1: Field Axioms
> A **field** is a set $F$ with two operations $+$ and $\times$ such that for all $a, b, c \in F$:
>
> 1. Commutativity: $a + b = b + a$ and $ab = ba$.
>
> 2. There are two special elements $0, 1 \in F$ with $a + 0 = a$ and $a \cdot 1 = a$.
>
> 3. For each $a$, there is an inverse $-a$ for the operation $+$:    $a + (-a) = 0$.
>
> 4. For each $a \neq 0$, there is an inverse $a^{-1}$ for the operation $\times$:    $a a^{-1} = 1$.
>
> 5. Associativity: $a + (b + c) = (a + b) + c$ and $a(bc) = (ab)c$.
>
> 6. Distributivity (compatibility of the two operations): $a(b + c) = ab + ac$.

^def-3-1

> [!remark] Remark
> When $a = 0$, the inverse $a^{-1}$ does not exist, since $0 \cdot b = 0 \neq 1$ for every $b$. Note also that A4 is the only axiom distinguishing a field from a (commutative) ring: $\mathbb{Z}$ enjoys all the properties above *except* the existence of multiplicative inverses, so $\mathbb{Z}$ is a ring but not a field. Both $\mathbb{Q}$ and $\mathbb{R}$ are fields.

^rem-3-1

> [!remark] Remark: Dropping commutativity
> Can we think of a collection $M$ of elements that fails some of these properties — for example, with $ab \neq ba$? Yes: *matrices*. Non-commutativity of natural operations is important; in physics, the uncertainty principle is precisely a statement about two non-commuting operations.

^rem-3-2

## Order Axioms: Ordered Fields

The field properties above are purely algebraic. We now discuss a more geometric structure. One important geometric property of the line is the *sense of direction*: along a line we have left and right. This is directly related to **ordering**.

> [!definition] Definition §3.2: Order Axioms; Ordered Field
> Given $a, b \in \mathbb{Q}$, we can compare them to see if $a \leq b$. This order structure satisfies, for all $a, b, c$:
>
> 1. Either $a \leq b$ or $b \leq a$.  (*totality*)
>
> 2. If both $a \leq b$ and $b \leq a$, then $a = b$.  (*antisymmetry*)
>
> 3. If $a \leq b$ and $b \leq c$, then $a \leq c$.  (*transitivity*)
>
> 4. If $a \leq b$, then for any $c$: $a + c \leq b + c$.  (*compatibility with $+$*)
>
> 5. If $a \leq b$, then for any $c$ with $0 \leq c$: $ac \leq bc$.  (*compatibility with $\times$*)
>
> A field with an order $\leq$ satisfying O1–O5 is called an **ordered field**. Once we have $\leq$, we define $\geq$ by: $a \leq b$ if and only if $b \geq a$; and $a < b$ means $a \leq b$ and $a \neq b$.

^def-3-2

So $\mathbb{Q}$ is an ordered field, and similarly $\mathbb{R}$ is an ordered field — very reasonable when we represent $\mathbb{R}$ by the real line. Note that O4–O5 tie the order to the field operations; O1–O3 concern $\leq$ alone.

> [!theorem] Proposition §3.1: Basic Properties of Ordered Fields
> In any ordered field:
>
> - (a) If $a \leq b$, then $-b \leq -a$.
>
> - (b) If $a \leq b$ and $c \leq 0$, then $ac \geq bc$.
>
> - (c) If $a \leq 0$ and $b \leq 0$, then $ab \geq 0$.
>
> - (d) For any $a$: $a^2 \geq 0$.
>
> - (e) $0 < 1$.
>
> - (f) If $0 < a$, then $0 < a^{-1}$.
>
> - (g) If $0 < a < b$, then $0 < b^{-1} < a^{-1}$.

^prop-3-1

> [!proof]+ Proof
> (a) From $a \leq b$, add $c = (-a) + (-b)$ to both sides (O4):
>
> $$
> a + (-a) + (-b) \leq b + (-a) + (-b), \qquad \text{i.e.} \qquad -b \leq -a.
> $$
>
> (b) Suppose $a \leq b$ and $c \leq 0$. By (a) applied to $c \leq 0$, we get $0 \leq -c$. By O5, multiplying $a \leq b$ by $-c \geq 0$ gives $a(-c) \leq b(-c)$, i.e. $-ac \leq -bc$. By (a) again, $bc \leq ac$, i.e. $ac \geq bc$.
>
> (c) Suppose $a \leq 0$ and $b \leq 0$. Apply (b) with the inequality $a \leq 0$ and the multiplier $b \leq 0$: this gives $ab \geq 0 \cdot b = 0$.
>
> (d) If $a \geq 0$, then O5 (multiplying $0 \leq a$ by $a \geq 0$) gives $0 \leq a^2$. If $a \leq 0$, then (c) with $b = a$ gives $a^2 = a \cdot a \geq 0$. By O1 these cases are exhaustive.
>
> (e) By (d), $1 = 1^2 \geq 0$. Since $1 \neq 0$ (A2 provides two *distinct* special elements), we conclude $0 < 1$.
>
> (f) Let $0 < a$. First, $a^{-1} \neq 0$, since $a a^{-1} = 1 \neq 0$. Suppose for contradiction $a^{-1} < 0$. Multiplying $a^{-1} \leq 0$ by $a \geq 0$ (O5, in the form of (b) with roles arranged: from $a^{-1} \leq 0$ and $0 \leq a$, O5 gives $a^{-1} a \leq 0 \cdot a$) yields $1 \leq 0$, contradicting (e). Hence $0 < a^{-1}$.
>
> (g) Let $0 < a < b$. By (f), $a^{-1} > 0$ and $b^{-1} > 0$; then $a^{-1} b^{-1} > 0$ (O5: multiply $0 \leq a^{-1}$ by $b^{-1} \geq 0$; equality $a^{-1}b^{-1} = 0$ is impossible since $(a^{-1}b^{-1})(ba) = 1 \neq 0$). Multiplying $a < b$ by $a^{-1} b^{-1} \geq 0$ (O5) gives
>
> $$
> a \cdot a^{-1} b^{-1} \leq b \cdot a^{-1} b^{-1}, \qquad \text{i.e.} \qquad b^{-1} \leq a^{-1},
> $$
>
> and equality is impossible: $b^{-1} = a^{-1}$ would give $a = b$ after multiplying by $ab$. Hence $0 < b^{-1} < a^{-1}$.

^pf-3-1

> [!remark] Remark
> The lecture proved (e) by contradiction: if $0 \geq 1$, multiply by any $a > 0$ to get $0 \geq a$ — so *no* element could be positive, which is absurd. The proof above via (d) reaches the same conclusion directly. The remaining proofs are in the book (§3 of Ross); they are all short manipulations of O1–O5 of the same kind as above.

^rem-3-3

## Partial Orders; $\mathbb{C}$ Is Not an Ordered Field

People often expect to order everything — in competitions, in admission to schools. This expectation is exactly property O1: any two elements can be compared. But O1 is not always available.

> [!definition] Definition §3.3: Ordered and Partially Ordered Sets
> A set with a relation $\leq$ satisfying O1, O2, O3 is called an **ordered set** (or **linearly ordered set**). If $\leq$ satisfies only O2, O3 (dropping totality O1), the set is called a **partially ordered set**. (O4, O5 are not part of these definitions: they refer to the algebraic operations of a field.)

^def-3-3

> [!example] Example §3.1: The product order on $\mathbb{R}^2$ is partial but not linear
> On the plane $\mathbb{R}^2$, define
>
> $$
> (x_1, y_1) \leq (x_2, y_2) \quad \text{if} \quad x_1 \leq x_2 \ \text{and}\ y_1 \leq y_2.
> $$
>
> This satisfies O2 and O3, but not O1: the points $(1,2)$ and $(2,1)$ cannot be compared.

^ex-3-1

> [!example] Example §3.2: The lexicographic order
> We *can* define a linear order on $\mathbb{R}^2$:
>
> $$
> (x_1, y_1) \leq (x_2, y_2) \quad \text{if} \quad \text{either (1) } x_1 < x_2, \text{ or (2) } x_1 = x_2 \text{ and } y_1 \leq y_2.
> $$
>
> This is the **lexicographic (dictionary) order** — the order we use almost every day when looking up words in a dictionary.

^ex-3-2

![[m451-3-1.svg]]
*Left: in the product order the points comparable with $(1,2)$ fill exactly the two shaded quadrants ($\geq$ above right, $\leq$ below left); $(2,1)$ (red) lies in neither, so O1 fails. Right: in the lexicographic order every point with larger first coordinate, together with the ray above $(1,2)$ on its own vertical line, is $> (1,2)$ — so $(2,1) > (1,2)$, and any two points can be compared.*

Since $\mathbb{C}$ can be identified with $\mathbb{R}^2$, the lexicographic order makes $\mathbb{C}$ a linearly ordered *set*. Nevertheless:

> [!theorem] Proposition §3.2: $\mathbb{C}$ is not an ordered field
> $\mathbb{C}$ is a field, but there is no order $\leq$ on $\mathbb{C}$ satisfying O1–O5, i.e. no order compatible with its field operations.

^prop-3-2

> [!proof]+ Proof
> Suppose such an order existed. By property (d) above, every square is $\geq 0$; in particular $i^2 = -1 \geq 0$. But by (e), $0 < 1$, and by (a), $-1 < 0$. So $-1 \geq 0$ and $-1 < 0$ simultaneously — a contradiction.

^pf-3-2

## Absolute Value and Distance

For an ordered field like $\mathbb{Q}$ or $\mathbb{R}$, we have the notion of absolute value.

> [!definition] Definition §3.4: Absolute Value
> For $a \in \mathbb{R}$, define
>
> $$
> |a| =
> \begin{cases}
> \ a & \text{if } a \geq 0, \\
> \ -a & \text{if } a \leq 0.
> \end{cases}
> $$
>
> In the latter case $-a \geq 0$ (property (a)), so in any case $|a| \geq 0$.

^def-3-4

> [!theorem] Theorem §3.3: Properties of the Absolute Value
> For all $a, b \in \mathbb{R}$:
>
> - (i) $|a + b| \leq |a| + |b|$  (*[[Triangle inequality|triangle inequality]]*)
>
> - (ii) $|ab| = |a| \, |b|$.

^thm-3-3

> [!proof]+ Proof
> (i) From the definition, $-|a| \leq a \leq |a|$ and $-|b| \leq b \leq |b|$. Adding (O4 twice),
>
> $$
> -(|a| + |b|) \leq a + b \leq |a| + |b|.
> $$
>
> If $a + b \geq 0$, the right inequality gives $|a+b| = a+b \leq |a| + |b|$. If $a + b \leq 0$, the left inequality and (a) give $|a+b| = -(a+b) \leq |a| + |b|$.
>
> (ii) Check by cases. If $a, b \geq 0$, then $ab \geq 0$ (O5) and $|ab| = ab = |a||b|$. If $a, b \leq 0$, then $ab \geq 0$ (property (c)) and $|ab| = ab = (-a)(-b) = |a||b|$. If one is $\geq 0$ and the other $\leq 0$, say $a \geq 0 \geq b$, then $ab \leq 0$ (property (b)) and $|ab| = -ab = a(-b) = |a||b|$.

^pf-3-3

> [!remark] Remark
> Think about what these two properties mean: they describe how $|\cdot|$ interacts with the two field operations $+$ and $\times$ — sub-additive for $+$ (with equality exactly when $a, b$ have the same sign), and exactly multiplicative for $\times$.

^rem-3-4

> [!definition] Definition §3.5: Distance
> The **distance** between two numbers $a, b \in \mathbb{R}$ (two points on the real line) is
>
> $$
> \operatorname{dist}(a, b) = |a - b|.
> $$

^def-3-5

> [!theorem] Proposition §3.4: Properties of Distance
> For all $a, b, c \in \mathbb{R}$:
>
> - (i) $\operatorname{dist}(a,b) = \operatorname{dist}(b,a)$  (*symmetry*)
>
> - (ii) $\operatorname{dist}(a,c) \leq \operatorname{dist}(a,b) + \operatorname{dist}(b,c)$  (*triangle property*)

^prop-3-4

> [!proof]+ Proof
> (i) $|a - b| = |-(b-a)| = |b - a|$, using $|{-x}| = |x|$ from the definition. (Symmetry is not automatic in real life: an airplane ticket between two places may well depend on the direction!)
>
> (ii) Write $a - c = (a - b) + (b - c)$ and apply the triangle inequality:
>
> $$
> \operatorname{dist}(a,c) = |a - c| = |(a-b) + (b-c)| \leq |a - b| + |b - c| = \operatorname{dist}(a,b) + \operatorname{dist}(b,c).
> $$
>
> This explains the name *triangle* property: going from $a$ to $c$ directly is never longer than passing through an intermediate point $b$.

^pf-3-4
