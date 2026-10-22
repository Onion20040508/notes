---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 36
tags: [functional-analysis, math556]
---
← [[§35 Measures and the Radon–Nikodym Theorem]] · ↑ [[· 6 Bounded Linear Maps]] · [[§37 Separable Duals and Reflexive Spaces]] →

*Stage: maps — Thread: functionals. Hahn–Banach with a multiple of the norm as dominating function: there are enough bounded functionals to compute norms and distances, and the dual of $\ell^p$ is $\ell^{p'}$.*

Recall ([[§31 Dual Spaces|§31]]) that for a normed linear space $X$ over $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$ the dual space $X'$ consists of the bounded linear functionals $\ell : X \to \mathbb{F}$, with

$$
\|\ell\| = \sup_{x \neq 0} \frac{|\ell(x)|}{\|x\|} = \sup_{\|x\| = 1} |\ell(x)| ,
$$

and that $X'$ is a Banach space (Corollary [[§31 Dual Spaces#^cor-31-1|§31.1]]).
(The suprema agree because $|\ell(x)|/\|x\| = |\ell(x/\|x\|)|$ and $x/\|x\|$ has norm $1$. Taking the supremum over $\|x\| \le 1$ gives the same number: for $0 < \|x\| \le 1$, $|\ell(x)| = \|x\|\, |\ell(x/\|x\|)| \le \sup_{\|x'\| = 1} |\ell(x')|$, and $\ell(0) = 0$. In particular $|\ell(x)| \le \|\ell\|\,\|x\|$ for all $x$.)
This lecture explains why $X'$ is called the *dual* space: just as $\|\ell\|$ is computed by testing $\ell$ on the unit ball of $X$, norms and distances in $X$ can be computed by testing on the unit ball of $X'$.

## Hahn–Banach for Normed Spaces

The Hahn–Banach theorem of Chapter 2 needed no norm, only a positive homogeneous subadditive $p$. On a normed space there is a more specific version, in which $p$ is a multiple of the norm.

> [!theorem] Theorem §36.1: Hahn–Banach for Normed Spaces
> Let $X$ be a normed linear space over $\mathbb{F}$, $Y$ a linear subspace of $X$ (a normed linear space with the same norm), and $\ell : Y \to \mathbb{F}$ a bounded linear functional on $Y$, with norm
>
> $$
> \|\ell\|_Y = \sup_{y \in Y,\ \|y\| \le 1} |\ell(y)| .
> $$
>
> Then $\ell$ has an extension $L \in X'$, $L|_Y = \ell$, with the same norm: $\|L\| = \|\ell\|_Y$.

^thm-36-1

> [!proof]+ Proof
> Wu: “this is really Hahn–Banach”; the abstract theorem is applied with
>
> $$
> p(x) = \|\ell\|_Y\, \|x\|, \qquad x \in X .
> $$
>
> **Step 1: $p$ is admissible and dominates $\ell$ on $Y$.** For $a \in \mathbb{F}$, $p(ax) = \|\ell\|_Y\, |a|\, \|x\| = |a|\, p(x)$; in particular $p$ is positive homogeneous. By the triangle inequality, $p(x + x') \le p(x) + p(x')$. On $Y$, by the definition of $\|\ell\|_Y$ (the bound $|\ell(x)| \le \|\ell\|\,\|x\|$ noted at the start of this section, applied in the normed space $Y$), $|\ell(y)| \le \|\ell\|_Y\, \|y\|$, i.e.
>
> $$
> |\ell(y)| \le p(y) \qquad \text{for all } y \in Y .
> $$
>
> **Step 2: extend.**
> *Real case.* Since $\ell(y) \le |\ell(y)| \le p(y)$ on $Y$, Theorem [[§5 Statement and Motivation#^thm-5-2|§5.2]] gives a linear functional $L : X \to \mathbb{R}$ with $L|_Y = \ell$ and $L(x) \le p(x)$ for all $x \in X$. Applied to $-x$, this gives $-L(x) = L(-x) \le p(-x) = p(x)$. Hence $|L(x)| \le p(x)$ for all $x$.
>
> *Complex case.* By Step 1, $p$ satisfies conditions (1)–(2) of Theorem [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|§9.2]], and $|\ell| \le p$ on $Y$. That theorem gives a linear extension $L$ of $\ell$ with $|L(x)| \le p(x)$ for all $x \in X$.
>
> **Step 3: the norm.** In both cases $|L(x)| \le p(x) = \|\ell\|_Y\, \|x\|$ for all $x$, so $L$ is bounded, $L \in X'$, and $\|L\| \le \|\ell\|_Y$. Conversely, $L = \ell$ on $Y$, and the supremum defining $\|L\|$ runs over a larger set than the one defining $\|\ell\|_Y$:
>
> $$
> \|L\| = \sup_{x \in X,\ \|x\| \le 1} |L(x)| \ \ge\ \sup_{y \in Y,\ \|y\| \le 1} |\ell(y)| = \|\ell\|_Y .
> $$
>
> Hence $\|L\| = \|\ell\|_Y$.

^pf-36-1

*Uses:* [[§5 Statement and Motivation#^thm-5-2|§5.2]], [[§9 The Complex Hahn–Banach Theorem#^thm-9-2|§9.2]]

> [!remark] Remark: The Pairing $\langle x, \ell \rangle$ Again
> Wu: one often writes $\ell(x) = \langle x, \ell \rangle$ for $x \in X$, $\ell \in X'$ (as in [[§31 Dual Spaces|§31]]). The expression is linear in $x$, and also linear in $\ell$, since $(c_1 \ell_1 + c_2 \ell_2)(x) = c_1 \ell_1(x) + c_2 \ell_2(x)$; so it is like a bilinear form on $X \times X'$, and it is convenient to think of $X$ and $X'$ as being in a dual relation. The notation comes from Hilbert space: a student asked whether “the dual is itself” means $H$ and $H'$ are isomorphic; Wu: by the Riesz representation theorem every $\ell \in H'$ is $\ell(x) = (x, a)$ for some $a \in H$, and $H'$ is identified with $H$ through $a \leftrightarrow \ell_a$ (Corollary [[§31 Dual Spaces#^cor-31-3|§31.3]]).
> Over $\mathbb{C}$ the two pairings differ slightly: $\langle x, \ell \rangle$ is linear in $\ell$, while $(x, a)$ is conjugate-linear in $a$; correspondingly, the Riesz map $a \mapsto \ell_a$ is conjugate-linear.

^rem-36-1

## The Norm as a Maximum over the Dual

For $\ell \in X'$, $\|\ell\|$ is computed as a supremum of $|\ell(x)|$ over $\|x\| \le 1$. The opposite is also true.

> [!theorem] Theorem §36.2: The Norm as a Maximum over the Dual
> Let $X$ be a normed linear space over $\mathbb{F}$. For every $y \in X$,
>
> $$
> \|y\| = \max \bigl\{ |\ell(y)| : \ell \in X',\ \|\ell\| \le 1 \bigr\} .
> $$
>
> If $X \neq \{0\}$, the maximum is attained by a functional of norm exactly $1$, so “$\|\ell\| \le 1$” may be replaced by “$\|\ell\| = 1$”.

^thm-36-2

> [!proof]+ Proof
> Fix $y_0 \in X$.
>
> **Step 1: $\sup \le \|y_0\|$.** Let $\ell \in X'$ with $\|\ell\| \le 1$. Then
>
> $$
> |\ell(y_0)| \le \|\ell\|\, \|y_0\| \le \|y_0\| .
> $$
>
> Taking the supremum over all such $\ell$, $\sup_{\|\ell\| \le 1} |\ell(y_0)| \le \|y_0\|$. At this point we do not yet know that the supremum is attained.
>
> **Step 2: a functional attaining $\|y_0\|$.** We want $L_0 \in X'$ with $\|L_0\| \le 1$ and $|L_0(y_0)| = \|y_0\|$.
> If $y_0 = 0$, then $L_0 = 0$ will do; and if $X \neq \{0\}$, applying the construction below to some $x_1 \neq 0$ produces an $L_0$ with $\|L_0\| = 1$, and $|L_0(0)| = 0 = \|0\|$. So assume $y_0 \neq 0$.
>
> Let $Y = \operatorname{span}\{y_0\} = \{ c\, y_0 : c \in \mathbb{F} \}$ and define $\ell_0 : Y \to \mathbb{F}$ by
>
> $$
> \ell_0(c\, y_0) = c\, \|y_0\|, \qquad \text{in particular } \ell_0(y_0) = \|y_0\| .
> $$
>
> (This is well defined because $y_0 \neq 0$: $c\, y_0 = c'\, y_0$ gives $(c - c')\, y_0 = 0$, so $c = c'$. It is linear: $\ell_0(c\, y_0 + c'\, y_0) = (c + c')\|y_0\|$ and $\ell_0(a\, c\, y_0) = a\, c\, \|y_0\|$.) It is bounded: every element of $Y$ is $c\, y_0$ for some $c$, and
>
> $$
> |\ell_0(c\, y_0)| = |c|\, \|y_0\| = \|c\, y_0\| .
> $$
>
> So $|\ell_0(y)| = \|y\|$ for every $y \in Y$, and $\|\ell_0\|_Y = 1$. By Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]], $\ell_0$ extends to $L_0 \in X'$ with $\|L_0\| = \|\ell_0\|_Y = 1$, and $L_0(y_0) = \ell_0(y_0) = \|y_0\|$.
>
> **Step 3: conclusion.** By Step 2, $\sup_{\|\ell\| \le 1} |\ell(y_0)| \ge |L_0(y_0)| = \|y_0\|$; with Step 1 the supremum equals $\|y_0\|$, and it is attained at $L_0$, so it is a maximum.

^pf-36-2
![[m556-36-2.svg]]
*Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]] in $\mathbb{R}^2$ with the norm $\|x\| = |x_1| + |x_2|$, whose unit ball is the blue square. A functional $\ell(x) = c_1 x_1 + c_2 x_2$ has norm $\max(|c_1|, |c_2|)$, and $\|\ell\| \le 1$ means that the ball lies in the strip $|\ell| \le 1$. A norming functional for $y_0$ ($\|\ell\| = 1$, $\ell(y_0) = \|y_0\| = 1$) is a line $\ell = 1$ touching the ball at $y_0$ with the ball on one side — a supporting line. Left: at a point of an edge it is unique. Right: at a corner there are many; this is the non-uniqueness of Hahn–Banach extensions (Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]) seen in the plane.*

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]

> [!remark] Remark: Duality
> The two formulas
>
> $$
> \|\ell\| = \sup_{x \in X,\ \|x\| \le 1} |\ell(x)|, \qquad \|y\| = \max_{\ell \in X',\ \|\ell\| \le 1} |\ell(y)|
> $$
>
> mirror each other. Wu: both are very useful in practice, for estimates; abstractly the proof is not difficult. A student asked whether “$\le 1$” should be “$= 1$”; Wu: either is a correct statement (“$\le$” does not make the maximum bigger), as the theorem records.
> The two formulas are not perfectly symmetric: the supremum over $X$ need not be attained (Example [[§36 Duality in Normed Spaces#^ex-36-1|§36.1]]), while the one over $X'$ always is; Hahn–Banach is what produces the maximizing functional.

^rem-36-2

> [!example] Example §36.1: The Supremum in $\|\ell\|$ Need Not be Attained
> On $c_0$, the sequences tending to $0$ with $\|a\| = \max_n |a_n|$ (Proposition [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]), let
>
> $$
> \ell(a) = \sum_{n=1}^\infty 2^{-n} a_n .
> $$
>
> The series converges absolutely, $|\ell(a)| \le \sum 2^{-n} |a_n| \le \|a\| \sum 2^{-n} = \|a\|$, and $\ell$ is linear; so $\ell \in c_0'$ with $\|\ell\| \le 1$. For $a^{(N)} = (1, \ldots, 1, 0, \ldots)$ ($N$ ones), $\|a^{(N)}\| = 1$ and $\ell(a^{(N)}) = 1 - 2^{-N} \to 1$; so $\|\ell\| = 1$. But no $a$ with $\|a\| \le 1$ has $|\ell(a)| = 1$: that would give
>
> $$
> 1 = \Bigl| \sum_n 2^{-n} a_n \Bigr| \le \sum_n 2^{-n} |a_n| \le \sum_n 2^{-n} = 1, \qquad \text{so} \qquad \sum_n 2^{-n} \bigl( 1 - |a_n| \bigr) = 0 ,
> $$
>
> a sum of non-negative terms; hence $|a_n| = 1$ for every $n$, contradicting $a_n \to 0$.

^ex-36-1
![[m556-36-4.svg]]
*Example [[§36 Duality in Normed Spaces#^ex-36-1|§36.1]]: the values $\ell(a^{(N)}) = 1 - 2^{-N}$ on the unit vectors $a^{(N)} = (1, \ldots, 1, 0, \ldots)$ of $c_0$ increase to $\|\ell\| = 1$. Reaching $1$ would need $|a_n| = 1$ for every $n$, which no element of $c_0$ has: the supremum over the unit ball of $X$ is not attained, while the maximum over the unit ball of $X'$ in Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]] always is.*

> [!theorem] Corollary §36.3: Bounded Functionals Separate Points
> Let $X$ be a normed linear space. If $x \in X$ and $\ell(x) = 0$ for every $\ell \in X'$, then $x = 0$. Equivalently, for $x \neq x'$ there is $\ell \in X'$ with $\ell(x) \neq \ell(x')$.

^cor-36-3

> [!proof]+ Proof
> By Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]], $\|x\| = \max_{\|\ell\| \le 1} |\ell(x)| = 0$. For the second form apply this to $x - x'$.

^pf-36-3

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]]

This is the precise form of the remark in [[§6 Proof of the Hahn–Banach Theorem|§6]] that Hahn–Banach guarantees “enough” linear functionals: on a normed space there are enough *bounded* ones to tell points apart.

## The Dual of $\ell^p$

Before going on, Wu derived the dual of $\ell^p$, announced in Lecture 10 (Theorem [[§31 Dual Spaces#^thm-31-4|§31.4]]). This was Problem 3 of the current homework; Wu waived it after doing it in class. Let $e_j = (0, \ldots, 0, 1, 0, \ldots)$ denote the sequence with $1$ in the $j$-th place and $0$ elsewhere, and let $p'$ be the conjugate exponent of $p$ (Definition [[§17 Hölder's Inequality for Sequences#^def-17-3|§17.3]]).

> [!theorem] Theorem §36.4: The Dual of $\ell^p$
> Let $1 \le p < \infty$ and $\frac1p + \frac1{p'} = 1$, so that $1 < p' \le \infty$.
>
> 1. For $a = (a_1, a_2, \ldots) \in \ell^{p'}$,
>
> $$
> \ell_a(x) = \sum_{j=1}^\infty x_j\, \overline{a_j}, \qquad x = (x_1, x_2, \ldots) \in \ell^p,
> $$
>
> defines $\ell_a \in (\ell^p)'$, with $\|\ell_a\| \le \|a\|_{p'}$.
> 2. For every $\ell \in (\ell^p)'$, the numbers $a_j = \overline{\ell(e_j)}$ form a sequence $a \in \ell^{p'}$ with $\|a\|_{p'} \le \|\ell\|$, and $\ell = \ell_a$.
>
> Consequently $a \mapsto \ell_a$ is a one-to-one map of $\ell^{p'}$ onto $(\ell^p)'$ with $\|\ell_a\| = \|a\|_{p'}$; it is linear if $\mathbb{F} = \mathbb{R}$ and conjugate-linear if $\mathbb{F} = \mathbb{C}$. In this sense $(\ell^p)' = \ell^{p'}$.

^thm-36-4

> [!proof]+ Proof
> Wu first treated $1 < p < \infty$ (so $p' < \infty$) and then indicated the changes for $p = 1$, $p' = \infty$; the reason for separating the cases is that $\|a\|_{p'}$ is written differently for $p' = \infty$.
>
> **Step 1: every $a \in \ell^{p'}$ gives a bounded functional.** Let $a \in \ell^{p'}$. By Hölder's inequality (Theorem [[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]], with the pair $p, p'$), for $x \in \ell^p$
>
> $$
> \sum_{j=1}^\infty |x_j\, \overline{a_j}| = \sum_{j=1}^\infty |x_j|\, |a_j| \le \|x\|_p\, \|a\|_{p'} < \infty .
> $$
>
> So the series defining $\ell_a(x)$ converges absolutely, hence converges, and $\ell_a$ is well defined. It is linear, because its partial sums are linear in $x$ and limits of sums are sums of limits. It is bounded, since $|\ell_a(x)| \le \sum_j |x_j|\,|a_j| \le \|a\|_{p'}\, \|x\|_p$. Hence $\ell_a \in (\ell^p)'$ and $\|\ell_a\| \le \|a\|_{p'}$. (Wu put the bar on $a_j$ “just in case” $\mathbb{F} = \mathbb{C}$, so that for $p = 2$ the formula is the inner product of $\ell^2$, as in Example [[§31 Dual Spaces#^ex-31-1|§31.1]].)
>
> **Step 2: the candidate $a$, and $a \in \ell^{p'}$.** Let $\ell \in (\ell^p)'$. We want to write $\ell$ as in Step 1. The $j$-th entry of $a$ can be read off by testing on $e_j \in \ell^p$: if $\ell = \ell_a$, then $\ell(e_j) = \overline{a_j}$. Inspired by this, *define*
>
> $$
> a_j = \overline{\ell(e_j)} \in \mathbb{F}, \qquad a = (a_1, a_2, \ldots) .
> $$
>
> Infinite sums are difficult, so start with finite ones. A finite sequence $x = (x_1, \ldots, x_n, 0, 0, \ldots)$ is the finite linear combination $\sum_{j=1}^n x_j e_j$, so by linearity of $\ell$
>
> $$
> \ell(x) = \sum_{j=1}^n x_j\, \ell(e_j) = \sum_{j=1}^n x_j\, \overline{a_j} . \tag{F}
> $$
>
> Now we show $a \in \ell^{p'}$, by computing its norm with a special choice of $x$.
>
> *Case 1: $1 < p < \infty$, so $1 < p' < \infty$.* Fix $n$. The quantity to bound is $\sum_{j=1}^n |a_j|^{p'}$, and we write each term in the form $x_j\, \overline{a_j}$ of (F):
>
> $$
> |a_j|^{p'} = |a_j|^{p'-2}\, a_j\, \overline{a_j} .
> $$
>
> So take $x_j = |a_j|^{p'-2} a_j$ for $j \le n$, and $x^0 = (x_1, \ldots, x_n, 0, 0, \ldots) \in \ell^p$.
> (If $p' < 2$ and $a_j = 0$, the power $|a_j|^{p'-2}$ is undefined; set $x_j = 0$ then. The identity $|a_j|^{p'} = x_j\, \overline{a_j}$ still holds, both sides being $0$.) Its norm: $|x_j| = |a_j|^{p'-1}$, so
>
> $$
> \|x^0\|_p^p = \sum_{j=1}^n |x_j|^p = \sum_{j=1}^n |a_j|^{(p'-1)p} = \sum_{j=1}^n |a_j|^{p'},
> $$
>
> because $(p' - 1)\,p = p'$.
> (Multiplying $\frac1p + \frac1{p'} = 1$ by $p p'$ gives $p' + p = p p'$, so $(p'-1)\,p = p p' - p = p'$.) Wu: “when things are correct, it will just work out fine.” Write $S_n = \sum_{j=1}^n |a_j|^{p'}$. By (F) and the choice of $x^0$,
>
> $$
> \ell(x^0) = \sum_{j=1}^n x_j\, \overline{a_j} = \sum_{j=1}^n |a_j|^{p'} = S_n ,
> $$
>
> and since $\ell$ is bounded,
>
> $$
> S_n = |\ell(x^0)| \le \|\ell\|\, \|x^0\|_p = \|\ell\|\, S_n^{1/p} .
> $$
>
> $S_n$ is a finite number, so we may divide. If $S_n = 0$ there is nothing to prove. Otherwise, dividing by $S_n^{1/p}$, $S_n^{1 - 1/p} \le \|\ell\|$, and $1 - \frac1p = \frac1{p'}$:
>
> $$
> \Bigl( \sum_{j=1}^n |a_j|^{p'} \Bigr)^{1/p'} \le \|\ell\| \qquad \text{for every } n .
> $$
>
> The left side increases with $n$ and is bounded, so letting $n \to \infty$,
>
> $$
> \|a\|_{p'} = \Bigl( \sum_{j=1}^\infty |a_j|^{p'} \Bigr)^{1/p'} \le \|\ell\| .
> $$
>
> So $a \in \ell^{p'}$, and (F) says that $\ell(x) = \sum_j x_j \overline{a_j}$ for every finite sequence $x$.
>
> **Step 3: $\ell = \ell_a$ on all of $\ell^p$.** The formula holds on finite sequences, and these are dense in $\ell^p$; this is where $p < \infty$ is used. Let $x = (x_1, x_2, \ldots) \in \ell^p$ and $x^{(n)} = (x_1, \ldots, x_n, 0, 0, \ldots)$. Then $x^{(n)} \to x$ in $\ell^p$, because
>
> $$
> \|x - x^{(n)}\|_p^p = \sum_{j=n+1}^\infty |x_j|^p \to 0 \qquad (n \to \infty),
> $$
>
> the tail of a convergent series. A bounded linear functional is continuous (Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]), so $\ell(x^{(n)}) \to \ell(x)$. On the other hand, by (F),
>
> $$
> \ell(x^{(n)}) = \sum_{j=1}^n x_j\, \overline{a_j} ,
> $$
>
> and these are the partial sums of the series $\sum_j x_j \overline{a_j}$, which converges to $\ell_a(x)$ by Step 1 (Hölder, as $x \in \ell^p$ and $a \in \ell^{p'}$). Limits are unique, so $\ell(x) = \ell_a(x)$.
>
> *Case 2: $p = 1$, $p' = \infty$.* Step 1 is unchanged, and so is Step 3.
> (It uses only $\|x - x^{(n)}\|_1 = \sum_{j > n} |x_j| \to 0$ and Hölder with the pair $1, \infty$.) In Step 2 we still have (F), and now want $a \in \ell^\infty$, i.e. a bound on each $|a_j|$. If $a_j = 0$ there is nothing to prove. Otherwise write $|a_j| = \frac{a_j}{|a_j|}\, \overline{a_j}$ and let
>
> $$
> x = \frac{a_j}{|a_j|}\, e_j = \Bigl( 0, \ldots, 0, \frac{a_j}{|a_j|}, 0, \ldots \Bigr) ,
> $$
>
> zero except in one component. Then $\|x\|_1 = 1$, and by (F) $\ell(x) = \frac{a_j}{|a_j|}\, \overline{a_j} = |a_j|$. Hence
>
> $$
> |a_j| = |\ell(x)| \le \|\ell\|\, \|x\|_1 = \|\ell\| \qquad \text{for all } j,
> $$
>
> so $\|a\|_\infty \le \|\ell\|$ and $a \in \ell^\infty$.
>
> **Conclusion.** Let $a \in \ell^{p'}$. Applying Step 2 to $\ell = \ell_a$, the candidate is $a$ itself, since $\ell_a(e_j) = \overline{a_j}$; so $\|a\|_{p'} \le \|\ell_a\|$, and with Step 1, $\|\ell_a\| = \|a\|_{p'}$. The map $a \mapsto \ell_a$ is onto by Steps 2–3, and one-to-one: if $\ell_a = \ell_b$, then $\overline{a_j} = \ell_a(e_j) = \ell_b(e_j) = \overline{b_j}$ for every $j$. Termwise, $\ell_{a + b} = \ell_a + \ell_b$ and $\ell_{ca} = \bar c\, \ell_a$.

^pf-36-4

*Uses:* [[§17 Hölder's Inequality for Sequences#^thm-17-1|§17.1]], [[§31 Dual Spaces#^ex-31-1|Ex. §31.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]

> [!remark] Remark: The Pairing Without the Bar
> Over $\mathbb{C}$ one can equally use the pairing without the bar: $a \mapsto \ell_{\bar a}$, $\ell_{\bar a}(x) = \sum_j x_j a_j$, is a *linear* one-to-one, onto, norm-preserving map $\ell^{p'} \to (\ell^p)'$, i.e. an isometric isomorphism. With the bar, the case $p = 2$ is the Riesz representation of $(\ell^2)'$ (Example [[§31 Dual Spaces#^ex-31-1|§31.1]]), and the map is conjugate-linear exactly like the Riesz map (Corollary [[§31 Dual Spaces#^cor-31-3|§31.3]]). The test vector $x_j = |a_j|^{p'-2} a_j$ of Step 2 is the vector for which Hölder's inequality is an equality; the same choice reappears below.

^rem-36-3

> [!theorem] Corollary §36.5: Duality Formula for the $\ell^p$ Norm
> Let $1 \le p < \infty$. For every $a \in \ell^p$,
>
> $$
> \|a\|_p = \max \Bigl\{ \Bigl| \sum_{j=1}^\infty a_j\, \overline{b_j} \Bigr| : b \in \ell^{p'},\ \|b\|_{p'} = 1 \Bigr\} .
> $$
>
> *Lax: §5.1, Thm 5*

^cor-36-5

> [!proof]+ Proof
> By Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]] with $X = \ell^p$ (in the version with $\|\ell\| = 1$), $\|a\|_p = \max \{ |\ell(a)| : \ell \in (\ell^p)',\ \|\ell\| = 1 \}$. By Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], the functionals $\ell \in (\ell^p)'$ are exactly the $\ell_b$ with $b \in \ell^{p'}$, with $\|\ell_b\| = \|b\|_{p'}$ and $\ell_b(a) = \sum_j a_j \overline{b_j}$. Substituting gives the formula.

^pf-36-5

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]], [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]]

> [!remark] Remark: Why Duality Formulas are Useful
> Wu: instead of computing the $p$-th power sum $\bigl( \sum_j |a_j|^p \bigr)^{1/p}$, which can be awkward, one multiplies $a$ by an arbitrary $b$ in the unit sphere of $\ell^{p'}$ and maximizes; that is much easier to work with. “This kind of formula is called duality.” For functions it reads
>
> $$
> \|f\|_{L^p} = \sup \Bigl\{ \Bigl| \int f(x)\, \overline{g(x)}\, d\mu(x) \Bigr| : \|g\|_{L^{p'}} = 1 \Bigr\} .
> $$
>
> For $1 < p < \infty$ the maximum can also be exhibited directly: for $a \neq 0$, $b_j = |a_j|^{p-2} a_j / \|a\|_p^{p-1}$ ($b_j = 0$ where $a_j = 0$) has $\|b\|_{p'}^{p'} = \sum_j |a_j|^{(p-1)p'} / \|a\|_p^{(p-1)p'} = 1$, since $(p-1)p' = p$, and $\sum_j a_j \overline{b_j} = \sum_j |a_j|^p / \|a\|_p^{p-1} = \|a\|_p$; for $p = 1$ take $b_j = a_j/|a_j|$ where $a_j \neq 0$ and $b_j = 1$ elsewhere. Together with Hölder this proves Corollary [[§36 Duality in Normed Spaces#^cor-36-5|§36.5]] without Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], and the same choice $g = |f|^{p-2} f / \|f\|_{L^p}^{p-1}$ shows the supremum for functions is a maximum for $1 \le p < \infty$. This is Lax's route to Minkowski's inequality (Concordance, C.2). What Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]] adds is that *every* bounded functional on $\ell^p$ is of the form $\ell_b$.

^rem-36-4
![[m556-36-3.svg]]
*Corollary [[§36 Duality in Normed Spaces#^cor-36-5|§36.5]] in $\mathbb{R}^2$ for $p = 3$, $p' = \tfrac32$. For $a$ on the unit sphere of $\ell^3$, the maximizing $b_j = |a_j|^{p-2} a_j$ (the remark Why Duality Formulas are Useful) lies on the unit sphere of $\ell^{3/2}$ (dashed), and the line $\sum_j x_j b_j = 1$ touches the $\ell^3$ ball exactly at $a$: by Hölder every $x$ in the ball has $\sum_j x_j b_j \le 1$, with equality at $a$. The maximizer is the normal of the supporting line.*

> [!remark] Remark: The Dual of $L^p$, Revisited
> Wu: similarly, for any measure space $(X, \mu)$, e.g. $\Omega \subset \mathbb{R}^n$ with Lebesgue measure, and $1 \le p < \infty$, $(L^p(X, \mu))' = L^{p'}(X, \mu)$; this is Theorem [[§31 Dual Spaces#^thm-31-4|§31.4]]. For those who have learned measure theory, the candidate is found with the Radon–Nikodym theorem, and the rest goes as for sequences; Wu left the proof to the class (an outline is given after Theorem [[§31 Dual Spaces#^thm-31-4|§31.4]]).
> For $p = 1$ the measure must be $\sigma$-finite (Lebesgue measure on $\Omega$ is); for $1 < p < \infty$ no condition is needed. Wu also set the scope of the midterm: results that need measure theory (the $L^p$ spaces, beyond their basic properties) and the PDE applications will not be tested; $\ell^p$ will.

^rem-36-5

> [!example] Example §36.2: $(\ell^\infty)'$ is Larger than $\ell^1$
> Wu: the theorem fails for $p = \infty$. $(\ell^\infty)' \neq \ell^1$, and likewise $(L^\infty)' \neq L^1$; the dual of $\ell^\infty$ can be described as a space of finite measures on $\mathbb{N}$.
> (Precisely: bounded *finitely* additive set functions on the subsets of $\mathbb{N}$; the countably additive ones correspond to $\ell^1$.) In the homework the space is not $\ell^\infty$ but $c_0$, the sequences tending to $0$ (Proposition [[§29 Sequence and Function Spaces#^prop-29-2|§29.2]]); there the finite sequences are dense, and the same strategy as in Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]] applies. In $\ell^\infty$ they are not dense: for every finite sequence $x$, $\|(1, 1, 1, \ldots) - x\|_\infty \ge 1$. So Step 3 of the proof breaks down.

^ex-36-2

> [!proof]+ Proof
> (Stated in lecture without proof.) We show that $a \mapsto \ell_a$, $\ell^1 \to (\ell^\infty)'$, is not onto. Step 1 of Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]] works for $p = \infty$, $p' = 1$: each $a \in \ell^1$ gives $\ell_a \in (\ell^\infty)'$. Let $c \subset \ell^\infty$ be the linear subspace of convergent sequences and $\lambda(x) = \lim_{j \to \infty} x_j$ on $c$. Then $\lambda$ is linear and $|\lambda(x)| \le \sup_j |x_j| = \|x\|_\infty$, so $\|\lambda\|_c \le 1$. By Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]], $\lambda$ extends to some $L \in (\ell^\infty)'$. If $L = \ell_a$ with $a \in \ell^1$, then $\overline{a_j} = L(e_j) = \lambda(e_j) = 0$ for every $j$ (since $e_j \in c$ tends to $0$), so $a = 0$ and $L = 0$; but $L(1, 1, 1, \ldots) = \lambda(1, 1, 1, \ldots) = 1$. So $L$ is not of the form $\ell_a$.

^pf-ex-36-2
![[m556-36-5.svg]]
*Why Step 3 of Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]] needs $p < \infty$. Left: for $x \in \ell^p$ the truncation $x^{(n)}$ (blue, here $n = 5$) differs from $x$ by a tail whose $p$-th power sum tends to $0$, so finite sequences are dense and a bounded functional is determined by its values $\ell(e_j)$. Right: in $\ell^\infty$ the tail of $(1, 1, 1, \ldots)$ always has supremum $1$; the finite sequences are not dense, and the functional of Example [[§36 Duality in Normed Spaces#^ex-36-2|§36.2]] vanishes on every $e_j$ without being $0$.*

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]

## Distance to a Subspace

The next theorem extends Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]], which is the case $Y = \{0\}$, from the norm of a vector to its distance from a subspace.

> [!theorem] Theorem §36.6: Distance to a Subspace
> Let $X$ be a normed linear space over $\mathbb{F}$, $Y$ a linear subspace of $X$, and $z \in X$. Then
>
> $$
> \inf_{y \in Y} \|z - y\| = \max \bigl\{ |\ell(z)| : \ell \in X',\ \|\ell\| \le 1,\ \ell(y) = 0 \text{ for all } y \in Y \bigr\} .
> $$

^thm-36-6

![[m556-36-1.svg]]

Wu's heuristic, “cheating a little” by pretending there is an inner product: the distance from $z$ to $Y$ is the length of the perpendicular from $z$ to $Y$, i.e. of the projection of $z$ onto the perpendicular direction $Y^\perp$. If $Y^\perp$ is spanned by orthonormal $e_j$, that projection is $\sum_j (z, e_j)\, e_j$, and each $(z, e_j)$ is a bounded functional of norm $1$ vanishing on $Y$, applied to $z$. In a normed space “perpendicular to $Y$” is replaced by “a functional vanishing on $Y$”, and the theorem says the heuristic is exact.

> [!proof]+ Proof
> **Step 1: $\sup \le \inf$.** Let $\ell \in X'$ with $\|\ell\| \le 1$ and $\ell(y) = 0$ for all $y \in Y$. Then $\ell(z) = \ell(z) - \ell(y) = \ell(z - y)$ for every $y \in Y$, so
>
> $$
> |\ell(z)| \le \|\ell\|\, \|z - y\| \le \|z - y\| \qquad \text{for all } y \in Y .
> $$
>
> (Wu: the bound $\|\ell\| \le 1$ is essential; otherwise $\ell$ could be multiplied by any constant.) Taking the infimum over $y$, $|\ell(z)| \le \inf_{y \in Y} \|z - y\|$; then taking the supremum over all such $\ell$,
>
> $$
> \sup \bigl\{ |\ell(z)| : \ell \in X',\ \|\ell\| \le 1,\ \ell|_Y = 0 \bigr\} \le \inf_{y \in Y} \|z - y\| .
> $$
>
> We do not yet know that the supremum is attained.
>
> **Step 2: a functional attaining the infimum.** Fix $z_0 \in X$; the functional found depends on $z_0$ (a student asked whether the same $\ell$ works for every $z$; it does not, just as the maximizing functional in Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]] depends on $y_0$). Let
>
> $$
> m = \inf_{y \in Y} \|z_0 - y\| \ \ge 0 .
> $$
>
> We want $L \in X'$ with $\|L\| \le 1$, $L(y) = 0$ for all $y \in Y$, and $L(z_0) = m$.
>
> If $z_0 \in Y$, there is nothing to prove:
> taking $y = z_0$ shows $m = 0$, and $L = 0$ does it. So assume $z_0 \notin Y$, and let
>
> $$
> Y_1 = \operatorname{span}\{z_0, Y\} = \{ c\, z_0 + y : c \in \mathbb{F},\ y \in Y \} .
> $$
>
> Each element of $Y_1$ has only one such representation: if $c\, z_0 + y = c'\, z_0 + y'$, then $(c - c')\, z_0 = y' - y \in Y$; if $c \neq c'$ this would put $z_0 = (y' - y)/(c - c')$ in $Y$, so $c = c'$, and then $y = y'$. Define $\ell : Y_1 \to \mathbb{F}$ by
>
> $$
> \ell(c\, z_0 + y) = c\, m, \qquad \text{so } \ell(z_0) = m \text{ and } \ell(y) = 0 \text{ for } y \in Y .
> $$
>
> It is linear: $(c\, z_0 + y) + (c'\, z_0 + y') = (c + c')\, z_0 + (y + y')$ is sent to $(c + c')\, m$, and $a(c\, z_0 + y) = (ac)\, z_0 + ay$ to $ac\, m$.
>
> *$\|\ell\|_{Y_1} \le 1$.* Let $c\, z_0 + y \in Y_1$; then $|\ell(c\, z_0 + y)| = |c|\, m$. If $c \neq 0$, put the $c$ inside: since $-y/c \in Y$ and $m$ is the infimum of $\|z_0 - y_0\|$ over $y_0 \in Y$ (the name $y_0$ avoids a clash with $y$),
>
> $$
> |c|\, m \le |c|\, \Bigl\| z_0 - \Bigl( -\frac{y}{c} \Bigr) \Bigr\| = \Bigl\| c\, z_0 + y \Bigr\| .
> $$
>
> If $c = 0$, $|\ell(y)| = 0 \le \|y\|$. So $|\ell(w)| \le \|w\|$ for every $w \in Y_1$, i.e. $\|\ell\|_{Y_1} \le 1$.
>
> *Extend.* By Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]], $\ell$ has an extension $L \in X'$ with $\|L\| = \|\ell\|_{Y_1} \le 1$. Then $L(y) = \ell(y) = 0$ for $y \in Y$ and $L(z_0) = \ell(z_0) = m$.
>
> **Step 3: conclusion.** By Step 2 the supremum in Step 1 is at least $|L(z_0)| = m$; with Step 1 it equals $m$ and is attained at $L$. So it is a maximum, equal to $\inf_{y \in Y} \|z_0 - y\|$.

^pf-36-6

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]], [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]

> [!remark] Remark: How to Find the Proof
> A student asked how one would think of the subspace $Y_1$. Wu: first, believe the statement, because it is true in a Hilbert space (the picture above). Then what is left is to find an $\ell$ with $\|\ell\| \le 1$, $\ell = 0$ on $Y$ (“somehow perpendicular to $Y$”) and $\ell(z_0) = m$. On the span of $z_0$ and $Y$ these requirements leave no choice (up to replacing $m$ by $e^{i\theta} m$), so define $\ell$ there, check its norm, and let Hahn–Banach extend it. Extensions are usually not unique; on the smaller space there is no choice. “It's really just pure logic.” The proof of Theorem [[§36 Duality in Normed Spaces#^thm-36-2|§36.2]] is the same argument with $Y = \{0\}$.
> Closedness of $Y$ is not needed: if $z_0$ lies in the closure of $Y$ but not in $Y$, then $m = 0$ and the construction gives $L = 0$. If $Y$ is closed and $z_0 \notin Y$, then $m > 0$ (a ball around $z_0$ misses $Y$), so there is an $L \in X'$ vanishing on $Y$ with $L(z_0) \neq 0$.

^rem-36-6

## The Annihilator

By now the duality is visible, and it is natural to define a “perpendicular” in a normed space.

> [!definition] Definition §36.1: Annihilator
> Let $X$ be a normed linear space and $Y$ a linear subspace of $X$. The **annihilator** of $Y$ is
>
> $$
> Y^\perp = \{ \ell \in X' : \ell(y) = 0 \text{ for all } y \in Y \} ,
> $$
>
> the set of bounded linear functionals vanishing on $Y$.

^def-36-1

In this notation Theorem [[§36 Duality in Normed Spaces#^thm-36-6|§36.6]] reads $\inf_{y \in Y} \|z - y\| = \max_{\ell \in Y^\perp,\ \|\ell\| \le 1} |\ell(z)|$.

> [!remark] Remark: Two Meanings of $Y^\perp$
> The annihilator is a subset of $X'$, while the orthogonal complement of a subspace of a Hilbert space (Definition [[§25 Projection and Orthogonal Decomposition#^def-25-1|§25.1]]) is a subset of $H$. The shared notation is consistent: under the Riesz map $a \mapsto \ell_a$, $\ell_a(y) = (y, a) = 0$ for all $y \in Y$ exactly when $a$ is orthogonal to $Y$, so the Riesz map carries the orthogonal complement of $Y$ onto its annihilator.

^rem-36-7

> [!theorem] Proposition §36.7: The Annihilator is a Closed Subspace
> Let $X$ be a normed linear space and $Y$ a linear subspace of $X$. Then $Y^\perp$ is a closed linear subspace of $X'$.

^prop-36-7

> [!proof]+ Proof
> *Linear subspace.* The zero functional vanishes on $Y$. If $\ell_1, \ell_2$ vanish on $Y$ and $c_1, c_2 \in \mathbb{F}$, then $(c_1 \ell_1 + c_2 \ell_2)(y) = c_1 \ell_1(y) + c_2 \ell_2(y) = 0$ for $y \in Y$.
>
> *Closed.* Let $\ell_n \in Y^\perp$ with $\ell_n \to \ell$ in $X'$.
> For $y \in Y$,
>
> $$
> |\ell(y)| = |\ell(y) - \ell_n(y)| = |(\ell - \ell_n)(y)| \le \|\ell - \ell_n\|\, \|y\| \to 0 ,
> $$
>
> so $\ell(y) = 0$, and $\ell \in Y^\perp$.

^pf-36-7

> [!theorem] Theorem §36.8: The Dual of a Quotient
> Let $X$ be a normed linear space and $Y$ a closed linear subspace of $X$, so that $X/Y$ is a normed linear space with the quotient norm (Theorem [[§14 New Normed Spaces from Old#^thm-14-8|§14.8]]). Then $(X/Y)'$ is isometrically isomorphic to $Y^\perp$.

^thm-36-8

> [!proof]+ Proof
> (HW7, Problem 1.) Throughout, $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$ is the scalar field, $[x] = x + Y$ denotes the class of $x \in X$, and
>
> $$
> Y^\perp = \{ \ell \in X' : \ell(y) = 0 \text{ for all } y \in Y \},
> $$
>
> with the norm of $X'$ (Definition [[§36 Duality in Normed Spaces#^def-36-1|§36.1]]). Since $Y$ is closed, $X/Y$ is a normed linear space with the quotient norm (Theorem [[§14 New Normed Spaces from Old#^thm-14-8|§14.8]])
>
> $$
> \|[x]\| = \inf_{y \in Y} \|x + y\| ,
> $$
>
> so its dual $(X/Y)'$ is defined, with $\|\lambda\| = \sup_{[x] \neq [0]} |\lambda([x])| / \|[x]\|$. Let $\pi : X \to X/Y$, $\pi(x) = [x]$, be the quotient map. It is linear, and taking $y = 0$ in the infimum gives
>
> $$
> \|\pi(x)\| = \|[x]\| \le \|x\| \qquad \text{for all } x \in X. \tag{1}
> $$
>
> **Step 1: the map $T$.** For $\lambda \in (X/Y)'$ define $T\lambda = \lambda \circ \pi$, i.e.
>
> $$
> (T\lambda)(x) = \lambda([x]), \qquad x \in X .
> $$
>
> $T\lambda$ is linear as a composition of linear maps, and by (1),
>
> $$
> |(T\lambda)(x)| = |\lambda([x])| \le \|\lambda\|\, \|[x]\| \le \|\lambda\|\, \|x\| ,
> $$
>
> so $T\lambda \in X'$ with $\|T\lambda\| \le \|\lambda\|$. For $y \in Y$, $[y] = [0]$, so $(T\lambda)(y) = \lambda([0]) = 0$. Hence $T\lambda \in Y^\perp$, and $T : (X/Y)' \to Y^\perp$. $T$ is linear: for $\lambda_1, \lambda_2 \in (X/Y)'$, $c_1, c_2 \in \mathbb{F}$ and $x \in X$,
>
> $$
> T(c_1 \lambda_1 + c_2 \lambda_2)(x) = c_1 \lambda_1([x]) + c_2 \lambda_2([x]) = \bigl( c_1 T\lambda_1 + c_2 T\lambda_2 \bigr)(x) .
> $$
>
> **Step 2: $T$ is an isometry.** Step 1 gives $\|T\lambda\| \le \|\lambda\|$. For the reverse inequality, let $x \in X$ and $\varepsilon > 0$. By definition of the infimum there is $y \in Y$ with $\|x + y\| \le \|[x]\| + \varepsilon$. Since $[x + y] = [x]$,
>
> $$
> |\lambda([x])| = |\lambda([x + y])| = |(T\lambda)(x + y)| \le \|T\lambda\|\, \|x + y\| \le \|T\lambda\| \bigl( \|[x]\| + \varepsilon \bigr) .
> $$
>
> Letting $\varepsilon \to 0$, $|\lambda([x])| \le \|T\lambda\|\, \|[x]\|$ for every $[x] \in X/Y$, so $\|\lambda\| \le \|T\lambda\|$. Hence
>
> $$
> \|T\lambda\| = \|\lambda\| \qquad \text{for all } \lambda \in (X/Y)' .
> $$
>
> In particular $T$ is one-to-one: if $T\lambda_1 = T\lambda_2$, then $\|\lambda_1 - \lambda_2\| = \|T(\lambda_1 - \lambda_2)\| = 0$.
>
> **Step 3: $T$ is onto.** Let $\ell \in Y^\perp$. Define $\lambda : X/Y \to \mathbb{F}$ by
>
> $$
> \lambda([x]) = \ell(x) .
> $$
>
> This is well defined: if $[x] = [x']$, then $x - x' \in Y$, so $\ell(x) - \ell(x') = \ell(x - x') = 0$. It is linear: $\lambda(c_1 [x_1] + c_2 [x_2]) = \lambda([c_1 x_1 + c_2 x_2]) = \ell(c_1 x_1 + c_2 x_2) = c_1 \lambda([x_1]) + c_2 \lambda([x_2])$. It is bounded: for every $y \in Y$, $\ell(y) = 0$, so
>
> $$
> |\lambda([x])| = |\ell(x)| = |\ell(x + y)| \le \|\ell\|\, \|x + y\| ,
> $$
>
> and taking the infimum over $y \in Y$ gives $|\lambda([x])| \le \|\ell\|\, \|[x]\|$. Hence $\lambda \in (X/Y)'$, and $(T\lambda)(x) = \lambda([x]) = \ell(x)$ for all $x$, i.e. $T\lambda = \ell$.
>
> **Conclusion.** $T : (X/Y)' \to Y^\perp$ is linear (Step 1), norm-preserving and one-to-one (Step 2), and onto (Step 3). So $T$ is an isometric isomorphism of $(X/Y)'$ onto $Y^\perp$.

^pf-36-8

*Uses:* [[§36 Duality in Normed Spaces#^def-36-1|Def. §36.1]], [[§14 New Normed Spaces from Old#^thm-14-8|§14.8]]

> [!remark] Remark: No Hahn–Banach Needed Here
> *(Not from lecture.)* Every step of the proof is a direct computation with the quotient norm: Step 3 builds the functional on $X/Y$ from $\ell$ itself, so nothing has to be extended. The companion statement for a subspace, $Y' \cong X'/Y^\perp$ (the remark after Proposition [[§37 Separable Duals and Reflexive Spaces#^prop-37-9|§37.9]]), is different: there a functional on $Y$ must be extended to $X$, and onto-ness needs Hahn–Banach (Theorem [[§36 Duality in Normed Spaces#^thm-36-1|§36.1]]). Closedness of $Y$ is used only to make the quotient norm a norm; for a non-closed $Y$, $Y^\perp = (\overline{Y})^\perp$ (a bounded functional vanishing on $Y$ vanishes on its closure), and the theorem applies to $\overline{Y}$.

^rem-36-8

Wu's motivation: in a Hilbert space, $X = Y \oplus Y^\perp$ (Theorem [[§25 Projection and Orthogonal Decomposition#^thm-25-4|§25.4]]), and in any linear space $X \cong X/Y \oplus Y$ (Theorem [[§2 Quotient Spaces and Complements#^thm-2-6|§2.6]]); so $X/Y$ and $Y^\perp$ look like each other's dual. A student asked what “isometrically” means: both sides carry a norm — $(X/Y)'$ the dual norm of the quotient norm, $Y^\perp$ the norm of $X'$ — and the isomorphism preserves it. Wu: although today's material looks simple, it will be on the midterm.
