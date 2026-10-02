---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 118
bc: "118"
aliases: ["B&C 118"]
tags: [complex-variables, math342, extension]
---
← [[§117★ Transformations of Boundary Conditions]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§119★ Steady Temperatures in a Half Plane]] →

*Brown–Churchill, Section 118 (with Exercises 1, 4 and 13 of Section 121).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Chapter 10 uses conformal mapping to solve physical problems governed by Laplace's equation in two variables: heat conduction, electrostatics and fluid flow. This section sets up the first. Fourier's law says that heat flows down the temperature gradient; a balance of heat for a small element then shows that a steady temperature without sources is harmonic. Its level curves are the isotherms, and the level curves of a harmonic conjugate are the lines along which the heat flows. An insulated edge is a line of flow, which is why the Neumann condition $dT/dN = 0$ of [[§117★ Transformations of Boundary Conditions|§117]] is so common.

## Fourier's Law and Laplace's Equation

> [!definition] Definition §118.1: Flux; Fourier's Law
> In the theory of heat conduction, the **flux** across a surface within a solid body, at a point of that surface, is the quantity of heat flowing in a specified direction normal to the surface per unit time per unit area at the point (measured, for instance, in calories per second per square centimeter). It is denoted $\Phi$, and it varies with the normal derivative of the temperature $T$ at the point:
>
> $$
> \Phi = -K\,\frac{dT}{dN} \qquad (K > 0). \qquad (1)
> $$
>
> Relation (1) is **Fourier's law**, and the constant $K$ is the **thermal conductivity** of the material, which is assumed to be homogeneous.
>
> *B&C: Sec. 118 (text)*

^def-118-1

We restrict attention to temperatures $T$ that vary only with $x$ and $y$, so the flow of heat is two-dimensional and parallel to the $xy$ plane, and to the **steady state**, in which $T$ does not vary with time. It is assumed that no heat is created or destroyed within the solid (no sources or sinks), and that $T(x, y)$ and its partial derivatives of the first and second order are continuous at each interior point. These, with (1), are the postulates of the mathematical theory of heat conduction.

> [!theorem] Proposition §118.1: Steady Temperatures Are Harmonic
> Under these postulates the temperature satisfies Laplace's equation
>
> $$
> T_{xx}(x, y) + T_{yy}(x, y) = 0 \qquad (4)
> $$
>
> at each interior point; so $T$ is a harmonic function of $x$ and $y$ in the domain representing the interior of the solid.
>
> *B&C: Sec. 118 (text)*

^prop-118-1

