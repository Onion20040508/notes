---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 2
section: 13
tags: [multivariable-analysis, math452]
---
← [[§12 Composition of Functions and the Chain Rule]] · ↑ [[· 2 Differentiation]] · [[§14 The Function 2xy∕(x²+y²) and Its Partial Derivatives]] →

In [[§9 Directional Derivatives#^rem-9-2|§9]], we introduced the gradient $\nabla f$ of a scalar field. There are two more first-order differential operators that act on *vector* fields: the curl and the divergence. All three will play central roles in the integral theorems of Part II ([[§20 Multivariable Integration|§20]]–[[§34 Stokes' Theorem in ℝ³|§34]]) and will be unified by the [[§38 The Exterior Derivative#^def-38-1|exterior derivative]] in Part III (§37).

## Gradient (Scalar $\to$ Vector)

For a scalar field $f: \mathbb{R}^n \to \mathbb{R}$ with continuous partial derivatives, the **gradient** is:

$$
\nabla f = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right).
$$

In $\mathbb{R}^3$: $\nabla f = (f_x, f_y, f_z)$. As we saw in [[§9 Directional Derivatives#^rem-9-3|§9]], $\nabla f$ points in the direction of steepest increase, and $\nabla f \cdot \mathbf{v}$ gives the directional derivative of $f$ in direction $\mathbf{v}$.

## Divergence (Vector $\to$ Scalar)

For a vector field $\mathbf{F} = (F_1, F_2, \ldots, F_n): \mathbb{R}^n \to \mathbb{R}^n$ with continuous partial derivatives, the **divergence** is:

$$
\nabla \cdot \mathbf{F} = \frac{\partial F_1}{\partial x_1} + \frac{\partial F_2}{\partial x_2} + \cdots + \frac{\partial F_n}{\partial x_n}.
$$

In $\mathbb{R}^3$: $\nabla \cdot \mathbf{F} = (F_1)_x + (F_2)_y + (F_3)_z$. Geometrically, $\nabla \cdot \mathbf{F}$ measures the *net outward flux per unit volume* — how much the field “spreads out” at a point. A field with $\nabla \cdot \mathbf{F} = 0$ everywhere is called *incompressible* or *divergence-free*.

![[m452-11-1.svg]]
*Divergence is flux density: $\nabla\cdot\mathbf{F}(P) = \lim_{\varepsilon\to 0} \frac{1}{|B_\varepsilon|}\oint_{\partial B_\varepsilon}\mathbf{F}\cdot\hat{n}\,ds$ — shrink a test ball around $P$ and measure the net rate at which the field escapes, per unit area. Left: a stretching field pushes more flux out the far side than comes in the near side; the ball is a net source. Right: a uniform field passes straight through; whatever enters, leaves. The divergence theorem ([[Divergence Theorem in ℝ³|§18]]) is this local statement summed over a region: interior fluxes cancel ([[§27 Line Integrals and Green's Theorem#^thm-27-2|§27]]), leaving the boundary flux.*

## Curl (Vector $\to$ Vector, in $\mathbb{R}^3$ Only)

For a vector field $\mathbf{F} = (F_1, F_2, F_3): \mathbb{R}^3 \to \mathbb{R}^3$, the **curl** is:

$$
\nabla \times \mathbf{F} = \left(\frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z}, \;\; \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x}, \;\; \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y}\right).
$$

This can be written mnemonically as a “determinant”:

$$
\nabla \times \mathbf{F} = \begin{vmatrix} \hat{e}_x & \hat{e}_y & \hat{e}_z \\ \partial_x & \partial_y & \partial_z \\ F_1 & F_2 & F_3 \end{vmatrix}.
$$

Geometrically, $\nabla \times \mathbf{F}$ measures the *local rotation* of the field. A field with $\nabla \times \mathbf{F} = \mathbf{0}$ everywhere is called *irrotational* or *curl-free*.

![[m452-11-2.svg]]
*Three vector fields illustrating the operators. Left: a radial source — positive divergence, no rotation. Middle: rigid rotation — positive curl, no spreading. Right: uniform flow — neither. Divergence detects spreading; curl detects rotation.*

![[m452-11-3.svg]]
*Curl is circulation density: $(\nabla\times\mathbf{F})_z(P) = \lim_{\varepsilon\to 0} \frac{1}{|B_\varepsilon|}\oint_{\partial B_\varepsilon}\mathbf{F}\cdot\mathbf{T}\,ds$ — shrink a test loop around $P$ and measure how strongly the field pushes along it, per unit area (a paddle wheel placed at $P$ spins at this rate). Left: a rotational field drives the loop; positive curl. Right: a radial field is everywhere perpendicular to the loop; a paddle wheel would not turn — zero curl, even though the field is far from constant. Stokes' theorem ([[Stokes' Theorem in ℝ³|§20]]) is this local statement summed over a surface.*

