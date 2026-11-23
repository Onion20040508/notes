---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 73
tags: [group-theory, math493]
---
← [[§72 Representations of Cyclic Groups]] · ↑ [[· 12 Characters]]

*Source: Lecture (Mon Nov 23), from the board page and the transcript; there was no worksheet.*

This section finds all simple representations of $S_4$. The method is the one of [[§71 The Character Table|§71]], now used to discover representations and not only to check them. The columns of the table are the five conjugacy classes. Two rows are known at once, the trivial and the sign representation. The permutation representation $k^4$ gives a third row after the trivial representation is split off. Products of characters give further characters: the product with the sign is a fourth row, and the square of the third row is not simple. Its multiplicities are read off with the pairing, and what is left over is the fifth row, a two-dimensional representation that nobody wrote down in advance. There are five conjugacy classes, so there is no sixth row. At the end the two-dimensional representation is identified: its character shows that the Klein four-group acts trivially, so it comes from the two-dimensional representation of $S_3 \cong S_4/K$.

Throughout this section $k$ is a field containing $\mathbb{Q}$, all representations are finite-dimensional representations over $k$, and $\chi_0, \ldots, \chi_4$ denote the five rows of the table of $S_4$, as on the board. (In [[§72 Representations of Cyclic Groups|§72]] the letters $\chi_k$ denoted the characters of $\mathbb{Z}/N\mathbb{Z}$.)

## The Classes of $S_4$ and the Pairing for Symmetric Groups

