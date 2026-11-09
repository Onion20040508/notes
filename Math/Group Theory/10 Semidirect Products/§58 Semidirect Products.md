---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 58
tags: [group-theory, math493]
---
← [[§57 Internal and External Direct Products]] · ↑ [[· 10 Semidirect Products]] · [[§59 Representations and Subrepresentations]] →

*Reference: not covered in the Pinter chapters used so far.*

> [!definition] Definition §58.1: Internal Semidirect Product
> Let $G$ be a group, $N \trianglelefteq G$ a normal subgroup, and $S \leq G$ a subgroup (not necessarily normal), with $N \cap S = \{e\}$ and $G = NS$. Then $G$ is the **(internal) semidirect product** of $N$ and $S$.
>
> *Source: lecture 10/26; WS 11*

^def-58-1

> [!example] Example §58.1: $S_3$ and $S_n$
> $G = S_3$, $N = A_3 = \langle (1\,2\,3) \rangle$ (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]) and $S = \langle (1\,2) \rangle$. Here $A_3 \trianglelefteq S_3$, having index $2$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]]); $A_3 \cap S = \{e\}$, since $(1\,2)$ is odd (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|§21.2]]); and $A_3S = S_3$, since $A_3S$ is a subgroup (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]) containing subgroups of orders $3$ and $2$, so its order is divisible by $6$ (Lagrange). So $S_3$ is the semidirect product of $A_3$ and $\langle (1\,2) \rangle$. It is not a direct product: $S$ is not normal, as $(1\,3)(1\,2)(1\,3) = (2\,3) \notin S$. The same argument shows that $S_n$ ($n \geq 2$) is the semidirect product of $A_n$ and $\langle (1\,2) \rangle$ (not from class).
>
> *Source: lecture 10/26*

^ex-58-1

