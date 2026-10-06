---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 4
section: "50★"
powers: "4.6"
aliases: ["Powers 4.6"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§49 The Poisson Integral Formula and the Mean Value Property]] · ↑ [[· 4 The Potential Equation]] · [[§51★ Two-Dimensional Wave Equation꞉ Derivation]] →

*Powers, Section 4.6.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

The heat, wave and potential equations behave very differently, and the difference is predicted by a single number computed from the coefficients of the second derivatives: the sign of $B^2 - 4AC$ classifies a second-order linear equation in two variables as parabolic, hyperbolic or elliptic, like the conic section with the same coefficients. The second half of the section takes stock of what separation of variables can and cannot do. The equation must not mix the two variables in its second-order part, the region must be a "generalized rectangle" bounded by coordinate curves, and opposite sides must carry conditions that are preserved under sums. These limitations explain why Chapters 2–4 look the way they do, and why other methods (transforms, numerical schemes) are needed beyond them.

## Three Equations, Three Behaviors

So far we have concentrated on three homogeneous equations and found these qualitative features:

| Equation | Features |
|---|---|
| Heat | Exponential behavior in time. Existence of a limiting (steady-state) solution. Smooth graph for $t > 0$. |
| Wave | Oscillatory (not always periodic) behavior in time. Retention of discontinuities for $t > 0$. |
| Potential | Smooth surface. Maximum principle. Mean value property. |

