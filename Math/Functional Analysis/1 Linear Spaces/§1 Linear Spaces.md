---
type: section
subject: "[[Functional Analysis]]"
chapter: 1
section: 1
tags: [functional-analysis, math556]
---
↑ [[· 1 Linear Spaces]] · [[§2 Linear Maps, Convexity, and Linear Functionals]] →

*Stage: algebra — Threads: dimension. The vocabulary of the course; only finite sums exist ([[§1 Linear Spaces#Linear Span|§1]]), and the quotient stands in for an orthogonal complement until [[§18 Projection and Orthogonal Decomposition|§18]].*

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
> - The same definition in linear algebra: [[§2 Definition of Vector Space#^ladr-1-20|LADR 1.20]]; in measure theory: [[§19 Normed Linear Spaces and Lᵖ Spaces#^def-19-1|551 Def. §19.1]].

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

*Uses:* [[§1 Linear Spaces#^def-1-4|Def. §1.4]], [[§1 Linear Spaces#^def-1-3|Def. §1.3]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-1|Def. §2.1]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-2|Def. §2.2]]

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

> [!remark] Remark: Why Only Finite Sums
> The sums in the span are finite. We do not, at this point, know how to form an infinite sum of vectors: an infinite sum requires taking a limit, and a linear space carries no notion of limit. Adding two vectors is part of the structure; passing to infinitely many is not, and must be separately justified once a topology is available. Finite sums are also already enough to produce a subspace, as the proof shows.

^rem-1-5

## Quotient Spaces

> [!definition] Definition §1.6: Equivalence mod $Y$
> Let $X$ be a linear space and $Y$ a linear subspace of $X$. We say $x_1, x_2 \in X$ are **equivalent mod $Y$**, written
>
> $$
> x_1 \equiv x_2 \pmod{Y},
> $$
>
> if $x_1 - x_2 \in Y$.
>
> *Lax: Ch. 1, equivalence mod $Y$*

^def-1-6

> [!definition] Definition §1.7: Equivalence Class and Quotient Space
> For $x_0 \in X$, the **equivalence class** of $x_0$ is
>
> $$
> [x_0] = \{ x \in X \mid x - x_0 \in Y \} = x_0 + Y.
> $$
>
> The **quotient space** $X / Y$ ($X$ mod $Y$) is the set of all equivalence classes:
>
> $$
> X / Y = \{ [x] \mid x \in X \}.
> $$
>
> *Lax: Ch. 1, quotient space*

^def-1-7

> [!remark]- Connections
> - Axler's translates and quotient space: [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97]], [[§11 Products and Quotients of Vector Spaces#^ladr-3-99|LADR 3.99]].

> [!example] Example §1.4: Geometry of Equivalence Classes
> Let $X = \mathbb{R}^2$ and let $Y$ be a line through the origin. If $x_0 = 0$ then $[x_0] = Y$. For general $x_0$, the class $[x_0] = x_0 + Y$ is the line *parallel* to $Y$ passing through the tip of the vector $x_0$: any other point $x$ on this line, dragged back by $-x_0$, lands on $Y$, i.e. $x - x_0 \in Y$. The equivalence classes are therefore the parallel translates of $Y$. They are not subspaces (they do not contain the origin unless equal to $Y$); the quotient $X / Y$ is the collection of all these parallel lines.
>
> ![[m556-1-2.svg]]
> *The class $[x_0] = x_0 + Y$ (red) is the line through $x_0$ parallel to $Y$; a point $x$ on it, moved by $-x_0$, lands on $Y$.*

^ex-1-4

> [!theorem] Proposition §1.6: $X/Y$ is a Linear Space
> The operations
>
> $$
> [x_1] + [x_2] = [x_1 + x_2], \qquad k[x] = [kx]
> $$
>
> are well defined on $X / Y$ and make $X / Y$ a linear space over $\mathbb{F}$, with zero element $[0] = Y$.
>
> *Source: HW1, Problem 1*
>
> *Lax: Ch. 1, quotient space*

^prop-1-6

> [!proof]+ Proof
> (HW1, Problem 1.) **Well-definedness.** Suppose $[x_1] = [x_1']$ and $[x_2] = [x_2']$, i.e. $x_1 - x_1' \in Y$ and $x_2 - x_2' \in Y$. Then
>
> $$
> (x_1 + x_2) - (x_1' + x_2') = (x_1 - x_1') + (x_2 - x_2') \in Y, \qquad kx_1 - kx_1' = k(x_1 - x_1') \in Y,
> $$
>
> since $Y$ is a subspace. Hence $[x_1 + x_2] = [x_1' + x_2']$ and $[kx_1] = [kx_1']$: the operations do not depend on the representatives.
>
> **The axioms.** Let $[x], [y], [z] \in X/Y$ and $a, k \in \mathbb{F}$. In each line the outer equalities are the definitions of the operations on $X/Y$, and the middle equality is the corresponding axiom of $X$.
>
> *Commutativity:* $[x] + [y] = [x + y] = [y + x] = [y] + [x]$.
>
> *Associativity:* $([x] + [y]) + [z] = [x + y] + [z] = [(x + y) + z] = [x + (y + z)] = [x] + [y + z] = [x] + ([y] + [z])$.
>
> *Additive identity:* $[0] = Y \in X/Y$, and $[x] + [0] = [x + 0] = [x] = [0 + x] = [0] + [x]$.
>
> *Additive inverse:* $[-x] \in X/Y$, and $[x] + [-x] = [x - x] = [0] = [-x + x] = [-x] + [x]$.
>
> *Compatibility of scalar multiplication:* $k(a[x]) = k[ax] = [k(ax)] = [(ka)x] = (ka)[x]$.
>
> *Distributivity over vector addition:* $k([x] + [y]) = k[x + y] = [k(x + y)] = [kx + ky] = [kx] + [ky] = k[x] + k[y]$.
>
> *Distributivity over scalar addition:* $(a + k)[x] = [(a + k)x] = [ax + kx] = [ax] + [kx] = a[x] + k[x]$.
>
> *Unit:* $1[x] = [1x] = [x]$.
>
> Hence $X/Y$ is a linear space over $\mathbb{F}$ with zero element $[0] = Y$.

^pf-1-6

*Uses:* [[§1 Linear Spaces#^def-1-6|Def. §1.6]], [[§1 Linear Spaces#^def-1-7|Def. §1.7]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§1 Linear Spaces#^def-1-1|Def. §1.1]]

> [!remark]- Connections
> - The same result in linear algebra: the operations [[§11 Products and Quotients of Vector Spaces#^ladr-3-102|LADR 3.102]], and the quotient is a vector space, [[§11 Products and Quotients of Vector Spaces#^ladr-3-103|LADR 3.103]].

> [!remark] Remark
> The pattern of the verification is the same in every line: the outer equalities are the definitions of the operations on $X/Y$ and the middle equality is the corresponding axiom of $X$, e.g. $k([x_1]+[x_2]) = k[x_1+x_2] = [k(x_1+x_2)] = [kx_1+kx_2] = k[x_1]+k[x_2]$. The additive inverse is $-[x] = [-x]$.

^rem-1-6

> [!remark] Remark: Quotients and Orthogonal Complements
> In $\mathbb{R}^n$, one may think of $X / Y$ as playing the role of the orthogonal complement $Y^\perp$: each parallel translate $x_0 + Y$ meets $Y^\perp$ in exactly one point. But “orthogonal” requires an inner product, and a bare linear space has no such structure. The quotient space is the substitute that is available in full generality. Wu suggested in lecture that $(X/Y) \oplus Y \cong X$ “in some sense”; this became HW1, and the precise statement needs no inner product at all — only a subspace $W$ playing the role of $Y^\perp$. The tools are extracted below.

^rem-1-7

## Complements and the Isomorphism X ≅ X/Y ⊕ Y

Throughout this subsection $Y$ is a fixed linear subspace of $X$. The material is from HW1.

> [!definition] Definition §1.8: Complement
> A linear subspace $W \subset X$ is a **complement** of $Y$ if
>
> $$
> W \cap Y = \{0\} \qquad \text{and} \qquad W + Y = X.
> $$
>
> *Source: HW1*

^def-1-8

> [!theorem] Lemma §1.7: One-Step Enlargement
> Let $W \subset X$ be a linear subspace with $W \cap Y = \{0\}$, and let $x_0 \in X$ with $x_0 \notin W + Y$. Then $W' = W + \operatorname{span}\{x_0\}$ is a linear subspace with $W' \cap Y = \{0\}$ and $W \subsetneq W'$.
>
> *Source: HW1*

^lem-1-7

> [!proof]+ Proof
> $W'$ is a subspace as a sum of subspaces (Proposition [[§1 Linear Spaces#^prop-1-2|§1.2]]).
>
> *Strictness.* $x_0 \in W'$. If $x_0 \in W$ then $x_0 = x_0 + 0 \in W + Y$, contradicting the hypothesis; so $x_0 \in W' \setminus W$.
>
> *Intersection.* Let $w' \in W' \cap Y$, and write $w' = a x_0 + w$ with $a \in \mathbb{F}$, $w \in W$; put $y = w' \in Y$, so $a x_0 + w = y$. If $a \neq 0$, dividing by $a$ and rearranging gives
>
> $$
> x_0 = \frac{y}{a} - \frac{w}{a} \in Y + W,
> $$
>
> contradicting $x_0 \notin W + Y$. Hence $a = 0$, so $w' = w \in W \cap Y = \{0\}$. Thus $W' \cap Y = \{0\}$.

^pf-1-7

*Uses:* [[§1 Linear Spaces#^prop-1-2|§1.2]], [[§1 Linear Spaces#^prop-1-5|§1.5]]

> [!theorem] Proposition §1.8: Every Subspace Has a Complement
> For every linear subspace $Y \subset X$ there exists a complement $W$ of $Y$.
>
> *Source: HW1*

^prop-1-8

> [!proof]+ Proof
> Let $P = \{ W \subset X \text{ a linear subspace} : W \cap Y = \{0\} \}$, partially ordered by inclusion; $\{0\} \in P$. Chains in $P$ have upper bounds: the union of a chain of subspaces is a subspace (the argument in the [[§4 Proof of the Hahn–Banach Theorem#^pf-3-2|proof]] of Theorem [[§3 Statement and Motivation#^thm-3-2|§3.2]]), and it meets $Y$ only in $0$ since each member does. By Zorn's lemma (Theorem [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|§4.2]]) $P$ has a maximal element $W$. If $W + Y \neq X$, pick $x_0 \in X \setminus (W + Y)$; Lemma [[§1 Linear Spaces#^lem-1-7|§1.7]] gives a strictly larger element of $P$, contradicting maximality. Hence $W + Y = X$, and $W$ is a complement.

^pf-1-8

*Uses:* [[§1 Linear Spaces#^def-1-8|Def. §1.8]], [[§3 Statement and Motivation#^thm-3-2|§3.2]], [[§4 Proof of the Hahn–Banach Theorem#^thm-4-2|§4.2]], [[§1 Linear Spaces#^lem-1-7|§1.7]]

> [!remark]- Connections
> - The finite-dimensional version, by extending a basis: [[§5 Bases#^ladr-2-33|LADR 2.33]].

> [!remark] Remark
> When $\dim X < \infty$ Zorn's lemma is unnecessary: starting from $W = \{0\}$ and applying Lemma [[§1 Linear Spaces#^lem-1-7|§1.7]] repeatedly, $\dim W$ increases by one each time and the process stops after at most $\dim X - \dim Y$ steps.

^rem-1-8

> [!theorem] Proposition §1.9: When the Complement is Unique
> A linear subspace $Y$ of $X$ has exactly one complement if and only if $Y = \{0\}$ or $Y = X$.
>
> *Source: HW1*

^prop-1-9

> [!proof]+ Proof
> If $Y = \{0\}$, a complement $W$ satisfies $W = W + \{0\} = X$; if $Y = X$, it satisfies $W = W \cap X = \{0\}$. In both cases the complement is unique.
>
> Suppose $\{0\} \neq Y \neq X$, and let $W$ be a complement (Proposition [[§1 Linear Spaces#^prop-1-8|§1.8]]). Then $W \neq \{0\}$, since $W + Y = X \neq Y$. Choose $0 \neq y_0 \in Y$ and $0 \neq w_0 \in W$. Applying Proposition [[§1 Linear Spaces#^prop-1-8|§1.8]] inside the linear space $W$, the subspace $\operatorname{span}\{w_0\}$ has a complement $W_1$ in $W$: $\operatorname{span}\{w_0\} \cap W_1 = \{0\}$ and $\operatorname{span}\{w_0\} + W_1 = W$. Put
>
> $$
> W' = \operatorname{span}\{w_0 + y_0\} + W_1 .
> $$
>
> *$W' \cap Y = \{0\}$.* If $a(w_0 + y_0) + w_1 \in Y$ with $a \in \mathbb{F}$, $w_1 \in W_1$, then subtracting $a y_0 \in Y$ gives $a w_0 + w_1 \in Y \cap W = \{0\}$; so $a w_0 = -w_1 \in \operatorname{span}\{w_0\} \cap W_1 = \{0\}$, whence $a = 0$ and $w_1 = 0$.
>
> *$W' + Y = X$.* $w_0 = (w_0 + y_0) - y_0 \in W' + Y$ and $W_1 \subset W'$, so $W = \operatorname{span}\{w_0\} + W_1 \subset W' + Y$, and $X = W + Y \subset W' + Y$.
>
> *$W' \neq W$.* $w_0 + y_0 \in W'$; if it were in $W$, then $y_0 = (w_0 + y_0) - w_0 \in W \cap Y = \{0\}$, a contradiction.
>
> So $W'$ is a second complement of $Y$. (Not covered in lecture.)

^pf-1-9

*Uses:* [[§1 Linear Spaces#^def-1-8|Def. §1.8]], [[§1 Linear Spaces#^prop-1-8|§1.8]], [[§1 Linear Spaces#^prop-1-2|§1.2]], [[§1 Linear Spaces#^prop-1-5|§1.5]]

> [!example] Example §1.5: Complements of a Line in the Plane
> In $\mathbb{R}^2$ with $Y$ the $x$-axis, every line through the origin other than $Y$ is a complement of $Y$.
>
> *Source: HW1*

^ex-1-5

> [!remark]- Connections
> - The same example in linear algebra, in the remark “Not unique” after [[§5 Bases#^ladr-2-33|LADR 2.33]].

> [!theorem] Lemma §1.10: Unique Decomposition
> Let $W$ be a complement of $Y$. Then every $x \in X$ can be written as $x = w + y$ with $w \in W$, $y \in Y$, and this representation is unique.
>
> *Source: HW1*

^lem-1-10

> [!proof]+ Proof
> Existence is $X = W + Y$. If $w_1 + y_1 = w_2 + y_2$, then $w_1 - w_2 = y_2 - y_1$ lies in both $W$ and $Y$, hence in $W \cap Y = \{0\}$; so $w_1 = w_2$ and $y_1 = y_2$.

^pf-1-10

*Uses:* [[§1 Linear Spaces#^def-1-8|Def. §1.8]]

This is the implication (ii)$\Rightarrow$(iii) of Proposition [[§1 Linear Spaces#^prop-1-3|§1.3]], applied to $W$ and $Y$.

> [!theorem] Theorem §1.11: $X \cong X/Y \oplus Y$
> Let $W$ be a complement of $Y$. The map
>
> $$
> M : X \to X/Y \oplus Y, \qquad M(x) = ([w], y) \quad \text{where } x = w + y,\ w \in W,\ y \in Y,
> $$
>
> is an isomorphism. Consequently $X/Y \oplus Y \cong X$, with inverse $M^{-1}([x], y) = w + y$, where $w$ is the unique element of $W$ with $[w] = [x]$.
>
> *Source: HW1*

^thm-1-11

> [!proof]+ Proof
> $M$ is well defined by Lemma [[§1 Linear Spaces#^lem-1-10|§1.10]].
>
> *Linearity.* If $x_i = w_i + y_i$ and $a, b \in \mathbb{F}$, then $a x_1 + b x_2 = (a w_1 + b w_2) + (a y_1 + b y_2)$ with the two summands in $W$ and $Y$ respectively; by uniqueness this *is* the decomposition of $a x_1 + b x_2$, so
>
> $$
> M(a x_1 + b x_2) = \bigl([a w_1 + b w_2],\, a y_1 + b y_2\bigr) = a([w_1], y_1) + b([w_2], y_2) = a M(x_1) + b M(x_2),
> $$
>
> using the operations on $X/Y$ (Proposition [[§1 Linear Spaces#^prop-1-6|§1.6]]) and the componentwise operations on the direct sum.
>
> *Surjectivity.* Given $([x], y)$, decompose $x = w + y'$. Then $x - w = y' \in Y$, so $[x] = [w]$, and $M(w + y) = ([w], y) = ([x], y)$.
>
> *Injectivity.* If $M(x_1) = M(x_2)$ with $x_i = w_i + y_i$, then $y_1 = y_2$ and $[w_1] = [w_2]$, i.e. $w_1 - w_2 \in Y$; also $w_1 - w_2 \in W$, so $w_1 - w_2 \in W \cap Y = \{0\}$. Hence $x_1 = x_2$.
>
> $M$ is a linear bijection, hence an isomorphism, and $M^{-1}$ is an isomorphism by Lemma [[§2 Linear Maps, Convexity, and Linear Functionals#^lem-2-1|§2.1]]. The formula for $M^{-1}$ is read off from the surjectivity computation.

^pf-1-11

*Uses:* [[§1 Linear Spaces#^lem-1-10|§1.10]], [[§1 Linear Spaces#^prop-1-6|§1.6]], [[§1 Linear Spaces#^def-1-4|Def. §1.4]], [[§1 Linear Spaces#^def-1-7|Def. §1.7]], [[§2 Linear Maps, Convexity, and Linear Functionals#^def-2-2|Def. §2.2]], [[§2 Linear Maps, Convexity, and Linear Functionals#^lem-2-1|§2.1]]

> [!remark]- Connections
> - In finite dimensions it gives the dimension count of [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]].
> - The orthogonal version for Hilbert spaces: [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]].

> [!theorem] Corollary §1.12: A Complement is a Model of the Quotient
> If $W$ is a complement of $Y$, then the restricted quotient map $W \to X/Y$, $w \mapsto [w]$, is an isomorphism. In particular all complements of $Y$ are isomorphic to one another.
>
> *Source: HW1*

^cor-1-12

> [!proof]+ Proof
> Linearity is inherited from the quotient map. Injectivity and surjectivity are exactly the two computations in the proof of Theorem [[§1 Linear Spaces#^thm-1-11|§1.11]]: $[w_1] = [w_2]$ forces $w_1 - w_2 \in W \cap Y = \{0\}$, and every class $[x]$ equals $[w]$ for the $W$-component $w$ of $x$.

^pf-1-12

*Uses:* [[§1 Linear Spaces#^thm-1-11|§1.11]], [[§1 Linear Spaces#^prop-1-6|§1.6]], [[§1 Linear Spaces#^lem-1-10|§1.10]]

> [!remark] Remark: The Isomorphism is Not Canonical
> $M$ depends on the choice of complement $W$. The quotient $X/Y$ itself is canonical — it is built from $X$ and $Y$ alone — but identifying it with a subspace of $X$ requires choosing $W$, and different choices give different embeddings. This is the precise content of “$X/Y$ is like a complement of $Y$”: it is isomorphic to every complement, and equal to none.

^rem-1-9

![[m556-1-3.svg]]
*Quotient versus complement in $\mathbb{R}^2$. The elements of $X/Y$ are the red lines parallel to $Y$ (with $Y$ itself the zero class $[0]$). A complement $W$ (blue) is a line through $0$ that meets each class exactly once, at $w$ — this is the isomorphism $w \mapsto [w]$ of Corollary §1.12. A second complement $W'$ (green) meets the same classes at different points: $w$ and $w'$ represent the same class $[x]$, so each complement is a model of $X/Y$, and neither is $X/Y$ itself.*

> [!theorem] Corollary §1.13: Orthogonal Complement (inner products; later)
> Let $X$ carry an inner product $\langle \cdot, \cdot \rangle$ and let $Y^\perp = \{ z \in X : \langle z, y \rangle = 0 \ \forall y \in Y \}$. If $X = Y + Y^\perp$, then $Y^\perp$ is a complement of $Y$, so $X/Y \cong Y^\perp$ via $z \mapsto [z]$ and $X \cong X/Y \oplus Y$.
>
> *Source: HW1*

^cor-1-13

> [!proof]+ Proof
> If $z \in Y \cap Y^\perp$ then $\langle z, z \rangle = 0$, so $z = 0$ by positive-definiteness of the inner product (to be introduced later). With $X = Y + Y^\perp$ assumed, $Y^\perp$ is a complement; apply Corollary [[§1 Linear Spaces#^cor-1-12|§1.12]] and Theorem [[§1 Linear Spaces#^thm-1-11|§1.11]].

^pf-1-13

*Uses:* [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§1 Linear Spaces#^def-1-8|Def. §1.8]], [[§1 Linear Spaces#^cor-1-12|§1.12]], [[§1 Linear Spaces#^thm-1-11|§1.11]]

> [!remark]- Connections
> - The inner product and $Y^\perp$ in this course: [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]] (the orthogonal decomposition, which supplies $X = Y + Y^\perp$ for closed $Y$ in a Hilbert space).
> - In finite dimensions: [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]], and $V = U \oplus U^\perp$ ([[§21 Orthogonal Complements and Minimization Problems#^ladr-6-49|LADR 6.49]]).

> [!remark] Remark
> The hypothesis $X = Y + Y^\perp$ holds automatically in finite dimensions, and in infinite dimensions it holds when $X$ is complete and $Y$ is closed (the orthogonal decomposition theorem, Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]]). It can fail for a general subspace: in $\ell^2$ with the inner product of [[· 5 Inner Product Spaces|Chapter 5]], the finitely supported sequences form a subspace $Y$ with $Y^\perp = \{0\}$, since $(z, e_i) = z_i$, so $Y + Y^\perp = Y \neq \ell^2$. Then $Y^\perp$ is *not* a complement — although by Proposition [[§1 Linear Spaces#^prop-1-8|§1.8]] some other complement always exists. This is why the orthogonal version is only “roughly” true, while the algebraic version (Theorem [[§1 Linear Spaces#^thm-1-11|§1.11]]) is unconditional.

^rem-1-10
