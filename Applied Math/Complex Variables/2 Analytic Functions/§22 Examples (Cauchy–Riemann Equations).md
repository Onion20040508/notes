---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 22
bc: "22"
aliases: ["B&C 22"]
tags: [complex-variables, math342]
---
← [[§21 Cauchy–Riemann Equations]] · ↑ [[· 2 Analytic Functions]] · [[§23 Sufficient Conditions for Differentiability]] →

*Brown–Churchill, Section 22 · MAT 342 HW 3, Practice Final (Fall 1999).*

This section tests the theorem of [[§21 Cauchy–Riemann Equations|§21]] (Theorem) on examples. If $f'(z_0)$ exists, then $u_x = v_y$ and $u_y = -v_x$ at $z_0$ and $f'(z_0) = u_x + iv_x$. Since the equations are *necessary*, they confirm a derivative already known and, more usefully, they locate the points where a derivative *cannot* exist. They are not sufficient: Example §22.3 satisfies them at the origin and still has no derivative there. That gap is closed in [[§23 Sufficient Conditions for Differentiability|§23]], where continuity of the partial derivatives is added.

## The Necessary Condition at Work

> [!example] Example §22.1: The Function z²
> By [[§20 Rules for Differentiation|§20]] (Exercise 1), $f(z) = z^2$ is differentiable everywhere and $f'(z) = 2z$. Check the Cauchy–Riemann equations. Here
>
> $$
> f(z) = (x + iy)^2 = x^2 - y^2 + i\,2xy, \qquad u(x, y) = x^2 - y^2, \qquad v(x, y) = 2xy ,
> $$
>
> so
>
> $$
> u_x = 2x = v_y, \qquad u_y = -2y = -v_x
> $$
>
> at every point. The formula $f'(z_0) = u_x + iv_x$ of §21 gives back the known derivative:
>
> $$
> f'(z) = 2x + i2y = 2(x + iy) = 2z .
> $$
>
> *B&C: Sec. 22, Example 1*

^ex-22-1

> [!example] Example §22.2: The Function |z|²
> Let $f(z) = |z|^2$. Then
>
> $$
> u(x, y) = x^2 + y^2, \qquad v(x, y) = 0 .
> $$
>
> If the Cauchy–Riemann equations hold at $(x, y)$, then $u_x = v_y$ gives $2x = 0$ and $u_y = -v_x$ gives $2y = 0$, so $x = y = 0$. Consequently $f'(z)$ **does not exist at any nonzero point**, as found directly in [[§19 Derivatives|§19]] (Example 3).
>
> At the origin the equations do hold, but the theorem of §21 says nothing there: it gives conditions that a derivative must satisfy, not conditions that produce one. That $f'(0)$ exists (and equals $0$) follows from the theorem of §23, [[§23 Sufficient Conditions for Differentiability#^ex-23-2|Example §23.2]].
>
> *B&C: Sec. 22, Example 2*

^ex-22-2

> [!example] Example §22.3: The Equations Hold but f′(0) Does Not Exist
> Let
>
> $$
> f(z) = \begin{cases} \bar z^{\,2}/z & \text{when } z \ne 0, \\ 0 & \text{when } z = 0. \end{cases}
> $$
>
> **Components.** For $z \ne 0$, $\bar z^{\,2}/z = \bar z^{\,3}/|z|^2$, and $\bar z^{\,3} = (x - iy)^3 = x^3 - 3xy^2 + i(y^3 - 3x^2y)$, so ([[§14 The Mapping w = z²|§14]], Exercise 2(b))
>
> $$
> u(x, y) = \frac{x^3 - 3xy^2}{x^2 + y^2}, \qquad v(x, y) = \frac{y^3 - 3x^2y}{x^2 + y^2} \qquad \big((x, y) \ne (0, 0)\big),
> $$
>
> and $u(0, 0) = v(0, 0) = 0$.
>
> **The Cauchy–Riemann equations hold at the origin.** On the axes, $u(\Delta x, 0) = \Delta x$, $u(0, \Delta y) = 0$, $v(\Delta x, 0) = 0$, $v(0, \Delta y) = \Delta y$. Hence
>
> $$
> u_x(0, 0) = \lim_{\Delta x\to0}\frac{u(0 + \Delta x, 0) - u(0, 0)}{\Delta x} = \lim_{\Delta x\to0}\frac{\Delta x}{\Delta x} = 1, \qquad
> v_y(0, 0) = \lim_{\Delta y\to0}\frac{v(0, 0 + \Delta y) - v(0, 0)}{\Delta y} = \lim_{\Delta y\to0}\frac{\Delta y}{\Delta y} = 1 ,
> $$
>
> and in the same way $u_y(0, 0) = \lim 0/\Delta y = 0$ and $v_x(0, 0) = \lim 0/\Delta x = 0$. So $u_x = v_y$ and $u_y = 0 = -v_x$ at $z = 0$.
>
> **But $f'(0)$ does not exist** ([[§20 Rules for Differentiation|§20]], Exercise 9). At $z = 0$, with $\Delta z \ne 0$,
>
> $$
> \frac{\Delta w}{\Delta z} = \frac{f(\Delta z) - f(0)}{\Delta z} = \frac{\overline{\Delta z}^{\,2}}{(\Delta z)^2} = \Big(\frac{\overline{\Delta z}}{\Delta z}\Big)^2 .
> $$
>
> At a nonzero point $(\Delta x, 0)$ of the real axis this is $(\Delta x/\Delta x)^2 = 1$; at a nonzero point $(0, \Delta y)$ of the imaginary axis it is $\big({-i\Delta y}/{i\Delta y}\big)^2 = 1$. At a nonzero point $(\Delta x, \Delta x)$ of the line $\Delta y = \Delta x$, $\Delta z = \Delta x(1 + i)$ and
>
> $$
> \frac{\Delta w}{\Delta z} = \Big(\frac{1 - i}{1 + i}\Big)^2 = (-i)^2 = -1 .
> $$
>
> So $\Delta w/\Delta z$ tends to $1$ as $\Delta z \to 0$ along the axes and to $-1$ along the diagonal. A limit is unique ([[§15 Limits|§15]]), so $\lim_{\Delta z\to0}\Delta w/\Delta z$ does not exist. Horizontal and vertical approaches alone, which are all that the Cauchy–Riemann equations see, could not have detected this.
>
> *B&C: Sec. 22, Example 3; Sec. 20, Exercise 9*

