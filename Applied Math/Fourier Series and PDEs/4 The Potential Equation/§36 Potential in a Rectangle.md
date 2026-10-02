---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: 36
powers: "4.2"
aliases: ["Powers 4.2"]
tags: [fourier-series-and-pdes, math341]
---
← [[§35 Potential Equation]] · ↑ [[· 4 The Potential Equation]] · [[§37 Further Examples for a Rectangle]] →

*Powers, Section 4.2 · MAT 341 lectures 11.19–11.21 · HW 12 · Practice Final.*

Dirichlet's problem in a rectangle, Laplace's equation with prescribed values on all four sides, is one of the simplest and most important problems of mathematical physics: the steady temperature in a plate whose edges are held at given temperatures, or the potential in a rectangular box with given voltages on its walls. Separation of variables works as soon as the boundary values vanish on two parallel sides: the factor along those sides solves a familiar eigenvalue problem, the other factor is a combination of hyperbolic functions, and the two remaining sides are fitted with Fourier sine series. A general problem is split into two such problems and the solutions are added. Unlike the heat and wave equations there is no time variable; the two space variables play symmetric roles, and the choice of which pair of sides carries the eigenvalue problem is dictated by the boundary conditions.

## Two Nonzero Sides

Consider first a problem with homogeneous conditions on the two vertical sides:

$$
\begin{aligned}
&\frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0, && 0 < x < a, \quad 0 < y < b, && (1) \\
&u(x, 0) = f_1(x), \quad u(x, b) = f_2(x), && 0 < x < a, && (2), (3) \\
&u(0, y) = 0, \quad u(a, y) = 0, && 0 < y < b. && (4), (5)
\end{aligned}
$$

> [!theorem] Theorem §36.1: Dirichlet Problem in a Rectangle with Two Nonzero Sides
> Let $\lambda_n = n\pi/a$, and let $a_n$ and $c_n$ be the Fourier sine coefficients of $f_1$ and $f_2$ on $0 < x < a$:
>
> $$
> a_n = \frac2a\int_0^a f_1(x)\sin(\lambda_nx)\,dx, \qquad c_n = \frac2a\int_0^a f_2(x)\sin(\lambda_nx)\,dx .
> $$
>
> The series solution of (1)–(5) is
>
> $$
> u(x, y) = \sum_{n=1}^{\infty}\Big(a_n\cosh(\lambda_ny) + b_n\sinh(\lambda_ny)\Big)\sin(\lambda_nx), \qquad b_n = \frac{c_n - a_n\cosh(\lambda_nb)}{\sinh(\lambda_nb)} , \qquad (9)
> $$
>
> or, equivalently,
>
> $$
> u(x, y) = \sum_{n=1}^{\infty}\left(c_n\frac{\sinh(\lambda_ny)}{\sinh(\lambda_nb)} + a_n\frac{\sinh\big(\lambda_n(b - y)\big)}{\sinh(\lambda_nb)}\right)\sin(\lambda_nx) . \qquad (11)
> $$
>
> The function multiplying $c_n$ is $0$ at $y = 0$ and $1$ at $y = b$; the function multiplying $a_n$ is $1$ at $y = 0$ and $0$ at $y = b$.
>
> *Powers: 4.2, Equations (9)–(11)*

^thm-36-1

