---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 5
section: 28
tags: [multivariable-analysis, math452]
---
← [[§27 Line Integrals and Green's Theorem]] · ↑ [[· 5 Line Integrals and the Divergence Theorem]] · [[§29 Conservation of Mass and Laplace's Equation]] →

In the [[§27 Line Integrals and Green's Theorem|previous section]] we derived [[Green's Theorem|Green's theorem]] (2D) and its two vector reformulations: the [[§27 Line Integrals and Green's Theorem#^thm-27-3|2D Stokes form]] (circulation = integral of curl) and the [[§27 Line Integrals and Green's Theorem#^thm-27-2|2D Divergence form]] (flux = integral of divergence). We now extend the Divergence Theorem to $\mathbb{R}^n$ and derive the classical **Green's identities**, which are the key tools for studying the Laplacian.

## The Divergence Theorem in $\mathbb{R}^n$

> [!definition] Definition §28.1: Divergence in $\mathbb{R}^n$
> For a $C^1$ vector field $\mathbf{u} = (u_1, u_2, \ldots, u_n): D \to \mathbb{R}^n$, the **divergence** is the scalar field:
>
> $$
> \nabla \cdot \mathbf{u} = \sum_{i=1}^n \frac{\partial u_i}{\partial x_i} = \frac{\partial u_1}{\partial x_1} + \frac{\partial u_2}{\partial x_2} + \cdots + \frac{\partial u_n}{\partial x_n}.
> $$

^def-28-1

> [!theorem] Theorem §28.1: Divergence Theorem in $\mathbb{R}^n$
> Let $D \subseteq \mathbb{R}^n$ be a bounded domain with piecewise smooth boundary $\partial D$. If $\mathbf{u} = (u_1, \ldots, u_n)$ is $C^1$ on an open set containing $\overline{D}$, then:
>
> $$
> \boxed{\int_{\partial D} \mathbf{u} \cdot \hat{n} \, dS = \int_D \nabla \cdot \mathbf{u} \, dV}
> $$
>
> where $\hat{n}$ is the outward unit normal to $\partial D$, $dS$ is the surface area element on $\partial D$, and $dV = dx_1 \cdots dx_n$.

^thm-28-1

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
> By [[§23 Fubini's Theorem#^thm-23-2|Fubini's theorem]], we can write the volume integral as an iterated integral:
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
> where $\nabla' \beta = (\partial_1 \beta, \ldots, \partial_{n-1} \beta)$. The surface element is $dS = \sqrt{1 + |\nabla' \beta|^2} \, d\mathbf{x}'$. (We use this graph area element ahead of §31, where area elements are derived: for $n = 3$, [[Surface Area via the Gram Matrix|Theorem §31.1]] gives $dS = \sqrt{\det G}\, d\mathbf{x}'$ with $\det G = 1 + |\nabla' \beta|^2$ for the parametrization $\mathbf{x}' \mapsto (\mathbf{x}', \beta(\mathbf{x}'))$; for $n > 3$ we take the same formula as the area element of a graph.)
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

^pf-28-1

