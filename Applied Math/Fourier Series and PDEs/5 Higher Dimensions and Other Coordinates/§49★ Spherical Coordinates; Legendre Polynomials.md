---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 5
section: 49
powers: "5.9"
aliases: ["Powers 5.9"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§48★ Some Applications of Bessel Functions]] · ↑ [[· 5 Higher Dimensions and Other Coordinates]] · [[§50★ Some Applications of Legendre Polynomials]] →

*Powers, Section 5.9.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

After Cartesian and cylindrical coordinates, spherical coordinates are the system met most often. Separating the potential equation in a region with axial symmetry produces, after the change of variable $x = \cos\phi$, Legendre's equation $(1 - x^2)y'' - 2xy' + \mu^2y = 0$ on $-1 < x < 1$. It has solutions bounded at both singular points $x = \pm1$ only when $\mu^2 = n(n+1)$, and then one solution is a polynomial: the Legendre polynomial $P_n$. This section develops the facts needed to use them like sines and cosines: orthogonality on $-1 < x < 1$, the norm $2/(2n+1)$, Rodrigues' formula, recurrence relations, Legendre series and their convergence. Physically, $P_n(\cos\phi)$ are the zonal harmonics: the angular parts of axially symmetric potentials, temperatures and waves in and around spheres (electrostatics, gravitation, heat conduction, acoustics, and quantum mechanics in a central field).

## Spherical Coordinates

> [!definition] Definition §49.1: Spherical Coordinates
> The **spherical coordinates** $(\rho, \theta, \phi)$ of a point are related to its Cartesian coordinates by
>
> $$
> x = \rho\sin\phi\cos\theta, \qquad y = \rho\sin\phi\sin\theta, \qquad z = \rho\cos\phi ,
> $$
>
> with $0 \le \rho$, $0 \le \theta < 2\pi$, $0 \le \phi \le \pi$: $\rho$ is the distance from the origin, $\phi$ the angle from the positive $z$-axis (colatitude), and $\theta$ the polar angle of the projection to the $xy$-plane (longitude).
>
> *Powers: 5.9 (text), Figure 11*

^def-49-1

> [!theorem] Proposition §49.1: The Laplacian in Spherical Coordinates
> In spherical coordinates the Laplacian is
>
> $$
> \nabla^2u = \frac{1}{\rho^2}\bigg\{\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial u}{\partial\rho}\Big) + \frac{1}{\sin\phi}\frac{\partial}{\partial\phi}\Big(\sin\phi\,\frac{\partial u}{\partial\phi}\Big) + \frac{1}{\sin^2\phi}\frac{\partial^2u}{\partial\theta^2}\bigg\} .
> $$
>
> *Powers: 5.9 (text)*

^prop-49-1

