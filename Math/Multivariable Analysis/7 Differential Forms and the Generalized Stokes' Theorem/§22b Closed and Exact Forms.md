---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 7
section: "22b"
tags: [multivariable-analysis, math452]
---
← [[§22 The Algebra of Differential Forms]] · ↑ [[· 7 Differential Forms and the Generalized Stokes' Theorem]] · [[§23 The Generalized Stokes' Theorem]] →

## What the Exterior Derivative Really Measures

### What “Derivative” Means, Revisited

To understand what $d$ can and cannot do, we need to revisit what “derivative” actually means — not as a computational recipe, but as a mathematical object.

Recall from [[§6 Differentiability#^def-6-1|§6]]: $f$ is differentiable at $\mathbf{p} \in \mathbb{R}^n$ if there exists a linear map $Df_{\mathbf{p}}: \mathbb{R}^n \to \mathbb{R}$ satisfying $f(\mathbf{p} + \mathbf{h}) = f(\mathbf{p}) + Df_{\mathbf{p}}(\mathbf{h}) + o(|\mathbf{h}|)$, where $\mathbf{p} = (x_0, y_0, \ldots)$ and $\mathbf{h} = (h, k, \ldots)$ are vectors in $\mathbb{R}^n$.

> [!theorem] Proposition §22.6: Gradient = Differential = 1-Form
> The total derivative $Df_{\mathbf{p}}$ from [[§6 Differentiability#^def-6-2|§6]], the differential $df$ from [[§8 The Differential#^def-8-1|§8]], and the gradient $\nabla f$ from [[§7 Directional Derivatives#^rem-7-2|§7]] are three notations for the same linear map on tangent vectors:
>
> $$
> Df_{\mathbf{p}}(\mathbf{v}) = df(\mathbf{v}) = \nabla f \cdot \mathbf{v} = f_x v_1 + f_y v_2 + f_z v_3.
> $$
>
> Its components are the partial derivatives: $Df_{\mathbf{p}}(\hat{e}_i) = f_{x_i}(\mathbf{p})$.

^prop-22-6

*The notes give no separate proof: the first equality is [[§8 The Differential#^def-8-1|Def. §8.1]] read with $(h, k) = \mathbf{v}$, and the formula $Df_{\mathbf{p}}(\mathbf{v}) = \sum_i f_{x_i}(\mathbf{p})\, v_i$ is [[§6 Differentiability#^def-6-2|Def. §6.2]] (for unit $\mathbf{v}$ it is [[§6 Differentiability#^thm-6-1|Theorem §6.1]]).*

> [!remark]- Connections
> - $Df_{\mathbf{p}}$ is a linear functional on $\mathbb{R}^n$ ([[§12 Duality#^ladr-3-108|LADR 3.108]]); the gradient is the vector that represents it via the dot product, by the [[Riesz representation theorem|Riesz representation theorem (LADR 6.42)]].
> - On a manifold with no inner product only the differential survives, not the gradient vector: [[§30 The Cotangent Space#^rem-30-2|591 §30, Differential — Not Gradient]].

> [!definition] Definition §22.7: Second Total Derivative
> For $f: \mathbb{R}^n \to \mathbb{R}$ of class $C^2$ at $\mathbf{p}$, the **second total derivative** $D^2f_{\mathbf{p}}: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ is the bilinear form ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-1|LADR 9.1]]):
>
> $$
> D^2f_{\mathbf{p}}(\mathbf{u}, \mathbf{v}) = \lim_{t \to 0} \frac{Df_{\mathbf{p}+t\mathbf{u}}(\mathbf{v}) - Df_{\mathbf{p}}(\mathbf{v})}{t}.
> $$
>
> It measures how the [[§7 Directional Derivatives#^def-7-1|directional derivative]] $Df(\mathbf{v})$ changes as you move in direction $\mathbf{u}$.

^def-22-7

> [!theorem] Proposition §22.7: The Second Total Derivative Is the Hessian
> In coordinates:
>
> $$
> D^2f_{\mathbf{p}}(\mathbf{u}, \mathbf{v}) = \sum_{i,j} f_{x_i x_j}(\mathbf{p})\, u_i\, v_j.
> $$
>
> The matrix of $D^2f_{\mathbf{p}}$ in the standard basis ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]]) is the Hessian from [[§14a Second-Order Sufficient Conditions#^def-14-2|§14.2]]: $[D^2f_{\mathbf{p}}]_{ij} = f_{x_i x_j}(\mathbf{p})$.

^prop-22-7

*The notes state this without proof. By [[§22 The Algebra of Differential Forms#^prop-22-6|Prop. §22.6]], $Df_{\mathbf{p}+t\mathbf{u}}(\mathbf{v}) = \sum_j f_{x_j}(\mathbf{p}+t\mathbf{u})\, v_j$; differentiating each $f_{x_j}$ at $t = 0$ in the direction $\mathbf{u}$ ([[Directional Derivative Formula|directional derivative formula]]) gives $\sum_{i,j} \partial_{x_i}\partial_{x_j} f(\mathbf{p})\, u_i v_j$, and for $f \in C^2$ the order of the two partials does not matter ([[Schwarz–Clairaut Theorem|§5.1]]).*

Two directions appear because we are asking two separate questions: $\mathbf{v}$ asks “which directional derivative are we looking at?” and $\mathbf{u}$ asks “in which direction are we watching it change?” The Taylor expansion from [[Multivariable Taylor's Theorem|§9]] says exactly:

$$
f(\mathbf{p}+\mathbf{h}) = f(\mathbf{p}) + \underbrace{Df_{\mathbf{p}}(\mathbf{h})}_{\text{linear: gradient}} + \frac{1}{2}\underbrace{D^2f_{\mathbf{p}}(\mathbf{h}, \mathbf{h})}_{\text{bilinear: Hessian}} + o(|\mathbf{h}|^2).
$$

The second derivative test in [[Second Derivative Test in Several Variables|§14]] (checking whether $\mathbf{h}^T H_f \mathbf{h} > 0$ for all $\mathbf{h}$) was asking: is this bilinear form [[§14 Optimization and Lagrange Multipliers#^def-14-3|positive definite]]?

### Why $d^2 = 0$: Symmetry Kills Antisymmetry

> [!theorem] Proposition §22.8: Decomposition of Bilinear Forms
> Any bilinear form $B: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ decomposes uniquely as $B = B^{\mathrm{sym}} + B^{\mathrm{anti}}$, where:
>
> $$
> B^{\mathrm{sym}}(\mathbf{u}, \mathbf{v}) = \tfrac{1}{2}\big(B(\mathbf{u}, \mathbf{v}) + B(\mathbf{v}, \mathbf{u})\big), \qquad B^{\mathrm{anti}}(\mathbf{u}, \mathbf{v}) = \tfrac{1}{2}\big(B(\mathbf{u}, \mathbf{v}) - B(\mathbf{v}, \mathbf{u})\big).
> $$
>
> The symmetric part satisfies $B^{\mathrm{sym}}(\mathbf{u}, \mathbf{v}) = B^{\mathrm{sym}}(\mathbf{v}, \mathbf{u})$; the antisymmetric part satisfies $B^{\mathrm{anti}}(\mathbf{u}, \mathbf{v}) = -B^{\mathrm{anti}}(\mathbf{v}, \mathbf{u})$.

^prop-22-8

*The notes state this without proof: adding the two formulas gives $B$; swapping $\mathbf{u}$ and $\mathbf{v}$ gives the two symmetry properties; and if $B = S + A$ with $S$ symmetric and $A$ antisymmetric, then $B(\mathbf{u}, \mathbf{v}) + B(\mathbf{v}, \mathbf{u}) = 2S(\mathbf{u}, \mathbf{v})$ and $B(\mathbf{u}, \mathbf{v}) - B(\mathbf{v}, \mathbf{u}) = 2A(\mathbf{u}, \mathbf{v})$, which is uniqueness.*

> [!remark]- Connections
> - This is $V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}}$ in LADR ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]), with antisymmetric = alternating by [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-16|LADR 9.16]].

> [!theorem] Proposition §22.9: $d^2 = 0$ Is Clairaut's Theorem in Forms Language
> For $C^2$ functions, the following three statements are the same fact in three languages (all three hold, by Clairaut's theorem):
> 1. Equality of mixed partials: $f_{x_i x_j} = f_{x_j x_i}$ (Clairaut's theorem, [[Schwarz–Clairaut Theorem|§5]]).
> 2. The Hessian is symmetric: $D^2f(\mathbf{u}, \mathbf{v}) = D^2f(\mathbf{v}, \mathbf{u})$.
> 3. $d^2 = 0$: the exterior derivative applied twice gives zero.

^prop-22-9

> [!proof]+ Proof
> (1) $\Leftrightarrow$ (2): The Hessian matrix $[D^2f]_{ij} = f_{x_ix_j}$ is symmetric if and only if $f_{x_ix_j} = f_{x_jx_i}$.
>
> (2) $\Leftrightarrow$ (3): The exterior derivative $d$ produces antisymmetric outputs. Applied to $df$, it extracts the antisymmetric part of the second derivative:
>
> $$
> d(df) = \sum_{i < j} (f_{x_j x_i} - f_{x_i x_j})\,dx_i \wedge dx_j.
> $$
>
> This vanishes for all $f$ if and only if the antisymmetric part $\frac{1}{2}(f_{x_ix_j} - f_{x_jx_i})$ is zero, which is exactly the symmetry of the Hessian.

^pf-22-9

*Uses:* [[§22 The Algebra of Differential Forms#^prop-22-7|§22.7]], [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^prop-22-8|§22.8]], [[Schwarz–Clairaut Theorem|§5.1]], [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]

The circle of ideas is:

[[§5 Equality of Mixed Partials|§5]] (mixed partials commute: $f_{xy} = f_{yx}$) $\;\longleftrightarrow\;$ [[§14a Second-Order Sufficient Conditions|§14a]] (Hessian is symmetric) $\;\longleftrightarrow\;$ §22 ($d^2 = 0$).

**The two branches of bilinear algebra.** From “bilinear maps on tangent vectors,” two independent theories branch off:
- **Symmetric** ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-9|LADR 9.9]]): inner products, metrics, Hessians, the second derivative test. This is the world of Riemannian geometry (Chapter 13 of Lee).
- **Antisymmetric** ([[§32 Bilinear Forms and Quadratic Forms#^ladr-9-14|LADR 9.14]]): forms, wedge products, determinants, orientation. This is the world of differential forms (Chapter 14 of Lee).

Both arise from bilinear algebra; neither contains the other. The Hessian lives in the symmetric branch; forms live in the antisymmetric branch. The identity $d^2 = 0$ is the statement that the second derivative is entirely symmetric — so the antisymmetric branch sees nothing there.

## Closed and Exact Forms

### What $d$ Actually Measures: Obstructions to Exactness

If $d$ does not give higher derivatives of functions, what *does* it do on higher forms?

At each level, $d$ measures the **obstruction to solving an equation**:

**On 0-forms:** $df$ measures how $f$ changes. The equation $df = 0$ means $f$ is constant.

**On 1-forms:** $d\omega$ measures how far $\omega$ is from being the differential of some function. The equation $d\omega = 0$ means $\omega$ is *closed* — it satisfies the integrability condition. But closed does not mean *exact*: $\omega = df$ for some $f$. The question “is every closed 1-form exact?” depends on the *topology* of the domain.

**On 2-forms:** $d\eta$ measures how far $\eta$ is from being $d\omega$ for some 1-form $\omega$. The equation $d\eta = 0$ means $\eta$ is closed; the question “is $\eta = d\omega$?” again depends on the topology.

> [!definition] Definition §22.8: Closed Form
> A differential form $\omega$ is **closed** if $d\omega = 0$.

^def-22-8

> [!definition] Definition §22.8: Exact Form
> Let $\omega$ be a differential form. It is **exact** if $\omega = d\eta$ for some form $\eta$ of one degree lower.

^def-22-new2

> [!remark]- Connections
> - Computational version: the differential equation $M + Ny' = 0$ is exact, [[§9 Exact Differential Equations and Integrating Factors#^def-9-1|331 Def. §9.1]], when the 1-form $M\,dx + N\,dy$ is exact, $d\psi$ (with worked examples).

> [!theorem] Proposition §22.10: Exact $\Rightarrow$ Closed
> Every exact form is closed.

^prop-22-10

> [!proof]+ Proof
> If $\omega = d\eta$, then $d\omega = d(d\eta) = d^2\eta = 0$ by [[Exterior Derivative Squares to Zero|Theorem §22.5]].

^pf-22-10

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-8|Def. §22.8]], [[§22 The Algebra of Differential Forms#^def-22-new2|Def. §22.8]], [[Exterior Derivative Squares to Zero|§22.5]]

> [!remark]- Connections
> - Vector-field form: a conservative field satisfies $P_y = Q_x$, [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Calc Thm. §109.4]], and $\operatorname{curl}\nabla f = \mathbf 0$, [[§111 Curl and Divergence#^thm-111-1|Calc Thm. §111.1]] (with worked examples).

The forms terminology and the vector calculus terminology from [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-11-1|§11]] describe the same concepts:

| **Forms (§22)** | **Vector calculus (§11)** | **Condition** |
|---|---|---|
| exact 1-form: $\omega = df$ | conservative (gradient) field: $\mathbf{F} = \nabla f$ | has a potential |
| closed 1-form: $d\omega = 0$ | irrotational (curl-free) field: $\nabla \times \mathbf{F} = \mathbf{0}$ | no local rotation |
| exact 2-form: $\eta = d\omega$ | $\mathbf{F} = \nabla \times \mathbf{G}$ for some $\mathbf{G}$ | is a curl |
| closed 2-form: $d\eta = 0$ | solenoidal (divergence-free): $\nabla \cdot \mathbf{F} = 0$ | no net flux |
| exact $\Rightarrow$ closed | conservative $\Rightarrow$ irrotational; curl $\Rightarrow$ solenoidal | $d^2 = 0$ |

The converse — is every closed form exact? — is the central question. Equivalently:
- *Is every curl-free vector field a gradient?* (Is every closed 1-form exact?)
- *Is every divergence-free vector field a curl?* (Is every closed 2-form exact?)

> [!theorem] Proposition §22.11: A Closed Form That Is Not Exact
> On $\mathbb{R}^2 \setminus \{0\}$ (the plane with the origin removed), the 1-form
>
> $$
> \omega = \frac{-y\,dx + x\,dy}{x^2 + y^2}
> $$
>
> is closed ($d\omega = 0$) but not exact (there is no function $f$ on $\mathbb{R}^2 \setminus \{0\}$ with $df = \omega$).

^prop-22-11

> [!proof]+ Proof
> *Closed:* Write $\omega = f_1\,dx + f_2\,dy$ with $f_1 = \frac{-y}{x^2+y^2}$ and $f_2 = \frac{x}{x^2+y^2}$. Compute:
>
> $$
> (f_2)_x - (f_1)_y = \frac{(x^2+y^2) - x \cdot 2x}{(x^2+y^2)^2} - \frac{-(x^2+y^2) + y \cdot 2y}{(x^2+y^2)^2} = \frac{y^2 - x^2 + x^2 - y^2}{(x^2+y^2)^2} = 0.
> $$
>
> *Not exact:* Integrate $\omega$ around the unit circle $\boldsymbol{\gamma}(t) = (\cos t, \sin t)$ for $t \in [0, 2\pi]$:
>
> $$
> \int_{\boldsymbol{\gamma}} \omega = \int_0^{2\pi} \frac{-\sin t \cdot (-\sin t) + \cos t \cdot \cos t}{1}\,dt = \int_0^{2\pi} 1\,dt = 2\pi \neq 0.
> $$
>
> If $\omega = df$ for some $f$, the integral around any closed curve would be $f(\text{end}) - f(\text{start}) = 0$ ([[Fundamental Theorem of Calculus|FTC]]). The nonzero integral is a contradiction.

^pf-22-11

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-8|Def. §22.8]], [[§22 The Algebra of Differential Forms#^def-22-new2|Def. §22.8]], [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-5|Def. §22.5]], [[Multivariable Chain Rule|§10.2]], [[Fundamental Theorem of Calculus|451 §34.1]]

*Chain ([[Angle form on the punctured plane|angle form]]):* ← [[§13 The Inverse Function Theorem#^ex-13-3|Chapter 3]]

*Chain ([[Unit circle and unit sphere|unit circle]]):* ← [[§22a The Exterior Derivative#^ex-22-5|§22.5]]

What went wrong? The domain $\mathbb{R}^2 \setminus \{0\}$ has a *hole* — the removed origin. The closed curve $\boldsymbol{\gamma}$ wraps around this hole, and the form $\omega$ detects it. On domains without holes, this failure does not occur:

![[m452-22-2.svg]]
*The vector field $\frac{(-y,\,x)}{x^2+y^2}$ of $\omega = \frac{-y\,dx + x\,dy}{x^2+y^2}$ (blue; arrow lengths shrink like $1/r$) circulates around the removed origin (hollow dot). Locally the field is a gradient (the curl vanishes), but no global potential exists: the counterclockwise unit circle $\boldsymbol{\gamma}$ (red) picks up $\int_{\boldsymbol{\gamma}}\omega = 2\pi$ per loop around the hole. The form measures the winding — an analytic object detecting a topological feature.*

> [!remark]- Connections
> - The topological side of the same hole: $\pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \pi_1(S^1)$ ([[§26 Deformation Retracts and Homotopy Type#^thm-26-2|590 §26.2]]) $\cong \mathbb{Z}$ ([[Fundamental Group of the Circle]]); $\frac{1}{2\pi}\int_{\boldsymbol{\gamma}}\omega$ counts the winding.
> - On a manifold: the same form on $\mathbb{R}^2 \setminus \{0\}$ satisfies the necessary condition for being a differential, [[§43 One-Forms#^prop-43-3|591 Prop. §43.3]], yet is not $df$, [[§43 One-Forms#^rem-43-1|591 Remark: The Condition Is Not Sufficient]].
> - Used in Electromagnetism: $\omega$ is the field $\hat\varphi/s$ of a line current, curl-free off the axis with circulation $2\pi$ around it, so its curl is a delta function on the axis — [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^ex-b1-2-2|EM Example §B1.2.2]]; the warning that curl-free is not enough on a region with a hole — [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^cau-b1-2-1|EM Caution: Curl-free is not enough on a region with a hole]].

> [!theorem] Proposition §22.12: Poincaré Lemma
> On a star-shaped domain $D \subseteq \mathbb{R}^n$ (i.e., there exists a point $\mathbf{p}_0 \in D$ such that the line segment from $\mathbf{p}_0$ to any $\mathbf{p} \in D$ lies entirely in $D$), every closed form is exact: $d\omega = 0 \;\Rightarrow\; \omega = d\eta$ for some $\eta$.
>
> In particular, since $\mathbb{R}^n$ itself is star-shaped, every closed form on $\mathbb{R}^n$ is exact.

^prop-22-12

![[m452-22-3.svg]]
*Why star-shaped is the right hypothesis. Left: from $\mathbf{p}_0$ every segment stays in the domain, so a potential can be built by integrating along these segments (the homotopy operator) — closed forms are exact. Right: in $\mathbb{R}^2\setminus\{\mathbf{0}\}$ no point works as $\mathbf{p}_0$: the segment to the point $\mathbf{p}$ opposite the hole runs through the removed origin, and indeed the closed form of Proposition §22.11 is not exact there.*

> [!remark]- Connections
> - A star-shaped domain contracts to $\mathbf{p}_0$ along the segments — a [[§22 Homotopy of Paths#^thm-22-1|straight-line homotopy (590 §22.1)]] — so it is [[§23 The Fundamental Group#^def-23-3|simply connected (590 Def. §23.3)]]; the homotopy operator of the standard proof (not given in the course; see below) integrates along exactly these segments.
> - Used in Electromagnetism: on a star-shaped region a curl-free field is a gradient and a divergence-free field is a curl, which gives the scalar and vector potentials — [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^thm-b1-2-3|EM Theorem §B1.2.3]], with the hole case in [[§B1.2 The Dirac Delta Function and the Helmholtz Theorem#^cau-b1-2-1|EM Caution: Curl-free is not enough on a region with a hole]]. At level C: in four dimensions, every field tensor obeying the Bianchi identity on a star-shaped region has a potential, by the explicit homotopy formula — [[§C1.2 The Field Equations and the Bianchi Identity#^thm-c1-2-5|EM Theorem §C1.2.5]].
> - Used in Relativity: on a region without holes every field tensor obeying the homogeneous Maxwell pair comes from a four-potential — [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]], [[§B4.2 The Electromagnetic Field Tensor#^rem-b4-2-4|REL Remark: Layers, and what comes later]].
> - Vector-field form: curl-free fields on ℝ³ are conservative, [[§114 Stokes' Theorem#^thm-114-4|Calc Thm. §114.4]], and the plane test on simply-connected regions, [[§110 Green's Theorem#^thm-110-5|Calc Thm. §110.5]] (with worked examples).
> - Computational version: for 1-forms on a rectangle in $\mathbb{R}^2$ the lemma is the test for exactness $M_y = N_x$, proved there by building the potential $\psi$, [[§9 Exact Differential Equations and Integrating Factors#^thm-9-2|331 Thm. §9.2]] (with worked examples).
> - Complex version for 1-forms in the plane: [[§115★ Harmonic Conjugates#^thm-115-4|342 Thm. §115.4]] (on a simply connected domain the closed 1-form −(∂u/∂y) dx + (∂u/∂x) dy of a harmonic u is exact, which gives its harmonic conjugate).

The proof (constructing $\eta$ explicitly via a homotopy operator) is beyond the scope of this course; see Lee, Chapter 17. The key point is that the failure of exactness is a *topological* property of the domain — it detects holes.

### From Obstructions to Topology

The space of closed forms modulo exact forms:

$$
H^k = \frac{\{\text{closed } k\text{-forms}\}}{\{\text{exact } k\text{-forms}\}}
$$

is called the **$k$-th de Rham cohomology group**. It measures the “$k$-dimensional holes” in the domain:
- $H^0$ counts the connected components: no 0-form is exact (there are no $(-1)$-forms), so $H^0$ is the space of closed 0-forms, i.e., locally constant functions, with one dimension per [[§13 Connected Spaces#^def-13-new1|connected]] component.
- $H^1$ detects 1-dimensional holes: loops that cannot be contracted to a point. The example above ([[§22 The Algebra of Differential Forms#^prop-22-11|Proposition §22.11]]) shows $H^1(\mathbb{R}^2 \setminus \{0\}) \neq 0$.
- $H^2$ detects 2-dimensional holes: closed surfaces that do not bound a volume.

This is the bridge from calculus to topology: the exterior derivative $d$, defined purely by differentiation, detects the *shape* of the domain. This is the content of Chapters 17–18 of Lee's textbook (the 591 syllabus), and connects directly to the [[§23 The Fundamental Group#^def-23-2|fundamental group]] $\pi_1$ from 590.

## Applications to Physics

In physics, the exterior derivative on higher forms is not abstract at all — it describes the fundamental forces.

The electromagnetic potential $A$ is a 1-form. Its exterior derivative $F = dA$ is a 2-form — the electromagnetic field tensor (with 6 independent components: 3 for $\mathbf{E}$, 3 for $\mathbf{B}$, as discussed in [[§22 The Algebra of Differential Forms#^rem-22-4|Remark: The ℝ³ Accident]]). Two of Maxwell's equations become:

$$
dF = 0 \qquad \text{(no magnetic monopoles; Faraday's law)}.
$$

This is just $d^2A = 0$ — the identity $d^2 = 0$ is the reason magnetic monopoles do not exist (in classical electromagnetism). The other two Maxwell equations are $d{*}F = J$, where $*$ is the Hodge star and $J$ is the current 3-form.

More generally, in gauge theory and general relativity, the curvature of a connection is a 2-form, and the equations of motion (Yang–Mills, Einstein) are expressed as conditions on this curvature 2-form and its exterior derivative. The machinery of forms and $d$ is not a reformulation of known physics — it is the *native language* in which modern theoretical physics is written.
