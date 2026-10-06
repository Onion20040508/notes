---
type: section
subject: "[[Calculus]]"
chapter: 14
section: "95a"
stewart: "14.6"
aliases: ["Stewart 14.6 (cont.)"]
tags: [calculus, math233]
---
← [[§95 Directional Derivatives and the Gradient Vector]] · ↑ [[· 14 Partial Derivatives]] · [[§96 Maximum and Minimum Values]] →

*Stewart, Section 14.6 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q29–Q31, Q33), Practice Final Set 1 (Part II, Q3).*

The Chain Rule shows that the gradient is perpendicular to level curves and level surfaces, which gives tangent planes to surfaces $F(x, y, z) = k$, including those that are not graphs.

## Tangent Planes to Level Surfaces

Suppose $S$ is a surface with equation $F(x, y, z) = k$, a level surface of a function $F$ of three variables, and let $P(x_0, y_0, z_0)$ be a point on $S$. Let $C$ be any curve that lies on $S$ and passes through $P$, described by a continuous vector function $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$ ([[§86 Vector Functions and Space Curves#^def-86-4|Definition §86.4]]), with $\mathbf{r}(t_0) = \langle x_0, y_0, z_0 \rangle$.

> [!theorem] Theorem §95.5: The Gradient Is Normal to Level Surfaces
> Let $F$ be differentiable, let $S$ be the level surface $F(x, y, z) = k$, and let $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$ be a curve on $S$, with $x$, $y$, $z$ differentiable, passing through $P(x_0, y_0, z_0)$ at $t = t_0$. Then
>
> $$
> \nabla F(x_0, y_0, z_0) \cdot \mathbf{r}'(t_0) = 0 . \qquad (18)
> $$
>
> That is, the gradient vector at $P$ is perpendicular to the tangent vector $\mathbf{r}'(t_0)$ of every curve on $S$ through $P$.
>
> *Stewart: 14.6, Equation 18*

^thm-95-5

> [!proof]+ Proof
> Since $C$ lies on $S$, every point $(x(t), y(t), z(t))$ satisfies the equation of $S$:
>
> $$
> F(x(t), y(t), z(t)) = k . \qquad (16)
> $$
>
> Differentiate both sides with respect to $t$, using the Chain Rule ([[§94 The Chain Rule#^thm-94-3|Theorem §94.3]]) on the left; the right side is constant:
>
> $$
> \frac{\partial F}{\partial x}\frac{dx}{dt} + \frac{\partial F}{\partial y}\frac{dy}{dt} + \frac{\partial F}{\partial z}\frac{dz}{dt} = 0 . \qquad (17)
> $$
>
> Since $\nabla F = \langle F_x, F_y, F_z \rangle$ and $\mathbf{r}'(t) = \langle x'(t), y'(t), z'(t) \rangle$ ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-1|Theorem §87.1]]), Equation (17) says $\nabla F \cdot \mathbf{r}'(t) = 0$. At $t = t_0$, $\mathbf{r}(t_0) = \langle x_0, y_0, z_0 \rangle$, which gives (18).

^pf-95-5

*Uses:* [[§94 The Chain Rule#^thm-94-3|§94.3]], [[§95 Directional Derivatives and the Gradient Vector#^def-95-new1|Def. §95.4]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-1|§87.1]]

> [!definition] Definition §95.4: Tangent Plane to a Level Surface
> If $\nabla F(x_0, y_0, z_0) \ne \mathbf{0}$, the **tangent plane to the level surface** $F(x, y, z) = k$ at $P(x_0, y_0, z_0)$ is the plane that passes through $P$ and has normal vector $\nabla F(x_0, y_0, z_0)$:
>
> $$
> F_x(x_0, y_0, z_0)(x - x_0) + F_y(x_0, y_0, z_0)(y - y_0) + F_z(x_0, y_0, z_0)(z - z_0) = 0 . \qquad (19)
> $$
>
> *Stewart: 14.6, Equations 19 and 20*

^def-95-4

> [!definition] Definition §95.5: Normal Line to a Level Surface
> The **normal line** to $S$ at $P$ is the line through $P$ perpendicular to the tangent plane. Its direction is given by $\nabla F(x_0, y_0, z_0)$, so its symmetric equations are
>
> $$
> \frac{x - x_0}{F_x(x_0, y_0, z_0)} = \frac{y - y_0}{F_y(x_0, y_0, z_0)} = \frac{z - z_0}{F_z(x_0, y_0, z_0)} . \qquad (20)
> $$
>
> *Stewart: 14.6, Equations 19 and 20*

^def-95-new2

By [[§95a Tangent Planes to Level Surfaces#^thm-95-5|Theorem §95.5]] every tangent line at $P$ to a curve on $S$ through $P$ lies in this plane, which is the fact used in [[§93 Tangent Planes and Linear Approximations#^ex-93-5|Example §93.5]]. The normal line can also be written in vector form, $\mathbf{r}(t) = \langle x_0, y_0, z_0 \rangle + t\,\nabla F(x_0, y_0, z_0)$ ([[§84 Equations of Lines and Planes#^thm-84-1|Theorem §84.1]]); this form also works when a component of $\nabla F$ is $0$.

> [!theorem] Proposition §95.6: Consistency with the Tangent Plane to a Graph
> If $S$ is the graph $z = f(x, y)$ of a differentiable function, then the tangent plane (19) to $S$, regarded as the level surface $F(x, y, z) = f(x, y) - z = 0$, is the tangent plane $z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$ of [[§93 Tangent Planes and Linear Approximations#^thm-93-1|Theorem §93.1]].
>
> *Stewart: 14.6 (text)*

^prop-95-6

> [!proof]+ Proof
> With $F(x, y, z) = f(x, y) - z$,
>
> $$
> F_x(x_0, y_0, z_0) = f_x(x_0, y_0) , \qquad F_y(x_0, y_0, z_0) = f_y(x_0, y_0) , \qquad F_z(x_0, y_0, z_0) = -1 ,
> $$
>
> so $\nabla F \ne \mathbf{0}$ and Equation (19) becomes $f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) - (z - z_0) = 0$, which is the equation of [[§93 Tangent Planes and Linear Approximations#^thm-93-1|Theorem §93.1]]. For example, for $z = 2x^2 + y^2$ at $(1, 1, 3)$, $F = 2x^2 + y^2 - z$ has $\nabla F(1, 1, 3) = \langle 4, 2, -1 \rangle$, and (19) gives $4(x - 1) + 2(y - 1) - (z - 3) = 0$, or $z = 4x + 2y - 3$, as in [[§93 Tangent Planes and Linear Approximations#^ex-93-1|Example §93.1]] (Stewart, Example 14.6.9).

^pf-95-6

*Uses:* [[§95a Tangent Planes to Level Surfaces#^def-95-4|Def. §95.4]], [[§93 Tangent Planes and Linear Approximations#^thm-93-1|§93.1]]

> [!example] Example §95.4: Tangent Planes and Normal Lines
> **(a)** Find the equations of the tangent plane and normal line at the point $(-2, 1, -3)$ to the ellipsoid
>
> $$
> \frac{x^2}{4} + y^2 + \frac{z^2}{9} = 3 .
> $$
>
> The ellipsoid is the level surface (with $k = 3$) of $F(x, y, z) = \frac{x^2}{4} + y^2 + \frac{z^2}{9}$. So
>
> $$
> F_x = \frac{x}{2} , \quad F_y = 2y , \quad F_z = \frac{2z}{9} ; \qquad F_x(-2, 1, -3) = -1 , \quad F_y(-2, 1, -3) = 2 , \quad F_z(-2, 1, -3) = -\frac23 .
> $$
>
> By (19) the tangent plane is $-1(x + 2) + 2(y - 1) - \frac23 (z + 3) = 0$, which simplifies (multiply by $-3$) to $3x - 6y + 2z + 18 = 0$. By (20) the normal line is
>
> $$
> \frac{x + 2}{-1} = \frac{y - 1}{2} = \frac{z + 3}{-\frac23} .
> $$
>
> **(b)** Consider the surface $x^2 + y^2 - 2z^2 = 0$ (a cone) and the point $P(1, 1, 1)$ on it. Find the tangent plane at $P$ and a vector equation of the normal line at $P$.
>
> With $F(x, y, z) = x^2 + y^2 - 2z^2$, $\nabla F = \langle 2x, 2y, -4z \rangle$ and $\nabla F(1, 1, 1) = \langle 2, 2, -4 \rangle$. The tangent plane is
>
> $$
> 2(x - 1) + 2(y - 1) - 4(z - 1) = 0 , \qquad\text{or}\qquad x + y - 2z = 0 ,
> $$
>
> and the normal line is $\mathbf{r}(t) = \langle 1, 1, 1 \rangle + t\langle 2, 2, -4 \rangle = \langle 1 + 2t,\ 1 + 2t,\ 1 - 4t \rangle$. (The tangent plane passes through the vertex $(0, 0, 0)$, as every tangent plane to a cone with vertex at the origin does.)
>
> *The posted answer gives $\mathbf{r}(t) = \langle 1 + 2t, 2 + 2t, 1 - 4t \rangle$, which passes through $(1, 2, 1)$ at $t = 0$, not through $P$; the second component should be $1 + 2t$.*
>
> *Stewart: Example 14.6.8*
> *Source: 233 Midterm 1 Practice Questions, Q31*

^ex-95-4

> [!example] Example §95.5: Prescribing the Tangent Plane
> **(a)** Find every point on the ellipsoid $x^2 + 2y^2 + 3z^2 = 1$ at which the tangent plane is parallel to the plane $3x - y + 3z = 1$.
>
> Two planes are parallel when their normal vectors are parallel. The normal vector of the given plane is $\mathbf{n} = \langle 3, -1, 3 \rangle$, and the tangent plane at $(x, y, z)$ has normal vector $\nabla F = \langle 2x, 4y, 6z \rangle$, where $F = x^2 + 2y^2 + 3z^2$. So we need $\nabla F = \lambda \mathbf{n}$ for some scalar $\lambda$, together with the equation of the surface:
>
> $$
> 2x = 3\lambda , \qquad 4y = -\lambda , \qquad 6z = 3\lambda , \qquad x^2 + 2y^2 + 3z^2 = 1 .
> $$
>
> The first and third equations give $x = 3z$; the second and third give $z = -2y$, hence $x = -6y$. Substituting into the last equation,
>
> $$
> (-6y)^2 + 2y^2 + 3(-2y)^2 = 36y^2 + 2y^2 + 12y^2 = 50y^2 = 1 , \qquad y = \pm\frac{1}{5\sqrt2} .
> $$
>
> The two points are
>
> $$
> \Big( -\frac{6}{5\sqrt2},\ \frac{1}{5\sqrt2},\ -\frac{2}{5\sqrt2} \Big) \qquad\text{and}\qquad \Big( \frac{6}{5\sqrt2},\ -\frac{1}{5\sqrt2},\ \frac{2}{5\sqrt2} \Big) .
> $$
>
> **(b)** Find the point $(a, b, c)$ on the surface $F(x, y, z) = x^2 - 2xy - y^2 + 8x + 4y - z = 0$ at which the tangent plane is horizontal, that is, parallel to the plane $z = 0$.
>
> The tangent plane is horizontal when $\nabla F$ is parallel to $\mathbf{k}$, that is, $F_x = F_y = 0$ (and $F_z = -1 \ne 0$ automatically):
>
> $$
> F_x = 2x - 2y + 8 = 0 , \qquad F_y = -2x - 2y + 4 = 0 .
> $$
>
> Adding, $-4y + 12 = 0$, so $y = 3$, and then $x = y - 4 = -1$. On the surface, $z = x^2 - 2xy - y^2 + 8x + 4y = 1 + 6 - 9 - 8 + 12 = 2$. The point is $(-1, 3, 2)$. (Since the surface is the graph $z = f(x, y)$, this is the critical point condition $f_x = f_y = 0$ of [[§96 Maximum and Minimum Values#^def-96-2|Definition §96.2]].)
>
> *Source: 233 Practice Final Set 1, Part II Q3; 233 Midterm 1 Practice Questions, Q33*

^ex-95-5

## Significance of the Gradient Vector

For a function $f$ of three variables and a point $P$ of its domain, $\nabla f(P)$ gives the direction of fastest increase of $f$ ([[§95 Directional Derivatives and the Gradient Vector#^thm-95-4|Theorem §95.4]]) and is orthogonal to the level surface of $f$ through $P$ ([[§95a Tangent Planes to Level Surfaces#^thm-95-5|Theorem §95.5]]). These are compatible: moving along the level surface, $f$ does not change at all, so it is reasonable that $f$ increases most when we move perpendicular to it. The same holds for a function of two variables and its level curves.

> [!theorem] Theorem §95.7: Properties of the Gradient Vector
> Let $f$ be a differentiable function of two or three variables and suppose that $\nabla f(\mathbf{x}) \ne \mathbf{0}$.
> - The directional derivative of $f$ at $\mathbf{x}$ in the direction of a unit vector $\mathbf{u}$ is given by $D_{\mathbf{u}} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}$.
> - $\nabla f(\mathbf{x})$ points in the direction of maximum rate of increase of $f$ at $\mathbf{x}$, and that maximum rate of change is $|\nabla f(\mathbf{x})|$.
> - $\nabla f(\mathbf{x})$ is perpendicular to the level curve or level surface of $f$ through $\mathbf{x}$.
>
> *Stewart: 14.6, Properties of the Gradient Vector*

^thm-95-7

> [!proof]+ Proof
> The first property is [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|Corollary §95.2]] (two variables) and [[§95 Directional Derivatives and the Gradient Vector#^thm-95-3|Theorem §95.3]] (three variables); the second is [[§95 Directional Derivatives and the Gradient Vector#^thm-95-4|Theorem §95.4]]. The third, for three variables, is [[§95a Tangent Planes to Level Surfaces#^thm-95-5|Theorem §95.5]]: $\nabla f(\mathbf{x})$ is perpendicular to every curve in the level surface through $\mathbf{x}$. For two variables Stewart says only that "by considerations similar to our discussion of tangent planes, it can be shown"; the argument is the same one dimension down. If $\mathbf{r}(t) = \langle x(t), y(t) \rangle$ is a differentiable parametrization of the level curve $f(x, y) = k$ with $\mathbf{r}(t_0) = \mathbf{x}$, then $f(x(t), y(t)) = k$, and the Chain Rule ([[§94 The Chain Rule#^thm-94-1|Theorem §94.1]]) gives $f_x x'(t) + f_y y'(t) = 0$, that is, $\nabla f(\mathbf{x}) \cdot \mathbf{r}'(t_0) = 0$: the gradient is perpendicular to the tangent vector of the level curve.

^pf-95-7

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|§95.2]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-3|§95.3]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-4|§95.4]], [[§95a Tangent Planes to Level Surfaces#^thm-95-5|§95.5]], [[§94 The Chain Rule#^thm-94-1|§94.1]]

> [!remark] Remark: Curves of Steepest Ascent and Gradient Fields
> On a topographic map of a hill, with $f(x, y)$ the height above sea level, a **curve of steepest ascent** is drawn by making it perpendicular to all of the contour lines; a creek running downhill follows a curve of steepest descent. Mathematical software can plot sample gradient vectors $\nabla f(a, b)$, each starting at the point $(a, b)$: a **gradient vector field** ([[§107 Vector Fields#^def-107-3|Definition §107.3]]). For $f(x, y) = x^2 - y^2$, superimposed on the contour map of $f$ (hyperbolas), the gradient vectors $\langle 2x, -2y \rangle$ point "uphill" and cross the level curves at right angles.

^rem-95-2
