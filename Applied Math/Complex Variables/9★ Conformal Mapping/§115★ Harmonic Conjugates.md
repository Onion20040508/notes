---
type: section
subject: "[[Complex Variables]]"
chapter: 9
section: 115
bc: "115"
aliases: ["B&C 115"]
tags: [complex-variables, math342, extension]
---
← [[§114★ Local Inverses]] · ↑ [[· 9★ Conformal Mapping]] · [[§116★ Transformations of Harmonic Functions]] →

*Brown–Churchill, Section 115.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The real and imaginary parts of an analytic function are harmonic ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]); this section goes the other way. A harmonic function $v$ whose first partials are tied to those of $u$ by the Cauchy–Riemann equations is a *harmonic conjugate* of $u$, and $u + iv$ is then analytic. On a simply connected domain every harmonic function has a harmonic conjugate, built as a line integral, so every harmonic function there is the real part of an analytic function. This is what makes the complex methods of Chapter 10 possible: a steady temperature, an electrostatic potential or a velocity potential is the real part of an analytic function, and the conjugate gives the heat-flow lines, the field lines or the streamlines.

## Harmonic Conjugates

Recall ([[§27★ Harmonic Functions#^def-27-1|Definition §27.1]]) that a real-valued function is **harmonic** in a domain $D$ if it has continuous partial derivatives of the first and second order in $D$ and satisfies Laplace's equation there, and that if $f(z) = u(x, y) + iv(x, y)$ is analytic in $D$, then
$$
u_{xx} + u_{yy} = 0, \qquad v_{xx} + v_{yy} = 0 \qquad (1)
$$
in $D$ ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]).

> [!definition] Definition §115.1: Harmonic Conjugate
> Suppose that $u(x, y)$ and $v(x, y)$ are harmonic in a domain $D$ and that their first-order partial derivatives satisfy the Cauchy–Riemann equations
>
> $$
> u_x = v_y, \qquad u_y = -v_x \qquad (2)
> $$
>
> throughout $D$. Then $v$ is a **harmonic conjugate** of $u$. (The word *conjugate* here has nothing to do with the conjugate $\bar z$ of [[§6 Complex Conjugates#^def-6-1|Definition §6.1]].)
>
> *B&C: Sec. 115 (text)*

^def-115-1

> [!remark]- Connections
> - Harmonic functions and the Laplacian: [[§35 Potential Equation#^def-35-1|341 Def. §35.1]], and in $\mathbb{R}^n$, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|452 Def. §17.2]].

> [!theorem] Theorem §115.1: Analytic Functions and Harmonic Conjugates
> A function $f(z) = u(x, y) + iv(x, y)$ is analytic in a domain $D$ if and only if $v$ is a harmonic conjugate of $u$.
>
> *B&C: Sec. 115, Theorem*

^thm-115-1

> [!proof]+ Proof
> If $v$ is a harmonic conjugate of $u$ in $D$, the Cauchy–Riemann equations (2) hold in $D$, and the first partials of $u$ and $v$ are continuous there (being harmonic, $u$ and $v$ have continuous partials of the first and second order). By the sufficient conditions of [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]], $f$ is differentiable at each point of the open set $D$, that is, analytic in $D$.
>
> Conversely, if $f$ is analytic in $D$, then $u$ and $v$ are harmonic in $D$ ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]), and the Cauchy–Riemann equations (2) hold in $D$ ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]). So $v$ is a harmonic conjugate of $u$.

^pf-115-1

*Uses:* [[§115★ Harmonic Conjugates#^def-115-1|Def. §115.1]], [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]]

The relation is not symmetric: if $v$ is a harmonic conjugate of $u$, then $u$ need not be one of $v$.

> [!example] Example §115.1: v Is a Conjugate of u but Not Conversely
> Let $u(x, y) = x^2 - y^2$ and $v(x, y) = 2xy$, the real and imaginary parts of the entire function $f(z) = z^2$. By Theorem §115.1, $v$ is a harmonic conjugate of $u$ throughout the plane.
>
> But $u$ is not a harmonic conjugate of $v$ in any domain, since $F = 2xy + i(x^2 - y^2)$ is not analytic anywhere ([[§26 Further Examples (Analytic Functions)|§26]], Exercise 2(b)). Indeed, with $U = 2xy$ and $V = x^2 - y^2$,
>
> $$
> U_x = 2y, \quad V_y = -2y, \qquad U_y = 2x, \quad -V_x = -2x ,
> $$
>
> so $U_x = V_y$ only where $y = 0$ and $U_y = -V_x$ only where $x = 0$. Both hold only at the origin, and no neighborhood of a point is contained in the set where they hold. (In fact $-u$ is a harmonic conjugate of $v$: $v - iu = -i(u + iv) = -iz^2$ is entire. Compare B&C Exercises 3 and 4.)
>
> *B&C: Sec. 115, Example 1*

^ex-115-1

> [!remark] Remark: Method — Finding a Harmonic Conjugate
> Given $u$ harmonic in $D$:
> 1. **Check** that $u_{xx} + u_{yy} = 0$.
> 2. **Integrate the first Cauchy–Riemann equation** $v_y = u_x$ with respect to $y$, holding $x$ fixed: $v = \int u_x\,dy + g(x)$, with $g$ an unknown function of $x$.
> 3. **Use the second equation** $v_x = -u_y$ to get $g'(x)$, and integrate: $g(x) = \cdots + C$.
> 4. **Optionally write $f = u + iv$ in terms of $z$**: setting $y = 0$ gives $f(x)$, which suggests $f(z)$ (replace $x$ by $z$); check by expanding.
>
> Alternatively, evaluate the line integral (9) of Theorem §115.4 along a horizontal and then a vertical segment (Example §115.3). By Proposition §115.2 the answer is unique up to the constant $C$, customarily taken to be $0$.

^rem-115-1

> [!example] Example §115.2: A Conjugate of 2x(1 − y)
> The function
>
> $$
> u(x, y) = 2x(1 - y) = 2x - 2xy \qquad (3)
> $$
>
> is harmonic throughout the $xy$ plane: $u_{xx} = 0$, $u_{yy} = 0$. Find a harmonic conjugate.
>
> The first Cauchy–Riemann equation $u_x = v_y$ says $v_y(x, y) = 2 - 2y$. Holding $x$ fixed and integrating with respect to $y$,
>
> $$
> v(x, y) = 2y - y^2 + g(x), \qquad (4)
> $$
>
> where $g$ is, at present, an arbitrary differentiable function of $x$. The second equation $u_y = -v_x$ gives $-2x = -g'(x)$, so $g'(x) = 2x$ and $g(x) = x^2 + C$, $C$ an arbitrary real number. By (4),
>
> $$
> v(x, y) = 2y - y^2 + x^2 + C \qquad (5)
> $$
>
> is a harmonic conjugate of $u$, and the corresponding analytic function is
>
> $$
> f(z) = 2x(1 - y) + i(2y - y^2 + x^2 + C) . \qquad (6)
> $$
>
> Setting $y = 0$ in (6) gives $f(x) = 2x + i(x^2 + C)$, which suggests $f(z) = 2z + i(z^2 + C)$. Check: $2z + iz^2 = 2x + 2iy + i(x^2 - y^2) - 2xy = (2x - 2xy) + i(2y + x^2 - y^2)$. By Proposition §115.2 below, $v$ is unique up to the additive constant, and it is customary to take $C = 0$: $f(z) = 2z + iz^2$.
>
> *B&C: Sec. 115, Example 2*

^ex-115-2

> [!theorem] Proposition §115.2: Harmonic Conjugates Differ by a Constant
> If $v$ and $V$ are harmonic conjugates of $u(x, y)$ in a domain $D$, then $v(x, y)$ and $V(x, y)$ differ by at most an additive real constant.
>
> *B&C: Sec. 115, Exercise 5*

^prop-115-2

> [!proof]+ Proof
> By Theorem §115.1, $f_1 = u + iv$ and $f_2 = u + iV$ are analytic in $D$, hence so is $F = f_1 - f_2 = i(v - V)$, whose real part is $0$ and imaginary part is $v - V$. By the formula $F' = U_x + iV_x$ for $F = U + iV$ ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]) and the Cauchy–Riemann equations for both pairs,
>
> $$
> F'(z) = i(v_x - V_x) = i\big(-u_y - (-u_y)\big) = 0
> $$
>
> throughout $D$. A function whose derivative vanishes throughout a domain is constant ([[§25 Analytic Functions#^thm-25-3|Theorem §25.3]]). So $v - V$ is constant in $D$.

^pf-115-2

*Uses:* [[§115★ Harmonic Conjugates#^thm-115-1|§115.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§25 Analytic Functions#^thm-25-3|§25.3]]

## Existence on Simply Connected Domains

The proof that conjugates exist rests on a fact about line integrals from advanced calculus.

> [!theorem] Lemma §115.3: Path Independence on a Simply Connected Domain
> Suppose that $P(x, y)$ and $Q(x, y)$ have continuous first-order partial derivatives in a simply connected domain $D$ of the $xy$ plane, and that $P_y = Q_x$ everywhere in $D$. Then for any two points $(x_0, y_0)$ and $(x, y)$ of $D$ the line integral
>
> $$
> \int_C P(s, t)\,ds + Q(s, t)\,dt
> $$
>
> from $(x_0, y_0)$ to $(x, y)$ is independent of the contour $C$ in $D$. When $(x_0, y_0)$ is fixed and $(x, y)$ varies through $D$, it defines a single-valued function
>
> $$
> F(x, y) = \int_{(x_0, y_0)}^{(x, y)} P(s, t)\,ds + Q(s, t)\,dt \qquad (7)
> $$
>
> with
>
> $$
> F_x(x, y) = P(x, y), \qquad F_y(x, y) = Q(x, y) . \qquad (8)
> $$
>
> A different starting point $(x_0, y_0)$ changes $F$ by an additive constant.
>
> *B&C: Sec. 115 (text)*

^lem-115-3

*B&C omits the proof (it cites Kaplan, Advanced Mathematics for Engineers); see [[§110 Green's Theorem#^thm-110-5|Calc Thm. §110.5]] (the field $P\,\mathbf i + Q\,\mathbf j$ is conservative) and [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Calc Thm. §109.3]] (the potential is the line integral (7), with gradient (8)).*

> [!theorem] Theorem §115.4: Existence of Harmonic Conjugates
> If a harmonic function $u(x, y)$ is defined on a simply connected domain $D$, it always has a harmonic conjugate $v(x, y)$ in $D$. Consequently every harmonic function on a simply connected domain is the real part of an analytic function. Explicitly, for any fixed point $(x_0, y_0)$ of $D$,
>
> $$
> v(x, y) = \int_{(x_0, y_0)}^{(x, y)} -u_t(s, t)\,ds + u_s(s, t)\,dt \qquad (9)
> $$
>
> is a harmonic conjugate of $u$; every other one is $v + C$.
>
> *B&C: Sec. 115, Theorem*

^thm-115-4

> [!proof]+ Proof
> Take $P = -u_y$ and $Q = u_x$ in Lemma §115.3. Laplace's equation $u_{xx} + u_{yy} = 0$ says
>
> $$
> (-u_y)_y = (u_x)_x
> $$
>
> everywhere in $D$, that is, $P_y = Q_x$. The second-order partials of $u$ are continuous in $D$, so the first-order partials of $P = -u_y$ and $Q = u_x$ are continuous there. Hence the function $v$ in (9) is well defined for all $(x, y)$ in $D$, and by (8)
>
> $$
> v_x(x, y) = -u_y(x, y), \qquad v_y(x, y) = u_x(x, y) . \qquad (10)
> $$
>
> These are the Cauchy–Riemann equations. Since the first partials of $u$ are continuous, (10) shows that those of $v$ are continuous too, so $u + iv$ is analytic in $D$ ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]). Then $v$ is harmonic ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]), and $v$ is a harmonic conjugate of $u$ (Theorem §115.1). Any $v + C$, $C$ a real constant, is also one, and by Proposition §115.2 there are no others.

^pf-115-4

*Uses:* [[§115★ Harmonic Conjugates#^lem-115-3|§115.3]], [[§115★ Harmonic Conjugates#^thm-115-1|§115.1]], [[§115★ Harmonic Conjugates#^prop-115-2|§115.2]], [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]], [[§52 Simply Connected Domains#^def-52-1|Def. §52.1]], [[§110 Green's Theorem#^thm-110-5|Calc Thm. §110.5]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Calc Thm. §109.3]]

> [!remark]- Connections
> - In vector language, (9) says that $(-u_y, u_x)$, the gradient of $u$ turned through $+\pi/2$, is a conservative field on $D$, and $v$ is its potential: [[§110 Green's Theorem#^thm-110-5|Calc Thm. §110.5]] (test for conservative fields on simply connected regions) and [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Calc Thm. §109.3]]. In the language of forms, $-u_y\,dx + u_x\,dy$ is closed exactly when $u$ is harmonic, and the conjugate exists when it is exact: [[Poincaré Lemma|452 Poincaré Lemma]].
> - A second proof inside complex analysis: $g = u_x - iu_y$ satisfies the Cauchy–Riemann equations (they are $u_{xx} = -u_{yy}$ and $u_{xy} = u_{yx}$), so it is analytic in $D$; on a simply connected domain it has an antiderivative $G$ ([[§52 Simply Connected Domains#^cor-52-2|Corollary §52.2]]); then $G' = (\operatorname{Re}G)_x - i(\operatorname{Re}G)_y = u_x - iu_y$, so $\operatorname{Re}G = u + c$, and $G - c = u + iv$.

> [!example] Example §115.3: The Conjugate of 2x − 2xy by a Line Integral
> For $u(x, y) = 2x - 2xy$ (Example §115.2), $-u_t(s, t) = 2s$ and $u_s(s, t) = 2 - 2t$, so by (9) with $(x_0, y_0) = (0, 0)$
>
> $$
> v(x, y) = \int_{(0,0)}^{(x, y)} 2s\,ds + (2 - 2t)\,dt
> $$
>
> is a harmonic conjugate of $u$ in the whole plane. Integrate first along the horizontal segment from $(0, 0)$ to $(x, 0)$, where $t = 0$ and $dt = 0$, then along the vertical segment from $(x, 0)$ to $(x, y)$, where $s = x$ and $ds = 0$:
>
> $$
> v(x, y) = \int_0^x 2s\,ds + \int_0^y (2 - 2t)\,dt = x^2 + (2y - y^2) .
> $$
>
> (By inspection: $2s\,ds + (2 - 2t)\,dt$ is the differential of $s^2 + 2t - t^2$.) This is (5) with $C = 0$.
>
> *B&C: Sec. 115, Example 3*

^ex-115-3

> [!example] Example §115.4: ln r Needs a Simply Connected Domain
> **(a)** Show that $u(r, \theta) = \ln r$ is harmonic in the domain $r > 0$, $0 < \theta < 2\pi$, and find its harmonic conjugate there.
>
> The polar form of Laplace's equation ([[§27★ Harmonic Functions|§27]], Exercise 1) is $u_{rr} + \frac1ru_r + \frac{1}{r^2}u_{\theta\theta} = 0$. For $u = \ln r$: $u_{rr} = -1/r^2$, $\frac1ru_r = 1/r^2$, $u_{\theta\theta} = 0$, so the sum is $0$. The Cauchy–Riemann equations in polar form ([[§24★ Polar Coordinates#^prop-24-1|Proposition §24.1]]), $ru_r = v_\theta$ and $u_\theta = -rv_r$, give $v_\theta = r \cdot \frac1r = 1$ and $v_r = 0$, so $v = \theta + C$. Take $v(r, \theta) = \theta$: then $u + iv = \ln r + i\theta$ is the branch $\log z$ $(0 < \theta < 2\pi)$ of [[§33 Branches and Derivatives of Logarithms#^def-33-1|Definition §33.1]].
>
> **(b)** Show that $u = \ln|z| = \frac12\ln(x^2 + y^2)$, which is harmonic in the punctured plane $z \ne 0$, has no harmonic conjugate there. So Theorem §115.4 fails without simple connectivity.
>
> Suppose $v$ were one. Then $f = u + iv$ would be analytic in $z \ne 0$, with
>
> $$
> f'(z) = u_x - iu_y = \frac{x}{x^2 + y^2} - i\frac{y}{x^2 + y^2} = \frac{\bar z}{|z|^2} = \frac1z .
> $$
>
> So $1/z$ would have the antiderivative $f$ in $z \ne 0$, and its integral around the circle $|z| = 1$ would be $0$ ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]). But $\int_{|z| = 1}\frac{dz}{z} = \int_0^{2\pi}\frac{ie^{i\theta}}{e^{i\theta}}\,d\theta = 2\pi i \ne 0$. (The would-be conjugate is $\arg z$, which increases by $2\pi$ around the origin.)
>
> *B&C: Sec. 115, Exercise 6 (part (a)); part (b) is added*

^ex-115-4
