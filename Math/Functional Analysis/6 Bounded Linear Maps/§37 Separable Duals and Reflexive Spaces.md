---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 37
tags: [functional-analysis, math556]
---
← [[§36 Duality in Normed Spaces]] · ↑ [[· 6 Bounded Linear Maps]] · [[§38 ℝⁿ, Cᵐ and Lᵖ]] →

*Stage: maps — Thread: functionals. The spanning criterion turns density into a statement about functionals; with it, separability passes from $X'$ to $X$, and the second dual $X''$ contains $X$.*

## The Spanning Criterion

> [!theorem] Theorem §37.1: Spanning Criterion
> Let $X$ be a normed linear space over $\mathbb{F}$ ($= \mathbb{R}$ or $\mathbb{C}$) and $\{y_i\}_{i \in \Lambda} \subset X$, with $\Lambda$ any index set. Then for every $z \in X$:
>
> $$
> z \in \overline{\operatorname{span}\{y_i\}_{i \in \Lambda}} \iff \bigl( \text{for all } \ell \in X' : \ \ell(y_i) = 0 \text{ for all } i \in \Lambda \implies \ell(z) = 0 \bigr) .
> $$

^thm-37-1

> [!proof]+ Proof
> **($\Rightarrow$)** Assume $z \in \overline{\operatorname{span}\{y_i\}}$. Let $\ell \in X'$ with $\ell(y_i) = 0$ for all $i \in \Lambda$; we want $\ell(z) = 0$. By linearity,
>
> $$
> \ell\Bigl( \sum_{j=1}^n a_j\, y_{i_j} \Bigr) = \sum_{j=1}^n a_j\, \ell(y_{i_j}) = 0
> $$
>
> for every finite linear combination $\sum_j a_j y_{i_j}$, and these make up $\operatorname{span}\{y_i\}$ (Proposition [[§1 Linear Spaces#^prop-1-5|§1.5]]). So $\ell(y) = 0$ for every $y \in \operatorname{span}\{y_i\}$. Now $z$ is in the closure, so there is a sequence $z_k \in \operatorname{span}\{y_i\}$ with $z_k \to z$ (Definition [[§11 Normed Linear Spaces#^def-11-7|§11.7]]). Since $\ell$ is bounded, hence continuous (Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]), $\ell(z_k) \to \ell(z)$; and $\ell(z_k) = 0$ for every $k$. Hence $\ell(z) = 0$.
>
> **($\Leftarrow$)** Assume that every $\ell \in X'$ with $\ell(y_i) = 0$ for all $i$ has $\ell(z) = 0$. Let $Y = \operatorname{span}\{y_i\}_{i \in \Lambda}$. A functional vanishes on all of $Y$ exactly when it vanishes on every $y_i$: one direction is the computation above, the other holds because each $y_i \in Y$. So the assumption says $\ell(z) = 0$ for every $\ell \in Y^\perp$, and by the distance formula (Theorem [[§36 Duality in Normed Spaces#^thm-36-6|§36.6]])
>
> $$
> \inf_{y \in Y} \|z - y\| = \max_{\substack{\ell \in X',\ \|\ell\| \le 1 \\ \ell(y) = 0\ \forall y \in Y}} |\ell(z)| = 0 .
> $$
>
> Since the infimum is $0$, for each $k$ there is $y_k \in Y$ with $\|z - y_k\| < 1/k$; so $y_k \to z$ and $z \in \overline{Y} = \overline{\operatorname{span}\{y_i\}}$.

^pf-37-1

*Uses:* [[§1 Linear Spaces#^prop-1-5|§1.5]], [[§11 Normed Linear Spaces#^def-11-7|Def. §11.7]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]], [[§36 Duality in Normed Spaces#^thm-36-6|§36.6]]

> [!theorem] Corollary §37.2: Two Forms of the Spanning Criterion
> Let $X$ be a normed linear space.
>
> 1. $\overline{\operatorname{span}\{y_i\}_{i \in \Lambda}} = X$ if and only if the only $\ell \in X'$ with $\ell(y_i) = 0$ for all $i$ is $\ell = 0$.
> 2. If $Y$ is a closed linear subspace of $X$, then $Y = \{ z \in X : \ell(z) = 0 \text{ for all } \ell \in Y^\perp \}$.

^cor-37-2

> [!proof]+ Proof
> (1) If only $\ell = 0$ vanishes on every $y_i$, then the condition of Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-1|§37.1]] holds for every $z \in X$, so every $z$ lies in the closed span. Conversely, if the closed span is $X$ and $\ell$ vanishes on every $y_i$, then $\ell(z) = 0$ for every $z \in X$ by Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-1|§37.1]], i.e. $\ell = 0$.
>
> (2) Apply Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-1|§37.1]] with the family $\{y\}_{y \in Y}$: its span is $Y$, whose closure is $Y$, and the functionals vanishing on all of it form $Y^\perp$.

^pf-37-2

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^thm-37-1|§37.1]]

