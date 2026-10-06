---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 6
section: "18a"
tags: [multivariable-analysis, math452]
---
← [[§18 Surface Integrals]] · ↑ [[· 6 Surface Integrals and the Classical Theorems]] · [[§19 The Laplacian in Spherical Coordinates]] →

## The Vector Surface Integral (Flux)

Just as the Type II line integral $\oint \mathbf{F} \cdot d\mathbf{r}$ ([[§16 Line Integrals and Green's Theorem#^def-16-2|Def. §16.2]]) measures the work done by a vector field along a curve, the **flux integral** measures how much of a vector field passes *through* a surface.

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
> - In the language of forms, the flux integral is the integral of a 2-form: [[§22 The Algebra of Differential Forms#^def-22-6|Integration of a 2-Form over a Surface]], [[§22 The Algebra of Differential Forms#^rem-22-7|2-Form Integration Recovers the Flux Integral]].
> - The cross product $\mathbf{X}_u \times \mathbf{X}_v$ is a pullback: [[§22 The Algebra of Differential Forms#^rem-22-3|The Cross Product Is the Pullback in Disguise]].
> - Computational version: [[§113 Surface Integrals#^def-113-7|Calc Def. §113.7]] and [[§113 Surface Integrals#^thm-113-3|Calc Thm. §113.3]] (with worked examples).

**Interpretation:** $\iint_S \mathbf{F} \cdot d\mathbf{S}$ measures the net rate at which “stuff” (fluid, electric field, etc.) flows through $S$ in the direction of $\hat{n}$.

**Comparison with line integrals:**

| | **Curve** $\gamma$ | **Surface** $S$ |
|---|:---:|:---:|
| Scalar integral | $\int_\gamma f \, ds$ (Type I) | $\iint_S f \, dS$ |
| Vector integral | $\int_\gamma \mathbf{F} \cdot d\mathbf{r}$ (work) | $\iint_S \mathbf{F} \cdot d\mathbf{S}$ (flux) |
| Key vector | tangent $\boldsymbol{\gamma}'$ | normal $\mathbf{X}_u \times \mathbf{X}_v$ |

Note the geometric duality: the line integral uses the *tangent* vector (measuring the component of $\mathbf{F}$ *along* the curve), while the surface integral uses the *normal* vector (measuring the component of $\mathbf{F}$ *through* the surface).

> [!remark] Remark: Connection to the Divergence Theorem and Stokes' Theorem
> The flux integral is exactly the left-hand side of the **Divergence Theorem** ([[Divergence Theorem in ℝ³|Theorem §18.2]]):
>
> $$
> \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F} \, dV,
> $$
>
> which relates the flux through a closed surface $\partial V$ to the total divergence inside the enclosed volume $V$.
>
> Similarly, **Stokes' theorem** ([[Stokes' Theorem in ℝ³|Theorem §20.1]]) relates a line integral around $\partial S$ to a flux integral of the curl through $S$:
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
> \iint_S \mathbf{u} \cdot \hat{n} \, dS = \iint_S \big[ a \cdot n_1 + b \cdot n_2 + c \cdot n_3 \big] \, dS.
> $$
>
> For each component, we parametrize the surface by the “best choice” of two coordinates: the top/bottom surfaces use $(x,y)$, the left/right surfaces use $(y,z)$, and the front/back surfaces use $(x,z)$. This is exactly how the proof of the Divergence Theorem ([[Divergence Theorem in ℝ³|Theorem §18.2]]) proceeds.

^rem-18-6

## The Divergence Theorem in $\mathbb{R}^3$: Proof

### Orientation Convention for Closed Surfaces

For a closed surface $\partial V$ bounding a volume $V$:
- The **positive orientation** is defined by the **outward normal**: $\hat{n}$ points out of $V$.
- Equivalently: at each point $\mathbf{p} \in \partial V$, $\hat{n}$ is the unit normal with $\mathbf{p} + t\hat{n} \notin V$ and $\mathbf{p} - t\hat{n} \in V$ for small $t > 0$. For a parametrization $\mathbf{X}(u, v)$ of a piece of $\partial V$, this means $\mathbf{X}_u \times \mathbf{X}_v$ points out of $V$.
- A proper parametrization of $\partial V$ should yield a continuous outward-pointing normal field.

> [!theorem] Theorem §18.2: Divergence Theorem in $\mathbb{R}^3$
> Let $V \subseteq \mathbb{R}^3$ be a bounded region with piecewise smooth boundary $\partial V$, oriented with outward normal. If $\mathbf{u} = (a, b, c)$ is $C^1$ on an open set containing $\overline{V}$, then:
>
> $$
> \boxed{\iint_{\partial V} \mathbf{u} \cdot \hat{n} \, dS = \iiint_V \nabla \cdot \mathbf{u} \, dV = \iiint_V \left( \frac{\partial a}{\partial x} + \frac{\partial b}{\partial y} + \frac{\partial c}{\partial z} \right) dV}
> $$

^thm-18-2

![[m452-18-4.svg]]
*The setup of the proof for the $z$-component: $V$ lies between $S_{\text{bot}}\colon z = \phi(x,y)$ (blue) and $S_{\text{top}}\colon z = \psi(x,y)$ (red) over $D$, with vertical walls $S_{\text{side}}$. Along the dashed vertical segment above $(x,y)$, the FTC in $z$ gives $\int_\phi^\psi c_z\,dz = c(x,y,\psi) - c(x,y,\phi)$ (Step 2). On the boundary, $\mathbf{X}_x \times \mathbf{X}_y = (-\psi_x,-\psi_y,1)$ points up and out on the top, the outward normal on the bottom points down (hence $\mathbf{X}_y \times \mathbf{X}_x$ and $n_3\,dS = -dx\,dy$), and the walls have horizontal normals, $n_3 = 0$ (Step 3).*

> [!proof]+ Proof
> By linearity ([[§15 Multivariable Integration#^thm-15-3|Theorem §15.3]]), it suffices to prove the identity for each component separately:
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

*Uses:* [[§15 Multivariable Integration#^thm-15-3|§15.3]], [[§15 Multivariable Integration#^thm-15-9|§15.9]], [[Fundamental Theorem of Calculus|451 §34.1]], [[§18 Surface Integrals#^def-18-6|Def. §18.6]], [[§18 Surface Integrals#^def-18-5|Def. §18.5]], [[§18 Surface Integrals#^def-18-2|Def. §18.2]]

![[m452-18-2.svg]]
*The divergence theorem: $\iint_{\partial V}\mathbf{u}\cdot\hat{n}\,dS = \iiint_V \nabla\cdot\mathbf{u}\,dV$. Everything the sources inside $V$ produce (red: pointwise divergence, the microscopic outflux of [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]]) must exit through the boundary (green arrows crossing $\partial V$ along the outward normal $\hat n$). The proof is again the cancellation of [[§16 Line Integrals and Green's Theorem|§16]], one dimension up: tile $V$ into small cells; flux through every interior face cancels between neighbors, and only the outer boundary flux survives.*

> [!remark]- Connections
> - The 2D version: [[§16 Line Integrals and Green's Theorem#^thm-16-2|Divergence Theorem in ℝ²]]; the $n$-dimensional version: [[Divergence Theorem in ℝⁿ|Divergence Theorem in ℝⁿ]].
> - The 1D case is the [[Fundamental Theorem of Calculus]]; all are instances of the [[Generalized Stokes' Theorem|Generalized Stokes' Theorem]] with $d$ on 2-forms giving the divergence ([[§22 The Algebra of Differential Forms#^prop-22-4|Prop. §22.4]]).
> - Computational version: [[§115 The Divergence Theorem#^thm-115-1|Calc Thm. §115.1]] (with worked examples).
> - Used in PDEs: the local heat balance and the three-dimensional heat equation, [[§42 Three-Dimensional Heat Equation#^thm-42-2|341 Thm. §42.2]] and [[§42 Three-Dimensional Heat Equation#^thm-42-3|341 Thm. §42.3]].

> [!remark] Remark: Why the Bottom Surface Has Reversed Orientation
> The parameter reversal for the bottom surface is not a trick — it is the higher-dimensional manifestation of the sign pattern in the [[Fundamental Theorem of Calculus]].
>
> **1D:** $\int_a^b f'(x)\,dx = f(b) - f(a)$. The “boundary” of $[a,b]$ is two points. The outward normal at $b$ is $+1$ (pointing right, away from the interval), at $a$ is $-1$ (pointing left). Upper endpoint gets $+$, lower gets $-$.
>
> **2D ([[Green's Theorem|Green's theorem]]):** The boundary $\gamma$ of $D$ is traversed counterclockwise. The bottom edge $y = \phi(x)$ is traversed left-to-right ($x: a \to b$), but the top edge $y = \psi(x)$ is traversed right-to-left ($x: b \to a$) — because we go *around* the boundary, not across it. This reversed traversal produces the sign.
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
> Step 1 of the proof ([[§18 Surface Integrals#^pf-18-2|Theorem §18.2]]) assumed $V$ can be written as a region between two graphs $z = \phi(x,y)$ and $z = \psi(x,y)$. What does this require geometrically?
>
> **The condition:** Every vertical line (parallel to the $z$-axis) that passes through $V$ must enter exactly once and exit exactly once. That is, for each $(x,y)$ in the projection $D$, the slice $\{z : (x,y,z) \in V\}$ is a *single interval* $[\phi(x,y), \psi(x,y)]$.
>
> If a vertical line enters, exits, re-enters, and re-exits $V$, the boundary is not two graphs but four (or more), and the simple FTC argument breaks.
>
> For the full proof, we need this condition *in all three coordinate directions simultaneously*: every line parallel to the $z$-axis meets $V$ in a single interval (for the $c$-component), every line parallel to the $x$-axis meets $V$ in a single interval (for the $a$-component), and similarly for $y$. A domain satisfying all three is called a **simple (or elementary) solid region**.
>
> **Examples:**
> - Convex domains (balls, ellipsoids, tetrahedra, a solid hemisphere, a solid cone) are automatically simple.
> - Simplicity is weaker than convexity: the L-shaped block $\big([0,2]\times[0,1] \,\cup\, [0,1]\times[0,2]\big) \times [0,1]$ is not convex, yet every line parallel to a coordinate axis meets it in a single interval. A region bounded above and below by graphs satisfies the condition in the $z$-direction; the $x$- and $y$-directions must be checked separately.
> - A solid torus is *not* simple (a vertical line can enter and exit twice), but it can be cut into finitely many simple pieces.
>
> **General domains:** If $V$ is not simple, we **decompose** $V$ into finitely many simple solid regions $V_1, \ldots, V_N$ with disjoint interiors. Apply the theorem on each $V_k$ and sum. The boundary integrals on the *internal cuts* (where $V_k$ meets $V_{k+1}$) cancel in pairs: the two sides of a cut have opposite outward normals, so their contributions are equal and opposite.
>
> This is the same cancellation mechanism as in the 2D case ([[Green's Theorem|Section 16, Green's theorem]]), and parallel to how we handled general regions for [[Fubini's Theorem|Fubini's theorem]] in [[§15c Fubini's Theorem|§15c]]: there we needed Type I / Type II regions ([[§15 Multivariable Integration#^def-15-12|Def. §15.12]]) for iterated integrals and subdivided general [[§15 Multivariable Integration#^def-15-14|Jordan measurable]] domains. Same idea, one dimension up.

^rem-18-8

> [!remark] Remark: Green's Identities Revisited
> With the 3D Divergence Theorem now proved, the Green's identities from [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities|Section 17]] follow immediately for domains in $\mathbb{R}^3$ (not just $\mathbb{R}^n$ abstractly):
> - **Green's first identity:** choose $\mathbf{u} = u \, \nabla v$ in the 3D Divergence Theorem. The proof is exactly the same computation as in [[Green's First Identity|Theorem §17.2]] — divergence of $u \nabla v$ gives $\nabla u \cdot \nabla v + u \, \Delta v$, and the boundary term gives $u \, \partial v / \partial n$.
> - **Green's second identity:** apply the first identity twice and subtract, as in [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Theorem §17.3]].
>
> The point is that once you have the Divergence Theorem, Green's identities are *not separate theorems* — they are corollaries obtained by choosing $\mathbf{u}$ strategically.

^rem-18-9
