---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 10
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §9 Taylor's Theorem for Multivariable Functions]] · ↑ [[Multivariable Analysis — 2 Differentiation]] · [[Multivariable Analysis §11 The Three Differential Operators꞉ Gradient, Curl, Divergence]] →

## Setup

Consider the composition of functions:
- $f(\xi, \eta)$ — a function of two variables
- $\xi = \varphi(x, y)$ and $\eta = \psi(x, y)$ — each depends on $(x, y)$

The composition is $g(x, y) = f(\varphi(x, y), \psi(x, y))$.

![[m452-10-1.svg]]
*The composition: $(\varphi, \psi)$ sends the point $(x, y)$ to $(\xi, \eta)$, and $f$ sends $(\xi, \eta)$ to a number.*

**Questions:**
- When is $g$ continuous?
- When is $g$ differentiable?
- What are the partial derivatives of $g$?

Recall the single-variable [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-3|chain rule]]: $(f(g(x)))' = f'(g(x)) \cdot g'(x)$ — “derivative first, then compose.”

## Continuity of Composition

> [!theorem] Theorem §10.1: Continuity of Composition
> Suppose $\varphi, \psi$ are continuous at $(a, b)$, and $f$ is continuous at $(\varphi(a,b), \psi(a,b))$. Then
>
> $$
> g(x,y) = f(\varphi(x,y), \psi(x,y))
> $$
>
> is continuous at $(a, b)$.

^thm-10-1

> [!proof]+ Proof
> Let $\varepsilon > 0$. We need to find $\delta > 0$ such that $|x - a| < \delta$ and $|y - b| < \delta$ implies $|g(x,y) - g(a,b)| < \varepsilon$.
>
> **Step 1:** Since $f$ is [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|continuous]] at $(\varphi(a,b), \psi(a,b))$, there exists $\sigma > 0$ such that
>
> $$
> |\xi - \varphi(a,b)| < \sigma \text{ and } |\eta - \psi(a,b)| < \sigma \implies |f(\xi, \eta) - f(\varphi(a,b), \psi(a,b))| < \varepsilon.
> $$
>
> **Step 2:** Since $\varphi$ is continuous at $(a,b)$, there exists $\delta_1 > 0$ such that
>
> $$
> |x - a| < \delta_1 \text{ and } |y - b| < \delta_1 \implies |\varphi(x,y) - \varphi(a,b)| < \sigma.
> $$
>
> **Step 3:** Since $\psi$ is continuous at $(a,b)$, there exists $\delta_2 > 0$ such that
>
> $$
> |x - a| < \delta_2 \text{ and } |y - b| < \delta_2 \implies |\psi(x,y) - \psi(a,b)| < \sigma.
> $$
>
> **Conclusion:** Let $\delta = \min\{\delta_1, \delta_2\}$. Then for $|x - a| < \delta$ and $|y - b| < \delta$:
> - $|\varphi(x,y) - \varphi(a,b)| < \sigma$ (by Step 2)
> - $|\psi(x,y) - \psi(a,b)| < \sigma$ (by Step 3)
>
> Hence by Step 1:
>
> $$
> |f(\varphi(x,y), \psi(x,y)) - f(\varphi(a,b), \psi(a,b))| < \varepsilon.
> $$
>
> That is, $|g(x,y) - g(a,b)| < \varepsilon$. So $g$ is continuous at $(a,b)$.

^pf-10-1

*Uses:* [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]]

