---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 6
section: 18
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities]] · ↑ [[Multivariable Analysis — 6 Surface Integrals and the Classical Theorems]] · [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates]] →

> [!remark] Note: Smoothness Assumptions for This Section
> The results in this section require increasingly strong conditions on the parametrization $\mathbf{X}$, the surface $S$, and the vector field $\mathbf{F}$. Here is the hierarchy, from weakest to strongest:
>
> 1. **Tangent vectors exist:** $\mathbf{X}: D \to \mathbb{R}^3$ is $C^1$ (i.e., all partial derivatives $x_u, x_v, y_u, y_v, z_u, z_v$ exist and are continuous). This ensures the tangent vectors $\mathbf{X}_u, \mathbf{X}_v$ are well-defined and vary continuously.
> 2. **The parametrization describes a surface (regularity):** $\mathbf{X}$ is $C^1$ *and* the Jacobian $D\mathbf{X}$ ([[Multivariable Analysis §6 Differentiability#^def-6-2|Def. §6.2]]) has rank 2 everywhere, i.e., $\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$. This ensures a well-defined tangent plane at every point, and in particular ensures $|\mathbf{X}_u \times \mathbf{X}_v| > 0$ so the area element $dS$ is nondegenerate.
> 3. **The parametrization is injective** (on the interior of $D$): distinct parameter values give distinct surface points, so the surface does not self-intersect. Without this, the “surface area” might count some regions of $S$ multiple times.
> 4. **Orientability:** A continuous choice of unit normal $\hat{n}$ exists on all of $S$. This is needed for flux integrals (otherwise the sign of $\mathbf{F} \cdot \hat{n}$ is ambiguous). A regular parametrization automatically provides an orientation via $\hat{n} = (\mathbf{X}_u \times \mathbf{X}_v) / |\mathbf{X}_u \times \mathbf{X}_v|$; the question is whether different parametrizations of the same surface give consistent normals. (The Möbius strip is the classical example of a non-orientable surface.)
> 5. **For the integral theorems** (Divergence, Stokes): the boundary $\partial V$ or $\partial S$ must be **piecewise smooth** (finitely many smooth pieces joined along curves or edges), and the vector field $\mathbf{F}$ must be $C^1$ on an open set containing $\overline{V}$ (or $\overline{S}$). The piecewise smoothness allows us to decompose into pieces on which the proof works, and the $C^1$ condition on $\mathbf{F}$ ensures the divergence $\nabla \cdot \mathbf{F}$ ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-4|Def. §16.4]]) (or curl $\nabla \times \mathbf{F}$, [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-5|Def. §16.5]]) exists and is continuous.
>
> **Standing assumption for this section:** Unless stated otherwise, all parametrizations are $C^1$, injective on the interior of $D$, and regular. All surfaces are oriented. All vector fields are $C^1$.

^rem-18-1

## Parametrized Surfaces

### What is a Surface?

A **surface** $S$ is a subset of $\mathbb{R}^3$ that is locally two-dimensional: near any point, it “looks like” a piece of $\mathbb{R}^2$ that has been bent and placed into 3D space. Examples include spheres, cylinders, tori, and graphs $z = h(x,y)$.

**The problem:** To do calculus on $S$ (integrate functions, compute areas, etc.), we need a way to systematically describe *which points* belong to $S$. We need a coordinate system on $S$.

### Parametrization as a Coordinate System

We already understand curves: a curve in $\mathbb{R}^3$ is a map $t \mapsto \boldsymbol{\gamma}(t) = (x(t), y(t), z(t))$, one parameter tracing out a 1D object. A surface can be thought of as a **family of curves**: fix one parameter, say $u = u_0$, and let the other vary — the map $v \mapsto \mathbf{X}(u_0, v)$ traces out a curve on $S$. Now let $u_0$ vary continuously: the curve deforms, sweeping out a 2D region. The surface is the union of all these curves, one for each value of $u$.

So a **parametrization** labels every point on $S$ by two numbers $(u,v)$: one parameter ($v$) tells you where you are *along* a particular curve, and the other ($u$) tells you *which curve* you are on. Since a point in $\mathbb{R}^3$ is specified by $(x,y,z)$, this is a function:

$$
(u, v) \;\mapsto\; \text{point } \big( x(u,v), \, y(u,v), \, z(u,v) \big) \in S.
$$

We write this as $\mathbf{X}(u,v) = (x(u,v), y(u,v), z(u,v))$. Here:
- The domain $D \subseteq \mathbb{R}^2$ is the **parameter space** — a flat 2D region. Think of it as a “blueprint” for the surface.
- For each $(u,v) \in D$, the output $\mathbf{X}(u,v) \in \mathbb{R}^3$ is the **position** of the corresponding point on $S$. It is a vector only in the sense that points in $\mathbb{R}^3$ are identified with their position vectors from the origin; $\mathbf{X}(u,v)$ tells you *where the point sits* in 3D space.
- The surface is the image: $S = \mathbf{X}(D) = \{\mathbf{X}(u,v) : (u,v) \in D\}$.

The parametrization $\mathbf{X}: D \to \mathbb{R}^3$ is a “change of variables from 2D to 3D”: it takes a flat rectangle (or other 2D region) and wraps it into a curved surface in $\mathbb{R}^3$.

> [!definition] Definition §18.1: Parametrized Surface
> A **parametrized surface** in $\mathbb{R}^3$ is a $C^1$ map $\mathbf{X}: D \to \mathbb{R}^3$, where $D \subseteq \mathbb{R}^2$ is a domain, given by
>
> $$
> \mathbf{X}(u, v) = \big( x(u,v), \, y(u,v), \, z(u,v) \big).
> $$
>
> The image $S = \mathbf{X}(D) \subseteq \mathbb{R}^3$ is the **surface**, and $(u,v)$ are its **parameters** (coordinates on $S$).

^def-18-1

