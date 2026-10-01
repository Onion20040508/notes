---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 3
section: 12
tags: [multivariable-analysis, math452]
---
← [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence]] · ↑ [[· 3 Existence Theorems and Applications]] · [[§13 The Inverse Function Theorem]] →

## Motivation: Curves Defined Implicitly

Consider the equation $x^2 + y^2 = 1$ (a circle). This defines $y$ as a function of $x$ *implicitly* — we can solve to get $y = \pm\sqrt{1 - x^2}$, but only locally (we must choose a branch).

![[m452-12-1.svg]]
*The unit circle $x^2 + y^2 = 1$ (blue) is not the graph of any function of $x$, but it is locally: over the interval $|x - x_0| < \delta$ (red, open endpoints), the part of the circle near $(x_0, y_0)$ is the graph of a single function $y = f(x)$ (red arc) — here the upper branch $\sqrt{1 - x^2}$. The theorem produces exactly this local picture.*

More generally, given $F(x, y) = 0$, when can we solve for $y = f(x)$ near a point $(x_0, y_0)$ on the curve?

**Key insight:** If $F(a, b) = 0$ and the curve is not “vertical” at $(a, b)$ (i.e., $F_y(a, b) \neq 0$), then we can locally solve for $y$ as a function of $x$.

## Statement of the Theorem

> [!theorem] Theorem §12.1: Implicit Function Theorem
> Let $F : \mathbb{R}^2 \to \mathbb{R}$ satisfy the following conditions:
> - (i) $F(x_0, y_0) = 0$
> - (ii) $F_y(x_0, y_0) \neq 0$
> - (iii) $F_x$ and $F_y$ are continuous in a neighborhood $B((x_0, y_0); \varepsilon)$
>
> Then there exist $\delta, \eta > 0$ and a function $f : (x_0 - \delta, x_0 + \delta) \to (y_0 - \eta, y_0 + \eta)$, unique among functions with values in $(y_0 - \eta, y_0 + \eta)$, such that:
> - (a) $f(x_0) = y_0$
> - (b) $F(x, f(x)) = 0$ for all $x \in (x_0 - \delta, x_0 + \delta)$
> - (c) $f$ is continuous on $(x_0 - \delta, x_0 + \delta)$
> - (d) $f$ is differentiable, with
>
> $$
> f'(x) = -\frac{F_x(x, f(x))}{F_y(x, f(x))}
> $$

^thm-12-1