*Powers omits the proof; see [[§19 The Laplacian in Spherical Coordinates#^thm-19-1|452 Thm. §19.1]] (where the colatitude is called $\theta$ and the longitude $\psi$).*

> [!remark]- Connections
> - The same coordinates, with the same names $\rho, \theta, \phi$, and the volume element $dV = \rho^2\sin\phi\,d\rho\,d\theta\,d\phi$: [[§105 Triple Integrals in Spherical Coordinates#^def-105-1|Calc Def. §105.1]], [[§105 Triple Integrals in Spherical Coordinates#^thm-105-2|Calc Thm. §105.2]]. The factor $\sin\phi$ in the volume element is the weight that appears in the orthogonality of the functions $P_n(\cos\phi)$ (Theorem §49.13).
> - A proof of the formula by the divergence theorem: [[§19 The Laplacian in Spherical Coordinates#^thm-19-1|452 Thm. §19.1]].

From the cases seen so far, the problems we can expect to solve in spherical coordinates reduce to one of the following.
- **Problem 1.** $\nabla^2u = -\lambda^2u$ in $\mathcal{R}$, plus homogeneous boundary conditions. It comes from a heat or wave equation after the time variable is separated out.
- **Problem 2.** $\nabla^2u = 0$ in $\mathcal{R}$, plus homogeneous boundary conditions on facing sides of $\mathcal{R}$, a generalized rectangle in spherical coordinates. It is part of a potential problem.

The complete solution of either problem is very complicated, but some special cases are simple and important. Problem 1 with $u$ a function of $\rho$ only was solved in [[§48★ Some Applications of Bessel Functions#^prop-48-4|Proposition §48.4]]. The next case is Problem 2 when $u$ does not depend on $\theta$:

$$
\frac{1}{\rho^2}\bigg\{\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial u}{\partial\rho}\Big) + \frac{1}{\sin\phi}\frac{\partial}{\partial\phi}\Big(\sin\phi\,\frac{\partial u}{\partial\phi}\Big)\bigg\} = 0, \quad 0 < \rho < c, \quad 0 < \phi < \pi, \qquad (1) \qquad\qquad u(c, \phi) = f(\phi), \quad 0 < \phi < \pi . \qquad (2)
$$

From $u(\rho, \phi) = R(\rho)\Phi(\phi)$ it follows that

$$
\frac{(\rho^2R'(\rho))'}{R(\rho)} + \frac{(\sin\phi\,\Phi'(\phi))'}{\sin\phi\,\Phi(\phi)} = 0 .
$$

Both terms are constant. The second is taken negative, $-\mu^2$, because the boundary condition at $\rho = c$ will have to be satisfied by a linear combination of functions of $\phi$. The separated equations are

$$
(\rho^2R')' - \mu^2R = 0, \quad 0 < \rho < c, \qquad (3) \qquad\qquad (\sin\phi\,\Phi')' + \mu^2\sin\phi\,\Phi = 0, \quad 0 < \phi < \pi . \qquad (4)
$$

Neither equation has a boundary condition. But $\rho = 0$ is a singular point of (3), and $\phi = 0$ and $\phi = \pi$ are singular points of (4): there the coefficient of the highest derivative is zero while another coefficient is not. At each singular point we impose a boundedness condition ([[§4★ Singular Boundary Value Problems#^def-4-2|Definition §4.2]]):

$$
R(0) \text{ bounded}, \qquad \Phi(0) \text{ and } \Phi(\pi) \text{ bounded} .
$$

## Legendre's Equation

> [!theorem] Proposition §49.2: From the Angular Equation to Legendre's Equation
> Under the change of variables $x = \cos\phi$, $\Phi(\phi) = y(x)$, the angular equation (4) becomes
>
> $$
> (1 - x^2)y'' - 2xy' + \mu^2y = 0, \qquad -1 < x < 1 , \qquad (5)
> $$
>
> and the boundedness of $\Phi$ at $\phi = 0$ and $\phi = \pi$ becomes the boundedness of $y$ at $x = 1$ and $x = -1$. (Here $x$ is *not* the Cartesian coordinate.)
>
> *Powers: 5.9, Equation (5)*

^prop-49-2

> [!proof]+ Proof
> By the chain rule, with $dx/d\phi = -\sin\phi$,
>
> $$
> \frac{d\Phi}{d\phi} = -\sin\phi\,\frac{dy}{dx}, \qquad \frac{d}{d\phi}\Big(\sin\phi\,\frac{d\Phi}{d\phi}\Big) = \frac{d}{d\phi}\Big(-\sin^2\phi\,\frac{dy}{dx}\Big) = \sin^3\phi\,\frac{d^2y}{dx^2} - 2\sin\phi\cos\phi\,\frac{dy}{dx} .
> $$
>
> Substituting in (4) and dividing by $\sin\phi$ (which is positive for $0 < \phi < \pi$) gives
>
> $$
> \sin^2\phi\,\frac{d^2y}{dx^2} - 2\cos\phi\,\frac{dy}{dx} + \mu^2y = 0 ,
> $$
>
> and $\sin^2\phi = 1 - x^2$, $\cos\phi = x$ give (5). As $\phi$ runs over $0 < \phi < \pi$, $x = \cos\phi$ runs over $-1 < x < 1$, with $\phi \to 0$ corresponding to $x \to 1$ and $\phi \to \pi$ to $x \to -1$.

^pf-49-2

> [!definition] Definition §49.2: Legendre's Equation
> The equation
>
> $$
> (1 - x^2)y'' - 2xy' + \mu^2y = 0, \qquad -1 < x < 1 ,
> $$
>
> is **Legendre's equation**. Its points $x = \pm1$ are singular points, and in the boundary value problems of this chapter $y$ is required to be bounded at $x = 1$ and at $x = -1$. In self-adjoint form it reads $\big((1 - x^2)y'\big)' + \mu^2y = 0$.
>
> *Powers: 5.9, Equation (5) and the text after (5)*

^def-49-2

Solutions are found by the power series method: assume $y(x) = a_0 + a_1x + \cdots + a_kx^k + \cdots$.

> [!theorem] Proposition §49.3: The Recurrence for the Coefficients
> A power series $y = \sum_k a_kx^k$ satisfies Legendre's equation (5) if and only if
>
> $$
> a_{k+2} = \frac{k(k+1) - \mu^2}{(k+2)(k+1)}\,a_k, \qquad k = 0, 1, 2, \ldots .
> $$
>
> So $a_0$ and $a_1$ are arbitrary; the coefficients with even index are multiples of $a_0$ and those with odd index are multiples of $a_1$, and $y$ is $a_0$ times an even function plus $a_1$ times an odd function. The first coefficients are
>
> $$
> a_2 = \frac{-\mu^2}{2}a_0, \qquad a_4 = \frac{6 - \mu^2}{12}\cdot\frac{-\mu^2}{2}a_0, \qquad a_3 = \frac{2 - \mu^2}{6}a_1, \qquad a_5 = \frac{12 - \mu^2}{20}\cdot\frac{2 - \mu^2}{6}a_1 .
> $$
>
> *Powers: 5.9 (text)*

^prop-49-3

> [!proof]+ Proof
> Write the terms of the differential equation as power series and line up like powers of $x$:
>
> $$
> \begin{aligned}
> y'' &= 2a_2 + 3 \cdot 2a_3x + 4 \cdot 3a_4x^2 + \cdots + (k+2)(k+1)a_{k+2}x^k + \cdots \\
> -x^2y'' &= \hphantom{2a_2 + 3 \cdot 2a_3x} - 2a_2x^2 - \cdots - k(k-1)a_kx^k - \cdots \\
> -2xy' &= \hphantom{2a_2} - 2a_1x - 4a_2x^2 - \cdots - 2ka_kx^k - \cdots \\
> \mu^2y &= \mu^2a_0 + \mu^2a_1x + \mu^2a_2x^2 + \cdots + \mu^2a_kx^k + \cdots
> \end{aligned}
> $$
>
> Adding vertically, the left side is $0$ by the differential equation, so every coefficient of the power series on the right must be $0$: $2a_2 + \mu^2a_0 = 0$, $6a_3 + (\mu^2 - 2)a_1 = 0$, and in general
>
> $$
> (k+2)(k+1)a_{k+2} + \big[\mu^2 - k(k+1)\big]a_k = 0 ,
> $$
>
> since $k(k-1) + 2k = k(k+1)$. The general relation includes the first two cases ($k = 0, 1$). Conversely, coefficients satisfying the recurrence make every coefficient of the sum vanish.

^pf-49-3

> [!theorem] Theorem §49.4: Polynomial Solutions of Legendre's Equation
> **(a)** If $\mu^2 = n(n+1)$ for an integer $n \ge 0$, then Legendre's equation has a polynomial solution of degree exactly $n$, which is even if $n$ is even and odd if $n$ is odd. Every polynomial solution is a constant multiple of it.
>
> **(b)** For other values of $\mu^2$, the even and odd series both diverge at $x = \pm1$, and the solutions they define are unbounded as $x \to 1$ and as $x \to -1$; when $\mu^2 = n(n+1)$, the same holds for the series that does not terminate. Hence Legendre's equation has a solution bounded at both $x = 1$ and $x = -1$ only if $\mu^2$ is one of the numbers $0, 2, 6, \ldots, n(n+1), \ldots$, and then that solution is the polynomial of (a), up to a constant multiple.
>
> *Powers: 5.9 (text)*

^thm-49-4

> [!proof]+ Proof
> Powers gives the termination argument of (a) and illustrates it with $\mu^2 = 3 \cdot 4$. He omits the proof of the divergence and unboundedness in (b) ("it is not difficult to prove"); that part is assumed below, and only the final deduction of (b) is proved.
>
> **Existence.** Let $\mu^2 = n(n+1)$, and take $a_1 = 0$ if $n$ is even, $a_0 = 0$ if $n$ is odd. By [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-3|Proposition §49.3]], $a_{n+2} = \frac{n(n+1) - n(n+1)}{(n+2)(n+1)}a_n = 0$, so all later coefficients of the parity of $n$ vanish, while those of the other parity are $0$ by the choice made. The solution is a polynomial of degree at most $n$, of the parity of $n$. Its coefficient $a_n$ is not $0$ (if the starting coefficient is not $0$), because the factors $k(k+1) - n(n+1)$ with $k < n$ are not $0$.
>
> **Uniqueness.** (Powers asserts this when he calls the polynomial solution $P_n$, and again in Rodrigues' formula below; here is why.) Let $y$ be any polynomial solution, of degree $d$ with leading coefficient $a_d \ne 0$. The coefficient of $x^d$ in $(1 - x^2)y'' - 2xy' + n(n+1)y$ is $\big(-d(d-1) - 2d + n(n+1)\big)a_d = \big(n(n+1) - d(d+1)\big)a_d$, which must be $0$, so $d = n$. If $y$ had a nonzero coefficient of the parity opposite to $n$, then by the recurrence its series of that parity would have to terminate as well, which needs $k(k+1) = n(n+1)$ for some $k$ of that parity, impossible since $k \ne n$. So $y$ has the parity of $n$, its coefficients are determined by the recurrence from $a_0$ (or $a_1$), and it is a multiple of the polynomial constructed above.
>
> **The deduction in (b).** Let $E$ and $O$ be the even and odd series solutions ($a_0 = 1, a_1 = 0$ and $a_0 = 0, a_1 = 1$). When a series does not terminate, $|a_{k+2}/a_k| \to 1$, so it converges for $|x| < 1$; $E$ and $O$ are independent (their values and derivatives at $0$ are $1, 0$ and $0, 1$), so every solution on $-1 < x < 1$ is $y = AE + BO$. Suppose $y$ is bounded near $x = 1$ and near $x = -1$. Then so is $y(-x) = AE(x) - BO(x)$, and hence so are $AE = \frac12\big(y(x) + y(-x)\big)$ and $BO = \frac12\big(y(x) - y(-x)\big)$. If $\mu^2$ is not of the form $n(n+1)$, $E$ and $O$ are both unbounded, so $A = B = 0$. If $\mu^2 = n(n+1)$, the coefficient of the non-terminating series is $0$, and $y$ is a multiple of the polynomial of (a).

^pf-49-4

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-3|§49.3]]

> [!definition] Definition §49.3: Legendre Polynomials
> For $n = 0, 1, 2, \ldots$, the polynomial solution of Legendre's equation with $\mu^2 = n(n+1)$, normalized by the condition $y(1) = 1$, is the **Legendre polynomial** $P_n(x)$. The first five are:
>
> | $n$ | $P_n(x)$ |
> |---|---|
> | 0 | $1$ |
> | 1 | $x$ |
> | 2 | $(3x^2 - 1)/2$ |
> | 3 | $(5x^3 - 3x)/2$ |
> | 4 | $(35x^4 - 30x^2 + 3)/8$ |
>
> By Theorem §49.4, $P_n$ has degree $n$ and $P_n(-x) = (-1)^nP_n(x)$. (That a polynomial solution has $y(1) \ne 0$, so that the normalization is possible, follows from Rodrigues' formula, [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-6|Theorem §49.6]].)
>
> *Powers: 5.9 (text), Table 3*

^def-49-3

> [!example] Example §49.1: Legendre Polynomials from the Recurrence
> Find the polynomial solutions for $\mu^2 = 6$, $12$, $20$ and normalize them.
>
> **$\mu^2 = 12 = 3 \cdot 4$ ($n = 3$).** Here $a_3 = \frac{2 - 12}{6}a_1 = -\frac53a_1$ and $a_5 = \frac{12 - 12}{20}a_3 = 0$, and all subsequent coefficients with odd index are also zero. So one solution of $(1 - x^2)y'' - 2xy' + 12y = 0$ is the polynomial $a_1\big(x - \frac53x^3\big)$. Its value at $x = 1$ is $-\frac23a_1$, so $a_1 = -\frac32$ gives $P_3(x) = -\frac32x + \frac52x^3 = \frac12(5x^3 - 3x)$. The other solution, an even series, is unbounded at $x = \pm1$.
>
> **$\mu^2 = 6$ ($n = 2$).** $a_2 = -3a_0$ and $a_4 = \frac{6 - 6}{12}a_2 = 0$: $y = a_0(1 - 3x^2)$, with $y(1) = -2a_0$. So $P_2 = -\frac12(1 - 3x^2) = \frac12(3x^2 - 1)$.
>
> **$\mu^2 = 20$ ($n = 4$).** $a_2 = -10a_0$, $a_4 = \frac{6 - 20}{12}a_2 = \frac{35}{3}a_0$, $a_6 = \frac{20 - 20}{30}a_4 = 0$: $y = a_0\big(1 - 10x^2 + \frac{35}{3}x^4\big)$, with $y(1) = \frac83a_0$. So $P_4 = \frac38\big(1 - 10x^2 + \frac{35}{3}x^4\big) = \frac18(35x^4 - 30x^2 + 3)$, in agreement with Table 3.
>
> *Powers: 5.9 (text), Table 3*

^ex-49-1

![[m341-49-1.svg]]
*The Legendre polynomials $P_0, \ldots, P_4$ on $-1 \le x \le 1$. All equal $1$ at $x = 1$ and $\pm1$ at $x = -1$, all stay between $-1$ and $1$, and $P_n$ has exactly $n$ zeros in $-1 < x < 1$, like the $n$th eigenfunction of a Sturm–Liouville problem.*

## Orthogonality and Rodrigues' Formula

> [!theorem] Proposition §49.5: Orthogonality of the Legendre Polynomials
> **(a)** $\displaystyle\int_{-1}^{1} P_n(x)P_m(x)\,dx = 0$ for $n \ne m$.
>
> **(b)** Consequently $P_n$ is orthogonal on $-1 < x < 1$ to every polynomial of degree less than $n$.
>
> *Powers: 5.9 (text)*

^prop-49-5

> [!proof]+ Proof
> **(a)** Powers calls this routine, from the self-adjoint form $\big((1 - x^2)y'\big)' + \mu^2y = 0$. Here are the details, the argument of the proof of [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]] for this singular problem ([[§23 Sturm–Liouville Problems#^ex-23-2|Example §23.2]]). Write $s(x) = 1 - x^2$. Then $(sP_n')' = -n(n+1)P_n$ and $(sP_m')' = -m(m+1)P_m$. Multiplying the first by $P_m$ and the second by $P_n$ and subtracting,
>
> $$
> \big[s(P_n'P_m - P_m'P_n)\big]' = \big(m(m+1) - n(n+1)\big)P_nP_m .
> $$
>
> Integrating over $-1 < x < 1$, the left side gives $\big[(1 - x^2)(P_n'P_m - P_m'P_n)\big]_{-1}^{1} = 0$, because $1 - x^2$ vanishes at both ends and the polynomials are bounded there: the singular points need no boundary conditions. For $n \ne m$ (both $\ge 0$), $m(m+1) \ne n(n+1)$, so the integral of $P_nP_m$ is $0$.
>
> **(b)** $P_k$ has degree exactly $k$, so $P_0, \ldots, P_{n-1}$ are a basis of the polynomials of degree less than $n$ (by induction on the degree: subtract a multiple of $P_k$ to remove the $x^k$ term). Any such polynomial is a combination of $P_0, \ldots, P_{n-1}$, each orthogonal to $P_n$ by (a).

^pf-49-5

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Def. §49.3]], [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-4|§49.4]], [[§23 Sturm–Liouville Problems#^thm-23-2|§23.2]] (its argument)

> [!remark]- Connections
> - Gram–Schmidt applied to $1, x, x^2, \ldots$ in the inner product $\int_{-1}^{1} fg\,dx$ produces multiples of $P_0, P_1, P_2, \ldots$, by part (b) and uniqueness of the orthogonalization: [[§20 Orthonormal Bases#^ladr-6-34|LADR 6.34]] (worked to degree $2$), [[§46 Inner Product Spaces#^ex-46-5|235 Ex. §46.5]] (the same polynomials moved to $[0, 1]$), and in Hilbert space [[§24 Orthonormal Sets and Bases#^lem-24-14|556 Lem. §24.14]].
> - The self-adjoint form is what makes the operator $y \mapsto -\big((1 - x^2)y'\big)'$ symmetric; its eigenvectors for different eigenvalues are orthogonal as in [[§22 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]].

> [!theorem] Theorem §49.6: Rodrigues' Formula
> For $n = 0, 1, 2, \ldots$,
>
> $$
> P_n(x) = \frac{1}{n!\,2^n}\frac{d^n}{dx^n}\Big[(x^2 - 1)^n\Big] . \qquad (7)
> $$
>
> *Powers: 5.9, Equation (7); Exercises 5.9.8–5.9.9*

^thm-49-6

> [!proof]+ Proof
> Powers sketches the argument: the right side is a polynomial of degree $n$ that solves Legendre's equation with $\mu^2 = n(n+1)$, hence a multiple of $P_n$. Here are the steps, and the check of the constant.
>
> **A differential equation for $F = (x^2 - 1)^n$** (Exercise 5.9.8). $F' = 2nx(x^2 - 1)^{n-1}$, so $(x^2 - 1)F' = 2nxF$.
>
> **Differentiate $n + 1$ times** (Exercise 5.9.9). By Leibniz's rule ([[§73★ Multiplication and Division of Power Series#^lem-73-1|342 Lem. §73.1]]; only the first two derivatives of $x^2 - 1$ and the first derivative of $x$ are nonzero),
>
> $$
> (x^2 - 1)F^{(n+2)} + (n+1)\,2x\,F^{(n+1)} + \frac{(n+1)n}{2}\,2\,F^{(n)} = 2n\big(xF^{(n+1)} + (n+1)F^{(n)}\big) .
> $$
>
> With $y = F^{(n)}$ this is $(x^2 - 1)y'' + 2xy' - n(n+1)y = 0$, which is Legendre's equation (5) with $\mu^2 = n(n+1)$, multiplied by $-1$.
>
> **Degree.** $F$ has degree $2n$ with leading term $x^{2n}$, so $y = F^{(n)}$ is a polynomial of degree $n$, with leading coefficient $(2n)!/n! \ne 0$. By [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-4|Theorem §49.4]](a), $y$ is a constant multiple of the polynomial solution.
>
> **The constant.** Write $F = (x - 1)^n(x + 1)^n$. In the Leibniz expansion of $F^{(n)}$, every term in which $(x - 1)^n$ is differentiated fewer than $n$ times still contains a factor $x - 1$ and vanishes at $x = 1$. The remaining term is $n!\,(x + 1)^n$, so $y(1) = n!\,2^n$. Hence $y/(n!\,2^n)$ is the polynomial solution with value $1$ at $x = 1$, which is $P_n$. (In particular the polynomial solutions do not vanish at $x = 1$, as used in Definition §49.3.)

^pf-49-6

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-4|§49.4]], [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Def. §49.3]], [[§73★ Multiplication and Division of Power Series#^lem-73-1|342 Lem. §73.1]] (Leibniz's rule)

> [!theorem] Proposition §49.7: Recurrence Relations
> For $n \ge 1$,
>
> $$
> (2n+1)P_n(x) = P_{n+1}'(x) - P_{n-1}'(x) , \qquad (8)
> $$
>
> $$
> (n+1)P_{n+1}(x) + nP_{n-1}(x) = (2n+1)xP_n(x) , \qquad (9)
> $$
>
> and for $n \ge 0$,
>
> $$
> P_{n+1}'(x) = (n+1)P_n(x) + xP_n'(x), \qquad\text{in particular}\qquad P_n'(0) = nP_{n-1}(0) \ \ (n \ge 1) . \qquad (16)
> $$
>
> *Powers: 5.9, Equations (8), (9), (16); Exercise 5.9.7*

^prop-49-7

> [!proof]- Proof
> Powers states (8) and (9) without proof ("through Rodrigues' formula or otherwise, it is possible to prove"); here they are proved through Rodrigues' formula. The third relation is then derived from (8) and (9), as Powers says and as Exercise 5.9.7 outlines.
>
> Write $D = d/dx$ and $F_n = (x^2 - 1)^n$, so that $P_n = D^nF_n/(2^nn!)$ by [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-6|Theorem §49.6]]. Let $n \ge 1$. Note that $DF_{n+1} = 2(n+1)xF_n$.
>
> **(8).** Differentiate once more: $D^2F_{n+1} = 2(n+1)\big(F_n + xDF_n\big) = 2(n+1)\big(F_n + 2nx^2F_{n-1}\big)$. Since $x^2 = (x^2 - 1) + 1$, $x^2F_{n-1} = F_n + F_{n-1}$, so
>
> $$
> D^2F_{n+1} = 2(n+1)\big((2n+1)F_n + 2nF_{n-1}\big) .
> $$
>
> Apply $D^n$ and divide by $2^{n+1}(n+1)!$:
>
> $$
> P_{n+1}' = \frac{(2n+1)D^nF_n}{2^nn!} + \frac{2n\,D^nF_{n-1}}{2^nn!} = (2n+1)P_n + \frac{D^n F_{n-1}}{2^{n-1}(n-1)!} = (2n+1)P_n + P_{n-1}' .
> $$
>
> **(9).** Apply $D^n$ to $DF_{n+1} = 2(n+1)xF_n$ and use Leibniz's rule, $D^n(xF_n) = xD^nF_n + nD^{n-1}F_n$:
>
> $$
> 2^{n+1}(n+1)!\,P_{n+1} = 2(n+1)\big(2^nn!\,xP_n + nD^{n-1}F_n\big), \qquad\text{so}\qquad P_{n+1} = xP_n + n\,G, \quad G = \frac{D^{n-1}F_n}{2^nn!} .
> $$
>
> Now $G' = P_n$. Also $G(\pm1) = 0$: in the Leibniz expansion of $D^{n-1}\big[(x - 1)^n(x + 1)^n\big]$ each term differentiates the two factors at most $n - 1$ times in total, so it keeps a factor $x - 1$ and a factor $x + 1$. By (8), $H = (P_{n+1} - P_{n-1})/(2n+1)$ also has $H' = P_n$, and $H(1) = 0$ since every $P_k(1) = 1$. Two antiderivatives of $P_n$ that agree at $x = 1$ are equal, so $G = H$ and
>
> $$
> P_{n+1} = xP_n + \frac{n}{2n+1}\big(P_{n+1} - P_{n-1}\big), \qquad\text{that is,}\qquad (n+1)P_{n+1} + nP_{n-1} = (2n+1)xP_n .
> $$
>
> **The relation $P_{n+1}' = (n+1)P_n + xP_n'$** (Exercise 5.9.7). Differentiate (9): $(n+1)P_{n+1}' + nP_{n-1}' = (2n+1)P_n + (2n+1)xP_n'$. Eliminate $P_{n-1}' = P_{n+1}' - (2n+1)P_n$ by (8):
>
> $$
> (2n+1)P_{n+1}' - n(2n+1)P_n = (2n+1)P_n + (2n+1)xP_n' ,
> $$
>
> and divide by $2n + 1$: $P_{n+1}' = (n+1)P_n + xP_n'$ for $n \ge 1$. For $n = 0$ it reads $P_1' = P_0$, which is true. Replacing $n$ by $n - 1$ and putting $x = 0$ gives $P_n'(0) = nP_{n-1}(0)$ for $n \ge 1$, which is (16).

^pf-49-7

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-6|§49.6]], [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Def. §49.3]]

> [!theorem] Proposition §49.8: The Norm of Pₙ
> For $n = 0, 1, 2, \ldots$,
>
> $$
> \int_{-1}^{1} P_n^2(x)\,dx = \frac{2}{2n+1} . \qquad (6)
> $$
>
> *Powers: 5.9, Equation (6); Exercise 5.9.10*

^prop-49-8

> [!proof]+ Proof
> Powers says "by direct calculation" and outlines this route in Exercise 5.9.10. For $n = 0$ and $1$: $\int_{-1}^{1} 1\,dx = 2$ and $\int_{-1}^{1} x^2\,dx = \frac23$. Now let $n \ge 1$; we compute $\int P_{n+1}^2$.
>
> **(a)** Multiply (9) by $P_{n+1}$ and integrate from $-1$ to $1$. By orthogonality ([[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-5|Proposition §49.5]]) the term with $P_{n-1}P_{n+1}$ drops out:
>
> $$
> (n+1)\int_{-1}^{1} P_{n+1}^2\,dx = (2n+1)\int_{-1}^{1} xP_nP_{n+1}\,dx .
> $$
>
> **(b)** Replace $(2n+1)P_n$ by $P_{n+1}' - P_{n-1}'$, using (8): the right side becomes $\int_{-1}^{1} x\big(P_{n+1}' - P_{n-1}'\big)P_{n+1}\,dx$.
>
> **(c)** $xP_{n-1}'$ is a polynomial of degree at most $n - 1$, so $\int_{-1}^{1} xP_{n-1}'P_{n+1}\,dx = 0$ by Proposition §49.5(b).
>
> **(d)** What remains is integrated by parts, with $P_{n+1}'P_{n+1} = \frac12\big(P_{n+1}^2\big)'$ and $P_{n+1}^2(\pm1) = 1$:
>
> $$
> \int_{-1}^{1} xP_{n+1}'P_{n+1}\,dx = \frac12\Big[xP_{n+1}^2\Big]_{-1}^{1} - \frac12\int_{-1}^{1} P_{n+1}^2\,dx = 1 - \frac12\int_{-1}^{1} P_{n+1}^2\,dx .
> $$
>
> So $(n+1)\int P_{n+1}^2 = 1 - \frac12\int P_{n+1}^2$, that is, $\int_{-1}^{1} P_{n+1}^2\,dx = \dfrac{1}{n + \frac32} = \dfrac{2}{2(n+1) + 1}$.

^pf-49-8

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Def. §49.3]], [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-5|§49.5]], [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-7|§49.7]]

## Legendre Series

To use Legendre polynomials in boundary value problems, a given function $f(x)$ must be expressed in the form $f(x) = \sum_{n=0}^{\infty} b_nP_n(x)$, $-1 < x < 1$. Multiplying by $P_m$ and integrating, orthogonality and the norm (6) leave $\int_{-1}^{1} fP_m\,dx = b_m\frac{2}{2m+1}$.

> [!definition] Definition §49.4: Legendre Series
> The **Legendre series** of a function $f$ on $-1 < x < 1$ is
>
> $$
> \sum_{n=0}^{\infty} b_nP_n(x), \qquad b_n = \frac{2n+1}{2}\int_{-1}^{1} f(x)P_n(x)\,dx . \qquad (10)
> $$
>
> *Powers: 5.9, Equation (10)*

^def-49-4

> [!theorem] Theorem §49.9: Convergence of Legendre Series
> If $f(x)$ is sectionally smooth on the interval $-1 < x < 1$, then at every point of that interval the Legendre series of $f$ converges, and
>
> $$
> \sum_{n=0}^{\infty} b_nP_n(x) = \frac{f(x+) + f(x-)}{2} .
> $$
>
> *Powers: 5.9, Theorem*

^thm-49-9

*Powers omits the proof.* It is the analogue of the Fourier convergence theorem, [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1]].

> [!remark]- Connections
> - Convergence in the mean (in $L^2[-1, 1]$) has a short proof from results in the vault. The normalized polynomials $\sqrt{(2n+1)/2}\,P_n$ are an orthonormal set (Propositions §49.5 and §49.8) whose span is all polynomials. Polynomials are dense in $C[-1, 1]$ for the maximum norm by Weierstrass's approximation theorem ([[§27 Weierstrass's Approximation Theorem (Not Covered)|451 §27]], a heading only: the theorem was not covered), and continuous functions are dense in $L^2[-1, 1]$ ([[§19 Normed Linear Spaces and Lᵖ Spaces#^thm-19-19|551 Thm. §19.19]](iii)). So the set is complete, hence an orthonormal basis with Parseval's equality: [[§24 Orthonormal Sets and Bases#^thm-24-8|556 Thm. §24.8]]. The pointwise statement of the theorem needs more.

> [!theorem] Proposition §49.10: Legendre Series of Odd, Even and Half-Range Functions
> If $f$ is odd on $-1 < x < 1$, only the odd-indexed coefficients $b_n$ can be nonzero; if $f$ is even, only the even-indexed ones. Consequently a function $f$ given on $0 < x < 1$ is represented there both by
>
> $$
> f(x) = \sum_{n\ \mathrm{even}} b_nP_n(x), \qquad b_n = (2n+1)\int_0^1 f(x)P_n(x)\,dx \quad (n \text{ even}), \qquad (11)
> $$
>
> $$
> f(x) = \sum_{n\ \mathrm{odd}} b_nP_n(x), \qquad b_n = (2n+1)\int_0^1 f(x)P_n(x)\,dx \quad (n \text{ odd}), \qquad (12)
> $$
>
> the series of its even and of its odd extension.
>
> *Powers: 5.9, Equations (11)–(12)*

^prop-49-10

> [!proof]+ Proof
> $P_n$ is even or odd with $n$ ([[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Definition §49.3]]). If $f$ is odd and $n$ is even, $fP_n$ is odd and its integral over $-1 < x < 1$ is $0$; similarly if $f$ is even and $n$ is odd. If $f$ and $P_n$ have the same parity, $fP_n$ is even, and $\int_{-1}^{1} fP_n = 2\int_0^1 fP_n$, which turns (10) into (11) or (12). Applied to the even or odd extension of $f$, [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-9|Theorem §49.9]] shows that each series represents $f$ on $0 < x < 1$.

^pf-49-10

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Def. §49.3]], [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-4|Def. §49.4]], [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-9|§49.9]]

