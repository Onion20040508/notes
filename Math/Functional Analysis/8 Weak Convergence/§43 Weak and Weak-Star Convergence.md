---
type: section
subject: "[[Functional Analysis]]"
chapter: 8
section: 43
tags: [functional-analysis, math556]
---
← [[§42 Uniform Boundedness and Approximation]] · ↑ [[· 8 Weak Convergence]] · [[§44 Bras, Kets, and the Riesz Map]] →

*Stage: maps — Thread: functionals. Convergence tested against $X'$ (weak) or against $X$ (weak-$\ast$); Banach–Steinhaus gives the working criteria, Hahn–Banach the uniqueness, the norm bound and Mazur's theorem.*

*Lecture 18 (Thu Nov 5). Sources: the handwritten notes of the lecture and the Otter.ai transcript. The order is the lecture's, except that the hyperplane separation theorem in normed spaces now precedes Mazur's theorem, whose proof uses it.*

## Definitions

Recall that the closed unit ball in $\mathbb{R}^n$ is compact, while the closed unit ball of an infinite-dimensional normed linear space is not (Theorem [[§20 Compactness and the Unit Ball#^thm-20-5|§20.5]]); this is one of the main differences between finite and infinite dimensions. It is always useful to extract a convergent subsequence from a bounded sequence. Since this is impossible in general, one weakens the notion of convergence instead. This is the motivation for weak convergence.

> [!definition] Definition §43.1: Weak and Strong Convergence
> Let $X$ be a normed linear space, $\{x_n\}_{n=1}^\infty$ a sequence in $X$ and $x_0 \in X$.
>
> 1. $\{x_n\}$ **converges weakly** to $x_0$ if for every $\ell \in X'$,
>
> $$
> \lim_{n \to \infty} \ell(x_n) = \ell(x_0) .
> $$
>
> We write $\mathop{\text{w-lim}}_{n \to \infty} x_n = x_0$, or $x_n \rightharpoonup x_0$ as $n \to \infty$.
> 2. $\{x_n\}$ **converges strongly** to $x_0$ if $\lim_{n \to \infty} \|x_n - x_0\| = 0$. We write $\mathop{\text{s-lim}}_{n \to \infty} x_n = x_0$, or simply $\lim_{n \to \infty} x_n = x_0$, or $x_n \to x_0$.
>
> *Lax: Ch. 10, definition at the start of the chapter*

^def-43-1

“Converges” without qualification means strongly, i.e. in norm.

> [!theorem] Proposition §43.1: Basic Properties of Weak Limits
> Let $X$ be a normed linear space.
>
> 1. If $\mathop{\text{s-lim}}_{n \to \infty} x_n = x_0$, then $\mathop{\text{w-lim}}_{n \to \infty} x_n = x_0$.
> 2. If $x_n \rightharpoonup x_0$ and $x_n \rightharpoonup z_0$, then $x_0 = z_0$: weak limits are unique.
>
> *Lax: Ch. 10, the remark after the definition (part (1))*

^prop-43-1

> [!proof]+ Proof
> (1) For every $\ell \in X'$,
>
> $$
> |\ell(x_n) - \ell(x_0)| = |\ell(x_n - x_0)| \le \|\ell\|\, \|x_n - x_0\| \to 0 \qquad (n \to \infty),
> $$
>
> so $x_n \rightharpoonup x_0$.
>
> (2) If $x_n \rightharpoonup x_0$ and $x_n \rightharpoonup z_0$, then for every $\ell \in X'$
>
> $$
> \ell(x_0 - z_0) = \ell(x_0) - \ell(z_0) = \lim_{n \to \infty} \bigl( \ell(x_n) - \ell(x_n) \bigr) = 0 .
> $$
>
> For every $x \in X$, $\|x\| = \max_{\ell \in X',\ \|\ell\| \le 1} |\ell(x)|$ (Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]], a consequence of Hahn–Banach). Hence
>
> $$
> \|x_0 - z_0\| = \max_{\ell \in X',\ \|\ell\| \le 1} |\ell(x_0 - z_0)| = 0 .
> $$
>
> If a sequence could converge weakly to two different limits, the notion would make no sense.

^pf-43-1

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]

## Examples

> [!example] Example §43.1: Weak but Not Strong Convergence in $\ell^2$
> In $\ell^2 = \{ a = (a_1, a_2, \ldots) : \sum_{j=1}^\infty |a_j|^2 < \infty \}$ let $e_n = (0, \ldots, 0, 1, 0, \ldots)$, with $1$ in the $n$-th place; $\|e_n\|_{\ell^2} = 1$. Claim: $e_n \rightharpoonup 0$ in $\ell^2$, but $\{e_n\}$ does not converge strongly.
>
> Indeed, $(\ell^2)' = \ell^2$: every $\ell \in (\ell^2)'$ is $\ell(x) = (x, a)$ for some $a = (a_1, a_2, \ldots) \in \ell^2$ (Riesz representation). Then $(e_n, a) = \overline{a_n}$, and $\sum_n |a_n|^2 < \infty$ forces $a_n \to 0$ as $n \to \infty$ (the terms of a convergent series tend to $0$). So $\ell(e_n) \to 0 = \ell(0)$. If $\{e_n\}$ converged strongly to some $x$, then by Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-1|§43.1]] it would also converge weakly to $x$, so $x = 0$ by uniqueness; but $\|e_n - 0\| = 1$ for all $n$.
>
> *Lax: Ch. 10, Example 1 (left as an exercise there)*

^ex-43-1

The same holds in any Hilbert space, by an abstract argument.

> [!theorem] Proposition §43.2: Orthonormal Sequences Converge Weakly to $0$
> Let $H$ be a Hilbert space and $\{e_n\}_{n=1}^\infty$ an orthonormal sequence in $H$ (not necessarily a basis). Then $e_n \rightharpoonup 0$ as $n \to \infty$.
>
> *Lax: Ch. 10, Example 2*

^prop-43-2

> [!proof]+ Proof
> By Bessel's inequality (Theorem [[§27 Orthonormal Sets and Bases#^thm-27-5|§27.5]]), for every $x \in H$
>
> $$
> \sum_{n=1}^\infty |(x, e_n)|^2 \le \|x\|^2 < \infty ,
> $$
>
> so $(x, e_n) \to 0$ as $n \to \infty$ for every $x \in H$. Since $H' = H$ (every $\ell \in H'$ is $\ell(y) = (y, x)$ for some $x \in H$, and $(e_n, x) = \overline{(x, e_n)}$), $\ell(e_n) \to 0$ for every $\ell \in H'$, i.e. $e_n \rightharpoonup 0$.

^pf-43-2

*Uses:* [[§27 Orthonormal Sets and Bases#^thm-27-5|§27.5]]

> [!example] Example §43.2: $\sin(mx) \rightharpoonup 0$ in $L^2[0, 2\pi]$
> In $L^2([0, 2\pi])$ the functions $f_m(x) = \frac{1}{\sqrt\pi} \sin(mx)$, $m = 1, 2, \ldots$, form an orthonormal set (left to the class).
> (For $m, k \ge 1$, $\int_0^{2\pi} \sin(mx) \sin(kx)\, dx = \frac12 \int_0^{2\pi} \bigl( \cos((m-k)x) - \cos((m+k)x) \bigr) dx$, which is $0$ for $m \neq k$ and $\pi$ for $m = k$.) By Proposition [[§43 Weak and Weak-Star Convergence#^prop-43-2|§43.2]], for every $g \in L^2([0, 2\pi])$
>
> $$
> \lim_{m \to \infty} \int_0^{2\pi} \sin(mx)\, g(x)\, dx = 0 ,
> $$
>
> i.e. $\sin(mx) \rightharpoonup 0$ in $L^2([0, 2\pi])$; the factor $\frac{1}{\sqrt\pi}$ does not matter for convergence to $0$. (Whether or not $g$ is conjugated in the integral makes no difference, since $g$ runs over all of $L^2$ exactly when $\bar g$ does.) The functions oscillate faster and faster without settling down, and $\|\sin(mx)\|_{L^2} = \sqrt\pi$ for every $m$, so there is no strong convergence; but against any fixed $g$ the positive and negative parts cancel more and more.

^ex-43-2

![[m556-43-1.svg]]

![[m556-43-2.svg]]

Why $\sin(mx) \rightharpoonup 0$: the product $g(x) \sin(mx)$ for the test function $g(x) = \frac{x}{2\pi}$ (dashed: $\pm g$), with the positive part blue and the negative part red. As $m$ grows, each blue lobe is followed by a red lobe of almost the same area, and the integral, here exactly $-\frac1m$, tends to $0$; meanwhile $\|\sin(mx)\|_{L^2} = \sqrt\pi$ for every $m$.

![[m556-43-a1.gif|440]]

*(Not from lecture; animation added, vault only.)* The same test function $g(x) = \frac{x}{2\pi}$ against $\sin(mx)$ for $m = 1, 2, \ldots, 30$. Left: $g(x) \sin(mx)$ with its positive part blue and negative part red; right: the integral $\int_0^{2\pi} g(x) \sin(mx)\, dx = -\frac1m$, one dot per $m$. The oscillations do not shrink, but their net area does.

## Criteria and the Norm of a Weak Limit

> [!theorem] Theorem §43.3: Criterion for Weak Convergence
> Let $X$ be a normed linear space, $\{x_n\}_{n=1}^\infty \subset X$ and $x_0 \in X$. Then $x_n \rightharpoonup x_0$ in $X$ if and only if
>
> 1. $\sup_n \|x_n\| < \infty$, and
> 2. $\lim_{n \to \infty} \ell(x_n) = \ell(x_0)$ for all $\ell \in D$, where $D$ is a dense subset of $X'$.
>
> *Lax: §10.1, Thm 1 (the direction $\Leftarrow$, Exercise 3) and Thm 4$'$ (weakly convergent sequences are bounded)*

^thm-43-3

> [!proof]+ Proof
> This is Banach–Steinhaus (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-4|§42.4]]). Think of $x_n$ not as an element of $X$ but as an element of the dual of $X'$: $x_n \in (X')' = \mathcal{L}(X', \mathbb{F})$, via $x_n(\ell) = \langle x_n, \ell \rangle = \ell(x_n)$. So $\{x_n\}$ is a sequence of bounded linear maps from $X'$ to $\mathbb{F}$, and
> $X'$ is a Banach space even if $X$ is not (Corollary [[§31 Dual Spaces#^cor-31-1|§31.1]]), while $\mathbb{F}$ is a normed space. The norm of $x_n$ as an element of $(X')'$ is $\|x_n\|$ (Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]), and $x_0$ is the candidate limit map $A \in \mathcal{L}(X', \mathbb{F})$. Weak convergence says: for all $\ell \in X'$, $\ell(x_n) = \langle x_n, \ell \rangle \to \langle x_0, \ell \rangle$, i.e. the maps $x_n$ converge pointwise on $X'$ to $x_0$. Banach–Steinhaus says this happens if and only if (1) $\sup_n \|x_n\| < \infty$ and (2) the convergence holds for all $\ell$ in a dense subset $D \subset X'$.

