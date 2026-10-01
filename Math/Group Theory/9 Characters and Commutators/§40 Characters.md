---
type: section
subject: "[[Group Theory]]"
chapter: 9
section: 40
tags: [group-theory, math493]
---
← [[§39 Simple Groups]] · ↑ [[· 9 Characters and Commutators]] · [[§41 Commutators]] →

*Reference: Not treated in Pinter (characters in this sense).*

> [!definition] Definition §40.1: Character
> Let $G$ be a group and $A$ an *abelian* group. A homomorphism $\chi: G \to A$ is called a **character** of $G$. The most common case is $A = k^\times$ for a field $k$.
>
> *Source: lecture, “for now”; PS 2*

^def-40-1

> [!example] Example §40.1: Characters
> 1. The sign $\operatorname{sgn} = \operatorname{sgn}: S_n \to \{\pm 1\}$ ([[§20 The Sign Homomorphism and the Alternating Group#^thm-20-3|§20.3]]) is a character of $S_n$, the target $\{\pm 1\}$ being abelian.
> 2. The determinant $\det: GL_n(k) \to k^\times$ is a character of $GL_n(k)$: $\det(AB) = \det A \det B$, and $k^\times$ is abelian.
> 3. For any $G$ and $A$, the **trivial character** $g \mapsto e_A$.
> 4. If $G$ is abelian, the identity map $G \to G$ is a character; so is any homomorphism between abelian groups, e.g. $\mathbb{Z}/4\mathbb{Z} \to U_5$, $k \mapsto 2^k$ ([[§16 Isomorphisms#^prop-16-7|§16.7]]).
>
> *Source: lecture*

^ex-40-1

> [!remark]- Connections
> - The multiplicativity in (2): [[§34 Determinants#^ladr-9-49|Determinant is multiplicative]] (LADR 9.49).

> [!remark] Remark: Why Characters
> A character takes the non-commutative multiplication of $G$ and maps it into a commutative group, where computation is much easier. The price is information: as shown below, a character cannot distinguish conjugate elements and sends every commutator to $e_A$, so it sees only the “abelian part” of $G$.

^rem-40-1

> [!remark] Remark: The Word “Character”
> The definition is explicitly provisional: the word will be used in a somewhat different sense later in the course. The standard later meaning, in representation theory, is the *trace* function $g \mapsto \operatorname{tr}\rho(g)$ of a representation $\rho: G \to GL_n(k)$; for $1$-dimensional representations $\rho: G \to GL_1(k) = k^\times$ the two notions agree, since the trace of a $1 \times 1$ matrix is its entry.

^rem-40-2

> [!theorem] Proposition §40.1: Characters Are Constant on Conjugacy Classes
> Let $\chi: G \to A$ be a character. If $g_1$ and $g_2$ lie in the same conjugacy class of $G$, then $\chi(g_1) = \chi(g_2)$.
>
> *Source: PS 2.4(1)*

^prop-40-1

> [!proof]+ Proof
> It suffices to show $\chi(hgh^{-1}) = \chi(g)$ for all $g, h \in G$, since elements of one conjugacy class are all conjugates of a common $g$. Using that $\chi$ is a homomorphism, that $A$ is abelian, and $\chi(e) = e_A$ ([[§15 Homomorphisms#^prop-15-1|§15.1]]):
>
> $$ \chi(hgh^{-1}) = \chi(h)\chi(g)\chi(h^{-1}) = \chi(h)\chi(h^{-1})\chi(g) = \chi(hh^{-1})\chi(g) = \chi(e)\chi(g) = \chi(g). $$

^pf-40-1

*Uses:* [[§40 Characters#^def-40-1|Def. §40.1]], [[§31 Conjugacy Classes#^def-31-1|Def. §31.1]], [[§15 Homomorphisms#^prop-15-1|§15.1]]

> [!remark]- Connections
> - Used in [[§41 Commutators#^thm-41-5|The Commutator Subgroup of Sₙ]] to pin down all characters of $S_n$.

> [!remark] Remark: Where Commutativity of $A$ Is Needed
> The middle step swaps $\chi(g)$ past $\chi(h^{-1})$, which requires $A$ abelian. For a homomorphism into a non-abelian target the conclusion fails: the identity map $S_3 \to S_3$ sends the conjugate elements $(1\,2)$ and $(1\,3)$ to different values. What survives in general is only that $\varphi$ carries conjugates to conjugates: $\varphi(hgh^{-1}) = \varphi(h)\varphi(g)\varphi(h)^{-1}$.

^rem-40-3

> [!theorem] Theorem §40.2: A Common Eigenvector Yields a Character
> Let $k$ be a field, $V$ a $k$-vector space, and let $G$ act on $V$ by linear maps — for instance $G$ a subgroup of $GL(V)$; in lecture, $k = \mathbb{C}$. Suppose $v \in V$ is nonzero and is an eigenvector of every $g \in G$, say $g v = \lambda(g)\,v$ for a scalar $\lambda(g) \in k$. Then $\lambda(g) \in k^\times$ for every $g$, and
>
> $$ \lambda: G \to k^\times $$
>
> is a group homomorphism, i.e. a character of $G$.
>
> *Source: lecture; PS 2.3(1)*

^thm-40-2

> [!proof]+ Proof
> **Values are nonzero.** If $\lambda(g) = 0$ then $gv = 0$, and applying $g^{-1}$ gives $v = g^{-1}(gv) = g^{-1}(0) = 0$ (each group element acts by a linear map, which sends $0$ to $0$, [[§7 Vector Space of Linear Maps#^ladr-3-10|LADR 3.10]]), contradicting $v \neq 0$. So $\lambda(g) \in k \setminus \{0\} = k^\times$.
>
> **Eigenvalues are determined.** If $av = bv$ with $a, b \in k$, then $(a - b)v = 0$; were $a - b \neq 0$, multiplying by $(a-b)^{-1}$ would give $v = 0$. So $a = b$: the scalar $\lambda(g)$ is uniquely determined by $g$, and $\lambda$ is a well-defined function.
>
> **Homomorphism.** For $g_1, g_2 \in G$, using linearity of $g_1$ and commutativity of $k$,
>
> $$ (g_1 g_2)v = g_1(g_2 v) = g_1\big(\lambda(g_2) v\big) = \lambda(g_2)\,(g_1 v) = \lambda(g_2)\lambda(g_1)\, v = \lambda(g_1)\lambda(g_2)\,v. $$
>
> On the other hand $(g_1g_2)v = \lambda(g_1g_2)v$ by definition of $\lambda$ at $g_1 g_2 \in G$. Comparing and cancelling $v$ gives $\lambda(g_1 g_2) = \lambda(g_1)\lambda(g_2)$.

^pf-40-2

*Uses:* [[§23 Actions#^def-23-1|Def. §23.1]], [[§7 Vector Space of Linear Maps#^ladr-3-10|LADR 3.10]], [[§3 Basic Examples of Groups#^def-3-4|Def. §3.4]], [[§40 Characters#^def-40-1|Def. §40.1]]

> [!remark]- Connections
> - Eigenvectors in linear algebra: [[§14 Invariant Subspaces#^ladr-5-8|Eigenvector]] (LADR 5.8); here one vector is an eigenvector of every operator in $G$ simultaneously.

> [!example] Example §40.2: $\Delta$ and the Sign Character
> Let $V$ be the space of homogeneous polynomials of degree $\binom{n}{2}$ in $x_1, \ldots, x_n$ over $k$, with $S_n \subseteq GL(V)$ acting by permuting variables ([[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-3|Def. §19.3]]). Take
>
> $$ \Delta = \prod_{1 \leq i < j \leq n}(x_i - x_j). $$
>
> Expanding, each monomial picks one variable from each of the $\binom{n}{2}$ brackets, so $\Delta$ is homogeneous of degree $\binom{n}{2}$ and lies in $V$. By [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-2|§20.2]], $\sigma \cdot \Delta = \operatorname{sgn}(\sigma)\,\Delta$ for every $\sigma \in S_n$, so $\Delta$ is a common eigenvector and the resulting character is the sign:
>
> $$ \lambda = \operatorname{sgn}: S_n \to k^\times, \qquad \lambda(\sigma) = (-1)^{\operatorname{inv}(\sigma)} \in \{\pm 1\}. $$
>
> Consistently with [[§40 Characters#^thm-40-2|the theorem]], its values are nonzero.
>
> This is the lecture's explanation of a fact that is a genuine surprise from the inversion-count definition $\operatorname{sgn}(\sigma) = (-1)^{\#\{(i,j) : i < j,\ \sigma(i) > \sigma(j)\}}$ alone: counting inversions gives no visible reason for $\operatorname{sgn}(\sigma\tau) = \operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$, but reading the sign as an eigenvalue on the common eigenvector $\Delta$ makes multiplicativity automatic.
>
> *Source: lecture; PS 2.3(2)*

^ex-40-2

> [!remark] Remark: One-Dimensional Representations
> A character $G \to k^\times = GL_1(k)$ is precisely a $1$-dimensional representation of $G$. [[§40 Characters#^thm-40-2|The theorem]] says that a line in $V$ fixed by all of $G$ (a common eigenvector spans one) carves a $1$-dimensional representation out of a larger one. For $S_n$ acting on polynomials, the line spanned by $\Delta$ gives the sign; the line spanned by any symmetric polynomial gives the trivial character $\sigma \mapsto 1$. Decomposing a representation into such pieces is the central problem of the second half of the course.

^rem-40-4