> [!example] Example §18.1: Sphere
> The unit sphere $S^2 = \{(x,y,z) : x^2 + y^2 + z^2 = R^2\}$ is a set of points in $\mathbb{R}^3$. To parametrize it, we use spherical angles $(\theta, \varphi)$:
>
> $$
> \mathbf{X}(\theta, \varphi) = (R\cos\varphi\cos\theta, \; R\cos\varphi\sin\theta, \; R\sin\varphi),
> $$
>
> with $\theta \in [0, 2\pi)$ and $\varphi \in (-\pi/2, \pi/2)$.
>
> Here $\mathbf{X}(\theta, \varphi)$ tells you: “the point on the sphere at longitude $\theta$ and latitude $\varphi$ has Cartesian coordinates $(R\cos\varphi\cos\theta, R\cos\varphi\sin\theta, R\sin\varphi)$.”

^ex-18-1

> [!remark] Remark: Dimension Count
> A 1D object (curve) in 1D space cannot curve — it fills the whole space. A 1D object in 2D space *can* curve. Similarly, a surface is a 2D object that can curve only when it lives in 3D (or higher) space. The parametrization $\mathbf{X}: \mathbb{R}^2 \to \mathbb{R}^3$ maps a flat 2D domain into 3D, and the image can be curved.

^rem-18-2

## Tangent Vectors and Regularity

Fix a point $(u_0, v_0) \in D$. The two families of curves through this point give two tangent directions:
- The **$u$-curve** $u \mapsto \mathbf{X}(u, v_0)$ (fix $v$, vary $u$) has tangent vector $\mathbf{X}_u$.
- The **$v$-curve** $v \mapsto \mathbf{X}(u_0, v)$ (fix $u$, vary $v$) has tangent vector $\mathbf{X}_v$.

These are exactly the tangent vectors to the two families of curves that sweep out the surface.

> [!definition] Definition §18.2: Tangent Vectors
> The **tangent vectors** to the surface at $(u_0, v_0)$ are:
>
> $$
> \mathbf{X}_u = \left( \frac{\partial x}{\partial u}, \, \frac{\partial y}{\partial u}, \, \frac{\partial z}{\partial u} \right), \qquad \mathbf{X}_v = \left( \frac{\partial x}{\partial v}, \, \frac{\partial y}{\partial v}, \, \frac{\partial z}{\partial v} \right).
> $$

^def-18-2

![[m452-18-1.svg]]
*The surface integral is computed cell by cell: a grid cell $\Delta u \times \Delta v$ in the parameter domain (red, left) is carried by $\mathbf{X}$ to a curved patch on the surface (red, right). Zoomed to this scale, the patch is approximated by the tangent parallelogram (green) spanned by $\mathbf{X}_u\Delta u$ and $\mathbf{X}_v\Delta v$, with area $|\mathbf{X}_u \times \mathbf{X}_v|\,\Delta u\,\Delta v$. Summing over all cells and refining gives $\iint_S dS = \iint_D |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$: the cross product length is the area-scaling factor, playing exactly the role $|J|$ played in [[Multivariable Analysis §15 Multivariable Integration|§15]] — and $|\mathbf{r}'|$ in [[Multivariable Analysis §16 Line Integrals and Green's Theorem|§16]].*

