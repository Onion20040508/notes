---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 75
tags: [differentiable-manifolds, math591]
---
← [[§74 The Integrand Is a Two-Form]] · ↑ [[· 11 Differential Forms]] · [[§76 The Wedge Product]] →

*Stage: forms — Alternating multilinear forms on a vector space: the pointwise objects that differential forms are made of.*

*(Lecture 28.)* Forms are needed in every degree, not just two: this takes some multilinear algebra. A useful way to think of these objects is as minors of large determinants (Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](3)).

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

For $k = 2$ the lemma is the definition. For the determinant (Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](2)) it says that permuting the columns multiplies the determinant by the sign of the permutation, the fact behind the Leibniz formula. The sign does not depend on how $\sigma$ is written as a product of transpositions (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](3)); without that, Step 2 would give two different values for one number. Lee uses the lemma to find a basis of $\Lambda^k(V^{\ast})$ (Lemma 14.7 and Proposition 14.8); it is used in the same way in the proof of Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]].

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

*(Lecture 29.)* The linear algebra continues, with $V$ an $m$-dimensional real vector space (to be thought of as a tangent space, $V = T_pM$) and $k = 0, 1, 2, \ldots$. The lecture restated the definition of a $k$-form with all permutations at once: a multilinear map $\alpha : V \times \cdots \times V \to \mathbb{R}$ of $k$ entries is a $k$-form when, for every $\sigma \in S_k$ and all $v^1, \ldots, v^k \in V$,

$$
\alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big) = \operatorname{sgn}(\sigma)\, \alpha(v^1, \ldots, v^k) .
$$

By Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]] this is equivalent to Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]], which is the case of a transposition. Here $S_k$ is the group of permutations of $\{1, \ldots, k\}$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-3|§11.3]]) and $\operatorname{sgn}(\sigma)$ is the sign of $\sigma$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]): every permutation is a composition of transpositions; the decomposition is not unique, but the parity of the number of transpositions is, and $\operatorname{sgn}(\sigma)$ is $+1$ when that number is even and $-1$ when it is odd (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](3)).

