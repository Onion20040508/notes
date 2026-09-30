---
type: section
subject: "[[Group Theory]]"
chapter: 8
section: 39
tags: [group-theory, math493]
---
← [[§38 The First Isomorphism Theorem]] · ↑ [[8 Normal Subgroups and Quotient Groups]] · [[§40 Characters]] →

*Reference: Not treated in Pinter.*

> [!remark] Remark: The Picture So Far
> Groups and subgroups produce sets with actions: a subgroup $H$ gives the set $G/H$, with $G \curvearrowright G/H$. Conversely, whenever $G$ acts on a set $X$, the set breaks up into orbits, $X = \bigsqcup_i O_i$, and each $O_i$ is in natural bijection with $G/H_i$, where $H_i$ is the stabilizer of a point of $O_i$ ([[§28 Orbit–Stabilizer#^prop-28-2|§28.2]]). When $N$ is normal, $G/N$ is itself a group ([[§37 Quotient Groups#^thm-37-1|§37.1]]), and every homomorphic image of $G$ is of this form, $\operatorname{Im}\varphi \cong G/\operatorname{Ker}\varphi$ ([[§38 The First Isomorphism Theorem#^thm-38-1|§38.1]]). This suggests a strategy: to understand $G$, look for a normal subgroup $N$; understand $N$ and $G/N$; and understand how they are put together. Simple groups are the groups on which this strategy gives nothing, because they cannot be broken into smaller pieces this way.
>
> *Source: lecture 9/28*

^rem-39-1

> [!definition] Definition §39.1: Simple Group
> A group $G$ is **simple** if it has exactly two normal subgroups, $\{e_G\}$ and $G$. Equivalently, $G \neq \{e\}$ and the only normal subgroups of $G$ are $\{e\}$ and $G$. The trivial group is not simple, since it has only one normal subgroup.
>
> *Source: lecture 9/21, 9/28; WS 7*

^def-39-1

> [!remark] Remark: Why Simple Groups Matter
> The classification of finite simple groups is one of the landmark theorems of mathematics. Its significance is that simple groups are the basic building blocks: in a precise sense, every finite group is assembled from simple pieces, via normal subgroups and the quotient groups constructed from them. The trivial group is excluded by convention, much as $1$ is excluded from the primes.

^rem-39-2

> [!theorem] Theorem §39.1: Abelian Simple Groups
> An abelian group $G$ is simple if and only if $G \cong \mathbb{Z}/p\mathbb{Z}$ for a prime $p$.
>
> *Source: lecture; ($\Leftarrow$) is WS 7.3*

^thm-39-1

> [!proof]+ Proof
> ($\Leftarrow$) $\mathbb{Z}/p\mathbb{Z} \neq \{0\}$, and a group of prime order has no subgroups other than the trivial subgroup and itself ([[§27 The Index and Lagrange's Theorem#^cor-27-8|§27.8]]); in particular no other normal subgroups.
>
> ($\Rightarrow$) Let $G$ be abelian and simple. As $G \neq \{e\}$, pick $g \neq e$. The subgroup $\langle g \rangle$ is nontrivial and, $G$ being abelian, normal; by simplicity $\langle g \rangle = G$, so $G$ is cyclic. If $G$ were infinite cyclic, $G \cong \mathbb{Z}$, which is not simple since $2\mathbb{Z}$ is a proper nontrivial (normal) subgroup. So $G$ is cyclic of finite order $n \geq 2$ ([[§17 Cyclic Groups#^thm-17-1|§17.1]]). Suppose $n = ab$ with $1 < a < n$. Then $(g^a)^b = g^n = e$, while for $0 < k < b$ we have $0 < ak < n$, so $(g^a)^k \neq e$; thus $g^a$ has order $b$, and $\langle g^a \rangle$ is a subgroup with $1 < b < n$ elements — proper, nontrivial, and normal, contradicting simplicity. Hence $n$ is prime, and $G \cong \mathbb{Z}/n\mathbb{Z}$.

^pf-39-1

*Uses:* [[§39 Simple Groups#^def-39-1|Def. §39.1]], [[§27 The Index and Lagrange's Theorem#^cor-27-8|§27.8]], [[§35 Normal Subgroups#^prop-35-1|§35.1]], [[§4 Subgroups#^prop-4-5|§4.5]], [[§4 Subgroups#^def-4-5|Def. §4.5]], [[§17 Cyclic Groups#^thm-17-1|§17.1]]

> [!theorem] Corollary §39.2: $S_n$ Is Not Simple for $n \geq 3$
> For $n \geq 3$, $A_n$ is a proper nontrivial normal subgroup of $S_n$; hence $S_n$ is not simple.

^cor-39-2

> [!proof]+ Proof
> $A_n$ is normal, having index $2$ ([[§36 Sources of Normal Subgroups#^ex-36-1|Ex. §36.1]]). It is nontrivial, since it contains the $3$-cycle $(1\,2\,3) = (1\,3)(1\,2)$, a product of two transpositions; and proper, since the transposition $(1\,2)$ is odd.

^pf-39-2

*Uses:* [[§36 Sources of Normal Subgroups#^prop-36-1|§36.1]], [[§36 Sources of Normal Subgroups#^ex-36-1|Ex. §36.1]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3|Def. §20.3]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§39 Simple Groups#^def-39-1|Def. §39.1]]

> [!remark] Remark: Where the Interesting Simple Groups Are
> For abelian groups simplicity is only a question of whether any proper nontrivial subgroup exists, since every subgroup is normal; [[§39 Simple Groups#^thm-39-1|the theorem]] shows the answer is “no” exactly for prime order. Non-abelian simple groups are far subtler, since non-normal subgroups do not count against simplicity. The smallest example is [[§39 Simple Groups#^thm-39-7|identified below]].

^rem-39-3

> [!theorem] Proposition §39.3: Homomorphisms out of a Simple Group
> Let $G$ be simple and $H$ any group. Every homomorphism $\omega: G \to H$ is either injective or trivial.
>
> *Source: WS 7.1; lecture 9/28*

^prop-39-3

> [!proof]+ Proof
> $\operatorname{Ker}\omega$ is normal in $G$ ([[§36 Sources of Normal Subgroups#^prop-36-2|Kernels Are Normal]], §36), so by simplicity $\operatorname{Ker}\omega = \{e_G\}$ or $\operatorname{Ker}\omega = G$. In the first case $\omega$ is injective ([[§15 Homomorphisms#^prop-15-3|Surjectivity and Injectivity via Image and Kernel]], §15); in the second, $\omega(g) = e_H$ for every $g$, i.e. $\omega$ is trivial.

^pf-39-3

*Uses:* [[§36 Sources of Normal Subgroups#^prop-36-2|§36.2]], [[§39 Simple Groups#^def-39-1|Def. §39.1]], [[§15 Homomorphisms#^prop-15-3|§15.3]]

> [!theorem] Proposition §39.4: Homomorphisms into a Simple Group
> The analogous statement for homomorphisms *into* a simple group is false: $\omega: \mathbb{Z}/3\mathbb{Z} \to A_5$, $\omega([k]) = (1\,2\,3)^k$, is a homomorphism into the simple group $A_5$ that is neither surjective nor trivial.
>
> *Source: WS 7.2; lecture 9/28*

^prop-39-4

> [!proof]+ Proof
> $(1\,2\,3) = (1\,3)(1\,2)$ is even, so it lies in $A_5$, and it has order $3$; hence $[k] \mapsto (1\,2\,3)^k$ is a well-defined homomorphism (The Homomorphism $k \mapsto g^k$, [[§17 Cyclic Groups#^prop-17-3|§17.3]]). Its image $\{e, (1\,2\,3), (1\,3\,2)\}$ has $3$ elements: it is not $\{e\}$, and it is not all of $A_5$, which has $60$ elements. That $A_5$ is simple is [[§39 Simple Groups#^prop-39-6|WS 7.4]], below.

^pf-39-4

*Uses:* [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§11 Disjoint Cycle Decomposition#^lem-11-1|§11.1]], [[§17 Cyclic Groups#^prop-17-3|§17.3]], [[§20 The Sign Homomorphism and the Alternating Group#^prop-20-5|§20.5]], [[§39 Simple Groups#^prop-39-6|§39.6]]

> [!remark] Remark: Why 7.1 Does Not Dualize
> The proof of [[§39 Simple Groups#^prop-39-3|WS 7.1]] works because kernels are always normal. The analogous argument for [[§39 Simple Groups#^prop-39-4|WS 7.2]] would need the image to be normal in $H$, and images need not be ([[§36 Sources of Normal Subgroups#^prop-36-3|WS 6.5]], §36). The following corollary records what survives.

^rem-39-4

> [!theorem] Corollary §39.5: A Normal Image in a Simple Group
> Let $H$ be simple and $\omega: G \to H$ a homomorphism whose image is normal in $H$. Then $\omega$ is surjective or trivial.

^cor-39-5

> [!proof]+ Proof
> $\operatorname{Im}\omega$ is a normal subgroup of the simple group $H$, so it is $\{e_H\}$, in which case $\omega$ is trivial, or $H$, in which case $\omega$ is surjective.

^pf-39-5

*Uses:* [[§39 Simple Groups#^def-39-1|Def. §39.1]], [[§15 Homomorphisms#^prop-15-2|§15.2]]

> [!theorem] Proposition §39.6: $A_5$ Is Simple
> The conjugacy classes of $A_5$ are as follows (as given on the worksheet):
>
> | representative | $e$ | $(1\,2\,3)$ | $(1\,2)(3\,4)$ | $(1\,2\,3\,4\,5)$ | $(1\,2\,3\,5\,4)$ |
> |---|---|---|---|---|---|
> | class size | $1$ | $20$ | $15$ | $12$ | $12$ |
>
> Using this, $A_5$ is simple.
>
> *Source: WS 7.4; class 9/30*

^prop-39-6

> [!proof]+ Proof
> *(Worked in class, Wed Sept 30.)* Let $N \trianglelefteq A_5$. Then $N$ is a union of conjugacy classes of $A_5$ ([[§36 Sources of Normal Subgroups#^prop-36-7|Normal Subgroups Are Unions of Conjugacy Classes]], §36), and it contains the class $\{e\}$. So $|N| = 1 + s$, where $s$ is a sum of some of the numbers $20, 15, 12, 12$. The possible values of $1 + s$ are
>
> $$ 1,\ 13,\ 16,\ 21,\ 25,\ 28,\ 33,\ 36,\ 40,\ 45,\ 48,\ 60. $$
>
> By [[§27 The Index and Lagrange's Theorem#^thm-27-2|Lagrange]], $|N|$ divides $|A_5| = 60$, whose divisors are $1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60$. The only common values are $1$ and $60$, so $N = \{e\}$ or $N = A_5$. Since also $A_5 \neq \{e\}$, $A_5$ is simple.

^pf-39-6

*Uses:* [[§36 Sources of Normal Subgroups#^prop-36-7|§36.7]], [[§27 The Index and Lagrange's Theorem#^thm-27-2|§27.2]], [[§39 Simple Groups#^def-39-1|Def. §39.1]]

![[m493-39-1.svg]]
*The proof that $A_5$ is simple: a normal subgroup $N$ is a union of classes containing $\{e\}$, so $|N| = 1 + s$ with $s$ a sum of some of $20, 15, 12, 12$ (red), and $|N|$ must divide $60$ (blue). The two rows meet only at $1$ and $60$ (boxed).*

> [!theorem] Theorem §39.7: $A_5$ Is the Smallest Non-Abelian Simple Group
> Every non-abelian simple group has order at least $60 = |A_5|$.
>
> *Source: not from class*

^thm-39-7

> [!proof]- Proof
> *[To be proved.]*

^pf-39-7

> [!theorem] Lemma §39.8: $3$-Cycles Are Conjugate in $A_n$ for $n \geq 5$
> Let $n \geq 5$, and let $(i\,j\,k)$ and $(i'\,j'\,k')$ be $3$-cycles. Then there is $g \in A_n$ with $g\,(i\,j\,k)\,g^{-1} = (i'\,j'\,k')$. So the $3$-cycles form a single conjugacy class of $A_n$, not only of $S_n$.
>
> *Source: lecture 9/30*

^lem-39-8

> [!proof]+ Proof
> Choose $g \in S_n$ with $g(i) = i'$, $g(j) = j'$, $g(k) = k'$, extending these three assignments to a bijection of $\{1, \ldots, n\}$. Then $g\,(i\,j\,k)\,g^{-1} = (i'\,j'\,k')$ ([[§12 Multiplying and Conjugating Cycles#^prop-12-1|Conjugation Relabels a Cycle]], §12). If $g \in A_n$ we are done. If not, since $n \geq 5$ there are two points $x, y \notin \{i, j, k\}$; replace $g$ by $g(x\,y)$, which is even. Because $(x\,y)$ is disjoint from $(i\,j\,k)$, the two commute, so
>
> $$ \big[g(x\,y)\big]\,(i\,j\,k)\,\big[g(x\,y)\big]^{-1} = g\,(i\,j\,k)(x\,y)(x\,y)^{-1}\,g^{-1} = g\,(i\,j\,k)\,g^{-1} = (i'\,j'\,k'). $$

^pf-39-8

*Uses:* [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]]

> [!theorem] Theorem §39.9: $A_n$ Is Simple for $n \geq 5$
> Let $n \geq 5$, let $N$ be a nontrivial normal subgroup of $A_n$, and let $g \in N$ with $g \neq e$.
> 1. There is a $3$-cycle $(i\,j\,k) \in A_n$ that does not commute with $g$. Set $h = g\,(i\,j\,k)\,g^{-1}\,(i\,j\,k)^{-1}$.
> 2. $h \in N$.
> 3. $h$ has one of the cycle types $(a\,b\,c)(d\,e\,f)$, $(a\,b\,c\,d\,e)$, $(a\,b)(c\,d)$, $(a\,b\,c)$.
> 4. $N$ contains a $3$-cycle. (The case of type $(a\,b)(c\,d)$ uses $n \geq 5$.)
> 5. $N = A_n$.
>
> Hence $A_n$ is simple for every $n \geq 5$.
>
> *Source: WS 7.5; lecture 9/28, 9/30*

^thm-39-9

> [!proof]+ Proof
> *(Lecture 9/30 proved (1)–(3), the case $(a\,b)(c\,d)$ of (4), and (5). The cases of a $5$-cycle and of two $3$-cycles in (4) were left to a PDF on the course page; they are computed here.)* Since $N$ is normal, $sgs^{-1} \in N$ for every $s \in A_n$ and $g \in N$.
>
> **(1)** As $g \neq e$, choose $i$ with $g(i) \neq i$, and then $j, k$ with $i, j, k$ distinct and $j, k \notin \{i, g(i)\}$ (possible since $n \geq 4$). By [[§12 Multiplying and Conjugating Cycles#^prop-12-1|Conjugation Relabels a Cycle]], $g\,(i\,j\,k)\,g^{-1} = (g(i)\ g(j)\ g(k))$. This $3$-cycle sends $g(i) \mapsto g(j)$, whereas $(i\,j\,k)$ fixes $g(i)$, because $g(i) \notin \{i, j, k\}$; and $g(j) \neq g(i)$. So $g\,(i\,j\,k)\,g^{-1} \neq (i\,j\,k)$, i.e. $(i\,j\,k)$ does not commute with $g$.
>
> **(2)** $h = g \cdot \big[(i\,j\,k)\,g^{-1}\,(i\,j\,k)^{-1}\big]$. The bracket is the conjugate of $g^{-1} \in N$ by $(i\,j\,k) \in A_n$, so it lies in $N$; hence $h \in N$. By (1), $h \neq e$.
>
> **(3)** $h = (g(i)\ g(j)\ g(k)) \cdot (i\,k\,j)$ is a product of two $3$-cycles. So $h$ fixes every point outside $M = \{i, j, k, g(i), g(j), g(k)\}$, a set of at most $6$ points, and $h$ is even. The even cycle types on at most $6$ points are $(a\,b\,c)$, $(a\,b)(c\,d)$, $(a\,b\,c\,d\,e)$, $(a\,b\,c)(d\,e\,f)$ and $(a\,b)(c\,d\,e\,f)$, since an $r$-cycle has sign $(-1)^{r-1}$ ([[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]]). The last type moves $6$ points, which forces $|M| = 6$: the two $3$-cycles have disjoint supports, so $h$ is their product, of type $(a\,b\,c)(d\,e\,f)$ instead. So $h$ has one of the four listed types.
>
> **(4)** In each case we find a $3$-cycle in $N$. Throughout, $t$ denotes a $3$-cycle, so $t \in A_n$ and $h' := t\,h\,t^{-1} \in N$; then $hh'^{-1} \in N$ too.
> - *$h = (a\,b\,c)$:* $h$ itself is a $3$-cycle in $N$.
> - *$h = (a\,b)(c\,d)$ (lecture):* as $n \geq 5$, pick $x \notin \{a, b, c, d\}$ and take $t = (c\,d\,x)$. Then $h' = (a\,b)(d\,x)$, which is its own inverse, and
>
>   $$ hh'^{-1} = (a\,b)(c\,d)(a\,b)(d\,x) = (a\,b)^2(c\,d)(d\,x) = (c\,d\,x). $$
>
> - *$h = (a\,b\,c\,d\,e)$:* take $t = (a\,b\,c)$. Then $h' = (b\ c\ a\ d\ e)$, and tracking each point through $h'^{-1} = (e\ d\ a\ c\ b)$ followed by $h$ gives
>
>   $$ hh'^{-1} = (a\,d\,b): \qquad a \mapsto c \mapsto d,\quad d \mapsto a \mapsto b,\quad b \mapsto e \mapsto a,\quad c \mapsto b \mapsto c,\quad e \mapsto d \mapsto e. $$
>
> - *$h = (a\,b\,c)(d\,e\,f)$:* take $t = (a\,b\,d)$. Then $h' = (b\,d\,c)(a\,e\,f)$ and $h'^{-1} = (b\,c\,d)(a\,f\,e)$, and tracking points gives the $5$-cycle
>
>   $$ hh'^{-1} = (a\,d\,c\,e\,b): \qquad a \mapsto f \mapsto d,\quad d \mapsto b \mapsto c,\quad c \mapsto d \mapsto e,\quad e \mapsto a \mapsto b,\quad b \mapsto c \mapsto a, $$
>
>   with $f \mapsto e \mapsto f$ fixed. This $5$-cycle lies in $N$, and the previous case produces a $3$-cycle from it.
>
> **(5)** By (4), $N$ contains a $3$-cycle. By [[§39 Simple Groups#^lem-39-8|the lemma]], every $3$-cycle is conjugate to it in $A_n$, so, $N$ being normal, $N$ contains all $3$-cycles. Since $A_n$ is generated by $3$-cycles (Generators of $A_n$, [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-9|§20.9]]), $N = A_n$. Thus the only normal subgroups of $A_n$ are $\{e\}$ and $A_n$, and $A_n \neq \{e\}$: $A_n$ is simple.

^pf-39-9

*Uses:* [[§35 Normal Subgroups#^def-35-1|Def. §35.1]], [[§12 Multiplying and Conjugating Cycles#^prop-12-1|§12.1]], [[§20 The Sign Homomorphism and the Alternating Group#^cor-20-4|§20.4]], [[§11 Disjoint Cycle Decomposition#^lem-11-2|§11.2]], [[§39 Simple Groups#^lem-39-8|§39.8]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-9|§20.9]], [[§39 Simple Groups#^def-39-1|Def. §39.1]]

> [!remark] Remark: The Strategy
> Let $N \trianglelefteq A_n$ with $N \neq \{e\}$; the aim is $N = A_n$. First goal: some $3$-cycle $(i\,j\,k)$ lies in $N$. Second goal: every $3$-cycle lies in $N$. Big goal: $N = A_n$, which then follows because $A_n$ is generated by $3$-cycles (Generators of $A_n$, [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-9|§20.9]]). The argument starts from an arbitrary $g \in N$ with $g \neq e$. On Sept 30 the lecture added the missing link: for $n \geq 5$ the $3$-cycles form a single conjugacy class of $A_n$ ($3$-Cycles Are Conjugate in $A_n$ for $n \geq 5$, [[§39 Simple Groups#^lem-39-8|§39.8]]), so one $3$-cycle in $N$ brings all of them.
>
> *Source: lecture 9/28*

^rem-39-5

> [!theorem] Proposition §39.10: The Pair-Partition Homomorphism $S_4 \to S_3$
> Let $S_4$ act on the three ways of splitting $\{1, 2, 3, 4\}$ into two pairs,
>
> $$ P = \big\{\, \{\{1,2\},\{3,4\}\},\ \{\{1,3\},\{2,4\}\},\ \{\{1,4\},\{2,3\}\} \,\big\}, $$
>
> and let $\alpha: S_4 \to S_P \cong S_3$ be the associated homomorphism. Then $\alpha$ is surjective and $\operatorname{Ker}\alpha = V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$. Consequently $V$ is normal in $S_4$ and in $A_4$, and
>
> $$ S_4/V \cong S_3, \qquad A_4/V \cong A_3 \cong \mathbb{Z}/3\mathbb{Z}. $$
>
> *Source: lecture 9/30*

^prop-39-10

> [!proof]+ Proof
> A permutation carries a splitting into pairs to another such splitting, so this is an action, and it gives $\alpha$ (Actions Are Homomorphisms to $S_X$, [[§23 Actions#^thm-23-3|§23.3]]). *Surjective:* the transposition $(3\,4)$ fixes $\{\{1,2\},\{3,4\}\}$ and swaps $\{\{1,3\},\{2,4\}\} \leftrightarrow \{\{1,4\},\{2,3\}\}$; in the same way each transposition $(a\,b)$ fixes the splitting containing $\{a, b\}$ and swaps the other two. So the image contains all three transpositions of $S_P$, which generate it. *Kernel:* $|\operatorname{Ker}\alpha| = 24/6 = 4$ ($|G| = |\operatorname{Ker}\alpha| \cdot |\operatorname{Im}\alpha|$, [[§38 The First Isomorphism Theorem#^cor-38-2|§38.2]]). Each double transposition preserves every splitting, e.g. $(1\,2)(3\,4)$ swaps $\{1,3\} \leftrightarrow \{2,4\}$ and $\{1,4\} \leftrightarrow \{2,3\}$. So $V \subseteq \operatorname{Ker}\alpha$, and as both have $4$ elements, $\operatorname{Ker}\alpha = V$.
>
> [[§36 Sources of Normal Subgroups#^prop-36-2|Kernels are normal]], so $V \trianglelefteq S_4$, and $V \trianglelefteq A_4$ because $V \subseteq A_4$. The [[§38 The First Isomorphism Theorem#^thm-38-1|First Isomorphism Theorem]] gives $S_4/V \cong S_3$. Restricted to $A_4$, $\alpha$ has kernel $V \cap A_4 = V$, so $A_4/V \cong \alpha(A_4)$, a subgroup of $S_3$ with $12/4 = 3$ elements. The only such subgroup is $A_3 = \langle (1\,2\,3) \rangle$ (Subgroups of $S_3$, [[§13 Subgroups of S₃#^prop-13-1|§13.1]]), and it is cyclic of order $3$.

^pf-39-10

*Uses:* [[§23 Actions#^def-23-1|Def. §23.1]], [[§23 Actions#^thm-23-3|§23.3]], [[§20 The Sign Homomorphism and the Alternating Group#^thm-20-7|§20.7]], [[§38 The First Isomorphism Theorem#^cor-38-2|§38.2]], [[§36 Sources of Normal Subgroups#^prop-36-2|§36.2]], [[§38 The First Isomorphism Theorem#^thm-38-1|§38.1]], [[§13 Subgroups of S₃#^prop-13-1|§13.1]]

![[m493-39-2.svg]]
*The three ways of splitting $\{1,2,3,4\}$ into two pairs, each drawn as two blue edges. The transposition $(3\,4)$ fixes $\{\{1,2\},\{3,4\}\}$ and swaps the other two splittings (red), so it acts on $P$ as a transposition. A double transposition such as $(1\,2)(3\,4)$ carries every splitting to itself, which is why $V$ is the kernel.*

> [!example] Example §39.1: In $A_4$, $(1\,2\,3)$ and $(1\,3\,2)$ Are Not Conjugate
> The restriction $\alpha|_{A_4}: A_4 \to A_3$ is a character, since $A_3$ is abelian, and characters are constant on conjugacy classes ([[§40 Characters#^prop-40-1|Characters Are Constant on Conjugacy Classes]], §40). Now $\alpha((1\,2\,3)) \neq e$, because $(1\,2\,3) \notin V$, and $\alpha((1\,3\,2)) = \alpha((1\,2\,3))^{-1}$. In a group of order $3$ no non-identity element equals its own inverse, so the two images differ, and $(1\,2\,3)$ and $(1\,3\,2)$ are not conjugate in $A_4$ (although they are conjugate in $S_4$). So the lemma on $3$-cycles ([[§39 Simple Groups#^lem-39-8|§39.8]]) fails for $n = 4$.
>
> *Source: lecture 9/30*

^ex-39-1

> [!remark] Remark: Why $n \geq 5$
> The proof for $A_n$ ([[§39 Simple Groups#^thm-39-9|§39.9]]) used $n \geq 5$ twice: the $(a\,b)(c\,d)$ case needs a fifth point, and the lemma on $3$-cycles ([[§39 Simple Groups#^lem-39-8|§39.8]]) needs two points outside a $3$-cycle. For $n = 4$ both fail for a real reason: $A_4$ has the extra normal subgroup $V$. Group theory is a mix of universal principles and funny small counterexamples, and $A_4$ is one of the latter.
>
> *Source: lecture 9/30*

^rem-39-6

> [!theorem] Corollary §39.11: Which $A_n$ Are Simple
> $A_n$ is simple if and only if $n = 3$ or $n \geq 5$.

^cor-39-11

> [!proof]+ Proof
> For $n \geq 5$ this is [[§39 Simple Groups#^thm-39-9|WS 7.5]]. $A_1$ and $A_2$ are trivial, hence not simple. $A_3 = \langle (1\,2\,3) \rangle$ has prime order $3$, hence is simple ([[§39 Simple Groups#^thm-39-1|Abelian Simple Groups]]). $A_4$ is not simple: $V$ is a normal subgroup with $\{e\} \neq V \neq A_4$ ([[§39 Simple Groups#^prop-39-10|The Pair-Partition Homomorphism]]).

^pf-39-11

*Uses:* [[§39 Simple Groups#^thm-39-9|§39.9]], [[§39 Simple Groups#^def-39-1|Def. §39.1]], [[§39 Simple Groups#^thm-39-1|§39.1]], [[§39 Simple Groups#^prop-39-10|§39.10]]

> [!example] Example §39.2: The Field $\mathbb{F}_9$
> $\mathbb{F}_p$ denotes the field $\mathbb{Z}/p\mathbb{Z}$ ($p$ prime; [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]). Not every finite field is of this form: the set
>
> $$ \mathbb{F}_9 = \{a + bi : a, b \in \mathbb{F}_3\}, \qquad i^2 = -1, $$
>
> with the usual rules for adding and multiplying complex numbers, is a field with $9$ elements. It is *not* $\mathbb{Z}/9\mathbb{Z}$, which is not a field: $[3][3] = [0]$.
>
> *Source: lecture 9/30*

^ex-39-2

> [!proof]+ Proof
> Addition and multiplication are those of complex numbers with coefficients reduced modulo $3$, so the ring axioms carry over. For inverses: if $a + bi \neq 0$, then $a^2 + b^2 \neq 0$ in $\mathbb{F}_3$, because the squares in $\mathbb{F}_3$ are $0, 1, 1$, so a sum of two squares that are not both $0$ is $1$ or $2$. Hence $(a + bi)^{-1} = (a - bi)/(a^2 + b^2)$. Finally $\mathbb{Z}/9\mathbb{Z}$ is not a field since $9$ is not prime ($\mathbb{Z}/n\mathbb{Z}$ Is a Field if and only if $n$ Is Prime, [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]).

^pf-ex-39-2

*Uses:* [[§3 Basic Examples of Groups#^def-3-3|Def. §3.3]], [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]

> [!theorem] Theorem §39.12: Classification of Finite Fields
> Every finite field has $q = p^m$ elements for some prime $p$ and $m \geq 1$, and for every prime power $q$ there is exactly one field with $q$ elements up to isomorphism, written $\mathbb{F}_q$. Thus $\{\text{finite fields}\}/{\cong} \longleftrightarrow \{\text{prime powers}\}$.
>
> *Source: stated in lecture 9/30*

^thm-39-12

> [!proof]- Proof
> *[To be proved.]*

^pf-39-12

> [!remark] Remark: Why Finite Fields Here
> The classification was mentioned only for general culture and is not proved in the course. It explains the notation $\mathbb{F}_q$ in the projective special linear groups $PSL_n(\mathbb{F}_q)$ [[§39 Simple Groups#^def-39-2|below]], one of the three main families of simple groups: the $\mathbb{Z}/p\mathbb{Z}$, the $A_n$ ($n \geq 5$), and the $PSL_n(F)$.

^rem-39-7

> [!definition] Definition §39.2: Projective Special Linear Group
> Let $F$ be a field and $SL_n(F)$ the group of $n \times n$ matrices over $F$ with determinant $1$. Let $Z = \{\zeta I_n : \zeta \in F,\ \zeta^n = 1\}$, the scalar matrices in $SL_n(F)$. Scalar matrices commute with every matrix, so $Z \subseteq Z(SL_n(F))$ and $Z \trianglelefteq SL_n(F)$. The **projective special linear group** is the quotient $PSL_n(F) := SL_n(F)/Z$.
>
> *Source: WS 7*

^def-39-2

> [!theorem] Theorem §39.13: $PSL_n(F)$ Is Simple
> Let $F$ be a field and $n \geq 2$. Then $PSL_n(F)$ is simple, except for $PSL_2(\mathbb{F}_2)$ and $PSL_2(\mathbb{F}_3)$. (For $n = 1$, $PSL_1(F)$ is trivial and hence not simple.)
>
> *Source: WS 7; lecture 9/28*

^thm-39-13

> [!proof]- Proof
> *[To be proved.]*

^pf-39-13

> [!example] Example §39.3: The Two Exceptions
> $PSL_2(\mathbb{F}_2) \cong S_3$ and $PSL_2(\mathbb{F}_3) \cong A_4$. Neither is simple: $A_3 \trianglelefteq S_3$, and the Klein four-group $V$ is normal in $A_4$ ([[§39 Simple Groups#^prop-39-10|The Pair-Partition Homomorphism]], above).
>
> *Source: WS 7*

^ex-39-3

> [!proof]- Proof
> *[To be proved.]*

^pf-ex-39-3

> [!remark] Remark: About the Proof
> The proof that $PSL_n(F)$ is simple has many good ideas but is too long to be a worksheet problem. After the cyclic groups $C_p$ and the alternating groups $A_n$ ($n \geq 5$), the $PSL_n(F)$ are the most important simple groups.

^rem-39-8
