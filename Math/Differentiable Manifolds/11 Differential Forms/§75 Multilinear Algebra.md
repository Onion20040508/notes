---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 75
tags: [differentiable-manifolds, math591]
---
← [[§74 The Integrand Is a Two-Form]] · ↑ [[· 11 Differential Forms]]

*Stage: forms — Alternating multilinear forms on a vector space: the pointwise objects that differential forms are made of.*

*(Lecture 28.)* Forms are needed in every degree, not just two: this takes some multilinear algebra. Uribe thinks of these objects as minors of large determinants.

> [!definition] Definition §75.1: Linear $k$-Form
> Let $V$ be an $m$-dimensional real vector space and $k \in \{0, 1, 2, \ldots\}$. A **linear $k$-form** on $V$ is a multilinear map
>
> $$
> \alpha : \underbrace{V \times \cdots \times V}_{k} \longrightarrow \mathbb{R}
> $$
>
> (linear in each entry with the others fixed) that is **alternating**: exchanging two entries changes the sign,
>
> $$
> \alpha(v^1, \ldots, v^i, \ldots, v^j, \ldots, v^k) = -\alpha(v^1, \ldots, v^j, \ldots, v^i, \ldots, v^k) \qquad (i \neq j) .
> $$
>
> *Lee: Ch. 12, Symmetric and Alternating Tensors; Ch. 14, The Algebra of Alternating Tensors*

^def-75-1

> [!remark]- Connections
> - Axler's alternating forms, written $V^{(m)}_{\mathrm{alt}}$ for $m$ entries: [[§36 Alternating Multilinear Forms#^ladr-9-27|LADR 9.27]]; sign under swapping: [[§36 Alternating Multilinear Forms#^ladr-9-30|LADR 9.30]].

The definition copies the determinant, which changes sign when two columns are exchanged. For $k = 1$ the alternating condition is empty and the linear $1$-forms are the covectors, $V^{\ast}$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]); for $k = 0$ the linear $0$-forms are, by convention, the scalars. On a manifold there will be one of these at each point, with $V$ the tangent space.

> [!example] Example §75.1: Linear $k$-Forms
> 1. On $\mathbb{R}^3$, each $dx^i \wedge dx^j$ (Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]]) is a linear $2$-form, by Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](1).
> 2. On $\mathbb{R}^m$, the determinant $\alpha(v^1, \ldots, v^m) = \det(v^1 \cdots v^m)$ of the matrix with columns $v^1, \ldots, v^m$ is a linear $m$-form: it is linear in each column, and exchanging two columns changes its sign. For $m = 2$, $\det(v, w)$ is the signed area of the parallelogram spanned by $v$ and $w$ (figure below).
> 3. On $\mathbb{R}^m$, fix rows $1 \le i_1, \ldots, i_k \le m$. Let $\alpha(v^1, \ldots, v^k)$ be the $k \times k$ minor in the rows $i_1, \ldots, i_k$ of the $m \times k$ matrix with columns $v^1, \ldots, v^k$. Then $\alpha$ is a linear $k$-form, by the same two properties of the $k \times k$ determinant. This generalizes item 1, where $m = 3$, $k = 2$ and the rows are $i, j$.

^ex-75-1

> [!proof]+ Proof
> *(Not from lecture; filled in.)* (2) Multilinearity: expanding along the $j$-th column, $\det$ is a linear function of $v^j$ with the other columns fixed. Exchanging two columns changes the sign of a determinant. (3) The minor is the determinant of the $k \times k$ matrix whose $a$-th column is $(v^a_{i_1}, \ldots, v^a_{i_k})$; this column depends linearly on $v^a$, and exchanging $v^a$ and $v^{a'}$ exchanges two columns. So (2) applies. (1) is (3) with $m = 3$, $k = 2$, $(i_1, i_2) = (i, j)$, written with rows and columns exchanged, which does not change a determinant.

^pf-ex-75-1

> [!theorem] Lemma §75.1: Permuting the Entries of a $k$-Form
> Let $\alpha$ be a linear $k$-form on $V$ (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]) and $v^1, \ldots, v^k \in V$. For every permutation $\sigma \in S_k$,
>
> $$
> \alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big) = \operatorname{sgn}(\sigma)\, \alpha(v^1, \ldots, v^k) ,
> $$
>
> with $\operatorname{sgn}$ the sign of a permutation (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]). Conversely, a multilinear map $V \times \cdots \times V \to \mathbb{R}$ with this property for every $\sigma \in S_k$ is alternating.
>
> *Lee: Exercise 12.17*

