---
type: section
subject: "[[Group Theory]]"
chapter: 3
section: 10
tags: [group-theory, math493]
---
← [[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem]] · ↑ [[· 3 Permutations]] · [[§11 Disjoint Cycle Decomposition]] →

*Reference: Pinter Ch. 7, Ch. 8.*

> [!definition] Definition §10.1: Two-Line and Cycle Notation
> A permutation $\sigma \in S_n$ is determined by the list $\sigma(1), \ldots, \sigma(n)$. **Two-line notation** records this as
> $\sigma = \begin{pmatrix} 1 & 2 & \cdots & n \\ \sigma(1) & \sigma(2) & \cdots & \sigma(n) \end{pmatrix}$.
> **Cycle notation** writes $(a_1\ a_2\ \cdots\ a_r)$ for the permutation sending $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_r \mapsto a_1$ and fixing every other element; such a permutation is an **$r$-cycle**, and a $2$-cycle $(a\ b)$ is called a **transposition**. The identity is written $e$ (Worksheet 1 writes $1$; some authors write $()$). A cycle can be started at any of its entries: $(1\,2\,3) = (2\,3\,1) = (3\,1\,2)$.

^def-10-1

> [!remark]- Connections
> - Axler's permutations as lists, used for determinants: [[§33 Alternating Multilinear Forms#^ladr-9-31|LADR 9.31]].

