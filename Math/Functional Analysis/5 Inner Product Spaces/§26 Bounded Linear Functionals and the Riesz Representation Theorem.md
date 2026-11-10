---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 26
tags: [functional-analysis, math556]
---
← [[§25 Projection and Orthogonal Decomposition]] · ↑ [[· 5 Inner Product Spaces]] · [[§27 Orthonormal Sets and Bases]] →

*Stage: inner products — Thread: functionals. On a Hilbert space every bounded functional is an inner product.*

## Bounded Linear Functionals

On $\mathbb{R}^n$ every linear functional is $x \mapsto a \cdot x$ for a unique vector $a$ (Example [[§3 Linear Maps, Convexity, and Linear Functionals#^ex-3-2|§3.2]]). The Riesz representation theorem says the same is true in any Hilbert space, once “linear functional” is replaced by the right notion.

> [!definition] Definition §26.1: Bounded Linear Functional
> Let $(X, \|\cdot\|)$ be a normed linear space over $\mathbb{F}$. A linear functional $\ell : X \to \mathbb{F}$ is **bounded** if there is a constant $c > 0$ such that
>
> $$
> |\ell(x)| \le c\,\|x\| \qquad \text{for all } x \in X .
> $$
>
> *Lax: §6.3, (14)*

^def-26-1

> [!example] Example §26.1: Linear Functionals on $\mathbb{R}^n$ are Bounded
> Give $\mathbb{R}^n$ the Euclidean norm $\|x\| = (x \cdot x)^{1/2}$. By Example [[§3 Linear Maps, Convexity, and Linear Functionals#^ex-3-2|§3.2]] every linear functional on $\mathbb{R}^n$ is $\ell(x) = a \cdot x$ for some $a \in \mathbb{R}^n$. We show $\ell$ is bounded. By Cauchy–Schwarz (Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], for the dot product),
>
> $$
> |\ell(x)| = |a \cdot x| \le \|a\|\,\|x\| \qquad \text{for all } x \in \mathbb{R}^n ,
> $$
>
> so $c = \|a\|$ works in Definition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|§26.1]] when $a \neq 0$ (and any $c > 0$ works when $a = 0$).

^ex-26-1

> [!theorem] Proposition §26.1: Linear Functionals on Finite-Dimensional Spaces are Bounded
> Every linear functional on a finite-dimensional normed linear space is bounded.

^prop-26-1

> [!proof]+ Proof
> Let $X$ be finite-dimensional with norm $\|\cdot\|$ and $\ell$ a linear functional on $X$. If $X = \{0\}$, any $c > 0$ works. Otherwise let $e_1, \ldots, e_n$ be a basis, and for $x = \sum_i a_i e_i$ put $\|x\|_1 = \sum_i |a_i|$. By linearity and the triangle inequality in $\mathbb{F}$,
>
> $$
> |\ell(x)| = \Bigl| \sum_i a_i\, \ell(e_i) \Bigr| \le \sum_i |a_i|\,|\ell(e_i)| \le \Bigl( \max_i |\ell(e_i)| \Bigr) \|x\|_1 .
> $$
>
> By Theorem [[§14 New Normed Spaces from Old#^thm-14-4|§14.4]], $\|\cdot\|_1$ is equivalent to the given norm, so $\|x\|_1 \le C\|x\|$ for some $C$ and all $x$. Hence $|\ell(x)| \le c\,\|x\|$ with $c = \max\bigl\{ C \max_i |\ell(e_i)|,\, 1 \bigr\} > 0$.

^pf-26-1

*Uses:* [[§14 New Normed Spaces from Old#^thm-14-4|§14.4]]

> [!example] Example §26.2: An Unbounded Linear Functional
> *(Not from lecture; filled in.)* Let $X$ be an infinite-dimensional normed linear space over $\mathbb{F}$. We construct a linear functional on $X$ that is not bounded.
>
> *A Hamel basis.* Let $P$ be the set of linearly independent subsets of $X$, ordered by inclusion. $P \neq \varnothing$ since $\varnothing \in P$, and the union of a nonempty chain in $P$ lies in $P$, because each finite subset of the union lies in a single member of the chain and is therefore independent; the empty chain has the upper bound $\varnothing$. By Zorn's lemma (Theorem [[§6 Proof of the Hahn–Banach Theorem#^thm-6-2|§6.2]]) $P$ has a maximal element $B$. $B$ spans $X$: if some $x \in X$ were not a finite linear combination of elements of $B$, then $B \cup \{x\}$ would be independent, contradicting maximality. So every $x \in X$ is, uniquely, a finite combination $x = \sum_{b \in B} x_b\, b$ with $x_b \in \mathbb{F}$, all but finitely many equal to $0$. (This is the argument of Example [[§24 The Parallelogram Law and Jordan–von Neumann#^ex-24-1|§24.1]], with $X$ over $\mathbb{F}$ in place of $\mathbb{R}$ over $\mathbb{Q}$.)
>
> *$B$ is infinite.* Otherwise $X = \operatorname{span} B$ would be finite-dimensional. Choose distinct elements $b_1, b_2, \ldots$ of $B$. Each $b_k \neq 0$, since $0$ lies in no linearly independent set.
>
> *The functional.* For $x = \sum_{b \in B} x_b\, b$ put
>
> $$
> \ell(x) = \sum_{k=1}^\infty k\,\|b_k\|\, x_{b_k} ,
> $$
>
> a finite sum, because only finitely many coefficients $x_b$ are nonzero. Adding the expansions of $x$ and $y$ gives an expansion of $x + y$, and multiplying the expansion of $x$ by $a \in \mathbb{F}$ gives an expansion of $ax$; by uniqueness, $(x + y)_b = x_b + y_b$ and $(ax)_b = a\,x_b$ for every $b \in B$. Hence $\ell$ is linear. The expansion of $b_k$ is $b_k$ itself, so $\ell(b_k) = k\,\|b_k\|$.
>
> *$\ell$ is not bounded.* If there were $c > 0$ with $|\ell(x)| \le c\,\|x\|$ for all $x \in X$, then $k\,\|b_k\| = |\ell(b_k)| \le c\,\|b_k\|$, so $k \le c$ for every $k \in \mathbb{N}$, which is impossible. So $\ell$ is not bounded (Definition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|§26.1]]).

^ex-26-2

> [!remark] Remark: Why Boundedness
> In finite dimensions every linear functional is bounded (Example [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^ex-26-1|§26.1]], Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]). In infinite dimensions this fails: every infinite-dimensional normed linear space has linear functionals, built from a Hamel basis, that are not bounded (Example [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^ex-26-2|§26.2]]). So boundedness is a genuine hypothesis, and it is the one that makes the finite-dimensional picture survive. “Bounded” does not mean bounded as a function: a nonzero linear functional is never bounded on all of $X$, since $\ell(nx) = n\ell(x)$; it means bounded on the unit ball.

^rem-26-1

> [!remark]- Connections
> - The general notion for maps between normed spaces: [[§30 Boundedness and Continuity#^def-30-2|Def. §30.2]]; the dual space of bounded functionals: [[§31 Dual Spaces#^def-31-1|Def. §31.1]].

> [!theorem] Proposition §26.2: Bounded Means Continuous
> For a linear functional $\ell$ on a normed linear space $X$, the following are equivalent:
> - (i) $\ell$ is bounded;
> - (ii) $\ell$ is continuous on $X$ (if $x_n \to x$ then $\ell(x_n) \to \ell(x)$);
> - (iii) $\ell$ is continuous at $0$.

^prop-26-2

> [!proof]+ Proof
> (Not covered in lecture.) (i)$\Rightarrow$(ii): $|\ell(x_n) - \ell(x)| = |\ell(x_n - x)| \le c\|x_n - x\| \to 0$. (ii)$\Rightarrow$(iii) is trivial. (iii)$\Rightarrow$(i): if $\ell$ is not bounded, then for each $n$ there is $x_n$ with $|\ell(x_n)| > n\|x_n\|$, so $x_n \neq 0$; put $z_n = x_n / (n\|x_n\|)$. Then $\|z_n\| = 1/n \to 0$, so $z_n \to 0$, while $|\ell(z_n)| = |\ell(x_n)| / (n\|x_n\|) > 1$, so $\ell(z_n) \not\to 0 = \ell(0)$, contradicting (iii).

^pf-26-2

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]], [[§11 Normed Linear Spaces#^def-11-4|Def. §11.4]]

> [!remark]- Connections
> - The same statement for linear maps, proved again in Chapter 6: [[§30 Boundedness and Continuity#^prop-30-2|§30.2]].

## The Riesz Representation Theorem

The idea of the proof of the Riesz representation theorem (Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]] below) comes from $\mathbb{R}^n$: there $\ell(x) = x \cdot a$, the set $\{\ell = 0\}$ is a hyperplane, and $a$ is a normal vector to it. So one studies the null set of $\ell$ and looks for a vector perpendicular to it. Two facts about the null set are needed first; they are separated out as lemmas.

> [!definition] Definition §26.2: Kernel of a Linear Functional
> Let $\ell$ be a linear functional on a linear space $X$ over $\mathbb{F}$. The **kernel** (or null set) of $\ell$ is
>
> $$
> \ker \ell = \{ y \in X : \ell(y) = 0 \} .
> $$

^def-26-2

> [!theorem] Lemma §26.3: The Kernel of a Bounded Functional is Closed
> Let $\ell$ be a bounded linear functional on a normed linear space $X$. Then its kernel (Definition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-2|§26.2]])
>
> $$
> N = \ker \ell = \{ y \in X : \ell(y) = 0 \}
> $$
>
> is a closed linear subspace of $X$.

^lem-26-3

> [!proof]+ Proof
> *Subspace.* If $y_1, y_2 \in N$ and $a, b \in \mathbb{F}$, then $\ell(ay_1 + by_2) = a\ell(y_1) + b\ell(y_2) = 0$.
>
> *Closed.* Let $y_n \in N$ with $y_n \to y_0$. Since $\ell$ is bounded, $|\ell(x)| \le c\,\|x\|$ for some $c > 0$ and all $x$ (Definition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|§26.1]]), so
>
> $$
> |\ell(y_n) - \ell(y_0)| = |\ell(y_n - y_0)| \le c\,\|y_n - y_0\| \to 0 .
> $$
>
> As $\ell(y_n) = 0$ for all $n$, this gives $\ell(y_0) = 0$, i.e. $y_0 \in N$.

