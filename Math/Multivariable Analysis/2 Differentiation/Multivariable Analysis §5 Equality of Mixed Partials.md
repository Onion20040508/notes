---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 5
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §4 Partial Derivatives]] · ↑ [[Multivariable Analysis — 2 Differentiation]] · [[Multivariable Analysis §6 Differentiability]] →

> [!theorem] Theorem §5.1: Schwarz–Clairaut
> Let $R$ be an open rectangle. If $f_{xy}$ and $f_{yx}$ exist and are continuous on $R$, then $f_{xy} = f_{yx}$ on $R$.

^thm-5-1

> [!proof]+ Proof
> Let $(x_0, y_0) \in R$. Since $R$ is [[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|open]], there exists $r > 0$ such that $B((x_0, y_0), r) \subseteq R$.
>
> **Motivation for $I(h,k)$:** By [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|definition of partial derivatives]],
>
> $$
> f_{xy}(x_0, y_0) = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)\bigg|_{(x_0,y_0)} = \lim_{h \to 0} \frac{f_y(x_0 + h, y_0) - f_y(x_0, y_0)}{h}.
> $$
>
> Substituting the definition of $f_y$:
>
> $$
> f_{xy}(x_0, y_0) = \lim_{h \to 0} \lim_{k \to 0} \frac{1}{h}\left(\frac{f(x_0+h, y_0+k) - f(x_0+h, y_0)}{k} - \frac{f(x_0, y_0+k) - f(x_0, y_0)}{k}\right).
> $$
>
> Combining the fractions:
>
> $$
> f_{xy}(x_0, y_0) = \lim_{h \to 0} \lim_{k \to 0} \frac{f(x_0+h, y_0+k) - f(x_0+h, y_0) - f(x_0, y_0+k) + f(x_0, y_0)}{hk}.
> $$
>
> Similarly, $f_{yx}(x_0, y_0) = \lim_{k \to 0} \lim_{h \to 0}$ of the same expression. This motivates defining:
>
> $$
> I(h, k) = \frac{f(x_0 + h, y_0 + k) - f(x_0, y_0 + k) - f(x_0 + h, y_0) + f(x_0, y_0)}{hk}
> $$
>
> for $h, k \neq 0$ with $|h|, |k| < r/2$. The key observation is that $I(h,k)$ is symmetric in structure, and we will show it equals both $f_{xy}$ and $f_{yx}$ at nearby points.
>
> **Expressing $I$ via $f_{xy}$:** Define $\varphi(y) = f(x_0 + h, y) - f(x_0, y)$ for $y \in [y_0, y_0 + k]$. Then
>
> $$
> I(h, k) = \frac{\varphi(y_0 + k) - \varphi(y_0)}{hk}.
> $$
>
> Since $f_y$ exists on $R$, the function $\varphi$ is differentiable with $\varphi'(y) = f_y(x_0 + h, y) - f_y(x_0, y)$. By [[Mean Value Theorem|MVT]], there exists $\theta(h, k) \in [0, 1]$ such that
>
> $$
> \varphi(y_0 + k) - \varphi(y_0) = k \cdot \varphi'(y_0 + \theta(h,k) \cdot k) = k \cdot \bigl[f_y(x_0 + h, y_0 + \theta(h,k) \cdot k) - f_y(x_0, y_0 + \theta(h,k) \cdot k)\bigr].
> $$
>
> Thus
>
> $$
> I(h, k) = \frac{f_y(x_0 + h, y_0 + \theta(h,k) \cdot k) - f_y(x_0, y_0 + \theta(h,k) \cdot k)}{h}.
> $$
>
> Now define $g(x) = f_y(x, y_0 + \theta(h,k) \cdot k)$ for $x \in [x_0, x_0 + h]$. Since $f_{xy}$ exists on $R$, the function $g$ is differentiable with $g'(x) = f_{xy}(x, y_0 + \theta(h,k) \cdot k)$. By MVT, there exists $\alpha(h, k) \in [0, 1]$ such that
>
> $$
> g(x_0 + h) - g(x_0) = h \cdot g'(x_0 + \alpha(h,k) \cdot h) = h \cdot f_{xy}(x_0 + \alpha(h,k) \cdot h, y_0 + \theta(h,k) \cdot k).
> $$
>
> Therefore:
>
> $$
> I(h, k) = f_{xy}(x_0 + \alpha(h,k) \cdot h, \, y_0 + \theta(h,k) \cdot k).
> $$
>
> **Expressing $I$ via $f_{yx}$:** Define $\psi(x) = f(x, y_0 + k) - f(x, y_0)$ for $x \in [x_0, x_0 + h]$. Then
>
> $$
> I(h, k) = \frac{\psi(x_0 + h) - \psi(x_0)}{hk}.
> $$
>
> By the same argument (applying MVT twice, first in $x$, then in $y$), there exist $\beta(h, k), \gamma(h, k) \in [0, 1]$ such that
>
> $$
> I(h, k) = f_{yx}(x_0 + \beta(h,k) \cdot h, \, y_0 + \gamma(h,k) \cdot k).
> $$
>
> **Taking the limit:** Since both expressions equal $I(h, k)$:
>
> $$
> f_{xy}(x_0 + \alpha(h,k) \cdot h, y_0 + \theta(h,k) \cdot k) = f_{yx}(x_0 + \beta(h,k) \cdot h, y_0 + \gamma(h,k) \cdot k).
> $$
>
> As $(h, k) \to (0, 0)$:
> - $(x_0 + \alpha(h,k) \cdot h, y_0 + \theta(h,k) \cdot k) \to (x_0, y_0)$ since $\alpha(h,k), \theta(h,k) \in [0, 1]$
> - $(x_0 + \beta(h,k) \cdot h, y_0 + \gamma(h,k) \cdot k) \to (x_0, y_0)$ since $\beta(h,k), \gamma(h,k) \in [0, 1]$
>
> By [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|continuity]] of $f_{xy}$ and $f_{yx}$ at $(x_0, y_0)$:
>
> $$
> \begin{aligned}
> f_{xy}(x_0, y_0) &= \lim_{(h,k) \to (0,0)} f_{xy}(x_0 + \alpha(h,k) \cdot h, y_0 + \theta(h,k) \cdot k) \\
> &= \lim_{(h,k) \to (0,0)} f_{yx}(x_0 + \beta(h,k) \cdot h, y_0 + \gamma(h,k) \cdot k) = f_{yx}(x_0, y_0).
> \end{aligned}
> $$

^pf-5-1

*Uses:* [[Multivariable Analysis §2 Open and Closed Sets#^def-2-4|Def. §2.4]], [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-2|Def. §3.2]], [[Mean Value Theorem|451 §29.3]]

![[m452-5-1.svg]]
*The mixed second difference $\Delta = f(C) - f(B) - f(D) + f(A)$ (signs at the corners) is symmetric in the two directions: differencing first in $x$ then in $y$, or first in $y$ then in $x$, gives the same $\Delta$. Two applications of the [[Mean Value Theorem]] convert the two readings into $f_{xy}$ and $f_{yx}$ at interior points — continuity forces them equal in the limit.*

> [!remark]- Connections
> - Symmetry of mixed partials is what makes the [[Multivariable Analysis §14 Optimization and Lagrange Multipliers#^def-14-2|Hessian matrix]] symmetric, so the [[Real spectral theorem]] (LADR 7.29) applies to it; see also [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-7|The Second Total Derivative Is the Hessian]].
> - In the language of forms, Clairaut becomes [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-9|d² = 0]] ([[Multivariable Analysis §22 The Algebra of Differential Forms#^thm-22-5|§22.5]]).
