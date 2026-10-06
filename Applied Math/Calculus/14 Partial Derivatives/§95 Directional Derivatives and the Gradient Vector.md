---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 95
stewart: "14.6"
aliases: ["Stewart 14.6"]
tags: [calculus, math233]
---
← [[§94 The Chain Rule]] · ↑ [[· 14 Partial Derivatives]] · [[§96 Maximum and Minimum Values]] →

*Stewart, Section 14.6 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q29–Q31, Q33), Practice Final Set 1 (Part II, Q3).*

The partial derivatives $f_x$ and $f_y$ are the rates of change of $f$ in the directions of $\mathbf{i}$ and $\mathbf{j}$. The directional derivative $D_{\mathbf{u}} f$ is the rate of change in the direction of any unit vector $\mathbf{u}$, and for a differentiable $f$ it is the dot product of $\mathbf{u}$ with one vector, the gradient $\nabla f = \langle f_x, f_y \rangle$. From the dot product formula, the gradient points in the direction of fastest increase and its length is that fastest rate. The Chain Rule then shows that the gradient is perpendicular to level curves and level surfaces, which gives tangent planes to surfaces $F(x, y, z) = k$, including those that are not graphs.

## Directional Derivatives

On a weather map of a temperature function $T(x, y)$, $T_x$ at a location is the rate of change of temperature with respect to distance traveling east, and $T_y$ traveling north. For other directions (southeast, toward another city) we need a new kind of derivative.

> [!definition] Definition §95.1: Directional Derivative
> The **directional derivative** of $f$ at $(x_0, y_0)$ in the direction of a unit vector $\mathbf{u} = \langle a, b \rangle$ is
>
> $$
> D_{\mathbf{u}} f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + ha, y_0 + hb) - f(x_0, y_0)}{h}
> $$
>
> if this limit exists.
>
> *Stewart: 14.6, Definition 2*

^def-95-1

