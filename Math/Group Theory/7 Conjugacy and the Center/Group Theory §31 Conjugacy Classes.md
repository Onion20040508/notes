---
type: section
subject: "[[Group Theory]]"
chapter: 7
section: 31
tags: [group-theory, math493]
---
← [[Group Theory §30 Examples꞉ Linear Groups and the Cube]] · ↑ [[Group Theory — 7 Conjugacy and the Center]] · [[Group Theory §32 Conjugation as an Action and the Class Equation]] →

*Reference: Pinter Ch. 13, Ex. I.*

> [!definition] Definition §31.1: Conjugacy Class
> For $g \in G$, the **conjugacy class** of $g$ is the set
>
> $$
> \operatorname{Conj}(g) := \{ h g h^{-1} : h \in G \},
> $$
>
> the set of all conjugates of $g$ ([[Group Theory §18 Conjugation, Products, and Pointwise Products#^def-18-2|Def. §18.2]]: $hgh^{-1} = c_h(g)$).
>
> *Source: WS 3*

^def-31-1

> [!remark]- Connections
> - Normal subgroups are exactly the subgroups that are unions of classes: [[Group Theory §36 Sources of Normal Subgroups#^prop-36-7|§36.7]]; characters are constant on classes: [[Group Theory §40 Characters#^prop-40-1|§40.1]].

> [!theorem] Proposition §31.1: Conjugacy Class of $(1\,2)$ in $S_n$
> Let $n \geq 2$, and let $(1\,2) \in S_n$ be the permutation $1 \mapsto 2$, $2 \mapsto 1$, $j \mapsto j$ for $j \geq 3$. The conjugacy class of $(1\,2)$ in $S_n$ is the set of all transpositions:
>
> $$
> \operatorname{Conj}\big((1\,2)\big) = \{ (i\ j) : 1 \leq i < j \leq n \},
> $$
>
> a set of $\binom{n}{2}$ elements.
>
> *Source: WS 3.2*

^prop-31-1

> [!proof]+ Proof
> By [[Group Theory §12 Multiplying and Conjugating Cycles#^prop-12-1|Conjugation Relabels a Cycle, §12.1]], for any $\tau \in S_n$,
>
> $$
> \tau\,(1\,2)\,\tau^{-1} = \big(\tau(1)\ \ \tau(2)\big),
> $$
>
> a transposition. So every conjugate of $(1\,2)$ is a transposition. Conversely, given a transposition $(i\ j)$, choose any $\tau \in S_n$ with $\tau(1) = i$ and $\tau(2) = j$ (possible since $i \neq j$; e.g. extend arbitrarily to a bijection); then $\tau(1\,2)\tau^{-1} = (i\ j)$. Hence $\operatorname{Conj}((1\,2))$ is exactly the set of transpositions, of which there are $\binom{n}{2}$, one for each $2$-element subset of $\{1, \ldots, n\}$.

^pf-31-1

*Uses:* [[Group Theory §31 Conjugacy Classes#^def-31-1|Def. §31.1]], [[Group Theory §12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]]

> [!definition] Definition §31.2: Cycle Type
> Let $\sigma \in S_n$ have disjoint-cycle decomposition $\sigma = c_1 c_2 \cdots c_k$, where every element of $\{1, \ldots, n\}$ occurs in exactly one $c_i$ (so fixed points are written as $1$-cycles), and let $r_i$ be the length of $c_i$, indexed so that $r_1 \geq r_2 \geq \cdots \geq r_k$. The **cycle type** of $\sigma$ is the sequence
>
> $$
> \lambda(\sigma) = (r_1, r_2, \ldots, r_k), \qquad r_1 + r_2 + \cdots + r_k = n,
> $$
>
> a **partition** of $n$. For example, in $S_5$: $\lambda\big((1\,2\,3)(4\,5)\big) = (3, 2)$; $\lambda\big((1\,2)(3)(4)(5)\big) = (2,1,1,1)$, usually abbreviated $2\,1^3$; $\lambda(e) = (1,1,1,1,1) = 1^5$.

^def-31-2

> [!theorem] Theorem §31.2: Conjugacy Classes in $S_n$ Are Cycle Types
> For $\sigma, \sigma' \in S_n$: $\sigma$ and $\sigma'$ are conjugate in $S_n$ if and only if $\lambda(\sigma) = \lambda(\sigma')$. Hence the conjugacy classes of $S_n$ are in bijection with the partitions of $n$.

^thm-31-2

> [!proof]+ Proof
> ($\Rightarrow$) Let $\sigma = c_1 c_2 \cdots c_k$ with disjoint cycles $c_i = (a_{i,1}\ a_{i,2}\ \cdots\ a_{i,r_i})$, and let $\tau \in S_n$. Conjugating the product factor by factor,
>
> $$
> \tau \sigma \tau^{-1} = \tau c_1 c_2 \cdots c_k \tau^{-1} = (\tau c_1 \tau^{-1})(\tau c_2 \tau^{-1}) \cdots (\tau c_k \tau^{-1}),
> $$
>
> since the $\tau^{-1}\tau$ inserted between consecutive factors cancels. By [[Group Theory §12 Multiplying and Conjugating Cycles#^prop-12-1|Conjugation Relabels a Cycle, §12.1]],
>
> $$
> \tau c_i \tau^{-1} = \tau\,(a_{i,1}\ a_{i,2}\ \cdots\ a_{i,r_i})\,\tau^{-1} = \big(\tau(a_{i,1})\ \tau(a_{i,2})\ \cdots\ \tau(a_{i,r_i})\big),
> $$
>
> a cycle of the same length $r_i$. These relabeled cycles are again pairwise disjoint: the entries of $\tau c_i \tau^{-1}$ are $\tau(\{a_{i,1}, \ldots, a_{i,r_i}\})$, and $\tau$ is injective, so distinct $i$ give disjoint sets. Hence $\tau\sigma\tau^{-1}$ has cycle lengths $r_1, \ldots, r_k$, i.e. $\lambda(\tau\sigma\tau^{-1}) = \lambda(\sigma)$.
>
> ($\Leftarrow$) Suppose $\lambda(\sigma) = \lambda(\sigma') = (r_1, \ldots, r_k)$. Write both decompositions with their cycles in the same length order:
>
> $$
> \sigma = (a_{1,1}\ \cdots\ a_{1,r_1})(a_{2,1}\ \cdots\ a_{2,r_2}) \cdots (a_{k,1}\ \cdots\ a_{k,r_k}),
> $$
>
> $$
> \sigma' = (b_{1,1}\ \cdots\ b_{1,r_1})(b_{2,1}\ \cdots\ b_{2,r_2}) \cdots (b_{k,1}\ \cdots\ b_{k,r_k}).
> $$
>
> Since the cycles of each decomposition are disjoint and together use every element once, the list $a_{1,1}, \ldots, a_{1,r_1}, a_{2,1}, \ldots, a_{k,r_k}$ is an enumeration of $\{1, \ldots, n\}$ without repetition, and likewise for the $b$'s. Define $\tau \in S_n$ by
>
> $$
> \tau(a_{i,j}) = b_{i,j} \qquad (1 \leq i \leq k,\ 1 \leq j \leq r_i);
> $$
>
> this is a well-defined bijection, since it matches the two enumerations entry by entry. By the computation in ($\Rightarrow$),
>
> $$
> \tau\sigma\tau^{-1} = \big(\tau(a_{1,1})\ \cdots\ \tau(a_{1,r_1})\big) \cdots \big(\tau(a_{k,1})\ \cdots\ \tau(a_{k,r_k})\big) = (b_{1,1}\ \cdots\ b_{1,r_1}) \cdots (b_{k,1}\ \cdots\ b_{k,r_k}) = \sigma'.
> $$

^pf-31-2

*Uses:* [[Group Theory §11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]], [[Group Theory §31 Conjugacy Classes#^def-31-2|Def. §31.2]], [[Group Theory §12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]]

> [!remark]- Connections
> - In $A_n$ a class of $S_n$ can split: [[Group Theory §39 Simple Groups#^ex-39-1|Ex. §39.1]]; for $3$-cycles and $n \geq 5$ it does not: [[Group Theory §39 Simple Groups#^lem-39-8|§39.8]].

> [!example] Example §31.1: Conjugating One Permutation to Another
> In $S_5$, let $\sigma = (1\,2\,3)(4\,5)$ and $\sigma' = (2\,5\,1)(3\,4)$; both have cycle type $(3,2)$. Reading off the entries in order,
>
> $$
> \tau: 1 \mapsto 2,\quad 2 \mapsto 5,\quad 3 \mapsto 1,\quad 4 \mapsto 3,\quad 5 \mapsto 4,
> $$
>
> i.e. $\tau = (1\,2\,5\,4\,3)$, and then $\tau\sigma\tau^{-1} = (\tau(1)\ \tau(2)\ \tau(3))(\tau(4)\ \tau(5)) = (2\,5\,1)(3\,4) = \sigma'$. The conjugating element is not unique: one may start each cycle of $\sigma'$ at any of its entries, and permute cycles of equal length among themselves.

^ex-31-1

![[m493-31-1.svg]]
*Conjugation relabels: $\tau\sigma\tau^{-1}$ has the same arrow diagram as $\sigma$, with each point $i$ renamed $\tau(i)$. In particular it has the same cycle type.*

> [!example] Example §31.2: Conjugacy Classes of $S_3$ and $S_4$
> $S_3$ has three conjugacy classes, by cycle type: $\{e\}$; the three transpositions $\{(1\,2), (1\,3), (2\,3)\}$; the two $3$-cycles $\{(1\,2\,3), (1\,3\,2)\}$. Sizes $1 + 3 + 2 = 6$. In $S_4$ the cycle types are $1^4$, $2\,1^2$, $2^2$, $3\,1$, $4$, with classes of sizes $1, 6, 3, 8, 6$, summing to $24$. Note that the class sizes need not divide each other, but each divides $|S_n|$ — explained by the orbit–stabilizer theorem in [[Group Theory §32 Conjugation as an Action and the Class Equation#^cor-32-2|§32.2]].

^ex-31-2

![[m493-31-2.svg]]
*The $24$ elements of $S_4$ sorted into conjugacy classes, one box per cycle type (§31.2); the class sizes $1, 3, 8, 6, 6$ (red) sum to $24$. Any two elements in one box are conjugate, and no element of one box is conjugate to an element of another.*

> [!definition] Definition §31.3: Similar Matrices
> Two matrices $X, Y \in \operatorname{Mat}_{n \times n}(\mathbb{C})$ are called **similar** if $X = SYS^{-1}$ for some $S \in GL_n(\mathbb{C})$. Thus for $Y \in GL_n(\mathbb{C})$, the conjugacy class of $Y$ in $GL_n(\mathbb{C})$ is exactly the set of invertible matrices similar to $Y$. Similar matrices have the same characteristic polynomial: $\det(xI - SYS^{-1}) = \det(S(xI - Y)S^{-1}) = \det(xI - Y)$.
>
> *Source: lecture 9/9*

^def-31-3

*Uses:* [[Linear Algebra 9C Determinants#^ladr-9-49|LADR 9.49]]

> [!remark]- Connections
> - The operator version: [[Linear Algebra 9C Determinants#^ladr-9-52|LADR 9.52 (Determinant is a similarity invariant)]].

> [!theorem] Proposition §31.3: Conjugacy Class of a Diagonal Matrix
> Let $D = \begin{pmatrix} 3 & 0 \\ 0 & 4 \end{pmatrix} \in GL_2(\mathbb{C})$. The conjugacy class of $D$ in $GL_2(\mathbb{C})$ is the set of all $2 \times 2$ complex matrices with eigenvalues $3$ and $4$:
>
> $$
> \operatorname{Conj}(D) = \{ A \in GL_2(\mathbb{C}) : \det(xI - A) = (x - 3)(x - 4) \} = \{ A : \operatorname{tr} A = 7,\ \det A = 12 \}.
> $$
>
> *Source: WS 3.3*

^prop-31-3

> [!proof]+ Proof
> ($\subseteq$) If $A = SDS^{-1}$, then $A$ is similar to $D$, so $\det(xI - A) = \det(xI - D) = (x - 3)(x - 4)$.
>
> ($\supseteq$) Suppose $\det(xI - A) = (x - 3)(x - 4)$, so $A$ has the two distinct eigenvalues $3$ and $4$. Choose eigenvectors $v_3, v_4 \in \mathbb{C}^2$ with $Av_3 = 3v_3$, $Av_4 = 4v_4$. [[Linearly independent eigenvectors|Eigenvectors for distinct eigenvalues are linearly independent]] (if $av_3 + bv_4 = 0$, apply $A$ to get $3av_3 + 4bv_4 = 0$; subtracting $3$ times the first relation gives $bv_4 = 0$, so $b = 0$, then $a = 0$), so $S = [\,v_3 \mid v_4\,]$ is invertible. Then $AS = [\,3v_3 \mid 4v_4\,] = SD$, i.e. $A = SDS^{-1} \in \operatorname{Conj}(D)$. Finally, a $2 \times 2$ matrix has characteristic polynomial $x^2 - (\operatorname{tr} A)x + \det A$, so the condition is $\operatorname{tr} A = 7$, $\det A = 12$; such $A$ is automatically invertible since $\det A \neq 0$.

^pf-31-3

*Uses:* [[Group Theory §31 Conjugacy Classes#^def-31-1|Def. §31.1]], [[Group Theory §31 Conjugacy Classes#^def-31-3|Def. §31.3]], [[Linear Algebra 5A Invariant Subspaces#^ladr-5-11|LADR 5.11]], [[Linear Algebra 9C Determinants#^ladr-9-65|LADR 9.65]], [[Linear Algebra 9C Determinants#^ladr-9-50|LADR 9.50]]

> [!remark] Remark: What the Argument Uses
> The direction ($\supseteq$) needed the eigenvalues to be *distinct*, which forced diagonalizability. For a diagonal matrix with a repeated eigenvalue, e.g. $\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = 3I$, the conjugacy class is just $\{3I\}$ (it is [[Group Theory §33 The Center#^def-33-1|central]]), while $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$ has the same characteristic polynomial but is not similar to $3I$. Conjugacy classes in $GL_n(\mathbb{C})$ are classified in general by Jordan normal form, of which this problem is the diagonalizable case.

^rem-31-1

> [!remark]- Connections
> - Jordan normal form: [[Linear Algebra 8C Consequences of Generalized Eigenspace Decomposition#^ladr-8-46|LADR 8.46 (Jordan form)]].