Because the $P_n$ are polynomials, the integral (10) for any specific coefficient can be done in closed form for many functions $f$. Getting $b_n$ as a function of $n$ is not so easy, but some elementary integrals follow from the differential equation $\big((1 - x^2)P_n'\big)' + n(n+1)P_n = 0$.

> [!theorem] Proposition §49.11: Integrals of Pₙ and xPₙ
> For $n \ne 0$, respectively $n \ne 1$,
>
> $$
> \int P_n(x)\,dx = \frac{-(1 - x^2)}{n(n+1)}P_n'(x), \qquad (13) \qquad\qquad \int xP_n(x)\,dx = \frac{1 - x^2}{(n+2)(n-1)}\big(P_n(x) - xP_n'(x)\big) . \qquad (14)
> $$
>
> *Powers: 5.9, Summary box, Equations (13)–(14)*

^prop-49-11

> [!proof]+ Proof
> **(13).** Separate the two terms of the differential equation and integrate:
>
> $$
> n(n+1)\int P_n\,dx = \int -\big((1 - x^2)P_n'\big)'\,dx = -(1 - x^2)P_n'(x) ,
> $$
>
> and divide by $n(n+1) \ne 0$.
>
> **(14).** Multiply the differential equation by $x$, separate terms and integrate by parts twice:
>
> $$
> \begin{aligned}
> n(n+1)\int xP_n\,dx &= \int -x\big((1 - x^2)P_n'\big)'\,dx = -x(1 - x^2)P_n' + \int (1 - x^2)P_n'\,dx \\
> &= -x(1 - x^2)P_n' + (1 - x^2)P_n - \int (-2x)P_n\,dx .
> \end{aligned}
> $$
>
> Move the last term to the left: $\big(n(n+1) - 2\big)\int xP_n\,dx = (1 - x^2)\big(P_n - xP_n'\big)$, and $n(n+1) - 2 = (n+2)(n-1)$, which is not $0$ for $n \ne 1$. (For $n = 1$ the integration is done directly.)

^pf-49-11

These formulas are useful if $P_n(x)$ and $P_n'(x)$ can be evaluated easily, and the recurrence relations do this, in particular at $x = 0$.

> [!theorem] Proposition §49.12: Values at the Origin
> $$
> P_n(0) = (-1)^{n/2}\frac{1 \cdot 3 \cdots (n-1)}{2 \cdot 4 \cdots n}, \quad n = 2, 4, 6, \ldots; \qquad P_n(0) = 0, \quad n = 1, 3, 5, \ldots ; \qquad (15)
> $$
>
> and $P_n'(0) = nP_{n-1}(0)$ (16). So $P_2(0) = -\frac12$, $P_4(0) = \frac{1 \cdot 3}{2 \cdot 4} = \frac38$, $P_6(0) = -\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6} = -\frac{5}{16}$.
>
> *Powers: 5.9, Equations (15)–(16)*

^prop-49-12

> [!proof]+ Proof
> $P_n(0) = 0$ for odd $n$ because the odd-indexed Legendre polynomials are odd functions. For odd $n$, (9) at $x = 0$ gives $(n+1)P_{n+1}(0) + nP_{n-1}(0) = 0$, that is,
>
> $$
> P_{n+1}(0) = -\frac{n}{n+1}P_{n-1}(0) .
> $$
>
> Starting from $P_0(0) = 1$, successively $P_2(0) = -\frac12$, $P_4(0) = -\frac34P_2(0) = \frac{1 \cdot 3}{2 \cdot 4}$, $P_6(0) = -\frac56P_4(0) = -\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}$, and by induction (15): each step multiplies by $-\frac{n}{n+1}$ with $n$ odd. Formula (16) is part of [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-7|Proposition §49.7]].

^pf-49-12

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-7|§49.7]]

