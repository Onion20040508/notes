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
> with the norm $\|\ell\| = \sup_{x \neq 0} |\ell(x)|/\|x\|$, is the **dual space** of $X$. (The notation $X'$ is Lax's.)
>
> *Lax: §8.1, dual space*

^def-31-1

> [!remark]- Connections
> - The same space is recalled in the companion chapter, with the norm as the smallest admissible constant (Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]]): [[§46 Bras, Kets, and the Riesz Map|§46]]; the other special case of [[§30 Boundedness and Continuity#^def-30-4|Def. §30.4]] used there, bounded operators on $H$ ([[§30 Boundedness and Continuity#^def-30-2|Def. §30.2]]): [[§47 The Completeness Relation|§47]].
> - The algebraic dual in finite dimensions: [[§12 Duality#^ladr-3-108|LADR 3.108]], [[§12 Duality#^ladr-3-109|LADR 3.109]], [[§12 Duality#^ladr-3-110|LADR 3.110]]; [[§21 Linear Algebra Toolkit#^def-21-1|591 Def. §21.1]].

> [!theorem] Corollary §31.1: The Dual is Always a Banach Space
> For any normed linear space $X$ over $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, $X'$ is a Banach space, whether or not $X$ is complete.
>
> *Lax: §8.1, Thm 3*

^cor-31-1

> [!proof]+ Proof
> $\mathbb{F}$ is complete, so Theorem [[§30 Boundedness and Continuity#^thm-30-8|§30.8]](2) applies with $Y = \mathbb{F}$.

^pf-31-1

*Uses:* [[§30 Boundedness and Continuity#^thm-30-8|§30.8]], [[§12 Completeness#^def-12-2|Def. §12.2]], [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§10a Cauchy Sequences#^thm-10a-3|451 §10a.3]]

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
> (2) Existence and uniqueness of $a$ are Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]](2), proved in Lecture 8.
> (Uniqueness: if $(x, a) = (x, a')$ for all $x$, take $x = a - a'$ to get $\|a - a'\|^2 = 0$.) Then $\ell = \ell_a$, and $\|\ell\| = \|a\|$ by (1).

^pf-31-2

*Uses:* [[§22 Definition and Examples#^def-22-1|Def. §22.1]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]]

> [!remark]- Connections
> - This course's first statement, without norms: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-5|§26.5]]; the companion chapter's isometric Riesz map: [[§46 Bras, Kets, and the Riesz Map#^thm-46-1|§46.1]].
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
> - The same map in the companion chapter, in bra–ket notation: [[§46 Bras, Kets, and the Riesz Map#^thm-46-1|§46.1]].

> [!remark] Remark
> $R$ is an isometry, so the dual of a Hilbert space can be identified with the space itself, $H' = H$, through the Riesz representation. Over $\mathbb{C}$ the identification is conjugate-linear, which is harmless for norms and distances: $\|R(a) - R(b)\| = \|R(a - b)\| = \|a - b\|$. The companion chapter writes the same map in bra–ket notation (Theorem [[§46 Bras, Kets, and the Riesz Map#^thm-46-1|§46.1]]).

^rem-31-2

> [!example] Example §31.1: $(L^2)' = L^2$ and $(\ell^2)' = \ell^2$
> $L^2(\Omega)$ is a Hilbert space with $(f, g) = \int_\Omega f(x)\, \overline{g(x)}\, dx$. By Theorem [[§31 Dual Spaces#^thm-31-2|§31.2]], every bounded linear functional on $L^2(\Omega)$ is
>
> $$
> \ell(f) = \int_\Omega f(x)\, \overline{g(x)}\, dx \qquad \text{for a unique } g \in L^2(\Omega),
> $$
>
> with $\|\ell\| = \|g\|_{L^2}$. Likewise every $\ell \in (\ell^2)'$ is $\ell(a) = \sum_{j=1}^\infty a_j \overline{b_j}$ for a unique $b = (b_1, b_2, \ldots) \in \ell^2$, with $\|\ell\| = \|b\|_2$. The bar is on the second function, since $\ell$ is linear in the function it acts on.
>
> *Lax: §6.3, Thm 4 with §6.1, Examples 2–3*

^ex-31-1

> [!remark] Remark: Not Every Space is its Own Dual
> The dual of a space is in general not the space itself: the identification $X' = X$ is a Hilbert-space phenomenon, and almost always $X' \neq X$. The standard example, stated in lecture and proved for sequences in Lecture 13 (Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]]), is below; the reason the exponent $p'$ appears is [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|Hölder's inequality]], which makes $\int f g$ meaningful for $f \in L^p$, $g \in L^{p'}$.

^rem-31-3

> [!remark]- Connections
> - Vault home of Hölder's inequality: [[Hölder's Inequality]] ([[§34 Normed Linear Spaces and Lᵖ Spaces#^thm-34-5|551 §34.5]]).

> [!theorem] Theorem §31.4: The Dual of $L^p$
> Let $1 \le p < \infty$ and $\frac1p + \frac{1}{p'} = 1$. Then $(L^p)' = L^{p'}$: every $\ell \in (L^p)'$ is $\ell(f) = \int f g$ for a unique $g \in L^{p'}$, with $\|\ell\| = \|g\|_{L^{p'}}$.
>
> *Lax: §8.3, Thm 11*

^thm-31-4

> [!proof]+ Proof (outline; not proved in lecture)
> Not proved in lecture. Lecture 13 proves the sequence version, Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]]; the $L^p$ case is similar: those who know measure theory find the candidate $g$ with the Radon–Nikodym theorem and then argue as for sequences. This needs measure theory beyond the course.
>
> *Outline, along that route.* Measure-theoretic facts are used freely. Suppose first that $\Omega$ has finite measure $m(\Omega)$, and let $\ell \in (L^p)'$.
>
> (i) *The candidate.* For measurable $E \subset \Omega$ put $\nu(E) = \ell(\chi_E)$. If $E = \bigcup_k E_k$ is a disjoint union, then $\|\chi_E - \sum_{k \le n} \chi_{E_k}\|_{L^p} = m\bigl( \bigcup_{k > n} E_k \bigr)^{1/p} \to 0$ (here $p < \infty$), so continuity of $\ell$ gives $\nu(E) = \sum_k \nu(E_k)$; and $m(E) = 0$ gives $\chi_E = 0$ in $L^p$, so $\nu(E) = 0$. Thus $\nu$ is a (real or complex) measure with $\nu \ll m$. Theorem [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|§35.1]] is stated for positive measures; applied to the positive and negative parts of $\operatorname{Re}\nu$ and $\operatorname{Im}\nu$ (Jordan decomposition), it gives $g \in L^1(\Omega)$ with $\ell(\chi_E) = \int_E g$ for all $E$. By linearity $\ell(s) = \int s g$ for simple $s$; and since a bounded measurable $f$ is a uniform limit of simple $s_k$, with $\|f - s_k\|_{L^p} \le m(\Omega)^{1/p} \|f - s_k\|_\infty \to 0$ and $|\int (f - s_k) g| \le \|f - s_k\|_\infty \|g\|_{L^1} \to 0$, also $\ell(f) = \int f g$ for bounded measurable $f$. This is the analogue of (F) in the proof of Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]].
>
> (ii) *$g \in L^{p'}$, as in Step 2 of the proof of Theorem [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]].* For $1 < p < \infty$ test with the bounded function $f_n = |g|^{p'-2}\, \bar g\, \chi_{\{0 < |g| \le n\}}$: then $|f_n|^p = |g|^{p'} \chi_{\{|g| \le n\}}$ and $\ell(f_n) = \int_{\{|g| \le n\}} |g|^{p'} =: S_n$, so $S_n \le \|\ell\|\, S_n^{1/p}$, hence $S_n^{1/p'} \le \|\ell\|$, and the monotone convergence theorem gives $\|g\|_{L^{p'}} \le \|\ell\|$. For $p = 1$ and $\varepsilon > 0$, test with $f = \chi_A\, \bar g/|g|$, $A = \{ |g| > \|\ell\| + \varepsilon \}$: then $(\|\ell\| + \varepsilon)\, m(A) \le \int_A |g| = \ell(f) \le \|\ell\|\, m(A)$, so $m(A) = 0$ and $\|g\|_{L^\infty} \le \|\ell\|$.
>
> (iii) *$\ell(f) = \int f g$ on all of $L^p$, as in Step 3 of that proof.* The bounded functions $f\, \chi_{\{|f| \le n\}}$ converge to $f$ in $L^p$ (dominated convergence, $p < \infty$); both sides of $\ell(f) = \int f g$ are continuous in $f$ (the right side by Hölder), so the identity extends from bounded $f$ to all $f \in L^p$. Hölder gives $\|\ell\| \le \|g\|_{L^{p'}}$, so $\|\ell\| = \|g\|_{L^{p'}}$; and $g$ is unique, since $\int_E (g - \tilde g) = 0$ for all $E$ forces $g = \tilde g$ a.e.
>
> (iv) *$\Omega$ of infinite measure.* Apply (i)–(iii) on $\Omega_k = \Omega \cap B_k(0)$ to the restriction of $\ell$ to functions vanishing outside $\Omega_k$; by uniqueness the resulting $g_k$ agree a.e. on overlaps and define one $g$ on $\Omega$ with $\|g\, \chi_{\Omega_k}\|_{L^{p'}} \le \|\ell\|$ for all $k$, hence $\|g\|_{L^{p'}} \le \|\ell\|$; and the functions vanishing outside some $\Omega_k$ are dense in $L^p(\Omega)$.

^pf-31-4

*Uses:* [[§36 Duality in Normed Spaces#^thm-36-4|§36.4]], [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|§35.1]], [[§19 The Function Spaces Lᵖ(Ω)#^thm-19-1|§19.1]]

> [!remark] Remark
> On the board: $(L^p)' = L^{p'}$ with no range for $p$. The range $1 \le p < \infty$ is added here: for $p = \infty$ the statement fails (the dual of $L^\infty$ is larger than $L^1$), as noted in Lecture 13 (Example [[§36 Duality in Normed Spaces#^ex-36-2|§36.2]]).

^rem-31-4

## An Integral Functional on $C[0,1]$

A first dual norm computed by hand. The space is $C[0,1]$ with the maximum norm $\|x\| = \max_{t \in [0,1]} |x(t)|$ (a Banach space, Theorem [[§12 Completeness#^thm-12-1|§12.1]]), with real or complex values.

> [!theorem] Proposition §31.5: The Norm of $x \mapsto \int_0^1 f_0\, x\, dt$ on $C[0,1]$
> Let $f_0 \in C[0,1]$ be given and define
>
> $$
> \ell(x) = \int_0^1 f_0(t)\, x(t)\, dt \qquad \text{for } x \in C[0,1] .
> $$
>
> Then $\ell$ is a bounded linear functional on $C[0,1]$, and
>
> $$
> \|\ell\| = \int_0^1 |f_0(t)|\, dt .
> $$
>
> *Source: HW8, Problem 1*

^prop-31-5

> [!proof]+ Proof
> *(HW8, Problem 1. Not from lecture; filled in.)* Write $A = \int_0^1 |f_0(t)|\, dt$. Linearity of $\ell$ is linearity of the integral. We show $\|\ell\| \le A$ and $\|\ell\| \ge A - \varepsilon$ for every $\varepsilon > 0$, where $\|\ell\| = \sup_{x \neq 0} |\ell(x)| / \|x\|$ (Definition [[§31 Dual Spaces#^def-31-1|§31.1]]).
>
> **Step 1: $\|\ell\| \le A$.** For $x \in C[0,1]$, $|x(t)| \le \|x\|$ for all $t$, so
>
> $$
> |\ell(x)| \le \int_0^1 |f_0(t)|\, |x(t)|\, dt \le \|x\| \int_0^1 |f_0(t)|\, dt = A\, \|x\| .
> $$
>
> So $\ell$ is bounded and $\|\ell\| \le A$.
>
> **Step 2: test functions.** Equality in Step 1 would need $x(t) = \overline{f_0(t)} / |f_0(t)|$, which is not defined where $f_0 = 0$ and need not extend continuously there. Instead, for $\varepsilon > 0$ put
>
> $$
> x_\varepsilon(t) = \frac{\overline{f_0(t)}}{|f_0(t)| + \varepsilon} .
> $$
>
> The denominator is continuous and at least $\varepsilon > 0$, so $x_\varepsilon \in C[0,1]$, and $|x_\varepsilon(t)| = \frac{|f_0(t)|}{|f_0(t)| + \varepsilon} < 1$, so $\|x_\varepsilon\| \le 1$.
>
> **Step 3: $\|\ell\| \ge A - \varepsilon$.** Since $f_0 \overline{f_0} = |f_0|^2$,
>
> $$
> \ell(x_\varepsilon) = \int_0^1 \frac{|f_0(t)|^2}{|f_0(t)| + \varepsilon}\, dt .
> $$
>
> For a number $s \ge 0$, $\frac{s^2}{s + \varepsilon} = s - \frac{\varepsilon s}{s + \varepsilon} \ge s - \varepsilon$, because $\frac{s}{s + \varepsilon} \le 1$. With $s = |f_0(t)|$ and integrating over $[0,1]$,
>
> $$
> \ell(x_\varepsilon) \ge \int_0^1 \bigl( |f_0(t)| - \varepsilon \bigr)\, dt = A - \varepsilon .
> $$
>
> By Proposition [[§30 Boundedness and Continuity#^prop-30-1|§30.1]](b) with $Y = \mathbb{F}$ and $\|x_\varepsilon\| \le 1$, $|\ell(x_\varepsilon)| \le \|\ell\|\, \|x_\varepsilon\| \le \|\ell\|$. So $\|\ell\| \ge A - \varepsilon$ for every $\varepsilon > 0$, hence $\|\ell\| \ge A$. With Step 1, $\|\ell\| = A$.

^pf-31-5

*Uses:* [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§30 Boundedness and Continuity#^prop-30-1|§30.1]]

> [!example] Example §31.2: The Norm of the Integral Functional Need Not be Attained
> *(Not from lecture.)* Let $f_0(t) = t - \frac12$ in Proposition [[§31 Dual Spaces#^prop-31-5|§31.5]], so $\|\ell\| = \int_0^1 |t - \frac12|\, dt = \frac14$. There is no $x \in C[0,1]$ with $\|x\| \le 1$ and $|\ell(x)| = \|\ell\|$: the supremum defining $\|\ell\|$ is not a maximum.

^ex-31-2

> [!proof]+ Proof
> Suppose $x \in C[0,1]$, $\|x\| \le 1$ and $|\ell(x)| = \frac14$. Multiplying $x$ by a scalar of absolute value $1$ (which changes neither $\|x\|$ nor $|\ell(x)|$) we may assume $\ell(x) = \frac14$. Then
>
> $$
> \int_0^1 \Bigl( |f_0(t)| - \operatorname{Re}\bigl( f_0(t)\, x(t) \bigr) \Bigr) dt = \tfrac14 - \operatorname{Re} \ell(x) = 0 .
> $$
>
> The integrand is continuous, and it is non-negative because $\operatorname{Re}(f_0 x) \le |f_0|\, |x| \le |f_0|$. By Lemma [[§19 The Function Spaces Lᵖ(Ω)#^lem-19-6|§19.6]] it vanishes identically: $\operatorname{Re}\bigl( f_0(t) x(t) \bigr) = |f_0(t)|$ for all $t$. Since $f_0$ is real, this reads $(t - \frac12) \operatorname{Re} x(t) = |t - \frac12|$, so $\operatorname{Re} x(t) = -1$ for $t < \frac12$ and $\operatorname{Re} x(t) = 1$ for $t > \frac12$. Then $\operatorname{Re} x$ has left limit $-1$ and right limit $1$ at $t = \frac12$, which contradicts the continuity of $x$.

^pf-ex-31-2

*Uses:* [[§19 The Function Spaces Lᵖ(Ω)#^lem-19-6|Lem. §19.6]]

## Null Spaces of Linear Functionals

Lemmas [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]] and [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-4|§26.4]] described the null space of a bounded functional on a Hilbert space. Both facts hold in any normed space, and the first has a converse.

> [!theorem] Proposition §31.6: The Null Space Has Codimension One
> Let $X$ be a [[§1 Linear Spaces#^def-1-1|linear space]] over $\mathbb{F}$ and $\ell : X \to \mathbb{F}$ a nonzero [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-5|linear functional]], $N_\ell = \{x \in X : \ell(x) = 0\}$. Then $\dim X/N_\ell = 1$ ([[§2 Quotient Spaces and Complements#^def-2-3|quotient space]]). More precisely, for any $x_0$ with $\ell(x_0) \neq 0$, $X = N_\ell \oplus \operatorname{span}\{x_0\}$ ([[§1 Linear Spaces#^prop-1-3|internal direct sum]], [[§1 Linear Spaces#^def-1-5|linear span]]), with $x = \bigl( x - \frac{\ell(x)}{\ell(x_0)}\, x_0 \bigr) + \frac{\ell(x)}{\ell(x_0)}\, x_0$.
>
> *Source: HW5, Problem 4*
>
> *Lax: §6.3, Lemma 5(i)*

^prop-31-6

> [!proof]+ Proof
> (HW5, Problem 4.) Write $N = N_\ell$.
>
> **Step 1: a vector outside $N$.** Since $\ell$ is nontrivial, there is $x_0 \in X$ with $\ell(x_0) \neq 0$. In particular $x_0 \notin N$, so $[x_0] \neq [0]$ in $X/N$.
>
> **Step 2: every class is a multiple of $[x_0]$.** Let $x \in X$ and $k = \ell(x)/\ell(x_0) \in \mathbb{F}$. By linearity, $\ell(x - k x_0) = \ell(x) - \frac{\ell(x)}{\ell(x_0)}\, \ell(x_0) = 0$, so $y := x - k x_0 \in N$. Hence $[x] = [k x_0] = k [x_0]$.
>
> **Step 3: conclusion.** By Step 2, $X/N = \operatorname{span}\{[x_0]\}$, and by Step 1, $[x_0] \neq [0]$, so $\{[x_0]\}$ is a basis of $X/N$ and $\dim X/N = 1$. Equivalently, $X = N \oplus \operatorname{span}\{x_0\}$: by Step 2 every $x$ is $x = y + k x_0$ with $y \in N$; and $N \cap \operatorname{span}\{x_0\} = \{0\}$, since $\ell(c x_0) = c\,\ell(x_0) = 0$ forces $c = 0$.

^pf-31-6

*Uses:* [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-5|Def. §3.5]], [[§2 Quotient Spaces and Complements#^def-2-1|Def. §2.1]], [[§2 Quotient Spaces and Complements#^def-2-2|Def. §2.2]], [[§2 Quotient Spaces and Complements#^def-2-3|Def. §2.3]], [[§2 Quotient Spaces and Complements#^prop-2-2|§2.2]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]], [[§1 Linear Spaces#^prop-1-3|§1.3]], [[§5 Bases#^ladr-2-26|LADR 2.26]], [[§6 Dimension#^ladr-2-35|LADR 2.35]]

> [!remark]- Connections
> - The Hilbert-space case, with the line $N^\perp$ as the complement: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-4|§26.4]]; the move “subtract a multiple of $x_0$”: [[Functional Analysis Problem-Solving Techniques#^rem-t18|Technique 18]].
> - Linear algebra: null space [[§8 Null Spaces and Ranges#^ladr-3-11|LADR 3.11]]; $X/N_\ell \cong \operatorname{range} \ell = \mathbb{F}$ is [[§11 Products and Quotients of Vector Spaces#^ladr-3-107|LADR 3.107]](d) ([[First isomorphism theorem]]); in finite dimensions, $\dim N_\ell = \dim X - 1$ by [[§11 Products and Quotients of Vector Spaces#^ladr-3-105|LADR 3.105]].
> - The complement $\operatorname{span}\{x_0\}$ as a model of $X/N_\ell$: [[§2 Quotient Spaces and Complements#^cor-2-8|§2.8]].

> [!theorem] Proposition §31.7: Bounded if and only if the Null Space is Closed
> Let $X$ be a [[§11 Normed Linear Spaces#^def-11-1|normed linear space]] over $\mathbb{F}$ and $\ell : X \to \mathbb{F}$ a [[§3 Linear Maps, Convexity, and Linear Functionals#^def-3-5|linear functional]]. Then $\ell \in X'$ ([[§31 Dual Spaces#^def-31-1|Def. §31.1]]) if and only if $N_\ell$ ([[§31 Dual Spaces#^prop-31-6|§31.6]]) is [[§11 Normed Linear Spaces#^def-11-6|closed]].
>
> *Source: HW5, Problem 5*
>
> *Lax: §6.3, Lemma 5(iii)*

^prop-31-7

> [!proof]+ Proof
> (HW5, Problem 5.) **($\Rightarrow$)** Let $\ell \in X'$, and let $x_n \in N_\ell$ with $x_n \to x$ in $X$. Since $\ell$ is bounded, it is continuous (Proposition [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|§26.2]]), so $\ell(x) = \lim_n \ell(x_n) = 0$, i.e. $x \in N_\ell$.
>
> **($\Leftarrow$)** Assume $N_\ell$ is closed. If $\ell = 0$, then $\ell \in X'$. So assume $\ell \neq 0$, and choose $x_0$ with $\ell(x_0) \neq 0$; replacing $x_0$ by $x_0/\ell(x_0)$, we may assume $\ell(x_0) = 1$. Suppose, for contradiction, that $\ell$ is not bounded. Then for each $n \in \mathbb{N}$ there is $x_n \in X$ with $|\ell(x_n)| > n\,\|x_n\|$; in particular $\ell(x_n) \neq 0$. Let
>
> $$
> y_n = x_0 - \frac{x_n}{\ell(x_n)} .
> $$
>
> Then $\ell(y_n) = 1 - 1 = 0$, so $y_n \in N_\ell$, and $\|y_n - x_0\| = \|x_n\|/|\ell(x_n)| < 1/n \to 0$. So $y_n \to x_0$ with every $y_n \in N_\ell$; since $N_\ell$ is closed, $x_0 \in N_\ell$, contradicting $\ell(x_0) = 1$. Hence $\ell$ is bounded.

^pf-31-7

*Uses:* [[§31 Dual Spaces#^def-31-1|Def. §31.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|§26.2]], [[§11 Normed Linear Spaces#^def-11-6|Def. §11.6]], [[§11 Normed Linear Spaces#^def-11-4|Def. §11.4]], [[§11 Normed Linear Spaces#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - The Hilbert-space (⇒) direction: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-26-3|§26.3]]; “continuous iff bounded”: [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-26-2|§26.2]] for functionals, [[§30 Boundedness and Continuity#^prop-30-2|§30.2]] for maps.
> - The sequence $y_n = x_0 - x_n/\ell(x_n)$ is [[Functional Analysis Problem-Solving Techniques#^ex-t18|Technique 18]].

![[m556-22-1.svg]]
*Points $y_n$ of $N_\ell$ with $\|y_n - x_0\| < \frac1n$, approaching $x_0$, $\ell(x_0) = 1$, off the null space.*

The picture behind ($\Leftarrow$): if $\ell$ were unbounded, points $y_n$ of the null space would approach a point $x_0$ off it, so the null space could not be closed. (The picture is schematic: in finite dimensions every functional is bounded, and an unbounded $\ell$ has a *dense* null space.)

> [!remark] Remark
> Proposition [[§31 Dual Spaces#^prop-31-6|§31.6]] is pure algebra; Proposition [[§31 Dual Spaces#^prop-31-7|§31.7]] is where the norm enters. Together they say that the null space of a nonzero functional is a “hyperplane through $0$” ([[§5 Statement and Motivation#^def-5-3|Def. §5.3]]) that is either closed (bounded $\ell$) or not (unbounded $\ell$). Both proofs use the same move: subtract from $x$ the multiple of $x_0$ that lands it in the null space.

^rem-31-5

Proposition [[§31 Dual Spaces#^prop-31-7|§31.7]] is a statement about functionals. For a linear map into a general normed space, a closed null space is not enough.

> [!example] Example §31.3: A Closed Null Space Does Not Make a Linear Map Bounded
> Let $X, Y$ be normed linear spaces and $T : X \to Y$ linear with null space $N_T = \{x \in X : Tx = 0\}$. If $N_T$ is closed, $T$ need not belong to $\mathcal{L}(X, Y)$: on $X = Y = c_{00}$ with the norm $\|x\| = \sup_n |x_n|$, the linear map $T x = (n x_n)_{n \ge 1}$ has $N_T = \{0\}$, which is closed, and $T$ is not bounded.
>
> *Source: HW6, Problem 1*

^ex-31-3

> [!proof]+ Proof
> (HW6, Problem 1.) **Answer: no.** For $Y = \mathbb{F}$ (a functional) the answer is yes (Lax §6.3, Lemma 5; HW 5, Problem 5; Proposition [[§31 Dual Spaces#^prop-31-7|§31.7]]), but not for general $Y$.
>
> **Counterexample.** Let $X = Y = c_{00}$, the space of real sequences with only finitely many nonzero terms (Example [[§14 New Normed Spaces from Old#^ex-14-3|§14.3]]), with the norm $\|x\| = \sup_n |x_n|$, and define
>
> $$
> T x = (1 \cdot x_1,\ 2 x_2,\ 3 x_3,\ \ldots) = (n x_n)_{n \ge 1}.
> $$
>
> - *$T$ is well defined and linear.* If $x_n = 0$ for $n > M$, then $n x_n = 0$ for $n > M$, so $Tx \in c_{00}$; and $T(\alpha x + \beta y) = (n(\alpha x_n + \beta y_n))_n = \alpha Tx + \beta Ty$.
> - *$N_T$ is closed.* $Tx = 0$ means $n x_n = 0$ for all $n$, i.e. $x = 0$. So $N_T = \{0\}$, and a one-point set is closed in a metric space.
> - *$T$ is unbounded.* $\|e_n\| = 1$ and $T e_n = n e_n$, so $\|T e_n\| = n$. There is no constant $c$ with $\|Tx\| \le c\|x\|$ for all $x$, so $T \notin \mathcal{L}(X, Y)$ (Definition [[§30 Boundedness and Continuity#^def-30-2|§30.2]]).
>
> **A second counterexample, closer to the course.** Let $X = C^1[0,1]$ and $Y = C[0,1]$, both with the maximum norm, and $D f = f'$. Then $N_D$ is the set of constant functions. It is closed: if constants $c_n$ converge uniformly to $f$, then $(c_n)$ is Cauchy in $\mathbb{R}$, so $c_n \to c$, and $f = c$ is constant. But $D$ is unbounded: $f_n(t) = t^n$ has $\|f_n\| = 1$ and $\|D f_n\| = \max_t n t^{n-1} = n$ (Proposition [[§30 Boundedness and Continuity#^prop-30-6|§30.6]]).

^pf-ex-31-3

*Uses:* [[§31 Dual Spaces#^prop-31-7|§31.7]], [[§14 New Normed Spaces from Old#^ex-14-3|Ex. §14.3]], [[§30 Boundedness and Continuity#^def-30-2|Def. §30.2]], [[§30 Boundedness and Continuity#^prop-30-6|§30.6]]

Where the functional proof breaks: for $\ell : X \to \mathbb{F}$ one uses that $N_\ell$ has codimension one, so $X = N_\ell \oplus \operatorname{span}\{x_0\}$ (Proposition [[§31 Dual Spaces#^prop-31-6|§31.6]]). The correct generalization is the following.

> [!theorem] Proposition §31.8: Closed Null Space and Finite-Dimensional Range Imply Bounded
> Let $X, Y$ be normed linear spaces and $T : X \to Y$ linear with null space $N_T = \{x \in X : Tx = 0\}$. If $N_T$ is closed and $T(X)$ is finite-dimensional, then $T$ is bounded.
>
> *Source: HW6, Problem 1*

^prop-31-8

> [!proof]+ Proof
> (HW6, Problem 1, the remark after the solution.) Since $N_T$ is closed, $\|[x]\| = \inf_{y \in N_T} \|x + y\|$ is a norm on $X/N_T$ (Theorem [[§14 New Normed Spaces from Old#^thm-14-9|§14.9]]), and the quotient map $\pi : X \to X/N_T$ satisfies $\|\pi x\| \le \|x\|$. The map $\tilde T : X/N_T \to Y$, $\tilde T[x] = Tx$, is well defined (if $x - x' \in N_T$ then $Tx = Tx'$), linear and injective, so $\dim X/N_T = \dim T(X) < \infty$. A linear map on a finite-dimensional normed space is bounded (Proposition [[§30 Boundedness and Continuity#^prop-30-7|§30.7]]), so $\|Tx\| = \|\tilde T \pi x\| \le \|\tilde T\|\,\|\pi x\| \le \|\tilde T\|\,\|x\|$.

^pf-31-8

*Uses:* [[§14 New Normed Spaces from Old#^thm-14-9|§14.9]], [[§30 Boundedness and Continuity#^prop-30-7|§30.7]]

Both counterexamples of Example [[§31 Dual Spaces#^ex-31-3|§31.3]] have infinite-dimensional range.