> [!remark]- Connections
> - MATH 451 relative: the one-variable [[§29 The Mean Value Theorem#^thm-29-10|Inverse Function Theorem]] (451 §29.10) — also “$f' \neq 0$ gives a local inverse, with derivative $1/f'$.”
> - Used twice to prove the [[Inverse Function Theorem (several variables)|Inverse Function Theorem]] (§13.2), and to derive [[Method of Lagrange Multipliers|Lagrange multipliers]] (§14.2).
> - Reappears in the second proof of the [[§15 Multivariable Integration#^thm-15-14|change of variables formula]] (§15.14).

## Proof of the Implicit Function Theorem

The proof proceeds in several steps: (1) establish existence of $f$, (2) prove uniqueness, (3) prove continuity, (4) prove differentiability.

> [!proof]+ Proof
> Without loss of generality, assume $F_y(x_0, y_0) = a > 0$. (If $a < 0$, replace $F$ by $-F$.)
>
> **Step 1: Setting up the neighborhood.**
>
> Since $F_y$ is continuous at $(x_0, y_0)$ and $F_y(x_0, y_0) = a > 0$, there exists $\delta_1 > 0$ such that
>
> $$
> |x - x_0| < \delta_1 \text{ and } |y - y_0| < \delta_1 \implies F_y(x, y) > \frac{a}{2} > 0.
> $$
>
> This means $F$ is **strictly increasing in $y$** throughout the box $[x_0 - \delta_1, x_0 + \delta_1] \times [y_0 - \delta_1, y_0 + \delta_1]$ ([[§29 The Mean Value Theorem#^cor-29-7|451 §29.7]]).
>
> **Step 2: Sign conditions on the boundary.**
>
> Fix $x = x_0$. Since $F(x_0, \cdot)$ is strictly increasing in $y$ and $F(x_0, y_0) = 0$:
>
> $$
> F(x_0, y_0 + \delta_1) > F(x_0, y_0) = 0, \qquad F(x_0, y_0 - \delta_1) < F(x_0, y_0) = 0.
> $$
>
> Since $F$ is continuous (because $F_x, F_y$ exist and are continuous; [[Continuous Partials Imply Differentiability|Theorem §6.2]]), there exists $\delta_2 > 0$ such that for all $x \in [x_0 - \delta_2, x_0 + \delta_2]$:
>
> $$
> F(x, y_0 + \delta_1) > 0, \qquad F(x, y_0 - \delta_1) < 0.
> $$
>
> (We apply continuity of $F$ at the two points $(x_0, y_0 + \delta_1)$ and $(x_0, y_0 - \delta_1)$, obtaining radii $\delta_2'$ and $\delta_2''$ respectively, then take $\delta_2 = \min\{\delta_2', \delta_2''\}$.)
>
> **Step 3: Existence of $f(x)$ via the Intermediate Value Theorem.**
>
> Let $\delta = \min\{\delta_1, \delta_2\}$. For each fixed $x \in [x_0 - \delta, x_0 + \delta]$:
> - The function $y \mapsto F(x, y)$ is continuous on $[y_0 - \delta_1, y_0 + \delta_1]$
> - $F(x, y_0 - \delta_1) < 0$ and $F(x, y_0 + \delta_1) > 0$
>
> By the [[Intermediate Value Theorem]], there exists $y \in (y_0 - \delta_1, y_0 + \delta_1)$ such that $F(x, y) = 0$.
>
> Define $f(x)$ to be this $y$-value.
>
> **Step 4: Uniqueness of $f(x)$.**
>
> Suppose there exist $y_1, y_2 \in (y_0 - \delta_1, y_0 + \delta_1)$ with $y_1 < y_2$ and $F(x, y_1) = F(x, y_2) = 0$.
>
> Since $F_y(x, y) > \frac{a}{2} > 0$ throughout the box, $F(x, \cdot)$ is strictly increasing. But then $F(x, y_1) < F(x, y_2)$, contradicting $F(x, y_1) = F(x, y_2) = 0$.
>
> Hence $f(x)$ is uniquely defined. This is the (local) uniqueness in the theorem, with $\eta = \delta_1$.
>
> **Step 5: Continuity of $f$.**
>
> We prove $f$ is continuous at $x_0$. (The proof at other points is identical.)
>
> Let $\varepsilon > 0$ be given, with $\varepsilon < \delta_1$. We need to find $\delta > 0$ such that
>
> $$
> |x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon.
> $$
>
> We work within the rectangle $[x_0 - \delta, x_0 + \delta] \times [y_0 - \varepsilon, y_0 + \varepsilon]$, where $F_y > a/2 > 0$ (so $F$ is strictly increasing in $y$).
>
> Since $F_y > \frac{a}{2}$ in the box, we have ([[§29 The Mean Value Theorem#^prop-29-8|451 §29.8]]):
>
> $$
> F(x_0, y_0 + \varepsilon) \geq F(x_0, y_0) + \frac{a}{2} \cdot \varepsilon = \frac{a\varepsilon}{2} > 0.
> $$
>
> Similarly, $F(x_0, y_0 - \varepsilon) \leq F(x_0, y_0) - \frac{a}{2} \cdot \varepsilon = -\frac{a\varepsilon}{2} < 0$.
>
> By continuity of $F$, there exists $\delta' > 0$ such that for $|x - x_0| < \delta'$:
>
> $$
> F(x, y_0 + \varepsilon) > 0, \qquad F(x, y_0 - \varepsilon) < 0.
> $$
>
> For such $x$, since $F(x, f(x)) = 0$ and $F(x, \cdot)$ is strictly increasing:
>
> $$
> F(x, y_0 - \varepsilon) < 0 = F(x, f(x)) < F(x, y_0 + \varepsilon).
> $$
>
> Therefore $y_0 - \varepsilon < f(x) < y_0 + \varepsilon$, i.e., $|f(x) - y_0| < \varepsilon$.
>
> Since $f(x_0) = y_0$, we have $|f(x) - f(x_0)| < \varepsilon$ whenever $|x - x_0| < \delta'$.
>
> Hence $f$ is continuous at $x_0$.
>
> **Step 6: Differentiability of $f$ and the derivative formula.**
>
> We need to show:
>
> $$
> \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = -\frac{F_x(x_0, y_0)}{F_y(x_0, y_0)}.
> $$
>
> Since $F(x_0 + h, f(x_0 + h)) = 0$ and $F(x_0, f(x_0)) = 0$:
>
> $$
> 0 = F(x_0 + h, f(x_0 + h)) - F(x_0, f(x_0)).
> $$
>
> Apply the [[Mean Value Theorem]]. Write:
>
> $$
> \begin{aligned}
> 0 &= F(x_0 + h, f(x_0 + h)) - F(x_0, f(x_0 + h)) + F(x_0, f(x_0 + h)) - F(x_0, f(x_0)) \\
> &= F_x(x_0 + \alpha h, f(x_0 + h)) \cdot h + F_y(x_0, f(x_0) + \beta(f(x_0 + h) - f(x_0))) \cdot (f(x_0 + h) - f(x_0))
> \end{aligned}
> $$
>
> for some $\alpha, \beta \in [0, 1]$.
>
> Rearranging:
>
> $$
> \frac{f(x_0 + h) - f(x_0)}{h} = -\frac{F_x(x_0 + \alpha h, f(x_0 + h))}{F_y(x_0, f(x_0) + \beta(f(x_0 + h) - f(x_0)))}.
> $$
>
> As $h \to 0$:
> - $x_0 + \alpha h \to x_0$ (since $\alpha \in [0, 1]$)
> - $f(x_0 + h) \to f(x_0) = y_0$ (by continuity of $f$, proved in Step 5)
> - $f(x_0) + \beta(f(x_0 + h) - f(x_0)) \to y_0$ (since $\beta \in [0, 1]$ and $f(x_0 + h) \to y_0$)
>
> By continuity of $F_x$ and $F_y$:
>
> $$
> \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = -\frac{F_x(x_0, y_0)}{F_y(x_0, y_0)}.
> $$
>
> Hence $f$ is differentiable at $x_0$ with $f'(x_0) = -\dfrac{F_x(x_0, y_0)}{F_y(x_0, y_0)}$.
>
> The same argument at any point $(x, f(x))$ in the domain gives:
>
> $$
> f'(x) = -\frac{F_x(x, f(x))}{F_y(x, f(x))}.
> $$

^pf-12-1

*Uses:* [[§29 The Mean Value Theorem#^cor-29-7|451 §29.7]], [[Continuous Partials Imply Differentiability|§6.2]], [[Intermediate Value Theorem|451 §18.3]], [[§29 The Mean Value Theorem#^prop-29-8|451 §29.8]], [[Mean Value Theorem|451 §29.3]]

![[m452-12-3.svg]]
*Steps 1–4 of the proof in one picture. In the box around $(x_0, y_0)$ we have $F_y > a/2$, so $F$ increases along every vertical segment. Continuity of $F$ keeps the top edge positive (red) and the bottom edge negative (green) over the narrower strip $|x - x_0| \leq \delta$ (shaded). On each vertical segment in the strip, $F$ therefore crosses $0$ exactly once: the IVT gives a crossing and monotonicity rules out a second. That crossing is $f(x)$ (red dot), and together the crossings trace the graph $y = f(x)$ (blue).*

## Geometric Interpretation

> [!remark] Remark: Why $F_y \neq 0$?
> The condition $F_y(x_0, y_0) \neq 0$ means the level curve $F(x, y) = 0$ is not vertical at $(x_0, y_0)$.
>
> If $F_y = 0$ but $F_x \neq 0$, the curve is vertical, and we should solve for $x$ as a function of $y$ instead.
>
> If both $F_x = F_y = 0$, the point $(x_0, y_0)$ is a **singular point** of the curve, where the implicit function theorem does not apply.

^rem-12-1

![[m452-12-2.svg]]
*The Implicit Function Theorem on a contour map of the paraboloid $F = x^2/4 + y^2$ (dashed: neighboring levels; solid: the contour $F = c$). Zooming in at a generic point (green), the arc passes the vertical line test: locally $y = f(x)$, possible because $F_y \neq 0$ there. Zooming in at the rightmost point (red), the tangent is vertical ($F_y = 2y = 0$): the arc fails the vertical line test, and no $y = f(x)$ exists — but $F_x \neq 0$, the arc passes the* horizontal *line test, and $x = g(y)$ works. A regular contour is always locally a graph; the gradient tells you over which axis.*

> [!remark] Remark: The Derivative Formula
> The formula $f'(x) = -\dfrac{F_x}{F_y}$ can be derived heuristically by implicit differentiation:
>
> Starting from $F(x, f(x)) = 0$, differentiate both sides with respect to $x$ (by the [[Multivariable Chain Rule|chain rule]]):
>
> $$
> F_x(x, f(x)) \cdot 1 + F_y(x, f(x)) \cdot f'(x) = 0.
> $$
>
> Solving for $f'(x)$:
>
> $$
> f'(x) = -\frac{F_x(x, f(x))}{F_y(x, f(x))}.
> $$
>
> The Implicit Function Theorem justifies this formal computation by proving $f$ exists and is differentiable.

^rem-12-2

> [!example] Example §12.1: Circle
> Let $F(x, y) = x^2 + y^2 - 1$. Then $F_x = 2x$ and $F_y = 2y$.
>
> At $(x_0, y_0) = (0, 1)$: $F(0, 1) = 0$, $F_y(0, 1) = 2 \neq 0$.
>
> By the [[Implicit Function Theorem|Implicit Function Theorem]], near $(0, 1)$ we can solve for $y = f(x)$, and:
>
> $$
> f'(x) = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y}.
> $$
>
> Indeed, $f(x) = \sqrt{1 - x^2}$ near $(0, 1)$, and $f'(x) = \dfrac{-x}{\sqrt{1 - x^2}} = -\dfrac{x}{f(x)}$. $\checkmark$

^ex-12-1

> [!example] Example §12.2: Where IFT Fails
> Consider $F(x, y) = x^2 + y^2 - 1$ at the point $(1, 0)$.
>
> Here $F_y(1, 0) = 0$, so the [[Implicit Function Theorem|Implicit Function Theorem]] does not apply.
>
> Indeed, near $(1, 0)$, the circle is vertical — we cannot express $y$ as a single-valued function of $x$.
>
> However, $F_x(1, 0) = 2 \neq 0$, so we can solve for $x$ as a function of $y$ near this point.

^ex-12-2

## Summary of the Proof Structure

| **Step** | **Goal** | **Key Tool** |
|:---:|---|---|
| 1 | Set up neighborhood where $F_y > 0$ | Continuity of $F_y$ |
| 2 | Sign conditions: $F > 0$ on top, $F < 0$ on bottom | Continuity of $F$ |
| 3 | Existence of $f(x)$ | [[Intermediate Value Theorem]] |
| 4 | Uniqueness of $f(x)$ | Strict monotonicity ($F_y > 0$) |
| 5 | Continuity of $f$ | $\varepsilon$-$\delta$ using monotonicity |
| 6 | Differentiability of $f$ | [[Mean Value Theorem\|MVT]] + continuity of $F_x, F_y$ |

## Implicit Function Theorem: Multivariable Case

The Implicit Function Theorem generalizes to functions of more variables.

> [!theorem] Theorem §12.2: Implicit Function Theorem — General Case
> Let $F(x_1, x_2, \ldots, x_n, y)$ satisfy:
> - (i) $F(x_1^{(0)}, x_2^{(0)}, \ldots, x_n^{(0)}, y^{(0)}) = 0$
> - (ii) $F_y(x_1^{(0)}, x_2^{(0)}, \ldots, x_n^{(0)}, y^{(0)}) \neq 0$
> - (iii) All partial derivatives $F_{x_1}, \ldots, F_{x_n}, F_y$ are continuous in a neighborhood of $(x^{(0)}, y^{(0)})$
>
> Then there exists a function $y = Y(x_1, \ldots, x_n)$ defined in a neighborhood of $(x_1^{(0)}, \ldots, x_n^{(0)})$ such that:
> - (a) $F(x_1, \ldots, x_n, Y(x_1, \ldots, x_n)) = 0$
> - (b) $Y$ is continuously differentiable with
>
> $$
> \frac{\partial Y}{\partial x_i} = -\frac{F_{x_i}(x, Y(x))}{F_y(x, Y(x))}
> $$

^thm-12-2

> [!remark] Remark
> The proof follows the same structure as the [[Implicit Function Theorem|two-variable case]]. The condition $F_y \neq 0$ ensures we can solve for $y$ in terms of the other variables.

^rem-12-3

> [!remark]- Connections
> - Systems of equations: solving several equations for several unknowns needs a nonzero Jacobian determinant instead of $F_y \neq 0$ — see the [[Inverse Function Theorem (several variables)|Inverse Function Theorem]] (§13.2) and the two-constraint Lagrange derivation in [[§14 Optimization and Lagrange Multipliers|§14]]; the linear-algebra fact behind it is [[Invertible ⟺ nonzero determinant|LADR 9.50]].
> - The version for k equations in n + k unknowns, with an invertible k × k block of partials in place of $F_y \neq 0$, is [[§4 The Regular Value Theorem#^thm-4-1|591 Thm. §4.1]], and this theorem is its case k = 1, [[§4 The Regular Value Theorem#^cor-4-2|591 Cor. §4.2]].
