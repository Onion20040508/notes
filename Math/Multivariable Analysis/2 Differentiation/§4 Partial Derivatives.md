---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 4
tags: [multivariable-analysis, math452]
---
← [[§3 Continuity and Limits of Functions]] · ↑ [[2 Differentiation]] · [[§5 Equality of Mixed Partials]] →

> [!definition] Definition §4.1: Partial Derivatives
> For $f : \mathbb{R}^2 \to \mathbb{R}$ defined near $(x, y)$:
>
> $$
> f_x(x, y) = \frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x + h, y) - f(x, y)}{h}, \qquad f_y(x, y) = \frac{\partial f}{\partial y} = \lim_{k \to 0} \frac{f(x, y + k) - f(x, y)}{k}.
> $$

^def-4-1

![[m452-4-1.svg]]
*Partial derivatives are ordinary derivatives of slice curves: cutting the surface along $y = y_0$ gives a single-variable function of $x$ whose slope at the point is $f_x$; cutting along $x = x_0$ gives the $f_y$ slice. Each partial sees only its own slice — this is why the existence of both partials is far weaker than differentiability ([[§6 Differentiability|§6]]).*

> [!remark]- Connections
> - Each partial is the MATH 451 [[§28 Basic Properties of the Derivative#^def-28-1|derivative]] of a one-variable slice; the partial in an arbitrary direction is the [[§7 Directional Derivatives#^def-7-1|directional derivative]] of §7.

> [!example] Example §4.1: Partials Exist but Function Discontinuous
> Let $f(x, y) = \dfrac{2xy}{x^2 + y^2}$ for $(x,y) \neq (0,0)$ and $f(0,0) = 0$. Then
>
> $$
> f_x(0, 0) = \lim_{h \to 0} \frac{f(h, 0) - f(0, 0)}{h} = 0, \qquad f_y(0, 0) = 0.
> $$
>
> So partial derivatives exist at $(0, 0)$, but $f$ is [[§3 Continuity and Limits of Functions#^ex-3-2|not continuous there]].

^ex-4-1

> [!theorem] Theorem §4.1: Bounded Partials Imply Continuity
> Let $R$ be an open rectangle. If $f_x$ and $f_y$ both exist on $R$ and are bounded (i.e., $|f_x|, |f_y| \leq M$ for some $M > 0$), then $f$ is continuous on $R$.

^thm-4-1

> [!proof]+ Proof
> Let $(x_0, y_0) \in R$ and let $\varepsilon > 0$. Since $R$ is [[§2 Open and Closed Sets#^def-2-4|open]], there exists $r > 0$ such that $B((x_0, y_0), r) \subseteq R$.
>
> For $(h, k)$ with $|(h, k)| < r$, the points $(x_0, y_0)$, $(x_0 + h, y_0)$, and $(x_0 + h, y_0 + k)$ all lie in $R$. By the [[§3 The Set ℝ of Real Numbers#^thm-3-3|triangle inequality]]:
>
> $$
> |f(x_0 + h, y_0 + k) - f(x_0, y_0)| \leq |f(x_0 + h, y_0 + k) - f(x_0 + h, y_0)| + |f(x_0 + h, y_0) - f(x_0, y_0)|.
> $$
>
> **Second term:** Define $g(x) = f(x, y_0)$ for $x \in [x_0, x_0 + h]$ (or $[x_0 + h, x_0]$ if $h < 0$). Since $f_x$ exists on $R$, the function $g$ is differentiable with $g'(x) = f_x(x, y_0)$. By the [[Mean Value Theorem]], there exists $\theta(h) \in [0, 1]$ such that
>
> $$
> g(x_0 + h) - g(x_0) = h \cdot g'(x_0 + \theta(h) \cdot h) = h \cdot f_x(x_0 + \theta(h) \cdot h, y_0).
> $$
>
> Since $|f_x| \leq M$, we have $|f(x_0 + h, y_0) - f(x_0, y_0)| \leq M|h|$.
>
> **First term:** Define $\psi(y) = f(x_0 + h, y)$ for $y \in [y_0, y_0 + k]$. By MVT, there exists $\eta(h, k) \in [0, 1]$ such that
>
> $$
> \psi(y_0 + k) - \psi(y_0) = k \cdot \psi'(y_0 + \eta(h,k) \cdot k) = k \cdot f_y(x_0 + h, y_0 + \eta(h,k) \cdot k).
> $$
>
> Since $|f_y| \leq M$, we have $|f(x_0 + h, y_0 + k) - f(x_0 + h, y_0)| \leq M|k|$.
>
> (Note: $\theta$ depends on $h$; $\eta$ depends on $h$ and $k$. But the bounds $M|h|$ and $M|k|$ are uniform.)
>
> **Combining:**
>
> $$
> |f(x_0 + h, y_0 + k) - f(x_0, y_0)| \leq M|h| + M|k| \leq 2M\sqrt{h^2 + k^2}.
> $$
>
> Let $\delta = \min\left(r, \dfrac{\varepsilon}{2M}\right)$. Then for $|(h, k)| < \delta$:
>
> $$
> |f(x_0 + h, y_0 + k) - f(x_0, y_0)| \leq 2M \cdot \delta \leq \varepsilon.
> $$
>
> Hence $f$ is [[§3 Continuity and Limits of Functions#^def-3-1|continuous]] at $(x_0, y_0)$.

^pf-4-1

*Uses:* [[§2 Open and Closed Sets#^def-2-4|Def. §2.4]], [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§3 The Set ℝ of Real Numbers#^thm-3-3|451 §3.3]], [[Mean Value Theorem|451 §29.3]]

![[m452-4-2.svg]]
*The proof walks from $(x_0,y_0)$ to $(x_0+h,\,y_0+k)$ along an L-shaped path (blue) instead of the direct segment (dashed): first in $x$, then in $y$. On each leg only one variable moves, so the one-variable MVT applies, evaluating $f_x$ at $(x_0+\theta(h)h,\,y_0)$ and $f_y$ at $(x_0+h,\,y_0+\eta(h,k)k)$ (red). The bound $|f_x|, |f_y| \le M$ caps each leg's change at $M|h|$ and $M|k|$; the whole path stays in $B((x_0,y_0),r) \subseteq R$, which is why $R$ must be open.*

> [!example] Example §4.2: Second Partials of $r = \sqrt{x^2 + y^2}$
>
> $$
> r_x = \frac{x}{r}, \quad r_y = \frac{y}{r}, \quad r_{xx} = \frac{r^2 - x^2}{r^3}, \quad r_{yy} = \frac{r^2 - y^2}{r^3}, \quad r_{xy} = r_{yx} = -\frac{xy}{r^3}.
> $$
>
> Note: $\Delta r = r_{xx} + r_{yy} = \dfrac{1}{r}$.

^ex-4-2