> [!remark] Remark: Hilbert-Space Form
> In a Hilbert space, with $Y^\perp$ the orthogonal complement, (1) reads: a set has dense span if and only if only $0$ is orthogonal to it; and (2) is $(Y^\perp)^\perp = Y$ for closed $Y$ (Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-6|§25.6]], Lemma [[§25 Projection and Orthogonal Decomposition#^lem-25-5|§25.5]]). The spanning criterion is the normed-space version, with functionals in place of vectors.

^rem-37-1

![[m556-37-1.svg]]

The spanning criterion in a picture: a point $z$ outside the closed subspace $Y = \overline{\operatorname{span}\{y_i\}}$ (blue) is detected by a bounded functional $\ell$ that vanishes on $Y$ but not at $z$ (red level lines, parallel to $Y$). The criterion says this is the only way to be outside: if every $\ell$ that vanishes on all $y_i$ also vanishes at $z$, then $z \in Y$.

## Separability of the Dual

Recall that a normed linear space $X$ is **separable** if it has a countable dense subset ([[§28 Existence of Orthonormal Bases and Separability#^def-28-1|Definition §28.1]]). For $1 \le p < \infty$ the spaces $\ell^p$ and $L^p(E)$ are separable, and so is $c_0$ (Propositions [[§29 Sequence and Function Spaces#^prop-29-1|§29.1]], [[§29 Sequence and Function Spaces#^prop-29-4|§29.4]] and [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]); $\ell^\infty$ and $L^\infty(E)$, $m(E) > 0$, are not (Propositions [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]] and [[§29 Sequence and Function Spaces#^prop-29-5|§29.5]]).

> [!remark] Remark: Duals of the Sequence Spaces
> Recall $(\ell^p)' = \ell^{p'}$ for $1 \le p < \infty$, $\frac1p + \frac1{p'} = 1$, so that $1 < p' \le \infty$ (Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]]). In particular:
> - $(\ell^\infty)' \neq \ell^1$ (Example [[§36 Duality in Normed Spaces#^ex-36-2|§36.2]]);
> - $(c_0)' = \ell^1$, where $c_0 = \ell^\infty_0 = \{ (a_1, a_2, \ldots) : \lim_{n \to \infty} a_n = 0 \}$ with $\|a\| = \max_i |a_i| < \infty$ (homework; $c_0$ is the Banach space of Proposition [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]);
> - $(\ell^1)' = \ell^\infty$ (the case $p = 1$).
>
> The last example shows that a [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]] space can have a non-separable dual: $\ell^1$ is separable (Proposition [[§29 Sequence and Function Spaces#^prop-29-1|§29.1]]), but $\ell^\infty$ is not (Proposition [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]]). The other direction holds.

^rem-37-2

> [!theorem] Theorem §37.3: A Separable Dual Forces a Separable Space
> Let $X$ be a normed linear space. If $X'$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], then $X$ is separable.

^thm-37-3

> [!proof]+ Proof
> If $X = \{0\}$ there is nothing to prove, so assume $X \neq \{0\}$. Since $X'$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], there is a countable set $D = \{\ell_j\}_{j=1}^\infty \subset X'$ that is dense in $X'$. For each $j$ take $z_j \in X$ with
>
> $$
> \|z_j\| = 1 \qquad \text{and} \qquad |\ell_j(z_j)| \ge \tfrac12 \|\ell_j\| .
> $$
>
> (This is possible because $\|\ell_j\| = \sup_{\|z\| = 1} |\ell_j(z)|$: if $\ell_j = 0$ any unit vector will do; if $\ell_j \neq 0$, then $\frac12 \|\ell_j\| < \|\ell_j\|$ is not an upper bound of $\{|\ell_j(z)| : \|z\| = 1\}$.) The set $\{z_j\}$ is countable.
>
> **Step 1: $\overline{\operatorname{span}\{z_j\}_{j=1}^\infty} = X$.** By Corollary [[§37 Separable Duals and Reflexive Spaces#^cor-37-2|§37.2]](1) it suffices to show: if $\ell \in X'$ and $\ell(z_j) = 0$ for all $j = 1, 2, \ldots$, then $\ell = 0$ in $X'$. Let $\ell$ be such a functional. Since $D$ is dense in $X'$, there is a sequence $\{\ell_{j_k}\}_{k=1}^\infty \subset D$ with $\|\ell_{j_k} - \ell\| \to 0$ as $k \to \infty$. Using $\ell(z_{j_k}) = 0$ and $\|z_{j_k}\| = 1$,
>
> $$
> \tfrac12 \|\ell_{j_k}\| \le |\ell_{j_k}(z_{j_k})| = |(\ell_{j_k} - \ell)(z_{j_k})| \le \|\ell_{j_k} - \ell\|\, \|z_{j_k}\| = \|\ell_{j_k} - \ell\| \xrightarrow[k \to \infty]{} 0 .
> $$
>
> So $\|\ell_{j_k}\| \to 0$, i.e. $\ell_{j_k} \to 0$ in $X'$.
> Since also $\ell_{j_k} \to \ell$ and limits are unique ($\|\ell\| \le \|\ell - \ell_{j_k}\| + \|\ell_{j_k}\| \to 0$), $\ell = 0$.
>
> **Step 2: a countable dense set.** Let $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q}$ if $\mathbb{F} = \mathbb{R}$ and $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q} + i\mathbb{Q}$ if $\mathbb{F} = \mathbb{C}$, and
>
> $$
> D_1 = \Bigl\{ \sum_{j=1}^n a_j z_j : a_j \in \mathbb{Q}_{\mathbb{F}},\ n \in \mathbb{N} \Bigr\} .
> $$
>
> $D_1$ is countable and $\overline{D_1} = \overline{\operatorname{span}\{z_j\}} = X$.
> *Countable:* for fixed $n$, $D_1$'s elements with $n$ terms are the image of $\mathbb{Q}_{\mathbb{F}}^n$, a countable set, and a countable union of countable sets is countable. *Dense:* let $x \in X$ and $\varepsilon > 0$. By Step 1 there is $y = \sum_{j=1}^n c_j z_j$ in the span with $\|x - y\| < \varepsilon$. Choose $a_j \in \mathbb{Q}_{\mathbb{F}}$ with $|c_j - a_j| < \varepsilon/n$ ($\mathbb{Q}_{\mathbb{F}}$ is dense in $\mathbb{F}$). Then $d = \sum_{j=1}^n a_j z_j \in D_1$ and, since $\|z_j\| = 1$,
>
> $$
> \|x - d\| \le \|x - y\| + \sum_{j=1}^n |c_j - a_j|\, \|z_j\| < 2\varepsilon .
> $$
>
> So $D_1$ is a countable dense subset of $X$, and $X$ is separable.

^pf-37-3

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^cor-37-2|§37.2]]

> [!remark] Remark: The Converse Fails
> The converse is false: $\ell^1$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], while $(\ell^1)' = \ell^\infty$ is not. “Dual separable $\Rightarrow$ separable”, not conversely.

^rem-37-3

> [!theorem] Corollary §37.4: The Duals of $\ell^\infty$ and $L^\infty$
> $(\ell^\infty)'$ is not [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], and neither is $(L^\infty(E))'$ for $E \subset \mathbb{R}^n$ measurable with $m(E) > 0$. In particular $(\ell^\infty)' \neq \ell^1$ and $(L^\infty)' \neq L^1$.

^cor-37-4

> [!proof]+ Proof
> If $(\ell^\infty)'$ were [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]] would make $\ell^\infty$ separable, contradicting Proposition [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]]. Likewise for $L^\infty(E)$, by Proposition [[§29 Sequence and Function Spaces#^prop-29-5|§29.5]].
> Now $\ell^1$ and $L^1(E)$ are separable (Propositions [[§29 Sequence and Function Spaces#^prop-29-1|§29.1]] and [[§29 Sequence and Function Spaces#^prop-29-4|§29.4]]), and separability is preserved by an isometric isomorphism $T$ (indeed by any linear bijection with $T$ and $T^{-1}$ bounded): if $D$ is countable and dense in $\ell^1$ and $\|x - d_n\| \to 0$ with $d_n \in D$, then $\|Tx - Td_n\| \le \|T\|\,\|x - d_n\| \to 0$, so $T(D)$ is countable and dense. Hence $(\ell^\infty)'$ is not isometrically isomorphic to $\ell^1$, nor $(L^\infty)'$ to $L^1$.

^pf-37-4

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]], [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]], [[§29 Sequence and Function Spaces#^prop-29-5|§29.5]], [[§29 Sequence and Function Spaces#^prop-29-1|§29.1]], [[§29 Sequence and Function Spaces#^prop-29-4|§29.4]]

> [!remark] Remark: Every Identification is Ruled Out
> This is stronger than Example [[§36 Duality in Normed Spaces#^ex-36-2|§36.2]], which only showed that the particular map $a \mapsto \ell_a$, $\ell^1 \to (\ell^\infty)'$, is not onto. The corollary rules out *every* identification of $(\ell^\infty)'$ with $\ell^1$ as normed spaces, by a property ([[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separability]]) that any such identification would preserve.

^rem-37-4

## The Second Dual and Reflexive Spaces

Let $X$ be a normed linear space. Then $X'$ is a Banach space (Corollary [[§31 Dual Spaces#^cor-31-1|§31.1]]), and applying the same fact to $X'$, so is its dual

$$
X'' = (X')' ,
$$

the **second dual** of $X$. Every $x_0 \in X$ gives an element of $X''$ by evaluation.

> [!theorem] Proposition §37.5: The Canonical Embedding $X \to X''$
> Let $X$ be a normed linear space and $x_0 \in X$. Then
>
> $$
> \eta(\ell) = \ell(x_0), \qquad \ell \in X',
> $$
>
> defines $\eta \in X''$ with $\|\eta\| = \|x_0\|$. The map $i : X \to X''$, $i(x_0) = \eta$, that is,
>
> $$
> i(x_0)(\ell) = \ell(x_0) \qquad \text{for all } \ell \in X',
> $$
>
> is linear and an isometry, $\|i(x_0)\| = \|x_0\|$: $i$ is an **isometric embedding** of $X$ into $X''$.

^prop-37-5

> [!proof]+ Proof
> $\eta$ is linear in $\ell$: $\eta(c_1 \ell_1 + c_2 \ell_2) = (c_1 \ell_1 + c_2 \ell_2)(x_0) = c_1 \ell_1(x_0) + c_2 \ell_2(x_0) = c_1 \eta(\ell_1) + c_2 \eta(\ell_2)$. It is bounded, since $|\eta(\ell)| = |\ell(x_0)| \le \|\ell\|\, \|x_0\|$. Hence $\eta \in (X')' = X''$, and by Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]
>
> $$
> \|\eta\| = \sup_{\ell \in X',\ \|\ell\| = 1} |\ell(x_0)| = \|x_0\| .
> $$
>
> (If $X = \{0\}$ then $X' = \{0\}$ and both sides are $0$.) $i$ is linear: for every $\ell \in X'$, $i(ax + by)(\ell) = \ell(ax + by) = a\,\ell(x) + b\,\ell(y) = \bigl( a\, i(x) + b\, i(y) \bigr)(\ell)$. Being linear and norm-preserving, $i$ preserves distances, $\|i(x) - i(y)\| = \|i(x - y)\| = \|x - y\|$, and in particular is one-to-one; so $i$ identifies $X$ with the subspace $i(X)$ of $X''$, norms included.

^pf-37-5

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]

> [!example] Example §37.1: Hilbert Space: $\langle x, \ell \rangle$ from Both Sides
> Let $X = H$ be a Hilbert space. Each $\ell \in H'$ is $\ell(x) = (x, a) = \langle x, \ell \rangle$ for some $a \in H$, with $\|\ell\| = \|a\|$ (Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]]). For $x_0 \in H$, $i(x_0)$ is the functional $\ell \mapsto \ell(x_0) = \langle x_0, \ell \rangle$ on $H'$: in the pairing $\langle x, \ell \rangle$, fixing $\ell$ gives an element of $X'$, and fixing $x$ gives an element of $X''$.

^ex-37-1

> [!definition] Definition §37.1: Reflexive Space
> Let $X$ be a normed linear space and $i : X \to X''$ the map with $i(x_0)(\ell) = \ell(x_0)$ for all $\ell \in X'$. If $i$ is onto, $X$ is called **reflexive** (a **reflexive Banach space**); one writes $X = X''$.

^def-37-1

> [!theorem] Proposition §37.6: A Reflexive Space is a Banach Space
> If $X$ is reflexive, then $X$ is complete.

^prop-37-6

> [!proof]+ Proof
> *(Stated in lecture without proof; filled in.)* Let $\{x_n\}$ be Cauchy in $X$. Since $i$ is an isometry, $\|i(x_n) - i(x_m)\| = \|x_n - x_m\|$, so $\{i(x_n)\}$ is Cauchy in $X''$, which is a Banach space; let $\eta = \lim_n i(x_n)$. As $i$ is onto, $\eta = i(x)$ for some $x \in X$, and $\|x_n - x\| = \|i(x_n) - i(x)\| \to 0$.

^pf-37-6

> [!example] Example §37.2: Hilbert Spaces are Reflexive
> Let $H$ be a Hilbert space. Then $H$ is reflexive: $H' = H$ and $(H')' = H$.

^ex-37-2

> [!proof]+ Proof
> The two identifications must be combined so that the result is the map $i$ of Definition [[§37 Separable Duals and Reflexive Spaces#^def-37-1|§37.1]]. Let $\eta \in H''$. For $a \in H$ let $\ell_a = (\,\cdot\,, a) \in H'$ and put
>
> $$
> \varphi(a) = \overline{\eta(\ell_a)}, \qquad a \in H .
> $$
>
> Since $\ell_{a + b} = \ell_a + \ell_b$ and $\ell_{ca} = \bar c\, \ell_a$ (Corollary [[§31 Dual Spaces#^cor-31-3|§31.3]]), $\varphi(a + b) = \varphi(a) + \varphi(b)$ and $\varphi(ca) = \overline{\bar c\, \eta(\ell_a)} = c\, \varphi(a)$: $\varphi$ is linear. It is bounded, $|\varphi(a)| \le \|\eta\|\, \|\ell_a\| = \|\eta\|\, \|a\|$. By the Riesz representation theorem there is $x \in H$ with $\varphi(a) = (a, x)$ for all $a$. Hence
>
> $$
> \eta(\ell_a) = \overline{(a, x)} = (x, a) = \ell_a(x) = i(x)(\ell_a) .
> $$
>
> Every $\ell \in H'$ is some $\ell_a$ (Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]]), so $\eta = i(x)$, and $i$ is onto.

^pf-ex-37-2

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^def-37-1|Def. §37.1]], [[§31 Dual Spaces#^cor-31-3|§31.3]], [[§31 Dual Spaces#^thm-31-2|§31.2]]

> [!example] Example §37.3: $\ell^p$ is Reflexive for $1 < p < \infty$
> Let $1 < p < \infty$. Since $(\ell^p)' = \ell^{p'}$ with $1 < p' < \infty$ as well,
>
> $$
> (\ell^p)'' = (\ell^{p'})' = \ell^p ,
> $$
>
> so $\ell^p$ is reflexive for all $1 < p < \infty$. By contrast, $(\ell^1)' = \ell^\infty$ but $(\ell^\infty)' \neq \ell^1$.

^ex-37-3

> [!proof]+ Proof
> Let $\eta \in (\ell^p)''$. By Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], every element of $(\ell^p)'$ is $\ell_b(x) = \sum_j x_j \overline{b_j}$ for a unique $b \in \ell^{p'}$, with $\ell_{b + b'} = \ell_b + \ell_{b'}$, $\ell_{cb} = \bar c\, \ell_b$ and $\|\ell_b\| = \|b\|_{p'}$. Put $\varphi(b) = \overline{\eta(\ell_b)}$ for $b \in \ell^{p'}$. As in Example [[§37 Separable Duals and Reflexive Spaces#^ex-37-2|§37.2]], $\varphi$ is linear and $|\varphi(b)| \le \|\eta\|\, \|b\|_{p'}$, so $\varphi \in (\ell^{p'})'$. Since $1 < p' < \infty$ and the conjugate exponent of $p'$ is $p$, Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]] applied to $\ell^{p'}$ gives $x \in \ell^p$ with $\varphi(b) = \sum_j b_j \overline{x_j}$ for all $b$. Hence
>
> $$
> \eta(\ell_b) = \overline{\varphi(b)} = \sum_j x_j\, \overline{b_j} = \ell_b(x) = i(x)(\ell_b)
> $$
>
> for every $b$, i.e. $\eta = i(x)$.

^pf-ex-37-3

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], [[§37 Separable Duals and Reflexive Spaces#^ex-37-2|Ex. §37.2]]

> [!remark] Remark: Why the Check is Needed
> Reflexivity asks that the *specific* map $i$ be onto, not merely that $X''$ be isometrically isomorphic to $X$ in some way. The two differ: there are Banach spaces (James' space) isometrically isomorphic to their second dual that are not reflexive. That is why the two examples above compose the identifications explicitly and check that the result is $i$.

^rem-37-5

> [!example] Example §37.4: $C[0,1]$ is Not Reflexive
> $(C[0,1], \|\cdot\|_\infty)$ is not reflexive.

^ex-37-4

> [!proof]+ Proof
> Suppose it is: $\bigl( (C[0,1])' \bigr)' = C[0,1]$. Now $C[0,1]$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], because the polynomials with rational coefficients are dense.
> (By the Weierstrass approximation theorem, for $f \in C[0,1]$ and $\varepsilon > 0$ there is a polynomial $P(x) = \sum_{k=0}^n c_k x^k$ with $\|f - P\|_\infty < \varepsilon$; choosing $q_k \in \mathbb{Q}_{\mathbb{F}}$ with $|c_k - q_k| < \varepsilon/(n+1)$ and using $|x^k| \le 1$ on $[0,1]$, $Q = \sum q_k x^k$ has $\|P - Q\|_\infty < \varepsilon$. The polynomials with coefficients in $\mathbb{Q}_{\mathbb{F}}$ form a countable set, as in Step 2 above.) Then $(C[0,1])'$ would be separable: its dual $((C[0,1])')'$ is $i(C[0,1])$, isometrically isomorphic to $C[0,1]$ and hence separable (as in the proof of Corollary [[§37 Separable Duals and Reflexive Spaces#^cor-37-4|§37.4]]), and Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]], applied to the normed space $X = (C[0,1])'$, gives that $X$ is separable.
>
> This is not true. For $s \in [0,1]$ define $\ell_s(f) = f(s)$ for $f \in C[0,1]$. Then $\ell_s : C[0,1] \to \mathbb{R}$ is linear, and
>
> $$
> |\ell_s(f)| = |f(s)| \le \max_{x \in [0,1]} |f(x)| = \|f\|_\infty ,
> $$
>
> so $\|\ell_s\| \le 1$ and $\ell_s \in (C[0,1])'$. For $s, t \in [0,1]$, $(\ell_s - \ell_t)(f) = f(s) - f(t)$, and for $s \neq t$
>
> $$
> \|\ell_s - \ell_t\| = \sup_{\substack{f \in C[0,1] \\ \|f\|_\infty \le 1}} |(\ell_s - \ell_t)(f)| = \sup_{\substack{f \in C[0,1] \\ \|f\|_\infty \le 1}} |f(s) - f(t)| = 2 .
> $$
>
> ($\le 2$ because $|f(s) - f(t)| \le |f(s)| + |f(t)|$; and the continuous $f$ that is linear from $f(s) = 1$ to $f(t) = -1$ between $s$ and $t$ and constant outside has $\|f\|_\infty = 1$ and $f(s) - f(t) = 2$.) The family $\{\ell_s\}_{s \in [0,1]}$ is not countable, and its members are at mutual distance $2$, so $(C[0,1])'$ is not separable (as in Proposition [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]]: balls of radius $1$ about the $\ell_s$ are disjoint, and a dense set would need a point in each). This contradiction shows that $C[0,1]$ is not reflexive.

^pf-ex-37-4

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^cor-37-4|§37.4]], [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]], [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]]

![[m556-37-2.svg]]

Why $\|\ell_s - \ell_t\| = 2$: the function $f$ (blue) has $\|f\|_\infty = 1$, equals $1$ up to $s$ and $-1$ from $t$ on, so $(\ell_s - \ell_t)(f) = f(s) - f(t) = 2$ (red). However close $s$ and $t$ are, $f$ can drop from $1$ to $-1$ between them, so the uncountably many point evaluations stay at mutual distance $2$.

> [!theorem] Corollary §37.7: Separability of $X$ and $X'$ for Reflexive $X$
> Let $X$ be reflexive. Then $X$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]] if and only if $X'$ is separable. In particular $\ell^1$ is not reflexive.

^cor-37-7

> [!proof]+ Proof
> If $X'$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]], so is $X$ (Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]]; reflexivity is not needed). If $X$ is separable, then $X'' = i(X)$ is separable, being isometrically isomorphic to $X$, and Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]] applied to the normed space $X'$ shows that $X'$ is separable. For $\ell^1$: it is separable, but its dual is isometrically isomorphic to $\ell^\infty$ (Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], with the bar-free pairing of the remark after it), which is not separable; so $\ell^1$ is not reflexive. The proof of Example [[§37 Separable Duals and Reflexive Spaces#^ex-37-4|§37.4]] is this argument for $X = C[0,1]$. A variant shows that $c_0$ is not reflexive: if it were, $c_0'' = i(c_0)$ would be separable like $c_0$ (Proposition [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]), while $c_0'' \cong (\ell^1)' \cong \ell^\infty$ is not (Proposition [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]]). Here the corollary itself gives nothing, since $c_0$ and $c_0' \cong \ell^1$ are both separable.

^pf-37-7

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]], [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], [[§37 Separable Duals and Reflexive Spaces#^ex-37-4|Ex. §37.4]], [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]], [[§29 Sequence and Function Spaces#^prop-29-3|§29.3]]

![[m556-37-3.svg]]

[[§28 Existence of Orthonormal Bases and Separability#^def-28-1|Separability]] along the chain $X \to X' \to X''$ (green: separable; red: not). By Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-3|§37.3]] a green box can only have green boxes to its left, so once red appears it stays red. A reflexive space has $X'' = i(X)$, so its first and last boxes have the same colour; the rows for $c_0$ and $\ell^1$ end in red after starting in green, so neither is reflexive. ($c_0' = \ell^1$ is the homework statement of [[§37 Separable Duals and Reflexive Spaces#^rem-37-2|Remark: Duals of the Sequence Spaces]].)

## Closed Subspaces of Reflexive Spaces

> [!theorem] Theorem §37.8: Closed Subspaces of Reflexive Spaces are Reflexive
> Let $X$ be a reflexive Banach space and $Y$ a closed linear subspace of $X$. Then $Y$ is reflexive.

^thm-37-8

> [!proof]+ Proof
> Assume $X = X''$; we want $Y = Y''$. That is, we want: for every $\eta_0 \in (Y')'$ there is $y_0 \in Y$ with
>
> $$
> \eta_0(\ell_0) = \ell_0(y_0) \qquad \text{for all } \ell_0 \in Y' ,
> $$
>
> in the pairing notation $\langle \ell_0, \eta_0 \rangle = \langle y_0, \ell_0 \rangle$.
>
> **Restriction.** For every $\ell \in X'$ define $R(\ell)$ by
>
> $$
> R(\ell)(y) = \ell(y) \qquad \text{for all } y \in Y ,
> $$
>
> the restriction of $\ell$ to $Y$. Then $|R(\ell)(y)| \le \|\ell\|\, \|y\|$, so $R(\ell) \in Y'$ with $\|R(\ell)\| \le \|\ell\|$, and $R : X' \to Y'$.
> $R$ is linear, since $(c_1 \ell_1 + c_2 \ell_2)|_Y = c_1\, \ell_1|_Y + c_2\, \ell_2|_Y$. (Here $R$ is the restriction map, not the Riesz map of Corollary [[§31 Dual Spaces#^cor-31-3|§31.3]].)
>
> Let $\eta_0 : Y' \to \mathbb{F}$ be a bounded linear functional. Then $\eta_0 \circ R : X' \to \mathbb{F}$ is linear, and for $\ell \in X'$
>
> $$
> |\eta_0 \circ R(\ell)| = |\eta_0(R(\ell))| \le \|\eta_0\|\, \|R(\ell)\| \le \|\eta_0\|\, \|\ell\| ,
> $$
>
> so $\eta_0 \circ R \in X''$. Since $X'' = X$, there is $x_0 \in X$ with
>
> $$
> \eta_0 \circ R(\ell) = \ell(x_0) \qquad \text{for all } \ell \in X' .
> $$
>
> **Step 1: $x_0 \in Y$.** Since $Y$ is a closed linear subspace, by Corollary [[§37 Separable Duals and Reflexive Spaces#^cor-37-2|§37.2]](2) it suffices to show that $\ell(x_0) = 0$ for every $\ell \in Y^\perp$. Take $\ell \in Y^\perp$. Then $R(\ell) = 0$, since $R(\ell)(y) = \ell(y) = 0$ for all $y \in Y$. Hence
>
> $$
> \ell(x_0) = \eta_0 \circ R(\ell) = \eta_0(R(\ell)) = \eta_0(0) = 0 ,
> $$
>
> and so $x_0 \in Y$.
>
> **Step 2: $\eta_0(\ell_0) = \ell_0(x_0)$ for $\ell_0 \in Y'$.** Let $\ell_0 \in Y'$. By Hahn–Banach (Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]) there is an extension of $\ell_0$ to $X$; call it $\ell$: $\ell \in X'$ and $\ell(y) = \ell_0(y)$ for all $y \in Y$. That says $R(\ell) = \ell_0$. Therefore, using $x_0 \in Y$ from Step 1,
>
> $$
> \eta_0(\ell_0) = \eta_0(R(\ell)) = \ell(x_0) = \ell_0(x_0) .
> $$
>
> So $y_0 = x_0$ works, and $Y$ is reflexive.

^pf-37-8

*Uses:* [[§31 Dual Spaces#^cor-31-3|§31.3]], [[§37 Separable Duals and Reflexive Spaces#^cor-37-2|§37.2]], [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]

![[m556-37-4.svg]]

The proof in one diagram: $\eta_0 \in Y''$ is pulled back along the restriction $R$ to an element of $X''$, which reflexivity of $X$ represents by some $x_0$; functionals vanishing on $Y$ die under $R$, which puts $x_0$ in $Y$ (Step 1), and Hahn–Banach makes $R$ onto, so $x_0$ represents $\eta_0$ on all of $Y'$ (Step 2).

## Distance in the Dual

The distance formula (Theorem [[§36 Duality in Normed Spaces#^thm-36-6|§36.6]]) computes the distance from a vector to a subspace $Y$ by functionals in $Y^\perp$. The dual statement computes the distance from a functional to $Y^\perp$ by vectors in $Y$.

> [!theorem] Proposition §37.9: Distance from a Functional to $Y^\perp$
> Let $X$ be a normed linear space and $Y$ a linear subspace. Then for every $\ell \in X'$,
>
> $$
> \min_{m \in Y^\perp} \|\ell - m\| = \sup_{\substack{z \in Y \\ \|z\| = 1}} |\ell(z)| ,
> $$
>
> the norm of the restriction $\ell|_Y \in Y'$. Compare $\displaystyle \inf_{y \in Y} \|z - y\| = \max_{\substack{\ell \in Y^\perp \\ \|\ell\| \le 1}} |\ell(z)|$: now the minimum is attained on the side of the dual.

^prop-37-9

> [!proof]+ Proof
> (If $Y = \{0\}$, read the right side as $\|\ell|_Y\|_Y = 0$; then $Y^\perp = X'$ and $m = \ell$ gives $0$. Assume $Y \neq \{0\}$.)
>
> **Step 1: $\sup \le \inf$.** Let $\ell \in X'$ and $z \in Y$. For every $m \in Y^\perp$, $m(z) = 0$, so
>
> $$
> \ell(z) = (\ell - m)(z), \qquad |\ell(z)| \le \|\ell - m\|\, \|z\| .
> $$
>
> Hence $\sup_{z \in Y,\ \|z\| = 1} |\ell(z)| \le \|\ell - m\|$ for all $m \in Y^\perp$, and so
>
> $$
> \sup_{\substack{z \in Y \\ \|z\| = 1}} |\ell(z)| \le \inf_{m \in Y^\perp} \|\ell - m\| .
> $$
>
> **Step 2: an $m_0 \in Y^\perp$ attaining it.** We want $m_0 \in Y^\perp$ with $\|\ell - m_0\| = \sup_{z \in Y,\ \|z\| = 1} |\ell(z)|$. Consider $\ell_0 = \ell|_Y : Y \to \mathbb{F}$. Then $\ell_0 \in Y'$ and
>
> $$
> \sup_{\substack{z \in Y \\ \|z\| = 1}} |\ell_0(z)| = \|\ell_0\|_Y .
> $$
>
> By Hahn–Banach (Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]) there is an extension of $\ell_0$ to $\ell_1 \in X'$ with $\|\ell_1\| = \|\ell_0\|_Y$. Take $\ell - m_0 = \ell_1$, i.e. $m_0 = \ell - \ell_1$.
> Then $m_0 \in Y^\perp$, since $m_0(y) = \ell(y) - \ell_1(y) = \ell_0(y) - \ell_0(y) = 0$ for $y \in Y$, and
>
> $$
> \|\ell - m_0\| = \|\ell_1\| = \|\ell_0\|_Y = \sup_{\substack{z \in Y \\ \|z\| = 1}} |\ell(z)| .
> $$
>
> With Step 1, the infimum equals the supremum and is attained at $m_0$.

^pf-37-9

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]

![[m556-37-5.svg]]

The distance from $\ell$ to $Y^\perp$, drawn in $X'$: the smallest ball about $\ell$ (red, drawn square as for a maximum norm) that meets $Y^\perp$ (blue) has radius $\|\ell|_Y\|_Y$, and it does meet $Y^\perp$, so the minimum is attained. The points of contact (orange) are exactly the $m_0 = \ell - \ell_1$ with $\ell_1$ a norm-preserving extension of $\ell|_Y$; extensions need not be unique, and neither need the closest point, unlike the projection in a Hilbert space.

> [!remark] Remark: $Y' \cong X'/Y^\perp$
> $Y^\perp$ is a closed subspace of $X'$ (Proposition [[§36 Duality in Normed Spaces#^prop-36-7|§36.7]]), so $X'/Y^\perp$ carries the quotient norm $\|[\ell]\| = \inf_{m \in Y^\perp} \|\ell - m\|$ (Theorem [[§14 New Normed Spaces from Old#^thm-14-8|§14.8]]). The proposition says $\|[\ell]\| = \|\ell|_Y\|_Y$. Two functionals have the same restriction to $Y$ exactly when they differ by an element of $Y^\perp$, so $[\ell] \mapsto \ell|_Y$ is a well-defined, linear, norm-preserving map $X'/Y^\perp \to Y'$, and it is onto by Hahn–Banach. Hence $Y'$ is isometrically isomorphic to $X'/Y^\perp$: the dual of a subspace is a quotient of the dual, just as the dual of a quotient is a subspace of the dual (Theorem [[§36 Duality in Normed Spaces#^thm-36-8|§36.8]]).

^rem-37-6