> [!example] Example §49.2: The Legendre Series of a Step Function
> Find the Legendre series of
>
> $$
> f(x) = \begin{cases} -1, & -1 < x < 0, \\ \phantom{-}1, & 0 < x < 1. \end{cases}
> $$
>
> $f$ is odd, so only odd-indexed polynomials appear, and by (12), (13) and (16), for odd $n$,
>
> $$
> \begin{aligned}
> b_n &= (2n+1)\int_0^1 P_n(x)\,dx = -\frac{2n+1}{n(n+1)}\Big[(1 - x^2)P_n'(x)\Big]_0^1 = \frac{2n+1}{n(n+1)}P_n'(0) = \frac{2n+1}{n+1}P_{n-1}(0) \\
> &= (-1)^{(n-1)/2}\,\frac{1 \cdot 3 \cdot 5 \cdots (n-2)}{2 \cdot 4 \cdot 6 \cdots (n-1)}\cdot\frac{2n+1}{n+1} \qquad (n = 3, 5, 7, \ldots),
> \end{aligned}
> $$
>
> using (15) for the even index $n - 1$. Separately, $b_1 = 3\int_0^1 x\,dx = \frac32$ (the general formula also gives this, with $P_0(0) = 1$). So $b_3 = \frac74\cdot\big(-\frac12\big) = -\frac78$, $b_5 = \frac{11}{6}\cdot\frac38 = \frac{11}{16}$, $b_7 = -\frac{75}{128}$, $b_9 = \frac{133}{256}$, and because $f$ is sectionally smooth, by [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-9|Theorem §49.9]]
>
> $$
> f(x) = \frac32P_1(x) - \frac78P_3(x) + \frac{11}{16}P_5(x) - \cdots, \qquad -1 < x < 1,\ x \ne 0 ,
> $$
>
> and the series is $0$ at $x = 0$.
>
> *Powers: 5.9, Example*