> [!example] Example §73.1: Conjugacy Classes of $S_4$ and Their Sizes
> The conjugacy classes of $S_4$ are the cycle types (Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]); there are five (Example [[§33 Conjugacy Classes#^ex-33-2|§33.2]]). They are the columns of the character table.
>
> | representative | $e$ | $(1\,2)$ | $(1\,2\,3)$ | $(1\,2)(3\,4)$ | $(1\,2\,3\,4)$ |
> |---|---|---|---|---|---|
> | class size | $1$ | $6$ | $8$ | $3$ | $6$ |
>
> 1. *Transpositions:* $\binom{4}{2} = 6$.
> 2. *$3$-cycles:* choose $i$, $j$, $k$ in $4 \cdot 3 \cdot 2$ ways and divide by $3$, because $(i\,j\,k) = (j\,k\,i) = (k\,i\,j)$; this gives $8$. Or choose the set $\{i, j, k\}$ in $\binom{4}{3} = 4$ ways and one of the $2$ directions in which to cycle it: $4 \cdot 2 = 8$.
> 3. *The centralizer.* The first count is an instance of $|\operatorname{Conj}(g)| = |G|/|C_G(g)|$ (Corollary [[§34 Conjugation as an Action and the Class Equation#^cor-34-2|§34.2]]): for $g = (1\,2\,3)$ the centralizer (Definition [[§34 Conjugation as an Action and the Class Equation#^def-34-1|§34.1]]) is $\langle (1\,2\,3) \rangle$, of order $3$, and $24/3 = 8$. So every class size is a divisor of $24$.
> 4. *Double transpositions:* $3$, one for each way of splitting $\{1, 2, 3, 4\}$ into two pairs. Or choose one of the $6$ transpositions; the other is then determined, and each double transposition is obtained twice: $6/2 = 3$.
> 5. *$4$-cycles:* $6$. Check: $1 + 6 + 8 + 3 + 6 = 24$.
>
> *Source: lecture 11/23*

^ex-73-1

**Transcription note (board 11/23).** The board writes $|\operatorname{Conj}(\sigma)| = |G|/|Z(\sigma)|$; these notes write $C_G(\sigma)$ for the centralizer and keep $Z(G)$ for the center.

> [!theorem] Lemma §73.1: Every Permutation Is Conjugate to Its Inverse
> Let $\sigma \in S_n$.
>
> 1. $\sigma^{-1}$ has the same cycle type (Definition [[§33 Conjugacy Classes#^def-33-2|§33.2]]) as $\sigma$, so $\sigma^{-1}$ is conjugate to $\sigma$ in $S_n$.
> 2. For every finite-dimensional representation $V$ of $S_n$, over any field, $\chi_V(\sigma^{-1}) = \chi_V(\sigma)$.
> 3. If $n! \neq 0$ in $k$, the pairing (Definition [[§71 The Character Table#^def-71-2|§71.2]]) of two characters of $S_n$ is the dot product of the two rows weighted by the class sizes, with no inverses:
>
> $$
> \langle \chi_V, \chi_W \rangle = \frac{1}{n!}\sum_{i=1}^c |\operatorname{Conj}(g_i)|\,\chi_V(g_i)\,\chi_W(g_i).
> $$
>
> *Source: lecture 11/23*

^lem-73-1

> [!proof]+ Proof
> *(Lecture 11/23: “in the symmetric group, $g$ is always conjugate to $g^{-1}$, because it has the same cycle type”; details filled in.)* **(1)** Write $\sigma = c_1c_2 \cdots c_m$ as a product of disjoint cycles (Theorem [[§11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]]). The inverse of an $r$-cycle $(a_1\,a_2\,\ldots\,a_r)$ is $(a_r\,\ldots\,a_2\,a_1)$, an $r$-cycle that moves the same entries. Disjoint cycles commute (Lemma [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]]), so $\sigma^{-1} = c_1^{-1}c_2^{-1} \cdots c_m^{-1}$, a product of disjoint cycles of the same lengths as those of $\sigma$. So $\sigma^{-1}$ and $\sigma$ have the same cycle type, and they are conjugate (Theorem [[§33 Conjugacy Classes#^thm-33-3|§33.3]]).
>
> **(2)** Characters are constant on conjugacy classes (Proposition [[§67 Characters of Representations#^prop-67-1|§67.1]](2)).
>
> **(3)** In Definition [[§71 The Character Table#^def-71-2|§71.2]], replace $\chi_V(g_i^{-1})$ by $\chi_V(g_i)$, using (2).

^pf-73-1

*Uses:* [[§11 Disjoint Cycle Decomposition#^thm-11-3|§11.3]], [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]], [[§33 Conjugacy Classes#^thm-33-3|§33.3]], [[§67 Characters of Representations#^prop-67-1|§67.1]], [[§71 The Character Table#^def-71-2|Def. §71.2]]

**Transcription note (board 11/23).** The board computes the sums $\sum_C |C|\,\chi(C)\,\psi(C)$ without the factor $\frac{1}{24}$ and divides by $24$ at the end. Its “$(\chi_2, \chi_2) = 24$” is $\langle \chi_2, \chi_2 \rangle = 1$ in these notes, and its “$96/4 = 24$” is $\langle \chi_2^2, \chi_2^2 \rangle = 4$.

The lecture reads off multiplicities “as in an orthogonal basis”: to write a vector in an orthogonal basis, take dot products with the basis vectors. For characters this is the following statement, valid for every finite group.

> [!theorem] Proposition §73.2: Multiplicities from the Character
> Let $G$ be a finite group and $k$ a field containing $\mathbb{Q}$. Let $S_1, \ldots, S_r$ be finite-dimensional simple representations of $G$ over $k$ (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) with $S_i \not\cong S_j$ for $i \neq j$, let $a_1, \ldots, a_r \geq 0$ be integers, and let $V \cong S_1^{\oplus a_1} \oplus \cdots \oplus S_r^{\oplus a_r}$ (Definition [[§70 Schur's Lemma and Multiplicities#^def-70-2|§70.2]]). Then, for the pairing of Definition [[§71 The Character Table#^def-71-2|§71.2]]:
>
> 1. $\chi_V = \sum_{i=1}^r a_i\,\chi_{S_i}$;
> 2. $\langle \chi_V, \chi_{S_i} \rangle = a_i\,\langle \chi_{S_i}, \chi_{S_i} \rangle$, and $\langle \chi_{S_i}, \chi_{S_i} \rangle = \dim\operatorname{Hom}_G(S_i, S_i)$ is a positive integer; so $a_i = \langle \chi_V, \chi_{S_i} \rangle / \langle \chi_{S_i}, \chi_{S_i} \rangle$;
> 3. $\langle \chi_V, \chi_V \rangle = \sum_{i=1}^r a_i^2\,\langle \chi_{S_i}, \chi_{S_i} \rangle$.
>
> *Source: lecture 11/23*

^prop-73-2

> [!proof]+ Proof
> *Idea:* the characters of the $S_i$ are orthogonal, so pairing with $\chi_{S_i}$ picks out the term with $a_i$.
>
> *(Lecture 11/23, for $S_4$; written out for a finite group.)* **(1)** Isomorphic representations have the same character (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]), and the character of an external direct sum is the sum of the characters (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]]).
>
> **(2)** The pairing is linear in the first entry (Proposition [[§71 The Character Table#^prop-71-3|§71.3]](1)). By WS 18.3 (Proposition [[§71 The Character Table#^prop-71-5|§71.5]](1)), $\langle \chi_{S_j}, \chi_{S_i} \rangle = 0$ for $j \neq i$ and $\langle \chi_{S_i}, \chi_{S_i} \rangle = \dim\operatorname{Hom}_G(S_i, S_i)$. So by (1)
>
> $$
> \langle \chi_V, \chi_{S_i} \rangle = \sum_{j=1}^r a_j\,\langle \chi_{S_j}, \chi_{S_i} \rangle = a_i\,\langle \chi_{S_i}, \chi_{S_i} \rangle.
> $$
>
> The number $\dim\operatorname{Hom}_G(S_i, S_i)$ is a positive integer, because $\mathrm{Id}_{S_i} \neq 0$ lies in $\operatorname{Hom}_G(S_i, S_i)$; it is not zero in $k$, so one may divide by it.
>
> **(3)** By (1) and linearity in the second entry, $\langle \chi_V, \chi_V \rangle = \sum_i a_i\,\langle \chi_V, \chi_{S_i} \rangle$, and by (2) this is $\sum_i a_i^2\,\langle \chi_{S_i}, \chi_{S_i} \rangle$.

^pf-73-2

*Uses:* [[§67 Characters of Representations#^lem-67-3|§67.3]], [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]], [[§71 The Character Table#^prop-71-3|§71.3]], [[§71 The Character Table#^prop-71-5|§71.5]]

> [!theorem] Corollary §73.3: Representations with the Same Character Are Isomorphic
> Let $G$ be a finite group and $k$ a field containing $\mathbb{Q}$. If $V$ and $W$ are finite-dimensional representations of $G$ over $k$ with $\chi_V = \chi_W$ (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]), then $V \cong W$.
>
> *Source: not from class*

^cor-73-3

> [!proof]+ Proof
> *(Not from class.)* By Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], $V$ and $W$ are isomorphic to direct sums of simple representations. Choose simple representations $S_1, \ldots, S_r$, pairwise non-isomorphic, such that every simple summand of $V$ and every simple summand of $W$ is isomorphic to exactly one $S_i$. Replacing each summand by the $S_i$ isomorphic to it, coordinate by coordinate as in the proof of Corollary [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]], gives $V \cong \bigoplus_i S_i^{\oplus a_i}$ and $W \cong \bigoplus_i S_i^{\oplus b_i}$ with integers $a_i, b_i \geq 0$. By Proposition [[§73 The Character Table of S₄#^prop-73-2|§73.2]](2),
>
> $$
> a_i = \frac{\langle \chi_V, \chi_{S_i} \rangle}{\langle \chi_{S_i}, \chi_{S_i} \rangle} = \frac{\langle \chi_W, \chi_{S_i} \rangle}{\langle \chi_{S_i}, \chi_{S_i} \rangle} = b_i.
> $$
>
> So $V$ and $W$ are isomorphic to the same direct sum, and $V \cong W$ (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](3)).

^pf-73-3

*Uses:* [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]], [[§73 The Character Table of S₄#^prop-73-2|§73.2]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]]

## The First Four Rows

> [!example] Example §73.2: The Rows of the Trivial and the Sign Representation
> The trivial representation (Example [[§61 Representations and Subrepresentations#^ex-61-1|§61.1]]) and the sign representation (Example [[§61 Representations and Subrepresentations#^ex-61-2|§61.2]]) of $S_4$ are one-dimensional, hence simple. Their characters are
>
> $$
> \chi_0 = (1, 1, 1, 1, 1), \qquad \chi_1 = (1, -1, 1, 1, -1)
> $$
>
> on the classes of $e$, $(1\,2)$, $(1\,2\,3)$, $(1\,2)(3\,4)$, $(1\,2\,3\,4)$.
>
> 1. *The signs.* A transposition has sign $-1$. A double transposition is a product of two transpositions and has sign $1$. A $4$-cycle is a product of three transpositions and has sign $-1$. A $3$-cycle is a product of two transpositions and has sign $1$.
> 2. *Row orthogonality.* By Lemma [[§73 The Character Table of S₄#^lem-73-1|§73.1]](3), with the class sizes $1, 6, 8, 3, 6$,
>
> $$
> \langle \chi_0, \chi_1 \rangle = \tfrac{1}{24}(1 - 6 + 8 + 3 - 6) = 0, \qquad \langle \chi_0, \chi_0 \rangle = \tfrac{1}{24}(1 + 6 + 8 + 3 + 6) = 1.
> $$
>
> *Source: board 11/23*

^ex-73-2

> [!theorem] Proposition §73.4: The Permutation Representation $k^4$ and the Representation $V_2$
> Let $S_4$ act on $k^4$ by permuting the coordinates, the permutation representation (Definition [[§61 Representations and Subrepresentations#^def-61-2|§61.2]]) of the action on $\{1, 2, 3, 4\}$. Let
>
> $$
> U_1 = k\,(1, 1, 1, 1), \qquad V_2 = \{x \in k^4 : x_1 + x_2 + x_3 + x_4 = 0\}.
> $$
>
> 1. $U_1$ and $V_2$ are subrepresentations (Definition [[§61 Representations and Subrepresentations#^def-61-3|§61.3]]), and $U_1$ is isomorphic to the trivial representation.
> 2. $k^4 = U_1 \oplus V_2$.
> 3. $\chi_{k^4} = (4, 2, 1, 0, 0)$: the value at $\sigma$ is the number of fixed points of $\sigma$.
> 4. $\chi_2 = \chi_{V_2} = (3, 1, 0, -1, -1)$.
>
> *Source: lecture 11/23*

^prop-73-4

> [!proof]+ Proof
> *(Lecture 11/23.)* **(1)** Permuting the coordinates of a vector does not change the sum of its coordinates, and it fixes $(1, 1, 1, 1)$. So both subspaces are mapped into themselves by every $\sigma$, and every $\sigma$ acts on $U_1$ as the identity.
>
> **(2)** Let $x \in k^4$ and $s = x_1 + x_2 + x_3 + x_4$. Then $x = \frac{s}{4}(1, 1, 1, 1) + \big(x - \frac{s}{4}(1, 1, 1, 1)\big)$, and the second vector has coordinate sum $s - 4 \cdot \frac{s}{4} = 0$. So $k^4 = U_1 + V_2$. If $c\,(1, 1, 1, 1) \in V_2$, then $4c = 0$, so $c = 0$; hence $U_1 \cap V_2 = \{0\}$. Both steps use $4 \neq 0$ in $k$. The lecture remarks that the two subspaces are not complementary in characteristic $2$: there $(1, 1, 1, 1) \in V_2$.
>
> **(3)** The trace of a permutation matrix is the number of fixed points (Corollary [[§66 Invariant Vectors#^cor-66-11|§66.11]](1)): $4$ for $e$, $2$ for $(1\,2)$, $1$ for $(1\,2\,3)$, and $0$ for $(1\,2)(3\,4)$ and for $(1\,2\,3\,4)$. On the board, for $(1\,2)$:
>
> $$
> \rho_{k^4}\big((1\,2)\big) = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad \text{with trace } 2.
> $$
>
> **(4)** Characters add over direct sums (Proposition [[§67 Characters of Representations#^prop-67-2|§67.2]]), so $\chi_{V_2} = \chi_{k^4} - \chi_{U_1} = (4, 2, 1, 0, 0) - (1, 1, 1, 1, 1)$.

^pf-73-4

*Uses:* [[§66 Invariant Vectors#^cor-66-11|§66.11]], [[§67 Characters of Representations#^prop-67-2|§67.2]]

**Transcription note (board 11/23).** The board writes $V_2$ as $(1, 1, 1, 1)^\perp$, the vectors whose dot product with $(1, 1, 1, 1)$ is zero. This is the same subspace; the notation $U^\perp$ is used in these notes for an inner product over $\mathbb{R}$ (Definition [[§63 Invariant Inner Products and Maschke over ℝ#^def-63-2|§63.2]]) and for the annihilator (Definition [[§69 Dual Representations#^def-69-5|§69.5]]).

> [!theorem] Proposition §73.5: $V_2$ Is Simple
> For the representation $V_2$ of Proposition [[§73 The Character Table of S₄#^prop-73-4|§73.4]], $\langle \chi_2, \chi_2 \rangle = 1$. So $\dim\operatorname{Hom}_{S_4}(V_2, V_2) = 1$ and $V_2$ is simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]). Moreover $\langle \chi_2, \chi_0 \rangle = \langle \chi_2, \chi_1 \rangle = 0$.
>
> *Source: board 11/23*

^prop-73-5

> [!proof]+ Proof
> *(Board 11/23; the two sums for $\chi_0$ and $\chi_1$ are filled in.)* By Lemma [[§73 The Character Table of S₄#^lem-73-1|§73.1]](3),
>
> $$
> \langle \chi_2, \chi_2 \rangle = \tfrac{1}{24}\big(3^2 + 6 \cdot 1^2 + 8 \cdot 0^2 + 3 \cdot (-1)^2 + 6 \cdot (-1)^2\big) = \tfrac{1}{24}(9 + 6 + 3 + 6) = 1.
> $$
>
> By Corollary [[§71 The Character Table#^cor-71-4|§71.4]] this number is $\dim\operatorname{Hom}_{S_4}(V_2, V_2)$, and by the simplicity test (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]) $V_2$ is simple. The lecture adds that $\dim\operatorname{Hom}_G(V, V) = 1$ is equivalent to simplicity over $\mathbb{C}$ (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-12|§70.12]]) and implies it over every field containing $\mathbb{Q}$. The other two sums are
>
> $$
> \langle \chi_2, \chi_0 \rangle = \tfrac{1}{24}(3 + 6 + 0 - 3 - 6) = 0, \qquad \langle \chi_2, \chi_1 \rangle = \tfrac{1}{24}(3 - 6 + 0 - 3 + 6) = 0.
> $$

^pf-73-5

*Uses:* [[§73 The Character Table of S₄#^lem-73-1|§73.1]], [[§71 The Character Table#^cor-71-4|§71.4]], [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]], [[§70 Schur's Lemma and Multiplicities#^cor-70-12|§70.12]]

The lecture proposes two exercises, which are not done here: to prove directly from the definitions that $V_2$ is simple, and to carry the statements of this subsection over to $S_n$.

To find more rows, the lecture multiplies characters.

> [!theorem] Lemma §73.6: Products of Characters of $S_n$ Are Characters
> Let $V$ and $W$ be finite-dimensional representations of $S_n$ over a field $k$. Then the representation $\operatorname{Hom}(V, W)$ (Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]]) has the character
>
> $$
> \chi_{\operatorname{Hom}(V, W)}(\sigma) = \chi_V(\sigma)\,\chi_W(\sigma).
> $$
>
> *Source: lecture 11/23*

^lem-73-6

> [!proof]+ Proof
> *(Lecture 11/23.)* By The Character of $\operatorname{Hom}(V, W)$ (Proposition [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]]), $\chi_{\operatorname{Hom}(V, W)}(\sigma) = \chi_W(\sigma)\,\chi_V(\sigma^{-1})$, and $\chi_V(\sigma^{-1}) = \chi_V(\sigma)$ by Lemma [[§73 The Character Table of S₄#^lem-73-1|§73.1]](2).

^pf-73-6

*Uses:* [[§68 Homomorphisms Between Representations#^prop-68-5|§68.5]], [[§73 The Character Table of S₄#^lem-73-1|§73.1]]

The board also records $\chi_{V \otimes W}(g) = \chi_V(g)\,\chi_W(g)$ for the tensor product, which the course has met only in outline (the remark [[§69 Dual Representations#^rem-69-3|Tensor Products (Overview)]] in [[§69 Dual Representations|§69]]). For the three rows found so far, multiplying by $\chi_0$ changes nothing and $\chi_1^2 = \chi_0$. The products that can give something new are $\chi_1\chi_2$ and $\chi_2^2$.

> [!theorem] Lemma §73.7: Twisting by the Sign
> Let $V$ be a finite-dimensional representation of $S_n$ over a field $k$, and let $\mathrm{sign}$ be the sign representation (Example [[§61 Representations and Subrepresentations#^ex-61-2|§61.2]]).
>
> 1. The map $\operatorname{Hom}(\mathrm{sign}, V) \to V$, $\alpha \mapsto \alpha(1)$, is linear and bijective, and under it $\sigma$ acts on $V$ by $\operatorname{sgn}(\sigma)\,\rho_V(\sigma)$.
> 2. $\chi_{\operatorname{Hom}(\mathrm{sign}, V)}(\sigma) = \operatorname{sgn}(\sigma)\,\chi_V(\sigma)$.
> 3. $\operatorname{Hom}(\mathrm{sign}, V)$ is simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) if and only if $V$ is simple.
>
> *Source: lecture 11/23; parts (1) and (3) not from class*

^lem-73-7

> [!proof]+ Proof
> *(Part (2) is from the lecture of 11/23; parts (1) and (3) are filled in.)* **(1)** The sign representation is the vector space $k$ with $\sigma \cdot c = \operatorname{sgn}(\sigma)\,c$. A linear map $\alpha: k \to V$ is determined by the vector $\alpha(1)$, since $\alpha(c) = c\,\alpha(1)$, and every vector of $V$ occurs; so $\alpha \mapsto \alpha(1)$ is linear and bijective. By Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]],
>
> $$
> (\sigma \ast \alpha)(1) = \rho_V(\sigma)\big(\alpha(\operatorname{sgn}(\sigma^{-1}) \cdot 1)\big) = \operatorname{sgn}(\sigma^{-1})\,\rho_V(\sigma)\big(\alpha(1)\big) = \operatorname{sgn}(\sigma)\,\rho_V(\sigma)\big(\alpha(1)\big),
> $$
>
> because $\operatorname{sgn}(\sigma^{-1}) = \operatorname{sgn}(\sigma)^{-1} = \operatorname{sgn}(\sigma)$ for a number $\operatorname{sgn}(\sigma) = \pm 1$.
>
> **(2)** This is Lemma [[§73 The Character Table of S₄#^lem-73-6|§73.6]] with the character $\operatorname{sgn}$ of the sign representation.
>
> **(3)** By (1), the subrepresentations of $\operatorname{Hom}(\mathrm{sign}, V)$ correspond to the subspaces $U \subseteq V$ with $\operatorname{sgn}(\sigma)\,\rho_V(\sigma)U \subseteq U$ for all $\sigma$. Multiplying by $\pm 1$ maps a subspace to itself, so these are the subspaces with $\rho_V(\sigma)U \subseteq U$ for all $\sigma$, the subrepresentations of $V$. So one of the two representations has exactly two subrepresentations if and only if the other does.

^pf-73-7

*Uses:* [[§68 Homomorphisms Between Representations#^def-68-1|Def. §68.1]], [[§73 The Character Table of S₄#^lem-73-6|§73.6]]

> [!theorem] Proposition §73.8: The Representation $V_3 = \operatorname{Hom}(\mathrm{sign}, V_2)$
> Let $V_3 = \operatorname{Hom}(\mathrm{sign}, V_2)$, the representation $V_2$ of Proposition [[§73 The Character Table of S₄#^prop-73-4|§73.4]] twisted by the sign.
>
> 1. $\chi_3 = \chi_{V_3} = \chi_1\chi_2 = (3, -1, 0, -1, 1)$.
> 2. $V_3$ is simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]), and $\langle \chi_3, \chi_3 \rangle = 1$.
> 3. $\langle \chi_3, \chi_0 \rangle = \langle \chi_3, \chi_1 \rangle = \langle \chi_3, \chi_2 \rangle = 0$. In particular $V_3 \not\cong V_2$.
>
> *Source: lecture 11/23*

^prop-73-8

> [!proof]+ Proof
> *(Lecture 11/23; the three sums in (3) are left as a check in the lecture.)* **(1)** The character of $V_3$ is the product $\chi_1\chi_2$ (Lemma [[§73 The Character Table of S₄#^lem-73-7|§73.7]](2)): multiply the rows $(1, -1, 1, 1, -1)$ and $(3, 1, 0, -1, -1)$ entry by entry.
>
> **(2)** $V_2$ is simple (Proposition [[§73 The Character Table of S₄#^prop-73-5|§73.5]]), so $V_3$ is simple by Lemma [[§73 The Character Table of S₄#^lem-73-7|§73.7]](3). The entries of $\chi_3$ differ from those of $\chi_2$ only by signs, so the squares are the same and $\langle \chi_3, \chi_3 \rangle = \langle \chi_2, \chi_2 \rangle = 1$; this is the lecture's argument for simplicity, through Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]].
>
> **(3)** With the class sizes $1, 6, 8, 3, 6$:
>
> $$
> \begin{aligned} \langle \chi_3, \chi_0 \rangle &= \tfrac{1}{24}(3 - 6 + 0 - 3 + 6) = 0, \\ \langle \chi_3, \chi_1 \rangle &= \tfrac{1}{24}(3 + 6 + 0 - 3 - 6) = 0, \\ \langle \chi_3, \chi_2 \rangle &= \tfrac{1}{24}(9 - 6 + 0 + 3 - 6) = 0. \end{aligned}
> $$
>
> Since $\chi_3 \neq \chi_2$, the representations $V_3$ and $V_2$ are not isomorphic (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]).

^pf-73-8

*Uses:* [[§73 The Character Table of S₄#^lem-73-7|§73.7]], [[§73 The Character Table of S₄#^prop-73-5|§73.5]], [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]], [[§67 Characters of Representations#^lem-67-3|§67.3]]

> [!example] Example §73.3: $V_2$ and $V_3$ as Symmetries of the Tetrahedron and Rotations of the Cube
> In $k^3$ let
>
> $$
> q_1 = (1, 1, 1), \qquad q_2 = (1, -1, -1), \qquad q_3 = (-1, 1, -1), \qquad q_4 = (-1, -1, 1).
> $$
>
> These are four of the eight vertices $(\pm 1, \pm 1, \pm 1)$ of a cube, no two of them joined by an edge of the cube, and $q_1 + q_2 + q_3 + q_4 = 0$. For $k = \mathbb{R}$ they are the vertices of a regular tetrahedron. In $V_2$ let $p_i = e_i - \frac14(1, 1, 1, 1)$, so that $\sigma p_i = p_{\sigma(i)}$ and $p_1 + p_2 + p_3 + p_4 = 0$.
>
> 1. *$V_2$ in coordinates.* There is exactly one linear map $\beta: V_2 \to k^3$ with $\beta(p_i) = q_i$ for $i = 1, 2, 3, 4$, and it is bijective: $p_1, p_2, p_3$ is a basis of $V_2$ (every $x \in V_2$ is $\sum_i x_ip_i$, and $p_4 = -(p_1 + p_2 + p_3)$), $q_1, q_2, q_3$ is a basis of $k^3$ (the determinant of the matrix with these rows is $4$), and $\beta(p_4) = -\beta(p_1 + p_2 + p_3) = -(q_1 + q_2 + q_3) = q_4$. So $V_2$ is isomorphic to $k^3$ with $\sigma$ acting by the linear map that sends $q_i$ to $q_{\sigma(i)}$.
> 2. *The matrices.* The table lists this linear map for the representatives of the four classes other than $\{e\}$, and the map $\operatorname{sgn}(\sigma)\rho_{V_2}(\sigma)$ by which $\sigma$ acts on $V_3$ (Lemma [[§73 The Character Table of S₄#^lem-73-7|§73.7]](1)). The traces are the entries of $\chi_2$ and $\chi_3$.
> 3. *The geometry of $V_2$ for $k = \mathbb{R}$.* $(1\,2)$ is the reflection in the plane $y = -z$, which contains $q_3$ and $q_4$ and exchanges $q_1$ and $q_2$. $(1\,2\,3)$ is the rotation by $120^\circ$ about the line through $q_4$. $(1\,2)(3\,4)$ is the rotation by $180^\circ$ about the $x$-axis. $(1\,2\,3\,4)$ is the rotation by $90^\circ$ about the $y$-axis followed by the reflection $y \mapsto -y$. So $S_4$ acts on $V_2$ as the group of all symmetries of the regular tetrahedron.
> 4. *The geometry of $V_3$ for $k = \mathbb{R}$.* On $V_3$ every $\sigma$ acts with determinant $1$: $\det\rho_{V_2}(\sigma) = \operatorname{sgn}(\sigma)$, because the permutation matrix of $\sigma$ on $k^4 = U_1 \oplus V_2$ has determinant $\operatorname{sgn}(\sigma)$ (Theorem [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-2|§21.2]]) and $\sigma$ acts on $U_1$ as the identity; so $\det\big(\operatorname{sgn}(\sigma)\rho_{V_2}(\sigma)\big) = \operatorname{sgn}(\sigma)^3\operatorname{sgn}(\sigma) = 1$. The transposition $(1\,2)$ acts on $V_3$ as the rotation by $180^\circ$ about the line $x = 0$, $y = z$, and $(1\,2\,3\,4)$ as a rotation by $90^\circ$ about the $y$-axis. All these maps permute the eight vertices $\pm q_i$ of the cube, and different $\sigma$ give different maps: if $\operatorname{sgn}(\sigma)\rho_{V_2}(\sigma)$ is the identity, then $\rho_{V_2}(\sigma) = \pm\mathrm{id}$; the map $-\mathrm{id}$ does not permute the $q_i$, and $\rho_{V_2}(\sigma) = \mathrm{id}$ means $\sigma = e$. The cube has $24$ rotations (Proposition [[§32 Linear Groups, the Cube, S₃ and A₄#^prop-32-3|§32.3]]), so $S_4$ acts on $V_3$ by all of them. This gives the isomorphism of Theorem [[§32 Linear Groups, the Cube, S₃ and A₄#^thm-32-5|§32.5]] by explicit matrices.
> 5. *The three axes.* Each of the matrices permutes the three coordinate axes. The $x$-axis passes through the midpoints of the edges $q_1q_2$ and $q_3q_4$ of the tetrahedron, the $y$-axis through those of $q_1q_3$ and $q_2q_4$, the $z$-axis through those of $q_1q_4$ and $q_2q_3$. So the action on the three axes is the action of $S_4$ on the three ways of splitting $\{1, 2, 3, 4\}$ into two pairs (Proposition [[§43 Simple Groups#^prop-43-10|§43.10]]), and the double transpositions map each axis to itself.
>
> | $\sigma$ | $(x, y, z) \mapsto$ on $V_2$ | trace | $(x, y, z) \mapsto$ on $V_3$ | trace |
> |---|---|---|---|---|
> | $(1\,2)$ | $(x, -z, -y)$ | $1$ | $(-x, z, y)$ | $-1$ |
> | $(1\,2\,3)$ | $(y, -z, -x)$ | $0$ | $(y, -z, -x)$ | $0$ |
> | $(1\,2)(3\,4)$ | $(x, -y, -z)$ | $-1$ | $(x, -y, -z)$ | $-1$ |
> | $(1\,2\,3\,4)$ | $(z, -y, -x)$ | $-1$ | $(-z, y, x)$ | $1$ |
>
> *Source: not from class*

^ex-73-3

![[m493-73-2.svg]]

*(Not from lecture; figure added.)* Example [[§73 The Character Table of S₄#^ex-73-3|§73.3]] for $k = \mathbb{R}$: the tetrahedron with vertices $q_1, \ldots, q_4$ (marked $1, \ldots, 4$) inside the cube, and how the representatives of the four classes act on $V_2$. The three coordinate axes pass through the midpoints of opposite edges of the tetrahedron and are labelled by the corresponding splittings of $\{1, 2, 3, 4\}$ into two pairs.

## The Fifth Row and the Complete Table

> [!theorem] Proposition §73.9: Decomposing $\operatorname{Hom}(V_2, V_2)$: the Representation $V_4$
> Let $W = \operatorname{Hom}(V_2, V_2)$ (Definition [[§68 Homomorphisms Between Representations#^def-68-1|§68.1]]), a representation of $S_4$ of dimension $9$.
>
> 1. $\chi_W = \chi_2^2 = (9, 1, 0, 1, 1)$, and $\langle \chi_W, \chi_W \rangle = 4$.
> 2. $\langle \chi_W, \chi_0 \rangle = 1$,  $\langle \chi_W, \chi_1 \rangle = 0$,  $\langle \chi_W, \chi_2 \rangle = 1$,  $\langle \chi_W, \chi_3 \rangle = 1$.
> 3. $W \cong \mathrm{triv} \oplus V_2 \oplus V_3 \oplus V_4$, where $V_4$ is a simple representation (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) of dimension $2$ with $\langle \chi_4, \chi_4 \rangle = 1$ and with the character
>
> $$
> \chi_4 = \chi_{V_4} = \chi_2^2 - \chi_0 - \chi_2 - \chi_3 = (2, 0, -1, 2, 0).
> $$
>
> *Source: lecture 11/23*

^prop-73-9

> [!proof]+ Proof
> *Idea:* the pairing gives the multiplicities of the four known simple representations in $W$; they account for $7$ of the $9$ dimensions, and the rest is a new simple representation.
>
> *(Lecture 11/23; the bookkeeping with direct sums is filled in.)* **(1)** $\chi_W = \chi_2\chi_2$ by Lemma [[§73 The Character Table of S₄#^lem-73-6|§73.6]], and
>
> $$
> \langle \chi_W, \chi_W \rangle = \tfrac{1}{24}\big(81 + 6 \cdot 1^2 + 0 + 3 \cdot 1^2 + 6 \cdot 1^2\big) = \tfrac{96}{24} = 4.
> $$
>
> **(2)** With the class sizes $1, 6, 8, 3, 6$:
>
> $$
> \begin{aligned} \langle \chi_W, \chi_0 \rangle &= \tfrac{1}{24}(9 + 6 + 0 + 3 + 6) = 1, & \langle \chi_W, \chi_1 \rangle &= \tfrac{1}{24}(9 - 6 + 0 + 3 - 6) = 0, \\ \langle \chi_W, \chi_2 \rangle &= \tfrac{1}{24}(27 + 6 + 0 - 3 - 6) = 1, & \langle \chi_W, \chi_3 \rangle &= \tfrac{1}{24}(27 - 6 + 0 - 3 + 6) = 1. \end{aligned}
> $$
>
> **(3)** By Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], $W$ is isomorphic to a direct sum of simple representations. Those summands that are isomorphic to one of $\mathrm{triv}$, $\mathrm{sign}$, $V_2$, $V_3$ can be replaced by it, coordinate by coordinate as in the proof of Corollary [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]]; let $R$ be the direct sum of the remaining summands. Then
>
> $$
> W \cong \mathrm{triv}^{\oplus a_0} \oplus \mathrm{sign}^{\oplus a_1} \oplus V_2^{\oplus a_2} \oplus V_3^{\oplus a_3} \oplus R
> $$
>
> with integers $a_i \geq 0$. The four representations are simple and pairwise non-isomorphic, with $\langle \chi_i, \chi_i \rangle = 1$ (Example [[§73 The Character Table of S₄#^ex-73-2|§73.2]], Propositions [[§73 The Character Table of S₄#^prop-73-5|§73.5]] and [[§73 The Character Table of S₄#^prop-73-8|§73.8]]). So by Proposition [[§73 The Character Table of S₄#^prop-73-2|§73.2]](2) and by (2), $a_0 = 1$, $a_1 = 0$, $a_2 = 1$, $a_3 = 1$. On the board, as an identity of column vectors:
>
> $$
> \begin{pmatrix} 9 \\ 1 \\ 0 \\ 1 \\ 1 \end{pmatrix} = 1\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} + 0\begin{pmatrix} 1 \\ -1 \\ 1 \\ 1 \\ -1 \end{pmatrix} + 1\begin{pmatrix} 3 \\ 1 \\ 0 \\ -1 \\ -1 \end{pmatrix} + 1\begin{pmatrix} 3 \\ -1 \\ 0 \\ -1 \\ 1 \end{pmatrix} + \begin{pmatrix} 2 \\ 0 \\ -1 \\ 2 \\ 0 \end{pmatrix}.
> $$
>
> The last column is $\chi_R = \chi_W - \chi_0 - \chi_2 - \chi_3$ (Proposition [[§73 The Character Table of S₄#^prop-73-2|§73.2]](1)). Its first entry is $\dim R = 9 - 1 - 3 - 3 = 2$, so $R \neq \{0\}$. Finally
>
> $$
> \langle \chi_R, \chi_R \rangle = \tfrac{1}{24}\big(4 + 0 + 8 \cdot 1 + 3 \cdot 4 + 0\big) = 1,
> $$
>
> so $\dim\operatorname{Hom}_{S_4}(R, R) = 1$ (Corollary [[§71 The Character Table#^cor-71-4|§71.4]]) and $R$ is simple (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]). Put $V_4 = R$.

^pf-73-9

*Uses:* [[§73 The Character Table of S₄#^lem-73-6|§73.6]], [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]], [[§73 The Character Table of S₄#^ex-73-2|Ex. §73.2]], [[§73 The Character Table of S₄#^prop-73-5|§73.5]], [[§73 The Character Table of S₄#^prop-73-8|§73.8]], [[§73 The Character Table of S₄#^prop-73-2|§73.2]], [[§71 The Character Table#^cor-71-4|§71.4]], [[§70 Schur's Lemma and Multiplicities#^lem-70-11|§70.11]]

The value $\langle \chi_W, \chi_W \rangle = 4$ fits Proposition [[§73 The Character Table of S₄#^prop-73-2|§73.2]](3): $4 = 1^2 + 1^2 + 1^2 + 1^2$, four different simple representations, each once. The lecture uses it beforehand, to see that $W$ is not simple and that its multiplicities satisfy $a_1^2 + a_2^2 + \cdots = 4$. Over $\mathbb{C}$ the value $4 \neq 1$ shows at once that $W$ is not simple (Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-12|§70.12]]); over a general field containing $\mathbb{Q}$ this follows from part (3).

![[m493-73-3.svg]]

*(Not from lecture; figure added.)* Proposition [[§73 The Character Table of S₄#^prop-73-9|§73.9]](3) in matrices. In a basis of $\operatorname{Hom}(V_2, V_2)$ adapted to the decomposition, every $\sigma \in S_4$ acts by a block diagonal matrix with blocks of sizes $1$, $3$, $3$, $2$. The trace of the whole matrix is the sum of the traces of the blocks, which is the identity $\chi_2^2 = \chi_0 + \chi_2 + \chi_3 + \chi_4$.

> [!theorem] Theorem §73.10: The Character Table of $S_4$
> Let $k$ be a field containing $\mathbb{Q}$. The five representations $\mathrm{triv}$, $\mathrm{sign}$, $V_2$, $V_3$, $V_4$ of $S_4$ are simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) and pairwise non-isomorphic, each has $\dim\operatorname{Hom}_{S_4}(S, S) = 1$, and every finite-dimensional simple representation of $S_4$ over $k$ is isomorphic to exactly one of them. The character table (Definition [[§67 Characters of Representations#^def-67-2|§67.2]]) of $S_4$ is
>
> |  | representative | $e$ | $(1\,2)$ | $(1\,2\,3)$ | $(1\,2)(3\,4)$ | $(1\,2\,3\,4)$ |
> |---|---|---|---|---|---|---|
> |  | class size | $1$ | $6$ | $8$ | $3$ | $6$ |
> | $\chi_0$ | trivial | $1$ | $1$ | $1$ | $1$ | $1$ |
> | $\chi_1$ | sign | $1$ | $-1$ | $1$ | $1$ | $-1$ |
> | $\chi_2$ | $V_2$, coordinate sum $0$ in $k^4$ | $3$ | $1$ | $0$ | $-1$ | $-1$ |
> | $\chi_3$ | $V_3 = \operatorname{Hom}(\mathrm{sign}, V_2)$ | $3$ | $-1$ | $0$ | $-1$ | $1$ |
> | $\chi_4$ | $V_4$, from $S_3$ | $2$ | $0$ | $-1$ | $2$ | $0$ |
> |  | $k^4$, not simple | $4$ | $2$ | $1$ | $0$ | $0$ |
>
> *Source: lecture 11/23*

^thm-73-10

> [!proof]+ Proof
> *Idea:* five orthogonal rows in the five-dimensional space of class functions leave no room for a sixth.
>
> *(Lecture 11/23: “five orthogonal vectors in a five-dimensional space”; written out.)* The five representations are simple, with $\langle \chi_i, \chi_i \rangle = \dim\operatorname{Hom}_{S_4}(S, S) = 1$: Example [[§73 The Character Table of S₄#^ex-73-2|§73.2]], Propositions [[§73 The Character Table of S₄#^prop-73-5|§73.5]], [[§73 The Character Table of S₄#^prop-73-8|§73.8]] and [[§73 The Character Table of S₄#^prop-73-9|§73.9]]. Their characters are five different rows, so no two of them are isomorphic (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]). $S_4$ has $c = 5$ conjugacy classes (Example [[§73 The Character Table of S₄#^ex-73-1|§73.1]]), so by WS 18.4(2) (Corollary [[§71 The Character Table#^cor-71-7|§71.7]]) there are at most five pairwise non-isomorphic simple representations over $k$. Hence a simple representation $S$ is isomorphic to one of the five; and to only one, because being isomorphic is an equivalence relation (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](3)).

^pf-73-10

*Uses:* [[§73 The Character Table of S₄#^ex-73-2|Ex. §73.2]], [[§73 The Character Table of S₄#^prop-73-5|§73.5]], [[§73 The Character Table of S₄#^prop-73-8|§73.8]], [[§73 The Character Table of S₄#^prop-73-9|§73.9]], [[§67 Characters of Representations#^lem-67-3|§67.3]], [[§73 The Character Table of S₄#^ex-73-1|Ex. §73.1]], [[§71 The Character Table#^cor-71-7|§71.7]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]]

The lecture points out that the table, and the classification with it, is the same over every field of characteristic $0$. For $\mathbb{Z}/4\mathbb{Z}$ this was not so: it has three simple representations over $\mathbb{R}$ and four over $\mathbb{C}$ (Proposition [[§72 Representations of Cyclic Groups#^prop-72-10|§72.10]], Theorem [[§72 Representations of Cyclic Groups#^thm-72-5|§72.5]]).

> [!theorem] Corollary §73.11: Every Representation of $S_4$ Is Built from the Five
> Let $k$ be a field containing $\mathbb{Q}$ and $V$ a finite-dimensional representation of $S_4$ over $k$. Then
>
> $$
> V \cong \mathrm{triv}^{\oplus a_0} \oplus \mathrm{sign}^{\oplus a_1} \oplus V_2^{\oplus a_2} \oplus V_3^{\oplus a_3} \oplus V_4^{\oplus a_4}, \qquad a_i = \langle \chi_V, \chi_i \rangle.
> $$
>
> In matrices: if matrices $\rho(\sigma)$, $\sigma \in S_4$, multiply as the elements of $S_4$ do, then in a suitable basis they are all block diagonal at the same time (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]), with blocks of sizes $1$, $1$, $3$, $3$, $2$, each block being the matrix of $\sigma$ on one of the five simple representations.
>
> *Source: lecture 11/23*

^cor-73-11

> [!proof]+ Proof
> *(Lecture 11/23, as a comment on the table; written out.)* By Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], $V$ is isomorphic to a direct sum of simple representations, and by Theorem [[§73 The Character Table of S₄#^thm-73-10|§73.10]] each of them is isomorphic to one of the five; replace it by that one, as in the proof of Proposition [[§73 The Character Table of S₄#^prop-73-9|§73.9]](3). The multiplicities are $a_i = \langle \chi_V, \chi_i \rangle$ by Proposition [[§73 The Character Table of S₄#^prop-73-2|§73.2]](2), since $\langle \chi_i, \chi_i \rangle = 1$. An isomorphism from the direct sum to $V$ carries the bases of the summands, taken one after the other, to a basis of $V$ in which $V$ is an internal direct sum of subrepresentations isomorphic to the summands (Lemma [[§70 Schur's Lemma and Multiplicities#^lem-70-1|§70.1]]); in such a basis the matrices are block diagonal (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]).

^pf-73-11

*Uses:* [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], [[§73 The Character Table of S₄#^thm-73-10|§73.10]], [[§73 The Character Table of S₄#^prop-73-9|§73.9]], [[§73 The Character Table of S₄#^prop-73-2|§73.2]], [[§70 Schur's Lemma and Multiplicities#^lem-70-1|§70.1]], [[§62 Direct Sums and Maschke's Theorem#^prop-62-2|§62.2]]

## The Two-Dimensional Representation Comes from $S_3$

The representation $V_4$ was found as a leftover inside $\operatorname{Hom}(V_2, V_2)$. Its character tells what it is. The lecture starts from the entry $2$ in the column of $(1\,2)(3\,4)$: a matrix of order two in a two-dimensional representation with trace $2$.

> [!theorem] Lemma §73.12: An Element of Order Two with Trace $\dim V$ Acts as the Identity
> Let $V$ be a finite-dimensional representation of a group $G$ over a field $k$ containing $\mathbb{Q}$, and let $g \in G$ with $g^2 = e$. Put $V_+ = \{v \in V : gv = v\}$ and $V_- = \{v \in V : gv = -v\}$.
>
> 1. $V = V_+ \oplus V_-$. So $\rho_V(g)$ is diagonalizable, with eigenvalues among $1$ and $-1$.
> 2. $\chi_V(g) = \dim V_+ - \dim V_-$.
> 3. If $\chi_V(g) = \dim V$, then $\rho_V(g) = \mathrm{id}_V$.
>
> *Source: board 11/23*

^lem-73-12

> [!proof]+ Proof
> *(Board 11/23, for $g = (1\,2)(3\,4)$ and $V_4$: “$\rho(g)^2 = \mathrm{id}$, so $\rho(g)$ is diagonalizable with eigenvalues $\pm 1$; the trace is $2$, so the eigenvalues are $(1, 1)$”. Details filled in.)* Let $T = \rho_V(g)$, so $T^2 = \rho_V(g^2) = \mathrm{id}_V$.
>
> **(1)** Every $v \in V$ is $v = \frac12(v + Tv) + \frac12(v - Tv)$, and $T(v \pm Tv) = Tv \pm T^2v = \pm(v \pm Tv)$; so the first term lies in $V_+$ and the second in $V_-$. If $v \in V_+ \cap V_-$, then $v = Tv = -v$, so $2v = 0$ and $v = 0$. A basis of $V_+$ followed by a basis of $V_-$ is a basis of $V$ (Proposition [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]) consisting of eigenvectors of $T$.
>
> **(2)** In that basis the matrix of $T$ is diagonal, with $\dim V_+$ entries $1$ and $\dim V_-$ entries $-1$.
>
> **(3)** Let $p = \dim V_+$ and $q = \dim V_-$, so $\dim V = p + q$. By (2) the hypothesis says $p - q = p + q$ in $k$, that is, $2q = 0$ in $k$. A positive integer is not zero in a field containing $\mathbb{Q}$, so $q = 0$. Then $V = V_+$, and $T = \mathrm{id}_V$.

^pf-73-12

*Uses:* [[§62 Direct Sums and Maschke's Theorem#^prop-62-1|§62.1]]

> [!remark]- Connections
> - Linear Algebra: $T^2 = I$ says that $(x - 1)(x + 1)$ annihilates $T$, a product of distinct linear factors when $2 \neq 0$; diagonalizable by the minimal-polynomial criterion, [[§17 Diagonalizable Operators#^ladr-5-62|LADR 5.62]].
> - For any element of finite order over $\mathbb{C}$: [[§72 Representations of Cyclic Groups#^cor-72-8|Corollary §72.8]].

Over $\mathbb{C}$, part (1) is a case of Corollary [[§72 Representations of Cyclic Groups#^cor-72-8|§72.8]], with $N = 2$.

The lecture describes the result as a character of $S_3$ that is pulled back from the quotient. The construction is general.

> [!definition] Definition §73.1: Pullback of a Representation along a Homomorphism
> Let $\varphi: G \to H$ be a homomorphism of groups and $V$ a representation of $H$, given by $\rho_V: H \to GL(V)$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]). The **pullback** $\varphi^\ast V$ is the vector space $V$ with $g \in G$ acting by $\rho_V(\varphi(g))$. It is a representation of $G$, because $\rho_V \circ \varphi: G \to GL(V)$ is a homomorphism.
>
> *Source: lecture 11/23*

^def-73-1

> [!theorem] Lemma §73.13: The Character and the Subrepresentations of a Pullback
> Let $\varphi: G \to H$ be a homomorphism and $V$ a finite-dimensional representation of $H$, with pullback $\varphi^\ast V$ (Definition [[§73 The Character Table of S₄#^def-73-1|§73.1]]).
>
> 1. $\chi_{\varphi^\ast V}(g) = \chi_V(\varphi(g))$ for every $g \in G$.
> 2. Every element of $\operatorname{Ker}\varphi$ acts on $\varphi^\ast V$ as the identity.
> 3. If $\varphi$ is surjective, then $\varphi^\ast V$ and $V$ have the same subrepresentations; so $\varphi^\ast V$ is simple if and only if $V$ is simple.
>
> *Source: not from class*

^lem-73-13

> [!proof]+ Proof
> *(Not from class.)* **(1)** Both sides are the trace of the linear map $\rho_V(\varphi(g))$. **(2)** If $\varphi(g) = e$, then $g$ acts by $\rho_V(e) = \mathrm{id}_V$. **(3)** A subspace $U \subseteq V$ is a subrepresentation of $\varphi^\ast V$ if and only if $\rho_V(\varphi(g))U \subseteq U$ for all $g \in G$. When $\varphi$ is surjective, the elements $\varphi(g)$ are all the elements of $H$, so this says $\rho_V(h)U \subseteq U$ for all $h \in H$.

^pf-73-13

> [!theorem] Proposition §73.14: The Two-Dimensional Representation Comes from $S_3$
> Let $\rho: S_4 \to GL(V_4)$ be the representation $V_4$ of Proposition [[§73 The Character Table of S₄#^prop-73-9|§73.9]], and let $K = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ be the Klein four-group (Definition [[§39 Sources of Normal Subgroups#^def-39-1|§39.1]]).
>
> 1. $\operatorname{Ker}\rho = K$.
> 2. $\rho(S_4) \cong S_4/K \cong S_3$.
> 3. $V_4 \cong \alpha^\ast U$ (Definition [[§73 The Character Table of S₄#^def-73-1|§73.1]]), where $\alpha: S_4 \to S_3$ is the pair-partition homomorphism (Proposition [[§43 Simple Groups#^prop-43-10|§43.10]]) and $U = \{x \in k^3 : x_1 + x_2 + x_3 = 0\}$ is the two-dimensional simple representation of $S_3$, with character $(2, 0, -1)$ (Examples [[§67 Characters of Representations#^ex-67-1|§67.1]] and [[§70 Schur's Lemma and Multiplicities#^ex-70-2|§70.2]]). So $\chi_4(\sigma) = \chi_U(\alpha(\sigma))$, and the values $2$, $0$, $-1$ of $\chi_4$ are those of $\chi_U$.
>
> *Source: lecture 11/23*

^prop-73-14

> [!proof]+ Proof
> *Idea:* the character shows which elements act as the identity; the kernel is $K$, so the representation is one of $S_4/K \cong S_3$, and its character identifies it.
>
> *(Board 11/23; the proof of (3) is filled in.)* **(1)** Let $g = (1\,2)(3\,4)$. Then $g^2 = e$ and $\chi_4(g) = 2 = \dim V_4$, so $\rho(g) = \mathrm{id}$ by Lemma [[§73 The Character Table of S₄#^lem-73-12|§73.12]](3). The other two double transpositions have the same character value $2$ and also square to $e$, so they lie in $\operatorname{Ker}\rho$ as well; with $e$ this gives $K \subseteq \operatorname{Ker}\rho$. The elements of the other three classes have $\chi_4 = 0$, $-1$ or $0$, which is not the trace $2$ of the identity, so they are not in the kernel.
>
> **(2)** By the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]), $\rho(S_4) \cong S_4/\operatorname{Ker}\rho = S_4/K$, and $S_4/K \cong S_3$ by Proposition [[§43 Simple Groups#^prop-43-10|§43.10]]: $S_4$ acts on the three ways of splitting $\{1, 2, 3, 4\}$ into two pairs, with kernel $K$. The lecture describes the same action as the conjugation action of $S_4$ on the three double transpositions.
>
> **(3)** Number the three splittings $P_1 = \{1,2\},\{3,4\}$,  $P_2 = \{1,3\},\{2,4\}$,  $P_3 = \{1,4\},\{2,3\}$, so that $\alpha(\sigma)$ is a permutation of $\{1, 2, 3\}$. Then $\alpha(e) = e$ and $\alpha\big((1\,2)(3\,4)\big) = e$; $\alpha\big((1\,2)\big)$ fixes $P_1$ and exchanges $P_2$ and $P_3$, a transposition; $\alpha\big((1\,2\,3)\big)$ maps $P_1 \to P_3 \to P_2 \to P_1$, a $3$-cycle; and $\alpha\big((1\,2\,3\,4)\big)$ fixes $P_2$ and exchanges $P_1$ and $P_3$, a transposition. By Lemma [[§73 The Character Table of S₄#^lem-73-13|§73.13]](1) the character of $\alpha^\ast U$ on the five classes of $S_4$ is therefore
>
> $$
> \big(\chi_U(e),\ \chi_U(\text{transposition}),\ \chi_U(3\text{-cycle}),\ \chi_U(e),\ \chi_U(\text{transposition})\big) = (2, 0, -1, 2, 0) = \chi_4.
> $$
>
> Representations of $S_4$ over $k$ with the same character are isomorphic (Corollary [[§73 The Character Table of S₄#^cor-73-3|§73.3]]), so $V_4 \cong \alpha^\ast U$.

^pf-73-14

*Uses:* [[§73 The Character Table of S₄#^lem-73-12|§73.12]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]], [[§43 Simple Groups#^prop-43-10|§43.10]], [[§73 The Character Table of S₄#^lem-73-13|§73.13]], [[§73 The Character Table of S₄#^cor-73-3|§73.3]]

![[m493-73-1.svg]]

*(Board 11/23.)* The representation $V_4$ as a composite: the quotient map $S_4 \to S_4/K \cong S_3$, followed by the two-dimensional representation $U$ of $S_3$. On the board the upper arrow is marked with question marks and the right-hand arrow with $(1, 1, 1)^\perp$.

![[m493-73-4.svg]]

*(Not from lecture; figure added.)* The proof of Proposition [[§73 The Character Table of S₄#^prop-73-14|§73.14]](3). The three splittings of $\{1, 2, 3, 4\}$ into two pairs, and how the representatives of the five classes permute them. The representation $U$ of $S_3$ is the permutation representation $k^3$ without its trivial summand (Example [[§67 Characters of Representations#^ex-67-1|§67.1]]), so $\chi_U$ is the number of fixed points minus $1$. Hence $\chi_4(\sigma)$ is the number of splittings fixed by $\sigma$, minus $1$. The colours match the three axes of the figure after Example [[§73 The Character Table of S₄#^ex-73-3|§73.3]].

## Comments and the Regular Representation

> [!remark] Remark: Finding Representations in General
> Building the table of $S_4$ took some creativity: which representations to try, which characters to multiply. The lecture says that this is so in general. Working out the representations of the symmetric groups $S_n$ was a significant achievement, around 1900. For groups such as $GL_2(\mathbb{F}_p)$ and its relatives it was a major achievement of the twentieth century, for which the lecture names Deligne and Lusztig. For a given finite group the representation theory can be computed, but it is not something one usually hands to a computer.
>
> *Source: lecture 11/23*

^rem-73-1

The lecture ends with a representation, defined for every finite group, in which every simple representation occurs.

> [!definition] Definition §73.2: Regular Representation
> Let $G$ be a finite group. $G$ acts on the set $G$ by left multiplication, $g \star h = gh$; here $g$ is the group element and $h$ the element of the set. The **regular representation** $kG$ is the permutation representation (Definition [[§61 Representations and Subrepresentations#^def-61-2|§61.2]]) of this action: it has the basis $\{e_h : h \in G\}$, and $g \star e_h = e_{gh}$, extended linearly. For example, $g \star (e_h + 17\,e_{h'}) = e_{gh} + 17\,e_{gh'}$. Its dimension is $|G|$.
>
> *Source: lecture 11/23*

^def-73-2

That left multiplication is an action is checked in the proof of Cayley's Theorem (Theorem [[§25 Actions#^thm-25-5|§25.5]]). The lecture closes with two questions to think about over the break: what is the character of the regular representation, and why does every simple representation of $G$ occur in it. The lecture will come back to the regular representation after the break; the two questions are left open here.