^ex-22-3

![[m342-22-1.svg]]
*The difference quotient of Example §22.3 at $z = 0$ is $(\overline{\Delta z}/\Delta z)^2 = e^{-4i\varphi}$ along the ray at angle $\varphi$. It equals $1$ along both axes (blue), which is all that the partial derivatives and the Cauchy–Riemann equations test, and $-1$ along the diagonals (red), so it has no limit at $0$.*

> [!remark]- Connections
> - The same phenomenon for a real function of two variables: partial derivatives at a point say nothing about approaches along other directions, [[§6 Differentiability#^ex-6-1|452 Ex. §6.1]] ($2xy/(x^2 + y^2)$ has both partials $0$ at the origin and is not differentiable there). Here $u$ and $v$ have partials at $0$ but are not differentiable there; adding continuity of the partials is exactly what [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]] and the theorem of §23 do.

## Locating Points Without a Derivative

> [!example] Example §22.4: The Function e^z̄
> **(a)** Where is $f(z) = e^{\bar z}$ differentiable? Here $e^{\bar z} = e^{x - iy} = e^x e^{-iy}$, the function $e^xe^{-iy}$ of B&C's exercise, and by Euler's formula
>
> $$
> f(z) = e^x\cos y - ie^x\sin y, \qquad u = e^x\cos y, \qquad v = -e^x\sin y .
> $$
>
> Then
>
> $$
> u_x = e^x\cos y, \quad v_y = -e^x\cos y, \qquad u_y = -e^x\sin y, \quad v_x = -e^x\sin y .
> $$
>
> The equation $u_x = v_y$ says $2e^x\cos y = 0$, that is $\cos y = 0$; the equation $u_y = -v_x$ says $-e^x\sin y = e^x\sin y$, that is $\sin y = 0$. Since $\cos^2y + \sin^2y = 1$, the two cannot hold at the same point. So the Cauchy–Riemann equations fail at every point, and **$f'(z)$ exists nowhere**.
>
> **(b)** *True or false: $\displaystyle\lim_{z\to0}\frac{e^{\bar z} - 1}{z}$ exists and equals $1$.* False. The quotient is $\big(f(z) - f(0)\big)/(z - 0)$ for the function of (a), so the limit would be $f'(0)$, which does not exist. Directly: along the real axis ($z = x$) the quotient is $(e^x - 1)/x \to 1$; along the imaginary axis ($z = iy$) it is
>
> $$
> \frac{e^{-iy} - 1}{iy} \;\longrightarrow\; \frac{1}{i}\,\frac{d}{dy}e^{-iy}\Big|_{y=0} = \frac{-i}{i} = -1 .
> $$
>
> Two approaches give different limits, so there is no limit. (These two numbers are $u_x + iv_x = 1$ and $-i(u_y + iv_y) = -1$ at the origin, the two expressions for $f'(0)$ in §21; they disagree because $u_x \ne v_y$ there.)
>
> *B&C: Sec. 24, Exercise 1(d); Source: 342 HW 3, Q2(c); 342 practice final (Fall 1999), Q7a*

^ex-22-4

> [!remark] Remark: What the Necessary Condition Can and Cannot Do
> Solving the two equations $u_x = v_y$, $u_y = -v_x$ gives the **only candidates** for points where $f'$ exists. Outside that set $f'$ certainly does not exist (Examples §22.2 and §22.4). At the candidates the question stays open (Example §22.3). It is settled by the sufficient condition of §23 when the partial derivatives are continuous there, which is the case for every function built from polynomials, exponentials and trigonometric functions of $x$ and $y$. The full procedure is [[§23 Sufficient Conditions for Differentiability#^rem-23-1|Remark: Method — Checking Differentiability with Cauchy–Riemann]].

^rem-22-1
