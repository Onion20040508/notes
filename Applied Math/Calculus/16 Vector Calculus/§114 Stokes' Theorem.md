---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 114
stewart: "16.8"
aliases: ["Stewart 16.8"]
tags: [calculus, math233]
---
← [[§113 Surface Integrals]] · ↑ [[· 16 Vector Calculus]] · [[§115 The Divergence Theorem]] →

*Stewart, Section 16.8 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q9(c)), Practice Final Exam (Q1(c), Q6), Practice Final Set 1 (Part II, Q2), Practice Final Set 2 (Part II, Q5).*

Stokes' Theorem is Green's Theorem for curved surfaces. It relates the line integral of a vector field around the boundary curve $C$ of an oriented surface $S$ in space to the flux of its curl through $S$: $\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S}$. In practice it is used in two directions. A line integral around a complicated space curve becomes a flux integral over a simple surface bounded by it (often a flat disk). And the flux of a curl through a complicated surface can be computed on the boundary curve, or on any other surface with the same boundary. The theorem also explains the curl: its component along $\mathbf{n}$ is the circulation per unit area around $\mathbf{n}$. Finally it proves that a curl-free field on $\mathbb{R}^3$ is conservative.

## Stokes' Theorem

> [!definition] Definition §114.1: Positive Orientation of the Boundary Curve
> Let $S$ be an oriented surface with unit normal vector $\mathbf{n}$, bounded by a closed curve $C$. The orientation of $S$ induces the **positive orientation of the boundary curve $C$**: if you walk in the positive direction around $C$ with your head pointing in the direction of $\mathbf{n}$, the surface is always on your left. The positively oriented boundary curve of $S$ is written $\partial S$.
>
> *Stewart: 16.8 (text)*

^def-114-1

For example, if $S$ is oriented upward, $C$ is traversed counterclockwise as viewed from above; reversing $\mathbf{n}$ reverses $C$. (Curl the fingers of your right hand in the direction of $C$; your thumb points along $\mathbf{n}$.)

> [!theorem] Theorem §114.1: Stokes' Theorem
> Let $S$ be an oriented piecewise-smooth surface that is bounded by a simple, closed, piecewise-smooth boundary curve $C$ with positive orientation. Let $\mathbf{F}$ be a vector field whose components have continuous partial derivatives on an open region in $\mathbb{R}^3$ that contains $S$. Then
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S}, \qquad\text{that is,}\qquad \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \int_{\partial S} \mathbf{F} \cdot d\mathbf{r} . \qquad (1)
> $$
>
> Since $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F} \cdot \mathbf{T}\,ds$ and $\iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_S \operatorname{curl}\mathbf{F} \cdot \mathbf{n}\,dS$: the line integral around the boundary curve of the tangential component of $\mathbf{F}$ equals the surface integral over $S$ of the normal component of the curl of $\mathbf{F}$.
>
> *Stewart: 16.8, Stokes' Theorem and Equation 1*

^thm-114-1

