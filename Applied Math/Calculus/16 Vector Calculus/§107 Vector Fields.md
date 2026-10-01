---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 107
stewart: "16.1"
aliases: ["Stewart 16.1"]
tags: [calculus, math233]
---
← [[§106 Change of Variables in Multiple Integrals]] · ↑ [[· 16 Vector Calculus]] · [[§108 Line Integrals]] →

*Stewart, Section 16.1 · MATH 233 (UMass, Spring 2023): Practice Final Set 2 (Part I, Q4).*

A vector field attaches a vector to every point of a region: the wind velocity at each point of the air, the gravitational force at each point of space. Vector fields are the objects that the rest of this chapter integrates, along curves ([[§108 Line Integrals|§108]]) and across surfaces ([[§113 Surface Integrals|§113]]). The most important ones are gradients of scalar functions. A field that is a gradient is called conservative, and recognizing conservative fields and finding their potential functions is the theme of [[§109 The Fundamental Theorem for Line Integrals|§109]] and [[§111 Curl and Divergence|§111]].

## Vector Fields in ℝ² and ℝ³

> [!definition] Definition §107.1: Vector Field on ℝ²
> Let $D$ be a set in $\mathbb{R}^2$ (a plane region). A **vector field on $\mathbb{R}^2$** is a function $\mathbf{F}$ that assigns to each point $(x, y)$ in $D$ a two-dimensional vector $\mathbf{F}(x, y)$.
>
> Writing $\mathbf{F}(x, y)$ in terms of its **component functions** $P$ and $Q$,
>
> $$
> \mathbf{F}(x, y) = P(x, y)\,\mathbf{i} + Q(x, y)\,\mathbf{j} = \langle P(x, y), Q(x, y) \rangle, \qquad\text{or for short}\qquad \mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} .
> $$
>
> $P$ and $Q$ are scalar functions of two variables, sometimes called **scalar fields** to distinguish them from vector fields.
>
> *Stewart: 16.1, Definition 1*

^def-107-1

To picture $\mathbf{F}$, draw the arrow representing $\mathbf{F}(x, y)$ starting at the point $(x, y)$, for a selection of representative points.

> [!definition] Definition §107.2: Vector Field on ℝ³
> Let $E$ be a subset of $\mathbb{R}^3$. A **vector field on $\mathbb{R}^3$** is a function $\mathbf{F}$ that assigns to each point $(x, y, z)$ in $E$ a three-dimensional vector $\mathbf{F}(x, y, z)$. In terms of its component functions $P$, $Q$, $R$,
>
> $$
> \mathbf{F}(x, y, z) = P(x, y, z)\,\mathbf{i} + Q(x, y, z)\,\mathbf{j} + R(x, y, z)\,\mathbf{k} .
> $$
>
> As for vector functions ([[§86 Vector Functions and Space Curves|§86]]), $\mathbf{F}$ is **continuous** if and only if its component functions $P$, $Q$, $R$ are continuous. Identifying the point $(x, y, z)$ with its position vector $\mathbf{x} = \langle x, y, z \rangle$, we also write $\mathbf{F}(\mathbf{x})$ for $\mathbf{F}(x, y, z)$.
>
> *Stewart: 16.1, Definition 2*

^def-107-2