^lem-75-1

> [!remark]- Connections
> - Axler's version: [[§36 Alternating Multilinear Forms#^ladr-9-35|LADR 9.35]].
> - The sign of a permutation and why it is well defined: [[§21 The Sign Homomorphism and the Alternating Group#^def-21-2|493 Def. §21.2]], [[§21 The Sign Homomorphism and the Alternating Group#^thm-21-3|493 Thm. §21.3]].

> [!proof]+ Proof
> *(Discussed with Uribe after Lecture 28; the proof is written out here.)* For $\rho \in S_k$ write $\alpha_\rho = \alpha\big(v^{\rho(1)}, \ldots, v^{\rho(k)}\big)$, the value on the list rearranged by $\rho$; products of permutations are composites, $(\rho\tau)(i) = \rho(\tau(i))$.
>
> *Step 1: one more transposition changes the sign.* Let $\rho \in S_k$ and let $\tau = (a\ b)$ be a transposition, $a \neq b$. Put $u^i = v^{\rho(i)}$, so that $\alpha_\rho = \alpha(u^1, \ldots, u^k)$. Then $v^{(\rho\tau)(i)} = u^{\tau(i)}$, and since $\tau(a) = b$, $\tau(b) = a$ and $\tau(i) = i$ otherwise, the list $\big(u^{\tau(1)}, \ldots, u^{\tau(k)}\big)$ is the list $(u^1, \ldots, u^k)$ with the entries in places $a$ and $b$ exchanged. By the alternating property (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]),
>
> $$
> \alpha_{\rho\tau} = \alpha\big(u^{\tau(1)}, \ldots, u^{\tau(k)}\big) = -\alpha(u^1, \ldots, u^k) = -\alpha_\rho .
> $$
>
> *Step 2: induction along a factorization.* By Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](3), $\sigma = \tau_1 \tau_2 \cdots \tau_r$ for some transpositions $\tau_1, \ldots, \tau_r$, and $\operatorname{sgn}(\sigma) = (-1)^r$ (for $\sigma = \mathrm{id}$ take $r = 0$). Put $\rho_0 = \mathrm{id}$ and $\rho_j = \tau_1 \cdots \tau_j$, so $\rho_j = \rho_{j-1}\tau_j$ and $\rho_r = \sigma$. Step 1 with $\rho = \rho_{j-1}$ and $\tau = \tau_j$ gives $\alpha_{\rho_j} = -\alpha_{\rho_{j-1}}$ for $j = 1, \ldots, r$, hence
>
> $$
> \alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big) = \alpha_{\rho_r} = (-1)^r \alpha_{\rho_0} = \operatorname{sgn}(\sigma)\, \alpha(v^1, \ldots, v^k) .
> $$
>
> *The converse.* If the identity holds for every $\sigma$, take $\sigma = (i\ j)$ with $i \neq j$: its sign is $-1$ (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](2)), and the rearranged list is $(v^1, \ldots, v^k)$ with the entries $i$ and $j$ exchanged. So exchanging two entries changes the sign: the map is alternating.

^pf-75-1

*Uses:* [[§75 Multilinear Algebra#^def-75-1|Def. §75.1]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]]

For $k = 2$ the lemma is the definition. For the determinant (Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](2)) it says that permuting the columns multiplies the determinant by the sign of the permutation, the fact behind the Leibniz formula. The sign does not depend on how $\sigma$ is written as a product of transpositions (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](3)); without that, Step 2 would give two different values for one number. Lee uses the lemma to find a basis of $\Lambda^k(V^{\ast})$ (Lemma 14.7 and Proposition 14.8).

![[m591-75-2.svg]]

*(Not from lecture; figure added.)* Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]] for $k = 3$ and $\alpha = \det$ on $\mathbb{R}^3$, the signed volume. The same box, spanned by $v^1$ (blue), $v^2$ (orange) and $v^3$ (red), is read in three orders; the circled numbers give each vector's place in the order. Curl the fingers of the right hand from the first entry to the second (black arc): if the third entry lies on the side of the thumb the order is right-handed and the value is $+\mathrm{vol}$, otherwise $-\mathrm{vol}$. Left: $(v^1, v^2, v^3)$, right-handed. Middle: the cyclic order $(v^2, v^3, v^1)$ is a product of two transpositions, $\operatorname{sgn} = +1$, and is right-handed again. Right: exchanging $v^1$ and $v^2$, one transposition, $\operatorname{sgn} = -1$, gives the left-handed order and the value changes sign.

