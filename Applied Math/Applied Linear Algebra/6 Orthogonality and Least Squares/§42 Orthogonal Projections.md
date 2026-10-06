---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 6
section: 42
lay: "6.3"
aliases: ["Lay 6.3"]
tags: [applied-linear-algebra, math235]
---
← [[§41 Orthogonal Sets]] · ↑ [[· 6 Orthogonality and Least Squares]] · [[§43 The Gram–Schmidt Process]] →

*Lay, Section 6.3.*

The projection of a vector onto a line ([[§41 Orthogonal Sets#^def-41-3|Definition §41.3]]) has an analogue for every subspace $W$ of $\mathbb{R}^n$. Each $\mathbf{y}$ splits uniquely as $\hat{\mathbf{y}} + \mathbf{z}$ with $\hat{\mathbf{y}} \in W$ and $\mathbf{z} \in W^\perp$, and $\hat{\mathbf{y}} = \operatorname{proj}_W \mathbf{y}$ is computed from any orthogonal basis of $W$ as a sum of projections onto lines. The second main theorem says that $\hat{\mathbf{y}}$ is the point of $W$ closest to $\mathbf{y}$. With $W = \operatorname{Col} A$, these two properties solve the least-squares problem of [[§44 Least-Squares Problems|§44]].

> [!example] Example §42.1: Splitting a Vector Along an Orthogonal Basis
> Let $\{\mathbf{u}_1, \ldots, \mathbf{u}_5\}$ be an orthogonal basis of $\mathbb{R}^5$, $\mathbf{y} = c_1\mathbf{u}_1 + \cdots + c_5\mathbf{u}_5$, and $W = \operatorname{Span}\{\mathbf{u}_1, \mathbf{u}_2\}$. Write $\mathbf{y}$ as a sum of a vector $\mathbf{z}_1 \in W$ and a vector $\mathbf{z}_2 \in W^\perp$.
>
> Group the terms:
>
> $$
> \mathbf{y} = \underbrace{c_1\mathbf{u}_1 + c_2\mathbf{u}_2}_{\mathbf{z}_1} + \underbrace{c_3\mathbf{u}_3 + c_4\mathbf{u}_4 + c_5\mathbf{u}_5}_{\mathbf{z}_2} .
> $$
>
> Clearly $\mathbf{z}_1 \in W$. To show $\mathbf{z}_2 \in W^\perp$ it suffices to check it against the spanning set $\{\mathbf{u}_1, \mathbf{u}_2\}$ ([[§40 Inner Product, Length, and Orthogonality#^thm-40-5|Theorem §40.5]](1)):
>
> $$
> \mathbf{z}_2 \cdot \mathbf{u}_1 = c_3(\mathbf{u}_3 \cdot \mathbf{u}_1) + c_4(\mathbf{u}_4 \cdot \mathbf{u}_1) + c_5(\mathbf{u}_5 \cdot \mathbf{u}_1) = 0,
> $$
>
> since $\mathbf{u}_1$ is orthogonal to $\mathbf{u}_3, \mathbf{u}_4, \mathbf{u}_5$; likewise $\mathbf{z}_2 \cdot \mathbf{u}_2 = 0$. The next theorem produces the same splitting from an orthogonal basis of $W$ alone.
>
> *Lay: Example 6.3.1*

^ex-42-1

## The Orthogonal Decomposition Theorem

> [!theorem] Theorem §42.1: The Orthogonal Decomposition Theorem
> Let $W$ be a subspace of $\mathbb{R}^n$. Then each $\mathbf{y}$ in $\mathbb{R}^n$ can be written uniquely in the form
>
> $$
> \mathbf{y} = \hat{\mathbf{y}} + \mathbf{z} \tag{1}
> $$
>
> where $\hat{\mathbf{y}}$ is in $W$ and $\mathbf{z}$ is in $W^\perp$. In fact, if $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is any orthogonal basis of $W$, then
>
> $$
> \hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1}\mathbf{u}_1 + \cdots + \frac{\mathbf{y} \cdot \mathbf{u}_p}{\mathbf{u}_p \cdot \mathbf{u}_p}\mathbf{u}_p \tag{2}
> $$
>
> and $\mathbf{z} = \mathbf{y} - \hat{\mathbf{y}}$.
>
> *Lay: Theorem 8 (6.3)*

^thm-42-1

> [!proof]+ Proof
> If $W = \{\mathbf{0}\}$, then $W^\perp = \mathbb{R}^n$ and (1) is simply $\mathbf{y} = \mathbf{0} + \mathbf{y}$, which is the only possibility. So let $W \ne \{\mathbf{0}\}$; it has an orthogonal basis by [[§43 The Gram–Schmidt Process#^cor-43-2|Corollary §43.2]] (whose proof uses this theorem only for subspaces that already have an orthogonal basis, so there is no circularity).
>
> **Existence.** Let $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ be any orthogonal basis of $W$ and define $\hat{\mathbf{y}}$ by (2). It is a linear combination of $\mathbf{u}_1, \ldots, \mathbf{u}_p$, so $\hat{\mathbf{y}} \in W$. Let $\mathbf{z} = \mathbf{y} - \hat{\mathbf{y}}$. Since $\mathbf{u}_1$ is orthogonal to $\mathbf{u}_2, \ldots, \mathbf{u}_p$,
>
> $$
> \mathbf{z} \cdot \mathbf{u}_1 = \mathbf{y} \cdot \mathbf{u}_1 - \Big(\frac{\mathbf{y} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1}\Big)\mathbf{u}_1 \cdot \mathbf{u}_1 - 0 - \cdots - 0 = \mathbf{y} \cdot \mathbf{u}_1 - \mathbf{y} \cdot \mathbf{u}_1 = 0 .
> $$
>
> In the same way $\mathbf{z} \cdot \mathbf{u}_j = 0$ for every $j$. So $\mathbf{z}$ is orthogonal to a spanning set of $W$, hence $\mathbf{z} \in W^\perp$ ([[§40 Inner Product, Length, and Orthogonality#^thm-40-5|Theorem §40.5]](1)).
>
> **Uniqueness.** Suppose also $\mathbf{y} = \hat{\mathbf{y}}_1 + \mathbf{z}_1$ with $\hat{\mathbf{y}}_1 \in W$ and $\mathbf{z}_1 \in W^\perp$. Then $\hat{\mathbf{y}} + \mathbf{z} = \hat{\mathbf{y}}_1 + \mathbf{z}_1$, so
>
> $$
> \mathbf{v} = \hat{\mathbf{y}} - \hat{\mathbf{y}}_1 = \mathbf{z}_1 - \mathbf{z} .
> $$
>
> The left side is in $W$, and the right side is in $W^\perp$ because $W^\perp$ is a subspace. So $\mathbf{v} \in W \cap W^\perp$, hence $\mathbf{v} \cdot \mathbf{v} = 0$ and $\mathbf{v} = \mathbf{0}$ ([[§40 Inner Product, Length, and Orthogonality#^thm-40-5|Theorem §40.5]](3)). Thus $\hat{\mathbf{y}} = \hat{\mathbf{y}}_1$ and $\mathbf{z} = \mathbf{z}_1$.

^pf-42-1

*Uses:* [[§40 Inner Product, Length, and Orthogonality#^thm-40-1|§40.1]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-5|§40.5]], [[§43 The Gram–Schmidt Process#^cor-43-2|§43.2]]

> [!definition] Definition §42.1: Orthogonal Projection onto a Subspace
> The vector $\hat{\mathbf{y}}$ in (1) is the **orthogonal projection of $\mathbf{y}$ onto $W$**, written $\operatorname{proj}_W \mathbf{y}$. By the uniqueness in Theorem §42.1 it depends only on $W$, not on the orthogonal basis used in (2). When $W$ is one-dimensional, (2) has one term and agrees with [[§41 Orthogonal Sets#^def-41-3|Definition §41.3]].
>
> *Lay: 6.3 (text)*

^def-42-1

> [!remark]- Connections
> - Rigorous treatment: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]] ($V = U \oplus U^\perp$ for finite-dimensional $U$; $V$ itself may be infinite-dimensional) and the projection $P_U$ of [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-55|LADR 6.55]]; Axler proves existence from an orthonormal basis of $U$, exactly as here.
> - In a Hilbert space the decomposition holds for every *closed* subspace, proved by the closest-point theorem instead of a basis: [[§22 Projection and Orthogonal Decomposition#^thm-22-4|556 Thm. §22.4]].

> [!example] Example §42.2: Decomposing a Vector in ℝ³
> Let
>
> $$
> \mathbf{u}_1 = \begin{bmatrix} 2 \\ 5 \\ -1 \end{bmatrix}, \qquad \mathbf{u}_2 = \begin{bmatrix} -2 \\ 1 \\ 1 \end{bmatrix}, \qquad \mathbf{y} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} .
> $$
>
> Then $\mathbf{u}_1 \cdot \mathbf{u}_2 = -4 + 5 - 1 = 0$, so $\{\mathbf{u}_1, \mathbf{u}_2\}$ is an orthogonal basis of $W = \operatorname{Span}\{\mathbf{u}_1, \mathbf{u}_2\}$. Write $\mathbf{y}$ as a vector in $W$ plus a vector orthogonal to $W$, and find the point of $W$ closest to $\mathbf{y}$.
>
> $\mathbf{y} \cdot \mathbf{u}_1 = 2 + 10 - 3 = 9$, $\mathbf{u}_1 \cdot \mathbf{u}_1 = 4 + 25 + 1 = 30$, $\mathbf{y} \cdot \mathbf{u}_2 = -2 + 2 + 3 = 3$, $\mathbf{u}_2 \cdot \mathbf{u}_2 = 4 + 1 + 1 = 6$. By (2),
>
> $$
> \hat{\mathbf{y}} = \frac{9}{30}\begin{bmatrix} 2 \\ 5 \\ -1 \end{bmatrix} + \frac{3}{6}\begin{bmatrix} -2 \\ 1 \\ 1 \end{bmatrix} = \frac{9}{30}\begin{bmatrix} 2 \\ 5 \\ -1 \end{bmatrix} + \frac{15}{30}\begin{bmatrix} -2 \\ 1 \\ 1 \end{bmatrix} = \frac{1}{30}\begin{bmatrix} 18 - 30 \\ 45 + 15 \\ -9 + 15 \end{bmatrix} = \begin{bmatrix} -2/5 \\ 2 \\ 1/5 \end{bmatrix},
> $$
>
> $$
> \mathbf{y} - \hat{\mathbf{y}} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} - \begin{bmatrix} -2/5 \\ 2 \\ 1/5 \end{bmatrix} = \begin{bmatrix} 7/5 \\ 0 \\ 14/5 \end{bmatrix} .
> $$
>
> Theorem §42.1 guarantees $\mathbf{y} - \hat{\mathbf{y}} \in W^\perp$; as a check on the arithmetic, $(\mathbf{y} - \hat{\mathbf{y}}) \cdot \mathbf{u}_1 = \frac{14}{5} + 0 - \frac{14}{5} = 0$ and $(\mathbf{y} - \hat{\mathbf{y}}) \cdot \mathbf{u}_2 = -\frac{14}{5} + 0 + \frac{14}{5} = 0$. The decomposition is
>
> $$
> \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} = \begin{bmatrix} -2/5 \\ 2 \\ 1/5 \end{bmatrix} + \begin{bmatrix} 7/5 \\ 0 \\ 14/5 \end{bmatrix},
> $$
>
> and by the Best Approximation Theorem (Theorem §42.3 below) $\hat{\mathbf{y}} = (-\frac25, 2, \frac15)$ is the point of $W$ closest to $\mathbf{y}$.
>
> *Lay: Examples 6.3.2 and 6.3.3*

^ex-42-2

> [!remark] Remark: A Geometric Interpretation of the Orthogonal Projection
> Each term $\frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}\mathbf{u}_j$ of (2) is the projection $\hat{\mathbf{y}}_j$ of $\mathbf{y}$ onto the line spanned by $\mathbf{u}_j$. So $\operatorname{proj}_W \mathbf{y} = \hat{\mathbf{y}}_1 + \cdots + \hat{\mathbf{y}}_p$ is the sum of the projections of $\mathbf{y}$ onto mutually orthogonal lines in $W$. This is [[§41 Orthogonal Sets#^rem-41-1|the picture behind Theorem §41.2]], except that now $\mathbf{y}$ need not lie in $W$: it is $\hat{\mathbf{y}}$ that is rebuilt from its projections. The formula needs an *orthogonal* basis. For a basis that is not orthogonal, the sum of the projections onto the basis lines is in general not $\operatorname{proj}_W \mathbf{y}$.

^rem-42-1

## Properties of Orthogonal Projections

> [!theorem] Proposition §42.2: Projecting a Vector Already in W
> If $\mathbf{y}$ is in $W = \operatorname{Span}\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$, then $\operatorname{proj}_W \mathbf{y} = \mathbf{y}$.
>
> *Lay: 6.3 (boxed fact)*

^prop-42-2

> [!proof]+ Proof
> $\mathbf{y} = \mathbf{y} + \mathbf{0}$ is a decomposition with $\mathbf{y} \in W$ and $\mathbf{0} \in W^\perp$. By the uniqueness in Theorem §42.1, $\operatorname{proj}_W \mathbf{y} = \mathbf{y}$. (Equivalently: for an orthogonal basis $\{\mathbf{u}_j\}$ of $W$, formula (2) is exactly the expansion of $\mathbf{y}$ in [[§41 Orthogonal Sets#^thm-41-2|Theorem §41.2]].)

^pf-42-2

*Uses:* [[§42 Orthogonal Projections#^thm-42-1|§42.1]], [[§41 Orthogonal Sets#^thm-41-2|§41.2]]

> [!example] Example §42.3: A Projection That Returns the Vector
> Let $\mathbf{u}_1 = (-7, 1, 4)$, $\mathbf{u}_2 = (-1, 1, -2)$, $\mathbf{y} = (-9, 1, 6)$ and $W = \operatorname{Span}\{\mathbf{u}_1, \mathbf{u}_2\}$. Since $\mathbf{u}_1 \cdot \mathbf{u}_2 = 7 + 1 - 8 = 0$, formula (2) applies:
>
> $$
> \mathbf{y} \cdot \mathbf{u}_1 = 63 + 1 + 24 = 88, \quad \mathbf{u}_1 \cdot \mathbf{u}_1 = 49 + 1 + 16 = 66, \quad \mathbf{y} \cdot \mathbf{u}_2 = 9 + 1 - 12 = -2, \quad \mathbf{u}_2 \cdot \mathbf{u}_2 = 6,
> $$
>
> $$
> \operatorname{proj}_W \mathbf{y} = \frac{88}{66}\mathbf{u}_1 - \frac{2}{6}\mathbf{u}_2 = \frac43\begin{bmatrix} -7 \\ 1 \\ 4 \end{bmatrix} - \frac13\begin{bmatrix} -1 \\ 1 \\ -2 \end{bmatrix} = \frac13\begin{bmatrix} -28 + 1 \\ 4 - 1 \\ 16 + 2 \end{bmatrix} = \begin{bmatrix} -9 \\ 1 \\ 6 \end{bmatrix} = \mathbf{y} .
> $$
>
> So $\mathbf{y}$ happens to be the combination $\frac43\mathbf{u}_1 - \frac13\mathbf{u}_2$ of the basis, $\mathbf{y} \in W$, and the closest point of $W$ to $\mathbf{y}$ is $\mathbf{y}$ itself (Proposition §42.2).
>
> *Lay: 6.3, Practice Problem 1*

^ex-42-3

> [!theorem] Theorem §42.3: The Best Approximation Theorem
> Let $W$ be a subspace of $\mathbb{R}^n$, $\mathbf{y}$ any vector in $\mathbb{R}^n$, and $\hat{\mathbf{y}}$ the orthogonal projection of $\mathbf{y}$ onto $W$. Then $\hat{\mathbf{y}}$ is the closest point in $W$ to $\mathbf{y}$, in the sense that
>
> $$
> \|\mathbf{y} - \hat{\mathbf{y}}\| < \|\mathbf{y} - \mathbf{v}\| \tag{3}
> $$
>
> for all $\mathbf{v}$ in $W$ distinct from $\hat{\mathbf{y}}$.
>
> *Lay: Theorem 9 (6.3)*

^thm-42-3

> [!proof]+ Proof
> Let $\mathbf{v} \in W$, $\mathbf{v} \ne \hat{\mathbf{y}}$. Then $\hat{\mathbf{y}} - \mathbf{v} \in W$. By the Orthogonal Decomposition Theorem, $\mathbf{y} - \hat{\mathbf{y}} \in W^\perp$, so in particular $\mathbf{y} - \hat{\mathbf{y}}$ is orthogonal to $\hat{\mathbf{y}} - \mathbf{v}$. Since
>
> $$
> \mathbf{y} - \mathbf{v} = (\mathbf{y} - \hat{\mathbf{y}}) + (\hat{\mathbf{y}} - \mathbf{v}),
> $$
>
> the Pythagorean Theorem ([[§40 Inner Product, Length, and Orthogonality#^thm-40-4|Theorem §40.4]]) gives
>
> $$
> \|\mathbf{y} - \mathbf{v}\|^2 = \|\mathbf{y} - \hat{\mathbf{y}}\|^2 + \|\hat{\mathbf{y}} - \mathbf{v}\|^2 .
> $$
>
> Now $\|\hat{\mathbf{y}} - \mathbf{v}\|^2 > 0$ because $\hat{\mathbf{y}} - \mathbf{v} \ne \mathbf{0}$, so $\|\mathbf{y} - \mathbf{v}\|^2 > \|\mathbf{y} - \hat{\mathbf{y}}\|^2$, and (3) follows by taking square roots.

^pf-42-3

*Uses:* [[§42 Orthogonal Projections#^thm-42-1|§42.1]], [[§40 Inner Product, Length, and Orthogonality#^thm-40-4|§40.4]]

![[m235-42-1.svg]]
*The orthogonal projection $\hat{\mathbf{y}} = \operatorname{proj}_W \mathbf{y}$ onto a plane $W$ through $\mathbf{0}$. The component $\mathbf{z} = \mathbf{y} - \hat{\mathbf{y}}$ (red) is orthogonal to $W$ (Theorem §42.1). For any other $\mathbf{v} \in W$, the triangle $\mathbf{y}, \hat{\mathbf{y}}, \mathbf{v}$ has a right angle at $\hat{\mathbf{y}}$, so its hypotenuse $\|\mathbf{y} - \mathbf{v}\|$ is longer than the leg $\|\mathbf{y} - \hat{\mathbf{y}}\|$ (Theorem §42.3).*

> [!definition] Definition §42.2: Best Approximation; Distance to a Subspace
> The vector $\hat{\mathbf{y}} = \operatorname{proj}_W \mathbf{y}$ is called the **best approximation to $\mathbf{y}$ by elements of $W$**. The **distance from a point $\mathbf{y}$ in $\mathbb{R}^n$ to a subspace $W$** is the distance from $\mathbf{y}$ to the nearest point in $W$; by Theorem §42.3 it equals $\|\mathbf{y} - \operatorname{proj}_W \mathbf{y}\|$.
>
> Thinking of $\|\mathbf{y} - \mathbf{v}\|$ as the "error" of using $\mathbf{v}$ in place of $\mathbf{y}$, Theorem §42.3 says that the error is smallest exactly for $\mathbf{v} = \hat{\mathbf{y}}$. This also gives a second proof that $\hat{\mathbf{y}}$ does not depend on the orthogonal basis used to compute it: whichever basis is used, the result is the unique closest point of $W$ to $\mathbf{y}$.
>
> *Lay: 6.3 (text); Example 6.3.4*

^def-42-2

> [!remark]- Connections
> - Rigorous treatment: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]] ($\|v - P_Uv\| \le \|v - u\|$, with equality only for $u = P_Uv$; same Pythagorean proof).
> - For a closed convex set in a Hilbert space, a closest point exists and is unique without any basis, [[§22 Projection and Orthogonal Decomposition#^thm-22-2|556 Thm. §22.2]]; for a closed subspace it is characterized by $\mathbf{y} - \hat{\mathbf{y}} \perp W$, as here.
> - Fourier version: for the integral inner product of [[§46 Inner Product Spaces|§46]], the truncated Fourier series is the best mean-square approximation by [[§47 Applications of Inner Product Spaces#^def-47-3|trigonometric polynomials]], [[§11★ Mean Error and Convergence in Mean#^thm-11-2|341 Thm. §11.2]].

> [!example] Example §42.4: The Distance from a Point to a Plane
> Find the distance from $\mathbf{y}$ to $W = \operatorname{Span}\{\mathbf{u}_1, \mathbf{u}_2\}$, where
>
> $$
> \mathbf{y} = \begin{bmatrix} -1 \\ -5 \\ 10 \end{bmatrix}, \qquad \mathbf{u}_1 = \begin{bmatrix} 5 \\ -2 \\ 1 \end{bmatrix}, \qquad \mathbf{u}_2 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} .
> $$
>
> $\mathbf{u}_1 \cdot \mathbf{u}_2 = 5 - 4 - 1 = 0$, so $\{\mathbf{u}_1, \mathbf{u}_2\}$ is an orthogonal basis of $W$. Next $\mathbf{y} \cdot \mathbf{u}_1 = -5 + 10 + 10 = 15$, $\mathbf{u}_1 \cdot \mathbf{u}_1 = 25 + 4 + 1 = 30$, $\mathbf{y} \cdot \mathbf{u}_2 = -1 - 10 - 10 = -21$, $\mathbf{u}_2 \cdot \mathbf{u}_2 = 6$. So
>
> $$
> \hat{\mathbf{y}} = \frac{15}{30}\mathbf{u}_1 + \frac{-21}{6}\mathbf{u}_2 = \frac12\begin{bmatrix} 5 \\ -2 \\ 1 \end{bmatrix} - \frac72\begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} = \begin{bmatrix} -1 \\ -8 \\ 4 \end{bmatrix}, \qquad
> \mathbf{y} - \hat{\mathbf{y}} = \begin{bmatrix} -1 \\ -5 \\ 10 \end{bmatrix} - \begin{bmatrix} -1 \\ -8 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \\ 6 \end{bmatrix} .
> $$
>
> By Theorem §42.3 the distance is $\|\mathbf{y} - \hat{\mathbf{y}}\| = \sqrt{0 + 9 + 36} = \sqrt{45} = 3\sqrt5$.
>
> *Lay: Example 6.3.4*

^ex-42-4

> [!theorem] Theorem §42.4: Projection with an Orthonormal Basis
> If $\{\mathbf{u}_1, \ldots, \mathbf{u}_p\}$ is an orthonormal basis for a subspace $W$ of $\mathbb{R}^n$, then
>
> $$
> \operatorname{proj}_W \mathbf{y} = (\mathbf{y} \cdot \mathbf{u}_1)\mathbf{u}_1 + (\mathbf{y} \cdot \mathbf{u}_2)\mathbf{u}_2 + \cdots + (\mathbf{y} \cdot \mathbf{u}_p)\mathbf{u}_p . \tag{4}
> $$
>
> If $U = [\,\mathbf{u}_1\ \mathbf{u}_2\ \cdots\ \mathbf{u}_p\,]$, then
>
> $$
> \operatorname{proj}_W \mathbf{y} = UU^T\mathbf{y} \qquad\text{for all } \mathbf{y} \text{ in } \mathbb{R}^n . \tag{5}
> $$
>
> *Lay: Theorem 10 (6.3)*

^thm-42-4

> [!proof]+ Proof
> In (2) every denominator is $\mathbf{u}_j \cdot \mathbf{u}_j = 1$, which gives (4). By (4), $\operatorname{proj}_W \mathbf{y}$ is the linear combination of the columns of $U$ with weights $\mathbf{y} \cdot \mathbf{u}_1, \ldots, \mathbf{y} \cdot \mathbf{u}_p$. These weights are $\mathbf{u}_1^T\mathbf{y}, \ldots, \mathbf{u}_p^T\mathbf{y}$, the entries of $U^T\mathbf{y}$ (the rows of $U^T$ are the $\mathbf{u}_j^T$). A linear combination of the columns of $U$ with weight vector $U^T\mathbf{y}$ is $U(U^T\mathbf{y})$, which is (5).

^pf-42-4

*Uses:* [[§42 Orthogonal Projections#^thm-42-1|§42.1]], [[§4 The Matrix Equation Ax = b#^def-4-1|Def. §4.1]] ($A\mathbf{x}$ as a combination of columns)

> [!remark] Remark: The Matrices UᵀU and UUᵀ
> Let $U$ be an $n \times p$ matrix with orthonormal columns and $W = \operatorname{Col} U$. Then
>
> $$
> U^TU\mathbf{x} = I_p\mathbf{x} = \mathbf{x} \ \text{ for all } \mathbf{x} \in \mathbb{R}^p \quad \text{(Theorem §41.4)}, \qquad
> UU^T\mathbf{y} = \operatorname{proj}_W \mathbf{y} \ \text{ for all } \mathbf{y} \in \mathbb{R}^n \quad \text{(Theorem §42.4)} .
> $$
>
> The $n \times n$ matrix $UU^T$ is the identity only when $p = n$: then $U$ is an orthogonal matrix, $W = \mathbb{R}^n$, and $UU^T\mathbf{y} = \mathbf{y}$. Formula (5) also shows that $\mathbf{y} \mapsto \operatorname{proj}_W \mathbf{y}$ is a linear transformation: $\operatorname{proj}_W(\mathbf{x} + \mathbf{y}) = UU^T\mathbf{x} + UU^T\mathbf{y} = \operatorname{proj}_W \mathbf{x} + \operatorname{proj}_W \mathbf{y}$ (Lay's Practice Problem 2), and similarly for scalar multiples. Formula (4) is important in theory, but its unit vectors usually carry square roots; for hand calculations Lay recommends formula (2) with an orthogonal basis.

^rem-42-2

> [!remark]- Connections
> - Rigorous treatment: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-57|LADR 6.57]] (properties of $P_U$: linear, $P_U^2 = P_U$, range $U$, null space $U^\perp$, and formula (i) $P_Uv = \langle v, e_1\rangle e_1 + \cdots + \langle v, e_m\rangle e_m$).
