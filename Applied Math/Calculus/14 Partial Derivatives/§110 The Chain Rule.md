---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 110
stewart: "14.5"
aliases: ["Stewart 14.5"]
tags: [calculus, math233]
---
← [[§109 Tangent Planes and Linear Approximations]] · ↑ [[· 14 Partial Derivatives]] · [[§111 Directional Derivatives and the Gradient Vector]] →

*Stewart, Section 14.5 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q28), Practice Exam 1 (Q4(c), answer key), Practice Final Set 2 (Part I, Q2).*

The one-variable Chain Rule, $\frac{dy}{dt} = \frac{dy}{dx}\frac{dx}{dt}$, has several multivariable versions, one for each way of composing functions. If $z = f(x, y)$ and $x$, $y$ depend on $t$, then $\frac{dz}{dt}$ is a sum of two terms, one for each intermediate variable, each of the one-variable shape. The proof is the definition of differentiability divided by $\Delta t$. With $x$ and $y$ depending on several variables, and $f$ on several intermediate variables, the rule is the same: one term for each path from the dependent variable to the independent one in a tree diagram. As an application, implicit differentiation gets a formula, $\frac{dy}{dx} = -F_x/F_y$, whose validity is guaranteed by the Implicit Function Theorem.

## The Chain Rule: Case 1

