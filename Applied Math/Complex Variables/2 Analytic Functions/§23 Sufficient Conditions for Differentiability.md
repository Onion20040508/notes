---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 23
bc: "23"
aliases: ["B&C 23"]
tags: [complex-variables, math342]
---
← [[§22 Examples (Cauchy–Riemann Equations)]] · ↑ [[· 2 Analytic Functions]] · [[§24★ Polar Coordinates]] →

*Brown–Churchill, Section 23 · MAT 342 HW 3.*

The Cauchy–Riemann equations at a point do not guarantee a derivative there ([[§22 Examples (Cauchy–Riemann Equations)#^ex-22-3|Example §22.3]]). This section shows that they do once the first-order partial derivatives of $u$ and $v$ exist near the point and are continuous at it; then $f'(z_0) = u_x + iv_x$. Together with the necessary condition, [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]], this gives the working test for differentiability used throughout the course: solve the Cauchy–Riemann equations, check continuity of the partials, and read off the derivative. The proof is a two-variable linear approximation of $u$ and $v$, in which the Cauchy–Riemann equations make the linear part a complex multiple of $\Delta z$.

## The Theorem

> [!theorem] Theorem §23.1: Sufficient Conditions for Differentiability
> Let the function
>
> $$
> f(z) = u(x, y) + iv(x, y)
> $$
>
> be defined throughout some $\varepsilon$ neighborhood of a point $z_0 = x_0 + iy_0$, and suppose that
>
> **(a)** the first-order partial derivatives of the functions $u$ and $v$ with respect to $x$ and $y$ exist everywhere in the neighborhood;
>
> **(b)** those partial derivatives are continuous at $(x_0, y_0)$ and satisfy the Cauchy–Riemann equations
>
> $$
> u_x = v_y, \qquad u_y = -v_x
> $$
>
> at $(x_0, y_0)$.
>
> Then $f'(z_0)$ exists, its value being
>
> $$
> f'(z_0) = u_x + iv_x ,
> $$
>
> where the right-hand side is to be evaluated at $(x_0, y_0)$.
>
> *B&C: Sec. 23, Theorem*

^thm-23-1

> [!proof]+ Proof
> Assume (a) and (b), and write $\Delta z = \Delta x + i\Delta y$, where $0 < |\Delta z| < \varepsilon$, as well as $\Delta w = f(z_0 + \Delta z) - f(z_0)$. Thus
>
> $$
> \Delta w = \Delta u + i\Delta v , \qquad (1)
> $$
>
> where $\Delta u = u(x_0 + \Delta x, y_0 + \Delta y) - u(x_0, y_0)$ and $\Delta v = v(x_0 + \Delta x, y_0 + \Delta y) - v(x_0, y_0)$.
>
> **Step 1: linear approximation of $u$ and $v$.** The continuity of the first-order partial derivatives at $(x_0, y_0)$ enables us to write
>
> $$
> \Delta u = u_x(x_0, y_0)\Delta x + u_y(x_0, y_0)\Delta y + \varepsilon_1\Delta x + \varepsilon_2\Delta y \qquad (2)
> $$
>
> and
>
> $$
> \Delta v = v_x(x_0, y_0)\Delta x + v_y(x_0, y_0)\Delta y + \varepsilon_3\Delta x + \varepsilon_4\Delta y , \qquad (3)
> $$
>
> where $\varepsilon_1, \varepsilon_2, \varepsilon_3, \varepsilon_4$ tend to zero as $(\Delta x, \Delta y)$ approaches $(0, 0)$. (B&C cites an advanced calculus text for this; here is why.) Go from $(x_0, y_0)$ to $(x_0 + \Delta x, y_0 + \Delta y)$ first vertically, then horizontally:
>
> $$
> \Delta u = \big[u(x_0 + \Delta x, y_0 + \Delta y) - u(x_0, y_0 + \Delta y)\big] + \big[u(x_0, y_0 + \Delta y) - u(x_0, y_0)\big] .
> $$
>
> The points $(x_0 + s\Delta x, y_0 + \Delta y)$ and $(x_0, y_0 + s\Delta y)$, $0 \le s \le 1$, are at distance at most $|\Delta z| < \varepsilon$ from $z_0$, so they lie in the neighborhood, where $u_x$ and $u_y$ exist by (a). Hence $g(s) = u(x_0 + s\Delta x, y_0 + \Delta y)$ is differentiable on $[0, 1]$ with $g'(s) = u_x(x_0 + s\Delta x, y_0 + \Delta y)\Delta x$, and the mean value theorem gives an $s_1 \in (0, 1)$ with
>
> $$
> u(x_0 + \Delta x, y_0 + \Delta y) - u(x_0, y_0 + \Delta y) = g(1) - g(0) = u_x(x_0 + s_1\Delta x, y_0 + \Delta y)\,\Delta x .
> $$
>
> In the same way the second bracket is $u_y(x_0, y_0 + s_2\Delta y)\,\Delta y$ for some $s_2 \in (0, 1)$. (If $\Delta x = 0$ or $\Delta y = 0$, the corresponding bracket is $0$ and any $s_1$ or $s_2$ will do.) Put
>
> $$
> \varepsilon_1 = u_x(x_0 + s_1\Delta x, y_0 + \Delta y) - u_x(x_0, y_0), \qquad \varepsilon_2 = u_y(x_0, y_0 + s_2\Delta y) - u_y(x_0, y_0) .
> $$
>
> Then (2) holds, and since the points at which $u_x$ and $u_y$ are evaluated are within $|\Delta z|$ of $(x_0, y_0)$, the continuity of $u_x$ and $u_y$ at $(x_0, y_0)$ gives $\varepsilon_1, \varepsilon_2 \to 0$ as $\Delta z \to 0$. The same argument applied to $v$ gives (3).
>
> **Step 2: the Cauchy–Riemann equations.** Substituting (2) and (3) into (1),
>
> $$
> \Delta w = u_x(x_0, y_0)\Delta x + u_y(x_0, y_0)\Delta y + \varepsilon_1\Delta x + \varepsilon_2\Delta y + i\big[v_x(x_0, y_0)\Delta x + v_y(x_0, y_0)\Delta y + \varepsilon_3\Delta x + \varepsilon_4\Delta y\big] . \qquad (4)
> $$
>
> Because the Cauchy–Riemann equations hold at $(x_0, y_0)$, we may replace $u_y(x_0, y_0)$ by $-v_x(x_0, y_0)$ and $v_y(x_0, y_0)$ by $u_x(x_0, y_0)$. The linear terms then become
>
> $$
> u_x\Delta x - v_x\Delta y + iv_x\Delta x + iu_x\Delta y = (u_x + iv_x)(\Delta x + i\Delta y) = (u_x + iv_x)\,\Delta z ,
> $$
>
> and dividing through by $\Delta z$,
>
> $$
> \frac{\Delta w}{\Delta z} = u_x(x_0, y_0) + iv_x(x_0, y_0) + (\varepsilon_1 + i\varepsilon_3)\frac{\Delta x}{\Delta z} + (\varepsilon_2 + i\varepsilon_4)\frac{\Delta y}{\Delta z} . \qquad (5)
> $$
>
> **Step 3: the error terms vanish.** By the inequalities $|\Delta x| \le |\Delta z|$ and $|\Delta y| \le |\Delta z|$ of [[§4 Vectors and Moduli#^prop-4-1|Proposition §4.1]] (inequalities (3)),
>
> $$
> \Big|\frac{\Delta x}{\Delta z}\Big| \le 1 \qquad\text{and}\qquad \Big|\frac{\Delta y}{\Delta z}\Big| \le 1 .
> $$
>
> Consequently
>
> $$
> \Big|(\varepsilon_1 + i\varepsilon_3)\frac{\Delta x}{\Delta z}\Big| \le |\varepsilon_1 + i\varepsilon_3| \le |\varepsilon_1| + |\varepsilon_3|
> \qquad\text{and}\qquad
> \Big|(\varepsilon_2 + i\varepsilon_4)\frac{\Delta y}{\Delta z}\Big| \le |\varepsilon_2| + |\varepsilon_4| ,
> $$
>
> and the last two terms on the right in (5) tend to zero as $\Delta z \to 0$. So $\Delta w/\Delta z \to u_x + iv_x$ at $(x_0, y_0)$: $f'(z_0)$ exists and has that value.

^pf-23-1

*Uses:* [[§4 Vectors and Moduli#^prop-4-1|§4.1]], [[§19 Derivatives#^def-19-1|Def. §19.1]], [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (mean value theorem)

> [!remark]- Connections
> - Step 1 is the theorem that continuous partials imply differentiability, [[§6 Differentiability#^thm-6-2|452 Thm. §6.2]] (stated there for partials continuous on an open set; the proof above needs continuity only at the point). Equations (2)–(3) say that $u$ and $v$ are differentiable at $(x_0, y_0)$ in the sense of [[§6 Differentiability#^def-6-1|452 Def. §6.1]].
> - With $f'(z_0) = a + ib$, the Cauchy–Riemann equations say that the Jacobian matrix of $(u, v)$ at $(x_0, y_0)$ is $\begin{bmatrix} u_x & u_y \\ v_x & v_y \end{bmatrix} = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$, a rotation–scaling matrix, [[§36 Complex Eigenvalues#^prop-36-3|235 Prop. §36.3]]: the linear part of $\Delta w$ is multiplication by $f'(z_0)$, a rotation through $\arg f'(z_0)$ followed by a stretch by $|f'(z_0)|$. This is the geometric content of complex differentiability, and the source of conformality in Ch. 9.

The proof used hypotheses (a) and (b) only to obtain (2) and (3). So the conclusion holds whenever $u$ and $v$ admit such linear approximations at the point; this form is needed in [[§24★ Polar Coordinates#^thm-24-3|Theorem §24.3]].

> [!theorem] Corollary §23.2: Real Differentiability Plus Cauchy–Riemann
> Let $f(z) = u(x, y) + iv(x, y)$ be defined in a neighborhood of $z_0 = x_0 + iy_0$. If $u$ and $v$ are differentiable at $(x_0, y_0)$, that is,
>
> $$
> \Delta u = u_x\Delta x + u_y\Delta y + R_u, \qquad \Delta v = v_x\Delta x + v_y\Delta y + R_v, \qquad \frac{R_u}{|\Delta z|} \to 0, \quad \frac{R_v}{|\Delta z|} \to 0 ,
> $$
>
> with the partial derivatives evaluated at $(x_0, y_0)$, and if $u_x = v_y$, $u_y = -v_x$ at $(x_0, y_0)$, then $f'(z_0)$ exists and $f'(z_0) = u_x + iv_x$ there.
>
> *B&C: Sec. 23 (proof of the Theorem)*

^cor-23-2

> [!proof]+ Proof
> Put $\varepsilon_1 = R_u\Delta x/|\Delta z|^2$ and $\varepsilon_2 = R_u\Delta y/|\Delta z|^2$. Then $\varepsilon_1\Delta x + \varepsilon_2\Delta y = R_u(\Delta x^2 + \Delta y^2)/|\Delta z|^2 = R_u$, and $|\varepsilon_1|, |\varepsilon_2| \le |R_u|/|\Delta z| \to 0$. So (2) holds with $\varepsilon_1, \varepsilon_2 \to 0$; likewise (3) with $\varepsilon_3, \varepsilon_4$ built from $R_v$. Steps 2 and 3 of the proof of [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] use nothing else, and give $f'(z_0) = u_x + iv_x$.

^pf-23-2

*Uses:* [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]]

Conversely, if $f'(z_0)$ exists, then $\Delta w = f'(z_0)\Delta z + \eta\,\Delta z$ with $\eta \to 0$, and taking real and imaginary parts shows that $u$ and $v$ are differentiable at $(x_0, y_0)$. So **$f'(z_0)$ exists if and only if $u$ and $v$ are differentiable at $(x_0, y_0)$ and satisfy the Cauchy–Riemann equations there.**

## Using the Theorem

> [!remark] Remark: Method — Checking Differentiability with Cauchy–Riemann
> To find where $f$ is differentiable and compute $f'$:
> 1. **Components.** Substitute $z = x + iy$ and separate $f(z) = u(x, y) + iv(x, y)$.
> 2. **Partials.** Compute $u_x, u_y, v_x, v_y$ and note where they are continuous (for polynomials, exponentials and trigonometric functions of $x$ and $y$: everywhere).
> 3. **Candidates.** Solve $u_x = v_y$, $u_y = -v_x$ simultaneously. At points that fail, $f'$ does not exist ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]).
> 4. **Sufficiency.** At each solution $z_0$ where the partials exist nearby and are continuous at $z_0$, $f'(z_0)$ exists (Theorem §23.1).
> 5. **Derivative.** Only now evaluate $f'(z_0) = u_x + iv_x$ at the point (or $v_y - iu_y$). Writing down $u_x + iv_x$ as a formula for $f'$ before step 3 is a mistake whenever the candidates are not the whole region (Example §23.3).
>
> If the candidates form a curve or isolated points, $f$ is differentiable there but analytic nowhere ([[§25 Analytic Functions#^ex-25-3|Example §25.3]]).

^rem-23-1

> [!example] Example §23.1: The Function eˣeⁱʸ
> Consider $f(z) = e^xe^{iy} = e^x\cos y + ie^x\sin y$, where $y$ is to be taken in radians. Here
>
> $$
> u(x, y) = e^x\cos y, \qquad v(x, y) = e^x\sin y ,
> $$
>
> $$
> u_x = e^x\cos y = v_y, \qquad u_y = -e^x\sin y = -v_x
> $$
>
> everywhere, and these derivatives are everywhere continuous. So the conditions of Theorem §23.1 hold at all points of the complex plane, $f'(z)$ exists everywhere, and
>
> $$
> f'(z) = u_x + iv_x = e^x\cos y + ie^x\sin y = f(z) \qquad\text{for all } z .
> $$
>
> This is the function $e^z$ of [[§30 The Exponential Function#^def-30-1|Definition §30.1]].
>
> *B&C: Sec. 23, Example 1*

^ex-23-1

> [!example] Example §23.2: |z|² Has a Derivative at 0
> The function $f(z) = |z|^2$ has components $u(x, y) = x^2 + y^2$ and $v(x, y) = 0$, with $u_x = 2x$, $u_y = 2y$, $v_x = v_y = 0$, all continuous everywhere. At the origin, $u_x = 0 = v_y$ and $u_y = 0 = -v_x$, so by Theorem §23.1 $f'(0)$ exists and
>
> $$
> f'(0) = u_x(0, 0) + iv_x(0, 0) = 0 + i0 = 0 .
> $$
>
> By [[§22 Examples (Cauchy–Riemann Equations)#^ex-22-2|Example §22.2]], $f'(z)$ exists at no other point.
>
> *B&C: Sec. 23, Example 2*

^ex-23-2

> [!example] Example §23.3: Do Not Use u_x + iv_x Before Existence
> Consider $f(z) = x^3 + i(1 - y)^3$, so $u(x, y) = x^3$ and $v(x, y) = (1 - y)^3$. It would be a mistake to say that $f'(z)$ exists everywhere and that
>
> $$
> f'(z) = u_x + iv_x = 3x^2 . \qquad (6)
> $$
>
> Indeed $u_x = 3x^2$, $u_y = 0$, $v_x = 0$, $v_y = -3(1 - y)^2$. The first Cauchy–Riemann equation $u_x = v_y$ reads $3x^2 = -3(1 - y)^2$, which can hold only if
>
> $$
> x^2 + (1 - y)^2 = 0 , \qquad (7)
> $$
>
> and the second equation $u_y = -v_x$ is always satisfied ($0 = 0$). Condition (7) says $x = 0$ and $y = 1$, so $f'(z)$ can exist only at $z = i$. The partials are continuous everywhere, so by Theorem §23.1 $f'(z)$ exists **only** when $z = i$, and then, by (6) evaluated at that point, $f'(i) = 3 \cdot 0^2 = 0$.
>
> *B&C: Sec. 23, Example 3*

^ex-23-3

> [!example] Example §23.4: The Function (z² + 1) z̄
> Where is $f(z) = (z^2 + 1)\bar z$ differentiable? Compute $f'$ there.
>
> **Components.** $z^2 + 1 = (x^2 - y^2 + 1) + i\,2xy$, and multiplying by $\bar z = x - iy$,
>
> $$
> u = x(x^2 - y^2 + 1) + 2xy^2 = x^3 + xy^2 + x, \qquad v = -y(x^2 - y^2 + 1) + 2x^2y = x^2y + y^3 - y .
> $$
>
> **Partials** (all continuous everywhere):
>
> $$
> u_x = 3x^2 + y^2 + 1, \quad u_y = 2xy, \qquad v_x = 2xy, \quad v_y = x^2 + 3y^2 - 1 .
> $$
>
> **Candidates.** $u_y = -v_x$ says $2xy = -2xy$, that is $xy = 0$. And $u_x = v_y$ says $3x^2 + y^2 + 1 = x^2 + 3y^2 - 1$, that is $y^2 = x^2 + 1$.
> - If $x = 0$: $y^2 = 1$, so $y = \pm1$.
> - If $y = 0$: $x^2 = -1$, impossible for real $x$.
>
> So the Cauchy–Riemann equations hold exactly at $z = i$ and $z = -i$.
>
> **Conclusion.** By Theorem §23.1, $f$ is differentiable at $\pm i$ and nowhere else, with
>
> $$
> f'(\pm i) = u_x(0, \pm1) + iv_x(0, \pm1) = (0 + 1 + 1) + i \cdot 0 = 2 .
> $$
>
> (Check with the complex form of the Cauchy–Riemann equations, [[§24★ Polar Coordinates#^ex-24-3|Example §24.3]]: treating $z$ and $\bar z$ in $f = z^2\bar z + \bar z$ as independent variables, $\partial f/\partial\bar z = z^2 + 1$, which vanishes exactly at $z = \pm i$; and the $z$-derivative $2z\bar z = 2|z|^2$ equals $2$ there.)
>
> *Source: 342 HW 3, Q2(a)*

^ex-23-4

> [!example] Example §23.5: The Function e⁻ˣe⁻ⁱʸ and Its Second Derivative
> Show that $f(z) = e^{-x}e^{-iy}$ and $f'(z)$ are differentiable everywhere, and find $f''(z)$.
>
> **$f$.** $f(z) = e^{-x}\cos y - ie^{-x}\sin y$, so $u = e^{-x}\cos y$, $v = -e^{-x}\sin y$, and
>
> $$
> u_x = -e^{-x}\cos y = v_y, \qquad u_y = -e^{-x}\sin y = -v_x \quad (v_x = e^{-x}\sin y)
> $$
>
> everywhere, with continuous partials. By Theorem §23.1, $f'(z)$ exists everywhere and
>
> $$
> f'(z) = u_x + iv_x = -e^{-x}\cos y + ie^{-x}\sin y = -f(z) .
> $$
>
> **$f'$.** Write $f'(z) = U + iV$ with $U = -e^{-x}\cos y$, $V = e^{-x}\sin y$. Then
>
> $$
> U_x = e^{-x}\cos y = V_y, \qquad U_y = e^{-x}\sin y = -V_x \quad (V_x = -e^{-x}\sin y) ,
> $$
>
> again continuous everywhere, so $f''(z)$ exists everywhere and
>
> $$
> f''(z) = U_x + iV_x = e^{-x}\cos y - ie^{-x}\sin y = f(z) .
> $$
>
> (With [[§30 The Exponential Function#^def-30-1|Definition §30.1]], $f(z) = e^{-x - iy} = e^{-z}$, and the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]) gives $f' = -e^{-z}$, $f'' = e^{-z}$.)
>
> *B&C: Sec. 24, Exercise 2(b); Source: 342 HW 3, Q2(b)*

^ex-23-5
