---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 111
stewart: "16.5"
aliases: ["Stewart 16.5"]
tags: [calculus, math233]
---
← [[§110 Green's Theorem]] · ↑ [[· 16 Vector Calculus]] · [[§112 Parametric Surfaces and Their Areas]] →

*Stewart, Section 16.5 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q2), Practice Final Set 1 (Part I, Q5), Practice Final Set 2 (Part I, Q1).*

Two operations on vector fields in $\mathbb{R}^3$ resemble differentiation. The curl, $\nabla \times \mathbf{F}$, produces a vector field and measures rotation; the divergence, $\nabla \cdot \mathbf{F}$, produces a scalar field and measures spreading out. Both are built from the operator $\nabla$, and the two identities $\operatorname{curl}(\nabla f) = \mathbf{0}$ and $\operatorname{div}(\operatorname{curl}\mathbf{F}) = 0$ give quick tests: a field with nonzero curl is not conservative, and a field with nonzero divergence is not a curl. Curl and divergence also let us rewrite Green's Theorem in two vector forms, which are the models for Stokes' Theorem ([[§114 Stokes' Theorem|§114]]) and the Divergence Theorem ([[§115 The Divergence Theorem|§115]]).

## Curl

> [!definition] Definition §111.1: Curl
> If $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ is a vector field on $\mathbb{R}^3$ and the partial derivatives of $P$, $Q$ and $R$ all exist, the **curl** of $\mathbf{F}$ is the vector field on $\mathbb{R}^3$ defined by
>
> $$
> \operatorname{curl}\mathbf{F} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)\mathbf{i} + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)\mathbf{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\mathbf{k} . \qquad (1)
> $$
>
> With the vector differential operator $\nabla$ ("del"),
>
> $$
> \nabla = \mathbf{i}\,\frac{\partial}{\partial x} + \mathbf{j}\,\frac{\partial}{\partial y} + \mathbf{k}\,\frac{\partial}{\partial z} ,
> $$
>
> which produces the gradient $\nabla f = \frac{\partial f}{\partial x}\mathbf{i} + \frac{\partial f}{\partial y}\mathbf{j} + \frac{\partial f}{\partial z}\mathbf{k}$ when it operates on a scalar function, the curl is the formal cross product
>
> $$
> \operatorname{curl}\mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] P & Q & R \end{vmatrix} . \qquad (2)
> $$
>
> Expanding the determinant along the first row gives (1).
>
> *Stewart: 16.5, Definition 1 and Equation 2*

^def-111-1

> [!remark]- Connections
> - The same definition in 452: [[§16 Line Integrals and Green's Theorem#^def-16-5|452 Def. §16.5]] (first introduced in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §11]]). In the language of forms, the curl is the exterior derivative of a 1-form: [[§22 The Algebra of Differential Forms#^prop-22-3|452 Prop. §22.3]].

> [!theorem] Theorem §111.1: The Curl of a Gradient Is Zero
> If $f$ is a function of three variables that has continuous second-order partial derivatives, then
>
> $$
> \operatorname{curl}(\nabla f) = \mathbf{0} .
> $$
>
> *Stewart: 16.5, Theorem 3*

^thm-111-1

> [!proof]+ Proof
> $$
> \operatorname{curl}(\nabla f) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] \dfrac{\partial f}{\partial x} & \dfrac{\partial f}{\partial y} & \dfrac{\partial f}{\partial z} \end{vmatrix}
> = \left( \frac{\partial^2 f}{\partial y\,\partial z} - \frac{\partial^2 f}{\partial z\,\partial y} \right)\mathbf{i} + \left( \frac{\partial^2 f}{\partial z\,\partial x} - \frac{\partial^2 f}{\partial x\,\partial z} \right)\mathbf{j} + \left( \frac{\partial^2 f}{\partial x\,\partial y} - \frac{\partial^2 f}{\partial y\,\partial x} \right)\mathbf{k} = \mathbf{0}
> $$
>
> by Clairaut's Theorem ([[§92 Partial Derivatives#^thm-92-2|Theorem §92.2]]), since the second-order partial derivatives are continuous. (Compare $\mathbf{a} \times \mathbf{a} = \mathbf{0}$ for vectors, [[§83 The Cross Product#^ex-83-1|Example §83.1]].)

^pf-111-1

*Uses:* [[§111 Curl and Divergence#^def-111-1|Def. §111.1]], [[§92 Partial Derivatives#^thm-92-2|§92.2]]

> [!theorem] Corollary §111.2: Conservative Fields Are Curl-Free
> If $\mathbf{F}$ is conservative (with a potential function whose second-order partial derivatives are continuous), then $\operatorname{curl}\mathbf{F} = \mathbf{0}$. Equivalently: if $\operatorname{curl}\mathbf{F} \ne \mathbf{0}$, then $\mathbf{F}$ is not conservative.
>
> *Stewart: 16.5 (text)*

^cor-111-2

> [!proof]+ Proof
> If $\mathbf{F} = \nabla f$, then $\operatorname{curl}\mathbf{F} = \operatorname{curl}(\nabla f) = \mathbf{0}$ by [[§111 Curl and Divergence#^thm-111-1|Theorem §111.1]]. The second sentence is the [[Contrapositive, Converse and Inverse|contrapositive]].

^pf-111-2

*Uses:* [[§111 Curl and Divergence#^thm-111-1|§111.1]], [[§107 Vector Fields#^def-107-4|Def. §107.4]]

This is the three-dimensional form of [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Theorem §109.4]]: for a plane field $P\,\mathbf{i} + Q\,\mathbf{j}$ the curl is $(\partial Q/\partial x - \partial P/\partial y)\,\mathbf{k}$. The converse is not true in general, but Stewart states (16.5, Theorem 4) that it holds when $\mathbf{F}$ is defined everywhere: *if $\mathbf{F}$ is a vector field defined on all of $\mathbb{R}^3$ whose component functions have continuous partial derivatives and $\operatorname{curl}\mathbf{F} = \mathbf{0}$, then $\mathbf{F}$ is conservative.* (More generally it holds if the domain is simply-connected ([[§23 The Fundamental Group#^def-23-3|590 Def. §23.3]]), that is, "has no hole".) This is the three-dimensional version of [[§110 Green's Theorem#^thm-110-5|Theorem §110.5]]. Its proof requires Stokes' Theorem, so it is stated and proved there: [[§114 Stokes' Theorem#^thm-114-4|Theorem §114.4]].

> [!definition] Definition §111.2: Irrotational
> If $\operatorname{curl}\mathbf{F} = \mathbf{0}$ at a point $P$, then $\mathbf{F}$ is called **irrotational** at $P$.
>
> The name *curl* comes from rotation. If $\mathbf{F}$ is the velocity field of a fluid, particles near $(x, y, z)$ tend to rotate about the axis that points in the direction of $\operatorname{curl}\mathbf{F}(x, y, z)$, following the right-hand rule, and the length of the curl vector measures how quickly they move around the axis (this is made precise in [[§114 Stokes' Theorem#^thm-114-3|Theorem §114.3]]). If $\mathbf{F}$ is irrotational at $P$, the fluid is free from rotations there: a tiny paddle wheel placed at $P$ moves with the fluid but does not rotate about its axis. If $\operatorname{curl}\mathbf{F} \ne \mathbf{0}$, the paddle wheel rotates about its axis.
>
> For example, for $\mathbf{F}(x, y, z) = \sin y\,\mathbf{i} + \cos x\,\mathbf{j}$, $\operatorname{curl}\mathbf{F} = -(\sin x + \cos y)\,\mathbf{k}$, nonzero at most points: a paddle wheel spins counterclockwise where $\sin x + \cos y < 0$ (the curl points along $\mathbf{k}$) and clockwise where $\sin x + \cos y > 0$. For $\mathbf{F}(x, y, z) = 2xy\,\mathbf{i} + (x^2 + y)\,\mathbf{j}$, $\operatorname{curl}\mathbf{F} = (2x - 2x)\,\mathbf{k} = \mathbf{0}$ everywhere.
>
> *Stewart: 16.5 (text)*

^def-111-2

## Divergence

> [!definition] Definition §111.3: Divergence
> If $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ is a vector field on $\mathbb{R}^3$ and $\partial P/\partial x$, $\partial Q/\partial y$, $\partial R/\partial z$ exist, the **divergence** of $\mathbf{F}$ is the function of three variables
>
> $$
> \operatorname{div}\mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} . \qquad (9)
> $$
>
> In terms of $\nabla$ it is the formal dot product
>
> $$
> \operatorname{div}\mathbf{F} = \nabla \cdot \mathbf{F} . \qquad (10)
> $$
>
> If $\mathbf{F}$ is a vector field on $\mathbb{R}^2$, $\operatorname{div}\mathbf{F}$ is defined similarly as a function of two variables. Note that $\operatorname{curl}\mathbf{F}$ is a vector field but $\operatorname{div}\mathbf{F}$ is a scalar field.
>
> *Stewart: 16.5, Equations 9 and 10*

^def-111-3

> [!theorem] Theorem §111.3: The Divergence of a Curl Is Zero
> If $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ is a vector field on $\mathbb{R}^3$ and $P$, $Q$, $R$ have continuous second-order partial derivatives, then
>
> $$
> \operatorname{div}\operatorname{curl}\mathbf{F} = 0 .
> $$
>
> *Stewart: 16.5, Theorem 11*

^thm-111-3

> [!proof]+ Proof
> By Definitions §111.1 and §111.3,
>
> $$
> \begin{aligned}
> \operatorname{div}\operatorname{curl}\mathbf{F} = \nabla \cdot (\nabla \times \mathbf{F}) &= \frac{\partial}{\partial x}\left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right) + \frac{\partial}{\partial y}\left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right) + \frac{\partial}{\partial z}\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \\
> &= \frac{\partial^2 R}{\partial x\,\partial y} - \frac{\partial^2 Q}{\partial x\,\partial z} + \frac{\partial^2 P}{\partial y\,\partial z} - \frac{\partial^2 R}{\partial y\,\partial x} + \frac{\partial^2 Q}{\partial z\,\partial x} - \frac{\partial^2 P}{\partial z\,\partial y} = 0 ,
> \end{aligned}
> $$
>
> because the terms cancel in pairs by Clairaut's Theorem ([[§92 Partial Derivatives#^thm-92-2|Theorem §92.2]]). (Compare the scalar triple product $\mathbf{a} \cdot (\mathbf{a} \times \mathbf{b}) = 0$, [[§83 The Cross Product#^thm-83-2|Theorem §83.2]].)

^pf-111-3

*Uses:* [[§111 Curl and Divergence#^def-111-1|Def. §111.1]], [[§111 Curl and Divergence#^def-111-3|Def. §111.3]], [[§92 Partial Derivatives#^thm-92-2|§92.2]]

> [!remark]- Connections
> - Both identities, $\operatorname{curl}(\nabla f) = \mathbf{0}$ and $\operatorname{div}(\operatorname{curl}\mathbf{F}) = 0$, are proved the same way in [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §11]], and become the single identity $d^2 = 0$ for differential forms: [[§22 The Algebra of Differential Forms#^thm-22-5|452 Thm. §22.5]] (hub [[Exterior Derivative Squares to Zero]]), which is Clairaut's theorem in disguise, [[§22 The Algebra of Differential Forms#^prop-22-9|452 Prop. §22.9]].

So if $\operatorname{div}\mathbf{F} \ne 0$, then $\mathbf{F}$ is not the curl of another vector field.

> [!definition] Definition §111.4: Incompressible
> If $\operatorname{div}\mathbf{F} = 0$, then $\mathbf{F}$ is said to be **incompressible**.
>
> The name *divergence* comes from fluid flow. If $\mathbf{F}(x, y, z)$ is the velocity of a fluid (or gas), then $\operatorname{div}\mathbf{F}(x, y, z)$ represents the net rate of change (with respect to time) of the mass of fluid flowing from the point $(x, y, z)$ per unit volume: it measures the tendency of the fluid to diverge from the point (made precise in [[§115 The Divergence Theorem#^thm-115-3|Theorem §115.3]]). For example, $\mathbf{F}(x, y, z) = (1 + x^2)\,\mathbf{i} + y\,\mathbf{j}$ has $\operatorname{div}\mathbf{F} = 2x + 1$: the flow is outward (the arrows starting near a point are longer than those ending there) where $x > -\frac12$, and inward where $x < -\frac12$. The field $\mathbf{F}(x, y, z) = -x\,\mathbf{i} + y\,\mathbf{j}$ has $\operatorname{div}\mathbf{F} = -1 + 1 = 0$ everywhere.
>
> *Stewart: 16.5 (text)*

^def-111-4

> [!example] Example §111.1: Curl and Divergence of One Field
> Let $\mathbf{F}(x, y, z) = xz\,\mathbf{i} + xyz\,\mathbf{j} - y^2\,\mathbf{k}$.
>
> **The curl.** By (2),
>
> $$
> \begin{aligned}
> \operatorname{curl}\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] xz & xyz & -y^2 \end{vmatrix}
> &= \left[ \frac{\partial}{\partial y}(-y^2) - \frac{\partial}{\partial z}(xyz) \right]\mathbf{i} - \left[ \frac{\partial}{\partial x}(-y^2) - \frac{\partial}{\partial z}(xz) \right]\mathbf{j} + \left[ \frac{\partial}{\partial x}(xyz) - \frac{\partial}{\partial y}(xz) \right]\mathbf{k} \\
> &= (-2y - xy)\,\mathbf{i} - (0 - x)\,\mathbf{j} + (yz - 0)\,\mathbf{k} = -y(2 + x)\,\mathbf{i} + x\,\mathbf{j} + yz\,\mathbf{k} .
> \end{aligned}
> $$
>
> Since $\operatorname{curl}\mathbf{F} \ne \mathbf{0}$, $\mathbf{F}$ is **not conservative**, by [[§111 Curl and Divergence#^cor-111-2|Corollary §111.2]].
>
> **The divergence.** By (9),
>
> $$
> \operatorname{div}\mathbf{F} = \frac{\partial}{\partial x}(xz) + \frac{\partial}{\partial y}(xyz) + \frac{\partial}{\partial z}(-y^2) = z + xz .
> $$
>
> Since $\operatorname{div}\mathbf{F} \ne 0$, $\mathbf{F}$ **is not the curl of another vector field**: if $\mathbf{F} = \operatorname{curl}\mathbf{G}$, then [[§111 Curl and Divergence#^thm-111-3|Theorem §111.3]] would give $\operatorname{div}\mathbf{F} = \operatorname{div}\operatorname{curl}\mathbf{G} = 0$.
>
> *Stewart: Examples 16.5.1, 16.5.2, 16.5.4 and 16.5.5*

^ex-111-1

> [!example] Example §111.2: A Conservative Field in Space
> Let $\mathbf{F}(x, y, z) = y^2 z^3\,\mathbf{i} + 2xyz^3\,\mathbf{j} + 3xy^2z^2\,\mathbf{k}$. (a) Show that $\mathbf{F}$ is conservative. (b) Find a function $f$ such that $\mathbf{F} = \nabla f$. (c) Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ for the curve $\mathbf{r}(t) = t^{300}\,\mathbf{i} + t\ln(t^3 + t + 8)\,\mathbf{j} + t\,\mathbf{k}$, $0 \le t \le 1$.
>
> **(a)**
>
> $$
> \operatorname{curl}\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] y^2z^3 & 2xyz^3 & 3xy^2z^2 \end{vmatrix} = (6xyz^2 - 6xyz^2)\,\mathbf{i} - (3y^2z^2 - 3y^2z^2)\,\mathbf{j} + (2yz^3 - 2yz^3)\,\mathbf{k} = \mathbf{0} .
> $$
>
> The domain of $\mathbf{F}$ is all of $\mathbb{R}^3$ and its components are polynomials, so $\mathbf{F}$ is conservative by [[§114 Stokes' Theorem#^thm-114-4|Theorem §114.4]].
>
> **(b)** Following [[§109 The Fundamental Theorem for Line Integrals#^rem-109-1|the method of §109]], we need
>
> $$
> f_x = y^2z^3, \qquad (5) \qquad f_y = 2xyz^3, \qquad (6) \qquad f_z = 3xy^2z^2 . \qquad (7)
> $$
>
> Integrating (5) with respect to $x$: $f(x, y, z) = xy^2z^3 + g(y, z)$. Then $f_y = 2xyz^3 + g_y(y, z)$, and comparison with (6) gives $g_y(y, z) = 0$, so $g(y, z) = h(z)$. Then $f_z = 3xy^2z^2 + h'(z)$, and (7) gives $h'(z) = 0$. Therefore
>
> $$
> f(x, y, z) = xy^2z^3 + K .
> $$
>
> **(c)** By the Fundamental Theorem for Line Integrals ([[§109 The Fundamental Theorem for Line Integrals#^thm-109-1|Theorem §109.1]]) only the endpoints matter: $\mathbf{r}(0) = (0, 0, 0)$ and $\mathbf{r}(1) = (1, \ln 10, 1)$. So
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = f(1, \ln 10, 1) - f(0, 0, 0) = (\ln 10)^2 .
> $$
>
> (The complicated parametrization is a decoy: nothing about $C$ but its endpoints enters.)
>
> *Stewart: Example 16.5.3*
> *Source: 233 Chapter 16 Review, Q2*

^ex-111-2

> [!example] Example §111.3: Which Field Is Conservative?
> Determine which of the following vector fields is conservative: (a) $\langle -y, x, 0 \rangle$, (b) $\langle xy, yz, zx \rangle$, (c) $\langle 2xy,\ x^2 + 2yz,\ y^2 \rangle$, (d) $\langle y^2, z^2, x^2 \rangle$, (e) $\langle x^2y, y^2z, z^2x \rangle$, (f) $\langle x, x, x \rangle$.
>
> By [[§111 Curl and Divergence#^cor-111-2|Corollary §111.2]], any field with nonzero curl is disqualified. From (1):
>
> | field | $\operatorname{curl}\mathbf{F}$ |
> |---|---|
> | (a) $\langle -y, x, 0 \rangle$ | $\langle 0, 0, 2 \rangle$ |
> | (b) $\langle xy, yz, zx \rangle$ | $\langle -y, -z, -x \rangle$ |
> | (c) $\langle 2xy,\ x^2 + 2yz,\ y^2 \rangle$ | $\langle 2y - 2y,\ 0 - 0,\ 2x - 2x \rangle = \mathbf{0}$ |
> | (d) $\langle y^2, z^2, x^2 \rangle$ | $\langle -2z, -2x, -2y \rangle$ |
> | (e) $\langle x^2y, y^2z, z^2x \rangle$ | $\langle -y^2, -z^2, -x^2 \rangle$ |
> | (f) $\langle x, x, x \rangle$ | $\langle 0, -1, 1 \rangle$ |
>
> Only (c) can be conservative, and it is: its domain is $\mathbb{R}^3$ ([[§114 Stokes' Theorem#^thm-114-4|Theorem §114.4]]), and indeed $f(x, y, z) = x^2y + y^2z$ has $\nabla f = \langle 2xy,\ x^2 + 2yz,\ y^2 \rangle$. (Field (a) is the rotation field of [[§107 Vector Fields#^ex-107-1|Example §107.1]] with a zero third component; its curl $2\mathbf{k}$ is twice its angular velocity.)
>
> *Source: 233 Practice Final Set 2, Part I Q1*

^ex-111-3

> [!example] Example §111.4: A Product Rule for the Divergence
> Let $f(x, y, z)$ be a differentiable function and $\mathbf{F}(x, y, z)$ a differentiable vector field on $\mathbb{R}^3$. Then
>
> $$
> \operatorname{div}(f\mathbf{F}) = f\operatorname{div}\mathbf{F} + \mathbf{F} \cdot \nabla f .
> $$
>
> Write $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$, so $f\mathbf{F} = fP\,\mathbf{i} + fQ\,\mathbf{j} + fR\,\mathbf{k}$. By the Product Rule in each variable,
>
> $$
> \begin{aligned}
> \operatorname{div}(f\mathbf{F}) &= \frac{\partial}{\partial x}(fP) + \frac{\partial}{\partial y}(fQ) + \frac{\partial}{\partial z}(fR) = f\frac{\partial P}{\partial x} + P\frac{\partial f}{\partial x} + f\frac{\partial Q}{\partial y} + Q\frac{\partial f}{\partial y} + f\frac{\partial R}{\partial z} + R\frac{\partial f}{\partial z} \\
> &= f\left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) + \left( P\frac{\partial f}{\partial x} + Q\frac{\partial f}{\partial y} + R\frac{\partial f}{\partial z} \right) = f\operatorname{div}\mathbf{F} + \mathbf{F} \cdot \nabla f .
> \end{aligned}
> $$
>
> In the multiple-choice version, the competing formulas fail on types alone: $f\operatorname{curl}\mathbf{F}$ and $\mathbf{F} \times \nabla f$ are vectors, while $\operatorname{div}(f\mathbf{F})$ is a scalar; $f\operatorname{div}\mathbf{F} + \mathbf{F} \cdot \nabla f$ is a scalar, while $\operatorname{curl}(f\mathbf{F})$ is a vector. (The correct curl rule is $\operatorname{curl}(f\mathbf{F}) = f\operatorname{curl}\mathbf{F} + \nabla f \times \mathbf{F}$, by the same computation.)
>
> *Source: 233 Practice Final Set 1, Part I Q5*

^ex-111-4

> [!definition] Definition §111.5: Laplace Operator
> For a function $f$ of three variables,
>
> $$
> \operatorname{div}(\nabla f) = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2} ,
> $$
>
> abbreviated $\nabla^2 f$. The operator $\nabla^2 = \nabla \cdot \nabla$ is called the **Laplace operator**, because of its relation to **Laplace's equation**
>
> $$
> \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2} = 0 .
> $$
>
> On a vector field $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ it acts componentwise: $\nabla^2\mathbf{F} = \nabla^2 P\,\mathbf{i} + \nabla^2 Q\,\mathbf{j} + \nabla^2 R\,\mathbf{k}$.
>
> *Stewart: 16.5 (text)*

^def-111-5

## Vector Forms of Green's Theorem

Let the plane region $D$, its boundary curve $C$ and the functions $P$, $Q$ satisfy the hypotheses of Green's Theorem ([[§110 Green's Theorem#^thm-110-1|Theorem §110.1]]), and let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$.

> [!theorem] Theorem §111.4: Green's Theorem, Tangential Form
> $$
> \oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C \mathbf{F} \cdot \mathbf{T}\,ds = \iint_D (\operatorname{curl}\mathbf{F}) \cdot \mathbf{k}\,dA . \qquad (12)
> $$
>
> The line integral of the tangential component of $\mathbf{F}$ along $C$ equals the double integral of the vertical component of $\operatorname{curl}\mathbf{F}$ over $D$.
>
> *Stewart: 16.5, Equation 12*

^thm-111-4

> [!proof]+ Proof
> Regard $\mathbf{F}$ as a vector field on $\mathbb{R}^3$ with third component $0$. Since $P$ and $Q$ do not depend on $z$,
>
> $$
> \operatorname{curl}\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] P(x, y) & Q(x, y) & 0 \end{vmatrix} = \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\mathbf{k}, \qquad\text{so}\qquad (\operatorname{curl}\mathbf{F}) \cdot \mathbf{k} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} .
> $$
>
> On the other hand $\oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C P\,dx + Q\,dy$ ([[§108 Line Integrals#^thm-108-7|Theorem §108.7]]), and $\oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C \mathbf{F} \cdot \mathbf{T}\,ds$ by [[§108 Line Integrals#^def-108-8|Definition §108.8]]. So (12) is exactly Green's Theorem.

^pf-111-4

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§111 Curl and Divergence#^def-111-1|Def. §111.1]], [[§108 Line Integrals#^thm-108-7|§108.7]], [[§108 Line Integrals#^def-108-8|Def. §108.8]]

Equation 12 is the planar model of Stokes' Theorem ([[§114 Stokes' Theorem#^thm-114-1|Theorem §114.1]]). A similar formula holds for the *normal* component of $\mathbf{F}$.

> [!theorem] Theorem §111.5: Green's Theorem, Normal Form
> If $\mathbf{n}$ is the outward unit normal vector to $C$, then
>
> $$
> \oint_C \mathbf{F} \cdot \mathbf{n}\,ds = \iint_D \operatorname{div}\mathbf{F}(x, y)\,dA . \qquad (13)
> $$
>
> The line integral of the normal component of $\mathbf{F}$ along $C$ equals the double integral of the divergence of $\mathbf{F}$ over $D$.
>
> *Stewart: 16.5, Equation 13*

^thm-111-5

> [!proof]+ Proof
> Let $C$ be given by $\mathbf{r}(t) = x(t)\,\mathbf{i} + y(t)\,\mathbf{j}$, $a \le t \le b$, positively oriented. The unit tangent vector is
>
> $$
> \mathbf{T}(t) = \frac{x'(t)}{|\mathbf{r}'(t)|}\,\mathbf{i} + \frac{y'(t)}{|\mathbf{r}'(t)|}\,\mathbf{j}, \qquad\text{and}\qquad \mathbf{n}(t) = \frac{y'(t)}{|\mathbf{r}'(t)|}\,\mathbf{i} - \frac{x'(t)}{|\mathbf{r}'(t)|}\,\mathbf{j}
> $$
>
> is the outward unit normal. (Stewart leaves this to the reader; here is why: $\mathbf{n}$ is a unit vector with $\mathbf{n} \cdot \mathbf{T} = 0$, obtained by rotating $\mathbf{T}$ clockwise through $90^\circ$. So it points to the right of the direction of travel. Since $D$ lies on the left of the positively oriented curve, the right side is the outside.) By Formula 3 of [[§108 Line Integrals#^thm-108-1|Theorem §108.1]] ($ds = |\mathbf{r}'(t)|\,dt$),
>
> $$
> \begin{aligned}
> \oint_C \mathbf{F} \cdot \mathbf{n}\,ds &= \int_a^b (\mathbf{F} \cdot \mathbf{n})(t)\,|\mathbf{r}'(t)|\,dt = \int_a^b \left[ \frac{P(x(t), y(t))\,y'(t)}{|\mathbf{r}'(t)|} - \frac{Q(x(t), y(t))\,x'(t)}{|\mathbf{r}'(t)|} \right] |\mathbf{r}'(t)|\,dt \\
> &= \int_a^b \big[ P(x(t), y(t))\,y'(t) - Q(x(t), y(t))\,x'(t) \big]\,dt = \oint_C P\,dy - Q\,dx = \iint_D \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} \right) dA ,
> \end{aligned}
> $$
>
> where the last step is Green's Theorem applied to the pair $-Q$ (coefficient of $dx$) and $P$ (coefficient of $dy$): $\frac{\partial P}{\partial x} - \frac{\partial(-Q)}{\partial y} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}$. The integrand is $\operatorname{div}\mathbf{F}$.

^pf-111-5

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§111 Curl and Divergence#^def-111-3|Def. §111.3]], [[§108 Line Integrals#^thm-108-1|§108.1]], [[§108 Line Integrals#^thm-108-2|§108.2]], [[§110 Green's Theorem#^def-110-1|Def. §110.1]]

![[m233-111-1.svg]]
*The two vector forms of Green's Theorem at a boundary point. $\mathbf{T}$ (blue) is the unit tangent in the positive direction, with $D$ on its left; $\mathbf{n}$ (red) is $\mathbf{T}$ turned clockwise by $90^\circ$ and points out of $D$. Integrating $\mathbf{F}\cdot\mathbf{T}$ around $C$ measures circulation and gives $\iint_D (\operatorname{curl}\mathbf{F})\cdot\mathbf{k}\,dA$ (12); integrating $\mathbf{F}\cdot\mathbf{n}$ measures outflow and gives $\iint_D \operatorname{div}\mathbf{F}\,dA$ (13).*

> [!remark]- Connections
> - Both forms are in 452: the normal form is the divergence theorem in the plane, [[§16 Line Integrals and Green's Theorem#^thm-16-2|452 Thm. §16.2]], and the tangential form is [[§16 Line Integrals and Green's Theorem#^thm-16-3|452 Thm. §16.3]]; [[§16 Line Integrals and Green's Theorem#^rem-16-4|452 Remark: Two Faces of Green's Theorem]] sets them side by side. In space they become the Divergence Theorem ([[§115 The Divergence Theorem#^thm-115-1|Theorem §115.1]]) and Stokes' Theorem ([[§114 Stokes' Theorem#^thm-114-1|Theorem §114.1]]).
> - See also: [[§125★ The Stream Function#^prop-125-2|342 Prop. §125.2]] (the stream function of a plane flow as the flux across a curve).
