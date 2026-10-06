---
type: section
subject: "[[Complex Variables]]"
chapter: 10
section: 120
bc: "120"
aliases: ["B&C 120"]
tags: [complex-variables, math342, extension]
---
← [[§119★ Steady Temperatures in a Half Plane]] · ↑ [[· 10★ Applications of Conformal Mapping]] · [[§121★ Temperatures in a Quadrant]] →

*Brown–Churchill, Section 120 (with Exercises 2 and 11 of Section 121).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A solved problem becomes the solution of every problem that can be mapped onto it. Here $w = \sin z$ carries the semi-infinite slab $-\pi/2 < x < \pi/2$, $y > 0$ onto the upper half plane, with the base going to the segment $-1 < u < 1$ and the two sides to the rest of the $u$ axis, so the half-plane temperature of [[§119★ Steady Temperatures in a Half Plane|§119]] gives at once the steady temperature in a slab whose base is hot and whose sides are cold. The result is the closed form of the Fourier series that separation of variables produces for the same problem, and from it the isotherms and the heat flux through the faces follow by differentiation.

## The Semi-Infinite Slab

> [!example] Example §120.1: A Slab with a Hot Base and Cold Sides
> A semi-infinite slab in space is bounded by the planes $x = \pm\pi/2$ and $y = 0$; the first two are kept at temperature $0$ and the third at temperature $1$. Find the temperature $T(x, y)$ at interior points. (Equivalently: the temperatures in a thin plate $-\pi/2 \le x \le \pi/2$, $y \ge 0$ with perfectly insulated faces; B&C's Fig. 156.)
>
> **The problem.**
>
> $$
> T_{xx}(x, y) + T_{yy}(x, y) = 0 \qquad \Big(-\frac\pi2 < x < \frac\pi2,\ y > 0\Big), \qquad (1)
> $$
>
> $$
> T\Big(-\frac\pi2, y\Big) = T\Big(\frac\pi2, y\Big) = 0 \quad (y > 0), \qquad (2) \qquad\qquad T(x, 0) = 1 \quad \Big(-\frac\pi2 < x < \frac\pi2\Big), \qquad (3)
> $$
>
> with $T$ bounded.
>
> **The map.** By [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]], the transformation
>
> $$
> w = \sin z \qquad (4)
> $$
>
> maps the half strip one to one onto the upper half plane $v > 0$: the base $-\pi/2 < x < \pi/2$, $y = 0$ goes onto the segment $-1 < u < 1$ ($\sin x$), the side $x = \pi/2$ onto $u > 1$ ($\sin(\frac\pi2 + iy) = \cosh y$), and the side $x = -\pi/2$ onto $u < -1$. It is conformal except at $z = \pm\pi/2$, where $\cos z = 0$. So it transforms the problem into the one of Example [[§119★ Steady Temperatures in a Half Plane#^ex-119-1|§119.1]], whose solution (6) gives
>
> $$
> T = \frac1\pi\arctan\Big(\frac{2v}{u^2 + v^2 - 1}\Big) \qquad (0 \le \arctan t \le \pi). \qquad (5)
> $$
>
> **Back to $x$ and $y$.** By [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]], $u = \sin x\cosh y$ and $v = \cos x\sinh y$, so (5) becomes
>
> $$
> T = \frac1\pi\arctan\Big(\frac{2\cos x\sinh y}{\sin^2x\cosh^2y + \cos^2x\sinh^2y - 1}\Big) .
> $$
>
> With $\cosh^2y = 1 + \sinh^2y$, the denominator is $\sin^2x + \sinh^2y - 1 = \sinh^2y - \cos^2x$, so the quotient can be written
>
> $$
> \frac{2\cos x\sinh y}{\sinh^2y - \cos^2x} = \frac{2(\cos x/\sinh y)}{1 - (\cos x/\sinh y)^2} = \tan 2\alpha, \qquad\text{where } \tan\alpha = \frac{\cos x}{\sinh y} ,
> $$
>
> with $0 \le \alpha < \pi/2$ because $\cos x/\sinh y \ge 0$. Then $0 \le 2\alpha < \pi$ lies in the range of the arctangent in (5), so $T = \frac1\pi\cdot 2\alpha$, that is,
>
> $$
> T = \frac2\pi\arctan\Big(\frac{\cos x}{\sinh y}\Big) \qquad \Big(0 \le \arctan t \le \frac\pi2\Big). \qquad (6)
> $$
>
> **Why it is the solution.** $\sin z$ is entire and (5) is harmonic in $v > 0$, so (6) is harmonic in the half strip (Theorem [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]]). The function (5) is $1$ for $|u| < 1$, $v = 0$ and $0$ for $|u| > 1$, $v = 0$, so (6) satisfies (2) and (3) (Theorem [[§117★ Transformations of Boundary Conditions#^thm-117-2|§117.2]]); directly, $\cos(\pm\pi/2) = 0$ gives $T = 0$ on the sides, and as $y \to 0^+$ with $|x| < \pi/2$ the argument tends to $+\infty$ and $T \to 1$. Moreover $0 \le T \le 1$ throughout.
>
> **Isotherms.** $T = c_1$ $(0 < c_1 < 1)$ means $\cos x = \tan\big(\frac{\pi c_1}{2}\big)\sinh y$: within the slab, surfaces through the edges $(\pm\pi/2, 0)$.
>
> **Flux.** Differentiating (6),
>
> $$
> T_y = -\frac2\pi\,\frac{\cos x\cosh y}{\sinh^2y + \cos^2x}, \qquad T_x = -\frac2\pi\,\frac{\sin x\sinh y}{\sinh^2y + \cos^2x} .
> $$
>
> If $K$ is the thermal conductivity, the flux of heat into the slab through the face $y = 0$ (normal $(0, 1)$) is
>
> $$
> -KT_y(x, 0) = \frac{2K}{\pi\cos x} \qquad \Big(-\frac\pi2 < x < \frac\pi2\Big),
> $$
>
> and the flux outward through the face $x = \pi/2$ (normal $(1, 0)$) is
>
> $$
> -KT_x\Big(\frac\pi2, y\Big) = \frac{2K}{\pi\sinh y} \qquad (y > 0).
> $$
>
> Both become infinite at the edge $(\pi/2, 0)$, where the boundary temperature jumps.
>
> *B&C: Sec. 120 (text)*

^ex-120-1

> [!remark]- Connections
> - The same problem by separation of variables: [[§38 Potential in Unbounded Regions#^thm-38-1|341 Thm. §38.1]] gives the series $\frac4\pi\sum_{n\text{ odd}}\frac1n\sin(nx')e^{-ny}$ for the slot $0 < x' < \pi$, and [[§38 Potential in Unbounded Regions#^ex-38-1|341 Ex. §38.1]] sums it to $\frac2\pi\arctan\big(\sin x'/\sinh y\big)$. With $x' = x + \pi/2$, $\sin x' = \cos x$, this is (6). (Numerically, at $(x, y) = (0.3, 0.5)$ both give $0.682105$.) B&C's remark that separation of variables is "more direct, but gives the solution in the form of an infinite series" is exactly this comparison.

![[m342-120-1.svg]]
*Example §120.1. Isotherms $T = 0.1, \ldots, 0.9$ (blue) of $T = \frac2\pi\arctan(\cos x/\sinh y)$ in the slab: every isotherm runs from one bottom edge $(\pm\pi/2, 0)$ to the other, the hotter ones hugging the base $T = 1$ (red). Lines of flow (orange), the level curves of $\ln|(\sin z - 1)/(\sin z + 1)|$, carry heat from the base to the cold sides.*

## Uniqueness and a Related Strip

> [!example] Example §120.2: Infinitely Many Unbounded Solutions
> If the condition that $T$ be bounded is omitted, the problem (1)–(3) has infinitely many solutions: add to (6) the imaginary part of $A\sin z$, $A$ any real constant.
>
> $\operatorname{Im}(A\sin z) = A\cos x\sinh y$ is harmonic (imaginary part of an entire function), vanishes on $x = \pm\pi/2$ (where $\cos x = 0$) and on $y = 0$ (where $\sinh y = 0$). So $T + A\cos x\sinh y$ is harmonic and satisfies (2) and (3) for every $A$; for $A \ne 0$ it is unbounded, since $\sinh y \to \infty$. Boundedness is what makes (6) the answer. (Compare [[§119★ Steady Temperatures in a Half Plane#^ex-119-3|Example §119.3]]; in the $w$ plane the added term is $A\operatorname{Im} w = Av$.)
>
> *B&C: Sec. 121, Exercise 11*

^ex-120-2

> [!example] Example §120.3: A Half Strip with One Hot Side
> Solve the [[§116★ Transformations of Harmonic Functions#^def-116-new1|Dirichlet problem]]
>
> $$
> H_{xx} + H_{yy} = 0 \quad \Big(0 < x < \frac\pi2,\ y > 0\Big), \qquad H(x, 0) = 0, \qquad H(0, y) = 1, \qquad H\Big(\frac\pi2, y\Big) = 0 ,
> $$
>
> with $0 \le H \le 1$, by transforming it into the quadrant problem of [[§118★ Steady Temperatures#^ex-118-1|Example §118.1]].
>
> **Map.** $w = \sin z$ maps the half strip $0 < x < \pi/2$, $y > 0$ onto the first quadrant $u > 0$, $v > 0$ ([[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-2|Example §104.2]]): the side $x = 0$ goes to $\sin(iy) = i\sinh y$, the positive $v$ axis; the base goes to $\sin x \in (0, 1)$ and the side $x = \pi/2$ to $\cosh y \in (1, \infty)$, together the positive $u$ axis. So the new problem is: harmonic in the quadrant, $1$ on the positive $v$ axis, $0$ on the positive $u$ axis.
>
> **Solve and compose.** By [[§118★ Steady Temperatures#^ex-118-1|Example §118.1]], $H = \frac2\pi\operatorname{Arg} w = \frac2\pi\arctan\frac vu$. With $u = \sin x\cosh y$, $v = \cos x\sinh y$, $\frac vu = \frac{\cos x\sinh y}{\sin x\cosh y} = \frac{\tanh y}{\tan x}$, so
>
> $$
> H = \frac2\pi\arctan\Big(\frac{\tanh y}{\tan x}\Big) \qquad \Big(0 \le \arctan t \le \frac\pi2\Big).
> $$
>
> **Check.** As $x \to 0^+$ ($y > 0$), $\tanh y/\tan x \to +\infty$ and $H \to 1$; at $x = \pi/2$, $1/\tan x = 0$ and $H = 0$; at $y = 0$, $\tanh 0 = 0$ and $H = 0$. And $H$ is harmonic by [[§116★ Transformations of Harmonic Functions#^thm-116-1|Theorem §116.1]].
>
> *B&C: Sec. 121, Exercise 2*

^ex-120-3
