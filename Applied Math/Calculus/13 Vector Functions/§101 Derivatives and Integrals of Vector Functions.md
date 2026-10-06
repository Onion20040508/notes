---
type: section
subject: "[[Calculus]]"
chapter: 13
section: 101
stewart: "13.2"
aliases: ["Stewart 13.2"]
tags: [calculus, math233]
---
← [[§100 Vector Functions and Space Curves]] · ↑ [[· 13 Vector Functions]] · [[§102 Arc Length and Curvature]] →

*Stewart, Section 13.2 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q13), Practice Exam 1 (Q1(c)), Exam 1 Review (Q10(c), Q13, Q17), SI Midterm 1 Problem Set (Q4(a), Q4(c)).*

The calculus of vector functions is one-variable calculus done in each component. The derivative $\mathbf{r}'(t)$ is the limit of difference quotients, computed by differentiating the components; geometrically it is the tangent vector to the curve, which gives tangent lines and the unit tangent vector $\mathbf{T}$. The familiar differentiation rules carry over, with product rules for scalar multiples, dot products and cross products. One consequence is used constantly in [[§102 Arc Length and Curvature|§102]]: a vector function of constant length is perpendicular to its derivative. Integrals are also computed componentwise, and the Fundamental Theorem of Calculus holds for vector functions; in [[§104 Motion in Space꞉ Velocity and Acceleration|§104]] it recovers position from velocity and velocity from acceleration.

## Derivatives

> [!definition] Definition §118.1: Derivative of a Vector Function
> The **derivative** $\mathbf{r}'$ of a vector function $\mathbf{r}$ is
>
> $$
> \frac{d\mathbf{r}}{dt} = \mathbf{r}'(t) = \lim_{h \to 0} \frac{\mathbf{r}(t + h) - \mathbf{r}(t)}{h} ,
> $$
>
> if this limit exists.
>
> *Stewart: 13.2, Definition 1*

^def-101-1

> [!definition] Definition §118.3: Tangent Vector
> Let $C$ be the curve defined by $\mathbf{r}$ and $P$ the point with position vector $\mathbf{r}(t)$. If $\mathbf{r}'(t)$ exists and $\mathbf{r}'(t) \ne \mathbf{0}$, it is the **tangent vector** to $C$ at $P$.
>
> *Stewart: 13.2 (text)*

^def-101-2

> [!definition] Definition §118.4: Tangent Line
> For $C$, $P$ and $\mathbf{r}'(t) \ne \mathbf{0}$ as in [[§101 Derivatives and Integrals of Vector Functions#^def-101-2|Definition §101.2]], the **tangent line** to $C$ at $P$ is the line through $P$ parallel to $\mathbf{r}'(t)$.
>
> *Stewart: 13.2 (text)*

^def-101-3

> [!definition] Definition §118.6: Unit Tangent Vector
> The **unit tangent vector** is
>
> $$
> \mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} .
> $$
>
> *Stewart: 13.2 (text)*

^def-101-4

> [!remark] Remark: Why r′ Is Tangent
> If $P$ and $Q$ have position vectors $\mathbf{r}(t)$ and $\mathbf{r}(t + h)$, then $\overrightarrow{PQ} = \mathbf{r}(t + h) - \mathbf{r}(t)$ is a secant vector. For $h > 0$ the scalar multiple $\frac1h(\mathbf{r}(t + h) - \mathbf{r}(t))$ has the same direction (for $0 < h < 1$ it stretches the secant). As $h \to 0$, $Q$ slides toward $P$ along the curve and this vector appears to approach a vector lying on the tangent line. The same picture shows that $\mathbf{r}'(t)$ points in the direction of increasing $t$ (Stewart's Exercise 60).

^rem-101-1

![[m233-87-1.svg]]
*(a) The secant vector $\overrightarrow{PQ} = \mathbf{r}(t + h) - \mathbf{r}(t)$ joins two points of $C$. (b) Divided by $h$ it becomes the difference quotient (blue), which turns toward the tangent direction as $Q \to P$; its limit is the tangent vector $\mathbf{r}'(t)$ (red).*

