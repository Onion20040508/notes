---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 31
tags: [functional-analysis, math556]
---
← [[§30 Boundedness and Continuity]] · ↑ [[· 6 Bounded Linear Maps]] · [[§32 Sesquilinear Forms and the Lax–Milgram Theorem]] →

*Stage: maps — Thread: functionals. The bounded functionals on a space form a Banach space; on a Hilbert space it is the space itself.*

> [!definition] Definition §31.1: Dual Space
> Let $X$ be a normed linear space over $\mathbb{F}$. The set of bounded linear functionals on $X$,
>
> $$
> X' = \mathcal{L}(X, \mathbb{F}),
> $$
>
> with the norm $\|\ell\| = \sup_{x \neq 0} |\ell(x)|/\|x\|$, is the **dual space** of $X$. (Wu follows Lax's notation $X'$.)
>
> *Lax: §8.1, dual space*

^def-31-1

> [!remark]- Connections
> - The same space in the companion chapter, with the norm as an infimum: [[§34 Bras, Kets, and the Riesz Map#^def-34-1|Def. §34.1]], [[§34 Bras, Kets, and the Riesz Map#^lem-34-1|§34.1]]; the other special case of [[§30 Boundedness and Continuity#^def-30-4|Def. §30.4]] used there, bounded operators on $H$: [[§35 The Completeness Relation#^def-35-1|Def. §35.1]].
> - The algebraic dual in finite dimensions: [[§12 Duality#^ladr-3-108|LADR 3.108]], [[§12 Duality#^ladr-3-109|LADR 3.109]], [[§12 Duality#^ladr-3-110|LADR 3.110]]; [[§21 Linear Algebra Toolkit#^def-21-1|591 Def. §21.1]].

> [!theorem] Corollary §31.1: The Dual is Always a Banach Space
> For any normed linear space $X$ over $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, $X'$ is a Banach space, whether or not $X$ is complete.
>
> *Lax: §8.1, Thm 3*

^cor-31-1

> [!proof]+ Proof
> $\mathbb{F}$ is complete, so Theorem [[§30 Boundedness and Continuity#^thm-30-5|§30.5]](2) applies with $Y = \mathbb{F}$.

^pf-31-1

*Uses:* [[§30 Boundedness and Continuity#^thm-30-5|§30.5]], [[§12 Completeness#^def-12-2|Def. §12.2]], [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]]

> [!remark] Note: The Pairing $\langle x, \ell \rangle$
> For $\ell \in X'$ and $x \in X$ one often writes $\ell(x) = \langle x, \ell \rangle$. This is only notation, borrowed from inner product spaces: $\langle x, \ell \rangle$ pairs an element of $X$ with an element of $X'$, and is linear in $x$. In general $X'$ is a different space from $X$; on a Hilbert space the two can be identified, by the next theorem.

^rem-31-1

> [!theorem] Theorem §31.2: Riesz Representation Theorem, with Norms
> Let $H$ be a Hilbert space.
> - (1) For $a \in H$, $\ell_a(x) = (x, a)$ defines a bounded linear functional $\ell_a \in H'$ with $\|\ell_a\| = \|a\|$.
> - (2) For every $\ell \in H'$ there is a unique $a \in H$ with $\ell(x) = (x, a)$ for all $x \in H$; moreover $\|\ell\| = \|a\|$.
>
> *Lax: §6.3, Thm 4 (Lax does not state $\|\ell\| = \|a\|$)*

^thm-31-2

> [!proof]+ Proof
> (1) Linearity of $\ell_a$ is linearity of the inner product in its first slot. By [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]], $|\ell_a(x)| = |(x, a)| \le \|x\|\,\|a\|$, so
>
> $$
> \|\ell_a\| = \sup_{x \neq 0} \frac{|(x, a)|}{\|x\|} \le \|a\| .
> $$
>
> For equality, take $x = a$ (if $a = 0$ both sides are $0$): $\ell_a(a) = (a, a) = \|a\|^2$, so the ratio $|\ell_a(a)|/\|a\| = \|a\|$ is attained, and $\|\ell_a\| = \|a\|$.
>
> (2) Existence and uniqueness of $a$ are Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|§26.4]](2), proved in Lecture 8.
> (Uniqueness: if $(x, a) = (x, a')$ for all $x$, take $x = a - a'$ to get $\|a - a'\|^2 = 0$.) Then $\ell = \ell_a$, and $\|\ell\| = \|a\|$ by (1).

^pf-31-2

*Uses:* [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|§26.4]]

> [!remark]- Connections
> - This course's first statement, without norms: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|§26.4]]; the companion chapter's isometric Riesz map: [[§34 Bras, Kets, and the Riesz Map#^thm-34-2|§34.2]].
> - Finite-dimensional home: [[Riesz representation theorem]] ([[§21 Orthonormal Bases#^ladr-6-42|LADR 6.42]]).

> [!theorem] Corollary §31.3: The Riesz Map: $H' \cong H$
> The map $R : H \to H'$, $R(a) = \ell_a$, is one-to-one, onto, and norm-preserving: $\|R(a)\| = \|a\|$. It is additive, and $R(ca) = \bar{c}\, R(a)$ for scalars $c$; so $R$ is linear if $\mathbb{F} = \mathbb{R}$ and conjugate-linear if $\mathbb{F} = \mathbb{C}$.
>
> *Lax: §6.3, Thm 4; cf. §8.3, Thm 9*

^cor-31-3

> [!proof]+ Proof
> Onto and one-to-one are the existence and uniqueness in Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]](2), and $\|R(a)\| = \|a\|$ is part (1).
> For all $x$, $\ell_{a + b}(x) = (x, a + b) = (x, a) + (x, b)$ and $\ell_{ca}(x) = (x, ca) = \bar{c}\,(x, a)$, by conjugate-linearity of the inner product in its second slot.

^pf-31-3

*Uses:* [[§31 Dual Spaces#^thm-31-2|§31.2]], [[§22 Definition and Examples#^def-22-1|Def. §22.1]]

> [!remark]- Connections
> - The same map in the companion chapter, in bra–ket notation: [[§34 Bras, Kets, and the Riesz Map#^thm-34-2|§34.2]].

> [!remark] Remark
> Wu called $R$ an isometry and concluded that the dual of a Hilbert space can be identified with the space itself, $H' = H$, “through this Riesz representation.” Over $\mathbb{C}$ the identification is conjugate-linear, which is harmless for norms and distances: $\|R(a) - R(b)\| = \|R(a - b)\| = \|a - b\|$. The companion chapter writes the same map in bra–ket notation (Theorem [[§34 Bras, Kets, and the Riesz Map#^thm-34-2|§34.2]]).

^rem-31-2

> [!example] Example §31.1: $(L^2)' = L^2$ and $(\ell^2)' = \ell^2$
> $L^2(\Omega)$ is a Hilbert space with $(f, g) = \int_\Omega f(x)\, \overline{g(x)}\, dx$. By Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]], every bounded linear functional on $L^2(\Omega)$ is
>
> $$
> \ell(f) = \int_\Omega f(x)\, \overline{g(x)}\, dx \qquad \text{for a unique } g \in L^2(\Omega),
> $$
>
> with $\|\ell\| = \|g\|_{L^2}$. Likewise every $\ell \in (\ell^2)'$ is $\ell(a) = \sum_{j=1}^\infty a_j \overline{b_j}$ for a unique $b = (b_1, b_2, \ldots) \in \ell^2$, with $\|\ell\| = \|b\|_2$. A student asked which function carries the bar: the second one, since $\ell$ is linear in the function it acts on.
>
> *Lax: §6.3, Thm 4 with §6.1, Examples 2–3*

^ex-31-1

> [!remark] Remark: Not Every Space is its Own Dual
> A student asked whether the dual of every space is itself. No: the identification $X' = X$ is a Hilbert-space phenomenon, and “almost always” $X' \neq X$. The standard example, stated in lecture and to be proved next time, is below; the reason the exponent $p'$ appears is [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|Hölder's inequality]], which makes $\int f g$ meaningful for $f \in L^p$, $g \in L^{p'}$.

^rem-31-3

> [!remark]- Connections
> - Vault home of Hölder's inequality: [[Hölder's Inequality]] ([[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|551 §34.5]]).

> [!theorem] Theorem §31.4: The Dual of $L^p$
> Let $1 \le p < \infty$ and $\frac1p + \frac{1}{p'} = 1$. Then $(L^p)' = L^{p'}$: every $\ell \in (L^p)'$ is $\ell(f) = \int f g$ for a unique $g \in L^{p'}$, with $\|\ell\| = \|g\|_{L^{p'}}$.
>
> *Lax: §8.3, Thm 11*

^thm-31-4

> [!proof]+ Proof
> Next lecture.

^pf-31-4

> [!remark] Remark
> On the board: $(L^p)' = L^{p'}$ with no range for $p$. The range $1 \le p < \infty$ is added here: for $p = \infty$ the statement fails (the dual of $L^\infty$ is larger than $L^1$), which was not covered.

^rem-31-4

## Null Spaces of Linear Functionals

Lemmas [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-2|§26.2]] and [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]] described the null space of a bounded functional on a Hilbert space. Both facts hold in any normed space, and the first has a converse.

> [!theorem] Proposition §31.5: The Null Space Has Codimension One
> Let $X$ be a [[§1 Linear Spaces#^def-1-1|linear space]] over $\mathbb{F}$ and $\ell : X \to \mathbb{F}$ a nonzero [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-5|linear functional]], $N_\ell = \{x \in X : \ell(x) = 0\}$. Then $\dim X/N_\ell = 1$ ([[§2 Quotient Spaces and Complements#^def-2-2|quotient space]]). More precisely, for any $x_0$ with $\ell(x_0) \neq 0$, $X = N_\ell \oplus \operatorname{span}\{x_0\}$ ([[§1 Linear Spaces#^prop-1-3|internal direct sum]], [[§1 Linear Spaces#^def-1-5|linear span]]), with $x = \bigl( x - \frac{\ell(x)}{\ell(x_0)}\, x_0 \bigr) + \frac{\ell(x)}{\ell(x_0)}\, x_0$.
>
> *Source: HW5, Problem 4*
>
> *Lax: §6.3, Lemma 5(i)*

^prop-31-5

> [!proof]+ Proof
> (HW5, Problem 4.) Write $N = N_\ell$.
>
> **Step 1: a vector outside $N$.** Since $\ell$ is nontrivial, there is $x_0 \in X$ with $\ell(x_0) \neq 0$. In particular $x_0 \notin N$, so $[x_0] \neq [0]$ in $X/N$.
>
> **Step 2: every class is a multiple of $[x_0]$.** Let $x \in X$ and $k = \ell(x)/\ell(x_0) \in \mathbb{F}$. By linearity, $\ell(x - k x_0) = \ell(x) - \frac{\ell(x)}{\ell(x_0)}\, \ell(x_0) = 0$, so $y := x - k x_0 \in N$. Hence $[x] = [k x_0] = k [x_0]$.
>
> **Step 3: conclusion.** By Step 2, $X/N = \operatorname{span}\{[x_0]\}$, and by Step 1, $[x_0] \neq [0]$, so $\{[x_0]\}$ is a basis of $X/N$ and $\dim X/N = 1$. Equivalently, $X = N \oplus \operatorname{span}\{x_0\}$: by Step 2 every $x$ is $x = y + k x_0$ with $y \in N$; and $N \cap \operatorname{span}\{x_0\} = \{0\}$, since $\ell(c x_0) = c\,\ell(x_0) = 0$ forces $c = 0$.

^pf-31-5

*Uses:* [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-5|Def. §3.5]], [[§2 Quotient Spaces and Complements#^def-2-1|Def. §2.1]], [[§2 Quotient Spaces and Complements#^def-2-2|Def. §2.2]], [[§2 Quotient Spaces and Complements#^prop-2-1|§2.1]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]], [[§1 Linear Spaces#^prop-1-3|§1.3]], [[§5 Bases#^ladr-2-26|LADR 2.26]], [[§6 Dimension#^ladr-2-35|LADR 2.35]]

> [!remark]- Connections
> - The Hilbert-space case, with the line $N^\perp$ as the complement: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]]; the move “subtract a multiple of $x_0$”: [[Functional Analysis Problem-Solving Techniques#^rem-t18|Technique 18]].
> - Linear algebra: null space [[§8 Null Spaces and Ranges#^ladr-3-11|LADR 3.11]]; $X/N_\ell \cong \operatorname{range} \ell = \mathbb{F}$ is [[§11 Products and Quotients of Vector Spaces#^ladr-3-107|LADR 3.107]](d) ([[First isomorphism theorem]]); in finite dimensions, $\dim N_\ell = \dim X - 1$ by [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]].
> - The complement $\operatorname{span}\{x_0\}$ as a model of $X/N_\ell$: [[§2 Quotient Spaces and Complements#^cor-2-7|§2.7]].

> [!theorem] Proposition §31.6: Bounded if and only if the Null Space is Closed
> Let $X$ be a [[§11 Normed Linear Spaces#^def-11-1|normed linear space]] over $\mathbb{F}$ and $\ell : X \to \mathbb{F}$ a [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-5|linear functional]]. Then $\ell \in X'$ ([[§31 Dual Spaces#^def-31-1|Def. §31.1]]) if and only if $N_\ell$ ([[§31 Dual Spaces#^prop-31-5|§31.5]]) is [[§11 Normed Linear Spaces#^def-11-6|closed]].
>
> *Source: HW5, Problem 5*
>
> *Lax: §6.3, Lemma 5(iii)*

^prop-31-6

> [!proof]+ Proof
> (HW5, Problem 5.) **($\Rightarrow$)** Let $\ell \in X'$, and let $x_n \in N_\ell$ with $x_n \to x$ in $X$. Since $\ell$ is bounded, it is continuous (Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]]), so $\ell(x) = \lim_n \ell(x_n) = 0$, i.e. $x \in N_\ell$.
>
> **($\Leftarrow$)** Assume $N_\ell$ is closed. If $\ell = 0$, then $\ell \in X'$. So assume $\ell \neq 0$, and choose $x_0$ with $\ell(x_0) \neq 0$; replacing $x_0$ by $x_0/\ell(x_0)$, we may assume $\ell(x_0) = 1$. Suppose, for contradiction, that $\ell$ is not bounded. Then for each $n \in \mathbb{N}$ there is $x_n \in X$ with $|\ell(x_n)| > n\,\|x_n\|$; in particular $\ell(x_n) \neq 0$. Let
>
> $$
> y_n = x_0 - \frac{x_n}{\ell(x_n)} .
> $$
>
> Then $\ell(y_n) = 1 - 1 = 0$, so $y_n \in N_\ell$, and $\|y_n - x_0\| = \|x_n\|/|\ell(x_n)| < 1/n \to 0$. So $y_n \to x_0$ with every $y_n \in N_\ell$; since $N_\ell$ is closed, $x_0 \in N_\ell$, contradicting $\ell(x_0) = 1$. Hence $\ell$ is bounded.

^pf-31-6

*Uses:* [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]], [[§11 Normed Linear Spaces#^def-11-6|Def. §11.6]], [[§11 Normed Linear Spaces#^def-11-4|Def. §11.4]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - The Hilbert-space (⇒) direction: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-2|§26.2]]; “continuous iff bounded”: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-1|§26.1]] for functionals, [[§30 Boundedness and Continuity#^prop-30-2|§30.2]] for maps.
> - The sequence $y_n = x_0 - x_n/\ell(x_n)$ is [[Functional Analysis Problem-Solving Techniques#^ex-t18|Technique 18]].

![[m556-22-1.svg]]
*Points $y_n$ of $N_\ell$ with $\|y_n - x_0\| < \frac1n$, approaching $x_0$, $\ell(x_0) = 1$, off the null space.*

The picture behind ($\Leftarrow$): if $\ell$ were unbounded, points $y_n$ of the null space would approach a point $x_0$ off it, so the null space could not be closed. (The picture is schematic: in finite dimensions every functional is bounded, and an unbounded $\ell$ has a *dense* null space.)

> [!remark] Remark
> Proposition [[§31 Dual Spaces#^prop-31-5|§31.5]] is pure algebra; Proposition [[§31 Dual Spaces#^prop-31-6|§31.6]] is where the norm enters. Together they say that the null space of a nonzero functional is a “hyperplane through $0$” ([[§5 Statement and Motivation#^def-5-3|Def. §5.3]]) that is either closed (bounded $\ell$) or not (unbounded $\ell$). Both proofs use the same move: subtract from $x$ the multiple of $x_0$ that lands it in the null space.

^rem-31-5
