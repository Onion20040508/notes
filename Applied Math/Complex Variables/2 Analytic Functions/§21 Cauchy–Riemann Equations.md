---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 21
bc: "21"
aliases: ["B&C 21"]
tags: [complex-variables, math342]
---
← [[§20 Rules for Differentiation]] · ↑ [[· 2 Analytic Functions]] · [[§22 Examples (Cauchy–Riemann Equations)]] →

*Brown–Churchill, Section 21 · MAT 342 Practice Finals (Fall 2002, Spring 2005).*

If $f = u + iv$ has a derivative at $z_0$, the difference quotient must have the same limit whether $\Delta z$ approaches $0$ horizontally or vertically. The horizontal limit is $u_x + iv_x$, the vertical one $v_y - iu_y$, and equating them gives the two **Cauchy–Riemann equations** $u_x = v_y$, $u_y = -v_x$, together with a formula for $f'(z_0)$ in terms of partial derivatives. They are necessary conditions, used first of all to locate the points where a derivative cannot exist; with continuity of the partial derivatives they also become sufficient ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]). They are the link between complex analysis and two-dimensional potential theory: they make $u$ and $v$ harmonic, with level curves crossing at right angles, which is why the real and imaginary parts of an analytic function serve as electrostatic potentials and field lines, or as velocity potentials and streamlines ([[§124★ Two-Dimensional Fluid Flow|§124★]], [[§125★ The Stream Function|§125★]]).

## The Equations

Let

$$
f(z) = u(x, y) + iv(x, y) , \qquad (1)
$$

suppose that $f'(z_0)$ exists, and write $z_0 = x_0 + iy_0$, $\Delta z = \Delta x + i\Delta y$ and

$$
\Delta w = f(z_0 + \Delta z) - f(z_0) = \big[u(x_0 + \Delta x, y_0 + \Delta y) + iv(x_0 + \Delta x, y_0 + \Delta y)\big] - \big[u(x_0, y_0) + iv(x_0, y_0)\big] .
$$

Then

$$
\frac{\Delta w}{\Delta z} = \frac{u(x_0 + \Delta x, y_0 + \Delta y) - u(x_0, y_0)}{\Delta x + i\Delta y} + i\,\frac{v(x_0 + \Delta x, y_0 + \Delta y) - v(x_0, y_0)}{\Delta x + i\Delta y} , \qquad (2)
$$

and this expression remains valid as $(\Delta x, \Delta y)$ tends to $(0, 0)$ in any manner we may choose.

> [!definition] Definition §21.1: Cauchy–Riemann Equations
> The equations
>
> $$
> u_x = v_y, \qquad u_y = -v_x \qquad (6)
> $$
>
> between the first-order partial derivatives of the components $u$ and $v$ of $f = u + iv$, at a point $(x_0, y_0)$, are the **Cauchy–Riemann equations**.
>
> *B&C: Sec. 21, equations (6)*

^def-21-1

They are named after A. L. Cauchy (1789–1857), who discovered and used them, and G. F. B. Riemann (1826–1866), who made them fundamental in his development of the theory of functions of a complex variable.

> [!theorem] Theorem §21.1: Cauchy–Riemann Equations Are Necessary
> Suppose that
>
> $$
> f(z) = u(x, y) + iv(x, y)
> $$
>
> and that $f'(z)$ exists at a point $z_0 = x_0 + iy_0$. Then the first-order partial derivatives of $u$ and $v$ must exist at $(x_0, y_0)$, and they must satisfy the Cauchy–Riemann equations
>
> $$
> u_x = v_y, \qquad u_y = -v_x \qquad (7)
> $$
>
> there. Also, $f'(z_0)$ can be written
>
> $$
> f'(z_0) = u_x + iv_x , \qquad (8)
> $$
>
> where these partial derivatives are evaluated at $(x_0, y_0)$. Equivalently,
>
> $$
> f'(z_0) = v_y - iu_y = -i\,(u_y + iv_y) . \qquad (4),\ (5)
> $$
>
> *B&C: Sec. 21, Theorem*

