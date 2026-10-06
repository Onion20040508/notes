---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: 43
powers: "5.3"
aliases: ["Powers 5.3"]
tags: [fourier-series-and-pdes, math341]
---
← [[§42 Three-Dimensional Heat Equation]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§44★ Problems in Polar Coordinates]] →

*Powers, Section 5.3 · MAT 341 lecture 11.26 · HW 13 · Practice Final.*

This section solves the heat equation in a rectangular plate whose edges are held at temperature zero. Separation of variables is applied twice: $u = \phi(x, y)T(t)$ separates time from space and leaves a two-dimensional eigenvalue problem $\nabla^2\phi = -\lambda^2\phi$, and $\phi = X(x)Y(y)$ splits that into two familiar one-dimensional problems. The eigenfunctions $\sin(m\pi x/a)\sin(n\pi y/b)$ carry two indices, so the solution is a double Fourier sine series whose coefficients come from a double integral, by orthogonality. Every term decays exponentially, the one with the smallest eigenvalue most slowly, so the plate cools to zero in the shape of that lowest mode. The same eigenfunctions, with oscillating instead of decaying time factors, give the vibrations of a rectangular membrane.

## The Problem and the First Separation

The initial value–boundary value problem for the transient temperature $u(x, y, t)$ in a rectangular plate of uniform, isotropic material, with its edges held at temperature $0$, is

$$
\begin{aligned}
&\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = \frac{1}{k}\frac{\partial u}{\partial t}, && 0 < x < a, \quad 0 < y < b, \quad 0 < t, && (1) \\
&u(x, 0, t) = 0, \quad u(x, b, t) = 0, && 0 < x < a, \quad 0 < t, && (2) \\
&u(0, y, t) = 0, \quad u(a, y, t) = 0, && 0 < y < b, \quad 0 < t, && (3) \\
&u(x, y, 0) = f(x, y), && 0 < x < a, \quad 0 < y < b . && (4)
\end{aligned}
$$

The partial differential equation and the boundary conditions are homogeneous, so separation of variables applies. (Nonzero edge temperatures are first removed by subtracting a steady state; see Remark: Method below.)

> [!definition] Definition §43.1: The Eigenvalue Problem for the Rectangle
> The **two-dimensional eigenvalue problem** for the rectangle $0 < x < a$, $0 < y < b$ is
>
> $$
> \begin{aligned}
> &\frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} = -\lambda^2\phi, && 0 < x < a, \quad 0 < y < b, && (6) \\
> &\phi(x, 0) = 0, \quad \phi(x, b) = 0, && 0 < x < a, && (7) \\
> &\phi(0, y) = 0, \quad \phi(a, y) = 0, && 0 < y < b . && (8)
> \end{aligned}
> $$
>
> A number $\lambda^2$ for which it has a solution $\phi$ that is not identically zero is an **eigenvalue**, and such a $\phi$ is a corresponding **eigenfunction**.
>
> *Powers: 5.3, Equations (6)–(8)*

^def-43-1

> [!theorem] Theorem §43.1: Product Solutions of the Heat Problem
> A product $u(x, y, t) = \phi(x, y)T(t)$, not identically zero, satisfies (1)–(3) if and only if, for some constant $\lambda^2$, $\phi$ is a solution of the eigenvalue problem (6)–(8) and
>
> $$
> T' + \lambda^2kT = 0, \qquad 0 < t . \qquad (5)
> $$
>
> *Powers: 5.3 (text), Equations (5)–(8)*

^thm-43-1

