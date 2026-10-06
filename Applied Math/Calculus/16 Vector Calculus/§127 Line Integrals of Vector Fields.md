---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 127
stewart: "16.2"
aliases: ["Stewart 16.2 (cont.)"]
tags: [calculus, math233]
---
← [[§126 Line Integrals]] · ↑ [[· 16 Vector Calculus]] · [[§128 The Fundamental Theorem for Line Integrals]] →

*Stewart, Section 16.2 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q6(b)), Practice Final Exam (Q3).*

The line integral of a vector field, $\int_C \mathbf{F} \cdot d\mathbf{r}$, adds up the component of $\mathbf{F}$ along the direction of travel; it is the work done by a force field. Unlike the line integral with respect to arc length, it changes sign when the direction is reversed.

## Line Integrals of Vector Fields; Work

> [!remark] Remark: Where the Work Integral Comes From
> A constant force $\mathbf{F}$ moving an object along the displacement $\mathbf{D}$ does work $\mathbf{F} \cdot \mathbf{D}$ ([[§95 The Dot Product#^prop-95-7|Proposition §95.7]]). Now let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ be a continuous force field on $\mathbb{R}^3$ and $C$ a smooth curve, divided into subarcs $P_{i-1}P_i$ of lengths $\Delta s_i$ as before. If $\Delta s_i$ is small, the particle moving from $P_{i-1}$ to $P_i$ proceeds approximately in the direction of $\mathbf{T}(t_i^*)$, the [[§101 Derivatives and Integrals of Vector Functions#^def-101-4|unit tangent vector]] at $P_i^*$, so the work done along that subarc is approximately
>
> $$
> \mathbf{F}(x_i^*, y_i^*, z_i^*) \cdot \big[\Delta s_i\,\mathbf{T}(t_i^*)\big] = \big[\mathbf{F}(x_i^*, y_i^*, z_i^*) \cdot \mathbf{T}(t_i^*)\big]\,\Delta s_i ,
> $$
>
> and the total work is approximately the Riemann sum $\sum_{i=1}^{n} \big[\mathbf{F}(x_i^*, y_i^*, z_i^*) \cdot \mathbf{T}(x_i^*, y_i^*, z_i^*)\big]\,\Delta s_i$. $\qquad (11)$

^rem-127-1
> [!definition] Definition §127.1: Work
> The **work** $W$ done by the force field $\mathbf{F}$ in moving a particle along $C$ is the limit of the Riemann sums (11):
>
> $$
> W = \int_C \mathbf{F}(x, y, z) \cdot \mathbf{T}(x, y, z)\,ds = \int_C \mathbf{F} \cdot \mathbf{T}\,ds . \qquad (12)
> $$
>
> In words: *work is the line integral with respect to arc length of the tangential component of the force.*
>
> *Stewart: 16.2, Equation 12*

^def-127-1

If $C$ is given by $\mathbf{r}(t)$, then $\mathbf{T}(t) = \mathbf{r}'(t)/|\mathbf{r}'(t)|$, and Formula 9 turns (12) into

$$
W = \int_a^b \left[ \mathbf{F}(\mathbf{r}(t)) \cdot \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} \right] |\mathbf{r}'(t)|\,dt = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt .
$$

This integral is abbreviated $\int_C \mathbf{F} \cdot d\mathbf{r}$, and it makes sense for any continuous vector field.

> [!definition] Definition §127.2: Line Integral of a Vector Field
> Let $\mathbf{F}$ be a continuous vector field defined on a smooth curve $C$ given by a vector function $\mathbf{r}(t)$, $a \le t \le b$. The **line integral of $\mathbf{F}$ along $C$** is
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_C \mathbf{F} \cdot \mathbf{T}\,ds .
> $$
>
> Here $\mathbf{F}(\mathbf{r}(t))$ abbreviates $\mathbf{F}(x(t), y(t), z(t))$, and formally $d\mathbf{r} = \mathbf{r}'(t)\,dt$.
>
> *Stewart: 16.2, Definition 13*

^def-127-2

> [!remark]- Connections
> - The work integral in 452: [[§27 Line Integrals and Green's Theorem#^def-27-2|452 Def. §27.2]]. In the language of forms it is the integral of the 1-form $P\,dx + Q\,dy + R\,dz$, computed by pulling it back along $\mathbf{r}$: [[§37 The Algebra of Differential Forms#^ex-37-2|452 Ex. §37.2]], [[§38 The Exterior Derivative#^def-38-2|452 Def. §38.2]].

> [!theorem] Theorem §127.1: Reversing the Orientation of a Vector Line Integral
> $$
> \int_{-C} \mathbf{F} \cdot d\mathbf{r} = -\int_C \mathbf{F} \cdot d\mathbf{r} .
> $$
>
> *Stewart: 16.2 (text)*

^thm-127-1

> [!proof]+ Proof
> $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F} \cdot \mathbf{T}\,ds$, and integrals with respect to arc length do not change when the orientation is reversed ([[§126 Line Integrals#^thm-126-4|Theorem §126.4]]). But the integrand does: replacing $C$ by $-C$ replaces the unit tangent vector $\mathbf{T}$ by $-\mathbf{T}$. Hence $\int_{-C} \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F} \cdot (-\mathbf{T})\,ds = -\int_C \mathbf{F} \cdot d\mathbf{r}$.

^pf-127-1

*Uses:* [[§127 Line Integrals of Vector Fields#^def-127-2|Def. §127.2]], [[§126 Line Integrals#^thm-126-4|§126.4]]

> [!theorem] Theorem §127.2: Vector Line Integrals in Component Form
> If $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$ is a vector field on $\mathbb{R}^3$, then
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C P\,dx + Q\,dy + R\,dz .
> $$
>
> Similarly, for a vector field $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j}$ on $\mathbb{R}^2$,
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_C P\,dx + Q\,dy . \qquad (14)
> $$
>
> *Stewart: 16.2 (text) and Equation 14*

^thm-127-2

> [!proof]+ Proof
> By [[§127 Line Integrals of Vector Fields#^def-127-2|Definition §127.2]],
>
> $$
> \begin{aligned}
> \int_C \mathbf{F} \cdot d\mathbf{r} &= \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_a^b (P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}) \cdot \big(x'(t)\,\mathbf{i} + y'(t)\,\mathbf{j} + z'(t)\,\mathbf{k}\big)\,dt \\
> &= \int_a^b \Big[ P(x(t), y(t), z(t))\,x'(t) + Q(x(t), y(t), z(t))\,y'(t) + R(x(t), y(t), z(t))\,z'(t) \Big]\,dt .
> \end{aligned}
> $$
>
> By [[§126 Line Integrals#^thm-126-5|Theorem §126.5]] this last integral is precisely the line integral (10). The plane case is the same computation without the $z$ terms, using Formulas 7.

^pf-127-2

*Uses:* [[§127 Line Integrals of Vector Fields#^def-127-2|Def. §127.2]], [[§126 Line Integrals#^thm-126-5|§126.5]], [[§126 Line Integrals#^thm-126-2|§126.2]]

For example, the integral of [[§126 Line Integrals#^ex-126-4|Example §126.4]] is $\int_C \mathbf{F} \cdot d\mathbf{r}$ for $\mathbf{F}(x, y, z) = y\,\mathbf{i} + z\,\mathbf{j} + x\,\mathbf{k}$.

> [!remark] Remark: Method — Evaluating a Line Integral
> 1. **Parametrize the curve** by $\mathbf{r}(t)$, $a \le t \le b$, in the direction of travel. Use (8) for segments, $x = x$, $y = g(x)$ (or $y$ as the parameter) for graphs, and $(\cos t, \sin t)$-type parametrizations for circles; for the curve of intersection of two surfaces, parametrize the simpler one (for a cylinder $x^2 + y^2 = a^2$, take $x = a\cos t$, $y = a\sin t$) and solve the other for the remaining coordinate. Split a piecewise-smooth curve into smooth pieces.
> 2. **Compute $\mathbf{r}'(t)$**, and $ds = |\mathbf{r}'(t)|\,dt$ for an integral with respect to arc length.
> 3. **Substitute** $x = x(t)$, $y = y(t)$, $z = z(t)$ into $f$ or $\mathbf{F}$, and $dx = x'(t)\,dt$ etc.:
>    $\int_C f\,ds = \int_a^b f(\mathbf{r}(t))\,|\mathbf{r}'(t)|\,dt$, $\quad\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt$.
> 4. **Integrate in $t$** and add the pieces. If the parametrization runs against the given orientation, change the sign of $dx$, $dy$, $dz$ and $d\mathbf{r}$ integrals (not of $ds$ integrals).
> 5. **Look for shortcuts first**: a conservative field ([[§128 The Fundamental Theorem for Line Integrals#^thm-128-1|Theorem §128.1]]), or a closed curve in the plane or in space bounding a simple region or surface (Green's Theorem, [[§130 Green's Theorem#^thm-130-1|Theorem §130.1]]; Stokes' Theorem, [[§136 Stokes' Theorem#^thm-136-1|Theorem §136.1]]).

^rem-127-2
> [!example] Example §127.1: Work along a Segment
> Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$, where $\mathbf{F}(x, y) = xy^2\,\mathbf{i} - x\,\mathbf{j}$ and $C$ is given by $\mathbf{r}(t) = (1 + t)\,\mathbf{i} + (2 - t)\,\mathbf{j}$, $0 \le t \le 2$.
>
> Here $\mathbf{r}'(t) = \mathbf{i} - \mathbf{j}$ and $\mathbf{F}(\mathbf{r}(t)) = (1 + t)(2 - t)^2\,\mathbf{i} - (1 + t)\,\mathbf{j}$, so
>
> $$
> \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) = (1 + t)(2 - t)^2 + (1 + t) = (1 + t)(t^2 - 4t + 5) = t^3 - 3t^2 + t + 5 .
> $$
>
> Therefore
>
> $$
> \int_C \mathbf{F} \cdot d\mathbf{r} = \int_0^2 (t^3 - 3t^2 + t + 5)\,dt = \left[ \frac{t^4}{4} - t^3 + \frac{t^2}{2} + 5t \right]_0^2 = 4 - 8 + 2 + 10 = 8 .
> $$
>
> (Is there a shortcut? $\partial P/\partial y = 2xy$ and $\partial Q/\partial x = -1$ are not equal, so $\mathbf{F}$ is not conservative ([[§129 Conservative Vector Fields and Potential Functions#^thm-129-1|Theorem §129.1]]) and the integral must be computed along the curve.)
>
> *Source: 233 Practice Final Exam, Q3*

^ex-127-1
