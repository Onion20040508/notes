---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 129
stewart: "16.3"
aliases: ["Stewart 16.3 (cont.)"]
tags: [calculus, math233]
---
← [[§128 The Fundamental Theorem for Line Integrals]] · ↑ [[· 16 Vector Calculus]] · [[§130 Green's Theorem]] →

*Stewart, Section 16.3 · MATH 233 (UMass, Spring 2023): Practice Final Set 1 (Part II, Q4), Practice Final Set 2 (Part II, Q3).*

Two practical questions remain: how to recognize a conservative field in the plane ($\partial P/\partial y = \partial Q/\partial x$, on a simply-connected region), and how to find its potential function (partial integration). The section ends with the reason for the word *conservative*: conservation of energy.

## Conservative Vector Fields and Potential Functions

How can we tell whether a field $\mathbf{F}$ is conservative, and if it is, how can we find a potential function? Suppose $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ is conservative, with $P$ and $Q$ having continuous first-order partial derivatives. Then $P = \partial f/\partial x$ and $Q = \partial f/\partial y$ for some $f$, and Clairaut's Theorem gives a necessary condition.

> [!theorem] Theorem §129.1: A Necessary Condition for Conservative Fields
> If $\mathbf{F}(x, y) = P(x, y)\,\mathbf{i} + Q(x, y)\,\mathbf{j}$ is a conservative vector field, where $P$ and $Q$ have continuous first-order partial derivatives on a domain $D$, then throughout $D$
>
> $$
> \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} .
> $$
>
> *Stewart: 16.3, Theorem 5*

^thm-129-1

> [!proof]+ Proof
> There is $f$ with $\mathbf{F} = \nabla f$, so $P = \partial f/\partial x$ and $Q = \partial f/\partial y$. The second-order partial derivatives $f_{xy} = \partial P/\partial y$ and $f_{yx} = \partial Q/\partial x$ are continuous on $D$, so by Clairaut's Theorem ([[§108 Partial Derivatives#^thm-108-2|Theorem §108.2]])
>
> $$
> \frac{\partial P}{\partial y} = \frac{\partial^2 f}{\partial y\,\partial x} = \frac{\partial^2 f}{\partial x\,\partial y} = \frac{\partial Q}{\partial x} .
> $$

^pf-129-1

*Uses:* [[§125 Vector Fields#^def-125-4|Def. §125.4]], [[§108 Partial Derivatives#^thm-108-2|§108.2]]

> [!remark]- Connections
> - In 452 this is "exact implies closed", [[§39 Closed and Exact Forms#^prop-39-5|452 Prop. §39.5]]; its three-dimensional form $\operatorname{curl}(\nabla f) = \mathbf{0}$ is [[§132 Curl and Divergence#^thm-132-1|Theorem §132.1]]. The field of [[§131 Extended Versions of Green's Theorem#^ex-131-2|Example §131.2]] satisfies the condition without being conservative, so the converse needs a hypothesis on the region: [[§39 Closed and Exact Forms#^prop-39-6|452 Prop. §39.6]].
> - ODE version: the test for exact equations $M + Ny' = 0$, [[§11 Exact Differential Equations and Integrating Factors#^thm-11-2|331 Thm. §11.2]] ($M_y = N_x$ is necessary, and on a rectangle sufficient, for a function $\psi$ with $\psi_x = M$, $\psi_y = N$, that is, a potential of $M\,\mathbf{i} + N\,\mathbf{j}$).

The converse of [[§129 Conservative Vector Fields and Potential Functions#^thm-129-1|Theorem §129.1]] holds only for a special type of region.

> [!definition] Definition §129.1: Simple Curve
> A **simple curve** is a curve that does not intersect itself anywhere between its endpoints: for a simple closed curve, $\mathbf{r}(a) = \mathbf{r}(b)$ but $\mathbf{r}(t_1) \ne \mathbf{r}(t_2)$ when $a < t_1 < t_2 < b$.
>
> *Stewart: 16.3 (text)*

^def-129-1

> [!definition] Definition §129.2: Simply-Connected Region
> A **simply-connected region** in the plane is a connected region $D$ such that every simple closed curve in $D$ encloses only points that are in $D$. Intuitively, a simply-connected region contains no hole and does not consist of two separate pieces.
>
> *Stewart: 16.3 (text)*

^def-129-2

In terms of simply-connected regions, Stewart now states a partial converse to [[§129 Conservative Vector Fields and Potential Functions#^thm-129-1|Theorem §129.1]] (Stewart 16.3, Theorem 6): *if $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ is a vector field on an open simply-connected region $D$, $P$ and $Q$ have continuous first-order partial derivatives, and $\partial P/\partial y = \partial Q/\partial x$ throughout $D$, then $\mathbf{F}$ is conservative.* It is proved with Green's Theorem, so it is stated and proved in the next section: [[§131 Extended Versions of Green's Theorem#^thm-131-3|Theorem §131.3]]. Its three-dimensional version, with $\operatorname{curl}\mathbf{F} = \mathbf{0}$, is [[§136 Stokes' Theorem#^thm-136-4|Theorem §136.4]].

> [!example] Example §129.1: Testing for a Conservative Field
> Determine whether or not the given vector field is conservative.
>
> **(a)** $\mathbf{F}(x, y) = (x - y)\,\mathbf{i} + (x - 2)\,\mathbf{j}$. With $P = x - y$ and $Q = x - 2$,
>
> $$
> \frac{\partial P}{\partial y} = -1, \qquad \frac{\partial Q}{\partial x} = 1 .
> $$
>
> Since $\partial P/\partial y \ne \partial Q/\partial x$, $\mathbf{F}$ is not conservative, by [[§129 Conservative Vector Fields and Potential Functions#^thm-129-1|Theorem §129.1]].
>
> **(b)** $\mathbf{F}(x, y) = (3 + 2xy)\,\mathbf{i} + (x^2 - 3y^2)\,\mathbf{j}$. With $P = 3 + 2xy$ and $Q = x^2 - 3y^2$,
>
> $$
> \frac{\partial P}{\partial y} = 2x = \frac{\partial Q}{\partial x} .
> $$
>
> The domain of $\mathbf{F}$ is the entire plane $D = \mathbb{R}^2$, which is open and simply-connected. So [[§131 Extended Versions of Green's Theorem#^thm-131-3|Theorem §131.3]] applies, and $\mathbf{F}$ is conservative.
>
> (In plots of the two fields, the vectors of (a) along a suitable closed curve point roughly along the curve, so $\oint_C \mathbf{F} \cdot d\mathbf{r} > 0$, consistent with (a). For (b), some vectors near any closed curve point along it and others against it, consistent with all closed-path integrals being $0$.)
>
> *Stewart: Example 16.3.2*

^ex-129-1

The test of [[§131 Extended Versions of Green's Theorem#^thm-131-3|Theorem §131.3]] says that $\mathbf{F}$ is conservative but not how to find $f$. The proof of [[§128 The Fundamental Theorem for Line Integrals#^thm-128-3|Theorem §128.3]] suggests the way: integrate the components one variable at a time.

> [!remark] Remark: Method — Finding a Potential Function
> To find $f$ with $\nabla f = \mathbf{F}$:
> 1. **Test first.** In the plane, check $\partial P/\partial y = \partial Q/\partial x$ (on a simply-connected domain); in space, check $\operatorname{curl}\mathbf{F} = \mathbf{0}$ ([[§132 Curl and Divergence#^cor-132-2|Corollary §132.2]]; on all of $\mathbb{R}^3$ this suffices, [[§136 Stokes' Theorem#^thm-136-4|Theorem §136.4]]). If the test fails, there is no potential.
> 2. **Integrate $f_x = P$ with respect to $x$**: $f = \int P\,dx + g(y)$ in the plane, or $f = \int P\,dx + g(y, z)$ in space. The "constant" of integration is a function of the other variables.
> 3. **Differentiate with respect to $y$** and compare with $Q$. This gives $g'(y)$ (or $g_y(y, z)$), which must not depend on $x$; integrate it.
> 4. **In space, repeat with $z$**: write $g(y, z) = (\text{found part}) + h(z)$, differentiate $f$ with respect to $z$, compare with $R$, and solve for $h'(z)$.
> 5. **Check** that $\nabla f = \mathbf{F}$. Then line integrals of $\mathbf{F}$ are $f(\text{end}) - f(\text{start})$ by [[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|Theorem §128.1]].

^rem-129-1

> [!remark]- Connections
> - ODE version: [[§11 Exact Differential Equations and Integrating Factors#^rem-11-1|331 Remark: Method — Solving an Exact Equation]] (the same construction of $\psi$, whose level curves $\psi(x, y) = c$ are the solutions), worked in [[§11 Exact Differential Equations and Integrating Factors#^ex-11-2|331 Ex. §11.2]].

> [!example] Example §129.2: Finding a Potential and Using It
> Let $\mathbf{F}(x, y) = (3 + 2xy)\,\mathbf{i} + (x^2 - 3y^2)\,\mathbf{j}$. (a) Find a function $f$ such that $\mathbf{F} = \nabla f$. (b) Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $C$ is the curve $\mathbf{r}(t) = e^t\sin t\,\mathbf{i} + e^t\cos t\,\mathbf{j}$, $0 \le t \le \pi$.
>
> **(a)** By [[§129 Conservative Vector Fields and Potential Functions#^ex-129-1|Example §129.1(b)]], $\mathbf{F}$ is conservative, so there is $f$ with
>
> $$
> f_x(x, y) = 3 + 2xy, \qquad (7) \qquad\qquad f_y(x, y) = x^2 - 3y^2 . \qquad (8)
> $$
>
> Integrating (7) with respect to $x$, $f(x, y) = 3x + x^2 y + g(y)$, where the constant of integration $g(y)$ is constant with respect to $x$. Differentiating with respect to $y$, $f_y(x, y) = x^2 + g'(y)$. Comparing with (8), $g'(y) = -3y^2$, so $g(y) = -y^3 + K$. Hence
>
> $$
> f(x, y) = 3x + x^2 y - y^3 + K .
> $$
>
> **(b), using the potential.** Take $K = 0$. The curve starts at $\mathbf{r}(0) = (0, 1)$ and ends at $\mathbf{r}(\pi) = (0, -e^{\pi})$. By [[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|Theorem §128.1]],
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = f(0, -e^{\pi}) - f(0, 1) = \big(-(-e^{\pi})^3\big) - (-1) = e^{3\pi} + 1 .
> $$
>
> **(b), using independence of path.** Replace $C$ by the straight segment $C_1$ from $(0, 1)$ to $(0, -e^{\pi})$: $\mathbf{r}(t) = -t\,\mathbf{j}$, $-1 \le t \le e^{\pi}$. On it $x = 0$, so $\mathbf{F}(\mathbf{r}(t)) = 3\,\mathbf{i} - 3t^2\,\mathbf{j}$ and $\mathbf{r}'(t) = -\mathbf{j}$, giving
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} = \int_{-1}^{e^{\pi}} (3\,\mathbf{i} - 3t^2\,\mathbf{j}) \cdot (-\mathbf{j})\,dt = \int_{-1}^{e^{\pi}} 3t^2\,dt = t^3 \Big]_{-1}^{e^{\pi}} = e^{3\pi} + 1 .
> $$
>
> Either way is much shorter than integrating along $C$ itself.
>
> *Stewart: Examples 16.3.3 and 16.3.4*

^ex-129-2

> [!example] Example §129.3: A Potential in Space
> Consider $\mathbf{F}(x, y, z) = y\,\mathbf{i} + (x + z)\,\mathbf{j} + y\,\mathbf{k}$. (a) Is $\mathbf{F}$ conservative? If so, find a potential function. (b) Compute the line integral of $\mathbf{F}$ along the line segment from $(2, 1, 4)$ to $(8, 3, -1)$.
>
> **(a)** Look for $f$ with
>
> $$
> f_x = y, \qquad f_y = x + z, \qquad f_z = y .
> $$
>
> Integrating the first with respect to $x$: $f(x, y, z) = xy + g(y, z)$. Then $f_y = x + g_y(y, z)$, and comparison with $f_y = x + z$ gives $g_y(y, z) = z$, so $g(y, z) = yz + h(z)$ and $f = xy + yz + h(z)$. Finally $f_z = y + h'(z)$, and comparison with $f_z = y$ gives $h'(z) = 0$, so $h(z) = K$. Hence $\mathbf{F}$ is conservative, with potential
>
> $$
> f(x, y, z) = xy + yz + K = y(x + z) + K .
> $$
>
> (Check: $\nabla f = \langle y, x + z, y \rangle = \mathbf{F}$. Equivalently, $\operatorname{curl}\mathbf{F} = \mathbf{0}$ on all of $\mathbb{R}^3$; see [[§132 Curl and Divergence#^ex-132-2|Example §132.2]].)
>
> **(b)** By [[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|Theorem §128.1]], along the segment (or any path),
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = f(8, 3, -1) - f(2, 1, 4) = 3(8 - 1) - 1(2 + 4) = 21 - 6 = 15 .
> $$
>
> (The posted solution finds $f$ by integrating each component in its own variable and merging the results, $xy + f(y, z)$, $xy + yz + g(x, z)$, $yz + h(x, y)$; the procedure above, from Stewart's Example 16.3.5, organizes the same comparison.)
>
> *Source: 233 Practice Final Set 1, Part II Q4*

^ex-129-3

> [!example] Example §129.4: A Field That Is Not Conservative
> Let $\mathbf{F}(x, y) = e^y\sin x\,\mathbf{i} + e^y\cos x\,\mathbf{j}$. (a) Is $\mathbf{F}$ conservative? (b) Compute the work done by $\mathbf{F}$ along the line segment from $(0, 0)$ to $(\pi, 1)$.
>
> **(a)** With $P = e^y\sin x$ and $Q = e^y\cos x$,
>
> $$
> \frac{\partial P}{\partial y} = e^y\sin x, \qquad \frac{\partial Q}{\partial x} = -e^y\sin x .
> $$
>
> These differ wherever $\sin x \ne 0$, so $\mathbf{F}$ is not conservative ([[§129 Conservative Vector Fields and Potential Functions#^thm-129-1|Theorem §129.1]]). (The posted solution reaches the same conclusion by trying to integrate: $\int P\,dx = -e^y\cos x + f(y)$ and $\int Q\,dy = e^y\cos x + g(x)$ cannot be matched.)
>
> **(b)** So the integral must be computed along the segment: $\mathbf{r}(t) = \langle \pi t, t \rangle$, $0 \le t \le 1$, $\mathbf{r}'(t) = \langle \pi, 1 \rangle$, and
>
> $$
> W = \int_0^1 \big\langle e^t\sin(\pi t),\ e^t\cos(\pi t) \big\rangle \cdot \langle \pi, 1 \rangle\,dt = \pi \int_0^1 e^t\sin(\pi t)\,dt + \int_0^1 e^t\cos(\pi t)\,dt .
> $$
>
> Two integrations by parts (or differentiating the right-hand sides to check) give the antiderivatives
>
> $$
> \int e^t\sin(\pi t)\,dt = \frac{e^t(\sin\pi t - \pi\cos\pi t)}{1 + \pi^2}, \qquad \int e^t\cos(\pi t)\,dt = \frac{e^t(\cos\pi t + \pi\sin\pi t)}{1 + \pi^2} .
> $$
>
> At $t = 1$ and $t = 0$ ($\sin\pi = \sin 0 = 0$, $\cos\pi = -1$, $\cos 0 = 1$):
>
> $$
> \int_0^1 e^t\sin(\pi t)\,dt = \frac{\pi e + \pi}{1 + \pi^2} = \frac{\pi(e + 1)}{1 + \pi^2}, \qquad \int_0^1 e^t\cos(\pi t)\,dt = \frac{-e - 1}{1 + \pi^2} .
> $$
>
> Therefore
>
> $$
> W = \frac{\pi^2(e + 1) - (e + 1)}{1 + \pi^2} = (e + 1)\,\frac{\pi^2 - 1}{\pi^2 + 1} .
> $$
>
> (The same integral, evaluated by integrating by parts twice and solving for it: [[§51 Integration by Parts#^ex-51-5|Example §51.5]].)
>
> *Source: 233 Practice Final Set 2, Part II Q3*

^ex-129-4

*Chain: the same field earlier in [[§51 Integration by Parts#^ex-51-5|Chapter 7]].*

## Conservation of Energy

Let a continuous force field $\mathbf{F}$ move an object of mass $m$ along a path $C$ given by $\mathbf{r}(t)$, $a \le t \le b$, from $A = \mathbf{r}(a)$ to $B = \mathbf{r}(b)$. By Newton's Second Law of Motion ([[§104 Motion in Space꞉ Velocity and Acceleration#^rem-104-2|§104, Remark]]), $\mathbf{F}(\mathbf{r}(t)) = m\,\mathbf{r}''(t)$.

> [!definition] Definition §129.3: Kinetic Energy
> The **kinetic energy** of an object of mass $m$ moving with velocity $\mathbf{v}(t) = \mathbf{r}'(t)$ is $K = \frac12 m|\mathbf{v}(t)|^2$, half the mass times the square of the speed.
>
> *Stewart: 16.3 (text)*

^def-129-3

> [!definition] Definition §129.4: Potential Energy
> If $\mathbf{F} = \nabla f$ is a conservative force field, the **potential energy** of an object at the point $(x, y, z)$ is $P(x, y, z) = -f(x, y, z)$, so that $\mathbf{F} = -\nabla P$.
>
> *Stewart: 16.3 (text)*

^def-129-4

> [!theorem] Theorem §129.2: Work Equals Change in Kinetic Energy
> The work done by the force field $\mathbf{F}$ on the object along $C$ is
>
> $$
> W = \tfrac12 m|\mathbf{v}(b)|^2 - \tfrac12 m|\mathbf{v}(a)|^2, \qquad (15)
> \qquad\text{that is,}\qquad
> W = K(B) - K(A) . \qquad (16)
> $$
>
> *Stewart: 16.3, Equations 15 and 16*

^thm-129-2

> [!proof]+ Proof
> By [[§127 Line Integrals of Vector Fields#^def-127-2|Definition §127.2]] and Newton's Second Law,
>
> $$
> \begin{aligned}
> W = \int_C \mathbf{F} \cdot d\mathbf{r} &= \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_a^b m\,\mathbf{r}''(t) \cdot \mathbf{r}'(t)\,dt \\
> &= \frac{m}{2} \int_a^b \frac{d}{dt}\big[\mathbf{r}'(t) \cdot \mathbf{r}'(t)\big]\,dt = \frac{m}{2} \int_a^b \frac{d}{dt}|\mathbf{r}'(t)|^2\,dt = \frac{m}{2}\Big[|\mathbf{r}'(t)|^2\Big]_a^b = \frac{m}{2}\big(|\mathbf{r}'(b)|^2 - |\mathbf{r}'(a)|^2\big) .
> \end{aligned}
> $$
>
> The fourth step is the product rule for dot products ([[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|Theorem §101.2]], Formula 4), $\frac{d}{dt}(\mathbf{r}' \cdot \mathbf{r}') = 2\,\mathbf{r}' \cdot \mathbf{r}''$, and the sixth is the Fundamental Theorem of Calculus. With $\mathbf{v} = \mathbf{r}'$ this is (15), and (16) is (15) in the notation of [[§129 Conservative Vector Fields and Potential Functions#^def-129-3|Definition §129.3]].

^pf-129-2

*Uses:* [[§127 Line Integrals of Vector Fields#^def-127-2|Def. §127.2]], [[§129 Conservative Vector Fields and Potential Functions#^def-129-3|Def. §129.3]], [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|§101.2]], [[§104 Motion in Space꞉ Velocity and Acceleration#^rem-104-2|§104, Remark]] (Newton's Second Law), [[§41 The Fundamental Theorem of Calculus#^thm-41-2|§41.2]]

> [!theorem] Corollary §129.3: The Law of Conservation of Energy
> If an object moves from a point $A$ to a point $B$ under the influence of a conservative force field, then the sum of its potential energy and its kinetic energy remains constant:
>
> $$
> P(A) + K(A) = P(B) + K(B) .
> $$
>
> This is the reason the vector field is called *conservative*.
>
> *Stewart: 16.3 (text)*

^cor-129-3

> [!proof]+ Proof
> Since $\mathbf{F} = -\nabla P$, [[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|Theorem §128.1]] gives
>
> $$
> W = \int_C \mathbf{F} \cdot d\mathbf{r} = -\int_C \nabla P \cdot d\mathbf{r} = -\big[P(\mathbf{r}(b)) - P(\mathbf{r}(a))\big] = P(A) - P(B) .
> $$
>
> By [[§129 Conservative Vector Fields and Potential Functions#^thm-129-2|Theorem §129.2]], also $W = K(B) - K(A)$. Equating, $P(A) - P(B) = K(B) - K(A)$, which rearranges to $P(A) + K(A) = P(B) + K(B)$.

^pf-129-3

*Uses:* [[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|§128.1]], [[§129 Conservative Vector Fields and Potential Functions#^thm-129-2|§129.2]], [[§129 Conservative Vector Fields and Potential Functions#^def-129-3|Def. §129.3]], [[§129 Conservative Vector Fields and Potential Functions#^def-129-4|Def. §129.4]]