> [!remark] Remark: Why More Data Is Needed
> For a direct product, $N_1$ and $N_2$ alone determine $G$. For a semidirect product, $N$ and $S$ do not: one also needs to know how $S$ acts on $N$ (Example [[§58 Semidirect Products#^ex-58-2|§58.2]]).
>
> *Source: lecture 10/26*

^rem-58-1

> [!example] Example §58.2: $\mathbb{Z}/6\mathbb{Z}$ and $S_3$: Same $N$ and $S$, Different Groups
> $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$ and $S_3$ are both semidirect products of a normal subgroup of order $3$ and a subgroup of order $2$, but they are not isomorphic.
> - *$\mathbb{Z}/6\mathbb{Z}$.* Take $N = \{0, 2, 4\}$ of order $3$ and $S = \{0, 3\}$ of order $2$. $N$ is normal since the group is abelian; $N \cap S = \{0\}$; and $N + S$ is a subgroup (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]) whose order is divisible by $3$ and $2$ (Lagrange), hence is $6$. (Here $S$ is normal too, and $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ by Theorem [[§57 Internal and External Direct Products#^thm-57-1|§57.1]].)
> - *$S_3$.* $N = A_3$ and $S = \langle (1\,2) \rangle$, by Example [[§58 Semidirect Products#^ex-58-1|§58.1]].
> - *Not isomorphic.* $\mathbb{Z}/6\mathbb{Z}$ is abelian and $S_3$ is not: $(1\,2)(2\,3) = (1\,2\,3) \neq (1\,3\,2) = (2\,3)(1\,2)$.
>
> In both cases $N \cong \mathbb{Z}/3\mathbb{Z}$ and $S \cong \mathbb{Z}/2\mathbb{Z}$ (groups of prime order, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-7|§29.7]]); what differs is the action of $S$ on $N$: trivial in $\mathbb{Z}/6\mathbb{Z}$, inversion in $S_3$ (Example [[§58 Semidirect Products#^ex-58-4|§58.4]] below).
>
> *Source: lecture 10/26*

^ex-58-2

> [!theorem] Proposition §58.1: The Quotient by $N$
> In an internal semidirect product, $G/N \cong S$.
>
> *Source: WS 11.2*

^prop-58-1

> [!proof]+ Proof
> *Idea:* this is the Second Isomorphism Theorem.
>
> By the Second Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-5|§41.5]]), $G/N = SN/N \cong S/(S \cap N) = S/\{e\} \cong S$ (here $SN = NS$, as $N$ is normal). Explicitly, $s \mapsto sN$ is an isomorphism $S \to G/N$.

^pf-58-1

*Uses:* [[§41 The First and Second Isomorphism Theorems#^thm-41-5|§41.5]]

> [!theorem] Proposition §58.2: Unique Factorization $g = ns$
> In an internal semidirect product, every $g \in G$ can be written in exactly one way as $g = ns$ with $n \in N$ and $s \in S$.
>
> *Source: WS 11.3*

^prop-58-2

> [!proof]+ Proof
> *Idea:* two factorizations differ by an element of $N \cap S = \{e\}$.
>
> *(Done on the boards 10/26; written out here.)* Existence is $G = NS$. If $ns = n's'$ with $n, n' \in N$ and $s, s' \in S$, then $n'^{-1}n = s's^{-1}$; the left side lies in $N$ and the right side in $S$, so both lie in $N \cap S = \{e\}$. Hence $n = n'$ and $s = s'$.

^pf-58-2

> [!theorem] Proposition §58.3: $S$ Acts on $N$ by Automorphisms
> In an internal semidirect product, for $s \in S$ let $\varphi(s): N \to N$, $n \mapsto sns^{-1}$. Then:
>
> 1. $\varphi(s)$ is an automorphism of $N$, an isomorphism $N \to N$ (Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|§18.1]]);
> 2. $\varphi: S \to \operatorname{Aut}(N)$ is a group homomorphism: $\varphi(ss') = \varphi(s) \circ \varphi(s')$.
>
> Equivalently, $s \star n = sns^{-1}$ is an action of $S$ on $N$ by automorphisms.
>
> *Source: WS 11.4; lecture 10/26*

^prop-58-3

> [!proof]+ Proof
> *Idea:* $\varphi(s)$ is conjugation by $s$, restricted to the normal subgroup $N$.
>
> *(Done on the boards 10/26; written out here.)* **(1)** $\varphi(s)$ maps $N$ into $N$ because $N$ is normal. It is the restriction to $N$ of conjugation $c_s: G \to G$, which is a homomorphism (Conjugation Is an Automorphism, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], PS 1.2), so $\varphi(s)$ is a homomorphism $N \to N$. It has inverse $\varphi(s^{-1})$: $s^{-1}(sns^{-1})s = n$ and $s(s^{-1}ns)s^{-1} = n$, with $s^{-1}ns \in N$ again by normality. So $\varphi(s)$ is a bijective homomorphism $N \to N$.
>
> **(2)** For $n \in N$, $\varphi(ss')(n) = ss'\,n\,(ss')^{-1} = s\,(s'ns'^{-1})\,s^{-1} = \varphi(s)\big(\varphi(s')(n)\big)$.

^pf-58-3

*Uses:* [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]

> [!theorem] Proposition §58.4: Multiplication in the Form $ns$
> In an internal semidirect product, for $n_1, n_2 \in N$ and $s_1, s_2 \in S$,
>
> $$
> (n_1s_1)(n_2s_2) = \big(n_1\,\varphi(s_1)(n_2)\big)\,(s_1s_2),
> $$
>
> with $n_1\varphi(s_1)(n_2) \in N$ and $s_1s_2 \in S$.
>
> *Source: WS 11.5*

^prop-58-4

> [!proof]+ Proof
> *Idea:* move $s_1$ past $n_2$ at the cost of conjugating $n_2$.
>
> *(Done on the boards 10/26; written out here.)* Insert $s_1^{-1}s_1 = e$ between $n_2$ and $s_2$:
>
> $$
> n_1s_1n_2s_2 = n_1\,(s_1n_2s_1^{-1})\,s_1s_2 = n_1\,\varphi(s_1)(n_2)\,s_1s_2,
> $$
>
> and $\varphi(s_1)(n_2) \in N$ by Proposition [[§58 Semidirect Products#^prop-58-3|§58.3]](1).

^pf-58-4

*Uses:* [[§58 Semidirect Products#^prop-58-3|§58.3]]

> [!remark] Remark: The Data $(N, S, \varphi)$
> By Propositions [[§58 Semidirect Products#^prop-58-2|§58.2]] and [[§58 Semidirect Products#^prop-58-4|§58.4]] (WS 11.3 and 11.5), the multiplication of $G$ is determined by $N$, $S$, and the homomorphism $\varphi: S \to \operatorname{Aut}(N)$ given by conjugation. This suggests building a group from the triple $(N, S, \varphi)$ alone, with no ambient group $G$, where $N$ and $S$ are now any two groups and $\varphi$ is any homomorphism $S \to \operatorname{Aut}(N)$.
>
> *Source: lecture 10/26*

^rem-58-2

> [!definition] Definition §58.2: External Semidirect Product
> Let $N$ and $S$ be groups and $\varphi: S \to \operatorname{Aut}(N)$ a group homomorphism. The **external semidirect product** of $N$ and $S$ by $\varphi$ is the set $\{(n, s) : n \in N,\ s \in S\}$ with multiplication
>
> $$
> (n_1, s_1) \cdot (n_2, s_2) = \big(n_1\,\varphi(s_1)(n_2),\ s_1s_2\big).
> $$
>
> It is written $N \rtimes_\varphi S$, or $N \rtimes S$ when $\varphi$ is clear. Some authors put the normal subgroup second and write $S \ltimes_\varphi N$; this course writes $N \rtimes_\varphi S$.
>
> *Source: WS 11; lecture 10/26*

^def-58-2

> [!theorem] Theorem §58.5: $N \rtimes_\varphi S$ Is a Group
> $N \rtimes_\varphi S$ is a group, with identity $(e_N, e_S)$ and inverse
>
> $$
> (n, s)^{-1} = \big(\varphi(s^{-1})(n^{-1}),\ s^{-1}\big).
> $$
>
> *Source: WS 11.6*

^thm-58-5

> [!proof]+ Proof
> *Idea:* expand both sides of each axiom; associativity uses that $\varphi$ is a homomorphism into $\operatorname{Aut}(N)$, so $\varphi_{s_1}\varphi_{s_2} = \varphi_{s_1s_2}$ and each $\varphi_s$ respects products.
>
> *(Done on the boards 10/26, where associativity was the main check; written out here.)* Write $\varphi_s = \varphi(s)$. Since $\varphi$ is a homomorphism, $\varphi_{s}\varphi_{s'} = \varphi_{ss'}$ and $\varphi_{e} = \mathrm{id}_N$; since each $\varphi_s$ is a homomorphism, $\varphi_s(ab) = \varphi_s(a)\varphi_s(b)$ and $\varphi_s(e) = e$.
>
> *Associativity.* On one side,
>
> $$
> \big((n_1, s_1)(n_2, s_2)\big)(n_3, s_3) = \big(n_1\varphi_{s_1}(n_2),\, s_1s_2\big)(n_3, s_3) = \big(n_1\varphi_{s_1}(n_2)\,\varphi_{s_1s_2}(n_3),\ s_1s_2s_3\big).
> $$
>
> On the other,
>
> $$
> (n_1, s_1)\big((n_2, s_2)(n_3, s_3)\big) = (n_1, s_1)\big(n_2\varphi_{s_2}(n_3),\, s_2s_3\big) = \big(n_1\,\varphi_{s_1}\!\big(n_2\varphi_{s_2}(n_3)\big),\ s_1s_2s_3\big).
> $$
>
> These agree, because $\varphi_{s_1}\big(n_2\varphi_{s_2}(n_3)\big) = \varphi_{s_1}(n_2)\,\varphi_{s_1}\varphi_{s_2}(n_3) = \varphi_{s_1}(n_2)\,\varphi_{s_1s_2}(n_3)$.
>
> *Identity.* $(e, e)(n, s) = (e\,\varphi_e(n),\, s) = (n, s)$ and $(n, s)(e, e) = (n\,\varphi_s(e),\, s) = (n, s)$.
>
> *Inverse.* With $(n, s)^{-1}$ as stated,
>
> $$
> (n, s)\big(\varphi_{s^{-1}}(n^{-1}), s^{-1}\big) = \big(n\,\varphi_s\varphi_{s^{-1}}(n^{-1}),\ e\big) = (n\,n^{-1}, e) = (e, e),
> $$
>
> $$
> \big(\varphi_{s^{-1}}(n^{-1}), s^{-1}\big)(n, s) = \big(\varphi_{s^{-1}}(n^{-1})\,\varphi_{s^{-1}}(n),\ e\big) = \big(\varphi_{s^{-1}}(n^{-1}n), e\big) = (e, e).
> $$

^pf-58-5

> [!theorem] Theorem §58.6: Internal and External Semidirect Products Agree
> 1. If $G$ is the internal semidirect product of $N$ and $S$, and $\varphi: S \to \operatorname{Aut}(N)$ is conjugation (Proposition [[§58 Semidirect Products#^prop-58-3|§58.3]]), then $(n, s) \mapsto ns$ is an isomorphism $N \rtimes_\varphi S \to G$.
> 2. Conversely, in $N \rtimes_\varphi S$ the subsets $\tilde N = \{(n, e) : n \in N\}$ and $\tilde S = \{(e, s) : s \in S\}$ are subgroups isomorphic to $N$ and $S$, $\tilde N$ is normal, $N \rtimes_\varphi S$ is the internal semidirect product of $\tilde N$ and $\tilde S$, and conjugation by $\tilde S$ on $\tilde N$ recovers $\varphi$:
>
> $$
> (e, s)(n, e)(e, s)^{-1} = \big(\varphi(s)(n), e\big).
> $$
>
> *Source: WS 11; lecture 10/26*

^thm-58-6

> [!proof]+ Proof
> *Idea:* (1) is WS 11.3 and 11.5 read as a statement about the map $(n, s) \mapsto ns$; (2) computes inside $N \rtimes_\varphi S$ with the multiplication rule.
>
> **(1)** The map is a homomorphism by Multiplication in the Form $ns$ (Proposition [[§58 Semidirect Products#^prop-58-4|§58.4]]), which says exactly that $(n_1, s_1)(n_2, s_2) \mapsto (n_1s_1)(n_2s_2)$, and a bijection by Unique Factorization (Proposition [[§58 Semidirect Products#^prop-58-2|§58.2]]).
>
> **(2)** *(The displayed formula is from the board 10/26.)* By the multiplication rule, $(n, e)(n', e) = (n\,\varphi_e(n'), e) = (nn', e)$ and $(e, s)(e, s') = (\varphi_s(e), ss') = (e, ss')$, so $n \mapsto (n, e)$ and $s \mapsto (e, s)$ are injective homomorphisms, with images $\tilde N$ and $\tilde S$. The map $(n, s) \mapsto s$ is a homomorphism $N \rtimes_\varphi S \to S$ (the second coordinate of a product is $s_1s_2$) with kernel $\tilde N$, so $\tilde N$ is normal (Kernels Are Normal, Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]). $\tilde N \cap \tilde S = \{(e, e)\}$, and $(n, e)(e, s) = (n\,\varphi_e(e), s) = (n, s)$, so $\tilde N\tilde S$ is everything. Finally, using $(e, s)^{-1} = (e, s^{-1})$ (Theorem [[§58 Semidirect Products#^thm-58-5|§58.5]]),
>
> $$
> (e, s)(n, e)(e, s^{-1}) = \big(\varphi_s(n), s\big)(e, s^{-1}) = \big(\varphi_s(n)\,\varphi_s(e), e\big) = \big(\varphi_s(n), e\big).
> $$

^pf-58-6

*Uses:* [[§58 Semidirect Products#^prop-58-4|§58.4]], [[§58 Semidirect Products#^prop-58-2|§58.2]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§58 Semidirect Products#^thm-58-5|§58.5]]

> [!theorem] Proposition §58.7: Direct Products as a Special Case
> 1. If $\varphi: S \to \operatorname{Aut}(N)$ is trivial ($\varphi(s) = \mathrm{id}_N$ for all $s$), then $N \rtimes_\varphi S = N \times S$.
> 2. In an internal semidirect product of $N$ and $S$, with $\varphi$ given by conjugation, $\varphi$ is trivial exactly when every element of $S$ commutes with every element of $N$.
> 3. Given $G = NS$ as in (2), this happens exactly when $S$ is also normal in $G$.
>
> *Source: not from class*

^prop-58-7

> [!proof]+ Proof
> *Idea:* with trivial action the multiplication rule is componentwise; $\varphi(s)$ is conjugation by $s$.
>
> **(1)** With $\varphi(s_1) = \mathrm{id}_N$, the rule of Definition [[§58 Semidirect Products#^def-58-2|§58.2]] becomes $(n_1, s_1)(n_2, s_2) = (n_1n_2, s_1s_2)$, the componentwise product of $N \times S$ (Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]) on the same set of pairs.
>
> **(2)** $\varphi(s) = \mathrm{id}_N$ means $sns^{-1} = n$, i.e. $sn = ns$, for every $n \in N$; so $\varphi$ is trivial iff this holds for every $s \in S$.
>
> **(3)** If $S$ commutes with $N$, let $g = ns \in G$ with $n \in N$, $s \in S$. Then $sSs^{-1} = S$, and $ns'n^{-1} = s'$ for every $s' \in S$, so
>
> $$
> gSg^{-1} = n\,(sSs^{-1})\,n^{-1} = nSn^{-1} = S,
> $$
>
> and $S$ is normal. Conversely, if $S$ is normal, then $N$ and $S$ are normal subgroups with $N \cap S = \{e\}$, and Normal Subgroups with Trivial Intersection Commute (Proposition [[§47 Commutators#^prop-47-8|§47.8]]) shows that they commute.

^pf-58-7

*Uses:* [[§58 Semidirect Products#^def-58-2|Def. §58.2]], [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§47 Commutators#^prop-47-8|§47.8]]

Together with Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]](1), this recovers Theorem [[§57 Internal and External Direct Products#^thm-57-1|§57.1]] (WS 11.1).

> [!example] Example §58.3: $\mathbb{Z}/7\mathbb{Z} \rtimes \mathbb{Z}/3\mathbb{Z}$
> Let $N = \mathbb{Z}/7\mathbb{Z}$ and $S = \mathbb{Z}/3\mathbb{Z}$, and let $k \in \mathbb{Z}/3\mathbb{Z}$ act on $x \in \mathbb{Z}/7\mathbb{Z}$ by
>
> $$
> k \star x = 2^k x \bmod 7, \qquad \text{i.e.\ } \varphi(k)(x) = 2^k x.
> $$
>
> Multiplication by $2$ is an automorphism of $\mathbb{Z}/7\mathbb{Z}$ (a homomorphism, invertible since $2 \cdot 4 \equiv 1$). It is well defined on $k \bmod 3$ and gives an action because $2^3 = 8 \equiv 1 \pmod 7$: applying it three times, $x \mapsto 2x \mapsto 4x \mapsto 8x = x$. So there is a group $\mathbb{Z}/7\mathbb{Z} \rtimes_{k \mapsto 2^k} \mathbb{Z}/3\mathbb{Z}$ of order $21$, with
>
> $$
> (x_1, k_1)(x_2, k_2) = (x_1 + 2^{k_1}x_2,\ k_1 + k_2).
> $$
>
> No group of order $21$ had to be found first: the triple $(N, S, \varphi)$ is enough. The group is not abelian: $(1, 0)(0, 1) = (1, 1)$ but $(0, 1)(1, 0) = (2, 1)$. (Not from class, checked by computer: its center is trivial, and it has $14$ elements of order $3$, so $n_3 = 7$, the second candidate in Example [[§56 Simple Groups of Small Order#^ex-56-1|§56.1]], while $n_7 = 1$ as it must be.)
>
> *Source: lecture 10/26*

^ex-58-3

![[m493-55-1.svg]]

*(Not from lecture; figure added.)* The action in Example [[§58 Semidirect Products#^ex-58-3|§58.3]]: the generator $1 \in \mathbb{Z}/3\mathbb{Z}$ permutes $\mathbb{Z}/7\mathbb{Z}$ by $x \mapsto 2x$, fixing $0$ and cycling the other six elements in two $3$-cycles. Because $2^3 \equiv 1 \pmod 7$, applying it three times is the identity, which is what makes $k \mapsto (x \mapsto 2^kx)$ a homomorphism $\mathbb{Z}/3\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/7\mathbb{Z})$.

![[m493-55-2.svg]]

*(Not from lecture; figure added.)* The $21$ elements $(n, s)$ of $\mathbb{Z}/7\mathbb{Z} \rtimes \mathbb{Z}/3\mathbb{Z}$. The bottom row is the normal subgroup $\tilde N$, and the rows are its cosets, one for each $s$: this is $G/\tilde N \cong \mathbb{Z}/3\mathbb{Z}$ (Proposition [[§58 Semidirect Products#^prop-58-1|§58.1]]). The column $n = 0$ is $\tilde S$, which is not normal. The arrows are left multiplication by $(0, 1)$ on the bottom row, $(0, 1)(n, 0) = (2n, 1)$: moving up a row applies the action.

> [!example] Example §58.4: $S_3$ as an External Semidirect Product
> *(Not from class.)* Let $\varphi: \mathbb{Z}/2\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/3\mathbb{Z})$ send $1$ to $x \mapsto -x$. Then $\mathbb{Z}/3\mathbb{Z} \rtimes_\varphi \mathbb{Z}/2\mathbb{Z} \cong S_3$: in $S_3 = A_3 \rtimes \langle (1\,2) \rangle$ (Example [[§58 Semidirect Products#^ex-58-1|§58.1]]), conjugation by $(1\,2)$ sends $(1\,2\,3)$ to $(2\,1\,3) = (1\,3\,2) = (1\,2\,3)^{-1}$, which under $A_3 \cong \mathbb{Z}/3\mathbb{Z}$, $(1\,2\,3)^x \leftrightarrow x$, is $x \mapsto -x$. Apply part (1) of Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]]. With $\varphi$ trivial instead, one gets $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$.

^ex-58-4

> [!remark] Remark: Notation and Mnemonics
> Conventions differ on the order: $N \rtimes S$ and $S \ltimes N$ mean the same group, with $N$ normal and $S$ acting. Two mnemonics from the lecture: the triangle in $\rtimes$ or $\ltimes$ is like the symbol $\trianglelefteq$ and points toward the normal subgroup; and the vertical stroke stands on the side of $S$, the group that acts on $N$. Note that $N$ is not assumed to be normal in anything at the start; the input is just two groups and an action, and $N$ becomes normal in $N \rtimes_\varphi S$ (Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]](2)).
>
> *Source: lecture 10/26*

^rem-58-3

## Groups of Affine Maps

*Source: Problem Set 9, Problem 9.5 (submitted). The examples after the proposition are not from class.*

Semidirect products appear concretely as groups of affine maps $x \mapsto gx + \lambda$ of a vector space: the translations form the normal subgroup, and the linear parts act on them.

> [!theorem] Proposition §58.8: Groups of Affine Maps Are Semidirect Products
> Let $V$ be a vector space over a field $k$, let $G$ be a subgroup of $GL(V)$, and let $L \subseteq V$ be a subgroup of the additive group of $V$ with $gL = L$ for each $g \in G$. For $g \in G$ and $\lambda \in L$ let $\sigma_{(g, \lambda)}: V \to V$, $\sigma_{(g, \lambda)}(x) = gx + \lambda$, and let $\Gamma = \{\sigma_{(g, \lambda)} : g \in G,\ \lambda \in L\}$.
>
> 1. $\Gamma$ is a group under composition, and
>
> $$
> \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)} = \sigma_{(g_1 g_2,\ g_1\lambda_2 + \lambda_1)}.
> $$
>
> 2. $\varphi(g)(\lambda) = g\lambda$ defines a homomorphism $\varphi: G \to \operatorname{Aut}(L)$, and $\Psi(\lambda, g) = \sigma_{(g, \lambda)}$ is an isomorphism $L \rtimes_\varphi G \to \Gamma$ (Definition [[§58 Semidirect Products#^def-58-2|§58.2]]). So $\Gamma \cong L \rtimes G$, where $G$ acts on $L$ through its action on $V$.
>
> *Source: PS 9.5*

^prop-58-8

> [!proof]+ Proof
> *Idea:* Composing two affine maps multiplies the linear parts and adds the first linear part applied to the second translation, which is exactly the multiplication rule of $L \rtimes G$.
>
> *(Problem Set 9, Problem 9.5, as submitted.)* We use throughout that $gL = L$ for every $g \in G$.
>
> **(1)** *Closure.* Let $g_1, g_2 \in G$ and $\lambda_1, \lambda_2 \in L$. For $x \in V$, by linearity of $g_1$,
>
> $$
> \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)}(x) = g_1(g_2 x + \lambda_2) + \lambda_1 = g_1 g_2\, x + (g_1\lambda_2 + \lambda_1).
> $$
>
> Here $g_1 g_2 \in G$ since $G$ is a group, $g_1 \lambda_2 \in g_1 L = L$, and $g_1\lambda_2 + \lambda_1 \in L$ since $L$ is closed under addition. Hence
>
> $$
> \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)} = \sigma_{(g_1 g_2,\ g_1\lambda_2 + \lambda_1)} \in \Gamma. \tag{$\dagger$}
> $$
>
> *Identity.* Since $I \in G$ and $0 \in L$, $\sigma_{(I, 0)} \in \Gamma$, and $\sigma_{(I, 0)}(x) = x$ for all $x \in V$, so $\sigma_{(I, 0)} = \mathrm{id}_V$.
>
> *Inverses.* Let $g \in G$ and $\lambda \in L$. Then $g^{-1} \in G$, $g^{-1}\lambda \in g^{-1}L = L$, and $-g^{-1}\lambda \in L$ since $L$ is a subgroup; so $\sigma_{(g^{-1}, -g^{-1}\lambda)} \in \Gamma$. By $(\dagger)$,
>
> $$
> \begin{aligned}\sigma_{(g^{-1}, -g^{-1}\lambda)} \circ \sigma_{(g, \lambda)} &= \sigma_{(g^{-1}g,\ g^{-1}\lambda - g^{-1}\lambda)} = \sigma_{(I, 0)}, \\
> \sigma_{(g, \lambda)} \circ \sigma_{(g^{-1}, -g^{-1}\lambda)} &= \sigma_{(gg^{-1},\ -gg^{-1}\lambda + \lambda)} = \sigma_{(I, 0)}.\end{aligned}
> $$
>
> Hence $\sigma_{(g^{-1}, -g^{-1}\lambda)}$ is an inverse of $\sigma_{(g, \lambda)}$ in $\Gamma$.
>
> *Associativity.* Composition of functions is associative.
>
> Hence $\Gamma$ is a group under composition.
>
> **(2)** *The action.* Define $\varphi: G \to \operatorname{Aut}(L)$ by
>
> $$
> \varphi(g)(\lambda) = g\lambda \qquad (g \in G,\ \lambda \in L).
> $$
>
> For $g \in G$: since $gL = L$, $\varphi(g)$ maps $L$ onto $L$; it is injective since $g$ is invertible; and $g(\lambda + \mu) = g\lambda + g\mu$ by linearity of $g$. Hence $\varphi(g)$ is an automorphism of the additive group $L$. For $g_1, g_2 \in G$ and $\lambda \in L$,
>
> $$
> \varphi(g_1 g_2)(\lambda) = g_1(g_2\lambda) = \varphi(g_1)\big(\varphi(g_2)(\lambda)\big),
> $$
>
> so $\varphi$ is a group homomorphism. Thus $G$ acts on $L$ by $g \cdot \lambda = g\lambda$, and the external semidirect product $L \rtimes_\varphi G$ is the set of pairs $(\lambda, g)$ with $\lambda \in L$, $g \in G$, and multiplication
>
> $$
> (\lambda_1, g_1)(\lambda_2, g_2) = \big(\lambda_1 + \varphi(g_1)(\lambda_2),\ g_1 g_2\big) = \big(\lambda_1 + g_1\lambda_2,\ g_1 g_2\big).
> $$
>
> *The isomorphism.* Define
>
> $$
> \Psi: L \rtimes_\varphi G \to \Gamma, \qquad \Psi(\lambda, g) = \sigma_{(g, \lambda)}.
> $$
>
> By $(\dagger)$,
>
> $$
> \Psi(\lambda_1, g_1) \circ \Psi(\lambda_2, g_2) = \sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)} = \sigma_{(g_1 g_2,\ \lambda_1 + g_1\lambda_2)} = \Psi\big((\lambda_1, g_1)(\lambda_2, g_2)\big),
> $$
>
> so $\Psi$ is a homomorphism. It is surjective by the definition of $\Gamma$. For injectivity, suppose $\sigma_{(g, \lambda)} = \sigma_{(g', \lambda')}$. Evaluating at $x = 0$ gives $\lambda = \lambda'$, and then $gx = g'x$ for all $x \in V$, so $g = g'$. Hence $\Psi$ is an isomorphism, and
>
> $$
> \Gamma \cong L \rtimes_\varphi G,
> $$
>
> where $G$ acts on $L$ through its action on $V$: $g \cdot \lambda = g\lambda$.

^pf-58-8

The injectivity step shows that an element of $\Gamma$ determines its pair: $\lambda = \sigma_{(g, \lambda)}(0)$, and then $g$. So $g$ is well defined as the *linear part* of $\sigma_{(g, \lambda)}$, and $\lambda$ as its *translation part*.

> [!theorem] Proposition §58.9: Translations Form the Normal Subgroup
> In the setting of Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]], let $T = \{\sigma_{(I, \lambda)} : \lambda \in L\}$, the translations by elements of $L$, and $G_0 = \{\sigma_{(g, 0)} : g \in G\}$, the elements of $\Gamma$ fixing $0$.
>
> 1. The linear part $\ell: \Gamma \to G$, $\ell(\sigma_{(g, \lambda)}) = g$, is a surjective homomorphism with kernel $T$. So $T \trianglelefteq \Gamma$ and $\Gamma/T \cong G$.
> 2. Conjugating a translation by $\sigma_{(g, \lambda)}$ applies the linear part to the translation vector:
>
> $$
> \sigma_{(g, \lambda)} \circ \sigma_{(I, \mu)} \circ \sigma_{(g, \lambda)}^{-1} = \sigma_{(I, g\mu)}.
> $$
>
> 3. $\Gamma$ is the internal semidirect product of $T$ and $G_0$ (Definition [[§58 Semidirect Products#^def-58-1|§58.1]]).
>
> *Source: not from class*

^prop-58-9

> [!proof]+ Proof
> *Idea:* Everything follows from the composition rule $(\dagger)$ in the proof of Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]].
>
> *(Not from class; filled in.)* **(1)** $\ell$ is well defined by the remark before the proposition. By the composition rule of Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]](1), $\ell(\sigma_{(g_1, \lambda_1)} \circ \sigma_{(g_2, \lambda_2)}) = g_1g_2 = \ell(\sigma_{(g_1, \lambda_1)})\,\ell(\sigma_{(g_2, \lambda_2)})$, so $\ell$ is a homomorphism. It is surjective, since $\ell(\sigma_{(g, 0)}) = g$. Its kernel consists of the $\sigma_{(g, \lambda)}$ with $g = I$, which is $T$. So $T \trianglelefteq \Gamma$, as a kernel, and $\Gamma/T \cong G$ by the First Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]).
>
> **(2)** By the proof of Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]](1), $\sigma_{(g, \lambda)}^{-1} = \sigma_{(g^{-1}, -g^{-1}\lambda)}$. Applying the composition rule twice,
>
> $$
> \sigma_{(I, \mu)} \circ \sigma_{(g^{-1}, -g^{-1}\lambda)} = \sigma_{(g^{-1},\ -g^{-1}\lambda + \mu)}, \qquad \sigma_{(g, \lambda)} \circ \sigma_{(g^{-1},\ -g^{-1}\lambda + \mu)} = \sigma_{(gg^{-1},\ g(-g^{-1}\lambda + \mu) + \lambda)} = \sigma_{(I, g\mu)}.
> $$
>
> **(3)** $T$ is normal by (1). $G_0$ is a subgroup: $\sigma_{(I, 0)} \in G_0$, $\sigma_{(g_1, 0)} \circ \sigma_{(g_2, 0)} = \sigma_{(g_1g_2, 0)}$ by the composition rule, and $\sigma_{(g, 0)}^{-1} = \sigma_{(g^{-1}, 0)}$ by the formula for inverses in (2). If $\sigma_{(I, \lambda)} = \sigma_{(g, 0)}$, then $\lambda = 0$ and $g = I$ by the remark before the proposition, so $T \cap G_0 = \{\mathrm{id}_V\}$. Finally, by the composition rule, every element of $\Gamma$ is a product
>
> $$
> \sigma_{(g, \lambda)} = \sigma_{(I, \lambda)} \circ \sigma_{(g, 0)} \in TG_0.
> $$

^pf-58-9

*Uses:* [[§58 Semidirect Products#^prop-58-8|§58.8]], [[§41 The First and Second Isomorphism Theorems#^thm-41-1|§41.1]]

By (2), the conjugation action of $G_0$ on $T$ (Proposition [[§58 Semidirect Products#^prop-58-3|§58.3]]) is $\sigma_{(I, \mu)} \mapsto \sigma_{(I, g\mu)}$, which is the action $\varphi$ of Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]] under $\lambda \mapsto \sigma_{(I, \lambda)}$. So the internal description (3) and the external one agree, as Internal and External Semidirect Products Agree (Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]]) predicts.

> [!example] Example §58.5: The Affine Group
> *(Not from class.)* Take $L = V$ and $G = GL(V)$; every invertible linear map maps $V$ onto $V$. Then $\Gamma$ is the group $\operatorname{Aff}(V)$ of all maps $x \mapsto gx + \lambda$ with $g \in GL(V)$ and $\lambda \in V$, and Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]] gives
>
> $$
> \operatorname{Aff}(V) \cong V \rtimes GL(V).
> $$
>
> For $V = k$ these are the maps $x \mapsto ax + b$ with $a \in k^\times$ and $b \in k$, so $\operatorname{Aff}(k) \cong k \rtimes k^\times$, with $k^\times$ acting on the additive group $k$ by multiplication. For $k = \mathbb{F}_p$ this group has $p(p-1)$ elements. For $p = 3$ it has $6$ elements and permutes the three elements of $\mathbb{F}_3$. Only the identity map fixes all three: $ax + b = x$ at $x = 0$ gives $b = 0$, and then at $x = 1$ gives $a = 1$. So the permutation homomorphism $\operatorname{Aff}(\mathbb{F}_3) \to S_{\mathbb{F}_3} \cong S_3$ is injective between groups of order $6$, hence an isomorphism:
>
> $$
> S_3 \cong \mathbb{F}_3 \rtimes \mathbb{F}_3^\times = \mathbb{Z}/3\mathbb{Z} \rtimes \{\pm 1\},
> $$
>
> with $-1$ acting by $x \mapsto -x$, as in Example [[§58 Semidirect Products#^ex-58-4|§58.4]].

^ex-58-5

> [!example] Example §58.6: The Symmetries of $\mathbb{Z}$ in $\mathbb{R}$
> *(Not from class.)* Take $V = \mathbb{R}$, $G = \{\pm 1\} \subseteq GL_1(\mathbb{R})$ and $L = \mathbb{Z}$, so that $\pm\mathbb{Z} = \mathbb{Z}$. Then $\Gamma$ consists of the translations $x \mapsto x + n$ and the maps $x \mapsto -x + n$, $n \in \mathbb{Z}$. The map $x \mapsto -x + n$ is the reflection of $\mathbb{R}$ in the point $n/2$, since it fixes $n/2$ and sends $n/2 + t$ to $n/2 - t$. By Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]], $\Gamma \cong \mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$, with the generator of $\mathbb{Z}/2\mathbb{Z}$ acting by $n \mapsto -n$. This group is not abelian. By Proposition [[§58 Semidirect Products#^prop-58-9|§58.9]](2), conjugating the translation $t(x) = x + 1$ by the reflection $s(x) = -x$ gives $sts^{-1} = t^{-1}$, the translation by $-1$. These are the symmetries of the integer points of the line, the infinite analogue of the symmetries of a regular polygon.

^ex-58-6

> [!example] Example §58.7: A Wallpaper Group with Rotations by $120^\circ$
> *(Not from class; the problem set illustrates the case with a tiling by lizards.)* Let $V = \mathbb{R}^2$, let $r$ be the rotation by $120^\circ$ about $0$, $G = \{I, r, r^2\} \cong \mathbb{Z}/3\mathbb{Z}$, and let
>
> $$
> L = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2, \qquad \omega_1 = (1, 0), \quad \omega_2 = \big(\tfrac12, \tfrac{\sqrt3}{2}\big),
> $$
>
> the triangular lattice. Then $r\omega_1 = (-\frac12, \frac{\sqrt3}{2}) = \omega_2 - \omega_1$ and $r\omega_2 = (-1, 0) = -\omega_1$, so $rL \subseteq L$. Hence also $r^2L \subseteq rL \subseteq L$, and $L = r^3L = r(r^2L) \subseteq rL$; so $gL = L$ for every $g \in G$. By Proposition [[§58 Semidirect Products#^prop-58-8|§58.8]], $\Gamma \cong L \rtimes G \cong \mathbb{Z}^2 \rtimes \mathbb{Z}/3\mathbb{Z}$. It is the symmetry group of a pattern that has rotations by $120^\circ$ but no reflections, such as the figure below. In the classification of the seventeen wallpaper groups it is called $p3$.
>
> $\Gamma$ contains rotations about other points than $0$. Let $\lambda \in L$. Since $r$ has no nonzero fixed vector, $I - r$ is invertible, and with $c = (I - r)^{-1}\lambda$,
>
> $$
> \sigma_{(r, \lambda)}(x) - c = rx + (I - r)c - c = r(x - c).
> $$
>
> So $\sigma_{(r, \lambda)}$ is the rotation by $120^\circ$ about $c$. These centres are the $x = a\omega_1 + b\omega_2$ ($a, b \in \mathbb{R}$) with $(I - r)x \in L$. Since $(I - r)\omega_1 = 2\omega_1 - \omega_2$ and $(I - r)\omega_2 = \omega_1 + \omega_2$,
>
> $$
> (I - r)x = (2a + b)\,\omega_1 + (b - a)\,\omega_2,
> $$
>
> which lies in $L$ if and only if $2a + b$ and $b - a$ are integers. Then $3a = (2a + b) - (b - a) \in \mathbb{Z}$ and $b \in a + \mathbb{Z}$. So the centres of rotation are the points of
>
> $$
> L, \qquad c_1 + L, \qquad 2c_1 + L, \qquad c_1 = \tfrac13(\omega_1 + \omega_2):
> $$
>
> the lattice points and the centres of the two kinds of triangles of the lattice, those pointing up and those pointing down.

^ex-58-7

![[m493-58-1.svg]]

*(Not from lecture; figure added.)* The wallpaper group $\Gamma = L \rtimes \mathbb{Z}/3\mathbb{Z}$ of Example [[§58 Semidirect Products#^ex-58-7|§58.7]]. The blue motifs are the images $\gamma(F)$ of one motif $F$ under all $\gamma \in \Gamma$: at each lattice point (black) three copies, turned by $0^\circ$, $120^\circ$ and $240^\circ$. The arrows $\omega_1$, $\omega_2$ from the chosen origin $0$ (circled) span the translations $T \cong L$. Every element $\sigma_{(r, \lambda)}$ of $\Gamma$ is a rotation by $120^\circ$, about the point $(I - r)^{-1}\lambda$. These centres come in the three classes $L$ (black), $c_1 + L$ (red) and $2c_1 + L$ (orange), and the pattern looks the same when turned by $120^\circ$ about any of them. There is no mirror symmetry, because the motif is not symmetric.

> [!theorem] Corollary §58.10: Semidirect Products of Solvable Groups Are Solvable
> Let $\varphi: S \to \operatorname{Aut}(N)$ be a homomorphism. Then $N \rtimes_\varphi S$ is solvable if and only if $N$ and $S$ are solvable.
>
> *Source: not from class*

^cor-58-10

> [!proof]+ Proof
> *(Not from class; filled in.)* By Internal and External Semidirect Products Agree (Theorem [[§58 Semidirect Products#^thm-58-6|§58.6]](2)), $N \rtimes_\varphi S$ is the internal semidirect product of its subgroups $\tilde N \cong N$ and $\tilde S \cong S$, with $\tilde N$ normal. By The Quotient by $N$ (Proposition [[§58 Semidirect Products#^prop-58-1|§58.1]]), $(N \rtimes_\varphi S)/\tilde N \cong \tilde S \cong S$. Being solvable is preserved by isomorphisms, since an isomorphism carries a chain with abelian quotients to one. So by Corollary [[§48 Solvable Groups#^cor-48-8|§48.8]], $N \rtimes_\varphi S$ is solvable if and only if $\tilde N \cong N$ and $S$ are solvable.

^pf-58-10

*Uses:* [[§58 Semidirect Products#^thm-58-6|§58.6]], [[§58 Semidirect Products#^prop-58-1|§58.1]], [[§48 Solvable Groups#^cor-48-8|§48.8]]

All the groups of affine maps above are solvable, since in each of them $L$ and $G$ are abelian: $\operatorname{Aff}(k) \cong k \rtimes k^\times$, $\mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$ and $\mathbb{Z}^2 \rtimes \mathbb{Z}/3\mathbb{Z}$.

> [!example] Example §58.8: Groups of Order $pq$ Are Solvable
> *(Not from class.)* Let $p < q$ be primes and $|G| = pq$. The number $n_q$ of Sylow $q$-subgroups divides $p$ and is $\equiv 1 \pmod q$ (The Number of Sylow Subgroups Divides $|G|$, Corollary [[§55 The Sylow Theorems#^cor-55-10|§55.10]]). Since $p < q$, the only divisor of $p$ that is $\equiv 1 \pmod q$ is $1$, so $n_q = 1$. The Sylow $q$-subgroup $Q$, which exists by the First Sylow Theorem (Theorem [[§55 The Sylow Theorems#^thm-55-4|§55.4]]), is therefore normal (A Normal Sylow Subgroup Is the Only One, Corollary [[§55 The Sylow Theorems#^cor-55-7|§55.7]](2)). $Q$ has prime order $q$ and $G/Q$ has prime order $p$. A group of prime order is cyclic, generated by any non-identity element by Lagrange's theorem, hence abelian and solvable. By Corollary [[§48 Solvable Groups#^cor-48-8|§48.8]], $G$ is solvable. This covers the case $q \equiv 1 \pmod p$ as well, where $G$ need not be cyclic (Example [[§55 The Sylow Theorems#^ex-55-4|§55.4]]).

^ex-58-8