> [!proof]+ Proof
> *B&C gives this as a sketch.* Consider an element of volume interior to the solid, a rectangular prism of unit height perpendicular to the $xy$ plane with base $\Delta x$ by $\Delta y$ at $(x, y)$ (B&C's Fig. 154). By (1), the rate of flow of heat to the right across the left-hand face is $-KT_x(x, y)\Delta y$, and across the right-hand face it is $-KT_x(x + \Delta x, y)\Delta y$. The difference, the net rate of heat loss through these two faces, is
>
> $$
> -K\Big[\frac{T_x(x + \Delta x, y) - T_x(x, y)}{\Delta x}\Big]\Delta x\,\Delta y, \qquad\text{or}\qquad -KT_{xx}(x, y)\,\Delta x\,\Delta y \qquad (2)
> $$
>
> approximately, if $\Delta x$ is very small. Likewise the net loss through the other two faces is approximately
>
> $$
> -KT_{yy}(x, y)\,\Delta x\,\Delta y . \qquad (3)
> $$
>
> Heat enters or leaves the element only through these four faces, and the temperatures within it are steady, so the sum of (2) and (3) is zero, which gives (4).
>
> (Here is the exact version of the approximation.) Let $R = [x_1, x_2] \times [y_1, y_2]$ be any rectangle inside the solid. The exact net rate of heat loss through the four faces over $R$ is, by (1),
>
> $$
> -K\int_{y_1}^{y_2}\big[T_x(x_2, t) - T_x(x_1, t)\big]\,dt - K\int_{x_1}^{x_2}\big[T_y(s, y_2) - T_y(s, y_1)\big]\,ds = -K\iint_R\big(T_{xx} + T_{yy}\big)\,dA ,
> $$
>
> by the fundamental theorem of calculus in each variable and Fubini's theorem (the second partials are continuous). In the steady state with no sources this loss is $0$ for every such $R$. If $T_{xx} + T_{yy}$ were, say, positive at some interior point, by continuity it would be positive on a small rectangle around it, and the integral over that rectangle would be positive: a contradiction. So $T_{xx} + T_{yy} = 0$ everywhere inside, and with the continuity postulates $T$ is harmonic.

^pf-118-1

*Uses:* [[§118★ Steady Temperatures#^def-118-1|Def. §118.1]], [[§98 Double Integrals Over Rectangles#^thm-98-3|Calc Thm. §98.3]] (Fubini), [[§27★ Harmonic Functions|§27]] (harmonic functions)

> [!remark]- Connections
> - The same derivation in its general form, the heat equation $u_t = k\nabla^2u$ whose steady states are harmonic: [[§35 Potential Equation#^def-35-1|341 Def. §35.1]] and the discussion after it. The exact version above is the divergence theorem in the plane for the field $-K\nabla T$, [[§111 Curl and Divergence#^thm-111-5|Calc Thm. §111.5]] (Green's theorem, normal form).

## Isotherms and Lines of Flow

> [!definition] Definition §118.2: Isotherms; Lines of Flow
> The surfaces $T(x, y) = c_1$, $c_1$ a real constant, are the **isotherms** within the solid. They can also be regarded as curves in the $xy$ plane: then $T(x, y)$ is the temperature at a point $(x, y)$ of a thin sheet of material in that plane whose faces are thermally insulated, and the isotherms are the level curves of $T$. If $S$ is a harmonic conjugate of $T$, the curves $S(x, y) = c_2$ are the **lines of flow** of heat.
>
> *B&C: Sec. 118 (text)*

^def-118-2

> [!theorem] Proposition §118.2: Heat Flows Along the Lines of Flow
> Let $T$ be a steady temperature in a thin sheet and $S$ a harmonic conjugate of $T$.
>
> **(a)** The gradient of $T$ is perpendicular to the isotherm through each point where it is nonzero, and the maximum flux at such a point is in the direction of $-\operatorname{grad} T$, of size $K|\operatorname{grad} T|$.
>
> **(b)** At each point where the analytic function $T(x, y) + iS(x, y)$ is conformal, the curve $S(x, y) = c_2$ through the point has $\operatorname{grad} T$ as a tangent vector.
>
> **(c)** Along a smooth arc $C$ with unit tangent $\mathbf t$ and unit normal $\mathbf N$ obtained by turning $\mathbf t$ through $+\pi/2$,
>
> $$
> \frac{dS}{ds} = -\frac{dT}{dN} = \frac{\Phi}{K} ,
> $$
>
> so the heat crossing $C$ toward the side of $\mathbf N$, per unit time and unit height, is $K\big[S(\text{end}) - S(\text{start})\big]$. In particular, if $dT/dN = 0$ along a part of the boundary of the sheet, the flux across that part is zero (it is **thermally insulated**), $S$ is constant along it, and it is a line of flow.
>
> *B&C: Sec. 118 (text); Sec. 27, Exercise 2*

^prop-118-2

> [!proof]+ Proof
> **(a)** The gradient is perpendicular to level curves ([[§95 Directional Derivatives and the Gradient Vector#^thm-95-7|Calc Thm. §95.7]]). By (1) and $dT/dN = \operatorname{grad} T\cdot\mathbf N$, the flux in the direction $\mathbf N$ is $-K\operatorname{grad} T\cdot\mathbf N$, largest when $\mathbf N$ points along $-\operatorname{grad} T$, where it equals $K|\operatorname{grad} T|$.
>
> **(b)** By the Cauchy–Riemann equations $S_x = -T_y$, $S_y = T_x$, so $\operatorname{grad} S = (-T_y, T_x)$ is $\operatorname{grad} T$ turned through $+\pi/2$. Where $T + iS$ is conformal its derivative $T_x - iT_y$ ([[§21 Cauchy–Riemann Equations|§21]]) is nonzero, so $\operatorname{grad} S \ne \mathbf 0$ and the level curve $S = c_2$ is a smooth curve with normal $\operatorname{grad} S$ (implicit function theorem). Its tangent is perpendicular to $\operatorname{grad} S$, hence parallel to $\operatorname{grad} T$.
>
> **(c)** Write vectors as complex numbers, so $\operatorname{grad} S = i\operatorname{grad} T$ by (b), $\mathbf N = i\mathbf t$, and $\alpha\cdot\beta = \operatorname{Re}(\alpha\bar\beta)$. Then
>
> $$
> \frac{dS}{ds} = \operatorname{Re}\big(i\operatorname{grad} T\;\bar{\mathbf t}\big) = -\operatorname{Re}\big(\operatorname{grad} T\;\overline{i\mathbf t}\big) = -\frac{dT}{dN} ,
> $$
>
> since $\overline{i\mathbf t} = -i\bar{\mathbf t}$. By (1) this is $\Phi/K$. Integrating along $C$ gives the total heat crossing $C$. If $dT/dN = 0$ along a boundary arc, then $\Phi = 0$ there, and $dS/ds = 0$, so $S$ is constant on the arc.

^pf-118-2

*Uses:* [[§118★ Steady Temperatures#^def-118-1|Def. §118.1]], [[§118★ Steady Temperatures#^def-118-2|Def. §118.2]], [[§21 Cauchy–Riemann Equations|§21]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-7|Calc Thm. §95.7]], [[Implicit Function Theorem|452 Implicit Function Theorem]]

> [!remark] Remark: Other Interpretations; the Maximum Principle
> The function $T$ may also denote the concentration of a substance diffusing through a solid; then $K$ is the diffusion constant, and the derivation of (4) applies as well to steady-state diffusion. The maximum principle has a physical reading here: if $T = \operatorname{Re} f$ for $f$ analytic and not constant in a bounded region, $T$ attains its maximum and minimum only on the boundary ([[§59 Maximum Modulus Principle|§59]], Exercise 5). A steady temperature cannot have a hot spot inside: heat would flow away from it in every direction (Fourier's law), the temperature there would drop, and the state would not be steady (B&C Sec. 121, Exercise 13).

^rem-118-1

## Examples

> [!example] Example §118.1: A Quadrant with Edges at 0 and 1
> Find the bounded steady temperatures in a plate in the form of the quadrant $x \ge 0$, $y \ge 0$, with insulated faces and edge temperatures $T(x, 0) = 0$ and $T(0, y) = 1$, and find the isotherms and lines of flow.
>
> **Map.** $w = \operatorname{Log} z = \ln r + i\Theta$ maps the quadrant onto the strip $0 < v < \pi/2$, the positive $x$ axis onto $v = 0$ and the positive $y$ axis onto $v = \pi/2$. In the strip, $T = \frac2\pi v$ is harmonic (the imaginary part of $\frac2\pi w$), bounded, $0$ on $v = 0$ and $1$ on $v = \pi/2$.
>
> **Back to the plate.** By Theorems [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]] and [[§117★ Transformations of Boundary Conditions#^thm-117-2|§117.2]],
>
> $$
> T = \frac2\pi\operatorname{Arg} z = \frac2\pi\arctan\Big(\frac yx\Big) \qquad \Big(0 \le \arctan t \le \frac\pi2\Big).
> $$
>
> **Isotherms and lines of flow.** The isotherms $T = c_1$ are the rays $\theta = \pi c_1/2$ from the corner. Since $-\frac{2i}{\pi}\operatorname{Log} z = \frac2\pi\Theta - \frac{2i}{\pi}\ln r$ is analytic, $S = -\frac2\pi\ln r$ is a harmonic conjugate of $T$, and the lines of flow are the quarter circles $r = $ const. Heat flows from the hot edge to the cold edge along quarter circles. By Proposition §118.2(c), the heat crossing the radial segment $a \le r \le b$ of a ray is $K\big|S(b) - S(a)\big| = \frac{2K}{\pi}\ln\frac ba$, which grows without bound as $a \to 0$: the flow concentrates at the corner, where the edge temperatures jump.
>
> *B&C: Sec. 121, Exercise 1*

^ex-118-1

> [!example] Example §118.2: A Cylindrical Wedge with an Insulated Face
> Find the steady temperatures in a long cylindrical wedge $0 < r < r_0$, $0 < \theta < \theta_0$ whose plane faces $\theta = 0$ and $\theta = \theta_0$ are kept at temperatures $0$ and $T_0$, and whose curved face $r = r_0$ is perfectly insulated.
>
> **Solution.** Try $T = \dfrac{T_0}{\theta_0}\theta = \dfrac{T_0}{\theta_0}\arctan\Big(\dfrac yx\Big)$, the imaginary part of $\frac{T_0}{\theta_0}\log z$ for a branch of $\log z$ containing the wedge. It is harmonic, equals $0$ on $\theta = 0$ and $T_0$ on $\theta = \theta_0$, and on the curved face its normal derivative is $\partial T/\partial r = 0$, since $T$ does not depend on $r$.
>
> **Lines of flow.** As in Example §118.1, $S = -\frac{T_0}{\theta_0}\ln r$, and the lines of flow are the arcs $r = $ const. The insulated face $r = r_0$ is one of them, as Proposition §118.2(c) requires.
>
> *B&C: Sec. 121, Exercise 4*

^ex-118-2

> [!example] Example §118.3: Heat Entering a Semi-Infinite Strip
> For the steady temperature $T = e^{-y}\sin x$ in the strip $0 < x < \pi$, $y > 0$ ([[§116★ Transformations of Harmonic Functions#^ex-116-1|Example §116.1]]: edges at $0$, base at $\sin x$), find the flux into the plate through its base, the lines of flow, and the total heat entering.
>
> **Flux.** On the base the normal pointing into the plate is $\mathbf N = (0, 1)$, so by (1) the flux into the plate is $-KT_y(x, 0) = Ke^{0}\sin x = K\sin x$, positive for $0 < x < \pi$.
>
> **Lines of flow.** $T + iS = -ie^{iz} = e^{-y}\sin x - ie^{-y}\cos x$, so $S = -e^{-y}\cos x$ and the lines of flow are the curves $e^{-y}\cos x = c$. The one with $c = 0$ is the line $x = \pi/2$, by symmetry; the others start on the base and rise toward a side edge.
>
> **Total heat.** Directly, $\int_0^{\pi}K\sin x\,dx = 2K$. By Proposition §118.2(c), traversing the base from $(0, 0)$ to $(\pi, 0)$, the normal $i\mathbf t = i$ points into the plate, and the heat crossing is $K\big[S(\pi, 0) - S(0, 0)\big] = K[1 - (-1)] = 2K$. All of it leaves through the cold side edges, since none can escape to $y = \infty$ ($T$ and its gradient decay like $e^{-y}$).
>
> *B&C: Sec. 27, Example 1; the flux and lines of flow are added*

^ex-118-3
