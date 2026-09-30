---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 5
section: 17
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §16 Line Integrals and Green's Theorem]] · ↑ [[Multivariable Analysis — 5 Line Integrals and the Divergence Theorem]] · [[Multivariable Analysis §18 Surface Integrals]] →

In the [[Multivariable Analysis §16 Line Integrals and Green's Theorem|previous section]] we derived [[Green's Theorem|Green's theorem]] (2D) and its two vector reformulations: the [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-3|2D Stokes form]] (circulation = integral of curl) and the [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|2D Divergence form]] (flux = integral of divergence). We now extend the Divergence Theorem to $\mathbb{R}^n$ and derive the classical **Green's identities**, which are the key tools for studying the Laplacian.

## The Divergence Theorem in $\mathbb{R}^n$

> [!definition] Definition §17.1: Divergence in $\mathbb{R}^n$
> For a $C^1$ vector field $\mathbf{u} = (u_1, u_2, \ldots, u_n): D \to \mathbb{R}^n$, the **divergence** is the scalar field:
>
> $$
> \nabla \cdot \mathbf{u} = \sum_{i=1}^n \frac{\partial u_i}{\partial x_i} = \frac{\partial u_1}{\partial x_1} + \frac{\partial u_2}{\partial x_2} + \cdots + \frac{\partial u_n}{\partial x_n}.
> $$

^def-17-1

> [!theorem] Theorem §17.1: Divergence Theorem in $\mathbb{R}^n$
> Let $D \subseteq \mathbb{R}^n$ be a bounded domain with piecewise smooth boundary $\partial D$. If $\mathbf{u} = (u_1, \ldots, u_n)$ is $C^1$ on an open set containing $\overline{D}$, then:
>
> $$
> \boxed{\int_{\partial D} \mathbf{u} \cdot \hat{n} \, dS = \int_D \nabla \cdot \mathbf{u} \, dV}
> $$
>
> where $\hat{n}$ is the outward unit normal to $\partial D$, $dS$ is the surface area element on $\partial D$, and $dV = dx_1 \cdots dx_n$.

^thm-17-1

![[m452-17-1.svg]]
*The proof of the component identity for $k = n$, drawn for $n = 2$. The region $D$ sits over its projection $D'$ between the lower graph $S_{\text{bot}}\colon x_n = \alpha(\mathbf{x}')$ (blue) and the upper graph $S_{\text{top}}\colon x_n = \beta(\mathbf{x}')$ (red). Inside: along each vertical fiber the FTC turns $\int_\alpha^\beta \partial_n u_n\,dx_n$ into $u_n(\mathbf{x}',\beta) - u_n(\mathbf{x}',\alpha)$ (Step 2). On the boundary: a patch $dS$ of $S_{\text{top}}$ projects onto $d\mathbf{x}'$, and $n_n\,dS = d\mathbf{x}'$ exactly (the tilt that enlarges $dS$ shrinks $n_n$ by the same factor); on $S_{\text{bot}}$ the outward normal points down, giving $-d\mathbf{x}'$; on the vertical sides $n_n = 0$ (Step 3). Top minus bottom on both sides — that is the whole theorem.*

> [!proof]+ Proof
> By linearity, it suffices to prove the **component identity**:
>
> $$
> \int_{\partial D} u_k \, n_k \, dS = \int_D \frac{\partial u_k}{\partial x_k} \, dV \qquad \text{for each } k = 1, \ldots, n,
> $$
>
> since summing over $k$ gives:
>
> $$
> \sum_{k=1}^n \int_{\partial D} u_k \, n_k \, dS = \int_{\partial D} \left( \sum_{k=1}^n u_k \, n_k \right) dS = \int_{\partial D} \mathbf{u} \cdot \hat{n} \, dS
> $$
>
> and
>
> $$
> \sum_{k=1}^n \int_D \frac{\partial u_k}{\partial x_k} \, dV = \int_D \nabla \cdot \mathbf{u} \, dV.
> $$
>
> **Step 1: Set up.** Fix $k$. For simplicity of notation, we prove the case $k = n$ (the last coordinate); the argument for other $k$ is identical.
>
> Denote the “horizontal” variables by $\mathbf{x}' = (x_1, \ldots, x_{n-1})$ and the “vertical” variable by $x_n$. Assume $D$ can be written as:
>
> $$
> D = \{(\mathbf{x}', x_n) : \mathbf{x}' \in D', \;\; \alpha(\mathbf{x}') \leq x_n \leq \beta(\mathbf{x}')\}
> $$
>
> where $D' \subseteq \mathbb{R}^{n-1}$ is the projection of $D$ onto the first $n-1$ coordinates, and $\alpha, \beta: D' \to \mathbb{R}$ are $C^1$ functions describing the “lower” and “upper” boundary surfaces.
>
> (If $D$ cannot be globally represented this way, we subdivide $D$ into finitely many pieces for which the representation holds. The boundary integrals on the internal cuts cancel in pairs since the outward normals on opposite sides of a cut point in opposite directions.)
>
> **Step 2: Evaluate the volume integral using FTC.**
>
> By [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|Fubini's theorem]], we can write the volume integral as an iterated integral:
>
> $$
> \int_D \frac{\partial u_n}{\partial x_n} \, dV = \int_{D'} \left( \int_{\alpha(\mathbf{x}')}^{\beta(\mathbf{x}')} \frac{\partial u_n}{\partial x_n}(\mathbf{x}', x_n) \, dx_n \right) d\mathbf{x}'.
> $$
>
> By the [[Fundamental Theorem of Calculus]] applied to the inner integral:
>
> $$
> \int_{\alpha(\mathbf{x}')}^{\beta(\mathbf{x}')} \frac{\partial u_n}{\partial x_n} \, dx_n = u_n(\mathbf{x}', \beta(\mathbf{x}')) - u_n(\mathbf{x}', \alpha(\mathbf{x}')).
> $$
>
> Therefore:
>
> $$
> \int_D \frac{\partial u_n}{\partial x_n} \, dV = \int_{D'} \big[ u_n(\mathbf{x}', \beta(\mathbf{x}')) - u_n(\mathbf{x}', \alpha(\mathbf{x}')) \big] \, d\mathbf{x}'. \tag{$\dagger$}
> $$
>
> **Step 3: Evaluate the boundary integral.**
>
> The boundary $\partial D$ consists of three parts:
> - $S_{\text{top}}$: the upper surface $x_n = \beta(\mathbf{x}')$, parametrized by $\mathbf{x}' \in D'$.
> - $S_{\text{bot}}$: the lower surface $x_n = \alpha(\mathbf{x}')$, parametrized by $\mathbf{x}' \in D'$.
> - $S_{\text{side}}$: the lateral boundary (if any), on which $\hat{n}$ is perpendicular to $\hat{e}_n$, so $n_n = 0$.
>
> Since $n_n = 0$ on $S_{\text{side}}$, the lateral boundary contributes nothing to $\int_{\partial D} u_n \, n_n \, dS$.
>
> *Upper surface $S_{\text{top}}$:* The surface $x_n = \beta(\mathbf{x}')$ can be written as $F(\mathbf{x}', x_n) = x_n - \beta(\mathbf{x}') = 0$. The outward normal (pointing upward, out of $D$) is:
>
> $$
> \hat{n}_{\text{top}} = \frac{\nabla F}{|\nabla F|} = \frac{(-\partial_1 \beta, \ldots, -\partial_{n-1} \beta, 1)}{\sqrt{1 + |\nabla' \beta|^2}},
> $$
>
> where $\nabla' \beta = (\partial_1 \beta, \ldots, \partial_{n-1} \beta)$. The surface element is $dS = \sqrt{1 + |\nabla' \beta|^2} \, d\mathbf{x}'$.
>
> Therefore the $n$-th component of $\hat{n}$ times $dS$ is:
>
> $$
> n_n \, dS = \frac{1}{\sqrt{1 + |\nabla' \beta|^2}} \cdot \sqrt{1 + |\nabla' \beta|^2} \, d\mathbf{x}' = d\mathbf{x}'.
> $$
>
> The contribution from the upper surface is:
>
> $$
> \int_{S_{\text{top}}} u_n \, n_n \, dS = \int_{D'} u_n(\mathbf{x}', \beta(\mathbf{x}')) \, d\mathbf{x}'. \tag{$\dagger\dagger_1$}
> $$
>
> *Lower surface $S_{\text{bot}}$:* The outward normal now points *downward* (out of $D$), so:
>
> $$
> \hat{n}_{\text{bot}} = \frac{(\partial_1 \alpha, \ldots, \partial_{n-1} \alpha, -1)}{\sqrt{1 + |\nabla' \alpha|^2}}.
> $$
>
> The $n$-th component gives $n_n \, dS = -d\mathbf{x}'$. Therefore:
>
> $$
> \int_{S_{\text{bot}}} u_n \, n_n \, dS = -\int_{D'} u_n(\mathbf{x}', \alpha(\mathbf{x}')) \, d\mathbf{x}'. \tag{$\dagger\dagger_2$}
> $$
>
> **Step 4: Compare.**
>
> Combining $(\dagger\dagger_1)$ and $(\dagger\dagger_2)$:
>
> $$
> \int_{\partial D} u_n \, n_n \, dS = \int_{D'} u_n(\mathbf{x}', \beta(\mathbf{x}')) \, d\mathbf{x}' - \int_{D'} u_n(\mathbf{x}', \alpha(\mathbf{x}')) \, d\mathbf{x}' = \int_{D'} \big[ u_n(\mathbf{x}', \beta) - u_n(\mathbf{x}', \alpha) \big] \, d\mathbf{x}'.
> $$
>
> This is identical to $(\dagger)$. Therefore:
>
> $$
> \int_{\partial D} u_n \, n_n \, dS = \int_D \frac{\partial u_n}{\partial x_n} \, dV.
> $$
>
> Repeating the argument for each $k = 1, \ldots, n$ and summing yields the Divergence Theorem.

^pf-17-1

*Uses:* [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-1|Def. §17.1]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-3|§15.3]], [[Multivariable Analysis §15 Multivariable Integration#^thm-15-9|§15.9]], [[Fundamental Theorem of Calculus|451 §34.1]]

> [!remark]- Connections
> - $n = 1$ is the [[Fundamental Theorem of Calculus]]; $n = 2$ is [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|Theorem §16.2]]; the $\mathbb{R}^3$ version with parametrized surfaces is [[Divergence Theorem in ℝ³|Theorem §18.2]].
> - The same "FTC in one direction" proof, done for forms: [[Generalized Stokes' Theorem|Generalized Stokes' Theorem (§23.1)]].

## Green's Identities

The power of the Divergence Theorem lies in choosing $\mathbf{u}$ strategically. Green's identities arise from specific choices involving scalar functions and the Laplacian.

> [!definition] Definition §17.2: Gradient and Laplacian
> For a $C^2$ function $v: D \to \mathbb{R}$:
> - The **gradient** is $\nabla v = \left(\frac{\partial v}{\partial x_1}, \ldots, \frac{\partial v}{\partial x_n}\right)$.
> - The **Laplacian** is $\Delta v = \nabla \cdot (\nabla v) = \displaystyle\sum_{i=1}^n \frac{\partial^2 v}{\partial x_i^2}$.
> - The **normal derivative** on $\partial D$ is $\dfrac{\partial v}{\partial n} = \nabla v \cdot \hat{n} = \displaystyle\sum_{i=1}^n \frac{\partial v}{\partial x_i} \, n_i$.

^def-17-2

> [!remark]- Connections
> - The gradient was introduced in [[Multivariable Analysis §7 Directional Derivatives|§7]]; the normal derivative is the directional derivative ([[Directional Derivative Formula|Theorem §7.1]]) in the direction $\hat{n}$.

## Green's First Identity

> [!theorem] Theorem §17.2: Green's First Identity
> Let $D \subseteq \mathbb{R}^n$ be a bounded domain with piecewise smooth boundary. If $u \in C^1(\overline{D})$ and $v \in C^2(\overline{D})$, then:
>
> $$
> \boxed{\int_D \big( \nabla u \cdot \nabla v + u \, \Delta v \big) \, dV = \int_{\partial D} u \, \frac{\partial v}{\partial n} \, dS}
> $$
>
> Equivalently (rearranging):
>
> $$
> \int_D u \, \Delta v \, dV = \int_{\partial D} u \, \frac{\partial v}{\partial n} \, dS - \int_D \nabla u \cdot \nabla v \, dV.
> $$
>
> This is the **higher-dimensional integration by parts**: the “derivative” ($\Delta$) is transferred from $v$ to $u$ (as $\nabla u$), at the cost of a boundary term.

^thm-17-2

> [!proof]+ Proof
> Apply the Divergence Theorem ([[Divergence Theorem in ℝⁿ|Theorem §17.1]]) with the vector field $\mathbf{w} = u \, \nabla v$.
>
> **Step 1: Compute the divergence of $\mathbf{w}$.**
>
> The $i$-th component of $\mathbf{w}$ is $w_i = u \, \frac{\partial v}{\partial x_i}$. By the [[Multivariable Analysis §6 Differentiability#^thm-6-4|product rule]]:
>
> $$
> \frac{\partial w_i}{\partial x_i} = \frac{\partial u}{\partial x_i} \cdot \frac{\partial v}{\partial x_i} + u \cdot \frac{\partial^2 v}{\partial x_i^2}.
> $$
>
> Summing over $i$:
>
> $$
> \nabla \cdot \mathbf{w} = \sum_{i=1}^n \frac{\partial w_i}{\partial x_i} = \sum_{i=1}^n \frac{\partial u}{\partial x_i} \frac{\partial v}{\partial x_i} + u \sum_{i=1}^n \frac{\partial^2 v}{\partial x_i^2} = \nabla u \cdot \nabla v + u \, \Delta v.
> $$
>
> **Step 2: Compute the boundary term.**
>
> $$
> \mathbf{w} \cdot \hat{n} = (u \, \nabla v) \cdot \hat{n} = u \, (\nabla v \cdot \hat{n}) = u \, \frac{\partial v}{\partial n}.
> $$
>
> **Step 3: Apply the Divergence Theorem.**
>
> $$
> \int_{\partial D} u \, \frac{\partial v}{\partial n} \, dS = \int_{\partial D} \mathbf{w} \cdot \hat{n} \, dS = \int_D \nabla \cdot \mathbf{w} \, dV = \int_D \big( \nabla u \cdot \nabla v + u \, \Delta v \big) \, dV.
> $$

^pf-17-2

*Uses:* [[Divergence Theorem in ℝⁿ|§17.1]], [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|Def. §17.2]], [[Multivariable Analysis §6 Differentiability#^thm-6-4|§6.4]]

> [!remark]- Connections
> - For $n = 1$ this is ordinary [[Single Variable Analysis §34 Fundamental Theorem of Calculus#^thm-34-3|Integration by Parts (451 §34.3)]].
> - Revisited with surface integrals in $\mathbb{R}^3$: [[Multivariable Analysis §18 Surface Integrals#^rem-18-9|Green's Identities Revisited]].

> [!remark] Remark: Special Case: $u = v$
> Setting $u = v$ in Green's first identity:
>
> $$
> \int_D \big( |\nabla v|^2 + v \, \Delta v \big) \, dV = \int_{\partial D} v \, \frac{\partial v}{\partial n} \, dS.
> $$
>
> If in addition $v$ is **harmonic** ($\Delta v = 0$) and $v = 0$ on $\partial D$, then:
>
> $$
> \int_D |\nabla v|^2 \, dV = 0 \quad \Longrightarrow \quad \nabla v \equiv 0 \quad \Longrightarrow \quad v \equiv 0 \text{ on } D.
> $$
>
> This proves **[[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|uniqueness for the Dirichlet problem]]**: if $\Delta v = 0$ on $D$ and $v = 0$ on $\partial D$, then $v = 0$. Equivalently, a harmonic function is uniquely determined by its boundary values.

^rem-17-1

## Green's Second Identity

> [!theorem] Theorem §17.3: Green's Second Identity
> Let $D \subseteq \mathbb{R}^n$ be a bounded domain with piecewise smooth boundary. If $u, v \in C^2(\overline{D})$, then:
>
> $$
> \boxed{\int_D \big( u \, \Delta v - v \, \Delta u \big) \, dV = \int_{\partial D} \left( u \, \frac{\partial v}{\partial n} - v \, \frac{\partial u}{\partial n} \right) dS}
> $$

^thm-17-3

> [!proof]+ Proof
> Apply Green's first identity ([[Green's First Identity|Theorem §17.2]]) twice, then subtract.
>
> **Step 1:** Apply with $(u, v)$:
>
> $$
> \int_D (\nabla u \cdot \nabla v + u \, \Delta v) \, dV = \int_{\partial D} u \, \frac{\partial v}{\partial n} \, dS. \tag{$\star$}
> $$
>
> **Step 2:** Apply with the roles of $u$ and $v$ swapped:
>
> $$
> \int_D (\nabla v \cdot \nabla u + v \, \Delta u) \, dV = \int_{\partial D} v \, \frac{\partial u}{\partial n} \, dS. \tag{$\star\star$}
> $$
>
> **Step 3:** Subtract $(\star\star)$ from $(\star)$. On the left side, $\nabla u \cdot \nabla v = \nabla v \cdot \nabla u$, so these terms cancel:
>
> $$
> \int_D (u \, \Delta v - v \, \Delta u) \, dV = \int_{\partial D} \left( u \, \frac{\partial v}{\partial n} - v \, \frac{\partial u}{\partial n} \right) dS.
> $$

^pf-17-3

*Uses:* [[Green's First Identity|§17.2]]

> [!remark] Remark: Green's Second Identity as Symmetry
> Green's second identity expresses a kind of **symmetry of the Laplacian**: the “interaction” of $u$ with $\Delta v$ differs from the interaction of $v$ with $\Delta u$ only by a boundary term. This is the $L^2$ analog of integration by parts, and it shows that the Laplacian is a **[[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-10|self-adjoint operator]]** (up to boundary terms).
>
> In more advanced treatments, this property is the starting point for Sturm–Liouville theory, [[Real spectral theorem|spectral theory]], and the theory of distributions.

^rem-17-2

> [!remark]- Connections
> - Finite-dimensional model: an operator $T$ with $\langle Tu, v\rangle = \langle u, Tv\rangle$ ([[Linear Algebra 7A Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]) has an orthonormal eigenbasis by the [[Real spectral theorem]]; Green's second identity with vanishing boundary terms is the analogous statement for $\Delta$ with the $L^2$ inner product.

## Applications of Green's Identities

> [!example] Example §17.1: Uniqueness for the Dirichlet Problem
> **Claim:** If $\Delta u_1 = \Delta u_2$ on $D$ and $u_1 = u_2$ on $\partial D$, then $u_1 = u_2$ on $D$.
>
> *Proof.* Let $w = u_1 - u_2$. Then $\Delta w = 0$ on $D$ and $w = 0$ on $\partial D$. Apply [[Green's First Identity|Green's first identity]] with $u = v = w$:
>
> $$
> \int_D |\nabla w|^2 \, dV + \underbrace{\int_D w \, \Delta w \, dV}_{= 0} = \underbrace{\int_{\partial D} w \, \frac{\partial w}{\partial n} \, dS}_{= 0}.
> $$
>
> Therefore $\int_D |\nabla w|^2 \, dV = 0$. Since $|\nabla w|^2 \geq 0$ and is continuous, this implies $\nabla w = 0$ on $D$, so $w$ is constant. Since $w = 0$ on $\partial D$, we conclude $w \equiv 0$.

^ex-17-1

*Uses:* [[Green's First Identity|§17.2]], [[Topology §13 Connected Spaces#^def-13-1|590 §13.1]]

> [!remark]- Connections
> - 1D version of “nonnegative continuous integrand with zero integral vanishes”: [[Single Variable Analysis §33 Properties of the Riemann Integral#^thm-33-7|Vanishing Integral of a Nonnegative Function (451 §33.7)]].

> [!example] Example §17.2: Uniqueness for the Neumann Problem
> **Claim:** If $\Delta u_1 = \Delta u_2$ on $D$ and $\dfrac{\partial u_1}{\partial n} = \dfrac{\partial u_2}{\partial n}$ on $\partial D$, then $u_1 - u_2$ is constant on $D$.
>
> *Proof.* Let $w = u_1 - u_2$. Then $\Delta w = 0$ and $\dfrac{\partial w}{\partial n} = 0$ on $\partial D$. [[Green's First Identity|Green's first identity]] with $u = v = w$:
>
> $$
> \int_D |\nabla w|^2 \, dV = \int_{\partial D} w \, \underbrace{\frac{\partial w}{\partial n}}_{= 0} \, dS = 0.
> $$
>
> So $\nabla w = 0$, hence $w$ is constant. (Note: unlike Dirichlet, we cannot determine the constant — this is why Neumann solutions are unique only up to a constant.)

^ex-17-2

*Uses:* [[Green's First Identity|§17.2]], [[Topology §13 Connected Spaces#^def-13-1|590 §13.1]]

> [!example] Example §17.3: Mean Value Property of Harmonic Functions (Sketch)
> Green's identities can be used to prove the **mean value property**: if $\Delta u = 0$ on a ball $B_r(x_0) \subseteq \mathbb{R}^n$, then:
>
> $$
> u(x_0) = \frac{1}{|\partial B_r|} \int_{\partial B_r(x_0)} u \, dS,
> $$
>
> i.e., the value of a harmonic function at any point equals its average over any sphere centered at that point. The proof uses [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-3|Green's second identity]] with $v$ chosen as the **[[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|fundamental solution]]** of the Laplacian ($v = |x - x_0|^{2-n}$ for $n \geq 3$, or $v = \log |x - x_0|$ for $n = 2$).

^ex-17-3

> [!remark] Remark: Summary: The Hierarchy of Integral Theorems
> All the integral theorems in this course are instances of a single pattern:
>
> | **Theorem** | **Pattern** |
> |---|---|
> | [[Fundamental Theorem of Calculus]] | $\int_a^b F'(x) \, dx = F(b) - F(a)$ |
> | [[Green's Theorem\|Green's Theorem]] (2D) | $\iint_D (g_x - f_y) \, dA = \oint_{\partial D} f \, dx + g \, dy$ |
> | [[Divergence Theorem in ℝⁿ\|Divergence Theorem]] ($\mathbb{R}^n$) | $\int_D \nabla \cdot \mathbf{u} \, dV = \int_{\partial D} \mathbf{u} \cdot \hat{n} \, dS$ |
> | [[Stokes' Theorem in ℝ³\|Stokes' Theorem]] ($\mathbb{R}^3$) | $\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$ |
>
> In each case: *integral of a derivative over a region = integral of the function over the boundary*.
>
> In the language of differential forms (to be covered if time permits), all of these are special cases of the **[[Generalized Stokes' Theorem|generalized Stokes' theorem]]**: $\displaystyle\int_{\partial \Omega} \omega = \int_\Omega d\omega$.

^rem-17-3

> [!remark]- Connections
> - The full table after §20, including the $\mathbb{R}^3$ Divergence Theorem: [[Multivariable Analysis §20 Stokes' Theorem in ℝ³#^rem-20-5|The Complete Picture]].

## Physical Application: Conservation of Mass and Laplace's Equation

## Flux and the Continuity Equation

Consider a fluid with density $\rho(x, y, t)$ and velocity field $\mathbf{u}(x, y, t)$. Let $D$ be a fixed region in the plane with boundary $\gamma$.

**Rate of change of outflow of volume** across $\gamma$: if the flow speed is $u$ in a pipe of cross-section $S$, the volume displaced in time $T$ is $uTS$, so the volume flux per unit time is $uS$. For a general boundary:

$$
\text{rate of outflow of volume} = \oint_\gamma \mathbf{u} \cdot \hat{n} \, ds.
$$

**Rate of change of outflow of mass** across $\gamma$: weight by density:

$$
\text{rate of outflow of mass} = \oint_\gamma \rho \, \mathbf{u} \cdot \hat{n} \, ds.
$$

**Mass in $D$:**

$$
\text{mass in } D = \iint_D \rho \, dx \, dy.
$$

**Rate of change of mass in $D$:**

$$
\frac{d}{dt} \iint_D \rho \, dx \, dy = \iint_D \rho_t \, dx \, dy.
$$

If there are no sources or sinks ($\rho > 0$, mass is neither created nor destroyed), then conservation of mass says:

$$
\underbrace{\frac{d}{dt} \iint_D \rho \, dx \, dy}_{\text{rate of change of mass in } D} + \underbrace{\oint_\gamma \rho \, \mathbf{u} \cdot \hat{n} \, ds}_{\text{rate of outflow of mass}} = 0. \tag{①+②=0}
$$

Now apply the [[Multivariable Analysis §16 Line Integrals and Green's Theorem#^thm-16-2|Divergence Theorem]] to ②:

$$
\oint_\gamma \rho \, \mathbf{u} \cdot \hat{n} \, ds = \oint_\gamma (\rho \mathbf{u}) \cdot \hat{n} \, ds = \iint_D \nabla \cdot (\rho \mathbf{u}) \, dx \, dy.
$$

Substituting both terms:

$$
\iint_D \big( \rho_t + \nabla \cdot (\rho \mathbf{u}) \big) \, dx \, dy = 0 \qquad \text{for }\textbf{any}\text{ domain } D.
$$

**Key argument:** If $\iint_D f \, dx \, dy = 0$ for every domain $D$ and $f$ is continuous, then $f \equiv 0$. (If $f(a,b) > 0$, then by [[Multivariable Analysis §3 Continuity and Limits of Functions#^def-3-1|continuity]] $f \geq f(a,b)/2 > 0$ on some [[Multivariable Analysis §2 Open and Closed Sets#^def-2-1|ball]] $B_\delta(a,b) \subseteq D$, giving a [[Multivariable Analysis §15 Multivariable Integration#^thm-15-5|positive integral]] — contradiction.)

Therefore, the integrand vanishes pointwise:

> [!theorem] Theorem §17.4: Continuity Equation / Conservation of Mass
> $$
> \boxed{\rho_t + \nabla \cdot (\rho \mathbf{u}) = 0}
> $$

^thm-17-4

This is the **continuity equation**: the local form of conservation of mass.

## Incompressible Flow

Assume the fluid has constant density $\rho \equiv 1$ (incompressible). Then $\rho_t = 0$ and $\nabla \cdot (\rho \mathbf{u}) = \nabla \cdot \mathbf{u}$, so the continuity equation reduces to:

$$
\nabla \cdot \mathbf{u} = 0 \qquad \text{(divergence-free / incompressible)}.
$$

## Irrotational Flow

An additional physical condition: the flow is **[[Multivariable Analysis §11 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-11-1|irrotational]]** (no rotation), meaning:

$$
\nabla \times \mathbf{u} = 0 \qquad \text{(curl-free / irrotational)}.
$$

Writing $\mathbf{u} = (u, v)$, the two conditions become the system:

$$
\begin{cases} u_x + v_y = 0 & (\text{divergence-free}) \\ v_x - u_y = 0 & (\text{curl-free}) \end{cases}
$$

## From Potential Functions to Laplace's Equation

**Physical motivation:** If the flow is driven by a potential (e.g., gravity), there exists a **potential function** $\phi(x,y)$ such that contour lines $\phi(x,y) = c$ are level curves of energy. The gradient $\nabla \phi = (\phi_x, \phi_y)$ points in the direction of increasing energy, and the fluid flows in the *opposite* direction:

$$
\mathbf{u} = (u, v) = -\nabla \phi = (-\phi_x, -\phi_y).
$$

**Check curl-free:** With $u = -\phi_x$ and $v = -\phi_y$:

$$
v_x - u_y = -\phi_{yx} - (-\phi_{xy}) = -\phi_{yx} + \phi_{xy} = 0
$$

by [[Schwarz–Clairaut Theorem|equality of mixed partials]]. So the curl-free condition is *automatically satisfied* for any potential function. This is a [[Multivariable Analysis §11 The Three Differential Operators꞉ Gradient, Curl, Divergence|general fact]]: $\nabla \times (\nabla \phi) = 0$ always.

**Apply the divergence-free condition:**

$$
u_x + v_y = -\phi_{xx} - \phi_{yy} = 0 \qquad \Longleftrightarrow \qquad \boxed{\Delta \phi = \phi_{xx} + \phi_{yy} = 0.}
$$

This is **Laplace's equation**. A function satisfying $\Delta \phi = 0$ is called **harmonic**.

> [!remark] Remark: Summary of the Logical Chain
> $$
> \text{Conservation of mass} + \text{incompressible} + \text{irrotational} \quad \Longrightarrow \quad \text{Laplace's equation } \Delta \phi = 0.
> $$
>
> The problem of finding incompressible irrotational flow reduces to: find a potential function $\phi(x,y)$ satisfying $\Delta \phi = 0$ with appropriate boundary conditions. This is the **Dirichlet problem**, whose [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-17-1|uniqueness]] we proved using [[Green's First Identity|Green's first identity]].

^rem-17-4

> [!remark] Remark: Symmetry and Radial Solutions
> Laplace's equation $\phi_{xx} + \phi_{yy} = 0$ has a symmetric structure: the operator $\Delta$ treats $x$ and $y$ on equal footing. This symmetry motivates looking for **radial solutions**, i.e., solutions depending only on $r = \sqrt{x^2 + y^2}$: $\phi(x,y) = f(r)$.

^rem-17-5

## Computing $\Delta \phi$ for a Radial Function

Let $\phi(x,y) = f(r)$ where $r = \sqrt{x^2 + y^2}$. We compute $\phi_{xx}$ and $\phi_{yy}$ via the [[Multivariable Chain Rule|chain rule]].

**First derivatives of $r$:**

$$
r_x = \frac{x}{r}, \qquad r_y = \frac{y}{r}.
$$

**Second derivatives of $r$:**

$$
r_{xx} = \frac{\partial}{\partial x}\left(\frac{x}{r}\right) = \frac{r - x \cdot (x/r)}{r^2} = \frac{r^2 - x^2}{r^3}, \qquad r_{yy} = \frac{r^2 - y^2}{r^3}.
$$

**First derivative of $\phi$:**

$$
\phi_x = f'(r) \cdot r_x = f'(r) \cdot \frac{x}{r}.
$$

**Second derivative of $\phi$:** Using the [[Multivariable Analysis §6 Differentiability#^thm-6-4|product rule]] on $\phi_x = f'(r) \cdot r_x$:

$$
\begin{aligned}
\phi_{xx} &= \frac{\partial}{\partial x}\big(f'(r) \cdot r_x\big) = \big(f'(r)\big)_x \cdot r_x + f'(r) \cdot r_{xx} \\
&= f''(r) \cdot r_x \cdot r_x + f'(r) \cdot r_{xx} \\
&= f''(r) \cdot \frac{x^2}{r^2} + f'(r) \cdot \frac{r^2 - x^2}{r^3}.
\end{aligned}
$$

By the same argument (replacing $x$ with $y$):

$$
\phi_{yy} = f''(r) \cdot \frac{y^2}{r^2} + f'(r) \cdot \frac{r^2 - y^2}{r^3}.
$$

**The Laplacian:**

$$
\begin{aligned}
\Delta \phi = \phi_{xx} + \phi_{yy} &= f''(r) \cdot \frac{x^2 + y^2}{r^2} + f'(r) \cdot \frac{2r^2 - x^2 - y^2}{r^3} \\
&= f''(r) \cdot \frac{r^2}{r^2} + f'(r) \cdot \frac{2r^2 - r^2}{r^3} \\
&= f''(r) + \frac{f'(r)}{r}.
\end{aligned}
$$

## Solving the Radial ODE

Setting $\Delta \phi = 0$:

$$
f''(r) + \frac{1}{r} f'(r) = 0.
$$

**Step 1: Reduce order.** Let $g(r) = f'(r)$. Then:

$$
g'(r) + \frac{g(r)}{r} = 0.
$$

**Step 2: Separate variables.**

$$
\frac{dg}{g} = -\frac{dr}{r}.
$$

**Step 3: Integrate both sides.**

$$
\ln|g| = -\ln|r| + C_1 \qquad \Longrightarrow \qquad |g| = e^{C_1} \cdot \frac{1}{r} = \frac{C_2}{r}.
$$

So $g(r) = C/r$ for some constant $C$.

**Verification:** $g'(r) = -C/r^2$, so $g'(r) + g(r)/r = -C/r^2 + C/r^2 = 0$. ✓

**Step 4: Recover $f$.**

$$
f'(r) = g(r) = \frac{C}{r} \qquad \Longrightarrow \qquad f(r) = C \ln r + C'.
$$

Choosing $C' = 0$:

> [!theorem] Theorem §17.5: Fundamental Solution of the 2D Laplacian
> The function
>
> $$
> \phi(x,y) = C \ln r = C \ln \sqrt{x^2 + y^2}
> $$
>
> satisfies Laplace's equation $\Delta \phi = 0$ for all $(x,y) \neq (0,0)$.

^thm-17-5

> [!remark]- Connections
> - The 3D radial computation (giving $f'' + \frac{2}{r} f'$ and the solution $1/r$): [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates#^rem-19-2|Verification: Radial Functions]], from the [[Multivariable Analysis §19 The Laplacian in Spherical Coordinates#^thm-19-1|Laplacian in Spherical Coordinates (§19.1)]].

> [!remark] Remark: Connection to Other PDEs
> This fundamental solution is the starting point for solving boundary value problems via Green's functions. The same approach — exploit symmetry to reduce a PDE to an ODE — applies to other equations:
> - **Laplace's equation** $\Delta \phi = 0$: steady-state (time-independent) problems.
> - **Heat equation** $\phi_t = \Delta \phi$: diffusion and heat conduction (time-dependent).
> - **Wave equation** $\phi_{tt} = c^2 \Delta \phi$: vibrations and wave propagation.

^rem-17-6
