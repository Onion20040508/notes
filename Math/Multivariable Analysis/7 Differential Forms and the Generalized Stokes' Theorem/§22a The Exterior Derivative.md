---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 7
section: "22a"
tags: [multivariable-analysis, math452]
---
← [[§22 The Algebra of Differential Forms]] · ↑ [[· 7 Differential Forms and the Generalized Stokes' Theorem]] · [[§22b Closed and Exact Forms]] →

## The Exterior Derivative

The exterior derivative $d$ takes a $k$-form to a $(k+1)$-form. It is defined by a simple recipe and turns out to unify the gradient, curl, and divergence.

> [!definition] Definition §22.4: Exterior Derivative
> **On 0-forms** (functions $f$):
>
> $$
> df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz.
> $$
>
> This is the total differential from [[§8 The Differential#^def-8-1|Def. §8.1]] — the same $df$ we have been writing all semester.
>
> **On 1-forms** ($\omega = f_1 \, dx + f_2 \, dy + f_3 \, dz$): apply $d$ to each coefficient and wedge with the existing differential:
>
> $$
> d\omega = df_1 \wedge dx + df_2 \wedge dy + df_3 \wedge dz
> $$
>
> where $df_1 = (f_1)_x \, dx + (f_1)_y \, dy + (f_1)_z \, dz$, etc.
>
> **On 2-forms** ($\eta = f_{23} \, dy \wedge dz + f_{31} \, dz \wedge dx + f_{12} \, dx \wedge dy$): same rule:
>
> $$
> d\eta = df_{23} \wedge dy \wedge dz + df_{31} \wedge dz \wedge dx + df_{12} \wedge dx \wedge dy.
> $$

^def-22-4

The recipe is always the same: differentiate each coefficient, wedge the result with the existing differentials, and simplify using anti-commutativity.

> [!theorem] Proposition §22.2: $d$ on 0-Forms Gives the Gradient
> For a smooth function $f$ on $\mathbb{R}^3$:
>
> $$
> df = f_x \, dx + f_y \, dy + f_z \, dz.
> $$
>
> That is, the coefficients of the 1-form $df$ are the components of $\nabla f = (f_x, f_y, f_z)$. The differential from [[§8 The Differential#^def-8-1|§8]] and the gradient from [[§7 Directional Derivatives#^rem-7-2|§7]] are the same object: one is a 1-form, the other is the corresponding vector field.

^prop-22-2

*Immediate from the case of 0-forms in [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]]; no separate proof is needed.*

> [!theorem] Proposition §22.3: $d$ on 1-Forms Gives the Curl
> For a smooth 1-form $\omega = f_1 \, dx + f_2 \, dy + f_3 \, dz$ on $\mathbb{R}^3$:
>
> $$
> d\omega = \big((f_3)_y - (f_2)_z\big) \, dy \wedge dz + \big((f_1)_z - (f_3)_x\big) \, dz \wedge dx + \big((f_2)_x - (f_1)_y\big) \, dx \wedge dy.
> $$
>
> That is, the coefficients of the 2-form $d\omega$ are the components of $\nabla \times \mathbf{F}$ where $\mathbf{F} = (f_1, f_2, f_3)$ (written $P, Q, R$ in §16–§20). The curl, first introduced in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]] and [[§16 Line Integrals and Green's Theorem#^def-16-5|§16]], is $d$ applied to a 1-form.

^prop-22-3

> [!proof]+ Proof
> Compute:
>
> $$
> \begin{aligned}
> d\omega &= df_1 \wedge dx + df_2 \wedge dy + df_3 \wedge dz \\
> &= ((f_1)_x \, dx + (f_1)_y \, dy + (f_1)_z \, dz) \wedge dx + ((f_2)_x \, dx + (f_2)_y \, dy + (f_2)_z \, dz) \wedge dy \\
> &\quad + ((f_3)_x \, dx + (f_3)_y \, dy + (f_3)_z \, dz) \wedge dz.
> \end{aligned}
> $$
>
> Expanding, using $dx \wedge dx = dy \wedge dy = dz \wedge dz = 0$:
>
> $$
> \begin{aligned}
> d\omega &= (f_1)_y \, dy \wedge dx + (f_1)_z \, dz \wedge dx \\
> &\quad + (f_2)_x \, dx \wedge dy + (f_2)_z \, dz \wedge dy \\
> &\quad + (f_3)_x \, dx \wedge dz + (f_3)_y \, dy \wedge dz.
> \end{aligned}
> $$
>
> Using anti-commutativity to put each term in standard order ($dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$):
>
> $$
> d\omega = \big((f_3)_y - (f_2)_z\big) \, dy \wedge dz + \big((f_1)_z - (f_3)_x\big) \, dz \wedge dx + \big((f_2)_x - (f_1)_y\big) \, dx \wedge dy.
> $$
>
> The three coefficients are exactly the components of $\nabla \times \mathbf{F}$.

^pf-22-3

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[§16 Line Integrals and Green's Theorem#^def-16-5|Def. §16.5]]

> [!theorem] Proposition §22.4: $d$ on 2-Forms Gives the Divergence
> For a smooth 2-form $\eta = f_{23} \, dy \wedge dz + f_{31} \, dz \wedge dx + f_{12} \, dx \wedge dy$ on $\mathbb{R}^3$:
>
> $$
> d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big) \, dx \wedge dy \wedge dz.
> $$
>
> That is, the coefficient of the 3-form $d\eta$ is $\nabla \cdot \mathbf{F}$ where $\mathbf{F} = (f_{23}, f_{31}, f_{12})$ (written $\mathbf{u} = (a, b, c)$ in §18). The divergence, first introduced in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|§11]] and [[§16 Line Integrals and Green's Theorem#^def-16-4|§16]], is $d$ applied to a 2-form.

^prop-22-4

> [!proof]+ Proof
> Compute:
>
> $$
> \begin{aligned}
> d\eta &= df_{23} \wedge dy \wedge dz + df_{31} \wedge dz \wedge dx + df_{12} \wedge dx \wedge dy \\
> &= ((f_{23})_x \, dx + (f_{23})_y \, dy + (f_{23})_z \, dz) \wedge dy \wedge dz \\
> &\quad + ((f_{31})_x \, dx + (f_{31})_y \, dy + (f_{31})_z \, dz) \wedge dz \wedge dx \\
> &\quad + ((f_{12})_x \, dx + (f_{12})_y \, dy + (f_{12})_z \, dz) \wedge dx \wedge dy.
> \end{aligned}
> $$
>
> In each line, only the term with the “missing” differential survives (all others have a repeated factor):
>
> $$
> \begin{aligned}
> d\eta &= (f_{23})_x \, dx \wedge dy \wedge dz + (f_{31})_y \, dy \wedge dz \wedge dx + (f_{12})_z \, dz \wedge dx \wedge dy.
> \end{aligned}
> $$
>
> Reorder each to the standard $dx \wedge dy \wedge dz$ (each is an even permutation):
>
> $$
> d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big) \, dx \wedge dy \wedge dz.
> $$
>
> The coefficient is $\nabla \cdot \mathbf{F}$.

^pf-22-4

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[§22 The Algebra of Differential Forms#^prop-22-1|§22.1]], [[§16 Line Integrals and Green's Theorem#^def-16-4|Def. §16.4]]

These three propositions are summarized in the following table:

| **Input** | **Output** | **$d$ computes** | **Vector calculus name** |
|:-:|:-:|:-:|:-:|
| 0-form $f$ | 1-form $df$ | $\nabla f$ | gradient |
| 1-form $\omega$ | 2-form $d\omega$ | $\nabla \times \mathbf{F}$ | curl |
| 2-form $\eta$ | 3-form $d\eta$ | $\nabla \cdot \mathbf{F}$ | divergence |

### The Ladder: Gradient, Curl, and Divergence Are Not at the Same Level

In vector calculus, gradient, curl, and divergence all appear to be “differential operators on vector fields”:

$$
f \xrightarrow{\nabla} \mathbf{F} \xrightarrow{\nabla\times} \mathbf{G} \xrightarrow{\nabla\cdot} h.
$$

It seems like curl and divergence sit at the same level — both take vector fields and produce something. The identities $\nabla \times (\nabla f) = \mathbf{0}$ and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$ look like two separate facts.

In the forms picture, they form a **ladder**:

$$
\underbrace{f}_{\text{0-form}} \xrightarrow{\;d\;} \underbrace{P\,dx + Q\,dy + R\,dz}_{\text{1-form}} \xrightarrow{\;d\;} \underbrace{A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy}_{\text{2-form}} \xrightarrow{\;d\;} \underbrace{h\,dx \wedge dy \wedge dz}_{\text{3-form}}
$$

Each arrow is the *same* operator $d$, but applied at a different rung:
- $d$ on a 0-form (degree $0 \to 1$) = gradient
- $d$ on a 1-form (degree $1 \to 2$) = curl
- $d$ on a 2-form (degree $2 \to 3$) = divergence

Curl and divergence are **not** at the same level: curl goes from degree 1 to degree 2, divergence goes from degree 2 to degree 3. The two “separate” identities $\nabla \times (\nabla f) = 0$ and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$ are the single identity $d \circ d = 0$ applied at consecutive rungs.

> [!remark] Remark: The $\mathbb{R}^3$ Accident
> Why do curl and divergence *look* like they are at the same level in vector calculus? Because of a coincidence specific to $\mathbb{R}^3$.
>
> In $\mathbb{R}^n$, the number of independent $k$-forms is $\binom{n}{k}$. In $\mathbb{R}^3$:
>
> $$
> \binom{3}{0} = 1, \qquad \binom{3}{1} = 3, \qquad \binom{3}{2} = 3, \qquad \binom{3}{3} = 1.
> $$
>
> Both 1-forms and 2-forms have **3 components**. Since a vector field in $\mathbb{R}^3$ also has 3 components, we can represent *both* as vector fields. This lets us write both curl and divergence as operations on “vector fields,” hiding the fact that they act on forms of different degrees.
>
> **This coincidence fails in every other dimension:**
> - In $\mathbb{R}^2$: $\binom{2}{1} = 2$ components for 1-forms, $\binom{2}{2} = 1$ component for 2-forms. The “curl” of a 1-form $P\,dx + Q\,dy$ is the 2-form $(Q_x - P_y)\,dx \wedge dy$ — a single scalar, not a vector. This is why the 2D curl in [[§16 Line Integrals and Green's Theorem#^thm-16-3|Green's theorem]] is a number, not a vector field.
> - In $\mathbb{R}^4$: $\binom{4}{1} = 4$ components for 1-forms, $\binom{4}{2} = 6$ components for 2-forms. The “curl” of a 1-form is a 6-component object — it cannot be represented as a vector field. The cross product does not exist in $\mathbb{R}^4$ for the same reason.
>
> The exterior derivative $d$ works in *any* dimension. The vector calculus operators grad, curl, div are dimension-3 translations of $d$ that rely on the coincidence $\binom{3}{1} = \binom{3}{2}$.
>
> This also explains a fact from physics: the electromagnetic field in 4D spacetime is naturally a 2-form $F$ (with 6 independent components: 3 for $\mathbf{E}$, 3 for $\mathbf{B}$). Maxwell's equations become $dF = 0$ and $d{*}F = J$. The fact that $\mathbf{E}$ and $\mathbf{B}$ combine into a single object is invisible in 3D vector calculus but natural in the language of forms.

^rem-22-4

## $d^2 = 0$: The Unifying Identity

> [!theorem] Theorem §22.5: $d^2 = 0$
> For any smooth $k$-form $\omega$: $d(d\omega) = 0$.

^thm-22-5

> [!proof]+ Proof
> It suffices to check on a 0-form $f$: for $\omega = g\,dx_{i_1} \wedge \cdots \wedge dx_{i_k}$ the recipe of [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]] gives $d\omega = dg \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}$ and then $d(d\omega) = d(dg) \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}$, and a general $k$-form is a sum of such terms.
>
> Compute $d(df)$: we have $df = f_x \, dx + f_y \, dy + f_z \, dz$, so:
>
> $$
> \begin{aligned}
> d(df) &= (f_{xy} \, dy + f_{xz} \, dz) \wedge dx + (f_{yx} \, dx + f_{yz} \, dz) \wedge dy + (f_{zx} \, dx + f_{zy} \, dy) \wedge dz \\
> &= f_{xy} \, dy \wedge dx + f_{xz} \, dz \wedge dx + f_{yx} \, dx \wedge dy + f_{yz} \, dz \wedge dy \\
> &\quad + f_{zx} \, dx \wedge dz + f_{zy} \, dy \wedge dz.
> \end{aligned}
> $$
>
> Using $dy \wedge dx = -dx \wedge dy$, etc.:
>
> $$
> d(df) = (f_{yx} - f_{xy}) \, dx \wedge dy + (f_{xz} - f_{zx}) \, dz \wedge dx + (f_{zy} - f_{yz}) \, dy \wedge dz = 0
> $$
>
> by equality of mixed partials ([[Schwarz–Clairaut Theorem|Schwarz–Clairaut]]) ($f_{xy} = f_{yx}$, etc.).

^pf-22-5

*Uses:* [[§22 The Algebra of Differential Forms#^def-22-4|Def. §22.4]], [[§22 The Algebra of Differential Forms#^def-22-1|Def. §22.1]], [[Schwarz–Clairaut Theorem|§5.1]]

> [!remark]- Connections
> - Why it works: the second derivative is a symmetric bilinear form and $d$ keeps only the alternating part ([[§22 The Algebra of Differential Forms#^prop-22-9|Proposition §22.9]]; linear algebra: [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-17|LADR 9.17]]).
> - Used in Relativity: $d^2 = 0$ makes a gauge transformation leave the coupling of a charge and the field tensor unchanged — [[§B3.2 The Charged Particle#^thm-b3-2-3|REL Theorem §B3.2.3]]; and makes the homogeneous Maxwell pair an identity for any field tensor built from a potential — [[§B4.2 The Electromagnetic Field Tensor#^thm-b4-2-7|REL Theorem §B4.2.7]].
> - Vector-field form: $\operatorname{curl}\nabla f = \mathbf 0$, [[§111 Curl and Divergence#^thm-111-1|Calc Thm. §111.1]], and $\operatorname{div}\operatorname{curl}\mathbf F = 0$, [[§111 Curl and Divergence#^thm-111-3|Calc Thm. §111.3]].

> [!remark] Remark: Classical Consequences of $d^2 = 0$
> The identity $d^2 = 0$ applied at consecutive rungs of the ladder gives:
> - Rung $0 \to 1 \to 2$: $d(df) = 0$, i.e., $\nabla \times (\nabla f) = \mathbf{0}$. The curl of a gradient is zero.
> - Rung $1 \to 2 \to 3$: $d(d\omega) = 0$ for a 1-form, i.e., $\nabla \cdot (\nabla \times \mathbf{F}) = 0$. The divergence of a curl is zero.
>
> These are not two separate computational accidents — they are the *same* identity $d \circ d = 0$ applied at different points on the ladder. This also explains why the flux of a curl through a closed surface $S$ vanishes: by [[Stokes' Theorem in ℝ³|Stokes']], $\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \int_S d\omega = \int_{\partial S} \omega = 0$ since $\partial S = \emptyset$ (equivalently, by the [[Divergence Theorem in ℝ³|Divergence Theorem]], since $\nabla \cdot (\nabla \times \mathbf{F}) = 0$).

^rem-22-5

## Translating the Known Integrals into Forms

With the wedge product, exterior derivative, and $d^2 = 0$ in hand, we can define what it means to integrate a differential form. The key idea is **pullback**: substitute the parametrization into the form to obtain a function on the parameter domain, then integrate that function.

> [!definition] Definition §22.5: Integration of a 1-Form over a Curve
> Let $\omega = f_1\,dx + f_2\,dy + f_3\,dz$ be a $C^0$ 1-form on an open set $U \subseteq \mathbb{R}^3$, and let $\boldsymbol{\gamma}: [a,b] \to U$ be a $C^1$ curve. The integral of $\omega$ over $\boldsymbol{\gamma}$ is defined by pulling back: substitute $dx = x'(t)\,dt$, $dy = y'(t)\,dt$, $dz = z'(t)\,dt$:
>
> $$
> \int_{\boldsymbol{\gamma}} \omega \;=\; \int_a^b \big(f_1\,x' + f_2\,y' + f_3\,z'\big)\,dt.
> $$

^def-22-5

> [!remark] Remark: 1-Form Integration Recovers the Line Integral
> The integral $\int_{\boldsymbol{\gamma}} \omega$ is the same as the line integral $\int_{\boldsymbol{\gamma}} \mathbf{F} \cdot d\mathbf{r}$ from [[§16 Line Integrals and Green's Theorem#^def-16-2|§16]], where $\mathbf{F} = (f_1, f_2, f_3)$: expanding $\mathbf{F} \cdot d\mathbf{r} = (f_1, f_2, f_3) \cdot (x', y', z')\,dt$ gives the same integrand.

^rem-22-6

> [!definition] Definition §22.6: Integration of a 2-Form over a Surface
> Let $\eta = f_{23}\,dy \wedge dz + f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ be a $C^0$ 2-form, and let $\mathbf{X}: D \to \mathbb{R}^3$ be a $C^1$ parametrized surface. The integral of $\eta$ over $S = \mathbf{X}(D)$ is defined by pulling back: substitute $dy \wedge dz = (y_u z_v - z_u y_v)\,du\,dv$, etc.:
>
> $$
> \iint_S \eta \;=\; \iint_D (f_{23}, f_{31}, f_{12}) \cdot (\mathbf{X}_u \times \mathbf{X}_v)\,du\,dv.
> $$

^def-22-6

> [!remark] Remark: 2-Form Integration Recovers the Flux Integral
> The integral $\iint_S \eta$ is the same as the flux integral $\iint_S \mathbf{F} \cdot d\mathbf{S}$ from [[§18 Surface Integrals#^def-18-6|§18]], where $\mathbf{F} = (f_{23}, f_{31}, f_{12})$: the cross product $\mathbf{X}_u \times \mathbf{X}_v$ produces the oriented area element, and the dot product selects the normal component of $\mathbf{F}$.

^rem-22-7

> [!remark] Remark: Scalar Integrals Are Not Form Integrals
> The scalar line integral $\int_{\boldsymbol{\gamma}} f\,ds$ and the scalar surface integral $\iint_S f\,dS$ cannot be expressed as integrals of differential forms. Their elements $ds = |\boldsymbol{\gamma}'(t)|\,dt$ and $dS = |\mathbf{X}_u \times \mathbf{X}_v|\,du\,dv$ involve absolute values, making them orientation-independent ([[§21 Introduction to Differential Forms#Signed, Unsigned, and Signed in Disguise|Category 2]]). Since they carry no sign, they do not participate in any integral theorem.

^rem-22-8

> [!example] Example §22.5: Flux Through the Unit Sphere via Pullback
> Compute $\iint_S \eta$ where $\eta = z\,dx \wedge dy$ (a 2-form) and $S$ is the unit sphere with outward orientation.
>
> **Step 1: Parametrize.** Use spherical coordinates:
>
> $$
> \mathbf{X}(\phi, \theta) = (\cos\phi\sin\theta, \;\sin\phi\sin\theta, \;\cos\theta), \qquad \phi \in [0, 2\pi], \;\; \theta \in [0, \pi].
> $$
>
> **Step 2: Pull back.** On the sphere, $z = \cos\theta$, and we need $\mathbf{X}^{\ast}(dx \wedge dy)$. Compute:
>
> $$
> \begin{aligned}
> dx &= -\sin\phi\sin\theta\,d\phi + \cos\phi\cos\theta\,d\theta, \\
> dy &= \cos\phi\sin\theta\,d\phi + \sin\phi\cos\theta\,d\theta.
> \end{aligned}
> $$
>
> By the pullback definition:
>
> $$
> \begin{aligned}
> \mathbf{X}^*(dx \wedge dy) &= \det \begin{pmatrix} x_\phi & x_\theta \\ y_\phi & y_\theta \end{pmatrix} d\phi\,d\theta \\
> &= \det \begin{pmatrix} -\sin\phi\sin\theta & \cos\phi\cos\theta \\ \cos\phi\sin\theta & \sin\phi\cos\theta \end{pmatrix} d\phi\,d\theta \\
> &= (-\sin^2\phi\sin\theta\cos\theta - \cos^2\phi\sin\theta\cos\theta)\,d\phi\,d\theta \\
> &= -\sin\theta\cos\theta\,d\phi\,d\theta.
> \end{aligned}
> $$
>
> **Step 3: Integrate.** Pull back the full 2-form:
>
> $$
> \mathbf{X}^*\eta = \mathbf{X}^*(z\,dx \wedge dy) = \cos\theta \cdot (-\sin\theta\cos\theta)\,d\phi\,d\theta = -\cos^2\theta\sin\theta\,d\phi\,d\theta.
> $$
>
> So:
>
> $$
> \begin{aligned}
> \iint_S \eta &= \int_0^{2\pi}\int_0^{\pi} (-\cos^2\theta\sin\theta)\,d\theta\,d\phi = -2\pi \int_0^{\pi} \cos^2\theta\sin\theta\,d\theta \\
> &= -2\pi \left[-\frac{\cos^3\theta}{3}\right]_0^{\pi} = -2\pi\left(\frac{1}{3} + \frac{1}{3}\right) = -\frac{4\pi}{3}.
> \end{aligned}
> $$
>
> **Verification.** The 2-form $\eta = z\,dx \wedge dy$ corresponds to the flux of $\mathbf{F} = (0, 0, z)$ through $S$. By the [[Divergence Theorem in ℝ³|Divergence Theorem]]: $\iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F}\,dV = \iiint_V 1\,dV = \frac{4\pi}{3}$. The sign discrepancy is because our parametrization gives the *inward* normal (check: at $\theta = \pi/2$, $\phi = 0$, i.e., at $(1, 0, 0)$, the cross product $\mathbf{X}_\phi \times \mathbf{X}_\theta = (0, 1, 0) \times (0, 0, -1) = (-1, 0, 0)$ points inward). Reversing the parameter order gives $+\frac{4\pi}{3}$. $\checkmark$

^ex-22-5

*Chain ([[Unit circle and unit sphere|unit sphere]]):* ← [[§20a The Unit Sphere and Spherical Coordinates|Chapter 6]] · [[§22b Closed and Exact Forms#^pf-22-11|§22b]] →

The following tables summarize the translation at each dimension.

**Dimension 0.** A 0-form is a function $f$. “Integrating” it means evaluating: $\int_{\{p\}} f = f(p)$. Its exterior derivative is the 1-form $df = f_x\,dx + f_y\,dy + f_z\,dz$.

**Dimension 1.** The integrals over curves:

| **Vector calculus** | **Forms expression** | **Form?** |
|---|---|---|
| $\int_a^b f'(x)\,dx$ | $\int_{[a,b]} df$ | yes: 1-form $df$ |
| $\int_\gamma f_1\,dx + f_2\,dy + f_3\,dz$ | $\int_\gamma \omega$, $\omega = f_1\,dx + f_2\,dy + f_3\,dz$ | yes: 1-form $\omega$ |
| $\int_\gamma f\,ds$ | no form expression | no (uses $\vert\boldsymbol{\gamma}'\vert$) |

The scalar line integral $\int_\gamma f\,ds$ has no form expression because $ds = |\boldsymbol{\gamma}'|\,dt$ involves an absolute value — it is intrinsically unsigned (Category 2).

**Dimension 2.** The integrals over flat regions and surfaces:

| **Vector calculus** | **Forms expression** | **Form?** |
|---|---|---|
| $\oint_{\partial D} f_1\,dx + f_2\,dy$<br>$= \iint_D \big((f_2)_x - (f_1)_y\big)\,dA$ | $\int_{\partial D} \omega = \int_D d\omega$ | Green's thm |
| $\iint_S \mathbf{F} \cdot d\mathbf{S}$ | $\iint_S \eta$, $\eta = f_{23}\,dy \wedge dz$<br>$+ \, f_{31}\,dz \wedge dx + f_{12}\,dx \wedge dy$ | yes: 2-form $\eta$ |
| $\iint_{D^*} f(\Phi)\,\vert J\vert\,du\,dv$ | no form expression (uses $\vert J\vert$) | no (Cat. 3) |
| $\iint_S f\,dS$ | no form expression (uses $\vert\mathbf{X}_u \times \mathbf{X}_v\vert$) | no (Cat. 2) |

[[Green's Theorem|Green's theorem]] is now visibly a special case of $\int_{\partial \Omega} \omega = \int_\Omega d\omega$ with $\omega$ a 1-form on $\mathbb{R}^2$ and $d\omega = \big((f_2)_x - (f_1)_y\big)\,dx \wedge dy$.

The change-of-variables integral from [[Change of Variables Formula (multiple integrals)|§15]] and the scalar surface integral both lack form expressions: the first suppresses orientation via $|J|$ (Category 3), the second is intrinsically unsigned (Category 2).

**Dimension 3.** The integral over volumes:

| **Vector calculus** | **Forms expression** | **Form?** |
|---|---|---|
| $\iint_{\partial V} \mathbf{F} \cdot \hat{n}\,dS = \iiint_V \nabla \cdot \mathbf{F}\,dV$ | $\int_{\partial V} \eta = \int_V d\eta$ | Div. thm |
| $\iiint_V f\,dx\,dy\,dz$ | $\int_V f\,dx \wedge dy \wedge dz$ | yes: 3-form |

The Divergence Theorem is $\int_{\partial V} \eta = \int_V d\eta$ with $\eta$ a 2-form and $d\eta = \big((f_{23})_x + (f_{31})_y + (f_{12})_z\big)\,dx \wedge dy \wedge dz$.

**Summary: the chain of form integrals.**

| **Dim** | **Form integral** | **$d$ connects to…** | **Theorem** |
|:-:|:-:|:-:|:-:|
| 0 | $f(p)$ | $\int_\Omega df$ (dim 1) | FTC |
| 1 | $\int_\gamma \omega$ | $\int_\Omega d\omega$ (dim 2) | Green's / Stokes' |
| 2 | $\iint_S \eta$ | $\int_\Omega d\eta$ (dim 3) | Divergence |
| 3 | $\iiint_V \mu$ | — | (top dimension) |

Each row is related to the next by the exterior derivative $d$. The integral theorems are the statement that moving down one row (applying $d$ and integrating over the region) equals staying in the current row and integrating over the boundary. This is the content of the generalized Stokes' theorem in [[Generalized Stokes' Theorem|§23]].

*Continued in [[§22b Closed and Exact Forms]]: what the exterior derivative measures, closed and exact forms, and the Poincaré lemma.*