^pf-26-3

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§11 Normed Linear Spaces#^def-11-6|Def. §11.6]], [[§11 Normed Linear Spaces#^prop-11-6|§11.6]]

This is the only place in the proof where boundedness is used; by Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|§26.2]] it amounts to continuity of $\ell$.

> [!theorem] Lemma §26.4: The Kernel Has Codimension One
> Let $H$ be a Hilbert space, $\ell \neq 0$ a bounded linear functional on $H$, and $N = \ker \ell$. Then $N^\perp \neq \{0\}$, and for every nonzero $x_0 \in N^\perp$:
> - (a) $\ell(x_0) \neq 0$;
> - (b) $N^\perp = \{ k x_0 : k \in \mathbb{F} \}$, so $N^\perp$ is one-dimensional;
> - (c) every $x \in H$ can be written as $x = k x_0 + y$ with $k = \ell(x)/\ell(x_0) \in \mathbb{F}$ and $y \in N$.
>
> *Lax: §6.3, Lemma 5(i)*

^lem-26-4

> [!proof]+ Proof
> By Lemma [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]], $N$ is a closed linear subspace, and $N \neq H$ because $\ell \neq 0$. By Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]], $H = N \oplus N^\perp$; if $N^\perp$ were $\{0\}$ this would give $H = N$. So $N^\perp \neq \{0\}$. Fix $0 \neq x_0 \in N^\perp$.
>
> (a) If $\ell(x_0) = 0$ then $x_0 \in N \cap N^\perp = \{0\}$ (a vector orthogonal to itself is $0$), contrary to the choice of $x_0$.
>
> (b) Let $x_1 \in N^\perp$ and put $k = \ell(x_1)/\ell(x_0)$, a quotient of two scalars, so $k \in \mathbb{F}$. Then $\ell(x_1) = k\,\ell(x_0)$, so $\ell(x_1 - k x_0) = 0$ and $x_1 - k x_0 \in N$. But also $x_1 - k x_0 \in N^\perp$, a linear subspace (Proposition [[§25 Projection and Orthogonal Decomposition#^prop-25-3|§25.3]]). Hence $x_1 - k x_0 \in N \cap N^\perp = \{0\}$, i.e. $x_1 = k x_0$. Conversely every $k x_0$ lies in $N^\perp$.
>
> (c) With $k = \ell(x)/\ell(x_0)$ and $y = x - k x_0$, linearity gives $\ell(y) = \ell(x) - k\,\ell(x_0) = 0$, so $y \in N$.

^pf-26-4

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]], [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]], [[§25 Projection and Orthogonal Decomposition#^prop-25-3|§25.3]], [[§25 Projection and Orthogonal Decomposition#^def-25-1|Def. §25.1]], [[§25 Projection and Orthogonal Decomposition#^def-25-2|Def. §25.2]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]]

> [!remark] Remark
> Two points. The step $k = \ell(x_1)/\ell(x_0)$ may look like dividing vectors, but it is not: $\ell(x_1)$ and $\ell(x_0)$ are numbers, and the vector identity $x_1 = kx_0$ is obtained afterwards from $N \cap N^\perp = \{0\}$. And the argument shows $\dim N^\perp = 1$ because an arbitrary element $x_1$ of $N^\perp$ was shown to be a multiple of one fixed nonzero $x_0$.

^rem-26-2

> [!theorem] Theorem §26.5: Riesz Representation Theorem
> Let $H$ be a Hilbert space over $\mathbb{F}$.
> - (1) For every $a \in H$, the map $\ell_a : H \to \mathbb{F}$, $\ell_a(x) = (x, a)$, is a bounded linear functional on $H$.
> - (2) Conversely, for every bounded linear functional $\ell : H \to \mathbb{F}$ there is a unique $a \in H$ such that
>
> $$
> \ell(x) = (x, a) \qquad \text{for all } x \in H .
> $$
>
> *Lax: §6.3, Thm 4*

^thm-26-5

> [!proof]+ Proof of (1)
> Linearity of $\ell_a$ in $x$ is linearity of the inner product in its first argument. Boundedness is Cauchy–Schwarz (Theorem [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]]): $|\ell_a(x)| = |(x, a)| \le \|a\|\,\|x\|$, so $c = \|a\|$ works.

^pf-26-5

*Uses:* [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]]

