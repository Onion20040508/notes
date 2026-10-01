---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 7
tags: [multivariable-analysis, math452]
---
← [[§6 Differentiability]] · ↑ [[· 2 Differentiation]] · [[§8 The Differential]] →

A basic property of [[§6 Differentiability#^def-6-1|differentiable]] functions $f$ is that they not only possess [[§4 Partial Derivatives#^def-4-1|partial derivatives]] with respect to $x$ and $y$ — or, as we also say, in the $x$- and $y$-directions — but that they have derivatives in **any direction**, and these derivatives can all be expressed in terms of $f_x$ and $f_y$.

> [!definition] Definition §7.1: Directional Derivative
> By the **derivative in the direction $\alpha$** we mean the rate of change of $f$ at the point $(x, y)$ with respect to distance as we approach $(x, y)$ along the ray that forms the angle $\alpha$ with the positive $x$-axis.
>
> The points $(x + h, y + k)$ along this ray have the form
>
> $$
> h = \rho \cos \alpha, \qquad k = \rho \sin \alpha,
> $$
>
> where $\rho = \sqrt{h^2 + k^2}$ is the distance from $(x + h, y + k)$ to $(x, y)$.
>
> Along this ray, $f$ becomes a function of $\rho$:
>
> $$
> f(x + \rho \cos \alpha, \, y + \rho \sin \alpha).
> $$
>
> The **directional derivative** of $f$ at $(x, y)$ in the direction $\alpha$ is defined as:
>
> $$
> D_{(\alpha)} f(x, y) = \left( \frac{d}{d\rho} f(x + \rho \cos \alpha, \, y + \rho \sin \alpha) \right)\bigg|_{\rho = 0^+} = \lim_{\rho \to 0^+} \frac{f(x + \rho \cos \alpha, \, y + \rho \sin \alpha) - f(x, y)}{\rho},
> $$
>
> provided the limit exists. Since $\rho \ge 0$ is a distance, this is a one-sided limit: the right-hand derivative at $\rho = 0$.

^def-7-1

![[m452-7-1.svg]]
*The directional derivative restricts $f$ to a ray: points along the direction $\alpha$ have the form $(x + \rho\cos\alpha,\, y + \rho\sin\alpha)$, turning $f$ into a single-variable function of the distance $\rho$. Its derivative at $\rho = 0$ is $D_{(\alpha)}f$. The partials are the special cases $\alpha = 0$ and $\alpha = \pi/2$.*

> [!remark] Remark: Partial Derivatives as Special Cases
> The [[§4 Partial Derivatives#^def-4-1|partial derivatives]], when they exist, are directional derivatives in the coordinate directions:
>
> $$
> \begin{aligned}
> D_{(0)} f(x, y) &= \lim_{\rho \to 0^+} \frac{f(x + \rho, y) - f(x, y)}{\rho} = f_x(x, y), \\[6pt]
> D_{(\pi/2)} f(x, y) &= \lim_{\rho \to 0^+} \frac{f(x, y + \rho) - f(x, y)}{\rho} = f_y(x, y).
> \end{aligned}
> $$

^rem-7-1

> [!theorem] Theorem §7.1: Directional Derivative Formula
> If $f(x, y)$ is [[§6 Differentiability#^def-6-1|differentiable]] at $(x, y)$, then the directional derivative in direction $\alpha$ exists and is given by:
>
> $$
> D_{(\alpha)} f(x, y) = f_x(x, y) \cos \alpha + f_y(x, y) \sin \alpha.
> $$

^thm-7-1

> [!proof]+ Proof
> Since $f$ is differentiable ([[§6 Differentiability#^def-6-1|Def. §6.1]]), we have:
>
> $$
> f(x + h, y + k) - f(x, y) = h f_x + k f_y + \varepsilon \rho,
> $$
>
> where $\varepsilon \to 0$ as $\rho = \sqrt{h^2 + k^2} \to 0$.
>
> Substituting $h = \rho \cos \alpha$ and $k = \rho \sin \alpha$:
>
> $$
> f(x + \rho \cos \alpha, y + \rho \sin \alpha) - f(x, y) = \rho \cos \alpha \cdot f_x + \rho \sin \alpha \cdot f_y + \varepsilon \rho = \rho (f_x \cos \alpha + f_y \sin \alpha + \varepsilon).
> $$
>
> Dividing by $\rho$ and taking $\rho \to 0^+$:
>
> $$
> D_{(\alpha)} f(x, y) = \lim_{\rho \to 0^+} \frac{f(x + \rho \cos \alpha, y + \rho \sin \alpha) - f(x, y)}{\rho} = f_x \cos \alpha + f_y \sin \alpha + \lim_{\rho \to 0^+} \varepsilon = f_x \cos \alpha + f_y \sin \alpha.
> $$

^pf-7-1

*Uses:* [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§7 Directional Derivatives#^def-7-1|Def. §7.1]]

> [!remark]- Connections
> - The same result in unit-vector form, with $L = Df$ the total derivative: [[§6 Differentiability#^thm-6-1|Theorem §6.1]]; the converse is false ([[§6 Differentiability#^rem-6-4|warning]]).
> - In forms language the differential eats a direction and returns this derivative: [[§22 The Algebra of Differential Forms#^prop-22-6|Gradient = Differential = 1-Form]].

> [!remark] Remark: Unit Vector Notation
> If $\mathbf{u} = (a, b)$ is a **unit vector** (so $a^2 + b^2 = 1$), we can write $a = \cos \alpha$ and $b = \sin \alpha$ for some angle $\alpha$. Then:
>
> $$
> D_{\mathbf{u}} f(x, y) = f_x(x, y) \cdot a + f_y(x, y) \cdot b = \nabla f \cdot \mathbf{u},
> $$
>
> where $\nabla f = (f_x, f_y)$ is the **gradient** of $f$.

^rem-7-2

> [!remark] Remark: Gradient and Maximum Rate of Change
> The directional derivative $D_{(\alpha)} f = f_x \cos \alpha + f_y \sin \alpha = |\nabla f| \cos(\alpha - \theta)$, where $\theta$ is the angle of the gradient vector.
>
> This is maximized when $\alpha = \theta$, i.e., when we move in the direction of the gradient. The maximum rate of change is $|\nabla f| = \sqrt{f_x^2 + f_y^2}$.

^rem-7-3

![[m452-7-2.svg]]
*The gradient as a field on the contour map of $F = x^2/4 + y^2$ (contours $F = c$ for $c = \tfrac12, 1, \tfrac32, 2$, values marked on the left). At every point, $\nabla F = (x/2,\,2y)$ is perpendicular to the contour through that point and points toward higher values. Its length encodes steepness: at $(0,1)$ the contours are packed twice as tightly as at $(2,0)$, and the gradient is exactly twice as long. Along any contour the tangential directional derivative vanishes (green tangent) — moving along a level curve changes nothing; moving across contours, the shorter the crossing distance, the larger $|\nabla F|$.*

> [!remark]- Connections
> - The same maximization is the equality case of the [[Cauchy–Schwarz inequality]]: $\nabla f \cdot \mathbf{u} \le |\nabla f|\,|\mathbf{u}|$, with equality iff $\mathbf{u}$ is a positive multiple of $\nabla f$.
> - Gradient perpendicular to level curves is the geometry behind [[Method of Lagrange Multipliers|Lagrange multipliers (§14.2)]]; the gradient in $\mathbb{R}^n$ returns in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]] and [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|Def. §17.2]].
