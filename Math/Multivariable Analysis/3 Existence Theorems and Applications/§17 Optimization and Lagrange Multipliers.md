---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 3
section: 17
tags: [multivariable-analysis, math452]
---
← [[§16 The Inverse Function Theorem]] · ↑ [[· 3 Existence Theorems and Applications]] · [[§18 Second-Order Sufficient Conditions]] →

## Unconstrained Optimization

> [!definition] Definition §17.1: Local Maximum
> A function $f(x, y)$ has a **local maximum** at $(x_0, y_0)$ if there exists $\delta > 0$ such that $f(x, y) \leq f(x_0, y_0)$ for all $(x, y)$ with $\|(x, y) - (x_0, y_0)\| < \delta$.

^def-17-1

> [!definition] Definition §17.2: Local Minimum
> Similarly for **local minimum** with $f(x, y) \geq f(x_0, y_0)$.

^def-17-2

> [!theorem] Theorem §17.1: Necessary Condition for Extremum — Fermat's Theorem in $\mathbb{R}^n$
> If $f$ has a local max/min at $(x_0, y_0)$ and the partials $f_x, f_y$ exist there (e.g., $f$ is differentiable there), then
>
> $$
> f_x(x_0, y_0) = 0 \quad \text{and} \quad f_y(x_0, y_0) = 0.
> $$
>
> Equivalently, $\nabla f(x_0, y_0) = \mathbf{0}$. The same holds in $\mathbb{R}^n$: if $f$ has a local max/min at $\mathbf{a}$ and all partials $\partial f / \partial x_i(\mathbf{a})$ exist, then $\nabla f(\mathbf{a}) = \mathbf{0}$.

^thm-17-1

> [!proof]+ Proof
> Consider the single-variable function $g(x) = f(x, y_0)$ obtained by fixing $y = y_0$. If $f$ has a local max at $(x_0, y_0)$, then $g$ has a local max at $x_0$.
>
> By Fermat's theorem from single-variable calculus (451; [[§29 The Mean Value Theorem#^thm-29-1|Interior Extremum Theorem]]), $g'(x_0) = 0$.
>
> But $g'(x) = f_x(x, y_0)$ ([[§5 Partial Derivatives#^def-5-1|Def. §5.1]]), so $f_x(x_0, y_0) = 0$.
>
> By the same argument with $h(y) = f(x_0, y)$, we get $f_y(x_0, y_0) = 0$. In $\mathbb{R}^n$, the same argument applied to each $g_i(t) = f(\mathbf{a} + t\mathbf{e}_i)$ gives $\partial f / \partial x_i(\mathbf{a}) = 0$.

^pf-17-1