^pf-43-3

*Uses:* [[§42 Uniform Boundedness and Approximation#^thm-42-4|§42.4]], [[§31 Dual Spaces#^cor-31-1|§31.1]], [[§37 Separable Duals and Reflexive Spaces#^prop-37-5|§37.5]]

> [!theorem] Theorem §43.4: The Norm of a Weak Limit
> Let $X$ be a normed linear space, $\{x_n\}_{n=1}^\infty \subset X$, $x_0 \in X$, and $x_n \rightharpoonup x_0$ in $X$. Then $\{x_n\}$ is a bounded sequence, and
>
> $$
> \|x_0\| \le \liminf_{n \to \infty} \|x_n\| .
> $$
>
> *Lax: §10.1, Thms 4$'$ and 5*

^thm-43-4

> [!proof]+ Proof
> *Bounded:* this is part (1) of Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-3|§43.3]], i.e. the uniform boundedness principle applied to the $x_n \in \mathcal{L}(X', \mathbb{F})$, which are pointwise bounded because each $\{\ell(x_n)\}$ converges. Just as every convergent sequence is bounded, every weakly convergent sequence is bounded.
>
> *The norm bound.* Since $x_n \rightharpoonup x_0$, for every $\ell \in X'$ we have $\ell(x_0) = \lim_n \ell(x_n)$, hence $|\ell(x_0)| = \lim_n |\ell(x_n)|$. Also $|\ell(x_n)| \le \|\ell\|\, \|x_n\|$. Take the $\liminf$ on both sides: the left side has a limit, equal to $|\ell(x_0)|$; the right side may not have a limit, but the $\liminf$ always makes sense. So
>
> $$
> |\ell(x_0)| = \lim_{n \to \infty} |\ell(x_n)| = \liminf_{n \to \infty} |\ell(x_n)| \le \|\ell\| \liminf_{n \to \infty} \|x_n\| .
> $$
>
> Now take the supremum over all $\ell \in X'$ with $\|\ell\| \le 1$: by Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]] the left side becomes $\|x_0\|$, so
>
> $$
> \|x_0\| = \sup_{\ell \in X',\ \|\ell\| \le 1} |\ell(x_0)| \le \liminf_{n \to \infty} \|x_n\| .
> $$

^pf-43-4

*Uses:* [[§43 Weak and Weak-Star Convergence#^thm-43-3|§43.3]], [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]

In Example [[§43 Weak and Weak-Star Convergence#^ex-43-1|§43.1]], $\|e_n\| = 1$ for all $n$ while the weak limit $0$ has norm $0$: the inequality can be strict. Norm can be lost in a weak limit, but not gained.

## Mazur's Theorem

The norm bound says how large the weak limit can be; Mazur's theorem says where it is. Its proof uses the hyperplane separation theorem of Chapter 2, in a form adapted to normed spaces, which comes first.

> [!theorem] Theorem §43.5: Hyperplane Separation in a Normed Space
> Let $X$ be a normed linear space over $\mathbb{R}$, $K$ a closed convex set in $X$, and $x_0 \notin K$. Then there exist $a \in \mathbb{R}$ and $\ell \in X'$ such that
>
> $$
> \ell(x_0) > a > \ell(x) \qquad \text{for all } x \in K .
> $$
>
> *Lax: §8.4, in the proof of Thm 17 (a ball about $x_0$ is separated from $K$ by the extended hyperplane separation theorem, Ch. 3 Thm 6)*

^thm-43-5

It is important that $\ell$ is *bounded*, and that $K$ is *closed* and convex. The version proved in Chapter 2 (Theorem [[§8 The Hyperplane Separation Theorem#^thm-8-1|§8.1]]) was for a linear space without a norm, for a convex set $K$ consisting of interior points (“open”) with $y_0 \notin K$; it produced a linear functional, not necessarily bounded. The idea of the proof: since $K$ is closed and $x_0 \notin K$, the distance from $x_0$ to $K$ is positive, so $K$ can be made slightly bigger without reaching $x_0$. Let

$$
K_\varepsilon = \{ x \in X : \text{there is } y \in K \text{ with } \|x - y\| < \varepsilon \} .
$$

Every point of $K_\varepsilon$ is an interior point, $K_\varepsilon$ is convex, and the previous theorem applies; or redo the previous proof from scratch.

![[m556-43-3.svg]]

> [!proof]+ Proof
> If $K = \varnothing$, take $\ell = 0$ and $a = -1$. Otherwise let $d = \inf_{y \in K} \|x_0 - y\|$; then $d > 0$, since otherwise there are $y_k \in K$ with $y_k \to x_0$, and $K$ closed would give $x_0 \in K$. Fix $0 < \varepsilon < d$ and define $K_\varepsilon$ as above.
>
> *$K_\varepsilon$ is convex.* If $x_1, x_2 \in K_\varepsilon$ with $\|x_i - y_i\| < \varepsilon$, $y_i \in K$, and $0 \le t \le 1$, then $y = t y_1 + (1-t) y_2 \in K$ and $\|t x_1 + (1-t) x_2 - y\| \le t\|x_1 - y_1\| + (1-t)\|x_2 - y_2\| < \varepsilon$.
>
> *Every point of $K_\varepsilon$ is interior.* If $\|x - y\| < \varepsilon$ with $y \in K$, put $\rho = \varepsilon - \|x - y\| > 0$; then $B(x, \rho) \subset K_\varepsilon$ by the triangle inequality, so $x$ is a metric interior point, hence an interior point (Proposition [[§11 Normed Linear Spaces#^prop-11-7|§11.7]]).
>
> *$x_0 \notin K_\varepsilon$,* since every point of $K_\varepsilon$ is within $\varepsilon < d$ of $K$.
>
> By Theorem [[§8 The Hyperplane Separation Theorem#^thm-8-1|§8.1]] there are a linear $\ell : X \to \mathbb{R}$ and $c_0$ with $\ell(x_0) = c_0$ and $\ell(x) < c_0$ for all $x \in K_\varepsilon$. Fix $y_1 \in K$. For $\|u\| < 1$, $y_1 + \varepsilon u \in K_\varepsilon$, so $\ell(y_1) + \varepsilon\, \ell(u) < c_0$, i.e. $\ell(u) < (c_0 - \ell(y_1))/\varepsilon =: C$ for all $\|u\| < 1$; applied to $-u$ as well, $|\ell(u)| \le C$ on the open unit ball, so $\ell$ is bounded, $\ell \in X'$. And $\ell \neq 0$, since $\ell(x_0) = c_0 > \ell(y_1)$. Now for $y \in K$ and $\|u\| < 1$, $y + \varepsilon u \in K_\varepsilon$, so $\ell(y) + \varepsilon\, \ell(u) < c_0$; taking the supremum over $\|u\| < 1$, $\ell(y) + \varepsilon \|\ell\| \le c_0$. Thus
>
> $$
> \ell(y) \le c_0 - \varepsilon \|\ell\| < c_0 - \tfrac{\varepsilon}{2} \|\ell\| =: a < c_0 = \ell(x_0) \qquad \text{for all } y \in K .
> $$

^pf-43-5

*Uses:* [[§11 Normed Linear Spaces#^prop-11-7|§11.7]], [[§8 The Hyperplane Separation Theorem#^thm-8-1|§8.1]]

> [!remark] Remark: Complex Scalars
> Over $\mathbb{C}$, apply the theorem to $X$ regarded as a real normed space: it gives a real-linear bounded $\ell_r$, and $\ell(x) = \ell_r(x) - i\, \ell_r(ix)$ is a complex-linear bounded functional with $\operatorname{Re} \ell = \ell_r$ (as in the complex Hahn–Banach theorem, Theorem [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|§9.2]]). The conclusion becomes $\operatorname{Re} \ell(x_0) > a > \operatorname{Re} \ell(x)$ for $x \in K$, and the proof of Mazur's theorem below goes through with $\operatorname{Re} \ell$.

^rem-43-1

> [!theorem] Theorem §43.6: Mazur's Theorem
> Let $X$ be a normed linear space, $\{x_n\}_{n=1}^\infty \subset X$, $x_0 \in X$, and $x_n \rightharpoonup x_0$ in $X$. Then $x_0$ belongs to the closed convex hull of $\{x_n\}_{n=1}^\infty$. That is, for every $\varepsilon > 0$ there are finitely many terms $x_1, \ldots, x_j$ of the sequence and $\lambda_k \ge 0$, $k = 1, \ldots, j$, with $\sum_{k=1}^j \lambda_k = 1$, such that
>
> $$
> \Bigl\| x_0 - \sum_{k=1}^j \lambda_k x_k \Bigr\| < \varepsilon .
> $$
>
> *Lax: §10.1, Thm 6 (for a closed convex $K$ containing the $x_n$; proved with support functions, §8.4 Thm 17)*

^thm-43-6

In other words, the weak limit can be approximated in norm by convex combinations of the terms of the sequence.
(The convex hull of $\{x_n\}$ (Definition [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-4|§3.4]]) consists of the finite convex combinations $\sum_k \lambda_k x_{n_k}$, $\lambda_k \ge 0$, $\sum_k \lambda_k = 1$: they form a convex set containing every $x_n$, and every convex set containing the $x_n$ contains them, by induction on the number of terms. The closed convex hull is the closure of this set; $x_0$ lies in it exactly when every ball about $x_0$ contains such a combination. Taking the first $j$ terms, with some $\lambda_k = 0$ allowed, loses nothing.)

> [!proof]+ Proof of Mazur's theorem
> Assume $x_n \rightharpoonup x_0$, but $x_0$ is not in the closed convex hull of $\{x_n\}$; call the closed convex hull $K$.
> ($K$ is closed by definition, and convex: if $z_k \to z$ and $w_k \to w$ with $z_k, w_k$ in the convex hull, then $t z_k + (1-t) w_k$ is in the convex hull and tends to $t z + (1-t) w$.) By the hyperplane separation theorem (Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-5|§43.5]]) there are $\ell \in X'$ and $a \in \mathbb{R}$ with
>
> $$
> \ell(x_0) > a \qquad \text{and} \qquad \ell(x_n) < a \quad \text{for all } n ,
> $$
>
> since every $x_n \in K$. But $x_n \rightharpoonup x_0$ implies $\ell(x_n) \to \ell(x_0)$, and a sequence of numbers all strictly less than $a$ cannot converge to something strictly bigger than $a$: the limit would satisfy $\ell(x_0) \le a$. This is a contradiction.

^pf-43-6

*Uses:* [[§43 Weak and Weak-Star Convergence#^thm-43-5|§43.5]]

![[m556-43-4.svg]]

Mazur's theorem for $e_n \rightharpoonup 0$ in $\ell^2$ (Example [[§43 Weak and Weak-Star Convergence#^ex-43-1|§43.1]]): no $e_n$ comes near $0$, since $\|e_n\| = 1$, but the convex combinations $\frac1N (e_1 + \cdots + e_N)$, with $N$ entries $\frac1N$, have norm $\bigl( N \cdot \frac{1}{N^2} \bigr)^{1/2} = \frac{1}{\sqrt N} \to 0$. Spreading the mass over many orthogonal directions is what the weak limit sees; it also shows the strict inequality $\|0\| < \liminf \|e_n\| = 1$ of Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-4|§43.4]].

## $\sin(mx)$ in $L^p$

> [!example] Example §43.3: $\sin(mx) \rightharpoonup 0$ in $L^p[0, 2\pi]$ for $1 < p < \infty$
> We know $\sin(mx) \rightharpoonup 0$ in $L^2([0, 2\pi])$ (Example [[§43 Weak and Weak-Star Convergence#^ex-43-2|§43.2]]). Since $|\sin(mx)| \le 1$, also $\sin(mx) \in L^p([0, 2\pi])$ for $1 \le p < \infty$. *Question:* does $\sin(mx) \rightharpoonup 0$ in $L^p([0, 2\pi])$ for all $1 < p < \infty$? Yes. (The case $p = 1$ is subtler and is excluded here; see Remark [[§43 Weak and Weak-Star Convergence#^rem-43-2|remark]].)
>
> Recall $(L^p)' = L^{p'}$ with $\frac1p + \frac1{p'} = 1$, so $1 < p' < \infty$ (Theorem [[§31 Dual Spaces#^thm-31-4|§31.4]]). We check the two conditions of Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-3|§43.3]].
>
> 1. *Bounded:* $\sup_m \|\sin(mx)\|_{L^p([0, 2\pi])} \le \bigl( \int_0^{2\pi} 1\, dx \bigr)^{1/p} = (2\pi)^{1/p} < \infty$.
> 2. *Convergence on a dense set:* for every $g \in L^2([0, 2\pi])$, $\int_0^{2\pi} g(x) \sin(mx)\, dx \to 0$ as $m \to \infty$. Continuous functions are in $L^2$, so for all $g \in C[0, 2\pi]$, $\int_0^{2\pi} g(x) \sin(mx)\, dx \to 0$. And $C[0, 2\pi]$ is dense in $L^{p'}([0, 2\pi])$, because $p' < \infty$: it contains $C_c^\infty((0, 2\pi))$, which is dense by Theorem [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-4|§19.4]] (the endpoints have measure zero, so $L^{p'}([0, 2\pi]) = L^{p'}((0, 2\pi))$).
>
> By Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-3|§43.3]], $\sin(mx) \rightharpoonup 0$ in $L^p([0, 2\pi])$.

^ex-43-3

> [!remark] Remark: Two Questions for Homework
> 1. *$p = 1$.* Does $\sin(mx) \rightharpoonup 0$ in $L^1([0, 2\pi])$? Here $(L^1)' = L^\infty$, and continuous functions are not dense in $L^\infty$ (Proposition [[§19 The Function Spaces Lᵖ(Ω)#^prop-19-5|§19.5]]), so the argument above does not apply; one has to test against $L^\infty$ functions. Homework.
> 2. *Products.* If $\{f_n\} \subset L^{p_1}([a,b])$ and $\{g_n\} \subset L^{p_2}([a,b])$, Hölder gives $f_n g_n \in L^p([a,b])$ with $\frac1p = \frac1{p_1} + \frac1{p_2} \le 1$. Assume $f_n \rightharpoonup f_0$ in $L^{p_1}$ and $g_n \rightharpoonup g_0$ in $L^{p_2}$. Does $f_n g_n \rightharpoonup f_0 g_0$ in $L^p$? Usually not: weak limits are not closed under nonlinearity; for instance $f_n \rightharpoonup f$ does not imply $f_n^2 \rightharpoonup f^2$. Finding an example is homework.
>
> Weak limits are useful but limited. A bounded sequence in infinite dimensions need not have a convergent subsequence; under certain circumstances it will have a weakly convergent one, but weak convergence does not commute with nonlinear operations.

^rem-43-2

## Weak-$\ast$ Convergence

Does every bounded sequence have a weakly convergent subsequence? This is a difficult question; to answer it, the weak limit must be weakened even further.

> [!definition] Definition §43.2: Weak-$\ast$ Convergence
> Let $X$ be a normed linear space and let $\{\ell_n\}_{n=1}^\infty$ and $\ell_0$ be in $X'$. We say $\ell_n$ **converges to $\ell_0$ in the weak-$\ast$ sense**, and write $\mathop{\mathrm{w}^{\ast}\text{-}\mathrm{lim}}_{n \to \infty} \ell_n = \ell_0$ or $\ell_n \overset{\ast}{\rightharpoonup} \ell_0$, if for every $x \in X$
>
> $$
> \lim_{n \to \infty} \ell_n(x) = \ell_0(x) .
> $$
>
> *Lax: §10.3, definition (there $X$ is a Banach space)*

^def-43-2

> [!remark] Remark: Weak Implies Weak-$\ast$
> On $X'$ two notions are available: weak convergence ($X'$ is a normed space, test against $(X')' = X''$) and weak-$\ast$ convergence (test against $X$). Since $X \subset X''$ (isometrically embedded), $\ell_n \rightharpoonup \ell_0$ in $X'$ implies $\ell_n \overset{\ast}{\rightharpoonup} \ell_0$ in $X'$: weak convergence tests against every element of $X''$, weak-$\ast$ only against those in $X$. So weak-$\ast$ is the weaker notion. *(Not from lecture.)* If $X$ is reflexive, every element of $X''$ is in $X$, and the two notions coincide (Lax §10.3, Remark 1).

^rem-43-3

> [!example] Example §43.4: Weak-$\ast$ but Not Weak
> $\ell_n \overset{\ast}{\rightharpoonup} \ell_0$ does not imply $\ell_n \rightharpoonup \ell_0$. Let $\ell^\infty_0 = c_0 = \{ (a_1, a_2, \ldots) : \lim_n a_n = 0 \}$ (Proposition [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]). Then $(c_0)' = \ell^1$ (homework) and $(\ell^1)' = \ell^\infty$ (Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]]). Consider $e_n = (0, \ldots, 0, 1, 0, \ldots) \in \ell^1$.
> - $e_n \overset{\ast}{\rightharpoonup} 0$ in $\ell^1 = (c_0)'$: for every $a = (a_1, a_2, \ldots) \in c_0$, $\langle a, e_n \rangle = a_n \to 0$.
> - $e_n \not\rightharpoonup 0$ in $\ell^1$: for $a = (a_1, a_2, \ldots) \in \ell^\infty = (\ell^1)'$, $\langle e_n, a \rangle = a_n$, which need not converge, since $a$ is only bounded.
>
> For instance $a = (1, 1, 1, \ldots)$ gives $\langle e_n, a \rangle = 1 \not\to 0$, and $a = (1, -1, 1, -1, \ldots)$ gives a sequence with no limit at all, so $\{e_n\}$ has no weak limit in $\ell^1$ (any weak limit would also be a weak-$\ast$ limit, hence $0$ by uniqueness). (The pairings are the bar-free ones, $\langle x, b \rangle = \sum_j x_j b_j$, of the remark after Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]].)
>
> *(Not from lecture.)* Lax's example (§10.3, Example 5) is of the same kind: the averages $m_n(h) = \frac{n}{2} \int_{-1/n}^{1/n} h(t)\, dt$ are functionals on $C[-1, 1]$ that converge weak-$\ast$ to the point evaluation $h \mapsto h(0)$, but not weakly, since against a bounded function with a jump at $0$ the averages do not converge to its value at $0$.

^ex-43-4

![[m556-43-5.svg]]

The same sequence $e_n \in \ell^1$ seen by two families of test vectors. Weak-$\ast$ convergence tests only against $c_0$ (left): the pairings are the entries $a_n$ of a null sequence, so they tend to $0$. Weak convergence must also pass the tests by $\ell^\infty = (\ell^1)'$ (right), and a bounded sequence that does not converge defeats it.

As for weak convergence, Banach–Steinhaus gives a criterion, and the norm of the limit is controlled.

> [!theorem] Theorem §43.7: Criterion for Weak-$\ast$ Convergence
> Let $X$ be a Banach space, $\{\ell_n\}_{n=1}^\infty \subset X'$ and $\ell_0 \in X'$. Then $\ell_n \overset{\ast}{\rightharpoonup} \ell_0$ in $X'$ if and only if
>
> 1. $\sup_n \|\ell_n\| < \infty$, and
> 2. $\lim_{n \to \infty} \ell_n(x) = \ell_0(x)$ for all $x \in D$, where $D$ is a dense subset of $X$.

^thm-43-7

> [!proof]+ Proof
> Banach–Steinhaus (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-4|§42.4]]) for the bounded linear maps $\ell_n, \ell_0 : X \to \mathbb{F}$: pointwise convergence on $X$ holds if and only if the $\ell_n$ are uniformly bounded and converge on a dense subset.

^pf-43-7

*Uses:* [[§42 Uniform Boundedness and Approximation#^thm-42-4|§42.4]]

> [!remark] Remark: The Weak-$\ast$ Criteria Need $X$ Complete
> In the lecture the theorem above, and the next one, were stated for a normed linear space $X$; Lax (§10.3) assumes $X$ Banach from the start. Banach–Steinhaus, however, needs the domain of the maps to be complete, and here the domain is $X$ (in Theorem [[§43 Weak and Weak-Star Convergence#^thm-43-3|§43.3]] the domain was $X'$, which is always complete). The direction ($\Leftarrow$) holds for any normed $X$ (the $\varepsilon/2$ argument does not use completeness), but ($\Rightarrow$), weak-$\ast$ convergent implies bounded, can fail. On $X = c_{00}$, the finitely supported sequences with the maximum norm, let $\ell_n(x) = n\, x_n$: then $\ell_n(x) = 0$ once $n$ exceeds the support of $x$, so $\ell_n \overset{\ast}{\rightharpoonup} 0$, but $\|\ell_n\| = n$. So in both theorems $X$ is assumed to be a Banach space; the bound $\|\ell_0\| \le \liminf \|\ell_n\|$ holds for any normed $X$.

^rem-43-4

> [!theorem] Theorem §43.8: The Norm of a Weak-$\ast$ Limit
> Let $X$ be a Banach space, $\{\ell_n\}_{n=1}^\infty \subset X'$, $\ell_0 \in X'$, and assume $\ell_n \overset{\ast}{\rightharpoonup} \ell_0$ in $X'$. Then $\sup_n \|\ell_n\| < \infty$, and
>
> $$
> \|\ell_0\| \le \liminf_{n \to \infty} \|\ell_n\| .
> $$
>
> *Lax: §10.3, Thm 11 (bounded) and Exercise 6 (the norm bound)*

^thm-43-8

> [!proof]+ Proof
> *Bounded:* to converge in the weak-$\ast$ sense, the sequence is pointwise bounded on $X$; this is the uniform boundedness principle (Theorem [[§42 Uniform Boundedness and Approximation#^thm-42-3|§42.3]]).
>
> *The norm bound.* The proof is almost the same as the previous one, but now the norm of $\ell_0$ is computed by its definition, without Hahn–Banach:
>
> $$
> \|\ell_0\| = \sup_{x \in X,\ \|x\| \le 1} |\ell_0(x)| , \qquad \ell_0(x) = \lim_{n \to \infty} \ell_n(x) .
> $$
>
> For $\|x\| \le 1$, $|\ell_0(x)| = \lim_n |\ell_n(x)| = \liminf_n |\ell_n(x)| \le \liminf_n \|\ell_n\|\, \|x\| \le \liminf_n \|\ell_n\|$. Take the supremum over $\|x\| \le 1$.

^pf-43-8

*Uses:* [[§42 Uniform Boundedness and Approximation#^thm-42-3|§42.3]]

Next lecture: under what conditions does a bounded sequence have a weak-$\ast$ convergent subsequence?