> [!proof]+ Proof
> *Stewart says that the theorem is too difficult to prove in full generality at this level, and proves it when $S$ is a graph and $\mathbf{F}$, $S$ and $C$ are well behaved. The general proof (parametrized surfaces, reduced to Green's Theorem on the parameter domain) is in [[§20 Stokes' Theorem in ℝ³#^thm-20-1|452 Thm. §20.1]].*
>
> **Special case: $S$ is a graph.** Assume $S$ has equation $z = g(x, y)$, $(x, y) \in D$, where $g$ has continuous second-order partial derivatives and $D$ is a simple plane region ([[§110 Green's Theorem#^def-110-2|Definition §110.2]]) whose boundary curve $C_1$ corresponds to $C$. Orient $S$ upward; then the positive orientation of $C$ corresponds to the positive orientation of $C_1$. Let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$, with continuous partial derivatives.
>
> **The surface integral.** Apply Formula 10 of [[§113 Surface Integrals#^thm-113-4|Theorem §113.4]] with $\mathbf{F}$ replaced by $\operatorname{curl}\mathbf{F}$ ([[§111 Curl and Divergence#^def-111-1|Definition §111.1]]):
>
> $$
> \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_D \left[ -\left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)\frac{\partial z}{\partial x} - \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)\frac{\partial z}{\partial y} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \right] dA , \qquad (2)
> $$
>
> where the partial derivatives of $P$, $Q$, $R$ are evaluated at $(x, y, g(x, y))$.
>
> **The line integral.** If $x = x(t)$, $y = y(t)$, $a \le t \le b$, is a parametric representation of $C_1$, then $x = x(t)$, $y = y(t)$, $z = g(x(t), y(t))$ is one of $C$, and by the Chain Rule $\dfrac{dz}{dt} = \dfrac{\partial z}{\partial x}\dfrac{dx}{dt} + \dfrac{\partial z}{\partial y}\dfrac{dy}{dt}$. So
>
> $$
> \begin{aligned}
> \int_C \mathbf{F} \cdot d\mathbf{r} &= \int_a^b \left( P\frac{dx}{dt} + Q\frac{dy}{dt} + R\frac{dz}{dt} \right) dt = \int_a^b \left[ P\frac{dx}{dt} + Q\frac{dy}{dt} + R\left( \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} \right) \right] dt \\
> &= \int_a^b \left[ \left( P + R\frac{\partial z}{\partial x} \right)\frac{dx}{dt} + \left( Q + R\frac{\partial z}{\partial y} \right)\frac{dy}{dt} \right] dt = \int_{C_1} \left( P + R\frac{\partial z}{\partial x} \right) dx + \left( Q + R\frac{\partial z}{\partial y} \right) dy \\
> &= \iint_D \left[ \frac{\partial}{\partial x}\left( Q + R\frac{\partial z}{\partial y} \right) - \frac{\partial}{\partial y}\left( P + R\frac{\partial z}{\partial x} \right) \right] dA
> \end{aligned}
> $$
>
> by Green's Theorem on $D$ ([[§110 Green's Theorem#^thm-110-1|Theorem §110.1]]). Now differentiate with the Chain Rule, remembering that $P$, $Q$, $R$ are functions of $x$, $y$ and $z$, and $z = g(x, y)$:
>
> $$
> \begin{aligned}
> \frac{\partial}{\partial x}\left( Q + R\frac{\partial z}{\partial y} \right) &= \frac{\partial Q}{\partial x} + \frac{\partial Q}{\partial z}\frac{\partial z}{\partial x} + \frac{\partial R}{\partial x}\frac{\partial z}{\partial y} + \frac{\partial R}{\partial z}\frac{\partial z}{\partial x}\frac{\partial z}{\partial y} + R\frac{\partial^2 z}{\partial x\,\partial y}, \\
> \frac{\partial}{\partial y}\left( P + R\frac{\partial z}{\partial x} \right) &= \frac{\partial P}{\partial y} + \frac{\partial P}{\partial z}\frac{\partial z}{\partial y} + \frac{\partial R}{\partial y}\frac{\partial z}{\partial x} + \frac{\partial R}{\partial z}\frac{\partial z}{\partial y}\frac{\partial z}{\partial x} + R\frac{\partial^2 z}{\partial y\,\partial x} .
> \end{aligned}
> $$
>
> Subtract. The terms with $\partial R/\partial z$ cancel, and so do the terms with $R$, because $\partial^2 z/\partial x\,\partial y = \partial^2 z/\partial y\,\partial x$ by Clairaut's Theorem ([[§92 Partial Derivatives#^thm-92-2|Theorem §92.2]]). Six terms remain:
>
> $$
> \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} + \frac{\partial Q}{\partial z}\frac{\partial z}{\partial x} - \frac{\partial R}{\partial y}\frac{\partial z}{\partial x} + \frac{\partial R}{\partial x}\frac{\partial z}{\partial y} - \frac{\partial P}{\partial z}\frac{\partial z}{\partial y} ,
> $$
>
> which is exactly the integrand of (2), rearranged. (Stewart states that "four of the terms cancel and the remaining six can be arranged to coincide"; the display above is that bookkeeping.) Hence $\int_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S}$.

^pf-114-1

*Uses:* [[§114 Stokes' Theorem#^def-114-1|Def. §114.1]], [[§113 Surface Integrals#^thm-113-4|§113.4]], [[§111 Curl and Divergence#^def-111-1|Def. §111.1]], [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§110 Green's Theorem#^def-110-2|Def. §110.2]], [[§108 Line Integrals#^thm-108-7|§108.7]], [[§94 The Chain Rule#^thm-94-1|§94.1]], [[§94 The Chain Rule#^thm-94-3|§94.3]] (Chain Rule), [[§92 Partial Derivatives#^thm-92-2|§92.2]] (Clairaut's Theorem)

![[m233-114-1.svg]]
*The special case in the proof. $S$ (blue) is the graph of $g$ over the plane region $D$ (gray), oriented upward, and its boundary $C$ sits directly above the boundary $C_1$ of $D$. Both run counterclockwise seen from above, so the walker on $C$ with head along $\mathbf{n}$ has $S$ on the left. Substituting $z = g(x, y)$ pushes the line integral down from $C$ to $C_1$, where Green's Theorem applies.*

> [!remark]- Connections
> - Rigorous treatment: [[§20 Stokes' Theorem in ℝ³#^thm-20-1|452 Thm. §20.1]], proved there first for graphs exactly as above and then for parametrized surfaces (hub [[Stokes' Theorem in ℝ³]]; orientation convention [[§20 Stokes' Theorem in ℝ³#^rem-20-1|452 Remark: Orientation Convention]]). With Green's Theorem, the Divergence Theorem and the Fundamental Theorem for Line Integrals it is a case of the [[Generalized Stokes' Theorem]], [[§23 The Generalized Stokes' Theorem#^thm-23-1|452 Thm. §23.1]].

> [!remark] Remark: Green's Theorem as a Special Case
> Stokes' Theorem, Green's Theorem and the Fundamental Theorem of Calculus are analogous: on the left of (1) is an integral involving derivatives ($\operatorname{curl}\mathbf{F}$ is a sort of derivative of $\mathbf{F}$), and on the right only the values of $\mathbf{F}$ on the *boundary* of $S$. In fact, if $S$ is flat and lies in the $xy$-plane with upward orientation, the unit normal is $\mathbf{k}$, the surface integral becomes a double integral, and Stokes' Theorem becomes
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_S (\operatorname{curl}\mathbf{F}) \cdot \mathbf{k}\,dA ,
> $$
>
> which is the vector form of Green's Theorem, [[§111 Curl and Divergence#^thm-111-4|Theorem §111.4]]. So Green's Theorem is really a special case of Stokes' Theorem.

^rem-114-1

> [!theorem] Corollary §114.2: Surfaces with the Same Boundary
> If $S_1$ and $S_2$ are oriented surfaces with the same oriented boundary curve $C$ and both satisfy the hypotheses of Stokes' Theorem, then
>
> $$
> \iint_{S_1} \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_{S_2} \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} . \qquad (3)
> $$
>
> *Stewart: 16.8, Equation 3*

^cor-114-2

> [!proof]+ Proof
> Apply [[§114 Stokes' Theorem#^thm-114-1|Theorem §114.1]] to $S_1$ and to $S_2$; both surface integrals equal the same line integral around $C$.

^pf-114-2

*Uses:* [[§114 Stokes' Theorem#^thm-114-1|§114.1]]

So the flux of a curl through a surface depends only on the boundary curve. This is useful when it is hard to integrate over one surface but easy over another.

> [!remark] Remark: Method — Using Stokes' Theorem
> 1. **For a line integral $\oint_C \mathbf{F} \cdot d\mathbf{r}$ around a closed space curve:** compute $\operatorname{curl}\mathbf{F}$, and choose the simplest surface $S$ with boundary $C$, usually the flat piece of a plane (a disk, an ellipse, a polygon) or a piece of a surface on which $C$ lies.
> 2. **For the flux of a curl $\iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S}$:** either compute $\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$ directly, or replace $S$ by a simpler surface with the same boundary (Corollary §114.2).
> 3. **Match the orientations** (Definition §114.1): counterclockwise from above goes with the upward normal; for a curve described "as viewed from the positive $x$-axis", the matching normal points toward $+x$.
> 4. **Evaluate** with Formula 9 or 10 ([[§113 Surface Integrals#^thm-113-3|Theorem §113.3]], [[§113 Surface Integrals#^thm-113-4|Theorem §113.4]]); on a horizontal disk $\operatorname{curl}\mathbf{F} \cdot \mathbf{k}$ is just the $\mathbf{k}$-component, and if it is constant the answer is that constant times the area.

^rem-114-2

> [!example] Example §114.1: Curves Cut by a Cylinder and a Plane
> **(a)** Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $\mathbf{F}(x, y, z) = -y^2\,\mathbf{i} + x\,\mathbf{j} + z^2\,\mathbf{k}$ and $C$ is the curve of intersection of the plane $y + z = 2$ and the cylinder $x^2 + y^2 = 1$, oriented counterclockwise when viewed from above.
>
> $C$ is an ellipse. The integral could be evaluated directly, but Stokes' Theorem is easier. First,
>
> $$
> \operatorname{curl}\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[6pt] -y^2 & x & z^2 \end{vmatrix} = (0 - 0)\,\mathbf{i} - (0 - 0)\,\mathbf{j} + (1 + 2y)\,\mathbf{k} = (1 + 2y)\,\mathbf{k} .
> $$
>
> Of the many surfaces with boundary $C$, choose the elliptical region $S$ in the plane $y + z = 2$ bounded by $C$. Orienting $S$ upward gives $C$ the induced positive orientation. $S$ is the graph of $g(x, y) = 2 - y$ over the disk $D$: $x^2 + y^2 \le 1$, so Formula 10 (with $P = Q = 0$, $R = 1 + 2y$) gives
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_D (1 + 2y)\,dA = \int_0^{2\pi} \int_0^1 (1 + 2r\sin\theta)\,r\,dr\,d\theta = \int_0^{2\pi} \left( \frac12 + \frac23\sin\theta \right) d\theta = \frac12(2\pi) + 0 = \pi .
> $$
>
> **(b)** The same steps for $\mathbf{F} = \langle x^2z, xy^2, z^2 \rangle$ and $C$ the intersection of the plane $x + y + z = 1$ with the cylinder $x^2 + y^2 = 9$, counterclockwise from above: $\operatorname{curl}\mathbf{F} = \langle 0 - 0,\ x^2 - 0,\ y^2 - 0 \rangle = \langle 0, x^2, y^2 \rangle$, and the plane piece $z = 1 - x - y$ over $x^2 + y^2 \le 9$ has upward normal $\langle 1, 1, 1 \rangle$. So
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_D (x^2 + y^2)\,dA = \int_0^{2\pi} \int_0^3 r^3\,dr\,d\theta = 2\pi \cdot \frac{81}{4} = \frac{81\pi}{2} .
> $$
>
> *Stewart: Example 16.8.1*
> *Source: 233 Practice Final Set 2, Part II Q5 (= Stewart Exercise 16.8.15a)*

^ex-114-1

> [!example] Example §114.2: The Flux of a Curl, Two Ways
> Compute $\iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S}$, where $\mathbf{F}(x, y, z) = xz\,\mathbf{i} + yz\,\mathbf{j} + xy\,\mathbf{k}$ and $S$ is the part of the sphere $x^2 + y^2 + z^2 = 4$ that lies inside the cylinder $x^2 + y^2 = 1$ and above the $xy$-plane (oriented upward).
>
> **Solution 1: on the boundary curve.** The boundary $C$: from $x^2 + y^2 + z^2 = 4$ and $x^2 + y^2 = 1$, subtracting, $z^2 = 3$, so $z = \sqrt3$ (since $z > 0$). So $C$ is the circle $x^2 + y^2 = 1$, $z = \sqrt3$: $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + \sqrt3\,\mathbf{k}$, $0 \le t \le 2\pi$, with $\mathbf{r}'(t) = -\sin t\,\mathbf{i} + \cos t\,\mathbf{j}$ and $\mathbf{F}(\mathbf{r}(t)) = \sqrt3\cos t\,\mathbf{i} + \sqrt3\sin t\,\mathbf{j} + \cos t\sin t\,\mathbf{k}$. By Stokes' Theorem,
>
> $$
> \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \int_C \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} \big( -\sqrt3\cos t\sin t + \sqrt3\sin t\cos t \big)\,dt = \sqrt3 \int_0^{2\pi} 0\,dt = 0 .
> $$
>
> **Solution 2: on another surface.** Let $S_1$ be the disk in the plane $z = \sqrt3$ inside the cylinder $x^2 + y^2 = 1$. It has the same boundary $C$, so by Corollary §114.2 the two fluxes agree. $S_1$ is horizontal with upward normal $\mathbf{k}$, and
>
> $$
> \operatorname{curl}\mathbf{F} = (x - y)\,\mathbf{i} + (x - y)\,\mathbf{j} + (0 - 0)\,\mathbf{k}, \qquad \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_{S_1} \big[(x - y)\,\mathbf{i} + (x - y)\,\mathbf{j}\big] \cdot \mathbf{k}\,dS = \iint_{S_1} 0\,dS = 0 .
> $$
>
> *Stewart: Example 16.8.2*

^ex-114-2

> [!example] Example §114.3: Work along a Curve on a Saddle
> Find the work done by $\mathbf{F} = x^2y\,\mathbf{i} + \frac13 x^3\,\mathbf{j} + xy\,\mathbf{k}$ along the curve $C$ of intersection of the hyperbolic paraboloid $z = y^2 - x^2$ and the cylinder $x^2 + y^2 = 1$, oriented counterclockwise as viewed from above.
>
> **By Stokes' Theorem.**
>
> $$
> \operatorname{curl}\mathbf{F} = \left( \frac{\partial(xy)}{\partial y} - \frac{\partial(\frac13 x^3)}{\partial z} \right)\mathbf{i} + \left( \frac{\partial(x^2y)}{\partial z} - \frac{\partial(xy)}{\partial x} \right)\mathbf{j} + \left( \frac{\partial(\frac13 x^3)}{\partial x} - \frac{\partial(x^2y)}{\partial y} \right)\mathbf{k} = x\,\mathbf{i} - y\,\mathbf{j} + 0\,\mathbf{k} .
> $$
>
> $C$ lies on the saddle, so take $S$ = the part of $z = g(x, y) = y^2 - x^2$ over the disk $D$: $x^2 + y^2 \le 1$, oriented upward (matching counterclockwise from above). Then $g_x = -2x$, $g_y = 2y$, and Formula 10 gives
>
> $$
> W = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_D \big[ -x(-2x) - (-y)(2y) + 0 \big]\,dA = \iint_D 2(x^2 + y^2)\,dA = \int_0^{2\pi} \int_0^1 2r^2 \cdot r\,dr\,d\theta = 2\pi \cdot \frac12 = \pi .
> $$
>
> **Directly.** The posted solution parametrizes $C$ by $\mathbf{r}(\theta) = \langle \cos\theta, \sin\theta, \sin^2\theta - \cos^2\theta \rangle$, $0 \le \theta \le 2\pi$, so $\mathbf{r}'(\theta) = \langle -\sin\theta, \cos\theta, 4\sin\theta\cos\theta \rangle$ and
>
> $$
> \mathbf{F}(\mathbf{r}(\theta)) \cdot \mathbf{r}'(\theta) = -\cos^2\theta\sin^2\theta + \tfrac13\cos^4\theta + 4\cos^2\theta\sin^2\theta = 3\cos^2\theta\sin^2\theta + \tfrac13\cos^4\theta .
> $$
>
> Since $\int_0^{2\pi} \cos^2\theta\sin^2\theta\,d\theta = \frac{\pi}{4}$ and $\int_0^{2\pi} \cos^4\theta\,d\theta = \frac{3\pi}{4}$, $W = \frac{3\pi}{4} + \frac{\pi}{4} = \pi$, the same answer with more trigonometry.
>
> *Source: 233 Practice Final Set 1, Part II Q2 (= Stewart Exercise 16.8.16a)*

^ex-114-3

> [!example] Example §114.4: Any Capping Surface
> Let $C$ be the circle $y^2 + z^2 = 2$, $x = 0$, oriented counterclockwise when viewed from the positive $x$-axis, and let $S$ be any oriented capping surface of $C$ such that $C$ is positively oriented with respect to $S$. Find $n$ with
>
> $$
> \iint_S \nabla \times (xyz\,\mathbf{i} + z\,\mathbf{j} - y\,\mathbf{k}) \cdot d\mathbf{S} = n\pi .
> $$
>
> Let $\mathbf{G} = xyz\,\mathbf{i} + z\,\mathbf{j} - y\,\mathbf{k}$. By [[§114 Stokes' Theorem#^cor-114-2|Corollary §114.2]] the flux is the same for every such $S$, and equals $\oint_C \mathbf{G} \cdot d\mathbf{r}$.
>
> **On the curve.** Seen from the positive $x$-axis, the $y$-axis points right and the $z$-axis up, so $\mathbf{r}(t) = \langle 0, \sqrt2\cos t, \sqrt2\sin t \rangle$, $0 \le t \le 2\pi$, runs counterclockwise. On $C$, $x = 0$, so $\mathbf{G}(\mathbf{r}(t)) = \langle 0,\ \sqrt2\sin t,\ -\sqrt2\cos t \rangle$, and with $\mathbf{r}'(t) = \langle 0, -\sqrt2\sin t, \sqrt2\cos t \rangle$,
>
> $$
> \oint_C \mathbf{G} \cdot d\mathbf{r} = \int_0^{2\pi} \big( -2\sin^2 t - 2\cos^2 t \big)\,dt = -4\pi .
> $$
>
> **On the flat cap.** Check with $S$ = the disk $y^2 + z^2 \le 2$ in the plane $x = 0$; the normal matching the orientation of $C$ is $\mathbf{i}$. Here
>
> $$
> \nabla \times \mathbf{G} = \left( \frac{\partial(-y)}{\partial y} - \frac{\partial z}{\partial z} \right)\mathbf{i} + \left( \frac{\partial(xyz)}{\partial z} - \frac{\partial(-y)}{\partial x} \right)\mathbf{j} + \left( \frac{\partial z}{\partial x} - \frac{\partial(xyz)}{\partial y} \right)\mathbf{k} = -2\,\mathbf{i} + xy\,\mathbf{j} - xz\,\mathbf{k} ,
> $$
>
> which is $-2\,\mathbf{i}$ on the disk ($x = 0$), so the flux is $-2 \cdot \text{area} = -2 \cdot 2\pi = -4\pi$. Hence $n = -4$.
>
> *Source: 233 Practice Final Exam, Q6*

^ex-114-4

> [!example] Example §114.5: A Cone Meets a Sphere
> Let $\mathbf{F}(x, y, z) = \langle \sin z, x, \cos y \rangle$. Use Stokes' Theorem to calculate $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $C$ is the curve of intersection of the cone $z = \sqrt{x^2 + y^2}$ and the sphere $x^2 + y^2 + z^2 = 9$.
>
> **The curve.** On the cone $x^2 + y^2 = z^2$, so the sphere gives $2z^2 = 9$, $z = 3/\sqrt2$ (positive on the cone). So $C$ is the horizontal circle $x^2 + y^2 = \frac92$, $z = \frac{3}{\sqrt2}$. The problem gives no orientation; take $C$ counterclockwise as viewed from above, as the posted solution does (the reverse orientation changes the sign of the answer).
>
> **The surface.** Take the flat disk $S$: $x^2 + y^2 \le \frac92$ in the plane $z = 3/\sqrt2$, with upward normal $\mathbf{k}$. Then
>
> $$
> \operatorname{curl}\mathbf{F} = \left( \frac{\partial(\cos y)}{\partial y} - \frac{\partial x}{\partial z} \right)\mathbf{i} + \left( \frac{\partial(\sin z)}{\partial z} - \frac{\partial(\cos y)}{\partial x} \right)\mathbf{j} + \left( \frac{\partial x}{\partial x} - \frac{\partial(\sin z)}{\partial y} \right)\mathbf{k} = -\sin y\,\mathbf{i} + \cos z\,\mathbf{j} + \mathbf{k} ,
> $$
>
> so $\operatorname{curl}\mathbf{F} \cdot \mathbf{k} = 1$ and
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_S 1\,dS = \text{area of the disk} = \pi \cdot \frac92 = \frac{9\pi}{2} .
> $$
>
> *Source: 233 Chapter 16 Review, Q9(c)*

^ex-114-5

## The Meaning of Curl

> [!definition] Definition §114.2: Circulation
> Let $C$ be an oriented closed curve and $\mathbf{v}$ the velocity field of a fluid. The line integral
>
> $$
> \int_C \mathbf{v} \cdot d\mathbf{r} = \int_C \mathbf{v} \cdot \mathbf{T}\,ds
> $$
>
> is called the **circulation** of $\mathbf{v}$ around $C$. Since $\mathbf{v} \cdot \mathbf{T}$ is the component of $\mathbf{v}$ in the direction of $\mathbf{T}$ (larger the closer $\mathbf{v}$ is to $\mathbf{T}$, negative when they point in roughly opposite directions), the circulation measures the tendency of the fluid to move around $C$ in the direction of its orientation.
>
> *Stewart: 16.8 (text)*

^def-114-2

> [!theorem] Theorem §114.3: Curl as Circulation per Unit Area
> Let $P_0(x_0, y_0, z_0)$ be a point in the fluid, $\mathbf{n}$ a unit vector, $S_a$ the disk with radius $a$ and center $P_0$ perpendicular to $\mathbf{n}$, and $C_a$ its boundary circle, oriented positively with respect to $\mathbf{n}$. If the components of $\mathbf{v}$ have continuous partial derivatives, then
>
> $$
> \operatorname{curl}\mathbf{v}(P_0) \cdot \mathbf{n}(P_0) = \lim_{a \to 0} \frac{1}{\pi a^2} \int_{C_a} \mathbf{v} \cdot d\mathbf{r} . \qquad (4)
> $$
>
> *Stewart: 16.8, Equation 4*

^thm-114-3

> [!proof]+ Proof
> *Stewart gives this as a sketch: for $P$ on $S_a$, $(\operatorname{curl}\mathbf{v})(P) \approx (\operatorname{curl}\mathbf{v})(P_0)$, so $\int_{C_a} \mathbf{v} \cdot d\mathbf{r} \approx \operatorname{curl}\mathbf{v}(P_0) \cdot \mathbf{n}(P_0)\,\pi a^2$, "and the approximation becomes better as $a \to 0$". Here is the estimate behind that.*
>
> By Stokes' Theorem, with $\mathbf{n}$ constant on the flat disk $S_a$,
>
> $$
> \int_{C_a} \mathbf{v} \cdot d\mathbf{r} = \iint_{S_a} \operatorname{curl}\mathbf{v} \cdot \mathbf{n}\,dS , \qquad\text{so}\qquad
> \int_{C_a} \mathbf{v} \cdot d\mathbf{r} - \operatorname{curl}\mathbf{v}(P_0) \cdot \mathbf{n}\,\pi a^2 = \iint_{S_a} \big[\operatorname{curl}\mathbf{v}(P) - \operatorname{curl}\mathbf{v}(P_0)\big] \cdot \mathbf{n}\,dS ,
> $$
>
> using $\iint_{S_a} dS = \pi a^2$. Since $|\mathbf{w} \cdot \mathbf{n}| \le |\mathbf{w}|$ for a unit vector $\mathbf{n}$, the right side is at most $\pi a^2 \cdot M(a)$ in absolute value, where $M(a)$ is the largest value of $|\operatorname{curl}\mathbf{v}(P) - \operatorname{curl}\mathbf{v}(P_0)|$ for $P$ on $S_a$. Dividing by $\pi a^2$,
>
> $$
> \left| \frac{1}{\pi a^2} \int_{C_a} \mathbf{v} \cdot d\mathbf{r} - \operatorname{curl}\mathbf{v}(P_0) \cdot \mathbf{n} \right| \le M(a) .
> $$
>
> $\operatorname{curl}\mathbf{v}$ is continuous (its components are differences of continuous partial derivatives), and every point of $S_a$ is within distance $a$ of $P_0$, so $M(a) \to 0$ as $a \to 0$. This proves (4).

^pf-114-3

*Uses:* [[§114 Stokes' Theorem#^thm-114-1|§114.1]], [[§114 Stokes' Theorem#^def-114-2|Def. §114.2]], [[§111 Curl and Divergence#^def-111-1|Def. §111.1]], [[§113 Surface Integrals#^def-113-7|Def. §113.7]]

> [!remark]- Connections
> - See also: [[§124★ Two-Dimensional Fluid Flow#^prop-124-2|342 Prop. §124.2]] (the planar case: the rotation of a plane flow as the limiting angular speed on small circles).

> [!remark] Remark: The Paddle Wheel and the Axis of Fastest Rotation
> Equation 4 says that $\operatorname{curl}\mathbf{v} \cdot \mathbf{n}$ measures the rotating effect of the fluid about the axis $\mathbf{n}$: a tiny paddle wheel at $P_0$ with axis $\mathbf{n}$ turns at a rate proportional to it. The curling effect is greatest about the axis parallel to $\operatorname{curl}\mathbf{v}$, because $\operatorname{curl}\mathbf{v} \cdot \mathbf{n} = |\operatorname{curl}\mathbf{v}|\cos\theta$ is largest when the angle $\theta$ between them is $0$.
>
> For example, for $\mathbf{F} = \langle z - y,\ x - z,\ -x - y \rangle$,
>
> $$
> \operatorname{curl}\mathbf{F} = \big( (-1) - (-1),\ 1 - (-1),\ 1 - (-1) \big) = \langle 0, 2, 2 \rangle ,
> $$
>
> so the unit normal that maximizes the rotation is $\dfrac{\langle 0, 2, 2 \rangle}{2\sqrt2} = \dfrac{1}{\sqrt2}(\mathbf{j} + \mathbf{k})$. (The option $\langle 0, 2, 2 \rangle$ itself has the right direction but is not a unit vector.)
>
> *Source: 233 Practice Final Exam, Q1(c)*

^rem-114-3

## Curl-Free Fields on ℝ³ Are Conservative

Stokes' Theorem supplies the proof, announced in §111 after [[§111 Curl and Divergence#^cor-111-2|Corollary §111.2]] (of which it is a partial converse), of the three-dimensional test for conservative fields.

> [!theorem] Theorem §114.4: Curl-Free Fields on ℝ³ Are Conservative
> If $\mathbf{F}$ is a vector field defined on all of $\mathbb{R}^3$ whose component functions have continuous partial derivatives and $\operatorname{curl}\mathbf{F} = \mathbf{0}$, then $\mathbf{F}$ is a conservative vector field.
>
> *Stewart: 16.5, Theorem 4 (proof sketched in 16.8)*

^thm-114-4

> [!proof]+ Proof
> *Stewart gives this as a sketch.* By [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|Theorem §109.2]] and the space version of [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Theorem §109.3]] (same proof with three coordinates; $\mathbb{R}^3$ is open and connected), it suffices to show that $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every closed path $C$.
>
> Let $C$ be a simple closed path, and suppose we can find an orientable surface $S$ whose boundary is $C$. (This can be done, but the proof requires advanced techniques.) Then Stokes' Theorem gives
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}\mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{0} \cdot d\mathbf{S} = 0 .
> $$
>
> A curve that is not simple can be broken into a number of simple closed curves, and the integrals around these are all $0$. Adding them, $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for any closed curve $C$.
>
> (The two steps taken on trust, the existence of the surface and the decomposition into simple curves, are what make this a sketch. More generally the conclusion holds on any simply-connected domain, [[§23 The Fundamental Group#^def-23-3|590 Def. §23.3]].)

^pf-114-4

*Uses:* [[§114 Stokes' Theorem#^thm-114-1|§114.1]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|§109.2]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|§109.3]]

> [!remark]- Connections
> - Rigorous treatment, with a different proof that avoids surfaces: on a star-shaped domain (such as $\mathbb{R}^3$) every closed form is exact, [[§22 The Algebra of Differential Forms#^prop-22-12|452 Prop. §22.12]] ([[Poincaré Lemma]]); for 1-forms on $\mathbb{R}^3$ "closed" means $\operatorname{curl}\mathbf{F} = \mathbf{0}$ and "exact" means conservative ([[§22 The Algebra of Differential Forms#^def-22-8|452 Def. §22.8]]). The plane analog is [[§110 Green's Theorem#^thm-110-5|Theorem §110.5]].