> [!theorem] Theorem §130.1: The Chain Rule (Case 1)
> Suppose that $z = f(x, y)$ is a differentiable function of $x$ and $y$ ([[§109 Tangent Planes and Linear Approximations#^def-109-4|Definition §109.4]]), where $x = g(t)$ and $y = h(t)$ are both differentiable functions of $t$. Then $z$ is a differentiable function of $t$ and
>
> $$
> \frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} .
> $$
>
> Since $\partial z / \partial x$ is often written for $\partial f / \partial x$, this is also written $\dfrac{dz}{dt} = \dfrac{\partial z}{\partial x}\dfrac{dx}{dt} + \dfrac{\partial z}{\partial y}\dfrac{dy}{dt}$.
>
> *Stewart: 14.5, Theorem 1*

^thm-110-1

> [!proof]+ Proof
> Fix $t$. A change $\Delta t$ in $t$ produces changes $\Delta x = g(t + \Delta t) - g(t)$ in $x$ and $\Delta y = h(t + \Delta t) - h(t)$ in $y$. These in turn produce a change $\Delta z$ in $z$, and since $f$ is differentiable, [[§109 Tangent Planes and Linear Approximations#^def-109-4|Definition §109.4]] gives
>
> $$
> \Delta z = \frac{\partial f}{\partial x}\,\Delta x + \frac{\partial f}{\partial y}\,\Delta y + \varepsilon_1\,\Delta x + \varepsilon_2\,\Delta y ,
> $$
>
> where $\varepsilon_1 \to 0$ and $\varepsilon_2 \to 0$ as $(\Delta x, \Delta y) \to (0, 0)$. If $\varepsilon_1$ and $\varepsilon_2$ are not defined at $(0, 0)$, define them to be $0$ there; then they are continuous at $(0, 0)$, and the formula still holds when $\Delta x = \Delta y = 0$. Dividing both sides by $\Delta t \ne 0$,
>
> $$
> \frac{\Delta z}{\Delta t} = \frac{\partial f}{\partial x}\frac{\Delta x}{\Delta t} + \frac{\partial f}{\partial y}\frac{\Delta y}{\Delta t} + \varepsilon_1 \frac{\Delta x}{\Delta t} + \varepsilon_2 \frac{\Delta y}{\Delta t} .
> $$
>
> Now let $\Delta t \to 0$. Then $\Delta x = g(t + \Delta t) - g(t) \to 0$, because $g$ is differentiable and therefore continuous ([[§15 The Derivative as a Function#^thm-15-1|Theorem §15.1]]); similarly $\Delta y \to 0$. This in turn means that $\varepsilon_1 \to 0$ and $\varepsilon_2 \to 0$: as functions of $(\Delta x, \Delta y)$ they are continuous at $(0, 0)$ with value $0$, and $(\Delta x, \Delta y) \to (0, 0)$ as $\Delta t \to 0$ (the composition argument of [[§107 Limits and Continuity#^thm-107-5|Theorem §107.5]](b)). So
>
> $$
> \begin{aligned}
> \frac{dz}{dt} = \lim_{\Delta t \to 0} \frac{\Delta z}{\Delta t}
> &= \frac{\partial f}{\partial x} \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} + \frac{\partial f}{\partial y} \lim_{\Delta t \to 0} \frac{\Delta y}{\Delta t} + \Big( \lim_{\Delta t \to 0} \varepsilon_1 \Big) \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} + \Big( \lim_{\Delta t \to 0} \varepsilon_2 \Big) \lim_{\Delta t \to 0} \frac{\Delta y}{\Delta t} \\
> &= \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + 0 \cdot \frac{dx}{dt} + 0 \cdot \frac{dy}{dt}
> = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} .
> \end{aligned}
> $$

^pf-110-1

*Uses:* [[§109 Tangent Planes and Linear Approximations#^def-109-3|Def. §109.3]], [[§109 Tangent Planes and Linear Approximations#^def-109-4|Def. §109.4]], [[§15 The Derivative as a Function#^thm-15-1|§15.1]] (differentiable implies continuous), [[§107 Limits and Continuity#^thm-107-5|§107.5]] (composition with a continuous function)

Notice the similarity with the differential $dz = \frac{\partial z}{\partial x}\,dx + \frac{\partial z}{\partial y}\,dy$ of [[§109 Tangent Planes and Linear Approximations#^def-109-5|Definition §109.5]]. Recall that $f$ is differentiable whenever $f_x$ and $f_y$ are continuous ([[§109 Tangent Planes and Linear Approximations#^thm-109-2|Theorem §109.2]]).

> [!remark]- Connections
> - Rigorous treatment: [[§8 Algebra of Differentiable Functions#^thm-8-7|452 Thm. §8.7]] (differentiable inner and outer functions, by the same expansion) and [[§12 Composition of Functions and the Chain Rule#^thm-12-2|452 Thm. §12.2]] (under continuity of the partials); hub [[Multivariable Chain Rule]]. In matrix form it says that the derivative of a composite is the product of the Jacobian matrices ([[§7 Differentiability#^def-7-3|452 Def. §7.3]]).

> [!example] Example §130.1: Case 1
> **(a)** If $z = x^2 y + 3xy^4$, where $x = \sin 2t$ and $y = \cos t$, find $dz/dt$ when $t = 0$.
>
> $$
> \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} = (2xy + 3y^4)(2\cos 2t) + (x^2 + 12xy^3)(-\sin t) .
> $$
>
> There is no need to substitute for $x$ and $y$ in terms of $t$: when $t = 0$, $x = \sin 0 = 0$ and $y = \cos 0 = 1$, so
>
> $$
> \left. \frac{dz}{dt} \right|_{t = 0} = (0 + 3)(2\cos 0) + (0 + 0)(-\sin 0) = 6 .
> $$
>
> This is the rate of change of $z$ as the point $(x, y)$ moves along the curve $C$: $x = \sin 2t$, $y = \cos t$, at the point $(0, 1)$. If $z = T(x, y) = x^2 y + 3xy^4$ is the temperature at $(x, y)$, then $dz/dt$ is the rate at which the temperature changes along $C$.
>
> **(b)** Let $z = x^2 y$, and let $x$, $y$ be functions of $t$ with $x(1) = 1$, $y(1) = 2$, $x(2) = 3$, $y(2) = 4$, $x'(1) = A$, $y'(1) = B$, $x'(2) = C$, $y'(2) = D$. Find $dz/dt$ when $t = 1$. (Choices: $4A + D$, $4A + B$, $4C + D$, $A + 2D$, $4C + 2D$, $A + 4B$.)
>
> $z_x = 2xy$ and $z_y = x^2$. At $t = 1$ the point is $(x, y) = (1, 2)$, so $z_x = 2(1)(2) = 4$ and $z_y = 1^2 = 1$, and
>
> $$
> \left. \frac{dz}{dt} \right|_{t = 1} = 4\,x'(1) + 1 \cdot y'(1) = 4A + B . \qquad \textbf{Answer: } 4A + B .
> $$
>
> The values at $t = 2$ are irrelevant: everything is evaluated at the same $t$.
>
> *Stewart: Example 14.5.1*
> *Source: 233 Practice Final Set 2, Part I Q2*

^ex-110-1

For instance, for one mole of an ideal gas $P = 8.31\,T/V$ (kPa, K, L). If $T = 300$ and increases at $0.1$ K/s while $V = 100$ and increases at $0.2$ L/s, then $\frac{dP}{dt} = \frac{8.31}{V}\frac{dT}{dt} - \frac{8.31\,T}{V^2}\frac{dV}{dt} = \frac{8.31}{100}(0.1) - \frac{8.31(300)}{100^2}(0.2) = -0.04155$: the pressure decreases at about $0.042$ kPa/s (Stewart, Example 14.5.2).

## The Chain Rule: Case 2

> [!theorem] Theorem §130.2: The Chain Rule (Case 2)
> Suppose that $z = f(x, y)$ is a differentiable function of $x$ and $y$, where $x = g(s, t)$ and $y = h(s, t)$ are differentiable functions of $s$ and $t$. Then
>
> $$
> \frac{\partial z}{\partial s} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial s} ,
> \qquad
> \frac{\partial z}{\partial t} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial t} .
> $$
>
> *Stewart: 14.5, Theorem 2*

^thm-110-2

> [!proof]+ Proof
> In computing $\partial z / \partial t$ we hold $s$ fixed and compute the ordinary derivative of $z$ with respect to $t$ ([[§108 Partial Derivatives#^thm-108-1|Theorem §108.1]]). With $s$ fixed, $x = g(s, t)$ and $y = h(s, t)$ are differentiable functions of the single variable $t$, with derivatives $\partial x / \partial t$ and $\partial y / \partial t$. So [[§110 The Chain Rule#^thm-110-1|Theorem §110.1]] applies and gives the formula for $\partial z / \partial t$. The same argument with $t$ fixed gives $\partial z / \partial s$.

^pf-110-2

*Uses:* [[§110 The Chain Rule#^thm-110-1|§110.1]], [[§108 Partial Derivatives#^thm-108-1|§108.1]]

> [!remark]- Connections
> - PDE version: this chain rule, applied twice, gives the Laplacian in polar coordinates, [[§44 Potential Equation#^thm-44-3|341 Thm. §44.3]], and the wave equation in the characteristic coordinates $x \pm ct$, [[§39 d'Alembert's Solution#^thm-39-1|341 Thm. §39.1]].

> [!remark] Remark: Tree Diagrams
> Case 2 has three kinds of variables: $s$ and $t$ are **independent** variables, $x$ and $y$ are **intermediate** variables, and $z$ is the **dependent** variable. [[§110 The Chain Rule#^thm-110-2|Theorem §110.2]] has one term for each intermediate variable, and each term resembles the one-variable Chain Rule ([[§20 The Chain Rule#^thm-20-2|Theorem §20.2]]). To remember it, draw a **tree diagram**: branches from the dependent variable $z$ to the intermediate variables $x$ and $y$, then from each of these to the independent variables $s$ and $t$, and write on each branch the corresponding partial derivative. To find $\partial z / \partial s$, multiply the partial derivatives along each path from $z$ to $s$ and add the products:
>
> $$
> \frac{\partial z}{\partial s} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial s} .
> $$
>
> Similarly, $\partial z / \partial t$ uses the paths from $z$ to $t$.

^rem-110-1

![[m233-94-1.svg]]
*The tree diagram for Case 2. Each path from $z$ down to $s$ (red) contributes the product of the derivatives on its branches; adding the two products gives $\partial z / \partial s$. The paths to $t$ (blue) give $\partial z / \partial t$.*

> [!example] Example §130.2: Case 2 at a Point
> Let $f(x, y) = x^2 - 2xy + 3y + y^2$, where $x = st^2$ and $y = e^{s - t}$. Find $\partial f / \partial s$ and $\partial f / \partial t$ at $s = 2$, $t = 1$.
>
> **At the point.** When $s = 2$ and $t = 1$: $x = 2 \cdot 1^2 = 2$ and $y = e^{2 - 1} = e$.
>
> **Outer partials.**
>
> $$
> f_x = 2x - 2y = 4 - 2e , \qquad f_y = -2x + 3 + 2y = -1 + 2e .
> $$
>
> **Inner partials.**
>
> $$
> \frac{\partial x}{\partial s} = t^2 = 1 , \quad \frac{\partial x}{\partial t} = 2st = 4 , \qquad \frac{\partial y}{\partial s} = e^{s - t} = e , \quad \frac{\partial y}{\partial t} = -e^{s - t} = -e .
> $$
>
> **Chain Rule.**
>
> $$
> \begin{aligned}
> \frac{\partial f}{\partial s} &= f_x \frac{\partial x}{\partial s} + f_y \frac{\partial y}{\partial s} = (4 - 2e)(1) + (-1 + 2e)(e) = 4 - 3e + 2e^2 , \\
> \frac{\partial f}{\partial t} &= f_x \frac{\partial x}{\partial t} + f_y \frac{\partial y}{\partial t} = (4 - 2e)(4) + (-1 + 2e)(-e) = 16 - 7e - 2e^2 .
> \end{aligned}
> $$
>
> (The question writes $df/ds$ and $df/dt$ for these partial derivatives.) Stewart's Example 14.5.3 is the same computation with symbols left in: for $z = e^x \sin y$, $x = st^2$, $y = s^2 t$, $\partial z / \partial s = (e^x \sin y)(t^2) + (e^x \cos y)(2st)$.
>
> *Source: 233 Midterm 1 Practice Questions, Q28*

^ex-110-2

## The Chain Rule: General Version

> [!theorem] Theorem §131.1: The Chain Rule (General Version)
> Suppose that $u$ is a differentiable function of the $n$ variables $x_1, x_2, \ldots, x_n$ and each $x_j$ is a differentiable function of the $m$ variables $t_1, t_2, \ldots, t_m$. Then $u$ is a function of $t_1, t_2, \ldots, t_m$ and
>
> $$
> \frac{\partial u}{\partial t_i} = \frac{\partial u}{\partial x_1}\frac{\partial x_1}{\partial t_i} + \frac{\partial u}{\partial x_2}\frac{\partial x_2}{\partial t_i} + \cdots + \frac{\partial u}{\partial x_n}\frac{\partial x_n}{\partial t_i}
> $$
>
> for each $i = 1, 2, \ldots, m$.
>
> *Stewart: 14.5, Theorem 3*

^thm-110-3

> [!proof]+ Proof
> Stewart says only that "the proof is similar to that of Case 1"; here it is. Fix $i$ and hold the other $t$'s fixed, so that each $x_j$ is a function of $t_i$ alone, with derivative $\partial x_j / \partial t_i$; in particular it is continuous in $t_i$. Differentiability of $u$ ([[§109 Tangent Planes and Linear Approximations#^def-109-6|Definition §109.6]], the $n$-variable form of [[§109 Tangent Planes and Linear Approximations#^def-109-4|Definition §109.4]]) says that
>
> $$
> \Delta u = \sum_{j=1}^n \frac{\partial u}{\partial x_j}\,\Delta x_j + \sum_{j=1}^n \varepsilon_j\,\Delta x_j , \qquad \varepsilon_j \to 0 \text{ as } (\Delta x_1, \ldots, \Delta x_n) \to \mathbf{0}
> $$
>
> (with $\varepsilon_j = 0$ when all $\Delta x_j = 0$). Divide by $\Delta t_i \ne 0$ and let $\Delta t_i \to 0$. Then each $\Delta x_j \to 0$, so each $\varepsilon_j \to 0$, while $\Delta x_j / \Delta t_i \to \partial x_j / \partial t_i$. Hence
>
> $$
> \frac{\partial u}{\partial t_i} = \lim_{\Delta t_i \to 0} \frac{\Delta u}{\Delta t_i} = \sum_{j=1}^n \frac{\partial u}{\partial x_j}\frac{\partial x_j}{\partial t_i} + \sum_{j=1}^n 0 \cdot \frac{\partial x_j}{\partial t_i} = \sum_{j=1}^n \frac{\partial u}{\partial x_j}\frac{\partial x_j}{\partial t_i} .
> $$

^pf-110-3

*Uses:* [[§109 Tangent Planes and Linear Approximations#^def-109-6|Def. §109.6]], [[§110 The Chain Rule#^thm-110-1|§110.1]] (same argument)

There are $n$ terms, one for each intermediate variable. For example, if $w = f(x, y, z, t)$ with $x = x(u, v)$, $y = y(u, v)$, $z = z(u, v)$, $t = t(u, v)$, then ($n = 4$, $m = 2$)
$$
\frac{\partial w}{\partial u} = \frac{\partial w}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial w}{\partial y}\frac{\partial y}{\partial u} + \frac{\partial w}{\partial z}\frac{\partial z}{\partial u} + \frac{\partial w}{\partial t}\frac{\partial t}{\partial u} ,
$$
and similarly for $\partial w / \partial v$; the tree diagram has four branches from $w$, each splitting into $u$ and $v$ (Stewart, Example 14.5.4).

> [!example] Example §130.3: Three Intermediate Variables
> If $u = x^4 y + y^2 z^3$, where $x = rse^t$, $y = rs^2 e^{-t}$ and $z = r^2 s \sin t$, find the value of $\partial u / \partial s$ when $r = 2$, $s = 1$, $t = 0$.
>
> The tree diagram has branches from $u$ to $x$, $y$, $z$, and from each of these to $r$, $s$, $t$. Following the three paths from $u$ to $s$:
>
> $$
> \begin{aligned}
> \frac{\partial u}{\partial s} &= \frac{\partial u}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial u}{\partial y}\frac{\partial y}{\partial s} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial s} \\
> &= (4x^3 y)(re^t) + (x^4 + 2yz^3)(2rse^{-t}) + (3y^2 z^2)(r^2 \sin t) .
> \end{aligned}
> $$
>
> When $r = 2$, $s = 1$, $t = 0$: $x = 2$, $y = 2$, $z = 0$, and
>
> $$
> \frac{\partial u}{\partial s} = (4 \cdot 8 \cdot 2)(2) + (16 + 0)(4) + (0)(0) = 128 + 64 = 192 .
> $$
>
> *Stewart: Example 14.5.5*

^ex-110-3

> [!example] Example §131.1: The Chain Rule with an Unspecified Function
> **(a)** If $g(s, t) = f(s^2 - t^2, t^2 - s^2)$ and $f$ is differentiable, show that $g$ satisfies $t\,\dfrac{\partial g}{\partial s} + s\,\dfrac{\partial g}{\partial t} = 0$.
>
> Let $x = s^2 - t^2$ and $y = t^2 - s^2$, so $g(s, t) = f(x, y)$. By Case 2,
>
> $$
> \frac{\partial g}{\partial s} = \frac{\partial f}{\partial x}(2s) + \frac{\partial f}{\partial y}(-2s) , \qquad
> \frac{\partial g}{\partial t} = \frac{\partial f}{\partial x}(-2t) + \frac{\partial f}{\partial y}(2t) .
> $$
>
> Therefore
>
> $$
> t\,\frac{\partial g}{\partial s} + s\,\frac{\partial g}{\partial t} = \Big( 2st\,\frac{\partial f}{\partial x} - 2st\,\frac{\partial f}{\partial y} \Big) + \Big( -2st\,\frac{\partial f}{\partial x} + 2st\,\frac{\partial f}{\partial y} \Big) = 0 .
> $$
>
> **(b)** If $z = f(x, y)$ has continuous second-order partial derivatives and $x = r^2 + s^2$, $y = 2rs$, find $\partial z / \partial r$ and $\partial^2 z / \partial r^2$.
>
> By Case 2,
>
> $$
> \frac{\partial z}{\partial r} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial r} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial r} = 2r\,\frac{\partial z}{\partial x} + 2s\,\frac{\partial z}{\partial y} .
> $$
>
> By the Product Rule,
>
> $$
> \frac{\partial^2 z}{\partial r^2} = \frac{\partial}{\partial r}\Big( 2r\,\frac{\partial z}{\partial x} + 2s\,\frac{\partial z}{\partial y} \Big) = 2\,\frac{\partial z}{\partial x} + 2r\,\frac{\partial}{\partial r}\Big( \frac{\partial z}{\partial x} \Big) + 2s\,\frac{\partial}{\partial r}\Big( \frac{\partial z}{\partial y} \Big) . \qquad (4)
> $$
>
> The key point: $\partial z / \partial x$ and $\partial z / \partial y$ are again functions of $x$ and $y$, hence of $r$ and $s$, so the Chain Rule applies to them too:
>
> $$
> \frac{\partial}{\partial r}\Big( \frac{\partial z}{\partial x} \Big) = \frac{\partial^2 z}{\partial x^2}(2r) + \frac{\partial^2 z}{\partial y\,\partial x}(2s) , \qquad
> \frac{\partial}{\partial r}\Big( \frac{\partial z}{\partial y} \Big) = \frac{\partial^2 z}{\partial x\,\partial y}(2r) + \frac{\partial^2 z}{\partial y^2}(2s) .
> $$
>
> Putting these into (4) and using the equality of the mixed partials (Clairaut's Theorem, [[§108 Partial Derivatives#^thm-108-2|Theorem §108.2]]),
>
> $$
> \frac{\partial^2 z}{\partial r^2} = 2\,\frac{\partial z}{\partial x} + 4r^2\,\frac{\partial^2 z}{\partial x^2} + 8rs\,\frac{\partial^2 z}{\partial x\,\partial y} + 4s^2\,\frac{\partial^2 z}{\partial y^2} .
> $$
>
> *Stewart: Examples 14.5.6 and 14.5.7*

^ex-110-4

## Implicit Differentiation

> [!theorem] Theorem §131.2: Implicit Differentiation, One Equation in Two Variables
> Suppose that an equation $F(x, y) = 0$ defines $y$ implicitly as a differentiable function of $x$, that is, $y = f(x)$ with $F(x, f(x)) = 0$ for all $x$ in the domain of $f$. If $F$ is differentiable and $F_y \ne 0$, then
>
> $$
> \frac{dy}{dx} = -\frac{\partial F / \partial x}{\partial F / \partial y} = -\frac{F_x}{F_y} . \qquad (5)
> $$
>
> *Stewart: 14.5, Equation 5*

^thm-110-4

> [!proof]+ Proof
> Apply Case 1 of the Chain Rule ([[§110 The Chain Rule#^thm-110-1|Theorem §110.1]], with $x$ itself as the parameter) to both sides of $F(x, y) = 0$, where $x = x$ and $y = f(x)$ are differentiable functions of $x$:
>
> $$
> \frac{\partial F}{\partial x}\frac{dx}{dx} + \frac{\partial F}{\partial y}\frac{dy}{dx} = 0 .
> $$
>
> Since $dx/dx = 1$ and $\partial F / \partial y \ne 0$, we can solve for $dy/dx$ and obtain (5).

^pf-110-4

*Uses:* [[§110 The Chain Rule#^thm-110-1|§110.1]]

The proof *assumes* that $F(x, y) = 0$ defines $y$ as a differentiable function of $x$. The Implicit Function Theorem ([[§110 The Chain Rule#^thm-110-6|Theorem §110.6]] below) gives conditions under which this assumption is valid.

> [!theorem] Theorem §131.3: Implicit Differentiation, One Equation in Three Variables
> Suppose that $z$ is given implicitly as a function $z = f(x, y)$ by an equation $F(x, y, z) = 0$, that is, $F(x, y, f(x, y)) = 0$ for all $(x, y)$ in the domain of $f$. If $F$ and $f$ are differentiable and $F_z \ne 0$, then
>
> $$
> \frac{\partial z}{\partial x} = -\frac{\partial F / \partial x}{\partial F / \partial z} = -\frac{F_x}{F_z} ,
> \qquad
> \frac{\partial z}{\partial y} = -\frac{\partial F / \partial y}{\partial F / \partial z} = -\frac{F_y}{F_z} . \qquad (6)
> $$
>
> *Stewart: 14.5, Equations 6*

^thm-110-5

> [!proof]+ Proof
> Differentiate both sides of $F(x, y, z) = 0$ with respect to $x$, holding $y$ fixed, by the general Chain Rule ([[§110 The Chain Rule#^thm-110-3|Theorem §110.3]], with intermediate variables $x$, $y$, $z$ and independent variables $x$, $y$):
>
> $$
> \frac{\partial F}{\partial x}\frac{\partial x}{\partial x} + \frac{\partial F}{\partial y}\frac{\partial y}{\partial x} + \frac{\partial F}{\partial z}\frac{\partial z}{\partial x} = 0 .
> $$
>
> But $\frac{\partial}{\partial x}(x) = 1$ and $\frac{\partial}{\partial x}(y) = 0$, so this becomes
>
> $$
> \frac{\partial F}{\partial x} + \frac{\partial F}{\partial z}\frac{\partial z}{\partial x} = 0 .
> $$
>
> If $\partial F / \partial z \ne 0$, solving for $\partial z / \partial x$ gives the first formula in (6). Differentiating with respect to $y$ instead gives the second.

^pf-110-5

*Uses:* [[§110 The Chain Rule#^thm-110-3|§110.3]]

The same assumption is made here: that $F(x, y, z) = 0$ defines $z$ as a differentiable function of $x$ and $y$.

> [!theorem] Theorem §110.6: The Implicit Function Theorem
> **(a) Two variables.** If $F$ is defined on a disk containing $(a, b)$, where $F(a, b) = 0$, $F_y(a, b) \ne 0$, and $F_x$ and $F_y$ are continuous on the disk, then the equation $F(x, y) = 0$ defines $y$ as a function of $x$ near the point $(a, b)$, and the derivative of this function is given by Equation (5).
>
> **(b) Three variables.** If $F$ is defined within a sphere containing $(a, b, c)$, where $F(a, b, c) = 0$, $F_z(a, b, c) \ne 0$, and $F_x$, $F_y$ and $F_z$ are continuous inside the sphere, then the equation $F(x, y, z) = 0$ defines $z$ as a function of $x$ and $y$ near the point $(a, b, c)$, and this function is differentiable, with partial derivatives given by Equations (6).
>
> *Stewart: 14.5 (text)*

^thm-110-6

*Stewart omits the proof ("proved in advanced calculus"); see [[§15 The Implicit Function Theorem#^thm-15-1|452 Thm. §15.1]] for (a) and [[§15 The Implicit Function Theorem#^thm-15-2|452 Thm. §15.2]] for (b).*

> [!remark]- Connections
> - Rigorous treatment: [[§15 The Implicit Function Theorem#^thm-15-1|452 Thm. §15.1]] (two variables, with formula (5) for the derivative) and [[§15 The Implicit Function Theorem#^thm-15-2|452 Thm. §15.2]] (one equation in $n + 1$ variables); hub [[Implicit Function Theorem]]. The circle $x^2 + y^2 = 1$ near $(1, 0)$, where $F_y = 0$ and $y$ is not a function of $x$, shows why the hypothesis $F_y \ne 0$ matters: [[§15 The Implicit Function Theorem#^ex-15-2|452 Ex. §15.2]].

> [!example] Example §131.2: Implicit Differentiation by Formula
> **(a)** Find $y'$ if $x^3 + y^3 = 6xy$.
>
> Write the equation as $F(x, y) = x^3 + y^3 - 6xy = 0$. By (5),
>
> $$
> \frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{3x^2 - 6y}{3y^2 - 6x} = -\frac{x^2 - 2y}{y^2 - 2x} .
> $$
>
> Compare the implicit differentiation of the folium of Descartes in [[§21 Implicit Differentiation#^ex-21-2|Example §21.2]].
>
> **(b)** Find $\partial z / \partial x$ and $\partial z / \partial y$ if $x^3 + y^3 + z^3 + 6xyz + 4 = 0$.
>
> Let $F(x, y, z) = x^3 + y^3 + z^3 + 6xyz + 4$. By (6),
>
> $$
> \frac{\partial z}{\partial x} = -\frac{F_x}{F_z} = -\frac{3x^2 + 6yz}{3z^2 + 6xy} = -\frac{x^2 + 2yz}{z^2 + 2xy} ,
> \qquad
> \frac{\partial z}{\partial y} = -\frac{F_y}{F_z} = -\frac{3y^2 + 6xz}{3z^2 + 6xy} = -\frac{y^2 + 2xz}{z^2 + 2xy} ,
> $$
>
> the same as in [[§108 Partial Derivatives#^ex-108-4|Example §108.4]], with less work.
>
> **(c)** For the ellipsoid $x^2 + \dfrac{y^2}{9} + \dfrac{z^2}{4} = 1$, calculate $z_x$ and $z_y$ at an arbitrary point $(x, y, z)$ of the surface, wherever possible.
>
> Let $F(x, y, z) = x^2 + \frac{y^2}{9} + \frac{z^2}{4} - 1$, so $F_x = 2x$, $F_y = \frac{2y}{9}$, $F_z = \frac{z}{2}$. Where $z \ne 0$,
>
> $$
> z_x = -\frac{2x}{z/2} = -\frac{4x}{z} , \qquad z_y = -\frac{2y/9}{z/2} = -\frac{4y}{9z} .
> $$
>
> At the points with $z = 0$ (the ellipse $x^2 + y^2/9 = 1$ in the $xy$-plane) the tangent plane is vertical, and $z$ is not a differentiable function of $(x, y)$ there.
>
> *In the answer key's second line, $\partial z / \partial x$ is written where $\partial z / \partial y$ is meant: the line should read $\frac{2y}{9} + \frac{z}{2}\frac{\partial z}{\partial y} = 0$; the answers $-4x/z$ and $-4y/(9z)$ are correct. This part appears only in the answer key, not in the posted exam.*
>
> *Stewart: Examples 14.5.8 and 14.5.9*
> *Source: 233 Practice Exam 1, Q4(c) (answer key)*

^ex-110-5

*Chain: the folium of Descartes earlier in [[§21 Implicit Differentiation#^ex-21-2|Chapter 3]].*