*Uses:* [[§29 The Mean Value Theorem#^thm-29-1|451 §29.1]], [[§5 Partial Derivatives#^def-5-1|Def. §5.1]]

> [!remark]- Connections
> - The 1D version in MATH 451: [[§29 The Mean Value Theorem#^thm-29-1|Interior Extremum Theorem]] (451 §29.1), applied here along each coordinate slice.
> - On a manifold the critical points of $f : M \to \mathbb{R}$ are the points where $df_p = 0$, [[§34 Submersions#^prop-34-2|591 Prop. §34.2]].
> - Computational version: [[§113 Maximum and Minimum Values#^thm-113-1|Calc Thm. §113.1]] (with worked examples); one-variable case [[§28 Maximum and Minimum Values#^thm-28-2|Calc Thm. §28.2]].

> [!remark] Remark
> A point where $\nabla f = \mathbf{0}$ is called a **critical point** or **stationary point**. Not every critical point is a max or min — it could be a saddle point.

^rem-17-1

## Constrained Optimization: The Setup

Now suppose we want to optimize $f(x, y)$ subject to a constraint $g(x, y) = 0$.

> [!example] Example §17.1
> Maximize $f(x, y) = xy$ subject to $g(x, y) = x^2 + y^2 - 1 = 0$ (on the unit circle).

^ex-17-1

The constraint $g(x, y) = 0$ defines a curve in $\mathbb{R}^2$. We seek points on this curve where $f$ is maximized or minimized.

## Geometric Insight: Tangent and Normal Vectors

Suppose the constraint curve $g(x, y) = 0$ can be parametrized as $(x(t), y(t))$. Along this curve:

$$
g(x(t), y(t)) = 0 \quad \text{for all } t.
$$

Differentiating with respect to $t$ (by the [[Multivariable Chain Rule|chain rule]]):

$$
\frac{d}{dt}[g(x(t), y(t))] = g_x \cdot x'(t) + g_y \cdot y'(t) = \nabla g \cdot (x'(t), y'(t)) = 0.
$$

This shows: $\nabla g \perp (x'(t), y'(t))$, i.e., **$\nabla g$ is perpendicular to the tangent vector of the constraint curve**.

In other words, $\nabla g$ is **normal** (perpendicular) to the level curve $g = 0$ (compare [[§9 Directional Derivatives#^rem-9-3|Gradient and Maximum Rate of Change]]).

## Derivation of the Lagrange Condition

Now consider $F(t) = f(x(t), y(t))$, the value of $f$ along the constraint curve.

If $f$ has a max/min at $t = t_0$ along the curve, then $F'(t_0) = 0$ (by Fermat's theorem, [[§29 The Mean Value Theorem#^thm-29-1|451 §29.1]]).

By the [[Multivariable Chain Rule|chain rule]]:

$$
F'(t_0) = f_x \cdot x'(t_0) + f_y \cdot y'(t_0) = \nabla f \cdot (x'(t_0), y'(t_0)) = 0.
$$

This shows: $\nabla f \perp (x'(t_0), y'(t_0))$, i.e., **$\nabla f$ is also perpendicular to the tangent vector**.

**Key conclusion:** At a constrained extremum, both $\nabla f$ and $\nabla g$ are perpendicular to the same tangent vector.

In $\mathbb{R}^2$, there is essentially only one direction perpendicular to the tangent. Therefore:

$$
\boxed{\nabla f \parallel \nabla g \quad \Longleftrightarrow \quad \nabla f = \lambda \nabla g \text{ for some } \lambda \in \mathbb{R}.}
$$

![[m452-14-2.svg]]
*At a constrained extremum $(x_0, y_0)$ (red), the constraint curve $g = 0$ (green) touches a level curve of $f$ (blue) without crossing it. At a crossing point such as $Q$, $\nabla f$ is not normal to $g = 0$: moving along the constraint changes $f$, so $Q$ cannot be an extremum. Tangency makes the normals $\nabla f$ and $\nabla g$ lie on the same line, which is the Lagrange condition $\nabla f = \lambda \nabla g$.*

> [!theorem] Theorem §17.2: Method of Lagrange Multipliers
> Let $f, g: \mathbb{R}^2 \to \mathbb{R}$ be $C^1$ functions. Suppose $f$ has a local max/min at $(x_0, y_0)$ subject to the constraint $g(x_0, y_0) = 0$.
>
> If $\nabla g(x_0, y_0) \neq \mathbf{0}$ (the **constraint qualification**), then there exists $\lambda \in \mathbb{R}$ such that:
>
> $$
> \nabla f(x_0, y_0) = \lambda \nabla g(x_0, y_0).
> $$
>
> Equivalently:
>
> $$
> f_x = \lambda g_x, \quad f_y = \lambda g_y, \quad g(x, y) = 0.
> $$

^thm-17-2

> [!proof]+ Proof
> We give a proof using the [[Implicit Function Theorem|Implicit Function Theorem]].
>
> Since $\nabla g(x_0, y_0) \neq \mathbf{0}$, at least one of $g_x$ or $g_y$ is nonzero. WLOG, assume $g_y(x_0, y_0) \neq 0$.
>
> By IFT, there exists a $C^1$ function $\alpha(x)$ defined near $x_0$ such that:
>
> $$
> g(x, \alpha(x)) = 0 \quad \text{and} \quad \alpha(x_0) = y_0.
> $$
>
> Moreover, $\alpha'(x) = -\dfrac{g_x}{g_y}$.
>
> Now $f$ restricted to the constraint curve becomes a single-variable function:
>
> $$
> F(x) = f(x, \alpha(x)).
> $$
>
> If $f$ has a max/min at $(x_0, y_0)$ on the constraint, then $F$ has a max/min at $x_0$.
>
> By Fermat's theorem ([[§29 The Mean Value Theorem#^thm-29-1|451 §29.1]]): $F'(x_0) = 0$.
>
> Computing $F'$ by the [[Multivariable Chain Rule|chain rule]]:
>
> $$
> F'(x) = f_x(x, \alpha(x)) + f_y(x, \alpha(x)) \cdot \alpha'(x) = f_x - f_y \cdot \frac{g_x}{g_y}.
> $$
>
> Setting $F'(x_0) = 0$:
>
> $$
> f_x - f_y \cdot \frac{g_x}{g_y} = 0 \quad \Longrightarrow \quad f_x g_y = f_y g_x.
> $$
>
> Set $\lambda = f_y / g_y$ (at $(x_0, y_0)$, where $g_y \neq 0$). Then $f_y = \lambda g_y$, and $f_x g_y = f_y g_x = \lambda g_x g_y$; dividing by $g_y \neq 0$ gives $f_x = \lambda g_x$.
>
> Therefore $f_x = \lambda g_x$ and $f_y = \lambda g_y$, i.e., $\nabla f = \lambda \nabla g$.

^pf-17-2

*Uses:* [[Implicit Function Theorem|§15.1]], [[§29 The Mean Value Theorem#^thm-29-1|451 §29.1]], [[Multivariable Chain Rule|§12.2]]

> [!remark]- Connections
> - Generalized to several constraints in $\mathbb{R}^n$: [[§17 Optimization and Lagrange Multipliers#^thm-17-3|Theorem §17.3]].
> - Without a constraint it reduces to [[§17 Optimization and Lagrange Multipliers#^thm-17-1|Fermat's theorem]] (§17.1); the proof is the 1D [[§29 The Mean Value Theorem#^thm-29-1|Interior Extremum Theorem]] (451 §29.1) along the constraint curve.
> - Computational version: [[§114 Lagrange Multipliers#^thm-114-1|Calc Thm. §114.1]] (with worked examples).

> [!remark] Remark: The Constraint Qualification
> The condition $\nabla g \neq \mathbf{0}$ is essential. If $\nabla g = \mathbf{0}$ at a point on the constraint curve, that point is called a **singular point** of the constraint ([[§15 The Implicit Function Theorem#^rem-15-1|§15, remark on singular points]]). The IFT does not apply there, and the Lagrange multiplier method may fail.
>
> Geometrically, $\nabla g = \mathbf{0}$ means the constraint curve may have a cusp, self-intersection, or isolated point — it's not a smooth curve locally.

^rem-17-2

![[m452-14-4.svg]]
*Why the constraint qualification is needed. Minimize $f(x, y) = x$ on the cusp $g = y^2 - x^3 = 0$ (green). The minimum is at the origin (red), where $\nabla g = (-3x^2, 2y) = \mathbf{0}$. There $\nabla f = (1, 0)$ (blue) is not $\lambda \cdot \mathbf{0}$ for any $\lambda$. The Lagrange system has no solution at all ($\lambda \neq 0$ forces $y = 0$, hence $x = 0$, hence $1 = 0$), so the method misses the true minimum. Nor is the level line $x = 0$ through the minimum tangent to the curve there: both branches leave the cusp along the positive $x$-axis, perpendicular to that level line.*

> [!remark] Remark: What if $f_y = 0$?
> In the proof, we assumed $g_y \neq 0$. What if $g_y \neq 0$ but $f_y = 0$?
>
> From the equation $f_x = \lambda g_x$ and $f_y = \lambda g_y$ with $f_y = 0$ and $g_y \neq 0$, we get $\lambda = 0$.
>
> Then $f_x = 0 \cdot g_x = 0$ as well. So $\nabla f = \mathbf{0}$, which is consistent with $\nabla f = \lambda \nabla g = \mathbf{0}$.
>
> The Lagrange equations still hold, just with $\lambda = 0$. This corresponds to a “free” critical point where the constraint happens to pass through a critical point of $f$.

^rem-17-3

## Higher Dimensions: Multiple Constraints

> [!theorem] Theorem §17.3: Lagrange Multipliers with Multiple Constraints
> To optimize $f(x_1, \ldots, x_n)$ subject to constraints $g_1 = 0, g_2 = 0, \ldots, g_k = 0$ (where $k < n$):
>
> If the gradients $\nabla g_1, \ldots, \nabla g_k$ are [[§4 Span and Linear Independence#^ladr-2-15|linearly independent]] at a constrained extremum, then there exist $\lambda_1, \ldots, \lambda_k \in \mathbb{R}$ such that:
>
> $$
> \nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2 + \cdots + \lambda_k \nabla g_k.
> $$

^thm-17-3

> [!proof]+ Proof
> The proof (carried out below for two constraints in $\mathbb{R}^4$) uses the implicit function theorem for systems of equations — the general form of [[§15 The Implicit Function Theorem#^thm-15-2|Theorem §15.2]] for several equations, which is not proved in these notes.
>
> **General Case: Two Constraints in $\mathbb{R}^4$.**
>
> Consider optimizing $f(x, y, z, t)$ subject to two constraints:
>
> $$
> \phi(x, y, z, t) = 0, \qquad \psi(x, y, z, t) = 0.
> $$
>
> The constraint set is generically a 2-dimensional surface in $\mathbb{R}^4$.
>
> **Constraint qualification:** The gradients $\nabla \phi$ and $\nabla \psi$ are [[§4 Span and Linear Independence#^ladr-2-15|linearly independent]]. Equivalently, the $2 \times 4$ Jacobian matrix has [[§9 Matrices#^ladr-3-58|rank]] 2, meaning some $2 \times 2$ submatrix has nonzero determinant.
>
> Suppose
>
> $$
> \det \begin{pmatrix} \phi_z & \phi_t \\ \psi_z & \psi_t \end{pmatrix} \neq 0.
> $$
>
> By the implicit function theorem for systems (the general form of [[§15 The Implicit Function Theorem#^thm-15-2|§15.2]] for several equations, not proved in these notes; compare the two-step argument of [[Inverse Function Theorem (several variables)|§16.2]]), we can locally solve for $z = g(x, y)$ and $t = h(x, y)$ such that:
>
> $$
> \phi(x, y, g(x,y), h(x,y)) = 0, \qquad \psi(x, y, g(x,y), h(x,y)) = 0.
> $$
>
> With this notation ([[§17 Optimization and Lagrange Multipliers#^rem-17-6|Remark: Notation Convention]], after this proof), the constraint qualification becomes:
>
> $$
> \det \begin{pmatrix} \phi_g & \phi_h \\ \psi_g & \psi_h \end{pmatrix} \neq 0.
> $$
>
> **Reduced problem:** Optimize $F(x, y) = f(x, y, g(x,y), h(x,y))$ (unconstrained in two variables).
>
> At an extremum $(x_0, y_0)$ ([[§17 Optimization and Lagrange Multipliers#^thm-17-1|Theorem §17.1]]):
>
> $$
> \frac{\partial F}{\partial x} = 0, \qquad \frac{\partial F}{\partial y} = 0.
> $$
>
> **Computing the derivatives:** By [[Multivariable Chain Rule|chain rule]],
>
> $$
> \begin{aligned}
> \frac{\partial F}{\partial x} &= f_x + f_g \cdot g_x + f_h \cdot h_x = 0 \\
> \frac{\partial F}{\partial y} &= f_y + f_g \cdot g_y + f_h \cdot h_y = 0
> \end{aligned}
> $$
>
> In matrix form:
>
> $$
> (f_g, f_h) \begin{pmatrix} g_x & g_y \\ h_x & h_y \end{pmatrix} = -(f_x, f_y) \tag{*}
> $$
>
> **Finding $g_x, g_y, h_x, h_y$:** Differentiate the constraints.
>
> From $\phi(x, y, g, h) = 0$:
>
> $$
> \begin{aligned}
> \phi_x + \phi_g \cdot g_x + \phi_h \cdot h_x &= 0 \\
> \phi_y + \phi_g \cdot g_y + \phi_h \cdot h_y &= 0
> \end{aligned}
> $$
>
> From $\psi(x, y, g, h) = 0$:
>
> $$
> \begin{aligned}
> \psi_x + \psi_g \cdot g_x + \psi_h \cdot h_x &= 0 \\
> \psi_y + \psi_g \cdot g_y + \psi_h \cdot h_y &= 0
> \end{aligned}
> $$
>
> In matrix form:
>
> $$
> \begin{pmatrix} \phi_g & \phi_h \\ \psi_g & \psi_h \end{pmatrix} \begin{pmatrix} g_x & g_y \\ h_x & h_y \end{pmatrix} = -\begin{pmatrix} \phi_x & \phi_y \\ \psi_x & \psi_y \end{pmatrix} \tag{**}
> $$
>
> **Combining the equations:** We substitute $(\ast \ast )$ into $(\ast )$. Let $A = \begin{pmatrix} \phi_g & \phi_h \\ \psi_g & \psi_h \end{pmatrix}$, which is invertible by the constraint qualification. From $(\ast \ast )$:
>
> $$
> \begin{pmatrix} g_x & g_y \\ h_x & h_y \end{pmatrix} = -A^{-1} \begin{pmatrix} \phi_x & \phi_y \\ \psi_x & \psi_y \end{pmatrix}
> $$
>
> So $(*)$ becomes:
>
> $$
> -(f_g, f_h) A^{-1} \begin{pmatrix} \phi_x & \phi_y \\ \psi_x & \psi_y \end{pmatrix} = -(f_x, f_y)
> $$
>
> **Define Lagrange multipliers:** Let $(\lambda, \mu) = (f_g, f_h) A^{-1}$, i.e.,
>
> $$
> (f_g, f_h) = (\lambda, \mu) A = (\lambda, \mu) \begin{pmatrix} \phi_g & \phi_h \\ \psi_g & \psi_h \end{pmatrix} = (\lambda \phi_g + \mu \psi_g, \lambda \phi_h + \mu \psi_h)
> $$
>
> This gives:
>
> $$
> f_g = \lambda \phi_g + \mu \psi_g, \qquad f_h = \lambda \phi_h + \mu \psi_h \tag{I}
> $$
>
> Or in terms of the original variables:
>
> $$
> f_z = \lambda \phi_z + \mu \psi_z, \qquad f_t = \lambda \phi_t + \mu \psi_t
> $$
>
> **Verify the equations for $x$ and $y$:** From the manipulation above:
>
> $$
> (\lambda, \mu) \begin{pmatrix} \phi_x & \phi_y \\ \psi_x & \psi_y \end{pmatrix} = (f_x, f_y)
> $$
>
> This gives:
>
> $$
> f_x = \lambda \phi_x + \mu \psi_x, \qquad f_y = \lambda \phi_y + \mu \psi_y \tag{II}
> $$
>
> **Conclusion:** Combining (I) and (II), at a constrained extremum $(x_0, y_0, z_0, t_0)$:
>
> $$
> \boxed{\nabla f = \lambda \nabla \phi + \mu \nabla \psi}
> $$
>
> Together with the constraints $\phi = 0$ and $\psi = 0$, this gives 6 equations in 6 unknowns $(x, y, z, t, \lambda, \mu)$.

^pf-17-3

*Uses:* [[§15 The Implicit Function Theorem#^thm-15-2|§15.2]], [[§17 Optimization and Lagrange Multipliers#^thm-17-1|§17.1]], [[Multivariable Chain Rule|§12.2]], [[§16 The Inverse Function Theorem#^prop-16-1|§16.1]]

> [!remark]- Connections
> - The linear algebra behind it: $\nabla f$ is orthogonal to the tangent space of the constraint set, and that orthogonal complement ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-46|LADR 6.46]]) has dimension $k$ ([[§22 Orthogonal Complements and Minimization Problems#^ladr-6-51|LADR 6.51]]), so it is spanned by the $k$ independent constraint gradients.
> - The case $k = 1$, $n = 2$ is [[Method of Lagrange Multipliers|Theorem §17.2]]; the case $k = 2$, $n = 4$ is derived in the proof above.
> - The implicit function theorem for systems that the proof needs, not proved in 452, is [[§7 The Regular Value Theorem#^thm-7-1|591 Thm. §7.1]]; the tangent space of the constraint set is the kernel of the constraint Jacobian, [[§25 The Geometric Tangent Space#^thm-25-3|591 Thm. §25.3]], and the coordinate-free counterpart of the normal space spanned by the $\nabla g_i$ is the conormal space, [[§35 Regular Submanifolds#^def-35-3|591 Def. §35.3]].
> - Computational version: [[§114 Lagrange Multipliers#^thm-114-2|Calc Thm. §114.2]] (two constraints, with worked examples).
> - A worked special case: [[§60★ Constrained Optimization#^thm-60-1|235 Thm. §60.1]] (the extremes of xᵀAx on the unit sphere are the extreme eigenvalues of A; the Lagrange condition there reads Ax = λx) and, with the two constraints xᵀx = 1, xᵀu₁ = 0, [[§60★ Constrained Optimization#^thm-60-4|235 Thm. §60.4]].
> - Used in Electromagnetism: charges on conductors at fixed total charges minimize the electrostatic energy, and the multiplier of each charge constraint is that conductor's potential (Thomson's theorem) — [[§C4.1 Induced Charge, Screening and Thomson's Theorem#^thm-c4-1-3|EM Theorem §C4.1.3]].
> - The constraint qualification matters in practice: in the honors-thesis proof that stripes are the ground state of quadrupoles on the triangular lattice, $\nabla C$ vanishes at exactly four points of the constraint surface and the minimum lies at three of them, so those points are checked by direct evaluation rather than by the multiplier rule ([[§M5.5 Triangular Lattice꞉ Global Optimality by Tensor–Luttinger–Tisza#^thm-m5-5-3|Thesis Thm. §M5.5.3]]).
> - For $N$ unit spins there are $N$ constraints $|\mathbf S_i|=1$; the Luttinger–Tisza method replaces them by the single constraint $\frac1N\sum_i|\mathbf S_i|^2=1$, whose one multiplier is an eigenvalue, at the price of giving only a lower bound ([[§M3.3 The Luttinger–Tisza Method#^thm-m3-3-2|Thesis Thm. §M3.3.2]]).

> [!remark] Remark: Notation Convention
> Once we substitute $z = g(x,y)$ and $t = h(x,y)$, we write:
> - $\phi_g$ for the partial derivative of $\phi$ with respect to its third argument (the slot filled by $g$), i.e., $\phi_g = \phi_z$ evaluated at $(x, y, g, h)$.
> - $\phi_h$ for the partial derivative of $\phi$ with respect to its fourth argument (the slot filled by $h$), i.e., $\phi_h = \phi_t$ evaluated at $(x, y, g, h)$.
>
> Similarly for $\psi_g, \psi_h$ and $f_g, f_h$. This notation reminds us that these arguments are now functions of $(x, y)$, not independent variables.

^rem-17-6

> [!remark] Remark: Choice of Variables for IFT
> We assumed $\det \begin{pmatrix} \phi_g & \phi_h \\ \psi_g & \psi_h \end{pmatrix} \neq 0$ and solved for $(z, t)$ as functions $g(x,y), h(x,y)$ of the free variables $(x, y)$.
>
> We could equally well have used any other $2 \times 2$ submatrix with nonzero determinant. For instance, if $\det \begin{pmatrix} \phi_y & \phi_h \\ \psi_y & \psi_h \end{pmatrix} \neq 0$, we could solve for $(y, t)$ as functions of $(x, z)$.
>
> The final Lagrange equations $\nabla f = \lambda \nabla \phi + \mu \nabla \psi$ are **independent of this choice**. This is the key insight: the multipliers $\lambda, \mu$ adjust to give the same geometric condition regardless of how we parametrize the constraint surface.

^rem-17-7

> [!remark] Remark: Why Multiple Constraints?
> In $\mathbb{R}^3$, a single constraint $g(x, y, z) = 0$ defines a surface (2D object). To get a curve (1D object), we need two constraints.
>
> Geometrically: $\nabla g_1$ and $\nabla g_2$ are both normal to the constraint curve. The tangent to the curve is perpendicular to both. At a constrained extremum, $\nabla f$ must also be perpendicular to the tangent, so $\nabla f$ lies in the plane spanned by $\nabla g_1$ and $\nabla g_2$.
>
> This is why we need $\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2$ rather than just $\nabla f = \lambda \nabla g$.
>
> In $\mathbb{R}^2$, two vectors perpendicular to the same vector must be parallel. In $\mathbb{R}^3$ and higher, two vectors perpendicular to the same vector need only lie in a plane — they are not necessarily parallel!

^rem-17-4

## Practical Method: Solving Lagrange Equations

To find candidates for constrained extrema of $f$ subject to $g = 0$:

**Step 1:** Write down the system of equations:

$$
\begin{aligned}
f_x &= \lambda g_x \\
f_y &= \lambda g_y \\
g(x, y) &= 0
\end{aligned}
$$

**Step 2:** Solve this system for $x$, $y$, and $\lambda$. (Three equations, three unknowns.)

**Step 3:** Evaluate $f$ at each solution to determine which gives the max/min.

> [!remark] Remark
> The Lagrange conditions are **necessary** but not sufficient. They find all *candidates* for extrema. To determine if a candidate is actually a max, min, or neither, we must either:
> - Compare values of $f$ at all candidates (if the constraint set is compact, EVT guarantees max/min exist; [[Extreme Value Theorem]], in its compact-space form [[Continuous Image of a Compact Space is Compact|590 §18.3]]).
> - Use the bordered Hessian (second-order test for constrained optimization).

^rem-17-5

## Worked Example: $f = xy$ on the Unit Circle

> [!example] Example §17.2
> Maximize and minimize $f(x, y) = xy$ subject to $\phi(x, y) = x^2 + y^2 - 1 = 0$.

^ex-17-2

**Step 1: Set up the Lagrange equations.**

The key condition is $\nabla f \parallel \nabla \phi$, i.e., $\nabla f = \lambda \nabla \phi$ ([[Method of Lagrange Multipliers|Theorem §17.2]]).

$$
\begin{aligned}
f_x &= \lambda \phi_x \quad \Rightarrow \quad y = \lambda \cdot 2x = 2\lambda x \qquad (1) \\
f_y &= \lambda \phi_y \quad \Rightarrow \quad x = \lambda \cdot 2y = 2\lambda y \qquad (2) \\
\phi(x,y) &= 0 \quad \Rightarrow \quad x^2 + y^2 = 1 \qquad (3)
\end{aligned}
$$

**Step 2: Solve the system.**

From (1): $y = 2\lambda x$. Substitute into (2):

$$
x = 2\lambda y = 2\lambda(2\lambda x) = 4\lambda^2 x
$$

So $x(1 - 4\lambda^2) = 0$. Either $x = 0$ or $\lambda^2 = \frac{1}{4}$, i.e., $\lambda = \pm\frac{1}{2}$.

**Case 1:** $x = 0$. From (3): $y^2 = 1$, so $y = \pm 1$. From (1): $y = 2\lambda \cdot 0 = 0$, contradiction. So $x = 0$ gives no solutions.

**Case 2:** $\lambda = \frac{1}{2}$. From (1): $y = 2 \cdot \frac{1}{2} \cdot x = x$. From (3): $x^2 + x^2 = 1$, so $x = \pm\frac{1}{\sqrt{2}}$, $y = \pm\frac{1}{\sqrt{2}}$ (same sign).

Solutions: $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ and $\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

**Case 3:** $\lambda = -\frac{1}{2}$. From (1): $y = -x$. From (3): $x^2 + x^2 = 1$, so $x = \pm\frac{1}{\sqrt{2}}$, $y = \mp\frac{1}{\sqrt{2}}$ (opposite signs).

Solutions: $\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ and $\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$.

**Step 3: Evaluate $f$ at each candidate.**

$$
\begin{aligned}
f\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) &= \frac{1}{2} \quad \text{(maximum)} \\
f\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right) &= \frac{1}{2} \quad \text{(maximum)} \\
f\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right) &= -\frac{1}{2} \quad \text{(minimum)} \\
f\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) &= -\frac{1}{2} \quad \text{(minimum)}
\end{aligned}
$$

![[m452-14-3.svg]]
*Example §14.2 in the plane. The level curves $xy = c$ of $f$ are hyperbolas (blue; dashed for $c < 0$). The constraint $\phi = 0$ is the unit circle (green). The circle meets the hyperbolas $xy = \pm\tfrac14$ transversally, misses $xy = \pm 1$, and is tangent to exactly $xy = \tfrac12$ (at the two maxima, red) and $xy = -\tfrac12$ (at the two minima, orange). At a maximum, $\nabla f = (y, x)$ and $\nabla \phi = (2x, 2y)$ point the same way ($\lambda = \tfrac12$). At a minimum they point in opposite directions ($\lambda = -\tfrac12$).*

*Continued in [[§18 Second-Order Sufficient Conditions]]: the Hessian test for critical points.*
