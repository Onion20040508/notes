---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 11
section: 77
tags: [differentiable-manifolds, math591]
---
← [[§76 Shuffles]] · ↑ [[· 11 Differential Forms]] · [[§78 Properties of the Wedge Product]] →

*Stage: forms — Multiplying a $k$-form and an $l$-form into a $(k + l)$-form, by a signed sum over shuffles; why the product is alternating; the first cases computed.*

*(Lectures 29 and 30.)* This section defines the wedge product: a product that takes a $k$-form $\alpha$ and an $l$-form $\beta$ on $V$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]) to a $(k + l)$-form $\alpha \wedge \beta$, by a sum over the shuffles of [[§76 Shuffles|§76]]. The forms of all degrees with this product make up the *Grassmann algebra* of $V$ (Lee: the exterior algebra). It was developed in the 19th century, and brought into its present form, for differential forms, by \'Elie Cartan in the first half of the 20th century. Throughout, $V$ is an $m$-dimensional real vector space and $k, l \ge 0$.

> [!definition] Definition §77.1: Wedge Product
> Given $\alpha \in \Lambda^k V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$ (Definition [[§75 Multilinear Algebra#^def-75-2|§75.2]]), their **wedge product** is the function $\alpha \wedge \beta : V^{k+l} \to \mathbb{R}$,
>
> $$
> (\alpha \wedge \beta)(v^1, \ldots, v^{k+l}) = \sum_{\sigma \in \mathrm{Sh}(k, l)} \operatorname{sgn}(\sigma)\, \alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big)\, \beta\big(v^{\sigma(k+1)}, \ldots, v^{\sigma(k+l)}\big) ,
> $$
>
> the sum over all $(k, l)$-shuffles (Definition [[§76 Shuffles#^def-76-1|§76.1]]). It is a linear $(k + l)$-form, $\alpha \wedge \beta \in \Lambda^{k+l} V^{\ast}$ (Proposition [[§77 The Wedge Product#^prop-77-2|§77.2]](3)).
>
> *Lee: Ch. 14, The Wedge Product*

^def-77-1

> [!remark]- Connections
> - MATH 452 introduces the wedge product of forms on $\mathbb{R}^n$ by its rules (anticommutativity of the $dx_i$, bilinearity, associativity), [[§37 The Algebra of Differential Forms#^def-37-1|452 Def. §37.1]]; here it is defined by a formula and the rules become Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]].

Degrees add under multiplication, as a degree should. Each term of the sum hands $k$ of the $k + l$ vectors to $\alpha$ and the remaining $l$ to $\beta$, both in increasing order of their labels; by Lemma [[§76 Shuffles#^lem-76-1|§76.1]](2) there is one term for each way of choosing which $k$ vectors go to $\alpha$, and its sign is the sign of the shuffle. For $k = 0$, $\alpha$ is a number $c$, the only $(0, l)$-shuffle is the identity, and $c \wedge \beta = c\, \beta$. In practice the formula is used directly only in low degrees.

**Transcription note (Lecture 29).** The board wrote $(-1)^\sigma$ for $\operatorname{sgn}(\sigma)$, lower labels $v_{\sigma(1)}, \ldots$ for the vectors, and $r_{\sigma(1)}, \ldots, r_{\sigma(k)}$ in the entries of $\alpha$, which are $v^{\sigma(1)}, \ldots, v^{\sigma(k)}$.

One can also sum over all permutations of $\{1, \ldots, k+l\}$ instead of the shuffles, but then there are many repetitions: in each term the entries of $\alpha$, and those of $\beta$, can be put into increasing order at the price of a sign. This, and the algebraic meaning of the formula, are made precise next. Lecture 29 presented the algebraic description for conceptual understanding only; it is not used in computations. Lecture 30 returned to it to answer a question left from Lecture 29: why is $\alpha \wedge \beta$ alternating, which the shuffle formula does not show at a glance? The answer is Proposition [[§77 The Wedge Product#^prop-77-2|§77.2]]: the shuffle sum is a multiple of the skew-symmetrization of $\alpha \otimes \beta$, and a skew-symmetrization is always alternating.

> [!definition] Definition §77.2: Tensor Product of Multilinear Maps
> Let $S : V^k \to \mathbb{R}$ and $T : V^l \to \mathbb{R}$ be multilinear. Their **tensor product** is the map $S \otimes T : V^{k+l} \to \mathbb{R}$,
>
> $$
> (S \otimes T)(v^1, \ldots, v^{k+l}) = S(v^1, \ldots, v^k)\, T(v^{k+1}, \ldots, v^{k+l}) .
> $$
>
> It is multilinear.
>
> *Lee: Ch. 12, Multilinear Algebra*

^def-77-2

$S \otimes T$ is linear in each of the first $k$ entries because $S$ is, and in each of the last $l$ entries because $T$ is. For forms $\alpha \in \Lambda^k V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$ the tensor product $\alpha \otimes \beta$ is multilinear but in general not alternating: for $k = l = 1$, $(\alpha \otimes \beta)(v, v) = \alpha(v)\beta(v)$, which is not $0$ when $\alpha(v) \neq 0 \neq \beta(v)$ (compare Lemma [[§75 Multilinear Algebra#^lem-75-2|§75.2]](1)). The board writes $V^{\ast} \otimes \cdots \otimes V^{\ast}$ ($n$ factors) for the vector space of all multilinear maps $V^n \to \mathbb{R}$.

> [!definition] Definition §77.3: The Skew-Symmetrizer
> Let $T : V^n \to \mathbb{R}$ be multilinear. For $\pi \in S_n$ let $T^\pi$ be $T$ with its entries rearranged by $\pi$,
>
> $$
> T^\pi(v^1, \ldots, v^n) = T\big(v^{\pi(1)}, \ldots, v^{\pi(n)}\big) .
> $$
>
> The **skew-symmetrizer** is the map $\mathcal{A}$ that sends $T$ to
>
> $$
> \mathcal{A}(T) = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)\, T^\pi .
> $$
>
> *Lee: Ch. 14, The Algebra of Alternating Tensors*

^def-77-3

*(Lecture 29 named the map and described it as the natural projection onto the completely antisymmetric maps; Lecture 30 wrote the formula, in the letters of the remark [[§76 Shuffles#^rem-76-1|Notation of Lecture 30]], and called the map the antisymmetrizer. Lee calls it alternation and writes $\operatorname{Alt}$.)* Each $T^\pi$ is multilinear, so $\mathcal{A}(T)$ is multilinear, and $\mathcal{A}$ is a linear map from the space of multilinear maps $V^n \to \mathbb{R}$ to itself.

> [!theorem] Lemma §77.1: The Skew-Symmetrizer Projects onto the Forms
> Let $T : V^n \to \mathbb{R}$ be multilinear and $\mathcal{A}$ the skew-symmetrizer (Definition [[§77 The Wedge Product#^def-77-3|§77.3]]).
>
> 1. $\mathcal{A}(T)$ is alternating: $\mathcal{A}(T) \in \Lambda^n V^{\ast}$.
> 2. If $T$ is alternating, then $\mathcal{A}(T) = T$.
>
> So $\mathcal{A}$ is a linear projection of the space of multilinear maps $V^n \to \mathbb{R}$ onto $\Lambda^n V^{\ast}$: its image is $\Lambda^n V^{\ast}$, and $\mathcal{A} \circ \mathcal{A} = \mathcal{A}$.
>
> *Lee: Proposition 14.3*

^lem-77-1

> [!proof]+ Proof
> *(Lecture 30 proved (1), by the change of variables in the sum used below, and observed (2). The rule for rearranging twice is added to keep track of the order of composition.)* *A rule for rearranging twice.* For $\pi, \mu \in S_n$, $(T^\pi)^\mu = T^{\mu \circ \pi}$. Indeed, put $w^i = v^{\mu(i)}$; then
>
> $$
> \begin{aligned}
> (T^\pi)^\mu(v^1, \ldots, v^n) &= T^\pi(w^1, \ldots, w^n) = T\big(w^{\pi(1)}, \ldots, w^{\pi(n)}\big) \\
> &= T\big(v^{\mu(\pi(1))}, \ldots, v^{\mu(\pi(n))}\big) = T^{\mu \circ \pi}(v^1, \ldots, v^n) .
> \end{aligned}
> $$
>
> (1) Let $\mu \in S_n$. By the rule, and since $\operatorname{sgn}(\pi) = \operatorname{sgn}(\mu)\, \operatorname{sgn}(\mu \circ \pi)$ (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](1), with $\operatorname{sgn}(\mu)^2 = 1$),
>
> $$
> \mathcal{A}(T)^\mu = \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\pi)\, T^{\mu \circ \pi} = \operatorname{sgn}(\mu)\, \frac{1}{n!} \sum_{\pi \in S_n} \operatorname{sgn}(\mu \circ \pi)\, T^{\mu \circ \pi} = \operatorname{sgn}(\mu)\, \mathcal{A}(T) ;
> $$
>
> the last step holds because $\pi \mapsto \mu \circ \pi$ is a bijection of $S_n$, so the sum runs over all of $S_n$ again. Thus $\mathcal{A}(T)\big(v^{\mu(1)}, \ldots, v^{\mu(n)}\big) = \operatorname{sgn}(\mu)\, \mathcal{A}(T)(v^1, \ldots, v^n)$ for every $\mu$, and $\mathcal{A}(T)$ is multilinear. By the converse in Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]], $\mathcal{A}(T)$ is alternating.
>
> (2) If $T$ is alternating, $T^\pi = \operatorname{sgn}(\pi)\, T$ for every $\pi$, by Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]]. Then $\mathcal{A}(T) = \frac{1}{n!} \sum_\pi \operatorname{sgn}(\pi)^2\, T = T$, as $S_n$ has $n!$ elements.
>
> *The projection.* By (1) the image of $\mathcal{A}$ lies in $\Lambda^n V^{\ast}$, and by (2) every element of $\Lambda^n V^{\ast}$ is its own image. Applying (2) to the alternating map $\mathcal{A}(T)$ gives $\mathcal{A}(\mathcal{A}(T)) = \mathcal{A}(T)$.

^pf-77-1

*Uses:* [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]], [[§75 Multilinear Algebra#^lem-75-1|§75.1]]

**Transcription note (Lecture 30).** On the board the proof of (1) reads: for $\tau \in S_n$,

$$
A(\psi)(v_{\tau(1)}, \ldots, v_{\tau(n)}) = \frac{1}{n!} \sum_\sigma (-1)^\sigma\, \psi(v_{\sigma(\tau(1))}, \ldots, v_{\sigma(\tau(n))}) ;
$$

then $\mu = \sigma \circ \tau$ is substituted, with $(-1)^{\mu \circ \tau^{-1}} = (-1)^\mu (-1)^\tau$, and the sum over $\mu$ gives $(-1)^\tau A(\psi)(v_1, \ldots, v_n)$. The subscripts compose in the other order: with $w_i = v_{\tau(i)}$ one has $w_{\sigma(i)} = v_{\tau(\sigma(i))}$, so the substitution is $\mu = \tau \circ \sigma$, which is the rule $(T^\pi)^\mu = T^{\mu \circ \pi}$ of the proof above. The argument is not affected: $\sigma \mapsto \tau \circ \sigma$ is also a bijection of $S_n$, and $\operatorname{sgn}(\tau \circ \sigma) = \operatorname{sgn}(\tau)\,\operatorname{sgn}(\sigma)$.

> [!theorem] Proposition §77.2: The Wedge Product as a Skew-Symmetrized Tensor Product
> Let $\alpha \in \Lambda^k V^{\ast}$ and $\beta \in \Lambda^l V^{\ast}$.
>
> 1. The wedge product (Definition [[§77 The Wedge Product#^def-77-1|§77.1]]) is also the sum over all permutations, divided by $k!\, l!$:
>
> $$
> (\alpha \wedge \beta)(v^1, \ldots, v^{k+l}) = \frac{1}{k!\, l!} \sum_{\pi \in S_{k+l}} \operatorname{sgn}(\pi)\, \alpha\big(v^{\pi(1)}, \ldots, v^{\pi(k)}\big)\, \beta\big(v^{\pi(k+1)}, \ldots, v^{\pi(k+l)}\big) .
> $$
>
> 2. In terms of the tensor product (Definition [[§77 The Wedge Product#^def-77-2|§77.2]]) and the skew-symmetrizer (Definition [[§77 The Wedge Product#^def-77-3|§77.3]]),
>
> $$
> \alpha \wedge \beta = \frac{(k + l)!}{k!\, l!}\, \mathcal{A}(\alpha \otimes \beta) .
> $$
>
> 3. $\alpha \wedge \beta$ is a linear $(k + l)$-form: $\alpha \wedge \beta \in \Lambda^{k+l} V^{\ast}$.
>
> *Lee: Ch. 14, The Wedge Product*

^prop-77-2

> [!proof]+ Proof
> *((1) was stated in Lecture 29, and (2) in the form $\alpha \wedge \beta = \mathcal{A}(\alpha \otimes \beta)$. Lecture 30 stated (2) with its factor, as the lemma $A(\alpha \otimes \beta) = \frac{k!\, l!}{(k+l)!}\, \alpha \wedge \beta$, and proved it in outline by the factorization of Lemma [[§76 Shuffles#^lem-76-1|§76.1]](3). This is that proof with the details filled in; in the board's letters, $\pi, \sigma, \tau, \tau'$ below are $\sigma, s, \lambda, \tau$.)* Write $n = k + l$.
>
> (1) Let $\pi \in S_n$ and factor it as $\pi = \sigma \circ \rho$ with $\sigma \in \mathrm{Sh}(k, l)$ and $\rho \in S_k \times S_l$ (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](3)), where $\rho$ acts by $\tau \in S_k$ on $\{1, \ldots, k\}$ and by $\rho(k + j) = k + \tau'(j)$, $\tau' \in S_l$. Put $u^i = v^{\sigma(i)}$ for $i \le k$ and $w^j = v^{\sigma(k + j)}$ for $j \le l$. Then $v^{\pi(i)} = v^{\sigma(\tau(i))} = u^{\tau(i)}$ and $v^{\pi(k + j)} = v^{\sigma(k + \tau'(j))} = w^{\tau'(j)}$, and by Lemma [[§75 Multilinear Algebra#^lem-75-1|§75.1]], applied to $\alpha$ and to $\beta$,
>
> $$
> \alpha\big(v^{\pi(1)}, \ldots, v^{\pi(k)}\big) = \alpha\big(u^{\tau(1)}, \ldots, u^{\tau(k)}\big) = \operatorname{sgn}(\tau)\, \alpha\big(v^{\sigma(1)}, \ldots, v^{\sigma(k)}\big) ,
> $$
>
> $$
> \beta\big(v^{\pi(k+1)}, \ldots, v^{\pi(k+l)}\big) = \beta\big(w^{\tau'(1)}, \ldots, w^{\tau'(l)}\big) = \operatorname{sgn}(\tau')\, \beta\big(v^{\sigma(k+1)}, \ldots, v^{\sigma(k+l)}\big) .
> $$
>
> Also $\operatorname{sgn}(\pi) = \operatorname{sgn}(\sigma)\, \operatorname{sgn}(\rho) = \operatorname{sgn}(\sigma)\, \operatorname{sgn}(\tau)\, \operatorname{sgn}(\tau')$ (Proposition [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]](1) and Lemma [[§76 Shuffles#^lem-76-1|§76.1]](1)). Multiplying the three equations, the signs of $\tau$ and $\tau'$ appear squared, and the term of $\pi$ in the sum over $S_n$ equals the term of $\sigma$ in the sum over shuffles:
>
> $$
> \operatorname{sgn}(\pi)\, \alpha\big(v^{\pi(1)}, \ldots\big)\, \beta\big(v^{\pi(k+1)}, \ldots\big) = \operatorname{sgn}(\sigma)\, \alpha\big(v^{\sigma(1)}, \ldots\big)\, \beta\big(v^{\sigma(k+1)}, \ldots\big) .
> $$
>
> By the uniqueness of the factorization, the permutations $\pi$ with a given shuffle $\sigma$ are the $\sigma \circ \rho$ with $\rho \in S_k \times S_l$, and there are $k!\, l!$ of them. So the sum over $S_n$ is $k!\, l!$ times the sum over $\mathrm{Sh}(k, l)$.
>
> (2) By Definitions [[§77 The Wedge Product#^def-77-2|§77.2]] and [[§77 The Wedge Product#^def-77-3|§77.3]], $(\alpha \otimes \beta)^\pi(v^1, \ldots, v^n) = \alpha\big(v^{\pi(1)}, \ldots, v^{\pi(k)}\big)\, \beta\big(v^{\pi(k+1)}, \ldots, v^{\pi(n)}\big)$, so the sum in (1) is $\sum_\pi \operatorname{sgn}(\pi)\, (\alpha \otimes \beta)^\pi = n!\, \mathcal{A}(\alpha \otimes \beta)$. Dividing by $k!\, l!$ gives (2).
>
> (3) $\mathcal{A}(\alpha \otimes \beta) \in \Lambda^n V^{\ast}$ by Lemma [[§77 The Wedge Product#^lem-77-1|§77.1]](1), and $\Lambda^n V^{\ast}$ is a vector space; so (3) follows from (2).

^pf-77-2

*Uses:* [[§76 Shuffles#^lem-76-1|§76.1]], [[§75 Multilinear Algebra#^lem-75-1|§75.1]], [[§11 Topological Groups and Classical Matrix Groups#^prop-11-2|§11.2]], [[§77 The Wedge Product#^def-77-2|Def. §77.2]], [[§77 The Wedge Product#^def-77-3|Def. §77.3]], [[§77 The Wedge Product#^lem-77-1|§77.1]]

> [!remark] Remark: Two Conventions for the Wedge Product
> The board of Lecture 29 wrote $\alpha \wedge \beta = \mathcal{A}(\alpha \otimes \beta)$: take the tensor product, then its skew-symmetric part. With $\mathcal{A}$ normalized as a projection (Lemma [[§77 The Wedge Product#^lem-77-1|§77.1]]), this holds up to the factor $\binom{k+l}{k}$ of Proposition [[§77 The Wedge Product#^prop-77-2|§77.2]](2). Lee defines the wedge product by the formula with the factor and calls this the *determinant convention*: the factor is what makes $\varepsilon^{a_1} \wedge \cdots \wedge \varepsilon^{a_k}$ equal to the determinant $\varepsilon^A$ with no factorials (Proposition [[§78 Properties of the Wedge Product#^prop-78-4|§78.4]](4)), and it is the convention of the shuffle formula of Definition [[§77 The Wedge Product#^def-77-1|§77.1]], which has no factorials at all. Some books, for example Kobayashi–Nomizu, define the product as $\mathcal{A}(\alpha \otimes \beta)$ without the factor (the *Alt convention*); their wedge product differs from this one by the constant $\binom{k+l}{k}$. Lecture 30 wrote the relation with its factor, $A(\alpha \otimes \beta) = \frac{k!\, l!}{(k+l)!}\, \alpha \wedge \beta$, which is Proposition [[§77 The Wedge Product#^prop-77-2|§77.2]](2).

^rem-77-1

> [!example] Example §77.1: The Wedge of Two One-Forms
> Let $k = l = 1$, so $\alpha, \beta \in V^{\ast}$. The group $S_2$ has two elements, the identity $(1, 2)$ and the transposition $(2, 1)$ in one-line notation, and both are shuffles: $\mathrm{Sh}(1, 1) = S_2$, because with $k = l = 1$ there are no two values to compare. The identity has sign $+1$ and the transposition $-1$, so
>
> $$
> (\alpha \wedge \beta)(v^1, v^2) = \alpha(v^1)\beta(v^2) - \alpha(v^2)\beta(v^1) = \det \begin{pmatrix} \alpha(v^1) & \alpha(v^2) \\ \beta(v^1) & \beta(v^2) \end{pmatrix} .
> $$
>
> *Lee: Ch. 14, The Wedge Product*

^ex-77-1

This is the formula of Lecture 28: for $\alpha = dx^i$ and $\beta = dx^j$ on $\mathbb{R}^3$ it gives $(dx^i \wedge dx^j)(u, v) = u^i v^j - u^j v^i$, which is Definition [[§74 The Integrand Is a Two-Form#^def-74-1|§74.1]]. So the two-form named $dx^i \wedge dx^j$ there is the wedge product of the one-forms $dx^i$ and $dx^j$. This case of the wedge product is the one used most often. The next case, $k = 1$ and $l = 2$, is Example [[§77 The Wedge Product#^ex-77-2|§77.2]].

![[m591-76-3.svg]]

*(Not from lecture; figure added.)* Example [[§77 The Wedge Product#^ex-77-1|§77.1]] as an area, for the covectors $\alpha(x) = 0.9\, x^1 + 0.3\, x^2$ and $\beta(x) = -0.35\, x^1 + 0.85\, x^2$ on $V = \mathbb{R}^2$. Left: the level lines $\alpha = 0, 1, 2, \ldots$ (blue) and $\beta = 0, 1, 2, \ldots$ (red) cut $V$ into cells; the cell $0 \le \alpha \le 1$, $0 \le \beta \le 1$ is shaded grey. Right: the linear map $v \mapsto (\alpha(v), \beta(v))$ sends the cells to the unit squares of the $(\alpha, \beta)$-plane, and the vectors $v^1, v^2$ to $(\alpha(v^1), \beta(v^1)) = (2, 0.5)$ and $(\alpha(v^2), \beta(v^2)) = (0.5, 1.5)$. The determinant $(\alpha \wedge \beta)(v^1, v^2) = 2 \cdot 1.5 - 0.5 \cdot 0.5 = 2.75$ is the signed area of the parallelogram on the right, which is the area of the parallelogram spanned by $v^1$ and $v^2$ on the left measured in cells of the grid (orange). Exchanging $v^1$ and $v^2$ reverses the orientation and the sign.

> [!example] Example §77.2: The Wedge of a One-Form and a Two-Form
> Let $\alpha \in V^{\ast}$ ($k = 1$) and $\beta \in \Lambda^2 V^{\ast}$ ($l = 2$). A $(1, 2)$-shuffle is determined by $\sigma(1)$, which can be any of $1, 2, 3$; the other two values then follow in increasing order. With their signs, the $(1, 2)$-shuffles are
>
> $$
> (1 \mid 2, 3)\ {+}, \qquad (2 \mid 1, 3)\ {-}, \qquad (3 \mid 1, 2)\ {+}
> $$
>
> (Example [[§76 Shuffles#^ex-76-2|§76.2]]): the second is a transposition, and the third has the two inversions formed by its first entry with the second and with the third. So Definition [[§77 The Wedge Product#^def-77-1|§77.1]] gives
>
> $$
> (\alpha \wedge \beta)(v^1, v^2, v^3) = \alpha(v^1)\,\beta(v^2, v^3) - \alpha(v^2)\,\beta(v^1, v^3) + \alpha(v^3)\,\beta(v^1, v^2) .
> $$
>
> Now let $\beta$ itself be a wedge product of two one-forms, $\beta = \gamma \wedge \delta$ with $\gamma, \delta \in V^{\ast}$. By Example [[§77 The Wedge Product#^ex-77-1|§77.1]], $\beta(v, w)$ is the $2 \times 2$ determinant with rows $(\gamma(v), \gamma(w))$ and $(\delta(v), \delta(w))$, and the three terms are the expansion of a $3 \times 3$ determinant along its top row:
>
> $$
> \big(\alpha \wedge (\gamma \wedge \delta)\big)(v^1, v^2, v^3) = \det \begin{pmatrix} \alpha(v^1) & \alpha(v^2) & \alpha(v^3) \\ \gamma(v^1) & \gamma(v^2) & \gamma(v^3) \\ \delta(v^1) & \delta(v^2) & \delta(v^3) \end{pmatrix} .
> $$
>
> Indeed, in that expansion the entry $\alpha(v^j)$ of the top row is multiplied by $(-1)^{1+j}$ and by the $2 \times 2$ minor left after deleting the top row and the $j$-th column, which is $\beta$ evaluated on the two vectors other than $v^j$. The general statement is Lemma [[§78 Properties of the Wedge Product#^lem-78-2|§78.2]].
>
> *Source: Lecture 30*

^ex-77-2

![[m591-76-5.svg]]

*(Not from lecture; figure added.)* Example [[§77 The Wedge Product#^ex-77-2|§77.2]] for $\beta = \gamma \wedge \delta$: the three terms of $(\alpha \wedge \beta)(v^1, v^2, v^3)$, one for each $(1, 2)$-shuffle, are the three terms of the expansion of the $3 \times 3$ determinant along its top row. The shuffle chooses the vector $v^{\sigma(1)}$ given to $\alpha$ (orange); the other two vectors, in increasing order, go to $\beta$, whose value is the complementary $2 \times 2$ minor (blue). The sign of the shuffle is the sign $(-1)^{1 + \sigma(1)}$ of the cofactor.

**Transcription note (Lecture 30).** The $3 \times 3$ determinant was first written with $\beta$ in the second and third rows, and corrected in class to the rows $\gamma$ and $\delta$.

> [!example] Example §77.3: The Wedge of Two Two-Forms
> Let $k = l = 2$. A $(2, 2)$-shuffle is determined by the two places $\sigma(1) < \sigma(2)$, so there are $\binom{4}{2} = 6$ of them (Lemma [[§76 Shuffles#^lem-76-1|§76.1]](2)); in one-line notation, with their signs, they are
>
> $$
> (1, 2, 3, 4)\ {+}, \quad (1, 3, 2, 4)\ {-}, \quad (1, 4, 2, 3)\ {+}, \quad (2, 3, 1, 4)\ {+}, \quad (2, 4, 1, 3)\ {-}, \quad (3, 4, 1, 2)\ {+} ,
> $$
>
> with $0, 1, 2, 2, 3, 4$ inversions. For $\alpha, \beta \in \Lambda^2 V^{\ast}$, Definition [[§77 The Wedge Product#^def-77-1|§77.1]] gives
>
> $$
> \begin{aligned}
> (\alpha \wedge \beta)(v^1, v^2, v^3, v^4) ={}& \alpha(v^1, v^2)\beta(v^3, v^4) - \alpha(v^1, v^3)\beta(v^2, v^4) + \alpha(v^1, v^4)\beta(v^2, v^3) \\
> &+ \alpha(v^2, v^3)\beta(v^1, v^4) - \alpha(v^2, v^4)\beta(v^1, v^3) + \alpha(v^3, v^4)\beta(v^1, v^2) .
> \end{aligned}
> $$
>
> *Source: not from lecture · filled in*

^ex-77-3

![[m591-76-2.svg]]

*(Not from lecture; figure added.)* The six $(2, 2)$-shuffles of Example [[§77 The Wedge Product#^ex-77-3|§77.3]]. In each diagram the top row is the entries $1, 2$ of $\alpha$ (red) and $3, 4$ of $\beta$ (blue), and the strand from $i$ ends at the vector $v^{\sigma(i)}$ that this entry receives. Strands of the same colour never cross, which is the shuffle condition. Each crossing of a red strand with a blue one (black dot) is an inversion of $\sigma$, so the sign of the term is $+$ for an even number of crossings (green) and $-$ for an odd number (red).
