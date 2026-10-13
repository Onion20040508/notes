---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 51
tags: [group-theory, math493]
---
← [[§50 S₃, S₄, Aₙ and GLₙ]] · ↑ [[· 10 The Sylow Theorems]] · [[§52 The Sylow Theorems]] →

*Reference: Worksheet 10. Throughout, $p$ is a prime.*

> [!remark] Remark: The Question
> By Lagrange ([[§29 The Index and Lagrange's Theorem#^thm-29-2|Theorem §29.2]]), if $H \leq G$ and $G$ is finite, then $|H|$ divides $|G|$. Conversely, if $m$ divides $|G|$, is there a subgroup of order $m$? Not in general: $A_4$ has order $12$ but no subgroup of order $6$ (The Converse of Lagrange Fails: $A_4$, [[§29 The Index and Lagrange's Theorem#^ex-29-1|Example §29.1]]). The lecture's answer is yes when $m$ is a power of a prime. The case of a prime $m = p$ is Cauchy's theorem ([[§29 The Index and Lagrange's Theorem#^thm-29-6|Theorem §29.6]]), and the case of the largest power of $p$ dividing $|G|$ is the First Sylow Theorem ([[§52 The Sylow Theorems#^thm-52-4|Theorem §52.4]]). For example, $|S_3| = 6$, and $\langle (1\,2) \rangle$ and $\langle (1\,2\,3) \rangle$ have orders $2$ and $3$. The lecture also asked for a subgroup of order $8$ in $S_4$, of order $24$ ([[§51 p-Groups and Sylow Subgroups#^ex-51-1|Example §51.1]] below).
>
> *Source: lecture 10/12*

^rem-51-1

Worksheet 10 begins by restating the definition of a $p$-group, already met with the [[§35 The Center#^def-35-2|center]]:

![[§35 The Center#^def-35-3]]

Nontrivial $p$-groups have nontrivial center ([[§35 The Center#^thm-35-3|Theorem §35.3]], PS 3.5); for groups of order $p^2$ this already decides the group ([[§51 p-Groups and Sylow Subgroups#Groups of Order p²|below]], PS 6.3).

> [!definition] Definition §51.1: $p$-Subgroup
> For a group $G$, a **$p$-subgroup** of $G$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $G$ which is a $p$-group ([[§35 The Center#^def-35-3|Def. §35.3]]).
>
> *Source: WS 10*

^def-51-1

> [!theorem] Proposition §51.1: Fixed Points of a $p$-Group Action
> Let $P$ be a $p$-group and let $X$ be a finite set on which $P$ [[§25 Actions#^def-25-1|acts]]. If $|X| \not\equiv 0 \pmod p$, then $P$ [[§26 Stabilizers and Fixed Points#^def-26-2|fixes]] some point of $X$.
>
> *Source: WS 10.1*

^prop-51-1

> [!proof]- Proof
> *[To be proved.]*

^pf-51-1

Let $G$ be a finite group, and factor $|G| = p^k m$ where $p$ does not divide $m$.

> [!definition] Definition §51.2: Sylow $p$-Subgroup
> A **Sylow $p$-subgroup** of $G$ is a [[§4 Subgroups#^def-4-1|subgroup]] of $G$ of [[§4 Subgroups#^def-4-6|order]] $p^k$.
>
> *Source: WS 10*

^def-51-2

> [!example] Example §51.1: Sylow Subgroups of $S_3$ and $S_4$
> 1. $|S_3| = 6 = 2 \cdot 3$. The [[§51 p-Groups and Sylow Subgroups#^def-51-2|Sylow]] $2$-subgroups are $\langle (1\,2) \rangle$, $\langle (1\,3) \rangle$, $\langle (2\,3) \rangle$, and the only Sylow $3$-subgroup is $A_3 = \langle (1\,2\,3) \rangle$.
> 2. $|S_4| = 24 = 2^3 \cdot 3$. The Sylow $2$-subgroups have order $8$: they are the three subgroups $K \cup \tau K$ ($\tau$ a transposition) containing $K$, found in The Correspondence for $S_4$ and $K$ ([[§45 S₃, S₄, A₄ and A₅#^ex-45-2|Example §45.2]]). The Sylow $3$-subgroups are the four subgroups $\langle (1\,2\,3) \rangle$, $\langle (1\,2\,4) \rangle$, $\langle (1\,3\,4) \rangle$, $\langle (2\,3\,4) \rangle$.
>
> The numbers of Sylow subgroups are $3, 1$ for $S_3$ and $3, 4$ for $S_4$, each $\equiv 1 \pmod p$, as the Third Sylow Theorem ([[§52 The Sylow Theorems#^thm-52-7|Theorem §52.7]]) predicts.
>
> *Source: lecture 10/12; the counts are not from class*

^ex-51-1

*(PS 6.4.)* The order of $GL_n(\mathbb{F}_p)$ is found by counting bases of $\mathbb{F}_p^n$: an invertible matrix is the same as an ordered list of $n$ linearly independent columns.

> [!theorem] Lemma §51.2: Invertible Matrices Have Independent Columns
> Let $k$ be a field and $M \in \operatorname{Mat}_n(k)$ with columns $\vec m_1, \ldots, \vec m_n$. Then $M \in GL_n(k)$ ([[§3 Basic Examples of Groups#^def-3-6|general linear group]]) if and only if $(\vec m_1, \ldots, \vec m_n)$ is linearly independent.
>
> *Source: not from class*

^lem-51-2

> [!proof]+ Proof
> For $\vec c = (c_1, \ldots, c_n) \in k^n$, $M\vec c = \sum_{i=1}^n c_i \vec m_i$. So the columns are linearly independent if and only if $M\vec c = \vec 0$ forces $\vec c = \vec 0$, that is, if and only if the linear map $\vec c \mapsto M\vec c$ of $k^n$ is injective. If $M$ is invertible, this map has the inverse $\vec c \mapsto M^{-1}\vec c$, so it is injective. Conversely, if it is injective, its kernel is $0$, so by rank–nullity its image has dimension $n$ and is all of $k^n$; the map is then a bijective linear map, its inverse is linear, and the matrix $N$ of the inverse satisfies $MN = NM = I_n$, so $M \in GL_n(k)$ (Definition [[§3 Basic Examples of Groups#^def-3-6|§3.6]]).

^pf-51-2

*Uses:* [[§3 Basic Examples of Groups#^def-3-6|Def. §3.6]]

> [!remark]- Connections
> - Rank–nullity, used in the proof: [[Fundamental theorem of linear maps|Linear Algebra hub]]; the determinant criterion for the same property: [[Invertible ⟺ nonzero determinant|Linear Algebra hub]].

> [!theorem] Lemma §51.3: Counting Linearly Independent Tuples
> For $1 \leq k$, the number of linearly independent $k$-tuples $(\vec v_1, \ldots, \vec v_k)$ of vectors in $\mathbb{F}_p^n$ is
>
> $$
> (p^n - 1)(p^n - p) \cdots (p^n - p^{k-1}) .
> $$
>
> *Source: PS 6.4(1)*

^lem-51-3

> [!proof]+ Proof
> By induction on $k$. Throughout, $|\mathbb{F}_p^n| = p^n$: each of the $n$ entries is one of the $p$ elements of $\mathbb{F}_p$.
>
> *Base case $k = 1$.* $(\vec v_1)$ is linearly independent if and only if $\vec v_1 \neq \vec 0$: if $\vec v_1 = \vec 0$, then $1 \cdot \vec v_1 = \vec 0$ is a nontrivial relation; if $\vec v_1 \neq \vec 0$ and $c\vec v_1 = \vec 0$ with $c \neq 0$, then $\vec v_1 = c^{-1}(c\vec v_1) = \vec 0$, a contradiction. So there are $p^n - 1$ such $1$-tuples.
>
> *Inductive step.* Assume the count for $k$. If $(\vec v_1, \ldots, \vec v_{k+1})$ is linearly independent, so is $(\vec v_1, \ldots, \vec v_k)$ (a relation among the first $k$ is one among all $k+1$ with coefficient $0$ on $\vec v_{k+1}$). So it suffices to show: *for each linearly independent $(\vec v_1, \ldots, \vec v_k)$ there are exactly $p^n - p^k$ vectors $\vec v_{k+1}$ with $(\vec v_1, \ldots, \vec v_{k+1})$ linearly independent*; then the count for $k+1$ is the count for $k$ times $p^n - p^k$. Let $S = \operatorname{span}(\vec v_1, \ldots, \vec v_k)$.
> 1. *$(\vec v_1, \ldots, \vec v_{k+1})$ is dependent if and only if $\vec v_{k+1} \in S$.* If $\vec v_{k+1} = \sum_i c_i\vec v_i$, then $\sum_i c_i \vec v_i - 1\cdot\vec v_{k+1} = \vec 0$ is a nontrivial relation. Conversely, let $\sum_i c_i\vec v_i + c\,\vec v_{k+1} = \vec 0$ be a nontrivial relation. If $c = 0$ it is a nontrivial relation among $\vec v_1, \ldots, \vec v_k$, which is impossible; so $c \neq 0$ and $\vec v_{k+1} = -\sum_i c^{-1}c_i\,\vec v_i \in S$.
> 2. *$|S| = p^k$.* The map $\mathbb{F}_p^k \to S$, $(c_1, \ldots, c_k) \mapsto \sum_i c_i\vec v_i$, is onto by the definition of the span, and one-to-one: $\sum_i c_i\vec v_i = \sum_i d_i\vec v_i$ gives $\sum_i (c_i - d_i)\vec v_i = \vec 0$, so $c_i = d_i$ by independence. Hence $|S| = |\mathbb{F}_p^k| = p^k$.
>
> So exactly $p^k$ of the $p^n$ vectors $\vec v_{k+1}$ give a dependent tuple, and $p^n - p^k$ give an independent one.

^pf-51-3

For $k > n$ the product contains the factor $p^n - p^n = 0$, in agreement with there being no $n+1$ linearly independent vectors in $\mathbb{F}_p^n$.

> [!theorem] Proposition §51.4: The Order of $GL_n(\mathbb{F}_p)$
>
> $$ |GL_n(\mathbb{F}_p)| = p^{\binom{n}{2}} \prod_{k=1}^{n} (p^k - 1). $$
>
> In particular a [[§51 p-Groups and Sylow Subgroups#^def-51-2|Sylow $p$-subgroup]] of $GL_n(\mathbb{F}_p)$ ([[§3 Basic Examples of Groups#^def-3-6|Def. §3.6]], with $\mathbb{F}_p$ the field of [[§8 Invertibility and Unit Groups#^prop-8-4|§8.4]]) has order $p^{\binom{n}{2}}$, since $p \nmid p^k - 1$.
>
> *Source: stated on WS 10; PS 6*

^prop-51-4

> [!proof]+ Proof
> *(PS 6.4(2); the last step, rewriting the product, is not from the problem set.)* A matrix $M \in \operatorname{Mat}_n(\mathbb{F}_p)$ is the same as the ordered list $(\vec m_1, \ldots, \vec m_n)$ of its columns, and $M \in GL_n(\mathbb{F}_p)$ exactly when that list is linearly independent (Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-2|§51.2]]). So by Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-3|§51.3]] with $k = n$,
>
> $$
> |GL_n(\mathbb{F}_p)| = (p^n - 1)(p^n - p) \cdots (p^n - p^{n-1}) = \prod_{i=0}^{n-1} (p^n - p^i) .
> $$
>
> Each factor is $p^n - p^i = p^i(p^{n-i} - 1)$, so
>
> $$
> |GL_n(\mathbb{F}_p)| = p^{0 + 1 + \cdots + (n-1)} \prod_{i=0}^{n-1} (p^{n-i} - 1) = p^{\binom{n}{2}} \prod_{k=1}^{n} (p^k - 1),
> $$
>
> with $0 + 1 + \cdots + (n-1) = \binom{n}{2}$ and $k = n - i$. Finally $p \nmid p^k - 1$ for $k \geq 1$ (as $p \mid p^k$, it would divide $1$), so by unique factorization the largest power of $p$ dividing $|GL_n(\mathbb{F}_p)|$ is $p^{\binom{n}{2}}$, which is the order of a Sylow $p$-subgroup (Definition [[§51 p-Groups and Sylow Subgroups#^def-51-2|§51.2]]).

^pf-51-4

*Uses:* [[§51 p-Groups and Sylow Subgroups#^lem-51-2|§51.2]], [[§51 p-Groups and Sylow Subgroups#^lem-51-3|§51.3]], [[§51 p-Groups and Sylow Subgroups#^def-51-2|Def. §51.2]]

Worksheet 10 quotes this order from Problem Set 6; the proof above is the submitted solution of [[493 Problem Set 6#^hw-6-4|Problem 6.4]].

> [!theorem] Proposition §51.5: The Unitriangular Matrices Are a Sylow $p$-Subgroup of $GL_n(\mathbb{F}_p)$
> Let $P \subseteq GL_n(\mathbb{F}_p)$ be the group of matrices of the form
>
> $$ \begin{bmatrix} 1 & b_{12} & b_{13} & \cdots & b_{1(n-1)} & b_{1n} \\ 0 & 1 & b_{23} & \cdots & b_{2(n-1)} & b_{2n} \\ 0 & 0 & 1 & \cdots & b_{3(n-1)} & b_{3n} \\ & & & \ddots & & \vdots \\ 0 & 0 & 0 & \cdots & 1 & b_{(n-1)n} \\ 0 & 0 & 0 & \cdots & 0 & 1 \end{bmatrix}. $$
>
> Then $P$ is a Sylow $p$-subgroup of $GL_n(\mathbb{F}_p)$ ([[§51 p-Groups and Sylow Subgroups#^def-51-2|Def. §51.2]]).
>
> *Source: WS 10.2*

^prop-51-5

> [!proof]- Proof
> *[To be proved.]*

^pf-51-5


## Groups of Order p²

*(PS 6.3.)* A nontrivial central element, which every nontrivial $p$-group has, is enough to classify the groups of order $p^2$. The splitting step is a general criterion, isolated first.

> [!theorem] Lemma §51.6: Internal Direct Products
> Let $G$ be a finite group and $H, L \leq G$ subgroups with
> 1. every element of $H$ commuting with every element of $L$,
> 2. $H \cap L = \{e\}$, and
> 3. $|H|\,|L| = |G|$.
>
> Then $\varphi: H \times L \to G$, $\varphi(h, l) = hl$, is an isomorphism from the [[§3 Basic Examples of Groups#^def-3-2|direct product]]. Condition (1) holds in particular if $H$ is central ($H \subseteq Z(G)$, the [[§35 The Center#^def-35-2|center]]), or if $H$ and $L$ are both [[§38 Normal Subgroups#^def-38-1|normal]] and (2) holds.
>
> *Source: from PS 6.3(5)*

^lem-51-6

> [!proof]+ Proof
> *Homomorphism.* For $h, h' \in H$ and $l, l' \in L$, using $lh' = h'l$ from (1),
>
> $$
> \varphi\big((h, l)(h', l')\big) = \varphi(hh', ll') = hh'll' = hlh'l' = \varphi(h, l)\,\varphi(h', l')
> $$
>
> (the product in $H \times L$ is componentwise, Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]). *Injective.* If $\varphi(h, l) = hl = e$, then $h = l^{-1}$ lies in $H \cap L = \{e\}$, so $(h, l) = (e, e)$: the kernel is trivial. *Bijective.* $|H \times L| = |H|\,|L| = |G|$, and an injective map between finite sets of the same size is a bijection. So $\varphi$ is an isomorphism.
>
> *The two sufficient conditions for (1).* If $H \subseteq Z(G)$ (Definition [[§35 The Center#^def-35-2|§35.2]]), every $h \in H$ commutes with everything. If $H, L \trianglelefteq G$ and $H \cap L = \{e\}$, let $h \in H$, $l \in L$ and consider $hlh^{-1}l^{-1}$: grouped as $(hlh^{-1})\,l^{-1}$ it lies in $L$, since $hlh^{-1} \in L$ by normality of $L$; grouped as $h\,(lh^{-1}l^{-1})$ it lies in $H$, since $lh^{-1}l^{-1} \in H$ by normality of $H$. So $hlh^{-1}l^{-1} \in H \cap L = \{e\}$, i.e. $hl = lh$. *(Not from the problem set: the problem used only the central case.)*

^pf-51-6

*Uses:* [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§35 The Center#^def-35-2|Def. §35.2]]

> [!theorem] Theorem §51.7: Groups of Order $p^2$
> Let $p$ be prime and $|G| = p^2$. Then $G \cong \mathbb{Z}/p^2\mathbb{Z}$ or $G \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$.
>
> *Source: PS 6.3*

^thm-51-7

> [!proof]+ Proof
> Throughout: if $h \in G$ has finite order $c$, then $|\langle h \rangle| = c$ and $h^N = e$ iff $c \mid N$ (Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]]); and *every $h \neq e$ in $G$ has order $p$ or $p^2$*, since $|\langle h \rangle|$ divides $p^2$ (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]) and is not $1$.
>
> By Theorem [[§35 The Center#^thm-35-3|§35.3]] (PS 3.5) there is $z \neq e$ with $zg = gz$ for all $g \in G$.
>
> *(1) If $z$ has order $p^2$.* Then $\langle z \rangle \subseteq G$ both have $p^2$ elements, so $G = \langle z \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$ (Proposition [[§17 Cyclic Groups#^prop-17-3|§17.3]](3)). From now on $z$ has order $p$.
>
> *(2) $\langle z \rangle \trianglelefteq G$ and $G/\langle z \rangle \cong \mathbb{Z}/p\mathbb{Z}$.* By induction on $k \geq 0$, $gz^k = z^kg$ for every $g \in G$: $gz^k = (gz^{k-1})z = z^{k-1}gz = z^{k-1}zg = z^kg$. So $g h g^{-1} = h$ for all $h \in \langle z \rangle = \{e, z, \ldots, z^{p-1}\}$, and $\langle z \rangle$ is normal (Definition [[§38 Normal Subgroups#^def-38-1|§38.1]]); the quotient $G/\langle z \rangle$ is a group (Definition [[§40 Quotient Groups#^def-40-1|§40.1]]) of order $[G : \langle z \rangle] = p^2/p = p$ (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]), hence $\cong \mathbb{Z}/p\mathbb{Z}$ (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]], PS 2.5).
>
> *(3) A generator.* Let $\bar g$ generate $G/\langle z \rangle$ and let $g \in G$ with $g\langle z \rangle = \bar g$. As $\bar g$ generates a group of order $p$, it has order $p$, so $g^p\langle z \rangle = \bar g^{\,p} = \langle z \rangle$ and $g^p \in \langle z \rangle$: $g^p = z^m$, and writing $m = qp + a$ with $0 \leq a < p$, $g^p = (z^p)^q z^a = z^a$. Also $g \neq e$, since $\bar g \neq \langle z \rangle$ (the quotient has $p \geq 2$ elements).
>
> *(4) If $a \neq 0$.* Then $p \nmid a$, so $g^p = z^a \neq e$; $g$ has order $p$ or $p^2$, and not $p$, so order $p^2$, and $G = \langle g \rangle \cong \mathbb{Z}/p^2\mathbb{Z}$ as in (1).
>
> *(5) If $a = 0$.* Then $g^p = e$, so $g$ has order $p$ and $\langle g \rangle \cong \mathbb{Z}/p\mathbb{Z} \cong \langle z \rangle$. The subgroup $\langle z \rangle \cap \langle g \rangle$ of $\langle g \rangle$ has order $1$ or $p$ (Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]); order $p$ would give $\langle g \rangle \subseteq \langle z \rangle$, so $g \in \langle z \rangle$ and $\bar g = \langle z \rangle$, which is false. So $\langle z \rangle \cap \langle g \rangle = \{e\}$. Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-6|§51.6]] with $H = \langle z \rangle$ (central) and $L = \langle g \rangle$, $|H|\,|L| = p \cdot p = |G|$, gives
>
> $$
> G \cong \langle z \rangle \times \langle g \rangle \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z} .
> $$

^pf-51-7

*Uses:* [[§17 Cyclic Groups#^prop-17-3|§17.3]], [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]], [[§35 The Center#^thm-35-3|§35.3]], [[§38 Normal Subgroups#^def-38-1|Def. §38.1]], [[§40 Quotient Groups#^def-40-1|Def. §40.1]], [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]], [[§51 p-Groups and Sylow Subgroups#^lem-51-6|§51.6]]

> [!theorem] Corollary §51.8: Groups of Order $p^2$ Are Abelian
> Every group of order $p^2$, $p$ prime, is [[§1 The Definition of a Group#^def-1-2|abelian]].

^cor-51-8

> [!proof]+ Proof
> By Theorem [[§51 p-Groups and Sylow Subgroups#^thm-51-7|§51.7]], $G$ is isomorphic to $\mathbb{Z}/p^2\mathbb{Z}$ or to $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$, both abelian (the product componentwise, Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]); and a group isomorphic to an abelian group is abelian, since $\varphi(ab) = \varphi(a)\varphi(b) = \varphi(b)\varphi(a) = \varphi(ba)$ and $\varphi$ is injective.

^pf-51-8

*Uses:* [[§51 p-Groups and Sylow Subgroups#^thm-51-7|§51.7]], [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]]

> [!remark] Remark: Groups of Order $p^k$
> Speyer, on Problem Set 6: one can continue classifying groups of order $p^k$ in this way for any particular $k$, although the number of cases grows rapidly; groups of order $p^3$ are “tractable for an undergraduate”. The largest exponent fully classified is $k = 7$ (O'Brien and Vaughan-Lee, “The groups with order $p^7$ for odd prime $p$”, *Journal of Algebra*, 2005), with partial progress on $k = 8$ and $9$ published as recently as 2026.
>
> *Source: PS 6, stated, not proved*

^rem-51-2

*$GL_n$ elsewhere:* ← [[§50 S₃, S₄, Aₙ and GLₙ#GLₙ, SLₙ and O(n)|Chapter 9]] · no later appearance yet · [[Matrix groups GLₙ, SLₙ and O(n)|all appearances]]
