---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 56
tags: [group-theory, math493]
---
← [[§55 Internal and External Direct Products]] · ↑ [[· 10 Semidirect Products]]

*Reference: not covered in the Pinter chapters used so far.*

> [!definition] Definition §56.1: Internal Semidirect Product
> Let $G$ be a group, $N \trianglelefteq G$ a normal subgroup, and $S \leq G$ a subgroup (not necessarily normal), with $N \cap S = \{e\}$ and $G = NS$. Then $G$ is the **(internal) semidirect product** of $N$ and $S$.
>
> *Source: lecture 10/26; WS 11*

^def-56-1

> [!example] Example §56.1: $S_3$ and $S_n$
> $G = S_3$, $N = A_3 = \langle (1\,2\,3) \rangle$ (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-3|§21.3]]) and $S = \langle (1\,2) \rangle$. Here $A_3 \trianglelefteq S_3$, having index $2$ (Proposition [[§39 Sources of Normal Subgroups#^prop-39-1|§39.1]]); $A_3 \cap S = \{e\}$, since $(1\,2)$ is odd (Definition [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|§21.2]]); and $A_3S = S_3$, since $A_3S$ is a subgroup (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]) containing subgroups of orders $3$ and $2$, so its order is divisible by $6$ (Lagrange). So $S_3$ is the semidirect product of $A_3$ and $\langle (1\,2) \rangle$. It is not a direct product: $S$ is not normal, as $(1\,3)(1\,2)(1\,3) = (2\,3) \notin S$. The same argument shows that $S_n$ ($n \geq 2$) is the semidirect product of $A_n$ and $\langle (1\,2) \rangle$ (not from class).
>
> *Source: lecture 10/26*

^ex-56-1

> [!remark] Remark: Why More Data Is Needed
> For a direct product, $N_1$ and $N_2$ alone determine $G$. For a semidirect product, $N$ and $S$ do not: one also needs to know how $S$ acts on $N$. For example, $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$ and $S_3$ are both semidirect products of a normal subgroup of order $3$ and a subgroup of order $2$.
>
> *Source: lecture 10/26*

^rem-56-1

> [!theorem] Proposition §56.1: The Quotient by $N$
> In an internal semidirect product, $G/N \cong S$.
>
> *Source: WS 11.2*

^prop-56-1

> [!proof]+ Proof
> *Idea:* this is the Second Isomorphism Theorem.
>
> By the Second Isomorphism Theorem (Theorem [[§41 The First and Second Isomorphism Theorems#^thm-41-5|§41.5]]), $G/N = SN/N \cong S/(S \cap N) = S/\{e\} \cong S$ (here $SN = NS$, as $N$ is normal). Explicitly, $s \mapsto sN$ is an isomorphism $S \to G/N$.

^pf-56-1

*Uses:* [[§41 The First and Second Isomorphism Theorems#^thm-41-5|§41.5]]

> [!theorem] Proposition §56.2: Unique Factorization $g = ns$
> In an internal semidirect product, every $g \in G$ can be written in exactly one way as $g = ns$ with $n \in N$ and $s \in S$.
>
> *Source: WS 11.3*

^prop-56-2

> [!proof]+ Proof
> *Idea:* two factorizations differ by an element of $N \cap S = \{e\}$.
>
> *(Done on the boards 10/26; written out here.)* Existence is $G = NS$. If $ns = n's'$ with $n, n' \in N$ and $s, s' \in S$, then $n'^{-1}n = s's^{-1}$; the left side lies in $N$ and the right side in $S$, so both lie in $N \cap S = \{e\}$. Hence $n = n'$ and $s = s'$.

^pf-56-2

> [!theorem] Proposition §56.3: $S$ Acts on $N$ by Automorphisms
> In an internal semidirect product, for $s \in S$ let $\varphi(s): N \to N$, $n \mapsto sns^{-1}$. Then:
>
> 1. $\varphi(s)$ is an automorphism of $N$, an isomorphism $N \to N$ (Definition [[§18 Conjugation, Products, and Pointwise Products#^def-18-1|§18.1]]);
> 2. $\varphi: S \to \operatorname{Aut}(N)$ is a group homomorphism: $\varphi(ss') = \varphi(s) \circ \varphi(s')$.
>
> Equivalently, $s \star n = sns^{-1}$ is an action of $S$ on $N$ by automorphisms.
>
> *Source: WS 11.4; lecture 10/26*

^prop-56-3

> [!proof]+ Proof
> *Idea:* $\varphi(s)$ is conjugation by $s$, restricted to the normal subgroup $N$.
>
> *(Done on the boards 10/26; written out here.)* **(1)** $\varphi(s)$ maps $N$ into $N$ because $N$ is normal. It is the restriction to $N$ of conjugation $c_s: G \to G$, which is a homomorphism (Conjugation Is an Automorphism, Proposition [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]], PS 1.2), so $\varphi(s)$ is a homomorphism $N \to N$. It has inverse $\varphi(s^{-1})$: $s^{-1}(sns^{-1})s = n$ and $s(s^{-1}ns)s^{-1} = n$, with $s^{-1}ns \in N$ again by normality. So $\varphi(s)$ is a bijective homomorphism $N \to N$.
>
> **(2)** For $n \in N$, $\varphi(ss')(n) = ss'\,n\,(ss')^{-1} = s\,(s'ns'^{-1})\,s^{-1} = \varphi(s)\big(\varphi(s')(n)\big)$.

^pf-56-3

*Uses:* [[§18 Conjugation, Products, and Pointwise Products#^prop-18-1|§18.1]]

> [!theorem] Proposition §56.4: Multiplication in the Form $ns$
> In an internal semidirect product, for $n_1, n_2 \in N$ and $s_1, s_2 \in S$,
>
> $$
> (n_1s_1)(n_2s_2) = \big(n_1\,\varphi(s_1)(n_2)\big)\,(s_1s_2),
> $$
>
> with $n_1\varphi(s_1)(n_2) \in N$ and $s_1s_2 \in S$.
>
> *Source: WS 11.5*

^prop-56-4

> [!proof]+ Proof
> *Idea:* move $s_1$ past $n_2$ at the cost of conjugating $n_2$.
>
> *(Done on the boards 10/26; written out here.)* Insert $s_1^{-1}s_1 = e$ between $n_2$ and $s_2$:
>
> $$
> n_1s_1n_2s_2 = n_1\,(s_1n_2s_1^{-1})\,s_1s_2 = n_1\,\varphi(s_1)(n_2)\,s_1s_2,
> $$
>
> and $\varphi(s_1)(n_2) \in N$ by Proposition [[§56 Semidirect Products#^prop-56-3|§56.3]](1).

^pf-56-4

*Uses:* [[§56 Semidirect Products#^prop-56-3|§56.3]]

> [!remark] Remark: The Data $(N, S, \varphi)$
> By Propositions [[§56 Semidirect Products#^prop-56-2|§56.2]] and [[§56 Semidirect Products#^prop-56-4|§56.4]] (WS 11.3 and 11.5), the multiplication of $G$ is determined by $N$, $S$, and the homomorphism $\varphi: S \to \operatorname{Aut}(N)$ given by conjugation. This suggests building a group from the triple $(N, S, \varphi)$ alone, with no ambient group $G$, where $N$ and $S$ are now any two groups and $\varphi$ is any homomorphism $S \to \operatorname{Aut}(N)$.
>
> *Source: lecture 10/26*

^rem-56-2

> [!definition] Definition §56.2: External Semidirect Product
> Let $N$ and $S$ be groups and $\varphi: S \to \operatorname{Aut}(N)$ a group homomorphism. The **external semidirect product** of $N$ and $S$ by $\varphi$ is the set $\{(n, s) : n \in N,\ s \in S\}$ with multiplication
>
> $$
> (n_1, s_1) \cdot (n_2, s_2) = \big(n_1\,\varphi(s_1)(n_2),\ s_1s_2\big).
> $$
>
> It is written $N \rtimes_\varphi S$, or $N \rtimes S$ when $\varphi$ is clear. Some authors put the normal subgroup second and write $S \ltimes_\varphi N$; this course writes $N \rtimes_\varphi S$.
>
> *Source: WS 11; lecture 10/26*

^def-56-2

> [!theorem] Theorem §56.5: $N \rtimes_\varphi S$ Is a Group
> $N \rtimes_\varphi S$ is a group, with identity $(e_N, e_S)$ and inverse
>
> $$
> (n, s)^{-1} = \big(\varphi(s^{-1})(n^{-1}),\ s^{-1}\big).
> $$
>
> *Source: WS 11.6*

^thm-56-5

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

^pf-56-5

> [!theorem] Theorem §56.6: Internal and External Semidirect Products Agree
> 1. If $G$ is the internal semidirect product of $N$ and $S$, and $\varphi: S \to \operatorname{Aut}(N)$ is conjugation (Proposition [[§56 Semidirect Products#^prop-56-3|§56.3]]), then $(n, s) \mapsto ns$ is an isomorphism $N \rtimes_\varphi S \to G$.
> 2. Conversely, in $N \rtimes_\varphi S$ the subsets $\tilde N = \{(n, e) : n \in N\}$ and $\tilde S = \{(e, s) : s \in S\}$ are subgroups isomorphic to $N$ and $S$, $\tilde N$ is normal, $N \rtimes_\varphi S$ is the internal semidirect product of $\tilde N$ and $\tilde S$, and conjugation by $\tilde S$ on $\tilde N$ recovers $\varphi$:
>
> $$
> (e, s)(n, e)(e, s)^{-1} = \big(\varphi(s)(n), e\big).
> $$
>
> *Source: WS 11; lecture 10/26*

^thm-56-6

> [!proof]+ Proof
> *Idea:* (1) is WS 11.3 and 11.5 read as a statement about the map $(n, s) \mapsto ns$; (2) computes inside $N \rtimes_\varphi S$ with the multiplication rule.
>
> **(1)** The map is a homomorphism by Multiplication in the Form $ns$ (Proposition [[§56 Semidirect Products#^prop-56-4|§56.4]]), which says exactly that $(n_1, s_1)(n_2, s_2) \mapsto (n_1s_1)(n_2s_2)$, and a bijection by Unique Factorization (Proposition [[§56 Semidirect Products#^prop-56-2|§56.2]]).
>
> **(2)** *(The displayed formula is from the board 10/26.)* By the multiplication rule, $(n, e)(n', e) = (n\,\varphi_e(n'), e) = (nn', e)$ and $(e, s)(e, s') = (\varphi_s(e), ss') = (e, ss')$, so $n \mapsto (n, e)$ and $s \mapsto (e, s)$ are injective homomorphisms, with images $\tilde N$ and $\tilde S$. The map $(n, s) \mapsto s$ is a homomorphism $N \rtimes_\varphi S \to S$ (the second coordinate of a product is $s_1s_2$) with kernel $\tilde N$, so $\tilde N$ is normal (Kernels Are Normal, Proposition [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]]). $\tilde N \cap \tilde S = \{(e, e)\}$, and $(n, e)(e, s) = (n\,\varphi_e(e), s) = (n, s)$, so $\tilde N\tilde S$ is everything. Finally, using $(e, s)^{-1} = (e, s^{-1})$ (Theorem [[§56 Semidirect Products#^thm-56-5|§56.5]]),
>
> $$
> (e, s)(n, e)(e, s^{-1}) = \big(\varphi_s(n), s\big)(e, s^{-1}) = \big(\varphi_s(n)\,\varphi_s(e), e\big) = \big(\varphi_s(n), e\big).
> $$

^pf-56-6

*Uses:* [[§56 Semidirect Products#^prop-56-4|§56.4]], [[§56 Semidirect Products#^prop-56-2|§56.2]], [[§39 Sources of Normal Subgroups#^prop-39-2|§39.2]], [[§56 Semidirect Products#^thm-56-5|§56.5]]

> [!remark] Remark: Direct Products as a Special Case
> *(Not from class.)* If $\varphi$ is trivial ($\varphi(s) = \mathrm{id}_N$ for all $s$), the rule becomes $(n_1, s_1)(n_2, s_2) = (n_1n_2, s_1s_2)$, and $N \rtimes_\varphi S = N \times S$. In the internal picture, $\varphi$ is trivial exactly when every element of $S$ commutes with every element of $N$. Given $G = NS$, this happens exactly when $S$ is also normal: if $S$ commutes with $N$, then $nsSs^{-1}n^{-1} = nSn^{-1} = S$; conversely, if $S$ is normal, Normal Subgroups with Trivial Intersection Commute (Proposition [[§47 Commutators#^prop-47-8|§47.8]]) applies. This recovers Theorem [[§55 Internal and External Direct Products#^thm-55-1|§55.1]] (WS 11.1).

^rem-56-3

> [!example] Example §56.2: $\mathbb{Z}/7\mathbb{Z} \rtimes \mathbb{Z}/3\mathbb{Z}$
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
> No group of order $21$ had to be found first: the triple $(N, S, \varphi)$ is enough. The group is not abelian: $(1, 0)(0, 1) = (1, 1)$ but $(0, 1)(1, 0) = (2, 1)$. (Not from class, checked by computer: its center is trivial, and it has $14$ elements of order $3$, so $n_3 = 7$, the second candidate in Example [[§54 Simple Groups of Small Order#^ex-54-1|§54.1]], while $n_7 = 1$ as it must be.)
>
> *Source: lecture 10/26*

^ex-56-2

![[m493-55-1.svg]]

*(Not from lecture; figure added.)* The action in Example [[§56 Semidirect Products#^ex-56-2|§56.2]]: the generator $1 \in \mathbb{Z}/3\mathbb{Z}$ permutes $\mathbb{Z}/7\mathbb{Z}$ by $x \mapsto 2x$, fixing $0$ and cycling the other six elements in two $3$-cycles. Because $2^3 \equiv 1 \pmod 7$, applying it three times is the identity, which is what makes $k \mapsto (x \mapsto 2^kx)$ a homomorphism $\mathbb{Z}/3\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/7\mathbb{Z})$.

![[m493-55-2.svg]]

*(Not from lecture; figure added.)* The $21$ elements $(n, s)$ of $\mathbb{Z}/7\mathbb{Z} \rtimes \mathbb{Z}/3\mathbb{Z}$. The bottom row is the normal subgroup $\tilde N$, and the rows are its cosets, one for each $s$: this is $G/\tilde N \cong \mathbb{Z}/3\mathbb{Z}$ (Proposition [[§56 Semidirect Products#^prop-56-1|§56.1]]). The column $n = 0$ is $\tilde S$, which is not normal. The arrows are left multiplication by $(0, 1)$ on the bottom row, $(0, 1)(n, 0) = (2n, 1)$: moving up a row applies the action.

> [!example] Example §56.3: $S_3$ as an External Semidirect Product
> *(Not from class.)* Let $\varphi: \mathbb{Z}/2\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/3\mathbb{Z})$ send $1$ to $x \mapsto -x$. Then $\mathbb{Z}/3\mathbb{Z} \rtimes_\varphi \mathbb{Z}/2\mathbb{Z} \cong S_3$: in $S_3 = A_3 \rtimes \langle (1\,2) \rangle$ (Example [[§56 Semidirect Products#^ex-56-1|§56.1]]), conjugation by $(1\,2)$ sends $(1\,2\,3)$ to $(2\,1\,3) = (1\,3\,2) = (1\,2\,3)^{-1}$, which under $A_3 \cong \mathbb{Z}/3\mathbb{Z}$, $(1\,2\,3)^x \leftrightarrow x$, is $x \mapsto -x$. Apply part (1) of Theorem [[§56 Semidirect Products#^thm-56-6|§56.6]]. With $\varphi$ trivial instead, one gets $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z}$.

^ex-56-3

> [!remark] Remark: Notation and Mnemonics
> Conventions differ on the order: $N \rtimes S$ and $S \ltimes N$ mean the same group, with $N$ normal and $S$ acting. Two mnemonics from the lecture: the triangle in $\rtimes$ or $\ltimes$ is like the symbol $\trianglelefteq$ and points toward the normal subgroup; and the vertical stroke stands on the side of $S$, the group that acts on $N$. Note that $N$ is not assumed to be normal in anything at the start; the input is just two groups and an action, and $N$ becomes normal in $N \rtimes_\varphi S$ (Theorem [[§56 Semidirect Products#^thm-56-6|§56.6]](2)).
>
> *Source: lecture 10/26*

^rem-56-4