> [!proof]+ Proof
> Substituting $u = \phi T$ into (1) gives
>
> $$
> \Big(\frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2}\Big)T = \frac{1}{k}\phi T' .
> $$
>
> Dividing by $\phi T$ separates the variables:
>
> $$
> \Big(\frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2}\Big)\frac{1}{\phi} = \frac{T'}{kT} .
> $$
>
> The left side depends only on $(x, y)$ and the right side only on $t$, so their common value is a constant, which we expect to be negative and call $-\lambda^2$ (Theorem §43.2 shows that it is). This gives (5) and (6). In terms of the product, the boundary conditions (2) and (3) become
>
> $$
> \phi(x, 0)T(t) = 0, \quad \phi(x, b)T(t) = 0, \quad \phi(0, y)T(t) = 0, \quad \phi(a, y)T(t) = 0 .
> $$
>
> Either $T(t) \equiv 0$, which wipes out the solution completely, or $\phi = 0$ on the boundary, which is (7) and (8). Conversely, if $\phi$ solves (6)–(8) and $T$ solves (5), then $\nabla^2(\phi T) = -\lambda^2\phi T = \phi T'/k$ and $\phi T$ vanishes on the edges.

^pf-43-1

*Uses:* [[§43 Two-Dimensional Heat Equation꞉ Solution#^def-43-1|Def. §43.1]]

## Solving the Eigenvalue Problem

Equations (6)–(8) form a new problem, a two-dimensional eigenvalue problem. But the equation and the boundary conditions are linear and homogeneous, so separation of variables may work again.

> [!theorem] Theorem §43.2: Eigenvalues and Eigenfunctions of the Rectangle
> The product solutions $\phi = X(x)Y(y)$ of the eigenvalue problem (6)–(8) are the multiples of
>
> $$
> \phi_{mn}(x, y) = \sin\Big(\frac{m\pi x}{a}\Big)\sin\Big(\frac{n\pi y}{b}\Big), \qquad \lambda_{mn}^2 = \mu_m^2 + \nu_n^2 = \Big(\frac{m\pi}{a}\Big)^2 + \Big(\frac{n\pi}{b}\Big)^2 ,
> $$
>
> with $m = 1, 2, 3, \ldots$ and $n = 1, 2, 3, \ldots$ independently. In particular every eigenvalue $\lambda_{mn}^2$ is positive.
>
> *Powers: 5.3 (text), Equations (9)–(13)*

^thm-43-2

> [!proof]+ Proof
> **Separation.** With $\phi = X(x)Y(y)$, the equation (6) becomes $X''Y + XY'' = -\lambda^2XY$, or
>
> $$
> \frac{X''(x)}{X(x)} + \frac{Y''(y)}{Y(y)} = -\lambda^2, \qquad 0 < x < a, \quad 0 < y < b .
> $$
>
> The sum of a function of $x$ and a function of $y$ can be constant only if the two functions are individually constant. (Powers asserts this; here is why: differentiating with respect to $x$ gives $(X''/X)' = 0$, so $X''/X$ is constant on the interval $0 < x < a$, and then so is $Y''/Y$.)
>
> **Boundary conditions.** On $\phi = XY$ they read $X(x)Y(0) = 0$, $X(x)Y(b) = 0$ for $0 < x < a$ and $X(0)Y(y) = 0$, $X(a)Y(y) = 0$ for $0 < y < b$. If either $X$ or $Y$ is zero throughout its interval, $\phi$ is identically zero. So each function must vanish at the endpoints of its interval:
>
> $$
> Y(0) = 0, \quad Y(b) = 0, \qquad (9) \qquad\qquad X(0) = 0, \quad X(a) = 0 . \qquad (10)
> $$
>
> **The constants are negative.** If $X'' = pX$ with $p \ge 0$ and $X(0) = X(a) = 0$, then $X \equiv 0$: for $p = 0$, $X = A + Bx$ forces $A = B = 0$; for $p > 0$, $X = A\cosh\sqrt{p}\,x + B\sinh\sqrt{p}\,x$, and $X(0) = 0$ gives $A = 0$, then $X(a) = B\sinh\sqrt{p}\,a = 0$ gives $B = 0$. The same holds for $Y$. So the ratios are negative constants, $X''/X = -\mu^2$ and $Y''/Y = -\nu^2$, and
>
> $$
> X'' + \mu^2X = 0, \quad 0 < x < a, \qquad (11) \qquad\qquad Y'' + \nu^2Y = 0, \quad 0 < y < b, \qquad (12)
> $$
>
> $$
> \lambda^2 = \mu^2 + \nu^2 . \qquad (13)
> $$
>
> **Two independent eigenvalue problems.** Equations (10) and (11) form one problem, (9) and (12) the other, each of the familiar form solved for the rod with fixed end temperatures ([[§19 Example꞉ Fixed End Temperatures#^thm-19-2|Theorem §19.2]]): $X = A\cos\mu x + B\sin\mu x$, $X(0) = 0$ gives $A = 0$, and $X(a) = B\sin\mu a = 0$ with $B \ne 0$ requires $\mu a = m\pi$. Hence
>
> $$
> X_m(x) = \sin\Big(\frac{m\pi x}{a}\Big), \quad \mu_m^2 = \Big(\frac{m\pi}{a}\Big)^2, \qquad Y_n(y) = \sin\Big(\frac{n\pi y}{b}\Big), \quad \nu_n^2 = \Big(\frac{n\pi}{b}\Big)^2 ,
> $$
>
> with $m, n = 1, 2, \ldots$. The indices $m$ and $n$ are independent, so $\phi_{mn} = X_mY_n$ has a double index, and $\lambda_{mn}^2 = \mu_m^2 + \nu_n^2 > 0$ by (13).

^pf-43-2

*Uses:* [[§43 Two-Dimensional Heat Equation꞉ Solution#^def-43-1|Def. §43.1]], [[§19 Example꞉ Fixed End Temperatures#^thm-19-2|§19.2]] (the one-dimensional problem)

The theorem finds the product eigenfunctions. That there are no others (every eigenfunction is a finite combination of $\phi_{mn}$ with the same eigenvalue) follows from the completeness of the double sine series below, by the orthogonality argument of [[§44★ Problems in Polar Coordinates#^thm-44-3|Theorem §44.3]]. With $\lambda^2 = \lambda_{mn}^2$, the time factor solving (5) is

$$
T_{mn}(t) = \exp\big(-\lambda_{mn}^2kt\big) .
$$

## The Double Series Solution

> [!theorem] Theorem §43.3: Orthogonality of the Eigenfunctions
> For $m, n, p, q = 1, 2, \ldots$,
>
> $$
> \int_0^b\!\!\int_0^a \phi_{mn}(x, y)\,\phi_{pq}(x, y)\,dx\,dy = \begin{cases} \dfrac{ab}{4} & \text{if } m = p \text{ and } n = q, \\[2mm] 0 & \text{otherwise.} \end{cases} \qquad (16)
> $$
>
> *Powers: 5.3, Equation (16); Exercise 5.3.8*

^thm-43-3

> [!proof]+ Proof
> The integrand is a product of a function of $x$ and a function of $y$, so the double integral over the rectangle is the product of two single integrals:
>
> $$
> \int_0^b\!\!\int_0^a \phi_{mn}\phi_{pq}\,dx\,dy = \int_0^a \sin\frac{m\pi x}{a}\sin\frac{p\pi x}{a}\,dx \cdot \int_0^b \sin\frac{n\pi y}{b}\sin\frac{q\pi y}{b}\,dy .
> $$
>
> By $\sin A\sin B = \frac12[\cos(A - B) - \cos(A + B)]$,
>
> $$
> \int_0^a \sin\frac{m\pi x}{a}\sin\frac{p\pi x}{a}\,dx = \frac12\int_0^a \Big[\cos\frac{(m - p)\pi x}{a} - \cos\frac{(m + p)\pi x}{a}\Big]dx = \begin{cases} a/2, & m = p, \\ 0, & m \ne p, \end{cases}
> $$
>
> since $\int_0^a \cos(j\pi x/a)\,dx = 0$ for every integer $j \ne 0$ and the first cosine is $1$ when $m = p$. In the same way the $y$-integral is $b/2$ if $n = q$ and $0$ otherwise. The product is $ab/4$ when both index pairs agree and $0$ otherwise.

^pf-43-3

*Uses:* [[§98 Double Integrals Over Rectangles#^thm-98-4|Calc Thm. §98.4]] (integrals of products)

> [!theorem] Theorem §43.4: Solution of the Heat Problem in a Rectangle
> For each pair of indices $m, n$ the function
>
> $$
> u_{mn}(x, y, t) = \phi_{mn}(x, y)T_{mn}(t) = \sin\Big(\frac{m\pi x}{a}\Big)\sin\Big(\frac{n\pi y}{b}\Big)\exp\big(-\lambda_{mn}^2kt\big)
> $$
>
> satisfies the partial differential equation (1) and the boundary conditions (2) and (3), and so does the double series
>
> $$
> u(x, y, t) = \sum_{m=1}^{\infty}\sum_{n=1}^{\infty} a_{mn}\,\phi_{mn}(x, y)\,T_{mn}(t) . \qquad (14)
> $$
>
> It satisfies the initial condition (4) if
>
> $$
> \sum_{m=1}^{\infty}\sum_{n=1}^{\infty} a_{mn}\,\phi_{mn}(x, y) = f(x, y), \qquad 0 < x < a, \quad 0 < y < b , \qquad (15)
> $$
>
> and the coefficients are then
>
> $$
> a_{mn} = \frac{4}{ab}\int_0^b\!\!\int_0^a f(x, y)\sin\Big(\frac{m\pi x}{a}\Big)\sin\Big(\frac{n\pi y}{b}\Big)\,dx\,dy . \qquad (17)
> $$
>
> If $f$ is a sufficiently regular function, the series (15) converges to $f(x, y)$ in the rectangle, and (14) solves the problem (1)–(4). Each term decays exponentially, so $u(x, y, t) \to 0$ as $t \to \infty$.
>
> *Powers: 5.3, Equations (14)–(17)*

^thm-43-4

> [!proof]+ Proof
> **Each $u_{mn}$ is a solution** (Powers' Exercise 5.3.4). By Theorem §43.2, $\nabla^2\phi_{mn} = -\lambda_{mn}^2\phi_{mn}$, and $T_{mn}' = -\lambda_{mn}^2kT_{mn}$, so
>
> $$
> \nabla^2u_{mn} = -\lambda_{mn}^2u_{mn} = \frac{1}{k}\frac{\partial u_{mn}}{\partial t} ;
> $$
>
> and $u_{mn}$ vanishes on the four edges because $\sin 0 = \sin m\pi = \sin n\pi = 0$.
>
> **Superposition.** The equation and the boundary conditions are linear and homogeneous, so every finite linear combination of the $u_{mn}$ satisfies them ([[§19 Example꞉ Fixed End Temperatures#^thm-19-4|Theorem §19.4]]), and so does the series (14) whenever it can be differentiated term by term. (Powers sets the convergence aside; here is why this holds for $t > 0$.) By (17), $|a_{mn}| \le M := \frac{4}{ab}\iint|f|\,dx\,dy$. Fix $t_0 > 0$. For $t \ge t_0$ the terms of (14) and of the series for $u_x$, $u_{xx}$, $u_y$, $u_{yy}$, $u_t$ are bounded in absolute value by
>
> $$
> M(1 + k)(1 + \mu_m^2)(1 + \nu_n^2)\,e^{-\mu_m^2kt_0}e^{-\nu_n^2kt_0} ,
> $$
>
> since $\lambda_{mn}^2 = \mu_m^2 + \nu_n^2$ and $\mu_m, \mu_m^2, \nu_n, \nu_n^2, \lambda_{mn}^2 \le (1 + \mu_m^2)(1 + \nu_n^2)$. The double sum of these bounds is $M(1 + k)\sum_m(1 + \mu_m^2)e^{-\mu_m^2kt_0}\cdot\sum_n(1 + \nu_n^2)e^{-\nu_n^2kt_0}$, a product of two series that converge by the [[Ratio Test|ratio test]]. By the Weierstrass M-test the six series converge absolutely (so in any order of summation) and uniformly on $0 \le x \le a$, $0 \le y \le b$, $t \ge t_0$. Their sums are continuous, and term-by-term differentiation is justified one variable at a time exactly as in the proof of [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|Theorem §19.5]]: integrate the uniformly convergent differentiated series term by term and apply the fundamental theorem of calculus. Since each term vanishes on the edges, so does the sum.
>
> **The coefficients.** At $t = 0$, (14) becomes (15). Multiply (15) by $\phi_{pq}$ and integrate over the rectangle. Integrating term by term (legitimate if the series converges uniformly, and in general in the mean-square sense) and using the orthogonality (16), every term vanishes except the one with $(m, n) = (p, q)$:
>
> $$
> \int_0^b\!\!\int_0^a f\,\phi_{pq}\,dx\,dy = a_{pq}\,\frac{ab}{4} ,
> $$
>
> which is (17).

^pf-43-4

*Uses:* [[§43 Two-Dimensional Heat Equation꞉ Solution#^thm-43-1|§43.1]], [[§43 Two-Dimensional Heat Equation꞉ Solution#^thm-43-2|§43.2]], [[§43 Two-Dimensional Heat Equation꞉ Solution#^thm-43-3|§43.3]], [[§19 Example꞉ Fixed End Temperatures#^thm-19-4|§19.4]], [[§19 Example꞉ Fixed End Temperatures#^thm-19-5|§19.5]], [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]] (M-test), [[§25 More on Uniform Convergence#^thm-25-2|451 Thm. §25.2]], [[§26 Differentiation and Integration of Power Series#^thm-26-3|451 Thm. §26.3]], [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]], [[§74 The Ratio and Root Tests#^thm-74-1|Calc Thm. §74.1]] (ratio test)

*Powers omits the proof that the double series (15) converges to $f$. In the mean-square sense it follows from the completeness of the one-dimensional sine systems on $(0, a)$ and $(0, b)$ (for the exponential form on an interval, [[§24 Orthonormal Sets and Bases#^thm-24-11|556 Thm. §24.11]]): products of orthonormal bases of the two intervals form an orthonormal basis of the rectangle, a fact the vault does not prove.*

> [!remark]- Connections
> - The normalized functions $\frac{2}{\sqrt{ab}}\phi_{mn}$ form an orthonormal set by (16), and (17) gives the coefficients of $f$ with respect to it. Completeness of this set is the statement that (15) holds in mean square, and is equivalent to Parseval's equality $\frac{4}{ab}\iint f^2 = \sum\sum a_{mn}^2$: [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]].
> - The two-dimensional analogue of the half-range sine series ([[§7a Even and Odd Functions; Half-Range Expansions#^def-7-new1|Definition §7.4]]). The $\phi_{mn}$ are eigenvectors of the symmetric operator $-\nabla^2$ with zero boundary values, and orthogonality for distinct eigenvalues is the infinite-dimensional analogue of [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]]; for a general region it is proved with Green's identity in [[§44★ Problems in Polar Coordinates#^thm-44-3|Theorem §44.3]].

> [!remark] Remark: Method — Heat Problems in a Rectangle
> To solve $u_t = k(u_{xx} + u_{yy})$ in $0 < x < a$, $0 < y < b$ with given edge temperatures and initial temperature $h(x, y)$:
> 1. **Steady state.** Find $v(x, y) = \lim_{t\to\infty} u(x, y, t)$: it solves Laplace's equation $\nabla^2v = 0$ with the given edge temperatures, a potential problem in a rectangle, solved by superposition of rectangle problems with one nonzero side each ([[§36 Potential in a Rectangle#^thm-36-2|Theorem §36.2]]; [[§37 Further Examples for a Rectangle#^rem-37-1|Remark: Method — Splitting a Rectangle Problem]]). If the edge temperatures are zero, $v = 0$.
> 2. **Transient problem** (as for the rod, [[§19 Example꞉ Fixed End Temperatures#^rem-19-1|Remark: Method — The Steady-State/Transient Split]]). $w = u - v$ satisfies the heat equation with zero edge temperatures and initial condition $w(x, y, 0) = h(x, y) - v(x, y)$: the problem (1)–(4) with $f = h - v$.
> 3. **Separate** $w = \phi(x, y)T(t)$: $T' = -\lambda^2kT$ and the eigenvalue problem (6)–(8) (Theorem §43.1).
> 4. **Separate again**, $\phi = X(x)Y(y)$: two one-dimensional eigenvalue problems, $\phi_{mn} = \sin(m\pi x/a)\sin(n\pi y/b)$, $\lambda_{mn}^2 = (m\pi/a)^2 + (n\pi/b)^2$ (Theorem §43.2). Basic solutions $w_{mn} = \phi_{mn}e^{-\lambda_{mn}^2kt}$.
> 5. **Double series** $w = \sum\sum a_{mn}w_{mn}$, with $a_{mn}$ from (17) applied to $f = h - v$; if $f$ is already a finite combination of the $\phi_{mn}$, read the coefficients off by matching terms.
> 6. **Answer** $u = v + w$.
>
> *Source: 341 lecture 11.26*

^rem-43-1

> [!remark] Remark: Insulated Edges
> If the edges $x = 0$ and $x = a$ are insulated instead, $u_x(0, y, t) = u_x(a, y, t) = 0$, then the $x$-problem becomes $X'' + \mu^2X = 0$, $X'(0) = X'(a) = 0$, with $X_m = \cos(m\pi x/a)$ and $\mu_m = m\pi/a$ for $m = 0, 1, 2, \ldots$, including $m = 0$ (Powers' Exercise 5.3.5). The eigenvalues are still $\lambda_{mn}^2 = (m\pi/a)^2 + (n\pi/b)^2$, and
>
> $$
> u(x, y, t) = \sum_{m=0}^{\infty}\sum_{n=1}^{\infty} a_{mn}\cos\Big(\frac{m\pi x}{a}\Big)\sin\Big(\frac{n\pi y}{b}\Big)e^{-\lambda_{mn}^2kt}, \qquad a_{0n} = \frac{2}{ab}\iint f\sin\frac{n\pi y}{b}, \quad a_{mn} = \frac{4}{ab}\iint f\cos\frac{m\pi x}{a}\sin\frac{n\pi y}{b} ,
> $$
>
> the factor for $m = 0$ being different because $\int_0^a \cos^2 0\,dx = a$ rather than $a/2$. If all four edges are insulated, both factors are cosines, the term $m = n = 0$ is the constant $a_{00} = \frac{1}{ab}\iint f\,dx\,dy$ with $\lambda_{00} = 0$, and $u \to a_{00}$: the plate settles to its mean initial temperature, as no heat can leave.

^rem-43-2

## Examples

> [!example] Example §43.1: Initial Temperature f(x, y) = xy
> Solve (1)–(4) with $f(x, y) = xy$, $0 < x < a$, $0 < y < b$.
>
> **The $x$-integral.** Integrating by parts,
>
> $$
> \int_0^a x\sin\frac{m\pi x}{a}\,dx = \Big[-\frac{a}{m\pi}x\cos\frac{m\pi x}{a}\Big]_0^a + \frac{a}{m\pi}\int_0^a \cos\frac{m\pi x}{a}\,dx = -\frac{a^2}{m\pi}\cos m\pi + 0 = \frac{a^2(-1)^{m+1}}{m\pi} .
> $$
>
> In the same way $\int_0^b y\sin(n\pi y/b)\,dy = b^2(-1)^{n+1}/(n\pi)$.
>
> **The coefficients.** Since $f = x\cdot y$ is a product, (17) factors:
>
> $$
> a_{mn} = \frac{4}{ab}\cdot\frac{a^2(-1)^{m+1}}{m\pi}\cdot\frac{b^2(-1)^{n+1}}{n\pi} = \frac{4ab\cos(m\pi)\cos(n\pi)}{\pi^2mn} = \frac{4ab}{\pi^2}\,\frac{(-1)^{m+n}}{mn} .
> $$
>
> **The solution.**
>
> $$
> u(x, y, t) = \frac{4ab}{\pi^2}\sum_{m=1}^{\infty}\sum_{n=1}^{\infty} \frac{(-1)^{m+n}}{mn}\sin\Big(\frac{m\pi x}{a}\Big)\sin\Big(\frac{n\pi y}{b}\Big)\exp\big(-\lambda_{mn}^2kt\big) . \qquad (18)
> $$
>
> For large $t$ the term with the smallest eigenvalue, $(m, n) = (1, 1)$, dominates: $u \approx \frac{4ab}{\pi^2}\sin\frac{\pi x}{a}\sin\frac{\pi y}{b}\exp\big(-\pi^2(a^{-2} + b^{-2})kt\big)$, a single hump that decays without changing shape. Since $f = xy$ is not zero on the edges $x = a$ and $y = b$, the series (15) converges to $f$ only inside the rectangle, with Gibbs overshoots near those edges; for $t > 0$ the solution is smooth.
>
> *Powers: 5.3, Example*

^ex-43-1

![[m341-43-1.svg]]
*The solution (18) for $a = b = 1$, $k = 1$, along the line $y = \frac12$, where $f(x, \frac12) = x/2$ (dashed). The thin gray curve is a partial sum of (15) at $t = 0$, with the Gibbs overshoot at $x = 1$, where $f$ jumps to the boundary value $0$. By $t = 0.005$ the jump is already smoothed out, and by $t = 0.1$ the profile is close to the lowest mode $\sin\pi x$, decaying like $e^{-2\pi^2t}$.*

> [!example] Example §43.2: Ordering the Double Series
> A double series is best handled by converting it into a single series, arranging the terms in order of increasing $\lambda_{mn}^2$: the first terms are the most significant, since they decay least rapidly. Order the terms for (a) $a = 2b$, (b) $a = b$, and write the first few terms of (18) in case (b).
>
> **(a)** If $a = 2b$, then $\lambda_{mn}^2 = \dfrac{m^2\pi^2}{a^2} + \dfrac{4n^2\pi^2}{a^2} = \dfrac{(m^2 + 4n^2)\pi^2}{a^2}$. The values of $m^2 + 4n^2$ are
>
> | $(m, n)$ | $(1, 1)$ | $(2, 1)$ | $(3, 1)$ | $(1, 2)$ | $(2, 2)$ | $(4, 1)$ | $(3, 2)$ | $(5, 1)$ |
> |---|---|---|---|---|---|---|---|---|
> | $m^2 + 4n^2$ | $5$ | $8$ | $13$ | $17$ | $20$ | $20$ | $25$ | $29$ |
>
> so the order is $(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (4, 1), (3, 2), \ldots$; the pairs $(2, 2)$ and $(4, 1)$ share an eigenvalue.
>
> **(b)** If $a = b$, then $\lambda_{mn}^2 = (m^2 + n^2)\pi^2/a^2$, with $m^2 + n^2 = 2$ for $(1, 1)$; $5$ for $(1, 2)$ and $(2, 1)$; $8$ for $(2, 2)$; $10$ for $(1, 3)$ and $(3, 1)$. Every eigenvalue with $m \ne n$ is shared by $(m, n)$ and $(n, m)$. With the coefficients $(-1)^{m+n}/(mn)$ of (18), the terms with the four smallest eigenvalues are
>
> $$
> \begin{aligned}
> u(x, y, t) \approx \frac{4a^2}{\pi^2}\Big[&\sin\frac{\pi x}{a}\sin\frac{\pi y}{a}\,e^{-2\pi^2kt/a^2} - \frac12\Big(\sin\frac{\pi x}{a}\sin\frac{2\pi y}{a} + \sin\frac{2\pi x}{a}\sin\frac{\pi y}{a}\Big)e^{-5\pi^2kt/a^2} \\
> &+ \frac14\sin\frac{2\pi x}{a}\sin\frac{2\pi y}{a}\,e^{-8\pi^2kt/a^2} + \frac13\Big(\sin\frac{\pi x}{a}\sin\frac{3\pi y}{a} + \sin\frac{3\pi x}{a}\sin\frac{\pi y}{a}\Big)e^{-10\pi^2kt/a^2}\Big] .
> \end{aligned}
> $$
>
> *Powers: 5.3 (text); Exercise 5.3.1*

^ex-43-2

> [!example] Example §43.3: A Single Mode on the Rectangle 1 × 2
> Solve
>
> $$
> \begin{aligned}
> &u_t = u_{xx} + u_{yy}, && 0 < x < 1, \quad 0 < y < 2, \quad t > 0, \\
> &u(x, 0, t) = 0, \quad u(x, 2, t) = 0, && 0 < x < 1, \quad t > 0, \\
> &u(0, y, t) = 0, \quad u(1, y, t) = 0, && 0 < y < 2, \quad t > 0, \\
> &u(x, y, 0) = \sin(\pi x)\sin(\pi y), && 0 < x < 1, \quad 0 < y < 2 .
> \end{aligned}
> $$
>
> **(a) First separation.** With $u = \Phi(x, y)T(t)$, $\dfrac{\Delta\Phi}{\Phi} = \dfrac{T'}{T} = p$, a constant: $\Delta\Phi = p\Phi$ with $\Phi(x, 0) = \Phi(x, 2) = 0$, $\Phi(0, y) = \Phi(1, y) = 0$, and $T' = pT$.
>
> **(b) Second separation.** With $\Phi = X(x)Y(y)$, $X''/X + Y''/Y = p$, so $X'' = \alpha X$, $X(0) = X(1) = 0$ and $Y'' = \beta Y$, $Y(0) = Y(2) = 0$, with $\alpha + \beta = p$. Nonzero solutions exist only for $\alpha = -(m\pi)^2$, $X_m = \sin(m\pi x)$, and $\beta = -(n\pi/2)^2$, $Y_n = \sin(n\pi y/2)$ (Theorem §43.2 with $a = 1$, $b = 2$). So $\Phi_{mn} = \sin(m\pi x)\sin(n\pi y/2)$ and
>
> $$
> p = -\lambda_{mn}^2 = -\pi^2\Big(m^2 + \frac{n^2}{4}\Big) .
> $$
>
> **(c) Basic solutions.** $T_{mn} = e^{-\pi^2(m^2 + n^2/4)t}$ and $u_{mn} = \sin(m\pi x)\sin(n\pi y/2)\,e^{-\pi^2(m^2 + n^2/4)t}$.
>
> **(d) The solution.** $u = \sum\sum A_{mn}u_{mn}$, and at $t = 0$ we need $\sum\sum A_{mn}\sin(m\pi x)\sin(n\pi y/2) = \sin(\pi x)\sin(\pi y)$. The right side is itself an eigenfunction: $\sin(\pi y) = \sin(2\pi y/2) = Y_2$, so it is $\Phi_{12}$. Matching terms (or computing (17): $A_{mn} = \frac{4}{2}\int_0^1 \sin\pi x\sin m\pi x\,dx\int_0^2 \sin\pi y\sin\frac{n\pi y}{2}\,dy = 2\cdot\frac{\delta_{m1}}{2}\cdot\delta_{n2}$) gives $A_{12} = 1$ and all other $A_{mn} = 0$. With $\lambda_{12}^2 = \pi^2(1 + 1) = 2\pi^2$,
>
> $$
> u(x, y, t) = \sin(\pi x)\sin(\pi y)\,e^{-2\pi^2t} .
> $$
>
> The initial temperature is a single mode, and it simply decays in place.
>
> *Source: 341 HW 13, Problem 2*

^ex-43-3

> [!example] Example §43.4: A Mode with Index Doubling, and an Initial Condition That Is Not a Mode
> Solve $u_t = u_{xx} + u_{yy}$ in $0 < x < 1$, $0 < y < 2$, $t > 0$, with zero edge temperatures, for the initial conditions (a) $u(x, y, 0) = \sin(p\pi x)\sin(q\pi y)$ and (b) $u(x, y, 0) = \sin(p\pi x)\cos(q\pi y)$, where $p$ and $q$ are fixed positive integers.
>
> **Eigenfunctions.** As in Example §43.3, $\Phi_{mn} = \sin(m\pi x)\sin(n\pi y/2)$ with $\lambda_{mn}^2 = \pi^2(m^2 + n^2/4)$, and $u = \sum\sum A_{mn}\Phi_{mn}e^{-\lambda_{mn}^2t}$.
>
> **(a)** Since $\sin(q\pi y) = \sin(2q\pi y/2)$, the initial condition is $\Phi_{p, 2q}$: $A_{p, 2q} = 1$ and all other coefficients are $0$. With $\lambda_{p, 2q}^2 = \pi^2\big(p^2 + (2q)^2/4\big) = \pi^2(p^2 + q^2)$,
>
> $$
> u(x, y, t) = e^{-\pi^2(p^2 + q^2)t}\sin(p\pi x)\sin(q\pi y) .
> $$
>
> The index in $y$ doubles because the side has length $2$: $\sin(q\pi y)$ has $2q$ half-waves on $0 < y < 2$.
>
> **(b)** Now $\cos(q\pi y)$ does not vanish at $y = 0, 2$, and the initial condition is not a finite combination of eigenfunctions. By (17) with $a = 1$, $b = 2$, the $x$-integral $\int_0^1 \sin p\pi x\sin m\pi x\,dx = \frac12\delta_{mp}$ leaves only $m = p$:
>
> $$
> A_{pn} = \frac{4}{2}\cdot\frac12\int_0^2 \cos(q\pi y)\sin\frac{n\pi y}{2}\,dy = \int_0^2 \cos(q\pi y)\sin\frac{n\pi y}{2}\,dy .
> $$
>
> With $\sin A\cos B = \frac12[\sin(A + B) + \sin(A - B)]$ and $\int_0^2 \sin(s\pi y)\,dy = \frac{1 - \cos 2s\pi}{s\pi}$ for $s \ne 0$, where $\cos 2s\pi = \cos(n\pi \pm 2q\pi) = (-1)^n$ for $s = n/2 \pm q$:
>
> $$
> A_{pn} = \frac{1 - (-1)^n}{2\pi}\Big(\frac{1}{n/2 + q} + \frac{1}{n/2 - q}\Big) = \begin{cases} \dfrac{4n}{\pi(n^2 - 4q^2)}, & n \text{ odd}, \\[2mm] 0, & n \text{ even} \end{cases}
> $$
>
> (for $n = 2q$ the term $\sin(A - B)$ is identically $0$, and the formula's value $0$ is still right). So
>
> $$
> u(x, y, t) = \sin(p\pi x)\sum_{n \text{ odd}} \frac{4n}{\pi(n^2 - 4q^2)}\sin\Big(\frac{n\pi y}{2}\Big)e^{-\pi^2(p^2 + n^2/4)t} .
> $$
>
> (The same computation with $q = 0$ gives $4/(n\pi)$ for odd $n$, the familiar sine series of the constant $1$.)
>
> *The practice-final sheet prints the initial condition as $\sin(n\pi x)\cos(m\pi y)$ and writes $b$, $a$ in the boundary conditions for $2$, $1$; the key solves it with $\sin(m\pi y)$, as in (a). Part (b) is the problem as printed.*
>
> *Source: 341 Practice Final, Q10*

^ex-43-4

## The Rectangular Membrane

> [!remark] Remark: The Rectangular Membrane
> The same eigenfunctions solve the membrane problem of [[§41★ Two-Dimensional Wave Equation꞉ Derivation#^ex-41-1|Example §41.1]]. The function
>
> $$
> u_{mn}(x, y, t) = \sin(\mu_mx)\sin(\nu_ny)\cos(\lambda_{mn}ct)
> $$
>
> satisfies $u_{xx} + u_{yy} = u_{tt}/c^2$ on the rectangle with $u = 0$ on the boundary, since $\nabla^2u_{mn} = -\lambda_{mn}^2u_{mn}$ and $\partial^2u_{mn}/\partial t^2 = -\lambda_{mn}^2c^2u_{mn}$ (Powers' Exercise 5.3.10; adding $\sin(\lambda_{mn}ct)$ terms accommodates an initial velocity).
> - **Frequencies.** The mode $(m, n)$ vibrates with angular frequency $\omega_{mn} = c\lambda_{mn} = c\pi\sqrt{m^2/a^2 + n^2/b^2}$. Unlike the overtones of a string, these are not integer multiples of the fundamental $\omega_{11}$: for a square, $\omega_{mn}/\omega_{11} = \sqrt{(m^2 + n^2)/2} = 1,\ 1.581,\ 2,\ 2.236,\ 2.550,\ \ldots$, which is why a drum has a less definite pitch than a string.
> - **Equal frequencies.** If $a = b$, the pairs $(m, n)$ and $(n, m)$ have the same frequency, and occasionally more pairs share one: $1^2 + 7^2 = 5^2 + 5^2 = 50$, so $(1, 7)$, $(7, 1)$ and $(5, 5)$ all vibrate at $5\omega_{11}$.
> - **Nodal lines**, where $u_{mn} = 0$ for all $t$, are the lines $x = ja/m$ ($0 < j < m$) and $y = jb/n$ ($0 < j < n$): for $(1, 2)$ the line $y = b/2$; for $(2, 3)$ the lines $x = a/2$, $y = b/3$, $y = 2b/3$; for $(3, 2)$ the lines $x = a/3$, $x = 2a/3$, $y = b/2$; for $(3, 3)$ the lines $x = a/3$, $2a/3$ and $y = b/3$, $2b/3$ (Exercise 5.3.11). When frequencies coincide, combinations vibrate too, with other nodal lines: on a square, $\phi_{12} + \phi_{21} = 2\sin\frac{\pi x}{a}\sin\frac{\pi y}{a}\big(\cos\frac{\pi y}{a} + \cos\frac{\pi x}{a}\big)$ vanishes along the diagonal $x + y = a$.

^rem-43-3