> [!definition] Definition §75.2: The Space $\Lambda^k V^{\ast}$
> $\Lambda^k V^{\ast}$ is the set of all linear $k$-forms on $V$ (Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]]), with the pointwise operations
>
> $$
> (\alpha + \beta)(v^1, \ldots, v^k) = \alpha(v^1, \ldots, v^k) + \beta(v^1, \ldots, v^k), \qquad (c\, \alpha)(v^1, \ldots, v^k) = c\, \alpha(v^1, \ldots, v^k) .
> $$
>
> In particular $\Lambda^1 V^{\ast} = V^{\ast}$, the dual space of all linear maps $V \to \mathbb{R}$ (Definition [[§21 Linear Algebra Toolkit#^def-21-1|§21.1]]), and by convention $\Lambda^0 V^{\ast} = \mathbb{R}$.
>
> *Lee: Ch. 14, The Algebra of Alternating Tensors*

^def-75-2

Sums and scalar multiples of alternating multilinear maps are again alternating and multilinear, so $\Lambda^k V^{\ast}$ is a vector space, a subspace of the space of all functions $V^k \to \mathbb{R}$ *(Lecture 28)*. For $k = 1$ the group $S_1$ has one element and the alternating condition is empty, which is why $\Lambda^1 V^{\ast} = V^{\ast}$. The convention $\Lambda^0 V^{\ast} = \mathbb{R}$ is a useful one: with it the dimension formula of Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]] and the wedge product of [[§76 The Wedge Product|§76]] also hold in degree $0$. For $k > m$, $\Lambda^k V^{\ast} = \{0\}$ (Corollary [[§75 Multilinear Algebra#^cor-75-3|§75.3]]); this comes out again from the basis constructed below.

> [!remark] Remark: Notation in This Section
> The board's notation and the notation of these notes differ in a few places.
> - *The space of $k$-forms.* Lecture 28 wrote $\Lambda^k V$; Lecture 29 corrected this to $\Lambda^k V^{\ast}$, which is Lee's $\Lambda^k(V^{\ast})$. These notes write $\Lambda^k V^{\ast}$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]).
> - *The symmetric group.* The permutations are those of $\{1, \ldots, k\}$, the group $S_k$ (the board first wrote $S_n$). The board's $(-1)^\sigma$ is $\operatorname{sgn}(\sigma)$.
> - *Vectors and components.* The board writes the vectors as $v_1, \ldots, v_k$ and expands $v_i = \sum_a v_i^a e_a$. These notes keep the convention of Definition [[§75 Multilinear Algebra#^def-75-1|§75.1]] and Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](3): the vectors are $v^1, \ldots, v^k$ (label up), and $v^j = \sum_{c=1}^m v^j_c\, e_c$ (component index down), so that $\varepsilon^i(v^j) = v^j_i$.
> - *Index sets.* A $k$-element subset $A \subseteq \{1, \ldots, m\}$ is always listed increasingly, $A = \{a_1 < \cdots < a_k\}$. On the board the letters $a_1, \ldots, a_k$ also served as summation indices running over all of $\{1, \ldots, m\}$ in any order; these notes call those $c_1, \ldots, c_k$. Lee indexes the basis by increasing multi-indices $I = (i_1 < \cdots < i_k)$ and writes $\sum'_I$ for a sum over them.

^rem-75-1

*The building blocks.* The $k$-forms are built from a basis $(\varepsilon^i)_{i = 1, \ldots, m}$ of $V^{\ast}$, as determinants.

> [!definition] Definition §75.3: The Elementary $k$-Forms $\varepsilon^A$
> Let $(\varepsilon^1, \ldots, \varepsilon^m)$ be a basis of $V^{\ast}$, let $1 \le k \le m$, and let $A \subseteq \{1, \ldots, m\}$ be a subset with exactly $k$ elements, listed increasingly: $A = \{a_1 < a_2 < \cdots < a_k\}$. For $v^1, \ldots, v^k \in V$ define
>
> $$
> \varepsilon^A(v^1, \ldots, v^k) = \det\big( \varepsilon^{a_i}(v^j) \big)_{i, j = 1, \ldots, k} = \det \begin{pmatrix} \varepsilon^{a_1}(v^1) & \cdots & \varepsilon^{a_1}(v^k) \\ \vdots & & \vdots \\ \varepsilon^{a_k}(v^1) & \cdots & \varepsilon^{a_k}(v^k) \end{pmatrix} ,
> $$
>
> the $k \times k$ determinant with row index $i$ and column index $j$. For $k = 0$ the only subset is $A = \varnothing$, and $\varepsilon^{\varnothing} = 1 \in \mathbb{R} = \Lambda^0 V^{\ast}$.
>
> *Lee: Ch. 14, Elementary Alternating Tensors*

^def-75-3

The order of the elements of $A$ has to be fixed: with the elements listed in another order the rows of the determinant are permuted, and it changes by the sign of the reordering. The convention is the increasing order. That $i$ is the row index is also only a convention, since transposing a matrix does not change its determinant. Lee calls $\varepsilon^A$ an *elementary $k$-covector* and indexes it by the increasing multi-index $(a_1, \ldots, a_k)$.

> [!theorem] Lemma §75.4: The Basis of $V$ Dual to a Basis of $V^{\ast}$
> Let $(\varepsilon^1, \ldots, \varepsilon^m)$ be a basis of $V^{\ast}$. There is exactly one basis $(e_1, \ldots, e_m)$ of $V$ with
>
> $$
> \varepsilon^i(e_j) = \delta^i_j ,
> $$
>
> that is, with dual basis $(\varepsilon^i)$ (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]). It is called the basis of $V$ **dual to** $(\varepsilon^i)$.

^lem-75-4

> [!proof]+ Proof
> *(Used in Lecture 29 without comment; filled in.)* Let $(\eta_1, \ldots, \eta_m)$ be the basis of $V^{\ast\ast} = (V^{\ast})^{\ast}$ dual to the basis $(\varepsilon^i)$ of $V^{\ast}$: $\eta_j(\varepsilon^i) = \delta^i_j$ (Definition [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]] and Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], applied to the vector space $V^{\ast}$). The map $\iota : V \to V^{\ast\ast}$, $\iota(v)(\lambda) = \lambda(v)$, is a linear isomorphism (Proposition [[§21 Linear Algebra Toolkit#^prop-21-3|§21.3]]). Put $e_j = \iota^{-1}(\eta_j)$. An isomorphism carries a basis to a basis, so $(e_j)$ is a basis of $V$, and
>
> $$
> \varepsilon^i(e_j) = \iota(e_j)(\varepsilon^i) = \eta_j(\varepsilon^i) = \delta^i_j .
> $$
>
> *Uniqueness.* If $(e'_j)$ is another basis with $\varepsilon^i(e'_j) = \delta^i_j$, then the linear maps $\iota(e'_j)$ and $\eta_j$ on $V^{\ast}$ agree on the basis $(\varepsilon^i)$, so they are equal (Proposition [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]](2)), and $e'_j = \iota^{-1}(\eta_j) = e_j$.

^pf-75-4

*Uses:* [[§21 Linear Algebra Toolkit#^def-21-2|Def. §21.2]], [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]], [[§21 Linear Algebra Toolkit#^prop-21-3|§21.3]], [[§21 Linear Algebra Toolkit#^prop-21-1|§21.1]]

In the coordinates of this basis, $v^j = \sum_{c=1}^m v^j_c\, e_c$ gives $\varepsilon^{a_i}(v^j) = v^j_{a_i}$ (Proposition [[§21 Linear Algebra Toolkit#^prop-21-2|§21.2]]), so $\varepsilon^A(v^1, \ldots, v^k)$ is the minor in the rows $a_1, \ldots, a_k$ of the $m \times k$ matrix of components whose columns are $v^1, \ldots, v^k$: the form of Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](3).

> [!theorem] Lemma §75.5: The Elementary $k$-Forms on the Dual Basis
> Let $(\varepsilon^i)$ be a basis of $V^{\ast}$ and $(e_j)$ the basis of $V$ dual to it (Lemma [[§75 Multilinear Algebra#^lem-75-4|§75.4]]). Let $A = \{a_1 < \cdots < a_k\}$ and $B = \{b_1 < \cdots < b_k\}$ be $k$-element subsets of $\{1, \ldots, m\}$.
>
> 1. $\varepsilon^A$ (Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]]) is a linear $k$-form: $\varepsilon^A \in \Lambda^k V^{\ast}$.
> 2. The value of $\varepsilon^A$ on the basis vectors singled out by $B$ is
>
> $$
> \varepsilon^A(e_{b_1}, \ldots, e_{b_k}) = \delta_{AB} = \begin{cases} 1, & A = B, \\ 0, & \text{otherwise}. \end{cases}
> $$
>
> *Lee: Lemma 14.7*

^lem-75-5

> [!proof]+ Proof
> *(Lecture 29.)* (1) By the properties of the determinant. The $j$-th column of the matrix $\big(\varepsilon^{a_i}(v^j)\big)$ is $\big(\varepsilon^{a_1}(v^j), \ldots, \varepsilon^{a_k}(v^j)\big)$; it depends linearly on $v^j$, and on no other vector. The determinant is linear in each column, so $\varepsilon^A$ is multilinear. Exchanging $v^j$ and $v^{j'}$ exchanges two columns, which changes the sign of the determinant, so $\varepsilon^A$ is alternating.
>
> (2) The matrix is $\big(\varepsilon^{a_i}(e_{b_j})\big)_{i, j} = \big(\delta^{a_i}_{b_j}\big)_{i, j}$. If $A = B$, then $a_i = b_i$ for all $i$, because both sets are listed increasingly; the matrix is the identity matrix, with determinant $1$. If $A \neq B$, some $b_j$ is not in $A$, because $A$ and $B$ have the same number of elements; then $\delta^{a_i}_{b_j} = 0$ for every $i$, the $j$-th column is zero, and the determinant is $0$.

^pf-75-5

By (2), the forms $\varepsilon^A$ behave like a dual basis: each is $1$ on its own $k$-tuple of basis vectors and $0$ on the others.

> [!theorem] Proposition §75.6: A Basis of $\Lambda^k V^{\ast}$
> The set $\Lambda^k V^{\ast}$ of all linear $k$-forms on the $m$-dimensional space $V$ is a vector space, of dimension $\binom{m}{k}$. More precisely, for any basis $(\varepsilon^i)$ of $V^{\ast}$,
>
> $$
> \big\{ \varepsilon^A : A \subseteq \{1, \ldots, m\},\ |A| = k \big\}
> $$
>
> is a basis of $\Lambda^k V^{\ast}$, and if $(e_j)$ is the basis of $V$ dual to $(\varepsilon^i)$, every $\alpha \in \Lambda^k V^{\ast}$ is
>
> $$
> \alpha = \sum_{|A| = k} \alpha(e_{a_1}, \ldots, e_{a_k})\, \varepsilon^A ,
> $$
>
> the sum over all $k$-element subsets $A = \{a_1 < \cdots < a_k\}$ of $\{1, \ldots, m\}$.
>
> *Lee: Proposition 14.8*

^prop-75-6

> [!remark]- Connections
> - The top degree in Axler: the formula for $(\dim V)$-linear alternating forms, [[§36 Alternating Multilinear Forms#^ladr-9-36|LADR 9.36]], whose proof is the span step above for $k = m$.

> [!proof]+ Proof
> *(Lecture 28 for the vector space; Lecture 29 for the basis, which is constructed in the course of the proof. The notation follows the remark [[§75 Multilinear Algebra#^rem-75-1|Notation in This Section]] above.)* That $\Lambda^k V^{\ast}$ is a vector space was noted after Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]. There are exactly $\binom{m}{k}$ subsets $A$ of $\{1, \ldots, m\}$ with $k$ elements, by the definition of the binomial coefficient, so it is enough to show that the forms $\varepsilon^A$, which lie in $\Lambda^k V^{\ast}$ by Lemma [[§75 Multilinear Algebra#^lem-75-5|§75.5]](1), are linearly independent and span. Let $(e_j)$ be the basis of $V$ dual to $(\varepsilon^i)$ (Lemma [[§75 Multilinear Algebra#^lem-75-4|§75.4]]).
>
> *Linear independence.* Suppose $\sum_A c_A\, \varepsilon^A = 0$ with $c_A \in \mathbb{R}$. Fix a $k$-element subset $B = \{b_1 < \cdots < b_k\}$ and evaluate both sides on $(e_{b_1}, \ldots, e_{b_k})$. By Lemma [[§75 Multilinear Algebra#^lem-75-5|§75.5]](2),
>
> $$
> 0 = \sum_A c_A\, \varepsilon^A(e_{b_1}, \ldots, e_{b_k}) = \sum_A c_A\, \delta_{AB} = c_B .
> $$
>
> So $c_B = 0$ for every $B$.
>
> *Span.* Let $\alpha \in \Lambda^k V^{\ast}$ and $v^1, \ldots, v^k \in V$, and expand each vector in the basis, $v^j = \sum_{c=1}^m v^j_c\, e_c$. Each of the $k$ entries needs its own summation index, $c_1, \ldots, c_k$. By multilinearity,
>
> $$
> \alpha(v^1, \ldots, v^k) = \alpha\Big( \sum_{c_1=1}^m v^1_{c_1} e_{c_1}, \ldots, \sum_{c_k=1}^m v^k_{c_k} e_{c_k} \Big) = \sum_{c_1, \ldots, c_k = 1}^m \Big( \prod_{j=1}^k v^j_{c_j} \Big)\, \alpha(e_{c_1}, \ldots, e_{c_k}) .
> $$
>
> Here $c_1, \ldots, c_k$ run independently over $\{1, \ldots, m\}$, in no particular order. If two of them are equal, two entries of $\alpha(e_{c_1}, \ldots, e_{c_k})$ are equal and the term is $0$, by Lemma [[§75 Multilinear Algebra#^lem-75-2|§75.2]](1). If they are all different, $\{c_1, \ldots, c_k\}$ is a $k$-element set $A$; list it increasingly, $A = \{a_1 < \cdots < a_k\}$. Then $c_j = a_{\sigma(j)}$ for exactly one $\sigma \in S_k$, and by Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]], applied to the vectors $e_{a_1}, \ldots, e_{a_k}$,
>
> $$
> \alpha(e_{c_1}, \ldots, e_{c_k}) = \alpha\big(e_{a_{\sigma(1)}}, \ldots, e_{a_{\sigma(k)}}\big) = \operatorname{sgn}(\sigma)\, \alpha(e_{a_1}, \ldots, e_{a_k}) .
> $$
>
> So in each term with all indices different, the indices are rearranged into increasing order at the price of the factor $\operatorname{sgn}(\sigma)$. Conversely, each pair of a $k$-element set $A$ and a permutation $\sigma \in S_k$ gives one such term, the one with $c_j = a_{\sigma(j)}$. Gathering the terms with the same set $A$:
>
> $$
> \alpha(v^1, \ldots, v^k) = \sum_{|A| = k} \Big( \sum_{\sigma \in S_k} \operatorname{sgn}(\sigma) \prod_{j=1}^k v^j_{a_{\sigma(j)}} \Big)\, \alpha(e_{a_1}, \ldots, e_{a_k}) .
> $$
>
> The inner sum is a determinant. Let $M$ be the $k \times k$ matrix with entries $M_{ij} = v^j_{a_i} = \varepsilon^{a_i}(v^j)$, so that $\prod_j v^j_{a_{\sigma(j)}} = \prod_j M_{\sigma(j), j}$. The Leibniz formula (stated in the proof of Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]]), applied to the transpose $M^{\mathsf T}$, whose $(j, i)$ entry is $M_{ij}$, reads $\det M^{\mathsf T} = \sum_{\sigma} \operatorname{sgn}(\sigma) \prod_j M_{\sigma(j), j}$, and $\det M^{\mathsf T} = \det M$. Hence the inner sum is
>
> $$
> \det\big( v^j_{a_i} \big)_{i, j} = \det\big( \varepsilon^{a_i}(v^j) \big)_{i, j} = \varepsilon^A(v^1, \ldots, v^k) ,
> $$
>
> by Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]]. Therefore
>
> $$
> \alpha(v^1, \ldots, v^k) = \sum_{|A| = k} \alpha(e_{a_1}, \ldots, e_{a_k})\, \varepsilon^A(v^1, \ldots, v^k)
> $$
>
> for all $v^1, \ldots, v^k$. This is the formula of the proposition; in particular the $\varepsilon^A$ span. The coefficients are the ones forced by Lemma [[§75 Multilinear Algebra#^lem-75-5|§75.5]](2): evaluating $\alpha = \sum_A c_A \varepsilon^A$ on $(e_{b_1}, \ldots, e_{b_k})$ gives $c_B = \alpha(e_{b_1}, \ldots, e_{b_k})$.
>
> *The edge cases.* For $k = 0$ the only subset is $\varnothing$, with $\varepsilon^\varnothing = 1$, a basis of $\Lambda^0 V^{\ast} = \mathbb{R}$, and $\binom{m}{0} = 1$. For $k > m$ there are no subsets, $\binom{m}{k} = 0$, and $\Lambda^k V^{\ast} = \{0\}$ by Corollary [[§75 Multilinear Algebra#^cor-75-3|§75.3]].

^pf-75-6

*Uses:* [[§75 Multilinear Algebra#^def-75-2|Def. §75.2]], [[§75 Multilinear Algebra#^lem-75-5|§75.5]], [[§75 Multilinear Algebra#^lem-75-4|§75.4]], [[§75 Multilinear Algebra#^lem-75-2|§75.2]], [[§75 Multilinear Algebra#^lem-75-1|§75.1]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-3|§11.3]], [[§75 Multilinear Algebra#^def-75-3|Def. §75.3]], [[§75 Multilinear Algebra#^cor-75-3|§75.3]]

The proof gives more than the dimension: every $k$-form is a linear combination of determinants of size $k$, the forms $\varepsilon^A$.

**Transcription note (Lecture 29).** In the span step the board wrote the coefficient as $v_j^{\sigma(a_j)}$, letting $\sigma$ act on the elements of $A$; with $\sigma \in S_k$ acting on the positions it is $v^j_{a_{\sigma(j)}}$ in the convention of these notes (remark [[§75 Multilinear Algebra#^rem-75-1|Notation in This Section]]). The step was corrected during the lecture; the version above is the one settled on in class.

> [!theorem] Corollary §75.7: The Top Degree
> Let $\dim V = m$. The space $\Lambda^m V^{\ast}$ is one-dimensional. For any basis $(\varepsilon^i)$ of $V^{\ast}$, with $(e_j)$ the basis of $V$ dual to it, it is spanned by
>
> $$
> \varepsilon^{\{1, \ldots, m\}}(v^1, \ldots, v^m) = \det\big( \varepsilon^i(v^j) \big)_{i, j = 1, \ldots, m} ,
> $$
>
> and every $\alpha \in \Lambda^m V^{\ast}$ is $\alpha = \alpha(e_1, \ldots, e_m)\, \varepsilon^{\{1, \ldots, m\}}$.

^cor-75-7

> [!remark]- Connections
> - The top degree, $\dim \Lambda^m V^{\ast} = 1$: [[§36 Alternating Multilinear Forms#^ladr-9-37|LADR 9.37]].

> [!proof]+ Proof
> *(Stated in Lecture 28; it follows from the basis of Lecture 29.)* This is Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]] for $k = m$: the only $m$-element subset of $\{1, \ldots, m\}$ is $A = \{1, \ldots, m\}$, and $\binom{m}{m} = 1$.

^pf-75-7

*Uses:* [[§75 Multilinear Algebra#^prop-75-6|§75.6]]

On $V = \mathbb{R}^m$ with the standard basis this says that every linear $m$-form is a constant multiple of the determinant of Example [[§75 Multilinear Algebra#^ex-75-1|§75.1]](2).

> [!example] Example §75.2: The Euclidean Case
> On $V = \mathbb{R}^m$ take $\varepsilon^i = dx^i : \mathbb{R}^m \to \mathbb{R}$, the differential of the $i$-th coordinate function, which extracts the $i$-th coordinate: $dx^i(u) = u^i$. The basis of $\mathbb{R}^m$ dual to $(dx^i)$ is the standard basis. For $i < j$,
>
> $$
> \varepsilon^{\{i, j\}}(u, v) = \det \begin{pmatrix} u^i & v^i \\ u^j & v^j \end{pmatrix} = u^i v^j - u^j v^i ,
> $$
>
> which is the form $dx^i \wedge dx^j$ of Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]] (there for $m = 3$; the formula is the same for every $m$). For example, $\Lambda^2 (\mathbb{R}^4)^{\ast}$, written $\Lambda^2 \mathbb{R}^4$ on the board, has dimension $\binom{4}{2} = 6$, with basis
>
> $$
> dx^1 \wedge dx^2, \quad dx^1 \wedge dx^3, \quad dx^1 \wedge dx^4, \quad dx^2 \wedge dx^3, \quad dx^2 \wedge dx^4, \quad dx^3 \wedge dx^4 .
> $$

^ex-75-2

> [!remark]- Connections
> - MATH 452 takes these as the starting point: the coordinate 1-forms, [[§36 Introduction to Differential Forms#^def-36-1|452 Def. §36.1]], and a $k$-form on $\mathbb{R}^n$ as a combination of their wedge products, [[§36 Introduction to Differential Forms#^def-36-2|452 Def. §36.2]].
> - The six components of a two-form on spacetime $\mathbb{R}^4$ in physics: the electromagnetic field tensor, [[§B4.2 The Electromagnetic Field Tensor#^def-b4-2-2|Relativity Def. §B4.2.2]] and [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-1|Thm. §B4.2.1]] (three components of $\mathbf{E}$, three of $\mathbf{B}$).

![[m591-75-3.svg]]

*(Not from lecture; figure added.)* The six basis forms of $\Lambda^2 (\mathbb{R}^4)^{\ast}$ in Example [[§75 Multilinear Algebra#^ex-75-2|§75.2]]. The two vectors $u, v \in \mathbb{R}^4$ are the columns of a $4 \times 2$ matrix. Each two-element subset $A = \{i < j\}$ of $\{1, 2, 3, 4\}$ selects two rows (shaded), and $\varepsilon^A(u, v) = (dx^i \wedge dx^j)(u, v)$ is the $2 \times 2$ minor in those rows. There are $\binom{4}{2} = 6$ ways to choose the rows, which is the dimension. In general $\varepsilon^A(v^1, \ldots, v^k)$ is the minor in the rows $a_1 < \cdots < a_k$ of the $m \times k$ matrix with columns $v^1, \ldots, v^k$, and Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]] says that every $k$-form is a combination of these $\binom{m}{k}$ minors.

The six-dimensional space $\Lambda^2 (\mathbb{R}^4)^{\ast}$ is the one that appears in Yang–Mills theory: two-forms in four variables. *(Not from lecture.)* The first instance is electromagnetism: the field strength is a two-form on spacetime $\mathbb{R}^4$, and its six components are the three components of the electric field and the three of the magnetic field.