> [!proof]+ Proof
> It is not obvious in advance that separation of variables will work, but the equation is homogeneous and so are two boundary conditions, so we try it.
>
> **Separation.** A product $u = X(x)Y(y)$ satisfies (1) when $X''(x)Y(y) + X(x)Y''(y) = 0$; dividing by $XY$,
>
> $$
> \frac{X''(x)}{X(x)} = -\frac{Y''(y)}{Y(y)} . \qquad (6)
> $$
>
> The left side does not depend on $y$ and the right side does not depend on $x$, so both equal a constant. The nonhomogeneous conditions (2), (3) do not, in general, become conditions on $X$ or $Y$; but the homogeneous conditions (4), (5) require (for a product that is not identically zero)
>
> $$
> X(0) = 0, \qquad X(a) = 0 . \qquad (7)
> $$
>
> **The sign of the constant.** If the constant is positive, $\mu^2$, then $X'' - \mu^2X = 0$, so $X = A\cosh(\mu x) + B\sinh(\mu x)$; $X(0) = A = 0$ and then $X(a) = B\sinh(\mu a) = 0$ forces $B = 0$, so $u \equiv 0$. (Powers checks only this case; if the constant is $0$, then $X = A + Bx$ and (7) again forces $A = B = 0$.) So the constant is negative, $-\lambda^2$, and (6) separates into
>
> $$
> X'' + \lambda^2X = 0, \qquad Y'' - \lambda^2Y = 0 . \qquad (8)
> $$
>
> **The eigenvalue problem.** $X'' + \lambda^2X = 0$ with (7) is the eigenvalue problem of [[§19 Example꞉ Fixed End Temperatures|§19]]: its solutions are $X_n(x) = \sin(\lambda_nx)$, $\lambda_n^2 = (n\pi/a)^2$, $n = 1, 2, \ldots$. The accompanying $Y$'s solve $Y'' - \lambda_n^2Y = 0$ ([[§1★ Homogeneous Linear Equations#^ex-1-1|Example §1.1]]):
>
> $$
> Y_n(y) = a_n\cosh(\lambda_ny) + b_n\sinh(\lambda_ny),
> $$
>
> with constants $a_n$, $b_n$ still unknown. Each product $X_nY_n$ satisfies (1), (4) and (5), and so does any sum of them; this gives the form (9).
>
> **The condition at $y = 0$.** Putting $y = 0$ in (9), (2) becomes
>
> $$
> u(x, 0) = \sum_{n=1}^{\infty} a_n\sin\Big(\frac{n\pi x}{a}\Big) = f_1(x), \qquad 0 < x < a , \qquad (10)
> $$
>
> a Fourier sine series ([[§7 Arbitrary Period and Half-Range Expansions|§7]], half-range expansions): the $a_n$ must be the sine coefficients of $f_1$.
>
> **The condition at $y = b$.** Condition (3) reads
>
> $$
> u(x, b) = \sum_{n=1}^{\infty}\Big(a_n\cosh(\lambda_nb) + b_n\sinh(\lambda_nb)\Big)\sin\Big(\frac{n\pi x}{a}\Big) = f_2(x), \qquad 0 < x < a .
> $$
>
> This is again a sine series, so $a_n\cosh(\lambda_nb) + b_n\sinh(\lambda_nb) = c_n$, the $n$th sine coefficient of $f_2$. Since $a_n$ is known and $\sinh(\lambda_nb) \ne 0$, this determines $b_n$ as in (9).
>
> **The form (11).** Substituting $b_n$ into (9),
>
> $$
> a_n\cosh(\lambda_ny) + b_n\sinh(\lambda_ny) = c_n\frac{\sinh(\lambda_ny)}{\sinh(\lambda_nb)} + a_n\Big(\cosh(\lambda_ny) - \frac{\cosh(\lambda_nb)}{\sinh(\lambda_nb)}\sinh(\lambda_ny)\Big) .
> $$
>
> (Powers says the last bracket simplifies "from hyperbolic identities"; here is how.) By the subtraction formula $\sinh(A - B) = \sinh A\cosh B - \cosh A\sinh B$,
>
> $$
> \cosh(\lambda_ny) - \frac{\cosh(\lambda_nb)}{\sinh(\lambda_nb)}\sinh(\lambda_ny) = \frac{\sinh(\lambda_nb)\cosh(\lambda_ny) - \cosh(\lambda_nb)\sinh(\lambda_ny)}{\sinh(\lambda_nb)} = \frac{\sinh\big(\lambda_n(b - y)\big)}{\sinh(\lambda_nb)} ,
> $$
>
> which gives (11). The values of the two coefficient functions at $y = 0$ and $y = b$ are read off from $\sinh 0 = 0$.

