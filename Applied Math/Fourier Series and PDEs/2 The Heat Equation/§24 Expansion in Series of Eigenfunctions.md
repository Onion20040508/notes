---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 24
powers: "2.8"
aliases: ["Powers 2.8"]
tags: [fourier-series-and-pdes, math341]
---
← [[§23 Sturm–Liouville Problems]] · ↑ [[· 2 The Heat Equation]] · [[§25 Generalities on the Heat Conduction Problem]] →

*Powers, Section 2.8 · MAT 341 lectures 10.10, 10.17 · HW 7, HW 8.*

Orthogonality of the eigenfunctions of a regular Sturm–Liouville problem ([[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]]) arose precisely because initial conditions have to be expanded in eigenfunctions. This short section draws the consequences: the coefficients of an eigenfunction expansion are computed exactly like Fourier coefficients, except that the weight $p(x)$ appears and the normalizing integrals $\int p\phi_n^2$ are no longer all equal; and a convergence theorem, the exact analogue of the Fourier series theorem, guarantees that every sectionally smooth function has such an expansion. The course called the eigenfunctions a *generalized Fourier basis*. Fourier sine and cosine series are the special case $s = p = 1$, $q = 0$.

## Coefficients

Consider a regular Sturm–Liouville problem ([[§23 Sturm–Liouville Problems#^def-23-1|Definition §23.1]])

$$
\begin{aligned}
(s\phi')' - q\phi + \lambda^2p\phi &= 0, && l < x < r, && (1) \\
\alpha_1\phi(l) - \alpha_2\phi'(l) &= 0, && && (2) \\
\beta_1\phi(r) + \beta_2\phi'(r) &= 0, && && (3)
\end{aligned}
$$

with eigenfunctions $\phi_1, \phi_2, \ldots$, orthogonal with weight $p$:

$$
\int_l^r p(x)\phi_n(x)\phi_m(x)\,dx = 0, \qquad n \ne m . \qquad (4)
$$

Given a function $f(x)$ on $l < x < r$, we wish to express it in terms of the eigenfunctions,

$$
f(x) = \sum_{n=1}^\infty c_n\phi_n(x), \qquad l < x < r . \qquad (5)
$$

> [!theorem] Proposition §24.1: The Coefficients of an Eigenfunction Expansion
> If $f(x) = \sum_{n=1}^\infty c_n\phi_n(x)$ on $l < x < r$, and the series may be integrated term by term after multiplication by $\phi_m(x)p(x)$ (for instance, if it converges uniformly), then for every $m$
>
> $$
> c_m = \frac{\int_l^r f(x)\phi_m(x)p(x)\,dx}{\int_l^r \phi_m^2(x)p(x)\,dx} .
> $$
>
> *Powers: 2.8 (text)*

^prop-24-1

> [!proof]+ Proof
> Multiply both sides of (5) by $\phi_m(x)p(x)$, where $m$ is a fixed integer, and integrate from $l$ to $r$ term by term:
>
> $$
> \int_l^r f(x)\phi_m(x)p(x)\,dx = \sum_{n=1}^\infty c_n\int_l^r \phi_n(x)\phi_m(x)p(x)\,dx .
> $$
>
> By the orthogonality relation (4) every term of the series vanishes except the one with $n = m$. So
>
> $$
> \int_l^r f(x)\phi_m(x)p(x)\,dx = c_m\int_l^r \phi_m^2(x)p(x)\,dx ,
> $$
>
> and the integral on the right is positive ($p > 0$ and $\phi_m \not\equiv 0$), so it can be divided out. (Term-by-term integration of a uniformly convergent series is [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]], applied to the partial sums times the continuous function $\phi_m p$.)

^pf-24-1

*Uses:* [[§23 Sturm–Liouville Problems#^thm-23-2|§23.2]], [[§25 More on Uniform Convergence#^thm-25-1|451 Thm. §25.1]]

> [!remark]- Connections
> - The same formula in a finite-dimensional inner product space: the coefficient of $\mathbf{y}$ along an orthogonal basis vector $\mathbf{u}_j$ is $\langle\mathbf{y}, \mathbf{u}_j\rangle/\langle\mathbf{u}_j, \mathbf{u}_j\rangle$, [[§46 Inner Product Spaces#^thm-46-2|235 Thm. §46.2]]; here the inner product is $\langle f, g\rangle_p = \int_l^r fgp\,dx$. In a Hilbert space, for an orthonormal set: [[§24 Orthonormal Sets and Bases#^lem-24-7|556 Lem. §24.7]].

> [!definition] Definition §24.1: Generalized Fourier Coefficients
> Let $\phi_1, \phi_2, \ldots$ be the eigenfunctions of a regular Sturm–Liouville problem (1)–(3) and $f$ a sectionally continuous function on $l < x < r$. The numbers
>
> $$
> c_n = \frac{\int_l^r f(x)\phi_n(x)p(x)\,dx}{\int_l^r \phi_n^2(x)p(x)\,dx}
> $$
>
> are the **generalized Fourier coefficients** of $f$.
>
> *Powers: 2.8 (text); Source: 341 lectures 10.10, 10.17*

^def-24-1

> [!definition] Definition §24.1: Eigenfunction Expansion
> With the generalized Fourier coefficients $c_n$ of [[§24 Expansion in Series of Eigenfunctions#^def-24-1|Definition §24.1]], the series $\sum_{n=1}^\infty c_n\phi_n(x)$ is the **eigenfunction expansion** (generalized Fourier series) of $f$.
>
> *Powers: 2.8 (text); Source: 341 lectures 10.10, 10.17*

^def-24-new1

> [!definition] Definition §24.1: Generalized Fourier Basis
> The family $\{\phi_n\}$ of eigenfunctions is called a **generalized Fourier basis** when every such $f$ is represented by its expansion ([[§24 Expansion in Series of Eigenfunctions#^def-24-new1|Definition §24.1]]) in the sense of Theorem §24.2.
>
> *Powers: 2.8 (text); Source: 341 lectures 10.10, 10.17*

^def-24-new2

## Convergence

> [!theorem] Theorem §24.2: Convergence of Eigenfunction Expansions
> Let $\phi_1, \phi_2, \ldots$ be the eigenfunctions of a regular Sturm–Liouville problem (1)–(3) in which the $\alpha$'s and $\beta$'s are not negative. If $f(x)$ is sectionally smooth on the interval $l < x < r$, then
>
> $$
> \sum_{n=1}^\infty c_n\phi_n(x) = \frac{f(x+) + f(x-)}{2}, \qquad l < x < r , \qquad (6)
> $$
>
> where
>
> $$
> c_n = \frac{\int_l^r f(x)\phi_n(x)p(x)\,dx}{\int_l^r \phi_n^2(x)p(x)\,dx} .
> $$
>
> Furthermore, if the series
>
> $$
> \sum_{n=1}^\infty |c_n|\Big[\int_l^r \phi_n^2(x)p(x)\,dx\Big]^{1/2}
> $$
>
> converges, then the series (6) converges uniformly, $l \le x \le r$.
>
> *Powers: 2.8, Theorem*

^thm-24-2

*Powers omits the proof. For $s = p = 1$, $q = 0$ the theorem contains the convergence of Fourier sine and cosine series, [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]], proved in [[§12★ Proof of Convergence#^thm-12-4|Theorem §12.4]] and [[§12★ Proof of Convergence#^cor-12-5|Corollary §12.5]]; the general case is not proved in the vault.*

> [!remark]- Connections
> - The mean-square counterpart: the normalized eigenfunctions (remark below) form an orthonormal basis of the weighted $L^2$ space in the sense of [[§24 Orthonormal Sets and Bases#^def-24-4|556 Def. §24.4]], characterized by Parseval's equality in [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]]; the case $\phi'' + \lambda^2\phi = 0$ with periodic conditions is the Fourier basis, [[§24 Orthonormal Sets and Bases#^thm-24-11|556 Thm. §24.11]].
> - The uniform-convergence clause has the form of the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], for the series of normalized eigenfunctions, which are uniformly bounded for a regular problem.
> - Used in Electromagnetism: expanding boundary potentials in separated eigenfunctions — [[§C6.2 Separation in Cartesian and Spherical Coordinates#^thm-c6-2-1|EM Theorem §C6.2.1]].

Notice the similarity to the Fourier series convergence theorem: at a jump the series converges to the average of the one-sided limits. At an endpoint where the boundary condition is $\phi = 0$, every term vanishes, so the series converges to $0$ there whatever $f$ is ([[§24 Expansion in Series of Eigenfunctions#^ex-24-2|Example §24.2]]).

> [!remark] Remark: Normalized Eigenfunctions and Parseval's Identity
> Powers' exercises add the following. Write $a_n = \int_l^r \phi_n^2p\,dx$; the numbers $\sqrt{a_n}$ are the **normalizing constants**, and $\psi_n = \phi_n/\sqrt{a_n}$ are the **normalized eigenfunctions**. They satisfy
>
> $$
> \int_l^r \psi_n^2(x)p(x)\,dx = 1, \qquad \int_l^r \psi_n(x)\psi_m(x)p(x)\,dx = 0 \quad (n \ne m) ,
> $$
>
> and the expansion of $f$ in them is $f = \sum b_n\psi_n$ with $b_n = \int_l^r f\psi_np\,dx = c_n\sqrt{a_n}$. Multiplying $f = \sum c_n\phi_n$ by $f(x)p(x)$ and integrating term by term suggests **Parseval's identity**
>
> $$
> \int_l^r f^2(x)p(x)\,dx = \sum_{n=1}^\infty a_nc_n^2 = \sum_{n=1}^\infty b_n^2 ,
> $$
>
> from which $c_n\sqrt{a_n} = b_n \to 0$. The inequality $\sum b_n^2 \le \int f^2p$ (Bessel's inequality) holds for any orthonormal set and is [[§24 Orthonormal Sets and Bases#^thm-24-5|556 Thm. §24.5]]; equality for every $f$ is the statement that the set is complete. For example, for $\phi'' + \lambda^2\phi = 0$, $\phi'(0) = \phi'(1) = 0$ the normalized eigenfunctions are $\psi_0 = 1$ and $\psi_n = \sqrt2\cos(n\pi x)$, $n \ge 1$.

^rem-24-1

> [!remark] Remark: Fourier Series as Eigenfunction Expansions
> For $\phi'' + \lambda^2\phi = 0$ on $0 < x < a$ with $\phi(0) = \phi(a) = 0$, the eigenfunctions are $\sin(n\pi x/a)$, $\int_0^a \sin^2(n\pi x/a)\,dx = a/2$, and the coefficient formula gives $c_n = \frac2a\int_0^a f(x)\sin(n\pi x/a)\,dx$: the Fourier sine series of [[§7 Arbitrary Period and Half-Range Expansions#^def-7-new1|Definition §7.4]]. With $\phi'(0) = \phi'(a) = 0$ the eigenfunctions are $1$ (norm $a$) and $\cos(n\pi x/a)$ (norm $a/2$), giving the cosine series with $a_0 = \frac1a\int_0^a f\,dx$. What is new in general is only that the normalizing integrals differ from one eigenfunction to the next and have to be computed.

^rem-24-2

## Examples

> [!example] Example §24.1: Coefficients for the Convection Eigenfunctions
> The transient $w = u - v$ of the convection problem of [[§22 Example꞉ Convection#^thm-22-3|Theorem §22.3]] satisfies $w_{xx} = \frac1kw_t$ on $0 < x < a$ with $w(0, t) = 0$, $hw(a, t) + \kappa w_x(a, t) = 0$ and $w(x, 0) = g(x)$. Its basic solutions are $\sin(\lambda_nx)e^{-\lambda_n^2kt}$, where $\tan(\lambda_na) = -\kappa\lambda_n/h$, and
>
> $$
> w(x, t) = \sum_{n=1}^\infty c_n\sin(\lambda_nx)e^{-\lambda_n^2kt}, \qquad g(x) = w(x, 0) = \sum_{n=1}^\infty c_n\sin(\lambda_nx) .
> $$
>
> The eigenfunctions $\{\sin(\lambda_nx)\}$ are a generalized Fourier basis: orthogonal by [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] (or by direct integration, [[§23 Sturm–Liouville Problems#^ex-23-3|Example §23.3]]), and complete by Theorem §24.2. Multiplying by $\sin(\lambda_mx)$ and integrating,
>
> $$
> c_m = \frac{\int_0^a g(x)\sin(\lambda_mx)\,dx}{\int_0^a \sin^2(\lambda_mx)\,dx} = \frac{\int_0^a g(x)\sin(\lambda_mx)\,dx}{\dfrac a2 + \dfrac{\kappa}{h}\,\dfrac{\cos^2(\lambda_ma)}{2}} ,
> $$
>
> by [[§23 Sturm–Liouville Problems#^ex-23-3|Example §23.3]](a). The denominator is not $a/2$, as it would be for $\sin(m\pi x/a)$. For instance, for constant $g(x) = T$, $\int_0^a \sin(\lambda_mx)\,dx = (1 - \cos(\lambda_ma))/\lambda_m$ and
>
> $$
> c_m = \frac{2hT\big(1 - \cos(\lambda_ma)\big)}{\lambda_m\big(ha + \kappa\cos^2(\lambda_ma)\big)} .
> $$
>
> *Source: 341 lecture 10.10; 341 HW 7, Problem 1(a)*

^ex-24-1

> [!example] Example §24.2: A Generalized Fourier Basis on 1 < x < b
> The eigenfunctions of [[§23 Sturm–Liouville Problems#^ex-23-4|Example §23.4]] are $\phi_n(x) = \sin(n\pi\ln x/\ln b)$, $n = 1, 2, \ldots$, for the problem $x(x\phi')' = \mu\phi$, $\phi(1) = \phi(b) = 0$. Does $\{\phi_n\}$ form a generalized Fourier basis on $(1, b)$? If so, write the expansion of a function $f$ and its coefficients, and the solution of
>
> $$
> \frac{\partial u}{\partial t} = x\frac{\partial}{\partial x}\Big(x\frac{\partial u}{\partial x}\Big), \quad 1 < x < b, \qquad u(1, t) = u(b, t) = 0, \qquad u(x, 0) = f(x) .
> $$
>
> **Basis.** The problem is a regular Sturm–Liouville problem with $s = x$, $p = 1/x$, $q = 0$. By [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] the $\phi_n$ are orthogonal with weight $1/x$,
>
> $$
> \int_1^b \frac1x\,\phi_n(x)\phi_m(x)\,dx = 0, \qquad n \ne m ,
> $$
>
> and by Theorem §24.2 every sectionally smooth $f$ on $(1, b)$ has a convergent expansion. So $\{\phi_n\}$ is a generalized Fourier basis, and
>
> $$
> f(x) = \sum_{n=1}^\infty c_n\sin\Big(\frac{n\pi\ln x}{\ln b}\Big), \qquad c_n = \frac{\int_1^b \frac1xf(x)\phi_n(x)\,dx}{\int_1^b \frac1x\phi_n^2(x)\,dx} = \frac{2}{\ln b}\int_1^b f(x)\sin\Big(\frac{n\pi\ln x}{\ln b}\Big)\frac{dx}{x} ,
> $$
>
> because, with $y = \ln x$, $\int_1^b \frac1x\phi_n^2\,dx = \int_0^{\ln b}\sin^2(n\pi y/\ln b)\,dy = \frac12\ln b$.
>
> **Solution.** The basic solutions are $w_n(x, t) = \phi_n(x)T_n(t) = e^{-(n\pi/\ln b)^2t}\sin(n\pi\ln x/\ln b)$, and since the equation and boundary conditions are homogeneous, no steady state needs to be subtracted:
>
> $$
> u(x, t) = \sum_{n=1}^\infty c_n\,e^{-(n\pi/\ln b)^2t}\sin\Big(\frac{n\pi\ln x}{\ln b}\Big) .
> $$
>
> **The case $f(x) = x$** (Powers' Exercise 2.8.1). With $y = \ln x$, $L = \ln b$ and $k_n = n\pi/L$,
>
> $$
> c_n = \frac2L\int_0^L e^y\sin(k_ny)\,dy = \frac2L\Big[\frac{e^y\big(\sin(k_ny) - k_n\cos(k_ny)\big)}{1 + k_n^2}\Big]_0^L = \frac2L\cdot\frac{k_n\big(1 - (-1)^nb\big)}{1 + k_n^2} = \frac{2n\pi\big(1 - (-1)^nb\big)}{n^2\pi^2 + (\ln b)^2} .
> $$
>
> At $x = 1$ and $x = b$ every term of the series vanishes, so the series converges to $0$ there, not to $f(1) = 1$ and $f(b) = b$; inside, it converges to $x$ (figure).
>
> *The key writes $\log a$ for $\log b$ inside the sine in its final formula for $u$.*
>
> *Source: 341 HW 8, Problem 1(c)–(e)*

^ex-24-2

![[m341-24-1.svg]]
*Partial sums $\sum_{n=1}^N c_n\sin(n\pi\ln x)$ of the expansion of $f(x) = x$ in Example §24.2, for $b = e$, where $c_n = 2n\pi(1 - (-1)^ne)/(1 + n^2\pi^2)$. Inside $(1, e)$ they approach $x$ (dashed); at both ends every eigenfunction vanishes, so the sums are pinned to $0$ and overshoot near the ends, as a Fourier sine series does for a function that is not zero at the endpoints.*

> [!example] Example §24.3: Expanding x² in the Eigenfunctions cos(λₙx)
> Find the eigenvalues and eigenfunctions of
>
> $$
> \phi'' = \mu\phi, \quad 0 < x < 2, \qquad \phi'(0) = 0, \qquad \phi'(2) + \phi(2) = 0 ,
> $$
>
> and the coefficients of the expansion $x^2 = \sum c_n\phi_n(x)$ on $0 < x < 2$. (This is the eigenvalue problem of the heat problem in [[§25 Generalities on the Heat Conduction Problem#^ex-25-1|Example §25.1]].)
>
> **Cases.**
> - $\mu = \lambda^2 > 0$: $\phi = Ae^{\lambda x} + Be^{-\lambda x}$, and $\phi'(0) = \lambda(A - B) = 0$ gives $A = B$, $\phi = 2A\cosh\lambda x$. Then $\phi'(2) + \phi(2) = 2A(\lambda\sinh 2\lambda + \cosh 2\lambda) = 0$, and the bracket is positive, so $A = 0$: no nonzero solution.
> - $\mu = 0$: $\phi = Ax + B$, $\phi'(0) = A = 0$, $\phi'(2) + \phi(2) = B = 0$: no nonzero solution.
> - $\mu = -\lambda^2 < 0$: $\phi = A\sin\lambda x + B\cos\lambda x$, $\phi'(0) = A\lambda = 0$ gives $A = 0$, and $\phi'(2) + \phi(2) = B(\cos 2\lambda - \lambda\sin 2\lambda) = 0$. A nonzero solution $\phi = B\cos(\lambda x)$ exists exactly when
>
> $$
> \cot(2\lambda) = \lambda .
> $$
>
> This is a regular Sturm–Liouville problem with all $\alpha$'s and $\beta$'s nonnegative, so the absence of nonnegative $\mu$ is what [[§23 Sturm–Liouville Problems#^thm-23-5|Theorem §23.5]](c) leads one to expect.
>
> **The eigenvalues.** The positive roots $\lambda_n$ are the $\lambda$-coordinates of the intersections of $y = \cot 2\lambda$ with the line $y = \lambda$ (figure). There is one on each branch of the cotangent, with $(n - 1)\frac\pi2 < \lambda_n < (n - 1)\frac\pi2 + \frac\pi4$, and $\lambda_n - (n - 1)\frac\pi2 \to 0$ as $n \to \infty$. Numerically,
>
> $$
> \lambda_n \approx 0.5384,\ 1.8218,\ 3.2892,\ 4.8148,\ 6.3611,\ 7.9168,\ \ldots
> $$
>
> **Coefficients.** The weight is $1$, so $c_n = \int_0^2 x^2\cos(\lambda_nx)\,dx \big/ \int_0^2 \cos^2(\lambda_nx)\,dx$. Both integrals simplify with the eigenvalue equation in the form $\cos 2\lambda_n = \lambda_n\sin 2\lambda_n$:
>
> $$
> \int_0^2 \cos^2(\lambda_nx)\,dx = 1 + \frac{\sin 4\lambda_n}{4\lambda_n} = 1 + \frac{\sin 2\lambda_n\cos 2\lambda_n}{2\lambda_n} = 1 + \frac12\sin^2 2\lambda_n ,
> $$
>
> and, integrating by parts twice,
>
> $$
> \int_0^2 x^2\cos(\lambda_nx)\,dx = \Big[\frac{x^2\sin\lambda_nx}{\lambda_n} + \frac{2x\cos\lambda_nx}{\lambda_n^2} - \frac{2\sin\lambda_nx}{\lambda_n^3}\Big]_0^2 = \frac{4\sin 2\lambda_n}{\lambda_n} + \frac{4\cos 2\lambda_n}{\lambda_n^2} - \frac{2\sin 2\lambda_n}{\lambda_n^3} = \sin 2\lambda_n\Big(\frac8{\lambda_n} - \frac2{\lambda_n^3}\Big) .
> $$
>
> Hence
>
> $$
> c_n = \frac{4(4\lambda_n^2 - 1)\sin 2\lambda_n}{\lambda_n^3\,(2 + \sin^2 2\lambda_n)} \approx 1.2980,\ -1.7511,\ 0.6631,\ -0.3275,\ 0.1918,\ \ldots
> $$
>
> The normalizing integrals $1.3876$, $1.1158$, $1.0423$, … differ from term to term and approach $1 = \frac12\cdot 2$, the value for $\cos(n\pi x/2)$.
>
> *Source: 341 HW 7, Problem 2(c)–(f)*

^ex-24-3

![[m341-24-2.svg]]
*The eigenvalue equation $\cot 2\lambda = \lambda$ of Example §24.3, solved graphically. Each branch of $\cot 2\lambda$ (between the dashed asymptotes $\lambda = j\pi/2$) meets the line $y = \lambda$ once; the roots $\lambda_1, \lambda_2, \ldots$ (red) lie in the left half of each branch, where $\cot 2\lambda > 0$, and approach its left asymptote as $n$ grows.*
