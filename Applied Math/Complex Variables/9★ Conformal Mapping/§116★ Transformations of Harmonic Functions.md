---
type: section
subject: "[[Complex Variables]]"
chapter: 9
section: 116
bc: "116"
aliases: ["B&C 116"]
tags: [complex-variables, math342, extension]
---
← [[§115★ Harmonic Conjugates]] · ↑ [[· 9★ Conformal Mapping]] · [[§117★ Transformations of Boundary Conditions]] →

*Brown–Churchill, Section 116 (with Exercises 1, 2, 8 and 9 of Section 117).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Boundary value problems for Laplace's equation (Dirichlet and Neumann problems) are central in applied mathematics: steady temperatures, electrostatic potentials and ideal fluid flows all lead to them. The key fact of this section is that harmonic functions stay harmonic under a change of variables by an analytic map: if $h(u, v)$ is harmonic in the $w$ plane and $w = f(z)$ is analytic, then $h(u(x, y), v(x, y))$ is harmonic in the $z$ plane. So a problem on a complicated region can be moved by an analytic map to a simple region (a half plane, a strip, a disk), solved there, and brought back. Two proofs are given: B&C's, via harmonic conjugates, and a direct chain-rule computation showing $\nabla^2_{xy}H = |f'(z)|^2\,\nabla^2_{uv}h$, which also covers Poisson's equation.

## Boundary Value Problems

> [!definition] Definition §116.1: Boundary Value Problem
> The problem of finding a function that is harmonic in a specified domain and satisfies prescribed conditions on the boundary of the domain is a **boundary value problem**.
>
> *B&C: Sec. 116 (text)*

^def-116-1