> [!definition] Definition §18.3: Regular Point
> The surface is **regular** at $(u_0, v_0)$ if $\mathbf{X}_u$ and $\mathbf{X}_v$ are [[Linear Algebra 2A Span and Linear Independence#^ladr-2-15|linearly independent]] at that point, i.e., $\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$.
>
> A surface is **regular** if it is regular at every point of $D$.

^def-18-3

**Geometric meaning:** At a regular point, the $u$-curves and $v$-curves cross transversally, spanning a 2D tangent plane. If $\mathbf{X}_u$ and $\mathbf{X}_v$ are parallel (or one is zero), the two families of curves are tangent to each other — they fail to sweep out a genuine 2D surface at that point, and the parametrization degenerates.

> [!remark] Remark: Regularity as a Rank Condition on the Derivative
> The regularity condition is best understood through the differentiability framework of [[Multivariable Analysis §6 Differentiability|Section 6]], applied to $\mathbf{X}: \mathbb{R}^2 \to \mathbb{R}^3$.
>
> **The derivative of $\mathbf{X}$.** Differentiability of $\mathbf{X}$ at $(u_0, v_0)$ ([[Multivariable Analysis §6 Differentiability#^def-6-1|Def. §6.1]]) means:
>
> $$
> \mathbf{X}(u_0 + h, v_0 + k) = \mathbf{X}(u_0, v_0) + D\mathbf{X} \begin{pmatrix} h \\ k \end{pmatrix} + o\!\left(\sqrt{h^2 + k^2}\right)
> $$
>
> where $D\mathbf{X}$ is the $3 \times 2$ Jacobian matrix ([[Multivariable Analysis §6 Differentiability#^def-6-2|Def. §6.2]]) whose columns are $\mathbf{X}_u$ and $\mathbf{X}_v$:
>
> $$
> D\mathbf{X} = \begin{pmatrix} x_u & x_v \\ y_u & y_v \\ z_u & z_v \end{pmatrix}.
> $$
>
> The image of $D\mathbf{X}$ — the set of all vectors $h \mathbf{X}_u + k \mathbf{X}_v$ — is the **tangent space**. Its dimension equals $\operatorname{rank}(D\mathbf{X})$ ([[Linear Algebra 3C Matrices#^ladr-3-58|LADR 3.58]]):
> - **Rank 2** ($\mathbf{X}_u, \mathbf{X}_v$ independent, i.e., regular): the image of $D\mathbf{X}$ is a 2D plane. The linear approximation faithfully represents a 2D surface. This is the good case.
> - **Rank 1** ($\mathbf{X}_u, \mathbf{X}_v$ parallel): the image is a line. The derivative compresses two dimensions into one — the parametrization “folds” the $(u,v)$-plane onto a curve at that point.
> - **Rank 0** ($\mathbf{X}_u = \mathbf{X}_v = \mathbf{0}$): the image is a point. The derivative gives zero information about the surface.
>
> So the surface is differentiable in all three cases (the linear approximation exists), but **regularity ensures the approximation is full-dimensional** — that it is actually approximating a *surface* and not a lower-dimensional object.
>
> **Parallel to earlier results.** This is the same idea as the change of variables theorem and the IFT:
> - In the **change of variables** ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-17|Section 15]]), $J \neq 0$ means the $2 \times 2$ Jacobian has rank 2, ensuring the map is locally invertible.
> - In the **IFT/Inverse FT** (Sections [[Multivariable Analysis §12 The Implicit Function Theorem#^thm-12-2|12]]–[[Multivariable Analysis §13 The Inverse Function Theorem#^thm-13-2|13]]), the nonvanishing determinant ensures the derivative has full rank.
> - Here, $\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$ means the $3 \times 2$ Jacobian has rank 2, ensuring the parametrization is locally injective (an **immersion**) — it does not collapse any direction.
>
> This also explains why $\det(G) = |\mathbf{X}_u \times \mathbf{X}_v|^2$ appears in the area formula ([[Multivariable Analysis §18 Surface Integrals#^thm-18-1|Theorem §18.1]]): it measures how much 2D area the derivative preserves. When $\det(G) = 0$, the derivative crushes some 2D area to zero — exactly the degenerate case.
>
> **Irregular point $\neq$ singular surface.** An irregular point can mean two different things:
> - **Bad parametrization, smooth surface.** The sphere parametrized by $(\theta, \varphi)$ ([[Multivariable Analysis §18 Surface Integrals#^ex-18-1|Example §18.1]]) has $\mathbf{X}_\theta = \mathbf{0}$ at the poles ($\varphi = \pm \pi/2$), because all values of $\theta$ map to the same point. The sphere is perfectly smooth there; the coordinate system degenerates. A different parametrization (e.g., centered at the pole) would be regular.
> - **Genuinely singular surface.** The cone $\mathbf{X}(u,v) = (v\cos u, v\sin u, v)$ has $\mathbf{X}_u = \mathbf{0}$ at the tip $v = 0$. No reparametrization can fix this — the cone tip has no well-defined tangent plane; it is not a smooth 2D surface.
>
> Distinguishing these cases requires checking whether the singularity persists under all possible reparametrizations — a question taken up systematically in differential geometry (MATH 591).

^rem-18-3

## Surface Area

### The Idea: Infinitesimal Parallelograms

A small change $du \times dv$ in the parameter domain maps to a “curved parallelogram” on the surface. The two edge vectors of this parallelogram are approximately:

$$
\boldsymbol{\alpha} = \mathbf{X}_u \, du, \qquad \boldsymbol{\beta} = \mathbf{X}_v \, dv.
$$

The area of the parallelogram spanned by $\boldsymbol{\alpha}$ and $\boldsymbol{\beta}$ is $|\boldsymbol{\alpha} \times \boldsymbol{\beta}| = |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv$.

In 3D, the cross product $\mathbf{X}_u \times \mathbf{X}_v$ gives a vector:
- **direction:** perpendicular to both $\mathbf{X}_u$ and $\mathbf{X}_v$ (i.e., normal to the surface),
- **magnitude:** $|\mathbf{X}_u \times \mathbf{X}_v|$ = area of the parallelogram generated by $\mathbf{X}_u$ and $\mathbf{X}_v$.

Therefore the surface area element is:

$$
dS = |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv.
$$

But we want a formula for area that works in *any* ambient dimension (not just $\mathbb{R}^3$), where the cross product is not defined. We need a formula that uses only **dot products** ([[Linear Algebra 6A Inner Products and Norms#^ladr-6-1|LADR 6.1]]).

### The Gram Matrix (First Fundamental Form)

> [!definition] Definition §18.4: Gram Matrix
> The **Gram matrix** (or **first fundamental form**) of the parametrized surface is the $2 \times 2$ matrix:
>
> $$
> G = \begin{pmatrix} \mathbf{X}_u \cdot \mathbf{X}_u & \mathbf{X}_u \cdot \mathbf{X}_v \\ \mathbf{X}_v \cdot \mathbf{X}_u & \mathbf{X}_v \cdot \mathbf{X}_v \end{pmatrix} = \begin{pmatrix} E & F \\ F & G \end{pmatrix}
> $$
>
> where the classical notation is $E = |\mathbf{X}_u|^2$, $F = \mathbf{X}_u \cdot \mathbf{X}_v$, $G = |\mathbf{X}_v|^2$.

^def-18-4

> [!theorem] Theorem §18.1: Surface Area via the Gram Matrix
> The surface area element is:
>
> $$
> \boxed{dS = \sqrt{\det(G)} \, du \, dv = \sqrt{EG - F^2} \, du \, dv}
> $$
>
> In $\mathbb{R}^3$, this equals $|\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv$.

^thm-18-1

> [!proof]+ Proof
> We prove the claim in $\mathbb{R}^3$: $\det(G) = |\mathbf{X}_u \times \mathbf{X}_v|^2$.
>
> Write $\mathbf{X}_u = (x_u, y_u, z_u)$ and $\mathbf{X}_v = (x_v, y_v, z_v)$.
>
> **Left side:**
>
> $$
> \begin{aligned}
> \det(G) &= (\mathbf{X}_u \cdot \mathbf{X}_u)(\mathbf{X}_v \cdot \mathbf{X}_v) - (\mathbf{X}_u \cdot \mathbf{X}_v)^2 \\
> &= (x_u^2 + y_u^2 + z_u^2)(x_v^2 + y_v^2 + z_v^2) - (x_u x_v + y_u y_v + z_u z_v)^2.
> \end{aligned}
> $$
>
> **Expand the product** $(x_u^2 + y_u^2 + z_u^2)(x_v^2 + y_v^2 + z_v^2)$: this has 9 terms:
>
> $$
> x_u^2 x_v^2 + x_u^2 y_v^2 + x_u^2 z_v^2 + y_u^2 x_v^2 + y_u^2 y_v^2 + y_u^2 z_v^2 + z_u^2 x_v^2 + z_u^2 y_v^2 + z_u^2 z_v^2.
> $$
>
> **Expand the square** $(x_u x_v + y_u y_v + z_u z_v)^2$: this has 9 terms:
>
> $$
> x_u^2 x_v^2 + y_u^2 y_v^2 + z_u^2 z_v^2 + 2x_u x_v y_u y_v + 2x_u x_v z_u z_v + 2y_u y_v z_u z_v.
> $$
>
> **Subtract:** The three “diagonal” terms $x_u^2 x_v^2, y_u^2 y_v^2, z_u^2 z_v^2$ cancel. The remaining 6 terms from the product minus the 3 cross terms from the square give:
>
> $$
> \begin{aligned}
> \det(G) &= (x_u^2 y_v^2 + y_u^2 x_v^2 - 2x_u x_v y_u y_v) \\
> &\quad + (x_u^2 z_v^2 + z_u^2 x_v^2 - 2x_u x_v z_u z_v) \\
> &\quad + (y_u^2 z_v^2 + z_u^2 y_v^2 - 2y_u y_v z_u z_v) \\
> &= (x_u y_v - x_v y_u)^2 + (z_u x_v - z_v x_u)^2 + (z_u y_v - z_v y_u)^2.
> \end{aligned}
> $$
>
> **Right side:**
>
> $$
> \mathbf{X}_u \times \mathbf{X}_v = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ x_u & y_u & z_u \\ x_v & y_v & z_v \end{vmatrix} = (y_u z_v - z_u y_v, \;\; z_u x_v - x_u z_v, \;\; x_u y_v - y_u x_v).
> $$
>
> Therefore:
>
> $$
> |\mathbf{X}_u \times \mathbf{X}_v|^2 = (y_u z_v - z_u y_v)^2 + (z_u x_v - x_u z_v)^2 + (x_u y_v - y_u x_v)^2.
> $$
>
> Comparing: LHS $=$ RHS.

^pf-18-1

*Uses:* [[Multivariable Analysis §18 Surface Integrals#^def-18-2|Def. §18.2]], [[Multivariable Analysis §18 Surface Integrals#^def-18-4|Def. §18.4]], [[Linear Algebra 6A Inner Products and Norms#^ladr-6-1|LADR 6.1]]

> [!remark]- Connections
> - The linear algebra behind it: $G = (D\mathbf{X})^{T} D\mathbf{X}$ is $T^*T$ for $T = D\mathbf{X}$, so $\operatorname{rank} G = \operatorname{rank} D\mathbf{X}$ ([[Linear Algebra 7E Singular Value Decomposition#^ladr-7-64|LADR 7.64]]) and $\det G > 0$ exactly at regular points ([[Multivariable Analysis §18 Surface Integrals#^def-18-3|Def. §18.3]]).
> - When $D\mathbf{X}$ is square, $\sqrt{\det(T^*T)} = |\det T|$ ([[Linear Algebra 9C Determinants#^ladr-9-60|LADR 9.60]], [[Linear Algebra 9C Determinants#^ladr-9-61|LADR 9.61]]): the $|J|$ of [[Multivariable Analysis §15 Multivariable Integration#^thm-15-20|Change of Variables in ℝⁿ]].
> - The same area element pulled back as a 2-form: [[Multivariable Analysis §22 The Algebra of Differential Forms#^ex-22-3|Pullback Along a Surface]].

> [!remark] Remark: Why the Gram Matrix?
> In $\mathbb{R}^3$, we could just use $|\mathbf{X}_u \times \mathbf{X}_v|$ directly. The Gram matrix formulation is preferred because:
> - It works in **any ambient dimension**: for a 2D surface in $\mathbb{R}^n$ ($n > 3$), the cross product is not defined, but the Gram matrix $G = (\mathbf{X}_u \cdot \mathbf{X}_v)$ always makes sense, and $\sqrt{\det(G)}$ always gives the correct area element.
> - It is the starting point of **Riemannian geometry**: the Gram matrix is the metric tensor of the surface, encoding intrinsic distances and angles.

^rem-18-4

## The Scalar Surface Integral

With the area element $dS = |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv$ in hand, we can integrate scalar functions over surfaces. The logic is identical to the scalar line integral ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-1|Def. §16.1]]): weight each infinitesimal piece of the surface by the value of $f$ at that point.

> [!definition] Definition §18.5: Scalar Surface Integral
> Let $S$ be a regular parametrized surface $\mathbf{X}: D \to \mathbb{R}^3$ and let $f: S \to \mathbb{R}$ be continuous. The **scalar surface integral** of $f$ over $S$ is:
>
> $$
> \iint_S f \, dS = \iint_D f(\mathbf{X}(u,v)) \, |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv.
> $$
>
> In particular, the **surface area** of $S$ is:
>
> $$
> \text{Area}(S) = \iint_S 1 \, dS = \iint_D |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv = \iint_D \sqrt{\det(G)} \, du \, dv.
> $$

^def-18-5

> [!remark]- Connections
> - One dimension down: the [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-1|Scalar Line Integral]].
> - Not an integral of a differential form (no orientation): [[Multivariable Analysis §22 The Algebra of Differential Forms#^rem-22-8|Scalar Integrals Are Not Form Integrals]].

**Interpretation:** If $f$ represents mass density (mass per unit area), then $\iint_S f \, dS$ is the total mass of a thin shell shaped like $S$.

**Comparison with line integrals:**

| | **Curve** $\gamma$ | **Surface** $S$ |
|---|:---:|:---:|
| Parametrization | $\boldsymbol{\gamma}(t)$, $t \in [a,b]$ | $\mathbf{X}(u,v)$, $(u,v) \in D$ |
| Length / Area element | $ds = \vert\boldsymbol{\gamma}'(t)\vert \, dt$ | $dS = \vert\mathbf{X}_u \times \mathbf{X}_v\vert \, du \, dv$ |
| Scalar integral | $\int_\gamma f \, ds$ | $\iint_S f \, dS$ |

> [!example] Example §18.2: Surface Area of a Sphere
> Parametrize the sphere of radius $R$ by $\mathbf{X}(\theta, \varphi) = (R\cos\varphi\cos\theta, R\cos\varphi\sin\theta, R\sin\varphi)$ with $\theta \in [0, 2\pi)$, $\varphi \in (-\pi/2, \pi/2)$ ([[Multivariable Analysis §18 Surface Integrals#^ex-18-1|Example §18.1]]).
>
> Compute the tangent vectors:
>
> $$
> \begin{aligned}
> \mathbf{X}_\theta &= (-R\cos\varphi\sin\theta, \; R\cos\varphi\cos\theta, \; 0), \\
> \mathbf{X}_\varphi &= (-R\sin\varphi\cos\theta, \; -R\sin\varphi\sin\theta, \; R\cos\varphi).
> \end{aligned}
> $$
>
> The cross product:
>
> $$
> \begin{aligned}
> \mathbf{X}_\theta \times \mathbf{X}_\varphi &= \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ -R\cos\varphi\sin\theta & R\cos\varphi\cos\theta & 0 \\ -R\sin\varphi\cos\theta & -R\sin\varphi\sin\theta & R\cos\varphi \end{vmatrix} \\
> &= (R^2\cos^2\!\varphi\cos\theta, \; R^2\cos^2\!\varphi\sin\theta, \; R^2\cos\varphi\sin\varphi).
> \end{aligned}
> $$
>
> Its magnitude:
>
> $$
> |\mathbf{X}_\theta \times \mathbf{X}_\varphi| = R^2\cos\varphi \sqrt{\cos^2\!\varphi\cos^2\!\theta + \cos^2\!\varphi\sin^2\!\theta + \sin^2\!\varphi} = R^2\cos\varphi \cdot 1 = R^2\cos\varphi.
> $$
>
> (Here $\cos\varphi > 0$ since $\varphi \in (-\pi/2, \pi/2)$.)
>
> Surface area ([[Multivariable Analysis §18 Surface Integrals#^def-18-5|Def. §18.5]]):
>
> $$
> \text{Area}(S^2) = \int_0^{2\pi} \int_{-\pi/2}^{\pi/2} R^2 \cos\varphi \, d\varphi \, d\theta = R^2 \cdot 2\pi \cdot \big[\sin\varphi\big]_{-\pi/2}^{\pi/2} = R^2 \cdot 2\pi \cdot 2 = \boxed{4\pi R^2}.
> $$

^ex-18-2

## The Vector Surface Integral (Flux)

Just as the Type II line integral $\oint \mathbf{F} \cdot d\mathbf{r}$ ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^def-16-2|Def. §16.2]]) measures the work done by a vector field along a curve, the **flux integral** measures how much of a vector field passes *through* a surface.

### The Normal Vector and Orientation

At a regular point, the cross product $\mathbf{X}_u \times \mathbf{X}_v$ is a nonzero vector perpendicular to the tangent plane. It defines a **unit normal**:

$$
\hat{n} = \frac{\mathbf{X}_u \times \mathbf{X}_v}{|\mathbf{X}_u \times \mathbf{X}_v|}.
$$

The choice of which direction is “outward” depends on the orientation of the parametrization (the ordering of $u, v$). Reversing the parametrization (swapping $u \leftrightarrow v$) flips the sign of the cross product, hence flips $\hat{n}$.

### Definition and Derivation

Consider a vector field $\mathbf{F}(x,y,z) = (P, Q, R)$ representing (say) fluid flow velocity. The flux of $\mathbf{F}$ through a small surface element is:

$$
\mathbf{F} \cdot \hat{n} \, dS = \mathbf{F} \cdot \frac{\mathbf{X}_u \times \mathbf{X}_v}{|\mathbf{X}_u \times \mathbf{X}_v|} \cdot |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv = \mathbf{F} \cdot (\mathbf{X}_u \times \mathbf{X}_v) \, du \, dv.
$$

The $|\mathbf{X}_u \times \mathbf{X}_v|$ cancels, giving a cleaner formula:

> [!definition] Definition §18.6: Vector Surface Integral / Flux Integral
> Let $S$ be an oriented regular surface parametrized by $\mathbf{X}: D \to \mathbb{R}^3$, and let $\mathbf{F} = (P, Q, R)$ be a continuous vector field on $S$. The **flux** of $\mathbf{F}$ through $S$ is:
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \hat{n} \, dS = \iint_D \mathbf{F}(\mathbf{X}(u,v)) \cdot (\mathbf{X}_u \times \mathbf{X}_v) \, du \, dv.
> $$
>
> The notation $d\mathbf{S} = \hat{n} \, dS = (\mathbf{X}_u \times \mathbf{X}_v) \, du \, dv$ is the **vector area element**.

^def-18-6

> [!remark]- Connections
> - In the language of forms, the flux integral is the integral of a 2-form: [[Multivariable Analysis §22 The Algebra of Differential Forms#^def-22-6|Integration of a 2-Form over a Surface]], [[Multivariable Analysis §22 The Algebra of Differential Forms#^rem-22-7|2-Form Integration Recovers the Flux Integral]].
> - The cross product $\mathbf{X}_u \times \mathbf{X}_v$ is a pullback: [[Multivariable Analysis §22 The Algebra of Differential Forms#^rem-22-3|The Cross Product Is the Pullback in Disguise]].

**Interpretation:** $\iint_S \mathbf{F} \cdot d\mathbf{S}$ measures the net rate at which “stuff” (fluid, electric field, etc.) flows through $S$ in the direction of $\hat{n}$.

**Comparison with line integrals:**

| | **Curve** $\gamma$ | **Surface** $S$ |
|---|:---:|:---:|
| Scalar integral | $\int_\gamma f \, ds$ (Type I) | $\iint_S f \, dS$ |
| Vector integral | $\int_\gamma \mathbf{F} \cdot d\mathbf{r}$ (work) | $\iint_S \mathbf{F} \cdot d\mathbf{S}$ (flux) |
| Key vector | tangent $\boldsymbol{\gamma}'$ | normal $\mathbf{X}_u \times \mathbf{X}_v$ |

Note the geometric duality: the line integral uses the *tangent* vector (measuring the component of $\mathbf{F}$ *along* the curve), while the surface integral uses the *normal* vector (measuring the component of $\mathbf{F}$ *through* the surface).

> [!remark] Remark: Connection to the Divergence Theorem and Stokes' Theorem
> The flux integral is exactly the left-hand side of the **Divergence Theorem** ([[Multivariable Analysis §18 Surface Integrals#^thm-18-2|Theorem §18.2]]):
>
> $$
> \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F} \, dV,
> $$
>
> which relates the flux through a closed surface $\partial V$ to the total divergence inside the enclosed volume $V$.
>
> Similarly, **Stokes' theorem** ([[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^thm-20-1|Theorem §20.1]]) relates a line integral around $\partial S$ to a flux integral of the curl through $S$:
>
> $$
> \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}.
> $$
>
> Both theorems require the surface integral machinery we have now developed.

^rem-18-5

## Graph Surfaces

An important special case: the surface is the graph of a function $z = \phi(x,y)$ over a domain $D \subseteq \mathbb{R}^2$. This gives the simplest parametrization and the most explicit formulas.

**Parametrization:** Use $(x,y)$ themselves as parameters:

$$
\mathbf{X}(x, y) = (x, \, y, \, \phi(x,y)).
$$

**Tangent vectors:**

$$
\mathbf{X}_x = \left(1, \, 0, \, \phi_x\right), \qquad \mathbf{X}_y = \left(0, \, 1, \, \phi_y\right).
$$

**Cross product:**

$$
\mathbf{X}_x \times \mathbf{X}_y = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 0 & \phi_x \\ 0 & 1 & \phi_y \end{vmatrix} = (-\phi_x, \; -\phi_y, \; 1).
$$

Note that the $\hat{k}$-component is $+1$, so this normal points **upward** (positive $z$-direction).

**Magnitude:**

$$
|\mathbf{X}_x \times \mathbf{X}_y| = \sqrt{\phi_x^2 + \phi_y^2 + 1}.
$$

**Unit outward normal** (upward):

$$
\hat{n} = \frac{(-\phi_x, \, -\phi_y, \, 1)}{\sqrt{\phi_x^2 + \phi_y^2 + 1}}.
$$

**Area element:**

$$
dS = |\mathbf{X}_x \times \mathbf{X}_y| \, dx \, dy = \sqrt{1 + \phi_x^2 + \phi_y^2} \, dx \, dy.
$$

**Flux of $\mathbf{u} = (a, b, c)$ through the graph surface:**

$$
\begin{aligned}
\iint_S \mathbf{u} \cdot \hat{n} \, dS &= \iint_D (a, b, c) \cdot (-\phi_x, -\phi_y, 1) \, dx \, dy \\
&= \iint_D \big( -a\phi_x - b\phi_y + c \big) \, dx \, dy.
\end{aligned}
$$

Note the cancellation: $\hat{n} \, dS = \frac{(-\phi_x, -\phi_y, 1)}{\sqrt{1+\phi_x^2+\phi_y^2}} \cdot \sqrt{1+\phi_x^2+\phi_y^2} \, dx \, dy = (-\phi_x, -\phi_y, 1) \, dx \, dy$. The square root appears in both $\hat{n}$ and $dS$ and cancels in the flux integral.

> [!remark] Remark: Component-by-Component Flux
> For a general vector field $\mathbf{u} = (a(x,y,z), \, b(x,y,z), \, c(x,y,z))$, the flux through the graph $z = \phi(x,y)$ involves three terms, one per component:
>
> $$
> \iint_S \mathbf{u} \cdot \hat{n} \, dS = \iint_D \big[ a \cdot n_1 + b \cdot n_2 + c \cdot n_3 \big] \, dS.
> $$
>
> For each component, we parametrize the surface by the “best choice” of two coordinates: the top/bottom surfaces use $(x,y)$, the left/right surfaces use $(y,z)$, and the front/back surfaces use $(x,z)$. This is exactly how the proof of the Divergence Theorem ([[Multivariable Analysis §18 Surface Integrals#^thm-18-2|Theorem §18.2]]) proceeds.

^rem-18-6

## The Divergence Theorem in $\mathbb{R}^3$: Proof

### Orientation Convention for Closed Surfaces

For a closed surface $\partial V$ bounding a volume $V$:
- The **positive orientation** is defined by the **outward normal**: $\hat{n}$ points out of $V$.
- Equivalently (right-hand rule): if you walk along a closed curve on $\partial V$ with $V$ on your left and look against $\hat{n}$, you are walking counterclockwise.
- A proper parametrization of $\partial V$ should yield a continuous outward-pointing normal field.

> [!theorem] Theorem §18.2: Divergence Theorem in $\mathbb{R}^3$
> Let $V \subseteq \mathbb{R}^3$ be a bounded region with piecewise smooth boundary $\partial V$, oriented with outward normal. If $\mathbf{u} = (a, b, c)$ is $C^1$ on an open set containing $\overline{V}$, then:
>
> $$
> \boxed{\iint_{\partial V} \mathbf{u} \cdot \hat{n} \, dS = \iiint_V \nabla \cdot \mathbf{u} \, dV = \iiint_V \left( \frac{\partial a}{\partial x} + \frac{\partial b}{\partial y} + \frac{\partial c}{\partial z} \right) dV}
> $$

^thm-18-2

> [!proof]+ Proof
> By linearity ([[Multivariable Analysis §15 Multivariable Integration#^thm-15-3|Theorem §15.3]]), it suffices to prove the identity for each component separately:
>
> $$
> \iint_{\partial V} a \, n_1 \, dS = \iiint_V \frac{\partial a}{\partial x} \, dV, \quad \iint_{\partial V} b \, n_2 \, dS = \iiint_V \frac{\partial b}{\partial y} \, dV, \quad \iint_{\partial V} c \, n_3 \, dS = \iiint_V \frac{\partial c}{\partial z} \, dV.
> $$
>
> We prove the third identity (the $z$-component); the others follow by the same argument with the roles of coordinates permuted.
>
> **Step 1: Represent $V$ using upper and lower graphs.**
>
> Assume $V$ can be written as:
>
> $$
> V = \{(x,y,z) : (x,y) \in D, \;\; \phi(x,y) \leq z \leq \psi(x,y)\}
> $$
>
> where $D \subseteq \mathbb{R}^2$ is the projection onto the $(x,y)$-plane, and $\phi, \psi$ are $C^1$ functions with $\phi \leq \psi$.
>
> **Step 2: Evaluate the volume integral via [[Fundamental Theorem of Calculus|FTC]].**
>
> $$
> \iiint_V \frac{\partial c}{\partial z} \, dV = \iint_D \left( \int_{\phi(x,y)}^{\psi(x,y)} \frac{\partial c}{\partial z} \, dz \right) dx \, dy = \iint_D \big[ c(x, y, \psi(x,y)) - c(x, y, \phi(x,y)) \big] \, dx \, dy.
> $$
>
> **Step 3: Evaluate the boundary flux integral.**
>
> The boundary $\partial V$ consists of three parts:
>
> *Top surface* $S_{\text{top}}$: $z = \psi(x,y)$, parametrized by $\mathbf{X}(x,y) = (x, y, \psi(x,y))$.
>
> Tangent vectors: $\mathbf{X}_x = (1, 0, \psi_x)$, $\mathbf{X}_y = (0, 1, \psi_y)$.
>
> Cross product: $\mathbf{X}_x \times \mathbf{X}_y = (-\psi_x, -\psi_y, 1)$. The $\hat{k}$-component is $+1$, so this points **upward** — out of $V$. Good: this is the outward normal.
>
> Unit outward normal: $\hat{n} = \dfrac{(-\psi_x, -\psi_y, 1)}{\sqrt{1 + \psi_x^2 + \psi_y^2}}$, and $dS = \sqrt{1 + \psi_x^2 + \psi_y^2} \, dx \, dy$.
>
> The $\sqrt{1 + \psi_x^2 + \psi_y^2}$ cancels between $\hat{n}$ and $dS$, giving $n_3 \, dS = +dx \, dy$:
>
> $$
> \iint_{S_{\text{top}}} c \, n_3 \, dS = \iint_D c(x, y, \psi(x,y)) \, dx \, dy.
> $$
>
> *Bottom surface* $S_{\text{bot}}$: $z = \phi(x,y)$, parametrized by $\mathbf{X}(x,y) = (x, y, \phi(x,y))$.
>
> If we naively compute $\mathbf{X}_x \times \mathbf{X}_y = (-\phi_x, -\phi_y, 1)$, this points upward — *into* $V$. This is the wrong orientation: the outward normal on the bottom should point *downward*.
>
> The issue is that the direction of $\mathbf{X}_u \times \mathbf{X}_v$ depends on the **ordering of the parameters**. To get the outward-pointing normal, we **reverse the parameter order**, using $\mathbf{X}_y \times \mathbf{X}_x$ instead:
>
> $$
> \mathbf{X}_y \times \mathbf{X}_x = -(\mathbf{X}_x \times \mathbf{X}_y) = (\phi_x, \, \phi_y, \, -1).
> $$
>
> The $\hat{k}$-component is now $-1$ — pointing downward, which is genuinely outward for the bottom of $V$. The sign is not imposed by hand; it comes from the anti-commutativity of the cross product ($\mathbf{a} \times \mathbf{b} = -\mathbf{b} \times \mathbf{a}$), which geometrically means reversing the parameter ordering reverses the orientation.
>
> After cancellation: $n_3 \, dS = -dx \, dy$:
>
> $$
> \iint_{S_{\text{bot}}} c \, n_3 \, dS = -\iint_D c(x, y, \phi(x,y)) \, dx \, dy.
> $$
>
> *Lateral surface* $S_{\text{side}}$: on the vertical walls, $\hat{n}$ is horizontal (perpendicular to the $z$-axis), so $n_3 = 0$ and this surface contributes zero to $\iint c \, n_3 \, dS$.
>
> **Step 4: Compare.**
>
> $$
> \iint_{\partial V} c \, n_3 \, dS = \iint_D c(x,y,\psi) \, dx \, dy - \iint_D c(x,y,\phi) \, dx \, dy = \iiint_V \frac{\partial c}{\partial z} \, dV.
> $$
>
> The $x$- and $y$-components follow identically: for $\iint a \, n_1 \, dS = \iiint \partial_x a \, dV$, represent $V$ using left/right graphs $x = \alpha(y,z)$ and $x = \beta(y,z)$, and parametrize those surfaces by $(y,z)$. Similarly for $b$.
>
> Summing all three components gives the full Divergence Theorem.

^pf-18-2

*Uses:* [[Multivariable Analysis §15 Multivariable Integration#^thm-15-3|§15.3]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]], [[Fundamental Theorem of Calculus|451 §34.1]], [[Multivariable Analysis §18 Surface Integrals#^def-18-6|Def. §18.6]], [[Multivariable Analysis §18 Surface Integrals#^def-18-2|Def. §18.2]]

![[m452-18-2.svg]]
*The divergence theorem: $\iint_{\partial V}\mathbf{F}\cdot\hat{n}\,dS = \iiint_V \nabla\cdot\mathbf{F}\,dV$. Everything the sources inside $V$ produce (red: pointwise divergence, the microscopic outflux of [[Multivariable Analysis §11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]]) must exit through the boundary (green arrows crossing $\partial V$ along the outward normal $\hat n$). The proof is again the cancellation of [[Multivariable Analysis §16 Line Integrals and Green's Theorem|§16]], one dimension up: tile $V$ into small cells; flux through every interior face cancels between neighbors, and only the outer boundary flux survives.*

> [!remark]- Connections
> - The 2D version: [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|Divergence Theorem in ℝ²]]; the $n$-dimensional version: [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|Divergence Theorem in ℝⁿ]].
> - The 1D case is the [[Fundamental Theorem of Calculus]]; all are instances of the [[Multivariable Analysis §23 The Generalized Stokes' Theorem#^thm-23-1|Generalized Stokes' Theorem]] with $d$ on 2-forms giving the divergence ([[Multivariable Analysis §22 The Algebra of Differential Forms#^prop-22-4|Prop. §22.4]]).

> [!remark] Remark: Why the Bottom Surface Has Reversed Orientation
> The parameter reversal for the bottom surface is not a trick — it is the higher-dimensional manifestation of the sign pattern in the [[Fundamental Theorem of Calculus]].
>
> **1D:** $\int_a^b f'(x)\,dx = f(b) - f(a)$. The “boundary” of $[a,b]$ is two points. The outward normal at $b$ is $+1$ (pointing right, away from the interval), at $a$ is $-1$ (pointing left). Upper endpoint gets $+$, lower gets $-$.
>
> **2D ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Green's theorem]]):** The boundary $\gamma$ of $D$ is traversed counterclockwise. The bottom edge $y = \phi(x)$ is traversed left-to-right ($x: a \to b$), but the top edge $y = \psi(x)$ is traversed right-to-left ($x: b \to a$) — because we go *around* the boundary, not across it. This reversed traversal produces the sign.
>
> **3D:** The boundary $\partial V$ is a closed surface. Standing outside and looking at the top, you see the outward normal pointing up. Walking around to look at the bottom from outside, you see the outward normal pointing down — and the surface appears **mirror-reflected** (left and right swap). The “natural” parametrization of the bottom, as seen from outside, has one coordinate reversed relative to the top.
>
> There are three equivalent ways to implement this:
> 1. **Swap cross product order:** use $\mathbf{X}_y \times \mathbf{X}_x$ instead of $\mathbf{X}_x \times \mathbf{X}_y$ (what we did in the proof).
> 2. **Reverse one parameter:** parametrize the bottom by $(s, y)$ where $s = a + b - x$ runs backwards, so $\tilde{\mathbf{X}}_s = (-1, 0, -\phi_x)$. Then $\tilde{\mathbf{X}}_s \times \tilde{\mathbf{X}}_y = (\phi_x, \phi_y, -1)$ points downward automatically.
> 3. **Negate the normal:** compute $\mathbf{X}_x \times \mathbf{X}_y$ and flip the sign.
>
> All three have the same underlying cause: reflecting one coordinate in the parameter domain has determinant $-1$, which reverses orientation. The general principle across all dimensions: *the upper boundary (in the FTC variable) is oriented positively, the lower boundary negatively*.

^rem-18-7

> [!remark] Remark: What Makes the Decomposition Work: Simple Solid Regions
> Step 1 of the proof ([[Multivariable Analysis §18 Surface Integrals#^pf-18-2|Theorem §18.2]]) assumed $V$ can be written as a region between two graphs $z = \phi(x,y)$ and $z = \psi(x,y)$. What does this require geometrically?
>
> **The condition:** Every vertical line (parallel to the $z$-axis) that passes through $V$ must enter exactly once and exit exactly once. That is, for each $(x,y)$ in the projection $D$, the slice $\{z : (x,y,z) \in V\}$ is a *single interval* $[\phi(x,y), \psi(x,y)]$.
>
> If a vertical line enters, exits, re-enters, and re-exits $V$, the boundary is not two graphs but four (or more), and the simple FTC argument breaks.
>
> For the full proof, we need this condition *in all three coordinate directions simultaneously*: every line parallel to the $z$-axis meets $V$ in a single interval (for the $c$-component), every line parallel to the $x$-axis meets $V$ in a single interval (for the $a$-component), and similarly for $y$. A domain satisfying all three is called a **simple (or elementary) solid region**.
>
> **Examples:**
> - Convex domains (balls, ellipsoids, tetrahedra) are automatically simple.
> - Many non-convex domains are also simple: a hemisphere, a solid cone, any region bounded above and below by graphs.
> - A solid torus is *not* simple (a vertical line can enter and exit twice), but it can be cut into finitely many simple pieces.
>
> **General domains:** If $V$ is not simple, we **decompose** $V$ into finitely many simple solid regions $V_1, \ldots, V_N$ with disjoint interiors. Apply the theorem on each $V_k$ and sum. The boundary integrals on the *internal cuts* (where $V_k$ meets $V_{k+1}$) cancel in pairs: the two sides of a cut have opposite outward normals, so their contributions are equal and opposite.
>
> This is the same cancellation mechanism as in the 2D case ([[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-1|Section 16, Green's theorem]]), and parallel to how we handled general regions for Fubini's theorem in [[Multivariable Analysis §15 Multivariable Integration|Section 15]]: there we needed Type I / Type II regions ([[Multivariable Analysis §15 Multivariable Integration#^def-15-12|Def. §15.12]]) for iterated integrals and subdivided general [[Multivariable Analysis §15 Multivariable Integration#^def-15-14|Jordan measurable]] domains. Same idea, one dimension up.

^rem-18-8

> [!remark] Remark: Green's Identities Revisited
> With the 3D Divergence Theorem now proved, the Green's identities from [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities|Section 17]] follow immediately for domains in $\mathbb{R}^3$ (not just $\mathbb{R}^n$ abstractly):
> - **Green's first identity:** choose $\mathbf{u} = u \, \nabla v$ in the 3D Divergence Theorem. The proof is exactly the same computation as in [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|Theorem §17.2]] — divergence of $u \nabla v$ gives $\nabla u \cdot \nabla v + u \, \Delta v$, and the boundary term gives $u \, \partial v / \partial n$.
> - **Green's second identity:** apply the first identity twice and subtract, as in [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Theorem §17.3]].
>
> The point is that once you have the Divergence Theorem, Green's identities are *not separate theorems* — they are corollaries obtained by choosing $\mathbf{u}$ strategically.

^rem-18-9
