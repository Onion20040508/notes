---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 78
tags: [differentiable-manifolds, math591]
---
← [[§77 The Wedge Product]] · ↑ [[· 11 Differential Forms]] · [[§79 Pullbacks of Linear Forms]] →

*Stage: forms — The wedge product is bilinear, associative and graded anticommutative; a product of one-forms is a determinant.*

*(Lecture 30, with the proofs filled in.)* The rules for computing with the wedge product of [[§77 The Wedge Product|§77]]. Three lemmas prepare the proof of the properties of the wedge product. The first two compute wedge products of one-forms; the third is what associativity needs.

> [!theorem] Lemma §78.1: A One-Form Wedge an $l$-Form
> For $\alpha \in V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$,
>
> $$
> (\alpha \wedge \beta)(v^1, \ldots, v^{l+1}) = \sum_{j=1}^{l+1} (-1)^{j-1}\, \alpha(v^j)\, \beta\big(v^1, \ldots, \widehat{v^j}, \ldots, v^{l+1}\big) ,
> $$
>
> where the hat means that $v^j$ is left out.

^lem-78-1

> [!proof]+ Proof
> *(Not from lecture; filled in. The case $l = 2$ is Example [[§77 The Wedge Product#^ex-77-2|§77.2]].)* Let $\sigma$ be a $(1, l)$-shuffle and $j = \sigma(1)$. By Definition [[§76 Shuffles#^def-76-1|§76.1]], $\sigma(2) < \cdots < \sigma(l+1)$, so these are the numbers $1, \ldots, l + 1$ other than $j$, in increasing order; and every $j \in \{1, \ldots, l+1\}$ occurs for exactly one shuffle (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](2)). The inversions of $\sigma$ (Definition [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|§11.4]]) are the pairs of positions $(1, i)$ with $\sigma(i) < j$: positions $2 \le i < i'$ are not inverted, and exactly $j - 1$ of the values $\sigma(2), \ldots, \sigma(l+1)$ are less than $j$. So $\operatorname{sgn}(\sigma) = (-1)^{j-1}$, and the term of $\sigma$ in Definition [[§77 The Wedge Product#^def-77-1|§77.1]] is $(-1)^{j-1}\, \alpha(v^j)\, \beta\big(v^1, \ldots, \widehat{v^j}, \ldots, v^{l+1}\big)$, the $j$-th term of the sum.

^pf-78-1

*Uses:* [[§76 Shuffles#^def-76-1|Def. §76.1]], [[§76 Shuffles#^lem-76-1|§76.1]], [[§11 Topological Groups and Classical Matrix Groups#^def-11-4|Def. §11.4]], [[§77 The Wedge Product#^def-77-1|Def. §77.1]]

> [!theorem] Lemma §78.2: Wedge Products of One-Forms Are Determinants
> Let $k \ge 1$ and let $\alpha^1, \alpha^2, \ldots, \alpha^k \in V^{\ast}$ be $k$ one-forms (the superscripts are labels, not powers). Bracket their product from the right,
>
> $$
> \omega = \alpha^1 \wedge \Big( \alpha^2 \wedge \big( \cdots \wedge (\alpha^{k-1} \wedge \alpha^k) \cdots \big) \Big) \in \Lambda^k V^{\ast} .
> $$
>
> Then for all $v^1, \ldots, v^k \in V$
>
> $$
> \omega(v^1, \ldots, v^k) = \det\big( \alpha^i(v^j) \big)_{i, j = 1, \ldots, k} ,
> $$
>
> a $k \times k$ determinant with row index $i$ and column index $j$.
>
> *Lee: Proposition 14.11(e)*

^lem-78-2

> [!remark]- Connections
> - The expansion of a determinant along a row, used in the proof: [[§24 Introduction to Determinants#^thm-24-1|235 Thm. §24.1]]. That the determinant is itself an alternating multilinear function of its columns: [[§37 Determinants#^ladr-9-45|LADR 9.45]].

> [!proof]+ Proof
> *(Lecture 30 stated the lemma for the product $\alpha^1 \wedge \cdots \wedge \alpha^k$ with its brackets placed in any way, which associativity allows (Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](2), proved below without this lemma), and indicated the proof: induction on $k$, expanding a $k \times k$ determinant along a row. Written out here for the bracketing from the right, which needs no associativity.)* For $k = 1$ both sides are $\alpha^1(v^1)$. Let $k \ge 2$ and assume the lemma for $k - 1$ one-forms. Then $\omega = \alpha^1 \wedge \beta$, where $\beta \in \Lambda^{k-1} V^{\ast}$ is the product of $\alpha^2, \ldots, \alpha^k$ bracketed from the right, and by the induction hypothesis
>
> $$
> \beta(w^1, \ldots, w^{k-1}) = \det\big( \alpha^{i+1}(w^j) \big)_{i, j = 1, \ldots, k-1} \qquad \text{for all } w^1, \ldots, w^{k-1} \in V .
> $$
>
> Let $M$ be the $k \times k$ matrix with entries $M_{ij} = \alpha^i(v^j)$, and let $M^{(1j)}$ be $M$ with the first row and the $j$-th column deleted: its rows belong to $\alpha^2, \ldots, \alpha^k$ and its columns to the vectors other than $v^j$, in their order. So $\beta\big(v^1, \ldots, \widehat{v^j}, \ldots, v^k\big) = \det M^{(1j)}$, and by Lemma [[§78 Properties of the Wedge Product#^lem-78-1|§78.1]]
>
> $$
> \omega(v^1, \ldots, v^k) = \sum_{j=1}^k (-1)^{j-1}\, \alpha^1(v^j)\, \beta\big(v^1, \ldots, \widehat{v^j}, \ldots, v^k\big) = \sum_{j=1}^k (-1)^{1+j}\, M_{1j}\, \det M^{(1j)} .
> $$
>
> The right-hand side is the expansion of $\det M$ along its first row.

^pf-78-2

*Uses:* [[§78 Properties of the Wedge Product#^lem-78-1|§78.1]]

For $k = 2$ the lemma is Example [[§77 The Wedge Product#^ex-77-1|§77.1]], and for $k = 3$ it is the $3 \times 3$ determinant of Example [[§77 The Wedge Product#^ex-77-2|§77.2]].

> [!theorem] Lemma §78.3: The Skew-Symmetrizer and Tensor Products
> Let $\mathcal{A}$ be the skew-symmetrizer (Definition [[§77 The Wedge Product#^def-77-3|§77.3]]).
>
> 1. For a multilinear map $U : V^N \to \mathbb{R}$ and $\mu \in S_N$: $\mathcal{A}(U^\mu) = \operatorname{sgn}(\mu)\, \mathcal{A}(U)$.
> 2. For multilinear maps $S : V^n \to \mathbb{R}$ and $T : V^r \to \mathbb{R}$ (Definition [[§77 The Wedge Product#^def-77-2|§77.2]]):
>
> $$
> \mathcal{A}\big(\mathcal{A}(S) \otimes T\big) = \mathcal{A}(S \otimes T) = \mathcal{A}\big(S \otimes \mathcal{A}(T)\big) .
> $$

^lem-78-3

> [!proof]+ Proof
> *(Not from lecture; filled in, with the antisymmetrizer of Lecture 30.)*
>
> (1) By the rule for rearranging twice in the proof of Lemma [[§77 The Wedge Product#^lem-77-1|§77.1]], $(U^\mu)^\pi = U^{\pi \circ \mu}$ for every $\pi \in S_N$. Since $\operatorname{sgn}(\pi) = \operatorname{sgn}(\mu)\, \operatorname{sgn}(\pi \circ \mu)$ (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](1), with $\operatorname{sgn}(\mu)^2 = 1$),
>
> $$
> \mathcal{A}(U^\mu) = \frac{1}{N!} \sum_{\pi \in S_N} \operatorname{sgn}(\pi)\, U^{\pi \circ \mu} = \operatorname{sgn}(\mu)\, \frac{1}{N!} \sum_{\pi \in S_N} \operatorname{sgn}(\pi \circ \mu)\, U^{\pi \circ \mu} = \operatorname{sgn}(\mu)\, \mathcal{A}(U) ;
> $$
>
> the last step holds because $\pi \mapsto \pi \circ \mu$ is a bijection of $S_N$.
>
> (2) For $\pi \in S_n$ let $\pi \oplus \mathrm{id} \in S_{n+r}$ be the permutation that acts by $\pi$ on $\{1, \ldots, n\}$ and fixes $n + 1, \ldots, n + r$. It lies in the subgroup $S_n \times S_r$, and $\operatorname{sgn}(\pi \oplus \mathrm{id}) = \operatorname{sgn}(\pi)$ (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](1), with $\tau = \pi$ and $\tau' = \mathrm{id}$). By Definitions [[§77 The Wedge Product#^def-77-2|§77.2]] and [[§77 The Wedge Product#^def-77-3|§77.3]],
>
> $$
> (S \otimes T)^{\pi \oplus \mathrm{id}}(v^1, \ldots, v^{n+r}) = S\big(v^{\pi(1)}, \ldots, v^{\pi(n)}\big)\, T(v^{n+1}, \ldots, v^{n+r}) = (S^\pi \otimes T)(v^1, \ldots, v^{n+r}) ,
> $$
>
> so $S^\pi \otimes T = (S \otimes T)^{\pi \oplus \mathrm{id}}$. The tensor product is linear in its first factor, since the value of $S \otimes T$ is the product of a value of $S$ and a value of $T$; hence $\mathcal{A}(S) \otimes T = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)\, S^\pi \otimes T$. As $\mathcal{A}$ is linear, part (1) gives
>
> $$
> \mathcal{A}\big(\mathcal{A}(S) \otimes T\big) = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)\, \mathcal{A}\big((S \otimes T)^{\pi \oplus \mathrm{id}}\big) = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)^2\, \mathcal{A}(S \otimes T) = \mathcal{A}(S \otimes T) ,
> $$
>
> as $S_n$ has $n!$ elements. For the second equality let $\mathrm{id} \oplus \pi' \in S_{n+r}$, for $\pi' \in S_r$, fix $1, \ldots, n$ and send $n + j$ to $n + \pi'(j)$; then $\operatorname{sgn}(\mathrm{id} \oplus \pi') = \operatorname{sgn}(\pi')$ and $S \otimes T^{\pi'} = (S \otimes T)^{\mathrm{id} \oplus \pi'}$ by the same two definitions, and the same computation, with the sum over $\pi' \in S_r$ and the factor $\frac{1}{r!}$, gives $\mathcal{A}\big(S \otimes \mathcal{A}(T)\big) = \mathcal{A}(S \otimes T)$.

^pf-78-3

*Uses:* [[§77 The Wedge Product#^lem-77-1|§77.1]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]], [[§76 Shuffles#^lem-76-1|§76.1]], [[§77 The Wedge Product#^def-77-2|Def. §77.2]], [[§77 The Wedge Product#^def-77-3|Def. §77.3]]

> [!theorem] Proposition §78.4: Properties of the Wedge Product
> For $\alpha, \alpha_1, \alpha_2 \in \Lambda^k V^{\ast}$, $\beta \in \Lambda^l V^{\ast}$, $\gamma \in \Lambda^r V^{\ast}$ and $\lambda \in \mathbb{R}$:
>
> 1. *bilinear*: $(\alpha_1 + \lambda\alpha_2) \wedge \beta = \alpha_1 \wedge \beta + \lambda\, \alpha_2 \wedge \beta$, and likewise in $\beta$;
> 2. *associative*: $\alpha \wedge (\beta \wedge \gamma) = (\alpha \wedge \beta) \wedge \gamma$;
> 3. *graded anticommutative*: $\beta \wedge \alpha = (-1)^{kl}\, \alpha \wedge \beta$; in particular, forms of even degree commute with all forms;
> 4. for a basis $(\varepsilon^i)$ of $V^{\ast}$ and $A = \{a_1 < \cdots < a_k\}$: $\varepsilon^A = \varepsilon^{a_1} \wedge \cdots \wedge \varepsilon^{a_k}$ (Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]]).
>
> *Lee: Proposition 14.11*

^prop-78-4

> [!remark]- Connections
> - MATH 452 takes (1)–(3) for the coordinate one-forms as the rules that define the wedge product, [[§37 The Algebra of Differential Forms#^def-37-1|452 Def. §37.1]]; property (4) with a permuted or repeated index set is [[§37 The Algebra of Differential Forms#^prop-37-1|452 Prop. §37.1]] (the Levi-Civita symbol).

> [!proof]+ Proof
> *(Lecture 29 stated the four properties. Lecture 30 recalled them and proved (3), using (4), which it read off Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]]. The proof of (2), which neither lecture gave, is filled in. The order below is (1), (2), (4), (3), so that nothing is used before it is proved.)*
>
> (1) By Definition [[§77 The Wedge Product#^def-77-1|§77.1]], for fixed vectors each term of the sum is the product of a value of $\alpha$ and a value of $\beta$, so it is linear in $\alpha$ and linear in $\beta$; hence so is the sum.
>
> (2) *(Not from lecture; filled in.)* By Proposition [[§77 The Wedge Product#^prop-77-2|§77.2]](2), applied first to the forms $\alpha \wedge \beta \in \Lambda^{k+l} V^{\ast}$ and $\gamma$, and then to $\alpha$ and $\beta$,
>
> $$
> (\alpha \wedge \beta) \wedge \gamma = \frac{(k + l + r)!}{(k + l)!\, r!}\, \mathcal{A}\big((\alpha \wedge \beta) \otimes \gamma\big) = \frac{(k + l + r)!}{(k + l)!\, r!} \cdot \frac{(k + l)!}{k!\, l!}\, \mathcal{A}\big(\mathcal{A}(\alpha \otimes \beta) \otimes \gamma\big) ,
> $$
>
> the second step because the tensor product is linear in its first factor and $\mathcal{A}$ is linear. By Lemma [[§78 Properties of the Wedge Product#^lem-78-3|§78.3]](2), $\mathcal{A}\big(\mathcal{A}(\alpha \otimes \beta) \otimes \gamma\big) = \mathcal{A}\big((\alpha \otimes \beta) \otimes \gamma\big)$, so
>
> $$
> (\alpha \wedge \beta) \wedge \gamma = \frac{(k + l + r)!}{k!\, l!\, r!}\, \mathcal{A}\big((\alpha \otimes \beta) \otimes \gamma\big) .
> $$
>
> In the same way, with the other equality of Lemma [[§78 Properties of the Wedge Product#^lem-78-3|§78.3]](2),
>
> $$
> \alpha \wedge (\beta \wedge \gamma) = \frac{(k + l + r)!}{k!\, (l + r)!} \cdot \frac{(l + r)!}{l!\, r!}\, \mathcal{A}\big(\alpha \otimes \mathcal{A}(\beta \otimes \gamma)\big) = \frac{(k + l + r)!}{k!\, l!\, r!}\, \mathcal{A}\big(\alpha \otimes (\beta \otimes \gamma)\big) .
> $$
>
> Finally $(\alpha \otimes \beta) \otimes \gamma = \alpha \otimes (\beta \otimes \gamma)$: by Definition [[§77 The Wedge Product#^def-77-2|§77.2]] both send $(v^1, \ldots, v^{k+l+r})$ to
>
> $$
> \alpha(v^1, \ldots, v^k)\, \beta(v^{k+1}, \ldots, v^{k+l})\, \gamma(v^{k+l+1}, \ldots, v^{k+l+r}) .
> $$
>
> So the two triple products are equal. By induction on the number of factors, a wedge product of any number of forms does not depend on how it is bracketed, and brackets are omitted from here on.
>
> (4) *(Lecture 30.)* Let $k \ge 1$. By Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]] with $\alpha^i = \varepsilon^{a_i}$, and by (2), which allows the brackets to be dropped,
>
> $$
> \big(\varepsilon^{a_1} \wedge \cdots \wedge \varepsilon^{a_k}\big)(v^1, \ldots, v^k) = \det\big(\varepsilon^{a_i}(v^j)\big)_{i, j = 1, \ldots, k} = \varepsilon^A(v^1, \ldots, v^k) ,
> $$
>
> the last equality being Definition [[§75 Multilinear Algebra#^def-75-3|§75.3]]: the forms $\varepsilon^A$ were defined as $k \times k$ determinants, and the lemma says that a product of $k$ one-forms is such a determinant.
>
> (3) *(Lecture 30.)* *Degree zero.* If $k = 0$, then $\alpha$ is a number $c$, the only $(0, l)$-shuffle and the only $(l, 0)$-shuffle are the identity, and Definition [[§77 The Wedge Product#^def-77-1|§77.1]] gives $c \wedge \beta = c\,\beta = \beta \wedge c$, which is (3) since $(-1)^0 = 1$; likewise if $l = 0$. Let $k, l \ge 1$.
>
> *Reduction to products of one-forms.* Let $(\varepsilon^1, \ldots, \varepsilon^m)$ be a basis of $V^{\ast}$. The forms $\varepsilon^A$ with $|A| = k$ are a basis of $\Lambda^k V^{\ast}$, and the $\varepsilon^B$ with $|B| = l$ a basis of $\Lambda^l V^{\ast}$ (Proposition [[§75 Multilinear Algebra#^prop-75-6|§75.6]]). Both $\beta \wedge \alpha$ and $(-1)^{kl}\, \alpha \wedge \beta$ are bilinear in $(\alpha, \beta)$, by (1), so it is enough to prove (3) for $\alpha = \varepsilon^A$ and $\beta = \varepsilon^B$. By (4) these are products of one-forms,
>
> $$
> \alpha = \alpha^1 \wedge \cdots \wedge \alpha^k, \qquad \beta = \beta^1 \wedge \cdots \wedge \beta^l , \qquad \alpha^i = \varepsilon^{a_i}, \quad \beta^j = \varepsilon^{b_j} .
> $$
>
> *One-forms anticommute.* For $\mu, \nu \in V^{\ast}$, $\mu \wedge \nu = -\nu \wedge \mu$: by Example [[§77 The Wedge Product#^ex-77-1|§77.1]], $(\mu \wedge \nu)(v^1, v^2) = \mu(v^1)\nu(v^2) - \mu(v^2)\nu(v^1)$, and exchanging $\mu$ and $\nu$ changes the sign.
>
> *Commuting the factors.* By (2), $\alpha \wedge \beta = \alpha^1 \wedge \cdots \wedge \alpha^k \wedge \beta^1 \wedge \cdots \wedge \beta^l$, a product of $k + l$ one-forms. Exchanging two neighbouring one-forms in such a product changes its sign: bracket the two neighbours together, by (2), replace $\mu \wedge \nu$ by $-\nu \wedge \mu$, and use (1). Move $\beta^1$ to the left, past $\alpha^k$, then past $\alpha^{k-1}$, and so on to the front; it passes $k$ one-forms, so
>
> $$
> \alpha^1 \wedge \cdots \wedge \alpha^k \wedge \beta^1 \wedge \cdots \wedge \beta^l = (-1)^k\, \beta^1 \wedge \alpha^1 \wedge \cdots \wedge \alpha^k \wedge \beta^2 \wedge \cdots \wedge \beta^l .
> $$
>
> Then move $\beta^2$ to the left past $\alpha^k, \ldots, \alpha^1$, to the place behind $\beta^1$, for another factor $(-1)^k$, and so on. After all $l$ of the $\beta^j$ have been moved,
>
> $$
> \alpha \wedge \beta = \big((-1)^k\big)^l\, \beta^1 \wedge \cdots \wedge \beta^l \wedge \alpha^1 \wedge \cdots \wedge \alpha^k = (-1)^{kl}\, \beta \wedge \alpha ,
> $$
>
> and multiplying by $(-1)^{kl}$ gives (3). Forms of even degree commute with all forms because $(-1)^{kl} = 1$ when $k$ or $l$ is even.

^pf-78-4

*Uses:* [[§77 The Wedge Product#^def-77-1|Def. §77.1]], [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]], [[§77 The Wedge Product#^prop-77-2|§77.2]], [[§78 Properties of the Wedge Product#^lem-78-3|§78.3]], [[§77 The Wedge Product#^def-77-2|Def. §77.2]], [[§75 Multilinear Algebra#^def-75-3|Def. §75.3]], [[§75 Multilinear Algebra#^prop-75-6|§75.6]], [[§77 The Wedge Product#^ex-77-1|Ex. §77.1]]

With (2), the brackets in Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]] can be placed in any way: $(\alpha^1 \wedge \cdots \wedge \alpha^k)(v^1, \ldots, v^k) = \det\big(\alpha^i(v^j)\big)$ for any $k$ one-forms, which is the form in which Lecture 30 stated the lemma. Lee proves (2) and (3) differently, from the formula $\varepsilon^I \wedge \varepsilon^J = \varepsilon^{IJ}$ for elementary forms (his Lemma 14.10); in (3) his sign is the sign of the permutation that carries the block of $\beta$ in front of the block of $\alpha$, a product of $kl$ transpositions.

![[m591-76-6.svg]]

*(Not from lecture; figure added.)* The sign in Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](3). The top row is $\alpha \wedge \beta = \alpha^1 \wedge \cdots \wedge \alpha^k \wedge \beta^1 \wedge \cdots \wedge \beta^l$ and the bottom row $\beta \wedge \alpha$; a strand joins each one-form to its new place. Every strand of $\beta$ (blue) crosses every strand of $\alpha$ (red) exactly once, and each crossing is one exchange of two neighbouring one-forms, with a factor $-1$. So there are $kl$ crossings and the sign is $(-1)^{kl}$: it is $-1$ only when $k$ and $l$ are both odd.

![[m591-76-a2.gif|620]]

*(Not from lecture; animation added, vault only.)* The proof of Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](3) in motion, for $k = 3$ and $l = 2$. The one-form $\beta^1$ is exchanged with its left neighbour three times, until it stands in front of $\alpha^1 \wedge \alpha^2 \wedge \alpha^3$: three factors $-1$, that is $(-1)^k$. Then $\beta^2$ does the same and stops behind $\beta^1$, for another $(-1)^k$. After the $kl = 6$ exchanges the product is $\beta \wedge \alpha$, and the sign is $((-1)^k)^l = (-1)^{kl} = +1$. Each exchange is one crossing in the figure above.

> [!theorem] Corollary §78.5: Forms of Odd Degree Square to Zero
> If $\alpha \in \Lambda^k V^{\ast}$ with $k$ odd, then $\alpha \wedge \alpha = 0$. In particular $\varepsilon \wedge \varepsilon = 0$ for every covector $\varepsilon \in V^{\ast}$.

^cor-78-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* By Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](3) with $\beta = \alpha$ and $l = k$: $\alpha \wedge \alpha = (-1)^{k^2}\, \alpha \wedge \alpha = -\alpha \wedge \alpha$, since $k^2$ is odd. So $2\, \alpha \wedge \alpha = 0$. For a covector, $k = 1$; this can also be read off Example [[§77 The Wedge Product#^ex-77-1|§77.1]]: $(\varepsilon \wedge \varepsilon)(v^1, v^2) = \varepsilon(v^1)\varepsilon(v^2) - \varepsilon(v^2)\varepsilon(v^1) = 0$.

^pf-78-5

*Uses:* [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]], [[§77 The Wedge Product#^ex-77-1|Ex. §77.1]]

For $\varepsilon = dx^i$ this is $dx^i \wedge dx^i = 0$, as in Lemma [[§74 The Integrand Is a Two-Form#^lem-74-1|§74.1]](2).

> [!example] Example §78.1: A Form of Even Degree with Nonzero Square
> *(Not from lecture; filled in.)* For even degree the corollary fails. On $\mathbb{R}^4$ let
>
> $$
> \omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4 \in \Lambda^2 (\mathbb{R}^4)^{\ast} , \qquad \omega(u, v) = u^1 v^2 - u^2 v^1 + u^3 v^4 - u^4 v^3
> $$
>
> (Example [[§75 Multilinear Algebra#^ex-75-2|§75.2]]). On the standard basis, $\omega(e_1, e_2) = \omega(e_3, e_4) = 1$, and $\omega(e_i, e_j) = 0$ for the other pairs $i < j$. By the six-term formula of Example [[§77 The Wedge Product#^ex-77-3|§77.3]] with $\alpha = \beta = \omega$, only the first and the last term are not zero:
>
> $$
> (\omega \wedge \omega)(e_1, e_2, e_3, e_4) = \omega(e_1, e_2)\,\omega(e_3, e_4) + \omega(e_3, e_4)\,\omega(e_1, e_2) = 2 .
> $$
>
> So $\omega \wedge \omega \neq 0$. By Corollary [[§75 Multilinear Algebra#^cor-75-7|§75.7]], $\omega \wedge \omega = 2\, \varepsilon^{\{1, 2, 3, 4\}}$, twice the determinant; with Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4) this reads $\omega \wedge \omega = 2\, dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4$.

^ex-78-1

Next: one more piece of linear algebra, the pullback of forms by a linear map ([[§79 Pullbacks of Linear Forms|§79]]); then $V$ becomes the tangent space $T_pM$ again, and the point $p$ varies over a manifold, so that the forms become functions of the point ([[§80 Differential Forms on Manifolds|§80]]). (Lecture 30 ended with the proof of Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](3).)
