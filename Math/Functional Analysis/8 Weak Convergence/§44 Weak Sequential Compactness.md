---
type: section
subject: "[[Functional Analysis]]"
chapter: 8
section: 44
tags: [functional-analysis, math556]
---
← [[§43 Weak and Weak-Star Convergence]] · ↑ [[· 8 Weak Convergence]] · [[§45 Convergence of Operators]] →

*Stage: maps — Thread: compactness. A bounded sequence of functionals on a separable space has a weak-$\ast$ convergent subsequence (Helly); a bounded sequence in a reflexive space has a weakly convergent subsequence (Eberlein). With Mazur's theorem and the norm bound this produces closest points.*

*Lecture 19 (Tue Nov 10). Source: the handwritten notes of the lecture; there is no transcript. Statements and proofs follow the notes. The steps the notes leave out, and the examples marked as such, are filled in from Lax (§10.2, §10.3, Ch. 12). Two statements that the notes record without a hypothesis they need are stated here with it; the remarks after them say what was changed.*

## The Question

Three modes of convergence are now available, in decreasing strength. In a normed linear space $X$, strong convergence implies weak convergence (Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]](1)). In a dual space $X'$, weak convergence implies weak-$\ast$ convergence (Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-8|§43.8]](1)), and the two coincide when $X$ is reflexive, $X = X''$ (part (2) of that proposition).

