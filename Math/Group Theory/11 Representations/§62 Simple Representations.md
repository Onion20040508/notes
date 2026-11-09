---
type: section
subject: "[[Group Theory]]"
chapter: 11
section: 62
tags: [group-theory, math493]
---
← [[§61 Invariant Inner Products and Maschke over ℝ]] · ↑ [[· 11 Representations]] · [[§63 Invariant Vectors]] →

*Source: Lecture (Fri Nov 6).*

> [!definition] Definition §62.1: Simple Representation
> Let $V$ be a representation of a group $G$. $V$ is **simple** if it has exactly two subrepresentations, $\{0\}$ and $V$.
> In particular $V \neq \{0\}$, since $\{0\}$ has only one subrepresentation, just as a simple group is nontrivial (Definition [[§43 Simple Groups#^def-43-1|§43.1]]).
>
> *Source: board 11/6*

^def-62-1

> [!definition] Definition §62.2: Irreducible Representation
> Let $V$ be a representation of a group $G$. $V$ is **irreducible** if $V \neq \{0\}$ and $V$ is not a direct sum $U_1 \oplus U_2$ (Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-1|§60.1]]) of two nonzero subrepresentations $U_1$, $U_2$.
> Many books call this notion *indecomposable* and use “irreducible” as a synonym for “simple”. In the lecture the two words are used interchangeably, which is justified under Maschke's hypotheses by Proposition [[§62 Simple Representations#^prop-62-1|§62.1]].
>
> *Source: board 11/6*

^def-62-2

> [!theorem] Proposition §62.1: Simple Equals Irreducible
> Let $G$ be finite and $V$ a finite-dimensional real representation of $G$ (more generally, a finite-dimensional representation over a field in which $|G| \neq 0$, by Maschke's theorem, Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]). Then $V$ is simple if and only if $V$ is irreducible.
>
> *Source: board 11/6*

^prop-62-1

> [!proof]+ Proof
> *Idea:* a nontrivial direct sum exhibits a third subrepresentation; conversely, Maschke's theorem turns a third subrepresentation into a nontrivial direct sum.
>
> Both notions require $V \neq \{0\}$ (Definitions [[§62 Simple Representations#^def-62-1|§62.1]] and [[§62 Simple Representations#^def-62-2|§62.2]]), so assume $V \neq \{0\}$.
>
> *Simple $\Rightarrow$ irreducible.* Suppose $V$ is not irreducible: $V = U_1 \oplus U_2$ with subrepresentations $U_1, U_2 \neq \{0\}$. Then $U_1 \neq V$: otherwise $U_2 = U_2 \cap V = U_2 \cap U_1 = \{0\}$. So $U_1$ is a subrepresentation different from $\{0\}$ and from $V$, and $V$ is not simple.
>
> *Irreducible $\Rightarrow$ simple.* Suppose $V$ is not simple. Since $V \neq \{0\}$, it has a subrepresentation $U$ with $\{0\} \subsetneq U \subsetneq V$. By Maschke's theorem over $\mathbb{R}$ (Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]]) there is a subrepresentation $U'$ with $V = U \oplus U'$, and $U' \neq \{0\}$, since otherwise $V = U + U' = U$. So $V$ is the direct sum of two nonzero subrepresentations, and $V$ is not irreducible.
>
> Only the second direction uses Maschke's theorem. Over a field in which $|G| \neq 0$, Maschke's theorem (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]) replaces Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]] there, and the argument is otherwise unchanged.

^pf-62-1

*Uses:* [[§62 Simple Representations#^def-62-1|Def. §62.1]], [[§62 Simple Representations#^def-62-2|Def. §62.2]], [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]], [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]

> [!definition] Definition §62.3: Direct Sum of Several Subspaces
> Let $V$ be a vector space and $V_1, \ldots, V_r$ subspaces of $V$. $V$ is the **direct sum** of $V_1, \ldots, V_r$, written $V = V_1 \oplus \cdots \oplus V_r$, if every $v \in V$ can be written in exactly one way as
>
> $$
> v = v_1 + \cdots + v_r \qquad (v_i \in V_i).
> $$
>
> For $r = 0$ the empty sum is $0$, so $V = \{0\}$.
>
> *Source: not from class; used in Corollary [[§62 Simple Representations#^cor-62-2|§62.2]]*

^def-62-3

> [!remark]- Connections
> - Linear Algebra: this is Axler's definition of a direct sum, [[§3 Subspaces#^ladr-1-41|LADR 1.41]]; for two subspaces, [[§3 Subspaces#^ladr-1-46|LADR 1.46]].

For $r = 2$ this is Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-1|§60.1]]. The existence of the sums says $V_1 + V_2 = V$. Uniqueness implies $V_1 \cap V_2 = \{0\}$: for $x \in V_1 \cap V_2$, $0 = 0 + 0 = x + (-x)$ are two ways of writing $0$, so $x = 0$; conversely, $V_1 \cap V_2 = \{0\}$ gives uniqueness by the paragraph after Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-1|§60.1]].

> [!theorem] Corollary §62.2: Every Representation Is a Direct Sum of Simples
> Let $G$ be finite and $V$ a finite-dimensional real representation of $G$. Then $V = V_1 \oplus \cdots \oplus V_r$ (Definition [[§62 Simple Representations#^def-62-3|§62.3]]) for simple subrepresentations $V_1, \ldots, V_r$ of $V$, with $r = 0$ when $V = \{0\}$.
>
> *Source: lecture 11/6*

^cor-62-2

> [!proof]+ Proof
> *Idea:* if $V$ is not simple already, split off a subrepresentation by Maschke's theorem and induct on the dimension.
>
> Induction on $\dim V$. If $V = \{0\}$, take $r = 0$. If $V$ is simple, take $r = 1$, $V_1 = V$.
>
> Otherwise $V \neq \{0\}$ is not simple, so it has a subrepresentation $U$ with $\{0\} \subsetneq U \subsetneq V$. By Maschke's theorem over $\mathbb{R}$ (Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]]), $V = U \oplus U'$ for a subrepresentation $U'$, and $U' \neq \{0\}$, since otherwise $V = U + U' = U$. By Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-1|§60.1]], $\dim V = \dim U + \dim U'$, and both dimensions are positive, so $\dim U, \dim U' < \dim V$. $U$ and $U'$ are finite-dimensional real representations of $G$ (with the restricted action), so by the induction hypothesis
>
> $$
> U = V_1 \oplus \cdots \oplus V_s, \qquad U' = V_{s+1} \oplus \cdots \oplus V_r
> $$
>
> with every $V_i$ a simple subrepresentation of $U$ or of $U'$, hence a $G$-stable subspace of $V$, i.e. a simple subrepresentation of $V$. It remains to show $V = V_1 \oplus \cdots \oplus V_r$.
>
> *Existence.* Let $v \in V$. Write $v = u + u'$ with $u \in U$, $u' \in U'$, then $u = v_1 + \cdots + v_s$ and $u' = v_{s+1} + \cdots + v_r$ with $v_i \in V_i$; so $v = v_1 + \cdots + v_r$.
>
> *Uniqueness.* Suppose $v_1 + \cdots + v_r = w_1 + \cdots + w_r$ with $v_i, w_i \in V_i$. Put $u = v_1 + \cdots + v_s$, $x = w_1 + \cdots + w_s$ (in $U$) and $u' = v_{s+1} + \cdots + v_r$, $x' = w_{s+1} + \cdots + w_r$ (in $U'$). Then $u + u' = x + x'$, so $u = x$ and $u' = x'$ by uniqueness in $V = U \oplus U'$ (the paragraph after Definition [[§60 Direct Sums and Maschke's Theorem#^def-60-1|§60.1]]). Uniqueness in $U = V_1 \oplus \cdots \oplus V_s$ and in $U' = V_{s+1} \oplus \cdots \oplus V_r$ then gives $v_i = w_i$ for every $i$.

^pf-62-2

*Uses:* [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]], [[§60 Direct Sums and Maschke's Theorem#^prop-60-1|§60.1]], [[§60 Direct Sums and Maschke's Theorem#^def-60-1|Def. §60.1]]

![[m493-61-2.svg]]

*(Not from lecture; figure added.)* The proof of Corollary [[§62 Simple Representations#^cor-62-2|§62.2]] as a tree, for a representation of dimension $5$. A piece that is not simple is split by Maschke's theorem into two subrepresentations of smaller dimension; the leaves are simple. In a basis made of bases of the leaves, every $\rho(g)$ is block diagonal, with one block per simple summand (Proposition [[§60 Direct Sums and Maschke's Theorem#^prop-60-2|§60.2]], applied at each split).

> [!theorem] Corollary §62.3: Every Representation Is a Direct Sum of Simples, over Any Field with $|G| \neq 0$
> Let $G$ be finite, $k$ a field in which $|G| \neq 0$, and $V$ a finite-dimensional representation of $G$ over $k$. Then $V = V_1 \oplus \cdots \oplus V_r$ (Definition [[§62 Simple Representations#^def-62-3|§62.3]]) for simple subrepresentations $V_1, \ldots, V_r$ of $V$, with $r = 0$ when $V = \{0\}$.
>
> *Source: not from class; available since PS 9.3 proves Maschke's theorem*

^cor-62-3

> [!proof]+ Proof
> *(Not from class.)* The proof of Corollary [[§62 Simple Representations#^cor-62-2|§62.2]] applies word for word after one renaming: “real representation” becomes “representation over $k$”, and Maschke's theorem over $\mathbb{R}$ (Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]]) becomes Maschke's theorem (Theorem [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]), proved in [[§60 Direct Sums and Maschke's Theorem|§60]] for every field in which $|G| \neq 0$. That citation is the only place where the field enters. Every other step uses only dimensions and direct sums, which work over any field.

^pf-62-3

*Uses:* [[§62 Simple Representations#^cor-62-2|§62.2]], [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]], [[§60 Direct Sums and Maschke's Theorem#^thm-60-10|§60.10]]

> [!example] Example §62.1: $S_3$ on $\mathbb{R}^3$ as a Sum of Simples
> $\mathbb{R}^3 = U \oplus V$, with $U = \mathbb{R}(1,1,1)$ and $V$ the sum-zero plane (Example [[§60 Direct Sums and Maschke's Theorem#^ex-60-1|§60.1]]), is a decomposition into simple representations, as in Corollary [[§62 Simple Representations#^cor-62-2|§62.2]].
>
> 1. *$U$ is simple:* it is one-dimensional, so its only subspaces are $\{0\}$ and $U$.
> 2. *$V$ is simple:* a subrepresentation $L$ with $\{0\} \subsetneq L \subsetneq V$ would be a line ($\dim V = 2$) with $gL \subseteq L$ for $g = (1\,2\,3)$, i.e. spanned by a real eigenvector of $\rho_V(g)$. In the orthonormal basis of Example [[§61 Invariant Inner Products and Maschke over ℝ#^ex-61-1|§61.1]], $\rho_V(g)$ is the rotation by $120^\circ$, whose characteristic polynomial $\lambda^2 + \lambda + 1$ has no real root. So there is no such $L$.
> 3. *Over $\mathbb{F}_3$ the decomposition fails:* there $(1,1,1)$ lies in the sum-zero plane (Proposition [[§59 Representations and Subrepresentations#^prop-59-3|§59.3]]).
>
> *Source: not from class*

^ex-62-1

![[m493-61-1.svg]]

*(Not from lecture; figure added.)* Part (2) of Example [[§62 Simple Representations#^ex-62-1|§62.1]] in the plane $V$, in the orthonormal basis $b_1, b_2$. The rotation $g = (1\,2\,3)$ moves every line $L$ through $0$ to a different line $gL$, so no line is a subrepresentation. A single element can preserve lines (the reflection $(1\,2)$ preserves the dotted axes $\mathbb{R}b_1$ and $\mathbb{R}b_2$), which is why a subrepresentation needs a common eigenvector of all the $\rho(g)$.

![[m493-61-a1.gif|600]]

*(Not from lecture; animation added, vault only.)* The rotation $g = (1\,2\,3)$ of the plane $V$, shown as a turn by $\theta$ from $0$ to $360^\circ$, applied to a line $L$. At $\theta = 120^\circ$ and $240^\circ$ (the elements $g$ and $g^2$) the line lands on the new lines $gL$ and $g^2L$; it returns to $L$ only after the full turn. A line through $0$ is mapped to itself only by turns of $0^\circ$ or $180^\circ$, so no line in $V$ is a subrepresentation.

> [!remark] Remark: Chemistry versus Fruit Salad
> Groups can be broken apart in several ways, each more special than the last: any normal subgroup $N$ splits $G$ into $N$ and $G/N$ ([[§40 Quotient Groups|§40]]); more special is a semidirect product ([[§58 Semidirect Products|§58]]); more special still a direct product ([[§57 Internal and External Direct Products|§57]]). For representations under Maschke's hypotheses these all coincide: there is no distinction between normal and non-normal subrepresentations, and every subrepresentation splits off as a direct summand (Corollary [[§61 Invariant Inner Products and Maschke over ℝ#^cor-61-6|§61.6]]). For the same reason the group analogue of irreducibility, not being a direct product of two nontrivial groups, is a much less useful notion than irreducibility of representations.
>
> An analogy: group theory is like chemistry, where one must learn the atoms (the simple groups, [[§43 Simple Groups|§43]]) and also how they bond ([[§50 Composition Series|§50]]); representation theory is like a fruit salad, where one only needs to know the fruits (the simple representations) and puts them in the bowl, with nothing connecting them. So most of representation theory is the study of the simple representations, and the main tool for that is **character theory**, the next topic of the course.
>
> *Source: lecture 11/6*

^rem-62-1

> [!remark] Remark: A Payoff in Group Theory
> Representation theory also proves theorems about groups. A first example: every finite group of order $p^a q^b$, with $p$ and $q$ prime, is solvable (Definition [[§48 Solvable Groups#^def-48-1|§48.1]]). Compare the groups of order $pq$ ([[§55 The Sylow Theorems|§55]]), which a problem set classifies as semidirect products of one cyclic group by another.
> *(Not from class.)* The result is Burnside's $p^aq^b$ theorem, not to be confused with Burnside's Lemma (Theorem [[§30 Orbit–Stabilizer#^thm-30-7|§30.7]]). Its proof uses characters of representations ([[§63 Invariant Vectors|§63]]) to find a proper nontrivial normal subgroup $N$, and finishes with Extensions of Solvable Groups Are Solvable (Theorem [[§48 Solvable Groups#^thm-48-7|§48.7]], PS 9.1): $N$ and $G/N$ have orders of the same form, so they are solvable by induction on $|G|$.
>
> *Source: lecture 11/6*

^rem-62-2