> [!definition] Definition §116.2: Dirichlet Problem
> If, in a [[§116★ Transformations of Harmonic Functions#^def-116-1|boundary value problem]], the values of the function are prescribed along the boundary, it is a **boundary value problem of the first kind**, or a **Dirichlet problem**.
>
> *B&C: Sec. 116 (text)*

^def-116-new1

> [!definition] Definition §116.3: Neumann Problem
> If, in a [[§116★ Transformations of Harmonic Functions#^def-116-1|boundary value problem]], the values of the normal derivative of the function are prescribed on the boundary, it is a **boundary value problem of the second kind**, or a **Neumann problem**. Modifications and combinations of these types of boundary conditions ([[§116★ Transformations of Harmonic Functions#^def-116-new1|Dirichlet]] and Neumann) also arise.
>
> *B&C: Sec. 116 (text)*

^def-116-new2

> [!remark]- Connections
> - The same definitions, with the normal derivative and the mixed (Robin) condition, solved by separation of variables in rectangles and disks: [[§35 Potential Equation#^def-35-2|341 Def. §35.2]]; uniqueness of the Dirichlet solution by the maximum principle, [[§39 Potential in a Disk#^cor-39-6|341 Cor. §39.6]], and non-uniqueness for Neumann, [[§35 Potential Equation#^prop-35-1|341 Prop. §35.1]].

The domains most frequently met in applications are simply connected, and a harmonic function on a simply connected domain has a harmonic conjugate ([[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]]). So solutions of boundary value problems on such domains are real or imaginary parts of analytic functions.

> [!example] Example §116.1: A Steady Temperature as the Real Part of an Entire Function
> In [[§27★ Harmonic Functions#^ex-27-1|Example §27.1]], $T(x, y) = e^{-y}\sin x$ was seen to satisfy the Dirichlet problem
>
> $$
> T_{xx} + T_{yy} = 0 \quad (0 < x < \pi,\ y > 0), \qquad T(0, y) = T(\pi, y) = 0, \qquad T(x, 0) = \sin x ,
> $$
>
> with $T$ bounded: the steady temperature in a semi-infinite strip whose edges are kept at $0$ and whose base is kept at $\sin x$. Identify $T$ as the real part of an entire function.
>
> With $e^{iz} = e^{ix - y} = e^{-y}(\cos x + i\sin x)$,
>
> $$
> -ie^{iz} = e^{-y}\sin x - ie^{-y}\cos x ,
> $$
>
> so $T = \operatorname{Re}(-ie^{iz})$; it is also $\operatorname{Im}(e^{iz})$. Hence $T$ is harmonic throughout the $xy$ plane, not only in the strip, and $-e^{-y}\cos x$ is a harmonic conjugate.
>
> *B&C: Sec. 116, Example 1*

^ex-116-1

*Chain: the temperature $e^{-y}\sin x$ earlier in [[§27★ Harmonic Functions#^ex-27-1|Chapter 2]] · later in [[§118★ Steady Temperatures#^ex-118-3|Chapter 10]]*

Recognizing a solution as the real or imaginary part of a familiar analytic function works only for simple problems. The following theorem is the general tool.

## Harmonic Functions Under Analytic Maps

> [!theorem] Theorem §116.1: Harmonic Functions Stay Harmonic Under Analytic Maps
> Suppose that
>
> **(a)** an analytic function $w = f(z) = u(x, y) + iv(x, y)$ maps a domain $D_z$ in the $z$ plane onto a domain $D_w$ in the $w$ plane;
>
> **(b)** $h(u, v)$ is a harmonic function defined on $D_w$.
>
> Then the function
>
> $$
> H(x, y) = h\big[u(x, y), v(x, y)\big]
> $$
>
> is harmonic in $D_z$.
>
> *B&C: Sec. 116, Theorem*

^thm-116-1

> [!proof]+ Proof
> **$D_w$ simply connected.** Then $h$ has a harmonic conjugate $g(u, v)$ in $D_w$ ([[§115★ Harmonic Conjugates#^thm-115-4|Theorem §115.4]]). So
>
> $$
> \Phi(w) = h(u, v) + ig(u, v) \qquad (1)
> $$
>
> is analytic in $D_w$ ([[§115★ Harmonic Conjugates#^thm-115-1|Theorem §115.1]]). Since $f$ is analytic in $D_z$ with values in $D_w$, the composite $\Phi[f(z)]$ is analytic in $D_z$ (chain rule, [[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]). Its real part $h[u(x, y), v(x, y)] = H(x, y)$ is therefore harmonic in $D_z$ ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]).
>
> **$D_w$ arbitrary.** Each point $w_0$ of $D_w$ has a neighborhood $|w - w_0| < \varepsilon$ lying in $D_w$. A disk is simply connected, so a function $\Phi$ of the type (1) is analytic in it. Let $z_0$ be a point of $D_z$ with $f(z_0) = w_0$. Since $f$ is continuous at $z_0$, there is a neighborhood $|z - z_0| < \delta$ whose image lies in $|w - w_0| < \varepsilon$. So $\Phi[f(z)]$ is analytic in $|z - z_0| < \delta$, and $H$ is harmonic there. Every point $z_0$ of $D_z$ is mapped to some point $w_0$ of $D_w$, so this applies around every point of $D_z$; being harmonic is a local property (continuous second partials and $H_{xx} + H_{yy} = 0$ at each point), so $H$ is harmonic throughout $D_z$.

^pf-116-1

*Uses:* [[§115★ Harmonic Conjugates#^thm-115-4|§115.4]], [[§115★ Harmonic Conjugates#^thm-115-1|§115.1]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]] (chain rule), [[§27★ Harmonic Functions#^thm-27-1|§27.1]], [[§19 Derivatives#^thm-19-1|§19.1]] (differentiable implies continuous)

> [!remark] Remark: Onto Is Not Needed
> The proof uses only that $f$ maps $D_z$ *into* $D_w$, so that $h$ is defined at every $f(z)$. The word "onto" in (a) matters only for the boundary value problems of Chapter 10, where all of $D_w$ must correspond to $D_z$ so that the boundary conditions can be transferred.

^rem-116-1

The theorem can also be proved directly by the chain rule for partial derivatives, without harmonic conjugates; the computation gives more.

> [!theorem] Proposition §116.2: The Laplacian Under an Analytic Change of Variables
> Suppose that an analytic function $w = f(z) = u(x, y) + iv(x, y)$ maps a domain $D_z$ onto a domain $D_w$, and that $h(u, v)$ has continuous partial derivatives of the first and second order on $D_w$. If $H(x, y) = h[u(x, y), v(x, y)]$, then
>
> $$
> H_{xx}(x, y) + H_{yy}(x, y) = \big[h_{uu}(u, v) + h_{vv}(u, v)\big]\,|f'(z)|^2 .
> $$
>
> In particular $H$ is harmonic in $D_z$ when $h$ is harmonic in $D_w$, even if $D_w$ is multiply connected.
>
> *B&C: Sec. 117, Exercise 8*

^prop-116-2

> [!proof]+ Proof
> Since $f$ is analytic, $u$ and $v$ have continuous partial derivatives of all orders ([[§57 Some Consequences of the Extension#^cor-57-2|Corollary §57.2]]), satisfy the Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$, and are harmonic ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]). By the chain rule,
>
> $$
> H_x = h_uu_x + h_vv_x .
> $$
>
> Differentiating again by the chain rule and the product rule,
>
> $$
> H_{xx} = \big(h_{uu}u_x + h_{uv}v_x\big)u_x + h_uu_{xx} + \big(h_{vu}u_x + h_{vv}v_x\big)v_x + h_vv_{xx}
> = h_{uu}u_x^2 + 2h_{uv}u_xv_x + h_{vv}v_x^2 + h_uu_{xx} + h_vv_{xx} ,
> $$
>
> using $h_{vu} = h_{uv}$ (continuous second partials). In the same way
>
> $$
> H_{yy} = h_{uu}u_y^2 + 2h_{uv}u_yv_y + h_{vv}v_y^2 + h_uu_{yy} + h_vv_{yy} .
> $$
>
> Adding,
>
> $$
> H_{xx} + H_{yy} = h_{uu}\big(u_x^2 + u_y^2\big) + h_{vv}\big(v_x^2 + v_y^2\big) + 2h_{uv}\big(u_xv_x + u_yv_y\big) + h_u\big(u_{xx} + u_{yy}\big) + h_v\big(v_{xx} + v_{yy}\big) .
> $$
>
> The last two brackets vanish because $u$ and $v$ are harmonic. By the Cauchy–Riemann equations, $u_xv_x + u_yv_y = u_xv_x - v_xu_x = 0$, and
>
> $$
> u_x^2 + u_y^2 = u_x^2 + v_x^2 = |f'(z)|^2, \qquad v_x^2 + v_y^2 = v_x^2 + u_x^2 = |f'(z)|^2 ,
> $$
>
> since $f'(z) = u_x + iv_x$. This leaves $H_{xx} + H_{yy} = (h_{uu} + h_{vv})|f'(z)|^2$. If $h$ is harmonic the right side is $0$; and $H$ has continuous second partials, by the formulas above. So $H$ is harmonic, with no assumption on the connectivity of $D_w$.

^pf-116-2

*Uses:* [[§57 Some Consequences of the Extension#^cor-57-2|§57.2]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§27★ Harmonic Functions#^thm-27-1|§27.1]], [[§94 The Chain Rule#^thm-94-2|Calc Thm. §94.2]] (chain rule), [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]], [[Schwarz–Clairaut Theorem|452 Schwarz–Clairaut]] ($h_{uv} = h_{vu}$)

> [!remark]- Connections
> - The polar form of the Laplacian is a special case. With $s = \ln r$, the map $w = \operatorname{Log} z = s + i\theta$ has $|f'(z)|^2 = 1/r^2$, so $H_{xx} + H_{yy} = r^{-2}(h_{ss} + h_{\theta\theta})$, and $r\partial_r = \partial_s$ turns $h_{ss}$ into $r^2h_{rr} + rh_r$: this is $h_{rr} + \frac1rh_r + \frac1{r^2}h_{\theta\theta}$, [[§35 Potential Equation#^thm-35-3|341 Thm. §35.3]].
> - The general rule behind the factor $|f'|^2$: the Laplacian depends on the metric, and a conformal map multiplies the metric by $|f'|^2$; in two dimensions this rescales $\nabla^2$ but keeps the equation $\nabla^2 h = 0$. Chain rule: [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]].
> - Used in Electromagnetism: analytic maps carry electrostatic solutions, and line charges with their strength (Corollary §116.3), to solutions — [[§C6.4★ The Complex Potential and the Variational Principle#^thm-c6-4-2|EM Theorem §C6.4.2]], [[§C7.5★ Logarithmic Potentials and the Poisson–Boltzmann Equation#^thm-c7-5-1|EM Theorem §C7.5.1]].

> [!theorem] Corollary §116.3: Poisson's Equation Under an Analytic Map
> Let $p(u, v)$ have continuous partial derivatives of the first and second order and satisfy **Poisson's equation**
>
> $$
> p_{uu}(u, v) + p_{vv}(u, v) = \Phi(u, v)
> $$
>
> in a domain $D_w$, where $\Phi$ is a prescribed function (in Fourier Series and PDEs the same equation is written $\nabla^2u = -H$, [[§37 Further Examples for a Rectangle#^def-37-1|341 Def. §37.1]]). If an analytic function $w = f(z) = u(x, y) + iv(x, y)$ maps a domain $D_z$ onto $D_w$, then $P(x, y) = p[u(x, y), v(x, y)]$ satisfies the Poisson equation
>
> $$
> P_{xx}(x, y) + P_{yy}(x, y) = \Phi\big[u(x, y), v(x, y)\big]\,|f'(z)|^2
> $$
>
> in $D_z$.
>
> *B&C: Sec. 117, Exercise 9*

^cor-116-3

> [!proof]+ Proof
> Apply Proposition §116.2 with $h = p$: $P_{xx} + P_{yy} = (p_{uu} + p_{vv})|f'(z)|^2 = \Phi(u, v)\,|f'(z)|^2$, with $(u, v) = (u(x, y), v(x, y))$.

^pf-116-3

*Uses:* [[§116★ Transformations of Harmonic Functions#^prop-116-2|§116.2]]

So the source term picks up the factor $|f'(z)|^2$: a charge or heat-source density is not carried over unchanged, but Laplace's equation (zero source) is.

## Examples

> [!example] Example §116.2: From a Half Plane to a Strip by e^z
> The transformation
>
> $$
> w = e^z = e^x\cos y + ie^x\sin y
> $$
>
> maps the horizontal strip $0 < y < \pi$ onto the upper half plane $v > 0$ ([[§103★ Mappings by the Exponential Function#^ex-103-3|Example §103.3]]). Since $w^2$ is analytic in that half plane, $h(u, v) = \operatorname{Re}(w^2) = u^2 - v^2$ is harmonic there. By Theorem §116.1 the function
>
> $$
> H(x, y) = (e^x\cos y)^2 - (e^x\sin y)^2 = e^{2x}(\cos^2y - \sin^2y) = e^{2x}\cos 2y
> $$
>
> is harmonic throughout the strip $0 < y < \pi$.
>
> **Direct check.** $H_{xx} = 4e^{2x}\cos 2y$ and $H_{yy} = -4e^{2x}\cos 2y$, so $H_{xx} + H_{yy} = 0$ (in fact in the whole plane, since $H = \operatorname{Re}(e^{2z})$). Also $h_{uu} + h_{vv} = 2 - 2 = 0$, consistent with Proposition §116.2.
>
> *B&C: Sec. 116, Example 2; Sec. 117, Exercise 1*

^ex-116-2

> [!example] Example §116.3: arctan(y/x) from Log z
> The transformation
>
> $$
> w = \operatorname{Log} z = \ln r + i\Theta \qquad \Big(r > 0,\ -\frac\pi2 < \Theta < \frac\pi2\Big)
> $$
>
> takes, in rectangular coordinates, the form $w = \ln\sqrt{x^2 + y^2} + i\arctan\big(\frac yx\big)$, where $-\pi/2 < \arctan t < \pi/2$. It maps the right half plane $x > 0$ onto the horizontal strip $-\pi/2 < v < \pi/2$: a point $re^{i\Theta}$ with $|\Theta| < \pi/2$ goes to $\ln r + i\Theta$, and as $r$ runs through $(0, \infty)$ along the ray $\Theta =$ const, $\ln r$ runs through all of $\mathbb{R}$ on the horizontal line $v = \Theta$. Since $h(u, v) = \operatorname{Im} w = v$ is harmonic in the strip, Theorem §116.1 says that
>
> $$
> H(x, y) = \arctan\Big(\frac yx\Big)
> $$
>
> is harmonic in the half plane $x > 0$. Check: $H_x = -\dfrac{y}{x^2 + y^2}$, $H_y = \dfrac{x}{x^2 + y^2}$, so $H_{xx} = \dfrac{2xy}{(x^2 + y^2)^2}$ and $H_{yy} = -\dfrac{2xy}{(x^2 + y^2)^2}$, which add to $0$.
>
> *B&C: Sec. 116, Example 3; Sec. 117, Exercise 3*

^ex-116-3

> [!example] Example §116.4: A Harmonic Function in the First Quadrant
> The function $h(u, v) = e^{-v}\sin u$ is harmonic in the whole $uv$ plane (Example §116.1 with $u, v$ in place of $x, y$), in particular in the upper half plane $D_w\colon v > 0$. The map $w = z^2$ takes the quadrant $D_z\colon x > 0,\ y > 0$ onto that half plane ([[§14 The Mapping w = z²#^ex-14-2|Example §14.2]]). With $u = x^2 - y^2$, $v = 2xy$, Theorem §116.1 gives that
>
> $$
> H(x, y) = e^{-2xy}\sin(x^2 - y^2)
> $$
>
> is harmonic in the quadrant $D_z$. (By Proposition §116.2 it is in fact harmonic in the whole plane, since $h$ is.) Check: with $\phi = x^2 - y^2$, $\psi = 2xy$, $H = e^{-\psi}\sin\phi$ and $\phi_x = 2x = \psi_y$, $\phi_y = -2y = -\psi_x$; then
>
> $$
> H_{xx} + H_{yy} = e^{-\psi}\Big[\big(\psi_x^2 + \psi_y^2\big)\sin\phi - \big(\phi_x^2 + \phi_y^2\big)\sin\phi - 2\big(\psi_x\phi_x + \psi_y\phi_y\big)\cos\phi - \big(\nabla^2\psi\big)\sin\phi + \big(\nabla^2\phi\big)\cos\phi\Big] = 0 ,
> $$
>
> since $\psi_x^2 + \psi_y^2 = \phi_x^2 + \phi_y^2 = 4(x^2 + y^2)$, $\psi_x\phi_x + \psi_y\phi_y = 4xy - 4xy = 0$, and $\nabla^2\phi = \nabla^2\psi = 0$.
>
> *B&C: Sec. 117, Exercise 2*

^ex-116-4
