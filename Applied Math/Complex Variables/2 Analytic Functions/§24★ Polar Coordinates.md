---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 24
bc: "24"
aliases: ["B&C 24"]
tags: [complex-variables, math342, extension]
---
← [[§23 Sufficient Conditions for Differentiability]] · ↑ [[· 2 Analytic Functions]] · [[§25 Analytic Functions]] →

*Brown–Churchill, Section 24 · MAT 342 HW 3 (optional problems).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Functions such as $1/z^n$, branches of $z^{1/2}$ and of $\log z$ are given most naturally in terms of $r$ and $\theta$, where $z = re^{i\theta}$. This section rewrites the Cauchy–Riemann equations and the sufficient condition [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] in polar coordinates: the equations become $ru_r = v_\theta$, $u_\theta = -rv_r$, and the derivative is $f'(z_0) = e^{-i\theta}(u_r + iv_r)$. The polar test is how B&C shows later that every branch of $\log z$ and of $z^c$ is analytic ([[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1]], [[§35 The Power Function#^thm-35-2|Theorem §35.2]]). The section closes with the complex form $\partial f/\partial\bar z = 0$ of the Cauchy–Riemann equations.

## The Cauchy–Riemann Equations in Polar Form

Assume $z_0 \ne 0$ and use the coordinate transformation

$$
x = r\cos\theta, \qquad y = r\sin\theta . \qquad (1)
$$

Depending on whether we write $z = x + iy$ or $z = re^{i\theta}$ ($z \ne 0$), the components of $w = u + iv$ are functions of $x$ and $y$ or of $r$ and $\theta$; as B&C does, we use the same letters $u, v$ for both, so that $u(r, \theta)$ means $u(r\cos\theta, r\sin\theta)$.

> [!theorem] Proposition §24.1: Polar Form of the Cauchy–Riemann Equations
> Let $z_0 = r_0e^{i\theta_0} \ne 0$, and let $u$ and $v$ be differentiable at $(x_0, y_0)$ as functions of $x$ and $y$ (for instance, their first-order partial derivatives exist in a neighborhood of $z_0$ and are continuous at $z_0$; see Step 1 of the proof of [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]). Then at $(r_0, \theta_0)$
>
> $$
> u_r = u_x\cos\theta + u_y\sin\theta, \qquad u_\theta = -u_xr\sin\theta + u_yr\cos\theta , \qquad (2)
> $$
>
> $$
> v_r = v_x\cos\theta + v_y\sin\theta, \qquad v_\theta = -v_xr\sin\theta + v_yr\cos\theta , \qquad (3)
> $$
>
> and, solving for the $x$ and $y$ derivatives,
>
> $$
> u_x = u_r\cos\theta - u_\theta\frac{\sin\theta}{r}, \qquad u_y = u_r\sin\theta + u_\theta\frac{\cos\theta}{r} \qquad (\text{and the same for } v) .
> $$
>
> Consequently the Cauchy–Riemann equations
>
> $$
> u_x = v_y, \qquad u_y = -v_x \qquad (4)
> $$
>
> hold at $z_0$ if and only if their **polar form**
>
> $$
> ru_r = v_\theta, \qquad u_\theta = -rv_r \qquad (6)
> $$
>
> holds at $(r_0, \theta_0)$.
>
> *B&C: Sec. 24, equations (2)–(6), and Exercise 5*

^prop-24-1