> [!theorem] Lemma §75.2: Alternating Forms Vanish on Dependent Vectors
> Let $\alpha$ be a linear $k$-form on $V$ (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]).
>
> 1. If two of the entries are equal, $v^i = v^j$ for some $i \neq j$, then $\alpha(v^1, \ldots, v^k) = 0$.
> 2. If $v^1, \ldots, v^k$ are linearly dependent, then $\alpha(v^1, \ldots, v^k) = 0$.
>
> *Lee: Lemma 14.1*

^lem-75-2

> [!remark]- Connections
> - [[§36 Alternating Multilinear Forms#^ladr-9-28|LADR 9.28]], with a figure and animation of a parallelepiped flattening as the vectors become dependent.

> [!proof]+ Proof
> *(Not from lecture; filled in, as in LADR, 9.28.)* (1) Exchanging the two equal entries does not change the list, but changes the sign of $\alpha$: $\alpha(v^1, \ldots, v^k) = -\alpha(v^1, \ldots, v^k)$, so the value is $0$.
>
> (2) Some $v^j$ is a linear combination of the others, $v^j = \sum_{i \neq j} c_i v^i$. By linearity of $\alpha$ in the $j$-th entry,
>
> $$
> \alpha(v^1, \ldots, v^j, \ldots, v^k) = \sum_{i \neq j} c_i\, \alpha(v^1, \ldots, \underbrace{v^i}_{j\text{-th entry}}, \ldots, v^k) ,
> $$
>
> and in the $i$-th term the vector $v^i$ appears twice, in the entries $i$ and $j$; by (1) every term is $0$.

^pf-75-2

> [!theorem] Corollary §75.3: No Nonzero $k$-Forms of Degree above the Dimension
> If $k > m = \dim V$, the only linear $k$-form on $V$ is $0$.

^cor-75-3

> [!remark]- Connections
> - [[§36 Alternating Multilinear Forms#^ladr-9-29|LADR 9.29]].

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Any $k > m$ vectors in the $m$-dimensional space $V$ are linearly dependent, so every value of a linear $k$-form is $0$ by Lemma [[§75 Multilinear Algebra#^lem-75-2|§75.2]](2).

^pf-75-3

*Uses:* [[§75 Multilinear Algebra#^lem-75-2|§75.2]]

![[m591-75-1.svg]]

*(Not from lecture; figure added.)* The $2$-form $\alpha = \det$ on $\mathbb{R}^2$ (Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](2)) as signed area. Left: $\alpha(v, w)$ is the area of the parallelogram spanned by $v$ and $w$, positive because $v$ turns to $w$ counterclockwise. Middle: exchanging the entries reverses the direction of turning and the sign, $\alpha(w, v) = -\alpha(v, w)$, the alternating condition of Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]. Right: for dependent vectors, here $w = 0.55\, v$, the parallelogram is flat and $\alpha(v, w) = 0$ (Lemma [[§75 Multilinear Algebra#^lem-75-2|§75.2]]).

> [!theorem] Proposition §75.4: The Space of $k$-Forms
> The set $\Lambda^k V$ of all linear $k$-forms on the $m$-dimensional space $V$ is a vector space, of dimension $\binom{m}{k}$.
>
> *Lee: Proposition 14.8*

^prop-75-4

> [!remark]- Connections
> - The top degree, $\dim \Lambda^m V = 1$: [[§36 Alternating Multilinear Forms#^ladr-9-37|LADR 9.37]].

> [!proof]+ Proof (to be filled)
> That linear combinations of alternating multilinear maps are again alternating and multilinear is immediate, so $\Lambda^k V$ is a subspace of the space of all functions $V^k \to \mathbb{R}$. The dimension, by writing down a basis, is for Lecture 29.

^pf-75-4

In particular $\Lambda^k V = 0$ for $k > m$ (this is Corollary [[§75 Multilinear Algebra#^cor-75-3|§75.3]], proved directly), and $\Lambda^m V$ is one-dimensional, spanned by the determinant in any basis. Lee writes $\Lambda^k(V^{\ast})$ for this space.

\appendix
