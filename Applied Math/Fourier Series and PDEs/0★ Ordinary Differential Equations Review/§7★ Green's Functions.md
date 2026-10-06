---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: "7★"
powers: "0.5"
aliases: ["Powers 0.5"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§6★ Singular Boundary Value Problems]] · ↑ [[· 0★ Ordinary Differential Equations Review]] · [[§8★ Mass–Spring–Damper System and Radial Heat Flow]] →

*Powers, Section 0.5.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

For a linear second-order boundary value problem with homogeneous boundary conditions at the two ends, $u'' + k(x)u' + p(x)u = f(x)$ on $l < x < r$, this section shows how the solution depends on the inhomogeneity $f$: it is an integral $u(x) = \int_l^r G(x, z)f(z)\,dz$, where the **Green's function** $G$ depends only on the equation and the boundary conditions. $G$ is built from two solutions of the homogeneous equation, one satisfying the left condition and one the right, by the variation-of-parameters formula of [[§4★ Variation of Parameters#^thm-4-3|Theorem §4.3]]. The construction fails exactly when the homogeneous problem has a nonzero solution, and this gives the existence and uniqueness theorem for boundary value problems: one solution, or else none or infinitely many. Physically, $G(x, z)$ is the response at $x$ to a unit point source at $z$ (a point load on a string, a point heat source in a rod), and $\int G f$ superposes these responses; the same idea, in more dimensions, gives the potential of a charge distribution.

## The Construction

> [!definition] Definition §10.1: Two-Point Boundary Value Problem with Separated Conditions
> The **boundary value problem** of this section is
>
> $$
> \frac{d^2u}{dx^2} + k(x)\frac{du}{dx} + p(x)u = f(x), \qquad l < x < r, \qquad (1)
> $$
>
> $$
> \alpha u(l) - \alpha'u'(l) = 0, \qquad (2)
> $$
>
> $$
> \beta u(r) + \beta'u'(r) = 0, \qquad (3)
> $$
>
> with constants $\alpha, \alpha', \beta, \beta'$, where $(\alpha, \alpha') \ne (0, 0)$ and $(\beta, \beta') \ne (0, 0)$. The primes on $\alpha'$, $\beta'$ do not indicate differentiation; they mark the coefficients of derivatives. Each condition involves only one endpoint, and both are homogeneous. The corresponding **homogeneous equation** is
>
> $$
> \frac{d^2u}{dx^2} + k(x)\frac{du}{dx} + p(x)u = 0, \qquad l < x < r . \qquad (4)
> $$
>
> *Powers: 0.5, Equations (1)–(4)*

^def-7-1

The construction uses two independent solutions $u_1$, $u_2$ of (4), chosen to simplify the algebra: $u_1$ satisfies the boundary condition at $x = l$ and $u_2$ the one at $x = r$,

$$
\alpha u_1(l) - \alpha'u_1'(l) = 0, \qquad (5) \qquad\qquad \beta u_2(r) + \beta'u_2'(r) = 0 , \qquad (6)
$$

with Wronskian

$$
W(z) = \begin{vmatrix} u_1(z) & u_2(z) \\ u_1'(z) & u_2'(z) \end{vmatrix} = u_1(z)u_2'(z) - u_2(z)u_1'(z) , \qquad (8)
$$

which is nonzero because $u_1$ and $u_2$ are independent ([[§1★ Homogeneous Linear Equations#^thm-1-3|Theorem §1.3]]).

> [!definition] Definition §11.1: Green's Function
> The **Green's function** for the problem (1), (2), (3) is
>
> $$
> G(x, z) = \begin{cases} \dfrac{u_1(z)u_2(x)}{W(z)}, & l < z \le x, \\[2ex] \dfrac{u_1(x)u_2(z)}{W(z)}, & x \le z < r, \end{cases} \qquad (17)
> $$
>
> with $u_1$, $u_2$ independent solutions of (4) satisfying (5) and (6), and $W$ their Wronskian (8). In words: $G(x, z)$ is $u_1$ evaluated at the smaller of $x, z$, times $u_2$ evaluated at the larger, divided by $W(z)$.
>
> *Powers: 0.5, Equation (17)*

^def-7-2

> [!theorem] Theorem §10.1: The Solution as a Green's Function Integral
> Let $k$, $p$, $f$ be continuous on $l \le x \le r$, and let $u_1$, $u_2$ be independent solutions of (4) satisfying (5), (6), such that
>
> $$
> \alpha u_2(l) - \alpha'u_2'(l) \ne 0 \qquad\text{and}\qquad \beta u_1(r) + \beta'u_1'(r) \ne 0 .
> $$
>
> Then
>
> $$
> u(x) = \int_l^r G(x, z)f(z)\,dz \qquad (18)
> $$
>
> solves the boundary value problem (1), (2), (3). Breaking the integral at $z = x$,
>
> $$
> u(x) = \int_l^x \frac{u_1(z)u_2(x)f(z)}{W(z)}\,dz + \int_x^r \frac{u_1(x)u_2(z)f(z)}{W(z)}\,dz . \qquad (16)
> $$
>
> *Powers: 0.5, Equations (7)–(18)*

^thm-7-1

> [!proof]+ Proof
> **The general solution.** By [[§4★ Variation of Parameters#^thm-4-3|Theorem §4.3]] with $t_0 = l$, together with [[§3★ Nonhomogeneous Linear Equations#^thm-3-2|Theorem §3.2]] and [[§1★ Homogeneous Linear Equations#^thm-1-3|Theorem §1.3]], the solutions of (1) are exactly the functions
>
> $$
> u(x) = c_1u_1(x) + c_2u_2(x) + \int_l^x \big(u_1(z)u_2(x) - u_2(z)u_1(x)\big)\frac{f(z)}{W(z)}\,dz . \qquad (7)
> $$
>
> **Its derivative.** Powers differentiates the integral by Leibniz's rule; the Fundamental Theorem of Calculus suffices. Put $A(x) = \int_l^x u_1f/W\,dz$ and $B(x) = \int_l^x u_2f/W\,dz$, so the integral in (7) is $u_2(x)A(x) - u_1(x)B(x)$. Since the integrands are continuous, $A' = u_1f/W$ and $B' = u_2f/W$, and
>
> $$
> \frac{d}{dx}\big(u_2A - u_1B\big) = u_2'A - u_1'B + \big(u_2u_1 - u_1u_2\big)\frac fW = u_2'A - u_1'B .
> $$
>
> Hence
>
> $$
> \frac{du}{dx} = c_1u_1'(x) + c_2u_2'(x) + \int_l^x \big(u_1(z)u_2'(x) - u_2(z)u_1'(x)\big)\frac{f(z)}{W(z)}\,dz .
> $$
>
> **The condition at $x = l$.** The integrals in $u$ and $u'$ are both $0$ at $x = l$, so
>
> $$
> \alpha u(l) - \alpha'u'(l) = c_1\big(\alpha u_1(l) - \alpha'u_1'(l)\big) + c_2\big(\alpha u_2(l) - \alpha'u_2'(l)\big) = 0 . \qquad (9)
> $$
>
> By (5) the first term is $0$, leaving $c_2\big(\alpha u_2(l) - \alpha'u_2'(l)\big) = 0$ (10); the factor is not $0$ by hypothesis, so $c_2 = 0$.
>
> **The condition at $x = r$.** With $c_2 = 0$,
>
> $$
> \beta u(r) + \beta'u'(r) = c_1\big(\beta u_1(r) + \beta'u_1'(r)\big) + \int_l^r \Big[u_1(z)\big(\beta u_2(r) + \beta'u_2'(r)\big) - u_2(z)\big(\beta u_1(r) + \beta'u_1'(r)\big)\Big]\frac{f(z)}{W(z)}\,dz = 0 . \qquad (11)
> $$
>
> By (6) the first term of the integrand is $0$, leaving
>
> $$
> \big(\beta u_1(r) + \beta'u_1'(r)\big)\Big(c_1 - \int_l^r u_2(z)\frac{f(z)}{W(z)}\,dz\Big) = 0 , \qquad (12)
> $$
>
> and the common factor is not $0$ by hypothesis, so
>
> $$
> c_1 = \int_l^r u_2(z)\frac{f(z)}{W(z)}\,dz . \qquad (13)
> $$
>
> **Assemble.** With these $c_1$, $c_2$, (7) satisfies both boundary conditions:
>
> $$
> u(x) = u_1(x)\int_l^r u_2(z)\frac{f(z)}{W(z)}\,dz + \int_l^x \big(u_1(z)u_2(x) - u_2(z)u_1(x)\big)\frac{f(z)}{W(z)}\,dz . \qquad (14)
> $$
>
> Break the first integral at $x$, $\int_l^r = \int_l^x + \int_x^r$ (15). The two terms $u_1(x)\int_l^x u_2f/W$ and $-\int_l^x u_2(z)u_1(x)f/W$ cancel, and what remains is (16). By Definition §7.2 the two integrands in (16) are $G(x, z)f(z)$ on $l < z \le x$ and on $x \le z < r$, which is (18).

^pf-7-1

*Uses:* [[§4★ Variation of Parameters#^thm-4-3|§4.3]], [[§3★ Nonhomogeneous Linear Equations#^thm-3-2|§3.2]], [[§1★ Homogeneous Linear Equations#^thm-1-3|§1.3]], [[§7★ Green's Functions#^def-7-2|Def. §7.2]], [[§41 The Fundamental Theorem of Calculus#^thm-41-1|Calc Thm. §41.1]] (FTC)

The two hypotheses on $u_1$, $u_2$ are automatic once they are independent: see [[§7★ Green's Functions#^lem-7-2|Lemma §7.2]].

> [!example] Example §10.1: Building a Green's Function
> Solve by constructing the Green's function:
>
> $$
> \frac{d^2u}{dx^2} - u = -1, \quad 0 < x < 1, \qquad u(0) = 0, \quad u(1) = 0 .
> $$
>
> **The two solutions.** The homogeneous equation $u'' - u = 0$ has the general solution $c_1\cosh(x) + c_2\sinh(x)$. For $u_1$ we need $u_1(0) = 0$: take $c_1 = 0$, $c_2 = 1$, $u_1(x) = \sinh(x)$. For $u_2$ we need $u_2(1) = 0$:
>
> $$
> u_2(x) = \sinh(1)\cosh(x) - \cosh(1)\sinh(x) = \sinh(1 - x) .
> $$
>
> **Wronskian.**
>
> $$
> W(x) = \begin{vmatrix} \sinh(x) & \sinh(1 - x) \\ \cosh(x) & -\cosh(1 - x) \end{vmatrix} = -\big(\sinh x\cosh(1 - x) + \cosh x\sinh(1 - x)\big) = -\sinh(1) ,
> $$
>
> by the addition formula for $\sinh$.
>
> **Green's function.** By (17),
>
> $$
> G(x, z) = \begin{cases} \dfrac{\sinh(z)\sinh(1 - x)}{-\sinh(1)}, & 0 < z \le x, \\[2ex] \dfrac{\sinh(x)\sinh(1 - z)}{-\sinh(1)}, & x \le z < 1. \end{cases}
> $$
>
> **Solution.** Since $f(x) = -1$, $u(x) = \int_0^1 -G(x, z)\,dz$. Breaking the integral at $x$, that is, using (16):
>
> $$
> \begin{aligned}
> u(x) &= \int_0^x \frac{\sinh(z)\sinh(1 - x)}{\sinh(1)}\,dz + \int_x^1 \frac{\sinh(x)\sinh(1 - z)}{\sinh(1)}\,dz \\
> &= \frac{\sinh(1 - x)}{\sinh(1)}\cosh(z)\Big|_0^x + \frac{\sinh(x)}{\sinh(1)}\big(-\cosh(1 - z)\big)\Big|_x^1 \\
> &= \frac{\sinh(1 - x)}{\sinh(1)}\big(\cosh(x) - 1\big) + \frac{\sinh(x)}{\sinh(1)}\big(\cosh(1 - x) - 1\big) \\
> &= \frac{\sinh(1 - x)\cosh(x) + \sinh(x)\cosh(1 - x)}{\sinh(1)} - \frac{\sinh(1 - x) + \sinh(x)}{\sinh(1)} \\
> &= 1 - \frac{\sinh(1 - x) + \sinh(x)}{\sinh(1)} ,
> \end{aligned}
> $$
>
> using the addition formula again in the last step. Check: $u'' = -\frac{\sinh(1 - x) + \sinh(x)}{\sinh(1)} = u - 1$, and $u(0) = u(1) = 1 - 1 = 0$.
>
> In this instance there are much quicker ways to the same result ($u = 1 + c_1\cosh x + c_2\sinh x$ and two boundary conditions). The advantage of the Green's function is that it shows how the solution depends on the inhomogeneity $f$: changing $f$ changes only the integrand.
>
> *Powers: 0.5, Example (constructing the Green's function)*

^ex-7-1

![[m341-5-1.svg]]
*The Green's function of Example §7.1, $G(x, z) = -\sinh(\min(x, z))\sinh(1 - \max(x, z))/\sinh 1$, as a function of $x$ for $z = \frac14, \frac12, \frac34$. Each graph satisfies $u'' - u = 0$ on both sides of $z$ and the boundary conditions at $0$ and $1$, is continuous at $x = z$, and has a corner there where the slope jumps by exactly $1$ (Proposition §7.5): it is the response to a unit point source at $z$.*

## When the Construction Fails

Looking back over the construction, the only possible failure (aside from discontinuous coefficients) is division by $0$. The quantities divided by or cancelled were

$$
W(x) = \begin{vmatrix} u_1(x) & u_2(x) \\ u_1'(x) & u_2'(x) \end{vmatrix}, \qquad \alpha u_2(l) - \alpha'u_2'(l), \qquad \beta u_1(r) + \beta'u_1'(r) \qquad (19)
$$

in (7), (10) and (12). Powers states that all three are $0$ if any one of them is, and that then $u_1$ and $u_2$ are proportional; here is the proof.

> [!theorem] Lemma §11.1: The Three Quantities Vanish Together
> Let $k$, $p$ be continuous on $l \le x \le r$, and let $u_1$, $u_2$ be solutions of (4), neither identically zero, with $u_1$ satisfying (5) and $u_2$ satisfying (6). Then the three quantities (19) are either all nonzero or all zero, and they are zero exactly when $u_1$ and $u_2$ are proportional.
>
> *Powers: 0.5 (text)*

^lem-7-2

> [!proof]+ Proof
> A solution of (4) that is not identically zero cannot have $u(x_0) = u'(x_0) = 0$ at any point $x_0$: the zero function solves (4) with these initial values, and by uniqueness ([[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|331 Thm. §18.1]]) it would be the only solution. (At an endpoint $x_0 = l$ or $r$, extend $k$, $p$ continuously beyond $[l, r]$, constant beyond the ends; the solution of the extended equation with the same data at an interior point agrees with $u$ on $[l, r]$, so uniqueness applies at the endpoints too.) So the vectors $U_j(x) = \big(u_j(x), u_j'(x)\big)$, $j = 1, 2$, are never $(0, 0)$ on $[l, r]$.
>
> **$W$ vanishes somewhere if and only if $u_1$, $u_2$ are proportional.** If $u_2 = cu_1$, then $W \equiv 0$. Conversely, if $W(x_0) = 0$, the nonzero vectors $U_1(x_0)$, $U_2(x_0)$ are linearly dependent, so $U_2(x_0) = cU_1(x_0)$ for some $c$. Then $u_2 - cu_1$ solves (4) with zero value and derivative at $x_0$, so $u_2 - cu_1 \equiv 0$ by uniqueness. (Powers asserts this; it is also [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-8|331 Thm. §18.8]] together with [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|331 Thm. §18.4]].)
>
> **If $u_1$, $u_2$ are proportional, all three are zero.** Say $u_2 = cu_1$, with $c \ne 0$ since $u_2 \not\equiv 0$. Then $W \equiv 0$; $\alpha u_2(l) - \alpha'u_2'(l) = c\big(\alpha u_1(l) - \alpha'u_1'(l)\big) = 0$ by (5); and $\beta u_1(r) + \beta'u_1'(r) = \frac1c\big(\beta u_2(r) + \beta'u_2'(r)\big) = 0$ by (6).
>
> **If the second or third is zero, $u_1$, $u_2$ are proportional.** Suppose $\alpha u_2(l) - \alpha'u_2'(l) = 0$. Then both $U_1(l)$ and $U_2(l)$ lie in the set $\{(a, b) : \alpha a - \alpha'b = 0\}$, which is a line through the origin because $(\alpha, \alpha') \ne (0, 0)$. Two nonzero vectors on one line are proportional, so $W(l) = 0$, and by the first step $u_1$, $u_2$ are proportional. The third quantity is handled the same way at $x = r$, with the line $\beta a + \beta'b = 0$.
>
> Together: if any one of the three is zero, $u_1$ and $u_2$ are proportional, and then all three are zero.

^pf-7-2

*Uses:* [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|331 Thm. §18.1]] (uniqueness), [[§7★ Green's Functions#^def-7-1|Def. §7.1]]

> [!theorem] Theorem §11.2: Existence and Uniqueness for the Boundary Value Problem
> Let $k(x)$, $p(x)$ and $f(x)$ be continuous, $l \le x \le r$. The boundary value problem
>
> $$
> \frac{d^2u}{dx^2} + k(x)\frac{du}{dx} + p(x)u = f(x), \quad l < x < r, \qquad \alpha u(l) - \alpha'u'(l) = 0 \ \ \text{(i)}, \qquad \beta u(r) + \beta'u'(r) = 0 \ \ \text{(ii)}
> $$
>
> has one and only one solution, unless there is a nontrivial solution of
>
> $$
> \frac{d^2u}{dx^2} + k(x)\frac{du}{dx} + p(x)u = 0, \qquad l < x < r ,
> $$
>
> that satisfies (i) and (ii). When a unique solution exists, it is given by (17) and (18). When the homogeneous problem has a nontrivial solution, the problem has either no solution or infinitely many.
>
> *Powers: 0.5, Theorem*

^thm-7-3

> [!proof]+ Proof
> **Choosing $u_1$ and $u_2$.** (Powers takes their existence for granted.) Extend $k$ and $p$ continuously to an open interval containing $[l, r]$ (constant beyond the ends, say). By [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|331 Thm. §18.1]] there is a solution $u_1$ of (4) with $u_1(l) = \alpha'$, $u_1'(l) = \alpha$, and a solution $u_2$ with $u_2(r) = \beta'$, $u_2'(r) = -\beta$. Then $\alpha u_1(l) - \alpha'u_1'(l) = \alpha\alpha' - \alpha'\alpha = 0$ and $\beta u_2(r) + \beta'u_2'(r) = \beta\beta' - \beta'\beta = 0$, and neither function is identically zero, since $(\alpha', \alpha) \ne (0, 0)$ and $(\beta', -\beta) \ne (0, 0)$.
>
> **If the homogeneous problem has only the zero solution.** Then $u_1$, which satisfies (i), cannot also satisfy (ii), so $\beta u_1(r) + \beta'u_1'(r) \ne 0$. By [[§7★ Green's Functions#^lem-7-2|Lemma §7.2]] all three quantities (19) are nonzero; in particular $u_1$, $u_2$ are independent. [[§7★ Green's Functions#^thm-7-1|Theorem §7.1]] then shows that (18) is a solution. It is the only one: if $u$ and $\tilde u$ are solutions, then $u - \tilde u$ solves the homogeneous equation ([[§3★ Nonhomogeneous Linear Equations#^thm-3-3|Theorem §3.3]]) and, the conditions (i), (ii) being linear and homogeneous, satisfies (i) and (ii); so $u - \tilde u \equiv 0$.
>
> **If the homogeneous problem has a nontrivial solution $\phi$.** If $u$ is a solution of the boundary value problem, then so is $u + c\phi$ for every constant $c$, by the same linearity, and these are all different. So there is never exactly one solution: either there is none, or there are infinitely many. (In this case $u_1$ and $u_2$ are both multiples of $\phi$, and all three quantities (19) are $0$: the construction breaks down.)

^pf-7-3

*Uses:* [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-1|331 Thm. §18.1]], [[§7★ Green's Functions#^lem-7-2|§7.2]], [[§7★ Green's Functions#^thm-7-1|§7.1]], [[§3★ Nonhomogeneous Linear Equations#^thm-3-3|§3.3]]

> [!remark]- Connections
> - This is the infinite-dimensional analogue of a fact about square matrices and operators on a finite-dimensional space: $T$ is surjective (every $f$ has a solution) if and only if it is injective (the null space is $\{0\}$), [[§10 Invertibility and Isomorphisms#^ladr-3-65|LADR 3.65]] with [[§8 Null Spaces and Ranges#^ladr-3-15|LADR 3.15]]. For the boundary value problem, $T$ is $u \mapsto u'' + ku' + pu$ on functions satisfying (i), (ii), and $f \mapsto \int G(\cdot, z)f(z)\,dz$ is its inverse. The general statement for such operators is the Fredholm alternative.

> [!example] Example §10.2: No Solution, or Infinitely Many
> **(a)** The boundary value problem
>
> $$
> \frac{d^2u}{dx^2} + u = -1, \quad 0 < x < \pi, \qquad u(0) = 0, \quad u(\pi) = 0
> $$
>
> does not have a unique solution, by Theorem §7.3, because $u(x) = \sin(x)$ is a nontrivial solution of $u'' + u = 0$, $u(0) = u(\pi) = 0$. Indeed, following the construction gives $u_1(x) = \sin(x)$ and also $u_2(x) = \sin(x)$ (or a multiple), and all three quantities (19) are $0$. Trying the usual method instead: the general solution is $u(x) = -1 + c_1\cos(x) + c_2\sin(x)$, and the boundary conditions lead to the contradictory requirements
>
> $$
> -1 + c_1 = 0 \qquad\text{and}\qquad -1 - c_1 = 0 .
> $$
>
> So there simply is **no solution**.
>
> **(b)** With the inhomogeneity $\pi - 2x$ instead: $u'' + u = \pi - 2x$, $u(0) = u(\pi) = 0$. A particular solution is $u_p = \pi - 2x$, so $u = \pi - 2x + c_1\cos x + c_2\sin x$. Then $u(0) = \pi + c_1 = 0$ gives $c_1 = -\pi$, and $u(\pi) = -\pi - c_1 = 0$ holds automatically. So
>
> $$
> u(x) = \pi - 2x - \pi\cos x + c_2\sin x
> $$
>
> is a solution for every $c_2$: **infinitely many** solutions, uniqueness fails.
>
> **What decides between (a) and (b).** If $u$ solves $u'' + u = f$, $u(0) = u(\pi) = 0$, two integrations by parts give
>
> $$
> \int_0^\pi u''\sin x\,dx = \big[u'\sin x - u\cos x\big]_0^\pi - \int_0^\pi u\sin x\,dx = -\int_0^\pi u\sin x\,dx ,
> $$
>
> so $\int_0^\pi f(x)\sin x\,dx = \int_0^\pi (u'' + u)\sin x\,dx = 0$. A solution can exist only if $f$ is orthogonal to the nontrivial homogeneous solution $\sin x$. In (a), $\int_0^\pi(-1)\sin x\,dx = -2 \ne 0$; in (b), $\int_0^\pi(\pi - 2x)\sin x\,dx = 2\pi - 2\pi = 0$.
>
> *Powers: 0.5, Example (no solution); Exercise 0.5.12*

^ex-7-2

> [!theorem] Corollary §11.3: Forcing at an Eigenvalue
> The boundary value problem
>
> $$
> \frac{d^2u}{dx^2} + \lambda^2u = f(x), \quad 0 < x < a, \qquad u(0) = 0, \quad u(a) = 0 ,
> $$
>
> with $f$ continuous and $\lambda > 0$, has no solution or infinitely many if $\lambda$ is an eigenvalue of $u'' + \lambda^2u = 0$, $u(0) = 0$, $u(a) = 0$, that is, if $\lambda = n\pi/a$; otherwise it has exactly one solution.
>
> *Powers: Exercise 0.5.14*

^cor-7-4

> [!proof]+ Proof
> By [[§5★ Boundary Value Problems#^prop-5-3|Proposition §5.3]], the homogeneous problem has a nontrivial solution, $\sin(n\pi x/a)$, exactly when $\lambda = n\pi/a$. Apply Theorem §7.3.

^pf-7-4

*Uses:* [[§5★ Boundary Value Problems#^prop-5-3|§5.3]], [[§7★ Green's Functions#^thm-7-3|§7.3]]

This is the boundary-value version of resonance ([[§3★ Nonhomogeneous Linear Equations#^ex-3-3|Example §3.3]]): forcing a system at one of its natural modes produces no steady response, or an undetermined one.

## Properties of the Green's Function

> [!theorem] Proposition §7.5: Defining Properties of the Green's Function
> Fix $z$ with $l < z < r$ and let $v(x) = G(x, z)$, with $G$ as in (17). Then:
> - (i) $v$ satisfies the boundary conditions (2) and (3) at $x = l$ and $x = r$;
> - (ii) $v$ is continuous for $l < x < r$, including at $x = z$;
> - (iii) $v'$ is discontinuous at $x = z$, and
>
> $$
> \lim_{h \to 0^+}\big(v'(z + h) - v'(z - h)\big) = 1 ;
> $$
>
> - (iv) $v$ satisfies the differential equation $v'' + k(x)v' + p(x)v = 0$ for $l < x < z$ and for $z < x < r$.
>
> Conversely, if $u_1$, $u_2$ are independent, $G(\cdot, z)$ is the only function with these four properties. They are therefore sometimes used to define the Green's function.
>
> *Powers: Exercise 0.5.13*

^prop-7-5

> [!proof]+ Proof
> For $x < z$, (17) gives $v(x) = \frac{u_2(z)}{W(z)}u_1(x)$, a constant multiple of $u_1$; for $x > z$, $v(x) = \frac{u_1(z)}{W(z)}u_2(x)$, a constant multiple of $u_2$.
>
> **(iv)** Constant multiples of solutions of (4) are solutions.
>
> **(i)** Near $x = l$ we have $x < z$, so $v$ is a multiple of $u_1$, which satisfies (2) by (5); near $x = r$, $v$ is a multiple of $u_2$, which satisfies (3) by (6).
>
> **(ii)** Both formulas give $v(z) = u_1(z)u_2(z)/W(z)$ at $x = z$, and each is continuous on its side.
>
> **(iii)** As $h \to 0^+$, $v'(z + h) = \frac{u_1(z)}{W(z)}u_2'(z + h) \to \frac{u_1(z)u_2'(z)}{W(z)}$ and $v'(z - h) = \frac{u_2(z)}{W(z)}u_1'(z - h) \to \frac{u_2(z)u_1'(z)}{W(z)}$, so the jump is
>
> $$
> \frac{u_1(z)u_2'(z) - u_2(z)u_1'(z)}{W(z)} = \frac{W(z)}{W(z)} = 1 .
> $$
>
> **Conversely** (not in Powers), let $w$ have properties (i)–(iv). On $l < x < z$, $w$ solves (4) and satisfies (2), so $\big(w(l), w'(l)\big)$ and $\big(u_1(l), u_1'(l)\big)$ lie on the line $\alpha a - \alpha'b = 0$. This line is spanned by the nonzero vector $\big(u_1(l), u_1'(l)\big)$, so $\big(w(l), w'(l)\big) = A\big(u_1(l), u_1'(l)\big)$ for a constant $A$, and $w - Au_1$ solves (4) with zero data at $l$; as in the proof of [[§7★ Green's Functions#^lem-7-2|Lemma §7.2]], uniqueness gives $w = Au_1$ there. Likewise $w = Bu_2$ on $z < x < r$. Continuity and the jump condition at $z$ give
>
> $$
> Au_1(z) - Bu_2(z) = 0, \qquad Bu_2'(z) - Au_1'(z) = 1 ,
> $$
>
> a linear system for $A$, $B$ with determinant $u_1(z)u_2'(z) - \big(-u_2(z)\big)\big(-u_1'(z)\big) = W(z) \ne 0$. Its unique solution is $A = u_2(z)/W(z)$, $B = u_1(z)/W(z)$ (substitute), so $w = G(\cdot, z)$.

^pf-7-5

*Uses:* [[§7★ Green's Functions#^def-7-2|Def. §7.2]], [[§7★ Green's Functions#^lem-7-2|§7.2]]

> [!remark]- Connections
> - In two and three dimensions the response of $\nabla^2u$ to a point source is the fundamental solution $C\ln r$ in the plane, [[§29 Conservation of Mass and Laplace's Equation#^thm-29-2|452 Thm. §29.2]], or $C/r$ in space, [[§33 The Laplacian in Spherical Coordinates#^rem-33-2|452 Remark: Verification: Radial Functions]]; Green's functions of the Laplacian on bounded regions are built from these together with Green's identities, [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|452 Thm. §28.3]].

> [!remark] Remark: The Green's Function as Response to a Point Source
> Properties (i)–(iv) say that $G(\cdot, z)$ is what the system does when the whole inhomogeneity is concentrated at the single point $z$ with total strength $1$. For example, for a cable or string under tension ([[§5★ Boundary Value Problems#^prop-5-1|Proposition §5.1]], $Tu'' = f$), a load concentrated at $z$ leaves the string straight on both sides of $z$, while the force balance at $z$ puts a corner there, a jump in the slope proportional to the load (Example §7.3). Since $f$ is a superposition of point sources $f(z)\,dz$ at all points $z$, linearity gives $u(x) = \int_l^r G(x, z)f(z)\,dz$. In physics notation, $G$ solves $LG = \delta(x - z)$ with the homogeneous boundary conditions, $\delta$ being the Dirac delta; the jump condition (iii) is what integrating $G'' = \delta$ across $z$ gives.

^rem-7-1

> [!remark] Remark: Method — Constructing a Green's Function
> To solve $u'' + k(x)u' + p(x)u = f(x)$ on $l < x < r$ with homogeneous conditions at both ends:
> 1. Put the equation in the form (1), with coefficient $1$ on $u''$; the Wronskian in (17) refers to this form.
> 2. Find a nonzero solution $u_1$ of the homogeneous equation that satisfies the left boundary condition (or, at a singular left end, is bounded there; on $-\infty < x$, is bounded as $x \to -\infty$).
> 3. Find a nonzero solution $u_2$ that satisfies the right boundary condition (or the corresponding boundedness condition).
> 4. Compute $W(z) = u_1(z)u_2'(z) - u_2(z)u_1'(z)$. If $W \equiv 0$, $u_1$ and $u_2$ are proportional, the homogeneous problem has a nontrivial solution, and there is no Green's function (Theorem §7.3).
> 5. Write down $G$ by (17): $u_1$ at the smaller of $x, z$, $u_2$ at the larger, over $W(z)$.
> 6. Compute $u(x) = \int_l^r G(x, z)f(z)\,dz$, breaking the integral at $z = x$ as in (16).
>
> Alternatively, in steps 4–5, write $G = A(z)u_1(x)$ for $x < z$ and $G = B(z)u_2(x)$ for $x > z$ and determine $A$, $B$ from continuity at $x = z$ and the unit jump in $\partial_xG$ (Proposition §7.5).

^rem-7-2

> [!example] Example §11.1: The Green's Function of u″ = f
> Find the Green's function for $u'' = f(x)$, $0 < x < a$, $u(0) = 0$, $u(a) = 0$, and use it for $f = 1$.
>
> **Solutions.** The homogeneous solutions are $c_1 + c_2x$. Take $u_1 = x$ ($u_1(0) = 0$) and $u_2 = x - a$ ($u_2(a) = 0$).
>
> **By the properties.** Write $G = A\,x$ for $x \le z$ and $G = B\,(x - a)$ for $x \ge z$. Continuity at $x = z$: $Az = B(z - a)$. Unit jump in slope: $B - A = 1$. Substituting $B = A + 1$: $Az = (A + 1)(z - a)$, so $Aa = z - a$, $A = \frac{z - a}a$ and $B = \frac za$:
>
> $$
> G(x, z) = \begin{cases} \dfrac{z(x - a)}{a}, & 0 < z \le x, \\[2ex] \dfrac{x(z - a)}{a}, & x \le z < a. \end{cases}
> $$
>
> The formula (17) gives the same: $W = x\cdot1 - (x - a)\cdot1 = a$, and $u_1(z)u_2(x)/W = z(x - a)/a$ for $z \le x$.
>
> **For $f = 1$.**
>
> $$
> u(x) = \int_0^x \frac{z(x - a)}{a}\,dz + \int_x^a \frac{x(z - a)}{a}\,dz = \frac{(x - a)x^2}{2a} - \frac{x(a - x)^2}{2a} = \frac{x(x - a)}{2a}\big(x - (x - a)\big) = \frac{x(x - a)}2 ,
> $$
>
> and indeed $u'' = 1$, $u(0) = u(a) = 0$. As a function of $x$, $G(x, z)$ is the triangle with vertices $(0, 0)$, $\big(z, z(z - a)/a\big)$, $(a, 0)$: the shape of a taut string ($Tu'' = f$ with $T = 1$, [[§5★ Boundary Value Problems#^prop-5-1|Proposition §5.1]]) under a unit point load at $z$.
>
> *Powers: Exercise 0.5.1*

^ex-7-3

## Singular Endpoints and Infinite Intervals

If the differential equation (1) has a singular point at $x = l$ or $x = r$ (or both), a Green's function may still be constructed: the boundary condition (2) or (3) is replaced by a boundedness condition ([[§6★ Singular Boundary Value Problems#^def-6-2|Definition §6.2]]), which then also applies to $u_1$ or $u_2$. A similar procedure is followed if the interval is infinite in length ([[§6★ Singular Boundary Value Problems#^def-6-4|Definition §6.4]]).

> [!example] Example §11.2: A Singular Endpoint
> Construct the Green's function for
>
> $$
> \frac1x\frac{d}{dx}\Big(x\frac{du}{dx}\Big) = f(x), \quad 0 < x < 1, \qquad u(0) \text{ bounded}, \quad u(1) = 0 .
> $$
>
> **Standard form.** The equation is $u'' + \frac1xu' = f$, with $k = 1/x$ singular at $x = 0$ ([[§6★ Singular Boundary Value Problems#^ex-6-1|Example §6.1]](b)).
>
> **Solutions.** The homogeneous equation has the general solution $u = c_1 + c_2\ln(x)$ ([[§2★ Variable Coefficients and Higher-Order Equations#^ex-2-1|Example §2.1]](c)). Choose $u_1(x) = 1$, bounded at $x = 0$, and $u_2(x) = \ln(x)$, which is $0$ at $x = 1$. Their Wronskian is $W(z) = 1\cdot\frac1z - \ln(z)\cdot0 = \frac1z$.
>
> **Green's function.** By (17),
>
> $$
> G(x, z) = \begin{cases} z\ln(x), & 0 < z \le x, \\ z\ln(z), & x \le z < 1. \end{cases}
> $$
>
> **Check with $f = 1$.** By (16),
>
> $$
> u(x) = \int_0^x z\ln(x)\,dz + \int_x^1 z\ln(z)\,dz = \frac{x^2}2\ln x + \Big[\frac{z^2}{2}\ln z - \frac{z^2}4\Big]_x^1 = \frac{x^2 - 1}{4} .
> $$
>
> This is the radial heat flow solution (4) of [[§6★ Singular Boundary Value Problems#^ex-6-2|Example §6.2]] with $H = -1$, $c = 1$, $T = 0$, as it should be: $\frac1x(x\cdot\frac x2)' = 1$, and $u$ is bounded with $u(1) = 0$.
>
> *Powers: 0.5, Example (singular point)*

^ex-7-4

> [!example] Example §11.3: The Whole Line
> Find the Green's function for
>
> $$
> \frac{d^2u}{dx^2} - \gamma^2u = f(x), \quad -\infty < x < \infty, \qquad u(x) \text{ bounded as } x \to \pm\infty \quad (\gamma > 0),
> $$
>
> and use it to solve the problem with $f = -\gamma^2$.
>
> **Solutions.** By [[§6★ Singular Boundary Value Problems#^prop-6-1|Proposition §6.1]] the homogeneous solution bounded as $x \to -\infty$ is $u_1 = e^{\gamma x}$, and the one bounded as $x \to +\infty$ is $u_2 = e^{-\gamma x}$. Their Wronskian is $W = e^{\gamma x}(-\gamma e^{-\gamma x}) - e^{-\gamma x}(\gamma e^{\gamma x}) = -2\gamma$.
>
> **Green's function.** By (17), $G = e^{\gamma z}e^{-\gamma x}/(-2\gamma)$ for $z \le x$ and $e^{\gamma x}e^{-\gamma z}/(-2\gamma)$ for $x \le z$, that is,
>
> $$
> G(x, z) = -\frac{1}{2\gamma}e^{-\gamma|x - z|} .
> $$
>
> It depends only on $x - z$ (the problem is unchanged by translation) and decays on both sides of the source.
>
> **For $f = -\gamma^2$.**
>
> $$
> u(x) = \int_{-\infty}^{\infty} -\frac{1}{2\gamma}e^{-\gamma|x - z|}\,(-\gamma^2)\,dz = \frac\gamma2\int_{-\infty}^{\infty}e^{-\gamma|s|}\,ds = \frac\gamma2\cdot\frac2\gamma = 1 .
> $$
>
> Directly: the general solution is $u = 1 + c_1e^{\gamma x} + c_2e^{-\gamma x}$, and boundedness at $\pm\infty$ forces $c_1 = c_2 = 0$, so $u = 1$. (Powers states that the construction carries over to infinite intervals; for bounded continuous $f$ the integrals converge, and the proof of Theorem §7.1 goes through with the boundary conditions replaced by boundedness.)
>
> *Powers: Exercises 0.5.8 and 0.5.10*

^ex-7-5