> [!example] Example §107.1: The Rotation Field
> Describe the vector field $\mathbf{F}(x, y) = -y\,\mathbf{i} + x\,\mathbf{j}$ by sketching some of its vectors.
>
> $\mathbf{F}(1, 0) = \mathbf{j} = \langle 0, 1 \rangle$, so we draw $\langle 0, 1 \rangle$ starting at $(1, 0)$; $\mathbf{F}(0, 1) = -\mathbf{i} = \langle -1, 0 \rangle$ is drawn starting at $(0, 1)$. Some more values:
>
> | $(x, y)$ | $\mathbf{F}(x, y)$ | $(x, y)$ | $\mathbf{F}(x, y)$ |
> |---|---|---|---|
> | $(1, 0)$ | $\langle 0, 1 \rangle$ | $(-1, 0)$ | $\langle 0, -1 \rangle$ |
> | $(2, 2)$ | $\langle -2, 2 \rangle$ | $(-2, -2)$ | $\langle 2, -2 \rangle$ |
> | $(3, 0)$ | $\langle 0, 3 \rangle$ | $(-3, 0)$ | $\langle 0, -3 \rangle$ |
> | $(0, 1)$ | $\langle -1, 0 \rangle$ | $(0, -1)$ | $\langle 1, 0 \rangle$ |
> | $(-2, 2)$ | $\langle -2, -2 \rangle$ | $(2, -2)$ | $\langle 2, 2 \rangle$ |
> | $(0, 3)$ | $\langle -3, 0 \rangle$ | $(0, -3)$ | $\langle 3, 0 \rangle$ |
>
> Each arrow appears tangent to a circle centered at the origin. To confirm this, dot $\mathbf{F}$ with the position vector $\mathbf{x} = x\,\mathbf{i} + y\,\mathbf{j}$:
>
> $$
> \mathbf{x} \cdot \mathbf{F}(\mathbf{x}) = (x\,\mathbf{i} + y\,\mathbf{j}) \cdot (-y\,\mathbf{i} + x\,\mathbf{j}) = -xy + yx = 0 .
> $$
>
> So $\mathbf{F}(x, y)$ is perpendicular to $\langle x, y \rangle$, hence tangent to the circle with center the origin and radius $|\mathbf{x}| = \sqrt{x^2 + y^2}$. Moreover
>
> $$
> |\mathbf{F}(x, y)| = \sqrt{(-y)^2 + x^2} = \sqrt{x^2 + y^2} = |\mathbf{x}| ,
> $$
>
> so the length of the arrow equals the radius of the circle. The field turns counterclockwise, faster farther out: it is the velocity field of a wheel rotating counterclockwise with angular speed $1$.
>
> *Stewart: Example 16.1.1*

^ex-107-1

![[m233-107-1.svg]]
*The rotation field $\mathbf{F} = -y\,\mathbf{i} + x\,\mathbf{j}$ (arrows scaled down). Every arrow is tangent to a circle about the origin (gray) and as long as that circle's radius, so the field circulates counterclockwise and grows linearly with distance. This field returns throughout the chapter: it is not conservative, since $\partial P/\partial y = -1 \ne 1 = \partial Q/\partial x$ ([[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Theorem §109.4]]), and its curl is $2\mathbf{k}$ ([[§111 Curl and Divergence#^ex-111-3|Example §111.3]]).*

> [!example] Example §107.2: Force Fields from Inverse Square Laws
> **Gravitation.** Newton's Law of Gravitation says that the magnitude of the gravitational force between two objects with masses $m$ and $M$ is $|\mathbf{F}| = mMG/r^2$, where $r$ is the distance between them and $G$ is the gravitational constant. Put the object of mass $M$ at the origin and let $\mathbf{x} = \langle x, y, z \rangle$ be the position vector of the object of mass $m$. Then $r = |\mathbf{x}|$, and the force on the second object points toward the origin, in the direction of the unit vector $-\mathbf{x}/|\mathbf{x}|$. So the **gravitational field** is
>
> $$
> \mathbf{F}(\mathbf{x}) = -\frac{mMG}{|\mathbf{x}|^3}\,\mathbf{x} \qquad (3)
> $$
>
> (physicists write $\mathbf{F} = -(mMG/r^3)\,\mathbf{r}$), or in components, using $|\mathbf{x}| = \sqrt{x^2 + y^2 + z^2}$,
>
> $$
> \mathbf{F}(x, y, z) = \frac{-mMGx}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{i} + \frac{-mMGy}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{j} + \frac{-mMGz}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{k} .
> $$
>
> All its arrows point toward the origin and grow as they approach it.
>
> **Electrostatics.** By Coulomb's Law, a charge $Q$ at the origin exerts on a charge $q$ at $\mathbf{x}$ the electric force
>
> $$
> \mathbf{F}(\mathbf{x}) = \frac{\varepsilon q Q}{|\mathbf{x}|^3}\,\mathbf{x} \qquad (4)
> $$
>
> where $\varepsilon$ is a constant that depends on the units. For like charges $qQ > 0$ and the force is repulsive; for unlike charges $qQ < 0$ and it is attractive. Fields (3) and (4) are examples of **force fields**. The force per unit charge,
>
> $$
> \mathbf{E}(\mathbf{x}) = \frac{1}{q}\,\mathbf{F}(\mathbf{x}) = \frac{\varepsilon Q}{|\mathbf{x}|^3}\,\mathbf{x} ,
> $$
>
> is a vector field on $\mathbb{R}^3$ called the **electric field** of $Q$.
>
> *Stewart: Examples 16.1.4 and 16.1.5*

^ex-107-2

## Gradient Fields

