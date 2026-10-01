---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 10
tags: [multivariable-analysis, math452]
---
← [[§9 Taylor's Theorem for Multivariable Functions]] · ↑ [[· 2 Differentiation]] · [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence]] →

## Setup

Consider the composition of functions:
- $f(\xi, \eta)$ — a function of two variables
- $\xi = \varphi(x, y)$ and $\eta = \psi(x, y)$ — each depends on $(x, y)$

The composition is $g(x, y) = f(\varphi(x, y), \psi(x, y))$.

![[m452-10-1.svg]]
*The composition near a point: $(\varphi, \psi)$ sends $(x_0, y_0)$ to $(\xi_0, \eta_0) = (\varphi(x_0,y_0), \psi(x_0,y_0))$ and bends the square grid around it into a curved grid; $f$ then sends $(\xi_0,\eta_0)$ to the number $g(x_0,y_0)$. The linear parts (red) follow along: an increment $(h,k)$ is carried by the Jacobian $D(\varphi,\psi)$ to a tangent vector (close to the true image point, gray), which $Df$ turns into a change in value. Composing the two linear maps is the chain rule, $Dg = Df \cdot D(\varphi,\psi)$ ([[§10 Composition of Functions and the Chain Rule#^rem-10-2|matrix form]]).*

**Questions:**
- When is $g$ continuous?
- When is $g$ differentiable?
- What are the partial derivatives of $g$?

Recall the single-variable [[§28 Basic Properties of the Derivative#^thm-28-3|chain rule]]: $(f(g(x)))' = f'(g(x)) \cdot g'(x)$ — “derivative first, then compose.”

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
> **Step 1:** Since $f$ is [[§3 Continuity and Limits of Functions#^def-3-1|continuous]] at $(\varphi(a,b), \psi(a,b))$, there exists $\sigma > 0$ such that
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

*Uses:* [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§2 Open and Closed Sets#^def-2-2|Def. §2.2]]

> [!remark]- Connections
> - The same statement was proved in [[§3 Continuity and Limits of Functions#^thm-3-4|Theorem §3.4]].
> - MATH 451 version: [[§17 Continuous Functions#^thm-17-4|Composition of Continuous Functions (451 §17.4)]]; topological version: [[§9 Continuous Functions#^thm-9-4|Rules for Continuous Functions (590 §9.4)]], with the $\varepsilon$-$\delta$ form from [[§11 Metric Topology#^thm-11-7|590 §11.7]].

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
> - MATH 451 version: [[§28 Basic Properties of the Derivative#^thm-28-3|Chain Rule (451 §28.3)]].
> - Under differentiability hypotheses only: [[§6 Differentiability#^thm-6-9|Theorem §6.9]]; continuous partials give differentiability by [[Continuous Partials Imply Differentiability|Theorem §6.2]].
> - The chain rule is the engine of the [[Implicit Function Theorem|Implicit]] and [[Inverse Function Theorem (several variables)|Inverse Function Theorems]].
> - Used in Relativity: the gradient of a scalar field transforms as a covector under Lorentz transformations — [[§B2.2 Tensors and the Covariance Principle#^thm-b2-2-6|REL Theorem §B2.2.6]].
> - Computational version: [[§94 The Chain Rule#^thm-94-2|Calc Thm. §94.2]] (same case) and [[§94 The Chain Rule#^thm-94-3|Calc Thm. §94.3]] (with worked examples).

> [!remark] Remark: Matrix Form
> In matrix notation, the chain rule becomes:
>
> $$
> \begin{pmatrix} g_x & g_y \end{pmatrix} = \begin{pmatrix} f_\xi & f_\eta \end{pmatrix} \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}.
> $$
>
> That is: $Dg = Df \cdot D(\varphi, \psi)$ — the [[§6 Differentiability#^def-6-2|Jacobians]] multiply!

^rem-10-2

> [!remark]- Connections
> - Linear algebra: the matrix of a composition is the product of the matrices, [[§9 Matrices#^ladr-3-43|LADR 3.43]].
> - Computational version: [[§11 Matrix Operations#^def-11-3|235 Def. §11.3]] (the matrix product is defined so that it represents the composite linear map).

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
> Note the matrix is the **[[§9 Matrices#^ladr-3-54|transpose]]** of the Jacobian $D(\varphi, \psi) = \begin{pmatrix} \varphi_x & \varphi_y \\ \psi_x & \psi_y \end{pmatrix}$. This is because we are relating column vectors of operators.

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

Taking [[§9 Matrices#^ladr-3-55|transposes]]:

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
> - Linear algebra: [[§9 Matrices#^ladr-3-43|Matrix of product of linear maps (LADR 3.43)]].
> - Applied to a map and its inverse, this gives [[§13 The Inverse Function Theorem#^rem-13-6|reciprocal Jacobians]] ([[§13 The Inverse Function Theorem#^def-13-1|Def. §13.1]]).

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
> Similarly (fixing $x = x_0$ and varying $y$) we obtain the formula for $\partial g / \partial y$. Finally, $g$ is differentiable at $(x_0, y_0)$: the hypotheses hold at every point near $(x_0, y_0)$ (since $\varphi, \psi$ are continuous), so both formulas hold near $(x_0, y_0)$, and they express $g_x, g_y$ as sums of products of compositions of continuous functions ([[§3 Continuity and Limits of Functions#^thm-3-1|Theorem §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-2|Theorem §3.2]], [[§10 Composition of Functions and the Chain Rule#^thm-10-1|Theorem §10.1]]). Hence $g_x, g_y$ are continuous near $(x_0, y_0)$, and $g$ is differentiable there by [[§6 Differentiability#^thm-6-2|Theorem §6.2]].

^pf-10-2

*Uses:* [[Mean Value Theorem|451 §29.3]], [[§4 Partial Derivatives#^def-4-1|Def. §4.1]], [[§3 Continuity and Limits of Functions#^def-3-1|Def. §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-1|Thm. §3.1]], [[§3 Continuity and Limits of Functions#^thm-3-2|Thm. §3.2]], [[§10 Composition of Functions and the Chain Rule#^thm-10-1|Thm. §10.1]], [[§6 Differentiability#^thm-6-2|Thm. §6.2]]

> [!remark] Remark: Warning: Differentiability of Composition
> **Question:** If $f$ is differentiable and $\varphi, \psi$ are differentiable, is the composition $g = f \circ (\varphi, \psi)$ necessarily differentiable?
>
> **Answer:** Yes — this is [[§6 Differentiability#^thm-6-9|Theorem §6.9]]. The **continuity of the partial derivatives** assumed in [[Multivariable Chain Rule|the theorem above]] is only a sufficient condition used by its mean-value proof; it is not needed for the conclusion. (Mere existence of the partials, however, is not enough: then $f, \varphi, \psi$ need not be differentiable at all.)

^rem-10-5

> [!remark]- Connections
> - Compare [[§6 Differentiability#^thm-6-9|Theorem §6.9]] (composition of differentiable functions) and the summary [[§6 Differentiability#^rem-6-5|Algebra of Differentiable Functions]].