**Why only $\mathbb{R}^3$?** The curl takes a vector field (3 components) and produces another vector field (3 components). This works because there are exactly 3 independent pairs from $\{x, y, z\}$: $(y,z)$, $(z,x)$, $(x,y)$. In $\mathbb{R}^2$, there is only 1 such pair, so the “curl” of a 2D field is a scalar, not a vector: $(\nabla \times \mathbf{F})_z = (F_2)_x - (F_1)_y$. In $\mathbb{R}^4$, there are 6 pairs, so the “curl” would have 6 components and cannot be a vector field. The exterior derivative ([[§38 The Exterior Derivative#^def-38-1|§38.1]]) removes this dimension restriction.

## Terminology for Vector Fields

> [!definition] Definition §13.1: Conservative
> A $C^1$ vector field $\mathbf{F}$ on a domain $D \subseteq \mathbb{R}^3$ is called:
> - **Conservative** (or a **gradient field**) if $\mathbf{F} = \nabla f$ for some scalar field $f$ (called the *potential*).

^def-13-1

> [!definition] Definition §13.2: Irrotational
> A $C^1$ vector field $\mathbf{F}$ on a domain $D \subseteq \mathbb{R}^3$ is called:
> - **Irrotational** (or **curl-free**) if $\nabla \times \mathbf{F} = \mathbf{0}$ everywhere on $D$.

^def-13-2

> [!definition] Definition §13.3: Solenoidal
> A $C^1$ vector field $\mathbf{F}$ on a domain $D \subseteq \mathbb{R}^3$ is called:
> - **Solenoidal** (or **divergence-free** or **incompressible**) if $\nabla \cdot \mathbf{F} = 0$ everywhere on $D$.

^def-13-3

> [!remark]- Connections
> - Divergence and curl return for the integral theorems: [[§27 Line Integrals and Green's Theorem#^def-27-5|Def. §27.5]], [[§27 Line Integrals and Green's Theorem#^def-27-6|Def. §27.6]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-1|Def. §28.1]], [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-28-2|Def. §28.2]].
> - All three operators are the exterior derivative $d$ in degrees 0, 1, 2: [[§38 The Exterior Derivative#^prop-38-1|Prop. §38.1]], [[§38 The Exterior Derivative#^prop-38-2|Prop. §38.2]], [[§38 The Exterior Derivative#^prop-38-3|Prop. §38.3]]; see also [[§38 The Exterior Derivative#^rem-38-4|the ℝ³ accident]].
> - Conservative/irrotational become exact/closed: [[§39 Closed and Exact Forms#^def-39-2|Def. §39.2]], [[Poincaré Lemma|Poincaré Lemma]].
> - Same notions in Stewart: [[§125 Vector Fields#^def-125-4|Calc Def. §125.4]], [[§132 Curl and Divergence#^def-132-2|Calc Def. §132.2]] and [[§132 Curl and Divergence#^def-132-4|Calc Def. §132.4]].

## Two Fundamental Identities

For any $C^2$ scalar field $f$ and $C^2$ vector field $\mathbf{F}$ on $\mathbb{R}^3$:

$$
\nabla \times (\nabla f) = \mathbf{0} \qquad \text{and} \qquad \nabla \cdot (\nabla \times \mathbf{F}) = 0.
$$

In the terminology above: *every conservative field is irrotational*, and *every curl of a vector field is solenoidal*.

*Proof of the first:* The $x$-component of $\nabla \times (\nabla f)$ is $f_{zy} - f_{yz} = 0$ by equality of mixed partials ([[Schwarz–Clairaut Theorem|§5]]). The other components are similar.

*Proof of the second:* $\nabla \cdot (\nabla \times \mathbf{F}) = (F_3)_{yx} - (F_2)_{zx} + (F_1)_{zy} - (F_3)_{xy} + (F_2)_{xz} - (F_1)_{yz} = 0$, again by equality of mixed partials.

The converses are more subtle: *is every irrotational field conservative?* *Is every solenoidal field a curl?* These depend on the *topology* of the domain $D$. On all of $\mathbb{R}^3$ the answer is yes; on domains with holes (like $\mathbb{R}^3$ minus a line), it can fail. This will be made precise in Part III ([[§39 Closed and Exact Forms#^def-39-2|§39.2]]), where “conservative” becomes “[[§39 Closed and Exact Forms#^def-39-3|exact]],” “irrotational” becomes “closed,” and the failure of the converse is detected by de Rham cohomology ([[§39 Closed and Exact Forms#^prop-39-6|a closed form that is not exact]]).

These identities say: the image of one operator lies in the kernel of the next. In Part III ([[§38 The Exterior Derivative#^rem-38-5|§38]]), we will see that both are the *same identity* $d^2 = 0$ ([[Exterior Derivative Squares to Zero|Theorem §38.4]]) applied at different levels, and that the equality of mixed partials ([[Schwarz–Clairaut Theorem|§5]]) is the underlying reason for both ([[§39 Closed and Exact Forms#^prop-39-4|Prop. §39.4]]).