> [!remark]- Connections
> - The same statement was proved in [[Multivariable Analysis §3 Continuity and Limits of Functions#^thm-3-4|Theorem §3.4]].
> - MATH 451 version: [[Single Variable Analysis §17 Continuous Functions#^thm-17-4|Composition of Continuous Functions (451 §17.4)]]; topological version: [[Topology §9 Continuous Functions#^thm-9-4|Rules for Continuous Functions (590 §9.4)]], with the $\varepsilon$-$\delta$ form from [[Topology §11 Metric Topology#^thm-11-7|590 §11.7]].

> [!remark] Remark
> The proof uses $\sigma$ as an “intermediate variable” connecting $\varepsilon$ (for $f$) to $\delta$ (for $\varphi, \psi$). This is the essence of composing continuous functions.

^rem-10-1

## The Chain Rule

> [!theorem] Theorem §10.2: Multivariable Chain Rule
> Let $g(x,y) = f(\varphi(x,y), \psi(x,y))$. Suppose:
> - $f_\xi, f_\eta$ are continuous in a neighborhood of $(\varphi(x_0, y_0), \psi(x_0, y_0))$
> - $\varphi_x, \varphi_y, \psi_x, \psi_y$ are continuous in a neighborhood of $(x_0, y_0)$
>
> Then $g$ is differentiable at $(x_0, y_0)$ with:
>
> $$
> \begin{aligned}
> \frac{\partial g}{\partial x} &= f_\xi(\varphi, \psi) \cdot \varphi_x(x,y) + f_\eta(\varphi, \psi) \cdot \psi_x(x,y), \\[6pt]
> \frac{\partial g}{\partial y} &= f_\xi(\varphi, \psi) \cdot \varphi_y(x,y) + f_\eta(\varphi, \psi) \cdot \psi_y(x,y).
> \end{aligned}
> $$

^thm-10-2

> [!remark]- Connections
> - MATH 451 version: [[Single Variable Analysis §28 Basic Properties of the Derivative#^thm-28-3|Chain Rule (451 §28.3)]].
> - Under differentiability hypotheses only: [[Multivariable Analysis §6 Differentiability#^thm-6-9|Theorem §6.9]]; continuous partials give differentiability by [[Continuous Partials Imply Differentiability|Theorem §6.2]].
> - The chain rule is the engine of the [[Implicit Function Theorem|Implicit]] and [[Inverse Function Theorem (several variables)|Inverse Function Theorems]].

> [!remark] Remark: Matrix Form
> In matrix notation, the chain rule becomes:
>
> $$
> \begin{pmatrix} g_x & g_y \end{pmatrix} = \begin{pmatrix} f_\xi & f_\eta \end{pmatrix} \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}.
> $$
>
> That is: $Dg = Df \cdot D(\varphi, \psi)$ — the [[Multivariable Analysis §6 Differentiability#^def-6-2|Jacobians]] multiply!

^rem-10-2

> [!remark]- Connections
> - Linear algebra: the matrix of a composition is the product of the matrices, [[Linear Algebra 3C Matrices#^ladr-3-43|LADR 3.43]].

## The Chain Rule in Matrix and Operator Form

The chain rule has an elegant formulation using matrices and differential operators. This perspective is essential for understanding the [[Inverse Function Theorem (several variables)|Inverse Function Theorem]].

### Setup

Consider the composition:

$$
(x, y) \xrightarrow{(\varphi, \psi)} (\xi, \eta) \xrightarrow{f} f(\xi, \eta)
$$

where $\xi = \varphi(x, y)$ and $\eta = \psi(x, y)$.

### The Operator Viewpoint

Think of $\partial_x$ and $\partial_y$ as operators that act on functions. For a function $f(\xi, \eta)$ where $\xi, \eta$ depend on $(x, y)$:

$$
\partial_x f = \frac{\partial f}{\partial \xi} \cdot \frac{\partial \xi}{\partial x} + \frac{\partial f}{\partial \eta} \cdot \frac{\partial \eta}{\partial x} = f_\xi \cdot \xi_x + f_\eta \cdot \eta_x.
$$

This can be written as:

$$
\partial_x = \xi_x \, \partial_\xi + \eta_x \, \partial_\eta.
$$

Similarly:

$$
\partial_y = \xi_y \, \partial_\xi + \eta_y \, \partial_\eta.
$$

### Matrix Form of the Operator Relation

Writing this as a matrix equation:

$$
\begin{pmatrix} \partial_x \\ \partial_y \end{pmatrix} = \begin{pmatrix} \xi_x & \eta_x \\ \xi_y & \eta_y \end{pmatrix} \begin{pmatrix} \partial_\xi \\ \partial_\eta \end{pmatrix}.
$$

With $\xi = \varphi(x,y)$ and $\eta = \psi(x,y)$:

$$
\boxed{\begin{pmatrix} \partial_x \\ \partial_y \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix} \begin{pmatrix} \partial_\xi \\ \partial_\eta \end{pmatrix}}
$$

> [!remark] Remark
> Note the matrix is the **[[Linear Algebra 3C Matrices#^ladr-3-54|transpose]]** of the Jacobian $D(\varphi, \psi) = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}$. This is because we are relating column vectors of operators.

^rem-10-3

### Applying to a Function

For any function $f(\xi, \eta)$, applying both sides to $f$:

$$
\begin{pmatrix} \partial_x f \\ \partial_y f \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix} \begin{pmatrix} \partial_\xi f \\ \partial_\eta f \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix} \begin{pmatrix} f_\xi \\ f_\eta \end{pmatrix}.
$$

Writing out the components:

$$
\begin{aligned}
\partial_x f &= \varphi_x f_\xi + \psi_x f_\eta, \\
\partial_y f &= \varphi_y f_\xi + \psi_y f_\eta.
\end{aligned}
$$

This is exactly the [[Multivariable Chain Rule|chain rule]]!

### For Multiple Output Functions

If we have two functions $f(\xi, \eta)$ and $g(\xi, \eta)$, we can apply the operator to both:

$$
\begin{pmatrix} \partial_x f & \partial_x g \\ \partial_y f & \partial_y g \end{pmatrix} = \begin{pmatrix} \varphi_x & \psi_x \\ \varphi_y & \psi_y \end{pmatrix} \begin{pmatrix} f_\xi & g_\xi \\ f_\eta & g_\eta \end{pmatrix}.
$$

Taking transposes:

$$
\begin{pmatrix} f_x & f_y \\ g_x & g_y \end{pmatrix} = \begin{pmatrix} f_\xi & f_\eta \\ g_\xi & g_\eta \end{pmatrix} \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}.
$$

This gives the **Jacobian multiplication rule**:

$$
\boxed{D(f \circ (\varphi, \psi), \, g \circ (\varphi, \psi)) = D(f, g) \cdot D(\varphi, \psi)}
$$

> [!remark] Remark: Chain Rule for Jacobians
> In compact notation: if $(u, v) = (f, g)(\xi, \eta)$ and $(\xi, \eta) = (\varphi, \psi)(x, y)$, then:
>
> $$
> \frac{\partial(u, v)}{\partial(x, y)} = \frac{\partial(u, v)}{\partial(\xi, \eta)} \cdot \frac{\partial(\xi, \eta)}{\partial(x, y)}.
> $$
>
> Jacobians multiply like matrices under composition.

^rem-10-4

> [!remark]- Connections
> - Linear algebra: [[Linear Algebra 3C Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]].
> - Applied to a map and its inverse, this gives [[Multivariable Analysis §13 The Inverse Function Theorem#^rem-13-6|reciprocal Jacobians]] ([[Multivariable Analysis §13 The Inverse Function Theorem#^def-13-1|Def. §13.1]]).

> [!proof]+ Proof of $\partial g / \partial x$
> Fix $(x_0, y_0)$ and let $y = y_0$. Define:
>
> $$
> \partial_1 = f(\varphi(x_0 + h, y_0), \psi(x_0 + h, y_0)) - f(\varphi(x_0, y_0), \psi(x_0, y_0)).
> $$
>
> Add and subtract $f(\varphi(x_0 + h, y_0), \psi(x_0, y_0))$:
>
> $$
> \begin{aligned}
> \partial_1 &= \underbrace{\bigl[f(\varphi(x_0+h,y_0), \psi(x_0+h,y_0)) - f(\varphi(x_0+h,y_0), \psi(x_0,y_0))\bigr]}_{\text{(I): change in } \eta} \\
> &\quad + \underbrace{\bigl[f(\varphi(x_0+h,y_0), \psi(x_0,y_0)) - f(\varphi(x_0,y_0), \psi(x_0,y_0))\bigr]}_{\text{(II): change in } \xi}.
> \end{aligned}
> $$
>
> **Term (II):** Define $u(\xi) = f(\xi, \psi(x_0, y_0))$. By [[Mean Value Theorem|MVT]], there exists $\alpha(h) \in [0,1]$ such that:
>
> $$
> \begin{aligned}
> \text{(II)} &= u(\varphi(x_0+h, y_0)) - u(\varphi(x_0, y_0)) \\
> &= u'(\varphi(x_0, y_0) + \alpha(h)[\varphi(x_0+h, y_0) - \varphi(x_0, y_0)]) \cdot [\varphi(x_0+h, y_0) - \varphi(x_0, y_0)] \\
> &= f_\xi(\varphi(x_0, y_0) + \alpha(h) \cdot \Delta\varphi, \, \psi(x_0, y_0)) \cdot \Delta\varphi,
> \end{aligned}
> $$
>
> where $\Delta\varphi = \varphi(x_0+h, y_0) - \varphi(x_0, y_0)$.
>
> **Term (I):** Define $v(\eta) = f(\varphi(x_0+h, y_0), \eta)$. By MVT, there exists $\theta(h) \in [0,1]$ such that:
>
> $$
> \begin{aligned}
> \text{(I)} &= f_\eta(\varphi(x_0+h, y_0), \, \psi(x_0, y_0) + \theta(h) \cdot \Delta\psi) \cdot \Delta\psi,
> \end{aligned}
> $$
>
> where $\Delta\psi = \psi(x_0+h, y_0) - \psi(x_0, y_0)$.
>
> **Dividing by $h$:**
>
> $$
> \frac{\partial_1}{h} = f_\eta(\cdots) \cdot \frac{\Delta\psi}{h} + f_\xi(\cdots) \cdot \frac{\Delta\varphi}{h}.
> $$
>
> **Taking $h \to 0$:**
> - $\dfrac{\Delta\varphi}{h} = \dfrac{\varphi(x_0+h, y_0) - \varphi(x_0, y_0)}{h} \to \varphi_x(x_0, y_0)$
> - $\dfrac{\Delta\psi}{h} = \dfrac{\psi(x_0+h, y_0) - \psi(x_0, y_0)}{h} \to \psi_x(x_0, y_0)$
> - The arguments of $f_\xi$ converge to $(\varphi(x_0, y_0), \psi(x_0, y_0))$ since $\alpha(h) \in [0,1]$ and $\Delta\varphi \to 0$
> - The arguments of $f_\eta$ converge similarly
> - By continuity of $f_\xi$ and $f_\eta$, the $f_\xi(\cdots)$ and $f_\eta(\cdots)$ terms converge
>
> Therefore:
>
> $$
> \frac{\partial g}{\partial x}(x_0, y_0) = \lim_{h \to 0} \frac{\partial_1}{h} = f_\xi(\varphi(x_0,y_0), \psi(x_0,y_0)) \cdot \varphi_x(x_0, y_0) + f_\eta(\varphi(x_0,y_0), \psi(x_0,y_0)) \cdot \psi_x(x_0, y_0).
> $$
>
> The proof for $\partial g / \partial y$ is parallel.

^pf-10-2

*Uses:* [[Mean Value Theorem|451 §29.3]], [[Multivariable Analysis §4 Partial Derivatives#^def-4-1|Def. §4.1]]

> [!remark] Remark: Warning: Differentiability of Composition
> **Question:** If $f$ is differentiable and $\varphi, \psi$ are differentiable, is the composition $g = f \circ (\varphi, \psi)$ necessarily differentiable?
>
> **Answer:** Not automatically! [[Multivariable Chain Rule|The theorem]] requires **continuity of the partial derivatives**, not just their existence. Without this, the composition may fail to be differentiable even if all component functions are.

^rem-10-5

> [!remark]- Connections
> - Compare [[Multivariable Analysis §6 Differentiability#^thm-6-9|Theorem §6.9]] (composition of differentiable functions) and the summary [[Multivariable Analysis §6 Differentiability#^rem-6-5|Algebra of Differentiable Functions]].