The heat features are those of [[§25 Example꞉ Fixed End Temperatures#^thm-25-5|Theorem §25.5]] and [[§31 Generalities on the Heat Conduction Problem#^thm-31-4|Theorem §31.4]] (terms $e^{-\lambda_n^2kt}$ that smooth out any initial jump), the wave features those of [[§38 Solution of the Vibrating String Problem#^thm-38-2|Theorem §38.2]] and [[§39 d'Alembert's Solution#^thm-39-3|Theorem §39.3]] (traveling waves that carry corners and jumps along unchanged), and the potential features those of [[§48 Potential in a Disk|§48]] ([[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-2|Theorem §49.2]], [[§49 The Poisson Integral Formula and the Mean Value Property#^thm-49-3|Theorem §49.3]]).

## Classification

> [!definition] Definition §50.1: Elliptic, Parabolic and Hyperbolic Equations
> The most general second-order linear partial differential equation in two variables is
>
> $$
> A\frac{\partial^2u}{\partial\xi^2} + B\frac{\partial^2u}{\partial\xi\,\partial\eta} + C\frac{\partial^2u}{\partial\eta^2} + D\frac{\partial u}{\partial\xi} + E\frac{\partial u}{\partial\eta} + Fu + G = 0 ,
> $$
>
> where $A, B, C, \ldots$ are, in general, functions of $\xi$ and $\eta$. (Greek letters are used for the independent variables to avoid implying any relation to space or time.) The equation is called
>
> $$
> \text{elliptic if } B^2 - 4AC < 0, \qquad \text{parabolic if } B^2 - 4AC = 0, \qquad \text{hyperbolic if } B^2 - 4AC > 0 .
> $$
>
> Because $A$, $B$ and $C$ are functions of $\xi$ and $\eta$ (not of $u$), the classification of an equation may vary from point to point.
>
> *Powers: 4.6 (text)*

^def-50-1

> [!remark]- Connections
> - The names come from conic sections: $A\xi^2 + B\xi\eta + C\eta^2 = 1$ is the level curve of the quadratic form with matrix $\begin{bmatrix} A & B/2 \\ B/2 & C \end{bmatrix}$, whose determinant is $AC - B^2/4 = -\frac14(B^2 - 4AC)$; it is an ellipse, a pair of lines (degenerate parabola) or a hyperbola according to the sign, [[§59★ Quadratic Forms#^prop-59-3|235 Prop. §59.3]]. For constant coefficients, rotating the $(\xi, \eta)$ axes to the principal axes of this form, [[§59★ Quadratic Forms#^thm-59-2|235 Thm. §59.2]], removes the mixed term $Bu_{\xi\eta}$ and turns the second-order part into $\lambda_1u_{\xi'\xi'} + \lambda_2u_{\eta'\eta'}$: Laplace-like if $\lambda_1\lambda_2 > 0$, wave-like if $\lambda_1\lambda_2 < 0$, heat-like if one of them is $0$.

The classification determines important features of the solution, and also dictates the method of attack when numerical techniques are used ([[§71★ Potential Equation|§71★]], [[§69★ Heat Problems|§69★]], [[§70★ Wave Equation|§70★]]).

> [!example] Example §50.1: Heat, Wave and Potential Equations
> **Heat.** $u_{xx} = \frac1ku_t$: with $\xi = x$, $\eta = t$, $A = 1$, $B = 0$, $C = 0$, so $B^2 - 4AC = 0$: **parabolic**.
>
> **Wave.** $u_{xx} = \frac{1}{c^2}u_{tt}$, that is, $u_{xx} - \frac{1}{c^2}u_{tt} = 0$: $A = 1$, $B = 0$, $C = -1/c^2$, so $B^2 - 4AC = 4/c^2 > 0$: **hyperbolic**.
>
> **Potential.** $u_{xx} + u_{yy} = 0$: $A = C = 1$, $B = 0$, so $B^2 - 4AC = -4 < 0$: **elliptic**.
>
> The lower-order terms play no role: the heat equation with lateral convection, $u_t = u_{xx} - \gamma^2(u - T)$ ([[§24 Steady-State Temperatures#^ex-24-5|Example §24.5]]), is still parabolic, and the Poisson equation ([[§46 Further Examples for a Rectangle#^def-46-1|Definition §46.1]]) is still elliptic.
>
> *Powers: 4.6 (text)*

^ex-50-1

## Limitations of the Product Method

The question naturally arises whether separation of variables works on all equations. The answer is no, and in general it is difficult to say just which equations can be solved by this method. But it is necessary to have $B \equiv 0$.

> [!remark] Remark: Why the Mixed Term Spoils Separation
> (Powers states the condition $B \equiv 0$ without argument; here is the idea.) Take constant coefficients and $u = X(\xi)Y(\eta)$. Dividing the second-order part by $XY$ gives
>
> $$
> A\frac{X''}{X} + B\,\frac{X'}{X}\cdot\frac{Y'}{Y} + C\frac{Y''}{Y} .
> $$
>
> The first and last terms are a function of $\xi$ plus a function of $\eta$, which is what makes "both sides equal a constant" work. The middle term is a *product* of a function of $\xi$ and a function of $\eta$, and such a product cannot in general be split into a sum; so the equation does not decouple into two ordinary differential equations for $X$ and $Y$. (For constant coefficients the mixed term can be removed first by rotating the axes, as in the Connections of Definition §50.1, but the rotated region is usually no longer convenient.)

^rem-50-1

> [!example] Example §50.2: An Equation of Mixed Type That Does Not Separate
> Consider
>
> $$
> (\xi + \eta^2)\frac{\partial^2u}{\partial\xi^2} + \frac{\partial^2u}{\partial\eta^2} = 0 .
> $$
>
> **Classification.** $A = \xi + \eta^2$, $B = 0$, $C = 1$, so $B^2 - 4AC = -4(\xi + \eta^2)$. The equation is elliptic where $\xi + \eta^2 > 0$, parabolic on the parabola $\xi = -\eta^2$, and hyperbolic inside it, where $\xi + \eta^2 < 0$ (figure below). The type genuinely varies from point to point.
>
> **No separation, although $B = 0$.** (Powers asserts this; here is why.) Suppose $u = X(\xi)Y(\eta)$ is a solution with $X$, $Y$ not identically zero. Dividing by $XY$ where it is nonzero and writing $F(\xi) = X''/X$, $G(\eta) = Y''/Y$,
>
> $$
> (\xi + \eta^2)F(\xi) + G(\eta) = 0 .
> $$
>
> Differentiate with respect to $\xi$: $(\xi + \eta^2)F'(\xi) + F(\xi) = 0$. Differentiate this with respect to $\eta$: $2\eta F'(\xi) = 0$, so $F' \equiv 0$, and then the previous equation gives $F \equiv 0$, and the first gives $G \equiv 0$. So $X'' = 0$ and $Y'' = 0$: the only product solutions are $(a + b\xi)(c + d\eta)$, far too few to satisfy boundary conditions. The coefficient $\xi + \eta^2$ couples the variables even though there is no mixed derivative; $B \equiv 0$ is necessary but not sufficient.
>
> *Powers: 4.6 (text)*

^ex-50-2

![[m341-40-1.svg]]
*The type of $(\xi + \eta^2)u_{\xi\xi} + u_{\eta\eta} = 0$ in the $\xi\eta$-plane: elliptic outside the parabola $\xi = -\eta^2$ (green), hyperbolic inside it (orange), parabolic on the parabola itself (red). Equations whose type changes across a curve, like this one, arise for flows that pass from subsonic to supersonic speeds.*

The region in which the solution is to be found also limits the applicability of the method.

> [!definition] Definition §50.2: Generalized Rectangle
> A **generalized rectangle** is a region bounded by coordinate curves of the coordinate system of the partial differential equation. Put another way, the region is described by inequalities on the coordinates, whose endpoints are fixed quantities.
>
> *Powers: 4.6 (text)*

^def-50-2

> [!example] Example §50.3: Regions Used So Far
> The regions in which equations were solved in Chapters 2–4 are described by the following sets of inequalities:
>
> | Region | Where |
> |---|---|
> | $0 < x < a$, $\ 0 < t$ | finite rod or string ([[§25 Example꞉ Fixed End Temperatures|§25]], [[§38 Solution of the Vibrating String Problem|§38]]) |
> | $0 < x$, $\ 0 < t$ | semi-infinite rod ([[§32 Semi-Infinite Rod|§32]]) |
> | $-\infty < x < \infty$, $\ 0 < t$ | infinite rod or string ([[§33 Infinite Rod|§33]], [[§39 d'Alembert's Solution|§39]]) |
> | $0 < x < a$, $\ 0 < y < b$ | rectangle ([[§45 Potential in a Rectangle|§45]]) |
> | $0 < r < c$, $\ -\pi < \theta \le \pi$ | disk ([[§48 Potential in a Disk|§48]]) |
>
> All of these are generalized rectangles, but only one is an ordinary rectangle. In polar coordinates an annulus $c_1 < r < c_2$, a sector $0 < \theta < \alpha$, and a sector of an annulus are generalized rectangles too. An L-shaped region is not a generalized rectangle: although its sides lie on coordinate lines, it cannot be described by inequalities $a_1 < x < a_2$, $b_1 < y < b_2$ with fixed endpoints, because the range of $y$ depends on $x$. The methods of this chapter would break down if applied, for instance, to the potential equation there.
>
> *Powers: 4.6 (text)*

^ex-50-3

Finally, there are restrictions on the kinds of boundary conditions that can be handled. From the examples in this chapter it is clear that we need homogeneous or "homogeneous-like" conditions on opposite sides of a generalized rectangle.

> [!remark] Remark: Homogeneous-Like Conditions
> Examples of homogeneous-like conditions are the requirement that a function remain bounded as some variable tends to infinity ([[§47 Potential in Unbounded Regions#^rem-47-1|§47]]), and the periodic conditions at $\theta = \pm\pi$ ([[§48 Potential in a Disk#^prop-48-1|Proposition §48.1]]). The point is that if two or more functions satisfy the conditions, so does a sum of those functions. For instance, if $f_1, f_2, \ldots$ all satisfy $f(-\pi) = f(\pi)$, $f'(-\pi) = f'(\pi)$, then so does $c_1f_1 + c_2f_2$, because evaluation and differentiation are linear; and a sum of finitely many bounded functions is bounded. This closure under sums is exactly what superposition of product solutions needs. A condition like $u(0, y) = g(y)$ with $g \ne 0$ does not have it, which is why such conditions are split off ([[§46 Further Examples for a Rectangle#^rem-46-1|Remark: Method — Splitting a Rectangle Problem]]).

^rem-50-2

In spite of these limitations, separation of variables works well on many important problems in two or more variables and provides insight into the nature of their solutions. Moreover, Powers notes that in those cases where separation of variables can be carried out, it will find a solution if one exists. Where it cannot, other tools take over: the Laplace transform ([[§66★ Partial Differential Equations|§66★]]) and numerical methods (Chapter 7★, [[§68★ Boundary Value Problems|§68★]]).
