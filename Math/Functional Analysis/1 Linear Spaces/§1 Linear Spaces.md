---
type: section
subject: "[[Functional Analysis]]"
chapter: 1
section: 1
tags: [functional-analysis, math556]
---
↑ [[· 1 Linear Spaces]] · [[§2 Quotient Spaces and Complements]] →

*Stage: algebra — Threads: dimension. The vocabulary of the course; only finite sums exist ([[§1 Linear Spaces#Linear Span|§1]]).*

## Definition and Examples

Throughout, $\mathbb{F}$ denotes the scalar field, which is always $\mathbb{R}$ or $\mathbb{C}$.

> [!definition] Definition §1.1: Linear Space
> We say $X$ is a **linear space** (or **vector space**) over the field $\mathbb{F}$ ($= \mathbb{R}$ or $\mathbb{C}$) if there are two operations on $X$, an addition
>
> $$
> + : X \times X \to X, \qquad (x, y) \mapsto x + y,
> $$
>
> and a scalar multiplication
>
> $$
> \cdot : \mathbb{F} \times X \to X, \qquad (k, x) \mapsto kx,
> $$
>
> together with a distinguished element $0 \in X$, satisfying:
> - (1) $x + y = y + x$ for all $x, y \in X$ (commutativity)
> - (2) $(x + y) + z = x + (y + z)$ for all $x, y, z \in X$ (associativity)
> - (3) $x + 0 = x$ for all $x \in X$ (additive identity)
> - (4) for every $x \in X$ there is an element $-x \in X$ with $x + (-x) = 0$ (additive inverse)
> - (5) $k(ax) = (ka)x$ for all $k, a \in \mathbb{F}$, $x \in X$
> - (6) $k(x + y) = kx + ky$ for all $k \in \mathbb{F}$, $x, y \in X$
> - (7) $(a + b)x = ax + bx$ for all $a, b \in \mathbb{F}$, $x \in X$
> - (8) $1x = x$ for all $x \in X$.
>
> *Lax: Ch. 1, axioms for a linear space*

^def-1-1

> [!remark]- Connections
> - The same definition in linear algebra: [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]; in measure theory: [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-1|551 Def. §34.1]].
> - Computational version: [[§29 Vector Spaces and Subspaces#^def-29-1|235 Def. §29.1]] (the same axioms over ℝ, with worked examples of function and polynomial spaces).

> [!remark] Remark
> The two operations are *closed*: adding two elements of $X$, or multiplying an element of $X$ by a scalar, produces an element of $X$. This is the content of writing $+ : X \times X \to X$ and $kx \in X$ for all $k \in \mathbb{F}$, and is the property that must be checked first when verifying that a given set is a linear space.

^rem-1-1

> [!example] Example §1.1: $\mathbb{R}^n$
> $\mathbb{R}^n$ is a linear space over $\mathbb{R}$ with componentwise addition and scalar multiplication. It is $n$-dimensional: it has a basis, and every vector is a finite linear combination of basis vectors.

^ex-1-1

## Linear Subspaces

> [!definition] Definition §1.2: Linear Subspace
> Let $X$ be a linear space and $Y \subset X$. We say $Y$ is a **(linear) subspace** of $X$ if
> - (i) $y_1 + y_2 \in Y$ for all $y_1, y_2 \in Y$, and
> - (ii) $ky \in Y$ for all $y \in Y$, $k \in \mathbb{F}$.
>
> In other words, $Y$ is a subset of $X$ that is itself a linear space under the operations inherited from $X$.
>
> *Lax: Ch. 1, definition of linear subspace*

^def-1-2

> [!remark]- Connections
> - Subspaces in linear algebra: [[§3 Subspaces#^ladr-1-33|LADR 1.33]], with the conditions [[§3 Subspaces#^ladr-1-34|LADR 1.34]].
> - Computational version: [[§29 Vector Spaces and Subspaces#^def-29-2|235 Def. §29.2]] (the three subspace conditions, with examples and non-examples).

> [!theorem] Proposition §1.1: Subspaces Contain the Origin
> Every linear subspace $Y$ of $X$ contains $0$.

^prop-1-1

> [!proof]+ Proof
> A subspace is nonempty by convention. Take any $y \in Y$; then $0 = 0 \cdot y \in Y$ by (ii).

^pf-1-1

*Uses:* [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]]

> [!remark] Remark
> Geometrically, in $\mathbb{R}^3$ the subspaces are the origin, lines through the origin, planes through the origin, and $\mathbb{R}^3$ itself. A plane not passing through the origin is *not* a subspace.

^rem-1-2

> [!remark] Note: Notation
> The inclusion $Y \subset X$ allows equality; $X$ is a subspace of itself. Strict inclusion, when it matters, is written $Y \subsetneq X$.

^rem-1-3

## Sums and Direct Sums

> [!definition] Definition §1.3: Sum of Subsets
> Let $X$ be a linear space and $S, T \subset X$ be subsets (not necessarily subspaces). The **sum** of $S$ and $T$ is
>
> $$
> S + T = \{ s + t \mid s \in S,\ t \in T \}.
> $$
>
> *Lax: Ch. 1, sum of subsets*

^def-1-3

> [!theorem] Proposition §1.2: Sum of Subspaces
> If $S$ and $T$ are linear subspaces of $X$, then $S + T$ is a linear subspace of $X$.
>
> *Lax: Ch. 1, Thm 1(ii)*

^prop-1-2

> [!proof]+ Proof
> Let $s_1 + t_1, s_2 + t_2 \in S + T$ with $s_i \in S$, $t_i \in T$, and $k \in \mathbb{F}$. Then
>
> $$
> (s_1 + t_1) + (s_2 + t_2) = (s_1 + s_2) + (t_1 + t_2) \in S + T, \qquad k(s_1 + t_1) = ks_1 + kt_1 \in S + T,
> $$
>
> since $s_1 + s_2, ks_1 \in S$ and $t_1 + t_2, kt_1 \in T$.

^pf-1-2

*Uses:* [[§1 Linear Spaces#^def-1-3|Def. §1.3]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]]

> [!remark]- Connections
> - Sums of subspaces in linear algebra: [[§3 Subspaces#^ladr-1-36|LADR 1.36]], and the sum is the smallest containing subspace, [[§3 Subspaces#^ladr-1-40|LADR 1.40]].

> [!definition] Definition §1.4: Direct Sum
> Let $X, Y$ be linear spaces over the same field. The **direct sum** of $X$ and $Y$, written $X \oplus Y$, is
>
> $$
> X \oplus Y = \{ (x, y) \mid x \in X,\ y \in Y \},
> $$
>
> with componentwise operations $(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)$ and $k(x, y) = (kx, ky)$.
>
> *Lax: Ch. 1, direct sum*

^def-1-4

> [!remark]- Connections
> - This external direct sum is Axler's product of vector spaces: [[§11 Products and Quotients of Vector Spaces#^ladr-3-87|LADR 3.87]], a vector space by [[§11 Products and Quotients of Vector Spaces#^ladr-3-89|LADR 3.89]].

> [!example] Example §1.2: $\mathbb{R} \oplus \mathbb{R}^2 = \mathbb{R}^3$
> An element of $\mathbb{R} \oplus \mathbb{R}^2$ is a pair $(a, (b, c))$ with $a \in \mathbb{R}$ and $(b, c) \in \mathbb{R}^2$; identifying it with $(a, b, c)$ gives $\mathbb{R} \oplus \mathbb{R}^2 = \mathbb{R}^3$.

^ex-1-2

> [!remark] Remark: Direct Sum vs. Sum; Comparison with Axler
> The direct sum $X \oplus Y$ is a set of *pairs*; it is what other texts call the (external) direct sum or the product $X \times Y$. It is defined for any two linear spaces, which need not sit inside a common ambient space. By contrast, $S + T$ is a set of *vectors* in a fixed ambient space $X$.
>
> This differs from the definition in Axler, where the direct sum $U_1 \oplus U_2$ is an *internal* notion: it is the sum $U_1 + U_2$ of two subspaces of a common space, with the extra requirement that every element decomposes uniquely as $u_1 + u_2$. The convention here follows Lax. When the two internal summands are subspaces of a common $X$ with $U_1 \cap U_2 = \{0\}$, the two notions agree up to the isomorphism $(u_1, u_2) \mapsto u_1 + u_2$ (Proposition [[§1 Linear Spaces#^prop-1-3|§1.3]] below), but the course uses the external definition throughout.

^rem-1-4

> [!theorem] Proposition §1.3: Internal and External Direct Sums
> Let $U$ and $V$ be linear subspaces of a linear space $X$, and define
>
> $$
> \Phi : U \oplus V \to U + V, \qquad \Phi(u, v) = u + v .
> $$
>
> Then $\Phi$ is linear and onto, and the following are equivalent:
> - (i) $\Phi$ is an isomorphism;
> - (ii) $U \cap V = \{0\}$;
> - (iii) every element of $U + V$ can be written as $u + v$ with $u \in U$, $v \in V$ in exactly one way.

^prop-1-3

> [!proof]+ Proof
> (Not covered in lecture.) $\Phi$ is linear because the operations on $U \oplus V$ are componentwise, and onto by the definition of $U + V$. So (i) says that $\Phi$ is one-to-one, and (iii) says the same thing, since $\Phi(u,v) = \Phi(u',v')$ means $u + v = u' + v'$. It remains to show that $\Phi$ is one-to-one iff $U \cap V = \{0\}$. If $U \cap V = \{0\}$ and $u + v = u' + v'$, then $u - u' = v' - v$ lies in $U \cap V$, so $u = u'$ and $v = v'$. Conversely, if $0 \neq w \in U \cap V$, then $\Phi(w, -w) = 0 = \Phi(0, 0)$ although $(w, -w) \neq (0, 0)$.

^pf-1-3

*Uses:* [[§1 Linear Spaces#^def-1-4|Def. §1.4]], [[§1 Linear Spaces#^def-1-3|Def. §1.3]], [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-1|Def. §3.1]], [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-2|Def. §3.2]]

> [!remark]- Connections
> - Axler's internal direct sum: [[§3 Subspaces#^ladr-1-41|LADR 1.41]]; (ii) ⇔ (iii) is [[§3 Subspaces#^ladr-1-46|LADR 1.46]], via [[Condition for a direct sum|LADR 1.45]].

## Linear Span

> [!definition] Definition §1.5: Linear Span
> Let $X$ be a linear space and $S \subset X$ a subset. The **linear span** of $S$, written $\operatorname{span}\{S\}$, is the smallest linear subspace of $X$ containing $S$.
>
> *Lax: Ch. 1, definition of linear span*

^def-1-5

> [!theorem] Proposition §1.4: The Smallest Subspace Exists
> Let $S \subset X$. The intersection of any family of linear subspaces of $X$ is a linear subspace, and
>
> $$
> \operatorname{span}\{S\} = \bigcap \{ W : W \text{ a linear subspace of } X,\ S \subset W \}.
> $$
>
> In particular the smallest subspace containing $S$ exists, so the definition of span is meaningful.
>
> *Lax: Ch. 1, Thm 2(i)*

^prop-1-4

> [!proof]+ Proof
> Let $\{W_i\}_{i \in I}$ be subspaces and $W = \bigcap_i W_i$. If $x, y \in W$ and $k \in \mathbb{F}$, then $x + y \in W_i$ and $kx \in W_i$ for every $i$, so $x + y, kx \in W$; hence $W$ is a subspace. (For $I = \varnothing$ the intersection is $X$, also a subspace.)
>
> Now let $W_S$ be the intersection of all subspaces containing $S$; the family is nonempty since $X$ belongs to it. Then $W_S$ is a subspace, $S \subset W_S$, and $W_S \subset W$ for every subspace $W \supset S$. So $W_S$ is the smallest subspace containing $S$, i.e. $W_S = \operatorname{span}\{S\}$.

^pf-1-4

*Uses:* [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]]

> [!example] Example §1.3: Span of a Single Vector
> Let $s_0 \in \mathbb{R}^2$ be a nonzero vector. Then
>
> $$
> \operatorname{span}\{s_0\} = \{ a s_0 \mid a \in \mathbb{R} \},
> $$
>
> the line through the origin in the direction of $s_0$: for $a > 0$ one stretches in the positive direction, for $a < 0$ in the negative direction.
>
> ![[m556-1-1.svg]]
> *The span of a nonzero $s_0 \in \mathbb{R}^2$: the dashed line through the origin, containing the multiples $a s_0$ for $a > 1$ and for $a < 0$.*

^ex-1-3

> [!theorem] Proposition §1.5: Span as Finite Linear Combinations
> For any subset $S$ of a linear space $X$,
>
> $$
> \operatorname{span}\{S\} = \Bigl\{ \sum_{i=1}^{k} a_i s_i \;\Big|\; k \geq 1,\ a_i \in \mathbb{F},\ s_i \in S \Bigr\},
> $$
>
> the set of all *finite* linear combinations of elements of $S$ (with $\operatorname{span}\{\varnothing\} = \{0\}$).
>
> *Lax: Ch. 1, Thm 2(ii)*

^prop-1-5

> [!proof]+ Proof
> Let $L$ denote the set of finite linear combinations of elements of $S$. Then $L$ is a subspace: the sum of two finite linear combinations is again a finite linear combination (concatenate the two sums), and a scalar multiple of a finite linear combination is a finite linear combination (multiply each coefficient). Also $S \subset L$ (take $k = 1$, $a_1 = 1$). So $\operatorname{span}\{S\} \subset L$ by minimality.
>
> Conversely, any subspace containing $S$ contains every sum $\sum_{i=1}^k a_i s_i$ by closure under addition and scalar multiplication applied finitely many times, so $L \subset \operatorname{span}\{S\}$.

^pf-1-5

*Uses:* [[§1 Linear Spaces#^def-1-5|Def. §1.5]], [[§1 Linear Spaces#^prop-1-4|§1.4]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]]

> [!remark]- Connections
> - In linear algebra the span is defined by linear combinations and shown to be the smallest containing subspace: [[§4 Span and Linear Independence#^ladr-2-6|LADR 2.6]].
> - Computational version: [[§29 Vector Spaces and Subspaces#^thm-29-4|235 Thm. §29.4]] (the span of finitely many vectors is the smallest subspace containing them, with worked spanning-set examples).

> [!remark] Remark: Why Only Finite Sums
> The sums in the span are finite. We do not, at this point, know how to form an infinite sum of vectors: an infinite sum requires taking a limit, and a linear space carries no notion of limit. Adding two vectors is part of the structure; passing to infinitely many is not, and must be separately justified once a topology is available. Finite sums are also already enough to produce a subspace, as the proof shows.

^rem-1-5
