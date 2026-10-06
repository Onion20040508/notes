---
type: section
subject: "[[Calculus]]"
chapter: 13
section: "88a"
stewart: "13.3"
aliases: ["Stewart 13.3 (cont.)"]
tags: [calculus, math233]
---
← [[§88 Arc Length and Curvature]] · ↑ [[· 13 Vector Functions]] · [[§89 Motion in Space꞉ Velocity and Acceleration]] →

*Stewart, Section 13.3 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q15, Q16), Practice Exam 1 (Q3(b)), Exam 1 Review (Q12, Q14), SI Midterm 1 Problem Set (Q4(b)).*

The unit normal $\mathbf{N}$ and binormal $\mathbf{B}$ complete $\mathbf{T}$ to a moving orthonormal frame, which gives the normal and osculating planes and the osculating circle, and torsion measures how fast the osculating plane turns. Curvature and $\mathbf{N}$ reappear in [[§89 Motion in Space꞉ Velocity and Acceleration|§89]], where they split acceleration into tangential and normal parts.

## The Normal and Binormal Vectors

> [!definition] Definition §88.5: Principal Unit Normal Vector
> Let $\mathbf{r}(t)$ be a smooth space curve. Since $|\mathbf{T}(t)| = 1$, $\mathbf{T}'(t)$ is orthogonal to $\mathbf{T}(t)$ ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-3|Theorem §87.3]]). At any point where $\kappa \ne 0$ (equivalently $\mathbf{T}' \ne \mathbf{0}$), the **principal unit normal vector** (or **unit normal**) is
>
> $$
> \mathbf{N}(t) = \frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|} .
> $$
>
> $\mathbf{N}$ indicates the direction in which the curve is turning.
>
> *Stewart: 13.3 (text)*

^def-88-5

