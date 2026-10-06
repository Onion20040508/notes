---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 6
section: 31
tags: [multivariable-analysis, math452]
---
← [[§30 Radial Functions]] · ↑ [[· 6 Surface Integrals and the Classical Theorems]] · [[§32 Flux Integrals and the Divergence Theorem in ℝ³]] →

> [!remark] Note: Smoothness Assumptions for This Section
> The results in this section require increasingly strong conditions on the parametrization $\mathbf{X}$, the surface $S$, and the vector field $\mathbf{F}$. Here is the hierarchy, from weakest to strongest:
>
> 1. **Tangent vectors exist:** $\mathbf{X}: D \to \mathbb{R}^3$ is $C^1$ (i.e., all partial derivatives $x_u, x_v, y_u, y_v, z_u, z_v$ exist and are continuous). This ensures the tangent vectors $\mathbf{X}_u, \mathbf{X}_v$ are well-defined and vary continuously.
> 2. **The parametrization describes a surface (regularity):** $\mathbf{X}$ is $C^1$ *and* the Jacobian $D\mathbf{X}$ ([[§7 Differentiability#^def-7-3|Def. §7.3]]) has rank 2 everywhere, i.e., $\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$. This ensures a well-defined tangent plane at every point, and in particular ensures $|\mathbf{X}_u \times \mathbf{X}_v| > 0$ so the area element $dS$ is nondegenerate.
> 3. **The parametrization is injective** (on the interior of $D$): distinct parameter values give distinct surface points, so the surface does not self-intersect. Without this, the “surface area” might count some regions of $S$ multiple times.
> 4. **Orientability:** A continuous choice of unit normal $\hat{n}$ exists on all of $S$. This is needed for flux integrals (otherwise the sign of $\mathbf{F} \cdot \hat{n}$ is ambiguous). A regular parametrization automatically provides an orientation via $\hat{n} = (\mathbf{X}_u \times \mathbf{X}_v) / |\mathbf{X}_u \times \mathbf{X}_v|$; the question is whether different parametrizations of the same surface give consistent normals. (The Möbius strip is the classical example of a non-orientable surface.)
> 5. **For the integral theorems** (Divergence, Stokes): the boundary $\partial V$ or $\partial S$ must be **piecewise smooth** (finitely many smooth pieces joined along curves or edges), and the vector field $\mathbf{F}$ must be $C^1$ on an open set containing $\overline{V}$ (or $\overline{S}$). The piecewise smoothness allows us to decompose into pieces on which the proof works, and the $C^1$ condition on $\mathbf{F}$ ensures the divergence $\nabla \cdot \mathbf{F}$ ([[§27 Line Integrals and Green's Theorem#^def-27-5|Def. §27.5]]) (or curl $\nabla \times \mathbf{F}$, [[§27 Line Integrals and Green's Theorem#^def-27-6|Def. §27.6]]) exists and is continuous.
>
> **Standing assumption for this section:** Unless stated otherwise, all parametrizations are $C^1$, injective on the interior of $D$, and regular. All surfaces are oriented. All vector fields are $C^1$.

^rem-31-1

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

> [!definition] Definition §31.1: Parametrized Surface
> A **parametrized surface** in $\mathbb{R}^3$ is a $C^1$ map $\mathbf{X}: D \to \mathbb{R}^3$, where $D \subseteq \mathbb{R}^2$ is a domain, given by
>
> $$
> \mathbf{X}(u, v) = \big( x(u,v), \, y(u,v), \, z(u,v) \big).
> $$
>
> The image $S = \mathbf{X}(D) \subseteq \mathbb{R}^3$ is the **surface**, and $(u,v)$ are its **parameters** (coordinates on $S$).

^def-31-1

> [!remark]- Connections
> - Computational version: [[§133 Parametric Surfaces and Their Areas#^def-133-1|Calc Def. §133.1]] (with worked examples).

> [!example] Example §31.1: Sphere
> The sphere of radius $R$, $\{(x,y,z) : x^2 + y^2 + z^2 = R^2\}$, is a set of points in $\mathbb{R}^3$. To parametrize it, we use spherical angles $(\theta, \varphi)$:
>
> $$
> \mathbf{X}(\theta, \varphi) = (R\cos\varphi\cos\theta, \; R\cos\varphi\sin\theta, \; R\sin\varphi),
> $$
>
> with $\theta \in [0, 2\pi)$ and $\varphi \in (-\pi/2, \pi/2)$.
>
> Here $\mathbf{X}(\theta, \varphi)$ tells you: “the point on the sphere at longitude $\theta$ and latitude $\varphi$ has Cartesian coordinates $(R\cos\varphi\cos\theta, R\cos\varphi\sin\theta, R\sin\varphi)$.”

^ex-31-1

![[m452-18-3.svg]]
*Example §18.1 on the sphere of radius $R$: the point $\mathbf{X}(\theta,\varphi)$ has longitude $\theta$ (measured in the $xy$-plane from the $x$-axis) and latitude $\varphi$ (measured up from the equator). Through it pass the latitude circle $\varphi = \text{const}$ (a $\theta$-curve) and the meridian $\theta = \text{const}$ (a $\varphi$-curve), whose tangents are $\mathbf{X}_\theta$ and $\mathbf{X}_\varphi$ (red), with lengths $R\cos\varphi$ and $R$. Their cross product has length $R^2\cos\varphi$ — the area factor of Example §31.2. At the poles the latitude circles shrink to a point, so $\mathbf{X}_\theta = \mathbf{0}$: the irregular points of [[§31 Surface Integrals#^rem-31-3|Regularity as a Rank Condition on the Derivative]], a defect of the coordinates, not of the sphere.*

> [!remark] Remark: Dimension Count
> A 1D object (curve) in 1D space cannot curve — it fills the whole space. A 1D object in 2D space *can* curve. Similarly, a surface is a 2D object that can curve only when it lives in 3D (or higher) space. The parametrization $\mathbf{X}: \mathbb{R}^2 \to \mathbb{R}^3$ maps a flat 2D domain into 3D, and the image can be curved.

^rem-31-2

## Tangent Vectors and Regularity

Fix a point $(u_0, v_0) \in D$. The two families of curves through this point give two tangent directions:
- The **$u$-curve** $u \mapsto \mathbf{X}(u, v_0)$ (fix $v$, vary $u$) has tangent vector $\mathbf{X}_u$.
- The **$v$-curve** $v \mapsto \mathbf{X}(u_0, v)$ (fix $u$, vary $v$) has tangent vector $\mathbf{X}_v$.

These are exactly the tangent vectors to the two families of curves that sweep out the surface.

> [!definition] Definition §31.2: Tangent Vectors
> The **tangent vectors** to the surface at $(u_0, v_0)$ are:
>
> $$
> \mathbf{X}_u = \left( \frac{\partial x}{\partial u}, \, \frac{\partial y}{\partial u}, \, \frac{\partial z}{\partial u} \right), \qquad \mathbf{X}_v = \left( \frac{\partial x}{\partial v}, \, \frac{\partial y}{\partial v}, \, \frac{\partial z}{\partial v} \right).
> $$

^def-31-2

![[m452-18-1.svg]]
*The surface integral is computed cell by cell: a grid cell $\Delta u \times \Delta v$ in the parameter domain (red, left) is carried by $\mathbf{X}$ to a curved patch on the surface (red, right). Zoomed to this scale, the patch is approximated by the tangent parallelogram (green) spanned by $\mathbf{X}_u\Delta u$ and $\mathbf{X}_v\Delta v$, with area $|\mathbf{X}_u \times \mathbf{X}_v|\,\Delta u\,\Delta v$. Summing over all cells and refining gives $\iint_S dS = \iint_D |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$: the cross product length is the area-scaling factor, playing exactly the role $|J|$ played in [[§24 The Change of Variables Formula|§24]] — and $|\mathbf{r}'|$ in [[§27 Line Integrals and Green's Theorem|§27]].*

> [!remark]- Connections
> - The tangent space as the image of the derivative of a parametrization is one of three equal descriptions in [[§23 The Geometric Tangent Space#^cor-23-4|591 Cor. §23.4]] (velocities of curves, kernel of the constraint Jacobian, image of the parametrization's derivative).

> [!definition] Definition §31.3: Regular Point
> The surface is **regular** at $(u_0, v_0)$ if $\mathbf{X}_u$ and $\mathbf{X}_v$ are [[§4 Span and Linear Independence#^ladr-2-15|linearly independent]] at that point, i.e., $\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$.
>
> A surface is **regular** if it is regular at every point of $D$.

^def-31-3

**Geometric meaning:** At a regular point, the $u$-curves and $v$-curves cross transversally, spanning a 2D tangent plane. If $\mathbf{X}_u$ and $\mathbf{X}_v$ are parallel (or one is zero), the two families of curves are tangent to each other — they fail to sweep out a genuine 2D surface at that point, and the parametrization degenerates.

> [!remark] Remark: Regularity as a Rank Condition on the Derivative
> The regularity condition is best understood through the differentiability framework of [[§7 Differentiability|§7]], applied to $\mathbf{X}: \mathbb{R}^2 \to \mathbb{R}^3$.
>
> **The derivative of $\mathbf{X}$.** Differentiability of $\mathbf{X}$ at $(u_0, v_0)$ ([[§7 Differentiability#^def-7-1|Def. §7.1]]) means:
>
> $$
> \mathbf{X}(u_0 + h, v_0 + k) = \mathbf{X}(u_0, v_0) + D\mathbf{X} \begin{pmatrix} h \\ k \end{pmatrix} + o\!\left(\sqrt{h^2 + k^2}\right)
> $$
>
> where $D\mathbf{X}$ is the $3 \times 2$ Jacobian matrix ([[§7 Differentiability#^def-7-3|Def. §7.3]]) whose columns are $\mathbf{X}_u$ and $\mathbf{X}_v$:
>
> $$
> D\mathbf{X} = \begin{pmatrix} x_u & x_v \\ y_u & y_v \\ z_u & z_v \end{pmatrix}.
> $$
>
> The image of $D\mathbf{X}$ — the set of all vectors $h \mathbf{X}_u + k \mathbf{X}_v$ — is the **tangent space**. Its dimension equals $\operatorname{rank}(D\mathbf{X})$ ([[§9 Matrices#^ladr-3-58|LADR 3.58]]):
> - **Rank 2** ($\mathbf{X}_u, \mathbf{X}_v$ independent, i.e., regular): the image of $D\mathbf{X}$ is a 2D plane. The linear approximation faithfully represents a 2D surface. This is the good case.
> - **Rank 1** ($\mathbf{X}_u, \mathbf{X}_v$ parallel): the image is a line. The derivative compresses two dimensions into one — the parametrization “folds” the $(u,v)$-plane onto a curve at that point.
> - **Rank 0** ($\mathbf{X}_u = \mathbf{X}_v = \mathbf{0}$): the image is a point. The derivative gives zero information about the surface.
>
> So the surface is differentiable in all three cases (the linear approximation exists), but **regularity ensures the approximation is full-dimensional** — that it is actually approximating a *surface* and not a lower-dimensional object.
>
> **Parallel to earlier results.** This is the same idea as the change of variables theorem and the IFT:
> - In the **change of variables** ([[§24 The Change of Variables Formula|§24]]), $J \neq 0$ means the $2 \times 2$ Jacobian has rank 2, ensuring the map is locally invertible.
> - In the **IFT/Inverse FT** (Sections [[§15 The Implicit Function Theorem|§15]]–[[§16 The Inverse Function Theorem|§16]]), the nonvanishing determinant ensures the derivative has full rank.
> - Here, $\mathbf{X}_u \times \mathbf{X}_v \neq \mathbf{0}$ means the $3 \times 2$ Jacobian has rank 2, ensuring the parametrization is locally injective (an **immersion**) — it does not collapse any direction.
>
> This also explains why $\det(G) = |\mathbf{X}_u \times \mathbf{X}_v|^2$ appears in the area formula ([[Surface Area via the Gram Matrix|Theorem §31.1]]): it measures how much 2D area the derivative preserves. When $\det(G) = 0$, the derivative crushes some 2D area to zero — exactly the degenerate case.
>
> **Irregular point $\neq$ singular surface.** An irregular point can mean two different things:
> - **Bad parametrization, smooth surface.** The sphere parametrized by $(\theta, \varphi)$ ([[§31 Surface Integrals#^ex-31-1|Example §31.1]]) has $\mathbf{X}_\theta = \mathbf{0}$ at the poles ($\varphi = \pm \pi/2$), because all values of $\theta$ map to the same point. The sphere is perfectly smooth there; the coordinate system degenerates. A different parametrization (e.g., centered at the pole) would be regular.
> - **Genuinely singular surface.** The cone $\mathbf{X}(u,v) = (v\cos u, v\sin u, v)$ has $\mathbf{X}_u = \mathbf{0}$ at the tip $v = 0$. No reparametrization can fix this — the cone tip has no well-defined tangent plane; it is not a smooth 2D surface.
>
> Distinguishing these cases requires checking whether the singularity persists under all possible reparametrizations — a question taken up systematically in differential geometry (MATH 591).

^rem-31-3

> [!remark]- Connections
> - A parametrization that is regular at every point is an immersion, [[§35 Immersions#^def-35-1|591 Def. §35.1]], and one that is also a homeomorphism onto its image is the internal description of a manifold, [[§19 Manifolds in Euclidean Space#^def-19-1|591 Def. §19.1]].

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

But we want a formula for area that works in *any* ambient dimension (not just $\mathbb{R}^3$), where the cross product is not defined. We need a formula that uses only **dot products** ([[§20 Inner Products and Norms#^ladr-6-1|LADR 6.1]]).

### The Gram Matrix (First Fundamental Form)

> [!definition] Definition §31.4: Gram Matrix
> The **Gram matrix** (or **first fundamental form**) of the parametrized surface is the $2 \times 2$ matrix:
>
> $$
> G = \begin{pmatrix} \mathbf{X}_u \cdot \mathbf{X}_u & \mathbf{X}_u \cdot \mathbf{X}_v \\ \mathbf{X}_v \cdot \mathbf{X}_u & \mathbf{X}_v \cdot \mathbf{X}_v \end{pmatrix} = \begin{pmatrix} E & F \\ F & \tilde{G} \end{pmatrix}
> $$
>
> where the classical notation is $E = |\mathbf{X}_u|^2$, $F = \mathbf{X}_u \cdot \mathbf{X}_v$, $\tilde{G} = |\mathbf{X}_v|^2$ (classically also called $G$; we write $\tilde{G}$ to avoid a clash with the matrix $G$).

^def-31-4

> [!theorem] Theorem §31.1: Surface Area via the Gram Matrix
> The surface area element is:
>
> $$
> \boxed{dS = \sqrt{\det(G)} \, du \, dv = \sqrt{E\tilde{G} - F^2} \, du \, dv}
> $$
>
> In $\mathbb{R}^3$, this equals $|\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv$.

^thm-31-1

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
> **Expand the square** $(x_u x_v + y_u y_v + z_u z_v)^2$: its 9 terms combine into 6:
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

^pf-31-1

*Uses:* [[§31 Surface Integrals#^def-31-2|Def. §31.2]], [[§31 Surface Integrals#^def-31-4|Def. §31.4]], [[§20 Inner Products and Norms#^ladr-6-1|LADR 6.1]]

> [!remark]- Connections
> - The linear algebra behind it: $G = (D\mathbf{X})^{T} D\mathbf{X}$ is $T^*T$ for $T = D\mathbf{X}$, so $\operatorname{rank} G = \operatorname{rank} D\mathbf{X}$ ([[§27 Singular Value Decomposition#^ladr-7-64|LADR 7.64]]) and $\det G > 0$ exactly at regular points ([[§31 Surface Integrals#^def-31-3|Def. §31.3]]).
> - When $D\mathbf{X}$ is square, $\sqrt{\det(T^*T)} = |\det T|$ ([[§37 Determinants#^ladr-9-60|LADR 9.60]], [[§37 Determinants#^ladr-9-61|LADR 9.61]]): the $|J|$ of [[§25 Change of Variables on General Domains#^thm-25-6|Change of Variables in ℝⁿ]].
> - The same area element pulled back as a 2-form: [[§37 The Algebra of Differential Forms#^ex-37-3|Pullback Along a Surface]].
> - Computational version: [[§133 Parametric Surfaces and Their Areas#^def-133-6|Calc Def. §133.6]] ($dS = |\mathbf r_u \times \mathbf r_v|\,du\,dv$, with worked examples); for graphs [[§119 Surface Area#^thm-119-1|Calc Thm. §119.1]], for surfaces of revolution [[§61 Area of a Surface of Revolution#^def-61-2|Calc Def. §61.2]].

> [!remark] Remark: Why the Gram Matrix?
> In $\mathbb{R}^3$, we could just use $|\mathbf{X}_u \times \mathbf{X}_v|$ directly. The Gram matrix formulation is preferred because:
> - It works in **any ambient dimension**: for a 2D surface in $\mathbb{R}^n$ ($n > 3$), the cross product is not defined, but the Gram matrix $G = (\mathbf{X}_u \cdot \mathbf{X}_v)$ always makes sense, and $\sqrt{\det(G)}$ always gives the correct area element.
> - It is the starting point of **Riemannian geometry**: the Gram matrix is the metric tensor of the surface, encoding intrinsic distances and angles.

^rem-31-4

## The Scalar Surface Integral

With the area element $dS = |\mathbf{X}_u \times \mathbf{X}_v| \, du \, dv$ in hand, we can integrate scalar functions over surfaces. The logic is identical to the scalar line integral ([[§27 Line Integrals and Green's Theorem#^def-27-1|Def. §27.1]]): weight each infinitesimal piece of the surface by the value of $f$ at that point.

> [!definition] Definition §31.5: Scalar Surface Integral
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

^def-31-5

> [!remark]- Connections
> - One dimension down: the [[§27 Line Integrals and Green's Theorem#^def-27-1|Scalar Line Integral]].
> - Not an integral of a differential form (no orientation): [[§38 The Exterior Derivative#^rem-38-8|Scalar Integrals Are Not Form Integrals]].
> - Computational version: [[§134 Surface Integrals#^def-134-1|Calc Def. §134.1]] and [[§134 Surface Integrals#^thm-134-1|Calc Thm. §134.1]] (with worked examples).

**Interpretation:** If $f$ represents mass density (mass per unit area), then $\iint_S f \, dS$ is the total mass of a thin shell shaped like $S$.

**Comparison with line integrals:**

| | **Curve** $\gamma$ | **Surface** $S$ |
|---|:---:|:---:|
| Parametrization | $\boldsymbol{\gamma}(t)$, $t \in [a,b]$ | $\mathbf{X}(u,v)$, $(u,v) \in D$ |
| Length / Area element | $ds = \vert\boldsymbol{\gamma}'(t)\vert \, dt$ | $dS = \vert\mathbf{X}_u \times \mathbf{X}_v\vert \, du \, dv$ |
| Scalar integral | $\int_\gamma f \, ds$ | $\iint_S f \, dS$ |

> [!example] Example §31.2: Surface Area of a Sphere
> Parametrize the sphere of radius $R$ by $\mathbf{X}(\theta, \varphi) = (R\cos\varphi\cos\theta, R\cos\varphi\sin\theta, R\sin\varphi)$ with $\theta \in [0, 2\pi)$, $\varphi \in (-\pi/2, \pi/2)$ ([[§31 Surface Integrals#^ex-31-1|Example §31.1]]).
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
> Surface area ([[§31 Surface Integrals#^def-31-5|Def. §31.5]]):
>
> $$
> \text{Area}(S^2) = \int_0^{2\pi} \int_{-\pi/2}^{\pi/2} R^2 \cos\varphi \, d\varphi \, d\theta = R^2 \cdot 2\pi \cdot \big[\sin\varphi\big]_{-\pi/2}^{\pi/2} = R^2 \cdot 2\pi \cdot 2 = \boxed{4\pi R^2}.
> $$

^ex-31-2

*Continued in [[§32 Flux Integrals and the Divergence Theorem in ℝ³]]: flux integrals, graph surfaces, and the proof of the Divergence Theorem in ℝ³.*
