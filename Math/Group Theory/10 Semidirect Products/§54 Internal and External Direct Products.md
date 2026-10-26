---
type: section
subject: "[[Group Theory]]"
chapter: 10
section: 54
tags: [group-theory, math493]
---
← [[§53 Simple Groups of Small Order]] · ↑ [[· 10 Semidirect Products]] · [[§55 Semidirect Products]] →

*Reference: Pinter Ch. 4, Ex. G (direct products).*

> [!remark] Remark: Two Meanings of “Direct Sum”
> Let $V$ be a vector space and $L_1, L_2$ subspaces with $V = L_1 + L_2$ and $L_1 \cap L_2 = \{0\}$; for instance, a plane and a line through the origin in $\mathbb{R}^3$, the line not lying in the plane. Then every $v \in V$ can be written uniquely as $v = v_1 + v_2$ with $v_1 \in L_1$, $v_2 \in L_2$, and one writes $V = L_1 \oplus L_2$. Mathematicians use “direct sum” in two ways:
> - the **external direct sum** $L_1 \oplus L_2 = \{(v_1, v_2) : v_1 \in L_1,\ v_2 \in L_2\}$, with $(v_1, v_2) + (v_1', v_2') = (v_1 + v_1', v_2 + v_2')$ and $c(v_1, v_2) = (cv_1, cv_2)$, built from $L_1$ and $L_2$ with no ambient space;
> - the **internal direct sum**: $V$ is given in advance, and $L_1, L_2$ already sit inside it as above.
>
> Strictly, the elements of the external direct sum are ordered pairs and the elements of $V$ are not, so in the internal situation one should write $V \cong L_1 \oplus L_2$. The same distinction appears for groups, and it causes the most confusion for semidirect products. The lecture is careful about it for now, but warned that most people are not, and that the course will soon stop being so careful. (The lecturer compared it to embedded versus abstract manifolds.)
>
> *Source: lecture 10/26*

^rem-54-1

![[m493-54-1.svg]]

*(Not from lecture; figure added, after the board sketch.)* An internal direct sum in $\mathbb{R}^3$: a plane $L_1$ and a line $L_2$ meeting only at $0$. Every $v$ splits uniquely as $v = v_1 + v_2$ with $v_1 \in L_1$, $v_2 \in L_2$, so $v \mapsto (v_1, v_2)$ identifies $\mathbb{R}^3$ with the external direct sum $L_1 \oplus L_2$.

> [!definition] Definition §54.1: Internal Direct Product
> Let $G$ be a group and $N_1, N_2$ normal subgroups of $G$ with $N_1 \cap N_2 = \{e\}$ and $G = N_1N_2$. Then $G$ is the **internal direct product** of $N_1$ and $N_2$. By contrast, the **external direct product** $N_1 \times N_2$ is the group of pairs with componentwise multiplication (Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]); it is built from $N_1$ and $N_2$ without any ambient group.
>
> *Source: lecture 10/26; WS 11*

^def-54-1

> [!theorem] Theorem §54.1: Internal Direct Products Are Direct Products
> Let $N_1, N_2 \trianglelefteq G$ with $N_1 \cap N_2 = \{e\}$ and $G = N_1N_2$. Then $n_1n_2 = n_2n_1$ for all $n_1 \in N_1$, $n_2 \in N_2$, and
>
> $$
> \mu: N_1 \times N_2 \to G, \qquad (n_1, n_2) \mapsto n_1n_2
> $$
>
> is an isomorphism. In particular $G \cong N_1 \times N_2$.
>
> *Source: WS 11.1; PS 4.2; lecture 10/26*

^thm-54-1

> [!proof]+ Proof
> *Idea:* the two factors commute, so multiplying out is a homomorphism; trivial intersection makes it injective, and $G = N_1N_2$ makes it onto.
>
> *(Done on the boards 10/26; written out here.)* The elements commute by Normal Subgroups with Trivial Intersection Commute (Proposition [[§47 Commutators#^prop-47-8|§47.8]], PS 4.2).
>
> *Homomorphism.* Using $n_2 n_1' = n_1' n_2$ and the componentwise product of $N_1 \times N_2$ (Definition [[§3 Basic Examples of Groups#^def-3-2|§3.2]]),
>
> $$
> \mu\big((n_1, n_2)(n_1', n_2')\big) = n_1n_1'\,n_2n_2' = n_1\,(n_1'n_2)\,n_2' = n_1\,(n_2n_1')\,n_2' = \mu(n_1, n_2)\,\mu(n_1', n_2').
> $$
>
> *Injective.* If $n_1n_2 = e$, then $n_1 = n_2^{-1} \in N_1 \cap N_2 = \{e\}$, so $(n_1, n_2) = (e, e)$: the kernel is trivial, and $\mu$ is injective (Proposition [[§15 Homomorphisms#^prop-15-3|§15.3]]).
>
> *Surjective.* Every element of $G = N_1N_2$ has the form $n_1n_2$.

^pf-54-1

*Uses:* [[§47 Commutators#^prop-47-8|§47.8]], [[§3 Basic Examples of Groups#^def-3-2|Def. §3.2]], [[§15 Homomorphisms#^prop-15-3|§15.3]]

> [!remark] Remark: Two Forms of the Criterion
> *(Not from class.)* Internal Direct Products (Lemma [[§51 p-Groups and Sylow Subgroups#^lem-51-6|§51.6]], from PS 6.3(5)) is the finite version: commuting subgroups $H, L$ with $H \cap L = \{e\}$ and $|H|\,|L| = |G|$. For finite $G$ and normal $N_1, N_2$ with $N_1 \cap N_2 = \{e\}$, the conditions $G = N_1N_2$ and $|N_1|\,|N_2| = |G|$ are equivalent, because $|N_1N_2| = |N_1|\,|N_2|$ (The Order of a Product of Subgroups, Lemma [[§52 The Sylow Theorems#^lem-52-8|§52.8]]). The theorem above needs no finiteness.

^rem-54-2

> [!example] Example §54.1: $\mathbb{Z}/15\mathbb{Z}$
> In $\mathbb{Z}/15\mathbb{Z}$ (written additively), $N_1 = 3\mathbb{Z}/15\mathbb{Z}$ has $5$ elements and $N_2 = 5\mathbb{Z}/15\mathbb{Z}$ has $3$ elements. Both are normal, as the group is abelian. $N_1 \cap N_2$ is a subgroup of both, so its order divides $\gcd(5, 3) = 1$ (Lagrange, Theorem [[§29 The Index and Lagrange's Theorem#^thm-29-2|§29.2]]). And $N_1 + N_2$ is a subgroup containing $N_1$ and $N_2$ (Lemma [[§41 The First and Second Isomorphism Theorems#^lem-41-3|§41.3]]), so its order is divisible by $5$ and $3$, hence is $15$. So $\mathbb{Z}/15\mathbb{Z}$ is the internal direct product of $3\mathbb{Z}/15\mathbb{Z} \cong \mathbb{Z}/5\mathbb{Z}$ and $5\mathbb{Z}/15\mathbb{Z} \cong \mathbb{Z}/3\mathbb{Z}$, and $\mathbb{Z}/15\mathbb{Z} \cong \mathbb{Z}/5\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ (Theorem [[§54 Internal and External Direct Products#^thm-54-1|§54.1]]).
>
> *Source: WS 11*

^ex-54-1
