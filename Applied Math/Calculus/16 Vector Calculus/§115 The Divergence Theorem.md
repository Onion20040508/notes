---
type: section
subject: "[[Calculus]]"
chapter: 16
section: 115
stewart: "16.9"
aliases: ["Stewart 16.9"]
tags: [calculus, math233]
---
← [[§114 Stokes' Theorem]] · ↑ [[· 16 Vector Calculus]] · [[§116 Numbers, Inequalities, and Absolute Values]] →

*Stewart, Section 16.9 · MATH 233 (UMass, Spring 2023): Chapter 16 Review (Q8), Practice Final Exam (Q7), Practice Final Set 1 (Part I, Q6), Practice Final Set 2 (Part II, Q4).*

The normal form of Green's Theorem ([[§111 Curl and Divergence#^thm-111-5|Theorem §111.5]]) says that the outward flux of a plane field across the boundary of a region equals the double integral of its divergence over the region. The Divergence Theorem is the same statement one dimension up: the flux of $\mathbf{F}$ outward across the closed surface $S$ bounding a solid $E$ equals $\iiint_E \operatorname{div}\mathbf{F}\,dV$. Like Green's and Stokes' Theorems, it integrates a derivative over a region on one side and the original function over the boundary on the other. In practice it turns a flux through a closed surface made of several pieces into one triple integral, usually of a much simpler integrand. Applied to a region between two surfaces, it gives Gauss's Law for a point charge; applied to tiny balls, it explains the divergence as outward flux per unit volume.

## The Divergence Theorem

Stewart states and proves the theorem for regions $E$ over which triple integrals were evaluated in Stewart 15.6: type 1 regions ([[§103 Triple Integrals#^def-103-3|Definition §103.3]]) and type 2 and type 3 regions ([[§103 Triple Integrals#^def-103-4|Definition §103.4]]).

> [!definition] Definition §115.1: Simple Solid Region
> A **simple solid region** is a solid region $E$ that is simultaneously of types 1, 2 and 3: it can be written as $\{(x, y, z) \mid (x, y) \in D_1,\ u_1(x, y) \le z \le u_2(x, y)\}$ (type 1), as $\{(x, y, z) \mid (y, z) \in D_2,\ v_1(y, z) \le x \le v_2(y, z)\}$ (type 2) and as $\{(x, y, z) \mid (x, z) \in D_3,\ w_1(x, z) \le y \le w_2(x, z)\}$ (type 3). (For instance, regions bounded by ellipsoids or rectangular boxes are simple solid regions.) Its boundary is a closed surface, given the positive (outward) orientation of [[§113a Oriented Surfaces and Flux#^def-113-new2|Definition §113.7]].
>
> *Stewart: 16.9 (text)*

^def-115-1

> [!theorem] Theorem §115.1: The Divergence Theorem
> Let $E$ be a simple solid region and let $S$ be the boundary surface of $E$, given with positive (outward) orientation. Let $\mathbf{F}$ be a vector field whose component functions have continuous partial derivatives on an open region that contains $E$. Then
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_E \operatorname{div}\mathbf{F}\,dV .
> $$
>
> So the flux of $\mathbf{F}$ across the boundary surface of $E$ equals the triple integral of the divergence of $\mathbf{F}$ over $E$. (It is also called Gauss's Theorem, or, in Eastern Europe, Ostrogradsky's Theorem.)
>
> *Stewart: 16.9, The Divergence Theorem*

^thm-115-1

> [!proof]+ Proof
> Let $\mathbf{F} = P\,\mathbf{i} + Q\,\mathbf{j} + R\,\mathbf{k}$. Then $\operatorname{div}\mathbf{F} = \partial P/\partial x + \partial Q/\partial y + \partial R/\partial z$, so
>
> $$
> \iiint_E \operatorname{div}\mathbf{F}\,dV = \iiint_E \frac{\partial P}{\partial x}\,dV + \iiint_E \frac{\partial Q}{\partial y}\,dV + \iiint_E \frac{\partial R}{\partial z}\,dV .
> $$
>
> If $\mathbf{n}$ is the unit outward normal of $S$, the surface integral on the left side of the theorem is
>
> $$
> \iint_S \mathbf{F} \cdot \mathbf{n}\,dS = \iint_S P\,\mathbf{i} \cdot \mathbf{n}\,dS + \iint_S Q\,\mathbf{j} \cdot \mathbf{n}\,dS + \iint_S R\,\mathbf{k} \cdot \mathbf{n}\,dS .
> $$
>
> So it suffices to prove the three equations
>
> $$
> \iint_S P\,\mathbf{i} \cdot \mathbf{n}\,dS = \iiint_E \frac{\partial P}{\partial x}\,dV, \qquad (2)
> \qquad
> \iint_S Q\,\mathbf{j} \cdot \mathbf{n}\,dS = \iiint_E \frac{\partial Q}{\partial y}\,dV, \qquad (3)
> \qquad
> \iint_S R\,\mathbf{k} \cdot \mathbf{n}\,dS = \iiint_E \frac{\partial R}{\partial z}\,dV . \qquad (4)
> $$
>
> **Equation 4.** Since $E$ is a type 1 region, $E = \{(x, y, z) \mid (x, y) \in D,\ u_1(x, y) \le z \le u_2(x, y)\}$, where $D$ is the projection of $E$ onto the $xy$-plane. Computing the triple integral as an iterated integral ([[§103 Triple Integrals#^thm-103-2|Theorem §103.2]]) and the inner integral by the Fundamental Theorem of Calculus,
>
> $$
> \iiint_E \frac{\partial R}{\partial z}\,dV = \iint_D \left[ \int_{u_1(x, y)}^{u_2(x, y)} \frac{\partial R}{\partial z}(x, y, z)\,dz \right] dA = \iint_D \big[ R(x, y, u_2(x, y)) - R(x, y, u_1(x, y)) \big]\,dA . \qquad (5)
> $$
>
> The boundary $S$ consists of three pieces: the bottom surface $S_1$ ($z = u_1(x, y)$), the top surface $S_2$ ($z = u_2(x, y)$), and possibly a vertical surface $S_3$ above the boundary curve of $D$ (it may be absent, as for a sphere). On $S_3$, $\mathbf{k} \cdot \mathbf{n} = 0$, because $\mathbf{k}$ is vertical and $\mathbf{n}$ is horizontal, so $\iint_{S_3} R\,\mathbf{k} \cdot \mathbf{n}\,dS = 0$. Thus, whether or not there is a vertical surface,
>
> $$
> \iint_S R\,\mathbf{k} \cdot \mathbf{n}\,dS = \iint_{S_1} R\,\mathbf{k} \cdot \mathbf{n}\,dS + \iint_{S_2} R\,\mathbf{k} \cdot \mathbf{n}\,dS . \qquad (6)
> $$
>
> On $S_2$ the outward normal points upward, so Formula 10 of [[§113a Oriented Surfaces and Flux#^thm-113-4|Theorem §113.4]], applied to the field $R\,\mathbf{k}$ (with $P$ and $Q$ replaced by $0$), gives $\iint_{S_2} R\,\mathbf{k} \cdot \mathbf{n}\,dS = \iint_D R(x, y, u_2(x, y))\,dA$. On $S_1$ the outward normal points downward, so we multiply by $-1$: $\iint_{S_1} R\,\mathbf{k} \cdot \mathbf{n}\,dS = -\iint_D R(x, y, u_1(x, y))\,dA$. By (6),
>
> $$
> \iint_S R\,\mathbf{k} \cdot \mathbf{n}\,dS = \iint_D \big[ R(x, y, u_2(x, y)) - R(x, y, u_1(x, y)) \big]\,dA ,
> $$
>
> which equals the triple integral by (5). This proves Equation 4.
>
> **Equations 2 and 3** are proved in the same way, using the expressions for $E$ as a type 2 and a type 3 region, respectively. (Stewart says only "in a similar manner"; for (2): write $E = \{(x, y, z) \mid (y, z) \in D',\ v_1(y, z) \le x \le v_2(y, z)\}$. The Fundamental Theorem of Calculus in $x$ gives $\iiint_E P_x\,dV = \iint_{D'} [P(v_2, y, z) - P(v_1, y, z)]\,dA$. On the front surface $x = v_2(y, z)$, parametrized by $y$ and $z$, $\mathbf{r}_y \times \mathbf{r}_z = \langle 1, -\partial v_2/\partial y, -\partial v_2/\partial z \rangle$ points outward, and $P\,\mathbf{i} \cdot (\mathbf{r}_y \times \mathbf{r}_z) = P$; on the back surface the outward normal is the opposite one; on the remaining surface, parallel to the $x$-axis, $\mathbf{i} \cdot \mathbf{n} = 0$. The surface integral therefore gives the same expression.)
>
> Adding (2), (3) and (4) gives the Divergence Theorem.

^pf-115-1

*Uses:* [[§115 The Divergence Theorem#^def-115-1|Def. §115.1]], [[§113a Oriented Surfaces and Flux#^thm-113-4|§113.4]], [[§113a Oriented Surfaces and Flux#^thm-113-3|§113.3]], [[§113a Oriented Surfaces and Flux#^def-113-6|Def. §113.6]], [[§113a Oriented Surfaces and Flux#^def-113-new2|Def. §113.7]], [[§111 Curl and Divergence#^def-111-3|Def. §111.3]], [[§103 Triple Integrals#^thm-103-2|§103.2]], [[§103 Triple Integrals#^thm-103-3|§103.3]] (triple integrals over type 1, 2, 3 regions), [[§36 The Fundamental Theorem of Calculus#^thm-36-2|§36.2]] (FTC Part 2)

> [!remark]- Connections
> - Rigorous treatment: [[§18 Surface Integrals#^thm-18-2|452 Thm. §18.2]], with the same proof (one component at a time, FTC along vertical segments, the bottom surface with reversed normal); hub [[Divergence Theorem in ℝ³]]. The version in $\mathbb{R}^n$ is [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-1|452 Thm. §17.1]], and the plane version is [[§16 Line Integrals and Green's Theorem#^thm-16-2|452 Thm. §16.2]] ([[§111 Curl and Divergence#^thm-111-5|Theorem §111.5]] here).
> - PDE version: applied to the heat flux out of every subregion, it turns the integral heat balance into the local balance $-\nabla\cdot\mathbf{q} + g = \rho c\,u_t$, [[§42 Three-Dimensional Heat Equation#^thm-42-2|341 Thm. §42.2]], and so gives the three-dimensional heat equation, [[§42 Three-Dimensional Heat Equation#^thm-42-3|341 Thm. §42.3]].

> [!remark] Remark: Two Fluxes in One Line
> - **The unit sphere.** For $\mathbf{F}(x, y, z) = z\,\mathbf{i} + y\,\mathbf{j} + x\,\mathbf{k}$, $\operatorname{div}\mathbf{F} = \frac{\partial z}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial x}{\partial z} = 1$. The unit sphere $S$ bounds the unit ball $B$, so the flux of $\mathbf{F}$ across $S$ is $\iiint_B 1\,dV = V(B) = \frac43\pi(1)^3 = \frac{4\pi}{3}$ (Stewart, Example 16.9.1). Compare the direct computation over the sphere in [[§113a Oriented Surfaces and Flux#^ex-113-3|Example §113.3(b)]].
> - **A constant field.** If $\mathbf{v}$ is a constant vector and $S$ is the surface of the cube with vertices $(\pm1, \pm1, \pm1)$, then $\operatorname{div}(2\mathbf{v}) = 0$, so the flux of $2\mathbf{v}$ across $S$ is $0$ with either orientation (the inward orientation only changes the sign of $0$). The posted solution gets $0$ directly: opposite faces have equal areas and opposite normals, so their contributions cancel in pairs.
>
> *Source: 233 Practice Final Set 1, Part I Q6*

^rem-115-1

> [!remark] Remark: Method — Using the Divergence Theorem
> 1. **Check that $S$ is closed** (the whole boundary of a solid $E$) and oriented outward. If $S$ is not closed, either compute the flux directly or close it up with simple pieces (disks), apply the theorem, and subtract the flux through the added pieces. If $S$ is oriented inward, change the sign.
> 2. **Check that $\mathbf{F}$ is smooth on all of $E$.** If $\mathbf{F}$ is undefined at a point inside (as for $\mathbf{x}/|\mathbf{x}|^3$ at the origin), cut out a small ball around it and use [[§115 The Divergence Theorem#^thm-115-2|Theorem §115.2]].
> 3. **Compute $\operatorname{div}\mathbf{F}$.** Terms of $P$ not involving $x$, of $Q$ not involving $y$, and of $R$ not involving $z$ drop out.
> 4. **Evaluate $\iiint_E \operatorname{div}\mathbf{F}\,dV$** in coordinates suited to $E$: cylindrical for cylinders and paraboloids ([[§104 Triple Integrals in Cylindrical Coordinates#^thm-104-1|Theorem §104.1]]), spherical for balls and cones ([[§105 Triple Integrals in Spherical Coordinates#^thm-105-2|Theorem §105.2]]). Use symmetry: an odd function of $y$ over a region symmetric in $y$ integrates to $0$.

^rem-115-2

> [!example] Example §115.1: A Region with Four Faces
> Evaluate $\iint_S \mathbf{F} \cdot d\mathbf{S}$, where $\mathbf{F}(x, y, z) = xy\,\mathbf{i} + \big(y^2 + e^{xz^2}\big)\,\mathbf{j} + \sin(xy)\,\mathbf{k}$ and $S$ is the surface of the region $E$ bounded by the parabolic cylinder $z = 1 - x^2$ and the planes $z = 0$, $y = 0$ and $y + z = 2$.
>
> Directly, this would need four surface integrals, one for each piece of $S$. But the divergence of $\mathbf{F}$ is much simpler than $\mathbf{F}$:
>
> $$
> \operatorname{div}\mathbf{F} = \frac{\partial}{\partial x}(xy) + \frac{\partial}{\partial y}\big(y^2 + e^{xz^2}\big) + \frac{\partial}{\partial z}\big(\sin xy\big) = y + 2y + 0 = 3y .
> $$
>
> The easiest way to evaluate the triple integral is to describe $E$ as a type 3 region: $E = \{(x, y, z) \mid -1 \le x \le 1,\ 0 \le z \le 1 - x^2,\ 0 \le y \le 2 - z\}$. Then
>
> $$
> \begin{aligned}
> \iint_S \mathbf{F} \cdot d\mathbf{S} &= \iiint_E 3y\,dV = 3\int_{-1}^{1} \int_0^{1 - x^2} \int_0^{2 - z} y\,dy\,dz\,dx = 3\int_{-1}^{1} \int_0^{1 - x^2} \frac{(2 - z)^2}{2}\,dz\,dx \\
> &= \frac32 \int_{-1}^{1} \left[ -\frac{(2 - z)^3}{3} \right]_0^{1 - x^2} dx = -\frac12 \int_{-1}^{1} \big[(x^2 + 1)^3 - 8\big]\,dx \\
> &= -\int_0^1 (x^6 + 3x^4 + 3x^2 - 7)\,dx = -\left( \frac17 + \frac35 + 1 - 7 \right) = \frac{184}{35} .
> \end{aligned}
> $$
>
> (At $z = 1 - x^2$, $2 - z = 1 + x^2$; and $(x^2 + 1)^3 - 8 = x^6 + 3x^4 + 3x^2 - 7$ is even, which gives the factor $2$ in the last line.)
>
> *Stewart: Example 16.9.2*

^ex-115-1

> [!example] Example §115.2: A Cylinder Cut by a Slanted Plane
> Evaluate $\iint_S \mathbf{F} \cdot d\mathbf{S}$, where $\mathbf{F}(x, y, z) = \langle xy + 2xz,\ x^2 + y^2,\ xy - z^2 \rangle$ and $S$ is the surface of the solid bounded by the cylinder $x^2 + y^2 = 4$ and the planes $z = y - 2$ and $z = 0$ (outward).
>
> $$
> \operatorname{div}\mathbf{F} = (y + 2z) + 2y + (-2z) = 3y .
> $$
>
> Inside the cylinder $y \le 2$, so $y - 2 \le 0$: the solid is $E = \{(x, y, z) \mid x^2 + y^2 \le 4,\ y - 2 \le z \le 0\}$, of height $0 - (y - 2) = 2 - y$ over the disk $D$: $x^2 + y^2 \le 4$. So
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_E 3y\,dV = \iint_D 3y(2 - y)\,dA = \iint_D 6y\,dA - 3\iint_D y^2\,dA .
> $$
>
> The first integral is $0$ ($y$ is odd and $D$ is symmetric about the $x$-axis). In polar coordinates, $\iint_D y^2\,dA = \int_0^{2\pi} \sin^2\theta\,d\theta \int_0^2 r^3\,dr = \pi \cdot 4 = 4\pi$. Hence
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = 0 - 3(4\pi) = -12\pi .
> $$
>
> *The posted solution integrates $z$ from $0$ up to $y - 2$, the reverse of the solid's limits ($y - 2 \le z \le 0$), and gets $12\pi$; with the limits in order the flux is $-12\pi$.*
>
> *Source: 233 Chapter 16 Review, Q8*

^ex-115-2

> [!example] Example §115.3: A Hemisphere with Its Base
> Let $\mathbf{F}(x, y, z) = \dfrac{1}{12\pi}\langle x^3, y^3, z^3 \rangle$, and let $S$ consist of the upper hemisphere ($z \ge 0$) of $x^2 + y^2 + z^2 = 100$ together with the disk of radius $10$ in the $xy$-plane centered at the origin, oriented with the outward normal. Calculate $\iint_S \mathbf{F} \cdot \mathbf{n}\,dS$.
>
> $S$ is the closed boundary of the solid half-ball $E$: $0 \le \rho \le 10$, $0 \le \phi \le \pi/2$, $0 \le \theta \le 2\pi$. Here
>
> $$
> \operatorname{div}\mathbf{F} = \frac{1}{12\pi}\,(3x^2 + 3y^2 + 3z^2) = \frac{\rho^2}{4\pi} .
> $$
>
> In spherical coordinates ($dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$),
>
> $$
> \iint_S \mathbf{F} \cdot \mathbf{n}\,dS = \frac{1}{4\pi} \int_0^{2\pi} \int_0^{\pi/2} \int_0^{10} \rho^4\sin\phi\,d\rho\,d\phi\,d\theta = \frac{1}{4\pi} \cdot 2\pi \cdot \Big[-\cos\phi\Big]_0^{\pi/2} \cdot \frac{10^5}{5} = \frac12 \cdot 1 \cdot 20000 = 10000 .
> $$
>
> *Source: 233 Practice Final Exam, Q7*

^ex-115-3

> [!example] Example §115.4: A Flux That Vanishes by Symmetry
> Determine the flux of $\mathbf{F} = ye^{z^2}\,\mathbf{i} + y^2\,\mathbf{j} + e^{xy}\,\mathbf{k}$ across the cylinder $S$ defined by $x^2 + y^2 = 9$, $0 \le z \le 4$, with positive orientation.
>
> Take $S$ to be the closed surface of the solid cylinder $E$ (side, top and bottom), as the posted solution does. Then
>
> $$
> \operatorname{div}\mathbf{F} = \frac{\partial}{\partial x}\big(ye^{z^2}\big) + \frac{\partial}{\partial y}(y^2) + \frac{\partial}{\partial z}\big(e^{xy}\big) = 0 + 2y + 0 = 2y ,
> $$
>
> and in cylindrical coordinates
>
> $$
> \iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_E 2y\,dV = 2\int_0^{2\pi} \int_0^3 \int_0^4 (r\sin\theta)\,r\,dz\,dr\,d\theta = 2\left( \int_0^{2\pi} \sin\theta\,d\theta \right)\left( \int_0^3 r^2\,dr \right)\left( \int_0^4 dz \right) = 0 ,
> $$
>
> since the $\theta$-integral is $0$.
>
> *If "the cylinder" is read as the lateral surface only, the answer is still $0$: the top disk ($z = 4$, $\mathbf{n} = \mathbf{k}$) contributes $\iint_{x^2 + y^2 \le 9} e^{xy}\,dA$ and the bottom disk ($z = 0$, $\mathbf{n} = -\mathbf{k}$) contributes the negative of the same integral, because the $\mathbf{k}$-component $e^{xy}$ does not depend on $z$. So the lateral flux is $0 - 0 = 0$.*
>
> *Source: 233 Practice Final Set 2, Part II Q4*

^ex-115-4

## Regions Between Two Surfaces

The Divergence Theorem was proved only for simple solid regions, but it can be proved for regions that are finite unions of simple solid regions, by the cutting procedure used for Green's Theorem ([[§110a Extended Versions of Green's Theorem#^thm-110-3|Theorem §110.3]]). *Stewart states this extension without proof.*

> [!theorem] Theorem §115.2: Regions Between Two Closed Surfaces
> Let $E$ be the region that lies between closed surfaces $S_1$ and $S_2$, where $S_1$ lies inside $S_2$, and let $\mathbf{n}_1$ and $\mathbf{n}_2$ be the outward normals of $S_1$ and $S_2$. If $\mathbf{F}$ satisfies the hypotheses of the Divergence Theorem on $E$, then
>
> $$
> \iiint_E \operatorname{div}\mathbf{F}\,dV = -\iint_{S_1} \mathbf{F} \cdot d\mathbf{S} + \iint_{S_2} \mathbf{F} \cdot d\mathbf{S} , \qquad (7)
> $$
>
> where both surface integrals are taken with the outward orientations $\mathbf{n}_1$, $\mathbf{n}_2$.
>
> *Stewart: 16.9, Equation 7*

^thm-115-2

> [!proof]+ Proof
> The boundary surface of $E$ is $S = S_1 \cup S_2$, and its normal pointing out of $E$ is $\mathbf{n} = -\mathbf{n}_1$ on $S_1$ (out of $E$ means into the inner surface) and $\mathbf{n} = \mathbf{n}_2$ on $S_2$. Applying the Divergence Theorem to $E$ (a finite union of simple solid regions),
>
> $$
> \iiint_E \operatorname{div}\mathbf{F}\,dV = \iint_S \mathbf{F} \cdot \mathbf{n}\,dS = \iint_{S_1} \mathbf{F} \cdot (-\mathbf{n}_1)\,dS + \iint_{S_2} \mathbf{F} \cdot \mathbf{n}_2\,dS = -\iint_{S_1} \mathbf{F} \cdot d\mathbf{S} + \iint_{S_2} \mathbf{F} \cdot d\mathbf{S} .
> $$

^pf-115-2

*Uses:* [[§115 The Divergence Theorem#^thm-115-1|§115.1]] (extended to finite unions of simple solid regions), [[§113a Oriented Surfaces and Flux#^def-113-7|Def. §113.7]], [[§113 Surface Integrals#^def-113-3|Def. §113.3]]

![[m233-115-1.svg]]
*[[§115 The Divergence Theorem#^thm-115-2|Theorem §115.2]]: the region $E$ between an inner closed surface $S_1$ and an outer one $S_2$ (cross-section). Out of $E$ means along $\mathbf{n}_2$ on the outer surface but along $-\mathbf{n}_1$, toward the inside, on the inner one; hence the minus sign in front of the flux through $S_1$. In [[§115 The Divergence Theorem#^ex-115-5|Example §115.5]], $S_1$ is a small sphere around a point charge and $S_2$ is an arbitrary surface enclosing it.*

> [!example] Example §115.5: Gauss's Law for a Point Charge
> Let $\mathbf{E}(\mathbf{x}) = \dfrac{\varepsilon Q}{|\mathbf{x}|^3}\,\mathbf{x}$ be the electric field of a charge $Q$ at the origin ([[§107 Vector Fields#^ex-107-2|Example §107.2]]). Show that the electric flux of $\mathbf{E}$ through any closed surface $S$ that encloses the origin is
>
> $$
> \iint_S \mathbf{E} \cdot d\mathbf{S} = 4\pi\varepsilon Q .
> $$
>
> The difficulty is that we have no explicit equation for $S$, and $\mathbf{E}$ is undefined at the origin, inside $S$. Let $S_1$ be a sphere centered at the origin with radius $a$ small enough that $S_1$ lies inside $S$, and let $E$ be the region between $S_1$ and $S$. By [[§115 The Divergence Theorem#^thm-115-2|Theorem §115.2]],
>
> $$
> \iiint_E \operatorname{div}\mathbf{E}\,dV = -\iint_{S_1} \mathbf{E} \cdot d\mathbf{S} + \iint_S \mathbf{E} \cdot d\mathbf{S} . \qquad (8)
> $$
>
> **$\operatorname{div}\mathbf{E} = 0$** away from the origin (Stewart leaves this as Exercise 16.9.25): with $\rho = |\mathbf{x}| = \sqrt{x^2 + y^2 + z^2}$ and $\partial\rho/\partial x = x/\rho$,
>
> $$
> \frac{\partial}{\partial x}\left( \frac{x}{\rho^3} \right) = \frac{\rho^3 - x \cdot 3\rho^2 (x/\rho)}{\rho^6} = \frac{\rho^2 - 3x^2}{\rho^5} ,
> $$
>
> and adding the analogous $y$ and $z$ terms gives $\varepsilon Q\,\dfrac{3\rho^2 - 3(x^2 + y^2 + z^2)}{\rho^5} = 0$. So (8) gives $\iint_S \mathbf{E} \cdot d\mathbf{S} = \iint_{S_1} \mathbf{E} \cdot d\mathbf{S}$.
>
> **On the sphere** $|\mathbf{x}| = a$ the outward normal is $\mathbf{n} = \mathbf{x}/|\mathbf{x}|$, so
>
> $$
> \mathbf{E} \cdot \mathbf{n} = \frac{\varepsilon Q}{|\mathbf{x}|^3}\,\mathbf{x} \cdot \frac{\mathbf{x}}{|\mathbf{x}|} = \frac{\varepsilon Q}{|\mathbf{x}|^4}\,\mathbf{x} \cdot \mathbf{x} = \frac{\varepsilon Q}{|\mathbf{x}|^2} = \frac{\varepsilon Q}{a^2} ,
> $$
>
> a constant. Therefore
>
> $$
> \iint_S \mathbf{E} \cdot d\mathbf{S} = \iint_{S_1} \mathbf{E} \cdot \mathbf{n}\,dS = \frac{\varepsilon Q}{a^2} \iint_{S_1} dS = \frac{\varepsilon Q}{a^2}\,A(S_1) = \frac{\varepsilon Q}{a^2}\,4\pi a^2 = 4\pi\varepsilon Q .
> $$
>
> This is a special case of Gauss's Law ([[§113a Oriented Surfaces and Flux#^def-113-8|Definition §113.8]], Equation 11) for a single charge, with $\varepsilon = 1/(4\pi\varepsilon_0)$. Compare [[§110a Extended Versions of Green's Theorem#^ex-110-5|Example §110.5]], the same argument in the plane.
>
> *Stewart: Example 16.9.3*

^ex-115-5

## The Meaning of Divergence

> [!theorem] Theorem §115.3: Divergence as Flux per Unit Volume
> Let $\mathbf{F}$ have components with continuous partial derivatives, let $P_0(x_0, y_0, z_0)$ be a point, and let $B_a$ be the ball with center $P_0$ and radius $a$, with boundary sphere $S_a$ oriented outward. Then
>
> $$
> \operatorname{div}\mathbf{F}(P_0) = \lim_{a \to 0} \frac{1}{V(B_a)} \iint_{S_a} \mathbf{F} \cdot d\mathbf{S} . \qquad (9)
> $$
>
> *Stewart: 16.9, Equation 9*

^thm-115-3

> [!proof]+ Proof
> *Stewart gives this as a sketch ("$\operatorname{div}\mathbf{F}(P) \approx \operatorname{div}\mathbf{F}(P_0)$ for all $P$ in $B_a$ … this approximation becomes better as $a \to 0$ and suggests that …"). Here is the estimate behind it.* By the Divergence Theorem,
>
> $$
> \iint_{S_a} \mathbf{F} \cdot d\mathbf{S} - \operatorname{div}\mathbf{F}(P_0)\,V(B_a) = \iiint_{B_a} \big[ \operatorname{div}\mathbf{F}(P) - \operatorname{div}\mathbf{F}(P_0) \big]\,dV ,
> $$
>
> whose absolute value is at most $V(B_a)\,M(a)$, where $M(a)$ is the largest value of $|\operatorname{div}\mathbf{F}(P) - \operatorname{div}\mathbf{F}(P_0)|$ for $P$ in $B_a$. Dividing by $V(B_a)$,
>
> $$
> \left| \frac{1}{V(B_a)} \iint_{S_a} \mathbf{F} \cdot d\mathbf{S} - \operatorname{div}\mathbf{F}(P_0) \right| \le M(a) \longrightarrow 0 \quad (a \to 0) ,
> $$
>
> because $\operatorname{div}\mathbf{F}$ is continuous at $P_0$ and every point of $B_a$ is within distance $a$ of $P_0$.

^pf-115-3

*Uses:* [[§115 The Divergence Theorem#^thm-115-1|§115.1]], [[§111 Curl and Divergence#^def-111-3|Def. §111.3]]

> [!remark]- Connections
> - The same characterization, "divergence is flux density", with the picture of a shrinking test ball: [[§11 The Three Differential Operators꞉ Gradient, Curl, Divergence|452 §11]]. Its physical form is the continuity equation (conservation of mass), [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-4|452 Thm. §17.4]].

> [!definition] Definition §115.2: Source and Sink
> Equation 9 says that $\operatorname{div}\mathbf{F}(P_0)$ is the net rate of outward flux per unit volume at $P_0$; this is the reason for the name *divergence*. (If $\mathbf{v}$ is the velocity field of a fluid with constant density $\rho$, then $\mathbf{F} = \rho\mathbf{v}$ is the rate of flow per unit area.) If $\operatorname{div}\mathbf{F}(P) > 0$, the net flow is outward near $P$, and $P$ is called a **source**. If $\operatorname{div}\mathbf{F}(P) < 0$, the net flow is inward near $P$, and $P$ is called a **sink**.
>
> For example, $\mathbf{F} = x^2\,\mathbf{i} + y^2\,\mathbf{j}$ has $\operatorname{div}\mathbf{F} = 2x + 2y$, which is positive when $y > -x$: the points above the line $y = -x$ are sources and those below it are sinks. (In a plot, near a source the arrows ending near the point are shorter than those starting there; near a sink, longer.)
>
> *Stewart: 16.9 (text)*

^def-115-2