^pf-36-1

*Uses:* [[§35 Potential Equation#^def-35-1|Def. §35.1]], [[§1★ Homogeneous Linear Equations#^ex-1-1|Ex. §1.1]], [[§19 Example꞉ Fixed End Temperatures|§19]] (the eigenvalue problem), [[§7 Arbitrary Period and Half-Range Expansions|§7]] (sine series)

> [!remark]- Connections
> - Why the series really is harmonic inside: for $\delta \le y \le b - \delta$, $\big|\sinh(\lambda_ny)/\sinh(\lambda_nb)\big| \le 2e^{-\lambda_n(b - y)} \le 2e^{-n\pi\delta/a}$ (for $\lambda_n b \ge 1$, say), and the same for the other factor, while $|a_n|, |c_n| \le 2\max|f_i|$. Differentiating term by term only brings in powers of $\lambda_n$, so the series and its differentiated series are dominated by $\sum n^2e^{-n\pi\delta/a} < \infty$; by the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]], they converge uniformly and (with [[§25 More on Uniform Convergence#^thm-25-2|451 Thm. §25.2]]) define a continuous function that may be differentiated term by term. At $y = 0$ and $y = b$ the series reduce to the Fourier sine series of $f_1$, $f_2$, whose convergence is the subject of [[§8 Convergence of Fourier Series|§8]].

> [!remark] Remark: Method — Separation of Variables for the Potential Equation in a Rectangle
> Lecture 11.19 organizes the work into steps:
> 1. **Split** the problem, if necessary, into problems that each have homogeneous conditions on one pair of parallel sides (Theorem §36.2 below; for other boundary conditions, [[§37 Further Examples for a Rectangle#^rem-37-1|§37]]).
> 2. **Separate:** set $u = X(x)Y(y)$, get $X''/X = -Y''/Y = $ constant, and turn the homogeneous conditions into conditions on the factor along those sides.
> 3. **Solve the eigenvalue problem** for that factor, checking the cases constant positive, zero and negative; this gives the eigenvalues $\lambda_n$ and eigenfunctions.
> 4. **Solve the other factor's equation**, $Y'' - \lambda_n^2Y = 0$ (hyperbolic functions; $A + By$ for $\lambda_0 = 0$), and write the **basic solutions** $X_nY_n$.
> 5. **Superpose** and fit the two remaining sides: each gives a Fourier series problem that determines one constant per $n$.
> 6. **Add** the solutions of the split problems.
>
> *Source: 341 lecture 11.19*

^rem-36-1

> [!example] Example §36.1: Equal Triangular Data on Top and Bottom
> Solve (1)–(5) with
>
> $$
> f_1(x) = f_2(x) = \begin{cases} \dfrac{2x}{a}, & 0 < x < \dfrac a2, \\[2mm] 2\Big(\dfrac{a - x}{a}\Big), & \dfrac a2 < x < a, \end{cases}
> $$
>
> a triangle of height $1$.
>
> **Coefficients.** Since $f_1 = f_2$, $a_n = c_n$. Integrating by parts on each half,
>
> $$
> \frac2a\int_0^{a/2}\frac{2x}{a}\sin\Big(\frac{n\pi x}{a}\Big)dx + \frac2a\int_{a/2}^a 2\Big(\frac{a - x}{a}\Big)\sin\Big(\frac{n\pi x}{a}\Big)dx = \frac{8}{\pi^2}\,\frac{\sin(n\pi/2)}{n^2} ,
> $$
>
> so $c_n = a_n = \dfrac{8}{\pi^2}\dfrac{\sin(n\pi/2)}{n^2}$, which is zero for even $n$.
>
> **Solution.** By (11),
>
> $$
> u(x, y) = \frac{8}{\pi^2}\sum_{n=1}^{\infty}\frac{\sin(n\pi/2)}{n^2}\,\frac{\sinh\big(\frac{n\pi}{a}y\big) + \sinh\big(\frac{n\pi}{a}(b - y)\big)}{\sinh\big(\frac{n\pi b}{a}\big)}\,\sin\Big(\frac{n\pi x}{a}\Big) . \qquad (12)
> $$
>
> **A symmetric form.** By $\sinh A + \sinh B = 2\sinh\frac{A + B}{2}\cosh\frac{A - B}{2}$ and $\sinh(2C) = 2\sinh C\cosh C$, with $A = \lambda_ny$, $B = \lambda_n(b - y)$,
>
> $$
> \frac{\sinh(\lambda_ny) + \sinh\big(\lambda_n(b - y)\big)}{\sinh(\lambda_nb)} = \frac{2\sinh(\lambda_nb/2)\cosh\big(\lambda_n(y - \frac b2)\big)}{2\sinh(\lambda_nb/2)\cosh(\lambda_nb/2)} = \frac{\cosh\big(\frac{n\pi}{a}(y - \frac12b)\big)}{\cosh\big(\frac{n\pi b}{2a}\big)} ,
> $$
>
> which shows the symmetry of $u$ about the midline $y = b/2$.
>
> **The value at the center.** At $(a/2, b/2)$ the cosh in the numerator is $1$ and $\sin^2(n\pi/2) = 1$ for odd $n$, so
>
> $$
> u\Big(\frac a2, \frac b2\Big) = \frac{8}{\pi^2}\sum_{n \text{ odd}}\frac{1}{n^2\cosh\big(\frac{n\pi b}{2a}\big)} \approx \begin{cases} 0.325, & b = a, \\ 0.070, & b = 2a, \\ 0.630, & b = a/2. \end{cases}
> $$
>
> The terms decrease very fast: for $b = a$ the first term alone gives $0.323$. The center is a saddle point of $u$, as the maximum principle requires: $u$ increases toward the top and bottom edges, where the data are largest, and decreases toward the sides, where $u = 0$ (figure below).
>
> *Powers: 4.2, Example; Exercises 4.2.2 and 4.2.3*

^ex-36-1

![[m341-36-1.svg]]
*Level curves $u = 0.1, 0.2, \ldots, 0.9$ of the solution (12) in the square $a = b = 1$, computed from the series in its symmetric form. Curves with $u \ge 0.5$ (red) close up against the top and bottom edges around the peaks of the triangular data; the curves with $u \le 0.4$ (blue) run from top to bottom near the sides, where $u = 0$. The two families meet at the saddle point in the center.*

## The General Dirichlet Problem

In general the boundary values are nonzero on all four sides:

$$
\begin{aligned}
&\nabla^2u = 0, && 0 < x < a, \quad 0 < y < b, && (13) \\
&u(x, 0) = f_1(x), \quad u(x, b) = f_2(x), && 0 < x < a, && (14), (15) \\
&u(0, y) = g_1(y), \quad u(a, y) = g_2(y), && 0 < y < b. && (16), (17)
\end{aligned}
$$

> [!theorem] Theorem §36.2: Dirichlet Problem in a Rectangle by Superposition
> The solution of (13)–(17) is $u = u_1 + u_2$, where $u_1$ solves
>
> $$
> \nabla^2u_1 = 0, \qquad u_1(x, 0) = f_1(x), \quad u_1(x, b) = f_2(x), \quad u_1(0, y) = 0, \quad u_1(a, y) = 0 ,
> $$
>
> and is given by Theorem §36.1, and $u_2$ solves
>
> $$
> \nabla^2u_2 = 0, \qquad u_2(x, 0) = 0, \quad u_2(x, b) = 0, \quad u_2(0, y) = g_1(y), \quad u_2(a, y) = g_2(y) ,
> $$
>
> and is given by
>
> $$
> u_2(x, y) = \sum_{n=1}^{\infty}\sin(\mu_ny)\,\frac{A_n\sinh(\mu_nx) + B_n\sinh\big(\mu_n(a - x)\big)}{\sinh(\mu_na)}, \qquad \mu_n = \frac{n\pi}{b} , \qquad (18)
> $$
>
> $$
> A_n = \frac2b\int_0^b g_2(y)\sin(\mu_ny)\,dy, \qquad B_n = \frac2b\int_0^b g_1(y)\sin(\mu_ny)\,dy .
> $$
>
> *Powers: 4.2, Equation (18); Exercise 4.2.8*

^thm-36-2

> [!proof]+ Proof
> **The sum solves the problem.** The Laplacian is linear, so $\nabla^2(u_1 + u_2) = \nabla^2u_1 + \nabla^2u_2 = 0$, and the boundary values add: $u(x, 0) = f_1(x) + 0$, $u(x, b) = f_2(x) + 0$, $u(0, y) = 0 + g_1(y)$, $u(a, y) = 0 + g_2(y)$. Each of $u_1$ and $u_2$ has homogeneous conditions on a pair of parallel sides, which is what makes separation of variables work.
>
> **The formula for $u_2$** (Exercise 8). This is Theorem §36.1 with the roles of $x$ and $y$ (and of $a$ and $b$) exchanged. With $u_2 = X(x)Y(y)$, the homogeneous conditions give $Y(0) = Y(b) = 0$, so now $-Y''/Y = X''/X$ must be $\mu^2 > 0$ (the other signs give only $Y \equiv 0$, as in the proof of Theorem §36.1), and
>
> $$
> Y_n(y) = \sin(\mu_ny), \quad \mu_n = \frac{n\pi}{b}, \qquad X_n'' - \mu_n^2X_n = 0 .
> $$
>
> For $X_n$ use the solutions $\sinh(\mu_nx)$ and $\sinh(\mu_n(a - x))$. They are independent (Exercise 4.2.1): their Wronskian is
>
> $$
> \sinh(\mu x)\cdot\big(-\mu\cosh(\mu(a - x))\big) - \mu\cosh(\mu x)\sinh(\mu(a - x)) = -\mu\sinh\big(\mu x + \mu(a - x)\big) = -\mu\sinh(\mu a) \ne 0 ,
> $$
>
> by the addition formula for $\sinh$, so they span the solutions of $X'' - \mu^2X = 0$ just as well as $\cosh$ and $\sinh$ do. Superposing gives (18). At $x = 0$ the first fraction is $0$ and the second is $1$, so $u_2(0, y) = \sum B_n\sin(\mu_ny) = g_1(y)$: the $B_n$ are the sine coefficients of $g_1$ on $0 < y < b$. At $x = a$ the roles are reversed, and the $A_n$ are the sine coefficients of $g_2$.

^pf-36-2

*Uses:* [[§36 Potential in a Rectangle#^thm-36-1|§36.1]], [[§1★ Homogeneous Linear Equations#^thm-1-3|§1.3]] (Wronskian test), [[§7 Arbitrary Period and Half-Range Expansions|§7]] (sine series)

In the individual problems for $u_1$ and $u_2$, separation of variables works because homogeneous conditions on parallel sides of the rectangle translate into conditions on one of the factor functions. The same splitting works for other kinds of boundary conditions ([[§37 Further Examples for a Rectangle|§37]]).

> [!remark] Remark: Using Polynomials
> When the boundary conditions are not complicated functions, it may be possible to satisfy some of them with a harmonic polynomial ([[§35 Potential Equation#^prop-35-2|Proposition §35.2]], [[§35 Potential Equation#^ex-35-2|Example §35.2]]). Then the difference between $u$ and the polynomial is a solution of the potential equation that satisfies some homogeneous boundary conditions, and fewer series are needed. Worked instances: [[§37 Further Examples for a Rectangle#^ex-37-4|Example §37.4]] and, for the Poisson equation, [[§37 Further Examples for a Rectangle#^ex-37-5|Example §37.5]].

^rem-36-2

> [!example] Example §36.2: Data on Two Adjacent Sides of a Square
> Solve
>
> $$
> \begin{aligned}
> &u_{xx} + u_{yy} = 0, && 0 < x < \pi, \quad 0 < y < \pi; \\
> &u(x, 0) = x, \quad u(x, \pi) = 0, && 0 < x < \pi; \\
> &u(0, y) = \sin(3y), \quad u(\pi, y) = 0, && 0 < y < \pi .
> \end{aligned}
> $$
>
> **(a) Split.** Let $v$ solve the problem with $v(0, y) = \sin(3y)$ and $v = 0$ on the other three sides, and $w$ the problem with $w(x, 0) = x$ and $w = 0$ on the other three sides. Then $(w + v)_{xx} + (w + v)_{yy} = (w_{xx} + w_{yy}) + (v_{xx} + v_{yy}) = 0$, and on the four sides $w + v$ takes the values $x + 0$, $0 + 0$, $0 + \sin(3y)$, $0 + 0$: it is the solution.
>
> **(b) Separation for $v$.** With $v = X(x)Y(y)$, $-X''/X = Y''/Y = p$, so $X'' = -pX$, $Y'' = pY$, and $v(x, 0) = v(x, \pi) = 0$ give $Y(0) = Y(\pi) = 0$.
>
> **(c) Basic solutions.** If $p > 0$, $Y = Ae^{\sqrt p y} + Be^{-\sqrt p y}$, and $Y(0) = Y(\pi) = 0$ force $A = B = 0$; if $p = 0$, $Y = Ay + B$ is again forced to vanish. If $p = -\lambda^2 < 0$, $Y = A\sin(\lambda y) + B\cos(\lambda y)$; $Y(0) = 0$ gives $B = 0$ and $Y(\pi) = A\sin(\lambda\pi) = 0$ gives $\lambda = n = 1, 2, \ldots$. Then $X'' = n^2X$, and the basic solutions are
>
> $$
> v_n(x, y) = \sin(ny)\big(a_n\sinh(nx) + b_n\cosh(nx)\big) .
> $$
>
> **(d) The solution $v$.** At $x = 0$: $\sum b_n\sin(ny) = \sin(3y)$, so $b_3 = 1$ and $b_n = 0$ for $n \ne 3$. At $x = \pi$: $a_n\sinh(n\pi) + b_n\cosh(n\pi) = 0$, so $a_3 = -\coth(3\pi)$ and $a_n = 0$ otherwise. Thus
>
> $$
> v(x, y) = \sin(3y)\big(\cosh(3x) - \coth(3\pi)\sinh(3x)\big) = \sin(3y)\,\frac{\sinh\big(3(\pi - x)\big)}{\sinh(3\pi)} ,
> $$
>
> by the identity in the proof of Theorem §36.1.
>
> **(e) Basic solutions for $w$.** Exchanging the roles of $x$ and $y$: $X(0) = X(\pi) = 0$ gives $X = \sin(nx)$, and
>
> $$
> w_n(x, y) = \sin(nx)\big(c_n\sinh(ny) + d_n\cosh(ny)\big), \qquad n = 1, 2, \ldots
> $$
>
> **(f) The solution $w$.** At $y = 0$: $\sum d_n\sin(nx) = x$ on $0 < x < \pi$, so, integrating by parts,
>
> $$
> d_n = \frac2\pi\int_0^\pi x\sin(nx)\,dx = \frac2\pi\Big[-\frac{x\cos(nx)}{n}\Big]_0^\pi + \frac{2}{\pi n}\int_0^\pi\cos(nx)\,dx = \frac{2(-1)^{n+1}}{n} .
> $$
>
> At $y = \pi$: $c_n\sinh(n\pi) + d_n\cosh(n\pi) = 0$, so $c_n = -d_n\coth(n\pi)$, and
>
> $$
> w(x, y) = \sum_{n=1}^{\infty}\frac{2(-1)^{n+1}}{n}\,\sin(nx)\,\frac{\sinh\big(n(\pi - y)\big)}{\sinh(n\pi)} .
> $$
>
> The solution is $u = v + w$.
>
> *Source: 341 HW 12, Problem 1*

^ex-36-2

> [!example] Example §36.3: A Rapidly Oscillating Boundary Value
> Solve
>
> $$
> \begin{aligned}
> &u_{xx} + u_{yy} = 0, && 0 < x < 1, \quad 0 < y < 2; \\
> &u(0, y) = 1, \quad u(1, y) = 0, && 0 < y < 2; \\
> &u(x, 0) = \sin(20\pi x), \quad u(x, 2) = 0, && 0 < x < 1 .
> \end{aligned}
> $$
>
> **Split** as in Theorem §36.2: $v$ carries the data $v(0, y) = 1$ and vanishes on the other sides; $w$ carries $w(x, 0) = \sin(20\pi x)$ and vanishes on the other sides; $u = v + w$ by the same check as in Example §36.2(a).
>
> **The problem for $v$.** With $v = X(x)Y(y)$, $X'' = pX$, $Y'' = -pY$, $Y(0) = Y(2) = 0$. For $-p \le 0$ there is no nonzero solution; for $p = \lambda^2$, $Y_n = \sin(n\pi y/2)$ with $\lambda = n\pi/2$, and $X_n = A_n\cosh(n\pi x/2) + B_n\sinh(n\pi x/2)$. At $x = 0$:
>
> $$
> 1 = \sum_{n=1}^{\infty}A_n\sin\Big(\frac{n\pi y}{2}\Big), \qquad A_n = \frac22\int_0^2\sin\Big(\frac{n\pi y}{2}\Big)dy = \frac{2}{n\pi}\big(1 - (-1)^n\big) ,
> $$
>
> which is $4/(n\pi)$ for odd $n$ and $0$ for even $n$. At $x = 1$: $A_n\cosh(n\pi/2) + B_n\sinh(n\pi/2) = 0$, so $B_n = -A_n\coth(n\pi/2)$, and
>
> $$
> v(x, y) = \sum_{n=1}^{\infty}\frac{2(1 - (-1)^n)}{n\pi}\,\sin\Big(\frac{n\pi y}{2}\Big)\,\frac{\sinh\big(\frac{n\pi}{2}(1 - x)\big)}{\sinh\big(\frac{n\pi}{2}\big)} = \frac4\pi\sum_{n \text{ odd}}\frac1n\sin\Big(\frac{n\pi y}{2}\Big)\frac{\sinh\big(\frac{n\pi}{2}(1 - x)\big)}{\sinh\big(\frac{n\pi}{2}\big)} .
> $$
>
> **The problem for $w$.** Now $X(0) = X(1) = 0$ gives $X_n = \sin(n\pi x)$ and $w_n = \sin(n\pi x)\big(C_n\cosh(n\pi y) + D_n\sinh(n\pi y)\big)$. At $y = 0$: $\sum C_n\sin(n\pi x) = \sin(20\pi x)$, so $C_{20} = 1$ and all other $C_n = 0$. At $y = 2$: $C_n\cosh(2n\pi) + D_n\sinh(2n\pi) = 0$, so $D_{20} = -\coth(40\pi)$ and the other $D_n$ vanish:
>
> $$
> w(x, y) = \sin(20\pi x)\big(\cosh(20\pi y) - \coth(40\pi)\sinh(20\pi y)\big) = \sin(20\pi x)\,\frac{\sinh\big(20\pi(2 - y)\big)}{\sinh(40\pi)} .
> $$
>
> **The solution** is $u = v + w$. Note the size of $w$: $\sinh(20\pi(2 - y))/\sinh(40\pi) \approx e^{-20\pi y}$, which is below $0.002$ already at $y = 0.1$. A rapidly oscillating boundary value is felt only in a thin layer next to its edge; the interior sees essentially only the smooth part $v$. This is the potential-equation counterpart of the fast decay of high-frequency modes in the heat equation.
>
> *The key's final formula for $w$ has $\sinh(n\pi y)$ where $\sinh(20\pi y)$ is meant; its coefficients are correct.*
>
> *Source: 341 Practice Final, Q9*

^ex-36-3