> [!example] Example §10.1: The Group $S_3$ in Detail
> **Elements.** $|S_3| = 3! = 6$:
>
> | cycle | two-line | arrows | action |
> |:---:|:---:|:---:|:---|
> | $1$ | $\begin{pmatrix}1&2&3\\1&2&3\end{pmatrix}$ | $1\mapsto1,\ 2\mapsto2,\ 3\mapsto3$ | fixes everything |
> | $(1\,2)$ | $\begin{pmatrix}1&2&3\\2&1&3\end{pmatrix}$ | $1\mapsto2,\ 2\mapsto1,\ 3\mapsto3$ | swaps $1 \leftrightarrow 2$ |
> | $(1\,3)$ | $\begin{pmatrix}1&2&3\\3&2&1\end{pmatrix}$ | $1\mapsto3,\ 2\mapsto2,\ 3\mapsto1$ | swaps $1 \leftrightarrow 3$ |
> | $(2\,3)$ | $\begin{pmatrix}1&2&3\\1&3&2\end{pmatrix}$ | $1\mapsto1,\ 2\mapsto3,\ 3\mapsto2$ | swaps $2 \leftrightarrow 3$ |
> | $(1\,2\,3)$ | $\begin{pmatrix}1&2&3\\2&3&1\end{pmatrix}$ | $1\mapsto2,\ 2\mapsto3,\ 3\mapsto1$ | $1 \to 2 \to 3 \to 1$ |
> | $(1\,3\,2)$ | $\begin{pmatrix}1&2&3\\3&1&2\end{pmatrix}$ | $1\mapsto3,\ 2\mapsto1,\ 3\mapsto2$ | $1 \to 3 \to 2 \to 1$ |
>
> In two-line notation the top row lists the inputs and the bottom row the corresponding outputs: column $i$ reads “$i \mapsto \sigma(i)$.”
>
> **Multiplying.** $\sigma\tau$ is the composition $\sigma \circ \tau$: *apply $\tau$ first, then $\sigma$*. To compute a product, track each number through the factors from right to left. For $(1\,2)(2\,3)$:
>
> $$ 1 \xrightarrow{(2\,3)} 1 \xrightarrow{(1\,2)} 2, \qquad 2 \xrightarrow{(2\,3)} 3 \xrightarrow{(1\,2)} 3, \qquad 3 \xrightarrow{(2\,3)} 2 \xrightarrow{(1\,2)} 1, $$
>
> so $(1\,2)(2\,3) = (1\,2\,3)$. In the other order, $(2\,3)(1\,2)$: $1 \to 2 \to 3$, $2 \to 1 \to 1$, $3 \to 3 \to 2$, so $(2\,3)(1\,2) = (1\,3\,2) \neq (1\,2)(2\,3)$. Thus $S_3$ is non-abelian.
>
> **Inverses** are read off by reversing the arrows: each transposition is its own inverse, and $(1\,2\,3)^{-1} = (1\,3\,2)$.
>
> **Multiplication table** (entry in row $\sigma$, column $\tau$ is $\sigma\tau$, i.e. $\tau$ applied first):
>
> | $\sigma \backslash \tau$ | $e$ | $(1\,2)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2\,3)$ | $(1\,3\,2)$ |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | $e$ | $e$ | $(1\,2)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2\,3)$ | $(1\,3\,2)$ |
> | $(1\,2)$ | $(1\,2)$ | $e$ | $(1\,3\,2)$ | $(1\,2\,3)$ | $(2\,3)$ | $(1\,3)$ |
> | $(1\,3)$ | $(1\,3)$ | $(1\,2\,3)$ | $e$ | $(1\,3\,2)$ | $(1\,2)$ | $(2\,3)$ |
> | $(2\,3)$ | $(2\,3)$ | $(1\,3\,2)$ | $(1\,2\,3)$ | $e$ | $(1\,3)$ | $(1\,2)$ |
> | $(1\,2\,3)$ | $(1\,2\,3)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2)$ | $(1\,3\,2)$ | $e$ |
> | $(1\,3\,2)$ | $(1\,3\,2)$ | $(2\,3)$ | $(1\,2)$ | $(1\,3)$ | $e$ | $(1\,2\,3)$ |
>
> Reading the table: every row and column is a permutation of the six elements (a consequence of [[§2 First Consequences of the Axioms#^prop-2-1|cancellation]], [[§2 First Consequences of the Axioms#^cor-2-8|§2.8]]); the upper-left $2 \times 2$ block shows $\{e, (1\,2)\}$ is closed; the lower-right $2 \times 2$ block, together with the first row and column, shows $\{e, (1\,2\,3), (1\,3\,2)\}$ is closed; and the table is not symmetric about the diagonal, which is non-commutativity made visible.

^ex-10-1

![[m493-10-1.svg]]
*$S_3$ as the symmetries of a triangle with corners labeled $1, 2, 3$: a symmetry moves the corner at $i$ to the position of $\sigma(i)$. The rotation by $120^\circ$ in the direction of the blue arrow is $(1\,2\,3)$, the opposite rotation is $(1\,3\,2)$, and the reflection in each dashed red axis fixes the corner on the axis and swaps the other two, giving $(2\,3)$, $(1\,3)$, $(1\,2)$. With the identity, these are all six elements.*

> [!remark]- Connections
> - The same table as a worksheet problem: [[§14 Multiplication Tables#^ex-14-5|Table of S₃]] (WS 2.4); 590 counterpart: [[§21 Algebra Prerequisites꞉ Groups#^ex-21-1|590 Ex. §21.1]].

> [!remark] Remark: Convention Warning
> “Right factor first” is the function-composition convention, confirmed in class on Sept 2: Speyer defines the operation on $S_n$ by $(f \circ g)(j) = f(g(j))$ and computes $(1\,2)(2\,3) = (1\,2\,3)$ by applying $(2\,3)$ first. Some authors — particularly in combinatorics — compose left to right, writing $x^{\sigma\tau} = (x^\sigma)^\tau$; under that convention every product above is reversed, e.g. $(1\,2)(2\,3)$ would equal $(1\,3\,2)$. When reading any source on permutations, locate its convention before trusting a single computation.

^rem-10-1

![[m493-10-2.svg]]
*Right factor first, as wiring: each strand passes through the factor applied first, then the second. Left: $(1\,2)(2\,3)$ sends $1 \to 1 \to 2$ (red), $2 \to 3 \to 3$ (blue), $3 \to 2 \to 1$ (green), so it is $(1\,2\,3)$. Right: the other order gives $(1\,3\,2)$. Different diagrams, so $S_3$ is non-abelian; reading a product left to right would swap the two pictures.*
