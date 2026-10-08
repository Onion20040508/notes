---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 28
tags: [functional-analysis, math556]
---
← [[§27 Orthonormal Sets and Bases]] · ↑ [[· 5 Inner Product Spaces]] · [[§29 Sequence and Function Spaces]] →

*Stage: inner products — Thread: dimension. Every Hilbert space has an orthonormal basis; the countable ones are exactly the bases of separable spaces.*

Both examples of [[§27 Orthonormal Sets and Bases|§27]] (Example [[§27 Orthonormal Sets and Bases#^ex-27-1|§27.1]] and Theorem [[§27 Orthonormal Sets and Bases#^thm-27-11|§27.11]]) have *countable* orthonormal bases. Wu announced for next lecture that every Hilbert space has an orthonormal basis — which by itself is “almost useless, because there are too many” — and, more usefully, that the countable ones are exactly the bases of separable spaces.

> [!remark] Remark: The Idea: Keep Adding Orthogonal Directions
> Wu first described the construction informally. Assume $H \neq \{0\}$ and take $e_1 \in H$ with $\|e_1\| = 1$. If $H = \operatorname{span}\{e_1\}$, then $\{e_1\}$ is an orthonormal basis. If not, take $y_2 \in H$ with $y_2 \notin \operatorname{span}\{e_1\}$ and remove its component along $e_1$:
>
> $$
> x_2 = y_2 - (y_2, e_1)\, e_1, \qquad (x_2, e_1) = (y_2, e_1) - (y_2, e_1)(e_1, e_1) = 0,
> $$
>
> so $x_2 \perp e_1$; put $e_2 = x_2 / \|x_2\|$. If $H = \operatorname{span}\{e_1, e_2\}$ we are done; if not, take $y_3 \notin \operatorname{span}\{e_1, e_2\}$ and continue.
>
> ![[m556-20-2.svg]]
> *The first step: $y_2$ minus its component $(y_2, e_1)\,e_1$ along $e_1$ leaves $x_2 \perp e_1$, and normalizing gives $e_2$.*
>
> The step-by-step description looks countable, but it need not be: an orthonormal basis $\{e_\alpha\}_{\alpha \in \Lambda}$ need not be countable. The precise argument is [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|Zorn's lemma]], which says “keep adding until nothing more can be added” without any enumeration.

^rem-28-1

> [!theorem] Theorem §28.1: Existence of Orthonormal Bases
> Every Hilbert space $H$ has an orthonormal basis.
>
> *Lax: §6.4, Thm 9*

^thm-28-1

> [!proof]+ Proof
> If $H = \{0\}$, the empty set is an orthonormal basis: it is complete, since every $x \in H$ is $0$. Assume $H \neq \{0\}$.
>
> **Step 1: the partially ordered set.** Let $S$ be the set of all orthonormal sets in $H$, partially ordered by inclusion: for $O_1, O_2 \in S$, $O_1 \prec O_2$ if $O_1 \subset O_2$. Two orthonormal sets need not be comparable. $S \neq \varnothing$: for any $x \neq 0$, $\{x/\|x\|\} \in S$.
>
> **Step 2: every chain has an upper bound.** Let $C = \{O_\beta\}_{\beta \in I}$ be a chain in $S$ (if $C$ is empty, any element of $S$ is an upper bound), and let $U = \bigcup_{\beta \in I} O_\beta$. Then $U \in S$: each $u \in U$ lies in some $O_\beta$, so $\|u\| = 1$; and if $u \neq v$ in $U$, say $u \in O_{\beta_1}$ and $v \in O_{\beta_2}$, then since $C$ is a chain one of $O_{\beta_1}, O_{\beta_2}$ contains the other, so $u$ and $v$ lie in a single orthonormal set and $(u, v) = 0$. Since $O_\beta \subset U$ for every $\beta$, $U$ is an upper bound of $C$.
>
> **Step 3: a maximal orthonormal set.** By Zorn's lemma (Theorem [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|§6.2]]), $S$ has a maximal element $O = \{e_\alpha\}_{\alpha \in \Lambda}$.
>
> **Step 4: $O$ is complete.** Suppose not. Then there is $x \in H$, $x \neq 0$, with $(x, e_\alpha) = 0$ for all $\alpha \in \Lambda$. Put $e = x/\|x\|$. Then $\|e\| = 1$ and $(e, e_\alpha) = 0$ for every $\alpha$; in particular $e \notin O$, since $(e, e) = 1 \neq 0$. So $O \cup \{e\}$ is an orthonormal set strictly containing $O$, contradicting the maximality of $O$. Hence $O$ is complete, and by Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]] it is an orthonormal basis.

^pf-28-1

*Uses:* [[§27 Orthonormal Sets and Bases#^def-27-1|Def. §27.1]], [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|§6.2]], [[§27 Orthonormal Sets and Bases#^def-27-2|Def. §27.2]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]

> [!remark]- Connections
> - Finite-dimensional home, where Gram–Schmidt suffices: [[§21 Orthonormal Bases#^ladr-6-35|LADR 6.35]].
> - Computational version: [[§53 The Gram–Schmidt Process#^cor-53-2|235 Cor. §53.2]] (every nonzero subspace of ℝⁿ has an orthonormal basis, by Gram–Schmidt).

> [!definition] Definition §28.1: Separable Space
> A normed linear space $X$ is **separable** if it has a countable dense subset: a countable $D \subset X$ such that every $x \in X$ is a limit of a sequence in $D$. Completeness is not required.
>
> *Lax: §5.1, definition of separable space*

^def-28-1

> [!remark]- Connections
> - Same definition for metric spaces: [[§35 Lᵖ as a Banach Space#^def-35-5|551 Def. §35.5]]; for topological spaces: [[§22 Countability Axioms#^def-22-5|590 Def. §22.5]].

## Countable Orthonormal Bases

> [!theorem] Lemma §28.2: Gram–Schmidt
> Let $y_1, y_2, \ldots$ be a finite or infinite sequence of linearly independent vectors in an inner product space $X$. Then there is an orthonormal sequence $e_1, e_2, \ldots$ (of the same length) with
>
> $$
> \operatorname{span}\{y_1, \ldots, y_j\} = \operatorname{span}\{e_1, \ldots, e_j\} \qquad \text{for every } j.
> $$
>
> *Lax: §6.4, Thm $9'$*

^lem-28-2

> [!proof]+ Proof
> Define recursively
>
> $$
> e_1 = \frac{y_1}{\|y_1\|}, \qquad x_j = y_j - \sum_{i=1}^{j-1} (y_j, e_i)\, e_i, \qquad e_j = \frac{x_j}{\|x_j\|} \quad (j \ge 2),
> $$
>
> exactly as in the informal construction in [[§28 Existence of Orthonormal Bases and Separability#^rem-28-1|the remark before Theorem §28.1]]: subtract from $y_j$ its components along the directions already built, and normalize. We check by induction on $j$ that the recursion is well defined and that $\{e_1, \ldots, e_j\}$ is orthonormal with $\operatorname{span}\{e_1, \ldots, e_j\} = \operatorname{span}\{y_1, \ldots, y_j\}$.
>
> *$j = 1$.* $y_1 \neq 0$ by linear independence, so $e_1$ is defined, $\|e_1\| = 1$, and $\operatorname{span}\{e_1\} = \operatorname{span}\{y_1\}$.
>
> *From $j - 1$ to $j$.* *$x_j \neq 0$:* otherwise $y_j = \sum_{i<j} (y_j, e_i) e_i \in \operatorname{span}\{e_1, \ldots, e_{j-1}\} = \operatorname{span}\{y_1, \ldots, y_{j-1}\}$, contradicting linear independence. So $e_j$ is defined and $\|e_j\| = 1$. *Orthogonality:* for $k < j$, using $(e_i, e_k) = \delta_{ik}$ for $i, k < j$,
>
> $$
> (x_j, e_k) = (y_j, e_k) - \sum_{i=1}^{j-1} (y_j, e_i)(e_i, e_k) = (y_j, e_k) - (y_j, e_k) = 0,
> $$
>
> so $(e_j, e_k) = 0$. *Spans:* $e_j$ is a combination of $y_j$ and $e_1, \ldots, e_{j-1} \in \operatorname{span}\{y_1, \ldots, y_{j-1}\}$, so $e_j \in \operatorname{span}\{y_1, \ldots, y_j\}$; conversely $y_j = \|x_j\|\, e_j + \sum_{i<j} (y_j, e_i) e_i \in \operatorname{span}\{e_1, \ldots, e_j\}$. With the induction hypothesis, the two spans are equal.
>
> Since $e_j$ depends only on $y_1, \ldots, y_j$, the recursion runs through an infinite sequence as well.

^pf-28-2

*Uses:* [[§27 Orthonormal Sets and Bases#^def-27-1|Def. §27.1]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]]

> [!remark]- Connections
> - Finite-dimensional home: [[Gram–Schmidt procedure|LADR 6.32]].
> - Used in Electromagnetism: Gram–Schmidt applied to $1, x, x^2, \dots$ in $L^2[-1, 1]$ gives the Legendre polynomials up to normalization — [[§B3.4 Separation of Variables in Spherical Coordinates#^rem-b3-4-1|EM Remark: Legendre polynomials are orthogonalized powers]], with their properties in [[§B3.4 Separation of Variables in Spherical Coordinates#^thm-b3-4-2|EM Theorem §B3.4.2]].
> - Computational version: [[§53 The Gram–Schmidt Process#^thm-53-1|235 Thm. §53.1]] (with worked examples and the QR factorization), and in inner product spaces [[§56 Inner Product Spaces#^thm-56-2|235 Thm. §56.2]].
> - Computational version: applied to $1, x, x^2, \ldots$ in $L^2[-1,1]$, Gram–Schmidt gives multiples of the Legendre polynomials, [[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|341 Def. §60.3]], whose orthogonality is [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-5|341 Prop. §60.5]].

> [!theorem] Theorem §28.3: Separable Hilbert Spaces and Countable Bases
> A Hilbert space $H$ has a countable orthonormal basis if and only if it is separable.
>
> *Lax: §6.4, Thm $9'$*

^thm-28-3

> [!proof]+ Proof of (⇒)
> Assume $H$ has a countable orthonormal basis $\{e_1, e_2, \ldots\}$ (finite or infinite). Then $H = \overline{\operatorname{span}}\{e_1, e_2, \ldots\}$: every $x \in H$ is $x = \sum_j (x, e_j)\, e_j$ (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]), a finite sum if the basis is finite and a limit of partial sums otherwise. Let
>
> $$
> D = \bigcup_{n} \Bigl\{ \sum_{j=1}^n a_j e_j : a_j \in \mathbb{Q}_{\mathbb{F}} \Bigr\},
> $$
>
> the union over $n = 1, 2, \ldots$ (only up to the number of basis vectors if the basis is finite). Each set in the union is in bijection with $\mathbb{Q}_{\mathbb{F}}^n$, so $D$ is countable.
>
> *$D$ is dense.* Let $x \in H$ and $\varepsilon > 0$. The partial sums of the expansion converge to $x$, so there is $n$ with $\bigl\| x - \sum_{j=1}^n (x, e_j) e_j \bigr\| < \varepsilon/2$ (if the basis is finite, take $n$ its size, and this term is $0$). Choose $a_j \in \mathbb{Q}_{\mathbb{F}}$ with $|(x, e_j) - a_j| < \frac{\varepsilon}{2\sqrt{n}}$. By Pythagoras (Lemma [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]]),
>
> $$
> \Bigl\| \sum_{j=1}^n \bigl( (x, e_j) - a_j \bigr) e_j \Bigr\|^2 = \sum_{j=1}^n |(x, e_j) - a_j|^2 < n \cdot \frac{\varepsilon^2}{4n} = \frac{\varepsilon^2}{4},
> $$
>
> so $\bigl\| x - \sum_{j=1}^n a_j e_j \bigr\| < \varepsilon/2 + \varepsilon/2 = \varepsilon$. The tail of the expansion is small, as for $\ell^p$ ([[§29 Sequence and Function Spaces#^prop-29-1|§29.1]], below).

^pf-28-3

*Uses:* [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]], [[§27 Orthonormal Sets and Bases#^prop-27-6|§27.6]], [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]], [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|Def. §28.1]], [[Countable Union of Countable Sets is Countable|551 §3.1]]

For the converse, the countable dense set has to be turned into an orthonormal set, which is the Gram–Schmidt process (Lemma [[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|§28.2]] above).

> [!proof]+ Proof of (⇐) in Theorem §28.3
> Assume $D = \{y_1, y_2, \ldots\}$ is a countable dense subset of $H$. If $H = \{0\}$, the empty set is a countable orthonormal basis; assume $H \neq \{0\}$, so $D$ contains a nonzero element.
>
> **Step 1: a linearly independent subsequence.** Discard elements that depend linearly on earlier ones. Precisely: let $n_1$ be the first index with $y_{n_1} \neq 0$, and put $y_1' = y_{n_1}$. Having chosen $n_1 < \cdots < n_k$, let $n_{k+1}$ be the first index $n > n_k$ with $y_n \notin \operatorname{span}\{y_1', \ldots, y_k'\}$, and put $y_{k+1}' = y_{n_{k+1}}$; if there is no such index, stop. Wu: “we just take the first linearly independent one, name it $y_2'$, then continue.” The result $D' = \{y_1', y_2', \ldots\}$ (finite or infinite) is linearly independent by construction, and every element of $D$ is a linear combination of elements of $D'$: an element $y_j$ that was discarded, with $n_k < j < n_{k+1}$ (or $j > n_k$ if the process stopped at $k$), lies in $\operatorname{span}\{y_1', \ldots, y_k'\}$, and $y_j = 0$ if $j < n_1$. So
>
> $$
> \text{for every } y_j \in D \text{ there is } k \text{ with } y_j \in \operatorname{span}\{y_1', \ldots, y_k'\}. \tag{5.5}
> $$
>
> **Step 2: Gram–Schmidt.** Lemma [[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|§28.2]] gives an orthonormal sequence $\{e_1, e_2, \ldots\}$ with
>
> $$
> \operatorname{span}\{e_1, \ldots, e_j\} = \operatorname{span}\{y_1', \ldots, y_j'\} \qquad \text{for every } j.
> $$
>
> It is countable; it remains to show it is complete, hence (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]) an orthonormal basis.
>
> **Step 3: completeness.** Let $x \in H$ with $(x, e_j) = 0$ for all $j$; we show $x = 0$. Since $D$ is dense in $H$, there is a sequence $y_{n_k} \in D$ with $\lim_{k \to \infty} y_{n_k} = x$. By (5.5) and Step 2, each $y_{n_k}$ lies in $\operatorname{span}\{e_1, \ldots, e_{j_k}\}$ for some $j_k$, say $y_{n_k} = \sum_{j=1}^{j_k} a_j^{(k)} e_j$. Then
>
> $$
> (x, y_{n_k}) = \sum_{j=1}^{j_k} \overline{a_j^{(k)}}\, (x, e_j) = 0 \qquad \text{for all } k,
> $$
>
> and by continuity of the inner product (Lemma [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]]),
>
> $$
> (x, x) = \lim_{k \to \infty} (x, y_{n_k}) = 0 .
> $$
>
> Hence $x = 0$, and $\{e_j\}$ is complete.

^pf-28-3-2

*Uses:* [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|Def. §28.1]], [[§28 Existence of Orthonormal Bases and Separability#^lem-28-2|§28.2]], [[§27 Orthonormal Sets and Bases#^def-27-2|Def. §27.2]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]], [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]]

> [!remark]- Connections
> - Every orthonormal set in a separable Hilbert space is countable, not just this one: [[§39 Position Eigenstates and Continuous Resolutions#^prop-39-1|§39.1]].

> [!remark] Remark
> The dense set $D$ is used twice, for different purposes: its span supplies the orthonormal vectors, and its density supplies the approximating sequence in Step 3. Only finite linear combinations appear anywhere — the limit is taken in the inner product, not in the expansion. Compare Proposition [[§39 Position Eigenstates and Continuous Resolutions#^prop-39-1|§39.1]]: in a separable Hilbert space *every* orthonormal set is countable, not just the one constructed here.

^rem-28-2

## Classification of Separable Hilbert Spaces

> [!definition] Definition §28.2: Isomorphic Hilbert Spaces
> Let $H_1$ and $H_2$ be Hilbert spaces over the same field, with inner products $(\cdot, \cdot)_1$ and $(\cdot, \cdot)_2$. $H_1$ is **isomorphic** to $H_2$ if there is a map $T : H_1 \to H_2$ that is linear, one-to-one and onto, and preserves the inner product:
>
> $$
> (Tx, Ty)_2 = (x, y)_1 \qquad \text{for all } x, y \in H_1 .
> $$

^def-28-2

> [!remark] Remark: Isomorphic or Isometric?
> A student asked whether “isomorphic” here means the map preserves distance. It does: $\|Tx - Ty\|_2^2 = (T(x-y), T(x-y))_2 = \|x - y\|_1^2$, so $T$ is an *isometry*. Preserving the inner product already forces one-to-one ($Tx = 0$ gives $\|x\|_1 = \|Tx\|_2 = 0$). What it does not force is *onto*, which is why the definition requires a bijection; the next example shows the difference. (The example is not from lecture.)

^rem-28-3

> [!remark]- Connections
> - Isometries between finite-dimensional inner product spaces, and why they are injective: [[§26 Isometries, Unitary Operators, and Matrix Factorization#^ladr-7-44|LADR 7.44]].

> [!example] Example §28.1: An Isometry That is Not an Isomorphism
> On $\ell^2$ let $S(a_1, a_2, \ldots) = (0, a_1, a_2, \ldots)$. $S$ is linear and $(Sa, Sb) = \sum_{j \ge 1} a_j \overline{b_j} = (a, b)$, so $S$ preserves the inner product. It is not onto: every $Sa$ has first coordinate $0$, so $e_1 = (1, 0, 0, \ldots)$ is not in the range.

^ex-28-1

> [!theorem] Theorem §28.4: Classification of Separable Hilbert Spaces
> Every [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|separable]] [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Hilbert space]] $H$ over $\mathbb{F}$ is [[§28 Existence of Orthonormal Bases and Separability#^def-28-2|isomorphic]] either to $\mathbb{F}^n$ for some $n \in \{0, 1, 2, \ldots\}$, or to $\ell^2$.
>
> *Source: HW5, Problem 2*
>
> *Lax: §6.4, Exercise 10*

^thm-28-4

> [!proof]+ Proof
> (HW5, Problem 2, for infinite-dimensional $H$; the finite-dimensional case is Claude's.) By Theorem [[§28 Existence of Orthonormal Bases and Separability#^thm-28-3|§28.3]], $H$ has a countable orthonormal basis.
>
> **Step 1: the size of the basis.** If the basis is finite, $\{e_1, \ldots, e_n\}$ ($n = 0$ meaning the empty set, $H = \{0\}$), every $x = \sum_{j=1}^n (x, e_j)\, e_j$ lies in $\operatorname{span}\{e_1, \ldots, e_n\}$. If $H$ is infinite-dimensional, the basis is therefore infinite, and we index it as $\{e_j\}_{j \in \mathbb{N}}$. Let $\mathcal{M}$ denote $\mathbb{F}^n$ in the finite case and $\ell^2$ in the infinite case, with $(a, b) = \sum_j a_j \overline{b_j}$.
>
> **Step 2: the map.** Define $T : H \to \mathcal{M}$ by $Tx = \bigl( (x, e_j) \bigr)_j$. By Parseval (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]]), $\sum_j |(x, e_j)|^2 = \|x\|^2 < \infty$, so $Tx \in \mathcal{M}$ and $\|Tx\| = \|x\|$. $T$ is linear because each $x \mapsto (x, e_j)$ is linear.
>
> **Step 3: $T$ preserves the inner product.** Let $x, y \in H$ and $s_N = \sum_{j \le N} (x, e_j)\, e_j$. Then $s_N \to x$, so by continuity of the inner product (Lemma [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]])
>
> $$
> (x, y) = \lim_{N \to \infty} (s_N, y) = \lim_{N \to \infty} \sum_{j \le N} (x, e_j)\,(e_j, y) = \sum_{j} (x, e_j)\, \overline{(y, e_j)} = (Tx, Ty),
> $$
>
> the last series converging absolutely by [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]] in $\ell^2$, since $Tx, Ty \in \ell^2$. (In the finite case all sums are finite.)
>
> **Step 4: $T$ is one-to-one.** If $Tx = 0$, then $\|x\| = \|Tx\| = 0$, so $x = 0$.
>
> **Step 5: $T$ is onto.** Let $b \in \mathcal{M}$ and $t_N = \sum_{j \le N} b_j e_j$. For $M < N$, by Pythagoras (Lemma [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]]), $\|t_N - t_M\|^2 = \sum_{j = M+1}^N |b_j|^2 \to 0$ as $M, N \to \infty$, so $\{t_N\}$ is Cauchy and, $H$ being complete, converges to some $x \in H$ (in the finite case simply $x = \sum_{j=1}^n b_j e_j$). For each $k$ and $N \ge k$, $(t_N, e_k) = b_k$; by continuity of the inner product, $(x, e_k) = b_k$. Hence $Tx = b$.
>
> So $T$ is linear, one-to-one, onto, and preserves the inner product: $H$ is isomorphic to $\mathbb{F}^n$ or to $\ell^2$.

^pf-28-4

*Uses:* [[§28 Existence of Orthonormal Bases and Separability#^thm-28-3|§28.3]], [[§27 Orthonormal Sets and Bases#^thm-27-8|§27.8]], [[§25 Projection and Orthogonal Decomposition#^lem-25-1|§25.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§27 Orthonormal Sets and Bases#^lem-27-1|§27.1]], [[§28 Existence of Orthonormal Bases and Separability#^def-28-2|Def. §28.2]], [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Def. §23.1]], [[§22 Definition and Examples#^ex-22-2|Ex. §22.2]]

> [!remark]- Connections
> - Finite-dimensional analogue: vector spaces of the same dimension are isomorphic, [[Dimension shows whether vector spaces are isomorphic|LADR 3.70]], via coordinates [[§10 Invertibility and Isomorphisms#^ladr-3-73|LADR 3.73]].

> [!remark] Remark
> The isomorphism is “take coordinates”: $x \mapsto ((x, e_j))_j$. Every result about a separable Hilbert space can therefore be checked on $\ell^2$, and the [[§27 Orthonormal Sets and Bases#^rem-27-9|earlier remark]] that $L^2[0, 2\pi]$ with the [[§27 Orthonormal Sets and Bases#^thm-27-11|Fourier basis]] is “the same” as $\ell^2(\mathbb{Z})$ is the special case $e_n = e^{inx}/\sqrt{2\pi}$. The isomorphism depends on the choice of basis, as in finite dimensions.

^rem-28-4

> [!remark] Remark
> On the board: “isomorphic either to $\mathbb{R}^n$, $n \in \mathbb{N}$, or $\ell^2$” — the real case. Over $\mathbb{C}$ the finite-dimensional models are $\mathbb{C}^n$, and $n = 0$ covers $H = \{0\}$. By Theorem [[§28 Existence of Orthonormal Bases and Separability#^thm-28-3|§28.3]] a separable $H$ has a countable orthonormal basis; the finite case gives $\mathbb{F}^n$ and the infinite case $\ell^2$.

^rem-28-5
