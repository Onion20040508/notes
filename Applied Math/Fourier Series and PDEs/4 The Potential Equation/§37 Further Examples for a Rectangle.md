---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: 37
powers: "4.3"
aliases: ["Powers 4.3"]
tags: [fourier-series-and-pdes, math341]
---
← [[§36 Potential in a Rectangle]] · ↑ [[· 4 The Potential Equation]] · [[§38 Potential in Unbounded Regions]] →

*Powers, Section 4.3 · MAT 341 lectures 11.19–11.21 · HW 12.*

Separation of variables in a rectangle is not limited to Dirichlet problems. Insulated sides (zero normal derivative) or mixed conditions on a pair of facing sides lead to the other eigenvalue problems of Chapter 2, with cosine eigenfunctions, a constant eigenfunction for the eigenvalue $0$, or the eigenvalues $(n - \frac12)\pi/a$. The splitting principle of [[§36 Potential in a Rectangle#^thm-36-2|§36]] still applies: zero the conditions on two facing sides and copy the rest. Harmonic polynomials can absorb simple boundary data and save a series. The section ends with the Poisson equation $\nabla^2u = -H$, the potential equation with a source: the deflection of a loaded membrane, the temperature in a current-carrying wire, the stress function of a twisted bar.

## Insulated Sides

> [!example] Example §37.1: A Conductor with Insulated Sides
> The unknown $u$ might be a voltage in a rectangular conductor whose left and right sides are electrically insulated:
>
> $$
> \begin{aligned}
> &\frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0, && 0 < x < a, \quad 0 < y < b, \\
> &\frac{\partial u}{\partial x}(0, y) = 0, \quad \frac{\partial u}{\partial x}(a, y) = 0, && 0 < y < b, \\
> &u(x, 0) = 0, \quad u(x, b) = V_0x/a, && 0 < x < a .
> \end{aligned}
> $$
>
> **Separation.** The conditions are homogeneous on the facing sides $x = 0$ and $x = a$. A product $u = X(x)Y(y)$ gives, as expected, $X''/X = -Y''/Y =$ constant, with $X'(0) = 0$, $X'(a) = 0$. With the constant $-\lambda^2$ this is the eigenvalue problem of the insulated bar ([[§20 Example꞉ Insulated Bar#^thm-20-1|Theorem §20.1]]):
>
> $$
> X_0(x) = 1, \quad \lambda_0 = 0; \qquad X_n(x) = \cos(\lambda_nx), \quad \lambda_n = \frac{n\pi}{a}, \quad n = 1, 2, \ldots
> $$
>
> For the factor $Y$ the equation is $Y_0'' = 0$ or $Y_n'' - \lambda_n^2Y_n = 0$, with solutions
>
> $$
> Y_0(y) = a_0 + b_0y, \qquad Y_n(y) = a_n\cosh(\lambda_ny) + b_n\sinh(\lambda_ny) .
> $$
>
> The eigenvalue $0$ contributes a linear function of $y$, not just a constant. By superposition,
>
> $$
> u(x, y) = a_0 + b_0y + \sum_{n=1}^{\infty}\big(a_n\cosh(\lambda_ny) + b_n\sinh(\lambda_ny)\big)\cos(\lambda_nx) .
> $$
>
> **The bottom.** At $y = 0$: $a_0 + \sum a_n\cos(\lambda_nx) = 0$ for $0 < x < a$, so all the $a$'s are $0$.
>
> **The top.** At $y = b$:
>
> $$
> b_0b + \sum_{n=1}^{\infty}\big(b_n\sinh(\lambda_nb)\big)\cos(\lambda_nx) = \frac{V_0x}{a}, \qquad 0 < x < a ,
> $$
>
> a slightly disguised cosine series ([[§7 Arbitrary Period and Half-Range Expansions#^def-7-4|Definition §7.4]]). Its coefficients are
>
> $$
> b_0b = \frac1a\int_0^a V_0\frac xa\,dx = \frac{V_0}{2}, \qquad b_n\sinh(\lambda_nb) = \frac2a\int_0^a V_0\frac xa\cos(\lambda_nx)\,dx = \frac{2V_0\big((-1)^n - 1\big)}{n^2\pi^2} ,
> $$
>
> the last by parts: $\int_0^a x\cos(n\pi x/a)\,dx = \big[\frac{ax}{n\pi}\sin\frac{n\pi x}{a}\big]_0^a - \frac{a}{n\pi}\int_0^a\sin\frac{n\pi x}{a}\,dx = \frac{a^2}{n^2\pi^2}\big((-1)^n - 1\big)$. So $b_n = 0$ for even $n$ and $b_n = -4V_0/(n^2\pi^2\sinh(\lambda_nb))$ for odd $n$:
>
> $$
> u(x, y) = \frac{V_0}{2}\,\frac yb - \frac{4V_0}{\pi^2}\sum_{n \text{ odd}}\frac{\sinh(n\pi y/a)}{n^2\sinh(n\pi b/a)}\cos\Big(\frac{n\pi x}{a}\Big) .
> $$
>
> The term $V_0y/(2b)$ is the uniform field that carries the average $V_0/2$ of the top voltage; the series corrects for the variation of the top voltage along $x$ and dies out away from the top edge.
>
> *Powers: 4.3, Example 1; Exercise 4.3.3*

^ex-37-1

> [!example] Example §37.2: General Data on Top and Bottom, Insulated Sides
> Solve
>
> $$
> u_{xx} + u_{yy} = 0 \ \ (0 < x < a, \ 0 < y < b); \qquad u(x, 0) = f_1(x), \ \ u(x, b) = f_2(x); \qquad u_x(0, y) = 0, \ \ u_x(a, y) = 0 .
> $$
>
> **(a) Separation.** With $u = X(x)Y(y)$, $X''/X = -Y''/Y = p$: $X'' = pX$, $Y'' = -pY$, and the insulated sides give $X'(0) = 0$, $X'(a) = 0$.
>
> **(b) Basic solutions.** If $p > 0$, $X = Ae^{\sqrt p x} + Be^{-\sqrt p x}$, $X'(0) = \sqrt p(A - B) = 0$ gives $A = B$, and then $X'(a) = 2A\sqrt p\sinh(\sqrt p a) = 0$ gives $A = 0$. If $p = 0$ (the case to be careful with), $X = A + Bx$, $X'(0) = B = 0$, and $X =$ constant is a nonzero solution; then $Y'' = 0$, $Y = a_0y + b_0$. If $p = -\lambda^2 < 0$, $X = A\sin(\lambda x) + B\cos(\lambda x)$, $X'(0) = A\lambda = 0$, and $X'(a) = -B\lambda\sin(\lambda a) = 0$ gives $\lambda = n\pi/a$. So the basic solutions are
>
> $$
> u_0(x, y) = a_0y + b_0, \qquad u_n(x, y) = \cos\Big(\frac{n\pi x}{a}\Big)\Big(a_n\sinh\Big(\frac{n\pi y}{a}\Big) + b_n\cosh\Big(\frac{n\pi y}{a}\Big)\Big), \quad n = 1, 2, \ldots
> $$
>
> **(c) Coefficients.** With $u = u_0 + \sum_{n \ge 1}u_n$, the bottom condition is the cosine series $b_0 + \sum b_n\cos(n\pi x/a) = f_1(x)$, and the top condition is the cosine series $(a_0b + b_0) + \sum\big(a_n\sinh(n\pi b/a) + b_n\cosh(n\pi b/a)\big)\cos(n\pi x/a) = f_2(x)$. Hence
>
> $$
> b_0 = \frac1a\int_0^a f_1(x)\,dx, \qquad b_n = \frac2a\int_0^a f_1(x)\cos\Big(\frac{n\pi x}{a}\Big)dx ,
> $$
>
> $$
> a_0 = \frac{1}{ab}\int_0^a f_2(x)\,dx - \frac{b_0}{b}, \qquad a_n = \frac{2}{a\sinh(n\pi b/a)}\int_0^a f_2(x)\cos\Big(\frac{n\pi x}{a}\Big)dx - b_n\coth\Big(\frac{n\pi b}{a}\Big) .
> $$
>
> Example §37.1 is the case $f_1 = 0$, $f_2 = V_0x/a$.
>
> *Source: 341 HW 12, Problem 2*

^ex-37-2

> [!example] Example §37.3: Fixed Temperature Below, Prescribed Flux Above
> Solve
>
> $$
> \begin{aligned}
> &u_{xx} + u_{yy} = 0, && 0 < x < a, \quad 0 < y < b, \\
> &u_x(0, y) = 0, \quad u_x(a, y) = 0, && 0 < y < b, \\
> &u(x, 0) = T, \quad u_y(x, b) = f(x) = \begin{cases} 1, & 0 < x < a/2, \\ 0, & a/2 < x < a. \end{cases}
> \end{aligned}
> $$
>
> As a heat problem: a plate with insulated sides, its bottom held at temperature $T$, and heat flowing in through the left half of the top edge at a constant rate.
>
> **Basic solutions.** The sides are as in Example §37.2, so
>
> $$
> u_0 = A_0y + B_0, \qquad u_n = \cos\Big(\frac{n\pi x}{a}\Big)\Big(A_n\sinh\Big(\frac{n\pi y}{a}\Big) + B_n\cosh\Big(\frac{n\pi y}{a}\Big)\Big) .
> $$
>
> **The bottom.** $T = B_0 + \sum B_n\cos(n\pi x/a)$ gives $B_0 = T$ and $B_n = 0$ for $n \ge 1$.
>
> **The top.** Now the condition is on $u_y$:
>
> $$
> u_y(x, b) = A_0 + \sum_{n=1}^{\infty}\frac{n\pi}{a}\cosh\Big(\frac{n\pi b}{a}\Big)A_n\cos\Big(\frac{n\pi x}{a}\Big) = f(x) ,
> $$
>
> a cosine series for $f$. So
>
> $$
> A_0 = \frac1a\int_0^{a/2}1\,dx = \frac12, \qquad \frac{n\pi}{a}\cosh\Big(\frac{n\pi b}{a}\Big)A_n = \frac2a\int_0^{a/2}\cos\Big(\frac{n\pi x}{a}\Big)dx = \frac{2\sin(n\pi/2)}{n\pi} ,
> $$
>
> $$
> A_n = \frac{2a}{(n\pi)^2}\,\frac{\sin(n\pi/2)}{\cosh(n\pi b/a)} .
> $$
>
> **Solution.**
>
> $$
> u(x, y) = T + \frac12y + \sum_{n=1}^{\infty}\frac{2a\sin(n\pi/2)}{(n\pi)^2\cosh(n\pi b/a)}\cos\Big(\frac{n\pi x}{a}\Big)\sinh\Big(\frac{n\pi y}{a}\Big) .
> $$
>
> The average inflow $\frac12$ through the top is carried straight down to the bottom by the linear term $\frac12y$; the series redistributes it sideways.
>
> *In the lecture's boxed answer the last factor is $\cosh(n\pi y/a)$; it must be $\sinh(n\pi y/a)$, since $B_n = 0$ (with $\cosh$ the condition $u(x, 0) = T$ fails).*
>
> *Source: 341 lecture 11.21*

^ex-37-3

## Splitting the Problem

The success of separation of variables depends on having homogeneous boundary conditions at the ends of one of the intervals involved. A Dirichlet problem is split, if necessary, to achieve this ([[§36 Potential in a Rectangle#^thm-36-2|Theorem §36.2]]); the same splitting technique applies when boundary conditions of other kinds are used.

> [!remark] Remark: Method — Splitting a Rectangle Problem
> To solve the potential equation in a rectangle with nonhomogeneous conditions on adjacent sides:
> 1. Write $u = u_1 + u_2$. For $u_1$, **zero the conditions on two facing sides** and **copy the rest**; for $u_2$, zero the conditions on the other pair of facing sides and copy the rest. A condition is "zeroed" by keeping its type and replacing its data by $0$: $u = g$ becomes $u = 0$, $\partial u/\partial n = g$ becomes $\partial u/\partial n = 0$.
> 2. Check the sum: the potential equation is linear and homogeneous, so $u_1 + u_2$ satisfies it (Principle of Superposition); derivatives of a sum are sums of derivatives, so on each side the conditions of $u_1$ and $u_2$ add up to the original condition.
> 3. Solve each part by separation of variables; the zeroed pair of sides gives the eigenvalue problem.
> 4. Before splitting, see whether a harmonic polynomial ([[§35 Potential Equation#^prop-35-2|Proposition §35.2]]) satisfies some of the conditions: if nonhomogeneous conditions on adjacent sides are constants or first-degree polynomials in one variable, subtracting a polynomial may leave a problem that needs only one series (Example §37.4).

^rem-37-1

> [!example] Example §37.4: A Plate between Insulating Sheets
> The temperature $u(x, y)$ in a thin plate between insulating sheets might satisfy
>
> $$
> \begin{aligned}
> &\frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0, && 0 < x < a, \quad 0 < y < b, \\
> &\frac{\partial u}{\partial x}(0, y) = 0, \quad u(a, y) = Sy, && 0 < y < b, \\
> &\frac{\partial u}{\partial y}(x, 0) = S, \quad u(x, b) = \frac{Sbx}{a}, && 0 < x < a .
> \end{aligned}
> $$
>
> **By splitting.** The conditions are nonhomogeneous on adjacent sides, so split $u = u_1 + u_2$:
>
> $$
> \begin{aligned}
> &\nabla^2u_1 = 0: && \frac{\partial u_1}{\partial x}(0, y) = 0, \ \ u_1(a, y) = 0, \ \ \frac{\partial u_1}{\partial y}(x, 0) = S, \ \ u_1(x, b) = \frac{Sbx}{a}; \\
> &\nabla^2u_2 = 0: && \frac{\partial u_2}{\partial x}(0, y) = 0, \ \ u_2(a, y) = Sy, \ \ \frac{\partial u_2}{\partial y}(x, 0) = 0, \ \ u_2(x, b) = 0 .
> \end{aligned}
> $$
>
> Then $u(a, y) = 0 + Sy$, $u(x, b) = Sbx/a + 0$, $u_x(0, y) = 0 + 0$, $u_y(x, 0) = S + 0$. For $u_1$ the factor $X$ satisfies $X'(0) = 0$, $X(a) = 0$, the mixed eigenvalue problem of [[§21 Example꞉ Different Boundary Conditions#^thm-21-1|Theorem §21.1]], and for $u_2$ the factor $Y$ satisfies $Y'(0) = 0$, $Y(b) = 0$. The product solutions are
>
> $$
> u_1: \ \cos(\lambda_nx)\big(a_n\cosh(\lambda_ny) + b_n\sinh(\lambda_ny)\big), \quad \lambda_n = \Big(n - \frac12\Big)\frac\pi a ; \qquad
> u_2: \ \cos(\mu_ny)\big(A_n\cosh(\mu_nx) + B_n\sinh(\mu_nx)\big), \quad \mu_n = \Big(n - \frac12\Big)\frac\pi b ,
> $$
>
> $n = 1, 2, \ldots$, and two series must be computed.
>
> **With a polynomial.** The polynomial $v(y) = Sy$ is harmonic and satisfies several of the conditions:
>
> $$
> \frac{\partial v}{\partial x}(0, y) = 0, \quad v(a, y) = Sy, \quad \frac{\partial v}{\partial y}(x, 0) = S, \quad v(x, b) = Sb .
> $$
>
> So set $u = v + w$. Then $w$ solves
>
> $$
> \nabla^2w = 0, \qquad \frac{\partial w}{\partial x}(0, y) = 0, \quad w(a, y) = 0, \quad \frac{\partial w}{\partial y}(x, 0) = 0, \quad w(x, b) = \frac{Sb(x - a)}{a} ,
> $$
>
> a problem with only one nonhomogeneous condition. Its product solutions are $\cos(\lambda_nx)\cosh(\lambda_ny)$, $\lambda_n = (2n - 1)\pi/(2a)$: the $\cos$ satisfies $X'(0) = 0$, $X(a) = 0$, and $\cosh$ is the solution of $Y'' - \lambda_n^2Y = 0$ with $Y'(0) = 0$. So
>
> $$
> w(x, y) = \sum_{n=1}^{\infty}c_n\frac{\cosh(\lambda_ny)}{\cosh(\lambda_nb)}\cos(\lambda_nx), \qquad \sum_{n=1}^{\infty}c_n\cos(\lambda_nx) = \frac{Sb(x - a)}{a}, \quad 0 < x < a .
> $$
>
> The functions $\cos(\lambda_nx)$ are orthogonal on $0 < x < a$ with $\int_0^a\cos^2(\lambda_nx)\,dx = a/2$ ([[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]]). Integrating by parts, and using $\cos(\lambda_na) = 0$,
>
> $$
> \int_0^a(x - a)\cos(\lambda_nx)\,dx = \Big[\frac{(x - a)\sin(\lambda_nx)}{\lambda_n}\Big]_0^a - \frac{1}{\lambda_n}\int_0^a\sin(\lambda_nx)\,dx = -\frac{1 - \cos(\lambda_na)}{\lambda_n^2} = -\frac{1}{\lambda_n^2} ,
> $$
>
> so $c_n = \dfrac2a\cdot\dfrac{Sb}{a}\cdot\Big(-\dfrac{1}{\lambda_n^2}\Big) = -\dfrac{8Sb}{(2n - 1)^2\pi^2}$, and
>
> $$
> u(x, y) = Sy - \frac{8Sb}{\pi^2}\sum_{n=1}^{\infty}\frac{\cosh(\lambda_ny)}{(2n - 1)^2\cosh(\lambda_nb)}\cos(\lambda_nx), \qquad \lambda_n = \frac{(2n - 1)\pi}{2a} .
> $$
>
> **Check.** $u(a, y) = Sy$ since $\cos(\lambda_na) = 0$; $u_x(0, y) = 0$ and $u_y(x, 0) = S$ term by term; and at $y = b$, $u(x, b) = Sb - Sb\big(1 - \frac xa\big) = \frac{Sbx}{a}$ by the expansion of $1 - x/a$ just computed. One series instead of two: the polynomial did half the work.
>
> *Powers: 4.3, Examples 2 and 3; Exercise 4.3.7*

^ex-37-4

## The Poisson Equation

> [!definition] Definition §37.1: Poisson Equation
> The **Poisson equation** is
>
> $$
> \nabla^2u = -H \qquad \text{in a region } \mathcal R ,
> $$
>
> where $H$ is a given function (a source term). Three examples:
> 1. $u$ is the deflection of a membrane that is fastened at its edges, so $u = 0$ on the boundary of $\mathcal R$; $H$ is proportional to the pressure difference across the membrane ([[§41★ Two-Dimensional Wave Equation꞉ Derivation|§41★]]).
> 2. $u$ is the steady-state temperature in a cross section of a long cylindrical rod that is carrying an electrical current; $H$ is proportional to the power in resistance heating ([[§42 Three-Dimensional Heat Equation#^def-42-1|Definition §42.1]]).
> 3. $u$ is the stress function on the cross section $\mathcal R$ of a cylindrical bar or rod in torsion (the shear stresses are proportional to the partial derivatives of $u$); $H$ is proportional to the rate of twist and to the shear modulus of the material; $u = 0$ on the boundary of $\mathcal R$.
>
> *Powers: 4.3 (text)*

^def-37-1

> [!remark]- Connections
> - Uniqueness: two solutions of the same Poisson equation with the same boundary values differ by a harmonic function vanishing on the boundary, hence coincide, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|452 Ex. §17.1]] (stated there for $\Delta u_1 = \Delta u_2$); in the vault's terms also [[§39 Potential in a Disk#^cor-39-6|Corollary §39.6]] applied to the difference.
> - See also: [[§116★ Transformations of Harmonic Functions#^cor-116-3|342 Cor. §116.3]] (how the Poisson equation transforms under an analytic change of variables).

> [!theorem] Proposition §37.1: Polynomial Solutions of the Poisson Equation
> If $H$ is a constant, the polynomial
>
> $$
> P(x, y) = A + Bx + Cy + Dx^2 + Exy + Fy^2
> $$
>
> is a solution of $\nabla^2P = -H$ if and only if $2(D + F) = -H$. The other coefficients are arbitrary and may be chosen for convenience in satisfying boundary conditions.
>
> *Powers: 4.3 (text); Exercise 4.3.10*

^prop-37-1

> [!proof]+ Proof
> $P_{xx} = 2D$ and $P_{yy} = 2F$, so $\nabla^2P = 2(D + F)$, which equals $-H$ exactly when $2(D + F) = -H$.

^pf-37-1

*Uses:* [[§37 Further Examples for a Rectangle#^def-37-1|Def. §37.1]]

More generally, if $H$ is a polynomial in $x$ and $y$, a solution can be found in the form of a polynomial of total degree $2$ higher than $H$. If $H$ is a more general function, it may be expanded in a double Fourier series ([[§43 Two-Dimensional Heat Equation꞉ Solution|§43]]) and the equation solved term by term, following the idea of [[§16★ Applications of Fourier Series and Integrals#^thm-16-2|Theorem §16.2]] (Powers 1.11B). In a disk the analogous idea is a Fourier series in $\theta$ alone: [[§39 Potential in a Disk#^ex-39-3|Example §39.3]].

> [!remark] Remark: Method — Poisson's Equation in a Rectangle
> To solve $\nabla^2u = -H$ ($H$ constant) in a rectangle with given boundary values:
> 1. Choose a polynomial $v$ as in Proposition §37.1 that satisfies the Poisson equation and the boundary conditions on one pair of facing sides (often a function of one variable, such as $Hx(a - x)/2$).
> 2. Set $u = v + w$. Then $\nabla^2w = \nabla^2u - \nabla^2v = -H + H = 0$, and $w$ has boundary values "original data minus $v$", which vanish on the chosen pair of sides.
> 3. Solve the potential problem for $w$ by [[§36 Potential in a Rectangle#^thm-36-1|Theorem §36.1]] (or a variant for other boundary conditions), and add.

^rem-37-2

> [!example] Example §37.5: Deflection of a Pressurized Membrane
> A membrane is stretched over the rectangle $0 < x < a$, $0 < y < b$ and fastened at its edges; a pressure difference $p$ (below to above) acts on it, and $\sigma$ is the surface tension. Its deflection satisfies
>
> $$
> \nabla^2u = -H \quad \text{in the rectangle}, \qquad u = 0 \quad \text{on the boundary}, \qquad H = \frac p\sigma .
> $$
>
> **The polynomial.** $v(x) = Hx(a - x)/2$ satisfies $v'' = -H$, the Poisson equation, and the two boundary conditions $v(0) = 0$, $v(a) = 0$. It is the deflection of an infinitely long strip of width $a$.
>
> **The correction.** Set $u = v + w$. Then $w$ solves
>
> $$
> \nabla^2w = 0, \qquad w(0, y) = 0, \quad w(a, y) = 0, \quad w(x, 0) = -v(x), \quad w(x, b) = -v(x) .
> $$
>
> This is Theorem §36.1 with $f_1 = f_2 = -v$. The sine coefficients of $v$ are
>
> $$
> \frac2a\int_0^a\frac{Hx(a - x)}{2}\sin\Big(\frac{n\pi x}{a}\Big)dx = \frac{2Ha^2\big(1 - (-1)^n\big)}{n^3\pi^3} ,
> $$
>
> that is, $4Ha^2/(n^3\pi^3)$ for odd $n$ and $0$ for even $n$. With equal data on top and bottom the symmetric form of [[§36 Potential in a Rectangle#^ex-36-1|Example §36.1]] applies, and
>
> $$
> u(x, y) = \frac{Hx(a - x)}{2} - \frac{4Ha^2}{\pi^3}\sum_{n \text{ odd}}\frac{1}{n^3}\,\frac{\cosh\big(\frac{n\pi}{a}(y - \frac b2)\big)}{\cosh\big(\frac{n\pi b}{2a}\big)}\sin\Big(\frac{n\pi x}{a}\Big) .
> $$
>
> **The maximum deflection** is at the center. Using only the first term of the series,
>
> $$
> u\Big(\frac a2, \frac b2\Big) \approx Ha^2\Big(\frac18 - \frac{4}{\pi^3\cosh(\pi b/2a)}\Big) .
> $$
>
> For a square ($b = a$) this is $Ha^2(0.1250 - 0.0514) = 0.0736\,Ha^2$; the full series gives $0.0737\,Ha^2$. For a long rectangle ($b \gg a$) the correction vanishes and the center deflection tends to $Ha^2/8$, that of the strip.
>
> *Powers: 4.3, Example 4; Exercise 4.3.9*

^ex-37-5