^thm-21-1

> [!proof]+ Proof
> Since $\lim_{\Delta z\to0}\Delta w/\Delta z = f'(z_0)$, the limit is the same when $\Delta z$ is restricted to any set of points accumulating at $0$, in particular to the nonzero points of either axis. (If $|\Delta w/\Delta z - f'(z_0)| < \varepsilon$ for all $0 < |\Delta z| < \delta$, then certainly for those $\Delta z$ on an axis.)
>
> **Horizontal approach.** Put $\Delta y = 0$ and let $(\Delta x, 0)$ tend to $(0, 0)$. Then (2) is
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{u(x_0 + \Delta x, y_0) - u(x_0, y_0)}{\Delta x} + i\,\frac{v(x_0 + \Delta x, y_0) - v(x_0, y_0)}{\Delta x} ,
> $$
>
> a complex-valued function of the real variable $\Delta x$ whose real and imaginary parts are the two difference quotients shown. It tends to $f'(z_0)$. As in [[§16 Theorems on Limits#^thm-16-1|Theorem §16.1]] (the real and imaginary parts of a complex number are at most its modulus), each part then has a limit: the real part tends to $\operatorname{Re} f'(z_0)$ and the imaginary part to $\operatorname{Im} f'(z_0)$. These limits are, by definition, the partial derivatives $u_x(x_0, y_0)$ and $v_x(x_0, y_0)$. So both exist and
>
> $$
> f'(z_0) = u_x(x_0, y_0) + iv_x(x_0, y_0) . \qquad (3)
> $$
>
> **Vertical approach.** Put $\Delta x = 0$ instead. Then (2) is
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{u(x_0, y_0 + \Delta y) - u(x_0, y_0)}{i\Delta y} + i\,\frac{v(x_0, y_0 + \Delta y) - v(x_0, y_0)}{i\Delta y} = \frac{v(x_0, y_0 + \Delta y) - v(x_0, y_0)}{\Delta y} - i\,\frac{u(x_0, y_0 + \Delta y) - u(x_0, y_0)}{\Delta y} ,
> $$
>
> because $1/i = -i$. This tends to $f'(z_0)$ as $\Delta y \to 0$; its real and imaginary parts are the two real difference quotients with the signs shown. So, as before, $v_y(x_0, y_0)$ and $u_y(x_0, y_0)$ exist and
>
> $$
> f'(z_0) = v_y(x_0, y_0) - iu_y(x_0, y_0) , \qquad (4)
> $$
>
> which can also be written $f'(z_0) = -i\big[u_y(x_0, y_0) + iv_y(x_0, y_0)\big]$ (5).
>
> **The equations.** Expressions (3) and (4) are two expressions for the same number $f'(z_0)$, by uniqueness of limits ([[§15 Limits#^thm-15-1|Theorem §15.1]]). Equating the real parts and then the imaginary parts gives
>
> $$
> u_x(x_0, y_0) = v_y(x_0, y_0) \qquad\text{and}\qquad v_x(x_0, y_0) = -u_y(x_0, y_0) ,
> $$
>
> which are (7); and (3) is (8).

^pf-21-1

