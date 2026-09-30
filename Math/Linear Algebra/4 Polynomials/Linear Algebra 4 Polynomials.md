---
type: section
subject: "[[Linear Algebra]]"
chapter: 4
section: "4"
tags: [linear-algebra]
---
← [[Linear Algebra 3F Duality]] · ↑ [[Linear Algebra — 4 Polynomials]] · [[Linear Algebra 5A Invariant Subspaces]] →

> [!definition] 4.1 Real part, Re z, imaginary part, Im z
> For $z=a+bi$ with $a,b\in\R$: the *real part* is $\operatorname{Re}z=a$ and the *imaginary part* is $\operatorname{Im}z=b$. So $z=\operatorname{Re}z+(\operatorname{Im}z)\,i$.

^ladr-4-1

> [!remark]- Connections
> - Used to define [[Linear Algebra 4 Polynomials#^ladr-4-2|Complex conjugate, z, absolute value, ∣z∣]].

> [!definition] 4.2 Complex conjugate, z, absolute value, |z|
> For $z\in\C$:
> - the *complex conjugate* is $\bar z=\operatorname{Re}z-(\operatorname{Im}z)\,i$;
> - the *absolute value* is $|z|=\sqrt{(\operatorname{Re}z)^2+(\operatorname{Im}z)^2}$.

^ladr-4-2

> [!remark]- Connections
> - Properties: [[Linear Algebra 4 Polynomials#^ladr-4-4|Properties of complex numbers]]. The conjugate is why complex inner products are conjugate-symmetric ([[Linear Algebra 6A Inner Products and Norms#^ladr-6-2|Inner product]]) and why adjoints involve conjugate transposes ([[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-7|Conjugate transpose, A∗]]).

> [!example] 4.3 Real and imaginary part, complex conjugate, absolute value (p. 120)
> For $z=3+2i$: $\operatorname{Re}z=3$, $\operatorname{Im}z=2$, $\bar z=3-2i$, $|z|=\sqrt{3^2+2^2}=\sqrt{13}$.
>
> Identifying $z$ with $(\operatorname{Re}z,\operatorname{Im}z)\in\R^2$, $|z|$ is the distance from $0$, and $\bar z$ is the reflection across the real axis. So $\bar z=z$ iff $z$ is real. As a complex vector space $\C$ is $1$-dimensional; as a real vector space it is $\R^2$, $2$-dimensional ([[Linear Algebra 2C Dimension#^ladr-2-36|2.36]]).
>
> ![[ladr-4.3-complex-plane.svg|300]]

^ladr-4-3

> [!theorem] 4.4 Properties of complex numbers
> For $w,z\in\C$:
> - $z+\bar z=2\operatorname{Re}z$ and $z-\bar z=2(\operatorname{Im}z)\,i$;
> - $z\bar z=|z|^2$;
> - $\overline{w+z}=\bar w+\bar z$, $\overline{wz}=\bar w\,\bar z$, $\bar{\bar z}=z$;
> - $|\operatorname{Re}z|\le|z|$ and $|\operatorname{Im}z|\le|z|$;
> - $|\bar z|=|z|$ and $|wz|=|w|\,|z|$;
> - **triangle inequality** $|w+z|\le|w|+|z|$.

^ladr-4-4

> [!remark] Reverse triangle inequality
> $\big||w|-|z|\big|\le|w-z|$ follows by applying the triangle inequality to $w=(w-z)+z$ and to $z=(z-w)+w$.

> [!proof]+
> All but the last are direct computations from [[Linear Algebra 4 Polynomials#^ladr-4-2|Complex conjugate, z, absolute value, ∣z∣]] (e.g. $(a+bi)(a-bi)=a^2+b^2$). *(Filled in: multiplicativity of $|\cdot|$.)* $|wz|^2=wz\,\overline{wz}=(w\bar w)(z\bar z)=|w|^2|z|^2$.
>
> **Triangle inequality.**
> $$
> |w+z|^2=(w+z)(\bar w+\bar z)=|w|^2+|z|^2+w\bar z+\overline{w\bar z}
> =|w|^2+|z|^2+2\operatorname{Re}(w\bar z)\le|w|^2+|z|^2+2|w||z|=(|w|+|z|)^2 ,
> $$
> using $\operatorname{Re}u\le|u|$ and $|w\bar z|=|w||z|$. Take square roots.

*Uses:* [[Linear Algebra 4 Polynomials#^ladr-4-2|4.2]]

> [!remark]- Connections
> - The same proof pattern gives the triangle inequality for norms: [[Triangle inequality]], via [[Cauchy–Schwarz inequality]].

> [!definition] 4.5 Zero of a polynomial
> $\lambda\in\F$ is a *zero* (or *root*) of $p\in\Poly(\F)$ if $p(\lambda)=0$.

^ladr-4-5

> [!remark]- Connections
> - Zeros correspond to linear factors: [[Linear Algebra 4 Polynomials#^ladr-4-6|Each zero of a polynomial corresponds to a degree-one factor]]. How many: [[Linear Algebra 4 Polynomials#^ladr-4-8|Degree m implies at most m zeros]]. Zeros of the minimal polynomial are eigenvalues: [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]].

> [!theorem] 4.6 Each zero of a polynomial corresponds to a degree-one factor
> Let $p\in\Poly(\F)$ have degree $m\ge1$ and $\lambda\in\F$. Then $p(\lambda)=0$ iff there is $q\in\Poly(\F)$ of degree $m-1$ with
> $$
> p(z)=(z-\lambda)q(z)\quad\text{for all }z\in\F .
> $$

^ladr-4-6

> [!proof]+
> ($\Rightarrow$) Write $p(z)=\sum_{k=0}^ma_kz^k$. Since $p(\lambda)=0$,
> $$
> p(z)=p(z)-p(\lambda)=\sum_{k=1}^m a_k(z^k-\lambda^k),\qquad z^k-\lambda^k=(z-\lambda)\sum_{j=1}^{k}\lambda^{j-1}z^{k-j}.
> $$
> So $p(z)=(z-\lambda)q(z)$ where $q$ has degree $m-1$ (its $z^{m-1}$ coefficient is $a_m\neq0$).
>
> ($\Leftarrow$) $p(\lambda)=(\lambda-\lambda)q(\lambda)=0$.

> [!remark]- Connections
> - Gives [[Linear Algebra 4 Polynomials#^ladr-4-8|Degree m implies at most m zeros]], and the step $p(z)=(z-\lambda)q(z)$ in [[Existence of eigenvalues]] and [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]].

> [!theorem] 4.8 Degree m implies at most m zeros
> A polynomial $p\in\Poly(\F)$ of degree $m\ge1$ has at most $m$ zeros in $\F$.

^ladr-4-8

> [!remark] Coefficients are unique
> If a polynomial function had two coefficient lists, their difference would be a nonzero-coefficient polynomial with infinitely many zeros (all of $\F$), contradicting this result. So coefficients and degree are well defined (used in [[Linear Algebra 2A Span and Linear Independence#^ladr-2-10|Polynomial, P(F)]], [[Linear Algebra 2A Span and Linear Independence#^ladr-2-11|Degree of a polynomial, deg p]]), and $1,z,\dots,z^m$ is linearly independent.

> [!proof]+
> Induction on $m$. For $m=1$, $a_0+a_1z$ with $a_1\ne0$ has exactly one zero $-a_0/a_1$. For $m>1$: if $p$ has no zero we are done; otherwise let $p(\lambda)=0$ and write $p=(z-\lambda)q$ with $\deg q=m-1$ ([[Linear Algebra 4 Polynomials#^ladr-4-6|Each zero of a polynomial corresponds to a degree-one factor]]). The zeros of $p$ are $\lambda$ together with the zeros of $q$, of which there are at most $m-1$.

*Uses:* [[Linear Algebra 4 Polynomials#^ladr-4-6|4.6]]

> [!remark]- Connections
> - Alternative bound on the number of eigenvalues: via [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]] and [[Existence, uniqueness, and degree of minimal polynomial]] (compare [[Linear Algebra 5A Invariant Subspaces#^ladr-5-12|Operator cannot have more eigenvalues than dimension of vector space]]).

> [!theorem] 4.9 Division algorithm for polynomials
> Let $p,s\in\Poly(\F)$ with $s\neq0$. Then there are unique $q,r\in\Poly(\F)$ with
> $$
> p=sq+r\quad\text{and}\quad\deg r<\deg s .
> $$

^ladr-4-9

> [!remark] A linear-algebra proof
> No long division: existence and uniqueness both come from a basis of $\Poly_n(\F)$.

> [!proof]+
> Let $n=\deg p$, $m=\deg s$. If $n<m$ take $q=0$, $r=p$. Otherwise consider
> $$
> 1,\ z,\ \dots,\ z^{m-1},\ s,\ zs,\ \dots,\ z^{n-m}s\quad\text{in }\Poly_n(\F).
> $$
> These have distinct degrees $0,1,\dots,n$, so they are linearly independent; there are $n+1=\dim\Poly_n(\F)$ of them, so they form a basis ([[Linear Algebra 2C Dimension#^ladr-2-38|Linearly independent list of the right length is a basis]]). Expand
> $$
> p=\underbrace{a_0+a_1z+\dots+a_{m-1}z^{m-1}}_{r}+s\,\underbrace{(b_0+b_1z+\dots+b_{n-m}z^{n-m})}_{q}.
> $$
> Then $\deg r<m$. *(Filled in.)* Uniqueness: any $q,r$ with $p=sq+r$, $\deg r<m$ expand $p$ in this basis, and coordinates are unique ([[Linear Algebra 2B Bases#^ladr-2-28|Criterion for basis]]).

*Uses:* [[Linear Algebra 2C Dimension#^ladr-2-38|2.38]], [[Linear Algebra 2B Bases#^ladr-2-28|2.28]]

> [!remark]- Connections
> - Key step in [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-29|Q(T) = 0 ⟺ q is a polynomial multiple of the minimal polynomial]]: every annihilating polynomial is a multiple of the minimal polynomial.

> [!theorem] 4.12 Fundamental theorem of algebra, first version
> Every nonconstant polynomial with complex coefficients has a zero in $\C$.

^ladr-4-12

> [!remark] Analysis inside algebra
> The proof needs a genuinely analytic input: a continuous function on a compact set attains its minimum (the extreme value theorem). There is no purely algebraic proof over $\C$.

> [!proof]+
> **$k$-th roots exist.** By De Moivre, $(\cos\theta+i\sin\theta)^k=\cos k\theta+i\sin k\theta$. Writing $w=r(\cos\theta+i\sin\theta)$, the number $r^{1/k}\big(\cos\frac{\theta}{k}+i\sin\frac{\theta}{k}\big)$ is a $k$-th root of $w$.
>
> **A minimum exists.** If $p$ has leading term $c_mz^m$, then $|p(z)|/|z|^m\to|c_m|$, so $|p(z)|\to\infty$ as $|z|\to\infty$. Hence the continuous function $|p|$ attains a global minimum at some $\zeta\in\C$ (minimize over a large closed disk, which is compact).
>
> **The minimum is $0$.** Suppose $p(\zeta)\ne0$ and set $q(z)=p(z+\zeta)/p(\zeta)$, so $|q|$ has global minimum $1$ at $0$. Write $q(z)=1+a_kz^k+\dots+a_mz^m$ with $a_k\ne0$ the first nonzero coefficient after the constant, and choose $\beta$ with $\beta^k=-1/a_k$. There is $c>1$ such that for $t\in(0,1)$
> $$
> |q(t\beta)|\le|1+a_kt^k\beta^k|+t^{k+1}c=1-t^k(1-tc).
> $$
> With $t=1/(2c)$ this is $<1$, a contradiction. So $p(\zeta)=0$.

%% ex:4.12-fig %%
> [!example] The key step of the proof, pictured
> The plane of values of $q$: $q(0)=1$ lies on the unit circle. Going from $0$ to $t\beta$, the term $a_kt^k\beta^k=-t^k$ pulls the value straight toward $0$, to $1-t^k$ (blue), and the higher terms move it by at most $t^{k+1}c$ (red disk). Once $tc<1$ the disk lies inside the unit circle, so $|q(t\beta)|<1$, contradicting the minimum $1$.
>
> ![[ladr-4.12-fta-step.svg|320]]

> [!theorem] 4.13 Fundamental theorem of algebra, second version
> A nonconstant $p\in\Poly(\C)$ has a factorization, unique up to the order of the factors,
> $$
> p(z)=c(z-\lambda_1)\cdots(z-\lambda_m),\qquad c,\lambda_1,\dots,\lambda_m\in\C .
> $$

^ladr-4-13

> [!proof]+
> Induction on $m=\deg p$; $m=1$ is clear.
>
> **Existence.** By [[Fundamental theorem of algebra, first version]], $p(\lambda)=0$ for some $\lambda$; by [[Linear Algebra 4 Polynomials#^ladr-4-6|Each zero of a polynomial corresponds to a degree-one factor]], $p=(z-\lambda)q$ with $\deg q=m-1$, and $q$ factors by induction.
>
> **Uniqueness.** $c$ is the leading coefficient. If $(z-\lambda_1)\cdots(z-\lambda_m)=(z-\tau_1)\cdots(z-\tau_m)$, setting $z=\lambda_1$ shows some $\tau_j=\lambda_1$; relabel so $\tau_1=\lambda_1$. For $z\ne\lambda_1$ divide by $z-\lambda_1$:
> $$
> (z-\lambda_2)\cdots(z-\lambda_m)=(z-\tau_2)\cdots(z-\tau_m).
> $$
> *(Filled in.)* Both sides are polynomials agreeing at infinitely many points, so they are equal everywhere ([[Linear Algebra 4 Polynomials#^ladr-4-8|Degree m implies at most m zeros]] applied to their difference). By induction the $\tau$'s are the $\lambda$'s up to order.

*Uses:* [[Fundamental theorem of algebra, first version|4.12]], [[Linear Algebra 4 Polynomials#^ladr-4-6|4.6]], [[Linear Algebra 4 Polynomials#^ladr-4-8|4.8]]

> [!remark]- Connections
> - Complex minimal polynomials split: [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-27|Eigenvalues are the zeros of the minimal polynomial]](b). Real version: [[Linear Algebra 4 Polynomials#^ladr-4-16|Factorization of a polynomial over R]].

> [!theorem] 4.14 Polynomials with real coefficients have nonreal zeros in pairs
> If $p\in\Poly(\C)$ has real coefficients and $\lambda\in\C$ is a zero of $p$, then so is $\bar\lambda$.

^ladr-4-14

> [!proof]+
> From $a_0+a_1\lambda+\dots+a_m\lambda^m=0$ with all $a_k\in\R$, conjugate both sides using [[Linear Algebra 4 Polynomials#^ladr-4-4|Properties of complex numbers]]: $a_0+a_1\bar\lambda+\dots+a_m\bar\lambda^m=0$.

*Uses:* [[Linear Algebra 4 Polynomials#^ladr-4-4|4.4]]

> [!remark]- Connections
> - Pairs $(z-\lambda)(z-\bar\lambda)=z^2-2(\operatorname{Re}\lambda)z+|\lambda|^2$: the real quadratic factors of [[Linear Algebra 4 Polynomials#^ladr-4-16|Factorization of a polynomial over R]].
> - Physics: for real (e.g. time-reversal symmetric) problems, complex eigenvalues come in conjugate pairs.

> [!theorem] 4.15 Factorization of a quadratic polynomial
> For $b,c\in\R$: $x^2+bx+c=(x-\lambda_1)(x-\lambda_2)$ with $\lambda_1,\lambda_2\in\R$ if and only if $b^2\ge4c$.

^ladr-4-15

> [!proof]+
> Complete the square: $x^2+bx+c=\big(x+\tfrac b2\big)^2+\big(c-\tfrac{b^2}{4}\big)$.
>
> If $b^2<4c$, the right side is positive for every real $x$, so there is no real zero and no such factorization.
>
> If $b^2\ge4c$, pick $d\in\R$ with $d^2=\tfrac{b^2}{4}-c$; then $x^2+bx+c=\big(x+\tfrac b2+d\big)\big(x+\tfrac b2-d\big)$.

> [!remark]- Connections
> - The irreducible quadratics ($b^2<4c$) appear in [[Linear Algebra 4 Polynomials#^ladr-4-16|Factorization of a polynomial over R]], [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-33|Even-dimensional null space]], [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-34|Operators on odd-dimensional vector spaces have eigenvalues]].

%% ex:4.15-fig %%
> [!example] Completing the square, pictured
> $x^2+bx+c$ is lowest at $x=-\tfrac b2$, where it equals $c-\tfrac{b^2}4$. Red: $x^2+2x+2$ ($b^2=4<8=4c$) has lowest value $1>0$ and no real zero. Blue: $x^2+2x-1$ ($b^2=4\ge-4=4c$) has lowest value $-2<0$ and zeros $-1\pm d$ with $d^2=\tfrac{b^2}4-c=2$.
>
> ![[ladr-4.15-quadratic.svg|340]]

> [!theorem] 4.16 Factorization of a polynomial over R
> A nonconstant $p\in\Poly(\R)$ has a factorization, unique up to order,
> $$
> p(x)=c(x-\lambda_1)\cdots(x-\lambda_m)(x^2+b_1x+c_1)\cdots(x^2+b_Mx+c_M)
> $$
> with all constants real and $b_k^2<4c_k$ for each $k$.

^ladr-4-16

> [!proof]+
> **Existence.** View $p$ in $\Poly(\C)$. If all its zeros are real, use [[Linear Algebra 4 Polynomials#^ladr-4-13|Fundamental theorem of algebra, second version]]. Otherwise let $\lambda\notin\R$ be a zero; by [[Linear Algebra 4 Polynomials#^ladr-4-14|Polynomials with real coefficients have nonreal zeros in pairs]] so is $\bar\lambda$, and
> $$
> p(x)=(x-\lambda)(x-\bar\lambda)q(x)=\big(x^2-2(\operatorname{Re}\lambda)x+|\lambda|^2\big)q(x)
> $$
> with $\deg q=\deg p-2$. For real $x$, $q(x)=p(x)/(x^2-2(\operatorname{Re}\lambda)x+|\lambda|^2)$ is real (the denominator is positive), so the polynomial $\operatorname{Im}q$ vanishes on all of $\R$ and hence has zero coefficients ([[Linear Algebra 4 Polynomials#^ladr-4-8|Degree m implies at most m zeros]]). Thus $q\in\Poly(\R)$, and induction on the degree finishes. The quadratic factor has $b^2<4c$ because it has no real zero ([[Linear Algebra 4 Polynomials#^ladr-4-15|Factorization of a quadratic polynomial]]).
>
> **Uniqueness.** *(Filled in.)* Each irreducible real quadratic factor splits over $\C$ as $(x-\mu)(x-\bar\mu)$ with $\mu\notin\R$, so any real factorization yields a complex one. By uniqueness in [[Linear Algebra 4 Polynomials#^ladr-4-13|Fundamental theorem of algebra, second version]], the multiset of complex zeros is determined; its real elements give the linear factors and its conjugate pairs of nonreal elements give the quadratic factors.

*Uses:* [[Linear Algebra 4 Polynomials#^ladr-4-13|4.13]], [[Linear Algebra 4 Polynomials#^ladr-4-14|4.14]], [[Linear Algebra 4 Polynomials#^ladr-4-8|4.8]], [[Linear Algebra 4 Polynomials#^ladr-4-15|4.15]]

> [!remark]- Connections
> - Used in [[Linear Algebra 5B The Minimal Polynomial#^ladr-5-34|Operators on odd-dimensional vector spaces have eigenvalues]] to find an irreducible quadratic factor of a real minimal polynomial.
