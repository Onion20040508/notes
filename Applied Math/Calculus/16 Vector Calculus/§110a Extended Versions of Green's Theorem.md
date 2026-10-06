---
type: section
subject: "[[Calculus]]"
chapter: 16
section: "110a"
stewart: "16.4"
aliases: ["Stewart 16.4 (cont.)"]
tags: [calculus, math233]
---
← [[§110 Green's Theorem]] · ↑ [[· 16 Vector Calculus]] · [[§111 Curl and Divergence]] →

*Stewart, Section 16.4 · MATH 233 (UMass, Spring 2023): Practice Final Exam (Q2), Chapter 16 Review (Q6(a)).*

Cutting regions into pieces extends Green's Theorem ([[§110 Green's Theorem#^thm-110-1|Theorem §110.1]]) to regions with holes. That gives the standard calculation for fields with a singularity, such as $(-y\,\mathbf{i} + x\,\mathbf{j})/(x^2 + y^2)$, and the proof of the test for conservative fields announced in [[§109 The Fundamental Theorem for Line Integrals|§109]] (the converse of [[§109a Conservative Vector Fields and Potential Functions#^thm-109-4|Theorem §109.4]]).

## Extended Versions of Green's Theorem

> [!theorem] Theorem §110.3: Green's Theorem for Finite Unions of Simple Regions
> Green's Theorem holds when $D$ is a finite union of non-overlapping simple regions and $C = \partial D$ is its positively oriented boundary.
>
> *Stewart: 16.4 (text)*

^thm-110-3

> [!proof]+ Proof
> First let $D = D_1 \cup D_2$, where $D_1$ and $D_2$ are simple and meet along a curve $C_3$. Let the rest of the boundary of $D_1$ be $C_1$ and the rest of the boundary of $D_2$ be $C_2$, so that $\partial D = C_1 \cup C_2$. The positively oriented boundary of $D_1$ is $C_1 \cup C_3$, and that of $D_2$ is $C_2 \cup (-C_3)$: the common curve is traversed in opposite directions, because the two regions lie on opposite sides of it. Green's Theorem for simple regions ([[§110 Green's Theorem#^thm-110-1|Theorem §110.1]]) gives
>
> $$
> \int_{C_1 \cup C_3} P\,dx + Q\,dy = \iint_{D_1} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA, \qquad
> \int_{C_2 \cup (-C_3)} P\,dx + Q\,dy = \iint_{D_2} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA .
> $$
>
> Add the two equations. Since $\int_{-C_3} = -\int_{C_3}$, the line integrals along $C_3$ and $-C_3$ cancel, and the double integrals add up to the double integral over $D$:
>
> $$
> \int_{C_1 \cup C_2} P\,dx + Q\,dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA .
> $$
>
> This is Green's Theorem for $D$, since its boundary is $C = C_1 \cup C_2$. For a union of more simple regions, the same argument applies: every internal edge is shared by two of the pieces, it is traversed once in each direction, and its contributions cancel.

^pf-110-3

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§108 Line Integrals#^thm-108-4|§108.4]] (reversing orientation), [[§99 Double Integrals Over General Regions#^thm-99-4|§99.4]] (additivity over regions)

> [!example] Example §110.4: Sectors of Annuli
> **(a) A semiannulus.** Evaluate $\displaystyle\oint_C y^2\,dx + 3xy\,dy$, where $C$ is the boundary of the semiannular region $D$ in the upper half-plane between the circles $x^2 + y^2 = 1$ and $x^2 + y^2 = 4$.
>
> $D$ is not simple, but the $y$-axis divides it into two simple regions, so [[§110a Extended Versions of Green's Theorem#^thm-110-3|Theorem §110.3]] applies. In polar coordinates $D = \{(r, \theta) \mid 1 \le r \le 2,\ 0 \le \theta \le \pi\}$, and
>
> $$
> \frac{\partial}{\partial x}(3xy) - \frac{\partial}{\partial y}(y^2) = 3y - 2y = y .
> $$
>
> Therefore
>
> $$
> \begin{aligned}
> \oint_C y^2\,dx + 3xy\,dy &= \iint_D y\,dA = \int_0^{\pi} \int_1^2 (r\sin\theta)\,r\,dr\,d\theta = \int_0^{\pi} \sin\theta\,d\theta \int_1^2 r^2\,dr \\
> &= \Big[-\cos\theta\Big]_0^{\pi} \Big[\tfrac13 r^3\Big]_1^2 = 2 \cdot \frac73 = \frac{14}{3} .
> \end{aligned}
> $$
>
> **(b) A sector of an annulus.** Use Green's Theorem to evaluate
>
> $$
> \oint_C \big(\sqrt{2 + x^3} - 8y^3\big)\,dx + \big(8x^3 + \sqrt{1 + y^3}\big)\,dy ,
> $$
>
> where $C$ is the boundary of $D = \{(x, y) \mid 1 \le x^2 + y^2 \le 4,\ -y \le x \le y,\ y \ge 0\}$, traversed in the positive sense.
>
> **The region.** $-y \le x \le y$ with $y \ge 0$ says $|x| \le y$: the wedge between the lines $y = x$ and $y = -x$ above the origin. So in polar coordinates $D = \{(r, \theta) \mid 1 \le r \le 2,\ \pi/4 \le \theta \le 3\pi/4\}$, a sector of an annulus. Like the semiannulus of part (a), it is a union of simple regions.
>
> **The integrand.** With $P = \sqrt{2 + x^3} - 8y^3$ and $Q = 8x^3 + \sqrt{1 + y^3}$, the square roots drop out:
>
> $$
> \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 24x^2 - (-24y^2) = 24(x^2 + y^2) = 24r^2 .
> $$
>
> **The integral.**
>
> $$
> \oint_C \cdots = \int_{\pi/4}^{3\pi/4} \int_1^2 24r^2 \cdot r\,dr\,d\theta = 24 \cdot \frac{\pi}{2} \cdot \Big[\tfrac14 r^4\Big]_1^2 = 12\pi \cdot \frac{16 - 1}{4} = 45\pi .
> $$
>
> *A caveat on the problem as set: $\sqrt{2 + x^3}$ is undefined where $x < -\sqrt[3]{2} \approx -1.26$, and $D$ reaches $x = -\sqrt2 \approx -1.41$ at its corner $(-\sqrt2, \sqrt2)$. So $P$ is not defined on all of $D$, and strictly the hypotheses of Green's Theorem fail. The intended point is step 3 of the method: a term of $P$ that depends on $x$ alone contributes nothing. The posted answer $45\pi$ is the value of the intended problem.*
>
> *Stewart: Example 16.4.4*
> *Source: 233 Practice Final Exam, Q2*

^ex-110-4

> [!theorem] Theorem §110.4: Green's Theorem for Regions with Holes
> Let $D$ be a region whose boundary $C$ consists of two piecewise-smooth simple closed curves, an outer curve $C_1$ and an inner curve $C_2$, oriented so that $D$ is always on the left as $C$ is traversed: counterclockwise on $C_1$, clockwise on $C_2$. If $P$ and $Q$ have continuous partial derivatives on an open region containing $D$, then
>
> $$
> \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \int_{C_1} P\,dx + Q\,dy + \int_{C_2} P\,dx + Q\,dy = \int_C P\,dx + Q\,dy .
> $$
>
> The same holds with several holes. Such regions are not simply connected ([[§109a Conservative Vector Fields and Potential Functions#^def-109-5|Definition §109.5]]).
>
> *Stewart: 16.4 (text)*

^thm-110-4

> [!proof]+ Proof
> Cut $D$ along two segments joining $C_1$ to $C_2$ (one on each side of the hole). This divides $D$ into two regions $D'$ and $D''$, as in the figure below, each a union of simple regions. Apply [[§110a Extended Versions of Green's Theorem#^thm-110-3|Theorem §110.3]] to each and add:
>
> $$
> \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
> = \iint_{D'} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA + \iint_{D''} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
> = \int_{\partial D'} P\,dx + Q\,dy + \int_{\partial D''} P\,dx + Q\,dy .
> $$
>
> The boundaries $\partial D'$ and $\partial D''$ both run along each cut, in opposite directions, so the line integrals along the cuts cancel. What is left is $\partial D'$ and $\partial D''$ along $C_1$, which together make up $C_1$ counterclockwise, and along $C_2$, which together make up $C_2$ clockwise. So the sum is
>
> $$
> \int_{C_1} P\,dx + Q\,dy + \int_{C_2} P\,dx + Q\,dy = \int_C P\,dx + Q\,dy .
> $$
>
> With several holes, make more cuts; the bookkeeping is the same.

^pf-110-4

*Uses:* [[§110a Extended Versions of Green's Theorem#^thm-110-3|§110.3]], [[§108 Line Integrals#^thm-108-4|§108.4]] (reversing orientation), [[§99 Double Integrals Over General Regions#^thm-99-4|§99.4]] (additivity over regions)

![[m233-110-2.svg]]
*The cutting argument for a region with a hole. Each half $D'$ and $D''$ gets its own counterclockwise boundary. Along the two cuts (green) the upper half travels one way and the lower half the other, so those contributions cancel. What remains is the outer curve $C_1$ counterclockwise and the inner curve $C_2$ clockwise, both with $D$ on the left.*

> [!remark]- Connections
> - Complex-variables version: [[§53 Multiply Connected Domains#^thm-53-1|342 Thm. §53.1]] (the Cauchy–Goursat theorem for a region with holes, with the same orientation of the boundary).

> [!example] Example §110.5: A Field with a Singularity at the Origin
> If $\mathbf{F}(x, y) = \dfrac{-y\,\mathbf{i} + x\,\mathbf{j}}{x^2 + y^2}$, show that $\displaystyle\int_C \mathbf{F} \cdot d\mathbf{r} = 2\pi$ for every positively oriented simple closed path $C$ that encloses the origin.
>
> Green's Theorem cannot be applied to $C$ directly, because $\mathbf{F}$ is undefined at the origin, which lies inside $C$. And $C$ is arbitrary, so we cannot parametrize it. Instead, choose $a > 0$ small enough that the counterclockwise circle $C'$ with center the origin and radius $a$ lies inside $C$. Let $D$ be the region between $C$ and $C'$. It does not contain the origin, and its positively oriented boundary is $C \cup (-C')$. With $P = \dfrac{-y}{x^2 + y^2}$ and $Q = \dfrac{x}{x^2 + y^2}$,
>
> $$
> \frac{\partial Q}{\partial x} = \frac{(x^2 + y^2) - x \cdot 2x}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}, \qquad
> \frac{\partial P}{\partial y} = \frac{-(x^2 + y^2) + y \cdot 2y}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2} .
> $$
>
> These are continuous away from the origin, hence on an open region containing $D$. By [[§110a Extended Versions of Green's Theorem#^thm-110-4|Theorem §110.4]],
>
> $$
> \int_C P\,dx + Q\,dy + \int_{-C'} P\,dx + Q\,dy = \iint_D \left[ \frac{y^2 - x^2}{(x^2 + y^2)^2} - \frac{y^2 - x^2}{(x^2 + y^2)^2} \right] dA = 0 ,
> $$
>
> so $\displaystyle\int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C'} \mathbf{F} \cdot d\mathbf{r}$. The circle is easy: with $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j}$, $0 \le t \le 2\pi$,
>
> $$
> \int_{C'} \mathbf{F} \cdot d\mathbf{r} = \int_0^{2\pi} \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_0^{2\pi} \frac{(-a\sin t)(-a\sin t) + (a\cos t)(a\cos t)}{a^2\cos^2 t + a^2\sin^2 t}\,dt = \int_0^{2\pi} dt = 2\pi .
> $$
>
> So $\int_C \mathbf{F} \cdot d\mathbf{r} = 2\pi$ for every such $C$, even though $\partial Q/\partial x = \partial P/\partial y$ everywhere on the domain of $\mathbf{F}$. In particular $\mathbf{F}$ is not conservative on $\mathbb{R}^2 \setminus \{(0, 0)\}$: its integral around a closed path is not $0$.
>
> *Stewart: Example 16.4.5*

^ex-110-5

> [!remark]- Connections
> - This field is the angle form $d\theta$ of 452, the standard closed but not exact form: [[Angle form on the punctured plane]], [[§22 The Algebra of Differential Forms#^prop-22-11|452 Prop. §22.11]]. The value $\frac{1}{2\pi}\oint_C \mathbf{F} \cdot d\mathbf{r}$ is the [[§93 Argument Principle#^def-93-2|winding number]] of $C$ about the origin.

## Curl-Free Fields on Simply-Connected Regions

Green's Theorem supplies the proof, promised in [[§109 The Fundamental Theorem for Line Integrals|§109]] after [[§109a Conservative Vector Fields and Potential Functions#^thm-109-4|Theorem §109.4]], of the test for conservative vector fields in the plane.

> [!theorem] Theorem §110.5: Test for Conservative Fields
> Let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ be a vector field on an open simply-connected region $D$. Suppose that $P$ and $Q$ have continuous first-order partial derivatives and
>
> $$
> \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} \quad \text{throughout } D .
> $$
>
> Then $\mathbf{F}$ is conservative.
>
> *Stewart: 16.3, Theorem 6 (proof sketched in 16.4)*

^thm-110-5

> [!proof]+ Proof
> *Stewart gives this as a sketch.* Let $C$ be any simple closed path in $D$, and $R$ the region that $C$ encloses. Since $D$ is simply connected, $C$ encloses only points of $D$, so $R \subseteq D$ and $P$, $Q$ have continuous partial derivatives on the open set $D \supseteq R$. If $C$ is positively oriented, Green's Theorem gives
>
> $$
> \oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C P\,dx + Q\,dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \iint_R 0\,dA = 0 .
> $$
>
> If $C$ is negatively oriented, the integral is $-0 = 0$. A closed curve that is not simple crosses itself at one or more points and can be broken up into a number of simple closed curves. The line integral of $\mathbf{F}$ around each of these is $0$, so the sum is $0$. Hence $\int_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every closed curve $C$ in $D$. By [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|Theorem §109.2]], $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of path in $D$. Since $D$ is open and connected, $\mathbf{F}$ is conservative by [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|Theorem §109.3]].
>
> (What makes this a sketch is the step "broken up into simple closed curves": it is clear for curves that cross themselves finitely often, but needs more care in general.)

^pf-110-5

*Uses:* [[§110 Green's Theorem#^thm-110-1|§110.1]], [[§108a Line Integrals of Vector Fields#^thm-108-6|§108.6]], [[§109a Conservative Vector Fields and Potential Functions#^def-109-5|Def. §109.5]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|§109.2]], [[§109 The Fundamental Theorem for Line Integrals#^thm-109-3|§109.3]]

> [!remark]- Connections
> - Rigorous treatment in the language of forms: on a star-shaped domain every closed form is exact, [[§22 The Algebra of Differential Forms#^prop-22-12|452 Prop. §22.12]] ([[Poincaré Lemma]]). [[§110a Extended Versions of Green's Theorem#^ex-110-5|Example §110.5]] shows that some hypothesis on the region is needed.
> - Topology's definition of simply connected (path-connected, every loop shrinks to a point): [[§23 The Fundamental Group#^def-23-3|590 Def. §23.3]]. Stewart's definition (every simple closed curve in $D$ encloses only points of $D$) agrees with it for open connected regions in the plane (a nontrivial fact of plane topology).
> - ODE version: [[§9 Exact Differential Equations and Integrating Factors#^thm-9-2|331 Thm. §9.2]] (the test for exact equations, $M_y = N_x$, proved on a rectangle by constructing $\psi$ directly).
> - See also: [[§115★ Harmonic Conjugates#^thm-115-4|342 Thm. §115.4]] (applied to the field $(-u_y, u_x)$, the test gives a harmonic conjugate of a harmonic function on a simply connected domain).