> [!remark] Remark: Directional Derivatives as Rates and Slopes
> Let $S$ be the surface $z = f(x, y)$ and $P(x_0, y_0, z_0)$ with $z_0 = f(x_0, y_0)$. The vertical plane through $P$ in the direction of $\mathbf{u}$ cuts $S$ in a curve $C$. A point $Q(x, y, z)$ of $C$ lies over $(x, y) = (x_0 + ha, y_0 + hb)$, at horizontal distance $|h|$ from $(x_0, y_0)$ (since $\mathbf{u}$ is a unit vector), so
>
> $$
> \frac{\Delta z}{h} = \frac{z - z_0}{h} = \frac{f(x_0 + ha, y_0 + hb) - f(x_0, y_0)}{h} .
> $$
>
> Its limit $D_{\mathbf{u}} f(x_0, y_0)$ is the rate of change of $z$ with respect to distance in the direction of $\mathbf{u}$, and the slope of the tangent line $T$ to $C$ at $P$. Comparing with the definitions of $f_x$ and $f_y$ ([[§92 Partial Derivatives#^def-92-1|Definition §92.1]]): $D_{\mathbf{i}} f = f_x$ and $D_{\mathbf{j}} f = f_y$. The partial derivatives are special cases of the directional derivative.
>
> On a contour map, $D_{\mathbf{u}} f$ is estimated by an average rate of change: on the weather map, the line through Reno toward the southeast crosses the isothermals $T = 50$ and $T = 60$ about $75$ miles apart, so $D_{\mathbf{u}} T \approx \frac{60 - 50}{75} \approx 0.13$ °F/mi for $\mathbf{u} = (\mathbf{i} - \mathbf{j})/\sqrt2$ (Stewart, Example 14.6.1).

^rem-95-1

> [!remark]- Connections
> - Rigorous treatment: [[§7 Directional Derivatives#^def-7-1|452 Def. §7.1]] (direction given by an angle $\alpha$, as in Equation (6) below).

> [!theorem] Theorem §95.1: Directional Derivatives from Partial Derivatives
> If $f$ is a differentiable function of $x$ and $y$, then $f$ has a directional derivative in the direction of any unit vector $\mathbf{u} = \langle a, b \rangle$ and
>
> $$
> D_{\mathbf{u}} f(x, y) = f_x(x, y)\,a + f_y(x, y)\,b .
> $$
>
> If $\mathbf{u}$ makes an angle $\theta$ with the positive $x$-axis, then $\mathbf{u} = \langle \cos\theta, \sin\theta \rangle$ and
>
> $$
> D_{\mathbf{u}} f(x, y) = f_x(x, y) \cos\theta + f_y(x, y) \sin\theta . \qquad (6)
> $$
>
> *Stewart: 14.6, Theorem 3 and Equation 6*

^thm-95-1

> [!proof]+ Proof
> Fix $(x_0, y_0)$ and define a function $g$ of the single variable $h$ by
>
> $$
> g(h) = f(x_0 + ha, y_0 + hb) .
> $$
>
> By the definition of a derivative,
>
> $$
> g'(0) = \lim_{h \to 0} \frac{g(h) - g(0)}{h} = \lim_{h \to 0} \frac{f(x_0 + ha, y_0 + hb) - f(x_0, y_0)}{h} = D_{\mathbf{u}} f(x_0, y_0) . \qquad (4)
> $$
>
> On the other hand, $g(h) = f(x, y)$ with $x = x_0 + ha$ and $y = y_0 + hb$, so Case 1 of the Chain Rule ([[§94 The Chain Rule#^thm-94-1|Theorem §94.1]]) gives
>
> $$
> g'(h) = \frac{\partial f}{\partial x}\frac{dx}{dh} + \frac{\partial f}{\partial y}\frac{dy}{dh} = f_x(x, y)\,a + f_y(x, y)\,b .
> $$
>
> In particular $g'(0)$ exists, and putting $h = 0$ (so $x = x_0$, $y = y_0$),
>
> $$
> g'(0) = f_x(x_0, y_0)\,a + f_y(x_0, y_0)\,b . \qquad (5)
> $$
>
> Comparing (4) and (5), the limit defining $D_{\mathbf{u}} f(x_0, y_0)$ exists and equals $f_x(x_0, y_0)\,a + f_y(x_0, y_0)\,b$. Equation (6) is the case $a = \cos\theta$, $b = \sin\theta$.

^pf-95-1

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^def-95-1|Def. §95.1]], [[§94 The Chain Rule#^thm-94-1|§94.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§7 Directional Derivatives#^thm-7-1|452 Thm. §7.1]] and [[§6 Differentiability#^thm-6-1|452 Thm. §6.1]] (directly from the definition of differentiability); hub [[Directional Derivative Formula]]. Without differentiability the formula can fail even when all directional derivatives exist (Stewart, Exercise 76: $\sqrt[3]{xy}$ at the origin has $f_x = f_y = 0$ but no other directional derivatives).

## The Gradient Vector

By Theorem §95.1, the directional derivative of a differentiable function is a dot product:
$$
D_{\mathbf{u}} f(x, y) = f_x(x, y)\,a + f_y(x, y)\,b = \langle f_x(x, y), f_y(x, y) \rangle \cdot \langle a, b \rangle = \langle f_x(x, y), f_y(x, y) \rangle \cdot \mathbf{u} . \qquad (7)
$$
The first vector occurs in many other contexts too, so it gets a name.

> [!definition] Definition §95.2: Gradient
> If $f$ is a function of two variables $x$ and $y$, then the **gradient** of $f$ is the vector function $\nabla f$ (read "del $f$"; also written $\mathbf{grad}\,f$) defined by
>
> $$
> \nabla f(x, y) = \langle f_x(x, y), f_y(x, y) \rangle = \frac{\partial f}{\partial x}\,\mathbf{i} + \frac{\partial f}{\partial y}\,\mathbf{j} .
> $$
>
> For example, if $f(x, y) = \sin x + e^{xy}$, then $\nabla f(x, y) = \langle \cos x + ye^{xy}, xe^{xy} \rangle$ and $\nabla f(0, 1) = \langle 2, 0 \rangle$.
>
> *Stewart: 14.6, Definition 8 and Example 14.6.3*

^def-95-2

> [!theorem] Corollary §95.2: The Directional Derivative as a Dot Product
> If $f$ is a differentiable function of $x$ and $y$ and $\mathbf{u}$ is a unit vector, then
>
> $$
> D_{\mathbf{u}} f(x, y) = \nabla f(x, y) \cdot \mathbf{u} . \qquad (9)
> $$
>
> That is, the directional derivative in the direction of $\mathbf{u}$ is the scalar projection of the gradient vector onto $\mathbf{u}$ ([[§82 The Dot Product#^def-82-5|Definition §82.5]]).
>
> *Stewart: 14.6, Equation 9*

^cor-95-2

> [!proof]+ Proof
> This is Equation (7), which rewrites Theorem §95.1 using Definition §95.2 and the definition of the dot product.

^pf-95-2

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^thm-95-1|§95.1]], [[§95 Directional Derivatives and the Gradient Vector#^def-95-2|Def. §95.2]]

## Functions of Three Variables

> [!definition] Definition §95.3: Directional Derivative and Gradient in Three Variables
> The **directional derivative** of $f$ at $(x_0, y_0, z_0)$ in the direction of a unit vector $\mathbf{u} = \langle a, b, c \rangle$ is
>
> $$
> D_{\mathbf{u}} f(x_0, y_0, z_0) = \lim_{h \to 0} \frac{f(x_0 + ha, y_0 + hb, z_0 + hc) - f(x_0, y_0, z_0)}{h}
> $$
>
> if this limit exists. In vector notation, both definitions (two and three variables) read
>
> $$
> D_{\mathbf{u}} f(\mathbf{x}_0) = \lim_{h \to 0} \frac{f(\mathbf{x}_0 + h\mathbf{u}) - f(\mathbf{x}_0)}{h} , \qquad (11)
> $$
>
> where $\mathbf{x}_0 = \langle x_0, y_0 \rangle$ or $\langle x_0, y_0, z_0 \rangle$; here $f(\mathbf{x}_0 + h\mathbf{u})$ is the value of $f$ at a point of the line $\mathbf{x} = \mathbf{x}_0 + t\mathbf{u}$ ([[§84 Equations of Lines and Planes#^thm-84-1|Theorem §84.1]]). The **gradient** of a function of three variables is
>
> $$
> \nabla f = \langle f_x, f_y, f_z \rangle = \frac{\partial f}{\partial x}\,\mathbf{i} + \frac{\partial f}{\partial y}\,\mathbf{j} + \frac{\partial f}{\partial z}\,\mathbf{k} . \qquad (13)
> $$
>
> *Stewart: 14.6, Definition 10 and Equations 11, 13*

^def-95-3

> [!theorem] Theorem §95.3: Directional Derivatives in Three Variables
> If $f(x, y, z)$ is differentiable and $\mathbf{u} = \langle a, b, c \rangle$ is a unit vector, then
>
> $$
> D_{\mathbf{u}} f(x, y, z) = f_x(x, y, z)\,a + f_y(x, y, z)\,b + f_z(x, y, z)\,c = \nabla f(x, y, z) \cdot \mathbf{u} . \qquad (12),\ (14)
> $$
>
> *Stewart: 14.6, Equations 12 and 14*

^thm-95-3

> [!proof]+ Proof
> Stewart says that "the same method that was used to prove Theorem 3" works. Indeed, let $g(h) = f(x_0 + ha, y_0 + hb, z_0 + hc)$. Then $g'(0) = D_{\mathbf{u}} f(x_0, y_0, z_0)$ by definition, while the general Chain Rule ([[§94 The Chain Rule#^thm-94-3|Theorem §94.3]], with three intermediate variables and one independent variable $h$) gives $g'(h) = f_x a + f_y b + f_z c$, evaluated at $(x_0 + ha, y_0 + hb, z_0 + hc)$. Put $h = 0$. The dot product form is the same rewriting as in (7).

^pf-95-3

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^def-95-3|Def. §95.3]], [[§94 The Chain Rule#^thm-94-3|§94.3]]

> [!example] Example §95.1: Computing Directional Derivatives
> **(a)** Find $D_{\mathbf{u}} f(1, 2)$ for $f(x, y) = x^3 - 3xy + 4y^2$ and $\mathbf{u}$ the unit vector given by the angle $\theta = \pi/6$ from the positive $x$-axis.
>
> By Equation (6),
>
> $$
> D_{\mathbf{u}} f(x, y) = f_x \cos\frac{\pi}{6} + f_y \sin\frac{\pi}{6} = (3x^2 - 3y)\frac{\sqrt3}{2} + (-3x + 8y)\frac12 = \tfrac12 \Big[ 3\sqrt3\,x^2 - 3x + \big( 8 - 3\sqrt3 \big) y \Big] ,
> $$
>
> so $D_{\mathbf{u}} f(1, 2) = \frac12 \big[ 3\sqrt3 - 3 + (8 - 3\sqrt3)(2) \big] = \dfrac{13 - 3\sqrt3}{2}$. This is the slope of the tangent line, in the direction of $\mathbf{u}$, to the curve in which the vertical plane through $(1, 2, 0)$ in that direction cuts the surface $z = x^3 - 3xy + 4y^2$.
>
> **(b)** Find the directional derivative of $f(x, y) = x^2 y^3 - 4y$ at $(2, -1)$ in the direction of $\mathbf{v} = 2\mathbf{i} + 5\mathbf{j}$.
>
> $\nabla f(x, y) = 2xy^3\,\mathbf{i} + (3x^2 y^2 - 4)\,\mathbf{j}$, so $\nabla f(2, -1) = -4\,\mathbf{i} + 8\,\mathbf{j}$. The vector $\mathbf{v}$ is not a unit vector; since $|\mathbf{v}| = \sqrt{29}$, the unit vector in its direction is $\mathbf{u} = \frac{2}{\sqrt{29}}\,\mathbf{i} + \frac{5}{\sqrt{29}}\,\mathbf{j}$. By (9),
>
> $$
> D_{\mathbf{u}} f(2, -1) = (-4\,\mathbf{i} + 8\,\mathbf{j}) \cdot \Big( \frac{2}{\sqrt{29}}\,\mathbf{i} + \frac{5}{\sqrt{29}}\,\mathbf{j} \Big) = \frac{-4 \cdot 2 + 8 \cdot 5}{\sqrt{29}} = \frac{32}{\sqrt{29}} .
> $$
>
> **(c)** If $f(x, y, z) = x \sin yz$, find $\nabla f$ and the directional derivative of $f$ at $(1, 3, 0)$ in the direction of $\mathbf{v} = \mathbf{i} + 2\mathbf{j} - \mathbf{k}$.
>
> $\nabla f(x, y, z) = \langle \sin yz,\ xz\cos yz,\ xy\cos yz \rangle$, so $\nabla f(1, 3, 0) = \langle 0, 0, 3 \rangle$. The unit vector in the direction of $\mathbf{v}$ is $\mathbf{u} = \frac{1}{\sqrt6}\langle 1, 2, -1 \rangle$, and by Theorem §95.3
>
> $$
> D_{\mathbf{u}} f(1, 3, 0) = 3\mathbf{k} \cdot \frac{1}{\sqrt6}(\mathbf{i} + 2\mathbf{j} - \mathbf{k}) = 3\Big( -\frac{1}{\sqrt6} \Big) = -\sqrt{\frac32} .
> $$
>
> **(d)** For $f(x, y) = 2x^2 + xy^2$, find $\nabla f(1, 2)$ and the directional derivative of $f$ at $(1, 2)$ in the direction of $\mathbf{v} = \langle 3, 4 \rangle$.
>
> $\nabla f = \langle 4x + y^2, 2xy \rangle$, so $\nabla f(1, 2) = \langle 8, 4 \rangle$. With $|\mathbf{v}| = 5$, $\mathbf{u} = \langle \frac35, \frac45 \rangle$ and $D_{\mathbf{u}} f(1, 2) = \frac{24}{5} + \frac{16}{5} = 8$. (The same question asks for $f_{xx} = 4$, $f_{yy} = 2x$, $f_{xy} = f_{yx} = 2y$.)
>
> *Stewart: Examples 14.6.2, 14.6.4 and 14.6.5*
> *Source: 233 Midterm 1 Practice Questions, Q29*

^ex-95-1

## Maximizing the Directional Derivative

> [!theorem] Theorem §95.4: Maximizing the Directional Derivative
> Suppose $f$ is a differentiable function of two or three variables. The maximum value of the directional derivative $D_{\mathbf{u}} f(\mathbf{x})$ is $|\nabla f(\mathbf{x})|$, and it occurs when $\mathbf{u}$ has the same direction as the gradient vector $\nabla f(\mathbf{x})$.
>
> *Stewart: 14.6, Theorem 15*

^thm-95-4

> [!proof]+ Proof
> By Equation (9) or (14) and the geometric form of the dot product (Stewart, Theorem 12.3.3; [[§82 The Dot Product#^thm-82-2|Theorem §82.2]]),
>
> $$
> D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = |\nabla f|\,|\mathbf{u}| \cos\theta = |\nabla f| \cos\theta ,
> $$
>
> where $\theta$ is the angle between $\nabla f$ and $\mathbf{u}$ (and $|\mathbf{u}| = 1$). The maximum value of $\cos\theta$ is $1$, attained when $\theta = 0$. Therefore the maximum value of $D_{\mathbf{u}} f$ is $|\nabla f|$, and it occurs when $\theta = 0$, that is, when $\mathbf{u}$ has the same direction as $\nabla f$. (If $\nabla f = \mathbf{0}$, every directional derivative is $0 = |\nabla f|$.) Likewise the minimum value of $D_{\mathbf{u}} f$ is $-|\nabla f|$, at $\theta = \pi$: $f$ decreases fastest in the direction of $-\nabla f$.

^pf-95-4

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|§95.2]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-3|§95.3]], [[§82 The Dot Product#^thm-82-2|§82.2]] (angle between vectors)

> [!remark]- Connections
> - This is the equality case of the Cauchy–Schwarz inequality $|\nabla f \cdot \mathbf{u}| \le |\nabla f|\,|\mathbf{u}|$ ([[§19 Inner Products and Norms#^ladr-6-14|LADR 6.14]]), and it holds in $\mathbb{R}^n$ for every $n$. The 452 version: [[§7 Directional Derivatives#^rem-7-3|452 Remark: Gradient and Maximum Rate of Change]].

> [!example] Example §95.2: The Direction of Fastest Increase
> **(a)** If $f(x, y) = xe^y$, find the rate of change of $f$ at the point $P(2, 0)$ in the direction from $P$ to $Q(\frac12, 2)$. In what direction does $f$ have the maximum rate of change, and what is this maximum rate?
>
> $\nabla f(x, y) = \langle f_x, f_y \rangle = \langle e^y, xe^y \rangle$, so $\nabla f(2, 0) = \langle 1, 2 \rangle$. The vector $\overrightarrow{PQ} = \langle -\frac32, 2 \rangle$ has length $\sqrt{\frac94 + 4} = \frac52$, so the unit vector in its direction is $\mathbf{u} = \langle -\frac35, \frac45 \rangle$, and
>
> $$
> D_{\mathbf{u}} f(2, 0) = \nabla f(2, 0) \cdot \mathbf{u} = \langle 1, 2 \rangle \cdot \langle -\tfrac35, \tfrac45 \rangle = -\tfrac35 + \tfrac85 = 1 .
> $$
>
> By Theorem §95.4, $f$ increases fastest in the direction of $\nabla f(2, 0) = \langle 1, 2 \rangle$, and the maximum rate of change is $|\nabla f(2, 0)| = |\langle 1, 2 \rangle| = \sqrt5$.
>
> **(b)** Suppose that the temperature at a point $(x, y, z)$ in space is $T(x, y, z) = 80/(1 + x^2 + 2y^2 + 3z^2)$ (°C, with $x, y, z$ in meters). In which direction does the temperature increase fastest at $(1, 1, -2)$? What is the maximum rate of increase?
>
> By the Chain Rule for one variable,
>
> $$
> \nabla T = -\frac{160x}{(1 + x^2 + 2y^2 + 3z^2)^2}\,\mathbf{i} - \frac{320y}{(1 + x^2 + 2y^2 + 3z^2)^2}\,\mathbf{j} - \frac{480z}{(1 + x^2 + 2y^2 + 3z^2)^2}\,\mathbf{k} = \frac{160}{(1 + x^2 + 2y^2 + 3z^2)^2}\big( -x\,\mathbf{i} - 2y\,\mathbf{j} - 3z\,\mathbf{k} \big) .
> $$
>
> At $(1, 1, -2)$, $1 + 1 + 2 + 12 = 16$, so $\nabla T(1, 1, -2) = \frac{160}{256}(-\mathbf{i} - 2\mathbf{j} + 6\mathbf{k}) = \frac58(-\mathbf{i} - 2\mathbf{j} + 6\mathbf{k})$. The temperature increases fastest in the direction of $-\mathbf{i} - 2\mathbf{j} + 6\mathbf{k}$, or of the unit vector $(-\mathbf{i} - 2\mathbf{j} + 6\mathbf{k})/\sqrt{41}$, and the maximum rate of increase is $|\nabla T(1, 1, -2)| = \frac58 \sqrt{1 + 4 + 36} = \frac58\sqrt{41} \approx 4$ °C/m.
>
> *Stewart: Examples 14.6.6 and 14.6.7*

^ex-95-2

![[m233-95-1.svg]]
*Example §95.2(a): level curves $xe^y = c$ of $f(x, y) = xe^y$ near $P(2, 0)$. The gradient $\nabla f(2, 0) = \langle 1, 2 \rangle$ (red) is perpendicular to the level curve $xe^y = 2$ through $P$ (bold) and points toward higher values; $f$ increases at the rate $\sqrt5$ in its direction. In the direction of $Q$ (blue) the rate is only $\nabla f \cdot \mathbf{u} = 1$.*

> [!example] Example §95.3: Climbing a Mountain
> A hiker is walking on a mountain modeled by $z = f(x, y) = 100 - 4x^2 - 5y^2$, where the positive $x$-axis points East and the positive $y$-axis points North.
>
> **(a)** At the point $P(2, -1, 79)$, heading North, is the hiker ascending or descending?
>
> $\nabla f = \langle -8x, -10y \rangle$, so $\nabla f(2, -1) = \langle -16, 10 \rangle$. Heading North means $\mathbf{u} = \mathbf{j} = \langle 0, 1 \rangle$, and $D_{\mathbf{j}} f(2, -1) = f_y(2, -1) = 10 > 0$. The height increases: the hiker is **ascending**.
>
> **(b)** At the point $Q(1, 0, 96)$, in which direction on the map should the hiker initially head to descend most rapidly?
>
> $\nabla f(1, 0) = \langle -8, 0 \rangle$. By Theorem §95.4 the height decreases fastest in the direction of $-\nabla f(1, 0) = \langle 8, 0 \rangle$, that is, in the direction of $\mathbf{i}$: **East**. (In that direction the height decreases at the rate $|\nabla f(1, 0)| = 8$ per unit of horizontal distance.)
>
> *Source: 233 Midterm 1 Practice Questions, Q30*

^ex-95-3

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

*Uses:* [[§94 The Chain Rule#^thm-94-3|§94.3]], [[§95 Directional Derivatives and the Gradient Vector#^def-95-3|Def. §95.3]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-1|§87.1]]

> [!definition] Definition §95.4: Tangent Plane and Normal Line to a Level Surface
> If $\nabla F(x_0, y_0, z_0) \ne \mathbf{0}$, the **tangent plane to the level surface** $F(x, y, z) = k$ at $P(x_0, y_0, z_0)$ is the plane that passes through $P$ and has normal vector $\nabla F(x_0, y_0, z_0)$:
>
> $$
> F_x(x_0, y_0, z_0)(x - x_0) + F_y(x_0, y_0, z_0)(y - y_0) + F_z(x_0, y_0, z_0)(z - z_0) = 0 . \qquad (19)
> $$
>
> The **normal line** to $S$ at $P$ is the line through $P$ perpendicular to the tangent plane. Its direction is given by $\nabla F(x_0, y_0, z_0)$, so its symmetric equations are
>
> $$
> \frac{x - x_0}{F_x(x_0, y_0, z_0)} = \frac{y - y_0}{F_y(x_0, y_0, z_0)} = \frac{z - z_0}{F_z(x_0, y_0, z_0)} . \qquad (20)
> $$
>
> *Stewart: 14.6, Equations 19 and 20*

^def-95-4

By Theorem §95.5 every tangent line at $P$ to a curve on $S$ through $P$ lies in this plane, which is the fact used in [[§93 Tangent Planes and Linear Approximations#^ex-93-5|Example §93.5]]. The normal line can also be written in vector form, $\mathbf{r}(t) = \langle x_0, y_0, z_0 \rangle + t\,\nabla F(x_0, y_0, z_0)$ ([[§84 Equations of Lines and Planes#^thm-84-1|Theorem §84.1]]); this form also works when a component of $\nabla F$ is $0$.

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

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^def-95-4|Def. §95.4]], [[§93 Tangent Planes and Linear Approximations#^thm-93-1|§93.1]]

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

For a function $f$ of three variables and a point $P$ of its domain, $\nabla f(P)$ gives the direction of fastest increase of $f$ (Theorem §95.4) and is orthogonal to the level surface of $f$ through $P$ (Theorem §95.5). These are compatible: moving along the level surface, $f$ does not change at all, so it is reasonable that $f$ increases most when we move perpendicular to it. The same holds for a function of two variables and its level curves.

> [!theorem] Theorem §95.7: Properties of the Gradient Vector
> Let $f$ be a differentiable function of two or three variables and suppose that $\nabla f(\mathbf{x}) \ne \mathbf{0}$.
> - The directional derivative of $f$ at $\mathbf{x}$ in the direction of a unit vector $\mathbf{u}$ is given by $D_{\mathbf{u}} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}$.
> - $\nabla f(\mathbf{x})$ points in the direction of maximum rate of increase of $f$ at $\mathbf{x}$, and that maximum rate of change is $|\nabla f(\mathbf{x})|$.
> - $\nabla f(\mathbf{x})$ is perpendicular to the level curve or level surface of $f$ through $\mathbf{x}$.
>
> *Stewart: 14.6, Properties of the Gradient Vector*

^thm-95-7

> [!proof]+ Proof
> The first property is Corollary §95.2 (two variables) and Theorem §95.3 (three variables); the second is Theorem §95.4. The third, for three variables, is Theorem §95.5: $\nabla f(\mathbf{x})$ is perpendicular to every curve in the level surface through $\mathbf{x}$. For two variables Stewart says only that "by considerations similar to our discussion of tangent planes, it can be shown"; the argument is the same one dimension down. If $\mathbf{r}(t) = \langle x(t), y(t) \rangle$ is a differentiable parametrization of the level curve $f(x, y) = k$ with $\mathbf{r}(t_0) = \mathbf{x}$, then $f(x(t), y(t)) = k$, and the Chain Rule ([[§94 The Chain Rule#^thm-94-1|Theorem §94.1]]) gives $f_x x'(t) + f_y y'(t) = 0$, that is, $\nabla f(\mathbf{x}) \cdot \mathbf{r}'(t_0) = 0$: the gradient is perpendicular to the tangent vector of the level curve.

^pf-95-7

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|§95.2]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-3|§95.3]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-4|§95.4]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|§95.5]], [[§94 The Chain Rule#^thm-94-1|§94.1]]

> [!remark] Remark: Curves of Steepest Ascent and Gradient Fields
> On a topographic map of a hill, with $f(x, y)$ the height above sea level, a **curve of steepest ascent** is drawn by making it perpendicular to all of the contour lines; a creek running downhill follows a curve of steepest descent. Mathematical software can plot sample gradient vectors $\nabla f(a, b)$, each starting at the point $(a, b)$: a **gradient vector field** ([[§107 Vector Fields#^def-107-3|Definition §107.3]]). For $f(x, y) = x^2 - y^2$, superimposed on the contour map of $f$ (hyperbolas), the gradient vectors $\langle 2x, -2y \rangle$ point "uphill" and cross the level curves at right angles.

^rem-95-2
