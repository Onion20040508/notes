---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 5
section: 16
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §15 Multivariable Integration]] · ↑ [[Multivariable Analysis — 5 Line Integrals and the Divergence Theorem]] · [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities]] →

## Line Integrals: Two Types

![[m452-16-1.svg]]
*The line integral is computed through its parametrization: partition time $[a,b]$ into equal steps $\Delta t$; the map $\mathbf{r}$ pushes the ticks forward to points $\mathbf{r}(t_j)$ on the curve, spaced unevenly — wide where the speed $|\mathbf{r}'|$ is large, tight where it is small. Each time step contributes the displacement $\Delta\mathbf{r} \approx \mathbf{r}'(t_j)\Delta t$ and the work term $\mathbf{F}\cdot\Delta\mathbf{r}$. Summing and refining: $\int_{\boldsymbol{\gamma}}\mathbf{F}\cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)\,dt$ — an ordinary one-variable [[Single Variable Analysis §32 The Definition of the Riemann Integral#^def-32-3|integral]]. The speed factor is automatic: $d\mathbf{r} = \mathbf{r}'(t)\,dt$ is the 1D case of the Jacobian story ([[Multivariable Analysis §15 Multivariable Integration|§15]]).*

Let $\gamma$ be a smooth curve in $\mathbb{R}^2$ parametrized by $x = x(t)$, $y = y(t)$ for $t \in [a, b]$.

## The Scalar Line Integral (Type I)

> [!definition] Definition §16.1: Scalar Line Integral
> Let $f: \mathbb{R}^2 \to \mathbb{R}$ be continuous and let $\gamma$ be a piecewise smooth curve. The **scalar line integral** of $f$ along $\gamma$ is:
>
> $$
> \int_\gamma f \, ds = \int_a^b f(x(t), y(t)) \sqrt{x'(t)^2 + y'(t)^2} \, dt.
> $$

^def-16-1

> [!remark]- Connections
> - The 2D analog, weighting by the area element: [[Multivariable Analysis §18 Surface Integrals#^def-18-5|Scalar Surface Integral (Def. §18.5)]].
> - Unlike the work integral, this is not the integral of a differential form: [[Multivariable Analysis §22 The Algebra of Differential Forms#^rem-22-8|Scalar Integrals Are Not Form Integrals]].

**Derivation.** Partition $[a, b]$ into $a = t_0 < t_1 < \cdots < t_N = b$. The $i$-th piece of $\gamma$ has arc length approximately:

$$
\sqrt{(x(t_i) - x(t_{i-1}))^2 + (y(t_i) - y(t_{i-1}))^2}.
$$

By the [[Mean Value Theorem]], $x(t_i) - x(t_{i-1}) = x'(\xi_i)(t_i - t_{i-1})$ and $y(t_i) - y(t_{i-1}) = y'(\eta_i)(t_i - t_{i-1})$ for some intermediate points. Therefore the arc length of the $i$-th piece is:

$$
\sqrt{x'(\xi_i)^2 + y'(\eta_i)^2} \, (t_i - t_{i-1}).
$$

Weighting each piece by $f(x(t_i), y(t_i))$ and summing:

$$
\sum_{i=1}^N f(x(t_i), y(t_i)) \sqrt{x'(\xi_i)^2 + y'(\eta_i)^2} \, (t_i - t_{i-1}).
$$

Taking $N \to \infty$:

$$
\int_\gamma f \, ds = \int_a^b f(x(t), y(t)) \underbrace{\sqrt{x'(t)^2 + y'(t)^2}}_{ds/dt} \, dt.
$$

**Physical interpretation:** If $f$ represents a density (mass per unit length), then $\int_\gamma f \, ds$ gives the total mass of a wire shaped like $\gamma$.

## The Work Line Integral (Type II)

> [!definition] Definition §16.2: Work Line Integral
> Let $\mathbf{F} = (f(x,y), g(x,y))$ be a continuous vector field. The **work done by $\mathbf{F}$** along $\gamma$ is:
>
> $$
> \int_\gamma f \, dx + g \, dy = \int_a^b \big[ f(x(t), y(t)) \, x'(t) + g(x(t), y(t)) \, y'(t) \big] \, dt.
> $$

^def-16-2

> [!remark]- Connections
> - In forms language this is the integral of the 1-form $f\,dx + g\,dy$, computed by pullback: [[Multivariable Analysis §22 The Algebra of Differential Forms#^ex-22-2|Pullback Along a Curve (Ex. §22.2)]], [[Multivariable Analysis §22 The Algebra of Differential Forms#^rem-22-6|1-Form Integration Recovers the Line Integral]].

**Derivation.** Along the $i$-th piece, the displacement vector is approximately:

$$
\big( x(t_i) - x(t_{i-1}), \; y(t_i) - y(t_{i-1}) \big).
$$

The force at $(x(t_i), y(t_i))$ is $(f(x(t_i), y(t_i)), \, g(x(t_i), y(t_i)))$. The work done is the [[Linear Algebra 6A Inner Products and Norms#^ladr-6-1|inner product]] of force and displacement:

$$
\begin{aligned}
W_i &= f(x(t_i), y(t_i)) \cdot (x(t_i) - x(t_{i-1})) + g(x(t_i), y(t_i)) \cdot (y(t_i) - y(t_{i-1})) \\
&\approx f(x(t_i), y(t_i)) \, x'(t_i)(t_i - t_{i-1}) + g(x(t_i), y(t_i)) \, y'(t_i)(t_i - t_{i-1}).
\end{aligned}
$$

Summing and taking the limit:

$$
\sum_{i=1}^N W_i \;\longrightarrow\; \int_a^b \big[ f(x(t), y(t)) \, x'(t) + g(x(t), y(t)) \, y'(t) \big] \, dt.
$$

In differential notation, writing $dx = x'(t) \, dt$ and $dy = y'(t) \, dt$:

$$
\int_\gamma f \, dx + g \, dy = \int_a^b f \, dx(t) + g \, dy(t).
$$

> [!remark] Remark: Parametrization Independence
> The Type I integral $\int_\gamma f \, ds$ is *independent of orientation*: reversing the direction of traversal does not change the value (since $ds > 0$ always).
>
> The Type II integral $\int_\gamma f \, dx + g \, dy$ *depends on orientation*: reversing the direction of traversal changes the sign (since $dx$ and $dy$ change sign).

^rem-16-1

## Green's Theorem

For this and the [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities|next section]], we study the relationship between line integrals and double integrals.

## Setup and Orientation Convention

Let $\gamma$ be a closed curve in $\mathbb{R}^2$ enclosing a bounded domain $D$. The **positive orientation** of $\gamma$ is defined so that $D$ lies on the left side of $\gamma$ as you traverse it. Equivalently, $\gamma$ is traversed **counterclockwise**.

![[m452-16-2.svg]]
*The positive orientation of $\partial D$: traverse counterclockwise, so the region lies on your left. This convention is what makes the signs in Green's theorem come out correctly — and in [[Multivariable Analysis §23 The Generalized Stokes' Theorem|§23]] it will reappear as the induced orientation of a boundary.*

Suppose $(f(x,y), g(x,y))$ is a vector field (force field) in the plane. We want to relate $\oint_\gamma f \, dx + g \, dy$ to a double integral over $D$.

## Assumption on the Domain

For convenience, assume $D$ can be represented simultaneously as:
- **[[Multivariable Analysis §15 Multivariable Integration#^def-15-12|Type I]]** (upper and lower graphs in $x$): $D = \{(x,y) : a \leq x \leq b, \; \phi(x) \leq y \leq \psi(x)\}$
- **[[Multivariable Analysis §15 Multivariable Integration#^def-15-12|Type II]]** (left and right graphs in $y$): $D = \{(x,y) : c \leq y \leq d, \; \alpha(y) \leq x \leq \beta(y)\}$

If $D$ cannot be represented this way (e.g., if $D$ is not convex), we subdivide $D$ into pieces that can, and sum the results. The boundary contributions from internal cuts cancel.

![[m452-16-3.svg]]
*Why the integral theorems glue: apply the theorem to each cell with its own counterclockwise boundary. The shared internal edge is traversed in opposite directions by the two cells, so its two line-integral contributions cancel exactly, leaving only the outer boundary. This is how the proof extends from rectangles to arbitrary decomposable regions — and, in [[Multivariable Analysis §23 The Generalized Stokes' Theorem|§23]], how Stokes' theorem passes from one parameter patch to a whole manifold.*

## Derivation: The $\oint f \, dx$ Term

Consider $\oint_\gamma f \, dx$ using the Type I representation. The boundary $\gamma$ consists of two pieces:
- $\gamma_1$: the lower curve $y = \phi(x)$, traversed from $x = a$ to $x = b$ (left to right).
- $\gamma_2$: the upper curve $y = \psi(x)$, traversed from $x = b$ to $x = a$ (right to left).

(The vertical segments at $x = a$ and $x = b$, if present, contribute zero to $\oint f \, dx$ since $dx = 0$ on them.)

Computing each piece:

$$
\int_{\gamma_1} f \, dx = \int_a^b f(x, \phi(x)) \, dx, \qquad \int_{\gamma_2} f \, dx = \int_b^a f(x, \psi(x)) \, dx = -\int_a^b f(x, \psi(x)) \, dx.
$$

Therefore:

$$
\oint_\gamma f \, dx = \int_a^b \big[ f(x, \phi(x)) - f(x, \psi(x)) \big] \, dx.
$$

By the [[Fundamental Theorem of Calculus]] applied to the inner variable $y$:

$$
f(x, \phi(x)) - f(x, \psi(x)) = -\int_{\phi(x)}^{\psi(x)} f_y(x, y) \, dy.
$$

Substituting:

$$
\oint_\gamma f \, dx = -\int_a^b \int_{\phi(x)}^{\psi(x)} f_y(x, y) \, dy \, dx = -\iint_D f_y \, dy \, dx.
$$

## Derivation: The $\oint g \, dy$ Term

Similarly, consider $\oint_\gamma g \, dy$ using the Type II representation. The boundary consists of:
- $\gamma_3$: the left curve $x = \alpha(y)$, traversed from $y = d$ to $y = c$ (top to bottom).
- $\gamma_4$: the right curve $x = \beta(y)$, traversed from $y = c$ to $y = d$ (bottom to top).

Computing:

$$
\int_{\gamma_3} g \, dy = \int_d^c g(\alpha(y), y) \, dy = -\int_c^d g(\alpha(y), y) \, dy, \qquad \int_{\gamma_4} g \, dy = \int_c^d g(\beta(y), y) \, dy.
$$

Therefore:

$$
\oint_\gamma g \, dy = \int_c^d \big[ g(\beta(y), y) - g(\alpha(y), y) \big] \, dy = \int_c^d \int_{\alpha(y)}^{\beta(y)} g_x(x, y) \, dx \, dy = \iint_D g_x \, dx \, dy.
$$

(Iterated = double integral: Fubini, [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]] and [[Multivariable Analysis §15 Multivariable Integration#^thm-15-10|§15.10]].)

## Combining the Two Terms

Adding the results:

> [!theorem] Theorem §16.1: Green's Theorem
> Let $D \subseteq \mathbb{R}^2$ be a bounded domain whose boundary $\gamma = \partial D$ is a piecewise smooth, simple closed curve, oriented counterclockwise. If $f, g$ are $C^1$ on an open set containing $\overline{D}$, then:
>
> $$
> \boxed{\oint_\gamma f \, dx + g \, dy = \iint_D \left( \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y} \right) dx \, dy}
> $$

^thm-16-1

> [!remark]- Connections
> - 1D ancestor: the [[Fundamental Theorem of Calculus]] (boundary of $[a,b]$ is $\{a,b\}$); curved-surface version: [[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1|Stokes' Theorem (§20.1)]]; everything at once: [[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1|Generalized Stokes' Theorem (§23.1)]].
> - Why the region must have no holes for "curl-free ⇒ conservative": [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-11|A Closed Form That Is Not Exact (§22.11)]]; the topological notion is [[Topology §23 The Fundamental Group#^def-23-3|simply connected]] (590 §23.3).

> [!remark] Remark: Why the Signs Work Out
> The sign pattern $g_x - f_y$ is not arbitrary. It comes from:
> - The $\oint f \, dx$ computation gives $-\iint f_y$ (the minus sign comes from the upper curve being traversed right-to-left).
> - The $\oint g \, dy$ computation gives $+\iint g_x$ (the right curve is traversed bottom-to-top, which is the positive direction).

^rem-16-2

> [!remark] Remark: Higher Dimensions
> For the multi-dimensional case, the idea is the same. If a domain in $\mathbb{R}^n$ is bounded by surfaces $x_n = \beta(x_1, \ldots, x_{n-1})$ (upper) and $x_n = \alpha(x_1, \ldots, x_{n-1})$ (lower), we can relate a boundary integral to a volume integral using the [[Fundamental Theorem of Calculus]] in the $x_n$ direction. This leads to the **[[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1|generalized Stokes' theorem]]**.

^rem-16-3

## Normal Vectors and Orientation

Let $\gamma: (x(t), y(t))$, $t \in [a, b]$ be a smooth curve bounding a domain $D$.

> [!definition] Definition §16.3: Tangent and Normal Vectors
> The **tangent vector** to $\gamma$ at parameter $t$ is:
>
> $$
> \mathbf{T}(t) = (x'(t), \, y'(t)).
> $$
>
> To obtain a **normal vector**, we rotate $\mathbf{T}$ by $\pm \frac{\pi}{2}$:
> - **Inner normal** (pointing into $D$): rotate $\mathbf{T}$ by $+\frac{\pi}{2}$ counterclockwise: $\mathbf{n}_{\text{in}} = (-y'(t), \, x'(t))$.
> - **Outer normal** (pointing out of $D$): rotate $\mathbf{T}$ by $-\frac{\pi}{2}$ clockwise: $\mathbf{n}_{\text{out}} = (y'(t), \, -x'(t))$.

^def-16-3

**Convention:** With $\gamma$ oriented counterclockwise (so $D$ is on our left), the outer normal points to the right of the direction of travel.

**Verification:** A circle of radius $r$ parametrized as $(r\cos\theta, r\sin\theta)$ has tangent vector $(-r\sin\theta, r\cos\theta)$. The outer normal is:

$$
\mathbf{n}_{\text{out}} = (r\cos\theta, r\sin\theta) \cdot \frac{1}{r} = (\cos\theta, \sin\theta),
$$

which indeed points radially outward. Equivalently, the rotation $(x, y) \mapsto (y, -x)$ applied to the tangent gives the outer normal.

## The Divergence Theorem (2D)

We now derive the 2D Divergence Theorem by rewriting [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's theorem]] in terms of the outward normal.

## Rewriting the Line Integral as a Flux Integral

Parametrize $\gamma$ with $(x(t), y(t))$. The Type II line integral is:

$$
\oint_\gamma f \, dx + g \, dy = \int_a^b \big[ f \, x' + g \, y' \big] \, dt = \int_a^b (f, g) \cdot (x', y') \, dt.
$$

The **unit outward normal** is $\hat{n} = \dfrac{(y', -x')}{\sqrt{x'^2 + y'^2}}$. A key algebraic observation:

$$
f \, x' + g \, y' = (g, -f) \cdot (y', -x').
$$

(Just expand the right side: $g \, y' + (-f)(-x') = g \, y' + f \, x'$.) Therefore:

$$
\oint_\gamma f \, dx + g \, dy = \int_a^b (g, -f) \cdot (y', -x') \, dt = \int_a^b (g, -f) \cdot \hat{n} \, \sqrt{x'^2 + y'^2} \, dt = \oint_\gamma (g, -f) \cdot \hat{n} \, ds.
$$

This rewrites a work integral as a **flux integral** of the rotated field $(g, -f)$.

## Deriving the Divergence Theorem

By [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's theorem]]:

$$
\oint_\gamma (g, -f) \cdot \hat{n} \, ds = \oint_\gamma f \, dx + g \, dy = \iint_D (g_x - f_y) \, dx \, dy.
$$

But $g_x - f_y = g_x + (-f)_y = \nabla \cdot (g, -f)$. So:

$$
\oint_\gamma (g, -f) \cdot \hat{n} \, ds = \iint_D \nabla \cdot (g, -f) \, dx \, dy.
$$

Now rename: let $\mathbf{u} = (u_1, u_2)$ be any $C^1$ vector field. Set $g = u_1$ and $f = -u_2$, so $(g, -f) = (u_1, u_2) = \mathbf{u}$:

> [!theorem] Theorem §16.2: Divergence Theorem in $\mathbb{R}^2$
> Let $D \subseteq \mathbb{R}^2$ be a bounded domain with piecewise smooth boundary $\gamma = \partial D$, oriented counterclockwise. If $\mathbf{u} = (u_1, u_2)$ is $C^1$ on an open set containing $\overline{D}$, then:
>
> $$
> \boxed{\oint_\gamma \mathbf{u} \cdot \hat{n} \, ds = \iint_D \nabla \cdot \mathbf{u} \, dx \, dy}
> $$
>
> where $\nabla \cdot \mathbf{u} = \frac{\partial u_1}{\partial x} + \frac{\partial u_2}{\partial y}$ is the **divergence** of $\mathbf{u}$, and $\hat{n}$ is the outward unit normal to $\gamma$.

^thm-16-2

> [!remark]- Connections
> - Generalizes to [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|Divergence Theorem in ℝⁿ (§17.1)]] and, with surface integrals, [[Multivariable Analysis §18 Surface Integrals#^thm-18-2|Divergence Theorem in ℝ³ (§18.2)]].

> [!definition] Definition §16.4: Divergence
> The **divergence** of a vector field $\mathbf{u} = (u_1, u_2)$ is the scalar field:
>
> $$
> \nabla \cdot \mathbf{u} = \frac{\partial u_1}{\partial x} + \frac{\partial u_2}{\partial y}.
> $$
>
> **Physical interpretation:** $\nabla \cdot \mathbf{u} > 0$ at a point means the field acts as a **source** (net outflow); $\nabla \cdot \mathbf{u} < 0$ means it acts as a **sink** (net inflow).

^def-16-4

> [!remark]- Connections
> - First introduced with the gradient and curl in [[Multivariable Analysis §11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]]; in forms language: [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-4|d on 2-Forms Gives the Divergence (§22.4)]].

> [!example] Example §16.1: Divergence Computations
> **1.** $\mathbf{u}(x,y) = (x, y)$. Then $\nabla \cdot \mathbf{u} = \partial_x(x) + \partial_y(y) = 1 + 1 = 2$.
>
> Every point is a source with constant strength. This field “expands” uniformly.
>
> **2.** $\mathbf{u}(x,y) = \left(\dfrac{x}{r}, \dfrac{y}{r}\right)$ where $r = \sqrt{x^2 + y^2}$.
>
> $$
> \frac{\partial}{\partial x}\left( \frac{x}{r} \right) = \frac{r - x \cdot (x/r)}{r^2} = \frac{r^2 - x^2}{r^3} = \frac{y^2}{r^3}.
> $$
>
> Similarly, $\frac{\partial}{\partial y}\left( \dfrac{y}{r} \right) = \dfrac{x^2}{r^3}$. Therefore:
>
> $$
> \nabla \cdot \mathbf{u} = \frac{y^2}{r^3} + \frac{x^2}{r^3} = \frac{x^2 + y^2}{r^3} = \frac{r^2}{r^3} = \frac{1}{r}.
> $$
>
> The source strength decreases with distance from the origin.

^ex-16-1

## Green's Theorem as 2D Stokes' Theorem

We can also reinterpret Green's theorem using the **curl**.

> [!definition] Definition §16.5: Curl
> For a vector field $\mathbf{u} = (u_1, u_2, u_3)$ in $\mathbb{R}^3$, the **curl** is:
>
> $$
> \nabla \times \mathbf{u} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ \partial_x & \partial_y & \partial_z \\ u_1 & u_2 & u_3 \end{vmatrix} = \left( \frac{\partial u_3}{\partial y} - \frac{\partial u_2}{\partial z}, \;\; \frac{\partial u_1}{\partial z} - \frac{\partial u_3}{\partial x}, \;\; \frac{\partial u_2}{\partial x} - \frac{\partial u_1}{\partial y} \right).
> $$
>
> (This determinant is a notational mnemonic, not a literal determinant.)

^def-16-5

> [!remark]- Connections
> - First introduced in [[Multivariable Analysis §11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]]; in forms language: [[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-3|d on 1-Forms Gives the Curl (§22.3)]].

**Reduction to 2D.** For a planar vector field $\mathbf{u} = (u_1(x,y), \, u_2(x,y), \, 0)$ (with $u_3 = 0$ and no $z$-dependence):

$$
\nabla \times \mathbf{u} = \left( 0, \; 0, \; \frac{\partial u_2}{\partial x} - \frac{\partial u_1}{\partial y} \right).
$$

The only nonzero component is the $\hat{k}$-component: $(\nabla \times \mathbf{u})_3 = \frac{\partial u_2}{\partial x} - \frac{\partial u_1}{\partial y}$.

This is exactly the integrand in [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's theorem]]! With $\mathbf{u} = (f, g)$:

> [!theorem] Theorem §16.3: Green's Theorem as 2D Stokes' Theorem
> $$
> \oint_\gamma \mathbf{u} \cdot d\mathbf{x} = \iint_D (\nabla \times \mathbf{u}) \cdot \hat{k} \, dx \, dy
> $$
>
> where $\mathbf{u} = (f, g)$, $d\mathbf{x} = (dx, dy)$, and $(\nabla \times \mathbf{u}) \cdot \hat{k} = g_x - f_y$.

^thm-16-3

> [!remark]- Connections
> - The flat case of [[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1|Stokes' Theorem (§20.1)]], with $S = D$ and $\hat{n} = \hat{k}$.

> [!remark] Remark: Two Faces of Green's Theorem
> Green's theorem has two equivalent vector formulations:
>
> | **Form** | **Line integral** | **Area integral** |
> |---|---|---|
> | Circulation (Stokes) | $\oint_\gamma \mathbf{u} \cdot d\mathbf{x}$ | $\iint_D (\nabla \times \mathbf{u}) \cdot \hat{k} \, dA$ |
> | Flux (Divergence) | $\oint_\gamma \mathbf{u} \cdot \hat{n} \, ds$ | $\iint_D \nabla \cdot \mathbf{u} \, dA$ |
>
> The **[[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-3|Stokes form]]** relates the *circulation* of $\mathbf{u}$ around $\gamma$ (tangential component) to the total curl (“rotation”) inside $D$.
>
> The **[[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|Divergence form]]** relates the *flux* of $\mathbf{u}$ through $\gamma$ (normal component) to the total divergence (“expansion”) inside $D$.
>
> Both generalize to higher dimensions: [[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1|Stokes' theorem]] on surfaces in $\mathbb{R}^3$, and the [[Multivariable Analysis §18 Surface Integrals#^thm-18-2|Divergence Theorem]] on volumes in $\mathbb{R}^3$.

^rem-16-4