*Uses:* [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§16 Theorems on Limits#^thm-16-1|§16.1]], [[§15 Limits#^thm-15-1|§15.1]], [[§15 Limits#^cor-15-2|§15.2]], [[§4 Partial Derivatives#^def-4-1|452 Def. §4.1]] (partial derivatives)

> [!remark]- Connections
> - In the language of multivariable calculus: if $f'(z_0) = a + ib$ exists, then $f(z_0 + \Delta z) - f(z_0) = (a + ib)\Delta z + o(|\Delta z|)$, so the map $(x, y) \mapsto (u, v)$ is differentiable at $(x_0, y_0)$ in the sense of [[§6 Differentiability#^def-6-1|452 Def. §6.1]], with Jacobian matrix ([[§13 The Inverse Function Theorem#^def-13-1|452 Def. §13.1]])
>
> $$
> \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix} = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} .
> $$
>
>   The Cauchy–Riemann equations say exactly that the Jacobian is a rotation–scaling matrix, [[§36 Complex Eigenvalues#^prop-36-3|235 Prop. §36.3]]: the derivative acts on small displacements as multiplication by the complex number $f'(z_0)$. The converse (real differentiability plus the Cauchy–Riemann equations imply complex differentiability) is the content of [[§23 Sufficient Conditions for Differentiability|§23]], where continuity of the partials supplies real differentiability through [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]].
> - Used in Electromagnetism: the complex potential of two-dimensional electrostatics, whose real and imaginary parts are the potential and the flux function — [[§C6.4★ The Complex Potential and the Variational Principle#^def-c6-4-1|EM Def. §C6.4.1]], [[§C6.4★ The Complex Potential and the Variational Principle#^thm-c6-4-1|EM Theorem §C6.4.1]].

> [!remark] Remark: What the Theorem Does and Does Not Say
> The theorem gives **necessary** conditions. Where the Cauchy–Riemann equations fail, or a partial derivative fails to exist, $f'$ does not exist; solving them therefore produces the only **candidates** for points of differentiability. At a candidate the theorem says nothing: the equations can hold at a point where $f'$ does not exist ([[§22 Examples (Cauchy–Riemann Equations)#^ex-22-3|Example §22.3]]). Existence at a candidate is settled either directly from the definition (Example §21.2 below) or by the sufficient conditions of [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] (the full procedure is [[§23 Sufficient Conditions for Differentiability#^rem-23-1|Remark: Method — Checking Differentiability with Cauchy–Riemann]]). When $f'$ does exist, formula (8) computes it from a single horizontal derivative. A polar form of the equations is [[§24★ Polar Coordinates#^prop-24-1|Proposition §24.1]].

^rem-21-1

## Examples

> [!example] Example §21.1: Three Functions Differentiable Nowhere
> Use Theorem §21.1 to show that $f'(z)$ does not exist at any point if (a) $f(z) = \bar z$; (b) $f(z) = z - \bar z$; (c) $f(z) = 2x + ixy^2$.
>
> **(a)** $\bar z = x - iy$, so $u = x$, $v = -y$, and $u_x = 1$, $v_y = -1$. The equation $u_x = v_y$ fails at every point. (This is [[§19 Derivatives#^ex-19-2|Example §19.2]] again, now without any limit computation.)
>
> **(b)** $z - \bar z = 2iy$, so $u = 0$, $v = 2y$, and $u_x = 0$, $v_y = 2$. Again $u_x = v_y$ fails everywhere.
>
> **(c)** $u = 2x$, $v = xy^2$, so
>
> $$
> u_x = 2, \quad v_y = 2xy, \qquad u_y = 0, \quad v_x = y^2 .
> $$
>
> The second equation $u_y = -v_x$ requires $y^2 = 0$, that is $y = 0$; but then the first, $u_x = v_y$, reads $2 = 0$. So the two equations never hold together.
>
> In each case the Cauchy–Riemann equations fail at every point, and by Theorem §21.1 $f'(z)$ exists nowhere, although $u$ and $v$ are polynomials in $x$ and $y$.
>
> *B&C: Sec. 24, Exercise 1(a)–(c)*

^ex-21-1

> [!example] Example §21.2: A Single Candidate, Checked from the Definition
> Determine where $f(z) = z\operatorname{Im} z$ has a derivative, and find it.
>
> **Candidates.** $f(z) = (x + iy)y = xy + iy^2$, so $u = xy$, $v = y^2$ and
>
> $$
> u_x = y, \quad v_y = 2y, \qquad u_y = x, \quad v_x = 0 .
> $$
>
> The equation $u_x = v_y$ gives $y = 2y$, so $y = 0$; the equation $u_y = -v_x$ gives $x = 0$. So the equations hold only at $z = 0$, and by Theorem §21.1, **$f'(z)$ does not exist at any nonzero point.**
>
> **At the candidate.** The theorem cannot decide whether $f'(0)$ exists, but the definition can. For $\Delta z \ne 0$,
>
> $$
> \frac{f(\Delta z) - f(0)}{\Delta z} = \frac{\Delta z\operatorname{Im}\Delta z}{\Delta z} = \operatorname{Im}\Delta z \longrightarrow 0 ,
> $$
>
> since $|\operatorname{Im}\Delta z| \le |\Delta z|$. So $f'(0)$ exists and equals $0$, in agreement with (8): $u_x + iv_x = 0 + i0$ at the origin.
>
> *B&C: Sec. 24, Exercise 3(c)*

^ex-21-2

> [!example] Example §21.3: The Derivative of 1/z from Its Components
> By [[§19 Derivatives#^ex-19-1|Example §19.1]], $f(z) = 1/z$ is differentiable at every $z \ne 0$. Find $f'(z)$ from formula (8), and check the Cauchy–Riemann equations.
>
> By [[§13 Functions and Mappings#^ex-13-1|Example §13.1]],
>
> $$
> u = \frac{x}{x^2 + y^2}, \qquad v = \frac{-y}{x^2 + y^2} \qquad \big((x, y) \ne (0, 0)\big) .
> $$
>
> The quotient rule gives
>
> $$
> u_x = \frac{y^2 - x^2}{(x^2 + y^2)^2}, \quad u_y = \frac{-2xy}{(x^2 + y^2)^2}, \qquad v_x = \frac{2xy}{(x^2 + y^2)^2}, \quad v_y = \frac{y^2 - x^2}{(x^2 + y^2)^2} ,
> $$
>
> so $u_x = v_y$ and $u_y = -v_x$ at every nonzero point, as Theorem §21.1 requires. By (8),
>
> $$
> f'(z) = u_x + iv_x = \frac{-(x^2 - 2ixy - y^2)}{(x^2 + y^2)^2} = -\frac{(x - iy)^2}{|z|^4} = -\frac{\bar z^{\,2}}{(z\bar z)^2} = -\frac{1}{z^2} ,
> $$
>
> the derivative found in §19. Formula (4) gives the same: $v_y - iu_y = \big(y^2 - x^2 + 2ixy\big)/(x^2 + y^2)^2$.
>
> *B&C: Sec. 24, Exercise 3(a)*

^ex-21-3

> [!remark]- Remark: The Cauchy–Riemann Equations Alone Rule Out a Real Part
> *True or false: there exists an entire function whose real part is $xe^y$.* [[§27★ Harmonic Functions#^ex-27-4|Example §27.4]] answers "false" because $xe^y$ is not harmonic, which rests on the smoothness of analytic functions proved in [[§57 Some Consequences of the Extension#^cor-57-2|Corollary §57.2]]. Theorem §21.1 alone also suffices. If $f = u + iv$ were differentiable everywhere with $u = xe^y$, then at every point
>
> $$
> v_y = u_x = e^y, \qquad v_x = -u_y = -xe^y .
> $$
>
> For fixed $x$, $y \mapsto v(x, y) - e^y$ has derivative $0$ on the whole line, so it is a constant depending on $x$ ([[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]]): $v(x, y) = e^y + \varphi(x)$. Then $\varphi'(x) = v_x(x, y) = -xe^y$ for all $x$ and $y$; at $x = 1$, $\varphi'(1) = -e^y$ for every $y$, which is impossible. The same argument disposes of $e^{x + y}$: $v_y = e^{x + y}$ gives $v = e^{x + y} + \varphi(x)$, and then $v_x = e^{x + y} + \varphi'(x)$ must equal $-u_y = -e^{x + y}$, so $\varphi'(x) = -2e^{x + y}$ would depend on $y$.
>
> *Source: 342 practice final (Fall 2002), Q8(d); 342 practice final (Spring 2005), Q8(d)*

^rem-21-2