> [!proof]+ Proof of (2)
> If $\ell = 0$, then $\ell(x) = (x, 0)$ for all $x$, so $a = 0$ works. Assume $\ell \neq 0$, let $N = \ker \ell$, and fix $0 \neq x_0 \in N^\perp$ (Lemma [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-4|§26.4]]).
>
> *Finding $a$.* Consider the bounded linear functional $\ell_1(x) = (x, x_0)$. For $x = k x_0 + y$ as in Lemma [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-4|§26.4]](c),
>
> $$
> \ell_1(x) = k(x_0, x_0) + (y, x_0) = k\,\|x_0\|^2, \qquad \ell(x) = k\,\ell(x_0) + \ell(y) = k\,\ell(x_0),
> $$
>
> since $(y, x_0) = 0$ ($y \in N$, $x_0 \in N^\perp$) and $\ell(y) = 0$. The two differ by the constant factor $\ell(x_0)/\|x_0\|^2$. This suggests
>
> $$
> a = \frac{\overline{\ell(x_0)}}{\|x_0\|^2}\, x_0 ,
> $$
>
> the conjugate being needed because the inner product is conjugate-linear in its second argument.
>
> *Verification.* For $x = k x_0 + y$ as above, using $(x, c\,x_0) = \bar{c}\,(x, x_0)$,
>
> $$
> (x, a) = \frac{\ell(x_0)}{\|x_0\|^2}\,(k x_0 + y,\, x_0) = \frac{\ell(x_0)}{\|x_0\|^2}\, k\,\|x_0\|^2 = k\,\ell(x_0) = \ell(x).
> $$
>
> *Uniqueness.* If $(x, a) = (x, a')$ for all $x \in H$, then $(x, a - a') = 0$ for all $x$; taking $x = a - a'$ gives $\|a - a'\|^2 = 0$, so $a = a'$. (Not written out in lecture.)

