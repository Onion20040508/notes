---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: "6a"
tags: [multivariable-analysis, math452]
---
← [[§6 Differentiability]] · ↑ [[· 2 Differentiation]] · [[§7 Directional Derivatives]] →

The rules for partial derivatives and for differentiable functions under sums, differences, products, quotients and composition, building on [[§6 Differentiability|§6]].

## Algebra of Partial Derivatives

> [!theorem] Theorem §6.3: Partial Derivatives of Sum and Difference
> If $f_x, f_y, g_x, g_y$ exist at $(x_0, y_0)$, then $(f \pm g)_x$ and $(f \pm g)_y$ exist at $(x_0, y_0)$ and:
>
> $$
> (f \pm g)_x = f_x \pm g_x, \qquad (f \pm g)_y = f_y \pm g_y.
> $$

^thm-6-3

> [!proof]+ Proof
> By [[§4 Partial Derivatives#^def-4-1|definition]]:
>
> $$
> \begin{aligned}
> (f + g)_x(x_0, y_0) &= \lim_{h \to 0} \frac{(f + g)(x_0 + h, y_0) - (f + g)(x_0, y_0)}{h} \\
> &= \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h} + \lim_{h \to 0} \frac{g(x_0 + h, y_0) - g(x_0, y_0)}{h} \\
> &= f_x(x_0, y_0) + g_x(x_0, y_0).
> \end{aligned}
> $$
>
> The proofs for $(f + g)_y$, $(f - g)_x$, and $(f - g)_y$ are identical.

^pf-6-3

*Uses:* [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§20 Limits of Functions#^rem-20-2|451 §20 (limit laws)]]

> [!theorem] Theorem §6.4: Product Rule for Partial Derivatives
> If $f_x, f_y, g_x, g_y$ exist at $(x_0, y_0)$, then $(fg)_x$ and $(fg)_y$ exist at $(x_0, y_0)$ and:
>
> $$
> (fg)_x = f_x g + f g_x, \qquad (fg)_y = f_y g + f g_y.
> $$

^thm-6-4

> [!proof]+ Proof
> We compute:
>
> $$
> (fg)_x(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) g(x_0 + h, y_0) - f(x_0, y_0) g(x_0, y_0)}{h}.
> $$
>
> Add and subtract $f(x_0 + h, y_0) g(x_0, y_0)$:
>
> $$
> \begin{aligned}
> &= \lim_{h \to 0} \frac{f(x_0 + h, y_0) [g(x_0 + h, y_0) - g(x_0, y_0)] + g(x_0, y_0) [f(x_0 + h, y_0) - f(x_0, y_0)]}{h} \\
> &= \lim_{h \to 0} f(x_0 + h, y_0) \cdot \frac{g(x_0 + h, y_0) - g(x_0, y_0)}{h} + g(x_0, y_0) \cdot \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}.
> \end{aligned}
> $$
>
> Since $f_x$ exists, $f$ is continuous in $x$ at $(x_0, y_0)$ ([[§28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]]), so $\lim_{h \to 0} f(x_0 + h, y_0) = f(x_0, y_0)$. Thus:
>
> $$
> (fg)_x(x_0, y_0) = f(x_0, y_0) \cdot g_x(x_0, y_0) + g(x_0, y_0) \cdot f_x(x_0, y_0).
> $$
>
> The proof for $(fg)_y$ is identical.

^pf-6-4