> [!definition] Definition §88.6: Binormal Vector
> At a point of a smooth space curve $\mathbf{r}(t)$ where $\kappa \ne 0$, the **binormal vector** is
>
> $$
> \mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t) .
> $$
>
> $\mathbf{B}$ is perpendicular to both $\mathbf{T}$ and $\mathbf{N}$ and is a unit vector (by [[§83 The Cross Product#^thm-83-4|Theorem §83.4]], $|\mathbf{B}| = |\mathbf{T}||\mathbf{N}|\sin\frac{\pi}{2} = 1$). The three mutually orthogonal unit vectors $\mathbf{T}$, $\mathbf{N}$, $\mathbf{B}$ form the **TNB frame**, which moves along the curve; it is basic in differential geometry and in the motion of spacecraft.
>
> *Stewart: 13.3 (text)*

^def-88-new1

![[m233-88-2.svg]]
*The TNB frame at a point $P$ of the helix $\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle$ ([[§88a The TNB Frame and Torsion#^ex-88-5|Example §88.5]]). $\mathbf{T}$ (red) is tangent to the helix, $\mathbf{N} = \langle -\cos t, -\sin t, 0 \rangle$ (blue) is horizontal and points straight at the $z$-axis, around which the helix turns, and $\mathbf{B} = \mathbf{T} \times \mathbf{N}$ (green) completes the right-handed frame.*

> [!definition] Definition §88.6: Normal Plane
> At a point $P$ of a curve $C$:
> - the **normal plane** is the plane determined by $\mathbf{N}$ and $\mathbf{B}$; it consists of all lines through $P$ orthogonal to the tangent vector $\mathbf{T}$, so $\mathbf{T}$ (or $\mathbf{r}'$) is a normal vector for it;
>
> *Stewart: 13.3 (text)*

^def-88-6

> [!definition] Definition §88.7: Osculating Plane
> At a point $P$ of a curve $C$:
> - the **osculating plane** is the plane determined by $\mathbf{T}$ and $\mathbf{N}$; $\mathbf{B}$ is a normal vector for it. (From the Latin *osculum*, "kiss": it is the plane that comes closest to containing the part of the curve near $P$. For a plane curve it is the plane of the curve.)
>
> *Stewart: 13.3 (text)*

^def-88-new2

> [!definition] Definition §88.8: Osculating Circle
> At a point $P$ of a curve $C$:
> - the **circle of curvature**, or **osculating circle**, is the circle in the osculating plane through $P$ with radius $1/\kappa$ and center a distance $1/\kappa$ from $P$ along $\mathbf{N}$; its center is the **center of curvature**. It is the circle that best describes how $C$ behaves near $P$: it shares the tangent, normal and curvature of $C$ at $P$.
>
> *Stewart: 13.3 (text)*

^def-88-new3

> [!remark] Remark: Summary of Formulas
> $$
> \mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|}, \qquad \mathbf{N}(t) = \frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|}, \qquad \mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t), \qquad
> \kappa = \left| \frac{d\mathbf{T}}{ds} \right| = \frac{|\mathbf{T}'(t)|}{|\mathbf{r}'(t)|} = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3} .
> $$
>
> Stewart's Example 13.3.7 carries out the whole computation for $\mathbf{r}(t) = \langle t, \sqrt2\ln t, 1/t \rangle$ at $(1, 0, 1)$, finding $\mathbf{T}(1) = \frac12\langle 1, \sqrt2, -1 \rangle$, $\mathbf{N}(1) = \frac{1}{\sqrt2}\langle 1, 0, 1 \rangle$, $\mathbf{B}(1) = \frac12\langle 1, -\sqrt2, -1 \rangle$ and $\kappa(1) = \frac{\sqrt2}{4}$.

^rem-88-5

## Torsion

> [!theorem] Proposition §88.6: How T and B Turn
> At a point of a smooth curve where $\kappa \ne 0$,
>
> $$
> \frac{d\mathbf{T}}{ds} = \kappa\,\mathbf{N} ,
> $$
>
> and $\dfrac{d\mathbf{B}}{ds}$ is parallel to $\mathbf{N}$. Consequently there is a scalar $\tau$ with
>
> $$
> \frac{d\mathbf{B}}{ds} = -\tau\,\mathbf{N} . \qquad (12)
> $$
>
> *Stewart: 13.3, Equation 12 (proofs are Exercises 63 and 65)*

^prop-88-6

> [!proof]+ Proof
> By the Chain Rule and [[§88 Arc Length and Curvature#^prop-88-2|Propositions §88.2]] and [[§88 Arc Length and Curvature#^prop-88-3|§88.3]],
>
> $$
> \frac{d\mathbf{T}}{ds} = \frac{\mathbf{T}'(t)}{|\mathbf{r}'(t)|} = \frac{|\mathbf{T}'(t)|}{|\mathbf{r}'(t)|}\cdot\frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|} = \kappa\,\mathbf{N} .
> $$
>
> For $\mathbf{B}$: since $|\mathbf{B}| = 1$, $d\mathbf{B}/ds$ is orthogonal to $\mathbf{B}$ ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-3|Theorem §87.3]]). By the product rule for cross products ([[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|Theorem §87.2]], Formula 5),
>
> $$
> \frac{d\mathbf{B}}{ds} = \frac{d\mathbf{T}}{ds} \times \mathbf{N} + \mathbf{T} \times \frac{d\mathbf{N}}{ds} = \kappa\,(\mathbf{N} \times \mathbf{N}) + \mathbf{T} \times \frac{d\mathbf{N}}{ds} = \mathbf{T} \times \frac{d\mathbf{N}}{ds} ,
> $$
>
> which is orthogonal to $\mathbf{T}$ ([[§83 The Cross Product#^thm-83-2|Theorem §83.2]]). A vector orthogonal to both $\mathbf{T}$ and $\mathbf{B}$ is a multiple of $\mathbf{N}$, because $\mathbf{T}$, $\mathbf{N}$, $\mathbf{B}$ are mutually orthogonal unit vectors: writing the vector as $\alpha\mathbf{T} + \beta\mathbf{N} + \gamma\mathbf{B}$, its dot products with $\mathbf{T}$ and $\mathbf{B}$ are $\alpha$ and $\gamma$. So $d\mathbf{B}/ds = (\text{scalar})\,\mathbf{N}$; the minus sign in (12) is a convention.

^pf-88-6

*Uses:* [[§88a The TNB Frame and Torsion#^def-88-5|Def. §88.5]], [[§88a The TNB Frame and Torsion#^def-88-new1|Def. §88.6]], [[§88 Arc Length and Curvature#^prop-88-2|§88.2]], [[§88 Arc Length and Curvature#^prop-88-3|§88.3]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|§87.2]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-3|§87.3]], [[§83 The Cross Product#^thm-83-2|§83.2]]

> [!definition] Definition §88.7: Torsion
> The **torsion** of a curve is
>
> $$
> \tau = -\frac{d\mathbf{B}}{ds} \cdot \mathbf{N} ,
> $$
>
> obtained by dotting (12) with $\mathbf{N}$, since $\mathbf{N} \cdot \mathbf{N} = 1$.
>
> *Stewart: 13.3, Definition 13*

^def-88-7

> [!remark] Remark: What Torsion Measures
> Curvature $\kappa = |d\mathbf{T}/ds|$ says how tightly the curve bends; $d\mathbf{T}/ds$ describes how the normal plane (whose normal is $\mathbf{T}$) changes. A space curve can also twist out of its osculating plane, and since $\mathbf{B}$ is normal to the osculating plane, $d\mathbf{B}/ds$ describes how that plane turns. Torsion is the rate of this twisting: if $\tau > 0$ at $P$, the curve twists out of the osculating plane in the direction of $\mathbf{B}$; if $\tau < 0$, in the opposite direction. A plane curve has $\tau = 0$ (its $\mathbf{B}$ is constant). Under suitable conditions the curvature and torsion at every point determine the shape of a space curve completely.

^rem-88-6

> [!theorem] Proposition §88.7: Torsion in Terms of t
> $$
> \tau(t) = -\frac{\mathbf{B}'(t) \cdot \mathbf{N}(t)}{|\mathbf{r}'(t)|} .
> $$
>
> *Stewart: 13.3, Equation 14*

^prop-88-7

> [!proof]+ Proof
> By the Chain Rule, $\dfrac{d\mathbf{B}}{dt} = \dfrac{d\mathbf{B}}{ds}\dfrac{ds}{dt}$, so $\dfrac{d\mathbf{B}}{ds} = \dfrac{\mathbf{B}'(t)}{ds/dt} = \dfrac{\mathbf{B}'(t)}{|\mathbf{r}'(t)|}$ ([[§88 Arc Length and Curvature#^prop-88-2|Proposition §88.2]]). Substitute into [[§88a The TNB Frame and Torsion#^def-88-7|Definition §88.7]].

^pf-88-7

*Uses:* [[§88a The TNB Frame and Torsion#^def-88-7|Def. §88.7]], [[§88 Arc Length and Curvature#^prop-88-2|§88.2]]

> [!theorem] Theorem §88.8: Torsion from r′, r″, r‴
> At a point where $\mathbf{r}' \times \mathbf{r}'' \ne \mathbf{0}$, the torsion of the curve given by $\mathbf{r}$ is
>
> $$
> \tau(t) = \frac{[\mathbf{r}'(t) \times \mathbf{r}''(t)] \cdot \mathbf{r}'''(t)}{|\mathbf{r}'(t) \times \mathbf{r}''(t)|^2} .
> $$
>
> *Stewart: 13.3, Theorem 15*

^thm-88-8

> [!proof]- Proof
> Stewart outlines this in Exercise 72. Write $v = ds/dt = |\mathbf{r}'|$ and use a prime for $d/dt$. By [[§88 Arc Length and Curvature#^thm-88-4|Theorem §88.4]], $\mathbf{r}' \times \mathbf{r}'' \ne \mathbf{0}$ means $\kappa \ne 0$, so $\mathbf{N}$ and $\mathbf{B}$ are defined.
>
> **Step 1: $\mathbf{r}'$ and $\mathbf{r}''$ in the frame.** $\mathbf{r}' = v\mathbf{T}$, and by [[§88a The TNB Frame and Torsion#^prop-88-6|Proposition §88.6]], $\mathbf{T}' = \dfrac{d\mathbf{T}}{ds}\,v = \kappa v\,\mathbf{N}$. So
>
> $$
> \mathbf{r}'' = v'\,\mathbf{T} + v\,\mathbf{T}' = v'\,\mathbf{T} + \kappa v^2\,\mathbf{N}, \qquad \mathbf{r}' \times \mathbf{r}'' = v\mathbf{T} \times (v'\mathbf{T} + \kappa v^2\mathbf{N}) = \kappa v^3\,\mathbf{B} ,
> $$
>
> using $\mathbf{T} \times \mathbf{T} = \mathbf{0}$ and $\mathbf{T} \times \mathbf{N} = \mathbf{B}$. Hence $|\mathbf{r}' \times \mathbf{r}''| = \kappa v^3$.
>
> **Step 2: $d\mathbf{N}/ds$.** Since $\mathbf{T}$, $\mathbf{N}$, $\mathbf{B}$ is a right-handed orthonormal frame ($\mathbf{B} = \mathbf{T} \times \mathbf{N}$), we have $\mathbf{N} = \mathbf{B} \times \mathbf{T}$, $\mathbf{N} \times \mathbf{T} = -\mathbf{B}$ and $\mathbf{B} \times \mathbf{N} = -\mathbf{T}$ (the same pattern as $\mathbf{i}, \mathbf{j}, \mathbf{k}$). By Formula 5 of [[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|Theorem §87.2]] and [[§88a The TNB Frame and Torsion#^prop-88-6|Proposition §88.6]],
>
> $$
> \frac{d\mathbf{N}}{ds} = \frac{d\mathbf{B}}{ds} \times \mathbf{T} + \mathbf{B} \times \frac{d\mathbf{T}}{ds} = -\tau\,\mathbf{N} \times \mathbf{T} + \kappa\,\mathbf{B} \times \mathbf{N} = -\kappa\,\mathbf{T} + \tau\,\mathbf{B} .
> $$
>
> So $\mathbf{N}' = v\,\dfrac{d\mathbf{N}}{ds} = -\kappa v\,\mathbf{T} + \tau v\,\mathbf{B}$.
>
> **Step 3: the $\mathbf{B}$-component of $\mathbf{r}'''$.** Differentiating $\mathbf{r}'' = v'\mathbf{T} + \kappa v^2\mathbf{N}$,
>
> $$
> \mathbf{r}''' = v''\,\mathbf{T} + v'\,\mathbf{T}' + (\kappa v^2)'\,\mathbf{N} + \kappa v^2\,\mathbf{N}' .
> $$
>
> The first three terms are multiples of $\mathbf{T}$ and $\mathbf{N}$, and the $\mathbf{B}$-component of the last is $\kappa v^2 \cdot \tau v = \kappa\tau v^3$. Since $\mathbf{B}$ is orthogonal to $\mathbf{T}$ and $\mathbf{N}$, $\mathbf{B} \cdot \mathbf{r}''' = \kappa\tau v^3$.
>
> **Step 4.** By Steps 1 and 3,
>
> $$
> \frac{(\mathbf{r}' \times \mathbf{r}'') \cdot \mathbf{r}'''}{|\mathbf{r}' \times \mathbf{r}''|^2} = \frac{\kappa v^3\,(\mathbf{B} \cdot \mathbf{r}''')}{\kappa^2 v^6} = \frac{\kappa v^3 \cdot \kappa\tau v^3}{\kappa^2 v^6} = \tau .
> $$

^pf-88-8

*Uses:* [[§88a The TNB Frame and Torsion#^prop-88-6|§88.6]], [[§88 Arc Length and Curvature#^thm-88-4|§88.4]], [[§88a The TNB Frame and Torsion#^def-88-5|Def. §88.5]], [[§88a The TNB Frame and Torsion#^def-88-new1|Def. §88.6]], [[§87 Derivatives and Integrals of Vector Functions#^thm-87-2|§87.2]], [[§83 The Cross Product#^prop-83-7|§83.7]]

> [!example] Example §88.5: The Helix: Frame, Planes, Curvature and Torsion
> For the circular helix $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\,\mathbf{k}$:
>
> **(a) T, N, B.** We have $\mathbf{r}'(t) = -\sin t\,\mathbf{i} + \cos t\,\mathbf{j} + \mathbf{k}$ and $|\mathbf{r}'(t)| = \sqrt2$, so
>
> $$
> \mathbf{T}(t) = \frac{1}{\sqrt2}(-\sin t\,\mathbf{i} + \cos t\,\mathbf{j} + \mathbf{k}), \qquad \mathbf{T}'(t) = \frac{1}{\sqrt2}(-\cos t\,\mathbf{i} - \sin t\,\mathbf{j}), \qquad |\mathbf{T}'(t)| = \frac{1}{\sqrt2} ,
> $$
>
> $$
> \mathbf{N}(t) = \frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|} = -\cos t\,\mathbf{i} - \sin t\,\mathbf{j} = \langle -\cos t, -\sin t, 0 \rangle .
> $$
>
> The unit normal at every point is horizontal and points toward the $z$-axis. The binormal is
>
> $$
> \mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t) = \frac{1}{\sqrt2}\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -\sin t & \cos t & 1 \\ -\cos t & -\sin t & 0 \end{vmatrix} = \frac{1}{\sqrt2}\langle \sin t, -\cos t, 1 \rangle .
> $$
>
> **(b) Curvature.** $\kappa = |\mathbf{T}'(t)|/|\mathbf{r}'(t)| = \frac{1/\sqrt2}{\sqrt2} = \frac12$, constant.
>
> **(c) Normal and osculating planes at $P(0, 1, \pi/2)$.** $P$ corresponds to $t = \pi/2$. The normal plane has normal vector $\mathbf{r}'(\pi/2) = \langle -1, 0, 1 \rangle$, so it is
>
> $$
> -1(x - 0) + 0(y - 1) + 1\Big(z - \frac{\pi}{2}\Big) = 0, \qquad\text{or}\qquad z = x + \frac{\pi}{2} .
> $$
>
> The osculating plane contains $\mathbf{T}$ and $\mathbf{N}$, so $\mathbf{B}(\pi/2) = \big\langle \frac{1}{\sqrt2}, 0, \frac{1}{\sqrt2} \big\rangle$ is normal to it, and so is the parallel vector $\langle 1, 0, 1 \rangle$:
>
> $$
> 1(x - 0) + 0(y - 1) + 1\Big(z - \frac{\pi}{2}\Big) = 0, \qquad\text{or}\qquad z = -x + \frac{\pi}{2} .
> $$
>
> **(d) Torsion.** $\mathbf{B}'(t) = \frac{1}{\sqrt2}\langle \cos t, \sin t, 0 \rangle$ and $ds/dt = \sqrt2$, so by [[§88a The TNB Frame and Torsion#^prop-88-7|Proposition §88.7]]
>
> $$
> \tau(t) = -\frac{\mathbf{B}'(t) \cdot \mathbf{N}(t)}{|\mathbf{r}'(t)|} = -\frac{1}{2}\langle \cos t, \sin t, 0 \rangle \cdot \langle -\cos t, -\sin t, 0 \rangle = \frac12 .
> $$
>
> Check with [[§88a The TNB Frame and Torsion#^thm-88-8|Theorem §88.8]]: $\mathbf{r}'' = \langle -\cos t, -\sin t, 0 \rangle$, $\mathbf{r}''' = \langle \sin t, -\cos t, 0 \rangle$, $\mathbf{r}' \times \mathbf{r}'' = \langle \sin t, -\cos t, 1 \rangle$, so $\tau = \dfrac{\sin^2 t + \cos^2 t}{2} = \dfrac12$. The unit circle $\langle \cos t, \sin t, 0 \rangle$ has $\kappa = 1$ and $\tau = 0$: it bends but never twists, while the helix both bends and twists upward at every point.
>
> *Stewart: Examples 13.3.6, 13.3.8 and 13.3.10*

^ex-88-5
