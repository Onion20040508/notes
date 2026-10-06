---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 50
lay: "6.1"
aliases: ["Lay 6.1 (cont.)"]
tags: [applied-linear-algebra, math235]
---
← [[§49 Inner Product, Length, and Orthogonality]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§51 Orthogonal Sets]] →

*Lay, Section 6.1 · MATH 235 lecture L22.*

The main theorem says that the row space and the null space of a matrix are orthogonal complements, and so are the column space and the null space of the transpose.

## Orthogonal Complements

> [!definition] Definition §60.1: Orthogonal Complement
> Let $W$ be a subspace of $\mathbb{R}^n$. A vector $\mathbf{z}$ is **orthogonal to $W$** if $\mathbf{z}$ is orthogonal to every vector in $W$. The set of all vectors orthogonal to $W$ is the **orthogonal complement** of $W$, written $W^\perp$ (read "$W$ perp"):
>
> $$
> W^\perp = \{\mathbf{z} \in \mathbb{R}^n : \mathbf{z} \cdot \mathbf{w} = 0 \text{ for all } \mathbf{w} \in W\} .
> $$
>
> *Lay: 6.1 (text)*

^def-50-1

> [!theorem] Theorem §60.1: Basic Facts About the Orthogonal Complement
> Let $W$ be a subspace of $\mathbb{R}^n$.
>
> 1. A vector $\mathbf{x}$ is in $W^\perp$ if and only if $\mathbf{x}$ is orthogonal to every vector in a set that spans $W$.
> 2. $W^\perp$ is a subspace of $\mathbb{R}^n$.
> 3. $W \cap W^\perp = \{\mathbf{0}\}$.
>
> *Lay: 6.1, boxed facts 1 and 2; Exercise 31*

^thm-50-1

> [!proof]+ Proof
> Lay suggests these proofs in Exercises 29–31.
>
> (1) If $\mathbf{x} \in W^\perp$, then $\mathbf{x}$ is orthogonal to every vector of $W$, in particular to the vectors of a spanning set. Conversely, let $W = \operatorname{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_p\}$ and $\mathbf{x} \cdot \mathbf{v}_j = 0$ for every $j$. Any $\mathbf{w} \in W$ is $\mathbf{w} = c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p$, and by the linear-combination rule of [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|Theorem §49.1]],
>
> $$
> \mathbf{w} \cdot \mathbf{x} = c_1(\mathbf{v}_1 \cdot \mathbf{x}) + \cdots + c_p(\mathbf{v}_p \cdot \mathbf{x}) = 0 .
> $$
>
> (2) $\mathbf{0} \in W^\perp$. Let $\mathbf{z}, \mathbf{z}_1, \mathbf{z}_2 \in W^\perp$, $c$ a scalar, and $\mathbf{u} \in W$. Then $(c\mathbf{z}) \cdot \mathbf{u} = c(\mathbf{z} \cdot \mathbf{u}) = 0$ and $(\mathbf{z}_1 + \mathbf{z}_2) \cdot \mathbf{u} = \mathbf{z}_1 \cdot \mathbf{u} + \mathbf{z}_2 \cdot \mathbf{u} = 0$. Since $\mathbf{u}$ was arbitrary, $c\mathbf{z}$ and $\mathbf{z}_1 + \mathbf{z}_2$ lie in $W^\perp$, which is therefore closed under scalar multiplication and addition.
>
> (3) If $\mathbf{x} \in W$ and $\mathbf{x} \in W^\perp$, then $\mathbf{x}$ is orthogonal to itself: $\mathbf{x} \cdot \mathbf{x} = 0$, so $\mathbf{x} = \mathbf{0}$ by [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|Theorem §49.1]](d).

^pf-50-1