^ex-49-2

> [!example] Example §49.3: The Legendre Series of |x|
> Find the Legendre series of $f(x) = |x|$, $-1 < x < 1$.
>
> $f$ is even, so by (11) $b_n = (2n+1)\int_0^1 xP_n(x)\,dx$ for even $n$. For $n = 0$, $b_0 = \int_0^1 x\,dx = \frac12$. For even $n \ge 2$, (14) gives
>
> $$
> \int_0^1 xP_n(x)\,dx = \bigg[\frac{(1 - x^2)\big(P_n - xP_n'\big)}{(n+2)(n-1)}\bigg]_0^1 = -\frac{P_n(0)}{(n+2)(n-1)}, \qquad b_n = -\frac{(2n+1)P_n(0)}{(n+2)(n-1)} .
> $$
>
> With (15): $b_2 = -\frac{5 \cdot (-1/2)}{4 \cdot 1} = \frac58$, $b_4 = -\frac{9 \cdot (3/8)}{6 \cdot 3} = -\frac{3}{16}$, $b_6 = -\frac{13 \cdot (-5/16)}{8 \cdot 5} = \frac{13}{128}$. So
>
> $$
> |x| = \frac12 + \frac58P_2(x) - \frac{3}{16}P_4(x) + \frac{13}{128}P_6(x) - \cdots, \qquad -1 < x < 1 .
> $$
>
> $|x|$ is continuous, with a corner at $0$, and the convergence is much faster than for the step function: the partial sum through $P_6$ is within $0.086$ of $|x|$ everywhere on $-1 \le x \le 1$, the worst place being the corner $x = 0$.
>
> *Powers: 5.9, Figure 13(b) (Exercise 5.9.11)*

^ex-49-3

![[m341-49-2.svg]]
*Partial sums of Legendre series, computed from Examples §49.2 and §49.3. (a) The step function and its partial sum through $P_9$: it oscillates about $\pm1$, with the largest errors near the jump and near the endpoints, as a Fourier series does. (b) $|x|$ and its partial sum through $P_6$, already close except near the corner at $x = 0$.*

## Zonal Harmonics

> [!theorem] Theorem §49.13: The Legendre Eigenvalue Problems
> The solutions of the eigenvalue problem
>
> $$
> \big((1 - x^2)y'\big)' + \mu^2y = 0, \quad -1 < x < 1, \qquad y(x) \text{ bounded at } x = -1 \text{ and at } x = 1 ,
> $$
>
> are $y(x) = P_n(x)$, $\mu_n^2 = n(n+1)$, $n = 0, 1, 2, \ldots$. The solutions of the eigenvalue problem
>
> $$
> \big(\sin\phi\,\Phi'\big)' + \mu^2\sin\phi\,\Phi = 0, \quad 0 < \phi < \pi, \qquad \Phi(\phi) \text{ bounded at } \phi = 0 \text{ and at } \phi = \pi ,
> $$
>
> are $\Phi(\phi) = P_n(\cos\phi)$, $\mu_n^2 = n(n+1)$, $n = 0, 1, 2, \ldots$. The eigenfunctions $\Phi_n$ are orthogonal with weight $\sin\phi$: $\int_0^{\pi}\Phi_n(\phi)\Phi_m(\phi)\sin\phi\,d\phi = 0$ for $n \ne m$.
>
> *Powers: 5.9, Summary box; Exercise 5.9.6*

^thm-49-13

> [!proof]+ Proof
> The first statement is [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-4|Theorem §49.4]] with the normalization of [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Definition §49.3]]; it rests on the unboundedness assumed in part (b) of that theorem, which Powers does not prove. The second follows by the change of variables $x = \cos\phi$ of [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-2|Proposition §49.2]]. For the orthogonality, the same substitution, with $dx = -\sin\phi\,d\phi$, gives
>
> $$
> \int_0^{\pi} P_n(\cos\phi)P_m(\cos\phi)\sin\phi\,d\phi = \int_{-1}^{1} P_n(x)P_m(x)\,dx = 0 \qquad (n \ne m)
> $$
>
> by [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-5|Proposition §49.5]].

^pf-49-13

*Uses:* [[§49★ Spherical Coordinates; Legendre Polynomials#^thm-49-4|§49.4]], [[§49★ Spherical Coordinates; Legendre Polynomials#^def-49-3|Def. §49.3]], [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-2|§49.2]], [[§49★ Spherical Coordinates; Legendre Polynomials#^prop-49-5|§49.5]]

> [!definition] Definition §49.5: Zonal Harmonics
> The functions $P_n(\cos\phi)$ on the sphere are called **zonal harmonics**, because their nodal lines, the loci of $P_n(\cos\phi) = 0$, are parallels $\phi =$ const that divide the sphere into zones. $P_n(\cos\phi)$ has $n$ nodal parallels, at the colatitudes $\phi = \arccos x_k$ of the $n$ zeros $x_k$ of $P_n$, and the zones between them are alternately positive and negative.
>
> *Powers: 5.9 (text), Figure 14*

^def-49-5

For example, $P_1(\cos\phi) = \cos\phi$ has the equator as its only nodal line; $P_2(\cos\phi) = \frac12(3\cos^2\phi - 1)$ vanishes on the two parallels $\cos\phi = \pm1/\sqrt3$, $\phi \approx 54.7°$ and $125.3°$, so it is positive on two polar caps and negative on the equatorial belt.
