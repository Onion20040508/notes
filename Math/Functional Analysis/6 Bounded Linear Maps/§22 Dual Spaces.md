---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 22
tags: [functional-analysis, math556]
---
← [[§21 Boundedness and Continuity]] · ↑ [[· 6 Bounded Linear Maps]] · [[§23 Sesquilinear Forms and the Lax–Milgram Theorem]] →

*Stage: maps — Thread: functionals. The bounded functionals on a space form a Banach space; on a Hilbert space it is the space itself.*

> [!definition] Definition §22.1: Dual Space
> Let $X$ be a normed linear space over $\mathbb{F}$. The set of bounded linear functionals on $X$,
>
> $$
> X' = \mathcal{L}(X, \mathbb{F}),
> $$
>
> with the norm $\|\ell\| = \sup_{x \neq 0} |\ell(x)|/\|x\|$, is the **dual space** of $X$. (Wu follows Lax's notation $X'$.)
>
> *Lax: §8.1, dual space*

^def-22-1

> [!remark]- Connections
> - The same space in the companion chapter, with the norm as an infimum: [[§24 Bras, Kets, and the Riesz Map#^def-24-1|Def. §24.1]], [[§24 Bras, Kets, and the Riesz Map#^lem-24-1|§24.1]]; the other special case of [[§21 Boundedness and Continuity#^def-21-3|Def. §21.3]] used there, bounded operators on $H$: [[§25 The Completeness Relation#^def-25-1|Def. §25.1]].
> - The algebraic dual in finite dimensions: [[§12 Duality#^ladr-3-108|LADR 3.108]], [[§12 Duality#^ladr-3-109|LADR 3.109]], [[§12 Duality#^ladr-3-110|LADR 3.110]]; [[§10 Vector Spaces and Matrix Groups#^def-10-1|591 Def. §10.1]].

> [!theorem] Corollary §22.1: The Dual is Always a Banach Space
> For any normed linear space $X$ over $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, $X'$ is a Banach space, whether or not $X$ is complete.
>
> *Lax: §8.1, Thm 3*

^cor-22-1

> [!proof]+ Proof
> $\mathbb{F}$ is complete, so Theorem [[§21 Boundedness and Continuity#^thm-21-5|§21.5]](2) applies with $Y = \mathbb{F}$.

^pf-22-1

*Uses:* [[§21 Boundedness and Continuity#^thm-21-5|§21.5]], [[§9 Completeness#^def-9-2|Def. §9.2]], [[§22 Dual Spaces#^def-22-1|Def. §22.1]]

> [!remark] Note: The Pairing $\langle x, \ell \rangle$
> For $\ell \in X'$ and $x \in X$ one often writes $\ell(x) = \langle x, \ell \rangle$. This is only notation, borrowed from inner product spaces: $\langle x, \ell \rangle$ pairs an element of $X$ with an element of $X'$, and is linear in $x$. In general $X'$ is a different space from $X$; on a Hilbert space the two can be identified, by the next theorem.

^rem-22-1

> [!theorem] Theorem §22.2: Riesz Representation Theorem, with Norms
> Let $H$ be a Hilbert space.
> - (1) For $a \in H$, $\ell_a(x) = (x, a)$ defines a bounded linear functional $\ell_a \in H'$ with $\|\ell_a\| = \|a\|$.
> - (2) For every $\ell \in H'$ there is a unique $a \in H$ with $\ell(x) = (x, a)$ for all $x \in H$; moreover $\|\ell\| = \|a\|$.
>
> *Lax: §6.3, Thm 4 (Lax does not state $\|\ell\| = \|a\|$)*

^thm-22-2

> [!proof]+ Proof
> (1) Linearity of $\ell_a$ is linearity of the inner product in its first slot. By [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Cauchy–Schwarz]], $|\ell_a(x)| = |(x, a)| \le \|x\|\,\|a\|$, so
>
> $$
> \|\ell_a\| = \sup_{x \neq 0} \frac{|(x, a)|}{\|x\|} \le \|a\| .
> $$
>
> For equality, take $x = a$ (if $a = 0$ both sides are $0$): $\ell_a(a) = (a, a) = \|a\|^2$, so the ratio $|\ell_a(a)|/\|a\| = \|a\|$ is attained, and $\|\ell_a\| = \|a\|$.
>
> (2) Existence and uniqueness of $a$ are Theorem [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|§19.2]](2), proved in Lecture 8.
> (Uniqueness: if $(x, a) = (x, a')$ for all $x$, take $x = a - a'$ to get $\|a - a'\|^2 = 0$.) Then $\ell = \ell_a$, and $\|\ell\| = \|a\|$ by (1).

^pf-22-2

*Uses:* [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§22 Dual Spaces#^def-22-1|Def. §22.1]], [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|§19.2]]

> [!remark]- Connections
> - This course's first statement, without norms: [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-19-2|§19.2]]; the companion chapter's isometric Riesz map: [[§24 Bras, Kets, and the Riesz Map#^thm-24-2|§24.2]].
> - Finite-dimensional home: [[Riesz representation theorem]] ([[§20 Orthonormal Bases#^ladr-6-42|LADR 6.42]]).

> [!theorem] Corollary §22.3: The Riesz Map: $H' \cong H$
> The map $R : H \to H'$, $R(a) = \ell_a$, is one-to-one, onto, and norm-preserving: $\|R(a)\| = \|a\|$. It is additive, and $R(ca) = \bar{c}\, R(a)$ for scalars $c$; so $R$ is linear if $\mathbb{F} = \mathbb{R}$ and conjugate-linear if $\mathbb{F} = \mathbb{C}$.
>
> *Lax: §6.3, Thm 4; cf. §8.3, Thm 9*

^cor-22-3

> [!proof]+ Proof
> Onto and one-to-one are the existence and uniqueness in Theorem [[§22 Dual Spaces#^thm-22-2|§22.2]](2), and $\|R(a)\| = \|a\|$ is part (1).
> For all $x$, $\ell_{a + b}(x) = (x, a + b) = (x, a) + (x, b)$ and $\ell_{ca}(x) = (x, ca) = \bar{c}\,(x, a)$, by conjugate-linearity of the inner product in its second slot.

^pf-22-3

*Uses:* [[§22 Dual Spaces#^thm-22-2|§22.2]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]]

> [!remark]- Connections
> - The same map in the companion chapter, in bra–ket notation: [[§24 Bras, Kets, and the Riesz Map#^thm-24-2|§24.2]].

> [!remark] Remark
> Wu called $R$ an isometry and concluded that the dual of a Hilbert space can be identified with the space itself, $H' = H$, “through this Riesz representation.” Over $\mathbb{C}$ the identification is conjugate-linear, which is harmless for norms and distances: $\|R(a) - R(b)\| = \|R(a - b)\| = \|a - b\|$. The companion chapter writes the same map in bra–ket notation (Theorem [[§24 Bras, Kets, and the Riesz Map#^thm-24-2|§24.2]]).

^rem-22-2

> [!example] Example §22.1: $(L^2)' = L^2$ and $(\ell^2)' = \ell^2$
> $L^2(\Omega)$ is a Hilbert space with $(f, g) = \int_\Omega f(x)\, \overline{g(x)}\, dx$. By Theorem [[§22 Dual Spaces#^thm-22-2|§22.2]], every bounded linear functional on $L^2(\Omega)$ is
>
> $$
> \ell(f) = \int_\Omega f(x)\, \overline{g(x)}\, dx \qquad \text{for a unique } g \in L^2(\Omega),
> $$
>
> with $\|\ell\| = \|g\|_{L^2}$. Likewise every $\ell \in (\ell^2)'$ is $\ell(a) = \sum_{j=1}^\infty a_j \overline{b_j}$ for a unique $b = (b_1, b_2, \ldots) \in \ell^2$, with $\|\ell\| = \|b\|_2$. A student asked which function carries the bar: the second one, since $\ell$ is linear in the function it acts on.
>
> *Lax: §6.3, Thm 4 with §6.1, Examples 2–3*

^ex-22-1

> [!remark] Remark: Not Every Space is its Own Dual
> A student asked whether the dual of every space is itself. No: the identification $X' = X$ is a Hilbert-space phenomenon, and “almost always” $X' \neq X$. The standard example, stated in lecture and to be proved next time, is below; the reason the exponent $p'$ appears is [[§14 The Function Spaces Lᵖ(Ω)#^thm-14-1|Hölder's inequality]], which makes $\int f g$ meaningful for $f \in L^p$, $g \in L^{p'}$.

^rem-22-3

> [!remark]- Connections
> - Vault home of Hölder's inequality: [[Hölder's Inequality]] ([[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-5|551 §19.5]]).

> [!theorem] Theorem §22.4: The Dual of $L^p$
> Let $1 \le p < \infty$ and $\frac1p + \frac{1}{p'} = 1$. Then $(L^p)' = L^{p'}$: every $\ell \in (L^p)'$ is $\ell(f) = \int f g$ for a unique $g \in L^{p'}$, with $\|\ell\| = \|g\|_{L^{p'}}$.
>
> *Lax: §8.3, Thm 11*

^thm-22-4

> [!proof]+ Proof
> Next lecture.

^pf-22-4

> [!remark] Remark
> On the board: $(L^p)' = L^{p'}$ with no range for $p$. The range $1 \le p < \infty$ is added here: for $p = \infty$ the statement fails (the dual of $L^\infty$ is larger than $L^1$), which was not covered.

^rem-22-4