> [!theorem] Theorem §118.1: Differentiate Each Component
> If $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle = f(t)\,\mathbf{i} + g(t)\,\mathbf{j} + h(t)\,\mathbf{k}$, where $f$, $g$ and $h$ are differentiable functions, then
>
> $$
> \mathbf{r}'(t) = \langle f'(t), g'(t), h'(t) \rangle = f'(t)\,\mathbf{i} + g'(t)\,\mathbf{j} + h'(t)\,\mathbf{k} .
> $$
>
> *Stewart: 13.2, Theorem 2*

^thm-101-1

> [!proof]+ Proof
> By [[§101 Derivatives and Integrals of Vector Functions#^def-101-1|Definition §101.1]] and the componentwise arithmetic of [[§94 Vectors#^thm-94-4|Theorem §94.4]],
>
> $$
> \begin{aligned}
> \mathbf{r}'(t) &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\big[\mathbf{r}(t + \Delta t) - \mathbf{r}(t)\big]
> = \lim_{\Delta t \to 0} \Big\langle \frac{f(t + \Delta t) - f(t)}{\Delta t}, \frac{g(t + \Delta t) - g(t)}{\Delta t}, \frac{h(t + \Delta t) - h(t)}{\Delta t} \Big\rangle \\
> &= \Big\langle \lim_{\Delta t \to 0} \frac{f(t + \Delta t) - f(t)}{\Delta t},\ \lim_{\Delta t \to 0} \frac{g(t + \Delta t) - g(t)}{\Delta t},\ \lim_{\Delta t \to 0} \frac{h(t + \Delta t) - h(t)}{\Delta t} \Big\rangle = \langle f'(t), g'(t), h'(t) \rangle ,
> \end{aligned}
> $$
>
> where the second line uses [[§100 Vector Functions and Space Curves#^def-100-2|Definition §100.2]]: the component limits exist because $f$, $g$, $h$ are differentiable.

^pf-101-1

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^def-101-1|Def. §101.1]], [[§100 Vector Functions and Space Curves#^def-100-2|Def. §100.2]], [[§94 Vectors#^thm-94-4|§94.4]], [[§15 The Derivative as a Function#^def-15-1|Def. §15.1]]

> [!remark]- Connections
> - For a plane curve this is the tangent vector $(x'(t), y'(t))$ of [[§27 Line Integrals and Green's Theorem#^def-27-3|452 Def. §27.3]]. In 452's language, $\mathbf{r}'(t)$ is the Jacobian (a $3 \times 1$ matrix) of $\mathbf{r}: \mathbb{R} \to \mathbb{R}^3$, and [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|Theorem §101.1]] says it is computed entry by entry.
> - ODE version: [[§34 Matrices#^def-34-10|331 Def. §34.10]] (matrix functions, differentiated and integrated entry by entry; a vector function is the case of a single column).
> - Complex-variables version: [[§41 Derivatives of Functions w(t)#^def-41-1|342 Def. §41.1]] (the derivative of $w(t) = u(t) + iv(t)$, taken component by component).

> [!definition] Definition §118.7: Second Derivative
> The **second derivative** of a vector function $\mathbf{r}$ is the derivative of $\mathbf{r}'$: $\mathbf{r}'' = (\mathbf{r}')'$. In [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-1|Definition §104.1]] and [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-3|Definition §104.3]], $\mathbf{r}'(t)$ and $\mathbf{r}''(t)$ are the velocity and acceleration of a particle with position $\mathbf{r}(t)$ at time $t$.
>
> *Stewart: 13.2 (text)*

^def-101-5

> [!example] Example §118.1: Derivatives and Unit Tangent Vectors
> **(a)** For $\mathbf{r}(t) = (1 + t^3)\,\mathbf{i} + te^{-t}\,\mathbf{j} + \sin 2t\,\mathbf{k}$, [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|Theorem §101.1]] gives
>
> $$
> \mathbf{r}'(t) = 3t^2\,\mathbf{i} + (1 - t)e^{-t}\,\mathbf{j} + 2\cos 2t\,\mathbf{k}
> $$
>
> (Product Rule for $te^{-t}$, Chain Rule for $\sin 2t$). At $t = 0$: $\mathbf{r}(0) = \mathbf{i}$ and $\mathbf{r}'(0) = \mathbf{j} + 2\mathbf{k}$, so the unit tangent vector at $(1, 0, 0)$ is
>
> $$
> \mathbf{T}(0) = \frac{\mathbf{r}'(0)}{|\mathbf{r}'(0)|} = \frac{\mathbf{j} + 2\mathbf{k}}{\sqrt{1 + 4}} = \frac{1}{\sqrt5}\,\mathbf{j} + \frac{2}{\sqrt5}\,\mathbf{k} .
> $$
>
> **(b)** For $\mathbf{r}(t) = \langle \sin t, 2t, t^2 \rangle$: $\mathbf{r}'(t) = \langle \cos t, 2, 2t \rangle$, $\mathbf{r}'(0) = \langle 1, 2, 0 \rangle$, and $\mathbf{T}(0) = \big\langle \frac{1}{\sqrt5}, \frac{2}{\sqrt5}, 0 \big\rangle$.
>
> **(c)** For the plane curve $\mathbf{r}(t) = \sqrt t\,\mathbf{i} + (2 - t)\,\mathbf{j}$: $\mathbf{r}'(t) = \dfrac{1}{2\sqrt t}\,\mathbf{i} - \mathbf{j}$, so $\mathbf{r}(1) = \mathbf{i} + \mathbf{j}$ and $\mathbf{r}'(1) = \frac12\mathbf{i} - \mathbf{j}$. Eliminating $t$ from $x = \sqrt t$, $y = 2 - t$ gives $y = 2 - x^2$, $x \ge 0$: the tangent vector at $(1, 1)$ points down the parabola, in the direction of increasing $t$.
>
> **(d)** For $\mathbf{r}(t) = \Big\langle \sqrt{2 - t}, \dfrac{e^t - 1}{t}, \ln(t + 1) \Big\rangle$ (Quotient Rule in the middle component):
>
> $$
> \mathbf{r}'(t) = \Big\langle -\frac{1}{2\sqrt{2 - t}},\ \frac{te^t - (e^t - 1)}{t^2},\ \frac{1}{t + 1} \Big\rangle .
> $$
>
> *Stewart: Examples 13.2.1 and 13.2.2*
> *Source: 233 Practice Exam 1, Q1(c); 233 Exam 1 Review, Q10(c)*

^ex-101-1

> [!example] Example §118.2: Tangent Lines
> **(a)** Find parametric equations for the tangent line to the helix $x = 2\cos t$, $y = \sin t$, $z = t$ at the point $(0, 1, \pi/2)$.
>
> The vector equation is $\mathbf{r}(t) = \langle 2\cos t, \sin t, t \rangle$, so $\mathbf{r}'(t) = \langle -2\sin t, \cos t, 1 \rangle$. The point corresponds to $t = \pi/2$, where $\mathbf{r}'(\pi/2) = \langle -2, 0, 1 \rangle$. The tangent line passes through $(0, 1, \pi/2)$ parallel to $\langle -2, 0, 1 \rangle$, so by [[§98 Equations of Lines and Planes#^prop-98-2|Proposition §98.2]]
>
> $$
> x = -2t, \qquad y = 1, \qquad z = \frac{\pi}{2} + t .
> $$
>
> **(b)** $\mathbf{r}(t) = \langle 2t + \sin t, \cos t, 2t \rangle$ at $(2\pi, -1, 2\pi)$. From $z = 2t = 2\pi$, $t = \pi$; check $x = 2\pi + \sin\pi = 2\pi$, $y = \cos\pi = -1$. Then $\mathbf{r}'(t) = \langle 2 + \cos t, -\sin t, 2 \rangle$, $\mathbf{r}'(\pi) = \langle 1, 0, 2 \rangle$, and the tangent line is $x = 2\pi + t$, $y = -1$, $z = 2\pi + 2t$.
>
> **(c)** $x = t\cos t$, $y = t$, $z = t\sin t$ at $(-\pi, \pi, 0)$, that is, at $t = \pi$. Here $\mathbf{r}'(t) = \langle \cos t - t\sin t, 1, \sin t + t\cos t \rangle$ and $\mathbf{r}'(\pi) = \langle -1, 1, -\pi \rangle$, so the tangent line is $x = -\pi - s$, $y = \pi + s$, $z = -\pi s$.
>
> **(d)** $\mathbf{r}(t) = t^2\,\mathbf{i} - t^2\,\mathbf{j} + \frac12 t^2\,\mathbf{k}$, $t \ge 0$, at $(4, -4, 2)$, that is, $t = 2$. Here $\mathbf{r}'(t) = \langle 2t, -2t, t \rangle$ and $\mathbf{r}'(2) = \langle 4, -4, 2 \rangle$, so the tangent line is $x = 4 + 4s$, $y = -4 - 4s$, $z = 2 + 2s$. (Since $\mathbf{r}(t) = t^2\langle 1, -1, \frac12 \rangle$, the curve is itself a ray from the origin, and the tangent line is the line containing it.)
>
> *Stewart: Example 13.2.3*
> *Source: 233 Midterm 1 Practice Questions, Q13; 233 Exam 1 Review, Q17; 233 SI Midterm 1 Problem Set, Q4(a)*

^ex-101-2

## Differentiation Rules

> [!theorem] Theorem §101.2: Differentiation Rules
> Suppose $\mathbf{u}$ and $\mathbf{v}$ are differentiable vector functions, $c$ is a scalar, and $f$ is a real-valued function. Then
>
> $$
> \begin{aligned}
> &1.\ \frac{d}{dt}[\mathbf{u}(t) + \mathbf{v}(t)] = \mathbf{u}'(t) + \mathbf{v}'(t) &\qquad &2.\ \frac{d}{dt}[c\,\mathbf{u}(t)] = c\,\mathbf{u}'(t) \\
> &3.\ \frac{d}{dt}[f(t)\,\mathbf{u}(t)] = f'(t)\,\mathbf{u}(t) + f(t)\,\mathbf{u}'(t) &\qquad &4.\ \frac{d}{dt}[\mathbf{u}(t) \cdot \mathbf{v}(t)] = \mathbf{u}'(t) \cdot \mathbf{v}(t) + \mathbf{u}(t) \cdot \mathbf{v}'(t) \\
> &5.\ \frac{d}{dt}[\mathbf{u}(t) \times \mathbf{v}(t)] = \mathbf{u}'(t) \times \mathbf{v}(t) + \mathbf{u}(t) \times \mathbf{v}'(t) &\qquad &6.\ \frac{d}{dt}[\mathbf{u}(f(t))] = f'(t)\,\mathbf{u}'(f(t)) \quad \text{(Chain Rule)}
> \end{aligned}
> $$
>
> (In 3 and 6, $f$ is differentiable as well.)
>
> *Stewart: 13.2, Theorem 3*

^thm-101-2

> [!proof]+ Proof
> Stewart proves Formula 4 and leaves the others as exercises. Write $\mathbf{u} = \langle f_1, f_2, f_3 \rangle$ and $\mathbf{v} = \langle g_1, g_2, g_3 \rangle$. By [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|Theorem §101.1]] every formula can be checked component by component using the rules for real-valued functions: the Sum and Constant Multiple Rules ([[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-4|Theorem §17.4]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-3|Theorem §17.3]]), the Product Rule ([[§18 The Product and Quotient Rules#^thm-18-1|Theorem §18.1]]) and the Chain Rule ([[§20 The Chain Rule#^thm-20-2|Theorem §20.2]]).
>
> **1, 2.** The $i$-th component of $\mathbf{u} + \mathbf{v}$ is $f_i + g_i$, with derivative $f_i' + g_i'$; that of $c\mathbf{u}$ is $cf_i$, with derivative $cf_i'$ (Sum and Constant Multiple Rules).
>
> **3.** The $i$-th component of $f\mathbf{u}$ is $ff_i$, with derivative $f'f_i + ff_i'$ by the Product Rule: the $i$-th component of $f'\mathbf{u} + f\mathbf{u}'$.
>
> **4.** Since $\mathbf{u}(t) \cdot \mathbf{v}(t) = \sum_{i=1}^3 f_i(t)g_i(t)$, the ordinary Product Rule gives
>
> $$
> \frac{d}{dt}[\mathbf{u}(t) \cdot \mathbf{v}(t)] = \sum_{i=1}^3 \frac{d}{dt}[f_i(t)g_i(t)] = \sum_{i=1}^3 \big[f_i'(t)g_i(t) + f_i(t)g_i'(t)\big] = \sum_{i=1}^3 f_i'(t)g_i(t) + \sum_{i=1}^3 f_i(t)g_i'(t) = \mathbf{u}'(t) \cdot \mathbf{v}(t) + \mathbf{u}(t) \cdot \mathbf{v}'(t) .
> $$
>
> **5.** The first component of $\mathbf{u} \times \mathbf{v}$ is $f_2g_3 - f_3g_2$, with derivative
>
> $$
> f_2'g_3 + f_2g_3' - f_3'g_2 - f_3g_2' = (f_2'g_3 - f_3'g_2) + (f_2g_3' - f_3g_2') ,
> $$
>
> the first component of $\mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$; the other two components are the same with the indices shifted. The order of the factors must be kept, because the cross product is not commutative.
>
> **6.** The $i$-th component of $\mathbf{u}(f(t))$ is $f_i(f(t))$, with derivative $f_i'(f(t))\,f'(t)$ by the Chain Rule: the $i$-th component of $f'(t)\,\mathbf{u}'(f(t))$.

^pf-101-2

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|§101.1]], [[§95 The Dot Product#^def-95-1|Def. §95.1]], [[§96 The Cross Product#^def-96-1|Def. §96.1]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-3|§17.3]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-4|§17.4]], [[§18 The Product and Quotient Rules#^thm-18-1|§18.1]], [[§20 The Chain Rule#^thm-20-2|§20.2]]

> [!remark]- Connections
> - Componentwise, these are the sum, product and chain rules of [[§28 Basic Properties of the Derivative#^thm-28-2|451 Thm. §28.2]] and [[§28 Basic Properties of the Derivative#^thm-28-3|451 Thm. §28.3]]; Formula 6 is the special case of the multivariable chain rule [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]] for $\mathbb{R} \to \mathbb{R} \to \mathbb{R}^3$.
> - ODE version: [[§34 Matrices#^prop-34-4|331 Prop. §34.4]] (sum and product rules for matrix functions, where the order of the factors must be kept).

> [!theorem] Theorem §101.3: Constant Length Means r′ ⟂ r
> If $|\mathbf{r}(t)| = c$ (a constant), then $\mathbf{r}'(t)$ is orthogonal to $\mathbf{r}(t)$ for all $t$.
>
> *Stewart: 13.2, Theorem 4*

^thm-101-3

> [!proof]+ Proof
> Since $\mathbf{r}(t) \cdot \mathbf{r}(t) = |\mathbf{r}(t)|^2 = c^2$ is constant, Formula 4 of [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|Theorem §101.2]] gives
>
> $$
> 0 = \frac{d}{dt}[\mathbf{r}(t) \cdot \mathbf{r}(t)] = \mathbf{r}'(t) \cdot \mathbf{r}(t) + \mathbf{r}(t) \cdot \mathbf{r}'(t) = 2\,\mathbf{r}'(t) \cdot \mathbf{r}(t) .
> $$
>
> So $\mathbf{r}'(t) \cdot \mathbf{r}(t) = 0$, which says $\mathbf{r}'(t)$ is orthogonal to $\mathbf{r}(t)$ ([[§95 The Dot Product#^thm-95-4|Theorem §95.4]]).

^pf-101-3

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|§101.2]], [[§95 The Dot Product#^thm-95-1|§95.1]], [[§95 The Dot Product#^thm-95-4|§95.4]]

> [!remark] Remark: Curves on a Sphere
> Geometrically, [[§101 Derivatives and Integrals of Vector Functions#^thm-101-3|Theorem §101.3]] says that if a curve lies on a sphere centered at the origin, its tangent vector $\mathbf{r}'(t)$ is always perpendicular to the position vector $\mathbf{r}(t)$, the radius of the sphere. The most important application is to the unit tangent vector: $|\mathbf{T}(t)| = 1$, so $\mathbf{T}'(t) \perp \mathbf{T}(t)$, which is how the unit normal vector is defined in [[§103 The TNB Frame and Torsion#^def-103-1|Definition §103.1]].

^rem-101-2

> [!example] Example §118.3: The Angle Between Two Curves
> The helix $\mathbf{r}_1(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\,\mathbf{k}$ meets the curve $\mathbf{r}_2(t) = (1 + t)\,\mathbf{i} + t^2\,\mathbf{j} + t^3\,\mathbf{k}$ at $(1, 0, 0)$. Find the angle of intersection.
>
> The angle between two curves at a common point is the angle between their tangent vectors there. Both curves pass through $(1, 0, 0)$ at $t = 0$. Now $\mathbf{r}_1'(t) = \langle -\sin t, \cos t, 1 \rangle$, so $\mathbf{r}_1'(0) = \langle 0, 1, 1 \rangle$, and $\mathbf{r}_2'(t) = \langle 1, 2t, 3t^2 \rangle$, so $\mathbf{r}_2'(0) = \langle 1, 0, 0 \rangle$. Since
>
> $$
> \mathbf{r}_1'(0) \cdot \mathbf{r}_2'(0) = 0 + 0 + 0 = 0 ,
> $$
>
> the tangent vectors are perpendicular ([[§95 The Dot Product#^thm-95-4|Theorem §95.4]]): the curves meet at an angle of $90^\circ$.
>
> *Source: 233 Exam 1 Review, Q13*

^ex-101-3

## Integrals

> [!definition] Definition §118.8: Integral of a Vector Function
> The **definite integral** of a continuous vector function $\mathbf{r}(t)$ is defined as for real-valued functions ([[§39 The Definite Integral#^def-39-1|Definition §39.1]]), except that the integral is a vector:
>
> $$
> \int_a^b \mathbf{r}(t)\,dt = \lim_{n \to \infty} \sum_{i=1}^n \mathbf{r}(t_i^*)\,\Delta t .
> $$
>
> *Stewart: 13.2 (text)*

^def-101-6

> [!definition] Definition §118.9: Antiderivative of a Vector Function
> An **antiderivative** of $\mathbf{r}$ is a vector function $\mathbf{R}$ with $\mathbf{R}'(t) = \mathbf{r}(t)$, and $\int \mathbf{r}(t)\,dt$ denotes the indefinite integral (the general antiderivative).
>
> *Stewart: 13.2 (text)*

^def-101-7

> [!theorem] Proposition §101.4: Integrate Each Component
> If $\mathbf{r}(t) = f(t)\,\mathbf{i} + g(t)\,\mathbf{j} + h(t)\,\mathbf{k}$ is continuous on $[a, b]$, then
>
> $$
> \int_a^b \mathbf{r}(t)\,dt = \left( \int_a^b f(t)\,dt \right)\mathbf{i} + \left( \int_a^b g(t)\,dt \right)\mathbf{j} + \left( \int_a^b h(t)\,dt \right)\mathbf{k} .
> $$
>
> *Stewart: 13.2 (boxed)*

^prop-101-4

> [!proof]+ Proof
> Each Riemann sum splits into components:
>
> $$
> \sum_{i=1}^n \mathbf{r}(t_i^*)\,\Delta t = \left( \sum_{i=1}^n f(t_i^*)\,\Delta t \right)\mathbf{i} + \left( \sum_{i=1}^n g(t_i^*)\,\Delta t \right)\mathbf{j} + \left( \sum_{i=1}^n h(t_i^*)\,\Delta t \right)\mathbf{k} .
> $$
>
> Since $f$, $g$, $h$ are continuous, they are integrable ([[§39 The Definite Integral#^thm-39-1|Theorem §39.1]]), so the three component sums converge to $\int_a^b f$, $\int_a^b g$, $\int_a^b h$ as $n \to \infty$, and by [[§100 Vector Functions and Space Curves#^def-100-2|Definition §100.2]] the limit of the vector is the vector of the limits.

^pf-101-4

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^def-101-6|Def. §101.6]], [[§100 Vector Functions and Space Curves#^def-100-2|Def. §100.2]], [[§39 The Definite Integral#^def-39-1|Def. §39.1]], [[§39 The Definite Integral#^thm-39-1|§39.1]]

> [!theorem] Theorem §101.5: Fundamental Theorem of Calculus for Vector Functions
> If $\mathbf{r}$ is continuous on $[a, b]$ and $\mathbf{R}$ is an antiderivative of $\mathbf{r}$, that is, $\mathbf{R}'(t) = \mathbf{r}(t)$, then
>
> $$
> \int_a^b \mathbf{r}(t)\,dt = \mathbf{R}(t)\Big]_a^b = \mathbf{R}(b) - \mathbf{R}(a) .
> $$
>
> *Stewart: 13.2 (text)*

^thm-101-5

> [!proof]+ Proof
> Write $\mathbf{R} = \langle F, G, H \rangle$. By [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|Theorem §101.1]], $\mathbf{R}' = \mathbf{r}$ means $F' = f$, $G' = g$, $H' = h$. By [[§101 Derivatives and Integrals of Vector Functions#^prop-101-4|Proposition §101.4]] and Part 2 of the Fundamental Theorem of Calculus ([[§41 The Fundamental Theorem of Calculus#^thm-41-2|Theorem §41.2]]) in each component,
>
> $$
> \int_a^b \mathbf{r}(t)\,dt = \big\langle F(b) - F(a),\ G(b) - G(a),\ H(b) - H(a) \big\rangle = \mathbf{R}(b) - \mathbf{R}(a) .
> $$

^pf-101-5

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^thm-101-1|§101.1]], [[§101 Derivatives and Integrals of Vector Functions#^prop-101-4|§101.4]], [[§41 The Fundamental Theorem of Calculus#^thm-41-2|§41.2]]

> [!remark]- Connections
> - Componentwise this is [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]] (Stewart's Part 2 of the FTC).
> - Complex-variables version: [[§42 Definite Integrals of Functions w(t)#^thm-42-2|342 Thm. §42.2]] (the fundamental theorem of calculus for complex-valued $w(t)$).

> [!example] Example §118.4: Integrals and Initial Values
> **(a)** If $\mathbf{r}(t) = 2\cos t\,\mathbf{i} + \sin t\,\mathbf{j} + 2t\,\mathbf{k}$, then integrating each component,
>
> $$
> \int \mathbf{r}(t)\,dt = \left( \int 2\cos t\,dt \right)\mathbf{i} + \left( \int \sin t\,dt \right)\mathbf{j} + \left( \int 2t\,dt \right)\mathbf{k} = 2\sin t\,\mathbf{i} - \cos t\,\mathbf{j} + t^2\,\mathbf{k} + \mathbf{C} ,
> $$
>
> where $\mathbf{C}$ is a vector constant of integration, and by [[§101 Derivatives and Integrals of Vector Functions#^thm-101-5|Theorem §101.5]]
>
> $$
> \int_0^{\pi/2} \mathbf{r}(t)\,dt = \Big[2\sin t\,\mathbf{i} - \cos t\,\mathbf{j} + t^2\,\mathbf{k}\Big]_0^{\pi/2} = \Big(2\,\mathbf{i} + \frac{\pi^2}{4}\,\mathbf{k}\Big) - (-\mathbf{j}) = 2\,\mathbf{i} + \mathbf{j} + \frac{\pi^2}{4}\,\mathbf{k} .
> $$
>
> **(b)** A particle has velocity $\mathbf{v}(t) = \langle \sin t, 2\cos 2t, 3e^t \rangle$ and initial position $\mathbf{r}(0) = \langle 1, 2, 0 \rangle$. Find $\mathbf{r}(t)$.
>
> Since $\mathbf{r}' = \mathbf{v}$, integrate each component: $\mathbf{r}(t) = \langle -\cos t, \sin 2t, 3e^t \rangle + \mathbf{C}$. At $t = 0$ this is $\langle -1, 0, 3 \rangle + \mathbf{C} = \langle 1, 2, 0 \rangle$, so $\mathbf{C} = \langle 2, 2, -3 \rangle$ and
>
> $$
> \mathbf{r}(t) = \langle 2 - \cos t,\ 2 + \sin 2t,\ 3e^t - 3 \rangle .
> $$
>
> Check: $\mathbf{r}'(t) = \langle \sin t, 2\cos 2t, 3e^t \rangle$ and $\mathbf{r}(0) = \langle 1, 2, 0 \rangle$.
>
> *Stewart: Example 13.2.4*
> *Source: 233 SI Midterm 1 Problem Set, Q4(c)*

^ex-101-4