The question left open at the end of [[§43 Weak and Weak-Star Convergence|§43]]: let $\{x_n\}_{n=1}^\infty$ be a bounded sequence in $X$. Is there a subsequence $\{x_{n_j}\}_{j=1}^\infty$ that converges weakly, or (when $X$ is a dual space) in the weak-$\ast$ sense, to some $x_0 \in X$? For strong convergence the answer is no as soon as $X$ is infinite-dimensional, since the closed unit ball is then not compact (Theorem [[§20 Compactness and the Unit Ball#^thm-20-5|§20.5]]). In $\ell^2$, for instance, the bounded sequence $\{e_n\}$ of Example [[§43 Weak and Weak-Star Convergence#^ex-43-1|§43.1]] has $\|e_n - e_m\| = \sqrt{2}$ for $n \neq m$, so none of its subsequences is Cauchy.

> [!definition] Definition §44.1: Weakly Sequentially Compact Set
> Let $X$ be a normed linear space and $C$ a subset of $X$. $C$ is **weakly sequentially compact** if every sequence $\{x_n\}_{n=1}^\infty \subset C$ has a subsequence $\{x_{n_j}\}_{j=1}^\infty$ and a point $x_0 \in C$ such that $x_{n_j} \rightharpoonup x_0$ as $j \to \infty$ (Definition [[§43 Weak and Weak-Star Convergence#^def-43-1|§43.1]]).
>
> *Lax: §10.2, definition*

^def-44-1

> [!remark]- Connections
> - The model: sequential compactness for strong convergence, [[§20 Compactness and the Unit Ball#^def-20-1|Def. §20.1]]; it fails for the unit ball in infinite dimensions, [[The Unit Ball of an Infinite-Dimensional Space Is Not Compact]].
> - In finite dimensions weak and strong convergence agree and this is Bolzano–Weierstrass: [[Bolzano–Weierstrass Theorem]].

> [!definition] Definition §44.2: Weak-$\ast$ Sequentially Compact Set
> Let $X$ be a normed linear space and $C$ a subset of $X'$. $C$ is **weak-$\ast$ sequentially compact** if every sequence $\{\ell_n\}_{n=1}^\infty \subset C$ has a subsequence $\{\ell_{n_j}\}_{j=1}^\infty$ and a point $\ell_0 \in C$ such that $\ell_{n_j} \overset{\ast}{\rightharpoonup} \ell_0$ as $j \to \infty$ (Definition [[§43 Weak and Weak-Star Convergence#^def-43-2|§43.2]]).
>
> *Lax: §10.3, definition*

^def-44-2

Both definitions copy Definition [[§20 Compactness and the Unit Ball#^def-20-1|§20.1]], with strong convergence replaced by a weaker one. In both the limit is required to lie in $C$.

## Helly's Theorem

> [!theorem] Theorem §44.1: Helly's Theorem
> Let $X$ be a separable normed linear space (Definition [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|§28.1]]), and let $\{\ell_n\}_{n=1}^\infty$ be a bounded sequence in $X'$, with $M = \sup_n \|\ell_n\| < \infty$. Then there are a subsequence $\{\ell_{n_j}\}_{j=1}^\infty$ and some $\ell_0 \in X'$ such that
>
> $$
> \ell_{n_j} \overset{\ast}{\rightharpoonup} \ell_0 \qquad \text{as } j \to \infty .
> $$
>
> Moreover $\|\ell_0\| \le M$.
>
> *Lax: §10.3, Thm 12 (for a separable Banach space, stated for the closed unit ball of $X'$; the name of Helly is Lax's)*

^thm-44-1

> [!proof]+ Proof
> Step 1 produces the subsequence by a diagonal process, so that it converges at every point of a countable dense set. Step 2 extends the convergence to all of $X$, and Step 3 shows that the limit is a bounded linear functional.
>
> Let $D = \{y_k\}_{k=1}^\infty$ be a countable dense subset of $X$, listed as a sequence (with repetitions if $D$ is finite).
>
> **Step 1: a subsequence that converges on $D$.** For each fixed $y \in X$ the numbers $\ell_n(y)$ are bounded:
>
> $$
> |\ell_n(y)| \le \|\ell_n\|\, \|y\| \le M\, \|y\| \qquad \text{for all } n
> $$
>
> (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](b)). A bounded sequence in $\mathbb{F}$ has a convergent subsequence, by the [[Bolzano–Weierstrass Theorem|Bolzano–Weierstrass theorem]]; for $\mathbb{F} = \mathbb{C}$ apply it to the real parts and then, along the subsequence obtained, to the imaginary parts.
>
> Apply this to $\{\ell_n(y_1)\}_{n}$: there are indices $n_{1,1} < n_{1,2} < n_{1,3} < \cdots$ such that $\{\ell_{n_{1,j}}(y_1)\}_{j=1}^\infty$ converges in $\mathbb{F}$. The sequence $\{\ell_{n_{1,j}}(y_2)\}_{j=1}^\infty$ is again bounded in $\mathbb{F}$, so the index sequence $\{n_{1,j}\}_j$ has a subsequence $n_{2,1} < n_{2,2} < \cdots$ such that $\{\ell_{n_{2,j}}(y_2)\}_{j=1}^\infty$ converges. Continue in the same way: if $\{n_{k,j}\}_{j=1}^\infty$ has been formed, then $\{\ell_{n_{k,j}}(y_{k+1})\}_{j=1}^\infty$ is bounded in $\mathbb{F}$, and $\{n_{k+1,j}\}_{j=1}^\infty$ is a subsequence of $\{n_{k,j}\}_{j=1}^\infty$ along which $\ell_{n_{k+1,j}}(y_{k+1})$ converges. This gives index sequences, each a subsequence of the one before,
>
> $$
> \{n_{1,j}\}_j \supset \{n_{2,j}\}_j \supset \cdots \supset \{n_{k,j}\}_j \supset \{n_{k+1,j}\}_j \supset \cdots .
> $$
>
> Put $z_k = \lim_{j \to \infty} \ell_{n_{k,j}}(y_k) \in \mathbb{F}$. Since a subsequence of a convergent sequence converges to the same limit,
>
> $$
> \lim_{j \to \infty} \ell_{n_{k,j}}(y_i) = z_i \qquad \text{for each } i = 1, \ldots, k .
> $$
>
> Now take the diagonal:
>
> $$
> n_j = n_{j,j}, \qquad \ell_{n_j} = \ell_{n_{j,j}}, \qquad j = 1, 2, \ldots .
> $$
>
> ![[m556-44-1.svg]]
>
> The diagonal process (the picture in the notes). Row $k$ is the index sequence $\{n_{k,j}\}_j$, a subsequence of the row above, along which $\ell_n(y_1), \ldots, \ell_n(y_k)$ converge. The circled diagonal $n_j = n_{j,j}$ is, from its $k$-th term on, a subsequence of row $k$, for every $k$.
>
> *The $n_j$ increase strictly.* Since $\{n_{j+1,i}\}_i$ is a subsequence of $\{n_{j,i}\}_i$, its $(j+1)$-st term is the $m$-th term of $\{n_{j,i}\}_i$ for some $m \ge j+1$. So $n_{j+1} = n_{j+1,j+1} = n_{j,m} \ge n_{j,j+1} > n_{j,j} = n_j$.
>
> *For each $k$, $\{n_j\}_{j \ge k}$ is a subsequence of $\{n_{k,j}\}_{j \ge 1}$.* For $j \ge k$ the number $n_j = n_{j,j}$ is a term of the $j$-th index sequence, hence of the $k$-th. As the $n_j$ increase strictly and $\{n_{k,i}\}_i$ is strictly increasing, the numbers $n_k < n_{k+1} < \cdots$ occur in $\{n_{k,i}\}_i$ at increasing positions.
>
> Consequently, for each fixed $k$,
>
> $$
> \ell_{n_{k,j}}(y_k) \to z_k \ \text{ as } j \to \infty \qquad \Longrightarrow \qquad \ell_{n_j}(y_k) \to z_k \ \text{ as } j \to \infty ,
> $$
>
> because $\{\ell_{n_j}(y_k)\}_{j \ge k}$ is a subsequence of the convergent sequence on the left. So $\{\ell_{n_j}\}_{j=1}^\infty$ is a subsequence of $\{\ell_n\}_{n=1}^\infty$ with
>
> $$
> \ell_{n_j}(y_k) \to z_k \in \mathbb{F} \qquad \text{for each } k, \text{ as } j \to \infty .
> $$
>
> **Step 2: the subsequence converges at every point of $X$.** We show that for every $x_0 \in X$ the sequence $\{\ell_{n_j}(x_0)\}_{j=1}^\infty$ is Cauchy in $\mathbb{F}$; since $\mathbb{F}$ is complete, it then converges. A bounded sequence of functionals that converges at every point of a dense set converges at every point.
>
> Let $x_0 \in X$ and $\varepsilon > 0$. We need $N$ such that $|\ell_{n_j}(x_0) - \ell_{n_k}(x_0)| < \varepsilon$ for all $j, k \ge N$. For every $y \in D$, by the triangle inequality, linearity, and $\|\ell_n\| \le M$ for all $n$,
>
> $$
> \begin{aligned}|\ell_{n_j}(x_0) - \ell_{n_k}(x_0)| &\le |\ell_{n_j}(y) - \ell_{n_k}(y)| + |\ell_{n_j}(x_0 - y) - \ell_{n_k}(x_0 - y)| \\
> &\le |\ell_{n_j}(y) - \ell_{n_k}(y)| + 2M\, \|x_0 - y\| .\end{aligned}
> $$
>
> First take $y_0 \in D$ with $2M\, \|x_0 - y_0\| < \frac{\varepsilon}{2}$, which is possible because $D$ is dense in $X$. Then take $N$ such that $|\ell_{n_j}(y_0) - \ell_{n_k}(y_0)| < \frac{\varepsilon}{2}$ for all $j, k \ge N$, which is possible because $\{\ell_{n_j}(y_0)\}_j$ converges by Step 1 and is therefore Cauchy. For $j, k \ge N$ the two terms add up to less than $\varepsilon$. So $\{\ell_{n_j}(x_0)\}_j$ is Cauchy in $\mathbb{F}$. (This step is Proposition [[§42 Uniform Boundedness and Approximation#^prop-42-8|§42.8]] with $Y = \mathbb{F}$.)
>
> **Step 3: the limit is a bounded linear functional.** Define
>
> $$
> \ell_0(x_0) := \lim_{j \to \infty} \ell_{n_j}(x_0), \qquad x_0 \in X ,
> $$
>
> which exists by Step 2. For $x, y \in X$ and $a, b \in \mathbb{F}$, by linearity of each $\ell_{n_j}$ and of limits,
>
> $$
> \ell_0(ax + by) = \lim_{j \to \infty} \ell_{n_j}(ax + by) = \lim_{j \to \infty} \bigl( a\, \ell_{n_j}(x) + b\, \ell_{n_j}(y) \bigr) = a\, \ell_0(x) + b\, \ell_0(y) ,
> $$
>
> so $\ell_0$ is linear. For $x \in X$,
>
> $$
> |\ell_0(x)| = \lim_{j \to \infty} |\ell_{n_j}(x)| \le M\, \|x\| ,
> $$
>
> since $|\ell_{n_j}(x)| \le M \|x\|$ for every $j$. So $\ell_0$ is bounded, $\ell_0 \in X'$, and $\|\ell_0\| \le M$. Finally, $\ell_{n_j}(x) \to \ell_0(x)$ for every $x \in X$ is the definition of $\ell_{n_j} \overset{\ast}{\rightharpoonup} \ell_0$ (Definition [[§43 Weak and Weak-Star Convergence#^def-43-2|§43.2]]).

^pf-44-1

*Uses:* [[§30 Boundedness and Continuity#^prop-30-1|§30.1]], [[§42 Uniform Boundedness and Approximation#^prop-42-8|§42.8]], [[§43 Weak and Weak-Star Convergence#^def-43-2|Def. §43.2]]

> [!remark]- Connections
> - Each extraction step is [[Bolzano–Weierstrass Theorem]] for a bounded sequence of numbers.
> - Technique: [[Functional Analysis Problem-Solving Techniques#^rem-t31|T31]].

> [!theorem] Corollary §44.2: Closed Balls in the Dual of a Separable Space
> Let $X$ be a separable normed linear space and $R \ge 0$. Then the closed ball $\{ \ell \in X' : \|\ell\| \le R \}$ of $X'$ is weak-$\ast$ sequentially compact (Definition [[§44 Weak Sequential Compactness#^def-44-2|§44.2]]).
>
> *Lax: §10.3, Thm 12*

^cor-44-2

> [!proof]+ Proof
> Let $\{\ell_n\}$ be a sequence in the ball, so $\sup_n \|\ell_n\| \le R$. By Theorem [[§44 Weak Sequential Compactness#^thm-44-1|§44.1]] a subsequence converges in the weak-$\ast$ sense to some $\ell_0 \in X'$ with $\|\ell_0\| \le \sup_n \|\ell_n\| \le R$. So $\ell_0$ lies in the ball.

^pf-44-2

*Uses:* [[§44 Weak Sequential Compactness#^thm-44-1|§44.1]]

> [!remark] Remark: Which Sets in $X'$ are Weak-$\ast$ Sequentially Compact
> In the notes of the lecture the corollary reads: if $X$ is separable, any bounded closed convex set in $X'$ is weak-$\ast$ sequentially compact. For a sequence in a bounded set $C \subset X'$, Helly's theorem gives a subsequence with a weak-$\ast$ limit $\ell_0 \in X'$; the definition asks in addition that $\ell_0 \in C$. For a closed ball this is the bound $\|\ell_0\| \le M$ of the theorem. For a convex set that is only closed in the norm of $X'$ it can fail (Example [[§44 Weak Sequential Compactness#^ex-44-1|§44.1]]), so the corollary is stated here for balls, as in Lax. For every bounded closed convex subset of $X'$ the statement is true when $X$ is reflexive (Corollary [[§44 Weak Sequential Compactness#^cor-44-8|§44.8]]).

^rem-44-1

> [!example] Example §44.1: A Bounded Closed Convex Set that is Not Weak-$\ast$ Sequentially Compact
> *(Not from lecture.)* Let $X = c_0$, which is separable (Proposition [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]), and identify $X'$ with $\ell^1$ by $a \mapsto \ell_a$, $\ell_a(x) = \sum_{j} x_j\, \overline{a_j}$ (Proposition [[§36 Duality in Normed Spaces#^prop-36-8|§36.8]]). The set
>
> $$
> C = \Bigl\{ \ell_a : a \in \ell^1,\ \|a\|_1 \le 1,\ \sum_{j=1}^\infty a_j = 1 \Bigr\} \subset X'
> $$
>
> is bounded, convex, and closed in the norm of $X'$, but it is not weak-$\ast$ sequentially compact.

^ex-44-1

> [!proof]+ Proof
> For $a \in \ell^1$ write $s(a) = \sum_{j=1}^\infty a_j$. The series converges absolutely, $s$ is linear on $\ell^1$, and $|s(a)| \le \|a\|_1$. By Proposition [[§36 Duality in Normed Spaces#^prop-36-8|§36.8]], $\|\ell_a\| = \|a\|_1$ and $\ell_a - \ell_b = \ell_{a - b}$ for $a, b \in \ell^1$.
>
> *Bounded.* $\|\ell_a\| = \|a\|_1 \le 1$ for $\ell_a \in C$.
>
> *Convex.* Let $\ell_a, \ell_b \in C$ and $0 \le t \le 1$. Since $t$ is real, $t\, \ell_a + (1 - t)\, \ell_b = \ell_c$ with $c = t a + (1 - t) b$. Then $\|c\|_1 \le t \|a\|_1 + (1 - t) \|b\|_1 \le 1$ and $s(c) = t\, s(a) + (1 - t)\, s(b) = 1$, so $\ell_c \in C$.
>
> *Closed.* Let $\ell_{a^{(k)}} \in C$ converge in $X'$ to some $\ell$. By Proposition [[§36 Duality in Normed Spaces#^prop-36-8|§36.8]](2), $\ell = \ell_a$ for some $a \in \ell^1$, and $\|a^{(k)} - a\|_1 = \|\ell_{a^{(k)}} - \ell_a\| \to 0$. So $\|a\|_1 = \lim_k \|a^{(k)}\|_1 \le 1$ (Proposition [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]), and $|s(a) - 1| = |s(a - a^{(k)})| \le \|a - a^{(k)}\|_1 \to 0$, so $s(a) = 1$. Hence $\ell \in C$.
>
> *Not weak-$\ast$ sequentially compact.* Let $e_n = (0, \ldots, 0, 1, 0, \ldots) \in \ell^1$, with the $1$ in the $n$-th place. Then $\|e_n\|_1 = 1$ and $s(e_n) = 1$, so $\ell_{e_n} \in C$. For every $x \in c_0$, $\ell_{e_n}(x) = x_n \to 0$ as $n \to \infty$. So $\ell_{e_n} \overset{\ast}{\rightharpoonup} 0$, and every subsequence of $\{\ell_{e_n}\}$ converges in the weak-$\ast$ sense to the zero functional as well. A weak-$\ast$ limit is a pointwise limit and therefore unique, so no subsequence has any other weak-$\ast$ limit. The zero functional is $\ell_a$ only for $a = 0$ (the map $a \mapsto \ell_a$ is one-to-one), and $s(0) = 0 \neq 1$; so it is not in $C$. No subsequence of $\{\ell_{e_n}\} \subset C$ converges in the weak-$\ast$ sense to a point of $C$.

^pf-ex-44-1

*Uses:* [[§36 Duality in Normed Spaces#^prop-36-8|§36.8]], [[§11 Normed Linear Spaces#^prop-11-4|§11.4]]

## Eberlein's Theorem

In a reflexive space, Helly's theorem applies to $X'' = X$ and gives weakly convergent subsequences. Helly's theorem needs a separable space, and a reflexive space need not be separable; the proof therefore passes to the closed linear span of the given sequence. That this span is separable is the following lemma.

> [!theorem] Lemma §44.3: The Closed Span of a Countable Set is Separable
> *(Not from lecture; filled in.)* Let $X$ be a normed linear space over $\mathbb{F}$ and $\{z_j\}_{j=1}^\infty \subset X$. Then $X_0 = \overline{\operatorname{span}}\, \{z_j\}_{j=1}^\infty$ (Definition [[§11 Normed Linear Spaces#^def-11-9|§11.9]]), with the norm of $X$, is a separable normed linear space.

^lem-44-3

> [!proof]+ Proof
> $X_0$ is a linear subspace of $X$ (Lemma [[§11 Normed Linear Spaces#^lem-11-8|§11.8]](1)), so it is a normed linear space in the norm of $X$. Let $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q}$ if $\mathbb{F} = \mathbb{R}$ and $\mathbb{Q}_{\mathbb{F}} = \mathbb{Q} + i\mathbb{Q}$ if $\mathbb{F} = \mathbb{C}$, a countable dense subset of $\mathbb{F}$, and
>
> $$
> D_1 = \Bigl\{ \sum_{j=1}^n a_j z_j : n \in \mathbb{N},\ a_1, \ldots, a_n \in \mathbb{Q}_{\mathbb{F}} \Bigr\} \subset X_0 .
> $$
>
> *$D_1$ is countable.* For each $n$ the $n$-tuples $(a_1, \ldots, a_n)$ of elements of the countable set $\mathbb{Q}_{\mathbb{F}}$ form a countable set, and $D_1$ is the union over $n \in \mathbb{N}$ of the images of these sets; a countable union of countable sets is countable.
>
> *$D_1$ is dense in $X_0$.* Let $x \in X_0$ and $\varepsilon > 0$. Since $X_0$ is the closure of $\operatorname{span}\{z_j\}$, there is a finite linear combination $z = \sum_{j=1}^n c_j z_j$, $c_j \in \mathbb{F}$, with $\|x - z\| < \frac{\varepsilon}{2}$. Since $\mathbb{Q}_{\mathbb{F}}$ is dense in $\mathbb{F}$, there are $a_j \in \mathbb{Q}_{\mathbb{F}}$ with $|c_j - a_j|\, \|z_j\| < \frac{\varepsilon}{2n}$ for $j = 1, \ldots, n$. Then $w = \sum_{j=1}^n a_j z_j \in D_1$ and
>
> $$
> \|x - w\| \le \|x - z\| + \sum_{j=1}^n |c_j - a_j|\, \|z_j\| < \frac{\varepsilon}{2} + n \cdot \frac{\varepsilon}{2n} = \varepsilon .
> $$
>
> So $X_0$ has a countable dense subset: it is separable (Definition [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|§28.1]]).

^pf-44-3

*Uses:* [[§11 Normed Linear Spaces#^lem-11-8|§11.8]], [[§28 Existence of Orthonormal Bases and Separability#^def-28-1|Def. §28.1]]

> [!theorem] Theorem §44.4: Eberlein's Theorem
> Let $X$ be a reflexive Banach space (Definition [[§37 Separable Duals and Reflexive Spaces#^def-37-1|§37.1]]). Then every bounded sequence $\{x_n\}_{n=1}^\infty$ in $X$ has a subsequence $\{x_{n_j}\}_{j=1}^\infty$ that converges weakly to some element $x_0 \in X$.
>
> *Lax: §10.2, Thm 7 (stated for the closed unit ball)*

^thm-44-4

> [!proof]+ Proof
> Let $i : X \to X''$, $i(x)(\ell) = \ell(x)$, be the canonical embedding (Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]); $X$ reflexive means that $i$ is onto.
>
> **Case 1: $X$ is separable.** Since $X$ is reflexive and separable, $X'$ is separable (Corollary [[§37 Separable Duals and Reflexive Spaces#^cor-37-7|§37.7]]). Let $\{x_n\}$ be a bounded sequence in $X$ and put $\eta_n = i(x_n) \in X''$. Then $\|\eta_n\| = \|x_n\|$, so $\{\eta_n\}$ is a bounded sequence in $X'' = (X')'$, the dual of the separable normed linear space $X'$. By Helly's theorem (Theorem [[§44 Weak Sequential Compactness#^thm-44-1|§44.1]], with $X'$ in place of $X$) there are a subsequence $\{\eta_{n_j}\}$ and some $\eta_0 \in X''$ with $\eta_{n_j} \overset{\ast}{\rightharpoonup} \eta_0$, that is,
>
> $$
> \eta_{n_j}(\ell) \to \eta_0(\ell) \qquad \text{for all } \ell \in X' .
> $$
>
> Since $i$ is onto, $\eta_0 = i(x_0)$ for some $x_0 \in X$. As $\eta_{n_j}(\ell) = \ell(x_{n_j})$ and $\eta_0(\ell) = \ell(x_0)$, this reads
>
> $$
> \ell(x_{n_j}) \to \ell(x_0) \qquad \text{for all } \ell \in X' , \qquad \text{i.e.} \qquad x_{n_j} \rightharpoonup x_0 .
> $$
>
> **Case 2: $X$ is any reflexive Banach space.** Let $\{x_n\}$ be a bounded sequence in $X$ and define
>
> $$
> X_0 = \overline{\operatorname{span}}\, \{x_n\}_{n=1}^\infty .
> $$
>
> $X_0$ is a closed linear subspace of $X$ (Lemma [[§11 Normed Linear Spaces#^lem-11-8|§11.8]](1)); it is separable (Lemma [[§44 Weak Sequential Compactness#^lem-44-3|§44.3]]), and it is reflexive, as a closed linear subspace of a reflexive Banach space (Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-8|§37.8]]): $X_0 = X_0''$. The sequence $\{x_n\}$ lies in $X_0$ and is bounded there. By Case 1, applied to $X_0$, there are a subsequence $\{x_{n_j}\}$ and some $x_0 \in X_0 \subset X$ such that
>
> $$
> m(x_{n_j}) \to m(x_0) \quad \text{as } j \to \infty, \qquad \text{for all } m \in X_0' .
> $$
>
> We want: $\ell(x_{n_j}) \to \ell(x_0)$ for all $\ell \in X'$. Let $\ell \in X' = \mathcal{L}(X, \mathbb{F})$ and let $m = \ell|_{X_0}$ be its restriction to $X_0$, that is, $m(x) = \ell(x)$ for all $x \in X_0$. Then $m$ is linear and $|m(x)| \le \|\ell\|\, \|x\|$ on $X_0$, so $m \in X_0'$, and therefore $m(x_{n_j}) \to m(x_0)$. But $m(x_{n_j}) = \ell(x_{n_j})$ and, since $x_0 \in X_0$, $m(x_0) = \ell(x_0)$. Hence $\ell(x_{n_j}) \to \ell(x_0)$ as $j \to \infty$, for every $\ell \in X'$: $x_{n_j} \rightharpoonup x_0$ in $X$.

^pf-44-4

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]], [[§37 Separable Duals and Reflexive Spaces#^cor-37-7|§37.7]], [[§44 Weak Sequential Compactness#^thm-44-1|§44.1]], [[§11 Normed Linear Spaces#^lem-11-8|§11.8]], [[§44 Weak Sequential Compactness#^lem-44-3|§44.3]], [[§37 Separable Duals and Reflexive Spaces#^thm-37-8|§37.8]]

> [!theorem] Corollary §44.5: Closed Balls of a Reflexive Space
> Let $X$ be a reflexive Banach space and $R \ge 0$. Then the closed ball $\{ x \in X : \|x\| \le R \}$ is weakly sequentially compact (Definition [[§44 Weak Sequential Compactness#^def-44-1|§44.1]]).
>
> *Lax: §10.2, Thm 7*

^cor-44-5

> [!proof]+ Proof
> *(Not from lecture; filled in.)* Let $\{x_n\}$ be a sequence with $\|x_n\| \le R$. By Theorem [[§44 Weak Sequential Compactness#^thm-44-4|§44.4]] a subsequence $\{x_{n_j}\}$ converges weakly to some $x_0 \in X$, and by Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]], $\|x_0\| \le \liminf_{j \to \infty} \|x_{n_j}\| \le R$. So $x_0$ lies in the ball.

^pf-44-5

*Uses:* [[§44 Weak Sequential Compactness#^thm-44-4|§44.4]], [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]

> [!theorem] Theorem §44.6: Weak Sequential Compactness of the Unit Ball Forces Reflexivity
> Let $X$ be a normed linear space. If the closed unit ball $\{ x \in X : \|x\| \le 1 \}$ of $X$ is weakly sequentially compact, then $X$ is a reflexive Banach space.
>
> *Lax: §10.2, Thm 8 (attributed to Eberlein; stated without proof)*

^thm-44-6

> [!proof]+ Proof (not given in this course)
> Stated in lecture without proof, under the name of Eberlein; Lax also states it without proof. With Corollary [[§44 Weak Sequential Compactness#^cor-44-5|§44.5]] it says that the closed unit ball of a Banach space is weakly sequentially compact if and only if the space is reflexive.

^pf-44-6

> [!theorem] Corollary §44.7: Bounded Closed Convex Sets in a Reflexive Space
> Let $X$ be a reflexive Banach space. Then every bounded closed convex subset $K$ of $X$ is weakly sequentially compact.
>
> *Lax: §10.2, Thm 9*

^cor-44-7

> [!proof]+ Proof
> *(Stated in lecture without proof; filled in, following Lax.)* Let $\{x_n\}$ be a sequence in $K$. It is bounded, since $K$ is. By Theorem [[§44 Weak Sequential Compactness#^thm-44-4|§44.4]] there are a subsequence $\{x_{n_j}\}$ and $x_0 \in X$ with $x_{n_j} \rightharpoonup x_0$. It remains to show $x_0 \in K$.
>
> By Mazur's theorem (Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-7|§43.7]]), applied to the sequence $\{x_{n_j}\}_j$, for every $k \in \mathbb{N}$ there is a convex combination $u_k$ of finitely many terms of $\{x_{n_j}\}_j$ with $\|x_0 - u_k\| < \frac1k$. The terms $x_{n_j}$ lie in the convex set $K$, and a convex set contains the finite convex combinations of its points (by induction on the number of points, as in the paragraph after the proof of Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-7|§43.7]]); so $u_k \in K$. Thus $u_k \to x_0$ with $u_k \in K$, and since $K$ is closed, $x_0 \in K$ (Definition [[§11 Normed Linear Spaces#^def-11-6|§11.6]]).

^pf-44-7

*Uses:* [[§44 Weak Sequential Compactness#^thm-44-4|§44.4]], [[§43 Weak and Weak-Star Convergence#^thm-43-7|§43.7]], [[§11 Normed Linear Spaces#^def-11-6|Def. §11.6]]

> [!theorem] Corollary §44.8: Bounded Closed Convex Sets in the Dual of a Reflexive Space
> *(Not from lecture.)* Let $X$ be a reflexive normed linear space. Then every bounded convex subset $C$ of $X'$ that is closed in the norm of $X'$ is weak-$\ast$ sequentially compact.

^cor-44-8

> [!proof]+ Proof
> $X$ is a Banach space (Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-6|§37.6]]), so $X'$ is reflexive (Theorem [[§37 Separable Duals and Reflexive Spaces#^thm-37-9|§37.9]]), and $X'$ is a Banach space (Corollary [[§31 Dual Spaces#^cor-31-1|§31.1]]). Let $\{\ell_n\}$ be a sequence in $C$. By Corollary [[§44 Weak Sequential Compactness#^cor-44-7|§44.7]], applied to the reflexive Banach space $X'$ and its bounded closed convex subset $C$, there are a subsequence $\{\ell_{n_j}\}$ and $\ell_0 \in C$ with $\ell_{n_j} \rightharpoonup \ell_0$ weakly in $X'$. Weak convergence in $X'$ implies weak-$\ast$ convergence (Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-8|§43.8]](1)), so $\ell_{n_j} \overset{\ast}{\rightharpoonup} \ell_0 \in C$.

^pf-44-8

*Uses:* [[§37 Separable Duals and Reflexive Spaces#^prop-37-6|§37.6]], [[§37 Separable Duals and Reflexive Spaces#^thm-37-9|§37.9]], [[§31 Dual Spaces#^cor-31-1|§31.1]], [[§44 Weak Sequential Compactness#^cor-44-7|§44.7]], [[§43 Weak and Weak-Star Convergence#^prop-43-8|§43.8]]

![[m556-44-2.svg]]

How the results of this section depend on each other. Each arrow names what is added. Alaoglu's theorem (below) drops separability, at the price of replacing subsequences by compactness in a topology.

## Alaoglu's Theorem

Helly's theorem asks for a separable $X$. For sequences this hypothesis cannot be dropped.

> [!example] Example §44.2: A Bounded Sequence in $(\ell^\infty)'$ with No Weak-$\ast$ Convergent Subsequence
> *(Not from lecture.)* Let $X = \ell^\infty$, which is not separable (Proposition [[§29 Sequence and Function Spaces#^prop-29-4|§29.4]]), and let $\delta_n(x) = x_n$ be the $n$-th coordinate of $x = (x_1, x_2, \ldots) \in \ell^\infty$. Then $\delta_n \in X'$ with $\|\delta_n\| = 1$, and no subsequence of $\{\delta_n\}_{n=1}^\infty$ converges in the weak-$\ast$ sense.

^ex-44-2

> [!proof]+ Proof
> $\delta_n$ is linear and $|\delta_n(x)| = |x_n| \le \|x\|_\infty$, so $\delta_n \in X'$ with $\|\delta_n\| \le 1$; and $\delta_n(e_n) = 1$ for the sequence $e_n \in \ell^\infty$ with $1$ in the $n$-th place and $0$ elsewhere, $\|e_n\|_\infty = 1$, so $\|\delta_n\| = 1$.
>
> Let $n_1 < n_2 < \cdots$ be any sequence of indices. Define $x \in \ell^\infty$ by $x_{n_j} = (-1)^j$ for $j = 1, 2, \ldots$ and $x_i = 0$ for all other $i$; then $\|x\|_\infty = 1$. The numbers $\delta_{n_j}(x) = (-1)^j$ do not converge as $j \to \infty$. So $\{\delta_{n_j}\}$ does not converge at the point $x$, and hence has no weak-$\ast$ limit (Definition [[§43 Weak and Weak-Star Convergence#^def-43-2|§43.2]]).

^pf-ex-44-2

*Uses:* [[§43 Weak and Weak-Star Convergence#^def-43-2|Def. §43.2]]

What holds without separability is compactness in a topology on $X'$, not compactness for sequences.

> [!definition] Definition §44.3: Weak-$\ast$ Topology
> *(Not from lecture; needed to state Alaoglu's theorem.)* Let $X$ be a normed linear space. A subset $U \subset X'$ is **weak-$\ast$ open** if for every $\ell_1 \in U$ there are finitely many points $x_1, \ldots, x_k \in X$ and $\varepsilon > 0$ such that
>
> $$
> \bigl\{ \ell \in X' : |\ell(x_i) - \ell_1(x_i)| < \varepsilon \text{ for } i = 1, \ldots, k \bigr\} \subset U .
> $$
>
> The collection of weak-$\ast$ open sets is the **weak-$\ast$ topology** of $X'$. It is the coarsest topology on $X'$ in which every function $\ell \mapsto \ell(x)$, $x \in X$, is continuous.
>
> *Lax: Ch. 12, definition before Thm 3*

^def-44-3

> [!definition] Definition §44.4: Weak-$\ast$ Compact Set
> *(Not from lecture.)* Let $X$ be a normed linear space. A subset $K \subset X'$ is **weak-$\ast$ compact** if every collection of weak-$\ast$ open sets (Definition [[§44 Weak Sequential Compactness#^def-44-3|§44.3]]) whose union contains $K$ has a finite subcollection whose union still contains $K$. This is Definition [[§20 Compactness and the Unit Ball#^def-20-4|§20.4]] with weak-$\ast$ open sets in place of open sets.

^def-44-4

> [!theorem] Theorem §44.9: Alaoglu's Theorem
> Let $X$ be a normed linear space. Then the closed unit ball $\{ \ell \in X' : \|\ell\| \le 1 \}$ of $X'$ is weak-$\ast$ compact (Definition [[§44 Weak Sequential Compactness#^def-44-4|§44.4]]).
>
> *Lax: Ch. 12, Thm 3*

^thm-44-9

> [!proof]+ Proof (not given in this course)
> Stated in lecture without proof. Lax's proof regards a functional $\ell$ with $\|\ell\| \le 1$ as the point $(\ell(x))_{x \in X}$ of the product of the compact sets $\{ c \in \mathbb{F} : |c| \le \|x\| \}$, $x \in X$. The product is compact by Tychonoff's theorem, the weak-$\ast$ topology of the ball is the topology it inherits from the product, and the image of the ball is closed in the product.

^pf-44-9

> [!remark]- Connections
> - Compactness by open covers: [[§20 Compactness and the Unit Ball#^def-20-4|Def. §20.4]]; topologies and compact spaces in general: [[Topology]].
> - Tychonoff's theorem (products of compact spaces are compact) is the tool in Lax's proof; it is not proved in these notes.

> [!remark] Remark: Alaoglu's Theorem and Sequences
> In the notes of the lecture the theorem reads: for a normed linear space $X$, any bounded sequence in $X'$ has a weak-$\ast$ convergent subsequence. In this sequential form the statement is Helly's theorem (Theorem [[§44 Weak Sequential Compactness#^thm-44-1|§44.1]]), and it needs $X$ separable: for $X = \ell^\infty$ it fails (Example [[§44 Weak Sequential Compactness#^ex-44-2|§44.2]]). Alaoglu's theorem has no separability hypothesis, and its conclusion is compactness in the weak-$\ast$ topology; for a space $X$ that is not separable this does not provide convergent subsequences.

^rem-44-2

## The Closest Point in a Reflexive Space

In a Hilbert space every nonempty closed convex set has a unique closest point to any given point (Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-2|§25.2]]); the proof used the parallelogram law to show that a minimizing sequence is Cauchy. In a reflexive Banach space there is no parallelogram law, but a minimizing sequence still has a weakly convergent subsequence, and that is enough for existence.

> [!theorem] Theorem §44.10: Closest Point in a Closed Convex Subset of a Reflexive Space
> Let $X$ be a reflexive Banach space, $K$ a nonempty closed convex subset of $X$, and $x_0 \in X$. Then there is $y_0 \in K$ such that
>
> $$
> \operatorname{dist}(x_0, K) := \inf_{y \in K} \|x_0 - y\| = \|x_0 - y_0\| .
> $$
>
> *Lax: §10.2, Thm 10*

^thm-44-10

> [!proof]+ Proof
> Let $d = \inf_{y \in K} \|x_0 - y\|$; it is a finite number $\ge 0$ because $K$ is nonempty. We find $y_0 \in K$ with $\|x_0 - y_0\| \le d$; since $\|x_0 - y_0\| \ge d$ for every point of $K$, this proves the theorem.
>
> **Step 1: a minimizing sequence.** By the definition of the infimum, for every $n \in \mathbb{N}$ there is $y_n \in K$ with
>
> $$
> d \le \|x_0 - y_n\| < d + \frac1n .
> $$
>
> So $\|y_n - x_0\| < d + 1$ for all $n$: $\{y_n - x_0\}$ is a bounded sequence in $X$, and $\|y_n - x_0\| \to d$.
>
> **Step 2: a weakly convergent subsequence.** By Eberlein's theorem (Theorem [[§44 Weak Sequential Compactness#^thm-44-4|§44.4]]) there are a subsequence $\{y_{n_j}\}$ and a point of $X$, which we write as $y_0 - x_0$, such that
>
> $$
> y_{n_j} - x_0 \rightharpoonup y_0 - x_0 \qquad \text{as } j \to \infty .
> $$
>
> Then also $y_{n_j} \rightharpoonup y_0$, since $\ell(y_{n_j}) = \ell(y_{n_j} - x_0) + \ell(x_0) \to \ell(y_0 - x_0) + \ell(x_0) = \ell(y_0)$ for every $\ell \in X'$.
>
> **Step 3: $y_0 \in K$.**
> By Mazur's theorem (Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-7|§43.7]]), $y_0$ lies in the closed convex hull of $\{y_{n_j}\}_j$: for every $k$ there is a finite convex combination $u_k$ of the points $y_{n_j} \in K$ with $\|y_0 - u_k\| < \frac1k$. As in the proof of Corollary [[§44 Weak Sequential Compactness#^cor-44-7|§44.7]], $u_k \in K$ because $K$ is convex, and $y_0 = \lim_k u_k \in K$ because $K$ is closed.
>
> **Step 4: $y_0$ is a closest point.** Since $y_0 \in K$, $d \le \|y_0 - x_0\|$. By the bound for the norm of a weak limit (Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]), applied to $y_{n_j} - x_0 \rightharpoonup y_0 - x_0$, and by Step 1,
>
> $$
> d \le \|y_0 - x_0\| \le \liminf_{j \to \infty} \|y_{n_j} - x_0\| = d .
> $$
>
> So $\|x_0 - y_0\| = d$.

^pf-44-10

*Uses:* [[§44 Weak Sequential Compactness#^thm-44-4|§44.4]], [[§43 Weak and Weak-Star Convergence#^thm-43-7|§43.7]], [[§44 Weak Sequential Compactness#^cor-44-7|§44.7]], [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]]

> [!remark]- Connections
> - The Hilbert space case, with uniqueness: [[Closest Point in a Closed Convex Set]] ([[§25 Projection and Orthogonal Decomposition#^thm-25-2|§25.2]]).
> - Technique: [[Functional Analysis Problem-Solving Techniques#^rem-t32|T32]].

![[m556-44-3.svg]]

The closest point (the picture in the notes): $y_0 \in K$ with $\|x_0 - y_0\| = d = \operatorname{dist}(x_0, K)$.

The theorem gives existence only. Uniqueness, which holds in a Hilbert space, can fail; and existence can fail when $X$ is not reflexive. The next lemma supplies a reflexive space for the first example.

> [!theorem] Lemma §44.11: Finite-Dimensional Normed Spaces are Reflexive
> *(Not from lecture.)* Let $X$ be a finite-dimensional normed linear space. Then $X$ is reflexive.

^lem-44-11

> [!proof]+ Proof
> If $X = \{0\}$, then $X' = \{0\}$ and $X'' = \{0\}$, and $i$ is onto. Let $n = \dim X \ge 1$ and let $e_1, \ldots, e_n$ be a basis of $X$.
>
> *$\dim X' = n$.* Every linear functional on $X$ is bounded (Proposition [[§30 Boundedness and Continuity#^prop-30-7|§30.7]]), so $X'$ consists of all linear functionals on $X$. For $k = 1, \ldots, n$ let $\varepsilon_k$ be the $k$-th coordinate functional, $\varepsilon_k\bigl( \sum_{i=1}^n a_i e_i \bigr) = a_k$. Every linear $\ell$ satisfies $\ell\bigl( \sum_i a_i e_i \bigr) = \sum_i a_i\, \ell(e_i)$, i.e. $\ell = \sum_{k=1}^n \ell(e_k)\, \varepsilon_k$; so the $\varepsilon_k$ span $X'$. They are linearly independent: if $\sum_k c_k \varepsilon_k = 0$, evaluating at $e_i$ gives $c_i = 0$. So $\varepsilon_1, \ldots, \varepsilon_n$ is a basis of $X'$.
>
> *$i$ is onto.* Applying the previous step to the $n$-dimensional normed linear space $X'$ gives $\dim X'' = n$. The canonical embedding $i : X \to X''$ is linear and an isometry (Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]), hence one-to-one (Lemma [[§13 The Completion of a Normed Space#^lem-13-2|§13.2]](2)). So $i(e_1), \ldots, i(e_n)$ are linearly independent in $X''$: if $\sum_k c_k\, i(e_k) = i\bigl( \sum_k c_k e_k \bigr) = 0$, then $\sum_k c_k e_k = 0$ and all $c_k = 0$. Being $n$ linearly independent vectors in a space of dimension $n$, they span $X''$. So $i$ is onto, and $X$ is reflexive (Definition [[§37 Separable Duals and Reflexive Spaces#^def-37-1|§37.1]]).

^pf-44-11

*Uses:* [[§30 Boundedness and Continuity#^prop-30-7|§30.7]], [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]], [[§13 The Completion of a Normed Space#^lem-13-2|§13.2]], [[§37 Separable Duals and Reflexive Spaces#^def-37-1|Def. §37.1]]

> [!example] Example §44.3: The Closest Point Need Not be Unique
> *(Not from lecture.)* Let $X = \mathbb{R}^2$ with the maximum norm $\|x\|_\infty = \max\{|x_1|, |x_2|\}$, a reflexive Banach space (Lemma [[§44 Weak Sequential Compactness#^lem-44-11|§44.11]]). Let $K = \{ x \in \mathbb{R}^2 : x_1 \ge 1 \}$ and $x_0 = 0$. Then $K$ is nonempty, closed and convex, $\operatorname{dist}(x_0, K) = 1$, and every point $(1, t)$ with $|t| \le 1$ is a closest point of $K$ to $x_0$.

^ex-44-3

> [!proof]+ Proof
> $K$ is nonempty, and it is convex: if $x_1 \ge 1$ and $y_1 \ge 1$, then $s x_1 + (1 - s) y_1 \ge 1$ for $0 \le s \le 1$. It is closed: if $x^{(k)} \in K$ and $\|x^{(k)} - x\|_\infty \to 0$, then $x^{(k)}_1 \to x_1$, so $x_1 \ge 1$. For $x \in K$, $\|x - 0\|_\infty \ge |x_1| \ge 1$, so $\operatorname{dist}(0, K) \ge 1$; and for $|t| \le 1$, $(1, t) \in K$ with $\|(1, t)\|_\infty = \max\{1, |t|\} = 1$. So the distance is $1$, and it is attained at every $(1, t)$, $|t| \le 1$.

^pf-ex-44-3

![[m556-44-4.svg]]

The closest points of the half-plane $K = \{x_1 \ge 1\}$ to $x_0 = 0$ are where the ball of radius $\operatorname{dist}(x_0, K) = 1$ about $x_0$ touches $K$ (red). The round ball of the Euclidean norm touches in one point; the square ball of the maximum norm (Example [[§44 Weak Sequential Compactness#^ex-44-3|§44.3]]) touches along a whole side.

> [!example] Example §44.4: No Closest Point in $C[0,1]$
> *(Not from lecture.)* Let $X = C[0,1]$ with the maximum norm, which is not reflexive (Example [[§37 Separable Duals and Reflexive Spaces#^ex-37-5|§37.5]]). Let $\ell(x) = \int_0^1 \bigl( t - \frac12 \bigr)\, x(t)\, dt$, so $\ell \in X'$ with $\|\ell\| = \frac14$ (Proposition [[§31 Dual Spaces#^prop-31-5|§31.5]]), and
>
> $$
> K = \bigl\{ x \in C[0,1] : \ell(x) = \tfrac14 \bigr\} .
> $$
>
> Then $K$ is nonempty, closed and convex, $\operatorname{dist}(0, K) = 1$, and no point of $K$ has norm $1$: $K$ has no closest point to $0$. So in Theorem [[§44 Weak Sequential Compactness#^thm-44-10|§44.10]] the reflexivity of $X$ cannot be dropped.

^ex-44-4

> [!proof]+ Proof
> *$K$ is closed and convex.* If $x_k \in K$ and $x_k \to x$ in $X$, then $\ell(x) = \lim_k \ell(x_k) = \frac14$, because $\ell$ is continuous (Proposition [[§30 Boundedness and Continuity#^prop-30-2|§30.2]]); so $x \in K$. If $x, y \in K$ and $0 \le s \le 1$, then $\ell(sx + (1 - s)y) = \frac{s}{4} + \frac{1 - s}{4} = \frac14$.
>
> *Every point of $K$ has norm at least $1$.* For $x \in K$, $\frac14 = |\ell(x)| \le \|\ell\|\, \|x\| = \frac14 \|x\|$, so $\|x\| \ge 1$.
>
> *$K$ is nonempty and $\operatorname{dist}(0, K) = 1$.* Let $0 < \varepsilon < \frac14$. By Steps 2 and 3 of the proof of Proposition [[§31 Dual Spaces#^prop-31-5|§31.5]] (with $f_0(t) = t - \frac12$ and $A = \frac14$ there) there is $x_\varepsilon \in C[0,1]$ with $\|x_\varepsilon\| \le 1$ and $\ell(x_\varepsilon)$ real, $\ell(x_\varepsilon) \ge \frac14 - \varepsilon > 0$. Put $y_\varepsilon = \frac{1}{4\, \ell(x_\varepsilon)}\, x_\varepsilon$. Then $\ell(y_\varepsilon) = \frac14$, so $y_\varepsilon \in K$, and
>
> $$
> \|y_\varepsilon\| = \frac{\|x_\varepsilon\|}{4\, \ell(x_\varepsilon)} \le \frac{1}{1 - 4\varepsilon} \longrightarrow 1 \qquad \text{as } \varepsilon \to 0 .
> $$
>
> With the previous step, $\inf_{y \in K} \|y\| = 1$.
>
> *The distance is not attained.* If some $y \in K$ had $\|y\| = 1$, then $\|y\| \le 1$ and $|\ell(y)| = \frac14 = \|\ell\|$, which is impossible by Example [[§31 Dual Spaces#^ex-31-2|§31.2]].

^pf-ex-44-4

*Uses:* [[§30 Boundedness and Continuity#^prop-30-2|§30.2]], [[§31 Dual Spaces#^prop-31-5|§31.5]], [[§31 Dual Spaces#^ex-31-2|Ex. §31.2]]