*Uses:* [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]], [[§20 Limits of Functions#^rem-20-2|451 §20 (limit laws)]]

> [!theorem] Theorem §6.5: Quotient Rule for Partial Derivatives
> If $f_x, f_y, g_x, g_y$ exist at $(x_0, y_0)$ and $g(x_0, y_0) \neq 0$, then $(f/g)_x$ and $(f/g)_y$ exist at $(x_0, y_0)$ and:
>
> $$
> \left(\frac{f}{g}\right)_x = \frac{f_x g - f g_x}{g^2}, \qquad \left(\frac{f}{g}\right)_y = \frac{f_y g - f g_y}{g^2}.
> $$

^thm-6-5

> [!proof]+ Proof
> First, we show $(1/g)_x = -g_x / g^2$. We have:
>
> $$
> \begin{aligned}
> \left(\frac{1}{g}\right)_x(x_0, y_0) &= \lim_{h \to 0} \frac{\frac{1}{g(x_0 + h, y_0)} - \frac{1}{g(x_0, y_0)}}{h} \\
> &= \lim_{h \to 0} \frac{g(x_0, y_0) - g(x_0 + h, y_0)}{h \cdot g(x_0 + h, y_0) \cdot g(x_0, y_0)} \\
> &= \frac{-g_x(x_0, y_0)}{g(x_0, y_0)^2}.
> \end{aligned}
> $$
>
> (We used continuity of $g$ in $x$, which follows from existence of $g_x$ ([[§28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]]).)
>
> Now apply the [[§6 Differentiability#^thm-6-4|product rule]] to $f \cdot (1/g)$:
>
> $$
> \left(\frac{f}{g}\right)_x = f_x \cdot \frac{1}{g} + f \cdot \left(-\frac{g_x}{g^2}\right) = \frac{f_x}{g} - \frac{f g_x}{g^2} = \frac{f_x g - f g_x}{g^2}.
> $$
>
> The proof for $(f/g)_y$ is identical.

^pf-6-5

*Uses:* [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§6 Differentiability#^thm-6-4|§6.4]], [[§28 Basic Properties of the Derivative#^thm-28-1|451 §28.1]], [[§20 Limits of Functions#^rem-20-2|451 §20 (limit laws)]]

> [!remark]- Connections
> - Each partial is a one-variable derivative, so §6.3–§6.5 are the MATH 451 [[§28 Basic Properties of the Derivative#^thm-28-2|Arithmetic of Derivatives]] applied to slices.

## Algebra of Differentiable Functions

> [!theorem] Theorem §6.6: Sum and Difference of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$, then $f + g$ and $f - g$ are differentiable at $(x_0, y_0)$.

^thm-6-6

> [!proof]+ Proof
> Since $f$ is differentiable at $(x_0, y_0)$:
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_x(x_0, y_0) h + f_y(x_0, y_0) k + o(\rho).
> $$
>
> Since $g$ is differentiable at $(x_0, y_0)$:
>
> $$
> g(x_0 + h, y_0 + k) - g(x_0, y_0) = g_x(x_0, y_0) h + g_y(x_0, y_0) k + o(\rho).
> $$
>
> Adding these:
>
> $$
> (f + g)(x_0 + h, y_0 + k) - (f + g)(x_0, y_0) = (f_x + g_x) h + (f_y + g_y) k + o(\rho).
> $$
>
> This is exactly the [[§6 Differentiability#^def-6-1|definition of differentiability]] for $f + g$, with partial derivatives $f_x + g_x$ and $f_y + g_y$.

^pf-6-6

*Uses:* [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]]

> [!theorem] Theorem §6.7: Product of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$, then $fg$ is differentiable at $(x_0, y_0)$.

^thm-6-7

> [!proof]+ Proof
> Let $f_0 = f(x_0, y_0)$, $g_0 = g(x_0, y_0)$, and write:
>
> $$
> \begin{aligned}
> f(x_0 + h, y_0 + k) &= f_0 + f_x h + f_y k + o(\rho) =: f_0 + \Delta f, \\
> g(x_0 + h, y_0 + k) &= g_0 + g_x h + g_y k + o(\rho) =: g_0 + \Delta g.
> \end{aligned}
> $$
>
> where $\Delta f = f_x h + f_y k + o(\rho)$ and $\Delta g = g_x h + g_y k + o(\rho)$.
>
> Then:
>
> $$
> \begin{aligned}
> (fg)(x_0 + h, y_0 + k) - (fg)(x_0, y_0) &= (f_0 + \Delta f)(g_0 + \Delta g) - f_0 g_0 \\
> &= f_0 \Delta g + g_0 \Delta f + \Delta f \cdot \Delta g.
> \end{aligned}
> $$
>
> Now:
>
> $$
> \begin{aligned}
> f_0 \Delta g + g_0 \Delta f &= f_0 (g_x h + g_y k) + g_0 (f_x h + f_y k) + o(\rho) \\
> &= (f_0 g_x + g_0 f_x) h + (f_0 g_y + g_0 f_y) k + o(\rho) \\
> &= (fg)_x h + (fg)_y k + o(\rho).
> \end{aligned}
> $$
>
> For the remaining term, note that $|\Delta f| \leq C\rho$ and $|\Delta g| \leq C\rho$ for some constant $C$ (since linear terms plus $o(\rho)$ are $O(\rho)$). Thus:
>
> $$
> |\Delta f \cdot \Delta g| \leq C^2 \rho^2 = o(\rho).
> $$
>
> Therefore:
>
> $$
> (fg)(x_0 + h, y_0 + k) - (fg)(x_0, y_0) = (fg)_x h + (fg)_y k + o(\rho).
> $$
>
> Hence $fg$ is differentiable at $(x_0, y_0)$.

^pf-6-7

*Uses:* [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]], [[§6 Differentiability#^thm-6-4|§6.4]]

> [!theorem] Theorem §6.8: Quotient of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$ and $g(x_0, y_0) \neq 0$, then $f/g$ is differentiable at $(x_0, y_0)$.

^thm-6-8

> [!proof]+ Proof
> It suffices to show $1/g$ is differentiable (then apply the [[§6 Differentiability#^thm-6-7|product rule]] to $f \cdot (1/g)$).
>
> Let $g_0 = g(x_0, y_0) \neq 0$. Since $g$ is differentiable:
>
> $$
> g(x_0 + h, y_0 + k) = g_0 + g_x h + g_y k + o(\rho) = g_0(1 + \epsilon),
> $$
>
> where $\epsilon = \frac{g_x h + g_y k + o(\rho)}{g_0} = O(\rho)/g_0$.
>
> For small $\rho$, $|\epsilon| < 1$, so we can use $\frac{1}{1 + \epsilon} = 1 - \epsilon + O(\epsilon^2)$:
>
> $$
> \begin{aligned}
> \frac{1}{g(x_0 + h, y_0 + k)} &= \frac{1}{g_0(1 + \epsilon)} = \frac{1}{g_0}(1 - \epsilon + O(\epsilon^2)) \\
> &= \frac{1}{g_0} - \frac{1}{g_0} \cdot \frac{g_x h + g_y k + o(\rho)}{g_0} + O(\rho^2) \\
> &= \frac{1}{g_0} - \frac{g_x}{g_0^2} h - \frac{g_y}{g_0^2} k + o(\rho).
> \end{aligned}
> $$
>
> Thus:
>
> $$
> \frac{1}{g(x_0 + h, y_0 + k)} - \frac{1}{g(x_0, y_0)} = -\frac{g_x}{g^2} h - \frac{g_y}{g^2} k + o(\rho).
> $$
>
> This shows $1/g$ is differentiable with $(1/g)_x = -g_x/g^2$ and $(1/g)_y = -g_y/g^2$.

^pf-6-8

*Uses:* [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]], [[§6 Differentiability#^thm-6-7|§6.7]], [[§14 Series#^ex-14-4|451 Ex. §14.4]]

> [!theorem] Theorem §6.9: Chain Rule: Composition of Differentiable Functions
> Let $g(x,y) = f(\varphi(x,y), \psi(x,y))$. If $\varphi, \psi$ are differentiable at $(x_0, y_0)$ and $f$ is differentiable at $(\varphi(x_0, y_0), \psi(x_0, y_0))$, then $g$ is differentiable at $(x_0, y_0)$ with:
>
> $$
> g_x = f_\xi \varphi_x + f_\eta \psi_x, \qquad g_y = f_\xi \varphi_y + f_\eta \psi_y.
> $$

^thm-6-9

> [!proof]+ Proof
> Let $(\xi_0, \eta_0) = (\varphi(x_0, y_0), \psi(x_0, y_0))$. Since $\varphi, \psi$ are differentiable at $(x_0, y_0)$:
>
> $$
> \begin{aligned}
> \varphi(x_0 + h, y_0 + k) - \varphi(x_0, y_0) &= \varphi_x h + \varphi_y k + o(\rho) =: \Delta\xi, \\
> \psi(x_0 + h, y_0 + k) - \psi(x_0, y_0) &= \psi_x h + \psi_y k + o(\rho) =: \Delta\eta.
> \end{aligned}
> $$
>
> Note that $|\Delta\xi|, |\Delta\eta| = O(\rho)$, so $\sigma := \sqrt{(\Delta\xi)^2 + (\Delta\eta)^2} = O(\rho)$.
>
> Since $f$ is differentiable at $(\xi_0, \eta_0)$:
>
> $$
> f(\xi_0 + \Delta\xi, \eta_0 + \Delta\eta) - f(\xi_0, \eta_0) = f_\xi \Delta\xi + f_\eta \Delta\eta + o(\sigma).
> $$
>
> Since $\sigma = O(\rho)$, we have $o(\sigma) = o(\rho)$. Substituting:
>
> $$
> \begin{aligned}
> g(x_0 + h, y_0 + k) - g(x_0, y_0) &= f_\xi (\varphi_x h + \varphi_y k + o(\rho)) + f_\eta (\psi_x h + \psi_y k + o(\rho)) + o(\rho) \\
> &= (f_\xi \varphi_x + f_\eta \psi_x) h + (f_\xi \varphi_y + f_\eta \psi_y) k + o(\rho).
> \end{aligned}
> $$
>
> Hence $g$ is differentiable with the stated partial derivatives.

^pf-6-9

*Uses:* [[§6 Differentiability#^def-6-1|Def. §6.1]], [[§3 Continuity and Limits of Functions#^def-3-3|Def. §3.3]], [[§3 Continuity and Limits of Functions#^def-3-new1|Def. §3.3]]

> [!remark]- Connections
> - MATH 451 version: [[§28 Basic Properties of the Derivative#^thm-28-3|Chain Rule]]; the continuity analogue is [[§3 Continuity and Limits of Functions#^thm-3-4|§3.4]].
> - General form in §10: [[Multivariable Chain Rule|Multivariable Chain Rule]] and its [[§10 Composition of Functions and the Chain Rule#^rem-10-2|matrix form]] (Jacobians multiply, [[§9 Matrices#^ladr-3-43|LADR 3.43]]).
> - Computational version: [[§94 The Chain Rule#^thm-94-2|Calc Thm. §94.2]] (same two-intermediate-variable case) and [[§94 The Chain Rule#^thm-94-3|Calc Thm. §94.3]] (with worked examples).

> [!remark] Remark: Summary: Algebra of Differentiable Functions
> If $f$ and $g$ are differentiable at $(x_0, y_0)$:
>
> | **Function** | **Differentiable?** | **Partial Derivatives** |
> |:---:|:---:|:---:|
> | $f + g$ | Yes | $(f+g)_x = f_x + g_x$, $(f+g)_y = f_y + g_y$ |
> | $f - g$ | Yes | $(f-g)_x = f_x - g_x$, $(f-g)_y = f_y - g_y$ |
> | $fg$ | Yes | $(fg)_x = f_x g + f g_x$, $(fg)_y = f_y g + f g_y$ |
> | $f/g$ | Yes (if $g \neq 0$) | $(f/g)_x = \dfrac{f_x g - f g_x}{g^2}$, $(f/g)_y = \dfrac{f_y g - f g_y}{g^2}$ |
> | $h(f, g)$ | Yes (if $h$ diff.) | [[§6 Differentiability#^thm-6-9\|Chain rule]] |

^rem-6-5
