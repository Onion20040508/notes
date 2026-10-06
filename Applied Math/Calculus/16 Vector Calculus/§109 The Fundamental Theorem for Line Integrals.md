---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 109
stewart: "16.3"
aliases: ["Stewart 16.3"]
tags: [calculus, math233]
---
← [[§108 Line Integrals]] · ↑ [[· 16 Vector Calculus]] · [[§110 Green's Theorem]] →

*Stewart, Section 16.3 · MATH 233 (UMass, Spring 2023): Practice Final Set 1 (Part II, Q4), Practice Final Set 2 (Part II, Q3).*

Part 2 of the Fundamental Theorem of Calculus says $\int_a^b F'(x)\,dx = F(b) - F(a)$: to integrate a derivative, only the values at the endpoints are needed. The gradient is a kind of derivative, and the Fundamental Theorem for Line Integrals says the same thing for it: $\int_C \nabla f \cdot d\mathbf{r} = f(\text{end}) - f(\text{start})$. So the line integral of a conservative field depends only on the endpoints of the path, and around a closed path it is $0$. Conversely, a field whose line integrals are independent of path is conservative. The section then answers the two practical questions: how to recognize a conservative field in the plane ($\partial P/\partial y = \partial Q/\partial x$, on a simply-connected region), and how to find its potential function (partial integration). It ends with the reason for the word *conservative*: conservation of energy.

## The Fundamental Theorem for Line Integrals

> [!theorem] Theorem §109.1: The Fundamental Theorem for Line Integrals
> Let $C$ be a [[§88 Arc Length and Curvature#^def-88-3|smooth curve]] given by the vector function $\mathbf{r}(t)$, $a \le t \le b$. Let $f$ be a differentiable function of two or three variables whose gradient vector $\nabla f$ is continuous on $C$. Then
>
> $$
> \int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{r}(b)) - f(\mathbf{r}(a)) .
> $$
>
> The same holds for piecewise-smooth curves. For a plane curve from $A(x_1, y_1)$ to $B(x_2, y_2)$ this reads $\int_C \nabla f \cdot d\mathbf{r} = f(x_2, y_2) - f(x_1, y_1)$, and for a space curve from $A(x_1, y_1, z_1)$ to $B(x_2, y_2, z_2)$ it reads $\int_C \nabla f \cdot d\mathbf{r} = f(x_2, y_2, z_2) - f(x_1, y_1, z_1)$.
>
> *Stewart: 16.3, Theorem 2*

^thm-109-1

> [!proof]+ Proof
> We give the proof for $f$ a function of three variables (two variables is the same with the $z$ terms dropped). By the definition of the line integral of a vector field ([[§108 Line Integrals#^def-108-8|Definition §108.8]]) and the Chain Rule ([[§94 The Chain Rule#^thm-94-1|Theorem §94.1]]),
>
> $$
> \begin{aligned}
> \int_C \nabla f \cdot d\mathbf{r} &= \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_a^b \left( \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \frac{\partial f}{\partial z}\frac{dz}{dt} \right) dt \\
> &= \int_a^b \frac{d}{dt}\, f(\mathbf{r}(t))\,dt = f(\mathbf{r}(b)) - f(\mathbf{r}(a)) .
> \end{aligned}
> $$
>
> The last step is Part 2 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]]), applied to the function $t \mapsto f(\mathbf{r}(t))$, whose derivative is continuous.
>
> If $C$ is piecewise smooth, subdivide it into smooth curves $C_1, \ldots, C_n$, where $C_i$ runs from $\mathbf{r}(t_{i-1})$ to $\mathbf{r}(t_i)$. Adding the results for the pieces, the sum telescopes: $\sum_{i=1}^n \big[f(\mathbf{r}(t_i)) - f(\mathbf{r}(t_{i-1}))\big] = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$.

^pf-109-1

*Uses:* [[§108 Line Integrals#^def-108-8|Def. §108.8]], [[§108 Line Integrals#^def-108-2|Def. §108.2]], [[§94 The Chain Rule#^thm-94-1|§94.1]], [[§36 The Fundamental Theorem of Calculus#^thm-36-2|§36.2]]

> [!remark]- Connections
> - In the language of forms this is the generalized Stokes theorem for a 0-form on a curve, $\int_C df = f(B) - f(A)$: [[§23 The Generalized Stokes' Theorem#^thm-23-1|452 Thm. §23.1]] (hub [[Generalized Stokes' Theorem]]). It is the argument used in [[§22 The Algebra of Differential Forms#^prop-22-11|452 Prop. §22.11]] to show that a form with a nonzero integral around a closed curve is not exact.
> - Complex-variables version: [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|342 Thm. §49.1]] (for contour integrals: having an antiderivative, independence of path and vanishing integrals around closed contours are equivalent).

So the line integral of a conservative field is computed from the values of the potential function at the endpoints alone; in fact $\int_C \nabla f \cdot d\mathbf{r}$ is the net change in $f$. In particular, if $C_1$ and $C_2$ are smooth curves with the same initial point and the same terminal point, then $\int_{C_1} \nabla f \cdot d\mathbf{r} = \int_{C_2} \nabla f \cdot d\mathbf{r}$.

> [!example] Example §109.1: Work Done by Gravity
> Find the work done by the gravitational field $\mathbf{F}(\mathbf{x}) = -\dfrac{mMG}{|\mathbf{x}|^3}\,\mathbf{x}$ in moving a particle with mass $m$ from the point $(3, 4, 12)$ to the point $(2, 2, 0)$ along a piecewise-smooth curve $C$.
>
> By [[§107 Vector Fields#^ex-107-4|Example §107.4]], $\mathbf{F} = \nabla f$ with $f(x, y, z) = \dfrac{mMG}{\sqrt{x^2 + y^2 + z^2}}$. So by [[§109 The Fundamental Theorem for Line Integrals#^thm-109-1|Theorem §109.1]], whatever the curve,
>
> $$
> W = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \nabla f \cdot d\mathbf{r} = f(2, 2, 0) - f(3, 4, 12) = \frac{mMG}{\sqrt{2^2 + 2^2}} - \frac{mMG}{\sqrt{3^2 + 4^2 + 12^2}} = mMG\left( \frac{1}{2\sqrt2} - \frac{1}{13} \right) .
> $$
>
> *Stewart: Example 16.3.1*

^ex-109-1

## Independence of Path

> [!definition] Definition §109.1: Independence of Path
> Piecewise-smooth curves are called **paths**. If $\mathbf{F}$ is a continuous vector field with domain $D$, the line integral $\int_C \mathbf{F} \cdot d\mathbf{r}$ is **independent of path** if $\int_{C_1} \mathbf{F} \cdot d\mathbf{r} = \int_{C_2} \mathbf{F} \cdot d\mathbf{r}$ for any two paths $C_1$ and $C_2$ in $D$ that have the same initial points and the same terminal points.
>
> *Stewart: 16.3 (text)*

^def-109-1

In general, line integrals are not independent of path ([[§108 Line Integrals#^ex-108-3|Example §108.3]]). But by [[§109 The Fundamental Theorem for Line Integrals#^thm-109-1|Theorem §109.1]], *line integrals of conservative vector fields are independent of path.*

> [!definition] Definition §109.2: Closed Curve
> A curve is **closed** if its terminal point coincides with its initial point, that is, $\mathbf{r}(b) = \mathbf{r}(a)$.
>
> *Stewart: 16.3 (text)*

^def-109-2

> [!theorem] Theorem §109.2: Independence of Path and Closed Paths
> $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of path in $D$ if and only if $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every closed path $C$ in $D$.
>
> *Stewart: 16.3, Theorem 3*

^thm-109-2

> [!proof]+ Proof
> ($\Rightarrow$) Let $C$ be a closed path in $D$. Choose two points $A$ and $B$ on $C$ and regard $C$ as the path $C_1$ from $A$ to $B$ followed by the path $C_2$ from $B$ to $A$. Then $C_1$ and $-C_2$ both run from $A$ to $B$, so by independence of path and [[§108 Line Integrals#^thm-108-6|Theorem §108.6]],
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} + \int_{C_2} \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} - \int_{-C_2} \mathbf{F} \cdot d\mathbf{r} = 0 .
> $$
>
> ($\Leftarrow$) Let $C_1$ and $C_2$ be two paths in $D$ from $A$ to $B$, and let $C$ be $C_1$ followed by $-C_2$. Then $C$ is a closed path, so
>
> $$
> 0 = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} + \int_{-C_2} \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} - \int_{C_2} \mathbf{F} \cdot d\mathbf{r} ,
> $$
>
> and $\int_{C_1} \mathbf{F} \cdot d\mathbf{r} = \int_{C_2} \mathbf{F} \cdot d\mathbf{r}$.

^pf-109-2

*Uses:* [[§109 The Fundamental Theorem for Line Integrals#^def-109-1|Def. §109.1]], [[§109 The Fundamental Theorem for Line Integrals#^def-109-2|Def. §109.2]], [[§108 Line Integrals#^thm-108-6|§108.6]], [[§108 Line Integrals#^def-108-2|Def. §108.2]] (integrals over a union of paths add)

Since the line integral of any conservative field is independent of path, $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every closed path. Physically: the work done by a conservative force field (such as the gravitational or electric field of [[§107 Vector Fields#^ex-107-2|Example §107.2]]) as it moves an object around a closed path is $0$. The next theorem says that the *only* fields with path-independent line integrals are the conservative ones. It is stated and proved for plane curves; the version for space curves is similar.

> [!definition] Definition §109.3: Open Region
> A region $D$ is **open** if for every point $P$ in $D$ there is a disk with center $P$ that lies entirely in $D$ (so $D$ contains none of its [[§96 Maximum and Minimum Values#^def-96-new2|boundary points]]).
>
> *Stewart: 16.3 (text)*

^def-109-3

> [!definition] Definition §109.4: Connected Region
> $D$ is **connected** if any two points in $D$ can be joined by a path that lies in $D$.
>
> *Stewart: 16.3 (text)*

^def-109-new1

> [!theorem] Theorem §109.3: Path Independence Implies Conservative
> Suppose $\mathbf{F}$ is a vector field that is continuous on an open connected region $D$. If $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of path in $D$, then $\mathbf{F}$ is a conservative vector field on $D$; that is, there exists a function $f$ such that $\nabla f = \mathbf{F}$.
>
> *Stewart: 16.3, Theorem 4*

^thm-109-3

> [!proof]+ Proof
> Let $A(a, b)$ be a fixed point in $D$, and define
>
> $$
> f(x, y) = \int_{(a, b)}^{(x, y)} \mathbf{F} \cdot d\mathbf{r}
> $$
>
> for any $(x, y)$ in $D$, the integral taken along any path in $D$ from $(a, b)$ to $(x, y)$. Such a path exists because $D$ is connected, and by independence of path the value does not depend on which one is used. So $f$ is well defined.
>
> **$\partial f/\partial x = P$.** Write $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ and fix $(x, y)$ in $D$. Since $D$ is open, there is a disk with center $(x, y)$ contained in $D$. Choose a point $(x_1, y)$ in that disk with $x_1 < x$, and let $C$ be any path $C_1$ from $(a, b)$ to $(x_1, y)$ followed by the horizontal segment $C_2$ from $(x_1, y)$ to $(x, y)$ (it lies in the disk, hence in $D$). Then
>
> $$
> f(x, y) = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} + \int_{C_2} \mathbf{F} \cdot d\mathbf{r} = \int_{(a, b)}^{(x_1, y)} \mathbf{F} \cdot d\mathbf{r} + \int_{C_2} \mathbf{F} \cdot d\mathbf{r} .
> $$
>
> The first integral does not depend on $x$ (for $x$ near the fixed value, $x_1$ can be kept fixed), so
>
> $$
> \frac{\partial}{\partial x} f(x, y) = 0 + \frac{\partial}{\partial x} \int_{C_2} \mathbf{F} \cdot d\mathbf{r} = \frac{\partial}{\partial x} \int_{C_2} P\,dx + Q\,dy
> $$
>
> by [[§108 Line Integrals#^thm-108-7|Theorem §108.7]]. On $C_2$, $y$ is constant, so $dy = 0$. Using $t$ as the parameter, $x_1 \le t \le x$,
>
> $$
> \frac{\partial}{\partial x} f(x, y) = \frac{\partial}{\partial x} \int_{x_1}^{x} P(t, y)\,dt = P(x, y)
> $$
>
> by Part 1 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]), since $t \mapsto P(t, y)$ is continuous.
>
> **$\partial f/\partial y = Q$.** The same argument with a vertical segment from $(x, y_1)$ to $(x, y)$, $y_1 < y$, at the end of the path (now $dx = 0$) gives
>
> $$
> \frac{\partial}{\partial y} f(x, y) = \frac{\partial}{\partial y} \int_{y_1}^{y} Q(x, t)\,dt = Q(x, y) .
> $$
>
> Thus $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} = \dfrac{\partial f}{\partial x}\,\mathbf{i} + \dfrac{\partial f}{\partial y}\,\mathbf{j} = \nabla f$, which says that $\mathbf{F}$ is conservative.

^pf-109-3

*Uses:* [[§109 The Fundamental Theorem for Line Integrals#^def-109-1|Def. §109.1]], [[§109 The Fundamental Theorem for Line Integrals#^def-109-3|Def. §109.3]], [[§109 The Fundamental Theorem for Line Integrals#^def-109-new1|Def. §109.4]], [[§108 Line Integrals#^thm-108-7|§108.7]], [[§108 Line Integrals#^def-108-2|Def. §108.2]], [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]], [[§107 Vector Fields#^def-107-4|Def. §107.4]]

![[m233-109-1.svg]]
*The potential in the proof of [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Theorem §109.3]]: $f(x,y)$ is the line integral of $\mathbf{F}$ from the base point $(a,b)$ to $(x,y)$, along any path. To differentiate in $x$, end the path with a short horizontal segment $C_2$ (red) inside a disk in $D$ (open region). Only $C_2$ depends on $x$, and along it the integral is $\int_{x_1}^{x} P(t,y)\,dt$, whose $x$-derivative is $P(x,y)$. A vertical last segment gives $\partial f/\partial y = Q$ in the same way.*

*The section continues in [[§109a Conservative Vector Fields and Potential Functions]].*
