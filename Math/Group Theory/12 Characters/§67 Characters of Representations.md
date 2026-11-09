---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 67
tags: [group-theory, math493]
---
← [[§66 Invariant Vectors]] · ↑ [[· 12 Characters]] · [[§68 Actions on Matrix Spaces]] →

*Source: Lecture (Mon Nov 9).*

> [!definition] Definition §67.1: The Character of a Representation
> Let $V$ be a finite-dimensional representation of $G$ over $k$. The **character** of $V$ is the function
>
> $$
> \chi_V: G \to k, \qquad \chi_V(g) = \operatorname{Tr}\rho_V(g)
> $$
>
> (Definition [[§66 Invariant Vectors#^def-66-2|§66.2]]).
>
> *Source: WS 15; lecture 11/9*

^def-67-1

> [!remark]- Connections
> - Not the characters of [[§46 Characters#^def-46-1|Def. §46.1]] (homomorphisms to an abelian group), except in dimension $1$: see the remark *Two Meanings of “Character”* below.

In this language, WS 15.6 (Theorem [[§66 Invariant Vectors#^thm-66-10|§66.10]]) reads

$$
\dim V^G = \frac{1}{|G|}\sum_{g \in G} \chi_V(g).
$$

Many things in representation theory can be computed from characters, starting with this one.

> [!remark] Remark: Two Meanings of “Character”
> In [[§46 Characters|§46]] a character was a homomorphism from $G$ to an abelian group, most often $k^\times$ (Definition [[§46 Characters#^def-46-1|§46.1]]). That is the special case of a one-dimensional representation (One-Dimensional Representations and Characters, Example [[§61 Representations and Subrepresentations#^ex-61-2|§61.2]]): for $V = k$, $\rho_V(g)$ is the $1 \times 1$ matrix $[\chi(g)]$, whose trace is $\chi(g)$, so $\chi_V = \chi$. In general $\chi_V$ is not a homomorphism (Example [[§67 Characters of Representations#^ex-67-2|§67.2]]).
>
> *Source: lecture 11/9*

^rem-67-1

> [!theorem] Proposition §67.1: Characters Are Class Functions
> Let $V$ be a finite-dimensional representation of $G$. Then
>
> 1. $\chi_V(e) = (\dim V) \cdot 1_k$;
> 2. $\chi_V(hgh^{-1}) = \chi_V(g)$ for all $g, h \in G$: the character is constant on each conjugacy class.
>
> *Source: lecture 11/9; part (1) not from class*

^prop-67-1

> [!proof]+ Proof
> **(1)** *(Not from class; filled in.)* $e$ acts as the identity (action axiom), whose matrix in any basis is the identity matrix, of trace $(\dim V) \cdot 1_k$.
>
> **(2)** *(Board 11/9.)* Since $\rho_V$ is a homomorphism (Representations Are Homomorphisms to $GL(V)$, Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]),
>
> $$
> \rho_V(hgh^{-1}) = \rho_V(h)\,\rho_V(g)\,\rho_V(h)^{-1},
> $$
>
> and $\operatorname{Tr}(SAS^{-1}) = \operatorname{Tr}(A)$ for invertible $S$ (Corollary [[§66 Invariant Vectors#^cor-66-2|§66.2]], from $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$, Proposition [[§66 Invariant Vectors#^prop-66-1|§66.1]]). Hence $\chi_V(hgh^{-1}) = \operatorname{Tr}\rho_V(g) = \chi_V(g)$.

^pf-67-1

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§66 Invariant Vectors#^cor-66-2|§66.2]], [[§66 Invariant Vectors#^prop-66-1|§66.1]]

So a character is determined by one value per conjugacy class, which is much less data than one value per element: groups usually have many fewer conjugacy classes than elements. This is the analogue of Characters Are Constant on Conjugacy Classes (Proposition [[§46 Characters#^prop-46-1|§46.1]]) for the new meaning of the word, with a different reason: the trace is invariant under conjugation, while a homomorphism to an abelian group is constant on conjugacy classes because the target is commutative.

> [!theorem] Proposition §67.2: Characters Add over Direct Sums
> Let $W = U \oplus V$ (Definition [[§62 Direct Sums and Maschke's Theorem#^def-62-1|§62.1]]) be finite-dimensional, let $A: U \to U$ and $B: V \to V$ be linear, and let $A \oplus B: W \to W$, $u + v \mapsto Au + Bv$. Then
>
> $$
> \operatorname{Tr}(A \oplus B) = \operatorname{Tr}(A) + \operatorname{Tr}(B).
> $$
>
> Consequently, if $W = U \oplus V$ is a representation of $G$ and $U$, $V$ are subrepresentations, then $\chi_W = \chi_U + \chi_V$.
>
> *Source: lecture 11/9*

^prop-67-2

> [!proof]+ Proof
> *(Board 11/9; the statement was proposed in class and then proved.)* By Bases of a Direct Sum (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]), a basis $u_1, \ldots, u_m$ of $U$ and a basis $v_1, \ldots, v_n$ of $V$ together form a basis of $W$. In it the matrix of $A \oplus B$ is block diagonal, $\left(\begin{smallmatrix} A & 0 \\ 0 & B \end{smallmatrix}\right)$: $A$ uses nothing from $V$, and $B$ nothing from $U$. Its diagonal is that of $A$ followed by that of $B$, so the traces add. For representations, $\rho_W(g) = \rho_U(g) \oplus \rho_V(g)$, since $g(u + v) = gu + gv$ with $gu \in U$ and $gv \in V$ (WS 14.2, Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]). Taking traces gives $\chi_W(g) = \chi_U(g) + \chi_V(g)$.

^pf-67-2

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]], [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]

> [!definition] Definition §67.2: Character Table
> The **character table** of $G$ lists characters of representations: its columns are indexed by the conjugacy classes of $G$ (one representative each), its rows by representations, and the entry is the value of $\chi_V$ on the class.
>
> *Source: lecture 11/9*

^def-67-2

> [!example] Example §67.1: Characters of $S_3$ over $\mathbb{R}$
> The conjugacy classes of $S_3$ are the cycle types (Conjugacy Classes in $S_n$ Are Cycle Types, Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]), with representatives $e$, $(1\,2)$, $(1\,2\,3)$ and sizes $1$, $3$, $2$.
>
> | | $e$ | $(1\,2)$ | $(1\,2\,3)$ |
> |---|:-:|:-:|:-:|
> | trivial, $\mathbb{R}(1,1,1)$ | $1$ | $1$ | $1$ |
> | sign | $1$ | $-1$ | $1$ |
> | $U = (1,1,1)^\perp$ | $2$ | $0$ | $-1$ |
> | permutation, $\mathbb{R}^3 = \mathbb{R}(1,1,1) \oplus U$ | $3$ | $1$ | $0$ |
>
> - *Trivial:* every $\rho(g)$ is the $1 \times 1$ matrix $[1]$.
> - *Permutation representation:* the trace of a permutation matrix counts the basis vectors $e_i$ sent to themselves, i.e. the fixed points: $3$ for $e$, $1$ for $(1\,2)$, whose matrix $\left(\begin{smallmatrix} 0&1&0\\1&0&0\\0&0&1 \end{smallmatrix}\right)$ has one $1$ on the diagonal, and $0$ for $(1\,2\,3)$. It is not simple.
> - *$U$:* by additivity (Proposition [[§67 Characters of Representations#^prop-67-2|§67.2]]), $\chi_U = \chi_{\mathbb{R}^3} - \chi_{\mathrm{triv}} = (2, 0, -1)$, matching the traces of the matrices $\rho_{U_2}(g)$ in Example [[§61 Representations and Subrepresentations#^ex-61-3|§61.3]].
> - *Sign:* $\rho(g) = [\operatorname{sgn} g]$, so the values are those of $\operatorname{sgn}$: $1$, $-1$, and $1$ for the even permutation $(1\,2\,3)$.
>
> *(Not from class.)* Checking WS 15.6 against the table, with class sizes $1, 3, 2$: $\frac{1}{6}(3 + 3 \cdot 1 + 2 \cdot 0) = 1 = \dim (\mathbb{R}^3)^{S_3}$, the line $\mathbb{R}(1,1,1)$; $\frac{1}{6}(2 + 0 - 2) = 0$ for $U$; and $\frac16(1 - 3 + 2) = 0$ for the sign representation, as in Examples [[§66 Invariant Vectors#^ex-66-3|§66.3]] and [[§66 Invariant Vectors#^ex-66-4|§66.4]].
>
> *Source: lecture 11/9; the check not from class*

^ex-67-1

![[m493-64-1.svg]]

*(Not from lecture; figure added.)* Where the rows of the table come from. Left: $S_3$ permutes the basis vectors $e_1, e_2, e_3$, drawn as the corners of a triangle. The trace of a permutation matrix is the number of fixed corners: $3$ for $e$, $1$ for $(1\,2)$, which reflects in the dashed mirror and fixes only $e_3$ (circled), and $0$ for $(1\,2\,3)$, which turns the triangle by $120^\circ$. Right: on the plane $U = (1,1,1)^\perp$, with $\bar e_i$ the projections of the $e_i$, $(1\,2)$ is the reflection in the dashed line. It fixes the red vector on the mirror (eigenvalue $+1$) and reverses the perpendicular vector $x$ (eigenvalue $-1$), so its trace is $1 + (-1) = 0$. The $3$-cycle is the rotation by $120^\circ$, with matrix $\left(\begin{smallmatrix} \cos 120^\circ & -\sin 120^\circ \\ \sin 120^\circ & \cos 120^\circ \end{smallmatrix}\right)$ in an orthonormal basis and trace $2\cos 120^\circ = -1$.

> [!example] Example §67.2: The Character of $k\{1,2,3\}$ Is Not a Homomorphism
> *(Not from class.)* The character of the permutation representation $k\{1,2,3\} = k^3$ of $S_3$ takes the values $3$, $1$, $0$ on the three conjugacy classes (Example [[§67 Characters of Representations#^ex-67-1|§67.1]]). The value $0$ at $(1\,2\,3)$ does not lie in $k^\times$, so $\chi$ is not a homomorphism $S_3 \to k^\times$. And $\chi(e) = 3 \neq 1$ whenever $2 \neq 0$ in $k$, while a homomorphism sends $e$ to $1$.

^ex-67-2