*Uses:* [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-1|Def. §28.1]], [[§22 Properties of the Integral#^thm-22-2|§22.2]], [[§23 Fubini's Theorem#^thm-23-2|§23.2]], [[§22 Properties of the Integral#^thm-22-3|§22.3]], [[Surface Area via the Gram Matrix|§31.1]], [[Fundamental Theorem of Calculus|451 §34.1]]

> [!remark]- Connections
> - $n = 1$ is the [[Fundamental Theorem of Calculus]]; $n = 2$ is [[§27 Line Integrals and Green's Theorem#^thm-27-2|Theorem §27.2]]; the $\mathbb{R}^3$ version with parametrized surfaces is [[Divergence Theorem in ℝ³|Theorem §32.1]].
> - The same "FTC in one direction" proof, done for forms: [[Generalized Stokes' Theorem|Generalized Stokes' Theorem (§40.1)]].
> - Used in Electromagnetism: integration by parts in four dimensions turns the variation of the Maxwell action into the field equations and makes the coupling gauge invariant exactly when charge is conserved — [[§C1.1 Building the Maxwell Action#^thm-c1-1-2|EM Theorem §C1.1.2]], [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-2|EM Theorem §C1.2.2]], [[§C1.3 Gauge Symmetry and Charge Conservation#^thm-c1-3-1|EM Theorem §C1.3.1]].

## Green's Identities

The power of the Divergence Theorem lies in choosing $\mathbf{u}$ strategically. Green's identities arise from specific choices involving scalar functions and the Laplacian.

> [!definition] Definition §28.2: Gradient
> For a $C^2$ function $v: D \to \mathbb{R}$:
> - The **gradient** is $\nabla v = \left(\frac{\partial v}{\partial x_1}, \ldots, \frac{\partial v}{\partial x_n}\right)$.

^def-28-2

> [!definition] Definition §28.3: Laplacian
> For a $C^2$ function $v: D \to \mathbb{R}$:
> - The **Laplacian** is $\Delta v = \nabla \cdot (\nabla v) = \displaystyle\sum_{i=1}^n \frac{\partial^2 v}{\partial x_i^2}$.

^def-28-3

> [!remark]- Connections
> - Computational version: [[§44 Potential Equation#^def-44-1|341 Def. §44.1]] (the potential equation $\nabla^2u=0$ and [[§44 Potential Equation#^def-44-2|harmonic functions]], solved by separation of variables in rectangles and disks); the five-point difference approximation of the Laplacian, [[§71★ Potential Equation#^def-71-1|341 Def. §71.1]].
> - Computational version: [[§27★ Harmonic Functions#^def-27-1|342 Def. §27.1]] (harmonic functions of two variables, Δu = 0, with worked examples) and [[§116★ Transformations of Harmonic Functions#^prop-116-2|342 Prop. §116.2]] (the Laplacian under an analytic change of variables is multiplied by |f′|²).

> [!definition] Definition §28.4: Normal Derivative
> For a $C^2$ function $v: D \to \mathbb{R}$:
> - The **normal derivative** on $\partial D$ is $\dfrac{\partial v}{\partial n} = \nabla v \cdot \hat{n} = \displaystyle\sum_{i=1}^n \frac{\partial v}{\partial x_i} \, n_i$.

^def-28-4

> [!remark]- Connections
> - The gradient was introduced in [[§9 Directional Derivatives|§9]]; the normal derivative is the directional derivative ([[Directional Derivative Formula|Theorem §9.1]]) in the direction $\hat{n}$.

### Green's First Identity

> [!theorem] Theorem §28.2: Green's First Identity
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

^thm-28-2

> [!proof]+ Proof
> Apply the Divergence Theorem ([[Divergence Theorem in ℝⁿ|Theorem §28.1]]) with the vector field $\mathbf{w} = u \, \nabla v$.
>
> **Step 1: Compute the divergence of $\mathbf{w}$.**
>
> The $i$-th component of $\mathbf{w}$ is $w_i = u \, \frac{\partial v}{\partial x_i}$. By the [[§8 Algebra of Differentiable Functions#^thm-8-2|product rule]]:
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

^pf-28-2

*Uses:* [[Divergence Theorem in ℝⁿ|§28.1]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-2|Def. §28.2]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-3|Def. §28.3]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-4|Def. §28.4]], [[§8 Algebra of Differentiable Functions#^thm-8-2|§8.2]]

> [!remark]- Connections
> - For $n = 1$ this is ordinary [[§34 Fundamental Theorem of Calculus#^thm-34-3|Integration by Parts (451 §34.3)]].
> - Revisited with surface integrals in $\mathbb{R}^3$: [[§32 Flux Integrals and the Divergence Theorem in ℝ³#^rem-32-9|Green's Identities Revisited]].
> - Its case n = 1 is integration by parts on [a, b]: [[§51 Integration by Parts#^thm-51-2|Calc Thm. §51.2]] (with worked examples).
> - Used in PDEs: with $u=v=\phi$ an eigenfunction, it shows that the Dirichlet eigenvalues of the Laplacian are positive, [[§54★ Problems in Polar Coordinates#^rem-54-2|341 Remark §44.2]].
> - Concrete case: [[§140★ Neumann Problems#^rem-140-1|342 Remark §140.1]] (Neumann data on a circle must have mean zero, the case u = 1).
> - Used in Electromagnetism: the static action is a minimum, self-capacitance as an energy integral, the capacitance matrix as a Gram matrix, uniqueness with conductors and dielectrics, and the eigenfunction expansion of a Green function — [[§C2.1 The Static Limit and the Field of a Charge Distribution#^thm-c2-1-2|EM Theorem §C2.1.2]], [[§C4.2 Self-Capacitance and Capacitors#^thm-c4-2-1|EM Theorem §C4.2.1]], [[§C4.3 The Capacitance Matrix#^thm-c4-3-2|EM Theorem §C4.3.2]], [[§C6.1 Potential Theory and Uniqueness#^thm-c6-1-1|EM Theorem §C6.1.1]], [[§C7.4 Constructing Green Functions#^thm-c7-4-1|EM Theorem §C7.4.1]].

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
> (The last step uses that $D$ is connected, so $v$ is constant, and that $v$ is continuous up to the boundary, so this constant equals the boundary value $0$.)
>
> This proves **[[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|uniqueness for the Dirichlet problem]]**: if $\Delta v = 0$ on $D$ and $v = 0$ on $\partial D$, then $v = 0$. Equivalently, a harmonic function is uniquely determined by its boundary values.

^rem-28-1

### Green's Second Identity

> [!theorem] Theorem §28.3: Green's Second Identity
> Let $D \subseteq \mathbb{R}^n$ be a bounded domain with piecewise smooth boundary. If $u, v \in C^2(\overline{D})$, then:
>
> $$
> \boxed{\int_D \big( u \, \Delta v - v \, \Delta u \big) \, dV = \int_{\partial D} \left( u \, \frac{\partial v}{\partial n} - v \, \frac{\partial u}{\partial n} \right) dS}
> $$

^thm-28-3

> [!proof]+ Proof
> Apply Green's first identity ([[Green's First Identity|Theorem §28.2]]) twice, then subtract.
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

^pf-28-3

*Uses:* [[Green's First Identity|§28.2]]

> [!remark]- Connections
> - Used in PDEs: eigenfunctions of the Laplacian for different eigenvalues are orthogonal, [[§54★ Problems in Polar Coordinates#^thm-54-3|341 Thm. §54.3]], as for the vibrating drum, [[§58★ Vibrations of a Circular Membrane#^prop-58-3|341 Prop. §58.3]].
> - Concrete case on a disk: [[§134★ Poisson Integral Formula#^thm-134-1|342 Thm. §134.1]] (the Poisson integral formula, which represents a harmonic function by its boundary values).
> - Used in Electromagnetism: the mean-value theorem with sources, the representation formula of potential theory (single and dipole layers), and the reciprocity of Green functions — [[§C6.1 Potential Theory and Uniqueness#^thm-c6-1-2|EM Theorem §C6.1.2]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-2|EM Theorem §C7.3.2]], [[§C7.3 Green Functions for Poisson’s Equation#^thm-c7-3-3|EM Theorem §C7.3.3]].

> [!remark] Remark: Green's Second Identity as Symmetry
> Green's second identity expresses a kind of **symmetry of the Laplacian**: the “interaction” of $u$ with $\Delta v$ differs from the interaction of $v$ with $\Delta u$ only by a boundary term. This is the $L^2$ analog of integration by parts, and it shows that the Laplacian is a **[[§23 Self-Adjoint and Normal Operators#^ladr-7-10|self-adjoint operator]]** (up to boundary terms).
>
> In more advanced treatments, this property is the starting point for Sturm–Liouville theory, [[Real spectral theorem|spectral theory]], and the theory of distributions.

^rem-28-2

> [!remark]- Connections
> - Finite-dimensional model: an operator $T$ with $\langle Tu, v\rangle = \langle u, Tv\rangle$ ([[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]) has an orthonormal eigenbasis by the [[Real spectral theorem]]; Green's second identity with vanishing boundary terms is the analogous statement for $\Delta$ with the $L^2$ inner product.
> - One-dimensional version: the Sturm–Liouville operator is symmetric in the same way, [[§29 Sturm–Liouville Problems#^rem-29-3|341 Remark §23.3]], which makes its eigenfunctions orthogonal, [[§29 Sturm–Liouville Problems#^thm-29-2|341 Thm. §29.2]].

### Applications of Green's Identities

> [!example] Example §28.1: Uniqueness for the Dirichlet Problem
> **Claim:** If $\Delta u_1 = \Delta u_2$ on $D$ and $u_1 = u_2$ on $\partial D$, then $u_1 = u_2$ on $D$.
>
> *Proof.* Let $w = u_1 - u_2$. Then $\Delta w = 0$ on $D$ and $w = 0$ on $\partial D$. Apply [[Green's First Identity|Green's first identity]] with $u = v = w$:
>
> $$
> \int_D |\nabla w|^2 \, dV + \underbrace{\int_D w \, \Delta w \, dV}_{= 0} = \underbrace{\int_{\partial D} w \, \frac{\partial w}{\partial n} \, dS}_{= 0}.
> $$
>
> Therefore $\int_D |\nabla w|^2 \, dV = 0$. Since $|\nabla w|^2 \geq 0$ and is continuous, this implies $\nabla w = 0$ on $D$, so $w$ is constant (as $D$ is connected). Since $w$ is continuous on $\overline{D}$ and $w = 0$ on $\partial D$, we conclude $w \equiv 0$.

^ex-28-1

*Uses:* [[Green's First Identity|§28.2]], [[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]

> [!remark]- Connections
> - 1D version of “nonnegative continuous integrand with zero integral vanishes”: [[§33 Properties of the Riemann Integral#^thm-33-7|Vanishing Integral of a Nonnegative Function (451 §33.7)]].
> - Used in Electromagnetism: with [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-2|Ex. §28.2]], the uniqueness of the electrostatic potential for given boundary values or normal derivatives — [[§B3.1 Laplace's Equation and the Uniqueness Theorems#^thm-b3-1-3|EM Theorem §B3.1.3]]. At level C: uniqueness with conductors at given potentials or charges and with linear dielectrics — [[§C6.1 Potential Theory and Uniqueness#^thm-c6-1-1|EM Theorem §C6.1.1]].
> - Computational version: [[§49 The Poisson Integral Formula and the Mean Value Property#^cor-49-4|341 Cor. §49.4]] (uniqueness for Dirichlet's problem, proved there from the maximum principle, for the disk solved explicitly).

> [!example] Example §28.2: Uniqueness for the Neumann Problem
> **Claim:** If $\Delta u_1 = \Delta u_2$ on $D$ and $\dfrac{\partial u_1}{\partial n} = \dfrac{\partial u_2}{\partial n}$ on $\partial D$, then $u_1 - u_2$ is constant on $D$.
>
> *Proof.* Let $w = u_1 - u_2$. Then $\Delta w = 0$ and $\dfrac{\partial w}{\partial n} = 0$ on $\partial D$. [[Green's First Identity|Green's first identity]] with $u = v = w$:
>
> $$
> \int_D |\nabla w|^2 \, dV = \int_{\partial D} w \, \underbrace{\frac{\partial w}{\partial n}}_{= 0} \, dS = 0.
> $$
>
> So $\nabla w = 0$, hence $w$ is constant (as $D$ is connected). (Note: unlike Dirichlet, we cannot determine the constant — this is why Neumann solutions are unique only up to a constant.)

^ex-28-2

*Uses:* [[Green's First Identity|§28.2]], [[§15 Connected Spaces#^def-15-2|590 Def. §15.2]]

> [!remark]- Connections
> - Computational version: [[§44 Potential Equation#^prop-44-1|341 Prop. §44.1]] (adding a constant to a solution of Neumann's problem gives another, and $\oint\partial u/\partial n\,ds=0$ is needed for a solution to exist).

> [!example] Example §28.3: Mean Value Property of Harmonic Functions (Sketch)
> Green's identities can be used to prove the **mean value property**: if $\Delta u = 0$ on a ball $B_r(x_0) \subseteq \mathbb{R}^n$, then:
>
> $$
> u(x_0) = \frac{1}{|\partial B_r|} \int_{\partial B_r(x_0)} u \, dS,
> $$
>
> i.e., the value of a harmonic function at any point equals its average over any sphere centered at that point. The proof uses [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|Green's second identity]] with $v$ chosen as the **[[§29 Conservation of Mass and Laplace's Equation#^thm-29-2|fundamental solution]]** of the Laplacian ($v = |x - x_0|^{2-n}$ for $n \geq 3$, or $v = \log |x - x_0|$ for $n = 2$).

^ex-28-3

> [!remark]- Connections
> - Used in Electromagnetism: the mean-value property of the electrostatic potential, proved there in full — [[§B3.1 Laplace's Equation and the Uniqueness Theorems#^thm-b3-1-1|EM Theorem §B3.1.1]]. At level C: the mean value with charges inside the sphere — [[§C6.1 Potential Theory and Uniqueness#^thm-c6-1-2|EM Theorem §C6.1.2]].
> - Computational version: [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-2|341 Thm. §49.2]] (the mean value property in the plane, proved in full from the Poisson integral), and the maximum principle it gives, [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-3|341 Thm. §49.3]].

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
> In the language of differential forms ([[§36 Introduction to Differential Forms|§36]]–[[§40 The Generalized Stokes' Theorem|§40]]), all of these are special cases of the **[[Generalized Stokes' Theorem|generalized Stokes' theorem]]**: $\displaystyle\int_{\partial \Omega} \omega = \int_\Omega d\omega$.

^rem-28-3

> [!remark]- Connections
> - The full table after §34, including the $\mathbb{R}^3$ Divergence Theorem: [[§34 Stokes' Theorem in ℝ³#^rem-34-5|The Complete Picture]].

*Continued in [[§29 Conservation of Mass and Laplace's Equation]]: the continuity equation, incompressible irrotational flow, and the fundamental solution of the 2D Laplacian.*