> [!proof]+ Proof
> **(2) and (3).** The map $(r, \theta) \mapsto (r\cos\theta, r\sin\theta)$ is differentiable, with $\partial x/\partial r = \cos\theta$, $\partial y/\partial r = \sin\theta$, $\partial x/\partial\theta = -r\sin\theta$, $\partial y/\partial\theta = r\cos\theta$. Since $u$ is differentiable at its image $(x_0, y_0)$, the chain rule gives
>
> $$
> \frac{\partial u}{\partial r} = \frac{\partial u}{\partial x}\frac{\partial x}{\partial r} + \frac{\partial u}{\partial y}\frac{\partial y}{\partial r}, \qquad \frac{\partial u}{\partial\theta} = \frac{\partial u}{\partial x}\frac{\partial x}{\partial\theta} + \frac{\partial u}{\partial y}\frac{\partial y}{\partial\theta} ,
> $$
>
> which is (2); likewise (3).
>
> **Inverse formulas** (B&C's Exercise 5). From (2), $u_r\cos\theta - \frac{u_\theta}{r}\sin\theta = u_x\cos^2\theta + u_y\sin\theta\cos\theta + u_x\sin^2\theta - u_y\cos\theta\sin\theta = u_x$, and $u_r\sin\theta + \frac{u_\theta}{r}\cos\theta = u_x\cos\theta\sin\theta + u_y\sin^2\theta - u_x\sin\theta\cos\theta + u_y\cos^2\theta = u_y$. The same computation applies to $v$.
>
> **(4) $\Rightarrow$ (6).** If $u_x = v_y$ and $u_y = -v_x$ at $z_0$, equations (3) become
>
> $$
> v_r = -u_y\cos\theta + u_x\sin\theta, \qquad v_\theta = u_yr\sin\theta + u_xr\cos\theta \qquad (5)
> $$
>
> at that point. Comparing with (2): $ru_r = u_xr\cos\theta + u_yr\sin\theta = v_\theta$, and $u_\theta = -u_xr\sin\theta + u_yr\cos\theta = -rv_r$.
>
> **(6) $\Rightarrow$ (4).** If $v_\theta = ru_r$ and $u_\theta = -rv_r$, the inverse formulas give
>
> $$
> v_y = v_r\sin\theta + \frac{v_\theta}{r}\cos\theta = v_r\sin\theta + u_r\cos\theta = u_r\cos\theta - \frac{u_\theta}{r}\sin\theta = u_x ,
> $$
>
> $$
> -v_x = -v_r\cos\theta + \frac{v_\theta}{r}\sin\theta = -v_r\cos\theta + u_r\sin\theta = u_r\sin\theta + \frac{u_\theta}{r}\cos\theta = u_y .
> $$

^pf-24-1

*Uses:* [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]] (Step 1 of the proof), [[§6 Differentiability#^thm-6-9|452 Thm. §6.9]] (chain rule)

> [!remark]- Connections
> - The same chain-rule computation, carried one order further, turns the Laplacian into polar form, [[§35 Potential Equation#^thm-35-3|341 Thm. §35.3]]; with (6) it shows that the components of an analytic function satisfy $r^2u_{rr} + ru_r + u_{\theta\theta} = 0$ (B&C's Sec. 27, Exercise 1; see [[§27★ Harmonic Functions#^def-27-1|Definition §27.1]]).

> [!theorem] Proposition §24.2: The Derivative in Polar Form
> If $f = u + iv$ is differentiable at $z_0 = r_0e^{i\theta_0} \ne 0$, then at $(r_0, \theta_0)$
>
> $$
> f'(z_0) = e^{-i\theta}(u_r + iv_r) = \frac{-i}{z_0}(u_\theta + iv_\theta) .
> $$
>
> *B&C: Sec. 24, Exercises 6 and 7(a)*

^prop-24-2

> [!proof]+ Proof
> If $f'(z_0)$ exists, $u$ and $v$ are differentiable at $(x_0, y_0)$ (the remark after [[§23 Sufficient Conditions for Differentiability#^cor-23-2|Corollary §23.2]]) and satisfy the Cauchy–Riemann equations there ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]), so Proposition §24.1 applies and (6) holds. By the inverse formulas and (6) ($u_\theta = -rv_r$, $v_\theta = ru_r$),
>
> $$
> f'(z_0) = u_x + iv_x = \Big(u_r\cos\theta - \frac{u_\theta}{r}\sin\theta\Big) + i\Big(v_r\cos\theta - \frac{v_\theta}{r}\sin\theta\Big) = (u_r\cos\theta + v_r\sin\theta) + i(v_r\cos\theta - u_r\sin\theta) .
> $$
>
> The right side is $(u_r + iv_r)(\cos\theta - i\sin\theta) = e^{-i\theta}(u_r + iv_r)$. For the second form, (6) gives $u_r + iv_r = \frac1r(v_\theta - iu_\theta) = \frac{-i}{r}(u_\theta + iv_\theta)$, so $f'(z_0) = \dfrac{-i}{re^{i\theta}}(u_\theta + iv_\theta) = \dfrac{-i}{z_0}(u_\theta + iv_\theta)$.

^pf-24-2

*Uses:* [[§24★ Polar Coordinates#^prop-24-1|§24.1]], [[§23 Sufficient Conditions for Differentiability#^cor-23-2|§23.2]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]]

## The Sufficient Condition in Polar Form

In view of (6) and Proposition §24.2, the theorem of §23 can be restated using $r$ and $\theta$.

> [!theorem] Theorem §24.3: Sufficient Conditions in Polar Coordinates
> Let the function
>
> $$
> f(z) = u(r, \theta) + iv(r, \theta)
> $$
>
> be defined throughout some $\varepsilon$ neighborhood of a nonzero point $z_0 = r_0\exp(i\theta_0)$, and suppose that
>
> **(a)** the first-order partial derivatives of the functions $u$ and $v$ with respect to $r$ and $\theta$ exist everywhere in the neighborhood;
>
> **(b)** those partial derivatives are continuous at $(r_0, \theta_0)$ and satisfy the polar form
>
> $$
> ru_r = v_\theta, \qquad u_\theta = -rv_r
> $$
>
> of the Cauchy–Riemann equations at $(r_0, \theta_0)$.
>
> Then $f'(z_0)$ exists, its value being
>
> $$
> f'(z_0) = e^{-i\theta}(u_r + iv_r) ,
> $$
>
> where the right-hand side is to be evaluated at $(r_0, \theta_0)$.
>
> *B&C: Sec. 24, Theorem*

^thm-24-3

> [!proof]+ Proof
> B&C states the theorem as a restatement of §23; the point to check is that the polar hypotheses give what the proof of §23 needs. Shrinking $\varepsilon$ if necessary, assume $\varepsilon < r_0$.
>
> **Polar coordinates near $z_0$.** For $|z - z_0| < \varepsilon$ we have $|z/z_0 - 1| < \varepsilon/r_0 < 1$, so $z/z_0$ lies in the right half plane and $\theta(z) = \theta_0 + \operatorname{Arg}(z/z_0)$, with $|\theta(z) - \theta_0| < \pi/2$, is a continuous choice of the argument with $\theta(z_0) = \theta_0$. Together with $r = |z|$ this gives differentiable functions $r(x, y)$, $\theta(x, y)$ on the neighborhood, with
>
> $$
> r_x = \cos\theta, \qquad r_y = \sin\theta, \qquad \theta_x = -\frac{\sin\theta}{r}, \qquad \theta_y = \frac{\cos\theta}{r}
> $$
>
> (locally $\theta$ differs from $\tan^{-1}(y/x)$ or $\cot^{-1}(x/y)$ by a constant). The polar description of the neighborhood is the open set $P$ of pairs $(r, \theta)$ with $|re^{i\theta} - z_0| < \varepsilon$ and $|\theta - \theta_0| < \pi/2$, which contains $(r_0, \theta_0)$.
>
> **$u$ and $v$ are differentiable at $(x_0, y_0)$.** By (a) the partial derivatives $u_r$, $u_\theta$ exist on $P$, and by (b) they are continuous at $(r_0, \theta_0)$. Step 1 of the proof of [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]], carried out in the variables $(r, \theta)$ on a small rectangle about $(r_0, \theta_0)$ inside $P$, shows that $u(r, \theta)$ is differentiable at $(r_0, \theta_0)$. Since $u(x, y) = u\big(r(x, y), \theta(x, y)\big)$ near $z_0$ and $r(x, y)$, $\theta(x, y)$ are differentiable, the chain rule shows that $u$ is differentiable at $(x_0, y_0)$ as a function of $x$ and $y$, with
>
> $$
> u_x = u_rr_x + u_\theta\theta_x = u_r\cos\theta - u_\theta\frac{\sin\theta}{r}, \qquad u_y = u_r\sin\theta + u_\theta\frac{\cos\theta}{r} ,
> $$
>
> the inverse formulas of Proposition §24.1. The same holds for $v$.
>
> **Conclusion.** By Proposition §24.1, the polar equations (6) at $(r_0, \theta_0)$ give the Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$ at $(x_0, y_0)$. By [[§23 Sufficient Conditions for Differentiability#^cor-23-2|Corollary §23.2]], $f'(z_0)$ exists, and by Proposition §24.2 it equals $e^{-i\theta}(u_r + iv_r)$ at $(r_0, \theta_0)$.

^pf-24-3

*Uses:* [[§24★ Polar Coordinates#^prop-24-1|§24.1]], [[§24★ Polar Coordinates#^prop-24-2|§24.2]], [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]], [[§23 Sufficient Conditions for Differentiability#^cor-23-2|§23.2]], [[§6 Differentiability#^thm-6-9|452 Thm. §6.9]] (chain rule)

> [!example] Example §24.1: The Function 1/z²
> If
>
> $$
> f(z) = \frac{1}{z^2} = \frac{1}{(re^{i\theta})^2} = \frac{1}{r^2}e^{-i2\theta} = \frac{1}{r^2}(\cos 2\theta - i\sin 2\theta) ,
> $$
>
> where $z \ne 0$, the component functions are
>
> $$
> u = \frac{\cos 2\theta}{r^2} \qquad\text{and}\qquad v = -\frac{\sin 2\theta}{r^2} .
> $$
>
> Since
>
> $$
> ru_r = -\frac{2\cos 2\theta}{r^2} = v_\theta, \qquad u_\theta = -\frac{2\sin 2\theta}{r^2} = -rv_r \quad \Big(v_r = \frac{2\sin 2\theta}{r^3}\Big) ,
> $$
>
> and since the partial derivatives are continuous at every nonzero point $z = re^{i\theta}$, Theorem §24.3 shows that the derivative of $f$ exists when $z \ne 0$. Moreover,
>
> $$
> f'(z) = e^{-i\theta}\Big(-\frac{2\cos 2\theta}{r^3} + i\frac{2\sin 2\theta}{r^3}\Big) = -2e^{-i\theta}\frac{e^{-i2\theta}}{r^3} = -\frac{2}{(re^{i\theta})^3} = -\frac{2}{z^3} ,
> $$
>
> in agreement with the power rule, [[§20 Rules for Differentiation#^thm-20-3|Theorem §20.3]].
>
> *B&C: Sec. 24, Example 1*

^ex-24-1

> [!example] Example §24.2: Branches of the Square Root
> Show that any branch
>
> $$
> f(z) = \sqrt r\,e^{i\theta/2} \qquad (r > 0,\ \alpha < \theta < \alpha + 2\pi)
> $$
>
> of the square root function $z^{1/2}$ has a derivative everywhere in its domain of definition. Here
>
> $$
> u(r, \theta) = \sqrt r\cos\frac\theta2 \qquad\text{and}\qquad v(r, \theta) = \sqrt r\sin\frac\theta2 .
> $$
>
> Inasmuch as
>
> $$
> ru_r = \frac{\sqrt r}{2}\cos\frac\theta2 = v_\theta \qquad\text{and}\qquad u_\theta = -\frac{\sqrt r}{2}\sin\frac\theta2 = -rv_r ,
> $$
>
> and the partial derivatives are continuous on the domain (an open set, on which $\theta$ is a continuous function of $z$), Theorem §24.3 shows that $f'(z)$ exists at each point where $f(z)$ is defined, and
>
> $$
> f'(z) = e^{-i\theta}\Big(\frac{1}{2\sqrt r}\cos\frac\theta2 + i\frac{1}{2\sqrt r}\sin\frac\theta2\Big) = \frac{1}{2\sqrt r}e^{-i\theta}e^{i\theta/2} = \frac{1}{2\sqrt r\,e^{i\theta/2}} = \frac{1}{2f(z)} .
> $$
>
> *B&C: Sec. 24, Example 2*

^ex-24-2

## The Complex Form of the Cauchy–Riemann Equations

> [!example] Example §24.3: The Equation ∂f/∂z̄ = 0
> **(a)** Since $z = x + iy$ and $\bar z = x - iy$ ([[§6 Complex Conjugates#^prop-6-2|Proposition §6.2]]),
>
> $$
> x = \frac{z + \bar z}{2}, \qquad y = \frac{z - \bar z}{2i} .
> $$
>
> Treat $z$ and $\bar z$ formally as independent variables. Since $\partial x/\partial\bar z = \frac12$ and $\partial y/\partial\bar z = -\frac{1}{2i} = \frac i2$, formally applying the chain rule to a function $F(x, y)$ gives
>
> $$
> \frac{\partial F}{\partial\bar z} = \frac{\partial F}{\partial x}\frac{\partial x}{\partial\bar z} + \frac{\partial F}{\partial y}\frac{\partial y}{\partial\bar z} = \frac12\Big(\frac{\partial F}{\partial x} + i\frac{\partial F}{\partial y}\Big) .
> $$
>
> **(b)** Define the operator
>
> $$
> \frac{\partial}{\partial\bar z} = \frac12\Big(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\Big) ,
> $$
>
> suggested by (a). For $f(z) = u(x, y) + iv(x, y)$,
>
> $$
> \frac{\partial f}{\partial\bar z} = \frac12\big(u_x + iv_x + iu_y - v_y\big) = \frac12\big[(u_x - v_y) + i(v_x + u_y)\big] .
> $$
>
> The real part vanishes exactly when $u_x = v_y$, and the imaginary part exactly when $u_y = -v_x$. So if the first-order partial derivatives of $u$ and $v$ satisfy the Cauchy–Riemann equations, then $\partial f/\partial\bar z = 0$, and conversely: **$\partial f/\partial\bar z = 0$ is the complex form of the Cauchy–Riemann equations.**
>
> **(c) Illustrations.** For $f = |z|^2 = z\bar z$, $\frac12(f_x + if_y) = \frac12(2x + i\,2y) = z$, which is what formal differentiation of $z\bar z$ in $\bar z$ gives; it vanishes only at $z = 0$, as in [[§22 Examples (Cauchy–Riemann Equations)#^ex-22-2|Example §22.2]]. For $f = x^2 - iy^2$, $\frac12(2x + i(-2iy)) = x + y$, which vanishes exactly on the line $y = -x$ ([[§25 Analytic Functions#^ex-25-3|Example §25.3]]). A function given by a formula in $z$ alone, such as a polynomial, has $\partial f/\partial\bar z = 0$ everywhere.
>
> *B&C: Sec. 24, Exercise 8; Source: 342 HW 3 (optional problems)*

^ex-24-3
