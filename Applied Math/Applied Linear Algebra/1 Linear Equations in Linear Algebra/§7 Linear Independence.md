---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 7
lay: "1.7"
aliases: ["Lay 1.7"]
tags: [applied-linear-algebra, math235]
---
← [[§6 Applications of Linear Systems]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§8 Introduction to Linear Transformations]] →

*Lay, Section 1.7 · MATH 235 lectures L3, Feb-18.*

The homogeneous equation $x_1\mathbf{v}_1 + \cdots + x_p\mathbf{v}_p = \mathbf{0}$ always has the trivial solution. The vectors are linearly independent when it has no other. Then each vector in their span is a combination of them in only one way, and none of them is redundant. Testing independence means row reducing and looking for a free variable. Sets of one or two vectors can be judged by inspection, a set that contains $\mathbf{0}$ or has more vectors than entries is automatically dependent, and a set is dependent exactly when one of its vectors is a linear combination of the others.

## Linear Independence

> [!definition] Definition §7.1: Linearly Independent, Linearly Dependent, Linear Dependence Relation
> An indexed set of vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ in $\mathbb{R}^n$ is **linearly independent** if the vector equation
>
> $$
> x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_p\mathbf{v}_p = \mathbf{0}
> $$
>
> has only the trivial solution. The set is **linearly dependent** if there exist weights $c_1, \ldots, c_p$, not all zero, such that
>
> $$
> c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_p\mathbf{v}_p = \mathbf{0} ; \qquad (2)
> $$
>
> equation (2), with weights not all zero, is a **linear dependence relation** among $\mathbf{v}_1, \ldots, \mathbf{v}_p$. A set is linearly dependent if and only if it is not linearly independent. For brevity, "$\mathbf{v}_1, \ldots, \mathbf{v}_p$ are linearly dependent" means that $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ is a linearly dependent set, and likewise for independent. (The lecture's form: $\mathbf{v}_1, \ldots, \mathbf{v}_m$ are linearly dependent if $A\mathbf{x} = \mathbf{0}$, $A = [\,\mathbf{v}_1\ \cdots\ \mathbf{v}_m\,]$, has a solution $\mathbf{x} \ne \mathbf{0}$; see Proposition §7.1.)
>
> *Lay: 1.7, Definition*

^def-7-1

> [!remark]- Connections
> - Rigorous treatment: [[§4 Span and Linear Independence#^ladr-2-15|LADR 2.15]] and [[§4 Span and Linear Independence#^ladr-2-17|LADR 2.17]], for lists in any vector space (the empty list counts as independent). Axler notes the equivalent form: the list is independent iff each vector in its span has exactly one representation as a linear combination of it.
> - See also: [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-2|331 Def. §29.2]] (the same definition, with real or complex weights) and, for vector functions on an interval, [[§29 Systems of Linear Algebraic Equations; Linear Independence, Eigenvalues, Eigenvectors#^def-29-3|331 Def. §29.3]], the notion used for solutions of $\mathbf{x}' = A\mathbf{x}$.

> [!theorem] Proposition §7.1: Independence of Matrix Columns
> The columns of a matrix $A$ are linearly independent if and only if the equation $A\mathbf{x} = \mathbf{0}$ has *only* the trivial solution.
>
> *Lay: 1.7, boxed statement (3)*

^prop-7-1

> [!proof]+ Proof
> If $A = [\,\mathbf{a}_1\ \cdots\ \mathbf{a}_n\,]$, then $A\mathbf{x} = x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$ ([[§4 The Matrix Equation Ax = b#^def-4-1|Definition §4.1]]). So the solutions of $A\mathbf{x} = \mathbf{0}$ are exactly the lists of weights $(x_1, \ldots, x_n)$ with $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = \mathbf{0}$; each linear dependence relation among the columns is a nontrivial solution and conversely. Now apply Definition §7.1.

^pf-7-1

*Uses:* [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]], [[§7 Linear Independence#^def-7-1|Def. §7.1]]

By [[§5 Solution Sets of Linear Systems#^cor-5-1|Corollary §5.1]], the test is: row reduce $A$ (or $[\,A\ \ \mathbf{0}\,]$). The columns are independent if there is no free variable, that is, a pivot in every column, and dependent if there is a free variable. The order of the vectors does not matter.

> [!example] Example §7.1: Dependent or Independent?
> **(a)** Let $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}$. Is $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ linearly independent? If not, find a linear dependence relation.
>
> Row reduce the augmented matrix of $x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + x_3\mathbf{v}_3 = \mathbf{0}$ ($R_2 - 2R_1$, $R_3 - 3R_1$, then $R_3 - 2R_2$):
>
> $$
> \begin{bmatrix} 1 & 4 & 2 & 0 \\ 2 & 5 & 1 & 0 \\ 3 & 6 & 0 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 4 & 2 & 0 \\ 0 & -3 & -3 & 0 \\ 0 & -6 & -6 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 4 & 2 & 0 \\ 0 & -3 & -3 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> $x_1, x_2$ are basic and $x_3$ is free, so each nonzero $x_3$ gives a nontrivial solution: the vectors are linearly **dependent**. To find a relation, finish the reduction ($-\tfrac13 R_2$, then $R_1 - 4R_2$):
>
> $$
> \begin{bmatrix} 1 & 0 & -2 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}, \qquad x_1 = 2x_3, \quad x_2 = -x_3 .
> $$
>
> Taking $x_3 = 5$ gives $x_1 = 10$, $x_2 = -5$, and the relation
>
> $$
> 10\mathbf{v}_1 - 5\mathbf{v}_2 + 5\mathbf{v}_3 = \mathbf{0}
> $$
>
> (one of infinitely many; $x_3 = 1$ gives $\mathbf{v}_2 = 2\mathbf{v}_1 + \mathbf{v}_3$). **Check:** $2(1, 2, 3) + (2, 1, 0) = (4, 5, 6)$. As the lecture concludes, $\mathbf{v}_3$ is redundant: $\operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\} = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\}$ is a plane (Proposition §7.5).
>
> **(b)** Are the columns of $A = \begin{bmatrix} 0 & 1 & 4 \\ 1 & 2 & -1 \\ 5 & 8 & 0 \end{bmatrix}$ linearly independent? Interchange rows 1 and 2, then $R_3 - 5R_1$, then $R_3 + 2R_2$:
>
> $$
> \begin{bmatrix} 0 & 1 & 4 & 0 \\ 1 & 2 & -1 & 0 \\ 5 & 8 & 0 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 2 & -1 & 0 \\ 0 & 1 & 4 & 0 \\ 0 & -2 & 5 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 2 & -1 & 0 \\ 0 & 1 & 4 & 0 \\ 0 & 0 & 13 & 0 \end{bmatrix} .
> $$
>
> Three basic variables and no free variable: $A\mathbf{x} = \mathbf{0}$ has only the trivial solution, and the columns are linearly **independent**.
>
> *Lay: Examples 1.7.1 and 1.7.2*
> *Source: 235 lecture Feb-18*

^ex-7-1

## Sets of One or Two Vectors

> [!theorem] Proposition §7.2: Sets of One Vector
> A set $\{\mathbf{v}\}$ containing only one vector is linearly independent if and only if $\mathbf{v} \ne \mathbf{0}$.
>
> *Lay: 1.7 (text)*

^prop-7-2

> [!proof]+ Proof
> If $\mathbf{v} \ne \mathbf{0}$ and $x_1\mathbf{v} = \mathbf{0}$ with $x_1 \ne 0$, then $\mathbf{v} = \tfrac{1}{x_1}(x_1\mathbf{v}) = \tfrac{1}{x_1}\mathbf{0} = \mathbf{0}$, a contradiction; so $x_1\mathbf{v} = \mathbf{0}$ has only the trivial solution. If $\mathbf{v} = \mathbf{0}$, then $x_1\mathbf{0} = \mathbf{0}$ for every $x_1$, so there are nontrivial solutions (e.g. $x_1 = 1$).

^pf-7-2

*Uses:* [[§7 Linear Independence#^def-7-1|Def. §7.1]], [[§3 Vector Equations#^thm-3-2|§3.2]]

> [!theorem] Proposition §7.3: Sets of Two Vectors
> A set of two vectors $\{\mathbf{v}_1, \mathbf{v}_2\}$ is linearly dependent if at least one of the vectors is a multiple of the other. The set is linearly independent if and only if neither of the vectors is a multiple of the other. Geometrically: two vectors are linearly dependent if and only if they lie on the same line through the origin.
>
> *Lay: 1.7, boxed statement*

^prop-7-3

> [!proof]+ Proof
> If $\mathbf{v}_2 = k\mathbf{v}_1$, then $k\mathbf{v}_1 - \mathbf{v}_2 = \mathbf{0}$ is a linear dependence relation (the weight of $\mathbf{v}_2$ is $-1 \ne 0$); similarly if $\mathbf{v}_1 = k\mathbf{v}_2$. Conversely, suppose $c\mathbf{v}_1 + d\mathbf{v}_2 = \mathbf{0}$ with $c, d$ not both zero. If $c \ne 0$, then $\mathbf{v}_1 = (-d/c)\mathbf{v}_2$ is a multiple of $\mathbf{v}_2$; if $c = 0$, then $d \ne 0$ and $\mathbf{v}_2 = (-c/d)\mathbf{v}_1 = \mathbf{0} = 0\mathbf{v}_1$ is a multiple of $\mathbf{v}_1$. So the set is dependent exactly when one vector is a multiple of the other, and independent exactly when neither is. (This is the argument of Lay's Example 3(b) and of the lecture.) Two vectors one of which is a multiple of the other lie on one line through $\mathbf{0}$, and conversely.

^pf-7-3

*Uses:* [[§7 Linear Independence#^def-7-1|Def. §7.1]]

So for two vectors no row operations are needed: check by inspection whether one is a multiple of the other. (The test applies only to sets of *two* vectors.) In the lecture's words, two independent vectors span a plane, two dependent ones only a line.

## Sets of Two or More Vectors

> [!theorem] Theorem §7.4: Characterization of Linearly Dependent Sets
> An indexed set $S = \{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ of two or more vectors is linearly dependent if and only if at least one of the vectors in $S$ is a linear combination of the others. In fact, if $S$ is linearly dependent and $\mathbf{v}_1 \ne \mathbf{0}$, then some $\mathbf{v}_j$ (with $j > 1$) is a linear combination of the preceding vectors, $\mathbf{v}_1, \ldots, \mathbf{v}_{j-1}$.
>
> *Lay: Theorem 7 (1.7)*

^thm-7-4

> [!proof]+ Proof
> **If some vector is a combination of the others, $S$ is dependent.** Suppose $\mathbf{v}_j = \sum_{i \ne j} c_i\mathbf{v}_i$. Subtracting $\mathbf{v}_j$ from both sides gives a linear dependence relation with the nonzero weight $-1$ on $\mathbf{v}_j$. For instance, if $\mathbf{v}_1 = c_2\mathbf{v}_2 + c_3\mathbf{v}_3$, then $\mathbf{0} = (-1)\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 + 0\mathbf{v}_4 + \cdots + 0\mathbf{v}_p$.
>
> **Conversely**, suppose $S$ is linearly dependent. If $\mathbf{v}_1 = \mathbf{0}$, it is a (trivial) linear combination of the others: $\mathbf{v}_1 = 0\mathbf{v}_2 + \cdots + 0\mathbf{v}_p$. Otherwise $\mathbf{v}_1 \ne \mathbf{0}$, and there are weights $c_1, \ldots, c_p$, not all zero, with
>
> $$
> c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_p\mathbf{v}_p = \mathbf{0} .
> $$
>
> Let $j$ be the largest subscript for which $c_j \ne 0$. If $j = 1$, then $c_1\mathbf{v}_1 = \mathbf{0}$ with $c_1 \ne 0$, which is impossible because $\mathbf{v}_1 \ne \mathbf{0}$ (Proposition §7.2). So $j > 1$, and
>
> $$
> c_1\mathbf{v}_1 + \cdots + c_j\mathbf{v}_j + 0\mathbf{v}_{j+1} + \cdots + 0\mathbf{v}_p = \mathbf{0}, \qquad
> c_j\mathbf{v}_j = -c_1\mathbf{v}_1 - \cdots - c_{j-1}\mathbf{v}_{j-1},
> $$
>
> $$
> \mathbf{v}_j = \Big(-\frac{c_1}{c_j}\Big)\mathbf{v}_1 + \cdots + \Big(-\frac{c_{j-1}}{c_j}\Big)\mathbf{v}_{j-1} ,
> $$
>
> a linear combination of the preceding vectors, and in particular of the others.

^pf-7-4

*Uses:* [[§7 Linear Independence#^def-7-1|Def. §7.1]], [[§7 Linear Independence#^prop-7-2|§7.2]]

> [!remark]- Connections
> - Rigorous treatment: the linear dependence lemma, [[§4 Span and Linear Independence#^ladr-2-19|LADR 2.19]], with the same "largest index with nonzero weight" proof; Axler adds that removing such a $\mathbf{v}_j$ does not change the span (Proposition §7.5 below), the step behind every "a spanning list contains a basis" argument.

> [!remark] Remark: Warning
> Theorem §7.4 does *not* say that *every* vector in a linearly dependent set is a linear combination of the preceding (or of the other) vectors. For example, $\{(1, 0, 0), (2, 0, 0), (0, 0, 1)\}$ is dependent, but $(0, 0, 1)$ is not a combination of the other two.

^rem-7-1

> [!theorem] Proposition §7.5: Dropping a Redundant Vector
> Call $\mathbf{v}_j$ **redundant** in $\{\mathbf{v}_1, \ldots, \mathbf{v}_m\}$ if it is a linear combination of the other vectors $\mathbf{v}_1, \ldots, \mathbf{v}_{j-1}, \mathbf{v}_{j+1}, \ldots, \mathbf{v}_m$. Then
>
> $$
> \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_m\} = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_{j-1}, \mathbf{v}_{j+1}, \ldots, \mathbf{v}_m\} .
> $$
>
> By Theorem §7.4, a set of two or more vectors is linearly dependent exactly when it contains a redundant vector. So a linearly dependent set has too many vectors for a parametric description of its span.
>
> *Source: 235 lecture Feb-18*

^prop-7-5

> [!proof]+ Proof
> The right side is contained in the left (take weight $0$ on $\mathbf{v}_j$). Conversely, write $\mathbf{v}_j = \sum_{i \ne j} b_i\mathbf{v}_i$. Any $\mathbf{y} = c_1\mathbf{v}_1 + \cdots + c_m\mathbf{v}_m$ in the left side equals
>
> $$
> \mathbf{y} = \sum_{i \ne j} c_i\mathbf{v}_i + c_j\sum_{i \ne j} b_i\mathbf{v}_i = \sum_{i \ne j} (c_i + c_jb_i)\mathbf{v}_i ,
> $$
>
> a linear combination of the vectors other than $\mathbf{v}_j$.

^pf-7-5

*Uses:* [[§3 Vector Equations#^def-3-4|Def. §3.4]], [[§3 Vector Equations#^thm-3-2|§3.2]]

> [!example] Example §7.2: Removing Redundant Vectors
> Let $\mathbf{v}_1 = \begin{bmatrix} 1 \\ -4 \\ -3 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 3 \\ 2 \\ -2 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} 4 \\ -6 \\ -7 \end{bmatrix}$, whose span is the plane $x - \tfrac{y}{2} + z = 0$ ([[§4 The Matrix Equation Ax = b#^ex-4-2|Example §4.2]]). Show that they are linearly dependent and simplify the description of the span.
>
> Row reduce $A = [\,\mathbf{v}_1\ \mathbf{v}_2\ \mathbf{v}_3\,]$ ($R_2 + 4R_1$, $R_3 + 3R_1$, $R_3 - \tfrac12 R_2$; then $\tfrac1{14}R_2$ and $R_1 - 3R_2$):
>
> $$
> \begin{bmatrix} 1 & 3 & 4 \\ -4 & 2 & -6 \\ -3 & -2 & -7 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & 4 \\ 0 & 14 & 10 \\ 0 & 0 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & 4 \\ 0 & 1 & \tfrac57 \\ 0 & 0 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & \tfrac{13}{7} \\ 0 & 1 & \tfrac57 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> ($4 - 3 \cdot \tfrac57 = \tfrac{13}{7}$.) $x_3 = t$ is free, so the vectors are dependent, and $x_1 = -\tfrac{13}{7}t$, $x_2 = -\tfrac57 t$. With $t = 7$:
>
> $$
> -13\mathbf{v}_1 - 5\mathbf{v}_2 + 7\mathbf{v}_3 = \mathbf{0} .
> $$
>
> **Check:** first entries $-13 - 15 + 28 = 0$; second $52 - 10 - 42 = 0$; third $39 + 10 - 49 = 0$. All three weights are nonzero, so *each* vector is a combination of the other two and is redundant. By Proposition §7.5,
>
> $$
> \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\} = \operatorname{Span}\{\mathbf{v}_2, \mathbf{v}_3\} = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_3\} = \operatorname{Span}\{\mathbf{v}_1, \mathbf{v}_2\} .
> $$
>
> Any two of them, being non-proportional, describe the plane without redundancy.
>
> *In the lecture (p. 3) the third entry of $\mathbf{v}_3$ is written $7$ in places; it is $-7$ (as on p. 2), and the row reduction there is the one for $-7$.*
>
> *Source: 235 lecture Feb-18*

^ex-7-2

> [!example] Example §7.3: Two Vectors, and a Third in Their Plane
> **(a)** $\mathbf{v}_1 = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 6 \\ 2 \end{bmatrix}$: $\mathbf{v}_2 = 2\mathbf{v}_1$, so $-2\mathbf{v}_1 + \mathbf{v}_2 = \mathbf{0}$ and the set is dependent. $\mathbf{v}_1 = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 6 \\ 2 \end{bmatrix}$: neither is a multiple of the other ($6/3 \ne 2/2$), so the set is independent (Proposition §7.3).
>
> **(b)** Let $\mathbf{u} = \begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} 1 \\ 6 \\ 0 \end{bmatrix}$. Describe $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$, and explain why $\mathbf{w}$ is in $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$ if and only if $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is linearly dependent.
>
> Neither of $\mathbf{u}$, $\mathbf{v}$ is a multiple of the other, so they are independent and span a plane in $\mathbb{R}^3$: the $x_1x_2$-plane ($x_3 = 0$), since both have third entry $0$ and any $(a, b, 0)$ is a combination of them. If $\mathbf{w}$ is a combination of $\mathbf{u}$ and $\mathbf{v}$, then $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is dependent by Theorem §7.4. Conversely, if $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is dependent, then since $\mathbf{u} \ne \mathbf{0}$, Theorem §7.4 makes some vector a combination of the *preceding* ones. It is not $\mathbf{v}$ (not a multiple of $\mathbf{u}$), so it is $\mathbf{w}$, and $\mathbf{w}$ lies in $\operatorname{Span}\{\mathbf{u}, \mathbf{v}\}$. The same holds for any $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ in $\mathbb{R}^3$ with $\mathbf{u}$, $\mathbf{v}$ independent: the set is dependent if and only if $\mathbf{w}$ lies in the plane spanned by $\mathbf{u}$ and $\mathbf{v}$.
>
> *Lay: Examples 1.7.3 and 1.7.4*

^ex-7-3

![[m235-7-1.svg]]
*Example §7.3(b): $\mathbf{u}$ and $\mathbf{v}$ span the $x_1x_2$-plane. If $\mathbf{w}$ lies in that plane, $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is dependent (left); if $\mathbf{w}$ leaves the plane, the set is independent (right).*

## Automatic Dependence

> [!theorem] Theorem §7.6: More Vectors Than Entries Means Dependent
> If a set contains more vectors than there are entries in each vector, then the set is linearly dependent. That is, any set $\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ in $\mathbb{R}^n$ is linearly dependent if $p > n$.
>
> *Lay: Theorem 8 (1.7)*

^thm-7-6

> [!proof]+ Proof
> Let $A = [\,\mathbf{v}_1\ \cdots\ \mathbf{v}_p\,]$. Then $A$ is $n \times p$, and $A\mathbf{x} = \mathbf{0}$ is a system of $n$ equations in $p$ unknowns. At most one pivot fits in each row, so there are at most $n$ pivot columns; if $p > n$, there are more variables than equations, and some variable is free. Hence $A\mathbf{x} = \mathbf{0}$ has a nontrivial solution ([[§5 Solution Sets of Linear Systems#^cor-5-1|Corollary §5.1]]), and the columns of $A$ are linearly dependent (Proposition §7.1). In matrix form: a wide $n \times p$ matrix ($p > n$) always has dependent columns.

^pf-7-6

*Uses:* [[§5 Solution Sets of Linear Systems#^cor-5-1|§5.1]], [[§7 Linear Independence#^prop-7-1|§7.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§4 Span and Linear Independence#^ladr-2-22|LADR 2.22]] (an independent list is never longer than a spanning list), applied with the spanning list $\mathbf{e}_1, \ldots, \mathbf{e}_n$ of $\mathbb{R}^n$ ([[§4 Span and Linear Independence#^ladr-2-23|LADR 2.23]]); Axler proves it by exchanging vectors, Lay by counting pivots. Equivalent form for homogeneous systems: [[§8 Null Spaces and Ranges#^ladr-3-26|LADR 3.26]].

*Warning:* Theorem §7.6 says nothing when the number of vectors does *not* exceed the number of entries.

> [!theorem] Theorem §7.7: A Set Containing Zero Is Dependent
> If a set $S = \{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ in $\mathbb{R}^n$ contains the zero vector, then the set is linearly dependent.
>
> *Lay: Theorem 9 (1.7)*

^thm-7-7

> [!proof]+ Proof
> By renumbering the vectors, we may suppose $\mathbf{v}_1 = \mathbf{0}$. Then $1\mathbf{v}_1 + 0\mathbf{v}_2 + \cdots + 0\mathbf{v}_p = \mathbf{0}$ is a linear dependence relation.

^pf-7-7

*Uses:* [[§7 Linear Independence#^def-7-1|Def. §7.1]]

> [!example] Example §7.4: Deciding by Inspection
> **(a)** $\begin{bmatrix} 2 \\ 1 \end{bmatrix}, \begin{bmatrix} 4 \\ -1 \end{bmatrix}, \begin{bmatrix} -2 \\ 2 \end{bmatrix}$ are dependent by Theorem §7.6 (three vectors with two entries each), although none of them is a multiple of another.
>
> **(b)** $\begin{bmatrix} 1 \\ 7 \\ 6 \end{bmatrix}, \begin{bmatrix} 2 \\ 0 \\ 9 \end{bmatrix}, \begin{bmatrix} 3 \\ 1 \\ 5 \end{bmatrix}, \begin{bmatrix} 4 \\ 1 \\ 8 \end{bmatrix}$: four vectors in $\mathbb{R}^3$, dependent by Theorem §7.6.
>
> **(c)** $\begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\ 8 \end{bmatrix}$: Theorem §7.6 does not apply, but the set contains $\mathbf{0}$, so it is dependent by Theorem §7.7.
>
> **(d)** $\begin{bmatrix} -2 \\ 4 \\ 6 \\ 10 \end{bmatrix}, \begin{bmatrix} 3 \\ -6 \\ -9 \\ 15 \end{bmatrix}$: the second vector looks like $-\tfrac32$ times the first, and this holds for the first three pairs of entries ($3, -6, -9$), but $-\tfrac32 \cdot 10 = -15 \ne 15$. Neither vector is a multiple of the other, so the set is independent (Proposition §7.3).
>
> *Lay: Examples 1.7.5 and 1.7.6*

^ex-7-4

> [!example] Example §7.5: Dependence Depending on a Parameter
> For which $h$ are $\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \\ 4 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 3 \\ -5 \\ 7 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} -1 \\ 5 \\ h \end{bmatrix}$ linearly dependent?
>
> Row reduce ($R_2 + R_1$, $R_3 - 4R_1$; then $-\tfrac12 R_2$; then $R_3 + 5R_2$):
>
> $$
> \begin{bmatrix} 1 & 3 & -1 \\ -1 & -5 & 5 \\ 4 & 7 & h \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & -1 \\ 0 & -2 & 4 \\ 0 & -5 & h + 4 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & -1 \\ 0 & 1 & -2 \\ 0 & -5 & h + 4 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 3 & -1 \\ 0 & 1 & -2 \\ 0 & 0 & h - 6 \end{bmatrix} .
> $$
>
> If $h = 6$, column 3 has no pivot, $x_3$ is free, and the vectors are dependent; indeed then $-5\mathbf{v}_1 + 2\mathbf{v}_2 + \mathbf{v}_3 = \mathbf{0}$ (check: $-5 + 6 - 1 = 0$, $5 - 10 + 5 = 0$, $-20 + 14 + 6 = 0$). If $h \ne 6$, there is a pivot in every column, no free variable, and the vectors are independent.
>
> *The lecture (p. 5) labels the second step "÷2"; it is division by $-2$, which gives the row $(0, 1, -2)$ written there.*
>
> *Source: 235 lecture Feb-18*

^ex-7-5
