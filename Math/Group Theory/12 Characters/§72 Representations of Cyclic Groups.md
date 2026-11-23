---
type: section
subject: "[[Group Theory]]"
chapter: 12
section: 72
tags: [group-theory, math493]
---
← [[§71 The Character Table]] · ↑ [[· 12 Characters]] · [[§73 The Character Table of S₄]] →

*Source: Lecture (Fri Nov 20), from a handwritten page of the board; there was no worksheet.*

The cyclic group $\mathbb{Z}/N\mathbb{Z}$ is the first group for which all simple complex representations are found. A representation of $\mathbb{Z}/N\mathbb{Z}$ is one matrix $g$ with $g^N = \mathrm{Id}$. Over $\mathbb{C}$ there are $N$ one-dimensional representations, one for each $N$-th root of unity, and $\mathbb{Z}/N\mathbb{Z}$ has $N$ conjugacy classes. So by WS 18.4(2) (Corollary [[§71 The Character Table#^cor-71-7|§71.7]]) there are no further simple representations, and every complex representation is a direct sum of one-dimensional ones. In matrices: every complex matrix with $g^N = \mathrm{Id}$ is diagonalizable. This is WS 16.4, which Worksheet 16 left open (Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]]), and it gives $\operatorname{Tr}(g^{-1}) = \overline{\operatorname{Tr}(g)}$. The section ends with two other fields: over $\mathbb{R}$ the group $\mathbb{Z}/4\mathbb{Z}$ has only three simple representations, and in characteristic $p$ a matrix with $g^p = \mathrm{Id}$ need not be diagonalizable.

Throughout, $N \geq 1$ is an integer, and the elements of $\mathbb{Z}/N\mathbb{Z}$ are written $j = 0, 1, \ldots, N - 1$, with addition modulo $N$.

## A Representation of $\mathbb{Z}/N\mathbb{Z}$ Is One Matrix

> [!theorem] Proposition §72.1: A Representation of $\mathbb{Z}/N\mathbb{Z}$ Is a Matrix $g$ with $g^N = \mathrm{Id}$
> Let $k$ be a field and $n \geq 1$.
>
> 1. If $\rho: \mathbb{Z}/N\mathbb{Z} \to GL_n(k)$ is a representation of $\mathbb{Z}/N\mathbb{Z}$ on $k^n$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]) and $g = \rho(1)$, then $g^N = \mathrm{Id}$ and $\rho(j) = g^j$ for every $j$.
> 2. If $g$ is an $n \times n$ matrix over $k$ with $g^N = \mathrm{Id}$, then $g$ is invertible, and $\rho(j) = g^j$ is a well defined representation of $\mathbb{Z}/N\mathbb{Z}$ on $k^n$ with $\rho(1) = g$.
>
> So the representations of $\mathbb{Z}/N\mathbb{Z}$ on $k^n$ correspond one to one to the $n \times n$ matrices $g$ with $g^N = \mathrm{Id}$. The same holds for a representation on any vector space $V$, with a linear map $g: V \to V$ in place of the matrix.
>
> *Source: lecture 11/20*

^prop-72-1

> [!proof]+ Proof
> *Idea:* $1$ generates $\mathbb{Z}/N\mathbb{Z}$, so $\rho(1)$ determines $\rho$; and $N = 0$ in $\mathbb{Z}/N\mathbb{Z}$ forces $\rho(1)^N = \mathrm{Id}$.
>
> *(Board 11/20.)* **(1)** A representation on $k^n$ is a homomorphism $\rho: \mathbb{Z}/N\mathbb{Z} \to GL_n(k)$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]). So
>
> $$
> \rho(2) = \rho(1 + 1) = \rho(1)^2 = g^2, \qquad \rho(3) = \rho(1 + 1 + 1) = \rho(1)^3 = g^3, \qquad \ldots, \qquad \rho(j) = g^j,
> $$
>
> by induction on $j$, with $\rho(j + 1) = \rho(j)\rho(1) = g^jg$. Since $N = 0$ in $\mathbb{Z}/N\mathbb{Z}$, $g^N = \rho(N) = \rho(0) = \mathrm{Id}$. The board also notes why every $\rho(h)$ must be invertible: $\rho(h)\rho(h^{-1}) = \rho(hh^{-1}) = \rho(e) = \mathrm{Id}$.
>
> **(2)** $g \cdot g^{N-1} = g^N = \mathrm{Id}$, so $g$ is invertible with inverse $g^{N-1}$, and $g \in GL_n(k)$. The map $\varphi: \mathbb{Z} \to GL_n(k)$, $\varphi(j) = g^j$, is a homomorphism by the Exponent Laws (Lemma [[§4 Subgroups#^lem-4-4|§4.4]]), and $\varphi(N) = g^N = \mathrm{Id}$. By Descending a Map to $\mathbb{Z}/n\mathbb{Z}$ (Lemma [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]](2)) it descends to a homomorphism $\rho: \mathbb{Z}/N\mathbb{Z} \to GL_n(k)$ with $\rho(j) = g^j$. Explicitly, $g^{j + mN} = g^j(g^N)^m = g^j$, so $g^j$ depends only on $j$ modulo $N$. A homomorphism to $GL_n(k)$ is a representation on $k^n$ (Proposition [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]]).
>
> *One to one.* The two constructions are inverse to each other: starting from $g$, the representation $j \mapsto g^j$ has $\rho(1) = g$; starting from $\rho$, the matrix $g = \rho(1)$ gives back $j \mapsto g^j = \rho(j)$ by (1). The same proof works for linear maps $g: V \to V$ and homomorphisms to $GL(V)$.

^pf-72-1

*Uses:* [[§61 Representations and Subrepresentations#^prop-61-1|§61.1]], [[§4 Subgroups#^lem-4-4|§4.4]], [[§7 The Group ℤ∕nℤ#^lem-7-2|§7.2]]

> [!theorem] Lemma §72.2: Subrepresentations and Homomorphisms for $\mathbb{Z}/N\mathbb{Z}$
> Let $V$ and $W$ be representations of $\mathbb{Z}/N\mathbb{Z}$ over a field $k$, and let $g = \rho_V(1)$ and $h = \rho_W(1)$, so that $\rho_V(j) = g^j$ and $\rho_W(j) = h^j$ (Proposition [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]]).
>
> 1. A subspace $U \subseteq V$ is a subrepresentation (Definition [[§61 Representations and Subrepresentations#^def-61-3|§61.3]]) if and only if $gU \subseteq U$. In particular, for $v \neq 0$ the line $kv$ is a subrepresentation if and only if $v$ is an eigenvector of $g$.
> 2. A linear map $\alpha: V \to W$ is a homomorphism of representations (Definition [[§61 Representations and Subrepresentations#^def-61-4|§61.4]]) if and only if $\alpha g = h\alpha$.
> 3. For $V = W = k^n$, with matrices $g$ and $h$: the two representations are isomorphic (Definition [[§61 Representations and Subrepresentations#^def-61-5|§61.5]]) if and only if $h = SgS^{-1}$ for an invertible matrix $S$.
>
> *Source: not from class; the lecture of 11/20 uses it without comment*

^lem-72-2

> [!proof]+ Proof
> *(Not from class.)* **(1)** If $U$ is a subrepresentation, then $\rho_V(1)U \subseteq U$, which is $gU \subseteq U$. Conversely, if $gU \subseteq U$, then $g^jU \subseteq U$ for all $j \geq 0$ by induction, since $g^{j+1}U = g(g^jU) \subseteq gU \subseteq U$; so $U$ is preserved by every $\rho_V(j) = g^j$. For a line: $g(kv) \subseteq kv$ if and only if $gv = \lambda v$ for some $\lambda \in k$.
>
> **(2)** $\alpha$ is a homomorphism of representations if and only if $\alpha g^j = h^j\alpha$ for all $j$. The case $j = 1$ is $\alpha g = h\alpha$. Conversely, if $\alpha g = h\alpha$, then by induction $\alpha g^{j+1} = (\alpha g^j)g = h^j\alpha g = h^jh\alpha = h^{j+1}\alpha$.
>
> **(3)** An isomorphism from the representation given by $g$ to the one given by $h$ is an invertible matrix $S$ that is a homomorphism of representations. By (2) this means $Sg = hS$, which for invertible $S$ is $h = SgS^{-1}$.

^pf-72-2

## Roots of Unity and the One-Dimensional Complex Representations

From here on the field is $\mathbb{C}$, until the last subsection. The letter $k$ no longer denotes the field; as on the board, it is an index.

> [!definition] Definition §72.1: Root of Unity
> Let $N \geq 1$. A complex number $\zeta$ is an **$N$-th root of unity** if $\zeta^N = 1$.
>
> *Source: board 11/20*

^def-72-1

> [!theorem] Lemma §72.3: The $N$-th Roots of Unity
> Let $N \geq 1$.
>
> 1. The $N$-th roots of unity (Definition [[§72 Representations of Cyclic Groups#^def-72-1|§72.1]]) are exactly the $N$ numbers $e^{2\pi ik/N} = \cos\frac{2\pi k}{N} + i\sin\frac{2\pi k}{N}$ with $0 \leq k \leq N - 1$, and these are pairwise distinct. They are the powers $1, \omega, \omega^2, \ldots, \omega^{N-1}$ of $\omega = e^{2\pi i/N}$.
> 2. Every $N$-th root of unity $\zeta$ satisfies $|\zeta| = 1$ and $\zeta^{-1} = \overline{\zeta}$.
>
> *Source: board 11/20*

^lem-72-3

> [!proof]+ Proof
> *(Board 11/20: part (1), stated, with the picture for $N = 5$; part (2) is used on the board for the trace of $g^{-1}$; the proofs are not from class.)* *(Not from class.)* **(1)** Each of the numbers is an $N$-th root of unity: $\big(e^{2\pi ik/N}\big)^N = e^{2\pi ik} = 1$. They are pairwise distinct: $e^{i\theta} = \cos\theta + i\sin\theta$ is the point of the unit circle at the angle $\theta$, and the angles $2\pi k/N$ for $0 \leq k \leq N - 1$ are $N$ different angles in $[0, 2\pi)$. There are no others: the $N$-th roots of unity are the zeros of the polynomial $z^N - 1$ of degree $N$, which has at most $N$ zeros ([[§13 Polynomials#^ladr-4-8|Axler 4.8]]). Finally $e^{2\pi ik/N} = \big(e^{2\pi i/N}\big)^k = \omega^k$.
>
> **(2)** $|\zeta|^N = |\zeta^N| = 1$, and $|\zeta|$ is a nonnegative real number, so $|\zeta| = 1$. Then $\zeta\overline{\zeta} = |\zeta|^2 = 1$, so $\zeta^{-1} = \overline{\zeta}$.

^pf-72-3

> [!remark]- Connections
> - Complex Variables: the $n$th roots of any nonzero complex number, [[§10 Roots of Complex Numbers#^thm-10-2|342 Theorem §10.2]]; the $n$th roots of unity as the vertices of a regular polygon, [[§11 Examples (Roots of Complex Numbers)#^ex-11-2|342 Example §11.2]].

![[m493-72-1.svg]]

*(Board 11/20.)* The five $5$-th roots of unity: five points equally spaced on the unit circle, starting at $1$.

> [!theorem] Proposition §72.4: The One-Dimensional Complex Representations of $\mathbb{Z}/N\mathbb{Z}$
> For $0 \leq k \leq N - 1$ let
>
> $$
> \rho_k: \mathbb{Z}/N\mathbb{Z} \to GL_1(\mathbb{C}), \qquad \rho_k(j) = \big[e^{2\pi ijk/N}\big].
> $$
>
> Write $\mathbb{C}_k$ for the vector space $\mathbb{C}$ with this action, so that $j$ multiplies every vector of $\mathbb{C}_k$ by $e^{2\pi ijk/N}$.
>
> 1. $\mathbb{C}_k$ is a representation of $\mathbb{Z}/N\mathbb{Z}$, with character (Definition [[§67 Characters of Representations#^def-67-1|§67.1]]) $\chi_k(j) = e^{2\pi ijk/N}$.
> 2. $\mathbb{C}_k$ is simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]).
> 3. $\mathbb{C}_k \not\cong \mathbb{C}_l$ for $k \neq l$.
> 4. Every representation of $\mathbb{Z}/N\mathbb{Z}$ on $\mathbb{C}^1$ is equal to exactly one of $\rho_0, \ldots, \rho_{N-1}$.
>
> *Source: lecture 11/20*

^prop-72-4

> [!proof]+ Proof
> *(Lecture 11/20: for each $N$-th root of unity $\zeta$ there is a one-dimensional representation $\rho(j) = [\zeta^j]$; parts (2)–(4) are spelled out.)* *(Lecture 11/20; details filled in.)* **(1)** The number $\zeta = e^{2\pi ik/N}$ is an $N$-th root of unity (Lemma [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]](1)). So the $1 \times 1$ matrix $g = [\zeta]$ satisfies $g^N = [\zeta^N] = [1]$, and by Proposition [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]](2) the rule
>
> $$
> \rho(j) = g^j = [\zeta^j] = \big[e^{2\pi ijk/N}\big]
> $$
>
> is a representation. The trace of a $1 \times 1$ matrix is its entry.
>
> **(2)** $\mathbb{C}_k$ is one-dimensional, so its only subspaces are $\{0\}$ and $\mathbb{C}_k$, and these are different. So it has exactly two subrepresentations.
>
> **(3)** Isomorphic representations have the same character (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]). For $k \neq l$, $\chi_k(1) = e^{2\pi ik/N} \neq e^{2\pi il/N} = \chi_l(1)$ by Lemma [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]](1).
>
> **(4)** By Proposition [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]](1), a representation $\rho$ on $\mathbb{C}^1$ is $\rho(j) = g^j$ for a $1 \times 1$ matrix $g = [\zeta]$ with $\zeta^N = 1$. By Lemma [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]](1), $\zeta = e^{2\pi ik/N}$ for exactly one $k$ with $0 \leq k \leq N - 1$, and then $\rho = \rho_k$.

^pf-72-4

*Uses:* [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]], [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]], [[§67 Characters of Representations#^lem-67-3|§67.3]]

> [!example] Example §72.1: The Tables for $N = 5$ and $N = 4$
> $\mathbb{Z}/N\mathbb{Z}$ is abelian, so every element is central and every conjugacy class is a single element (Proposition [[§35 The Center#^prop-35-1|§35.1]]). The table of the characters $\chi_0, \ldots, \chi_{N-1}$ has one column for each $j \in \mathbb{Z}/N\mathbb{Z}$, and the entry in the row of $\chi_k$ is $e^{2\pi ijk/N}$.
>
> For $N = 5$ put $\alpha = e^{2\pi i/5}$, so that $\chi_k(j) = \alpha^{jk}$ and $\alpha^5 = 1$:
>
> | $N = 5$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> |---|---|---|---|---|---|
> | $\chi_0(j) = 1$ | $1$ | $1$ | $1$ | $1$ | $1$ |
> | $\chi_1(j) = \alpha^{j}$ | $1$ | $\alpha$ | $\alpha^2$ | $\alpha^3$ | $\alpha^4$ |
> | $\chi_2(j) = \alpha^{2j}$ | $1$ | $\alpha^2$ | $\alpha^4$ | $\alpha$ | $\alpha^3$ |
> | $\chi_3(j) = \alpha^{3j}$ | $1$ | $\alpha^3$ | $\alpha$ | $\alpha^4$ | $\alpha^2$ |
> | $\chi_4(j) = \alpha^{4j}$ | $1$ | $\alpha^4$ | $\alpha^3$ | $\alpha^2$ | $\alpha$ |
>
> For $N = 4$, $e^{2\pi i/4} = i$:
>
> | $N = 4$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|
> | $\chi_0(j) = 1$ (trivial) | $1$ | $1$ | $1$ | $1$ |
> | $\chi_1(j) = i^{j}$ | $1$ | $i$ | $-1$ | $-i$ |
> | $\chi_2(j) = (-1)^{j}$ | $1$ | $-1$ | $1$ | $-1$ |
> | $\chi_3(j) = (-i)^{j}$ | $1$ | $-i$ | $-1$ | $i$ |
>
> 1. *The entries for $N = 5$.* Exponents are reduced modulo $5$: for instance $\chi_2(3) = \alpha^6 = \alpha$ and $\chi_2(4) = \alpha^8 = \alpha^3$. The board fills in the first three rows; the last two are computed in the same way.
> 2. *Compared with the lecture of 11/18.* The rows $\chi_0$ and $\chi_2$ for $N = 4$ are the trivial representation and the representation $(-1)^k$ of Example [[§71 The Character Table#^ex-71-2|§71.2]]. The rows $\chi_1$ and $\chi_3$ are the further representations over $\mathbb{C}$ announced there. They are not defined over $\mathbb{R}$, since their values are not real.
> 3. *These are complete character tables.* By Proposition [[§72 Representations of Cyclic Groups#^prop-72-4|§72.4]] the rows belong to $N$ pairwise non-isomorphic simple representations, and by Theorem [[§72 Representations of Cyclic Groups#^thm-72-5|§72.5]] below there are no others. So each table is the character table of $\mathbb{Z}/N\mathbb{Z}$ over $\mathbb{C}$ in the sense of Definition [[§67 Characters of Representations#^def-67-2|§67.2]].
>
> *Source: board 11/20*

^ex-72-1

**Transcription note (board 11/20).** The board labels the rows of the table for $N = 5$ by $1$, $\alpha^k$, $\alpha^{2k}$, $\alpha^{3k}$, $\alpha^{4k}$ and the rows of the table for $N = 4$ by $1$, $i^k$, $(-1)^k$, $(-i)^k$, with $k$ for the group element. These notes write $j$ for the group element and keep $k$ for the number of the row, as in the board's formula $e^{2\pi ik/N}$.

![[m493-72-2.svg]]

*(Not from lecture; figure added.)* Two rows of the table for $N = 5$, with $\alpha = e^{2\pi i/5}$. The point marked $j$ is the value $\chi_k(j)$ on the unit circle. For $\chi_1$ each step from $j$ to $j + 1$ turns by $72^\circ$, for $\chi_2$ by $144^\circ$. Both walks visit the same five points, in different orders; this is why each row of the table is a rearrangement of $1, \alpha, \alpha^2, \alpha^3, \alpha^4$.

## All Simple Complex Representations of $\mathbb{Z}/N\mathbb{Z}$

> [!theorem] Theorem §72.5: The Simple Complex Representations of $\mathbb{Z}/N\mathbb{Z}$
> Every finite-dimensional simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) complex representation of $\mathbb{Z}/N\mathbb{Z}$ is isomorphic to exactly one of $\mathbb{C}_0, \mathbb{C}_1, \ldots, \mathbb{C}_{N-1}$ (Proposition [[§72 Representations of Cyclic Groups#^prop-72-4|§72.4]]). So, up to isomorphism, $\mathbb{Z}/N\mathbb{Z}$ has exactly $N$ finite-dimensional simple complex representations, as many as conjugacy classes (Definition [[§33 Conjugacy Classes#^def-33-1|§33.1]]), and all of them are one-dimensional.
>
> *Source: lecture 11/20*

^thm-72-5

> [!proof]+ Proof
> *Idea:* there are at most as many simple representations as conjugacy classes, and $N$ have been found.
>
> *(Board 11/20: “we just found $N = \#\operatorname{Conj}(\mathbb{Z}/N\mathbb{Z})$ non-isomorphic simple representations of $\mathbb{Z}/N\mathbb{Z}$”.)* $\mathbb{Z}/N\mathbb{Z}$ is abelian, so each of its conjugacy classes is a single element (Proposition [[§35 The Center#^prop-35-1|§35.1]]), and it has $c = N$ conjugacy classes. By Proposition [[§72 Representations of Cyclic Groups#^prop-72-4|§72.4]], $\mathbb{C}_0, \ldots, \mathbb{C}_{N-1}$ are $N$ pairwise non-isomorphic simple representations.
>
> Let $S$ be a finite-dimensional simple complex representation. If $S$ were isomorphic to none of the $\mathbb{C}_k$, then $\mathbb{C}_0, \ldots, \mathbb{C}_{N-1}, S$ would be $N + 1$ pairwise non-isomorphic simple representations over $\mathbb{C}$, a field containing $\mathbb{Q}$. This contradicts WS 18.4(2) (Corollary [[§71 The Character Table#^cor-71-7|§71.7]]), which allows at most $c = N$. So $S \cong \mathbb{C}_k$ for some $k$. If also $S \cong \mathbb{C}_l$, then $\mathbb{C}_k \cong \mathbb{C}_l$ (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](3)), so $k = l$ by Proposition [[§72 Representations of Cyclic Groups#^prop-72-4|§72.4]](3).

^pf-72-5

*Uses:* [[§35 The Center#^prop-35-1|§35.1]], [[§72 Representations of Cyclic Groups#^prop-72-4|§72.4]], [[§71 The Character Table#^cor-71-7|§71.7]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]]

For $\mathbb{Z}/N\mathbb{Z}$ over $\mathbb{C}$ the inequality of Corollary [[§71 The Character Table#^cor-71-7|§71.7]] is therefore an equality: the number of simple representations equals the number of conjugacy classes.

> [!theorem] Corollary §72.6: Every Complex Representation of $\mathbb{Z}/N\mathbb{Z}$ Is a Direct Sum of One-Dimensional Representations
> Let $V$ be a finite-dimensional complex representation of $\mathbb{Z}/N\mathbb{Z}$. Then there are integers $a_0, a_1, \ldots, a_{N-1} \geq 0$ with
>
> $$
> V \cong \mathbb{C}_0^{\oplus a_0} \oplus \mathbb{C}_1^{\oplus a_1} \oplus \cdots \oplus \mathbb{C}_{N-1}^{\oplus a_{N-1}}
> $$
>
> (external direct sum, Definitions [[§70 Schur's Lemma and Multiplicities#^def-70-1|§70.1]] and [[§70 Schur's Lemma and Multiplicities#^def-70-2|§70.2]]). For these integers,
>
> $$
> \chi_V = \sum_{k=0}^{N-1} a_k\,\chi_k, \qquad \dim V = \sum_{k=0}^{N-1} a_k.
> $$
>
> *Source: lecture 11/20*

^cor-72-6

> [!proof]+ Proof
> *(Lecture 11/20: “so every representation must be a direct sum of these”, for complex finite-dimensional representations.)* *(Lecture 11/20; details filled in.)* $|\mathbb{Z}/N\mathbb{Z}| = N \neq 0$ in $\mathbb{C}$, so by Corollary [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]] there are pairwise non-isomorphic simple representations $S_1, \ldots, S_r$ and positive integers $b_1, \ldots, b_r$ with $V \cong S_1^{\oplus b_1} \oplus \cdots \oplus S_r^{\oplus b_r}$. By Theorem [[§72 Representations of Cyclic Groups#^thm-72-5|§72.5]], each $S_i$ is isomorphic to $\mathbb{C}_{k(i)}$ for exactly one $k(i)$, and the numbers $k(1), \ldots, k(r)$ are different because the $S_i$ are pairwise non-isomorphic. Choose isomorphisms $\beta_i: \mathbb{C}_{k(i)} \to S_i$. Applying $\beta_i$ in every coordinate that belongs to $S_i$ gives a map $\bigoplus_i \mathbb{C}_{k(i)}^{\oplus b_i} \to \bigoplus_i S_i^{\oplus b_i}$ that is linear, bijective and commutes with the group, because all operations are coordinatewise; so the two sums are isomorphic. Put $a_{k(i)} = b_i$ and $a_k = 0$ for the other $k$. Then $V \cong \bigoplus_k \mathbb{C}_k^{\oplus a_k}$ (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](3)).
>
> Isomorphic representations have the same character (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]), and the character of an external direct sum is the sum of the characters (Proposition [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]]); this gives $\chi_V = \sum_k a_k\chi_k$. At $j = 0$ this reads $\dim V = \chi_V(0) = \sum_k a_k\chi_k(0) = \sum_k a_k$.

^pf-72-6

*Uses:* [[§70 Schur's Lemma and Multiplicities#^cor-70-3|§70.3]], [[§72 Representations of Cyclic Groups#^thm-72-5|§72.5]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]], [[§67 Characters of Representations#^lem-67-3|§67.3]], [[§70 Schur's Lemma and Multiplicities#^prop-70-2|§70.2]]

> [!theorem] Proposition §72.7: The Multiplicities $a_k$ from the Character
> In Corollary [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]], for $0 \leq k \leq N - 1$,
>
> $$
> a_k = \langle \chi_V, \chi_k \rangle = \frac{1}{N}\sum_{j=0}^{N-1} \chi_V(j)\,e^{-2\pi ijk/N},
> $$
>
> with the pairing of Definition [[§71 The Character Table#^def-71-2|§71.2]]. In particular the integers $a_k$ are determined by $V$, and two finite-dimensional complex representations of $\mathbb{Z}/N\mathbb{Z}$ with the same character are isomorphic.
>
> *Source: not from class*

^prop-72-7

> [!proof]+ Proof
> *(Not from class.)* The pairing is linear in the first entry (Proposition [[§71 The Character Table#^prop-71-3|§71.3]](1)), and the characters of the pairwise non-isomorphic simple complex representations $\mathbb{C}_l$ satisfy $\langle \chi_l, \chi_k \rangle = 1$ for $l = k$ and $0$ for $l \neq k$ (WS 18.3, Proposition [[§71 The Character Table#^prop-71-5|§71.5]](2)). So
>
> $$
> \langle \chi_V, \chi_k \rangle = \Big\langle \sum_{l=0}^{N-1} a_l\chi_l,\ \chi_k \Big\rangle = \sum_{l=0}^{N-1} a_l\,\langle \chi_l, \chi_k \rangle = a_k.
> $$
>
> *The formula.* Every conjugacy class of $\mathbb{Z}/N\mathbb{Z}$ has one element, and the inverse of $j$ is $-j$. So the pairing is $\langle \chi_V, \chi_k \rangle = \frac{1}{N}\sum_j \chi_V(-j)\chi_k(j)$. Replacing $j$ by $-j$, which runs through $\mathbb{Z}/N\mathbb{Z}$ as $j$ does, this is $\frac{1}{N}\sum_j \chi_V(j)\chi_k(-j) = \frac{1}{N}\sum_j \chi_V(j)\,e^{-2\pi ijk/N}$.
>
> *Same character.* If $\chi_V = \chi_W$, the formula gives the same integers $a_k$ for $V$ and for $W$, so both are isomorphic to $\bigoplus_k \mathbb{C}_k^{\oplus a_k}$, and $V \cong W$ (Lemma [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]](3)).

^pf-72-7

*Uses:* [[§71 The Character Table#^prop-71-3|§71.3]], [[§71 The Character Table#^prop-71-5|§71.5]], [[§61 Representations and Subrepresentations#^lem-61-5|§61.5]]

> [!theorem] Corollary §72.8: A Complex Matrix with $g^N = \mathrm{Id}$ Is Diagonalizable
> Let $g$ be an $n \times n$ complex matrix with $g^N = \mathrm{Id}_n$. Then there is an invertible matrix $S$ such that $SgS^{-1}$ is diagonal, and the diagonal entries are $N$-th roots of unity (Definition [[§72 Representations of Cyclic Groups#^def-72-1|§72.1]]). The root $e^{2\pi ik/N}$ occurs $a_k$ times, where the $a_k$ are the integers of Corollary [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]] for the representation $j \mapsto g^j$ on $\mathbb{C}^n$.
>
> *Source: lecture 11/20; WS 16.4(1)*

^cor-72-8

> [!proof]+ Proof
> *(Lecture 11/20; this is WS 16.4(1), Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]](1).)* *Idea:* a decomposition of $\mathbb{C}^n$ into one-dimensional representations is a basis of eigenvectors of $g$.
>
> *(Board 11/20: “so if $g^N = \mathrm{Id}_n$ there is a change of basis matrix $S$” with $SgS^{-1}$ diagonal, $N$-th roots of unity on the diagonal. The passage from the direct sum to $S$ is filled in.)* By Proposition [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]](2), $\rho(j) = g^j$ is a representation of $\mathbb{Z}/N\mathbb{Z}$ on $\mathbb{C}^n$. By Corollary [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]] there is an isomorphism of representations
>
> $$
> P: E = \mathbb{C}_0^{\oplus a_0} \oplus \cdots \oplus \mathbb{C}_{N-1}^{\oplus a_{N-1}} \to \mathbb{C}^n.
> $$
>
> The elements of $E$ are tuples of $\sum_k a_k = n$ complex numbers, so $E = \mathbb{C}^n$ as a vector space and $P$ is an invertible $n \times n$ matrix. The group acts on $E$ coordinate by coordinate (Definition [[§70 Schur's Lemma and Multiplicities#^def-70-1|§70.1]]): the element $1$ multiplies a coordinate that belongs to $\mathbb{C}_k$ by $e^{2\pi ik/N}$. So $1$ acts on $E$ by a diagonal matrix $D$, in which $e^{2\pi ik/N}$ occurs $a_k$ times. By Lemma [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]](3), applied to the isomorphism $P$ from the representation given by $D$ to the one given by $g$, $g = PDP^{-1}$. With $S = P^{-1}$, $SgS^{-1} = D$.

^pf-72-8

*Uses:* [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]], [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]], [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]], [[§70 Schur's Lemma and Multiplicities#^def-70-1|Def. §70.1]], [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]]

> [!remark]- Connections
> - Linear Algebra: diagonalizable means a basis of eigenvectors, [[§17 Diagonalizable Operators#^ladr-5-55|LADR 5.55]]; the minimal-polynomial criterion used in the second proof, [[§17 Diagonalizable Operators#^ladr-5-62|LADR 5.62]].
> - The same statement with its other proofs: WS 16.4, [[§68 Homomorphisms Between Representations#^prop-68-9|Proposition §68.9]], and PS 10.1, [[§68 Homomorphisms Between Representations#^prop-68-11|Proposition §68.11]].

> [!proof]+ Second proof (minimal polynomial)
> *(Not from class. This is the argument of Problem 10.1, written out in the proof of Proposition [[§68 Homomorphisms Between Representations#^prop-68-11|§68.11]](2).)* The polynomial $x^N - 1$ annihilates $g$, and it has $N$ distinct roots in $\mathbb{C}$ (Lemma [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]](1); alternatively, it has no root in common with its derivative $Nx^{N-1}$, whose only root $0$ is not a root of $x^N - 1$). The minimal polynomial of $g$ divides $x^N - 1$ ([[§15 The Minimal Polynomial#^ladr-5-29|Axler 5.29]]), so it is a product of distinct linear factors, and $g$ is diagonalizable ([[§17 Diagonalizable Operators#^ladr-5-62|Axler 5.62]]). The eigenvalues of $g$ are roots of its minimal polynomial ([[§15 The Minimal Polynomial#^ladr-5-27|Axler 5.27]]), hence roots of $x^N - 1$.

^pf-72-8-2

*Uses:* [[§68 Homomorphisms Between Representations#^prop-68-11|§68.11]], [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]]

These notes now contain three proofs that a complex matrix with $g^N = \mathrm{Id}$ is diagonalizable: by splitting off one eigenvector at a time with Maschke's theorem (the filled-in proof of Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]](1)), by the minimal polynomial (Problem 10.1, Proposition [[§68 Homomorphisms Between Representations#^prop-68-11|§68.11]](2)), and the lecture's, by counting the simple representations of $\mathbb{Z}/N\mathbb{Z}$. The lecture's proof does not use the other two: Corollary [[§71 The Character Table#^cor-71-7|§71.7]] rests on the orthogonality of the rows (Proposition [[§71 The Character Table#^prop-71-5|§71.5]](1)) and on Schur's Lemma, not on diagonalizing a matrix.

**The trace of the inverse (board 11/20).** Let $g^N = \mathrm{Id}_n$, and let $\lambda_1, \ldots, \lambda_n$ be the eigenvalues of $g$, the diagonal entries of $SgS^{-1}$. They are roots of unity, so $\lambda_j^{-1} = \overline{\lambda_j}$ (Lemma [[§72 Representations of Cyclic Groups#^lem-72-3|§72.3]](2)), and the board concludes

$$
\operatorname{Tr}(g) = \sum_j \lambda_j, \qquad \operatorname{Tr}(g^{-1}) = \sum_j \lambda_j^{-1} = \sum_j \overline{\lambda_j} = \overline{\operatorname{Tr}(g)}.
$$

This is WS 16.4(2) (Proposition [[§68 Homomorphisms Between Representations#^prop-68-9|§68.9]](2), where the steps are written out). Applied to $g = \rho_V(x)$ for an element $x$ of a finite group $G$, for which $\rho_V(x)^{|G|} = \mathrm{Id}$, it gives $\chi_V(x^{-1}) = \overline{\chi_V(x)}$, which is WS 16.5 (Corollary [[§68 Homomorphisms Between Representations#^cor-68-10|§68.10]]).

> [!example] Example §72.2: Rotation by $90^\circ$, Complexified
> Let $\mathbb{Z}/4\mathbb{Z}$ act on $\mathbb{R}^2$ by $j \mapsto J^j$ with $J = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, the representation $R$ of Example [[§71 The Character Table#^ex-71-2|§71.2]], which is simple over $\mathbb{R}$ (Example [[§71 The Character Table#^ex-71-3|§71.3]](1)). The same matrices act on $\mathbb{C}^2$, and $J^4 = \mathrm{Id}$, so Corollaries [[§72 Representations of Cyclic Groups#^cor-72-6|§72.6]] and [[§72 Representations of Cyclic Groups#^cor-72-8|§72.8]] apply with $N = 4$.
>
> 1. *The decomposition* (board). The vectors $\left(\begin{smallmatrix} 1 \\ i \end{smallmatrix}\right)$ and $\left(\begin{smallmatrix} 1 \\ -i \end{smallmatrix}\right)$ are eigenvectors of $J$, for the eigenvalues $-i$ and $i$: the board computes the first, and in the same way $J\left(\begin{smallmatrix} 1 \\ -i \end{smallmatrix}\right) = \left(\begin{smallmatrix} i \\ 1 \end{smallmatrix}\right) = i\left(\begin{smallmatrix} 1 \\ -i \end{smallmatrix}\right)$. So the two lines they span are subrepresentations (Lemma [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]](1)); they are the lines $L'$ and $L$ of Example [[§71 The Character Table#^ex-71-3|§71.3]]. On the board:
>
> $$
> \mathbb{C}^2 = \mathbb{C}\begin{pmatrix} 1 \\ i \end{pmatrix} \oplus \mathbb{C}\begin{pmatrix} 1 \\ -i \end{pmatrix}, \qquad \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ i \end{pmatrix} = \begin{pmatrix} -i \\ 1 \end{pmatrix} = (-i)\begin{pmatrix} 1 \\ i \end{pmatrix}.
> $$
>
> 2. *Which one-dimensional representations.* On $\mathbb{C}\left(\begin{smallmatrix} 1 \\ -i \end{smallmatrix}\right)$ the element $j$ acts by $i^j$, so this line is isomorphic to $\mathbb{C}_1$. On $\mathbb{C}\left(\begin{smallmatrix} 1 \\ i \end{smallmatrix}\right)$ it acts by $(-i)^j = i^{3j}$, so this line is isomorphic to $\mathbb{C}_3$. Hence $\mathbb{C}^2 \cong \mathbb{C}_1 \oplus \mathbb{C}_3$: the multiplicities are $a_0 = 0$, $a_1 = 1$, $a_2 = 0$, $a_3 = 1$.
> 3. *The characters* (board). The character of $J^j$ is the sum of two rows of the table for $N = 4$ (Example [[§72 Representations of Cyclic Groups#^ex-72-1|§72.1]]):
>
> $$
> (2, 0, -2, 0) = (1, -i, -1, i) + (1, i, -1, -i), \qquad \text{that is,} \quad \chi_R = \chi_3 + \chi_1.
> $$
>
> 4. *The multiplicities from the character* (check, not from class). By Proposition [[§72 Representations of Cyclic Groups#^prop-72-7|§72.7]], with $\chi_R = (2, 0, -2, 0)$,
>
> $$
> a_k = \tfrac14\big(2 \cdot 1 + 0 + (-2) \cdot i^{-2k} + 0\big) = \tfrac14\big(2 - 2(-1)^k\big) = \begin{cases} 0 & k = 0, 2, \\ 1 & k = 1, 3. \end{cases}
> $$
>
> 5. *The diagonal form* (not from class). With $P = \left(\begin{smallmatrix} 1 & 1 \\ -i & i \end{smallmatrix}\right)$, whose columns are the two eigenvectors, $P^{-1}JP = \left(\begin{smallmatrix} i & 0 \\ 0 & -i \end{smallmatrix}\right)$. So $S = P^{-1}$ in Corollary [[§72 Representations of Cyclic Groups#^cor-72-8|§72.8]].
>
> So a representation that is simple over $\mathbb{R}$ can split over $\mathbb{C}$.
>
> *Source: lecture 11/20; parts (2), (4) and (5) not from class*

^ex-72-2

![[m493-72-3.svg]]

*(Not from lecture; figure added.)* Part (3) of Example [[§72 Representations of Cyclic Groups#^ex-72-2|§72.2]], value by value. For each $j$ the blue arrow is $\chi_1(j) = i^j$ and the red arrow, drawn from its tip, is $\chi_3(j) = (-i)^j$, the complex conjugate. Their sum (orange dot) is real: $2$, $0$, $-2$, $0$. This is the character of the rotation representation $R$.

> [!theorem] Lemma §72.9: The Sum of the Powers of a Root of Unity
> Let $\zeta$ be an $N$-th root of unity (Definition [[§72 Representations of Cyclic Groups#^def-72-1|§72.1]]). Then
>
> $$
> \sum_{j=0}^{N-1} \zeta^j = \begin{cases} N & \text{if } \zeta = 1, \\ 0 & \text{if } \zeta \neq 1. \end{cases}
> $$
>
> *Source: not from class*

^lem-72-9

> [!proof]+ Proof
> *(Not from class.)* If $\zeta = 1$, every term is $1$. In general
>
> $$
> (\zeta - 1)\sum_{j=0}^{N-1} \zeta^j = \sum_{j=1}^{N} \zeta^j - \sum_{j=0}^{N-1} \zeta^j = \zeta^N - 1 = 0,
> $$
>
> so if $\zeta \neq 1$ the sum is $0$.

^pf-72-9

> [!remark]- Connections
> - Complex Variables: the same sum, $1 + c + \cdots + c^{n-1} = 0$ for an $n$th root of unity $c \neq 1$, [[§11 Examples (Roots of Complex Numbers)#^ex-11-2|342 Example §11.2]].

> [!example] Example §72.3: The Rows of the Table of $\mathbb{Z}/N\mathbb{Z}$ Are Orthonormal: a Direct Check
> By WS 18.3 over $\mathbb{C}$ (Proposition [[§71 The Character Table#^prop-71-5|§71.5]](2)), $\langle \chi_k, \chi_l \rangle$ is $1$ for $k = l$ and $0$ for $k \neq l$. For $\mathbb{Z}/N\mathbb{Z}$ this can be checked directly. The inverse of $j$ is $-j$, so
>
> $$
> \langle \chi_k, \chi_l \rangle = \frac{1}{N}\sum_{j=0}^{N-1} \chi_k(-j)\,\chi_l(j) = \frac{1}{N}\sum_{j=0}^{N-1} e^{2\pi ij(l - k)/N} = \frac{1}{N}\sum_{j=0}^{N-1} \zeta^j, \qquad \zeta = e^{2\pi i(l - k)/N}.
> $$
>
> Here $\zeta$ is an $N$-th root of unity, and $\zeta = 1$ exactly when $N$ divides $l - k$, that is, when $k = l$, since $|l - k| < N$. By Lemma [[§72 Representations of Cyclic Groups#^lem-72-9|§72.9]] the sum is $N$ for $k = l$ and $0$ for $k \neq l$. For $N = 5$, $k = 0$ and $l = 1$ this is $1 + \alpha + \alpha^2 + \alpha^3 + \alpha^4 = 0$: the entries of the row $\chi_1$ add up to zero, and so do the entries of every row except $\chi_0$.
>
> *Source: not from class*

^ex-72-3

![[m493-72-4.svg]]

*(Not from lecture; figure added.)* Lemma [[§72 Representations of Cyclic Groups#^lem-72-9|§72.9]] for $N = 5$, with $\alpha = e^{2\pi i/5}$. The powers of $\zeta$ are drawn head to tail, starting at $0$. Each arrow has length $1$ and is turned against the previous one by the angle of $\zeta$ ($72^\circ$ on the left, $144^\circ$ on the right). After five steps the path closes, so the sum is $0$.

## Other Fields: $\mathbb{R}$ and Characteristic $p$

Theorem [[§72 Representations of Cyclic Groups#^thm-72-5|§72.5]] is a statement about $\mathbb{C}$. The board of 11/18 announced what happens for $\mathbb{Z}/4\mathbb{Z}$ over $\mathbb{R}$ (Example [[§71 The Character Table#^ex-71-2|§71.2]](3)), and the lecture of 11/20 ended with an example in characteristic $p$.

> [!theorem] Proposition §72.10: The Simple Real Representations of $\mathbb{Z}/4\mathbb{Z}$
> Every finite-dimensional simple (Definition [[§65 Simple Representations#^def-65-1|§65.1]]) real representation of $\mathbb{Z}/4\mathbb{Z}$ is isomorphic to exactly one of the following three:
>
> 1. the trivial representation on $\mathbb{R}$ (Example [[§61 Representations and Subrepresentations#^ex-61-1|§61.1]]);
> 2. $\mathbb{R}$ with $j$ acting by $(-1)^j$;
> 3. $R = \mathbb{R}^2$ with $j$ acting by $J^j$, $J = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$.
>
> *Source: board 11/18*

^prop-72-10

> [!proof]+ Proof
> *(Board 11/18 (announced: the three rows of Example [[§71 The Character Table#^ex-71-2|§71.2]] are the only simple representations over $\mathbb{R}$); the proof is not from class.)* *Idea:* $g = \rho_V(1)$ satisfies $(g^2)^2 = \mathrm{id}$, so $V$ splits into the parts where $g^2 = 1$ and where $g^2 = -1$; a simple $V$ is one of the two.
>
> *(Not from class.)* Let $V$ be a finite-dimensional simple real representation and $g = \rho_V(1): V \to V$, so $g^4 = \mathrm{id}_V$ and the subrepresentations of $V$ are the subspaces $U$ with $gU \subseteq U$ (Proposition [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]], Lemma [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]](1)).
>
> *Step 1: $g^2 = \mathrm{id}_V$ or $g^2 = -\mathrm{id}_V$.* Put $V_+ = \{v \in V : g^2v = v\}$ and $V_- = \{v \in V : g^2v = -v\}$. These are subspaces, and $g$ maps each of them into itself, because $g$ commutes with $g^2$: for $v \in V_\pm$, $g^2(gv) = g(g^2v) = \pm gv$. So both are subrepresentations. Every $v \in V$ is the sum
>
> $$
> v = \tfrac12(v + g^2v) + \tfrac12(v - g^2v),
> $$
>
> where the first term lies in $V_+$ and the second in $V_-$, since $g^2(v \pm g^2v) = g^2v \pm g^4v = g^2v \pm v$. So $V = V_+ + V_-$. As $V$ is simple, $V_+$ is $\{0\}$ or $V$. If $V_+ = V$, then $g^2 = \mathrm{id}_V$. If $V_+ = \{0\}$, then $V = V_-$ and $g^2 = -\mathrm{id}_V$.
>
> *Step 2: the case $g^2 = \mathrm{id}_V$.* The same argument with $g$ in place of $g^2$: the subspaces $\{v : gv = v\}$ and $\{v : gv = -v\}$ are subrepresentations, and every $v$ is $\frac12(v + gv) + \frac12(v - gv)$ with the first term in the first subspace and the second in the second. So $g = \mathrm{id}_V$ or $g = -\mathrm{id}_V$. In both cases every subspace of $V$ is mapped into itself by $g$, so every subspace is a subrepresentation. Choose $v \neq 0$ in $V$ (a simple representation is not $\{0\}$). The line $\mathbb{R}v$ is a nonzero subrepresentation, so $\mathbb{R}v = V$. The map $\mathbb{R} \to V$, $c \mapsto cv$, is linear and bijective, and it commutes with the action when $j$ acts on $\mathbb{R}$ by $1$ (if $g = \mathrm{id}_V$) or by $(-1)^j$ (if $g = -\mathrm{id}_V$). So $V$ is isomorphic to (1) or to (2).
>
> *Step 3: the case $g^2 = -\mathrm{id}_V$.* Choose $v \neq 0$ in $V$ and let $U = \operatorname{span}(v, gv)$. Then $g(v) = gv \in U$ and $g(gv) = -v \in U$, so $gU \subseteq U$: $U$ is a nonzero subrepresentation, and $U = V$. The vectors $v$, $gv$ are linearly independent. Otherwise $gv = \lambda v$ for some $\lambda \in \mathbb{R}$, since $v \neq 0$; then $-v = g^2v = \lambda^2v$, so $\lambda^2 = -1$, which no real number satisfies. So $(v, gv)$ is a basis of $V$. The linear map
>
> $$
> \beta: \mathbb{R}^2 \to V, \qquad \beta(x, y) = xv + y\,gv,
> $$
>
> is bijective, and it satisfies $\beta J = g\beta$: $\beta(J(x, y)) = \beta(-y, x) = -yv + x\,gv$ and $g\beta(x, y) = x\,gv + y\,g^2v = x\,gv - yv$. By Lemma [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]](2), $\beta$ is an isomorphism of representations $R \to V$. So $V$ is isomorphic to (3).
>
> *Exactly one.* The three representations are simple: (1) and (2) are one-dimensional, and $R$ is simple by Problem 10.4(1) (Example [[§71 The Character Table#^ex-71-3|§71.3]](1)). Their characters are the three different rows $(1, 1, 1, 1)$, $(1, -1, 1, -1)$, $(2, 0, -2, 0)$ of Example [[§71 The Character Table#^ex-71-2|§71.2]], so no two of them are isomorphic (Lemma [[§67 Characters of Representations#^lem-67-3|§67.3]]).

^pf-72-10

*Uses:* [[§71 The Character Table#^ex-71-2|Ex. §71.2]], [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]], [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]], [[§71 The Character Table#^ex-71-3|Ex. §71.3]], [[§67 Characters of Representations#^lem-67-3|§67.3]]

> [!remark] Remark: $\mathbb{Z}/4\mathbb{Z}$ over $\mathbb{R}$ and over $\mathbb{C}$
> $\mathbb{Z}/4\mathbb{Z}$ has four conjugacy classes. Over $\mathbb{C}$ it has four simple representations, $\mathbb{C}_0, \mathbb{C}_1, \mathbb{C}_2, \mathbb{C}_3$ (Theorem [[§72 Representations of Cyclic Groups#^thm-72-5|§72.5]]); over $\mathbb{R}$ it has three (Proposition [[§72 Representations of Cyclic Groups#^prop-72-10|§72.10]]), so the inequality of WS 18.4(2) (Corollary [[§71 The Character Table#^cor-71-7|§71.7]]) is strict over $\mathbb{R}$. The trivial representation and $(-1)^j$ are $\mathbb{C}_0$ and $\mathbb{C}_2$, whose characters are real. The characters $\chi_1$ and $\chi_3$ are not real, and they are complex conjugates of each other; neither $\mathbb{C}_1$ nor $\mathbb{C}_3$ is defined over $\mathbb{R}$, but their sum is, and it is the simple real representation $R$ (Example [[§72 Representations of Cyclic Groups#^ex-72-2|§72.2]]). The weights in WS 18.3 (Proposition [[§71 The Character Table#^prop-71-5|§71.5]](1)) record this: $\langle \chi_R, \chi_R \rangle = \dim\operatorname{Hom}_G(R, R) = 2 = 1^2 + 1^2$.
>
> *Source: not from class*

^rem-72-1

> [!remark] Remark: In Characteristic $p$ a Matrix with $g^p = \mathrm{Id}$ Need Not Be Diagonalizable
> The lecture ended with $k = \mathbb{Z}/p\mathbb{Z}$ and $G = \mathbb{Z}/p\mathbb{Z}$, acting on $k^2$ by $j \mapsto \left(\begin{smallmatrix} 1 & j \\ 0 & 1 \end{smallmatrix}\right)$. Here $g = \left(\begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix}\right)$ satisfies $g^p = \left(\begin{smallmatrix} 1 & p \\ 0 & 1 \end{smallmatrix}\right) = \mathrm{Id}$, because $p = 0$ in $k$; so this is a representation by Proposition [[§72 Representations of Cyclic Groups#^prop-72-1|§72.1]](2). It is the representation of Problem 9.4(2) (Example [[§62 Direct Sums and Maschke's Theorem#^ex-62-4|§62.4]]): the line $ke_1$ is a subrepresentation without a complementary subrepresentation. In the terms of this section, $g^p = \mathrm{Id}$ but $g$ is not diagonalizable over $k$: its only eigenvalue is $1$, its eigenvectors are the multiples of $e_1$, and a basis of eigenvectors would contain a second invariant line (Lemma [[§72 Representations of Cyclic Groups#^lem-72-2|§72.2]](1)). So Corollary [[§72 Representations of Cyclic Groups#^cor-72-8|§72.8]] does not hold over $\mathbb{Z}/p\mathbb{Z}$. The hypotheses that fail are $|G| \neq 0$ in $k$ in Maschke's theorem (Theorem [[§62 Direct Sums and Maschke's Theorem#^thm-62-10|§62.10]]) and $\mathbb{Q} \subseteq k$ in Corollary [[§71 The Character Table#^cor-71-7|§71.7]]. The polynomial shows the difference: over $\mathbb{C}$, $x^N - 1$ has $N$ distinct roots, while over $\mathbb{Z}/p\mathbb{Z}$, $x^p - 1 = (x - 1)^p$ has the single root $1$.
>
> *Source: lecture 11/20*

^rem-72-2

*Source note.* Lecture 11/20; the board page ends in the middle of this example, and the comparison with $\mathbb{C}$ is not from class.