*Uses:* [[§49 Inner Product, Length, and Orthogonality#^thm-49-1|§49.1]], [[§21 Subspaces of ℝⁿ#^def-21-1|Def. §21.1]] (subspace)

> [!theorem] Theorem §60.2: The Fundamental Subspaces Are Orthogonal Complements
> Let $A$ be an $m \times n$ matrix. The orthogonal complement of the row space of $A$ is the null space of $A$, and the orthogonal complement of the column space of $A$ is the null space of $A^T$:
>
> $$
> (\operatorname{Row} A)^\perp = \operatorname{Nul} A \qquad\text{and}\qquad (\operatorname{Col} A)^\perp = \operatorname{Nul} A^T .
> $$
>
> *Lay: Theorem 3 (6.1)*

^thm-50-2

> [!proof]+ Proof
> Both equalities of sets are proved by showing two inclusions.
>
> Let $\mathbf{r}_1, \ldots, \mathbf{r}_m \in \mathbb{R}^n$ be the rows of $A$, written as vectors. By the row–column rule, the $i$th entry of $A\mathbf{x}$ is $\mathbf{r}_i \cdot \mathbf{x}$. If $\mathbf{x} \in \operatorname{Nul} A$, then $A\mathbf{x} = \mathbf{0}$, so $\mathbf{r}_i \cdot \mathbf{x} = 0$ for every $i$. The rows span $\operatorname{Row} A$, so $\mathbf{x} \in (\operatorname{Row} A)^\perp$ by [[§50 Orthogonal Complements and Angles#^thm-50-1|Theorem §50.1]](1). Conversely, if $\mathbf{x} \in (\operatorname{Row} A)^\perp$, then $\mathbf{x}$ is orthogonal to each row, every entry of $A\mathbf{x}$ is $0$, and $\mathbf{x} \in \operatorname{Nul} A$. This proves $(\operatorname{Row} A)^\perp = \operatorname{Nul} A$.
>
> This holds for every matrix, in particular for $A^T$: $(\operatorname{Row} A^T)^\perp = \operatorname{Nul} A^T$. The rows of $A^T$ are the columns of $A$, so $\operatorname{Row} A^T = \operatorname{Col} A$, which gives the second statement.

^pf-50-2

*Uses:* [[§50 Orthogonal Complements and Angles#^thm-50-1|§50.1]], [[§5 The Matrix Equation Ax = b#^prop-5-4|§5.4]] (row–vector rule), [[§30 Null Spaces, Column Spaces, and Linear Transformations#^def-30-3|Def. §30.3]] (row space)

> [!remark]- Connections
> - Rigorous treatment: [[§23 Self-Adjoint and Normal Operators#^ladr-7-6|LADR 7.6]] ($\operatorname{null} T^* = (\operatorname{range} T)^\perp$ and $\operatorname{range} T^* = (\operatorname{null} T)^\perp$ for a linear map between inner product spaces; the transpose becomes the adjoint, and the row space is $\operatorname{range} T^*$). Orthogonal complements in general: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]], with $\dim U^\perp = \dim V - \dim U$ in [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-51|LADR 6.51]] and $(U^\perp)^\perp = U$ in [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-52|LADR 6.52]] ([[§50 Orthogonal Complements and Angles#^prop-50-3|Proposition §50.3]] and [[§50 Orthogonal Complements and Angles#^cor-50-4|Corollary §50.4]] below).
> - In a Hilbert space the orthogonal complement ([[§22 Projection and Orthogonal Decomposition#^def-22-1|556 Def. §22.1]]) of any set is a closed subspace, [[§22 Projection and Orthogonal Decomposition#^prop-22-3|556 Prop. §22.3]], and the double complement is the closed span, [[§22 Projection and Orthogonal Decomposition#^thm-22-6|556 Thm. §22.6]].

> [!theorem] Proposition §60.4: Dimension of the Orthogonal Complement
> If $W$ is a subspace of $\mathbb{R}^n$, then
>
> $$
> \dim W + \dim W^\perp = n .
> $$
>
> *Lay: 6.1, Practice Problem 3*

^prop-50-3

> [!proof]+ Proof
> If $W = \{\mathbf{0}\}$, then $W^\perp = \mathbb{R}^n$ and the formula reads $0 + n = n$. Otherwise let $\{\mathbf{b}_1, \ldots, \mathbf{b}_p\}$ be a basis of $W$, $1 \le p \le n$, and let $A$ be the $p \times n$ matrix with rows $\mathbf{b}_1^T, \ldots, \mathbf{b}_p^T$. Then $W = \operatorname{Row} A$, and by [[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]], $W^\perp = (\operatorname{Row} A)^\perp = \operatorname{Nul} A$. By the Rank Theorem,
>
> $$
> \dim W + \dim W^\perp = \dim \operatorname{Row} A + \dim \operatorname{Nul} A = \operatorname{rank} A + \dim \operatorname{Nul} A = n .
> $$

^pf-50-3

*Uses:* [[§50 Orthogonal Complements and Angles#^thm-50-2|§50.2]], [[§34 Rank#^thm-34-3|§34.3]] (the Rank Theorem)

> [!theorem] Corollary §60.3: The Double Complement
> If $W$ is a subspace of $\mathbb{R}^n$, then $(W^\perp)^\perp = W$. In particular, for an $m \times n$ matrix $A$,
>
> $$
> (\operatorname{Nul} A)^\perp = \operatorname{Row} A = \operatorname{Col} A^T \qquad\text{and}\qquad (\operatorname{Nul} A^T)^\perp = \operatorname{Col} A .
> $$
>
> The lecture stated the orthogonality theorem as $(\operatorname{Nul} A)^\perp = \operatorname{Row} A = \operatorname{Col} A^T$ together with $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$ ([[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]]).
>
> *Source: 235 lecture L22*

^cor-50-4

> [!proof]+ Proof
> Every $\mathbf{w} \in W$ is orthogonal to every vector of $W^\perp$, so $W \subseteq (W^\perp)^\perp$. By [[§50 Orthogonal Complements and Angles#^prop-50-3|Proposition §50.3]], applied to $W$ and then to $W^\perp$,
>
> $$
> \dim (W^\perp)^\perp = n - \dim W^\perp = n - (n - \dim W) = \dim W .
> $$
>
> A subspace of $(W^\perp)^\perp$ with the same dimension is all of it (a basis of $W$ is a linearly independent set of $\dim (W^\perp)^\perp$ vectors there, hence a basis, by the Basis Theorem; this is [[§33 The Dimension of a Vector Space#^cor-33-6|Corollary §33.6]]). So $W = (W^\perp)^\perp$. Taking complements in [[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]] gives $(\operatorname{Nul} A)^\perp = ((\operatorname{Row} A)^\perp)^\perp = \operatorname{Row} A$ and $(\operatorname{Nul} A^T)^\perp = \operatorname{Col} A$.

^pf-50-4

*Uses:* [[§50 Orthogonal Complements and Angles#^prop-50-3|§50.3]], [[§50 Orthogonal Complements and Angles#^thm-50-2|§50.2]], [[§33 The Dimension of a Vector Space#^thm-33-5|§33.5]] (the Basis Theorem), [[§33 The Dimension of a Vector Space#^cor-33-6|§33.6]]

![[m235-40-1.svg]]
*The four fundamental subspaces of an $m \times n$ matrix $A$. In $\mathbb{R}^n$, $\operatorname{Row} A$ and $\operatorname{Nul} A$ are orthogonal complements ([[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2]]); in $\mathbb{R}^m$, so are $\operatorname{Col} A$ and $\operatorname{Nul} A^T$. Their dimensions add up to $n$ and to $m$ ([[§50 Orthogonal Complements and Angles#^prop-50-3|Proposition §50.3]]): $\operatorname{rank} A + \dim \operatorname{Nul} A = n$ and $\operatorname{rank} A + \dim \operatorname{Nul} A^T = m$.*

> [!example] Example §60.1: A Plane and Its Normal Line
> **(a)** Let $W$ be a plane through the origin in $\mathbb{R}^3$ and $L$ the line through the origin perpendicular to $W$. For nonzero $\mathbf{z} \in L$ and $\mathbf{w} \in W$, the segments from $\mathbf{0}$ to $\mathbf{z}$ and to $\mathbf{w}$ are perpendicular, so $\mathbf{z} \cdot \mathbf{w} = 0$. In fact $L$ consists of *all* vectors orthogonal to $W$, and $W$ of all vectors orthogonal to $L$:
>
> $$
> L = W^\perp \qquad\text{and}\qquad W = L^\perp .
> $$
>
> **(b)** Concretely, let $W = \{\mathbf{x} \in \mathbb{R}^3 : x_1 + 2x_2 - x_3 = 0\}$, a plane through $\mathbf{0}$. With $\mathbf{v} = (1, 2, -1)$, the defining equation says $\mathbf{v} \cdot \mathbf{x} = 0$, so
>
> $$
> W = \{\mathbf{x} : \mathbf{v} \cdot \mathbf{x} = 0\} = \operatorname{Nul} \begin{bmatrix} 1 & 2 & -1 \end{bmatrix} = \operatorname{Span}\{\mathbf{v}\}^\perp .
> $$
>
> By [[§50 Orthogonal Complements and Angles#^cor-50-4|Corollary §50.4]], $W^\perp = (\operatorname{Span}\{\mathbf{v}\}^\perp)^\perp = \operatorname{Span}\{\mathbf{v}\}$: a vector $\mathbf{y}$ is orthogonal to $W$ if and only if $\mathbf{y} = \lambda\mathbf{v}$ for some scalar $\lambda$, that is, $\mathbf{y}$ is proportional to $(1, 2, -1)$. The dimensions agree with [[§50 Orthogonal Complements and Angles#^prop-50-3|Proposition §50.3]]: $2 + 1 = 3$.
>
> *Lay: Example 6.1.6*
> *Source: 235 lecture L22*

^ex-50-1

> [!example] Example §60.2: Testing Membership in an Orthogonal Complement
> Let $W \subseteq \mathbb{R}^4$ be the set of solutions of
>
> $$
> x_1 + x_2 + x_3 + x_4 = 0, \qquad x_2 + x_3 = 0,
> $$
>
> and $\mathbf{u} = (0, 1, 1, 0)$. Show that $\mathbf{u} \in W^\perp$.
>
> **Method 1: a spanning set.** By [[§50 Orthogonal Complements and Angles#^thm-50-1|Theorem §50.1]](1) it is enough to check $\mathbf{u}$ against a finite set spanning $W$. Solving the system ($x_3 = -x_2$ from the second equation, then $x_1 = -x_4$ from the first), $W$ is the $2$-dimensional plane
>
> $$
> W = \operatorname{Span}\{\mathbf{w}_1, \mathbf{w}_2\}, \qquad \mathbf{w}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ -1 \end{bmatrix}, \quad \mathbf{w}_2 = \begin{bmatrix} 0 \\ 1 \\ -1 \\ 0 \end{bmatrix} .
> $$
>
> Then $\mathbf{u} \cdot \mathbf{w}_1 = 0 + 0 + 0 + 0 = 0$ and $\mathbf{u} \cdot \mathbf{w}_2 = 0 + 1 - 1 + 0 = 0$. This suffices, because any $\mathbf{w} \in W$ is $a\mathbf{w}_1 + b\mathbf{w}_2$, and $\mathbf{w} \cdot \mathbf{u} = a(\mathbf{w}_1 \cdot \mathbf{u}) + b(\mathbf{w}_2 \cdot \mathbf{u}) = 0$.
>
> **Method 2: the row space.** $W = \operatorname{Nul} A$ for
>
> $$
> A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 0 \end{bmatrix}, \qquad\text{so}\qquad W^\perp = (\operatorname{Nul} A)^\perp = \operatorname{Row} A = \operatorname{Span}\{\mathbf{r}_1, \mathbf{r}_2\}
> $$
>
> by [[§50 Orthogonal Complements and Angles#^cor-50-4|Corollary §50.4]], where $\mathbf{r}_1 = (1, 1, 1, 1)$ and $\mathbf{r}_2 = (0, 1, 1, 0)$ are the rows. The question becomes whether $\mathbf{u} \in \operatorname{Span}\{\mathbf{r}_1, \mathbf{r}_2\}$, and here $\mathbf{u} = \mathbf{r}_2$. This is the quickest solution; it needs no basis of $W$.
>
> *Source: 235 lecture L22*

^ex-50-2

## Angles in ℝ² and ℝ³ (Optional)

> [!theorem] Theorem §50.5: The Inner Product and the Angle
> Let $\mathbf{u}$ and $\mathbf{v}$ be nonzero vectors in $\mathbb{R}^2$ or $\mathbb{R}^3$, and let $\vartheta$ be the angle between the line segments from the origin to the points $\mathbf{u}$ and $\mathbf{v}$. Then
>
> $$
> \mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\| \cos\vartheta .
> $$
>
> For $n > 3$ this formula is used to *define* the angle between two nonzero vectors of $\mathbb{R}^n$. (In statistics, $\cos\vartheta$ for suitable vectors $\mathbf{u}$, $\mathbf{v}$ is the correlation coefficient.)
>
> *Lay: 6.1, Equation (2)*

^thm-50-5

> [!proof]+ Proof
> The triangle with vertices $\mathbf{0}$, $\mathbf{u}$, $\mathbf{v}$ has sides of lengths $\|\mathbf{u}\|$, $\|\mathbf{v}\|$, $\|\mathbf{u} - \mathbf{v}\|$, and its angle at $\mathbf{0}$ is $\vartheta$. The law of cosines ([[§142 Trigonometry#^thm-142-6|Calc Thm. §142.6]]) gives
>
> $$
> \|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\,\|\mathbf{v}\| \cos\vartheta .
> $$
>
> Solving for the last term, for $\mathbf{u} = (u_1, u_2)$, $\mathbf{v} = (v_1, v_2)$:
>
> $$
> \begin{aligned}
> \|\mathbf{u}\|\,\|\mathbf{v}\| \cos\vartheta &= \tfrac12\big[\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - \|\mathbf{u} - \mathbf{v}\|^2\big] \\
> &= \tfrac12\big[u_1^2 + u_2^2 + v_1^2 + v_2^2 - (u_1 - v_1)^2 - (u_2 - v_2)^2\big] \\
> &= \tfrac12\big[2u_1v_1 + 2u_2v_2\big] = u_1v_1 + u_2v_2 = \mathbf{u} \cdot \mathbf{v} .
> \end{aligned}
> $$
>
> In $\mathbb{R}^3$ the three points $\mathbf{0}$, $\mathbf{u}$, $\mathbf{v}$ still span a triangle in a plane, the law of cosines applies to it, and the same computation with a third coordinate gives $u_1v_1 + u_2v_2 + u_3v_3$. (If $\mathbf{u}$ and $\mathbf{v}$ lie on one line, the triangle is degenerate, $\vartheta = 0$ or $\pi$, and the formula is checked directly from $\mathbf{v} = c\mathbf{u}$.) Equivalently, the middle line is [[§49 Inner Product, Length, and Orthogonality#^prop-49-3|Proposition §49.3]].

^pf-50-5

*Uses:* [[§49 Inner Product, Length, and Orthogonality#^prop-49-3|§49.3]], [[§49 Inner Product, Length, and Orthogonality#^def-49-4|Def. §49.4]], [[§142 Trigonometry#^thm-142-6|Calc Thm. §142.6]] (law of cosines)

> [!remark]- Connections
> - Stewart proves the same formula for vectors in $\mathbb{R}^2$ and $\mathbb{R}^3$, also from the law of cosines: [[§95 The Dot Product#^thm-95-2|Calc Thm. §95.2]]; orthogonality test [[§95 The Dot Product#^thm-95-4|Calc Thm. §95.4]].
> - For $n > 3$ the definition of the angle needs $|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\|\,\|\mathbf{v}\|$ first: the Cauchy–Schwarz inequality, [[§20 Inner Products and Norms#^ladr-6-14|LADR 6.14]], proved here in [[§56 Inner Product Spaces#^thm-56-4|Theorem §56.4]].

> [!remark] Remark: The Cauchy Inequality
> Since $|\cos\vartheta| \le 1$, the angle formula gives $|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\|\,\|\mathbf{v}\|$, that is,
>
> $$
> (u_1v_1 + \cdots + u_nv_n)^2 \le (u_1^2 + \cdots + u_n^2)(v_1^2 + \cdots + v_n^2) .
> $$
>
> This is the Cauchy inequality. As an argument it only works for $n \le 3$, where the angle exists geometrically. For $n > 3$ the angle is *defined* by $\cos\vartheta = \mathbf{u} \cdot \mathbf{v} / (\|\mathbf{u}\|\,\|\mathbf{v}\|)$, and that definition makes sense only once the inequality is known. A proof that works in $\mathbb{R}^n$, and in every inner product space, is [[§56 Inner Product Spaces#^thm-56-4|Theorem §56.4]] (Cauchy–Schwarz).
>
> *Source: 235 lecture L22*

^rem-50-2
