---
type: section
subject: "[[Linear Algebra]]"
chapter: 6
section: 21
aliases: ["LADR 6B", "6B Orthonormal Bases"]
tags: [linear-algebra]
---
← [[§20 Inner Products and Norms]] · ↑ [[· 6 Inner Product Spaces]] · [[§22 Orthogonal Complements and Minimization Problems]] →

> [!definition] Definition 6.22: Orthonormal
> A list $e_1,\dots,e_m$ in $V$ is *orthonormal* if
> $$
> \langle e_j,e_k\rangle=\begin{cases}1&j=k,\\0&j\ne k,\end{cases}
> $$
> i.e. each vector has norm $1$ and distinct vectors are orthogonal.

^ladr-6-22

> [!remark]- Connections
> - Physics: $\langle e_j|e_k\rangle=\delta_{jk}$.
> - Same definition for possibly infinite sets: [[§24 Orthonormal Sets and Bases#^def-24-1|556 Def. §24.1]].
> - Computational version: [[§51 Orthogonal Sets#^def-51-4|235 Def. §51.4]] (orthonormal sets in $\mathbb R^n$).

> [!example] Example 6.23: Orthonormal lists (p. 197)
> - (a) The standard basis of $\F^n$.
> - (b) $\big(\tfrac1{\sqrt3},\tfrac1{\sqrt3},\tfrac1{\sqrt3}\big),\ \big(-\tfrac1{\sqrt2},\tfrac1{\sqrt2},0\big)$ in $\F^3$.
> - (c) The list in (b) together with $\big(\tfrac1{\sqrt6},\tfrac1{\sqrt6},-\tfrac2{\sqrt6}\big)$: an orthonormal basis of $\F^3$ ([[§21 Orthonormal Bases#^ladr-6-28|6.28]]).
> - (d) $\tfrac1{\sqrt{2\pi}},\ \tfrac{\cos x}{\sqrt\pi},\dots,\tfrac{\cos nx}{\sqrt\pi},\ \tfrac{\sin x}{\sqrt\pi},\dots,\tfrac{\sin nx}{\sqrt\pi}$ in $C[-\pi,\pi]$ with $\langle f,g\rangle=\int_{-\pi}^{\pi}fg$: the Fourier basis (orthogonality is $\int_{-\pi}^\pi\cos jx\cos kx\,dx=0$ for $j\ne k$, etc.).
> - (e) In $\Poly_2(\R)$ with $\int_{-1}^1pq$: normalizing $1,x,x^2$ gives $\tfrac1{\sqrt2},\sqrt{\tfrac32}x,\sqrt{\tfrac52}x^2$, but $\langle1,x^2\rangle=\tfrac23\ne0$, so this is **not** orthonormal. Fixed in [[§21 Orthonormal Bases#^ladr-6-34|6.34]].

^ladr-6-23

> [!remark]- Connections
> - In L² the Fourier list of (d), continued indefinitely, is an orthonormal basis: [[§24 Orthonormal Sets and Bases#^thm-24-11|556 Thm. §24.11]] (stated there with complex exponentials on [0, 2π]).
> - Computational version: [[§57 Applications of Inner Product Spaces#^prop-57-2|235 Prop. §57.2]] (orthogonality of the trigonometric system, as in (d), with $\langle1,1\rangle=2\pi$ and $\langle\cos kt,\cos kt\rangle=\pi$).
> - Computational version: the orthogonality relations of the trigonometric system on $[-\pi,\pi]$, [[§9 Periodic Functions and Fourier Series#^prop-9-3|341 Prop. §9.3]], which give the Fourier coefficient formulas, [[§9 Periodic Functions and Fourier Series#^prop-9-4|341 Prop. §9.4]].

> [!theorem] Theorem 6.24: Norm of an orthonormal linear combination
> If $e_1,\dots,e_m$ is orthonormal, then for all $a_1,\dots,a_m\in\F$,
> $$
> \|a_1e_1+\dots+a_me_m\|^2=|a_1|^2+\dots+|a_m|^2 .
> $$

^ladr-6-24

> [!proof]+ Proof
> The vectors $a_ke_k$ are pairwise orthogonal with $\|a_ke_k\|=|a_k|$ ([[§20 Inner Products and Norms#^ladr-6-9|6.9]]); apply [[§20 Inner Products and Norms#^ladr-6-12|6.12]] repeatedly (induction on $m$).

*Uses:* [[§20 Inner Products and Norms#^ladr-6-9|6.9]], [[§20 Inner Products and Norms#^ladr-6-12|6.12]]

> [!remark]- Connections
> - Gives [[§21 Orthonormal Bases#^ladr-6-25|6.25]] and [[§21 Orthonormal Bases#^ladr-6-30|6.30]](b).

> [!theorem] Theorem 6.25: Orthonormal lists are linearly independent
> Every orthonormal list is linearly independent.

^ladr-6-25

> [!proof]+ Proof
> If $\sum a_ke_k=0$ then $\sum|a_k|^2=0$ by [[§21 Orthonormal Bases#^ladr-6-24|6.24]], so every $a_k=0$.

*Uses:* [[§21 Orthonormal Bases#^ladr-6-24|6.24]]

> [!remark]- Connections
> - Hence [[§21 Orthonormal Bases#^ladr-6-28|6.28]].
> - Computational version: [[§51 Orthogonal Sets#^thm-51-1|235 Thm. §51.1]] (an orthogonal set of nonzero vectors in $\mathbb R^n$ is linearly independent).

> [!theorem] Theorem 6.26: Bessel’s inequality
> If $e_1,\dots,e_m$ is orthonormal and $v\in V$, then
> $$
> |\langle v,e_1\rangle|^2+\dots+|\langle v,e_m\rangle|^2\le\|v\|^2 .
> $$

^ladr-6-26

> [!proof]+ Proof
> Write $v=u+w$ with $u=\sum_k\langle v,e_k\rangle e_k$ and $w=v-u$. Then $\langle w,e_k\rangle=\langle v,e_k\rangle-\langle v,e_k\rangle=0$ for each $k$, so $w\perp u$. By [[§20 Inner Products and Norms#^ladr-6-12|6.12]] and [[§21 Orthonormal Bases#^ladr-6-24|6.24]], $\|v\|^2=\|u\|^2+\|w\|^2\ge\|u\|^2=\sum_k|\langle v,e_k\rangle|^2$.

*Uses:* [[§20 Inner Products and Norms#^ladr-6-12|6.12]], [[§21 Orthonormal Bases#^ladr-6-24|6.24]]

> [!remark] Remark: Meaning
> $\sum_k\langle v,e_k\rangle e_k$ is the orthogonal projection of $v$ onto $\Span(e_1,\dots,e_m)$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](i)); the inequality says projection shortens. Equality for all $v$ iff the list is a basis ([[§21 Orthonormal Bases#^ladr-6-30|6.30]](b)).

> [!remark]- Connections
> - Physics: the probabilities $|\langle e_k|\psi\rangle|^2$ over any orthonormal set of outcomes sum to at most $\|\psi\|^2=1$.
> - Same inequality in 556 ([[§24 Orthonormal Sets and Bases#^lem-24-2|556 Lemma §24.2]]), extended to arbitrary orthonormal families in [[§24 Orthonormal Sets and Bases#^thm-24-5|556 Thm. §24.5]].
> - Computational version: [[§15★ Mean Error and Convergence in Mean#^thm-15-3|341 Thm. §15.3]] (for the trigonometric system on $[-a,a]$, in the limit $N\to\infty$ too).

> [!definition] Definition 6.27: Orthonormal basis
> An *orthonormal basis* of $V$ is an orthonormal list that is also a basis of $V$. Example: the standard basis of $\F^n$.

^ladr-6-27

> [!remark]- Connections
> - In a Hilbert space ([[§21 Cauchy–Schwarz and the Induced Norm#^def-21-1|556 Def. §21.1]]) an orthonormal basis is defined by the series expansion of every vector ([[§24 Orthonormal Sets and Bases#^def-24-4|556 Def. §24.4]]); in infinite dimensions it is never a basis in the sense of this definition, since some vectors need infinitely many terms.
> - Computational version: [[§51 Orthogonal Sets#^def-51-4|235 Def. §51.4]] (orthonormal basis of a subspace of $\mathbb R^n$).

> [!theorem] Theorem 6.28: Orthonormal lists of the right length are orthonormal bases
> If $V$ is finite-dimensional, every orthonormal list of length $\dim V$ is an orthonormal basis.

^ladr-6-28

> [!proof]+ Proof
> Orthonormal lists are independent ([[§21 Orthonormal Bases#^ladr-6-25|6.25]]), and independent lists of length $\dim V$ are bases ([[§6 Dimension#^ladr-2-38|2.38]]).

*Uses:* [[§21 Orthonormal Bases#^ladr-6-25|6.25]], [[§6 Dimension#^ladr-2-38|2.38]]

> [!example] Example 6.29: An orthonormal basis of F⁴ (p. 199)
> $\big(\tfrac12,\tfrac12,\tfrac12,\tfrac12\big),\ \big(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12\big),\ \big(\tfrac12,-\tfrac12,-\tfrac12,\tfrac12\big),\ \big(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12\big)$ is an orthonormal basis of $\F^4$. Each has norm $\sqrt{4\cdot\frac14}=1$; each pair has two $+\frac14$ and two $-\frac14$ products, so inner product $0$; four orthonormal vectors in $\F^4$ form a basis ([[§21 Orthonormal Bases#^ladr-6-28|6.28]]).

^ladr-6-29

> [!theorem] Theorem 6.30: Writing a vector as a linear combination of an orthonormal basis
> Let $e_1,\dots,e_n$ be an orthonormal basis of $V$ and $u,v\in V$. Then
> - (a) $v=\langle v,e_1\rangle e_1+\dots+\langle v,e_n\rangle e_n$;
> - (b) $\|v\|^2=|\langle v,e_1\rangle|^2+\dots+|\langle v,e_n\rangle|^2$ (Parseval);
> - (c) $\langle u,v\rangle=\langle u,e_1\rangle\overline{\langle v,e_1\rangle}+\dots+\langle u,e_n\rangle\overline{\langle v,e_n\rangle}$.

^ladr-6-30

> [!proof]+ Proof
> Write $v=\sum a_ke_k$. Taking the inner product with $e_j$ gives $\langle v,e_j\rangle=a_j$: this is (a). (b) follows from (a) and [[§21 Orthonormal Bases#^ladr-6-24|6.24]]. For (c), take the inner product of $u$ with both sides of (a) and use [[§20 Inner Products and Norms#^ladr-6-6|6.6]](d),(e).

*Uses:* [[§21 Orthonormal Bases#^ladr-6-24|6.24]], [[§20 Inner Products and Norms#^ladr-6-6|6.6]]

> [!remark] Remark: Coordinates are inner products
> An orthonormal basis turns $V$ into $\F^n$ isometrically: $v\mapsto(\langle v,e_1\rangle,\dots,\langle v,e_n\rangle)$ preserves inner products by (c). No linear system has to be solved to find coordinates ([[§21 Orthonormal Bases#^ladr-6-31|6.31]]).

> [!remark]- Connections
> - Physics: (a) is the completeness relation $\sum_k|e_k\rangle\langle e_k|=I$; (c) in Dirac order reads $\langle u|v\rangle=\sum_k\langle u|e_k\rangle\langle e_k|v\rangle$ (conjugate on the other factor, per the convention remark in [[§20 Inner Products and Norms#^ladr-6-2|6.2]]).
> - Hilbert-space version: [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]], where the expansion and Parseval characterize orthonormal bases; (a) as an operator identity is the completeness relation, [[§31 The Completeness Relation#^thm-31-2|556 Thm. §31.2]].
> - Computational version: [[§51 Orthogonal Sets#^thm-51-2|235 Thm. §51.2]] (the weights $c_j=\mathbf y\cdot\mathbf u_j/\mathbf u_j\cdot\mathbf u_j$ in an orthogonal basis, as in (a)).

> [!example] Example 6.31: Finding coefficients for a linear combination (p. 200)
> Write $(1,2,4,7)$ in the basis of [[§21 Orthonormal Bases#^ladr-6-29|6.29]]. By [[§21 Orthonormal Bases#^ladr-6-30|6.30]](a) the coefficients are just inner products:
> $$
> (1,2,4,7)=7\big(\tfrac12,\tfrac12,\tfrac12,\tfrac12\big)-4\big(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12\big)+\big(\tfrac12,-\tfrac12,-\tfrac12,\tfrac12\big)+2\big(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12\big).
> $$
> (E.g. $\langle(1,2,4,7),(\frac12,\frac12,\frac12,\frac12)\rangle=\frac{14}2=7$.) Four inner products instead of a $4\times4$ linear system. Check Parseval: $49+16+1+4=70=1+4+16+49$.

^ladr-6-31

> [!theorem] Theorem 6.32: Gram–Schmidt procedure
> Let $v_1,\dots,v_m$ be linearly independent in $V$. Set $f_1=v_1$ and, for $k=2,\dots,m$,
> $$
> f_k=v_k-\frac{\langle v_k,f_1\rangle}{\|f_1\|^2}f_1-\dots-\frac{\langle v_k,f_{k-1}\rangle}{\|f_{k-1}\|^2}f_{k-1},\qquad e_k=\frac{f_k}{\|f_k\|}.
> $$
> Then $e_1,\dots,e_m$ is orthonormal and $\Span(v_1,\dots,v_k)=\Span(e_1,\dots,e_k)$ for each $k$.

^ladr-6-32

> [!proof]+ Proof
> Induction on $k$. For $k=1$, $e_1$ is a unit multiple of $v_1$. Suppose $e_1,\dots,e_{k-1}$ are orthonormal with $\Span(v_1,\dots,v_{k-1})=\Span(e_1,\dots,e_{k-1})=\Span(f_1,\dots,f_{k-1})$.
>
> **$f_k\ne0$:** otherwise $v_k\in\Span(f_1,\dots,f_{k-1})=\Span(v_1,\dots,v_{k-1})$, contradicting independence. So $e_k$ is defined and has norm $1$.
>
> **Orthogonality:** for $j<k$, using $\langle f_i,f_j\rangle=0$ for $i\ne j$,
> $$
> \langle f_k,f_j\rangle=\langle v_k,f_j\rangle-\frac{\langle v_k,f_j\rangle}{\|f_j\|^2}\langle f_j,f_j\rangle=0 .
> $$
> **Spans:** $v_k\in\Span(e_1,\dots,e_k)$ from the definition, so $\Span(v_1,\dots,v_k)\subseteq\Span(e_1,\dots,e_k)$; both have dimension $k$ (independent lists, [[§21 Orthonormal Bases#^ladr-6-25|6.25]]), so they are equal ([[§6 Dimension#^ladr-2-39|2.39]]).

*Uses:* [[§21 Orthonormal Bases#^ladr-6-25|6.25]], [[§6 Dimension#^ladr-2-39|2.39]]

> [!remark] Remark: What each step does
> $f_k$ is $v_k$ minus its orthogonal projection onto $\Span(e_1,\dots,e_{k-1})$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](i)): subtract the shadow, keep the perpendicular part, normalize.

> [!remark]- Connections
> - Computational version: [[§53 The Gram–Schmidt Process#^thm-53-1|235 Thm. §53.1]] (Gram–Schmidt in $\mathbb R^n$, worked in [[§53 The Gram–Schmidt Process#^ex-53-2|235 Ex. §53.2]]); in an inner product space, [[§56 Inner Product Spaces#^thm-56-2|235 Thm. §56.2]].

%% ex:6.32-fig %%
> [!example] Example: One Gram–Schmidt step, pictured
> $f_2=v_2-\langle v_2,e_1\rangle e_1$: remove from $v_2$ its shadow on $e_1$; what remains is perpendicular to $e_1$, and normalizing gives $e_2$.
>
> ![[ladr-6.32-gram-schmidt.svg|340]]

> [!example] Example 6.34: An orthonormal basis of P2(R) (p. 202)
> Gram–Schmidt on $1,x,x^2$ in $\Poly_2(\R)$ with $\langle p,q\rangle=\int_{-1}^1pq$:
> - $f_1=1$, $\|f_1\|^2=2$.
> - $f_2=x-\frac{\langle x,1\rangle}{2}1=x$ (since $\int_{-1}^1t\,dt=0$), $\|f_2\|^2=\frac23$.
> - $f_3=x^2-\frac{\langle x^2,1\rangle}{2}1-\frac{\langle x^2,x\rangle}{2/3}x=x^2-\frac13$, $\|f_3\|^2=\int_{-1}^1\big(t^2-\tfrac13\big)^2dt=\frac8{45}$.
>
> Normalizing gives the orthonormal basis
> $$
> \sqrt{\tfrac12},\qquad \sqrt{\tfrac32}\,x,\qquad \sqrt{\tfrac{45}8}\Big(x^2-\tfrac13\Big)
> $$
> (checked by computer). Up to scaling these are the Legendre polynomials $P_0=1$, $P_1=x$, $P_2=\tfrac12(3x^2-1)$.

^ladr-6-34

> [!remark]- Connections
> - Computational version: [[§56 Inner Product Spaces#^ex-56-5|235 Ex. §56.5]] (Gram–Schmidt on $1,2t-1,12t^2$ in $C[0,1]$: the Legendre polynomials moved to $[0,1]$).
> - Continued in Fourier Series and PDEs: the Legendre polynomials $P_n$ in general, [[§60★ Spherical Coordinates; Legendre Polynomials#^def-60-3|341 Def. §60.3]], orthogonal on $[-1,1]$, [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-5|341 Prop. §60.5]], with norm $2/(2n+1)$, [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-8|341 Prop. §60.8]].

> [!theorem] Theorem 6.35: Existence of orthonormal basis
> Every finite-dimensional inner product space has an orthonormal basis.

^ladr-6-35

> [!proof]+ Proof
> Apply [[Gram–Schmidt procedure|6.32]] to any basis; the result is an orthonormal list of length $\dim V$, hence a basis ([[§21 Orthonormal Bases#^ladr-6-28|6.28]]).

*Uses:* [[Gram–Schmidt procedure|6.32]], [[§21 Orthonormal Bases#^ladr-6-28|6.28]]

> [!remark]- Connections
> - Every Hilbert space has an orthonormal basis ([[§24 Orthonormal Sets and Bases#^thm-24-12|556 Thm. §24.12]], by Zorn's lemma, [[Zorn's Lemma|556 Thm. §5.2]]), and a countable one exactly when it is separable ([[§24 Orthonormal Sets and Bases#^thm-24-13|556 Thm. §24.13]]).
> - Computational version: [[§53 The Gram–Schmidt Process#^cor-53-2|235 Cor. §53.2]] (every nonzero subspace of $\mathbb R^n$ has an orthonormal basis).

> [!theorem] Theorem 6.36: Every orthonormal list extends to an orthonormal basis
> If $V$ is finite-dimensional, every orthonormal list in $V$ extends to an orthonormal basis of $V$.

^ladr-6-36

> [!proof]+ Proof
> The list $e_1,\dots,e_m$ is independent ([[§21 Orthonormal Bases#^ladr-6-25|6.25]]); extend it to a basis $e_1,\dots,e_m,v_1,\dots,v_n$ ([[Every linearly independent list extends to a basis|2.32]]). Gram–Schmidt ([[Gram–Schmidt procedure|6.32]]) leaves $e_1,\dots,e_m$ unchanged (each $f_k=e_k$ since the subtracted inner products vanish, and $\|e_k\|=1$) and produces an orthonormal list $e_1,\dots,e_m,e_{m+1},\dots,e_{m+n}$ of length $\dim V$, a basis by [[§21 Orthonormal Bases#^ladr-6-28|6.28]].

*Uses:* [[§21 Orthonormal Bases#^ladr-6-25|6.25]], [[Every linearly independent list extends to a basis|2.32]], [[Gram–Schmidt procedure|6.32]], [[§21 Orthonormal Bases#^ladr-6-28|6.28]]

> [!theorem] Theorem 6.37: Upper-triangular matrix with respect to some orthonormal basis
> Let $V$ be finite-dimensional and $T\in\Lin(V)$. Then $T$ has an upper-triangular matrix with respect to some **orthonormal** basis iff the minimal polynomial of $T$ equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some $\lambda_k\in\F$.

^ladr-6-37

> [!proof]+ Proof
> If $T$ is upper triangular in a basis $v_1,\dots,v_n$, each $\Span(v_1,\dots,v_k)$ is invariant ([[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]]). Gram–Schmidt gives an orthonormal basis with $\Span(e_1,\dots,e_k)=\Span(v_1,\dots,v_k)$ ([[Gram–Schmidt procedure|6.32]]), so these spans are invariant and $T$ is upper triangular in $e_1,\dots,e_n$ ([[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]]). Now [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]] gives the equivalence.

*Uses:* [[§16 Upper-Triangular Matrices#^ladr-5-39|5.39]], [[Gram–Schmidt procedure|6.32]], [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]]

> [!remark]- Connections
> - Same condition as [[§16 Upper-Triangular Matrices#^ladr-5-44|5.44]]: orthonormality costs nothing here.

> [!theorem] Theorem 6.38: Schur’s theorem
> Every operator on a finite-dimensional complex inner product space has an upper-triangular matrix with respect to some orthonormal basis.

^ladr-6-38

> [!proof]+ Proof
> The minimal polynomial splits over $\C$ ([[§13 Polynomials#^ladr-4-13|4.13]]); apply [[§21 Orthonormal Bases#^ladr-6-37|6.37]].

*Uses:* [[§13 Polynomials#^ladr-4-13|4.13]], [[§21 Orthonormal Bases#^ladr-6-37|6.37]]

> [!remark]- Connections
> - Matrix form: every complex square matrix is unitarily similar to an upper-triangular one. Normal operators get a diagonal matrix: [[Complex spectral theorem|7.31]].

> [!definition] Definition 6.39: Linear functional
> A *linear functional* on $V$ is a linear map $V\to\F$.

^ladr-6-39

> [!remark]- Connections
> - On an inner product space every functional is $\langle\cdot,v\rangle$: [[Riesz representation theorem|6.42]].

> [!definition] Definition 6.39b: Dual space, V′
> The *dual space* is $V'=\Lin(V,\F)$ (as in [[§12 Duality#^ladr-3-110|3.110]]).

^ladr-6-39b

> [!example] Example 6.40: Linear functional on F³ (p. 204)
> $\varphi(z_1,z_2,z_3)=2z_1-5z_2+z_3$ on $\F^3$ equals $\langle z,w\rangle$ with $w=(2,-5,1)$: the Riesz vector ([[Riesz representation theorem|6.42]]) can be read off (over $\C$ it is the conjugate of the coefficient list, here real).

^ladr-6-40

> [!example] Example 6.41: Linear functional on P5(R) (p. 204)
> $\varphi(p)=\int_{-1}^1p(t)\cos(\pi t)\,dt$ is a linear functional on $\Poly_5(\R)$. With $\langle p,q\rangle=\int_{-1}^1pq$ one cannot take $q=\cos(\pi t)$, since it is not a polynomial; yet [[Riesz representation theorem|6.42]] promises some $q\in\Poly_5(\R)$ with $\varphi(p)=\langle p,q\rangle$ for all $p$. See [[§21 Orthonormal Bases#^ladr-6-44|6.44]].

^ladr-6-41

> [!theorem] Theorem 6.42: Riesz representation theorem
> Let $V$ be finite-dimensional and $\varphi$ a linear functional on $V$. There is a unique $v\in V$ with
> $$
> \varphi(u)=\langle u,v\rangle\quad\text{for every }u\in V .
> $$

^ladr-6-42

> [!proof]+ Proof
> **Existence.** Take an orthonormal basis $e_1,\dots,e_n$ ([[§21 Orthonormal Bases#^ladr-6-35|6.35]]). By [[§21 Orthonormal Bases#^ladr-6-30|6.30]](a),
> $$
> \varphi(u)=\varphi\Big(\sum_k\langle u,e_k\rangle e_k\Big)=\sum_k\langle u,e_k\rangle\varphi(e_k)=\Big\langle u,\ \sum_k\overline{\varphi(e_k)}\,e_k\Big\rangle ,
> $$
> so $v=\overline{\varphi(e_1)}e_1+\dots+\overline{\varphi(e_n)}e_n$ works.
>
> **Uniqueness.** If $\langle u,v_1\rangle=\langle u,v_2\rangle$ for all $u$, take $u=v_1-v_2$: $\|v_1-v_2\|^2=0$.

*Uses:* [[§21 Orthonormal Bases#^ladr-6-35|6.35]], [[§21 Orthonormal Bases#^ladr-6-30|6.30]]

> [!remark] Remark: Basis independence
> The formula for $v$ seems to depend on the orthonormal basis, but uniqueness shows it does not.

> [!remark]- Connections
> - In several variables the gradient is the Riesz representer of the derivative, $Df_{\mathbf p}(\mathbf u)=\nabla f(\mathbf p)\cdot\mathbf u$: [[Directional Derivative Formula|452 Thm. §9.1]].
> - Same theorem for Hilbert spaces: [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-23-2|556 Thm. §23.2]] (there $V$ may be infinite-dimensional and the functional must be bounded).

> [!example] Example 6.44: Computation illustrating Riesz representation theorem (p. 206)
> Find $q\in\Poly_2(\R)$ with $\int_{-1}^1p(t)\cos(\pi t)\,dt=\int_{-1}^1pq$ for all $p\in\Poly_2(\R)$. Use the orthonormal basis $e_1,e_2,e_3$ of [[§21 Orthonormal Bases#^ladr-6-34|6.34]] and the formula $q=\sum_k\varphi(e_k)e_k$ from the proof of [[Riesz representation theorem|6.42]]:
> $$
> q(x)=\sum_{k=1}^3\Big(\int_{-1}^1e_k(t)\cos(\pi t)\,dt\Big)e_k(x)=\frac{15}{2\pi^2}\big(1-3x^2\big)
> $$
> (verified symbolically). For $\Poly_5(\R)$ the same procedure gives
> $$
> q(x)=\frac{105}{8\pi^4}\Big((27-2\pi^2)+(24\pi^2-270)x^2+(315-30\pi^2)x^4\Big).
> $$
> In words: $q$ is the orthogonal projection of $\cos(\pi t)$ onto the polynomial subspace ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-57|6.57]](i)). The polynomial that represents $\varphi$ is the best polynomial approximation of the function inside the integral.

^ladr-6-44

%% ex:6.44-fig %%
> [!example] Example: The representing polynomials, pictured
> $\cos(\pi x)$ (black) with its orthogonal projections onto $\Poly_2(\R)$ (blue dashed, $\frac{15}{2\pi^2}(1-3x^2)$) and onto $\Poly_5(\R)$ (red, the degree-$4$ formula above). The larger subspace gives the better approximation in the sense of [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|6.61]].
>
> ![[ladr-6.44-riesz-cos.svg|400]]