^pf-26-5-2

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-4|§26.4]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^pf-26-5|§26.5 (1)]], [[§25 Projection and Orthogonal Decomposition#^def-25-1|Def. §25.1]], [[§25 Projection and Orthogonal Decomposition#^def-25-2|Def. §25.2]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]]

> [!remark]- Connections
> - The finite-dimensional home: [[Riesz representation theorem|LADR 6.42]], revisited through orthogonal projection in [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]].
> - The map $a \mapsto \ell_a$ as an isometry onto the dual, and its bra–ket reading: [[§44 Bras, Kets, and the Riesz Map#^thm-44-1|§44.1]].

![[m556-19-1.svg]]
*The kernel $N$, the line $N^\perp$ spanned by $x_0$ (red), and the decomposition $x = kx_0 + y$ that locates $x$ on the level set $\{\ell = \ell(x)\}$ (dashed): $\ell(x)$ sees only the $N^\perp$-component $kx_0$. The representing vector $a$ (blue) is the multiple of $x_0$ normal to $N$.*

![[m556-19-a1.gif|420]]

*(Not from lecture; animation added, vault only.)* $\ell(x) = (x, x_0)$ for $x_0 = (1.2, 0.6)$ (chosen for the picture), with $N = \ker\ell$ (blue). As $x$ moves, it splits as $x = kx_0 + y$ with $y \in N$; $\ell(x)$ depends only on $k$, and the level set $\{\ell = \ell(x)\}$ through $x$ (dashed) is the line parallel to $N$.

The null set $N$ is a closed hyperplane and $N^\perp$ a line; $a$ is a normal vector to $N$, a multiple of $x_0$. The level sets $\{\ell = c\}$ are the translates of $N$, and $\ell(x)$ records only which translate $x$ lies on, i.e. the $N^\perp$-component $kx_0$ of $x$.

> [!remark] Remark: Reading the Statement
> Part (1) is the easy direction and holds in any inner product space. Part (2) is the content: on a Hilbert space there are *no other* bounded linear functionals than the ones given by inner products, exactly as on $\mathbb{R}^n$ (Example [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^ex-26-3|§26.3]] spells this out for $L^2$). The vector is on the *second* slot because the functional must be linear in $x$, and the inner product is linear in its first argument; with the physicists' convention it would be $(a, x)$.

^rem-26-3

> [!example] Example §26.3: Bounded Linear Functionals on $L^2$
> Let $\Omega \subset \mathbb{R}^n$ be a domain. Every bounded linear functional $\ell$ on $L^2(\Omega)$ is of the form
>
> $$
> \ell(f) = \int_\Omega f(x)\, \overline{g(x)}\, dx \qquad (f \in L^2(\Omega))
> $$
>
> for a unique $g \in L^2(\Omega)$; conversely every such formula defines a bounded linear functional. Indeed $L^2(\Omega)$ with $(f, g) = \int_\Omega f \bar g$ (Example [[§22 Definition and Examples#^ex-22-3|§22.3]]) is a Hilbert space (Example [[§23 Cauchy–Schwarz and the Induced Norm#^ex-23-1|§23.1]]), so Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]](2) gives a unique $g$ with $\ell(f) = (f, g) = \int_\Omega f \bar g$ for all $f$, and Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]](1) gives the converse.

^ex-26-3

> [!remark] Remark
> On method: when proving a big theorem, the simple examples from linear algebra very often give the answer, so start with simple examples and go from there. Here the finite-dimensional picture dictated both the object to study ($\ker \ell$) and the candidate ($a$ normal to it); the analysis consisted of making the orthogonal decomposition available, which is where completeness of $H$ and boundedness of $\ell$ enter.

^rem-26-4

> [!remark] Remark: Comparison with Lax
> Lax proves the representation theorem through his Lemma 5: the null space of a nonzero functional has codimension one, and two functionals with the same null space are proportional. He takes $z \neq 0$ in $N^\perp$ and observes that $\ell$ and $x \mapsto (x, z)$ have the same null space, so $\ell$ is a multiple of $(\cdot, z)$. The proof in lecture (Lemma [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-4|§26.4]] and the explicit decomposition $x = kx_0 + y$) is the same argument with the proportionality constant computed by hand.

^rem-26-5

> [!theorem] Proposition §26.6: Minimizing a Quadratic Functional over a Closed Convex Set
> Let $H$ be a [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Hilbert space]] over $\mathbb{R}$, $\ell \in H'$ ([[§31 Dual Spaces#^def-31-1|dual space]]), $K$ a nonempty [[§11 Normed Linear Spaces#^def-11-6|closed]] [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-3|convex]] subset of $H$, and
>
> $$
> f(v) = \frac12 \|v\|^2 - \ell(v) \qquad (v \in K).
> $$
>
> - (a) There is $u^{\ast} \in H$ with $f(v) = \frac12 \|u^{\ast} - v\|^2 - \frac12 \|u^{\ast}\|^2$ for all $v \in K$.
> - (b) There is a unique $u_0 \in K$ with $f(u_0) = \inf_{v \in K} f(v)$: the point of $K$ closest to $u^{\ast}$ ([[§25 Projection and Orthogonal Decomposition#^thm-25-2|Theorem §25.2]]).
>
> *Source: HW5, Problem 3*

^prop-26-6

> [!proof]+ Proof
> (HW5, Problem 3.) **(a)** By the Riesz representation theorem (Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]]) there is $u^{\ast} \in H$ with $\ell(v) = (v, u^{\ast})$ for all $v \in H$. Since $H$ is real, $(u^{\ast}, v) = (v, u^{\ast})$, and for every $v \in K$
>
> $$
> \frac12 \|u^{\ast} - v\|^2 - \frac12 \|u^{\ast}\|^2 = \frac12 \bigl( \|u^{\ast}\|^2 - 2(v, u^{\ast}) + \|v\|^2 \bigr) - \frac12 \|u^{\ast}\|^2 = \frac12 \|v\|^2 - (v, u^{\ast}) = f(v).
> $$
>
> **(b)** *Existence.* Let $d = \inf_{v \in K} \|u^{\ast} - v\|$. By Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-2|§25.2]] there is a unique $u_0 \in K$ with $\|u^{\ast} - u_0\| = d$. For every $v \in K$, $\|u^{\ast} - v\| \ge d \ge 0$, so $\|u^{\ast} - v\|^2 \ge \|u^{\ast} - u_0\|^2$, and by (a)
>
> $$
> f(v) = \frac12 \|u^{\ast} - v\|^2 - \frac12 \|u^{\ast}\|^2 \ge \frac12 \|u^{\ast} - u_0\|^2 - \frac12 \|u^{\ast}\|^2 = f(u_0).
> $$
>
> Since $u_0 \in K$, $f(u_0) = \inf_{v \in K} f(v)$.
>
> *Uniqueness.* Let $u_1 \in K$ with $f(u_1) = f(u_0)$. By (a), $\|u^{\ast} - u_1\|^2 = \|u^{\ast} - u_0\|^2 = d^2$, so $\|u^{\ast} - u_1\| = d$: $u_1$ is also a point of $K$ closest to $u^{\ast}$, and $u_1 = u_0$ by the uniqueness in Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-2|§25.2]].

