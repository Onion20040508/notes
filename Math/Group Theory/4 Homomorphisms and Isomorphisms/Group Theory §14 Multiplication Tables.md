---
type: section
subject: "[[Group Theory]]"
chapter: 4
section: 14
tags: [group-theory, math493]
---
← [[Group Theory §13 Subgroups of S₃]] · ↑ [[Group Theory — 4 Homomorphisms and Isomorphisms]] · [[Group Theory §15 Homomorphisms]] →

*Reference: Pinter Ch. 3 (group tables), Ch. 9 (isomorphism).*

> [!definition] Definition §14.1: Multiplication Table
> For a finite group $G = \{g_1, \ldots, g_n\}$, the **multiplication table** (or **Cayley table**) is the $n \times n$ array whose entry in row $g_i$, column $g_j$ is the product $g_i g_j$ (row element on the left). By [[Group Theory §2 First Consequences of the Axioms#^prop-2-7|Unique Solvability]], every row and every column is a permutation of $G$; the table is symmetric about the main diagonal exactly when $G$ is abelian.
>
> When the group operation is composition of functions ($\sigma\tau = \sigma \circ \tau$, right factor first), the two conventions combine as follows: *the element from the top row (the column label) is applied first; the element from the left column (the row label) is applied second.* E.g. in the $S_3$ table ([[Group Theory §14 Multiplication Tables#^ex-14-5|Ex. §14.5]]), row $(1\,2)$, column $(2\,3)$ holds $(1\,2)(2\,3) = (1\,2\,3)$, computed by applying $(2\,3)$ first.

^def-14-1

> [!example] Example §14.1: The Tables of $\mathbb{Z}/4\mathbb{Z}$ and $U_5$
> The worksheet gives, side by side:
>
> | $+$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|
> | $0$ | $0$ | $1$ | $2$ | $3$ |
> | $1$ | $1$ | $2$ | $3$ | $0$ |
> | $2$ | $2$ | $3$ | $0$ | $1$ |
> | $3$ | $3$ | $0$ | $1$ | $2$ |
>
> | $\times$ | $1$ | $2$ | $3$ | $4$ |
> |---|---|---|---|---|
> | $1$ | $1$ | $2$ | $3$ | $4$ |
> | $2$ | $2$ | $4$ | $1$ | $3$ |
> | $3$ | $3$ | $1$ | $4$ | $2$ |
> | $4$ | $4$ | $3$ | $2$ | $1$ |
>
> Both are symmetric (abelian). Each entry of the right table is a product reduced modulo $5$, e.g. $3 \cdot 4 = 12 \equiv 2$.

^ex-14-1

> [!example] Example §14.2: Table of $\mathbb{Z}/6\mathbb{Z}$
> Operation $+$, entries reduced modulo $6$:
>
> | $+$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
> |---|---|---|---|---|---|---|
> | $0$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
> | $1$ | $1$ | $2$ | $3$ | $4$ | $5$ | $0$ |
> | $2$ | $2$ | $3$ | $4$ | $5$ | $0$ | $1$ |
> | $3$ | $3$ | $4$ | $5$ | $0$ | $1$ | $2$ |
> | $4$ | $4$ | $5$ | $0$ | $1$ | $2$ | $3$ |
> | $5$ | $5$ | $0$ | $1$ | $2$ | $3$ | $4$ |
>
> Each row is the previous row shifted one place left: row $a$ is $a, a+1, \ldots$ wrapping around. The table is symmetric (abelian), and $0$ appears in row $a$ at column $6 - a$, exhibiting $-a$.
>
> *Source: WS 2.1*

^ex-14-2

> [!example] Example §14.3: Table of $U_7$
> Operation $\times$, entries reduced modulo $7$:
>
> | $\times$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
> |---|---|---|---|---|---|---|
> | $1$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
> | $2$ | $2$ | $4$ | $6$ | $1$ | $3$ | $5$ |
> | $3$ | $3$ | $6$ | $2$ | $5$ | $1$ | $4$ |
> | $4$ | $4$ | $1$ | $5$ | $2$ | $6$ | $3$ |
> | $5$ | $5$ | $3$ | $1$ | $6$ | $4$ | $2$ |
> | $6$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ |
>
> Symmetric (abelian). The position of $1$ in each row gives the inverse: $2^{-1} = 4$, $3^{-1} = 5$, $6^{-1} = 6$, matching the inverse table in [[Group Theory §8 Invertibility and Unit Groups#^ex-8-2|Ex. §8.2]].
>
> *Source: WS 2.2*

^ex-14-3

> [!example] Example §14.4: Table of $U_8$
> Operation $\times$, entries reduced modulo $8$:
>
> | $\times$ | $1$ | $3$ | $5$ | $7$ |
> |---|---|---|---|---|
> | $1$ | $1$ | $3$ | $5$ | $7$ |
> | $3$ | $3$ | $1$ | $7$ | $5$ |
> | $5$ | $5$ | $7$ | $1$ | $3$ |
> | $7$ | $7$ | $5$ | $3$ | $1$ |
>
> Symmetric (abelian). The diagonal consists entirely of $1$'s: every element is its own inverse.
>
> *Source: WS 2.3*

^ex-14-4

> [!example] Example §14.5: Table of $S_3$
> The worksheet recalls that $S_n$ is the group of bijections $\{1, \ldots, n\} \to \{1, \ldots, n\}$ under composition, introduces cycle notation — $(x_1\ x_2\ \cdots\ x_k)$ for $x_1 \mapsto x_2 \mapsto \cdots \mapsto x_k \mapsto x_1$, fixing everything else — and writes $\mathrm{Id}$ or $e$ for the identity. WS 2.4 asks for the multiplication table of $S_3$ with rows and columns ordered $e, (1\,2), (1\,3), (2\,3), (1\,2\,3), (1\,3\,2)$. With the convention $(f \circ g)(j) = f(g(j))$ — column element applied first — the entry in row $\sigma$, column $\tau$ is $\sigma\tau$:
>
> | $\circ$ | $e$ | $(1\,2)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2\,3)$ | $(1\,3\,2)$ |
> |---|---|---|---|---|---|---|
> | $e$ | $e$ | $(1\,2)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2\,3)$ | $(1\,3\,2)$ |
> | $(1\,2)$ | $(1\,2)$ | $e$ | $(1\,3\,2)$ | $(1\,2\,3)$ | $(2\,3)$ | $(1\,3)$ |
> | $(1\,3)$ | $(1\,3)$ | $(1\,2\,3)$ | $e$ | $(1\,3\,2)$ | $(1\,2)$ | $(2\,3)$ |
> | $(2\,3)$ | $(2\,3)$ | $(1\,3\,2)$ | $(1\,2\,3)$ | $e$ | $(1\,3)$ | $(1\,2)$ |
> | $(1\,2\,3)$ | $(1\,2\,3)$ | $(1\,3)$ | $(2\,3)$ | $(1\,2)$ | $(1\,3\,2)$ | $e$ |
> | $(1\,3\,2)$ | $(1\,3\,2)$ | $(2\,3)$ | $(1\,2)$ | $(1\,3)$ | $e$ | $(1\,2\,3)$ |
>
> This agrees with the table in [[Group Theory §10 Cycle Notation and the Group S₃#^ex-10-1|Ex. §10.1]]. It is *not* symmetric: e.g. row $(1\,2)$, column $(2\,3)$ holds $(1\,2\,3)$, while row $(2\,3)$, column $(1\,2)$ holds $(1\,3\,2)$. Every row and column is a permutation of the six elements, and $e$ appears on the diagonal for the transpositions (self-inverse) and off the diagonal for the $3$-cycles (inverse to each other).
>
> *Source: WS 2.4*

^ex-14-5

![[m493-14-1.svg]]
*The $S_3$ table of Ex. §14.5 with the identity cells in blue. They lie on the diagonal (shaded) for $e$ and the three transpositions, each its own inverse, but off it for the $3$-cycles $(1\,2\,3)$ and $(1\,3\,2)$, which are inverse to each other. The two red cells are mirror images across the diagonal yet hold different elements, $(1\,2)(2\,3) = (1\,2\,3)$ and $(2\,3)(1\,2) = (1\,3\,2)$: the table is not symmetric, so $S_3$ is not abelian.*