> [!definition] Definition §107.3: Gradient Vector Field
> If $f$ is a scalar function of two variables, its gradient ([[§95 Directional Derivatives and the Gradient Vector|§95]])
>
> $$
> \nabla f(x, y) = f_x(x, y)\,\mathbf{i} + f_y(x, y)\,\mathbf{j}
> $$
>
> is a vector field on $\mathbb{R}^2$, called a **gradient vector field**. Likewise, if $f$ is a scalar function of three variables, its gradient is a vector field on $\mathbb{R}^3$:
>
> $$
> \nabla f(x, y, z) = f_x(x, y, z)\,\mathbf{i} + f_y(x, y, z)\,\mathbf{j} + f_z(x, y, z)\,\mathbf{k} .
> $$
>
> *Stewart: 16.1 (text)*

^def-107-3

> [!example] Example §107.3: Gradient Fields and Level Curves
> **(a)** The gradient vector field of $f(x, y) = x^2 y - y^3$ is
>
> $$
> \nabla f(x, y) = \frac{\partial f}{\partial x}\,\mathbf{i} + \frac{\partial f}{\partial y}\,\mathbf{j} = 2xy\,\mathbf{i} + (x^2 - 3y^2)\,\mathbf{j} .
> $$
>
> Plotted together with a contour map of $f$, the gradient vectors are perpendicular to the level curves, as they must be ([[§95 Directional Derivatives and the Gradient Vector|§95]]). They are long where the level curves are close together and short where the curves are far apart: the length $|\nabla f|$ is the maximum directional derivative of $f$, and closely spaced level curves mean a steep graph. (For instance, at the origin $\nabla f = \mathbf{0}$, and there the level curve $f = 0$, which is the three lines $y = 0$, $y = \pm x$, crosses itself.)
>
> **(b)** The value at $(1, 1)$ of the gradient vector field of $z = x^2 y^3$: since $\nabla z = \langle 2xy^3,\ 3x^2y^2 \rangle$,
>
> $$
> \nabla z(1, 1) = \langle 2 \cdot 1 \cdot 1^3,\ 3 \cdot 1^2 \cdot 1^2 \rangle = \langle 2, 3 \rangle .
> $$
>
> *Stewart: Example 16.1.6*
> *Source: 233 Practice Final Set 2, Part I Q4*

^ex-107-3

> [!definition] Definition §107.4: Conservative Vector Field
> A vector field $\mathbf{F}$ is called a **conservative vector field** if it is the gradient of some scalar function, that is, if there exists a function $f$ such that $\mathbf{F} = \nabla f$. In this situation $f$ is called a **potential function** for $\mathbf{F}$.
>
> *Stewart: 16.1 (text)*

^def-107-4

> [!remark]- Connections
> - Same definition in 452 (with "irrotational" and "solenoidal" alongside): [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence#^def-11-1|452 Def. §11.1]]. In the language of differential forms a conservative field is an exact 1-form: [[§22 The Algebra of Differential Forms#^def-22-8|452 Def. §22.8]], with the gradient as the differential [[§22 The Algebra of Differential Forms#^prop-22-6|452 Prop. §22.6]].

Not every vector field is conservative (the rotation field of [[§107 Vector Fields#^ex-107-1|Example §107.1]] is not; the test is [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Theorem §109.4]]), but conservative fields arise often in physics.

> [!example] Example §107.4: A Potential for the Gravitational Field
> The gravitational field of [[§107 Vector Fields#^ex-107-2|Example §107.2]] is conservative. Define
>
> $$
> f(x, y, z) = \frac{mMG}{\sqrt{x^2 + y^2 + z^2}} = mMG\,(x^2 + y^2 + z^2)^{-1/2} .
> $$
>
> By the Chain Rule, $\dfrac{\partial f}{\partial x} = mMG \cdot \left(-\tfrac12\right)(x^2 + y^2 + z^2)^{-3/2} \cdot 2x = \dfrac{-mMGx}{(x^2 + y^2 + z^2)^{3/2}}$, and similarly for $y$ and $z$. Hence
>
> $$
> \nabla f(x, y, z) = \frac{-mMGx}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{i} + \frac{-mMGy}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{j} + \frac{-mMGz}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{k} = \mathbf{F}(x, y, z) .
> $$
>
> How to tell whether a field is conservative, and how to find $f$ when it is, are the subjects of [[§109 The Fundamental Theorem for Line Integrals|§109]] and [[§111 Curl and Divergence|§111]]. This potential is used in [[§109 The Fundamental Theorem for Line Integrals#^ex-109-1|Example §109.1]] to compute work.
>
> *Stewart: 16.1 (text)*

^ex-107-4