^pf-26-6

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]], [[§25 Projection and Orthogonal Decomposition#^thm-25-2|§25.2]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Def. §23.1]]

> [!theorem] Corollary §26.7: Variational Form of the Riesz Representation Theorem
> *(Not from lecture.)* Let $H$ be a Hilbert space over $\mathbb{R}$ and $\ell \in H'$, with Riesz representer $u^{\ast}$: $\ell(v) = (v, u^{\ast})$ for all $v \in H$ (Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]]). Then $u^{\ast}$ is the unique minimizer over $H$ of $f(v) = \frac12\|v\|^2 - \ell(v)$.

^cor-26-7

> [!proof]+ Proof
> $K = H$ is nonempty, closed and convex, so Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-6|§26.6]] applies, with the $u^{\ast}$ of part (a) the Riesz representer (as in its proof). By part (b), $f$ has a unique minimizer over $H$, namely the point of $H$ closest to $u^{\ast}$. Since $u^{\ast} \in H$ and $\|u^{\ast} - u^{\ast}\| = 0$, that point is $u^{\ast}$.

^pf-26-7

*Uses:* [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-6|§26.6]]

> [!remark] Remark
> The proof of Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-6|§26.6]] is “complete the square”: adding and subtracting $\frac12\|u^{\ast}\|^2$ turns the minimization of $f$ into the minimization of a distance, which is the [[§25 Projection and Orthogonal Decomposition#^thm-25-2|projection theorem]]. For $K = H$ the minimizer is $u^{\ast}$ itself (Corollary [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^cor-26-7|§26.7]]), so minimizing $\frac12\|v\|^2 - \ell(v)$ over $H$ produces the Riesz representer of $\ell$ — the variational form of the [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|Riesz representation theorem]], and the prototype of Dirichlet's principle. For a proper $K$ the minimizer is the projection of $u^{\ast}$ onto $K$, the starting point of variational inequalities (obstacle problems).

^rem-26-6

> [!remark]- Connections
> - Finite-dimensional counterpart, minimizing the distance to a subspace: [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]].
> - The pattern as a technique: [[Functional Analysis Problem-Solving Techniques#^rem-t17|Technique 17]].

![[m556-19-2.svg]]
*Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-6|§26.6]] in one picture: the closed convex set $K$ (blue), the Riesz representer $u^\ast$ of $\ell$ (grey arrow from $0$), and the level sets of $f(v) = \tfrac12\|u^\ast - v\|^2 - \tfrac12\|u^\ast\|^2$, which are circles centred at $u^\ast$ (dashed). The small circles miss $K$ and the large one cuts it; the red circle $\{f = f(u_0)\}$ is the first to touch $K$, at the minimizer $u_0$ — the point of $K$ closest to $u^\ast$ ([[§25 Projection and Orthogonal Decomposition#^thm-25-2|projection theorem]]) — and the red segment from $u^\ast$ to $u_0$ is perpendicular to the supporting line of $K$ at $u_0$ (grey). For $K = H$ the minimizer would be $u^\ast$ itself ([[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^rem-26-6|remark]]). (Drawn for these notes in the vault; not in the course tex.)*
