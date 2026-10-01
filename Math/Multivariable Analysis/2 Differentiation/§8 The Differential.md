---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 8
tags: [multivariable-analysis, math452]
---
← [[§7 Directional Derivatives]] · ↑ [[· 2 Differentiation]] · [[§9 Taylor's Theorem for Multivariable Functions]] →

## What is the Differential?

The notation $df = f'(x) \, dx$ is familiar from single-variable calculus, but what does it actually **mean**? The professor emphasizes: **the derivative $f'(x)$ is defined before the differential**.

> [!remark] Remark: Single Variable: The Differential as a Function
> For $f: \mathbb{R} \to \mathbb{R}$, we first define the [[§28 Basic Properties of the Derivative#^def-28-1|derivative]]:
>
> $$
> f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}.
> $$
>
> Then we **define** the differential $df$ as a function of **two variables** $(x, h)$:
>
> $$
> df\big|_{(x, h)} = f'(x) \cdot h.
> $$
>
> What about $dx$? Consider the identity function $r(x) = x$. Its differential is:
>
> $$
> dr\big|_{(x, h)} = r'(x) \cdot h = 1 \cdot h = h.
> $$
>
> So $dx = h$, and we can write $df = f'(x) \cdot dx$.
>
> **Key insight:** The differential $df$ is a **linear function in the increment $h$**, not just a symbol.

^rem-8-1

![[m452-8-1.svg]]
*The differential is a rise along the tangent line, not along the graph. For the increment $h = dx$, the value $df = f'(x)\,h$ (red) is how much the tangent line climbs, while $f(x+h) - f(x)$ (brace) is how much $f$ itself climbs. The gap between the two (dotted) is the error of the linear approximation; it shrinks faster than $h$, which is exactly what makes $df$ the best linear approximation to the change in $f$ (in two variables: the [[§8 The Differential#^rem-8-2|connection to differentiability]] below).*

> [!definition] Definition §8.1: Differential in Multivariable Calculus
> For $f : \mathbb{R}^2 \to \mathbb{R}$, the **differential** $df$ is a function of **four variables** $(x, y, h, k)$:
>
> $$
> df\big|_{(x, y, h, k)} = f_x(x, y) \cdot h + f_y(x, y) \cdot k.
> $$
>
> Since $dx = h$ and $dy = k$ (by the same reasoning as above), we write:
>
> $$
> df = f_x \, dx + f_y \, dy.
> $$

^def-8-1

> [!remark]- Connections
> - For fixed $(x, y)$, $df$ is a [[§12 Duality#^ladr-3-108|linear functional]] on $\mathbb{R}^2$ — the total derivative [[§6 Differentiability#^def-6-2|Def. §6.2]].
> - Reappears as a 1-form: [[§22 The Algebra of Differential Forms#^prop-22-6|Gradient = Differential = 1-Form]].

> [!remark] Remark: Connection to Differentiability
> The differential $df$ is precisely the **linear map** $L(h, k) = f_x \cdot h + f_y \cdot k$ from our [[§6 Differentiability#^def-6-1|definition of differentiability]]!
>
> Differentiability says:
>
> $$
> f(x_0 + h, y_0 + k) - f(x_0, y_0) = df\big|_{(x_0, y_0, h, k)} + o(\rho).
> $$
>
> So the differential $df$ is the “best linear approximation” to the change in $f$ (see [[§6 Differentiability#^def-6-2|the total derivative]]; [[§3 Continuity and Limits of Functions#^def-3-3|little-o notation]]).

^rem-8-2

> [!remark] Note: Looking Ahead
> The symbols $dx$ and $dy$ are defined here as “the increment $h$ and $k$.” In Part III ([[§21 Introduction to Differential Forms|§21]]–[[§22 The Algebra of Differential Forms|§22]]), we will see that $dx$ and $dy$ are more precisely *[[§21 Introduction to Differential Forms#^def-21-1|1-forms]]*: machines that eat a tangent vector and extract its components. The differential $df = f_x\,dx + f_y\,dy$ is then a 1-form that eats a tangent vector $\mathbf{v}$ and outputs the directional derivative $\nabla f \cdot \mathbf{v}$ ([[§7 Directional Derivatives#^rem-7-2|§7]]). The two viewpoints — “best linear approximation” and “1-form” — are the same object ([[§22 The Algebra of Differential Forms#^prop-22-6|Prop. §22.6]]).

^rem-8-3

## Higher Differentials

> [!definition] Definition §8.2: Second Differential
> The **second differential** is $d^2f = d(df)$. To compute it, we apply $d$ to $df = f_x \cdot h + f_y \cdot k$, treating $h$ and $k$ as constants:
>
> $$
> d^2f = d(f_x \cdot h + f_y \cdot k) = d(f_x) \cdot h + d(f_y) \cdot k.
> $$
>
> Compute each piece:
>
> $$
> \begin{aligned}
> d(f_x) &= (f_x)_x \cdot h + (f_x)_y \cdot k = f_{xx} \cdot h + f_{xy} \cdot k, \\
> d(f_y) &= (f_y)_x \cdot h + (f_y)_y \cdot k = f_{yx} \cdot h + f_{yy} \cdot k.
> \end{aligned}
> $$
>
> Substituting:
>
> $$
> \begin{aligned}
> d^2f &= (f_{xx} h + f_{xy} k) \cdot h + (f_{yx} h + f_{yy} k) \cdot k \\
> &= f_{xx} h^2 + f_{xy} hk + f_{yx} hk + f_{yy} k^2.
> \end{aligned}
> $$
>
> If $f_{xy} = f_{yx}$ (by [[Schwarz–Clairaut Theorem|Schwarz–Clairaut]]), then:
>
> $$
> d^2f = f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2.
> $$

^def-8-2

> [!remark]- Connections
> - Its coefficient matrix is the [[§14 Optimization and Lagrange Multipliers#^def-14-2|Hessian (Def. §14.2)]]; in forms language, [[§22 The Algebra of Differential Forms#^prop-22-7|the second total derivative is the Hessian]].
> - Linear algebra: the [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-18|quadratic form associated with a (symmetric) bilinear form]] (LADR 9.18, 9.20).

> [!remark] Remark: Interpretation of $d^2f$
> The second differential $d^2f$ is a **[[§32 Bilinear Forms and Quadratic Forms#^ladr-9-18|quadratic form]]** in $(h, k)$. It captures the **curvature** or second-order behavior of $f$:
> - It appears in the [[§9 Taylor's Theorem for Multivariable Functions#^ex-9-2|second-order Taylor expansion]] of $f$.
> - It [[Second Derivative Test in Several Variables|determines]] whether a critical point is a local max, local min, or saddle point.

^rem-8-4

> [!definition] Definition §8.3: Higher Differentials
> For well-behaved functions (with continuous higher partials), the $n$-th differential is:
>
> $$
> d^n f = \sum_{i=0}^{n} \binom{n}{i} \frac{\partial^n f}{\partial x^i \, \partial y^{n-i}} h^i k^{n-i}.
> $$
>
> This is a homogeneous polynomial of degree $n$ in $(h, k)$, and it appears in the $n$-th order [[Multivariable Taylor's Theorem|Taylor expansion]].

^def-8-3

> [!remark] Remark: Symbolic Interpretation
> The formula for $d^n f$ can be written symbolically as:
>
> $$
> d^n f = \left( h \frac{\partial}{\partial x} + k \frac{\partial}{\partial y} \right)^n f,
> $$
>
> where we expand the power using the binomial theorem and then apply the resulting differential operators to $f$.

^rem-8-5

## Summary

| **Object** | **Formula** | **Interpretation** |
|---|---|---|
| $df$ | $f_x h + f_y k$ | Linear approximation ([[§6 Differentiability#^def-6-3\|tangent plane]]) |
| $d^2f$ | $f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2$ | Quadratic form (curvature) |
| $d^n f$ | $\displaystyle\sum_{i=0}^{n} \binom{n}{i} \partial_x^i \partial_y^{n-i} f \cdot h^i k^{n-i}$ | $n$-th order Taylor term |

**The differential is not just notation — it is a function (linear map, quadratic form, etc.) that captures how $f$ changes to various orders.**
